---
otero_id: 11070
otero_key: "6SMV3KNB"
title: "A kernel entropy manifold learning approach for financial data analysis"
authors: "Yan Huang; Gang Kou"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2014.04.004"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A kernel entropy manifold learning approach for <sup>fi</sup>nancial data analysis<sup>☆</sup>

Yan Huang <sup>a</sup>, Gang Kou <sup>b,c,</sup>⁎

<sup>a</sup> School of Management and Economics, University of Electronic Science and Technology of China, Chengdu 610054, China

<sup>b</sup> School of Business Administration, Southwestern University of Finance and Economics, Chengdu, China

<sup>c</sup> Collaborative Innovation Center of Financial Security, Southwestern University of Finance and Economics, Chengdu, China

## a r t i c l e i n f o

Article history: Received 23 August 2013 Received in revised form 6 April 2014 Accepted 18 April 2014 Available online xxxx

Keywords: Manifold learning Financial analysis Low-dimensional embedding Information metric

## a b s t r a c t

Identi<sup>fi</sup>cation of intrinsic characteristics and structure of high-dimensional data is an important task for <sup>fi</sup>nancial analysis. This paper presents a kernel entropy manifold learning algorithm, which employs the information metric to measure the relationships between two <sup>fi</sup>nancial data points and yields a reasonable low-dimensional representation of high-dimensional <sup>fi</sup>nancial data. The proposed algorithm can also be used to describe the characteristics of a <sup>fi</sup>nancial system by deriving the dynamical properties of the original data space. The experiment shows that the proposed algorithm cannot only improve the accuracy of <sup>fi</sup>nancial early warning, but also provide objective criteria for explaining and predicting the stock market volatility.

© 2014 The Authors. Published by Elsevier B.V. This is an open access article under the CC BY license

(http://creativecommons.org/licenses/by/3.0/).

## 1. Introduction

Traditional <sup>fi</sup>nancial analysis methodologies include quantitative model and textual analysis. The quantitative model is the analysis about <sup>fi</sup>nancial data by the use of statistical analysis tools or arti<sup>fi</sup>cial intelligence technologies, which relies on the selection about basic important factors, such as <sup>fi</sup>nancial ratios, technical indexes, and macroeconomic indexes [1]. The textual analysis utilizes text mining techniques to analyze the context of <sup>fi</sup>nancial reports, which are dependent on the identi<sup>fi</sup>cation of a prede<sup>fi</sup>ned set of keywords [2]. Since different factors or keywords are selected for different studies, the results are often subjective.

The real <sup>fi</sup>nancial indicators are numerous while the complex high-dimensional data tends to obscure the essential feature of data [4]. Identifying intrinsic characteristics and structure of highdimensional data is important for <sup>fi</sup>nancial analysis. Inspired by the Quantitative Structure–Property Relationship (QSPR) method [3], whose core idea is that the microscopic structure of a material determines its macroscopic properties, this paper tries to <sup>fi</sup>nd the inherent relationships between data points of <sup>fi</sup>nancial dataset, and further derive the overall characteristics of the <sup>fi</sup>nancial system.

Manifold learning, which explores the inherent low-dimensional manifold structure of high-dimensional data, is a valid choice for this task. In the <sup>fi</sup>eld of <sup>fi</sup>nancial analysis, data information characteristics, i.e. probability distributions, are important. However, many existing manifold learning algorithms concern about space geometric characteristics [5–8]. When Probability Density Functions (PDFs) are constrained to form a sub-manifold of interest, the straight-shot distance is no longer an accurate description of the manifold distance [50]. For <sup>fi</sup>nancial data sets, each data point represents a listed company, while the distance between the data points indicates the degree of difference between the <sup>fi</sup>nancial positions of listed companies. If the difference was characterized only by the geometric space distance between data points, it may not only un<sup>fi</sup>t the practical signi<sup>fi</sup>cance of <sup>fi</sup>nancial analysis, but also cause problems in the subsequent analysis. Therefore, this study employs the information metric to measure the relationships between listed companies and obtains the relationship metric model.

Real-world <sup>fi</sup>nancial data is often nonlinear [10] and linear mapping manifold learning cannot fully capture the data information. Though Qiao et al. proposed a nonlinear mapping [11], the method is too complicated for the current problem. Kernel is often used to discover nonlinear structure in data [12,13]. The objective of this paper is to propose a kernel entropy manifold learning (KEML) algorithm to obtain the lowdimensional representation of high-dimensional <sup>fi</sup>nancial data from the perspective of manifold learning. The KEML algorithm is extended to a kernel feature space so that the low-dimensional embedding can re<sup>fl</sup>ect the characteristics of the original <sup>fi</sup>nancial data set. Experiments using small and medium-sized companies from China A-share Stock Market are designed to validate the proposed algorithm.

The rest of the paper is organized as follows: Section 2 reviews related works. Section 3 describes the modeling of <sup>fi</sup>nancial data manifold and the proposed algorithm. Section 4 reports the experimental study and the last section concludes the paper.

Y. Huang, G. Kou / Decision Support Systems xxx (2014) xxx–xxx

## 2. Literature review and preliminaries

## 2.1. Machine learning in financial analysis

Over the past few decades, machine learning algorithms have been widely used in the <sup>fi</sup>nancial <sup>fi</sup>eld and have been reported to be quite effective in some cases [14]. Machine learning quantitative models include single algorithms, such as ANN [15–17], SVM [18–20] and SOM [21,22], and hybrid techniques, which combine two or more algorithms. Many studies have been conducted to develop hybrid techniques for <sup>fi</sup>nancial analysis. Serrano-Cinca and Gutiérrez-Nieto [23] combined partial least square (PLS) regression model and principal component analysis (PCA) and multiple linear regression (MLR) for bankruptcy prediction. Yolcu et al. [24] used a hybrid arti<sup>fi</sup>cial neural network containing linear and nonlinear components for time series forecasting. Kao et al. [25] combined multivariate adaptive regression splines (MARS) and support vector regression (SVR) for stock index forecasting. Lu et al. [26] used independent component analysis (ICA) and support vector regression (SVR) in <sup>fi</sup>nancial time series forecasting.

Context-based text analysis had been used to analyze unstructured data in <sup>fi</sup>nancial reporting. Groth and Muntermann [27] and Chan and Franklin [2] and Humpherys et al. [28] adopted text mining technology to analyze the unstructured data of <sup>fi</sup>nancial reports to improve prediction accuracy of <sup>fi</sup>nancial risk. Schumaker and Chen [29] used textual representations of <sup>fi</sup>nancial news articles to estimate the discrete stock price. Olson et al. [30] compared data mining methods for bankruptcy prediction.

The <sup>fi</sup>nancial dataset can be considered as a system, in which each data point is an element. The intrinsic relationships between elements constitute the system structure, which determines the characteristics of the system. Inspired by the idea of QSPR, this study tried to explore the intrinsic structure of the system, and then discover the overall status of the system.

## 2.2. Manifold learning

A manifold is a topological space which is locally Euclidean. Highdimensional data observed in real world are often the consequences of a small number of factors [31]. Manifold learning algorithms assume that the input data resides on or close to a low-dimensional manifold embedded in the ambient space [32]. Thus it is possible to construct a mapping that obeys certain properties of the manifold and obtain low-dimensional representation of high-dimensional data with good preservation of the intrinsic structure in the data [32].

Currently dimension reduction techniques are mainly divided into two categories: linear and nonlinear methods. The most well known linear method is principal component analysis (PCA), which is based on correlation matrices [38]. PCA is a classical feature extraction and data representation technique widely used in pattern recognition and computer vision. Sirovich and Kirby utilized PCA to represent pictures of human faces [54]. Turk and Pentland presented the well-known Eigenfaces method for face recognition in 1991 [54]. Kernel PCA (KPCA), a kernel extension of PCA, is also a very in<sup>fl</sup>uential method. KPCA performs traditional PCA in a kernel feature space, which is nonlinearly related to the input space [38].

Compared with traditional dimension reduction approaches, manifold learning has advantages such as nonlinear nature, geometric intuition, and computational feasibility. Many manifold learning methods have been developed over the years. Isometric Feature Mapping (ISOMAP) [6] and Locally Linear Embedding (LLE) [7] are the earliest ones. The key idea of ISOMAP algorithm is to preserve the geodesic distance among points on the manifold and embed data into low-dimensional space by multidimensional scaling. LLE computes the reconstruction weights of each point and then minimizes the embedding cost by solving an eigenvalue problem to preserve the proximity relationship among data.

Local tangent space alignment (LTSA) constructs local linear approximations of the manifold in the form of a collection of overlapping approximate tangent spaces at each sample point, and then aligns those tangent spaces to obtain a global parameterization of the manifold [5]. LTSA maps the high dimensional data points on a manifold to points in a lower dimension Euclidean space. This mapping is isometric if the manifold is isometric to its parameter space [5]. Local Multidimensional Scaling (LMDS) is a data embedding method based on the alignment of overlapping locally scaled patches [8] and inputs are local distances. A subset of overlapping patches is chosen by a greedy approximation algorithm of minimum set cover. The patches are aligned to derive global coordinates and minimize a residual measure. LMDS is locally isometric and scales with the number of patches rather than the number of data points. LMDS produces less deformed embedding results than LLE [8].

These manifold learning algorithms use geodesic distance metric or weight measurement to calculate similarities between data points. In many problems of practical interest, however, the manifold geometry is unavailable and the calculation of geodesics must be done in a model-free, nonparametric fashion [34]. In applications like <sup>fi</sup>nancial analysis, for example, only considering the geometry structure of data space may miss some essential characteristics of data and destroy the proximity relations (topology) of the original data space [9].

## 2.3. Information distance metric

This study adopted an information theory-based metric to measure the difference between data points. Shannon suggested that “information entropy plays a central role in information theory as measures of information, choice, and uncertainty” [35]. Kolmogorov complexity [36] measures information content of an object. Bennett et al. [37] proposed the information distance theory and proved the fundamental universal theorem. Information distance measures the essential relationship between things. Due to its parameter-free, feature-free, and alignmentfree characteristics, it can be used to deal with unstructured and incomprehensible data. A distance is a function D with nonnegative real values, de<sup>fi</sup>ned on the Cartesian product X × X of a set X. It is called a metric on X if for every $x , y , z \in X ;$

$\cdot D ( x , y ) = 0$ iff x <sub>¼</sub> y <sub>ð</sub> <sub>Þ</sub> the identity axiom ;

$\cdot D ( x , y ) + D ( y , z ) \geq D ( x , z ) ($ the triangle inequality ;

$D ( x , y ) = D ( y$ ; x the symmetry axiom :

A set X provided with a metric is called a metric space. For example, every set X has the trivial discrete metric $D ( x , y ) = 0 { \mathrm { i f } } x = y$ and D(x, y) = 1 otherwise [37]. The information metric between stochastic sources X and Y is de<sup>fi</sup>ned as $D ( x , y ) = H ( x | y ) + H ( y | x ) [ 3 7 ] .$ . Here H(x|y) is used to measure the difference between probability distributions.

In recent years, entropy-based distance metric has been investigated by the manifold learning <sup>fi</sup>eld. Costa and Hero [33] proposed geodesicminimal-spanning-tree (GMST) method that jointly estimates both the intrinsic dimension and intrinsic entropy on the manifold. Jenssen [38] developed kernel entropy component analysis (KECA) for data transformation and dimensionality reduction. KECA reveals structure relating to the Renyi entropy of the input space data set. Carter et al. [34] proposed Fisher Information Nonparametric Embedding (FINE) which utilizes the properties of information geometry and statistical manifolds to de<sup>fi</sup>ne similarities between data sets using Fisher information distance. FINE showed that this metric can be approximated using nonparametric methods. Carter et al. [50] presented methods for

Please cite this article as: Y. Huang, G. Kou, A kernel entropy manifold learning approach for <sup>fi</sup>nancial data analysis, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.04.004

Y. Huang, G. Kou / Decision Support Systems xxx (2014) xxx–xxx

low-dimensional representation of information-geometric data and illustrated the methods in <sup>fl</sup>ow cytometry and demography analysis.

The proposed KEML algorithm is different from the above mentioned methods in the following ways: 1) each data point in a <sup>fi</sup>nancial data set is regarded as a subset of the probability distribution and all data points constitute a space of probability distributions. It seeks to discover a statistical manifold on a probability density space, while previous algorithms are based on the Euclidean vector space. 2) In the KEML algorithm, information divergence is used for measuring pairwise distance rather than Euclidean distance. 3) Though there are previous manifold learning algorithms using the Rényi entropy, the proposed algorithm utilizes it differently. For instance, Costa and Hero [33] employed the Rényi entropy of the sample points to measure the data compression on the manifold, while the proposed algorithm adopts the Rényi entropy to estimate the distance metric, which was the criteria for the topological relations in high-dimensional data. 4) The construction of the probability density space is different from previous statistical manifold learning algorithms. For example, the Information-Geometric Dimensionality Reduction (IGDR) algorithm proposed by Carter et al. [50] also used the Rényi entropy as the distance metric. However, each index is considered as a class label of a subset with N sample points in the IGDR. Thus the original dataset is divided into d subsets and d is the number of indicators. While in the proposed algorithm, each point x is considered as a set, in which each feature index is a sample. The original dataset was divided into N subsets.

## 2.4. Manifold and dynamical property

In 1930s, Whitney proposed the embedding theorem which an m-dimensional manifold can be realized in a Euclidean space of dimension 2m + 1. A potentially low-dimensional copy of the manifold can be recovered and a bijection exists between the original and its copy [52]. Based on Whitney's theorem, Takens provided a theoretical foundation for the reconstruction of an m-dimensional manifold when only a scalar time series is observable [52]. Li et al. [53] proved that high-dimensional time series can be parsimoniously represented by a dynamical process de<sup>fi</sup>ned on a low-dimensional manifold.

The dynamical model parameters can be learned in the dimensionality-reduced state space [53]. The statistical quantities that characterize the properties of a dynamical system can be obtained through the parameters. Kolmogorov entropy (K entropy), a quantitative measure of uncertainty, is used to describe the degree of system movement disorder or random [47]. The larger the K value, the greater the information loss and the greater the degree of chaos. For random behaviors, K entropy is unbounded when the information is completely lost. For regular motions, K entropy should be zero when no information is generated. For a low-dimensional chaotic dynamics system, K entropy is a <sup>fi</sup>nite value greater than zero [47].

In this paper, each data set is treated as a dynamical system and the low-dimensional embedding of a dynamical system can be learned through the proposed algorithm. Then the statistical quantity, such as K entropy, can be derived from the low-dimensional embedding to characterize the properties of the dynamical system.

## 3. Kernel entropy manifold learning algorithm for <sup>fi</sup>nancial data

## 3.1. Manifold of financial data

The objects in this study are n listed companies $( X _ { 1 } , X _ { 2 } , . . . , X _ { n } )$ , each X has D <sup>fi</sup>nancial indicators $( X _ { i } ^ { 1 } , X _ { i } ^ { 2 } , . . . , X _ { i } ^ { D } )$ . Each company X is a data set consisting of <sup>fi</sup>nancial indicators, which is $X _ { i } = ( X _ { i } ^ { 1 } , X _ { i } ^ { 2 } , . . . , X _ { i } ^ { D } ) . \chi$ is a family of data sets $\chi = \{ X _ { 1 } , . . . , X _ { i } , . . . , X _ { n } \} ( i = 1 , . . . , n )$ , where $X _ { i } = ( X _ { i } ^ { 1 } , X _ { i } ^ { 2 }$ $. . . , X _ { i } ^ { D } ]$ . Assume that each data set X has an underlying probability distribution function p determined by D <sup>fi</sup>nancial indicators and the parameters are unknown. Then, we can get a collection of Probability Density Functions (PDFs) $P = \{ p _ { 1 } , . . . , p _ { n } \}$ which lie on a statistical manifold π. In the statistical manifold π, each element is a probability distribution p . We try to reconstruct π in the space of probability densities using available information in P. That is to <sup>fi</sup>nd an embedding $A : p ( x )  y ,$ where $y \in \mathbb { R } ^ { m } , m < D$ . Different from the traditional manifold learning algorithm in Euclidean space, the proposed algorithm is to discover a low-dimensional embedding in the density space, i.e. a statistical manifold of probability distributions.

## 3.2. Information distance metric for financial data points

To obtain the low-dimensional embedding from the high-dimensional data sets, pairwise sample distance which measures the amount of information change between data points should be preserved. There is the corresponding Kullback–Leibler divergence KL(P,Q) [50] between any two probability distributions P and Q, where $K L ( P , Q ) = E { \Big [ } { \log } { \frac { f ( x ) } { g ( x ) } } { \Big ] } = \int f ( x ) \log { \frac { f ( x ) } { g ( x ) } } d x , P$ and Q are described by the density function f(x) and $g ( x )$ , respectively. Divergence is an approximate distance function, which meets the non-negative distance de<sup>fi</sup>nition, but does not satisfy the symmetry and triangle inequality. The Renyi quadratic entropy is $h ( p ) = - \log \int p ^ { 2 } ( x ) d x ,$ where p(x) is the probability density function generating the data set, or sample $X = x _ { 1 } , x _ { 2 } , . . . , x _ { N } [ 3 8 ]$ . Since the logarithm is a monotonic function, we may concentrate on the quantity $V ( p ) = \int p ^ { 2 } ( x ) d x$ . Alternatively, the formula may be formulated as $V ( p ) = \varepsilon _ { p } ( p )$ , where $\varepsilon _ { p } ( \mathfrak { g } )$ denotes expectation with regard to the density p(x).

To estimate $V ( p )$ and $h ( p )$ , the kernel estimation, given by $\hat { p ( x ) } \infty \frac { 1 } { N } \sum _ { i = 1 } ^ { N } k ( x - x _ { i } , \sigma ) \left[ 3 9 \right]$ , where $k ( x - x _ { i } , \sigma ) = \exp ( - | | x - x _ { i } | | ^ { 2 } / \sigma ^ { 2 } )$ , is introduced. The non-parametric estimation of Renyi entropy is:

$$
\begin{array}{l} \hat {h} (p) = - \log \left(\int p ^ {2} (\hat {x}) d x\right) \\ \qquad = - \log \left(\frac {1}{N ^ {2}} \sum_ {i = 1} ^ {N} \sum_ {j = 1} ^ {N} \int k (x - x _ {i}, \sigma) k \Big (x - x _ {j}, \sigma \Big) d x\right) \\ \qquad = - \log \left(\frac {1}{N ^ {2}} \sum_ {i = 1} ^ {N} \sum_ {j = 1} ^ {N} k \Big (x _ {i} - x _ {j}, \sqrt {2} \sigma \Big)\right). \end{array}\tag{1}
$$

Please cite this article as: Y. Huang, G. Kou, A kernel entropy manifold learning approach for <sup>fi</sup>nancial data analysis, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.04.004

Formula (1) indicates that the Renyi second order entropy can be decided by the Mahalanobis distance between any two samples in a collection For n listed companies, each company has D <sup>fi</sup>nancial indicators. The following information metric model can be formulated: Suppose $P _ { i } = ( p _ { i } ^ { 1 } , p _ { i } ^ { 2 } , . . . , p _ { i } ^ { D } ) , ( i = 1 , 2 , . . . , n )$ is the probability distribution vector of the i-th listed company <sup>fi</sup>nancial indicators, i.e.,

$$
p _ {i} ^ {j} \geq 0, \sum_ {j = 1} ^ {D} p _ {i} ^ {j} = 1, (i = 1, 2,..., n).\tag{2}
$$

The information metric between any two companies named Renyi divergence:

$$
h \left(P _ {i}, P _ {j}\right) = \sum_ {m = 1} ^ {D} p _ {i} ^ {m} \log \frac {p _ {i} ^ {m}}{p _ {j} ^ {m}}.\tag{3}
$$

Since $h ( P _ { i } , P _ { j } ) \neq h ( P _ { j } , P _ { i } )$ , the cross entropy does not satisfy the symmetry and can be transformed using the following formula:

Let

$$
\begin{array}{l} h \Big (P _ {i}, P _ {j} \Big) = h \Big (P _ {i}, P _ {j} \Big) + h \Big (P _ {j}, P _ {i} \Big) = \sum_ {m = 1} ^ {D} p _ {i} ^ {m} \log \frac {p _ {i} ^ {m}}{p _ {j} ^ {m}} + \sum_ {m = 1} ^ {D} p _ {j} ^ {m} \log \frac {p _ {j} ^ {m}}{p _ {i} ^ {m}} \\ = \sum_ {m = 1} ^ {D} p _ {i} ^ {m} \log p _ {i} ^ {m} + \sum_ {m = 1} ^ {D} p _ {j} ^ {m} \log p _ {j} ^ {m} - \sum_ {m = 1} ^ {D} p _ {i} ^ {m} \log p _ {j} ^ {m} - \sum_ {m = 1} ^ {D} p _ {j} ^ {m} \log p _ {i} ^ {m}. \end{array}\tag{4}
$$

$p _ { i }$ and $p _ { j }$ can be obtained from the above kernel density estimation.

## 3.3. Information distance metric in kernel space

Real world <sup>fi</sup>nancial data sets are nonlinear. This study proposes a kernel extension of the metric to tackle the nonlinear problem. For a given data $\mathsf { s e t } X _ { 1 } , X _ { 2 } , . . . , X _ { n } \in \boldsymbol { R } ^ { D }$ with a positive de<sup>fi</sup>nite mercer kerne $\Theta \overset { \cdot } { : } R ^ { D } \times R ^ { D } \to R$ , there exists a unique Reproducing Kernel Hilbert Space (RKHS) Ω of real valued functions on $R ^ { D }$ Let $\bar { \boldsymbol { \phi } } : \boldsymbol { R } ^ { D }  \Omega$ be a feature map from the input space $R ^ { D }$ to Ω, and $\varTheta _ { i j } = \theta ( X _ { i } , X _ { j } ) = \langle \phi ( X _ { i } ) , \phi ( X _ { j } ) \rangle = \phi ( X _ { i } ) ^ { T } \phi ( X _ { j } )$ . Let ϕ(X) denotes the data matrix in RKHS, such that $\phi ( X ) = ( \phi ( x _ { 1 } ) , . . . , \phi ( x _ { n } ) )$ ). The Euclidean distance between ϕ(X ) and ϕ(X ) in the feature space is

$$
\left\| \phi (X _ {i}) - \phi (X _ {j}) \right\| = \sqrt {\theta_ {i i} + \theta_ {j j} - 2 \theta_ {i j}}.
$$

Then, in the feature space, the estimated probability density function is

$$
\stackrel {\wedge} {p (x)} \propto \frac {1}{N} \sum_ {i = 1} ^ {N} k (\phi (x) - \phi (x _ {i}), \sigma),\tag{5}
$$

where

$$
k (\phi (x) - \phi (x _ {i}), \sigma) = \exp \left(- \| \phi (x) - \phi (x _ {i}) \| ^ {2} / \sigma^ {2}\right) = \exp \left(- (\theta_ {\cdot \cdot} + \theta_ {i i} - 2 \theta_ {\cdot i}) / \sigma^ {2}\right).\tag{6}
$$

Substitute Eq. (6) with Eq. (5), Eq. (5) can be reformulated as;

$$
\hat {p (x)} \propto \frac {1}{N} \sum_ {i = 1} ^ {N} \exp \left(- (\theta_ {\cdot .} + \theta_ {i i} - 2 \theta_ {. i}) / \sigma^ {2}\right),\tag{7}
$$

and formula $( 7 )$ can be substituted with Eq. (4). Suppose $P _ { i } = ( p _ { i } ^ { 1 } , p _ { i } ^ { 2 } , . . . , p _ { i } ^ { D } ) , ( i = 1 , 2 , . . . , n )$ ) is the probability distribution vector of the ith-listed company <sup>fi</sup>nancial indicators, i.e.,

$$
p _ {i} ^ {j} \geq 0, \sum_ {j = 1} ^ {D} p _ {i} ^ {j} = 1, (i = 1, 2,..., n)\tag{8}
$$

h(P<sub>i</sub>,P<sub>j</sub>) becomes

$$
\begin{array}{l} h \Big (P _ {i}, P _ {j} \Big) = \frac {1}{N} \sum_ {m = 1} ^ {D} \sum_ {n = 1} ^ {N} \left[ \exp (- (\theta_ {i i} ^ {m m} + \theta_ {i i} ^ {n n} - 2 \theta_ {i i} ^ {m n}) / \sigma^ {2}) \log \left(\frac {1}{N} \sum_ {n = 1} ^ {N} \exp (- (\theta_ {i i} ^ {m m} + \theta_ {i i} ^ {n n} - 2 \theta_ {i i} ^ {m n}) / \sigma^ {2}\right) \right] \\ \quad + \frac {1}{N} \sum_ {m = 1} ^ {D} \sum_ {n = 1} ^ {N} \left[ \exp (- (\theta_ {j j} ^ {m m} + \theta_ {j j} ^ {n n} - 2 \theta_ {j j} ^ {m n}) / \sigma^ {2}) \log \left(\frac {1}{N} \sum_ {n = 1} ^ {N} \exp (- (\theta_ {j j} ^ {m m} + \theta_ {j j} ^ {n n} - 2 \theta_ {j j} ^ {m n}) / \sigma^ {2})\right) \right] \\ \quad - \frac {1}{N} \sum_ {m = 1} ^ {D} \sum_ {n = 1} ^ {N} \left[ \exp (- (\theta_ {i i} ^ {m m} + \theta_ {i i} ^ {n n} - 2 \theta_ {i i} ^ {m n}) / \sigma^ {2}) \log \left(\frac {1}{N} \sum _ {n = 1} ^ {N} \exp (- (\theta_ {j j} ^ {m m} + \theta_ {j j} ^ {n n} - 2 \theta_ {j j} ^ {m n}) / \sigma^ {2})\right) \right] \\ \quad - \frac {1}{N} \sum_ {m = 1} ^ {D} \sum_ {n = 1}^{N} \left[ \exp (- (\theta_ {j j} ^ {m m} + \theta_ {j j} ^ {n n} - 2 \theta_ {j j} ^ {m n}) / \sigma^ {2}) \log \left(\frac {1}{N} \sum_ {n = 1} ^ {N} \exp (- (\theta_ {i i} ^ {m m} + \theta_ {i i} ^ {n n} - 2 \theta_ {i i} ^ {m n}) / \sigma^ {2})\right) \right]. \end{array}\tag{9}
$$

Please cite this article as: Y. Huang, G. Kou, A kernel entropy manifold learning approach for <sup>fi</sup>nancial data analysis, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.04.004

Y. Huang, G. Kou / Decision Support Systems xxx (2014) xxx–xxx

## 3.4. Low-embedding manifold of financial data

In LLE, the local linear structure between the neighbors remains unchanged after dimensionality reduction. For <sup>fi</sup>nancial data points, the concept and scope of neighbors can be extended. Different from image data sets, adjacency relationships of <sup>fi</sup>nancial data do not wholly depend on geometric relationships of data points. As stated in Section 3.3, the original data set can be mapped into the linear RKHS by the kernel function. Assume that every data point and its neighborhood data points are located on the same linear manifold. When reproducing low-dimensional manifold, the corresponding data points in the intrinsic low-dimensional space maintain the same global neighbor relationship. To obtain the low-dimensional rep resentation of data sets. KEML algorithm constructs extended local linear structure and preserves the global topological characteristics in the inherent low-dimensional manifold. As mentioned above, the relationship metric $h _ { i j } = h ( P _ { i } , P _ { j } )$ re<sup>fl</sup>ects the essential relationships between the <sup>fi</sup>nancial data points. $h _ { 1 1 }$ represented the information distance of data point 1 with itself, $h _ { 1 2 }$ represented the information distance between data point 1 and data point 2 and so on. Therefore, we can further obtain the global relationship metric matrix $H = \left( \begin{array} { c c c c } { h _ { 1 1 } } & { h _ { 1 2 } } & { . . . } & { h _ { 1 n } } \\ { . . . } & { . . . } & { . . . } & { . . . } \\ { h _ { i 1 } } & { h _ { i 2 } } & { . . . } & { h _ { i n } } \\ { h _ { n 1 } } & { h _ { n 2 } } & { . . . } & { h _ { n n } } \end{array} \right)$ , which is the reconstruction

weight matrix and may be mapped to low-dimensional embedding manifold. The low-dimensional embedding Y re<sup>fl</sup>ects the corresponding reconstruction weight relationship of the sample points in the high-dimensional input space. Similar to the LLE method, we obtain the low-dimensiona embedding by solving the following optimization problem:

$$
\text { Min } \quad \Phi (Y) = \sum_ {i = 1} ^ {n} \left\| Y _ {i} - \sum_ {j = 1} ^ {n} h _ {i j} Y _ {j} \right\| ^ {2}.\tag{10}
$$

To eliminate the coordinates translation, rotation, and scaling factor of the low-dimensional embedding, two constraints are added: $( 1 ) \sum _ { i = 1 } ^ { N } Y _ { i } = 0 ,$ $\left( 2 \right) \frac { 1 } { N - 1 } \sum _ { i = 1 } ^ { N } Y _ { i } Y _ { i } ^ { T } = I .$ Furthermore, Eq. (10) can be written as $\varPhi ( Y ) = \sum _ { i = 1 } ^ { n } \left\| Y _ { i } { - } \sum _ { j = 1 } ^ { n } h _ { i j } Y _ { j } \right\| ^ { 2 } = \left\| \left( I { - } H \right) ^ { T } Y ^ { T } \right\| ^ { 2 } = t r { \Bigl ( } Y M Y ^ { T } { \Bigr ) }$ , where $M = ( I - H ) ^ { T } ( I - H )$ is a n × n matrix. In order to minimize the cost function, the low dimensional embedding Y should be taken as the corresponding eigenvectors $\nu _ { 1 } , . . . , \nu _ { d + 1 } \mathrm { t } 0$ the smallest $d + 1$ eigenvalues of the matrix M, that is $Y = [ \nu _ { 2 } , \cdots , \nu _ { d + 1 } ]$ , and d is determined by Renyi information dimension [51]. Information dimen sion was de<sup>fi</sup>ned as follows:

$$
d = - \lim _ {\varepsilon \rightarrow 0} \frac {\sum_ {i = 1} ^ {N} P _ {i} \log P _ {i}}{\log \varepsilon}
$$

where P represented the probability of a point falling into the i-th unit, and here, it denoted the probability distribution of the i-th company which has been obtained above, ε was the standard body, and N was the number of points. Thus, we can get the intrinsic dimension by information dimension d.

## 3.5. Computational complexity of KEML

In KEML, the reconstruction weight matrix adopts information matrix H, which re<sup>fl</sup>ects the essential relationships between the <sup>fi</sup>nancial data points. As a bridge between high-dimensional observation space and low dimensional embedding space, the matrix H makes the low-dimensional embedding space maintains the original topological relations. KEML algorithm has the global optimal solution, without iteration. The computational complexity of KEML is dominated by three parts: N data points were projected into kernel space by use of kernel function, which the computational complexity was $O ( N ^ { 2 } ) ;$ ; calculated the information distance between the data points in kernel space, which the computational complexity is $O ( N ( N -$ 1)); calculated the low-dimensional embedding through the relationship distance matrix H, which the computational complexity is $O ( N ^ { 2 } )$

## 3.6. KEML algorithm

The proposed KEML algorithm is summarized as follows (Table 1):

Step 1 Construct the relationship measure matrix H

Let Θ be the $N \times N$ kernel matrix with its (i, j) th entry $\theta _ { i j } = \phi ( x _ { i } ) ^ { T } \phi ( x _ { j } ) = \phi ( x _ { i } , x _ { j } )$ . ϕ is a data-independent kernel associated with the kernel matrix Θ. In the KEML algorithm, the Gaussian kernel was adopted for all the kernel-based methods. Compute the relationship model $h _ { i j } ,$ which builds the relationships between <sup>fi</sup>nancial data points, and then get the relationship matrix H.

Step 2 Calculate the low-dimensional embedding

Compute the eigenvalues of matrix $( I - H ) ( I - H ) ^ { T }$ and the corresponding eigenvector Y. Step 3 Select data

Select the smallest d non-zero eigenvalues and the corresponding eigenvector Y.

Table 1

Algorithm of manifold learning for <sup>fi</sup>nancial data (KEML).

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Input: data set X, Gaussian kernel and parameter  $\sigma$ ;
Output: low-dimensional coordinates Y.
Procedure
1. Construct the kernel matrix  $\Theta$  with the Gaussian kernel.
2. Compute  $h_{ij}$  by Eq. (9) and obtain the matrix H.
3. Compute the smallest d non-zero eigenvalues of matrix  $(I - H)(I - H)^{T}$  and the corresponding eigenvectors Y.
</div>

Please cite this article as: Y. Huang, G. Kou, A kernel entropy manifold learning approach for <sup>fi</sup>nancial data analysis, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.04.004

Y. Huang, G. Kou / Decision Support Systems xxx (2014) xxx–xxx

## 3.7. Dynamical property derived from KEML

The KEML algorithm produces d-dimensional manifold M from the original data set $X _ { 1 } , X _ { 2 } , . . . , X _ { n } \in R ^ { D } . \left( R , \rho \right)$ is the original space and $( M , \rho _ { 1 } )$ is ddimensional space, where ρ and $\rho _ { 1 }$ represent respectively the corresponding space mapping. As known from the preceding analysis, the mapping Φ : $R \to M$ meets: (1) Φ is subjective; $( 2 ) \forall x , y \in R , \rho ( x , y ) = \rho _ { 1 } ( \phi ( x ) , \phi ( y ) )$ is true. Assume $( R , \rho )$ and $( M , \rho _ { 1 } )$ are isometrically isomorphic. According to Whitney's theorem [48], $( M , \rho _ { 1 } )$ can be embedded in $( R , \rho ) . ( M , \rho _ { 1 } )$ is regarded as the reconstructed space of the system S. Since $( R , \rho )$ and $( M , \rho _ { 1 } )$ are isometrically isomorphic, the evolving trajectory of S in the reconstructed space M is diffeomorphism in the original space R. That is, we can restore the original dynamics of the system in the sense of topologically equivalent to maintain its chaotic characteristics, such as the Kolmogorov entropy [47]. Assuming the d-dimensional reconstructed space attractor track $X ( t ) , P ( i _ { 1 } , i _ { 2 } , . . . , i _ { n } )$ is the joint probability when $X ( t = \tau )$ in the box $i _ { 1 } , X ( t = 2 \tau )$ in the box $i _ { 2 } , \ldots ,$ , and $X ( t = n \tau )$ in the box $i _ { n } ,$ then K entropy is de<sup>fi</sup>ned as

$$
K = - \lim _ {\tau \to 0} \lim _ {\varepsilon \to 0} \lim _ {n \to} \frac {1}{n \tau} \sum_ {i _ {1}, i _ {2}, \ldots , i _ {n}} P (i _ {1}, i _ {2}, \ldots , i _ {n}) \log P (i _ {1}, i _ {2}, \ldots , i _ {n}) = \lim _ {\tau \to 0} \lim _ {l \to 0} \lim _ {n \to \infty} \frac {1}{n \tau} \sum \bigl (K _ {n + 1} - K _ {n} \bigr).
$$

$K _ { n + 1 } - K _ { n }$ measures the information loss of the system from time n to time $n = 1 .$ . K entropy de<sup>fi</sup>nes the average loss rate of the system. In the KEML algorithm, we obtain the statistical manifold $\pi = \{ p ( x ; \theta ) | \theta \in \mathbb { R } ^ { m } \}$ of n companies, the joint probability $P _ { i } = ( p _ { i } ^ { \bar { 1 } } , p _ { i } ^ { 2 } , . . . , p _ { i } ^ { D } )$ ) of the i-th company, and the information distance $h _ { i j } = h ( P _ { i } , P _ { j } )$ between any two companies. If each company in the data set is taken as an independent subsystem, we can measure $K _ { n + 1 } - K _ { n }  { \mathrm { b y } } h _ { i j } ,$ , and then K entropy of any company can be obtained as $K _ { i \cdot }$ Furthermore, we can get the K entropy of the system S.

## 4. Empirical study

In this section, three experiments are conducted to validate the proposed KEML algorithm using data from China A-share Stock Market. All algorithms are implemented in MATLAB 2010Rb.

## 4.1. Data sets

The 2006–2010 annual <sup>fi</sup>nancial data of small and medium-sized companies (a total of 205) from China A-share Stock Market were chosen from Wind Information Database for the experiment. Twenty-seven <sup>fi</sup>nancial indicators were selected to re<sup>fl</sup>ect six aspects of the companies' <sup>fi</sup>nancial positions [40] (Table 2).

According to [40], the following relationships between <sup>fi</sup>nancial indicators can be expected. First, there is a positive correlation between solvency and cash <sup>fl</sup>ow. It indicates that when cash <sup>fl</sup>ows of a listed company are less than adequate, its debt levels are high. Second, there

## Table 2

Financial indicators of listed company.

<table><tr><td>Types of indicators</td><td>Variable</td><td>Name of index</td></tr><tr><td rowspan="5">Solvency</td><td> $X_1$ </td><td>Current ratio</td></tr><tr><td> $X_2$ </td><td>Quick ratio</td></tr><tr><td> $X_3$ </td><td>Interest coverage ratio</td></tr><tr><td> $X_4$ </td><td>Interest bearing debt ratio</td></tr><tr><td> $X_5$ </td><td>Account payable turnover ratio</td></tr><tr><td rowspan="6">Operating capacity</td><td> $X_6$ </td><td>Inventory turnover ratio</td></tr><tr><td> $X_7$ </td><td>Accounts receivable turnover ratio</td></tr><tr><td> $X_8$ </td><td>Current asset turnover ratio</td></tr><tr><td> $X_9$ </td><td>Fixed asset turnover ratio</td></tr><tr><td> $X_{10}$ </td><td>Total asset turnover ratio</td></tr><tr><td> $X_{11}$ </td><td>Nonperforming asset ratio</td></tr><tr><td rowspan="5">Profitability</td><td> $X_{12}$ </td><td>Operating margin</td></tr><tr><td> $X_{13}$ </td><td>Return on equity</td></tr><tr><td> $X_{14}$ </td><td>Return on total assets</td></tr><tr><td> $X_{15}$ </td><td>Gross margin</td></tr><tr><td> $X_{16}$ </td><td>Net margin</td></tr><tr><td rowspan="4">Ability to grow</td><td> $X_{17}$ </td><td>Operating income ratio</td></tr><tr><td> $X_{18}$ </td><td>Net profit ratio</td></tr><tr><td> $X_{19}$ </td><td>Net assets growth ratio</td></tr><tr><td> $X_{20}$ </td><td>Net profit ratio (deducting non-recurring gains and losses)</td></tr><tr><td rowspan="4">Cash flow ratio</td><td> $X_{21}$ </td><td>Net cash flow ratio</td></tr><tr><td> $X_{22}$ </td><td>Cash ratio</td></tr><tr><td> $X_{23}$ </td><td>Cash-to-current-liabilities ratio</td></tr><tr><td> $X_{24}$ </td><td>Cash debt ratio</td></tr><tr><td rowspan="3">Capital structure</td><td> $X_{25}$ </td><td>Equity ratio</td></tr><tr><td> $X_{26}$ </td><td>Fixed asset ratio</td></tr><tr><td> $X_{27}$ </td><td>Debt asset ratio</td></tr></table>

are positive correlations between operating capacity, pro<sup>fi</sup>tability and ability to grow. Especially, there exists a signi<sup>fi</sup>cant positive correlation between pro<sup>fi</sup>tability and ability to grow, indicating that the growth rate of a listed company is consistent with its ability to generate earnings. Third, there exist signi<sup>fi</sup>cant negative correlations between cash <sup>fl</sup>ow and operating capacity, pro<sup>fi</sup>tability, and ability to grow. This suggests that when a listed company pursues an increase in net cash <sup>fl</sup>ow, its pro<sup>fi</sup>tability, growth rate and operational turnaround situation will be negatively affected. Fourth, solvency is negatively correlated to operational index, pro<sup>fi</sup>tability, and ability to grow.

## 4.2. Experimental settings

## The experiments are conducted as follows:

First, the KEML are compared with six dimensionality reduction methods: KPCA, LTSA, LMDS, ISOMAP, LLE, and PCA. The quantitative indicator Procrustes Measure (PM) is used to measure the resulting low-dimensional embeddings. As a quantitative indicator, PM is a nonlinear measurement of goodness [42–44] and a smaller PM value indicates a more accurate embedding [42]. MATLAB provides a PM function to compute the corresponding PM values.

Second, the resulting low-dimensional embeddings in the <sup>fi</sup>rst experiment are applied to provide early <sup>fi</sup>nancial warnings. K-means clustering method is used to divide the low-dimensional embedding into two clusters to identify abnormal companies. The clustering results were examined respectively using $F _ { 1 } -$ scores and risk expectation.

Third, the KEML algorithm is used to analyze the overall running characteristics of the stock market. As <sup>fi</sup>nancial markets can be viewed as a highly complex evolving system [41], the experimental data constitutes a subsystem of the complex system. KEML explores the subsystem geometric space, which makes it possible to further use the relevant analytical tools to study the running characteristics of the system.

## 4.3. Experimental results

## 4.3.1. Low-dimensional embedding results

The low-dimensional embeddings of the high-dimensional <sup>fi</sup>nancial data sets were obtained through different methods. In the experiment, the essential parameter is the bandwidth selection of Kernel Density Estimation. According to the existing literature, we <sup>fi</sup>rst set $\sigma = \{ 0 . 1 , . . . . . . ,$ 100} with the step length of 10 and calculate the value of PM in each situation. After a series of PM values were generated, the smallest one is selected and the corresponding σ is obtained. Similarly, the

Please cite this article as: Y. Huang, G. Kou, A kernel entropy manifold learning approach for <sup>fi</sup>nancial data analysis, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.04.004

a)  
![](/api/attachments/6SMV3KNB/fulltext/images/c86b757abf6dd6173bbe4cace91294117e2b6962a06907a42d827be8efcac070.jpg)  
Fig. 1. (a) Three-dimensional embedding results by KEML on the <sup>fi</sup>ve data sets. (b) Three-dimensional embedding results of the comparative experiments.

Table 3  
PM values of data sets in Fig. 1.

<table><tr><td>Dataset</td><td>KEML</td><td>KPCA</td><td>LTSA</td><td>LMDS</td><td>ISOMAP</td><td>LLE</td><td>PCA</td></tr><tr><td>2006 dataset</td><td>0.0013</td><td>0.0065</td><td>0.0058</td><td>0.0041</td><td>0.0078</td><td>0.0102</td><td>0.0074</td></tr><tr><td>2007 dataset</td><td>0.0027</td><td>0.0051</td><td>0.0043</td><td>0.0049</td><td>0.0069</td><td>0.0425</td><td>0.0059</td></tr><tr><td>2008 dataset</td><td>0.0021</td><td>0.0079</td><td>0.0056</td><td>0.0063</td><td>0.0096</td><td>0.0164</td><td>0.0085</td></tr><tr><td>2009 dataset</td><td>0.0042</td><td>0.0098</td><td>0.0064</td><td>0.0078</td><td>0.0115</td><td>0.0652</td><td>0.0106</td></tr><tr><td>2010 dataset</td><td>0.0009</td><td>0.0013</td><td>0.0011</td><td>0.0012</td><td>0.0087</td><td>0.0306</td><td>0.0015</td></tr></table>

corresponding optimal parameters were selected for the other six methods in the experiment respectively.

Fig. 1(a) shows the three-dimensional embedding results of KEML on the <sup>fi</sup>ve data sets and Fig. 1(b) summarizes the comparative results. The corresponding PM values of low-dimensional embeddings are illustrated in Table 3.

It can be seen that KEML achieves the best results on all the <sup>fi</sup>ve data sets. The other methods used Euclidean distances between sample points to drive the dimensionality-reduction algorithm [50], so their performances are unsatisfactory for the <sup>fi</sup>nancial area problems. One interesting observation is that the linear PCA outperforms ISOMAP and LLE on the selected <sup>fi</sup>nancial data sets. PCA adopts the relative Euclidean distance as distance metric, compared to the geodesic distance or spatial location, which is closer to the meanings of logic relationship. When Probability Density Functions (PDFs) are constrained to form a sub-manifold of interest, and the true geodesic distance is no longer an accurate description of the manifold distance [50]. In this scenario, PCA may produce better performance than some non-linear manifold learning methods. But in general, nonlinear manifold learning methods produce better results than PCA in the experiment.

To statistically validate the results, a statistical test is conducted. Let $x = { \mathrm { K E M L } } y _ { 1 } = { \mathrm { K P C A } } y _ { 2 } = \operatorname { L T S A } y _ { 3 } = \operatorname { L M D S } y _ { 4 } = \operatorname { I S O M A P } y _ { 5 } = \operatorname { L L E } y _ { 6 } = \operatorname { L A E } y _ { 7 }$ PCA, thus we got six pairwise independent observed results: $( x , y _ { 1 } )$ $( x , y _ { 2 } ) , ( x , y _ { 3 } ) , ( x , y _ { 4 } ) , ( x , y _ { 5 } ) , ( x , y _ { 6 } )$ . Let $D _ { i } = x - y _ { i } , ( i = 1 , . . . , 6 )$ then $D _ { 1 } , D _ { 2 } , . . . , D _ { 6 }$ were independent to each other. Since $D _ { 1 } , D _ { 2 } , . . . , D _ { 6 }$ were caused by the performance of the algorithm, they could be considered to obey the same distribution. Assume $D _ { i } \sim N ( \mu _ { D } , \sigma _ { D } ^ { 2 } ) , i = 1 , 2 , \dots n ,$ which means $D _ { 1 } , D _ { 2 } , . . . , D _ { 6 }$ constituting a sample of the normal population $N ( \mu _ { D } , \sigma _ { D } ^ { 2 } )$ , and where $\mu _ { D } , \sigma _ { D } ^ { 2 }$ were unknown. We test the following hypothesis:

$$
H _ {0}: \mu_ {D} \geq 0, H _ {1}: \mu_ {D} <   0
$$

Observed sample mean and sample variance of $D _ { 1 } , D _ { 2 } , . . . , D _ { 6 }$ were denoted by d ; $S _ { D } ^ { 2 } ,$ respectively, and the signi<sup>fi</sup>cance level is $\alpha =$ 0.01. The refusal domain of the test is $\begin{array} { r } { t = \frac { \overline { d } } { S _ { D } / \sqrt { n } } { \le - t _ { \alpha } ( n - 1 ) . n } = 6 , } \end{array}$ $t _ { 0 . 0 1 } ( 5 ) = 3 . 3 6 4 9 - t _ { 0 . 0 1 } ( 5 ) = - 3 . 3 6 4 9$ . The T-statistics of $D _ { 1 } , . . . , D _ { 6 }$ are respectively: $t _ { D _ { 1 } } = - 4 . 1 5 3 5$ $t _ { D _ { 2 } } = - 3 . 4 5 8 1$ $t _ { D _ { 3 } } = - 4 . 2 4 5 8$ $t _ { D _ { 4 } } = - 1 0 . 9 4 1 1$ $t _ { D _ { 5 } } = - 3 . 5 9 8 1$ $t _ { D _ { 6 } } = - 4 . 2 3 9 5$

The hypothesis H can be rejected due to $\left( t _ { D _ { 1 } } , . . . , t _ { D _ { 6 } } \right) { < } - t _ { 0 . 0 1 } ( 5 )$ which means that the better performances of KEML algorithm in terms of PM values over the <sup>fi</sup>ve selected data sets, compared to the other dimensionality reduction algorithms, are statistically signi<sup>fi</sup>cant.

## 4.3.2. Experiment on financial warning

The low-dimensional embeddings are then applied for early <sup>fi</sup>nancial warning, which investigated the effectiveness of KEML, KPCA, LTSA, LMDS, ISOMAP, LLE, and PCA. For Chinese A-share stock market, “ST” or “\*ST” will be put before the stock name of a company to warn about the investment risk or delisting risk when there is an abnormal <sup>fi</sup>- nancial condition.

The <sup>fi</sup>rst stage of the experiment obtained the low-dimensional embeddings of the <sup>fi</sup>nancial data using the seven algorithms. The K-means algorithm was used to identify companies with abnormal <sup>fi</sup>nancial positions among these low-dimensional representations. We used the $F _ { 1 } - s c o r e s \left[ 1 2 \right]$ to evaluate the result of each clustering. The $F _ { 1 } -$ scores combines recall (r) and precision (p) with an equal weight in the following form [12]:

$$
F _ {1} (r, p) = \frac {2 r p}{r + p}.
$$

Precision (p) is the ratio of correct assignments by the classi<sup>fi</sup>er divided by the total number of the classi<sup>fi</sup>er's assignments. Recall (r) is de<sup>fi</sup>ned to be the ratio of correct assignments by the classi<sup>fi</sup>er divided by the total number of correct assignments. The greater $F _ { 1 } - s c o r e$ the better performance of the algorithm is. Fig. 2 showed the $F _ { 1 } - s c o r e s$ (in percentages) about the clustering results of the seven algorithms on the <sup>fi</sup>ve data sets, respectively.

It can be seen that KEML algorithm is superior to the other approaches. Similarly, T-test is conducted on the $F _ { 1 } - s c o r e s .$ The test results indicate that the hypothesis $H _ { 1 }$ can be rejected at the level of 0.01 signi<sup>fi</sup>cance, which means the $F _ { 1 } - s c o r e s$ of KEML are all higher than

![](/api/attachments/6SMV3KNB/fulltext/images/e61fe8dfa9056d5ebf3f283aaa5cfe51ea3e7a539f45761a78a9b6f2ed6f5d25.jpg)

$$
T - t e s t: t _ {D _ {1}} = 3 6. 4 0 8 2, t _ {D _ {2}} = 2 9. 1 0 0 3, t _ {D _ {3}} = 2 6. 5 4 9 9, t _ {D _ {4}} = 1 9. 7 1 4 6, t _ {D _ {5}} = 2 6. 4 0 8 0, t _ {D _ {6}} = 2 2. 9 9 8 6; \alpha = 0. 0 1
$$

Fig. 2. F − scores (in percentages) about the clustering results of the seven algorithms.

Please cite this article as: Y. Huang, G. Kou, A kernel entropy manifold learning approach for <sup>fi</sup>nancial data analysis, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.04.004

Table 4  
Error rates (%) of the clustering results (K-means).

<table><tr><td>Dataset</td><td>KEML</td><td>KPCA</td><td>LTSA</td><td>LMDS</td><td>ISOMAP</td><td>LLE</td><td>PCA</td></tr><tr><td>2006 dataset</td><td>4.25</td><td>9.53</td><td>9.43</td><td>9.48</td><td>11.36</td><td>15.13</td><td>9.68</td></tr><tr><td>2007 dataset</td><td>5.13</td><td>9.51</td><td>9.15</td><td>9.28</td><td>10.54</td><td>12.03</td><td>10.34</td></tr><tr><td>2008 dataset</td><td>3.82</td><td>8.98</td><td>8.54</td><td>8.87</td><td>12.47</td><td>11.47</td><td>15.74</td></tr><tr><td>2009 dataset</td><td>6.51</td><td>9.95</td><td>9.58</td><td>9.69</td><td>10.08</td><td>15.81</td><td>10.11</td></tr><tr><td>2010 dataset</td><td>2.05</td><td>7.83</td><td>6.93</td><td>7.44</td><td>13.92</td><td>14.65</td><td>8.73</td></tr><tr><td>T-test</td><td colspan="7"> $t_{D_1}=-12.8766, t_{D_2}=-12.6904, t_{D_3}=-12.1460, t_{D_4}=-5.6556, t_{D_5}=-9.9479, t_{D_6}=-4.9928; \alpha = 0.01$ </td></tr></table>

the others. $F _ { 1 }$ −scores is called micro-averaging, which tends to be dominated by the classi<sup>fi</sup>er's performance on common categories [12].

The expected risk is de<sup>fi</sup>ned as $\begin{array} { r } { \hat { \mathbf { \rho } } _ { 1 } \pi _ { 1 } \frac { n _ { 1 } } { \left| A _ { 1 } \right| } + c _ { 0 } ( 1 - \pi _ { 1 } ) \frac { n _ { 0 } } { \left| A _ { 0 } \right| } } \end{array}$ [45,46], where $A _ { 1 }$ and $A _ { 0 }$ are the sets of abnormal and normal companies in the experimental data, $n _ { 1 }$ and $n _ { 0 }$ are the numbers of misclassi<sup>fi</sup>cations among abnormal and normal companies, $\pi _ { 1 }$ is the prior probability of abnormal, and $c _ { 1 }$ and $c _ { 0 }$ are misclassi<sup>fi</sup>cation costs of abnormal and normal companies [46]. Altman [49] obtained $3 2 \leq c _ { 1 } / c _ { 0 } \leq 6 2$ when $\pi _ { 1 } =$ 0.016 : 0.03. In the experiment, the average percentage of abnormal companies is approximately $\pi _ { 1 } = 0 . 1 : 0 . 2 ,$ , so we got $4 \leq c _ { 1 } / c _ { 0 } \leq 9$ Similar to [49], we set $c _ { 1 } / c _ { 0 } \cong 6 ,$ , and then the total error rate was $\begin{array} { r } { 0 . 5 1 \frac { n _ { 1 } } { | A _ { 1 } | } + 0 . 4 9 \frac { n _ { 0 } } { | A _ { 0 } | } } \end{array}$ . The results were summarized in Table 4.

Table 4 listed the error rates of all the clustering on the resulting low-dimensional embeddings in the <sup>fi</sup>rst experiment. From the results about T-test, it can be seen that the hypothesis $H _ { 0 }$ can be rejected, which means that the error rates of KEML (K-means) are lower than the others. KEML algorithm re<sup>fl</sup>ects the logical relationship between the <sup>fi</sup>nancial data. Fig. 3 shows the results of KEML (K-means).

In Fig. 3, “×” represents an abnormal company, and $" \bigcirc '$ represents a normal company. In 2006 and 2007, the number of the abnormal companies was relatively small among the 205 small and medium companies. Starting in 2008, the number rapidly increased and reached the peak in 2009, while it decreased in 2010. In 2006 and 2007, due to the bubble economic expansion of China stock market, a large number of companies were prospered in the surface. In 2008, the <sup>fi</sup>nancial crisis spread to China, a large number of companies had fallen into <sup>fi</sup>nancial distress, even bankruptcy. In 2009, the impact of the <sup>fi</sup>nancial crisis on China was sustained, which many companies were still in <sup>fi</sup>nancial trouble. In 2010, the crisis was eased under the efforts of the Chinese government. The results of KEML (K-means) re<sup>fl</sup>ect the actual situation, which indicates the effectiveness of the KEML algorithm in predicting <sup>fi</sup>nancial distress in the early stages.

## 4.3.3. KEML-based analysis of stock market volatility

The third stage of the experiment explored the intrinsic relationship structure of the <sup>fi</sup>nancial data set, which explains and predicts the operational status of stock market. To further analyze the intrinsic structure, we visualized the topology of manifold and established corresponding three-dimensional mesh graphs according to the neighborhood relations obtained by the KEML algorithm. Fig. 4 showed the spatial topology logical relationships of data points. In Fig. 4, each data set represented a system. Red areas represent the abnormal composition.

From 2006 to 2008, the red part was increasing every year. From 2009 to 2010, this trend slows down, which con<sup>fi</sup>rmed the results of clustering analysis. These irregular structure charts were projected into the corresponding contour plots. We conducted a structural analysis for 2010 dataset. According to the properties of contour plot, data points in the same contour line have the same probability distribution. The distances between different contour lines represent the information divergence between different types of data points. A smaller interval between the contour lines represented a greater information divergence between the two types of data points. The red line represents the abnormal data points in the “Peak”, and the adjacent orange and yellow contours represent the corresponding data points might fall into crisis. In the contour plot of 2010 data set, the blue contour data sets increased much more than other datasets. And the overall distribution of the lines was no longer complex, which illustrates that the number of abnormal data points and the subsystem instability declined and the system tends to stabilize.

The ups and downs of terrains indicate that the system reached a state at this time after a dramatic evolution. Through a series of information change, each data set formed a stable intrinsic structure, which is center manifold. The KEML algorithm provides the information variation between data points and information evolving trajectories of the intrinsic structure. As shown in Fig. 5, the horizontal axis represents the data points and the vertical axis represents the information change between points.

The <sup>fi</sup>gure showed that from 2006 to 2008, the information changes gradually increased and reached its peak in 2008. In 2009 and 2010, the magnitude of information change became weak. This indicates that the system had undergone dramatic internal oscillations from 2006 to 2008 and had tended to stabilized in 2009 and 2010. This overall trend can also be seen from the surface of the above three-dimensional mesh graphs. Through the complex information evolution, the system <sup>fi</sup>nally reached equilibrium.

This study uses Kolmogorov entropy (K entropy) to characterize this equilibrium state. Because each data set represented a system, K entropies for the <sup>fi</sup>ve data sets could be obtained through Section 3.7, which re<sup>fl</sup>ected the chaotic degree of the systems. Fig. 6 showed the trend of the <sup>fi</sup>ve K entropies and CSI 300 index during the period of 2006–2010.

![](/api/attachments/6SMV3KNB/fulltext/images/4f40b72c4caeb898f5ab7ddf81b8298c0cf4fa28e38e16338d96401f10655752.jpg)

![](/api/attachments/6SMV3KNB/fulltext/images/3d3dbbcd0b5f44dd28ee5d4110c92ff2cb5054d6a8c4bd328d517daaff74b94b.jpg)

![](/api/attachments/6SMV3KNB/fulltext/images/78b24723a49f5c2a2441edf502e5833fa1943fa4b264902bf01cbd62932b9505.jpg)  
Fig. 3. Results of KEML (K-means).

![](/api/attachments/6SMV3KNB/fulltext/images/63cdaac076c972951c9bda52811313819353ceb7a62ef080d43b189e6dccfa5f.jpg)

![](/api/attachments/6SMV3KNB/fulltext/images/d2d93e2498738377729a9c7bb229785c536df59d2ad0cffa57835cbfe03263f6.jpg)  
Please cite this article as: Y. Huang, G. Kou, A kernel entropy manifold learning approach for <sup>fi</sup>nancial data analysis, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.04.004

![](/api/attachments/6SMV3KNB/fulltext/images/bf54ce2dad2f7732ec9daeac579363a7da2f59a3108ce33d6c559b52d77597aa.jpg)

![](/api/attachments/6SMV3KNB/fulltext/images/dcc15ed73e66a5786397ec8541e335d451afe437314768746375ea2738ed0b34.jpg)

![](/api/attachments/6SMV3KNB/fulltext/images/d5a9afaf366b2b01f1dab451e662c66902869144405dce9f1350f5802183fdd9.jpg)  
Fig. 4. Mesh graphs of the manifolds. (For interpretation of the references to color in this <sup>fi</sup>gure legend, the reader is referred to the web version of this article.)

In the information evolution, positive and negative information shift, severe vibration information changes did not mean that the <sup>fi</sup>nal entropy value was greater. In 2008, the resulting entropy value was less than 2007. CSI 300 index describes the overall trend of China A-share market, which re<sup>fl</sup>ects an overview and running status of the stock price changes of China's securities market. As shown in Fig. 6, the K entropy increased from 2006 to 2007, and peaked in 2007, which means that the uncertainty and instability in the system increased rapidly. At the same time, the CSI 300 Index was peaked. In 2008, the global <sup>fi</sup>nancial crisis spread to China while CSI 300 Index plummeted. After the crisis, the instability factors were partially removed and K entropy began to reduce. This can be con<sup>fi</sup>rmed from the above Fig. 6: the CSI 300 index gradually rose in 2009–2010. Thus, the KEML algorithm can help to forecast the overall trend of a stock market.

Information evolving trajectories of the intrinsic structures:  
![](/api/attachments/6SMV3KNB/fulltext/images/d1c9d2d0f23a2ce4a0fa618eb25dac1c18981237987366073ad6595ccbc9a23c.jpg)  
Fig. 5. Information evolving trajectories of the intrinsic structures.

The experiment shows that the KEML algorithm is able to extract the objective logical relationships among <sup>fi</sup>nancial data to improve the accuracy of the early <sup>fi</sup>nancial warning. It can also derive the overall characteristics of the system, which provide the objective criteria for explaining and predicting the stock market volatility.

## 5. Conclusion

Based on the assumption that high-dimensional data lie approximately on a low-dimensional manifold embedded in the ambient space, this paper tried to discover the intrinsic manifold (or lowdimensional representation) in high-dimensional <sup>fi</sup>nancial data by proposing a manifold learning algorithm for <sup>fi</sup>nancial data.

![](/api/attachments/6SMV3KNB/fulltext/images/a8875f5c820932336b84831d2726ff99e227421e41685c9a627e6db75055137d.jpg)  
Fig. 6. K entropies and CSI300 in 2006–2010  
Please cite this article as: Y. Huang, G. Kou, A kernel entropy manifold learning approach for <sup>fi</sup>nancial data analysis, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.04.004

Different from traditional manifold learning methods, KEML employs the information metric to measure the relationships between <sup>fi</sup>- nancial data points and yields reasonable and accurate low-dimensional embedding of the original <sup>fi</sup>nancial data set. The results of the experiment indicate that the KEML algorithm outperforms other six dimensionality reduction algorithms in terms of accuracy of low-dimensional embedding. In the subsequent <sup>fi</sup>nancial early warning experiment, the error rates of the clustering results generated by KEML were lower than the six other algorithms. The experiment further derived the Kolmogorov entropies, which characterize the system dynamical properties of the original data space. In comparison with CSI300 index, the Kolmogorov entropies obtained from the KEML algorithm can explain and predict the stock market volatility.

The theoretical and practical implications of this study are:

(1) Introduced kernel entropy manifold learning into <sup>fi</sup>nancial analysis to explore and analyze the problems of <sup>fi</sup>nancial <sup>fi</sup>eld, and proved the effectiveness of the proposed algorithm through experiments.

(2) The traditional manifold learning assumption is that highdimensional data lie on a manifold in Euclidean space. Through the theoretical and empirical analyses, this study proved that this assumption may not be valid in <sup>fi</sup>nancial data analysis.

There are several limitations in our approach, which need to be further investigated in the future. First, since the computational complexity of all the kernel-based techniques depends on the number of data points, the computational cost may increase a lot in our approach, when applied to large-scale data sets; Second, our approach may not adaptively extract features of the data set, and need to be extended to other <sup>fi</sup>elds, such as population analysis and biometrics, rather than restricted to <sup>fi</sup>nancial datasets.

## Acknowledgments

This research has been partially supported by grants from the National Natural Science Foundation of China (#71222108), the Research Fund for the Doctoral Program of Higher Education (20120185110031), and Program for New Century Excellent Talents in University (NCET-10- 0293).

## References

[1] C.F. Tsai, Y.C. Hsiao, Combining multiple feature selection methods for stock prediction: union, intersection, and multi-intersection approaches, Decision Support Systems 50 (2010) 258–269.

[2] S.W.K. Chan, J. Franklin, A text-based decision support system for <sup>fi</sup>nancial sequence prediction, Decision Support Systems 52 (2011) 189–198.

[3] T. Le, V.C. Epa, F.R. Burden, D.A. Winkler, Quantitative structure–property relationship modeling of diverse materials properties, Chemical Reviews 112 (2012) 2889–2919.

[4] H.S. Seung, D.D. Lee, The manifold ways of perception, Science 290 (2000) 2268–2269.

[5] Z. Zhang, H. Zha, Principal manifolds and nonlinear dimension reduction via local tangent space alignment, SIAM Journal on Scienti<sup>fi</sup>c Computing 26 (2004) 313–338.

[6] J.B. Tenenbaum, V. Sivlar, J.C. Langford, A global geometric framework for nonlinear dimensionality reduction Science 290 (2000) 2319–2323

[7] S.T. Roweis, L.K. Saul, Nonlinear dimensionality reduction by locally linear embedding Science 290 (2000) 2323–2326

[8] L. Yang, Alignment of overlapping locally scaled patches for multidimensional scaling and dimensionality reduction JEEE Transactions on Pattern Analysis and Machine Intelligence 30 (2008) 438–450.

[9] S. Kaski, J. Sinkkonen, J. Peltonen, Bankruptcy analysis with self-organizing maps in learning metrics, IEEE Transaction on Neural Networks 12 (2001) 936–947.

[10] M. Zhang, S. Xu, J. Fulcher, Neuron-adaptive higher order neural-network models for automated <sup>fi</sup>nancial data modeling, IEEE Transactions on Neural Networks 13 (2002) 188–204.

[11] H. Qiao, P. Zhang, D. Wang, B. Zhang, An explicit nonlinear mapping for manifold learning, IEEE Transactions on Cybernetics 43 (2013) 51–63.

[12] D. Cai, X. He, Manifold adaptive experimental design for text categorization, IEEE Transactions on Knowledge and Data Engineering 24 (2012) 707–719.

[13] B. Schölkopf, A.J. Smola, Learning with Kernels, MIT Press, Cambridge, MA, USA, 2002.

[14] T. Bellotti, R. Matousek, C. Stewart, A note comparing support vector machines and ordered choice models' predictions of international banks' ratings, Decision Support Systems 51 (2011) 682–687.

[15] P. Hájek, Municipal credit rating modeling by neural networks, Decision Support Systems 51 (2011) 108–118.

[16] P. Ravisankar, V. Ravi, I. Bose, Failure prediction of dotcom companies using neural network-genetic programming hybrids, Information Science 180 (2010) 1257–1267.

[17] A.F. Atiya, Bankruptcy prediction for credit risk using neural networks: a survey and new results, IEEE Transactions on Neural Networks 12 (2001) 929–935

[18] Z. Huang, H. Chen, C.J. Hsu, W.H. Chen, S. Wu, Credit rating analysis with support vector machines and neural networks: a market comparative study, Decision Support Systems 37 (2004) 543–558.

[19] D. Martens, B. Baesens, T.V. Gestel, J. Vanthienen, Comprehensible credit scoring models using rule extraction from support vector machines, European Journal of Operational Research 183 (2007) 1466–1476.

[20] Y. Wang, S. Wang, K.K. Lai, A new fuzzy support vector machine to evaluate credit risk, IEEE Transactions on Fuzzy Systems 13 (2005) 820–831.

[21] P. Jardin, E. Séverin, Predicting corporate bankruptcy using a self-organizing map: an empirical study to improve the forecasting horizon of a <sup>fi</sup>nancial failure model, Decision Support Systems 51 (2011) 701–711.

[22] P. Sarlin, Decomposing the global <sup>fi</sup>nancial crisis: a self-organizing time map, Pattern Recognition Letters 34 (2013) 1701–1709.

[23] C. Serrano-Cinca, B. Gutiérrez-Nieto, Partial least square discriminator analysis for bankruptcy prediction, Decision Support Systems 54 (2013) 1245–1255.

[24] U. Yolcu, E. Egrioglu, C.H. Aladag, A new linear & nonlinear arti<sup>fi</sup>cial neural network model for time series forecasting, Decision Support Systems 54 (2013) 1340–1347.

[25] L.J. Kao, C.C. Chiu, C.J. Lu, C.H. Chang, A hybrid approach by integrating waveletbased feature extraction with MARS and SVR for stock index forecasting, Decision Support Systems 54 (2013) 1228–1244.

[26] C.J. Lu, T.S. Lee, C.C. Chiu, Financial time series forecasting using independent component analysis and support vector regression, Decision Support Systems 47 (2009) 115–125.

[27] S.S. Groth, J. Muntermann, An intraday market risk management approach based on textual analysis, Decision Support Systems 50 (2011) 680–691.

[28] S.L. Humpherys, K.C. Mof<sup>fi</sup>tt, M.B. Burns, J.K. Burgoon, W.F. Felix, Identi<sup>fi</sup>cation of fraudulent <sup>fi</sup>nancial statements using linguistic credibility analysis, Decision Support Systems 50 (2011) 585–594.

[29] R.P. Schumaker, H. Chen, Textual analysis of stock market prediction using breaking <sup>fi</sup>nancial news: the AZFin Text System, ACM Transactions on Information Systems 27 (2009) 1–19.

[30] D.L. Olson, D. Delen, Y. Meng, Comparative analysis of data mining methods for bankruptcy prediction, Decision Support Systems 52 (2012) 464–473.

[31] M.H.C. Law, A.K. Jain, Incremental nonlinear dimensionality reduction by manifold learning, IEEE Transactions on Pattern Analysis and Machine Intelligence 28 (2006) 377–391.

[32] T. Lin, H. Zha, Riemannian manifold learning, IEEE Transactions on Pattern Analysis and Machine Intelligence 30 (2008) 796–809

[33] I.A. Costa, A.O. Hero, Geodesic entropic graphs for dimension and entropy estimation in manifold learning, IEEE Transaction on Signal Processing 52 (2004) 2210-2221.

[34] K.M. Carter, R. Raich, W.G. Finn, A.O. Hero, FINE: <sup>fi</sup>sher information nonparametric embedding, IEEE Transactions on Pattern Analysis and Machine Intelligence 31 (2009) 2093–2098.

[35] C.E. Shannon, A mathematical theory of communication, Bell System Technical Journal 27 (1948) 379–423.

[36] A.N. Kolmogorov, Three approaches to the quantitative de<sup>fi</sup>nition of information, Problems of Information Transmission 1 (1965) 1–7.

[37] C.H. Bennett, P. Gács, M. Li, P.M.B. Vitányi, W.H. Zurek, Information distance, IEEE Transactions on Information Theory 44 (1998) 1407–1423.

[38] R. Jenssen, Kernel entropy component analysis, IEEE Transactions on Pattern Analysis and Machine Intelligence 32 (2010) 847–860.

[39] E. Parzen, On the estimation of a probability density function and the mode, Annals of Mathematical Statistics 32 (1962).1065–1076

[40] R.C. Moyer, J.R. McGuigan, R.P. Rao, W.J. Kretlow, Contemporary Financial Management, Cengage Learning, Ohio, 2012

[41] T. Bury, Market structure explained by pairwise interactions, Physica A—Statistical Mechanics and its Applications 392 (2013) 1375–1385.

[42] G. Seber, Multivariate Observations, John Wiley & Sons, New York, 1984.

[43] S. Xiang, F. Nie, C. Zhang, C. Zhang, Nonlinear dimensionality reduction with local spine embedding, IEEE Transactions on Knowledge and Data Engineering 21 (2009) 1285–1298.

[44] Y. Goldberg, Y. Ritov, Local procrustes for manifold embedding: a measure of embedding quality and embedding algorithms, Machine Learning 77 (2009) 1–25.

[45] H. Frydman, E.I. Altman, D. Kao, Introducing recursive partitioning for <sup>fi</sup>- nancial classi<sup>fi</sup>cation: the case of <sup>fi</sup>nancial distress, Journal of Finance 40 (1985) 269-291

[46] Y.U. Ryu, W.T. Yue, Firm bankruptcy prediction: experimental comparison of isotonic separation and other classification approaches JEEE Transactions on Systems Man, and Cybernetics—Part A: Systems and Humans 35 (2005) 727–737.

[47] A.N. Kolmogorov, A new metric invariant of transient dynamical systems and automorphisms of Lebesgue spaces, Doklady Akademii Nauk SSSR 119 (1958) 861–864.

[48] N. Brodsky, A. Chigogidze, E.V. Scepin, Sections of serre <sup>fi</sup>brations with 2-manifold <sup>fi</sup>bers, Topology and its Applications 155 (2008) 773–782.

[49] E.I. Altman, Commercial bank lending: process, credit scoring, and costs of errors in lending, Journal of Financial and Quantitative Analysis 15 (1980) 813–832.

[50] K.M. Carter, R. Raich, W.G. Finn, A.O. Hero, Information-geometric dimensionality reduction JFFE Signal Processing Magazine 28 (2011) 89–99

[51] A. Renyi, On the dimension and entropy of probability distributions, Acta Mathematica Academiae Scientiarum Hungarica 10 (1959) 193–215.

[52] A.A. Jamshidi, M.J. Kirby, D.S. Broomhead, Geometric manifold learning, IEEE Signal Processing Magazine 28 (2011) 69–76.

[53] R. Li, T.P. Tian, S. Sclaroff, Divide, conquer and coordinate: globally coordinated switching linear dynamical system, IEEE Transactions on Pattern Analysis and Machine Intelligence 34 (2012) 654–669.

[54] J. Yang, D. Zhang, A.F. Frangi, J. Yang, Two-dimensional PCA: a new approach to appearance-based face representation and recognition, IEEE Transactions on Pattern Analysis and Machine Intelligence 26 (2004) 131–137.

Yan Huang is a doctoral candidate of School of Management and Economics, University of Electronic Science and Technology of China. She received her M.S. degree in Management Science and Engineering from Beijing University of Technology in 2007. Her research interests include data mining, machine learning and information management.

Gang Kou is a Professor and Executive Dean of School of Business Administration, Southwestern University of Finance and Economics. He is the managing editor of International Journal of Information Technology & Decision Making and series editor of Quantitative Management (Springer). Previously, he was a professor of School of Management and Economics, University of Electronic Science and Technology of China, and a research scientist in Thomson Co., R&D. He received his Ph.D. in Information Technology from the College of Information Science & Technology, Univ. of Nebraska at Omaha; got his Master's degree in Dept of Computer Science, Univ. of Nebraska at Omaha; and B.S. degree in Department of Physics, Tsinghua University, Beijing, China. He has participated in various data mining projects, including data mining for software engineering, network intrusion detection, health insurance fraud detection and credit card portfolio analysis. He has published more than eighty papers in various peer-reviewed journals and conferences. Gang Kou has been Keynote speaker/workshop chair in several international conferences. He co-chaired Data Mining contest on The Seventh IEEE International Conference on Data Mining 2007 and he is the Program Committee Co-Chair of the 20th International Conference on Multiple Criteria Decision Making (2009) and NCM 2009: 5th International Joint Conference on INC, ICM and IDC. He is also co-editor of special issues of several journals, such as Journal of Multi Criteria Decision Analysis, Decision Support Systems, Journal of Supercomputing and Information Sciences.

Please cite this article as: Y. Huang, G. Kou, A kernel entropy manifold learning approach for <sup>fi</sup>nancial data analysis, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.04.004
