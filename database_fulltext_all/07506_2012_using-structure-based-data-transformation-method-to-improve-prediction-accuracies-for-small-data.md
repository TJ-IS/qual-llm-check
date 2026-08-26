---
otero_id: 7506
otero_key: "Y45UQMC7"
title: "Using structure-based data transformation method to improve prediction accuracies for small data sets"
authors: "Der-Chiang Li; Chih-Chieh Chang; Chiao-Wen Liu"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.11.021"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Using structure-based data transformation method to improve prediction accuracies for small data sets

Der-Chiang Li ⁎, Chih-Chieh Chang, Chiao-Wen Liu

Department of Industrial and Information Management, National Cheng Kung University, Taiwan

## a r t i c l e i n f o

Article history: Received 12 November 2010 Received in revised form 7 October 2011 Accepted 18 November 2011 Available online 1 December 2011

Keywords: Manufacturing Small data set Cluster DBSCAN SVR

## a b s t r a c t

Small data set problems have been widely considered in many <sup>fi</sup>elds, where increasing the prediction ability is the most important goal. This study considers the data structure to identify new data points in a more precise manner, and is thus able to achieve improved prediction capability. The proposed method, named structure-based data transformation, consists of two steps. The <sup>fi</sup>rst step is using the density-based spatial clustering of applications with noise (DBSCAN) algorithm to separate data sets into clusters, which generates the number of clusters dynamically. The second step is to build up the data transformation function, in which the new attributes are computed using fuzzy membership functions obtained by the corresponding membership grades in each cluster. Three real cases are selected to compare the proposed forecasting model with the linear regression (LR), backpropagation neural network (BPNN), and support vector machine for regression (SVR) methods. The result show that the structure-based data transformation method has better performance than when using the raw data with regard to the error improving rate, mean square error (MSE), and standard deviation (STD).

© 2011 Elsevier B.V. All rights reserved.

## 1. Introduction

Small data set problems have been widely considered in many <sup>fi</sup>elds, such as manufacturing systems for high cost products or special medical cases. Taking polarizers as an example, they are one of the key parts in Thin Film Transistor-Liquid Crystal Displays (TFT-LCD), and the production cost is very expensive. Thus, how to use the small data sets obtained in the pilot runs to build a management model to reduce overall manufacturing costs is a very important task. Similarly, spinocerebellar ataxia is a rare hereditary disease, with only few records from all over the world, and thus is also de<sup>fi</sup>ned as a small data set problem. Theoretically, it is hard to make precise predictions using a small data set, and so the main goal of this study is how to decrease the error rate between predicted and real data.

Several approaches have been proposed to deal with small data set problems, one of which is virtual sample generation. The original idea was proposed by Niyogi et al. [27], who used prior knowledge obtained from a given small training set to create virtual samples to improve recognition performance. This work generated new views of a given 3-D object from any other direction through a mathematical transformation, with the samples thus generated called virtual ones. Later, Li et al. [16] used a functional virtual population to solve the scheduling problem in early <sup>fl</sup>exible manufacturing systems, where they utilized a virtual sample generation technique to increase the amount of training data to improve the classi<sup>fi</sup>cation accuracy of a BPNN. Huang and Moraga [11] proposed a diffusion neural network (DNN) which, compared with other such networks, had more nodes in the inputs and layers, and was trained by derived patterns instead of the original ones. The DNN method's error rate, 48%, was found to be better than that of the conventional BPNN. Recently, Yang et al. [35] presented a Gaussian distribution virtual sample generation method, which showed good performance in both in small sample problems and imbalanced sample problems. Khan et al. [26] presented a novel model to deal with the face recognition classi<sup>fi</sup>cation problem, which was also small data set problem.

Using kernel methods, such as a support vector machine, is another effective approach to solve small data problems. A kernel κ : X X→R is de<sup>fi</sup>ned as the Mercer kernel viewed as a measure of <sup></sup>the similarity between two paired data, where X is the input data set and R is a real number [5]. A typical kernel representation uses a feature map ϕ:Ω→F to transform data from the input space Ω into a feature space F, and then constructs linear algorithms in the feature space to solve nonlinear problems in the input space, as shown in Fig. 1. It is usually supposed that the transformed data in the feature space has a better linear estimation than that of the original data in the input space. The map ϕ is usually represented implicitly by a kernel function, such as the inner product denoted asκ x; x<sup>′</sup>   ϕ x ; ϕ x<sup>′</sup>   [4]. <sup>¼ ð Þ</sup>Hence, the main purpose of a kernel method is extending the data set into a higher dimensional space by using a functional kernel.

Although using a kernel function to extend data into a higher dimension feature space is effective for data analysis, it is dif<sup>fi</sup>cult to <sup>fi</sup>nd the best kernel function for a problem. Therefore, this research follows the concept of extending the original data set into a higher dimensional feature space and develops a data transformation procedure as the kernel function. In fact, the proposed method, named structure-based data transformation, uses the data clustering technique to place similar data into groups based on data density to further obtain the geographic structure of the data set, where DBSCAN is employed as the data clustering tool to generate clusters dynamically and also to detect any noise. Based on these clusters, the second step of the proposed approach is to build up the attribute creation procedure to generate new attributes using the fuzzy membership function. Through the fuzzy membership function, one attribute could generate several cluster-possibility attributes using the clusters constructed in the <sup>fi</sup>rst step. Finally, after mapping the data into a higher dimensional space, the data with the newly generated attributes and values will be input into the classi<sup>fi</sup>er as the training data set.

![](/api/attachments/Y45UQMC7/fulltext/images/85b40ac5877965862a431c899912d0d321c92fdb5c6a84bee85a18b8c57cb52b.jpg)  
Fig. 1. The mapping ϕ from Ω to F.

In the proposed method, the main difference from the kernel method is that we consider the data structure using DBSCAN clustering, and based on this the new attributes are constructed to increase the attribute information. It is thus a data structure oriented approach to extend the data dimensions. Also, different from the virtual sample generation methods, the proposed method generates more effective data attribute (for prediction accuracy) into the small data set. Although virtual sample generation can increase the data quantity, there is still a risk of data bias when oversupplying virtual samples. The proposed method can arti<sup>fi</sup>cially increase the prediction accuracy by creating attributes.

Three real case studies are examined in this study to evaluate the proposed approach. The <sup>fi</sup>rst case uses multi-layer ceramic capacitors (MLCC), which are a product made of ceramic powder. The second case is a concrete slump test, which is commonly used in the literature and drawn from the UCI database. The last case study is used to predict the quality of TFT-LCD. The error improving rate, MSE, STD, and t-test statistic are used to verify the effectiveness of the forecasting model, with the results compared to the LR, BPNN, and SVR methods. The results show that the proposed method is superior to other approaches with regard to its prediction capability.

The rest of this paper is organized as follows: Section 2 describes the modeling concept of the data transformation method. The structure-based transformation function is shown in Section 3. In Section 4, three real cases are demonstrated to explain the proposed method. Finally, the conclusions and suggestions for future studies are presented in Section 5.

## 2. Related studies

## 2.1. The data transformation methods

Mapping the original data set by a nonlinear function to deal with nonlinear prediction problems is widely used in the past research, as it is a useful preprocessing technique to map data to a higher dimensional space [23]. For example, the residuals are structureless design of experiment if the analysis model is correct and the assumptions are satis<sup>fi</sup>ed [25]. However, the residuals in some of the cases are not structureless, and an outward-opening funnel or megaphone will occur when these get larger as the number of observations increases. To deal with this problem, the population of observations is generally transformed, using method such as Box–Cox transformation, logarithmic transformation, and arcsin transformation.

Arti<sup>fi</sup>cial neural networks (ANN) are allowed to transform data to solve nonlinear problems. They use activation functions to transform linear combinations of the weights and input data sets [32]. A representative model is multilayer perceptrons, which uses multiple layers with several activation functions to transform the data into a feature space that can produce a forecast model with less prediction error. Fig. 2 shows a simple arti<sup>fi</sup>cial neuron model, where ${ \bf x } = ( x _ { 1 } , x _ { 2 } , \cdots$ $x _ { M } )$ is the input, y is the output, b is the bias, f(⋅) is an activation function, and $\mathbf { w } = ( w _ { 1 } , w _ { 2 } , \cdots , w _ { M } )$ is the weights. The mathematical representation of the neuron is $\scriptstyle y = f ( \sum _ { i = 1 } ^ { M } w _ { i } x _ { i } + b )$ ). It is easy to see that when the activation function $f ( \cdot )$ is nonlinear, the input data will be transformed to another feature space.

Another transformation is the kernel method, and support vector machines (SVM) are commonly used to achieve this. In an SVM, in order to deal with a nonlinear problem, the kernel usually transforms the data set into a higher dimension feature space, and this is then used to <sup>fi</sup>nd an appropriate hyperplane for the problem [32]. For instance, given two samples ${ \bf x } = ( x _ { 1 } , x _ { 2 } )$ and ${ \pmb z } = ( z _ { 1 } , z _ { 2 } )$ , which are the two-dimensional input space data, when a polynomial kernel is used to expand the data the transformed feature space is obtained as a three-dimensional space, as shown below:

$$
\begin{array}{c} \kappa (\mathbf {x}, \mathbf {z}) = \left(\mathbf {x} ^ {T} \mathbf {z}\right) ^ {2} = (x _ {1} z _ {1} + x _ {2} z _ {2}) ^ {2} = x _ {1} ^ {2} z _ {1} ^ {2} + 2 x _ {1} z _ {1} x _ {2} z _ {2} + x _ {2} ^ {2} z _ {2} ^ {2} \\ = x _ {1} ^ {2} z _ {1} ^ {2} + 2 x _ {1} z _ {1} x _ {2} z _ {2} + x _ {2} ^ {2} z _ {2} ^ {2} = \left(x _ {1} ^ {2}, \sqrt {2} x _ {1} x _ {2}, x _ {2} ^ {2}\right) \left(z _ {1} ^ {2}, \sqrt {2} z _ {1} z _ {2}, z _ {2} ^ {2}\right) ^ {T}. \end{array}\tag{1}
$$

## 2.2. Support vector machines for regression

SVM have been widely used in many <sup>fi</sup>elds, such as to <sup>fi</sup>nd tighter error bounds on performance of classi<sup>fi</sup>cation [9], and to predict human wine taste preferences [7]. Unlike traditional methods, SVM minimize the upper bound of the generalization error by maximizing the margin between the separating hyperplane and the data [2]. In its original form, SVM learning leads to a quadratic programming problem with a convex constrained optimization property, and thus there is a unique solution to it. Given a training set of N samples, $( { \bf x } _ { 1 } , t _ { 1 } ) , ( { \bf x } _ { 2 } , t _ { 2 } )$ $\cdots , ( \mathbf { x } _ { N } , t _ { N } )$ , where $\mathbf { x } _ { i } { \in } \mathbb { R } ^ { p }$ is the input vector corresponding to the ith sample labeled by $t _ { i } \in \{ - 1 , + 1 \}$ } depending on its class. The SVM problem can be formulated as a quadratic programming optimization problem that will <sup>fi</sup>nd the weight parameter w and the bias parameter b that maximize the margin while ensuring that the training samples are

![](/api/attachments/Y45UQMC7/fulltext/images/d2991567eaddffee752af6f3362944ed224e72c8afb435145af61710590b1fb7.jpg)  
Fig. 2. The arti<sup>fi</sup>cial neuron model [14].

![](/api/attachments/Y45UQMC7/fulltext/images/2f0f6554e1a940c212d78a0275db9e97cba1d74f016c477e03ac21e5d8a97665.jpg)  
Fig. 3. Comparison of the ε-insensitive error function (dotted line) and quadratic error function (solid line).

well classi<sup>fi</sup>ed:

$$
\begin{array}{l l} \min & \frac {1}{2} \| \mathbf {w} \| ^ {2} + C \sum_ {i = 1} ^ {N} \xi_ {i} \\ s. t & t _ {i} \Big (\mathbf {w} ^ {T} \cdot \varphi (\mathbf {x} _ {i}) + b \Big) \geq 1 - \xi_ {i} \\ & \xi_ {i} \geq 0 \quad i = 1, \dots , N \end{array}\tag{2}
$$

where parameter C is used to tune the trade-off between the acceptable amount of errors. $\xi _ { i } = | \ t _ { i } - y ( \mathbf x _ { i } ) | , i = 1 , \cdots , n$ are slack variables and $y ( \mathbf { x } _ { i } ) = \mathbf { w } ^ { T } \cdot \varphi ( \mathbf { x } _ { i } ) + b$

Vapnik [34] extended SVM for regression models, called SVR, for treating a regression problem as a single classi<sup>fi</sup>cation case. Given a training set of N samples: $( { \bf x } _ { 1 } , t _ { 1 } ) , ( { \bf x } _ { 2 } , t _ { 2 } ) , \cdots , ( { \bf x } _ { N } , t _ { N } )$ , where $\mathbf { x } _ { i } \in \mathbb { R } ^ { p }$ is the input vector and the corresponding value $t _ { i } { \in } \mathbb { R }$ is the target value of $\mathbf { x } _ { i } ,$ and an ε-insensitive error function (the dotted line in $\mathrm { F i g } . 3 )$ is proposed as a trade-off with the acceptable amount of errors.

$$
E _ {\varepsilon} (y (\mathbf {x}) - t) = \left\{ \begin{array}{c l} | y (\mathbf {x}) - t | - \varepsilon , & \text { otherwise } \\ 0, & \text { if } | y (\mathbf {x}) - t | <   \varepsilon \end{array} \right.\tag{3}
$$

When minimizing the objective function, also called the error function,

$$
C \sum_ {i = 1} ^ {N} E _ {\varepsilon} (y (\mathbf {x} _ {i}) - t _ {i}) + \frac {1}{2} \| \mathbf {w} \| ^ {2}.\tag{4}
$$

One can re-express the optimization problem by introducing slack variables to the model. For each data point x , we use two slack variables, $\xi _ { i } \ge 0$ and $\hat { \xi } _ { i } { \geq } 0$ , to outline the points that are out of the interval, $[ y - \varepsilon , y + \varepsilon ] ,$ , where $\xi _ { i } > 0$ corresponds to a point for which $t _ { i } > y ( \mathbf { x } _ { i } ) + \varepsilon ,$ and $\hat { \xi } _ { i } > 0$ corresponds to a point for which $t _ { i } { < } y ( \mathbf { x } _ { i } ) + \varepsilon ,$ as illustrated in Fig. 4.

<sup>ð Þ þ</sup>The condition for a target point to lie inside the ε-tube is that $y ( \mathbf { x } _ { i } ) - \varepsilon \leq t _ { i } \leq y ( \mathbf { x } _ { i } ) + \varepsilon ,$ and the purpose of introducing the slack vari-<sup>ð Þ ð Þ þ</sup>ables is to allow points to lie outside the tube provided that the slack variables are nonzero, and the corresponding conditions are:

![](/api/attachments/Y45UQMC7/fulltext/images/ed0679923c583fa2fa8675a983473e640b015c242294fdb1b8efff601af6830d.jpg)  
Fig. 4. Illustration of SVM for regression.

$$
\begin{array}{l} t _ {i} \leq y (\mathbf {x} _ {i}) + \varepsilon + \xi_ {i} \\ t _ {i} \leq y (\mathbf {x} _ {i}) - \varepsilon - \xi_ {i}, i = 1, \dots , N. \end{array}\tag{5}
$$

Hence, the error function for support vector regression can then be written as:

$$
C \sum_ {i = 1} ^ {N} \left(\xi_ {i} + \hat {\xi} _ {i}\right) + \frac {1}{2} \| \mathbf {w} \| ^ {2}.\tag{6}
$$

Using the Lagrange multipliers $\alpha _ { i } { \geq } 0 , i { = } 1 , \cdots , N$ to solve the quadratic programming problem, one can write the dual problem as:

$$
\begin{array}{l l} \max & - \frac {1}{2} \sum_ {i = 1} ^ {N} \sum_ {j = 1} ^ {N} (\alpha_ {i} - \hat {\alpha} _ {i}) \Big (\alpha_ {j} - \hat {\alpha} _ {j} \Big) k \Big (\mathbf {x} _ {i}, \mathbf {x} _ {j} \Big) \\ & - \varepsilon \sum_ {i = 1} ^ {N} (\alpha_ {i} - \hat {\alpha} _ {i}) + \sum_ {j = 1} ^ {N} \Big (\alpha_ {j} - \hat {\alpha} _ {j} \Big) t _ {j} \\ s. t & 0 \leq \alpha_ {i} \leq C, \\ & 0 \leq \hat {\alpha} _ {i} \leq C, i = 1,..., N \end{array}\tag{7}
$$

where $k ( \cdot , \cdot )$ is called a positive semide<sup>fi</sup>nite kernel (or Mercer kernel) which satis<sup>fi</sup>es the symmetric $( \mathrm { i . e . } k \Big ( \mathbf { x } _ { i } , \mathbf { x } _ { j } \Big ) = k \Big ( \mathbf { x } _ { j } , \mathbf { x } _ { i } \Big ) ;$ ) and the following equation:

$$
\sum_ {i = 1} ^ {s} \sum_ {j = 1} ^ {s} b _ {i} b _ {j} k (\mathbf {x} _ {i}, \mathbf {x} _ {j}) \geq 0 \forall s \geq 2, \text { where } b _ {q} \in \mathbb {R} \forall q = 1,..., s.\tag{8}
$$

Each Mercer kernel can be expressed as $k ( { \bf x } , { \bf x ^ { \prime } } ) = \phi ( { \bf x } ) , \phi ( { \bf x ^ { \prime } } )$ where $\phi { : } X {  } F$ is a mapping of feature selection, and $\langle \cdot , \cdot \rangle$ is the inner product. Some of the commonly used functions are polynomial, radial-basis function, and two-layer perceptron kernels [37]:

$$
\begin{array}{l} K (\mathbf {x}, \mathbf {y}) = \left(\mathbf {x} ^ {t} \mathbf {y} + 1\right) ^ {d} \\ K (\mathbf {x}, \mathbf {y}) = \exp \left(- \frac {\| \mathbf {x} - \mathbf {y} \| ^ {2}}{2 \sigma^ {2}}\right) \\ K (\mathbf {x}, \mathbf {y}) = \tanh \left(\beta_ {0} \mathbf {x} ^ {t} \mathbf {y} + \beta_ {1}\right) \end{array}\tag{9}
$$

where $d , \sigma , \beta _ { 0 } , \mathrm { a n d } \beta _ { 1 }$ are speci<sup>fi</sup>ed a priori by the user.

There are several studies that discuss the performance of SVR [1,12,22,31], and Ali and Smith-Miles [1] indicated that radial-basis function kernels have superior performance, and thus we use one of these as the analysis tool in this paper.

## 3. Structure-based data transformation

This section presents a detailed procedure to explain the proposed method. The structure-based transformation starts from clustering the data and then building mega-trend diffusion (MTD) functions for clusters in order to lay the basis for further analysis.

## 3.1. DBSCAN and the MTD function

Cluster analysis is a method for clustering objects according to their measured or perceived intrinsic characteristics or similarity [13]. It is basically a statistical classi<sup>fi</sup>cation technique for discovering whether the individuals in a population fall into different groups by making quantitative comparisons of multiple characteristics [24].

Data clustering has been used for many purposes. One is to explore the underlying data structure to gain insight, generate hypotheses, detect anomalies, and identify salient features. One approach is to explore the natural classi<sup>fi</sup>cation or to identify the degree of similarity among forms or organisms. In addition, there is also data compression, which is a method for organizing the data and summarizing it through cluster prototypes. This research applies the DBSCAN clustering algorithm to classify the target values with M attributes into K-clusters dynamically, and then transform them into a new data set with M (K+1) attributes.

## 3.1.1. DBSCAN

DBSCAN, a density-based clustering algorithm proposed by Ester et al. [10], is suitable for high dimensional data sets and also for applications such as examining the hyperlink structure of web [6]. DBSCAN assembles high density data into clusters based on two main variables, epsilon (ε) and Minpts, where ε represents the radius of the core object, and Minpts stands for the minimum data points (sets) of each cluster that should be selected. The DBSCAN algorithm is as follows: First, it searches for clusters through checking the surroundings of each data point within a scope called the ε-neighborhood. If the ε-neighborhood of a data point contains other data which has a data size that is more than a certain pre-de<sup>fi</sup>ned number (Minpts), a cluster with this data (called the core object) is created; otherwise, the data is treated as noise which will be eventually deleted. DBSCAN iteratively collects directly density-reachable data (data within the ε- neighborhood of a core object) until no new data can be added to any cluster, and this may involve merging some items [19]. In this study, we apply the DBSCAN algorithm to cluster overall data sets to detect the data structures and noise.

The two main parameters, ε and Minpts, might be overestimated or underestimated, resulting in the misclassi<sup>fi</sup>cation of points or the misidenti<sup>fi</sup>cation of clusters [29]. Daszykowski et al. [8] thus suggested that Minpts can be calculated as m/25, where m is the number of samples. However, since this study is dealing with small data set problems there is not be enough samples to use this equation. Therefore, we used the settings in Li and Fang [15], where it suggested that Minpts is 2. With regard to the parameter ε, the literature survey in Pei et al. [29] showed that the estimation of it is still a subjective process [20,21,28,30]. Furthermore, Ankerst et al. [3] proposed a method, ordering points to identify the clustering structure (OPTICS), which extends DBSCAN to help it compute ε. There are two variables shown in OPTICS, core-distance and reachability-distance. The coredistance is the smallest distance from p, a core object, to an object in its ε-neighborhood, while the reachability-distance stands for the smallest density-reachable distance between a data set and a core object p. Daszykowski et al. [8] proposed a method to determine the ε value, but it is not suitable for generating clusters from small data sets. Therefore, this study used the median value of OPTICS coredistance as the ε value.

## 3.1.2. MTD function

The MTD function was proposed by Li et al. [17] to deal with the small data set problem for scheduling strategies in early <sup>fl</sup>exible manufacturing systems (FMS) by generating virtual samples. For most analytical cases, from the statistical viewpoint, the assumption of normal distribution is often a necessary condition before data processing. However, it is dif<sup>fi</sup>cult to show that a data set follows a normal distribution when the data size is small. Consequently, Li et al. [17] used the membership function in fuzzy set theory to calculate the possibility values of samples instead of the probability in statistics to avoid the normal distribution assumption. Fig. 5 shows the concept of the fuzzy theorem applied to the MTD function, where the triangle shape is the membership function, and the heights of samples m and n are the possibility values of the membership function, denoted as $M ( m )$ and $M ( n )$

This paper employs the MTD function to present the probability of a sample belonging to a cluster. The detailed steps to build an MTD function are presented below, and the next section will show how this study applies it to the building of fuzzy-based transformation functions. Given the sample of $X = \{ x _ { 1 } , x _ { 2 } , \cdots x _ { n } \}$ , the boundaries a and

![](/api/attachments/Y45UQMC7/fulltext/images/72a5e6fe76d69aeede11940d2c715f42752ea29316de869d7dc05329ab361e49.jpg)  
Fig. 5. MTD function.

b are de<sup>fi</sup>ned as follows:

$$
a = u _ {s e t} - s k e w _ {L} \times \sqrt {(- 2) \times \hat {s} _ {x} ^ {2} / N _ {L} \times \ln (f (t))}\tag{10}
$$

$$
b = u _ {s e t} + s k e w _ {L} \times \sqrt {(- 2) \times \hat {s} _ {x} ^ {2} / N _ {U} \times \ln (f (t))}\tag{11}
$$

where $u _ { s e t } = ( \mathrm { m i n } + \mathrm { m a x } ) / 2$ and $\hat { s } _ { x } ^ { 2 }$ is the variance of X. $N _ { L }$ is the number of data points, smaller than $u _ { s e t } . N _ { U }$ is the number of data points greater than $u _ { s e t } .$ $s k e w _ { L } { = } N _ { L } / ( N _ { L } { + } N _ { U } )$ and $s k e w _ { U } { = } N _ { U } / ( N _ { L } + N _ { U } )$ show the rates of skewness in the distribution of the data, and $f ( t )$ is a real number. In Fig. 5, the value of the membership function presents the possibility value of $\mid x ,$ as denoted by $M ( x )$ ). The MTD function is thus formulated as:

$$
M (x) = \left\{ \begin{array}{l l} (x - a) / (u _ {s e t} - a) & a \leq x \leq u _ {s e t} \\ (b - x) / (b - u _ {s e t}) & u _ {s e t} \leq x \leq b \\ 0 & o t h e r w i s e. \end{array} \right.\tag{12}
$$

## 3.2. Structure-based transformation

Based on the MTD distribution, considering the forecast problem with DBSCAN, the transformed x produced by the structure-based transformation is formulated as:

$$
\psi (x) ^ {\prime} = \left(x, M ^ {1} (x), M ^ {2} (x),..., M ^ {k} (x)\right), x \in \mathbb {R}\tag{13}
$$

where $M ^ { i } ( x )$ become the new attributes, and these are de<sup>fi</sup>ned using the MTD distribution $i = 1 , \cdots , k .$ It is easy to <sup>fi</sup>nd the function ψ(x) for an extended point x from one dimension to k+1 dimensions.

As an example, Fig. 6 shows a two-cluster problem with a single attribute, where the triangle on the left side with a solid line represents the transformation function for cluster 1 denoted as $M ^ { 1 } ( x )$ and the triangle with a dotted line represents the transformation function for cluster 2, denoted as $M ^ { 2 } ( { \bar { x } } )$ . Thus, for the two-cluster one-attribute classi<sup>fi</sup>cation problem, the transformed data is $\psi ( x ) =$ $( x , \ M ^ { 1 } ( x ) , \ M ^ { 2 } ( x ) )$ ).

## 3.2.1. Steps

The complete procedure of structure-based transformation is described as follows: Assuming that we have a sample set $X = \{ ( \mathbf { x } _ { 1 } . . . , t _ { 1 } ) , ( \mathbf { x } _ { 2 } . . . , t _ { 2 } ) , ^ { . . . } , ( \mathbf { x } _ { N } . . . . , t _ { N } ) \}$ , where for each sample $\mathbf { x } _ { i } ,$ $i { = } 1 , \cdots , N ,$ in X has M attributes (means $\mathbf { x } _ { i } = ( x _ { 1 } , \cdots , \ x _ { M } ) )$ , and t is the target value of x<sub>i</sub>.

![](/api/attachments/Y45UQMC7/fulltext/images/5bca7f7da04f0a91738ff6c19aa2bed79596ac945356aaa9341e8ff9e704f651.jpg)  
Fig. 6. The fuzzy-based transformation function for a two-class problem.

Step 1: Determine the radius ε and the Minpts. The set ε is based on the OPTICS here, and it is the median of the core-distance of the data set, with Minpts=2 used in this study. After the two variables have been set, the data set is clustered into K clusters through the DBSCAN algorithm, where K is a dynamic value.

Step 2: Assume S is the number of the sample size. Starting with cluster 1, the value of attribute $1 , x _ { 1 } ,$ of the samples in $\tilde { X } ^ { 1 }$ is denoted as $\mathbf { x } _ { i 1 } ^ { 1 } , i = 1 , 2 , \cdots , S .$ The value is used to derive the transformation function for attribute 1, $M ^ { 1 } ( x _ { 1 } )$ , and then this computation is repeated for every attribute to obtain $M ^ { 1 } ( x _ { j } ) , j = 1 , \cdots , M ,$ as shown in Fig. 7. Iterate this step K times for each class to build up $K \times M$ transformation functions, $M ^ { k } ( x _ { j } ) , j = 1 , \cdots , M k = 1 , \cdots , K .$

Step 3: Starting with attribute $1 , x _ { 1 } ,$ , for all samples in X. The transformation function of $x _ { 1 }$ is set as $( x _ { 1 } , M ^ { 1 } ( x _ { 1 } ) , M ^ { 2 } ( x _ { 1 } ) , \cdots , M ^ { K } ( x _ { 1 } ) )$ Repeat this step M times to get $( x _ { j } , M ^ { 1 } ( x _ { j } ) , M ^ { 2 } ( x _ { j } ) , \cdots , M ^ { K } ( x _ { j } ) )$ , where j=1,2,⋯,M.

Step 4: For every sample x ∈X with M attributes, use the transformation function to extend the attribute from M attributes into $M \times \left( K + 1 \right)$ dimensions.

## 3.2.2. An example

The following example illustrates the computation for the fuzzybased transformation. Table 1 shows the detailed training data information. The computation steps are as follows:

Step 1: Assume that ε is 0.69 (computed through OPTICS) and Minpts is 2 in this example, then the training data generates one cluster, which involves $\mathrm { X } _ { 2 } , \mathrm { X } _ { 4 } ,$ and $\mathrm { X } _ { 5 } ,$ , while $\Chi _ { 1 }$ and ${ \mathrm { X } } _ { 3 }$ are regarded as noise, as shown in Table 2.

Step 2: Apply the MTD technique to compute the membership grade of each attribute in the cluster. Use the fuzzy-based transformation functions to extend X into a higher dimension, and the transformation values of X are shown in Table 3.

## 4. Experiment

In this section, we use three real cases to verify the performance of the proposed method. The <sup>fi</sup>rst case uses MLCC, which are passive components in modern electronics with high cost pilot runs [33].

Detailed information of data set X.

<table><tr><td>Data</td><td>Attribute 1</td><td>Attribute 2</td><td>Y</td></tr><tr><td> $X_1$ </td><td>1.00</td><td>1.12</td><td>10.2</td></tr><tr><td> $X_2$ </td><td>0.09</td><td>-0.68</td><td>9.64</td></tr><tr><td> $X_3$ </td><td>1.41</td><td>-0.03</td><td>9.87</td></tr><tr><td> $X_4$ </td><td>0.80</td><td>-1.75</td><td>9.50</td></tr><tr><td> $X_5$ </td><td>0.49</td><td>-0.11</td><td>9.93</td></tr></table>

The second case is the concrete slump test, which is downloaded from the UCI repository, available at http://www.ics.uci.edu. The last case uses the production process of TFT-LCD, in which we predict cell verniers to control the relevant variables to retain high product quality [18]. The LR, SVR, and BPNN are used as the prediction models to compare the results in the raw and transformed data sets. Moreover, we also compare the different values of ε in three conditions, Q1 (one-fourth quarter), Q2 (median), and Q3 (three-fourth quarter) in the MLCC and TFT-LCD cases to ensure the robustness of the ε settings.

## 4.1. Case I: MLCC

An MLCC is a product composed of ceramic powder, which contributes about 40% of the entire production cost, and is thus a great in-<sup>fl</sup>uence on the pro<sup>fi</sup>t margin. Most of the key technology for ceramic powder is currently held by Japanese manufacturers, though some domestic Taiwanese <sup>fi</sup>rms are developing their own techniques. Many of the physical characteristics of ceramic powder are dif<sup>fi</sup>cult to understand and control, and one notable problem is the low stability among batches. Consequently, manufacturers must do some pilot runs after receiving a batch of powder to assess the dielectric constant (K-value), which is the dielectric property that determines the amount of electrostatic energy stored in a capacitor relative to a vacuum, and is considered the material's most important characteristic. This work leads to a delay in production and thus increases in costs. Therefore, if one can appraise the K-value faster and infer the production parameters and the defect rate, the related lead time and stock costs will be decreased. This case is thus used to predict the K-value of the AD143 ceramic powder. After consulting a Taiwanese manufacturer, there are twelve key input factors that affect the K-value, as follows: SA, PSD-90, PSD-50, PSD-10, Mois, Sinter Temp, K, DF, TC-min, TC-max, TC-peak, and D-50 [33].

![](/api/attachments/Y45UQMC7/fulltext/images/f4ecda7d52850b23a0983e69ac2aafc374a04d6a79ab8de75be71690f95f8bd2.jpg)  
Fig. 7. The transformation function for each attribute of samples in cluster K.

Table 2 Results of data-clustering.

<table><tr><td>Data</td><td>Cluster</td></tr><tr><td> $X_1$ </td><td>Noise</td></tr><tr><td> $X_2$ </td><td>1</td></tr><tr><td> $X_3$ </td><td>Noise</td></tr><tr><td> $X_4$ </td><td>1</td></tr><tr><td> $X_5$ </td><td>1</td></tr></table>

## 4.1.1. Parameter settings and experimental design

The parameter settings are shown in Table 4. For the MTD function, Li et al. [17] suggested the parameter f(t) be set at $\ln ( 1 0 ^ { - 2 0 } )$ and thus this is used in this paper. In the SVR, the parameter setting of C is 1.0, the kernel is RBF, and the other parameters are the default settings of WEKA (the subsequent parameter settings of the SVR are the same as here). The parameters of the BPNN are a learning rate of 0.3, learning time of 500, and momentum of 0.2. The radius of DBSCAN is ε, which is based on the selected sample's distance. In this case, resampling experiments were used in which each experiment has different samples, and thus ε is dynamic.

We obtained data from the Ferro Company, and 44 pilot runs were collected. The experiment was designed for small data sets, where 5, 10, 15, 20 and 25 training data are randomly selected for resampling 20 times. For performance evaluation, the average and the error improving rate are used to compare the initial and transformed data. We use the average MSE and average error rate to evaluate the LR, SVR, and BPNN methods, and the tool for analysis is the WEKA 3.7.2, software, downloaded from: http://www.weka.com/download.

$$
\text { Average   MSE } = \frac {\sum_ {i = 1} ^ {2 0} M S E _ {x i}}{2 0}\tag{14}
$$

$$
\text { The   error   improving   rate } = \frac {\sum_ {i = 1} ^ {2 0} \frac {\text { Raw } _ {i} - \text { Transform } _ {i}}{\text { Raw } _ {i}}}{2 0}.\tag{15}
$$

## 4.1.2. Sensitivity analysis

In this section, we compare the different values of ε in three conditions, Q1, Q2, and Q3. Table 5 shows the results for the P-value in each size, where the SVR shows no signi<sup>fi</sup>cant differences in Q1 and Q2, Q2 and Q3, and Q1 and Q3 (P>0.05).

## 4.1.3. The results of the experiment

This section describes the changes in the average MSE and the error improving rate of the three prediction models. Table 6 shows details of the resampling experiment. As Table 7 shows, all the models improved with regard to average MSE. Note that when the data transforms into a higher dimension, LR faces certain problems in degree, and thus we evaluate only the performance of BPNN and SVR for transformed data. In Table 7, raw- represents using the raw data set to process the prediction, and transform- refers using the transformed data set.

Table 3  
The transformation value of X.

<table><tr><td>Data</td><td>Att1</td><td> $M^{1}(A_{1})$ </td><td>Att2</td><td> $M^{1}(A_{2})$ </td><td>Y</td></tr><tr><td> $X_{1}$ </td><td>1</td><td>0.66</td><td>1.12</td><td>0.46</td><td>10.2</td></tr><tr><td> $X_{2}$ </td><td>0.09</td><td>0.69</td><td>-0.68</td><td>0.93</td><td>9.64</td></tr><tr><td> $X_{3}$ </td><td>1.41</td><td>0.4</td><td>-0.03</td><td>0.76</td><td>9.87</td></tr><tr><td> $X_{4}$ </td><td>0.8</td><td>0.78</td><td>-1.75</td><td>0.69</td><td>9.5</td></tr><tr><td> $X_{5}$ </td><td>0.49</td><td>0.97</td><td>-0.11</td><td>0.78</td><td>9.93</td></tr></table>

Table 4  
Parameter settings of the models.

<table><tr><td></td><td>SVR</td><td>BPNN</td><td>DBSCAN</td><td>MTD</td></tr><tr><td rowspan="4">Parameter setting</td><td>C = 1.0</td><td>Learning rate = 0.3</td><td>Minpts = 2</td><td rowspan="4"> $f(t) = \ln (10^{-20})$ </td></tr><tr><td>RBF kernel</td><td>Momentum = 0.2</td><td> $\varepsilon$ =dynamic</td></tr><tr><td>Degree = 3</td><td>Training time = 500</td><td></td></tr><tr><td>Gamma = 0.5</td><td></td><td></td></tr></table>

Table 8 shows the error improving rate for the two prediction models, both of which show good performance for all sample sizes. In the statistical t-test which we have conducted, except for a sample size of 5 in the BPNN, the proposed method outperforms the other methods for all sample sizes.

## 4.2. Case II: Concrete slump test

The data set includes 103 data points, with seven input, and three output variables. We select one of the three output variables, SLUMP, as our prediction object [36]. The seven input variables are cement, slag, <sup>fl</sup>y ash, water, SP, coarse aggr., and <sup>fi</sup>ne aggr. The experiment design and parameter settings are the same as those in the MLCC case.

## 4.2.1. The results of the experiment

As the results show in Table 9, the proposed method has good prediction ability in both the SVR and BPNN. Table 10 shows the details of the resampling experiment.

The error improving rate and p-value are shown in Table 11. The results of the t-test show the signi<sup>fi</sup>cant improvement of the proposed method with regard to the SVR model (Pb0.05). However, with the BPNN, it shows no signi<sup>fi</sup>cant difference in sizes 10 and 25.

## 4.3. Case III: TFT-LCD

TFT-LCDs are widely used in TVs, notebook computers, mobile phones, and digital cameras. A TFT-LCD consists of a Thin Film Transistor (TFT) panel and a Color Filter (CF) panel. In the process of making a cell, a TFT panel is precisely aligned with a CF panel and then combined. The cell vernier is de<sup>fi</sup>ned as the distance (or error) between the TFT alignment marks and the CF alignment marks. If the value of the cell vernier is high, the panel will have insuf<sup>fi</sup>ciently high contrast, and thus it is a very important factor for high panel quality. Manufacturers de<sup>fi</sup>ne the error between the designed and the actual pitch values of a panel as the total pitch error (TPE). There are six TPEs in a CF and six in a TFT. Considering the complex process of making a TFT, to reduce vernier values, engineers usually prefer to adjust the TPEs in a CF to match a TFT in the alignment process. The input data is the six TPEs in a panel, X1, X4, Y1, Y6, D1, and D2. Nineteen valid yield data points for making middle-size panels were collected from statics process control (SPC) database, and more details are given in [18].

## 4.3.1. Parameter setting and experimental design

This case used leave-one-out cross-validation to compare the raw and transformed data sets. The parameter settings are almost the

Table 5  
The sensitivity analysis in the MLCC case.

<table><tr><td rowspan="2">Size</td><td colspan="3">SVR</td><td colspan="3">BPNN</td></tr><tr><td>Q1 and Q2</td><td>Q2 and Q3</td><td>Q1 and Q3</td><td>Q1 and Q2</td><td>Q2 and Q3</td><td>Q1 and Q3</td></tr><tr><td>5</td><td>0.497</td><td>0.473</td><td>0.857</td><td>0.764</td><td>0.905</td><td>0.842</td></tr><tr><td>10</td><td>0.131</td><td>0.092</td><td>0.953</td><td>0.919</td><td>0.998</td><td>0.949</td></tr><tr><td>15</td><td>0.498</td><td>0.701</td><td>0.831</td><td>0.481</td><td>0.918</td><td>0.447</td></tr><tr><td>20</td><td>0.084</td><td>0.891</td><td>0.098</td><td>0.001</td><td>0.309</td><td>0.158</td></tr><tr><td>25</td><td>0.136</td><td>0.917</td><td>0.23</td><td>0.087</td><td>0.004</td><td>0.161</td></tr></table>

<table><tr><td>Size</td><td>Raw-LR</td><td>Raw-SVR</td><td>Transform-SVR</td><td>Raw-BPNN</td><td>Transform-BPNN</td></tr><tr><td>5</td><td>1372.52</td><td>983.90</td><td>959.34</td><td>1302.54</td><td>1256.83</td></tr><tr><td>10</td><td>1568.23</td><td>939.48</td><td>884.83</td><td>1434.44</td><td>1173.71</td></tr><tr><td>15</td><td>1408.98</td><td>954.97</td><td>860.14</td><td>1509.74</td><td>1122.28</td></tr><tr><td>20</td><td>1300.34</td><td>926.30</td><td>866.40</td><td>1390.49</td><td>1105.11</td></tr><tr><td>25</td><td>1047.40</td><td>891.76</td><td>818.54</td><td>1442.95</td><td>1051.02</td></tr></table>

The details of the resam<sub>p</sub>lin<sub>g</sub> ex<sub>p</sub>eriment in the MLCC case  
<sup>al.</sup> <sup>/</sup> <sup>Decision</sup> <sup>Support</sup> <sup>Syste</sup>m<sub>s</sub> <sub>52</sub> <sub>(2012</sub>

<table><tr><td rowspan="2">MLCC</td><td colspan="5">Size = 5</td><td colspan="5">Size = 10</td><td colspan="5">Size = 15</td><td colspan="5">Size = 20</td><td colspan="5">Size = 25</td></tr><tr><td colspan="3">Raw</td><td colspan="2">Transformed</td><td colspan="3">Raw</td><td colspan="2">Transform</td><td colspan="3">Raw</td><td colspan="2">Transformed</td><td colspan="3">Raw</td><td colspan="2">Transformed</td><td colspan="3">Raw</td><td colspan="2">Transformed</td></tr><tr><td>Sample</td><td>LR</td><td>SVR</td><td>BPNN</td><td>SVR</td><td>BPNN</td><td>LR</td><td>SVR</td><td>BPNN</td><td>SVR</td><td>BPNN</td><td>LR</td><td>SVR</td><td>BPNN</td><td>SVR</td><td>BPNN</td><td>LR</td><td>SVR</td><td>BPNN</td><td>SVR</td><td>BPNN</td><td>LR</td><td>SVR</td><td>BPNN</td><td>SVR</td><td>BPNN</td></tr><tr><td>1</td><td>1823.3</td><td>1039.4</td><td>1856.9</td><td>950.9</td><td>1655.0</td><td>1639.3</td><td>855.3</td><td>1865.1</td><td>780.3</td><td>1371.8</td><td>1482.2</td><td>1210.6</td><td>1502.6</td><td>1005.3</td><td>1264.5</td><td>1192.5</td><td>871.7</td><td>807.4</td><td>888.5</td><td>1074.2</td><td>1085.0</td><td>925.7</td><td>1496.7</td><td>729.4</td><td>748.0</td></tr><tr><td>2</td><td>1631.2</td><td>856.3</td><td>1273.2</td><td>850.6</td><td>1095.1</td><td>1667.0</td><td>871.1</td><td>1521.6</td><td>832.2</td><td>1133.3</td><td>1384.0</td><td>932.1</td><td>1159.8</td><td>916.9</td><td>1031.7</td><td>1385.4</td><td>851.5</td><td>1743.5</td><td>800.2</td><td>1026.5</td><td>784.3</td><td>799.5</td><td>2129.9</td><td>844.9</td><td>987.0</td></tr><tr><td>3</td><td>1279.9</td><td>1045.0</td><td>1270.2</td><td>997.7</td><td>1190.8</td><td>1951.6</td><td>818.1</td><td>1469.4</td><td>852.9</td><td>1293.7</td><td>1303.9</td><td>970.6</td><td>1771.7</td><td>723.3</td><td>1162.9</td><td>1014.0</td><td>833.9</td><td>1281.9</td><td>828.4</td><td>1152.8</td><td>1285.1</td><td>1033.1</td><td>1374.2</td><td>834.8</td><td>1135.0</td></tr><tr><td>4</td><td>1259.3</td><td>989.1</td><td>1239.0</td><td>955.6</td><td>1006.1</td><td>1106.9</td><td>868.5</td><td>1105.2</td><td>803.7</td><td>960.4</td><td>1781.1</td><td>1051.1</td><td>1897.9</td><td>927.8</td><td>1052.2</td><td>851.9</td><td>786.8</td><td>1224.9</td><td>816.3</td><td>1007.7</td><td>1038.1</td><td>962.0</td><td>1786.5</td><td>768.1</td><td>1120.9</td></tr><tr><td>5</td><td>1537.3</td><td>880.2</td><td>1392.1</td><td>887.5</td><td>1379.3</td><td>1051.8</td><td>904.1</td><td>1244.0</td><td>919.8</td><td>1033.8</td><td>1277.3</td><td>851.6</td><td>1768.4</td><td>726.7</td><td>1066.4</td><td>1421.5</td><td>1098.1</td><td>1603.5</td><td>815.1</td><td>939.1</td><td>1226.9</td><td>784.6</td><td>1380.6</td><td>801.9</td><td>860.2</td></tr><tr><td>6</td><td>1863.2</td><td>912.0</td><td>1243.0</td><td>874.6</td><td>1360.9</td><td>1418.0</td><td>1003.2</td><td>1370.9</td><td>977.0</td><td>1106.5</td><td>1292.6</td><td>906.3</td><td>1883.1</td><td>870.4</td><td>1419.1</td><td>1368.4</td><td>998.8</td><td>1367.3</td><td>969.3</td><td>1025.3</td><td>936.9</td><td>814.6</td><td>915.2</td><td>1022.0</td><td>1475.1</td></tr><tr><td>7</td><td>1048.7</td><td>922.6</td><td>1029.5</td><td>871.8</td><td>949.4</td><td>1311.1</td><td>871.2</td><td>982.8</td><td>906.0</td><td>892.1</td><td>1496.5</td><td>969.0</td><td>1404.3</td><td>886.3</td><td>1424.0</td><td>1021.3</td><td>1061.2</td><td>1561.2</td><td>980.7</td><td>1453.6</td><td>861.5</td><td>980.0</td><td>1293.1</td><td>948.3</td><td>1234.2</td></tr><tr><td>8</td><td>1107.1</td><td>849.9</td><td>1056.7</td><td>824.5</td><td>1374.9</td><td>1067.3</td><td>899.5</td><td>1209.7</td><td>966.0</td><td>1132.8</td><td>1543.3</td><td>966.9</td><td>1799.4</td><td>926.8</td><td>1106.7</td><td>1437.9</td><td>972.2</td><td>1739.4</td><td>880.0</td><td>1524.7</td><td>726.1</td><td>701.1</td><td>1495.4</td><td>771.5</td><td>1104.7</td></tr><tr><td>9</td><td>1047.1</td><td>899.0</td><td>1044.0</td><td>915.7</td><td>1154.9</td><td>1111.8</td><td>921.5</td><td>1299.3</td><td>941.4</td><td>1041.7</td><td>902.7</td><td>867.8</td><td>1166.9</td><td>772.4</td><td>1030.0</td><td>1110.2</td><td>906.0</td><td>1308.3</td><td>831.0</td><td>1140.1</td><td>1123.2</td><td>887.3</td><td>1533.2</td><td>710.8</td><td>889.8</td></tr><tr><td>10</td><td>1175.7</td><td>1067.6</td><td>1234.4</td><td>1041.1</td><td>1079.0</td><td>1749.9</td><td>1034.4</td><td>1622.8</td><td>879.7</td><td>1103.2</td><td>1519.5</td><td>956.2</td><td>1325.3</td><td>846.4</td><td>951.3</td><td>2219.0</td><td>1192.3</td><td>2110.8</td><td>948.2</td><td>1496.5</td><td>1089.0</td><td>904.1</td><td>978.5</td><td>732.6</td><td>907.7</td></tr><tr><td>11</td><td>1124.9</td><td>979.5</td><td>1082.3</td><td>991.3</td><td>1150.7</td><td>1580.2</td><td>1058.2</td><td>1600.5</td><td>882.5</td><td>1344.0</td><td>1137.9</td><td>928.0</td><td>861.2</td><td>928.4</td><td>1032.6</td><td>1385.8</td><td>974.9</td><td>1042.8</td><td>949.4</td><td>919.8</td><td>877.4</td><td>758.5</td><td>1310.5</td><td>791.6</td><td>907.1</td></tr><tr><td>12</td><td>2504.4</td><td>865.4</td><td>2219.7</td><td>816.7</td><td>1322.7</td><td>1419.9</td><td>1166.8</td><td>1371.3</td><td>1148.2</td><td>1284.3</td><td>1614.3</td><td>1110.5</td><td>1369.0</td><td>958.9</td><td>1183.9</td><td>1027.9</td><td>788.8</td><td>924.8</td><td>771.1</td><td>1138.8</td><td>906.9</td><td>1015.1</td><td>1784.3</td><td>946.7</td><td>1327.5</td></tr><tr><td>13</td><td>1232.5</td><td>932.9</td><td>1218.3</td><td>900.0</td><td>1132.3</td><td>2251.2</td><td>1130.9</td><td>1932.9</td><td>907.2</td><td>1205.0</td><td>2499.6</td><td>946.9</td><td>1686.4</td><td>914.2</td><td>1327.8</td><td>1674.8</td><td>913.8</td><td>1128.4</td><td>917.3</td><td>1183.2</td><td>922.3</td><td>926.6</td><td>1693.4</td><td>833.0</td><td>1032.8</td></tr><tr><td>14</td><td>1239.2</td><td>1182.9</td><td>1255.8</td><td>1163.4</td><td>1280.6</td><td>1102.0</td><td>969.4</td><td>1349.9</td><td>927.1</td><td>1460.7</td><td>976.8</td><td>958.1</td><td>1284.4</td><td>862.2</td><td>1112.8</td><td>1258.7</td><td>854.4</td><td>1024.2</td><td>867.3</td><td>964.1</td><td>1018.1</td><td>1020.4</td><td>1606.0</td><td>797.3</td><td>1317.4</td></tr><tr><td>15</td><td>1255.4</td><td>1098.7</td><td>1289.5</td><td>1095.0</td><td>1196.8</td><td>2030.0</td><td>922.5</td><td>1583.0</td><td>838.6</td><td>1301.4</td><td>1636.7</td><td>1123.7</td><td>1324.7</td><td>882.4</td><td>1129.9</td><td>1451.4</td><td>900.6</td><td>1271.9</td><td>889.7</td><td>1035.6</td><td>905.5</td><td>791.2</td><td>967.2</td><td>819.0</td><td>717.2</td></tr><tr><td>16</td><td>1141.7</td><td>1142.2</td><td>1254.7</td><td>1138.3</td><td>1447.8</td><td>2132.8</td><td>815.6</td><td>1206.5</td><td>771.7</td><td>1624.0</td><td>1163.1</td><td>884.6</td><td>1629.7</td><td>755.4</td><td>922.1</td><td>976.8</td><td>767.4</td><td>1311.7</td><td>800.8</td><td>1017.4</td><td>895.1</td><td>873.0</td><td>1090.4</td><td>791.3</td><td>1212.5</td></tr><tr><td>17</td><td>1238.1</td><td>969.2</td><td>1061.7</td><td>992.2</td><td>1072.6</td><td>1697.1</td><td>874.9</td><td>1411.4</td><td>837.0</td><td>1266.8</td><td>1145.3</td><td>753.7</td><td>1580.3</td><td>767.3</td><td>993.2</td><td>1232.4</td><td>889.8</td><td>1542.9</td><td>821.8</td><td>990.2</td><td>1803.1</td><td>1113.1</td><td>1798.1</td><td>869.4</td><td>1227.4</td></tr><tr><td>18</td><td>1299.3</td><td>897.9</td><td>1255.1</td><td>871.9</td><td>1722.1</td><td>1508.0</td><td>953.2</td><td>1471.1</td><td>874.7</td><td>1147.8</td><td>966.6</td><td>814.3</td><td>902.9</td><td>840.6</td><td>1018.2</td><td>1274.7</td><td>1065.4</td><td>1528.8</td><td>851.7</td><td>876.5</td><td>1402.7</td><td>980.8</td><td>1134.7</td><td>863.5</td><td>1071.9</td></tr><tr><td>19</td><td>1413.2</td><td>1000.2</td><td>1533.1</td><td>941.6</td><td>1405.4</td><td>1575.9</td><td>972.8</td><td>1271.8</td><td>917.4</td><td>1164.7</td><td>1550.8</td><td>951.5</td><td>1461.2</td><td>860.6</td><td>1014.5</td><td>1190.8</td><td>909.0</td><td>1780.5</td><td>846.6</td><td>1069.2</td><td>1329.0</td><td>826.1</td><td>1813.5</td><td>811.5</td><td>673.6</td></tr><tr><td>20</td><td>1229.0</td><td>1148.1</td><td>1241.6</td><td>1106.6</td><td>1160.2</td><td>1994.0</td><td>878.2</td><td>1792.3</td><td>754.5</td><td>1171.2</td><td>1505.4</td><td>945.7</td><td>2415.6</td><td>830.5</td><td>1201.9</td><td>1511.3</td><td>889.5</td><td>1505.6</td><td>854.5</td><td>1067.8</td><td>731.9</td><td>738.6</td><td>1277.7</td><td>683.3</td><td>1070.5</td></tr></table>

<sup>ose</sup> <sup>in</sup> <sup>the</sup> <sup>previous</sup> <sup>ca</sup><sub>ses.</sub> <sub>The</sub> <sub>only</sub> <sub>difference</sub> <sup>s</sup> <sup>cases</sup> <sup>are</sup> <sup>dyna</sup>m<sub>ically</sub> <sub>changed</sub> <sub>based</sub> <sub>on</sub> <sub>the</sub> <sup>t.</sup> <sup>As</sup> <sup>this</sup> <sup>case</sup> <sup>does</sup> <sup>not</sup> <sup>use</sup> <sup>a</sup> <sup>resa</sup>m<sub>pling</sub> <sub>expe</sub> <sup>d</sup> <sup>value</sup> <sup>(0.45).</sup> <sup>The</sup> <sup>experime</sup>n<sub>t</sub> <sub>was</sub> <sub>designed</sub> <sup>all</sup> <sup>data</sup> <sup>set</sup> <sup>analysis</sup> <sup>by</sup> <sup>usi</sup>n<sub>g</sub> <sub>the</sub> <sub>clustering-p</sub> <sup>ew</sup> <sup>attributes.</sup> <sup>The</sup> m<sub>ean</sub> <sub>square</sub> <sub>error</sub> <sub>(MSE)</sub> <sup>mpare</sup> <sup>the</sup> <sup>initi</sup>a<sub>l</sub> <sub>and</sub> <sub>transformed</sub> <sub>data</sub> <sub>for</sub> <sub>p</sub> <sup>In</sup> <sup>this</sup> <sup>section,</sup> <sup>we</sup> w<sub>ill</sub> <sub>use</sub> <sub>the</sub> <sub>total</sub> <sub>errors,</sub> <sub>MS</sub> <sup>ions</sup> <sup>to</sup> <sup>evaluate</sup> <sup>the</sup> <sup>three</sup> <sup>prediction</sup> m<sub>odels</sub> m<sub>pared</sub> <sub>the</sub> <sub>different</sub> <sub>values</sub> <sub>of</sub> <sub>theε</sub> <sub>setting</sub> <sub>at</sub> Q<sub>3.</sub>

<sup>ensitivity</sup> <sup>ana</sup>l<sub>ysis</sub> <sub>and</sub> <sub>expe</sub> <sup>ho</sup>w<sub>s</sub> <sub>the</sub> <sub>prediction</sub> <sub>results</sub> <sub>of</sub> <sub>differentε</sub> <sub>in</sub> <sup>nd</sup> <sup>Q3</sup> <sup>(0.56).</sup> <sup>The</sup> <sup>results</sup> <sup>sho</sup>w <sub>that</sub> <sub>there</sub> <sub>is</sub> <sub>n</sub> <sup>e</sup> <sup>in</sup> <sup>either</sup> <sup>the</sup> <sup>SVR</sup> <sup>and</sup> <sup>BPNN</sup> m<sub>odels</sub> <sub>(</sub>

<sup>ows</sup> <sup>the</sup> <sup>three</sup> <sup>prediction</sup> m<sub>odels'</sub> <sub>performan</sub> <sup>he</sup> <sup>results</sup> <sup>show</sup> <sup>th</sup><sub>at</sub> <sub>MSE,</sub> <sub>total</sub> <sub>errors,</sub> <sub>and</sub> <sub>sta</sub> <sup>all</sup> <sup>improved,</sup> <sup>SVR</sup> <sup>havi</sup>n<sub>g</sub> <sub>the</sub> <sub>best</sub> <sub>perform</sub> <sup>ure-based</sup> <sup>data</sup> <sup>transfor</sup>m

<sup>he</sup> <sup>proposed</sup> <sup>method</sup> <sup>does</sup> <sub>not</sub> <sub>perform</sub> <sub>stati</sub> w<sub>ell</sub> <sub>in</sub> <sub>this</sub> <sub>data</sub> <sub>set,</sub> <sub>it</sub> <sub>has</sub> <sub>good</sub> <sub>prediction</sub> <sub>ac</sub> <sup>he</sup> <sup>MSE.</sup> W<sub>e</sub> <sub>thus</sub> <sub>use</sub> <sub>another</sub> <sub>index,</sub> <sub>quality</sub> <sub>s</sub> <sup>esents</sup> <sup>the</sup> <sup>acceptable</sup> <sup>range</sup> <sup>in</sup> <sup>the</sup> <sup>TFT-LC</sup>D <sup>erformance</sup> <sup>of</sup> <sup>the</sup> <sub>proposed</sub> <sub>method.</sub> <sub>In</sub> <sub>this</sub> <sub>c</sub> <sup>lue</sup> <sup>is</sup> <sup>given</sup> <sup>by</sup> <sup>factory</sup> <sup>e</sup>n<sub>gineers</sub> <sub>and</sub> <sub>the</sub> <sub>acc</sub> <sup>9.49</sup> <sup>to</sup> <sup>9.91.</sup> <sup>The</sup> <sup>results</sup> <sup>sho</sup>w <sub>that</sub> <sub>the</sub> <sub>propo</sub> <sup>0.5%</sup> <sup>impr</sup>o<sub>vement</sub> <sub>rate</sub> <sub>in</sub> <sub>SVR,</sub> <sub>and</sub> <sub>15.8%</sub> <sub>in</sub> <sub>B</sub> <sup>e</sup> <sup>conclude</sup> <sup>that</sup> <sup>the</sup> <sup>proposed</sup> m<sub>ethod</sub> <sub>is</sub> <sub>indeed</sub> <sup>cessing</sup> <sup>for</sup> <sup>the</sup> <sup>SVR</sup> <sup>and</sup> <sup>BPN</sup><sub>N</sub> <sub>approaches.</sub> <sub>In</sub> <sub>a</sub> <sup>uted</sup> <sup>the</sup> <sup>impr</sup>o<sub>vements</sub> <sub>in</sub> <sub>the</sub> <sub>prediction</sub> <sub>acc</sub> <sup>proposed</sup> m<sub>ethodology</sub> <sub>to</sub> <sub>the</sub> <sub>TFT-LCD</sub> <sub>case</sub> <sup>y</sup> <sup>Li</sup> <sup>et</sup> <sup>al.[18],</sup> <sup>and</sup> <sup>the</sup> <sup>MSE</sup> <sub>is</sub> <sub>improved</sub> <sub>fro</sub> <sup>.21</sup><sub>90</sub>

The details of the resam<sub>p</sub>lin<sub>g</sub> ex<sub>p</sub>eriment in concrete slum<sub>p</sub> test case.

<table><tr><td rowspan="2">Slump</td><td colspan="5">Size = 5</td><td colspan="5">Size = 10</td><td colspan="5">Size = 15</td><td colspan="5">Size = 20</td><td colspan="5">Size = 25</td></tr><tr><td colspan="3">Raw</td><td colspan="2">Transformed</td><td colspan="3">Raw</td><td colspan="2">Transformed</td><td colspan="3">Raw</td><td colspan="2">Transformed</td><td colspan="3">Raw</td><td colspan="2">Transformed</td><td colspan="3">Raw</td><td colspan="2">Transformed</td></tr><tr><td>Sample</td><td>LR</td><td>SVR</td><td>BPNN</td><td>SVR</td><td>BPNN</td><td>LR</td><td>SVR</td><td>BPNN</td><td>SVR</td><td>BPNN</td><td>LR</td><td>SVR</td><td>BPNN</td><td>SVR</td><td>BPNN</td><td>LR</td><td>SVR</td><td>BPNN</td><td>SVR</td><td>BPNN</td><td>LR</td><td>SVR</td><td>BPNN</td><td>SVR</td><td>BPNN</td></tr><tr><td>1</td><td>15.65</td><td>6.63</td><td>6.13</td><td>6.59</td><td>6.32</td><td>11.21</td><td>6.34</td><td>11.70</td><td>6.60</td><td>12.65</td><td>9.16</td><td>7.01</td><td>15.14</td><td>6.81</td><td>10.65</td><td>7.36</td><td>6.32</td><td>8.59</td><td>6.35</td><td>8.83</td><td>7.67</td><td>6.44</td><td>8.09</td><td>6.32</td><td>6.62</td></tr><tr><td>2</td><td>9.68</td><td>6.43</td><td>18.01</td><td>6.30</td><td>13.97</td><td>7.28</td><td>6.43</td><td>9.81</td><td>6.61</td><td>11.45</td><td>8.72</td><td>6.45</td><td>8.13</td><td>6.22</td><td>7.74</td><td>8.47</td><td>6.61</td><td>11.11</td><td>6.45</td><td>10.73</td><td>7.19</td><td>6.85</td><td>10.14</td><td>6.47</td><td>7.56</td></tr><tr><td>3</td><td>8.43</td><td>7.39</td><td>8.21</td><td>7.30</td><td>7.86</td><td>6.70</td><td>6.72</td><td>7.64</td><td>6.53</td><td>10.35</td><td>7.17</td><td>6.53</td><td>8.98</td><td>6.50</td><td>8.13</td><td>7.59</td><td>6.85</td><td>11.17</td><td>6.98</td><td>7.81</td><td>6.77</td><td>6.14</td><td>14.68</td><td>5.63</td><td>6.79</td></tr><tr><td>4</td><td>8.44</td><td>6.33</td><td>8.53</td><td>6.24</td><td>7.93</td><td>9.82</td><td>6.22</td><td>5.51</td><td>6.27</td><td>6.02</td><td>10.14</td><td>6.08</td><td>12.79</td><td>6.31</td><td>11.81</td><td>7.58</td><td>5.88</td><td>8.91</td><td>5.69</td><td>6.57</td><td>7.71</td><td>6.91</td><td>14.88</td><td>6.65</td><td>6.91</td></tr><tr><td>5</td><td>16.08</td><td>6.59</td><td>12.27</td><td>6.35</td><td>10.57</td><td>7.88</td><td>6.77</td><td>9.63</td><td>6.76</td><td>12.45</td><td>7.00</td><td>6.14</td><td>6.07</td><td>5.98</td><td>7.10</td><td>7.47</td><td>6.90</td><td>6.33</td><td>6.75</td><td>9.18</td><td>7.35</td><td>6.09</td><td>5.56</td><td>5.56</td><td>10.30</td></tr><tr><td>6</td><td>12.10</td><td>7.06</td><td>11.48</td><td>7.16</td><td>9.67</td><td>7.14</td><td>6.85</td><td>8.62</td><td>6.56</td><td>10.99</td><td>8.99</td><td>8.87</td><td>8.68</td><td>8.12</td><td>9.61</td><td>6.89</td><td>6.17</td><td>6.69</td><td>5.46</td><td>6.15</td><td>7.63</td><td>6.58</td><td>6.94</td><td>6.26</td><td>8.35</td></tr><tr><td>7</td><td>14.29</td><td>7.19</td><td>7.45</td><td>6.79</td><td>8.24</td><td>8.76</td><td>8.07</td><td>9.18</td><td>7.47</td><td>7.84</td><td>8.24</td><td>7.22</td><td>8.85</td><td>7.24</td><td>8.11</td><td>8.67</td><td>7.12</td><td>11.56</td><td>6.26</td><td>7.00</td><td>6.98</td><td>7.29</td><td>7.34</td><td>7.05</td><td>7.66</td></tr><tr><td>8</td><td>24.16</td><td>7.80</td><td>14.89</td><td>7.56</td><td>12.51</td><td>8.49</td><td>6.57</td><td>6.94</td><td>6.42</td><td>9.68</td><td>7.45</td><td>6.62</td><td>7.05</td><td>6.65</td><td>8.03</td><td>7.27</td><td>6.04</td><td>9.25</td><td>6.08</td><td>7.16</td><td>7.17</td><td>6.15</td><td>12.60</td><td>6.19</td><td>7.95</td></tr><tr><td>9</td><td>8.34</td><td>7.07</td><td>7.96</td><td>7.07</td><td>7.26</td><td>7.32</td><td>6.26</td><td>7.51</td><td>6.31</td><td>8.23</td><td>6.70</td><td>7.14</td><td>9.22</td><td>7.26</td><td>7.67</td><td>6.90</td><td>6.34</td><td>9.47</td><td>6.44</td><td>9.11</td><td>6.82</td><td>6.14</td><td>12.32</td><td>5.90</td><td>9.19</td></tr><tr><td>10</td><td>10.75</td><td>6.64</td><td>10.61</td><td>6.52</td><td>7.56</td><td>13.10</td><td>8.76</td><td>12.63</td><td>8.64</td><td>9.38</td><td>9.10</td><td>6.31</td><td>12.21</td><td>6.21</td><td>10.19</td><td>7.19</td><td>6.19</td><td>10.84</td><td>5.76</td><td>8.07</td><td>7.32</td><td>5.93</td><td>9.80</td><td>5.88</td><td>8.13</td></tr><tr><td>11</td><td>12.39</td><td>8.05</td><td>8.78</td><td>7.95</td><td>6.66</td><td>14.58</td><td>6.71</td><td>16.08</td><td>6.51</td><td>13.12</td><td>9.40</td><td>6.67</td><td>17.49</td><td>6.52</td><td>9.16</td><td>6.05</td><td>6.00</td><td>19.67</td><td>5.79</td><td>9.44</td><td>7.16</td><td>6.46</td><td>7.98</td><td>6.11</td><td>7.35</td></tr><tr><td>12</td><td>14.75</td><td>6.62</td><td>10.67</td><td>6.58</td><td>10.86</td><td>10.50</td><td>6.48</td><td>9.24</td><td>6.17</td><td>7.38</td><td>9.98</td><td>7.40</td><td>9.75</td><td>7.02</td><td>7.84</td><td>8.83</td><td>6.87</td><td>14.49</td><td>6.65</td><td>8.35</td><td>9.05</td><td>7.32</td><td>10.05</td><td>6.99</td><td>10.65</td></tr><tr><td>13</td><td>6.24</td><td>7.07</td><td>6.34</td><td>7.14</td><td>6.38</td><td>7.13</td><td>6.46</td><td>18.62</td><td>6.20</td><td>10.12</td><td>8.30</td><td>6.53</td><td>8.65</td><td>6.68</td><td>8.33</td><td>12.46</td><td>5.95</td><td>17.11</td><td>5.65</td><td>6.68</td><td>7.66</td><td>6.31</td><td>5.34</td><td>6.19</td><td>7.27</td></tr><tr><td>14</td><td>6.60</td><td>6.77</td><td>9.11</td><td>6.76</td><td>7.25</td><td>9.93</td><td>6.97</td><td>8.93</td><td>6.39</td><td>8.73</td><td>7.91</td><td>6.82</td><td>15.95</td><td>6.78</td><td>7.59</td><td>9.04</td><td>6.86</td><td>10.61</td><td>6.53</td><td>11.95</td><td>6.26</td><td>6.39</td><td>7.32</td><td>6.47</td><td>7.14</td></tr><tr><td>15</td><td>17.84</td><td>11.22</td><td>16.75</td><td>10.42</td><td>19.07</td><td>12.16</td><td>6.22</td><td>8.83</td><td>6.32</td><td>7.78</td><td>8.37</td><td>6.85</td><td>8.99</td><td>6.54</td><td>9.40</td><td>6.56</td><td>6.50</td><td>6.01</td><td>6.27</td><td>8.12</td><td>6.11</td><td>5.87</td><td>10.09</td><td>5.64</td><td>7.01</td></tr><tr><td>16</td><td>16.34</td><td>8.60</td><td>6.04</td><td>8.38</td><td>5.93</td><td>13.36</td><td>8.34</td><td>8.16</td><td>8.36</td><td>11.78</td><td>7.47</td><td>6.06</td><td>10.90</td><td>5.54</td><td>7.69</td><td>8.25</td><td>6.90</td><td>8.61</td><td>7.49</td><td>11.99</td><td>7.43</td><td>6.39</td><td>6.50</td><td>6.32</td><td>8.09</td></tr><tr><td>17</td><td>15.22</td><td>6.81</td><td>15.64</td><td>6.73</td><td>12.01</td><td>8.74</td><td>6.94</td><td>10.27</td><td>6.89</td><td>8.50</td><td>8.88</td><td>7.86</td><td>14.49</td><td>6.66</td><td>9.68</td><td>7.50</td><td>7.31</td><td>7.66</td><td>7.18</td><td>7.12</td><td>6.98</td><td>5.83</td><td>7.30</td><td>5.46</td><td>9.54</td></tr><tr><td>18</td><td>7.95</td><td>9.28</td><td>12.20</td><td>8.26</td><td>12.73</td><td>12.14</td><td>7.56</td><td>11.95</td><td>7.47</td><td>8.91</td><td>6.60</td><td>6.17</td><td>5.78</td><td>6.66</td><td>5.92</td><td>7.72</td><td>6.55</td><td>13.91</td><td>6.49</td><td>8.79</td><td>6.55</td><td>6.15</td><td>13.63</td><td>5.98</td><td>9.30</td></tr><tr><td>19</td><td>27.74</td><td>6.46</td><td>8.84</td><td>6.57</td><td>8.88</td><td>7.19</td><td>6.87</td><td>7.72</td><td>6.85</td><td>6.73</td><td>6.93</td><td>6.31</td><td>9.35</td><td>6.27</td><td>8.12</td><td>6.59</td><td>6.55</td><td>15.26</td><td>6.29</td><td>7.97</td><td>6.84</td><td>6.70</td><td>11.00</td><td>6.41</td><td>5.97</td></tr><tr><td>20</td><td>22.43</td><td>7.47</td><td>20.68</td><td>7.53</td><td>16.78</td><td>7.16</td><td>9.99</td><td>22.02</td><td>9.21</td><td>8.58</td><td>9.60</td><td>5.98</td><td>9.83</td><td>5.64</td><td>9.01</td><td>8.61</td><td>6.49</td><td>12.62</td><td>6.30</td><td>8.93</td><td>6.82</td><td>6.42</td><td>8.86</td><td>6.51</td><td>9.95</td></tr></table>

<sup>al.</sup> <sup>/</sup> <sup>Decision</sup> <sup>Support</sup> <sup>Syste</sup>m<sub>s</sub> <sub>52</sub> <sub>(2012</sub>

<table><tr><td>Size</td><td>SVR</td><td>P-value</td><td>BPNN</td><td>P-value</td></tr><tr><td>5</td><td>2.20%</td><td>0.020</td><td>11.16%</td><td>0.010</td></tr><tr><td>10</td><td>2.12%</td><td>0.021</td><td>10.65%</td><td>0.281</td></tr><tr><td>15</td><td>2.54%</td><td>0.049</td><td>21.25%</td><td>0.008</td></tr><tr><td>20</td><td>2.69%</td><td>0.019</td><td>29.39%</td><td>0.011</td></tr><tr><td>25</td><td>3.38%</td><td>0.000</td><td>17.72%</td><td>0.074</td></tr></table>

<table><tr><td>Exact value</td><td>LR</td><td>Raw-SVR</td><td>Transform-SVR</td><td>Raw-BPNN</td><td>Transform-BPNN</td></tr><tr><td>9.27</td><td>9.701</td><td>9.635</td><td>9.763</td><td>9.603</td><td>9.53</td></tr><tr><td>9.34</td><td>9.877</td><td>9.417</td><td>9.551</td><td>9.464</td><td>9.344</td></tr><tr><td>9.38</td><td>10.001</td><td>9.784</td><td>9.743</td><td>10.407</td><td>9.748</td></tr><tr><td>9.43</td><td>9.851</td><td>9.852</td><td>9.751</td><td>9.773</td><td>9.438</td></tr><tr><td>9.5</td><td>9.544</td><td>9.663</td><td>9.576</td><td>10.475</td><td>9.737</td></tr><tr><td>9.52</td><td>9.972</td><td>9.942</td><td>9.681</td><td>9.923</td><td>9.62</td></tr><tr><td>9.58</td><td>9.8</td><td>9.657</td><td>9.713</td><td>9.697</td><td>9.674</td></tr><tr><td>9.6</td><td>9.665</td><td>9.648</td><td>9.611</td><td>9.314</td><td>9.655</td></tr><tr><td>9.64</td><td>9.81</td><td>9.643</td><td>9.864</td><td>9.633</td><td>9.755</td></tr><tr><td>9.67</td><td>9.87</td><td>10.111</td><td>9.722</td><td>10.462</td><td>10.141</td></tr><tr><td>9.77</td><td>9.418</td><td>9.679</td><td>9.655</td><td>9.278</td><td>9.376</td></tr><tr><td>9.8</td><td>9.727</td><td>9.648</td><td>9.545</td><td>9.433</td><td>9.615</td></tr><tr><td>9.87</td><td>9.509</td><td>9.793</td><td>9.887</td><td>9.949</td><td>10.124</td></tr><tr><td>9.88</td><td>9.677</td><td>9.688</td><td>9.84</td><td>9.858</td><td>10.081</td></tr><tr><td>9.93</td><td>9.756</td><td>9.782</td><td>9.822</td><td>9.734</td><td>10.344</td></tr><tr><td>9.95</td><td>9.589</td><td>9.728</td><td>9.719</td><td>9.621</td><td>9.703</td></tr><tr><td>9.96</td><td>9.603</td><td>9.793</td><td>9.791</td><td>9.828</td><td>9.746</td></tr><tr><td>9.97</td><td>9.736</td><td>9.732</td><td>9.727</td><td>10.24</td><td>9.71</td></tr><tr><td>10.2</td><td>9.415</td><td>9.731</td><td>9.698</td><td>9.513</td><td>9.648</td></tr><tr><td>Total error</td><td>6.061</td><td>4.178</td><td>3.725</td><td>6.981</td><td>4.433</td></tr><tr><td>MSE</td><td>0.3191</td><td>0.219</td><td>0.196</td><td>0.367</td><td>0.233</td></tr><tr><td>STD</td><td>0.371</td><td>0.138</td><td>0.097</td><td>0.359</td><td>0.258</td></tr></table>

<sup>nclusions</sup> <sub>and</sub> <sub>future</sub> <sub>s</sub>

<sup>presented</sup> <sup>a</sup> <sup>new</sup> <sub>method,</sub> <sub>structure-based</sub> <sup>to</sup> <sup>deal</sup> <sup>with</sup> <sup>small</sup> <sup>data</sup> <sup>s</sup><sub>et</sub> <sub>problems,</sub> <sub>which</sub> <sub>e</sub> <sup>er</sup> <sup>di</sup>m<sub>ensional</sub> <sub>space.</sub> <sub>Thefirst</sub> <sub>step</sub> <sub>is</sub> <sub>using</sub> <sub>D</sub> <sup>enerate</sup> <sup>k</sup> <sup>clusters,</sup> <sup>which</sup> <sup>is</sup> <sub>a</sub> <sub>dynamic</sub> <sub>value.</sub> <sup>o</sup>m<sub>pute</sub> <sub>the</sub> <sub>possibility</sub> <sub>values</sub> <sub>through</sub> <sub>the</sub> <sub>fuz</sub> <sup>on</sup> <sup>to</sup> <sup>build</sup> <sup>up</sup> <sup>the</sup> <sup>attribute</sup> <sup>transfor</sup>m<sub>atio</sub>

<sup>cases</sup> <sup>are</sup> <sup>used</sup> <sup>to</sup> <sup>verify</sup> <sup>the</sup> <sup>forecasting</sup> m<sub>od</sub> <sup>m</sup> <sub>with</sub> <sub>the</sub> <sub>LR,</sub> <sub>SVR,</sub> <sub>and</sub> <sub>BPNN</sub> <sub>approaches.</sub> <sub>In</sub> <sub>t</sub> <sup>esults</sup> <sup>show</sup> <sup>that</sup> <sup>each</sup> <sup>s</sup><sub>cale</sub> <sub>of</sub> <sub>resampling</sub> <sub>for</sub> <sup>rror</sup> <sup>improving</sup> <sup>rate</sup> <sup>h</sup>a<sub>s</sub> <sub>better</sub> <sub>performance</sub> <sup>d</sup> <sup>data.</sup> <sup>Cross-validatio</sup><sub>n</sub> <sub>and</sub> <sub>the</sub> <sub>data</sub> <sub>speci</sub> <sup>rate</sup> w<sub>ere</sub> <sub>selected</sub> <sub>to</sub> <sub>evaluate</sub> <sub>the</sub> <sub>results</sub> <sup>ll</sup> <sup>the</sup> <sup>forecasting</sup> <sup>mod</sup>e<sub>ls'</sub> <sub>MSE,</sub> <sub>total</sub> <sub>errors,</sub> <sub>a</sub> <sup>i</sup>m<sub>proved</sub> <sub>significantly</sub> <sub>using</sub> <sub>the</sub> <sub>proposed</sub> <sub>ap</sub> <sup>de</sup> <sup>that</sup> <sup>the</sup> <sup>structur</sup>e<sub>-based</sub> <sub>data</sub> <sub>sets</sub> <sub>are</sub> <sub>sup</sub> w <sub>data</sub> <sub>set</sub>

<sup>he</sup> <sup>result</sup> <sup>of</sup> <sup>thet-test</sup> <sup>in</sup> <sup>so</sup>m<sub>e</sub> <sub>sizes</sub> <sub>(case</sub> = <sub>10,</sub> <sub>25)</sub> <sub>showed</sub> <sub>no</sub> <sub>significant</sub> <sub>differences</sub> <sub>i</sub> <sup>d</sup> <sup>method</sup> <sup>can</sup> <sup>be</sup> <sup>combin</sup><sub>ed</sub> <sub>with</sub> <sub>virtual</sub> <sub>sampl</sub> <sup>the</sup> <sup>analysis</sup> <sup>perfor</sup>m<sub>ance</sub> <sub>in</sub> <sub>future</sub>

## References

[1] S. Ali, K.A. Smith-Miles, A meta-learning approach to automatic kernel selection for support vector machines, Neurocomputing 70 (1–3) (2006) 173–186.

[2] S. Amari, S. Wu, Improving support vector machine classi<sup>fi</sup>ers by modifying kernel functions, Neural Networks 12 (6) (1999) 783–789.

[3] M. Ankerst, M.M. Breunig, H.P. Kriegel, J. Sander, OPTICS: ordering points to identify the clustering structure, ACM SIGMOD'99, 28 (2), 1999, pp. 49–60.

[4] N. Aronsajn, Theory of reproducing kernels, Transactions of the American Mathematical Society 68 (1950) 337–404.

[5] C.M. Bishop, Pattern Recognition and Machine Learning, Springer, 2006.

[6] M.H. Chehreghani, H. Abolhassani, Density link-based methods for clustering web pages, Decision Support Systems 47 (4) (2009) 374–382

[7] P. Cortez, A. Cerdeira, F. Almeida, T. Matos, J. Reis, Modeling wine preferences by data mining from physicochemical properties, Decision Support Systems 47 (4) (2009) 547–553.

[8] M. Daszykowski, B. Walczak, D. Massart, Looking for natural patterns in data Part 1. Density-based approach, Chemometrics and Intelligent Laboratory Systems 56 (2) (2001) 83–92.

[9] E. Eryarsoy, G.J. Koehler, H. Aytug, Using domain-speci<sup>fi</sup>c knowledge in generalization error bounds for support vector machine learning, Decision Support Systems 46 (2) (2009) 481–491.

[10] M. Ester, H.P. Kriegel, J. Sander, X. Xu, A density-based algorithm for discovering clusters in large spatial databases with noise, KDD'96, 1996, pp. 226–231.

[11] C. Huang, C. Moraga, A diffusion-neural-network for learning from small samples, International Journal of Approximate Reasoning 35 (2) (2004) 137–161.

[12] H. Ince, T.B. Trafalis, A hybrid model for exchange rate prediction, Decision Support Systems 42 (2) (2006) 1054–1062.

[13] A.K. Jain, Data clustering: 50 years beyond K-means, Pattern Recognition Letters 31 (8) (2010) 651–666.

[14] S. Kumar, Neural Networks: A Classroom Approach, Tata McGraw-Hill Education, 2004.

[15] D.C. Li, Y.H. Fang, A non-linearly virtual sample generation technique using group discovery and parametric equations of hypersphere, Expert Systems with Applications 36 (1) (2009) 844–851.

[16] D.C. Li, L.S. Chen, Y.S. Lin, Using functional virtual population as assistance to learn scheduling knowledge in dynamic manufacturing environments, International Journal of Production Research 41 (17) (2003) 4011–4024.

[17] D.C. Li, C.S. Wu, T.I. Tsai, Y.S. Lina, Using mega-trend-diffusion and arti<sup>fi</sup>cial samples in small data set learning for early <sup>fl</sup>exible manufacturing system scheduling knowledge, Computers and Operations Research 34 (4) (2007) 966–982.

[18] D.C. Li, W.C. Chen, C.W. Liu, Y.S. Lin, A non-linear quality improvement model using SVR for manufacturing TFT-LCDs, Journal of Intelligent Manufacturing (2010), doi:10.1007/s10845-010-0440-1.

[19] D.C. Li, Y.H. Fang, Y. Fang, The data complexity index to construct an ef<sup>fi</sup>cient cross-validation method, Decision Support Systems 50 (1) (2010) 93–102.

[20] C.Y. Lin, C.C. Chang, C.C. Lin, A new density-based scheme for clustering based on genetic algorithm, Fundamenta Informaticae 68 (4) (2005) 315–331.

[21] P. Liu, D. Zhou, N. Wu, VDBSCAN: varied density based spatial clustering of applications with noise, Proceedings of IEEE International Conference on Service Systems and Service Management (2007) 1–4.

[22] C.J. Lu, T.S. Lee, C.C. Chiu, Financial time series forecasting using independent component analysis and support vector regression, Decision Support Systems 47 (2) (2009) 115–125.

[23] E. Marrocu, An investigation of the effects of data transformation on nonlinearity, Empirical Economics 31 (4) (2006) 801–820.

[24] Merriam-Webster, Cluster analysisAvailable, http://www.merriam-webster.com/ info/08words.htm 2008.

[25] D.C. Montgomery, Design and Analysis of Experiments, John Wiley, NJ USA, 2005.

[26] N. Khan, R. Ksantini, I. Ahmad, B. Boufama, A novel SVM+ NDA model for classi-<sup>fi</sup>cation with an application to face recognition. Pattern Recognition 45 (1) (2012) 66–79.

[27] P. Niyogi, F. Girosi, T. Poggio, Incorporating prior information in machine learning by creating virtual examples, Proceedings of the IEEE 86 (11) (1998) 2196–2209.

[28] D. Pascual, F. Pla, J. Sanchez, Non parametric local density-based clustering for multimodal overlapping distributions, Intelligent Data Engineering and Automated Learning 4224 (2006) 671–678.

[29] T. Pei, A. Jasra, D.J. Hand, A.X. Zhu, C. Zhou, DECODE: a new method for discovering clusters of different densities in spatial data, Data Mining and Knowledge Discovery 18 (3) (2009) 337–369.

[30] S. Roy, D. Bhattacharyya, An approach to <sup>fi</sup>nd embedded clusters using density based techniques, Distributed Computing and Internet Technology 3816 (2005) 523–535.

[31] A. Sanchez, V. David, Advanced support vector machines and kernel methods, Neurocomputing 55 (1–2) (2003) 5–20.

[32] S. Theodoridis, K. Koutroumbas, Pattern Recognition, Second edition, Elsevier Academic Press, 2003.

[33] T.I. Tsai, D.C. Li, Utilize bootstrap in small data set learning for pilot run modeling of manufacturing systems, Expert Systems with Applications 35 (3) (2008) 1293–1300.

[34] V. Vapnik, The Nature of Statistical Learning Theory, Springer, 1995.

[35] T. Yang, V. Kecman, Adaptive local hyperplane algorithm for learning small medical data sets, Expert Systems 26 (4) (2009) 355–359.

[36] I.C. Yeh, Exploring concrete slump model using arti<sup>fi</sup>cial neural networks, Journal of Computing in Civil Engineering 20 (3) (2006) 217–221.

[37] J. Yu, Y. Wang, Y. Shen, Noise reduction and edge detection via kernel anisotropic diffusion, Pattern Recognition Letters 29 (10) (2008) 1496–1503.

![](/api/attachments/Y45UQMC7/fulltext/images/377c632bbb2099cfa42d8b14136a56d9dbcef8c380bfc8ea8e690f7935c0f7c1.jpg)  
Der-Chiang Li is a Distinguished Professor in the Department of Industrial and Information Management, the National Cheng Kung University, Taiwan. He received his PhD degree at the Department of Industrial Engineering at Lamar University Beaumont, Texas, USA, in 1985. As a research professor, his current interest concentrates on learning with small data sets.

![](/api/attachments/Y45UQMC7/fulltext/images/56309809673c3a04996f90355b7218aa11bfd74080a424b60994bd526f5d9836.jpg)  
Chih-Chieh Chang is a PhD student at the Department of Industrial and Information Management, the National Cheng Kung University, Taiwan. He is also working at the laboratory for small sample learning.

![](/api/attachments/Y45UQMC7/fulltext/images/1af12626c6937a26d22a223d252e5ebc07046882c9e1cabe49a2158ec573d973.jpg)

Chiao-Wen Liu is a PhD student at the Department of Industrial and Information Management, the National Cheng Kung University, Taiwan. She is also working at the laboratory for small sample learning.
