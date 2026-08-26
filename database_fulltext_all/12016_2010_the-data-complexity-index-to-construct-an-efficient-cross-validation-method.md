---
otero_id: 12016
otero_key: "CAZEBHN6"
title: "The data complexity index to construct an efficient cross-validation method"
authors: "Der-Chiang Li; Yao-Hwei Fang; Y.M. Frank Fang"
year: "2010"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.07.005"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# The data complexity index to construct an ef<sup>fi</sup>cient cross-validation method

Der-Chiang $\operatorname { L i } ^ { \mathrm { a } , \ast }$ , Yao-Hwei Fang <sup>b</sup>, Y.M. Frank Fang <sup>c</sup>

<sup>a</sup> Department of Industrial and Information Management National Cheng Kung University, Taiwan

<sup>b</sup> Division of Biostatistics and Bioinformatics, National Health Research Institutes, Taiwan

<sup>c</sup> Geographic Information System Research Center, Feng Chia University, Taiwan

## a r t i c l e i n f o

Article history: Received 20 January 2009 Received in revised form 31 March 2010 Accepted 18 July 2010 Available online 23 July 2010

Keywords: Binary classi<sup>fi</sup>cation problem Cross-validation Data complexity

## a b s t r a c t

Cross-validation is a widely used model evaluation method in data mining applications. However, it usually takes a lot of effort to determine the appropriate parameter values, such as training data size and the number of experiment runs, to implement a validated evaluation. This study develops an ef<sup>fi</sup>cient cross-validation method called Complexity-based Ef<sup>fi</sup>cient (CBE) cross-validation for binary classi<sup>fi</sup>cation problems. CBE cross-validation establishes a complexity index, called the CBE index, by exploring the geometric structure and noise of data. The CBE index is used to calculate the optimal training data size and the number of experiment runs to reduce model evaluation time when dealing with computationally expensive classi<sup>fi</sup>cation data sets. A simulated and three real data sets are employed to validate the performance of the proposed method in the study, while the validation methods compared are repeated random subsampling validation and K-fold cross-validation. The results show that CBE cross-validation, repeated random sub-sampling validation and K-fold cross-validation have similar validation performance, except that the training time required for CBE cross-validation is indeed lower than that for the other two methods. © 2010 Elsevier B.V. All rights reserved.

## 1. Introduction

In data mining applications, researchers generally use crossvalidation to evaluate the learned classi<sup>fi</sup>cation model [11]. However, this usually requires considerable computational costs. With K-fold cross-validation, for example, the number of experiment runs must increase when parameter K increases, making the training computationally expensive [1]. Speci<sup>fi</sup>cally, ((K−1)/K)% training data are theoretically needed for learning a classi<sup>fi</sup>cation model, and when the data size is very large, ((K−1)/K)% training data makes computation expensive [1].

In another common scenario, repeated random sub-sampling validation is usually repeated 30 or 50 times for model evaluation [23]. However, if the data structure is simple or uniform, the number of times sub-sampling validation is repeated is much more than what is needed, and thus the procedure is inef<sup>fi</sup>cient.

Our research develops an effective cross-validation procedure, called Complexity-based Ef<sup>fi</sup>cient (CBE) cross-validation, for binary classi<sup>fi</sup>cation problems. The CBE cross-validation method can be used to calculate the optimal training data size and the number of experiment runs to reduce model validation time. The CBE crossvalidation procedure systematically establishes a non-linear data complexity index (de<sup>fi</sup>ned in Section 3) called CBE index by exploring the geometric structure and noise of data.

The density-based clustering algorithm (DBSCAN) is used to discover the geometric structure and noise, while the betweendistance and within-distance of the clusters found are used as the factors of the CBE index. Based on this, this research develops an ef<sup>fi</sup>cient CBE cross-validation procedure to calculate the optimal training data size and number of experiment runs.

The rest of this paper is organized as follows: The literature review is given in Section 2 while the detailed procedure of the proposed method is described in Section 3. One simulated and three real data sets are used to illustrate the CBE cross-validation model in Section 4, and Section 5 contains the conclusion and discussion of our research.

## 2. Literature review

In this section we review the concept of linear data complexity (the de<sup>fi</sup>nition is explained in Section 3), the geometric structure and noise of data, and existing cross-validation methods.

## 2.1. Linear data complexity

For linear data complexity, the index used to detect the level of data complexity is Fisher's discriminant ratio f [1,10]:

$$
f = \frac {\left(\mu_ {1} - \mu_ {2}\right) ^ {2}}{\sigma_ {1} ^ {2} + \sigma_ {2} ^ {2}}\tag{1}
$$

where $\mu _ { 1 } , \mu _ { 2 } , \sigma _ { 1 } ^ { 2 } ,$ ,and σ <sup>2</sup> are the means and variances of the two classes in a data set, respectively. f is speci<sup>fi</sup>c for one feature dimension case.

For a multidimensional problem, the maximum f over all the feature dimensions is used to describe the problem. For problems with multidimensional features, Li and Fang proposed a Purity Level (PL) to measure linear data complexity [15]. The parameters of the index are de<sup>fi</sup>ned as follows:

n: the number of data points. k: the number of dimensions of the data (k≥2).

$A _ { i j } ^ { + } , A _ { i j } ^ { - }$ : the value of the j-th dimension of the i-th data point in the positive and negative classes, respectively.

$\bar { A } _ { j } ^ { + } , \bar { A } _ { j } ^ { - }$ : the average value of the j-th dimension of the data in the positive and negative classes, respectively.

$A _ { j \operatorname* { m a x } } , A _ { j \operatorname* { m i n } } ;$ : the maximum and the minimum values of the j-th dimension, respectively. Using the parameters listed above, the Purity Level is set as:

$$
\text { Purity   Level } = \frac {\sum_ {i = 1} ^ {n} \left(\sqrt {\frac {\sum_ {j = 1} ^ {k} \left(\frac {A _ {i j} ^ {+} - \overline {{A}} _ {j} ^ {-}}{A _ {j \max} - A _ {j \min}}\right) ^ {2}}{k - 1}} + \sqrt {\frac {\sum_ {j = 1} ^ {k} \left(\frac {A _ {i j} ^ {-} - \overline {{A}} _ {j} ^ {+}}{A _ {j \max} - A _ {j \min}}\right) ^ {2}}{k - 1}}\right)}{\sum_ {i = 1} ^ {n} \left(\sqrt {\frac {\sum_ {j = 1} ^ {k} \left(\frac {A _ {i j} ^ {+} - \overline {{A}} _ {j} ^ {+}}{A _ {j \max} - A _ {j \min}}\right) ^ {2}}{k - 1}} + \sqrt {\frac {\sum_ {j = 1} ^ {k} \left(\frac {A _ {i j} ^ {-} - \overline {{A}} _ {j} ^ {-}}{A _ {j \max} - A _ {j \min}}\right) ^ {2}}{k - 1}}\right)}\tag{2}
$$

where the numerator is the sum of the between-class distance of the whole data set, and the denominator is the sum of the within-class distance of the whole data set. The results show that the smaller the PL value, the higher the linear data complexity, and vice versa. However, neither Fisher's discriminant ratio nor PL considers the geometric structure and noise of data.

## 2.2. The concept of geometric structure and noise of data

Rubinov [21] discussed the relationship between classes and clusters in data sets, and examined the distribution of classes within the obtained clusters. He found that some characteristics link data points more strongly than the classes they belong to. We thus believe that the geometric structure of data is an essential characteristic for classifying data sets.

In a study on the effect of noise in data processing, Lee et al. [14] combined the fuzzy adaptive resonance theory and the general regression neural network into a hybrid model, which assisted the removal of noise embedded in training data in order to improve the classi<sup>fi</sup>cation ability. Han et al. [9] proposed a revised Expectation-Maximization (EM) algorithm to discover and remove noise to improve the one-against-the-rest method in binary text classi<sup>fi</sup>cation. Cao et al. [2] proposed a data preprocessing method for training data to remove noise or outliers, and used the remaining data to obtain the decision function. However, the drawback of this method is that it is dif<sup>fi</sup>cult to remove noise and outliers without the assistance of problem domain knowledge.

## 2.3. Common types of cross-validation method

Cross-validation is a model evaluation method that is better than residual analysis. The weakness of residual evaluation is that it does not give an indication of how well the learner will do when it is used to make predictions for unseen data. One way to overcome this problem is to leave out part of the data points from the data set when training a classi<sup>fi</sup>er, So that when training is <sup>fi</sup>nished the removed data are used to test the performance of the model. This is the basic idea for the model evaluation method called cross-validation [24].

Two widely used such methods, repeated random sub-sampling validation and K-fold cross-validation, are described below.

## 2.3.1. Repeated random sub-sampling validation

This method randomly splits a data set into training and validation data sets and then repeats this procedure several times. For each split, the classi<sup>fi</sup>er is trained with the training data and validated with the validation data. The results from each split can be averaged. This method is usually applied in small sample learning cases that use a small amount of training data to learn the model and large amount of validation data to validate it [16,17].

## 2.3.2. K-fold cross-validation

In K-fold cross-validation, the original sample is partitioned into K partitions. A partition is then used as the validation data for testing the model, and the remaining K−1 partitions are used as the training data. The cross-validation process is then repeated K times, with each of the K partitions used as the validation data exactly once. The K results from the folds can be averaged to produce a single estimation [24]. The advantage of this method over the repeated random subsampling validation method is that all observations are used for both training and validation, and each observation is used for validation exactly once. 10-fold cross-validation is commonly used by researchers.

## 3. Proposed method

With binary classi<sup>fi</sup>cation problems, data complexity is de<sup>fi</sup>ned as the level of complexity for separating data into classes. When the data complexity is high this means it is hard to classify. Complexities can be subdivided into linear and non-linear cases: linear data complexity means a complex level for separating the data using a linear hyperplane; while non-linear data complexity means a complex level for separating the data using a non-linear hyperplane. Taking the XOR problem as an example, we usually use a non-linear hyperplane to separate the data rather than a linear one.

This research focuses on <sup>fi</sup>nding an effective way to classify data by calculating the non-linear data complexity for high dimensional classi<sup>fi</sup>cation problems. We develop the CBE index by improving the Purity Level (PL) method [15], and consider the geometric structure and noise of data to precisely measure the level of non-linear separability. We then use the CBE index to form a sample size determination method to develop an ef<sup>fi</sup>cient CBE cross-validation method to improve computational ef<sup>fi</sup>ciency. The proposed Complexity-based Ef<sup>fi</sup>cient (CBE) index is described in detail in subsection 3.1, and the proposed CBE cross-validation is described in subsection 3.2.

## 3.1. CBE index

Research on pattern recognition suffers from the uncertainty concerning the match between knowledge and a problem due to the strong dependence of classifying performance on available data. In other words, the accuracy of a classi<sup>fi</sup>er is highly dependent on the data characteristics [10]. Unfortunately, this uncertainty often remains because of a lack of understanding of the full data characteristics [18], and this situation also occurs in model validation. Therefore, in this work we consider more descriptors, such as the geometric structure and noise of data, to further understand the data characteristics with the goal of improving validation ef<sup>fi</sup>ciency.

The CBE index relies heavily on the realization of the data's geometric structure, because, in our experience, when the center of the data belonging to a class is not located in the data cluster (such as with the XOR problem in Fig. 1), it is not reasonable to use a linear index, such as an F-test statistic or purity level, to measure the data complexity. We thus develop the non-linear CBE index to <sup>fi</sup>nd multiple centers according to the geometric structures of data. In that we calculate the centers of data clusters and let the centers be located in the data. Note that the linear index concept is a special case of the non-linear one when it has only one cluster in each class.

![](/api/attachments/CAZEBHN6/fulltext/images/99e329bd389117113bb25cf132e2f313ff000ef5b1a47359b3404c2a0bf72af6.jpg)  
Fig. 1. The structure of a XOR problem.

To discover the geometric structure and noise of data, researchers usually rely on prior knowledge, although this is experience oriented and inconclusive [22]. This research thus proposes a non-linear data complexity index, the CBE index, to systematically re<sup>fl</sup>ect the geometric structure and noise of data precisely. This study uses the density-based clustering (DBSCAN) algorithm to discover the geometric structure and noise of data to <sup>fi</sup>nd the complexity level to separate data into classes, as explained below.

## 3.1.1. DBSCAN algorithm

DBSCAN is a clustering algorithm suitable for a data set with a large amount of data with high dimensionality [7]. DBSCAN gathers together high density data as clusters and the shape of each cluster are arbitrary. The algorithm <sup>fi</sup>nds the clusters and then deletes data that does not belong to any of them. It searches for clusters by checking the surroundings of each data point within a scope called the ε-neighborhood. If the ε-neighborhood of a data point contains other data which has a data size that is more than a certain pre-de<sup>fi</sup>ned number (MinPts), a cluster with this data (called the core object) is created; otherwise, the data is treated as noise which will be eventually deleted. DBSCAN iteratively collects directly densityreachable data (data within the ε-neighborhood of a core object) until no new data can be added to any cluster, and this may involve merging some clusters. We apply the DBSCAN algorithm to each class to detect the geometric structure and noise of data in binary classi<sup>fi</sup>cation. Table 1 shows the DASCAN algorithm pseudo code.

Consider the radius of a default $\varepsilon ,$ obtained by considering the fraction of objects to be selected $( k / m )$ and the volume V [6]. We extend this concept to binary classi<sup>fi</sup>cation and suppose that n is the dimension of the data, k is the number of MinPts, Γ is the gamma function, $m _ { + }$ and m are the amounts of data in the positive and negative classes, repectively, and $\begin{array} { r } { V _ { + } = \prod _ { j } \mathrm { r a n g e } \left( x _ { j } ^ { + } \right) } \end{array}$ and $V _ { - } =$ $\Pi _ { j } \mathrm { r a n g e } \Big ( x _ { j } ^ { - } \Big ) \mathrm { f o r } j = 1 , . . , k$ are the data ranges in the positive and negative classes, respectively. The following are the formula sets for $\varepsilon _ { + }$ , and ε for positive and negative classes, respectively:

$$
\varepsilon_ {+} = \sqrt [ n ]{\frac {(k / m _ {+}) V _ {+} \Gamma (k / 2 + 1)}{\sqrt {\pi^ {n}}}}\tag{3}
$$

$$
\varepsilon_ {-} = \sqrt [ n ]{\frac {(k / m _ {-}) V _ {-} \Gamma (k / 2 + 1)}{\sqrt {\pi^ {n}}}}\tag{4}
$$

The pseudo code of the DBSCAN algorithm

```txt
Input : ←
    X = {x₁, x₂,..., xₙ} //Set of elements←↓
    Minpt //Minimum number of points in cluster←↓
    Eps ε //Maximum distance for density measure←↓
Output : ←
    C = {C₁, C₂,..., Cₖ} //Set of clusters←↓
DBSCAN algorithm : ←
    c = 0 //Initially there is no clusters←↓
    FOR i = 1 to n DO←↓
    IF xᵢ is not a cluster, THEN ←↓
    Y = {Xⱼ, |Xⱼ is density-reachable from Xᵢ}; ←↓
    IF Y is a valid cluster, THEN ←↓
    c = c + 1 ←↓
    C_c = Y ←↓
    END IF ←↓
    END IF ←↓
END FOR ←↓
```

Daszykowski et al. proposed a default MinPts calculation formula [5]. We extend this formula to binary classi<sup>fi</sup>cation and de<sup>fi</sup>ne:

$$
\begin{array}{l} \text { MinPts } _ {+} = \text { integer } \left(\frac {m _ {+}}{2 5}\right), \text { for   a   positiveclass } \\ \text { MinPts } _ {-} = \text { integer } \left(\frac {m _ {-}}{2 5}\right), \text { for   a   negative   class } \end{array}\tag{5}
$$

6

For a data set with numerous data points of positive and negative classes (m or m ), we suggest that MinPts or MinPts be equal to 20.

## 3.1.2. The calculation of the CBE index

This research uses the CBE index to depict the level of non-linear data complexity. The CBE index of binary classi<sup>fi</sup>cation can be regarded as the relative distance of clusters discovered by the DBSCAN algorithm for each class, and it is found as follows:

Let $\mathbf { X } { = } \{ \mathbf { X } _ { 1 } , . . . , \mathbf { X } _ { N } \}$ be a data set that includes positive samples $\mathbf { \Sigma } _ { + } \mathbf { X } = \left\{ \mathbf { \Sigma } _ { + } \mathbf { X } _ { 1 } \mathbf { \Sigma } , \mathbf { . . . } , \mathbf { + } \mathbf { X } _ { \mathrm { n _ { + } } } \mathbf { \Sigma } \right\}$ and negative samples $\mathbf { X } = \left\{ \mathbf { \Phi } _ { - } \mathbf { X } _ { 1 } \ , . . . , \mathbf { \Phi } _ { - } \mathbf { X } _ { \mathrm { n _ { - } } } \ \right\}$ where $n _ { + } + n _ { - } = N .$ g<sub>Let</sub> $\mathbf { \Phi } _ { _ { F } } C \mathbf { \Phi } = \left\{ { _ { + } } { \mathbf { C } } _ { 1 } , . . . , _ { + } { \mathbf { C } } _ { | _ { + } } { \mathbf { c } } _ { | } \ \right\}$ be a set that consists $ 0 \mathrm { f } | _ { + } C |$ positive clusters, $\begin{array} { r } { \mathbf { \Psi } _ { C } = \left\{ \mathbf { \Psi } _ { - } \mathbf { C } _ { 1 } , \dots , - \mathbf { C } _ { | - } \mathbf { c } _ { | } \right\} } \end{array}$ be a set consisting of $| \neg C \ |$ negative clusters, $\mathbf { d } ( \mathbf { { X } } _ { i } , \mathbf { { X } } _ { j } )$ be the distance between $\mathbf { X } _ { i }$ and $\mathbf { X } _ { j } ,$ , and $\mathbf { \mu } _ { _ { + } } C _ { i } \mathbf { \sigma } = \left\{ { \bf \Phi } _ { + } \mathbf { X } _ { 1 } ^ { \mathrm { i } } , . . . , \mathbf { \Phi } _ { + } \mathbf { X } _ { + } ^ { \mathrm { i } } \mathbf { m } _ { \mathrm { i } } \right\}$ be the i-th positive cluster, where m is the number of positive samples in the i-th cluster, and $i = 1 , . . . , | _ { + } C |$ Similarly, let $\mathbf { \mu } _ { - } C _ { i } = \left\{ \mathbf { \mu } _ { - } \mathbf { X } _ { 1 } ^ { \mathrm { i } } , \dots , \mathbf { \mu } _ { - } \mathbf { X } _ { \mathrm { ~ - ~ } } ^ { \mathrm { i } } \mathbf { \Sigma } _ { \mathrm { m _ { i } } } \right\}$ <sup>þ</sup>be the i-th negative cluster, <sup>g</sup>where m is the number of negative samples in i-th cluster, and $i = 1 , . . . , \big | _ { - } C \ |$ . We <sup>fi</sup>rst calculate the minimum average distance between <sup>j</sup>a pair of clusters which belong to different classes as Min\_Bet:

$$
\text{Min\_Bet} = \underset { \begin{array}{c} k = 1, \ldots , | _ {+} C | \\ l = 1, \ldots , | _ {-} C | \end{array} }{\text{Min}} \left\{\frac {\sum_ {i = 1} ^ {+ m _ {k}} \sum_ {j = 1} ^ {- m _ {l}} d \left(_ {+} \mathbf {X} _ {i} ^ {k} , - \mathbf {X} _ {j} ^ {l}\right)}{_ {+} m _ {k} \cdot - m _ {l}} \right\}\tag{7}
$$

A large value of Min\_Bet indicates that the data are widely scattered and easy to classify.

We then calculate the average distance within all clusters of the positive class as:

$$
\text { Within } _ {+} = \sum_ {k = 1} ^ {| + C |} \frac {\sum_ {i = 1} ^ {+ m _ {k}} \sum_ {j = 1} ^ {- m _ {k}} d \left(_ {+} \mathbf {X} _ {i} ^ {k} , - \mathbf {X} _ {j} ^ {l}\right)}{_ {+} \mathbf {m} _ {k} (_ {+} \mathbf {m} _ {k} - 1)}\tag{8}
$$

and for all clusters of the negative class as:

$$
\text { Within } _ {-} = \sum_ {k = 1} ^ {| + C |} \frac {\sum_ {i = 1} ^ {+ m _ {k}} \sum_ {i = 1} ^ {- m _ {k}} d \left(_ {-} \mathbf {X} _ {i} ^ {k} , - \mathbf {X} _ {j} ^ {l}\right)}{_ {-} m _ {k} (_ {-} m _ {k} - 1)}\tag{9}
$$

If the value of the average distance within all clusters of a class Within and Within is small, it means that these clusters <sup>ð Þþ</sup>congregate with each other.

The calculation of the CBE index is de<sup>fi</sup>ned as follows:

$$
\text { CBE   index } = \frac {\text { MinBet }}{\frac {\text { Within } _ {+} + \text { Within } _ {-}}{| _ {+} C | + | _ {-} C |}}\tag{10}
$$

The determination of the CBE index takes three steps:

Step 1: Normalize the data

For different units of dimensions, the data is normalized before calculating the CBE index.

Step 2: Discover the geometric structure and noise of data Use the DBSCAN algorithm in the binary classes with the suggested parameter settings: $\varepsilon _ { + } , \varepsilon _ { - }$ , MinPts ,and MinPts , to detect the geometric structure and remove the data noise.

Step 3: Calculate the CBE index

Calculate Min\_Bet, Within<sub>+</sub>, and Within to obtain the CBE index.

The CBE index has the following properties:

(1) 0≤CBE indexb∞.

(2) The smaller the CBE index is, the higher the data complexity is.

(3) The larger the CBE index is, the lower the data complexity is.

## 3.2. CBE cross-validation method

We apply the CBE index to develop the CBE cross-validation method, where we <sup>fi</sup>rst randomly select a certain small proportion (for example, 5%) of samples as the training data and calculate the CBE index. This process is repeated 30 times to calculate the averages $\overline { { \mathsf { X } } } _ { \mathrm { C B E } }$ and the standard deviations S . In order to achieve a stable CBE index for the optimal training data size N, this process is iterated while increasing the proportion of the training data and checking the difference of $\overline { { \mathsf { X } } } _ { \mathrm { C B E } }$ as:

When $\overline { { X } } _ { \mathrm { C B E } } ^ { n \% } \mathrm { - } \overline { { X } } _ { \mathrm { C B E } } ^ { n + 1 \% } \mathrm { < } 0 . 0 1 , \mathrm { T H E N }$

N = Max no:of n% samples; no: of 10% samples · data size

11

When the difference decreases by a level smaller than 0.01, we consider the structure of the training data to be stable, and use this training data size as the optimal one. Where 0.01 is only an empirical suggestion and 10% is also an empirical save low sample size limit.

For the number of experiment runs, we repeat the process 30 times to calculate the average and standard deviation of CBE. Note that the sample distribution of the CBE index will converge to a normal distribution according to the Central Limit Theorem (CLT) [3], and the optimal training data size (average $\overline { { \mathbf { X } } } _ { \mathrm { C B E } } ^ { n _ { 6 } ^ { q } }$ and standard deviations $S _ { \mathrm { C B E } } ^ { n _ { \mathrm { e } } ^ { \mathrm { \sigma } } } )$ is used to calculate the number of experiment runs. The number of experiment runs K is determined as:

$$
\begin{array}{l} \text {CALCULATE} \frac {\left(Z _ {\alpha / 2}\right) ^ {2} S _ {\mathrm{CBE}} ^ {n \% 2}}{\left(0 . 0 5 \cdot \overline {{X}} _ {\mathrm{CBE}} n \%\right) ^ {2}} = k, \text {THEN} \\ \text {Max} \{k, 5 \} = K \end{array}\tag{12}
$$

where α is the signi<sup>fi</sup>cance level, $Z _ { \alpha / 2 }$ is the value with α/2% in the tail of the cumulative standard Normal distribution, and $\left( 0 . 0 5 { \cdot } \overline { { \mathbf { X } } } _ { \mathrm { C B E } } ^ { n _ { 0 } ^ { q } } \right)$ is set as the desired margin of error, where 5 is again our suggestion.

## 4. Experiment

In this section, we use one simulated and three real data sets to verify the performance of the Complexity-based Ef<sup>fi</sup>cient (CBE) crossvalidation method. In the simulation experiments, a support vector machine (SVM) [12], a Back-propagation Network (BPN) [8,20], and a Naive Bayes Classi<sup>fi</sup>er (NBC) [24] are used as the classi<sup>fi</sup>cation tools, while in the three real data sets, only SVM is used.

To <sup>fi</sup>nd the relationship between CBE index and classi<sup>fi</sup>cation accuracy, we randomly select 10% of the total samples and calculate the CBE index with the suggested $\varepsilon _ { + } , \varepsilon _ { - } , \mathsf { M i n P t } _ { + }$ ,and MinPt in Section 3 to measure the relationship for all data sets. This process is repeated 10 times, where SVM, BPN, and NBC are used as the classi<sup>fi</sup>ers with the resubstitution method (all available data are used for training and testing) [13].

To implement the CBE cross-validation, we randomly select a small proportion of the data as the training set (such as 5%), and calculate the CBE indexes. This procedure is repeated 30 times. The training data size is gradually increased, where we calculate the average and the standard deviation of the CBE index in order to <sup>fi</sup>nd the optimal training data size and the number of experiment runs.

## 4.1. Simulated data experiments

This research uses the Parametric Equation of a Hypersphere [16], brie<sup>fl</sup>y introduced below, to generate simulated data. The n-hypersphere (often simply called the n-sphere) is a generalization of an object with n dimensions in $\mathbb { R } ^ { \mathrm { n } }$ (the circle and sphere are called the two-sphere and three-sphere, respectively). The n-sphere centered at the origin can therefore be de<sup>fi</sup>ned as a set of points $\left( x _ { 1 } , x _ { 2 } , . . . , x _ { k } \right)$ such that:

$$
x _ {1} ^ {2} + x _ {2} ^ {2} + \ldots + x _ {n} ^ {2} = r ^ {2}\tag{13}
$$

## Table 2

<table><tr><td>CBE index</td><td>2.964</td><td>2.447</td><td>2.743</td><td>2.594</td><td>3.628</td><td>3.264</td><td>3.896</td><td>3.889</td><td>4.168</td><td>4.357</td></tr><tr><td>Average no. of noisy samples found</td><td>0.46</td><td>0.32</td><td>0.68</td><td>0.72</td><td>0.63</td><td>0.84</td><td>0.91</td><td>0.54</td><td>0.42</td><td>0.86</td></tr><tr><td>Average no. of clusters found (pos., neg.)</td><td>(2, 2)</td><td>(2, 2)</td><td>(2, 2)</td><td>(2, 2)</td><td>(2, 2)</td><td>(2, 2)</td><td>(2, 2)</td><td>(2, 2)</td><td>(2, 2)</td><td>(2, 2)</td></tr><tr><td>Accuracy of SVM</td><td>70.25</td><td>70.56</td><td>71.11</td><td>71.45</td><td>72.42</td><td>72.56</td><td>72.44</td><td>75.35</td><td>76.55</td><td>77.89</td></tr><tr><td>Accuracy of BPN</td><td>70.75</td><td>71.02</td><td>71.84</td><td>71.76</td><td>72.12</td><td>72.84</td><td>75.32</td><td>75.98</td><td>76.35</td><td>78.52</td></tr><tr><td>Accuracy of NBC</td><td>68.14</td><td>69.45</td><td>70.12</td><td>70.85</td><td>71.34</td><td>72.81</td><td>73.56</td><td>74.38</td><td>75.92</td><td>75.45</td></tr></table>

The CBE index and classi<sup>fi</sup>cation accuracies of the three classi<sup>fi</sup>ers for the simulated data sets with 1% noise where “Average no. of noise samples found” means for the average number of noise found, “Average no. of clusters found” means for the average number of cluster found by using DBSCAN algorithm

The hypersphere can be speci<sup>fi</sup>ed in a parametric equations as:

$$
\left\{ \begin{array}{l} x _ {1} = r   \sin \theta_ {1} \sin \theta_ {2} \dots \sin \theta_ {n - 1} \\ x _ {2} = r   \sin \theta_ {1} \sin \theta_ {2} \dots \cos \theta_ {n - 1} \\ x _ {3} = r   \sin \theta_ {1} \sin \theta_ {2} \dots \cos \theta_ {n - 2} \\ x _ {4} = r   \sin \theta_ {1} \sin \theta_ {2} \dots \cos \theta_ {n - 3} \\ \quad \vdots \\ x _ {n - 1} = r   \sin \theta_ {1} \cos \theta_ {2} \\ x _ {n} = r   \cos \theta_ {1} \end{array} \right.\tag{14}
$$

where r is the radius and θ ; $\theta _ { 2 } , . . . , \theta _ { n - 1 } \in [ 0 ,$ 2π are the angles of the hypersphere. The formula of parametric equations is not unique, but must satisfy the identity $x _ { 1 } ^ { 2 } + x _ { 2 } ^ { 2 } + \ldots + x _ { n } ^ { 2 } = 1$

We consider the two-cluster condition in each class and insert noise into the data. We generate 808 <sup>fi</sup>ve-dimension data (404 positive and 404 negative samples) following the Parametric Equation of a Hypersphere [16]. In the positive class, the data is generated into two clusters. One is:

$$
\left\{ \begin{array}{l} x _ {1} = - 0. 7 + \sin \theta_ {1} \sin \theta_ {2} \dots \sin \theta_ {4} \\ x _ {2} = - 0. 7 + \sin \theta_ {1} \sin \theta_ {2} \dots \cos \theta_ {4} \\ x _ {3} = - 0. 7 + \sin \theta_ {1} \sin \theta_ {2} \dots \cos \theta_ {3} \\ x _ {4} = - 0. 7 + \sin \theta_ {1} \sin \theta_ {2} \cos \theta_ {2} \\ x _ {5} = - 0. 7 + \cos \theta_ {1} \end{array} , 0 \leq \theta \leq 2 \pi \right.\tag{15}
$$

and the other is:

$$
\left\{ \begin{array}{l} x _ {1} = - 0. 7 + s i n \theta_ {1} \sin \theta_ {2} \dots \sin \theta_ {4} \\ x _ {2} = 0. 7 + s i n \theta_ {1} \sin \theta_ {2} \dots \cos \theta_ {4} \\ x _ {3} = - 0. 7 + s i n \theta_ {1} \sin \theta_ {2} \dots \cos \theta_ {3} \\ x _ {4} = - 0. 7 + s i n \theta_ {1} \sin \theta_ {2} \cos \theta_ {2} \\ x _ {5} = - 0. 7 + c o s \theta_ {1} \end{array} , 0 \leq \theta \leq 2 \pi \right.\tag{16}
$$

In the negative class, the data is generated into two clusters too. One is

$$
\left\{ \begin{array}{l} x _ {1} = 0. 7 + \sin \theta_ {1} \sin \theta_ {2} \dots \sin \theta_ {4} \\ x _ {2} = - 0. 7 + \sin \theta_ {1} \sin \theta_ {2} \dots \cos \theta_ {4} \\ x _ {3} = - 0. 7 + \sin \theta_ {1} \sin \theta_ {2} \dots \cos \theta_ {3} \\ x _ {4} = - 0. 7 + \sin \theta_ {1} \sin \theta_ {2} \cos \theta_ {2} \\ x _ {5} = - 0. 7 + \cos \theta_ {1} \end{array} , 0 \leq \theta \leq 2 \pi \right.\tag{17}
$$

and the other is:

$$
\left\{ \begin{array}{l} x _ {1} = 0. 7 + s i n \theta_ {1} \sin \theta_ {2} \dots \sin \theta_ {4} \\ x _ {2} = 0. 7 + s i n \theta_ {1} \sin \theta_ {2} \dots \cos \theta_ {4} \\ x _ {3} = - 0. 7 + s i n \theta_ {1} \sin \theta_ {2} \dots \cos \theta_ {3} \\ x _ {4} = - 0. 7 + s i n \theta_ {1} \sin \theta_ {2} \cos \theta_ {2} \\ x _ {5} = - 0. 7 + \cos \theta_ {1} \end{array} , 0 \leq \theta \leq 2 \pi \right.\tag{18}
$$

We then add 1% noise to each class by randomly selecting 4 samples to change class label. Table 2 and Fig. 2 show the results of using the CBE index with the simulated data sets.

![](/api/attachments/CAZEBHN6/fulltext/images/4951a5ca444eb48cce607824caaa7d37ae5d39c0f9333547eadc68248d4bdbf6.jpg)  
Fig. 2. The relationship between classi<sup>fi</sup>cation accuracy and the CBE index with 1% noise

The averages and standard deviations (SDs) of CBE indexes with increasing size of the training data sets for the simulated data set. (Bold value means the optimal data size).

<table><tr><td>Training data</td><td>40 (5%)</td><td>81 (10%)</td><td>121 (15%)</td><td>161 (20%)</td><td>202 (25%)</td></tr><tr><td>Average</td><td>3.836</td><td>3.474</td><td>3.408</td><td>3.071</td><td>2.684</td></tr><tr><td>SD</td><td>0.368</td><td>0.393</td><td>0.424</td><td>0.393</td><td>0.382</td></tr><tr><td>Training data</td><td>242 (30%)</td><td>283 (35%)</td><td>291 (36%)</td><td>299 (37%)</td><td>307 (38%)</td></tr><tr><td>Average</td><td>2.224</td><td>2.167</td><td>2.140</td><td>2.129</td><td>2.124</td></tr><tr><td>SD</td><td>0.236</td><td>0.287</td><td>0.296</td><td>0.138</td><td>0.161</td></tr></table>

From the table and <sup>fi</sup>gure above we can see that when the value of CBE increases, the classi<sup>fi</sup>cation accuracies of SVM, BPN, and NBC also rise. There is thus a highly positive correlation between the CBE index and classi<sup>fi</sup>cation accuracy for the simulated data sets.

To <sup>fi</sup>nd the optimal training data size, we calculate various CBE indexes by increasing the training set size. Table 3 and Fig. 3 show the results of using the CBE index with various simulated data sets.

$$
\begin{array}{r l} & \text { WHEN } \overline {{X}} _ {\mathrm{CBE}} ^ {3 7 \%} - \overline {{X}} _ {\mathrm{CBE}} ^ {3 8 \%} <   0. 0 1, \text { THEN } \\ & \text { Max } \{\text { no.   of   37\%   samples,   no.of   10\%   samples } \} \cdot \text { data   size } \\ & = 3 7 \% \cdot 8 0 8 \\ & = 2 9 9 \end{array}\tag{19}
$$

We determine that the optimal training data size is 299 when $C B E _ { \overline { { X } } }$ decreases by less than 0.01, and consider that the geometric structure of the optimal training data is stable.

To <sup>fi</sup>nd the optimal number of experiment runs for the simulated data set. We use the optimal sample size to measure the optimal experiment runs as:

$$
\begin{array}{r l} & \text { CALCULATE } \frac {\left(Z _ {\alpha / 2}\right) ^ {2} 0 . 1 3 8 ^ {2}}{(0 . 0 5 \cdot 2 . 1 2 9) ^ {2}} = 6. 4 2 6, \text { THEN } \\ & \text { Max } \{6. 4 5 6, 5 \} \\ & \quad = 6 \end{array}\tag{20}
$$

In the simulated data set, with a signi<sup>fi</sup>cance level $\alpha { = } 0 . 0 5$ and a margin of error of 0.1065, the optimal number of training data is 299, and the optimal number of experiment runs is six.

We use repeated random sub-sampling validation (with 533 (66%) training data points, 275 (34%) testing data points, experiment repeated 30 times) to validate that our CBE cross-validation (with 299 (37%) training data points, 509 (63%) testing data points, experiment repeated six times) is ef<sup>fi</sup>cient. The average and standard deviations of the SVM with the repeated random sub-sampling validation are 78.326 and 1.044, respectively; and of the CBE cross-validation are 77.779 and 1.145. The performances of the two cross-validation methods thus have insigni<sup>fi</sup>cant differences (the P-value is 0.125, using the independent t-test). The average training time of the repeated random sub-sampling validation is $0 . 8 9 ^ { * } 3 0 = 2 6 . 7 ~ s ,$ and that of the CBE cross-validation is $0 . 5 1 ^ { * } 6 = 3 . 1 s$ . We also use <sup>fi</sup>ve-fold cross-validation to validate that our CBE cross-validation is ef<sup>fi</sup>cient. The average and standard deviations of the SVM with <sup>fi</sup>ve-fold crossvalidation are 78.454 and 1.141, respectively. The performances of the cross-validation methods have insigni<sup>fi</sup>cant differences (the P-value is 0.138, using the independent t-test) and the average training time of the <sup>fi</sup>ve-fold cross-validation is $0 . 9 9 ^ { * } 6 = 5 . 9 4 s$

![](/api/attachments/CAZEBHN6/fulltext/images/02f6a12e820e6fc29bed79c896a504543cfe912698ed383b79ccaf05881ac536.jpg)  
Fig. 3. Relationship between training size and the CBE index with the simulated data set.

Properties of the three data sets.

<table><tr><td>Data set</td><td>No. of dimensions</td><td>No. of samples</td><td>No. of classes</td></tr><tr><td>Pima Indians diabetes</td><td>8</td><td>768</td><td>2</td></tr><tr><td>Haberman&#x27;s survival</td><td>3</td><td>306</td><td>2</td></tr><tr><td>Australian credit approval</td><td>14</td><td>690</td><td>2</td></tr></table>

In addition, when we use 10% of the total data (the lower bound of the training data size) as the training data, and <sup>fi</sup>ve experiments runs (the lower bound of the experiment runs), the average and standard deviations of SVM are 73.779 and 2.563, with a signi<sup>fi</sup>cant difference (lower) compared to CBE cross-validation (the P-valuebb0.01, using the independent t-test). The average training data is $0 . 3 2 ^ { * } 5 = 1 . 6 8 ~ \mathrm { s } .$ Since validation effectiveness is the bssic concern of researchers, the CBE cross-validation is thus considered to be better than the crossvalidation using the lower bound of the training data size and experiment runs, and so it is an ef<sup>fi</sup>cient and effective method.

## 4.2. Real data experiment

This research uses two medical data sets, Pima Indians Diabetes and and Haberman's Survival, and one business data set, Australian Credit Approval, in the experiment. The Pima Indians diabetes data set consists of 768 data with eight numeric dimensions (attributes), and it is a two-class data set with target values denoted by 0 and 1. The class value 1 means tested positive for diabetes, and the class value 0 means tested negative. The Haberman's Survival data set consists of 306 data with three numeric dimensions, and it is a two-class data set to record the survival status for breast cancer patients. The Australian Credit Approval data set consists of 690 data with 14 dimensions that include six numerical and eight categorical data, and it is a two-class data set. Table 4 shows the summary of the sample characteristics of the three data sets, which are all downloaded from the UCI repository, available at http://www.ics.uci.edu. The results of the experiment for the three data sets are shown in the following subsection.

## 4.2.1. The Pima data set

The relationship between the CBE indexes and classi<sup>fi</sup>cation accuracies is shown in Table 5 and Fig. 4.

From the table and <sup>fi</sup>gure above we can see that when the value of CBE decreases, the classi<sup>fi</sup>cation accuracy of the SVM also falls. There is thus a highly positive correlation between the CBE index and classi<sup>fi</sup>cation accuracy for the Pima data set. Table 6 and Fig. 5 show the experimental results of CBE cross-validation for the Pima data set.

$$
\begin{array}{r l} & \text { WHEN } \overline {{X}} _ {\mathrm{CBE}} ^ {1 3 \%} - \overline {{X}} _ {\mathrm{CBE}} ^ {1 4 \%} <   0. 0 1, \text { THEN } \\ & \text { Max } \{\text { no.   of } 1 3 \% \text { samples }, \text { no.   of } 1 0 \% \text { samples } \} \cdot \text { data   size } \\ & = 1 3 \% \cdot 7 6 8 \\ & = 1 0 0 \end{array}\tag{21}
$$

Pima data set with 77 selected samples as the training data (default MinPt=3).  
![](/api/attachments/CAZEBHN6/fulltext/images/a10fd660ab91b329c2677c0e312b22c3851947c686f1f4d99f00190aa2eef779.jpg)  
Fig. 4. Relationship between CBE indexes and accuracies with the Pima data set (correlation coef<sup>fi</sup>cient=0.773).

The averages and standard deviations (SDs) of CBE indexes with increasing size of the training data sets for the Pima data set. (Bold value means the optimal data size).

<table><tr><td>Training data</td><td>38 (5%)</td><td>46 (6%)</td><td>54 (7%)</td><td>61 (8%)</td><td>70 (9%)</td></tr><tr><td>Average</td><td>1.536</td><td>1.474</td><td>1.428</td><td>1.481</td><td>1.444</td></tr><tr><td>SD</td><td>0.260</td><td>0.292</td><td>0.321</td><td>0.293</td><td>0.287</td></tr><tr><td>Training data</td><td>77 (10%)</td><td>84 (11%)</td><td>92 (12%)</td><td>100 (13%)</td><td>108 (14%)</td></tr><tr><td>Average</td><td>1.202</td><td>1.177</td><td>1.170</td><td>1.128</td><td>1.123</td></tr><tr><td>SD</td><td>0.137</td><td>0.107</td><td>0.106</td><td>0.026</td><td>0.061</td></tr></table>

We determine this size as the optimal training data size to be 100, and thus consider that the geometric structure of the optimal training data is stable.

We use the optimal sample size to calculate the optimal number of experiment runs with the Pima data set as:

$$
\begin{array}{r l} & \text { CALCULATE } \frac {\left(Z _ {\alpha / 2}\right) ^ {2} 0 . 0 2 6 ^ {2}}{(0 . 0 5 \cdot 1 . 1 2 8) ^ {2}} = 0. 8 1 5, \text { THEN } \\ & \text { Max } \{0. 8 1 5, 5 \} \\ & = 5 \end{array}\tag{22}
$$

where $\alpha { = } 0 . 0 5$ is the signi<sup>fi</sup>cance level, and $( 0 . 0 5 \cdot 1 . 1 2 8 ) = 0 . 0 5 6 4$ is <sup>ð Þ¼</sup>the desired margin of error. We thus determine that the optimal number of experiment runs to be <sup>fi</sup>ve.

We then use repeated random sub-sampling validation (with 507 (66%) training data points, 261 (34%) testing data points, experiment repeated 30 times) to validate that our CBE cross-validation (with 100 (13%) training data points, 668 (87) testing data points, experiment repeated <sup>fi</sup>ve times) is ef<sup>fi</sup>cient. The average and standard deviations of the SVM with the repeated random sub-sampling validation are 76.578 and 1.743, respectively; and of the CBE cross-validation are 74.192 and 2.044. The performances of the two cross-validation methods have insigni<sup>fi</sup>cant differences (the P-value is 0.043, using the independent t-test). The average training time of the repeated random sub-sampling validation is $0 . 9 1 ^ { * } 3 0 = 2 7 . 3 \ s$ and the average training time of the CBE cross-validation is $1 . 9 ^ { * } 5 = 6 . 2 :$ s.

We also use <sup>fi</sup>ve-fold cross-validation to validate that our CBE cross-validation is ef<sup>fi</sup>cient. The average and standard deviations of the SVM with the <sup>fi</sup>ve-fold cross-validation are 75.824 and 1.874, respectively. The performances of the two cross-validation methods have insigni<sup>fi</sup>cant differences (the P-value is 0.052, using the independent t-test). The average training time of the <sup>fi</sup>ve-fold crossvalidation is $3 . 1 6 ^ { * } 5 = 1 5 . 8 ~ s$

In addition, when we use 10% of the total data (the lower bound of the training data size) as the training data with <sup>fi</sup>ve experiment runs (the lower bound of the experiment runs), the average and standard deviations of SVM are 72.731 and 2.942, and it has signi<sup>fi</sup>cant differences with CBE cross-validation (the $P { \mathrm { - } } { \mathrm { V a l u e } } = 0 . 0 5 5$ , using the independent t-test). The average training data is $1 . 6 9 ^ { * } 5 = 8 . 4 \ s .$ . The CBE crossvalidation is better than the cross-validation using the lower bounds of the training data size and experiment runs. Therefore, CBE crossvalidation is considered an ef<sup>fi</sup>cient and effective method.

<table><tr><td>Accuracy</td><td>63.75</td><td>71.25</td><td>68.75</td><td>75</td><td>76.25</td><td>78.75</td><td>82.5</td><td>85</td><td>81.25</td><td>86.25</td></tr><tr><td>CBE index</td><td>1.063</td><td>1.089</td><td>1.098</td><td>1.123</td><td>1.124</td><td>1.163</td><td>1.176</td><td>1.215</td><td>1.221</td><td>1.481</td></tr></table>

Table 7  
![](/api/attachments/CAZEBHN6/fulltext/images/dd750310bbdeffe0e07bb1d9e570f15eba4bda46c7e3c87b5d3739a38d7519c8.jpg)  
Fig. 5. Relationship between training size and CBE index with the Pima data set

## 4.2.2. The Haberman data set

The relationship between the CBE indexes and classi<sup>fi</sup>cation accuracies is shown in Table 7 and Fig. 6.

From the table and <sup>fi</sup>gure above we can see that when the value of CBE decreases, the classi<sup>fi</sup>cation accuracy of the SVM also falls. There is thus a highly positive correlation between the CBE index and classi<sup>fi</sup>cation accuracy for this data set. Table 8 and Fig. 7 show the results of CBE cross-validation for the Haberman data set.

$$
\text { WHEN } \overline {{X}} _ {\mathrm{CBE}} ^ {33 \%} - \overline {{X}} _ {\mathrm{CBE}} ^ {34 \%} <   0. 0 1, \text { THEN }
$$

$$
\begin{array}{r l} \text {Max} & \{\text {no.of 33\% samples, no.of 10\% samples} \} \cdot \text {data size} \\ & = 33 \% \cdot 3 0 6 \\ & = 1 0 1 \end{array}\tag{23}
$$

Using the above equation, we determine the optimal training data size to be 101. With that, we consider the geometric structure of the optimal training data is stable.

By a similar procedure, the optimal number of experiment runs is:

$$
\begin{array}{r l} & \text { CALCULATE } \frac {\left(Z _ {\alpha / 2}\right) ^ {2} 0 . 0 1 9 ^ {2}}{(0 . 0 5 \cdot 1 . 1 3 2) ^ {2}} = 9. 9 7 3, \text { THEN } \\ & \text { Max } \{9. 9 7 3, 5 \} \\ & \approx 1 0 \end{array}\tag{24}
$$

where $\alpha { = } 0 . 0 5$ is the signi<sup>fi</sup>cance level, and 0:05⋅1:132 0:0566 is <sup>ð Þ¼</sup>the desired margin of error. We thus determine the optimal number of experiment runs to be 10.

We then use repeated random sub-sampling validation (with 204 (66%) training data points, 104 (34%) testing data points, experiment repeated 30 times) to validate that our CBE cross-validation (with 101 (33%) training data points, 205 (67%) testing data points, experiment repeated 10 times) is ef<sup>fi</sup>cient. The average and standard deviations of the SVM with the repeated random sub-sampling validation are 74.027 and 3.219, respectively, and the average and standard deviations of the SVM with the CBE cross-validation are 73.058 and

![](/api/attachments/CAZEBHN6/fulltext/images/c834d5d5f993308f2635c9fd6f338215e93f71b4ac5d7019ebe8a6667d8ecee4.jpg)  
Fig. 6. Relationship between CBE indexes and accuracies with the Haberman data set (correlation coef<sup>fi</sup>cient=0.827).

2.024. The performances of the two cross-validations have insignificant differences (the P-value is 0.379, using the independent t-test). The average training time of the repeated random sub-sampling validation is $0 . 3 3 ^ { \ast } 3 0 = 9 . 9 \ : \mathrm { s } ,$ while that of the CBE cross-validation is $0 . 2 3 ^ { * } 1 0 = 2 . 3 ~ \mathrm { s } .$

We then use 10-fold cross-validation to validate that our CBE cross-validation is ef<sup>fi</sup>cient. The average and standard deviations of SVM with the <sup>fi</sup>ve-fold cross-validation are 75.124 and 2.168, respectively. The performances of the two cross-validation methods have insigni<sup>fi</sup>cant differences (the P-value is 0.075, using the independent t-test). The average training time of the 10-fold crossvalidation is $0 . 5 1 2 ^ { * } 1 0 = 5 . 1 2 s$

In addition, when we use 10% of the total data (the lower bound of the training data size) as the training data with <sup>fi</sup>ve experiment runs, the average and standard deviations of the SVM are 72.913 and 3.641, and it has signi<sup>fi</sup>cant differences with the CBE cross-validation (the Pvaluebb 0.01, using the independent t-test). The average training data is $0 . 1 8 ^ { * } 5 = 0 . 9 s .$ . By considering validation effectiveness, the CBE cross-validation is thus again considered better than the crossvalidation using the lower bounds of training data size and experiment runs. Therefore, CBE cross-validation is an ef<sup>fi</sup>cient and effective method.

## 4.2.3. The Australian credit approval

First, for numerical independent variables analysis, we delete the categorical independent variables $\mathbf { X } _ { 1 } , \mathbf { X } _ { 4 } , \mathbf { X } _ { 8 } , \mathbf { X } _ { 9 } , \mathbf { X } _ { 1 1 } , { \mathrm { a n d } } \mathbf { X } _ { 1 2 }$ and delete the data that have missing value. The relationship between the CBE indexes and classi<sup>fi</sup>cation accuracies is shown in Table 9 and Fig. 8.

From the table and <sup>fi</sup>gure above we can see a highly positive correlation between the CBE index and classi<sup>fi</sup>cation accuracy.

Haberman data set with 31 samples selected as the training data (Default MinPt=2).

<table><tr><td>Accuracy</td><td>73.3</td><td>76.67</td><td>80</td><td>76.67</td><td>80</td><td>76.67</td><td>83.33</td><td>80</td><td>86.67</td><td>86.67</td></tr><tr><td>CBE index</td><td>1.66</td><td>1.884</td><td>2.055</td><td>2.289</td><td>2.492</td><td>2.703</td><td>2.75</td><td>3.552</td><td>3.697</td><td>4.54</td></tr></table>

Table 9  
Table 8  
The averages and standard deviations (SD) of CBE indexes with increasing the size of the training data set for the Haberman data set. (Bold value means the optimal data size).

<table><tr><td>Training data</td><td>42 (14%)</td><td>52 (17%)</td><td>61 (20%)</td><td>70 (23%)</td><td>73 (24%)</td><td>77 (25%)</td><td>80 (26%)</td><td>83 (27%)</td></tr><tr><td>Average</td><td>2.532</td><td>2.298</td><td>2.417</td><td>2.165</td><td>2.092</td><td>2.105</td><td>2.066</td><td>2.019</td></tr><tr><td>SD</td><td>1.104</td><td>0.706</td><td>0.874</td><td>0.361</td><td>0.692</td><td>0.518</td><td>0.726</td><td>0.512</td></tr><tr><td>Training data</td><td>86 (28%)</td><td>89 (29%)</td><td>92 (30%)</td><td>95 (31%)</td><td>97 (32%)</td><td>101 (33%)</td><td>104 (34%)</td><td></td></tr><tr><td>Average</td><td>1.452</td><td>1.349</td><td>1.342</td><td>1.362</td><td>1.287</td><td>1.131</td><td>1.122</td><td></td></tr><tr><td>SD</td><td>0.395</td><td>0.292</td><td>0.288</td><td>0.315</td><td>0.255</td><td>0.091</td><td>0.057</td><td></td></tr></table>

![](/api/attachments/CAZEBHN6/fulltext/images/a614e89388d02a82d6d828171ef2543321ff5d85cc065d316ef9ad204873b7ac.jpg)  
Fig. 7. Relationship between training size and the CBE index with the Haberman data set.

Australian data set with 1,902 samples selected as training data (Default MinPt=3).

<table><tr><td>Accuracy</td><td>68.12</td><td>68.44</td><td>69.4</td><td>70.37</td><td>70.05</td><td>71.01</td><td>71.18</td><td>71.82</td><td>71.66</td><td>72.62</td></tr><tr><td>CBE index</td><td>2.868</td><td>2.998</td><td>3.042</td><td>3.059</td><td>3.572</td><td>3.868</td><td>4.467</td><td>4.867</td><td>4.96</td><td>5.021</td></tr></table>

Table 10 and Fig. 9 show the results of CBE cross-validation for the Australian data set.

$$
\text { WHEN } \overline {{X}} _ {\mathrm{CBE}} ^ {42 \%} - \overline {{X}} _ {\mathrm{CBE}} ^ {43 \%} <   0. 0 1, \text { THEN }
$$

$$
\begin{aligned} \text{Max}\{\text{no.of 37\% samples, no.of 10\% samples}\} & \cdot \text{data size}\\ = 42\% \cdot 690 \\ = 290 \end{aligned}\tag{25}
$$

By a similar procedure, we determine the optimal number of training data points to be 290, and measure the optimal number of experiment runs as:

$$
\begin{array}{r l} & \text { CALCULATE } \frac {\left(Z _ {\alpha / 2}\right) ^ {2} 0 . 0 8 3 ^ {2}}{(0 . 0 5 \cdot 2 . 2 3 1) ^ {2}} = 2. 1 2 7, \text { THEN } \\ & \text { Max } \{2. 1 2 7, 5 \} \\ & = 5 \end{array}\tag{26}
$$

where $\alpha { = } 0 . 0 5$ is the signi<sup>fi</sup>cance level, and 0:05⋅2:231 = 0:1116 is <sup>ð Þ</sup>the desired margin of error. We determine the optimal number of experiment runs to be <sup>fi</sup>ve.

![](/api/attachments/CAZEBHN6/fulltext/images/1122bfc1a2ab604601f7497e635565472b3263d9586fdcffc4a816aeac9db53b.jpg)  
Fig. 8. Relationship between CBE indexes and accuracies with the Australian data set (correlation coefficient =0.892).

Again, when we use repeated random sub-sampling validation (with 455 (66%) training data points, 235 (34%) testing data points, experiment repeated 30 times) to validate that our CBE crossvalidation (with 290 (42%) training data points, 400 (58%) testing data points, experiment repeated 5 times) is ef<sup>fi</sup>cient. The average and standard deviations of the SVM with the repeated random subsampling validation are 79.17 and 1.302, respectively, and the average and standard deviations of the SVM with the CBE cross-validation are 77.870 and 1.504. The performances of the two cross-validations have insigni<sup>fi</sup>cant differences (the P-value is 0.305, using the independent t-test). The average training time of the repeated random subsampling validation is $1 . 8 3 * 3 0 = 5 4 . 9 \ s ,$ , and that of the CBE crossvalidation is $1 . 8 4 ^ { * } 5 = 9 . 2 ~ \mathrm { s } .$

When we use <sup>fi</sup>ve-fold cross-validation to validate CBE crossvalidation, the average and standard deviations of SVM with the <sup>fi</sup>vefold cross-validation are 79.2 and 1.351, respectively. Thus, the performance of the two cross-validation methods has insigni<sup>fi</sup>cant differences (the P-value is 0.333, using the independent t-test). The average training time of the <sup>fi</sup>ve-fold cross-validation is $1 . 9 8 ^ { \ast } 5 = 9 . 9 ~ \mathrm { s } .$

In addition, using 10% of the total data (the lower bound of the training data size) as training data with <sup>fi</sup>ve experiment runs, the average and standard deviations of SVM are 74.124 and 2.169, showing signi<sup>fi</sup>cant differences with the CBE cross-validation (the P-valuebb0.01, using the independent t-test). The average training data is $1 . 4 9 ^ { * } 5 = 7 . 5$ s. Similarly, the CBE cross-validation is better than the cross-validation using the lower bounds of the training data size and experiment runs. Therefore, CBE cross-validation is an ef<sup>fi</sup>cient and effective method.

## 4.3. Discussion of CBE index for various data characteristics

In this subsection, we apply sensitivity analysis to the calculation of the CBE index using unbalanced classes, dimensions, and sample sizes of a data set as the attributes.

## 4.3.1. Unbalanced class

Nguyen and Yonggwan proposed that the accuracy of classi<sup>fi</sup>ers goes down as the unbalanced level increases. Speci<sup>fi</sup>cally, they used

Table 10  
The averages and standard deviations (SD) of CBE indexes with increasing the size of the training data set for the Australian data set. (Bold value means the optimal data size).

<table><tr><td>Training data</td><td>23 (10%)</td><td>138 (20%)</td><td>173 (25%)</td><td>207 (30%)</td><td>242 (35%)</td></tr><tr><td>Average</td><td>3.051</td><td>2.873</td><td>2.651</td><td>2.501</td><td>2.371</td></tr><tr><td>SD</td><td>0.397</td><td>0.185</td><td>0.146</td><td>0.2</td><td>0.139</td></tr><tr><td>Training data</td><td>276 (40%)</td><td>283 (41%)</td><td>290 (42%)</td><td>296 (43%)</td><td></td></tr><tr><td>Average</td><td>2.283</td><td>2.256</td><td>2.231</td><td>2.225</td><td></td></tr><tr><td>SD</td><td>0.097</td><td>0.089</td><td>0.083</td><td>0.063</td><td></td></tr></table>

SVM as the classi<sup>fi</sup>cation tool and found that it was affected by the unbalanced effect [19]. In our experiments, we <sup>fi</sup>rst consider the unbalanced class characteristic of a data set with the same data structure. We generate data sets by <sup>fi</sup>xing the positive sample size and increasing the negative sample size, and the results are shown in Table 11. Table 11 shows that the higher the unbalanced level, the higher the data complexity and the lower the CBE index.

## 4.3.2. Dimensions

For a <sup>fi</sup>xed sample size, adding dimensions will degrade the performance (high data complexity) of a classi<sup>fi</sup>er if the number of training data points is small relative to the number of dimensions [4]. For the second characteristic, a <sup>fi</sup>xed sample size of 50 is used. When increasing the number of dimensions with the same data structure, given that the number of training data is smaller than the number of dimensions in the experiments, the results are obtained and shown in Table 12. Table 12 shows that when the dimensions are high, the data complexity is also high, while the CBE index is low.

## 4.3.3. Sample size

For the third characteristic in our experiments, we use the same sample sizes for both classes, and these are increasing with the same structure. The results are shown in Table 13.

Table 13 shows that when the samples of both classes increase, the data complexity stays the same, as does the CBE index.

## 5. Conclusion and discussions

Our research develops an ef<sup>fi</sup>cient and effective cross-validation method called Complexity-based Ef<sup>fi</sup>cient (CBE) cross-validation. The CBE cross-validation uses the CBE index (calculated by exploring the data's geometric structure and noise) to precisely discover the data's characteristics and its non-linear complexity, in order to help understand the data set. We also employ the CBE index to calculate the optimal training data size and number of experiment runs. CBE cross-validation aims to reduce model evaluation time when a complex and computationally expensive classi<sup>fi</sup>er is used.

We expect that when we apply CBE cross-validation to real binary data sets, we can use the proposed method to <sup>fi</sup>nd the optimal training

Table 11  
Sensitivity analysis of the CBE index for unbalanced data sets.

<table><tr><td></td><td>Positive samples</td><td>Negative samples</td><td>MinPts</td><td>CBE index</td></tr><tr><td>Case1</td><td>100</td><td>100</td><td>8</td><td>2.122</td></tr><tr><td>Case2</td><td>100</td><td>150</td><td>10</td><td>2.087</td></tr><tr><td>Case3</td><td>100</td><td>200</td><td>12</td><td>1.887</td></tr><tr><td>Case4</td><td>100</td><td>250</td><td>14</td><td>1.653</td></tr><tr><td>Case5</td><td>100</td><td>300</td><td>16</td><td>1.481</td></tr></table>

Table 12  
Sensitivity analysis of the CBE index for various data dimensions

<table><tr><td></td><td>No. of dimensions</td><td>MinPts</td><td>CBE index</td></tr><tr><td>Case 1</td><td>50</td><td>2</td><td>1.501</td></tr><tr><td>Case 2</td><td>60</td><td>2</td><td>1.366</td></tr><tr><td>Case 3</td><td>70</td><td>2</td><td>1.318</td></tr><tr><td>Case 4</td><td>80</td><td>2</td><td>1.302</td></tr><tr><td>Case 5</td><td>90</td><td>2</td><td>1.296</td></tr></table>

## Table 13

Sensitivity analysis of the CBE index for various sample sizes of both classes.

<table><tr><td></td><td>Positive samples</td><td>Negative samples</td><td>MinPts</td><td>CBE index</td></tr><tr><td>Case 1</td><td>100</td><td>100</td><td>8</td><td>2.122</td></tr><tr><td>Case 2</td><td>150</td><td>150</td><td>12</td><td>2.116</td></tr><tr><td>Case 3</td><td>200</td><td>200</td><td>16</td><td>2.113</td></tr><tr><td>Case 4</td><td>250</td><td>250</td><td>20</td><td>2.112</td></tr><tr><td>Case 5</td><td>300</td><td>300</td><td>20</td><td>2.112</td></tr></table>

data and the number of experiment runs, to help researchers to develop more precise classi<sup>fi</sup>cation tools with less evaluation time. Thus this work can assist researchers in developing new classi<sup>fi</sup>cation tools.

The threshold criterion of $\cdot \frac { \overline { { x } } ^ { n \% } } { X _ { \mathrm { C B E } } } { - \overline { { X } } _ { \mathrm { C B E } } ^ { n + 1 \% } }$ , the lower bound sample size of 0.01, and the lower bound of experiment runs of <sup>fi</sup>ve are empirical values, that we hope to <sup>fi</sup>nd theoretical values in future studies. With regard to the setting of the threshold criterion of the lower bound, we consider that when the number of data is large, we do not want to use too few data for the analysis, even though the data is easy to classify, because the information lost could be signi<sup>fi</sup>cant, and thus it is very dif<sup>fi</sup>cult to convince decision makers intuitively. Besides, when we use these low limits, we are indicating that there are about 40% of the whole data that have the chance to be selected as the training data $\left( 1 - \left( 1 - ^ { 1 } / _ { 1 0 } \right) ^ { 5 } \approx 4 0 \% \right)$

As to the experiment being repeated 30 times, we consider that the CBE distribution will normally converge to a normal distribution when n is large. As a matter of convenience, we thus use 30 times to approximate a normal distribution. In fact, one may need to use Q-Q plot to check if the statistics (accuracy) does in fact follow a normal distribution.

![](/api/attachments/CAZEBHN6/fulltext/images/6bd1b1c45b9cd5e3d4dc4aadf8f2974874806e7f72af70f9410867396f515861.jpg)  
Fig. 9. Relationship between training size and CBE index of Australian data set.

CBE cross-validation is a binary classi<sup>fi</sup>cation validation method. However, multi-class classi<sup>fi</sup>cation problems are very common in both studies and real-world applications. Therefore, the study of CBE cross-validation with multiple classes is also considered as one direction for future research.

## References

[1] C.M. Bishop, Pattern Recognition and Machine Learning, Springer, 2006

[2] L.J. Cao, H.P. Lee, W.K. Chong, Modi<sup>fi</sup>ed support vector novelty detector using training data with outliers, Pattern Recognition Letters 24 (2003) 2479–2487.

[3] G. Casella, R.L. Berger, Statistical Inference, second edition, Duxbury, 2002.

[4] R. Clarke, H.W. Ressom, A. Wang, J. Xuan, M.C. Liu, E.A. Gehan, Y. Wang, The properties of high-dimensional data spaces: implications for exploring gene and protein expression data, Nature Reviews. Cancer 8 (1) (2008) 37–49.

[5] M. Daszykowski, B. Walczak, D.L. Massart, Looking for natural patterns in data part 1. density-based approach, Chemometrics and Intelligent Laboratory Systems 56 (2) (2001) 83–92.

[6] M. Daszykowski, B. Walczak, D.L. Massart, Representative subset selection, Analytica Chimica Acta 468 (2002) 91–103.

[7] M. Ester, H.P. Kriegel, J. Sander, X. Xu.,, A density-based algorithm for discovering clusters in large spatial databases with noisy, Proceedings of 2nd International Conference on Knowledge Discovery and Data Mining, Portland, 1996, pp. 226–231.

[8] M.T. Hagan, H.B. Demuth, M. Beale, Neural Network Design, Thomson, Singapore, 1996.

[9] H. Han, Y. Ko, J. Seo, Using the revised EM algorithm to remove noisy for improving the one-against-the-rest method in binary text classi<sup>fi</sup>cation, Information Processing and Management 43 (5) (2007) 1281–1293.

[10] T.K. Ho, A data complexity analysis of comparative advantages of decision forest constructors, Pattern Analysis and Applications 5 (2002) 102–112.

[11] M.Y. Hu, M. Shanker, G.P. Zhang, M.S. Hung, Modeling consumer situational choice of long distance communication with neural networks, Decision Support Systems 44 (4) (2008) 899–908.

[12] V.N. Vapnik, The Nature of Statistical Learning Theory, second editionSpringer, New York, 2000.

[13] M. Kantardzic, Data Mining: Concept, Model, Method, and Algorithms, Wiley-Interscience, 2003.

[14] E.W.M. Lee, Y.Y. Lee, C.P. Lim, C.Y. Tang, Application of a noisy classi<sup>fi</sup>cation technique to determine the occurrence of <sup>fl</sup>ashover in compartment <sup>fi</sup>res, Advanced Engineering Informatics 20 (2006) 213–222.

[15] D.C. Li, Y.H. Fang, An algorithm to cluster data for ef<sup>fi</sup>cient classi<sup>fi</sup>cation of support vector machines, Expert Systems with Applications 34 (2008) 2013–2018.

[16] D.C. Li, Y.H. Fang, A non-linearly virtual sample generation technique using cluster discovery and parametric equations of hypersphere, Expert Systems with Applications 36 (2009) 844–851.

[17] D.C. Li, C.W. Yeh, T.I. Tsai, Y.H. Fang, Susan C. Hu, Acquiring knowledge with limited experience, Expert Systems 24 (3) (2007) 162–170.

[18] E.B. Mansilla, On classi<sup>fi</sup>er domains of competence, Proceedings of the 17th International Conference on Pattern Recognition (ICPR'04), 2004.

[19] H.V. Nguyen, W. Yonggwan, Classi<sup>fi</sup>cation of unbalanced medical data with weighted Regularized Least Squares, Proceedings of the Frontiers in the Convergence of Bioscience and Information Technologies (IEEE), 2007, pp. 347–352.

[20] S. Piramuthu, M.J. Shaw, J.A. Gentry, A classi<sup>fi</sup>cation approach using multi-layered neural networks, Decision Support Systems 11 (5) (1994) 509–525.

[21] A.M. Rubinov, N.V. Soukhorkova, J. Ugon, Classes and clusters in data analysis European Journal of Operational Research 173 (2006) 849–865.

[22] C. Schaffer, Technical note: selecting a classi<sup>fi</sup>cation method by cross-validation, Machine Learning 13 (1993) 135–143.

[23] P.N. Tan, M. Steinbach, V. Kumar, Introduction to Data Mining, 1st edition, Pearson Addison, Wesley, Boston, 2006.

[24] I.H. Witten, Eibe was presented as. <sup>fi</sup>rst name and Frank as.surname. Please check if. appropriate.Eibe Frank, Data Mining: Practical Machine Learning Tools and Techniques, Second editionMorgan Kaufman, Amsterdam, 2005.

![](/api/attachments/CAZEBHN6/fulltext/images/131d521903a2ced85aada123d2b8aa5e1e27f14a4d4b1f4edda7577390f342f7.jpg)  
Der-Chiang Li is a Distinguished Professor in the Department of Industrial and Information Management, the National Cheng Kung University, Taiwan. He received his Ph.D. degree at the Department of Industrial Engineering at Lamar University Beaumont, Texas, USA, in 1985. As a research professor, his current interest concentrates on learning with small data sets.

![](/api/attachments/CAZEBHN6/fulltext/images/675d3a2e554628701e136e54883ede31de1124d36aa9b9162db7bc809abf350d.jpg)

Yao-Hwei Fang is a postdoctoral fellow in the Division of Biostatistics and Bioinformatics, National Health Research Institutes. He is working at the laboratory for statistical analysis of human genetic. He received his Ph.D. at the Department of Industrial and Information Management at National Cheng Kung University, Taiwan, in 2009.

![](/api/attachments/CAZEBHN6/fulltext/images/4565f412c9fde0dcc6721ebe54b5ed479c7b2f198e2c329332de30291d562644.jpg)

Y.M. Frank Fang obtained his PhD degree from the Department of Civil and Hydraulic Engineering, Feng Chia University in 2006. Before he joined the Department of Civil and Hydraulic Engineering of Feng Chia University (FCU) in 2006, he worked as a post doctoral researcher in Geographic Information Systems Research Center, Feng Chia University. Currently, Assistant Professor Fang is Chief Researcher of Geographic Information Systems Research Center. FCU. His research interests include disaster Mon: itoring and civil engineering.
