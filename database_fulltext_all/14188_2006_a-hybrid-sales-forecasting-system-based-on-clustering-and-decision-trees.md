---
otero_id: 14188
otero_key: "RZS3SXDC"
title: "A hybrid sales forecasting system based on clustering and decision trees"
authors: "Sébastien Thomassey; Antonio Fiordaliso"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2005.01.008"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Decision Support Systems 42 (2006) 408 – 421

www.elsevier.com/locate/dsw

# A hybrid sales forecasting system based on clustering and decision trees

Se´bastien Thomassey <sup>a,T</sup>, Antonio Fiordaliso

<sup>a</sup> GEMTEX- ENSAIT, 9 rue de l<sup>T</sup>ermitage 59100 Roubaix, France

<sup>b</sup> MATHRO- Faculte´ Polytechnique de Mons, 9 rue du Houdain, Mons, Belgium

Available online 28 March 2005

## Abstract

Competition and globalization imply a very accurate production and sourcing management of the Textile–Apparel– Distribution network actors. A sales forecasting system is required to respond to the versatile textile market and the needs of the distributors. Nowadays, due to the specific constraints of the textile sales (numerous and new items, short life time), existing forecasting models are generally unsuitable or unusable. We propose a forecasting system, based on clustering and classification tools, which performs mid-term forecasting. Performances of our models are evaluated using real data from an important French textile distributor.

<sup>D</sup> 2005 Elsevier B.V. All rights reserved.

Keywords: Sales forecasting; Decision trees; Clustering

## 1. Introduction

Due to the competitive environment of the Textile– Apparel–Distribution industry, companies require a rigorous management of sourcing, production and distribution. Existing methods, based on Supply Chain Management tools (Manufacturing Requirement Planning, Distribution Requirement Planning, Enterprise Resource Planning), improve the reactivity of the Textile–Apparel–Distribution network. However, many transformations, which are required to produce textile items, always impose significant and not easily reducible manufacturing lead times. Emergent globalization causes the dispersion of network actors and increases these lead times. Thus, in order to deal with the customer<sup>T</sup>s requests, companies often need to rely on an appropriate sales forecasting system to anticipate production volumes and to stock up items. However, the constraints of the apparel market complicate the forecasting procedure. The system must deal with:

<sup>!</sup> the large number of items (about 15000/year)

<sup>!</sup> the items with short lifetimes (6–12 weeks)

<sup>!</sup> the replacement of most of the items for each collection

<sup>!</sup> the long lead time of textile items which requires considerations about producing and source planning at a mid-term horizon (the forecasting horizon is one season or a year)

<sup>!</sup> the influence of many explanatory variables. These factors can be: weather data, holiday, marketing action, promotions, fashion or economic environment.

Several forecasting models, such as regression models [44], exponential and Box and Jenkins models [45], neural networks [58] or fuzzy systems [21,40], have been developed in different domains, such as electricity consumption, farm produce industry or traffic flow. Some of them provide satisfactory results [34] according to the field of application, forecast goal, user experience, and forecast horizon [8,14]. Nevertheless, all these methods are not easily usable in the textile environment, because the replacement of items each season deletes historical data.

In the last decade, several data mining techniques arise to assist decision makers who manage large volume of data. These methods are helpful to find and describe patterns in data sets, such as links or associations between sales and descriptive criteria (numeric or nominal). These patterns, when they exist, may be generalized to carry out forecasts of future data. There are many different ways to represent patterns in a data set (decision trees, classification rules, clustering, linear models, fuzzy systems or neural networks) and each of them leads to a different representation of knowledge.

Preceding works suggest fuzzy and neuro-fuzzy models [50–52] for mid and short-term sales forecasting at the item family level. However, these models, which are not easily interpretable, require aggregation of data by item family to obtain complete historical data of several years.

In this paper, our contribution to this issue is to estimate items sales by extracting and analyzing available data with an appropriate clustering procedure and decision tree. The clustering procedure carries out groups of similar items in term of sales profile (normalized sales) while the decision tree finds understandable links between these clusters and descriptive criteria.

The proposed forecasting system has been specifically developed to answer to the forecast issue of the textile–apparel industry. However, our model could also be considered in other domains characterized by:

<sup>!</sup> a large number of historical items,

<sup>!</sup> no historical data to make predictions (for instance: new product or new customer),

<sup>!</sup> availability of descriptive criteria (numerical or nominal).

For instance, the forecasting of electricity consumption profile for a new customer could be employed by our method. Indeed, the combination of clustering procedures and decision tree has already been applied in this domain [29].

The outline of this paper is as follow. Basic concepts of clustering and decision trees are introduced in the next section. Section 3 describes the environment of the textile distribution. Section 4 details the proposed forecasting model. Section 5 reports and analyzes the empirical results obtained with a real data set supplied by an important French ready-to-wear distributor<sup>1</sup>. The last section provides the conclusions.

## 2. Overview on decision trees and clustering procedures

Before we introduce the proposed data mining methods, it is important to describe the basic concepts of instance and attribute. The information required by the classifier takes the form of instances. Each instance is an independent example which is characterized by the values of attributes that measure different aspects of an instance. Attributes can be nominal (for example: gender is male, female), ordinal (for example: price is low, moderate, high) or numeric (for example: price <sup>a</sup> [10; 25]). Many data mining techniques exist for pattern classification [59] and for time series identification [37]. Amongst these methods, a wide variety of statistical models, such as linear discriminant analysis or logistic regression perform well on a large number of applications [4]. However, the classification accuracy of these models is often limited when the relationships of the input/output data set are complex and/or non-linear [3]. In such situation, which are frequently found in real world problems, machine learning methods are more suitable for building simple and interpretable pattern classification models [37,41]. The most common models are [32,62]: Bayesian networks [35], neural networks [49], rough sets [25], decision trees [11] and genetic algorithm classifiers [23].

In this section, we focus on two basic methods to classify (C4.5 algorithm [47]) and to cluster (k-means algorithm [27]) data. These tools are effective not only to find and describe patterns in data in order to make prediction but also tobuild an explicit representation of the knowledge.

## 2.1. Decision tree

Neural networks and decision trees are competitive techniques which are considered to be the most efficient tools in many pattern classification applications [54,37]. Neural networks are generally preferred for their generalization ability [26,60]. However, decision trees obviously outperform neural networks in terms of interpretability [61]. Decision trees are also fast and easy to use. Although their limitations are sometimes criticized [18,17], the rules generated by decision trees are simple and accurate [18] for most problems. Therefore, decision trees are very popular and powerful tools in data mining [18,54] and several significant works confirm their efficiency [54,37]. Indeed, in many applications, the structural description of the knowledge is as important as the ability to perform well on new examples [10,22,5]. In our case, interpretability of the classification results is a key issue because decision makers in textile companies never use tools that they do not understand. The fact that decision trees are efficient in terms of performance and easily interpretable is a major argument for their use in our problem.

Each node in a decision tree contains a question relative to a particular attribute. Leaf nodes are groups of instances that receive the same class label. An unknown (or test) instance is routed down the tree according to the values of the attributes in the successive nodes. When the instance reaches a leaf, it is classified according to the label assigned to the corresponded leaf. Leaves have to be homogeneous as much as possible.

## 2.1.1. Decision trees induction: C4.5 algorithm

Many algorithms for decision tree induction exist. ID3 [46] and C4.5 [47] are the most widely used [18] with the CART algorithm [11]. The CART (Classification and Regression Tree) algorithm is suitable for problems with numerical classes, thus, it is not appropriate in our context for which the classes are the label of the sales prototypes (nominal classes). Other interesting techniques have been proposed in the literature: CID3 [13], oblique decision tree [43], CAL5 [42], CDT [17] or NeC4.5 [61]. But their efficiencies have only been demonstrated in specific applications. The implementation of these techniques in our context could be the subject for future research. We chose the C4.5 algorithm because of its predictive accuracy [36] and the numerous possibilities in term of pruning, treatment of numerical and nominal attributes.

C4.5 algorithm is an extension of ID3 (Interactive Dichotomizer) algorithm and the divide-and-conquer approach [47,56]. Main improvements included in C4.5 deal with the pruning methodology and the processing of numeric attributes, missing values and noisy data. The splitting node strategy is based on the computation of the information gain ratio. The basic idea is that each node should hold a question concerning the attribute which is the most informative amongst the set of attributes not yet considered in the path from the root to that node. Information value also called Entropy measures how informative is the association of an attribute with a node [24]. The information gain associated with an attribute is computed as the difference between the information values of a node with or without the attribute. The notion of gain ratio [47] is useful to rank attributes. For decision tree induction purpose, the classical overfitting problem can be addressed via pruning strategies.

Two strategies can be adapted to prune a decision tree: prepruning or post- pruning. Prepruning involves trying to decide when to stop developing subtrees or branches during the tree building. Generally, the stopping criterion associated with the Information theory relies on the Minimum Descriptive Length principle [20,48]. Postpruning consists in building the complete tree and pruning it afterward. In general, the second method seems to be more attractive since it enables to build very informative subtrees composed of attributes which are individually low informative [47]. Two rather different operations have been considered for postpruning: subtree replacement and subtree raising (Fig. 1). At each node, the learning scheme might decide whether to perform subtree replacement, subtree raising or leave the subtree unpruned.

## 2.1.2. Learning technique: k-fold cross-validation

The performance of a classifier can be evaluated by computing the classification error rate. If the classifier predicts a correct class, it is a success, else it is an error. The evaluation of the error rate on the data used to train the classifier (training set) is not a reliable criterion. Indeed, with such a strategy, the classifier could overfit the training data. To predict the performance of a classifier, we need to access its error rate on an independent data set not used for the training process: the test set. In some situations, a third independent data sets can be considered: the validation set. The validation set is used to optimize the classifier parameters. This process is more suitable when lots of data are available. In this case, methods such as the k-fold cross-validation [33], the leave-one-out cross-validation and the bootstrap [19,33], are useful to predict the error rate on a new test set. The k-fold cross-validation, relies on a random partitioning of the data set in k parts. Then, one partition is used for testing while the k-1 remainders are used for training. This procedure is repeated k-1 times in order to use every part once for testing. Finally, the k error estimates are averaged to yield a robust overall error estimate. Due to the random selection of the folds, different k-fold crossvalidation experiments can lead to different classification error rates. Thus, in order to improve the accuracy of the error rate, it is a standard procedure to repeat the k-fold cross-validation process k times. Also, it is recommended to build the folds such that each class is properly represented, in the right proportion, in both training and test sets (stratified k-fold cross-validation). Generally, a value of k = 10 is sufficient (10-fold cross-validation).

## 2.2. Clusters

Unlike decision trees which assign a class to an instance (supervised method), clustering procedures are used when instances are divided into natural groups or clusters (unsupervised method). There are different ways to produce these clusters. The groups may be:

<sup>!</sup> exclusive [38], i.e. any instance belongs to only one group

<sup>!</sup> probabilistic [16] or fuzzy [9], i.e. an instance belongs to each group to a certain probability or degree (membership value)

<sup>!</sup> hierarchical [31], i.e. there is a crude division of instances into groups at the top level and each of these groups are refined further up to individual instances.

![](/api/attachments/RZS3SXDC/fulltext/images/ad69c629ba95bafe49e4ca5d4182281f5bdac430e2c3de9edffb4da8bd2499cf.jpg)  
Fig. 1. Example of subtree replacement and subtree raising.

The choice between these possibilities (exclusive clusters, membership degree, hierarchical clusters) is dictated by the future exploitation of the results. Indeed, in data mining applications, clustering is often followed by a stage where a decision tree or a set of rules is inferred to allocate each instance to the cluster in which it belongs [57]. The clustering method used in this paper is the classic and straightforward $k \mathrm { - }$ means algorithm [27], which has been used for several decades.

The k-means method is simplistic but reasonably effective to carry out the training for the decision trees. It allows to divide instances into disjoint clusters from numeric attributes. Different final clusters can be found because of the random initialization of the center of classes. Thus, as it is the case with other practical clustering techniques, each final cluster center do not represent a global optimum but a local one. To increase the chance of finding the global optimum, it is a simple matter to repeat the whole algorithm several times with different starting points and chose the best.

## 3. The apparel industry environment

Sales forecasting in textile industry is a very complex problem. Indeed, a wide range of textile item references exists (about 15,000/year for our French distributor partner). But most of the items are substituted at the next collection and their sales, which often have short lifespan (6–12 weeks) are particularly perturbed by numerous factors. These factors, which are neither strictly controlled nor identified [15], can depend on the item itself (colors, price,...), distributor (number of stores, merchandizing,...), customers $( \mathrm { f a s h i o n } , . . . )$ or external factors (weather, holidays,...). Moreover, they are not always available nor observable, and have different influences on sales.

The various stage durations in the production of textile items imply the need for predicting up to 1 year ahead before the raw materials are ordered. Production managers also require item quantities to manufacture, particularly early in the case of imported items from far away. It is also essential to fit in the forecast during the life cycle of the items, according to the replenishment achieved by local manufacturers.

![](/api/attachments/RZS3SXDC/fulltext/images/6fc6e3a13de81caf9f7773076329c022ee4f8366a3658efde4a526dc2e27460f.jpg)  
Fig. 2. Aggregation of textile items.

Therefore, apparel industry involves mid-term (1 year) and short-term (1–2 weeks) forecasts.

The replacement of items at each collection is very problematic for sales forecasting. Indeed, complete historical data of several years are often required for the learning process of forecasting models. To obtain such a data set, sales must be aggregated by item families (see Fig. 2). Sales forecasting of item families have been developed in a previous work [52]. The main issue of this paper is to compute mid-term forecasting of the sales profiles for new items for which we have no historical data. The inputs of our model are thus the historical sales data and descriptive criteria relative to old collections.

## 4. The proposed forecasting system

The purpose of the proposed system is to perform mid-term item sale forecasting according to the textile market constraints (numerous and new items, short life span) described in the previous section. It could be also implemented in other domains where the specificity of products is similar.

For historical items, the available data are the real sales and three descriptive criteria: price, the starting date of the sales and life span of each items. For future items, only descriptive criteria are known.

In order to compare sales behavior of two items having different sales volumeand life span, we deal with the sales profiles (normalized sales). This normalization involves two steps:

<sup>!</sup> normalization of the sales volume. The normalized sales $x _ { \mathrm { i } }$ (also called <sup>b</sup>life curve<sup>Q</sup>) is the sale $y _ { \mathrm { i } }$ divided by the sum of sales of the season: $\textstyle x _ { \mathrm { i } } = { \frac { y _ { \mathrm { i } } } { \sum _ { j = 1 } ^ { y _ { \mathrm { i } } } } } .$

<sup>!</sup> normalization of the life span is computed with the help of an homothety on the sales curve according to the time axis (Fig. 3).

![](/api/attachments/RZS3SXDC/fulltext/images/f6183824952b263a695d18e9088c088f55a67d0458ca6dc71196a153494e4a87.jpg)

![](/api/attachments/RZS3SXDC/fulltext/images/ff0bdb87d635b90b5ca466aa53a60f8682fa595b9b555471292a041e2b53ca7b.jpg)  
Fig. 3. Example of real sales and normalized sales profiles.

Our method, illustrated on Fig. 4, takes into account all items belonging to the same family. We proceed in two stages:

(1) a clustering procedure produces the sales pro files (also called <sup>b</sup>prototypes<sup>Q</sup>),

(2) a decision tree assigns each future items to one <sup>b</sup>prototype<sup>Q</sup> from the available descriptive criteria.

The sales profile forecasting is then given by the prototype of the considered item.

## 4.1. Clustering of sales profile

The purpose here is to achieve, inside a given family, clusters of similar items in terms of sales profiles. Each cluster center defines a sales profile, called <sup>b</sup>prototype<sup>Q</sup>, which characterizes the sales behavior of items included in the cluster considered.

![](/api/attachments/RZS3SXDC/fulltext/images/c75b616aca19eafd0b2a0f491d309bcf47594af70211da8d7147ee3b8d47fe6d.jpg)  
Fig. 4. Forecasting system based on clustering and decision tree.

The k-means algorithm (section 2.2) achieves exclusive clusters (each item belongs to only one group) and requires to determine the desired number of clusters. This value strongly influences the quality of the partition and the efficiency of the decision tree (second stage of the forecasting system). The number of clusters can be fixed manually, but this strategy is relatively complex when items are numerous. Consequently, we have to optimize this parameter automatically. We now explain how to determine the optimal number of clusters $( n _ { \mathrm { c } } ^ { * } )$ to build the most accurate decision tree classifier. The range used to evaluate the optimal number of clusters is selected between 2 and the expected maximum. This maximum has to be large enough to accurately cluster the data. However, if it is too large, the noise in the data set could impact the clusters strongly. Practically, we consider that the range is correct when the optimal number of clusters obviously appears in the curve represented in Fig. 6. Theoretically, the suitable maximum number of clusters is sometimes estimated as $\sqrt { N }$ , where N is the size of the data set [55]. In our case $( \sqrt { N } = \sqrt { 4 8 2 } \approx 2 2 )$ , we chose to find the optimal number of clusters between 2 and 20. Fig. 6 confirms that this range is large enough. Our method is based on the 10-fold cross-validation (see section 2.1.2 and Fig. 5):

(1) the k-means algorithm identifies a fixed number of clusters $n _ { \mathrm { c } }$ (and $n _ { \mathrm { c } }$ prototypes), which varies between 2 and 20, from a training set of historical items

(2) a decision tree is elaborated from the $n _ { \mathrm { c } }$ prototypes and additional descriptive criteria such as the price, the starting time of the sales and the life span of items available in the training set

(3) the decision tree maps each item of the validation set to one prototype (subset of historical items)

(4) the absolute error between real sales profiles and the assigned prototype is computed

(5) the number of cluster $n _ { \mathrm { c } } ^ { * } \mathrm { ~ c ~ }$ producing the more accurate classification is selected

This method enables an optimal linkage between the clustering and the classification algorithm. The $n _ { \mathrm { c } } ^ { * }$ clusters are then re-computed by the k-means algorithm with the complete historical data set.

The main shortcoming of this procedure is the computational time involved by the numerous required iterations. This could be very problematic when the size of the data set is large. Indeed, the computational complexity is estimated to be O(K I N) for the k-means clustering [2], between $O ( M ^ { 2 } N )$

![](/api/attachments/RZS3SXDC/fulltext/images/4356e4413f72b9cfbb99210bd706efb19606da1a4aad56b95b52c7239d7508f5.jpg)  
Fig. 5. Selection of the optimum number of clusters (n\*) with k-fold cross-validation.

![](/api/attachments/RZS3SXDC/fulltext/images/278932d80c8a7d56c7aa933b28ce86ebb96bacea1b235ad87c10badc332acea1.jpg)  
Fig. 6. Absolute error between real profiles and their forecasts according to the number of clusters.

and $O ( M ^ { 2 } N ^ { 3 } )$ for decision tree building algorithm and O(Nh) for the post-pruning tree procedure [39], where K is the number of desired clusters, I is the number of iterations of the k-means algorithm, N is the number of data, M is the number of attributes and h is the average size of the tree. For instance, in our case, the time required for one iteration including the clustering and the classification for $n _ { \mathrm { c } } ^ { * } { = } 1 4$ , is 11 s with a 1.2 GHz processor.

## 4.2. Decision tree for classification of future items

From the historical data set, a decision tree is built to carry out understandable links between descriptive criteria and the previously computed prototypes. Then, the decision tree associates each future item with a prototype according to the known descriptive criteria. The forecasting of the sales profile is the prototype adapted to the life span of the future item (homothety). The method used is the C4.5 algorithm (see section 2.1.1). In order to avoid overfitting problem and to carry out simple trees, the learning of the decision tree makes use of the 10-fold cross-validation technique (section 2.1.2) (not stratified because the number of items is quite large). The tree is then pruned with a postpruning strategy.

![](/api/attachments/RZS3SXDC/fulltext/images/00743ab6b8ea330ad8be20a34d4d5b1985d05d5fc2116cae64cc38f1ad8e81fb.jpg)

![](/api/attachments/RZS3SXDC/fulltext/images/c4fd3abb2488c4ddda5c6618f1b4fd1ba24d293732f242ce6f2455173ddb1d9b.jpg)

![](/api/attachments/RZS3SXDC/fulltext/images/26904c4ab51294022e43e7ed641890f1c1a74c84b24ad4b3a1101f3a31ab8603.jpg)

![](/api/attachments/RZS3SXDC/fulltext/images/159e8c76c03ec36137aeda161462ec4db8e8961ed9b1cc9859ab26556f066272.jpg)  
Fig. 7. Four examples of profile clusters and their associated prototypes.

Table 1  
Number of items included in each clusters and mean absolute error between real profiles and prototypes

<table><tr><td>Cluster</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td></tr><tr><td>Number of items</td><td>25</td><td>21</td><td>25</td><td>51</td><td>18</td><td>31</td><td>44</td><td>34</td><td>33</td><td>63</td><td>14</td><td>73</td><td>31</td><td>19</td></tr><tr><td>Clustering absolute error ( $\times 10^{-1}$ )</td><td>2.52</td><td>2.39</td><td>2.59</td><td>2.43</td><td>2.35</td><td>2.57</td><td>2.22</td><td>2.39</td><td>2.31</td><td>2.37</td><td>2.43</td><td>2.28</td><td>2.75</td><td>2.57</td></tr></table>

## 5. Experimental results

## 5.1. Sales data

Sales and descriptive data are extracted from our database relative to an important French textile distributor. Historical data, which are used for the learning process, are composed of 482 items (corresponding to years 1998 and 1999). Future data, which are used to evaluate the accuracy of our model, are composed of 285 items (corresponding to year 2000). In order to compare and to cluster sales profiles, life span of all items are normalized to 52 weeks. The selected descriptive criteria of items must have a significant influence on the observed sales. However, the choice is generally imposed by the availability of these criteria in the distributor’s database. In this work, the criteria are the price, the starting time of the sales and the life span of items. Additional criteria such as style or textile material are also of a great interest for forecasting purposes. However, these data are not available in our database.

## 5.2. Accuracy evaluation and comparison

In order to compute the forecasting errors of the sales profiles, we have selected the following three standard criteria:

<sup>!</sup> Root Mean Square Error (RMSE). Despite the fact that this criterion has been particularly criticized [6,7,53], it is often chosen by practitioners for its ease of use and simplicity [12].

<sup>!</sup> Mean Absolute Percentage Error (MAPE). This criterion is less sensitive than RMSE to large errors.

<sup>!</sup> Median Absolute Percentage Error (MdAPE). This criterion, less sensitive to aberrant points, is recommended to compare models on numerous series [6].

## 5.3. Forecasting models used for comparison

It is difficult to compare our model with classical time series forecasting models since:

<sup>!</sup> the forecast horizon is too large

<sup>!</sup> items do not have specific sales time series (substitution of items at each collection)

Very often, textile distributors rely on sales forecasting based on aggregated data and mean profiles of items belonging to the same family. This mean sales profile (mean predictor) will be used later as a benchmark. In order to evaluate the efficiency of the C4.5 algorithm, we have also tested 4 other classifiers:

Table 2  
Characteristics of the final decision tree

<table><tr><td rowspan="2">Number of classes</td><td rowspan="2">Number of attributes</td><td rowspan="2">Number of leaves</td><td rowspan="2">Size of the tree</td><td colspan="3">Number of nodes to reach each leaf</td></tr><tr><td>Min</td><td>Max</td><td>Mean</td></tr><tr><td>14</td><td>3</td><td>28</td><td>55</td><td>3</td><td>9</td><td>6</td></tr></table>

![](/api/attachments/RZS3SXDC/fulltext/images/d861eb4e4ea40e9ab5deb0ae85868935f20d3aedafb4cef25c4affeb55c6e390.jpg)  
Fig. 8. Illustration of a portion of the final decision tree.

<sup>!</sup> the most primitive algorithm, called ZeroR, simply outputs the most frequent class on the training data set. Inclusion of the ZeroR in the set of benchmark methods can help in identifying eventual overfitting problems,

<sup>!</sup> the OneR algorithm [28] generates simple rules based on the attribute that produces the smallest number of classification errors,

<sup>!</sup> the Na<sup>R</sup>ve Bayesian [30] method is based on the prior probabilities of each class computed from the training data,

<sup>!</sup> the k-nearest-neighbors classifier (IBk) [1] uses a distance function (for instance the Euclidian distance) to determine the k nearest neighbors of the test instance. These k instances predict the class of the test instance via simple majority vote. In our case, the number neighbors (k = 6) has been selected by 10-fold-cross-validation.

## 5.4. Results with real data

## 5.4.1. Clustering results

Our database is composed of 482 historical items. The optimal number of k-means clusters is n\*=14 (Fig. 6). Thus, the sale behavior of the 482 items are summarized by 14 prototypes of sales profiles.

Fig. 7 illustrates some examples of clusters (we show the 4 clusters which have the maximum error between real profiles and prototype) along with their associated prototypes. We remark that the k-means clustering procedure produces an efficient grouping of items with similar sales profiles. Consequently, the sales behavior of items belonging to a given cluster are accurately summarized by the associated prototype. Table 1 shows the number of items included in each cluster. It is important to note that prototypes are computed from a significant number of items (at least 14). We can then conclude that a robust estimation of the prototypes has been achieved.

## 5.4.2. Decision tree results

The final decision tree is composed of 55 nodes and 28 leaves (Table 2). As previously stated, three attributes are taken into account: the price, the starting time of the sales and the life span of items. The mean number of nodes to reach each leaf is 6. This relatively important tree is quite complex but still interpretable (Fig. 8). For instance, it appears that the price is only tested in 6 nodes which are final nodes. This means that the price is the less influent attribute for sales profile forecasting <sup>2</sup>. To reduce the size of the decision tree, it is possible to tune some parameters like the confidence threshold for the pruning procedure or the minimum number of instances allowed in each leaf. But a more drastic pruning could result in an overpruned tree producing bad performances in learning phase. Consequently, no additional tuning has been considered.

![](/api/attachments/RZS3SXDC/fulltext/images/87843db9941b3196c54f524fdec1b62a79d08b015659586bb24fc8d21353218a.jpg)

![](/api/attachments/RZS3SXDC/fulltext/images/215f9e083136b5899bfc71f22ba77ab20e20b2406794248735bfeaed6d6b344c.jpg)

![](/api/attachments/RZS3SXDC/fulltext/images/23f6ef0a8d8c782d4036649a4ec802de52680449ea4a11520ba1791326fde07d.jpg)

![](/api/attachments/RZS3SXDC/fulltext/images/c0ad1d44f4a17351dc6a4c2629ca1c6c52c1e7da0472f753f0e6c4b3e3dcc4b4.jpg)  
Fig. 9. Comparison of assigned prototypes and real profiles for new items (dotted lines represent the mean profile predictor).

Fig. 9 enables a comparison between four prototypes assigned by the decision tree and the real sales profiles of future items. For most cases, the decision tree assigns prototypes relatively similar to real sales profiles, except for a few items whose sales are very different in only some weeks (see Fig. 9, prototypes 3, 8 and 9). We also remark that profiles of items associated with prototype 7 are relatively similar but are quite different from the prototype. This could result from the fact that the attributes used to build the decision tree are not rich enough to explain the sales behavior of these items. Nevertheless, Table 3 and Fig. 10 show that our forecasting method is globally the most accurate model. Amongst the 4 benchmark rule based methods, IBk is the most accurate one, but it still compares unfavorably with our method: the observed degradations are 5% for the RMSE, 9% for the MAPE and 21% for the MdAPE.

Comparison of the error criteria between the 6 tested models on 285 test items

<table><tr><td></td><td>RMSE(average)</td><td>MAPE(average)</td><td>MdAPE</td></tr><tr><td>Mean profile</td><td>13.6E-3</td><td>203</td><td>119</td></tr><tr><td>ZeroR</td><td>13.9E-3</td><td>308</td><td>170</td></tr><tr><td>OneR</td><td>17.4E-3</td><td>257</td><td>123</td></tr><tr><td>Naïve Bayesian</td><td>16.3E-3</td><td>138</td><td>93</td></tr><tr><td>IBk</td><td>13.3E-3</td><td>138</td><td>80</td></tr><tr><td>Proposed system (C4.5)</td><td>12.7E-3</td><td>126</td><td>66</td></tr></table>

## 6. Conclusions and perspectives

The constraints of the apparel market significantly complicate the mid-term sales forecasting of items. The proposed model, based on existing clustering technique (k-means algorithm) and decision tree classifier (C4.5 algorithm) is useful to estimate sales profiles of new items for which we have no historical sales data. The clustering procedure groups similar historical items in term of sales profiles. The decision tree links up descriptive criteria of historical items with prototypes of sales profiles extracted from clusters.

![](/api/attachments/RZS3SXDC/fulltext/images/784120336d823a036e9a7c1a47c10d4dfdff25a7d010af8aec6f8d764eb936f8.jpg)

![](/api/attachments/RZS3SXDC/fulltext/images/af0dec7d983123efcd41a911aa29950fc5ca7707752cbffde4213db402359993.jpg)

![](/api/attachments/RZS3SXDC/fulltext/images/2b838c3a22577982bd87bbcaf35b9740b375ba9cb973505f49140d37cf1ad489.jpg)

![](/api/attachments/RZS3SXDC/fulltext/images/9d22d5366d369a2604664509a4dc964ecb958c8fec3bbdb8f10bd790e71e1873.jpg)  
Fig. 10. RMSE and MAPE computed on 285 test items.

Then, the decision tree associates future items with prototypes from their descriptive criteria. These prototypes constitute the forecasting of the sales profiles.

Tested on 285 real sales items, this model allows an overall increase of the accuracy of mid-term forecasting in comparison with the mean sales profile predictor and the other tested classifiers. The clustering procedure carries out homogeneous grouping of items. The proposed decision tree has a relatively complex structure and enables an estimation of the behavior of future items. However, some mistakes arise from the decision tree. In one case, the prototype is relatively different from the future items sales profiles. These classification errors of the decision tree could result from the fact that the used descriptive criteria are not rich enough to discriminate the sales behaviors of all future items. Further criteria, such as style or textile material must be considered in the hope of increasing the forecasting accuracy, but such data are not often available in the apparel industry.

Finally, considering the various sources of uncertainty that arise in apparel market, it would be interesting to compare the decision tree with other classifiers based on soft computing such as neural networks, genetic programming or fuzzy logic. We let these perspectives as future works.

## References

[1] D. Aha, Tolerating noisy, irrelevant, and novel attributes in instance-basedlearning algorithms, International Journal of Man–Machine Studies 36 (2) (1992) 267– 287.

[2] D. Akume, G.W. Weber, Cluster algorithms: theory and methods, Journal of Computational Technologies 7 (1) (2002) 15– 27.

[3] E.I. Altam, G. Macro, F. Varetto, Corporate distress diagnosis: comparison using linear discriminant analysis and neural networks, Journal Banking and Finance 18 (1994) 505–529.

[4] J. Andre´s, M. Landajo, P. Lorca, Forecasting business profitability by using classification techniques: a comparative analysis based on a Spanish case, European Journal of Operational Research 167 (2) (2005) 518–542.

[5] R. Andrews, J. Diederich, A.B. Tickle, A survey and critique of techniques for extracting rules from trained artificial neural networks, Knowledge Based Systems 8 (1995) 373– 389.

[6] J.S. Armstrong, F. Collopy, Error measures for generalizing about forecasting methods: empirical comparisons, International Journal of Forecasting 8 (1992) 69– 80.

[7] J.S. Armstrong, R. Fildes, Correspondence on the selection of error measures for comparisons among forecasting methods, Journal of Forecasting 14 (1995) 67– 71.

[8] J.S. Armstrong, Principles of Forecasting—A Handbook for Researchers and Practitioners, Kluwer Academic Publishers, Norwell, MA, 2001.

[9] J.C. Bezdek, Pattern Recognition with Fuzzy Objective Function Algorithms, Plenum Press, New-York, 1981.

[10] R.J. Brachman, H.J. Levesque, Reading in Knowledge Representation, Morgan Kaufmann, San Francisco, 1985.

[11] L. Breiman, J. Friedman, R. Olshen, C. Stone, Classification and Regression Trees, Wadsworth, Belmont, CA, 1984.

[12] R. Carbon, J.S. Armstrong, Evaluation of extrapolative forecasting methods: results of a survey of academicians and practitioners, Journal of Forecasting 1 (1982) 215 – 217.

[13] K. Cios, N. Liu, A machine learning method for generation of a neural network architecture: a continuous ID3 algorithm, IEEE Transactions on Neural Networks 3 (2) (1992) 280–291.

[14] C.G. Dasgupta, G.S. Dispensa, S. Ghose, Comparative the predictive performance of a neural network model with some traditional market response models, International Journal of Forecasting 10 (1994) 235– 244.

[15] A. De Toni, A. Meneghetti, The production planning process for a network of firms in the textile–apparel industry, International Journal of Production Economics 65 (2000) 17– 32.

[16] P.A. Devijer, J. Kittler, Pattern Recognition: A Statistical Approach, Prentice-Hall, Englewood Cliffs, NJ, 1982.

[17] J. Dombi, A. Zsiros, Learning multicriteria classification models from examples: decision rules in continuous space, European Journal of Operational Research 160 (3) (2005) 663– 675.

[18] W. Duch, R. Setiono, J.M. Zurada, Computational intelligence methods for rule-based data understanding, Proceddings of the IEEE 92 (5) (2004) 771 – 805.

[19] B. Efron, R. Tibshirani, An Introduction to the Bootstrap, Chapman and Hall, London, 1993.

[20] U.M. Fayyad, K.B. Irani, Multi-interval discretization of continuous valued attributes for classification learning, Proceeding of the 13th International Joint Conference on Artificia Intelligence, Chambery, France, Morgan Kauffmann, San Francisco, 1993.

[21] A. Fiordaliso, A nonlinear forecasts combination method based on Takagi–Sugeno fuzzy systems, International Journal of Forecasting 14 (1998) 367– 379.

[22] A. Fiordaliso, Autostructuration of fuzzy systems by rules sensitivity analysis, International Journal for Fuzzy Sets and Systems 118 (2) (2000) 281–296.

[23] D.E. Goldberg, Genetic Algorithm in Search, Optimization, and Machine Learning, Addison-Wesley, Reading, MA, 1989.

[24] R.M. Gray, Entropy and Information Theory, Springer-Verlag, New-York, 1990.

[25] S. Greco, B. Matarazzo, R. Slowinski, Rough sets theory for multicriteria decision analysis, European Journal of Operational Research 129 (1) (2001) 1 –47.

[26] L.K. Hansen, P. Salamon, Neural network ensembles, IEEE Transactions on Pattern Analysis and Machine Intelligence 12 (10) (1990) 993– 1001.

[27] J.A. Hartigan, Clustering Algorithms, John Wiley, New-York, 1975.

[28] R.C. Holte, Very simple classification rules perform well on most commonly used datasets, Machine Learning 11 (1993) 63 – 91.

[29] B. Hugueney, Repre´sentations symboliques de longues se´ries temporelles, the\`se de l<sup>T</sup>universite´ de Paris VI, 2003.

[30] G.H. John, P. Langley, Estimating continuous distributions in Bayesian classifiers, Proceedings of the 11th Conference on Uncertainty in Artificial Intelligence, Morgan Kaufmann, Montreal Canada, 1995, pp. 338– 345.

[31] S.C. Johnson, Hierarchical clustering schemes, Psychometrika 2 (1967) 241–254.

[32] T. Kervahut, J.Y. Potvin, An interactive–graphic environment for automatic generation of decision trees, Decision Support Systems 18 (2) (1996) 117–134.

[33] R. Kohavi, A study of cross-validation and bootstrap accuracy estimation and model selection, Proceeding of 14th International Joint Conference on Artificial Intelligence, Montreal, Canada, Morgan Kaufmann, San Francisco, 1995, pp. 1137– 1143.

[34] R.J. Kuo, K.C. Xue, Fuzzy neural networks with application to sales forecasting, Fuzzy Sets and Systems 108 (1999) 123– 143.

[35] P. Langley, W. Iba, K. Thompson, An analysis of Bayesian classifiers, Proceedings of the Tenth National Conference on Artificial Intelligence, AAAI Press, San Jose, CA, 1992, pp. 223– 228.

[36] M. Last, O. Maimon, A compact and accurate model for classification, IEEE Transactions on Knowledge and Data Engineering 16 (2) (2004) 203– 215.

[37] K.C. Lee, S.B. Oh, An intelligent approach to time series identification by a neural network-driven decision tree classifier, Decision Support Systems 17 (1996) 183 – 197.

[38] J.B. MacQueen, Some methods for classification and analysis of multivariate observations, Proceedings of 5th Berkeley Symposium on Mathematical Statistics and Probability, vol. 1, University of California Press, Berkeley, 1967, pp. 281– 297.

[39] J.K. Martin, D.S. Hirschberg, The time complexity of decision tree induction, Technical report 95-27, Department of Information and Computer Science, University of California, Irvine, 1995.

[40] P.A. Mastorocostas, J.B. Theocharis, V.S. Petridis, A constrained orthogonal least-squares method for generating TSK fuzzy models: application to short-term load forecasting, Fuzzy Sets and Systems 118 (2001) 215– 233.

[41] W. Muller, E. Wiederhold, Applying decision tree methodology for rules extraction under cognitive constraints, European Journal of Operational Research 136 (2) (2002) 282– 289.

[42] W. Muller, F. Wysotzky, Automatic construction of decision trees for classification, in: K. Moser, M. Schader (Eds.), Annals of Operation Research, vol. 92, J.C. Baltzer AG Sciences Publishers, Wijdenes, Netherlands, 1994.

[43] S. Murthy, S. Kasif, S. Salzberg, A system for induction of oblique decision trees, Journal of Artificial Intelligence Research 2 (1994) 1– 32.

[44] A.D. Papalexopoulos, T.C. Hesterberg, A regression-based approach to short-term system load forecasting, IEEE Transactions on Power Systems 5 (1990) 1535–1547.

[45] J.H. Park, Y.M. Park, K.Y. Lee, Composite modeling for adaptive short-term load forecasting, IEEE Transactions on Power Systems 6 (1991) 450 – 457.

[46] J.R. Quinlan, Induction of decision trees, Machine Learning 1 (1986) 81–106

[47] J.R. Quinlan, C4.5: Programs for Machine Learning, Morgan Kauffman, San Francisco, 1993.

[48] J. Rissanen, The minimum description length principle, in: S. Kotz, N.L. Johnson (Eds.), Encyclopedia of Statistical Sciences, vol. 5, John Whiley, New-York, 1985, pp. 523–527.

[49] S. Schocken, Neural networks for decision support: problems and opportunities, Decision Support Systems 11 (5) (1994) 393– 414.

[50] S. Thomassey, M. Happiette, J.M. Castelain, An automatic textile sales forecast using fuzzy treatment of explanatory variables, Journal of Textile and Apparel Technology and Management 3 (1) (2002) 1 – 15 (http://www.tx.ncsu.edu/jtatm/).

[51] S. Thomassey, M. Happiette, J.M. Castelain, X. Zeng, A shortterm forecasting system adapted to textile distribution, IPMU, Annecy, France, 2002 (July 8–9).

[52] S. Thomassey, M. Happiette, J.M. Castelain, A short and mean-term automatic forecasting system—application to textile logistics, European Journal of Operational Research 161 (1) (2003) 275– 284.

[53] P.A. Thompson, An MSE statistic for comparing forecast accuracy across series, International Journal of Forecasting 6 (1990) 219–227.

[54] K. Tsujino, S. Nishida, Implementation and refinement of decision trees using neural networks for hybrid knowledge

acquisition, Artificial Intelligence in Engineering 9 (1995) 265– 275.

[55] J. Vesanto, E. Alhoniemi, Clustering of the self-organizing map, IEEE Transactions on Neural Networks 11 (3) (2000) 586– 600.

[56] P.H. Winston, Artificial Intelligence, Third Edition, Addison-Wesley, Boston, 1992.

[57] I.H. Witten, E. Frank, Data Mining: Practical Machine Learning Tools and Techniques with Java Implementations, Morgan Kaufmann, San Francisco, 1999.

[58] H. Yoo, R.L. Pimmel, Short-term load forecasting using a selfsupervised adaptative neural network, IEEE Transactions on Power Systems 14 (2) (1999) 779 – 784.

[59] R.S. Youssif, C.N. Purdy, Combining genetic algorithms and neural networks to build a signal pattern classifier, Neurocomputing (Amst) 61 (2004) 39– 56.

[60] Z.H. Zhou, J. Wu, W. Tang, Ensembling neural networks: many could be better than all, Artificial Intelligence 137 (1–2) (2002) 239– 263.

[61] Z.H. Zhou, Y. Jiang, NeC4.5: neural ensemble based C4.5, IEEE Transactions on Knowledge and Data Engineering 16 (6) (2004) 770– 773.

[62] C. Zopounidis, M. Doumpos, Multicriteria classification and sorting methods: a literature review, European Journal of Operational Research 138 (2002) 229– 246.

Antonio Fiordaliso holds a Ph.D. in mathematics. He works as a researcher at the Faculte´ Polytechnique de Mons and Universite´ Libre de Bruxelles (Belgium). His research interests include multicriteria decision aid methods, data mining and time series forecasting.

Se´bastien Thomassey received the M.Sc. degree from the Ecole Nationale Supe´rieure des Arts et Industries Textiles (ENSAIT) in Roubaix in 1999 and the Ph.D. in automation from the University of Lille 1 (France) in 2002. He is assistant Professor in logistic and automation at the ENSAIT since 2003. His Preprint submitted to Elsevier Science 24 January 2005 research interests include classification and sales forecasting of textile items.
