---
otero_id: 2546
otero_key: "6UV7CHG8"
title: "Constraint-based sequential pattern mining: The consideration of recency and compactness"
authors: "Yen-Liang Chen; Ya-Han Hu"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2005.10.006"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dsw

# Constraint-based sequential pattern mining: The consideration of recency and compactness

Yen-Liang Chen <sup>\*</sup>, Ya-Han Hu

Department of Information Management, National Central University, Chung-Li 320, Taiwan, ROC

Received 26 July 2004; received in revised form 29 May 2005; accepted 20 October 2005 Available online 1 December 2005

## Abstract

Sequential pattern mining is an important data-mining method for determining time-related behavior in sequence databases. The information obtained from sequential pattern mining can be used in marketing, medical records, sales analysis, and so on. Existing methods only focus on the concept of frequency because of the assumption that sequences’ behaviors do not change over time. The environment from which the data is generated is often dynamic, however, so the sequences’ behaviors may change over time. To adapt the discovered patterns to these changes, two new concepts, recency and compactness, are incorporated into traditional sequential pattern mining. The concept of recency causes patterns to quickly adapt to the latest behaviors in sequence databases, while the concept of compactness ensures reasonable time spans for the discovered patterns. We named the new patterns CFRpatterns because three concepts (compactness, frequency, and recency) are simultaneously considered. An efficient method is presented to find CFR-patterns. Empirical evaluation shows that the proposed methods are computationally efficient and that they are more advantageous than traditional methods when sequences’ behaviors change over time. <sup>D</sup> 2005 Elsevier B.V. All rights reserved.

Keywords: Sequential pattern; Constraint-based mining; Temporal databas

## 1. Introduction

It has been well recognized that mining in temporal databases is an important data-mining task. Many approaches to temporal data mining have been proposed to extract information, such as time series analysis [2,11,19,26], temporal association rules mining [3,20,21], and sequential pattern discovery [2,33,34]. Among them, sequential pattern mining is one of the most well-known methods and has broad applications (see [15,35,41] for an overview), including web-log analysis, customer purchase behavior analysis, process analysis of scientific experiments, and medical record analysis [36,38,39]. Given a set of data sequences, the goal is to discover subsequences that are frequent, meaning that the percentage of data sequences containing them exceeds a user-specified frequency threshold (also known as minimum support).

Many approaches [4,12] in sequential pattern mining have been proposed and most of them focus on the following two issues: (1) improving the efficiency of the mining process [18,22,29,40], and (2) extending the mining of sequential patterns to other types of timerelated patterns [5–9,16,17,24,25,31,37]. It is worth noting that all the works mentioned above are based on the concept of frequency. If a pattern is not frequent, it is removed from further consideration.

Frequency is a good indicator of the importance of a pattern. In real life, however, the environment may change constantly and users’ behavior may also change over time. This has resulted in numerous studies [3,10,20,21,23,32] researching and comparing the differences in the patterns and association rules mined from several database snapshots taken at different times. These studies were brought about by the observation that a user’s recent behavior is not necessarily the same as past behavior, and a pattern that occurred frequently in the past may rarely occur in the present or possibly never occur again.

From that observation, one must decide which is more important—recent patterns or long-run patterns. There is no definite answer to this question. When the environment and the user’s behavior are stable, we may feel that patterns observed in the long run are more important. On the other hand, when there are constant and violent changes in the environment, recent users’ patterns are more important, since long-term patterns do not react well to changing behaviors. These observations cause us to consider the possibility that we may have patterns that are important in both the long run and in recent periods. Therefore, the sequential patterns we want to discover must satisfy not only the frequency minsup (the definition of minimum support in [1]) for the whole sequence database but also the recency minsup for the recent sequence database (i.e., the subset of the sequence database that occurs recently).

We further add the constraint that a discovered pattern must be compact, meaning the time span from the first item to the last item in the pattern must be no more than a given threshold Maximum Span Length (ms<sup>\_</sup>length). For example, suppose we have a customer who bought item a in (1999:Sep:3), and bought items b and c in (2003:Sep:3). Another customer bought a in (2003:Aug:3), and b and c in (2003:Sep:3). It is evident that pattern h(a), (bc)i appears in both data sequences. Yet if we set ms<sup>\_</sup>length at 3 months, only the second data sequence contains this pattern. We add this constraint to ensure that the purchases implied by a pattern occur during a reasonable time period. If the time span for the purchases is too long, it reduces the significance of the pattern and weakens the strength of the implication of the pattern. Therefore, when we compute the support of a pattern, we only count those data sequences that match the pattern compactly, meaning the time span of the items in the data sequence matching the pattern is no larger than ms<sup>\_</sup>length.

Ultimately, we want to discover the patterns that are frequent, recent, and compact. The first two properties ensure that patterns are important in both the long run and in recent periods, and the last property ensures that the purchases implied by patterns occur within a reasonable time period.

The patterns proposed in this paper are a generalization of traditional sequential patterns. The traditional model only considers frequency minsup, while our model has two additional thresholds: recency minsup and ms<sup>\_</sup>length. One can easily nullify a threshold simply by setting a threshold very low (for frequency minsup and recency minsup) or very large (for ms<sup>\_</sup>length). By adjusting these two thresholds according to our needs, we can have four different kinds of patterns, consisting of CFR (compact, frequent, and recent), CF\* (compact and frequent), \*FR (frequent and recent), and \*F\* (frequent only). For example, by setting the recency minsup very low and ms<sup>\_</sup>length very large, we can find \*F\* patterns, which are traditional sequential patterns.

In this paper, we propose a novel algorithm, the CFR-PostfixSpan algorithm, which was developed from the PrefixSpan algorithm [29], for finding all frequent sequential patterns with consideration to compactness and recency. Section 2 reviews previous research related to mining in a changing environment and constraint-based sequential pattern mining. Section 3 formally defines the problem and the compact, frequent, and recent sequential patterns (CFR-patterns). Section 4 develops the CFR-PostfixSpan algorithm to find all CFR-patterns. Section 5 provides the preparation of data, performance measures, and experimental setup. Section 6 presents thorough experimental results and discussions. Section 7 concludes our study.

## 2. Related work

## 2.1. Data mining in a changing environment

Finding interesting and useful information is one of the most important tasks in data mining. From the temporal aspect, the environment continually changes and user behavior is not always the same. In different time periods, we may find different sets of rules or the significance of a rule may fluctuate.

Dong and Li [10] proposed a new concept called emerging patterns, which captures patterns with significant changes and differences between data sets. It is defined as a pattern whose minimum support grows significantly, for example, larger than a user-specified threshold, from one data set to another. When applied to two different time period databases, the emerging patterns technique can capture emerging trends over time. Liu et al. [23] presented a set of statistical methods to analyze the behavior of rules over time. They first partitioned the data set into several sub-data sets according to the different time periods. Then, all the rules in each sub-data set were found. These rules, the corresponding support, and the confidence values were analyzed through a number of statistical tests. Finally, several kinds of change patterns were generated. Song et al. [32] summarized all the possible types of changes from past research in temporal association rule mining, such as emerging patterns, unexpected change, and the added/perished rule. Several similarity and difference measures have been developed to discover all types of change rules.

## 2.2. Constraint-based sequential pattern mining

In recent years, researchers have recognized that frequency is not the best measure to use in determining the significance of a pattern in many applications [13,28,30]. When using the single frequency constraint, the traditional mining method often generates a huge number of patterns and rules, but most of them are worthless. Due to its inefficiency and ineffectiveness, the importance of constraint-based pattern mining has been emphasized [13,14,27]. Many approaches have also been proposed to consider the interesting issue of time constraints [8,25,33]. Users are allowed to specify their focus in the mining process through various time constraints and then relevant patterns are generated.

Srikant and Agrawal [33] first generalized the sequential pattern mining problem to allow for the handling of time constraints. The time-gap constraints confine the time interval between two adjacent elements to a reasonable period while the sliding time window constraint permits elements of a pattern to span a set of transactions within a user-specified window. For example, if $m a x - g a p = 3 0 , m i n - g a p = 0 ,$ , and sliding time win-$d o w = 7$ , a sequential pattern ((a, b), (c, d)) means that items a and b occurred within 7 days of each other; items c and d also occurred within 7 days of each other, and the time interval between itemset $( a , b )$ and $( c , d )$ is within 30 days. Mannila et al. [25] specified the window width (win) to find frequent episodes in sequences of events. This study finds serial episodes in which, in a time range win, a occurs, b follows, and finally c occurs. It also finds parallel episodes such that in a time range win, a, b, and c all occur in no specific order. Chen et al. [8] specified a time-interval set into discovering timeinterval sequential patterns, which can reveal not only the order of items, but also the time intervals between successive items. An example of a time-interval sequential pattern is $( a , I _ { 2 } , b , I _ { 1 } , c )$ , meaning that a is bought first, then after a time-interval of $I _ { 2 } ,$ , b is bought, and finally after a time interval of $I _ { 1 }$ , c is bought.

## 2.3. Discussion

All the work mentioned in Section 2.1 identifies changes in association rules from different time snapshot databases. In our study, however, we focus on discovering sequential patterns that are constant in both the long run and the recent period, without considering various kinds of change rules. Hence, the two concepts of compactness and recency are considered, where recency ensures a sequential pattern still holds in the recent period, while compactness ensures the purchases implied by patterns occur within a reasonable time period. Moreover, as discussed in Section 2.2, constraint-based pattern mining has been well-developed. By defining various types of time constraints, all the results in previous studies show that the number of patterns and their processing times can be significantly reduced. In our study, the concepts of compactness and recency can be viewed as kinds of time constraints in sequential pattern mining. Thus, we adopted the constraint-based approach as our basis for designing an algorithm that is both efficient and effective.

## 3. Problem definition

In the past, the customer data sequence was represented as an ordered list of itemsets, with a transaction time assigned to each. This work represents the data sequence differently: a data sequence A is represented as $\langle ( a _ { 1 } , t _ { 1 } ) , ( a _ { 2 } , t _ { 2 } ) , ( a _ { 3 } , t _ { 3 } ) , \ldots , ( a _ { n } , t _ { n } ) \rangle$ i, where $a _ { j }$ is an item and $t _ { j }$ stands for the time at which $a _ { j }$ occurs, $1 \leq j \leq n$ , and $t _ { j - I } \leq t _ { j }$ for $2 \leq j \leq n$ . If items occur at the same time in the data sequence, they are ordered alphabetically. This new representation of data sequences is actually typical. A data sequence in the previous format can be transformed into the new format by sorting all the items first by time, and then alphabetically. Likewise, a data sequence in the new format can be transformed into the traditional format by combining items that occur at the same time into an itemset, and then sorting these itemsets by time.

Based on this format, we give the following definitions:

Definition 1. Let I denote the set of items in the database. Let $A = \langle ( a _ { 1 } , t _ { 1 } ) , ( a _ { 2 } , t _ { 2 } ) , \dots , ( a _ { n } , t _ { n } ) \rangle$ be a data sequence and $I _ { q } = \langle i _ { 1 } i _ { 2 } . . . i _ { m } \rangle$ be an itemset where $i _ { p } \in I ( 1 \leq p \leq m )$ We say itemset $I _ { q }$ is contained in A if integers $1 \leq k _ { 1 } < k _ { 2 } < . . . < k _ { m } \leq n$ exist such that, $i _ { 1 } { = } a _ { k _ { 1 } } , i _ { 2 } { = } a _ { k _ { 2 } } ,$ $. . . , i _ { m } { = } a _ { k _ { m } }$ and $t _ { k _ { 1 } } { = } t _ { k _ { 2 } } { = } . . . { = } t _ { k _ { m } }$ . We refer to $k _ { 1 }$ and $t _ { k _ { 1 } }$ as the position and the time that $I _ { q }$ occurs in A, respectively.

Definition 2. Let $B { = } \langle I _ { 1 } I _ { 2 } { \ldots } . . . I _ { s } \rangle$ be a sequence of itemsets, where $I _ { q } \subseteq I \left( 1 \leq q \leq s \right)$ . Sequence B is contained in A, or is a subsequence of A if the following conditions are satisfied: (1) each $I _ { q }$ in B is contained in A, and $( 2 ) t _ { I _ { 1 } } { < } t _ { I _ { 2 } } { < } . . . { < } t _ { I _ { s } }$ where $t _ { I _ { q } } \left( 1 \leq q \leq s \right)$ is the time at which $I _ { q }$ occurs in A.

For example, itemset h(ab)i is contained in data sequence $A = \langle ( a , 1 ) , ( c , 3 ) ( a , 4 ) , ( b , 4 ) , ( e , 5 ) , ( a , 6 )$ 2 $( e , 6 ) , ( c , 1 0 ) \rangle$ , because both items a and b occur in A at time 4. The sequence $\left. ( a b ) ( a e ) \right.$ is a subsequence of A because itemset (ab) occurs in A at time 4 and (ae) occurs at time 6.

Definition 3. Assume that $t _ { I _ { q } }$ is the time at which $I _ { q }$ $( 1 \leq q \leq s )$ occurs in A. Let ms<sup>\_</sup>length be the userspecified maximum span length and $t _ { \mathrm { R } }$ be the userspecified recency threshold. B is called a compact subsequence of A if and only if (1) B is a subsequence of A, and (2) the compactness constraint is satisfied, i.e. $t _ { I _ { s } } - t _ { I _ { 1 } } \leq m s \_ l e n g t h .$ . B is called a compact recent subsequence of A if and only if (1) B is a compact subsequence of A, and (2) the recency constraint is satisfied, i.e., $t _ { I _ { s } } \ge t _ { \mathrm { R } }$

Example 1. Let $A = \langle ( a , 1 ) , ( c , 3 ) , ( a , 4 ) , ( b , 4 ) , ( a , 6 ) ,$ (e, 6), (c, 10), (d, 10)i be a data sequence and ms<sup>\_</sup>length = 5. Then, sequence $\left. ( c ) ( b ) ( a e ) \right.$ is a compact subsequence of A (the time stamps of itemsets (c), (b) and (ae) are 3, 4 and 6, respectively, and the difference between them is $3 \leq m s .$ <sup>\_</sup>length). Moreover, if $t _ { \mathrm { R } } { = } 6$ , then $\left. ( c ) ( b ) ( a e ) \right.$ is a compact recent subsequence of A because $\left. ( c ) ( b ) ( a e ) \right.$ is a compact subsequence of A and the time stamp of itemset $( a e ) { = } 6 \geq t _ { \mathrm { R } }$ Sequence $\langle ( b ) ( a e ) ( c d ) \rangle$ is not a compact subsequence of A because the difference between itemsets (b) and (cd) does not satisfy the ms<sup>\_</sup>length.

Definition 4. A sequence database S is formed by a set of records $\langle s i d , s \rangle$ , where s is a data sequence and sid is the identifier of this data sequence. For a given sequence a, its cf<sup>\_</sup>support count and cr<sup>\_</sup>support count in S can be defined as follows:

$$
c f \_ s u p p o r t _ {S} (\alpha) = | \big \{(s i d, s) | (s i d, s) \in S \wedge \alpha
$$

is a compact subsequence in $s \}$ j

$$
c r \_ s u p p o r t _ {S} (\alpha) = | \left\{(s i d, s) | (s i d, s) \in S \wedge \alpha \right.
$$

is a compact recent subsequence in $s \}$ :

Example 2. Consider the sequence database shown in Fig. 1 and $t _ { \mathrm { R } } = 1 4$ . The cf<sup>\_</sup>support of the sequence h(ab)(c)i is 3 (in data sequences 10, 20, and 30), while the cr<sup>\_</sup>support of the sequence $\langle ( a b ) ( c ) \rangle$ is 2 (in data sequences 20 and 30). The subsequence h(a, 4), (b, 4), (c, 10)i contained in data sequence 10 cannot be counted when computing cr<sup>\_</sup>support because the time stamp of item c is smaller than $t _ { \mathrm { R } }$

```txt
sid sequence
10 < (a, 1), (c, 3), (a, 4), (b, 4), (a, 6), (e, 6), (c, 10)>
20 < (d, 5), (a, 7), (b, 7), (e, 7), (d, 9), (e, 9), (c, 14), (d, 14)>
30 < (a, 8), (b, 8), (e, 11), (d, 13), (b, 16), (f, 16), (c, 20)>
40 < (b, 15), (f, 17), (e, 18), (b, 22), (c, 22)>
50 < (c, 5), (b, 6), (d, 6), (a, 10), (b, 17), (b, 19), (c, 19)>
```  
Fig. 1. A sequence database.

Definition 5. Let f<sup>\_</sup>minsup and r<sup>\_</sup>minsup be the user specified frequency and recency thresholds, respectively. A sequence a is called a compact frequent sequential pattern (CF-pattern) if cf<sup>\_</sup>support<sub>S</sub>(a) <sub>z</sub> f<sup>\_</sup>minsup. A sequence a is called a compact recent sequential pattern (CR-pattern) if $c r \_ s u p p o r t _ { S } ( \alpha ) \ge r .$ <sup>\_</sup>minsup. Finally, a sequence a is called a compact frequent recent sequential pattern (CFR-pattern) if it satisfies the relationship:

$$
c f \_ s u p p o r t _ {S} (\alpha) \geq f \_ m i n s u p \wedge c r \_ s u p p o r t _ {S} (\alpha) \geq r \_ m i n s u p.
$$

To formally state our problem, given a sequence database S, the aim is to discover all sequential patterns that satisfy f<sup>\_</sup>minsup and r<sup>\_</sup>minsup in S (CFRpatterns).

## 4. The CFR-PostfixSpan algorithm

We now introduce an efficient algorithm, CFR-PostfixSpan, for mining all the CFR-patterns from sequence databases. The CFR-PostfixSpan algorithm is developed by modifying the well-known PrefixSpan algorithm, which partitions the sequence database into a number of projected databases and shows the sequential patterns by exploring only local frequent patterns in each projected database.

First, we define compact postfix, compact recent postfix, compact projection, compact prefix, and projected database, since the CFR-PostfixSpan algorithm is based on these definitions. Then, we summarize the original PrefixSpan algorithm and the differences between the two. Finally, we explore the CFR-Postfix-Span algorithm in detail.

Definition 6 The compact postfix and the compact recent postfix. Given a data sequence $\boldsymbol { \alpha } = \langle ( a _ { 1 } , \ t _ { 1 } )$ $( a _ { 2 } , \ t _ { 2 } ) , \ . \ . . . , ( a _ { n } , \ t _ { n } ) \rangle$ and a sequence $\beta = \left. I _ { 1 } I _ { 2 } \dots I _ { m } \right.$ $\beta$ is a compact postfix of a if and only if (1) b is a subsequence of $\alpha , \ ( 2 ) \ t _ { I _ { m } } = t _ { n } .$ , and (3) $t _ { I _ { m } } - t _ { I _ { 1 } } \le m s _ { \_ }$ length. Furthermore, $\beta$ is a compact recent postfix of a if and only if (1) $\beta$ is a compact postfix of a, and (2) $t _ { I _ { m } } \ge t _ { \mathrm { R } }$

For example, we are given a data sequence $\alpha = \langle ( a _ { i }$ 1), (c, 3), (a, 4), (b, 4), (a, 6), (e, 6), (c, 10)i and ms<sup>\_</sup>length = 5. Sequence h(ae)(c)i is a compact postfix of $\alpha ,$ but $\langle ( a ) ( e ) ( c ) \rangle$ is not because it does not satisfy ms<sup>\_</sup>length. Furthermore, if $t _ { \mathrm { R } } { = } 8$ , then sequence h(ae)(c)i is also a compact recent postfix of $\textsf { X } .$

Definition 7 The compact projection. Given a data sequence $\alpha = \langle ( a _ { 1 } , ~ t _ { 1 } ) , ~ ( a _ { 2 } , ~ t _ { 2 } ) , ~ ( a _ { 3 } , ~ t _ { 3 } ) , ~ . ~ . ~ . , ~ ( a _ { n } , ~ t _ { n } ) \rangle$ let $\beta$ be a subsequence of a of length s. Let $i _ { 1 }$ be the position in a that matches the first item of $\beta . \mathrm { ~ A ~ }$ data subsequence $\alpha ^ { \prime } = \langle ( a _ { 1 } ^ { \prime } , t _ { 1 } ^ { \prime } ) , ( a _ { 2 } ^ { \prime } , t _ { 2 } ^ { \prime } ) , ( a _ { 3 } ^ { \prime } , t _ { 3 } ^ { \prime } ) , . . . , ( a _ { p } ^ { \prime } , t _ { p } ^ { \prime } ) \rangle$ of a is called a compact projection of a with respect to $\beta$ if and only if $( 1 ) \ \alpha ^ { \prime }$ has the postfix $\beta , ( 2 )$ the first $( p - s )$ items of $\alpha ^ { \prime }$ appears consecutively from position $i _ { 1 } - ( p - s )$ to position $i _ { 1 } + 1 \quad \quad \mathrm { i n } \quad \quad \alpha ,$ (3) $t _ { p } ^ { \prime } - t _ { 1 } ^ { \prime } { = } m s \_ l e n g t h$ , and (4) adding any item to the front of $\alpha ^ { \prime }$ causes it to violate a condition (3).

Example 3. Let $\alpha = \langle ( a , 1 ) , ( c , 3 ) , ( a , 4 ) , ( c , 4 ) , ( a , 6 ) , ( e ,$ $6 ) , ( c , 1 0 ) \rangle$ , ms<sup>\_</sup>length =5, and $t _ { \mathrm { R } } = 4 .$ . If a is projected with respect to the postfix $\beta = ( c )$ , then there are three possible positions of $i _ { 1 } \colon$ positions 2, 4, and 7. For these three different $i _ { 1 } ,$ three different compact projections $\alpha ^ { \prime }$ are obtained, the first of which is $\langle ( a , 1 ) , ( c , 3 ) \rangle$ , the second is $\langle ( a , 1 ) , ( c , 3 ) , ( a , 4 ) , ( c , 4 ) \rangle$ , and the third is $\langle ( a ,$ $6 ) , ( e , 6 ) , ( c , 1 0 ) \rangle$ . Each of these projected sequences satisfies the conditions: (1) it has postfix c, (2) the first $( p - s ) { = } ( p - 1 )$ positions appear consecutively in a, (3) the time span is no more than 5, and (4) adding any item to the front causes its time span to extend longer than 5. Using the projected sequence $\alpha ^ { \prime } = \langle ( a , 6 ) , ( e , 6 ) , ( c , 1 0 ) \rangle$ to further explain the last condition, we note that the subsequence $\langle ( a , 1 ) , ( c , 3 ) , ( a , 4 ) , ( c , 4 ) \rangle$ is not included in $\alpha ^ { \prime }$ because adding (a, 4) or (c, 4) into $\alpha ^ { \prime }$ will cause $\alpha ^ { \prime }$ to violate the time span constraint.

This example reveals that projecting a data sequence a with respect to a compact postfix $\beta$ may produce more than one compact projection. To differentiate between different projections from the same data sequence, Sid and End<sup>\_</sup>time are attached while building the compact projection of $\beta ,$ where Sid is the identifier of the data sequence and End<sup>\_</sup>time is the time stamp in a that matches the last itemset of $\beta .$

Definition 8 The compact projection. Let $\alpha ^ { \prime } = \langle ( a _ { 1 } ^ { \prime }$ $t _ { 1 } ^ { \prime } ) , ~ ( a _ { 2 } ^ { \prime } , ~ t _ { 2 } ^ { \prime } ) , ~ ( a _ { 3 } ^ { \prime } , ~ t _ { 3 } ^ { \prime } ) , . . . , ~ ( a _ { p } ^ { \prime } , ~ t _ { p } ^ { \prime } ) \rangle$ be the compact projection of a w.r.t. the compact postfix $\beta = { \langle I _ { 1 } I _ { 2 } }$ $\cdots . I _ { m } \rangle$ . Let $i _ { s }$ be the first item in itemset $I _ { 1 }$ and $t _ { s } ^ { \prime }$ the time at which $i _ { s }$ occurs in $\alpha ^ { \prime }$ . Then, data sequence $\gamma = \langle { ( a _ { 1 } ^ { \prime } , ~ t _ { 1 } ^ { \prime } ) , ~ ( a _ { 2 } ^ { \prime } , ~ t _ { 2 } ^ { \prime } ) , ~ . ~ . ~ . , ~ ( a _ { s - 1 ) } ^ { \prime } , ~ t _ { s - 1 ) } ^ { \prime } } \rangle$ is the compact prefix of a w.r.t. $\beta .$

Definition 8 indicates that the compact prefix can be easily obtained by directly removing the compact postfix from the compact projection. In Example $3 , \ \beta { = } ( c )$ and the three different compact projections $\alpha ^ { \prime }$ are $\langle ( a ,$ $1 ) , ( c , 3 ) \rangle , \langle ( a , 1 ) , ( c , 3 ) , ( a , 4 ) , ( c , 4 ) \rangle$ and $\langle ( a , 6 ) , ( e ,$ $6 ) , ( c , 1 0 ) \rangle$ . Therefore, the three compact prefixes are $\langle ( a , \ 1 ) \rangle , \ \langle ( a , \ 6 ) , \ ( e , \ 6 ) \rangle$ and $\langle ( a , \ 1 ) , \ ( c , \ 3 ) , \ ( a , \ 4 ) \rangle$

The original PrefixSpan algorithm solved problems using the divide and conquer strategy, meaning that instead of projecting a sequence database by considering all the possible occurrences of frequent subsequences, the projection was based only on frequent prefixes because any frequent subsequences could always be found by growing a frequent prefix. The algorithm can be briefly explained as follows. Initially, we set $\alpha { = } \mathrm { { n u l l } } .$ For a given a-projected database $S | _ { \alpha } ,$ , the algorithm first finds all the frequent 1-patterns. For each frequent 1-pattern in $S | _ { \alpha }$ , named b, b is appended to a to form a sequential pattern $\alpha ^ { \prime }$ , and constructs the $\alpha ^ { \prime }$ -projected database $S | _ { \alpha ^ { \prime } }$ . Recursively finding the sequential patterns in $S | _ { \alpha ^ { \prime } }$ yields all the sequential patterns in S.

Extending the PrefixSpan algorithm to discover all CFR-patterns is not as straightforward. There are two major differences between the PrefixSpan algorithm and our CFR-PostfixSpan algorithm. First, the proposed algorithm needs to deal with the time stamp of each item in data sequences while the PrefixSpan algorithm is only concerned with the order of items in data sequences. Without knowing items’ times, it is impossible to check the recency and compactness constraints. Second, the proposed algorithm projects a database based on the <sup>b</sup>frequent recent postfixes<sup>Q</sup> while the PrefixSpan algorithm projects a database based on the <sup>b</sup>frequent prefixes<sup>Q</sup>. As mentioned previously, a pattern may occur in a sequence several times, but the last occurrence is the most important, since if it does not satisfy the recency constraint, then neither will all the preceding patterns. Projecting the database using postfixes instead of prefixes can improve the efficiency of the algorithm because patterns that do not satisfy the recency constraint can be removed earlier. The CFR-PostfixSpan algorithm is outlined in Fig. 2. The following gives a detailed explanation of the major steps of the algorithm.

## 4.1. Step 1: find 1-CFR-patterns

We scan the database once to find all 1-CFR-patterns. Here, we only need to preserve the 1-CFR-patterns as the postfix to project the database. Other 1- patterns, such as 1-CF-patterns but not 1-CFR-patterns, will not generate any CFR-patterns if used as the postfix to partition the database, since all of them will not satisfy the recency constraint.

![](/api/attachments/6UV7CHG8/fulltext/images/216a05aa085b0f251435058517b45eb680b0955e843995fac382096ca7bcf6fa.jpg)  
Fig. 2. The CFR-PostfixSpan algorithm.

Example 4. Consider the sequence database shown in Fig. 1. We scan the database once and count both the cf<sup>\_</sup>support and cr<sup>\_</sup>support of each item. They are h(a)i: (4, 0), h(b)i: (5, 3), h(c)i: (5, 4), h(d)i: (3, 1), h(e)i: (5, 1), and h( f)i: (2, 2), where hpatterni: (cf<sup>\_</sup>support, cr<sup>\_</sup>support) represents the pattern and its associated support counts. Let f<sup>\_</sup>minsup = 3 and r<sup>\_</sup>minsup = 2. The set of 1-CFR-patterns is {b, c}.

## 4.2. Step 2: divide search space

In the algorithm shown in Fig. 2, a denotes a compact recent postfix, and l is the length of a. In the projected databases, each data sequence has the same compact recent postfix a. For the sake of compactness, we remove a from each data sequence in $S | _ { \alpha }$ because all data sequences in $S | _ { \alpha }$ have the same postfix. Notice that each data sequence in $S | _ { \alpha }$ may generate more than one compact projection w.r.t. a. For each compact projection, both Sid and End<sup>\_</sup>time are recorded and the compactness constraint (the difference between the time stamp of the earliest item and End<sup>\_</sup>time must be smaller than or equal to ms<sup>\_</sup>length) is satisfied.

Following Example 4, we can partition the database into two subsets: (1) with postfix h(b)i (b-projected database), and (2) with postfix h(c)i (c-projected database). Let ms<sup>\_</sup>length = 7 and $t _ { \mathrm { R } } = 1 4$ . Suppose we want to build the b-projected database. In the first data sequence h(a, 1), (c, 3), (a, 4), (b, 4), (a, 6), (e, 6), (c, 10)i, item b is at position 4 and the compact projection w.r.t. item b is [4,10]: h(a, 1), (c, 3), (a,

4)i, where [sid, End<sup>\_</sup>time]: hcompact projectioni represents the compact projection and its sid and End<sup>\_</sup>time. Each item in the compact projection must satisfy the compactness constraint. Although item b in this data sequence does not satisfy the recency constraint $t _ { \mathrm { R } } ,$ we need to retain its compact projection to compute the cf<sup>\_</sup>support. In the second data sequence h(d, 5), (a, 7), (b, 7), (e, 7), (d, 9), (e, 9), (c, 14), (d, 14)i, item b is at position 3 and the compact projection w.r.t. item b is [7,20]: h(d, 5), (a, 7)i. In the third data sequence h(a, 8), (b, 8), (e, 11), (d, 13), (b, 16), ( f, 16), (c, 20)i, item b is at positions 2 and 5. For position 2, the compact projection w.r.t. b is [8,30]: h(a, 8)i, and for position 5, the compact projection w.r.t. b is [17,30]: h(b, 9), (e, 11), (d, 13)i. Continuing in this manner yields the entire b’s projected databases. Fig. 3 shows the $b \mathbf { \hat { s } }$ and $c \mathbf { \hat { s } }$ projected databases.

## 4.3. Step 3: find subsets of sequential patterns

The CFR-patterns can be found by constructing the corresponding projected databases and recursively mining each one. An explanation of the mining process follows Example 4.

<table><tr><td>postfix</td><td>sid</td><td>end time</td><td>projected (prefix) database</td></tr><tr><td rowspan="8">(b)</td><td>10</td><td>4</td><td></td></tr><tr><td>20</td><td>7</td><td></td></tr><tr><td>30</td><td>16</td><td></td></tr><tr><td>30</td><td>8</td><td></td></tr><tr><td>40</td><td>22</td><td></td></tr><tr><td>50</td><td>19</td><td></td></tr><tr><td>50</td><td>17</td><td></td></tr><tr><td>50</td><td>6</td><td></td></tr><tr><td rowspan="6">(c)</td><td>10</td><td>10</td><td></td></tr><tr><td>10</td><td>3</td><td></td></tr><tr><td>20</td><td>14</td><td></td></tr><tr><td>30</td><td>20</td><td></td></tr><tr><td>40</td><td>22</td><td></td></tr><tr><td>50</td><td>19</td><td></td></tr></table>

Fig. 3. The b’s and c’s projected database.

All the projected databases are shown in Fig. 3. First, let us find CFR-patterns with the postfix h(b)i. The b’s projected database consists of 8 compact projections. For the first compact projection [4,10]: h(a, 1), (c, 3), (a, 4)i, the End<sup>\_</sup>time is 4 (does not satisfy the recency constraint) and only the cf<sup>\_</sup>support of each pattern will be counted (the cf<sup>\_</sup>support of h(a)(b)i, h(c)(b)i, and h(ab)i plus 1). Similarly, for the second compact projection [7,20]: h(d, 5), (a, 7)i, the cf<sup>\_</sup>supports of h(d)(b)i and h(ab)i will be added by 1. For the third compact projection [17,30]: h(b, 9), (e, 11), (d, 13), ( f, 16)i, since the End<sup>\_</sup>time is 16 (satisfying the recency constraint), both cf<sup>\_</sup>support and cr<sup>\_</sup>support of each pattern will be counted (both cf<sup>\_</sup>support and cr<sup>\_</sup>support of h(bb)i, h(e)(b)i, h(d)(b)i, h( f)(b)i plus 1). The remaining compact projections can be mined in the same manner.

For a compact projection, we count the cr<sup>\_</sup>supports of patterns occurred if its End<sup>\_</sup>time satisfies the recency constraint. After counting each pattern in the b-projected database, we obtain the 2-CFR-patterns w.r.t. postfix h(b)i as follows: h(a)(b)i: (4, 2), and h(b)(b)i: (3, 3).

Recursively partitioning the database, all data sequences with the postfix h(b)i can be divided into 2 subsets: (1) those with postfix h(a)(b)i, and (2) those with postfix h(b)(b)i. To mine these subsets, construct respective projected databases and mine each for all the 3-CFR-patterns w.r.t. the corresponding postfixes.

## 5. Experimental study

In this section, we perform a simulation study to empirically compare the proposed algorithm with the traditional sequential pattern mining methods. Three algorithms (the GSP [33], the PrefixSpan [29], and the CFR-PostfixSpan algorithms) were implemented in Java language and tested on a Pentium IV-1.8 GHz Windows 2000 system with 1 gigabyte of main memory. We ignored the time stamp for the GSP algorithm and the PrefixSpan algorithm because they were designed for mining sequential patterns without time stamps.

## 5.1. Data

Several synthetic data sets and real data sets are used to evaluate the performance of the proposed method. The synthetic data are generated by modifying Trad<sup>\_</sup> datagen, the well-known data generation algorithm [1]. Modification is necessary because the environment in the original data generation program differs from ours in the following ways:

1. The original program assumes that the environment is static over time, whereas we assume that the environment is dynamic.

2. The original program generates a set of sequences, each of which is an ordered list of itemsets without time stamps. In our model, an itemset in the sequence must be associated with a time stamp.

As a result of these differences, Trad<sup>\_</sup>datagen was revised in several ways. The details of the modification are in Appendix A. Table 1 lists the parameters set in our data generation algorithm; the first eight parameters are the ones classically used in Trad<sup>\_</sup>datagen, but the last three $( T _ { I } , \ T _ { p } ,$ and $R _ { r } )$ are new parameters created for the problem considered here. The goal of these three parameters is to evaluate the influence of the degree of changing environment. For ease of comparison, we only use $R _ { r }$ as a changeable parameter and keep the other two fixed; we set $T _ { p } = 3 0$ and $T _ { I } { = } 7 .$ In the simulation, some parameters are fixed: N = 10 000, $N _ { S } { = } 5 0 0 0 .$ $\scriptstyle N _ { I } = 2 5 , 0 0 0$ , |C| = 10, |S| = 4 and |I| = 1.25. Other parameter settings of synthetic data generation are shown in Table 2.

We also investigated several real-life sequential data sets in our experiments. The first real data set, called SC-POS, is the sales data of a chain supermarket in Taiwan. The SC-POS data set recorded all transactions from twenty branches between 2001/12/27 and 2002/ 12/31. Each transaction in the SC-POS data set is the customer’s shopping list, where the purchase date, time, and purchased items are recorded. A series of data preprocessing and cleaning tasks were performed, including combining the sequence data from all stores of this chain, removing uninteresting items and transactions that did not use a member card, and merging the transactions of the same customer into one data se-

Parameters |D| Number of customers |C| Average number of transactions per customer |T| Average number of items per transaction |S| Average length of maximal potentially large sequences |I| Average size of itemsets in maximal potentially large sequences $N _ { S }$ Number of maximal potentially large sequences $N _ { I }$ Number of maximal potentially large itemsets $N$ Number of items $T _ { I }$ Average length between two adjacent transactions $T _ { p }$ The length of time period $R _ { r }$ The replacement rate of PLS per period

Table 2  
Parameter settings of synthetic data generation

<table><tr><td>Name</td><td> $|D|$ </td><td> $|C|$ </td><td> $|T|$ </td><td> $|S|$ </td><td> $|I|$ </td><td> $|T_I|$ </td><td> $|T_p|$ </td><td> $|R_r|$ </td></tr><tr><td>SYN-DS1</td><td>250K</td><td>10</td><td>2.5</td><td>4</td><td>1.25</td><td>7</td><td>30</td><td>0.2</td></tr><tr><td>SYN-DS2</td><td>500K</td><td>10</td><td>2.5</td><td>4</td><td>1.25</td><td>7</td><td>30</td><td>0.2</td></tr><tr><td>SYN-DS3</td><td>750K</td><td>10</td><td>2.5</td><td>4</td><td>1.25</td><td>7</td><td>30</td><td>0.2</td></tr><tr><td>SYN-DS4</td><td>250K</td><td>10</td><td>5</td><td>4</td><td>1.25</td><td>7</td><td>30</td><td>0.2</td></tr><tr><td>SYN-DS5</td><td>250K</td><td>10</td><td>7.5</td><td>4</td><td>1.25</td><td>7</td><td>30</td><td>0.2</td></tr><tr><td>SYN-DS6</td><td>250K</td><td>10</td><td>2.5</td><td>4</td><td>1.25</td><td>7</td><td>30</td><td>0.1</td></tr><tr><td>SYN-DS7</td><td>250K</td><td>10</td><td>2.5</td><td>4</td><td>1.25</td><td>7</td><td>30</td><td>0.3</td></tr></table>

quence. The SC-POS data set contained 18,162 items and 102,601 customers’ data sequences. Moreover, due to all items having their own predefined concept taxonomies from the primitive level concept to the higher one, we also generalized the SC-POS data set to a higher level of abstraction. Hence, two more data sets, SC-POS-lv1 and SC-POS-lv2, were generated in our study. The SC-POS-lv1 data set contains 561 items while the SC-POS-lv2 only contains 133 items.

The second real data set, called NASA-LOG, is the NASA Web server log, which recorded all HTTP requests by the NASA Kennedy Space Center WWW server in Florida from 1995/7/1 to 1995/8/31. The data set is available at http://ita.ee.lbl.gov/html/contrib/ NASA-HTTP.html. In the NASA-LOG data set, we only kept the requests that asked for html files. Other noisy requests, such as requests for image files, have been removed. Moreover, requests from the same IP were treated as the same user, as in the same data sequence. The final data set contains 2174 items and 118,336 data sequences.

## 5.2. Performance measures

In the experiments, we consider both the efficiency and effectiveness of the CFR-PostfixSpan algorithm.

The efficiency tests are designed to compare the run times using several synthetic data sets as well as reallife data sets. To evaluate effectiveness, we first examine the number of patterns discovered from traditional approaches and ours. As mentioned in Section 1, our expectation in this study was to discover sequential patterns that were important in both the long run and in recent periods. It is important to see what percentages of patterns were eliminated when considering both the long run and recent periods instead of just considering the long run. We conducted a case study, and in this work we demonstrate four kinds of patterns mined from real-life data sets and discuss what we learned from them.

## 5.3. Experimental setup

We have designed four tests to evaluate the proposed method. The first three tests are designed for the evaluation of efficiency, while the last one evaluates effectiveness. The data sets with corresponding parameter settings used in our experiments are shown in Table 3.

Test I was executed based on the SYN-DS1 data set and two real-life data sets. We compared the run times of the three algorithms. In Test II, seven synthetic data sets were used to perform scalability analysis, which varied the value of $| D |$ (from 250K to 750K), |T| (from 2.5 to 7.5), and $| R _ { r } |$ (from 0.1 to 0.3). Test III evaluated the scale-up effect for the parameters unique to CFR patterns, $t _ { \mathrm { R } } ,$ ms<sup>\_</sup>length, and r<sup>\_</sup>minsup. The NASA-LOG data set was used for this test and we varied the value of a single parameter and kept all the other parameters constant. Test IV used all the synthetic and real-life data sets to compare the number of patterns between traditional sequential pattern mining and our approach. Four kinds of patterns were generated in our experiments, consisting of \*F\*, CF\*, \*FR, and CFR patterns. Some patterns discovered from the SC-POSlv2 data set are summarized.

Table 3  
Parameter settings of different tests

<table><tr><td>Test</td><td>Data set</td><td>f_minsup</td><td>r_minsup</td><td> $t_R$ </td><td>ms_length</td></tr><tr><td rowspan="3">I</td><td>SYN-DS 1</td><td>1.25–0.75%</td><td>0.3125–0.1875%</td><td>53</td><td>15</td></tr><tr><td>SC-POS</td><td>4.5–3.75%</td><td>1.125–0.9375%</td><td>277</td><td>60</td></tr><tr><td>NASA-LOG</td><td>1.25–0.75%</td><td>0.3125–0.1875%</td><td>45</td><td>15</td></tr><tr><td rowspan="3">II</td><td>SYN-DS 1, 2, 3</td><td>1.25–0.75%</td><td>0.3125–0.1875%</td><td>53</td><td>15</td></tr><tr><td>SYN-DS 1, 4, 5</td><td>1.25–0.75%</td><td>0.3125–0.1875%</td><td>53</td><td>15</td></tr><tr><td>SYN-DS 1, 6, 7</td><td>1.25–0.75%</td><td>0.3125–0.1875%</td><td>53</td><td>15</td></tr><tr><td rowspan="3">III</td><td>NASA-LOG</td><td>1%</td><td>0.25%</td><td>30–60</td><td>15</td></tr><tr><td>NASA-LOG</td><td>1%</td><td>0.25%</td><td>45</td><td>5–30</td></tr><tr><td>NASA-LOG</td><td>1%</td><td>0.05–0.45%</td><td>45</td><td>15</td></tr><tr><td rowspan="5">IV</td><td>SYN-DS 1–7</td><td>1%</td><td>0.25%</td><td>53</td><td>15</td></tr><tr><td>NASA-LOG</td><td>1%</td><td>0.25%</td><td>45</td><td>15</td></tr><tr><td>SC-POS</td><td>3.75%</td><td>0.9375%</td><td>277</td><td>60</td></tr><tr><td>SC-POS-lv1</td><td>10%</td><td>5%</td><td>277</td><td>90</td></tr><tr><td>SC-POS-lv2</td><td>20%</td><td>12%</td><td>277</td><td>90</td></tr></table>

![](/api/attachments/6UV7CHG8/fulltext/images/26169bb1dd5f84112d3ebe57ac55a98a9cc81894b933ddb7823405d25626d2bb.jpg)  
Fig. 4. Run time vs. minsup (SYN-DS1).

## 6. Results and discussions

This section reports the simulation results based on the four tests addressed in Section 5.3.

Test I compared the run times of the three algorithms. Fig. 4 illustrates the results of the SYN-DS1 data set and it indicates that the CFR-PostfixSpan algorithm is the fastest, followed by the PrefixSpan algorithm, and finally the GSP algorithm. These results seem slightly counter-intuitive, because more complicated patterns take less time than simpler ones. One possible reason may be that the most important factor influencing the run time is not the complexity of the algorithm or pattern, but the number of patterns we need to process. When more constraints are added, more candidate patterns are removed; thus, fewer patterns have to be processed and the run time decreases. The results of the SC-POS data set are shown in Fig. 5.

![](/api/attachments/6UV7CHG8/fulltext/images/6c9d9418524ffa0b4e3691dce8063af00b6a269f4528c31dd93cee04458f2718.jpg)  
Fig. 5. Run time vs. minsup (SC-POS).

![](/api/attachments/6UV7CHG8/fulltext/images/10db95f6aa4a5c06d1dd0385f4dfa71f22338f17c02c4e1479f96f3321b465e1.jpg)  
Fig. 6. Run time vs. |D|.

Unsurprisingly, the CFR-PostfixSpan algorithm is the fastest. But the PrefixSpan algorithm is not applicable here because its run time becomes unmanageably long. To understand why, note that the PrefixSpan algorithm needs to store the entire compressed database in the main memory, causing its performance to become very sensitive to the amount of main memory available. Since supermarket data sequence length can be very long, a great deal of main memory is needed to store the compressed database. The operating system is then forced to swap the data between the main memory and the hard disks, increasing its run time dramatically. The CFR-PostfixSpan algorithm is stronger because the compactness constraint restricts the length of the sequence. By setting the ms<sup>\_</sup>length, the length of data sequences we need to store in the main memory is greatly reduced, resulting in strong performances with long sequence data.

In Test II, the scalabilities of the three algorithms were performed. To begin, we varied the value of |D from 250K to 750K. According to the results in Fig. 6, the CFR-PostfixSpan algorithm is the fastest, followed by the PrefixSpan, and finally the GSP. All three algorithms scale up linearly with |D|. Fig. 7 shows the results of varying the value of |T| from 2.5 to 7.5. All three algorithms scale up exponentially with |T|. Moreover, we noted that the PrefixSpan algorithm becomes the slowest when |T| is large. We also observed that the CFR-PostfixSpan algorithm remains the fastest at all times. These two observations correspond with Test I, which shows that as the sequence length becomes longer, the PrefixSpan algorithm deteriorates. Fig. 8 evaluates the scale-up effect by varying the value of $| R _ { r } |$ from 0.1 to 0.3. The results reveal that as the value of $R _ { r }$ increases, the run time decreases. A possible reason is that increasing the value of $R _ { r }$ makes the environment more dynamic, causing the supports of candidate patterns to become smaller, and thus fewer patterns are generated. As a result, we can spend less time processing these patterns, and the run time is reduced.

![](/api/attachments/6UV7CHG8/fulltext/images/11fadfbe5fadff486bbef3d6e12db78c07f7559d09c999c628cb91035212d75a.jpg)  
Fig. 7. Run time vs. |T|.

![](/api/attachments/6UV7CHG8/fulltext/images/00c41eb0301ac52bde95fb4546b2826759529c9961d2774401619a641385925b.jpg)  
Fig. 8. Run time vs. $R _ { r }$ .

Test III evaluated the scale-up effect for the parameters unique to CFR patterns, $t _ { \mathrm { R } } ,$ ms<sup>\_</sup>length, and r<sup>\_</sup>minsup. We first varied the recency time, $t _ { \mathrm { R } } .$ The results indicate that $t _ { \mathrm { R } }$ has little impact on the run time, but as $t _ { \mathrm { R } }$ increases, the number of patterns decreases. This result matches our expectations, because if $t _ { \mathrm { R } }$ increases, then the recency window shrinks and a candidate pattern is less likely to be frequent. The second test varies the maximum span length, ms<sup>\_</sup>length. The results show that as ms<sup>\_</sup>length increases, the run times of the two algorithms and the number of patterns increase. This is because if the max-span window is enlarged, more candidate patterns become frequent, so the run time and the number of patterns increase. The final test varies recency minsup, r<sup>\_</sup>minsup. It shows that as r<sup>\_</sup>minsup increases, the run times of the two algorithms and the number of patterns decrease. The lower the value of r<sup>\_</sup>minsup, the more difficult it is for a pattern to be frequent, and thus fewer patterns are generated and less time is needed to process these patterns.

In Test IV, we explored how the recency and compactness constraints influence the generation of sequential patterns. Four kinds of patterns are shown here, CFR patterns, CF\* patterns, \*FR patterns, and \*F\* patterns, where \*F\* patterns are the traditional sequential patterns. Table 4 lists the amounts of these four patterns and their corresponding percentages with respect to the traditional patterns (\*F\*). The results indicate that approximately one-fourth to one-half of the traditional sequences are not recent and compact. The situation worsens with long sequence data, where about two-thirds of traditional patterns are not recent and compact.

The four kinds of patterns discovered in SC-POS-lv2 are summarized in Fig. 9. Due to the high number of patterns, we only list patterns related to four items, Canned Food, Ice, Instant Noodles, and Paper Products. In Fig. 9, we can see that all four items are \*F\* patterns, or traditional patterns. Once we consider the recency constraint, item Ice becomes eliminated in the sets of CFR and \*FR patterns. Our investigation indicates that item Ice was purchased frequently between 2002/6/1 and 2002/9/30, but rarely after 2002/10/1. This causes item Ice to not satisfy the recency threshold since we set the recency time at $t _ { \mathrm { R } } { = } 2 7 7$ , or 2002/ 9/30. The result shows that customers buy item Ice frequently during the summer, but hardly at all after fall. Such patterns cannot provide any support for decisions and can even confuse decision makers. However, our study can eliminate it after considering the recency constraint. Moreover, we find that a pattern h(Paper Product)(Instant Noodles)i holds in the set of \*F\* patterns, but not in the set of CFR patterns (ms<sup>\_</sup>length = 90). This means that most of the purchases implied by this pattern occur over three months, thus reducing the significance of the pattern.

Number of patterns in different data sets

<table><tr><td>Pattern type Data sets</td><td colspan="2">CFR</td><td colspan="2">CF*</td><td colspan="2">*FR</td><td colspan="2">*F*</td></tr><tr><td>Name</td><td># of patterns</td><td>%</td><td># of patterns</td><td>%</td><td># of patterns</td><td>%</td><td># of patterns</td><td>%</td></tr><tr><td>SYN-DS1</td><td>301</td><td>73.77</td><td>337</td><td>82.60</td><td>372</td><td>91.18</td><td>408</td><td>100</td></tr><tr><td>SYN-DS2</td><td>310</td><td>75.61</td><td>347</td><td>84.63</td><td>374</td><td>91.22</td><td>410</td><td>100</td></tr><tr><td>SYN-DS3</td><td>307</td><td>74.70</td><td>344</td><td>83.70</td><td>375</td><td>91.24</td><td>411</td><td>100</td></tr><tr><td>SYN-DS4</td><td>1692</td><td>70.03</td><td>1979</td><td>81.91</td><td>2235</td><td>92.51</td><td>2416</td><td>100</td></tr><tr><td>SYN-DS5</td><td>2944</td><td>33.97</td><td>3325</td><td>38.36</td><td>8335</td><td>96.17</td><td>8667</td><td>100</td></tr><tr><td>SYN-DS6</td><td>416</td><td>79.54</td><td>469</td><td>89.67</td><td>467</td><td>89.29</td><td>523</td><td>100</td></tr><tr><td>SYN-DS7</td><td>231</td><td>84.93</td><td>260</td><td>95.59</td><td>245</td><td>90.07</td><td>272</td><td>100</td></tr><tr><td>SC-POS</td><td>409</td><td>54.90</td><td>523</td><td>71.41</td><td>627</td><td>84.16</td><td>745</td><td>100</td></tr><tr><td>SC-POS-lv1</td><td>348</td><td>29.24</td><td>633</td><td>53.19</td><td>944</td><td>79.33</td><td>1190</td><td>100</td></tr><tr><td>SC-POS-lv2</td><td>106</td><td>25.18</td><td>262</td><td>62.23</td><td>329</td><td>78.15</td><td>421</td><td>100</td></tr><tr><td>NASA-LOG</td><td>158</td><td>71.17</td><td>181</td><td>81.53</td><td>206</td><td>92.79</td><td>222</td><td>100</td></tr></table>

<table><tr><td>CFR pattern</td><td>CF* pattern</td></tr><tr><td>(Canned Food)(Canned Food)(Canned Food)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Paper Product)(Canned Food)(Paper Product)(Paper Product)</td><td>(Canned Food)(Canned Food)(Canned Food)(Ice)(Canned Food)(Instant Noodles)(Canned Food)(Paper Product)(Ice)(Canned Food)(Ice)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Nombres)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Niosles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Nodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(InstantNoodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(InstantNiosles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)( Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)( Instant Niosles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)</td></tr><tr><td>*FR pattern</td><td>*F* pattern</td></tr><tr><td>(Canned Food)(Canned Food)(Canned Food)(Canned Food)(Canned Food)(Instant Noodles)(Canned Food)(Paper Product)(Instant Noodles)(Canned Food)(Canned Food)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Paper Product)(Paper Product)(Canned Food)(Paper Product)(Instant Noodles)(Paper Product)(Paper Product)</td><td>(Canned Food)(Canned Food)(Canned Food)(Canned Food)(Canned Food)(Instant Noodles)(Canned Food)(Ice)(Canned Food)(Paper Product)(Ice)(Canned Food)(Ice)(Ice)(Ice)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)( Instant Noidles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant 100% (Instant 100% (Instant 100% (Instant 100% (Instant 100% (Instant 100% (Instant 100% (Instant 100% (Instant 100% (Instant 100% (Instant 100% (Instant 100% (Instant 100% (Instant 100% (Instant 100% (Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)(Instant Noodles)</td></tr></table>

Fig. 9. Different kinds of rules discovered from SC-POS-lv2.

## 7. Conclusions and future works

Sequential pattern mining is a useful and important method to discover customer-purchasing behavior from databases. Since the sequential pattern mining problem was first proposed by Agrawal and Skrikant, many approaches have been presented. Most existing methods, however, focus on the concept of frequency in the sequence databases and do not consider the concepts of recency and compactness.

To solve this problem, we first defined an extension of the traditional pattern, called the CFR pattern, to include recency and compactness. Then a novel algorithm, the CFR-PostfixSpan algorithm, was proposed for finding CFR patterns.

Detailed experiments were also presented. Several synthetic data sets and real-life data sets were used in our performance analyses and scalability tests were also given. As discussed in Section 6, the PrefixSpan algorithm needs to build larger projected databases in the main memory, which greatly reduces the possibility of use in long-sequence databases. The proposed CFR-PostfixSpan algorithm, however, performs well in all kinds of situations. It is also a generalization of the traditional algorithms, and by setting r<sup>\_</sup>minsup and ms<sup>\_</sup>length properly, many uninteresting patterns can be pruned and other interesting ones can be further discovered.

This paper can be extended in several ways. First, the crisp recency constraint considered here can be extended so that a fuzzy recency time constraint is used instead. Second, since it is difficult for a user to set all parameters simultaneously, an immediate problem is how to maintain the discovered patterns as the user adjusts the parameters. Finally, we may consider adding other useful constraints to the CFR pattern, such as the constraint that the number of repetitions in a sequence must be no less than a given threshold.

## Acknowledgments

This research was supported in part by the Ministry of Education (MOE) Program for Promoting Academic Excellence of Universities under Grant No. 91-H-FA07-1-4.

## Appendix A. The generation of synthetic data set

The Trad<sup>\_</sup>datagen was revised in several ways. We only report the main modifications here and details of Trad<sup>\_</sup>datagen can be found in [1].

(1) Since the environment is dynamic, we assume that the set of potential large sequence (PLS) may be different for different time periods. Therefore, we cut the timeline into periods, each with length $T _ { p } .$ . Let $R _ { r }$ $( 0 \leq R _ { r } \leq 1 )$ be the replacement rate of PLS in every period. We generate PLS for the first period, and then we generate PLS in the next period based on PLS in the current period. For each sequence in the current PLS, we produce a random number ranging from 0 to 1 and compare it with $R _ { r }$ . If the random number is smaller than $R _ { r } ,$ we remove this sequence and generate a new one to replace it. Otherwise, we carry over this sequence into the next period.

(2) When generating a data sequence, we first determine the number of transactions in this data sequence and the average size of each transaction. This process is the same as Trad<sup>\_</sup>datagen, but the transaction data are extended such that different itemsets are associated with different time stamps. A value w is drawn from a Poisson distribution with mean $T _ { I }$ for each data sequence. The drawn value w represents the average time interval between successive itemsets in the data sequence. The intervals between successive itemsets of a customer are determined by repetitively drawing values from a Poisson distribution with mean w. After all time stamps of the data sequence are decided, we identify which time period each transaction belongs to. We then randomly choose a series of sequences from the corresponding PLS.

## References

[1] R. Agrawal, R. Srikant, Mining sequential patterns, Proceedings of the 11th International Conference on Data Engineering, Taipei, Taiwan, 1995.

[2] R. Agrawal, C. Faloutsos, A. Swami, Efficient similarity search in sequence databases, Lecture Notes in Computer Science 730 (1993) 69 – 84.

[3] C.Y. Chang, M.S. Chen, C.H. Lee, Mining general temporal association rules for items with different exhibition periods, IEEE International Conference on Data Mining, Maebashi City, Japan, 2002.

[4] M.S. Chen, J. Han, P.S. Yu, Data mining: an overview from a database perspective, IEEE Transactions on Knowledge and Data Engineering 8 (6) (1996) 866 – 883.

[5] M.S. Chen, J.S. Park, P.S. Yu, Efficient data mining for path traversal patterns, IEEE Transactions on Knowledge and Data Engineering 10 (2) (1998) 209 – 221.

[6] R.S. Chen, G.H. Tzeng, C.C. Chen, Y.C. Hu, Discovery of fuzzy sequential patterns for fuzzy partitions in quantitative attributes, ACS/IEEE International Conference on Computer Systems and Applications, Beirut, Lebanon, 2001.

[7] Y.L. Chen, S.S. Chen, P.Y. Hsu, Mining hybrid sequential patterns and sequential rules, Information Systems 27 (5) (2002) 345–362.

[8] Y.L. Chen, M.C. Chiang, M.T. Kao, Discovering time-interval sequential patterns in sequence databases, Expert Systems with Applications 25 (3) (2003) 343 – 354.

[9] R. Cooley, B. Mobasher, J. Srivastava, Data preparation for mining world wide web browsing patterns, Journal of Knowledge and Information Systems 1 (1) (1999) 5 – 32.

[10] G. Dong, J. Li, Efficient mining of emerging patterns: discovering trends and differences, Proceedings of ACM SIGKDD Conference on Knowledge Discovery and Data Mining, San Diego, California, 1999.

[11] C. Faloutsos, M. Ranganathan, Y. Manolopoulos, Fast subsequence matching in time-series databases, Proceedings of the ACM SIGMOD International Conference on Management of Data, Minneapolis, Minnesota, 1994.

[12] W.J. Frawley, G. Piatetsky-Shapiro, C.J. Matheus, Knowledge Discovery in Databases: An Overview, AAAI/MIT Press, 1991.

[13] K. Gade, J. Wang, G. Karypis, Efficient closed pattern mining in the presence of tough block constraints, Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, Seattle, Washington, USA, 2004.

[14] M.N. Garofalakis, R. Rastogi, K. Shim, SPIRIT: sequential pattern mining with regular expression constraints, Proceedings of 25th VLDB Conference, Edinburgh, Scotland, 1999.

[15] J. Han, M. Kamber, Data Mining: Concepts and Techniques, Academic Press, 2001.

[16] J. Han, W. Gong, Y. Yin, Mining segment-wise periodic patterns in time-related databases, Proceedings of 4th International Conference on Knowledge Discovery and Data Mining, New York City, New York, 1998.

[17] J. Han, G. Dong, Y. Yin, Efficient mining of partial periodic patterns in time series database, Proceedings of 15th International Conference on Data Engineering, Sydney, Australia, 1999.

[18] J. Han, J. Pei, B. Mortazavi-Asl, Q. Chen, U. Dayal, M.C. Hsu, FreeSpan: frequent pattern-projected sequential pattern mining, Proceedings of 6th International Conference on Knowledge Discovery and Data Mining, Boston, Massachusetts, 2000.

[19] B. LeBaron, A.S. Weigend, A bootstrap evaluation of the effect of data splitting on financial time series, IEEE Transactions on Neural Networks 9 (1) (1998) 213 – 220.

[20] C.H. Lee, M.S. Chen, C.R. Lin, Progressive partition miner: an efficient algorithm for mining general temporal association rules, IEEE Transactions on Knowledge and Data Engineering 15 (4) (2003) 1004–1017.

[21] Y. Li, P. Ning, X.S. Wang, S. Jajodia, Discovering calendarbased temporal association rules, Proceedings of the 8th International Symposium on Temporal Representation and Reasoning, Cividale, Italy, 2001, pp. 111 – 118.

[22] M.Y. Lin, S.Y. Lee, S.S. Wang, DELISP: efficient discovery of generalized sequential patterns by delimited pattern-growth technology, Lecture Notes in Computer Science 2336 (2002) 198– 209.

[23] B. Liu, Y. Ma, R. Lee, Analyzing the interestingness of association rules from the temporal dimension, IEEE International Conference on Data Mining, Silicon Valley, California, 2000.

[24] S. Ma, J.L. Hellerstein, Mining partially periodic event patterns with unknown periods, Proceedings of the 17th International Conference Data Engineering, Heidelberg, Germany, 2001.

[25] H. Mannila, H. Toivonen, A. Inkeri Verkamo, Discovery of frequent episodes in event sequences, Data Mining and Knowledge Discovery 1 (3) (1997) 259 – 289.

[26] K. Mehta, S. Bhattacharyya, Adequacy of training data for evolutionary mining of trading rules, Decision Support Systems 37 (4) (2004) 461– 474.

[27] J. Pei, J. Han, Constrained frequent pattern mining: a patterngrowth view, ACM SIGKDD Explorations Newsletter 4 (1) (2002) 31–39.

[28] J. Pei, G. Dong, W. Zou, J. Han, On computing condensed frequent pattern bases, Proceedings of the IEEE International Conference on Data Mining, Maebashi City, Japan, 2002.

[29] J. Pei, J. Han, B. Mortazavi-Asl, J. Wang, H. Pinto, Q. Chen, U. Dayal, M.-C. Hsu, Mining sequential patterns by patterngrowth: the PrefixSpan approach, IEEE Transactions on Knowledge and Data Engineering 16 (10) (2004) 1424– 1440.

[30] J. Pei, G. Dong, W. Zou, J. Han, Mining condensed frequentpattern bases, Knowledge and Information Systems 6 (5) (2004) 570– 594.

[31] Helen Pinto, J. Han, J. Pei, K. Wang, Q. Chen, Umeshwar Dayal, Multi-dimensional sequential pattern mining, Proceedings of the 10th International Conference on Information and Knowledge Management, Atlanta, Georgia, 2001.

[32] H.S. Song, J.K. Kim, S.H. Kim, Mining the change of customer behavior in an internet shopping mall, Expert Systems with Applications 21 (3) (2001) 157 – 168.

[33] R. Srikant, R. Agrawal, Mining sequential patterns: generalizations and performance improvements, Research Report RJ 9994, IBM Almaden Research Center, San Jose, California, 1995.

[34] R. Srikant, R. Agrawal, Mining sequential patterns: generalizations and performance improvements, Proceedings of the 5th

International Conference on Extending Database Technology, Avignon, France, 1996.

[35] J. Srivastava, Mining temporal data, http://www.cs.umn.edu research/websift/survey/.

[36] R. Srikant, Y. Yang, Mining web logs to improve website organization, Proceedings of the 10th International World Wide Web Conference, Hong Kong, 2001.

[37] S.L. Wang, C.Y. Kuo, T.P. Hong, Mining fuzzy similar sequential patterns from quantitative data, IEEE International Conference on Systems, Man and Cybernetics, Hammamet, Tunisia, 2002.

[38] X. Yan, J. Han, CloSpan: mining closed sequential patterns in large datasets, Proceedings of the 2003 SIAM International Conference on Data Mining (SDM’03), San Francisco, California, May, 2003.

[39] J. Yang, P. Yu, W. Wang, J. Han, Mining long sequential patterns in a noisy environment, Proceedings of the 2002 ACM SIG-MOD International Conference on Management of Data, Madison, Wisconsin, 2002, pp. 406–417.

[40] M.J. Zaki, SPADE: an efficient algorithm for mining frequent sequences, Machine Learning Journal 42 (1–2) (2001) 31 – 60.

[41] Q. Zhao, S.S. Bhowmick, Sequential pattern mining: a survey, Technical Report Center for Advanced Information Systems, School of Computer Engineering, Nanyang Technological University, Singapore, 2003.

![](/api/attachments/6UV7CHG8/fulltext/images/7d25db007684009f7cc12b8daebcbc4a2acd0fb7d9c30ef69e33334257d9a84f.jpg)

Yen-Liang Chen is a Professor and Chairperson of Information Management at the National Central University of Taiwan. He received his Ph.D. degree in computer science from National Tsing Hua University, Hsinchu, Taiwan. His current research interests include data modeling, data mining, data warehousing and operations research. He has published papers in Operations Research, Decision Support Systems, IEEE Transactions on Knowledge and Data Engineering,

IEEE Transactions on Software Engineering, Computers & OR, European Journal of Operational Research, Information and Management, Information Processing Letters, Information Systems, Journal of Operational Research Society, and Transportation Research.

![](/api/attachments/6UV7CHG8/fulltext/images/c844f0a191d491fee37d174d904daa0bb36c5a15863106294d66af566b3ee911.jpg)

Ya-Han Hu is currently a PhD student in the Department of Information Management, National Central University, Taiwan. He received his M.S. degree in Information Management from National Central University of Taiwan. His research interests include data mining, information systems and EC technologies. His research has appeared in Decision Support Systems.
