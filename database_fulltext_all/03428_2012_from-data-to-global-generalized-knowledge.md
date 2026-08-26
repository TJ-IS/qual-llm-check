---
otero_id: 3428
otero_key: "WP2XKEHW"
title: "From data to global generalized knowledge"
authors: "Yen-Liang Chen; Yu-Ying Wu; Ray-I Chang"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.08.005"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# From data to global generalized knowledge

Yen-Liang Chen <sup>a,</sup>⁎, Yu-Ying Wu <sup>b</sup>, Ray-I Chang <sup>c</sup>

<sup>a</sup> Department of Information Management, National Central University, Jhongli, Taiwan

<sup>b</sup> Department of Information Management, Nanya Institute of Technology, Jhongli, Taiwan

<sup>c</sup> Department of Engineering Science and Ocean Engineering, National Taiwan University, Taipei, Taiwan

## a r t i c l e i n f o

Article history: Received 17 September 2010 Received in revised form 11 July 2011 Accepted 21 August 2011 Available online 26 August 2011

Keywords: Attribute-oriented induction Data mining Multiple-level mining Generalized knowledge

## a b s t r a c t

The attribute-oriented induction (AOI) is a useful data mining method that extracts generalized knowledge from relational data and user's background knowledge. The method uses two thresholds, the relation threshold and attribute threshold, to guide the generalization process, and output generalized knowledge, a set of generalized tuples which describes the major characteristics of the target relation. Although AOI has been widely used in various applications, a potential weakness of this method is that it only provides a snapshot of the generalized knowledge, not a global picture. When thresholds are different, we would obtain different sets of generalized tuples, which also describe the major characteristics of the target relation. If a user wants to ascertain a global picture of induction, he or she must try different thresholds repeatedly. That is time-consuming and tedious. In this study, we propose a global AOI (GAOI) method, which employs the multiple-level mining technique with multiple minimum supports to generate all interesting generalized knowledge at one time. Experiment results on real-life dataset show that the proposed method is effective in <sup>fi</sup>nding globa generalized knowledge.

© 2011 Elsevier B.V. All rights reserved.

## 1. Introduction

Data mining has attracted a great deal of attention in the information industry and society in recent years due to its wide applicability in many areas such as fraud detection, <sup>fi</sup>nancial forecast, crime discovery and behavior identi<sup>fi</sup>cation [1,5,32]. Many data mining approaches designed to <sup>fi</sup>nd useful information and knowledge from huge amounts of data have already been proposed [12,18,23]. One of the most important approaches is the attribute-oriented induction (AOI) method which was <sup>fi</sup>rst introduced by Cai et al. in 1990 [6].

AOI is a data mining technique which is used to extract generalized knowledge from relational data and user's background knowledge. The essential background knowledge applied in AOI takes the form of a concept hierarchy which is associated with each attribute in the relational database [9]. Concept hierarchies often refer to domain knowledge and can be created by domain experts or knowledge engineers. The applications, such as customer relationship management [26], outpatient clinic [30], spatial data induction [24,31], which need induce useful generalized knowledge from data for further analysis, can apply the AOI method. As one example, the generalized knowledge about market phenomena can be generated from customer behavior data. Such knowledge can facilitate market orientation, decision making, and distinguish marketing. Medical abstraction knowledge is another example.

We can generate such knowledge from clinical database or individual patient cases. The knowledge can help us obtain the disease trend or make an expert consultant system.

In AOI method, the generalization process is performed by either attribute removal or concept hierarchy ascension, and controlled by two parameters: the attribute generalization threshold (Ta) and the generalized relation threshold (Tr) [18,19]. The attribute threshold speci<sup>fi</sup>es the maximum number of distinct values of any attribute that may exist after generalization, and the relation threshold gives an upper bound to the number of generalized tuples that remain after the generalization process [8]. Given the speci<sup>fi</sup>c thresholds, AOI can be applied to generate a set of generalized tuples to describe the target relation. The following example illustrates the use of the AOI method to produce two generalized relations with different thresholds.

Example 1. Let us consider a small relational table with 20 tuples and 4 attributes. Table 1 shows the synthetic car information data. To save space all concept hierarchies are shown only in Appendix A. Assume there are two sets of thresholds: (1) Ta=3, Tr=4; and (2) Ta=5, Tr=5. After applying the AOI method in the synthetic relation, we obtain two small sets of generalized tuples which display the general characteristics of the input relation, as shown in Tables 2 and 3.

There is no doubt that AOI is very useful for inducing the general characteristics of an input relation. However, the above example reveals a serious weakness in the AOI, that it only provides a snapshot of the generalized knowledge, not a global picture. If we set different thresholds, we will obtain different sets of generalized tuples that also describe the general characteristics of the input relation. If a user wants to ascertain a global picture of induction, he or she must try different thresholds repeatedly. That is time-consuming and tedious. It is therefore important to provide an ef<sup>fi</sup>cient algorithm capable of generating all interesting generalized tuples at one time.

Table 1  
Synthetic relation showing car information with 20 tuples and 4 attributes.

<table><tr><td>Rid</td><td>Manufacturer</td><td>Model</td><td>Engine</td><td>Price</td><td>Rid</td><td>Manufacturer</td><td>Model</td><td>Engine</td><td>Price</td></tr><tr><td>1</td><td>Kia</td><td>Compact car</td><td>1600</td><td>12,250</td><td>11</td><td>Ford</td><td>Compact van</td><td>2500</td><td>25,000</td></tr><tr><td>2</td><td>Chevrolet</td><td>Fullsize van</td><td>3500</td><td>26,900</td><td>12</td><td>Chevrolet</td><td>Compact van</td><td>2700</td><td>25,230</td></tr><tr><td>3</td><td>Toyota</td><td>Compact car</td><td>1600</td><td>14,950</td><td>13</td><td>Daewoo</td><td>Fullsize car</td><td>1600</td><td>23,980</td></tr><tr><td>4</td><td>Honda</td><td>Fullsize car</td><td>4000</td><td>24,950</td><td>14</td><td>Hyundai</td><td>Fullsize van</td><td>1600</td><td>20,343</td></tr><tr><td>5</td><td>Chrysler</td><td>Compact SUV</td><td>3200</td><td>28,635</td><td>15</td><td>Kia</td><td>Compact car</td><td>1600</td><td>12,250</td></tr><tr><td>6</td><td>Nissan</td><td>Fullsize car</td><td>3200</td><td>24,000</td><td>16</td><td>Mazda</td><td>Compact pick-up</td><td>3200</td><td>15,535</td></tr><tr><td>7</td><td>BMW</td><td>Sports car</td><td>4500</td><td>52,500</td><td>17</td><td>Chrysler</td><td>Compact SUV</td><td>3200</td><td>28,635</td></tr><tr><td>8</td><td>Chevrolet</td><td>Compact van</td><td>2700</td><td>25,230</td><td>18</td><td>Kia</td><td>Compact car</td><td>1300</td><td>9998</td></tr><tr><td>9</td><td>Porsche</td><td>Sports car</td><td>4000</td><td>59,100</td><td>19</td><td>Dodge</td><td>Compact SUV</td><td>4000</td><td>27,335</td></tr><tr><td>10</td><td>Ferrari</td><td>Sporty car</td><td>6000</td><td>186,925</td><td>20</td><td>Chevrolet</td><td>Fullsize SUV</td><td>4700</td><td>32,905</td></tr></table>

In this paper, we proposed a global AOI (GAOI) approach, which generates multiple-level and cross-level generalized knowledge at one time. The multiple-level mining approach [17] and multiple minimum supports concept [27] are adopted in this design. To explore multiplelevel generalized knowledge, one needs to provide concept hierarchies of attributes from speci<sup>fi</sup>c concepts to general concepts. Generally, a generalized knowledge at high levels of abstraction is more likely to have a large support. Hence, it is necessary to apply different minimum support thresholds at different levels of abstraction [17]. Furthermore, the mining results of GAOI method are cross-level generalized knowledge. Hence, a generalized tuple can contain values with different levels of abstraction, and the minimum support of a generalized tuple must be determined carefully. The generation algorithm proposed in this study, called FGV, extends the Apriori algorithm and employs the multiple minimum supports concept proposed by Liu et al. [27] to generate all interesting generalized tuples. In addition, an association measure is used to eliminate uninteresting tuples.

From the description above, it is obvious that not all generalized tuples are useful or interesting to the user. Hence, it is not appropriate to generate all generalized tuples without information reduction, because too much information may hinder users from applying the knowledge. Therefore, we must have some way to <sup>fi</sup>nd only those interesting generalized tuples. Accordingly, we use the following criteria to search for interesting generalized tuples:

1. Minimum support constraint: An interesting generalized tuple must satisfy the minimum support constraint. The rationale is that a generalized tuple must have a good representability. If a generalized tuple covers only a tiny fraction of data, we view it as noise rather than characteristic. Therefore, we ask that every generalized tuple must satisfy a minimum representability constraint.

2. Multiple level support constraint: Among all generalized tuples, some are generalized to higher levels, while others are generalized to lower levels. Those higher level generalized tuples are expected to have larger support while lower levels ones have smaller support. Therefore, we set a different minimum support threshold for each generalization level.

3. Strong association: Two values are said to have strong association if their probability of co-occurrence is signi<sup>fi</sup>cantly larger than the multiplication of their individual probabilities. Furthermore it is possible that although a generalized tuple has large support, the association among its constituent values may be weak. (Note that a higher level generalized tuple tends to have higher support.) To avoid this problem, the association of a generalized tuple is measured by the relative ratio of its actual support and its expected probability of occurrence. Thus, only those generalized tuples with strong associations are worth keeping.

The remainder of the paper is organized as follows. In Section 2 the AOI method and related work are reviewed. In Section 3, we de-<sup>fi</sup>ne the problem. In Section 4 the GAOI algorithm designed to generate all interesting generalized tuples from relational databases is developed. The results of our performance evaluation are given in Section 5. Finally, the conclusions are drawn in Section 6.

## 2. Related work

AOI is a set-oriented database mining method which generalizes the task-relevant subset of the data attribute by attribute [16]. The generation of each attribute is associated with a concept hierarchy. The concept hierarchy represents necessary background knowledge which controls the generalization processes. Different level concepts are often organized into a taxonomy of concepts. The concepts range from the single, most generalized root concept, to the most speci<sup>fi</sup>c concepts corresponding to the speci<sup>fi</sup>c values of attributes in the database [8,19].

The goal of AOI is to perform generalization based on the examination of the number of distinct values of each attribute in the relevant set of data. As mentioned in Section 1, there are two parameters controlling the generalization process. The attribute generalization threshold (Ta) speci<sup>fi</sup>es the maximum number of distinct values of an attribute. If the number of distinct values for an attribute is greater than the threshold for that attribute, further attribute removal or attribute generalization should be performed. Attribute generalization also known as concept hierarchy ascension is based on the following rule: If there exists a higher level concept in the concept tree for an attribute value of a tuple, the substitution of the value by its higher level concept generalizes the tuple [19].

After attribute removal or attribute generalization, the second parameter, the generalized relation threshold (Tr), is applied in the AOI algorithm to further aggregate the generalized relation. If the number of distinct tuples in the generalized relation is greater than the threshold, further aggregation should be performed. Aggregation is performed by merging identical, generalized tuples, and accumulating their respective counts [18].

Table 2  
Generalized tuples after the application of AOI with Ta=3, Tr=4.

<table><tr><td>Manufacturer</td><td>Model</td><td>Engine</td><td>Price</td><td>Vote</td></tr><tr><td>North America</td><td>Light truck</td><td>Any</td><td>High price</td><td>8</td></tr><tr><td>Asia</td><td>Car</td><td>Any</td><td>Low price</td><td>7</td></tr><tr><td>European</td><td>Car</td><td>High</td><td>High price</td><td>3</td></tr><tr><td>Asia</td><td>Light truck</td><td>Any</td><td>Low price</td><td>2</td></tr></table>

Table 3  
Generalized tuples after the application of AOI with Ta=5, Tr=5.

<table><tr><td>Manufacturer</td><td>Model</td><td>Engine</td><td>Price</td><td>Vote</td></tr><tr><td>Asia</td><td>General car</td><td>Any</td><td>Low price</td><td>7</td></tr><tr><td>North America</td><td>Light truck</td><td>High</td><td>Valued</td><td>5</td></tr><tr><td>European</td><td>Performance Car</td><td>High</td><td>Expensive</td><td>3</td></tr><tr><td>North America</td><td>Van</td><td>Middle</td><td>Valued</td><td>3</td></tr><tr><td>Asia</td><td>Light truck</td><td>Any</td><td>Economic</td><td>2</td></tr></table>

Obviously, these two thresholds are the critical factors of in<sup>fl</sup>uence on the generalization results. The attribute generalization threshold is especially important. If the attribute is generalized too high, it may lead to over-generalization, and the resulting tuples may not be very informative. On the other hand, if the attribute is not generalized to a suf-<sup>fi</sup>ciently high level, then under-generalization may result, in which case the inductions obtained may also not be informative. However, the control of how high an attribute should be generalized is typically quite subjective. It is very dif<sup>fi</sup>cult to attain a balance and set an appropriate threshold at one time. When the generalization is accomplished based on a certain attribute generalization threshold, the AOI algorithm provides only a snapshot of generalized knowledge for a given threshold, as shown in Tables 2 and 3. If users want to obtain a global picture of generalized tuples, they must try different thresholds repeatedly. This is a time-consuming and error-prone process.

There are several researches that enhanced or extended the AOI approach. Carter and Hamilton [7] proposed GDBR and FIGR, two enhancements of AOI. Basically, both algorithms control generalization levels by using attribute threshold. The GDBR is an on-line algorithm and requires only a small space, while the FIGR is incremental, allowing changes to the database without re-scan of the input relation. Cheung [10] proposed a rule-based conditional concept hierarchy, which extended the traditional approach to a conditional AOI, thereby allowing different tuples to be generalized through different paths depending on other attributes of the tuple. Hsu [21] extended the basic AOI algorithm to the generalization of major and numeric values. Hsu's algorithm generalizes the results by introducing an additional major value threshold through which major values are preserved and presented successfully. In addition, Hsu suggests an alternative algorithm for processing numeric attributes to avoid constructing a numeric concept hierarchy subjectively. Chen and Shen [8] proposed a dynamic programming algorithm to <sup>fi</sup>nd generalized knowledge from an ordered list of data. Their algorithm can generate K generalized tuples to describe the characteristics of different segments of data along the list.

Furthermore, since the AOI did not analyze data dependency relationships among attributes, Hu and Cercone [22] integrated machinelearning paradigm with rough set techniques to retain the set of relevant attributes and eliminate the set of unimportant ones to <sup>fi</sup>nd a minimal subset of interesting attributes for distinguishing different classes. Other researches concentrated on the management of uncertainty in relational databases [4] and the utilization of the fuzzy concept hierarchies [3,25,29]. A fuzzy hierarchy of concepts re<sup>fl</sup>ects the degree to which a concept belongs to its direct general level. More than one parent of a single concept is allowed during fuzzy induction. The AOI and its extended methods have also been used in many applications to induce the domain dependent generalized knowledge [14,24,26,30,31,33].

The survey above indicates that the speci<sup>fi</sup>c problems studied here have not been addressed in previous research. We take a fundamentally different approach from what has been discussed so far. The GAOI algorithm employs the multiple-level mining technique with multiple minimum supports to generate all frequent generalized knowledge at a time. Then, an association measure is used to <sup>fi</sup>lter out all weak association generalized knowledge.

The association measure used in the GAOI has the same purpose as the interestingness measure popularly used in data mining. Many measures have been suggested for ranking or pruning patterns according to their potential interest to the user [15,20]. Geng and Hamilton [15] made a comprehensive survey of interestingness measures and categorized the measures into four criteria: diversity, conciseness, peculiarity, and surprisingness. Concise measures are easily understood, and concise ones are usually more interesting than complex ones. Fabris and Freitas [13] de<sup>fi</sup>ned a concise measure I to re<sup>fl</sup>ect the degree of correlation (A, B) as follows:

$$
I (A, B) = | P (A, B) - P (A) P (B) |,
$$

where P(A, B) denotes the observed probability of attributes A and B. P (A) and P(B) denote the probability of attribute A and attribute B, respectively. In the GAOI algorithm, we use the variation of concise measure I to measure the degree of association.

## 3. Problem formulation

In this section, we de<sup>fi</sup>ne the problem of mining global generalized tuples from a relational database. Let $R { = } \{ a _ { 1 } , a _ { 2 } { , } { \ldots } { } , a _ { m } \}$ be a set of attributes, where m is the number of attributes. Each attribute $a _ { t }$ possesses its corresponding domain (i.e., values) which maps them to a corresponding concept hierarchy tree $T _ { t \cdot }$ A concept hierarchy represents a taxonomy of values for an attribute domain that are partially ordered according to a speci<sup>fi</sup>c-to-general relation. A value in the tree is also called a node. Based on these notations, we <sup>fi</sup>rst give a problem statement and then state the de<sup>fi</sup>nitions used in the problem.

Problem statement: Given a task-related relation with corresponding concept hierarchies and a set of thresholds at different levels and the association measure threshold, the aim of GAOI is to mine all interesting generalized knowledge.

De<sup>fi</sup>nition 1 (Value). Let $\nu _ { t , i }$ denote the $i _ { t h }$ node of tree $T _ { t } ,$ where the sequence of nodes are numbered according to some traversal order.

Example 2. In Fig. 1 in Appendix A, there are four attributes with four concept hierarchies $T _ { 1 } , T _ { 2 } , T _ { 3 }$ and $T _ { 4 } ,$ respectively. Suppose the node labels are numbered according to the level order traversal. We now have the values $\nu _ { 2 , 1 } { = } \mathrm { C a r }$ , and $\nu _ { 2 , 6 } { = } \operatorname* { P i c k } { \mathrm { - u p } }$ . Fig. 1 shows an illustration of the labeled concept hierarchy $T _ { 2 } .$

![](/api/attachments/WP2XKEHW/fulltext/images/f2eda50879d5ceb3a698b8a22fe7fa7a2c21044390810f2fa57dba383016e873.jpg)  
Fig. 1. Concept hierarchy T with labeling.

De<sup>fi</sup>nition 2 (Valueset). A valueset $l = \{ \nu _ { t _ { 1 } , i _ { 1 } } , \nu _ { t _ { 2 } , i _ { 2 } } , . . . , \nu _ { t _ { r } , i _ { r } } \}$ is a nonempty set of values, where no two values in the set belong to the same attribute, i.e., all $t _ { p } \neq t _ { q } . .$ A valueset with k values is called a k-valueset.

For example, l={Kia, Compact Car} is a 2-valueset, while {General $\mathrm { C a r , V a n } \}$ is not.

De<sup>fi</sup>nition 3 (Level, Leaf, and Nonleaf). Let $l \nu l ( \nu _ { t , i } )$ denote the level of value $\nu _ { t , i } ,$ let leaf(T<sub>t</sub>) denote the set of leaf nodes of tree $T _ { t ; }$ and let nonleaf(T ) denote the set of non-leaf nodes of tree $T _ { t \cdot }$

Example 3. In Fig. 1, we have $l \nu l ( \nu _ { 2 , 1 } ) = 3 , l \nu l ( \nu _ { 2 , 9 } ) = 1$ , leaf(T<sub>2</sub>) = {Compact Car, Fullsize Car, Sports Car, Sporty $\mathrm { C a r , . . . , }$ Compact SUV, Fullsize SUV}.

De<sup>fi</sup>nition 4 (Tuple and Rid). Let m be the number of attributes in the relation. A primitive tuple is an m-valueset, where each value is in leaf (T ) for some t. Further, a generalized tuple g is an m-valueset, where each value is in leaf(T ) or nonleaf(T ) for some t. A relational database D is a set of primitive tuples. Each tuple in database D is associated with a unique identi<sup>fi</sup>er Rid.

For reducing the time in scanning database, the cover concept [28,34] is adopted to record the rids-lists of values.

De<sup>fi</sup>nition 5 (Cover). For each value $\boldsymbol { v } _ { t , i } ,$ let $c o v ( \nu _ { t , i } )$ denote the cover of value $\nu _ { t , i } ,$ which is the set of Rids for primitive tuples in D whose values are descendents of $\nu _ { t , i }$ in the concept hierarchy $T _ { t \cdot }$ For each valueset $l = \{ \nu _ { t _ { 1 } , i _ { 1 } } , ~ \nu _ { t _ { 2 } , i _ { 2 } } , . . . , \nu _ { t _ { r } , i _ { r } } \} , ~ c o v ( l ) = c o v ( \nu _ { t _ { 1 } , i _ { 1 } } ) ~ \cap . . . , ~ \cap ~ c o v ( \nu _ { t _ { r } , i _ { r } } )$ $( 1 \leq r \leq m )$

Example 4. In Table 1, each record is a primitive tuple and has a unique number Rid. Those tuples in Tables 2 and 3 are generalized tuples. From Table 1, we <sup>fi</sup>nd that cov(Chevrolet)={2, 8, 12, 20}, cov(Compact $\mathsf { V a n } ) =$ {8, 11, 12} and cov({Chevrolet, Compact Van})={8, 12}. After performing the concept hierarchy ascension, Chevrolet is ascended to USA and Compact Van is ascended to Van. According to De<sup>fi</sup>nition $5 ,$ the cover of a general value is the union of Rids that contains the descendents of the general value in concept hierarchy tree. Therefore, we have $c o \nu ( \mathrm { U S A } ) = \{ 2 , 5 , 8 ,$ 11, 12, 17, 19, 20} and $c o \nu ( \mathrm { V a n } ) { = } \{ 2 , 8 , $ 11, 12, 14}. The cover of valueset cov ({USA, Van}) is the intersection of cov(USA) and cov(Van), which is {2, 8, 11, 12}.

De<sup>fi</sup>nition 6 (Support). The support of a valueset l in a database $D ,$ where sup(l), is the number of Rids in cov(l) versus the total number of tuples in $D ,$ as shown in Eq. (1)

$$
\sup (l) = \frac {| c o v (l) |}{| D |}.\tag{1}
$$

Example 5. Since |cov({USA, Van})|=−{2, 8, 11, 12}|=4 and |D|=20, we obtain sup $( \{ \mathrm { U S A } , \mathrm { V a n } \} ) = 4 / 2 0 = 2 0 \% .$

The values in each valueset may come from different concept levels. It is expected that those higher level values have larger supports, while lower level ones have smaller supports. Therefore, assigning different minimum support thresholds for different concept levels is necessary [17].

De<sup>fi</sup>nition 7 (Minimum level support, MLS). Each level in a concept hierarchy has a minimum support constraint speci<sup>fi</sup>ed by the user. Hence, each value $\nu _ { t , i }$ in a concept hierarchy has a minimum level support based upon its level, denoted as $\mathsf { M L S } ( l \nu l ( \nu _ { t , i } ) )$ . Moreover, since higher level values are more general than lower level ones, the MLSs must obey the nondecreasing assumption, i.e., the MLSs of higher levels should not be less than the ones in lower level.

Adopting a similar approach proposed by Liu et al. [27], we then de-<sup>fi</sup>ne the minimum support threshold of a generalized valueset as the lowest MLS value among the values in the valueset. By doing $s 0 ,$ we can achieve the goal of having higher minimum support thresholds for valuesets that only involve more general values, and having lower minimum support thresholds for valuesets that involve speci<sup>fi</sup>c values.

De<sup>fi</sup>nition 8 (MLS of valueset). Each valueset has an MLS. The MLS of valueset $l = \{ \nu _ { t _ { 1 } , i _ { 1 } } , \nu _ { t _ { 2 } , i _ { 2 } } , . . . , \nu _ { t _ { \mathrm { r } } , i _ { \mathrm { r } } } \}$ (1≤r≤m) is equal to MLS(l)=min[MLS $( l \nu l ( \nu _ { t _ { 1 } , r _ { 1 } } ) ) , \mathrm { M L S } ( \dot { l } \nu l ( \tilde { \nu _ { t _ { 2 } , r _ { 2 } } } ) ) , . . . , \mathrm { M L S } ( l \nu l ( \nu _ { t _ { 2 } , i _ { \mathrm { r } } } ) ) ]$

Example 6. Consider three levels 1, 2, and 3 in the concept hierarchy. Assume the MLS are: $\mathrm { M L S } ( 1 ) = 7 \% , \mathrm { M L S } ( 2 ) = 1 0 \% ,$ , and $\mathrm { M L S } ( 3 ) = 1 5 \%$ The value $\nu _ { 1 , 1 0 }$ (Kia) and $\nu _ { 2 , 1 } ~ ( \mathrm { C a r } )$ shown in Fig. 1 in Appendix A are at levels 1 and 3, so their MLSs are 7% and 15%, respectively. If there is a valueset={Kia, Car}, then $\mathrm { M L S } ( \{ \nu _ { 1 , 1 0 } , \nu _ { 2 , 1 } \} ) = 7 \% .$

De<sup>fi</sup>nition 9 (Potentially frequent and Frequent). Let MIN denote the MLS of the lowest level of the concept hierarchy. A value v is potentially frequent if sup(v)≥MIN. A valueset l is potentially frequent if sup $( \nu ) \geq \mathrm { M L S } ( l ) \ \forall \ \nu \in l .$ On the other hand, a valueset l is frequent if sup $( l ) { \geq } \mathrm { M L S } ( l )$

Example 7. Let us continue with Example 6. The MIN is 7%. Assume there are 4 values: $\nu _ { 1 , 1 } , \mathrm { l e v e l } = 3$ , suppo $\mathrm { t } = 8 \% ; \nu _ { 2 , 5 } ,$ level=2, sup-$\begin{array} { r } { \mathsf { p o r t } { = } 2 0 \% ; ~ \nu _ { 3 , 9 } , } \end{array}$ level=1, support=5%, and $\nu _ { 4 , 1 2 } \mathrm { \ l e v e l } = 1$ , support=7%. Then, $\nu _ { 1 , 1 }$ is a potentially frequent value; $\nu _ { 2 , 5 }$ and $\nu _ { 4 , 1 2 }$ are frequent. Value $\nu _ { 3 , 9 }$ is not a potentially frequent value because sup $\left( \nu _ { 3 , 9 } \right) { < } \mathrm { M I N }$ , and $\nu _ { 1 , 1 }$ is not frequent because $s u p ( \nu _ { 1 , 1 } ) { < } \mathsf { M L S } ( l \nu l$ $\left( \nu _ { 1 , 1 } \right) )$ . The valueset $\left\{ \nu _ { 1 , 1 } , \ \nu _ { 4 , 1 2 } \right\}$ is a potentially frequent valueset, and the valueset $\left\{ \nu _ { 1 , 1 } , \nu _ { 2 , 5 } \right\}$ is not a potentially frequent valueset because su $( \nu _ { 1 , 1 } ) – \mathrm { M L S } ( l \nu l ( \nu _ { 2 , 5 } ) ) = 1 0 \%$

In Section 1, we mentioned that an interesting generalized valueset must satisfy three constraints. Obviously, the frequent generalized valuesets in De<sup>fi</sup>nition 8 satisfy the <sup>fi</sup>rst two constraints, the minimum support constraint and the multiple level support constraint. In order to satisfy the third constraint, the strong association constraint, we de<sup>fi</sup>ne a new measure to estimate the association strength of a generalized valueset [13].

De<sup>fi</sup>nition 10 (Association). Let $l = \{ \nu _ { t _ { 1 } , i _ { 1 } } , \nu _ { t _ { 2 } , i _ { 2 } } . . . , \nu _ { t _ { r } , i _ { r } } \}$ be a generalized valueset. Let $A ( l )$ denote the association strength of a generalized valueset l.

$$
A (l) = \frac {\sup (l)}{\sup \left(v _ {t _ {1} , i _ {1}}\right) \times \dots \times \sup \left(v _ {t _ {r} , i _ {r}}\right)}.\tag{2}
$$

The values in a generalized valueset l are independent if $A ( l ) = 1 ;$ otherwise, the values are dependent and correlated. An association measure above 1 indicates positive relation. A generalized valueset l has a strong association if $A ( l ) \geq \delta ,$ , where δ≥1 is a user-speci<sup>fi</sup>ed constant.

## 4. Global attribute-oriented induction

In this section, we propose a global AOI (GAOI) algorithm to im prove the insuf<sup>fi</sup>ciency of the traditional AOI method. The GAOI algorithm employs the multiple minimum supports concept and multiple-level mining technique to generate global generalized knowledge. The input of the GAOI algorithm includes four parts: (1) a task-related relation; (2) a set of concept hierarchies; (3) a set of MLS thresholds; and (4) an association measure threshold. The output consists of interesting generalized tuples learned from the relational relation. The major steps of GAOI are shown in Fig. 2. We <sup>fi</sup>rst discuss how to collect and transform the input relational data into the hierarchical-information encoded table. Then we detail the algorithm designed for inducing all frequent generalized tuples. Finally, the pruning and transformation processes are shown.

<table><tr><td>Algorithm GAOI.</td></tr><tr><td>Input: (1) A task-related relation; (2) a set of concept hierarchies; (3) a set of MLS thresholds; (4) an association measure threshold.</td></tr><tr><td>Output. Interesting generalized tuples learned from the task-related relation.</td></tr><tr><td>Method. Four steps:Step 1. Collect and encode the task-relevant tuples.Step 2. Discover all frequent generalized tuples.Step 3. Prune uninteresting generalized tuples.Step 4. Transform and Output final tuples.</td></tr></table>

Fig. 2. GAOI algorithm

![](/api/attachments/WP2XKEHW/fulltext/images/26c41de98293bbf0a967b0dc8bf035f4bf3dbe23f2ce24b4b84832224e855083.jpg)  
Fig. 3. Concept hierarchy for price showing encoded numbers.

## 4.1. Collect and encode the task-relevant tuples

GAOI <sup>fi</sup>rst collects the data set that is relevant to the learning task using relational database operations, $\mathrm { e . g . }$ , projection and selection. The retrieved task-relevant tuples are stored in a table called the initial relation table. Each tuple in the initial relation has a unique identi<sup>fi</sup>er called Rid. Next, the initial relation can be transformed into a hierarchical-information encoded table, in which each tuple contains a record id (Rid) and GID (Generalized Identi<sup>fi</sup>er) codes. Each GID code is a number string containing the path information of the corresponding attribute in the corresponding concept hierarchy.

Example 8. In Table 1, the price attribute is the fourth attribute in the tuple. Suppose the value of the price is ‘19,800’. According to the concept hierarchy shown in Fig. 3, this value can be encoded as ‘4121’, where the <sup>fi</sup>rst digit ‘4’ represents the fourth attribute in tuple, the second ‘1 represents the ‘Low Price’ at level-3, the third ‘2’ represents ‘Economical’ at level-2, and the fourth ‘1’ indicates ‘15,000–19,999’ at level-1.

Since the concept hierarchies are constructed in advance, the <sup>fi</sup>rst task we have to do is to determine the GID codes for all leaf nodes in all concept trees. This can be done by traversing all concept trees once. After that, we have a value-GID map table that can help us to <sup>fi</sup>nd the corresponding GID code when we are given an attribute value. Here, please note that since we store each digit by a short integer (two bytes long) in memory, the number of branches in a node can be far greater than 10. Then, the next task we must do is to scan the database one tuple after another and at the same time transform each attribute value to its GID code by searching the value-GID map table. Using this process can build the encoded table successfully.

It is bene<sup>fi</sup>cial to transform the original values to GID codes, because it requires fewer bits to represent the position of an encoded string in a hierarchy than simply using the corresponding object-identi<sup>fi</sup>er. The taxonomic information for each value in Table 1 is encoded as a GID code following the encoding rule mentioned above. The results are shown in Table 4 (T). Throughout the rest of this paper, we refer to the sample table, Table 4 in our explanation.

## 4.2. The mining algorithm

The mining algorithm for discovering all frequent generalized valuesets (FGV) is extended from the multiple-level mining algorithm (ML\_T2LA) proposed by Han and Fu [17] as well as from the multiple minimum supports algorithm (MSapriori) proposed by Liu et al. [27]. The <sup>fi</sup>rst step of the algorithm is to scan the encoded table T to <sup>fi</sup>nd all distinct values (C ) for all levels. Next, the potentially frequent values (P<sub>1</sub>) and frequent values, i.e., 1-valuesets $\left( L _ { 1 } \right)$ , are generated from set $C _ { 1 } ,$ as de<sup>fi</sup>ned in De<sup>fi</sup>nition 8.

Let $L _ { k }$ be the set of frequent k-valuesets, whose support values are equal to or greater than the MLS of the corresponding valuesets. The 2-valuesets are generated using $P _ { 1 }$ and $L _ { 1 } ,$ while the k-valuesets (kN2) are generated using just $L _ { k - 1 } .$ . Note that since a 2-valueset may contain values at different concept levels, the result of $L _ { 1 } \times L _ { 1 }$ cannot cover all potentially frequent 2-valuesets. So, we have to combine one potentially frequent value with another frequent value to enumerate all potentially frequent 2-valuesets (for the formal proof, please refer to Lemma 2). The generation process is shown in Fig. 4. The k-valueset generation is repeated until k is equal to the number of attributes in the tuple. Finally, we obtain all generalized tuples by uniting all k-valuesets. The details of the FGV algorithm are shown in Fig. 5.

In line 1 a pass is made over T to produce the set of all distinct values $C _ { 1 } .$ The algorithm init-pass, which contains the following two steps, is applied:

1. A pass is made over $T ,$ to record the actual support and the cover of each value at each concept level.

2. The values are then ordered according to their MLS values in ascending order i.e., from lowest concept level to topmost concept level.

Results encoded from Table 1: T.

<table><tr><td>Rid</td><td>Manufacturer</td><td>Model</td><td>Engine</td><td>Price</td><td>Rid</td><td>Manufacturer</td><td>Model</td><td>Engine</td><td>Price</td></tr><tr><td>1</td><td>1111</td><td>2111</td><td>3120</td><td>4112</td><td>11</td><td>1311</td><td>2211</td><td>3210</td><td>4211</td></tr><tr><td>2</td><td>1312</td><td>2212</td><td>3310</td><td>4211</td><td>12</td><td>1312</td><td>2211</td><td>3220</td><td>4211</td></tr><tr><td>3</td><td>1121</td><td>2111</td><td>3120</td><td>4112</td><td>13</td><td>1112</td><td>2112</td><td>3120</td><td>4122</td></tr><tr><td>4</td><td>1122</td><td>2112</td><td>3310</td><td>4122</td><td>14</td><td>1113</td><td>2212</td><td>3120</td><td>4122</td></tr><tr><td>5</td><td>1314</td><td>2231</td><td>3310</td><td>4211</td><td>15</td><td>1111</td><td>2111</td><td>3120</td><td>4112</td></tr><tr><td>6</td><td>1123</td><td>2112</td><td>3310</td><td>4122</td><td>16</td><td>1124</td><td>2221</td><td>3310</td><td>4121</td></tr><tr><td>7</td><td>1212</td><td>2121</td><td>3320</td><td>4221</td><td>17</td><td>1314</td><td>2231</td><td>3310</td><td>4211</td></tr><tr><td>8</td><td>1312</td><td>2211</td><td>3220</td><td>4211</td><td>18</td><td>1111</td><td>2111</td><td>3120</td><td>4111</td></tr><tr><td>9</td><td>1213</td><td>2121</td><td>3310</td><td>4222</td><td>19</td><td>1313</td><td>2231</td><td>3310</td><td>4211</td></tr><tr><td>10</td><td>1222</td><td>2122</td><td>3320</td><td>4222</td><td>20</td><td>1312</td><td>2232</td><td>3320</td><td>4211</td></tr></table>

![](/api/attachments/WP2XKEHW/fulltext/images/bc77f61071bfdfb29ae3da114c8520ef54837e8d5c4468c0963b25b90df8ccaf.jpg)  
Fig. 4. Illustration of k-valueset generation

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm FGV.
Input. (1) The hierarchical-information encoded table T; and (2) the set of MLS thresholds.
Output. All frequent generalized valuesets.
Algorithm FGV(T, MLSs)
// |attr|: the number of attributes in the tuples
// S: the set of frequent valuesets for all levels
{
1  $C_{1} = \text{init-pass}(T)$ ;
2  $P_{1} = \{v \mid v \in C_{1}, \sup(v) \geq \text{MIN}\}$ ;
3  $L_{1} = \{p \mid p \in P_{1}, \sup(p) \geq \text{MLS}(lvl(p))\}$ ;
4  $S = L_{1}$ 
5 for  $(k = 2; k \leq |\text{attr}|; k++)$  do {
6    if k = 2 then
7    $L_{2} = 2$  valueset-frequent-gen( $L_{1}, P_{1}$ )
8    else
9    $L_{k} = \text{frequent-gen}(L_{k-1})$ ;
10    $S = S + L_{k}$ 
11    }
}
</div>

Fig. 5. FGV algorithm.

In line 2 all potentially frequent values (P ) for all levels are generated from $C _ { 1 } .$ Although a database could be large, only distinct attribute values and their abstraction values which conform to the support constraint can be included in $P _ { 1 } .$ Frequent values, i.e., 1-valuesets (L ), are then obtained from $P _ { 1 }$ (line 3). The steps can be formulated as (Fig. 6):

Example 9. Consider T as shown in Table 4, and the concept hierarchies in Fig. 1 in Appendix A. Assume that MLS(1)=15%, MLS(2)=25%, and MLS(3)=35%. Then MIN, which is the MLS of the lowest level, is 15%. Table 5 shows partial results for set $P _ { 1 }$ , where the right hand column indicates whether these values are in set $L _ { 1 } .$ In $P _ { 1 }$ we keep the values with supports≥MIN (15% in this example), while in L we store only those values whose supports are no less than the MLS of the corresponding values. The cover <sup>fi</sup>eld records the Rids of those primitive tuples in T whose values are descendents of the table value in the concept hierarchy. The wildcard character ‘\*’ can be used to substitute any digit. For example, the value 111\* may contain 1111, 1112, 1113…and so on

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$P_{1}=\{v\mid v\in C_{1},sup(v)\geq MIN\}$ 

1. for each value v in  $C_{1}$  do {

2. if sup(v)≥MIN then

3. insert &lt;v&gt; into  $P_{1}$ ;

4. }
</div>

Fig. 6. Steps for generating $P _ { 1 }$ and $L _ { 1 } .$

$$
P _ {1}.
$$

<table><tr><td>Value</td><td>Support (%)</td><td>Cover</td><td> $L_1$ </td></tr><tr><td>1111</td><td>15</td><td>1,15,18</td><td>Y</td></tr><tr><td>1312</td><td>20</td><td>2,8,12,20</td><td>Y</td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td>4211</td><td>40</td><td>2,5,8,11,12,17,19,20</td><td>Y</td></tr><tr><td>111*</td><td>25</td><td>1,13,14,15,18</td><td>Y</td></tr><tr><td>112*</td><td>20</td><td>3,4,6,16</td><td>N</td></tr><tr><td>131*</td><td>40</td><td>2,5,8,11,12,17,19,20</td><td>Y</td></tr><tr><td>211*</td><td>35</td><td>1,3,4,6,13,15,18</td><td>Y</td></tr><tr><td>221*</td><td>25</td><td>2,8,11,12,14</td><td>Y</td></tr><tr><td>223*</td><td>20</td><td>5,17,19,20</td><td>N</td></tr><tr><td>312*</td><td>30</td><td>1,3,13,1415,18</td><td>Y</td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td>411*</td><td>20</td><td>1,3,15,18</td><td>N</td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td>22**</td><td>50</td><td>2,5,8,11,12,14,16,17,19,20</td><td>Y</td></tr><tr><td>31**</td><td>30</td><td>1,3,13,1415,18</td><td>N</td></tr><tr><td>32**</td><td>15</td><td>8,11,12</td><td>N</td></tr><tr><td>33**</td><td>55</td><td>2,4,5,6,7,9,10,16,17,19,20</td><td>Y</td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td></tr></table>

and $3 1 ^ { * * }$ may contain 311\*, 312\*, 3111, 3122…etc. Furthermore, the values stored in $P _ { 1 }$ are ordered from lower abstract concept levels to higher abstract concept levels as shown in Table 5.

The derivation of the frequent k-valuesets (kN1) proceeds as in line 5 through line 10. For each subsequent pass, say pass k, the frequent valuesets in $L _ { k - 1 }$ are used to generate the frequent valuesets $L _ { k }$ (obtained by the algorithm frequent-gen). However, i $\mathrm { f } k = 2 , L _ { 2 }$ is generated from $L _ { 1 }$ and $P _ { 1 } .$

Many of the previous frequent pattern generation algorithms have been designed based on the downward closure property [2], which states that if a set of items does not satisfy the minimum support constraint, then all its supersets also do not satisfy this constraint. The downward closure property enables us to prune infrequent itemsets ef-<sup>fi</sup>ciently. However, in the proposed model, the downward closure property no longer holds due to monotonic increase of support thresholds in the hierarchies. Let us consider the example below.

Example 10. Following Example 9 and the MLS values given for the three levels, assume we have the following support values.

<table><tr><td>Valueset</td><td>Support</td><td>MLS{}</td><td>Frequent</td></tr><tr><td>{4211}</td><td>40%</td><td>15%</td><td>Yes</td></tr><tr><td>{223*}</td><td>20%</td><td>25%</td><td>No</td></tr><tr><td>{33**}</td><td>55%</td><td>35%</td><td>Yes</td></tr><tr><td>{223*, 33**}</td><td>20%</td><td>25%</td><td>No</td></tr><tr><td>{4211, 223*, 33**}</td><td>20%</td><td>15%</td><td>Yes</td></tr></table>

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 2valueset-frequent-gen( $L_{1},P_{1}$ )

// attr(x): the attribute of the value x
{
    for each value  $v \in L_{1}$  do
    for each value  $p \in P_{1}$  whose order follows the value v do
    if sup(p) ≥ MLS(lvl(v)) and attr(v) &lt;&gt; attr(p) then {
    cov(&lt;v,p&gt;) = intersection(v,p);
    sup(&lt;v,p&gt;) = |cov(&lt;v,p&gt;)| / |D|;
    if sup(&lt;v,p&gt;) ≥ MLS(lvl(v)) then
    insert &lt;v,p&gt; into  $L_{2}$ ;
    }
}
</div>

Fig. 7. 2valueset-frequent-gen algorithm

According to the downward closure property, the 3-valueset {4211, 223\*, 33\*\*} cannot be frequent because $\{ 2 2 3 ^ { * } , 3 3 ^ { * * } \}$ is not frequent. However, as shown above, {4211, 223\*, 33\*\*} is indeed frequent.

To solve this problem, we propose a concept called the level closure property.

Property 1 (Level Sorted Order). The values in a valueset $\{ \nu _ { 1 } , \nu _ { 2 } , . . . . , \nu _ { k } \}$ satisfy the level sorted order $i f l \nu l ( \nu _ { 1 } ) { \le } l \nu l ( \nu _ { 2 } ) . . . \le l \nu l ( \nu _ { k } )$

For example, the level sorted order of values $1 2 3 1 , 2 1 ^ { * * } , 3 1 2 ^ { * }$ , and $4 2 ^ { * * }$ is 1231, 312\*, 21\*\*, and $4 2 ^ { * * }$ . Similarly, the following valuesets {1231, 312\*}, {1231, 312\*, 21\*\*}, and $\{ 3 1 2 ^ { * } , 2 1 ^ { * * } , 4 2 ^ { * * } \}$ comply with the level sorted order.

Lemma 1 (Level Closure Property). If a level sorted k-valueset={v , $\nu _ { 2 } , . . . , \nu _ { k } \}$ is frequent, then all of its level sorted (k-1)-subsets with $\nu _ { 1 }$ are also frequent.

Proof. The k-valueset $\{ \nu _ { 1 } , \nu _ { 2 } , . . . , \nu _ { k } \}$ has k subsets with k-1 values, which can be divided into two groups, with or without $\nu _ { 1 } \colon$

$$
1 \colon \{v _ {1}, v _ {2}, \dots , v _ {k - 1} \}, \{v _ {1}, v _ {2}, \dots , v _ {k - 2}, v _ {k} \}, \dots , \{v _ {1}, v _ {3}, \dots , v _ {k} \};
$$

group $\underline { { ? } } \colon \{ \nu _ { 2 } , . . . , \nu _ { k } \} .$

Note that all valuesets in group 1 have the same lowest MLS, i.e., $\mathsf { M L S } ( l \nu l ( \nu _ { 1 } ) )$ ). If any valueset in group 1 is not frequent, i.e., its support is less than $\mathsf { M L S } ( l \nu l ( \nu _ { 1 } ) )$ , then the support of the entire valueset must be less than $\mathsf { M L S } ( l \nu l ( \nu _ { 1 } ) )$ . Therefore, the lemma follows.

Based on the level closure property, the 2valueset-frequent-gen algorithm takes two arguments: $L _ { 1 }$ and $P _ { 1 }$ (not just $L _ { 1 } ) ,$ and returns the set of all frequent 2-valuesets. The algorithm is described as (Fig. 7).

Example 11. Let us use the example from Table 5 to explain the above algorithm. $\operatorname { I f } \nu = 1 1 1 ^ { * } , \{ 1 1 1 ^ { * } , 4 1 1 ^ { * } \}$ is not a potentially frequent 2-valueset, because sup(411\*)=20% is less than MLS(lvl(111\*))=25%. The {111\*, 131\*} is also discarded, because {111\*} and {131\*} belong to the same attribute. The $\{ 1 1 1 ^ { * } , 3 1 ^ { * * } \}$ is a potentially frequent 2-valueset, although sup $( 3 1 ^ { * * } ) { < } \mathrm { M L S } ( l \nu l ( 3 1 ^ { * * } ) )$ , it satis<sup>fi</sup>es sup(31\*\*)≥MLS (lvl(111\*)). To determine if {111\*, 31\*\*} is in $L _ { 2 } ,$ we must compute its support by intersecting the covers of values {111\*} and {31\*\*}. Thus we obtain cov({111\*, 31\*\*})={1, 13, 14, 15, 18} and sup({111\*, 31\*\*})=25%. Since the support of {111\*, 31\*\*} is no less than MLS(lvl(111\*)), it is in L .

Lemma 2. The 2valueset-frequent-gen algorithm generates all frequent 2-valuesets from $L _ { 1 }$ and $P _ { 1 } .$

Proof. Consider a 2-valueset $( \nu , p )$ in the 2valueset-frequent-gen algorithm. The value p is selected from $P _ { 1 }$ rather than $L _ { 1 }$ (line 2), because the result of $L _ { 1 } \times L _ { 1 }$ may not contain those 2-valuesets that satisfy MLS (lvl(v)) but not MLS(lvl(p)). Therefore, the lemma follows.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm frequent-gen( $L_{k-1}$ )

{
    for each valueset  $u \in L_{k-1}$  in the same order do
    for each valueset  $v \in L_{k-1}$  whose order follows the value u do
    if  $u.value_{1} = v.value_{1}$  and...and  $u.value_{k-2} = v.value_{k-2}$  and
    attr( $u.value_{k-1}$ ) &lt;&gt; attr( $v.value_{k-1}$ ) then {
    cov(&lt;u,v&gt;) = intersection(u,v);
    sup(&lt;u,v&gt;) = |cov(&lt;u,v&gt;)| / |D|;
    if sup(&lt;u,v&gt;) ≥ MLS(lvl(u.value $_{1}$ )) then
    insert &lt;u,v&gt; into  $L_{k}$ ;
    }
}
</div>

Fig. 8. Frequent-gen algorithm

We now present the frequent-gen algorithm (Fig. 8). The algorithm takes $L _ { k - 1 } \ ( k { > } 2 )$ as an argument and returns the set of all frequent kvaluesets. The join step uses a double loop (lines 1–2) to generate the kvaluesets. It performs a similar task as apriori-gen in the Apriori algorithm [2], except that no two values of the same attribute can occur simultaneously in a valueset (line 3). Basically, it joins any two valuesets in $L _ { k - 1 }$ whose <sup>fi</sup>rst k-2 values are the same, but whose last values are different. After the join step, lines 4 and 5 perform the same task as in the 2valueset-frequent-gen algorithm. Finally, the algorithm keeps the k-valuesets with supports that are no less than the MLS of the <sup>fi</sup>rst value in valueset.

In the frequent-gen algorithm (Fig. 8), when we compare two values, since the values are encoded in GID codes, the actual operation is a comparison between two series of digit numbers. To make sure if two values are equal, all the digit numbers must be compared in order until the last digit number.

Example 12. Let $L _ { 2 }$ be {b1312, 4211N, b1312, 221\*N, b111\*, 211\*N, $< 1 1 1 ^ { * } , 3 1 2 ^ { * } { > } \rbrace$ , where the values in each valueset are in level-sorted order. After performing the algorithm, we preserve the 3-valueset {1312, 4211, 221\*} but discard the 3-valueset {111\*, 211\*, 312\*}.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$cov(\{1312, 4211, 221^{*}\}) = cov(\{1312, 4211\}) \cap cov(\{1312, 221^{*}\}) = \{2, 8, 12\},$ $sup(\{1312, 4211, 221^{*}\}) = 15\% (\geq \text{MLS}(lvl(1312)) = 15\%),$

preserved.

$cov(\{111^{*}, 211^{*}, 312^{*}\}) = cov(\{111^{*}, 211^{*}\}) \cap cov(\{111^{*}, 312^{*}\}) = \{1, 13, 15, 18\},$ $sup(\{111^{*}, 211^{*}, 312^{*}\}) = 20\% (&lt; \text{MLS}(lvl(111^{*})) = 25\%),$

discarded.
</div>

The FGV algorithm unites all k-valuesets where k is equal to m (line 10, Fig. 5). We thus obtain all frequent generalized valuesets.

## 4.3. Pruning and transformation

Not every generalized valueset is interesting enough to be presented to users. In this study, an association measure, as de<sup>fi</sup>ned in De<sup>fi</sup>nition 9, is proposed to <sup>fi</sup>lter out uninteresting valuesets. Using the algorithm shown in Fig. 9 we can remove all uninteresting generalized valuesets.

Example 14. Assume that we have a generalized tuple $l = \{ 1 3 1 ^ { * }$ 22\*\*, 33\*\*, 4211} with sup(l)= 25%. Further, assume that we have sup(131\*)=40%, sup(22\*\*)=50%, sup(33\*\*)=55%, sup(4211)= 40% and δ=5. Then l is of strong association, because $A ( l ) =$ 25%/(40%× 50% × 55% × 40%)= 5.68 (N5).

The <sup>fi</sup>nal step is to convert interesting frequent valuesets into generalized tuples with m attributes, where m is the number of attributes in the relation. This algorithm (Fig. 10) inserts the value of ‘Any’ to the valuesets, if the number of attributes of a frequent valueset is less than m. In a concept hierarchy, the most general concept is the null description (Any) which covers all possible values of the attribute.

```txt
Algorithm Association-pruning (S, δ)
// S: the set of all frequent valuesets
// δ : the threshold of the association measure
{
    for each valueset l in S do {
    A(l) = compute-association(l);
    if A(l) < δ then
    remove l from S;
}
```  
Fig. 9. Association-pruning algorithm.

Table 7

<table><tr><td colspan="2">Algorithm convert(S)</td></tr><tr><td colspan="2">// S: the set of all interesting frequent valuesets</td></tr><tr><td colspan="2">// |v|: the number of values in the valueset</td></tr><tr><td colspan="2">// |attr|: the number of attributes in the tuple</td></tr><tr><td colspan="2">{</td></tr><tr><td>1</td><td>for each valueset l in S do</td></tr><tr><td>2</td><td>if |v| &lt; |attr| then</td></tr><tr><td>3</td><td>for (i=1, i ≤ (|attr|-|v|), i++) do</td></tr><tr><td>4</td><td>insert &lt;Any&gt; into l</td></tr><tr><td colspan="2">}</td></tr></table>

Fig. 10. Convert algorithm.

Example 13. The source relation T in Table 1 has 4 attributes. A 2- valueset {1231, 21\*\*} can be converted to the generalized tuple {1231, 21\*\*, Any, Any}, because the 2-valueset did not contain the values with pre<sup>fi</sup>xes 3 and 4. Similarly the 3-valueset {211\*, 31\*\*, 42\*\*} can be converted to the generalized tuple {Any, 211\*, 31\*\*, 42\*\*}, because the 3-valueset did not contain the value with pre<sup>fi</sup>x 1.

Finally, the generalized tuples are transformed and outputted. To do so, we <sup>fi</sup>rst convert each GID code in the tuples to its original value. Next, we output the <sup>fi</sup>nal tuples. For example, the encoded tuple b111\*, 211\*, Any, 41\*\*N will be converted to bKorea, General Car, Any, Low PriceN.

## 5. Experiments

In this section, we discuss several experiments conducted to evaluate the performance of the proposed algorithm. The GAOI algorithm was implemented using the Java programming language and tested on a PC with an Intel Core 2 Duo 3.0 GHz processor and 2 GB main memory under the Windows XP operating system. A real dataset of credit card data was used in the experiments. To make the time measurements more reliable, no other application was running on the machine while the experiments were running.

We <sup>fi</sup>rst explain the source and properties of the real dataset. Then we present and discuss the generalized knowledge generated by the classic AOI and the GAOI algorithm, respectively. Finally, we focused on evaluating the performance of the GAOI algorithm under the various parameter settings. Speci<sup>fi</sup>cally, its performance was studied with respect to four factors, including: (1) the number of tuples; (2) the number of attributes; (3) the minimal support thresholds; and (4) the association threshold. For each factor, we noted how the run time and the number of generalized tuples varied as the value of the factor changed. We discuss a series of comparisons obtained by varying the values of these four factors.

## 5.1. Real dataset

The real dataset used in this study consists of credit card records collected from the survey research center at a university in Taiwan [11]. It is the collections of questionnaire surveyed on March 2002 and consists of 2 million tuples, each of which has 27 attributes including card type, frequency, sex, age, occupation, marital status, blood type, income, consumption, family size, etc. We invited two domain experts to select six attributes that have values well suited to repeated generalization and create concept hierarchies from them. The concept hierarchy for each attribute is shown in Fig. 2 in Appendix A. Since the attribute values for the dataset are stored as speci<sup>fi</sup>c codes de<sup>fi</sup>ned by the research center, we must convert these attribute values to leaf concepts, i.e., the GID code, before the generalization tasks could be started.

Generalized tuples generated by the classic AOI algorithm with Ta=3, Tr=15.

<table><tr><td>Frequency</td><td>Age</td><td>Occupation</td><td>Income</td><td>Family size</td><td>Consumption</td><td>Vote</td></tr><tr><td>Any</td><td>Any</td><td>Non-student</td><td>Low</td><td>Any</td><td>Low</td><td>21,597</td></tr><tr><td>Any</td><td>Young adult</td><td>Any</td><td>High</td><td>Any</td><td>High</td><td>8107</td></tr><tr><td>Any</td><td>Any</td><td>Non-student</td><td>High</td><td>Small</td><td>Low</td><td>5963</td></tr><tr><td>Any</td><td>Advanced age</td><td>Student</td><td>Low</td><td>Any</td><td>Low</td><td>3878</td></tr><tr><td>Any</td><td>Young adult</td><td>Student</td><td>Low</td><td>Small</td><td>Low</td><td>3140</td></tr><tr><td>Any</td><td>Young adult</td><td>Non-student</td><td>High</td><td>Large</td><td>Low</td><td>3121</td></tr><tr><td>Any</td><td>Young adult</td><td>Non-student</td><td>Low</td><td>Small</td><td>High</td><td>2797</td></tr><tr><td>Any</td><td>Young adult</td><td>Non-student</td><td>Low</td><td>Large</td><td>High</td><td>2205</td></tr><tr><td>Any</td><td>Advanced age</td><td>Non-student</td><td>Low</td><td>Small</td><td>High</td><td>2179</td></tr><tr><td>Any</td><td>Young adult</td><td>Student</td><td>Low</td><td>Large</td><td>Low</td><td>2163</td></tr><tr><td>Any</td><td>Advanced age</td><td>Non-student</td><td>High</td><td>Large</td><td>Low</td><td>1526</td></tr><tr><td>Any</td><td>Advanced age</td><td>Non-student</td><td>High</td><td>Any</td><td>High</td><td>1520</td></tr><tr><td>Any</td><td>Advanced age</td><td>Non-student</td><td>Low</td><td>Large</td><td>High</td><td>1462</td></tr><tr><td>Any</td><td>Advanced age</td><td>Student</td><td>High</td><td>Any</td><td>High</td><td>342</td></tr></table>

Partial generalized tuples generated by the classic AOI algorithm with Ta=10, Tr=80.

<table><tr><td>Frequency</td><td>Age</td><td>Occupation</td><td>Income</td><td>Family size</td><td>Consumption</td><td>Vote</td></tr><tr><td>Any</td><td>Any</td><td>Non-student</td><td>High</td><td>Any</td><td>80,001–150,000</td><td>6764</td></tr><tr><td>Often</td><td>Any</td><td>Any</td><td>&lt;10,001</td><td>Any</td><td>Low</td><td>4829</td></tr><tr><td>Sometimes</td><td>Any</td><td>Low-level</td><td>Any</td><td>Any</td><td>Low</td><td>3898</td></tr><tr><td>Any</td><td>Any</td><td>Self-business</td><td>Low</td><td>Any</td><td>40,001–80,000</td><td>2888</td></tr><tr><td>Any</td><td>Any</td><td>Young-student</td><td>&lt;10,001</td><td>Any</td><td>0–40,000</td><td>2746</td></tr><tr><td>Any</td><td>Any</td><td>Self-business</td><td>Low</td><td>Any</td><td>High</td><td>2061</td></tr><tr><td>Sometimes</td><td>Any</td><td>Home-worker</td><td>Low</td><td>Any</td><td>40,001–80,000</td><td>1862</td></tr><tr><td>Often</td><td>Any</td><td>Student</td><td>10,001–30,000</td><td>Any</td><td>40,001–80,000</td><td>1363</td></tr><tr><td>Any</td><td>Any</td><td>Student</td><td>High</td><td>Any</td><td>80,001–150,000</td><td>1198</td></tr><tr><td>Often</td><td>Any</td><td>Low-level</td><td>10,001–30,000</td><td>Any</td><td>40,001–80,000</td><td>724</td></tr><tr><td>Sometimes</td><td>Any</td><td>High-level</td><td>10,001–30,000</td><td>Any</td><td>40,001–80,000</td><td>722</td></tr><tr><td>Sometimes</td><td>Any</td><td>Young-student</td><td>10,001–30,000</td><td>Any</td><td>40,001–80,000</td><td>704</td></tr><tr><td>Sometimes</td><td>Any</td><td>High-level</td><td>&lt;10,001</td><td>Any</td><td>0–40,000</td><td>692</td></tr><tr><td>Seldom</td><td>Any</td><td>Low-level</td><td>&lt;10,001</td><td>Any</td><td>40,001–80,000</td><td>487</td></tr></table>

Table 8  
Generalized tuples generated by the GAOI algorithm: data size 60,000.

<table><tr><td>Seq.</td><td>Frequency</td><td>Age</td><td>Occupation</td><td>Income</td><td>Family size</td><td>Consumption</td><td>Support</td><td>Association</td></tr><tr><td>1</td><td>Any</td><td>Young adult</td><td>Non-student</td><td>&gt;60,000</td><td>Large</td><td>100,001–150,000</td><td>4088</td><td>22.77</td></tr><tr><td>2</td><td>Any</td><td>Young adult</td><td>Non-student</td><td>&gt;50,000</td><td>Large</td><td>100,001–150,000</td><td>4141</td><td>15.05</td></tr><tr><td>3</td><td>Any</td><td>Young adult</td><td>Non-student</td><td>High</td><td>Large</td><td>100,001–150,000</td><td>4360</td><td>6.30</td></tr><tr><td>4</td><td>Any</td><td>Young adult</td><td>Sales</td><td>Any</td><td>Large</td><td>100,001–150,000</td><td>4088</td><td>18.75</td></tr><tr><td>5</td><td>Any</td><td>Any</td><td>Student</td><td>&lt;10,001</td><td>Any</td><td>&lt; 40,000</td><td>4885</td><td>4.85</td></tr><tr><td>6</td><td>Any</td><td>Any</td><td>Student</td><td>&lt;10,001</td><td>Any</td><td>20,001–40,000</td><td>3074</td><td>4.08</td></tr><tr><td>7</td><td>Any</td><td>Any</td><td>Student</td><td>&lt;10,001</td><td>Any</td><td>Low</td><td>5701</td><td>2.14</td></tr><tr><td>8</td><td>Any</td><td>Young adult</td><td>Non-student</td><td>High</td><td>Large</td><td>80,001–150,000</td><td>5173</td><td>3.90</td></tr><tr><td>9</td><td>Any</td><td>20–24</td><td>Non-student</td><td>High</td><td>Any</td><td>80,001–150,000</td><td>3074</td><td>3.79</td></tr><tr><td>10</td><td>Any</td><td>Any</td><td>Home worker</td><td>Any</td><td>5</td><td>High</td><td>3073</td><td>2.88</td></tr><tr><td>11</td><td>Any</td><td>Any</td><td>Sales</td><td>High</td><td>Large</td><td>Any</td><td>3135</td><td>2.76</td></tr><tr><td>12</td><td>Any</td><td>Young adult</td><td>Any</td><td>High</td><td>5</td><td>High</td><td>3080</td><td>2.55</td></tr><tr><td>13</td><td>Any</td><td>30–34</td><td>Non-student</td><td>High</td><td>Large</td><td>Any</td><td>3193</td><td>2.40</td></tr><tr><td>14</td><td>Any</td><td>20–24</td><td>Non-student</td><td>Any</td><td>Large</td><td>High</td><td>3205</td><td>2.39</td></tr><tr><td>15</td><td>Any</td><td>25–34</td><td>Non-student</td><td>Any</td><td>5</td><td>High</td><td>3188</td><td>2.28</td></tr><tr><td>16</td><td>Often</td><td>20–24</td><td>Any</td><td>High</td><td>Any</td><td>Any</td><td>3016</td><td>2.38</td></tr><tr><td>17</td><td>High</td><td>20–24</td><td>Any</td><td>High</td><td>Any</td><td>Any</td><td>3073</td><td>2.37</td></tr><tr><td>18</td><td>Any</td><td>30–34</td><td>Any</td><td>High</td><td>3–4</td><td>Any</td><td>3084</td><td>2.36</td></tr><tr><td>19</td><td>Any</td><td>Young adult</td><td>Sales</td><td>High</td><td>Any</td><td>Any</td><td>3415</td><td>2.26</td></tr><tr><td>20</td><td>Any</td><td>Young adult</td><td>Sales</td><td>Any</td><td>Any</td><td>High</td><td>3024</td><td>2.21</td></tr><tr><td>21</td><td>Seldom</td><td>Any</td><td>Housewife</td><td>Any</td><td>Any</td><td>Any</td><td>3125</td><td>2.22</td></tr><tr><td>22</td><td>Any</td><td>Any</td><td>Housewife</td><td>Any</td><td>Any</td><td>80,001–150,000</td><td>3669</td><td>2.02</td></tr></table>

## 5.2. Generalized tuples from the classic AOI

We present the generalized knowledge produced by the classic AOI algorithm in the section. We randomly extracted 60,000 tuples, each with 6 attributes, from the credit card dataset for the experiments. There are two sets of thresholds used in the test: (1) Ta=3, Tr=15; and (2) Ta=10, Tr=80. The generalized results generated from the classic AOI method are shown in Tables 6 and 7.

From Table 6, we can see that when Ta threshold is low, the tuples are generalized to the more general level. This generalized relation indicates how the whole population is constituted by generalized tuples. However, the results are just a snapshot of the generalized knowledge.

In the second experiment, we give a larger Ta threshold and get richer results. Table 7 shows the partial results with Ta=10 and Tr=80. A larger Ta threshold will retain more speci<sup>fi</sup>c values for each attribute, which results in too many generalized tuples. Based upon the generalization threshold Tr, we further generalize the relation. There are many strategies to reduce the generalized tuples and the <sup>fi</sup>nal results depend on the selected strategy. The <sup>fi</sup>nal result shows a snapshot of a set of generalized knowledge constituting the entire relation.

Since the generalized tuples in Table 6 look very differently from those in Table 7, we see the weakness of traditional AOI lies in that it is hard to provide us a global understanding of the underlying data, because its picture changes dramatically whenever the parameters are changed.

![](/api/attachments/WP2XKEHW/fulltext/images/70295b9f5262f278e1c077617d1cab199bb7d5a0303cd2728d2c56eec61ce184.jpg)  
Fig. 11. Run time vs. data size.

## 5.3. Generalized tuples from the GAOI

In this section, we discuss the generalized knowledge produced by the GAOI algorithm. In the test, we randomly extracted 60,000 tuples, each with 6 attributes, from the credit card dataset. The MLS values, from speci<sup>fi</sup>c to general, are as follows: MLS(1)=5%; MLS(2)=8%; and MLS(3)=10%. In addition, the association measure threshold is set to 2. Applying the GAOI algorithm, we get 96 interesting generalized tuples. Some interesting tuples are shown in Table 8.

Each of the generated tuples in the table can be interpreted as a generalized knowledge. For example, tuple 1 indicates that about 6.8% (4088/60,000) of users have a pro<sup>fi</sup>le of “young adult, non-student, salaryN60,000, large family size, and consumption between 100,001 and 150,000.” Furthermore, the association value of the tuple is very high (22.77). It means that the associations among these attribute values are quite strong. However, if the association of this tuple is low, then it only shows us the composition of the population; it does not imply a strong relation among them. In the following we give some explanations for the generalized tuples with high association values.

Tuples 1, 2, and 3 do have high association values. They indicate that those young adults with a high salary and large family size are very likely to spend more money with credit cards. Tuple 4 indicates that a young salesperson, no matter how much he/she earns, is willing to spend more with a credit card. From tuples 5, 6 and 7, we see that a student with a low salary will spend less. However, tuples 16 and 17 indicate that a young person with a high salary uses a credit card more often than others. Tuple 21 points out that about 5% of housewives seldom use credit cards, while tuple 22 indicates that about 5% of housewives spend between \$80,001 and 150,000 via credit card each year.

![](/api/attachments/WP2XKEHW/fulltext/images/58747e74a14be833aefa002244a2d47357d5b2db2240d8b54aae9181875e09cd.jpg)  
Fig. 12. Number of tuples vs. data size.

![](/api/attachments/WP2XKEHW/fulltext/images/d4eb05b48916d6674feb8a6e7c1a98135261c6bab39a783cf457bb599893c57b.jpg)  
Fig. 13. Run time vs. threshold.

The advantage of our method is that all interesting generalized knowledge originally existing in many AOI snapshots are collected in a single table, Table 8. Without using GAOI, this global knowledge can only be obtained by repeatedly trying AOI with all possible parameters settings and then extracting the valuable generalized tuples from all these snapshots.

## 5.4. Performance evaluations

In this section, we describe a series of experiments. In the <sup>fi</sup>rst, we evaluate the run time for the GAOI algorithm using varied data size (number of tuples) from 25,000 to 150,000 but <sup>fi</sup>xed MLS thresholds. The MLS values from speci<sup>fi</sup>c to general are MLS(1)=5%, MLS(2)= 10% and MLS(3)=15%. In addition, different numbers of attributes are evaluated: 4 attributes—frequency, age, occupation, and income (attr-4); 5 attributes—plus consumption (attr-5); and 6 attributes— plus family size (attr-6). The results are illustrated in Fig. 11. From this <sup>fi</sup>gure, we can see that the time required increases as the number of tuples increases. Moreover, when more attributes are given, more run time is required. This is because the GAOI algorithm generates the potentially frequent 2-valuesets by recursively combining distinct attribute values. When the attributes increase, the more attribute values are generated. In addition, the support values of k-valuesets are calculated by intersecting two of their (k-1)-valuesets. More tuples resulted more cover lists. Hence, both the number of attributes and the number of tuples have signi<sup>fi</sup>cant effect on the run time.

We also study how the number of generalized tuples changes as the data size changes. Since not every generalized tuple is interesting, we set the association measure to be 1.1. Fig. 12 shows the results of <sup>fi</sup>ltering for different data sizes and different numbers of attributes. The results show that more generalized tuples are generated as more attributes are considered. The reason is because more attributes result in more generalized tuples, which in turn generate more interesting tuples. However, for the same number of attributes, the number of generalized tuples remains almost the same even though the data size changes. The reason for this may be that, since the data are all drawn from the same dataset, the data sets have similar properties, even though their sizes are different.

![](/api/attachments/WP2XKEHW/fulltext/images/3c9a2016f9b363e8dc2c587184957b3a69a4d3237eda51b52a86067ac5cb611e.jpg)  
Fig. 14. Number of tuples vs. threshold.

![](/api/attachments/WP2XKEHW/fulltext/images/d52adff258d772943cc95060122a5ef71e2864e5483c297280bd640caf183dc0.jpg)  
Fig. 15. Number of generalized tuples vs. association measure (from 1 to 1.9)

Next, we study how the MLS thresholds in<sup>fl</sup>uence the run time of the GAOI algorithm. To this end, we give three sets of thresholds and <sup>fi</sup>x the data size at 25,000 and the number of attributes at 6. The thresholds are set from speci<sup>fi</sup>c to general as follows: 3%–6%–9%; 4%–7%–10%; 5%–10%–15%. Fig. 13 shows the performance curve. Time required increases as the threshold values decreases. The reason is because when the thresholds decrease, the number of potentially frequent valuesets increase, which in turn increases the run time.

We also demonstrate how the number of generalized tuples changes as the MLS values change. We set the association measure as 1.1. Fig. 14 shows the results for different sets of thresholds. From this <sup>fi</sup>gure, one can see that the number of generalized tuples decreases as the threshold values get larger. This result is quite reasonable, because the thresholds are used to <sup>fi</sup>lter out the valuesets, smaller thresholds naturally result in more valuesets.

As mentioned earlier, an association measure is proposed to <sup>fi</sup>lter out uninteresting tuples. In the <sup>fi</sup>nal experiment, we evaluate the in-<sup>fl</sup>uence of the association measures. The parameters of experiment are: data size is <sup>fi</sup>xed at 60,000 tuples; number of attributes is 6; and MLS thresholds are 5%, 8%, 10%. Fig. 15 illustrates the variation of the number of generalized tuples with different association measures, from 1 to 1.9. Fig. 16 shows the results given a large scale of association measure, from 2 to 9. From these <sup>fi</sup>gures, we can see that by setting an appropriate association measure one can easily <sup>fi</sup>lter out many uninteresting generalized tuples. Note that since the <sup>fi</sup>ltering was done by post-processing, there was no difference in the run time in this experiment.

## 6. Conclusion

We present an algorithm, the GAOI, for generating all interesting generalized knowledge at one time. The GAOI method is based on the multiple-level mining technique and multiple minimum supports concept. Although it spends a longer time than the classic AOI to derive the generalized knowledge, its advantages lie in that it provides a simple and effective way for knowledge generalization and achieves a more accurate and useful data representation. A real-life dataset is used for experiment and the results show that the proposed method can induce more comprehensive generalized knowledge from relation database.

![](/api/attachments/WP2XKEHW/fulltext/images/c8c7bc92c21827bca5298690f456d28eebe95ca55769a4b6a6bd6be172daec4e.jpg)  
Fig. 16. Number of generalized tuples vs. association measure (from 2 to 9).

![](/api/attachments/WP2XKEHW/fulltext/images/1def133c62451e57fa708dda0d6e92dd18c564c81ab867b362e252114d9641dc.jpg)  
Fig. 1. Concept hierarchies for the car information data.

There are many possible directions for future research. First, the proposed algorithm implicitly assumes that all attributes in the data are of the same nature and assigns the same minimum level support thresholds to each attribute. However, since different attributes may have different distributions in every level, we could attempt to give different minimum level support thresholds for different attributes according to their distributions. Second, it is dif<sup>fi</sup>cult for a user to properly set all threshold values at one time. How to develop an automatic approach, based on some heuristic, structure of trees or data distribution, to set the thresholds is an interesting issue. Third, it is a good idea to have a <sup>fi</sup>ltering mechanism to <sup>fi</sup>lter the output results of generalized tuples that are less interesting than their descendants. Furthermore, since the cover <sup>fi</sup>eld is a data structure that is very space-consuming and only suitable for small-sized relation, an attempt should be made to propose a new data structure which is space-saving and suitable for large-sized relation. Finally, we could extend the usage of background knowledge by using domain generalization graphs rather than concept trees or using fuzzy concept trees rather than crisp concept trees.

## Appendix A

(c) T : Engine Displacement

(d) T : Price

![](/api/attachments/WP2XKEHW/fulltext/images/35a5da53b7d1d3a08f004d2cccec937b94352f3f4f22782890cf42f814ecf7ef.jpg)  
(c) ${ \bf { T } } _ { 3 } { \mathrm { : } }$ Occupation

![](/api/attachments/WP2XKEHW/fulltext/images/3a318c019cfc5411211eb2b3293c0ede25afe5ecacfc8335792b4233369b4f48.jpg)  
Fig. 2. Concept hierarchies for the credit card dataset.

## References

[1] R. Adderley, M. Townsley, J. Bond, Use of data mining techniques to model crime scene investigator performance, Knowledge-Based Systems 20 (2) (2007) 170-176

[2] R. Agrawal, R. Srikant, Fast algorithms for mining association rules, Proceedings of the 20th International Conference on Very Large Data Bases, VLDB, 1994, pp, 487-499.

[3] R.A. Angryk, F.E. Petry, Mining multi-level associations with fuzzy hierarchies, The 14th JEEE International Conference on Fuzzy Systems, FUZZ'05. 2005. pp. 785–790.

[4] T. Beaubouef, F.E. Petry, Attribute-oriented knowledge discovery in rough relational databases, Proceedings of the Twentieth International Florida Arti<sup>fi</sup>cial In telligence Research Society Conference (2007) 507–508.

[5] S. Bhattacharyya, S. Jha, K. Tharakunnel, J.C. Westland, Data mining for credit card fraud: a comparative study, Decision Support Systems (2010), doi:10.1016/j.dss.2010.08.008.

[6] Y. Cai, N. Cercone, J. Han, An attribute-oriented approach for learning classi<sup>fi</sup>cation rules from relational databases, Proceedings of the Sixth International Conference on Data Engineering (1990) 281–288.

[7] C.L. Carter, H.J. Hamilton, Ef<sup>fi</sup>cient attribute-oriented generalization for knowledge discovery from large databases, IEEE Transactions on Knowledge and Data Engineering 10 (2) (1998) 193–208.

[8] Y.-L. Chen, C.-C. Shen, Mining generalized knowledge from ordered data through attribute-oriented induction techniques, European Journal of Operational Re search 166 (1) (2005) 221–245.

[9] M.S. Chen, J. Han, P.S. Yu, Data mining: an overview from a database perspective, JEEE Transactions on Knowledge and Data Engineering 8 (6) (1996) 866–883.

[10] D.W. Cheung, H.Y. Hwang, A.W. Fu, J. Han, Ef<sup>fi</sup>cient rule-based attribute-oriented induction for data mining, Journal of Intelligent Information Systems 15 (2) (2000) 175–200.

[11] Credit card dataset, http://www.im.nanya.edu.tw/yywu2002.

[12] D. Dudek, RMAIN: association rules maintenance without reruns through data, Information Sciences 179 (24) (2009) 4123–4139.

[13] C.C. Fabris, A.A. Freitas, Incorporating deviation-detection functionality into the olap paradigm, Proceedings of the 16th Brazilian Symposium on Databases, 2001, pp. 274–285.

[14] B. Fan, P. Zhang, Spatially enabled customer segmentation using a data classi<sup>fi</sup>cation method with uncertain predicates, Decision Support Systems 47 (4) (2009) 343–353.

[15] L. Geng, H.J. Hamilton, Interestingness measures for data mining: a survey, ACM Computing Surveys 38 (3) (2006) 1–32.

[16] J. Han, Y. Fu, Exploration of the Power of Attribute-oriented Induction in Data Mining, AAAI/MIT Press, Cambridge, Mass., 1996, pp. 399–421.

[17] J. Han, Y. Fu, Mining multiple-level association rules in large databases, IEEE Transactions on Knowledge and Data Engineering 11 (5) (1999) 798–805.

[18] J. Han, M. Kamber, Data Mining: Concepts and Techniques, Morgan Kaufmann, New York, 2006.

[19] J. Han, Y. Cai, N. Cercone, Data-driven discovery of quantitative rules in relational databases, IEEE Transactions on Knowledge and Data Engineering 5 (1) (1993) 29–40.

[20] R.J. Hilderman, H.J. Hamilton, Knowledge Discovery and Measures of Interest Kluwer Academic Publishers. 2001

[21] C.-C. Hsu, Extending attribute-oriented induction algorithm for major values and numeric values, Expert Systems with Applications 27 (2) (2004) 187–202.

[22] X. Hu, N. Cercone, Learning in relational databases: a rough set approach, Computational Intelligence 11 (2) (1995) 323–338.

[23] Y. Hu, Y. Chen, Mining association rules with multiple minimum supports: a new mining algorithm and a support tuning mechanism, Decision Support Systems 42 (1) (2006) 1–24.

[24] E.M. Knorr, R.T. Ng, Extraction of spatial proximity patterns by concept generalization, Second International Conference on Knowledge Discovery and Data Min ing (1996) 347–350.

[25] D.H. Lee, M.H. Kim, Database summarization using fuzzy ISA hierarchies, IEEE Transactions on Systems, Man, and Cybernetics—Part B 27 (1) (1997) 68–78.

[26] S. Li, L. Shue, S. Lee, Enabling customer relationship management in ISP services through mining usage patterns, Expert Systems with Applications 30 (4) (2006) 621–632.

[27] B. Liu, W. Hsu, Y. Ma, Mining association rules with multiple minimum supports, Proceedings of the <sup>fi</sup>fth ACM SIGKDD international conference on Knowledge dis covery and data mining (1999) 337–341.

[28] M.K. Muyeba, J.A. Keane, Extending attribute-oriented induction as a key-preserving data mining method, 3rd European Conference on Principles and Practice of Knowledge Discovery in Databases, 1999, pp. 448–455.

[29] G. Raschia, N. Mouaddib, Saintetiq: a fuzzy set-based approach to database summarization, Fuzzy Sets and Systems 129 (2) (2002) 137–162.

[30] S. Tsumoto, Knowledge discovery in clinical databases and evaluation of discovered knowledge in outpatient clinic, Information Sciences 124 (1–4) (2000) 125–137.

[31] L.Z. Wang, L.H. Zhou, T. Chen, A new method of attribute-oriented spatial generalization, Proceedings of 2004 International Conference on Machine Learning and Cybernetics, 2004, pp. 1393–1398.

[32] Y.C. Yang, Web user behavioral pro<sup>fi</sup>ling for user identi<sup>fi</sup>cation, Decision Support Systems 49 (3) (2010) 261–271.

[33] S.C. Yoon, E.K. Park, An approach to intensional query answering at multiple abstraction levels using data mining approaches, Proceedings of the 32th Hawaii conference on System Sciences, 1999, p. 204.

[34] M.J. Zaki, Scalable algorithms for association mining, IEEE Transactions on Knowledge and Data Engineering 12 (3) (2000) 372–390.

Yen-Liang Chen is a Professor in the Department of Information Management, National Central University, Taiwan. He received his Ph.D. degree in computer science from the National Tsing Hua University, Hsinchu, Taiwan. His current research interests include data mining, information retrieval, knowledge management and decision making models. He has published papers in Decision Support Systems, Information & Management, Electronic Commerce Research & Applications, IEEE Transactions on Software Engineering, IEEE Transactions on Knowledge and Data Engineering, IEEE Transactions on SMC—part A and part B, Information Systems, Operations Research and many others. He is currently the editor-in-chief of the Journal of Information Management.

Yu-Ying Wu is an Assistant Professor in the Department of Information Management, Nanya Institute of Technology, Jhongli, Taiwan. She received her Ph.D. degree in information management from National Central University, Jhongli, Taiwan. Her current research interests include data mining, information retrieval and EC technologies.

Ray-I Chang is an Associate Professor in the Department of Engineering Science and Ocean Engineering, National Taiwan University, Taiwan. He received his Ph.D. degree in computer science from National Chiao Tung University, Hsinchu, Taiwan. His current research interests include data mining, multimedia networking and wireless sen sor networks.
