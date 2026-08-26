---
otero_id: 7870
otero_key: "4W5NR3J3"
title: "A change detection method for sequential patterns"
authors: "Chieh-Yuan Tsai; Yu-Chen Shieh"
year: "2009"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2008.09.003"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A change detection method for sequential patterns

Chieh-Yuan Tsai ⁎, Yu-Chen Shieh

Department of Industrial Engineering and Management, Yuan Ze University, Taiwa

a r t i c l e i n f o

Article history: Received 29 August 2007 Received in revised form 4 September 2008 Accepted 15 September 2008 Available online 25 September 2008

Keywords: Sequential patterns Change mining Pattern matching Customer behaviors

## a b s t r a c t

Recent trends in customer-oriented markets drive many researchers to develop sequential pattern mining algorithms to explore consumer behaviors. However, most of these studies concentrated on how to improve accuracy and ef<sup>fi</sup>ciency of their methods, and seldom discussed how to detect sequential pattern changes between two time-periods. To help business managers understand the changing behaviors of their customers, a three-phase sequential pattern change detection framework is proposed in this paper. In phase I, two sequential pattern sets are generated respectively from two time-period databases. In phase II, the dissimilarities between all pairs of sequential patterns are evaluated using the proposed sequential pattern matching algorithm. Based on a set of judgment criteria, a sequential pattern is clari<sup>fi</sup>ed as one of the following three change types: an emerging sequential pattern, an unexpected sequence change, or an added/ perished sequential pattern. In phase III, signi<sup>fi</sup>cant change patterns are returned to managers if the degree of change for a pattern is large enough. A practical transaction database is demonstrated to show how the proposed framework helps managers to analyze their customers and make better marketing strategies.

© 2008 Elsevier B.V. All rights reserved.

## 1. Introduction

Sequential pattern mining is the technique that explores frequently occurring patterns related to time from a large-scale database. It has been applied to web log mining [5], customer purchase behavior analysis [10], DNA sequence analysis [11], project team coordination [22], retailing management [8], and so on. Previous studies related to sequential pattern mining mainly focused on how to build accurate models or how to discover interesting rules in ef<sup>fi</sup>cient ways. AprioriAll [1], GSP [29], Pre<sup>fi</sup>xSpan [27], FFS [32], and SPAM [3] are some well known algorithms that ef<sup>fi</sup>ciently identify sequential patterns. In addition, other efforts have concentrated on sequential pattern mining in multi-databases [18] with constraints [7], time-intervals [9], and fuzzy sets [6]. Relatively few attempts have been made to analyze sequential pattern changes in databases collected over time [19]. However, some popular patterns at one time-period may not be valid in another time-period [4]. For example, the sequential pattern “Computer→Memory→Color\_Printer” is frequent in the last year. However, this pattern might not be popular in this year but change to “Computer→Memory→Multifunctional\_Printer.” If managers cannot capture this dynamic behavior change in time and provide appropriate products or services to their customer, customer attrition will be unavoidable.

There have been many existing works focusing on dynamic aspects or comparison between two different datasets. They can be broadly classi<sup>fi</sup>ed as four research trends [4,23,28]. The <sup>fi</sup>rst trend is to improve rule matching accuracy when new transaction data are constantly added to the original transaction database. El-Sayed et al. [14] introduced an ef<sup>fi</sup>cient strategy for discovering frequent patterns in sequence databases that requires only two scans of the database. Koh and Shieh [17] proposed an algorithm of AFPIM (Adjusting FP-tree for Incremental Mining) based on adjusting FP-tree structures to maintain frequent itemsets discovered in a changing database. The algorithm only scans changed data in the database, and adjusts FP-tree structures to enhance the ef<sup>fi</sup>ciency of mining association rules. Masseglia et al. [24] proposed an ef<sup>fi</sup>cient algorithm, called incremental sequence extraction (ISE), to compute frequent sequences in an updated database. The algorithm minimizes computational costs by re-using the minimal information from the original database. Lee et al. [21] proposed a SWF (sliding-window <sup>fi</sup>ltering) algorithm, which uses a <sup>fi</sup>ltering thresho ld to deal with the candidate itemset generation. The algorithm has not only signi<sup>fi</sup>cantly reduced I/O and CPU costs but also effectively controlled memory utilization. The second research trend is to discover emerging patterns. Emerging pattern mining gauges signi<sup>fi</sup>cant changes or differences from one database to another [12]. Fan and Ramamohanarao [15] developed an algorithm which applied the minimum support, the minimum growth rate and chi-squared values to extract interesting emerging patterns. Terlecki and Walczak [30] presented the relations between rough set and jumping emerging patterns. They proposed practical applications of these observations to the minimal reduced problem and to test whether a given attribute set is differentiating.

The third research trend is subjective interestingness mining. Interestingness mining is used to <sup>fi</sup>nd unexpected rules with respect to the user's existing knowledge. Padmanabhan and Tuzhilin [25] developed methods to generate unexpected patterns with respect to managerial intuition by eliciting managers' beliefs about the domain and used these beliefs to seed the search for unexpected patterns in data. The methods provide managers with more relevant patterns from data and aid in effective decision making. Liu et al. [23] proposed a new approach to assist users in <sup>fi</sup>nding interesting rules from discovered association rules and analyze subjective interestingness. The approach <sup>fi</sup>rst asks users to specify his/her existing knowledge such as beliefs or concepts, and then analyzes the discovered association rules to conformity and various interestingness criteria. Padmanabhan and Tuzhilin [26] presented a method for discovering unexpected patterns in data. The method combines independent concepts of minimality and unexpectedness to discover a minimal set of unexpected patterns. Lanquillon [20] proposed the concepts of added rules and perished rules. An added rule is the rule that is hard to be found in the past database, while a perished rule is the rule that is dif<sup>fi</sup>cult to be found in the present database.

The fourth research trend is to discover regularity from time series data. Han et al. [16] presented several algorithms for ef<sup>fi</sup>cient mining of partial periodic patterns by exploring some interesting properties related to partial periodicity. The algorithms shows that mining partial periodicity needs only two scans over a time series database to ef<sup>fi</sup>ciently mine long periodic patterns. Yu et al. [31] proposed a granulation-based method to <sup>fi</sup>nd similarities between two time series. The granulation-based method deals with problematic temporal data mining tasks such as similar subsequence searching, clustering and indexing etc. Altiparmark et al. [2] proposed a novel approach for information mining between time series data. They utilized frequent itemset mining as well as clustering and declustering techniques with novel distance metrics for measuring similarities between items series data.

Although these researches can ef<sup>fi</sup>ciently detect the dynamic changes between two datasets, their discussions are limited to association rules only. None of them discusses the change of sequential patterns in two time-periods. To bridge the gap, this study proposes a change detection framework to observe the dynamic alternation of sequential patterns between two time-periods. The rest of this paper is organized as follows. Section 2 de<sup>fi</sup>nes the dissimilarity measurement for sequential patterns. Section 3 details each phase of the proposed change detection framework. With the framework, a sequential pattern can be classi<sup>fi</sup>ed as one of the three change types: an emerging sequential pattern, an unexpected sequence change, or an added/perished sequential pattern. Section 4 provides an implementation case to demonstrate the bene<sup>fi</sup>t of the proposed framework. A summary and future perspective for the study is concluded in Section 5.

## 2. The dissimilarity measurement for sequential patterns

In this section, a formal representation for sequential patterns is illustrated <sup>fi</sup>rst. Then, the dissimilarity measurement for two sequential patterns in different time-periods is de<sup>fi</sup>ned. The measurement is then derived using the proposed sequential pattern matching algorithm. Finally, the minimal difference value between one and a set of sequential patterns are formulated.

## 2.1. Sequential patterns

Let $I = \{ i _ { 1 } , i _ { 2 } , . . . , i _ { n } \}$ be a set of items. An itemset is a non-empty set of items. A sequence is an ordered list of itemsets, represented as $< S _ { 1 } S _ { 2 } . . . . S _ { l } >$ where $s _ { j }$ is an itemset, $\mathrm { i . e . , } s _ { j } \subseteq I \mathrm { f o r } 1 \leq j \leq l . s _ { j }$ is also called an element of the sequence and denoted as $\left( x _ { 1 } x _ { 2 } . . . x _ { m } \right)$ where $x _ { k } \in I$ for 1≤k≤m. The number of instances of items in a sequence is called the length of the sequence. A sequence with length l is called a l-sequence. A sequence $a { = } { < } a _ { 1 } a _ { 2 } { \ldots } a _ { n } { > }$ is called a subsequence of $b { = } { < } b _ { 1 } b _ { 2 } { \ldots } b _ { m } { > }$ , and b is called a super sequence of a, denoted as $a \subseteq b ,$ if there exist integers $1 \leq j _ { 1 } < j _ { 2 } < \ldots < j _ { n } \leq m$ such that $a _ { 1 } \subseteq b _ { j 1 } , a _ { 2 } \subseteq b _ { j 2 } ,$ $a _ { n } \subseteq b _ { j _ { n } } .$ A sequence database $D$ is a set of tuples bsid, $S > ,$ , where sid is a sequence-id and s is a sequence. A tuple bsid, sN is said to contain a sequence $a ,$ if a is a subsequence of $\mathit { \Pi } _ { \left\{ s , \right. } $ i.e., a⊆s. The number of tuples in a sequence database D containing sequence a is called the support of $a ,$ denoted as Sup(a)1. Given a sequence database D and user speci<sup>fi</sup>ed minimum support $\gamma _ { \mathrm { { m i n } } } ,$ a sequence a is a sequential pattern in $D \operatorname { i f } \operatorname { S u p } ( a ) { \geq } \gamma _ { \operatorname* { m i n } } .$ . The sequential pattern mining problem is to <sup>fi</sup>nd the complete set of sequential patterns with respect to D and γ<sub>min</sub>.

## 2.2. Dissimilarity measurement

Let $D ^ { t }$ and $D ^ { t + k }$ be the databases (or datasets) at time-period t and t+k respectively, where $D ^ { t }$ and $D ^ { t + k }$ are disjoint. S<sup>t</sup> and $S ^ { t + k }$ represent the discovered sequential pattern sets from $D ^ { t }$ and $D ^ { t + k }$ respectively. s<sup>t</sup>and $s _ { j } ^ { t + k }$ indicate individual sequential patterns in the corresponding sequential pattern sets $S ^ { t }$ and $S ^ { t + \hat { k } }$ respectively, where $\displaystyle i = 1 , 2 , . . . , | S ^ { t } |$ and $j = \bar { 1 } , 2 , . . . , | S ^ { t ^ { + } k } |$ . Sup(s<sup>t</sup>) represents the support of s<sup>t</sup> in $D ^ { t }$ and $\mathsf { S u p } ( s _ { j } ^ { t + k } )$ represents the support of $s _ { j } ^ { t + k }$ in $D ^ { t + k }$

The dissimilarity between s<sup>t</sup> in $S ^ { t }$ and $s _ { i } ^ { t + k }$ in $S ^ { t + k }$ is de<sup>fi</sup>ned based on the following three considerations. First, the higher the number of mismatched elements between s<sup>t</sup> and $s _ { j } ^ { t + k }$ is, the higher the dissimilarity is. For instance, we have s<sup>t</sup>: $\stackrel { \cdot } { A }  B  C  D$ and $s _ { i + 1 } ^ { t } \colon A \to$ $B {  } C {  } D$ →E in $S ^ { t } ,$ and s<sup>t</sup> <sup>+</sup> <sup>k</sup> <sub>j</sub> : A→B→C→D→E→F in $S ^ { t + k }$ . When $s _ { i } ^ { t { + } k }$ is compared with $s _ { j , } ^ { t }$ there are two among the six elements mismatched $( 2 / 6 ) .$ . However, when $s _ { j } ^ { t + k }$ is compared with $s _ { i + 1 } ^ { t } ,$ only one among six elements are mismatched $( 1 / 6 )$ . It is reasonable to claim that the dissimilarity between s<sup>t</sup> and $s _ { j } ^ { t + k }$ is greater than the dissimilarity between $S _ { i + 1 } ^ { t }$ and $s _ { j } ^ { t + k }$

Second, the position of the element changed in a sequence is taken into consideration based on the following observation. Assume that we have a sequence s and a sequential pattern set D. To predict what element(s) will appear after s, we will match the elements in s with the pre<sup>fi</sup>x elements of all patterns in D. For example, $D =$ $\{ ^ { \mathrm { u } } \mathrm { A } \to \mathrm { B } \to \mathrm { C } \to \mathrm { D } ^ { \mathrm { v } } , ^ { \mathrm { ~ } \mathrm { u } } \mathrm  \to \mathrm { B } \to \mathrm { C } \to \mathrm { E } ^ { \mathrm { v } } , ^ { \mathrm { ~ } \mathrm { u } } \mathrm { A } \to \mathrm { B } \to \mathrm { F } \to \mathrm { G } ^ { \mathrm { v } } , ^ { \mathrm { ~ } \mathrm { u } } \mathrm  \to \mathrm { B } \to \mathrm { H } \mathrm { \to \mathrm { J } ^ { \mathrm { v } } } \}$ . If $s { = } ^ { \mathfrak { u } } \mathsf { A } { \to } \mathsf { B } { \to } \mathsf { C } ^ { \prime \prime }$ , the patterns $ { { } ^ { \circ } } \mathsf { A } \to \mathsf { B } \to \mathsf { C } \to \mathsf { D } ^ { \prime \prime }$ and $ { { } ^ { \circ } } \mathsf { A }  {  } \mathsf { B }  {  } \mathsf { C }  {  } \mathsf { E } ^ { \prime \prime }$ are matched. Thus, two elements (subsequences) $\ " \mathrm { D } ^ { \prime \prime } \mathrm { O r } \ \mathrm { \Lambda } ^ { \ast } \mathrm { E } ^ { \prime \prime }$ could appear next if s is inputted. On the other hand, if $S = \ ^ { \ast } \mathsf { A } \longrightarrow \mathsf { B } ^ { \prime \prime } ,$ , the patterns $^  { } ^ { 4 } { \mathrm { A } }  { \mathrm { B } }  { \mathrm { C } }  { \mathrm { D } } ^ { { \mathrm { " } } } , { } ^  { } ^ { \alpha } { \mathrm { A } }  { \mathrm { B } }  { \mathrm { C } }  { \mathrm { E } } ^ { { \mathrm { " } } } , { } ^  { } ^ { { \alpha } { \mathrm { A } } }  { \mathrm { B } }  { \mathrm { F } }  { \mathrm { G } } ^ { { \mathrm { " } } } , { } ^  { \alpha } { \mathrm { A } }  { \mathrm { B } }  { \mathrm { H } }  { \mathrm { J } } ^ { { \mathrm { " } } }$ are matched. Thus, four subsequences $^ { \ast } \mathrm { C } \longrightarrow \mathrm { D } ^ { \ast } , ^ { \ast } \mathrm { C } \longrightarrow \mathrm { E } ^ { \ast } , ^ { \ast } \mathrm { F } \longrightarrow \mathrm { G } ^ { \ast } , 0 \mathrm { r } ^ { \ast } \mathrm { H } \longrightarrow \mathrm { J } ^ { \ast }$ could appear next. It is clear that if number of elements in s is fewer, the number of patterns matched is higher. This also implies that the prediction accuracy is low since there are many possible outcomes when s is known. Based on this observation, the change between two patterns appears in the rare position is prefer, because the number of matched elements is more. Therefore, if the element change position from $s _ { i } ^ { t }$ and $s _ { j } ^ { t + k }$ is later than the one from s<sup>t</sup> and ${ s } _ { j + 1 } ^ { t + k } ,$ the dissimilarity between s<sup>t</sup> and $s _ { j } ^ { t + k }$ should be smaller than the dissimilarity between s<sup>t</sup> and $\begin{array} { r } { { s _ { j + 1 } ^ { t + k } } . } \end{array}$ For example, we have s $\vdots A {  } B {  } C {  } D \mathrm { i n } S ^ { t } , s _ { j } ^ { t { + } k } { \mathrel { : } } A {  } B {  }$ $C  E$ and $S _ { j + 1 } ^ { t + k } \colon A { \longrightarrow } B { \stackrel { \textstyle { \cdot } } { \to } } E { \longrightarrow } D \operatorname * { i n } S ^ { t + k } \cdot$ The alternation from s<sup>t</sup> to $s _ { j } ^ { t + k }$ is in position four (three common pre<sup>fi</sup>x elements between $s _ { i } ^ { t }$ and $s _ { j } ^ { t + k } ,$ while the alternation from s<sup>t</sup> and $S _ { j + 1 } ^ { t + k }$ is in position three (two common pre<sup>fi</sup>x elements between s<sup>t</sup> and $S _ { j + 1 } ^ { t + k } )$ . Thus, we claim that the dissimilarity between $s _ { i } ^ { t }$ and $S _ { j } ^ { t + k }$ is smaller than the dissimilarity between s<sup>t</sup> and $\begin{array} { r } { { s _ { j } ^ { t + k } } _ { + 1 \ast } } \end{array}$

Third, the dissimilarity between any mismatched elements should be evaluated. For example, we have s<sup>t</sup>: A→B→C→D in $S ^ { t }$ and $s _ { j } ^ { t + k } \colon$ $A {  } B {  } C {  } E$ and s<sup>t</sup> <sup>+</sup> <sup>k</sup> : $\stackrel { \cdot } { A }  B  C  F \mathrm { i n } S ^ { t + k }$ . In addition, element D contains items $( p , q , x , y , z )$ , element E contains items $( m , p , q , x , y ) ,$ and element F contains items $( m , n , o , q , r )$ . It is obvious that both the change from s<sup>t</sup> to $s _ { j } ^ { t + k }$ and the change from s<sup>t</sup> to $s _ { j } ^ { t + k }$ are one element mismatched. However, the dissimilarity between D in s<sup>t</sup> and F in $S _ { j } ^ { t + k }$ (i.e. one of the same item q) is higher than the dissimilarity between D in s<sup>t</sup> and E in $s _ { j } ^ { t + k }$ (i.e. four of the same items $p , q , x , y ) .$

```txt
Algorithm: Sequential Pattern Matching.
01. Input: Si[m] and Sj[n] // Two sequential patterns with length m and n respectively.
02. for i = 1 to m do
03. C[i][0] = i
04. for j = 1 to n do
05. C[0][j] = j
06. for i = 1 to m do // Starting the sequential pattern matching
07. for j = 1 to n do
08. a1 = 0, a2 = 0, a3 = 0
09. if Sj[i-1] == Si[j-1] then
10. a1 = C[i-1][j-1] // Edit operation: No Change
11. else
12. a1 = C[i-1][j]+1 // Edit operation: Insertion (→)
13. a2 = C[i][j-1]+1 // Edit operation: Deletion (↓)
14. a3 = C[i-1][j-1]+1 // Edit operation: Substitution (↘)
15. C[i][j] = min (a1,a2,a3) // Finish the matrix of edit distance
16. q = max(m, n) // Derive longest sequence q
17. A[q] = C[m][n]
18. for p = q-1 to 1 do // Now trace back and record operation for each position
19. a1 = C[m-1][n] // Edit operation: Insertion (→)
20. a2 = C[m][n-1] // Edit operation: Deletion (↓)
21. a3 = C[m-1][n-1] // Edit operation: Substitution (↘)
22. if a3 <= a1 && a3 <= a2 then
23. A[p] = a3, B[p] = “Sub” // Record the type of operation (substitution)
24. elseif a1 == a2 then
25. if m >= n then
26. A[p] = a2, B[p] = “Del” // Record the type of operation (deletion)
27. else
28. A[p] = a1, B[p] = “Ins” // Record the type of operation (insertion)
29. else
30. A[p] = min (a1,a2,a3)
31. if A[p] = a1 then B[p] = “Ins” // Record the type of operation
32. if A[p] = a2 then B[p] = “Del”
33. if A[p] = a3 then B[p] = “Sub”
34. if B[p] == “Sub” then // Calculates the edit distance for each position
35. if A[p+1] == A[p] then // Edit operation: No Change
36. Cost[p] = 0;
37. else // Edit operation: Substitution (↘)
38. Cost [p] = 1 - itemset_similarity (Si[p], Sj[p])
39. m = m - 1, n = n - 1
40. elseif B[p] == “Del” then // Edit operation: Deletion (↓)
41. Cost [p] = 1
42. n = n - 1
43. else B[p] == “Ins” then // Edit operation: Insertion (→)
```  
Fig. 1. The pseudo-code of the proposed sequential pattern matching algorithm.

Based on the three considerations, the dissimilarity between $s _ { i } ^ { t }$ and $S _ { j } ^ { t + k } , \mathsf { D V } _ { i j } ,$ is formulated in Eq. (1). If the two sequential patterns are exactly the same, $\mathrm { D V } _ { i j }$ will be 0. If all elements in the two sequential patterns are mismatched and all items among any mismatched elements are not the same, $\mathrm { D V } _ { i j }$ is equal to 1.

$$
\mathrm{DV} _ {i j} = \sum_ {p = 1} ^ {l} \left(w _ {p} \times \operatorname{Cost} _ {i, j, p}\right) / \sum_ {p = 1} ^ {l} w _ {p}.\tag{1}
$$

$l { = } \operatorname* { m a x } ( | s _ { i } ^ { t } | , | s _ { j } ^ { t { + } \mathbf { k } } | )$ is the maximal length of sequential patterns s<sup>t</sup>and $\mathbf { \Phi } _ { i } ^ { t + k } ,$ $w _ { p } = \big ( l - p + 1 \big ) / l$ is the penalty weight in position p, and $\mathrm { C o s t } _ { i , j , p }$ is the penalty cost of taking required operations to change element $\dot { I } _ { j , p } ^ { t + k }$ in $S _ { j } ^ { t + k }$ to element $I _ { i , p } ^ { t }$ in s<sup>t</sup>. $\mathrm { C o s t } _ { i , j , p }$ can be evaluated using the proposed sequential pattern matching algorithm which will be introduced in the following section. Note that the penalty weight $w _ { p }$ decreases gradually when p increases.

## 2.3. Sequential pattern matching algorithm

The sequential pattern matching algorithm evaluates the minimal total penalty cost, also called the edit distance or Levenshtein distance, to transform sequential pattern $s _ { j } ^ { t + k }$ into s<sup>t</sup> based on the concepts of dynamic programming [13]. Four basic edit operations of “no change,” “substitution,” “deletion,” and “insertion” are considered during transformation. The penalty cost for taking each “substitution,” “deletion,” and “insertion” operation is set as 1, while the penalty cost for “no change” is 0. The algorithm chooses the operation with the lowest penalty cost in each step unti $S _ { j } ^ { t + k }$ has been transformed to s<sup>t</sup>. If the same penalty cost can be obtained using different operations, the following tie-break rules are followed. First, if any of the three operations generates the same penalty cost, the substitution operation is selected. Second, if the insertion or deletion operation causes the same penalty cost and the length of $s _ { j } ^ { t + k }$ is shorter than the length of s<sup>t</sup>, the insertion operation is selected. Last, if the insertion or deletion operation causes the same penalty cost and the length $\mathrm { o f } s _ { j } ^ { t + k }$ is no shorter than the length of s<sup>t</sup>, the deletion operation is selected. After the penalty cost evaluation is completed, the algorithm returns the set of penalty costs for all positions as the output.

Table 1 Two sequential pattern sets

<table><tr><td>Sequential pattern set</td><td>Sequential pattern</td><td>Support</td></tr><tr><td rowspan="2"> $S^t$ </td><td> $s_1^t: C \to D \to B \to F$ </td><td>2</td></tr><tr><td> $s_2^t: I \to J \to K \to L \to M$ </td><td>3</td></tr><tr><td rowspan="4"> $S^{t+k}$ </td><td> $s_1^{t+k}: C \to D \to B$ </td><td>7</td></tr><tr><td> $s_2^{t+k}: C \to D \to B \to F$ </td><td>6</td></tr><tr><td> $s_3^{t+k}: B \to C \to D \to F \to E$ </td><td>3</td></tr><tr><td> $s_4^{t+k}: E \to A \to G \to H$ </td><td>4</td></tr></table>

Table 2  
The items for each element

<table><tr><td>Element</td><td>Items</td><td>Element</td><td>Items</td></tr><tr><td>A</td><td>a, b, e</td><td>H</td><td>b, e, f, g</td></tr><tr><td>B</td><td>b, e</td><td>I</td><td>a, e, l, p</td></tr><tr><td>C</td><td>a, b, c</td><td>J</td><td>c, f, o, m</td></tr><tr><td>D</td><td>e, f, g</td><td>K</td><td>b, d, h</td></tr><tr><td>E</td><td>b, c, e, f</td><td>L</td><td>a, e</td></tr><tr><td>F</td><td>a, c, d</td><td>M</td><td>c, d, f, m</td></tr><tr><td>G</td><td>c, e, f, g</td><td></td><td></td></tr></table>

Based on the above concept, the penalty cost of taking required edit operations to change element $I _ { j , p } ^ { t + k } \mathrm { i n } \ s _ { j } ^ { t + k }$ to element $I _ { i , p } ^ { t }$ in $s _ { i } ^ { t }$ is summarized as:

$$
\operatorname{Cost} _ {i, j, p} = \left\{ \begin{array}{l l} 0, & \text { if   No   Change } \\ 1, & \text { if   Insertion   or   Deletion } \\ 1 - \operatorname{Sim} \left(I _ {i, p} ^ {t}, I _ {j, p} ^ {t + k}\right), & \text { if   Substitution } \end{array} \right.\tag{2}
$$

where $\mathrm { S i m } ( I _ { i , p } ^ { t } , I _ { j , p } ^ { t + k } )$ is the element similarity between mismatched elements $I _ { j , p } ^ { t + k } \mathrm { i n } \ s _ { j } ^ { t + k }$ and $I _ { i , p } ^ { t }$ in s<sup>t</sup> which can be de<sup>fi</sup>ned as follows:

$$
\operatorname{Sim} \left(I _ {i, p} ^ {t}, I _ {j, p} ^ {t + k}\right) = \frac {\text { NumofComItems } \left(I _ {i , p} ^ {t} , I _ {j , p} ^ {t + k}\right)}{\text { Max } \left(| I _ {i , p} ^ {t} | , | I _ {j , p} ^ {t + k} |\right)}.\tag{3}
$$

$\lvert I _ { i , p } ^ { t } \rvert$ is the number of items in element $I _ { i , p } ^ { t } , | I _ { j , p } ^ { t + k } |$ is the number of items in element $I _ { j , p } ^ { t + k } , \ \mathrm { M a x } ( | I _ { i , p } ^ { t } | , | I _ { j , p } ^ { t + k } | )$ is the maximal number of items between $I _ { i , p } ^ { t }$ and $I _ { j , p } ^ { t + k }$ , NumofComItem $( I _ { i , p } ^ { t } , I _ { j , p } ^ { t + k } )$ is the number of common items between $I _ { i , p } ^ { t }$ and $I _ { j , p } ^ { t + k }$

<table><tr><td>C[i,j]</td><td>null</td><td>C</td><td>D</td><td>B</td><td>F</td></tr><tr><td>null</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td>C</td><td>1</td><td>0</td><td>1</td><td>2</td><td>3</td></tr><tr><td>D</td><td>2</td><td>1</td><td>0</td><td>1</td><td>2</td></tr><tr><td>B</td><td>3</td><td>2</td><td>1</td><td>0</td><td>1</td></tr></table>

(a)  
![](/api/attachments/4W5NR3J3/fulltext/images/984124ca97126da847c46d1d4ca4eb8f0224c42c203e10368fb055b7737188d9.jpg)  
(c)

The pseudo-code of the proposed sequential pattern matching algorithm is summarized in Fig. 1. The input to the algorithm includes two sequential patterns from different time-period databases, and the output is a Cost vector that stores the penalty costs for all positions. The pseudo-code includes two major stages. The <sup>fi</sup>rst stage is to generate the minimal penalty cost matrix, C, as shown from lines 2 to 15. The process starts from the top left of the matrix, traces through the matrix step by step, and stops at the bottom right of the matrix. Another stage as shown in lines 18–45 calculates the penalty costs for all positions. In the second stage, the process starts from the bottom right of the matrix C, traces back the matrix step by step, and stops at the top left of the matrix. After deriving the operation types for all positions, the penalty cost for each position can be derived based on a set of tie-break rules in lines 34 to $4 5 .$ . Note that the itemset\_similarity function at line 38 calculates the similarity of two mismatched elements (itemsets) using the formula in Eq. (3).

## 2.4. Minimal difference

Although the dissimilarity value between s<sup>t</sup> and $S _ { j } ^ { t + k } , \mathsf { D V } _ { i j } ,$ can be derived according to Eq. (1), the number of sequential patterns in $S ^ { t }$ and $S ^ { t + k }$ is large in many cases. The large number of sequential patterns might make change detection trivial if the changes between all pairs of s<sup>t</sup> and $s _ { j } ^ { t + k }$ are discussed. In practice, we are only interesting in the change between s<sup>t</sup> and all sequential patterns in $S ^ { t + k }$ . Therefore, the smallest dissimilarity value between s<sup>t</sup><sub>i</sub> and all sequential patterns in $S ^ { t + k }$ , called minimal difference MD<sup>t</sup>, is de<sup>fi</sup>ned as:

$$
\mathrm{MD} _ {i} ^ {t} = \min \left(\mathrm{DV} _ {i 1}, \mathrm{DV} _ {i 2}, \dots , \mathrm{DV} _ {i | S ^ {t + k} |}\right)\tag{4}
$$

Similarly, the smallest dissimilarity value between $s _ { j } ^ { t + k }$ and all sequential patterns in $S ^ { t } ,$ , called minimal difference $\mathrm { M D } _ { j } ^ { t + k } ,$ , is de<sup>fi</sup>ned as:

$$
\mathrm{MD} _ {j} ^ {t + k} = \min \left(\mathrm{DV} _ {1 j}, \mathrm{DV} _ {2 j}, \dots , \mathrm{DV} _ {| S ^ {t} | j}\right)\tag{5}
$$

2.5. An example

A simple example is demonstrated to show the computation process of the dissimilarity value and minimal difference value.

<table><tr><td>C[i,j]</td><td>null</td><td>C</td><td>D</td><td>B</td><td>F</td></tr><tr><td>null</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td>C</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>D</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>B</td><td>3</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>F</td><td>4</td><td>0</td><td>0</td><td>0</td><td>0</td></tr></table>

(b)

![](/api/attachments/4W5NR3J3/fulltext/images/b8586d358d80b5cce4ef72c84f20d285f5665012c5831c0ea5b20b468cb967b5.jpg)  
(d)  
Fig. 2. The evaluation process of edit distances for s <sup>t</sup> and all $S _ { j } ^ { t + k } \mathrm { i n } S ^ { t + k } ,$

![](/api/attachments/4W5NR3J3/fulltext/images/36f3839fca9d79eb674a1e06d5737c2f09261b4761d6b4e6998975b6438a60c3.jpg)  
Fig. 3. The proposed sequential pattern change detection framework.

Table 1 illustrates two sequential pattern sets discovered from two time-period databases, and Table 2 depicts the items contained in each element. When s<sup>t</sup> is matched with $s _ { 1 } ^ { t + k }$ using the proposed sequential pattern matching algorithm, one insertion operation in the fourth position is required. The matching process is visually shown in Fig. 2 (a). Based on Eqs. (1) and (2), $\begin{array} { r } { \mathrm { D V } _ { 1 1 } \overline { { = \big ( } } \frac { 4 } { 4 } \times 0 + \frac { 3 } { 4 } \times 0 + \frac { 2 } { 4 } \times 0 + \frac { 1 } { 4 } \times 1 \big ) / \overline { { \big ( } } \frac { 4 } { 4 } + } \end{array}$ $\frac { 3 } { 4 } + \frac { 2 } { 4 } + \frac { 1 } { 4 } ) \ = 0 . 1$ . When s<sup>t</sup> is matched with $s _ { 2 } ^ { t + \dot { k } }$ , four “no change” operations are taken as illustrated in Fig. 2(b). Therefore, $\begin{array} { r } { \mathrm { D V } _ { 1 2 } { = } \left( \frac { 4 } { 4 } \times 0 + \frac { 3 } { 4 } \times \right. } \end{array}$ $\textstyle 0 + { \frac { 2 } { 4 } } \times 0 + { \frac { 1 } { 4 } } \times 0 ) / \left( { \frac { 4 } { 4 } } + { \frac { 3 } { 4 } } + { \frac { 2 } { 4 } } + { \frac { 1 } { 4 } } \right) = 0 .$ . When s<sup>t</sup> is matched with $S _ { 3 } ^ { t { + } k } ,$ as shown in Fig. $2 ( \mathsf { c } ) ,$ one deletion operation in the <sup>fi</sup>rst position and two substitution operations in the fourth and <sup>fi</sup>fth positions are conducted. For the two mismatched elements, the similarities between element B (b, e) and element F (a, c, d) is 0/3 and the similarity between F (a, c, d) and E (b, c, e, f) is 1/4. Therefore, $\begin{array} { r } { \mathsf { D V } _ { 1 3 } = [ \underline { { 5 } } \times 1 + \frac { 4 } { 5 } \times 0 + \frac { 3 } { 5 } \times 0 + \frac { 2 } { 5 } \times ( 1 - 0 ) + \frac { 1 } { 5 } \times ~ \left( 1 - \frac { 1 } { 4 } \right) ] / \left[ \frac { 5 } { 5 } + \frac { 4 } { 5 } + \frac { 3 } { 5 } + \frac { 2 } { 5 } + \frac { 1 } { 5 } \right] = 0 . 5 1 6 7 . ~ \mathsf { A } } \end{array}$ similar matching process between s<sup>t</sup> and s is shown in Fig. 2(d), where $\begin{array} { r } { \mathrm { D V } _ { 1 4 } = [ \frac { 4 } { 4 } \times ( 1 - \frac { 2 } { 4 } ) + \ \frac { 3 } { 4 } \times ( 1 - \frac { 1 } { 3 } ) + \frac { 2 } { 4 } \times ( 1 - \frac { 1 } { 4 } ) + \frac { 1 } { 4 } \times ( 1 - \frac { 0 } { 4 } ) ] / [ \frac { 4 } { 4 } + \frac { 3 } { 4 } + \frac { 2 } { 4 } + \frac { 1 } { 4 } ] = 0 . 6 5 } \end{array}$ After all $\mathsf { D V } _ { 1 j }$ are known, MD <sup>t</sup>=min(0.1, 0, 0.5167, $0 . 6 5 ) \ i = 0 .$ . The similar matching procedure is repeated for $s _ { 2 } ^ { t } .$ After s<sup>t</sup> is matched with all sequential patterns in $S ^ { t ^ { + } k }$ , we obtain $\mathrm { D V } _ { 2 1 } { = } 0 . 8 8 9 , \mathrm { D V } _ { 2 2 } { = }$ 0.833, $\mathrm { D V } _ { 2 3 } = 0 . 7 7 2 , \mathrm { D V } _ { 2 4 } = 0 . 7 5 0 ,$ , and MD<sup>t</sup> =min(0.889, 0.833, 0.772, $0 . 7 5 0 ) = 0 . 7 5 .$

## 3. Sequential pattern change detection framework

The proposed sequential pattern change detection framework, as illustrated in Fig. 3, includes three major phases. In phase I, two sequential pattern sets are generated from two different time-period databases respectively using the GSP (Generalized Sequential Patterns) algorithm. In phase II, a sequential pattern is clari<sup>fi</sup>ed as one of the three change types: an emerging sequential pattern, an unexpected sequence change, or an added/perished sequential pattern. In phase III, the sets of signi<sup>fi</sup>cant change patterns for the three types are generated and reported to users for further analysis.

![](/api/attachments/4W5NR3J3/fulltext/images/0fadff4daba0196271a57b18302ce32c97a05567494f7e5a04fbb2e867808a3e.jpg)  
Fig. 4. The pseudo-code of the GSP algorithm.

![](/api/attachments/4W5NR3J3/fulltext/images/1b79fedb476b1f31b86aa388130ac34547a88b01e8e4d65ad10a0351e715fe77.jpg)  
Fig. 5. The relationships among the three change types and the $\beta _ { \mathrm { m i n } }$ value.

## 3.1. Phase I: sequential pattern generation

In phase I, two sequential pattern sets are generated from two time-period databases respectively using the GSP algorithm. The GSP algorithm proposed by Srikant and Agrawal [29] is designed for transaction data, where each sequence is a list of transactions ordered by transaction-time, and each transaction is a set of items. The algorithm <sup>fi</sup>nds all sequences whose support is greater than the userde<sup>fi</sup>ned $\gamma _ { \mathrm { m i n } } .$ The GSP algorithm <sup>fi</sup>nds frequent items at level one. At level two, however, GSP considers two conditions for generating candidates with two items. That is, a candidate sequence with two items can be formed by one element or two elements. After that, the process of level-wise candidate generation is alike to that in the Apriori algorithm except when merging two frequent patterns into a candidate, the items in the same element in any original frequent pattern will also be in the same element in the candidate, and vice versa. The multiple occurrences of a candidate in a sequence contribute only one to the support of the candidate, which would not happen in transaction database. This is the only subtle difference of support counting between Apriori and GSP. The pseudo-code of the GSP algorithm is illustrated in Fig. 4.

## 3.2. Phase II: change type detection

After sequential pattern sets $S ^ { t }$ and $S ^ { t + k }$ are discovered from $D ^ { t }$ and $D ^ { t + k }$ respectively, the dissimilarity value $\mathrm { D V } _ { i j }$ between each pairs of $s _ { i } ^ { t }$ in $S ^ { t }$ and $s _ { j } ^ { t + k }$ in $S ^ { t + k }$ can be derived using Eq. (1). In addition, the smallest dissimilarity value MD<sup>t</sup> $( \mathrm { M D } _ { j } ^ { t + k } )$ between s<sup>t</sup> $( s _ { j } ^ { t + k } )$ and all sequential patterns in $S ^ { t ^ { + k } } ( S ^ { t } )$ can be calculated using Eqs. (4) and (5) respectively. After obtaining these values, a sequential pattern can be classi<sup>fi</sup>ed as one of the three change types: an emerging sequential pattern, an unexpected sequence change, or an added/perished sequential pattern according to the following De<sup>fi</sup>nitions 1–3. Notes that although $\mathrm { D V } _ { i j } ,$ MD<sup>t</sup>, and $\mathrm { M D } _ { j } ^ { t + k }$ can be objectively obtained, the concept of an unexpected sequence change and an added/perished sequential pattern are subjective for each individual. Therefore, a minimum dissimilarity value, denoted as $\beta _ { \mathrm { m i n } } ,$ is proposed to judge whether a sequential pattern is clari<sup>fi</sup>ed as an unexpected sequence change in De<sup>fi</sup>nition $^ 2$ or an added/perished sequential pattern in De<sup>fi</sup>nition 3. Fig. 5 shows the conceptual relationship between β and the three change types. The leftmost point of the line represents the position where the two sequential patterns are “completely the same,” while the rightmost point of the <sup>fi</sup>gure represents the position where two sequential patterns are “completely different.” If the dissimilarity between two sequential patterns is greater than $\beta _ { \mathrm { m i n } } ,$ , the two sequential patterns are “different” and might be classi<sup>fi</sup>ed as an unexpected sequence change. Conversely, if the dissimilarity between two sequential patterns is smaller than or equal to $\beta _ { \mathrm { m i n } } ,$ , the two sequential patterns are “quite different” and might be classi<sup>fi</sup>ed as an added/perished sequential pattern. Note that the $\beta _ { \mathrm { m i n } }$ value is decided by users depending on their needs.

Evaluation standard for each change type

<table><tr><td>Change type</td><td>Evaluation standard</td></tr><tr><td>Emerging sequential pattern</td><td> $DV_{ij}=0$ , and the supports between two sequential patterns are different.</td></tr><tr><td>Unexpected sequence change</td><td> $\beta_{\min}>MD_{i}^{t} (or \beta_{\min}>MD_{j}^{t+k})$  and  $DV_{ij}>0$ </td></tr><tr><td>Added sequential pattern (or Perished sequential pattern)</td><td> $MD_{j}^{t+k}\geq\beta_{\min} (or MD_{i}^{t}\geq\beta_{\min})$ </td></tr></table>

## De<sup>fi</sup>nition 1. Emerging sequential patterns

Sequential pattern $s _ { i } ^ { t }$ is clari<sup>fi</sup>ed as an emerging sequential pattern with respect to sequential pattern $s _ { j } ^ { t + k }$ if $\mathrm { D V } _ { i j } { = } 0$ and the supports between the two sequential patterns are different. Similarly, sequential pattern $s _ { j } ^ { t + k }$ is also clari<sup>fi</sup>ed as an emerging sequential pattern with respect to sequential pattern $s _ { i \cdot } ^ { t }$

## De<sup>fi</sup>nition 2. Unexpected sequence changes

$S _ { i } ^ { t } \big ( S _ { j } ^ { t { + } k } \big )$ is an unexpected sequence change with respect to $S _ { j } ^ { t { + } k } \left( S _ { i } ^ { t } \right)$ if MD<sup>t</sup> (or $\mathrm { M D } _ { j } ^ { t + k } ) { < } \beta _ { \mathrm { m i n } }$ and $\mathrm { D V } _ { i j } { > } 0$

## De<sup>fi</sup>nition 3. Added/Perished sequential patterns

$s _ { j } ^ { t + k }$ is an added sequential pattern with respect to all sequential patterns in $D ^ { t }$ if $\mathrm { M D } _ { j } ^ { t + k } \ge \beta _ { \operatorname* { m i n } } .$ Conversely, s<sup>t</sup> is a perished sequential pattern with respect to all sequential patterns in $\mathbf { \hat { \boldsymbol { D } } } ^ { t + k } \operatorname { i f } \mathbf { \boldsymbol { M } } \mathbf { \boldsymbol { D } } _ { i } ^ { t } { \geq } \mathbf { \hat { \boldsymbol { \beta } } } _ { \operatorname* { m i n } }$

The numbers of generated sequential patterns for two time-periods

<table><tr><td> $\gamma_{\text{min}}$ </td><td>Year 1997</td><td>Year 1998</td></tr><tr><td>5%</td><td>2239</td><td>33,143</td></tr><tr><td>6%</td><td>1307</td><td>12,911</td></tr><tr><td>7%</td><td>789</td><td>5727</td></tr><tr><td>8%</td><td>485</td><td>3087</td></tr><tr><td>9%</td><td>322</td><td>1756</td></tr><tr><td>10%</td><td>244</td><td>1107</td></tr><tr><td>15%</td><td>56</td><td>194</td></tr><tr><td>20%</td><td>19</td><td>52</td></tr><tr><td>25%</td><td>6</td><td>18</td></tr><tr><td>30%</td><td>4</td><td>7</td></tr><tr><td>35%</td><td>1</td><td>4</td></tr><tr><td>40%</td><td>0</td><td>0</td></tr><tr><td>45%</td><td>0</td><td>0</td></tr><tr><td>50%</td><td>0</td><td>0</td></tr></table>

Table 5  
The numbers of unexpected sequence changes and perished sequential patterns for year1997

<table><tr><td rowspan="2"> $\gamma_{\min}$ </td><td colspan="2"> $\beta_{\min}=0.1$ </td><td colspan="2"> $\beta_{\min}=0.2$ </td><td colspan="2"> $\beta_{\min}=0.3$ </td><td colspan="2"> $\beta_{\min}=0.4$ </td><td colspan="2"> $\beta_{\min}=0.5$ </td></tr><tr><td>Unexpected</td><td>Perished</td><td>Unexpected</td><td>Perished</td><td>Unexpected</td><td>Perished</td><td>Unexpected</td><td>Perished</td><td>Unexpected</td><td>Perished</td></tr><tr><td>6%</td><td>9,825,265</td><td>546</td><td>16,835,938</td><td>3</td><td>16,835,938</td><td>3</td><td>16,874,671</td><td>0</td><td>16,874,671</td><td>0</td></tr><tr><td>7%</td><td>2,244,975</td><td>397</td><td>4,478,505</td><td>7</td><td>4,478,505</td><td>7</td><td>4,518,594</td><td>0</td><td>4,518,594</td><td>0</td></tr><tr><td>8%</td><td>676,043</td><td>266</td><td>1,478,663</td><td>6</td><td>1,478,663</td><td>6</td><td>1,497,185</td><td>0</td><td>1,497,185</td><td>0</td></tr><tr><td>9%</td><td>224,749</td><td>194</td><td>549,609</td><td>9</td><td>549,609</td><td>9</td><td>565,413</td><td>0</td><td>565,413</td><td>0</td></tr><tr><td>10%</td><td>112,876</td><td>142</td><td>259,000</td><td>10</td><td>259,000</td><td>10</td><td>270,070</td><td>0</td><td>270,070</td><td>0</td></tr></table>

Table 6  
The numbers of unexpected sequence changes and added sequential patterns for year1998

<table><tr><td rowspan="2"> $\gamma_{\min}$ </td><td colspan="2"> $\beta_{\min}=0.1$ </td><td colspan="2"> $\beta_{\min}=0.2$ </td><td colspan="2"> $\beta_{\min}=0.3$ </td><td colspan="2"> $\beta_{\min}=0.4$ </td><td colspan="2"> $\beta_{\min}=0.5$ </td></tr><tr><td>Unexpected</td><td>Added</td><td>Unexpected</td><td>Added</td><td>Unexpected</td><td>Added</td><td>Unexpected</td><td>Added</td><td>Unexpected</td><td>Added</td></tr><tr><td>6%</td><td>2,399,646</td><td>11,075</td><td>13,782,309</td><td>2366</td><td>15,623,872</td><td>957</td><td>16,857,680</td><td>13</td><td>16,862,908</td><td>9</td></tr><tr><td>7%</td><td>519,153</td><td>5069</td><td>3,671,997</td><td>1073</td><td>4,012,845</td><td>641</td><td>4,502,025</td><td>21</td><td>4,502,025</td><td>21</td></tr><tr><td>8%</td><td>125,120</td><td>2829</td><td>1,150,410</td><td>715</td><td>1,236,740</td><td>537</td><td>1,486,030</td><td>23</td><td>1,487,970</td><td>19</td></tr><tr><td>9%</td><td>45,383</td><td>1615</td><td>429,207</td><td>423</td><td>433,393</td><td>410</td><td>556,719</td><td>27</td><td>556,719</td><td>27</td></tr><tr><td>10%</td><td>21,190</td><td>1020</td><td>193,210</td><td>315</td><td>199,798</td><td>288</td><td>265,678</td><td>18</td><td>266,166</td><td>16</td></tr></table>

The evaluation standard for the three different change types is summarized in Table 3. To show the judgment process, the example datasets in Section 2.5 is adopted again. Here, we set $\beta _ { \mathrm { m i n } }$ as 0.675. In Section 2.5, we obtained $\mathrm { D V _ { 1 1 } } = 0 . 1 , \mathrm { \ D V _ { 1 2 } } = 0 , \mathrm { \ D V _ { 1 3 } } = 0 . 1 5 6 7 , \mathrm { \ D V _ { 1 4 } } = 0 . 6 5 ,$ and $\mathsf { M D } _ { 1 } ^ { t } = \operatorname* { m i n } ( 0 . 1 , 0 , 0 . 5 1 6 7 , 0 . 6 5 ) = 0 .$ . Because $\mathrm { M D } _ { 1 } ^ { t } { < } \beta _ { \mathrm { m i n } } ,$ s<sup>t</sup> might be an emerging sequential pattern or unexpected sequential pattern with respect to the sequential patterns in $S ^ { t + \mathbf { \hat { k } } }$ , depending on individual DV values. For s<sup>t</sup> and $s _ { 1 } ^ { t { + } k } ,$ , because $\mathsf { D V } _ { 1 1 }$ is 0.1 (greater than zero), s<sup>t</sup>is an unexpected sequence change with respect to s<sup>t</sup> <sup>+</sup> <sup>k</sup> and $s _ { 1 } ^ { t + k }$ is an unexpected sequence change with respect to s<sup>t</sup> also. For s<sup>t</sup> and $s _ { 2 } ^ { t + k }$ since2 $D V _ { 1 2 }$ is 0 and their supports are different, s<sup>t</sup> is an emerging sequential pattern with respect to $s _ { 2 } ^ { t + k }$ and $s _ { 2 } ^ { t + k }$ is an emerging sequential pattern with respect to s<sup>t</sup> also. Similarly, since both $\mathsf { D V } _ { 1 3 }$ and $\mathsf { D V } _ { 1 4 }$ are greater than zero, both of them are categorized as unexpected sequence changes. In addition, we obtained $\mathrm { D V } _ { 2 1 } { = } 0 . 8 8 9 ,$ $\mathrm { D V } _ { 2 2 } { = } 0 . 8 3 3 , \mathrm { D V } _ { 2 3 } { = } 0 . 7 7 2 , \mathrm { D V } _ { 2 4 } { = } 0 . 7 5 0$ , and $\mathrm { M D } _ { 2 } ^ { t } { = } \operatorname* { m i n } ( 0 . 8 8 9 ,$ , 0.833, 0.772, 0.750)=0.75 in Section 2.5. Since MD<sup>t</sup> is greater than $\beta _ { \mathrm { m i n } } , s _ { 2 } ^ { t }$ is claimed as a perished sequential pattern with respect to all sequential patterns in $S ^ { \bar { \mathrm { t } } + k }$

## 3.3. Phase III: significant change evaluation

After completing the change type detection in phase II, each sequential pattern has been identi<sup>fi</sup>ed as one of the three types. However, a large number of change patterns might be generated and make users hard to <sup>fi</sup>nd out signi<sup>fi</sup>cant behavior changes. Consequently, instead of returning all change patterns to users, only signi<sup>fi</sup>cant change patterns, whose degrees of change are greater than a user speci<sup>fi</sup>ed minimum degree of change, $\alpha _ { \mathrm { { m i n } } } ,$ are reported.

Let the degree of change between s<sup>t</sup> and $s _ { j } ^ { t + k }$ be denoted as $\alpha _ { i j } .$ . For an emerging sequential pattern, $\alpha _ { i j }$ is de<sup>fi</sup>ned as the support of $s _ { j } ^ { t + k }$ minus support of s<sup>t</sup> divided by the support of $s _ { i \cdot } ^ { t }$ For an unexpected sequence change, $\alpha _ { i j }$ is de<sup>fi</sup>ned as the multiplication of the similarity between s<sup>t</sup> and $S _ { j } ^ { t + k } \left( 1 - \mathrm { D V } _ { i j } \right)$ with the support of $s _ { j } ^ { t + k }$ divided by the support of $s _ { i \cdot } ^ { t }$ For a perished sequential pattern, $\alpha _ { i j }$ is de<sup>fi</sup>ned as the multiplication of MD<sup>t</sup> with the support of s<sup>t</sup>. For an added sequential pattern, $\alpha _ { i j }$ is de<sup>fi</sup>ned as the multiplication of $\mathrm { \Delta M D } _ { j } ^ { t + k }$ with the support of $s _ { j } ^ { t + k }$ . In summary, the degree of change between s<sup>t</sup><sub>i</sub> and $s _ { j } ^ { t + k }$ for all change types is summarized as follows:

![](/api/attachments/4W5NR3J3/fulltext/images/c4125728073e2646d3b04952cfdaced2d9c5f7c77270489cf179357319dd3dc6.jpg)  
Fig. 6. The numbers of signi<sup>fi</sup>cant emerging sequential patterns when $\beta _ { \mathrm { m i n } } = 0 . 1 .$

Table 7  
A set of signi<sup>fi</sup>cant emerging sequential pattern

<table><tr><td>Sequential pattern</td><td>Year 1997 (or Year 1998)</td><td>Year 1997 Sup (%)</td><td>Year 1998 Sup (%)</td><td> $\alpha_{ij}$ </td></tr><tr><td>1</td><td>Breakfast Foods→Snack_Foods, Vegetables</td><td>10.1416</td><td>15.0946</td><td>0.4883</td></tr><tr><td>2</td><td>Jams_and_Jellies→Baking_Goods</td><td>10.1774</td><td>14.9668</td><td>0.4705</td></tr><tr><td>3</td><td>Bread→Meat</td><td>10.5357</td><td>15.3246</td><td>0.4545</td></tr><tr><td>4</td><td>Snack_Foods, Dairy→Dairy</td><td>10.2849</td><td>14.7495</td><td>0.4340</td></tr><tr><td>5</td><td>Candy→Meat</td><td>10.1416</td><td>14.4172</td><td>0.4215</td></tr><tr><td>6</td><td>Electrical→Fruit</td><td>10.2670</td><td>14.4939</td><td>0.4116</td></tr><tr><td>7</td><td>Dairy→Dairy, Vegetables</td><td>10.8583</td><td>15.0818</td><td>0.3889</td></tr><tr><td>8</td><td>Bathroom_Products→Fruit</td><td>10.4103</td><td>14.3533</td><td>0.3787</td></tr><tr><td>9</td><td>Meat→Candy</td><td>10.2670</td><td>14.0849</td><td>0.3718</td></tr></table>

$$
\alpha_ {i j} = \left\{ \begin{array}{l l} \left| \frac {\operatorname * {S u p} \left(s _ {j} ^ {t + k}\right) - \operatorname * {S u p} \left(s _ {j} ^ {t}\right)}{\operatorname * {S u p} \left(s _ {i} ^ {t}\right)} \right| & \text { Emerging   Sequential   Pattern } \\ (1 - D V _ {i j}) \times \frac {\operatorname * {S u p} \left(s _ {j} ^ {t + k}\right)}{\operatorname * {S u p} \left(s _ {i} ^ {t}\right)} & \text { Unexpected   Sequence   Changes } \\ \mathrm{MD} _ {i} ^ {t} \times \operatorname * {S u p} \left(s _ {i} ^ {t}\right) & \text { Perished   Sequential   Pattern } \\ \mathrm{MD} _ {j} ^ {t + k} \times \operatorname * {S u p} \left(s _ {j} ^ {t + k}\right) & \text { Added   Sequential   Pattern } \end{array} \right.\tag{6}
$$

Based on the Eq. (6), the system will only report the change patterns whose $\alpha _ { i j } { \geq } \alpha _ { \operatorname* { m i n } } .$

## 4. Implementation

To show the feasibility and merits of the proposed sequential pattern change detection framework, datasets Sales\_Fact\_1997 and Sales\_Fact\_1998 in FoodMart2000 database contributed from SQL Server 2000 are tested in this study. The Sales\_Fact\_1997 records 20,522 transactions from 5581 customers in year 1997, while the Sales\_Fact\_1998 records 34,015 transactions from 7824 customers in the year 1998. There are 1559 product items in total, which can be classi<sup>fi</sup>ed into 47 product categories, among these transactions. To avoid trivial mining results, this research aggregates product items to product categories for all transactions.

## 4.1. Phase I—sequential pattern generation

In phase I of the proposed framework, two sequential pattern sets are generated from datasets Sales\_Fact\_1997 and Sales\_Fact\_1998, respectively. Table 4 summarizes the number of sequential patterns for the two time-periods when different minimum support, $\gamma _ { \mathrm { m i n } } ,$ is provided. It is found that the number of sequential patterns decreases dramatically when $\gamma _ { \mathrm { m i n } }$ increases linearly. From Table 4, we <sup>fi</sup>nd that the number of sequential patterns in the year 1998 is signi<sup>fi</sup>cantly large than the one in 1997, especially when $\gamma _ { \mathrm { m i n } }$ is small. For instance, the number of sequential patterns in year 1998 is around 15 times that of year 1997 when $\gamma _ { \mathrm { m i n } }$ is set as 5%, while it is around 4.5 times when $\gamma _ { \mathrm { m i n } }$ is set as 10%. Based on our experience, it is suggested that the number of sequential patterns ranging from 100 to 1000 is suitable for the following change detection analysis. Therefore, in the following analysis, we will focus on experiments where the $\gamma _ { \mathrm { m i n } }$ values are set between 6% and 10%.

## 4.2. Phase II—change type detection

In phase II of the proposed framework, the detection procedure is conducted to judge the change type for each sequential pattern. Among the three change types, the number of emerging sequential patterns will not be affected by the user speci<sup>fi</sup>ed minimum dissimilarity value $\beta _ { \mathrm { m i n } } .$ . However, if a higher $\beta _ { \mathrm { m i n } }$ value is set, a sequential pattern tends to be clari<sup>fi</sup>ed as an unexpected sequence change. Conversely, when a lower $\beta _ { \mathrm { m i n } }$ value is set, a sequential pattern requires greater change to be clari<sup>fi</sup>ed as an added/perished sequential pattern. Tables 5 and 6 summarize the number of unexpected sequence changes and added/perished sequential patterns for years 1997 and 1998 when different $\gamma _ { \mathrm { m i n } }$ and $\beta _ { \mathrm { m i n } }$ values are applied. For example, when $\gamma _ { \mathrm { m i n } }$ is 6% and $\beta _ { \mathrm { m i n } }$ is 0.1, 9,825,265 unexpected sequence changes and 546 perished sequential patterns are detected for year 1997, while 2,399,646 unexpected sequence changes and 11,075 added sequential patterns are found for year 1998. Based on Tables 5 and 6, we <sup>fi</sup>nd that the number of added sequential patterns is considerably greater than the number of perished sequential patterns for all $\beta _ { \mathrm { m i n } }$ values. In addition, when $\beta _ { \mathrm { m i n } }$ is greater than 0.3, the number of perished sequential patterns is close to zero for all $\gamma _ { \mathrm { m i n } }$ values. To facilitate the following signi<sup>fi</sup>cant change evaluation, the system suggests that $\beta _ { \mathrm { m i n } }$ is equal to 0.1 to users so that at least 100 added/perished sequential patterns can be generated.

![](/api/attachments/4W5NR3J3/fulltext/images/23f21b932f1e12bbac1e66cee681b91a2a3cd59b261138dcffdb366715fbcbb7.jpg)  
Fig. 7. The numbers of signi<sup>fi</sup>cant unexpected sequence changes when $\beta _ { \mathrm { m i n } } = 0 . 1 .$

Table 8  
A set of signi<sup>fi</sup>cant unexpected sequence changes

<table><tr><td>Changed Sequence</td><td>Year 1997</td><td>Year 1998</td><td> $\alpha_{ij}$ </td></tr><tr><td>1</td><td>Snack_Foods→Snack_Foods→Snack_Foods, Vegetables (Sup:10.3745%)</td><td>Snack_Foods→Snack_Foods→Snack_Foods, Dairy (Sup:11.5158%)</td><td>1.0175</td></tr><tr><td>2</td><td>Dairy→Frozen_Desserts (Sup:10.5178%)</td><td>Dairy→Beer_and_Wine (Sup:12.6534%)</td><td>1.0025</td></tr><tr><td>3</td><td>Jams_and_Jellies→Canned_Soup (Sup:10.1416%)</td><td>Jams_and_Jellies→Breakfast_Foods (Sup:15.1074%)</td><td>0.9930</td></tr><tr><td>4</td><td>Snack_Foods→Vegetables→Vegetables (Sup:10.7328%)</td><td>Snack_Foods→Vegetables→Snack_Foods (Sup:11.5031%)</td><td>0.9824</td></tr><tr><td>5</td><td>Vegetables→Vegetables→Snack_Foods→Snack_Foods (Sup:10.1774%)</td><td>Vegetables→Vegetables→Snack_Foods→Snack_Foods, Vegetables (Sup:10.4167%)</td><td>0.9723</td></tr><tr><td>6</td><td>Bread→Frozen_Entrees (Sup:10.5537%)</td><td>Bread→Meat (Sup:15.3246%)</td><td>0.9680</td></tr><tr><td>7</td><td>Snack_Foods→Vegetables→Vegetables→Snack_Foods (Sup:10.3386%)</td><td>Snack_Foods→Vegetables→Vegetables→Snack_Foods, Vegetables (Sup:10.5061%)</td><td>0.9653</td></tr><tr><td>8</td><td>Dairy→Vegetables→Vegetables (Sup:14.0656%)</td><td>Dairy→Vegetables→Snack_Foods, Vegetables (Sup:12.7684%)</td><td>0.8327</td></tr><tr><td>9</td><td>Snack_Foods→Vegetables→Frozen_Entrees (Sup: 12.238%)</td><td>Snack_Foods→Vegetables→Frozen_Entrees, Vegetables (Sup: 10.9535%)</td><td>0.8204</td></tr></table>

## 4.3. Phase III—significant change evaluation

In phase III, instead of returning all change patterns to users, only signi<sup>fi</sup>cant change patterns, whose degrees of change are greater than a user speci<sup>fi</sup>ed minimum degree of change, $\alpha _ { \mathrm { { m i n } } } ,$ are reported. In addition, this system will suggest appropriate $\alpha _ { \mathrm { m i n } }$ to users so that at least 10 signi<sup>fi</sup>cant patterns in each type can be obtained.

## 4.3.1. Significant emerging sequential pattern

Signi<sup>fi</sup>cant emerging sequential patterns are rules that appear in both the year 1997 and 1998 (i.e. $\mathsf { D V } _ { i j } { = } 0 )$ but their supports are quite different. Fig. 6 depicts the numbers of signi<sup>fi</sup>cant emerging sequential patterns when different $\alpha _ { \mathrm { m i n } }$ are applied. If $\gamma _ { \mathrm { m i n } }$ is set as 10%, the system will suggest that $\alpha _ { \mathrm { { m i n } } }$ is 0.4 so that at least 10 signi<sup>fi</sup>cant emerging sequential patterns can be found. Table 7 illustrate 9 among 11 signi<sup>fi</sup>cant emerging sequential patterns when $\gamma _ { \mathrm { m i n } } { = } 1 0 \%$ and $\alpha _ { \mathrm { m i n } } { = } 0 . 4 . \ : \mathrm { A s }$ shown in Table 7, the supports for sequential patterns 1 to 3 increase from around 10% in 1997 to 15% in 1998. In addition, the degrees of change for the three signi<sup>fi</sup>cant emerging sequential patterns are relatively high. Note that sequential pattern 1 (“Breakfast\_Foods→Snack\_Foods, Vegetables”) is the most signi<sup>fi</sup>cant emerging sequential pattern since its degree of change is 0.4883. Therefore, it is strongly suggested that managers check the reasons why these three emerging sequential patterns are so strong. For sequential patterns 1, 4 and 7, we observed that the products “Snack\_Foods” and “Vegetables,” “Snack\_Foods” and “Dairy,” “Dairy” and “Vegetables” are often purchased simultaneously. It is clear that the relationship between these four products is stronger. Layout managers should carefully arrange these products in categories in close locations to increase the opportunities for cross-sales. A similar situation can be found for sequential patterns 5 and 9. We found that both “Candy” and “Meat” appear in the two patterns but in a different order. It indicates that the relationship between products “Candy” and “Meat” is very strong.

## 4.3.2. Significant unexpected sequence change

The second type of change behavior is unexpected sequence changes. When the change degree of an unexpected sequence change is greater than $\alpha _ { \mathrm { { m i n } } }$ the sequential pattern is called a signi<sup>fi</sup>cant unexpected sequence change. Fig. 7 illustrates the number of signi<sup>fi</sup>cant unexpected sequence changes when $\beta _ { \mathrm { m i n } } { = } 0 . 1 . \mathrm { I f } \gamma _ { \mathrm { m i n } }$ is set as 10% and $\beta _ { \mathrm { m i n } }$ as 0.1, the system will suggest $\alpha _ { \mathrm { m i n } } \mathrm { = } 0 . 8$ so that at least 10 signi<sup>fi</sup>cant unexpected sequence changes can be reported. Table 8 depicts 9 among 319 signi<sup>fi</sup>cant unexpected sequence changes when $\gamma _ { \mathrm { m i n } } = 1 0 \% , \ \beta _ { \mathrm { m i n } } = 0 . 1$ and $\alpha _ { \mathrm { m i n } } = 0 . 8 .$ . It is clear that the degree of change between “Snack\_ Foods→Snack\_Foods→Snack\_ Foods, Vegetables” and “Snack\_Foods→ Snack\_Foods→Snack\_Foods, Dairy” (Changed sequence 1) is most signi<sup>fi</sup>cant. According to further data analysis, we <sup>fi</sup>nd that there are 640 customers altering their patterns from “Dairy→Frozen\_Desserts” to “Dairy→Beer\_and\_Wine” (Changed sequence 2), 617 customers altering their patterns from “Jams\_and\_Jellies→Canned\_Soup” to “Jams\_and\_Jellies→Breakfast\_Foods” (Changed sequence 3), and 610 customers altered their patterns from “Bread→Meat” to “Bread→ Frozen\_Entrées” (Changed sequence $6 ) .$ Managers should be aware that some products are substituted by other products according to these signi<sup>fi</sup>cant unexpected sequence changes. In Table 8, with the exception of Change sequences 8 and 9, the support values of sequential patterns in year 1998 are all smaller than the support values of sequential patterns in year 1997. Among these Change sequences, the length of sequential patterns in Changed sequences 5 and 7 is four. The purchase order of the <sup>fi</sup>rst three element is the same for the two unexpected sequence changes, while the purchase behavior changes in the forth element from “Snack\_Foods” in year 1997 to “Vegetables” and “Snack\_Foods” in year 1998.

![](/api/attachments/4W5NR3J3/fulltext/images/9e70648e33d3378251899905c8c12d7e84ad40ecd2add8dd658c3b06a1c40252.jpg)  
Fig. 8. The numbers of signi<sup>fi</sup>cant perished sequential patterns when $\beta _ { \mathrm { m i n } } = 0 . 1 .$

Table 9  
A set of signi<sup>fi</sup>cant perished sequential patterns

<table><tr><td>Perished sequential pattern</td><td>Year 1997</td><td> $MD_{i}^{1997}$ </td><td> $\alpha_{ij}$ </td></tr><tr><td>1</td><td>Dairy→Candy (Sup: 11.79%)</td><td>0.3333</td><td>3.9300</td></tr><tr><td>2</td><td>Dairy→Electrical (Sup: 11.6467%)</td><td>0.3333</td><td>3.8822</td></tr><tr><td>3</td><td>Electrical→Dairy (Sup: 11.5392%)</td><td>0.3333</td><td>3.8464</td></tr><tr><td>4</td><td>Snack_Foods, Vegetables→Snack_Foods, Vegetables (Sup: 12.0767%)</td><td>0.1667</td><td>2.0128</td></tr><tr><td>5</td><td>Dairy→Vegetables→Dairy (Sup: 10.7328%)</td><td>0.1667</td><td>1.7888</td></tr></table>

## 4.3.3. Significant added/perished sequential pattern

The third type of behavior change is added or perished sequential patterns. A sequential pattern in year 1997 can be considered as a perished sequential pattern if its MD<sup>1997</sup> is higher than $\beta _ { \mathrm { m i n } } .$ Fig. 8 summarizes the number of signi<sup>fi</sup>cant perished sequential patterns when $\beta _ { \mathrm { m i n } } { = } 0 . 1$ 1. From the <sup>fi</sup>gure, we discover the number of signi<sup>fi</sup>cant perished sequential patterns decreases gradually when $\gamma _ { \mathrm { m i n } }$ or $\beta _ { \mathrm { m i n } }$ increases. Table 9 illustrates 6 among 10 signi<sup>fi</sup>cant perished sequential patterns when $\gamma _ { \mathrm { m i n } } = 1 0 \% , \ \beta _ { \mathrm { m i n } } = 0 . 1$ and $\alpha _ { \mathrm { { m i n } } } = 3 .$ . Perished sequential patterns 1 to 6 suggest that these customer behaviors are popular in the year 1997, but no longer valid in 1998. The most signi<sup>fi</sup>cant perished sequential pattern is sequential pattern 1 “Dairy→Candy” with support=11.79%, $\mathrm { M D } _ { i } ^ { 1 9 9 7 } { = } 0 . 3 3 3 3$ and $\alpha _ { i j } = 3 . 9 3$ In addition, we can observe that the relationship between “Dairy” and “Electrical” is very strong but perished in year 1998, according to perished sequential patterns 2 and 3.

Similarly, a sequential pattern in year 1998 is considered as an added sequential pattern if its $\mathrm { M D } _ { j } ^ { 1 9 9 8 }$ is higher than $\beta _ { \mathrm { m i n } } .$ . The number of signi<sup>fi</sup>cant added sequential patterns is summarized in Fig. 9. It is discovered that the number of signi<sup>fi</sup>cant added sequential patterns decreases gradually for all $\gamma _ { \mathrm { m i n } }$ levels when $\beta _ { \mathrm { m i n } }$ increases. In addition, the number of signi<sup>fi</sup>cant added sequential patterns is almost unchanged for $\beta _ { \mathrm { m i n } } = 0 . 5 .$ . Table 10 depicts 5 among 288 signi<sup>fi</sup>cant added sequence changes when $\gamma _ { \mathrm { m i n } } = 1 0 \% , \beta _ { \mathrm { m i n } } = 0 . 1$ and $\alpha _ { \mathrm { { m i n } } } = 3$ . For example, added sequential pattern 1 (“Pizza→Vegetables”) is not only the most signi<sup>fi</sup>cant $( \alpha _ { i j } { = } 8 . 2 1 4 1 )$ but also the most different $( \mathrm { M D } _ { i } ^ { 1 9 9 8 } { = } 0 . 6 6 6 7 )$ than any of the sequential patterns in year 1997. Both added sequential patterns 3 and 4 include the same products, “Meat,” “Vegetable” and $\mathrm { \ " { D a i r y , } " }$ but are different in their order of appearance. Besides, adding sequential pattern 5 provides more information about the customer's behavior due to its longer sequence length.

Table 10  
A set of signi<sup>fi</sup>cant added sequential patterns

<table><tr><td>Added sequential pattern</td><td>Year 1998</td><td> $MD_{j}^{1998}$ </td><td> $\alpha_{ij}$ </td></tr><tr><td>1</td><td>Pizza → Vegetables (Sup: 12.3211%)</td><td>0.6667</td><td>8.2141</td></tr><tr><td>2</td><td>Fruit → Bathroom_Products (Sup: 14.3788%)</td><td>0.3333</td><td>4.7929</td></tr><tr><td>3</td><td>Meat, Vegetables → Dairy (Sup: 14.021%)</td><td>0.3333</td><td>4.6737</td></tr><tr><td>4</td><td>Dairy, Vegetables → Meat (Sup: 13.9826%)</td><td>0.3333</td><td>4.6609</td></tr><tr><td>5</td><td>Snack_Foods → Breakfast_Foods → Vegetables (Sup: 13.5736%)</td><td>0.3333</td><td>4.5245</td></tr></table>

## 5. Conclusions

Recent trends in customer-oriented markets drive many researches develop sequential pattern algorithms to explore consumer behaviors. Sequential pattern mining is the technique that discovers frequently occurring patterns related to time from a large-scale database. With sequential patterns, enterprises can develop their own strategy for targeted marketing, customer retention, and promotion. However, customer behaviors usually change over time. Behavior patterns popular in the previous time-period may not be valid for the next time-period. To help managers capture the dynamic behavior changes in time, a sequential pattern change detection framework is proposed in this paper. The framework consists of three major phases. In phase I, two sequential pattern sets are generated from two different timeperiod databases respectively using the GSP algorithm. The algorithm <sup>fi</sup>nds all sequences whose support is greater than the user-de<sup>fi</sup>ned minimum support value $( \gamma _ { \mathrm { m i n } } ) .$ . The smaller the $\gamma _ { \mathrm { m i n } }$ value, the more the number of sequential patterns generated. In phase II, the dissimilarities between all pairs of sequential patterns are evaluated based on a developed sequential pattern matching algorithm. Then, the minimum dissimilarity values between all pairs of sequential patterns are derived and compared with a user-de<sup>fi</sup>ned minimum dissimilarity value $( \beta _ { \mathrm { m i n } } ) .$ .Based on a set of judgment criteria, each sequential pattern is clari<sup>fi</sup>ed as one of the following three change types: an emerging sequential pattern, an unexpected sequence change, or an added/perished sequential pattern. The higher the β<sub>min</sub> value, the less the number of added/perish sequential patterns generated but the more the number of unexpected sequence changes. In phase III, each change pattern is determined as signi<sup>fi</sup>cant or not using the user-de<sup>fi</sup>ned minimum degree of change $( \alpha _ { \mathrm { m i n } } ) .$ .The higher the $\alpha _ { \mathrm { { m i n } } }$ value, the less the number of changed patterns reported. Finally, the set of signi<sup>fi</sup>cant change patterns are generated and reported to users for further analysis.

![](/api/attachments/4W5NR3J3/fulltext/images/9e784418a5b7639fd08d1f31376f8207a385b8ae78a4457f90628838fe95cf69.jpg)  
Fig. 9. The numbers of signi<sup>fi</sup>cant added sequential patterns when $\beta _ { m i n } = 0 . 1 .$

It is clear that setting these threshold values could be a challenge for users. Unfortunately, it is hard or impossible to know how many or what sequential patterns might be generated except the whole analysis process is completed. Setting the same threshold values to different datasets will generate totally different results. Therefore, this system automatically conducts a set of experiments using different threshold values in the each phase. Then, the system summarizes the experimental results to users and provides proper threshold values as suggestions.

Two critical statistical measures are de<sup>fi</sup>ned in this research. The <sup>fi</sup>rst measure called “support” is used to evaluate how strong a sequential pattern is. It is de<sup>fi</sup>ned as the number of tuples in a sequence database containing sequence s. A sequential pattern having high support value means that the pattern appears quit often. Another statistical measure called “degree of change” is used to evaluate how signi<sup>fi</sup>cant a change between two sequential patterns might have. The de<sup>fi</sup>nition of “degree of change” for different change types is similar but different. A change pattern with high degree of change means that the change is dramatic. Based on the statistical measures “support” and “degree of change”, users can easily observe whether sequential patterns and change patterns are worth to pay attention or not.

In this study, the dissimilarity measurement is designed based on three major considerations. They are the number of mismatched elements, the position of the element changed, and the dissimilarity between any mismatched elements. However, some other considerations are worthwhile to try. For example, rule change based on money impact might be very interesting when evaluating the dissimilarity between two sequential patterns. If system can report the money impact for each change, users can easily evaluate the money gain or lost under different decision making. Another limitation of the proposed framework is that the time-intervals between transactions are ignored. Without considering time interval between elements, the generated sequential patterns might not distinguish customer behavior well. In the future, we will consider time interval issue in the proposed framework, so that the change detection task can be more accurate.

## Acknowledgement

This work was partially supported by the National Science Council of Taiwan No. NSC 94-2213-E-155-005.

## References

[1] R. Agrawal, R. Srikant, Mining sequential patterns, Proceedings of the 11th International Conference on Data Engineering, 1995, pp. 3–14.

[2] F. Altiparmak, H. Ferhatosmanoglu, S. Erdal, D.C. Trost, Information mining over heterogeneous and high-dimensional time-series data in clinical trials databases, IEEE Transactions on Information Technology in Biomedicine 10 (2) (2006) 254–263.

[3] J. Ayres, J. Flannick, J. Gehrke, T. Yiu, Sequential pattern mining using a bitmap representation, Proceedings of the ACM International Conference on Knowledge Discovery and Data Mining (SIGKDD), 2002, pp. 47–58.

[4] M.C. Chen, A.L. Chiu, H.H. Chang, Mining changes in customer behavior in retail marketing, Expert Systems with Applications 28 (4) (2005) 773–781.

[5] M.S. Chen, J.S. Park, P.S. Yu, Ef<sup>fi</sup>cient data mining for path traversal patterns, IEEE Transactions on Knowledge and Data Engineering 10 (2) (1998) 209–221.

[6] R.S. Chen, Y.C. Hu, A novel method for discovering fuzzy sequential patterns using the simple fuzzy partition method, Journal of the American Society for Information Science and Technology 54 (7) (2003) 660–670.

[7] Y.L. Chen, Y.H. Hu, Constraint-based sequential pattern mining: the consideration of recency and compactness, Decision Support Systems 42 (2) (2006) 1203–1215.

[8] Y.L. Chen, J.M. Chen, C.W. Tung, A data mining approach for retail knowledge discovery with consideration of the effect of shelf-space adjacency on sales, Decision Support Systems 42 (3) (2006) 1503–1520.

[9] D.A. Chiang, S.L. Lee, C.C. Chen, M.H. Wang, Mining interval sequential patterns, International Journal of Intelligent Systems 20 (3) (2005) 359–373.

[10] D.A. Chiang, Y.F. Wang, S.L. Lee, C.J. Lin, Goal-oriented sequential pattern for network banking churn analysis, Expert System with Applications 25 (3) (2003) 293–302.

[11] D. Chudova, P. Smyth, Analysis of pattern discovery in sequences using a Bayes error framework, Data Mining and Knowledge Discovery 7 (3) (2003) 273–299.

[12] G. Dong, J. Li, Ef<sup>fi</sup>cient mining of emerging patterns: discovering trends and differences, Proceedings of the 5th International Conference on Knowledge Discovery and Data Mining, 1999, pp. 43–52.

[13] R.O. Duda, P.E. Hart, D.G. Stork, Pattern Classi<sup>fi</sup>cation, 2nd edition, John Wiley, New York 2001

[14] M. El-Sayed, C. Ruiz, E.A. Rundensteiner, FS-Miner: ef<sup>fi</sup>cient and incremental mining of frequent sequence patterns in web logs, Proceedings of the 6th Annual ACM international Workshop on Web information and Data Management, 2004, pp. 128–135.

[15] H. Fan, K. Ramamohanarao, Ef<sup>fi</sup>ciently mining interesting emerging patterns, Advances in Web-age information management, Lecture Notes in Computer Science, vol. 2762, Springer, Berlin, 2003, pp. 189–201.

[16] J. Han, G. Dong, Y. Yin, Ef<sup>fi</sup>cient mining of partial periodic patterns in time series database, Proceedings of the 5th International Conference on Data Engineering, 1999, pp. 106–115.

[17] J.L. Koh, S.F. Shieh, An ef<sup>fi</sup>cient approach for maintaining association rules based on adjusting FP-tree structure, Lecture Notes in Computer Science (LNCS), vol. 2973, Springer, Berlin, 2004, pp. 417–424

[18] H.C. Kum, J.H. Chang, W. Wang, Sequential pattern mining in multi-databases via multiple alignment, Data Mining and Knowledge Discovery 12 (2–3) (2006) 151–180.

[19] H.C. Kum, J.H. Chang, W. Wang, Benchmarking the effectiveness of sequential pattern mining methods, Data & Knowledge Engineering 60 (1) (2007) 30–50.

[20] C. Lanquillon, Information <sup>fi</sup>ltering in changing domains, Proceedings of the International Joint Conference on Arti<sup>fi</sup>cial Intelligence, 1999, pp. 41–48.

[21] C.H. Lee, C.R. Lin, M.S. Chen, Sliding window <sup>fi</sup>ltering: an ef<sup>fi</sup>cient method for incremental mining on a time-variant database, Information Systems 30 (3) (2005) 227–244.

[22] F.R. Lin, K.J. Huang, N.S. Chen, Integrating information retrieval and data mining to discover project team coordination patterns, Decision Support Systems 42 (2) (2006) 745–758.

[23] B. Liu, W. Hsu, H.S. Han, Y. Xia, Mining changes for real-life applications, Proceedings of the 2th International Conference on Data Warehousing and Knowledge Discovery, 2000, pp. 337–346.

[24] F. Masseglia, P. Poncelet, M. Teisseire, Incremental mining of sequential patterns in large databases, Data and Knowledge Engineering 46 (1) (2003) 97–121.

[25] B. Padmanabhan, A. Tuzhilin, Unexpectedness as a measure of interestingness in knowledge discovery, Decision Support Systems 27 (3) (1999) 303–318.

[26] B. Padmanabhan, A. Tuzhilin, On characterization and discovery of minimal unexpected patterns in rule discovery, IEEE Transactions on Knowledge and Data Engineering 18 (2) (2006) 202–216.

[27] J. Pei, J. Han, B. Mortazavi-Asl, H. Zhu, Mining access patterns ef<sup>fi</sup>ciently from web logs, Proceedings of 2000 Pacific-Asia Conference on Knowledge Discovery and Data Mining, 2000.

[28] H.S. Song, I.K. Kim, S.H. Kim, Mining the change of customer behavior in an internet shopping mall, Expert Systems with Applications 21 (3) (2001) 157–168.

[29] R. Srikant, R. Agrawal, Mining sequential patterns: generalizations and performance improvements, Proceedings of 6th International Conference of Extending Database Technology (EDBT), 1996, pp. 3–17.

[30] P. Terlecki, K. Walczak, On the relation between rough set reducts and jumping emerging patterns, Information Sciences 177 (1) (2007) 74–83.

[31] F. Yu, F. Chen, K. Dong, A granulation-based method for <sup>fi</sup>nding similarity between time series, Proceedings of IEEE International Conference on Granular Computing, vol. 2, July 2005, pp. 700–703.

[32] M. Zhang, B. Kao, C.L. Yip, D.W.L. Cheung, FFS—an I/O-ef<sup>fi</sup>cient algorithm for mining frequent sequences, Lecture Notes in Computer Science (LNCS), vol. 2035, Springer, Berlin, 2001, pp. 294–305.

Chieh-Yuan Tsai is an associate professor in the Department of Industrial Engineering and Management at the Yuan-Ze University, Taiwan. He received his M.S. and Ph.D. degrees in Department of Industrial and Manufacturing Systems Engineering from the University of Missouri-Columbia, USA. His research activities include data mining customer relationship management (CRM), and product data management.

Yu-Chen Shieh is a Senior Engineering at the King Yuan Electronics Compnay, Taiwan. She graduated with a degree in Department of Industrial Engineering and Management, Yuan Ze University, Taiwan. Her research interests include data mining, change mining, and customer relationship management.
