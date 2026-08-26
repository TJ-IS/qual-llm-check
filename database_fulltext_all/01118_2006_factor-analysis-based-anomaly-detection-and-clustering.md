---
otero_id: 1118
otero_key: "FMZYSV2R"
title: "Factor-analysis based anomaly detection and clustering"
authors: "Ningning Wu; Jing Zhang"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2005.01.005"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dsw

# Factor-analysis based anomaly detection and clustering

Ningning Wu<sup>a,\*</sup>, Jing Zhang<sup>b</sup>

<sup>a</sup>University of Arkansas at Little Rock, Information Science, 2801 S. University Ave., 72204 Little Rock, United States <sup>b</sup>University of Arkansas at Little Rock, Applied Science, 2801 S. University Ave., 72204 Little Rock, United States

Available online 3 March 2005

## Abstract

This paper presents a novel anomaly detection and clustering algorithm for the network intrusion detection based on factor analysis and Mahalanobis distance. Factor analysis is used to uncover the latent structure of a set of variables. The Mahalanobis distance is used to determine the <sup>b</sup>similarity<sup>Q</sup> of a set of values from an <sup>b</sup>unknown<sup>Q</sup> sample to a set of values measured from a collection of <sup>b</sup>known<sup>Q</sup> samples. By utilizing factor analysis and Mahalanobis distance, we developed an algorithm 1) to identify outliers based on a trained model, and 2) to cluster attacks by abnormal features. <sup>D</sup> 2005 Elsevier B.V. All rights reserved.

Keywords: Anomaly detection; Intrusion detection; Factor analysis

## 1. Introduction

Intrusion detection is generally categorized into two broad categories: signature based and profile based. The signature-based approach (also called misuse detection) performs detection by searching network audit data for the matches of the <sup>b</sup>signatures<sup>Q</sup> of known attacks. Profile-based approach (also called anomaly detection) performs detection by searching the network audit data for deviations from the established profiles of normal behaviors of users and systems. Profiles of normal behavior can be built with a variety of techniques including statistical methods [1,4,21,22], association rules [2,3], neural networks [6], computer immunology [5], and specification based methods [24].

As network attacks generally do something different from normal network activity, they should not comply with profiles. The profile-based approach usually uses a collection of <sup>b</sup>normal<sup>Q</sup> measures on a set of statistics [21,22] or features [2,3] to represent profiles. To determine whether an observed event is normal or not, it examines its values on the statistics to see if they are different from those in the profile. If this is the case, the event is flagged as abnormal; otherwise, it is considered as normal. Techniques used for judging the normality of an event include eBayes [26], sequence analysis [5,28], expert system, association rules and classification [3], and pseudoBayes estimators [2].

When the profile is represented by a collection of observations on a set of statistics, it is natural to view the profile as a multivariate data set. The task of examining the <sup>b</sup>normality<sup>Q</sup> of an observed event is equivalent to the one of examining whether the event is an outlier of the profile. Thus, we can employ multivariate statistical methods to build the profile model and to detect events that do not fit the profile model. These events should correspond to the potential attacks.

In this paper, we propose a novel technique based on factor analysis for network anomaly detection and clustering. Factor analysis is a statistical approach that can be used to analyze interrelationships among a large number of variables and to explain these variables in terms of their common underlying dimensions (factors). It involves finding a way of condensing the information contained in a number of original variables into a smaller set of dimensions with a minimum loss of information [9]. As a measurement, the Mahalanobis distance is used in anomaly detection and clustering. The advantage of Mahalanobis distance is its scale independence.

In the proposed method, given a training data set, we first apply factor analysis to reduce the dimensionality of the training data by capturing and retaining the important factors of data. Then, for any test sample, we use Mahalanobis distance to examine whether it is an anomaly. Generally a test sample is considered as an anomaly if it has abnormal values on one or multiple factors. When an anomaly is found, the factors which have abnormal values can be identified and used for clustering anomaly. We apply our anomaly detection and clustering algorithm to network traffic data provided by DARPA Intrusion Detection System Evaluation program. The results demonstrate that the algorithm is effective in capturing network attacks with relatively low false alarms and high detection rate.

The remainder of this paper is organized as follows. Sections 2 and 3 give a brief introduction to factor analysis and Mahalanobis distance. Section 4 presents the factor-analysis based anomaly detection and clustering algorithm. Section 5 discusses the application of the algorithm to the network traffic analysis along with the experimental results. Section 6 contains related work and Section 7 concludes the paper.

## 2. Factor analysis

## 2.1. Introduction

Factor analysis is used to uncover the latent structure (dimensions) of a set of variables. It reduces attribute space from a larger number of variables to a smaller number of factors. Factor analysis has a variety of applications such as the assessment of underlying relationships or dimensions in the data, and the replacement of original variables with fewer, new variables.

Let X be the observable random vector with m variables $X _ { 1 } , X _ { 2 } , \ldots , X _ { m }$ that have means $\mu _ { 1 } , \mu _ { 2 } , \ldots , \mu _ { m } ,$ and covariance matrix -. The factor model postulates that X is linearly dependent on a few unobservable random variables $F _ { 1 } , F _ { 2 } , \ldots , F _ { p } ,$ called common factors, and m additional sources of variation $\varepsilon _ { 1 } , \varepsilon _ { 2 } , \ldots , \varepsilon _ { m } ,$ called errors, or specific factors. The factor analysis model is [11]:

$$
\begin{array}{l} X _ {1} - \mu_ {1} = l _ {1 1} F _ {1} + l _ {1 2} F _ {2} + \dots + l _ {1 p} F _ {p} + \varepsilon_ {1} \\ X _ {2} - \mu_ {2} = l _ {2 1} F _ {1} + l _ {2 2} F _ {2} + \dots + l _ {2 p} F _ {p} + \varepsilon_ {2} \\ \vdots \\ X _ {m} - \mu_ {m} = l _ {m 1} F _ {1} + l _ {m 2} F _ {2} + \dots + l _ {m p} F _ {p} + \varepsilon_ {m} \end{array}
$$

or, in matrix notation

$$
\mathbf {X} - \boldsymbol {\mu} = \mathbf {L F} + \varepsilon\tag{1}
$$

where,

$$
\begin{array}{l} \mathbf {X} = [ X _ {1} X _ {2} \dots X _ {m} ] ^ {\mathrm{T}}, \boldsymbol {\mu} = [ \mu_ {1} \mu_ {2} \dots \mu_ {m} ] ^ {\mathrm{T}}, \\ \mathbf {F} = [ F _ {1} F _ {2} \dots F _ {p} ] ^ {\mathrm{T}}, \varepsilon = [ \varepsilon_ {1} \varepsilon_ {2} \dots \varepsilon_ {m} ] ^ {\mathrm{T}} \end{array}
$$

$$
\mathbf {L} = \left[ \begin{array}{c c c c} l _ {1 1} & l _ {1 2} & \dots & l _ {1 p} \\ l _ {2 1} & l _ {2 2} & \dots & l _ {2 p} \\ \vdots & \vdots & \vdots & \vdots \\ l _ {m 1} & l _ {m 2} & \dots & l _ {m p} \end{array} \right]
$$

The coefficient $l _ { i j }$ is called the loading of the ith variable on the jth factor. The ith specific factor $\varepsilon _ { i }$ is associated only with the ith variable $X _ { i } .$ . The m deviations $X _ { 1 } { - } \mu _ { 1 } , X _ { 2 } { - } \mu _ { 2 } , \ldots , X _ { \mathrm { { m } } } { - } \mu _ { \mathrm { { m } } }$ are expressed in terms of m+p random variables $F _ { 1 } , F _ { 2 } , \dots , F _ { p } , \varepsilon _ { 1 }$ $\varepsilon _ { 2 } , \ldots , \varepsilon _ { m }$ which are unobservable. The unobservable random vectors F and e are assumed to satisfy the following conditions:

$$
E [ \mathbf {F} ] = 0, \operatorname{Cov} (\mathbf {F}) = E \left[ \mathbf {F F} ^ {\mathrm{T}} \right] = \mathbf {I}
$$

$$
\begin{array}{c} E [ \varepsilon ] = 0, \operatorname{Cov} (\varepsilon) = E \bigl [ \varepsilon \varepsilon^ {\mathrm{T}} \bigr ] = \Psi \\ = \left[ \begin{array}{c c c c} \psi_ {1} & 0 & \dots & 0 \\ 0 & \psi_ {2} & \dots & 0 \\ \vdots & \vdots & \dots & \vdots \\ 0 & 0 & \dots & \psi_ {m} \end{array} \right] \end{array}
$$

$$
\operatorname{Cov} (\varepsilon , \mathbf {F}) = E \left[ \varepsilon \mathbf {F} ^ {\mathrm{T}} \right] = 0\tag{2}
$$

The conditions in (2) and the relation in (1) constitute the orthogonal factor model. The orthogo nal factor model implies a covariance structure for X. From the model we have

$$
\begin{array}{l} (\mathbf {X} - \boldsymbol {\mu}) (\mathbf {X} - \boldsymbol {\mu}) ^ {\mathrm{T}} = (\mathbf {L F} + \varepsilon) (\mathbf {L F} + \varepsilon) ^ {\mathrm{T}} \\ \qquad = (\mathbf {L F} + \varepsilon) \Big ((\mathbf {L F}) ^ {\mathrm{T}} + \varepsilon^ {\mathrm{T}} \Big) \\ \qquad = \mathbf {L F} (\mathbf {L F}) ^ {\mathrm{T}} + \varepsilon (\mathbf {L F}) ^ {\mathrm{T}} + \mathbf {L F} \varepsilon^ {\mathrm{T}} + \varepsilon \varepsilon^ {\mathrm{T}} \end{array}
$$

Hence the covariance matrix is,

$$
\begin{array}{l} \Sigma = \operatorname{Cov} (\mathbf {X}) = E (\mathbf {X} - \boldsymbol {\mu}) (\mathbf {X} - \boldsymbol {\mu}) ^ {\mathrm{T}} \\ \quad = \mathbf {L} E \big (\mathbf {F} \mathbf {F} ^ {\mathrm{T}} \big) \mathbf {L} ^ {\mathrm{T}} + E \big (\varepsilon \mathbf {F} ^ {\mathrm{T}} \big) \mathbf {L} ^ {\mathrm{T}} + \mathbf {L} E \big (\mathbf {F} \varepsilon^ {\mathrm{T}} \big) + E \big (\varepsilon \varepsilon^ {\mathrm{T}} \big) \\ \quad = \mathbf {L} \mathbf {L} ^ {\mathrm{T}} + \boldsymbol {\Psi} \end{array}
$$

By (1) and (2) we have

$$
\begin{array}{l} (\mathbf {X} - \boldsymbol {\mu}) \mathbf {F} ^ {\mathrm{T}} = (\mathbf {L F} + \varepsilon) \mathbf {F} ^ {\mathrm{T}} = \mathbf {L F F} ^ {\mathrm{T}} + \varepsilon \mathbf {F} ^ {\mathrm{T}} \\ \text { so } \\ \operatorname{Cov} (\mathbf {X}, \mathbf {F}) = E (\mathbf {X} - \boldsymbol {\mu}) \mathbf {F} ^ {\mathrm{T}} = \mathbf {L} E \big (\mathbf {F F} ^ {\mathrm{T}} \big) + E \big (\varepsilon \mathbf {F} ^ {\mathrm{T}} \big) = \mathbf {L}. \end{array}
$$

Thus, we can get covariance structure for the orthogonal factor model:

$$
\begin{array}{c} \operatorname{Cov} (\mathbf {X}) = \mathbf {L L} ^ {\mathrm{T}} + \boldsymbol {\Psi} \text { or } \\ \operatorname{Var} (X _ {i}) = l _ {i 1} ^ {2} + \dots + l _ {i p} ^ {2} + \psi_ {i} \end{array}
$$

$$
\operatorname{Cov} \left(X _ {i}, X _ {k}\right) = l _ {i 1} l _ {k 1} + \dots + l _ {i p} l _ {k p}\tag{3}
$$

$$
\operatorname{Cov} (\mathbf {X}, \mathbf {F}) = \mathbf {L} \text { or } \operatorname{Cov} (X _ {i}, F _ {j}) = l _ {i j}\tag{4}
$$

In (3), $\textstyle \sum _ { j = 1 } ^ { p } l _ { i j } ^ { 2 }$ in the variance of the ith variable $X _ { i }$ is called the ith communality.

## 2.2. Methods of parameter estimation

In this section we will discuss the methods of estimating the parameters of the factor model (1) from a given training data set. For a given set of n observations on m observed variables $X _ { 1 } , X _ { 2 } , . . . , X _ { m } ,$ we use a vector to represent the m observed variables of the ith observation,

$$
\mathbf {x} _ {i} ^ {\mathrm{T}} = [ x _ {i 1}, x _ {i 2}, \dots , x _ {i m} ]
$$

The sample covariance matrix is given as

$$
\mathbf {S} = \frac {1}{n - 1} \sum_ {i = 1} ^ {n} \left(\mathbf {x} _ {i} - \bar {\mathbf {x}}\right) \left(\mathbf {x} _ {i} - \bar {\mathbf {x}}\right) ^ {\mathrm{T}}\tag{5}
$$

where $\bar { \mathbf { x } } { = } [ \bar { \mathrm { x } } _ { 1 } , \bar { \mathrm { x } } _ { 2 } , \ldots , \bar { \mathrm { x } } _ { m } ] ^ { \mathrm { T } }$ is the sample mean vector, and $\bar { \mathbf { X } } _ { j } ,$ , defined as $\begin{array} { r } { \bar { x } _ { j } = \frac { 1 } { n } \sum _ { i = 1 } ^ { n } x _ { i j } , } \end{array}$ , is the estimated mean of jth column random variable $X _ { j }$

The factor loadings in (1) can be estimated from the relationship between the covariance matrix and factor loading matrix given in (3). In the estimation, the sample covariance matrix S is used to estimate the factor loadings. From the spectral decomposition, the sample covariance matrix S can be represented by its eigenvalue–eigenvector pairs $( \hat { \lambda } _ { 1 } , \hat { \mathbf { e } } _ { 1 } ) , ( \hat { \lambda } _ { 2 } , \hat { \mathbf { e } } _ { 2 } ) , . . . ( \hat { \lambda } _ { m } ,$ $\widehat { \mathbf { e } } _ { m } )$ , where $\hat { \lambda } _ { 1 } { \geq } \hat { \lambda } _ { 2 } { \geq } . . . \hat { \geq } \hat { \lambda } _ { m }$

$$
\mathbf {S} = \sum_ {i = 1} ^ {m} \hat {\lambda} _ {i} \hat {\boldsymbol {e}} _ {i} \hat {\boldsymbol {e}} _ {i} ^ {\mathrm{T}}
$$

When the last $m - p \ \left( p < m \right)$ eigenvalues are small enough, we can use principal component method to simplify the expression of the sample covariance matrix S by selecting the first $p$ principal eigenvalue– eigenvactor pairs.

$$
\mathbf {S} \approx \sum_ {i = 1} ^ {p} \hat {\lambda} _ {i} \hat {e} _ {i} \hat {e} _ {i} ^ {\mathrm{T}} = \left[ \sqrt {\hat {\lambda} _ {1}} \hat {e} _ {1} \sqrt {\hat {\lambda} _ {2}} \hat {e} _ {2} \dots \sqrt {\hat {\lambda} _ {p}} \hat {e} _ {p} \right] \left[ \begin{array}{c} \sqrt {\hat {\lambda} _ {1}} \hat {e} _ {1} ^ {\mathrm{T}} \\ \sqrt {\hat {\lambda} _ {2}} \hat {e} _ {2} ^ {\mathrm{T}} \\ \vdots \\ \sqrt {\hat {\lambda} _ {p}} \hat {e} _ {p} ^ {\mathrm{T}} \end{array} \right]\tag{6}
$$

Then from (3) we can select the matrix of estimated factor loadings $\{ \hat { \bf l } _ { i j } \}$ }in (6) as

$$
\hat {\mathbf {L}} = \left[ \sqrt {\hat {\lambda} _ {1}} \hat {\mathbf {e}} _ {1}, \sqrt {\hat {\lambda} _ {2}} \hat {\mathbf {e}} _ {2}, \dots , \sqrt {\hat {\lambda} _ {p}} \hat {\mathbf {e}} _ {p} \right]\tag{7}
$$

The estimated specific variances are provided by the diagonal elements of the matrix $\mathbf { S } \mathrm { - } \mathbf { \hat { L } } \mathbf { \hat { L } } ^ { \mathrm { T } }$ , so

$$
\hat {\pmb {\Psi}} = \mathbf {S} - \hat {\mathbf {L}} \hat {\mathbf {L}} ^ {\mathrm{T}}
$$

$$
= \left[ \begin{array}{c c c c} \hat {\psi} _ {1} & 0 & \dots & 0 \\ 0 & \hat {\psi} _ {2} & \dots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \dots & \hat {\psi} _ {m} \end{array} \right] \text {with} \hat {\psi} _ {i} = s _ {i i} - \sum_ {j = 1} ^ {p} \hat {l} _ {i j} ^ {2}\tag{8}
$$

Communalities are estimated as

$$
\hat {\boldsymbol {h}} _ {i} ^ {2} = \hat {\boldsymbol {l}} _ {i 1} ^ {2} + \hat {\boldsymbol {l}} _ {i 2} ^ {2} + \dots + \hat {\boldsymbol {l}} _ {i p} ^ {2}
$$

For the principal component solution, the estimated loadings for a given factor do not change as the number of factors is increased. For example, if $p { = } 1$ $\hat { \mathbf { L } } = \left\lceil \sqrt { \hat { \lambda } _ { 1 } } \hat { \mathbf { e } } _ { 1 } \right\rceil$ and if $p { = } \underline { { 2 } } , \hat { \mathbf { L } } = \left\lceil \sqrt { \hat { \lambda } _ { 1 } } \hat { \mathbf { e } } _ { 1 } , \sqrt { \hat { \lambda } _ { 2 } } \hat { \mathbf { e } } _ { 2 } \right\rceil$ 4 where L $( \sqrt { \lambda } _ { 1 } , \mathbf { \bar { e } } _ { 1 } )$ and $( \sqrt { \hat { \lambda } _ { 2 } } , \hat { \mathbf { e } } _ { 2 } )$ are the first two eigenvalue–eigenvector pairs for S.

## 2.3. Factor scores

Factor scores are estimated values of the unobserved random factor vector $\mathbf { F } { = } [ F _ { 1 } F _ { 2 } . . . F _ { p } ] ^ { \mathrm { T } }$ . That ${ \mathrm { i s } } ,$ factor scores $\hat { \boldsymbol { \mathrm { f } } } _ { j }$ is equal to the estimate of the values $\mathbf { f } _ { j }$ attained by $\mathbf { F }$ in jth case.

Since the unobserved quantities $\mathbf { f } _ { j }$ and $\varepsilon _ { j }$ outnumber the observed $\mathbf { x } _ { j } ,$ approaches to estimating factor values have been proposed including the weighted least squares method and the regression method. Both approaches have two elements in common:

<sup>!</sup> They treat the estimated factor loadings $\hat { \mathrm { l } } _ { i j }$ and specific variances $\hat { \psi } _ { i }$ as if they were the true values.

<sup>!</sup> They involve linear transformation of the original data.

For simplicity, we give the result of factor scores estimated by the principal component using least squares method. Factor scores estimated by the principal component are generated using an unweighted least squares procedure:

$$
\hat {\mathbf {f}} _ {j} = \left(\hat {\mathbf {L}} ^ {\mathrm{T}} \hat {\mathbf {L}}\right) ^ {- 1} \hat {\mathbf {L}} ^ {\mathrm{T}} \left(\mathbf {x} _ {j} - \bar {\mathbf {x}}\right)\tag{9}
$$

## 3. Mahalanobis distance

The Mahalanobis distance is an effective way of determining the similarity of a set of values from an unknown sample to a set of values measured from a collection of known samples. Mahalanobis squared distance is a measure of statistical distance in multidimensional space. This statistics measures the distance from the centroid—multidimensional equivalent of a mean, for a set of vector for each of the independent variables included in the analysis.

Let $\mathbf { x } _ { 1 } , \ \mathbf { x } _ { 2 } , \ . . . , \ \mathbf { x } _ { n }$ be a random sample from a population with mean vector $\mu$ and covariance matrix $\Sigma .$ . The sample mean x¯ and sample covariance matrix S are

$$
\bar {\mathbf {x}} = \frac {1}{n} \sum_ {j = 1} ^ {n} \mathbf {x} _ {j}, \mathbf {S} = \frac {1}{n - 1} \sum_ {j = 1} ^ {n} \left(\mathbf {x} _ {j} - \bar {\mathbf {x}}\right) \left(\mathbf {x} _ {j} - \bar {\mathbf {x}}\right) ^ {\mathrm{T}}
$$

Given an m-dimensional vector $\mathbf { v } ,$ the Mahalanobis distance between v and x¯ is defined as [19]

$$
d = (\mathbf {v} - \bar {\mathbf {x}}) ^ {\mathrm{T}} \mathbf {S} ^ {- 1} (\mathbf {v} - \bar {\mathbf {x}})\tag{10}
$$

The larger the value of the Mahalanobis distance for a vector v is, the more likely the vector is a multivariate outlier.

One can think of the independent variables as defining a multidimensional space in which each observation can be plotted. Also, one can plot a point representing the means for all independent variables. This <sup>b</sup>mean point<sup>Q</sup> in the multidimensional space is also called the centroid. The Mahalanobis distance is the distance of a vector from the centroid in the multidimensional space, defined by the independent variables. If the independent variables are uncorrelated, it is the same as the simple Euclidean distance. Thus, this measure provides an indication of whether or not an observation is an outlier with respect to the independent variable values.

The Mahalanobis distance takes the sample variability into account. Instead of treating all values equally when calculating the distance from the centroid, it weighs the differences by the range of variability in the direction of the sample point. Therefore, the Mahalanobis distance constructs a space that weighs the variation in the sample along the axis of elongation less than in the shorter axis of the group ellipse. This concept becomes much clearer when referring to the

![](/api/attachments/FMZYSV2R/fulltext/images/98d745a456170639577aa7ed5ad34b0c314edcce3dd886f5e5edcf2de57fc9ea.jpg)  
Fig. 1. Mahalanobis distance vs. Euclidean distance.

Mahalanobis boundary that has been superimposed on Fig. 1. In terms of Mahalanobis measurements, sample o2 will have a substantially small distance to the mean than sample o1 since it lies along the axis of the group that has the largest variability. Thus, sample o1 is more likely to be an outlier.

Mahalanobis distances are calculated in units of standard deviation from the group mean. Therefore, the calculated circumscribing ellipse formed around the training data actually defines the one standard deviation boundary of that group. This allows the designing of a statistical probability to that measurement. In theory,<sup>1</sup> samples that have a Mahalanobis distance larger than 3 have a probability less than 0.01. These samples can be classified as non-members of the group. Samples that have distances less than 3 are then classified as members. The determination of the cutoff value (threshold) depends on the application and the type of samples.

## 4. Factor-analysis based anomaly detection and clustering algorithm

Factor analysis can be used to identify outliers from an orthogonal factor model. Given a dataset X representing a sample of an unknown population, factor analysis on X provides a mathematical model that characterizes the statistical properties of the population by a set of common factors. Any data point that is not from the same population as X will not fit the model. Such a data point is considered as an outlier of X. To determine whether a data point, say v, is an outlier, we need to test whether or not v fits the model. We propose to use Mahalanobis distance to perform the test because it uses a simple geometric approach to measure the fitness of v to the model. The test is performed in two steps. First $\nu \mathrm { { s } }$ factor scores are computed based on the common factors of X. Second, the Mahalanobis distance between v’s factor scores and $\mathbf { X } \mathbf { \hat { s } }$ factor scores is computed and used to determine whether v is an outlier or not. From (10), we can see that only $\mathbf { S } ^ { - 1 }$ and x¯ of X’s factor scores are needed for calculating Mahalanobis distance of $\nu ,$ and both are determined once X is given. From the discussion in this section, we will see that $\mathbf { S } ^ { - 1 }$ has non-zero values only for its diagonal elements. In summary factoranalysis based outlier detection has following features. 1) It captures the characteristics of the population, from which the dataset X is drawn, by a mathematical model. Once the model is established, X can be discarded and only a set of common factors are kept. 2) Based on the obtained factor model, it examines the fitness of a data point to the model by a simple geometric Mahalanobis distance that requires only a small set of values are kept for calculation.

Network anomaly detection, by nature, aims at identifying any abnormal events that are obviously different from the profile of normal behaviors of protected targets(s) such as a server. Therefore, the factor analysis is suitable for the network anomaly detection. In this section, we first present a factoranalysis based method for the network anomaly detection. Then we argue that factor analysis provides a natural way of clustering the anomalies and present an anomaly cluster method. Hence, the proposed algorithm not only identifies attacks but categorizes them into clusters. In the case of a new attack, the cluster information can guide the intrusion response system to react to it promptly.

## 4.1. Factor-analysis based anomaly detection

The factor-analysis based anomaly detection proceeds in two steps:

1. For a training data set ${ \bf X } { = } { \left[ { \bf x } _ { 1 } { \bf x } _ { 2 } . . . { \bf x } _ { n } \right] } ^ { \mathrm { T } }$ of normal network activities, we estimate the factor loadings, or factor model in (5) (6) (7), and then estimate the factor scores of the training data set by (9).

2.. Given a test sample v, its factor score is computed by (9) and compared with the factor scores of X by Mahalanobis distance. If the distance is larger than a predefined threshold, v is considered as an anomaly (or outlier); otherwise, it is not.

One of the important properties of the factors $F _ { 1 } , F _ { 2 } , \ldots , F _ { p }$ is that they are independent. As the original random variables in a sample may be correlated, the patterns of X will not be easily captured. With the orthogonal factor model, the factor analysis helps reduce the attribute space from a large number of variables $X _ { 1 } , \ X _ { 2 } , \ldots , \ X _ { m }$ to a smaller number of common factors $F _ { 1 } , F _ { 2 } , \ldots ,$ $F _ { p }$ . The characteristics of the unknown population from where X is drawn can be better captured by the factor scores. Thus it is more effective to perform anomaly analysis from the factor scores of X.

Fig. 2 shows the two procedures of the factoranalysis based anomaly detection algorithm. We assume that a collection of normal events of a protected target have been obtained and represented as a matrix X.

The model construction procedure, shown in Fig. 2(a), performs factor analysis on X to obtain the factor model and factor scores. In the figure, $\mathbf { X _ { z } }$ is obtained by subtracting the column mean from each column of X. F<sup>ˆ</sup> and L<sup>ˆ</sup> represent the factor scores and loadings, respectively. f<sup>¯</sup> and $\bf { S _ { f } }$ represent the sample mean and covariance matrix of the factor scores F<sup>ˆ</sup>.

The anomaly identification procedure, shown in Fig. 2(b), evaluates the <sup>b</sup>similarity<sup>Q</sup> of a test event to the model of normal events by Mahalanobis distance and judges whether it is an anomaly or not. $\hat { \boldsymbol { \mathrm { f } } } _ { \nu }$ denotes the factor scores of the test vector $\mathbf { v } - { \bar { \mathbf { X } } } ,$ and $d _ { \nu }$ represents the Mahalanobis distance from $\hat { \boldsymbol { \mathrm { f } } } _ { \nu }$ to the center point of F<sup>ˆ</sup>.

## 4.2. Factor-analysis based anomaly clustering

A closely related issue of the intrusion detection systems is how well their detection results can help the intrusion-response system. Most research efforts input: a data matrix X representing a training data set of normal activities $\mathbf { X } = \left[ \mathbf { x _ { 1 } } \mathbf { x _ { 2 } } \cdots \mathbf { x _ { n } } \right] ^ { l }$ output: the sample covariance matrix S, factor loadings L, and factor scores of X.

1. Compute sample covariance matrix of X: $\mathbf { S } = \mathbf { X _ { \boldsymbol { z } } } ^ { \mathrm { ~ r ~ } } \times \mathbf { X _ { \boldsymbol { z } } } / n - 1$ where ${ \bf X } _ { z } = ( { \bf x } _ { 1 } - \overline { { \bf x } } , { \bf x } _ { 2 } - \overline { { \bf x } } , . . . , { \bf x } _ { n } - \overline { { \bf x } } ) ^ { T }$

2. Do spectral decomposition of S to get its eigenvalue-eigenvector pairs: $\mathbf { S } = \mathbf { V } \ast \mathbf { \mathbf { \Omega } } \mathbf { A } \ast \mathbf { V } ^ { \mathbf { \Omega } }$

3. Pick the p principal factors. An ad hoc rule to choose p is $\sum _ { i = 1 } ^ { P } { \lambda _ { i } } / \sum _ { i = 1 } ^ { m } { \lambda _ { j } } = 8 5 \%$

4. Compute the factor scores of $\mathbf { X } _ { z }$ $\hat { \Phi } = \left[ \hat { \mathbf { f } } _ { 1 } , \hat { \mathbf { f } } _ { 2 } , \cdots \hat { \mathbf { f } } _ { n } \right] ^ { r } = \mathbf { X } _ { z } \hat { \mathbf { L } } ( \hat { \mathbf { L } } ^ { T } \hat { \mathbf { L } } ) ^ { - 1 }$ where $\hat { \bf L } = \left[ \sqrt { \hat { \lambda } _ { 1 } } \hat { \bf e } _ { 1 } , \sqrt { \hat { \lambda } _ { 2 } } \hat { \bf e } _ { 2 } , \cdots , \sqrt { \hat { \lambda } _ { p } } \hat { \bf e } _ { p } \right]$

5. Compute the sample factor mean ī and covariance matrix $\mathbf { S _ { f } }$ of $\hat { \Phi } : \bar { \mathbf { f } } = \frac { 1 } { n } \sum _ { j = 1 } ^ { n } \hat { \mathbf { f } } _ { j }$ ${ \bf S _ { f } } = \hat { \Phi } ^ { T } \hat { \Phi } / n - 1$

## (a) Procedure for model contructions

input: a sample vector v representing a test event, threshold for Mahalanobis distance $\dot { d }$ output: decision on v

1. Compute the factor scores of v: $\hat { \mathbf { f } } _ { \nu } = ( \hat { \mathbf { L } } ^ { T } \hat { \mathbf { L } } ) ^ { - 1 } \hat { \mathbf { L } } ^ { T } ( \mathbf { v } - \overline { { \mathbf { x } } } )$ , where x is the column mean of X.

2. Compute Mahalanobis distance of v: $d _ { \nu } = ( \hat { \mathbf { f } } _ { \mathrm { \mathbf { v } } } - \overline { { \mathbf { f } } } ) ^ { \mathrm { T } } \mathbf { S } _ { \mathbf { f } } ^ { - 1 } ( \hat { \mathbf { f } } _ { \mathrm { \mathbf { v } } } - \overline { { \mathbf { f } } } )$

3. if $d _ { \nu } > d$ , v is an abnormal event, otherwise, v is an normal event

(b) Procedure for anomaly identification

Fig. 2. Factor-analysis based anomaly detection.

on intrusion detection focus on efficient detection techniques, while few of them consider how to associate intrusion detection to intrusion response so that the detection results can provide guidance to intrusion response. The paper aims to bridge this gap.

In this section, we investigate an anomaly clustering scheme that groups attacks with similar <sup>b</sup>abnormality<sup>Q</sup> into the same cluster. The motivation behind the attack clustering is to provide insights into the mechanisms of a new attack and to aid intrusion-response system by providing potential counter-attack strategies.

Dealing with new attacks is a difficult task for the intrusion-response system (IRS). When a new attack is detected, the IRS is under the high pressure to thwart the attack as quickly as possible, in order to prevent it from further penetrating and infesting the entire network. However, the investigation of the new attack mechanism is often timeconsuming. Without the knowledge of an attack mechanism, it would be difficult for the IRS to work effectively.

When grouping attacks by <sup>b</sup>abnormality<sup>Q</sup>, anomaly clustering may provide clues for possible underlying mechanisms of a newly discovered attack, and it can also help the IRS perform potential counter-attack strategies. For instance, in the face of a new attack, before the IRS is able to trace it and analyze it, the intrusion response procedure of a known attack that is in the same cluster as the new attack can be chosen and adjusted to respond to the attack. Different schemes have been proposed for attacks clustering. One popular approach categorizes attacks into Denial of Service (DoS), Probe, Remote to Local (R2L), Local to Root (L2R), etc. This scheme may not help attack response very well due to its incoherent clustering criteria. For instance, it clusters DoS attacks by the attack effect, Probe attacks by attack purpose, and R2L and L2R attacks by the attack origin and target. In addition, the scheme might be too coarse in that attacks belonging to the same cluster, say R2L, differentiate greatly in attack mechanisms. Thus a finer clustering scheme is needed.

Ideally, we would like to cluster attacks by attack mechanisms, so that in the face of a new attack, we can employ a known attack’s response procedure to thwart it. However, it is almost impossible to cluster new attacks by their attack mechanisms without knowing them.

This paper investigates an alternative clustering scheme which classifies attacks based on their factor scores <sup>b</sup>abnormality<sup>Q</sup>. Without loss of generality, an audit record can be viewed as a tuple of values of the observed or derived features. Each feature has its domain of normal values. An attack, if detectable, must have some abnormal feature values. Thus, abnormality here is identified by an attack’s abnormal features. The motivation behind anomaly clustering is that attacks of the same cluster share the similar <sup>b</sup>abnormality<sup>Q</sup> and may be treated by the similar intrusion-response procedures. Thus the clustering can help select effective intrusion response especially when new attacks appear. It is worth pointing out that anomaly clustering aims at aiding the intrusion-response system by providing a reasonable intrusion-response procedure to thwart a new attack.

In the factor-analysis based outlier detection algorithm, the normality of an event v is determined based on the Mahalanobis distance ${ \bf d } _ { \bf v } { = } { \left( { \bf v } - { \bf X } \right) } ^ { \mathrm { T } }$ ${ \mathbf { S } _ { \mathrm { f } } ^ { - 1 } } ( \mathbf { v } { - \mathbf { X } } )$ from v to X in the factor space. Since factors are mutually independent, the sample covariance S of the factor scores of X is a diagonal matrix with $s _ { i j } { = } 0$ if ipj and $\scriptstyle { s _ { i j } = \sigma _ { i } ^ { 2 } }$ if $i { = } j .$ . Here $\bar { \boldsymbol { \sigma } } _ { i } ^ { 2 }$ is the sample variance of the ith factor. So Eq. (10) can be rewritten as

$$
d _ {v} = \left(\mathbf {v} - \bar {\mathbf {x}}\right) ^ {\mathrm{T}} \mathbf {S} _ {\mathbf {f}} ^ {- 1} (\mathbf {v} - \bar {\mathbf {x}}) = \sum_ {i = 1} ^ {m} \frac {\left(v _ {i} - \bar {x} _ {i}\right) ^ {2}}{\sigma_ {i} ^ {2}}\tag{11}
$$

(11) shows that the Mahalanobis distance is determined by normalized factor scores. If the normalized factor score of v on an individual factor is abnormally big, it is more likely abnormal. Thus, a natural approach to clustering anomalies is to group them by the abnormal factor scores. As each factor represents a combination of a set of features (or attributes), an anomaly with the abnormal score on a factor, say $F _ { i } ,$ suggests that its abnormality be related to the set of features associated with $F _ { i } .$ . Hence, it is reasonable to assume that two anomalies may have the similar attack mechanisms if both have the abnormal factor scores of the same factor. Anomalies are clustered as simple anomalies or composite anomalies.

Definition 1. Simple anomalies have abnormal factor scores on only one factor. Composite anomalies have abnormal factor scores on more than one factor.

The factors are indexed in the descending order of their variances. The 1st factor is the one with the largest variance, and the 2nd factor is one with the second largest variance, and so on. Simple anomalies can be further categorized as 1st anomalies, 2nd anomalies, and so on, denoted as F-1 anomalies,

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
input: a set of attacks, thresholds for factor scores  $m_{i}, i = 1, 2, \ldots, p$ 

output: clusters of attacks

1. for each attack v

2. compute the factor scores of v:  $\hat{\mathbf{f}}_{v} = (\hat{\mathbf{L}}^{T} \hat{\mathbf{L}})^{-1} \hat{\mathbf{L}}^{T}(\mathbf{v} - \overline{\mathbf{x}})$ ,

3. compute Mahalanobis distance of v:

 $d_{v} = (\mathbf{v} - \overline{\mathbf{x}})^{\mathrm{T}} \mathbf{S}_{\mathrm{f}}^{-1}(\mathbf{v} - \overline{\mathbf{x}}) = \sum_{i=1}^{m} (v_{i} - \overline{x}_{i})^{2} / \sigma_{i}^{2}$ 

4.  $\Theta = \Phi$ 

5. for  $i = 1, \ldots, p$ 

6. if  $v_{i} &gt; m_{i}$ 

7.  $\Theta = \Theta \cup i$ 

8. label v with  $C_{\Theta}^{|\Theta|}$
</div>

Fig. 3. Factor-analysis based anomaly clustering.

F-2 anomalies, etc. An anomaly is classified as $F { - } i$ if it has abnormal big factor scores only on the ith factor. Composite anomalies are denoted as $C _ { \theta } ^ { k }$ where k represents the number of factors and H denotes a set of factors on which anomalies have abnormal factor scores.

We characterize and cluster attacks by the abnormal factor scores. Attacks of the same cluster share the similar <sup>b</sup>abnormality<sup>Q</sup>. Fig. 3 shows the factoranalysis based anomaly clustering method. Step 6 examines whether a factor score is abnormally large or not, and $m _ { i }$ is the threshold for the normal factor scores of ith factor. A variety of methods can be used to specify $m _ { i } .$ . In this paper, $m _ { i }$ is defined as the maximum normal factor scores of the i-th factor.

## 5. Experiments

The proposed algorithms have been tested for network intrusion detection. Given a dataset (so-called reference data) containing only normal TCP/IP connections and a test dataset containing some attacks in it, the algorithms are employed to learn the property of the normal activities in the training data by factor analysis, and then to detect abnormal activities in the test data. The performance of the algorithm is evaluated based on the detection rate, missed attack rate, and false alarm rate. The detection rate is measured as the percentage of attacks detected by the algorithm as abnormal events; the missed attack rate as the percentage of attacks missed by the algorithm; and the false alarm rate as the percentage of normal activity mistaken as abnormal ones by the algorithm. The experiments are based on DARPA Intrusion Detection Evaluation Data.

## 5.1. DARPA intrusion detection evaluation data

DARPA Intrusion Detection Systems (IDS) Evaluation project is the first effort to provide data and methodology for off-line evaluation of intrusion detection systems. It was conducted by the Information System Technology Group of MIT Lincoln Laboratory, under DARPA ITO and Air Force Research Laboratory sponsorship. Details information can be found in [8]. The project started from 1998 and continued in 1999. Today DARPA data sets are widely used as the benchmark for IDS evaluation. 1998 DARPA evaluation data contains 7 weeks of training data and 2 weeks of test data. 1999 DARPA evaluation data contains 3 weeks of training data and 2 weeks of test data. Attacks in all training data are labeled. The test datasets of 1999 Evaluation contains of two parts collected at a gateway inside the mimic subnet and one outside the subnet respectively. Both training and test data are provided in several forms: UNIX BSM, tcpdump, and NT Data. We use tcpdump data for analysis.

## 5.2. Detecting abnormal activities of network traffic

## 5.2.1. Experiment setup

Configuration of the experiments is shown as following:

<sup>!</sup> Selection of the training data: We construct an attack-free dataset from 1998 training data by removing all the labeled attacks. We use it as the reference data of normal activity and then apply the algorithm on 1999 test data to detect abnormal activities that do not comply with the property of the reference data.

<sup>!</sup> Preprocessing of data: For a network traffic dataset, a connection record is generated for each TCP/IP connection based on a predefined schema R={Ts, src.ip, src.port, dst.ip, dst.port, service, flag}.

Ts gives the starting time of a connection. src.ip and src.port are source IP and port of a connection. dst.ip and dst.port are destination IP and port. service gives the protocol type used in a connection such as ftp, smtp, etc. flag gives the status of a connection which can be open, close, reset, etc. A connection record is obtained only from the header of a TCP/IP connection.

Before performing anomaly detection, the association rule mining is applied as the preprocessing

Table 1

procedure on the connection records. Then we perform anomaly detection and clustering on the association rules. Although the association rules can be directly used for identifying the anomaly [2,3], this work treats association rules as a condensed form of the audit data and uses them as the input of factoranalysis based anomaly detection and clustering algorithm. The advantage of using association rules rather than raw audit data is that the behavior patters in the audit data are better represented by them. An association rule describes a common property shared by a set of connections, while the occurrence of an individual connection is often arbitrary and can tell little about the property of other connections. For instance a connection record of the form (src.ip:129.174.111.3, src.port:3167, dst.ip:73.8.19.5, dst.port: 23, service: telnet, time: 15:23:12) just describes a fact that there is a telnet connection from 129.174.111.3:3167 to 73.8.19.5:23 at the time 15:23:12. However an association rule of the form src.ip:129.174.111.3Ydst.ip:73.8.19.5, dst.port: 23, service: telnet, duration: 15:20:49–15:29:03 [support=1000] reveals an interesting pattern worthy of further investigation.

Three data mining algorithms are used including single-level association mining, multi-level association mining and feature selection. The rule set obtained by each mining algorithm captures the different characteristics of the data. Each rule set is then translated into a set of vectors, which is represented by a matrix. Three matrixes are generated, one from each mining algorithm. The factor scores and associated factor loadings are then computed for each matrix. Details of the mining algorithms and the way to translate rules into vectors can be found in [2,3]. For instance, the association rule of the above example is translated into the vector {23, telnet, 494, 1000}, the fields of which correspond to the dst.port, service, duration, support respectively. For conven ience, each service type is designated with a unique index number. The service type telnet in the vector will be replaced with its index instead.

For the attack-free reference data, the factor loadings are computed and used as a model to describe normal activity patterns in the reference data. For the test data, the factor scores of each matrix are computed, and for each test vector v, the Mahalanobis distance between v and the centroid of the training data is computed. If the distance exceeds a predefined threshold, then the test vector is considered as abnormal.

## 5.2.2. Experimental result

5.2.2.1. Anomaly detection. Table 1 shows the detection results on 1999 DARPA inside dataset and outside dataset, which are collected from an inside router and outside router of a simulated network. The significance level is chosen as d=10. Each table contains the results of the test matrixes generated from the mining algorithms. singleLevel refers to the matrix generated from the single-level association rule algorithm, multiLevel refers to one generated from the multi-level association rule algorithm, and featureSelect refers to one generated from the feature selection algorithm. Size gives the total number of test vectors in a matrix; trueNo gives the number of real attacks detected by the algorithm. dRate gives the attack detection rate defined as dRate/(trueNo+missedNo). falseNo gives the number of false alarms. fRate gives the false alarm rate defined as falseNo/ (size-trueNo-missedNo). missedNo gives the number of attacks in the test data are missed by the algorithm; mRate gives the missed attack rate defined as (1-dRate). The sum of trueNo and falseNo is the total number of alarms generated by the algorithm. The sum of trueNo and missedNo is the total number of real attacks in the test data.

From Table 1, we can see that detection results on multiLevel and featureSelect matrixes are better than that on singleLevel matrix. The latter has a higher rate of false detection and missed attacks, and contributes most false alarms and missed attacks to the overall result. One reason is that the entire anomaly detection process is based on connection records, which contains information only from headers of TCP/IP connections. When abnormality of an attack activity is not shown in the header but in the payload of a TCP/ IP connection, the mining algorithms cannot capture them. Using only header information of a connection makes data preprocess faster and easier to handle high-speed network traffic, however, at the risk of losing information of the payload. Another reason is that patterns extracted from the mining algorithms are not able to distinguish some attacks from normal activity. DARPA only published limited performance results of the top systems, and they are mainly detection rate and false alarm rate. Our results are comparable to the top performed anomaly detection system, ADAM, of 1999 DARPA IDS Evaluation contest: it has the same detection rate, but its false alarm rate is slightly higher.

Detection results on 1999 DARPA test data

<table><tr><td>Test data</td><td>Size</td><td>trueNo/dRate</td><td>missedNo/mRate</td><td>falseNo/fRate</td></tr><tr><td colspan="5">(a) Experimental results on 1999 inside data</td></tr><tr><td>SingleLevel</td><td>4055</td><td>18/79%</td><td>5/23%</td><td>47/1.1%</td></tr><tr><td>MultiLevel</td><td>510</td><td>4/100%</td><td>0/0%</td><td>6/1.2%</td></tr><tr><td>FeatureSelect</td><td>786</td><td>5/100%</td><td>0/0%</td><td>2/0.25%</td></tr><tr><td>Total</td><td>5351</td><td>27/84.4%</td><td>5/15.6%</td><td>53/1%</td></tr><tr><td colspan="5">(b) Experimental results on 1999 outside data</td></tr><tr><td>SingleLevel</td><td>5296</td><td>15/80%</td><td>5/20%</td><td>49/0.8%</td></tr><tr><td>MultiLevel</td><td>421</td><td>2/100%</td><td>0/0%</td><td>0/0%</td></tr><tr><td>FeatureSelect</td><td>654</td><td>8/80%</td><td>0/0%</td><td>2/20%</td></tr><tr><td>Total</td><td>6371</td><td>25/83%</td><td>5/17%</td><td>51/0.8%</td></tr></table>

Table 2 gives attack distribution in both inside and outside data, along with the names and number of detected attacks.<sup>2</sup> The first two columns Name and attackNo give the name and number of an attack in a test data, and detectedNo gives the number of a specific kind of attacks detected by the algorithm.

Fig. 4 visualizes the factors obtained from the normal featureSelect data. The X-axis represents the original variables, the Y-axis presents the values of the variables. There are six original variables, and factor analysis discovers four hidden factors. Factor-1 shows that the 2nd and 3rd variables are negatively correlated, and they both are weakly related to the rest variables. Similarly, factor-2 shows that the 5th and 6th variables are negatively correlated, and they both are weakly correlated with the rest variables. Factor-3 shows that the 1st variable is positively correlated with the 4th variable but negatively correlated with the 2nd and 5th variables. Factor-4 shows that both 4th and 5th variables are positively correlated.

Fig. 4 also explains the idea behind factor-analysis based anomaly detection. Factors of a given dataset are the hidden variables that each sample is linearly dependent on. Each factor describes a specific property about correlations among the original variables of the normal data. Intuitively, an anomaly does not come from the same population as the normal data, thus it is very likely to violate these correlations. One way to identify an anomaly is the Mahalanobis distance. The Mahalanobis distance of a test sample measures how similar it is to a set of normal samples. A test sample with a large distance value is likely to be an anomaly. For brevity, we do not show the factors of singleLevel and multiLevel data here.

Table 2  
Attack distribution of 1999 test data

<table><tr><td>Name</td><td>attackNo</td><td>detectedNo</td></tr><tr><td colspan="3">(a) Attack distribution of the inside data</td></tr><tr><td>Apache2</td><td>4</td><td>3</td></tr><tr><td>Back</td><td>2</td><td>1</td></tr><tr><td>Dict</td><td>1</td><td>1</td></tr><tr><td>Guessftp</td><td>1</td><td>0</td></tr><tr><td>Guesspop</td><td>1</td><td>0</td></tr><tr><td>Mailbomb</td><td>2</td><td>2</td></tr><tr><td>Neptune</td><td>3</td><td>3</td></tr><tr><td>Pod</td><td>3</td><td>2</td></tr><tr><td>Portsweep</td><td>3</td><td>3</td></tr><tr><td>Process</td><td>3</td><td>3</td></tr><tr><td>Satan</td><td>1</td><td>1</td></tr><tr><td>Smurf</td><td>4</td><td>4</td></tr><tr><td>Teardrop</td><td>1</td><td>1</td></tr><tr><td>Telnet</td><td>1</td><td>1</td></tr><tr><td>Udpstorm</td><td>2</td><td>2</td></tr><tr><td>Total</td><td>32</td><td>27</td></tr><tr><td colspan="3">(b) Attack distribution of the outside data</td></tr><tr><td>Apache2</td><td>2</td><td>1</td></tr><tr><td>Back</td><td>3</td><td>2</td></tr><tr><td>Crashiis</td><td>1</td><td>0</td></tr><tr><td>Guessftp</td><td>1</td><td>0</td></tr><tr><td>Guesspop</td><td>1</td><td>0</td></tr><tr><td>Ipsweep</td><td>1</td><td>1</td></tr><tr><td>Mailbomb</td><td>3</td><td>3</td></tr><tr><td>Neptune</td><td>4</td><td>4</td></tr><tr><td>Pod</td><td>3</td><td>3</td></tr><tr><td>Portsweep</td><td>3</td><td>3</td></tr><tr><td>process</td><td>1</td><td>1</td></tr><tr><td>Satan</td><td>1</td><td>1</td></tr><tr><td>Smurf</td><td>2</td><td>2</td></tr><tr><td>Teardrop</td><td>1</td><td>1</td></tr><tr><td>Telnet</td><td>3</td><td>3</td></tr><tr><td>Total</td><td>30</td><td>25</td></tr></table>

Fig. 5 shows factor scores distribution of normal singleLevel data and attacks. Fig. 5(a) shows the distributions on the 1st and 2nd factors, and Fig. 5(b)

![](/api/attachments/FMZYSV2R/fulltext/images/97eeac0f2a92f5e4b8ff4d2bc42012145e5415c2505e6db4b5e736a064a2e17e.jpg)  
Fig. 4. Factors of featureSelect data.

shows that on the 2nd and 3rd factors. The bar on the lower left corner of each figure represents the factor scores of normal data, while the dots represent attacks including neptune, portsweep, satan, and udpstorm.<sup>3</sup> We can see that these attacks are distinguishable from the normal data as their factor scores deviate far from those of normal data. Due to space limit, we do not show all distribution figures here, but they are all similar to Fig. 5.

5.2.2.2. Anomaly clustering. Table 3 shows anomaly clustering of the DARPA data. Six clusters are generated. Three of them are from single-level attacks, one from multi-level attacks, and two from featureselection attacks. The multi-level attacks and featureselection attacks are well clustered. For attacks detected by feature selection programs, portsweep and satan attacks are categorized to the same cluster $C _ { ( 1 , 3 , 4 ) } { } ^ { 3 }$ because both are involved in heavy port scanning activities, and ipsweep attacks are clustered to a different cluster. Here, the cluster $C _ { ( 1 , 3 , 4 ) } { } ^ { 3 }$ represents that its members have anomaly values on the 1st, 3rd, and 4th factors of featureSelection data. Note that one of the singleLevel clusters is also denoted as $C _ { ( 1 , 3 , 4 ) } { } ^ { 3 }$ , but it denotes anomalies on different factors—the factors of singleLevel data. Attacks detected by multiLevel algorithm contain only smurf attacks, and they are categorized as one cluster.

As to singleLevel attacks, neptune, portsweep, satan,<sup>4</sup> and udpstorm attacks are grouped to a same cluster, and it is reasonable because they all share a common property even though they target on different network services: incurring a large number of connections during a short period of time. If a new attack is found belonging to this cluster, before its attack mechanism is studied, a possible response strategy is to shut down the targeted network service at the cost of denying service to legitimate users.

For the cluster $\bar { C } _ { ( 1 , 3 , 4 ) } { } ^ { 3 } ,$ both back and apache target against an apache server; mailbomb and process attacks (in DARPA) target against a mail server. All these attacks also share a similarity: their goals are to make the victim slow down and eventually crash. Thus all these attacks are observed to have a large number of abnormally long duration connections. If a new attack is found to belong to this cluster, a possible response strategy is to close the connections that have long connection time. In addition, the attack investigation effort should first focus on examining the status of system stacks, memory, and protocol vulnerabilities of the targeted service.

For the cluster $C _ { ( 3 , 4 ) } ^ { 3 }$ , both dict and telnet belong to password guessing attacks and target on the telnet service, while teardrop exploits a flaw in the implementation of older TCP/IP stacks that cannot handle overlapping IP fragments, and pod exploits a flaw in some ICMP implementations that cannot handle packets longer than 64 KB. These attacks share little similarity. Thus the cluster $C _ { ( 3 , 4 ) } ^ { 3 }$ fails to characterize these attacks which should be grouped into at least two clusters: one for dict and telnet, the other for teardrop and pod. The possible reason for failures of $C _ { ( 3 , 4 ) } ^ { 3 }$ is that the collected features of audit records, used to describe the normal behavior patterns, are not sufficient to distinguish certain single-level attacks. One solution is to increase more features in the audit data. The problem of feature selection for attack detection and clustering is the future work of this research.

![](/api/attachments/FMZYSV2R/fulltext/images/121edb7b5d547b5650a2b4f39b19b0c7f3b326d7ac9010fef12b93bc07fc763a.jpg)

![](/api/attachments/FMZYSV2R/fulltext/images/5d2721087b07fb71965357a4dde8310fdf2ebc2ab23e7e8082d580a19894d60f.jpg)  
Fig. 5. Factor scores distribution of both normal data and attacks.

## 6. Related work

A variety of techniques have been exploited in anomaly detection including data mining, machine learning and neural networks, specification-based approaches, computer immunology, information-theoretic measures, and statistical methods. In this section, we first give a brief overview of different approaches to anomaly detection. Then we focus on the related research work that applies data mining and statistical techniques in anomaly detection.

Teng et al. proposed a time-based inductive machine to generate rule-based sequential patterns to characterize users’ behavior over time [25]. The approach uses a rulebase to store profile patterns of users’ activities. Anomalies are identified whenever they are significantly different from those specified in the rulebase. Lane et al. proposed to build user profiles based on command sequences [17]. The current input sequence is compared with the profile using a similarity measure to find abnormal activities.

Table 3 Anomaly clusters

<table><tr><td>Algorithm</td><td>Clusters</td><td>Attacks</td></tr><tr><td rowspan="3">singleLevel</td><td> $1 \ C_{(1,3,4)}^{2}$ </td><td>Neptune, portsweep, satan, udpstorm</td></tr><tr><td> $2 \ C_{(1,3,4)}^{3}$ </td><td>Apache, back, mailbomb, process</td></tr><tr><td> $3 \ C_{(1,3,4)}^{2}$ </td><td>Dict, pod, teardrop, telnet</td></tr><tr><td>multiLevel</td><td> $1 \ C_{(1,3,4)}^{3}$ </td><td>Smurf</td></tr><tr><td rowspan="2">featureSelection</td><td> $1 \ C_{(1,3,4)}^{3}$ </td><td>Portscan, satan</td></tr><tr><td> $2 \ C_{(1,3,4)}^{2}$ </td><td>Ipsweep</td></tr></table>

Neural network has been used in several systems. [7] employs a back-propagation network to detect anomalous and unknown intrusions against a software system. [30] realizes a hierarchical intrusion detection system using a statistical processor to maintain a reference model of normal network activities and a neural network classifier to detect abnormal ones.

Inspired by the biological immune system’s ability to distinguish self from non-self, Forrest et al proposed a computer immunological method for anomaly detection [5]. The approach defines self as a collection of all the known <sup>b</sup>good<sup>Q</sup> sequences of system calls, and then these <sup>b</sup>self<sup>Q</sup> sequences are used for live monitoring to detect the non-self sequences that are potential intrusions. Further improvements on the computer immunology method are done by (1) allowing for variable length <sup>b</sup>self<sup>Q</sup> sequences to enhance the system’s flexibility and performance [28]; and (2) using an automaton to represent programs’ normal behaviors so as to accommodate more information about the programs’ normal behaviors and meanwhile to improve system’s performance [23].

Specification-based approaches are generally based on manually developed specifications of legitimate system behaviors. [15,16] use traces, ordered sequences of execution events to specify the intended behaviors of concurrent programs in distributed systems. A specification describes valid operation sequences in the execution of one or more programs. [14] employs state-machine specifications of network protocols and augments these state machines with information about necessary statistics to detect anomalies. [27] enhances the specification-based approach by automatically generating the specification of a program by deriving an abstract model of the programs from the source or binary code. Information theoretic measures were proposed and used to help understand the characteristics of audit data and build anomaly detection models [18].

In the past several years, data mining techniques have attracted a lot of attentions in the area of intrusion detection because of two reasons: (1) many data mining techniques are well suited for the needs of intrusion detection; and (2) from the data analysis point of view, the task of intrusion detection is closely related to data mining, and the entire process of intrusion detection is generally involved in some of the following operations: audit trail data preprocessing, audit data analysis, pattern extraction for attacks, <sup>b</sup>normal<sup>Q</sup> activity, and so on. ADAM is a network anomaly detection system [2,3] developed by the author. It employs an association rule mining module to learn system profile and to capture suspicious patterns of network traffic. A classification module is used to learn the output of mining module so as to further reduce the false alarms and assign right names to known attacks. The work of this paper differs from ADAM in 3 aspects. First, it uses association rule mining as a preprocessing procedure while ADAM uses it as the core method for anomaly detection. The relation between the two is that this work uses ADAM as its preprocessing module. Second, the factor-analysis based method possesses the capability of anomaly clustering while ADAM does not. Third, the factor-analysis based method is able to identify and remove redundant features in the audit data, and this makes its detection more efficient.

Helmer et al. present a distributed intrusion detection system that uses data mining agents to automate discovery of concise rules from system call traces [10]. Data mining techniques have also been used in alarm analysis. S. Manganaris et al. proposed to use association rules to detect anomaly on the IDS alarm stream [20]. Julish et al. proposed an alarm clustering algorithm to manage intrusion detection alarms by identifying and resolving their root causes [12] and a conceptual clustering technique to mine historical alarms so as to handle future alarms more effectively [13]. Klemettinen designed an alarm correlation system that uses association rules and frequent episodes algorithms to discover alarm patterns [14].

Statistical models have been widely used in anomaly detection. NIDES [1] and EMERALD [21,22] employ a statistical method to measure the user and system behavior by a number of variables sampled over time, and then build profiles based on the variables of normal behavior. Then the rea variables will be compared against profiles. Deviations are considered as abnormal. Cabrera et al. examined the application of statistical modeling fo detecting novel attacks against computer networks [4]. By using Kolmogorov–Smirnov Test, they demonstrate the difference between normal Telnet connections and attack embedded Telnet connections. Valdes et al. proposed eBayes technique to detect anomaly in network traffic [26]. Defining a session as temporally contiguous bursts of TCP/IP traffic from a given IP, eBayes applied Bayesian inference on observed and derived variables of the session to obtain a belief for the session over the states of hypothesis. Barbara et al. proposed a method based on pseudo-Bayes estimators to detect network anomaly that differs from normal network activity [2]. Pseudo-Bayes is effective in detecting network anomaly; however the parameter selection is an open problem. Ye et al. presented a multivariate quality control technique, based on Hotelling $T ^ { 2 }$ and chi-square distance test, to detect intrusions by building a long-term profile of normal activities and using the norm profile to detect anomalies [29]. Our technique differs from these statistical anomaly detection methods in that it performs anomaly detection in the factor space rather than the original variable space. When the original variables are not mutually independent, our method is more efficient because it analyzes anomaly in a reduced variable space.

## 7. Conclusion

A novel anomaly detection and clustering algorithm based on factor analysis and Mahalanobis distance is presented in this paper. The paper aims to bridge the gap between intrusion detection and intrusion response. The major contribution of this work is to employ factor analysis technique in network anomaly detection and clustering. Factor analysis can characterize the normal network activities by uncovering the latent structure and reduce attribute space to a smaller number of factors. Thus it is more efficient to characterize normal activities and to conduct anomaly detection in the reduced factor space. In addition, factor analysis provides a natural way of clustering the anomaly. The proposed anomaly clustering scheme can be used to guide the intrusion response to new attacks. We tested the algorithm using the DARPA Intrusion Detection System Evaluation data. The experimental results show that the factor-analysis based anomaly detection is able to detect network intrusions with tolerable false alarm rate, and the factor-analysis based clustering is effective in clustering attacks by their abnormal features.

Our future work includes the application of the anomaly clustering algorithm in misuse detection systems, and the investigation of different anomaly clustering techniques and their impact on intrusion response system.

## Acknowledgement

We would like to thank the anonymous reviewers for their very helpful comments and suggestions.

## References

[1] D. Anderson, T.F. Lunt, H. Javits, A. Tamaru, A. Valdes, Detecting Unusual Program Behavior Using the Statistical Component of the Next-generation Intrusion Detection System (NIDES), Technical Report SRI-CSL-95-06, SRI International (May 1995).

[2] D. Barbara, N. Wu, S. Jajodia, Detecting novel network intrusions using bayes estimators, Proceedings of the 1st SIAM Conference on Data Mining.

[3] D. Barbara, J. Couto, N. Wu, S. Jajodia, ADAM: detecting intrusion by data mining, Proceedings of the 2nd Annual IEEE Information Assurance Workshop.

[4] Joao B.D. Cabrera, B. Ravichandran, Raman K. Mehra, Statistical traffic modeling for network intrusion detection, 8th International Symposium on Modeling Analysis and Simulation of Computer and Telecommunication Systems.

[5] S. Forrest, S. Hofmeyr, A. Somayaji, T. Longstaff, A sense of self for Unix processes, Proceedings of IEEE Symposium on Security and Privacy.

[6] A.K. Ghosh, A. Schartzbard, A study in using neural networks for anomaly and misuse detection, Proceedings of USENIX Security Symposium.

[7] A.K. Ghosh, J. Wanken, F. Charron, Detecting anomalous and unknown intrusions against programs, Proceedings of the 14th Annual Computer Security Application Conference.

[8] Joshua W. Haines, Richard P. Lippmann, David J. Fried, Eushiuan Tran, Steve Boswell, Marc A. Zissman, 1999 DARPA intrusion detection system evaluation: design and procedures, MIT Lincoln Laboratory technical report.

[9] J.F. Hair, R. Anderson, R. Tatham, W. Black, Multivariate Data Analysis with Readings, Macmillan, New York, 1992.

[10] G. Helmer, J.S.K. Wong, V. Honavar, L. Miller, Automated discovery of concise predictive rules for intrusion detection, Journal of Systems and Software 60 (2002).

[11] R.J. Johnson, D.W. Wichern, Applied multivariate statistical analysis, Prentice Hall, New Jersey, 1998.

[12] K. Julisch, Mining alarms clusters to improve alarm handling efficiency, Proceedings of 17th Annual Computer Security Applications Conference (Dec. 2001).

[13] K. Julisch, M. Dacier, Mining intrusion detection alarms for actionable knowledge, Proceedings of 8th international conference on knowledge discovery and data mining (July 2002).

[14] M. Klemettinen, A knowledge discovery methodology for telecommunication network data, PhD thesis, University of Helsinky, 1999.

[15] C. Ko, Logic induction of valid behavior specifications for intrusion detection, Proceedings of 2000 IEEE Symposium on Security and Privacy, 2000.

[16] C. Ko, M. Ruschitzka, K. Levitt, Execution monitoring of security-critical programs in distributed systems: a specification-based approach, Proceedings of the 1997 IEEE Symposium on Security and Privacy, 1997.

[17] T. Lane, C.E. Brodley, An application of machine learning to anomaly detection, NIST-NCSC National Information Systems Security Conference, 1997.

[18] W. Lee, D. Xiang, Information-theoretic measures for anomaly detection, Proceedings of 2001 IEEE Symposium on Security and Privacy, 2001.

[19] P.C. Mahalanobis, On tests and measures of groups divergence, International Journal of the Asiatic Society of Benagal 26 (1930).

[20] S. Manganaris, M. Christensen, D. Zerkle, K. Hermiz, A data mining analysis of RTID alarms, Computer Networks 34 (2000).

[21] P. Neumann, P. Porras, Experience with emerald to date, Proceedings of 1st USENIX Workshop on Intrusion Detection and Network Monitoring (Apr. 1999).

[22] P. Porras, P.G. Neumann, Emerald: event monitoring enabling responses to anomalous live disturbances, Proceedings of 19th National Information Systems Security Conference, (Oct. 1997).

[23] R. Sekar, M. Bendre, D. Dhurjati, P. Bollineni, A fast automaton-based method for detecting anomalous program

behaviors, Proceedings of 2001 IEEE Symposium on Security and Privacy, 2001.

[24] R. Sekar, A. Gupta, J. Frullo, T. Shanbhag, A. Tiwari, H. Yang, S. Zhou, Specification-based anomaly detection: a new approach for detecting network intrusions, Proceedings of ACM Conference on Computer and Communication Security (Oct. 2002).

[25] H. Teng, K. Chen, S. Lu, Adaptive real-time anomaly detection using inductively generated sequential patterns, Proceedings of 1999 IEEE Symposium on Security and Privacy, 1999.

[26] A. Valdes, K. Skinner, Adaptive, model-based monitoring for cyber attack detection, Proceedings of 3rd International Workshop on Recent Advances in Intrusion Detection (Oct. 2000).

[27] D. Wagner, D. Dean, Intrusion detection via static analysis, Proceedings of 2001 IEEE Symposium on Security and Privacy, 2001.

[28] M. Dacier Wespi, H. Debar, Intrusion detection using variablelength audit trail patterns, Proceedings of the 3rd Symposium on Recent Advances in Intrusion Detection.

[29] N. Ye, S. Emran, Q. Chen, S. Vilbert, Multivariate statistical analysis of audit trails for host-based intrusion detection, IEEE Transactions on Computers 51 (7) (2002).

[30] Z. Zhang, J. Li, C.N. Manikopoulos, J. Jorgenson, J. Ucles, HIDE: a hierarchical network intrusion detection system using statistical preprocessing and neural network classification, Proceedings of the 2001 IEEE Workshop on Information Assurance and Security, 2001.

![](/api/attachments/FMZYSV2R/fulltext/images/5ce6afcf80d75be42b84a5b2ecd69db3fc1bebb98c4346ebcb4fc76d3f12abdf.jpg)

Ningning Wu is an assistant professor in the Department of Information Science at University of Arkansas at Little Rock. She received a PhD degree in Information Technology from George Mason University in 2001, and MSEE and BSEE degrees from the University of Science and Technology of China in 1995 and 1992, respectively. Her major research interest includes network intrusion detection, information system security, and data mining.

![](/api/attachments/FMZYSV2R/fulltext/images/50c79080812d2d2a0b3d4f6bb313b47000995d495f4cd9d97f217635ff96c30e.jpg)

Jing Zhang received the BSc and MSc degrees, both in Electrical Engineering from the Southeast University, Nanjing, China in 1983 and 1986, respectively, and PhD degree from the Swiss Federal Institute, Zurich, Switzerland in 1996.

He was a lecturer in the Southeast University, China from 1986 to 1991 and a senior engineer in Maxon Motor, AG, Switzerland from 1996 to 2001. He joined the University of Arkansas at Little Rock in

2001, where he is currently an assistant Professor in the Department of Applied Science. His research interests include digital signal processing, control systems and applications in network communication and information system security.
