---
otero_id: 9222
otero_key: "P8WH3JAB"
title: "Change detection model for sequential cause-and-effect relationships"
authors: "Tony Cheng-Kui Huang; Pu-Tai Yang; Jen-Hung Teng"
year: "2018"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2017.11.007"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Change detection model for sequential cause-and-effect relationships

![](/api/attachments/P8WH3JAB/fulltext/images/fb0c4b91a90a9c8f45b9f2aca9db9aec35e40f64ae37ac4405f9c76efff959d4.jpg)

Tony Cheng-Kui Huang<sup>a</sup>, Pu-Tai Yang<sup>b,</sup>\*, Jen-Hung Teng<sup>c</sup>

<sup>a</sup>Department of Business Administration, National Chung Cheng University, Chiayi, Taiwan, ROC

<sup>b</sup>Department of Business Administration, Tunghai University, Taichung, Taiwan, ROC

<sup>c</sup>Department of Information Management, National Chung Cheng University, Chiayi, Taiwan, ROC

## A R T I C L E I N F O

Article history: Received 27 July 2016 Received in revised form 31 October 2017 Accepted 27 November 2017 Available online 5 December 2017

Keywords: Data mining Change mining Classifiable sequential patterns Cause-and-effect relationships Big data

## A B S T R A C T

Detecting changes of behaviors or events is crucial when updating existing knowledge in a dynamic business environment. Currently, data analysts can immediately collect data and easily access existing knowledge. However, that knowledge can also rapidly become outdated. This study discusses a form of knowledge, classifiable sequential patterns (CSPs), defined as s c, where s is a temporal sequence; c is a class label; and “ ” is a sign which implies the sequential relationships between s (cause) and c (effect). If the CSP evolves into another, and the new knowledge is not updated, decision-makers would continue to work with the obsolete CSP. To the authors’ knowledge, no study has addressed the topic of change mining in CSPs. To address this research gap, this study proposes a novel change-mining model, SeqClassChange, to identify changes in CSPs. Experiments were conducted with a real-world dataset to evaluate the proposed model.

© 2018 Elsevier B.V. All rights reserved.

## 1. Introduction

Identifying changes in a series of behaviors or events is crucial for a company to survive in a dynamic and competitive business environment. Especially because of advancements in data storage technology, numerous enterprises have constructed information systems, such as e-commerce systems and gamification-based apps, to serve customers and to simultaneously collect their behavioral data. The speed of data generation is high and existing technology can be used to collect abundant, varied, and instantaneous big data (i.e., data with high volume, velocity, and variety, the 3Vs) [5]. Managers can use these data to instantly achieve frequent and meaningful observations of customer behavior [4], for example, online consumer reviews [26].

Despite acquiring customer behavior data, discovered patterns, and their implied knowledge, managers remained concerned about one paramount question: “Is the current knowledge still valid or already outdated?” Marketers always release new and short-term promotions to promote products or services in today’s competitive market. Thus, customers might rapidly change their preferences because of the influence from advertising or word of mouth from their friends; that is, changes in customer behaviors will always occur [18]. Therefore, managers need to quickly and often identify changes in customer behavior, renew their knowledge, and make timely and accurate responses to the change in order to adapt to the dynamic business environment.

One form of knowledge can be represented as follows: < $( a _ { 1 } ) , \cdots , ( a _ { k } ) , \cdot \cdot \cdot , ( a _ { m } ) >  c ,$ where $a _ { k }$ represents an event (or a customer behavior) at the kth time point; m is the length of the temporal sequence; and c represents the resulting class. Taking a retail behavioral sequence as an example, < (watches)(jewelery)(antiques) > V IP, means that customers belonging to the VIP class have the following sequential behaviors: Purchasing watches occurs before purchasing jewelery, and finally, antique purchasing occurs. This type of sequence is called a classifiable sequential pattern (CSP) because the sequence is connected to a class with an arrow; it reveals the relationships between sequential causes (purchases of watches, jewelery, and antiques) and the effect (the given VIP membership). However, the previous year’s pattern is substituted with < (smartphone)(jewelery)(antiques) > V IP. If a manager cannot recognize the change in a timely manner, he/she will reach an inaccurate conclusion with respect to the current trend: The VIP customers now purchase smart phones as their first priority. Without renewing this knowledge, managers might formulate inappropriate strategies to improve their services or designed promotions.

The primary aim in knowledge discovery and data mining is to use practical tools to discover behavioral patterns. Hence, numerous data-mining techniques have been proposed for producing useful behavioral knowledge in commerce, such as cross-selling in fuzzy time-interval sequential patterns [7], customer profiling [38], product bundling [41], recency, frequency, and monetary (RFM) sequential patterns [8], and role change patterns in social networks [20]. Of the numerous data-mining techniques, CSP mining plays crucial role in assisting managers to identify implied sequential relationships between causes and effects [21].

To the authors’ knowledge, no study has addressed the issue of change mining in CSPs. The contributions of this study can be summarized in three points:

1. This study proposes a novel change mining model, SeqClass-Change, by inheriting the models of Refs. Song et al. [28], Tsai and Shieh [32], Huang [17] and Huang et al. [16], to identify the changes in CSPs at different time periods.

2. This study proposes a CSP similarity computation index (CSCI) to emphasize the cause-and-effect relationships between two CSPs.

3. SeqClassChange uses the CSP definition in Refs. Lesh et al. [21] and Tseng and Lee [36], rather than that of Zhao et al. [43], which uses itemsets instead of items at a single time point. That is, the proposed model allows multiple events (customer behaviors) to occur at each time-point in a CSP, which can help managers to model complex customer behavior.

Based on the above points, managers can identify more complex implications of cause-and-effect relationships and their related changes, and in order to make better decisions. Moreover, a real-world dataset is used to show the model’s effectiveness and usefulness.

The remainder of this paper is organized as follows. Section 2 reviews related works including change mining and sequence-based classifications. Section 3 defines the SeqClassChange model for mining changes in CSPs. Section 4 provides the experimental results of the proposed model. Section 5 offers the conclusions.

## 2. Related work

Before the model for mining changes in CSPs is presented later in this paper, this section provides some basic research background. The information is separated into two different but correlated parts, namely change mining and sequence classifications, which are discussed in Sections 2.1 and 2.2, respectively. Finally, a fully integrated discussion is provided in Section 2.3.

## 2.1. Change mining

The core of the change mining problem is the association rule mining problem. The Apriori algorithm [1] was the original algorithm used to solve the association rule mining problem. It executes a number of iterations and the nth iteration can generate a set of n-length frequent patterns. The key to the Apriori algorithm is its generate-and-test (candidate generation and pruning) strategy. The new candidate itemsets in the current iteration are generated from the frequent itemsets in the previous iteration. Subsequently, the sequential version of the Apriori algorithm is also proposed in GSP [29].

Previous works have investigated change mining using two types of approaches: The maintenance approaches and the comparison approaches. The maintenance approaches adjust discovered patterns when new data, new transactions, or new customers are added to an original database, which improves the accuracy of the patterns in a dynamic environment [9,11,25]. This type of approach maintains existing knowledge but does not provide any extra information; that is, it cannot reveal the evolutionary process when customer behavior changes; therefore, a second type of approach has been proposed: the comparison approaches.

The comparison approaches recognize changes between different databases or within the same database at distinct time periods.

The first study of change mining was conducted by Liu et al. [23]. The study stemmed from the post-analysis of learned rules [22], which devised an approach of change mining in the context of decision trees for six identifying behavioral changes of customers. Song et al. [28] developed an overall architecture including three phases that detects changes of customer behavior in association rules from databases. They investigated possible types of change on the basis of previous research, and summarized three types of change: (1) emerging patterns, (2) unexpected changes, and (3) added/perished rules. They then used similarity and difference measures to identify the changed rules and to rank them according to the degree of change. Chen et al. [6] integrated customer behavioral variables (recency, frequency, and monetary), demographic variables, and transaction databases to propose a method of mining changes in customer behavior. They also followed the definitions of the three types of change proposed in Song et al. [28] to identify change patterns. In addition, Bala [3] contended that the work by Chen et al. [6] did not consider products in the conditional part of a pattern depicted by association rules. Therefore, he proposed a change-mining approach, in which the conditional part may contain products or items. In terms of other types of technique in the comparison approaches, Au and Chan [2] introduced a fuzzy technique to identify association rules over time and generalized the problem so that different fuzzy data-mining techniques could be used to address the issue of change.

To identify changes in sequential patterns, Tsai and Shieh [32], using the architecture in Song et al. [28], first proposed a change detection framework to observe the dynamic alternation of sequential patterns between two time-periods and divided them into three significant types of change patterns, based on those in Song et al. [28]. Regarding discerning changes in fuzzy-based sequential patterns, MineFuzzChange [17] was the first change-mining model that discussed the change of customer behavior in fuzzy time-interval sequential patterns. Subsequently, a novel change mining model for detecting change in another type of sequential pattern, fuzzy quantitative sequential patterns [16], was proposed.

There is another issue which is similar to the idea of change mining, called concept drift [12,37]<sup>1</sup>. However, the major concern of concept drift is to discuss the change of a predictive model in the conditional distribution of the output (i.e. target variable) given the input (input features). Specially, the distribution of the input may stay unchanged. Therefore, the past studies have proposed various adaptive learning algorithms for handling the issue. Since the traditional change mining does not concern on the distribution of the input or the output, this study will not address the issue of concept drift in advance.

## 2.2. Sequence classifications

Sequence classification, a sequence learning category [30], is used to determine whether a sequence is legitimate or is assigning class labels to new sequences. Previous studies have proposed different approaches to resolving the problems involved in sequence classifications, including decision trees, artificial neural networks, naive Bayes, k-nearest neighbors, the hidden Markov model, and support vector machines [15]. The investigation of sequence classification can be applied to numerous real-life circumstances such as protein function prediction [13], earthquake or typhoon prediction, text classification [39], debt detection in social security [43], and the class label prediction of new customers from temporal customer data [31].

The above approaches are algorithmic, statistical, or bionic methods. However, there is another branch of sequence classification: the pattern-based methods, which follow the generate-andtest (candidate generation and pruning) strategy [15], inspired by association rules mining [1,29]. Liu et al. [24] first integrated classification and association rule mining and created a special type of association rules, called class association rules (CARs). The primary idea of CARs is that the right-hand side of a sequence is attached to a class label as its consequence. The authors also proposed an algorithm, CBA (classification based on association), which uses Apriori [29] as a rule generator and develops a classifier builder to identify all CARs. The CBA can then harness the relationships between sequences and their classes.

After the CBA algorithm, Lesh et al. [21] presented the FeatureMine algorithm, converting mined patterns in each class into a Boolean features table, and feeding it into a classification algorithm. It uses SPADE [42], a tree-based algorithm for mining frequent sequences, for the rapid discovery of sequential patterns. Tseng and Lee [35] proposed a classify-by-sequence (CBS) algorithm to classify time-series datasets. The goal of the CBS algorithm is to reveal the CSP rules that can be used to construct the classifier. The main methodology of CBS is to integrate sequential pattern mining with probabilistic induction. Thus, patterns can be extracted eficiently and the classification work can be more easily completed. Adopting the core idea of CBS, Tseng and Lee [35] presented two approaches, CBS\_ALL and CBS\_CLASS; the former uses the traditional algorithm for mining sequential patterns on the whole dataset, whereas the latter acts on the several divided sub-datasets according to their classes. Experimental results showed that CBS\_CLASS outperforms both CBS\_ALL and FeatureMine. Tseng and Lee [36] extended the original CBS, improved CBS\_CLASS by removing the patterns found in all classes, and proposed a new score function in its classifier builder algorithm. In addition, a recent study [31] added a new consideration, namely time-interval, for mining time-interval sequence classification patterns.

## 2.3. Discussion

In traditional sequence classification problems, the related classes of sequences are categorized using specific algorithms, and the main goodness-of-fit metric used in evaluating their associated algorithms is their prediction accuracy, not the implied managerial cause-andeffect relationships among sequences. By contrast, traditional change mining problems only identify changes in itemsets or sequences; they do not consider CSPs, which contain valuable information such as implications of cause-and-effect relationships.

Basically, the problem addressed in this study is a change mining problem and is addressed using the comparison approaches. According to the above discussion, Song et al. [28] integrated the types of changes from the previous studies and devised the change detection framework for customer behavior. Tsai and Shieh [32] modified it for sequential patterns. Although Huang [17] and Huang et al. [16] included additional considerations to identify changes in fuzzybased sequential patterns, their work did not discuss the sequence classifications. Accordingly, this study inherits the change-mining models in Refs. Song et al. [28], Tsai and Shieh [32], Huang [17] and Huang et al. [16] and proposes a novel integrated model for change detection in CSPs. To the authors’ knowledge, no previous study has used the comparison approaches in change mining to address changes in relation to CSPs.

Moreover, this study uses the CSP definition given by Refs. Lesh et al. [21] and Tseng and Lee [36], a more general form than that used by Zhao et al. [43], which uses itemsets instead of items at a single time point. For example, the CSP form used by Zhao et al. [43] $\mathrm { i } s < ( a ) ( b ) ( d ) > $ c; by contrast, the CSP form in this study and that used by Lesh et al. $[ 2 1 ] { \mathrm { i } } { \mathrm { s } } < ( a e ) ( b f ) ( d ) >  c .$ To authors’ knowledge, no change mining model adopts this kind of CSP form, which can help managers model complex customer behavior.

In summary, for academic contributions, this study addresses the research gap by proposing a model for change mining in CSPs.

For practical applications, the change mining in CSPs can provide valuable suggestions for management.

## 3. Proposed change detection model: SeqClassChange

This section describes the novel model proposed in this study, SeqClassChange, for detecting changes in implied sequential causeand-effect behaviors in CSPs at different time periods. The SeqClass-Change model can be separated into three phases: (1) CSP generation, (2) change type detection, and (3) significant change evaluation. Section 3.1 briefly introduces the concepts of CSPs, and provides an overview of the SeqClassChange model. Sections 3.2 to 3.4 respectively present the details of the three phases of the SeqClassChange model.

## 3.1. Overview of the SeqClassChange model

Definition 1 (Temporal sequences). A temporal sequence (hereafter sequence<sup>2</sup>), s, consists of itemsets, defined $\mathsf { a s } < I S _ { 1 } , \cdot \cdot \cdot , I S _ { k } , \cdot \cdot \cdot , I S _ { m } >$ where $I S _ { k }$ is the kth itemset and m is the number of itemsets in s, also called the length of the sequence. Items in an itemset are alphabetically ordered by item name. For simplification, an item only occurs once in an itemset, but can occur multiple times in distinct itemsets in a sequence. Let $S ^ { t }$ and $S ^ { t + l }$ be two sequence databases at two separate time-periods t and $t { + } l$ , respectively, where $S ^ { t } \cap S ^ { t + l } = \emptyset .$ □

Definition 2 (Classifiable sequential patterns). A classifiable sequential pattern (CSP) is defined as $c s p = s  c ,$ where s is a temporal sequence and $c \in C$ is a class label. The class label of s can be obtained using by certain algorithms or functions. $C S P ^ { t }$ and $C S P ^ { t + l }$ represent the sets of CSPs identified from $S ^ { t }$ and $S ^ { t + l } . c s p _ { i } ^ { t } ( c s p _ { i } ^ { t + l } )$ represents the ith (jth) CSP in $C S P ^ { t } \left( C S P ^ { t + l } \right)$ , where $i ( j )$ is the pattern index in $C S P ^ { t }$ $( C S P ^ { t + l } ) , i = 1 , 2 , \cdot \cdot \cdot , | C S P ^ { t } | \ ( j = 1 , 2 , \cdot \cdot , | C S P ^ { t + l } | ) ; | C S P ^ { t } | \ ( | C S P ^ { t + l } | )$ is the number of patterns in $\bar { C S P ^ { t } } ( C S P ^ { t + l } ) ^ { 3 } . $ □

Example 1. For example, $c s p = < ( a ) ( b c ) ( d ) > $ churn means that customers belonging to the churn class have the following sequential signs: (1) behavior a appearing first; (2) b and c acting simultaneously; (3) and then d acting. The items can also be replaced by events or behaviors. For example, a is (frequent complaints); b and c are (low logging) and (low staying), respectively; and d is (low purchases). That is, this CSP provides the following message: customers belonging to the churn class will complain frequently at the beginning; then their time and frequency of online shopping site use will decrease; finally, they will no longer make purchase from the online shopping site.

The flow chart of the proposed change detection model is presented in Fig. 1. The first phase is CSP generation. Because the CBS algorithm [35] performs more favorably than do other algorithms, this study adopted it as the fundamental algorithm to identify the two sets of CSPs from $S ^ { t }$ and $S ^ { t + l }$ . In the second phase, given any pair of CSPs at $C S P ^ { t }$ and $C S P ^ { t + l }$ , they can be compared by measuring their similarity $^ { [ 2 8 , 3 2 ] }$ . Using the similarity, the change type of a pair of $( c s p _ { i } ^ { t } , c s p _ { i } ^ { t + \bar { l } } )$ can be identified. For example, one pattern at a later time period $t + l \mathrm { c a n }$ be said to have evolved from another pattern at an earlier time period t if their patterns have high similarity (compared to the other pairs of patterns). In the third phase, to avoid the numerous identified change patterns, this study uses the threshold mechanism used by Refs. Song et al. [28] and Tsai and Shieh [32] to evaluate the significance of the change patterns. Only when the significance of change patterns is higher than a threshold, will they be reported to system users or decision-makers.

![](/api/attachments/P8WH3JAB/fulltext/images/269a1c4e10d9b4915d4c04b5ac9fcf9f4ea3a05a80c6efde7002672a1a2aaeeb.jpg)  
Fig. 1. Flow chart of the SeqClassChange model.

The idea of Fig. 1 is mostly inspired by the studies of Song et al. [28] and Tsai and Shieh [32], whose models for change mining both consist of three phases, (1) rule/pattern generation, (2) rule/pattern matching and change type detection, and (3) significant change evaluation. One obvious difference among Refs. Song et al. [28] and Tsai and Shieh [32] and ours is the detection for different types of rules/patterns, i.e. association rules, sequential patterns, and CSPs.

## 3.2. Phase one: CSP generation

The purpose of Phase one is to identify two sets of CSPs $( C S P ^ { t }$ and $C S \dot { P } ^ { t + l } )$ from two original temporal sequence datasets $( S ^ { t }$ and $S ^ { t + l }$ , respectively). This study selected the concept of the CBS algorithm [35,36] as the CSP mining method and modified the CBS algorithm to adapt the data structure. The mining process can be described in two phases as follows.

The first phase of CBS is to mine CSPs. In the beginning, an original database is transferred to a sequence database (see Fig. 2). The events at different time points are arranged chronologically and abstractly summarized as a temporal sequence (this data pre-processing procedure is explained in Section 4.1 with real-dataset examples). Then, frequent patterns are generated using the following two variations of CBS algorithms: CBS\_CLASS and CBS\_ALL.

1. CBS\_CLASS: With CBS\_CLASS, the whole dataset is divided into sub-datasets according to their classes (see the upper part of Fig. 2). All sequences of each sub-dataset have the same class, and the CBS\_CLASS method then applies GSP algorithms [29] to identify the frequent patterns from each sub-dataset individually. For each class, CBS\_CLASS uses different minimum thresholds, respectively. This study uses the generate-and-test strategy [15] to generate all candidate sequences as Tseng and Lee [35] did; Tseng and Lee [36] used tree extension. Subsequently, each frequent pattern is assigned its corresponding class as its right-hand side label (effect). Finally, the complete set of CSPs with different classes can be obtained by joining all sets of CSPs with different classes.

2. CBS\_ALL: This algorithm does not use class sub-datasets (see the lower part of Fig. 2). Instead, CBS\_ALL considers the transaction support and the class support at the same time. In CBS\_ALL, each mined candidate CSP is assigned a class\_sup array. If the candidate CSP is contained in a sequence s with the class label $c ,$ then its class\_sup[x] will be incremented. A candidate CSP can be reserved to the next stage if its transaction support is more than a user-defined threshold and at least one class support is larger than the minimum class support threshold.

CBS\_ALL is equal to the confidence-based Apriori algorithm used in Song et al. [28]. For example, the confidence of $\begin{array} { r } { s _ { 1 } = \frac { \sigma ( s _ { 1 } \cup c _ { 1 } ) } { \sigma ( s _ { 1 } ) } = } \end{array}$ $\frac { 0 . 2 1 } { 0 . 3 5 } \ = \ 0 . 6$ (in the lower part of Fig. 2). The only difference is that CBS\_ALL uses the support values, while the confidence-based Apriori algorithm uses the percentages of the support values to generate CSPs. That is, CBS\_ALL can be seen as the performance from previous research [21,24,28]. Section 4 examines the effects of these two CBS methods, separately.

## 3.3. Phase two: change type detection

Phase two is designed to screen out CSPs of different types from two distinct databases according to their similarities. Similarity is first defined to understand the closeness of the two sequences [16,17].

In the following definitions, the following terminologies are used: Given csp<sup>t</sup> $\in C S P ^ { t }$ and $c s p _ { j } ^ { t + l } , c s p _ { j ^ { \prime } } ^ { t + l } \in C S P ^ { t + l } ;$ c are their classes.

$$
\begin{array}{l} c s p _ {i} ^ {t} = <   I S _ {1} ^ {t}, \dots , I S _ {x} ^ {t}, \dots , I S _ {m} ^ {t} > \to c \in C S P ^ {t}, \\ c s p _ {j} ^ {t + l} = <   I S _ {1} ^ {t + l}, \dots , I S _ {y} ^ {t + l}, \dots , I S _ {n} ^ {t + l} > \to c \in C S P ^ {t + l} \\ c s p _ {j ^ {\prime}} ^ {t + l} = <   I S _ {1} ^ {t + l}, \dots , I S _ {y ^ {\prime}} ^ {t + l}, \dots I S _ {n ^ {\prime}} ^ {t + l} > \to c \in C S P ^ {t + l}, \end{array}
$$

where $m , n , n ^ { \prime } \geq 2$ are the lengths of $c s p _ { i } ^ { t } , c s p _ { j } ^ { t + l } ,$ , and $c s p _ { j ^ { \prime } } ^ { t + l }$ , respectively; $x , y , y ^ { \prime }$ are the itemset indexes in $c s p _ { i } ^ { t } , \ c s p _ { j } ^ { t + l }$ , and $c s p _ { j ^ { \prime } } ^ { t + l } ,$ respectively. Subsequently, several examples are used to develop the definition of pattern similarity.

First, it is claimed that the higher the proportion of matching itemsets is in two patterns, the more closely related the two patterns are.

Example 2. Suppose csp<sup>t</sup> $= < ( a ) ( b c ) ( d ) >  V I P { \in } C S P ^ { t } , c s p _ { i } ^ { t + l } = <$ $( a ) ( b c ) ( d ) ( e f g ) >  V I P$ and $c s p _ { i ^ { \prime } } ^ { t + l } = < ( a ) ( b c ) >  V I P { \in } \bar { S ^ { t + l } }$ . The similarity between csp<sup>t</sup> and $c s p _ { j } ^ { t + l }$ is larger than that between csp<sup>t</sup> and $c s p _ { j ^ { \prime } } ^ { t + l }$ for the following reasons:

1 For csp<sup>t</sup> and $c s p _ { i } ^ { t + l } , I S _ { 1 } ^ { t } = I S _ { 1 } ^ { t + l } , I S _ { 2 } ^ { t } = I S _ { 2 } ^ { t + l } ,$ , and $I S _ { 3 } ^ { t } = I S _ { 3 } ^ { t + l }$ so that the number of matching itemsets is three.

2 For $c s p _ { i } ^ { t }$ and $c s p _ { i ^ { \prime } } ^ { t + l } , I S _ { 1 } ^ { t } = \bar { I } S _ { 1 } ^ { t + l }$ and $I S _ { 2 } ^ { t } ~ = ~ I S _ { 2 } ^ { t + l }$ , so that the number of matching itemsets is two.

3 For $c s p _ { i } ^ { t } , 3 > 2$ which shows tha $c s p _ { j } ^ { t + l }$ is a more closely related pattern to it. -

![](/api/attachments/P8WH3JAB/fulltext/images/0de98fdee6d12e7cd44a8b953c5ff465e8a8a9001e95fcc214f366c29770b485.jpg)  
Fig. 2. How the CBS algorithm transfers a temporal database into a set of CSPs.

Although the number of matching itemsets is the major consideration in computing the similarity between two CSPs, the number of matching items within itemsets is also crucial.

Example 3. Given csp<sup>t</sup> $= < ( a ) ( b c d e ) ( f ) >  V I P \in C S P ^ { t } , c s p _ { i } ^ { t + l } = <$ $( a ) ( b c d ) ( f ) >  V I P \in C S P ^ { t + l }$ , and $c s p _ { i } ^ { t + l } = < ( a ) ( d e ) ( f ) > \stackrel { , } {  } V I P \in$ $C S P ^ { t + l }$ , we consider that the similarity between csp<sup>t</sup> and $c s p _ { j } ^ { t + l }$ is larger than that between $c s p _ { i } ^ { t }$ and $c s p _ { j } ^ { t + l }$ , because of the following:

1 To the two pairs, the numbers of matching itemsets are the same (i.e., two. $I S _ { 1 } ^ { t } = I S _ { 1 } ^ { t + l } = I S _ { 1 } ^ { t + l } , I S _ { 3 } ^ { t } = I S _ { 3 } ^ { t + l } = I S _ { 3 } ^ { t + l } )$

2 The key point is that the similarity of the second paired itemsets between scp<sup>t</sup> and $s c p _ { i } ^ { t + l }$ ((bcde) and (bcd)) is greater than that between scp<sup>t</sup> and $s c p _ { j ^ { \prime } } ^ { t + l } ( ( b c d e ) \mathrm { a n d } ( d e ) ) .$ -

Subsequently, a definition is developed to measure the similarity of two itemsets in the same order in two CSPs.

Definition 3 (Similarity degree). The similarity degree (SD) is used to measure the matching degree of two itemsets in two distinct CSPs.

$$
S D _ {i j k} = \frac {\text { NumOfMatchingItems } \left(I S _ {i k} ^ {t} , I S _ {j k} ^ {t + l}\right)}{\max \left(\left| I S _ {i k} ^ {t} \right| , \left| I S _ {j k} ^ {t + l} \right|\right)},\tag{1}
$$

where $S D _ { i j k }$ is the similarity degree between the kth itemset in csp<sup>t</sup> and the kth itemset in $\mathrm { \bar { { c s p } } } _ { j } ^ { t + { \bar { l } } } ; \ \left| I S _ { i k } ^ { t } \right| \left( \left| I S _ { j k } ^ { t + l } \right| \right)$ is the number of items in the kth itemset of pattern $c s p _ { i } ^ { t } c \left( s p _ { j } ^ { t + l } \right)$ . max() is a maximum operator that selects the maximal number in the parentheses. NumOfMatchingItems() is the number of matching items in the kth itemsets of csp<sup>t</sup> and $c s p _ { j } ^ { t + l }$ □

The design of Definition 3 considers the issue of normalization, which divides the number of matching items into the maximal length of the two itemsets; that is, it adjusts the range of the SD of two itemsets between zero and one in case the lengths of the two itemsets are different. Next, a CSP similarity computation index (CSCI) is developed to calculate the similarity degree between two CSPs.

Definition 4 (CSP similarity computation index, CSCI). The CSCI is described as follows.

$$
C S C I _ {i j} = \frac {\sum_ {k = 1} ^ {n} \frac {n - k + 1}{n} \times S D _ {i j k}}{\sum_ {k = 1} ^ {n} \frac {n - k + 1}{n}},\tag{2}
$$

where CSCI is an index, which measures the similarity between $c s p _ { i } ^ { t }$ and $c s p _ { i } ^ { t + l } . S D _ { i j k }$ is the similarity degree of the kth itemsets between $c s p _ { i } ^ { t }$ and $c s p _ { j } ^ { t + l } ,$ , as defined in Definition 3. n is the maximal number of itemsets with respect to $c s p _ { i } ^ { t }$ and $c s p _ { i } ^ { t + l } . \ \frac { n - k + 1 } { n }$ is the weights assigned for the kth itemset. As a result, the value of the CSCI ranges from 0 to 1; 0 means that the pattern structures of csp<sup>t</sup> and $c s p _ { j } ^ { t + l }$ are completely different and 1 means that they are identical. □

Example 4. Given $c s p _ { 1 } ^ { t } = < ( a ) ( b c d e ) ( f g ) > $ VIP and $c s p _ { 1 } ^ { t + l } = <$ $( a ) ( b c d e ) ( f g ) >  V I P ,$ the SD calculations are $\begin{array} { r } { S D _ { 1 1 1 } = \frac { 1 } { \operatorname* { m a x } ( 1 , 1 ) } = 1 } \end{array}$ $\begin{array} { r } { S D _ { 1 1 2 } \ = \ \frac { 4 } { \operatorname* { m a x } ( 4 , 4 ) } \ = \ 1 } \end{array}$ , and $\begin{array} { r } { S D _ { 1 1 3 } \ = \ \frac { 2 } { \mathrm { m a x } ( 2 , 2 ) } \ = \ 1 } \end{array}$ . Because the itemset numbers of the two CSPs are both three, the maximal number between them, n, is also three. Their corresponding weights are $\textstyle { \frac { 3 - 1 + 1 } { 3 } } = 1 , { \frac { 3 - 2 + 1 } { 3 } } = { \frac { 2 } { 3 } } , { \mathrm { a n d ~ } } { \frac { 3 - 3 + 1 } { 3 } } = { \frac { 1 } { 3 } }$ , respectively. These assigned linear weights imply that more attention is given to the beginning causes and that their degrees of importance decrease in a linear order. Then, the $C S C I _ { 1 1 }$ is calculated as follows:

$$
C S C I _ {1 1} = \frac {\frac {3}{3} \times 1 + \frac {2}{3} \times 1 + \frac {1}{3} \times 1}{\frac {3}{3} + \frac {2}{3} + \frac {1}{3}} = 1.
$$

For any two identical patterns, the CSCI calculation always gives one. If given the second CSP at time $t + l , c s p _ { 2 } ^ { t + l } = < ( a ) ( \bar { d e } ) ( \bar { f } ) ( g ) > $ $V I P ,$ we calculate $C S C I _ { 1 2 }$ as follows: n is ma $\times ( 3 , 4 ) \ = \ 4 ; \ S D _ { 1 2 1 } \ =$ $\begin{array} { r } { \frac { 1 } { \operatorname* { m a x } _ { 0 } ^ { } 1 , 1 ) } = \underset { 0 } { 1 } { 1 } , S D _ { 1 2 2 } = \frac { 2 } { \operatorname* { m a x } ( 4 , 2 ) } = \frac { 1 } { 2 } , S D _ { 1 2 3 } = \frac { 1 } { \operatorname* { m a x } ( 2 , 1 ) } = \frac { 1 } { 2 } S D _ { 1 2 4 } = } \end{array}$ $\begin{array} { r } { \frac { \partial } { \operatorname* { m a x } ( 0 , 1 ) } = \frac { 0 } { 1 } = 0 . } \end{array}$

$$
C S C I _ {1 2} = \frac {\frac {4}{4} \times 1 + \frac {3}{4} \times \frac {1}{2} + \frac {2}{4} \times \frac {1}{2} + \frac {1}{4} \times 0}{\frac {4}{4} + \frac {3}{4} + \frac {2}{4} + \frac {1}{4}} = 0. 6 5.
$$

Apparently, to $c s p _ { 1 } ^ { t } , \ c s p _ { 1 } ^ { t + l }$ is a more similar pattern compared to $c s \bar { p } _ { 2 } ^ { t + l } ( 1 > 0 . 6 5 )$ A

The SD and CSCI metrics used in this study are taken from the SD and SSCI metrics presented in Refs. Huang [17] and Huang et al. [16]. The reason these definitions are used is that, in the aforementioned definition, the SD of the kth pair of itemsets is assigned a linear weight, and the weights decrease in time order. The assumption behind this linear weight is dependent on the earlier causes being able to influence the later causes, such as $( I S _ { 1 }  I S _ { 2 }  I S _ { 3 } . . . ) .$ . As a result, it is considered that the earlier causes are more important than the later ones in a cause-and-effect detection model. To the best of authors’ knowledge, no studies have used the CSCI to compute the similarity in relation to a cause-and-effect model.

Next, this study follows Refs. Song et al. [28], Tsai and Shieh [32], Huang [17] and Huang et al. [16] to classify the change patterns into three types: (1)emerging patterns, (2)unexpected changes and (3)added/perished patterns. The definitions of the three types of change patterns are slightly modified from those of the previous studies; however, this study has to consider the condition of the right-hand side (class labels). In addition, since the rationale of significant change evaluation (Phase three) is well designed by Refs. Song et al. [28], Tsai and Shieh [32], Huang [17] and Huang et al. [16], this study refers to their evaluated formulas and slightly modifies them (presented in Section 3.4).

## 3.3.1. Emerging patterns

An emerging pattern refers to a pattern whose support increases significantly over time [10,28]. Because “increasing significantly” is a subjective idea, a minimum difference of supports, min\_diff, is defined to measure the difference of supports by using users’ viewpoints. That is, the same pattern grows significantly more than a given threshold value. In real-world markets, the change trend indicates that a customer behavior is “emerging” (rising) and managers should pay attention to the trend for actions.

Definition 5 (Emerging patterns, EP). If csp<sup>t</sup> and $c s p _ { i } ^ { t + l }$ are completely the same pattern (i.e., $\begin{array} { r l r } { C S C I _ { i j } } & { { } \stackrel { \cdot } { = } } & { 1 } \end{array}$ and their classes are the same) and their supports significantly differ $\left( \operatorname* { s u p } \left( c s p _ { j } ^ { t + l } \right) - s \operatorname* { u p } \left( c s p _ { i } ^ { \dot { t } } \right) \geq \operatorname* { m i n } _ { - } d i f f \right)$ , the $c s p _ { i } ^ { t } \big ( c s p _ { j } ^ { t + l } \big )$ would be classified as a pair of emerging patterns, where sup csp<sup>t</sup> and sup $\left( c s p _ { j } ^ { t + l } \right)$ are the support values of csp<sup>t</sup> and $c s p _ { j } ^ { t + l }$ , respectively.

## 3.3.2. Unexpected change patterns

In real-life situations, managers always hope to predict consumer behaviors, which often tend to change rapidly and unpredictably. However, an unexpected change event could cause managers to misinterpret consumer preferences, derive inaccurate conclusions, and finally respond in an inappropriate way. To address this issue, unexpected changes must be identified from time-varying databases. In the proposed model, two kinds of unexpected change patterns are defined: slightly and totally unexpected change patterns<sup>4</sup>.

In this study, a slightly unexpected change pattern (SUCP), derived from Refs. Tsai and Shieh [32], Huang [17] and Huang et al. [16], refers to a pattern $( c s \bar { p } ^ { t + \bar { l } } )$ existing in the current database(S<sup>t+l</sup>), but is beyond managers’ original beliefs or a priori perceptions (csp<sup>t</sup> from the previous database, S<sup>t</sup>). If a past pattern csp<sup>t</sup> evolves into a slightly different csp<sup>t+l</sup>, it would be beyond managers’ understanding because their inherent impression of the past patterns (csp<sup>t</sup>) remains. As a result, unexpected change patterns are defined as “all current patterns that are similar to past patterns, but not exactly the same.” However, similarity is a subjective idea and its meaning changes with different people. A pattern-matching threshold (PMT), a user-defined threshold, is used to decide whether two CSPs are similar to each other. If the CSCI of a CSP pair exceeds the PMT, then they are recognized as a pair of similar patterns. Users can adjust the value of the PMT according to their viewpoints. The definition of slightly unexpected change patterns is as follows.

Definition 6 (Slightly unexpected change patterns, SUCP). $C S P ^ { * , t + l }$ is defined as a set of slightly unexpected change patterns with respect to csp<sup>t</sup> if

$$
\begin{array}{l} C S P ^ {*}, t + l = \left\{c s p _ {j} ^ {t + l} \mid \left(C S C I _ {i j} \geq P M T\right) \cap \left(C S C I _ {i j} \neq 1\right) \right\}. j = 1, 2, \dots , \left| C S P ^ {t + l} \right|, \\ \text {Class} \left(c s p _ {i} ^ {t}\right) = \text {Class} \left(c s p _ {j} ^ {t + l}\right). \end{array} \tag {3}
$$

First, for csp<sup>t</sup>, every $c s p _ { i } ^ { t + l } \in C S P ^ { t + l }$ is scanned to calculate their CSCI values. If the CSCI value of a $\mathsf { C S P }$ pair is greater than or equal to the PMT, then the CSP pair is recognized as a similar pair. Second, the similar CSP pairs are determined to be unexpected changes if their CSCI values are not equal to one. For example, a past pattern, < (watches)(jewelery)(antiques) > V IP, evolves into a current pattern $c s p ^ { t + l } , <$ (smartphone)(jewelery)(antiques) > V IP. These two CSPs are not equal (CSCI is not equal to 1), but they are very similar. When a manager perceives this change, he/she will feel surprise and unexpected because the discovered pattern $c s p ^ { t + l }$ is a “déjà-vu” (paramnésie) to his/her previous experience $( c s p ^ { t } )$ , but they are still different.

On the other hand, a csp<sup>t</sup> and a $c s p ^ { t + l }$ may be very similar, but cause a totally different effect (i.e., different classes). For example, a past pattern, < (watches)(jewelery)(antiques) > V IP, evolves into a current pattern $c s p ^ { t + l } , <$ (smartphone)(jewelery)(antiques) > NV IP. When a manager perceives this change, he/she may wonder why the similar process leads to a different outcome. In the next, we define the second unexpected change patterns.

Definition 7 (Totally unexpected change patterns). $C S P ^ { * , t + l }$ is defined as a set of totally unexpected change patterns (TUCP) with respect to csp<sup>t</sup> if

$$
\begin{array}{l} C S P ^ {*, t + l} = \left\{c s p _ {j} ^ {t + l} \Big | (C S C I _ {i j} \geq P M T) \right\}, j = 1, 2, \dots , \left| C S P ^ {t + l} \right|, \\ C l a s s \left(c s p _ {i} ^ {t}\right) \neq C l a s s \left(c s p _ {j} ^ {t + l}\right). \end{array}\tag{4}
$$

□

## 3.3.3. Added/perished patterns

The other variations are patterns that are found in the present database, but not in the past database; they are called added patterns (AP) [19,28]. The value of such patterns is new information, where the pattern structure is unlike any pattern in the past database. In contrast to added patterns, perished patterns (PP) are patterns that are found in the past database but that have disappeared from the current database. Added and perished patterns both exhibit completely different pattern structures and provide managers with novel insights related to the market such as which trends are new or disappearing. The added/perished patterns are defined as follows.

Definition 8 (Added/perished patterns). $c s p _ { i } ^ { t + l }$ is defined as an added pattern if all $c s p _ { i } ^ { t } \in C S P ^ { t }$ are not similar to $c s p _ { j } ^ { t + l }$ in the same class. That is, $c s p _ { j } ^ { t + l }$ is an added pattern if

$$
P M T > \max C S C I _ {j} = \max \left(C S C I _ {1 j}, C S C I _ {2 j}, \dots , C S C I _ {| C S P ^ {t} | j}\right).\tag{5}
$$

In contrast to an added pattern, csp<sup>t</sup> is defined as a perished pattern if all $c s p _ { i } ^ { t + l } \in C S P ^ { t + l }$ are not similar to csp<sup>t</sup> in the same class. That is, csp<sup>t</sup> is a perished pattern if

$$
P M T > \max C S C I _ {i} = \max \left(C S C I _ {i 1}, C S C I _ {i 2}, \dots , C S C I _ {i | C S P ^ {t + l} |}\right).\tag{6}
$$

□

The relationships among the PMT and the three types of change patterns are summarized in Fig. 3. The idea to portray the relationships among the three types of change patterns stems from the studies of Refs. Song et al. [28] and Tsai and Shieh [32]. A complete example, provided in Example $5 ,$ shows the change type detection procedures of the SeqClassChange model.

![](/api/attachments/P8WH3JAB/fulltext/images/b74f3d11e4d518ce3c81485769153f6104be022cd5d69575a916db6f780355a4.jpg)  
Fig. 3. Relationships of the three types of change patterns

Example 5. Given two sets of CSPs identified from time-periods t and $t + l , C S P ^ { t }$ and $C S P ^ { t + l } ,$ , in the following table, there are four CSPs in $C S P ^ { t }$ and five CSPs in $C S P ^ { t + l }$ . In this example, there are only two classes: V IP and NV IP; NV IP indicates that the customer is not qualified as a VIP. In this example, min\_diff and PMT are set as 0.03 and 0.3, respectively.

<table><tr><td>Time-period</td><td>Pattern set</td><td>Classifiable Sequential Patterns</td><td>Support</td></tr><tr><td rowspan="4"> $t$ </td><td rowspan="4"> $CSP^{t}$ </td><td> $csp_{1}^{t} = < (a)(bcde)(fg) > \rightarrow VIP$ </td><td>0.04</td></tr><tr><td> $csp_{2}^{t} = < (a)(b)(c) > \rightarrow VIP$ </td><td>0.05</td></tr><tr><td> $csp_{3}^{t} = < (a)(bc)(def) > \rightarrow NVIP$ </td><td>0.07</td></tr><tr><td> $csp_{4}^{t} = < (c)(d)(g) > \rightarrow NVIP$ </td><td>0.1</td></tr><tr><td rowspan="5"> $t + l$ </td><td rowspan="5"> $CSP^{t+l}$ </td><td> $csp_{1}^{t+l} = < (a)(bcde)(fg) > \rightarrow VIP$ </td><td>0.08</td></tr><tr><td> $csp_{2}^{t+l} = < (a)(de)(f)(g) > \rightarrow VIP$ </td><td>0.06</td></tr><tr><td> $csp_{3}^{t+l} = < (a)(bc)(de)(f) > \rightarrow NVIP$ </td><td>0.08</td></tr><tr><td> $csp_{4}^{t+l} = < (ab)(cd)(ef) > \rightarrow NVIP$ </td><td>0.15</td></tr><tr><td> $csp_{5}^{t+l} = < (b)(f)(g) > \rightarrow VIP$ </td><td>0.05</td></tr></table>

The first step is to calculate all corresponding $C S C I _ { i j }$ and class Boolean values, which are shown in the following two tables. The numbers in the cells refer to the $C S C I _ { i j }$ values in the first table. In the second Boolean table, one refers to the same classes and zero refers to the different classes. Several examples of different pattern types are demonstrated.

<table><tr><td> $CSCI_{ij}$ </td><td> $csp_1^{t+l}$ </td><td> $csp_2^{t+l}$ </td><td> $csp_3^{t+l}$ </td><td> $csp_4^{t+l}$ </td><td> $csp_5^{t+l}$ </td></tr><tr><td> $csp_1^t$ </td><td>1.00</td><td>0.65</td><td>0.55</td><td>0.5</td><td>0.08</td></tr><tr><td> $csp_2^t$ </td><td>0.58</td><td>0.40</td><td>0.55</td><td>0.25</td><td>0.00</td></tr><tr><td> $csp_3^t$ </td><td>0.72</td><td>0.46</td><td>0.83</td><td>0.53</td><td>0</td></tr><tr><td> $csp_4^t$ </td><td>0.17</td><td>0.15</td><td>0.15</td><td>0.16</td><td>0.17</td></tr></table>

<table><tr><td>Class Boolean</td><td> $csp_{1}^{t+l}$ </td><td> $csp_{2}^{t+l}$ </td><td> $csp_{3}^{t+l}$ </td><td> $csp_{4}^{t+l}$ </td><td> $csp_{5}^{t+l}$ </td></tr><tr><td> $csp_{1}^{t}$ </td><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td></tr><tr><td> $csp_{2}^{t}$ </td><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td></tr><tr><td> $csp_{3}^{t}$ </td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td></tr><tr><td> $csp_{4}^{t}$ </td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td></tr></table>

1 In the previous table, $c s p _ { 1 } ^ { t } \ = \ c s p _ { 1 } ^ { t + l }$ are emerging patterns because (1) they are the same pattern $( C S C I _ { 1 1 } = 1 . 0 0$ and their corresponding class Boolean $b _ { 1 1 } = 1 \rangle ,$ ; and (2) the difference of their support values is greater than the defined min\_diff.

$$
\left| \sup \left(c s p _ {1} ^ {t + l}\right) - \sup (c s p _ {1} ^ {t}) \right| = | 0. 0 8 - 0. 0 4 | = 0. 0 4 \geq \min \_ d i f f = 0. 0 3.
$$

2 $c s p _ { 1 } ^ { t + l }$ and $c s p _ { 2 } ^ { t + l }$ are similar patterns to $c s p _ { 1 } ^ { t }$ because their $C S C I _ { i j }$ is higher than the PMT $( C S C I _ { 1 1 } ~ = ~ 1 . 0 0 ~ \dot { \geq } ~ 0 . 3 $ and $\ C S C I _ { 1 2 } \ =$ $0 . 6 5 \ \geq \ 0 . 3 )$ and their classes are the same. However, for unexpected change patterns, they cannot be the same pattern $( C S C I _ { i j } = 1 )$ . As a result, $c s p _ { 2 } ^ { t + l }$ is a slightly unexpected change pattern regarding csp<sup>t</sup> .

3 In contrast to $\left( c s p _ { 1 } ^ { t } , c s p _ { 2 } ^ { t + l } \right)$ , a pair of slightly unexpected change patterns, $c s p _ { 3 } ^ { t + l }$ and $c s p _ { 4 } ^ { t + l }$ are the totally unexpected change patterns regarding csp<sup>t</sup> because they are similar patterns $( C S C I _ { 1 3 } ~ = ~ 0 . 5 5 ~ \ge ~ 0 . 3 $ and $C S C I _ { 1 4 } = 0 . 5 \ \geq \ 0 . 3 )$ with different classes $( b _ { 1 3 } = b _ { 1 4 } = 0 )$

4 For $c s p _ { 5 } ^ { t + l }$ , none of the patterns with same class in $C S P ^ { t }$ is similar to it $( \bar { C S } C I _ { 1 5 } = 0 . 0 8 < 0 . 3$ and $C S C I _ { 2 5 } = 0 \le 0 . 3 )$ ; thus, it is defined as an added pattern. By contrast, $c s p _ { 4 } ^ { t }$ is a perished pattern because no pattern in the current database is similar to it $( C S C I _ { 4 3 } = 0 . 1 5 < 0 . 3$ and $C S C I _ { 4 4 } = 0 . 1 6 < 0 . 3 )$

## 3.4. Phase three: significant change evaluation

Based on the above definitions, three types of change patterns can be identified. However, a large number of change patterns would disturb managers’ decision-making. To solve this problem, C is an index, designed to measure the significance of change [16,17,28,32]. If the value of C is equal to or greater than $\psi _ { \mathrm { m i n } }$ , then the patterns are determined to be “significant change patterns,” where $\psi _ { \mathrm { m i n } }$ is a user-defined minimum significance threshold, whose objective is to remove nonsignificant change patterns and retain only a valuable partial set of change patterns for decision makers. In the following definitions, sup csp<sup>t</sup> and sup $\left( c s p _ { j } ^ { t + l } \right)$ are the support values of csp<sup>t</sup> and $c s p _ { i } ^ { t + l }$ <sup>l</sup>, respectively.

In the case of the emerging pattern, $\Gamma _ { i j }$ is defined as the support changing ratio between csp<sup>t</sup> and $c s p _ { i } ^ { t + l }$ because users are interested in how many the support value increases over time.

Definition 9 (The significance of an emerging pattern). If a CSP pair, csp<sup>t</sup> and $c s p _ { j } ^ { t + l }$ , has been defined as a pair of emerging patterns, then its significance, $\Gamma _ { i j } ^ { e p }$ , would be defined as

$$
\Gamma_ {i j} ^ {e p} = \frac {\sup \left(c s p _ {j} ^ {t + l}\right) - \sup \left(c s p _ {i} ^ {t}\right)}{\sup \left(c s p _ {i} ^ {t}\right)}.\tag{7}
$$

${ \mathrm { I f } } \Gamma _ { i j } ^ { e p } \geq \psi _ { \operatorname* { m i n } } , c s p _ { i } ^ { t } = c s p _ { j } ^ { t + l }$ would be defined as a significant emerging pattern. □

From Section 3.3.2, the more similar two patterns are (but they cannot be equal), the more “unexpected” they are. On the other hand, if the support of an existing pattern is much greater than the support of a past pattern, they are considered an important change. Using the above reasons, to compute the significance of an unexpected change, the $\Gamma _ { i j }$ is defined as the multiplication of the support changing ratio between csp<sup>t</sup> and $c s p _ { j } ^ { t + l }$ and their similarity (CSCI ).

Definition 10 (The significance of an unexpected change). If a CSP pair, csp<sup>t</sup> and $c s p _ { i } ^ { t + l } ,$ , has been defined as an unexpected change, then its significance, $\Gamma _ { i j } ^ { u c }$ , would be defined as

$$
\Gamma_ {i j} ^ {u c} = C S C I _ {i j} \times \frac {\sup \left(c s p _ {j} ^ {t + l}\right)}{\sup \left(c s p _ {i} ^ {t}\right)}.\tag{8}
$$

If $\Gamma _ { i j } ^ { u c } \ge \psi _ { \mathrm { { m i n } } } .$ , csp<sup>t</sup> and $c s p _ { j } ^ { t + l }$ would be defined as a significant unexpected change. □

For the significance of an added pattern [28], this study uses $( 1 -$ maxCSCI ) to represent the dissimilarity between $c s p _ { i } ^ { t + l }$ and the patterns in $C S P ^ { t }$ . The greater the dissimilarity, the higher the likelihood that the pattern is an added pattern. Second, an added pattern with higher support should be considered more significant than others. Accordingly, this study defines the significance of added/perished patterns as follows.

Definition 11 (The significance of an added pattern). $\mathrm { I f } c s p _ { j } ^ { t + l }$ has been defined as an added pattern to all $c s p _ { i } ^ { t }$ in $C S P ^ { t }$ , then its significance, $\Gamma _ { j } ^ { a p }$ , is defined as

$$
\Gamma_ {j} ^ {a p} = \left(1 - \max C S C I _ {j}\right) \times 1 0 0 \times \sup \left(c s p _ {j} ^ {t + l}\right),\tag{9}
$$

where max $C S C I _ { j } = \operatorname* { m a x } \left( C S C I _ { 1 j } , C S C I _ { 2 j } , \cdot \cdot \cdot , C S C I _ { | C S P ^ { t } | j } \right) . \operatorname { I f } \Gamma _ { j } ^ { a p } \geq \psi _ { \operatorname* { m i n } } .$ $c s p _ { i } ^ { t + l }$ would be defined as a significant added pattern. The constant, 100, is for normalization, which may be adjusted to the characteristics of datasets. □

Definition 12 (The significance of a perished pattern). If csp<sup>t</sup> has been defined as a perished pattern to all $c s p _ { j } ^ { t + l }$ in $C S P ^ { t + l }$ , then its significance, $\Gamma _ { i } ^ { p p }$ , is defined as

$$
\Gamma_ {i} ^ {p p} = (1 - \max C S C I _ {i}) \times 1 0 0 \times \sup \left(c s p _ {i} ^ {t}\right),\tag{10}
$$

where max $C S C I _ { i } ~ = ~ \operatorname* { m a x } { \left( C S C I _ { i 1 } , C S C I _ { i 2 } , \cdot \cdot \cdot ~ , C S C I _ { i \vert C S P ^ { t + l } \vert } \right) }$ . If $\Gamma _ { i } ^ { p p } \ \geq$ $\psi _ { \mathrm { m i n } } , c s p _ { i } ^ { t }$ <sup> </sup>would be defined as a significant perished pattern. □

Example 6. Given $\psi _ { \mathrm { m i n } } = 0 . 3$ and following Example 5.

1 $c s p _ { 1 } ^ { t } \ = \ c s p _ { 1 } ^ { t + l }$ is an emerging pattern and its significance is $\begin{array} { r } { \tilde { \Gamma _ { 1 1 } ^ { e p } } ^ { 1 } = \frac { 0 . 0 8 \tilde { - } 0 . 0 4 } { 0 . 0 4 } = 1 . 0 0 \geq \breve { \psi } _ { \mathrm { { m i n } } } = 0 . 3 ; } \end{array}$ hence, it is a significant emerging pattern.

2 For csp<sup>t</sup> and $c s p _ { 2 } ^ { t + l }$ are defined as a pair of unexpected changes, their $\begin{array} { r } { \dot { \Gamma } _ { 1 2 } ^ { e p } = 0 . \dot { 6 } \dot { 5 } \times \frac { 0 . 0 6 } { 0 . 0 4 } = 0 . 9 7 5 \geq \dot { \psi } _ { \mathrm { m i n } } = 0 . 3 } \end{array}$ ; hence, they are also a pair of significant unexpected change.

3 For $c s \bar { p } _ { 5 } ^ { t + l }$ , its $\Gamma _ { 5 } ^ { \bar { a } p }$ is calculated as follows:

$$
\begin{array}{l} \Gamma_ {5} ^ {a p} = (1 - \max C S C I _ {j}) \times 1 0 0 \times \sup \left(c s p _ {5} ^ {t + l}\right) \\ \qquad = (1 - \max (0. 0 8, 0. 0 0)) \times 1 0 0 \times 0. 0 5 = 4. 6 \geq \psi_ {\min} = 0. 3; \end{array}
$$

hence $c s p _ { 5 } ^ { t + l }$ is a significant added pattern. 4 For $c s p _ { 4 } ^ { t }$ , its $\Gamma _ { 4 } ^ { p p }$ is calculated as follows:

$$
\begin{array}{l} \Gamma_ {4} ^ {p p} = (1 - \max C S C I _ {i}) \times 1 0 0 \times \sup \quad (c s p _ {4} ^ {t}) \\ \qquad = (1 - \max (0. 1 5, 0. 1 6)) \times 1 0 0 \times 0. 1 = 8. 4 \geq \psi_ {\min} = 0. 3; \end{array}
$$

hence $c s p _ { 4 } ^ { t }$ is a significant perished pattern.

## 4. Experiment results

## 4.1. FoodMart2000 dataset and its data pre-processing

This research adopted the FoodMart2000 database, a real-world database provided by Microsoft (https://technet.microsoft.com/enus/library/), as the experimental database; it includes data of customers, purchased products, and transactions. In the database, there are many tabs such as account, category, customer, days\_check, and employee. Numerous past studies have used this dataset to verify their research models [27,33,34,40].

This study constructed CSPs of purchasing behaviors from the FoodMart2000 database; for example,

$$
s = <   (D e l i S a l a d s), (T u n a, P e r s o n a l H y g i e n e) > \rightarrow L o w.
$$

This requires the following information: the purchased products, the customers who purchased these products, the time at which purchases were made, and how much the customers spent. As a result, only four tabs are used to build the CSPs: sales\_fact, time\_by\_day, product, and product\_class. The database diagram of FoodMart2000 is shown in Fig. 4, showing how the tabs as connected. The following shows how the original transaction database is transferred into a temporal sequence database (Fig. 5) by using the following four data pre-processing steps.

1. Data cleaning: In order to generate reasonable data mining results, this study set the standard of being frequent customers as four (this standard is selected in order to generate similar numbers of high and low CSPs in S<sup>t</sup> and $S ^ { t + \forall }$ , respectively. This reason will be discussed later in this subsection.) After the record deletion of less than three-time shopping customers, the remaining transactions are used in the next step.

2. Data partitioning: The database is divided into two subdatabases using two time intervals, t = 1997 and t+l = 1998. The FoodMart2000 database has already recorded the sales time in the column time\_id in the sales\_fact tab, which must be used with and be explained with the time\_by\_day tab. For example, time\_id = 483 represents 1997/4/27.

3. Data simplification: We consider that human brains cannot process too much information. Because there are 1560 types of products, interpreting the meanings of the numerous and similar discovered CSPs is dificult. As a result, data simplification is executed for two reasons: (1) If the number of product types increases, the number of possible generated CSPs will also significantly increase. Too many generated CSPs will interfere with managers’ decision-making ability. (2) For example, for the following two CSPs,

$$
\begin{array}{l}<   (L a k e L o w F a t \quad C o l e S l a w), (v e g e t a b l e s) > \rightarrow H\\<   (W a l d e n L o w F a t \quad C o l e S l a w), (v e g e t a b l e s) > \rightarrow H\end{array}
$$

there is only a very slight difference between them (their brands). It is unnecessary to report this CSP to the managers. The products are then replaced by their product subcategories (the transformation uses the corresponding columns, product\_id and product\_class\_id, in the product and product\_class tabs). For example, for the product, “Lake Low Fat Cole Slaw ”, its product\_subcategory is “Deli Salads.” The final number of product subcategories is 110.

4. Data transformation: The items in the same transaction (with the same time\_id) are placed into an itemset, the itemsets belonging to the same customer are transferred into a sequence, and the itemsets are then arranged in accordance

![](/api/attachments/P8WH3JAB/fulltext/images/d0b07f38dbec89cd5439db0ffc845b8b74ca0c83d53044b59be4616595a8413c.jpg)  
Fig. 4. Database diagram of FoodMart2000.mdb.

with the time of purchase. For example, Fig. 5 shows five shopping records. The time\_id shows that the first three records occur at the same time (their time\_ids are all 483) and the final two records occur at a later time (their time\_ids are 661). That is, the first three products (1318, 1534, and 885) are placed into the same itemset, and the fourth and fifth products are placed into the second itemset, (1279, 736). The generated sequence is s =< (1318, 1534, 885), (1279, 736) >. Subsequently, the customers are categorized into two classes based on their total consumption in one year: H (high consumption, more than US \$200 in a single transaction) and L (low consumption, less than or equal to US \$200 in a single transaction). For example, for the customer (customer \_id = 3) in Fig. 5, the annual consumption is \$2.79 + \$5.56 + \$2.76 + \$8.88 + \$6.39 = 26.38, which is lower than \$200 and is categorized as “L.” The standard is set as \$200 because it can generate the most equal numbers of H and L sequences when the standard of being frequent customers is four (see Fig. 6).

![](/api/attachments/P8WH3JAB/fulltext/images/d736fe201900ae21b62e2dc6beec64c8e8f3989b0dfc6b2569b14147eea17c75.jpg)  
Fig. 5. Data transformation from original transactions to a sequence in the FoodMart2000 database.

![](/api/attachments/P8WH3JAB/fulltext/images/52b74b9fd0a74242a8d295411f3b4d44cb071cbfd8c41569062be34527fc0532.jpg)  
(a) Number of sequences using various frequent customer standards.

![](/api/attachments/P8WH3JAB/fulltext/images/5f4df5f99b37ed154b29a45e73a5582229b7732dd3682b6bfe1389ea5992c227.jpg)  
(b) Number of H and L sequences using various VIP standard.  
Fig. 6. The reason the standard of being frequent customers is set as four and VIP is set as \$200.

From the example in Fig. 5, a temporal sequence can be obtained as follows:

$$
s = <   (1 3 1 8, 1 5 3 4, 8 8 5), (1 2 7 9, 7 3 6) > \rightarrow 2 6. 3 8.
$$

After the data interpretation using the connections among product and product\_class tabs, the aforementioned sequence can be transferred into the following easy-to-read sequence.

$$
s = <   (D e l i S a l a d s, S u g a r, P a s t a), (T u n a, P e r s o n a l H y g i e n e) > \rightarrow L.
$$

Finally, there are 1885 and 2879 sequences in S<sup>t</sup> and $S ^ { t + l } ,$ , in which t = 1997 and t + l = 1998, respectively (Table 1).

## 4.2. Data analysis

Microsoft SQL 2008 is used as the database software and MAT-LAB is used to construct the SeqClassChange model. In the first phase of the SeqClassChange model, CBS is used to mine CSPs from four sub-datasets (the four combinations of the two classes (H and L) and two time-periods). The differences between two CSP generation methods, CBS\_CLASS and CBS\_ALL, are examined first.

The number of discovered CSPs using CBS\_CLASS in different subdatasets and the minimum support thresholds are listed in Table 2. When the min\_sup decreases, the numbers of CSPs in four subdatasets increase. This intuitive and reasonable result shows that more CSPs are generated if more sequences pass the lower threshold.

On the other hand, CBS\_ALL requires one more parameter: minimum class support threshold, min\_cls\_sup. It was observed that almost no CSP can be generated if min\_cls\_sup 0.2 (Fig. 7). Even if min\_cls\_sup is 5%, the numbers of CSPs (from t = 1997 and t + l = 1998) are still very small and can not be compared to the number generated from CBS\_CLASS (Table 3). After further checking, almost all the same CSPs generated by CBS\_ALL appear in those generated by CBS\_CLASS. This intuitive result can be explained because the CSP generation must pass two support examinations in CBS\_ALL. As a result, it was decided to select CBS\_CLASS as the CSP generation method in Phase one because it is simpler and more effective.

Number of original sequences of the two customer groups (L and H) in two time periods after data transformation.

<table><tr><td>Class/Time-period</td><td> $S^{t}$  (t = 1997)</td><td> $S^{t+l}$  (t + l = 1998)</td></tr><tr><td>Class=L</td><td>1151</td><td>1430</td></tr><tr><td>Class=H</td><td>734</td><td>1449</td></tr><tr><td>Total</td><td>1885</td><td>2879</td></tr></table>

Five different types of change patterns were discovered in the third phase of the SeqClassChange model. The number of significant change patterns with varying PMT values from 0.1 to 0.9 were observed under different combinations of min\_sup\_L and min\_sup\_H. The $\psi _ { \mathrm { m i n } }$ value was set as 0.5. As shown in Fig. 8, the following phenomena can be observed.

As the PMT values increase, the number of added/perished patterns also increases; by contrast, the number of slightly/totally unexpected change patterns decreases. These results are consistent with expectations. That is, the closer the PMT value is to one, the fewer the number of similar CSP pairs because the similarity standard is increased. As a result, more added/perished patterns can pass the threshold. By contrast, the higher the PMT value, the fewer unexpected patterns can pass the higher PMT threshold. (The number of EP is not shown here because it is only related to the value of min\_diff, not PMT)

When min\_sup increases, the numbers of emerging and silghtly/totally unexpected change patterns, added, and perished patterns decrease. This is because the larger the min\_sup value, the fewer frequent CSPs passing the min\_sup threshold (they cannot be generated in the first phase of the SeqClassChange). The frequent CSPs are also the candidate sequence for comparing their similarities in the second phase. Thus, more and more emerging and added/perished patterns are generated because of the increasing number of candidate sequences. (There are only two lines in Fig. 8 (d) because the results show that min\_sup\_H does not affect the number of significant perished patterns.)

As examples, this study demonstrates several significant change patterns with the following parameters: PMT = 0.6, min\_diff = 0.03 and $\psi _ { \mathrm { m i n } } = 0 . 3$ . The managerial implications and customer behavior trends behind them are: (1) their types of change patterns and (2) their implied cause-and-effect relationships.

Numbers of CSPs using CBS\_CLASS in different customer categories and minimum support thresholds.

<table><tr><td>Class</td><td>min_sup(%)</td><td> $CSP^t$ </td><td> $CSP^{t+l}$ </td></tr><tr><td rowspan="2">L</td><td>1%</td><td>7956</td><td>9366</td></tr><tr><td>2%</td><td>2582</td><td>3220</td></tr><tr><td rowspan="2">H</td><td>15%</td><td>1339</td><td>6358</td></tr><tr><td>20%</td><td>596</td><td>2146</td></tr></table>

![](/api/attachments/P8WH3JAB/fulltext/images/362304fed68412148a4dd81d1eabafb3b0a1312b684c46540070381e490595a8.jpg)  
Fig. 7. Number of CSPs using CBS\_ALL under various min\_cls\_sup values under min\_sup\_L = 1% and min\_sup $\begin{array} { r } { H = 1 5 \% . } \end{array}$

The following shows two significant emerging patterns, whose support values highly increase from 1997 to 1998.

$$
c s p = <   (D r i e d F r u i t) (C l e a n e r s) > \rightarrow L
$$

$$
c s p = <   (C h e e s e) (C h i p s) (F r e s h V e g e t a b l e s) > \rightarrow H.
$$

From the contents of the patterns, it can be observed that the items are dried fruit, cleaners, cheese, chips and fresh vegetables, which are all daily commodities. These results imply that the consumption trends of daily commodities changed slightly in the research time interval. That is, the strengths (the support values) of the two significant emerging patterns increase from $t = 1 9 9 7 \tan t + l = 1 9 9 8$ . These results inform managers to pay attention to these trends. Moreover, the CSPs may also imply cause-and-effect relationships. The first emerging pattern belongs to the low class and the second one belongs to the high class. A significant difference between the two patterns is the type of fruit and vegetables (dried fruit and fresh vegetables). This implies that customers who are willing to spend money to purchase fresh food may become high-class customers.

< (Spices)(FreshFruit) > H and < (Pasta)(FreshVegetables) > H are slightly significant unexpected changes, which are beyond the manager’s apriori perceptions. In the first pattern, the customer purchasing spices belongs to the high class. However, in the current database, the pattern changes slightly. Now, the customers who first purchase (1) spices and then (2) fresh fruit also belong to the high class. Managers may need to know why these trends occur and enhance their understanding of the market.

< (Pasta)(Cheese) > for the “L” class in the present (t + l = 1998) database, which do not exist in the past $( t = 1 9 9 7 )$ database. Managers may establish new promotion strategies for these added consumption trends for the low-consumption customers. By contrast, < (Nuts)(Pizza)(FreshVegetables) > H also shows a new consumer behavior, which enables managers to promote related commodities to the high-consumption customers.

Numbers of CSPs using CBS\_ALL in different customer categories and minimum support thresholds.

<table><tr><td rowspan="2">Class</td><td rowspan="2">min_sup(%)</td><td colspan="2">min_cls_sup = 5%</td><td colspan="2">min_cls_sup = 10%</td></tr><tr><td> $CSP^t$ </td><td> $CSP^{t+l}$ </td><td> $CSP^t$ </td><td> $CSP^{t+l}$ </td></tr><tr><td rowspan="2">L</td><td>1%</td><td>187</td><td>161</td><td>59</td><td>42</td></tr><tr><td>2%</td><td>187</td><td>161</td><td>46</td><td>32</td></tr><tr><td rowspan="2">H</td><td>15%</td><td>233</td><td>883</td><td>238</td><td>825</td></tr><tr><td>20%</td><td>105</td><td>348</td><td>105</td><td>334</td></tr></table>

< (CannedFruit)(Mufins) > and < (DeliMeats)(CannedVegetables) >, appear in the “L” class in the past $( t = 1 9 9 7 )$ database; however, they disappear in the present $( t + l = 1 9 9 8 )$ database. Both patterns contain a keyword, “canned.” That phenomenon might indicate that the low-consumption customers do not like to purchase canned fruit anymore. Managers may stop related promotions aimed at low-consumption customers.

## 5. Conclusions, discussion, and future directions

In conclusion, this study provides an integrated three-phase model SeqClassChange, for revealing valuable information from the databases of two different time periods. The first phase uses the CBS\_CLASS algorithm to generate a form of temporal sequence, CSPs, which can distinguish the sequential relationships between causes and effects. The second phase analyzes the change within CSPs at two different time periods; then, the change can be classified into three types of categories: emerging patterns, unexpected change patterns, and added/perished patterns. The third phase employs a user-defined minimum significance threshold to reduce the number of discovered change patterns; only the valuable patterns are kept and reported to users. For academics, the value of this model is in addressing the gap in previous studies [16,17,28,32,35], in corporating CSPs in change mining, providing implications of sequential cause-and-effect relationships, and helping managers to make better decisions. The design of the proposed model is inspired and referring to the research of Tsai and Shieh [32]. Table 4 gives a comparison of the proposed model and the model of Tsai and Shieh [32], illustrating to what extent this study actually builds further on their research.

Next, some interesting topics must be considered.

1. How to partition the whole dataset into two disjointed datasets, S<sup>t</sup> and $S ^ { t + l }$ , in accordance with the time boundary<sup>5</sup>. This issue can be expected in a real-life situation or application. For instance, if one dataset is collected for marketing in order to understand customer change behaviors, the time boundary can be defined in light of four perspectives, month, season, half a year, or a year. In addition, the time boundary could also be defined as before and after a marketing strategy execution; therefore, managers can observe the difference between the before and after strategy execution periods. Another time boundary idea is used in financial or accounting management. Since the data collection of the two fields depends upon an annual time-frame, the time boundary can be suggested as a fiscal year. According to the above, time boundaries should be defined according to realistic situations or applications.

![](/api/attachments/P8WH3JAB/fulltext/images/b9ff411237158b517bc166115e4b2d06f31a24b79ff452050b56fd1c4963e729.jpg)  
(a) Significant SUCP.

![](/api/attachments/P8WH3JAB/fulltext/images/d4d994d38e742de8dd6679276936199be79ec1383b46563d8579b3d774eef84b.jpg)  
(b) Significant TUCP.

![](/api/attachments/P8WH3JAB/fulltext/images/b0790cffa98f1a3a1b24fc72b1c7aeeb46956b9c66a6e347174cc486d2e202fb.jpg)  
(c) Significant AP.

![](/api/attachments/P8WH3JAB/fulltext/images/c207593cf55b0d1b732c3c3a1c4cee94b58df4aa2dad56392938baed142c1360.jpg)  
(d) Significant PP.  
Fig. 8. Number of different significant change patterns.

2. The first phase of SeqClassChange is the CBS\_CLASS algorithm, which identifies temporal sequences and then assigns class labels to each sequence. Although this study adopts the CBS\_CLASS algorithm as the CSP generation algorithm, theoretically, the CBS\_CLASS algorithm can be replaced by any sequence classification algorithm as long as it is eficient.

3. There are also many parameters in the method which should be set. This makes the proposed model more dificult to use in practice for managers because they need to make more decisions. This limitation stems from the nature of the data mining field because the result is completely data-driven; practitioners cannot know the data distribution in the beginning. Hence, they have to use a trial and error to find the optimal thresholds for the proposed model.

However, despite the SeqClassChange model’s advantages, it does have some limitations<sup>6</sup>. Practitioners should pay attention to the following discussions for the research limitations: (1) the complete causality, (2) the sample databases, (3) the data simplification decision, and (4) the significant thresholds.

1. The complete causality: The mined CSP in this study can give the managers the implication of cause-and-effect relationships. However, it must be admitted that the proposed model cannot establish a complete causality, which requires three conditions: covariation, sequence (temporal sequence of events), and nonspurious covariance [14]. First, in the first phase of the proposed model, the covariation condition is achieved using the minimum support threshold. Second, the class labels of the proposed CSP are assigned to each customer only after the occurrence of the customer’s purchases; that is, the temporal relationship between the cause (the customer’s purchases) and effect (the customer’s class). However, the proposed model cannot be used to test nonspurious covariances (for example, moderator, mediator, or suppressor must be tested in Structural Equation Modeling).

2. The sample dataset: In Section 4.1, only four tabs in the Food-Mart2000 database are used to construct CSPs, but not all datasets have these levels of abstraction that can be simplified to form CSPs. Although this study uses a real-world consumer behavior database, provided by Microsoft, the generalization of the results to other different databases may be limited.

3. The data simplification decision: In Section 4.1, the data simplification is executed to avoid numerous and too similar CSPs being generated. But what if a manager does have the insight to identify the slight difference between two similar CSPs? In order to allow the construction of a good decision support system, users should be able to adjust how much information could be used. It is thus suggested that data simplification decisions be left to users.

4. Significance thresholds: With respect to the design of significant change evaluation, there is an idea that users or managers can furnish multiple significance thresholds to gauge the significance of different types of change patterns. This approach, however, will greatly increase the degree of user participation, leading to a dilemma. Hence, in practice it is suggested that only one threshold be used to obtain all types of significant change patterns.

Table 4  
Comparison between the proposed model and the model of Tsai and Shieh [32] .

<table><tr><td>Framework</td><td>Definitions and relationships of the three types of change patterns</td><td>Significant change evaluation</td><td>Patterns used for change detection</td></tr><tr><td>Similar but detecting changes for CSPs</td><td>Modified for the change mining of CSPs</td><td>Slightly modified their formulas as ours</td><td>Different and add extra information, sequential cause-and-effect relationships</td></tr></table>

Future research of different CSP generation and different sample databases is required. Several crucial topics are as follows.

1. Further research might extend the present use of the CBS\_CLASS algorithm to examine the effect of CSP generation on different types of change patterns.

2. The determination of pattern significance in this study uses two factors, support and similarity. However, the implication of significance is not only derived from these two factors, but also from context-sensitive consideration. This consideration is sometimes based on user judgment. Therefore, in the future, this model should include develop a friendly user interface (UI) for users so that they can identify all types of significant change patterns.

3. Change mining in temporal sequences is a useful technique to help managers identify management implications within databases; the next step may be to investigate the potential of the model in different sets of sequential events, for example, text mining.

4. The implementation of the fuzzy-time interval [17] into the SeqClassChange model would be the next step to extend the research scope.

## Acknowledgments

The authors are very grateful to the anonymous reviewers for their valuable suggestions to substantially improve the earlier version of our paper. The authors would also like to thank the Ministry of Science and Technology, Taiwan (R.O.C.) for financially supporting this research under Grant MOST 106-2410-H-194-026-MY2.

## Appendix A. Appendix

Theorem 1 (The time-complexity of the SeqClassChange algorithm). The time-complexity of the SeqClassChange algorithm is ${ \cal O } ( ( \mu _ { I S } \times \mu _ { I } ) ^ { 2 }$ $\left( N _ { t } + N _ { t + l } \right) )$ , where $\mu _ { I S }$ denotes the average number of itemsets in a temporal sequence, $\mu _ { I }$ denotes the average number of items in an itemset, $N _ { t }$ denotes the number of classifiable sequential patterns at time-period t, and $N _ { t + l }$ denotes the number of classifiable sequential patterns at time-period $t + l .$ □

Proof. According to the flow chart of the SeqClassChange model in Fig. 1, it is known that there are two major steps, (1) pattern matching to identify the change type of SCPs and (2) detection of significant change patterns, taking most times to be executed. For the first step, the algorithm is going to perform the similarity comparison between $C S P ^ { t }$ and $C S P ^ { t + l }$ . Any pair of CSPs picked from $C S P ^ { t }$ and $C S P ^ { t + l }$ must be non-repetitive. The itemsets and items of any pair must be compared for the similarity computation. The comparison therefore takes time ${ \cal O } ( ( \mu _ { I S } \times \mu _ { I } \times N _ { t } ) \times ( \mu _ { I S } \times \mu _ { I } \times N _ { t + l } ) )$ . For the second step, the algorithm identifies the significance of change patterns with the check of all patterns from $C S P ^ { t }$ and $C S P ^ { t + l }$ . Therefore, this step requires time $O ( N _ { t } + N _ { t + l } )$ . After observing the two steps, it is understood that the first step is the most time-consuming; therefore, the total time for the algorithm is $O ( ( \mu _ { I S } \times \mu _ { I } ) ^ { 2 } \times ( N _ { t } + N _ { t + l } ) )$ □

Theorem 2 (The space-complexity of the SeqClassChange algorithm). The space-complexity of the SeqClassChange algorithm is $\Theta ( ( \kappa _ { I S } \times \kappa _ { I } ) ^ { 2 } \times$ $( N _ { t } { + } N _ { t { + } l } ) )$ , where $\kappa _ { I S }$ denotes the maximal number of itemsets of a temporal sequence from $C S P ^ { t }$ and $C S P ^ { t + l }$ , j denotes the maximal number of items in an itemset, $N _ { t }$ denotes the number of classifiable sequential patterns at time-period t, and $N _ { t + l }$ denotes the number of classifiable sequential patterns at time-period $t + l .$ □

Proof. The data structure of the SeqClassChange algorithm is designed for saving all patterns from $C S P ^ { t }$ and $C S P ^ { t + l }$ <sup>l</sup>, respectively. After this, the similarity computation of any pair gathers any two patterns from this data structure. The space required by $C S P ^ { t }$ is $\Theta ( \kappa _ { I S } \times \kappa _ { I } \times N _ { t } )$ and $C S P ^ { t + l }$ requires $\Theta ( \kappa _ { I S } \times \kappa _ { I } \times N _ { t + l } )$ . Therefore, the total space for the algorithm is $\Theta ( ( \kappa _ { I S } \times \kappa _ { I } ) ^ { 2 } \times ( N _ { t } + N _ { t + l } ) )$ □

## References

[1] R. Agrawal, T. Imielinski, A. Swami, Mining Association Rules Between Sets of´ Items in Large Databases Proceedings of the 1993 ACM SIGMOD Internationa Conference on Management of Data, ACM, NY, USA, 1993, pp. 207–216.

[2] W.-H. Au, K.C. Chan, Mining changes in association rules: a fuzzy approach, Fuzzy Sets Syst, 149 (1) (2005) 87–104

[3] P.K. Bala, Mining changes in purchase behavior in retail sale with products as conditional part, Proceedings of the IEEE 2nd International Advance Computing Conference (IACC), IEEE, Thapar University, Patiala, India, 2010, pp. 78–81.

[4] R.M. Chang, R.J. Kauffman, Y. Kwon, Understanding the paradigm shift to computational social science in the presence of big data, Decis. Support. Syst. 63 (2014) 67–80.

[5] H. Chen, R.H.L. Chiang, V.C. Storey, Business intelligence and analytics: from big data to big impact, MIS Q. 36 (4) (2012) 1165–1188.

[6] M.-C. Chen, A.-L. Chiu, H.-H. Chang, Mining changes in customer behavior in retail marketing, Expert Syst. Appl. 28 (4) (2005) 773–781.

[7] Y.-L. Chen, T.-K. Huang, Discovering fuzzy time-interval sequential patterns in sequence databases, IEEE Trans. Syst. Man Cybern. Part B Cybern. 35 (2005) 959–972.

[8] Y.-L. Chen, M.-H. Kuo, S.-Y. Wu, K. Tang, Discovering recency, frequency, and monetary (RFM) sequential patterns from customers’ purchasing data, Electron. Commer. Res. Appl. 8 (5) (2009) 241–251.

[9] D.W. Cheung, J. Han, V.T. Ng, C. Wong, Maintenance of discovered association rules in large databases: an incremental updating technique, Proceedings of the Twelfth International Conference on Data Engineering, IEEE. 1996, pp. 106–114.

[10] G. Dong, J. Li, Eficient mining of emerging patterns: discovering trends and differences Proceedings of the Fifth ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, ACM. 1999, pp. 43–52.

[11] M. El-Sayed, C. Ruiz, E.A. Rundensteiner, FS-Miner: eficient and incremental mining of frequent sequence patterns in web logs, Proceedings of the 6th Annual ACM International Workshop on Web Information and Data Management, ACM. 2004, pp. 128–135.

[12] J.a. Gama, I. žliobaite, A. Bifet, M. Pechenizkiy, A. Bouchachia, A survey on˙ concept drift adaptation, ACM Comput. Surv. 46 (4). (2014) 44:1–44:37.

[13] D. Gusfield, Algorithms on Strings, Trees and Sequences: Computer Science and Computational Biology, Cambridge University Press. 1997.

[14] J.F. Hair, W.C. Black, B.J. Babin, R.E. Anderson, Multivariate Data Analysis, Prentice Hall, 2009.

[15] J. Han, M. Kamber, J. Pei, Data Mining: Concepts and Techniques, Third edition ed. Morgan Kaufmann. 2011.

[16] C.-K. Huang, T.-Y. Chang, B.G. Narayanan, Mining the change of customer behavior in dynamic markets, Inf. Technol. Manag. 16 (2) (2015) 117–138.

[17] T.C.-K. Huang, Mining the change of customer behavior in fuzzy time-interval sequential patterns, Appl. Soft Comput. 12 (3) (2012) 1068–1086.

[18] S.M. Keaveney, M. Parthasarathy, Customer switching behavior in online services: an exploratory study of the role of selected attitudinal, behavioral, and demographic factors, J. Acad. Market Sci. 29 (4) (2001) 374–390.

[19] C. Lanquillon, Information filtering in changing domains, Proceedings of the International Joint Conference on Artificial Intelligence, 1999. pp. 41–48.

[20] A.J. Lee, F.-C. Yang, H.-C. Tsai, Y.-Y. Lai, Discovering content-based behavioral roles in social networks, Decis. Support. Syst. 59 (2014) 250–261.

[21] N. Lesh, M. Zaki, M. Oglhara, Scalable feature mining for sequential data, IEEE Intell Svst, Appl,15 (2) (Mar 2000) 48–56

[22] B. Liu, W. Hsu, Post-analysis of learned rules, Proceedings of Pacific Asia Conference on Knowledge Discovery in Databases, 1996. pp. 828–834.

[23] B. Liu, W. Hsu, H.-S. Han, Y. Xia, Mining changes for real-life applications, Proceedings of the Second International Conference on Data Warehousing and Knowledge Discovery, vol. 1874, Springer. 2000, pp. 337.

[24] B. Liu, W.H. Hsu, Y. Ma, Integrating classification and association rule mining, Proceedings of the Fourth International Conference on Knowledge Discovery and Data Mining, 1998. pp. 80–86.

[25] F. Masseglia, P. Poncelet, M. Teisseire, Incremental mining of sequential patterns in large databases, Data Knowl. Eng. 46 (1) (2003) 97–121.

[26] M Salehan D I Kim Predicting the performance of online consumer reviews: a sentiment mining approach to big data analytics, Decis. Support. Syst. 81 (2016) 30–40.

[27] K. Sarath, V. Ravi, Association rule mining using binary particle swarm optimization, Eng. Appl. Artif. Intell. 26 (8) (2013) 1832–1840.

[28] H.S. Song, K.J. Kim, S.H. Kim, Mining the change of customer behavior in an internet shopping mall, Expert Syst. Appl. 21 (3) (2001) 157–168.

[29] R. Srikant, R. Agrawal, Mining Sequential Patterns: Generalizations and Performance Improvements, Proceedings of the 5th International Conference on Extending Database Technology: Advances in Database Technology, Springer-Verlag, London, UK, 1996, pp. 3–17.

[30] R. Sun, C.L. Giles, Sequence learning: from recognition and prediction to sequential decision making, IEEE Intell. Syst. 16 (4) (2001) 67–70.

[31] C.-Y. Tsai, C.-J. Chen, C.-J. Chien, A time-interval sequence classification method, Knowl, Inf Syst, 37 (2)(2013) 251–278.

[32] C.-Y. Tsai, Y.-C. Shieh, A change detection method for sequential patterns, Decision Support Systems 46 (2) (2009) 501–511.

[33] Y.-J. Tsay, T.-J. Hsu, J.-R. Yu, FIUT: a new method for mining frequent itemsets Inf. Sci. 179 (11) (2009) 1724–1737.

[34] M.-C. Tseng, W.-Y. Lin, Eficient mining of generalized association rules with non-uniform minimum support, Data Knowl. Eng. 62 (1) (2007) 41–64.

[35] S.M.V. Tseng, C.-H. Lee, CBS: A New Classification Method by Using Sequential Patterns, Proceedings of the 2005 SIAM International Conference on Data Mining, 2005.

[36] V.S. Tseng, C.-H. Lee, Effective temporal data classification by integrating sequential pattern mining and probabilistic induction, Expert Syst. Appl. 36 (5) (2009) 9524–9532.

[37] A. Tsymbal, The problem of concept drift: definitions and related work, technical Report, 106, Computer Science Department, Trinity College, Dublin, Ireland, 2004.

[38] K.W. Wong, S. Zhou, Q. Yang, J.M.S. Yeung, Mining customer value: from association rules to direct marketing, Data Min. Knowl. Disc. 11 (1) (2005) 57–79.

[39] Z. Xing, J. Pei, E. Keogh, A brief survey on sequence classification, SIGKDD Explor. Newslett. 12 (1) (Nov 2010) 40–48.

[40] H.-L. Yang, C.-S. Wang, Two stages of case-based reasoning-Integrating genetic algorithm with data mining mechanism, Expert Syst. Appl. 35 (1) (2008) 262–272.

[41] T.-C. Yang, H. Lai, Comparison of product bundling strategies on different online shopping behaviors, Electron. Commer. Res. Appl. 5 (4) (2006) 295–304.

[42] M.J. Zaki, SPADE: an eficient algorithm for mining frequent sequences, Mach. Learn. 42 (1-2) (2001) 31–60.

[43] Y. Zhao, H. Zhang, S. Wu, J. Pei, L. Cao, C. Zhang, H. Bohlscheid, Debt detection in social security by sequence classification using both positive and negative patterns, Machine Learning and Knowledge Discovery in Databases, Springer. 2009, pp. 648–663.

Tony Cheng-Kui Huang received the Ph.D. degree in Information Management from National Central University of Taiwan in 2006. He is a professor in the Department of Business Administration, National Chung Cheng University of Taiwan. His current research interests include data mining/business intelligence/big data, information management, e-commerce, and soft computing. He has published papers in Deci sion Support Systems, IEEE Transactions on Systems, Man and Cybernetics — Part B, European Journal of Operational Research, Information Technology and Management, International Journal of Information Management, Data & Knowledge Engineering, Information Sciences, Fuzzy Sets and Systems, Journal of Systems and Software, Com puters & Education, Knowledge-Based Systems, Applied Soft Computing, Telematics and Informatics, Applied Intelligence, International Journal of Innovative Computing, Information and Control, and Expert Systems with Applications.

Pu-Tai Yang is currently an assistant professor in the Department of Business Administration at Tunghai University, Taiwan. He received his Ph.D. degree in Industrial Engineering and the graduate certificate in applied statistics from Purdue University in 2012. He also received the B.S. degree in physics from National Tai wan Normal University and the M.S. degree in physics (semiconductor) from National Taiwan University. His research interests include data mining, industrial automation and applied statistics.

Jen-Hung Teng is currently an engineer in Garmin Corporation, Taiwan. He received his M.S. degree in Information Management from National Chung Cheng University Taiwan. His research interests include data mining and information systems.
