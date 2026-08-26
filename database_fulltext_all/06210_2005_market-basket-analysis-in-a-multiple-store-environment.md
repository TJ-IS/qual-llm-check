---
otero_id: 6210
otero_key: "E2B3PVHS"
title: "Market basket analysis in a multiple store environment"
authors: "Yen-Liang Chen; Kwei Tang; Ren-Jie Shen; Ya-Han Hu"
year: "2005"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2004.04.009"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dsw

# Market basket analysis in a multiple store environment

Yen-Liang Chen<sup>a</sup>, Kwei Tang<sup>b,</sup>\*, Ren-Jie Shen<sup>a</sup>, Ya-Han Hu<sup>a</sup>

<sup>a</sup> Department of Information Management, National Central University, Chung-Li, 320 Taiwan, ROC <sup>b</sup> Krannert Graduate School of Management, Purdue University, West Lafayette, IN 47907, USA

Received 1 December 2003; received in revised form 5 April 2004; accepted 5 April 2004 Available online 2 June 2004

## Abstract

Market basket analysis (also known as association-rule mining) is a useful method of discovering customer purchasing patterns by extracting associations or co-occurrences from stores’ transactional databases. Because the information obtained from the analysis can be used in forming marketing, sales, service, and operation strategies, it has drawn increased research interest. The existing methods, however, may fail to discover important purchasing patterns in a multi-store environment, because of an implicit assumption that products under consideration are on shelf all the time across all stores. In this paper, we propose a new method to overcome this weakness. Our empirical evaluation shows that the proposed method is computationally efficient, and that it has advantage over the traditional method when stores are diverse in size, product mix changes rapidly over time, and larger numbers of stores and periods are considered. <sup>D</sup> 2004 Elsevier B.V. All rights reserved.

Keywords: Association rules; Data mining; Store chain; Algorithm

## 1. Introduction

Because of advances in information and communication technologies, corporations can effectively obtain and store transactional and demographic data on individual customers at reasonable costs. One of the challenges for corporations that have invested heavily in customer data collection is how to extract important information from their vast customer databases in order to gain competitive advantage. Market basket analysis (also known as association rule mining) is a method of discovering customer purchasing patterns by extracting associations or co-occurrences from stores’ transactional databases. Discovering, for example, that supermarket customers are likely to purchase milk, bread, and cheese together, or that bank customers are likely to use a set of services jointly, can help managers in designing store layout, web sites, product mix and bundling, and other marketing strategies.

The methodology was introduced by Agrawal et al. [2] and can be stated as follows. Given two nonoverlapping subsets of product items, X and Y, an association rule in form of X ! Y indicates a purchase pattern that if a customer purchases X then he or she also purchases Y. Two measures, support and confidence, are commonly used to select the association rules. Support is a measure of how often the transactional records in the database contain both X and Y, and confidence is a measure of the accuracy of the rule, defined as the ratio of the number of transactional records with both X and Y to the number of transactional records with X only. By far, the Apriori algorithm [1] is the most known algorithm for mining the association rules from a transactional database, which satisfy the minimum support and confidence levels specified by users.

Since association rules are useful and easy to understand, there have been many successful business applications, including, for example, finance, telecommunication, marketing, retailing, and web analysis [5]. The method has also attracted increased research interest, and many extensions have been proposed in recent years, including (1) algorithm improvements [6,12,18,21]; (2) fuzzy rules [13,14]; (3) multi-level and generalized rules [7,10]; (4) quantitative rules [20,24,25]; (5) spatial rules [7,15]; (6) inter-transaction rules [19]; (7) interesting rules [4,9]; and (8) temporal association rules [3,16,17]. Brief literature reviews of association rules are given by Chen et al. [8] and Han and Kamber [11].

In today’s business world, it is common for a company to have subsidiaries, branches, dealers, or franchises in different geographical locations. For example, Wal-Mart, the largest supermarket chain in the world, has more than 4400 stores worldwide. For a company with multiple stores, discovery of purchasing patterns that may vary over time and exist in all, or in subsets of, stores can be useful in forming marketing, sales, service, and operation strategies at the company, local, and store levels.

There are two main problems in using the existing methods in a multi-store environment. The first is caused by the temporal nature of purchasing patterns. An apparent example is seasonal products. Temporal rules [3,16,17] are developed to overcome the weakness of the static association rules that either find patterns at a point of time or implicitly assume the patterns stay the same over time and across stores. A literature review on temporal rules is given by Roddick and Spiliopoulou [22]. In temporal rules, selling periods are considered in computing the support value, where the selling period of a product is defined as the time between its first and last appearances in the transaction records. Furthermore, the common selling period of the products in a product set is used as the base in computing the ‘‘temporal support’’ of the product set. The results of the method may be biased, however, because a product may be on shelf before its first transaction and/or after the last transaction occurs, and a product may also be put on-shelf and taken off-shelf multiple times during the data collection period.

The second problem is associated with finding common association patterns in subsets of stores. Similar to the problem in using existing temporal rules in a multi-store environment, we have to consider the possibility that some products may not be sold in some stores, for example, because of geographical, environmental, or political reasons. This is seemingly related to spatial association rules. However, the focus of spatial rules is on finding the association patterns that are related to topological or distance information in, for example, maps, remote sensing or medical imaging data and VLSI chip layout data [23].

To overcome the problems, we develop an Apriorilike algorithm for automatically extracting association rules in a multi-store environment. The format of the rules is similar to that of the traditional rules. However, the rules also contain information on store (location) and time where the rules hold. The results of the proposed method may contain rules that are applicable to the entire chain without time restriction or to a subset of stores in specific time intervals. For example, a rule may state: ‘‘In the second week of August, customers purchase computers, printers, Internet and wireless phone services jointly in electronics stores near campus.’’ Another example is: ‘‘In January, customers purchase cold medicine, humidifiers, coffee, and sunglasses together in supermarkets near skiing resorts.’’ These rules can be used not only for general or localized marketing strategies, but also for product procurement, inventory, and distribution strategies for the entire store chain. Furthermore, we allow an item to have multiple selling time periods; i.e., an item may be put on-shelf and taken off-shelf multiple times. We further assume that different stores can have different product-mixes in different time periods. That is, each store can have its own product-mix, and the product-mix in a store can be dynamically changed over time.

Because the time and store (location) factors are considered, the rule generation procedure is more complicated than the Apriori algorithm. The simulation results presented in the paper show that the proposed method is computationally efficient and has significant advantage over the traditional association method when the stores under consideration are diverse in size and have product mixes that change rapidly over time.

The paper is organized as follows. We formally define the problem in Section 2 and in Section 3 propose an algorithm. In Section 4, we compare the results generated from the proposed algorithm and the traditional Apriori algorithm in a simulated multi-store environment. The conclusion is given in Section 5.

## 2. Problem definition

We consider a market basket database D that contains transactional records from multiple stores over time period T. Our objective is to extract the association rules from the database. For convenience in presentation, the cardinal of a set, say R, is denoted by ARA. Let $I { = } \{ I _ { 1 } , ~ I _ { 2 } , . ~ . ~ . , ~ I _ { r } \}$ be the set of product items included in $D ,$ where $I _ { k } \ ( 1 \leq k \leq r )$ is the identifier for the kth item. Let X be a set of items in I. We refer X as a k-itemset if $| X | = k .$ . Furthermore, a transaction, denoted by $s ,$ is a subset of I. We use ${ \it W ( X , D ) = \{ s | s \in D \land X \subseteq s \} }$ to denote the set of transactions in D, which contain itemset X.

Definition 1. The support of X, denoted by $s u p ( \boldsymbol { X } , D )$ is the fraction of transactions containing X in database $D ;$ $\mathrm { i . e . , } s u p ( X , D ) \mathrm { = } \mid W ( X , D ) \mid / \mid D \mid$ . For a specified support threshold $\sigma _ { \mathrm { { s } } } ,$ X is a frequent itemset if sup(X, $D ) \geq \sigma _ { \mathrm { { s } } }$

Note that the definitions of the support and the frequent itemset are those used in the traditional association rules, and, therefore, the store and time information is not considered in determining the support of an itemset.

Let $\{ T _ { 1 } , T _ { 2 } , . . . , T _ { m } \}$ be the set of mutually disjoint time intervals (periods) and form a complete partition of T. Furthermore, they are ordered, such that $T _ { i + 1 }$ immediately follows $T _ { i }$ for i <sub>z</sub> 1. Note that the time periods are defined according to specific needs of the problem, such as 1 h, 6 h, 1 day, 1 week, and so on. Let $P { = } \{ P _ { 1 } , P _ { 2 } , . . . , P _ { q } \}$ be the set of stores, where $P _ { j }$ $( 1 \leq j \leq q )$ denotes the jth store in the store chain. We assume that each transaction s in D is attached with a timestamp, t, and store identifier, $p ,$ to indicate the store and time that the transaction occurs.

Let $S _ { k } \subseteq P$ and $R _ { k } \subseteq T$ be the sets of the stores and times that item $I _ { k }$ is sold, respectively. We define $V _ { I _ { k } } { = } S _ { k } \times R _ { k }$ as the context of item $I _ { k } ;$ i.e., the set of the combinations of stores and times where item $I _ { k }$ is sold. Furthermore, the context of itemset $X ,$ denoted by $V _ { X } ,$ is the set of the combinations of stores and times that all items in X are sold concurrently. For example, if itemset X consists of two items $I _ { k }$ and $I _ { k ^ { \prime } }$ the context of X is given by $V _ { X } = V _ { I k } \cap V _ { i k } ,$

Definition 2. Let X be an itemset in I with context $V _ { X } ,$ and $D _ { V _ { X } }$ the subset of transactions in D whose timestamps t and store identifiers $p$ satisfy $V _ { X } .$ We define the relative support of X with respect to the context $V _ { X }$ denoted by rel<sup>\_</sup>sup(X, $D _ { V _ { \chi } } )$ , as $\mid W$ (X, $D _ { V _ { \chi } } ) \lvert / \rvert D _ { V _ { \chi } } \lvert$ . For a given threshold for relative support $\sigma _ { \mathrm { r } }$ if a frequent itemset X satisfies rel<sup>\_</sup>sup(X, $D _ { V _ { X } } ) \geq \sigma _ { \mathrm { r } } ,$ we call X a relative-frequent (RF) itemset.

In the last definition, we require that a relativefrequent itemset X be frequent. We add this restriction for two reasons. First, it enables us to preserve the well-known downward-closure property, by which the candidate set of the next phase can be obtained by joining the frequent sets of the preceding phase; this will greatly improve the performance of the algorithm. Second, this restriction does not present any real problem to the mining algorithm, because none of the important patterns would be missing because of using a low $\sigma _ { \mathrm { { s } } }$ value. Therefore, we prefer using a low $\sigma _ { \mathrm { s } }$ value. However, it should not be too low because an itemset that occurs only in few transactions has no practical significance.

Furthermore, the minimum threshold for the relative support of an itemset is used to determine whether a sufficient percentage of transactions exists in its context to warrant the inclusion of the itemset as a relative-frequent (RF) itemset. Its use and purpose are similar to those of the traditional minimum support threshold. Consequently, we can set its value the same way as we set the traditional minimum support threshold.

Definition 3. Consider two itemsets X and Y. The relative support of X with respect to the context $V _ { x \cup y }$ denoted by rel<sup>\_</sup>sup(X, $D _ { V _ { \scriptscriptstyle { X \bigcup Y } } } )$ , is defined as AW(X, $D _ { V _ { \scriptscriptstyle { X \cup Y } } } ) \lvert / \lvert D _ { V _ { \scriptscriptstyle { X \cup Y } } } \rvert .$ . The confidence of rule $X { \Rightarrow } Y ,$ denoted by $c o n f ( X {  } Y )$ , is defined as rel<sup>\_</sup>sup(X[Y, $D _ { V _ { \scriptscriptstyle X \cup Y } } ) / r e l \_ s u p ( X , D _ { V _ { \scriptscriptstyle X \cup Y } } ) .$

The above definition implies that the context of rule $X { \Rightarrow } Y$ is $V _ { x \cup y } ;$ i.e., the base used to compute the confidence of rule $X { \Rightarrow } Y$ is the common stores and time periods shared by all the items in X[Y.

Definition 4. Let Z be an RF itemset, where $Z = X \cup Y ,$ $X \subseteq I ,$ and $Y \subseteq I \backslash X .$ Given a confidence threshold $\sigma _ { \mathrm { { c } } } ,$ if $c o n f ( X { \Rightarrow } Y ) { \geq } \sigma _ { \mathrm { c } } ,$ , we call $X { \Rightarrow } Y$ a store-chain (SC) association rule, and $V _ { x \cup y }$ as the context of the rule.

Based on Definitions 1 and 4, it is clear that the selection criteria and outputs for the store-chain association rules are different from those of the traditional association rules. For the store chain rules, the output includes the confidence, support, and a context indicating the stores and times the rules hold.

It can be shown that the traditional method underestimates the support and the confidence values (a proof is given in Appendix A). Consequently, important purchasing patterns that satisfy the criteria of the SC association rules may not be identified by the traditional association-rule methods.

## 3. Algorithm

We propose an Apriori-like algorithm for mining the store-chain association rules. The algorithm is outlined in Fig. 1. We first explain the general concept for developing the algorithm and then use five subsections to give detailed information on several key steps of the algorithm.

In describing the algorithm, we use $R F _ { k }$ to denote the set of all relative-frequent k-itemsets; $F _ { k } ,$ the set of all frequent k-itemsets; and $C _ { k } ,$ the set of candidate k-itemsets. Note that, in the traditional Apriori algorithm, a k-item candidate itemset must be a combination of k  1 frequent itemsets because of the anti-monotone property [1]. Therefore, the Apriori algorithm can generate the candidate itemsets in the kth phase by joining the frequent itemsets in the (k  1)th phase. However, for the SC association rule, a subset of an RF itemset may not be an RF itemset because the base for calculating the relative support value varies in different phases. Consequently, in the proposed algorithm, we generate candidate itemsets from the frequent itemsets, instead of the

RF itemsets. Furthermore, when we use the frequent itemsets to generate the candidate set in the next phase, it still satisfies the anti-monotone property, because we use the same base to compute the supports for all itemsets.

As the first step of the algorithm, we build a table, called the PT table, for each item in I to associate the item with its context (i.e., the stores and times it is sold) and use the table to determine the context of an itemset. The algorithm proceeds in phases, where in the kth phase we generate $F _ { k }$ from $C _ { k }$ and $R F _ { k }$ from $F _ { k } .$ In the first phase, we scan the database for the first time and build a two-dimensional table, called the TS $t a b l e$ . In this table, the entry at the position corresponding to $T _ { i }$ and $P _ { j } ,$ denoted by $\mathrm { T S } ( T _ { i } , \ P _ { j } )$ records the number of transactions that occur at store $P _ { j }$ in period $T _ { i \cdot }$ . Using this table and the PT table for a given itemset $X ,$ we can determine the number of transactions associated with the context of X, i.e., $\lvert D _ { V _ { x } } \rvert$ . In the kth phase of the algorithm, we first derive $C _ { k } ,$ and, then, generate $F _ { k }$ by evaluating their supports, which can be done by scanning the database and removing all infrequent itemsets. Since an RF itemset must be a frequent itemset, we generate $R F _ { k }$ from $F _ { k }$ by evaluating the relative supports of the itemsets X in $F _ { k } .$

In the following subsections, we give detailed descriptions for the key elements of the algorithm, including methods of (1) building the PT table, (2) building the TS table in the first phase, (3) finding $\mathrm { R F } _ { k } ,$ (4) generating candidate itemsets, and (5) generating the store-chain association rules.

## 3.1. The PT table

The purpose of the PT table is to efficiently store the time and store information for each product item in the database. We use a simple example to illustrate the procedure for constructing the table. Consider the bit matrices in Fig. 2 for items $I _ { 1 } , I _ { 2 } $ , and $I _ { 3 } ,$ in which there are six stores and six selling periods, and $^ { \ 6 \ } 1 ^ { , 9 }$ and $^ { 6 6 } 0 ^ { , 9 }$ indicate, respectively, that the item is or is not for sale in the corresponding store and time.

Because an item normally does not switch between on- and off-shelf very frequently in a typical application, we store an item’s context information in the PT table instead of the bit matrix in order to conserve data storage space. In the PT table, we need only to record

1. For each $I _ { m } ,$ construct the PT table;

2. For all transactions s in database D

3. { add 1 to the support count of 1-itemset c contained in s

4. increase the value at $T S ( T _ { i } , P _ { j } )$ by 1 where the time of s is in $T _ { i }$ and the store of s is at $P _ { j } ; \}$

5. ${ \cal F } _ { 1 } { = } \{ c | c | \ c . \mathrm { c o u n t } \ n | \ n | \geq \sigma _ { s } \}$

6. For $( k { = } 2 ; F _ { k - 1 } { \neq } \emptyset ; k { + } { + } )$

7. $\{ C _ { k } { = } C a n d G e n ( F _ { k - 1 } ) ;$

8. I $\dot { k } > 2$ then for each z in $R F _ { k - 1 }$ built its PT table

9. For all transactions s in D

10. {add 1 to the support counts of candidates c in $C _ { k }$ contained in $s ;$

11. add 1 to the support counts of all subsets x of each z in $R F _ { k - 1 }$ w.r.t. $V _ { \zeta } ; \}$

12. Fk={c in $C _ { k }$ and (c.count $/ \left| D \right| ) \geq \sigma _ { s } \}$

13. $R F _ { k } { = } \{ g$ in $F _ { k }$ and (g.count $/ | D _ { V _ { g } } | ) \geq \sigma _ { r } \}$

14. compute the confidence of $x \Longrightarrow y$ where x ∪ y in $R F _ { k - 1 } ;$

15. For each (x ∪ y) in $R F _ { k - 1 }$

16. {if conf(x ⇒ y) ≥ σc

17. output $x \Longrightarrow y$ with context $V _ { X \cup Y } ; \}$ 18. }

Fig. 1. Algorithm Apriori<sup>\_</sup>TP.

<table><tr><td rowspan="2">Store\Time</td><td colspan="6">Item  $I_1$ </td><td colspan="6">Item  $I_2$ </td><td colspan="6">Item  $I_3$ </td></tr><tr><td> $T_1$ </td><td> $T_2$ </td><td> $T_3$ </td><td> $T_4$ </td><td> $T_5$ </td><td> $T_6$ </td><td> $T_1$ </td><td> $T_2$ </td><td> $T_3$ </td><td> $T_4$ </td><td> $T_5$ </td><td> $T_6$ </td><td> $T_1$ </td><td> $T_2$ </td><td> $T_3$ </td><td> $T_4$ </td><td> $T_5$ </td><td> $T_6$ </td></tr><tr><td> $P_1$ </td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td> $P_2$ </td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td></tr><tr><td> $P_3$ </td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td> $P_4$ </td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td></tr><tr><td> $P_5$ </td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td> $P_6$ </td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td></tr></table>

Fig. 2. Bit matrices for $I _ { 1 } ,$ , $I _ { 2 } ,$ and $I _ { 3 } .$

![](/api/attachments/E2B3PVHS/fulltext/images/4e35e8d9506879c091475c0f2073ff7f789d9fadba4da96dd43836760d72957f.jpg)  
Fig. 3. The PT tables for $I _ { 1 } , I _ { 2 } ,$ and $I _ { 3 } .$

the time that the item changes its status between onshelf and off-shelf. (Initially, we assume that the item is on-shelf in all the stores.) For example, in Store $P _ { 1 }$ item $I _ { 1 }$ changes its status only in time $T _ { 4 } .$ . Therefore, we need only to record $" 4 >$ in the PT table to reflect the time and store information for item $I _ { 1 }$ in Store $P _ { 1 }$ Following this procedure, the information of the original bit matrices for items $I _ { 1 } , \ I _ { 2 } ,$ , and $I _ { 3 }$ is converted into the PT tables shown in Fig. 3.

As mentioned previously, the PT tables for individual items can be used to determine the PT table for a given itemset. The procedure given in Fig. 4 shows how to generate the jth row (store) of the PT table for an itemset X by combining the jth rows of the PT tables for all items in the itemset. We start with an mdimension bit array, denoted by $P T _ { j } ,$ for the itemset with initial values of $^ { \ 6 \ } 1 ^ { \ 9 }$ for each of the m time periods. These initial values are replaced by ‘‘0’’ found at the corresponding position in the PT tables for all the items in the itemset. Finally, we transform $P T _ { j }$ into $\operatorname { P T } ( X , j )$ , the jth row of the PT table for itemset X.

Let us use an itemset consisting of $I _ { 1 }$ and $I _ { 2 }$ as an example. In order to generate the second row (store) of the PT table, we start with an initial bit array: [1 1 1 1 1 1]. Since the corresponding row of the PT table for $I _ { 2 }$ is [1 2 5], the first, fifth, and sixth elements of the bit array are replaced by $^ { 6 6 } 0 ^ { , 9 }$ , resulting a new bit array: [0 1 1 1 0 0]. Following the same method, the third through the sixth elements of the new bit array are replaced $\mathrm { b y } \ ^ { \mathrm { * } } 0 ^ { \mathrm { * } }$ when $I _ { 2 }$ is considered. As a result, the final bit array is $[ 0 ~ 1 ~ 0 ~ 0 ~ 0 ~ 0 ]$ , and the corresponding (second) row of the PT table for the itemset is [1 2 3].

Using the concept described above, we develop the procedure in Fig. 4. In the procedure, $\mathrm { P T } ( k , j )$ denotes the jth row of the PT table for item $k ,$ and its <sup>S</sup> th element is $\mathrm { P T } ( k , j , \ell )$ , where $\ell$ is an odd number. The elements of $P T _ { j }$ are replaced by 0’s according to the rule stated in lines 4 through 6 in the algorithm: a segment of $\mathrm { P T } _ { j }$ is replaced by $^ { \circ } 0 ^ { \circ }$ , starting from position $\operatorname { P T } ( k , j , \ell )$ and ending at position $\mathrm { P T } ( k , j ,$ $\ell + 1 ) - 1 . \operatorname { P T } ( k , j )$ is inserted in sequence into $P T _ { j }$ for every item j in itemset X. The process of developing the PT table is included as line 8 in the algorithm given in Fig. 1.

## 3.2. The TS table

After building the PT table, the first phase of the algorithm is to build the TS table, where each entry at the position corresponding to $T _ { i }$ and $P _ { j }$ is the number of transactions that occur at store $P _ { j }$ in period $T _ { i \cdot }$ This can be done by a scan through the database. An

1) Fill 1's into the array of $P T _ { j } ;$

2) For every item k in X

3) n1=the number of elements in $P T ( k , j )$

4 for $( \ \ell = 1 \ ; \ell \leq n 1 \ ; \ell + 2 \ )$

5) $\mathrm { f o r } ~ ( ~ i = P T ( k , j , \ell ) ; i < P T ( k , j , \ell + 1 ) \mathrm { ~ a n d ~ } i \le m ; i + + ~ )$

6) PTj [i]=0; /\* PTj [i] is the i-th bit of array PTj \*/

7) Transform $P T _ { j }$ into $P T ( X , j )$

Fig. 4. The method to compute the jth row of the PT table for itemset X.

example of the table is given in Fig. 5. Using the TS and PT tables for itemset X, we can determine the value $| D _ { V _ { X } } |$ by summing all the values in the entries of the TS table according to the store and time information of the items in X. The process of constructing the table is described in lines 2 through 4 in Fig. 1.

## 3.3. Relative-frequent itemset

Because an RF itemset must be a frequent itemset, we can generate $R F _ { k }$ from $F _ { k }$ by computing the relative supports of those itemsets X in $F _ { k } .$ . It is evident that $\mid W ( X , D _ { V _ { X } } ) \mid$ equals AW(X, D)A because it is not possible for X to appear in a transaction not in $D _ { V _ { \chi } } .$ Further, $\lvert D _ { V _ { X } } \rvert$ can be obtained from the TS and PT tables of X. As a result, we can find the RF itemsets by first computing the relative supports of all X in $F _ { k }$ and then pruning those itemsets whose relative supports are less than $\sigma _ { r }$

## 3.4. Candidate itemsets

As discussed, we generate the candidate itemsets from the frequent itemsets, instead of the RF itemsets, from the last phase. Furthermore, when we use the frequent itemsets to generate the candidate set in the next phase, it still satisfies the anti-monotone property, because we use the same base to compute the supports for all itemsets. We illustrate the computation process by the following example.

Example 1. Suppose there are 15 periods, from $T _ { 1 }$ to $T _ { 1 5 } ,$ and the numbers of transactions occurring in these 15 periods are 19, 17, 14, 25, 20, 17, 15, 27, 21, 20, 22, 18, 25, 21, and 19, respectively. Assume that the selling periods of product A are from $T _ { 1 }$ to $T _ { 1 0 } ,$ and that there are 60 transactions containing product

<table><tr><td></td><td> $T_1$ </td><td> $T_2$ </td><td> $T_3$ </td><td> $T_4$ </td><td> $T_5$ </td><td> $T_6$ </td></tr><tr><td> $P_1$ </td><td>23</td><td>23</td><td>5</td><td>42</td><td>23</td><td>56</td></tr><tr><td> $P_2$ </td><td>93</td><td>42</td><td>12</td><td>39</td><td>47</td><td>23</td></tr><tr><td> $P_3$ </td><td>43</td><td>41</td><td>8</td><td>70</td><td>43</td><td>59</td></tr><tr><td> $P_4$ </td><td>21</td><td>32</td><td>43</td><td>34</td><td>10</td><td>21</td></tr><tr><td> $P_5$ </td><td>32</td><td>42</td><td>30</td><td>64</td><td>34</td><td>32</td></tr><tr><td> $P_6$ </td><td>45</td><td>12</td><td>16</td><td>90</td><td>12</td><td>65</td></tr></table>

Fig. 5. An example of the TS table.

A. Furthermore, assume that the selling periods for product B are from $T _ { 6 }$ to $T _ { 1 5 } .$ , and that 80 transactions of them include product B. Finally, there are 50 transactions containing both products A and B, and they are sold in periods from $T _ { 6 }$ to $T _ { 1 0 }$

In order to compute the supports and the relative supports for itemsets {A}, {B}, and $\{ \mathrm { A } , ~ \mathrm { B } \}$ , we identify the following values: $| \cal { W } ( \{ A \} , \ D \nu _ { \{ A \} } ) | =$ $| W ( \{ \mathrm { A } \} , \ D ) | = 6 0 , | W ( \{ \mathrm { B } \} , \ D \nu _ { \{ \mathrm { B } \} } ) | = | W ( \{ \mathrm { B } \}$ $D ) | = 8 0$ , and $| W ( \{ { \bf A } , ~ { \bf B } \} , D \nu _ { \{ { \bf A } , { \bf B } \} } ) | = | W ( \{ { \bf A } , ~ { \bf B } \}$ $D ) | = 5 0$ . Since the base for computing the support is $\vert D \vert = 3 0 0$ , the supports for the three itemsets are given by sup({A}, D) = 60/300 = 0.2, sup({B}, $D ) = 8 0 / 3 0 0 = 0 . 2 6 7$ , and sup({A, B}, D) = 50/ $3 0 0 = 0 . 1 6 7 _ { \cdot }$ , respectively. On the other hand, the bases for computing the relative support are $| D \nu _ { \{ \mathrm { A } \} } | = 1 9 5 \ /$ $| D \nu _ { \{ { \bf B } \} } | = 2 0 5$ , and $| D \nu _ { \{ \mathrm { A U B } \} } | = 1 0 0$ , respectively, for the three itemsets. As a result, the relative supports a r e re l <sup>\_</sup> s u p ( { A } , $D \nu _  \{ \mathrm { A \} \} } = 6 0 / 1 9 5 = 0 . 3 0 8$ rel<sup>\_</sup>sup({B}, $D \nu _ { \{ \mathrm { B } \} } = 8 0 / 2 0 5 = 0 . 3 9$ , rel<sup>\_</sup>sup({A, B}, $D \nu _ { \{ \mathrm { A , B \} } } ) { = } 5 0 / 1 0 0 { = } 0 . 5$ for the itemsets.

Suppose we set $\sigma _ { s }$ at 0.1 and $\sigma _ { r }$ at 0.35. Then, we find that {A}, {B}, and {A, B} are frequent. Furthermore, {A} is not relative-frequent, but {B} and {A, $| \mathrm { B } \}$ are relative-frequent.

## 3.5. The store-chain association rules

Having found the RF itemsets, we proceed to calculate the confidence values and to find all the SC association rules. As defined in Definition $^ { 3 , }$ the confidence value is given by $c o n f ( X ^ { \Rightarrow } Y ) =$ rel<sup>\_</sup>sup(X[Y, $D _ { V _ { \scriptscriptstyle { X \scriptscriptstyle \mathrm { U } Y } } } ) / r e l _ { - }$ <sup>\_</sup>sup(X, $D _ { V _ { \scriptscriptstyle { X \bigcup Y } } } )$ . If the confidence value exceeds $\sigma _ { \mathrm { { c } } } ,$ the SC association rule holds.

There is an issue that must be dealt with in computing the confidence value. In the calculation of rel<sup>\_</sup>sup(X[Y, $D _ { V _ { _ { X \cup Y } } } ) / r e l \_ s u p ( X , \ D _ { V _ { _ { X \cup Y } } } )$ , we obtain the numerator after the phase of processing X[Y. But the denominator is still undetermined after the phase of processing X[Y, because the length of X is smaller than that of X[Y, and we process the itemsets of the same length in a single phase. One possible solution to this problem is to add one step after the phase of processing X[Y. In this new step, we compute support levels of all subsets of X[Y under the context of $V _ { X \cup { \dot { Y } } }$ i.e., the support levels of X in database $D _ { V _ { \lambda \cup \vec { r } } }$ where X is a subset of X[Y.

If the RF itemset produced in each phase needs another scan to produce the confidence value, then the number of scans of the database in this algorithm is twice that required by the Apriori algorithm. In order to reduce this requirement, we use another method: if Z is an RF itemset found in the kth phase, we compute rel $s u p ( X , D _ { V _ { z } } )$ in the $( k + 1 )$ phase by ‘‘hitchhiking,’’ where X is a subset of Z. In other words, in phase $k + 1$ , we perform two operations: the first is to find the RF itemset of length $k + 1$ , and the second is to compute the relative supports, such as $r e l { \_ } s u p ( X ,$ $D _ { V _ { z } } )$ . All these values are calculated during the same scan of the database. Consequently, the proposed method requires only one more scan than the Apriori algorithm to obtain the confidence value when the RF itemset of the last phase is produced. This process is included as line 11 in the algorithm, and in Fig. 6, we give the process of computing rel<sup>\_</sup>sup(X, $D _ { V _ { z } } )$ for all subsets X of Z.

In order to compute rel<sup>\_</sup>sup(X, $D _ { V _ { z } } )$ for all subsets X of $Z ,$ we must enumerate all the subsets, X, of each RF itemset, $Z ,$ in the previous phase—if the length of the RF itemset is $k ,$ the number of subsets is $2 ^ { \bar { k } } - 2$ Because each Z has its own PT table (built in line 8 of Fig. 1), we need to check whether a transaction happens in the PT tables of all RF itemsets Z every time a transaction is read in, after computing the supports of the candidates in $C _ { k } .$ If not, it indicates that this transaction does not happen under the context of $V _ { z } ,$ and it can be ignored. On the other hand, if the answer is positive, it indicates that this transaction happens under the context of $V _ { z } ,$ and, as a result, we need to check if the transaction includes any subset X of Z. This enables us to determine the support levels of all the subsets X of Z under the context of $V _ { z } .$

For example, suppose that two RF itemsets are generated in the third phase: {A, B, C} and {C, D, E}. In the fourth phase, we build the PT tables for all the RF itemsets in $R F _ { 3 } .$ . And when a transaction is read, we need to check whether it includes any candidates $C _ { 4 } ,$ as well as whether its time and store combination is in the contexts of {A, B, C} or {C, D, E}. If the time and store combination of the transaction does not conform to the context of {A, B, C}, we need to check whether it does to that of {C, D, E}. If it does, we proceed to check whether it includes any subsets like {C, D, E}: {C}, {D}, {E}, {C, D}, {C, E}, and {D, E}. If it does, the counters of all the matching subsets are increased by one.

Finally, line 14 in Fig. 1 shows the step for generating the store chain association rule $X { \Rightarrow } Y ,$ where X[Y is in $\mathrm { R F } _ { k - 1 } .$ It is not difficult to compute the confidence of the rule—i.e., rel<sup>\_</sup>sup(X[Y, $D _ { V _ { \scriptscriptstyle { X + Y } } } ) /$ rel<sup>\_</sup>sup(X, $D _ { V _ { \scriptscriptstyle { X + Y } } } )$ —because rel<sup>\_</sup>sup(X[Y, $D _ { V _ { \scriptscriptstyle { X \bigcup Y } } } )$ has already been found in the previous phase and rel<sup>\_</sup>sup(X, $D _ { V _ { \scriptscriptstyle { X \bigcup Y } } } )$ found in the current phase.

## 3.6. Complexity analysis

In this section, we analyze the time complexity and memory space complexity of the algorithm. Let m be the number of items, n the number of transactions in the database, l the number of items in a transaction. Further, let x denote the largest value of $\vert C _ { k } \vert$ . Note that, although $\vert C _ { k } \vert$ can theoretically be as large as $\mathrm { O } ( m ^ { k } ) , \ | { \cal C } _ { k } |$ is very unlikely to be larger than $\mathrm { O } ( m ^ { 2 } )$ in practice. This is because, in an Apriori-like algo-

1) for each z in $R F _ { k - 1 }$

2) if Time and Store of a transaction s is in the context of $z$

3) for all subsets x of $z$

4) if x⊆s

5) increase count(x,Vz) by 1

Fig. 6. Compute the support counts of all the subsets X of Z.

rithm $[ 1 , 2 , 6 , 2 0 ] , C _ { 2 }$ usually has the largest size among all candidate sets. We discuss the time complexities of the steps of Apriori\_TP algorithm separately, as well as the total time complexity of the algorithm, as follows.

1. In step 1, we construct the PT table for each item. To produce the table for an item, its Bit Matrix table with $\left| P \right|$ rows and $\mid T \mid$ columns needs to be linearly scanned and processed. Thus, the time for step 1 is $\operatorname { O } ( m \times \mid P \mid \times \mid T \mid )$ .

2. In steps 2 to 4, two operations are performed: (1) compute the supports of all itemsets in $C _ { 1 } ,$ , and (2) construct the TS table. Since the first operation requires a linear scan of all the items in every transaction, its time is $\mathrm { O } ( n \times l )$ . The time needed for the second operation is ${ \mathrm { O } } ( n )$ because we examine the attached time and store identifier of each transaction, it requires time O(n). As a result, the total time for the three steps is $\mathrm { O } ( n \times l )$

3. Step 5 is for determining $F _ { 1 }$ by examining the support of every itemset in $C _ { 1 }$ . Since $C _ { 1 }$ has n itemsets, the time needed for the step is O(n).

4. There is a loop from steps 6 to 18. The time complexities of the steps in iteration k of the loop are discussed as follows.

4.1. In step 7, we generate $C _ { k } .$ Consequently, the required time is $\mathrm { O } ( \vert C _ { k } \vert )$ . Because we assume $\mathrm { O } ( | C _ { k } | ) { \le } \mathrm { O } ( \Upsilon )$ , the time is O(x ).

4.2. In step 8, we build a PT table for each itemset z in $R F _ { k - 1 }$ . We need $k - 2$ merging operations for this step because the k  1 PT tables of every individual item in z need to be merged. Because each merging operation can be done in time $\mathrm { O } ( | P | \times | T | )$ , the total time for step 8 is $\mathrm { O } ( \mid R F _ { k - I } \mid \times k \times \mid P \mid \times \mid T \mid )$ . Since $R F _ { k - 1 } \subseteq C _ { k - 1 }$ , we have $\mathrm { O } ( | R F _ { k - 1 } | ) { \le } \mathrm { O } ( \Upsilon )$ and the total time becomes $\mathrm { O } ( \Upsilon \times k \times$ $\vert P \vert \times \vert T \vert )$

4.3. In steps 9 to 11, there are two tasks: (1) compute the supports of all itemsets in $\mathrm { C } _ { \mathrm { k } } ,$ , and (2) compute the supports of all subsets of itemsets in $R F _ { k - 1 }$ . The time required for the first task is $\mathrm { O } ( n \times l \times \lvert C _ { k } \rvert )$ , because it can be done by first reading every transaction and then adding the counts to the corresponding itemsets. In the second task, we add the counts to all subsets of itemsets in $R F _ { k - 1 }$ rather than all itemsets in $R F _ { k - 1 }$ . Therefore, it can be done by first reading every transaction and every itemset in $R F _ { k - 1 } { : }$ , generating all subsets, and finally adding the counts. Performing these operations requires time ${ \mathrm { O } } ( n \times l \times$ $| R F _ { k - 1 } | \ \times \ 2 ^ { k - 1 } )$ . Since ${ \mathrm { O } } ( \vert R F _ { k - 1 } \vert ) \leq$ ${ \mathrm { O } } ( \mid C _ { k - 1 } \mid )$ , the time required for this part is ${ \mathrm { O } } ( n \times l \times \Upsilon \times 2 ^ { k - 1 } )$ .

4.4. Step 12 is used to generate $F _ { k }$ from $C _ { k } .$ Since the support of each itemset in $C _ { k }$ must be checked if it is no less than $\sigma _ { s } ,$ the time is $\mathrm { O } ( \vert C _ { k } \vert ) = \mathrm { O } ( \Upsilon )$

4.5. Step 13 is for generating $R F _ { k }$ from $F _ { k } .$ . Because the support of each itemset in $F _ { k }$ must be checked if it is no less than $\sigma _ { r } ,$ the time is $\mathrm { O } ( | \mathrm { F } _ { \mathrm { k } } | )$ . Since ${ \mathrm { O } } ( \vert F _ { k } \vert ) { \le } { \mathrm { O } } ( \vert C _ { k } \vert )$ , we have the total time O(x ).

4.6. In steps 14 through 17, we compute the confidence of $x { \Rightarrow } y$ where x[y in $R F _ { k - 1 }$ That means, for each $z = x \cup y$ in $R F _ { k - 1 } ,$ we need to check all of its subsets. Therefore, there are totally $| R F _ { k - 1 } | \ \times \ 2 ^ { k - 1 }$ possible combinations. Since each combination needs a simple division, the total time for this part is $0 ( | \bar { R F } _ { k - 1 } | \ \times \ 2 ^ { k - 1 } )$ Þ. Furthermore, because $\mathrm { O } ( \vert R F _ { k - 1 } \vert ) { \le } \mathrm { O } ( \vert C _ { k - 1 } \vert )$ , the total time required is $0 ( \Upsilon \times 2 ^ { k - 1 } )$

From the above analysis, we know that two parts of the algorithm are most time consuming. The first is step 8, and the second is steps 9 through 11, which require times $0 \cap \ \times \ k \ \times \ | P | \ \times \ | \ T | \ )$ and ${ \mathrm { O } } ( n \mid \times$ $l \times \Upsilon \times 2 ^ { k - 1 } )$ , respectively. Let K denote the total number of the phases in the loop from step 6 to step 17. Then the total time is ${ \mathrm { O } } ( \Upsilon \times K ^ { 2 } \times | P | \times | T | ) +$ $\mathrm { O } ( n \times l \times \Upsilon \times K \times 2 ^ { K } )$

Next, we analyze the memory space required for the algorithm. We perform the analysis by examining the space needed to store the data structures used in the algorithm.

1. Because the space requirement for the PT-Interval table for each item is $\mathrm { O } ( \mid P \mid \ \times \ \mid T \mid )$ the total requirement for all individual items is $\mathrm { O } ( m \times | P | \times | T | )$ .

2. The requirement for the PT-Interval table for each itemset in $R F _ { k - 1 }$ is ${ \mathrm { O } } ( \mid R F _ { k - 1 } \mid \ \times \ \mid P \mid \ \times \ \mid T \mid )$

Since $0 ( \mid R F _ { k - 1 } \mid ) { \le } \mathrm { O } ( \mid C _ { k - 1 } \mid )$ , the total requirement for all itemsets is $0 \cap \times \mid P \mid \times \mid T \mid )$

3. The requirement for the TS table is $\mathrm { O } ( \mid P \mid \ \times \ \mid T \mid ) .$ because it is a single table.

4. The space requirements for $C _ { k } , R F _ { k } ,$ and $F _ { k }$ are O(x ) individually. Note that, because the same space can be shared by different iterations in the loop from steps 6 to 17, we only need one copy of them rather than multiple copies.

5. The space for storing the supports of all subsets of itemsets in $R F _ { k - 1 }$ is ${ \mathrm O } ( \bar { \vert } \bar { R } F _ { k - 1 } \vert \ \times \ 2 ^ { k - 1 } )$ Since $\mathrm { O } ( \vert R F _ { k - 1 } \vert ) { \le } \mathrm { O } ( \vert C _ { k - 1 } \vert )$ , the required space is $0 \Upsilon \times 2 ^ { k - 1 } )$

6. Combining all the space requirements, we find the total space is ${ \mathrm { O } } ( \Upsilon \times 2 ^ { K } ) + { \mathrm { O } } ( \Upsilon \times | P | \times | T | )$

## 4. Performance evaluation

In this section, we perform a simulation study to empirically compare the proposed and traditional association-rule mining methods. The main objective of the simulation study is to identify the conditions under which the proposed method significantly outperforms the traditional method in identifying important purchasing patterns in a multi-store environment. Three factors are considered in the study: (1) the numbers of stores and periods, (2) the store size, and (3) the product replacement ratio. In addition, we evaluate the computational efficiency of the proposed Apriori<sup>\_</sup>TP algorithm using the Apriori algorithm [1] as the baseline for comparisons. The proposed algorithm is implemented by Borland C+ language and tested on a PC with a Celeron 1.8 G processor and 768 MB main memory under the Windows 2000 operating system.

## 4.1. Data generation

In the experiment, we randomly generate the synthetic transactional data sets by applying the data generation algorithm proposed by Agrawal and Srikant [1]. The factors considered in the simulation are listed in Table 1. In addition, we generate the time and store information for each transaction in the data sets.

To generate the store sizes, we use two parameters, $S _ { u }$ and $S _ { l } ,$ to represent the largest and smallest store sizes, respectively, and the size of store i for $1 \leq i \leq q$ denoted by $S _ { i } ,$ is generated by a uniform distribution between $S _ { u }$ and $S _ { l } .$ . We assume that the total number of transactions and the number of products are dependent on a store’s size. In addition, we also allow the stores to have different product replacement (turnover) ratios. In the simulation, these relationships are established by generating m random numbers for the store i from a Poisson distribution with mean $S _ { i } ,$ and we use the jth number, denoted by $W _ { i j } ,$ as the weight of store i in period $j .$ Let $D _ { i j }$ denote the number of transactions of store i in period j. The total number of transactions, $D ,$ is distributed to the store $i ,$ and period $j$ is determined by:

Table 1  
Parameters used in simulation

<table><tr><td colspan="2">Parameters used in simulation</td></tr><tr><td> $D$ </td><td>Number of transactions</td></tr><tr><td> $q$ </td><td>Number of stores</td></tr><tr><td> $m$ </td><td>Number of periods</td></tr><tr><td> $r$ </td><td>Number of items</td></tr><tr><td> $L$ </td><td>Average length of transactions</td></tr><tr><td> $F_{l}$ </td><td>Average length of maximum potentially frequent itemsets</td></tr><tr><td> $F_{d}$ </td><td>Number of maximum potentially frequent itemsets</td></tr><tr><td> $S_{u},S_{l}$ </td><td>The maximum and minimum sizes of stores</td></tr><tr><td> $I_{d}$ </td><td>Replacement rates of items</td></tr></table>

$$
D _ {i j} = \frac {D}{\sum_ {m = 0} ^ {P} \sum_ {n = 0} ^ {T} W _ {m n}} W _ {i j}
$$

Furthermore, we assume that the number of products in a store is proportional to the square root of its size. Thus, let $I S _ { i } = \sqrt { S _ { i } }$ for $i = 1 , 2 , . . . , q .$ . Then, the number of products in store i, denoted by $N _ { i } ,$ is determined by the following formula:

$$
N _ {i} = \frac {r}{\mathrm{Max} (\mathrm{IS} _ {i})} \times \mathrm{IS} _ {i}
$$

Note that the products sold in a store may change over time, although $N _ { i }$ is kept the same in all periods. Since the parameter $I _ { d }$ is the proportion of products that will be replaced in every period, store i replaces $N _ { i } \times I _ { d }$ products in each period. Furthermore, we follow the method used by Agrawal and Srikant [1] to generate $F _ { d }$ maximum potentially frequent itemsets with an average length of $F _ { l }$

Finally, we generate all the transactions in the data sets. To generate the transactions for store i in period j, we generate $D _ { i j }$ from a Poisson distribution with mean L and a series of maximum potentially frequent itemsets. If an itemset generated from the process has some items not sold at store i in period j, we remove these items, and repetitively add the items into the transaction until we have reached the intended size. If the last itemset exceeds the boundary of this transaction, we remove the part that exceeds the boundary. When adding an itemset to a transaction, we use a ‘‘corruption level,’’ $c { = } 0 . 7 ,$ , to simulate the phenomenon that all the items in a frequent itemset do not always appear together. Information on how the corruption level affects the procedure of generating items for a transaction is included in the paper by Agrawal and Srikant [1]. To generate the nine types of data sets shown in Table 2, we use the following parameter values: r = 1000, D = 100 K, L = 6, F<sub>l</sub> = 4, and $F _ { d } = 1 0 0 0$ . For each type of the data sets, 10 replications are generated for statistical analysis of the results.

## 4.2. Performance measures

As discussed in Section 2, the traditional method underestimates the support and the confidence values and, as a result, may fail to identify important purchasing patterns in a multiple-store environment. We define three measures (errors) for empirically assessing the magnitudes of the deviations in support, confidence, and the number of association rules when we use the traditional association rules for the storechain data.

<table><tr><td>Data set</td><td>Number of stores</td><td>Number of periods</td><td>Range of store sizes</td><td>Product replacement rate</td></tr><tr><td>1</td><td>5</td><td>5</td><td>50–100</td><td>0.001</td></tr><tr><td>2</td><td>10</td><td>10</td><td>50–100</td><td>0.001</td></tr><tr><td>3</td><td>50</td><td>50</td><td>50–100</td><td>0.001</td></tr><tr><td>4</td><td>50</td><td>50</td><td>10–100</td><td>0.001</td></tr><tr><td>5</td><td>50</td><td>50</td><td>50–100</td><td>0.001</td></tr><tr><td>6</td><td>50</td><td>50</td><td>90–100</td><td>0.001</td></tr><tr><td>7</td><td>50</td><td>50</td><td>50–100</td><td>0.001</td></tr><tr><td>8</td><td>50</td><td>50</td><td>50–100</td><td>0.005</td></tr><tr><td>9</td><td>50</td><td>50</td><td>50–100</td><td>0.010</td></tr></table>

The type A error measures the relative difference in the support levels of all frequent itemsets generated by the traditional and proposed methods. It is determined by rel<sup>\_</sup>sup(X, $D _ { V _ { \chi } } ) - s u p ( X ,$ , D )/ rel<sup>\_</sup>sup(X, $D _ { V _ { \chi } } )$ . For example, if the support and relative support for an itemset X are sup(X, D) = 0.02 and rel<sup>\_</sup>sup(X, $D _ { V _ { X } } ) = 0 . 0 3$ , respectively, then the type A error rate is rel<sup>\_</sup>sup(X, $D _ { V _ { \chi } } ) - s u p ( X , \ D ) ) /$ rel<sup>\_</sup>sup(X, $D _ { V _ { \scriptscriptstyle X } } ) = 3 3 . 3 3 \%$ . By averaging the error rates of all frequent itemsets, we obtain the overall type A error rate. Similarly, the type B error is used to compare the difference in confidence levels of all rules generated by the traditional and proposed meth ods. It is defined as $c o n f ( X { \Rightarrow } Y ) - c o n f ^ { \prime } ( X { \Rightarrow } Y ) ) / c o n f$ $( X { \Rightarrow } Y )$ , where $c o n f ^ { \prime } ( X { \Rightarrow } Y )$ is the rule confidence computed by the traditional methods. By averaging the type B error rates of all common rules in the two methods, we obtain the overall type B error rate. Finally, the type C error is used to compare the relative difference in the numbers of rules generated by the two methods. Note that we set $\sigma _ { s }$ and $\sigma _ { r }$ at the same level when evaluating the types A and B error rates. It is because the frequent itemsets found by the two algorithms have to be the same in order to have a common base to compare the results produced by the two algorithms. Furthermore, we set $\sigma _ { c }$ at 1% in the comparison based on the type B error. Using this low value, we can include almost all possible rules in the comparison. However, because in a practical situation the minimum confidence threshold could be higher than this value, we also obtain the results for selected minimum confidence values ranging from 40% to 60%. Finally, we set $\sigma _ { s }$ at 0.5% in the comparison based on the type C error.

## 4.3. Simulation results

The first comparison is carried out based on the first three types of data sets in Table 2. Because these three types of data sets have different numbers of stores and periods, the results show the effects of the size of store chain and the length of time on the errors associated with using the traditional method. In order to study the effect of $\sigma _ { s } ,$ we also obtain the results for selected minimum support thresholds ranging from 0.3% to 0.6%. The averages of the types A, B, and C errors are shown in parts (a), (b), and (c), respectively, of Fig. 7. The two-factor ANOVA model is used to

(c)  
(a)  
![](/api/attachments/E2B3PVHS/fulltext/images/742d051db70c3637ed1376f7316f946dc90c652b4c90edd47d3dcbb2638b0fce.jpg)

(b)  
![](/api/attachments/E2B3PVHS/fulltext/images/5b3a687dce7bf1f037cfe3133d7852edcc28f63caef4497b72feb8af0659e2bb.jpg)

![](/api/attachments/E2B3PVHS/fulltext/images/4052f7771fbc8dbdf4e69a7539c9eef85a8f43601c9a7522b5adf5abee89a239.jpg)  
Fig. 7. (a) Effects of the numbers of stores and periods on the type A error rate. (b) Effects of the numbers of stores and periods on the type B error rate. (c) Effects of the numbers of stores and periods on the type C error rate.

analyze the results. We find that all the three error rates are significantly larger in the cases involving larger numbers of stores and periods. We also notice that the error rates generally increase as the minimum support decreases. All these results suggest that the traditional method is not suitable for the store-chain data. The result in part (c) of the figure further supports this conclusion, where, in the worst case reported, 40% of the SC rules are not successfully discovered when $\sigma _ { c }$ is 60%.

The second comparison is used to study the effects of the store size on the error rates. The data set types $4 , 5 ,$ and 6 are used, and the average error rates are shown in Fig. 8. The results of statistical analysis based on the two-factor ANOVA model indicate that the error rates are significantly larger when the store size has a larger variation. As shown in parts (a) and

(a)  
![](/api/attachments/E2B3PVHS/fulltext/images/f488530226b8a4f0709b98e39d117bf87f452fd982169cec411f68ddfec01a04.jpg)

(b)  
![](/api/attachments/E2B3PVHS/fulltext/images/22104d128af08d2afaf72951788e1332c2f4bcb229b2cf0ced2f7778c8558748.jpg)

![](/api/attachments/E2B3PVHS/fulltext/images/fa2809570a8645355909083ae4004000e12fb3ac03622bd590093aa6854d61d7.jpg)  
Fig. 8. (a) Effects of store size on the type A error rate. (b) Effects of store size on the type B error rate. (c) Effects of store size on the type C error rate.

(a)  
![](/api/attachments/E2B3PVHS/fulltext/images/931f1b23b52e4f177fdfe27540913d692ac3863cfe782cf64a5d3f0fb68e5e52.jpg)

(b)  
![](/api/attachments/E2B3PVHS/fulltext/images/ccc33c68ef2795fc68e6ebd64ea01ed2f2bb243c324b67a59714c0aa0eb314f6.jpg)

![](/api/attachments/E2B3PVHS/fulltext/images/f7978c916b4026b215ff03540a25d1c8d5f44136a5fec5044df10f1251017066.jpg)  
Fig. 9. (a) Effects of product replacement ratio on the type A error rate. (b) Effects of product replacement ratio on the type B error rate. (c) Effects of product replacement ratio on the type C error rate.

(b) of the figure, when the variation of the store size is the largest, the types A and B errors rates are close to 35% and 23%, respectively. In part (c), we find that more than 50% of the SC rules are not generated by the traditional method when $\sigma _ { c }$ is 50%, and the error rate reaches almost 70% when $\sigma _ { c }$ is 60%.

In the third part of the simulation study, we compare the error rates under different replacement rates. We use data set types 7, 8, and 9 for the comparison. The results, shown in Fig. 9, indicate that the error rates associated with larger replacement ratios are significantly higher than those associated with smaller replacement ratios. We also notice that the error rates increase as the minimum support decreases. These observations are supported by the results of our statistical analysis. Consequently, we conclude that the performance of the traditional method deteriorates as the product replacement ratio increases.

In the second part of the simulation study, we observe how the type B error rate changes when $\sigma _ { c }$ is varied from 40% to 60%. In this experiment, we set $\sigma _ { s }$ at 0.5% and use data set types 2, 4, 5, and 9 for comparison. We use data set type 5 as the baseline; data set type 2 to study the effect of smaller numbers of time periods and stores; and data set types 4 and 9, to study a larger variation in store size and a larger product replacement rate, respectively.

The simulation results are summarized in Fig. 10, where lines 1, 2, 3, and 4 correspond to the results of data sets 5, 2, 4 and 9, respectively. The result indicates that the error rate decreases significantly as we increase $\sigma _ { \mathrm { { c } } } .$ . This is because, when $\sigma _ { c }$ is higher, only those rules with higher confidence values are used in comparison, causing the type B error rate to decrease. Furthermore, we found that the effect of the product replacement rate is very similar to that of the numbers of periods and stores, and both factors are stronger than that of the variation in store size.

![](/api/attachments/E2B3PVHS/fulltext/images/19b6e8130b395786f6dd9cb80589650294a4e3ae6560c59163f60b825d89af3c.jpg)  
Fig. 10. The type B error rates vs. minimum confidence thresholds.

![](/api/attachments/E2B3PVHS/fulltext/images/b368ae7e6f3992d734ac665127a4e963bfb5659b9bc839baf1533c3d487d7f4a.jpg)  
Fig. 11. Run times.

To summarize the simulation study, we conclude that the traditional association rules may not be able to extract all important purchasing patterns for a multistore chain, especially when there are large numbers of stores and periods, a large variation in store sizes, and high product replacement ratios. This finding is significant because many store chains are growing in size to maintain the economy of scale and, at the same time, dynamically localize their product-mix strategies. All these trends support the need for the proposed method.

Finally, we evaluate the computational efficiency of the proposed algorithm by comparing it with the Apriori algorithm. We show the result in Fig. 11, where the running time is obtained by averaging the running times of all the data sets in Table 2. From the figure, we find that the proposed algorithm requires larger process times, but the differences are not substantial. This result is reasonable, because the proposed algorithm requires one more scan of the data than does the Apriori algorithm, and also requires additional basic operations in each phase of the algorithm.

## 5. Conclusion

Association-rule mining is a useful method of discovering customer purchasing patterns by extracting associations or co-occurrences from stores’ transactional databases. Since the method was first proposed by Agrawal et al. [1] in 1993, it has become an established and active research area. The existing methods, however, may fail to discover important purchasing patterns in a multi-store environment, because of an implicit assumption that products under consideration are on-shelf all the time across all stores.

To overcome the problem, a new method, called store-chain association rules, is proposed specifically for a multi-store environment, where stores may have different product-mix strategies that can be adjusted over time. The format of the rules is similar to that of the traditional rules. However, the rules also contain information on store (location) and time where the rules hold. The rules extracted by the proposed method may be applicable to the entire chain without time restriction, but may also be store- and timespecific. These rules have a distinct advantage over the traditional ones because they contain store (location) and time information so that they can be used not only for general or local marketing strategies (depending on the results), but also for product procurement, inventory, and distribution strategies for the entire store chain.

An Apriori-like algorithm is developed for mining chain-store association rules. A simulation is used to empirically compare the proposed and traditional association-rule mining methods. Three factors are considered in generating stores’ sales data: (1) the numbers of stores and periods, (2) the store size, and (3) the product replacement ratio. The analysis of the simulation result suggests that the proposed method has advantages over the traditional method especially when the numbers of stores and periods are large, stores are diverse in size, and product mix changes rapidly over time. Furthermore, the time complexity of the proposed algorithm is discussed, and the simulation results show that the algorithm is computationally efficient.

Store-chain association rules represent a promising research area in data mining. The results of this paper can be extended by considering time constraints, spatial constraints, quantitative attributes and/or taxonomy, and other kinds of time- or location-related knowledge. Furthermore, it is important to explore the strategies of generating the store-chain association rules incrementally, in an on-line model, in a distributed environment, or in parallel models.

## Acknowledgements

The first author was supported in part by the Ministry of Education (MOE) Program for Promoting Academic Excellence of Universities under Grant No. 91-H-FA07-1-4 and National Science Council Grant No. 91-2416-H-008-003.

## Appendix A

The support values and the confidence values obtained by the traditional association mining are underestimated, compared with the true value discussed in this paper. First, it is easy to see that the traditional support value is lower because its base is larger. As to the confidence value, say $c o n f ( X {  } Y )$ , the traditional approach defines it as follows.

$$
\begin{array}{l} \text { conf } (X \Rightarrow Y) \\ = \sup (X \cup Y, D) / \sup (X, D) \\ = [ | W (X \cup Y, D) | / | D | ] / [ | W (X, D) | / | D | ] \\ = | W (X \cup Y, D) | / | W (X, D) |. \end{array} \tag {A1}
$$

But the correct one should be

$$
\begin{array}{l} \text {conf} (X \Rightarrow Y) \\ = \text {rel\_sup} (X \cup Y, D _ {V _ {X \cup Y}}) / \text {rel\_sup} (X, D _ {V _ {X \cup Y}}) \\ = [ | W (X \cup Y, D _ {V _ {X \cup Y}}) | / | D _ {V _ {X \cup Y}} | ] \\ / [ | W (X, D _ {V _ {X \cup Y}}) | / | D _ {V _ {X \cup Y}} | ] \\ = | W (X \cup Y, D _ {V _ {X \cup Y}}) | / | W (X, D _ {V _ {X \cup Y}}) | \end{array}\tag{A2}
$$

By comparing Eq. (A1) with Eq. (A2), we find that the numerators are the same, because it is not possible that X[Y appears in a transaction not in $D _ { V _ { \scriptscriptstyle  { X } \cup Y } }$ , and that the denominator of Eq. (A1) is no less than that of Eq. (A2), because $| W ( X , D ) | \ge | W ( X , D _ { V _ { X \cup Y } } ) |$ Thus, we conclude that the confidence value of Eq. (A1) is no larger than that of Eq. (A2).

## References

[1] R. Agrawal, R. Srikant, Fast algorithms for mining association rules, Proceedings of the 20th VLDB Conference, Santiago, Chile, 1994, pp. 478–499.

[2] R. Agrawal, T. Imielinski, A. Swami, Mining association rules between sets of items in large databases, Proceedings of the ACM SIGMOD International Conference on Management of Data, Washington, D.C., 1993, pp. 207 – 216.

[3] J.M. Ale, G.H. Rossi, An approach to discovering temporal association rules, Proceedings of the 2000 ACM Symposium on Applied Computing (Vol. 1), Villa Olmo, Como, Italy, 2000, pp. 294 – 300.

[4] R.J. Bayardo Jr., R. Agrawal, Mining the most interesting rules, Proceedings of the 5th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, San Diego, CA, USA, 1999, pp. 145 – 154, Aug.

[5] I. Bose, R.K. Mahapatra, Business data mining—a machine learning perspective, Information and Management 39 (2001) 211 – 225.

[6] S. Brin, R. Motwani, J.D. Ullman, S. Tsur, Dynamic itemset counting and implication rules for market basket data, Proceedings of the 1997 ACM-SIGMOD Conference on Management of Data, Tucson, Arizona, USA, May 1997, pp. 255 – 264.

[7] E. Clementini, P.D. Felice, K. Koperski, Mining multiplelevel spatial association rules for objects with a broad boundary, Data and Knowledge Engineering 34 (3) (2000) 251– 270.

[8] M.-S. Chen, J. Han, P.S. Yu, Data mining: an overview from a database perspective, IEEE Transactions on Knowledge and Data Engineering 8 (1996) 866 – 883.

[9] A. Freitas, On rule interestingness measures, Knowledge-Based Systems 12 (5) (1999) 309– 315.

[10] J. Han, Y. Fu, Mining multiple-level association rules in large databases, IEEE Transactions on Knowledge and Data Engineering 11 (5) (1999) 798–805.

[11] J. Han, M. Kamber, Data Mining, Morgan Kaufmann, San Francisco, 2001.

[12] J. Han, J. Pei, Y. Yin, Mining frequent patterns without candidate generation, Proceedings of the 2000 ACM-SIGMOD Int. Conf. on Management of Data, Dallas, TX, 2000, May.

[13] H. Ishibuchi, T. Nakashima, T. Yamamoto, Fuzzy association rules for handling continuous attributes, Proceedings of the IEEE International Symposium on Industrial Electronics, Pusan, Korea, 2001, pp. 118 – 121.

[14] C.M. Kuok, A.W. Fu, M.H. Wong, Mining fuzzy association rules in databases, SIGMOD Record 27 (1) (1998) 41 – 46.

[15] K. Koperski, J. Han, Discovery of spatial association rules in geographic information databases, Proc. 4th International Symposium on Large Spatial Databases (SSD95), Portland, Maine, Aug. 1995, pp. 47–66.

[16] C.H. Lee, C.R. Lin, M.S. Chen, On mining general temporal association rules in a publication database, Proceedings of the 2001 IEEE International Conference on Data Mining, San Jose, California, 2001, pp. 337 – 344.

[17] Y. Li, P. Ning, X.S. Wang, S. Jajodia, Discovering calendarbased temporal association rules, Proceedings of the Eighth International Symposium on Temporal Representation and Reasoning, Cividale Del Friuli, Italy, 2001, pp. 111 – 118.

[18] J. Liu, Y. Pan, K. Wang, J. Han, Mining frequent item sets by opportunistic projection, Proceedings of the 2002 Int. Conf.

on Knowledge Discovery in Databases, Edmonton, Canada, 2003, July.

[19] H. Lu, L. Feng, J. Han, Beyond intra-transaction association analysis: mining multi-dimensional inter-transaction association rules, ACM Transactions on Information Systems 18 (4) (2000) 423 – 454.

[20] J.-S. Park, M.-S. Chen, P.S. Yu, Using a hash-based method with transaction trimming for mining association rules, IEEE Transactions on Knowledge and Data Engineering 9 (1997) 813– 825.

[21] R. Rastogi, K. Shim, Mining optimized association rules with categorical and numeric attributes, IEEE Transactions on Knowledge and Data Engineering 14 (2002) 29–50.

[22] J.F. Roddick, M. Spiliopoilou, A survey of temporal knowledge discovery paradigms and methods, IEEE Transactions on Knowledge and Data Engineering 14 (2002) 750–767.

[23] S. Shekhar, S. Chawla, S. Ravadam, A. Fetterer, X. Liu, C. Lu, Spatial databases—accomplishments and needs, IEEE Transactions on Knowledge and Data Engineering 11 (1999) 45 – 55.

[24] R. Srikant, R. Agrawal, Mining quantitative association rules in large relational tables, Proceedings of the ACM-SIGMOD 1996 Conference on Management of Data, Montreal, Canada, 1996, pp. 1 – 12, June.

[25] J. Wijsen, R. Meersman, On the complexity of mining quantitative association rules, Data Mining and Knowledge Discovery 2 (1998) 263– 281.

Yen-Liang Chen is Professor of Information Management at National Central University of Taiwan. He received his PhD degree in Computer Science from the National Tsing Hua University, Hsinchu, Taiwan. His current research interests include data modeling, data mining, data warehousing and operations research. He has published papers in Operations Research, IEEE Transaction on Software Engineering, Computers and OR, European Journal of Operational Research, Information and Management, Information Processing Letters, Information Systems, Journal of Operational Research Society, and Transportation Research.

Kwei Tang is Professor of Management and the area coordinator of quantitative methods in the Krannert Graduate School of Management at Purdue University. He received a BS from National Chiao Tung University, Taiwan, an MS from Bowling Green State University, and a PhD in Management Science from Purdue University. His current research interests include data mining, supply chain management, and quality management.

Ren-Jie Shen is a system analyst and designer in Data Systems Consulting, a leading commercial software company in Taiwan. He received his MS degree in Information Management from National Central University of Taiwan. His research interests include data mining, information systems and EC technologies.

Ya-Han Hu is currently a PhD student in the Department of Information Management, National Central University, Taiwan. He received the MS degree in Information Management from National Central University of Taiwan. His research interests include data mining, information systems and EC technologies.
