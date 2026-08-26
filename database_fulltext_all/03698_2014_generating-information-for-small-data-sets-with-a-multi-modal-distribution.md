---
otero_id: 3698
otero_key: "JJMAEGDT"
title: "Generating information for small data sets with a multi-modal distribution"
authors: "Der-Chiang Li; Liang-Sian Lin"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2014.06.004"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Generating information for small data sets with a multi-modal distribution

Der-Chiang Li ⁎, Liang-Sian Lin

Department of Industrial and Information Management, National Cheng Kung University, University Road, Tainan 70101, Taiwan, ROC

## a r t i c l e i n f o

Article history: Received 15 August 2013 Received in revised form 26 February 2014 Accepted 7 June 2014 Available online 16 June 2014

Keywords: Multi-modal distribution Small data set Multi-modal virtual sample Virtual sample size

## a b s t r a c t

Virtual sample generation approaches have been used with small data sets to enhance classi<sup>fi</sup>cation performance in a number of reports. The appropriate estimation of data distribution plays an important role in this process, with performance usually better for data sets that have a simple distribution rather than a complex one. Mixed-type data sets often have a multi-modal distribution instead of a simple, uni-modal one. This study thus proposes a new approach to detect multi-modality in data sets, to avoid the problem of inappropriately using a uni-modal distribution. We utilize the common k-means clustering method to detect possible clusters, and, based on the clustered sample sets, a Weibull variate is developed for each of these to produce multi-modal virtual data. In this approach, the degree of error variation in the Weibull skewness between the original and virtual data is measured and used as the criterion for determining the sizes of virtual samples. Six data sets with different training data sizes are employed to check the performance of the proposed method, and comparisons are made based on the classi<sup>fi</sup>cation accuracies. The results using non-parametric testing show that the proposed method has better classi<sup>fi</sup>cation performance to that of the recently presented Mega-Trend-Diffusion method.

© 2014 Elsevier B.V. All rights reserved.

## 1. Introduction

Companies can gain a competitive advantage by speedily providing new products, but when these are in the pilot run stage there is generally only a small amount of data that can be used to improve their performance, due to <sup>fi</sup>nancial and time limitations. It is thus important to develop analysis methods for use with small data sets, in order to achieve better classi<sup>fi</sup>cation performance [19,20,23,25,28]. Many approaches have been proposed to deal with this issue, with, for example Das and Nenadic [8] and Xu et al. [33] creating algorithms for certain data sets. While this approach is very effective for speci<sup>fi</sup>c classi<sup>fi</sup>ers, the classi<sup>fi</sup>cation is less accurate when the items in the data sets have various characteristics [12]. Other researchers have utilized virtual sample generation (VSG) methods to enlarge data sets, such as those in Yang et al. [34], Li et al. [19] and Li and Lin [21], which all used VSG methods based on estimated density functions. Poggio and Vetter [29] <sup>fi</sup>rst proposed the concept of using virtual samples to increase the recognition rate in 2D models, and this approach has since been applied in many <sup>fi</sup>elds. Cho et al. [7] presented a scheme to select close samples from the population of a network. Li et al. [22] proposed a uniform data generation method to produce a functional virtual population to learn more from small data sets, and provided a criterion for expanding the domain of each feature in a data set to produce the virtual data. Li et al. [24] applied the Mega-

Trend-Diffusion (MTD) method to improve small data set learning using early <sup>fl</sup>exible manufacturing system scheduling knowledge. They used a linear, triangular membership function to generate the virtual samples. Presenting a nonlinear model, Yang et al. [34] used the Gaussian distribution to generate virtual samples and achieved data smoothness. The results of these earlier papers demonstrate that various VSG approaches can be used to help solve the problem of small data sets. Nevertheless, these studies all aimed to improve small data set classi<sup>fi</sup>cation based on the assumption of a uni-modal distribution, such as the Gaussian or uniform distributions, which may sometimes lead to an analytical bias in the results. In practice, a complex data set may have a distribution based on a multi-modal density function, in which the mode size of the data is more than one.

Many methods have been developed to <sup>fi</sup>nd multi-modality in a distribution. For example, Hartigan and Hartigan [15] presented a dip test to measure multi-modality with uniform samples. In this approach, the dip statistic is equal to the maximum difference between the empirical cumulative distribution function (CDF) and the theoretical CDF within all sample points, where the null hypothesis is that the sample has a uniform distribution. Müller and Sawitzki [27] proposed an excess mass test to search for the maximum mode size when the distribution is assumed to be uniform. Without using the uniform assumption, Cheng and Hall [6] proposed a calibrated excess mass test based on other unimodality models, including those with beta, normal, and t distributions.

Many studies have employed these modality test methods to improve performance in classi<sup>fi</sup>cation problems. For example, Polonik and Wang [30] adopted the excess mass test to estimate the modality of each cluster before implementing classi<sup>fi</sup>cation. Using mixed data, Chan and Hall [4] proposed a non-parametric approach, before performing clustering algorithms, for selecting the main features according to the testing modality of the density function. In the literature, the mode-testing technique is often used as a criterion to assess whether it is necessary to implement data preprocessing by using cluster analysis. Unfortunately, in these earlier papers the mode-testing methods including the dip test, excess mass test, and calibrated excess mass test, operate on the assumptions that there are suf<sup>fi</sup>cient samples and that the data has a uni-modal distribution. However, these often do not apply to small data sets, as the distributions of these are often in<sup>fl</sup>exible. Therefore, in the current work we use a two-parameter Weibull distribution to <sup>fi</sup>t the data and thus achieve greater <sup>fl</sup>exibility, and propose a new modality test by constructing a hypothesis testing procedure to evaluate the <sup>fi</sup>tness of the resulting distribution. We use the Cramer–von Mises statistic in the proposed testing method, which is a common goodness-of-<sup>fi</sup>t technique for small data sets [11,18]. With a given signi<sup>fi</sup>cance level, α, we use the statistic to compute the difference between the empirical CDF $\widetilde { F } ( \boldsymbol { x } )$ and the theoretical CDF $F ( x )$ , where the $\widetilde { F } ( x )$ <sup>ð Þ</sup>is the population distribution function of a small data set from a single Weibull distribution. A uni-modal Weibull distribution is chosen as the $F ( x )$ , because when the sample size is small data may come from an arbitrary probability distribution. This paper uses the Weibull distribution recommended by Little [26] to form various shapes of a density function and represent uni-modal distributions, including skewed and mound-shaped curves. The Weibull density function can depict the shape of a small data distribution with various shape parameters, as seen in Abernethy [1], Zhang et al. [35], Wahed et al. [32], and Li and Lin [21]. These works all suggest using the <sup>fl</sup>exible shape of the Weibull distribution to handle small data set problems.

In the null hypothesis, we <sup>fi</sup>rst assume that all data can be <sup>fi</sup>tted by a single Weibull distribution. If the null hypothesis is rejected, we determine that the data is beyond a single Weibull distribution, and thus use two or three Weibull distributions in order to make the <sup>fi</sup>tting process more <sup>fl</sup>exible. Based on the proposed approach, when the density function of a data set indicates multi-modality, we employ the k-means clustering approach to set the modality size. Since deciding the exact size is not the main aim of this study, we examine only twoand three-modality cases, as there are few small data sets for which the modality size is more than three, as noted by Good and Gaskins [14] and Silverman [31]. In addition, using the simulated data from a four-modality distribution, Davies and Kovac [9] showed that the peaks are not signi<sup>fi</sup>cant with small samples. In this study we assume that all samples follow a two-parameter Weibull distribution, and the parameters can be evaluated by using the Maximal p-Value (MPV) method recommended in Li and Lin [21].

Based on the estimated Weibull distribution with consideration of multi-modality, we generate virtual samples to improve classi<sup>fi</sup>cation performance with small data sets. The determination of the appropriate virtual sample size is another important task in this paper, since adding too many virtual samples to training data sets does not always improve the classi<sup>fi</sup>cation accuracy, while it can signi<sup>fi</sup>cantly decrease the computational ef<sup>fi</sup>ciency. For this reason, this paper uses the error variation of the Weibull skewness between the original and virtual data in order to measure the structure of virtual data sets, and thus <sup>fi</sup>nd the suitable virtual sample size (the low variation indicates that the distribution of virtual samples is suitable to depict the original data).

Finally, four real and two simulated data sets are employed in this work to illustrate the effectiveness of the proposed method by comparing its classi<sup>fi</sup>cation accuracy with that of the MTD method. In addition, the technique recommended in Demšar [10] is applied to test the statistical signi<sup>fi</sup>cance and classi<sup>fi</sup>cation performance of the following four classi-<sup>fi</sup>ers, namely Fisher's linear discriminant analysis (LDA), K nearestneighbor (KNN), and two types of support vector machines (SVMs) [16].

The remainder of this study is organized as follows: Section 2 reviews the MTD method for small data set problems, and also describes the use of the MPV approach for evaluating the two-parameter Weibull distribution. Section 3 presents a VSG scheme with the proposed testing steps for multi-modality, and explains how to determine the virtual sample size. Section 4 uses six data sets, and compares the results obtained from the proposed method, the MTD, and REAL (a method using only the existing real data). Finally, we present the conclusions of this work in Section 5.

## 2. Related studies

Modeling with more training data can usually achieve better classi-<sup>fi</sup>cation accuracy, and so many researchers have suggested using virtual sample generation (VSG) approaches when dealing with small data sets. The current study aims to generate multi-modal virtual samples using an estimation method (i.e., MPV) for the two-parameter Weibull distribution. The related studies are reviewed in detail in the following subsections.

## 2.1. The MTD method

As mentioned above, Li et al. [24] proposed the MTD for small data learning in an early manufacturing system, using this approach to data trend estimation to create virtual data. As shown in Fig. 1, the MTD method constructs a triangular membership function to calculate the range of virtual data, which is the interval from α to b, described mathematically as:

$$
a = u _ {s e t} - S k e w _ {L} \times \sqrt {- 2 \times s _ {x} ^ {2} / N _ {L} \times \ln (1 0 ^ {- 2 0})}, 1 <   N _ {L} <   \infty ,\tag{1}
$$

$$
b = u _ {s e t} + S k e w _ {U} \times \sqrt {- 2 \times s _ {x} ^ {2} / N _ {U} \times \ln (1 0 ^ {- 2 0})}, 1 <   N _ {U} <   \infty .\tag{2}
$$

Note that the Skew $= N _ { L } / ( N _ { L } + N _ { U } )$ is the left of the skewness degree of degree of $\sqrt { - 2 \times s _ { x } ^ { 2 } / N _ { L } \times \ln \left( 1 0 ^ { - 2 0 } \right) }$ , and Ske , and Ske $w _ { U } = N _ { U } / ( N _ { L } + N _ { U } )$ is is the right of the skewness degree of $\sqrt { - 2 \times s _ { x } ^ { 2 } / N _ { U } \times \ln \left( 1 0 ^ { - 2 0 } \right) }$ Where $N _ { U }$ and $N _ { L }$ denote the number of data less and more than $u _ { s e t } =$ (min + max)/2, respectively, and the min and max are the minimum and maximum values in real data sets. The lower bound α and the upper bound b can be calculated from Eqs. (1) and (2). After obtaining the values of α and b, generate virtual samples that are distributed following the triangular density function in the interval [α, b], and add them to the original data set. Li et al. [24] set the number of virtual samples that are generated at 100.

## 2.2. The MPV method for parameter estimation

Given a random variable X that is denoted by a two-parameter Weibull distribution, the probability density function (PDF) of the Weibull distribution is expressed as:

$$
f (x, \lambda , \beta) = \frac {\beta}{\lambda} \left(\frac {x}{\lambda}\right) ^ {\beta - 1} \exp \left\{- \left(\frac {x}{\lambda}\right) ^ {\beta} \right\}, x \geq 0, \lambda > 0, \beta > 0\tag{3}
$$

where λ is the scale parameter and β is the shape parameter.

![](/api/attachments/JJMAEGDT/fulltext/images/c416c6edaa3c8bc9ce5f74b9a94573a2719fcb0309c5e3dc4897425abf252fd7.jpg)  
Fig. 1. Data trend estimation.

When X has the characteristics of this distribution, we also write it as X \~ Weibul $( \lambda , \beta )$ . That is, $P ( X \leq x ) = F ( x , \lambda , \beta )$ , where the cumulative distribution function (CDF) of X is de<sup>fi</sup>ned as:

$$
F (x, \lambda , \beta) = 1 - \exp \left\{- \left(\frac {x}{\lambda}\right) ^ {\beta} \right\}, x \geq 0, \lambda > 0, \beta > 0.\tag{4}
$$

Supposing that a set of random samples $x _ { 1 } , x _ { 2 } , . . . , x _ { n }$ is drawn from a Weibull distribution with unknown parameters λ and $\beta ,$ and the data in the set has been ordered as $x _ { 1 } \leq x _ { 2 } \leq \ldots \leq x _ { n } .$ Li and Lin [21] proposed a strategic testing procedure to estimate the parameters λ and β for small sample sizes, as follows:

Step 1: The null hypothesis is set as:

$$
H _ {0}: \beta = \beta_ {0}.
$$

Step 2: The alternative hypothesis is set as:

$$
H _ {1}: \beta \neq \beta_ {0}.
$$

Step 3: The testing statistic uses the Gini statistic as:

$$
G _ {n} = \sum_ {i = 1} ^ {n - 1} i \times W _ {i + 1} / (n - 1) \sum_ {i = 1} ^ {n} W _ {i}\tag{5}
$$

where, $W _ { i } = ( n - i + 1 ) \times ( x _ { ( i ) } ^ { \beta } - x _ { ( i - 1 ) } ^ { \beta } ) , i = 1 , 2 , \cdots , n ,$ and $x _ { ( 0 ) } \equiv 0 .$

Step 4: I. The rejection region for a sample size n between 3 and 20 is set as:

$$
\left\{G _ {n} > \xi_ {1 - \alpha / 2} \right\} \text {   and   } \left\{G _ {n} <   \xi_ {\alpha / 2} \right\}
$$

where the critical value $\xi _ { \alpha / 2 }$ is the $1 0 0 ( \alpha / 2 )$ percentile of the $G _ { n }$ statistic. Moreover, the p-value $= P \{ | G _ { n } | > | g _ { n } | | \beta = \beta _ { 0 } \}$ where $g _ { n }$ indicates the estimated value of $G _ { n } ,$ as follows:

$$
P (G _ {n} \leq x) = x ^ {n - 1} \cdot \left\{\prod_ {i = 1} ^ {n - 1} c _ {i} \right\} ^ {- 1} - \sum_ {j = r + 1} ^ {n - 1} \left(x - c _ {j}\right) ^ {n - 1} \cdot \left\{c _ {j} \prod_ {k \neq j} ^ {n - 1} \left(c _ {k} - c _ {j}\right) \right\} ^ {- 1}\tag{6}
$$

where $c _ { j } = \left( n - j \right) / \left( n - 1 \right)$ , and r is the largest index, such that $x \leq c _ { r } .$ . Note that the corresponding two-tailed percentiles $\xi _ { \alpha / 2 }$ of the Gini statistic $G _ { n }$ are shown in Gail and Gastwirth [13].

![](/api/attachments/JJMAEGDT/fulltext/images/c3d04f7937309479370abf4f9d1282dfaaf6f8b41043d832b777e81e15d137c0.jpg)  
Fig. 2. The relationships among two populations, two small data sets, two virtual data sets and the overlapping area.

II. The rejection region for a sample size n that is more than 20 is set as follows:

$$
\left\{G _ {n} > Z _ {1 - \alpha / 2} \right\} \text { and } \left\{G _ {n} <   Z _ {\alpha / 2} \right\}
$$

where $g _ { n }$ is the observed value of $[ 1 2 ( n - 1 ) ] ^ { 1 / 2 } ( G _ { n } - 0 . 5 )$ which follows an approximately standard normal distribution Normal(0,1), as below:

$$
P \left\{| Z | > \left| [ 1 2 (n - 1) ] ^ {1 / 2} \left(g _ {n} - 0. 5\right) \right| | \beta = \beta_ {0} \right\}.\tag{7}
$$

Step 5: The decision rule of the statistical test is designed as: When $\beta =$ $\beta _ { 0 } ,$ the p-value has a maximal value, which means that there is a strong evidence to accept the null hypothesis, $H _ { 0 } .$

The <sup>fi</sup>ttest shape parameter β can be found based on this testing procedure. When $\beta$ is estimated, we can compute the scale parameter λ from the following equation:

$$
\lambda = \exp \left\{- \frac {1}{\beta} \times \frac {1}{n} \left[ \sum i = 1 n \left(\ln \left\{- \ln \left[ 1 - \hat {F} (x _ {i}) \right] \right\} - \beta \ln x _ {i}\right) \right] \right\}\tag{8}
$$

where the Bernard's median rank estimator $\hat { F } ( x _ { i } ) = ( i \mathrm { - } 0 . 3 ) / ( n + 0 . 4 ) ,$ $i = 1 , \cdots , n .$

## 3. The proposed method

Although most VSG methods are developed based on a uni-modal distribution, in practice a small data set may have a multi-modal one. This study proposes a modality test that is integrated into the VSG scheme with a mixed Weibull distribution, where we employ the k-means algorithm to set the k modalities in the distribution. In addition, the virtual sample size is computed based on the error variation of the Weibull skewness between the original and virtual data.

## 3.1. The VSG scheme

Since the population information is insuf<sup>fi</sup>ciently represented in small data sets, it is dif<sup>fi</sup>cult to obtain stable training performance with regard to classi<sup>fi</sup>cation, and many researchers have proposed using VSG to overcome this. However, one of the problems in small sample learning using traditional VSG approaches is that these usually assume that the population is characterized by a uni-modal distribution. In fact, as shown in Fig. 2, a data set might have two populations, or be a mixture data set with two distributions.

Therefore, in this research, a unique VSG scheme is developed that considers the issue of multi-modality in real data sets. It contains three main steps, as shown in Fig. 3.

## 3.2. The proposed modality test

With regard to the modality of the distribution in a data set, we <sup>fi</sup>rst use two simulated data sets with a two-modal distribution to examine the relationship between CDF and PDF. A mathematical testing procedure is then constructed to obtain an estimation of modality for small data sets.

## 3.2.1. The relationship between CDF and PDF

To demonstrate the proposed concept, we generate 1000 simulated data points from two mixed populations, as shown in Fig. $4 ( \mathsf { a } )$ and (c). Given two sets of data with bimodal-shaped PDFs, the corresponding CDFs are constructed in Fig. 4(b) and (d). In Fig. 4(a), when two peaks are located very close to each other, the estimate of the distribution could be a uni-modal one. In other words, the data is considered unimodal for a large overlapping area, and one can see in Fig. 4(b) that the two lines “Empirical $\mathrm { C D F ^ { \prime } }$ and “Theoretical $\mathrm { C D F ^ { \prime } }$ are close to each other. In contrast, when peaks are located apart from each other, there is a signi<sup>fi</sup>cant difference between the empirical and theoretical CDFs. The empirical CDF can be constructed by the Bernard's median rank estimator $( i - 0 . 3 ) / { ( n + 0 . 4 ) } , i = 1 , 2 , . . . , n ,$ , where n is the number of observed data, and the theoretical CDF is an estimated CDF obtained from Eq. (4) using two estimators, where we use ordered and observed data $\left( \mathrm { i . e . , } x _ { 1 } \leq x _ { 2 } \leq \ldots \leq x _ { n } \right)$ to calculate the two estimators, as in Section 2.2. For example, in Fig. 4(c), the data set is distributed into a two-modality density function, so the two lines of the CDFs are different from each other in Fig. 4(d).

![](/api/attachments/JJMAEGDT/fulltext/images/c4763dd3be8d6875895183598c8e532016f7e9179df4aa7043d713a2d1d6f012.jpg)  
Fig. 3. The proposed VSG scheme contains three steps.

For a more detailed explanation, consider two small sample cases, with a size of 10, randomly drawn from the two sets of populations, above, where the CDFs are shown in Fig. 5(a) and (b). It is obviously dif<sup>fi</sup>cult to decide the modality of the density function, and thus the proposed procedure is used to estimate whether the function is uni-modal or multi-modal for the small data sets.

## 3.2.2. The procedure of the modality test

Supposing a data set $x _ { i j } , i = 1 , 2 , . . . , n , j = 1 , 2 , . . . , m ,$ where m variables $\{ x _ { 1 } , x _ { 2 } , . . . , x _ { m } \}$ are following Weibull distributions, and the CDF $F ( x )$ is found using Eq. (4). With a given signi<sup>fi</sup>cance level α, the Cramer–von Mises statistic [18] is used here as the goodness-of-<sup>fi</sup>t measurement. This statistic measures the difference between the empirical CDF F x and theoretical CDF F(x) to test the modality of data sets. <sup>ð Þ</sup>Note that F x is the observed CDF, and F(x) is the estimated CDF. To estimate the two parameters λ and β in F(x), the estimators in Li and Lin [21] are employed to calculate $\hat { \lambda }$ and ${ \hat { \boldsymbol { \beta } } } ,$ as in Section 2.2. The proposed hypothesis testing procedure with regard to data modality is based on the following steps:

![](/api/attachments/JJMAEGDT/fulltext/images/bbf7ed80d1996bdac79830f66b5d60425632be26c9bf9aa1b6db98d2d45203de.jpg)

(b)  
![](/api/attachments/JJMAEGDT/fulltext/images/b3cc8637716fa6e2fcdc35cba46b8d06bf2d60067332ea361337f8a3d669ee07.jpg)

(c)  
![](/api/attachments/JJMAEGDT/fulltext/images/ac0ed94021b6aec324a9d30f61790a070141336ba56fef168cd9e3591c3e27f9.jpg)

(d)  
![](/api/attachments/JJMAEGDT/fulltext/images/16c2db25f6acbd91f6a8d0e58704930996b9f1682d1767789f3b92b57a837aba.jpg)  
Fig. 4. The overlapping region of PDFs and the two corresponding lines of CDFs: (a) a large overlapping region; (b) two close CDF lines; (c) a small overlapping region; (d) two distinct CDF lines.

![](/api/attachments/JJMAEGDT/fulltext/images/cb4f2e088f5cf379d1517d4f8f9cf1ca228f4908df00599c5c1300a225a741ac.jpg)

![](/api/attachments/JJMAEGDT/fulltext/images/c81f8f76582b951b97cc252adfd2c05781dd0c69b764d8f9f9705a5f27542aab.jpg)  
Fig. 5. Two sets of small mixed data for “Empirical CDF” and “Theoretical CDF”: (a) from Population 1 and Population $^ { 2 ; }$ and (b) from Population 3 and Population 4

Step 1. The null hypothesis is set as:

$$
H _ {0}: \widetilde {F} (x) = F (x) \text {   for   all   } x.
$$

Step 2. The alternative hypothesis is set as:

$$
H _ {1}: \widetilde {F} (x) \neq F (x) \text {   for   at   least   one   } x.
$$

Step 3. The testing statistic used as the Cramer–von Mises statistic is:

$$
W _ {n} ^ {2} = n \int_ {- \infty} ^ {+ \infty} \left[ \widetilde {F} (x) - F (x) \right] ^ {2} d F (x)\tag{9}
$$

where n is the sample size, $\widetilde { F } ( \boldsymbol { x } )$ is the Bernard's median rank estimator $( i - 0 . 3 ) / \left( n + 0 . 4 \right) , i = 1 , 2 , . . . , n ,$ and $F ( x )$ is Eq. (4) with the estimators λ and ${ \hat { \beta } } .$

Step 4. The rejection region is set as:

$$
W _ {n} ^ {2} \geq w _ {n, \alpha^ {\prime}} ^ {2}
$$

where the critical value $w _ { n , \alpha ^ { \prime } } ^ { 2 }$ is the $1 0 0 \times \alpha ^ { \prime }$ percentile of $W _ { n } ^ { 2 } ,$ such that $P \Big \{ W _ { n } ^ { 2 } \ge w _ { n , \alpha ^ { \prime } } ^ { 2 } \Big \} = \alpha ^ { \prime }$ . Note that the corresponding one-tailed percentiles $w _ { n , \alpha ^ { \prime } } ^ { 2 }$ of the statistic $W _ { n } ^ { 2 }$ are explained in detail in Knott [18].

Step 5. The decision rule of the statistical test is as follows:

$\mathrm { I f } W _ { n } ^ { 2 } \geq w _ { n , \alpha ^ { \prime } } ^ { 2 } ,$ , conclude that the data distribution is not a singlemodality Weibull distribution, and thus reject $H _ { 0 }$

If $W _ { n } ^ { 2 } < w _ { n , \alpha ^ { \prime } } ^ { 2 }$ , conclude that the data distribution is a singlemodality Weibull distribution, and thus accept $H _ { 0 } .$

The modality of the data distribution can be decided based on the results of this procedure. There is the possibility of type I and type II errors when the null hypothesis $\left( H _ { 0 } \right)$ is rejected or accepted. A type I error means that $H _ { 0 }$ is true, but the test rejects $H _ { 0 } ,$ , and the probability of type I error can be de<sup>fi</sup>ned as P(reject $H _ { 0 } | H _ { 0 }$ is true). In the proposed method, a type I error indicates that the data actually follows a unimodal Weibull distribution, while the results of the test show that the data actually has a multi-modal Weibull distribution. In fact, in hypothesis testing, a lower signi<sup>fi</sup>cance level α′ (i.e., lower probability of type I error) means that the criteria for the rejection of $H _ { 0 }$ are stricter. For example, $\alpha ^ { \prime } = 0 . 0 1$ indicates that the P(reject $H _ { 0 } | H _ { 0 }$ is true) is 1%, meaning that the tolerable probability of incorrectly rejecting $H _ { 0 }$ is 1%. Regarding type II errors, these occur when $H _ { 0 }$ is false, but the test accepts $H _ { 0 } ,$ and in this paper this means that a multi-modal Weibull distribution is classi<sup>fi</sup>ed as a uni-modal one. In the proposed method, the probability of a type II error, which is de<sup>fi</sup>ned as $P ($ (accept $H _ { 0 } | H _ { 0 }$ is false), can calculated by using $P \left( W _ { n } ^ { 2 } { < } w _ { n , \alpha ^ { \prime } } ^ { 2 } \right)$ , which is the distribution function from Cramer–von Mises $[ 1 8 ] ,$ , where $W _ { n } ^ { 2 }$ can be estimated using Eq. $( 9 )$ and $w _ { n , \alpha ^ { \prime } } ^ { 2 }$ is as seen in Knott [18] at a given n and $\alpha ^ { \prime }$ based on $H _ { 0 }$ being rejected.

In theory, there is a trade-off between type I and type II errors, with a too low α′ leading to a higher probability of the latter. For this reason, the proposed method carefully considers the setting of $\alpha ^ { \prime }$ to reduce the risk of incorrectly rejecting $H _ { 0 }$ of a uni-modal Weibull distribution, and we set the value of α′ as 0.01, 0.05, 0.10, and 0.20 for different data sizes.

## 3.3. The decision of virtual sample size

With regard to the number of virtual samples, Li et al. [20] stated that too many may decrease the computational ef<sup>fi</sup>ciency while also not improving the classi<sup>fi</sup>cation performance. In this paper we try to control the number of virtual samples based on the error variation of the skewness between the original and virtual data, using the Weibull skewness. In addition, we select a certain small proportion of the training data set, such as 10%, as the number of virtual samples that will be used to calculate the error variation of the Weibull skewness between the original and virtual samples. The estimation of the Weibull skewness is obtained as follows:

$$
\gamma = \frac {\hat {\lambda} ^ {3} \Gamma_ {3} - 3 \mu \sigma^ {2} - \mu^ {3}}{\sigma^ {3}}, - 1 \leq \gamma \leq 1,\tag{10}
$$

where the mean μis $\hat { \lambda } { \cal { T } } _ { 1 } .$ the standard deviation σis $\left( { { I _ { 2 } } - { I _ { 1 } ^ { 2 } } } \right) ^ { 1 / 2 }$ , the $\Gamma _ { i }$ is $\boldsymbol { { \Gamma } } \Big ( 1 + i / \hat { \beta } \Big )$ , and the estimators $\hat { \lambda }$ and $\hat { \beta }$ are from the MPV method, as in Section 2.2. Concerning the value of $\gamma ,$ if the coef<sup>fi</sup>cient of skewness is zero, the density function is symmetrical. In addition, $\gamma \approx 1$ and $\gamma \approx - 1$ indicate that the distribution of the data set has an extreme right or left skewness, respectively.

Table 1  
Data set description.

<table><tr><td>Data sets</td><td>No. instances</td><td>No. features</td><td>No. classes</td><td>Feature characteristics</td><td>Modality of features</td></tr><tr><td>HSD</td><td>306</td><td>3</td><td>2</td><td>N</td><td>2U, 1M</td></tr><tr><td>BUPA</td><td>345</td><td>6</td><td>2</td><td>N</td><td>6U</td></tr><tr><td>IRIS</td><td>150</td><td>4</td><td>3</td><td>N</td><td>1U, 3M</td></tr><tr><td>FMS</td><td>200</td><td>3</td><td>3</td><td>N</td><td>1U, 2M</td></tr><tr><td>S2</td><td>200</td><td>4</td><td>2</td><td>N</td><td>1U, 3M</td></tr><tr><td>S3</td><td>300</td><td>5</td><td>3</td><td>N</td><td>5M</td></tr></table>

When the shape parameter $\beta$ is known, Bowman and Shenton [3] showed that the Weibull skewness γ has a consistent property, and based on this one can know that when the number of virtual samples in a Weibull distribution increases, the error variation of γ between the original and virtual data becomes lower. Regarding the error variation of γ, if it is too small then the number of virtual samples may be too large. In order to avoid this we use a suitably small value of the variation of $\gamma ,$ set at 0.01 in this paper. To <sup>fi</sup>nd the ideal virtual sample size, this process is iterated while increasing the number of the virtual samples and monitoring the variation of γ of a data set $\{ x _ { j } ^ { C } \}$ , as follows:when $\Delta \gamma _ { j } ^ { C , t } \leq 0 . 0 1$ then $\begin{array} { r } { N _ { j } ^ { C , t } = t \times n \times 1 0 \% , j = 1 , 2 , . . . , m , C = 1 , 2 , . . . , } \end{array}$ c where $\Delta \gamma _ { j } ^ { C , t } =$ <sub>γ</sub>C;original<sub>−γ</sub>C;t<sup>	</sup><sub>	</sub> <sup>	</sup><sub>	</sub>

$$
\frac {\left| \gamma_ {j} ^ {C ,   o r i g i n a l} - \gamma_ {j} ^ {C ,   t} \right|}{\gamma_ {j} ^ {C ,   o r i g i n a l}}
$$

$$
\gamma_ {j} ^ {C, \text { original }}
$$

ness of original data, and $\Delta \gamma _ { j } ^ { C , t }$ is the error variation of Weibull skewness for the j-th variable in C-th class with the added number of $t \times n \times 1 0 \%$ When the index $\Delta \gamma _ { j } ^ { C }$ of each class is smaller than 0.01, we consider that the number of virtual data that have been generated is suf<sup>fi</sup>cient, with the N<sup>C</sup> being the ideal virtual sample size for j-th variable in C-th class.

## 3.4. Random variate generation

Random variate generation is used to generate samples from a speci<sup>fi</sup>ed distribution, and is frequently employed in the <sup>fi</sup>eld of simulation. For example, the Markov Chain Monte Carlo Method has been widely used to obtain reliable results. In this study, supposing that the data characteristic function has a Weibull distribution, we use the MPV method to estimate the underlying distribution for a given data set, and then apply the inversion method to generate the variates.

## 3.4.1. The inversion method

In the inversion method, a random variable X is distributed in a Weibull distribution containing both a scale parameter λ and a shape parameter $\beta ,$ or $X \sim \mathrm { \sf { W e i b u l l } } ( \lambda , \beta )$ . Given that F(x, λ, β) is the CDF of the data, as in Eq. (4), the formula to derive the Weibull variates is as follows:

$$
x = \lambda \{- \ln [ 1 - F (x, \lambda , \beta) ] \} ^ {1 / \beta}\tag{11}
$$

where $x \ge 0 , \lambda > 0 , \beta > 0 .$ . Eq. (11) is then modi<sup>fi</sup>ed to generate virtual samples $\hat { x } _ { 1 } , \hat { x } _ { 2 } , . . . \hat { x } _ { N _ { i } ^ { C } }$ as follows:

$$
\hat {x} _ {i} = \hat {\lambda} \left\{- \ln \left[ 1 - \hat {F} (x _ {i}) \right] \right\} ^ {1 / \hat {\beta}}\tag{12}
$$

where the Bernard's median rank estimator $\hat { F } ( x _ { i } ) = ( i - 0 . 3 ) / \Big ( N _ { j } ^ { C } + 0 . 4 \Big )$ the desired number of N<sup>C</sup> is given by $i = 1 , 2 , . . . , N _ { j } ^ { C } , \forall j , C ,$ , and λ<sup>^</sup> and β<sup>^</sup> are calculated by the MPV method.

## 3.4.2. k-Modality selection for each feature

Based on a Weibull density function, this study uses the modality test to estimate whether a density function is uni-modal or multimodal. As mentioned before, when the function estimator adopts the Weibull distribution with different shape parameters, then this indicates that a combination of many Weibull density functions may exist. In other words, a data set which is <sup>fi</sup>tted by a Weibull distribution may contain other kinds of density functions with a multi-modality curve. With small data sets, it is dif<sup>fi</sup>cult theoretically to estimate the value of k, and the dependence of the data with regard to each modality would increase the complexity of the estimation of k. For simplicity, this paper tests whether a small data set follows a multi-modal distribution, and assumes that there are two or three modes if uni-modality is rejected. In addition, no more than three modes are considered in this work, as it is very rare for small data sets to have more modes than this. For the above reasons, the proposed method for generating virtual samples is modi<sup>fi</sup>ed by using the following steps:

Step 1. Use the k-means algorithm to cluster a training data set with a size n into k types of mutually independent data sets (i.e., k sets of Weibull distributed density estimators).

Step 2. Calculate the parameters $\left( { \hat { \lambda } } , { \hat { \beta } } \right)$ using the MPV method for clustered data sets.

Step 3. For each Weibull density curve, generate the corresponding Weibull variates using $\operatorname { E q . } \left( 1 2 \right)$ ) and compute the number of virtual samples $N _ { j , k } ^ { C }$ for the k-th cluster based on the criterion in Section 3.3.

Step 4. Calculate the sum of virtual samples in class $C , C = 1 , 2 , . . . , c ,$ , is $\begin{array} { r } { N _ { t o t a l } ^ { C } = \sum _ { k } ^ { k } = _ { 1 } N _ { j , k } ^ { C } , j = 1 , 2 , . . . , m . } \end{array}$

Based on these steps, the modi<sup>fi</sup>ed method can be applied to <sup>fi</sup>t both uni-modal and multi-modal distributions.

## 3.5. The detailed steps for the use of the proposed method

Assuming that a training data set has n samples and m mutually independent features, denoted as $T = \{ ( x _ { 1 } , y _ { 1 } ) , ( x _ { 2 } , y _ { 2 } ) , . . . , ( x _ { n } , y _ { n } ) \}$ , and the data set contains c classes where each sample $x _ { i } , i = 1 , . . . ,$ n in $x _ { i }$ has m features (and thus $x _ { i } = \{ X _ { i 1 } , X _ { i 2 } . . . , X _ { i m } \} ) , y _ { i } \in C$ is the target value of $\cdot _ { x _ { i } }$ and $C = \{ 1 , 2 , . . . , c \} .$

Step 1. Separate the data set T into c groups by the corresponding target values denoted as $T = \{ \stackrel {  } { t } _ { 1 } , \stackrel {  } { t } _ { 2 } , . . . \stackrel {  } { t } _ { c } \}$ , where $\overline { { t _ { j } } } =$ $\{ I ( y _ { i } = C ) ( x _ { 1 } , C ) , I ( y _ { i } = C ) ( x _ { 2 } , C ) , . . . , I ( y _ { i } = C ) ( x _ { n } , C ) \} , C = 1 , 2 ,$ $\cdots , c$ <sup>gÞ¼ ð Þ¼ ð Þ¼ ¼</sup>and I(⋅) is an indicator function with selecting conditions.

Step 2. Use the proposed modality test for the sub-feature set $\{ X _ { 1 } ^ { C } ,$ $X _ { 2 } ^ { C } , . . . , X _ { m } ^ { C } \} \left( X _ { m } ^ { C } \right.$ means that the data set is from the m-th variable in C-th class) and assess whether the variable has a multi-modal distribution. If it does, go to Step 3; otherwise, go to Step 4.

Step 3. Select the number of modality, such as $k = 2$ and $k = 3 ,$ , and use the k-means algorithm to group the data into two and three clusters for the multi-modal variables, respectively.

Step 4. When $\begin{array} { r } { \Delta \gamma _ { j } ^ { C } < 0 . 0 1 , \forall j , C , } \end{array}$ obtain a number of m of $N _ { t o t a l } ^ { C }$ and take the maximum $N _ { t o t a l } ^ { C } ~ ( \mathrm { i . e . , m a x } ~ N _ { t o t a l } ^ { C } )$ among these for each class C.

Step 5. According to the virtual sample size max $N _ { t o t a l } ^ { C } ,$ generate the virtual data sets $V ^ { c }$ in class C using the variate generation method presented in Section 3.4.

Step 6. Add virtual data sets $V ^ { c }$ to the original training data sets $\widehat { t } _ { j }$ based on the class C of virtual samples.

We can use the above procedure to generate a virtual data set $\{ V ^ { 1 } , V ^ { 2 } , . . . V ^ { c } \}$ and extend the original training data set from n × m into $\left( n + \sum _ { C } \operatorname* { m a x } N _ { t o t a l } ^ { C } \right)$ m dimensions.

## 4. Experiments

In order to demonstrate the performance of the proposed method, we examine the multi-modal distributions constructed from the histograms of each feature using six data sets. The results of the following experiments with different small sample sizes show that the proposed method has better classi<sup>fi</sup>cation accuracy than that of the MTD and REAL approaches, where REAL denotes using the real data set to carry out classi<sup>fi</sup>cation, without the aid of virtual samples.

Table 2  
![](/api/attachments/JJMAEGDT/fulltext/images/cd22a2bffc2c0e90876d331ed92200247562798ed2ab637cc6e0a66f60e530c8.jpg)

![](/api/attachments/JJMAEGDT/fulltext/images/163260a3e94d2c2c9623c335ac58f14552d3a0526f3c743733606b977d968a26.jpg)

![](/api/attachments/JJMAEGDT/fulltext/images/866fada237235f8e9251172a0859ed752b3c75e3432e63ef0aa7cdf19072015d.jpg)  
Fig. 6. The histograms of features in the HSD data set

## 4.1. The six data sets

The MTD and our proposed method are compared in this section by using six data sets for classi<sup>fi</sup>cation problems. The six data sets include four real data sets and two simulated data sets. These data sets are the Haberman's survival data (HSD), the BUPA liver disorders (BUPA), the IRIS plants data (IRIS), an early <sup>fl</sup>exible manufacturing scheduling (FMS) problem, a simulated two-modality data set (S2), and a simulated three-modality data set (S3). The BUPA, HSD, and IRIS data sets are downloaded from the UCI Machine Learning Repository database [2], while the FMS data is from Li et al. [24]. Both data sets S2 and S3 are mixtures from the union of different Weibull distributions. S2 has a total of $2 0 0 ( = n )$ samples (100 in each of the two classes, class1 and class2), and each sample has four numerical features. The features are one uni-modal and three two-modal independent Weibull density functions. The data set S2 is considered as $x _ { j } , j = 1 , . . . , 4 ,$ , where

$$
x _ {1} \sim \mathrm{W} (1. 5, 2),
$$

$$
x _ {2} \sim 1 / 2 W (2, 4) + 1 / 2 W (3, 6),
$$

$$
x _ {3} \sim 1 / 2 W (3. 5, 2) + 1 / 2 W (4, 6),
$$

$$
x _ {4} \sim 1 / 2 W (4, 5) + 1 / 2 W (5, 8)
$$

where ${ \boldsymbol { x } } \sim 1 / p \mathsf { W } ( \lambda , \beta )$ means that a data x is drawn from a Weibull distribution with a scale parameter λ and a shape parameter $\beta ,$ and the size of the data is n/p. Similarly, the data set S3 has a total of 300 (=n) samples (100 in each of the three classes, class1, class2, and class3), and each sample has <sup>fi</sup>ve mutually exclusive numerical features, $x _ { j } , j = 1 , . . . , 5 .$ . Using the union of Weibull distributions, including one two-modal and four threemodal features, S3 can be composed as follows:

$$
x _ {1} \sim 1 / 2 W (1, 2) + 1 / 2 W (1. 5, 4),
$$

$$
x _ {2} \sim 1 / 3 W (2, 6) + 1 / 3 W (3, 8) + 1 / 3 W (3, 8),
$$

$$
x _ {3} \sim 1 / 3 W (3, 5) + 1 / 3 W (4, 8) + 1 / 3 W (5, 1 1),
$$

$$
x _ {4} \sim 1 / 3 W (1. 5, 2) + 1 / 3 W (2. 5, 4) + 1 / 3 W (3. 5, 6),
$$

$$
x _ {5} \sim 1 / 3 W (1. 2, 4) + 1 / 3 W (2. 4, 7) + 1 / 3 W (3. 6, 1 0),
$$

The six data sets have different features, with {BUPA, HSD, S2} and {IRIS, FMS, S3} being two- and three-class classi<sup>fi</sup>cation problems, respectively. The details of these data sets are summarized in Table 1, where $\ " \mathrm { N } "$ indicates numerical value features, $\ " \mathrm { U } ^ { \prime \prime }$ denotes unimodality, and “M” denotes multi-modality. For example, the data set HSD in Table 1 contains 306 instances, three numerical features, and two classes. In addition, (2U, 1M) indicates that there are two unimodal density functions and one multi-modal ones in the features, as shown in Fig. 6.

## 4.2. An example for the proposed method

In this section, we use the HSD data set with three input variables and one output variable to explain the proposed procedure in detail. We take ten data from the HSD data set to be the training data set and use the steps to obtain a new training data set:

Step 1. Table 2 shows that the information of the training data set $T =$ $\{ \stackrel {  } { t } _ { 1 } , \stackrel {  } { t } _ { 2 } \}$ includes ten data $\{ x _ { 1 } , x _ { 2 } , . . . , x _ { 1 0 } \}$ with three features $\{ X _ { 1 } , X _ { 2 } , X _ { 3 } \}$ and one class variable C. In variable C, a value of 1 means a patient survived at least <sup>fi</sup>ve years, and a value of 2 means a patient died within <sup>fi</sup>ve years.

The information of data set $T = { \Big \{ } { \vec { t } } _ { 1 } , { \vec { t } } _ { 2 } { \Big \} } .$

<table><tr><td rowspan="2">Data</td><td>Feature 1</td><td>Feature 2</td><td>Feature 3</td><td>Class variable</td></tr><tr><td> $X_1$ </td><td> $X_2$ </td><td> $X_3$ </td><td>C</td></tr><tr><td> $x_1$ </td><td>34</td><td>60</td><td>1</td><td>1</td></tr><tr><td> $x_2$ </td><td>40</td><td>58</td><td>2</td><td>1</td></tr><tr><td> $x_3$ </td><td>52</td><td>60</td><td>5</td><td>1</td></tr><tr><td> $x_4$ </td><td>58</td><td>61</td><td>2</td><td>1</td></tr><tr><td> $x_5$ </td><td>64</td><td>65</td><td>22</td><td>1</td></tr><tr><td> $x_6$ </td><td>34</td><td>66</td><td>9</td><td>2</td></tr><tr><td> $x_7$ </td><td>41</td><td>60</td><td>23</td><td>2</td></tr><tr><td> $x_8$ </td><td>43</td><td>58</td><td>52</td><td>2</td></tr><tr><td> $x_9$ </td><td>66</td><td>61</td><td>13</td><td>2</td></tr><tr><td> $x_{10}$ </td><td>78</td><td>65</td><td>1</td><td>2</td></tr></table>

Table 3  
The values of $W _ { n } ^ { 2 }$ in the sub-feature set.

<table><tr><td>Class</td><td>Feature 1</td><td>Feature 2</td><td>Feature 3</td></tr><tr><td>1</td><td>0.0295</td><td>0.1164*</td><td>0.0966*</td></tr><tr><td>2</td><td>0.0770*</td><td>0.0605*</td><td>0.0342</td></tr></table>

Step 2. Use the proposed modality test in Section 3.2.2 to compute the value of testing statistic $W _ { n } ^ { 2 }$ for each input variable $X _ { 1 } , X _ { 2 } , X _ { 3 }$ in each class, and the corresponding $w _ { n , \alpha ^ { \prime } } ^ { 2 }$ at $( n , \alpha ^ { \prime } ) = ( 5 , 0 . 0 5 )$ is 0.0404, as seen in Knott [18]. Table 3 shows the values of $W _ { n } ^ { 2 }$ of the sub-feature set $\{ X _ { 1 } ^ { 1 } , X _ { 1 } ^ { 2 } , X _ { 2 } ^ { 1 } , X _ { 2 } ^ { 2 } , X _ { 3 } ^ { 1 } , X _ { 3 } ^ { 2 } \}$ , where ‘\*’ indicates the results of $W _ { n } ^ { 2 } { \geq } w _ { n , \alpha ^ { \prime } } ^ { 2 } = 0 . 0 4 0 4$ , meaning that the data is not from a uni-modal Weibull distribution. For instance, the W<sup>2</sup> value of X<sup>1</sup> is 0.1164, which is greater than 0.0404.

Step 3. Select k = 2 and k = 3 in the k-means algorithm to group the data into two and three clusters for the multi-modality feature set $\{ X _ { 1 } ^ { 2 } , X _ { 2 } ^ { 1 } , X _ { 2 } ^ { 2 } , X _ { 3 } ^ { 1 } \}$ .

Step 4. Use the procedure proposed in Section 3.3 to decide the number of virtual samples for the set $\{ X _ { 1 } ^ { 1 } , X _ { 1 } ^ { 2 } , X _ { 2 } ^ { 1 } , X _ { 2 } ^ { 2 } , X _ { 3 } ^ { 1 } , X _ { 3 } ^ { 2 } \}$ .

Step 5. Generate uni-modal virtual samples for the set {X<sup>1</sup>, X<sup>2</sup>} and multi-modal virtual samples for the set $\{ X _ { 1 } ^ { 2 } , X _ { 2 } ^ { 1 } , X _ { 2 } ^ { 2 } , X _ { 3 } ^ { 1 } \}$ based on the number of virtual samples chosen in Step 4 to produce the virtual data sets $V ^ { 1 }$ and $V ^ { 2 } .$

Step 6. Add the virtual data sets $V ^ { 1 }$ and $V ^ { 2 }$ to the original training sets $\stackrel {  } { t } _ { 1 }$ and ${ \overline { { t } } } _ { 2 } ,$ respectively.

## 4.3. The experiment design

To design the experiment for small data set analysis, we use a random sampling method to create several small training data sets from the original data sets, and use the rest for testing. In this the training data size n will be set at 10, 20, 30, and 50. With the six data sets, we iterate the experiments 30 times for each size of n to obtain the related classi<sup>fi</sup>cation accuracies. The classi<sup>fi</sup>cation accuracy is de<sup>fi</sup>ned as the average of the classi<sup>fi</sup>cation rates, and this is an important index when evaluating classi<sup>fi</sup>cation performance. The current work compares the classi<sup>fi</sup>cation performance of REAL, MTD, and the proposed method based on the use of the four classi<sup>fi</sup>ers. The four classi<sup>fi</sup>ers are LDA, KNN, and two types of SVM. In the parameter settings, the value of k in KNN is 3 and the kernel functions in the SVM are linear and radial bases, with the cost parameter set at 0.1 and the gamma parameter at 0.07 in the kernel functions. The algorithms of the LDA and 3-NN classi-<sup>fi</sup>ers are implemented in Matlab, using the Statistics Toolbox. The two kinds of SVMs use LIBSVM [5] as the analysis tool, and are labeled SVM(linear) and SVM(radial) respectively. Without using the generated data, the classi<sup>fi</sup>cation accuracies and results of the statistical tests using the four classi<sup>fi</sup>ers are shown in Section 4.4.

The proposed method is designed to test whether a density function is uni-modal or multi-modal. Consequently, in the k-means method, k clusters means k-modality. k = 2 and k = 3 are used in the experiments, as shown in Tables 7–9, where signs “PM2” and “PM3” indicate twomodality and three-modality, respectively.

## 4.4. The results for selection of classifiers

Based on the six data sets, we can obtain the classi<sup>fi</sup>cation accuracies using the four classi<sup>fi</sup>ers (LDA, 3-NN, SVM(linear), and SVM(radial)) with the training data size $n = \{ 1 0 , 2 0 , 3 0 , 5 0 \}$ . In Table 4, the values in bold show the best classi<sup>fi</sup>cation accuracies for the four classi<sup>fi</sup>ers.

The nonparametric test (the Friedman test) proposed in Demšar [10] is used to examine whether the results using multiple data sets are statistically signi<sup>fi</sup>cant. Six different data sets are thus used to assess the signi<sup>fi</sup>cance of the classi<sup>fi</sup>cation accuracy for the four classi<sup>fi</sup>ers. For example, when using the six data sets at $n = 1 0$ , the average accuracy ranks $\mathsf { R } _ { i }$ for ith methods in order as LDA, 3-NN, SVM(linear) and SVM(radial) are shown in Table 5.

With four methods $( K = 4 )$ and six data sets (N = 6), the Friedman statistic is computed as:

$$
\begin{array}{l} \chi_ {F} ^ {2} = \frac {1 2 N}{K (K + 1)} \left[ \sum_ {i} R _ {i} ^ {2} - \frac {K (K + 1) ^ {2}}{4} \right] \\ = \frac {1 2 \times 6}{4 \times (4 + 1)} \times \left[ \left(2. 0 0 ^ {2} + 2. 6 7 ^ {2} + 1. 6 7 ^ {2} + 3. 6 7 ^ {2}\right) - \frac {4 \times (4 + 1) ^ {2}}{4} \right] \\ = 8. 4 0. \end{array}
$$

The modi<sup>fi</sup>cation is suggested by Iman and Davenport [17], and the statistic $F _ { F }$ is computed as:

$$
\begin{array}{l} F _ {F} = \frac {(N - 1) \chi_ {F} ^ {2}}{N (K - 1) - \chi_ {F} ^ {2}} \\ = \frac {(6 - 1) \times 8 . 4}{6 \times (4 - 1) - 8 . 4} \\ = 4. 3 4, \end{array}
$$

where F is distributed according to the distribution with $( K - 1 ) =$ (4 − 1) = 3 and $( K - 1 ) ( N - 1 ) = ( 4 - 1 ) \times ( 6 - 1 ) = 1 5$ degrees of freedom. The critical value is $F _ { 1 5 } ^ { 3 } = 3 . 2 8 7$ at the signi<sup>fi</sup>cance level of 0.05, and we reject the null hypothesis when there is statistical signi<sup>fi</sup>cance with regard to the classi<sup>fi</sup>cation accuracy. Further, we compare the methods by using the following formula:

Classi<sup>fi</sup>cation accuracies for the four classi<sup>fi</sup>ers

<table><tr><td>Data sets</td><td>LDA</td><td>3-NN</td><td>SVM(linear)</td><td>SVM(radial)</td><td>LDA</td><td>3-NN</td><td>SVM(linear)</td><td>SVM(radial)</td></tr><tr><td>n</td><td>10</td><td></td><td></td><td></td><td>30</td><td></td><td></td><td></td></tr><tr><td>HSD</td><td>57.48</td><td>56.37</td><td>59.01</td><td>54.13</td><td>63.43</td><td>60.65</td><td>63.86</td><td>56.89</td></tr><tr><td>BUPA</td><td>57.19</td><td>55.87</td><td>59.26</td><td>51.49</td><td>58.80</td><td>57.01</td><td>59.67</td><td>54.84</td></tr><tr><td>IRIS</td><td>92.36</td><td>91.26</td><td>74.60</td><td>33.88</td><td>97.22</td><td>95.44</td><td>92.15</td><td>90.58</td></tr><tr><td>FMS</td><td>63.35</td><td>57.02</td><td>62.05</td><td>42.86</td><td>66.94</td><td>70.92</td><td>74.41</td><td>66.31</td></tr><tr><td>S2</td><td>79.81</td><td>77.44</td><td>81.58</td><td>81.45</td><td>86.47</td><td>78.55</td><td>86.06</td><td>85.44</td></tr><tr><td>S3</td><td>83.06</td><td>89.41</td><td>87.33</td><td>33.11</td><td>96.99</td><td>95.23</td><td>97.49</td><td>97.51</td></tr><tr><td>n</td><td>20</td><td></td><td></td><td></td><td>50</td><td></td><td></td><td></td></tr><tr><td>HSD</td><td>61.86</td><td>58.28</td><td>63.35</td><td>53.72</td><td>68.75</td><td>63.95</td><td>66.67</td><td>54.60</td></tr><tr><td>BUPA</td><td>57.79</td><td>55.15</td><td>58.48</td><td>50.95</td><td>64.84</td><td>59.92</td><td>66.15</td><td>57.69</td></tr><tr><td>IRIS</td><td>95.72</td><td>95.00</td><td>87.41</td><td>66.56</td><td>99.27</td><td>98.33</td><td>94.33</td><td>67.88</td></tr><tr><td>FMS</td><td>68.02</td><td>64.96</td><td>69.12</td><td>45.36</td><td>82.60</td><td>82.27</td><td>78.82</td><td>55.84</td></tr><tr><td>S2</td><td>81.09</td><td>73.96</td><td>81.26</td><td>81.35</td><td>84.33</td><td>79.29</td><td>84.79</td><td>84.89</td></tr><tr><td>S3</td><td>91.99</td><td>91.69</td><td>93.29</td><td>63.82</td><td>97.05</td><td>95.08</td><td>97.69</td><td>78.43</td></tr></table>

Table 5  
Table 7  
The ranking results for the four classi<sup>fi</sup>ers.

<table><tr><td>n = 10</td><td colspan="4">Classifiers</td></tr><tr><td>Data sets</td><td>LDA</td><td>3-NN</td><td>SVM(linear)</td><td>SVM(radial)</td></tr><tr><td>HSD</td><td>2</td><td>3</td><td>1</td><td>4</td></tr><tr><td>BUPA</td><td>2</td><td>3</td><td>1</td><td>4</td></tr><tr><td>IRIS</td><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td>FMS</td><td>1</td><td>3</td><td>2</td><td>4</td></tr><tr><td>S2</td><td>3</td><td>4</td><td>1</td><td>2</td></tr><tr><td>S3</td><td>3</td><td>1</td><td>2</td><td>4</td></tr><tr><td> $R_i$ </td><td>2.00</td><td>2.67</td><td>1.67</td><td>3.67</td></tr><tr><td>Z value</td><td>0.45</td><td>1.34</td><td>*</td><td>2.68</td></tr></table>

$$
\begin{array}{l} Z = \frac {| R * - R _ {i} |}{S E}, i = 1, \dots , K \\ S E = \sqrt {\frac {K (K + 1)}{6 N}} = \sqrt {\frac {4 \times (4 + 1)}{6 \times 6}} = 0. 7 4 5 4. \end{array}
$$

The results for the Z value are shown in Table 5, where $R ^ { * }$ is the best $R _ { i } .$ When Z is larger than the critical value $z _ { 0 . 0 5 } = 1 . 6 4 5 ,$ , the performance of the classi<sup>fi</sup>er is considered to be statistically signi<sup>fi</sup>cantly better than those of the other methods.

Based on the above procedure, the other results of classi<sup>fi</sup>cation performance assessment, including computed values of Z and $F _ { F } ,$ are presented in Table 6 for $\boldsymbol { \mathrm { n } } = \{ 2 0 , 3 0 , 5 0 \}$ , where the Z values are the results of a Friedman test among the four classi<sup>fi</sup>ers, and the $F _ { F }$ values are used to assess whether the testing hypothesis is true or not. Here, when the values of $\dot { \boldsymbol { F } } _ { F }$ are larger than 3.287, and the Z values are considered statistically signi<sup>fi</sup>cant for the four classi<sup>fi</sup>ers. Note that the “\*” indicates that the classi<sup>fi</sup>er has the best R (i.e., R\*), and thus the best classi<sup>fi</sup>cation performance, and we use $R ^ { * }$ to calculate the $Z$ values of the other classi<sup>fi</sup>ers in Tables 5 and 6. The results of the Friedman test when n = {10,20} show that the classi<sup>fi</sup>er SVM(linear) has the best classi<sup>fi</sup>cation performance for the six data sets, as F is greater than 3.287. While this result is not statistically signi<sup>fi</sup>cant, as $F _ { F } = 3 . 0 4 < 3 . 2 8 7$ at $n = 3 0$ , we still tentatively select SVM(linear) as the best classi<sup>fi</sup>er. In addition. the LDA classifier is chosen to perform the classification at $n = 5 0$

## 4.5. The results of the experiment to compare the methods

Tables 7 and 8 show the results of the experiment, which include the average classi<sup>fi</sup>cation accuracies for methods PM3, PM2, MTD and REAL based on the signi<sup>fi</sup>cance levels of α′ = {0.01, 0.05, 0.10, 0.20}. The REAL method means using the best classi<sup>fi</sup>er without adding virtual samples, while the other methods all create virtual samples and add them to the original data set. For example, in data set HSD, the classi<sup>fi</sup>cation accuracy is increased from 59.82% to 64.95% by using the proposed method PM3 at $( n , \alpha ^ { \prime } ) = ( 1 0 , 0 . 0 1 )$ . Tables 7 and 8 also show the experimental results for the other data sets, where the values in bold indicate that the classi<sup>fi</sup>cation accuracy is better than that achieved with MTD and REAL at signi<sup>fi</sup>cance levels of $\alpha ^ { \prime } = \{ 0 . 0 1 , 0 . 0 5 , 0 . 1 0 , 0 . 2 0 \}$

Based on the Friedman test discussed in Section 4.4, the results of the experiment with regard to Z and $F _ { F }$ for PM3, PM2, MTD, and REAL methods are shown in Table 9 with α' set at 0.01, 0.05, 0.10, and 0.20 and $n = \{ 1 0 , 2 0 , 3 0 , 5 0 \}$ . Note that the "\*" indicates that the method has the best classi<sup>fi</sup>cation performance in Table 9. The results show that all values of $F _ { F }$ are larger than 3.287 (the standard for the results of the Friedman test to be statistically signi<sup>fi</sup>cant), indicating the effectiveness of the test. In addition, the Z values of the MTD and REAL methods are larger than 1.645, indicating that the PM3 and PM2 methods are statistically superior to these approaches for various different data sizes n = {10,20,30,50}.

Table 6  
The results of the Friedman test for classi<sup>fi</sup>ers.

<table><tr><td>Data size</td><td colspan="4">Z value</td><td rowspan="2"> $F_{F}$ </td></tr><tr><td>n</td><td>LDA</td><td>3-NN</td><td>SVM(linear)</td><td>SVM(radial)</td></tr><tr><td>10</td><td>0.45</td><td>1.34</td><td>*</td><td>2.68</td><td>4.34</td></tr><tr><td>20</td><td>0.67</td><td>2.01</td><td>*</td><td>2.68</td><td>5.00</td></tr><tr><td>30</td><td>0.45</td><td>1.79</td><td>*</td><td>2.24</td><td>3.04</td></tr><tr><td>50</td><td>*</td><td>1.57</td><td>0.45</td><td>2.46</td><td>3.49</td></tr></table>

## 4.6. Summary

Six data sets were used in this research to show the performance of the proposed method with regard to improving small data set classi<sup>fi</sup>cation. Based on the results of the experiment, as shown in Tables 7–9, we can make the following summary with regard to the proposed method. First, the proposed method has signi<sup>fi</sup>cantly better classi<sup>fi</sup>cation accuracy than the MTD and REAL for small sample sizes when the issue of modality is considered. Second, when the training data size is large enough, such as 50, the classi<sup>fi</sup>cation accuracy of the proposed method becomes close to that of the MTD, due to the effects of much over-lapping data. Third, after the data set has been estimated to be a multi-modal one, PM3 and PM2 have very similar results with regard to classi<sup>fi</sup>cation accuracy. Fourth, when the signi<sup>fi</sup>cance levels are set at 0.01, 0.05, 0.10, and 0.20 for the proposed method, the classi<sup>fi</sup>cation performance is better than that of the MTD.

## 5. Conclusion

Arti<sup>fi</sup>cially generating virtual samples to overcome the lack of knowledge in small data sets is an effective way to solve classi<sup>fi</sup>cation problems. This paper proposed a modality-test technique based on the Weibull density function to compute whether the number of modalities

Classi<sup>fi</sup>cation accuracies of the various methods with $\alpha ^ { \prime } = \{ 0 . 0 1 , 0 . 0 5 \}$

<table><tr><td> $\alpha'$ </td><td colspan="4">0.01</td><td colspan="4">0.05</td></tr><tr><td>Data sets</td><td>PM3</td><td>PM2</td><td>MTD</td><td>REAL</td><td>PM3</td><td>PM2</td><td>MTD</td><td>REAL</td></tr><tr><td>n</td><td>10</td><td></td><td></td><td></td><td>10</td><td></td><td></td><td></td></tr><tr><td>HSD</td><td>64.95</td><td>64.93</td><td>61.88</td><td>59.82</td><td>67.71</td><td>67.30</td><td>62.69</td><td>61.87</td></tr><tr><td>BUPA</td><td>60.34</td><td>61.31</td><td>58.39</td><td>57.64</td><td>60.69</td><td>60.46</td><td>58.92</td><td>58.84</td></tr><tr><td>IRIS</td><td>93.26</td><td>93.64</td><td>91.34</td><td>76.62</td><td>93.54</td><td>93.14</td><td>91.19</td><td>74.53</td></tr><tr><td>FMS</td><td>65.57</td><td>66.45</td><td>63.00</td><td>62.66</td><td>67.42</td><td>65.84</td><td>65.15</td><td>64.93</td></tr><tr><td>S2</td><td>80.15</td><td>80.05</td><td>77.64</td><td>76.34</td><td>82.42</td><td>82.04</td><td>80.84</td><td>79.65</td></tr><tr><td>S3</td><td>95.56</td><td>95.62</td><td>94.05</td><td>87.60</td><td>95.90</td><td>96.08</td><td>93.46</td><td>91.23</td></tr><tr><td>n</td><td>20</td><td></td><td></td><td></td><td>20</td><td></td><td></td><td></td></tr><tr><td>HSD</td><td>66.84</td><td>67.24</td><td>64.77</td><td>63.07</td><td>69.81</td><td>69.58</td><td>66.80</td><td>65.46</td></tr><tr><td>BUPA</td><td>62.76</td><td>62.87</td><td>61.41</td><td>60.43</td><td>60.28</td><td>62.44</td><td>60.70</td><td>59.20</td></tr><tr><td>IRIS</td><td>94.39</td><td>94.11</td><td>93.31</td><td>88.01</td><td>93.81</td><td>94.17</td><td>93.46</td><td>89.74</td></tr><tr><td>FMS</td><td>71.20</td><td>69.08</td><td>68.28</td><td>67.78</td><td>67.65</td><td>68.28</td><td>66.37</td><td>65.49</td></tr><tr><td>S2</td><td>86.70</td><td>86.37</td><td>84.83</td><td>83.41</td><td>83.17</td><td>82.89</td><td>80.78</td><td>79.39</td></tr><tr><td>S3</td><td>97.44</td><td>97.42</td><td>95.92</td><td>95.60</td><td>97.22</td><td>96.97</td><td>95.32</td><td>95.78</td></tr><tr><td>n</td><td>30</td><td></td><td></td><td></td><td>30</td><td></td><td></td><td></td></tr><tr><td>HSD</td><td>67.52</td><td>68.56</td><td>65.51</td><td>62.63</td><td>69.99</td><td>70.66</td><td>67.69</td><td>67.04</td></tr><tr><td>BUPA</td><td>62.36</td><td>61.45</td><td>60.23</td><td>60.88</td><td>63.67</td><td>62.80</td><td>62.51</td><td>61.69</td></tr><tr><td>IRIS</td><td>95.04</td><td>95.40</td><td>93.72</td><td>92.66</td><td>95.33</td><td>95.01</td><td>93.53</td><td>93.11</td></tr><tr><td>FMS</td><td>72.11</td><td>71.60</td><td>70.09</td><td>70.63</td><td>75.02</td><td>74.28</td><td>72.93</td><td>72.26</td></tr><tr><td>S2</td><td>83.12</td><td>83.44</td><td>82.21</td><td>81.22</td><td>81.24</td><td>81.77</td><td>79.20</td><td>78.78</td></tr><tr><td>S3</td><td>97.61</td><td>97.46</td><td>96.96</td><td>96.49</td><td>97.63</td><td>97.68</td><td>96.90</td><td>96.55</td></tr><tr><td>n</td><td>50</td><td></td><td></td><td></td><td>50</td><td></td><td></td><td></td></tr><tr><td>HSD</td><td>74.14</td><td>75.44</td><td>72.81</td><td>71.02</td><td>74.19</td><td>72.42</td><td>72.17</td><td>71.99</td></tr><tr><td>BUPA</td><td>62.71</td><td>61.95</td><td>60.99</td><td>60.12</td><td>64.20</td><td>63.41</td><td>62.64</td><td>62.38</td></tr><tr><td>IRIS</td><td>99.83</td><td>99.17</td><td>99.12</td><td>98.73</td><td>99.23</td><td>98.80</td><td>98.68</td><td>98.50</td></tr><tr><td>FMS</td><td>78.93</td><td>81.89</td><td>76.72</td><td>75.20</td><td>81.98</td><td>82.38</td><td>80.49</td><td>79.91</td></tr><tr><td>S2</td><td>85.16</td><td>84.76</td><td>83.36</td><td>81.91</td><td>86.89</td><td>86.42</td><td>85.97</td><td>84.62</td></tr><tr><td>S3</td><td>98.08</td><td>98.43</td><td>98.13</td><td>97.69</td><td>96.87</td><td>97.11</td><td>96.40</td><td>95.81</td></tr></table>

Table 8  
Classi<sup>fi</sup>cation accuracies of the methods with α′ = {0.10, 0.20}.

<table><tr><td> $\alpha'$ </td><td colspan="4">0.10</td><td colspan="4">0.20</td></tr><tr><td>Data sets</td><td>PM3</td><td>PM2</td><td>MTD</td><td>REAL</td><td>PM3</td><td>PM2</td><td>MTD</td><td>REAL</td></tr><tr><td>n</td><td>10</td><td></td><td></td><td></td><td>10</td><td></td><td></td><td></td></tr><tr><td>HSD</td><td>66.89</td><td>65.55</td><td>62.54</td><td>61.36</td><td>63.15</td><td>64.13</td><td>60.73</td><td>57.50</td></tr><tr><td>BUPA</td><td>60.94</td><td>60.18</td><td>58.17</td><td>58.09</td><td>59.99</td><td>59.33</td><td>57.62</td><td>56.80</td></tr><tr><td>IRIS</td><td>94.58</td><td>94.58</td><td>92.56</td><td>76.54</td><td>94.25</td><td>94.53</td><td>91.43</td><td>76.88</td></tr><tr><td>FMS</td><td>65.57</td><td>65.89</td><td>61.87</td><td>60.82</td><td>66.97</td><td>66.47</td><td>64.76</td><td>62.15</td></tr><tr><td>S2</td><td>83.51</td><td>83.27</td><td>81.07</td><td>79.37</td><td>82.15</td><td>81.48</td><td>78.98</td><td>76.49</td></tr><tr><td>S3</td><td>97.18</td><td>96.96</td><td>95.02</td><td>89.76</td><td>94.94</td><td>94.88</td><td>90.88</td><td>89.48</td></tr><tr><td>n</td><td>20</td><td></td><td></td><td></td><td>20</td><td></td><td></td><td></td></tr><tr><td>HSD</td><td>67.79</td><td>68.31</td><td>63.53</td><td>62.51</td><td>67.10</td><td>66.38</td><td>65.91</td><td>61.43</td></tr><tr><td>BUPA</td><td>62.51</td><td>62.62</td><td>61.44</td><td>59.91</td><td>61.33</td><td>60.82</td><td>58.87</td><td>57.55</td></tr><tr><td>IRIS</td><td>94.59</td><td>94.67</td><td>92.75</td><td>88.81</td><td>93.13</td><td>93.13</td><td>92.82</td><td>88.67</td></tr><tr><td>FMS</td><td>71.83</td><td>70.39</td><td>69.72</td><td>69.51</td><td>72.64</td><td>71.88</td><td>69.18</td><td>68.86</td></tr><tr><td>S2</td><td>83.59</td><td>83.72</td><td>81.85</td><td>80.73</td><td>84.02</td><td>84.40</td><td>82.86</td><td>81.82</td></tr><tr><td>S3</td><td>96.95</td><td>96.93</td><td>96.27</td><td>95.42</td><td>96.77</td><td>96.80</td><td>95.27</td><td>95.66</td></tr><tr><td>n</td><td>30</td><td></td><td></td><td></td><td>30</td><td></td><td></td><td></td></tr><tr><td>HSD</td><td>73.47</td><td>70.68</td><td>68.67</td><td>66.20</td><td>68.59</td><td>66.99</td><td>66.85</td><td>64.18</td></tr><tr><td>BUPA</td><td>63.72</td><td>63.52</td><td>62.99</td><td>62.81</td><td>62.54</td><td>63.01</td><td>61.98</td><td>60.56</td></tr><tr><td>IRIS</td><td>94.85</td><td>94.90</td><td>93.68</td><td>92.84</td><td>95.05</td><td>95.51</td><td>94.73</td><td>93.60</td></tr><tr><td>FMS</td><td>72.37</td><td>71.64</td><td>70.82</td><td>69.22</td><td>73.71</td><td>73.88</td><td>72.68</td><td>72.57</td></tr><tr><td>S2</td><td>85.02</td><td>85.09</td><td>83.97</td><td>82.98</td><td>83.36</td><td>83.09</td><td>81.67</td><td>79.77</td></tr><tr><td>S3</td><td>96.19</td><td>96.11</td><td>95.71</td><td>95.22</td><td>97.26</td><td>97.36</td><td>96.45</td><td>95.74</td></tr><tr><td>n</td><td>50</td><td></td><td></td><td></td><td>50</td><td></td><td></td><td></td></tr><tr><td>HSD</td><td>70.01</td><td>69.69</td><td>68.61</td><td>67.07</td><td>71.20</td><td>69.73</td><td>68.13</td><td>67.31</td></tr><tr><td>BUPA</td><td>64.84</td><td>64.07</td><td>63.79</td><td>63.45</td><td>64.14</td><td>64.10</td><td>63.95</td><td>63.86</td></tr><tr><td>IRIS</td><td>96.27</td><td>96.51</td><td>95.61</td><td>95.30</td><td>94.98</td><td>95.26</td><td>94.13</td><td>93.78</td></tr><tr><td>FMS</td><td>77.49</td><td>76.92</td><td>72.24</td><td>74.74</td><td>78.98</td><td>78.92</td><td>77.30</td><td>77.28</td></tr><tr><td>S2</td><td>85.05</td><td>85.02</td><td>83.65</td><td>83.02</td><td>86.77</td><td>86.27</td><td>84.95</td><td>83.79</td></tr><tr><td>S3</td><td>97.93</td><td>97.94</td><td>97.95</td><td>96.85</td><td>97.14</td><td>97.19</td><td>96.98</td><td>96.17</td></tr></table>

exceeds one in the density function. In addition, if the degree of variation in Weibull skewness between the original and virtual samples is low when the virtual sample size is gradually increased, then it is possible to decide the number of virtual samples that need to be generated based on this. With a given virtual sample size, the Weibull density function independently generates virtual samples after estimating the modality of the density function. The results, based on the six data sets, show that the classi<sup>fi</sup>cation accuracy of the proposed method is better than that obtained with the current, state-of-the-art MTD and REAL approaches. This work has thus demonstrated that virtual sample generation with the use of the proposed modality-test method and a computed virtual sample size is an effective way to enhance analytical performance in small data set learning.

Table 9  
The results of the Friedman test for the various methods.

<table><tr><td> $\alpha' = 0.01$ </td><td colspan="4">Z value</td><td rowspan="2"> $F_F$ </td></tr><tr><td>n</td><td>PM3</td><td>PM2</td><td>MTD</td><td>REAL</td></tr><tr><td>10</td><td>0.45</td><td>*</td><td>2.24</td><td>3.58</td><td>51.25</td></tr><tr><td>20</td><td>*</td><td>0.45</td><td>2.24</td><td>3.58</td><td>51.25</td></tr><tr><td>30</td><td>*</td><td>*</td><td>2.46</td><td>2.91</td><td>21.47</td></tr><tr><td>50</td><td>0.22</td><td>*</td><td>1.79</td><td>3.35</td><td>21.47</td></tr><tr><td> $\alpha' = 0.05$ </td><td colspan="4">Z value</td><td rowspan="2"> $F_F$ </td></tr><tr><td>n</td><td>PM3</td><td>PM2</td><td>MTD</td><td>REAL</td></tr><tr><td>10</td><td>*</td><td>0.89</td><td>2.46</td><td>3.80</td><td>85.00</td></tr><tr><td>20</td><td>0.22</td><td>*</td><td>2.01</td><td>3.13</td><td>14.57</td></tr><tr><td>30</td><td>*</td><td>*</td><td>2.01</td><td>3.35</td><td>45.00</td></tr><tr><td>50</td><td>*</td><td>0.45</td><td>2.24</td><td>3.58</td><td>51.25</td></tr><tr><td> $\alpha' = 0.10$ </td><td colspan="4">Z value</td><td rowspan="2"> $F_F$ </td></tr><tr><td>n</td><td>PM3</td><td>PM2</td><td>MTD</td><td>REAL</td></tr><tr><td>10</td><td>*</td><td>0.89</td><td>2.46</td><td>3.80</td><td>85.00</td></tr><tr><td>20</td><td>0.45</td><td>*</td><td>2.24</td><td>3.58</td><td>51.25</td></tr><tr><td>30</td><td>*</td><td>0.45</td><td>2.24</td><td>3.58</td><td>51.25</td></tr><tr><td>50</td><td>*</td><td>0.45</td><td>1.79</td><td>3.13</td><td>10.00</td></tr><tr><td> $\alpha' = 0.20$ </td><td colspan="4">Z value</td><td rowspan="2"> $F_F$ </td></tr><tr><td>n</td><td>PM3</td><td>PM2</td><td>MTD</td><td>REAL</td></tr><tr><td>10</td><td>*</td><td>0.45</td><td>2.24</td><td>3.58</td><td>51.25</td></tr><tr><td>20</td><td>*</td><td>0.45</td><td>2.46</td><td>3.35</td><td>29.62</td></tr><tr><td>30</td><td>0.45</td><td>*</td><td>2.24</td><td>3.58</td><td>51.25</td></tr><tr><td>50</td><td>*</td><td>0.45</td><td>2.24</td><td>3.58</td><td>51.25</td></tr></table>

Virtual sample generation is mainly used with numerical variables, and no method is appropriate in every situation. Hence, in future research, two research directions can be considered: One is generating virtual samples for category and nominal features, and the other is <sup>fi</sup>nding other density functions to generate more suitable virtual samples to enhance classi<sup>fi</sup>cation performance for different applications.

## Acknowledgment

This work was supported by the National Science Council, Taiwan (Project No. NSC 102-2221-E-006-239).

## References

[1] R.B. Abernethy, The New Weibull Handbook, <sup>fi</sup>fth ed., 2004, Robert Bob Abernethy, (536 Oyster Road, North Palm Beach, Florida).

[2] A. Asuncion, D.J. Newman, UCI Machine Learning Repository, University of California School of Information and Computer Science, Irvine, CA, 2007. (http://www.ics. uci.edu/mlearn/MLRepository.html)

[3] K.O. Bowman, L.R. Shenton, Weibull distributions when the shape parameter is de-<sup>fi</sup>ned, Computational Statistics & Data Analysis 36 (3) (2001) 299–310

[4] Y.-B. Chan, P. Hall, Using evidence of mixed populations to select variables for clustering very high-dimensional data, Journal of the American Statistical Association 105 (490) (2010) 798–809.

[5] C.-C. Chang, C.-J. Lin, LIBSVM: a library for support vector machines, ACM Transactions on Intelligent Systems and Technology 2 (3) (2011) 1–27.

[6] M.Y. Cheng, P. Hall, Mode testing in dif<sup>fi</sup>cult cases, The Annals of Statistics 27 (4) (1999) 1294–1315.

[7] S. Cho, M. Jang, S. Chang, Virtual sample generation using a population of networks, Neural Processing Letters 5 (2) (1997) 21–27.

[8] K. Das, Z. Nenadic, An ef<sup>fi</sup>cient discriminant-based solution for small sample size problem, Pattern Recognition 42 (5) (2009) 857–866.

[9] P.L. Davies, A. Kovac, Densities, spectral densities and modality, Annals of Statistics (2004) 1093–1136.

[10] J. Demšar, Statistical comparisons of classi<sup>fi</sup>ers over multiple data sets, The Journal of Machine Learning Research 7 (2006) 1–30.

[11] J. Durbin, M. Knott, C. Taylor, Components of Cramer–von Mises statistics. II, Journal of the Royal Statistical Society: Series B Methodological 37 (2) (1975) 216–237.

[12] A. Estabrooks, T. Jo, N. Japkowicz, A multiple resampling method for learning from imbalanced data sets, Computational Intelligence 20 (1) (2004) 18–36.

[13] M.H. Gail, J.L. Gastwirth, A scale-free goodness-of-<sup>fi</sup>t test for the exponential distribution based on the Gini statistic, Journal of the Royal Statistical Society: Series B Methodological 40 (3) (1978) 350–357.

[14] I. Good, R. Gaskins, Density estimation and bump-hunting by the penalized likelihood method exempli<sup>fi</sup>ed by scattering and meteorite data, Journal of the American Statistical Association 75 (369) (1980) 42–56.

[15] J.A. Hartigan, P. Hartigan, The dip test of unimodality, Annals of Statistics 13 (1) (1985) 70–84.

[16] T. Hastie, R. Tibshirani, J. Friedman, The Elements of Statistical Learning: Data Mining, Inference, and Prediction, second ed. Springer, New York, 2009.

[17] R.L. Iman, J.M. Davenport, Approximations of the critical region of the fbietkan sta tistic, Communications in Statistics—Theory and Methods 9 (6) (1980) 571–595.

[18] M. Knott, The distribution of the Cramér–von Mises statistic for small sample sizes, Journal of the Royal Statistical Society: Series B Methodological 36 (3) (1974) 430–438.

[19] D.C. Li, C.C. Chang, C.W. Liu, Using structure-based data transformation method to improve prediction accuracies for small data sets, Decision Support Systems 52 (3) (2012) 748–756.

[20] D.C. Li, Y.H. Fang, Y.M.F. Fang, The data complexity index to construct an ef<sup>fi</sup>cient cross-validation method, Decision Support Systems 50 (1) (2010) 93–102.

[21] D.C. Li, L.S. Lin, A new approach to assess product lifetime performance for small data sets, European Journal of Operational Research 230 (2) (2013) 290–298.

[22] D.C. Li, L.S. Chen, Y.S. Lin, Using functional virtual population as assistance to learn scheduling knowledge in dynamic manufacturing environments, International Journal of Production Research 41 (17) (2003) 4011–4024.

[23] D.C. Li, C.W. Liu, Extending attribute information for small data set classi<sup>fi</sup>cation, Knowledge and Data Engineering, IEEE Transactions on 24 (3) (2012) 452–464

[24] D.C. Li, C.S. Wu, T.I. Tsai, Y.S. Lina, Using mega-trend-diffusion and arti<sup>fi</sup>cial samples in small data set learning for early <sup>fl</sup>exible manufacturing system scheduling knowledge Computers & Operations Research 34 (4) (2007) 966–982

[25] Y.S. Lin, D.C. Li, The generalized-trend-diffusion modeling algorithm for small data sets in the early stages of manufacturing systems, European Journal of Operational Research 207 (1) (2010) 121–130

[26] S.N. Little, Weibull diameter distributions for mixed stands of western conifers, Canadian Journal of Forest Research 13 (1) (1983) 85–88.

[27] D.W. Müller, G. Sawitzki, Excess mass estimates and tests for multimodality, Journal of the American Statistical Association 86 (415) (1991) 738–746.

[28] M. Mannino, Y. Yang, Y. Ryu, Classi<sup>fi</sup>cation algorithm sensitivity to training data with non representative attribute noise, Decision Support Systems 46 (3) (2009) 743–751.

[29] T. Poggio, T. Vetter, Recognition and structure from one 2D model view: observations on prototypes, object classes and symmetries, DTIC Document, 1992.

[30] W. Polonik, Z. Wang, Estimation of regression contour clusters—an application of the excess mass approach to regression, Journal of Multivariate Analysis 94 (2) (2005) 227–249.

[31] B.W. Silverman, Using kernel density estimates to investigate multimodality, Journal of the Royal Statistical Society: Series B Methodological (1981) 97–99.

[32] A.S. Wahed, T.M. Luong, J.H. Jeong, A new generalization of Weibull distribution with application to a breast cancer data set, Statistics in Medicine 28 (16) (2009) 2077–2094.

[33] P. Xu, G.N. Brock, R.S. Parrish, Modi<sup>fi</sup>ed linear discriminant analysis approaches for classi<sup>fi</sup>cation of high-dimensional microarray data, Computational Statistics & Data Analysis 53 (5) (2009) 1674–1687.

[34] J. Yang, X. Yu, Z.-Q. Xie, J.-P. Zhang, A novel virtual sample generation method based on Gaussian distribution, Knowledge-Based Systems 24 (6) (2011) 740–748.

[35] L.F. Zhang, M. Xie, L.C. Tang, A study of two estimation approaches for parameters of Weibull distribution based on WPP, Reliability Engineering & System Safety 92 (3) (2007) 360–368.

![](/api/attachments/JJMAEGDT/fulltext/images/b3e155cb9232821bbe53b4ec9fb2951bd4cc2b3667c1a2a7376a96faa963f94e.jpg)

![](/api/attachments/JJMAEGDT/fulltext/images/ecd1bc20f01de2ea62eb510dbe9dbe261b899a479166e868d2071c8db70cddd9.jpg)

Der-Chiang Li is a Distinguished Professor at the Department of Industrial and Information Management, the National Cheng Kung University, Taiwan. He received his PhD degree at the Department of Industrial Engineering at Lamar University, Beaumont, Texas, USA, in 1985. As a research professor, his current interests concentrate on machine learning with small data sets.

Liang-Sian Lin is a doctoral candidate researcher at the De partment of Industrial and Information Management, the National Cheng Kung University, Taiwan. He is also working at the laboratory for small sample learning. As a research professor, his current interests concentrate on small data sets. His articles have appeared in European Journal of Operational Research and Decision Support Systems.
