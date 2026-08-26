---
otero_id: 15822
otero_key: "C5PFEEGZ"
title: "A synthetic informative minority over-sampling (SIMO) algorithm leveraging support vector machine to enhance learning from imbalanced datasets"
authors: "Saeed Piri; Dursun Delen; Tieming Liu"
year: "2018"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2017.11.006"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

A synthetic informative minority over-sampling (SIMO) algorithm leveraging support vector machine to enhance learning from imbalanced datasets

![](/api/attachments/C5PFEEGZ/fulltext/images/33013ef50241a6e43ed69715345f77c5168caee6f94247261e612d76b732e8f2.jpg)

Saeed Piri, Dursun Delen, Tieming Liu

<table><tr><td>PII:</td><td>S0167-9236(17)30218-X</td></tr><tr><td>DOI:</td><td>doi:10.1016/j.dss.2017.11.006</td></tr><tr><td>Reference:</td><td>DECSUP 12900</td></tr><tr><td>To appear in:</td><td>Decision Support Systems</td></tr><tr><td>Received date:</td><td>23 June 2017</td></tr><tr><td>Revised date:</td><td>17 October 2017</td></tr><tr><td>Accepted date:</td><td>25 November 2017</td></tr></table>

Please cite this article as: Saeed Piri, Dursun Delen, Tieming Liu , A synthetic informative minority over-sampling (SIMO) algorithm leveraging support vector machine to enhance learning from imbalanced datasets. The address for the corresponding author was captured as affiliation for all authors. Please check if appropriate. Decsup(2017), doi:10.1016/ j.dss.2017.11.006

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# A Synthetic Informative Minority Over-Sampling (SIMO) Algorithm Leveraging Support Vector Machine to Enhance Learning from Imbalanced Datasets

Saeed Piri<sup>a</sup>, Dursun Delen<sup>b#</sup>, and Tieming Liu<sup>c</sup>

<sup>a</sup> Department of Management Science and Information Systems, Spears School of Business, Oklahoma State University, Stillwater, OK, 74078, U.S.A. Email: saeed.piri@okstate.edu

<sup>b</sup> Department of Management Science and Information Systems, Center for Health Systems Innovation, Spears School of Business, Oklahoma State University, Tulsa, OK, 74106, U.S.A. Email: dursun.delen@okstate.edu

<sup>c</sup> Department of Industrial Engineering and Management, College of Engineering, Architecture and Technology, Oklahoma State University, Stillwater, OK, 74078, U.S.A. Email: tieming.liu@okstate.edu

## <sup>#</sup> Corresponding author:

Spears and Patterson Endowed Chairs in Business Analytics

Director of Research—Center for Health Systems Innovation

# A Synthetic Informative Minority Over-Sampling (SIMO) Algorithm Leveraging Support Vector Machine to Enhance Learning from Imbalanced Datasets

## Abstract

Developing decision support systems (DSS) based on imbalanced datasets is one the critical challenges in data mining and decision-analytics. A dataset is called imbalanced when the number of examples from one class outnumbers the number of the instances from another class. Learning from imbalanced datasets is one of the major challenges in machine learning. While a standard classifier could have a very good performance on a balanced dataset, when applied to an imbalanced dataset, its performance deteriorates dramatically. This poor performance is rather troublesome, especially in detecting the minority class, which usually is the class of interest. Therefore, the poor performance of machine learning techniques, which are used to develop DSS, negatively affect the practicality of DSS in real word problems. Oversampling the minority class is one of the most promising remedies for imbalanced data learning. In this study, we propose a new synthetic informative minority over-sampling (SIMO) algorithm leveraging support vector machine (SVM). In this algorithm, first SVM is applied to the original imbalanced dataset, then, minority examples close to the SVM decision boundary, as the informative minority examples are over-sampled. We also developed another version of SIMO and call it weighted SIMO (W-SIMO). W-SIMO is different from SIMO in the degree of over-sampling the informative minority examples. In W-SIMO, incorrectly classified informative minority examples are over-sampled with a higher degree compared to the correctly classified informative minority examples. In this way, there is more focus on incorrectly classified minority examples. The over-sampled dataset can be used to train any classifier. We applied these algorithms to the 15 publicly available benchmark imbalanced datasets and assessed their performance in comparison with existing approaches in the area of imbalanced data learning. The results showed that our algorithms had the best performance in all datasets compared to other approaches.

Keywords: Predictive modeling; machine learning; imbalanced data; over-sampling; support vector machines; performance metrics

# ACCEPTED MANUSCRIPT

## 1. Introduction

Developing decision support systems (DSS) based on imbalanced datasets is one the critical challenges in data mining and decision making. A dataset is called imbalanced when the distribution of different classes in the data is not similar. For instance, in the case of two-class data, there are many more examples of one class (negative examples) compared to the other class (positive examples). Let us call the class with fewer examples the minority class, and the class with more examples the majority class. Decision-making based on imbalanced datasets is very common in real-life problems, especially in decision support systems that are based on classification. For example, if a sample of people were tested for a specific disease, only a small portion of them would actually have the disease. Therefore, in building of the most of clinical decision support systems we deal with imbalanced data sets. For instance, Piri, et al. [1] developed a clinical DSS for diabetic retinopathy. In their data, only 5% of the patients had retinopathy and 95% of them did not have the disease. There are several other clinical DSS that are developed based on imbalanced datasets, predicting heart transplantation outcomes through data analytics Dag, et al. [2] predicted heart transplantation outcomes by analyzing imbalanced data. Finance is another area that extensively deals with decision-making based on analyzing imbalanced datasets. For instance, in credit card fraud detection, only a few numbers of transactions in the whole sample of transactions are actually fraud [3]. Another example is predicting bankruptcy in medium-sized enterprises by learning from imbalanced data [4]. In imbalanced datasets, the prediction accuracy, especially for the minority class, is a critical challenge. When the standard machine learning techniques are applied to the imbalanced data, the result will be in favor of the majority class, i.e. a big portion of the minority class examples will be classified as the majority. In real world applications, the detection accuracy of the minority class is critically important because the minority class usually is the class of interest. Thus, misclassifying the minority class has much higher cost compared to misclassifying a majority class example. To make it clearer, compare the cost of misclassifying a cancerous patient as non-cancerous to the cost of misclassifying a non-cancerous as cancerous; in the former case, the misclassification may lead to death of a person but in the latter case, there will be some more tests and screenings. All of the aforementioned examples, indicate the extremely importance role of imbalanced data learning in the performance of the decision support systems built on imbalanced datasets.

There are various approaches to improve the performance of predictive modeling in imbalanced datasets. Sampling methods are those that either increase the number of minority examples by generating synthetic examples, or decrease the number of majority examples by removing some of them. Another popular approach is assigning different misclassification costs for various classes; this approach is called cost-sensitive. There are other methods and algorithms that we cover in the literature review section. In this research, we propose a novel synthetic informative minority over-sampling (SIMO) algorithm, which employs support vector machine (SVM) to enhance learning from imbalanced datasets. Here we discuss why we chose over-sampling versus other methods to handle the imbalanced data learning challenge, and why we chose SVM. First, to apply a sampling method, no extra information is required other than the dataset itself [5]. However, in cost-sensitive methods, the information about the misclassification cost for each class is required, while this kind of information is unknown. The only known fact is that the misclassification cost for minority class is higher than misclassification cost for majority class ([6],[7]). Second, we apply over-sampling versus under-sampling. The major limitation in under-sampling is the possibility of losing important information by removing some parts of the data, while there is not such a problem in over-sampling.

There are three main reasons for choosing SVM as the classifier. First, this method has a very strong and at the same time simple theoretical background which makes it easy to explain intuitively [8]. Second, this method develops a hyperplane (decision boundary) that separates the data space for classifying the data points (examples). It is known that the data points near the decision boundary are more important and difficult to classify [9]. Therefore, identifying the near boundary data samples is rather easy in SVM. Finally, SVM has been shown to have a very good performance and high generalization power in many practical applications compared to other machine learning techniques ([8], [10]).

The proposed algorithm, SIMO, generates synthetic minority data points that are located near the boundary between two classes in the data space. After applying SIMO in an imbalanced dataset, the number of minority class data points will be increased and the dataset will be more balanced. In this research, we developed another version of SIMO, which we call weighted SIMO (W-SIMO). In W-SIMO, after identifying the informative minority examples, they are grouped into two categories. First, those that are correctly classified by the SVM, and second, those that are incorrectly classified by the SVM. At the over-sampling stage, more data points are generated in the space of the minority data examples that are misclassified. The over-sampled dataset through SIMO and W-SIMO can be used by other machine learning techniques and it is not limited only to the SVM. We expected that our proposed algorithms would have a competitive performance in imbalanced data learning compared to other existing methods. To test this hypothesis, we performed extensive numerical experiments and provide the results of this analysis.

The remainder of this manuscript is organized as follows. In Section 2, existing methods and algorithms in the area of imbalanced data learning are reviewed. In Section 3, we provide the SVM formulation and discuss its deficiency in imbalanced datasets. In Section 4, SIMO and W-SIMO algorithms and their characteristics are described. Section 5 provides numerical analysis to assess the performance of the SIMO and W-SIMO compared to other existing algorithms. Finally, Section 6 contains the conclusion and discussion about this study.

## 2. Literature Review

Studying the imbalanced data classification has received a considerable amount of attention in recent years. He and Garcia [7] classified the different approaches of analyzing imbalanced data into four main classes,

\- Sampling methods

\- Cost-sensitive methods

Kernel-based methods and active learning methods

\- Other methods such as, one-class learning, novelty detection, etc.

In this section, we briefly review the research studies that are the most related to our study.

## 2.1 Sampling methods

The aim of the sampling methods is to reach some degree of balanced distribution in the dataset. These methods can be categorized into two major streams, those that under-sample the majority class and those that over-sample the minority class. In under-sampling methods, some parts of the majority examples are removed. As a result, the distribution of the classes will be more balanced. The simplest method in this category is the random under-sampling. There is not any specific mechanism for under-sampling in this approach and it functions merely randomly. Other under-sampling approaches such as BalancedCascade and EasyEnsemble presented by Liu, et al. [11] are called informed under-sampling. In EasyEnsemble, several samples of the majority class data are taken and combined with minority class data. Multiple models are built based on these datasets, and at the end an ensemble model makes the final decision. The main criticism of the under-sampling methods is that by removing some parts of the data, potential important information in the data can be lost.

Over-sampling on the other hand, is to re-sample or generate extra examples of the minority class. The most basic over-sampling method is random over-sampling in which minority examples in the data are randomly duplicated. The main downside of random over-sampling is over-fitting. Another major approach in over-sampling is synthetic data generation. SMOTE (Synthetic Minority Over-Sampling Technique) is one of the most well-known methods in synthetic data generation. In this method, synthetic data points are generated on the line connecting the minority samples to their k nearest minority class neighbors [12]. The major drawback in SMOTE is that it may lead to over-generalization because it blindly generates synthetic data points without considering the majority data points that might be located near the minority examples. This over-generalization might lead to overlapping between classes [13].

There are extensions to the SMOTE that tried to improve the performance of this technique. Han, et al. [14] proposed a synthetic over-sampling method named Borderline-SMOTE. In this method, only a

# ACCEPTED MANUSCRIPT

subset of minority data points is over-sampled by SMOTE technique. Those minority data points are located near the border of two classes. Borderline minority data points are identified as minority examples that most of their nearest neighbors belong to the majority class. One limitation for Borderline-SMOTE is its mechanism for identifying the borderline and noise data points. In this method, a minority data is identified as noise, only if all of its neighbors are majority. However, in cases that there only two minority data points surrounded by majority examples, Borderline-SMOTE consider them borderline, while they are obviously noises. On the other hand, Bunkhumpornpat, et al. [15] introduced a method named Safe-Level SMOTE. This method calculates a parameter called safe-level. The greater that a safe-level is for a minority example shows that example is farther away from the borderline. After identifying the minority examples in safe regions, those data points will be over-sampled using SMOTE. Safe-level SMOTE focuses on the minority data points that are in the safe regions of the data space, while those are the data points that are easy to classify, and the main challenge is classifying the minority examples near the classes boundary. Cieslak, et al. [16] introduced the cluster SMOTE method. This method first clusters the minority examples, and then over-samples data points within each cluster by applying SMOTE.

Barua, et al. [17] proposed a majority weighted minority oversampling technique that first identifies hard to learn minority examples by considering their distance from the majority neighbors, and then it over-samples those examples using a clustering approach. Sáez, et al. [18] suggested a framework called SMOTE-IPF. In their framework, the data is first over-sampled by SMOTE method and then noisy data points are filtered by applying iterative-partitioning filter (IPF) method. Through a series of numerical experiments, they showed the efficiency of their framework. There are other studies in the area of synthetic data generation ([14], [19], and [20]). Generally speaking, synthetic oversampling significantly improves the classification accuracy, especially for the minority class [21]. Another advantage is that by generating the synthetic minority data (not simply replicating existing minority data), the minority region is generalized and overfitting can be avoided [22]. For a more comprehensive review of the sampling methods, we refer readers to He and Garcia [7].

## 2.2 Cost-sensitive Methods

Unlike sampling methods that alter the distribution of the data through either generating synthetic minority data points or removing some portion of majority data points, the idea of cost-sensitive methods is based on the different misclassification costs for different classes in the dataset. Usually the cost of misclassifying the minority class is much higher than the majority class misclassification [23]. To perform cost-sensitive methods, a matrix, called cost matrix is required. This matrix shows the misclassification cost for different classes in the dataset [24]. The main concern about cost-sensitive methods is that in most of the situations the exact misclassification cost related to various classes is unknown [6].

There are three major categories in cost sensitive approaches [7]. The first category includes techniques that assign various weights to the examples in the dataspace. Methods in this category are motivated by the AdaBoost algorithm [25]. AdaBoost is a meta-algorithm that begins with the original dataset and trains a model on this dataset. Incorrectly classified examples are identified, and in the next iteration more weight (higher error cost) will be assigned to them. In this way, more focus will be on the examples that are misclassified. This process repeats and the classifier performance improves. The second group encompasses approaches are those that use ensemble schemes integrated with cost-sensitive approaches. Many of the research studies in these two categories have combined various weighting and adaptive boosting techniques. For instance Sun, et al. [26] and Fan, et al. [27] proposed algorithms for updating the weights in AdaBoost in imbalanced data learning. Lee, et al. [28] used SVM to adjust the weights of the examples in AdaBoost to learn from imbalanced data. In the third category, cost-sensitive methods incorporate the misclassification costs directly into the classifiers. Cost-sensitive decision tree [29], cost-sensitive neural networks [30], and cost-sensitive SVM [31] are in this category.

## 2.3 Kernel-based Methods

Kernel-based methods are mostly integrated with SVM. Many researchers have studied imbalanced data learning through support vector machine. Wu and Chang [32] developed a boundary-alignment algorithm, which makes a change in the kernel function to move the boundary toward the negative instances. Akbani, et al. [33] proposed an algorithm by integrating the different error cost method [31] and the SMOTE over-sampling method, however they performed the SMOTE over-sampling independent from the SVM model. Wang and Japkowicz [34] applied boosting and asymmetric error cost for minority and majority classes. Mathew, et al. [35] proposed a kernel-based SMOTE for SVM. In their approach, the over-sampling through the SMOTE technique happens in kernel feature space. Yu, et al. [10] developed the SVM-OTHR algorithm. In this algorithm, they adjusted the decision threshold by moving the decision hyperplane toward the majority class data. Lee, et al. [28] proposed an improved weighted support vector machine for imbalanced data learning. Jian, et al. [36] developed a sampling framework by using support vector machine. They over-sampled minority data points and under-sampled majority data point, and classified the examples by an ensemble of support vector machines. To enhance the imbalanced data learning performance, Shao, et al. [37] proposed a weighted Lagrangian twin support vector machine. They introduced a graph based under-sampling in their algorithm. However, their approach is very sensitive to its parameters and it takes a long time to find the reasonable values for the parameters, therefore it is not very easy and practical to use their approach in real word problems.

# ACCEPTED MANUSCRIPT

Tang and Zhang [38] proposed a granular SVM with repetitive under-sampling. They utilized SVM for under-sampling in a way that they repeatedly developed SVM models and each time discarded the negative (majority class) support vectors from the data. Even though they performed the undersampling integrated with the SVM, the problem of losing potential important information by undersampling still exists. As Akbani, et al. [33] showed in their paper, under-sampling the majority class may decrease the total error, but it usually deteriorates the performance of the SVM on the test data, because it fails to approximate the orientation of the ideal hyperplane. Batuwita and Palade [39] suggested an oversampling method in which they selected the majority examples near the boundary as the informative negative data points, and then they randomly over-sampled the minority examples to have relatively balanced data. This work can be critiqued in two ways. First, they focused on the informative majority examples, while the primary interest in imbalanced datasets is on the minority examples, therefore the focus on the informative majority examples may lead to even more bias toward the majority class. Second, they simply applied random over-sampling that is not as powerful as synthetic data generation methods and may lead to over-fitting. The two former studies did not compare their model’s performance with other existing methods; therefore, it is not easy to comment on generalizability and efficiency of their model. [40] proposed a preprocessing approach using SVM for imbalanced data. In their approach, they first trained SVM on the original data, and then replaced the actual target variable value by the SVM predicted value. They claimed that SVM will classify a portion of the majority examples as minority, and therefore the processed data will have a more balanced distribution. Their claim is questionable, because in imbalanced data learning most of the time there is poor accuracy on minority class and good accuracy on majority. This means that most of the minority examples are misclassified as majority not the other way around. They tested their approach only on one dataset; therefore, their results could be because of the characteristics of that special dataset.

In this research, we propose a novel over-sampling algorithm leveraging SVM. We can numerate several advantages for our proposed algorithm. First, it leverages a powerful classifier, i.e. SVM, and therefore better results are expected compared to other pre-processing approaches. Second, we conduct over-sampling rather than under-sampling that may lead to information loss due to discarding a fraction of data. Finally, we perform the over-sampling only on the informative minority examples. In this way, we generate the least amount of synthetic data points; therefore, the distribution of the training data will not change dramatically. In addition, because the amount of synthetic generated data is much less compared to other existing methods such as SMOTE, Borderline SMOTE, Safe-Level SMOTE, and Cluster-SMOTE, the computational cost of training machine learning techniques will be lower.

## 3. Support vector machines (SVM)

# ACCEPTED MANUSCRIPT

SVM is a machine learning technique that can be applied to both regression and pattern recognition (classification) problems. For the classification, SVM develops a decision boundary that separates two classes in the data space. To build this decision boundary, SVM maximizes the separating margin between two classes in the data space while it minimizes the classification error. Figure 1 shows a linear SVM decision boundary. Dots and stars denote the two classes in the data. The data points that lie on the margins at both sides of the decision boundary are called support vectors. These support vectors are shown in Figure 1 with a circle around them. ?? is the normal to the decision boundary and $b / | w |$ is the perpendicular distance of the decision boundary from the origin [41]. When two classes are not completely separable, some of the examples will be misclassified. In Figure 1, one star data point has misclassified as a dot, the distance of this point from the decision boundary $\mathrm { i s } - \varepsilon / | w |$

![](/api/attachments/C5PFEEGZ/fulltext/images/134e239bab800a73e965152946104c76a7ec9c2627c8b1ab7ee0fa48e2542f73.jpg)  
Figure 1. Linear SVM hyperplane

SVM can be applied to both linear and non-linear separable problems. When two classes are not linearly separable, kernel trick can be employed and the data is mapped to a feature space (using a mapping function $\phi ( . ) )$ ), which is in a higher dimension [42]. In the feature space, two classes will be linearly separable and the problem will be handled similar to the linearly separable case.

The decision boundary of the SVM has the following formulation (Formulation 1),

$$
w ^ {T} \phi (x) + b\tag{1}
$$

Where ?? is obtain from Formulation 2,

$$
w = \sum_ {i = 1} ^ {N} \alpha_ {i} y _ {i} \phi (x _ {i})\tag{2}
$$

$$
y = s g n \{w ^ {T} \phi (x) + b \}
$$

To determine the class of a new sample, ??, a sign function (sgn(.)) is used, it is obtained using,

(3)

# ACCEPTED MANUSCRIPT

## 3.1 SVM on Imbalanced Datasets

Although SVM has a very good performance on balanced datasets, when applied to imbalanced datasets, its performance deteriorates dramatically, especially on the minority class. The SVM decision boundary in an imbalanced dataset is closer toward the minority class region compared to the ideal classification decision boundary. As a result, a considerable number of minority class examples will be misclassified as the majority. Wu and Chang [43] mentioned two reasons for this decision boundary skewness. The first reason is in regard to the imbalanced training data ratio, because the negative data points outnumber the positive examples, these positive examples are further away from the “ideal” decision boundary compared to the majority examples. Second, the imbalanced supports vector ratio, because the number of the negative (majority class) support vectors is much more than the positive (minority class) support vectors, a positive test data point might have more negative support vector neighbors, and as a result will be misclassified as negative (majority) class. Akbani, et al. [33] pointed out another reason for the skewed decision boundary. The objective of the SVM model is to maximize the margin between two classes as well as minimizing the classification errors and there is a tradeoff between these two. When the number of negative examples is much more than the positive ones, the cumulative misclassification cost of the positive points is relatively small, therefore SVM tends to maximize the margin to its highest possible degree by classifying most (sometimes all) of the examples as negative. Thus, the decision boundary will be shifted toward the minority class region. In the next section, we describe our proposed remedy to this problem.

## 4. SIMO and W-SIMO Algorithms

In this study, we developed a novel synthetic informative minority over-sampling (SIMO) algorithm integrated with SVM. As we mentioned earlier, when SVM is applied to an imbalanced dataset, the decision boundary will be closer to the minority class space in favor of the majority class examples. Therefore, a considerable portion of minority examples will be misclassified. In SIMO, we generate synthetic data points that belong to the minority class. In this way, the distribution of the dataset will be more balanced and a better performance will be expected from machine learning techniques. Research has shown the data points that are close to the boundary of classes are the important data points in forming the classifiers [7]. Therefore, in SIMO we focus on the minority data points near the boundary of two classes.

The first step in performing SIMO (Algorithm 1 and Flowchart 1) is to partition the dataset into training and test datasets. This partitioning is conducted in a way that the imbalance ratio in training and test datasets will be the same as the imbalance ratio in the original dataset. The reason for partitioning the data is to avoid biases and to assess the SIMO performance fairly on imbalanced data with the original imbalance ratio (test dataset). Next, we calculate the imbalanced gap in the training dataset. Imbalanced

# ACCEPTED MANUSCRIPT

gap is the difference between the number of majority examples and minority examples in the training dataset. Imbalanced gap is the upper bound for generating the synthetic data points in our algorithm. In the next stage, we develop a SVM on the original imbalanced training dataset and evaluate this initial model by computing the G mean. G mean is an evaluation metric that is widely used in imbalanced data learning. More details about G mean and its computation is provided in Section 5.1. As it can be seen in Figure 2a, the initial SVM decision boundary is close to the minority class data space in favor of majority class data space and the ideal decision boundary should be located farther away from the minority dataspace.

The next step in SIMO is to calculate the Euclidean distance of the minority data points from the SVM decision boundary. As we mentioned earlier, data points close to the boundary of classes are important and informative. In order to select the informative minority data points, we identify those that are close to the SVM decision boundary (have the least Euclidean distance from the decision boundary). Therefore, after calculating the Euclidean distance of the minority data points from the decision boundary, the top ∆% of them that are the closest ones to the decision boundary will be selected as informative minority data points (Figure 2b). Next, we generate synthetic data points in the space of the informative minority examples and append the generated data points to the training dataset. We use SMOTE approach for generating synthetic data points in the minority data space. In this approach, first, the K nearest neighbors of each informative minority data point is identified (the neighbors are also from informative minority examples). Then, a synthetic data point is generated on the line connecting the informative minority data point and its neighbors.

$$
x _ {s y n t h e t i c} = x _ {i} + (\hat {x} _ {i} - x _ {i}) \delta\tag{4}
$$

Where $x _ { i }$ is an informative minority data point, $\widehat { x } _ { i }$ is one of the K nearest neighbors of $x _ { i }$ , and ?? is a random number between 0 and 1.

At this stage, we have a new training dataset that includes more minority examples compared to the previous training dataset (Figure 2c). The number of synthetically generated data points and their indices will be recorded at each iteration. Next, a new SVM will be developed on the updated training dataset. The decision boundary of this new SVM will be shifted toward the majority class data space closer to the ideal decision boundary (Figure 2d). The reason is that by generating synthetic minority examples, the imbalance ratio of the training dataset will be reduced and following that, the imbalance ratio of the support vectors will be alleviated. Therefore, the decision boundary will be shifted toward the majority class dataspace (As we discussed in detail in Section 3.1, the position of the SVM decision boundary only depends on the support vectors). The new SVM will be assessed by computing the G mean, and the G mean will be logged into a vector for further evaluations. Again, in the updated training dataset, the Euclidean distance of the minority data points from the new SVM decision boundary is calculated, informative ones will be selected, and new synthetic minority data points will be generated. Another SVM will be developed on the updated dataset, the SVM will be assessed, and the results will be recorded. These steps will be repeated until the number of synthetically generated examples reaches the imbalanced gap.

![](/api/attachments/C5PFEEGZ/fulltext/images/e7dbee9b5c1990a6dec815d5df28e30f5823735dcc4f9abbade85fef94ec0cbe.jpg)

![](/api/attachments/C5PFEEGZ/fulltext/images/b24432dfb86a919527fa40b2d1bc3eac4b939e3ab4454e965fdcec589b524f8c.jpg)

![](/api/attachments/C5PFEEGZ/fulltext/images/b3f1849d12fb6a1a17522723a22742c8abc4d3ffec58c9b55445803bb018e5c6.jpg)

![](/api/attachments/C5PFEEGZ/fulltext/images/909f9c43f5654a1bfa2d0bd10b3713f60e89e70d00c94a0f1e722c6946ec590c.jpg)  
Figure 2. W-SIMO algorithm mechanism (simplified)

The performance of machine learning techniques highly depends on the structure and complexity of datasets. In our algorithm, in each iteration, we create a new updated dataset by generating more synthetic minority examples. Even though the performance of the SVM improves on the updated training datasets compared to the original imbalanced dataset, the improvement in the performance of the SVM in each iteration compared to the previous iteration is not guaranteed in all datasets. In the other words, the

G mean might not always be increasing through the iterations. Therefore, we keep track of the SVM performances and their corresponding training dataset in each iteration. At the end of the loop, the best performing model is identified by comparing the G mean values, and the training dataset associated with that model/iteration will be selected as the final over-sampled training dataset.

## ACCEPTED MANUSCRIPT

![](/api/attachments/C5PFEEGZ/fulltext/images/d7b61dc8da592324eec5ec353d321bb7503114c3becd442d6762f24a723c17d0.jpg)  
Flowchart 1- SIMO Algorithm

In this study, we proposed another version of SIMO that we call weighted synthetic informative minority over-sampling (W-SIMO). Steps 1 to 7 in W-SIMO (Algorithm 2 and Flowchart 2) are the same as SIMO, i.e. an initial SVM is developed on the original imbalanced training dataset, and top ∆% minority data points close to the SVM decision boundary are identified as informative minority examples.

# ACCEPTED MANUSCRIPT

In the next step, informative minority examples will be classified into two groups: first, those that are correctly classified $( S _ { \mathrm { i n f \_ c } } ^ { + } )$ through SVM, and second, those that are incorrectly classified $( S _ { \mathrm { i n f \underline { { i } } c } } ^ { + } )$ . The data points in $S _ { \mathrm { i n f \underline { { i } } c } } ^ { + }$ will be over-sampled to a higher degree compared to the data points in $S _ { \mathrm { i n f \_ c } } ^ { + }$ . We adopt this idea from AdaBoost, which pays more attention to the incorrectly classified examples [25]. In W-SIMO, by over-sampling the examples in $S _ { \mathrm { i n f \underline { { i } } c } } ^ { + }$ with a higher degree, we consider them even more informative compared to the examples in $S _ { \mathrm { i n f \_ c } } ^ { + }$ It means that more synthetic minority data points will be generated in the space of $S _ { \mathrm { i n f \underline { { i } } c } } ^ { + }$ examples. After over-sampling (synthetically generating) the informative minority data points in $S _ { \mathrm { i n f \underline { { i } } c } } ^ { + }$ and $S _ { \mathrm { i n f \_ c } } ^ { + } ,$ the reminder of the W-SIMO is similar to SIMO. Applying the SIMO and W-SIMO is not limited to the SVM. We use SVM in our algorithms to identify informative data points to over sample them, however the final over-sampled data can be used in any other machine learning technique, such as decision tree, logistic regression, and random forest. The notations of Algorithms 1 and 2 are shown in Table 1.

![](/api/attachments/C5PFEEGZ/fulltext/images/cb2e173e3b282a850ea85dfb640282752ac0cb9b3c2497112ae6acaf43ecb2cd.jpg)  
Flowchart 2- W-SIMO Algorithm

## Table 1. Notations for Algorithms 1 and 2

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
D: Initial imbalanced dataset
 $\widehat{S}$ : Initial imbalanced training dataset
T: Imbalanced test dataset
 $\Delta$ : Top  $\Delta\%$  of minority data points close to decision boundary
p: Oversampling degree for minority informative data points that are correctly classified at each iteration
P: Oversampling degree for minority informative data points that are incorrectly classified at each iteration
S_G_D: Synthetic generated data points count
G_m_L: G mean variation log in each iteration
</div>

## Algorithm 1- SIMO

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Given D,  $\Delta$ , p

1. Partition D into Training  $\hat{S}$ , and Test T datasets

2. Calculate the Imbalanced_Gap in  $\hat{S}$ 

Imbalance_Gap = Majority_Count - Minority_Count

3. Develop the Initial SVM model on  $\hat{S}$ , Initial SVM decision boundary:  $\widehat{D\_B} = \widehat{w}^{T} x + \widehat{b}$ $\{\widehat{w} = \sum_{j=1}^{N_{s}} \widehat{a}_{i} y_{i} \phi(x_{i})\}$ 

4. Compute G mean for Initial SVM on T: Initial_G Mean

5.  $S = \hat{S}$ , SVM = Initial SVM,  $D\_B = D\_B$ ,  $G\_m\_L = Initial\_G$  Mean,  $S\_G\_D = 0$ 

While  $S\_G\_D &lt; Imbalance\_Gap$ 

6. Calculate the Euclidean distance of minority data points form  $D\_B$ $Euc\_D(x^{k+}) = \frac{|\sum_{t=1}^{m} w_{t} x_{t}^{k+} + b|}{\sqrt{\sum_{t=1}^{m} w_{t}^{2}}}$ 

7. Identify informative minority data points:  $S_{inf}^{+}$ 

Top  $\Delta\%$  of minority data points close to  $D\_B$  based on the Euclidean distance

8. Over-sample data points in  $S_{inf}^{+}$  by p%, name the synthetic generated data points  $\hat{S}_{inf}^{+}$ 

9.  $S = S \cup \hat{S}_{inf}^{+}$ 

10. Calculate the number of synthetic generated data points

 $S\_G\_D = S\_count - \hat{S}_{count}$ 

11. Develop a support vector machine on S, SVM

12. Compute G mean for SVM on T

13. Add the G mean to the  $G\_m\_L$ , ( $G\_m\_L = [G\_m\_L; G\ mean]$ )

End

14. Find the maximum G mean and its index in  $G\_m\_L$ 

15. Select the over-sampled training dataset associated with the maximum G mean

16. Train the model of interest on the final over-sampled training dataset

17. Evaluate the model on the test dataset by computing the G mean and AUC
</div>

## Algorithm 2- W-SIMO

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Given D,  $\Delta$ , p, P, (p &lt; P)

1. Partition D into Training  $\hat{S}$ , and Test T datasets

2. Calculate the Imbalanced_Gap in  $\hat{S}$ 

Imbalance_Gap = Majority_Count - Minority_Count

3. Develop the Initial SVM model on  $\hat{S}$ , Initial SVM decision boundary:  $\widehat{D\_B} = \widehat{w}^{T} x + \widehat{b}$ $\{\widehat{w} = \sum_{j=1}^{N_{s}} \widehat{\alpha}_{i} y_{i} \phi(x_{i})\}$ 

4. Compute G mean for Initial SVM on T: Initial_G Mean

5.  $S = \hat{S}$ , SVM = Initial SVM,  $D\_B = D\_B$ ,  $G\_m\_L = Initial\_G$  Mean,  $S\_G\_D = 0$ 

While  $S\_G\_D &lt; Imbalance\_Gap$ 

6. Calculate the Euclidean distance of minority data points form  $D\_B$ $Euc\_D(x^{k+}) = \frac{|\sum_{t=1}^{m} w_{t} x_{t}^{k+} + b|}{\sqrt{\sum_{t=1}^{m} w_{t}^{2}}}$ 

7. Identify informative minority data points:  $S_{inf}^{+}$ 

Top  $\Delta\%$  of minority data points close to  $D\_B$  based on the Euclidean distance

8. Classify informative minority data points using the SVM model, form:

i.  $S_{inf\_c}^{+}$ , informative minority data points that are correctly classified

ii.  $S_{inf\_ic}^{+}$ , informative minority data points that are incorrectly classified

9. Over-sample data points in  $S_{inf\_c}^{+}$  by p%, name the synthetic generated data points  $\hat{S}_{i}^{+}$ 

10. Over-sample data points in  $S_{inf\_ic}^{+}$  by P%, name the synthetic generated data points  $\hat{S}_{ii}^{+}$ 

11.  $S = S \cup \hat{S}_{i}^{+} \cup \hat{S}_{ii}^{+}$ 

12. Calculate the number of synthetic generated data points

 $S\_G\_D = S\_count - \hat{S}_count$ 

13. Develop a support vector machine on S, SVM

14. Compute G mean for SVM on T

15. Add the G mean to the G_m_L, (G_m_L = [G_m_L; G mean])

End

16. Find the maximum G mean and its index in G_m_L

17. Select the over-sampled training dataset associated with the maximum G mean

18. Train the model of interest on the final over-sampled training dataset

19. Evaluate the model on the test dataset by computing the G mean and AUC
</div>

## 5. Numerical Experiments

In this section, we provide the results of our numerical experiments to assess the performance of SIMO and W-SIMO compared to other existing algorithms in imbalanced data learning. First, we describe the evaluation metrics that we used for the assessments. Second, we provide the characteristics of the benchmark imbalanced datasets that we used. Third, we present the results of the numerical experiments. Finally, we provide the results of sensitivity analysis on SIMO parameters.

## 5.1 Evaluation Metrics

In classification or pattern recognition problems confusion matrix plays an important role to assess the predictive models. Figure 3 shows a confusion matrix. As was pointed out earlier, in this study, we consider the minority class as positive, and the majority class as negative class. Accuracy of prediction (Formulation 5) is a common evaluation metric in the balanced datasets; however, it is misleading in assessing the predictive models when applied in imbalanced datasets. Consider an imbalanced dataset with the 10% rate of the positive examples. Because negative examples outnumber the positive ones, datasets other appropriate evaluation metrics such as sensitivity, specificity, G mean, and AUC should be applied [44].

![](/api/attachments/C5PFEEGZ/fulltext/images/d17b638825b0cfb5407a6647b8118584b40c21ec1c4bd9b1241729e9379877b2.jpg)  
Figure 3. Confusion Matrix

$$
A c c u r a c y = \frac {T P + T N}{T P + F N + F P + T N}\tag{5}
$$

Sensitivity or true positive rate (TPR) (it is also called hit rate or recall) is a metric that evaluates the accuracy of predicting the positive examples. On the other hand, specificity or true negative rate (TNR) assesses the accuracy of detecting the negative examples. Formulations 6 and 7 show the calculation of TPR and TNR.

$$
T P R = \frac {T P}{T P + F N}\tag{6}
$$

$$
T N R = \frac {T N}{F P + T N}\tag{7}
$$

TPR and TNR assess the detection accuracy in positive and negative examples separately. Therefore, considering one of them without the other one would not be helpful, therefore, we need a metric such as G mean that incorporates these two metrics at the same time. G mean is the geometric mean of TPR and TNR (Formulation 8). Thus, any model with poor performance on either positive or negative examples will have a low G mean.

# ACCEPTED MANUSCRIPT

$$
G m e a n = \sqrt {T P R \times T N R}\tag{8}
$$

Another assessment tool that is independent of the data distribution is Receiving Operator Characteristic (ROC) chart. ROC shows the tradeoff between TPR and TNR by manipulating the decision cut-off. Decision cut-off is the threshold value for decision making based on the output of a predictive model. When the decision cut-off for a model is 0, all of the examples will be classified as positive, therefore TPR=100% but TNR=0%. On the other hand, if decision cut-off is 1, TPR=0% and TNR=100%. Thus, by changing the decision cut-off from 1 to 0, we can increase the TPR, and TNR will decrease at the same time. In ROC chart, the x-axis shows the 1-TNR and y-axis denotes the TPR, in this way the graph will be increasing. Each point on the ROC chart shows the value of TPR and 1-TNR for a specific decision cut-off value. The closer the ROC chart to the top left point, the better the performance of the classifier. Figure 4 shows a ROC chart, the 45-degree line is the base line model (random), the dash line corresponds to a good performing model, and dotted line is for the perfect model.

An easier way to assess the models and compare different classifiers is to measure the area under the curve (AUC) in ROC chart. AUC takes values between 0 to 100%. AUC for the base line model is 50%, and therefore, classifiers with AUC below 50% are even worse than random guess. The closer the AUC of classifier to 100%, the better the performance of the classifier.

![](/api/attachments/C5PFEEGZ/fulltext/images/41e0ce48f8fed6409625159c46f3fc7f412cdd36a3636dc2dc294737faaeaf04.jpg)  
Figure 4. ROC chart

## 5.2 Datasets

In this study, we used 15 benchmark imbalanced datasets that are publicly available in UCI Machine Learning Repository (http://archive.ics.uci.edu/ml/). We tried to use datasets with various imbalance ratios from 1:1.38 to 1:8.9, i.e. the percentage of minority class in the benchmark datasets ranges from 42% to 10%. To test SIMO and W-SIMO on datasets with more severe imbalance ratio, we randomly removed some portions of minority class examples from Breast Cancer dataset and generated datasets with 1:3.91(BreastC20 dataset) and 1:8.9 (BreastC10) imbalance ratio. Table 2 shows the name and characteristics of these datasets.

Table 2. Benchmark Datasets Characteristics

<table><tr><td>Dataset</td><td>Minority class</td><td>Majority class</td><td># of variables</td><td># of records</td><td>Imbalance ratio</td></tr><tr><td>Liver Disorders (Liver)</td><td>“1”</td><td>“2”</td><td>7</td><td>345</td><td>1 : 1.38</td></tr><tr><td>Ionosphere</td><td>bad</td><td>good</td><td>34</td><td>351</td><td>1 : 1.79</td></tr><tr><td>Pima Indians Diabetes (Pima)</td><td>“1”</td><td>“0”</td><td>8</td><td>768</td><td>1 : 1.87</td></tr><tr><td>Breast Cancer Wisconsin Original (BreastCO)</td><td>malignant</td><td>benign</td><td>10</td><td>699</td><td>1 : 1.91</td></tr><tr><td>Iris</td><td>Versicolor</td><td>All other</td><td>5</td><td>150</td><td>1 : 2</td></tr><tr><td>Yeast</td><td>NUC</td><td>All other</td><td>8</td><td>1484</td><td>1 : 2.6</td></tr><tr><td>Statlog Vehicle Silhouettes (Vehicle)</td><td>van</td><td>All other</td><td>18</td><td>846</td><td>1 : 3.25</td></tr><tr><td>Contraceptive Method Choice (CMC)</td><td>Long-term</td><td>All other</td><td>9</td><td>1473</td><td>1 : 3.42</td></tr><tr><td>Breast Cancer Wisconsin_20% (BreastC20)</td><td>malignant</td><td>benign</td><td>10</td><td>699</td><td>1 : 3.91</td></tr><tr><td>Connectionist Bench_Vowel Recognition (Vowel)</td><td>“0” &amp; “1”</td><td>All other</td><td>11</td><td>990</td><td>1 : 4.5</td></tr><tr><td>Ecoli</td><td>pp</td><td>All other</td><td>8</td><td>336</td><td>1 : 5.46</td></tr><tr><td>Libras Movement_12 (Libras12)</td><td>“1” &amp; “2”</td><td>All other</td><td>91</td><td>360</td><td>1 : 5.88</td></tr><tr><td>Libras Movement_34 (Libras34)</td><td>“3” &amp; “4”</td><td>All other</td><td>91</td><td>360</td><td>1 : 6.34</td></tr><tr><td>Glass Identification (Glass)</td><td>“7”</td><td>All other</td><td>9</td><td>214</td><td>1 : 6.38</td></tr><tr><td>Breast Cancer Wisconsin_10% (BreastC10)</td><td>malignant</td><td>benign</td><td>10</td><td>699</td><td>1 : 8.9</td></tr></table>

## 5.3 Results

In this study, we compared the performance of our algorithms, SIMO and W-SIMO to seven other existing approaches in imbalanced data learning. We also provided the modeling results on the original imbalanced data for reference. For all of the algorithms, we used the parameters suggested by their developers. We assessed SIMO and W-SIMO in comparison with these algorithms: under-sampling, SMOTE, borderline SMOTE, safe-level SMOTE, cluster SMOTE, SMOTE-IPF, and cost sensitive SVM. In cost sensitive SVM, we assigned the error cost of the two classes based on the imbalance ratio in the dataset. For instance, if the imbalance ratio in a data is 1:4, the error cost for the minority class is 4 times greater that the error cost for majority class.

To avoid over-fitting and fairly assess the generalizability and performance of various approaches, we applied 4-fold cross validation in our numerical experiments [45]. In a 4-fold cross validation, the original dataset is partitioned into four mutually exclusive and exhaustive subsets with equal sizes $( S u b _ { 1 } , S u b _ { 2 } , S u b _ { 3 }$ , and $S u b _ { 4 } )$ . Then, the models are developed four times, each time the model is trained on three of the subsets, and is tested on the fourth one. The final performance will be the average of the models 1, 2, 3, and 4. Figure 5 shows the mechanism of 4-fold cross validation.

# ACCEPTED MANUSCRIPT

In order to further reduce the effect of randomness, we ran each 4-fold cross validation on all approaches 10 times. Therefore, each approach has been applied to each dataset 40 times. As a result, for each evaluation metric we have both average value and 95% confidence interval. Tables 3 and 4 show the performance of all of the 9 imbalanced data learning approaches as well as the learning from original imbalanced dataset in a linear SVM classifier. The first row for each dataset in this table shows the evaluation metric average (G mean in Table 3 and AUC in Table 4), the second row shows the half of the 95% confidence interval width (HCI) for the evaluation metric, and the third row shows the performance ranking of each approach compared to other approaches.

![](/api/attachments/C5PFEEGZ/fulltext/images/72a475f74bd3566906c9653f7a136e8a83ea414f1d6486417f059ff9d6db49fc.jpg)  
Figure 5. 4-fold cross validation mechanism

As it can be seen in Tables 3 and 4, in all of the 15 imbalanced datasets, our proposed algorithms, SIMO and W-SIMO had the best performance compared to other approaches (approaches with ranks 1, 2, and 3 are bolded in Tables 3 and 4). In addition, the difference between the G mean and AUC value for SIMO and W-SIMO and other approaches is significant. To show this difference and the achieved improvement thorough applying our algorithm, we calculated the difference between the G mean and AUC of our algorithm and the G mean and AUC of the best algorithm among other approaches (the approach with rank 3 in Tables 3 and 4) in all datasets. We also calculated the difference between the G mean and AUC of the best and second best algorithms among approaches other than our algorithm (the approaches with rank 3 and 4 in Tables 3 and 4) in all 15 benchmark datasets. Table 5 shows the average of these differences in all datasets. We ran a t test to compare the improvement from the approach with rank 3 to our algorithm to the achieved improvement from the approach with rank 4 to the approach with rank 3 (best and second best approaches not including SIMO and W-SIMO). The p-values for G mean and AUC were 0.0106 and 0.0136 respectively. Therefore, the t test showed that the difference between our algorithm and best algorithm among other existing approaches was significantly greater than the difference between the approaches with rank 3 and 4 at the confidence level of 95%. Table 6 demonstrates the overall ranking of SIMO and W-SIMO compared to other imbalanced data learning approaches when applied to linear SVM. The overall ranking is calculated based on the average of various approaches’ ranking in 15 benchmark datasets. Since W-SIMO and SIMO had the first and second places in all datasets, their overall ranking is 1.1 and 1.9 respectively.

## ACCEPTED MANUSCRIPT

Table 3. Comparing the performance of various imbalance data learning approaches (using G mean)

<table><tr><td colspan="2"></td><td>Original Data</td><td>Under Sampling</td><td>SMOTE</td><td>BorSMOTE</td><td>Safe Level SMOTE</td><td>Cluster SMOTE</td><td>SMOTE-IPF</td><td>Cost Sensitive</td><td>SIMO</td><td>W-SIMO</td></tr><tr><td rowspan="3">Liver</td><td>G mean</td><td>64.86%</td><td>65.37%</td><td>65.16%</td><td>64.62%</td><td>64.93%</td><td>65.89%</td><td>66.16%</td><td>65.23%</td><td>68.62%</td><td>69.08%</td></tr><tr><td>95% HCI</td><td>0.92%</td><td>1.68%</td><td>1.65%</td><td>1.25%</td><td>2.22%</td><td>1.19%</td><td>1.40%</td><td>1.14%</td><td>1.10%</td><td>1.50%</td></tr><tr><td>Rank</td><td>9</td><td>5</td><td>7</td><td>10</td><td>8</td><td>4</td><td>3</td><td>6</td><td>2</td><td>1</td></tr><tr><td rowspan="3">Ionosphere</td><td>G mean</td><td>82.92%</td><td>82.70%</td><td>83.36%</td><td>82.29%</td><td>82.47%</td><td>83.29%</td><td>83.58%</td><td>83.19%</td><td>84.69%</td><td>84.99%</td></tr><tr><td>95% HCI</td><td>1.97%</td><td>1.40%</td><td>1.48%</td><td>1.42%</td><td>2.12%</td><td>1.85%</td><td>1.49%</td><td>1.04%</td><td>0.90%</td><td>1.77%</td></tr><tr><td>Rank</td><td>7</td><td>8</td><td>4</td><td>10</td><td>9</td><td>5</td><td>3</td><td>6</td><td>2</td><td>1</td></tr><tr><td rowspan="3">Pima</td><td>G mean</td><td>70.12%</td><td>74.07%</td><td>74.33%</td><td>72.98%</td><td>74.61%</td><td>74.44%</td><td>74.34%</td><td>74.11%</td><td>75.48%</td><td>76.26%</td></tr><tr><td>95% HCI</td><td>0.91%</td><td>1.25%</td><td>0.90%</td><td>0.67%</td><td>0.77%</td><td>0.90%</td><td>0.87%</td><td>1.14%</td><td>0.69%</td><td>0.67%</td></tr><tr><td>Rank</td><td>10</td><td>8</td><td>6</td><td>9</td><td>3</td><td>4</td><td>5</td><td>7</td><td>2</td><td>1</td></tr><tr><td rowspan="3">BreastCO</td><td>G mean</td><td>96.71%</td><td>96.84%</td><td>97.09%</td><td>96.74%</td><td>96.96%</td><td>97.00%</td><td>97.45%</td><td>97.14%</td><td>97.87%</td><td>97.94%</td></tr><tr><td>95% HCI</td><td>0.32%</td><td>0.63%</td><td>0.36%</td><td>0.43%</td><td>0.37%</td><td>0.43%</td><td>0.36%</td><td>0.34%</td><td>0.29%</td><td>0.26%</td></tr><tr><td>Rank</td><td>10</td><td>8</td><td>5</td><td>9</td><td>7</td><td>6</td><td>3</td><td>4</td><td>2</td><td>1</td></tr><tr><td rowspan="3">Iris</td><td>G mean</td><td>57.72%</td><td>72.14%</td><td>74.54%</td><td>72.48%</td><td>75.17%</td><td>75.82%</td><td>76.20%</td><td>74.48%</td><td>78.13%</td><td>78.38%</td></tr><tr><td>95% HCI</td><td>7.67%</td><td>2.64%</td><td>2.60%</td><td>3.04%</td><td>1.55%</td><td>2.39%</td><td>2.12%</td><td>2.77%</td><td>1.80%</td><td>1.41%</td></tr><tr><td>Rank</td><td>10</td><td>9</td><td>6</td><td>8</td><td>5</td><td>4</td><td>3</td><td>7</td><td>2</td><td>1</td></tr><tr><td rowspan="3">Yeast</td><td>G mean</td><td>41.08%</td><td>70.42%</td><td>70.90%</td><td>69.19%</td><td>70.69%</td><td>70.96%</td><td>70.68%</td><td>70.89%</td><td>72.25%</td><td>72.12%</td></tr><tr><td>95% HCI</td><td>0.55%</td><td>0.78%</td><td>0.62%</td><td>0.53%</td><td>0.49%</td><td>0.55%</td><td>0.51%</td><td>0.64%</td><td>0.39%</td><td>0.46%</td></tr><tr><td>Rank</td><td>10</td><td>8</td><td>4</td><td>9</td><td>6</td><td>3</td><td>7</td><td>5</td><td>1</td><td>2</td></tr><tr><td rowspan="3">Vehicle</td><td>G mean</td><td>95.63%</td><td>95.83%</td><td>95.98%</td><td>95.78%</td><td>95.83%</td><td>95.76%</td><td>96.05%</td><td>95.90%</td><td>96.58%</td><td>96.81%</td></tr><tr><td>95% HCI</td><td>0.51%</td><td>0.53%</td><td>0.59%</td><td>0.59%</td><td>0.46%</td><td>0.45%</td><td>0.47%</td><td>0.63%</td><td>0.32%</td><td>0.51%</td></tr><tr><td>Rank</td><td>10</td><td>7</td><td>4</td><td>8</td><td>6</td><td>9</td><td>3</td><td>5</td><td>2</td><td>1</td></tr><tr><td rowspan="3">CMC</td><td>G mean</td><td>0.24%</td><td>65.45%</td><td>65.15%</td><td>64.72%</td><td>65.60%</td><td>65.38%</td><td>65.38%</td><td>65.55%</td><td>66.06%</td><td>66.55%</td></tr><tr><td>95% HCI</td><td>0.02%</td><td>1.17%</td><td>0.70%</td><td>0.49%</td><td>0.63%</td><td>0.55%</td><td>0.62%</td><td>0.25%</td><td>1.00%</td><td>0.49%</td></tr><tr><td>Rank</td><td>10</td><td>5</td><td>8</td><td>9</td><td>3</td><td>7</td><td>7</td><td>4</td><td>2</td><td>1</td></tr><tr><td rowspan="3">BreastC20</td><td>G mean</td><td>96.20%</td><td>96.12%</td><td>96.01%</td><td>96.28%</td><td>95.88%</td><td>96.12%</td><td>96.07%</td><td>96.12%</td><td>97.53%</td><td>97.55%</td></tr><tr><td>95% HCI</td><td>0.48%</td><td>0.82%</td><td>0.69%</td><td>0.49%</td><td>0.76%</td><td>0.44%</td><td>0.61%</td><td>0.73%</td><td>0.53%</td><td>0.40%</td></tr><tr><td>Rank</td><td>4</td><td>6</td><td>9</td><td>3</td><td>10</td><td>6</td><td>8</td><td>6</td><td>2</td><td>1</td></tr><tr><td rowspan="3">Vowel</td><td>G mean</td><td>86.85%</td><td>87.90%</td><td>89.03%</td><td>89.77%</td><td>88.90%</td><td>89.98%</td><td>89.26%</td><td>88.10%</td><td>91.06%</td><td>91.10%</td></tr><tr><td>95% HCI</td><td>0.55%</td><td>0.90%</td><td>0.59%</td><td>0.51%</td><td>0.99%</td><td>0.91%</td><td>0.87%</td><td>0.75%</td><td>0.79%</td><td>0.98%</td></tr><tr><td>Rank</td><td>10</td><td>9</td><td>6</td><td>4</td><td>7</td><td>3</td><td>5</td><td>8</td><td>2</td><td>1</td></tr><tr><td rowspan="3">Ecoli</td><td>G mean</td><td>71.28%</td><td>89.29%</td><td>89.55%</td><td>84.80%</td><td>90.05%</td><td>90.10%</td><td>89.90%</td><td>90.03%</td><td>91.85%</td><td>91.88%</td></tr><tr><td>95% HCI</td><td>1.62%</td><td>1.10%</td><td>1.14%</td><td>1.00%</td><td>0.65%</td><td>0.79%</td><td>0.75%</td><td>0.80%</td><td>0.76%</td><td>0.41%</td></tr><tr><td>Rank</td><td>10</td><td>8</td><td>7</td><td>9</td><td>4</td><td>3</td><td>6</td><td>5</td><td>2</td><td>1</td></tr><tr><td rowspan="3">Libras12</td><td>G mean</td><td>66.35%</td><td>33.99%</td><td>43.77%</td><td>44.69%</td><td>43.93%</td><td>48.34%</td><td>58.06%</td><td>70.69%</td><td>87.07%</td><td>85.49%</td></tr><tr><td>95% HCI</td><td>5.33%</td><td>3.53%</td><td>0.97%</td><td>2.45%</td><td>0.90%</td><td>1.31%</td><td>2.64%</td><td>6.63%</td><td>1.67%</td><td>2.49%</td></tr><tr><td>Rank</td><td>4</td><td>10</td><td>9</td><td>7</td><td>8</td><td>6</td><td>5</td><td>3</td><td>1</td><td>2</td></tr><tr><td rowspan="3">Libras34</td><td>G mean</td><td>84.04%</td><td>88.93%</td><td>89.36%</td><td>87.57%</td><td>89.90%</td><td>88.43%</td><td>89.72%</td><td>89.76%</td><td>91.64%</td><td>91.87%</td></tr><tr><td>95% HCI</td><td>3.24%</td><td>2.51%</td><td>1.73%</td><td>2.01%</td><td>1.56%</td><td>1.13%</td><td>1.56%</td><td>1.86%</td><td>1.70%</td><td>1.33%</td></tr><tr><td>Rank</td><td>10</td><td>7</td><td>6</td><td>9</td><td>3</td><td>8</td><td>5</td><td>4</td><td>2</td><td>1</td></tr><tr><td rowspan="3">Glass</td><td>G mean</td><td>91.62%</td><td>91.45%</td><td>91.52%</td><td>91.41%</td><td>91.09%</td><td>91.95%</td><td>91.99%</td><td>91.40%</td><td>92.84%</td><td>92.86%</td></tr><tr><td>95% HCI</td><td>2.31%</td><td>1.30%</td><td>2.03%</td><td>1.67%</td><td>1.59%</td><td>1.23%</td><td>1.36%</td><td>1.10%</td><td>1.55%</td><td>1.16%</td></tr><tr><td>Rank</td><td>5</td><td>7</td><td>6</td><td>8</td><td>10</td><td>4</td><td>3</td><td>9</td><td>2</td><td>1</td></tr><tr><td rowspan="3">BreastC10</td><td>G mean</td><td>94.06%</td><td>95.50%</td><td>94.53%</td><td>94.41%</td><td>94.72%</td><td>94.47%</td><td>95.70%</td><td>94.59%</td><td>95.98%</td><td>96.09%</td></tr><tr><td>95% HCI</td><td>1.65%</td><td>1.35%</td><td>0.85%</td><td>1.05%</td><td>1.01%</td><td>0.41%</td><td>0.76%</td><td>0.87%</td><td>0.74%</td><td>0.83%</td></tr><tr><td>Rank</td><td>10</td><td>4</td><td>7</td><td>9</td><td>5</td><td>8</td><td>3</td><td>6</td><td>2</td><td>1</td></tr></table>

## ACCEPTED MANUSCRIPT

Table 4. Comparing the performance of various imbalance data learning approaches (using AUC)

<table><tr><td colspan="2"></td><td>Original Data</td><td>Under Sampling</td><td>SMOTE</td><td>BorSMOTE</td><td>Safe Level SMOTE</td><td>Cluster SMOTE</td><td>SMOTE-IPF</td><td>Cost Sensitive</td><td>SIMO</td><td>W-SIMO</td></tr><tr><td rowspan="3">Liver</td><td>AUC</td><td>66.53%</td><td>65.62%</td><td>65.39%</td><td>64.86%</td><td>65.18%</td><td>66.64%</td><td>66.40%</td><td>65.50%</td><td>68.97%</td><td>69.45%</td></tr><tr><td>95% HCI</td><td>0.72%</td><td>1.63%</td><td>1.56%</td><td>1.30%</td><td>2.06%</td><td>1.20%</td><td>1.32%</td><td>1.09%</td><td>0.97%</td><td>1.38%</td></tr><tr><td>Rank</td><td>4</td><td>6</td><td>8</td><td>10</td><td>9</td><td>3</td><td>5</td><td>7</td><td>2</td><td>1</td></tr><tr><td rowspan="3">Ionosphere</td><td>AUC</td><td>83.94%</td><td>83.34%</td><td>83.98%</td><td>82.73%</td><td>83.30%</td><td>84.06%</td><td>83.92%</td><td>83.43%</td><td>85.22%</td><td>85.59%</td></tr><tr><td>95% HCI</td><td>1.73%</td><td>1.19%</td><td>1.34%</td><td>1.33%</td><td>1.88%</td><td>1.66%</td><td>1.34%</td><td>0.95%</td><td>0.84%</td><td>1.76%</td></tr><tr><td>Rank</td><td>5</td><td>8</td><td>4</td><td>10</td><td>9</td><td>3</td><td>6</td><td>7</td><td>2</td><td>1</td></tr><tr><td rowspan="3">Pima</td><td>AUC</td><td>72.03%</td><td>74.26%</td><td>74.49%</td><td>73.21%</td><td>74.76%</td><td>74.59%</td><td>74.52%</td><td>74.29%</td><td>75.71%</td><td>76.47%</td></tr><tr><td>95% HCI</td><td>0.74%</td><td>1.21%</td><td>0.87%</td><td>0.61%</td><td>0.74%</td><td>0.89%</td><td>0.84%</td><td>1.07%</td><td>0.65%</td><td>0.66%</td></tr><tr><td>Rank</td><td>10</td><td>8</td><td>6</td><td>9</td><td>3</td><td>4</td><td>5</td><td>7</td><td>2</td><td>1</td></tr><tr><td rowspan="3">BreastCO</td><td>AUC</td><td>96.72%</td><td>96.85%</td><td>97.10%</td><td>96.76%</td><td>96.97%</td><td>97.01%</td><td>97.48%</td><td>97.15%</td><td>97.89%</td><td>97.97%</td></tr><tr><td>95% HCI</td><td>0.32%</td><td>0.63%</td><td>0.36%</td><td>0.43%</td><td>0.37%</td><td>0.43%</td><td>0.36%</td><td>0.33%</td><td>0.29%</td><td>0.26%</td></tr><tr><td>Rank</td><td>10</td><td>8</td><td>5</td><td>9</td><td>7</td><td>6</td><td>3</td><td>4</td><td>2</td><td>1</td></tr><tr><td rowspan="3">Iris</td><td>AUC</td><td>63.82%</td><td>73.60%</td><td>75.50%</td><td>74.05%</td><td>75.93%</td><td>76.77%</td><td>77.14%</td><td>75.46%</td><td>79.12%</td><td>79.32%</td></tr><tr><td>95% HCI</td><td>3.29%</td><td>2.66%</td><td>2.66%</td><td>2.95%</td><td>1.54%</td><td>2.05%</td><td>1.87%</td><td>2.49%</td><td>1.45%</td><td>1.47%</td></tr><tr><td>Rank</td><td>10</td><td>9</td><td>6</td><td>8</td><td>5</td><td>4</td><td>3</td><td>7</td><td>2</td><td>1</td></tr><tr><td rowspan="3">Yeast</td><td>AUC</td><td>57.56%</td><td>70.57%</td><td>71.05%</td><td>70.18%</td><td>70.78%</td><td>71.07%</td><td>70.85%</td><td>70.98%</td><td>72.45%</td><td>72.33%</td></tr><tr><td>95% HCI</td><td>0.20%</td><td>0.71%</td><td>0.50%</td><td>0.54%</td><td>0.42%</td><td>0.52%</td><td>0.48%</td><td>0.56%</td><td>0.45%</td><td>0.46%</td></tr><tr><td>Rank</td><td>10</td><td>8</td><td>4</td><td>9</td><td>7</td><td>3</td><td>6</td><td>5</td><td>1</td><td>2</td></tr><tr><td rowspan="3">Vehicle</td><td>AUC</td><td>95.68%</td><td>95.86%</td><td>96.02%</td><td>95.83%</td><td>95.87%</td><td>95.80%</td><td>96.10%</td><td>95.94%</td><td>96.60%</td><td>96.84%</td></tr><tr><td>95% HCI</td><td>0.50%</td><td>0.53%</td><td>0.58%</td><td>0.59%</td><td>0.45%</td><td>0.44%</td><td>0.46%</td><td>0.61%</td><td>0.31%</td><td>0.50%</td></tr><tr><td>Rank</td><td>10</td><td>7</td><td>4</td><td>8</td><td>6</td><td>9</td><td>3</td><td>5</td><td>2</td><td>1</td></tr><tr><td rowspan="3">CMC</td><td>AUC</td><td>50.24%</td><td>65.85%</td><td>65.47%</td><td>65.80%</td><td>65.82%</td><td>65.86%</td><td>66.06%</td><td>65.81%</td><td>66.35%</td><td>66.76%</td></tr><tr><td>95% HCI</td><td>0.02%</td><td>1.17%</td><td>0.65%</td><td>0.44%</td><td>0.58%</td><td>0.54%</td><td>0.53%</td><td>0.23%</td><td>0.71%</td><td>0.61%</td></tr><tr><td>Rank</td><td>10</td><td>5</td><td>9</td><td>8</td><td>6</td><td>4</td><td>3</td><td>7</td><td>2</td><td>1</td></tr><tr><td rowspan="3">BreastC20</td><td>AUC</td><td>96.23%</td><td>96.14%</td><td>96.04%</td><td>96.29%</td><td>95.91%</td><td>96.14%</td><td>96.11%</td><td>96.14%</td><td>97.54%</td><td>97.59%</td></tr><tr><td>95% HCI</td><td>0.46%</td><td>0.81%</td><td>0.68%</td><td>0.48%</td><td>0.75%</td><td>0.44%</td><td>0.61%</td><td>0.73%</td><td>0.52%</td><td>0.39%</td></tr><tr><td>Rank</td><td>4</td><td>6</td><td>9</td><td>3</td><td>10</td><td>6</td><td>8</td><td>6</td><td>2</td><td>1</td></tr><tr><td rowspan="3">Vowel</td><td>AUC</td><td>87.50%</td><td>87.96%</td><td>89.08%</td><td>89.88%</td><td>88.96%</td><td>90.10%</td><td>89.32%</td><td>88.29%</td><td>91.16%</td><td>91.25%</td></tr><tr><td>95% HCI</td><td>0.50%</td><td>0.88%</td><td>0.59%</td><td>0.50%</td><td>0.98%</td><td>0.89%</td><td>0.84%</td><td>0.72%</td><td>0.75%</td><td>0.88%</td></tr><tr><td>Rank</td><td>10</td><td>9</td><td>6</td><td>4</td><td>7</td><td>3</td><td>5</td><td>8</td><td>2</td><td>1</td></tr><tr><td rowspan="3">Ecoli</td><td>AUC</td><td>75.29%</td><td>89.47%</td><td>89.70%</td><td>85.06%</td><td>90.20%</td><td>90.22%</td><td>90.02%</td><td>90.19%</td><td>91.96%</td><td>91.97%</td></tr><tr><td>95% HCI</td><td>1.16%</td><td>1.07%</td><td>1.17%</td><td>0.97%</td><td>0.63%</td><td>0.81%</td><td>0.74%</td><td>0.78%</td><td>0.74%</td><td>0.41%</td></tr><tr><td>Rank</td><td>10</td><td>8</td><td>7</td><td>9</td><td>4</td><td>3</td><td>6</td><td>5</td><td>2</td><td>1</td></tr><tr><td rowspan="3">Libras12</td><td>AUC</td><td>72.81%</td><td>55.65%</td><td>55.47%</td><td>51.93%</td><td>54.95%</td><td>55.59%</td><td>70.06%</td><td>74.03%</td><td>88.15%</td><td>86.83%</td></tr><tr><td>95% HCI</td><td>3.14%</td><td>1.73%</td><td>1.42%</td><td>2.16%</td><td>1.48%</td><td>1.65%</td><td>2.49%</td><td>5.37%</td><td>1.41%</td><td>1.93%</td></tr><tr><td>Rank</td><td>4</td><td>6</td><td>8</td><td>10</td><td>9</td><td>7</td><td>5</td><td>3</td><td>1</td><td>2</td></tr><tr><td rowspan="3">Libras34</td><td>AUC</td><td>85.17%</td><td>89.12%</td><td>89.61%</td><td>87.88%</td><td>90.17%</td><td>88.76%</td><td>89.97%</td><td>89.94%</td><td>91.82%</td><td>92.03%</td></tr><tr><td>95% HCI</td><td>2.61%</td><td>2.50%</td><td>1.65%</td><td>1.90%</td><td>1.42%</td><td>1.07%</td><td>1.48%</td><td>1.80%</td><td>1.63%</td><td>1.29%</td></tr><tr><td>Rank</td><td>10</td><td>7</td><td>6</td><td>9</td><td>3</td><td>8</td><td>4</td><td>5</td><td>2</td><td>1</td></tr><tr><td rowspan="3">Glass</td><td>AUC</td><td>92.07%</td><td>91.78%</td><td>91.85%</td><td>91.86%</td><td>91.56%</td><td>92.25%</td><td>92.31%</td><td>91.70%</td><td>93.13%</td><td>93.22%</td></tr><tr><td>95% HCI</td><td>2.08%</td><td>1.21%</td><td>1.89%</td><td>1.57%</td><td>1.47%</td><td>1.15%</td><td>1.28%</td><td>1.13%</td><td>1.38%</td><td>1.03%</td></tr><tr><td>Rank</td><td>5</td><td>8</td><td>7</td><td>6</td><td>10</td><td>4</td><td>3</td><td>9</td><td>2</td><td>1</td></tr><tr><td rowspan="3">BreastC10</td><td>AUC</td><td>94.26%</td><td>95.57%</td><td>94.64%</td><td>94.53%</td><td>94.85%</td><td>94.58%</td><td>95.83%</td><td>94.68%</td><td>96.07%</td><td>96.18%</td></tr><tr><td>95% HCI</td><td>1.57%</td><td>1.30%</td><td>0.78%</td><td>0.93%</td><td>0.96%</td><td>0.39%</td><td>0.71%</td><td>0.78%</td><td>0.71%</td><td>0.78%</td></tr><tr><td>Rank</td><td>10</td><td>4</td><td>7</td><td>9</td><td>5</td><td>8</td><td>3</td><td>6</td><td>2</td><td>1</td></tr></table>

# ACCEPTED MANUSCRIPT

As we mentioned earlier, the oversampled training data by SIMO and W-SIMO can be used in any other machine learning technique. Therefore, SIMO and W-SIMO can be considered pre-processing oversampling algorithms. To evaluate the performance of SIMO and W-SIMO in other data mining techniques, we applied them in SVM with RBF kernel function, logistic regression, and decision tree. Tables 7, 8, and 9 present the overall rankings of our algorithms as well as their counterparts when applied to SVM with RBF kernel, logistic regression, and decision tree in all benchmark datasets. As it can be seen in Tables 7, 8, and 9, the overall ranking of W-SIMO and SIMO is not about 1 and 2, unlike what we observed in Table 6. This means that our algorithms were not always the best when applied in machine learning techniques other than linear SVM. In fact, these results were expected since SIMO and W-SIMO are imbedded into linear SVM, therefore, we expected them to have a better performance in linear SVM. Even though our algorithms were not always the best ones in other machine learning techniques, their overall performance was better compared to other approaches. As Tables 7, 8, and 9 show, either SIMO or W-SIMO was the best overall algorithm in SVM with RBF kernel, logistic regression, and decision tree.

Table 5. Average difference between the performance of our algorithm and other approaches

<table><tr><td></td><td>Average difference between our algorithm and the best one among other approaches</td><td>Average difference between the best and second best ones among other approaches</td></tr><tr><td>G mean</td><td>2.36%</td><td>0.44%</td></tr><tr><td>AUC</td><td>2.2%</td><td>0.23%</td></tr></table>

<table><tr><td colspan="3">Table 6. Overall ranking on linear SVM</td><td colspan="3">Table 7. Overall ranking- SVM-RBF kernel</td></tr><tr><td>Approach</td><td>G Mean</td><td>AUC</td><td>Approach</td><td>G Mean</td><td>AUC</td></tr><tr><td>W-SIMO</td><td>1.1</td><td>1.1</td><td>W-SIMO</td><td>2.9</td><td>2.8</td></tr><tr><td>SIMO</td><td>1.9</td><td>1.9</td><td>Cluster SMOTE</td><td>3.8</td><td>3.9</td></tr><tr><td>SMOTE-IPF</td><td>4.6</td><td>4.5</td><td>SIMO</td><td>4.2</td><td>4.2</td></tr><tr><td>Cluster SMOTE</td><td>5.3</td><td>5.0</td><td>SMOTE-IPF</td><td>4.9</td><td>4.8</td></tr><tr><td>Cost Sensitive</td><td>5.7</td><td>6.1</td><td>Cost Sensitive</td><td>5.0</td><td>4.9</td></tr><tr><td>SMOTE</td><td>6.3</td><td>6.4</td><td>Under Sampling</td><td>5.6</td><td>5.6</td></tr><tr><td>Safe Level SMOTE</td><td>6.3</td><td>6.7</td><td>Safe Level SMOTE</td><td>6.3</td><td>6.3</td></tr><tr><td>Under Sampling</td><td>7.3</td><td>7.1</td><td>SMOTE</td><td>6.8</td><td>6.9</td></tr><tr><td>BorSMOTE</td><td>8.1</td><td>8.1</td><td>BorSMOTE</td><td>7.1</td><td>7.2</td></tr><tr><td>Original Data</td><td>8.6</td><td>8.1</td><td>Original Data</td><td>8.4</td><td>8.4</td></tr><tr><td colspan="3">Table 8. Overall ranking on Logistic Regression</td><td colspan="3">Table 9. Overall ranking on Decision Tree</td></tr><tr><td>Approach</td><td>G Mean</td><td>AUC</td><td>Approach</td><td>G Mean</td><td>AUC</td></tr><tr><td>W-SIMO</td><td>2.6</td><td>2.4</td><td>SIMO</td><td>2.8</td><td>2.7</td></tr><tr><td>Cluster SMOTE</td><td>3.3</td><td>3.6</td><td>SMOTE-IPF</td><td>3.0</td><td>3.1</td></tr><tr><td>SMOTE-IPF</td><td>3.9</td><td>4.2</td><td>Under Sampling</td><td>3.9</td><td>3.8</td></tr><tr><td>SMOTE</td><td>4.6</td><td>4.5</td><td>W-SIMO</td><td>4.2</td><td>4.3</td></tr><tr><td>SIMO</td><td>4.8</td><td>4.9</td><td>SMOTE</td><td>5.2</td><td>5.1</td></tr><tr><td>Safe Level SMOTE</td><td>5.4</td><td>5.4</td><td>Cluster SMOTE</td><td>5.5</td><td>5.2</td></tr><tr><td>Under Sampling</td><td>6</td><td>5.8</td><td>Original Data</td><td>5.5</td><td>5.9</td></tr><tr><td>BorSMOTE</td><td>6.8</td><td>6.7</td><td>Safe Level SMOTE</td><td>6.8</td><td>6.5</td></tr><tr><td>Original Data</td><td>7.6</td><td>7.5</td><td>BorSMOTE</td><td>8.1</td><td>8.4</td></tr></table>

As we noted in the introduction section, one of the reasons that we used SVM in our algorithm was its great performance and accuracy compared to other machine learning techniques. The results of the numerical experiments in logistic regression and decision tree showed that our algorithm was not always the best in all datasets in these data mining techniques. However, when we compared the best performing algorithms (imbalanced data learning algorithms, such as SIMO, SMOTE, and under-sampling) in each machine learning technique in each dataset, it turned out that SVM always outperformed other data mining techniques. Therefore, our algorithm might not always have the best performance when applied to logistic regression and decision tree, but its performance in SVM is better and has higher G mean and AUC. Table 10 demonstrates these results. For each dataset, we provide the G mean and AUC of the best imbalanced data learning approach in each of the four machine learning techniques, linear SVM, SVM with RBF kernel, logistic regression, and decision tree. The bold numbers show the best performing machine learning technique in each dataset and the underlined numbers are the results of our algorithms. Only in three datasets, the best performing model was not incorporated with our algorithm; those cases are shown in italic bold. The output of our algorithm in those cases is shown in parenthesis and they are not much lower than the best performing approaches. Overall, no one can claim that their algorithm is the best performing algorithm in all datasets, because the performance of a technique or algorithm highly depends on the distribution, size, and complexity of datasets, however, the overall performance of algorithms on multiple datasets from various domains can be a fair comparison measure.

Table 10. The performance of best approach in each machine learning technique

<table><tr><td></td><td colspan="2">SVM-Linear</td><td colspan="2">SVM-RBF</td><td colspan="2">Logistic Regression</td><td colspan="2">Decision Tree</td></tr><tr><td></td><td>G mean</td><td>AUC</td><td>G mean</td><td>AUC</td><td>G mean</td><td>AUC</td><td>G mean</td><td>AUC</td></tr><tr><td>Liver</td><td>69.08%</td><td>69.45%</td><td>62.31%</td><td>64.09%</td><td>65.19%</td><td>66.77%</td><td>62.51%</td><td>63.18%</td></tr><tr><td>Ionosphere</td><td>84.99%</td><td>85.59%</td><td>94.11%(94.00%)</td><td>94.19%(94.04%)</td><td>81.54%</td><td>82.62%</td><td>87.68%</td><td>87.79%</td></tr><tr><td>Pima</td><td>76.26%</td><td>76.47%</td><td>70.51%</td><td>70.62%</td><td>74.60%</td><td>74.66%</td><td>69.25%</td><td>69.38%</td></tr><tr><td>BreastCO</td><td>97.94%</td><td>97.97%</td><td>97.04%</td><td>97.16%</td><td>96.52%</td><td>96.54%</td><td>94.76%</td><td>94.84%</td></tr><tr><td>Iris</td><td>78.38%</td><td>79.32%</td><td>97.06%</td><td>97.14%</td><td>75.12%</td><td>75.50%</td><td>94.31%</td><td>94.45%</td></tr><tr><td>Yeast</td><td>72.25%</td><td>72.45%</td><td>70.31%</td><td>70.39%</td><td>70.88%</td><td>71.17%</td><td>66.28%</td><td>66.39%</td></tr><tr><td>Vehicle</td><td>96.81%</td><td>96.84%</td><td>95.90%</td><td>96.04%</td><td>96.25%</td><td>96.30%</td><td>91.56%</td><td>91.64%</td></tr><tr><td>CMC</td><td>66.55%</td><td>66.76%</td><td>66.17%</td><td>66.35%</td><td>65.74%</td><td>65.92%</td><td>61.82%</td><td>61.98%</td></tr><tr><td>BreastC20</td><td>97.55%</td><td>97.59%</td><td>97.34%</td><td>97.35%</td><td>96.37%</td><td>96.43%</td><td>93.61%</td><td>93.57%</td></tr><tr><td>Vowel</td><td>91.10%</td><td>91.25%</td><td>99.61%</td><td>99.66%</td><td>90.35%</td><td>90.41%</td><td>95.67%</td><td>95.62%</td></tr><tr><td>Ecoli</td><td>91.88%</td><td>91.97%</td><td>93.56%(91.93%)</td><td>93.67%(92.72%)</td><td>90.69%</td><td>90.79%</td><td>86.20%</td><td>86.88%</td></tr><tr><td>Libras12</td><td>87.07%</td><td>88.15%</td><td>97.68%</td><td>97.79%</td><td>39.37%</td><td>42.83%</td><td>84.34%</td><td>85.86%</td></tr><tr><td>Libras34</td><td>91.87%</td><td>92.03%</td><td>93.01%</td><td>93.15%</td><td>82.84%</td><td>83.06%</td><td>82.75%</td><td>83.13%</td></tr><tr><td>Glass</td><td>92.86%</td><td>93.22%</td><td>89.43%</td><td>89.98%</td><td>91.62%</td><td>91.93%</td><td>92.40%</td><td>92.63%</td></tr><tr><td>BreastC10</td><td>96.09%</td><td>96.18%</td><td>96.76%</td><td>96.81%</td><td>94.76%</td><td>94.85%</td><td>92.23%</td><td>92.36%</td></tr></table>

Another advantage of our proposed algorithm is that it makes a minimal alteration to the original distribution of the dataset. While other over-sampling approaches generate enough data points to completely fill the imbalanced gap in the data, SIMO and W-SIMO only focus on the informative data points close to the decision boundary between two classes in the data, and therefore, they do not generate as many synthetic data points as other over-sampling methods. Table 11 demonstrates the imbalanced gap between majority and minority class in various datasets. It also shows the average number of data points generated by our algorithms as well as other over-sampling approaches. The number in parenthesis shows the amount of the synthetically generated data points as a percentage of the total imbalanced gap in the training datasets. As it can be seen, SIMO and W-SIMO usually generate less number of data points compared to other over-sampling methods. This result shows two advantages of our proposed algorithms. First, our algorithms do not dramatically change the distribution of the data from its original shape. Second, with less amount of data generated, the further computational cost in training the machine learning techniques will be lower.

Table 11. Imbalanced gap and Average # of synthetically generated data points (% of the imbalance gap)

<table><tr><td></td><td>Imbalanced Gap in Training Data</td><td>Other Approaches</td><td>SIMO</td><td>W-SIMO</td></tr><tr><td>Liver</td><td>41</td><td>41 (100%)</td><td>20 (48.8%)</td><td>22 (53.7%)</td></tr><tr><td>Ionosphere</td><td>75</td><td>75 (100%)</td><td>18 (24%)</td><td>22 (29.3%)</td></tr><tr><td>Pima</td><td>174</td><td>174 (100%)</td><td>104 (59.8%)</td><td>96 (55.1%)</td></tr><tr><td>BreastCO</td><td>154</td><td>154 (100%)</td><td>25 (16.2%)</td><td>30 (19.5%)</td></tr><tr><td>Iris</td><td>38</td><td>38 (100%)</td><td>25 (65.8%)</td><td>24 (63.1%)</td></tr><tr><td>Yeast</td><td>467</td><td>467 (100%)</td><td>392 (83.9%)</td><td>373 (79.9%)</td></tr><tr><td>Vehicle</td><td>336</td><td>336 (100%)</td><td>50 (14.9%)</td><td>46 (13.7%)</td></tr><tr><td>CMC</td><td>606</td><td>606 (100%)</td><td>543 (89.6%)</td><td>569 (93.9%)</td></tr><tr><td>BreastC20</td><td>229</td><td>229 (100%)</td><td>13 (5.7%)</td><td>18 (7.9%)</td></tr><tr><td>Vowel</td><td>473</td><td>473 (100%)</td><td>173 (36.6%)</td><td>152 (32.1%)</td></tr><tr><td>Ecoli</td><td>174</td><td>174 (100%)</td><td>60 (34.5%)</td><td>58 (33.3%)</td></tr><tr><td>Libras12</td><td>175</td><td>175 (100%)</td><td>29 (16.6%)</td><td>17 (9.7%)</td></tr><tr><td>Libras34</td><td>180</td><td>180 (100%)</td><td>20 (11.1%)</td><td>17 (9.4%)</td></tr><tr><td>Glass</td><td>117</td><td>117 (100%)</td><td>5 (4.2%)</td><td>6 (5.1%)</td></tr><tr><td>BreastC10</td><td>282</td><td>282 (100%)</td><td>35 (12.4%)</td><td>19 (6.7%)</td></tr></table>

## 5.4 Sensitivity Analysis

For applying SIMO and W-SIMO, their parameters, i.e. ∆, ??, and ?? need to be specified. To evaluate the performance of SIMO in different parameters values, we performed a sensitivity analysis. In the sensitivity analysis, we considered values 10% to 50% for ∆, and 5% to 50% for ??. Table 12 depicts the results of the sensitivity analysis for ∆=10, 20, 30, and 40% and ??=10 and 40%. As it can be seen in Table 12, different values of parameters do not make a considerable difference in the performance of SIMO. Therefore, SIMO is not very sensitive to the value of its parameters. Moreover, except in 4 cases, in all of the other cases, with even the worst parameters value, SIMO had a better performance compared to the 3<sup>rd</sup> best approach. Based $\mathrm { o n }$ this analysis, we suggest the following policy for choosing the parameters values. When the imbalance ratio of the data is high (the minority class rate below 20%), it is better to select higher values for $\Delta$ and ??, i.e. values between 30 to 40% for ∆, and values between 25 to 50% for $p .$ The reason is that, because the number of the minority data points in highly imbalanced datasets is very low, by selecting relatively higher values for ∆, we consider greater number of minority data points for over-sampling. Therefore, we avoid the potential overfitting that might happen. On the other hand, for datasets with lower imbalanced ratio (the minority class rate between 20-40%), choosing lower values for $\Delta$ and ?? will generate better results. selecting the parameters for W-SIMO follows the same policy with one difference, and that is selecting a higher value for ?? compared to $p .$ Our suggestion based on the sensitivity analysis is to choose 20 to 30% greater values for ??. For example, if $p { = } 2 0 \%$ , values between 40 to 50% are appropriate for ??.

Table 12. Sensitivity analysis on SIMO parameters

<table><tr><td colspan="11">SIMO</td><td rowspan="2">3rd best approach</td></tr><tr><td></td><td></td><td colspan="2">Δ=10%</td><td colspan="2">Δ=20%</td><td colspan="2">Δ=30%</td><td colspan="2">Δ=40%</td><td>Best Δ &amp; p</td></tr><tr><td></td><td></td><td>p=10%</td><td>p=40%</td><td>p=10%</td><td>p=40%</td><td>p=10%</td><td>p=40%</td><td>p=10%</td><td>p=40%</td><td></td><td></td></tr><tr><td rowspan="2">Liver</td><td>G mean</td><td>68.99%</td><td>68.70%</td><td>68.91%</td><td>68.73%</td><td>68.57%</td><td>68.58%</td><td>68.32%</td><td>68.42%</td><td>Δ=10%</td><td>66.16%</td></tr><tr><td>AUC</td><td>69.34%</td><td>68.91%</td><td>69.26%</td><td>68.94%</td><td>68.74%</td><td>68.67%</td><td>68.60%</td><td>68.60%</td><td>p=10%</td><td>66.64%</td></tr><tr><td rowspan="2">Ionosphere</td><td>G mean</td><td>85.14%</td><td>84.94%</td><td>85.10%</td><td>84.49%</td><td>84.74%</td><td>84.46%</td><td>84.49%</td><td>84.18%</td><td>Δ=20%</td><td>83.58%</td></tr><tr><td>AUC</td><td>85.71%</td><td>85.55%</td><td>85.63%</td><td>84.64%</td><td>85.43%</td><td>85.01%</td><td>85.16%</td><td>84.87%</td><td>p=05%</td><td>84.06%</td></tr><tr><td rowspan="2">Pima</td><td>G mean</td><td>75.88%</td><td>75.59%</td><td>75.99%</td><td>75.90%</td><td>75.65%</td><td>75.75%</td><td>75.64%</td><td>75.52%</td><td>Δ=20%</td><td>74.61%</td></tr><tr><td>AUC</td><td>76.08%</td><td>75.80%</td><td>76.22%</td><td>76.12%</td><td>75.98%</td><td>75.97%</td><td>75.86%</td><td>75.64%</td><td>p=10%</td><td>74.76%</td></tr><tr><td rowspan="2">BreastCO</td><td>G mean</td><td>98.14%</td><td>98.07%</td><td>98.13%</td><td>98.12%</td><td>98.15%</td><td>97.88%</td><td>97.90%</td><td>97.76%</td><td>Δ=15%</td><td>97.45%</td></tr><tr><td>AUC</td><td>98.15%</td><td>98.09%</td><td>98.15%</td><td>98.13%</td><td>98.16%</td><td>97.90%</td><td>97.91%</td><td>97.77%</td><td>p=15%</td><td>97.48%</td></tr><tr><td rowspan="2">Iris</td><td>G mean</td><td>78.45%</td><td>78.45%</td><td>78.91%</td><td>78.24%</td><td>78.76%</td><td>78.03%</td><td>78.44%</td><td>78.08%</td><td>Δ=20%</td><td>76.20%</td></tr><tr><td>AUC</td><td>79.15%</td><td>79.18%</td><td>79.68%</td><td>78.97%</td><td>79.46%</td><td>78.80%</td><td>79.20%</td><td>78.61%</td><td>p=25%</td><td>77.14%</td></tr><tr><td rowspan="2">Yeast</td><td>G mean</td><td>71.86%</td><td>72.33%</td><td>72.21%</td><td>72.03%</td><td>72.31%</td><td>71.80%</td><td>71.80%</td><td>71.58%</td><td>Δ=10%</td><td>70.96%</td></tr><tr><td>AUC</td><td>72.10%</td><td>72.51%</td><td>72.40%</td><td>72.26%</td><td>72.46%</td><td>72.05%</td><td>72.06%</td><td>71.79%</td><td>p=15%</td><td>71.07%</td></tr><tr><td rowspan="2">Vehicle</td><td>G mean</td><td>96.74%</td><td>96.94%</td><td>96.84%</td><td>96.77%</td><td>97.03%</td><td>96.73%</td><td>96.92%</td><td>96.75%</td><td>Δ=30%</td><td>96.05%</td></tr><tr><td>AUC</td><td>96.76%</td><td>96.95%</td><td>96.87%</td><td>96.79%</td><td>97.06%</td><td>96.76%</td><td>96.94%</td><td>96.77%</td><td>p=30%</td><td>96.1%</td></tr><tr><td rowspan="2">CMC</td><td>G mean</td><td>66.03%</td><td>66.15%</td><td>66.32%</td><td>66.48%</td><td>66.46%</td><td>66.34%</td><td>66.14%</td><td>65.96%</td><td>Δ=20%</td><td>65.60%</td></tr><tr><td>AUC</td><td>66.33%</td><td>66.44%</td><td>66.55%</td><td>66.77%</td><td>66.74%</td><td>66.62%</td><td>66.44%</td><td>66.28%</td><td>p=40%</td><td>66.06%</td></tr><tr><td rowspan="2">BreastC20</td><td>G mean</td><td>97.72%</td><td>97.59%</td><td>97.85%</td><td>97.67%</td><td>97.47%</td><td>97.41%</td><td>97.33%</td><td>97.25%</td><td>Δ=12%</td><td>96.28%</td></tr><tr><td>AUC</td><td>97.73%</td><td>97.60%</td><td>97.86%</td><td>97.68%</td><td>97.49%</td><td>97.42%</td><td>97.34%</td><td>97.26%</td><td>p=05%</td><td>96.29%</td></tr><tr><td rowspan="2">Vowel</td><td>G mean</td><td>90.94%</td><td>91.50%</td><td>90.95%</td><td>91.22%</td><td>91.13%</td><td>90.92%</td><td>91.19%</td><td>91.00%</td><td>Δ=10%</td><td>89.98%</td></tr><tr><td>AUC</td><td>91.06%</td><td>91.60%</td><td>91.08%</td><td>91.35%</td><td>91.24%</td><td>91.01%</td><td>91.31%</td><td>91.12%</td><td>p=35%</td><td>90.10%</td></tr><tr><td rowspan="2">Ecoli</td><td>G mean</td><td>91.30%</td><td>91.51%</td><td>92.06%</td><td>92.02%</td><td>92.15%</td><td>91.74%</td><td>91.99%</td><td>91.94%</td><td>Δ=12%</td><td>90.10%</td></tr><tr><td>AUC</td><td>91.51%</td><td>91.72%</td><td>92.17%</td><td>92.13%</td><td>92.25%</td><td>91.84%</td><td>92.07%</td><td>92.05%</td><td>p=20%</td><td>90.22%</td></tr><tr><td rowspan="2">Libras12</td><td>G mean</td><td>86.98%</td><td>87.12%</td><td>87.47%</td><td>86.85%</td><td>86.67%</td><td>86.44%</td><td>86.50%</td><td>86.50%</td><td>Δ=20%</td><td>70.69%</td></tr><tr><td>AUC</td><td>88.16%</td><td>88.26%</td><td>88.55%</td><td>88.08%</td><td>87.77%</td><td>87.53%</td><td>87.75%</td><td>87.81%</td><td>p=10%</td><td>74.03%</td></tr><tr><td rowspan="2">Libras34</td><td>G mean</td><td>91.12%</td><td>91.31%</td><td>91.55%</td><td>91.51%</td><td>91.75%</td><td>91.76%</td><td>91.63%</td><td>91.71%</td><td>Δ=30%</td><td>89.90%</td></tr><tr><td>AUC</td><td>91.30%</td><td>91.50%</td><td>91.84%</td><td>91.72%</td><td>91.95%</td><td>91.96%</td><td>91.80%</td><td>91.87%</td><td>p=25%</td><td>90.17%</td></tr><tr><td rowspan="2">Glass</td><td>G mean</td><td>92.98%</td><td>92.67%</td><td>92.63%</td><td>92.89%</td><td>92.77%</td><td>93.02%</td><td>92.95%</td><td>92.51%</td><td>Δ=30%</td><td>91.99%</td></tr><tr><td>AUC</td><td>93.28%</td><td>92.98%</td><td>92.96%</td><td>93.19%</td><td>93.07%</td><td>93.31%</td><td>93.28%</td><td>92.86%</td><td>p=40%</td><td>92.31%</td></tr><tr><td rowspan="2">BreastC10</td><td>G mean</td><td>95.39%</td><td>95.73%</td><td>95.72%</td><td>95.90%</td><td>95.91%</td><td>95.71%</td><td>95.96%</td><td>96.21%</td><td>Δ=40%</td><td>95.70%</td></tr><tr><td>AUC</td><td>95.54%</td><td>95.80%</td><td>95.79%</td><td>95.99%</td><td>96.02%</td><td>95.85%</td><td>96.07%</td><td>96.30%</td><td>p=35%</td><td>95.83%</td></tr></table>

## 6 Discussion and Conclusion

Imbalanced datasets are widespread in various domains such as healthcare, finance, and information system security. Nowadays, a large portion of decision support systems are built by analyzing data.

# ACCEPTED MANUSCRIPT

Therefore, decision support systems in the above mentioned domains are affected by the imbalanced data learning challenges. In an imbalanced dataset, the number of examples belonging to one class outnumbers the number of examples from the other class. Therefore, in an imbalanced dataset, there are majority and minority classes of examples. Training machine-learning techniques using imbalanced datasets is a critical challenge in data analytics. The prediction accuracy of a data mining technique, especially prediction accuracy of detecting the minority class in an imbalanced dataset, is inferior to the performance of the same technique when applied to a balanced dataset. There has been an enormous effort to address the problem of imbalanced data learning in recent years. Sampling methods along with cost sensitive approaches are among the most efficient remedies to the imbalanced data learning problem. Improving the prediction accuracy of machine learning techniques when applied to imbalanced datasets, leads to better decision making in real world problems. This improved decision making is critically important when we are dealing with imbalanced datasets, because in most the cases, the minority class is the class of interest for decision makers. As a result, any effort toward enhancing imbalanced data learning,

In this study, we proposed a synthetic informative minority oversampling (SIMO) algorithm integrated with SVM to enhance the performance of machine learning techniques when applied to imbalanced datasets. In this algorithm, first SVM is applied to the original imbalanced dataset. In the next step, minority examples close to the SVM decision boundary are selected as the informative minority examples. Next, these examples are over-sampled to a pre-specified degree. Finally, a new SVM model is developed on the updated dataset. This process iterates until we reach a pre-specified balance level. In each iteration, we have an updated training dataset, which is formed by adding the newly generated data points to the previous dataset. Each of these training datasets is used to develop a SVM model, and the SVM model is assessed on the test dataset. At the end, the best model and its associated training dataset is selected as the final over-sampled training dataset. In this research, we also developed another version of SIMO called W-SIMO. W-SIMO is different from SIMO in the degree of over-sampling the informative minority examples. In W-SIMO, informative minority examples that are incorrectly classified are oversampled with a higher degree compared to the informative minority examples that are correctly classified. In this way, there is more focus on incorrectly classified minority examples.

SIMO and W-SIMO have several advantages compared to other imbalanced data learning methods. First, they leverage SVM, which is a powerful machine learning technique in pattern recognition problems. Second, in SIMO and W-SIMO, we over-sample the minority examples rather than under-sampling the majority examples, therefore we avoid losing potentially useful information by discarding some portion of the data. Third, our focus in SIMO and W-SIMO is only on the data points (examples) near the decision boundary as the informative minority data points. This focus is even more important in W-SIMO where we over-sample the incorrectly classified examples with a higher degree. Therefore, SIMO and W-SIMO concentrate on the informative minority examples that usually are misclassified by standard machine learning techniques. Fourth, compared to other oversampling methods, SIMO generates fewer synthetic data points. Therefore, the changes to the original distribution of the data and further computational costs will be lower compared to other oversampling approaches. Fifth, the oversampled data through SIMO can be used to train any other machine learning technique, thus its application is not limited only to SVM. Finally, SIMO and W-SIMO are not very sensitive to their parameters, even though we suggest to select higher values for ∆ and ?? in highly imbalanced datasets and lower values in moderately imbalanced datasets.

We applied our algorithms to 15 publicly available benchmark imbalanced datasets and assessed their performance in comparison with existing approaches in the area of imbalanced data learning. These approaches were cost sensitive SVM, under sampling, SMOTE, cluster SMOTE, safe level SMOTE and borderline SMOTE as well as the original imbalanced dataset. Our algorithm had the best performance in all datasets compared to the other seven approaches in the linear SVM. In fact, the difference between our algorithm and second best algorithm was significantly greater than the difference between other algorithms (for instance, the difference between second and third best approaches). Besides linear SVM that SIMO and W-SIMO were integrated with, we also assessed SIMO and W-SIMO in other machine learning techniques such as SVM with RBF kernel, logistic regression, and decision tree. Our algorithms were not always the best in these machine learning techniques in all bench mark datasets, however their overall performances were better than all other imbalanced data learning approaches. Moreover, the results showed that the best performing machine learning technique in all datasets was either linear SVM or SVM with RBF kernel function, and except for in three datasets, our algorithms were the best ones. From the practical implication point of view, our proposed algorithm can enhance the performance of the predictive models and decision support systems in various domains such as diagnosing diseases, detecting re-admissions, and predicting the loan defaults in financial institutions among other application domains.

Our proposed algorithms may have a limitation that all of the over-sampling approaches face. This limitation is the computational time when the algorithms are applied to very large size datasets. Even though considering the recent advances in computational power of the computers, the computational time is not as critical as it used to be, we still need to enhance the speed of our algorithms in large size datasets. Therefore, we consider speeding up our algorithms in big data usage as one of the most important directions for future research. One way to achieve higher speed could be decreasing the size of the data thorough approaches such as variable selection before using the data in over-sampling algorithms. Another way could be improving the SVM training algorithms. We are considering another direction for future research, and that is applying our developed algorithms to develop a clinical decision support system for predicting kidney disease among diabetic patients. The dataset that we are going to use for that research contains the lab, demographic, clinical events, and comorbidity data of a large number of diabetic patients. We believe that this future research will reveal the performance and efficiency of our algorithm in a larger imbalanced dataset.

## References

[1] S. Piri, D. Delen, T. Liu, and H. M. Zolbanin, "A data analytics approach to building a clinical decision support system for diabetic retinopathy: Developing and deploying a model ensemble," Decision Support Systems, vol. 101, pp. 12-27, 2017/09/01 2017.

[2] A. Dag, A. Oztekin, A. Yucel, S. Bulur, and F. M. Megahed, "Predicting heart transplantation outcomes through data analytics," Decision Support Systems, vol. 94, no. Supplement C, pp. 42- 52, 2017/02/01/ 2017.

[3] P. K. Chan, F. Wei, A. L. Prodromidis, and S. J. Stolfo, "Distributed data mining in credit card fraud detection," Intelligent Systems and their Applications, IEEE, vol. 14, no. 6, pp. 67-74, 1999.

[4] E. Tobback, T. Bellotti, J. Moeyersoms, M. Stankova, and D. Martens, "Bankruptcy prediction for SMEs using relational data," Decision Support Systems, vol. 102, Supplement C, 69-81, 2017.

[5] P. Liu, Y. Wang, L. Cai, and L. Zhang, "Classifying skewed data streams based on reusing data," in 2010 International Conference on Computer Application and System Modeling (ICCASM 2010), 2010, vol. 4, pp. V4-90-V4-93: IEEE.

[6] M. A. Maloof, "Learning when data sets are imbalanced and when costs are unequal and unknown," in ICML-2003 workshop on learning from imbalanced data sets II, 2003, vol. 2, pp. 2- 1.

[7] H. He and E. A. Garcia, "Learning from imbalanced data," Knowledge and Data Engineering, IEEE Transactions on, vol. 21, no. 9, pp. 1263-1284, 2009.

[8] M. A. Hearst, S. T. Dumais, E. Osman, J. Platt, and B. Scholkopf, "Support vector machines," IEEE Intelligent Systems and their Applications, vol. 13, no. 4, pp. 18-28, 1998.

[9] A. Anand, G. Pugalenthi, G. B. Fogel, and P. Suganthan, "An approach for classification of highly imbalanced data using weighting and undersampling," Amino acids, 39(5), 1385-1391, 2010.

[10] H. Yu, C. Mu, C. Sun, W. Yang, X. Yang, and X. Zuo, "Support vector machine-based optimized decision threshold adjustment strategy for classifying imbalanced data," Knowledge-Based Systems, vol. 76, pp. 67-78, 2015.

[11] X.-Y. Liu, J. Wu, and Z.-H. Zhou, "Exploratory undersampling for class-imbalance learning," IEEE Transactions on Systems, Man, and Cybernetics, Part B (Cybernetics), vol. 39, no. 2, pp. 539-550, 2009.

[12] N. V. Chawla, K. W. Bowyer, L. O. Hall, and W. P. Kegelmeyer, "SMOTE: synthetic minority over-sampling technique," Journal of artificial intelligence research, pp. 321-357, 2002.

[13] N. J. Benjamin X. Wang "Imbalanced Data Set Learning with Synthetic Samples," in IRIS Machine Learning Workshop, 2004.

[14] H. Han, W.-Y. Wang, and B.-H. Mao, "Borderline-SMOTE: a new over-sampling method in imbalanced data sets learning," in Advances in intelligent computing: Springer, 2005, pp. 878- 887.

[15] C. Bunkhumpornpat, K. Sinapiromsaran, and C. Lursinsap, "Safe-Level-SMOTE: Safe-Level-Synthetic Minority Over-Sampling TEchnique for Handling the Class Imbalanced Problem," in Advances in Knowledge Discovery and Data Mining: 13th Pacific-Asia Conference, PAKDD 2009 Bangkok, Thailand, April 27-30, 2009 Proceedings, T. Theeramunkong, B. Kijsirikul, N. Cercone, and T.-B. Ho, Eds. Berlin, Heidelberg: Springer Berlin Heidelberg, 2009, pp. 475-482.

[16] D. A. Cieslak, N. V. Chawla, and A. Striegel, "Combating imbalance in network intrusion datasets," in IEEE International Conference on Granular Computing, 2006, pp. 732-737.

[17] S. Barua, M. M. Islam, X. Yao, and K. Murase, "MWMOTE--Majority Weighted Minority Oversampling Technique for Imbalanced Data Set Learning," IEEE Transactions on Knowledge and Data Engineering, vol. 26, no. 2, pp. 405-425, 2014.

[18] J. A. Sáez, J. Luengo, J. Stefanowski, and F. Herrera, "SMOTE–IPF: Addressing the noisy and borderline examples problem in imbalanced classification by a re-sampling method with filtering," Information Sciences, vol. 291, pp. 184-203, 2015.

[19] H. He, Y. Bai, E. Garcia, and S. Li, "ADASYN: Adaptive synthetic sampling approach for Computational Intelligence). IEEE International Joint Conference on, 2008, pp. 1322-1328: IEEE.

[20] A. Pourhabib, B. K. Mallick, and Y. Ding, "Absent data generating classifier for imbalanced class sizes," The Journal of Machine Learning Research, vol. 16, no. 1, pp. 2695-2724, 2015.

[21] S. Piri, D. Delen, T. Liu, and H. M. Zolbanin, "A data analytics approach to building a clinical decision support system for diabetic retinopathy: Developing and deploying a model ensemble," Decision Support Systems, 2017.

[22] B. Wang and N. Japkowicz, "Imbalanced data set learning with synthetic samples," in Proc. IRIS Machine Learning Workshop, 2004, p. 19.

## ACCEPTED MANUSCRIPT

[23] C. Elkan, "The foundations of cost-sensitive learning," in International joint conference on artificial intelligence, 2001, vol. 17, no. 1, pp. 973-978.

[24] R. Longadge and S. Dongre, "Class Imbalance Problem in Data Mining Review," arXiv preprint arXiv:1305.1707, 2013.

[25] Y. Freund and R. E. Schapire, "A desicion-theoretic generalization of on-line learning and an application to boosting," in European conference on computational learning theory, 1995, pp. 23- 37: Springer Berlin Heidelberg.

[26] Y. Sun, M. S. Kamel, A. K. Wong, and Y. Wang, "Cost-sensitive boosting for classification of imbalanced data," Pattern Recognition, vol. 40, no. 12, pp. 3358-3378, 2007.

[27] W. Fan, S. J. Stolfo, J. Zhang, and P. K. Chan, "AdaCost: misclassification cost-sensitive boosting," in Icml, 1999, pp. 97-105.

[28] W. Lee, C.-H. Jun, and J.-S. Lee, "Instance categorization by support vector machines to adjust weights in AdaBoost for imbalanced data classification," Information Sciences, 381, 92-103, 2017.

[29] C. Drummond and R. C. Holte, "Exploiting the cost (in) sensitivity of decision tree splitting criteria," in ICML, 2000, vol. 1, no. 1.

[30] M. Kukar and I. Kononenko, "Cost-Sensitive Learning with Neural Networks," in ECAI, 1998, pp. 445-449.

[31] K. Veropoulos, C. Campbell, and N. Cristianini, "Controlling the sensitivity of support vector machines," in Proceedings of the international joint conference on AI, 1999, pp. 55-60.

[32] G. Wu and E. Y. Chang, "Class-boundary alignment for imbalanced dataset learning," in ICML 2003 workshop on learning from imbalanced data sets II, Washington, DC, 2003, pp. 49-56.

[33] R. Akbani, S. Kwek, and N. Japkowicz, "Applying support vector machines to imbalanced datasets," in European conference on machine learning, 2004, pp. 39-50: Springer.

[34] B. Wang and N. Japkowicz, "Boosting support vector machines for imbalanced data sets," Knowledge and information systems, vol. 25, no. 1, pp. 1-20, 2010.

[35] J. Mathew, M. Luo, C. K. Pang, and H. L. Chan, "Kernel-based SMOTE for SVM classification of imbalanced datasets," in Industrial Electronics Society, IECON 2015-41st Annual Conference of the IEEE, 2015, pp. 001127-001132: IEEE.

[36] C. Jian, J. Gao, and Y. Ao, "A new sampling method for classifying imbalanced data based on support vector machine ensemble," Neurocomputing, vol. 193, pp. 115-122, 2016.

[37] Y.-H. Shao, W.-J. Chen, J.-J. Zhang, Z. Wang, and N.-Y. Deng, "An efficient weighted Lagrangian twin support vector machine for imbalanced data classification," Pattern Recognition, vol. 47, no. 9, pp. 3158-3167, 2014.

[38] Y. Tang and Y.-Q. Zhang, "Granular SVM with repetitive undersampling for highly imbalanced protein homology prediction," in 2006 IEEE International Conference on Granular Computing, 2006, pp. 457-460: IEEE.

[39] R. Batuwita and V. Palade, "Efficient resampling methods for training support vector machines with imbalanced datasets," in The 2010 International Joint Conference on Neural Networks (IJCNN), 2010, pp. 1-8: IEEE.

[40] M. A. H. Farquad and I. Bose, "Preprocessing unbalanced data using support vector machine," Decision Support Systems, vol. 53, no. 1, pp. 226-233, 4// 2012.

[41] C. J. Burges, "A tutorial on support vector machines for pattern recognition," Data mining and knowledge discovery, vol. 2, no. 2, pp. 121-167, 1998.

[42] B. E. Boser, I. M. Guyon, and V. N. Vapnik, "A training algorithm for optimal margin classifiers," in Proceedings of the fifth annual workshop on Computational learning theory, 1992, pp. 144-152: ACM.

[43] G. Wu and E. Y. Chang, "Adaptive feature-space conformal transformation for imbalanced-data learning," in ICML, 2003, pp. 816-823.

[44] N. V. Chawla, "Data mining for imbalanced datasets: An overview," in Data mining and knowledge discovery handbook: Springer, 2005, pp. 853-867.

[45] G. Seni and J. F. Elder, "Ensemble methods in data mining: improving accuracy through combining predictions," Synthesis Lectures on Data Mining and Knowledge Discovery, vol. 2, no. 1, pp. 1-126, 2010.

# ACCEPTED MANUSCRIPT

## Authors’ Biographies

![](/api/attachments/C5PFEEGZ/fulltext/images/d2bfb96a0b581a5112318ea9c8b9a9fb90f4f032ff766f012ffcf5cd8d477089.jpg)

Saeed Piri is a PhD student in the Industrial Engineering and Management and a Research Associate in the Center for Health Systems Innovation at Oklahoma State University. He earned his Master’s degree in Industrial Engineering from Sharif University of Technology in 2008. He has presented his research in several national and international conferences. His research interests include developing decision support systems, machine learning, imbalanced data learning, and application of business analytics in healthcare domain.

![](/api/attachments/C5PFEEGZ/fulltext/images/4dc40dd92ebe50c74689ec16d8cc6b384a21be686822e0e6c0e2241f5e573c5f.jpg)

Dr. Dursun Delen is the holder of William S. Spears and Neal Patterson Endowed Chairs in Business Analytics, Director of Research for the Center for Health Systems Innovation, and Professor of Management Science and Information Systems in the Spears School of Business at Oklahoma State University (OSU). He received his Ph.D. in Industrial Engineering and Management from OSU in 1997. Prior to his appointment as an Assistant Professor at OSU in 2001, he worked for a privately-owned research and

consultancy company, Knowledge Based Systems Inc., in College Station, Texas, as a research scientist for five years, during which he led a number of decision support, information systems and advanced analytics related research projects funded by federal agencies, including DoD, NASA, NIST and DOE. His research has appeared in major journals including Decision Support Systems, Communications of the ACM, Computers and Operations Research, Computers in Industry, Journal of Production Operations Management, Artificial Intelligence in Medicine, Expert Systems with Applications, among others. He recently published seven books/textbooks in the broader are of Business Analytics. He is often invited to national and international conferences for keynote addresses on topics related to Healthcare Analytics Data/Text Mining, Business Intelligence, Decision Support Systems, Business Analytics and Knowledge Management. He regularly serves and chairs tracks and mini-tracks at various information systems and analytics conferences, and serves on several academic journals as editor-in-chief, senior editor, associate editor and editorial board member. His research and teaching interests are in data and text mining, decision support systems, knowledge management, business intelligence and enterprise modeling.

# ACCEPTED MANUSCRIPT

![](/api/attachments/C5PFEEGZ/fulltext/images/326e7166deb9643fe2d01668808a856fc9ea101f85fa6eea495e1e6682654490.jpg)

Dr. Tieming Liu is an associate professor at the School of Industrial Engineering and Management, Oklahoma State University. He received his doctoral degree in Transportation and Logistics from the Massachusetts Institute of Technology in 2005, his master’s degree in Industrial Engineering and Management Science from Northwestern University in 2001, and his master’s and bachelor’s degrees in Control Theory and Control Engineering from Tsinghua University in 2000 and 1997, respectively. His research interests include supply chain management, logistics planning, and healthcare analytics. His research has been

published in major journals, including IIE Transactions, Interfaces, Production and Operations Management, Naval Research Logistics, Operations Research Letters, European Journal of Operational Research, among others.

## Highlights

\- This research addresses the imbalanced data learning problem.

\- Two over-sampling algorithms, termed SIMO and W-SIMO, are proposed.

\- The performance of SIMO and W-SIMO are assessed by comparing them to the exiting approaches.

\- Numerical experiments showed better performance of SIMO and W-SIMO compared to the existing approaches.
