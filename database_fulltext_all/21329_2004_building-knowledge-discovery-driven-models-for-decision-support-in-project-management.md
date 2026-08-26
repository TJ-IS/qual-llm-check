---
otero_id: 21329
otero_key: "ZMYZGDVH"
title: "Building knowledge discovery-driven models for decision support in project management"
authors: "Marı́a N. Moreno Garcı́a; Luis A.Miguel Quintales; Francisco J. Garcı́a Peñalvo; M.José Polo Martı́n"
year: "2004"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(03)00100-3"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Building knowledge discovery-driven models for decision support in project management

Marı´a N. Moreno Garcı´a\*, Luis A. Miguel Quintales, Francisco J. Garcı´a Pen˜alvo, M. Jose´ Polo Martı´n

Department Informa´tica y Automa´tica, University of Salamanca, Plaza Merced s/n, 37008 Salamanca, Spain

Received 23 July 2002; received in revised form 27 June 2003; accepted 28 June 2003 Available online 6 August 2003

## Abstract

Accurate estimations of software size in the early stages of a software project are critical in software project management because they lead to a good planning and reduce project costs. In this work, the relation between early software size measures as the function points and measures of the final product as the lines of code has been studied. A process to refine association rules, based on the generation of unexpected patterns, is proposed. The goal is to generate strong association rules between attributes that can be obtained early in the project and the final software size. <sup>D</sup> 2003 Elsevier B.V. All rights reserved.

Keywords: Association rules; Clustering; Data mining; Software size estimation; Project management

## 1. Introduction

A current trend in software organizations is to take advantage of data-mining techniques to extract knowledge from the huge volumes of data that they manage. Data-mining techniques provides the objective information needed to make decisions about business and engineering performance. In the project management environment, many of those decisions are based on the software size estimation.

The determination of the value of software size in the early stages of a software project is a key activity in order to predict the effort to be consumed in a software project. Accurate estimations are critical in software project management because they lead to a good planning and reduce project costs. Many methods for estimating software size have been developed. Most of them provide functional measures of the software size such as functions points [1], functions blocks [6] and object points [2]. The values obtained for those functional variables should correspond with the final product size (for example lines of code). In an earlier work [9], we used several supervised data mining techniques to obtain software size estimation models. A component-based method [13] and a global method (Mark II) [12] were taken as reference. We observed that models obtained by combining attributes from both methods were better than models obtained by using attributes of each method separately. We also found a correlation between the function points of the method Mark II (MKII FP) and lines of code (LOC). This indicates that the function points of the method Mark II are good size predictors, but that correlation is stronger for some size intervals than for others.

In this work, we have used unsupervised datamining algorithms in order to discover knowledge that enhances the results of the classification models obtained previously and lead to the development of more efficient decision-support systems. We have applied two knowledge discovery-driven techniques: clustering and association rules. The goal in knowledge discovery modeling is to discover rules and segments of the data that behave similarly. The aim of clustering is to partition the data into segments of similar records. Usually, a measure of distance is used to obtain homogeneous subsets of data (clusters) [3]. Homogeneity means that records in a cluster are in close proximity to each other. The proximity between records indicates similarity between them. That is, similar values of their attributes. This approach is known as demographic clustering. We use this technique to do an exploratory analysis of the distribution of attribute values around the pre-fixed LOC intervals (classes). We force the creation of clusters, which only contain records of one class. This guides us in the attribute discretization.

The generation of association rules is also an unsupervised task. Association rule algorithms discover patterns in the form ‘‘IF X THEN Y’’. The purpose is to find items that imply the presence of other items in the same transaction. A purchase consisting of several articles (items) can be considered as a transaction. In that context, rules represent affinities between items such as ‘‘customers who buy spaghetti also buy tomato sauce’’ (IF spaghetti THEN tomato sauce). The process of deriving rules is simple (count of occurrences of items) [3], but this is not the main objective. The objective is to evaluate the validity of the rules. Most of the existing methods consider two factors, support and confidence, which capture the statistical strength of a pattern. However, these factors are useful neither for informing about rules convenience nor for detecting conflicts between rules. It is necessary to consider another factors in order to obtain consistent and interesting patterns. This is the motivation for rules refinement. The topic of knowledge refinement has been treated in the literature, but in the area of association rules little research has been done. In Refs. [10,11], the concept of unexpectedness is introduced in an iterative process for refining association rules. The authors have proposed methods to discover unexpected pattern in data. They use prior domain knowledge to reconcile unexpected patterns and to obtain stronger association rules. Domain knowledge is fed with the experience of the managers. This is a drawback for the use of the method in the project management environment because the rules are numeric correlations between project attributes and they are influenced by many factors (size and complexity of the software, programming language, etc.). It is very difficult to acquire experience in this class of problem. For this reason, in this work we present a refinement method that is more suitable for our purposes, which does not need use managerial experience. It is also based on the discovery of unexpected patterns, but it uses ‘‘the best attributes for classification’’ in a progressive process for rules refinement. The best attributes are obtained by the technique of ‘‘importance of columns’’ [8] based on the amount of information (entropy) that the attributes provide in discriminating the classes (intervals of values of the target attribute LOC).

At first, we applied several data clustering algorithms to obtain a high-level view of what is occurring in the data with respect to software size and to classify records. We also applied association rule algorithms in order to discover data patterns, which relate software size to others software attributes. Extracted rules revealed which software size intervals showed a weak correlation between lines of code and Mark II function Points. Conflicts between rules were also detected. We applied a refinement process in order to solve these conflicts and obtain stronger rules that reinforce the relation between LOC and MKII FP by using other attributes that can be obtained early in the project life cycle. Our proposal allows valuable patterns to be obtained from data for suitable decision making in the context of project management.

The rest of the paper is organized as follows. Section 2 describes the experimental data used in this study and the meaning of the available attributes. In

Section 3, we explain the use of data clustering in the attributes discretization. Section 4 presents the ‘‘importance of columns’’ technique. We introduce de basis of association rules and the concept of unexpectedness in Section 5. The rules refinement process is explained in Section 6. Conclusions are presented in Section 7.

## 2. Data description

This section describes the data set used to build the models. It was obtained from experiments carried out by Dolado [4]. The data originate from academic projects in which students developed accounting information systems that have the characteristics of commercial products. Each system includes some or all of the following subsystems: sales, purchases, inventories, financial statements and production cycles. We have analyzed data from 42 projects written in Informix-4GL.

The information available was divided in two groups. One group containing global data from each project (42 records) and other group containing attributes from each component of the projects (1537 records). The code of the applications was classified into three types of components according to Verner and Tate [13].

## 2.1. Component attributes

TYPECOMP: type of component (1: menu, 2: input, 3: report/query)

OPTMENU: number of choices (only for menus)

![](/api/attachments/ZMYZGDVH/fulltext/images/ffc4933543f03025d06ea78e2eed80cdcbee84d09815810ad3efd3465f8edafd.jpg)

![](/api/attachments/ZMYZGDVH/fulltext/images/d0bcb3e31d86d512644346ff6b5646d9cbc36c2ec2ed3c29d32cc1ce760f1e0e.jpg)

![](/api/attachments/ZMYZGDVH/fulltext/images/43eabb60c8ce5cf0b3e9bf2af9a3f439231a11c6d2fbb02920f606e8af7483c4.jpg)

![](/api/attachments/ZMYZGDVH/fulltext/images/62c44072d1bf8cb7b65a6b49742072eb4d4f4e6d0aa9337588ddf934dbbaf55f.jpg)

![](/api/attachments/ZMYZGDVH/fulltext/images/a3760161957ac09eba69bc8cc6e4a25d15b0f8998d46d4b6b54cb28fd677939f.jpg)  
Fig. 1. Statistical study of the data.

![](/api/attachments/ZMYZGDVH/fulltext/images/585105c81a3603b99ddcb86f2ed2326d047e5f41d07a81f2729e14b6861b726d.jpg)

![](/api/attachments/ZMYZGDVH/fulltext/images/53c3396809946b9be80b1d31da58d5895497fb266ba67ec1a960d863bede56cd.jpg)

DATAELEMENT: number of data elements (only for inputs and reports/queries) RELATION: number of relations (only for inputs and reports/queries) LOC: lines of code.

## 2.2. Project attributes

The attributes described below are used in Mark II method [12] to calculate functions points. That proposal consists of considering a system composed of logical transactions. A logical transaction is a unique input/process/output combination triggered by a unique event of interest to the user or a need to retrieve information. The central concept in this method is that of entity, which replaces the concept of logical file.

LOC: lines of code

NOC: number of components

NTRNSMKII: number of transactions MKII

INPTMKII: number of total inputs

ENTMKII: number of referenced entities

OUTMKII: number of total ouputs (data elements over all transactions)

UFPMKII: number of unadjusted functions points MKII

We observed in previous research [9] that classification models obtained by combining attributes from both methods were better than models obtained by using attributes of each method separately. So, we added to project attributes those that we calculated from the module attributes of each project. The new attributes are the following:

NOC-MENU: total number of menu components NOC-INPUT: total number of input components NOC-RQ: total number of report/query components OPTMENU: total number of menu choices DATAELEMENT: total number of data elements RELATION: total number of relations

The statistical study of some of these attributes is shown in Fig. 1. The projects are between 726 and 8888 LOC. There are more records with low values of the attributes. However, high values have sufficient weight to influence the induction of the models.

## 3. Data clustering

Data used in the data mining process can be nominal, discrete and/or continuous. Discrete and continuous data are ordinal data types with orders among the values, while nominal values do not possess any order among them. Discrete values are intervals in a continuous spectrum of values. This kind of attributes is required in many induction algorithms. Furthermore, the discretization of continuous attributes can provide many benefits: data mining tasks are faster, rules induced with discrete values are shorter and easily understood and results can be more closely examined, compared and used [7].

All the attributes that are used in this work to generate association rules are continuous, that is, they can take a wide range of values. In order to reduce the number of rules generated, it is necessary to discretize the attributes by splitting the range of values into a manageable number of intervals.

At first, we considered the target attribute LOC. The values of LOC were partitioned into five uniform intervals. We want to know the relation between LOC and the values of others attributes that can be obtained early in the software life cycle. It is important to find the intervals of values of these attributes that produce strong relations. Therefore, we need to apply a multivariate discretization method, which considers multiple attributes simultaneously. For this purpose, we introduce a distance measure. A clustering technique was applied to all available attributes in order to know the relationship between the values of the attributes and the classes (LOC intervals). The clusters were built by using the single k-means algorithm with a Euclidean distance metric [5]. This distance function is very common for quantitative variables. In a space of n dimensions, the Euclidean distance $D ( p , q )$ between two points $p$ and $q$ is:

$$
[ D (p, q) ] ^ {2} = | | p - q | | ^ {2} = \sum_ {i = 1} ^ {n} \left(p _ {i} - q _ {i}\right) ^ {2}\tag{1}
$$

where $p _ { i }$ and $q _ { i }$ are the coordinates of the points $p$ and $q ,$ respectively. In our case, the points are the records to be compared and the coordinates are the n attributes of each record.

K-Means clustering is used to find groups of similar records. The number of clusters (k) is established before applying the algorithm that groups the records to minimize the overall dispersion within each cluster. The algorithm is iterative:

1. A value is assigned to k.

2. The k cluster centers are situated in random positions in the space of n dimensions.

3. Each record in the data is assigned to the cluster whose center is closest to it.

4. The cluster centers are recalculated based on the new data in each cluster.

5. If there are records that are closer to the center of a different cluster than the cluster that they belong to, then these records are moved to the closer cluster.

Steps 4 and 5 are repeated until no further improvement can be made.

There are many clustering techniques [5], but this is very simple and it is suitable for our purpose of doing an exploratory analysis of the data distribution.

The clusters were created with a weight for LOC three times greater than for other attributes. This is a way of driving the clustering of the attributes around the LOC intervals. The best results (low overlapping of the LOC intervals) were obtained with five clusters. We observed that the two intervals with the highest values of LOC always appeared together in a single cluster. Those intervals represent a low number of transactions, therefore we decided to join them. From the study of the distribution of attribute values in each cluster, we obtained the partition of the data values in order to generate the association rules (Fig. 2). The potential cut points were those situated in the boundaries between clusters. The clustering algorithm was applied again to the discretized data in order to eliminate cut points and to obtain greater intervals by joining adjacent intervals that always appeared together in the clusters.

![](/api/attachments/ZMYZGDVH/fulltext/images/67a52b9dbc821cfbdbbbfe8e2ae19ff875384fe2d09e59c578e1fd5cfb556277.jpg)  
Fig. 2. Distribution of the attribute values in five clusters.

## 4. Importance of columns

In classification problems, the label attribute is the target of the prediction process. By constructing a relation model between the label and the other attributes, the model can make predictions about new, unlabeled data. Importance of columns is a technique that determines how important various attributes (columns) are in discriminating the different values of the label attribute.

A measure called purity (a number from 0 to 100) informs about how well the columns discriminate the classes (different values of the label attribute). It is based on the amount of information (entropy) that the column (attribute) provides. The expression for that information (I) is:

$$
I (P (c _ {1}), \ldots , P (c _ {n})) = \sum_ {i = 1} ^ {n} - P (c _ {i}) \mathrm{log} _ {n} P (c _ {i})\tag{2}
$$

where P(ci) is the probability of the class i and n is the number of classes.

If the probabilities of the classes are the same, then the information is 1.

The purity is defined as:

$$
\text { Purity } = 1 - I\tag{3}
$$

The cumulative purity is a measure of the purity of partitioning the data when more than one column is used. The data are partitioned using columns, which influence the classification, in other words, columns that lead to a high purity partition. Each set in the partition has its own purity measure and the purity of the partition is a combination of these individual measures. For a given set in the partition, the purity is 0 if each class has equal weight and 100 if every record belongs to the same class. Similarly, the cumulative purity will be 0 if each set in the partition has an equal representation of classes and 100 if each set in the partition contains record that all have the same class [8].

In our case, we use this method to find the best attributes for discriminating the LOC-bin label. We searched for the four best attributes. The attributes found by means of the Mineset tool [8] were RELA-TION, NTRNSMKII, OPT<sup>\_</sup>MENU and OUTMKII, and the cumulative purity was 95.9. These attributes were used in the refinement of the association rules.

## 5. Association rules and unexpectedness

Methods for rule discovery are well known and widely used in many domains. However, most of the existing algorithms have the drawbacks that they discover too many patterns, which are either obvious or irrelevant. Padmanabhan and Tuzhilin have developed ways to generate useful patterns by incorporating managers’ prior knowledge in the process of searching for patterns in data. They generate unexpected patterns with respect to managerial intuition and use them to refine domain knowledge [10]. Recently, they have proposed an iterative refinement process in which it is possible to search through all possible rules [11]. In this work, we use the concept of unexpected patterns to refine association rules, but not their meaning nor their elicitation process. Another difference is the application domain, which provides us with another kind of attributes. Padmanabhan and Tuzhilin manage atributes from the business area, most of which are nominal. We use continuous attributes because they come from the application of software metrics. This fact adds the problem of choosing the best way to partition the range of values of the attributes. We explained how to solve it in the section three.

For example, rules obtained from supermarket transactions may indicate patterns such as ‘‘shoppers who buy diapers on Friday tend to buy beer too’’ (IF diapper, friday THEN beer). Rules generated in the context of the present study are different because they establish correlations between intervals of values of the attributes. A representative rule of this area can be: IF UFPMKII = 120 – 195 THEN LOC = 2168 – 3578. Otherwise, in Ref. [10], the intuition of the business managers is exploited to obtain domain knowledge. In the project management environment, this is very difficult. The experience of the managers in previous projects is insufficient to predict numeric correlations between project attributes or to detect unexpected correlations. It is necessary to resort to mathematical methods.

The aim of this work is not to improve the Padmanabhan and Tuzhilin approach but to propose a different way of knowledge refinement that can be applied in the project management context. Besides, the rule refinement process is simplified due to the use of the best attributes for classification (importance of columns). The procedure provides managers with high confidence rules that show correlation between project attributes obtained early in the life cycle and the size of the final software product. That information is critical in order to take decisions about scheduling and resource allocation.

Now, we introduce the basis of decision rules and the concepts of unexpectedness given in Ref. [11]. A set of discrete attributes $A t { = } \{ a _ { 1 } , a _ { 2 } , . ~ . ~ . , a _ { m } \}$ is considered. Let $D { = } \{ T _ { 1 } , T _ { 2 } , . . . . , T _ { N } \}$ be a relation consisting on N transactions $T _ { 1 } , . . . . T _ { N }$ over the relation schema $\{ a _ { 1 } , a _ { 2 } , . . . , a _ { m } \}$ . Also, let an atomic condition be a proposition of the form value<sub>1</sub>VattributeVvalue<sub>2</sub> for ordered attributes and attribute=value for unordered attributes, where value, value and value belong to the set of distinct values taken by attribute in D. Finally, an itemset is a conjunction of atomic conditions. In Ref. [11], rules and beliefs are defined as extended association rules of the form X!Y, where X is the conjunction of atomic conditions (an itemset) and Y is an atomic condition. The strength of the association rule is quantified by the following factors.

## Confidence or predictability

A rule has confidence c if c% of the transactions in D that contain X also contain Y. A rule is said to hold on a dataset D if the confidence of the rule is greater than a user-specified threshold value which is usually greater than 50%.

## Support or prevalence

The rule has support s in D if s% of the transactions in D contain both X and Y.

## Expected predictability

This is the frequency of occurrence of the item Y. So the difference between expected predictability and predictability (confidence) is a measure of the change in predictive power due to the presence of X [8].

In Ref. [10], unexpectedness is defined by starting with a set of beliefs that represent knowledge about the domain. A rule A ! B is defined to be unexpected with respect to the belief X ! Y on the database D if the following conditions hold:

B and Y logically contradict each other (B AND YA = FALSE);

A AND X holds on a ‘‘large’’ subset of tuples in D;

The rule A, X ! B holds.

For example, a belief X ! Y is that professionals tend to shop more on weekends than on weekdays (Professional ! Weekend). The rule December ! Weekday is unexpected with respect to that belief if:

Weekend AND Weekday A = FALSE.

Professional and December holds on a large subset of tuples on the database.

The rule Professional, December !Weekday holds.

Given a belief and a set of unexpected patterns, Padmanabhan and Tuzhilin refine the belief using the discovered unexpected patterns. In the same paper they demonstrate formally that the refined rules have more confidence than the original ones.

## 6. Refinement process

The refinement of association rules provides managers with more confident rules and allows them to solve conflicts between rules. In Ref. [10], the beliefs can either be obtained from the decision maker or induced from the data using machine learning methods. In our case, those beliefs are based on prior knowledge from previous research, but they were generated from the historical data of projects by an association rule algorithm [8]. In an earlier work [9], we have used several visualization techniques and classification methods, such as decision trees and decision tables, to build and validate models for software size prediction. We found that the function points of the method Mark II (UFPMKII) play an important role in the prediction of lines of code (LOC), but the induction of accurate estimation models requires a great number of attributes. The association rules technique and the refinement procedure proposed in this paper allow us to reduce the number of attributes needed.

Given that the earlier study showed that MKII function points (UFPMKII) are good software size predictors, we decided to start with a set of beliefs, which relate lines of code with UFPMKII. Furthermore, many software size estimation methods [1,4,13] measure the system functionality by means of function points. The initial beliefs were generated applying an association rules technique to the available data from 42 software projects. Then we search for unexpected patterns that could help us to increase the confidence or to solve ambiguities or inconsistencies between the rules representing the beliefs.

The refinement process fits into a generic iterative strategy [11]. Each iteration consists of three steps:

1. Pattern generation procedure: generation of unexpected patterns for a belief.

2. Selection procedure: selection of a subset of unexpected patterns that will be used to refine the belief.

3. Refinement procedure: refining the belief using selected patterns.

The process ends when no more unexpected patterns can be generated. The beliefs are checked at the end of each iteration in order to know if they have acceptable support and confidence.

This generic refinement strategy can be viewed as a broad framework that can allow for a large number of different refinement approaches. We have instantiated this generic strategy and created a specific refinement process. The steps to be taken are described below:

1. Obtain the best attributes for classification and create the sequence: $\mathit { s e q A } = \langle A _ { k } \rangle , k { = } 1 . . . t$ (t: number of attributes). The attributes in the sequence are ordered from greater to lesser purity.

2. Split the continuous values of each attribute into discrete intervals. The intervals of values of the attribute $A _ { k }$ are represented as $\{ V _ { k , l } \} , l = 1 . \ . \ m$ (m: number of intervals).

3. Set $k = 1$ and establish the minimal confidence $c _ { \mathrm { m i n } }$ and minimal support $s _ { \mathrm { m i n } } .$

4. Generate initial beliefs with confidence $c \geq c _ { \mathrm { m i n } }$ and support $s \geq s _ { \mathrm { m i n } } .$

5. Select beliefs with confidence near $c _ { \mathrm { m i n } }$ or with conflicts between each other: Let $X _ { i } \longrightarrow Y _ { i }$ and $X _ { j } \longrightarrow Y _ { j }$ be two beliefs, $R _ { i }$ and $R _ { j } ,$ respectively. There is a conflict between $R _ { i }$ and $R _ { j }$ if $X _ { i } = X _ { j }$ and $Y _ { i } { \neg } { = } Y _ { j } .$

6. With the selected beliefs create the rule set set $ R { = } \{ R _ { i } \} , i { = } 1 . . . n$ (n: number of selected beliefs)

7. For all beliefs $R _ { i } { \in } \mathrm { s e t } R$ do:

7.1. Use the values $\{ V _ { k , l } \}$ of the attribute $A _ { k }$ for generating unexpected pattern fulfilling conditions of unexpectedness and confidence $\geq$ $c _ { \mathrm { m i n } } .$ The form of the patterns is: $V _ { k , l } \longrightarrow B$

7.2. Refine the beliefs by searching for rules R like:

$$
X _ {i}, V _ {k, l} \rightarrow B \text {   and   } X _ {i}, \neg V _ {k, l} \rightarrow Y _ {i}.
$$

7.3. Let setRVbe the set of refined rules, then the beliefs refined in step 7.2 should be added to it: set ${ \cal R } ^ { \prime } { = } \mathrm { s e t } { \cal R } ^ { \prime } \cup \{ { \cal R } _ { u } ^ { \prime } \} , u { = } 1 . . . f$ ( f: number of refined rules obtained in the iteration i).

8. Set k = k + 1 and setR = setRV.

9. Repeat steps 7 and 8 until no more unexpected patterns can be found.

The principal feature of our approach is the gradual generation of the unexpected patterns by taking a single attribute in each iteration. We take advantage of knowledge of good attributes for classification (see Section 4) and use them progressively, beginning with the best. This simplifies the selection of patterns and the refinement process.

Rules representing the beliefs were generated and visualized by using Mineset, a Silicon Graphics tool [8]. The initial beliefs are used to seed the search for unexpected patterns. Fig. 3 is a graphical representation of first rules on a grid landscape with left-hand side (LHS) items on one axis, and right-hand side (RHS) items on the other. Attributes of a rule (LHS ! RHS) are displayed at the junction of its LHS and RHS item. The display includes bars, disk and colors whose meaning is given in the graph.

![](/api/attachments/ZMYZGDVH/fulltext/images/bcff1343bf37d285212fbfa824b584bab6e8b689cb6ad74beb71624d61929bf3.jpg)  
Fig. 3. Rules representing the initial beliefs.

Rules generator does not report rules in which the predictability (confidence) is less than the expected predictability, that is, the result of dividing predictability by expected predictability (pred<sup>\_</sup>div<sup>\_</sup>expect) should be greater than one. Good rules are those with high values of pred<sup>\_</sup>div<sup>\_</sup>expect. We have also specified a minimum predictability threshold of 50%.

Table 1 contains numeric information about the represented rules. We have extracted the rules with UFPMKII in the left-hand side because UFPMKII serve as predictors of LOC. Relations in the opposite sense are not of interest.

The plot and the table show that good rules are in two software size intervals. When LOC>4987 the rule confidence is 75%, support 7.14% and pred<sup>\_</sup>div<sup>\_</sup>espect 10.50. When LOC < 2168 confidence is 100%, support 28.57 and pred<sup>\_</sup>div<sup>\_</sup>expect 2.10. There are less transactions with high values of LOC than with low values, this fact influences the lower value of suppor for LOC>4987.

<table><tr><td>X (UFPMKII)</td><td>Y (LOC)</td><td>Confidence (predictability)</td><td>Support (prevalence)</td><td>Expected predictability</td><td>Pred_div_ respect</td></tr><tr><td>420</td><td>&gt;4987</td><td>75</td><td>7.14</td><td>7.14</td><td>10.50</td></tr><tr><td>245–295</td><td>3578–4987</td><td>50</td><td>4.76</td><td>11.90</td><td>4.20</td></tr><tr><td>245–295</td><td>2168–3578</td><td>50</td><td>4.76</td><td>33.33</td><td>1.50</td></tr><tr><td>190–245</td><td>2168–3578</td><td>50</td><td>9.52</td><td>33.33</td><td>1.50</td></tr><tr><td>120–195</td><td>2168–3578</td><td>50</td><td>16.67</td><td>33.33</td><td>1.50</td></tr><tr><td>120–195</td><td>&lt;2168</td><td>50</td><td>16.67</td><td>47.62</td><td>1.05</td></tr><tr><td>&lt;120</td><td>&lt;2168</td><td>100</td><td>28.57</td><td>47.62</td><td>2.10</td></tr></table>

Intermediate rules are weak because they have low confidence and show confused correlations between UFPMKII and LOC. Two conflicts that can be observed are the following:

1. UFPMKII: 120–195 ! LOC < 2168;

UFPMKII: 120–195 ! LOC: 2168–3578

2. UFPMKII: 245 –295 ! LOC: 2168– 3578; UFPMKII: 245–295 ! LOC: 3578–4987

We take these rules (beliefs) to explain the refinement process that we propose. The beliefs selected are those with confidence = 50%. The refinement process is applied to each belief.

Taking as the first belief (X ! Y ):

X ! Y If UFPMKII: 120– 195 then LOC < 2168 (confidence = 50%, support = 16.67, pred<sup>\_</sup>div<sup>\_</sup>expect = 1.05)

To refine that belief we take steps 7.1 and 7.2 of the proposed algorithm:

7.1. Generation of unexpected patterns (V ! B): We select the best attribute for classification A<sub>1</sub> according to the procedure explained in Section 4 (importance of columns). In this case, the best attribute is RELA-TION. It is used to search for rules with LHS fulfilling the condition: LOC <sub>z</sub> 2168. The potential unexpected patterns are shown in Fig. 4. The following rule is a unexpected pattern with respect to the belief:

If RELATION: 62 – 90 then LOC 2168– 3578

Other possible patterns are the following, but they are not unexpected patterns because the rule V, X ! B does not hold.

If RELATION: 90–153 then LOC 3578–4987 If RELATION>153 then LOC>4987

The unexpected patterns that we choose are used to solve the conflicts between beliefs. They should have a minimum predictability of 50%. In this example, there is only one pattern to be selected:

If RELATION: 62–90 then LOC 2168–3578

7.2. Refinement procedure. The belief is refined by searching for rules with the form X, V ! B and X, IV ! Y. These are the rules obtained:

X, V ! B If UFPMKII: 120 –195 and RELATION: 6 2 – 9 0 t h e n L O C : 2 1 6 8 – 3 5 7 8 ( c o n - fidence = 100%, support = 9.52%, pred<sup>\_</sup>div<sup>\_</sup> expect = 3)

X, IV ! Y If UFPMKII: 120–195 and RELA-TION: < 62 then LOC < 2168 (confidence = 70%, support = 16.67%, pred<sup>\_</sup>div<sup>\_</sup>expect = 1.47)

![](/api/attachments/ZMYZGDVH/fulltext/images/43d66f2d37175c08cb9cc6d722233a9af4f27740498df5b9ede8dd29736e2fbf.jpg)  
Fig. 4. Potential unexpected patterns in the first iteration.

Note the significant increase in the confidence and in pred<sup>\_</sup>div<sup>\_</sup>expect. The two refined rules have 100% and 70% of confidence, respectively, since the belief (If UFPMKII: 120 –195 then $\mathrm { L O C } < 2 1 6 8 )$ has a confidence of 50%. Therefore, in the first iteration, the following conditions hold:

$$
\begin{array}{l} c (X, \neg V \to Y) > c (X \to Y) <   c (X, V \to B), \\ c: \text { confidence } \end{array}
$$

The remaining beliefs are treated by carrying out the same steps. The process is iterative. Refined beliefs are the input to the next iteration. In that iteration, new unexpected patterns are generated by taking another good attribute (the following best attribute) from classification models. The refinements obtained in the first iteration can be seen in Fig. 5.

In the second iteration, the attribute $A _ { 2 }$ selected to find the unexpected patterns is NTRNSMKII. A belief to be refined in that iteration is:

X ! Y If UFPMKII: 120–195 and RELATION < 62 then LOC < 2168 (confidence = 70%, support = 16.67%, pred<sup>\_</sup>div<sup>\_</sup>expect = 1.47)

The only unexpected pattern with respect to NTRNSMKII is:

If NTRNSMKII: 28–38 then LOC: 2168–3578

The refined beliefs are:

X, V ! B UFPMKII: 120 –195, RELATION < 62, NTRNSMKII: 28 –38 Z LOC: 2168– 3578 (confidence: 100%, support: 2.38%, pred<sup>\_</sup>div<sup>\_</sup>expect: 3)

$X , \lnot V { \longrightarrow } Y$ UFPMKII: 120–195, RELATION: < 62, NTRNSMKII: 18–28 Z LOC < 2168 (confidence: 75%, support: 7.14%, pred<sup>\_</sup>div<sup>\_</sup>expect: 1.57) UFPMKII: 120 – 195, RELATION: < 62, NTRNSMKII < 18 Z LOC < 2168 (confidence: 80%, support: 9.5%, pred<sup>\_</sup>div<sup>\_</sup>expect: 1.68)

In all cases, confidence and pred<sup>\_</sup>div<sup>\_</sup>expect of the refined beliefs are greater than the original beliefs. In this iteration, the conditions $c ( X , \neg V \to Y ) { > } c ( X \to Y ) <$ $c ( X , V \longrightarrow B )$ also hold. Therefore, we have demonstrated empirically that the rules are stronger after the process of incremental refinement.

The iterative process can continue if more unexpected patterns can be generated by taking de following best attribute.

## 7. Conclusions

Due to the interest that the estimation of the software size has in the first stages of the project, we have studied the relation between early software size measures as the function points and measures of the final product as the lines of code. In this work, we have presented the results obtained by using knowledge discovery-driven techniques. The goal is to generate strong association rules between attributes that can be obtained early in the project and the final software size. To do that, we have instantiated a rule refinement framework [11] based on discovering unexpected patterns for a belief. In this way, we have created a specific process that is very appropriate for solving problems in the project management area. Our approach introduces some features that simplify the refinement process and solve some problems such as the use of domain knowledge.

![](/api/attachments/ZMYZGDVH/fulltext/images/9fb098a9264b2893242b58c8caf479a06c99c975d5009f979586c98168476b79.jpg)  
Fig. 5. Refined beliefs in the first iteration.

The main aspects of our proposal are the following ones.

Data clustering is used for partitioning the values of continuous attributes into a suitable number of intervals. The best partition was obtained from the study of the distribution of attribute values in each cluster.

The identification of weak rules representing beliefs and conflicts between them is the starting point to the iterative refinement process.

The generation of the unexpected patterns is gradual, by taking a single attribute in each iteration. We use information about good attributes for classification and take them progressively, beginning with the best. This simplifies the selection of patterns and the refinement process because the number of patterns generated in each iteration is less.

## References

[1] A.J. Albrecht, Measuring application development, Proc. IBM Applications Development Joint SHARE/GUIDE Symposium, Monterey, CA, 1979, pp. 83 – 92.

[2] B.W. Boehm, B. Clark, E. Horowitz, et al., Cost models for future life cycle processes: COCOMO 2.0, Annals Software Engineering 1 (1995) 1 – 24.

[3] P. Cabena, P. Hadjinian, R. Stadler, J. Verhees, A. Zanasi, Discovering Data Mining, Prentice Hall, Upper Saddle River, NJ, 1998, from concept to implementation.

[4] J.J. Dolado, A validation of the component-based method for software size estimation, IEEE Transactions on Software Engineering 26 (10) (2000) 1006– 1021.

[5] J. Grabmeier, A. Rudolph, Techniques of cluster algorithms in data mining, Data Mining and Knowledge Discovery 6 (2002) 303– 360.

[6] B. Hall, G. Orr, T.E. Reeves, A technique for function

block counting, Journal of System and Software 57 (2001) 217– 220.

[7] H. Liu, F. Hussain, C.L. Tan, M. Dash, Discretization: an enabling technique, Data Mining and Knowledge Discovery 6 (2002) 393–423.

[8] Mineset user’s guide, v. 007-3214-004, 5/98, Silicon Graphics, 1998.

[9] M.N. Moreno, L.A. Miguel, F.J. Garcı´a, M.J. Polo, Data mining approaches for early software size estimation, Proc. 3rd ACIS International Conference on Software Engineering, Artificial Intelligence, Networking and Parallel/Distributed Computing (SNPD’02), Madrid, Spain, 2002, pp. 361 – 368.

[10] B. Padmanabhan, A. Tuzhilin, Knowledge refinement based on the discovery of unexpected patterns in data mining, Decision Support Systems 27 (1999) 303 – 318.

[11] B. Padmanabhan, A. Tuzhilin, Unexpectedness as a measure of interestingness in knowledge discovery, Decision Support Systems 33 (2002) 309–321.

[12] C.R. Symons, Software Sizing and Estimating MKII FPA, John Wiley & Sons, New York, 1991.

[13] J. Verner, G. Tate, A software size model, IEEE Transaction of Software Engineering 18 (4) (1992) 265– 278.

![](/api/attachments/ZMYZGDVH/fulltext/images/ad33e3b34640b9c2eb0b9fc9045a46dedc95d445d6a1e26f048439246b41a98f.jpg)  
Marı´a N. Moreno is Associate Professor of Computer Science at the University of Salamanca, Spain. She received her PhD from Salamanca University in 1988. She is a member of the ‘‘Data Mining and Automatic Learning’’ Spanish research group and the Adaptive Web Engineering Group (AWEG). Her research interests are in the areas of data mining, software metrics and Web engineering.

![](/api/attachments/ZMYZGDVH/fulltext/images/77bdaf7da6851718006d79bd12faffb34442c258e902b2d6677f34e7891ed74e.jpg)

Luis A.M. Quintales is Associate Professor of Computer Science at the University of Salamanca, Spain, which he joined in 1992. He is a member of the ‘‘Data Mining and Automatic Learning’’ Spanish research group. His research interests include data mining, parallel algorithms and distributed systems.

![](/api/attachments/ZMYZGDVH/fulltext/images/cf3840cd2a0af4097606bcac5fa7c20bae78be66d3e115e7f465bf754d41399f.jpg)

Francisco J. Garcı´a received his PhD in Computer Science from the University of Salamanca, Spain, in 2000. He is a Professor of the Informatics and Automatic Department of the University of Salamanca, Spain. He is the Director of the Adaptive Web Engineering Group (AWEG) research group. Dr. Garcı´a’s research interests include Web Engineering and Software Reuse.

![](/api/attachments/ZMYZGDVH/fulltext/images/e867137b39980130c6e1c51c35f9a4919b5c5c19b5976e0f50e7489f3deb99bf.jpg)  
M. Jose´ Polo Martı´n is Associate Professor of Computer Science at the University of Salamanca, Spain. She is a member of the ‘‘Data Mining and Automatic Learning’’ Spanish research group. Her research interests are data mining and distributed systems.
