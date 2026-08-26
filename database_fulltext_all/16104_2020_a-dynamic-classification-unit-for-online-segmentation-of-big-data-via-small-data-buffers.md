---
otero_id: 16104
otero_key: "YNTXU2UK"
title: "A dynamic classification unit for online segmentation of big data via small data buffers"
authors: "Anna Khalemsky; Roy Gelbard"
year: "2020"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2019.113157"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A dynamic classification unit for online segmentation of big data via small data bufers

Anna Khalemsky, Roy Gelbard

Information Systems Program, Graduate School of Business Administration, Bar-Ilan University, Ramat Gan 5290002, Israel

A R T I C L E I N F O

Keywords: Incremental dynamic classifier Dynamic segmentation Incremental data analysis Cluster analysis Classification Big data

## A B S T R A C T

In many segmentation processes, we assign new cases according to a model that was built on the basis of past cases. As long as the new cases are “similar enough” to the past cases, segmentation proceeds normally. However, when a new case is substantially diferent from the known cases, a reexamination of the previously created segments is required. The reexamination may result in the creation of new segments or in the updating of the existing ones. In this paper, we assume that in big and dynamic data environments it is not possible to reexamine all past data and, therefore, we suggest using small groups of selected cases, stored in small data bufers, as an alternative to the collection of all past data. We present an incremental dynamic classifier that supports real-time unsupervised segmentation in big and dynamic data environments. In order to reduce the computational efort of unsupervised clustering in such environments, the suggested model performs calculations only on the relevant data bufers that store the relevant representative cases. In addition, the suggested model can serve as a dynamic classification unit (DCU) that can act as an autonomous agent, as well as collaborate with other DCUs. The evaluation is presented by comparing three approaches: static, dynamic, and in cremental dynamic

## 1. Introduction

The field of knowledge discovery and data processing is not trivial in the era of big data. It has become a very important part of organizations' constant attempts to expand their intangible assets and to achieve a competitive advantage through real-time data analysis of data collected from diferent sources. A variety of practical data-mining algorithms have been adapted to a wide range of real-life problems [1,2]. Fayyad and Stolorz wrote in 1997 that “databases are growing in size to a stage where traditional techniques for analysis and visualization of the data are breaking down” [3]. In the past two decades their statement has come to appear in a brand new light. As a result of the en: ormous increase in data volume in that period and the increase in organizations' expectations and requirements for obtaining a relative advantage, one of the important ways to approach data processing is to understand the similarities between diferent segments (customers, products, events, etc.). This procedure incurs high processing costs and algorithmic instability. That is why the search for similarities calls for the development of new eficient and robust methods [4].

One of the main goals of data mining and knowledge discovery is the segmentation of cases into homogeneous groups. The literature uses several terms for the diferent segmentation tasks, such as “supervised classification” and “unsupervised clustering” [5]. The term “classification” is used in situations in which a target attribute is known (labeled data), and “clustering” is used in situations in which the target attribute is unknown. Clustering techniques are divided into two main categories: hierarchical methods, such as Ward's method, which uses a similarity-distance matrix for group formation, followed by a merging of the groups by means of diverse similarity measures [6,7]; and partitional methods, such as the widely used k-means algorithm, which produces clusters by optimizing a criterion function [8,9]. Numerous partitional methods for finding classification rules have been developed and used in the academy and industry. They are adapted to work with diferent data types and are suitable for many business problems [10,11].

The constant growth of data in industry has led to a clear under standing that data-mining tools need to be more compatible with a dynamic data environment [12]. In particular, they need to allow quick analysis, prediction, and decision-making solutions at any given moment by minimizing the analytical resources required for data analysis [13]. In the reality of big and dynamic data environments, which are characterized by a constant flow of new cases that may have existing features as well as new features, where, indeed, the features themselves may be constantly changing, it is impossible to recalculate all the similarities every time a new case appears – even with the most sophisticated hardware and algorithmic tools [14,15]. This problem has led to the development of incremental data analysis. As Siddharth, Chauhan, and Bhandery put it, “Since the amount of data being processed is large, it is important for the mining algorithms to be very computationally eficient. Recently many important applications have created the need of incremental mining” [16].

The literature review presented in Section 2 gives some idea of the complexity of incremental dynamic segmentation and related subjects, such as the analogy between decision trees and clustering, diferent reasoning methodologies, and popular implementation areas. At the same time, it reveals that incremental updating of the segmentation process is growing in popularity due to the increasing use of segmentation tasks in big and dynamic data environments.

In the context of this paper, segmentation is a combination of supervised classification and unsupervised clustering; therefore, we refer to segmentation as “dynamic classification” or “evolving classification.” Since the classifier can act as an autonomous agent, we use the term “dynamic classification unit” (DCU). The novelty of this real-time incremental mechanism is based on the use of small data bufers that store selected representative cases from each segment. In addition to being an autonomous agent, each DCU can synchronously or asyn chronously communicate with other DCUs, even though it may have a unique configuration of parameters. In this way, several DCUs managed by a central controller can solve the complex task of dynamic segmentation of endless cases that may “flow” from diferent sources and information nodes. Upon the appearance of a significantly “unusual” new case, one or more bufers are dynamically rearranged according to segmentation quality criteria. The incremental updating of a specific bufer in one DCU can initiate synchronization of the whole system.

In order to support calibration to diverse domains, the model accommodates diferent forms of processing by using a wide range of parameters (presented in Appendix 1). The decision-making process strictly depends on the user's preferences and/or the implementation requirements. The final product can be either directly analyzed by the user in order to interpret the results or can be processed automatically in the case of a censoring task. The model is designed to handle nu merical attributes, and it is demonstrated and evaluated using three datasets, each of which was selected to demonstrate a specific decisionmaking task: a dataset with ordinal attributes for performance evaluation tasks: and the other two datasets with continuous attributes re presenting quantitative assessments.

## 2. Related work

In many segmentation processes, new cases are classified according to a model that was built on the basis of past cases and known target attributes (labeled data). As long as the new cases are “similar enough” to the past cases, the segmentation proceeds normally. However, when a new case is substantially diferent from the known cases, a reex amination of the previously created segments is required. In many situations, databases do not remain static and, as new data is dynamically added, there is a constant need to update the segmentation rules based on a limited set of representative cases of both old and new data, without reexamining all the past data. This process is called incremental data analysis [16.17]. Periodic analysis of the data is not enough since the dynamic data environment is characterized by constant change. Therefore, new tools for updating and reorganizing data at any given moment are required [16]. The first researchers who dealt with a dy namic data environment adopted existing algorithms that were developed primarily for a static data environment [18]. The history of incremental dynamic analysis starts in the late '90s, when the first density-based spatial clustering algorithm (dbscan) was introduced by Martin Ester [19]. Lately, the idea of using irregularly updated databases has spawned a wide range of studies [20].

The present paper focuses on incremental segmentation of the data stream and dynamic updating of segmentation rules that enable real time segmentation, and provides an efective tool for a big data environment, where reexamination of all the past data is impossible or costly. The paper proposes a segmentation model that does not depend on the existence of a target attribute and can be used with or without a training phase.

The present study taps into many areas at once: dynamic archetypebased reasoning, which is diferent from the widely used rule-based reasoning and case-based reasoning; limited data bufer storage, which is usually applied in computer science; a customized, hybrid approach of decision tree analysis and clustering analysis, which allows us to quantitatively evaluate the product of the clustering process. We describe each one of these areas and its connection to the present study next. Finally, we provide a detailed presentation of the process of incremental data analysis, with reference to the most relevant studies.

2.1. Dynamic archetype-based reasoning vs rule-based reasoning and casebased reasoning; data bufers

Before introducing our new approach, it's important to review two well-known approaches that are very useful in data mining: rule-based reasoning (RBR) [21] and case-based reasoning (CBR). RBR involves a given set of rules and is usually performed by an experienced professional [22]. It can provide very good results, but it usually involves a lag between the time that the control signal is received and the time that the signal's efect is known. RBR is widely used in data-mining applications [23–25]. In CBR, new problems are analyzed on the basis of similar or old problems, by comparing, contrasting, and moving forward from them. Learning is achieved when a new case is added to the previous ones. CBR is very similar to the way people try to solve problems both in daily life and in professional life, such as in medicine, business administration, law, and science [26].

In this paper, we introduce a dynamic approach that incorporates elements of CBR, but in a very stringent way. In order to reduce the computational efort of the segmentation and updating processes that are performed in the ongoing attempt to keep up with new trends that arise in a dynamic data environment, we propose a kind of reasoning that ignores the majority of past data and bases itself on selected cases stored in limited data bufers. Because these selected cases can be regarded as representative archetypes, we call this kind of reasoning dynamic archetype-based reasoning (ABR). An archetype difers from a case (CBR) in that it represents not a specific single case but a “gene pool” that allows for the formation of diverse variations.

Data memory bufers (or “data bufers” for short) are widely used in computer science applications [27]. There are two popular policies in bufer management: FIFO (first in, first out) and LIFO (last in, first out). Under the FIFO policy, as new cases are added to the existing bufer, they displace the oldest cases. One can also implement other policies such as “furthest member,” under which only “extreme” cases (outliers) are stored. In such cases the centroid of each “furthest-member” segment can be regarded as a virtual archetype (as defined above). The use of data bufers can result in a significant reduction of statistical power [28]. The use of data bufers in information technology is beginning to gain traction, e.g., in forecasting problems [29], spatial clustering [30,31], online recommendations [32], and other applications.

The principle of data bufers perfectly suits the need for real-time dynamic segmentation without loss of too much important information. The dynamic classification unit proposed in this paper implements the FIFO policy as well as the “furthest-member” policy. The furthestmember policy ensures high diversity in each data bufer and provides a general “archetype” for each segment, which is consistent with the idea of dynamic archetype-based reasoning (ABR) described in the previous section.

## 2.2. Analogy between decision tree analysis and cluster analysis

Decision tree algorithms are commonly used for purposes of supervised classification. In contrast to other data-mining algorithms, such as neural networks, which are regarded as “black boxes,” decision tree algorithms yield understandable outputs, using content-related terms (the original variables) and values (the original value range of each attribute). However, decision tree algorithms cannot be used in cluster analysis due to the absence of a target attribute.

As mentioned, the model proposed in the present paper uses the concept of unsupervised clustering, where the target attribute is unknown. In order to justify the use of unsupervised clustering, as well as to provide a qualitative basis for evaluating the results of clustering, we next compare the results of cluster analysis and decision tree analysis.

Cluster analysis involves subjectivity in the interpretation of results and, therefore, there is a constant need to justify the interpretation. Gelbard, Goldman, and Spiegler [1] demonstrate that a clustering method that uses diferent algorithms is expected to yield inconsistent results. Consequently, clustering depends on the underlying assump tions of the algorithm in use. Rahman and Verma [33] and Barak and Gelbard [34] combine clustering techniques and classification tasks. Using multiple clusters of classified data, both studies show that a cluster-based classifier can generate an ensemble of classifiers. In a follow-up study, Barak and Gelbard [35] show that clusters present a pattern, just like paths in decision trees, and that the number of leaves can be interpreted as the number of possible clusters. Thus, while it was well known that diferent leaves can belong to the same group, Barak and Gelbard show that diferent clusters can belong to the same group too.

## 2.3. Incremental and dynamic data analysis

In this section we present a brief review of the key studies on the development of incremental clustering techniques (i.e. incremental clustering). We organize this section according to the main problems and goals that we plan to solve; first, we present techniques for the simultaneous division and merging of segments, then incremental methods for discovery and maintenance of associated rules, and then techniques that serve a particular practical implementation, such as diverse sources management or social network analysis.

One strand of the literature on incremental data mining presents techniques for the simultaneous division and merging of cases or groups. For example, Mishra et al. [36] present a segmentation method that improves input/output eficiency by identification of centroids. Lughofer [37] presents a split-and-merge evolving algorithm that compares updated clusters to original clusters using a Bayesian criterion. Correa-Morris, Espinosa-Isidron, and Alvarez-Nadiozhin [38] present a nested incremental distribution technique for static and dy namic databases that competes with classic methods of hierarchical clustering and ofers a sequence of nested clusters, where each division is achieved through a diferent combination of criteria.

One of the most important topics in the literature concerns the development of methods for incremental dynamic discovery and the maintenance and updating of association rules [39,40]. Amornchewin and Kreesuradej [41] present an incremental algorithm for updating association rules based on the principle of using Bernoulli trials to find expected frequent items and to reduce the number of scan iterations. Ariya and Kreesuradej [42] use the same principle and claim that in some situations one can use the normal approximation to estimate the probability of occurrence of an expected itemset. Thomas et al. [43] present an algorithm based on the concept of negative borders (the collection of itemsets that were candidates by the level-wise method but did not have enough support). Specifically, their algorithm uses negative borders to decide when a full scan of previous data is needed, which happens when the negative border of the large itemset expands. The authors define two thresholds – minimum support and confidence – and suggest that an incremental increase in new cases may cause existing groups to shrink or expand significantly. Charikar et al. [44] provide an incremental clustering method, based on an analysis of the requirements of the information retrieval applications, that eficiently maintains and updates clusters after the appearance of each new case. Bouchachia [45] presents a hybrid evolving method for using incremental learning tasks. The method consists of two sequential and incremental learning mechanisms: a growing Gaussian mixture mechanism and a resource-allocating neural network. The model combines labeled and unlabeled data and aims at boosting the accuracy of the segmentation.

Another strand of the literature on incremental dynamic processing focuses on the eficiency of the segmentation process. Hadzicadic [46] uses a decision tree-like construction to improve the eficiency of clustering by reducing the number of nodes.

As diferent technologies become more compatible with each other and begin to cooperate, data can be obtained from diverse sources such as text, audio, and video. The streams of data that flow from these various sources into a single database require a dynamic process for segmentation as well as for profiling or association [47,48]. The aggregate view of the data that arrives from the diferent streams is an important issue in data analysis [49,50]. For example, data streams can be eficiently clustered by subsequences using a window model [51]. The algorithm proposed by Barbosa [52] uses a forgetting function that facilitates complex management of clusters. The DCU model proposed in this paper can successfully deal with diferent data streams simultaneously.

The majority of recent studies are motivated by diferent industry needs, like customer segmentation [53], service innovation [54], transaction classification [2], fraud detection [55], and dynamic sensing data [56,57,69].

Another area with great potential, social network analysis, also uses the idea of incremental dynamic clustering [58,59]. In order to discover the structure of the network' segments, Xia and Tuo [60] propose to give diferent weights to diferent attributes, using a topological graph. In addition, they use a threshold to determine whether an attribute's weight changes significantly. The authors show that the node-by-node approach to updating yields a very ineficient result, and present an alternative, subgraph-by-subgraph approach. Their main objective is to monitor patterns of events in dynamic networks. Held et al. [61] use the Louvain method of community detection to reveal dynamic changes in graphs.

Since this research is mainly motivated by the need for eficiency in segmentation processes, we shall conclude this review of incremental dynamic processing by pointing out the diferences between the proposed method and the previously mentioned methods that are closely related to it. The method developed by Thomas et al. [38] difers significantly from our method since they assume a full scan of all previous data, whereas we assume a scan of only selected cases stored in the relevant data bufers. Hadzicadic [46] focuses on weighted attribute relevance, whereas we use the option of weighted attributes as one of the parameters in the model, but not as the most important parameter. Finally, in contrast to our algorithm, Song et al. [62] use a densitybased algorithm.

## 3. The proposed dynamic classification unit

The proposed dynamic classification unit (DCU) is a mechanism for incrementally updating segmentation rules, based on small data bufers, that can be successfully used in a large, dynamic data environment. It should be recalled that the main assumption of our study is that a dynamic data environment is characterized by a constant “flow” of new cases and no option to recalculate all the past cases each time a new case appears. The DCU uses small data bufers to store selected representative cases from each segment in order to constantly recalculate and update segmentation rules and parameters. In this way, the DCU uses each bufer such that it represents a specific segment.

The proposed DCU consists of two main phases: the initialization phase and the real-time computing phase.

## 3.1. The initialization phase

The DCU does not assume any initial training (i.e., learning) phase and it can start “from scratch,” i.e., with empty bufers and no segmentation rules. The initialization phase is required only in cases where we would like to shorten the training phase of the system, as well as in cases where there is preliminary knowledge about the existing segments. In such cases, for each existing segment, a limited number of representative cases are stored in each bufer, and the dynamic segmentation process is based on a similarity-distance calculation. The bufer's management uses several parameters (such as the distance function and the similarity threshold) that determine whether a new case is similar enough to one of the existing clusters (see Section 3.3 for a discussion of the model parameters and Appendix 1 for the complete list).

## 3.2. The real-time computing phase: assignment of a new case

The assignment of each new case results in one of the following situations:

1) Assigning the new case to one of the existing segments.

2) Splitting an existing segment into two or three homogeneous subsegments and assigning the case to one of them.

3) Creating a new segment for an outlier.

4) Merging multiple segments into one unified segment, if the distance between two or more segments is below a certain threshold.

Table 1 presents the notation used in the paper.

Fig. 1 presents a flow chart that describes the real-time computing phase.

The assignment process consists of the following steps:

Step 1: Calculate the distance between the new case and the centroids of N existing bufers. For simplicity, we use the root-mean square error (RMSE) as the distance measure.

Step 2: According to the threshold δ and $m _ { m i n } ,$ assign $x _ { i }$ to $R _ { \mathrm { m i n } }$ or split $R _ { \mathrm { m i r } }$ or create a new segment.

If $R M S E ( x _ { i } , R _ { m i n } ) \ : < \ : \delta$ assign the new case to segment $R _ { \mathrm { m i n } } .$ Return to step 1 for $x _ { i + 1 } .$

$I f R M S E ( x _ { i } , R _ { m i n } ) \geq \delta ,$ split the closest segment according to $m _ { m i n } \mathrm { . }$

1) If $m _ { m i n } < Z _ { m i n } \ : ( \mathrm { i . e . , } m _ { m i n }$ is too small), x initiates a new segment, the total number of segments becomes $\mathrm { N } + 1$ , and the new segment is numbered according to a sequential numbering technique. Return to step 1 for $\mathbf { X } _ { \mathrm { i + 1 } }$ .

2) If $Z _ { m i n } < m _ { m i n } < Z ( \mathrm { i . e . }$ , the number of cases in the bufer is high enough to justify the split, but lower than the maximal number), split $m _ { m i n }$ into 2 sub-bufers. Proceed to step 3.

3) I $\mathbf { f } ~ Z \leq m _ { m i n } ~ ( \mathbf { i . e . }$ , the bufer contains the maximal number of cases), split $m _ { m i n } = Z$ into 2 sub-bufers. Proceed to step 3.

Step 3: According to the threshold δ, assign x<sub>i</sub> to ${ R _ { m i n } } ^ { ( 1 ) } \operatorname { o r } { { R _ { m i n } } ^ { ( 2 ) } }$ or split $R _ { m i n }$ again into 3 sub-bufers.

If $[ R M S E ( x _ { i } , R _ { m i n } { } ^ { ( 1 ) } ) \cup R M S E ( x _ { i } , R _ { m i n } { } ^ { ( 2 ) } ) ] ~ < ~ \delta ~ ( \mathrm { i . e . } )$ , the distance between the new case and at least one of the centroids of two sub-bufers is below the specified threshold), assign a new case to the most similar subgroup. Return to step 1.

If $[ R M S E ( x _ { i } , R _ { m i n } { } ^ { ( 1 ) } ) \cup R M S E ( x _ { i } , R _ { m i n } { } ^ { ( 2 ) } ) ] \geq \delta \mathrm { ( i . e . }$ , the distance be tween the new case and two centroids is above the specified threshold), split the initial bufer into 3 sub-bufers. Proceed to step 4.

Step 4: According to the threshold δ, assign x<sub>i</sub> to ${ R _ { m i n } } ^ { ( 1 ) } \operatorname { o r } { { R _ { m i n } } ^ { ( 2 ) } }$ or ${ R _ { m i n } } ^ { ( 3 ) }$ or create a new segment.

$\mathrm { I f } \{ R M S E ( x _ { i } , R _ { m i n }  ^ { ( 1 ) } ) \cup R M S E ( x _ { i } , R _ { m i n } { } ^ { ( 2 ) } ) \cup R M S E ( x _ { i } , R _ { m i n } { } ^ { ( 3 ) } ) ] < \delta$ (i.e., the distance between the new case and at least one of the centroids of three sub-bufers is below the specified threshold), assign a new case to the closest subgroup. Return to step 1.

If $[ R M S E ( x _ { i } , R _ { m i n } { } ^ { ( 1 ) } ) \cup R M S E ( x _ { i } , R _ { m i n } { } ^ { ( 2 ) } ) \cup R M S E ( x _ { i } , R _ { m i n } { } ^ { ( 3 ) } ) ] \geq \delta \ ( \mathrm { i . e . , }$ the distance between the new case and three centroids is above the specified threshold), create a new segment. Return to step 1.

Step 5: Merge similar groups.

## 3.3. Model parameters

In order to render the model compatible with diverse domains, as well as to allow for a sensitivity analysis of the results, the model supports 20 parameters, e.g., clustering methods, attribute types, distance measures, bufer policies, etc. A detailed list of parameters is presented in Appendix 1.

## 4. Research method

## 4.1. Preliminary evaluation

As discussed in Section 2, the results of clustering problems (where the target attribute is unknown) may be less accurate than the results of classification problems (where the target attribute is known). The purpose of this section is to examine the possibility that a clustering algorithm can provide results almost as accurate as those of a decision tree. Since each path from the root to a leaf in a decision tree presents classification rules, we have referred in previous work to decision tree paths as clusters and vice versa [34,35]. In those studies, we compared the results of a forced “classification” of clusters to the original values of the target attribute. In this way we were able to measure the accuracy of the clustering as a percentage of well-classified cases, exactly as we would measure the accuracy of a tree classification. Thus, our preliminary evaluation of the clustering algorithm consists of the following steps.

Table 1 Notation.

<table><tr><td> $X_i$ </td><td>New case</td></tr><tr><td>N</td><td>Number of segments at the moment of a new-case assignment</td></tr><tr><td> $RMSE_j j = 1, ..., N$ </td><td>RMSE distance between a new case and the centroids of N existing segments</td></tr><tr><td> $RMSE_{min}$ </td><td>The least distance between a new case and the centroid of the closest segment</td></tr><tr><td> $R_{min}$ </td><td>The closest existing segment to a new case $RMSE_{min} = RMSE(X_i, R_{min}) = \min (RMSE_j)$ </td></tr><tr><td>M. R. N</td><td>Minimal Rule Number: The number of rules in the existing rule set (the unique identifier number of the rule). Each rule is numbered in a hierarchical format in a sequential numbering structure. Each stage is given a time stamp for tracking</td></tr><tr><td> $m_j = 1, ..., N$ </td><td>The number of cases in each one of N existing segments</td></tr><tr><td> $m_{min}$ </td><td>Number of cases in  $R_{min}$  at the moment of a new-case assignment</td></tr><tr><td>δ</td><td>The threshold for immediate assignment</td></tr><tr><td> $Z_{min}$ </td><td>Minimal number of cases in buffer that justifies the updating of the buffer</td></tr><tr><td>Z</td><td>Buffer size</td></tr></table>

![](/api/attachments/YNTXU2UK/fulltext/images/076a29cbc73d860906e9ba58e2e4100dd4bf9b97629ae5b68e6bc8cd4d41f421.jpg)  
Fig. 1. Running phase: Segmentation of new item.

Step 1: Execute decision tree algorithms to determine the number of leaves. In this step, any decision tree algorithm can be used. The data contains the original target attribute. All attributes but the target attribute are normalized using standardization techniques to create a uniform presentation of the diferent kinds of variables. The number of leaves produced by the decision tree and the accuracy of the classification is then registered, where L is the number of leaves and $\pmb { y } = ( \pmb { y } _ { 1 } , \pmb { y } _ { 2 } , . . . , \pmb { y } _ { n } )$ is the target attribute vector. Step 2: Aggregate all leaves with the same target attribute value. All leaves that belong to one of the target attribute values y 1 ≤ i ≤ n are aggregated into one group. The mean vector of all attributes in this group is calculated. Finally, we get n mean vectors, each one with a diferent target attribute value. These vectors are called “tree mean vectors.”

Step 3: Create the required number of clusters according to the number of leaves obtained in step 1. The clustering algorithm (for example, the classic k-means algorithm) is forced to create L clusters (equal to the number of leaves in a classification tree output). The mean vector of all the attributes in each cluster is calculated. The resulting vectors are called “cluster mean vectors.” It is worth mentioning that the target attribute is not involved in this step at all. Step 4: Interpret the clustering results. In order to interpret each of the obtained clusters, the RMSE (root-mean-square error) between each cluster-mean-vector and each tree-mean-vector is calculated. The smallest value is used to associate each of the L clusters with each of the n target attribute values.

Step 5: Compare the accuracy of the results obtained by the decision tree and the results obtained by the clustering algorithm. The original target attribute values are compared with the “interpreted results” (step 4) and the ratio of precise results is calculated. This ratio is compared to the accuracy of the decision tree.

Table 2 shows the results of this preliminary evaluation. They are discussed further in Section 5.1

## 4.2. Evaluation of the proposed model

The proposed model was evaluated using three datasets and different conditions. We used diferent configurations of parameters (presented in Section 3.3 and Appendix 1), mainly bufer size, initial number of segments, threshold level, and standardization technique. Diferent threshold levels (in terms of the RMSE) enabled us to detect significantly “diferent” cases that serve to indicate the formation of a new segment. We expected to find that the final number of segments, as well as the average and standard deviation of the RMSE, depend on the threshold δ (the sensitivity level). As δ rises, the model becomes less sensitive, and fewer cases are expected to exceed the threshold, fewer updates are needed, but more cases fall in the margins of the segments and create a bigger average and standard deviation. In other words, with the less sensitive threshold, it is easier to assign cases, but the assignments are less accurate. Some of the new cases are close to the bufer's centroid, while others are relatively far. The RMSE average shows the distance to the group's center and the standard deviation shows the level of diversification.

Table 2  
Analogy between decision tree analysis and cluster analysis.

<table><tr><td>Experiment #</td><td>Dataset (normalized/standardized)</td><td>Tree algorithm</td><td>Tree accuracy</td><td>Number of segments</td><td>Cluster accuracy</td></tr><tr><td>1</td><td>Lev - normalized</td><td>J 48</td><td>60.4%</td><td>65</td><td>49.5%</td></tr><tr><td>2</td><td></td><td>REPTree</td><td>60.1%</td><td>30</td><td>52.3%</td></tr><tr><td>3</td><td></td><td>Random Forest</td><td>62.8%</td><td>90</td><td>47.6%</td></tr><tr><td>4</td><td>Occupancy - normalized</td><td>J 48</td><td>99.2%</td><td>42</td><td>94.44%</td></tr><tr><td>5</td><td></td><td>REPTree</td><td>99.01%</td><td>40</td><td>94.43%</td></tr><tr><td>6</td><td></td><td>Random Forest</td><td>99.2%</td><td>186</td><td>93.53%</td></tr><tr><td>7</td><td>Occupancy - standardized</td><td>J 48</td><td>99.22%</td><td>42</td><td>86.43%</td></tr><tr><td>8</td><td></td><td>REPTree</td><td>99.09%</td><td>40</td><td>86.37%</td></tr><tr><td>9</td><td></td><td>Random Forest</td><td>99.16%</td><td>183</td><td>87.04%</td></tr><tr><td>10</td><td>deepScapulaSSM - normalized</td><td> $J\ 48^a$ </td><td>88.279%</td><td>117</td><td>72.11%</td></tr></table>

<sup>a</sup> Pruning of original tree was relevant for J48 algorithm only.

## 4.3. Tools and data

The proposed model was evaluated using three datasets: Lev, Occupancy-Detection, and deepScapulaSSM. The datasets represent typical examples of diferent segmentation tasks. The Lev dataset [63] contains examples of anonymous student evaluations of lecturers, conducted at the end of MBA courses. Before receiving their final grades, students were asked to evaluate their lecturers according to four criteria, such as verbal skills and contribution to professional/general knowledge. The single output is a total evaluation of the lecturer's performance. All input and output attributes are ordinal. The dataset includes 4 input attributes and 1 output attribute and 1000 records. All attributes have ordinal values. UCI's Occupancy-Detection dataset [64–66] is a time series and includes 20,560 records and contains 5 input attributes, such as room temperature, humidity, CO<sup>2</sup> level, etc. The output attribute is ground-truth occupancy (1 – occupied, 0 – not occupied). All attributes have continuous values. Kaggle's deepScapu laSSM dataset was downloaded from the Kaggle machine-learning repository [67]. The dataset includes 100,000 records that represent Scapula features and contains 10 main input attributes. One of the in dependent attributes had an extremely strong correlation to the target attribute (the tilt category), and so it was excluded from the final experiments. All attributes have continuous values.

The classification (decision trees) and the clustering (k-means algorithm) were done using Weka version 3.7.11 [68], which is a collection of machine-learning algorithms for data-mining tasks. The RMSE calculation and comparison was done using Microsoft Excel 2013. The entire process was subsequently programmed in Python to enable additional features (such as sensitivity analysis) as well as better performance.

## 5. Results and discussion

The results are presented and discussed as follows. Section 5.1 describes the results of the preliminary evaluation (as presented in Section 4.1). Section 5.2 presents the convergence of the model's results. Section 5.3 evaluates the model's eficiency. Section 5.4 presents the validation of the incremental approach in comparison to the dynamic approach. Section 5.5 describes the model's results when it is activated without a training phase.

5.1. Interpretation and evaluation of clustering results compared to decision tree results

As mentioned in Section 4.1, we performed a pre-test in which clustering results were compared to decision tree results in order to evaluate the ability of clustering algorithms to achieve good results, despite the fact that these algorithms use unlabeled data (i.e., the target attributes are unknown). Three diferent decision tree algorithms, which are available in Weka 3.7.11 software, were used for the Lev and Occupancy-Detection datasets: J48, REPTree, and Random Forest, while J48 was used for the deepScapulaSSM dataset.

The following example demonstrates the way we executed this technique on the normalized Occupancy-Detection dataset, using J48 as the decision tree algorithm and k-means as the clustering algorithm. The results are shown in the fourth row of Table 2. The target attribute values were “yes”/“no,” the number of leaves provided by the J48 was 42, each leaf was classified as a “yes” or “no” category, and the mean vectors of all attributes of all cases classified as $\mathrm { ^ { * } y e s ^ { \prime \prime } } / \mathrm { ^ { * } n o ^ { \prime \prime } }$ were calculated. The number of clusters provided by the k-means algorithm was adjusted to the number of leaves (42) and for each cluster the RMSE between the centroid and each one of the $" \mathrm { y e s } " / " \mathrm { n o } "$ mean vectors was calculated. In this way we obtained the matrix of 84 RMSE values = 42 clusters × 2 target values. The smaller value of the RMSE determined which clusters could be classified as “yes” or “no.” Finally, the predicted “yes”/“no” results of the cluster analysis were compared to a target variable and the percentage of correctly classified records was our measure of accuracy.

Table 2 summarizes the results of the comparison between decision tree accuracy and clustering accuracy for three datasets. Four experiments are presented: normalized Lev data, normalized and standardized Occupancy-Detection data, and normalized deepScapulaSSM data. The columns report the results on the accuracy of the decision tree algorithms, the number of leaves created by the decision tree algorithms (which is equal to the number of clusters). and the accuracy of the k. means clustering process. It can be seen that the classification of the clustering results was more eficient when the clustering algorithm was forced to learn from the classification tree.

In the Lev dataset, the comparison between the classification process and the clustering process revealed a similar picture. In particular, all three decision tree algorithms and the k-means algorithm provided very poor but consistent accuracy results when the number of clusters was determined according to the number of leaves (60.4% for J48 with 65 leaves compared to 49.5% for k-means with 65 clusters; 60.1% for REPTree with 30 leaves compared to 52.3% for k-means with 30 clusters: 62,8% for Random Forest with 90 leaves compared to 47.6% for kmeans with 90 clusters). The Occupancy-Detection dataset provided very good accuracy results (both for normalized and standardized versions) (normalized: 99.2% for J48 with 42 leaves compared to 94.44% for kmeans with 42 clusters; 99.01% for REPTree with 40 leaves compared to 94.43% for k-means with 40 clusters; 99.2% for Random Forest with 186 leaves compared to 93.53% for k-means with 186 clusters standardized: 99.22% for J48 with 42 leaves compared to 86.43% for k means with 42 clusters; 99.09% for REPTree with 40 leaves compared to 86.37% for k-means with 40 clusters; 99.16% for Random Forest with 183 leaves compared to 87.04% for k-means with 186 clusters). The deepScapulaSSM dataset provided a decision tree with almost 2500 leaves; thus, in order to get a reasonable number of segments, we pruned the tree by defining the minimal number of cases in each leaf at 100. This option was possible for the J48 algorithm only; hence, there are no results to report for REPTree and Random Forest. The comparison between the decision tree algorithm and the clustering algorithm revealed a similar picture: 88.279% for J48 with 117 leaves compared to 72.11% for k-means with 117 clusters. This is a relatively small gap, considering that the cluster analysis did not use a target attribute.

## 5.1.1. Intermediate discussion

As predicted, the clustering algorithm provided less accurate but good results, comparable to those of the diferent kinds of decision tree algorithms. A comparison of the results of the three datasets shows the feasibility of using DCUs in problematic datasets in which even decision tree algorithms cannot provide good results. The results of this feasi bility test of the proposed model's accuracy show that in the absence of target values (i.e., labeled data), we can still rely on clustering algorithms to provide accurate results. This fact corroborates our decision to use the clustering algorithm in our model. The results also confirm the analogy between a cluster and a path in a decision tree, since both the cluster and the path yield very similar segmentation results.

## 5.2. Model convergence and types of outliers

According to the accepted protocol in machine learning, the dataset is divided into a training set and a test set. We use several proportions of training and test sets. In one experiment we use only 10% of the records for the training set. In another experiment the process was performed without any training set at all. While the training set was used to learn and to define the initial clusters (the initialization phase), the test set simulated a new data stream (the running phase). The initial number of segments in each experiment was 10, with a bufer size of 100, and 3 diferent threshold levels of δ. For each new case the decision options were: (1) classify the existing segment; (2) split the existing segment into two or three new sub-segments in the case of reaching a threshold; (3) create a new segment in the case of not reaching a threshold. In other words, a new case is defined as the “seed” of a new segment, because it significantly difers from all existing segments. This case may indicate an outlier as well as a new trend to come.

Figs. 2, 3, and 4 present a comparison of the dynamics of the updating phase at three levels of threshold sensitivity for each of the datasets. The figures illustrate the convergence of the process as long as the model runs on the test set. In each figure, δ separately presents the same picture: multiple updates at the beginning of the process and fewer updates later. At higher levels of δ (less sensitive thresholds), the updating process is relatively idle and updates are less frequent; at lower levels of δ (more sensitive thresholds), the process is very active at the beginning, but slows down as the process continues. The curves with diferent δ do not intersect.

## 5.2.1. Intermediate discussion

Despite the apparent non-representability of the “historic” data, the bufers worked very well as long as the updating process continued. The period between the reexamination points became longer. By using the small data bufers the model still succeeded in capturing the changes in the data and, in particular, the new cases that indicated these changes. The segmentation process converged in all databases, despite the use of partial data for each reexamination.

The results of the experiments are presented in Table 3. The within group distance of each segment was calculated using the RMSE (average and standard deviation). The threshold values for the comparisons were set in the following way: the 90th percentile of the obtained RMSE distribution was taken as a reasonable threshold value. It can be seen that the average RMSE increased in all datasets as threshold δ rose. The higher the δ threshold was, the lower the sensi tivity was, and the fewer the cases that were expected to exceed it. More cases were classified into existing segments, even if they were relatively far from the centroid, which is why the average RMSE increased and the final number of segments remained relatively small. For the Lev dataset, the sensitivity levels were 0.6 (more sensitive), 0.7, and 0.8 (less sen sitive). For $\delta = 0 . 6 ,$ n. of segments = 37 and av. = 0.3179; for δ = 0.7, n. of segments = 24 and av. = 0.4124; for δ = 0.8, n. of segments = 16 and av. = 0.4777. The same tendency was detected in the Occupancy-Detection dataset (for δ = 0.85, n. of segments = 22 and av. = 0.4282; for δ = 0.9, n. of segments = 15 and av. = 0.4817; for δ = 1, n. of segments = 15 and av. = 0.4846). And the deepScapulaSSM dataset revealed the same picture (for δ = 1.5, n. of segments = 35 and av. = 0.5484; for δ = 1.75, n. of segments = 23 and av. = 0.5703; for δ = 2, n. of segments = 15 and av. = 0.5814).

The same tendency was expected in the standard deviation. As δ became less sensitive, the assignments became rougher. Only one δ in the Lev dataset deviated from this expectation: for δ = 0.6 (the smallest threshold in an experiment), the standard deviation was 0.1772 and this value was greater than the standard deviation for δ = 0.7, 0.8. It turns out that we can explain this anomaly. Table 4 shows the assignment of the cases into three types of segments: original segments (created during the training phase and not divided during the process), divided segments (created in cases where the original segment was split into 2 or 3 sub-segments), and new segments (created in exceptional cases). In all datasets it can be seen that the model succeeded in recognizing the third group only for the smallest δ levels, where the sensitivity was high. In the case of the Lev dataset with ordinal attributes, the smallest chosen δ resulted in the creation of a relatively large number of segments, a significant portion of which were outliers. This explains why the standard deviation in this case was larger than expected.

## 5.2.2. Types of outliers

An important point relates to the outliers. The outliers in the context of this research are the cases that exceed the threshold level, and where the attempt to split the closest segment into two or three sub-segments still does not satisfy the threshold demand. These cases force the model to create a new segment. Apparently, there are two possible types of outliers: the first type consists of outliers that later on will succeed in gathering additional cases; the second type consists of outliers that do not succeed in gathering a significant group of new cases. The first type represents the discovery of a new, non-accidental segment in the data stream (a “new trend forerunner”), and the second type represents real outliers. The real outliers still raise the number of segments, and the final number is biased because of them; however, it's very easy to identify the real outliers and to eliminate them from the presentation of the final results if needed. Table 4 presents the number of cases for both types of outliers: a segment is defined as a new trend if at least 20 additional cases are associated with the new segment. It can be seen that only a very sensitive threshold level makes it possible to detect outliers. We plan to study this efect in future research on the identification of new trends.

## 5.3. Model eficiency

The eficiency of the DCU is measured in terms of the running time of the test phase. In order to show the advantages of the incremental dynamic approach, we compared it with its static and dynamic counterparts. First, we formulated an operational definition of each approach in order to clarify the comparison method.

1) The static approach involves a situation of a fixed number of segments with no option for new segments to appear, nor for existing segments to split or merge. Although this approach is a very cheap and easy one in terms of computational efort, it is not flexible and thus isn't suitable for situations in which a dynamic change may occur during the appearance of new cases. Each case is assigned to the closest segment, even if the new case is relatively far from the segment's centroid.

![](/api/attachments/YNTXU2UK/fulltext/images/368526f335b11774fd575e4babd167488baa5f2ec466d347e3d25f7262c801a0.jpg)  
Fig. 2. Occupancy dataset: The convergence of the updating process at diferent threshold levels (initial number of segments = 10).

2) The dynamic approach allows for changes in segmentation (i.e., the splitting [or optionally the merging] of existing segments and the creation of new segments), but at the cost of performing a reexamination of the relevant segment on the basis of all past cases associated with this segment. Thus, the dynamic approach represents a situation in which there is no limit on the buffer size

3) The incremental dynamic approach, presented in this paper, allows for changes in segmentation (i.e., the splitting [or optionally the merging] of existing segments and the creation of new

![](/api/attachments/YNTXU2UK/fulltext/images/ee5af9319017b4446b2add78e72dff4a0ba081b41731862200cc22eee9a0dffe.jpg)  
Fig. 3. LEV dataset: The convergence of the updating process at diferent threshold levels (initial number of clusters = 10).

![](/api/attachments/YNTXU2UK/fulltext/images/930b98fa4c1d359db29d93e7f45058982271c48c5901864e8e62ad7ac8d7c0a3.jpg)  
Fig. 4. deepScapulaSSM dataset: The convergence of the updating process at diferent threshold levels (initial number of clusters = 10).

Table 3  
The dynamic incremental updating of segments, by threshold.

<table><tr><td rowspan="2">Dataset</td><td rowspan="2">δ = threshold</td><td colspan="2">Within-group distance (RMSE)</td><td rowspan="2">Number of segmentsa</td></tr><tr><td>Average</td><td>Std. dev.</td></tr><tr><td>Lev</td><td>0.6</td><td>0.3179</td><td>0.1772</td><td>37</td></tr><tr><td rowspan="2">Initial number of segments = 10</td><td>0.7</td><td>0.4124</td><td>0.1434</td><td>24</td></tr><tr><td>0.8</td><td>0.4777</td><td>0.1579</td><td>16</td></tr><tr><td>Occupancy</td><td>0.85</td><td>0.4282</td><td>0.2092</td><td>22</td></tr><tr><td rowspan="2">Initial number of segments = 10</td><td>0.9</td><td>0.4817</td><td>0.2118</td><td>20</td></tr><tr><td>1</td><td>0.4846</td><td>0.225</td><td>15</td></tr><tr><td>deepScapulaSSMb</td><td>1.5</td><td>0.5484</td><td>0.182</td><td>35</td></tr><tr><td rowspan="2">Initial number of segments = 10</td><td>1.75</td><td>0.5703</td><td>0.202</td><td>23</td></tr><tr><td>2</td><td>0.5814</td><td>0.2115</td><td>15</td></tr></table>

<sup>a</sup> The final segmentation consists of 3 main groups: initial segments based on the training set, segments split into subgroups, and new segments created by cases that couldn't be assigned to any of the existing groups (some of which are defined as outliers and others as forerunners of a new trend). See Table 3 for a detailed picture of all three types of segments.

<sup>b</sup> All tests use 70% of the records for training, unless otherwise specified.

segments), but at a lower cost, since the data bufers are limited in size and can store only selected cases, which serve as archetypes of the cases that belong to each segment. The method for selecting this limited set of representative cases is defined by specific parameters, namely, the FIFO policy, in which only new cases are considered, and the “furthest-member” policy, which stores the most unique items in each segment. Thus, the incremental dynamic approach ensures that the cases stored in the data bufers are very small in number and heterogeneous, and that each reexamination requires a limited computational efort in comparison to the dynamic approach.

Tables 5, $^ { 6 , }$ and Fig. 6 present a comparison of these three approaches executed on the same dataset at the same level of threshold sensitivity. The Occupancy-Detection dataset was used in an experiment where 70% of the records were used for the training set, with 10 initial segments, and a threshold value δ of 0.9. The deepScapulaSSM dataset was used in two diferent experiments, with 70% and 10% training sets, respectively, 10 initial segments, and a threshold of 1.75. The final number of segments is shown, together with the within-group distance measure (RMSE average and standard deviation) of all the segments.

Table 4  
The dynamic incremental updating of segments in a test set.

<table><tr><td rowspan="2">Dataset</td><td rowspan="2">δ = threshold</td><td rowspan="2">Original</td><td rowspan="2">Splits</td><td colspan="2">New segments</td><td rowspan="2">Final number of  $segments^a$ </td></tr><tr><td>Outliers</td><td>New trend</td></tr><tr><td>Lev</td><td>0.6</td><td>41</td><td>217</td><td>23</td><td>19</td><td>37</td></tr><tr><td rowspan="2">Initial number of segments = 10</td><td>0.7</td><td>70</td><td>230</td><td>-</td><td>-</td><td>24</td></tr><tr><td>0.8</td><td>138</td><td>162</td><td>-</td><td>-</td><td>16</td></tr><tr><td>Occupancy</td><td>0.85</td><td>4007</td><td>3772</td><td>11</td><td>770</td><td>22</td></tr><tr><td rowspan="2">Initial number of segments = 10</td><td>0.9</td><td>3637</td><td>4923</td><td>-</td><td>-</td><td>20</td></tr><tr><td>1</td><td>5232</td><td>3328</td><td>-</td><td>-</td><td>15</td></tr><tr><td rowspan="3">deepScapulaSSM Initial number of segments = 10</td><td>1.5</td><td>9433</td><td>20,398</td><td>3</td><td>3</td><td>35</td></tr><tr><td>1.75</td><td>19,612</td><td>10,388</td><td>-</td><td>-</td><td>23</td></tr><tr><td>2</td><td>24,771</td><td>5229</td><td>-</td><td>-</td><td>15</td></tr></table>

<sup>a</sup> Total number of cases in each row is equal to the number of cases in the test set.

Table 5  
Evaluation and eficiency.  
Occupation dataset (Delta = 0.9, Initial number of segments = 10).

<table><tr><td>Evaluation measures</td><td>Static state</td><td>Dynamic state: Unrestricted buffer</td><td>Incremental dynamic state: Buffer size = 100</td></tr><tr><td>Final number of segments</td><td>10</td><td>18</td><td>16</td></tr><tr><td>Average RMSE</td><td>0.5117</td><td>0.4205</td><td>0.41</td></tr><tr><td>Std. dev. (RMSE)</td><td>0.2929</td><td>0.1491</td><td>0.2042</td></tr><tr><td>Running time</td><td>56 s</td><td>154 s</td><td>138 s</td></tr></table>

Finally, the running time is presented in order to evaluate the compu tational efort.

In the Occupancy-Detection dataset the static approach is characterized by significantly high RMSE values (av. = 0.5117, std. = 0.2929), compared to the dynamic approach (av. = 04205, std. = 0.1491) and to the incremental dynamic approach (av. = 0.41, std. = 0.2042). The same tendency is detected in both experiments with the deepScapulaSSM dataset. Specifically, in the 70% training experiment, with 10 final segments under the static approach, av. = 0.5921, std. = 0.2194; with 20 final segments under the dynamic approach av. = 0.5623, std. = 0.1992; with 23 final segments under the incremental dynamic approach, av. = 0.5703, std. = 0.202. In the 10% training experiment, with 10 final segments under the static approach, av. = 0.5934, std. = 0.2182; with 23 final segments under the dynamic approach, av. = 0.5629, std. = 0.2007; with 26 final segments under the incremental dynamic approach, av. = 0.5549, std. = 0.1895.

The reason for this discrepancy is the lack of flexibility of the static approach: to avoid the need to update the existing set of segments, each new case was associated with one of the existing segments, even if the closest segment was relatively far away (high RMSE), and therefore all potential outliers joined the existing segments and raised the average RMSE. If we compare the two dynamic approaches (characterized by a restricted and an unrestricted bufer size, respectively), we can see that the incremental dynamic approach achieves maximal flexibility and computational eficiency at the cost of accuracy.

## 5.3.1. Intermediate discussion

The running time of each experiment provides a good way to evaluate the advantage of the incremental dynamic approach in com parison to the dynamic approach. In the Occupancy-Detection dataset, the static approach, which never reexamines the segmentation set, takes only 56 s, which is 175% faster than the dynamic approach (154 s) and 146.4% faster than the incremental dynamic approach (138 s). The comparison of the dynamic and incremental dynamic approaches is much more important. The incremental dynamic approach is 11.59% faster than the dynamic approach and, as the dataset volume grows, the advantage of using limited data bufers becomes more and more prominent. In the deepScapulaSSM dataset with a 70% training set, the static approach takes 143 s, with is 28.67% faster than the dynamic approach (184 s) and 9.79% faster than the incremental dynamic approach (157 s). The advantage of the incremental dynamic approach over the dynamic approach is 19.74%. In the deepScapulaSSM dataset with a 10% training set, the static approach takes 646 s, which is 33.44% faster than the dynamic approach (862 s) and 18.42% faster than the incremental dynamic approach (765 s). The advantage of the incremental dynamic approach over the dynamic approach is 12.68%.

## 5.4. Model validation: comparison between segmentation under the dynamic and incremental dynamic approaches

In order to validate the proposed incremental dynamic segmentation approach that uses size limited bufers, we compared the resulting segments to those achieved under the dynamic approach that uses unlimited size bufers. We used the Occupancy-Detection dataset. The goal was to show whether the segments achieved under the two approaches are quite similar. Table 7 describes the comparison process.

Each segment is indicated by a number (segment ID); there is no meaning associated with the number itself, except in the case of splitting an existing segment, in such case the digits on the subsequent places indicate the level of splitting. The table rows are numbered for convenience in the following explanations and comparisons. The first two columns show segment ID and the number of cases in each segment, in the dynamic experiment with unlimited bufer size. These results are the baseline for the validation process. The next three columns show the ID of the closest segment in the incremental experiment (with the smallest RMSE between the centroid of the segment and the centroid of a particular segment in the dynamic experiment), the RMSE value, and the number of cases in the segment, respectively. The last three columns show the same properties for the “second best” segment.

The dynamic experiment provided 18 diferent segments: segments 0,1,3,4,5,6,7,8,9 are the segments created during the training phase, segments 2.0 and 2.1 are the sub-segments of segment 2, and segments 8.0 and all subdivisions of 8.1 (8.1.1, 8.1.1.1, etc.) are sub-segments of segment 8. Segment 10 is an outlier. The incremental experiment provided 16 diferent segments that are numbered in a similar way. Of the 16 segments in the incremental experiment, 13 are closely related (i.e., determined to be the best segment) only once to a segment in dynamic experiment, 4are related repeatedly, and three are not related at all (namely, segments 5.0, 6.0, and 6.1.1.1.0). Since all these sub-segments are expected to be close to another sub-segment in the same subdivision, we checked whether the “second best” sub-segment came from the same segment. Lines 9 and 10 demonstrate that the best segment is 5.1 and the second best is 5.0 (the closest expected “relative"). lines 15 and 17 demonstrate that the best segment is 6.1.1.1.1.1 and the second best is 6.1.1.1.0, and lines 16 and 18 demonstrate that the best segment is 6.1.1.1.0 and the second best is 6.1.1.1.1.1. This way all segments in the incremental experiment were found to be related as the best or the second best segment to a particular segment in the dynamic experiment. This was the goal of the validation process.

The diferences in the segmentation products in the two experiments are explained as follows. (1) We used a k-means algorithm which is sensitive to the data order. (2) The incremental experiment used a limited number of cases for each segment (limited to 100), compared to the unlimited number of cases, which could reach thousands, used in the dynamic experiment. (3) The time series example, illustrated by the Occupancy-Detection dataset, demonstrates a situation in which limited bufer size is used and thus part of the trend information could be missing. (4) The diferences between best RMSE and second best RMSE are significantly smaller than the diferences between the third-closest segment and all the rest. (5) Only sub-segments that originate from the same segment, in the incremental experiment, were found as best subsegments to particular sub-segments in the dynamic experiment. If we combine two such sub-segments in the former experiment, the combined segment will always be related as the best segment to the latter experiment.

Evaluation and eficiency.  
deepScapulaSSM dataset (Delta = 1.75, Initial number of segments = 10).

<table><tr><td>Training-test</td><td>Evaluation measures</td><td>Static state</td><td>Dynamic state: Unrestricted buffer</td><td>Incremental dynamic state: Buffer size = 100</td></tr><tr><td rowspan="4">70% training set</td><td>Final number of segments</td><td>10</td><td>20</td><td>23</td></tr><tr><td>Average RMSE</td><td>0.5921</td><td>0.5623</td><td>0.5703</td></tr><tr><td>Std. dev. (RMSE)</td><td>0.2194</td><td>0.1992</td><td>0.202</td></tr><tr><td>Running time</td><td>143 s</td><td>184 s</td><td>157 s</td></tr><tr><td rowspan="4">10% training set</td><td>Final number of segments</td><td>10</td><td>23</td><td>26</td></tr><tr><td>Average RMSE</td><td>0.5934</td><td>0.5629</td><td>0.5549</td></tr><tr><td>Std. dev. (RMSE)</td><td>0.2182</td><td>0.2007</td><td>0.1895</td></tr><tr><td>Running time</td><td>646 s</td><td>862 s</td><td>765 s</td></tr></table>

Validation of segmentation  
Occupation dataset (Delta = 0.9, Initial number of segments = 10, unlimited bufer for dynamic, bufer size = 100 for incremental dynamic).

<table><tr><td rowspan="3">#</td><td colspan="2">Method - dynamic</td><td colspan="6">Method - incremental</td></tr><tr><td rowspan="2">Segment ID</td><td rowspan="2">No. of cases</td><td colspan="3">Best RMSE</td><td colspan="3">Second best RMSE</td></tr><tr><td>Related segment ID</td><td>No. of cases</td><td>RMSE</td><td>Related segment ID</td><td>No. of cases</td><td>RMSE</td></tr><tr><td>1</td><td>0</td><td>2806</td><td>4</td><td>100</td><td>0.0155</td><td>0</td><td>100</td><td>0.7357</td></tr><tr><td>2</td><td>1</td><td>630</td><td>9</td><td>100</td><td>0.0531</td><td>1</td><td>100</td><td>0.9760</td></tr><tr><td>3</td><td>3</td><td>261</td><td>6.0</td><td>100</td><td>1.0902</td><td>6.1.0</td><td>100</td><td>1.1774</td></tr><tr><td>4</td><td>4</td><td>1225</td><td>3</td><td>100</td><td>0.2246</td><td>7</td><td>100</td><td>0.6996</td></tr><tr><td>5</td><td>5</td><td>2258</td><td>1</td><td>100</td><td>0.0858</td><td>8</td><td>100</td><td>0.7462</td></tr><tr><td>6</td><td>6</td><td>3789</td><td>0</td><td>100</td><td>0.0012</td><td>5.0</td><td>71</td><td>0.5926</td></tr><tr><td>7</td><td>7</td><td>591</td><td>8</td><td>100</td><td>0.0097</td><td>1</td><td>100</td><td>0.7957</td></tr><tr><td>8</td><td>9</td><td>2120</td><td>2</td><td>100</td><td>0.0004</td><td>0</td><td>100</td><td>0.7104</td></tr><tr><td>9</td><td>2.0</td><td>3295</td><td>5.1</td><td>100</td><td>0.3531</td><td>5.0</td><td>71</td><td>0.4294</td></tr><tr><td>10</td><td>2.1</td><td>1619</td><td>5.1</td><td>100</td><td>0.7532</td><td>5.0</td><td>71</td><td>0.8412</td></tr><tr><td>11</td><td>8</td><td>931</td><td>6.1.0</td><td>100</td><td>0.1191</td><td>6.0</td><td>100</td><td>0.4191</td></tr><tr><td>12</td><td>8.1.1</td><td>210</td><td>6.1.1.0</td><td>47</td><td>0.3478</td><td>6.1.1.1.0</td><td>100</td><td>0.8467</td></tr><tr><td>13</td><td>8.1.0.0</td><td>118</td><td>6.1.1.0</td><td>47</td><td>0.0311</td><td>6.1.1.1.0</td><td>100</td><td>0.7683</td></tr><tr><td>14</td><td>8.1.0.2.0</td><td>93</td><td>6.1.1.0</td><td>47</td><td>0.3080</td><td>6.1.1.1.0</td><td>100</td><td>0.5908</td></tr><tr><td>15</td><td>8.1.0.2.1</td><td>87</td><td>6.1.1.1.1.1</td><td>99</td><td>0.5054</td><td>6.1.1.1.0</td><td>100</td><td>0.6884</td></tr><tr><td>16</td><td>8.1.0.1.0</td><td>94</td><td>6.1.1.1.1.0</td><td>9</td><td>0.2173</td><td>6.1.1.1.1.1</td><td>99</td><td>0.5339</td></tr><tr><td>17</td><td>8.1.0.1.1</td><td>426</td><td>6.1.1.1.1.1</td><td>99</td><td>0.1126</td><td>6.1.1.1.0</td><td>100</td><td>0.2523</td></tr><tr><td>18</td><td>10</td><td>7</td><td>6.1.1.1.1.0</td><td>9</td><td>0.2848</td><td>6.1.1.1.1.1</td><td>99</td><td>0.9043</td></tr></table>

## 5.4.1. Intermediate discussion

The validation test shows that each segment formed in the dynamic segmentation process, when unlimited bufer size cases are used, is closely related to a particular segment formed in the incremental segmentation process, when only limited number of cases in the data bufer are used. This finding strengthens the argument that the proposed incremental approach succeeds in achieving segmentation results close to those of the dynamic approach.

## 5.5. Model eficiency when no training phase is used

The last experiment examines whether the model converges if it is activated without a training phase. In other words, will it converge in situations where no initial segmentation is provided? The entire Occupancy-Detection dataset of 20,560 cases was used as a test set. Thus, the algorithm had to work without any history to rely on. Fig. 5 illustrates the comparison of two experiments with the same threshold level of 0.9. One experiment uses the initial 10 segments (bufers) and the other experiment starts with no preliminary knowledge. We can see that the two curves converge by the end of the process and behave similarly.

The final number of segments obtained without a training phase is relatively high (34 segments), with an average RMSE of 0.4397. The diference between the final number of segments with and without the training phase is easy to explain: it takes time for the algorithm to learn and to create good representative segments. A large number of additional segments are outliers that remain outliers throughout the process. The segments at the end of the process are a combination of two categories: (1) “real” segments and (2) outlier segments that remained almost inactive until the end the process. The results show that 14 of 34 segments consist of fewer than 100 cases (within a range of 1 to 90 cases) and the other 20 segments consist of more than 100 cases (within a range of 111 to 3193 cases). The number of “real” segments is similar to the final number of segments obtained in the scenario that used the initial 10 segments. These results show that the model can achieve good segmentation without requiring an initial training phase.

## 6. Conclusions and further research

In this paper we presented a model of a dynamic classification unit (DCU) that enables dynamic updating of segments and of segmentation rules using a very small number of representative cases, stored in data bufers. The DCU can be used efectively in a wide range of decisionmaking segmentation tasks. It has twenty parameters that can be used to adjust the classifier to almost every potential use. Due to incremental structure of the classifier, which distinguishes it from existing classifiers, the DCU can be used for real-time processing in a large, dynamic data environment, where new trends can arise and those in charge have to decide whether each unusual case is an outlier or a new trend. In the same way the dynamic segmentation of a time series can be used to detect a real-time trend or kind of anomaly.

In addition, the DCU can act as an autonomous agent, as well as collaborate with additional DCUs (synchronously or asynchronously), even when they each have a unique configuration of parameters and segmentation rules. It thus becomes possible for several DCUs managed by a central controller to solve the complex task of dynamic segmentation of endless cases that may “flow” from diferent sources and information nodes. In this way, the incremental updating of a specific bufer in one DCU can initiate synchronization of the whole system.

The DCU model was demonstrated and evaluated using three datasets. In a pre-test, the clustering ability of the model was evaluated by comparing its results to those obtained by decision trees. This pre-test showed that the model can achieve accurate segmentation despite the fact that it doesn't use labeled data (known target attributes).

The next test demonstrated the advantages of the incremental dynamic approach over non-incremental approaches. The model demonstrated a computational advantage in terms of running time compared to the non-incremental approaches, which reexamine all past data. Further, the incremental dynamic approach and the dynamic approach

![](/api/attachments/YNTXU2UK/fulltext/images/d169c04de8a5cff9c86c55bc048cc455554ab58955c26f1550ece46231cd61ec.jpg)  
Fig. 5. Occupancy dataset: The comparison between convergence of updating process with and without training set (threshold level = 0.9, initial number of clusters = 10).

are very close in terms of accuracy, and so it seems that there is no need for a full recalculation in order to achieve good segmentation results. We managed to show that the updating process converges, and that the need to update and rearrange the segments decreases over time. We proved that the accuracy and processing costs are strongly dependent on the configuration of the main parameters, such as sensitivity level and bufer size. The model can be efective even without any training phase.

To sum up, the proposed DCU is designed to address segmentation problems in a dynamic data environment for fully automated or partly automated decision-making processes. The main assumption, which holds in a wide range of decision-making tasks, is that reexamination of all historical data for purposes of segmentation of the data stream is impossible or prohibitively costly. The trade-of between the benefits of immediate online decision-making and the costs of the resulting in accuracies is subject to the user control.

![](/api/attachments/YNTXU2UK/fulltext/images/f1f27cdcfd23e03365e58f15ba7901c1dc2b44742b7ed59cc1a6a9d96887b9d0.jpg)  
Fig. 6. Occupancy dataset: Comparison between static, dynamic, and incremental dynamic states (delta = 0.9).

Further research is planned in three areas. (1) We aim to adjust the model to textual data, in order to enable its use in social media environments, which pose various segmentation challenges. (2) We aim to study the efects of synchronous and asynchronous communication between autonomous DCUs, as well as between autonomous DCUs and a central controller. (3) Finally, we aim to enable early detection of new trends, based on the capability of the DCU to detect the two types of outliers discussed above: “real” outliers and “new trend forerunners.”

Declaration competing interest

None.

## Acknowledgments

This work was supported in part by a grant from the MAGNET program of the Israeli Innovation Authority, who also funded the patent registration (Ref #69). We also thank Hadassah Academic College for their support to Anna.

Appendix 1. Model Parameters

<table><tr><td>#</td><td>Category</td><td>Parameter Name</td><td>Description</td></tr><tr><td>1</td><td>Attributes</td><td>Attribute Type</td><td>The parameter indicates the type of attribute values: discrete, continuous, categorical, ordinal, etc. The attribute type determines the mode of comparison between different values.</td></tr><tr><td>2</td><td></td><td>Attribute weight</td><td>The parameter allows for assigning different weights to different attributes in cases where one attribute is more or less important than the other one.</td></tr><tr><td>3</td><td></td><td>Normalization/Standardization</td><td>The parameter enables one to determine the basis for comparing different scales of attributes.</td></tr><tr><td>4</td><td>Number of Segments</td><td>Initial Number of Segments</td><td>The parameter indicates the initial number of segments (and their properties) that were created during the training phase.</td></tr><tr><td>5</td><td></td><td>Maximal Number of Segments</td><td>The parameter indicates the option of limiting the final number of segments and of stopping the updating process.</td></tr><tr><td>6</td><td>Buffers</td><td>Buffer Size</td><td>The parameter determines the maximal number of cases stored in each buffer.</td></tr><tr><td>7</td><td></td><td>Buffer Filling Method</td><td>The parameter indicates the way in which buffers are filled during the updating process: (1) FIFO - first in, first out method or (2) Outliers - collecting cases that are far enough from the buffer&#x27;s center. This method increases the chance of successful partitioning of an existing segments.</td></tr><tr><td>8</td><td></td><td>Due Date for Recalculation of Buffer Center</td><td>This parameter enables one to define the time to recalculate the buffer&#x27;s center, since its center changes during the updating process. It can be recalculated every time a new case is added to the buffer or when X % of the buffer population changes.</td></tr><tr><td>9</td><td>Initialization Phase</td><td>Initialization Algorithm</td><td>This parameter indicates the method that is used to create initial segments and their buffers.</td></tr><tr><td>10</td><td></td><td>Threshold Level for Switching between Two Steps</td><td>This parameter determines the threshold level for switching between the initialization phase and the run phase.</td></tr><tr><td>11</td><td>Classification and Updating Phase</td><td>Splitting Algorithm</td><td>This parameter indicates the method for splitting an existing buffer into sub-buffers.</td></tr><tr><td>12</td><td></td><td>Minimal Number of Cases that Justify the Splitting of a Group</td><td>This parameter is used in cases where a new item exceeds the threshold level and causes the existing segment to split into sub-segments. If the number of cases in a buffer is relatively small, the model will skip the splitting step and the case will open a new segment.</td></tr><tr><td>13</td><td></td><td>Number of Subgroups</td><td>This parameter defines the number of sub-segments in the case of a split.</td></tr><tr><td>14</td><td></td><td>Similarity Measure in Splitting Algorithm</td><td>This parameter indicates the similarity/distance-measuring method used in the splitting algorithm (Euclidian distance, Manhattan, etc.)</td></tr><tr><td>15</td><td></td><td>Similarity Index for Classification of Items into Existing Segments</td><td>This parameter indicates the evaluation method for the classification process, including the similarity/distance index to calculate distances between different items or between an item and a segment&#x27;s center (RMSE, etc.)</td></tr><tr><td>16</td><td></td><td>Threshold Level for Classification of a New Item to an Existing Segment</td><td>This parameter indicates the maximal level of the similarity index; each item that exceeds the threshold level causes the existing segments to be updated.</td></tr><tr><td>17</td><td></td><td>Threshold Level for Merging</td><td>This parameter presents the minimal level of distance between segment centers that justifies merging.</td></tr><tr><td>18</td><td></td><td>Maximal Scattering in Buffer</td><td>This parameter is used in the merging phase; it indicates the level of scattering of cases in the buffer.</td></tr><tr><td>19</td><td>Evaluation</td><td>Processing Method</td><td>This parameter indicates the way to recalculate and reflects the scope of the data used for updating under static, dynamic, and dynamic incremental approaches.</td></tr><tr><td>20</td><td>Parallel Processing</td><td>Synchronous/asynchronous use</td><td>This parameter indicates the option of the model to communicate with “a central controller” and/or other agents that act simultaneously.</td></tr></table>

## References

[1] R. Gelbard, O. Goldman, I. Spieger, Investigating diversity of clustering methods: an empirical comparison, Data and Knowledge Engineering 63 (2007) 155–166.

[2] D.W. Cheung, J. Han, V.T. Ng, C.Y. Wong, Maintenance of discovered association rules in large databases: An incremental updating technique, Proceedings of the Twelfth International Conference on Data Engineering, 1996, pp. 106–114, , https://doi.org/10.1109/ICDE.1996.492094.

[3] U. Fayyad, P. Stolorz, Data mining and KDD: promise and challenges, Futur. Gener. Comput, Syst. 13 (1997) 99–115. https://doi,org/10.1016/S0167-739X(97 00015-0.

[4] J. Fan. F. Han, L. Han, Challenges of big data analysis, Natl, Sci, Rey. (2014 293–314.

[5] N. Grira, M. Crucianu, N. Boujemaa, Unsupervised and Semi-supervised Clustering: A Brief Survey, a Review of Machine Learning Techniques for Processing Multimedia Content. (2005).

[6] M.M. Deza, E. Deza, Encyclopedia of Distances, 3rd ed., Springer, 2014.

[7] S.-H. Cha, Comprehensive survey on distance/similarity measures between probability density functions, International Journal of Mathematical Models and Methods in Applied Sciences 1 (2007).

[8] A.K. Jain, M.N. Murty, P.L. Flynn, Data clustering: a survey, ACM Comput. Surv. 31 (1999) 264–323

[9] Zhao Ying, Karypis George, Criterion Functions for Document Clustering: Experiments and Analysis | Karypis Lab, (n.d.). http://glaros.dtc.umn.edu/gkhome node/165 ((accessed September 2. 2018)).

[10] J. Hipp, U. Güntzer, G. Nakhaeizadeh, Algorithms for association rule mining: a general survey and comparison, SIGKDD Explorations Newsletter 2 (2000) 58–64, https://doi.org/10.1145/360402.360421.

[11] X. Fang, O.R.L. Sheng, P. Goes, When is the right time to refresh knowledge dis covered from data? Oper, Res, 61 (2013) 32–44, https://doi,org/10.1287/opre. 1120.1148

[12] S.C. Park, S. Piramuthu, M.J. Shaw, Dynamic rule refinement in knowledge-based data mining systems, Decis. Support. Syst, 31 (2001) 205–222, https://doi.org/10

1016/S0167-9236(00)00132-9.

[13] G. Sreedhar, Web Data Mining and the Development of Knowledge-based Decision Support Systems, IGI Global, 2016.

[14] S. Muthukrishnan, Data Streams: Algorithms and Applications, Now Publishers, 2005. https://doi.org/10.1561/0400000002

[15] S. Guha, N. Mishra, Clustering Data Streams, Data Stream Management, Springer (2016) 169–187 (accessed February 8, 2018), https://link.springer.com/chapter/ 10.1007/978-3-540-28608-0\_8.

[16] S. Shah, N.C. Chauhan, S.D. Bhandery, Incremental mining of association rules: a survey, International Journal of Computer Science and Information Technologies 3 (2012) 4041–4074.

[17] P. Joshi, P. Kulkarni, Incremental learning: areas and methods – a survey, International Journal of Data Mining & Knowledge Management Process 2 (2012) 43–51. https://doi.org/10.5121/jidkp.2012.2504.

[18] J. Gama, Knowledge Discovery from Data Streams, Chapman and Hall/CRC (2010) (accessed August 3, 2016), http://www.crcnetbase.com/doi/book/10.1201/ FBK1439826119

[19] E. Martin, H.-P. Kriegel, J. Sander, M. Wimmer, X. Xu, Incremental clustering for mining in a data warehouse environment. Proceedings of the 24th VLDE Conference, New York, USA, 1998.

[20] E. Kolatch, Clustering Algorithms for Spatial Databases: A Survey, http://citeseerx. ist.psu.edu/viewdoc/download?doi=10.1.1.28.1145&rep=rep1&type=pdf, (2001) , Accessed date: 12 August 2019.

[21] L.A. Zadeh, Outline of a new approach to the analysis of complex systems and decision processes, IEEE Transactions on Systems, Man, and Cybernetics SMC-3 (1973) 28–44, https://doi.org/10.1109/TSMC.1973.5408575.

[22] J.A. Bernard, Use of a rule-based system for process control, IEEE Control. Syst. Mag. 8 (1988) 3–13, https://doi.org/10.1109/37.7735.

[23] A. Ferranti, F. Marcelloni, A. Segatori, M. Antonelli, P. Ducange, A distributed approach to multi-objective evolutionary generation of fuzzy rule-based classifiers from big data, Inf. Sci. 415 (2017) 319–340, https://doi.org/10.1016/j.ins.2017. 06.039.

[24] Q. Madera, O. Castillo, M. García-Valdez, A. Mancilla, A method based on interactive evolutionary computation and fuzzy logic for increasing the efectiveness of advertising campaigns, Inf. Sci. 414 (2017) 175–186, https://doi.org/10.1016/j. ins.2017.06.001.

[25] O. Alhabashneh, R. Iqbal, F. Doctor, A. James, Fuzzy rule-based profiling approach for enterprise information seeking and retrieval, Inf. Sci. 394 (2017) 18–37, https:/ doi.org/10.1016/j.ins.2016.12.040.

[26] J. Kolodner, Case-Based Reasoning, Morgan Kaufmann, 2014.

[27] Y. Solt, S. Horovitz, Bufer Management Architecture, US8176291 B1, http://www. google.com/patents/US8176291. (2012).

[28] P.-T. Huang, W. Hwang, Two-level FIFO bufer design for routers in on-chip in terconnection networks. JEICE Trans. Fundam. Electron. Commun. Comput. Sci E94–A (2011) 2412–2424.

[29] L. Wu, S. Liu, Y. Yang, L. Ma, H. Liu, Multi-variable weakening bufer operator and its application, Inf. Sci. 339 (2016) 98–107, https://doi.org/10.1016/j.ins.2016.01 002.

[30] Y. Jayababu, G.P.S. Varma, A. Govardhan, Incremental topological spatial association rule mining and clustering from geographical datasets using probabilistic approach, Journal of King Saud University: Computer and Information Sciences (2016) 510–523, https://doi.org/10.1016/j.jksuci.2016.12.006.

[31] Y. Gao, Q. Liu, X. Miao, J. Yang, Reverse k-nearest neighbor search in the presence of obstacles, Inf. Sci. 330 (2016) 274–292, https://doi.org/10.1016/j.ins.2015.10. 022.

[32] G. Gimenes, R.L.F. Cordeiro, J.F. Rodrigues-Jr, ORFEL: eficient detection of defa mation or illegitimate promotion in online recommendation, Inf. Sci. 379 (2017) 274–287, https://doi.org/10.1016/j.ins.2016.09.006.

[33] A. Rahman, B. Verma, Cluster-based ensemble of classifiers, Expert. Syst. 30 (2013) 270–282, https://doi.org/10.1111/j.1468-0394.2012.00637.x.

[34] A. Barak, R. Gelbard, Classification by clustering decision tree-like classifier based on adjusted clusters, Expert Syst. Appl. 38 (2011) 8220–8228, https://doi.org/10. 1016/i.eswa.2011.01.001

[35] A. Barak, R. Gelbard, Classification by clustering using an extended saliency measure, Expert. Syst. 33 (2016) 46–59, https://doi.org/10.1111/exsy.12121.

[36] N. Mishra, M. Hsu, U. Daval, Computer Implemented Scalable, Incremental and Parallel Clustering Based on Divide and Conquer, US6466946 B1, http://www. google.com/patents/US6466946, (2002) , Accessed date: 1 August 2016.

[37] E. Lughofer, A dynamic split-and-merge approach for evolving cluster models, Evol. Syst. 3 (2012) 135–151, https://doi.org/10.1007/s12530-012-9046-5.

[38] J. Correa-Morris, D.L. Espinosa-Isidron, D.R. Alvarez-Nadiozhin, An incremental nested partition method for data clustering. Pattern Recogn. 43 (2010) 2439–2455

[39] A. Woina, Constraint based incremental learning of classification rules, in: W. Ziarko, Y. Yao (Eds.), Rough Sets and Current Trends in Computing, Springer, 2001, pp. 428–435.

[40] T. Li, D. Ruan, J. Song, Dynamic maintenance of decision rules with rough set under characteristic relation. 20o7 International Conference on Wireless Communications, Networking and Mobile Computing, 2007, pp. 3713–3716, , https://doi.org/10.1109/WICOM.2007.918

[41] R. Amornchewin, W. Kreesuradej, Probability-based incremental association rule discovery algorithm, International Symposium on Computer Science and Its Applications. 2008, pp. 212–215.

[42] A. Ariya, W. Kreesuradej, Probability-based incremental association rule discovery using the normal approximation. 2013 JEEE 14th International Conference on Information Reuse Integration (IRI), 2013, pp. 432–439, , https://doi.org/10.1109 JRL2013.6642503.

[43] S. Thomas, S. Bodagala, K. Alsabti, S. Ranka, An efficient algorithm for the incremental updation of association rules in large databases, KDD-97, 1997, pp. 263–266

[44] M. Charikar, C. Chekuri, T. Feder, R. Motwani, Incremental clustering and dynamic

information retrieval, SIAM J. Comput. 33 (2004) 1417–1440, https://doi.org/10. 1137/S0097539702418498

[45] A. Bouchachia, An evolving classification cascade with self-learning, Evol. Syst. 1 (2010) 143–160, https://doi.org/10.1007/s12530-010-9014-x.

[46] M. Hadzikadic, B. Bohren, C. Eichelberger, Incremental Clustering Classifier and Predictor, US7213023 B2, (2007).

[47] C. Weare, Dynamic Content Clustering, US7333985B2, https://patents.google.com patent/US7333985B2/en, (2008).

[48] J. Beringer, E. Hüllermeier, Online clustering of parallel data streams, Data Knowl. Eng. 58 (2006) 180–204, https://doi.org/10.1016/j.datak.2005.05.009.

[49] G. Cormode, F. Korn, S. Muthukrishnan, D. Srivastava, Finding hierarchical heavy hitters in data streams, Proceedings 2003 VLDB Conference, Morgan Kaufmann, San Francisco, 2003, pp. 464–475 http://www.sciencedirect.com/science/article/pii/ B9780127224428500483.

[50] P. Zhang, X. Zhu, Y. Shi, L. Guo, X. Wu, Robust ensemble learning for mining noisy data streams, Decis. Support. Syst. 50 (2011) 469–479, https://doi.org/10.1016/j. dss.2010.11.004.

[51] D. Nhung, Developments in Data Extraction, Management, and Analysis, IGI Global, 2012.

[52] N.A. Barbosa, L. Travé-Massuyès, V.H. Grisales, A novel algorithm for dynamic clustering: Properties and performance, 2016 15th IEEE International Conference on Machine Learning and Applications (ICMLA), 2016, pp. 565–570, , https://doi. org/10.1109/ICMLA.2016.0099.

[53] T.S. Raghu, P.K. Kannan, H.R. Rao, A.B. Whinston, Dynamic profiling of consumers for customized oferings over the Internet: a model and analysis, Decis. Support. Syst. 32 (2001) 117–134, https://doi.org/10.1016/S0167-9236(01)00106-3.

[54] D. Nylén, J. Holmström, Digital innovation strategy: a framework for diagnosing and improving digital product and service innovation, Business Horizons 58 (2015) 57–67, https://doi.org/10.1016/j.bushor.2014.09.001.

[55] I. Sadgali, N. Sael, F. Benabbou, Performance of machine learning techniques in the detection of financial frauds, Procedia Computer Science 148 (2019) 45–54, https://doi.org/10.1016/j.procs.2019.01.007.

[56] R. Gelbard, A. Khalemsky, Dynamic classifier and sensor using small memory bufers, in: P. Perner (Ed.), Advances in Data Mining. Applications and Theoretical Aspects. Springer International Publishing. 2018. pp. 173–182

[57] T. Li, J.M. Corchado, S. Sun, J. Bajo, Clustering for filtering: multi-object detection and estimation using multiple/massive sensors, Inf. Sci. 388 (2017) 172–190, https://doi.org/10.1016/i.ins.2017.01.028

[58] J. Li, H. Xu, Suggest what to tag: recommending more precise hashtags based on users' dynamic interests and streaming tweet content. Knowl.-Based Syst. 106 (2016).196–205, https://doi,org/10.1016/i,knosys.2016.05.047

[59] Z. Miller, B. Dickinson, W. Deitrick, W. Hu, A.H. Wang, Twitter spammer detection using data stream clustering, Inf, Sci. 260 (2014) 64–73, https://doi.org/10.1016/j. ins,2013.11.016.

[60] Y. Xia, L. Tuo, An incremental community mining method in dynamic social networks 2014 IEEE 3rd International Conference on Cloud Computing and Intelligence Systems, 2014, pp. 305–309. , https://doi.org/10.1109/CCIS.2014.7175748

[61] P. Held, B. Krause, R. Kruse, Dynamic clustering in social networks using Louvain and Infomap method, 2016 Third European Network Intelligence Conference (ENIC), 2016, pp. 61–68, , https://doi.org/10.1109/ENIC.2016.017.

[62] Y.C. Song, H.D. Meng, S.L. Wang, M. O’Grady, G. O’Hare, Dynamic and incremental clustering based on density reachable, Fifth International Joint Conference on INC, IMS and IDC, 2009. NCM ‘09, 2009, pp. 1307–1310, , https://doi.org/10.1109/ NCM.2009.376.

[63] A. Ben-David, Automatic generation of symbolic multiattribute ordinal knowledgebased DSS’s: methodology and applications, Decis. Sci. 23 (1992) 1357–1372.

[64] L.M. Candanedo, V. Feldheim, D. Deramaix, A methodology based on hidden Markov models for occupancy detection and a case study in a low energy residential building, Energy and Buildings 148 (2017) 327–341, https://doi.org/10.1016/j. enbuild.2017.05.031.

[65] L.M. Candanedo, V. Feldheim, Accurate occupancy detection of an ofice room from light, temperature, humidity and CO measurements using statistical learning models, Energy and Buildings 112 (2016) 28–39, https://doi.org/10.1016/j. enbuild.2015.11.071.

[66] UCI machine learning repository: data sets, (n.d.). https://archive.ics.uci.edu/ml/ datasets.html (accessed December 10. 2016).

[67] Kaggle: Your Home for Data Science, (n.d.). https://www.kaggle.com/ (accessed February 25, 2019).

[68] Weka - Browse/weka-3-7-windows-x64 at SourceForge.net, (n.d.). https://sourceforge. net/projects/weka/files/weka-3-7-windows-x64/ (accessed October 15. 2017)

[69] R. Gelbard, Method and system for dynamic updating of classifier parameters based on dynamic buffers. U.S. Patent 10.268.923 B2 (Apr. 23 2019).

Anna Khalemsky is a doctoral student at the Information System program, at the Graduate School of Business Administration. Bar-Ilan University. She holds a B.A. and M A degrees in Statistics both from the Hebrew University of Jerusalem She also holds M.B.A degree in Finance from the Hebrew University and M.B.A. degree in Information Systems from Bar-Ilan University. In the last years she serves as a coordinator and a lecturer of mathematics and statistics at Hadassah Academic College.

Gelbard Roy serves as vice chairman of the Graduate School of Business Administration and as a member of the Data Science Institute, Bar-Ilan University. He received his Ph.D. and M.Sc. degrees in Information Systems from Tel-Aviy University. His work involves two main areas: (a) knowledge discovery in which he focuses on data representation, data mining, and recommendation systems, and (b) software project management in which he focuses on methodological and behavioral aspects.
