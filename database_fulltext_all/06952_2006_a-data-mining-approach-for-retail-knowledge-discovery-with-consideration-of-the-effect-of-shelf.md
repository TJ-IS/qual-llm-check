---
otero_id: 6952
otero_key: "NZJAFRB6"
title: "A data mining approach for retail knowledge discovery with consideration of the effect of shelf-space adjacency on sales"
authors: "Yen-Liang Chen; Jen-Ming Chen; Ching-Wen Tung"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2005.12.004"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dss

# A data mining approach for retail knowledge discovery with consideration of the effect of shelf-space adjacency on sales

Yen-Liang Chen <sup>a,⁎</sup>, Jen-Ming Chen <sup>b,1</sup>, Ching-Wen Tung

<sup>a</sup> Department of Information Management, National Central University, 300 Jhongda Road, Jhongli City, Taiwan 32001, Republic of China <sup>b</sup> Institute of Industrial Management, National Central University, 300 Jhongda Road, Jhongli City, Taiwan 32001, Republic of China

Received 3 December 2003; received in revised form 3 December 2005; accepted 28 December 2005 Available online 21 February 2006

## Abstract

Recent marketing research has suggested that in-store environmental stimuli, such as shelf-space allocation and product display, has a great influence upon consumer buying behavior and may induce substantial demand. Prior work in this area, however, has not considered the effect of spatial relationships, such as the shelf-space adjacencies of distinct items, on unit sales. This paper, motivated in great part by the prominent beer and diapers example, uses data mining techniques to discover the implicit, yet meaningful, relationship between the relative spatial distance of displayed products and the items' unit sales in a retailer's store. The purpose of the developed mining scheme is to identify and classify the effects of such relationships. The managerial implications of the discovered knowledge are crucial to the retailer's strategic formation in merchandising goods. This paper proposes a novel representation scheme and develops a robust algorithm based on association analysis. To show its efficiency and effectiveness, an intensive experimental study using self-defined simulation data was conducted. The authors believe that this is the first academically researched attempt at exploring this emerging area of the merchandising problem using data mining.

© 2006 Elsevier B.V. All rights reserved.

Keywords: Data mining; Association rules; Shelf-space management; Retailing management; Merchandising

## 1. Introduction

Over the past three decades, merchandisers have relied heavily on marketing stimuli to increase their sales volume. Marketing research has suggested that the in-store stimuli (such as display, layout, atmosphere, and shelf-space arrangement) has a great influence on consumer buying behavior and may encourage sales by maximizing impulse buying and cross-selling. For example, a factorial experiment revealed that an in-store display of an item creates excitement and increases the average amount purchased [13]. A case study showed that effective store layout could stimulate demand to the point of doubling the sales rate by making it easier to find items and creating a positive image or feeling [43]. Psychological experiments show that elements of a store's atmosphere, like lighting, color, music, and aisle width, may have a greater influence on shopping behavior than characteristics of the product itself [19,27]. The positive curvilinear relationship between an item's shelf-space and its sales has been verified empirically for a wide variety of consumer goods [16,24].

Prior studies on in-store environmental stimuli, or merchandising techniques, have not considered the effect of spatial relationships, such as the shelf-space adjacencies of distinct items, on unit sales. As the famous beer and diapers example reveals [4], not considering the effects of side-by-side displays of items commonly purchased together may cause a retailer to miss out on tremendous revenue potential. The visual effect of adjacency can stimulate impulse purchases that account for 70% of buying decisions in a supermarket [5]. In light of this potential, this paper attempts to discover the implicit, yet meaningful, relationship between the relative spatial “distance” of displayed products and the items' unit sales in a retail store using data mining techniques. Special focus is placed on building a novel representation scheme for the historical transaction data and on developing an efficient and robust algorithm for knowledge mining. The proposed approaches measure and classify the effects of spatial adjacency of distinct items on increased sales.

Our data mining approach differs from the wellknown market basket analysis in several aspects. Our approach takes the product-to-shelf assignment information into account and incorporates the transaction time into the data stream dynamically. In contrast, the market basket analysis mainly determines what products customers purchase together in a static fashion, disregarding the product-to-shelf information. Therefore, our approach requires a differently formatted datawarehouse that must have spatial and temporal contents, and demands a more sophisticated algorithm for mining the dynamic transaction data effectively and efficiently. For the purposes of this study, we have assumed that all the required historical data is readily available and has been stored in the data-warehouse. To manage sales, a retail company must continue storing information in its databases on when the items are on the shelf and where they are placed. By properly pre-processing and integrating this data using the standard ETL tools provided by data warehouse software, one can obtain all this information in the format specified in this paper. Based on the simplified scenario, the problem is defined, the representation scheme is proposed, and the mining algorithm is developed using the association rules.

The more sophisticated mining techniques, like the one discussed in this paper, are superior to traditional approaches in retail knowledge discovery, such as the market basket analysis or frequent-buyer program [7]. In some cases, the fact that items sell well together is obvious, such as laundry detergent and fabric softener [34], greeting cards and seasonal candy, or coffee and coffee makers. Occasionally, however, the fact that certain items would sell well together is far from obvious, such as in the case of diapers and beer [4] or bottled juice and cold remedies [7]. The true reason behind such purchase patterns remain unclear; it may be due to their close proximity in shelf location or other consumer behavior we have yet to discover. In this regard, the market basket analysis or frequent-buyer program is unable to provide satisfactory results. The proposed scheme attempts to dig for obscure clues by introducing the spatial relationship and transaction time information into the mining techniques.

These approaches are separated not only by function and required data content but also by their managerial implications. The frequent-buyer program focuses on a consumer-level analysis to investigate individual purchase habits, such as a customer's affinity analysis. The market basket analysis, on the other hand, is mainly devoted to a market-level analysis. Due to the crossover of consumer traffic among stores, market-level analysis classifies the demand relationships across product categories into complement, independent, or substitute within the consumer choice process [39]. In contrast, our mining scheme is a store-level merchandise technique that identifies the effects of shelf-space proximity on unit sales over a finite time horizon and classifies the patterns as positive, independent, or negative. A positive pattern refers to a positive effect of shelf arrangement of distinct products on sales, meaning that placing specific product assortments sideby-side or in close proximity will trigger supplemental sales due to factors such as increased impulse purchasing and cross-selling. The negative pattern refers to a negative effect of such a spatial relationship.

The discovered relationship between shelf patterns and unit sales is crucial for effective decision-making and strategic planning in merchandising goods. For example, retailers can rearrange their shelf-space to increase impulse buying, and the store manager can measure the effect on revenue. The beer and diapers example has suggested the potential of utilizing spatial relationships [4]. In another related example [30], Seven-Eleven Japan has a policy of adjusting its store layout and product placement multiple times every day to reflect the changing purchase patterns at different hours of the day, so that customers can easily find their favorite items. In this regard, this paper is very likely the first academic research that explores this emerging, high-potential area.

The remainder of this paper is organized as follows. The related literature is reviewed in Section 2. Section 3 defines the problem context and proposes a representation scheme, and algorithmic development based on that scheme is detailed in Section 4. Using self-defined simulation data, an intensive experimental study was carried out and the results are discussed in Section 5. Special emphasis is placed on a comparative study between the proposed scheme and the traditional scheme, the Apriori algorithm, in terms of efficiency and effectiveness. The final section is devoted to recapping the research contributions and potential applications, discussing the limitations of the research, and offering directions for future research.

## 2. Literature review

Since our inter-disciplinary research embraces instore merchandising techniques and data mining techniques, we review both branches of research, beginning with the current literature dealing with instore merchandising, especially the highly related area of shelf-space allocation.

There is substantial literature on issues involving shelf-space allocation, or more specifically, product-toshelf allocation, which can be broadly classified into three categories: commercial, experimental, and optimization models. The commercial model focuses on practical aspects, or operational simplicity. It allocates shelf-space to a specific product based on simple heuristics or rules-of-thumb, such as proportion to revenue or gross profit [18,46]. One of its drawbacks is over-emphasis on the aspects of cost and static marginal return, with no consideration of the demand effects.

Most of the experimental studies have involved investigation of shelf-space elasticity of demand, which is defined as the ratio of relative change in unit sales to relative change in shelf-space. Comprehensive reviews of this literature are given in Curhan [16,17]. Previous experiments indicate that there is a small, positive relationship between shelf-space and unit sales [17], but large differences exist among product categories in the increased sales of the displayed products [13,16].

One of the earliest optimization models developed by Hansen and Heinsbroek [23] considers nonlinear demand and individual space-elasticity. Corstjens and Doyle [15] broadened the model to consider both spaceand cross-elasticity. Based on the Corstjens–Doyne model, Bultez and Naert [11] took into account the interdependencies within product groups and across groups, and Borin et al. [8] further extended the model by allowing simultaneous decisions on assortment selection and shelf-space allocation. Some recent work focuses in great part on algorithmic development, such as the heuristic procedure [45,44], the simulated annealing [8], and the meta-heuristic embracing Tabu search and squeaky-wheel optimization [31].

Unfortunately, most related work dealing with shelfspace issues does not focus on the spatial proximity effect on sales. In addition, our research interest is in knowledge discovery, not in empirical validation or optimization. Therefore, using data mining is a technically feasible and operationally sound approach.

Data mining is a process of nontrivial extraction of implicit, previously unknown, and potentially useful information from databases [12]. The discovered knowledge has been used in a wide array of applications such as market analysis, fraud detection, customer relationship management, and other business decisionmaking processes. The mining techniques can be roughly classified into five categories [40]: dependency analysis, class identification, concept description, deviation detection, and data visualization. Dependency analysis is further divided into two subcategories: association analysis and sequential pattern analysis. The latent knowledge from databases can be exposed by using one of the mining schemes, the selection of which depends on the types of databases being mined as well as the specific knowledge being uncovered. The mining scheme proposed in this paper falls into the subcategory of association rules, which was initially introduced in Agrawal et al. [1,2].

Since association rules are useful and easy to understand, they have been successfully applied in a variety of industries such as finance, telecommunications, marketing, retail, and on-line commerce [9]. It has also attracted increasing academic research interest in recent years and, as a consequence, many extensions have been proposed, including algorithmic improvements [10,22,32], fuzzy rules [25,28], multi-level and generalized rules [14,20], quantitative rules [36,41,42], spatial rules [14,26], inter-transactional rules [33], interesting rules [6], temporal association rules [3,29], and hybrid optimization modeling [35]. Comprehensive reviews of this field of research are given in Chen et al. [12] and Han and Kamber [21].

The aforementioned work, however, does not incorporate the product-to-shelf assignment information into the association rules. Traditional association rules, like the market basket analysis, can only discover associations between distinct product categories being purchased in a household's shopping trip, such as purchasing combinations. The results generated by such rules may be misleading due to inadequate data in analyzing the inherently dynamic and diverse retailing environment. This is because the product-to-shelf assignment may not only change over time in a designated store, but will also vary greatly from one store to another. From a market-level or industry-level viewpoint, the discovered associations are distorted to a certain degree because they exclude such unforeseen experimental factors. The proposed mining scheme intends to rectify this inherent shortcoming of the currently widely used association rules by taking spatial relationship into account and emphasizing, on a store level, analysis in a dynamic fashion for merchandising applications.

![](/api/attachments/NZJAFRB6/fulltext/images/9c3df7982d25d2dfd0940d47a4413f075be9038d0785f7d4ecbe9de4f1c77e00.jpg)  
Fig. 1. An illustrative transaction database.

## 3. The problem and definitions

We study the scenario of a single store, the shelf layout of which is represented by a multi-level tree. The tree corresponds to the space in a certain granularity, such as a floor, section, aisle, shelf, or package. An upper level corresponds to a coarser granularity, while a lower level corresponds to a finer granularity. Based on this representation, we can have a unique assignment between a specific shelf location and a product, allowing us to define the shelf pattern for each product being displayed in the store.

Let $I { = \{ i _ { 1 } , i _ { 2 } , \ldots , i _ { n } \} }$ denote the set of items that are displayed in a store. We consider a transaction database

$D = \{ s _ { 1 } , \ s _ { 2 } , \ \dots \ , \ s _ { m } \}$ , where $s _ { i } \subseteq I$ represents the i-th transaction. Each transaction $s _ { i }$ is associated with a transaction identity denoted by $T I D _ { i }$ and a time epoch $t _ { i } .$ Without loss of generality, we assume $T I D _ { i } { < } T I D _ { j }$ for $t _ { i } \leq t _ { j } .$ . Fig. 1 illustrates a transaction database containing 5 items $I { = } \{ \mathrm { A } $ , B, C, D, E} and three transactions generated at time epochs 1, 5, and 12, respectively.

The shelf-space in a store is represented by a space tree with ht levels. Let $P = \{ p _ { 1 } , p _ { 2 } , \dots , p _ { q } \}$ denote the set of shelf locations, where $p _ { i } { = } ( l _ { 1 } , l _ { 2 } , \ldots , l _ { h t } )$ is a leaf node in the space tree representing a specific shelf location. We can reach location $p _ { i }$ if we go down from the root to the leaf node by traversing the $l _ { j } { \mathrm { - t h } }$ branch in level $j - 1$ for j = 2 to ht. Fig. 2 is an example where the highest level corresponds to store, and then going from top to bottom are floor, section, shelf, and package. The location of item A in the space tree is 11111, meaning the item is being displayed in store 1, floor 1, Section 1, shelf 1, and package 1. Likewise, the code for item B is 11221, representing store 1, floor 1, Section 2, shelf 2, and package 1. This representation scheme is unique and easy to implement.

The historical list of the products' locations in the display shelf are stored in table $H { = } \left\{ h _ { 1 } , h _ { 2 } , \ldots , h _ { r } \right\}$ 9 where $h _ { i } { = \{ i _ { i } , ~ p _ { i } , ~ T _ { i } \} }$ , meaning that item $i _ { i }$ has been placed in the shelf location $p _ { i }$ over time period $T _ { i \cdot }$ An example in Fig. 3 shows that the locations of items A and C have been changed in time epochs 11 and 16, respectively, but items B, D, and E remain unchanged throughout time period [0,20].

![](/api/attachments/NZJAFRB6/fulltext/images/fa2dcda026eec4ca43d1fbefb5b7632146e3d3f1ea808aa6b3a8efe6a58d5e24.jpg)  
Fig. 2. The space tree

<table><tr><td>Item</td><td>location</td><td>T</td></tr><tr><td>A</td><td>11111</td><td>[0, 10]</td></tr><tr><td>A</td><td>12353</td><td>[11,20]</td></tr><tr><td>B</td><td>11122</td><td>[0, 20]</td></tr><tr><td>C</td><td>12235</td><td>[0, 15]</td></tr><tr><td>C</td><td>11223</td><td>[16, 20]</td></tr><tr><td>D</td><td>12145</td><td>[0, 20]</td></tr><tr><td>E</td><td>11334</td><td>[0, 20]</td></tr></table>

Fig. 3. The historical list H of products' locations.

Definition 1. Let $p _ { i } \mathrm { = } ( l _ { 1 } , ~ l _ { 2 } , ~ \ldots ~ , ~ l _ { z - 1 } , ~ l _ { z } , ~ \ldots ~ , ~ l _ { h t } )$ and $p _ { j } { = } ( l ^ { \prime } _ { 1 } , ~ l ^ { \prime } _ { 2 } , ~ . . . ~ , ~ l ^ { \prime } _ { z - 1 } , ~ l ^ { \prime } _ { z } , ~ . . . ~ , ~ l ^ { \prime } _ { h t } )$ . Then the spatial relationship between locations $p _ { i }$ and $p _ { j } ,$ denoted $r _ { i , j } =$ $p _ { i } \Delta p _ { j } ,$ , can be defined as: $r _ { i , j } { = } z - 1$ if $l _ { w } = l _ { \ w } ^ { \prime }$ for $1 \leq w \leq z - 1$ but $l _ { z } \neq l _ { z } ^ { \prime }$

Based on the definition above, a spatial relationship between two items will be in the set $\{ 1 , 2 , . . . , h t \}$ , and we use $( a , b , r e )$ to represent that the spatial relationship between items $a$ and b is $r e .$ . The example in Fig. 4 shows that the spatial relationship between items $\mathrm { A } =$ (1,1,1,1,1) and $\mathbf { B } { = } ( 1 , 1 , 1 , 2 , 2 )$ is 3. It is worth noting that a smaller value of re implies a larger distance between display locations, and a larger value of re implies a smaller distance.

Definition 2. Let X denote a set of items, or itemset, where $X \subseteq I .$ In database $D ,$ the set of transactions containing X can be represented as ${ \cal W } ( X , D ) =$ $\{ s | s \in D \land X \subseteq s \}$ . If X contains k items, we label it as k-itemset.

Definition 3. Let $S D { = } \{ s p _ { 1 } , s p _ { 2 } , \ldots , s p _ { m } \}$ denote the transaction database incorporated with the shelf location information; that is, SD is a combination of the original database D and the historical list H of positions. Stated specifically, $s p _ { i } , i \in [ l . . . m ]$ consists of the i-th transaction $s _ { i }$ in $D ,$ and the spatial relationships between each pair of items in $s _ { i }$ at time $t _ { i } ,$ where $t _ { i }$ is the time epoch of transaction $s _ { i } .$ Thus, each transaction $s p$ in $S D$ can be represented as $s p = \{ s p . \alpha , ~ s p . \beta \}$ , which satisfies the following conditions:

$$
\begin{array}{l} s p. \alpha \subseteq I, \text { and } \\ s p. \beta = \{(a, b, r e) | a,   b \in s p. \alpha , \quad a \neq b, \quad r e \in \{1, 2, \ldots , h t \} \}. \end{array}
$$

For example, assume that the locations of A, B, $\mathrm { C } ,$ and D are (1,1,1,1,1), (1,1,1,2,2), (1,1,1,1,3), and (1,2,2,2,3), respectively. Fig. 5 shows an extended transaction in the database, where sp.α = {A, B, C, D} and $s p . \beta = \{ ( \mathrm { A } , \mathrm { B } , 3 ) , ( \mathrm { A } , \mathrm { C } , 4 ) , ( \mathrm { A } , \mathrm { D } , 1 ) , ( \mathrm { B } , \mathrm { C } , 3 ) , ( \mathrm { B } , 1 ) , ( \mathrm { B } , 1 ) , ( \mathrm { B } , 1 ) , ( \mathrm { B } , 1 ) , ( \mathrm { B } , 1 ) , ( \mathrm { B } , 1 ) , ( \mathrm { C } , 1 ) \}$ $\mathrm { D } , 1 ) , ( \mathrm { C } , \mathrm { D } , 1 ) \}$

Definition 4. An s-itemset is denoted by $x p { = } \{ x p . \alpha ,$ $x p . \beta \}$ , where xp $. \alpha \subseteq I$ and $x p . \beta { = } \left\{ \left( a , b , r e \right) \vert a , b { \in } x p . \alpha , \right.$ $a \neq b , r e \in \{ 1 , 2 , \ldots , h t \} $ . If xp.α contains l items, we call it l − s-itemset.

For example, the extended transaction in Fig. 5 contains the following 3 − s-itemsets: $x p . \alpha = \{ \mathrm { A } , \mathrm { B } , \mathrm { C } \}$ and $x p . \beta = \{ ( \mathrm { A } , \mathrm { B } , 3 ) , ( \mathrm { A } , \mathrm { C } , 4 ) , ( \mathrm { B } , \mathrm { C } , 3 ) \}$ . The set of transactions in SD containing s-itemset xp can be represented as ${ \cal W } ( x p , S D ) { = } \{ s p | s p \in S D \land x p . \alpha \subseteq s p . \alpha \land$ $x p . \beta \subseteq s p . \beta \}$

For the sake of brevity, we can represent $x p . \beta$ as a sequence of values ordered first by row and then by column. That is, we can write $x p . \beta$ as $r e _ { 1 , 2 } , r e _ { 1 , 3 } , \ldots , r e _ { 1 }$ $\phantom { + } _ { k } , r e _ { 2 , 3 } , r e _ { 2 , 4 } , \ldots , r e _ { 2 , k } , r e _ { 3 , 3 } , \ldots , r e _ { k - 1 , k } ,$ where $r e _ { i , j }$ is the value of the spatial relationship of the i-th item and the jth item in xp.α. For example, $x p . \beta$ in Fig. 5 can be represented as 3, 4, 1, 3, 1, 1.

<table><tr><td></td><td>level</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td rowspan="2">A</td><td rowspan="2">SITE</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>II</td><td>II</td><td>II</td><td>#</td><td></td></tr><tr><td>B</td><td>SITE</td><td>1</td><td>1</td><td>1</td><td>2</td><td>2</td></tr></table>

Fig. 4. The spatial relationship between items A and B.

![](/api/attachments/NZJAFRB6/fulltext/images/5e0810519fedd1ad839f99545a3acedb94b35294313bd02b5d0932c73e246e1a.jpg)  
Fig. 5. An example of an extended transaction.

Definition 5. Let t(a, b, re) denote the set of time epochs at which the spatial relationship between items a and b is re. Accordingly, we define $S D ( a , \ b , \ r e ) =$ $\{ s p | s p \in S D \land$ the attached time of sp is in $t ( a , b , r e ) \}$ Note that a 2 − s-itemset $( a , b , r e )$ , if it occurs, can only occur in time epochs $t ( a , b , r e )$ and in transactions SD $( a , b , r e )$ . Similarly, for an s-itemset xp, we can define $T _ { x p } = \{ \cap t ( a , b , r e )$ for all $( a , b , r e ) \in x p . \beta \}$ as the times when xp could possibly occur. We use $S D _ { x p } = \{ s p | s p \in$ SD ∧ the time of sp is in $T _ { x p } \}$ to denote the set of extended transactions in SD where xp could possibly occur.

Fig. 6 shows that if we consider (A, C, 1), then we have SD(A, C, 1)={T1, T2, T3, T4, T5, T9, T10}, because during the times of these transactions, the spatial relationship of item A and item C is 1. Similarly, for an s-itemset xp, such as $x p . { \alpha } = \{ \mathrm { A }$ , B, C} and xp.β= 3, 1, 1, we have $S D _ { x p } { = } \{ \mathrm { T } 1$ , T2, T3, T4, T5}.

Definition 6. Let x denote an itemset. The global support of x, denoted by gs(x, D), is the percentage of transactions in D that contain x. It can be computed by | $W ( x , \ D ) | / | D |$ . Given a global minimum support threshold $\sigma _ { g } \in [ 0 , 1 ] , \mathrm { i f } \ g s ( x , D ) \geq \sigma _ { g } ,$ , we refer to x as a global frequent itemset.

Definition 7. Let xp denote an s-itemset. The p\_global support of s-itemset xp, denoted as p\_gs(xp, SD), is the percentage of extended transactions in SD that contain xp. It can be computed as $\vert W ( x p , \ S D ) \vert / \vert S D \vert$ . Given a p\_global minimum support threshold $\sigma _ { p - g } \in [ 0 , 1 ]$ , if $p _ { - } g s ( x p , \ S D ) { \geq } \sigma _ { p - g } ,$ we refer to xp as a p\_global frequent s-itemset. When xp is a p\_global frequent s-itemset, we call it a shelf pattern.

Definition 8. The actual support of s-itemset xp, denoted as as(xp, SD), is the percentage of extended transactions in $S D _ { x p }$ that contain xp. It can be computed as $| W ( x p , S D _ { x p } ) | / | \dot { S } D _ { x p } |$

For illustrative purposes, assume that we have |D| = $| S D | = 1 0 0 , x = \{ \mathrm { A , B , C } \} , x p . \alpha = \{ \mathrm { A , B , C } \} , x p . \beta = 3 , 2 , 2 ,$ xp′.α = {A, B, C}, xp′.β = 3, 1, 2; further, $| W ( x , D ) | = 3 0 .$ |W(xp, SD)| = 15, and |W(xp′, SD)| = 15. Based on the scenario above, the global support of itemset x is 30%, the p\_global support of xp is 15%, and the p\_global support of xp′ is 15%. If we make additional assumptions that $| S D _ { x p } | = 1 5$ and $| S D _ { x p ^ { \prime } } | = 6 0$ , the actual support of xp is $1 5 / 1 5 = 1 0 \%$ , since it occurs 15 times out of 15 possible chances. Likewise, the actual support of $x p ^ { \prime }$ is 15/60 = 25%, since it occurs 15 times out of 60 possible chances. Since the global support of x, which does not include any shelf information, is 30%, we find that the shelf arrangement of xp greatly increases sales. In contrast, the shelf arrangement of xp′ is not conducive to increasing sales. Therefore, xp is a good, or positive, shelf pattern and $x p ^ { \prime }$ is a bad, or negative, shelf pattern.

![](/api/attachments/NZJAFRB6/fulltext/images/1bd9a7138c8d584db1a1b7bc995fc91bb64575c3575e07228f366be2581abc28.jpg)  
Fig. 6. The shelf relations.

Definition 9. The strength of a shelf pattern xp is defined as: streng $t h { = } a s ( x p , S D ) / g s ( x p . \alpha , D )$

We are interested in discovering the following useful patterns:

1. Positive patterns: if the strength of shelf pattern xp is larger than the positive threshold ps, we say that this pattern is a positive pattern. Higher strength implies increasing sales.

2. Negative patterns: if the strength of shelf pattern xp is smaller than ns, we say that this pattern is a negative pattern. Lower strength implies decreasing sales.

## 4. The algorithm

In order to understand how shelf location will influence sales and associations of the purchased products, an algorithm is developed to identify the shelf patterns, with special emphasis on classifying the patterns into positive or negative. Based on the classifications, a retailer can merchandise goods effectively, such as displaying items in closer proximity for positive patterns, and as far apart as possible for the negative.

To this end, a novel algorithm, the AprioriLJ algorithm, is proposed, based on the traditional Apriori algorithm [2]. Let $L _ { k }$ denote the set of frequent $k -$ itemsets or k − s-itemsets, and $C _ { k + I }$ the set of candidate (k + 1)-itemsets or (k + 1) − s-itemsets. As in the traditional Apriori algorithm, we repeatedly execute the cycle, consisting of three major steps: find the set $L _ { k } ,$ form the candidate set $C _ { k + l } ,$ and finally scan the database to remove infrequent patterns. The proposed AprioriLJ algorithm, however, differs from the traditional Apriori algorithm in three aspects:

(1) More input data is required for the proposed algorithm. The additional input data includes the space tree (shown in Fig. 2), the historical list of products' locations (as shown in Fig. 3), and the thresholds $\sigma _ { p - g } , p s$ and ns.

(2) The output patterns are different. The patterns found by the Apriori algorithm can only explain which items are frequently bought together, while our patterns indicate the spatial relationships between items and therefore can explain how such relationships influence sales.

(3) Although our algorithm adopts the Apriori algorithm framework, we have to substantially modify each step of the process to deal with spatial relationships. For example, the Apriori algorithm uses a simple joining of $L _ { k }$ with $L _ { k }$ to produce $C _ { k + 1 }$ , while we use a new spatial joining method to produce $C _ { k + 1 }$ from $L _ { k } , L _ { k }$ , and $L _ { 2 }$ .

The AprioriLJ algorithm is graphically detailed in Fig. 7. The input includes the transaction database, the historical list of the products' positions on the shelf, the space tree, and various thresholds. First, we scan the database once in line 1, allowing us to compute the number of occurrences of each item and find the set of frequent items, labeled $L _ { 1 } .$ . After the scan, we can construct a balanced tree for each item that stores the TIDs of all transactions containing that particular item, keeping them in the main memory during the execution period of the algorithm. Later, the balanced trees will be employed to find the supports of itemsets.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Input: Transaction database D, the space tree
The historical list of the products' positions on shelf (H)
Various thresholds, such as  $\sigma_{g}$ ,  $\sigma_{p-g}$ , ps and ns

Output: shelf patterns, positive patterns, and negative patterns

Method:
1)  $L_{1}=Find\_frequent\_l\_items(D)$  and construct a balanced tree for each item in  $L_{1}$ ;
2)  $C_{2}=Relation(L_{1})$ ;
3)  $L_{2}=Find\_frequent\_k\_s\_items(C_{2})$ ;
4) For ( $k=3; L_{k-1} \neq \emptyset; k++$ ) {
5)  $C_{k}=AprioriLJ\_gen(L_{k-1}, L_{2})$ ;
6)  $L_{k}=Find\_frequent\_k\_s\_items(C_{k});\quad\}$ 
7) return  $\cup_{k}L_{k}$ ;
</div>

Fig. 7. The AprioriLJ algorithm.

In line 2, we use the procedure $R e l a t i o n ( L _ { 1 } )$ to produce $C _ { 2 } ,$ which is the candidate set of 2− s-itemset. Note that a 2− s-itemset may occur in several time periods. Therefore, for each 2− s-itemset, we need to record its supports for all the time segments, and then add up all the values. After obtaining the supports of all 2 − s-itemsets in $C _ { 2 } ,$ line 3 deletes the patterns whose frequencies do not satisfy the minimum p\_global support, and then determines the positive and negative patterns.

The loop from line 4 to line 7 produces the candidate sets and finds the frequent sets of s-itemsets after $C _ { 3 }$ Unlike the traditional Apriori algorithm, the proposed algorithm produces the candidate set $C _ { k }$ from $L _ { k - 1 } *$ $L _ { k - 1 } * L _ { 2 }$ , which will be further discussed in Section 4.4. Then we delete the patterns that do not satisfy the minimum p\_global support to find the frequent shelf patterns. Additionally, we calculate the strengths of the patterns to determine whether they are positive or negative.

## 4.1. Find L1 and build balanced trees

In line 1, we need to scan the database in order to determine which items are in the database and how frequently they occur. If the support of an item exceeds the minimal global support threshold, it is 1-itemset, that is, 1 − s-itemset. In addition, we build a balanced tree for each item, like an AVL tree, to store the TIDs of all transactions containing the item. The construction procedure of AVL trees is omitted, since it is available in all data structure textbooks. Fig. 8 shows an example of constructing AVL trees for each item in the database.

Because each node in an AVL tree is used to store a TID containing the item, the total size of the AVL trees for all items in $L _ { 1 }$ is no more than the total number of occurrences of items in the database. This implies that the memory space needed for the computation must be restricted to an acceptable size. Assume that the average number of items in each transaction is 10, and recording one TID requires 4 bytes. If we have ten million records, the memory space needed by all trees is no more than $4 * 1 0 * 1 0 , 0 0 0 , 0 0 0$ bytes, or 400 megabytes. Currently, the memory of a personal computer is generally at least several gigabytes. Thus, the memory space is sufficient for the AVL trees of all the items, making the approach practical for real world implementation.

![](/api/attachments/NZJAFRB6/fulltext/images/ef871e263f5839b5b9eda4a4a9ab3beb3c40d2192a6b907e88dbaac8a2e4bf7c.jpg)  
Fig. 8. The constructed AVL trees.

## 4.2. Produce $C _ { 2 }$

By definition, $C _ { 2 }$ must contain all spatial relationships between all pairs of items in $L _ { 1 } \ ( \mathrm { F i g . } \ 9 )$ . Because two items may have the same spatial relations in different time segments, each 2 − s-itemset needs to record the supports in all of these time segments. Therefore, to compute the support of a 2 − s-itemset in $C _ { 2 } ,$ we first compute its count in each separate time segment where this pattern could possibly occur, and then add up these values. As a result, in $C _ { 2 } ,$ we not only record which $2 - s -$ itemsets are included, but we also record the count of each 2 − s-itemset in each possible period, such as the count of items $l _ { 1 }$ and $l _ { 2 }$ with relation re in period T.

In line 4, we determine the intersections of time intervals of $l _ { 1 }$ and $l _ { 2 } .$ . Given the intervals of $l _ { 1 }$ and $l _ { 2 } ,$ , we can determine all of the intersected intervals by linearly scanning and merging the intervals of $l _ { 1 }$ and $l _ { 2 } .$ Interested readers should refer to textbooks for data structure or algorithms [37].

In line 5, the spatial relation between items $l _ { 1 }$ and $l _ { 2 }$ in period $T$ is determined. Let $p _ { 1 }$ and $p _ { 2 }$ be the shelf locations of $l _ { 1 }$ and $l _ { 2 }$ in period T, respectively. Their spatial relation can then be easily determined in the manner shown in Definition 1.

Line 6 is a complicated step in which we need to determine the number of transactions containing $l _ { 1 }$ and $l _ { 2 }$ with spatial relationship re in period T. To do this, we need a map table to record the range of TIDs occurring at time $t _ { i } .$ The table can be constructed by scanning the database in line 1 of the AprioriLJ algorithm. Using this table, if we are given a period $T ,$ we can determine the range of TIDs occurring in this period. Let $t s$ be the smallest TID and te be the largest TID. Then we traverse the AVL trees for items $l _ { 1 }$ and $l _ { 2 } ,$ and output all the common TIDs in both trees that are between ts and te. The number of these common TIDs is the count of $\mathbf { \dot { \rho } } l _ { 1 }$ and $l _ { 2 }$ with relation re in period T.

## 4.3. Produce $L _ { k }$

This section introduces the function used in lines 3 and 6 of the AprioriLJ algorithm: Find\_frequent\_k\_s\_items (C ) (Fig. 10). Since a k-itemset may generate many copies of k −s-itemset by having different shelf relations, line 2 is used to compute the global support of itemset xp.α. Based on the p\_global support of s-itemset $x p ,$ we can determine if xp is in $L _ { k } .$ Note that when we insert an xp into $L _ { k } ,$ we not only insert the pattern xp and its support into $L _ { k }$ but we also insert into $L _ { k }$ the counts of xp in different time periods. Furthermore, based on the global support of xp.α and the actual support of $x p ,$ we can compute the strength of xp as well as decide if xp is positive or negative.

<table><tr><td colspan="2">Function Relation $(L_1)$ </td></tr><tr><td>1)</td><td>For each item  $l_1 \in L_1$ </td></tr><tr><td>2)</td><td>For each item  $l_2 \in L_1$ </td></tr><tr><td>3)</td><td>For every pair of time intervals of  $l_1$  and  $l_2$  {</td></tr><tr><td>4)</td><td>Let T be the intersection of the two intervals;</td></tr><tr><td>5)</td><td>Determine the relation re between  $l_1$  and  $l_2$  in period T;</td></tr><tr><td>6)</td><td>Compute the number of transactions in period T containing  $l_1$  and  $l_2$ ;</td></tr><tr><td>7)</td><td>Insert the pattern  $(l_1, l_2, re, T)$  and its count into  $C_2$ ; }</td></tr></table>

Fig. 9. The generation of $C _ { 2 }$ by function Relation $( L _ { 1 } )$

## 4.4. Produce the candidate set of s-itemset

This section explains the details of the generation of the candidate set $C _ { k } ,$ line 5 in the AprioriLJ algorithm (Fig. 11). Unlike traditional methods that generate $C _ { k }$ by joining $L _ { k - 1 }$ with itself, we generate $C _ { k }$ by joining $L _ { k - 1 }$ with $L _ { k - 1 }$ and then with $L _ { 2 }$

In lines 1 and 2, we extract the two patterns $l _ { 1 }$ and $l _ { 2 }$ from $L _ { k - 1 } ,$ , where $l _ { 1 }$ is composed of $i _ { 1 } , \ldots \ldots , i _ { k - 2 } , i _ { k - 1 } ;$ and $l _ { 2 }$ of $i _ { 1 } , \ldots , i _ { k - 2 } , i _ { k }$ . The two patterns must have the same (k − 2) − s-itemset, including items $i _ { 1 } ,$ , … $i _ { k - 2 , }$ as well as the same spatial relationship between them. We then extract from $L _ { 2 }$ the pattern $l _ { 3 } ,$ composed of $i _ { k - 1 }$ and $i _ { k }$ .

In line 4 and line $5 ,$ we need to determine the intersections of the time intervals of $l _ { 1 } , l _ { 2 }$ and $l _ { 3 } .$ . Given the intervals of $l _ { 1 } , l _ { 2 } ,$ , and $l _ { 3 } ,$ , we can determine all of the intersected intervals by sequentially scanning and merging the intervals of $l _ { 1 } , \ l _ { 2 } ,$ and $l _ { 3 }$ . For a given interval T, line 6 determines the spatial relationships between all pairs of items in the pattern generated by the joining of $l _ { 1 } , l _ { 2 }$ and $l _ { 3 } ,$ called $l p$ for short. Following that, line 7 determines the number of transactions containing $l p$ in period T, where the items in $l p$ have relation re in period T. To accomplish this, we can use the mapping table defined in Section 4.2 to determine the range of TIDs that occur in period T. Let ts be the smallest TID and te be the largest TID. We then traverse the AVL trees for all the items in $l p ,$ and output all the common TIDs that are between ts and te. The number of these common TIDs is the count of pattern $l p$ in period T. Finally, we insert the count of lp in period T into $C _ { k } .$

![](/api/attachments/NZJAFRB6/fulltext/images/44ea7fb20a943b2ae26364dbeb5598e84fcc6ea78863d2db61f1745b9e5d7863.jpg)  
Fig. 10. Function Find\_frequent\_k\_s\_items(C ).

<table><tr><td>1)</td><td>For each  $l_{1} \in L_{k-1}$  /  $l_{1}$  has items  $i_{1}, \ldots, i_{k-2}, i_{k-1}$ </td></tr><tr><td>2)</td><td>For each  $l_{2} \in L_{k-1}$  /  $l_{2}$  has items  $i_{1}, \ldots, i_{k-2}, i_{k}$ </td></tr><tr><td>3)</td><td>For each  $l_{3} \in L_{2}$  /  $l_{3}$  has items  $i_{k-1}, i_{k}$ </td></tr><tr><td>4)</td><td>For all time intervals of  $l_{1}$  and  $l_{2}$  and  $l_{3}$  {</td></tr><tr><td>5)</td><td>Let  $T$  be the intersection of the three intervals;</td></tr><tr><td>6)</td><td>Compute the relation  $re$  between  $l_{1}, l_{2}$  and  $l_{3}$  in period  $T$ ;</td></tr><tr><td>7)</td><td>Compute the number of transactions in period  $T$  containing the pattern coming from the join of  $l_{1}, l_{2}$  and  $l_{3}$ ;</td></tr><tr><td>8)</td><td>Insert this pattern into  $C_{k}$ ; }</td></tr></table>

Fig. 11. Function AprioriLJ\_gen $( L _ { k - 1 } , L _ { 2 } )$

Before further detailing how to generate $C _ { k }$ by joining $L _ { k - 1 }$ with $L _ { k - 1 }$ and then with $L _ { 2 } ,$ we must define the following terms:

subpat(X, u, v): Suppose that the shelf pattern X is composed of items $i _ { I } , ~ i _ { 2 } , \ldots , ~ i _ { k }$ and their spatial relationships. Then subpat(X, u, v) represents the sub-pattern of X containing items $i _ { u } , i _ { u + 1 } , \ldots , i _ { \nu }$ and the spatial relationships between these items. An illustrative example in Fig. 5 shows a shelf pattern containing items {A, B, C, D} and the relationships 3, 4, 1, 3, 1, 1. Then subpat(X, 1, 3) indicates the sub-pattern containing items {A, B, C} and the relationships 3, 4, 3.

re(X, u, v): The spatial relationship between items $i _ { u }$ and $i _ { \nu }$ in pattern X. As shown in Fig. 5, we have re(X, 2, 3) = 3 and re(X, 1, 4) =1.

Suppose xp and yp are two shelf patterns in $L _ { k - 1 }$ , and zp is a shelf pattern in $L _ { 2 } .$ . If subpat(xp, 1, k − 2) = subpat (yp, 1, k − 2) and subpat(xp, k − 1, k − 1) ≠ subpat(yp, k − 1, k − 1), then we generate wp in $C _ { k } ,$ which is defined as follows:

□ subpat(wp, 1, k −1)=subpat(xp, 1, k−1)

□ subpat(wp, k, k) = subpat(yp, k − 1, k − 1)

□ re(wp, j, k) = re(yp, j, k − 1) for j = 1 to k − 2

□ re(wp, k − 1, k) = re(zp, 1, 2).

Fig. 12 shows that the relation of ABCDE in S is 1,2,3,2,3,5,4,2,5,1, and the relation of ABCDF in pattern T is 1,2,3,3,3,5,1,2,4,2. Suppose we have another pattern of items E and F with relation 3. Combining the three patterns generates a new candidate pattern, shown on the right in Fig. 12.

## 4.5. An example

In this section, an example is presented to illustrate a step-by-step procedure of the proposed algorithm based on the transaction database in Fig. 1 and the historical list of items' shelf positions in Fig. 3. In addition, we set the following parameters: $\sigma _ { g } = 2 / 3 , \sigma _ { p - g } = 1 / 3 , p s = 1 . 2$ and ns=0.8.

After executing line 1 of the algorithm, we find $L _ { 1 }$ from $C _ { 1 } .$ . We also construct an AVL tree for each item in $L _ { 1 } .$ . For simplicity, we only show the result of $L _ { 1 }$ in Fig. 13.

In the next step, we generate $C _ { 2 }$ from $L _ { 1 }$ . As mentioned above, when we generate $C _ { 2 } .$ , we not only need to record what 2 − s-itemsets are included but we must also record the count of each 2 − s-itemset in its distinct time period. Let us take a closer look at the pattern containing item A and item C. For these, we must first use the time period of A and the time period of C, as shown in Fig. 3, to find the intersected intervals. The result includes three intervals [0, 10], [11, 15], and [16, 20]. For each interval, we find the number of transactions containing both items A and C by traversing the AVL trees of item A and item C. We show the result in Fig. 14.

![](/api/attachments/NZJAFRB6/fulltext/images/85ea633a0ef61ccfce733be6e5ec138b1de76914999376bfc01955e853863247.jpg)  
Fig. 12. Generate the candidate pattern.

![](/api/attachments/NZJAFRB6/fulltext/images/b61002aa55e6247e9395f034b6b1daa51f5f30a284cf3ad08369514efd6da43c.jpg)  
Fig. 13. Generate $L _ { 1 } .$

From $C _ { 2 } .$ , we delete the infrequent 2 − s-itemsets, i.e., the items whose p\_global supports are less than $\sigma _ { p - g } = 1 /$ 3. Then, for each 2 − s-itemset in $L _ { 2 } ,$ , we find its actual support. In addition, we compute the global supports of those 2-itemsets in $L _ { 2 }$ . Based on this data, we can determine which patterns are positive and which are negative. After executing Find\_frequent\_k\_s\_items $( C _ { 2 } )$ , the result is shown in Fig. 15, where the pattern of A and C with relation 2 is a positive pattern, while that of A and C with relation 1 is a negative pattern.

With $L _ { 2 } ,$ we can generate $C _ { 3 }$ by using the principles stated in Section 4.4. For example, by combing the pattern with items {A, B}, the pattern with {A, C}, and the pattern with {B, C}, we can generate candidate patterns with items {A, B, C}. Since the first has periods [0, 10] and [11, 20], the second has [0, 10] and [11, 15], and the third has [0, 15], the intersections of these intervals result in two intervals, [0, 10] and [11, 15]. This is why, in $C _ { 3 } ,$ , we generate the pattern of {A, B, C} in these two periods. The final result of $C _ { 3 }$ is shown in

<table><tr><td colspan="4"> $C_2$ </td></tr><tr><td>Item</td><td>RE</td><td>T</td><td>count</td></tr><tr><td>AB</td><td>3</td><td>[0, 10]</td><td>2</td></tr><tr><td>AB</td><td>1</td><td>[11, 20]</td><td>1</td></tr><tr><td>AC</td><td>1</td><td>[0, 10]</td><td>1</td></tr><tr><td>AC</td><td>2</td><td>[11, 15]</td><td>1</td></tr><tr><td>AC</td><td>1</td><td>[16, 20]</td><td>0</td></tr><tr><td>AD</td><td>1</td><td>[0, 10]</td><td>2</td></tr><tr><td>AD</td><td>2</td><td>[11, 20]</td><td>1</td></tr><tr><td>BC</td><td>1</td><td>[0, 15]</td><td>2</td></tr><tr><td>BC</td><td>2</td><td>[16, 20]</td><td>0</td></tr><tr><td>BD</td><td>1</td><td>[0, 20]</td><td>3</td></tr><tr><td>CD</td><td>2</td><td>[0, 15]</td><td>2</td></tr><tr><td>CD</td><td>1</td><td>[0, 20]</td><td>0</td></tr></table>

Fig. 14. Generate $C _ { 2 } .$

<table><tr><td colspan="7"> $L_2$ </td></tr><tr><td>Item</td><td>RE</td><td>T</td><td>AS</td><td>P_GS</td><td>GS</td><td>Strength</td></tr><tr><td>AB</td><td>3</td><td>[0, 10]</td><td>2/2</td><td>2/3</td><td rowspan="2">3/3</td><td>1</td></tr><tr><td>AB</td><td>1</td><td>[11, 20]</td><td>1/1</td><td>1/3</td><td>1</td></tr><tr><td>AC</td><td>1</td><td>[0, 10]</td><td>1/2</td><td>1/3</td><td rowspan="2">2/3</td><td>0.75</td></tr><tr><td>AC</td><td>2</td><td>[11, 15]</td><td>1/1</td><td>1/3</td><td>1.5</td></tr><tr><td>AD</td><td>1</td><td>[0, 10]</td><td>2/2</td><td>2/3</td><td rowspan="2">3/3</td><td>1</td></tr><tr><td>AD</td><td>2</td><td>[11, 20]</td><td>1/1</td><td>1/3</td><td>1</td></tr><tr><td>BC</td><td>1</td><td>[0, 15]</td><td>2/3</td><td>2/3</td><td>2/3</td><td>1</td></tr><tr><td>BD</td><td>1</td><td>[0, 20]</td><td>3/3</td><td>3/3</td><td>3/3</td><td>1</td></tr><tr><td>CD</td><td>2</td><td>[0, 15]</td><td>2/3</td><td>2/3</td><td>2/3</td><td>1</td></tr></table>

Fig. 15. Generate $L _ { 2 } .$

Fig. 16. Although the algorithm could be detailed further, we stop here for the sake of space.

## 5. The experiment

In the experiment, the Apriori and AprioriLJ algorithms were implemented in Borland C + Builder 6 and tested on a Pentium IV–2.0 GHz Windows 2000 system with 1024 megabytes of main memory. Since these two algorithms have different application scenarios, it may not make sense to compare them. For the sake of completeness, however, we still compare them whenever possible. Accordingly, Section 5.2.1 compares the two algorithms with regard to the run time and number of generated patterns. Afterward, in the experiments of Sections 5.2.2–5.2.6, we show only the results of the AprioriLJ algorithm, because the parameters studied are related to spatial proximity, which is not considered by the traditional Apriori algorithm.

## 5.1. Data generation

Generation of the synthetic data consists of three steps: generating the transaction database $D ,$ generating the space tree, and generating the historical list of items' positions $H .$ In the following sections, we provide detailed descriptions of each step.

<table><tr><td colspan="4"> $C_3$ </td></tr><tr><td>Item</td><td>RE</td><td>T</td><td>count</td></tr><tr><td>ABC</td><td>311</td><td>[0, 10]</td><td>1</td></tr><tr><td>ABC</td><td>121</td><td>[11, 15]</td><td>1</td></tr><tr><td>ABD</td><td>311</td><td>[0, 10]</td><td>2</td></tr><tr><td>ABD</td><td>121</td><td>[11, 20]</td><td>1</td></tr><tr><td>ACD</td><td>212</td><td>[0, 10]</td><td>1</td></tr><tr><td>ACD</td><td>122</td><td>[11, 15]</td><td>1</td></tr></table>

Fig. 16. The generation of $C _ { 3 } .$

We use the method given in Agrawal et al. [1,2] to generate the transaction data in $D ,$ since this method is widely used as a benchmark for generating transactions. Since time is an important factor in our problem, we have to associate these transactions with time stamps indicating the days these transactions took place. To this end, we assign all the transactions to $d$ different days that are normally distributed, where $d$ is a parameter representing the total number of days. Table 1 shows the parameters used for generating the transaction data.

In this paper, the shelf-space is represented by a space tree with five levels, where the nodes in the upper UL levels have five branches each and the nodes in the lower CL levels have ten branches. In this example, the upper UL levels mean unchangeable levels and the lower CL levels mean changeable levels. This restriction is for practical reasons; in reality, it is impossible to move a specific item to another floor. Usually a retailer can only change an item's display location to a distinct aisle, shelf, or shelf level, all of which are within the same section.

In addition to the restriction discussed above, a retail store also needs to consider the frequency of an item's change in shelf location. For example, the location of large electronic equipment, such as a refrigerator or television set, would rarely change, but the location of seasonal products may change frequently during transitions from season to season. Therefore, we categorize the frequency of the changes of an item's location into three classes: high H, middle $M ,$ and low L. Furthermore, the percentage of items belonging to these three classes is denoted by parameters PH, PM, and $P L ,$ respectively.

The parameters needed in generating the historical list H of items' locations are listed in Table 2. First, we randomly assign each item to the location of a leaf node in the space tree. Then, based on parameters PH, PM, and $P L ,$ all the items are categorized into one of three classes: class $ { { } ^ { 6 } \mathrm { { R } ^ { , 5 } } }$ , class $\mathbf { \ddot { \tau } } ^ { \mathrm { 4 6 } } \mathbf { M } ^ { \mathrm { 7 } } ;$ , and class $^ { 6 6 } \mathrm { L } ^ { 5 5 } .$ . We use Poisson processes with means $H , M ,$ and L to generate the numbers of location changes in the store. Let npc denote the number of location changes for a certain item. We then randomly chose npc time points from the selling time period, from 1 to d. For each time point, we randomly chose another position to move the item to, but kept the upper level unchanged. Based on the data generation procedure, we can determine how an item changes its location over time.

Table 1  
The parameters used in generating the transaction data

<table><tr><td>|D|</td><td>The number of transactions in the database</td></tr><tr><td>N</td><td>The number of items in the database</td></tr><tr><td>T</td><td>The average length of each transaction</td></tr><tr><td>I</td><td>The average length of the potential frequent itemset</td></tr><tr><td>d</td><td>The number of days</td></tr></table>

Table 2  
The parameters used in generating H

<table><tr><td>UL</td><td>The number of unchangeable levels</td></tr><tr><td>CL</td><td>The number of changeable levels</td></tr><tr><td>H</td><td>The average number of changes for class “H”</td></tr><tr><td>M</td><td>The average number of changes for class “M”</td></tr><tr><td>L</td><td>The average number of changes for class “L”</td></tr><tr><td>PH</td><td>The percentage of items in class “H”</td></tr><tr><td>PM</td><td>The percentage of items in class “M”</td></tr><tr><td>PL</td><td>The percentage of items in class “L”</td></tr></table>

In the simulation, different data sets will be used. For ease of comprehension, the parameters associated with a data set are represented in a unified manner. The number after each parameter is the value of this parameter. For example, D200K means the total number of transactions is 200× 1000; UL2 means the number of unchangeable levels is 2; H5 means the average number of position changes for class $ { { } ^ { 6 } \mathrm { H } ^ { 5 } }$ is 5; PH0.2 means the percentage of items in class $ { { } ^ { 6 } \mathrm { H } ^ { 5 } }$ is 0.2. Unless stated otherwise, the default parameter values set in the experiments are D200K, N2500, T10, I5, d300, UL2, CL3, H5, M3, L1, PH0.2, PM0.6, and PL0.2. In the experiments, we vary the value of each parameter to see how it affects the performance and patterns generated. Due to space limitations, however, not all of these experiments are included in this paper.

The minimum global support and the minimum p\_global support are set the same. To study the performance from different perspectives, various simulations are run by adjusting the parameters accordingly, but each run of the simulation only changes one parameter at a time. In each simulation, we compare two performance measures: (1) run time and (2) the number of frequent patterns.

## 5.2. The results of the experiments

## 5.2.1. DB scale up

In this experiment, we fix the other parameters but leave D as a variant in order to compare the run times of the two methods for different numbers of records. Table 3(a) shows the ratios of the run time of the AprioriLJ algorithm to that of the Apriori algorithm for different minimum supports. We first discuss the results when the minimum support is greater than

(a)

Table 3  
The relative performance of the two algorithms (a, b)

<table><tr><td rowspan="2">MSup</td><td colspan="3">100 K</td><td colspan="3">200 K</td><td colspan="3">300 K</td></tr><tr><td>Apriori</td><td>AprioriLJ</td><td>Ratio</td><td>Apriori</td><td>AprioriLJ</td><td>Ratio</td><td>Apriori</td><td>AprioriLJ</td><td>Ratio</td></tr><tr><td>0.50%</td><td>84.235</td><td>118.781</td><td>1.410115</td><td>121.871</td><td>196.423</td><td>1.611729</td><td>276.891</td><td>483.235</td><td>1.745217</td></tr><tr><td>0.75%</td><td>19.381</td><td>38.625</td><td>1.992931</td><td>32.548</td><td>71.365</td><td>2.192608</td><td>73.953</td><td>162.753</td><td>2.200763</td></tr><tr><td>1%</td><td>12.424</td><td>15.349</td><td>1.235431</td><td>18.493</td><td>26.763</td><td>1.447196</td><td>45.812</td><td>53.234</td><td>1.16201</td></tr><tr><td>1.25%</td><td>10.245</td><td>7.458</td><td>0.727965</td><td>16.329</td><td>11.426</td><td>0.699737</td><td>37.519</td><td>24.312</td><td>0.647992</td></tr><tr><td>1.50%</td><td>9.823</td><td>5.692</td><td>0.579456</td><td>15.143</td><td>7.854</td><td>0.518655</td><td>30.451</td><td>17.981</td><td>0.59049</td></tr><tr><td colspan="10">(b)</td></tr><tr><td>Sec</td><td>Apriori</td><td>AprioriLJ</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>100 K</td><td>12.424</td><td>15.349</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>200 K</td><td>18.493</td><td>26.763</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>300 K</td><td>45.812</td><td>53.234</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>500 K</td><td>64</td><td>1219</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>700 K</td><td>86</td><td>2541</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>1000 K</td><td>119</td><td>4863</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

0.75% and then discuss the results when it is smaller than 0.75%.

In the first case, the results in Table 3 indicate that as we increase the minimum support further and further, the ratio decreases continuously. This phenomenon may be because the AprioriLJ algorithm tends to produce more candidate patterns, but these patterns have smaller supports than those of the Apriori algorithm. When the minimum support increases, most candidate patterns in the AprioriLJ algorithm become infrequent, because their supports are smaller. This reduction in the number of frequent patterns generated allows the AprioriLJ to have a lower processing time.

Next, we consider when the minimum support ranges from 0.75% to 0.5%. From Table 3(a), we observe that the run time of the Apriori algorithm increases dramatically as we decrease the minimum support from 0.75% to 0.5%, compared with the changes in other minimum support intervals higher than 0.75%. For the AprioriLJ algorithm, however, we note that the change in run time in interval [0.5%, 0.75%] is not significantly different from those in other minimum support intervals higher than 0.75%. A possible explanation for this result is that, in many experiments involving association patterns, a frequent phenomenon is that when the minimum support is lower than a certain threshold, the number of patterns and the run time increase dramatically or exponentially [1,2,10,22]. Since the two algorithms are also used to find association patterns, they should follow the same behavior. Between these two, the threshold for the AprioriLJ algorithm would be lower than that of the

AprioriLJ algorithm, because the supports of candidate patterns generated in the AprioriLJ algorithm are usually smaller than those generated in the Apriori algorithm. From Table 3(a), we observe that the threshold for the Apriori algorithm may occur in interval [0.5%, 0.75%], but the threshold for the AprioriLJ algorithm may not yet have come. This is why the relative performance between AprioriLJ and Apriori decreases as we decrease the minimum support from 0.75% to 0.5%.

By setting the minimum support as 1%, Table 3(b) shows the run times for different data sizes, from 100 K to 1000 K. It is interesting to note that when the data size is no more than 300 K, the two algorithms have similar performances, but when the data size gets larger than this threshold, the AprioriLJ algorithm performs much worse than the Apriori algorithm. The possible reason may be that the AprioriLJ algorithm needs to use more memory space for storing the AVL trees, so when the data size is beyond the manageable limit, the operating system must swap the trees between disk space and main memory, slowing down the system.

Fig. 17 shows the numbers of frequent patterns in different phases when the minimum support is 1%. In $L _ { 1 } ,$ , since the definitions of frequent patterns in both algorithms coincide, the numbers of frequent patterns are the same. From the second phase on, because the shelf patterns need to satisfy both time and position, the suitable patterns generated by the AprioriLJ will not be as numerous as those in the Apriori algorithm. As a result, the number of frequent patterns found by the AprioriLJ algorithm would be lower than that found by the Apriori algorithm. In the figure, we also notice that the numbers of patterns in $L _ { 3 } , L _ { 4 } , . . . , L _ { 7 }$ are similar, but there is a large spike in $L _ { 2 } .$ . This is because the supports of most patterns in $L _ { 2 }$ produced by the Apriori algorithm are only slightly larger than the minimum support. When the spatial information is added, a pattern which was originally frequent becomes several infrequent shelf patterns. This results in a much smaller number of shelf patterns in $L _ { 2 }$

![](/api/attachments/NZJAFRB6/fulltext/images/d4c459303ba4741695ee1944bb8b8fb701b00ad9b586b5f32853d29e9bb189b3.jpg)  
Fig. 17. The number of frequent patterns.

## 5.2.2. p\_global support

According to the definitions given in Section 3, $\sigma _ { g }$ is the threshold for frequent itemsets, which did not consider the shelf-space information; $\sigma _ { p - g }$ is the threshold for frequent s-itemsets, which takes shelfspace information into consideration. In the preceding section, we assumed that $\sigma _ { g }$ and $\sigma _ { p - g }$ were the same, but in this section we will focus on the effects of changing $\sigma _ { p - g } .$ . In Fig. 18, when we decrease $\sigma _ { p - g }$ while keeping $\sigma _ { g }$ fixed, the needed run time increases and the number of frequent patterns increases as well. On the other hand, as we decrease $\sigma _ { g }$ under the same $\sigma _ { p - g } ,$ both the needed time and the number of frequent patterns increase.

(a)

<table><tr><td> $\sigma_{p-g}$ </td><td>0.50%</td><td>0.75%</td><td>1.00%</td><td>1.25%</td><td>1.50%</td></tr><tr><td>0.50%</td><td>283.542</td><td></td><td></td><td></td><td></td></tr><tr><td>0.75%</td><td>195.183</td><td>93.465</td><td></td><td></td><td></td></tr><tr><td>1%</td><td>126.756</td><td>69.153</td><td>28.348</td><td></td><td></td></tr><tr><td>1.25%</td><td>81.798</td><td>48.547</td><td>23.534</td><td>16.423</td><td></td></tr><tr><td>1.50%</td><td>46.756</td><td>30.534</td><td>19.432</td><td>14.312</td><td>11.265</td></tr></table>

(b)

<table><tr><td> $\sigma_{p-g}$ </td><td>0.50%</td><td>0.75%</td><td>1.00%</td><td>1.25%</td><td>1.50%</td></tr><tr><td>0.50%</td><td>1487</td><td></td><td></td><td></td><td></td></tr><tr><td>0.75%</td><td>892</td><td>786</td><td></td><td></td><td></td></tr><tr><td>1%</td><td>421</td><td>364</td><td>316</td><td></td><td></td></tr><tr><td>1.25%</td><td>358</td><td>312</td><td>239</td><td>207</td><td></td></tr><tr><td>1.50%</td><td>296</td><td>247</td><td>194</td><td>165</td><td>131</td></tr></table>

Fig. 18. (a) The run times for different $\sigma _ { g }$ and $\sigma _ { p - g * }$ . (b) The number of patterns for different $\sigma _ { g }$ and $\sigma _ { p - g } .$

![](/api/attachments/NZJAFRB6/fulltext/images/a75265f55f6de8faf4e31d8b146d947bf28cd9a7deacc9291a47785cd0bb26f8.jpg)  
Fig. 19. Run times for PH/PM/PL combinations.

Based on the numerical results above, we conclude that when either $\sigma _ { g } \operatorname { o r } \sigma _ { p - g }$ decreases, the time becomes longer and the number of patterns increases. An explanation may be that because $\sigma _ { g }$ is the threshold to search for frequent itemsets, when $\sigma _ { g }$ increases, the itemsets that are removed increase and the potential sitemsets that will be considered in the following process decrease, which results in lower execution time. Similarly, since $\sigma _ { p - g }$ is the threshold to search for frequent s-itemsets, if it is lower, then more s-itemsets will be considered, thus increasing the run time.

## 5.2.3. The percentages of items in different classes

As mentioned in Section 5.1, the frequency of the changes of an item's location can be classified into classes H, M, and L. In this section, we will change the percentages of items in classes H, M, and L. In Fig. 19, we present five scenarios. In the first scenario, the ratios of high-frequency items, middle-frequency items, and low-frequency items to all items are 0.2, 0.6, and 0.2, respectively. In scenarios 2 through 5, they are set as 0.3/ 0.4/0.3, 0.1/0.8/0.1, 0.1/0.3/0.6, and 0.6/0.3/0.1, respectively. We will compare performance under these five settings.

![](/api/attachments/NZJAFRB6/fulltext/images/13fb8a746a143f70965e8c5d357c36f07cba8a0a2cc9a78abac60a6faac4c753.jpg)  
Fig. 20. Number of patterns for PH/PM/PL combinations.

![](/api/attachments/NZJAFRB6/fulltext/images/821ee4da0b3345c0ac1034471b583c98fcf4670554965ab41b5bdef54b4873af.jpg)  
Fig. 21. Run times for H,M,L combinations.

Figs. 19 and 20 reveal that the 0.1/0.3/0.6 combination requires the longest time and produces the most patterns, while the 0.6/0.3/0.1 combination requires the shortest time and produces the fewest patterns. This is probably because when more items change their positions, s-itemsets' supports become smaller and more potential s-itemsets will be removed during the process, resulting in less execution time as well as fewer patterns.

## 5.2.4. The average number of changes in classes H, M, and L

This section studies the effects of changing the parameters H, M, and $L ,$ which denote the average number of position changes in classes H, M, and L. Fig. 21 shows that when the values of H, M, and L increase, the run time shortens. Fig. 22 shows that when the values of H, M, and L decrease, the number of generated patterns increases. This is probably because the more often items change their locations, the less possible it will be that a candidate s-itemset becomes frequent. Thus, this results in not only a shorter run time, but also fewer patterns.

![](/api/attachments/NZJAFRB6/fulltext/images/e20d7597c32e6e8a4711a4301b27323db12b2eee4fdd92e660500d1d0aa93adc.jpg)  
Fig. 22. Number of patterns for H,M,L combinations.

![](/api/attachments/NZJAFRB6/fulltext/images/d51e886f87173ae8202592c1f62e1d8266c1f664b25c4ec0fe0d330db97987c9.jpg)  
Fig. 23. Run times for UL,CL combinations.

## 5.2.5. The number of changeable levels and unchangeable levels

This section studies the effects of changing the parameters UL and CL, which denote the numbers of unchangeable levels and changeable levels. In Fig. 23, there are four kinds of scenarios: the first has one unchangeable level with four changeable levels (1/4), the second has 2/3, the third has 3/2, and the fourth has 4/1. Figs. 23 and 24 show that when we have more changeable levels, less time is needed and fewer patterns are generated. This may be because the more frequently items change their locations, the less possible it is for a candidate s-itemset to be frequent, resulting in a shorter run time and fewer patterns.

![](/api/attachments/NZJAFRB6/fulltext/images/14983e10f906fd12e0f766448c7d5eff80646dbec9297d1e4ebc3d9c9ddd1ba3.jpg)  
Fig. 24. Number of patterns for UL,CL combinations.

![](/api/attachments/NZJAFRB6/fulltext/images/49335668560b6492a63d49f8bd00467b7de503a75b2277f699ebad7c7db4d86a.jpg)  
Fig. 25. Negative patterns.

## 5.2.6. Negative and positive thresholds

As defined in Section 3, ns is the threshold for selecting negative patterns and ps is the threshold for selecting positive patterns. According to their definitions, we may expect that when ns is smaller, there will be fewer negative patterns satisfying the threshold. Similarly, when ps is larger, there will be fewer positive patterns satisfying the threshold. The results of Figs. 25 and 26 match our expectations.

## 6. Discussion and conclusion

Traditional data-driven analysis techniques such as the frequent-buyer program or the market basket analysis can only provide a profile of customers purchasing affinities; they tell us what combinations are in their shopping carts, but cannot tell us why. The reason why some products are frequently bought together, like detergent and fabric softener, is apparent, while other combinations, like bottled juice and cold remedies or beer and diapers, are not so easily explained. This research seeks a possible answer to these questions by investigating spatial relationships between displayed products and their impact on sales that result from the visual effects of adjacency on impulse buying and cross-selling. In this regard, this paper opens a new research dimension by treating the spatial relationship as an important marketing tool in retailing and merchandising.

In addition, the proposed mining scheme focuses on a store-level analysis in a dynamic fashion, which remedies the inherent shortcoming of the existing association analysis in dealing with the diverse and changing retail store environment. Our extensive and well-designed experiment has shown promising results that are numerically sound and computationally efficient. As with most management science applications, however, the proposed scheme is purely theoretical. In our study, the retailer's transaction data was assumed to include spatial content, such as product-to-shelf assignments, in a dynamic fashion. Furthermore, the proposed scheme can only work well in a designated scenario, which requires changes of such assignments. These assumptions and restrictive conditions may limit its applicability, yet they do not decrease its merit. Our exploratory research has demonstrated the technical feasibility of the proposed scheme and may also be applicable in practice, provided that adequate data is available. Our paper may contribute to the areas of data mining and datawarehousing and may also help data-gathering content in databases. These areas are extremely valuable in decision-making and strategic formation in future merchandise planning.

The representation scheme and knowledge-mining algorithm proposed in this paper represent a positive initiative in the emerging area of data-driven marketing, or so-called database marketing [38]. Using the proposed scheme, the positive or negative adjacent relationships among distinct products can be discovered in the first stage of implementation. In the second stage, the manager can develop an effective merchandising strategy by using this information to rearrange shelf-space and product placement in the store. For example, a manager can place products in the same area that have positive adjacent effects, such as displaying beer just outside the diaper aisle, and can place products as far apart as possible if a negative effect between the items is found. Additionally, a catalog or on-line merchant could use the information to determine the display and layout of its catalog or onscreen design, and direct marketers could use the knowledge to determine which new products should be introduced and which items should be bundled together with frequently bought items and offer them to their prior customers.

![](/api/attachments/NZJAFRB6/fulltext/images/66c173f013485270779003a6cace5f2525ed4b9efb192f24c62fc6fe14cea9d0.jpg)  
Fig. 26. Positive patterns.

In relation to the proposed scheme, there are some critical managerial issues that should be further studied. First, the issue of how the obtained positive and negative shelf patterns can be optimally implemented into the existing layout in a store remains unclear. Second, if the total space is given when the shelf-space layout has not yet been determined, how can we determine the shelfspace layout and product placement simultaneously, so that some objective criteria, such as total revenue or profit margin, can be optimized? Third, if the total space can be expanded via capital investment, how can the space, shelf layout, and location assignment be optimally determined? These questions should be further investigated in future research.

An empirical study should be conducted to validate the effectiveness of any theoretical scheme. Since database reformatting and data-gathering procedures are time-consuming and costly, empirical research in this area is challenging and may be difficult to accomplish. We believe, however, that our research idea and proposed scheme is a first step towards a novel approach of embracing data mining techniques and merchandise planning.

## Acknowledgments

Y.-L. Chen was supported in part by the MOE Program for Promoting Academic Excellence of Universities under Grant No. 91-H-FA07-1-4 and National Science Foundation Grant No. 91-2416-H-008-003. The authors thank the three anonymous referees for their many helpful suggestions that have greatly improved this paper.

## References

[1] R. Agrawal, T. Imielinski, A. Swami, Mining association rules between sets of items in large databases, Proceedings of the ACM SIGMOD International Conference on Management of Data, 1993, pp. 207–216.

[2] R. Agrawal, R. Srikant, Fast algorithms for mining association rules, Proceedings of the 20th VLDB Conference, Santiago, Chile, 1994, pp. 478–499.

[3] J.M. Ale, G.H. Rossi, An approach to discovering temporal association rules, Proceedings of the 2000 ACM Symposium on Applied Computing 2000, vol. 1, 2000, pp. 294–300.

[4] Anonymous, Data mining is more than beer and diapers, Chain Store Age 74 (6) (June 1998).

[5] K. Armata, Signs that sell, Progressive Grocer 75 (10) (October 1996) 21.

[6] R.J. Bayardo Jr., R. Agrawal, Mining the most interesting rules, Proceedings of the 5th ACM SIGKDD International

Conference on Knowledge Discovery and Data Mining, August 1999, pp. 145–154.

[7] T.J. Blischok, Every transaction tells a story, Chain Store Age Executive with Shopping Center Age 71 (3) (March 1995) 50–56.

[8] N. Borin, P.W. Farris, J.R. Freeland, A model for determining retail product category assortment and shelf space allocation, Decision Sciences 25 (3) (1994) 359–384.

[9] I. Bose, R.K. Mahapatra, Business data mining – a machine learning perspective, Information and Management 39 (2001) 211–225.

[10] S. Brin, R. Motwani , J.D. Ullman, S. Tsur, Dynamic itemset counting and implication rules for market basket data, Proceedings of the 1997 ACM-SIGMOD Conference on Management of Data, May 1997, pp. 255–264.

[11] A. Bultez, P. Naert, SHARP: shelf allocation for retailers profit, Marketing Science 7 (3) (1988) 211–231.

[12] M.-S. Chen, J. Han, P.S. Yu, Data mining: an overview from a database perspective, IEEE Transactions on Knowledge and Data Engineering 8 (1996) 866–883.

[13] M. Chevalier, Increase in sales due to in-store display, Journal of Marketing Research 12 (4) (November 1975) 426–431.

[14] E. Clementini, P.D. Felice, K. Koperski, Mining multiple-level spatial association rules for objects with a broad boundary, Data and Knowledge Engineering 34 (3) (2000) 251–270.

[15] M. Corstjens, P. Doyle, A model for optimizing retail space allocations, Management Science 27 (7) (July 1981) 822–833.

[16] R.C. Curhan, The relationship between shelf space and unit sales in supermarkets, Journal of Marketing Research 9 (4) (November 1972) 406–412.

[17] R.C. Curhan, Shelf space allocation and profit maximization in mass retailing, Journal of Marketing 37 (3) (July 1973) 54–60.

[18] P. Desmet, V. Renaudin, Estimation of product category sales responsiveness to allocated shelf space, International Journal of Research in Marketing 15 (1998) 443–457.

[19] R.J. Donovan, J.R. Rossiter, Store atmosphere: an environmental psychology approach, Journal of Retailing 58 (Spring 1982) 34–57.

[20] J. Han, Y. Fu, Mining multiple-level association rules in large databases, IEEE Transactions on Knowledge and Data Engineering 11 (5) (1999) 798–805.

[21] J. Han, M. Kamber, Data Mining, Morgan Kaufmann, San Francisco, 2001.

[22] J. Han, J. Pei, Y. Yin, Mining frequent patterns without candidate generation, Proceedings of the 2000 ACM-SIGMOD Int. Conf. on Management of Data, Dallas, TX, May 2000.

[23] P. Hansen, H. Heinsbroek, Product selection and space allocation in supermarkets, European Journal of Operational Research 3 (6) (1979) 474–484.

[24] C.W. Hubbard, The “shelving” of increased sales, Journal of Retailing 45 (4) (Winter 1969–1970) 75–84.

[25] H. Ishibuchi, T. Nakashima, T. Yamamoto, Fuzzy association rules for handling continuous attributes, Proceedings of the IEEE International Symposium on Industrial Electronics, 2001, pp. 118–121.

[26] K. Koperski, J. Han, Discovery of spatial association rules in geographic information databases, Proceedings of the 4th International Symposium on Large Spatial Databases (SSD95), Maine, 1995, pp. 47–66.

[27] P. Kotler, Atmospherics as a marketing tool, Journal of Retailing 49 (Winter 1974) 40–64.

[28] C.M. Kuok, A.W. Fu, M.H. Wong, Mining fuzzy association rules in databases, SIGMOD Record 27 (1) (1998) 41–46.

[29] C.H. Lee, C.R. Lin , M.S. Chen, On mining general temporal association rules in a publication database, Proceedings of the 2001 IEEE International Conference on Data Mining, November 2001, pp. 337–344.

[30] H.L. Lee, S. Whang, Demand chain excellence, Supply Chain Management Review (March/April 2001) 40–46.

[31] A. Lim, B. Rodrigues, X. Zhang, Metaheuristics with local search techniques for retail shelf-space optimization, Management Science 50 (1) (January 2004) 117–131.

[32] J. Liu, Y. Pan, K. Wang, J. Han, Mining frequent item sets by opportunistic projection, Proceedings of the 2002 Int. Conf. on Knowledge Discovery in Databases, Edmonton, Canada, July 2002.

[33] H. Lu, L. Feng, J. Han, Beyond intra-transaction association analysis: mining multi-dimensional inter-transaction association rules, ACM Transactions on Information Systems 18 (4) (2000) 423–454.

[34] P. Manchanda, A. Ansari, S. Gupta, The ‘shopping basket:’ a model for multi-category purchase incidence decisions, Market ing Science 18 (2) (1999) 95–114.

[35] B. Padmanabhan, A. Tuzhilin, On the use of optimization for data mining: theoretical interactions and eCRM opportunities, Management Science 49 (10) (2003) 1327–1343.

[36] J.-S. Park, M.-S. Chen, P.S. Yu, Using a hash-based method with transaction trimming for mining association rules, IEEE Transactions on Knowledge and Data Engineering 9 (1997) 813–825.

[37] F.P. Preparata, M.I. Shamos, Computational Geometry: An Introduction, Springer-Verlag, New York, 1985.

[38] G. Robins, Database marketing, Store Magazine 76 (5) (May 1994) 32–33.

[39] G.J. Russell, A. Petersen, Analysis of cross category dependence in market basket selection, Journal of Retailing 76 (3) (2000) 367–392.

[40] M.J. Shaw, C. Subramaniam, G.W. Tan, M.E. Welge, Knowledge management and data mining for marketing, Decision Support Systems 31 (2001) 127–137.

[41] R. Srikant, R. Agrawal, Mining quantitative association rules in large relational tables, Proceedings of the ACM-SIGMOD 1996 Conference on Management of Data, Montreal, Canada, June 1996, pp. 1–12.

[42] J. Wijsen, R. Meersman, On the complexity of mining quantitative association rules, Data Mining and Knowledge Discovery 2 (1998) 263–281.

[43] J.L. Willen, Simply irresistible, Nation's Business 83 (1) (January 1995) 40.

[44] M.-H. Yang, An efficient algorithm to allocate shelf space, European Journal of Operational Research 131 (2001) 107–111.

[45] M.-H. Yang, W.-C. Chen, A study of shelf space allocation and management, International Journal of Production Economics 60–61 (1999) 309–317.

[46] F.S. Zufryden, A dynamic programming approach for product selection and supermarket shelf-space allocation, Journal of the Operational Research Society 37 (4) (1986) 413–422.

![](/api/attachments/NZJAFRB6/fulltext/images/cebc57fd16fb79d47697c40d95ed52b56e771d915520eb3c2588b779f7266bc1.jpg)

Yen-Liang Chen is Professor and Chairperson of Information Management at the National Central University of Taiwan. He received his Ph.D. degree in Computer Science from the National Tsing Hua University, Hsinchu, Taiwan. His current research interests include data modeling, data mining, data warehousing and operations research. He has published papers in Operations Research, Decision Support Systems, Information and Manage-

ment, IEEE Transactions on Knowledge and Data Engineering, IEEE Transactions on Software Engineering, IEEE Transactions on SMC, Information Systems, Information Sciences, Information Processing Letters, Expert Systems with Applications, Computers and OR, European Journal of Operational Research, Journal of Operational Research Society and Transportation Research.

![](/api/attachments/NZJAFRB6/fulltext/images/36a6b5d834e12aa7d1f166dc3a2170f7fc11e82e5ceeac19e6fcc1adcdab516c.jpg)

Jen-Ming Chen is a professor in the Institute of Industrial Management at the National Central University (Taiwan). He received a Ph.D. in Industrial Engineering from the Pennsylvania State University in 1992. His research interests include inventory and supply chain management, channel coordination, and pricing and yield management. He is an active member of several professional organizations, including Informs, DSI, and IIE. Dr. Chen is the recipient of the George B.

Dantzig Dissertation Award from the Informs and the recipient of the IIE Doctoral Dissertation Award, both in 1994.

![](/api/attachments/NZJAFRB6/fulltext/images/9f42ffe5eae66d7fb4667a21d229b61432b119e71fd4824c26cab9c91382f949.jpg)

Ching-Wen Tung received his MS degree in Information Management from the National Central University, Chung-Li, Taiwan. Currently, he is serving the army of Taiwan for a period of two years to fulfill his military obligation. His research interests include data mining, information systems and EC technologies.
