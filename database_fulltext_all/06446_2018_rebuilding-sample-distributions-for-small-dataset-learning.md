---
otero_id: 6446
otero_key: "5G3NWNQF"
title: "Rebuilding sample distributions for small dataset learning"
authors: "Der-Chiang Li; Wu-Kuo Lin; Chien-Chih Chen; Hung-Yu Chen; Liang-Sian Lin"
year: "2018"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2017.10.013"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

Rebuilding sample distributions for small dataset learning

Der-Chiang Li, Wu-Kuo Lin, Chien-Chih Chen, Hung-Yu Chen, Liang-Sian Lin

![](/api/attachments/5G3NWNQF/fulltext/images/458aaa548bb7a9ab5e0982e7ae7d2b108e8f9911b11d6fe0af4a853d64075c3e.jpg)

<table><tr><td>PII:</td><td>S0167-9236(17)30201-4</td></tr><tr><td>DOI:</td><td>doi:10.1016/j.dss.2017.10.013</td></tr><tr><td>Reference:</td><td>DECSUP 12894</td></tr><tr><td>To appear in:</td><td>Decision Support Systems</td></tr><tr><td>Received date:</td><td>31 March 2017</td></tr><tr><td>Revised date:</td><td>28 October 2017</td></tr><tr><td>Accepted date:</td><td>29 October 2017</td></tr></table>

Please cite this article as: Der-Chiang Li, Wu-Kuo Lin, Chien-Chih Chen, Hung-Yu Chen, Liang-Sian Lin , Rebuilding sample distributions for small dataset learning. The address for the corresponding author was captured as affiliation for all authors. Please check if appropriate. Decsup(2017), doi:10.1016/j.dss.2017.10.013

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Rebuilding Sample Distributions for Small Dataset Learning

Der-Chiang Li\*, Wu-Kuo Lin, Chien-Chih Chen, Hung-Yu Chen, Liang-Sian Lin Department of Industrial and Information Management, National Cheng Kung University, University Road, Tainan 70101, Taiwan, R.O.C E-mail address: \*lidc@mail.ncku.edu.tw \*Corresponding author. Tel: (886) 2757575 x53134; Fax: (886) 2374252

## Abstract

Over the past few decades, a few learning algorithms have been proposed to extract knowledge from data. The majority of these algorithms have been developed with the assumption that training sets can denote populations. When the training sets contain only a few properties of their populations, the algorithms may extract minimal and/or biased knowledge for decision makers. This study develops a systematic procedure based on fuzzy theories to create new training sets by rebuilding the possible sample distributions, where the procedure contains new functions that estimate domains and a sample generating method. In this study, two real cases of a leading company in the thin film transistor liquid crystal display (TFT-LCD) industry are examined. Two learning algorithms—a back-propagation neural network and support vector regression—are employed for modeling, and two sample generation approaches—bootstrap aggregating (bagging) and the synthetic minority over-sampling technique (SMOTE)—are employed to compare the accuracy of the models. The results indicate that the proposed method outperforms bagging and the SMOTE with the greatest amount of statistical support.

Keyword: Small data, virtual sample, data preprocessing

## 1. Introduction

Over the past few decades, numerous machine learning algorithms have been developed to extract knowledge from data [1]. However, the majority of these algorithms were developed based on the assumption that training sets can represent the properties of populations. Conversely, if the training data contain insufficient information about the populations, the learning algorithms may output less precise results for future events.

## 1.1 Background

Although issues related to big-data learning have only attracted attention in recent years, issues related to small-data learning were revealed by Student's t-distribution [2] in 1908. The collection of additional samples to enlarge a sample size and ensure that algorithms can perform sufficient learning is sometimes difficult and/or expensive in certain situations, such as the diagnoses of rare diseases [3, 4], examination of deoxyribonucleic acid (DNA) microarrays [5], pattern recognition with limited pixels [6, 7], development of new products [8], and systems in their initial stages [9]. Methods for effectively learning robust and accurate information from small data is an issue that is worthy of additional research.

To demonstrate how small data affect the learning results of most algorithms, Fig. 1 displays two possible distributions of two small datasets with regard to their populations. In Fig. 1(a), the instances are evenly distributed in a population. Although most learning approaches can extract exact knowledge from a population, only a small amount of information will be obtained. Conversely, in Fig. 1(b), the instances are concentrated in a part of the population. The majority of learning approaches will produce biased outcomes regardless of the data size.

![](/api/attachments/5G3NWNQF/fulltext/images/868ab5a1cb111c6c900c78222ab6e4f8c03fe1131818e98a9fa53200384dd398.jpg)  
(a) Instances are evenly distributed (b) Instances are bias distributed  
Fig. 1. Two situations in which small data may be distributed relative to the populations

In addition to the sample distribution, another issue that can cause insufficient information to be obtained are the gaps between two observations in small data. As shown in Fig. 2, although the observations are evenly distributed in the population, gaps exist between filled with observations in a complete dataset; however, these observations are not available. Most learning algorithms fail to train their patterns with the unavailable instances in the information gaps in small datasets, and therefore, the obtained information is inadequate. For example, most tree-based algorithms, such as the C4.5 decision tree [10], need to partition continuous data into discrete intervals before evaluating the classification purity. However, the expected size of an interval is usually unavailable in small datasets since some intervals that contain no observations are integrated with their nearest intervals. If an insufficient number of candidate positions exist for the purity evaluation, then the trees that are built and the resulting hierarchy of the classification rules will be small.

![](/api/attachments/5G3NWNQF/fulltext/images/d6b6922a44a4fc7656ec0450bdfaa54120692b6c6a9ad9ba5e1577dcc1f15e0b.jpg)  
Fig. 2. Distribution of a small dataset and its unknown population

## 1.2 Related studies

Virtual sample generation (VSG) methods can be employed to address the learning problem of small data. These methods are a type of data-preprocessing method that is applied in the process of knowledge discovery in databases (KDD) [11]; research has demonstrated their effectiveness [12]. One of the most extensively applied VSG methods is the bootstrapping procedure (BP) which creates new training sets (referred to as bootstrapping sets) by resampling instances from the original data with a certain probability. The benefit of this approach is that most learning algorithms train a sample at least twice to gradually revise the identified patterns, which enables them to represent the behaviors of the actual data. To overcome the over-fitting issue in training sets, numerous ensemble learning methods were developed, such as bagging [14] and random forests [15], which employ BP to create bootstrapping sets for algorithms to build classifiers and determine classes by voting. Currently, bagging and random forests are extensively applied to extract knowledge from big data since each bootstrapping set can denote one evenly distributed part of a population.

When applying bagging or random forests to learn with small data, the use of bootstrapping sets may create two issues: an unstable data structure and overfitting, as shown in Fig. 3(a) and Fig. 3(b), respectively. A comparison of Fig. 2 with Fig. 3(a) reveals that certain observations in Fig. 2 are missing in Fig. 3(a) because they were not selected with a certain probability when forming the bootstrapping sets. The number of observations is very small, and thus, the difference between the features of the two bootstrapping sets in Fig. 3(a) is large. Since the amount of information provided by small data is minimal, any missing observations in the bootstrapping sets can increase the loss of information. Although we can double the observations to form the bootstrapping sets, as shown in Fig. 3(b), this step usually causes the patterns identified by the algorithms to represent the behaviors of a few 3(b) does not increase because the increased information is the same information provided by the same observations.

![](/api/attachments/5G3NWNQF/fulltext/images/e87d43c311f89a7c7d175b8fef854f093cda03634215382bd73ad2873ddb9572.jpg)

Original observations Newly added observations Original observations become missing

![](/api/attachments/5G3NWNQF/fulltext/images/17f2ab09bef938bf0bc49ced7da2529cbe99402a022736c3e66b5bf1a853f134.jpg)  
Fig. 3. Bootstrapping sets of small data, where (a) are two possible sets, and (b) is the set for which the observations are doubled

# ACCEPTED MANUSCRIPT

The synthetic minority over-sampling technique (SMOTE) [16] was proposed to generate artificial samples that differ from the original samples in the minority class. Based on the k-nearest neighbors, the SMOTE generates synthetic data along continuous vectors between the minority class’s instances and their nearest neighbors, as shown in Fig. 4. Although the information gaps in the minority class are filled with synthetic instances, they are distributed within the domain of the real instances in the minority class. The method employed by the SMOTE to generate samples is simple and does not consider the possible distributions of the entire minority class.

The k nearest neighbors The domain synthetic samples distribute

![](/api/attachments/5G3NWNQF/fulltext/images/b63fe147c81b18c96bed0aae1a33260ff7804798489cc9c6443a308bf3188ef6.jpg)  
Fig. 4. Sample generating mechanism of SMOTE

Since the fuzzy theory was proposed by Zadeh [17] in 1965, it has been employed to handle uncertain events. For example, to expand crisp observations to fill the information gaps caused by a lack of data, Huang [18] proposed the principle of information diffusion, in which a normal diffusion function that is developed based on fuzzy theories is defined as

$$
\tilde {f} _ {n} (x) = \frac {1}{n h \sqrt {2 \pi}} \sum_ {i = 1} ^ {n} \exp \left[ - \frac {\left(x - x _ {i}\right) ^ {2}}{2 h ^ {2}} \right],\tag{1}
$$

where h is the diffusion coefficient and n is the attribute size. In 2004, Huang and Moraga [19] proposed the diffusion neural network (DNN), which derives a pair of artificial samples for each observation based on Eq. (1) to fill the information gaps. Since the parameter n in Eq. (1) are determined to be a constant when a dataset is given, Huang and Moraga [19] applied the part $\exp { \left[ - ( x - x _ { i } ) ^ { 2 } \big / 2 h ^ { 2 } \right] }$ to derive the virtual values of an observation (x, y) as $x ^ { \prime } { = } x { \pm } \sqrt { { - } 2 h _ { x } ^ { \ 2 } \ln \psi ( r ) }$ and $y ^ { \prime } { = } y \pm { \sqrt { { - } 2 h _ { y } ^ { \ 2 } \ln \psi ( r ) } }$ for a two-dimensional dataset, where h are the diffusion coefficients, which are the inductions from a large amount of simulation results in DNN, r is the correlation coefficient of input X and output Y, and ( )r is the transforming function, which is defined as

$$
\psi (r) = \psi (0. 9 + m \times 1 0 ^ {- 2}) \mapsto \underbrace {0 . 9 \dots 9 9} _ {m 9 s} \quad \forall r \in \left\{0. 9 1, 0. 9 2, \dots , 0. 9 9 \right\},\tag{2}
$$

mapping r into a possibility value. For example, if r is 0.93 (or 0.96), then m is 3 (or 6) and

Since DNN needs r to be greater than 0.9, the applicability of the DNN method is limited with regard to most practical cases. In addition, the distributions constructed by DNN have information gaps because DNN only considers the behavior of an individual observation rather than the behavior of an entire dataset.

## 1.3 Motivation

To improve the robustness and/or accuracy of the forecasting models produced by data preprocessing when learning with small data, this study proposes a systematical procedure to create new training sets by rebuilding possible sample distributions. The procedure contains a set of new functions that estimate the possible ranges of observations and a sample generation method that considers the relations among attributes, where the functions and the method are developed based on the fuzzy normal function [18] and fuzzy concepts, respectively.

In the experiments, two learning algorithms—a back-propagation neural network (BPN) and support vector regression (SVR)—are adopted to build models. Two VSG approaches—bagging (using BP) and the SMOTE—are employed to compare the effectiveness of the models. Two real cases of a leading company in the thin film transistor liquid crystal display (TFT-LCD) industry in Taiwan are examined. The results indicate that the proposed method is more effective than bagging and the SMOTE for learning from the two cases with the greatest amount of statistical support.

The remainder of this study is organized as follows. Section 2 introduces the proposed procedure, and Section 3 describes the experimental environment and the background of the two real cases. Section 4 discusses the experimental results, and Section 5 presents the conclusions of this paper.

## 2. Proposed methodology

Two steps can be employed to enhance the data structures of small data by rebuilding the possible sample distributions: estimating the sample distributions and creating new samples. Before introducing the proposed method, the notations in this work are defined.

## 2.1 Definitions of notations

Assume that a small dataset with m 1 input attributes $\{ X _ { i } \vert j = 1 , 2 , . . . , m - 1 \}$ , one output attribute $X _ { { _ m } }$ , and n instances, as listed in Table 1. The elements of the attributes are $\{ x _ { i , j } \vert i = 1 , 2 , . . . , n ; j = 1 , 2 , . . . , m \}$ , and $L B _ { j } , C L _ { j } , U B _ { j } ,$ min<sub>j</sub>, and max<sub>j</sub> are the estimated lower bound, center location, upper bound, minimum, and maximum values of $\{ X _ { j } \vert j = 1 , 2 , . . . , m \}$ respectively. In this section, these symbols will be used in the equations, figures, and tables.

Table 1. Small dataset

<table><tr><td rowspan="2">No. of instances</td><td colspan="5">Inputs</td><td>Output</td></tr><tr><td> $X_1$ </td><td>...</td><td> $X_j$ </td><td>...</td><td> $X_{m-1}$ </td><td> $X_m$ </td></tr><tr><td>1</td><td> $x_{1,1}$ </td><td>...</td><td> $x_{1,j}$ </td><td>...</td><td> $x_{1,m-1}$ </td><td> $x_{1,m}$ </td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td>i</td><td> $x_{i,1}$ </td><td>...</td><td> $x_{i,j}$ </td><td>...</td><td> $x_{i,m-1}$ </td><td> $x_{i,m}$ </td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td>n</td><td> $x_{n,1}$ </td><td>...</td><td> $x_{n,j}$ </td><td>...</td><td> $x_{n,m-1}$ </td><td> $x_{n,m}$ </td></tr></table>

## 2.2 Estimating sample distributions

In fuzzy theories, three major types of membership functions (MFs) are commonly applied to denote sample distributions, including Gaussian, trapezoidal and triangular MFs. However, the Gaussian MF restricts the distributions to symmetrical distributions, whereas they may also be asymmetrical in reality. In previous studies [20, 21] the comparison of triangular MFs and trapezoidal MFs indicated that the triangular MF is preferred and the trapezoidal MF will increase the computational complexity. Therefore, this study adopts the triangular MFs to denote the possible sample distributions of small data. Three steps are taken to complete this task: determining the location centers, deriving the domain bounds, and building the sample distributions with triangular MFs.

## 2.2.1 Determining location centers

In contrast with DNN, in which virtual values are created on both sides of an individual observation, this study estimates the possible distribution of observations. We need to determine the center location (CL) of a distribution to denote the position of the height in a triangular MF. Three possible candidates are the mode (Mo), the mean, and the median (Me). Mo is not applicable in this study because it does not usually exist in small data, with the exception of designed experiments. The mean is not considered as a suitable CL for small data since it is more likely to be affected by an extreme outlier than Mo and Me when sample sizes are very small, as shown by the example in Fig. 5, in which a box plot is drawn to scale the observations with only one observation on the right side of the mean. Although taking the mean or Me as CL does not make a difference, since their deviation is small when no observations are identified as an outlier, taking the mean as CL would probably increase the risk of making one observation represent a half distribution when an outlier exists. Therefore, Me is more suitable than Mo as the mean to be applied to small datasets as the CL in this study and is calculated by

$$
C L _ {j} = \left\{ \begin{array}{l l} \frac {x _ {\frac {n}{2} , j} ^ {\prime} + x _ {\frac {n}{2} + 1 , j} ^ {\prime}}{2}, & \text { if   } n = 2 z, \\ x _ {\frac {n + 1}{2}, j} ^ {\prime}, & \text { if   } n = 2 z + 1, \end{array} \right.\tag{3}
$$

where $\forall z \in \mathbf { N }$ $\{ \stackrel { . } { x _ { i , j } } | i = 1 , 2 , . . . , n ; j = 1 , 2 , . . . , m \}$ are the sorted values of $X _ { j }$ , and n is the sample size.

![](/api/attachments/5G3NWNQF/fulltext/images/9d16151448abb7fc4ade325add231eb2695a1e2e60d95dc232e5cc64de729bc4.jpg)  
Fig. 5. Box plot to scale a small dataset that has an outlier

## 2.2.2 Deriving domain bounds

In contrast to a DNN, in which the part $\exp \Bigl [ - ( x - x _ { i } ) ^ { 2 } \big / 2 h ^ { 2 } \Bigr ] \in ( 0 , 1 ]$ in Eq. (1) is used to derive the virtual values of an observation, this research applies this expression to estimate the possible domain of an attribute. Huang and Moraga [19] considered that $\left| { r } \right| = \exp \Bigl [ - ( x - x _ { i } ) ^ { 2 } \big / 2 h ^ { 2 } \Bigr ]$ , where r is the correlation coefficient between input X and output Y was reasonable. To satisfy the network structures to make the learning procedure converge, they decided to set $\scriptstyle \psi ( { \big | } r { \big | } ) = \exp [ - ( x - x _ { i } ) ^ { 2 } / 2 h ^ { 2 } ]$ , where $\psi ( | r | )$ is a transforming function that maps $| r |$ into a possibility value, as formulated in Eq. (2). We redefine this part as

$$
\varphi \left(\left| r _ {p, q} \right|\right) = \exp \left[ - \frac {\left(C L _ {p} - B _ {p}\right) ^ {2}}{2 \hat {s} _ {p} {} ^ {2}} \right]\tag{4}
$$

to derive the sample boundaries $B _ { p }$ of $X _ { p }$ , where $C L _ { p }$ is the center location of $X _ { p } , \ r _ { p , q }$ is the relation between $X _ { p }$ and $X _ { q } , p , q \in \{ \ 1 , 2 , . . . , m \}$ and $p \neq q , \hat { s } _ { p }$ is the sample standard deviation of $X _ { q }$ , and $\varphi \mathbf { \left( \vec { \mathbf { \Lambda } } \right) }$ is the transforming function defined as Eq. (5). Since ( ) only considers the situation in which $| r |$ is greater than 0.9, we define Eq. (5)—a modified sigmoid function—to make $\varphi ( r )$ between (0, 1] when the relation $r \in [ - 1 , 1 ]$ is given. Similar to how ( ) acts in a DNN, $\varphi \mathbf { \left( \vec { \mu } \right) }$ makes the diffusion width narrower when r is larger; conversely, this width is wider when r is smaller.

$$
\varphi (r) = \frac {1}{1 + \exp (- 1 0 (\left| r \right| - 0 . 5))}\tag{5}
$$

However, before introducing how to derive sample boundaries, we need to identify suitable indicators to be employed in Eq. (4) when working with small datasets. Eq. (4) contains two indicators: the correlation coefficient $r _ { p , q }$ and the sample standard deviation $\hat { s } _ { p }$

The correlation coefficient $r _ { p , q }$ is not suitable for measuring the relations in small datasets since it is computed by taking two means $( \hat { X } _ { p }$ and ${ \bar { X } } _ { q } )$ as the bases, which increases the risk that the results may be affected by outliers. Therefore, this study adopts the indicator trend similarity between attributes (TSA) [22] to replace r. The TSA was developed based on a non-parametric method to measure the relation (occurring trend) between two attributes in small data without considering the distances between observations and their CLs to avoid the effect of any potential outlier on the results. The similar trend $g ( i ) _ { p , q }$ of the $i ^ { \mathrm { { t h } } }$ instance between $X _ { p }$ and $X _ { q }$ is computed as

$$
g (i) _ {p, q} = \left\{ \begin{array}{l} 1, \text {if} (x _ {i, p} - C L _ {p}) (x _ {i, q} - C L _ {q}) > 0 \\ 0, \text {if} (x _ {i, p} - C L _ {p}) (x _ {i, q} - C L _ {q}) = 0 \\ - 1, \text {if} (x _ {i, p} - C L _ {p}) (x _ {i, q} - C L _ {q}) <   0 \end{array} , \right.\tag{6}
$$

where $i = 1 , 2 , . . . n$ $p , q \in \{ \ 1 , 2 , . . . , m \ \}$ and $p \neq q$ ; and the similar trend $S _ { p , q } \in [ - 1 , 1 ]$

between $X _ { p }$ and $X _ { q }$ is obtained by

$$
S _ {p, q} = \frac {1}{n} \sum_ {i = 1} ^ {n} g (i) _ {p, q}, p, q \in \{1, 2,..., m; p \neq q \}.\tag{7}
$$

The sample standard deviation $\widehat { s } _ { p } = \sqrt { \sum _ { i = 1 } ^ { n } ( x _ { i , p } - \overline { { x } } _ { p } ) ^ { 2 } \left/ n - 1 \right. }$ is the indicator that measures the average of the Euclidean distances from the mean $\overline { { \ v x } } _ { p }$ to the observations $x _ { \perp _ { p } }$ $\hat { s } _ { p }$ is also considered to be unsuitable for assessing the degree of dispersion in small datasets because it takes $\overline { { \ v x } } _ { p }$ as the data center, which is very likely to be affected by outliers. This research employs the Euclidean distances to evaluate the degree of dispersion from the observations to Me. The new indicator $d _ { p }$ for $X _ { p }$ is then calculated by

$$
d _ {p} = \sqrt [ u ]{\sum_ {i = 1} ^ {n} (x _ {i , j} - C L _ {j}) ^ {u} / n},\tag{8}
$$

where $p = 1 , 2 , . . . , m , u = 1 , 2 , . . .$ , and u is set to two in this study. Therefore, the final equation for deriving the boundaries of an attribute is formulated as

$$
\varphi \left(S _ {p, q}\right) = \exp \left[ - \frac {\left(C L _ {p} - B _ {p}\right) ^ {2}}{2 d _ {p} ^ {2}} \right],\tag{9}
$$

where $S _ { p , q } \in [ - 1 , 1 ]$ is the similar trend between $X _ { p }$ and $X _ { q } ~ ; ~ C L _ { p }$ and $B _ { p }$ are the center location (the median) and the bound values of $X _ { p }$ , respectively; $p , q \in \{ \ 1 , 2 , . . . , m \ \}$ and $p \neq q$ . We can derive the bound values as

$$
B _ {p} = C L _ {p} \pm d _ {p} \sqrt {- 2 \ln (\varphi (S _ {p , q}))}.\tag{10}
$$

When considering the effect of the locations of observations relative to $C L _ { p }$ on the distribution skewness, $B _ { p }$ is redefined as

$$
B _ {p} ^ {L} = C L _ {p} - \min \left\{d _ {p} ^ {L} \sqrt {- 2 \ln (\varphi (S _ {p , q}))} | q = 1, 2, \dots , m, q \neq p \right\}\tag{11}
$$

$$
B _ {p} ^ {U} = C L _ {p} + \min \left\{d _ {p} ^ {U} \sqrt {- 2 \ln (\varphi (S _ {p , q}))} | q = 1, 2, \dots , m, q \neq p \right\},\tag{12}
$$

where $d _ { p } ^ { L }$ and $d _ { p } ^ { U }$ are the averaged Euclidean distances computed by the observations, whose values are smaller than $C L _ { p }$ and larger than $C L _ { p }$ , respectively. The reason for taking the minimum diffusion width in Eq. (11) and Eq. (12) is to obtain the intersection when working with multiple attributes. When considering the situation in which the boundary values do not cover the current value domain [ min , max ] in $X _ { p }$ , as shown in Fig. 6, the lower bound $L B _ { p }$ and the upper bound $U B _ { p }$ are determined as

$$
L B _ {p} = \left\{ \begin{array}{l} B _ {p} ^ {L}, \quad \text { if } B _ {p} ^ {L} \leq \min _ {p} \\ \min _ {p}, \text { if } B _ {p} ^ {L} > \min _ {p} \end{array} \right.\tag{13}
$$

$$
U B _ {p} = \left\{ \begin{array}{l} B _ {p} ^ {U}, \quad \text { if } B _ {p} ^ {U} \geq \max _ {p} \\ \max _ {p}, \text { if } B _ {p} ^ {U} <   \max _ {p} \end{array} , \right.\tag{14}
$$

respectively.

![](/api/attachments/5G3NWNQF/fulltext/images/d972f244d5d254746e647c06ce4ac102b4b8f96ba317c339901546a4e6cd6d93.jpg)

![](/api/attachments/5G3NWNQF/fulltext/images/e5d45c3f811399ba741108a33a454d5710a3fbc840ecbd17df5d6bb1300054f9.jpg)  
Fig. 6. The situation that $\big [ B _ { p } ^ { L } , B _ { p } ^ { U }$ ] fails to cover [min<sub>p</sub>, max<sub>p</sub>]

## 2.2.3 Building sample distributions

When the three parameters $L B _ { j } , \ C L _ { j }$ , and $U B _ { j }$ of $X _ { j }$ are obtained, the process continues to construct a fuzzy triangular MF to denote the possible sample distribution, as shown in Fig. 7, where $j = 1 , 2 , . . . , m$ . The MF function $\mathrm { M F } _ { j } ( x )$ is defined as

$$
\mathrm{MF} _ {j} (x) = \left\{ \begin{array}{l l} \left(x - L B _ {j}\right) / \left(C L _ {j} - L B _ {j}\right), & \text { if } x \leq C L _ {j}, \\ \left(U B _ {j} - x\right) / \left(U B _ {j} - C L _ {j}\right), & \text { if } x > C L _ {j}, \\ 0, & \text { if } x <   L B _ {j} \text { or } x > U B _ {j} \end{array} . \right.\tag{15}
$$

![](/api/attachments/5G3NWNQF/fulltext/images/0b95d7b8f1bfe960c956807b505f0b44901ddf2826302ebce8f5a84e8447c95d.jpg)  
Fig. 7. Sample distribution with a triangular MF

## 2.3 Generating samples

This subsection introduces how to generate the corresponding synthetic values of an attribute when the other attribute values are given, how to create the given attribute values, and how to handle data with three or more dimensions.

## 2.3.1 Generating corresponding attribute values

To create samples with consideration of the relations among attributes, a procedure is developed based on the MFs and $\mathrm { T S A } .$ A. explain the procedure, an example is shown in Fig. 7, in which $\mathbf { M F } _ { p }$ and $\mathrm { M F } _ { q }$ denote the two sample distributions of $X _ { p }$ and $X _ { q }$ respectively; $p , q \in \{ \ 1 , 2 , . . . , m \ \}$ ; and $p \neq q$ . By projecting the $\mathrm { { M F } } _ { p } ( \nu _ { p } )$ of a virtual value $\nu _ { p }$ onto $\operatorname { M F } _ { q }$ , we can infer two possible virtual values $\nu _ { q }$ in $X _ { q }$ . The sign of $S _ { p , q }$ indicates the corresponding $\nu _ { q }$ when $\nu _ { p }$ is given. Taking Fig. 8 as an example, if $S _ { p , q }$ is positive, we choose the left $\nu _ { q }$ ; otherwise, we select the right $\nu _ { q }$ . The equation to obtain $\nu _ { q }$ is formulated as

$$
v _ {q} = \left\{ \begin{array}{l l} L B _ {q} + \mathrm{MF} _ {p} (v _ {p}) (C L _ {q} - L B _ {q}), & L B _ {q} \leq v _ {q} \leq C L _ {q} \\ U B _ {q} - \mathrm{MF} _ {p} (v _ {p}) (U _ {q} - C L _ {q}), & C L _ {q} <   v _ {q} \leq U B _ {q}. \\ 0, & \text { otherwise } \end{array} \right.\tag{16}
$$

![](/api/attachments/5G3NWNQF/fulltext/images/48d3685390333f436e85900d2c1287fbecdc472b7c78e3b298307df4175e2e2e.jpg)  
Fig. 8. Obtaining two possible $\nu _ { q }$ by projecting $\mathrm { M F } _ { \mathrm { p } } ( \nu _ { p } )$ onto $\mathrm { M F } _ { q }$

However, slight deviations between two real world values in different instances always exist, where the deviations are probably not measured due to the preciseness of the scales. Therefore, the strategy employed by this study is to project one value interval instead of one exact value, as in the two examples shown in Fig. 9 and Fig. 10. The interval bounds $[ \nu _ { p } ^ { - } , \nu _ { p } ^ { + } ]$ of $\nu _ { p }$ are obtained by

$$
v _ {p} ^ {-} = \left\{ \begin{array}{l l} v _ {p} - \theta_ {p, q} (U B _ {p} - L B _ {p}), & \text {if} v _ {p} - \theta_ {p, q} (U B _ {p} - L B _ {p}) \geq L B _ {p} \\ L B _ {p}, & \text {if} v _ {p} - \theta_ {p, q} (U B _ {p} - L B _ {p}) <   L B _ {p} \end{array} \right.\tag{17}
$$

$$
v _ {p} ^ {+} = \left\{ \begin{array}{l l} v _ {p} + \theta_ {p, q} (U B _ {p} - L B _ {p}), & \text { if } v _ {p} + \theta_ {p, q} (U B _ {p} - L B _ {p}) \leq U B _ {p} \\ U B _ {p}, & \text { if } v _ {p} + \theta_ {p, q} (U B _ {p} - L B _ {p}) > U B _ {p} \end{array} , \right.\tag{18}
$$

where $U B _ { p } - L B _ { p }$ is the sample range, and $\theta _ { p , q } \in ( 0 , 1 )$ is the diffusion coefficient, which determines the diffused widths.

![](/api/attachments/5G3NWNQF/fulltext/images/d3450a962e995abf78476a8f119cd90292f1e26f68c5a6f6541fa932bb1ea6e3.jpg)  
Fig. 9. Projecting $[ \mathrm { M F } _ { p } ( \nu _ { p } ^ { - } )$ $\mathrm { M F } _ { p } ( \nu _ { p } ^ { + } ) \mathrm { \Gamma } .$ ] onto $\mathrm { M F } _ { q }$ to estimate possible ranges of $X _ { q }$ when $S _ { p , q } > 0$ and $S _ { p , q }$ is large

![](/api/attachments/5G3NWNQF/fulltext/images/1f1995a018777febb3cf09b390f80253dc549d6af1bf6c8d69f60714285a555e.jpg)  
Fig. 10. Projecting $[ \mathrm { M F } _ { p } ( \nu _ { p } ^ { - } )$ $\mathrm { M F } _ { p } ( \nu _ { p } ^ { + } ) \big ]$ onto $\operatorname { M F } _ { q }$ to estimate possible ranges of $X _ { q }$ when $S _ { p , q } > 0$ and $S _ { p , q }$ is small

In this study, we consider a simple linear relation as an example to transform $\left| S _ { p , q } \right|$ into $\theta _ { p , q }$ as

$$
\theta_ {p, q} = a \times \left| S _ {p, q} \right| + b,\tag{19}
$$

where a and b are the coefficients to be determined. Apart from Eq. (19), other functions, such as a modified bipolar sigmoid, is applicable here. However, the transformation functions should adhere to the following principles:

1. When $\left| S _ { p , q } \right|$ is closer to 0, which implies that extracting the occurring trend between $X _ { p }$ and $X _ { q }$ from the observations is difficult, then the range $[ \nu _ { q } ^ { - } , \nu _ { q } ^ { + } ]$ within which $\nu _ { q }$ may be located can be very wide.

2. When $\left. S _ { p , q } \right. \mathrm { ~ i s ~ }$ closer to 1, the interval width $\nu _ { p } ^ { + } - \nu _ { p } ^ { - }$ and $\nu _ { q } ^ { + } - \nu _ { q } ^ { - }$ are narrow, which decreases the probability that $\nu _ { q }$ may be located on the opposite side relative to $C L _ { q }$ to retain their high relation degree.

If we expect the minimum diffusion coefficient and maximum diffusion coefficient to be 10% (or 1%) and 90% (or 99%), respectively, when $\left| S _ { p , q } \right|$ are 1 and 0, respectively, then we can derive a = -0.8 (or -0.98) and b = 0.9 (or 0.99) as the coefficients in $\operatorname { E q }$ . (19).

Note that three situations need to be considered when computing the corresponding interval bounds $[ \nu _ { q } ^ { - } , \nu _ { q } ^ { + }$ ]: the side of the location of $\nu _ { p }$ that is relative to $C L _ { p }$ , the sign of $S _ { p , q }$ , and whether $\nu _ { p } ^ { - }$ or $\nu _ { p } ^ { + }$ are on the opposite side of $C L _ { p }$ (as in the example in Fig. 10). A total of eight conditions can be applied to determine how to compute $\nu _ { q } ^ { - }$ and $\nu _ { q } ^ { + }$ Regardless of which of the eight conditions occurs, we can obtain two $\nu _ { q } ^ { - }$ and two $\nu _ { q } ^ { + }$ by solving the equations as $\mathbf { M F } _ { q } ( \nu _ { q } ^ { - } ) = \mathbf { M F } _ { p } ( \nu _ { p } ^ { - } )$ and $\mathbf { M F } _ { q } ( \nu _ { q } ^ { + } ) { = } \mathbf { M F } _ { p } ( \nu _ { p } ^ { + } )$ , respectively, and determine the proper $\nu _ { q } ^ { - }$ and $\nu _ { q } ^ { + }$ according to the three previously mentioned situations. When $\nu _ { q } ^ { - }$ and $\nu _ { q } ^ { + }$ are obtained, v is created by drawing one value from a uniform $\nu _ { q }$ distribution ${ [ \nu _ { q } ^ { - } }$ , $\nu _ { q } ^ { + }$ ].

## 2.3.2 Generating given attribute values

The previous subsection indicated two types of virtual values: the corresponding value $\nu _ { q }$ of $X _ { q }$ and the given value $\nu _ { p }$ of $X _ { p }$ . In this study, $\nu _ { p }$ is generated by the possibility assessment mechanism (PAM). When sample sizes are small, observations located near distribution edges are more likely to be identified as noise (outliers) by learning algorithms than observations located around distribution centers, where the noise would probably reduce the accuracy of any identified patterns. This paper employs PAM to decrease and increase the sizes of the synthetic values near the edges $\cdot ^ { L B _ { p } }$ and $U B _ { p } )$ and $C L _ { p }$ , respectively, and make the distribution of $\nu _ { p }$ obey the shape of $\mathrm { M F } _ { p }$ . In computer programming, the distribution of v will present a uniform distribution $\nu _ { p }$ $[ L B _ { p } , U B _ { p } ]$ if we directly take random seeds from a uniform distribution [0, 1] to generate $\nu _ { p }$ . PAM is a computer programming technique that was developed based on the concept of genetic algorithms [23], i.e., the ‘survival of the fittest’, to assess whether a random value satisfies the criterion for a suitable virtual value. The steps in PAM to create v are summarized as follows: $\nu _ { p }$

Step 1. Randomly take the value $\nu _ { p }$ from $[ L B _ { p } , U B _ { p } ]$ , and compute its MF value (i.e., the possibility) as $\mathbf { M F } _ { p } ( \nu _ { p } )$ using Eq. (15).

Step 2. Draw a random seed (rs) from a uniform distribution [0, 1] as the threshold value to assess whether the $\nu _ { p }$ can be reserved. Once $\mathbf { M F } _ { p } ( \nu _ { p } ) > r s$ , then $\nu _ { p }$ can be treated as a suitable virtual value of $X _ { p }$ ; otherwise, v should be discarded. $\nu _ { p }$

Step 3. Repeat Steps 1 to 2 until a suitable virtual value v is available. $\nu _ { p }$

The principle of PAM, as shown in Fig. 11, is the probability that an rs is lower than $\mathrm { { M F } } _ { p } ( \nu _ { p } )$ and is actually $\mathbf { M F } _ { p } ( \nu _ { p } )$ . Therefore, once $\mathrm { { M F } } _ { p } ( \nu _ { p } )$ is a larger value (i.e., $\nu _ { p }$ is closer to $C L _ { p } )$ $\nu _ { p }$ will have a higher probability of being a suitable virtual value. When additional $\nu _ { p }$ are generated using PAM, their distributions will obey the shapes of the estimated sample distributions rather than exhibiting a uniform distribution. Note that PAM does not intend to compare the possibility value in fuzzy theories with the probability value in statistics; however, it examines the probability of a given value (although it is an MF value) in a uniform distribution.

![](/api/attachments/5G3NWNQF/fulltext/images/e46db820b42b6a4fb30cc858365071cabbbace47c70d9d8f286b8591881c7174.jpg)  
Fig. 11. Principle of the possibility assessment mechanism

## 2.3.3 Generating high-dimensional data

When learning two-dimensional data, a virtual sample is created by employing PAM to generate a $\nu _ { 1 }$ of $X _ { 1 }$ and taking the $\nu _ { 1 }$ to create its corresponding $\nu _ { 2 }$ of $X _ { 2 }$ . When working with multiple dimensional data, this process can be continued by taking $\nu _ { 2 }$ to create its corresponding $\nu _ { 3 }$ of $X _ { 3 }$ until all virtual values of the m attributes are created to complete one virtual sample. Although the previously mentioned process is simple, it has the $X _ { 1 } , X _ { 2 } ,$ and $X _ { 3 }$ listed in Table 2 as examples. If the previously mentioned process is employed to generate samples by directly taking the sequence $\{ X _ { 1 } , X _ { 2 } , X _ { 3 } \}$ , the relations between $( X _ { 1 } , X _ { 2 } )$ and $( X _ { 2 } , X _ { 3 } )$ may be kept in a certain degree but the relation between $( X _ { 1 } , X _ { 3 } )$ may be lost, i.e., most $\nu _ { 1 }$ and $\nu _ { 3 }$ become located on the opposite side relative to their CLs since the process does not consider the relation between $( X _ { 1 } , X _ { 3 } )$ . To reduce the risk, two processes are needed: determining the generating sequence of attributes and applying a learning procedure to retain the relations.

Table 2. Example of a TSA matrix in a high-dimensional dataset

<table><tr><td></td><td> $X_{1}$ </td><td> $X_{2}$ </td><td> $X_{3}$ </td><td> $X_{4}$ </td><td> $X_{5}$ </td></tr><tr><td> $X_{1}$ </td><td>-</td><td>0</td><td>0.7</td><td>0.8</td><td>0.5</td></tr><tr><td> $X_{2}$ </td><td></td><td>-</td><td>-0.9</td><td>-0.8</td><td>0.6</td></tr><tr><td> $X_{3}$ </td><td></td><td></td><td>-</td><td>0.7</td><td>0.4</td></tr><tr><td> $X_{4}$ </td><td></td><td></td><td></td><td>-</td><td>0.5</td></tr><tr><td> $X_{5}$ </td><td></td><td></td><td></td><td></td><td>-</td></tr></table>

The principles for determining the generating sequence are summarized, with an example given in Table 2.

1. Arrange the attributes whose absolute TSA (|S|) values are larger in the anterior parts of the sequences as much as possible, since their diffusion widths are narrower. This step can prevent the loss of additional relations in the beginning stage. In Table 2, since the maximum |S| is |-0.9|, the first attribute can be decided as $X _ { 2 }$ or $X _ { 3 }$ . When we begin searching from $X _ { 2 } ,$ the second attribute is $X _ { 3 }$ and the maximum |S| in $\{ | S _ { 3 , j } | , j { = } 1 , 4 , 5 \}$ are $| S _ { 3 , 1 } | { = } 0 . 7$ and $| S _ { 3 , 4 } | { = } 0 . 7 .$ From here, the sequence makes a branch. When the searching terminates, two possible sequences can be obtained as $\{ X _ { 2 } , X _ { 3 } , X _ { 1 } , X _ { 4 } , X _ { 5 } \}$ (marked as Seq1) and $\{ X _ { 2 } , X _ { 3 } , X _ { 4 } , X _ { 1 } , X _ { 5 } \}$ (marked as $S e q 2 )$ . When we begin searching from $X _ { 3 } .$ , the sequence is determined as $\{ X _ { 3 } , X _ { 2 } , X _ { 4 } , X _ { 1 } , X _ { 5 } \}$ (marked as Seq3).

2. Select the sequence whose sum of |S| is the largest to prevent the loss of additional total relations. In this example, the sums of |S| in Seq1, Seq2, and Seq3 are $( | - 0 . 9 | + | 0 . 7 | +$ $| 0 . 8 | + | 0 . 5 | ) = 2 . 9 , ( | - 0 . 9 | + | 0 . 7 | + | 0 . 8 | + | 0 . 5 | ) = 2 . 9 , \mathrm { a n d } ( | - 0 . 9 | + | - 0 . 8 | + | 0 . 8 | + | 0 . 5 | ) = 3 . 9 ,$ respectively. Therefore, Seq3 is adopted.

3. Consider the sequence whose |S| values are larger in the anterior parts of sequence once two or more sequences whose sums of |S| are equivalent. Assume that a fake sequence (marked as Seq4), whose |S| are {-0.9, -0.8, 0.5, 0.8} and its sum of |S| happens to be the same as Seq3, is given. Seq3 is preferred since its third |S| (0.8) is larger than its third |S (0.5) in Seq4.

However, when attribute sizes are large, the relations of the created samples may present the bullwhip effect [24], i.e., the relations among attributes become biased in the posterior parts in the sequences since their |S| values are smaller (even close to zero) after sequences are arranged. To control this outcome, a learning mechanism is suggested by taking the intersections of the estimated ranges of the prior attributes in the sequence. Taking Seq3, for instance, the final diffused range $[ \nu _ { 4 } ^ { - } , \nu _ { 4 } ^ { + } ]$ for the third attribute (X ) is the intersection of the attributes obtained by treating $( X _ { 3 } , X _ { 4 } )$ and $( X _ { 2 } , X _ { 4 } )$ , the final diffused range for the fourth attribute (X<sub>1</sub>) is the final diffused range of the attributes obtained by treating $( X _ { 3 } , X _ { 1 } ) , ( X _ { 2 } , X _ { 1 } )$ and $( X _ { 4 } , X _ { 1 } )$ . This mechanism increases the time complexity to O m(( 1) !) .

## 3. Experimental environment

This section presents the designs of experiments and a description of two real cases of a TFT-LCD maker in Taiwan.

## 3.1 Experimental designs

In this study, we adopt a k-fold like cross-validation procedure to implement the experiment k times to obtain even results, where each cross-validation involves preparing, training, and testing stages, as shown in Fig. 12.

![](/api/attachments/5G3NWNQF/fulltext/images/cfc26bf7dc6632755980269dc51f4219f6ec8e0dee0c1c4eb799a30a1a7dcf60.jpg)  
Fig. 12. Experimental design in this study

At the preparing stage, n instances are randomly drawn from the dataset as the training set, and the remaining N-n experiment is implemented with one control and three experiment groups. In the control group, the training set is regarded as a given small data set (SDS). In experiment groups 1, 2, and 3, the training set is replaced by a new training set created by BP (in bagging), the SMOTE, and the proposed method (PM), respectively, where the new training sets contain n real and M artificial instances. The algorithms that were adopted to learn the training sets are BPN and SVR. Consequently, a total of eight models are constructed. At the testing stage, the testing set is used to evaluate the forecasting errors of the eight models, where the errors are indicated by the mean absolute percentage error (MAPE) and are computed by

$$
\mathrm{MAPE} = \frac {1}{N - n} \sum_ {i = 1} ^ {N - n} \left| \frac {y _ {i} - \hat {y} _ {i}}{y _ {i}} \right|,\tag{20}
$$

where y<sub>i</sub> is the output value of the $i ^ { \mathrm { { t h } } }$ instance in the testing set, and $\hat { y } _ { i }$ is the prediction of y<sub>i</sub>. When the k cross-validations with a given training size n are completed, the final result is represented by the average of the k MAPEs, where the averaged MAPE (AvgMAPE) is computed by

$$
\text { AvgMAPE } = \frac {1}{k} \sum_ {j = 1} ^ {k} \text { MAPE } _ {j}.\tag{21}
$$

To identify whether significant differences exist between group 3 and the other three groups with statistical support, paired t-tests with a two-tailed test are performed. The null hypothesis (H<sub>0</sub>) and alternative hypothesis $\mathrm { ( H _ { a } ) }$ are formulated as

$$
\left\{ \begin{array}{l} \mathrm{H} _ {0}: \mu_ {d} = 0 \\ \mathrm{H} _ {\mathrm{a}}: \mu_ {d} \neq 0 \end{array} \right.,\tag{22}
$$

where $\mu _ { d }$ is the average of $\{ d _ { j } \vert j = 1 , 2 , . . . , k \ \}$ , and $d _ { j }$ is the deviation between the MAPE of control group 3 and the MAPE of the other three groups in the $j ^ { \mathrm { t h } }$ cross-validation run.

In addition, the experiments also contain a sensitivity analysis, in which two parameters, the training sizes n and the artificial sample sizes $M ,$ are designed. The objective of the analysis is to examine the effect of n and M on the experimental results.

The parameters in the experiments are described as follows: The number of times each experiment is repeated (k) in each n is 30, the sensitivity analysis of the training sizes n are set depending on the cases, the artificial instance sizes M are 100%, $2 0 0 \% . . . ,$ , and 1000% relative to n, and the test level for the paired t-test is 0.05.

The software that was employed to help build the models is Weka 3.80, in which BPN, SVR, and bagging are employed; these models are denoted as “MultilayerPerceptron,” “SMOreg,” and “bagging,” respectively. Weka can also implement the SMOTE after downloading the package from the option “Package manager”. The parameters for BPN and SVR in Weka are set as the defaults, where the default kernel of SVR is “PolyKernel”. The parameters for bagging and the SMOTE also take the defaults, with the exception of the artificial instance sizes M. Although Weka’s SMOTE cannot be directly applied to numerical forecasting cases, we can add fake class values to the data to create a minority class that is accepted by Weka’s SMOTE.

## 3.2 Case description

Three major processes are required to make a TFT-LCD panel: the TFT process (or array), the CF process (color filter), and the LCD process (or cell). In the TFT and CF processes, transistors are fabricated on a glass substrate. In the LCD process, the arrayed back substrate and the CF front substrate are assembled, and then the space between these substrates is filled with liquid crystal.

Two real learning tasks are examined in the experiments, as summarized in Table 3. The first task (Case I) in the LCD process is to estimate the biased distances between the TFT substrates and the CF substrates when they are assembled using only a few samples that contain the six measured deviations on the CF substrates. The second task (Case II) in the CF process is to infer the height of the photo spacer (PSH), which creates the space between the TFT substrates and the CF substrates to be filled by the liquid crystal when the CF process is completed.

Table 3. Two datasets examined in the empirical evaluation

<table><tr><td>Case No.</td><td>Instance sizes</td><td>Attribute sizes</td><td>Learning targets</td></tr><tr><td>I</td><td>19</td><td>7</td><td>Predicting the shift between two assembled glass substrates in the LCD process using the six scales measured in the CF process.</td></tr><tr><td>II</td><td>30</td><td>4</td><td>Estimating the measured photo-spacer height (PSH) on a CF glass substrate when the CF process is completed.</td></tr></table>

## 4. Experimental results and discoveries

In the sensitivity analysis, the training size n in Case I is 5, 10, and 15; in Case II, the training size n is 5, 10, 15, and 20. The experimental results are summarized in Fig. 13 and group, experiment 2 group and experiment 3 group, respectively; the symbol “-” in “PM” indicates no significant difference between “PM” and “SDS;” the rectangles with solid lines and dotted lines indicate no significant differences between “PM” and “bagging” and “PM” and “SMOTE”, respectively; and the values depicted in gray are the minimum AvgMAPEs of “bagging,” “SMOTE,” and “PM” for the ten artificial sample sizes M.

The findings from Fig. 13 and Fig. 14 are as follows:

1. The averaged errors (AvgMAPEs) of the two models of “SDS” monotonically decrease as the original training size n increases, which reveals that the training size affects the accuracy of the forecasting models when the sample sizes are very small.

![](/api/attachments/5G3NWNQF/fulltext/images/8fe9904e2da77c42b5f4e7ccb870e932bd64c395ca2bab5a9cfb4a597dac1d10.jpg)

![](/api/attachments/5G3NWNQF/fulltext/images/062a2c0fb8cd3be9a75586572891d22bfb5f6f40c8700efd60cb1737e84fadb2.jpg)

![](/api/attachments/5G3NWNQF/fulltext/images/492034e8999d30528c0b1be227ca6d60540bd3a7dda60c9a519a7d7d48ce3ae5.jpg)

![](/api/attachments/5G3NWNQF/fulltext/images/071952c49b93405253b70232428cad08e0397f411b176da1134087070f400a73.jpg)

![](/api/attachments/5G3NWNQF/fulltext/images/d1351055809800ccd9daa525979a02096f02eb01c5302fe838f1fec48ffb9473.jpg)  
Fig. 13. Experimental results for Case I

![](/api/attachments/5G3NWNQF/fulltext/images/b6581fad0f5285dced3ec6de5e3946fb932b705609ea5541d1e8cf3b04bfdcc8.jpg)

![](/api/attachments/5G3NWNQF/fulltext/images/0957ea41bfa15f5a09cbf91ac68c8da2d594d3a35fb2dab5158bb31227ccfc38.jpg)

<table><tr><td rowspan="22" colspan="2">Training size is 5 &amp; model is BPN</td><td rowspan="22" colspan="101">AvgMAPEs(%) SDS Bagging SMOTE PM</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="5" colspan="52">SDS Bagging SMOTE PM</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="53">SDS Bagging SMOTE PM</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="53">SDS Bagging SMOTE PM</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="2">1</td><td rowspan="2">2</td><td rowspan="2">3</td><td rowspan="2">4</td><td rowspan="2">5</td><td rowspan="2">6</td><td rowspan="2">7</td><td rowspan="2">8</td><td rowspan="2">9</td><td rowspan="2">10</td><td rowspan="2">10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="95">SDS Bagging SMOTE PM</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>15</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>15</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>12</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10</td><td>10 |
| Training size is 5 &amp; model is BPN | AvgMAPEs(%) SDS Bagging SMOTE PM | AvgMAPEs(%) SDS Bagging SMOTE PM | AvgMAPEs(%) SDS Bagging SMOTE PM | AvgMAPEs(%) SDS Bagging SMOTE PM | AvgMAPEs(%) SDS Bagging SMOTE PM | AvgMAPEs(%) SDS Bagging SMOTE PM | AvgMAPEs(%) SDS Bagging SMOTE PM | AvgMAPEs(%) SDS Bagging SMOTE PM | AvgMAPEs(%) SDS Barge SMOTE PM | AvgMAPEs(%) SDS Bagging SMOTE PM | AvgMAPEs(%) SDS Bagging SMOTE PM | AvgMAPEs(%) SDS Bagging SMOTE PM | AvgMAPEs(%) SDS Bagging SMOTE PM | AvgMAPEs(%) SDS Bagging SMOTE PM | AvgMAPEs(%) SDS Bagging SMOTE PM | AvgMAPEs(%) SDS Bagging SMOTE PM | AvgMAPEs (SMOTE) SMOTE PM | AvgMAPEs(SMOTE) SMOTE PM | AvgMAPEs(SMOTE) SMOTE PM | AvgMAPEs(SMOTE) SMOTE PM | AvgMAPEs(SMOTE) SMOTE PM | AvgMAPEs(SMOTE) SMOTE PM | AvgMAPEs(SMOTE) SMOTE PM | AvgMAPEs(SMOTE) SMOTE PM | AvgMAPEs(SMOTE) SMOTE PM | AvgMAPEs(SMOTE) SMTT | AvgMAPEs(SMOTE) SMOTE PM | AvgMAPEs(SMOTE) SMOTE PM | AvgMAPEs(SMOTE) SMOTE PM | AvgMAPEs(SMOTE) SMOTE PM | AvgMAPEs(SMOTE) SMOTE PM | AvgMAPEs(SMOTE) SMOTE PM | AvgMAPEs(SMOTE) SMOTE PM | AvgMAPEs(SMOTE) SMOTE PM | AvgMAEPS(SMOTE) SMOTE PM | AvgMAPEs(SMOTE) SMOTE PM | AvgMAPEs(SMOTE) SMOTE PM | AvgMAPEs(SMOTE) SMOTE PM | AvgMAPEs(SMOTE) SMOTE PM | AvgMAPEs(SMOTE) SMOTE PM | AvgMAPEs(SMOTE) SMOTE PM | AvgMAPEs(SMOTE) SMOTE PM | AvgMAPEs(SMOTE SMOTE) SMOTE PM | AvgMAPEs(SMOTE) SMOTE SMOTE PM | AvgMAPEs(SMOTE) SMOTE SMOTE PM | AvgMAPEs(SMOTE) SMOTE SMOTE PM | AvgMAPEs(SMOTE) SMOTE SMOTE PM | AvgMAPEs(SMOTE) SMOTE SMOTE PM | AvgMAPEs(SMOTE) SMOTE SMOTE PM | AvgMAPEs(SMOTE) SMOTE SMOTE PM | AvgMAPEs(SMOTE) SMOTE SMOTM | AvgMAPEs(SMOTE) SMOTE SMOTE SMOTE PM | AvgMAPEs(SMOTE) SMOTE SMOTE SMOTE PM | AvgMAPEs(SMOTE) SMOTE SMOTE SMOTE PM | AvgMAPEs(SMOTE) SMOTE SMOTE SMOTE PM | AvgMAPEs(SMOTE) SMOTE SMOTE SMOTE PM | AvgMAPEs(SMOTE) SMOTE SMOTE SMOTE PM | AvgMAPEs(SMOTE) SMOTE SMOTE SMOTE PM | AvgMAEPS(SMOTE) SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTM | AvgMAPEs(SMOTE) SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTM | AvgMSAPEs(SMOTE) SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTE SMOTM | AvgMSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSA POSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPO SS APOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSA PPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAFO PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PSPS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS Ps PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PAOSS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS PS SP S APOSS APOSS APOSS APOSS APOSS APOSS APOSS APOSS APOSS APOSS APOSS APOSS APOSS APOSS APOSS APOSS APOSS APOSS APOSS APOSS APOSS APOSS APOSS APOSS APOSS APOSS APOSS APOSS APOSS APOSS APOSS APOSS APOSS APOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSSAPPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPPPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOPPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAOPPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPLPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAROPSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSASPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSTAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSSFAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSSAPOSES APOSES APOSES APOSES APOSES APOSES APOSES APOSES APOSES APOSES APOSES APOSES APOSES APOSES APOSES APOSES APOSES APOSES APOSES APOSES APOSES APOSES APOSES APOSES APOSES APOSES APOSES APOSES APOSES APOSES APOSES APOSES APOSES APOSES AFORESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPE STRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAFESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPETRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPESTRAPEST</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Fig. 14. Experimental results for Case II

2. When n is small (such as five or ten) and the artificial sample size M is also small (ranges from 100% to 400%), the AvgMAPEs of the three VSG approaches are very unstable. For some M, the AvgMAPEs are larger than the AvgMAPEs of “SDS”; this situation is especially distinct in “bagging” and “SMOTE.” This finding implies that when n is quite small, the VSG approaches cannot improve the accuracy of the forecasting models by generating only a few samples based on the average.

3. When n is large (such as fifteen or twenty), the AvgMAPEs of the three VSG approaches are not only smaller than “SDS” but also more stable than “SDS”, even though M is small. This finding suggests that the information about the populations in the training sets is sufficient and the artificial samples can contain correct population properties when n is large.

4. As M increases, the AvgMAPEs of the three VSG methods are stable and small and most of their minimum AvgMAPEs appear to range from 400% to 800%. In some cases, their AvgMAPEs do not continue to decrease; instead, they increase in the range of 800% to 1000%. This finding implies that too many artificial samples will cause the information contained in the original samples to be dominated by the information contained in the artificial samples, which yields biased results. However, the most suitable M to obtain the best results depends on the behaviors of the data, the operation of the kernels of the learning models, the mechanisms that underlie the VSG approaches, and the size of the data.

5. Most of the AvgMAPEs in “PM” are significantly smaller than the AvgMAPEs in “SDS”, “bagging,” and “SMOTE” with statistical support. This finding indicates that the proposed method outperforms bagging and the SMOTE in the two cases.

6. The difference between “bagging” and “SMOTE” is difficult to discern in the two cases. Their p-values exceed 0.05, and in some cases in Fig. 13 and Fig. 14, the AvgMAPEs are very similar. By taking their minimum AvgMAPEs and averages of AvgMAPEs as indicators, the SMOTE achieves better results than bagging when the model is SVR, whereas the reverse is true when the model is BPN.

## 5. Conclusions

While issues surrounding big data learning have attracted a substantial amount of data analyzers have to learn with small amounts of data, such as the two cases described in this paper. Numerous virtual sample generation approaches, which are data preprocessing methods in KDD, have been developed to extract knowledge from these data. Although BP is extensively applied to create new training sets, the data structures of the resulting sets encounter the issue of incompleteness when handling with small data. Although the SMOTE does not consider the entire distribution when generating samples, it does fill the information gaps with synthetic samples. This research proposed a systematic procedure that contains bound estimating functions and a sample generating approach to enhance the structures of small data to ensure that algorithms have sufficient training to improve the robustness and/ or accuracy of the patterns that they identify.

This study examined two real cases from a leading manufacturer in the TFT-LCD industry in Taiwan, performed experiments using two algorithms—BPN and SVR—and implemented two VSG approaches—bagging (using BP) and the SMOTE—to compare the accuracies of the approaches. The results of the two cases indicated that the forecasting errors of the proposed method are smaller than the forecasting errors of bagging and the SMOTE with the majority of statistical support. The proposed method has considerable practical value for engineers in the two cases because it can help them build more robust and precise models when they try to infer the possible manufacturing results in TFT-LCD processes. Future studies should consider applying manufacturing fields to validate the effectiveness of the approach.

## References

[1] H.J. Gómez-Vallejo, B. Uriel-Latorre, M. Sande-Meijide, B. Villamarín-Bello, R. Pavón, F. Fdez-Riverola, D. Glez-Peña, A case-based reasoning system for aiding detection and classification of nosocomial infections, Decision Support Systems, 84 (2016) 104-116.

[2] W.S. Gosset, The probable error of a mean, Biometrika, 6 (1908) 1-25.

[3] G.Y. Chao, T.I. Tsai, T.J. Lu, H.C. Hsu, B.Y. Bao, W.Y. Wu, M.T. Lin, T.L. Lu, A new approach to prediction of radiotherapy of bladder cancer cells in small dataset analysis,

Expert Systems with Applications, 38 (2011) 7963-7969.

[4] C.J. Huang, H.F. Wang, H.J. Chiu, T.H. Lan, T.M. Hu, E.W. Loh, Prediction of the period of psychotic episode in individual schizophrenics by simulation-data construction approach, Journal of medical systems, 34 (2010) 799-808.

[5] Z. Huang, J. Li, H. Su, G.S. Watts, H. Chen, Large-scale regulatory network analysis from microarray data: modified Bayesian network learning and association rule mining, Decision Support Systems, 43 (2007) 1207-1225.

[6] P. Niyogi, F. Girosi, T. Poggio, Incorporating prior information in machine learning by creating virtual examples, Proceedings of the IEEE, 86 (1998) 2196-2209.

[7] G. Guo, C.R. Dyer, Learning from examples in the small sample case: face expression 35 (2005) 477-488.

[8] D.C. Li, W.T. Huang, C.C. Chen, C.J. Chang, Employing virtual samples to build early high-dimensional manufacturing models, International Journal of Production Research, 51 (2013) 3206-3224.

[9] D.C. Li, L.S. Lin, Generating information for small data sets with a multi-modal distribution, Decision Support Systems, 66 (2014) 71-81.

[10] J.R. Quinlan, Learning with continuous classes, 5th Australian joint conference on artificial intelligence, Singapore, 1992, pp. 343-348.

[11] U. Fayyad, G. Piatetsky-Shapiro, P. Smyth, From data mining to knowledge discovery in databases, AI magazine, 17 (1996) 37.

[12] A. Dag, A. Oztekin, A. Yucel, S. Bulur, F.M. Megahed, Predicting heart transplantation outcomes through data analytics, Decision Support Systems, 94 (2017) 42-52.

[13] B. Efron, R.J. Tibshirani, An Introduction to the Bootstrap, New York: Chapmen & Hall1993.

[14] L. Breiman, Bagging Predictors, Machine Learning, 24 (1996) 123-140.

[15] L. Breiman, Random forests, Machine Learning, 45 (2001) 5-32.

[16] N.V. Chawla, K.W. Bowyer, L.O. Hall, W.P. Kegelmeyer, SMOTE: synthetic minority over-sampling technique, Journal of artificial intelligence research, 16 (2002) 321-357.

[17] L.A. Zadeh, Fuzzy sets, Information and Control, 8 (1965) 338-353.

[18] C.F. Huang, Principle of information, Fuzzy Sets and Systems, 91 (1997) 69-90.

[19] C.F. Huang, C. Moraga, A diffusion-neural-network for learning from small samples, Int. J. Approx. Reasoning, 35 (2004) 137-161.

[20] O.A.M. Ali, A.Y.A. Ali, B.S. Sumait, Comparison between the Effects of Different Types of Membership Functions on Fuzzy Logic Controller Performance, International Journal of Emerging Engineering Research and Technology, 3 (2015) 76-83.

[21] Z. Jin, B.K. Bose, Evaluation of membership functions for fuzzy logic controlled induction motor drive, IEEE 2002 28th Annual Conference of the Industrial Electronics

Society. IECON 02, 2002, pp. 229-234.

[22] D.C. Li, W.K. Lin, L.S. Lin, C.C. Chen, W.T. Huang, The attribute-trend-similarity method to improve learning performance for small datasets, International Journal of Production Research, 55 (2017) 1898-1913.

[23] J. Holland, Adaptation in Natural and Artificial Systems, The University of Michigan Press1975.

[24] J.W. Forrester, Industrial Dynamics, MIT Press: Cambridge, Massachusetts1961.

## Biographical Note

![](/api/attachments/5G3NWNQF/fulltext/images/9f6c567620240a1a1d87edb6dd0659dacd5ca730776ece3292ce541c2b9ef83d.jpg)

Der-Chiang Li is a Distinguished Professor at the Department of Industrial and Information Management, the National Cheng Kung University, Taiwan. He received his PhD degree at the Department of Industrial Engineering at Lamar University Beaumont, Texas, USA, in 1985. As a research professor, his current interest concentrates on

machine learning with small data sets. His articles have appeared in Decision Support Systems, Omega, Information Sciences, European Journal of Operational Research, Computers & Operations Research, International Journal of Production Research, and other publications.

![](/api/attachments/5G3NWNQF/fulltext/images/b01781c1b89509013c888ba731edfb5b28ae575b08380501212ade0677a9cd42.jpg)

Wu-Kuo Lin is a Ph.D. candidate at the Department of Industrial and Information Management, the National Cheng Kung University, Taiwan. His current research interests are in the area of forecasting and data mining with small data sets. His articles have appeared in

![](/api/attachments/5G3NWNQF/fulltext/images/961bd6189001287581b88de38c5ad787f6a2d3761be2e159083599356ebbe88a.jpg)

Chien-Chih Chen is a postdoctoral fellow at the Department of Industrial and Information Management, the National Cheng Kung University, Taiwan. His article has appeared in Omega, Expert Systems with Applications, International Journal of Production Research, Neurocomputing, Computers & Industrial Engineering, igent Manufacturing, and other publications.

![](/api/attachments/5G3NWNQF/fulltext/images/b740d6c0b56a2f2e19a1e2f4cc6fa63e3c9c6ba01b713fbd8ab71177ca0f5fab.jpg)

Hung-Yu Chen is a Ph.D. candidate at the Institute of Information Management, the National Cheng Kung University, Taiwan. His current research interests focus on the learning issue of small datasets.

![](/api/attachments/5G3NWNQF/fulltext/images/207d6627297d7072f40866ebb201fb9b785574f6ad25d97926c49a75db02d7e7.jpg)

Liang-Sian Lin is a PH.D researcher at the Department of Industrial and Information Management, the National Cheng Kung University, Taiwan. He is also working at the laboratory for small sample learning. As a research professor, his current interests concentrate on small data sets. His article has appeared in European Journal of

Operational Research, Decision Support Systems, and International Journal of Production Research.

## Highlights

 Most algorithms often output unsatisfying predictions when working with small data.

 A data-driven method is proposed for enhancing the data structures of small data.

 A set of new functions are derived to estimate the domains of small data.

 The method successfully improves the predictions of algorithms in two real cases.
