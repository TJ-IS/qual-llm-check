---
otero_id: 396
otero_key: "UVFYD75F"
title: "CLAP: Collaborative pattern mining for distributed information systems"
authors: "Xingquan Zhu; Bin Li; Xindong Wu; Dan He; Chengqi Zhang"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.05.002"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# CLAP: Collaborative pattern mining for distributed information systems

Xingquan Zhu <sup>a,b,</sup>⁎, Bin Li <sup>a</sup>, Xindong Wu <sup>c,d</sup>, Dan He <sup>e</sup>, Chengqi Zhang

<sup>a</sup> QCIS Centre, Faculty of Eng. & Info. Technology, Univ. of Technology, Sydney, Ultimo 2007, Australia

<sup>b</sup> Dept. of Computer Science & Eng., Florida Atlantic University, Boca Raton, FL 33431, USA

<sup>c</sup> Dept. of Computer Science, University of Vermont, Burlington VT 05404, USA

<sup>d</sup> School of Computer Science and Information Engineering, Hefei University of Technology, Hefei 230009, China

<sup>e</sup> Dept. of Computer Science, Univ. of California at Los Angeles, Los Angeles, CA, 90095, USA

## a r t i c l e i n f o

Article history: Received 8 October 2010 Received in revised form 4 May 2011 Accepted 15 May 2011 Available online 27 May 2011

Keywords: Distributed data mining Distributed association rule mining Frequent item-sets Bloom filter

## a b s t r a c t

The purpose of data mining from distributed information systems is usually threefold: (1) identifying locally signi<sup>fi</sup>cant patterns in individual databases; (2) discovering emerging signi<sup>fi</sup>cant patterns after unifying distributed databases in a single view; and (3) <sup>fi</sup>nding patterns which follow special relationships across different data collections. While existing research has signi<sup>fi</sup>cantly advanced the techniques for mining local and global patterns (the <sup>fi</sup>rst two goals), very little attempt has been made to discover patterns across distributed databases (the third goal). Moreover, no framework currently exists to support the mining of all three types of patterns. This paper proposes solutions to discover patterns from distributed databases. More speci<sup>fi</sup>cally, we consider pattern mining as a query process where the purpose is to discover patterns from distributed databases with patterns relationships satisfying user speci<sup>fi</sup>ed query constraints. We argue that existing self-contained mining frameworks are neither ef<sup>fi</sup>cient, nor feasible to ful<sup>fi</sup>ll the objective, mainly because their pattern pruning is single-database oriented. To solve the problem, we advocate a cross-database pruning concept and propose a collaborative pattern (CLAP) mining framework with cross-database pruning mechanisms for distributed pattern mining. In CLAP, distributed databases collaboratively exchange pattern information between sites so that each site can leverage information from other sites to gain cross-database pruning. Experimental results show that CLAP <sup>fi</sup>ts a niche position, and demonstrate that CLAP not only outperforms its other peers with signi<sup>fi</sup>cant runtime performance gains, but also helps <sup>fi</sup>nd patterns incapable of being discovered by others.

Crown Copyright © 2011 Published by Elsevier B.V. All rights reserved.

## 1. Introduction

Many applications possess data collected from distributed sources [42,57]. Examples include market basket transaction data from different branches of a wholesale store, insurance claim data from different states, patient health records from different hospitals, census data of different states in one particular year, among many others. Even for one single database, the temporal or spatial relationships may also provide multiple views for the underlying data [11,21]. For example, transaction data [6] collected in a single wholesale store over different time periods can be regarded as multiple correlated databases. Census data of a certain state in different years [26], and patient records of one hospital from different time periods, can also form a collection of multiple databases. For years, knowledge discovery and data mining (also referred to as KDD) have demonstrated themselves to be an effective tool to search for novel and actionable patterns and relationships in the data [42]. Examples of patterns of interests include, but are not limited to, classi<sup>fi</sup>cation models (decision trees or statistical reasoning models) [3,19,45], clusters [14,18], and association rules [2,4,24,33].

From an association rule mining perspective, past research has made signi<sup>fi</sup>cant efforts to discover a variety of patterns, such as frequent item-sets, temporal, spatial, and/or sequential association rules, closed patterns or sequential patterns. Common challenges in this area are usually twofold: (1) identifying patterns from a single (large volume) database [55] or from data with continuous volumes [35,58] (referred to as local patterns or L-pattern mining in this paper); and (2) discovering new patterns by unifying multiple databases into a single view [4,57] (referred to as global or G-pattern mining in this paper). For distributed databases, a common goal is to discover G-patterns, which are trivial in local databases, but signi<sup>fi</sup>cant after multiple databases are uni<sup>fi</sup>ed into a single view. Collective data mining [31] represents the most typical research work in the area. A common practice is to act on local databases, and forward promising local candidates to a central place for synthesizing [12,50].

For distributed databases, G-patterns are important because they contain knowledge that is hard, if not impossible, to be realized by L-patterns [61]. In practice, there is a third type of pattern that may help discover data relationships across multiple distributed databases.

Take a wholesale store with three branches, A, B, and C as an example where a store manager was organizing data from these three branches for intelligent data analysis, he/she may easily raise concerns such as:

$\mathbf { Q _ { 1 } } \mathbf { : }$ What are the patterns frequent in A, B and $C ? ~ i . e . , ~ ( A \geq \alpha )$ & $\left( B \ge \alpha \right) \ \& \ \left( C \ge \alpha \right)$ , where α is the threshold in <sup>fi</sup>nding frequent patterns, and $A \geq \alpha$ means that a pattern's support value in database A should be no less than the value α.

$\mathbf { Q } _ { 2 } \mathbf { : }$ What are the frequent patterns which appear more often in A than in B, but infrequent in C? i.e., (ANB≥α) & (Cbβ)

$\mathbf { Q } _ { 3 } \mathbf { \dot { . } }$ What are the patterns whose support of differences in stores A and B are greater or equal to the value α? i.e., $\left| A - B \right| \geq \alpha .$

The above concerns lead to the problem of <sup>fi</sup>nding pattern relationships across a number of data collections. This problem is essentially different from local and global pattern mining mainly because users are interested in neither local signi<sup>fi</sup>cant patterns (i.e., L-patterns) nor global signi<sup>fi</sup>cant (i.e., G-patterns). In reality, when users are exposed to the data collected from multiple databases or multiple data sources,<sup>1</sup> it is natural to refer to a comparative study tool for knowledge and pattern discovery. In addition, it is often the case that users know some basic features of the data, such as the date and time each database was collected, or the region or entity each database may represent. What remains unclear is the relationship of the patterns hidden across the multiple data collections. For example, the store managers may want to <sup>fi</sup>nd customers' gradually increasing shopping patterns in a certain period of time, or a microbiologist may want to <sup>fi</sup>nd disease patterns along an evolving order. For these purposes, discovering pattern relationships across multiple databases (referred to as inter-pattern or I-pattern mining in this paper) can be a very important part of the KDD process.

The above observations motivate the necessity of <sup>fi</sup>nding Ipatterns from multiple databases, where patterns need to be discovered in individual databases and further compared across different data collections. Although this problem seems easy to solve by simply mining a “seed” database and then comparing patterns across all databases, in practice, I-pattern discovery is severely challenged by the following practical issues: (1) databases may be physically distributed so that intensive data transmission across sites should be avoided; (2) due to data privacy or other concerns, data aggregation for mining should be discouraged; and (3) in order to <sup>fi</sup>nd a pattern p's relationships across multiple databases, one has to scan each database to check p's frequencies with respect to each individual database. This database scanning process is heavily time-consuming if the number of patterns for comparison is large. In addition to the above three issues, if we consider L-, G-, and I-patterns as a whole, we have to face the challenge of devising a uni<sup>fi</sup>ed framework capable of <sup>fi</sup>nding all three types of patterns in distributed data environments. Under such circumstances, we believe that the major technique challenges are fourfold:

• System Framework: How to design a uni<sup>fi</sup>ed data mining framework capable of discovering all three types of patterns?

• Mining Procedures: How to transfer a user's mining query into actionable mining activities, so that the mining results from distributed sites can form legitimate answers?

• Data Transmission: What type of information should be exchanged between distributed sites? Also, how should the information be exchanged?

• Cross-database Pruning: How to carry out data mining activities by leveraging information from different sites? In other words, how to enable cross-database pattern pruning so that messages exchanged between sites can speed up the mining process?

This paper reports our recent progress in resolving the above problems, from both system and algorithm design perspectives. We consider pattern mining as a query process where the purpose is to discover patterns satisfying user speci<sup>fi</sup>ed constraints. To achieve distributed pattern mining, we propose a collaborative pattern mining (CLAP) framework with its own unique method to enable crossdatabase pruning.

The remainder of the paper is organized as follows. Section 2 reviews existing work in the literature. Section 3 formally de<sup>fi</sup>nes the problem and discusses pattern queries for mining. Section 4 provides an overview of the distributed pattern mining frameworks. Section 5 articulates technical details of the proposed CLAP mining framework. We report experimental results in Section 6, and conclude in Section 7.

## 2. Related work

Mining distributed databases [22,30,38]are a practical issue and a large amount of research work has signi<sup>fi</sup>cantly advanced the techniques for distributed classi<sup>fi</sup>cation [3,34,45], clustering [14,18], OLAP [11,21], frequent pattern mining [2,4,12,24], stream data mining [35,46], and database similarity assessments [32,49]. Presumably, nearly every major data mining research area has at least one distributed mining module or algorithm. The main themes of these research activities share striking similarities in the sense that they all intend to unify, and/or compare distributed data sources to achieve a common goal.

From clustering and classi<sup>fi</sup>cation perspectives, the pattern discovery from distributed databases problem arises of how to train global models by leveraging information from multiple databases. This can be achieved by either aggregating data into a single view or integrating models built from single databases [17,36]. Kargupta et. al. [31] proposed a collective data mining framework with a primary key to unify all data into a single view. Similar assumptions were also made for privacy preserving data mining [29,43], cluster ensembling [18], and kernel based model integration [17] for learning heterogeneous data. Yin et. al [53] previously proposed a CrossMiner for classi<sup>fi</sup>cation from multiple relational databases. Wang et. al. [48] addressed the problem of reinforcement clustering of multi-type inter-related objects (e.g. web documents). The problem of frequent pattern mining for distributed databases has also been well studied [1,4,12,23,31,33,37,44,50,54,55], where count distribution, data distribution, and candidate distribution are three basic mechanisms [31]. Along with all research activities, the focus has been primarily on mining large volume databases or continuous volume data streams (i.e., mining L-patterns), or unifying patterns discovered from single databases into new knowledge (i.e., mining G-patterns). Some system architectures also exist to discover frequent patterns from terabytescale data-sets running on cluster systems [9], by using compressed data structures (similar to FP-tree [24]) and succinct encoding methods. Such frameworks and solutions, however, typically limit their scope to the data volumes but have no mechanism to comparatively study multiple databases and discover their relationships at pattern levels.

In short, the de<sup>fi</sup>ciency of the existing work for distributed database mining is mainly threefold: (1) they lack general crossdatabase pruning mechanisms; (2) they have no effective message exchanging paradigm but mainly switch patterns in raw formats; and (3) they are not capable of mining all three types of patterns $( L \mathrm { - } , G \mathrm { - } ,$ and I-patterns). In comparison, this paper focuses on <sup>fi</sup>nding all types of patterns from distributed databases under a uni<sup>fi</sup>ed mining framework.

When data involve multiple (distributed/centralized) sources, one of the most important tasks is to assess the similarity between databases to discover structural information between databases for clustering [56] or classi<sup>fi</sup>cation [59]. Parthasarathy [39] and Li [32] have previously addressed the problem of database similarity assessment by comparing association rules from different databases, $e . g .$ the identical rules discovered by different databases and the numbers of instances covered by identical rules. The importance of <sup>fi</sup>nding differences between databases has been addressed by many researchers [5,15,49,52], and most methods focus on comparing a pair of databases one at a time. Webb et al. [49] proposed a rule based method to explore a contrast set between two databases. Xu et al. [51] proposed to discover comparative opinions between products from customer reviews. In [52], we proposed methods to evaluate the conceptual equivalence between two databases. Ji et al. [27] proposed methods to explore minimal distinguishing subsequence patterns between two data-sets, where the patterns take the form of “frequent in database A, but signi<sup>fi</sup>cantly less frequent in database $B " ,$ , i.e. $\{ ( A \ge \alpha ) \ \& \ ( B \le \beta ) \}$ . All these methods focus on <sup>fi</sup>nding differences (in terms of data items or patterns) between two data-sets, but they cannot support complex queries like the ones in the Introduction. Therefore, this type of work is a sub-set of our framework, and our goal is to address a broader area of problems in pattern discovery from distributed databases.

Research in database queries has made signi<sup>fi</sup>cant efforts in supporting data mining operations [8,28,47,60], with extensions of the database query languages to support mining tasks, but most research effort has focused on a single database with relatively simple query conditions. Two works are closely related to this research: (a) the complex mining optimization system proposed by Jin and Agrawal [28]; and (b) our recent work on relational pattern discovery across multiple databases [60]. In [28], Jin and Agrawal presented an SQLbased mechanism for mining frequent patterns across multiple databases, with the objective of optimizing users' queries to <sup>fi</sup>nd quali<sup>fi</sup>ed patterns. The essential difference between work in [28] and the proposed research is twofold: (1) the efforts in [28] only focus on enumerating query plans and choosing the one with the least cost. Instead of optimizing queries our research will propose a distributed data mining framework to support users' queries to <sup>fi</sup>nd broader types of patterns; (2) because of the limitations of their pattern mining framework (relying on each single database), the solution in [28] can only answer simple queries like $\{ ( S _ { i } \ge \alpha _ { 1 } ) ~ \& ~ ( S _ { j } \ge \alpha _ { 2 } ) ~ \& ~ ( S _ { k } \le \beta ) \}$ , i.e., each element of such a query must explicitly specify one single database and its corresponding threshold value. As a result, their methods cannot answer complex queries like Queries 2 and 3 in the Introduction, and therefore its applicability is limited; and (3) the methods in [28] are only applicable for centralized databases, whereas we intend to mine patterns from distributed databases. In [60], we have proposed a solution to discover relational patterns (e.g., Ipatterns) across multiple databases, which requires the aggregation of all databases at a central place, which is not feasible for distributed mining scenarios.

In short, although the distributed pattern mining problem has been extensively addressed in the literature, no framework is currently available for mining all three types $( L - , \ G - ,$ and I-) of patterns in distributed scenarios. As the major contribution of this work, we propose a distributed mining framework and a number of algorithms to resolve the key challenges, such as cross-database pruning for distributed mining.

## 3. Problem de<sup>fi</sup>nition & query decomposition

Given a number of distributed databases $D _ { i } , i { = } 1 , . . . , n ,$ each of which corresponds to an individual site $S _ { i } , i { = } 1 , { \ldots } , n ,$ , we assume that all distributed sites are able to compute and communicate with others, and a dedicated master site is provided for users to submit queries/constraints. The pattern discovery from distributed databases problem is <sup>fi</sup>nding patterns complying with the users' queries without aggregating data to a central place (e.g., the master site).

A pattern, P, discussed in this paper takes the form as an item-set, i.e. a set of items satisfying user queries/constraint(s). The support of a pattern P in a database $D _ { i } ,$ , represents the ratio between the number of times P appears in $D _ { i }$ and the total transactions in $D _ { i } .$

A user's query/constraint speci<sup>fi</sup>es the patterns he/she intend to discover. For example, a user can specify $\{ S _ { i } { \geq } \alpha \}$ to indicate that he/she intends to <sup>fi</sup>nd patterns from site $S _ { i }$ with all legitimate patterns' support larger than or equal to the threshold α. Assuming that X and Y denote two databases, we de<sup>fi</sup>ne the following two types of relationship factors and four operators to help users con<sup>fi</sup>ne their queries.

Relationship and set operators:

$X { \geq } \alpha \left( X { > } \alpha \right)$ indicates that a pattern's support value in X is no less than α (X is larger than α).

$X { \le } \alpha \left( X { < } \alpha \right)$ indicates that a pattern's support value in X is no larger than α (X is less than α)

• X Y indicates a virtual set which is the union of the transactions of X and Y.

Arithmetic operators:

$X + Y$ indicates the summation of the support in X and Y

• X −Y indicates the subtraction of the support in Y from the support in X

• X & Y indicates the operation of X and Y

• X | Y indicates the operation of X or Y

• |X| indicates the absolute support value in X.

A user's query is a combination of the above operators for <sup>fi</sup>nding patterns from distributed databases. More speci<sup>fi</sup>cally, a query should involve at least one database and one relationship operator, $e . g . , \{ S _ { i } \ge \alpha \}$ A query may also involve multiple relationship and arithmetic operators, which is often the case in reality. Following this process, the mining of the L-, G-, and I-patterns can be achieved by using different queries. For instance, the following examples list the queries for each type of pattern:

• L-pattern query examples: ${ \cal Q } = \{ S _ { i } \ge \alpha \} \mathrm { o r } { \cal Q } = \{ S _ { j } \ge \alpha \}$

• G-pattern query example: $Q = \{ ( S _ { i } \cup S _ { j } ) \geq \alpha \}$

• I-pattern query example: $Q = \{ S _ { i } \ge S _ { j } \ge \alpha \}$

Due to limitations of the pattern mining process, a user's query cannot take arbitrary forms, but has to involve at least one relationship operator $\geq \left( \mathrm { o r } > \right)$ with a numerical threshold value following this operator. For example $0 = \{ S _ { i } { \geq } S _ { j } { \geq } S _ { k } \}$ is not a valid query; whereas $0 = \{ S _ { i } \ge S _ { j } \ge S _ { k } \ge \alpha \}$ is. The reason we require a valid query is because without a threshold α, it is practically infeasible to <sup>fi</sup>nd all patterns satisfying $Q = \{ S _ { i } \ge S _ { j } \ge S _ { k } \}$

## 3.1. Query decomposition

A query decomposition process is needed for the following reasons: (1) from the data mining perspective, it is often the case that not all parts of the query comply with the down-closure property [2], i.e., any sub-set of a frequent item-set is also frequent. For example, the $" { \le } "$ and $" < "$ relationship operators normally do not comply with the down closure property. It is obvious that even if a pattern, say {abc}, in $S _ { i } ,$ does not satisfy $S _ { i } { \le } \beta ,$ its super-set, say {abcd}, may still comply with $S _ { i } { \le } \beta .$ Therefore, we must pre-process a user's query and explicitly decompose it into a set of sub-queries complying with the down closure property, so that the mining module can use these sub-queries for candidate pruning; and (2) from a distributed mining perspective, a site may be involved in only a sub-set of the query. Consequently, we need to decompose each user query into a number of sub-queries, each of which only involves necessary sites in the mining process. In this sub-section, we brie<sup>fl</sup>y list <sup>fi</sup>ve properties for query decomposition; other properties [60] are also available but omitted in the paper.

Property 1. Given a sub-query which contains a relationship operator $" \geq " 0 r \ " > " ,$ , if the sub-query has a single database and a threshold value α listed as the antecedent and the consequent of the operator $" \geq "$ or $^ { \ast } > ^ { \ast } ,$ respectively, this sub-query complies with the down closure property.

Proof. This property is based on the Apriori rule [2] in frequent itemset mining, which states that if a pattern $P \boldsymbol { s }$ support in a database is less than a given threshold $\alpha ,$ then any super-sets of P (the patterns growing from P) will also have their support less than α. Therefore, if a query involves multiple databases, relationship operator $\ " \geq \ "$ or $" > "$ and a single threshold value α, we may decompose this query into a set of sub-queries with each single database and the threshold value α listed as the antecedent and the consequent the relationship operator, respectively. For example, a query $\{ A \ge B \ge C \ge \alpha \}$ can be decomposed into three sub-querie $( A \geq \alpha ) , \ ( B \geq \alpha ) .$ , and $\left( C \geq \alpha \right)$ , each of which strictly complies with the Apriori rule. It is obvious that if a pattern P violates any one of these three sub-queries, there is no way for $P ,$ as well as P's super-sets, to be a quali<sup>fi</sup>ed pattern.

Property 2. Given a sub-query which contains a relationship operator $\ddot { \geq } \ " { o r } \ " > \ " { , }$ , if the sub-query has the sum $( \ " + \ " )$ of multiple databases and a threshold value α as the antecedent and the consequent of the relationship operator $" \geq " 0 r \ " > " ,$ , respectively, this sub-query complies with the down closure property.

Proof. Given a pattern P and any of its sub-patterns $Q ,$ assuming $P \boldsymbol { s }$ and Q's supports in A, B and C are $p _ { 1 } , p _ { 2 } , p _ { 3 }$ and $q _ { 1 } , q _ { 2 } , q _ { 3 }$ respectively, it is obvious that q<sub>1</sub> ≥ p<sub>1</sub>, q<sub>2</sub> ≥ p<sub>2</sub>, q<sub>3</sub> ≥ p<sub>3</sub>. If $( p _ { 1 } + p _ { 2 } + p _ { 3 } ) \ge \alpha$ , then it is obvious that $( q _ { 1 } + q _ { 2 } + q _ { 3 } ) \geq ( p _ { 1 } + p _ { 2 } + p _ { 3 } ) \geq \alpha$ . Therefore, the property 2 is true. This property states that if a sub-query sums up multiple databases and is followed by factors $" \geq " 0 \Gamma " > "$ and a threshold value α, then the sub-query strictly follows the down closure property and can be directly used for pattern pruning.

Property 3. Given a sub-query which contains a relationship operator $\because o r ^ { \ast } > " ,$ if the sub-query has the support difference of two databases, say $( S _ { i } – S _ { j } )$ , and a threshold value α listed as the antecedent and the consequent of the relationship operator $" \geq " o r " > "$ , respectively, this subquery can be further transformed into a sub-query like $S _ { i } { \geq } \alpha ,$ which still complies with the down closure property.

Proof. It is obvious that if $( A - B ) \geq \alpha$ , then $A \geq \left( B + \alpha \right)$ . Since a pattern's support in a database cannot be negative, we have A≥α.

Property 4. Given a sub-query which contains a relationship operator $" \geq " 0 r \ " > " ,$ if the sub-query has the absolute support difference of two databases, say $| S _ { i } { - } S _ { j } | ,$ , and a threshold value α listed as antecedent and the consequent of the relationship operator $" \geq " \ o r \ \stackrel { * } { > } " ,$ , respectively, this query can be transformed into a sub-query like $\{ ( S _ { i } \ge \alpha ) \mid ( S _ { j } \ge \alpha ) \}$ }, which still complies with the down closure property.

Proof. It is obvious that i $\operatorname { f } \left| A - B \right| \ge \alpha$ , then we have $( A - B ) \geq \alpha \ \mathrm { o r } \ ( A -$ $B ) \leq - \alpha$ , which are equivalent to the inequations $A \geq \left( B + \alpha \right) \operatorname { o r } B \geq \left( A + \alpha \right)$ α), i.e. $\{ ( A { \ge } \alpha ) | ( B { \ge } \alpha ) \}$ . For any pattern $P ,$ if its supports in A and B are both less than $\alpha ,$ there is no way for $P s$ super-set to have a higher support than α. Therefore, the pattern P still complies with the down closure property.

Property 5. A sub-query containing relationship factors $" \leq "$ or “b”complies with the down closure property.

Proof. It is obvious that even if a pattern, say $\mathrm { P } _ { 1 } = \{ \mathsf { a b c } \}$ in a database $S _ { i } ,$ does not satisfy $S _ { i } { \le } \beta ,$ its super-set, say $\mathsf { P } _ { 2 } = \{ \mathsf { a b c d } \}$ , may still comply with $S _ { i } { \le } \beta .$ Therefore, any pattern that does not satisfy query $S _ { i } { \le } \beta$ cannot be pruned out, because it can later grow into a longer length pattern, which eventually will satisfy the query constraint $( S _ { i } { \le } \beta )$

In our design, a query is decomposed at the master site based on the above properties. The decomposed sub-queries (which comply with the down-closure property) are placed into Down Closure (DC) sub-sets and are further dispatched to distributed sites. The original query is also kept to validate patterns at the <sup>fi</sup>nal stage.

## 4. Pattern mining frameworks

From a system perspective, the problem of distributed mining (for $\mathrm { L } \mathrm { - } , \mathrm { G } \mathrm { - } ,$ and I-pattern discovery) can be solved by three frameworks: (1) SeQuentiaL Pattern mining (SQLP); (2) PAralleL Pattern mining (PALP); and (3) CoLlAborative Pattern mining (CLAP). The conceptual views of the three frameworks are shown in Fig. 1, where a master node collects user queries and collects mining results from distributed databases DB , $\mathsf { D B } _ { 2 } , . . . , \mathsf { D B } _ { \mathrm { n } }$

In Fig. 1, SQLP and PALP are self-contained mining frameworks, because mining is essentially carried out in individual sites without involving data from other sources. For SQLP, pattern mining is initialized at a seed database $( i . e . , D B _ { 1 }$ in Fig. 1(a)) with results passed on to the second database for veri<sup>fi</sup>cation. The above process repeats until patterns are veri<sup>fi</sup>ed by all databases involved in the query. For example, to answer $\mathrm { Q } _ { 2 } { = } \{ ( A { > } B { \geq } \alpha ) ~ \up& { } ( \mathrm { C } { < } \beta ) \}$ } in Section 1, SQLP may start from database A to <sup>fi</sup>nd frequent patterns satisfying $\{ { \sf A } > { \bf \alpha } \}$ , and then pass on patterns to database B to <sup>fi</sup>nd patterns satisfying $\{ A > B \}$ . Any patterns not satisfying the query will be pruned out immediately.

Instead of mining and verifying patterns in a sequential way, PALP carries out the mining of individual databases in parallel, and collects all patterns in a central location to <sup>fi</sup>nd the ones satisfying the user queries. In Fig. 1(b), the mining is initiated in all databases, and the answers are forwarded to the master site for validity check. For example, to answer $\mathrm { Q } _ { 2 } { = } \{ ( A { > } B { \geq } \alpha ) \ \up& \ ( \mathrm { C } { < } \beta ) \}$ in Section 1, PALP concurrently discovers patterns from each single database (A and B), and then collects all patterns to <sup>fi</sup>nd those that are quali<sup>fi</sup>ed. One should be aware that it is technically not feasible to <sup>fi</sup>nd patterns which satisfy $\{ C < \beta \}$ by using database C alone, because no deterministic pruning rules will hold and one has to list all the candidates, if he/she intends to do so. Therefore, PALP will concurrently mine patterns from A and $B ,$ and then pass on the patterns to C for veri<sup>fi</sup>cation.

For both SQLP and PALP, the pattern mining process (candidate generation and pruning) is carried out at each single site. The inherent disadvantage of such self-contained mining frameworks is that pattern generation and pruning are essentially single-database-oriented and inef<sup>fi</sup>cient for distributed mining. Taking a simple query like $Q =$ $\{ ( \mathsf { S } _ { \mathrm { i } } \ge \alpha ) \& ( \mathsf { S } _ { \mathrm { j } } \ge \alpha ) \}$ } as an example, for small α values, a large number of patterns may satisfy either $\mathrm { S _ { i } } 2 \alpha \ \mathrm { o r } \mathrm { S _ { j } } 2 \alpha$ , but very few of them satisfy $( { \sf S } _ { \mathrm { i } } \ge { \alpha } ) \ \& \ ( { \sf S } _ { \mathrm { j } } \ge { \alpha } )$ . Consequently, a pruning process utilizing information from S and S is much more ef<sup>fi</sup>cient than mining $\mathsf { S } _ { \mathrm { i } }$ and $S _ { \mathrm { j } }$ alone.

Different from self-contained mining where sites are independent of each other and the mining process is limited to the local data, joint mining intends to let distributed databases collaborate with each other for pattern discovery. Ideally, a joint mining framework should meet the following three criteria for pattern discovery: (1) being able to unify distributed databases for cross-database pattern pruning; (2) being able to answer complex queries for mining all three types of $( \mathrm { L } \mathrm { - } , \mathsf { G } \mathrm { - } ,$ , and I-) patterns; and (3) being able to scale up to large volume databases with limited bandwidth consumption and no source data sharing.

Fig. 1(c) proposes a framework, CLAP, which carries out mining activities in a $\ " \mathrm { j } 0 \mathrm { i n t } \ "$ manner. CLAP allows the distributed sites to communicate with each other and exchange messages, so the mining is carried out at distributed sites without any data integration. The crossdatabase pattern pruning is achieved by using messages exchanged between sites.

Several concerns remain regarding the ef<sup>fi</sup>ciency of the proposed collective and collaborative mining frameworks:

• What type of information should be exchanged between sites for effective mining and data privacy protection?

![](/api/attachments/UVFYD75F/fulltext/images/0af74c756b948fe7b091a23460ef8da63e39ab13e5b31a978338c299d04d00bc.jpg)  
Fig. 1. Conceptual views of the data and knowledge <sup>fl</sup>ow of different mining frameworks: solid lines indicate physical connections and dash lines show the data and knowledge <sup>fl</sup>ow. Gray nodes indicate nodes actually carrying out the mining activities (candidate generation and pruning). In SQLP, patterns are discovered from one DB and sequentially passed to others for veri<sup>fi</sup>cation; in PALP, patterns are generated in each single database and forwarded to the master site for validation; and in CLAP, the mining activities are carried out in distributed sites with messages exchanged between sites for cross-database pruning.

• How to exchange messages between sites for effective transmission and mining?

• How to utilize information from other sites to ful<sup>fi</sup>ll cross-database pattern pruning and mining?

This paper proposes to rely on the exchanging of pattern <sup>fi</sup>lters between distributed sites for cross database pruning. More speci<sup>fi</sup>cally, the distributed sites will exchange the complete set of length-l patterns with other sites for cross database pruning, so each site can immediately prune out candidates which do not satisfy the query. Because exchanging patterns and checking pattern existences in a database are timeconsuming, we will employ bloom <sup>fi</sup>lters to accelerate the whole mining process.

## 5. Clap: Collaborative pattern mining

Collaborative pattern mining advocates pattern discovery in a distributed manner with each distributed site carrying out pattern pruning in collaboration with its peers, by employing the Bloom Filter (BF) [7,10,13,16,20] based pattern switching mechanism. In following sub-sections, we <sup>fi</sup>rst brie<sup>fl</sup>y introduce the bloom <sup>fi</sup>lter and its potential for distributed mining. In Section 5.2 we introduce a depth-limited FP-growth process which utilizes bloom <sup>fi</sup>lters to achieve cross-database pruning. The collaborative pattern mining framework is introduced in Section 5.3.

## 5.1. Bloom filters for distributed mining

A bloom <sup>fi</sup>lter (BF) is a space ef<sup>fi</sup>cient data structure, which consists of k hash functions, $H _ { 1 } ( \cdot ) , H _ { 2 } ( \cdot ) , . . . , H _ { k } ( \cdot )$ , and an m bits binary array. The strength of a BF tests whether a given element is a member of a set in a very effective way [7,16,20]. Fig. 2 shows given elements $x _ { 1 } , x _ { 2 } , . . . , x _ { n } ,$ each of which is hashed by k hash functions to k locations of the m-bits array. The m-bits array is initially set to 0, but a bit j of the array is <sup>fl</sup>ipped to 1, if any hash function maps a pattern x to the jth location. Following the above procedure, one can add all n patterns $x _ { 1 } , x _ { 2 } , . . . , x _ { n }$ into the bloom <sup>fi</sup>lter. To check whether a pattern x exists in a bloom <sup>fi</sup>lter or not, one can use all k hash functions to map $x _ { t }$ to k positions. If any of the k positions is $0 , x _ { t }$ does not exist in the bloom <sup>fi</sup>lter. If all k bits are 1, we conclude that x exists in the bloom <sup>fi</sup>lter with regard to a false positive rate (the bits may be set to 1 during the insertion of other patterns rather than x ).

![](/api/attachments/UVFYD75F/fulltext/images/83c03efe6563e005ca3738814b41508ccf5e75c3ed43feb8074547815589b2d8.jpg)  
Fig. 2. Bloom <sup>fi</sup>lter architecture.

Assume the size of the bloom <sup>fi</sup>lter array is m bits, the probability that a certain bit is not set to one by a certain hash function h(⋅) during the insertion of an element is

$$
1 - \frac {1}{m}\tag{1}
$$

Given k hash functions $h _ { 1 } ( \cdot ) , h _ { 2 } ( \cdot ) , . . . , h _ { k } ( \cdot )$ , the probability that a certain bit is not set to one by any of the k hash functions is given below

$$
\left(1 - \frac {1}{m}\right) ^ {k}\tag{2}
$$

Because the insertion of each element is independent, after inserting n elements to the bloom <sup>fi</sup>lter, the probability that a certain bit is set to 1 is given in Eq. (3)

$$
1 - \left(1 - \frac {1}{m}\right) ^ {n k}\tag{3}
$$

Assume an element x was not inserted into the bloom <sup>fi</sup>lter earlier, a false positive happens only if all of the k hash positions of x are set to 1. This is equivalent to the probability shown in Eq. (4), which asserts that the false positive rate of a bloom <sup>fi</sup>lter decreases as the <sup>fi</sup>lter size (m value) increases, and increases as the number of inserted items (n value) increase.

$$
\left(1 - \left(1 - \frac {1}{m}\right) ^ {n k}\right) ^ {k} \approx \left(1 - e ^ {- k n / m}\right) ^ {k}\tag{4}
$$

Assume two sites $S _ { i }$ and $S _ { j }$ are carrying out pattern mining to discover patterns frequent in both $S _ { i }$ and $S _ { j } ,$ bloom <sup>fi</sup>lters can help both sites achieve cross-database pruning by switching their bloom <sup>fi</sup>lters $B F _ { i }$ and $B F _ { j }$ (each contains patterns frequent at one site). The employment of the bloom <sup>fi</sup>lters has a number of advantages. First, a bloom <sup>fi</sup>lter is fast for membership checks. Assume site $S _ { i }$ has the bloom <sup>fi</sup>lter $B F _ { j }$ from $S _ { j } , S _ { i }$ can query $B F _ { j } ,$ , with O(1) time complexity, to check whether a pattern exists in $S _ { j }$ or not. Secondly, a bloom <sup>fi</sup>lter is space ef<sup>fi</sup>cient. Exchanging bloom <sup>fi</sup>lters between sites is much more ef<sup>fi</sup>cient than exchanging patterns between sites. Thirdly, a bloom <sup>fi</sup>lter's false negative value is zero. In other words, $\operatorname { i f } S _ { i }$ queries $B F _ { j }$ and <sup>fi</sup>nds that a pattern x does not exist in $B F _ { j } ,$ then x is indeed not frequent in $S _ { j } .$ As a result, $S _ { i }$ may safely remove x. So the cross-database pattern pruning can be achieved.

## 5.2. Depth-limited pattern growth for cross-database pruning

By using bloom <sup>fi</sup>lters, a naive cross-database pruning approach, following the Apriori principle [2], can be implemented as follows:

1. Given a site $S _ { \mathrm { i } } ,$ use the Apriori mining approach to generate a complete set of length-l patterns.

2. Use frequent length-l patterns in site $S _ { i }$ to construct a bloom <sup>fi</sup>lter $\left( B F _ { i ^ { - } } l \right)$ , and broadcast BF -l to other sites.

3. After site $S _ { i }$ receives the bloom <sup>fi</sup>lters $B F _ { j }  – l$ from other sites, it can query $B F _ { j }  – l$ and prune out length-l patterns in $S _ { i }$ and then grow length-(l + 1) patterns.

4. Set $l \gets l + 1$ and repeat Steps 2 to 4 until no more frequent patterns can be discovered from any sites.

The main disadvantage of the above cross-database pruning approach is that it critically relies on the Apriori principle, where repetitive database scanning is heavily time-consuming and will signi<sup>fi</sup>cantly slow down the mining process. In this sub-section, we propose a new depth-limited FP-growth (DLFP-growth) which combines the strength of the bloom <sup>fi</sup>lter and FP-growth for distributed sites to achieve cross-database pruning.

Intuitively, although FP-growth is effective for pattern mining, it is, however, unsuitable for cross-database pruning. This is because FPgrowth is a depth-<sup>fi</sup>rst recursive process which starts from an item $" a '$ and discovers all patterns related to $" a '$ before it moves on to the next item $" b " .$ . Such a depth-<sup>fi</sup>rst approach makes the collection of the complete set of length-l patterns unavailable until the whole algorithm ceases. In other words, we cannot collect all length-l patterns from site S and distribute them to other sites until the whole mining process at S stops (then pattern switching between sites becomes meaningless). Alternatively, we can forbid the recursive FPgrowth process from going deeper once the length of the pattern reaches a limit l, then force FP-growth to turn to the next items and continue to discover the complete set of length-l patterns (i.e., turn the depth-<sup>fi</sup>rst search into a depth-limited approach).

The depth-limited FP-growth (DLFP-growth), as shown in Fig. 3, takes four parameters, an FP tree, a base set BS, a length constraint l, and a set of bloom <sup>fi</sup>lters, if they exist, BF[], as input. On Step 1, DLFP-Growth will terminate and stop growing the pattern longer if the length of the pattern (enclosed in the BS) reaches the length l.

In Step 2, the pattern growth will be carried out for each item $x _ { i }$ of the given FP tree. This process utilizes the bloom <sup>fi</sup>lters collected from distributed sites for cross-database pruning. Given a base set BS and item $x _ { i } ,$ the new pattern ϑ for growth is the concatenation of BS and $x _ { i } ,$ as shown in Step 2.a. Instead of directly building an FP tree for $x _ { i } ,$ which is a relatively expensive process, we can query bloom <sup>fi</sup>lters BF [] and prune out x if any sub-sets of ϑ do not exist in BF[]. For example, assume BS={abd} and $x _ { i } = \operatorname g ,$ then the pattern under growth is $\vartheta =$ {abdg}. Assume a bloom <sup>fi</sup>lter in $B F [ ] ,$ denoted by $B F _ { j } – 3$ , contains length-3 patterns from site $S _ { j } .$ We query any length-3 sub-sets of ϑ, such as $\displaystyle \vartheta _ { 1 } = \{ { \mathrm { b d g } } \}$ , from $B F _ { j }  – 3 .$ . If $\vartheta _ { 1 }$ does not exist in $B F _ { j }  – 3 ,$ , we can safely prune out $x _ { i } = \mathbf { g }$ without growing an FP tree for $x _ { i }$ because pattern ϑ is not frequent in the distributed sites $S _ { j } ,$ so there is no need to grow it in the local site $S _ { i } .$

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
DLFP-Growth (FP-tree, BS, l, BF[])
Input: (1) An FP tree: FP-tree; (2) A Base set BS; (3) a length constraint l
(4) Bloom filters collected from other sites, if exist: BF[]
Output: Length l pattern set P
1. If BS contains l items
    a. Return BS
2. For each item  $x_{i}$  in the header table of FP-tree
    a.  $\vartheta \leftarrow BS \cup x_{i}$ 
    b. If (BF[] exist and any subset of  $\vartheta$  does not exit in BF[])
    i. Continue //Prune out  $a_{i}$  and move to next items
    EndIf
    c. Build an FP-tree $_{i}$  from FP-tree (please refer to [11] for details)
    d.  $p \leftarrow$ LCFP-Growth(FP-tree $_{i}$ ,  $\vartheta$ , l, BF[])
    e.  $P \leftarrow P \cup p$ 
EndFor
3. Return (P)
</div>

Fig. 3. Depth-Limited FP-growth process.

It is worth noting that the DLFP-growth process can be easily adjusted to <sup>fi</sup>t different situations through the tuning of the parameters l and BF[]. For example, if we set l=−1 and BF[]=null, then DLFP-growth degenerates as the traditional FP-growth. On the other hand, setting l to any values greater than 0 with BF[]=null, one can collect all length-l patterns without utilizing any bloom <sup>fi</sup>lters from other sites. In the next sub-section, we will articulate technical details of using DLFP-growth for collaborative pattern mining from distributed databases.

## 5.3. Collaborative pattern mining with DLFP-growth

In Fig. 4, we list major steps for a site to carry out collaborative pattern mining using length constrained FP-Growth, where crossdatabase pruning is achieved through the following three major steps:

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
CLAP: Collaborative Pattern Mining ( $S_{i}$ , SQ, l)

Input  $S_{i}$ : A distributed site along with its data D

SQ: A subquery delivered from the master site

l: The pattern length constraint for cross site pruning through BF.

Output  $\Phi$ : pattern set satisfying the subquery SQ

1.  $\Phi \leftarrow \emptyset$ 

2.  $FP_{i} \leftarrow \text{build\_FP\_Tree}(S_{i}, SQ)$ 

3.  $length\_l\_set \leftarrow \text{DLFP-Growth}(FP_{i}, null, l, null)$ 

4.  $BF_{i\_l} \leftarrow \text{build\_BF}\text{(length\_l\_set)}$  // a BF contains length l patterns

5.  $S[] \leftarrow \text{check relevant sites}(SQ)$  // check sites relevant to the subquery SQ

6. Request length_l_set from sites S[] // request length l patterns from relevant sites

7. Switch (Events) // event actions

8. Case: receiving length_l_set request from sites  $S_{j}$  // a site request patterns

9. Send  $BF_{i\_l}$  to  $S_{i}$  if available

10. Case: site  $S_{j}$  responds BF_l request // a site confirm request sent on Step 6

11. BF_l[j] ← receive BF_l from  $S_{j}$ 

12. Else: For every item  $a_{i}$  in  $FP_{i}$  // FP-Growth with cross site pruning

13. P ← DLFP-Growth ( $FP_{i}, null, -1, BF\_l[]$ )

14.  $\Phi \leftarrow \Phi \cup P$ 

15. EndFor

16. Send  $\Phi$  to the master site

17. EndSwitch

18. Return ( $\Phi$ )
</div>

• A local site S generates the complete set of length-l frequent patterns by calling DLFP-growth. (Step 3)

• Site $S _ { i }$ constructs a bloom <sup>fi</sup>lter, BF \_l, by using length-l frequent patterns discovered at Step 3, and sends BF \_l to distributed sites. (Steps 4, 8, and 9)

• Site $S _ { i }$ carries out pattern growth with cross-database pruning, by using BF\_l[] collected from other sites. (Steps 12, 13, and 14)

The framework in Fig. 4 is essentially an asynchronous distributed mining module, which means that each distributed site can work independently without synchronizing with any other sites. For any site $S _ { i } ,$ a sub-query SQ is accepted from the master site as an input, and then the sites relevant to the sub-query SQ are determined (Step 5). After that, $S _ { i }$ will send a request to each of the relevant sites and ask them to send a bloom <sup>fi</sup>lter containing length-l patterns to $S _ { i \cdot }$ The mining process then runs into an event driving loop between Steps 7 and 17. More speci<sup>fi</sup>cally, if site $S _ { i }$ receives a request from site $S _ { j } ,$ which is asking for length-l patterns, $S _ { i }$ will immediately send BF \_l to $S _ { j }$ as shown in Steps 8 and 9. If a site $S _ { j }$ responds to S 's request at Step 6, S will collect the bloom <sup>fi</sup>lter from $S _ { j }$ and include it with the bloom <sup>fi</sup>lter arrays BF[]. Under any other circumstances, $S _ { i }$ will continuously grow patterns by using the bloom <sup>fi</sup>lters collected from other sites (Steps 12 to 15).

After each site completes the mining process, the results (patterns and their actual support values) are delivered to the master site, which will further verify and <sup>fi</sup>nalize valid patterns. For example, for a query like $Q = \{ ( S _ { i } \ge S _ { j } \ge \alpha )$ and $S _ { k } { \le } \beta \}$ , the master site needs to collect patterns satisfying $( S _ { i } { \ge } S _ { j } { \ge } \alpha )$ and then deliver the pattern to $S _ { k }$ to <sup>fi</sup>nalize those with their support values less or equal to $\beta .$

Alert readers may have noticed that a large portion of length-l patterns discovered at Step 3 will be re-discovered at Step 13. This raises a concern regarding the extra cost involved at Step 3, especially if this step takes a signi<sup>fi</sup>cant amount of system runtime. In Section 6.2, we will show that when using small l values (e.g., l=2 or 3), Step 3 only costs 1–2% (or less) of the runtime compared to the FP-Growth without length constraints. Given that the goal of Step 3 is to enable the cross-database pruning, the extra cost added to this step is of little concern.

Notice that a bloom <sup>fi</sup>lter cannot encode support values of the patterns, indicating that CLAP may not directly answer a summation based query like $Q = \{ ( S _ { i } + S _ { \mathrm { i } } ) \geq \alpha \}$ because, without knowing the support values of a pattern p in both $S _ { i }$ and $S _ { j } ,$ we cannot determine whether p (along with its successors) can satisfy the query $Q = \{ ( S _ { i } +$ $\mathrm { S _ { j } } ) { \geq } \alpha \}$ . In addition, even if a pattern p's support in $S _ { i }$ is 0, it may have the summation $S _ { i } + S _ { \mathrm { j } }$ greater than $\alpha ,$ which makes p a legitimate pattern with regard to the query Q (but mining patterns satisfying $Q = \{ S _ { i } \ge 0 \}$ are technically infeasible). CLAP solves this problem by repetitively exchanging length-1, length-2 and length-3 item-sets between sites to collect a reasonable set of length-3 patterns from which the pattern growth becomes possible. More speci<sup>fi</sup>cally, given query $Q = \{ ( S _ { i } + S _ { \mathrm { j } } ) \geq \alpha \}$ , we <sup>fi</sup>rst collect length-1 item-sets and their support values for both S and $S _ { j } ,$ and we exchange item-sets and their values between $S _ { i }$ and $S _ { j } ,$ so each site knows exactly the support values of each item in the other site. According to Property 2 in Section 3, any item with its support value $( S _ { i } + S _ { j } ) { < } \alpha$ cannot grow patterns satisfying $\mathrm { Q } { = } \{ ( S _ { i } { + } S _ { \mathrm { j } } ) { \geq } \alpha \}$ . As a result, sites S and S can prune out length-1 item-sets, and grow and exchange length-2 item-sets between each other. The above process involves a heavy communication cost, so we repeat this process for only a limited number of times (l=3 in our experiments), then we let S and S independently grow without further communication.

## 5.4. Distributed pattern mining framework comparisons

In Table 1, we brie<sup>fl</sup>y summarize the strength and weakness of the three distributed mining frameworks (SQLP, PALP, and CLAP), from system design, functionalities, and data privacy perspectives. The detailed performance comparisons are reported in Section 6. Between all three frameworks, CLAP is the only one with cross-database pruning that is capable of mining all three (L-, G-, and I-) types of patterns.

A simple comparison between three distributed mining frameworks. “+” indicates that a framework is positive with respect to the assessment criterion $" - "$ means negative, “\~” represents partially positive (i.e., a framework may partially meet the criterion), and $" / "$ means the criterion is meaningless for that particular framework

<table><tr><td>Assessment criteria</td><td>SQLP</td><td>PALP</td><td>CLAP</td></tr><tr><td>Mining L-patterns?</td><td>+</td><td>+</td><td>+</td></tr><tr><td>Mining G-patterns?</td><td>-</td><td>-</td><td>+</td></tr><tr><td>Mining I-patterns?</td><td>~</td><td>~</td><td>+</td></tr><tr><td>Distributed mining activities?</td><td>+</td><td>+</td><td>+</td></tr><tr><td>Cross-database pruning?</td><td>-</td><td>-</td><td>+</td></tr><tr><td>Distributed data structure?</td><td>+</td><td>+</td><td>+</td></tr><tr><td>Low memory consumption?</td><td>+</td><td>~</td><td>+</td></tr><tr><td>Limited # of DB scanning?</td><td>-</td><td>+</td><td>+</td></tr><tr><td>Data privacy concerns?</td><td>+</td><td>+</td><td>+</td></tr><tr><td>Effective message switching?</td><td>-</td><td>/</td><td>+</td></tr><tr><td>Parallel mining activities?</td><td>-</td><td>+</td><td>+</td></tr></table>

From a message exchanging perspective, CLAP and SQLP are the only two frameworks requiring message switching between sites (excluding the master site). Comparing CLAP and SQLP, CLAP employs the bloom <sup>fi</sup>lter for message switching, whereas SQLP directly passes on the original patterns from one database to another. As a result, CLAP is much more ef<sup>fi</sup>cient in terms of message switching.

## 6. Experiments

## 6.1. Experimental settings

## 6.1.1. Methods

For comparison purposes, we implement all three frameworks discussed in Section 4. All programs are written in C++ (Borland C++ Builder 6.0). For CLAP, we use open bloom <sup>fi</sup>lter [40] as the basis and implement our own bloom <sup>fi</sup>lter. In the experiments, the size of the bloom <sup>fi</sup>lter (m) is selected so that the ratio between the <sup>fi</sup>lter size (m) and the item number (n) is 8, and the number of hash functions is set to $k = 5 , ^ { 2 }$ which gives a theoretical false positive rate of about 2.14%. For SQLP and PALP, each site uses an FP tree to achieve maximal mining speeds (we implement the FP tree using an STL-like C++ tree class [41]).

## 6.1.2. Data

Our test-bed, listed in Table 1, consists of two groups of synthetic data-sets generated from an IBM quest data generator [25]. The explanation of the data description used in Table 2 is as follows. T1000k.N10kS1kL20 means a database with one million transactions, 10,000 unique items (N), and 1000 signi<sup>fi</sup>cant patterns (S), where the average length of the maximum length pattern is 20 (L) (L20+19 means the combinations of setting L to 20 and 19; more details follow).

The two groups in Table 2 simulate “strong dense (SD)” and “weak sparse (WS)” distributed databases. More speci<sup>fi</sup>cally, “dense vs. sparse” means the number of unique items in the database, and a dense database has a smaller number of unique items compared to a sparse database; “strong vs. weak” indicates the similarity or correlations between databases, where “strong” means that distributed databases have high similarities and strong correlations with each other. In Table 3, we report the pair-wise similarities of the WS and SD databases, where each similarity value between row $\left( D _ { r } \right)$ and column databases $\left( D _ { c } \right)$ is given in Eq. (5). In short, for a speci<sup>fi</sup>c support value $\alpha ,$ the pair-wise similarity between $D _ { r }$ and $D _ { c }$ in Eq. (5) is calculated as the percentage of the number of rules discovered by both $D _ { c }$ and $D _ { r }$ , in comparison with the total number of rules discovered by $D _ { r }$ . The pair-wise similarity is asymmetric so $D B _ { \alpha } ( r , c ) \neq D B _ { \alpha } ( c , r )$ . For the IBM quest data generator, the L value will determine the pattern distributions. Varying the L values will generate databases with very little correlation (whereas <sup>fi</sup>xing the L value will output strongly correlated databases). Therefore, in our experiments, the WS databases are generated by a mixture of two L values.

Benchmark database characteristics.

<table><tr><td>Database</td><td></td><td>Database description</td></tr><tr><td rowspan="4">Strong dense databases</td><td> $SD_1$ </td><td>T1000k.N1kS1000L20</td></tr><tr><td> $SD_2$ </td><td>T500k.N1kS1000L20</td></tr><tr><td> $SD_3$ </td><td>T250k.N1kS1000 L20</td></tr><tr><td> $SD_4$ </td><td>T125k.N1kS1000 L20</td></tr><tr><td rowspan="4">Weak sparse databases</td><td> $WS_1$ </td><td>T1000k.N10kS1000 L20 + 20</td></tr><tr><td> $WS_2$ </td><td>T500k.N10kS1000 L20 + 19</td></tr><tr><td> $WS_3$ </td><td>T250k.N10kS1000 L20 + 18</td></tr><tr><td> $WS_4$ </td><td>T125k.N10kS1000 L20 + 17</td></tr></table>

The values in Tables 3 show that SD databases have very high similarity, e.g., almost all rules discovered in $S D _ { 4 }$ are discovered by $S D _ { 1 }$ as well, whereas a very small percentage of rules in the WS databases are identical to each other.

$$
D B _ {\alpha} (r, c) = \frac {| D _ {r} \cap D _ {c} |}{| D _ {r} |}\tag{5}
$$

## 6.1.3. Measures

The experiments select a number of queries (listed in Table 4) as benchmarks which are provided to a dedicated master site. The queries are further decomposed into a number of sub-queries and are dispatched to corresponding sites if necessary. Although it is possible to re-use previously discovered results to answer a query (e.g., results from {S ≥0.5%} can be re-used by query {S ≥0.8%}), for fairness of the comparison, all queries are answered by reinitializing the whole mining process. All algorithms are compared based on their runtime performances and/or the size of messages exchanged between sites. The runtime of the systems crucially relies on the underlying queries. For an objective assessment, we de<sup>fi</sup>ne four queries, as shown in Table 4, and will demonstrate the average system runtime performances to answer these queries.

The performance of CLAP relies on two important factors: (1) depthlimited pattern growth for cross-database pruning; and (2) bloom <sup>fi</sup>lter based message exchanging between sites. The following sections study CLAP in detail. A comparative study across all three frameworks (including SQLP and PALP) is reported in Sections 6.4.

## 6.2. Depth limited pattern growth results

As shown in Fig. 4, the cross-database pruning of CLAP relies on the exchange of the length-l patterns between sites. This raises an important issue of <sup>fi</sup>nding the proper l value for DLFP-growth to <sup>fi</sup>nd the complete set of length-l patterns (Step 3 in Fig. 4). Practically, although exchanging length-l patterns between sites can enable cross-database pruning, the process of <sup>fi</sup>nding the complete set of length-l patterns adds extra cost to individual sites. So l values must be properly determined to ensure balanced performance gains.

Table 3  
Pair-wise database similarities $( \alpha = 0 . 5 \% )$

<table><tr><td colspan="5">(a) Strong dense databases</td><td colspan="5">(b) Weak sparse databases</td></tr><tr><td>DB</td><td> $SD_1$ </td><td> $SD_2$ </td><td> $SD_3$ </td><td> $SD_4$ </td><td>DB</td><td> $WS_1$ </td><td> $WS_2$ </td><td> $WS_3$ </td><td> $WS_4$ </td></tr><tr><td> $SD_1$ </td><td>1.0</td><td>0.91</td><td>0.98</td><td>0.22</td><td> $WS_1$ </td><td>1.0</td><td>0.04</td><td>0.04</td><td>0.03</td></tr><tr><td> $SD_2$ </td><td>0.97</td><td>1.0</td><td>0.96</td><td>0.21</td><td> $WS_2$ </td><td>0.02</td><td>1.0</td><td>0.02</td><td>0.02</td></tr><tr><td> $SD_3$ </td><td>0.91</td><td>0.84</td><td>1.0</td><td>0.19</td><td> $WS_3$ </td><td>0.01</td><td>0.01</td><td>1.0</td><td>0.01</td></tr><tr><td> $SD_4$ </td><td>0.99</td><td>0.92</td><td>0.90</td><td>1.0</td><td> $WS_4$ </td><td>0.02</td><td>0.02</td><td>0.02</td><td>1.0</td></tr></table>

Table 4  
Query plan description.

<table><tr><td>Query</td><td>Query constraints</td></tr><tr><td> $Q_1$  (L-pattern)</td><td> $\{(S_1| S_2| S_3| S_4) \geq \alpha |\}$ </td></tr><tr><td> $Q_2$  (G-pattern)</td><td> $\{(S_1 \cup S_2 \cup S_3) \geq \alpha \}$ </td></tr><tr><td> $Q_3$  (I-pattern)</td><td> $\{(S_1 + S_2) \geq \alpha \& (S_3 \leq S_4 \leq \beta)\}$ </td></tr><tr><td> $Q_4$  (I-pattern)</td><td> $\{S_1 \geq S_2 \geq S_3 \geq S_4 \geq \alpha\}$ </td></tr></table>

In Fig. 5, we report the ratios between the runtimes of DLFPgrowth with different l values and DLFP-growth without any length constraint, as de<sup>fi</sup>ned in Eq. (6), which shows the extra cost of CLAP in <sup>fi</sup>nding the complete set of length-l patterns (compared to the total mining cost for each individual site).

$$
r = \text { DLFP } (F P \text {   tree }, \text { null }, l, \text { null }) / \text { DLFP } (F P \text {   tree }, \text { null }, - 1, \text { null })\tag{6}
$$

The results in Fig. 5 indicate that for both databases $( S D _ { 1 } , W S _ { 1 } )$ , the major cost of the FP-growth is the discovery of medium size patterns. For example, for $S D _ { 1 }$ the cost of <sup>fi</sup>nding all length-3 (and length-2) patterns by DLFP is only 3.7% of the cost of <sup>fi</sup>nding all frequent patterns, whereas <sup>fi</sup>nding all length-10 (and shorter) patterns takes about 53% of system runtime. This is easy to understand because when l is small, the number of length-l item-sets is only a small portion of the candidate patterns evaluated by the system. Similarly, only a very small portion of patterns in the database have a long length, and the majority of patterns (or candidates) are medium length, which explains why two curves in Fig. 5 are sigmoid in shape.

In order to study the impact of the length-l patterns for crossdatabase pruning, we choose databases $W S _ { \imath }$ and $W S _ { 2 }$ and run CLAP mining at WS<sub>1</sub> by using bloom <sup>fi</sup>lters from $W S _ { 2 }$ with different lengths of patterns, i.e. $B F _ { 2 - } l ~ ( l = 2 , 3 , . . 6 )$ . If mining were carried out on WS alone without using any bloom <sup>fi</sup>lters from $W S _ { 2 } ,$ it takes WS 21.31 s for tree pruning and eventually outputs 49,660 patterns. The pruning ef<sup>fi</sup>ciency in this case is 0%. By including bloom <sup>fi</sup>lters from WS to assist cross-database pruning, as shown in Fig. 6, we can <sup>fi</sup>nd that CLAP signi<sup>fi</sup>cantly improves its mining ef<sup>fi</sup>ciency. For example, when including a length-2 pattern bloom <sup>fi</sup>lter $( B F _ { 2 - 2 } )$ , the tree pruning time for $W S _ { \imath }$ is reduced to 2.47 s, and the total runtime (including bloom <sup>fi</sup>lter construction) is about 21% of the stand-alone pruning time of $W S _ { 1 } .$ As pattern length l grows, the time percentage will gradually increase, mainly because mining of the complete set of length-l patterns demands more time (Fig. 6) and the cross-database pruning at WS will have to validate more candidates.

![](/api/attachments/UVFYD75F/fulltext/images/96a9527efc394db8c45da538f6b49973b5c1cfbc923614e4e682cdc10fa4c8bf.jpg)  
Fig. 5. System runtime for <sup>fi</sup>nding different length-l patterns. The x-axis denotes the pattern length l, and the y-axis denotes the percentages of the system runtimes between <sup>fi</sup>nding all patterns with length less or equal to l and <sup>fi</sup>nding all patterns (α=0.7%).

![](/api/attachments/UVFYD75F/fulltext/images/8bf36fe9981f74db21d6c05b3c674849b45c6f7b9c06ce80e2755f9648209547.jpg)  
Fig. 6. The CLAP mining results on WS by using bloom <sup>fi</sup>lters with different pattern lengths $B F _ { 2 - } l ~ ( l = 2 , 3 , . . 6 )$ from WS . “WS Pruning Time” denotes CLAP pruning time (Steps 12 to 16 in Fig. 4) on WS w.r.t. different bloom <sup>fi</sup>lter pattern lengths. “BF Construction Time” is the bloom <sup>fi</sup>lter construction time at WS . “Time Percentage” denotes the ratio between the summation of ${ } ^ { * } W S _ { 1 }$ Pruning Time”, “BF Construction Time”, and “WS Pruning Time”, and the runtime of CLAP on $W S _ { \imath }$ without using any bloom <sup>fi</sup>lters from WS (21.31 s). “Pruning Ef<sup>fi</sup>ciency” is the ratio between the number of pruned patterns (due to the inclusion of the bloom <sup>fi</sup>lters) and the number of patterns without including any bloom <sup>fi</sup>lters (49660). The support value is $\alpha = 0 . 5 \% ,$ and solid lines correspond to the left y-axis and dash lines correspond to the right yaxis.

Interestingly, the results in Fig. 6 show that, although CLAP's crossdatabase pruning ef<sup>fi</sup>ciency remains relatively stable for different l values, overall the larger the l values, the less effectively CLAP prunes out irrelevant patterns. We believe that this is mainly because length-l patterns can only help prune length-(l+1) patterns, but not length-(l-1) patterns. As the length l grows, patterns with length less than l become a signi<sup>fi</sup>cant portion of the pattern space, but they are not pruned by CLAP. Considering the above factors we set length l to 3 in our experiments.

## 6.3. Bloom filters based inter-sites message exchanging results

Table 5 reports the results of bloom <sup>fi</sup>lters built from SD with respect to different threshold values α (the results from other databases are more or less similar to the results in Table 5), where the actual False Positive (FP) rate (the last column) was collected by an average of 10,000 random queries. The results in Table 4 assert that the construction and query of the bloom <sup>fi</sup>lters are very ef<sup>fi</sup>cient, and the bloom <sup>fi</sup>lter construction time is only a tiny portion of the tree pruning time. The query time of the bloom <sup>fi</sup>lters, which is independent of the <sup>fi</sup>lter size, is also ef<sup>fi</sup>cient and can be achieved in 0.05 s for 10,000 queries. The sizes of the bloom <sup>fi</sup>lters are typically several hundred kilo-bytes or less, even for a very small support value (e.g., α≤0.1%). Consequently, the exchanging (delivering) of the bloom <sup>fi</sup>lters between sites incurs very little extra cost.

In short, the observations in this sub-section conclude that the collection of the complete set of length-l patterns and the construction of the bloom <sup>fi</sup>lters add little extra cost to the system. As a result, the employment of the depth-limited pattern growth and bloom <sup>fi</sup>lters ensures CLAP can effectively carry out cross-database pruning in a distributed manner.

The results of bloom <sup>fi</sup>lters for message exchanging between sites (l=3) (SD database).

<table><tr><td>Support α (%)</td><td># of patterns</td><td>BF size (K bytes)</td><td>BF const. time (s)</td><td>BF query time (s/10,000)</td><td>Actual FP rate (%)</td></tr><tr><td>0.5</td><td>23,668</td><td>24</td><td>0.20</td><td>0.051</td><td>2.13</td></tr><tr><td>0.4</td><td>51,955</td><td>51</td><td>0.48</td><td>0.050</td><td>2.30</td></tr><tr><td>0.3</td><td>97,094</td><td>95</td><td>0.89</td><td>0.039</td><td>2.34</td></tr><tr><td>0.2</td><td>175,433</td><td>172</td><td>1.64</td><td>0.040</td><td>2.10</td></tr><tr><td>0.1</td><td>419,898</td><td>410</td><td>3.98</td><td>0.047</td><td>2.09</td></tr></table>

![](/api/attachments/UVFYD75F/fulltext/images/495772eb2ddb08a59944e2571bf3834a0f85296e1d3dcb1251ff48c21b4f2747.jpg)  
Support Threshold (%)  
Fig. 7. Query runtime comparison on $Q _ { 4 }$ in Table 4 (SD databases).

## 6.4. Comparative studies

Figs. 7 and 8 report the system runtime comparisons across all three frameworks (SQLP, PALP, and CLAP) in answering an I-pattern (query $Q _ { 4 } )$ listed in Table 4. The results are collected with respect to different support values (α). The general setting of the experiments are as follows. For SQLP, mining is invoked at site $S _ { 1 } ,$ with the results sequentially passed on to sites $S _ { 2 } , S _ { 3 } ,$ and $S _ { 4 }$ for validation. For PALP, mining is invoked at all sites simultaneously, and the master site collects and <sup>fi</sup>nalizes the patterns satisfying the query (both SQLP and PALP use an FP tree to gain maximum speed). For CLAP, each site uses l=3, m/n=8, and $k = 5$ for depth-limited pattern growth and bloom <sup>fi</sup>lter construction. For comparison purposes, we decompose the system runtime of each framework into a number of major components, and report the decomposed runtime in Tables 6.1 to 6.3 to enable the detailed study and comparison of the three frameworks

Between the three frameworks SQLP has the smallest overhead for large support values (e.g., α≥1%) because it initiates mining at a seed site and sequentially passes on the mining results to other databases for veri<sup>fi</sup>cation. For large α values, only a very limited number of patterns are discovered from the seed site, so SQLP is quite ef<sup>fi</sup>cient in answering this type of query. The results in Figs. 7 and 8 support the hypothesis and show that when the value of α is around 1.0%, the runtime performance of all three frameworks are close to each other.

For self-contained mining frameworks, when support values α decrease, the performance of both SQLP and PALP deteriorates dramatically for two reasons. First, the mining activities of SQLP and PALP are single database oriented and as the support value decreases, pruning of the individual FP tree becomes ineffective and time consuming. Secondly, as the support value decreases, the number of patterns satisfying $S _ { i } { \geq } \alpha$ for each site $S _ { i }$ increases exponentially. For SQLP, each pattern needs to be forwarded to other databases for veri<sup>fi</sup>cation. Increasing of the pattern numbers adds signi<sup>fi</sup>cant complexity for database scanning, even if we ignore the FP tree pruning cost. Taking the result in Table 6.2 as an example, when $\alpha { = } 0 . 5 \%$ , the number of patterns generated from $W S _ { \imath }$ is 49,660 are all needed for forwarding and veri<sup>fi</sup>cation by $W S _ { 2 }$ (with over 1700 s scanning cost<sup>3</sup>). In the same setting, the dense database $D S _ { 1 }$ generate more than six million rules requiring veri<sup>fi</sup>cation by $D S _ { 2 }$ (this analysis explains why SQLP runs forever on DS databases for α≤0.5%). For PALP, all sites forward their patterns to the master site for veri<sup>fi</sup>cation, creating a huge burden for the master site to compare and verify the patterns. In our implementation, the master site builds a bloom <sup>fi</sup>lter for patterns discovered from each site, so PALP avoids clause-level rule comparison and saves a tremendous amount of runtime, but it is still time consuming when the number of patterns is large.

![](/api/attachments/UVFYD75F/fulltext/images/11d66db550f1ed0fb442f9a677be58bda3ce9a9a8e1818c4b80af1ed285e7af2.jpg)  
Support Threshold (%)  
Fig. 8. Query runtime comparison on $Q _ { 4 }$ in Table 4 (WS databases).

Because of these reasons, the performance of both SQLP and PALP are inef<sup>fi</sup>cient when the support value α is 0.5% or smaller.

CLAP, although it is subject to overheads for pattern switching between sites, provides signi<sup>fi</sup>cantly better overall performance of the joint mining framework than self-contained mining frameworks. For relatively small α values $( e . g . , 0 . 5 \% \leq \alpha \leq 1 . 0 \% )$ , CLAP linearly responds to the support value when answering the query.

CLAP's system runtime mainly consists of two parts: (1) the FP tree and bloom <sup>fi</sup>lter construction for each local site; and (2) CLAP crossdatabase pruning and pattern growth. As shown in Table 6.3, by switching bloom <sup>fi</sup>lters across sites, CLAP receives very signi<sup>fi</sup>cant performance gains for both SD and WS databases. Intuitively, CLAP is superior to PALP because it does not need to build a centralized data structure for cross-database pruning. In addition, because the mining activities of the distributed sites are collaboratively carried out in parallel, CLAP is superior to PALP on SD databases. Altogether, CLAP provides the best performance for both SD and WS databases.

Table 7 reports the system runtime for answering the <sup>fi</sup>rst three queries of Table 4, con<sup>fi</sup>rming that CLAP provides the best performance for mining all three types (L-, G-, and I-) of patterns. One interesting <sup>fi</sup>nding is that CLAP is not only effective for I-pattern discovery, but is also effective for L-pattern mining (e.g. Q ). This is because the bloom <sup>fi</sup>lter (which contains length-l patterns) built for each local site can be re-used during the local pattern growing process. For example, assume we have a bloom <sup>fi</sup>lter BF\_3 for the local site S and a base set BS={abd}. When growing a pattern ϑ=BS∪g= {abdg} by using DLFP-Growth in Fig. 3, we can query and check whether a length-3 sub-set of ϑ, say {bdg}, exists in the BF\_3 or not. According to the Apriori rule, we can stop growing θ if {bdg} does not exist in BF\_3 and, therefore, speed up the pruning process. Traditional FP-Growth, however, does not have all length-3 patterns (due to its recursive pruning nature), and has to continuously grow ϑ. In our experiment, when α=0.7% the tree pruning time for $F P _ { 1 }$ is 694.15 s (SD database), whereas, by using a local BF\_3 bloom <sup>fi</sup>lter, CLAP's pruning time is 271.46 s (in addition to 6 s for length-3 pattern discovery and BF\_3 bloom <sup>fi</sup>lter construction), which is about a 40% runtime reduction!

System runtime decomposition for SQLP, PALP, and CLAP to answer query $Q _ { 4 } =$ {S S S S 0.5%} in Table 4.  
Runtime decomposition for SQLP. The system runtime mainly consists of: (1) FP tree mining at the seed site ${ \mathrm { S } } _ { 1 } ;$ and (2) database scanning for $S _ { 2 } , S _ { 3 } ,$ and $\mathsf { S } _ { 4 } .$

<table><tr><td colspan="2">Databases</td><td> $S_1$ </td><td> $S_2$ </td><td> $S_3$ </td><td> $S_4$ </td><td>System runtime</td></tr><tr><td rowspan="2">WS</td><td>Seconds</td><td>431.43</td><td>1758.32</td><td>8.79</td><td>5.36</td><td>2209.7</td></tr><tr><td># Rules</td><td>49,660</td><td>378</td><td>37</td><td>36</td><td></td></tr><tr><td rowspan="2">SD</td><td>Seconds</td><td>3528.3</td><td> $185687^§$ </td><td>19542.2</td><td>1031.1</td><td>209788.8</td></tr><tr><td># Rules</td><td>5582 k</td><td>1097 k</td><td>106 k</td><td>32881</td><td></td></tr></table>

<sup>§</sup>Time estimated based on the average pattern search speed.

System runtime decomposition for SQLP, PALP, and CLAP to answer query $Q _ { 4 } =$ {S S S S 0.5%} in Table 4.  
Runtime decomposition for PALP. The system runtime mainly consists of: (1) the maximum FP tree mining from $S _ { 1 } , S _ { 2 } , S _ { 3 } ,$ and $S _ { 4 } \mathrm { : }$ and (2) pattern comparison at the master site.

<table><tr><td colspan="2">Databases</td><td> $S_1$ </td><td> $S_2$ </td><td> $S_3$ </td><td> $S_4$ </td><td>Master</td><td>System runtime</td></tr><tr><td rowspan="2">WS</td><td>Seconds</td><td>431.43</td><td>194.81</td><td>190.35</td><td>39.92</td><td>100.40</td><td>531.83</td></tr><tr><td># Rules</td><td>49,660</td><td>75,651</td><td>225,415</td><td>17,819</td><td>368,545</td><td></td></tr><tr><td rowspan="2">SD</td><td>Seconds</td><td>3528.3</td><td>1356.4</td><td>719.6</td><td>393.8</td><td>1744.0</td><td>5283.39</td></tr><tr><td># Rules</td><td>5582 k</td><td>6230 k</td><td>6137 k</td><td>4836 k</td><td>22785 k</td><td></td></tr></table>

Table 8 summarizes the overall performance of three frameworks for different databases and threshold values. The simple summary concludes that CLAP is suitable for any types of data and parameter settings. PALP is mostly effective if the support values are large, but deteriorates signi<sup>fi</sup>cantly for small support values (due to its selfcontained mining nature). SQLP is the least attractive choice for mining distributed databases,

## 7. Conclusions

In this paper, we advocated that the essential goal for distributed pattern mining, from an association rule mining perspective, is to discover local, global, and inter patterns (namely L-, G-, and Ipatterns). We argued that existing research mainly focuses on L- and G-pattern discovery, and has left I-pattern mining inadequately addressed, where single database oriented pattern pruning is essentially ineffective. More importantly, no existing framework is able to support the mining of all three types of patterns. We therefore proposed a distributed mining framework, namely collaborative pattern mining (CLAP), which is fully distributed with capability for cross-database pruning. The CLAP distributed mining framework has very little privacy concerns and requires low computational costs and memory consumption. Experimental comparisons demonstrated that CLAP signi<sup>fi</sup>cantly outperforms other simple methods.

The problem addressed in this paper mainly focuses on frequent item-set mining. However, the distributed mining framework and the cross-database pruning principles can be extended to handle other patterns, such as constrained frequent item-sets, closed frequent patterns, and sequential patterns.

System runtime decomposition for SQLP, PALP, and CLAP to answer query $Q _ { 4 } =$ {S ≥S ≥S ≥S ≥0.5%} in Table 4.  
Runtime decomposition for CLAP. The system runtime mainly consists of: (1) constructing bloom <sup>fi</sup>lters containing length-l patterns for each site; and (2) the maximum collaborative mining time on a site. (l=3).

<table><tr><td colspan="2">Databases</td><td> $BF_{1\_l}$ </td><td> $BF_{2\_l}$ </td><td> $BF_{3\_l}$ </td><td> $BF_{4\_l}$ </td><td> $CLAP(S_1)$ </td><td>System runtime</td></tr><tr><td rowspan="2">WS</td><td>Seconds</td><td>405.94</td><td>164.29</td><td>87.84</td><td>30.93</td><td>5.84</td><td>411.78</td></tr><tr><td># Rules</td><td>958</td><td>2308</td><td>2829</td><td>1831</td><td>141</td><td></td></tr><tr><td rowspan="2">SD</td><td>Seconds</td><td>51.08</td><td>26.21</td><td>14.28</td><td>7.95</td><td>448.43</td><td>499.51</td></tr><tr><td># Rules</td><td>30181</td><td>29493</td><td>30147</td><td>30301</td><td>40721</td><td></td></tr></table>

Table 7  
Query runtime comparison on $Q _ { l } , Q _ { 2 } ,$ , and $Q _ { 3 }$ in Table 4 $: ( \alpha = 0 . 5 \% , \beta = 0 . 0 1 \% ) ,$ , a dash line indicates that a speci<sup>fi</sup>c method is not capable of answering the query.

<table><tr><td rowspan="2">Frameworks</td><td colspan="3">WS</td><td colspan="3">SD</td></tr><tr><td> $Q_1$ </td><td> $Q_2$ </td><td> $Q_3$ </td><td> $Q_1$ </td><td> $Q_2$ </td><td> $Q_3$ </td></tr><tr><td>SQLP</td><td>859.52</td><td>-</td><td>-</td><td>6030.17</td><td>-</td><td>-</td></tr><tr><td>PALP</td><td>435.21</td><td>-</td><td>-</td><td>3531.30</td><td>-</td><td>-</td></tr><tr><td>CLAP</td><td>407.24</td><td>478.53</td><td>778.69</td><td>706.32</td><td>3604.02</td><td>4339.11</td></tr></table>

## Table 8

The niche of the three mining frameworks. $" + " , ~ " - " ,$ and $" \sim$ denotes that the framework in a speci<sup>fi</sup>c row is effective, ineffective, or partially effective for conditions listed in the corresponding column.

<table><tr><td rowspan="2">Frameworks</td><td colspan="2">Strong dense databases</td><td colspan="2">Weak sparse databases</td></tr><tr><td>Small α</td><td>Large α</td><td>Small α</td><td>Large α</td></tr><tr><td>SQLP</td><td>-</td><td>~</td><td>-</td><td>~</td></tr><tr><td>PALP</td><td>-</td><td>+</td><td>-</td><td>+</td></tr><tr><td>CLAP</td><td>+</td><td>+</td><td>+</td><td>+</td></tr></table>

## Acknowledgments

This research is supported in part by Australian Research Council (ARC) Future Fellowship under grant No. FT100100971, ARC Discovery Project under grant No. DP1093762, National Science Foundation of China Innovative Grant (70921061), and by the CAS/SAFEA International Partnership Program for Creative Research Teams.

## References

[1] R. Agrawal, J.C. Shafer, Parallel mining of association rules, IEEE Transactions on Knowledge and Data Engineering 8 (6) (December 1996) 962–969.

[2] R. Agrawal, R. Srikant, Fast algorithms for mining association rules, Proc. of VLDB Conference, 1994.

[3] M. Aounallah, G. Mineau, Distributed data mining: why do more than aggregating models, Proc. of IJCAI Conference, 2007, pp. 2645–2650.

[4] M. Ashra<sup>fi</sup>, D. Taniar, K. Smith, ODAM: an optimized distributed association rule mining algorithm, IEEE Distributed Systems Online 5 (3) (2004).

[5] S. Bay, M. Pazzani, Detecting group differences: mining Contrast sets, Data Mining and Knowledge Discovery 5 (3)(2001) 213–246

[6] S. Bhattacharyya, S. Jha, K. Tharakunnel, J. Westland, Data mining for credit card fraud: a comparative study, Decision Support Systems 59 (3) (2011) 602–613.

[7] A. Border, M. Mitzenmacher, Network applications of bloom <sup>fi</sup>lters: a survey, Proc. of the 40th Annual Allerton Conf. on Communication, Control, and Computing, Urbana-Champaign, Illinois, 2002, pp. 636–646.

[8] C. Bucila, J. Gehrke, D. Kifer, W. Whote, DualMiner: a dual-pruning algorithm for itemsets with constraint, Proc. of ACM SIGKDD Conference, 2002.

[9] G. Buehrer, S. Parthasarathy, S. Tatikonda, T. Kurc, J. Saltz, Toward terabyte pattern mining: an architecture-conscious solution, Proc. of the 12th ACM SIGPLAN symposium on Principles and practice of parallel programming, 2007.

[10] B. Chazelle, J. Kilian, R. Rubinfeld, A. Tal, The Bloomier <sup>fi</sup>lter: an ef<sup>fi</sup>cient data structure for static support lookup tables, Proc. of the 5th ACM-SIAM Symposium on Discrete Algorithms, 2004, pp. 30–39.

[11] B. Chen, L. Chen, Y. Lin, R. Ramakrishnan, Prediction cubes, Proc. of the 31st VLDB Conference, Norway, 2005.

[12] D. Cheung, V. Ng, A. Fu, Y. Fu, Ef<sup>fi</sup>cient mining of association rules in distributed databases, IEEE Trans. on Knowledge and Data Engineering 8 (1996).

[13] S. Cohen, Y. Matias, Spectral bloom <sup>fi</sup>lters, Proc. of SIGMOD Conference, 2003, pp. 241–252.

[14] S. Datta, C. Giannella, H. Kargupta, K-means clustering over a large, dynamic network, Proc. of 2006 SIAM Conference on Data Mining, April 2006.

[15] G. Dong, J. Li, Ef<sup>fi</sup>cient mining of emerging patterns: discovering trends and differences, Proc. of the 5th ACM SIGKDD Conference, 1999.

[16l L Fan P Cao I Almeida A Broder Summary cache: a scalable wide-area web cache sharing protocol, IEEE/ACM Trans. on Networking 8 (3) (2000) 281–293.

[17] W. Fujibuchi, T. Kato, Classi<sup>fi</sup>cation of heterogeneous microarray data by maximum entropy kernel, BMC:Bioinformatics (267) (2007) 8.

[18] A. Gionis, H. Mannila, P. Tsaparas, Clustering aggregation, Proc. of the 21st ICDE Conference, 2005.

[19] A. D'Costa, V. Ramachandran, A. Sayeed, Distributed classi<sup>fi</sup>cation of Gaussian space-time sources in wireless sensor networks, IEEE Journal on Selected Areas in Communications 22 (6) (2004) 1026–1036.

[20] X. Gong, W. Qian, Y. Yan, A. Zhou, Bloom <sup>fi</sup>lter-based XML packets <sup>fi</sup>ltering for millions of path queries, Proc. of ICDE Conference, 2005, pp. 890–901.

[21] J. Gray, A. Bosworth, A. Layman, H. Pirahesh, Data cube: a relational aggregation operator generalizing group-by, cross-tab, and sub-total, Proc. of the 12th ICDE Conference, 1996, pp. 152–159.

[22] R. Grossman, A top-ten list for data mining, SIAM News 34 (5) (2001).

[23] E. Han, G. Karypis, V. Kumar, Scalable parallel data mining for association rules, Proc. of ACM SIGMOD Conference, 1997.

[24] J. Han, J. Pei, Y. Yin, Mining frequent patterns without candidates generation, Proc. of ACM SIGMOD Conf., 2000.

[25] [25] IBM Quest Data Mining Project. Quest synthetic data generation code, http:// www.cs.loyola.edu/\~cgiannel/assoc\_gen.html.

[26] [26] IPUMS: Integrated Public Use Microdata Series, http://www.ipums.umn.edu/ usa/index.html.

[27] X. Ji, J. Bailey, G. Dong, Mining minimal distinguishing subsequence patterns with gap constraints, Proc. of ICDM Conference, 2005.

[28] R. Jin, G. Agrawal, A systematic approach for optimizing complex mining tasks on multiple databases Proc, of ICDE Conference 2006.

[29] M. Kantarcioglu, C. Clifton, Privacy-preserving distributed mining of association rules on horizontally partitioned data, Proc. of ACM SIGMOD Workshop on Research Issues on Data Mining and Knowledge Discovery (DMKD'02), June 2002.

[30] [31] H. Kargupta et al., Distributed association rule mining bibliography, http:// www.cs.umbc.edu/\~hillol/DDMBIB/ddmbib\_html/DistAss.html

[31] H. Kargupta, B.H. Park, D. Hershberger, E. Johnson, Collective data mining: a new perspective toward distributed data mining, Advances in Distributed and Parallel Knowledge Discovery, MIT/AAAI Press. Cambridge, MA. 1999.

[32] T. Li, M. Ogihara, S. Zhu, Association-based similarity testing and its applications, Intelligent Data Analysis 7 (3) (2003) 209–232.

[33] S. Li, T. Wu, W. Pottenger, Distributed higher order association rule mining using information extracted from textual data, ACM SIGKDD Explorations 7 (1) (2005).

[34] P. Luo, H. Xiong, K. Lü, Z. Shi, Distributed classi<sup>fi</sup>cation in peer-to-peer networks, Proc. Of ACM KDD, 2007, pp. 968–976.

[35] A. Manjhi, V. Shkapenyuk, K. Dhamdhere, C. Olston, Finding (recently) frequent items in distributed data streams, Proc. of ICDE Conference, 2005

[36] S. Merugu, J. Ghosh, A distributed learning framework for heterogeneous data sources, Proc. of the 11th ACM KDD Conference, 2005.

[37] M. Otey, A. Veloso, C. Wang, S. Parthasarathy, W. Meira, Mining frequent itemsets in distributed and dynamic databases, Proc. of ICDM Conference, 2003.

[39] S. Parthasarathy, M. Ogihara, Exploiting dataset similarity for distributed mining, Proc. of High Performance Data Mining Workshop, 2000.

[40] A. Partow, Open Bloom FilterSource code download:, http://bloom.googlecode. com/syn-history/r5/trunk/bloom. filter.h 2000.

[41] [41] K. Peeters, Tree.hh: an STL-like C++ tree class, http://www.aei.mpg.de \~peekas/tree/ September 2009.

[42] [42] F. Provost, Distributed data mining: scaling up and beyond. In Kargupta, H., Chan, P., eds.: Advances in Distributed and Parallel Knowledge Discovery, MIT/ AAAI Press, 2000.

[43] L. Qiu, Y. Li, X. Wu, Preserving privacy in association rule mining with bloom filters, Journal of Intelligent Information Systems 29 (3) (2007) 253–278

[44] A. Schuster, R. Wolff, Communication-ef<sup>fi</sup>cient distributed mining of association rules, Data Mining and Knowledge Discovery 8 (2) (2004) 171–196

[46] J. Sun, S. Papadimitriou, C. Faloutsos, Distributed pattern discovery in multiple streams, Proc. of PAKDD Conference, 2006, pp. 713–718.

[47] D. Tsur, J.D. Ullman, S. Abitboul, C. Clifton, R. Motwani, S. Nestorov, Query <sup>fl</sup>ocks: a generalization of association-rule mining, Proc. of ACM-SIGMOD Conference, 1998.

[48] J. Wang, H. Zeng, Z. Chen, H. Lu, L. Tao, W. Ma, ReCoM: reinforcement clustering of multi-type interrelated data objects, Proc. of SIGIR Conference, 2003, pp. 274–281.

[49] G. Webb, S. Butler, D. Newlands, On detecting differences between groups, Proc. of the 9th ACM SIGKDD Conference, 2003.

[50] X. Wu, S. Zhang, Synthesizing high-frequency rules from different data sources, IEEE Transactions on Knowledge and Data Engineering 15 (2) (2003) 353–367.

[51] K. Xu, S. Liao, J. Li, Y. Song, Mining comparative opinions from customer reviews for competitive intelligence, Decision Support Systems 50 (4) (2011) 743–754.

[52] Y. Yang, X.D. Wu, X. Zhu, Conceptual equivalence for contrast mining in classi<sup>fi</sup>cation learning, Data and Knowledge Engineering 67 (3) (2008) 413–429.

[53] X. Yin, J. Han, P. Yu, Crossminer: ef<sup>fi</sup>cient classi<sup>fi</sup>cation across multiple database relations, Proc. of ICDE Conference, 2004.

[54] M. Zaki, Parallel and distributed association mining: a survey, IEEE Concurrency 7 (4) (1999).

[55] S. Zhang, M. Zaki, Mining multiple data sources: local pattern analysis, Data Mining and Knowledge Discovery 12 (2–3) (2006) 121–125.

[56] T. Zhang, R. Ramakrishnan, M. Linvy, BIRCH: an ef<sup>fi</sup>cient data clustering method for very large databases, Proc. of ACM SIGMOD Conference, 1996.

[57] S. Zhang, C. Zhang, X. Wu, Knowledge discovery in multiple database, Springer, 2004.

[58] P. Zhang, X. Zhu, Y. Shi, L. Guo, X. Wu, Robust ensemble learning for mining noisy data streams Decision Support Systems 50 (2) (2011) 469–479

[59] X. Zhu, R. Jin, Multiple information source cooperative learning, Proc. of 21st International Joint Conference on Arti<sup>fi</sup>cial Intelligence, 2009, pp. 1369–1376.

[60] X. Zhu, X. Wu, Discovering relational patterns across multiple databases, Proc. of ICDE Conference, 2007.

[61] X. Zhu, R. Jin, Y. Breitbart, G. Agrawal, MMIS-07, 08: mining multiple information sources workshop report, ACM SIGKDD Explorations 10 (2) (2008) 61–65.

Xingquan Zhu received his Ph.D degree in Computer Science from Fudan University, Shanghai China, in 2001. He is a recipient of the Australia ARC Future Fellowship and a Professor of the Centre for Quantum Computation & Intelligent Systems, Faculty of Engineering and Information Technology, University of Technology, Sydney (UTS), Australia. Before joining the UTS, he was a tenure track Assistant Professor in the Department of Computer Science & Engineering, Florida Atlantic University, Boca Raton FL, USA (2006–2009), a Research Assistant Professor in the Department of Computer Science, University of Vermont, Burlington VT, USA (2002–2006), and a Postdoctoral Associate in the Department of Computer Science, Purdue University, West Lafayette IN, USA (2001–2002). Dr. Zhu's research mainly focuses on data mining, machine learning, and multimedia systems. Since 2000, he has published more than 110 referred journal and conference proceedings papers in these areas. Dr. Zhu is an Associate Editor of the IEEE Transactions on Knowledge and Data Engineering (2009-), a Program Committee Co-Chair for the 23rd IEEE International Conference on Tools with Arti<sup>fi</sup>cial Intelligence (ICTAI 2011), and a Program Committee Co-Chair for the 9th International Conference on Machine Learning and Applications (ICMLA 2010).

Bin Li received his PhD degree in Computer Science from Fudan University, Shanghai China, in 2009. He is a Postdoctoral Research Fellow at the Faculty of Engineering and Information Technology, University of Technology, Sydney (UTS), Australia. Before joining the UTS, he worked as a research fellow at the Institut TELECOM SudParis, France. Dr Bin Li's research interests include Machine Learning and Data Mining as well as their applications to Web and Knowledge-based Information Systems and Social Media Mining.

Xindong Wu is a Professor of Computer Science at the University of Vermont (USA), and a Fellow of the IEEE. He holds a PhD in Arti<sup>fi</sup>cial Intelligence from the University of Edinburgh, Britain. His research interests include data mining, knowledge-based systems, and Web information exploration. He has published over 200 refereed papers as well as 25 books and conference proceedings in these areas. His research has been supported by the U.S. National Science Foundation (NSF), the U.S. Department of Defense (DOD), the National Natural Science Foundation of China (NSFC), and the Chinese Academy of Sciences, as well as industrial companies including Microsoft Research US. West Advanced Technologies and Empact Solutions

Dr. Wu is the founder and current Steering Committee Chair of the IEEE International Conference on Data Mining (ICDM), the founder and current Editor-in-Chief of Knowledge and Information Systems (KAIS, by Springer), the Founding Chair (2002- 2006) of the IEEE Computer Society Technical Committee on Intelligent Informatics (TCII), and a Series Editor of the Springer Book Series on Advanced Information and Knowledge Processing (AI&KP). He was the Editor-in-Chief of the IEEE Transactions on Knowledge and Data Engineering. He served as Program Committee Chair/Co-Chair for the 2003 IEEE International Conference on Data Mining, the 13th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, and the 19th ACM Conference on Information and Knowledge Management.

Dan He is a Ph.D student in the Computer Science Department, University of California, Los Angles. He received his Master's degree from the University of Vermont in 2005. Hi research mainly focuses on pattern mining from sequence databases and Bioinformatics.

Chengqi Zhang received the PhD degree from Queensland University in 1991, followed by a Doctor of Science (DSc-Higher Doctorate) from Deakin University in 2002. He has been a research professor in information technology at The University of Technology, Sydney (UTS) since December 2001. He is currently the director of the UTS Research Centre for Quantum Computation and Intelligent Systems. In addition, he is the leader of the data mining program at the Australian Capital Market Cooperative Research Centre. Dr. Zhang's research interests mainly focus on data mining and its applications, especially domain driven data mining, negative association rule mining, and multidatabase mining. He has published more than 200 research papers, including several in <sup>fi</sup>rst-class international journals, such as Arti<sup>fi</sup>cial Intelligence and IEEE and ACM Transactions. He has delivered 12 keynote/invited speeches at international conferences over the last six years. He has been chairman of the Australian Computer Society National Committee for Arti<sup>fi</sup>cial Intelligence since November 2005. He is a fellow of the Australian Computer Society (ACS) and a senior member of the IEEE Computer Society. His personal web page can be found at: http://www-staff.it.uts.edu.au/ \~chengqi/.
