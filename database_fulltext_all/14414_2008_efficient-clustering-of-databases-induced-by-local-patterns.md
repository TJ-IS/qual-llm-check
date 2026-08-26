---
otero_id: 14414
otero_key: "7ASEF4VR"
title: "Efficient clustering of databases induced by local patterns"
authors: "Animesh Adhikari; P.R. Rao"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2007.11.001"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dss

# Efficient clustering of databases induced by local patterns

Animesh Adhikari <sup>a,⁎</sup>, P.R. Rao

<sup>a</sup> Department of Computer Science, S P Chowgule College, Margao, Goa 403 602, India <sup>b</sup> Department of Computer Science and Technology, Goa University, Goa 403 206, India

Received 16 November 2005; received in revised form 19 October 2007; accepted 8 November 2007 Available online 17 November 2007

## Abstract

Many large organizations have multiple large databases as they transact from multiple branches. Most of the previous pieces of work are based on a single database. Thus, it is necessary to study data mining on multiple databases. In this paper, we propose two measures of similarity between a pair of databases. Also, we propose an algorithm for clustering a set of databases. Efficiency of the clustering process has been improved using the following strategies: reducing execution time of clustering algorithm, using more appropriate similarity measure, and storing frequent itemsets space efficiently. © 2007 Elsevier B.V. All rights reserved.

Keywords: Clustering; IS coding; Local pattern analysis; Multi-database mining; Similarity between a pair of databases

## 1. Introduction

Many large organizations operate from multiple branches. Some of the branches collect data continuously and store data locally. Thus, the collection of all branch databases might be very large. Effective data analysis using a traditional data mining technique on multi-gigabyte repositories has proven difficult. A quick approximate knowledge from large databases would be adequate for many decision support applications.

Consider a company that deals with multiple large databases. The company might need to make an association analysis involving non-profit making items (products). The objective is to identify the items that neither make much profit nor help promoting other products. An association analysis involving non-profit making items might identify such items. The company could then stop dealing with such items. Such analysis might require identifying similar databases. Two databases are similar if they contain many similar transactions. Again, two transactions are similar if they have many common items. We shall observe latter that two databases containing many common items are not necessarily very similar. First we define a few terms used frequently in this paper.

Let I(D) be the set of items in database D. An itemset is a set of items in a database. An itemset X in D is associated with a statistical measure called support [1], denoted by supp(X, D), for $X \subseteq I ( D )$ Support of an itemset X in D is the fraction of transactions in D containing X. The importance of an itemset could be judged by its support. X is called a frequent itemset (FIS) in D if supp(X, $D ) \geq \alpha .$ , where α is the user defined minimum support. A frequent itemset possesses higher support. Thus, the collection of frequent itemsets determines major characteristics of a database. One could define similarity between a pair databases in terms of their frequent itemsets. Thus, two databases are similar if they have many common frequent itemsets.

Based on the similarity between two databases, we could cluster branch databases. After the clustering process, we could mine all the databases in a class together to make an approximate association analysis involving frequent items. An approximate association analysis could be performed using the frequent itemsets in the union of all the databases in a class. Clustering of databases thus helps reducing data for analyzing the items. In this paper, we study the problem of clustering transactional databases using the local frequent itemsets.

For clustering transactional databases, Wu et at. [21] have proposed two similarity measures sim , and sim . Let $D = \{ D _ { 1 } , ~ D _ { 2 } , ~ . . . , ~ D _ { n } \}$ , where $D _ { i }$ is the database corresponding to i-th branch of a multi-branch company, for $i { = } 1 , 2 , . . . , n$ . sim is based on the items in $D _ { i } ,$ for $i { = } 1 , 2 { , } { \ldots } , n . \ \mathrm { s i m } _ { 1 }$ has been defined as follows:

$$
\operatorname{sim} _ {1} \left(D _ {1}, D _ {2}\right) = | I (D _ {1}) \cap I (D _ {2}) | / | I (D _ {1}) \cup I (D _ {2})
$$

Let $S _ { i }$ be the set of association rules in $D _ { i } ,$ for $i { = } 1 , 2 ,$ …, n. sim is based on the items generated from $S _ { i } ,$ for $i { = } 1 , 2 , . . . , n$ . Let $I ( S _ { i } )$ be the set of items generated from $S _ { i } ,$ for $i { = } 1 , 2 , . . . , n$ . sim has been defined as follows:

$$
\operatorname{sim} _ {2} \left(D _ {1}, D _ {2}\right) = | I \left(S _ {1}\right) \cap I \left(S _ {2}\right) | / | I \left(S _ {1}\right) \cup I \left(S _ {2}\right) |
$$

$I ( S _ { i } ) ~ \subseteq ~ I ( D _ { i } )$ , for $i { = } 1 , \ 2 , . . . , \ n$ . sim estimates similarity between two databases more correctly than sim , since the number of items participate in estimating the similarity between two databases under sim is more than that of sim . A database may not extract any association rule at a given value of pair $( \alpha , \beta )$ , where $\beta$ is the user defined minimum confidence. In such situations, the accuracy of $\mathrm { s i m } _ { 2 }$ is low. In the following example, we discuss a situation where the accuracy of sim and sim are low.

Example 1. A multi-branch company possesses following three databases. $\mathrm { D B } _ { 1 } = \{ \{ a , b , c , e \} , \{ a , b , d , f \}$ $\{ b , ~ c , ~ g \} , ~ \{ b , ~ d , ~ g \} \} , ~ \mathrm { D B } _ { 2 } = \{ \{ a , ~ g \} , ~ \{ b , ~ e \} , ~ \{ c , ~ f \} \}$ $\{ d , g \} \}$ , and $\mathrm { D B } _ { 3 } = \{ \{ a , b , c \} , \{ a , b , d \} , \{ b , c \} , \{ b , d , g \} \}$ Here, $\mathrm { I ( D B _ { 1 } ) } = \{ a , b , c , d , e , f , g \} , \mathrm { I ( D B _ { 2 } ) } = \{ a , b , c , d , e ,$ $f , g \} , \operatorname { I ( D B } _ { 3 } ) = \{ a , b , c , d , g \}$ . Thus, sim $_ 1 ( \mathrm { D B } _ { 1 } , \mathrm { D B } _ { 2 } ) { = } 1 . 0$ (maximum), and $\sin _ { 1 } ( \mathrm { D B } _ { 1 } , ~ \mathrm { D B } _ { 3 } ) = 0 . 7 1 4 2 9$ . Ground realities are as follows: (i) The similarity between $\mathrm { D B } _ { 1 }$ and $\mathrm { D B } _ { 2 }$ is low, since they contain dissimilar transactions. (ii) The similarity between $\mathrm { D B } _ { 1 }$ and $\mathrm { D B } _ { 3 }$ is more than the similarity between $\mathrm { D B } _ { 1 }$ and $\mathrm { D B } _ { 2 } .$ , since $\mathrm { D B } _ { 1 }$ and $\mathrm { D B } _ { 3 }$ contain similar transactions. Thus, the similarity measures $\mathrm { s i m } _ { 1 }$ produces low accuracy in finding the similarity between two databases. There is no frequent itemsets in $\begin{array} { r } { \mathrm { D B } _ { 2 } , } \end{array}$ if $\alpha { > } 0 . 2 5$ . Thus, $I ( S _ { 2 } ) { = } \phi ,$ , if $\alpha { > } 0 . 2 5$ . Hence, the accuracy of sim is low in finding the similarity between $\mathrm { D B } _ { 1 }$ and $\begin{array} { r } { \mathrm { D B } _ { 2 } , } \end{array}$ , if $\alpha { > } 0 . 2 5$ □

Thus, we have observed that the similarity measures based on items in databases might not be appropriate in finding similarity between two databases. A more appropriate similarity measure could be designed based on frequent itemsets in both the databases. The frequent itemsets in two databases could find similarity among transactions in two databases better. Thus, frequent itemsets in two databases could find similarity between two databases more correctly.

Wu et al. [20] have proposed a solution of inverse frequent itemset mining. They argued that one could efficiently generate a synthetic market basket dataset from the frequent itemsets and their supports. Thus, the similarity between two databases could be estimated more correctly by involving supports of the frequent itemsets. We propose two measures of similarity based on the frequent itemsets and their supports. A new algorithm for clustering databases is designed based on a proposed measure of similarity.

The existing industry practice is to refresh a data warehouse on a periodic basis. Let λ be the periodicity of data warehouse refreshing. In this situation, an incremental mining algorithm [14] could be used to obtain updated supports of the existing frequent itemsets in a database on a periodic basis. But, there could be addition $_ { \mathrm { o r } , }$ deletion of frequent itemsets over time. Thus, we need to mine the databases individually again on a periodic basis. Let Λ be the periodicity of data warehouse mining. The values of λ and Λ could be chosen suitably such that $\varLambda { > } \lambda$ . Based on the updated local frequent itemsets, we could cluster the databases afresh.

Another alternative for taming multi-gigabyte data could be sampling. A commonly used technique for approximate query answering is sampling [4]. If an itemset is frequent in a large dataset then it is likely that the itemset is frequent in a sampled dataset. Thus, one could analyze approximately the dataset by analyzing the frequent itemsets in a representative sampled dataset.

The rest of the paper is organized as follows. We formulate the problem in Section 2. In Section 3, we discuss work related to this problem. In Section 4, we cluster all the branch databases. The experimental results are presented in Section 5.

## 2. Problem statement

Let there are n branch databases. Also, let $\mathrm { F I S } ( D _ { i } , \alpha )$ be the set of frequent itemsets corresponding to database $D _ { i }$ at a given value of α, for $i { = } 1 , 2 , . . . , n .$ . Thus, our problem could be stated as follows.

$$
\begin{array}{c} \text { Find   the   best   non - trivial   partition   (if   it   exists)   of   \{D_{1} ,} \\ D _ {2},..., D _ {n} \} \text { using   FIS } (D _ {i}, \alpha), \text { for   i = 1,2,...,n. } \end{array}
$$

A partition [15] is a specific type of clustering. Formal definition of a non-trivial partition is given in Section 4.

## 3. Related work

Jain et al. [12] have presented an overview of clustering methods from a statistical pattern recognition perspective, with a goal of providing useful advice and references to fundamental concepts accessible to the broad community of clustering practitioners. Chan and Chong [6] have devised a novel quantitative model of non-textual World Wide Web classification based on image information. A traditional clustering technique [23] is based on metric attributes. A metric attribute is one whose values can be represented by explicit coordinates in an Euclidean space. Thus, a traditional clustering technique might not work in this case, since we interested in clustering databases. Ali et al. [3] have proposed a partial classification technique using association rules. The clustering of databases using local association rules might not be a good idea. The number of frequent itemsets obtained from a set of association rules might be much less than the number of frequent itemsets extracted using apriori algorithm [2]. Thus, the efficiency of the clustering process would be low. Liu et al. [16] have proposed multidatabase mining technique that searches only the relevant databases. Identifying relevant databases is based on selecting the relevant tables (relations) that contain specific, reliable and statistically significant information pertaining to the query. Our study involves in clustering transactional databases. Yin and Han [22] have proposed a new strategy for relational heterogeneous database classification. This strategy might not be suitable for clustering transactional databases. Chen et al. [7] propose a method of discovering customer purchasing patterns by extracting associations or co-occurrences from stores' transactional databases.

In the context of similarity measures, Tan et al. [19] have presented an overview of twenty one interestingness measures proposed in the statistics, machine learning and data mining literature. The itemset measures, i.e., support and confidence [1] are used to identify frequently occurring association rules between two sets of items in large databases. Our first measure, simi , is similar to measure Jaccard [19]. Measures such as support, interest [19], cosine [19] do not serve as good measures of similarity, since their denominators are not relevant. Other measures in [19] might not be relevant in finding similarity between two databases.

Zhang et al. [25] designed a local pattern analysis for mining multiple databases. Zhang et al. [24] studied various strategies for mining multiple databases. For utilizing the low-cost information and knowledge on the internet, Su et al. [18] have proposed a logical framework for identifying quality knowledge from different data sources. It helps working towards the development of an agreed ontology.

Data mining serves as a tool for decision making as well as managing activities. Accurate estimations of software size in the early stages of a software project are critical in software project management because they lead to a good planning and reduce project costs. García et al. [10] have studied the relation between early software size measures as the function points and measures of the final product as the lines of code.

## 4. Clustering databases

Our approach of finding the best partition of a set of databases has been explained in the following steps. (i) Find $\mathrm { F I S } ( D _ { i } , \ \alpha )$ , for $i { = } 1 , \ 2 , . . . , \ n .$ (ii) Determine the similarity between each pair of databases using the proposed measure of similarity simi<sub>2</sub>. (iii) Check for the existence of partitions at the required similarity levels [please see Theorem 5]. (iv) Calculate the goodness values for all the non-trivial partitions. (v) Report the nontrivial partition for which the goodness value is the maximum. All the steps (i) to (v) will be followed and explained with the help of a running example. We start with an example of a multi-branch company that has multiple databases.

Example 2. A multi-branch company has seven branches. The branch databases are given below.

$D _ { 1 } = \{ ( a , b , c ) , ( a , c ) , ( a , c , d ) \} ; D _ { 2 } = \{ ( a , c ) , ( a , b ) , ( a , c , e ) \} ; D _ { 3 } = \{ ( a , e ) , ( a , c , e ) , ( a , b , c ) \} ; D _ { 4 } = \{ ( f , d ) , ( f , d , e ) , ( f , f , e ) , ( a , b , e ) \} .$ $h ) , ( e , f , d ) , ( e , f , h ) \} ; D _ { s } = \{ ( g , h , i ) , ( i , j ) , ( h , i ) , ( i , j , g ) \} ; D _ { 6 } = \{ ( g , h , i ) , ( i , j , h ) , ( i , j ) \} ; D _ { 7 } = \{ ( a , b ) , ( g , h ) , ( h , i ) , ( h , i ) , ( h , i ) \}$ $i , j ) \}$ . The sets of frequent itemsets are given below. $\operatorname { F I S } ( D _ { 1 } , 0 . 3 5 ) = \{ ( a , 1 . 0 ) , ( c , 1 . 0 ) , ( a c , 1 . 0 ) \} ; \operatorname { F I S } ( D _ { 2 } , 0 . 3 5 ) = \{ ( a , 1 . 0 ) , ( c , 0 . 6 7 ) , ( a c , 0 . 6 7 ) \} ; \operatorname { F I S } ( D _ { 3 } , 0 . 3 5 ) = \{ ( a , 0 . 3 ) , ( a c , 0 . 6 7 ) \} .$ $1 . 0 ) , ( c , 0 . 6 7 ) , ( e , 0 . 6 7 ) , ( a c , 0 . 6 7 ) , ( a e , 0 . 6 7 ) , ( a e , 0 . 6 7 ) ; \mathrm { F I S } ( D _ { 4 } , 0 . 3 5 ) = \{ ( d , 0 . 7 5 ) , ( e , 0 . 5 ) , ( f , 1 . 0 ) , ( h , 0 . 5 ) , ( d f , 0 . 7 5 ) , ( e f , 0 . 5 ) \}$ $( \langle \hbar , 0 . 5 \rangle ) _ { \mathrm { i } } ^ { * } \operatorname { F I S } ( D _ { 5 } , 0 . 3 5 ) = \{ ( g , 0 . 5 ) , ( h , 0 . 5 ) , ( i , 1 . 0 ) _ { \mathrm { i } } ^ { * } , ( j , 0 . 5 ) , ( g i , 0 . 5 ) , ( h i , 0 . 5 ) , ( i j , 0 . 5 ) , \} ; \operatorname { F I S } ( D _ { 6 } , 0 . 3 5 ) = \{ ( i , 1 . 0 )$ $( j , 0 . 6 7 ) , ( h , 0 . 6 7 ) , ( h i , 0 . 6 7 ) , ( i j , 0 . 6 7 ) \} ; \mathrm { F I S } ( D _ { 7 } , 0 . 3 5 ) = \{ ( h , 0 . 7 5 ) , ( i , 0 . 5 ) , ( h i , 0 . 5 ) \}$ 厂

Based on the sets of frequent itemsets in a pair of databases, one could define many measures of similarity between them. We propose two measures of similarity between a pair of databases. Our first measure $\mathrm { \dot { \ s i m i } _ { 1 } }$ is defined as follows.

Definition 1. The measure of similarity simi between databases $D _ { 1 }$ and $D _ { 2 }$ is defined as follows.

$$
\operatorname{simi} _ {1} (D _ {1}, D _ {2}, \alpha) = \frac {\left| \mathrm{FIS} (D _ {1} , \alpha) \cap \mathrm{FIS} (D _ {2} , \alpha) \right|}{\left| \mathrm{FIS} (D _ {1} , \alpha) \cup \mathrm{FIS} (D _ {2} , \alpha) \right|},
$$

where, the symbols ∩ and ∪ stand for the intersection and union operations of set theory, respectively.

The similarity measure $\mathrm { \dot { \ s i m i } _ { 1 } }$ is the ratio of the number frequent itemsets common to $D _ { 1 }$ and $D _ { 2 } ,$ , and the total number of distinct frequent itemsets in $D _ { 1 }$ and $D _ { 2 }$ . Frequent itemsets are the dominant patterns that determine major characteristics of a database. There are many implementations [8] of mining frequent itemsets in a database. Let X and Y be two frequent itemsets in database DB. The itemset X is more dominant than the itemset Y in DB if supp(X, DB) N supp(Y, DB). Therefore, the characteristics of DB are revealed more by the pair (X, supp(X, DB)) than that of (Y, supp(Y, DB)). Thus, a good measure of similarity between two databases is a function of the supports of the frequent itemsets in the databases. Our second measure of similarity $\mathrm { s i m i } _ { 2 }$ is defined as follows.

Definition 2. The measure of similarity simi between databases $D _ { 1 }$ and $D _ { 2 }$ is defined as follows.

$$
\operatorname{simi} _ {2} (D _ {1}, D _ {2}, \alpha) = \frac {\sum_ {X \in \{F I S (D _ {1} , \alpha) \cap F I S (D _ {2} , \alpha) \}} \text {minimum} \{\operatorname{supp} (X , D _ {1}) , \operatorname{supp} (X , D _ {2}) \}}{\sum_ {X \in \{F I S (D _ {1} , \alpha) \cup F I S (D _ {2} , \alpha) \}} \text {maximum} \{\operatorname{supp} (X , D _ {1}) , \operatorname{supp} (X , D _ {2}) \}}
$$

where, the symbols ∩ and ∪ stand for the intersection and union operations of set theory, respectively. Assume that, supp(X, D ) = 0, if $X \not \in \mathrm { F I S } ( D _ { i } , \alpha ) $ , for i = 1, 2. □

With reference to Example 1, the frequent itemsets in different databases are given as follows: $\mathrm { F I S } ( \mathrm { D B } _ { 1 } , 0 . 3 ) { = } \{ a ( 0 . 5 ) , $ $b ( 1 . 0 ) , c ( 0 . 5 ) , d ( 0 . 5 ) , g ( 0 . 5 ) , a b ( 0 . 5 ) , b c ( 0 . 5 ) , b d ( 0 . 5 ) \} , \mathrm { ~ F I S ( D B _ { 2 } , ~ 0 . 3 ) = \{ g ( 0 . 5 ) \} ~ }$ , and $\mathrm { F I S } ( \mathrm { D B } _ { 3 } , 0 . 3 ) = \{ a ( 0 . 5 ) , b ( 1 . 0 ) $ $c ( 0 . 5 ) , d ( 0 . 5 ) , a b ( 0 . 5 ) , b c ( 0 . 5 ) , b d ( 0 . 5 ) \}$ . We obtain simi $_ { 1 } ( \mathrm { D B } _ { 1 } , \mathrm { D B } _ { 2 } , 0 . 3 ) = 0 . 1 2 5$ , simi $_ { 1 } ( \mathrm { D B } _ { 1 } , \mathrm { D B } _ { 3 } , 0 . 3 ) = 0 . 8 7 5 ,$ , simi $( \mathrm { D B } _ { 1 } , \ \mathrm { D B } _ { 2 } , \ 0 . 3 ) { = } 0 . 1 1 1$ , and $\mathrm { s i m i _ { 2 } ( D B _ { 1 } , ~ D B _ { 3 } , ~ } 0 . 3 ) = 0 . 8 8 9$ . Thus, our proposed measures simi and simi match ground reality better than the existing measures. Theorem 1 justifies the fact that $\mathrm { s i m i } _ { 2 }$ matches ground reality better than simi .

Theorem 1. The similarity measure simi<sub>2</sub> has better discriminating power than that of the similarity measure simi<sub>1</sub>.

Proof. The support of a frequent itemset could be considered as its weight in the database. But, we attach an weight 1.0 to itemset X in database $D _ { i } ,$ under the similarity measure simi , if $X { \in { \mathrm { F I S } } } ( D _ { i } , \alpha )$ , for i = 1, 2. We attach an weight supp $( X , D _ { i } )$ to the itemset X in database $D _ { i } ,$ under the similarity measure $\mathrm { s i m i } _ { 2 } ,$ , if $X { \in { \mathrm { F I S } } } ( D _ { i } , \alpha )$ , for $i = 1 , 2$ . The similarity measures $\mathrm { s i m } _ { 1 }$ and $\mathrm { s i m } _ { 2 }$ are defined as a ratio of two quantities. If $X { \in { \mathrm { F I S } } } ( D _ { i } , \alpha )$ , and $X { \in { \mathrm { F I S } } } ( D _ { j } , \alpha )$ , then it is more justifiable to add minimum $\{ \operatorname { s u p p } ( X , D _ { i } )$ , supp(X, $D _ { j } ) \}$ (instead of 1.0) in the numerator and maximum $\{ \operatorname { s u p p } ( X , D _ { i } )$ supp(X, $D _ { j } ) \}$ (instead of 1.0) in the denominator for the itemset X, for $i , j \in \{ 1 , 2 \}$ . I $\operatorname { f } X { \in { \mathrm { F I S } } } ( D _ { i } , \alpha )$ , and $X \notin \mathrm { F I S } ( D _ { j } , \alpha )$ then it is more justifiable to add 0 in the numerator and supp(X, D<sub>i</sub>) (instead of 1.0) in the denominator for the itemset X, for $i , j \in \{ 1 , 2 \}$ }. Hence, the theorem follows. □

Example 3 verifies that simi matches ground reality better than simi .

Example 3. With reference to Example 2, supp( $\{ a \} , D _ { 1 } ) = \operatorname { s u p p } ( \{ c \} , D _ { 1 } ) = \operatorname { s u p p } ( \{ a , c \} , D _ { 1 } ) = 1 . 0$ $\operatorname { s u p p } ( \{ a \} , D _ { 2 } ) = 1 . 0$ an $\mathrm { 1 } \operatorname* { s u p p } _ { 2 } ( \{ c \} , D _ { 2 } ) = \operatorname* { s u p p } ( \{ a , c \} , D _ { 2 } ) = 0 . 6 7 . \ \mathrm { s i m i } _ { 2 } ( D _ { 1 } , D _ { 2 } , 0 . 3 5 ) = 0 . 7 8 \ \mathrm { s i m e }$ , and $\mathrm { s i m i _ { 1 } } ( D _ { 1 } , D _ { 2 } , 0 . 3 5 ) { = } 1 . 0$ . We observe that the databases $D _ { 1 }$ and $D _ { 2 }$ are highly similar, but not the same. Thus, the similarity obtained by simi matches the ground reality better. □

We study some interesting properties of simi and simi using Theorems 2, 3 and 4.

Theorem 2. The similarity measure simi satisfies the following properties, $( k = l , ~ 2 )$

$$
(i) 0 \leq \operatorname{simi} _ {k} \left(D _ {i}, D _ {j}, \alpha\right) \leq 1, (i i) \operatorname{simi} _ {k} \left(D _ {i}, D _ {j}, \alpha\right) = \operatorname{simi} _ {k} \left(D _ {j}, D _ {i}, \alpha\right), (i i i) \operatorname{simi} _ {k} \left(D _ {i}, D _ {j}, \alpha\right) = 1, f o r i, j = 1, 2, \dots , n.
$$

Proof. The properties follow from the definition of simi , (k = 1, 2).

We express the distance between two databases in term of their similarity.

Definition 3. The distance measure $\mathrm { d i s t _ { k } }$ between two databases $D _ { 1 }$ and $D _ { 2 }$ based on the similarity measure $\mathrm { s i m i } _ { k }$ is defined as dis $\mathrm { \Delta } _ { \mathrm { t } } ( D _ { 1 } , D _ { 2 } , \alpha ) = 1 - \mathrm { s i m i } _ { k } ( D _ { 1 } , D _ { 2 } , \alpha ) , ( k { = } 1 , 2 )$ □

A good distance measure satisfies the metric properties [5]. Higher the distance between two databases, lower is the similarity between them. For the purpose of elegant presentation, we use the notation $I _ { i }$ in place of $\mathrm { F I S } ( D _ { i } , \alpha )$ in Theorems 3 and 4, for i=1, 2.

Theorem 3. $d i s t _ { I }$ is a metric over $\it { 1 0 , 1 7 . }$

Proof. We show that $\mathrm { d i s t } _ { 1 }$ satisfies the triangular inequality. Other properties of a metric follow from Theorem 2.

$$
\operatorname{dist} _ {1} \left(D _ {1}, D _ {2}, \alpha\right) = 1 - \frac {\left| I _ {1} \cap I _ {2} \right|}{\left| I _ {1} \cup I _ {2} \right|} \geq \frac {\left| I _ {1} - I _ {2} \right| + \left| I _ {2} - I _ {1} \right|}{\left| I _ {1} \cup I _ {2} \cup I _ {3} \right|}\tag{1}
$$

$$
\text { Thus,   } \operatorname{dist} _ {1} (D _ {1}, D _ {2}, \alpha) + \operatorname{dist} _ {1} (D _ {2}, D _ {3}, \alpha) \geq \frac {\left| I _ {1} - I _ {2} \right| + \left| I _ {2} - I _ {1} \right| + \left| I _ {2} - I _ {3} \right| + \left| I _ {3} - I _ {2} \right|}{\left| I _ {1} \cup I _ {2} \cup I _ {3} \right|}\tag{2}
$$

$$
= \frac {\left| I _ {1} \cup I _ {2} \cup I _ {3} \right| - \left| I _ {1} \cap I _ {2} \cap I _ {3} \right| + \left| I _ {1} \cap I _ {3} \right| + \left| I _ {2} \right| - \left| I _ {1} \cap I _ {2} \right| - \left| I _ {2} \cap I _ {3} \right|}{\left| I _ {1} \cup I _ {2} \cup I _ {3} \right|}\tag{3}
$$

$$
= 1 - \frac {\left| I _ {1} \cap I _ {2} \cap I _ {3} \right| - \left| I _ {1} \cap I _ {3} \right| - \left| I _ {2} \right| + \left| I _ {1} \cap I _ {2} \right| + \left| I _ {2} \cap I _ {3} \right|}{\left| I _ {1} \cup I _ {2} \cup I _ {3} \right|}\tag{4}
$$

$$
= 1 - \frac {\left\{\left| I _ {1} \cap I _ {2} \cap I _ {3} \right| + \left| I _ {1} \cap I _ {2} \right| + \left| I _ {2} \cap I _ {3} \right| \right\} - \left\{\left| I _ {1} \cap I _ {3} \right| + \left| I _ {2} \right| \right\}}{\left| I _ {1} \cup I _ {2} \cup I _ {3} \right|}\tag{5}
$$

Let the number of elements in the shaded regions of Fig. 1(c) and (d) be $N _ { 1 }$ and $N _ { 2 } ,$ , respectively. Then the expression (5) becomes

$$
1 - \frac {N _ {1} - N _ {2}}{\left| I _ {1} \cup I _ {2} \cup I _ {3} \right|} \geq \left\{ \begin{array}{l l} 1 - \frac {N _ {1} - N _ {2}}{\left| I _ {1} \cup I _ {2} \cup I _ {3} \right|}, & \text { if } N _ {1} \geq N _ {2} \quad (\text { case   1 }) \\ 1 - \frac {\left| I _ {1} \cap I _ {3} \right|}{\left| I _ {1} \cup I _ {2} \cup I _ {3} \right|}, & \text { if } N _ {1} <   N _ {2} \quad (\text { case   2 }) \end{array} \right.\tag{6}
$$

![](/api/attachments/7ASEF4VR/fulltext/images/146fc81acedea8a0f3c7e7b87d0ee3e26544563dc59fcaa51957dfa33a046ff1.jpg)  
Fig. 1. Simplification using Venn diagram.

In case 1, the expression remains the same. In case 2, a positive quantity $I _ { 1 } \cap I _ { 3 }$ has been put in place of a negative quantity $N _ { 1 } - N _ { 2 }$ . Thus, the expression (6) is

$$
\geq \left\{ \begin{array}{l} 1 - \frac {N _ {1} - N _ {2}}{\left| I _ {1} \cup I _ {3} \right|}, \text {   if   } N _ {1} \geq N _ {2} \\ 1 - \frac {\left| I _ {1} \cap I _ {3} \right|}{\left| I _ {1} \cup I _ {3} \right|}, \text {   if   } N _ {1} <   N _ {2} \end{array} \right. \geq \left\{ \begin{array}{l} 1 - \frac {N _ {1}}{\left| I _ {1} \cup I _ {3} \right|}, \text {   if   } N _ {1} \geq N _ {2} \\ 1 - \frac {\left| I _ {1} \cap I _ {3} \right|}{\left| I _ {1} \cup I _ {3} \right|}, \text {   if   } N _ {1} <   N_{2} \end{array} \right.\tag{7}
$$

$$
\geq \left\{ \begin{array}{l} 1 - \frac {\left| I _ {1} \cap I _ {3} \right|}{\left| I _ {1} \cup I _ {3} \right|}, \text {   if   } N _ {1} \geq N _ {2} \\ 1 - \frac {\left| I _ {1} \cap I _ {3} \right|}{\left| I _ {1} \cup I _ {3} \right|}, \text {   if   } N _ {1} <   N _ {2} \end{array} \right., \text {   where   } N _ {1} = | I _ {1} \cap I _ {2} \cap I _ {3} | \leq | I _ {1} \cap I _ {3} |\tag{8}
$$

Therefore, irrespective of the relationship between $N _ { 1 }$ and $N _ { 2 } , \mathrm { d i s t } _ { 1 } ( D _ { 1 } , D _ { 2 } , \alpha ) + \mathrm { d i s t } _ { 1 } ( D _ { 2 } , D _ { 3 } , \alpha ) \geq \mathrm { d i s t } _ { 1 } ( D _ { 1 } , D _ { 3 } , \alpha ) |$ Thus, dist satisfies the triangular inequality. □

We shall also show that dist satisfies the metric properties.

Theorem 4. dist is a metric over $\mathit { l 0 , l J . }$

Proof. We show that $\mathrm { d i s t } _ { 2 }$ satisfies the triangular inequality. Other properties of a metric follow from Theorem 2.

$$
\operatorname{dist} _ {2} \left(D _ {1}, D _ {2}, \alpha\right) = 1 - \frac {\sum_ {x \in I _ {1} \cap I _ {2}} \text {minimum} \left\{\operatorname{supp} \left(x , D _ {l}\right) , \operatorname{supp} \left(x , D _ {2}\right) \right\}}{\sum_ {x \in I _ {1} \cup I _ {2}} \text {maximum} \left\{\operatorname{supp} \left(x , D _ {l}\right) , \operatorname{supp} \left(x , D _ {2}\right) \right\}} = 1 - \frac {\sum_ {x \in I _ {1} \cap I _ {2}} \min _ {1 2} (x)}{\sum_ {x \in I _ {1} \cup I _ {2}} \max _ {1 2} (x)}\tag{9}
$$

where, $\scriptstyle \operatorname* { m a x } _ { i j } ( x ) = \operatorname* { m a x i m u m } \{ \operatorname* { s u p p } ( x , D _ { i } )$ , supp(x, $D _ { j } ) \}$ , and $ \scriptstyle \operatorname* { m i n } _ { i j } ( x ) = \mathrm { m i n i m u m } \{ \mathrm { s u p p } ( x , D _ { i } )$ , supp(x, $D _ { j } ) \}$ }, for $i \neq j .$ Also, let max<sub>123</sub>(x) = maximum{supp(x, $D _ { 1 } )$ , supp(x, $D _ { 2 } )$ , supp(x, $D _ { 3 } ) _ { j } ^ { \dagger }$ }, and $\mathrm { m i n } _ { 1 2 3 } ( x ) { = } \mathrm { m i n i m u m } \{ \mathrm { s u p p } ( x , D _ { 1 } )$ , supp $( x , D _ { 2 } )$ , supp(x, $D _ { 3 } ) _ { j } ^ { \backslash }$

Thus, $\mathrm { d i s t } _ { 2 } ( D _ { 1 } , D _ { 2 } , \alpha ) + \mathrm { d i s t } _ { 2 } ( D _ { 2 } , D _ { 3 } , \alpha )$

$$
= \frac {\sum_ {x \in I _ {1} \cup I _ {2}} \max _ {1 2} (x) - \sum_ {x \in I _ {1} \cap I _ {2}} \min _ {1 2} (x)}{\sum_ {x \in I _ {1} \cup I _ {2}} \max _ {1 2} (x)} + \frac {\sum_ {x \in I _ {2} \cup I _ {3}} \max _ {2 3} (x) - \sum_ {x \in I _ {2} \cap I _ {3}} \min _ {2 3} (x)}{\sum_ {x \in I _ {2} \cup I _ {3}} \max _ {2 3} (x)}\tag{10}
$$

$$
\begin{array}{l} \geq \frac {\sum_ {x \in I _ {1} - I _ {2}} \max _ {1 2} (x) + \sum_ {x \in I _ {2} - I _ {1}} \max _ {1 2} (x)}{\sum_ {x \in I _ {1} \cup I _ {2}} \max _ {1 2} (x)} + \frac {\sum_ {x \in I _ {2} - I _ {3}} \max _ {2 3} (x) + \sum_ {x \in I _ {3} - I _ {2}} \max _ {2 3} (x)}{\sum_ {x \in I _ {2} \cup I _ {3}} \max _ {2 3} (x)} \\ \geq \frac {\sum_ {x \in I _ {1} - I _ {2}} \max _ {1 2} (x) + \sum_ {x \in I _ {2} - I _ {1}} \max _ {1 2} (x) + \sum_ {x \in I _ {2} - I _ {3}} \max _ {2 3} (x) + \sum_ {x \in I _ {3} - I _ {2}} \max _ {2 3} (x)}{\sum_ {x \in I _ {1} \cup I _ {2} \cup I _ {3}} \max _ {1 2 3} (x)} \end{array}\tag{11}
$$

12

Using the simplification performed in Fig. 2, the expression (12) becomes

$$
\frac {\sum_ {x \in I _ {1} \cup I _ {2} \cup I _ {3}} \max _ {1 2 3} (x) - N _ {1} + N _ {2}}{\sum_ {x \in I _ {1} \cup I _ {2} \cup I _ {3}} \max _ {1 2 3} (x)}\tag{13}
$$

where, $N _ { 1 }$ and $N _ { 2 }$ are the value of $\begin{array} { r } { \sum _ { \mathbf { x } } \operatorname* { m a x } _ { 1 2 3 } \left( \mathbf { x } \right) } \end{array}$ over the shaded regions of Fig. 2(c) and (d), respectively. The expression (13) is equal to

$$
1 - \frac {N _ {1} - N _ {2}}{\sum_ {x \in I _ {1} \cup I _ {2} \cup I _ {3}} \max _ {1 2 3} (x)} \geq \left\{ \begin{array}{l} 1 - \frac {N _ {1}}{\sum_ {x \in I _ {1} \cup I _ {2} \cup I _ {3}} \max _ {1 2 3} (x)}, \text {   if   } N _ {1} \geq N _ {2} \\ 1 - \frac {N _ {1} - N _ {2}}{\sum_ {x \in I _ {1} \cup I _ {2} \cup I _ {3}} \max _ {1 2 3} (x)}, \text {   if   } N _ {1} <   N _ {2} \end{array} \right. \geq \left\{ \begin{array}{l} 1 - \frac {\sum_ {x \in I _ {1} \cap I _ {3}} \max _ {1 3} (x)}{\sum_ {x \in I _ {1} \cup I _ {2} \cup I _ {3}} \max _ {1 2 3} (x)}, \text {   if   } N _ {1} \geq N _ {2} \\ 1 - \frac {\sum_ {x \in I _ {1} \cap I _ {3}} \max _ {1 3} (x)}{\sum_ {x \in I _ {1} \cup I _ {2} \cup I _ {3}} \max _ {1 2 3} (x)}, \text {   if   } N _ {1} <   N _ {2} \end{array} \right.\tag{14}
$$

Therefore, irrespective of the relationship between $N _ { 1 }$ and $N _ { 2 } , \mathrm { d i s t } _ { 2 } ( D _ { 1 } , D _ { 2 } , \alpha ) + \mathrm { d i s t } _ { 2 } ( D _ { 2 } , D _ { 3 } , \alpha ) \geq \mathrm { d i s t } _ { 2 } ( D _ { 1 } , D _ { 3 } , \alpha )$ Thus, dis $\mathbf { t } _ { 2 }$ satisfies the triangular inequality. □

Given a set of databases, the similarity between pairs of databases could be expressed by a square matrix, called database similarity matrix (DSM). We define DSM of a set of databases as follows.

Definition 4. Let $D { = } \{ D _ { 1 } , D _ { 2 } { , } { \ldots } , D _ { n } \}$ be the set of all databases. The database similarity matrix $\mathrm { D S M } _ { k }$ of D using the measure of similarity simi , is a symmetric square matrix of size n by n, whose $( i , j ) \cdot$ -th element $\mathrm { D S M } _ { k } ^ { i , j } ( D , \alpha ) { = } \mathrm { s i m i } _ { k } ( D _ { i } ,$ $D _ { j } , \alpha )$ ; for $D _ { i } , D _ { j } \in D$ , and $i , j { = } 1 , 2 , . . . , n , ( k { = } 1 , 2 )$ . □

For n databases, there are ${ } ^ { n } C _ { 2 }$ pairs of databases. For each pair of databases, we compute similarity between them. If the similarity is high then the databases may be put in the same class. We define a class as follows.

Definition 5. Let $D { = } \{ D _ { 1 } , D _ { 2 } { , } { \ldots } , D _ { n } \}$ . A class $\mathrm { c l a s s } _ { k } ^ { \delta }$ formed at the level of similarity $\delta$ under the measure of similarity $\mathrm { s i m i } _ { k } ,$ is defined as

$$
\operatorname{class} _ {k} ^ {\delta} (D, \alpha) = \left\{ \begin{array}{l} P: P \subseteq D, | P | \geq 2, \text {   and   } \operatorname{simi} _ {k} (A, B, \alpha) \geq \delta , \text {   for   } A, B \in P \\ P: P \subseteq D, | P | = 1 \end{array} \right., (k = 1, 2).
$$

A DSM could be viewed as a complete weighted graph. Each database forms a vertex. An weight of an edge is the similarity between the pair of concerned databases. Le $D { = } \{ D _ { 1 } , D _ { 2 } { , } { \ldots } , D _ { n } \}$ be the set of all databases. During the process of clustering, we assume that the databases $\mathrm { D } _ { 1 } , D _ { 2 } , . . . , D _ { i }$ have been included in some classes, and the remaining databases are yet to be clustered. Then the clustering process forms the next class by finding a maximal complete sub-graph of the complete weighted graph containing vertices $D _ { r + 1 } , D _ { r + 2 } . . . , D _ { n } .$ A maximal complete sub-graph is defined as follows.

![](/api/attachments/7ASEF4VR/fulltext/images/afc17145fd678dc83f2cd6e3dfbf1b6babaa79f8a1a1bb49107c6b1ec08b5329.jpg)  
(a)

![](/api/attachments/7ASEF4VR/fulltext/images/a0f3ef239bdf7f02efe634af195db32b4fc700e4c26622a9fbc2b247a074ffca.jpg)  
(b)

![](/api/attachments/7ASEF4VR/fulltext/images/c8de06fb225a1653f02b46e5865b98570591a315de674b30613da14d71844da6.jpg)  
(c)

![](/api/attachments/7ASEF4VR/fulltext/images/d79bce3d243a7f162301185c0ab2c6d909e63cb718c12cb0527141e58a92a401.jpg)  
(d)  
Fig. 2. Simplification using Venn diagram.

Definition 6. An weighted complete sub-graph g of a complete weighted graph G is maximal at the similarity level δ if the following conditions are true: (i) The weight of every edge of g is greater than or equal to δ. (ii) The addition of one more vertex (i.e., a database) to g leads to the addition of at least one edge to g having weight less than δ. □

We need to find out a maximal weighted complete sub-graph of the complete weighted graph of the remaining vertices to form the next class. This process continues till all the vertices are clustered. A clustering of databases could be defined as follows.

Definition 7. Let D be a set of databases. Let $\pi _ { k } ^ { \delta } ( D , \alpha )$ be a clustering of databases in D at the similarity level δ under the similarity measure simi . Then, $\pi _ { k } ^ { \delta } ( D , \alpha ) = \{ X ; X { \in } \rho ( D )$ , and X is a class ${ } _ { k } ^ { \delta } ( D , \alpha ) \}$ , where $\rho ( D )$ is the power set of D, (k = 1, 2). □

During the clustering process we may like to impose the restriction that each database belongs to at least one class. This restriction makes a clustering complete. We define a complete clustering as follows.

Definition 8. Let D be a set of databases. Let $\pi _ { k } ^ { \delta } ( D , \alpha ) = \{ C _ { k , I } ^ { \delta } ( D , \alpha ) , C _ { k , 2 } ^ { \delta } ( D , \alpha ) , . . . , C _ { k , m } ^ { \delta } ( D , \alpha ) \}$ , where $C _ { k , i } ^ { \delta } ( D , \alpha )$ is the i-th class of $\pi _ { k } ^ { \delta } .$ , for $i { = } 1 , 2 { , } . . . , m . \pi _ { k } ^ { \delta }$ is complete, $\mathsf { i f } \cup _ { i = 1 } ^ { m } C _ { k , i } ^ { \delta } ( D , \alpha ) { = } D , ( k { = } 1 , 2 )$ □

In a complete clustering, two classes may have a common database. We may be interested in finding out a clustering of mutually exclusive classes. A mutually exclusive clustering could be defined as follows.

Definition 9. Let D be a set of databases. Let $\pi _ { k } ^ { \delta } ( D , \alpha ) \mathrm { = } \{ C _ { k , 1 } ^ { \delta } ( D , \alpha ) , C _ { k , 2 } ^ { \delta } ( D , \alpha ) , . . . , C _ { k m } ^ { \delta } ( D , \alpha ) \}$ , where $C _ { k , i } ^ { \delta } ( D , \alpha )$ is the i-th class of $\pi _ { k } ^ { \delta } ,$ for $i { = } 1 , 2 { , } . . . , m . \ \pi _ { k } ^ { \delta }$ is mutually exclusive if $C _ { k , i } ^ { \delta } ( D , \alpha ) \cap C _ { k , j } ^ { \delta } ( D , \alpha ) = \phi$ , for $i \neq j , 1 \leq i , j \leq m .$ $( k { = } 1 , 2 )$ □

We may be interested in finding out such a mutually exclusive and complete clustering. A partition of a set of databases is defined as follows.

Definition 10. Let D be a set of databases. Also, let $\pi _ { k } ^ { \delta } ( D , \alpha )$ be a clustering of databases in D at the similarity level δ under the similarity measure simi . $\mathrm { I f } \pi _ { k } ^ { \delta } ( D , \alpha )$ is a mutually exclusive and complete clustering then it is called a partition, $( k { = } 1 , 2 )$ □

Definition 11. Let D be a set of databases. Also, let $\pi _ { k } ^ { \delta } ( D , \alpha )$ be a partition of D at the similarity level δ under the similarity measure sim $\mathfrak { i } _ { k } . \ \pi _ { k } ^ { \delta } ( D , \alpha )$ is called a non-trivial partition if $1 < \vert \pi _ { k } ^ { \delta } \vert < n , ( k { = } 1 , 2 )$ □

A clustering is not necessarily be a partition. In the following example, we wish to find partitions (if they exist) of a set of databases.

Example 4. With reference to Example 2, consider the set of databases $D { = } \{ D _ { 1 } , D _ { 2 } , . . . , D _ { 7 } \}$ . The corresponding $\mathrm { D S M } _ { 2 }$ is given below.

$$
\mathrm{DSM} _ {2} (D, 0. 3 5) = \left[ \begin{array}{c c c c c c c} 1. 0 & 0. 7 8 0 & 0. 5 3 9 & 0. 0 & 0. 0 & 0. 0 & 0. 0 \\ 0. 7 8 0 & 1. 0 0 & 0. 6 3 6 & 0. 0 & 0. 0 & 0. 0 & 0. 0 \\ 0. 5 3 9 & 0. 6 3 6 & 1. 0 & 0. 0 6 1 & 0. 0 & 0. 0 & 0. 0 \\ 0. 0 & 0. 0 & 0. 0 6 1 & 1. 0 & 0. 0 6 3 & 0. 0 6 5 & 0. 0 8 7 \\ 0. 0 & 0. 0 & 0. 0 & 0. 0 6 3 & 1. 0 & 0. 6 4 1 & 0. 3 5 3 \\ 0. 0 & 0. 0 & 0. 0 & 0. 0 6 5 & 0. 6 4 1 & 1. 0 & 0. 4 4 4 \\ 0. 0 & 0. 0 & 0. 0 & 0. 0 8 7 & 0. 3 5 3 & 0. 4 4 4 & 1. 0 \end{array} \right]
$$

We arrange all non-zero and distinct $\mathrm { D S M } _ { 2 } ^ { i , j } ( \mathrm { D } , 0 . 3 5 )$ values in non-increasing order, for $1 \leq i < j \leq 7$ . The arranged similarity values are given as follows: 0.780, 0.641, 0.636, 0.539, 0.444, 0.353, 0.087, 0.065, 0.063, 0.061. We get many non-trivial partitions at different similarity levels. At similarity levels 0.780, 0.641, 0.539, and 0.353, we get nontrivial partitions as $\pi _ { 2 } ^ { 0 . 7 8 0 } = \{ \{ D _ { 1 } , D _ { 2 } \} , \{ D _ { 3 } \} , \{ D _ { 4 } \} , \{ D _ { 5 } \} , \{ D _ { 6 } \} , \{ D _ { 7 } \} \} , \pi _ { 2 } ^ { 0 . 6 4 1 } = \{ \{ D _ { 1 } , D _ { 2 } \} , \{ D _ { 3 } \} , \{ D _ { 4 } \} , \{ D _ { 5 } , D _ { 6 } \} \} .$ $\{ D _ { 7 } \} \} , \ \pi _ { 2 } ^ { 0 . 5 3 9 } = \{ \{ D _ { 1 } , \ D _ { 2 } , \ D _ { 3 } \} , \ \{ D _ { 4 } \} , \ \{ D _ { 5 } , \ D _ { 6 } \} , \ \{ D _ { 7 } \} \}$ , and $\pi _ { 2 } ^ { 0 . 3 5 3 } = \{ \{ D _ { 1 } , ~ D _ { 2 } , ~ D _ { 3 } \} , ~ \{ D _ { 4 } \} , ~ \{ D _ { 5 } , ~ D _ { 6 } , ~ D _ { 7 } \} \} ,$ respectively. □

Our BestDatabasePartition algorithm (presented in Section 4.1) is based on binary similarity matrix (BSM). We derive binary similarity matrix ${ \mathrm { B S M } } _ { k }$ from the corresponding $\mathrm { D S M } _ { k } , ( k = 1 , 2 ) . \mathrm { \ B S M } _ { k }$ is defined as follows.

Definition 12. The $( i , j )$ -th element of the binary similarity matrix ${ \mathrm { B S M } } _ { k }$ at the similarity level δ using the similarity measure $\mathrm { s i m i } _ { k }$ is defined as follows.

$$
\mathrm{BSM} _ {k} ^ {i, j} (D, \alpha , \delta) = \left\{ \begin{array}{l l} 1, & \text { if   } \operatorname{simi} _ {k} (D _ {i}, D _ {j}, \alpha) \geq \delta \\ 0, & \text { otherwise } \end{array} \right., \text { for   } i, j = 1, 2,..., n, (k = 1, 2)  .
$$

We take an example of ${ \mathrm { B S M } } _ { 2 }$ and observe the distribution of 0s and 1s.

Example 5. With reference to Example 4, the ${ \mathrm { B S M } } _ { 2 }$ at similarity level 0.353 is given below.

$$
\mathrm{BSM} _ {2} (D, 0. 3 5, 0. 3 5 3) = \left[ \begin{array}{c c c c c c c} 1 & 1 & 1 & 0 & 0 & 0 & 0 \\ 1 & 1 & 1 & 0 & 0 & 0 & 0 \\ 1 & 1 & 1 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 1 & 1 & 1 \\ 0 & 0 & 0 & 0 & 1 & 1 & 1 \\ 0 & 0 & 0 & 0 & 1 & 1 & 1 \end{array} \right], \text { where } D = \{D _ {1}, D _ {2}, \dots D _ {7} \}.
$$

There may exist two same partitions at two distinct similarity levels. Two partitions are distinct if they are not the same. In the following, we define two same partitions at two distinct similarity levels

Definition 13. Let D be a set of databases. Let $C \subseteq D .$ , and $C \neq \phi$ . Two partitions $\pi _ { k } ^ { \delta 1 } ( D , \alpha )$ and $\pi _ { k } ^ { \delta 2 } ( D , \alpha )$ are the same, if the following statement is true: $C \in \pi _ { k } ^ { \delta 1 }$ if and only if $C \dot { \in } \pi _ { k } ^ { \ \delta 2 }$ , for $\delta _ { 1 } \neq \delta _ { 2 }$ □

We would like to enumerate the maximum number of possible distinct partitions. In Theorem 5, we find the maximum number of possible distinct partitions of a set of databases.

Theorem 5. Let D be a set of databases. Let m be the number of distinct non-zero similarity values in the upper triangle of DSM<sub>2</sub>. Then the number of distinct partitions is less than or equal to m.

Proof. We arrange the non-zero similarity values of the upper triangle of $\mathrm { D S M } _ { 2 }$ in non-increasing order. Let $\delta _ { 1 }$ , $\delta _ { 2 } , . . . , \delta _ { m }$ be m non-zero ordered similarity values. Let $\delta _ { i } , \delta _ { i + 1 }$ be two consecutive similarity values in the sequence of non-increasing similarity values. Let $x , y \in [ \delta _ { i } , \delta _ { i + 1 } )$ , for some $i { = } 1 , 2 , . . . , m ,$ , where $\delta _ { m { \mathrm { ~ + ~ } } 1 } = 0$ . Then $\mathrm { B S M } _ { 2 } ( D , \alpha , x ) { = } \mathrm { B S M } _ { 2 } ( D , \alpha , y )$ . Thus, there exists at the most one distinct non-trivial partition in the interval $[ \delta _ { i } ,$ $\delta _ { i { \mathrm { ~ + ~ } } 1 } )$ , for $i = 1 , \ 2 , . . . ,$ m. We have m such semi-closed interval $[ \delta _ { i } , \delta _ { i { \mathrm { ~ + ~ } } 1 } )$ , for $i { = } 1 , 2 , . . . , m$ . The theorem follows. □

For the purpose of finding partitions of the input databases, we shall first design a simple algorithm that uses apriori property [2]. The similarity values considered here are based on simi . Initially, we have n database classes, where n is the number of databases. At this time, each class contains a single database object. These classes are assumed at level 1. Based on the classes at level 1, we construct database classes at level 2. At level 1, we assume that the i-th class contains database $D _ { i } ,$ for $i { = } 1 , 2 , . . . , n .$ i-th class and j-th class of level 1 could be merged if $\sin \mathrm { i } _ { 2 } ( D _ { i } , \ D _ { j } ) \geq \delta ,$ , where δ is the user defined level of similarity. We proceed further until no more classes could be generated and no more levels could be generated. The algorithm is presented below.

Algorithm 1. Partitions (if they exist) of a set of databases using apriori property.

```csv
procedure AprioriDatabaseClustering (n, DSM₂)
Input: n, DSM₂
n: number of databases, DSM₂: database similarity matrix
Output: Partitions (if they exist) of input databases
01: sort all the non-zero values that exist in the upper triangle of DSM₂ in non-increasing order into an
02: array called simValues; let the number of non-zero values be m;
03: let k = 1; let simValues(m+1) = 0; let delta = simValues(k);
04: while (delta > 0) do
05: construct n classes, where each class contains a single database; // level: 1
06: repeat line 7 until no more level could be generated;
07: construct all possible classes at level (i + 1) using lines 8-10; // level: i + 1
08: let A and B be two classes at the i-th level such that |A ∩ B| = i - 1;
09: let a ∈ (A-B), and b ∈ (B-A);
10: if DSM₂ᵃᵇ ≥ δ then construct a new class A ∪ B; end if
11: repeat line 12 from top level to level 1;
12: for each class at the current level do
13: if all databases of the current class are not included a class generated earlier then
14: generate the current class;
15: end if
16: end for
17: if the current clustering is a partition then store it; end if
18: increase k by 1; let delta = simValues(k);
19: end while
20: display all the partitions;
end procedure
```

Lines 1–2 take $O ( m \times \log ( m ) )$ time to sort m data. While-loop at line 4 executes m times. Line 5 takes $O ( n )$ time. Initially (at line 5), n classes are constructed. At the first iteration of line $^ { 6 , }$ the maximum number of classes generated is $^ n C _ { 2 } .$ . At the second iteration, the maximum number of classes generated is ${ } ^ { n } C _ { 3 }$ . Lastly, at the (n − 1)-th iteration, the maximum number of classes generated is $^ n C _ { n } .$ Thus, the maximum number of possible classes is $O ( \sum _ { i } \mathbf { \Pi } _ { = } ^ { n } \mathbf { \Pi } _ { 1 } \mathbf { \Pi } ^ { n } C _ { i } )$ , i.e., $O ( 2 ^ { n } )$ . Let $p$ be the average size of a class. Line 8 takes $O ( p )$ time. $\mathrm { A l s o } ,$ line 11 takes $O ( 2 ^ { n } )$ time, since the maximum number of possible classes is $O ( 2 ^ { n } )$ . Thus, the time complexity of lines 4–19 is $O ( m \times p \times 2 ^ { n } )$ . The line 20 takes time $O ( m \times n )$ , since the maximum number of partitions is m. Thus, the time complexity of the procedure AprioriDatabaseClustering is maximum $\{ O ( m \times \log ( m )$ $O ( m \times p \times 2 ^ { n } )$ $O ( m \times n ) _ { \ l } ^ { \ l }$ , i.e., $O ( m \times p \times 2 ^ { n } )$ , since $p \times 2 ^ { n } { > } 2 ^ { n } { > } n ^ { 2 } { > } m { > } \log _ { 2 } ( m )$ , for $p > 1$ and $n { > } 4$ The AprioriDatabaseClustering algorithm generates all possible classes level-wise. It is a simple but not an efficient clustering technique, since the time-complexity of the algorithm is an exponential function of $n .$ In Theorems 6, 7, 8, and 9, we discuss some properties of ${ \mathrm { B S M } } _ { 2 }$

Theorem 6. Let $D = \{ D _ { I } , ~ D _ { 2 } , . . . , ~ D _ { n } \} .$ . Let $\pi _ { 2 } ^ { \delta } \langle D ,$ , α) be a clustering of databases in D at the similarity level δ. $\pi _ { 2 } ^ { \delta }$ is a partition if and only if the corresponding $B S M _ { 2 }$ gets transformed into the following form by inter-changing jointly a row and the corresponding column with another row and the corresponding column.

$$
\left[ \begin{array}{c c c c} U _ {1} & 0 & ... & 0 \\ 0 & U _ {2} & ... & 0 \\ ... & ... & ... & ... \\ 0 & 0 & ... & U _ {m} \end{array} \right], U _ {i} \text { is a matrix of size n_{i} \times n_{i}, containing all elements as 1, \sum_{i = 1} ^{m} n_{i} = n, |\pi_{2}^{\delta}| = m.}
$$

Proof. Let $\{ D _ { 1 } ^ { i } , D _ { 2 } ^ { i } , . . . , D _ { n _ { i } } ^ { i } \}$ be the i-th database class of the partition at the similarity level $\delta ,$ for $i { = } 1 , 2 , . . . , m$ . The row corresponding to $D _ { j } ^ { i }$ of $B S M _ { 2 }$ corresponds to a unique combination of 0s and ${ 1 \mathrm { s } , \mathrm { f o r } j \mathrm { = } 1 , 2 . . . , n _ { i } } .$ . Similarly, the column corresponding to $D _ { j } ^ { i } o f B S M _ { 2 }$ corresponds to a unique combination of 0s and 1s, for $j = 1 , 2 , . . . , n _ { i } .$ . All such $n _ { i }$ rows and columns may not be consecutive initially, for $i { = } 1 , 2 , . . . , m$ . We shall keep these $n _ { i }$ rows and columns consecutive, for $i { = } 1 , 2 , . . . , m$ . Initially, we keep $n _ { 1 }$ rows and the corresponding columns of the first database class consecutively. Then, we keep $n _ { 2 }$ rows and the corresponding columns of the second database class consecutively, and so on. In general, to fix the matrix $U _ { i }$ at the proper position, we interchange jointly $\left( \sum _ { l } ^ { i - 1 } n _ { j } + k \right)$ -th row and $\left( \sum _ { l } ^ { i - 1 } n _ { j } + k \right)$ -th column with $D _ { k } ^ { i } \mathrm { \mathrm { - t h } }$ row and ${ D _ { k } } ^ { i } – \mathrm { t h }$ column of $\mathrm { B S M } _ { 2 } .$ , for $1 \leq \dot { k } \leq n _ { i } , i = ^ { \prime } 1 , 2 , . . . ,$ m. □

With reference to ${ \mathrm { B S M } } _ { 2 }$ in Example 5, we apply Theorem $^ { 6 , }$ and conclude that a partition exists at similarity level 0.353.

Theorem 7. Let D be a set of databases. $L e t \pi _ { 2 } ^ { \delta } ( D ,$ α) be a clustering of databases in D at the similarity level δ. Let $\langle J _ { l } ^ { i } ,$ $D _ { 2 } ^ { i } . . . , D _ { n i } ^ { i } \}$ be the i-th database class $o f \pi _ { 2 } ^ { \delta } ( D , \alpha )$ . Then D<sup>i</sup>-th row (or, D<sup>i</sup>-th column) of BSM contains $n _ { i } I s , f o r k = 1 , 2 ,$ $\ldots , n _ { i } , i = I , 2 , \ldots , | \pi _ { 2 } ^ { \delta } |$

Proof. If possible, let $D _ { k } ^ { i } \mathrm { - t h }$ row or, ${ D _ { k } } ^ { i } – \mathrm { t h }$ column has $\left( n _ { i } + 1 \right)$ 1s. Then $D _ { k } ^ { i } { \mathrm { - t h } }$ database would belong to two database classes. It contradicts mutually exclusiveness of classes of a partition. If possible, let $D _ { k } ^ { i } { \mathrm { - t h } }$ row $\mathrm { o r , ~ } D _ { k } ^ { \ i } { \cdot } \mathrm { t h }$ column contains $( n _ { i } - 1 )$ 1s. It contradicts the fact that $\mathrm { B } \mathrm { \dot { S } M } _ { 2 j } ^ { D i , D } { } _ { k } ^ { i } = 1$ , for $j { = } 1 , 2 , . . . , n _ { i } ,$ $j \neq \mathbf { k }$ □

Theorem 8. Let D be a set of databases. $L e t \pi _ { 2 } ^ { \delta } ( D , \alpha )$ be a clustering of databases in D at the similarity level δ. Then, the rank of the corresponding $B S M _ { 2 } \ i s \ | \pi _ { 2 } ^ { \delta } |$

Proof. Let $\{ D _ { 1 } ^ { i } , D _ { 2 } ^ { i } , . . . , D _ { n i } ^ { i } \}$ be the i-th database class of $\pi _ { 2 } ^ { \delta }$ . Then,

$$
\operatorname{BSM} _ {2} ^ {D _ {j} ^ {i}, D _ {k} ^ {i}} (D, \alpha) = \left\{ \begin{array}{l} 1, \text {   for   } D _ {j} ^ {i}, D _ {k} ^ {i} \in \left\{D _ {l} ^ {i}, D _ {2} ^ {i}, \ldots , D _ {n _ {i}} ^ {i} \right\} \\ 0, \text {   for   } D _ {j} ^ {i} \in \left\{D _ {l} ^ {i}, D _ {2} ^ {i}, \ldots D _ {n _ {i}} ^ {i} \right\} \text {   and   } D _ {k} ^ {i} \notin \left\{D _ {l} ^ {i}, D _ {2} ^ {i}, \ldots D _ {n _ {i}} ^ {i} \right\} \\ 0, \text {   for   } D _ {j} ^ {i} \notin \left\{D _ {l} ^ {i}, D _ {2} ^ {i}, \ldots D _ {n _ {i}} ^ {i} \right\} \text {   and   } D _ {k} ^ {i} \in \left\{D _ {l} ^ {i}, D _ {2} ^ {i}, \ldots D _ {n _ {i}} ^ {i} \right\} \end{array} \right.
$$

The row corresponding to $D _ { j } ^ { i }$ of ${ \mathrm { B S M } } _ { 2 }$ corresponds to a unique combination of 0s and 1s, for $\cdot j { = 1 , 2 , . . . , n _ { i } . \mathrm { S } } 0 .$ , all the rows of ${ \mathrm { \ B S M } } _ { 2 }$ are divided into $| \pi _ { 2 } ^ { \delta } |$ groups such that all the rows in a group correspond to a unique combination of 0s and 1s. Thus, ${ \mathrm { B S M } } _ { 2 }$ has $| \pi _ { 2 } ^ { \delta } |$ independent rows. □

Theorem 9. Let $D = \{ D _ { I } , D _ { 2 } , . . . , D _ { n } \} .$ . At a given value of the triplet $( D , \alpha , \delta )$ , there exists at the most one partition of D.

Proof. At a given value of the pair $( D , \alpha )$ , the element $\mathrm { D S M } _ { 2 } ^ { i , j }$ is unique, for $i , j { = } 1 , 2 , . . . , n .$ . Thus, at a given value of the tuple $( D , \ \alpha , \delta )$ the element $\mathrm { B S M } _ { 2 } ^ { i , j }$ is unique, for $i , j { = } 1 , 2 , . . . , n$ . There exists a partition if the ${ \mathrm { B S M } } _ { 2 }$ gets transformed into a specific form [Theorem 6], by inter-changing jointly a row and the corresponding column with another row and the corresponding column. Hence, the theorem follows. □

## 4.1. Finding the best non-trivial partition

We return back to the Example 4. We observe that at different similarity levels there may exist different partitions. We have observed the existence of four non-trivial partitions. We would like to find the best partition among these partitions. The best partition is based on the principle of maximizing the intra-class similarity and maximizing the inter-class distance. The intra-class similarity and inter-class distance are defined as follows.

Definition 14. The intra-class similarity intra-sim of a partition π at the similarity level δ using the similarity measure simi is defined as follows:

$$
\text { intra } - \text { sim } \left(\pi_ {2} ^ {\delta}\right) = \sum_ {C \in \pi_ {2} ^ {\delta}} \sum_ {D _ {i}, D _ {j} \in C; i <   j} \text { simi } _ {2} \left(D _ {i}, D _ {j}, \alpha\right).
$$

Definition 15. The inter-class distance inter-dist of a partition π at the similarity level δ using the similarity measure simi is defined as follows:

$$
\operatorname{inter} - \operatorname{dist} \left(\pi_ {2} ^ {\delta}\right) = \sum_ {C _ {p}, C _ {q} \in \pi_ {2} ^ {\delta}; p <   q} \sum_ {D _ {i} \in C _ {p}; D _ {j} \in C _ {q}; i <   j} \operatorname{dist} _ {2} \left(D _ {i}, D _ {j}, \alpha\right).
$$

The best partition among a set of partitions is selected on the basis of goodness value of a partition. The goodness measure goodness of a partition is defined as follows.

Definition 16. The goodness of a partition π at similarity level δ using the similarity measure simi is defined as follows: goodness(π<sup>δ</sup>) = intra-sim(π<sup>δ</sup>) + inter-dist $( \pi _ { 2 } ^ { \delta } ) - | \pi _ { 2 } ^ { \delta } |$ , where $| \pi _ { 2 } ^ { \delta } |$ is the number classes in π. □

We have subtracted $| \pi _ { 2 } ^ { \delta } |$ from the sum of intra-class similarity and inter-class distance to remove the bias of goodness value of a partition. Higher the value of goodness, better is the partition. Now, we would like to partition the set of databases D using the proposed goodness measure.

Example 6. With reference to Example 4, we would like to calculate the goodness value of each of the non-trivial partitions using simi .

$$
\text { intra } - \operatorname{sim} \left(\pi_ {2} ^ {0. 3 5 3}\right) = 3. 1 8 5, \text {   inter   } - \operatorname{dist} \left(\pi_ {2} ^ {0. 3 5 3}\right) = 1 5. 7 2 6, | \pi_ {2} ^ {0. 3 5 3} | = 3, \text {   goodness } \left(\pi_ {2} ^ {0. 3 5 3}\right) = 1 5. 4 6 1.
$$

$$
\text { intra } - \text { sim } (\pi_ {2} ^ {0. 5 3 9}) = 2. 5 9 6, \text { inter } - \text { dist } (\pi_ {2} ^ {0. 5 3 9}) = 1 6. 6 6 6, | \pi_ {2} ^ {0. 5 3 9} | = 4, \text { goodness } (\pi_ {2} ^ {0. 5 3 9}) = 1 5. 2 6 2.
$$

$$
\text { intra } - \text { sim } (\pi_ {2} ^ {0. 6 4 1}) = 1. 4 2 1, \text { inter } - \text { dist } (\pi_ {2} ^ {0. 6 4 1}) = 1 7. 4 9 1, | \pi_ {2} ^ {0. 6 4 1} | = 5, \text { goodness } (\pi_ {2} ^ {0. 6 4 1}) = 1 3. 9 1 2.
$$

$$
\text { intra } - \operatorname{sim} \left(\pi_ {2} ^ {0. 7 8 0}\right) = 0. 7 8 0, \text { inter } - \operatorname{dist} \left(\pi_ {2} ^ {0. 7 8 0}\right) = 1 7. 1 1 8, | \pi_ {2} ^ {0. 7 8 0} | = 6, \text { goodness } \left(\pi_ {2} ^ {0. 7 8 0}\right) = 1 1. 8 9 8.
$$

The goodness value corresponding to the partition $\pi _ { 2 } ^ { 0 . 3 5 3 }$ is the maximum. Thus, the partition $\pi _ { 2 } ^ { 0 . 3 5 3 } = \{ \{ D _ { 1 } , D _ { 2 } , $ $D _ { 3 } \} , \ \{ D _ { 4 } \} , \ \{ D _ { 5 } , D _ { 6 } , D _ { 7 } \} \}$ is the best among all the non-trivial partitions. Let us look back into the databases of Example 2. We find that the partition $\pi _ { 2 } ^ { 0 . 3 5 3 }$ matches the ground reality the best among the partitions reported. □

We shall now present an algorithm for finding the best non-trivial partition of a set of databases.

Algorithm 2. Best non-trivial partition (if it exists) of a set of databases.

```txt
procedure BestDatabasePartition (n, DSM₂)
Input: n, DSM₂
n: number of databases, DSM₂: database similarity matrix
Output: The best partition (if it exists) of input databases
01: sort all the non-zero values that exist in the upper triangle of DSM₂ in non-increasing order into an
02: array called simValues; let the number of non-zero values be m;
03: let k = 1; let simValues(m + 1) = 0; let delta = simValues(k);
04: while (delta > 0) do
05:    for i = 1 to n do class(i) = 0; end for
06:    construct the BSM₂ at current level of the similarity delta;
07:    let currentClass = 1; let currentRow = 1; let class(1) = currentClass;
08:    for col = (currentRow + 1) to n do
09:    if (BSM₂ currentRow, col = 1) then
10:    if (class(col) = 0) then class(col) = currentClass;
11:    else if (class(col) ≠ currentClass) then go to line 24; end if
12:    end if
13:    end if
14:    end for
15:    let i = 1; let class(n + 1) = 0;
16:    while (class(i) ≠ 0) do increase i by 1; end while
17:    if (i = n + 1) then
18:    store the content of array class and current similarity level delta;
19:    else
20:    increase currentRow by 1;
21:    if (class(currentRow) = 0) then increase currentClass by 1; end if
22:    go to line 8;
23:    end if
24:    increase k by 1; let delta = simValues(k);
25: end while
26: for each non-trivial partition do
27:    calculate the goodness value of the current partition;
28: end for
29: return the partition whose goodness value is the maximum;
end procedure
```

We have sorted all non-zero values in the upper triangle DSM2 in non-increasing order at step 1. Thus, the algorithm checks the existence of a partition starting with the maximum of all the similarity values. At line 5 we initialize the class label of each database to 0. The algorithm starts forming a class with $D _ { 1 }$ (first database) as the variable currentRow is initialized with 1. Also, class label starts with 1 as the variable currentClass is initialized with 1. Lines 8– 14 are used to check the similarity of $D _ { \mathrm { c u r r e n t R o w } }$ with other databases. If the condition at line 9 is true then databases $D _ { \mathrm { c u r r e n t R o w } }$ and $D _ { \mathrm { c o l } }$ are similar. At line $1 0 , D _ { \mathrm { c o l } }$ is put in the currentClass if it is still unlabelled. If $D _ { \mathrm { c o l } }$ is already labelled with a class label not equal to current class label then $D _ { \mathrm { c o l } }$ get another label. Thus, partition does not exist at the current similarity level. Some useful explanations of the algorithm are given in Theorem 10.

Line 1 takes $O ( m \times \log ( m )$ time. Line 3 repeats for m times. Line 6 constructs ${ \mathrm { B S M } } _ { 2 }$ in $O ( n ^ { 2 } )$ time as the order of ${ \mathrm { B S M } } _ { 2 }$ is $n \times n$ . Each of lines 7 and 16 takes $O ( n )$ time. For-loop at line 8, repeats maximum n times. Line 18 takes O(n)

time, since the time required to store a partition is $O ( n )$ . Thus, the time complexity of lines 4–25 is $O ( m \times n ^ { 2 } )$ Therefore, the time complexity of the procedure best-database-partition is maximum $\{ O ( m \times \log ( m ) , \mathrm { O } ( m \times n ^ { 2 } ) \} , \mathrm { i . e . }$ $O ( m \times n ^ { 2 } )$ , since $n ^ { 2 } { > } m { > } \mathrm { l o g } _ { 2 } \dot { ( m ) }$ .

Our BestDatabasePartition algorithm performs better than the BestClassification algorithm [21]. BestClassification algorithm has the following drawbacks: (i) Step value of similarity level is user input. Thus, it fails to find the exact similarity level at which a partition exists. (ii) The algorithm BestClassification calls procedure GreedyClass [21] at different places. There is a mistake in the procedure GreedyClass. The following example shows that the procedure GreedyClass fails to construct the correct classes at a given level of similarity.

Example 7. A multi-branch company has 4 branch databases $D _ { 1 } , D _ { 2 } , D _ { 3 } ,$ , and $D _ { 4 } .$ . Let $D = \{ D _ { 1 } , D _ { 2 } , D _ { 3 } , D _ { 4 } \}$ , and $\alpha { = } 0 . 0 5$ . Assume that the corresponding $\mathrm { D S M } _ { 2 }$ has the following form.

$$
\mathrm{DSM} _ {2} (D, 0. 0 5) = \left[ \begin{array}{c c c c} 1. 0 & 0. 1 & 0. 1 & 0. 4 \\ 0. 1 & 1. 0 & 0. 1 & 0. 1 \\ 0. 1 & 0. 1 & 1. 0 & 0. 5 \\ 0. 4 & 0. 1 & 0. 5 & 1. 0 \end{array} \right]
$$

At the similarity level 0.3, we should get clustering as $\{ \{ D _ { 1 } , D _ { 4 } \} , \{ D _ { 2 } \} , \{ D _ { 3 } , D _ { 4 } \} \}$ . But, the GreedyClass procedure generates clustering as $\{ \{ D _ { 1 } , D _ { 4 } \} , \{ D _ { 2 } , D _ { 4 } \} , \{ D _ { 3 } , D _ { 4 } \} \}$ . The class $\{ D _ { 2 } , D _ { 4 } \}$ should not be formed, since simi $_ 2 ( D _ { 2 } , D _ { 4 } , 0 . 0 5 ) { < } 0 . 3$ □

The proposed BestDatabasePartition algorithm reports the exact similarity level at which a partition exists. Also, the algorithm works faster, since it is required to check for the existence of partitions only at m similarity levels. In Theorem 10, we prove that the proposed algorithm works correctly.

## Theorem 10. Algorithm BestDatabasePartition works correctly.

Proof. Let $D = \{ D _ { 1 } , D _ { 2 } , . . . , D _ { n } \}$ . Let there are m distinct non-zero similarity values in the upper triangle of DSM . Using Theorem $5 ,$ we could conclude that the maximum number of partitions of D is m at a given value of pair $( D , \alpha )$ While-loop at line 4 checks for the existence of partitions at m similarity levels. At each similarity level, we get a new ${ \mathrm { B S M } } _ { 2 }$ . The existence of a partition is determined from the ${ \mathrm { B S M } } _ { 2 }$ . We have an array ‘class’ that stores the class label given to each database under the current level of similarity. In a partition, each database has a unique class label. The existence of a partition is checked based on the principle that every database receives a unique class label. As soon as we find that a labeled database receives another class label, we conclude that a partition does not exist at the current level of similarity delta (at line 11). Initially, we put the class label 0 to all databases using line 5. Then, we start from the row 1 of ${ \mathrm { B S M } } _ { 2 }$ that corresponds to database $D _ { 1 }$ . Thus, $D _ { 1 }$ is in database class 1. If there is a 1 in the j-th column of ${ \mathrm { B S M } } _ { 2 } ,$ then we put class label of $D _ { j }$ as 1 using line 10. We find a database $D _ { i }$ that has not been clustered yet using lines $1 5 { - } 1 6$ . Then, we start at row i of ${ \mathrm { B S M } } _ { 2 }$ . If there is a 1 in the j-th column of row $i ,$ then we put database $D _ { j }$ in the current class. Thus, the algorithm BestDatabasePartition works correctly. □

## 4.2. Efficiency of clustering technique

The proposed clustering algorithm is based on the similarity measure simi . Also, the similarity measure simi is based on supports of the frequent itemsets in databases. If we vary the value of α then the number of frequent itemsets in a database varies. The accuracy of similarity between two databases increases as the number of frequent itemsets increases. Therefore, a clustering process would be more accurate at a smaller value of α. The frequent itemsets participate in the clustering process is limited by main memory. If we can store more frequent itemsets in main memory then $\mathrm { s i m i } _ { 2 }$ could determine similarity between two databases more accurately. Thus, the clustering process would be more accurate. This limitation begs a space efficient representation of the frequent itemsets in main memory. For this purpose, we propose a coding for representing frequent itemsets space efficiently. The coding allows more frequent itemsets to participate in determining the similarity between two databases.

Table 1  
Dataset characteristics

<table><tr><td>Dataset</td><td>N T</td><td>ALT</td><td>AFI</td><td>NI</td></tr><tr><td>T10I4D100K (T1)</td><td>1,00,000</td><td>11.102280</td><td>1276.124138</td><td>870</td></tr><tr><td>T40I10D100K (T4)</td><td>1,00,000</td><td>40.605070</td><td>4310.516985</td><td>942</td></tr><tr><td>BMS-Web-Wiew-1 (B1)</td><td>1,49,639</td><td>2.000000</td><td>155.711759</td><td>1922</td></tr></table>

## 4.2.1. Space efficient representation of frequent itemsets in different branch databases

In this technique, we represent each frequent itemset using a bit vector. Each frequent itemset has three components: database identification, frequent itemset, and support. Let the number of databases be n. Then, $2 ^ { p \ - 1 } < n \leq 2 ^ { p } .$ , for an integer $p .$ Then, $p$ bits are enough to represent a database. Let k be the number of digits after the decimal point to represent support. Support value 1.0 could be represented as 0.99999, for k = 5. If we represent the support s as an integer d containing of k digits then $s { = } d \times 1 0 ^ { - k }$ . The number digits required to represent a decimal number is obtained by Theorem 11.

Theorem 11. A p-digit decimal number can be represented by a $\lceil p \times l o g _ { 2 } I O \rceil$ -digit binary number.

Input database characteristics  
Table 2

<table><tr><td>DB</td><td>NT</td><td>ALT</td><td>AFI</td><td>NI</td></tr><tr><td> $T_{10}$ </td><td>10,000</td><td>11.05500</td><td>127.65589</td><td>866</td></tr><tr><td> $T_{11}$ </td><td>10,000</td><td>11.13330</td><td>128.41177</td><td>867</td></tr><tr><td> $T_{12}$ </td><td>10,000</td><td>11.06700</td><td>127.64706</td><td>867</td></tr><tr><td> $T_{13}$ </td><td>10,000</td><td>11.12260</td><td>128.43649</td><td>866</td></tr><tr><td> $T_{14}$ </td><td>10,000</td><td>11.13670</td><td>128.74798</td><td>865</td></tr><tr><td> $T_{15}$ </td><td>10,000</td><td>11.13910</td><td>128.62702</td><td>866</td></tr><tr><td> $T_{16}$ </td><td>10,000</td><td>11.10780</td><td>128.56250</td><td>864</td></tr><tr><td> $T_{17}$ </td><td>10,000</td><td>11.09840</td><td>128.45370</td><td>864</td></tr><tr><td> $T_{18}$ </td><td>10,000</td><td>11.08150</td><td>128.55568</td><td>862</td></tr><tr><td> $T_{19}$ </td><td>10,000</td><td>11.08140</td><td>128.10867</td><td>865</td></tr><tr><td> $T_{40}$ </td><td>10,000</td><td>40.56710</td><td>431.56489</td><td>940</td></tr><tr><td> $T_{41}$ </td><td>10,000</td><td>40.58240</td><td>432.18743</td><td>939</td></tr><tr><td> $T_{42}$ </td><td>10,000</td><td>40.63190</td><td>431.79490</td><td>941</td></tr><tr><td> $T_{43}$ </td><td>10,000</td><td>40.62690</td><td>431.74176</td><td>941</td></tr><tr><td> $T_{44}$ </td><td>10,000</td><td>40.66110</td><td>432.56489</td><td>940</td></tr><tr><td> $T_{45}$ </td><td>10,000</td><td>40.50630</td><td>430.46015</td><td>941</td></tr><tr><td> $T_{46}$ </td><td>10,000</td><td>40.74350</td><td>433.44149</td><td>940</td></tr><tr><td> $T_{47}$ </td><td>10,000</td><td>40.62380</td><td>431.70882</td><td>941</td></tr><tr><td> $T_{48}$ </td><td>10,000</td><td>40.52810</td><td>431.15000</td><td>940</td></tr><tr><td> $T_{49}$ </td><td>10,000</td><td>40.57960</td><td>432.15761</td><td>939</td></tr><tr><td> $B_{10}$ </td><td>14,000</td><td>2.0000</td><td>14.94130</td><td>1874</td></tr><tr><td> $B_{11}$ </td><td>14,000</td><td>2.0000</td><td>280.00000</td><td>100</td></tr><tr><td> $B_{12}$ </td><td>14,000</td><td>2.0000</td><td>280.00000</td><td>100</td></tr><tr><td> $B_{13}$ </td><td>14,000</td><td>2.0000</td><td>280.00000</td><td>100</td></tr><tr><td> $B_{14}$ </td><td>14,000</td><td>2.0000</td><td>280.00000</td><td>100</td></tr><tr><td> $B_{15}$ </td><td>14,000</td><td>2.0000</td><td>280.00000</td><td>100</td></tr><tr><td> $B_{16}$ </td><td>14,000</td><td>2.0000</td><td>280.00000</td><td>100</td></tr><tr><td> $B_{17}$ </td><td>14,000</td><td>2.0000</td><td>280.00000</td><td>100</td></tr><tr><td> $B_{18}$ </td><td>14,000</td><td>2.0000</td><td>280.00000</td><td>100</td></tr><tr><td> $B_{19}$ </td><td>23,639</td><td>2.0000</td><td>472.78000</td><td>100</td></tr></table>

Table 3  
Partitions of the input databases at a given value of α

<table><tr><td>Databases</td><td> $\alpha$ </td><td>Non-trivial distinct partition ( $\pi$ )</td><td> $\delta$ </td><td>goodness ( $\pi$ )</td></tr><tr><td> $\{T_{10},..., T_{19}\}$ </td><td>0.03</td><td> $\{ \{T_{10}\},\{T_{11}\},\{T_{12}\},\{T_{13}\},\{T_{14},T_{18}\},\{T_{15}\},\{T_{16}\},\{T_{17}\},\{T_{19}\} \}$ </td><td>0.880798</td><td>0.011031</td></tr><tr><td rowspan="3"> $\{T_{40},..., T_{49}\}$ </td><td rowspan="3">0.1</td><td> $\{ \{T_{40}\},\{T_{41},T_{45}\},\{T_{42}\},\{T_{43}\},\{T_{44}\},\{T_{46}\},\{T_{47}\},\{T_{48}\},\{T_{49}\} \}$ </td><td>0.949743</td><td>-3.977703</td></tr><tr><td> $\{ \{T_{40}\},\{T_{41},T_{45}\},\{T_{42}\},\{T_{43}\},\{T_{44}\},\{T_{46}\},\{T_{47}\},\{T_{48},T_{49}\} \}$ </td><td>0.943098</td><td>11.716271</td></tr><tr><td> $\{ \{T_{40}\},\{T_{41},T_{43},T_{45}\},\{T_{42}\},\{T_{44}\},\{T_{46}\},\{T_{47}\},\{T_{48},T_{49}\} \}$ </td><td>0.942427</td><td>24.206474</td></tr><tr><td rowspan="5"> $\{B_{10},..., B_{19}\}$ </td><td rowspan="5">0.009</td><td> $\{ \{B_{10}\},\{B_{11}\},\{B_{12},B_{14}\},\{B_{13}\},\{B_{15}\},\{B_{16}\},\{B_{17}\},\{B_{18}\},\{B_{19}\} \}$ </td><td>0.726502</td><td>11.702650</td></tr><tr><td> $\{ \{B_{10}\},\{B_{11}\},\{B_{12},B_{14}\},\{B_{13}\},\{B_{15}\},\{B_{16},B_{19}\},\{B_{17}\},\{B_{18}\} \}$ </td><td>0.698836</td><td>27.694834</td></tr><tr><td> $\{ \{B_{10}\},\{B_{11}\},\{B_{12},B_{13},B_{14}\},\{B_{15}\},\{B_{16},B_{19}\},\{B_{17}\},\{B_{18}\} \}$ </td><td>0.684409</td><td>36.970604</td></tr><tr><td> $\{ \{B_{10}\},\{B_{11}\},\{B_{12},B_{13},B_{14},B_{15},B_{16},B_{19},B_{17},B_{18}\} \}$ </td><td>0.582443</td><td>55.984833</td></tr><tr><td> $\{ \{B_{10},B_{11}\},\{B_{12},B_{13},B_{14},B_{15},B_{16},B_{17},B_{18},B_{19}\} \}$ </td><td>0.535796</td><td>81.028792</td></tr></table>

Proof. Let t be the minimum number of binary digits required to represent a p-digit decimal number x. Then, $x < 1 0 ^ { p } < 2 ^ { t }$ . So, $t { > } p \times \log _ { 2 } 1 0 ,$ since $\log _ { k } ( y )$ is a monotonic increasing function of y for $k > 1$ . Thus, we find the minimum integer t for which $x { < } 2 ^ { t }$ is true as $\lceil p \times \log _ { 2 } 1 0 \rceil$ □

The proposed coding is described with the help of Example 8.

Example 8. We refer to Example 2. Sorted frequent itemsets in non-increasing order on the number of extractions are given as follows: $( h , 4 ) , ( a , 3 ) , ( a c , 3 ) , ( c , 3 ) , ( h i , 3 ) , ( i , 3 ) , ( a e , 2 ) , ( e , 2 ) , ( i j , 2 ) , ( a b , 1 ) , ( b , 1 ) , ( d , 1 ) , ( d f , 1 ) , ( e f , 1 ) , ( f , 1 )$ $( f h , 1 ) , ( g , 1 ) , ( g i , 1 ) , ( j , 1 ) . ( X , \mu )$ denotes itemset X having number of extractions μ. We code the frequent itemsets from left to right. The frequent itemsets are coded using a technique similar to Huffman coding [11]. We attach code 0 to itemset h, 1 to itemset a, 00 to itemset ac, 01 to itemset $c ,$ etc. Itemset h gets a code of minimal length, since it has been extracted maximum number of times. We call this coding as itemset (IS) coding. It is a lossless coding [17]. The proposed IS coding and the Huffman coding are not the same, in the sense that an IS code may be a prefix of another IS code. Coded itemsets are given as follows: (h, 0), (a, 1), (ac, 00), (c, 01), (hi, 10), (i, 11), (ae, 000), (e, 001), (ij, 010), (ab, 011), (b, 100), (d, 101), (df, 110), (ef, 111), (f, 0000), ( fh, 0001), (g, 0010), (gi, 0011), ( j, 0100). (X, ν) denotes itemset X having IS code ν. □

## 4.2.2. Efficiency of IS coding

Using the above representation of the frequent itemsets, we could store more frequent itemsets in the main memory during the clustering process. Thus, it enhances the efficiency of the clustering process.

Definition 17. Let there are n databases $D _ { 1 } , D _ { 2 } , . . . , D _ { n } .$ . Let $S ^ { T } ( \cup _ { i = 1 } ^ { n } \mathrm { F I S } ( D _ { i } ) )$ be the amount of storage space (in bits) required to represent $\cup _ { i = 1 } ^ { n } { \mathrm { F I S } } ( D _ { i } )$ by a technique T. Let $S _ { m i n } ( \bigcup _ { i = 1 } ^ { n } \mathrm { F I S } ( D _ { i } ) )$ be the minimum amount of storage space (in bits) required to represent $( \cup _ { i } ^ { n } { } = { } _ { 1 } \mathrm { F I S } ( D _ { i } )$ . Let τ, κ, and λ denote a clustering algorithm, similarity measure, and computing resource under consideration, respectively. Let Γ be the set of all frequent itemset representation techniques. We define efficiency of a frequent itemset representation technique T at a given value of triplet $( \tau , \kappa , \lambda )$ as follows.

$$
\varepsilon (T | \tau , \kappa , \lambda) = S _ {\min} \left(\cup_ {i = 1} ^ {n} \operatorname{FIS} \left(D _ {i}\right)\right) / S ^ {T} \left(\cup_ {i = 1} ^ {n} \operatorname{FIS} \left(D _ {i}\right)\right), \text {   for   } T \in \Gamma .
$$

One could store an itemset conveniently using the following components: database identification, items in the itemset, and support. Database identification, an item and a support could be stored as a short integer, an integer and a real type data respectively. A typical compiler represents a short integer, an integer and a real number using 2 bytes, 4 bytes and 8 bytes respectively. Thus, a frequent itemset of size 2 could consume $( 2 + 2 \times 4 + 8 ) \times 8$ bits, i.e. 144 bits. An itemset representation may have an overhead of indexing frequent itemsets. Let OI(T) be the overhead of indexing for the frequent itemset representation technique T.

Theorem 12. IS coding stores a set of frequent itemsets 12. IS coding stores a set of frequent itemsets using minimum storage space, if OI(IS coding) ≤ OI(T), $T \in T .$

database identification, itemset, and support. Let the numberProof. A frequent itemset has three components, viz., database identification, itemset, and support. Let the number of databases be n. Then, $2 ^ { p \ - 1 } < n \leq 2 ^ { p }$ , for an integer p. We need minimum p bits to represent a database. The representation of database identification is independent of the corresponding frequent itemsets. If we keep k digits to store a support then $\lceil k \times \log _ { 2 } 1 0 \rceil$ binary digits are needed to represent a support [Theorem 11]. Thus, the representation of support becomes independent of the other components of the frequent itemset. Also, the sum of all IS codes is the minimum because of the way they are constructed. Thus, the space consumed by IS coding for representing a set of frequent itemsets is the minimum. □

Thus, the efficiency of a frequent itemset representation technique T could be expressed as follows:

$$
\varepsilon (T | \tau , \kappa , \lambda) = S ^ {\text { IS   coding }} \left(\cup_ {i = 1} ^ {n} \operatorname{FIS} \left(D _ {i}\right)\right) / S ^ {T} \left(\cup_ {i = 1} ^ {n} \operatorname{FIS} \left(D _ {i}\right)\right), \text {   provided   } \mathrm{OI(IScoding)} \leq \mathrm{OI} (T), \text {   for   } T \in \Gamma .\tag{15}
$$

If the condition in Eq. (15) is satisfied, then IS coding performs better than any other techniques. If the condition in Eq. (15) is not satisfied, then IS coding performs better than any other techniques in almost all cases. The following corollary is derived from Theorem 12.

Corollary 12.1. Efficiency of IS coding is maximum, ifCorollary 12.1. Efficiency of IS coding is maximum, if OI(IS coding) ${ \le } O I ( T )$ , for $T \in I .$ .

=1.0.Proof. <sup>e</sup>(IS coding $\mid \tau , \kappa , \lambda ) = 1 . 0 .$

IS coding maintains an index table to decode/search a frequent itemset. Index table contains frequent itemsets and their IS codes. In the following example, we compute the amount of space required to represent the frequent itemsets using an ordinary method and IS coding.

frequent itemsets. Among them, there are 20 itemsets of sizeExample 9. With reference to Example 8, there are 35 frequent itemsets. Among them, there are 20 itemsets of size 1 and 14 itemsets of size 2. Thus, an ordinary method could consume $1 1 2 \times 2 0 + 1 4 4 \times 1 5 \mathrm { b i t s , i . e . , 4 4 0 0 b i t s }$ . The amount of space required to represent frequent itemsets in seven databases using IS coding is $P { + } Q$ bits, where $P$ is the amount of space required to store frequent itemsets, and Q is the amount of space required to maintain the index table. Since there are seven databases, we need 3 bits to identify a database. The amount of memory required to represent the database identification for 35 frequent itemsets is $3 5 \times 3 6 \mathrm { { i t s } = 1 0 5 \mathrm { { b i t s } } }$ . Suppose we keep 5 digits after the decimal point for a support. Thus, $\left\lceil 5 \times \log _ { 2 } ( 1 0 ) \right\rceil$ bits, i.e., 17bits are required to represent a support. The amount of memory required to represent the supports of 35 frequent itemsets is $3 5 \times 1 7 \mathrm { b i t s } = 5 9 5 \mathrm { b i t s }$ . Let the number of items be $1 0 { , } 0 0 0$ . Therefore, 14bits are required to identify an item. The amount of storage space would require for itemsets $^ { \ast } h ^ { \ast }$ and $\cdot _ { a c ^ { \prime } }$ are 14 bits and 28 bits respectively. To represent 35 frequent itemsets, we need $2 0 \times 1 4 + 1 5 \times 2 8 \mathrm { { b i t s } = 7 0 0 \mathrm { { b i t s } } }$ . Thus, $P { = } ( 1 0 5 { + } 5 9 5 { + } 7 0 0 ) \ \mathrm { b i t s } { = } 1 4 0 0 \mathrm { b i t s } .$ There are 19 frequent itemsets in the index table. Using IS coding, 19 frequent itemsets consume 54bits. To represent 19 frequent itemsets, we need $1 4 \times 1 0 + 2 8 \times 9 6 { \mathrm { i t s } } = 3 9 2 { \mathrm { b i t s } }$ . Thus, $Q { = } 3 9 2 + 5 4 { = } 4 4 6 { \mathrm { b i t s } }$ . The total amount of memory space required (including the overhead of indexing) to represent frequent itemsets in 7 databases using IS coding is $\mathrm { P } { + } \mathrm { Q }$ bits = 1846bits. The amount of space saving in compared to an ordinary method is equal to 2554bits, i.e., 58% approximately. A technique without optimization (TWO) may not maintain index table separately. In this case, OI (TWO) = 0. In spite of that, IS coding performs better than a TWO. □

Finally, we claim that our clustering technique is more accurate. There are two reasons for this claim: (i) We propose better measures of similarity than the existing measures. Thus, the similarity between two databases is estimated more accurately. (ii) Also, our proposed IS coding enable us to mine local databases further at a lower level of <sup>a</sup> to accommodate more frequent itemsets in main memory. As a result, more frequent itemsets could participate in the clustering process.

## 5. Experiments

We have carried out several experiments to study the effectiveness of our approach. All the experiments have been implemented on a 1.6GHz Pentium processor with 256MB of memory, using visual $\mathrm { C } { + + }$ (version 6.0) software. We present experimental results using two synthetic datasets, and one real dataset. The synthetic datasets T10I4D100K [9] and T40I10D100K [9] have been generated using synthetic dataset generator from the IBM Almaden Quest research group. The real dataset BMS-Web-Wiew-1 [13] could be found from KDD CUP 2000. We present some characteristics of these datasets in Table 1. Let NT, ALT, AFI, NI and DB denote the number of transactions, the average length of a transaction, the average frequency of an item, the number of items and the database under consideration, respectively.

Table 5  
Table 4  
Best partitions of {T<sub>10</sub>, T<sub>11</sub>,…, T<sub>19</sub>}

<table><tr><td>α</td><td>Best partition (π)</td><td>δ</td><td>Goodness (π)</td></tr><tr><td>0.07</td><td> $\{ \{ T_{10},T_{13},T_{14},T_{16},T_{17}\},\{ T_{11}\},\{ T_{12}, T_{15}\},\{ T_{18},T_{19}\} \}$ </td><td>0.724778</td><td>85.585823</td></tr><tr><td>0.06</td><td> $\{ \{ T_{10},T_{11},T_{15},T_{16},T_{17},T_{18}\},\{ T_{12}\},\{ T_{13}, T_{14},T_{19}\} \}$ </td><td>0.732767</td><td>81.077277</td></tr><tr><td>0.05</td><td> $\{ \{ T_{10}\},\{ T_{11}\},\{ T_{12}\},\{ T_{13}\},\{ T_{14},T_{16}\},\{ T_{15}\},\{ T_{17},T_{19}\},\{ T_{18}\} \}$ </td><td>0.889875</td><td>13.345596</td></tr><tr><td>0.04</td><td> $\{ \{ T_{10}\},\{ T_{11},T_{13}\},\{ T_{12}\},\{ T_{14}\},\{ T_{15}\},\{ T_{16}\},\{ T_{17}\},\{ T_{18}\},\{ T_{19}\} \}$ </td><td>0.949766</td><td>-2.067990</td></tr><tr><td>0.03</td><td> $\{ \{ T_{10}\},\{ T_{11}\},\{ T_{12}\},\{ T_{13}\},\{ T_{14},T_{18}\},\{ T_{15}\},\{ T_{16}\},\{ T_{17}\},\{ T_{19}\} \}$ </td><td>0.880798</td><td>0.011031</td></tr></table>

Each of the above datasets is divided into 10 databases for the purpose of carrying out experiments. The databases obtained from T10I4D100K, and T40I10D100K are named as $T _ { 1 j } ,$ and $T _ { 4 j } ,$ respectively, for $j { = } 0 , 1 , . . . , 9 .$ . The databases obtained from BMS-Web-Wiew-1 are named as $B _ { 1 j } , \mathrm { f o r } j { = } 0 , \ 1 , . . . , 9$ . The databases $T _ { i j }$ and $B _ { 1 j }$ are called input databases, for i=1, 4, and $j { = } 0 , 1 , . . . , 9 .$ . Some characteristics of these input databases are presented in the Table 2.

At a given value of $\dot { \alpha } ,$ there may exist many partitions. Partitions of the set of input databases are presented in Table 3. If we vary the value of $\alpha ,$ the set of frequent itemsets in a database varies. Thus, the similarity between a pair of databases changes over the change of α.

Best partitions of $\{ \mathbf { B } _ { 1 0 } , \mathbf { B } _ { 1 1 } , . . . , \mathbf { B } _ { 1 9 } \}$

<table><tr><td> $\alpha$ </td><td>Best partition ( $\pi$ )</td><td> $\delta$ </td><td>Goodness ( $\pi$ )</td></tr><tr><td>0.020</td><td> $\{ \{ B_{10} \}, \{ B_{11}, B_{12}, B_{13}, B_{14}, B_{15}, B_{16}, B_{17}, B_{18}, B_{19} \} \}$ </td><td>0.667728</td><td>51.897608</td></tr><tr><td>0.017</td><td> $\{ \{ B_{10} \}, \{ B_{11}, B_{12}, B_{13}, B_{14}, B_{15}, B_{16}, B_{17}, B_{18}, B_{19} \} \}$ </td><td>0.664585</td><td>66.100075</td></tr><tr><td>0.014</td><td> $\{ \{ B_{10} \}, \{ B_{11}, B_{12}, B_{13}, B_{14}, B_{15}, B_{16}, B_{17}, B_{18}, B_{19} \} \}$ </td><td>0.581388</td><td>72.153178</td></tr><tr><td>0.010</td><td> $\{ \{ B_{10}, B_{11}, \}, \{ B_{12}, B_{13}, B_{14}, B_{15}, B_{16}, B_{17}, B_{18}, B_{19} \} \}$ </td><td>0.559567</td><td>63.671384</td></tr><tr><td>0.009</td><td> $\{ \{ B_{10}, B_{11}, \}, \{ B_{12}, B_{13}, B_{14} \}, \{ B_{15} \}, \{ B_{16}, B_{19} \}, \{ B_{17} \}, \{ B_{18} \} \}$ </td><td>0.535796</td><td>81.028792</td></tr></table>

![](/api/attachments/7ASEF4VR/fulltext/images/30556e487a5b5e15ef106b89a9b8798b5b71cc31896791250dda6c04ac446bdd.jpg)

Fig. 3. Execution time versus the number of databases.  
![](/api/attachments/7ASEF4VR/fulltext/images/5d2880115b42c9a7ee5913c62254c714508cdbe5f5695ba85dd6ad5ff93223f0.jpg)  
Fig. 4. Execution time versus α for experiment with {T10, T11,…, T19}.

At a smaller value of $\alpha ,$ more frequent itemsets are reported from a database. So, we get a more accurate value of similarity between a pair of databases. Thus, the partition generated at a smaller value of α would be more correct. In Tables 4 and 5, we have presented best partitions of a set of databases at different αs. So, the best partition of a set of databases may change over the change of α.

Thus, a partition may not remain the same over the change of α. But, we have observed a general characteristic that the databases show more similarity over a larger value of α. As the value of α becomes smaller, more frequent itemsets are reported from the databases, and they become more dissimilar.

In Fig. 3, we have shown how the execution time of an experiment increases as the number databases increases. The execution time increases faster as we increase input databases from dataset T1. The reason is that the size of each local database obtained from T1 is larger than that of T4 and B1.

The number of frequent itemsets decreases as the value of α increases. Thus, the execution time of an experiment decreases as α increases. We observe such phenomenon in Figs. 4 and 5.

![](/api/attachments/7ASEF4VR/fulltext/images/e3b35669ad0ddee58db61f33670ccd994ef0a099131b27861f35e01f12f9978f.jpg)  
Fig. 5. Execution time versus α for experiment with {B10, B11,…, B19}.

## 6. Conclusion

Clustering a set of databases is an important activity. It reduces cost of searching relevant information for many problems. We provide an efficient solution to this problem in three ways. Firstly, we propose more appropriate measures of similarity between two databases. Secondly, we need to find the existence of the best clustering only at few similarity levels. Thus, the proposed clustering algorithm executes faster. Lastly, we introduce IS coding for storing frequent itemsets in main memory. It allows more frequent itemsets to participate in the clustering process. IS coding enhances the accuracy of the clustering process. Thus, the proposed clustering technique is efficient in clustering a set of databases.

## Acknowledgements

The authors would like to thank the anonymous reviewers for their constructive comments on an earlier version of this paper.

The first author would like to thank State Government of Goa, India for having sponsored him on faculty improvement program with leave to take up full time research.

## References

[1] R. Agrawal, T. Imielinski, A. Swami, Mining association rules between sets of items in large databases, Proceedings of ACM SIGMOD Conference Management of Data, 1993, pp. 207–216.

[2] R. Agrawal, R. Srikant, Fast algorithms for mining association rules, Proceedings of the International Conference on Data Engineering, 1995, pp. 3–14.

[3] K. Ali, S. Manganaris, R. Srikant, Partial classification using association rules, Proceedings of the 3rd International Conference on Knowledge Discovery and Data Mining, 1997, pp. 115–118.

[4] B. Babcock, S. Chaudhury, G. Das, Dynamic sample selection for approximate query processing, Proceedings of ACM SIGMOD Conference Management of Data, 2003, pp. 539–550.

[5] R.G. Barte, The Elements of Real Analysis, 2nd ed. John Wiley & Sons, 1976.

[6] S.W.K. Chan, M.W.C. Chong, Unsupervised clustering for nontextual web document classification, Decision Support Systems 37 (3) (2004) 377–396.

[7] Y.-L. Chen, K. Tang, R.-J. Shen, Y.-H. Hu, Market basket analysis in a multiple store environment, Decision Support Systems 40 (2) (2005) 339–354.

[8] FIMI 2004, http://fimi.cs.helsinki.fi/src/.

[9] Frequent itemset mining dataset repository, http://fimi.cs.helsinki. fi/data.

[10] M.N.M. García, L.A.M. Quintales, F.J.G. Peñalvo, M.J.P. Martín, Building knowledge discovery-driven models for decision support in project management, Decision Support Systems 38 (2) (2004) 305–317.

[11] D.A. Huffman, A method for the construction of minimum redundancy codes, Proceedings of the IRE 40 (9) (1952) 1098–1101.

[12] A.K. Jain, M.N. Murty, P.J. Flynn, Data clustering: a review, ACM Computing Surveys 31 (3) (1999) 264–323.

[13] KDD CUP 2000, http://www.ecn.purdue.edu/KDDCUP.

[14] C.-H. Lee, C.-R. Lin, M.-S. Chen, Sliding-window filtering: an efficient algorithm for incremental mining, Proceedings of 10th International Conference on Information and Knowledge Management, 2001, pp. 263–270.

[15] C.L. Liu, Elements of Discrete Mathematics, 2nd ed.McGraw-Hill, 1985.

[16] H. Liu, H. Lu, J. Yao, Toward multi-database mining: Identifying relevant databases, IEEE Transactions on Knowledge and Data Engineering 13 (4) (2001) 541–553.

[17] K. Sayood, Introduction to Data Compression, 2nd ed.Morgan Kaufmann, 2000.

[18] K. Su, H. Huang, X. Wu, S. Zhang, A logical framework for identifying quality knowledge from different data sources, Decision Support Systems 42 (3) (2006) 1673–1683.

[19] P.-N. Tan, V. Kumar, J. Srivastava, Selecting the right interestingness measure for association patterns, Proceedings of SIGKDD Conference, 2002, pp. 32–41.

[20] X. Wu, Y. Wu, Y. Wang, Y. Li, Privacy-aware market basket data set generation: a feasible approach for inverse frequent set mining, Proceedings of SIAM International Conference on Data Mining, 2005, pp. 103–114.

[21] X. Wu, C. Zhang, S. Zhang, Database classification for multidatabase mining, Information Systems 30 (1) (2005) 71–88.

[22] X. Yin, J. Han, Efficient classification from multiple heterogeneous databases, Proceedings of 9th European Conference on Principles and Practice of Knowledge Discovery in Databases, 2005, pp. 404–416.

[23] T. Zhang, R. Ramakrishnan, M. Livny, BIRCH: A new data clustering algorithm and its applications, Data Mining and Knowledge Discovery 1 (2) (1997) 141–182.

[24] S. Zhang, C. Zhang, X. Wu, Knowledge Discovery in Multiple Databases, Springer, 2004.

[25] S. Zhang, X. Wu, C. Zhang, Multi-database mining, IEEE Computational Intelligence Bulletin 2 (1) (2003) 5–13.

![](/api/attachments/7ASEF4VR/fulltext/images/33a73699c892204f1feb51cfd6499e16254c026bf012a3bd15df9d5c72596177.jpg)

Animesh Adhikari is a lecturer in the Department of Computer Science, S P Chowgule College, Margao, Goa, India. He received Master of Computer Application degree in 1991 from Jadavpur University, Kolkata. He received Master of Technology in Computer Science degree in 1993 from Indian Statistical Institute, Kolkata. He is currently a full-time researcher in the Department of Computer Science and Technology, Goa University, Goa, India. He is now on a 2-year study leave

sponsored by the State Government of Goa, India. He has eight papers in different International Journals/International Conferences.

![](/api/attachments/7ASEF4VR/fulltext/images/9982d8f558cec59cce563c6a0dd4b976426575b18fff8221ecfc174472acd1a6.jpg)

Dr. P.R. Rao is a reader in the Department of Computer Science and Technology, Goa University, India. He received Ph.D. degree from Indian Institute of Technology, Mumbai, India. He has five Ph.D. students and six M Phil students. He has twenty six papers.
