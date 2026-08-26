---
otero_id: 14320
otero_key: "5H4GUQNJ"
title: "Mining consensus preference graphs from users' ranking data"
authors: "Yen-Liang Chen; Li-Chen Cheng; Po-Hsiang Huang"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.10.031"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Mining consensus preference graphs from users' ranking data

Yen-Liang Chen <sup>a,</sup>⁎, Li-Chen Cheng <sup>b</sup>, Po-Hsiang Huang <sup>a</sup>

<sup>a</sup> Department of Information Management, National Central University, Chung-Li 320, Taiwan, ROC

<sup>b</sup> Department of Computer Science and Information Management, Soochow University, Taipei 100, Taiwan, ROC

## a r t i c l e i n f o

Article history: Received 1 October 2011 Received in revised form 28 September 2012 Accepted 21 October 2012 Available online 27 October 2012

Keywords: Data mining Decision making Group decision making Maximum consensus sequence Preference graph

## a b s t r a c t

The group ranking problem consists of constructing coherent aggregated results from preference data provided by decision makers. Traditionally, the output of a group ranking problem can be classi<sup>fi</sup>ed into ranking lists and maximum consensus sequences. In this study, we propose a consensus preference graph approach to represent the coherent aggregated results of users' preferences. The advantages of our approach are that (1) the graph is built based on users' consensuses, (2) the graph can be understood intuitively, and (3) the relationships between items can be easily seen. An algorithm is developed to construct the consensus preference graph from users' total ranking data. Finally, extensive experiments are carried out using synthetic and real data sets. The experimental results indicate that the proposed method is computationally ef<sup>fi</sup>cient, and can effectively identify consensus graphs.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

The group ranking decision process involves aggregating individual rankings to obtain a representative group ranking. In other words, the group ranking algorithm generates consolidated ranking results that represent the group will, preference, or decision based on decision makers' preference data. In recent decades, the group ranking problem has become an important and interesting issue in decision making [11,15], machine learning [14], web search strategies [2,7] and others. The essence of this problem is how to consolidate and aggregate decision makers' rankings to obtain a group ranking that represents “better coherent” ordering in regards to the decision makers' rankings.

Generally, the traditional group ranking problem can be classi<sup>fi</sup>ed using three aspects: the completeness of the user-provided preference information, the input format used to express users' preferences, and the type of compromised output results. The group ranking problem can be roughly classi<sup>fi</sup>ed into two major approaches based on the completeness of the decision maker's preference information: the total ranking approach [7,17,20–23] and the partial ranking approach [3,4,8–10,18,19]. The former requires individuals to appraise all items (called alternatives), while the latter appraises only a subset of items. There are three typical input formats decision makers can use express their item preferences: weighting models, pair-wise comparisons, and ranking lists. All three formats have been used in previous studies to express individuals' input preferences. These formats may not be perfect, but they express user preferences reasonably well in most practical situations. Depending on the input format adopted, users are asked to rank (in the ranking list model), rate (in the weighting model), or compare (in the pair-wise comparison model) the items. After all preference data have been collected, an algorithm is applied to generate the consolidated output results. In previous research, output results could be divided into two main types. One is a total ranking list, which is an ordering list of all items that represent the achieved consensus. The other is a maximum consensus sequence, which gives the longest ranking lists of items that agree with the majority and disagree with the minority.

Unfortunately, both output formats have their own weaknesses. Most previous ranking list approaches attempted to minimize the total disagreement between multiple input rankings in order to obtain an overall ranking list that represented the achieved consensus. This disregards the fact that user opinions may be discordant and have no consensus, forcing a complete ranking result even if there is no consensus or only a slight consensus. In such a situation, what we obtain is merely the algorithm output, since different algorithms derive different ranking results due to their different designs. To overcome this weakness, Chen and Cheng [5,6] proposed the maximum consensus approach, which generates only those maximum sequences on which users have consensus, meaning they are agreed upon by a majority of users and disagreed with by a minority of users. However, this approach may generate many maximum consensus sequences, making the results fragmented and dif<sup>fi</sup>cult to understand and use.

Therefore, we propose a method that <sup>fi</sup>nds consensus preferences and represents these relationships as a graph. This is called a preference graph, where the relationships are agreed upon by majority of users and disagreed with by only a minority of users. Accordingly, we develop algorithms to discover preference graphs from users' ranking lists, and use the graphs to present the preferences of all users.

Table 1  
A sample database.

<table><tr><td> $u_{id}$ </td><td>User sequence</td></tr><tr><td>S1</td><td> $S_1=\{A=C>B=D>E\}$ </td></tr><tr><td>S2</td><td> $S_2=\{A>C=D\geq B>E\}$ </td></tr><tr><td>S3</td><td> $S_3=\{C>A=B\geq D>E\}$ </td></tr></table>

Example 1. Suppose we have the three ranking lists shown in Table 1. We will show their consolidated results in the ranked order, maximum consensus sequence, and preference graph formats.

Using a total ranking list, we may get the result $\{ \mathsf { A } \geq \mathsf { C } > \mathsf { B } \geq \mathsf { D } > \mathsf { E } \}$ which represents a coherent ranking of all items. There is no consensus, however, on the rankings of A and C in the preference data. The reason they are arranged that way is simply because we are forced into a complete ranking.

Using maximum consensus sequences, the longest patterns of coherent item rankings are $\{ { \mathsf { A } } { \geq } { \mathsf { D } } { > } { \mathsf { E } } \}$ and {C>B>E}. The problem is that it may output many consensus sequences that need to be checked. Additionally, the preference between items A and C is unknown.

Using our approach, the result may look like Fig. 1. Items in the same cluster are similarly preferred by users. Therefore, items A and C are similarly preferred, and B and D are similarly preferred. Additionally, $G _ { 1 }$ is preferred more than $G _ { 2 }$ and $G _ { 3 } ,$ and $G _ { 2 }$ is preferred more than $G _ { 3 } .$ There are several advantages to this approach. First, the graph is built based on users' consensuses. Second, the graph can be intuitively understood. Third, relationships between items can be observed from the graph.

This paper is divided into six sections. Our motivations are discussed in Section 1. Section 2 reviews related works. Section 3 de<sup>fi</sup>nes the problem of mining consensus preference graphs and provides de<sup>fi</sup>nitions. Section 4 introduces the preference graph mining algorithm. Experimental results are presented in Section 5. Finally, we draw conclusions in Section 6.

## 2. Related work

In this section, we review literature regarding the group ranking problem. As shown in Table 2, the group ranking problem can be classi-<sup>fi</sup>ed using three features: the completeness of input preference information, the type of input format, and the compromised output format.

When looking at the completeness of users' item appraisals, the group ranking problem can be identi<sup>fi</sup>ed as using the total ranking approach or the partial ranking approach. In the total ranking approach, all individuals have to appraise all items, no matter the input format. Originally, Kemeny and Snell studied the group ranking problem in a pair-wise format by minimizing the distance between two complete rankings [20]. This optimal approach has been proven as an NP-hard problem [1]. Following that, Cohen [7] developed a greedy-like algorithm that minimizes the discrepancy in rankings by integrating preference data. Additionally, Saaty developed the AHP (Analytical hierarchical process) method, a leading approach to multi-criteria decision making that consolidates many full ranking lists by assigning weights to different criteria [14,22,23].

![](/api/attachments/5H4GUQNJ/fulltext/images/cd2230a4e885bce0ff40ad600f41097526ead531084a15ef57441d0a8e9a37d2.jpg)  
Fig. 1. Preference graph.

Table 2  
Dimensions of group ranking problem.

<table><tr><td>Completeness of preference information</td><td>Total ranking</td><td>Partial ranking</td><td></td></tr><tr><td>Input format Output format</td><td>Weighting models Ranking orders</td><td>Pair-wise comparisons Consensus lists</td><td>Ranking lists Preference graph</td></tr></table>

In the partial ranking approach, users rank a selected subset of items to avoid appraising unfamiliar items. Many models have been proposed to deal with partial rankings. For instance, Bogart extended the Kemeny–Snell model by allowing users to appraise a subset of items, and then <sup>fi</sup>nish a partial ordering [3,4]. Various solution methods based on distance functions have also been studied [8–10]. In some group ranking problems, rankings include intensity [19]. The goal of most partial ranking approaches is to obtain a full ranking from user input data. Cook proved that in some cases, however, the aggregated results will not be a full order [11].

Individual preference data can be expressed as item weights/ scores, sets of pair-wise comparisons, or item ranking lists. Actually, scoring behavior varies from person to person [19]. It is dif<sup>fi</sup>cult for users to accurately express his/her preferences as a precise numerical value [13]. Pair-wise comparisons are widely used, but create a large amount of work due to numerous comparisons [8,12,19]. If there are many items, comparing them all may become tedious. Finally, ranking lists can be total ordering or partial ordering lists. Compared to total ordering, partial ordering lists are generally easier to use, but tend to result in incomplete and inconsistent information problems.

Typically, the group ranking problem has two output formats: a total ranking list or maximum consensus sequences. A total ranking list is a full ordering list that has found a consensus with minimum disagreement from all preference data. From this list, we can easily see the relationships between items. As mentioned in the introduction, however, even when there is no consensus, we are forced into a total ranking list. As a result, what we obtain is merely the algorithm output. Therefore, maximum consensus sequences were proposed to solve this problem [5,6]. These sequences represent the consensuses that are agreed upon by a majority of users and disagreed with by a minority of users. However, since we may generate numerous maximum consensuses of different lengths, the results are fragmented and dif<sup>fi</sup>cult to understand and use.

In our work, as shown in Table 2, we use the total ranking approach in regards to information completeness, ranking lists as the input, and preference graphs as the output format. Preference graphs are a brand new output format that has not been used in any previous research.

## 3. Problem de<sup>fi</sup>nition

In this section, we formally de<sup>fi</sup>ne the problem of mining consensus preference graphs from users' ranking data. Let $U { = } \{ u _ { 1 } , u _ { 2 } { , } . . . , u _ { m } \}$ and $I { = } \{ i _ { 1 } , i _ { 2 } { , } { \ldots } , i _ { n } \}$ denote the sets of all users and all items, respectively. Each user u creates a ranked list of all items that expresses his/her preferences. The ranked list of user $u _ { i }$ can be represented as a sequence ${ { S } _ { i } } = \{ { { a } _ { 1 } } \oplus { { a } _ { 2 } } \oplus . . . \oplus { { a } _ { n } } \}$

Each user sequence must satisfy the following conditions: <sup>fi</sup>rst, an item $a _ { j } \in I ,$ where $1 { \leq } j { \leq } n ,$ cannot appear more than once in a user sequence; second, the comparator⊕belongs to $\{ > , \geq , = \}$ . The comparator $" > "$ means that the preceding item is more preferable than the succeeding item. The comparator $\ " \geq \ "$ indicates that the preceding item is at least as preferable as the succeeding item. Finally, the comparator $" = "$ denotes the same preference for both items. For example, in

Table 1 we have $I = \{ { \sf A } , { \sf B } , { \sf C } , { \sf D } , { \sf E } \}$ and $u _ { 1 } \prime _ { S }$ sequences $S _ { 1 } = \{ { \mathsf { A } } = { \mathsf { C } } > { \mathsf { B } } =$ $\tt D > E \}$ . The sequence database D is formed from a set of records ${ < } u _ { i d } ,$ $S _ { i } { > }$ , where $u _ { i d }$ is the user identi<sup>fi</sup>er and $S _ { i }$ is a user sequence.

The objective of the proposed algorithm is to <sup>fi</sup>nd the preference relationships between items, and use a graph to represent these relationships. The following de<sup>fi</sup>nitions are given to formally de<sup>fi</sup>ne the problem.

De<sup>fi</sup>nition 1. (Item-pair) An item-pair can be represented as $p =$ {a<sub>i</sub> ⊕ a<sub>j</sub>}, where $a _ { i } , a _ { j } { \in } I$ and $\oplus \in \{ > , \geq , = \}$ . The relationship between two items in p can be represented as $R e l ( a _ { i } , a _ { j } , p )$

For example, we may have item-pair $p = \{ i _ { 1 } > i _ { 3 } \}$ with $R e l ( i _ { 1 } , i _ { 3 } , p ) =$ $" > "$

De<sup>fi</sup>nition 2. (Group) Item set I can be partitioned into k mutually exclusive and exhaustive groups $G _ { j } = \{ i _ { i } | i _ { i } \in I \}$ . That is, $G _ { i } \cap G _ { j } = \emptyset$ , for $i \neq j ,$ and $G _ { 1 } \cup . . . \cup G _ { k } { = } I .$

For example, item set ${ \mathrm { I } } = \{ { \mathrm { A } } , { \mathrm { ~ B } } , { \mathrm { ~ C } } , { \mathrm { ~ D } } , { \mathrm { ~ E } } \}$ can be partitioned into three groups: $G _ { 1 } = \{ \mathrm { A } , \mathrm { C } \} , G _ { 2 } = \{ \mathrm { B } , \mathrm { D } \}$ , and $G _ { 3 } = \{ \mathrm { E } \}$

De<sup>fi</sup>nition 3. (Set of item-pairs) Let $G _ { i j } { = } G _ { i } \otimes  G _ { j }$ denote the set of all item pairs whose <sup>fi</sup>rst object comes from $G _ { i }$ and the second object from $G _ { j } ,$ where $1 \leq i , j \leq k ,$ and ⊗ denotes a join operation. An item-pair $\alpha _ { r }$ in $G _ { i j }$ can be called a G-item-pair and be represented as $\alpha _ { r } = \{ a \oplus b \} ,$ , where $1 \leq r \leq | G _ { i } | \times | G _ { j } |$ and $a \in G _ { i } , b \in G _ { j } { \mathrm { ~ a n d ~ } } \oplus \in \{ > \}$

Here, we don't consider the case of $\oplus = " = "$ , because each arc in the preference graph represents a precedence relationship between two groups of items. For example, if we have $G _ { 1 } = \{ \mathsf { A } , \mathsf { C } \}$ and $G _ { 2 } = \{ \mathrm { B } , \mathrm { D } \}$ then $G _ { 1 , 2 } = G _ { 1 } \otimes G _ { 2 } = \{ \{ A > \mathrm { B } \} , \ \{ A > \mathrm { D } \} , \ \{ C > \mathrm { B } \} , \ \{ C > \mathrm { D } \} \}$ . If we prefer the items in $G _ { 1 }$ more than those in $G _ { 2 } ,$ there will be an arc from $G _ { 1 }$ to $G _ { 2 }$ in the preference graph.

De<sup>fi</sup>nition 4. (Relationship between item-pair and G-item-pair) Let α be a G-item-pair and x be an item-pair. Assume that α and x have the same items a and b. Then, the relationship between $\alpha _ { r }$ and x can be classi<sup>fi</sup>ed into three categories: comply, con<sup>fl</sup>ict, and no violation. Details are shown in Table 3.

When the relationship is comply, we have a>b in both $\alpha _ { r }$ and x. When the relationship is con<sup>fl</sup>ict, we have a>b in $\alpha _ { r }$ but $a = b$ or abb or $a \leq b$ in x. Finally, if the relationships is no violation, we have a>b in α but $a \geq b { \mathrm { ~ i n ~ } } x .$

De<sup>fi</sup>nition 5. (Sequence) A sequence is an ordered list of all n items in I. A sequence can be represented as $\beta = \{ a _ { 1 } \oplus a _ { 2 } \oplus . . . \oplus a _ { n } \}$ , where $a _ { i } \in I$ for $1 \leq i \leq n , a _ { i } \neq a _ { j }$ for i j, and $\oplus \in \{ > , \geq , = \}$ . Note that if the comparators in successive items are all $" = " ,$ , these items are ordered alphabetically.

De<sup>fi</sup>nition 6. (Relationship between two items in a sequence) Given a sequence $\beta = \{ a _ { 1 } \oplus _ { 1 } a _ { 2 } \oplus _ { 2 } . . . \oplus _ { n - 1 } a _ { n } \} ,$ let $R e l ( a _ { p } , a _ { q } , \beta )$ , where $p { < } q ,$ denote the relationship between items $a _ { p }$ and $a _ { q } \sin \beta ,$ which is de<sup>fi</sup>ned below.

(1) I $\boldsymbol { \mathrm { f } } \exists \oplus _ { j } \in \{ > \}$ , where $p { \le } j { \le } q - 1$ , then Rel $( a _ { p } , a _ { q } , \beta ) = " > " ;$

(2) If ∀⊕ ∈ {=}, for $p { \le } j { \le } q - 1$ , then $R e l ( a _ { p } , a _ { q } , \beta ) = " = " ;$

(3) Otherwise, $R e l ( a _ { p } , a _ { q } , \beta ) = \ " \geq " .$

For example, given a sequence $\beta = \{ { \tt A } > { \tt B } \geq { \tt D } = { \tt E } \}$ , we obtain Rel(A, E, $\beta ) = \ ' > " , R e l ( { \mathrm { B } } , { \mathrm { D } } , \beta ) = \ " \ge "$ , and $R e l ( \mathrm { D } , \mathrm { E } , \beta ) = " = "$

De<sup>fi</sup>nition 7. (Comply G-item-pair) G-item-pair α with items a and a complies with sequence β if the following conditions are satis<sup>fi</sup>ed: (1) items $a _ { i }$ and a also appear in $\beta ,$ and (2) Rel $( a _ { i } , a _ { j } , \alpha _ { r } )$ complies with $R e l ( a _ { i } , a _ { j } , \beta )$

Relationship between item-pair and G-item-pair.

<table><tr><td rowspan="2">Comparator</td><td rowspan="2"></td><td colspan="3"> $Rel(a, b, x)$ </td><td colspan="2"> $Rel(b, a, x)$ </td></tr><tr><td>&gt;</td><td>=</td><td>≥</td><td>&gt;</td><td>≥</td></tr><tr><td> $Rel (a, b, \alpha_r)$ </td><td>&gt;</td><td>Comply</td><td>Conflict</td><td>No violation</td><td>Conflict</td><td>Conflict</td></tr></table>

For example, assume we have sequence $\beta { = } \{ \mathtt { B } { > } { \mathtt { C } } { = } \mathtt { E } { \ge } \mathtt { D } { > } \mathtt { A } { > } \mathtt { H } \}$ and G-item-pair $\alpha _ { 1 } = \{ \mathsf { B } > \mathsf { A } \}$ . Then, $\alpha _ { 1 }$ complies with β, since Rel(B, A, $\alpha _ { 1 } ) { = } ^ { \mathfrak { n } }$ and $R e l ( \mathrm { B } , \mathrm { A } , \beta ) = \mathrm { \ " } > \mathrm { \ " }$

De<sup>fi</sup>nition 8. (Con<sup>fl</sup>ict G-item-pair) G-item-pair $\alpha _ { r }$ with items $a _ { i }$ and a con<sup>fl</sup>icts with sequence β if the following conditions are satis<sup>fi</sup>ed: (1) items $a _ { i }$ and $a _ { j }$ also appear in $\beta ,$ and $( 2 ) \ R e l ( a _ { i } , a _ { j } , \alpha _ { r } )$ con<sup>fl</sup>icts with Rel $( a _ { i } , a _ { j } , \beta )$ or $R e l ( a _ { j } , a _ { i } , \beta )$

For example, assume we have sequence $\beta = \{ \mathtt { E } > \mathtt { A } = \mathtt { B } \ge \mathtt { D } > \mathtt { C } > \mathtt { H } \}$ and item-pair $\alpha _ { 1 } = \{ \mathsf { B } > \mathsf { A } \}$ . Then, $\alpha _ { 1 }$ con<sup>fl</sup>icts with $\beta ,$ since Rel(B, A, $\alpha _ { 1 } ) { = } ^ { \mathfrak { n } }$ and $R e l ( { \tt A } , { \tt B } , { \beta } ) = " = "$

De<sup>fi</sup>nition 9. (No violation G-item-pair) G-item-pair $\alpha _ { r }$ with items $a _ { i }$ and $a _ { j }$ is in no violation with sequence $\beta$ if the following conditions are satis<sup>fi</sup>ed: (1) items a and $a _ { j }$ also appear in $\beta ,$ and $( 2 ) R e l ( a _ { i } , a _ { j } ,$ $\alpha _ { r } )$ is in no violation with $R e l ( a _ { i } , a _ { j } , \beta )$

For example, assume we have sequence $\beta = \{ \mathrm { E } > \mathrm { B } \ge \mathrm { A } > \mathrm { D } > \mathrm { C } > \mathrm { H } \}$ and item-pair $\alpha _ { 1 } = \{ \mathsf { B } > \mathsf { A } \}$ . Then, $\alpha _ { 1 }$ is in no violation with $\beta ,$ since $R e l ( \mathrm { B } , \mathrm { A } , \alpha _ { 1 } ) = \mathrm { \ " } > \mathrm { \ " }$ and $R e l ( \mathrm { B } , \mathrm { A } , \beta ) = \mathrm { ^ { 4 } } \geq ^ { \prime \prime }$

De<sup>fi</sup>nition 10. (Comply support) The comply support of G-item-pair $\alpha _ { r }$ in the database is de<sup>fi</sup>ned as:

$$
c m p \_ s u p (\alpha_ {r}) = | \{S _ {i} | S _ {i} \in D, \text {   and   } \alpha_ {r} \text {   complieswith   } S _ {i} \} | / | D |.\tag{1}
$$

For example, the comply support of $\{ \mathsf { A } > \mathsf { B } \}$ in Table 1 is 2/3, since {A>B} complies with $S _ { 1 }$ and $S _ { 2 } .$

De<sup>fi</sup>nition 11. (Con<sup>fl</sup>ict support) The con<sup>fl</sup>ict support of G-item-pair $\alpha _ { r }$ in the database is de<sup>fi</sup>ned as:

$$
c f \_ s u p (\alpha_ {r}) = | \{S _ {i} | S _ {i} \in D, \text {   and   } \alpha_ {r} \text {   conflictswith   } S _ {i} \} | / | D |.\tag{2}
$$

For example, the con<sup>fl</sup>ict support of $\{ \mathsf { A } > \mathsf { B } \}$ in Table 1 is 1/3, sinc {A>B} con<sup>fl</sup>icts with $S _ { 3 } .$

De<sup>fi</sup>nition 12. (Consensus item-pair) Let cmp\_minsup and cf\_maxsup be the user speci<sup>fi</sup>ed thresholds. G-item-pair $\alpha _ { r }$ is called a consensus item-pair if it satis<sup>fi</sup>es the following constraints: cmp $\_ s u p ( \alpha _ { r } ) { \geq }$ cmp\_minsup and $c f \_ s u p ( \alpha _ { r } ) \leq c f _ { - }$ \_maxsup.

De<sup>fi</sup>nition 13. (Consensus support) In a set of G-item-pairs $G _ { i j } ,$ the consensus support is the percentage of G-item-pairs in $G _ { i j }$ that are in consensus. It is de<sup>fi</sup>ned as:

$$
\text { consensus\_sup } \left(G _ {i j}\right) = \left| \left\{\alpha_ {r} | \alpha_ {r} \in G _ {i j}, \text {   and   } \alpha_ {r} \text {   is   a   consensus   item   -   pair } \right\} | / | G _ {i j} |. \right.\tag{3}
$$

For example, if $G _ { 1 2 } = \{ \{ A > B \} , \{ A > D \} , \{ C > B \} , \{ C > D \} \}$ and $\{ \mathsf { A } > \mathsf { B } \}$ $\{ { \mathsf { C } } > { \mathsf { B } } \}$ are consensus item-pairs, then consensus\_sup $( G _ { 1 2 } ) = 2 / 4$

De<sup>fi</sup>nition 14. (Consensus arcs between groups) Let consensus\_minsup be the user speci<sup>fi</sup>ed threshold. A consensus arc from group $G _ { i }$ to $G _ { j } ,$ denoted as $c a _ { i j } ,$ exists if it satis<sup>fi</sup>es the following constraints: consensus $s u p ( G _ { i j } ) \geq$ consensus\_minsup.

For example, suppose we have $G _ { 1 } = \{ \mathrm { A } , \mathbb { C } \} , G _ { 2 } = \{ \mathrm { B } , \mathrm { D } \}$ , and $G _ { 3 } = \{ \mathrm { E } \} .$ According to $G _ { i j } { = } G _ { i } \otimes G _ { j } ,$ we have 4 G-item-pairs $\{ \{ \mathsf { A } { \scriptstyle \mathsf { > B } } \} , \ \{ \mathsf { A } { \scriptstyle \mathsf { > D } } \}$ $\{ \mathsf { C } > \mathsf { B } \} , \ \{ \mathsf { C } > \mathsf { D } \} \}$ in $G _ { 1 2 } .$ If cmp\_minsup is 0.6 and cf\_maxsup is 0.4, we <sup>fi</sup>nd in Table 1 that $\{ \mathsf { A } > \mathsf { B } \} , \{ \mathsf { A } > \mathsf { D } \} , \{ \mathsf { C } > \mathsf { B } \} , \{ \mathsf { C } > \mathsf { D } \}$ are consensus item-pairs, so consensus\_sup is 1. If consensus\_minsup is 0.5, then the arc from $G _ { 1 }$ to $G _ { 2 }$ is a consensus arc.

De<sup>fi</sup>nition 15. (Consensus graph) From users' ranking lists, we can draw a graph $G = \{ E , V \}$ to represent users' consensus on the relationships between groups, where V is the set of groups and E is the set of consensus arcs between groups.

For example, we may draw a consensus graph like Fig. 2 from the data in Table 1, where the value along each arc is consensus support.

![](/api/attachments/5H4GUQNJ/fulltext/images/cfd0f1e39c84d5afa046e6ab01cedab7f677542a9e70ed71198b8772fd184dc7.jpg)  
Fig. 2. A sample preference graph.

Many graphs can be constructed from the same preference data. Which graph is better? We use the following criteria to measure the appropriateness of a graph: graph support and arc density.

De<sup>fi</sup>nition 16. (Graph support) The graph support, denoted as graph\_sup, is the average of all consensus arcs' consensus supports.

For example, graph support in Fig. 2 is 1.

De<sup>fi</sup>nition 17. (Density of arc) The arc density is the percentage of all potential arcs in the graph that are consensus arcs. Assume we have k groups. Then, the number of potential arcs is $C ^ { k } { } _ { 2 } ,$ and the arc density can be represented as $d _ { - } a r c = \left| E \right| / C _ { 2 } ^ { k }$

For example, in Fig. 2 the number of all potential arcs is $3 \ ( C ^ { 3 } { } _ { 2 } )$ and there are three consensus arcs, so the arc density is 1.

De<sup>fi</sup>nition 18. (Objective) We use the following objective function to measure the appropriateness of a graph, where $0 \leq \gamma \leq 1$ is speci<sup>fi</sup>ed by users.

$$
o b j e c t \_ f u n = \gamma \times g r a p h \_ s u p + (1 - \gamma) \times d \_ a r c.\tag{4}
$$

The graph support represents the percentage of users who support the consensus arcs in the graph. On the other hand, the arc density represents the percentage of arcs that become consensus. When the arc density is higher, it means more arcs become consensus. When the graph support is higher, it means the consensus arcs have more users' support. Since a better graph should have more arcs with more users' support, both measures should be as large as possible. Therefore, we set the weighted sum of them as our objective.

## 4. The algorithm

In this section, we propose a genetic algorithm (GA) to discover preference graphs from users' total ranking lists. The procedure is listed below.

1. Sort the items' scores and partition the sorted data into k groups.

2. Iteratively generate |P| chromosomes by the following steps. (1) For each item score, randomly increase or decrease by a percentage no more than R%.

(2) Sort the data and partition them into k groups.

3. Build the preference graph for every chromosome.

4. Iteratively use GA algorithm to re-cluster groups so that the objective can be improved, where the objective includes the graph support and arc density.

5. Draw the <sup>fi</sup>nal graph.

Table 4 Computation of items' scores.

<table><tr><td></td><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td></tr><tr><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td> $1 + 1$ </td></tr><tr><td>2</td><td>0</td><td> $1 + {0.5}$ </td><td>1</td><td>1</td><td> $1 + 1 + {0.5}$ </td></tr><tr><td>3</td><td>1</td><td>1</td><td>0</td><td> $1 + {0.5}$ </td><td> $1 + 1 + {0.5}$ </td></tr><tr><td>Total</td><td>1</td><td>3.5</td><td>1</td><td>3.5</td><td>7</td></tr></table>

## Detailed explanation of the algorithm's steps:

## Step 1: data transformation and partitioning

To compute the score of an item, we examine that item's position in every sequence. If the comparators before the item in the sequence are $^ { u } > ^ { v } , \ ^ { u } \ge ^ { v } , 0 \Gamma ^ { u } = ^ { v }$ , we add 1, 0.5, or 0 to the item's score, respectively. The score of an item is de<sup>fi</sup>ned as the sum of the values of that item in all sequences. For example, the item scores in Table 1 are shown in Table 4.

Then, we sort the items in non-descending order by the item's score and partition the data into k clusters that are roughly the same size. For example, we <sup>fi</sup>rst sort the items in Table 4. Then, if we partition them into three clusters, we get three groups ${ \cal G } _ { 1 } = \{ \mathsf { A } ,$ C}, $G _ { 2 } = \{ \mathtt { B } , \mathtt { D } \}$ , and $G _ { 3 } = \{ \mathrm { E } \}$ , as shown in Table 5.

## Step 2: generate the population of chromosomes

We randomly increase or decrease each item's score by no more than R%. Then, we re-sort the items in non-descending order using the new scores. Data is re-grouped into k clusters and partitioned into clusters of roughly the same size. This is repeated until |P| chromosomes are generated. The items' weights are changed so that we can generate different chromosomes. A chromosome is represented by an array of n elements, where n is the total number of items. As shown in Table 5, there are three groups $G _ { 1 } = \{ \mathrm { A } , \ \mathrm { C } \} , \ G _ { 2 } = \{ \mathrm { B } , \ \mathrm { D } \}$ and $G _ { 3 } = \{ \mathrm { E } \}$ . The chromosome can be represented as shown in Fig. 3. Note that the number recorded in an element indicates which group the element belongs to.

## Step 3: build the preference graph for every chromosome

To build the graph, we must determine whether link $G _ { i } > G _ { j }$ exists for all pairs in groups $G _ { i }$ and $G _ { j } .$ This can be accomplished using the following procedure. First, generate the set of G-item-pairs $G _ { i j } =$ $G _ { i } \otimes G _ { j } .$ Second, compute the comply support and con<sup>fl</sup>ict support of $G _ { i j } .$ Third, compute the consensus support. If consensus\_support is bigger than or equal to consensus\_minsup, there is a link from $G _ { i }$ to $G _ { j } .$

## Step 4: GA procedure

After we produce the initial population of individuals, we evaluate the <sup>fi</sup>tness of each individual in that population. Objective function de<sup>fi</sup>ned in Eq. (4) is used as the <sup>fi</sup>tness function to measure the quality of a chromosome. The higher the <sup>fi</sup>tness function value, the better quality of a chromosome.

Genetic operators involve selection, crossover and mutation. They are used to reproduce the next generation. We select the best-<sup>fi</sup>t individuals for reproduction using Roulette Wheel Selection. A proportion of the wheel is assigned to each of the possible chromosomes based on their <sup>fi</sup>tness value. Its probability of being selected is shown below

Partition of the sorted data into three groups.

<table><tr><td></td><td>A</td><td>C</td><td>B</td><td>D</td><td>E</td></tr><tr><td>Total</td><td>1</td><td>1</td><td>3.5</td><td>3.5</td><td>7</td></tr></table>

![](/api/attachments/5H4GUQNJ/fulltext/images/22a6e30f3bf1f7baed8be57b574b94ea21dcb5726bb18b515456c3410e29a06b.jpg)  
Fig. 3. An example chromosome.

$$
p _ {i} = \frac {f _ {i}}{\sum_ {j = 1} ^ {N} f _ {j}} \times N\tag{5}
$$

where $f _ { i }$ is the <sup>fi</sup>tness of individual i in the population and N is the number of individuals in the population.

We use double-point crossover operator to randomly select two crossover points within a chromosome. Then we interchange the two parent chromosomes between these points to create two new offspring [16]. For example, assume that we have two parent chromosomes, where the <sup>fi</sup>rst chromosome is $G _ { 1 } = \{ \mathrm { A } , \ \mathrm { B } \} , \ G _ { 2 } = \{ \mathrm { C } , \ \mathrm { D } \}$ , and $G _ { 3 } = \{ \mathrm { E } \}$ and the second chromosome is $G _ { 1 } = \{ { \sf A } \} , G _ { 2 } = \{ { \sf B } , { \sf C } \}$ , and $G _ { 3 } = \{ \mathrm { D } , \mathrm { E } \}$ . If the crossover points are A and D, then the crossover procedure may look like Fig. 4.

Mutation can prevent to <sup>fi</sup>nd local optimal solution. To avoid search process stagnation, we occasionally adjust an item's belonging group. Every item in a chromosome has a probability of mutation. If it is selected to mutate, the group number is randomly changed.

By repeatedly processing the GA procedure which includes selection, crossover, mutation and evaluation, we can determine the relationship among groups. Finally, we can draw the <sup>fi</sup>nal preference graph.

## 5. Experiments

To evaluate the ef<sup>fi</sup>ciency and effectiveness of the proposed preference graph algorithm, we performed several experiments using synthetic data sets. In this section, we <sup>fi</sup>rst describe the generation of the synthetic data set and the comparisons of run time and objective function. In the second portion, a real case study is applied to show the usefulness of consensus sequence mining in practice.

## 5.1. Synthetic data generation

In the following experiments, we generated several synthetic data sets composed of complete sequences. The parameters used in our data generation algorithm are listed in Table 6. Each synthetic data set is composed of |U| users' sequences that are full orderings of |I| items. Based on initial seed sequences, dcr% of |U| users' sequences and dcr% of |I| items in these user sequences are preserved in the same order, and others are generated randomly. In this way, a higher consensus rate creates a synthetic data set comprised of items with more coherent rankings. Two levels of data consensus rates (33% and 50%) were used in this experiment.

![](/api/attachments/5H4GUQNJ/fulltext/images/8e63b27da30bd727b72586899dfbfdde70ffc2d6f7f68ed67855ea520fef2678.jpg)  
Fig. 4. An example of crossover.

Table 6  
Parameters used in data generation.

<table><tr><td>Parameter</td><td>Description</td></tr><tr><td>|U|</td><td>Number of users</td></tr><tr><td>|I|</td><td>Number of items</td></tr><tr><td>dcr</td><td>Data consensus rate</td></tr></table>

5.2. Run time comparisons and objective value comparisons

We compared the algorithm's run times and objective values using the following different parameters. The parameters concerning the preference graph de<sup>fi</sup>nition and GA procedure are listed in Table 7.

In the baseline, we set k=7, cf\_maxsup=0.25, cmp\_minsup=0.5, consensus\_minsup=0.5, |P|=50, γ=0.5, R=0.1, ir=50, csr=0.8, mr=0.2 and adjust one parameter at a time to analyze the results. It would be excessively tedious to report how each of these parameters affected the algorithm's run time and objective value. According to our experiment results, most of these parameters have no signi<sup>fi</sup>- cant impact on the run time. Therefore, we only report the results of those parameters that may in<sup>fl</sup>uence run time and objective value.

The comparison can be divided into two groups. In the <sup>fi</sup>rst group comparison, we looked at how the parameters used in preference graph de<sup>fi</sup>nition affect the objective value and run time. Note that when the values of these parameters change, the solution (i.e., optimal objective value), also changes. In the second group comparison, we investigated how the parameters used in GA procedure, affect the objective value and run time. Note that the parameters concerning GA procedure do not change the optimal objective value, but setting better parameter values can help us search more ef<sup>fi</sup>ciently and effectively for solutions.

Since the objective is a weighted sum of graph support and arc density, both of which are valued between 0 and 1, the objective value is also valued between 0 and 1. The larger objective value is, the better solution will be got.

5.2.1. How parameters concerning preference graph definition affect the objective and run time

To investigate the influence of $k ,$ we varied the value of k from 4 to 10. As shown in Table 8, the objective value increases as k increases. This is because when items are partitioned into more groups, more consensus arcs are generated. We also observed, however, that the in-<sup>fl</sup>uence of k on the run time is not very signi<sup>fi</sup>cant.

The results in Table 8 indicate that the objective value decreases as the minimum comply support threshold increases. This is because when cmp\_minsup is increased, it becomes more dif<sup>fi</sup>cult for arcs to satisfy the threshold constraints and reach consensus. As a result, the graph would have fewer arcs, decreasing the objective value. The in<sup>fl</sup>uence of cmp\_minsup on the run time is not very signi<sup>fi</sup>cant.

Table 7 Parameters used in the experiments.

<table><tr><td>Parameter</td><td>Description</td></tr><tr><td colspan="2">Parameters concerning the preference graph definition</td></tr><tr><td>k</td><td>Number of groups</td></tr><tr><td>cmp_minsup</td><td>Comply support threshold</td></tr><tr><td>cf_maxsup</td><td>Conflict support threshold</td></tr><tr><td>consensus _minsup</td><td>Consensus support threshold</td></tr><tr><td>γ</td><td>The weight of graph support</td></tr><tr><td colspan="2">Parameters concerning the GA procedure</td></tr><tr><td>|P|</td><td>Number of populations</td></tr><tr><td>mr</td><td>Mutation rate</td></tr><tr><td>R</td><td>The maximum percentage to change item&#x27;s weight</td></tr><tr><td>ir</td><td>The number of iterations.</td></tr><tr><td>csr</td><td>Crossover rate</td></tr></table>

Table 8  
Parameters concerning preference graph de<sup>fi</sup>nition vs. objective and run time

<table><tr><td colspan="2">Data sets</td><td colspan="2">50I33DCR</td><td colspan="2">100I33DCR</td><td colspan="2">50I50DCR</td><td colspan="2">100I50DCR</td></tr><tr><td colspan="2">Parameters</td><td>Objective</td><td>Run time</td><td>Objective</td><td>Run time</td><td>Objective</td><td>Run time</td><td>Objective</td><td>Run time</td></tr><tr><td rowspan="3">k</td><td>4</td><td>0.508</td><td>294</td><td>0.522</td><td>1642</td><td>0.649</td><td>236</td><td>0.660</td><td>1865</td></tr><tr><td>7</td><td>0.578</td><td>298</td><td>0.559</td><td>1873</td><td>0.657</td><td>268</td><td>0.656</td><td>1905</td></tr><tr><td>10</td><td>0.612</td><td>301</td><td>0.578</td><td>2025</td><td>0.670</td><td>293</td><td>0.677</td><td>1931</td></tr><tr><td rowspan="3">cmp_minsup</td><td>0.2</td><td>0.656</td><td>302</td><td>0.594</td><td>1897</td><td>0.641</td><td>270</td><td>0.644</td><td>1885</td></tr><tr><td>0.5</td><td>0.578</td><td>294</td><td>0.559</td><td>1873</td><td>0.657</td><td>268</td><td>0.656</td><td>1905</td></tr><tr><td>0.8</td><td>0.530</td><td>296</td><td>0.492</td><td>1902</td><td>0.546</td><td>269</td><td>0.561</td><td>1868</td></tr><tr><td rowspan="3">cf_maxsup</td><td>0.25</td><td>0.578</td><td>294</td><td>0.559</td><td>1873</td><td>0.578</td><td>268</td><td>0.559</td><td>1905</td></tr><tr><td>0.35</td><td>0.681</td><td>284</td><td>0.649</td><td>1878</td><td>0.681</td><td>268</td><td>0.649</td><td>1829</td></tr><tr><td>0.55</td><td>0.791</td><td>334</td><td>0.860</td><td>1882</td><td>0.791</td><td>271</td><td>0.860</td><td>1865</td></tr><tr><td rowspan="3">consensus_minsup</td><td>0.2</td><td>0.542</td><td>302</td><td>0.696</td><td>1897</td><td>0.733</td><td>270</td><td>0.752</td><td>1885</td></tr><tr><td>0.5</td><td>0.578</td><td>294</td><td>0.559</td><td>1873</td><td>0.657</td><td>268</td><td>0.656</td><td>1905</td></tr><tr><td>0.8</td><td>0.578</td><td>296</td><td>0.556</td><td>1902</td><td>0.634</td><td>269</td><td>0.609</td><td>1868</td></tr></table>

Next, we varied the value of cf\_maxsup to observe its effect on the objective value and run time. The in<sup>fl</sup>uence of cf\_maxsup on the run time is not very signi<sup>fi</sup>cant. However, the objective value increases as the maximum con<sup>fl</sup>ict support threshold increases. This is because when cf\_maxsup is increased, it becomes easier for arcs to satisfy the threshold constraints and reach consensus. As a result, the graph would have more arcs, increasing the objective value.

In addition, we observe that as consensus\_minsup increases, the objective value decreases. This is because when consensus\_minsup is increased, it becomes more dif<sup>fi</sup>cult for arcs to satisfy the threshold constraints. As a result, the graph would have fewer arcs, decreasing the objective value. However, we also observed that when the data consensus rate is low, a low consensus\_minsup can achieve a better objective value than a high consensus\_minsup. One possible reason is as follows. The objective function has two components: graph support and arc density. When the data consensus rate and consensus\_minsup are both low, many arcs with low consensus supports may reach consensus. This results in low graph support, which in turn makes the objective value low.

According to our experiment results, these four parameters have no signi<sup>fi</sup>cant impact on the run time. In regards to the objective value, parameter cf\_maxsup has the greatest impact. When k=7 and cf\_maxsup=0.55, the objective value is the largest.

## 5.2.2. How parameters concerning GA procedure affect the objective and run time

In this experiment, we varied the number of populations, |P|, from 20 to 100. The results indicate that the run time increases linearly as the number of populations increases. This is because the number of crossover and mutation operations increases linearly with the population size. However, the objective value increases as the number of populations increases. This is because when more populations are produced, the chances of <sup>fi</sup>nding a better solution increase. We also noted that |P| is probably the most important factor among all parameters concerning GA procedure, because when using the same data set, the best objective value was mostly achieved by increasing the value of |P|.

Next, we varied R, the maximum percentage to change an item's score to produce new populations, from 5% to 30%. As shown in Table 9, it seems that low (5%) and high (30%) R values generate better objective values than medium (10%) R values. This is because the <sup>fi</sup>rst population generated by counting an item's score is usually quite good. After that, we use the R value to increase or decrease an item's score to produce new populations. When R is low, all populations have similar <sup>fi</sup>tness values as the <sup>fi</sup>rst population, making it easy to select a good population to reproduce. When R is high, in general, it leads to many populations with zero <sup>fi</sup>tness values. To resolve this situation, we selected the <sup>fi</sup>rst population to reproduce in the GA algorithm, thereby obtaining a better <sup>fi</sup>tness value. On the other hand, medium R values usually result in populations with worse nonzero <sup>fi</sup>tness values, which is why low (5%) and high (30%) R values attain better objective values than medium (10%) R values.

Next, we varied the number of iterations, ir, from 1 to 100. The re sults indicate that the run time increases linearly as the number of iterations increases. This is because when the number of iterations is increased, the algorithm will run more repetitions. As shown in Table 9, the objective function converges as the number of iterations increases. It seems that running the GA procedure 50 times leads to convergence with the <sup>fi</sup>nal objective value. This is because the <sup>fi</sup>rst population generated by counting and sorting is usually very good, about 90% of the <sup>fi</sup>nal value. Therefore, after a few more iterations of adjustments, the objective value cannot be improved any further.

The in<sup>fl</sup>uence of csr, the percentage of populations that will have crossover, on the preference graph algorithms' objective function is shown in Table 9. We varied csr from 40% to 100%. The results seem to show that a high csr has a greater chance of obtaining high <sup>fi</sup>tness values than a low csr; when csr is 80%, achieves the best <sup>fi</sup>tness value.

The in<sup>fl</sup>uence of mr, the percentage of items that will be mutated in every population, on the preference graph algorithms' objective function is shown in Table 9. We varied mr from 10% to 50%. The results seem to show that a low mr has a better chance of attaining a high <sup>fi</sup>tness value than a high mr; when mr is 20%, it achieves the best <sup>fi</sup>tness value. The in<sup>fl</sup>uence of mr on the run time is not very signi<sup>fi</sup>cant.

## Table 9

Parameters concerning GA procedure vs. objective and run time

<table><tr><td colspan="2">Data sets</td><td colspan="2">50I33DCR</td><td colspan="2">100I33DCR</td><td colspan="2">50I50DCR</td><td colspan="2">100I50DCR</td></tr><tr><td colspan="2">Parameters</td><td>Objective</td><td>Run time</td><td>Objective</td><td>Run time</td><td>Objective</td><td>Run time</td><td>Objective</td><td>Run time</td></tr><tr><td rowspan="3">|P|</td><td>20</td><td>0.551</td><td>115</td><td>0.538</td><td>785</td><td>0.650</td><td>116</td><td>0.652</td><td>807</td></tr><tr><td>50</td><td>0.578</td><td>294</td><td>0.559</td><td>1873</td><td>0.657</td><td>268</td><td>0.656</td><td>1905</td></tr><tr><td>100</td><td>0.648</td><td>614</td><td>0.616</td><td>3739</td><td>0.669</td><td>639</td><td>0.670</td><td>3879</td></tr><tr><td rowspan="3">R</td><td>0.05</td><td>0.580</td><td>289</td><td>0.541</td><td>1883</td><td>0.669</td><td>266</td><td>0.672</td><td>1924</td></tr><tr><td>0.1</td><td>0.578</td><td>294</td><td>0.559</td><td>1873</td><td>0.657</td><td>268</td><td>0.656</td><td>1905</td></tr><tr><td>0.3</td><td>0.601</td><td>288</td><td>0.581</td><td>1904</td><td>0.668</td><td>270</td><td>0.661</td><td>1874</td></tr><tr><td rowspan="4">ir</td><td>1</td><td>0.541</td><td>6</td><td>0.538</td><td>38</td><td>0.625</td><td>5</td><td>0.640</td><td>37</td></tr><tr><td>25</td><td>0.585</td><td>184</td><td>0.576</td><td>962</td><td>0.642</td><td>136</td><td>0.651</td><td>1064</td></tr><tr><td>50</td><td>0.586</td><td>294</td><td>0.578</td><td>1873</td><td>0.643</td><td>268</td><td>0.651</td><td>1905</td></tr><tr><td>100</td><td>0.586</td><td>582</td><td>0.578</td><td>3846</td><td>0.643</td><td>538</td><td>0.651</td><td>3821</td></tr><tr><td rowspan="3">csr</td><td>0.4</td><td>0.567</td><td>307</td><td>0.548</td><td>1932</td><td>0.633</td><td>269</td><td>0.639</td><td>1908</td></tr><tr><td>0.8</td><td>0.578</td><td>294</td><td>0.559</td><td>1873</td><td>0.657</td><td>268</td><td>0.656</td><td>1905</td></tr><tr><td>1</td><td>0.572</td><td>295</td><td>0.554</td><td>1866</td><td>0.641</td><td>271</td><td>0.644</td><td>1832</td></tr><tr><td rowspan="3">mr</td><td>0.1</td><td>0.575</td><td>291</td><td>0.555</td><td>1903</td><td>0.644</td><td>273</td><td>0.643</td><td>1856</td></tr><tr><td>0.2</td><td>0.578</td><td>294</td><td>0.559</td><td>1873</td><td>0.657</td><td>268</td><td>0.656</td><td>1905</td></tr><tr><td>0.5</td><td>0.565</td><td>294</td><td>0.538</td><td>1947</td><td>0.631</td><td>287</td><td>0.639</td><td>1867</td></tr></table>

![](/api/attachments/5H4GUQNJ/fulltext/images/65e64bccbfd3313ef3b2455ce0527e2b2867aa25af50170c83f0e21761993906.jpg)  
Fig. 5. Effect of |U| on the run time performance.

![](/api/attachments/5H4GUQNJ/fulltext/images/504387420d1236d82139c24eea947100d76f1a2ebea0e046d1750da3b7834740.jpg)  
Fig. 6. Effect of |I| on the run time performance.

## 5.3. Scalability

This section investigates the scalability of the proposed algorithm. The <sup>fi</sup>rst part of the experiment concerns the number of users, |U|, and the second part concerns the number of items per seed sequence, |I|.

![](/api/attachments/5H4GUQNJ/fulltext/images/763b4054e77055e874baf17b1b5ad08c070d8875c77188df0fd90498f9b0ffb0.jpg)  
(a) consensus\_minsup = 0.2

## 5.3.1. Effect of |U| on run time performance

In scaling up |U|, we varied the number of users from 200 to 1200, set k=7, cf\_maxsup=0.25, cmp\_minsup=0.5, consensus\_minsup= $0 . 5 , \ \gamma = 0 . 5 , \ R = 0 . 1 , \ i r = 5 0 , \ c s r = 0 . 8 ,$ , and mr=0.2. The x-axis and y-axis represent the number of users and the run time, respectively. As shown in Fig. 5, run time increases linearly with the number of users.

![](/api/attachments/5H4GUQNJ/fulltext/images/90a6aa3a5f0f319a5c22f59ee466c67e367fc11eea2a333608637e2b12aa0c8d.jpg)

## 5.3.2. Effect of |I| on run time performance

In scaling up |I|, we varied the number of items from 50 to 300, set k=7, cf\_maxsup=0.25, cmp\_minsup=0.5, consensus\_minsup=0.5, γ=0.5, R=0.1, ir=50, csr=0.8, and mr=0.2. The x-axis and y-axis represent the number of items and the run time, respectively. Fig. 6 shows that the algorithm's run time grows exponentially with the number of items.

## 5.4. Real case study

We composed a data set of 50 pictures of women from the site 140.115.222.54/belle. The ranking lists in the belle data set were collected from 221 users. From these preference data, we want to reach a consensus on the belle data set. The belle consensus information would be valuable in selecting which types of women might be successful as advertising models or activity/product endorsers in Taiwan. At <sup>fi</sup>rst, we evaluate the effectiveness of the proposed methods using belle data set. Then we applied the method proposed in previous work to evaluate the same dataset and make comparisons between the proposed approach and previous work.

## 5.4.1. The result of preference graph approach

In the experiments, we set cmp\_minsup=0.5, cf\_maxsup=0.25, and γ=0.5. The belle data set was grouped into k clusters, where k is 4 and 10. For every k value, we obtained three different preference graphs using three different consensus\_minsup: 0.2, 0.5, and 0.8. Finally, we drew a <sup>fi</sup>nal preference graph by combining the three different preference graphs. Figs. 7 and 8 show the preference graph results constructed by the proposed algorithm as $k = 4$ and 10. In these <sup>fi</sup>gures, P represents parent and C represents child. If a group has 2 parents and 1 child, it means there are two groups going into this group and this group is directed to one group. Tables 10 and 11 show the items in every k-group.

(c) consensus\_minsup = 0.8  
![](/api/attachments/5H4GUQNJ/fulltext/images/bb629c0350dbf7df90942380ab7986328be46668eb647b78138fae4a77f1674b.jpg)  
(b) consensus\_minsup = 0.5

![](/api/attachments/5H4GUQNJ/fulltext/images/df4cc87787a3743ccad58c08edfb35b4b4b408f3bafaa55424f6c3ec004e2234.jpg)  
(b) final preference graph  
Fig. 7. The preference graphs of belle (k=4).

Fig. 7(a), (b) and (c) shows the preference graph results when the number of groups is 4 and consensus\_minsup is set to 0.2, 0.5 and 0.8, respectively. Fig. 7(d) is the <sup>fi</sup>nal preference graph aggregated from these three graphs. As shown in Fig. 7(d), a consensus arc is the thickest if the consensus\_sup between two groups is greater than 80%, and a consensus arc is the thinnest if the consensus\_sup between two groups is greater than 20% but less than 50%. We observed that $( G _ { 1 } > G _ { 2 } > G _ { 4 } ) , ( G _ { 1 } > G _ { 3 } > G _ { 4 } )$ and $\left( G _ { 1 } > G _ { 4 } \right)$ in Fig. 7(d). This means the women in $G _ { 1 }$ are the most popular for the majority of users, while the women in $G _ { 4 }$ are the least popular.

The numbers of node parents and children are also helpful when analyzing preferences between two or more groups. From Fig. 8, we see that there is no connection between $G _ { 2 ^ { \prime } }$ and $G _ { 3 ^ { \prime } }$ . If we want to learn the preferences between these two groups, the <sup>fi</sup>gure shows that $G _ { 2 ^ { \prime } }$ has same number of parents as $G _ { 3 ^ { \prime } }$ , but $G _ { 2 ^ { \prime } }$ has more children than $G _ { 3 ^ { \prime } } .$ This means most people think $G _ { 2 ^ { \prime } }$ is more dominant than $G _ { 3 ^ { \prime } } ,$ meaning $G _ { 2 ^ { \prime } }$ is more popular than $G _ { 3 ^ { \prime } }$

The edges shown in a preference graph mean that a majority of people agree upon the corresponding relationships between groups. As shown in Fig. 8, all graph results indicate that $\left( G _ { 1 ^ { \prime } } { > } G _ { 6 ^ { \prime } } { > } G _ { 1 0 ^ { \prime } } \right)$ and $( G _ { 1 ^ { \prime } } { > } G _ { 7 ^ { \prime } } { > } G _ { 1 0 ^ { \prime } } ) . G _ { 1 }$ has the most outward links to other groups, and $G _ { 1 0 ^ { \prime } }$ has the most inward links from other groups. This means that the women in $G _ { 1 ^ { \prime } }$ are the most popular for the majority of users, and that the women in $G _ { 1 0 ^ { \prime } }$ are the least popular. Our investigation indicates that most people in Taiwan prefer Eastern beauty. Since the women in $G _ { 1 ^ { \prime } }$ all seem to have pale skin and Eastern faces, and those in $G _ { 1 0 ^ { \prime } }$ have different skin colors, we may conclude that a woman with Eastern features would be most successful as an advertising model or activity/product endorser in Taiwan. Similar conclusions can also be observed from Fig. 7, where most women in $G _ { 1 ^ { \prime } }$ and $G _ { 1 0 ^ { \prime } }$ belong to $G _ { 1 }$ and $G _ { 4 } ,$ respectively.

## 5.4.2. A comparison with previous work

To <sup>fi</sup>nd maximum consensus lists from the belle data set, we applied the MCS algorithm [5] developed in our previous work to the data set. Table 12 summarizes the results of <sup>fi</sup>nding maximum consensuses when cmp\_minsup=0.5 and cf\_maxsup=0.25. The number of maximum consensuses sequences is 446 and the length of the longest maximum consensuses sequence is only 3. (2>1), (2>10) and $( 3 2 > 9 > 1 0 )$ are three examples of maximum consensus sequences found by the MCS algorithm, where a number refers to a certain beauty.

Since it is dif<sup>fi</sup>cult to use, interpret or get insight from these 446 sequences, we do our best to summarize the discovered results. Since most maximum sequences have length 2, we roughly divide all the items into two groups, where group 2 = {1, 10, 16, 33, 48} as shown in Table 13 and group 1 contains the remaining ones. The results show that a majority of users like items of group 1 more than the items of group 2.

![](/api/attachments/5H4GUQNJ/fulltext/images/3b84cb6738ad872858f0c784910047df7bee5f74ab57aa8c319b4ac549629a95.jpg)  
Fig. 8. The preference graphs of belle (k=10).

Table 10 The result of belle (k= 4).  
![](/api/attachments/5H4GUQNJ/fulltext/images/108b5a7c917e16c44ac1e678432b273c081a872b96434dfbe2e63630fb3bfaac.jpg)

Since the personal aesthetic signi<sup>fi</sup>cantly affects the user' preference of beauty, it is dif<sup>fi</sup>cult to achieve consensus. This is the reason why the consensus sequences have short length. It was also observed that there was difference in preference for the items in the same groups. When there is no consensus or only slight consensus on items' rankings, the algorithm MCS may generate too many maximum consensus sequences, which make decision makers dif<sup>fi</sup>cult to use the results.

Contrarily, if we use the proposed method to analyze the same dataset, we will get preference graphs like Figs. 7 and 8. The preference graph provides useful clues for marketing campaigns. Suppose the items in a group are products instead of women. At <sup>fi</sup>rst, we can identify “hot group” of items. For example, $G _ { 1 }$ in Fig. 7 and $G _ { 1 ^ { \prime } }$ in Fig. 8 are hot groups. A “hot group” refers to a group having the most outward links to other groups. In other words, it is more popular than the products in the other groups for most users. Having identi<sup>fi</sup>ed “hot group”, we can recommend items of hot group to users, because a user may like the products that most users like. In addition, we can identify “cold group”, where a group is “cold” if it has the most inward links from

The result of belle (k=10).  
![](/api/attachments/5H4GUQNJ/fulltext/images/93404a13eba8cd5cc6ca6af696284b1b6f13c2bdc41d06d0e2a3e5025ddc5ce1.jpg)

African

Table 12  
Results for real case study.

<table><tr><td>Length of consensus lists</td><td>Number of sequences</td></tr><tr><td>2</td><td>445</td></tr><tr><td>3</td><td>1</td></tr></table>

Table 13

The items of group 2.

![](/api/attachments/5H4GUQNJ/fulltext/images/4f35caabfd83785fefced3109ba3e679c14fc187d9e5aa53bfe62ad9b35870b7.jpg)

other groups. The items in the cold group are the least popular products. We can simply take these cold items off the shelf, improve their packaging, or enhance their advertisements.

## 6. Conclusions

Generally, traditional group ranking problems can be classi<sup>fi</sup>ed according to the completeness of the user-provided preference information, the types of compromise outcomes, and the format used to express user preferences. In this work, we proposed a method that can <sup>fi</sup>nd maximum agreeable preferences and represent the results as a graph. This is called a preference graph. An algorithm was developed to <sup>fi</sup>nd a preference graph from users' ranking data. Extensive experiments were also carried out to examine the algorithm's performance. Several synthetic data sets were used in our performance analyses and scalability tests. Experimental results showed the effects of every parameter on the run times and objective values. Finally, a real case study showed satisfactory and acceptable results for the proposed algorithms.

It is easy to see many future extensions. We all know that there are already many variants of the group ranking problem. However, none of these previous variants have generated a preference graph as the output. If the output knowledge type of these traditional approaches is changed to preference graphs, we believe this will open the door to a large array of future research issues.

## Acknowledgment

It is our pleasure to acknowledge the anonymous reviewers for their valuable suggestions and the careful reading of our manuscript. The authors would like to express our gratitude to these reviewers for their suggestions that helped to substantially improve our paper. This study was supported by the National Science Council of Taiwan under grant NSC 97-2410-H-031-056 and 101-2410-H-008-008-MY3.

## References

[1] J. Bartholdi, C.A. Tovey, M.A. Trick, Voting schemes for which it can be dif<sup>fi</sup>cult to tell who won the election, Social Choice and Welfare 6 (2) (1989) 157–165.

[2] M.M.S. Beg, N. Ahmad, Soft computing techniques for rank aggregation on the World Wide Web, World Wide Web: Internet and Web Information Systems 6 (1) (2003) 5–22.

[3] K. Bogart, Preference structures I: distances between transitive preference relations, Journal of Mathematical Sociology 3 (1973) 49–67.

[4] K. Bogart, Preference structures II: distances between asymmetric relations, SIAM Journal of Applied Mathematics 29 (2) (1975) 254–265.

[5] Y.L. Chen, L.C. Cheng, Mining maximum consensus sequences from group ranking data, European Journal of Operational Research 198 (1) (2009) 241–251.

[6] Y.L. Chen, L.C. Cheng, An approach to group ranking decisions in a dynamic environment, Decision Support Systems 48 (4) (2010) 622–634.

[7] W. Cohen, Learning to order things, Journal of Arti<sup>fi</sup>cial Intelligence Research 10 (1999) 243.

[8] W.D. Cook, M. Kress, L. Seiford, An axiomatic approach to distance on partial orders, Revue Automatique, Informatique et Recherche Operationnelle 20 (2) (1986) 115–122.

[9] W.D. Cook, M. Kress, L. Seiford, Information and preference in partial orders: a bimatrix representation, Psychometrika 51 (2) (1986) 197–207.

[10] W.D. Cook, M. Kress, L. Seiford, A general framework for distance-based consensus in ordinal ranking models, European Journal of Operational Research 96 (1996) 392–397.

[11] W.D. Cook, B. Golany, M. Kress, M. Penn, T. Raviv, Optimal allocation of proposals to reviewers to facilitate effective ranking, Management Science 51 (4) (2005) 655–661

[12] W.D. Cook, B. Golany, M. Kress, M. Penn, T. Raviv, Creating a consensus ranking of proposals from reviewer's partial ordinal rankings, Computers & Operations Research 34 (4) (2007) 954–965.

[13] S. Damart, L.C. Dias, V. Mousseau, Supporting groups in sorting decisions: methodology and use of a multi-criteria aggregation/disaggregation DSS, Decision Support Systems 43 (4) (2007) 1464–1475.

[14] R. Fagin, R. Kumar, D. Sivakumar, Ef<sup>fi</sup>cient similarity search and classi<sup>fi</sup>cation via rank aggregation, in: Proceedings of the ACM SIGMOD International Conference on Management of Data, ACM, San Diego, California, 2003, pp. 301–312.

[15] E. Fernandez, R. Olemdo, An agent model based on ideas of concordance and discordance for group ranking problems, Decision Support Systems 39 (3) (2005) 429.

[16] D.E. Goldberg, Genetic Algorithms in Search: Optimization and Machine Learning Addison Wesley, Boston, 1998.

[17] B. Golden, The Analytic Hierarchy Process: Applications and Studies, Springer, New York, NY, 1989.

[18] S. Greco, V. Mousseau, R. Slowinski, Ordinal regression revisited: multiple criteria ranking using a set of additive value functions, European Journal of Operational Research 191 (2) (2008) 416–436.

[19] D.S. Hochbaum, A. Levin, Methodologies and algorithms for group-rankings decision, Management Science 52 (9) (2006) 1394–1408.

[20] J.G. Kemeny, L.J. Snell, Preference ranking: an axiomatic approach, in: Proceeding of Mathematical Models in the Social Science, 1962, pp. 9–23.

[21] M. Kendall, Rank Correlation Methods, Third ed. Hafner, New York, 1955

[22] F.D. Robert, H.F. Ernest, Group decision support with the analytic hierarchy process Decision Support Systems 8 (2) (1992) 99–124.

[23] T.L. Saaty, Rank generation, preservation, and reversal in the analytic hierarchy decision process, Decision Sciences 18 (2) (1987) 157.

![](/api/attachments/5H4GUQNJ/fulltext/images/e93d0baef268e914cbfc80501ab1246aea632fdde1e0b535271f4bdb820b3f26.jpg)

Yen-Liang Chen is Professor of Information Management at National Central University of Taiwan. He received his Ph.D. degree in computer science from National Tsing Hua University, Hsinchu, Taiwan. His current research interests include data mining, social network analysis, and decision making models. He has published papers in Decision Support Systems, IEEE Transactions on Software Engineering, IEEE Transactions on Knowledge and Data Engineering, IEEE Transactions on SMC, Information & Management, Information Processing & Management, Journal of American Society of Information Science and Technology, Information Systems, Operations Research, Naval Research Logistics, Transportation Research — part B, European Journal of Operational Research, and many others. He is the former editor-in-chief of Journal of Information Management and that of Journal of e-Business.

![](/api/attachments/5H4GUQNJ/fulltext/images/39f1e22ecf0a16924e1c70054c9b2c9891cc5989822f284ae845084955961405.jpg)

Li-Chen Cheng is an Associate Professor of Department of Computer Science and Information Management, Soochow University, Taipei, Taiwan. She received her Ph.D. degree in information management from National Central University, Chung-Li, Taiwan. Her current research interests include data mining, information retrieval and EC technologies. She has published papers in Decision Support Systems, Electronic Commerce Research and Applications, European Journal of Operational Research, and many others.

![](/api/attachments/5H4GUQNJ/fulltext/images/64867b8371e05760e5dcdaca6299b0cce577790b67f8465d61dce1ba36052721.jpg)

Po-Hsiang Huang received the M.S. degree in Information Management from National Central University Chung-Li Taiwan. His research interests include data mining, information systems and EC technologies.
