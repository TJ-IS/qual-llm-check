---
otero_id: 7908
otero_key: "7D83F6ME"
title: "Efficient classifiers for multi-class classification problems"
authors: "Hung-Yi Lin"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.02.014"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Ef<sup>fi</sup>cient classi<sup>fi</sup>ers for multi-class classi<sup>fi</sup>cation problems

Hung-Yi Lin ⁎

Department of Distribution Management, National Taichung University of Science and Technology, 129 Sanmin Rd., Sec. 3, Taichung, Taiwan, ROC

a r t i c l e i n f o

Article history: Received 15 September 2011 Received in revised form 25 January 2012 Accepted 28 February 2012 Available online 7 March 2012

Keywords: Multivariate analysis Multi-class problems Feature evaluation Feature selection Feature extraction Inductive learning

## a b s t r a c t

Classi<sup>fi</sup>cation problems have become more complex and intricate in modern applications in the face of continuous data explosion. In addition to great quantities of features and large numbers of instances, modern classi<sup>fi</sup>cation applications are continuously developed with multiple classes (objectives). The everincreasing growth in data quantity and computation complexity has largely deteriorated the performance and accuracy of classi<sup>fi</sup>cation models. In order to deal with such situations, multivariate statistical analyses are adopted in this paper. Multivariate statistical analyses have two advantages. First, they can explore the relationships between variables and <sup>fi</sup>nd the most characterizing features of the observed data. Second, they can solve problems which are stalled by high dimensionality. In this paper, the <sup>fi</sup>rst advantage is applied to the selection of relevant features and the second is employed to generate the multivariate classi<sup>fi</sup>er. Experimental results show that our model can signi<sup>fi</sup>cantly improve classi<sup>fi</sup>cation training time by combining a compact subset of relevant features without the loss of accuracy in multi-class classi<sup>fi</sup>cation problems. In addition, the discrimination degree of our classi<sup>fi</sup>er outperforms other conventional classi<sup>fi</sup>ers.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

Classi<sup>fi</sup>cation is a problem frequently encountered when a categorical dependent variable (i.e., target classi<sup>fi</sup>cation variable) is analyzed and its relation to a set of independent variables is explored. It is dif<sup>fi</sup>cult for any single variable to distinguish multiple classes (objectives) to their fullest. In general, one class is satis<sup>fi</sup>ed while other classes suffer as a result. Classi<sup>fi</sup>cation problems with multiple classes introduce intricate interaction between dependent and independent variables so that they necessitate more efforts in analytical processing. Many multi-class classi<sup>fi</sup>cation problems are related to our modern daily life. For example, web page classi<sup>fi</sup>cation [34] facilitates the maintenance of web directories and the execution of focused crawling; web spam detection [2,8,9] can <sup>fi</sup>lter out unsolicited messages and enhance search quality; and medical diagnosis [12,17,24] can induce the notable symptom from personal anamneses or pathological images. In addition, mobile commerce behavior [28], fraud detection [4], bankruptcy or credit prediction [11,23,27,39], and crime activity analysis [15] have attracted a crowd of studies and led to many new researches.

Classi<sup>fi</sup>cation models have been discussed and assessed from many aspects. For example, what data structure or data type can classi<sup>fi</sup>ers cope with? Are variables invariant under transformations and applicable to the construction of classi<sup>fi</sup>ers? Are classi<sup>fi</sup>ers robust with respect to outliers? Are classi<sup>fi</sup>cation structures stable under different training instances? In order to provide objective assessment, three criteria are commonly employed to evaluate classi<sup>fi</sup>ers. They are model complexity, classi<sup>fi</sup>cation ef<sup>fi</sup>ciency, and classi<sup>fi</sup>cation accuracy. The complexity of a classi<sup>fi</sup>cation model signi<sup>fi</sup>es the computational costs and technical designs entailed in the model construction process. It is deeply affected by the involved variables and training algorithm. The ef<sup>fi</sup>ciency of a classi<sup>fi</sup>er is usually measured by its classi<sup>fi</sup>cation performance. In brief, what is the response time required for the given input data to conclude their classi<sup>fi</sup>cation results? Evaluating the accuracy rate of a classi<sup>fi</sup>er is a very intuitive assessment method. High accuracy usually accompanies high model complexity and low ef<sup>fi</sup>ciency. Therefore, it is a challenge to design a classi<sup>fi</sup>cation model which can optimize the above three criteria. Modern applications allocate datasets with numerous attributes and the corresponding attribute values are rapidly accumulated into a huge size. The well-designed analytical methods are highly expected to ease the heavy computations on such enormous datasets. For instance, in bioinformatics, comparative method using score computation combined with probabilistic model was employed to identify functional RNA for the study of human genome [32,36]. In pharmacology, multiple evaluation methods were applied to drug screening [6]. In [29], the problem of building multiclass classi<sup>fi</sup>ers for tissue classi-<sup>fi</sup>cation according to gene expression was studied.

On one hand, the complexity of classi<sup>fi</sup>cation model is generally disproportional to its classi<sup>fi</sup>cation ef<sup>fi</sup>ciency. The higher the data dimensionalities, the more data are generated, thus incurring greater analytical efforts and computational costs. This is why classi<sup>fi</sup>cation ef<sup>fi</sup>ciencies draw much attention from the data mining community. On the other hand, it is a trade-off situation that losing some classi<sup>fi</sup>cation ef<sup>fi</sup>ciency can in return gain some classi<sup>fi</sup>cation accuracy and vice versa. This situation is the challenge frequently encountered in data mining problems. There is no doubt that exploring a model which can simultaneously promote classi<sup>fi</sup>cation ef<sup>fi</sup>ciency and accuracy is highly desired. The goal of classi<sup>fi</sup>cation models is to develop an effective supervised learning method, which can train the observed data with ef<sup>fi</sup>ciency and accomplish the entire classi<sup>fi</sup>cation task with high accuracy.

To achieve this goal, many studies [7,19,25,44] adopted the strategy of data dimensionality reduction (DDR). Feature extraction and feature selection are two special forms of DDR. Feature extraction can transform input data into a reduced representation set of features (also named feature vectors). Instead of using the full-size input, the extracted characterizing information simpli<sup>fi</sup>es the classi<sup>fi</sup>cation task. Feature selection [26,30,40,42] is the technique of identifying the most characterizing features to facilitate the classi<sup>fi</sup>cation task. However, as stated in [25,33,43], the m best features are not the best m features. In other words, combinations of individually good features do not necessarily lead to good classi<sup>fi</sup>cation performance. Feature selection must remove irrelevant and redundant features so as to sustain subsequent classi<sup>fi</sup>cation. Feature extraction and feature selection both aim at improving classi<sup>fi</sup>cation performance and accuracy by alleviating the effect of the curse of dimensionality. In this paper, we integrate the superiorities of feature selection and feature extraction into our novel learning model.

This paper is organized as follows. Section 2 reviews the past methods and strategies for approaching multi-class classi<sup>fi</sup>cation problems. The motivation of applying multivariate analysis to multiclass problems is also given in Section 2. Section 3 proposes the issues for large multi-class problems, i.e., classi<sup>fi</sup>cation problems with multiple classes and massive features. Section 4 presents the detailed construction procedures of our learning model. The heuristic algorithm of feature selection and the integrated manipulation of multivariate analysis and principal component analysis are also described in this section. The experimental and analytical results are presented in Section 5. Finally, concluding remarks are given in the last section.

## 2. Multi-class classi<sup>fi</sup>cation problems

Many learning algorithms are inherently binary and they can discriminate instances between two classes. However, modern problems often encounter more complicated situations with multiple classes [1,5,13,47]. There are two principal approaches to applying twoclass learning algorithms to multi-class problems. Pairwise classi<sup>fi</sup>cation [18,21] turns a single k-class learning problem into k(k−1)/2 two-class problems. One-against-all class binarization [14,22] transforms a k-class problem into k two-class problems, which are constructed by using the instances of class i as the positive instances and the instances of classes j $( j = 1 . . . k , j \neq i )$ as the negative instances. In a case where ordered classes are considered, decomposition of a single multi-class problem into several two-class sub-problems is problematic. Take a credit approval dataset for example. Customers' basic data (e.g., age and housing status), credit and <sup>fi</sup>nancial grading (e.g., status of checking account and credit history), and job-related rating (e.g., employment in years and job attribute) are employed to predict four credit levels: high (denoted as H), good (G), normal (N), and bad (B). When pairwise classi<sup>fi</sup>cation is applied, the classi-<sup>fi</sup>ers constructed using two continuous credit levels (e.g., H vs. $G ,$ or G vs. N) have lower discrimination than those constructed using discontinuous credit levels (e.g., H vs. B, or G vs. B). On the other hand, when one-against-all class binarization is applied, improper data separation may cause distinct classes to be collected into the same group and such preposterous handling will disturb the discrimination of classi<sup>fi</sup>ers. For example, the instances corresponding to class G are taken as positive and the instances corresponding to classes H, N, and B are taken as negative. Or, class N is taken as positive while classes H, G, and B are taken as negative. Moreover, imbalanced data and overweighed outliers in sub-problems could deeply affect the quality of classi<sup>fi</sup>ers. Huge effort derived from multiple training tasks is another worry.

The policy of separate-and-conquer suffers the problem of how to decompose or separate data into appropriate subgroups for inductive learning. The extension from a two-class to a multi-class classi<sup>fi</sup>cation problem is not so intuitive that it often incurs unexpected complexity and poor performance. Pairwise classi<sup>fi</sup>cation tends to have inconsistent discrimination effects due to the combinations of improper pairs of classes. One-against-all class binarization easily encounters two dif-<sup>fi</sup>culties. One is similar to that of pairwise classi<sup>fi</sup>cation and the generation of a consistent result could then be a bottleneck. The other dif<sup>fi</sup>culty arises because contrary classes should not be integrated into the same subgroup. In view of the distinct characteristics of multi-class classi<sup>fi</sup>cation problems, we propose a new approach to solving them.

Multi-class classi<sup>fi</sup>cation problems over high-dimensional datasets pose many challenges. Firstly, the involvement of a large number of variables always complicates the classi<sup>fi</sup>cation task. Decision trees [31] or rule-based methods [13] impose so many decision nodes or conditions that the explanation abilities of classi<sup>fi</sup>ers are arduous. Simultaneously, the tremendous amount of decision rules frequently puzzles users. Secondly, high dependences among variables can deteriorate classi<sup>fi</sup>cation performance and affect classi<sup>fi</sup>cation accuracy. In high-dimensional datasets, the use of highly correlated variables could confuse the learning process and in turn increase the computational overhead. CART algorithm spends a huge effort and yet gains negligible improvement of accuracy in return. Thirdly, multiple classes increase data patterns and request classi<sup>fi</sup>ers to be equipped with higher discrimination capability. The number of classes is usually disproportional to classi<sup>fi</sup>cation accuracy. SVMs [3,46] investigate separately all possibilities of two categories even though some classes may lack suf<sup>fi</sup>cient information or include outlier data. Hence, the drawback of SVMs is that some well-trained classi<sup>fi</sup>ers could be encumbered with the poorly trained classi<sup>fi</sup>ers. Finally, data granularity is usually neglected when developing learning method. This concern is addressed in Section 3.3.

Principal component analysis (PCA) is often used as the linear technique for dimensionality reduction. It performs linear mapping of the data to a lower dimensional space in such a way that the variance of the data in the low-dimensional representation is maximized. In practice, the correlation matrix of the data is constructed and the eigenvalues and eigenvectors on this matrix are computed. The largest eigenvalues (the <sup>fi</sup>rst principle components) are utilized as indicators to represent the large-scale physical behavior of the system. The comparison of the largest eigenvalues assists in designing our heuristic feature selection algorithm. In addition, at the subsequent stage of feature extraction, PCA is eventually utilized in the process of dimensionality reduction and thus generates multivariate classi<sup>fi</sup>ers for classi<sup>fi</sup>cation tasks.

To avoid getting stuck in heavy data analysis and computation, the characterizing variables with high relevance to the target classi<sup>fi</sup>cation variable should be authenticated as easily as possible. The completeness of classi<sup>fi</sup>cation task usually depends on a subset of relevant features. However, the respective class-discriminative power derived from different features can have great overlaps and contribute similar classi<sup>fi</sup>cation effects. Such redundancy in a collection of highly relevant features still impedes the enhancement of classi<sup>fi</sup>cation quality. An ideal subset of features should be voted under a situation that every selected feature can support different class-discriminative effects and they can cooperate well to complete the entire classi<sup>fi</sup>cation task. Similarly, the heuristic minimal-redundancy-maximal-relevance (mRMR) framework proposed in [33] can facilitate feature selection schemes and obtain a compact subset of superior features. To eliminate the abovementioned defect, multivariate statistical analysis is employed in this paper to formulate relationships between variables and the correlations between relevant features are carefully examined.

For the categorization of multiple con<sup>fl</sup>icting classes, the <sup>fi</sup>rst goal of this paper is to authenticate a compact subset of relevant features with high class-discriminative power. To this end, a new feature evaluation method involving data distribution and data variation is proposed. Moreover, a novel heuristic algorithm for feature selection is established to prevent redundancy problem. The second goal of this paper is to propose a simple learning model, which can speed up the classi<sup>fi</sup>cation training process. The last goal of this paper is to construct a multivariate classi<sup>fi</sup>er which is capable of implementing ef<sup>fi</sup>cient classi<sup>fi</sup>cation tasks with satisfactory accuracy. The contributions of this paper include the design of feature evaluation, the scheme of feature selection, the scheme of feature extraction, and the inductive learning process.

## 3. Issues for multiple classes and massive features

Before presenting our new learning model in Section 4, we discuss three issues regarding multiple classes and massive features. According to our observations between binarization and multi-class classi<sup>fi</sup>- cations, data variation (i.e., data variance) inside every subset and data distribution are both taken into account. In addition, the importance of handling redundancy is proved in Section 3.2. In order to strengthen the validity of using multivariate statistical analysis, Section 3.3 proposes the viewpoint of data granularity.

## 3.1. Data impurity and proximity

The main concept of Shannon's information theory quanti<sup>fi</sup>es the uncertainty involved in predicting the value of a random variable. Information theory is developed from probability theory and statistics. The most important quantities of information are entropy, which measures the amount of uncertainty associated with a discrete random variable. Information Gain is an entropy-based way of comparing two distributions in a manner that assumes q(X) to be the distribution underlying some data and $p ( X )$ to be the correct distribution. It is thus de<sup>fi</sup>ned as $\scriptstyle I G ( p ( X ) | q ( X ) ) = \sum _ { x \in X } p ( x )$ log <sup>p</sup> <sup>x</sup><sub>ð</sub> <sub>Þ</sub>. q x Information Gain <sup>ð Þ ð Þ</sup>Ratio adds the factor of population information amount. These entropy-based criteria all focus on evaluating the random variables with two classes (i.e., yes vs. no, or high vs. low, or good vs. bad). Although the analyses of data distribution (i.e., the statistical dispersion of data) can help distinguish the quality of classi<sup>fi</sup>cation effect, classi-<sup>fi</sup>cation problems involving multiple classes tend to have large data variation inside every subset. We illustrate this point with the following example. As shown in Fig. 1(a), a small dataset has two independent variables $( x , \ y )$ and four classes in its target classi<sup>fi</sup>cation variable c. After classifying all instances using x and $y ,$ the resulting subsets are depicted in Figs. 1(b) and (c), respectively. Intuitively, we vote x as the better feature than y since the entropy gained from $x \ ( { \mathrm { i } } . { \mathrm { e } } . , 0 . 9 2 )$ is better than that from $y \ ( \mathrm { i } . \mathrm { e } . , 1 )$ . However, the average data variance of $S _ { 1 }$ and $S _ { 2 } ~ ( \mathrm { i . e . , 0 . 8 9 } )$ is greater than that of $\overline { { S } } _ { 3 }$ and $S _ { 4 }$ (i.e., 0.25). Or, the data distribution in $S _ { 1 }$ has the probabilities of 0.67 $( c = 1 )$ and 0.33 $\left( c = 3 \right)$ , which have higher consistency than that in $S _ { 3 } ,$ the probabilities of $0 . 5 \ ( c = 1 )$ and $0 . 5 \ ( c = 2 )$ . The same condition happens to $S _ { 2 }$ and $S _ { 4 } .$ However, data variation in $S _ { 1 }$ (and $S _ { 2 } )$ is greater than that in $S _ { 3 }$ (and $S _ { 4 } )$ . As is well known, feature evaluation methods using the criterion of data distribution concern only the impurity inside each subset. Multiple classes make proximity another concern, which is ignored by many conventional evaluation criteria. Criteria such as entropy-based methods and Gini index are insuf<sup>fi</sup>cient to evaluate the features in multi-class problems. Our new evaluation criteria will give consideration to both impurity and proximity. The detailed design is given in Section 4.1.

![](/api/attachments/7D83F6ME/fulltext/images/8c4b6a08328dd5cbde314ac5a34b8d5d8e242437a66711594bc1a982ab437bde.jpg)  
Fig. 1. An example with six instances.

## 3.2. Relevance and redundancy analyses

The dependence between different variables could be positive, negative, or none. Positive and negative dependences respectively indicate identical and opposite movements in the trend. Correlation coef<sup>fi</sup>cient is a useful indicator for dependence detection. The detection of correlations between independent and dependent variables helps evaluate the relevance degree of features to the target feature. The highly relevant features are expected. On the other hand, the detection of correlations between independent variables can facilitate the discrimination of redundancy. Two highly correlated features have similar class-discriminative effects while two lowly correlated features possess different respective class-discriminative powers. The utilization of correlation coef<sup>fi</sup>cient in our study is completely different from that in many recent studies [26,39,42]. On one hand, in this paper, we call the task of exploring the relevant features to the target classi<sup>fi</sup>cation variable as relevance analysis. Entropy-based criteria and Gini index are typical relevance analyses for classi<sup>fi</sup>cation problems. Section 4.1 presents a sound relevance analysis for multi-class problems. On the other hand, the task of discriminating the dependence between independent features is called redundancy analysis. The following theorem and corollary verify the importance of redundancy analysis

Theorem. Assume that the entropy gained from variable x is denoted as $H ( x )$ . Then, $H ( a x ) = H ( x )$ and $\begin{array} { r } { H ( x + b ) = H ( x ) } \end{array}$ , where a and b are constants.

Proof. The data values (magnitudes) of variable x are simply employed to differentiate varieties of subclasses; hence, their values are not included in the calculation of entropy. Multiplication and shifting of variable x retain the same differentiability as the original X for the underlying data. Therefore, we have $\begin{array} { r } { H ( a x ) = H ( x + b ) = H ( x ) } \end{array}$ . ■

Corollary. If two variables x and y are highly correlated, then $H ( a x +$ by) is approximately measured as $H ( x )$ or $H ( y )$

Proof. A linear regression model $y = \alpha + \beta x + \varepsilon \mathrm { c a n }$ be employed to <sup>fi</sup>t the relationship between x and $y ,$ where intercept αand effect $\beta \cong \pm 1$ can be obtained by using the least squares approach. In the case of highly positive correlation, variable y can be approximately modeled asα+xand the entropy gained from variable $a x + b y$ can be concluded as follows:

$$
\begin{array}{l} H (a x + b y) = H (a x + b (\alpha + x)) = H ((a + b) x + b \alpha) = H ((a + b) x) \\ = H (x) \end{array}
$$

On the other side, in the case of highly negative correlation, variable y can be approximately modeled asα−xand the entropy gained from variable ax+by can also be concluded as $H ( x )$ in a similar way. ■

The corollary reveals the fact that the classi<sup>fi</sup>cation effect gained from a set of highly correlated features is similar to that gained from a single feature. To prevent duplicate discrimination effects from being included in the classi<sup>fi</sup>cation process, redundancy analysis among selected features should be carefully inspected. In order to simplify classi<sup>fi</sup>cation complexity, precise designs of relevance and redundancy analyses are important.

## 3.3. Data granularity

Data granularity refers to the <sup>fi</sup>neness with which data <sup>fi</sup>elds can be sub-divided. For example, census data can be recorded, with low granularity or coarse-grained description, as a single statement:

[one has 6 children at the age of 45 and his education level and standard of living are high], or with high granularity or <sup>fi</sup>ne-grained description, as multiple statements:

1. [Age= 45]

2. [Number of children=6]

3. [Education level=high]

4. [Standard of living=high]

Conventional decision trees adopt the concept of <sup>fi</sup>ne granularity in every single decision node, which classi<sup>fi</sup>es instances level by level. The initial classi<sup>fi</sup>cation triggered by the root node determines the subsequent handling. An adequate high-level decision can simplify the classi<sup>fi</sup>cation tasks assigned at low levels. In the case of multiclass classi<sup>fi</sup>cation, every single variable pays close attention to its own data dimension. It is dif<sup>fi</sup>cult to vote the most adequate variable and locate it in the root node for generating the optimal classi<sup>fi</sup>cation effect for all subsequent handling. As a result, different types of decision trees can build different classi<sup>fi</sup>cation models and achieve different effectiveness. In fact, the exploration of an optimal decision tree for multi-class problem is a NP-complete problem.

Now that a thoughtful classi<sup>fi</sup>cation is usually accomplished by the cooperation of a collection of relevant variables, data classi<sup>fi</sup>cation according to coarse granularity does not have a bias in favor of one single data dimension but simultaneously takes multiple data dimensions into account. That is, instead of applying univariate classi<sup>fi</sup>cation, the learning model with multivariate classi<sup>fi</sup>er can take more aspects into account and in turn achieve better classi<sup>fi</sup>cation quality.

## 4. Construction of learning model

## 4.1. Feature evaluation with relevance analysis

Gini impurity is computed by multiplying the probability of each chosen item with the probability of a mistake in categorizing that item, while information gain and information gain ratio are calculated using Shannon's entropy. Shannon's entropy is a broad and general concept, which studies the amount of information in a transmitted message. The probabilities that a particular message actually transmitted was a measure of how much information was in the message. Data patterns with diverseness are inherently hidden in multi-class problems. In addition to the information from data distribution, multi-class problems necessitate further investigation for explicit analyses. We simply integrate the information of data variation into Shannon's entropy and call this new criterion enhanced entropy (abbreviated as EH).

$$
E H (x, T) = \sum_ {i = 1} ^ {n} \frac {| T _ {i} |}{| T |} \times H (x, T _ {i}) \times \sigma^ {2} (T _ {i}),
$$

where feature x takes on values in $\{ 1 , 2 , . . . , n \}$ and splits the train set T into subset $T _ { i } , i { \in } \{ 1 , 2 , \cdots , n \}$ . In this design, the success of approving relevant features relies on the identi<sup>fi</sup>cation of low entropy and low data variation. This is why the summation of the product $\mathsf { o f } H ( x , T _ { i } )$ andσ $\scriptstyle \int ^ { 2 } ( T _ { i } )$ for all subsets becomes a better criterion for the feature evaluation of multi-class problems.

Ref. [35] has revealed no signi<sup>fi</sup>cant difference between Gini index and information gain criteria. The behavior of these two split functions is so similar that the probability in selecting the same splits is as high as 98%. Therefore, when numeric attribute x is tested for multi-class problems, Gini index can be modi<sup>fi</sup>ed in a similar way as Shannon's entropy, i.e.,

$$
\text { Enhanced } _ {G} \text { ini } (x, T) = \sum_ {i = 1} ^ {n} \frac {| T _ {i} |}{| T |} \times \text { Gini } (T _ {i}) \times \sigma^ {2} (T _ {i}).
$$

Similar to the design of information gain, EH(x, T)is compared with the initial status before splitting. Such improvement is called aggregation gain and de<sup>fi</sup>ned as $I ( T ) \times \sigma ^ { 2 } ( T ) - E H ( x , T ) ,$ , where I(T) is the total entropy and $\sigma ^ { 2 } ( T )$ is the total variance before splitting. AG(x, T) is taken to represent the aggregation gain obtained by adopting feature x. The greater $A G ( x , T )$ means that the feature x has higher relevance to the target classi<sup>fi</sup>cation variable.

## 4.2. Feature selection with redundancy analysis

After all features in a dataset are evaluated by our proposed AG criterion, the feature with the largest estimation is picked and it serves as the basis for the selection of the second feature. Data dependences between the <sup>fi</sup>rst selected feature and the other features are investigated. As mentioned in Section 3.2, highly correlated features have to be distinguished to avoid redundancy. The second relevant feature is selected according to the condition that its AG stays at a high level and its correlation with the <sup>fi</sup>rst selected feature is low. Such design is scheming out a way to supplement the insuf<sup>fi</sup>ciency of early selected features and in turn strengthens the collaborative classdiscriminative effect. Accordingly, the selections of the third and subsequent relevant features follow a similar procedure. The features classi<sup>fi</sup>ed as relevant in the late selection process have less effectiveness than those in the early process. In order to retain good performance, we propose a stop criterion for this heuristic selection process in the subsequent discussion.

An example is taken to explain our heuristic selection process in detail. As shown in Table 1, a small dataset (denoted as T) investigates the information regarding gender, car ownership, travel cost, and income for 10 instances. Three classes of transportation mode (bus, train, and car) are employed to classify these instances. The <sup>fi</sup>rst feature (x ) has two nominal values: male and female. The second feature has three numeric values: $x _ { 2 } = 0 ,$ 1, and 2. The third and fourth features both have three ordinal values representing three different levels. First of all, the probabilities of the three transportation modes are 0.3, $_ { 0 . 4 , }$ and 0.3 so thatI(T) is formulated as −0.3×log $_ 2 0 . 3 -$ $0 . 4 { \times } \log _ { 2 } ( 0 . 4 - 0 . 3 { \times } \log _ { 2 } ( 0 . 3 { \mathrm { a n d } }$ the result is 1.571. On the other hand, $\sigma ^ { 2 } ( T )$ is measured as 0.6 when bus, train, and car are respectively assigned as class numbers 1, 2 and 3. Therefore $I ( T ) \times \sigma ^ { 2 } ( T ) \mathrm { i }$ is evaluated to be 0.943. The evaluations of information gain (abbreviated as $I G ) ,$ gain ratio (abbreviated as $G R )$ , and AG for x , x , x and $x _ { 4 }$ are listed in Table 2. IG and GR both vote $x _ { 3 }$ as the <sup>fi</sup>rst relevant feature while AG votes x . Fig. 2 outlines the subclasses classi<sup>fi</sup>ed by $x _ { 2 }$ and $x _ { 3 } .$ Note that the subclasses are well classi<sup>fi</sup>ed except the <sup>fi</sup>rst subclass of {1 bus, 1 train, 3 cars} in Fig. 2(a) and the <sup>fi</sup>rst subclass of {3 buses, 2 cars} in Fig. 2(b). After the maximum support is used as the <sup>fi</sup>nal class identi<sup>fi</sup>er, there are two instances misclassi<sup>fi</sup>ed by $x _ { 2 }$ and $x _ { 3 } ;$ that is, 1 bus and 1 train in Fig. 2(a) and 2 cars in Fig. 2(b). The data variation in {1 bus, 1 train, 3 cars} is less than that in {3 buses, 2 cars}; that is why our AG authenticates $x _ { 2 }$ better than $x _ { 3 }$ (the shadow part in

Table 1 A small dataset.

<table><tr><td rowspan="2">Instance no.</td><td colspan="4">Features</td><td rowspan="2">Class(C)</td></tr><tr><td>Gender (x1)</td><td>Car ownership (x2)</td><td>Travel cost (x3)</td><td>Income level (x4)</td></tr><tr><td>1</td><td>Male</td><td>0</td><td>Cheap</td><td>Low</td><td>Bus</td></tr><tr><td>2</td><td>Male</td><td>1</td><td>Cheap</td><td>Medium</td><td>Bus</td></tr><tr><td>3</td><td>Female</td><td>1</td><td>Cheap</td><td>Low</td><td>Bus</td></tr><tr><td>4</td><td>Female</td><td>0</td><td>Expensive</td><td>High</td><td>Train</td></tr><tr><td>5</td><td>Female</td><td>2</td><td>Expensive</td><td>Medium</td><td>Train</td></tr><tr><td>6</td><td>Male</td><td>2</td><td>Expensive</td><td>Medium</td><td>Train</td></tr><tr><td>7</td><td>Female</td><td>2</td><td>Expensive</td><td>Medium</td><td>Train</td></tr><tr><td>8</td><td>Male</td><td>0</td><td>Cheap</td><td>Medium</td><td>Car</td></tr><tr><td>9</td><td>Female</td><td>0</td><td>Cheap</td><td>High</td><td>Car</td></tr><tr><td>10</td><td>Female</td><td>0</td><td>Standard</td><td>Medium</td><td>Car</td></tr></table>

Measurements for three criteria.

<table><tr><td>Rank</td><td colspan="2">IG</td><td colspan="2">GR</td><td colspan="2">AG</td></tr><tr><td>1</td><td> $x_{3}$ </td><td>1.086</td><td> $x_{3}$ </td><td>0.798</td><td> $x_{2}$ </td><td>0.50</td></tr><tr><td>2</td><td> $x_{2}$ </td><td>0.886</td><td> $x_{2}$ </td><td>0.596</td><td> $x_{3}$ </td><td>0.48</td></tr><tr><td>3</td><td> $x_{4}$ </td><td>0.496</td><td> $x_{4}$ </td><td>0.361</td><td> $x_{4}$ </td><td>0.48</td></tr><tr><td>4</td><td> $x_{1}$ </td><td>0.096</td><td> $x_{1}$ </td><td>0.098</td><td> $x_{1}$ </td><td>0.12</td></tr></table>

Table 2). Note that features $x _ { 3 }$ and $x _ { 4 }$ have the same $A G ,$ thus making them competitors in the next round. Feature $x _ { 1 }$ has the lowest AG and is so signi<sup>fi</sup>cantly different from $x _ { 3 }$ and $x _ { 4 }$ that it is an irrelevant feature. Hence, $x _ { 1 }$ is excluded from further processing.

Features $x _ { 3 }$ and $x _ { 4 }$ are then examined for their dependences on $x _ { 2 } .$ The correlation coef<sup>fi</sup>cient of $\left( x _ { 2 } , x _ { 4 } \right)$ is obviously smaller than that of $( x _ { 2 } , x _ { 3 } ) ;$ ; hence, $x _ { 4 }$ is selected as the second relevant feature. To verify the validity of our selection, two C4.5 decision trees are constructed using $\left( x _ { 2 } , x _ { 3 } \right)$ and $( x _ { 2 } , x _ { 4 } )$ , respectively. Tables $3 ( \mathsf { a } )$ and (b) show the confusion matrixes corresponding to the decision tree constructed using $\left( x _ { 2 } , x _ { 3 } \right)$ and $\left( x _ { 2 } , x _ { 4 } \right)$ , respectively. The <sup>fi</sup>rst classi<sup>fi</sup>er has the accuracy of 0.5 while the second classi<sup>fi</sup>er achieves a higher accuracy of 0.8, revealing that the collaborative classi<sup>fi</sup>cation effect achieved by a subset of highly relevant features with low correlation is better than that achieved by a subset of highly relevant features with high correlation.

Our heuristic selection process is different from stepwise regression. The only similarity is that the selection of a good feature depends on its importance to the target classi<sup>fi</sup>cation variable and only one feature is selected in every round. To avoid the problem of collinearity, stepwise regression can be employed to remove those elected variables whose predictive effect can be replaced by another variable. However, our method adopts a thoughtful authentication mechanism that does not remove any selected features from the set. The most signi<sup>fi</sup>cant difference is that stepwise regression never considers simultaneously all the combinations of selected features while our method checks the collaborative effect derived from the selected features. In the next subsection, multivariate analysis is employed to achieve these designs.

## 4.3. Determining number of features with multivariate analysis

Selecting a compact subset of relevant features is important to classi<sup>fi</sup>cation quality and classi<sup>fi</sup>cation performance. How to determine a subset with necessary and sufficient features is another issue when supporting an ef<sup>fi</sup>cient classi<sup>fi</sup>er. AG-based relevance and redundancy analyses are employed to ensure that necessary features are included in our model. To the other concern of sufficiency, multivariate analysis combined with a heuristic mechanism completes our entire feature selection process. The <sup>fi</sup>rst eigenvalues $\lambda _ { 1 }$ extracted from the multivariate analyses are utilized to indicate the major variability preserved by a subset of features. A largerλ means higher variability preserved in the first principle component and in turn the features involved can provide the most suf<sup>fi</sup>cient information for the classi<sup>fi</sup>cation task. Take again the example in Section 4.2. The <sup>fi</sup>rst eigenvalues extracted from the multivariate analyses using $( x _ { 2 } ,$ $x _ { 4 } ) , ( x _ { 2 } , x _ { 4 } , x _ { 3 } )$ and $\left( x _ { 2 } , x _ { 4 } , x _ { 3 } , x _ { 1 } \right)$ are listed in Table 4. The incremental percentages are also displayed in the last column. As can be seen, the addition of $x _ { 3 }$ has a signi<sup>fi</sup>cant effect on $( x _ { 2 } , x _ { 4 } )$ while $x _ { 1 }$ makes less contribution to $( x _ { 2 } , \ x _ { 4 } , \ x _ { 3 } )$ . Again, we verify that $x _ { 1 }$ should be excluded. Such selection can heuristically collect relevant features and its progress depends on the growth of eigenvalues.

Table 3 Confusion matrixes.

<table><tr><td rowspan="3"> $(x_2, x_3)$ </td><td colspan="3">(a)</td><td rowspan="3"> $(x_2, x_4)$ </td><td colspan="3">(b)</td></tr><tr><td colspan="3">Classified as</td><td colspan="3">Classified as</td></tr><tr><td>Bus</td><td>Train</td><td>Car</td><td>Bus</td><td>Train</td><td>Car</td></tr><tr><td>Bus</td><td>2</td><td>0</td><td>1</td><td>Bus</td><td>2</td><td>0</td><td>1</td></tr><tr><td>Train</td><td>0</td><td>3</td><td>1</td><td>Train</td><td>0</td><td>3</td><td>1</td></tr><tr><td>Car</td><td>2</td><td>1</td><td>0</td><td>Car</td><td>0</td><td>0</td><td>3</td></tr></table>

For the completeness of our learning model, we present below the algorithm of this heuristic selection process in detail.

The notations used in the algorithm are as follows.

• F: The set of all original features whose size exceeds 2.

• A: The set of candidate features for selection.

$B _ { 1 } , B _ { 2 } \colon$ The sets for collecting relevant and lowly correlated features.

$\alpha , \beta , \gamma \colon$ The <sup>fi</sup>rst, second and third selected features.

$r ( \beta , \gamma ) \colon$ The correlation coef<sup>fi</sup>cient between features $\beta$ and γ.

• λ (S): Apply multivariate analysis to S and extract the <sup>fi</sup>rst eigenvalue from the correlation matrix.

• ψ: The threshold for determining whether to proceed with the selection procedure or not.

## Feature selection

Input: the training dataset T

Output: the set containing selected features

1. Sort all features in F according to their AGs in decreasing order. If two or more features have the same evaluation value, the feature with higher priority ranks <sup>fi</sup>rst. The feature with the highest AG is denoted $\mathsf { a s } f _ { 1 }$ and so forth.

2. $m \gets \sqrt { | F | } + 1 . / ^ { * }$ Designate a maximum quantity of features for <sup>j j</sup>selection \*/

$A {  } \ \{ f _ { 1 } , f _ { 2 } , f _ { 3 } , . . . , f _ { m } \} / ^ { * }$ The <sup>fi</sup>rst m features in F are taken as candidates $^ * /$

3. Set $f _ { 1 }$ as the <sup>fi</sup>rst selected feature, i.e., $\alpha {  } f _ { 1 }$

4. $B _ { 1 }  \phi ; B _ { 2 }  \alpha .$

5. Select the second feature $\beta$ from $A { \mathrm { - } } B _ { 2 }$ which has the minimum correlation with α.

$$
B _ {1} \leftarrow B _ {2} \text { and } B _ {2} \leftarrow B _ {2} + \{\beta \}.
$$

6. Select the third feature γ from A-B which minimizes $\textstyle \sum _ { x \in B _ { 2 } } r ( \gamma , x )$ $/ ^ { * }$ <sup>ð Þ</sup>Feature γ has the lowest sum of correlation coef<sup>fi</sup>cients with α and $\beta ^ { * } /$

$$
B _ {1} \leftarrow B _ {2} \text { and } B _ {2} \leftarrow B _ {2} + \{\gamma \}.
$$

7. While $\lambda _ { 1 } ( B _ { 2 } ) / \lambda _ { 1 } ( B _ { 1 } ) { \geq } \psi$ and $| B _ { 2 } | < k$ do

8. Choose next feature f from A-B which minimizes $\textstyle \sum _ { x \in B _ { 2 } } r ( f , x )$

$$
B _ {1} \leftarrow B _ {2}; B _ {2} \leftarrow B _ {2} \{f \}.
$$

9. End While

10. Return $B _ { 2 } .$

![](/api/attachments/7D83F6ME/fulltext/images/0c586e9f37a64c52705926829eb831e9213a84a907812b4ab5e763cde7ac35fb.jpg)  
Fig. 2. Results classi<sup>fi</sup>ed by x and x .

Table 4  
First eigenvalues extracted from multivariate analyses.

<table><tr><td>Selected features</td><td> $\lambda_1$ </td><td>Increment</td></tr><tr><td> $\{x_2, x_4\}$ </td><td>1.18</td><td>-</td></tr><tr><td> $\{x_2, x_4, x_3\}$ </td><td>1.61</td><td>36.44%</td></tr><tr><td> $\{x_2, x_4, x_3, x_1\}$ </td><td>1.80</td><td>11.80%</td></tr></table>

Line 2 designates a maximum quantity of features for selection and this assignment can ensure a suf<sup>fi</sup>cient amount of selected features as $\left| F \right| < 1 0 .$ . Note that this assignment is only a suggestion of the statistical sampling method and users can adjust it according to their requirements. Generally, at least three input features (i.e., $\left| F \right| \geq 3 )$ are employed in a dataset, m is assigned to be at least 3 and this means at least three candidate features will be collected into set A. After the <sup>fi</sup>rst relevant feature is con<sup>fi</sup>rmed as described in line 3, the second and third relevant features are selected by redundancy analyses as outlined in lines 4–6. Then, line 7 is employed to <sup>fi</sup>nd out if there is room for the next selection and detect whether the growth of eigenvalues is signi<sup>fi</sup>cant. Lines 7–9 execute heuristically the selection process until the newly joined feature cannot signi<sup>fi</sup>- cantly contribute to the classi<sup>fi</sup>cation task. The thresholdψcan also be adjusted according to users' requirements. In other words, if fewer features are required to complete the classi<sup>fi</sup>cation task, a higher threshold is set. On the contrary, a lower threshold is employed to collect more features for the classi<sup>fi</sup>cation task. In this paper, a high threshold is suggested to fall within an interval of (1.3, 1.5] while a low threshold should be within (1.0, 1.2).

## 4.4. Feature extraction and inductive learning

Although a succinct set of discriminative features can bene<sup>fi</sup>t multiclass problems, there still leaves room for improvement between the selected features. In fact, the responsibility of every selected feature for classi<sup>fi</sup>cation is not even. Only a few of the selected features have the best relevance to the target feature, so they can contribute the greatest effectiveness to the classi<sup>fi</sup>cation task. The other remaining selected features are employed to assist them in enhancing classi<sup>fi</sup>cation quality. Since all features in a dataset are employed to predict the same objective(s), they are gathered mainly from some common factors such that the dependencies among these features are inevitable. It is hard to escape from the destiny of high correlation for any feature combinations especially when confronting high-dimensional datasets. To tackle this problem, the principal component analysis (PCA) is applied to the selected features. PCA is also referred to as the Karhunen–Loève transform [20]. This transform can reproduce the total system variability and achieves high reduction in dimensionality with usually lower noise than the original patterns. It is particularly helpful when simplifying highly dependent variables into fewer independent components. In practice, the correlation matrix of the data is constructed and the eigenvectors on this matrix are computed. Correlation matrix can overcome the problem attributed to different measure scales. The eigenvectors that correspond to the largest eigenvalues (the principal components) can now be utilized to reconstruct a large fraction of the variance of the original data. The disadvantage of PCA is that the principle components are not easy to interpret. However, a simple classi<sup>fi</sup>er integrating multiple aspects can be achieved by PCA. The mathematical background of PCA is explained as follows.

Table 5  
The abstract of <sup>fi</sup>ve datasets.

<table><tr><td>Datasets</td><td>segment</td><td>satimage</td><td>places</td><td>German credit</td><td>vehicle</td></tr><tr><td># of instances</td><td>2310</td><td>4455</td><td>987</td><td>1000</td><td>846</td></tr><tr><td># of features</td><td>19</td><td>36</td><td>9</td><td>20</td><td>18</td></tr><tr><td># of classes</td><td>7</td><td>6</td><td>4</td><td>4</td><td>4</td></tr></table>

Table 6  
Comparisons of average correlation coef<sup>fi</sup>cients for features selected by IG, GR, and AG.

<table><tr><td colspan="6">Datasets</td></tr><tr><td>Criteria</td><td>segment</td><td>satimage</td><td>places</td><td>German credit</td><td>vehicle</td></tr><tr><td>IG</td><td>0.57</td><td>0.83</td><td>0.46</td><td>0.20</td><td>0.85</td></tr><tr><td>GR</td><td>0.57</td><td>0.53</td><td>0.46</td><td>0.13</td><td>0.82</td></tr><tr><td>AG</td><td>0.26</td><td>0.48</td><td>0.28</td><td>0.02</td><td>0.74</td></tr></table>

Suppose there are p features (respectively denoted as $f _ { 1 } , f _ { 2 } , \ldots$ , and $f _ { p } )$ in a dataset consisting of n measurements on these $p$ features. In general, much of the total system variability can often be accounted for by a small number of k principal components. In other words, there is as much information in the k components as there is in the orig inal $p$ variables. The k principal components can then replace the initial p variables and the original dataset. Principal components are particular linear combinations of these features. Principal components depend solely on the correlation matrix $\scriptstyle \sum$ of these features. Let the eigenvalues of the correlation matrix $\scriptstyle \sum$ be $\begin{array} { r } { \lambda _ { 1 } \geq \lambda _ { 2 } \geq \cdots \geq \lambda _ { p } \geq 0 . } \end{array}$ . The i-th component is the linear combination which is given by ${ \dot { y } } _ { i } = a _ { i 1 } f _ { 1 } + a _ { i 2 } f _ { 2 } + \dots + a _ { i p } f _ { p }$ , where $[ a _ { i 1 } , a _ { i 2 } , \cdots , a _ { i p } ]$ is the eigenvector corresponding to $\lambda _ { i } , i { = } 1 , 2 , \cdots , p$ . Consequently, the proportion of total variance (i.e., explained variance) due to the i-th principal component is $\sum _ { j = 1 } ^ { \lambda _ { i } } \lambda _ { j }$ . The correlation coef<sup>fi</sup>cient between

the component $y _ { i }$ and the variable $f _ { k }$ is $\rho _ { i , k } = \frac { a _ { i k } \sqrt { \lambda _ { i } } } { \sqrt { \sigma _ { k } ^ { 2 } } }$ ; wherei; $k = 1 , 2 , \cdots p .$ If most (for instance, more than 70%) of the total population variance can be featured to some components, they can then replace the original p variables without much loss of information. In this paper, the <sup>fi</sup>rst and second principal components are considered effective for replacing the original p features. Take again the previous example. The <sup>fi</sup>rst and second principle components extracted from the three selected features are respectively formulated as $y _ { 1 } = 0 . 6 4 x _ { 2 } + 0 . 7 4 x _ { 3 } + 0 . 2 1 x _ { 4 }$ and $y _ { 2 } = 0 . 4 6 x _ { 2 } - 0 . 1 5 x _ { 3 } - 0 . 8 7 x _ { 4 }$ . Combining $y _ { 1 }$ and $y _ { 2 }$ can explain more than 92% of the population variance of the illustrated example.

Finally, the <sup>fi</sup>rst principal component is trained to become more consistent with the target feature. The training method is quite straightforward according to inductive reasoning, revealing the maximal support (or probability) to the conclusion. The <sup>fi</sup>rst principal component after the training process is called the high-level multivariate classi<sup>fi</sup>er (HLMC). If the classi<sup>fi</sup>cation quality achieved by the HLMC need to be further improved, the <sup>fi</sup>rst selected feature will take over the subsequent classi<sup>fi</sup>cation task. In other words, the HLMC takes the responsibility of coarse-granularity classi<sup>fi</sup>cation while the <sup>fi</sup>rst selected feature is responsible for <sup>fi</sup>ne-granularity classi<sup>fi</sup>cation. In order to retain the model's simplicity and emphasize the novelties of our feature selection and feature extraction, we only concentrate on the effectiveness of the HLMC in our experiments.

Table 7  
Comparisons of classi<sup>fi</sup>cation accuracies (%).

<table><tr><td rowspan="2"></td><td colspan="2">segment</td><td colspan="2">satimage</td><td colspan="2">places</td><td colspan="2">German credit</td><td colspan="2">vehicle</td></tr><tr><td>F</td><td> $\hat{F}$ </td><td>F</td><td> $\hat{F}$ </td><td>F</td><td> $\hat{F}$ </td><td>F</td><td> $\hat{F}$ </td><td>F</td><td> $\hat{F}$ </td></tr><tr><td>C4.5</td><td>93.6</td><td>89.8</td><td>85.8</td><td>78.9</td><td>95.3</td><td>84.5</td><td>71.5</td><td>72.3</td><td>65.5</td><td>50.4</td></tr><tr><td>CART</td><td>94.8</td><td>90.2</td><td>86.6</td><td>79.1</td><td>97.3</td><td>85.2</td><td>71.3</td><td>73.2</td><td>66.4</td><td>49.1</td></tr><tr><td>SVM</td><td>94.7</td><td>89.7</td><td>88.1</td><td>78.3</td><td>96.8</td><td>85.4</td><td>73.2</td><td>73.1</td><td>70.0</td><td>50.0</td></tr><tr><td>NaiveBayes</td><td>90.6</td><td>84.5</td><td>81.5</td><td>78.0</td><td>84.8</td><td>85.1</td><td>73.6</td><td>72.1</td><td>57.1</td><td>50.2</td></tr><tr><td>Achievement</td><td></td><td>0.95</td><td></td><td>0.92</td><td></td><td>0.91</td><td></td><td>1.00</td><td></td><td>0.77</td></tr></table>

Comparisons of ROC area and FPR $( 1 0 ^ { - 2 } )$ for four classi<sup>fi</sup>ers.

<table><tr><td colspan="2"></td><td colspan="2">segment</td><td colspan="2">satimage</td><td colspan="2">places</td><td colspan="2">German credit</td><td colspan="2">vehicle</td></tr><tr><td colspan="2"></td><td>F</td><td> $\hat{F}$ </td><td>F</td><td> $\hat{F}$ </td><td>F</td><td> $\hat{F}$ </td><td>F</td><td> $\hat{F}$ </td><td>F</td><td> $\hat{F}$ </td></tr><tr><td>C4.5</td><td>ROC FPR</td><td>98.8 [1.1]</td><td>98.6 [1.7]</td><td>94.1 [3.2]</td><td>94.4 [5.6]</td><td>98.0 [7.5]</td><td>90.3 [20.7]</td><td>86.2 [12.6]</td><td>88.5 [12.3]</td><td>84.8 [11.5]</td><td>77.1 [16.8]</td></tr><tr><td>CART</td><td>ROC FPR</td><td>98.8 [0.9]</td><td>98.4 [1.6]</td><td>95.4 [3.3]</td><td>94.0 [5.4]</td><td>99.5 [4.8]</td><td>84.3 [21.0]</td><td>88.5 [12.7]</td><td>88.4 [11.9]</td><td>85.5 [11.2]</td><td>75.3 [17.2]</td></tr><tr><td>SVM</td><td>ROC FPR</td><td>98.4 [0.9]</td><td>97.1 [1.7]</td><td>96.7 [2.6]</td><td>92.3 [5.3]</td><td>97.1 [3.8]</td><td>85.9 [20.0]</td><td>89.3 [11.4]</td><td>88.4 [12.6]</td><td>85.7 [10.0]</td><td>75.1 [16.9]</td></tr><tr><td>NaiveBayes</td><td>ROC FPR</td><td>98.5 [1.6]</td><td>97.5 [2.6]</td><td>96.8 [3.3]</td><td>94.6 [5.6]</td><td>95.3 [15.8]</td><td>93.3 [21.6]</td><td>92.0 [11]</td><td>89.6 [12.5]</td><td>80.9 [13.9]</td><td>74.6 [16.2]</td></tr></table>

## 5. Experimental results and analysis

## 5.1. Dataset acquisition and feature evaluation

The <sup>fi</sup>ve datasets used in this paper are named as segment, satimage, places, German credit, and vehicle. They are downloaded from Statlog [38], UCI [41], and StatLib [10,37] and their application domains cover image, <sup>fi</sup>nance, and traf<sup>fi</sup>c. Table 5 depicts the detailed information of these datasets. The number of features varies from 9 to 36 and the number of target classes varies from 4 to 7. Dataset segment has the highest number of classes and dataset satimage has the largest instance size of all. The raw data type in all features of the <sup>fi</sup>ve datasets is either numeric or nominal. To reduce computational complexity, continuous attributes are converted into discretized or nominal attributes. For comparison studies, <sup>fi</sup>ve datasets of preprocessed instances are saved into <sup>fi</sup>ve individual <sup>fi</sup>les so that they can be reused for building distinct decision models. All decision models were implemented in C and Matlab programming languages executed on a workstation with an Intel Core 2 dual 2.4 GHz processor. To verify our design, four classi<sup>fi</sup>cation methods including C4.5, CART, SVM, and NaiveBayes are selected from the 10 most in<sup>fl</sup>uential algorithms [45] and used in our comparison experiments.

First of all, the dependencies among the features selected by InformationGain (abbreviated as IG), GainRatio (abbreviated as GR), and AG were investigated. According to our selection algorithm, the numbers of candidate features were initialized as fififififi19p +1, fififififi36p +1, fififi9p + 1, fififififi20p + 1, and fififififi18p + 1 for the <sup>fi</sup>ve datasets; i.e., 6, 7, 4, 6, and 6; and the numbers of <sup>fi</sup>nal relevant features selected from the <sup>fi</sup>ve datasets were 5, 4, 3, 2, and 4, respectively. The feature reductions of <sup>fi</sup>ve datasets are 74%, 89%, 67%, 90%, and 78%, respectively. For fair comparisons, criteria IG and GR also selected the same number of features as that determined by our selection algorithm for the <sup>fi</sup>ve datasets (i.e., 5, 4, 3, 2, and 4, respectively). Table 6 shows the average correlation coef<sup>fi</sup>cients for every pair of selected features. For segment and places, IG and GR voted the same sets of relevant features and their average correlations stay at a medium level while AG <sup>fi</sup>ltered the subsets with low average correlations. This tells that lowly correlated features relevant to the target feature could be achieved in segment and places. For satimage, AG selected a set of moderately correlated features, which only show a slight improvement as compared with those selected by GR. As to German credit, low correlations between all original features are common. Hence, a subset of lowly correlated features can be easily achieved no matter which kinds of feature selection are used. This also reveals that relevance analysis is more important than redundancy analysis when evaluating the features in German Credit. For vehicle, the features selected by the three criteria all encounter the situation of high redundancy. Our feature extraction with PCA is particularly effective in resolving this situation.

Comparisons of training time (in seconds) for four classi<sup>fi</sup>ers.

<table><tr><td></td><td colspan="2">segment</td><td colspan="2">satimage</td><td colspan="2">places</td><td colspan="2">German credit</td><td colspan="2">vehicle</td></tr><tr><td></td><td>F</td><td> $\hat{F}$ </td><td>F</td><td> $\hat{F}$ </td><td>F</td><td> $\hat{F}$ </td><td>F</td><td> $\hat{F}$ </td><td>F</td><td> $\hat{F}$ </td></tr><tr><td>C4.5</td><td>0.06</td><td>0.02</td><td>0.56</td><td>0.05</td><td>0.01</td><td>0.01</td><td>0.08</td><td>-</td><td>0.09</td><td>-</td></tr><tr><td>CART</td><td>6.44</td><td>3.15</td><td>46.19</td><td>5.63</td><td>1.96</td><td>0.48</td><td>4.49</td><td>0.33</td><td>3.47</td><td>0.59</td></tr><tr><td>SVM</td><td>9.62</td><td>7.53</td><td>67.07</td><td>10.67</td><td>2.93</td><td>0.65</td><td>5.11</td><td>1.12</td><td>4.49</td><td>1.08</td></tr><tr><td>NaiveBayes</td><td>0.01</td><td>0.01</td><td>0.02</td><td>-</td><td>0.02</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr></table>

Note: ‘—’ means the time measured is short and less than 0.005 second.

## 5.2. Performance of classifiers

Let us look at the performance of classi<sup>fi</sup>ers built by the features selected in this paper. For convenience of explanation, let F stand for the set of all features in a dataset and <sup>^</sup>F stand for the set of features selected by our selection algorithm. All experimental results in this study were assessed using 10-fold cross-validation. Table 7 shows the accuracy estimation of F and <sup>^</sup>F using C4.5, CART, SVM, and NaiveBayes classi<sup>fi</sup>ers.

As seen in Table 7, both <sup>^</sup>F and F have similar performance for the four classi<sup>fi</sup>ers and <sup>fi</sup>ve datasets. The highest accuracies of different classi<sup>fi</sup>ers are marked by shadows. We averaged all estimations for different classi<sup>fi</sup>ers and calculate the achievement ratio between <sup>^</sup>F and F as depicted in the bottom row of Table 7. The ratio means the achievement of selected features as compared with that gained from all features. For segment, satimage, places, and German credit, <sup>^</sup>F utilizes the subsets with fewer features and achieves almost the same accuracies as F. As to vehicle, its accuracies are not as high as those of other datasets. In addition to the factor of data consistency, the selected features are likely to suffer from high redundancies. As a result, only 77% of classi<sup>fi</sup>cation accuracy is achieved by<sup>^</sup>F .

The discrimination degree of classi<sup>fi</sup>ers is measured by the ROC area. The ROC area is directly represented by plotting the fraction of true positives out of the positives (TPR=true positive rate) vs. the fraction of false positives out of the negatives (FPR=false positive rate). It is a comparison of two operating characteristics (TPR & FPR) as the criterion changes and therefore measures the discrimination capability of the classi<sup>fi</sup>er. The closer the curve is to the upper left-hand corner of the graph, the greater the area and the higher the discrimination capability [16]. The range of the ROC area is 0 to 1.

Table 8 shows the ROC areas and FPRs of F and <sup>^</sup>F obtained using four classi<sup>fi</sup>ers. As to places and vehicle, the ROC areas for <sup>^</sup>F using classi<sup>fi</sup>ers C4.5 and NaiveBayes are slightly lower than those for F. However, there is no signi<sup>fi</sup>cant difference between F and <sup>^</sup>F when segment, satimage, and German credit are used. That is, the discrimination capability and false positive rate of <sup>^</sup>F are as good as those of F. Such results verify that our feature selection method can distinguish a reduced set with necessary and suf<sup>fi</sup>cient features for accomplishing the classi<sup>fi</sup>cation task even when large amounts of features and instances are considered.

Table 9 shows the training time spent for building different classi-<sup>fi</sup>ers. The notation — represents that the time measured is short and less than 0.005 s. Although the classi<sup>fi</sup>cation accuracies, discrimination capability, and false positive rates of <sup>^</sup>F are poorer than those of F for places and vehicle, Table 9 shows that only less than one-fourth of the training time spent for F is required for <sup>^</sup>F . The performance in terms of competitive accuracy and improved ef<sup>fi</sup>ciency is veri<sup>fi</sup>ed by the experimental results. Subsequently in the next subsection, we conduct further experiments to compare the performance achieved by the selected features with that achieved by our multivariate classi<sup>fi</sup>ers.

![](/api/attachments/7D83F6ME/fulltext/images/a8f280ca3a235eddb671adc2bcb027487d118c2bbc74d457a75cf50b247b9849.jpg)  
Fig. 3. Comparisons of classi<sup>fi</sup>cation accuracy for six classi<sup>fi</sup>ers.

## 5.3. Performance of multivariate classifiers built by the selected features

Finally, we present the performance of the multivariate classi<sup>fi</sup>ers trained by our selected features in terms of accuracy, discrimination capability, and training time. For convenience of explanation, the C4.5 decision tree built by the features selected by GainRatio is denoted as GR(C4.5). In addition, the features obtained by our selection algorithm are employed to train the classi<sup>fi</sup>ers including C4.5, CART, SVM, NaiveBayes, and our proposed HLMC. Fig. 3 compares the accuracies obtained by the six classi<sup>fi</sup>ers. The performances of GR(C4.5) are sketched in gray bars while that of the other classi<sup>fi</sup>ers are outlined by line curves. We highlight two aspects according to the outcomes shown in Fig. 3. First, almost all curves are above the top of the gray bars, implying that the features selected by our heuristic algorithm possess better respective class-discriminative power than those selected by the traditional GR criterion. Second, HLMCs have accuracies similar to those of C4.5, CART, SVM, and NaiveBayes. In view of the results obtained, our model with low building complexity achieves performance comparable with that by traditional classi-<sup>fi</sup>ers with high building complexities.

As shown in Fig. 4, the ROC areas measured using the HLMCs are superior to those obtained using the other classi<sup>fi</sup>ers for places and vehicle. As to the other datasets, our HLMCs also exhibit superior discrimination capability compared with the other classi<sup>fi</sup>ers (C4.5 in segment,

![](/api/attachments/7D83F6ME/fulltext/images/f085521b12b0ccb51d33e6cb49d9465934f13db931b43e8516d63f35da36fe4d.jpg)  
Fig. 4. Comparisons of discrimination capability for six classi<sup>fi</sup>ers.

Table 10  
Comparisons of training time (in seconds) for six classi<sup>fi</sup>ers.

<table><tr><td></td><td>segment</td><td>satimage</td><td>places</td><td>German credit</td><td>vehicle</td></tr><tr><td>GR(C4.5)</td><td>0.02</td><td>0.06</td><td>0.08</td><td>-</td><td>0.01</td></tr><tr><td>C4.5</td><td>0.02</td><td>0.05</td><td>0.01</td><td>-</td><td>-</td></tr><tr><td>CART</td><td>3.15</td><td>5.63</td><td>0.48</td><td>0.33</td><td>0.59</td></tr><tr><td>SVM</td><td>7.53</td><td>10.67</td><td>1.23</td><td>1.12</td><td>1.58</td></tr><tr><td>NaiveBayes</td><td>0.01</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>HLMC</td><td>0.01</td><td>0.03</td><td>-</td><td>-</td><td>-</td></tr></table>

Note: ‘—’ means the time measured is short and less than 0.005 second.

NaiveBayes in satimage and German credit). In addition, our HLMCs support higher discrimination capability than GR(C4.5) for all datasets.

Depending on the precise nature of the probability model, NaiveBayes classi<sup>fi</sup>ers can be very ef<sup>fi</sup>ciently trained in a supervised learning setting. This is because NaiveBayes classi<sup>fi</sup>ers do not build decision models after training and they do not generate decision rules at all. Table 10 lists the training time for the six classi<sup>fi</sup>ers. As can be seen, the training time of HLMCs is almost as swift as that of NaiveBayes classi<sup>fi</sup>ers. In addition, the usage time of classi<sup>fi</sup>ers is another concern when choosing classi<sup>fi</sup>cation models. It is worthy to note that simple models facilitate users in predicting the classi<sup>fi</sup>cation results of new instances. Our HLMC founded on a linear combination of a limited number of relevant features is convenient to exercise, making it very attractive to users.

## 6. Conclusions

Multi-class classi<sup>fi</sup>cation problems incur more intricate conditions than binary classi<sup>fi</sup>cation problems. These conditions have pushed classi-<sup>fi</sup>cation problems to an even further boundary where more techniques and technologies are drawn into the data mining community. The method proposed in this paper takes the advantage of principal component analysis to formulate our own strategy in resolving the intricacy. Our learning model advances three new distinguishing characteristics including evaluation method, feature selection, and feature extraction. Hence, the main contributions of this paper are threefold. First, the enhanced relevance analysis is proposed for feature evaluation process. Second, the synergistic classi<sup>fi</sup>cation effect is enhanced by our heuristic feature selection algorithm. The management for selecting proper number of features is also explicitly formulated by means of multivariate analysis. Finally, the generation of coarse-grained classi<sup>fi</sup>er composed of lowly correlated relevant features is successfully realized.

Although our HLMC takes the major responsibility of the classi<sup>fi</sup>cation task, the remaining classi<sup>fi</sup>cation task can be taken over by two possible ways. First, the multivariate classi<sup>fi</sup>er generated from the second principal component can be a choice. However, whether the features employed to handle the remaining classi<sup>fi</sup>cation task are different from those of the HLMC merits further study. The other alternative is using a <sup>fi</sup>ne-grained classi<sup>fi</sup>er, in which case a proper classi<sup>fi</sup> cation model for subsequent classi<sup>fi</sup>cation task should be explored.

## References

[1] O. Aran, L. Akarun, A multi-class classi<sup>fi</sup>cation strategy for Fisher scores: Application to signer independent sign language recognition, Pattern Recognition 43 (5) (2010).1776-1788

[2] L. Becchetti, C. Castillo, D. Donato, R. Baeza-Yates, S. Leonardi, Link analysis for Web spam detection, ACM Transactions on the Web (TWEB) 2 (1) (2008).

[3] T. Bellotti, J. Crook, Support vector machines for credit scoring and discovery of signi<sup>fi</sup>cant features, Expert Systems with Applications 36 (2) (2009) 3302–3308

[4] R.J. Bolton, D.J. Hand, Statistical fraud detection: a review, Statistical Science 3 (2002) 235–255.

[5] C.-W. Bong, M. Rajeswari, Multi-objective nature-inspired clustering and classi<sup>fi</sup>- cation techniques for image segmentation, Applied Soft Computing 11 (4) (2011) 3271-3282

[6] E.J. Calabrese, J.W. Staudenmayer, E.J. Stanek, G.R. Hoffmann, Hormesis outperforms threshold model in National Cancer Institute Antitumor Drug Screening Database, Toxicological Sciences 94 (2) (2006) 368–378.

[7] M.A. Carreira-Perpinan, Continuous latent variable models for dimensionality reduction and sequential data reconstruction. PhD dissertation, Dept. of Compute Science, Univ. of Shef<sup>fi</sup>eld, U.K., 2001.

[8] C. Castillo, D. Donato, A. Gionis, V. Murdock, F. Silvestri, Know your neighbors: web spam detection using the web topology, Proc. 30th Annual Int. ACM Conf. on Research and Development in Information Retrieval, Amsterdam, SIGIR '07, New York, USA, 2007, pp. 423–430.

[9] V. Chandola, A. Banerjee, V. Kumar, Anomaly detection: A survey, ACM Computing Surveys (CSUR) 41 (3) (2009) Article 15.

[10] C.-C. Chang, C.-J. Lin, Software available: a library for support vector machines (LIBSVM), , 2001http://www.csie.ntu.edu.tw/\~cjlin/libsvm.

[11] L. Chen, Q. Ye, Y. Li, Research on GA-based bank customer's credit evaluation, Computer Engineering 32 (3) (2007) 70–72.

[12] D. Delen, G. Walker, A. Kadam, Predicting breast cancer survivability: a comparison of three data mining methods. Artificial Intelligence in Medicine 2 (2005) 113–127

[13] P. Ducange, B. Lazzerini, F. Marcelloni, Multi-objective genetic fuzzy classi<sup>fi</sup>ers for imbalanced and cost-sensitive datasets, Soft Computing 14 (7) (2010) 713–728.

[14] R. El-Yaniv, D. Pechyony, E. Yom-Tov, Better multiclass classi<sup>fi</sup>cation via a marginoptimized single binary problem, Pattern Recognition Letters 29 (14) (2008) 1954–1959.

[15] V. Estivill-Castro, I. Lee, Data mining techniques for autonomous exploration of large volumes of geo-referenced crime data, Proc. 6th Int. Conf. on Geocomputation, Brisbane, Australia, 2001.

[16] T. Fawcett, An introduction to ROC analysis, Pattern Recognition Letters 27 (2006) 861-874.

[17] Y. Feng, Z. Wu, X. Zhou, Z. Zhou, W. Fan, Knowledge discovery in traditional Chinese medicine: State of the art and perspectives, Arti<sup>fi</sup>cial Intelligence in Medicine 38 (3) (2006) 219–236.

[18] A. Fernández, M. Calderón, E. Barrenechea, H. Bustince, F. Herrera, Solving multiclass problems with linguistic fuzzy rule-based classi<sup>fi</sup>cation systems based on pairwise learning and preference relations, Fuzzy Sets and Systems 161 (2010) 3064–3080.

[19] I.K. Fodor, A Survey of Dimension Reduction Techniques, Technical Report UCRL-ID-148494, Lawrence Livermore National Laboratory, Center for Applied Scienti<sup>fi</sup>c Computing, 2002.

[20] K. Fukunaga, Introduction to Statistical Pattern Recognition, 2nd ed. Academic Press, San Diego, CA, USA, 1990.

[21] J. Fürnkranz, Round robin classi<sup>fi</sup>cation, Machine Learning Research 2 (2002) 721–747

[22] M. Galar, A. Fernández, E. Barrenechea, H. Bustince, F. Herrera, An overview of ensemble methods for binary classi<sup>fi</sup>ers in multi-class problems: Experimental study on one-vs-one and one-vs-all schemes, Pattern Recognition 44 (8) (2011) 1761–1776.

[23] X. Hao, W. Deng-sheng, X. Yang-qun, Study on enterprise credit evaluation based on PCA/FCM, Technology Economics 3 (2007).

[24] P.-W. Huang, C.-H. Lee, Automatic classi<sup>fi</sup>cation for pathological prostate images based on fractal analysis, IEEE Transactions on Medical Imaging 28 (7) (2009) 1037–1050.

[25] A.K. Jain, R.P.W. Duin, J. Mao, Statistical Pattern Recognition: A Review, IEEE Transactions on Pattern Analysis and Machine Intelligence 22 (1) (2000) 4–37.

[26] M.M. Kabira, M.M. Islamb, K. Murase, A new wrapper feature selection approach using neural network, Neurocomputing 73 (2010) 3273–3283.

[27] A. Khashman, Neural networks for credit risk evaluation: Investigation of different neural models and learning schemes, Expert Systems with Applications 37 (9) (2010) 6233-6239

[28] H.-W. Kim, H.C. Chan, S. Gupta, Value-based adoption of mobile Internet: An empirical investigation, Decision Support Systems 43 (1) (2007) 111–126.

[29] T. Li, C. Zhang, M. Ogihara, A comparative study of feature selection and multiclass classi<sup>fi</sup>cation methods for tissue classi<sup>fi</sup>cation based on gene expression, Bioinformatics 20 (15) (2004) 2429–2437.

[30] S. Maldonado, R. Weber, J. Basak, Simultaneous feature selection and classi<sup>fi</sup>cation using kernel-penalized support vector machines, Information Sciences 18 (2011) 115-128.

[31] C. Orsenigo, C. Vercellis, Multivariate classi<sup>fi</sup>cation trees based on minimum features discrete support vector machines, IMA Journal of Management Mathematics 14 (3) (2003) 221–234.

[32] J.S. Pedersen, G. Bejerano, A. Siepel, K. Rosenbloom, K. Lindblad-Toh, E.S. Lander, J. Kent, W. Miller, D. Haussler, Identi<sup>fi</sup>cation and classi<sup>fi</sup>cation of conserved RNA secondary structures in the human genome, PLoS Computational Biology 2 (4) (2006) e33.

[33] H. Peng, F. Long, C. Ding, Feature selection based on mutual information: Criteria of max-dependency, max-relevance, and min-redundancy, IEEE Transactions on Pattern Analysis and Machine Intelligence 27 (8) (August 2005) 1226–1238.

[34] X. Qi, B.D. Davison, Web page classi<sup>fi</sup>cation: Features and algorithms, ACM Computing Surveys (CSUR) 41 (2) (2009) 1–31.

[35] L.E. Raileanu, K. Stoffel, Theoretical comparison between the Gini index and information gain criteria, Annals of Mathematics and Arti<sup>fi</sup>cial Intelligence 41 (1) (2004) 77–93.

[36] A. Siepel, D. Haussler, Computational identi<sup>fi</sup>cation of evolutionary conserved exons, Proc. of the Eighth Annual Int. Conf. on Computational Biology (RECOMB-04), ACM Press, New York, 2004.

[37] StatLib Datasets Archive, http://lib.stat.cmu.edu/datasets.

[38] Statlog Datasets, http://www.is.umk.pl/project/datasets-stat.htm

[39] C.-F. Tsai, Feature selection in bankruptcy prediction, Knowledge -Based System 22 (2009) 120–127.

[40] C.-F. Tsai, Y.-C. Hsiao, Combining multiple feature selection methods for stock prediction: Union, intersection, and multi-intersection approaches, Decision Support Systems 50 (2010) 258–269.

[41] UCI Learning Repository, http://www.ics.uci.edu/mlearn/MLSummary.html2005.

[42] C.-M. Wang, Y.-F. Huang, Evolutionary-based feature selection approaches with new criteria for data mining: A case study of credit approval data, Expert Systems with Applications 36 (2009) 5900–5908.

[43] A. Webb, Statistical Pattern Recognition, Arnold, 1999.

[44] H. Wei, S. Billings, Feature subset selection and ranking for data dimensionality reduction, IEEE Transactions on Pattern Analysis and Machine Intelligence 1 (2007) 162–166.

[45] X. Wu, V. Kumar, J.R. Quinlan, J. Ghosh, Q. Yang, H. Motoda, G.J. McLachlan, A. Ng, B. Liu, P.S. Yu, et al., Top 10 algorithms in data mining, Knowledge and Information Systems 14 (1) (2008) 1–37.

[46] L. Yu, W. Yue, S. Wang, K.K. Lai, Support vector machine-based multiagent ensemble learning for credit risk evaluation, Expert Systems with Applications 37 (2) (2010) 1351–1360.

[47] H. Zhao, A multi-class genetic programming approach to developing Pareto optimal decision trees, Decision Support Systems 43 (3) (2007) 809–826.

## Hung-Yi Lin

886-952-263835linhy@nutc.edu.tw

## Education

• Bachelor of Science in Applied Mathematics from National ChungHsing University in 1992.

• Master degree in Information Management from National Taiwan University of Science and Technology in 1994.

• Ph.D. in Applied Mathematics from National ChungHsing University in 2005 winter.

## Occupation

• System research and software development engineer in Institute for Information Industry in 1994.

• Assistant professor in the Department of Finance in ChaoYang University of Technology, Taiwan (ROC).

• Associate professor in the Department of Distribution Management in National Taichung University of Science and Technology, Taiwan (ROC).

## Achievements and awards

• Journal paper review

▪ Knowledge-Based Systems

▪ Journal of Information Processing Systems

▪ Knowledge and Information Systems

▪ Journal of Quality

▪ International Journal of Knowledge-Based Organizations

▪ International Journal of Innovative Computing, Information and Control

• The champion of simulation investment in the first financial engineering competition (sponsored by FeAT 2004).

• Best Paper Award of The 2011 TOPCO paper competition, Certificate of Merit for Association Taiwan Electronic Commerce

• Best Paper Award of The 2011 IAENG, Certificate of Merit for The 2011 IAENG International Conference on Data Mining and Applications

## Research interests

• Spatial and temporal databases

• Mobile databases

• Multimedia databases

• Data mining

• Machine learning

• Knowledge discovery in databases
