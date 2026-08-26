---
otero_id: 4582
otero_key: "5VBE7BZW"
title: "New approach for the sequential pattern mining of high-dimensional sequence databases"
authors: "Hongyan Liu; Fangzhou Lin; Jun He; Yunjue Cai"
year: "2010"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.08.029"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# New approach for the sequential pattern mining of high-dimensional sequence databases

Hongyan Liu <sup>a,</sup>⁎, Fangzhou Lin <sup>a</sup>, Jun He <sup>b,</sup>⁎, Yunjue Cai <sup>a</sup>

<sup>a</sup> Department of Management Science and Engineering, Tsinghua University, Beijing, China

<sup>b</sup> Key Laboratory of Data Engineering and Knowledge Engineering, MOE, Beijing, China

## a r t i c l e i n f o

Article history: Received 20 March 2009 Received in revised form 4 August 2010 Accepted 17 August 2010 Available online 21 August 2010

Keywords: Sequential pattern mining High-dimensional database Data mining

## a b s t r a c t

In this paper a new algorithm, the Top-Down mining of Sequential patterns (TD-Seq), for mining sequential patterns from high-dimensional stock sequence databases is presented. Existing algorithms are limited by ef<sup>fi</sup>ciency problems in dealing with high-dimensional sequence databases. To address this problem, a twophase mining method is proposed, in which a top-down transposition-based searching strategy as well as a new support counting method are exploited. Three pruning rules were also developed to reduce the search space further. Experiments conducted on actual databases demonstrate the improved performance of TD-Seq over existing algorithms.

© 2010 Elsevier B.V. All rights reserved

## 1. Introduction

Sequential pattern mining is one of the most important problems in data mining. It has various applications including usage in customer purchase behavior analysis [17], webpage access pattern detection, disease treatment pattern analysis, DNA sequence analysis, stock sequence analysis, plan failure identi<sup>fi</sup>cation [21], network alarm pattern mining [7], and XML query access pattern analysis [5]. It was <sup>fi</sup>rst introduced by Agrawal and Srikant [2], after which many algorithms have been proposed for ef<sup>fi</sup>cient mining of frequent sequences [2,3,13,14,16,20,22], frequent closed sequences [18,19] and extension of sequential patterns [4] from the sequence database. Mining frequent closed sequences can provides a compact and complete result set, and better ef<sup>fi</sup>ciency than mining frequent sequences.

In this paper, strategies on <sup>fi</sup>nding sequential patterns ef<sup>fi</sup>ciently from stock exchange time-series data (herein referred to as stock sequence database after transformation) are studied. When existing algorithms were applied to this kind of database, the performance of these algorithms was found to be not very satisfying. They required a long running time (low ef<sup>fi</sup>ciency problem) and produced a huge volume of results. These algorithms are developed for deep and narrow sequence databases, which causes low ef<sup>fi</sup>ciency because many sequence data in real applications, such as stock sequence database, are shallow and wide (high-dimensional). Low ef<sup>fi</sup>ciency also stems from repeated counting and inequality of counting because of the method of support calculation in sequential pattern mining, and the special characteristics of the stock sequence database.

Based on these observations, we propose a new approach. There is a method which was proposed to deal with high-dimensional database for mining frequent closed itemsets [9,12]. This method makes use of the characteristics of the high dimension and a small number of tuples in the database, and transposes the original data set. For the transposed database, the original row ID becomes the item, and the original item becomes the row ID. By this way, the search space is reduced dramatically, leading to an improved performance of this kind of algorithm. However, mining sequential patterns are more complex than mining frequent itemsets; thus, applying this method to sequential pattern mining is a big challenge. To check if this method can solve the ef<sup>fi</sup>ciency problem, we develop an algorithm, the Top-Down mining of Sequential patterns (TD-Seq), to deal with sequence databases whose sequences consist of three elements (or transactions). An experimental study conducted on actual stock market data shows that this algorithm can effectively solve the ef<sup>fi</sup>ciency problem.

The major points of this algorithm are as follows:

1) The original sequence database is transposed and the transformed database is mined. Mining the transformed database can reduce searching space.

2) A method called first element-based support counting method is proposed to solve the repeated counting and inequality of counting problems.

3) The mining process is divided into two phases: <sup>fi</sup>nding frequent closed itemsets, and <sup>fi</sup>nding frequent closed sequential patterns. Through this, a top-down search of rowset space can be effectively applied [9] to mine frequent closed sequences from a highdimensional sequence database.

4) Three pruning rules are developed to reduce the search space during the second mining phase. The algorithm is implemented, and experimental results show that this method is very ef<sup>fi</sup>cient.

Finally, the existing frequent closed sequence mining algorithm CloSpan [19] (MCloSpan) is modi<sup>fi</sup>ed to deal with sequence databases containing sequences with any number of elements. Results show that MCloSpan substantially outperforms CloSpan in mining high-dimensional databases.

The rest of the paper is organized as follows. In Section 2, the mining task of the frequent closed sequence is described. The motivation cited in Section 1 is explained in detail. The new algorithm is presented in Section 3, 4 and experimental results are discussed in Section 5. Related work is described in Section 6, and <sup>fi</sup>nally, conclusions are presented in Section 7.

## 2. Problem statemen

Let $I = \{ i _ { 1 } , i _ { 2 } , . . . , i _ { n } \}$ be a set of distinct items. An itemset s is a set of items, $S j \subseteq I . \mathsf { A }$ sequence s is an ordered list of itemsets denoted by $s { = } { < } s _ { 1 } , s _ { 2 } , { \ldots } , s _ { 1 } { > }$ , where s<sub>j</sub> is an itemset, also called an element of the sequence, denoted as $\left( x _ { 1 } , x _ { 2 } , . . . , x _ { m } \right)$ , where x is an item. Without loss of generality, items of an element are assumed to be sorted in a certain order such as a numerical arrangement or a lexicographic order. An item can only appear once in an element of a sequence, but can appear multiple times in the sequence. The sequence with a total of k items is referred to as a k-length sequence or k-sequence, and each occurrence of the items in the sequence is counted. A sequence $a = < a _ { 1 } , a _ { 2 } ,$ $a _ { p } >$ is contained in another sequence $b { = } { < } b _ { 1 } , b _ { 2 } { , } { \ldots } , b _ { q } { > } { \mathrm { i f } } p$ integers $\dot { l _ { 1 } } { < } l _ { 2 } { < } . . . < l _ { p }$ exist, so that $a _ { 1 } \subseteq b _ { l _ { 1 } } , a _ { 2 } \subseteq b _ { l _ { 2 } } , . . . , a _ { p } \subseteq b _ { l _ { p } } .$ Thus, sequence b contains a, and b is a super sequence of a.

A sequence database SD contains a set of data-sequences, each of which is a sequence with a unique sequence ID SID.

De<sup>fi</sup>nition 1. (Support) The support of a sequence s, denoted as sup(s), is the number of data-sequences in SD, each of which contains this sequence.

De<sup>fi</sup>nition 2. (Frequent sequence) Given a user-speci<sup>fi</sup>ed minimum support threshold minsup, a sequence whose support is equal to or greater than minsup is called a frequent sequence, or we say this sequence is frequent.

De<sup>fi</sup>nition 3. (Closed sequence) For a frequent sequence s, if no other sequence contains s and has the same support as s, s is called a closed sequence.

The problem of closed sequential pattern mining is <sup>fi</sup>nding the complete set of closed sequences given a user-speci<sup>fi</sup>ed minimum support threshold minsup.

The above concepts and de<sup>fi</sup>nitions are de<sup>fi</sup>ned based on the terminology presented in reference [19].

Example 1. Stock market exchange data are taken as an example. Suppose that we have a transaction database DB for the price change trends of three companies in 6 weeks (Table 1). For simplicity, the trend of each company for each week is represented by a number, which is a unique combination of the company id and its trend, which can be up, stable, or down. Numbers 1, 4, and 7 denote up, stable, and down, respectively for Company 1 during the corresponding week; 2, 5, and 8 for Company 2; and 3, 6, and 9 for Company 3. The trends for the three companies during the <sup>fi</sup>rst week as shown in Table 1 is (135), indicating that Company 1 is up this week compared with last week, Company 2 is stable, and Company 3 is up. In the experiments for actual stock market data, the combination of company id and the trend such as 6,000,001 up is used, where 6,000,001 is a company id, and up means its price increased during the corresponding week. In Table 1, the number of items in each transaction is the same although it could also differ. Each transaction in the transaction database has a unique identi<sup>fi</sup>er, called RID.

Table 1  
6-week stock exchange database for 3 companies.

<table><tr><td>RID</td><td>Itemset</td></tr><tr><td>1</td><td>1 3 5</td></tr><tr><td>2</td><td>4 5 6</td></tr><tr><td>3</td><td>1 2 3</td></tr><tr><td>4</td><td>1 2 3</td></tr><tr><td>5</td><td>1 5 6</td></tr><tr><td>6</td><td>1 3 5</td></tr></table>

Taking a sliding window of size 3 over this time-series data, a stock sequence database SD can be obtained (Table 2).

In Table 2, EID refers to the element ID. For the <sup>fi</sup>rst sequence, b(135) (456) (123)N, the SID is 1, and itemset (135) is the <sup>fi</sup>rst element, (456) the second, and (123) the third. For the <sup>fi</sup>rst element of the sequence, there are three items, 1, 3, and 5. This is a 9-length sequence as it has 9 items in total. Sequences b(123) 1N and b(123) (13)N both have 3 as support, and are both frequent if minsup=3. However, sequence b(123) 1N is not closed because it is contained in sequence b(123)(13)N and has the same support as b(123)(13)N.

The depth of SD, |SD|, is measured by the number of datasequences it contains. Here, |SD|=6. The width of SD, measured by the maximum length of data-sequences, is 9. If |SD| is big, for example, hundreds of thousands of data-sequences, the database is deep. If it is less than a hundred, it is shallow. If the width is less than a hundred, the database is narrow. Otherwise, it is wide. In this paper, we call shallow and wide sequence database high-dimensional sequence database. This paper aims to develop an algorithm that can ef<sup>fi</sup>ciently deal with high-dimensional sequence databases.

With this example, the ef<sup>fi</sup>ciency problem mentioned in Section 1 will be explained in detail in the following subsections.

The stock sequence database is shallow but wide (Table 2). Let us take 200 companies as an example. Each company has 3 trends (up, stable, and down), in which the width of the database is greater than 100. Suppose the average number of items occurring in the datasequences is m, then there are potentially $O ( m ^ { k } )$ frequent ksequences. Existing algorithms perform well when m is small because they usually enumerate all the item combinations. However, when m becomes large, the search space becomes huge. Therefore, traditional algorithms do not perform well for a shallow but wide sequence database. This problem is called low ef<sup>fi</sup>ciency. Two other factors that cause this problem are the repeated counting and inequality of counting of support value, which increase the number of frequent sequences.

In the sequence database in Table 2, sup(b(135)N)= 4, sup $( < ( 4 5 6 ) > ) = 2 , \ : \mathrm { s u p } ( < ( 1 2 3 ) > ) = 4 ,$ and sup(b(156)N)=3. Comparing

Table 2 Example of sequence database SD

<table><tr><td rowspan="2">SID</td><td colspan="3">Data-sequence</td></tr><tr><td>EID = 1</td><td>EID = 2</td><td>EID = 3</td></tr><tr><td>1</td><td>(135)</td><td>(456)</td><td>(123)</td></tr><tr><td>2</td><td>(456)</td><td>(123)</td><td>(123)</td></tr><tr><td>3</td><td>(123)</td><td>(123)</td><td>(156)</td></tr><tr><td>4</td><td>(123)</td><td>(156)</td><td>(135)</td></tr><tr><td>5</td><td>(156)</td><td>(135)</td><td></td></tr><tr><td>6</td><td>(135)</td><td></td><td></td></tr></table>

Table 4

these support values with the times they appear in the original transaction database in Table 1: (135):2, (456):1, (123):2, (156):1, it is easy to see that all of the supports are overestimated. The multiple appearance of one element in different sliding windows accounts for this occurrence; thus, the manifestations are counted repeatedly. This phenomenon is called repeated counting. If every element or sequence is counted equally during sequential pattern mining, then repeated counting is not a problem. However, this is not true. Both (456) and (156) appear once in Table 1, but their supports are 2 and 3, respectively in Table 2. This phenomenon is called inequality of counting. If minsup is set as 3, then b(456)N is not frequent, while b(156)N is frequent, which is clearly an unreasonable result. The same problem can also happen for sequences with more than one element. For example, sequences b(123)(13)N and b(123)1(15)N both appear twice in the original transaction database in Table 1, but they have supports 3 and 2, respectively in the sequence database in Table 2. As a result, using traditional sequential pattern mining algorithms can produce more sequences, which leads to long running times. If threshold minsup is 3, the complete set of closed sequences found by using traditional sequential pattern mining algorithms is listed in Table 3, in which sequences from 11 to 17 are, in fact, not frequent. Sequence b(156)N occurs only once and the other six sequences occur only twice in the original stream shown in Table 1.

## 3. New approach

To ef<sup>fi</sup>ciently perform the sequential pattern mining task for the stock sequence database, a new algorithm, TD-Seq, is proposed. In this algorithm, two new methods are developed, the first element-based support counting method, and the two phase-based mining method. These are described in the following subsections.

## 3.1. First element-based support counting method

To avoid repeated counting and inequality of counting, the <sup>fi</sup>rst element-based support counting method is proposed. The support calculated by this method is called discounted support, which is de<sup>fi</sup>ned as follows:

De<sup>fi</sup>nition 4. (Discounted support) For a sequence $s { = } { < } s _ { 1 } , s _ { 2 } , { \ldots } , s _ { l } { > } ,$ where s is an itemset, its discounted support, denoted as dSup(s), is the number of data-sequences in SD that contains this sequence, and the <sup>fi</sup>rst element of each of these data-sequences contains s . This support counting method is called the first element-based support counting method. A sequence is frequent if its discounted support is greater than or equal to minsup. A sequence s is closed if there is no sequence ${ s } ^ { \prime } { = } { < } s _ { 1 } { ' } , s _ { 2 } { ' } , . . . , s _ { m } { ' } { > } ,$ so that it has the same discounted support as s, and l integers $1 = j _ { 1 } < j _ { 2 } < . . . < j _ { l } \leq m$ exist, so that $S _ { 1 } \subseteq { S _ { j _ { 1 } } } , { S _ { 2 } \subseteq S _ { j _ { 2 } } }$ $s _ { l } \subseteq s _ { j _ { l } } )$

Table 3  
Set of closed sequences based on traditional frequency counting method.

<table><tr><td>No.</td><td>Closed sequence</td><td>Support</td><td>No.</td><td>Closed sequence</td><td>Support</td></tr><tr><td>1</td><td>&lt;5&gt;</td><td>6</td><td>11</td><td>&lt;(123)&gt;</td><td>4</td></tr><tr><td>2</td><td>&lt;13&gt;</td><td>5</td><td>12</td><td>&lt;(135)&gt;</td><td>4</td></tr><tr><td>3</td><td>&lt;(13)&gt;</td><td>6</td><td>13</td><td>&lt;(156)&gt;</td><td>3</td></tr><tr><td>4</td><td>&lt;15&gt;</td><td>4</td><td>14</td><td>&lt;(123)(13)&gt;</td><td>3</td></tr><tr><td>5</td><td>&lt;(15)&gt;</td><td>5</td><td>15</td><td>&lt;(13)(123)&gt;</td><td>3</td></tr><tr><td>6</td><td>&lt;(56)&gt;</td><td>5</td><td>16</td><td>&lt;(56)(13)&gt;</td><td>4</td></tr><tr><td>7</td><td>&lt;1(15)&gt;</td><td>3</td><td>17</td><td>&lt;(15)5&gt;</td><td>3</td></tr><tr><td>8</td><td>&lt;1(13)&gt;</td><td>5</td><td></td><td></td><td></td></tr><tr><td>9</td><td>&lt;(13)(13)&gt;</td><td>3</td><td></td><td></td><td></td></tr><tr><td>10</td><td>&lt;(13)(56)&gt;</td><td>3</td><td></td><td></td><td></td></tr></table>

Based on De<sup>fi</sup>nition 4, given a user-speci<sup>fi</sup>ed minimum support threshold minsup, a sequence is called a frequent sequence if and only if its discounted support is greater than minsup.

Example 2. According to De<sup>fi</sup>nition 4, and taking the database SD (Table 2) as an example, $d S u p ( < ( 1 3 5 ) > ) = 2 , d S u p ( < ( 4 5 6 ) > ) = 1$ , dSup $( < ( 1 2 3 ) > ) = 2 , \ d S u p ( < ( 1 5 6 ) > ) = 1 , \ d S u p < ( 1 2 3 ) ( 1 3 ) > = 2 .$ , dSup $( < ( 1 2 3 ) ( 1 5 6 ) > ) = 2$ , and $d S u p ( < ( 1 2 3 ) ( 1 ) ( 1 5 ) > ) = 2 .$ . If minsup is set to 3, the complete set of closed sequences is shown in Table 4. This set of closed sequences covers 10 of the 17 sequences (numbers 1 to 10, Table 3) found by using traditional frequency counting method in terms of frequent sequences. The set also excludes the output (caused by repeated counting) of the seven other sequences (numbers 11 to 17, Table 3). Due to repeated counting, some sequences that are not closed become closed, and closed sequences become not closed using the traditional frequency counting method. If all of the frequent sequences are derived from the output of the set of closed sequences using our method, we <sup>fi</sup>nd that the set of frequent sequences cover all of the frequent sequences derived from the output of the really closed sequences, which was obtained by using the traditional method.

## 3.2. Two phase-based mining method

De<sup>fi</sup>nition 5. (rowset and restRowset) Given a sequence database SD and its transaction database DB, the rowset of an itemset $S _ { i }$ denoted as rowset(s ), is a set of RIDs in DB, each of which contains the itemset s . Its restRowset, denoted as restRowset(s ), is a set of SIDs in SD, in which the elements with an EID greater than 1 contains the itemset $s _ { i \cdot }$ The size of an itemset's rowset or restRowset, denoted as |rowset(s )| and |restRowset(s )|, respectively, is the number of RIDs or SIDs in the set. The support of itemset $s _ { i } ,$ denoted as sup(s ), is |rowset(s )|. The Maximum support of itemset $s _ { i \bullet }$ denoted as mSup(s<sub>i</sub>), is de<sup>fi</sup>ned by the following formula (1):

$$
m S u p (s _ {i}) = \max \left(\left| r o w s e t (s _ {i}) \right|, \left| r e s t R o w s e t (s _ {i}) \right|\right)\tag{1}
$$

We take the size of restRowset into consideration when computing the support of an itemset $s _ { i }$ because this itemset may not occur frequently in the <sup>fi</sup>rst elements of SD, but it may be frequent in the second or third elements. Therefore itemset s may become an element of a frequent closed sequence. We de<sup>fi</sup>ne mSup(s<sub>i</sub>) as the bigger support between |restRowset(s )| and |rowset(s )| because |restRowset(s )| could be smaller than |rowset(s )| in some cases. Example 3 explains this occurrence.

De<sup>fi</sup>nition 6. (Candidate frequent closed itemset) Itemset $s _ { i }$ is a candidate frequent itemset in the transactional database DB if its maximum support is greater than or equal to the user-speci<sup>fi</sup>ed minimum support threshold minsup. Itemset s is considered closed if no itemset $s _ { j }$ that is a super set of $s _ { i }$ and have the same support as $s _ { i }$ exists. If a candidate frequent itemset is closed, it is called candidate frequent closed itemset.

Set of closed sequences based on first element-based support counting method

<table><tr><td>No.</td><td>Closed sequence</td><td>Support</td></tr><tr><td>1</td><td>&lt;1&gt;</td><td>5</td></tr><tr><td>2</td><td>&lt;15&gt;</td><td>4</td></tr><tr><td>3</td><td>&lt;1(15)&gt;</td><td>3</td></tr><tr><td>4</td><td>&lt;1(13)&gt;</td><td>4</td></tr><tr><td>5</td><td>&lt;5(13)&gt;</td><td>3</td></tr><tr><td>6</td><td>&lt;(13)(13)&gt;</td><td>3</td></tr><tr><td>7</td><td>&lt;(13)(56)&gt;</td><td>3</td></tr></table>

Example 3. Take the sequence database SD in Table 2 and its transaction database DB in Table 1 as examples: rowset[(456)]= {2}, restRowset[(456)] = {1}, mSup[(456)] = 1; rowset[(13)] = {1,3,4,6}, restRowset[(13)] = {1,2,3,4,5}, mSup[(13)] = 5; rowset[(156)] = {6}, restRowset[(156)] = {4,5} and mSup[(156)] = 2. Given that minsup=2, itemset (456) is not a candidate frequent itemset, while (156) and (13) are both candidate frequent itemsets, although (156) is not frequent in the transaction database DB. If the <sup>fi</sup>rst transaction is changed to (456), then rowset[(456)]= {1, 2}, restRowset[(456)]= {1}, and mSup[(456)] =2. Here, |restRowset[(456)]| is smaller than |rowset[(456)]|.

Example 3 shows that the restRowset of an itemset can be directly obtained based on its rowset as shown in Formula (2).

$$
\operatorname{restRowset} \left(s _ {i}\right) = \left\{r _ {i} \mid t _ {i} \in \operatorname{rowset} \left(s _ {i}\right) \text { and } r _ {i} = t _ {i} - 1 \operatorname{orr} _ {i} = t _ {i} - 2 \text { and } r _ {i} \geq 1 \right\}\tag{2}
$$

Based on this formula, the restRowset of an itemset can also be called the restRowset of the itemset's rowset t. That is, Formula (2) can also be written as Formula (3).

$$
\operatorname{restRowset} (t) = \left\{r _ {i} \mid t _ {i} \in t \text {   and   } r _ {i} = t _ {i} - 1 \text {   or   } r _ {i} = t _ {i} - 2 \text {   and   } r _ {i} \geq 1 \right\}\tag{3}
$$

Lemma 1. For a frequent closed sequence $s { = } { < } s _ { 1 } , \ s _ { 2 } , \ . . . ,$ s Nof sequence database SD, each element s must be a candidate frequent closed itemset of the transaction database DB.

Proof. According to De<sup>fi</sup>nition 6, if one element s of s is not closed in database DB, a super set s of $s _ { i } ( s _ { i } \subseteq s _ { j ) }$ , which has the same support as $s _ { i } ,$ must exist. That is, each transaction which contains s also contains $s _ { j } .$ Each transaction of DB is an element of a sequence in SD; therefore, in sequence database SD, each element $t _ { i }$ containing itemset s also contains $s _ { j \cdot }$ Substituting s by $s _ { j } ,$ a super sequence $s ^ { \prime } { = } { < } s _ { 1 } , s _ { 2 } , { \ldots } , s _ { j } ,$ s Nof s is obtained. Each data-sequence containing s also contains $s ^ { \prime } .$ Thus, sup(s) ≤ sup(s′). s′ is a super sequence of s, that is, sup(s′) ≤ sup (s); therefore, sup(s) = sup(s′). This means that s is not closed in SD, which is contradictory to the precondition.

If the <sup>fi</sup>rst element $s _ { 1 }$ is not a candidate frequent itemset in DB, then the number of transactions containing $s _ { 1 }$ is less than minsup, indicating that the number of <sup>fi</sup>rst elements in SD containing $s _ { 1 }$ is less than minsup. According to the <sup>fi</sup>rst element-based support counting method, support of s is less than mSup(s ). Therefore, s cannot be frequent.

If element $s _ { i }$ (with EIDN1) of the sequence s is not a candidate frequent itemset in database DB, according to De<sup>fi</sup>nition 5, |restRowset (s )|bminsup. Thus, the number of data-sequences whose elements with EIDN1 containing s is less than minsup. Therefore, the number of data-sequences containing the whole sequence s cannot be greater than or equal to minsup.

Based on Lemma 1, a two-phase mining process is developed as follows.

Phase 1. All of the candidate frequent closed itemsets are mined from the transactional database DB.

Phase 2. All of the frequent closed sequences based on the candidate frequent closed itemsets found in the <sup>fi</sup>rst phase are obtained.

## 4. Algorithm TD-Seq

In this section, the novel algorithm, TD-Seq, is described to integrate the two methods introduced in the last subsections. It is designed for mining the sequential patterns from the stock sequence database with a size 3 sliding window. Mining sequential patterns is much easier with a size 2 window than a size 3 because sequential patterns can be obtained by simplifying TD-Seq. For a window size bigger than 3, the existing sequential pattern mining algorithm, CloSpan, is modi<sup>fi</sup>ed to use the same support counting method.

![](/api/attachments/5VBE7BZW/fulltext/images/f3d44b4106301bf9f4d87fe656457cd77caf8f9112ff5a7da83388090bdb4367.jpg)  
Fig. 1. Top-down RID enumeration tree.

The major steps of TD-Seq are discussed in Section 4.2.

## 4.1. Phase 1: frequent closed itemset mining

In the <sup>fi</sup>rst phase of the algorithm (<sup>fi</sup>rst step of algorithm TD-Seq), TD-Close [9] (with modi<sup>fi</sup>cations as shown in Fig. 1) is called upon to mine a set FCP of candidate frequent closed itemsets from DB. This is performed by mining the transformed database of DB as shown in Table 5.

This transformed database is termed transposed database of DB (or transposed table). In this table, each item i corresponds to one tuple of the table, consisting of a set of RIDs and the rowset o $\because _ { i _ { j } . }$ . Note that term “transposed” is not equivalent to the transposition in matrix operation, although they are similar to some extent.

With the transposed database, the mining of a set of candidate frequent closed itemsets becomes a large closed rowset mining. Here, a large rowset means that its size is larger than minsup, or the size of its restRowset is larger than minsup. The transposed table can be pruned before the actual mining process. Items with a rowset and restRowset smaller than minsup can be deleted from the transposed database.

In Table 7, item 4 with rowset {2} and restRowset {1} will be deleted as the size of both its rowset and restRowset is 1, which is smaller than minsup 2.

Large closed rowset mining can be performed by a top–down RID enumeration style (searching from large rowsets to small rowsets). For a set of RID {1, 2, 3, 4, and 5}, the enumeration tree is illustrated in Fig. 1.

The algorithm TD-Close [9] is proposed to mine a complete set of frequent closed itemsets from high-dimensional data sets. The major steps are given in the following algorithm (refer to [9] for a detailed explanation of these steps). The modi<sup>fi</sup>cations made, which are underlined, are explained in this study.

Transposed database of DB.

<table><tr><td>Item</td><td>Rowset</td></tr><tr><td>1</td><td>1 3 4 5 6</td></tr><tr><td>2</td><td>3 4</td></tr><tr><td>3</td><td>1 3 4 6</td></tr><tr><td>4</td><td>2</td></tr><tr><td>5</td><td>1 2 5 6</td></tr><tr><td>6</td><td>2 5</td></tr></table>

<table><tr><td colspan="2">Transposed Table</td><td rowspan="10"></td><td colspan="2">Table 7  $TT_{EID=2}$ </td><td rowspan="10"></td><td rowspan="10"></td><td colspan="2">Table 9  $TT_{EID=2\ or\ 3}$ </td></tr><tr><td>item</td><td>rowset</td><td>itemsets</td><td>rowset</td><td>itemsets</td><td>rowset</td></tr><tr><td>1</td><td>1 3 4 5 6</td><td>(1 2 3)</td><td>2 3</td><td>(1 2 3)</td><td>1 2 3</td></tr><tr><td>2</td><td>3 4</td><td>(1 5 6)</td><td>4</td><td>(1 5 6)</td><td>3 4</td></tr><tr><td>3</td><td>1 3 4 6</td><td>(5 6)</td><td>1 4</td><td>(5 6)</td><td>1 3 4</td></tr><tr><td>5</td><td>1 2 5 6</td><td>(1 3 5)</td><td>5</td><td>(1 3 5)</td><td>4 5</td></tr><tr><td>6</td><td>2 5</td><td>(1 3)</td><td>2 3 5</td><td>(1 3)</td><td>1 2 3 4 5</td></tr><tr><td></td><td></td><td>(5)</td><td>1 4 5</td><td>(5)</td><td>1 3 4 5</td></tr><tr><td></td><td></td><td>(1 5)</td><td>4 5</td><td>(1 5)</td><td>3 4 5</td></tr><tr><td></td><td></td><td>(1)</td><td>2 3 4 5</td><td>(1)</td><td>1 2 3 4 5</td></tr><tr><td colspan="5">1) <img src="/api/attachments/5VBE7BZW/fulltext/images/e8b21f4a46c65a467f376f3a5ba6c810be7007c3421348cc09658fd2a6551a2d.jpg"/></td><td colspan="4"><img src="/api/attachments/5VBE7BZW/fulltext/images/1a39e95f3dc2604f7e7c487a5b4b10de50ee303458526b5b0b7cedf31542fa85.jpg"/></td></tr><tr><td colspan="2">Table 6  $TT_{EID=1}$ </td><td rowspan="10">(ZWDK)</td><td colspan="2">Table 8  $TT_{EID=3}$ </td><td rowspan="10" colspan="4"><img src="/api/attachments/5VBE7BZW/fulltext/images/1c82e9413e8f26526d73bd51dab5f53be8ff99a6c0e3f0522c15f93ade7981db.jpg"/></td></tr><tr><td>itemsets</td><td>rowset</td><td>itemsets</td><td>rowset</td></tr><tr><td>(1 2 3)</td><td>3 4</td><td>(1 2 3)</td><td>1 2</td></tr><tr><td>(1 5 6)</td><td>5</td><td>(1 5 6)</td><td>3</td></tr><tr><td>(5 6)</td><td>2 5</td><td>(5 6)</td><td>3</td></tr><tr><td>(1 3 5)</td><td>1 6</td><td>(1 3 5)</td><td>4</td></tr><tr><td>(1 3)</td><td>1 3 4 6</td><td>(1 3)</td><td>1 2 4</td></tr><tr><td>(5)</td><td>1 2 5 6</td><td>(5)</td><td>3 4</td></tr><tr><td>(1 5)</td><td>1 5 6</td><td>(1 5)</td><td>3 4</td></tr><tr><td>(1)</td><td>1 3 4 5 6</td><td>(1)</td><td>1 2 3 4</td></tr></table>

Notes: 1) call TD-Close to find a set of frequent closed itemsets.  
2) rowset(s<sub>i</sub>) in $T T _ { E I D = 2 } { = } \{ ( t _ { i } { - } 1 ) \mid t _ { i } { \in } \mathrm { r o w s e t } ( s _ { i } )$ in $T T _ { E I D = \bar { I } }$ <sub>1</sub> and $t _ { i } > 1 \}$  
3) rowset(s<sub>i</sub>) in $T T _ { E I D = 3 } { = } \{ ( t _ { i } { - } 2 ) \mid t _ { i }$ rowset(s<sub>i</sub>) in $T T _ { E I D = \bar { I } }$ <sub>1</sub> and $t _ { i } > 1 \}$  
4) rowset(s<sub>i</sub>) in TT<sub>EID=2</sub> <sub>or</sub> <sub>3</sub>=rowset(s<sub>i</sub>) in $T T _ { E I D = 2 } \cup$ rowset(s ) in $T T _ { E I D = 3 } ;$ (156): deleted from corresponding table according to pruning rule 2. 6: deleted according to pruning rule 1.

Fig. 2. Example of a phase in TD\_Seq.

## Algorithm TD-Close

Input: database DB, and minimum support threshold, minsup Output: A complete set of frequent closed patterns, FCP Method:

1.Transform DB into transposed table $\begin{array} { r } { T T | _ { \phi } . } \end{array}$

2. Initialize $F C P { = } \Phi .$

3. Call Top–Down Mine $( T T | _ { \phi } ,$ minsup).

Subroutine Top–Down Mine $( T T | _ { x } ,$ cMinsup)

Method:

1. Pruning 1:

If (|x| ≥(|DB|–minsup and restRowset({1…|DB|}−x)≤minsup), return.

2. Pruning 2: If the size o $\mathrm { \Delta ~ } \cdot \mathrm { \Delta } T | _ { x } \mathrm { i } s 1$ , generate the corresponding item set if the rowset is closed, and then return.

3. Pruning 3: Derive ${ \cal { T } } { \cal { I } } _ { \ l { x } \cup \ l { y } }$ and $T { \cal I } | _ { x } \mathrm { ; }$ where y is the largest RID among RIDs in tuples of $T \Pi _ { x } ,$ $T T | _ { x } { \mathrm { ' } } { = } \{ { \mathrm { t u p l e } } t _ { i } | t _ { i } \in \mathbb { T } [ | _ { \mathrm { x } }$ and $t _ { i }$ contains y}, TT|<sub>x y</sub> = {tuple $t _ { i } \mid t _ { i } \in \boldsymbol { \Pi } | _ { \mathbf { x } } ,$ , and if t contains y, size of t must be greater than cMinsup or restRowset(t 's rowset−{y})≥minsup} Delete y from both $\mathrm { \Delta T I _ { x \cup y } }$ and $\mathrm { T I } | _ { \mathbf { x } } \mathbf { \cdot }$

4. Output: Add to the FCI itemset corresponding to each rowset in $\boldsymbol { T } \boldsymbol { I } _ { \boldsymbol { x } \cup \boldsymbol { y } }$ with the largest size k and ending with RID k.

5. Recursive call:

Top–Down Mine $( \Pi \vert _ { \mathbf { x } \cup \mathbf { y } } ,$ cMinsup)

Top–Down Mine (TT| ', cMinsup–1)

The two modi<sup>fi</sup>cations are made to re<sup>fl</sup>ect the de<sup>fi</sup>nition of maximum support in De<sup>fi</sup>nition 5, which means that through this algorithm, all of the candidate frequent closed itemsets should be found instead of the frequent closed itemsets.

In the <sup>fi</sup>rst step of subroutine Top–Down Mine, one more condition is added to the recursive call termination conditions. When the excluded rowset x is so large that the remaining rowset cannot satisfy minsup, the restRowset of the remaining rowset may be large. Thus, the corresponding itemset may be frequent in the second or third column of the sequence database. This situation is considered by this new condition. The modi<sup>fi</sup>cation in Step 3 has the same meaning.

For the database shown in Table 5, all the candidate frequent closed itemsets are listed in the left column of Table 6 in Fig. 2, and their rowsets are in the right column. This transposed table is called $T T _ { E I D = 1 } \left( 0 \Gamma T T _ { E I D = 1 } | \phi \right)$ , containing all frequent itemsets that appear in the <sup>fi</sup>rst elements of the data-sequences of SD.

## 4.2. Phase 2: frequent closed sequence mining

Based on the $\boldsymbol { T } \boldsymbol { I } _ { E I D = 1 }$ obtained in the <sup>fi</sup>rst phase, an additional three transposed tables (Step 2 of algorithm TD-Seq shown below) can be constructed. These are illustrated in Tables 7, 8, and 9 in Fig. 2. Similar to $T T _ { E I D = 1 } , T T _ { E I D = 2 }$ contains itemsets appearing in the second elements of the data-sequences of SD, and $\boldsymbol { T } \boldsymbol { T } _ { E I D = 3 }$ contains itemsets appearing in the third elements. $T { T _ { E I D } } _ { \mathrm { { = } } 2 \ o r \ 3 }$ is the union of Tables 7 and 8 for each itemset, which contains itemsets appearing in the second or third elements.

Table $\boldsymbol { T } \boldsymbol { T } _ { E I D = 2 }$ can be derived in two steps. First, each itemset $s _ { i }$ is copied from $\boldsymbol { T } \boldsymbol { T } _ { E I D = 1 } .$ . Then, its rowset is obtained by deleting 1 from each RID $t _ { i } \left( t _ { i } > 1 \right)$ ) of the rowset of s in $\begin{array} { r } { T _ { E I D = 1 } , } \end{array}$ that is, rowset(s ) in $T T _ { E I D = 2 } = \{ ( t _ { i } - 1 ) \mid t _ { i } \in$ rowset(s ) in $\boldsymbol { T } \boldsymbol { I } _ { E I D = 1 }$ and $t _ { i } > 1 \}$ . Every itemset appearing in the <sup>fi</sup>rst element of the data-sequence $t _ { i } \ \left( t _ { i } > 1 \right)$ also appears in the data-sequence $( t _ { i } - 1 )$ , thus the deletion.

Similarly, Table $\boldsymbol { T } \boldsymbol { T } _ { E I D = 3 }$ can be constructed based on $\begin{array} { r } { T _ { E I D = 2 } . } \end{array}$

Based on the <sup>fi</sup>rst element-based support counting method, frequent closed sequences have these four types of forms:

1) 1-sequences from $\boldsymbol { T } \boldsymbol { I } _ { E I D = 1 }$

2) 2-sequences with elements from $\boldsymbol { T } \boldsymbol { I } _ { E I D = 1 }$ and $\boldsymbol { T } \boldsymbol { T } _ { E I D = 2 }$ which can be mined from Tables $\boldsymbol { T } \boldsymbol { I } _ { E I D = 1 }$ and $T \ T _ { E I D = 2 } \ \mathrm { o r } \ 3 \cdot$

3) 2-sequences with elements from $\boldsymbol { T } \boldsymbol { I } _ { E I D = 1 }$ and $T T _ { E I D = 3 } ,$ which can be mined from Tables $\boldsymbol { T } \boldsymbol { I } _ { E I D = 1 }$ and $T \ T _ { E I D = 2 } \ \mathrm { o r } \ 3 \cdot$

4) 3-sequences with elements from $T T _ { E I D = 1 } , T T _ { E I D = 2 } ,$ , and $\begin{array} { r } { T _ { E I D = 3 } , } \end{array}$ which can be mined from Tables $T T _ { E I D = 1 } , T T _ { E I D = 2 } ,$ , and $\begin{array} { r } { T _ { E I D = 3 } . } \end{array}$

Based on this observation, in the following mining steps, all the combinations of itemsets from these four tables are examined following a top-down search strategy as used in TD-Close. This is performed by a subroutine Top–Down Mine\_Seq in Step 4 of algorithm TD-Seq shown below. In this step, all of the sequences which are not closed will be marked “Not Closed.” Therefore, in Step 5 of TD-Seq, all itemsets in FCI not marked “Not Closed” with rowset sizes not less than minsup (only in this case, it is frequent in DB) will be inserted into FCS as single element sequences.

Algorithm TD-Seq (DB: transaction database; minsup: minimum support threshold; FCS: a set of frequent closed sequences)

1. Call TD-Close(DB, minsup) to mine a complete set FCI of frequent closed itemsets.

2. Based on FCI, generate four tables: $T T _ { E I D = 1 } , T T _ { E I D = 2 } , T T _ { E I D = 3 } ,$ and $T { \cal T } _ { E I D = 2 ~ 0 \Gamma 3 } ,$ which correspond to TT<sub>EID= 1</sub>|<sub>Φ</sub>, TT<sub>EID=2</sub>|<sub>Φ</sub>, TT<sub>EID=3</sub>|<sub>Φ</sub>, and $T { \cal T } _ { E I D = 2 \mathrm { ~ o r } }$ | , respectively.

3. Initialize $F C S = \Phi .$

4. Call Top–Down Mine\_Seq $( T T _ { E I D } = 1 \vert \Phi , \ T { \cal T } _ { E I D } = 2 \vert \Phi , \ T { \cal T } _ { E I D } = 3 \vert \Phi$ $T { \cal T } _ { E I D = 2 \mathrm { ~ o r } }$ <sub>3</sub>|<sub>Φ</sub>, minsup).

5. If the rowset size of each itemset s in Table $\boldsymbol { T } \boldsymbol { I } _ { E I D = 1 }$ not labeled as “Not Closed” is greater than or equal to minsup, the itemset will be added into FCS as a 1-sequence.

Subroutine Top–Down Mine\_Seq $( T T _ { E I D = 1 } | _ { \bf x } , \ T { T _ { E I D = 2 } } | _ { \bf x } , \ T { T _ { E I D = 3 } } | _ { \bf x } ,$ $T T _ { E I D = 2 \mathrm { ~ o r ~ } 3 } | _ { \bf x } , c M i n s u p )$

Method:

1. $\operatorname { I f } | x | > = ( | S D | - m i n s u p ) ,$ , return.

2. Let r =the largest RID among RIDs in tuples of $\begin{array} { r } { T _ { E I D = 1 } | _ { \mathbf { x } } , } \end{array}$ $r _ { 2 } =$ the largest RID among RIDs in tuples of $T T _ { E I D = 2 \mathrm { ~ o r ~ } 3 } | _ { \bf x } ,$ and $r { = } m i n ( r _ { 1 } , r _ { 2 } )$ . Then, do the following two kinds of pruning: Pruning rule 1: Delete all RIDs larger than r in tuples of the four tables, and put these RIDs in skipRowset and x as follows: $x = x \cup$ {r |r is an RID larger than r in any of the four tables}. Pruning rule 2: Delete each tuple whose rowset size is less than cMinsup.

if $\begin{array} { r } { T _ { E I D = 1 } | _ { x } } \end{array}$ is empty or $\boldsymbol { T } \boldsymbol { T } _ { E I D = 2 }$ <sub>or 3</sub>|<sub>x</sub> is empty, return.

3. If $r { < } r _ { 1 } ,$ call CheckSeq(TT<sub>EID = 1</sub>|<sub>x</sub>, TT<sub>EID = 2</sub>|<sub>x</sub>, TT<sub>EID = 3</sub>|<sub>x</sub>, $T T _ { E I D = 2 } ~ \mathrm { o r } ~ 3 | _ { x } , ~ r )$

4. For each of the four tables, derive $\left. T T \right| _ { x } ^ { \prime }$ and $T \Pi _ { x \cup r } .$

$T T | _ { \times } ^ { \prime } { = } \{ \mathrm { t u p l e } ~ t _ { i } ~ | ~ t _ { i } \in T T | _ { x }$ and t contains $r \} ,$ $T T | _ { \times \cup r } = \{ { \mathrm { t u p l e } } t _ { i } \ | t _ { i } \in T T | _ { x } ,$ and if $t _ { i }$ contains r, size of $t _ { i }$ must be greater than cMinsup} Then delete r from both $\left. T \right| _ { x \cup r }$ and $\left. T T \right| _ { x } ^ { \prime } ,$ and prune tuples of $\left. T I \right| _ { x \cup r }$ according to pruning rule 2.

5. Let $r ^ { \prime } =$ the largest RID among RIDs in tuples of $T _ { E I D = 1 } | _ { x \cup r }$ . Call $\begin{array} { r } { C h e c k S e q ( T T _ { E I D } = 1 \big | x \cup r ) T \hat { T } _ { E I D } = 2 \big | x \cup r \mathcal { T } _ { E I D } = 3 \big | x \cup r \mathcal { T } T _ { E I D } = 2 \ : \mathrm { o r } \ : 3 \big | x \cup r \mathcal { r } ^ { \prime } \big ) } \end{array}$

Top–Down Mine\_Seq $( T T _ { E I D } = 1 | _ { x } , \quad T T _ { E I D } = 2 | _ { x } , \quad T T _ { E I D } = 3 | _ { x } ,$ $T { \cal T } _ { E I D = 2 } \quad \mathrm { ~ o r ~ }$ <sub>3</sub>|<sub>x</sub>, r, cMinsup, excluedSize + 1),Top–Down Mine\_Seq $( T T _ { E I D } = 1 \big | _ { x } ^ { \prime } , \ T T _ { E I D = 2 } \big | _ { x } ^ { \prime } , \ T T _ { E I D = 3 } \big | _ { x } ^ { \prime } , \ T T _ { E I D = 2 \mathrm { ~ o r ~ } 3 } \big | _ { x } ^ { \prime } , \ T$ cMinsup-1, excluedSize).

Subroutine $C h e c k S e q \left( T T _ { E I D } = 1 | \boldsymbol { x } , T T _ { E I D } = 2 | \boldsymbol { x } , T T _ { E I D } = 3 | \boldsymbol { x } , T T _ { E I D } = 2 \mathrm { \ o r \ } 3 | \boldsymbol { x } , r \right)$

1. If TT | , TT | , and $\displaystyle T T _ { E I D = 3 } | _ { x }$ have tuples $t _ { 1 } , t _ { 2 } ,$ and $t _ { 3 } ,$ respectively, all with the largest size r and ending with RID r, the candidate sequence is the combination of the itemsets of the three tuples. If the sequence is closed, add to FCS, and then label the itemset $t _ { 1 }$ as “Not Closed” if its skipRowset is empty.

2. If $\boldsymbol { T } \boldsymbol { T } _ { E I D = 1 } | _ { x }$ has tuple $t _ { 1 } ,$ , with the largest size r and ending with RID r, then for each tuple $t _ { 4 }$ in ${ T T _ { E I D = 2 } } _ { 0 \Gamma } \ _ { 3 } | _ { x }$ with the largest size r and ending with $R I D ~ r ,$ the candidate sequence is the combination of the itemsets of tuples $t _ { 1 }$ and $t _ { 4 } .$ If the sequence is closed, add to FCS, and then label the itemset $t _ { 1 }$ $\mathsf { a s } \ " \mathrm { N o t }$ Closed” if its skipRowset is empty.

3. Return.

## 4.2.1. Subroutine Top–Down Mine\_Seq

The major subroutine Top–Down Mine\_Seq is explained through examples. The major steps are also exempli<sup>fi</sup>ed in Fig. 3.

Example 4. Taking transaction database DB in Table 1 as an example, when algorithm TD-Seq <sup>fi</sup>rst calls upon subroutine Top–Down $\mathrm { M i n e \ . } S e q ,$ the <sup>fi</sup>rst four parameters (the four tables), are represented as Tables $6 , 7 ,$ 8, and 9 in Fig. 2. In this situation, cMinsup=2 if $m i n s u p { = } 2 . \ x$ is an excluded rowset; thus, it is excluded from any of the four current transposed tables. Therefore, in the first step of this subroutine, if the size of x is greater than (|SD|-minsup), the size of any rowset in the transposed tables cannot satisfy minsup because the size of the biggest rowset is |SD|. Therefore, the recursive call can be terminated.

In this example, for the <sup>fi</sup>rst call of Top–Down Mine $\operatorname { \_ } S e q , x$ is an empty set; thus, its size is less than |SD|-minsup $= 6 - 2 = 4$ . The second step is then initiated.

In the second step, the largest RID in $T { \cal T } _ { E I D } = 1 \vert \Phi , r _ { 1 } ,$ is 6, and the largest RID in $T { \cal T } _ { E I D = 2 \mathrm { ~ o I ~ } }$ | $r _ { 2 , }$ is 5. Thus, $r = m i n ( 6 , 5 ) = 5$ . Then, two kinds of pruning can be performed.

Pruning rule 1: All RIDs larger than 5, (in this case, it is 6) are deleted from all of the four tables, which is Table $T { T _ { E I D } } = 1 \big | \mathrm { d p }$ as shown in Table 6. Excluded rowset x now has one element 6, that is, $x = \{ 6 \}$ The deleted RID is also added to the skipRowset of each itemset.

Each element (itemset) of the frequent closed sequence must appear in the same set of rows; thus, RIDs which are not shared by these itemsets can be deleted.

Pruning rule 2: Delete from each of the four tables the itemsets whose rowsets have less than minsup RIDs. For example, in Table 6, the second and the fourth tuple, (156) and (135), will be deleted because their rowsets have less than 2 RIDs.

Apparently, a sequence having this kind of itemsets as elements will not be frequent.

After pruning, the four tables become $T T _ { E I D } = 1 | _ { \{ 6 \} } , \ T T _ { E I D } = 2 | _ { \{ 6 \} } ,$ $T { \cal T } _ { E I D = 3 } | _ { \{ 6 \} } ,$ and $\boldsymbol { T } \boldsymbol { T } _ { E I D = 2 }$ | as shown in Tables $1 0 , 1 1 , 1 2 ,$ , and 13 in Fig. 3. In Table 10, RIDs in brackets are skipRowset, used to keep those RIDs skipped while forming the current rowset. It is likewise used to check if an itemset is closed. When a skipRowset of an itemset is not empty, the itemset is not closed. Theoretical proof is given in [9].

After pruning, $i f T _ { E I D = 1 } | _ { 6 }$ or $T T _ { E I D = 2 } \mathrm { { o r } \ 3 | 6 }$ is empty, recursive call will be terminated. In this study, neither of them is empty; thus, step 3 is initiated.

In Step 3, since $r { < } 6 ,$ subroutine CheckSeq $( T T _ { E I D } = 1 | _ { 6 }$ $T T _ { E I D } = 2 | _ { 6 } ,$ TT | , TT | , 5) is called to determine if any sequence currently exists. As in Table $T T _ { E I D } = 1 | _ { 6 } ,$ no tuple which have a size 5 rowset and ends with RID 5 exists, and no sequence is found. Then, we proceed to Step 4 of Top–Down Mine\_Seq. The major steps of CheckSeq are discussed in 4.2.2.

In Step 4, two kinds of transposed tables are generated.

Tables of the <sup>fi</sup>rst kind contain RID 5 in each tuple, exempli<sup>fi</sup>ed by Tables 14, 15, 16, and 17 in Fig. 3. To avoid repetition, RID 5 is deleted from these tables, but it is implicitly included in each tuple. Therefore, for these tables, the dynamic minsup threshold cMinsup decreases by 1, that is, cMinsup $ / = 2 - 1 = 1$

Tables of the second kind do not contain RID 5. For those tuples having RID 5, RID 5 is placed in their skipRowset as shown in

![](/api/attachments/5VBE7BZW/fulltext/images/34ec2d7300cea4c8433280d36b9ba10d0331edc6ebcbf88a33f0274013ad4dda.jpg)

Notes: 1) Step 2 of subroutine TopDownMine\_Seq;

2) Step 4 of subroutine TopDownMine\_Seq;

(56): deleted from corresponding table according to pruning rule 2.

Fig. 3. Example of the major steps of subroutine Top–Down Mine\_Seq.

Tables 18, 19, 20, and 21 in Fig. 3. Itemset (5 6) and (1 5) in Table TT | , and itemset (1 5) in $\boldsymbol { T } \boldsymbol { \mathbf { \Pi } } _ { E I D = 2 }$ | are removed from these two tables according to pruning rule 2.

In Step 5, r′, the biggest RID in Table TT | is 4. Thus, CheckSeq(TT | , TT | , TT | , TT | , 4) is called. The rowset {1, 2, 3, 4} does not exist in Table $T T _ { E I D = 1 } | _ { \{ 6 , 5 \} } ;$ thus, no sequence is found.

In Step 6, Top–Down Mine\_Seq is recursively called twice. The <sup>fi</sup>rst is for tables excluding RID 5 and the second is for tables implicitly containing RID 5. For the latter, as mentioned above, cMinsup becomes 1.

## 4.2.2. Subroutine CheckSeq

To show the function of the subroutine CheckSeq, suppose we are calling this function to deal with transposed tables which contain the rowset {3, 4} implicitly, and do not contain the rowset {6, 5, 2} as shown. in. Tables $\begin{array} { c c c } { { T T _ { E I D } = 1 | { } _ { \{ 6 , 5 , 2 \} } , } } & { { T T _ { E I D } = 2 | { } _ { \{ 6 , 5 , 2 \} } , } } & { { T T _ { E I D } = 3 | { } _ { \{ 6 , 5 , 2 \} } } } \end{array}$ , and $\boldsymbol { T } \boldsymbol { T } _ { E I D = 2 }$ | in Fig. 4. In this case, cMinsup= 0, r = 1.

In the first step of CheckSeq, 3-sequences are searched, which is performed by pruning and then checking if any 3-sequence exists. The itemset in each transposed table is removed according to the pruning rule 3, de<sup>fi</sup>ned as:

Pruning rule 3: For each itemset t having a rowset with size r and ending with r in each transposed table, if a super itemset of t with the same rowset exists, t is deleted from the transposed table.

This pruning can be performed because such itemset t is not closed. There exists a superset of t with the same support.

According to pruning rule 3, in table $T T _ { E I D = 1 } | _ { \{ 6 , 5 , 2 \} } ,$ itemset (1) is removed because itemset (1,3) is a superset of (1), and both have rowset {1}. Similarly, itemsets (5) and (1) are removed from $T T _ { E I D = 2 \mathrm { o r } 3 } | _ { \{ 6 , 5 , 2 \} } \mathrm { a } s$ shown in Table 25.

Then, three itemsets (t , t , and t ), should be found from Tables $T T _ { E I D } = 1 | { \{ 6 , 5 , 2 \} }$ , TT | , and $T T _ { E I D = 3 } | _ { \{ 6 , 5 , 2 \} } ,$ respectively, each of which must have a rowset with a size r (=1) and ending with r. In table $T T _ { E I D } = 2 | \{ 6 , 5 , 2 \}$ no such itemset was found. Thus, any 3-sequence could not be found either.

![](/api/attachments/5VBE7BZW/fulltext/images/8896819a01e238df5c2567c528d8ecfca44e6e9df92b6a42e31e2e34a46baa86.jpg)  
Notes: 1) Step 1 of subroutine CheckSeq;  
2) Step 2 of subroutine CheckSeq;  
(1): deleted from corresponding table according to Pruning rule 3.  
Fig. 4. Example of the major steps of subroutine checkSeq.

In the second step of CheckSeq, we aim to <sup>fi</sup>nd 2-sequences. Itemset $t _ { 1 } = ( 1 \ 3 )$ in TT<sub>EID = 1</sub>|<sub>{6,5,2}</sub> with a rowset {1} is found, as well as two itemsets $t _ { 4 1 } = ( 1 3 )$ and $t _ { 4 2 } = ( 5 6 )$ . As a result, two sequences, b(13) (13)N and b(13) (56)N, were identi<sup>fi</sup>ed.

For each sequence, two things should be checked. One is if the intersection of the skipRowset of the two itemsets is empty, and two, if a super sequence is found in Step 1 as discussed above.

For sequence b(13) (13)N with elements $t _ { 1 }$ and $t _ { 4 1 } ,$ the intersection of skipRowset is {6}∩{2 5} =Φ. No sequence is found in Step 1. Therefore, sequence b(13) (13)N is inserted into FCS. Similarly, sequence b(13) (56)N is added into FCS.

Finally, itemset $t _ { 1 }$ is checked if its skipRowset is empty. If it is empty, then it should be marked “Not Closed” because a 1-sequence is contained by the sequence just found. In this study, the skipRowset of itemset $t _ { 1 }$ is {6}; thus, it is not empty and does not require marking.

## 5. Experimental study

To evaluate the performance of the new algorithm, TD-Seq was implemented. The source code of CloSpan was downloaded from the website of project Illimine [15] for comparison. Another intended algorithm is BIDE [18], but it can only deal with sequences with single item elements. Therefore, it was not used for comparison. Actual stock market exchange data of 2007 from Tsinghua Financial Database was used [16]. Weekly price change trends were calculated to form stock sequence databases with a size 3 sliding window. All experiments were conducted on a PC with Intel Core 2 Duo CPU E7200 2.53 GHz, 3.25 GB RAM, and Windows XP system.

![](/api/attachments/5VBE7BZW/fulltext/images/37c49b86573c90c3ef5db41b9f0f8b307ff564beb7c18621ee056df805e82897.jpg)  
Fig. 5. Runtime changes as minsup decreases (700 companies).

To deal with the sequence database with a sliding window bigger than 3, CloSpan [19] was modi<sup>fi</sup>ed so that the new support counting method can be used. In this study, the modi<sup>fi</sup>ed version of CloSpan is called MCloSpan. The modi<sup>fi</sup>cation was made to re<sup>fl</sup>ect the <sup>fi</sup>rst element-based support counting method.

Several sets of experiments were conducted to evaluate the performance as four parameters change: minsup, number of distinct items, number of data-sequences in the sequence database, and size of sliding windows.

## 5.1. Performance vs. minsup

The <sup>fi</sup>rst set of experiments aims to test the performance of three algorithms as the threshold minsup decreases. The <sup>fi</sup>rst sequence database contains weekly trends of 700 companies for 20 weeks. Each company may have three different trends: up, stable, and down. The total number of distinct items is 1219. The total runtime is depicted in Fig. 5, and the number of closed sequential patterns is shown in Fig. 6. The latter shows that the vertical axis is in logarithmic scale. In Fig. 5, when the minsup is 15, no frequent closed sequential pattern is found by TD-Seq. In Fig. 5, TD-Seq substantially outperforms CloSpan. As minsup decreases, the runtime of CloSpan increases dramatically, and cannot run to end successfully when minsup is greater than 11. When minsup is less than 9, TD-Seq uses up less time than MCloSpan. When minsup is less than 13, TD-Seq substantially outperforms CloSpan because as minsup decreases, the number of frequent sequential patterns increases considerably, while the number of data-sequences (the number of rows in the database) remains unchanged. TD-Seq is a kind of row-enumeration-based algorithm. Thus, an increase in the number of frequent sequential patterns does not have a major effect on its performance. Fig. 6 shows that the number of closed sequential patterns generated by CloSpan is greater than that by TD-Seq. Many sequences obtained exaggerated frequencies by traditional frequency counting method used by CloSpan.

![](/api/attachments/5VBE7BZW/fulltext/images/482ce3b9474d022c7ecad3b9f2ed283ce009379b3fed6843339940298ef8e1da.jpg)  
Fig. 6. Number of closed sequences as minsup decreases (700 companies).

![](/api/attachments/5VBE7BZW/fulltext/images/ab0b1a9d364e7fcc12145173ecae890f368004d8a62cee4392d3185dc62f2c6c.jpg)  
Fig. 7. Runtime changes as minsup decreases (900 companies).

Experiments were likewise conducted on another database containing 20 weeks of weekly trends for 900 companies. The total number of distinct items is 1474. The total runtime is depicted in Fig. 7, and the number of closed sequential patterns found is shown in Fig. 8. The vertical axis of Fig. 8 is also in logarithmic scale. These two <sup>fi</sup>gures have the same patterns as Figs. 5 and 6.

## 5.2. Performance vs. number of distinct items

The second set of experiments used data sets with a different number of distinct items, but the number of sequences remains 20, and minsup=8. The results are shown in Figs. 9 and 10. They also indicate that TD-Seq uses up the least time among the three algorithms, and MCloSpan, the second least. CloSpan fails to successfully run to end when the number of distinct item exceeds 556. As the number of distinct items (companies) grows larger, that is, the data sets become wider, TD-Seq shows greater advantages compared with MCloSpan and Clospan.

![](/api/attachments/5VBE7BZW/fulltext/images/02f4e24a3fffad5a164e953cdf4123bc399c9469b803c2bccfa5d274bb7de91c.jpg)  
Fig. 8. Number of closed sequences as minsup decreases (900 companies).

![](/api/attachments/5VBE7BZW/fulltext/images/6be08a1e868d8985c964ac576a8724500f8f40766dce5e02ece05bfdc2ffe13f.jpg)  
Fig. 9. Runtime vs. number of distinct items.

## 5.3. Performance vs. number of data sequences

The third set of experiments was conducted to test the performance of the three algorithms as the depth of the sequence database and the number of data-sequence (rows) in the sequence database increased. To do this, <sup>fi</sup>ve data sets were generated, each of which has 1219 distinct items but different number of rows, ranging from 18 to 26. Threshold minsup was set to 40% of the number of total rows. The results are depicted in Figs. 11 and 12. The vertical axis of Fig. 8 is in logarithmic scale. CloSpan could not successfully run to end for these databases because of a huge number of closed sequences that were found. Therefore, the results are not displayed in this paper. The number of data-sequences increases, the runtime of TD-Seq rapidly increases, while MCloSpan performs better when the database becomes deeper. The performance of MCloSpan is more dependent on the number of different items, while the performance of TD-Seq depends on the number of rows. Therefore, TD-Seq runtime increases as the number of rows increases, while that of MCloSpan does not. In Fig. 12, the number of closed sequential patterns found does not differ signi<sup>fi</sup>cantly because the threshold minsup is <sup>fi</sup>xed at 40%.

## 5.4. Performance vs. size of sliding windows

The last set of experiments was conducted to test the performance change as the size of sliding window increases. The experiments were conducted on four data sets, each of which contains the trends of 200 companies but with different number of elements in each of the 20 rows. The numbers, ranging from 3 to 6, corresponded to four different sliding window sizes. Threshold minsup was set to 12, 60% of the number of total rows. The results are depicted in Figs. 13 and 14. In the two <sup>fi</sup>gures, the y-axes are both in logarithmic scale. CloSpan failed to run to end (error, “probably corrupted stack”) for the size 6 sliding window. In Fig. 13, as the size of sliding window increases, the runtime of CloSpan rapidly increases very fast, while MCloSpan runs much faster than CloSpan. This can be attributed to the faster increase in the number of closed sequences, as the traditional frequency counting method was used rather than the <sup>fi</sup>rst element-based frequency counting method. This is shown in Fig. 14.

![](/api/attachments/5VBE7BZW/fulltext/images/743d9081d1a0f06ff162062a2b85d02f0cac2b7991e745bed95b3dbd72f2e828.jpg)  
Fig. 10. Number of closed sequences vs. number of distinct items.

![](/api/attachments/5VBE7BZW/fulltext/images/52fad9e67a11a15b64674ed65494cdb60668acb6c0d9c228dc2fe709bf045207.jpg)  
Fig. 11. Runtime vs. number of data-sequences.

![](/api/attachments/5VBE7BZW/fulltext/images/799ae57e54c3585fa572d074a664860e05bbc7c9a4d5c12a79cc3fc14f2bb509.jpg)  
Fig. 12. Number of closed sequences vs. number of data-sequences.

## 6. Related Work

Previous research related to the present work includes sequential pattern mining, row-enumeration-based mining method, and frequent episode mining.

For sequential pattern mining, many algorithms [1–7] have been proposed to <sup>fi</sup>nd frequent sequential patterns from transaction databases. They are either horizontal-based algorithms such as [2] and [13], or vertical-based algorithms such as [20]. Both conduct a search of the sequence space. To reduce the number of frequent sequences found, methods for mining frequent closed sequences are proposed [18,19]. These performed well for transactional databases, that is, deep and narrow databases. In this paper, we focus on frequent closed sequences mining for databases, which are shallow but wide.

The row enumeration-based mining method has been proposed in recent years to deal with high-dimensional databases [9,12]. Another method is the column enumeration-based mining method. Most frequent itemset mining algorithms such as a priori [1] and FP-growth [6] belong to this category. During the mining process, the former searches for interesting patterns, such as frequent itemsets from the rowset (set of row ids) space, while the latter from the itemset (set of items) space. Hence, for the row-enumeration-based method, the original database is transposed for further mining. However, to the best of our knowledge, this method is only used to mine frequent closed itemsets and not for sequential pattern mining. The algorithm of the present study uses this method in mining sequential patterns.

![](/api/attachments/5VBE7BZW/fulltext/images/b85f7dd73ebed0a3567be947b82ba0b4bcea48524657af8fe52070d5f678524e.jpg)  
Fig. 13. Runtime vs. size of sliding windows.

![](/api/attachments/5VBE7BZW/fulltext/images/38c28de02799138129e7bb6c664730051b7a92707a1d2789b99a35c0362a9dc2.jpg)  
Fig. 14. Number of closed sequences vs. size of sliding windows.

Frequent episode mining is related to our work as it is also a kind of temporal pattern. Frequent episode was <sup>fi</sup>rst proposed by Mannila, Toivonen, and Verkamo in 1995. Since then, algorithms for mining different versions of episode de<sup>fi</sup>nition [8,10,11] have been proposed to mine frequent episodes from sequential data. In [10], the algorithms for <sup>fi</sup>nding sliding window-based serial episodes and parallel episodes were proposed. In this paper, a method called minimal occurrence is also proposed, which avoids counting an episode occurrence repeatedly. In 2003, a variant of episode de<sup>fi</sup>nition was given in [11], which is similar to the <sup>fi</sup>rst element-based support counting method of this study. However, as a frequent episode is different from a frequent sequence, it cannot be used directly for sequential pattern mining, especially in a high-dimensional context.

## 7. Conclusions

Sequential pattern mining task for stock sequence databases was studied. Using existing algorithms to perform the task suffers from low ef<sup>fi</sup>ciency. To address this problem, a new algorithm, TD-Seq, was proposed and an existing algorithm, CloSpan, was modi<sup>fi</sup>ed. Both have good performance as demonstrated by the experimental results. Although this mining task was studied using stock sequence database as an example, the algorithm can be used for other application areas, such as customer purchase behavior analysis and customer online browsing behavior analysis. In these applications, sequential patterns found could be used to predict future behavior. For example, from frequent closed stock exchange trend sequences, rules such as “Company 1 is up and company 2 is down last week; company 3 is likely to be up this week, and company 4 will be down next week,” can be generated. For sequence database consisting of long datasequences and small number of data-sequences, TD-Seq performs better than other algorithms. Both TD-Seq and MCloSpan can produce a relatively small number of sequential patterns, which can ease the burden of understanding the patterns.

TD-Seq is designed for sequence database generated by sliding a window with sizes less than 4 over transactional databases. It could be used in many real world applications as discussed above. However, when the sliding window size is over 3, MCloSpan can be used although it is not designed for high-dimensional databases. Therefore, future work should include two directions. One is to modify algorithms such as McloSpan to deal with high-dimensional databases using the row-enumeration approach, and two, extend TD-Seq to deal with sequence databases with more than three elements.

## Acknowledgements

This paper was supported in part by the National Natural Science Foundation of China under Grant No. 70871068 and 70890083.

## References

[1] R. Agrawal, R. Srikant, Fast algorithms for mining association rules, in: J.B. Bocca, M. Jarke, C. Zaniolo (Eds.), Proceedings of the 20th International Conference Ver Large Data Bases (VLDB), San Francisco, CA, USA, 1994, pp. 487–499.

[2] R. Agrawal, R. Srikant, Mining sequential patterns, Proceedings of the Eleventh International Conference on Data Engineering (ICDE), Taipei, Taiwan, 1995, pp. 3–14.

[3] J. Ayres, J. Gehrke, T. Yu, J. Flannick, Sequential pattern mining using a bitmap representation, Proceedings of the Eighth ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, Edmonton, Alberta, Canada, July 23-26, 2002, pp. 429–435.

[4] Y. Chen, Y. Hu, Constraint-based sequential pattern mining: the consideration of recency and compactness, Decision Support Systems 42 (2) (2006) 1203–1215.

[5] J. Feng, Q. Qian, J. Wang, L. Zhou, SOLARIA: a sequence based hot XML query pattern mining algorithm, Proceedings of the 2006 ACM Symposium on Applied Computing, Dijon, France, April 2006, pp. 517–524.

[6] J. Han, J. Pei, Mining frequent patterns by pattern growth: methodology and implications, SIGKDD Explorations 2 (2000) 14–20.

[7] K. Hatonen, M. Klemettinen, H. Mannila, P. Ronkainen, H. Toivonen, Knowledge discovery from telecommunication network alarm databases, Proceedings of the Twelfth IEEE International Conference on Data Engineering (ICDE), New Orleans, Louisiana, USA, February, 1996, pp. 115–122.

[8] Srivatsan Laxman, P.S. Sastry, K.P. Unnikrishnan, A fast algorthm for <sup>fi</sup>nding frequent episodes in event streams, Proceedings of the 13th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, San Jose, CA, USA, August 2007, pp. 410–419.

[9] H. Liu, J. Han, D. Xin, Z. Shao, Mining interesting patterns from very high dimensional data: a top–down row enumeration approach, Proceedings of the Sixth SIAM International Conference on Data Mining (SDM), Newport Beach, CA, USA, April 21-23 2006, pp. 280–292.

[10] H. Mannila, H. Toivonen, A.I. Verkamo, Discovery of frequent episodes in event sequences, Data Mining and Knowledge Discovery 1 (1997) 59–289.

[11] A. Ng, A.W. Fu, Mining frequent episodes for relating <sup>fi</sup>nancial events and stock trends Proceedings of the Seventh Pacific-Asia Conference on Knowledge Discovery and Data Mining (PAKDD) Seoul Korea 2003 Lecture Notes in Computer Science, vol. 2637, Springer, 2003, pp. 27–39.

[12] F. Pan, G. Cong, A.K.H. Tung, J. Yang, M.J. Zaki, CARPENTER: Finding closed patterns in long biological datasets Proceedings 2003 ACM SIGKDD Internationa Conference on Knowledge Discovery and Data Mining, 2003, pp. 637–642.

[13] J. Pei, J. Han, H. Pinto, Q. Chen, U. Dayal, M.-C. Hsu, Pre<sup>fi</sup>xSpan: mining sequential patterns ef<sup>fi</sup>ciently by pre<sup>fi</sup>x-projected pattern growth, Proceedings of the of the 17th IEEE International Conference on Data Engineering (ICDE), Herdelberg, Germany, April 2001, pp. 215–224.

[14] J. Pei, J. Han, W. Wang, Constraint-based sequential pattern mining in large databases, Proceedings of the 11th ACM International Conference on Information and Knowledge Management (CIKM), McLean, VA, Nov. 2002, pp. 18–25.

[15] The IlliMine project: http://illimine.cs.uiuc.edu/.

[16] Tsinghua University Financial Database: http://thfd.sem.tsinghua.edu.cn/.

[17] C. Tsai, Y. Shieh, A change detection method for sequential patterns, Decision Support Systems 46 (2) (2009) 501–511.

[18] J. Wang, J. Han, BIDE: ef<sup>fi</sup>cient mining of frequent closed sequences, Proceedings of the 20th IEEE International Conference on Data Engineering (ICDE), Boston, MA, USA, 2004, pp. 79–90.

[19] X. Yan, J. Han, R. Afshar, CloSpan: mining closed sequential patterns in large datasets, Proceedings of the Third SIAM International Conference on Data Mining (SDM), San Francisco, CA, May 1–3, 2003, pp. 166–177.

[20] M. Zaki, SPADE: an ef<sup>fi</sup>cient algorithm for mining frequent sequences, Machine Learning 40 (2001) 31–60.

[21] M.J. Zaki, N. Lesh, M. Ogihara, PlanMine: sequence mining for plan failures, Proceedings of the 4th International Conference on Knowledge Discovery and Data Mining (SIGKDD), 1998, pp. 369–374.

[22] Z. Zhang, M. Kitsuregawa, LAPIN-SPAM: an improved algorithm for mining sequential pattern mining, Proceedings of International Special Workshop on Databases for Next Generation Researchers (SWOD'05), Apr. 2005, pp. 8–11.

Hongyan Liu is an associate professor in the Management Science and Engineering Department, Tsinghua University, China. She received her PhD in Management Science from Tsinghua University. Her current research interests include data mining, text and web mining, stream data mining, multi-relational data mining and data warehousing. Dr. Liu is member of ACM, IEEE, SIGKDD, AIS and SIAM. She has published papers in many top international conferences such as VLDB, IEEE ICDE, ACM SIGKDD, IEEE ICDM, SIAM on Data Mining (SDM), and top journals such as ACM Transactions on Database Systems (TODS), ACM Transactions on Information Systems (TOIS), Information Sciences, Decision Support Systems, Computational Intelligence and Knowledge and Information Systems.

Fangzhou Lin has received his bachelor's degree in Management Information Systems from the School of Economics and Management, Tsinghua University. He obtained MS degree in Computer Science from Florida State University in 2010, and now is a database developer at Homes.com.

Jun He is an associate professor in the School of Information, Renmin University of China, China. He received his PhD in Computer Science from Renmin University of China. His current research interests include data mining, web mining, information retrieval, database. Dr. He is member of ACM, IEEE and has published papers in many international conferences such as ACM SIGKDD, IEEE ICDM, SIAM on Data Mining and PAKDD, and journals such as Information Sciences, Decision Support Systems, Computational Intelligence and Knowledge and Information Systems.

Yuanjue Cai has received his bachelor's degree and master degree in Management Information Systems from the School of Economics and Management, Tsinghua University. He currently works at Digital China Holdings Limited.
