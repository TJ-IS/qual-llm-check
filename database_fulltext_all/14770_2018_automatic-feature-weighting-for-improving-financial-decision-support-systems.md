---
otero_id: 14770
otero_key: "REMFDNX6"
title: "Automatic feature weighting for improving financial Decision Support Systems"
authors: "Yosimar Oswaldo Serrano-Silva; Yenny Villuendas-Rey; Cornelio Yáñez-Márquez"
year: "2018"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2018.01.005"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Automatic feature weighting for improving financial Decision Support Systems

Yosimar Oswaldo Serrano-Silva <sup>a</sup>, Yenny Villuendas-Rey <sup>b,</sup>⁎, Cornelio Yáñez-Márquez <sup>a,</sup>⁎

<sup>a</sup> Centro de Investigación en Computación del Instituto Politécnico Nacional, Av. Juan de Dios Bátiz Esq. Miguel Othón de Mendizábal S/N, Nueva Industrial Vallejo, 07738 Gustavo A. Madero, CDMX, Mexico

<sup>b</sup> Centro de Innovación y Desarrollo Tecnológico en Cómputo del Instituto Politécnico Nacional, Av. Juan de Dios Bátiz Esq. Miguel Othón de Mendizábal S/N, Nueva Industrial Vallejo, 07738 Gustavo A. Madero, CDMX, Mexico

## a r t i c l e i n f o

Article history: Received 11 September 2017 Received in revised form 23 January 2018 Accepted 24 January 2018 Available online 31 January 2018

Keywords: Credit risk Bankruptcy prediction Banknote authentication Bank telemarketing Feature weight Decision support

## a b s t r a c t

We propose a novel methodology for improving financial Decision Support Systems (DSS) through automatic feature weighting. Using this methodology, we show that automatic feature weighting leads to a significant improvement in the performance of decision-making algorithms over financial data, which are the key of financial DSS. The statistical analysis carried out shows that metaheuristic algorithms are good for automatic feature weighting, and that Differential Evolution (DE) offers a good trade-off between decision-making performance and computational cost. We believe these results contribute to the development of novel financial DSS.

© 2018 Elsevier B.V. All rights reserved.

## 1. Introduction

In the world of financial companies, risk means the danger of loss [1]. Financial companies assume a certain credit risk in each one of the operations they carry out (loans, lines of credit, and guarantees, among others). These financial companies cannot know everything about of their clients and, on the other hand, a client's compliance with its obligations to a financial company depends on events in which no one can know whether they will occur. That is, there is an uncertainty associated to whether a customer will (or will not) pay their debt [2,3].

According to the Global Association of Risk Professionals (GARP), which is a non-for-profit association for world-class financial risk certification, the presence of risks in financial companies is relevant because the mismanagement of financial risks can lead to global financial crises, such as those registered in the world in a cyclical manner, since the origins of financial systems. In this context, financial companies have developed numerous methods to value credits and determine credit risks, as well as their management; all of this, in order to improve financial results and profitability. Some of these methods are closely linked to models of computer sensitivity, which indicates the importance of computational methods in financial risk management [4].

With the tremendous advance of technology, and specifically with the arrival in the world of powerful computer systems, in the 1980s financial institutions turned to see the possibilities that this type of technology offers them in their field of action. Thus, some researchers decided to venture into this type of topics, so that computing in its different manifestations, became part of the financing processes, including desktop computers.

According to [5], several types of DSS are being applied in the world of financial risks, such as neural networks and pattern recognition techniques. These approaches, among others, have provided a theoretical foundation for developing DSS (including expert systems) to estimate, for instance, the probability of bankruptcy and predict fraud.

While it is true that DSS are not the only option to solve problems related to financial risks, their importance as a good option has been growing in recent years [6]. They have been applied in quality control, financial forecasting, targeted marketing, bankruptcy prediction, optical character recognition, among other problems [2–9].

In the present work, we address the following problems: credits risk, bankruptcy prediction, banknote authentication and bank telemarketing. To do this, we focused on a key aspect of DSS: the improvement of the decision-making (or prediction) algorithm. Those algorithms are the kernel of DSS, due to they help the system to process knowledge and to “decide” or to predict the most likely situation in the future. For instance, the prediction of risks in the financial environment can be seen as a decision-making problem. That is, by deciding that a company is in bankruptcy risk, we can reduce the uncertainty for the potential investors, and the risk of capital loss due to an investment in a company that may be in bankruptcy in short term. In this work we are focused on the improvement of an algorithm recently proposed by us, which was designed for the financial area: the Naïve Associative Classifier (NAC) [3]. While it is true that there are several algorithms in the literature that can be used by DSS to improve decision-making [10–15], we have chosen the NAC because that it is one of the topics on which we are currently directing our research efforts.

The NAC has obtained very promising preliminary results in financial decision-making, and we hypothesize that if we develop a methodology for the automatic obtaining of weights for the attributes or features that describe financial data, we can improve the performance of the NAC in financial decision-making. Thus, we aim at improving the decision-making process, by improving the learning algorithm that guides this process.

Clearly, attribute selection is not the most important process to solve financial risk problems. Its importance lies in that, by improving the NAC, we can apply this model to different problems, ensuring better efficacy in the results; therefore, by making a good feature selection the NAC improves, and consequently, its application in DSS to reduce financial risks will be more effective. On the other hand, it is not in our interest to analyze the problems that people find when selecting attributes: we focus on selecting attributes to improve the NAC, and consequently to solve and predict financial risks in different areas. The results of this work support this affirmation.

Our main objective is to contribute to the development of DSS in the financial field, through the design of a methodology for the automatic adjustment of the attribute weights of financial data, by means of metaheuristic algorithms [7–9]. This methodology should improve the decision-making process in the financial area.

To test our hypothesis, we designed an experimental framework, taking into consideration the characteristics of financial data (such as data imbalance, presence of missing values, and presence of both numeric and categorical attributes), the functioning of metaheuristic algorithms, as well as the functioning of the NAC. We intended to compare the algorithms over the same conditions, and then to test the performance of the proposed automatic feature weighting methodology.

This paper offers the following contributions. First, we demonstrate how we can automatically obtain attribute weights in financial datasets, and how to improve the decision-making process in a Decision Support System of the financial field. Second, we examine the effect of metaheuristic algorithms for feature weighting, in the context of the NAC. The study's third contribution concerns the determination of the best metaheuristic for attribute weighting in the financial decisionmaking scenario. Our results show that DE is the most adequate algorithm for financial feature weighting.

The remainder of this paper is structured as follows. In Section 2, we review the related scientific literature on some of the problems that involve some type of risk within the financial environment. Then, in Section 3 we briefly describe the NAC, while in Section 4 the most relevant part of this article is profusely explained: the proposed methodology for financial feature weighting. After that, we present the results obtained, and discuss them in Section 5. The article ends with the conclusions in Section 6.

## 2. Related scientific literature

This section includes, and briefly describes, some of the research works that have addressed some of the four problems that we address in the present work: credits risk, bankruptcy prediction, banknote authentication and bank telemarketing. In this sense, the relationship of each of these works with our proposal is that the purpose is common: solve any of the four mentioned problems, using a computational method based on DSS. It is worth mentioning that, as far as we know, our proposal is the first to address financial problems by the improvement of a DSS through automatic feature weighting using metaheuristics. This means that in none of the works described in this section, feature selection, or feature weights, or metaheuristics are relevant. In the context of this article, the relevance of the works described here lies in the problems that intend to resolve, which are similar to those we approach with our proposal. In [10], the problem of credit risk and credit approval is faced. The authors propose a model to improve corporate credit rating systems that help financial experts to make decisions. Another different approach, based on social media is shown in [11], where it is analyzed whether the different opinions shared by users about different financial issues in these media are relevant or not for the prediction of credit risk to future of financial companies. To carry out this study, the authors analyzed the opinions expressed in two of the social networks for most popular financial investors in China, in addition to various articles published by financial analysts.

The second problem that we have selected, bankruptcy prediction, consists of to determine whether a company will be bankrupt in the near future [12]. Both financial institutions and investors need to reduce the possible risk of not obtaining the expected dividends or even of not recovering their capital if certain company declares bankruptcy. These types of situations can be addressed as a classification problem, in which a company can be classified as bankrupt or not in a short term, according to its current characteristics [6]. In this context, it is also important for financial firms to determine whether a person applying for a loan can file for bankruptcy in the short term, which would result in losses to such companies. It is well known that financial companies to grant some type of bank credit carry out a study of the client requesting such credit, i.e. they need to know if its economic solvency is good to be able to pay their obligations. For this type of problem, a model is proposed in [14] to help predict good clients (those who will meet their obligations), and bad clients (those who are likely to fail to fulfill their obligations for bankruptcy). With regard to banknote authentication problem, in [15] a system developed for discriminating fake notes from genuine ones and apply it to Indian banknotes is described. Image processing and pattern recognition techniques are used to design the overall approach.

The last of the problems we have selected is telemarketing. Today marketing campaigns can be considered as one of the most important business strategies, because different marketing strategies help companies to meet different goals and target specific sectors of customers [16]. However, the task of selecting the largest set of potential customers, for example, those clients most likely to hire a service or banking product, is considered NP-hard [17], so different solutions have been proposed to this problem in particular.

In one of these solutions, published in [18], a Decision Support System based on a Data Mining approach is proposed, which can automatically predict the outcome of a telephone call in which a banking service is offered. This DSS is intended to support the managers of financial companies in the selection and prioritization of customers to contact by telephone in the telemarketing banking campaigns and, consequently, reduce the cost and time of them. Another proposal is presented in [19], which is very similar to the previous proposal, since both seek to optimize the subscriptions to a banking service through telephone calls using a DSS, but in this case the aforementioned DSS uses Artificial Neural Networks

To conclude this section, it is necessary to mention what concerns to algorithms used for decision-making, against which our proposal will compete. In the design and operation of the DSS are used several of these algorithms, among which the Artificial Neural Networks, the Support Vector Machines, the C4.5, the rule induction, the Instance-based learning algorithms and those based on the Bayes Theorem stand out [20–25].

The results obtained in [16] were taken into account in our experiments. In those results, the performance of the NAC was significantly better than the models RIPPER, MLP, SMO and 1NN, so we discarded those models, and only C4.5 and Naïve Bayes (NB) were considered in our experiments, due to they do not had significant difference in performance with respect to NAC in the experiments of [16]. Therefore, our proposal will be measured against algorithms that could not be overcome before, in the mentioned experiments. We hope that the methodology proposed in this article can serve as a tool to reduce the different financial risks.

## 3. Decision-making methods: the NAC classifier

One of the most important subsystems of a DSS is the Knowledge based subsystem (KBS), which deals with data, and process it in order to obtain (or to extract) valuable knowledge about the phenomenon under study. This knowledge is used by KBS in the decision-making process. Usually, the KBS includes a classification (or learning) algorithm that supports decision-making. In this section, we explain the functioning of the learning algorithm used as a case study in the proposed methodology: the NAC.

The NAC classifier is a recently created associative learning model, whose main characteristics are its simplicity and transparency, but not because of these characteristics, it is less efficient. This algorithm has the advantage of not needing a large number of parameters to be set by the user. In addition, it is indifferent to the types of data contained in the dataset to classify, and to the presence or absence of missing values. It is not worthily to mention that NAC was specially designed for decision-making with financial data [3].

This classification model uses a similarity operator called MIDSO, which allows it to obtain competitive results without the need to perform data preprocessing. MIDSO (Mixed and Incomplete Data Similarity Operator), is a similarity operator that can handle missing values as well as numeric and categorical attributes. These characteristic make MIDSO the kernel of NAC classifier. Although the MIDSO operator does not need specific data, as mentioned above, it should be noted that processing different type data for the similarity calculation, is carried out independently, as can be observed in the following definition:

$$
\text { MIDSO } (x, y, A _ {i}) = \left\{ \begin{array}{l l} s _ {c} (x, y, A _ {i}) & \text { if   } A _ {i} \text {   is   categorical } \\ s _ {n} (x, y, A _ {i}) & \text { if   } A _ {i} \text {   is   numeric } \end{array} \right.\tag{1}
$$

where x and y are two patterns described by the attribute set $A =$ $\{ A _ { 1 } , . . . , A _ { m } \}$ . If there exist a missing value, it will be denoted as $\because$

With this definition, it can be seen that both categorical and numerical data will be treated independently, without the need to encode some data type in a specific dataset. After this brief operation to treat the categorical and numerical attributes, MIDSO proceeds to calculate the similarity of attribute values. For categorical attributes, the similarity between values is

$$
s _ {c} (x, y, A _ {i}) = \left\{ \begin{array}{l l} 0 & \text { if } \left((x _ {i} \neq y _ {i}) \vee \left(x _ {i} = ^ {\prime}? ^ {\prime}\right) \vee \left(y _ {i} = ^ {\prime}? ^ {\prime}\right)\right) \\ & 1 \quad \text { in   other   case } \end{array} \right.\tag{2}
$$

The similarity will be equal to zero if the attribute values of the two patterns are different, or if at least one of the pattern has a missing value. Otherwise, the similarity will be equal to one.

For numeric attributes, the similarity between attribute values is computed as follows:

$$
s _ {n} (x, y, A _ {i}) = \left\{ \begin{array}{c c} 0 & \text { if } \left((| x _ {i} - y _ {i} | > \sigma_ {i}) \vee \left(x _ {i} = ^ {\prime}? ^ {\prime}\right) \vee \left(y _ {i} = ^ {\prime}? ^ {\prime}\right)\right) \\ 1 & \text { in   other   case } \end{array} \right.\tag{3}
$$

As shown, for comparing numeric values, the standard deviation $\sigma _ { i }$ of the attribute A is consider in order to determine if two values are similar or not. That is, an absolute value of the difference between attribute values lower than standard deviation will result in a similarity outcome of one. The standard deviation of a numeric attribute is computed regardless the patterns having missing values in that attribute. Let w<sub>i</sub> be the weight of the $A _ { i }$ attribute, and let m be the total number of attributes. The overall similarity between two patterns $x , y \in U { \mathrm { i s } } s ^ { t } ,$ , where s means “similarity”, and the superscript t of s means “total”:

$$
s ^ {t} (x, y) = \sum_ {i = 1} ^ {m} w _ {i} * M I D S O (x, y, A _ {i})\tag{4}
$$

The NAC classifier has two phases: training and classification. For training, it assumes the following: There is a training set T, composed by labeled patterns, which are described by means of an attribute set $A = \{ A _ { 1 } , . . . , A _ { m } \}$ . The patterns belongs only to one of the classes or labels $K = \{ K _ { 1 } , . . . , K _ { p } \}$ , and the attribute set A has associated a set of attribute weights $w = \{ w _ { 1 } , . . . , w _ { m } \}$ . Finally, it should be emphasized that an attribute must not contain missing values for each and every one of the patterns of the dataset, as well as the patterns of the training set should not have values lost in each of its attributes.

Once these assumptions are fulfilled, we can go to the training phase of NAC, which consists of two steps: Store the training set T, and then the algorithm calculates maximum max , minimum min , and standard deviation $\sigma _ { i } ,$ for each of the numerical attributes $A _ { i } ,$ which are then stored. The decision-making (or classification) phase of NAC is carried out in two operations. The first operation consists in calculating the average similarity of the pattern to classify with respect to each of the classes. Let $T _ { j }$ be the set of patterns belonging to the class $K _ { j } .$ The average similarity of an object to the class $K _ { j }$ is given by:

$$
s _ {j} (o) = \frac {1}{| T _ {j} |} \sum_ {y \in T _ {j}} s ^ {t} (o, y)\tag{5}
$$

As can be seen, this classification model is easy to interpret, because there are very few operations carried out to obtain the classification. In summary, it assigns to the pattern to classify, the class that presents the maximum similarity, which is given by MIDSO. Finally, it should be mentioned that the correct adjustment of the weights associated with the dataset attributes could improve the performance of the NAC classifier. This is due to each of these weights represents how significant each attribute is to perform the classification task, so that an attribute will be more representative to discriminate between one class or another if its value is close to or equal to one, while it will be less significant if its value is close to or equal to zero.

## 4. Proposed methodology for financial feature weighting

## 4.1. Overview

The proposed methodology (Fig. 1) consists of two phases. In the first, the attribute weights of the datasets are computed by means of a metaheuristic algorithm. The second phase consists of the application of the NAC classifier using the weights obtained in the previous phase.

In the first phase of the methodology, the metaheuristic algorithm will be applied ten times, independently. Each time, the algorithm will return the best individual (feature weights) obtained, according to a certain fitness function. Previous experiments show that ten iterations are sufficient to obtain good results [26]. At the end of the 10 executions, the best set of feature weights will be consider for be included in the NAC classifier, and then it will be used in the decision-making process. The second phase of the methodology consist on applying the NAC classifier, using as feature weights the best set obtained in the previous phase (Fig. 2). Then, the dataset will be divided by means of stratified 5-fold cross validation as suggested in [27], and the performance of NAC classifier in the decision-making process is computed.

By means of the proposed methodology, we intended to improve the knowledge based system in a financial Decision Support System. We hypothesize that automatic feature weight computation leads to an improvement in the decision-making process, and therefore, we will obtain a better knowledge representation, leading to better decisions.

![](/api/attachments/REMFDNX6/fulltext/images/67df917ce9336b3b12fd0c068de85aeea381dbbaea9e4189db9e0efd00dd8e73.jpg)  
Fig. 1. General diagram of the proposed methodology

In the following, we will explain some aspects for the metaheuristic functioning in the proposed methodology, such as the codification of solutions (Section 4.2) and the fitness function used (Section 4.3).

## 4.2. Codification of solutions

To apply metaheuristic algorithms, it is needed to codify the problem solutions. For this, we use a vector of length equal to the number of attributes, having components in the [0,1] interval.

The components of the vector represent the corresponding feature weights, that is, the number between the [0,1] interval in the ith component corresponds to the importance (weight) of the ith feature. Fig. 3 shows and example of the codification of an individual for an attribute set of five features.

## 4.3. Fitness function

To evaluate the suitability of each solution it is necessary to establish an objective function. We use the classification performance obtained by NAC measured as the Area under the ROC Curve (AUC) [28]. AUC has been used to obtain classifier performance in several scenarios. In [28] it is used to quantify the performance of classifier committees for unbalanced learning, while in [29] was used to determine if there is a performance improvement working with imbalanced classes.

This performance metric was selected due to the class imbalance present in most datasets belonging to the financial environment, since this metric is independent of the class distribution of the dataset [13,27,30]. AUC computation is based directly on the Confusion Matrix, which is described in Table 1. This matrix classifies the different cases that can be presented when performing the classification task for a two-class problem.

As can be seen in Table 1, the cases called True Positive (VP) are those instances that the classifier labeled positive and are actually positive. False Positives (FP) occur when the classifier assigns the negative label to an instance that it was actually positive; a False Negative (FN), is an instance that was classified as positive when in reality belongs to the negative class. Finally, the True Negatives (VN) happen when negative instances are correctly classified as negative.

![](/api/attachments/REMFDNX6/fulltext/images/7568a5073163048ec309cbef8cd3e3fcd34c9d11e33606d05589f68b137c2a7d.jpg)  
Fig. 2. High-level architecture of a Decision Support System with the proposed methodology

It has been proven by Sokolova et al. [31] that the Area under the ROC curve for a discrete classifier can be computed as the average of True Positive Rate and True Negative Rate.

$$
\mathrm{AUC} = \frac {\mathrm{TPR} + \mathrm{TNR}}{2} \text {where TPR} = \frac {\mathrm{TP}}{\mathrm{TP} + \mathrm{FN}} \text {and TNR} = \frac {\mathrm{TN}}{\mathrm{FP} + \mathrm{TN}}\tag{6}
$$

Thus, the individuals in the metaheuristic algorithms will be compared by considering their fitness, that is, each candidate feature weights vector will have associated the AUC obtained by the NAC classifier using those weights. However, to obtain an accurate estimation of the classifier performance, it is needed to sample the dataset in order to obtain both training and testing sets.

The sampling method selected to generate such sets was Distribution optimally balanced Stratified Cross-Validation with five folds (Dob-SCV), which was proposed in [27], since it helps to make a better distribution of the patterns between the different partitions that it generates, reducing the problem of class imbalance in the training of decision-making models.

To perform the sampling, the Dob-SCV algorithm generates k partitions, where k is a user-defined positive integer (we used k = 5 as suggested in [27]). The procedure for assigning the patterns to each of these partitions is performed for each K classes contained in the dataset. For each class, a random instance is selected and assigned to the first partition. Then, the k − 1 nearest neighbors of the instance are computed, and assigned to the respective partitions.

<table><tr><td>0.23</td><td>0.18</td><td>0.86</td><td>0.95</td><td>1.00</td></tr></table>

Fig. 3. Example of the codi cation of an individual, for a problem having ve attributes.

It should be mentioned that the dissimilarity function used in the proposed methodology to find the neighbors considers the total similarity s<sup>t</sup> used by the NAC model [3], and is represented in the following expression, where m is the number of attributes of the dataset and $s ^ { t } ( x , y )$ is the total similarity between the instances x and y (Eq. (4)).

$$
d i s s (x, y) = m - s ^ {t} (x, y)\tag{7}
$$

Thus, in the proposed methodology, the fitness function of an individual is computed as the average AUC obtained in the k iterations of Dob-SCV procedure.

## 5. Results and discussion

## 5.1. Datasets

In order to evaluate the proposed methodology, different datasets belonging to the financial field were used (Table 2). They were obtained from the Machine Learning repository of the University of California at Irvine [32]. The datasets correspond to credits risk, bankruptcy prediction, banknote authentication and bank telemarketing. As can be seen in Table 2, all the datasets used have only two classes. As for the imbalance ratio, it can be observed that in at least six cases, this value is higher than 1.5, which is an established threshold [33], so that six of the 10 databases have imbalanced classes.

Confusion matrix for a two-class classification problem.

<table><tr><td></td><td>Classified as positive</td><td>Classified as negative</td></tr><tr><td>Positive instances</td><td>True Positive (TP)</td><td>False Negative (FN)</td></tr><tr><td>Negative instances</td><td>False Positive (FP)</td><td>True Negative (TN)</td></tr></table>

Description of the datasets used.

<table><tr><td>Datasets</td><td>Instances</td><td>Attributes</td><td>Missing values</td><td>Imbalance ratio</td></tr><tr><td>Bank</td><td>4521</td><td>16</td><td>No</td><td>7.677</td></tr><tr><td>Bank-additional</td><td>4119</td><td>20</td><td>No</td><td>7.956</td></tr><tr><td>Bank-additional-full</td><td>41,188</td><td>20</td><td>No</td><td>7.876</td></tr><tr><td>Bank-full</td><td>45,211</td><td>16</td><td>No</td><td>7.548</td></tr><tr><td>Banknote</td><td>1372</td><td>4</td><td>No</td><td>1.249</td></tr><tr><td>Bankruptcy</td><td>250</td><td>6</td><td>No</td><td>1.336</td></tr><tr><td>Credit-approval</td><td>690</td><td>15</td><td>Yes</td><td>1.247</td></tr><tr><td>Credit-Australian</td><td>690</td><td>15</td><td>Yes</td><td>1.247</td></tr><tr><td>Credit-German</td><td>1000</td><td>20</td><td>No</td><td>2.333</td></tr><tr><td>Default-credit</td><td>30,000</td><td>24</td><td>No</td><td>3.520</td></tr></table>

This is an important phenomenon to consider, since imbalanced datasets can generate a learning with tendency to the majority class, which could produce erroneous interpretations of the obtained results [33].

## 5.2. Parameter configuration and metaheuristics used

In order to test the proposed methodology, we selected three metaheuristic algorithms: Differential Evolution (DE) [7], Genetic Algorithms (GA) [8] and Novel Bat Algorithm (NBA) [9]. DE and GA have been successfully applied for feature weighting, and NBA is a recently proposed metaheuristic achieving good experimental results [9].

We used the same codification and fitness function for the three tested metaheuristics, and we defined a population number of 50 individuals. In addition, we set as stopping criterion the reach of a maximum number of fitness evaluation, defined as 10,000. Additional parameters of the metaheuristics are given in Table 3. According to the methodology, at phase 1, each metaheuristic was applied 10 times (in independent executions), and the best individual obtained was selected for the second phase. All metaheuristic algorithm tried to solve the same problem: to maximize the AUC metric for the NAC classifier using Dob-SCV sampling (Section 4.3). Then, the NAC classifier was evaluated on phase 2, according to the AUC metric computed in the decision-making process. In the next section, we detailed the results obtained.

Additional parameters in the metaheuristic tested.

<table><tr><td>Metaheuristic</td><td>Parameter values</td></tr><tr><td>Differential Evolution</td><td> $F = 0.5$ , crossover rate  $CR = 1.0$ </td></tr><tr><td>Genetic Algorithm</td><td>Mutation probability  $mp = 0.05$ Crossover probability  $cp = 1.0$ Crossover operator:  $blx_{\alpha}$  crossover [34]Parent selection strategy: binary tournamentReplacement strategy: elitist</td></tr><tr><td>Novel Bat Algorithm(Suggested values from author&#x27;s implementation [35])</td><td> $\gamma = 0.9, \alpha = 0.99, G = 10$  $freqDMax = 1.5, freqDMin = 0$  $AMax = 2, AMin = 1$  $probMax = 0.9, probMin = 0.6$  $\tau Max = 1, \tau Min = 0.5$  $wMax = 0.9, wMin = 0.5$  $CMax = 0.9, CMin = 0.1$ </td></tr></table>

## 5.3. Results

The results obtained by applying the proposed methodology to the different datasets belonging to the financial environment are shown below. Section 5.3.1 shows the AUC results obtained by the different metaheuristics while computing feature weights, as well as the execution time obtained in each case. Section 5.3.2 shows the AUC of the decision-making made by NAC classifier using each of the best individuals of each of the three metaheuristics. This section also presents a comparison of the results obtained with respect to the classifiers NAC had no significant differences in previous experiments.

5.3.1. Results obtained in the phase 1 of the proposed methodology, by the tested metaheuristics

Table 4 shows the results of the AUC corresponding to the best individual (Best), the averaged AUC obtained in the 10 independent executions (Avg), and the standard deviation obtained (Stdev).

It can be observed that the best results were obtained with Differential Evolution (DE), since it always obtained the best individual. Genetic Algorithm (GA) metaheuristics only obtained the best for four datasets (in all of them was a tie with DE), while Novel Bat Algorithm (NBA) algorithm tied on three datasets together with DE. All of the three metaheuristic showed low standard deviations (about 0.01), which is considered as a very good results. These low standard deviations suggest that the three algorithms converged appropriately in the 10 independent executions.

Table 5 shows the average execution costs in seconds of each one of the metaheuristics with each one of the different datasets used in this work. At first glance, it is possible to see that the worst average times of execution were obtained with NBA with a great difference with respect to the other two metaheuristics. It is also easy to see that GA and DE obtained the best execution times. In a deeper analysis of the results, it can be seen that the datasets where the GA obtained better execution times were the biggest ones, containing N4000 patterns.

In addition, the proposed methodology gives the feature weights computed by the metaheuristic algorithms. This information could be very useful in the decision-making process. Table 6 shows the average weights obtained by the best individuals, using DE, for each of the financial datasets used. Instead of applying the widely used threshold of 0.5, we decide to allow a margin between 0.4 and 0.6 to analyze attribute importance.

For instance, on the bank and bank-full datasets, there is a coincidence in assigning low weights (w ≤ 0.4) to the attributes age, pdays, previous and poutcome. Therefore, those attributes are not important for classification. On the other hand, attribute loan, contact and duration have high weights (w ≥ 0.6), and are considered important for the decision-making process. For bank-additional and bank-additional-full datasets, the methodology gives high importance to the attributes month, duration and nr.employed

Results of the fitness (AuC) of the individuals in the metaheuristic tested. Best results in bold,

<table><tr><td rowspan="2">Datasets</td><td colspan="3">DE</td><td colspan="3">GA</td><td colspan="3">NBA</td></tr><tr><td>Best</td><td>Avg.</td><td>Stdev</td><td>Best</td><td>Avg.</td><td>Stdev</td><td>Best</td><td>Avg.</td><td>Stdev</td></tr><tr><td>Bank</td><td>0.76</td><td>0.76</td><td>0.01</td><td>0.75</td><td>0.75</td><td>0.00</td><td>0.75</td><td>0.74</td><td>0.01</td></tr><tr><td>Bank-additional</td><td>0.80</td><td>0.79</td><td>0.01</td><td>0.78</td><td>0.77</td><td>0.00</td><td>0.76</td><td>0.75</td><td>0.01</td></tr><tr><td>Bank-additional-full</td><td>0.76</td><td>0.75</td><td>0.01</td><td>0.75</td><td>0.72</td><td>0.02</td><td>0.76</td><td>0.75</td><td>0.01</td></tr><tr><td>Bank-full</td><td>0.74</td><td>0.73</td><td>0.01</td><td>0.71</td><td>0.68</td><td>0.03</td><td>0.74</td><td>0.72</td><td>0.01</td></tr><tr><td>Banknote</td><td>0.89</td><td>0.89</td><td>0.00</td><td>0.89</td><td>0.88</td><td>0.00</td><td>0.88</td><td>0.88</td><td>0.01</td></tr><tr><td>Bankruptcy</td><td>1.00</td><td>1.00</td><td>0.00</td><td>1.00</td><td>1.00</td><td>0.00</td><td>1.00</td><td>0.99</td><td>0.01</td></tr><tr><td>Credit-approval</td><td>0.88</td><td>0.88</td><td>0.00</td><td>0.88</td><td>0.87</td><td>0.00</td><td>0.87</td><td>0.86</td><td>0.01</td></tr><tr><td>Credit-Australian</td><td>0.88</td><td>0.88</td><td>0.00</td><td>0.87</td><td>0.87</td><td>0.00</td><td>0.87</td><td>0.87</td><td>0.00</td></tr><tr><td>Credit-German</td><td>0.74</td><td>0.73</td><td>0.00</td><td>0.74</td><td>0.73</td><td>0.00</td><td>0.72</td><td>0.71</td><td>0.01</td></tr><tr><td>Default-credit</td><td>0.69</td><td>0.69</td><td>0.00</td><td>0.69</td><td>0.66</td><td>0.02</td><td>0.68</td><td>0.66</td><td>0.01</td></tr></table>

Table 5  
Execution time (in seconds) obtained by the metaheuristic algorithms tested. Best results in bold.

<table><tr><td>Datasets</td><td>DE</td><td>GA</td><td>NBA</td></tr><tr><td>Bank</td><td>44,172.88</td><td>42,362.75</td><td>1,937,832.65</td></tr><tr><td>Bank-additional</td><td>43,989.39</td><td>42,534.79</td><td>1,927,796.79</td></tr><tr><td>Bank-additional-full</td><td>100,963.99</td><td>39,640.86</td><td>444,556.30</td></tr><tr><td>Bank-full</td><td>100,608.20</td><td>39,377.14</td><td>441,644.94</td></tr><tr><td>Banknote</td><td>1489.85</td><td>1569.98</td><td>62,035.11</td></tr><tr><td>Bankruptcy</td><td>59.50</td><td>63.50</td><td>2495.35</td></tr><tr><td>Credit-approval</td><td>1069.56</td><td>1142.67</td><td>45,115.90</td></tr><tr><td>Credit-Australian</td><td>769.74</td><td>769.88</td><td>35,872.31</td></tr><tr><td>Credit-German</td><td>2097.96</td><td>3091.68</td><td>118,300.42</td></tr><tr><td>Default-credit</td><td>65,520.66</td><td>24,707.06</td><td>278,848.86</td></tr></table>

In the banknote datasets, attributes Skewness of Wavelet Transformed image and Kurtosis of Wavelet Transformed image are very important, while attribute Entropy of image may be discarded. Similarly, in the bankruptcy dataset, the fifth attribute obtain high importance, while attributes Industrial Risk and Operating Risk have medium importance $( 0 . 4 < w _ { i } < 0 . 6 )$ ).

Both credit-approval and credit-Australian datasets obtained low weights for attributes Age, Married and CreditScore, while features EducationLevel and PriorDefault had high importance. For the dataset credit-German, attributes checking\_status, duration, purpose, savings\_status, property\_magnitude, age and own\_telephone are very important, while features employment, housing and existing\_credits are not.

The results of the automatic feature weigh computation for the default-credit dataset consider that attributes Repayment status in September 2005, Repayment status in June 2005, Amount of bill statement in September 2005 and Amount of previous payment in July 2005, are useful for decision-making, while attributes Repayment status in August 2005, Repayment status in July 2005, Repayment status in May 2005 and Repayment status in April 2005 appear to be useless. For the above, it can be said that the best performance was obtained with the NAC classifier in conjunction with DE to automatically generate the weights corresponding to each dataset.

It is also possible to appreciate that the performance of the NAC was improved with each of the metaheuristics. In order to confirm the above and to determine if there is a significant difference between the performances of the different algorithms, a statistical analysis was performed. This analysis is given in the next section.

Table 6  
Averaged feature weights obtained by the best individuals in the methodology, using DE.

<table><tr><td>Dataset</td><td>Feature weights</td></tr><tr><td>Bank</td><td>{0.31, 0.42, 0.23, 0.45, 0.46, 0.38, 0.55, 0.81, 0.90, 0.64, 0.28, 0.89, 0.78, 0.33, 0.06, 0.06}</td></tr><tr><td>Bank-additional</td><td>{0.67, 0.61, 0.29, 0.54, 0.80, 0.26, 0.60, 0.51, 0.66, 0.29, 0.88, 0.29, 0.51, 0.01, 0.09, 0.27, 0.11, 0.60, 0.33, 0.69}</td></tr><tr><td>Bank-additional-full</td><td>{0.30, 0.50, 0.42, 0.57, 0.40, 0.65, 0.56, 0.43, 0.67, 0.29, 0.74, 0.38, 0.42, 0.44, 0.46, 0.27, 0.43, 0.38, 0.49, 0.63}</td></tr><tr><td>Bank-full</td><td>{0.35, 0.55, 0.50, 0.45, 0.48, 0.48, 0.54, 0.60, 0.82, 0.25, 0.66, 0.71, 0.34, 0.26, 0.29, 0.30}</td></tr><tr><td>Banknote</td><td>{0.55, 0.91, 0.94, 0.11}</td></tr><tr><td>Bankruptcy</td><td>{0.55, 0.09, 0.32, 0.37, 0.94, 0.54}</td></tr><tr><td>Credit-approval</td><td>{0.67, 0.11, 0.51, 0.25, 0.39, 0.90, 0.58, 0.67, 0.89, 0.44, 0.37, 0.45, 0.42, 0.26, 0.60}</td></tr><tr><td>Credit-Australian</td><td>{0.55, 0.05, 0.51, 0.33, 0.50, 0.80, 0.74, 0.54, 0.92, 0.71, 0.34, 0.29, 0.27, 0.42, 0.52}</td></tr><tr><td>Credit-German</td><td>{0.96, 0.98, 0.59, 0.94, 0.56, 0.96, 0.35, 0.55, 0.71, 0.53, 0.55, 0.88, 0.65, 0.51, 0.22, 0.36, 0.53, 0.41, 0.68, 0.48}</td></tr><tr><td>Default-credit</td><td>{0.44, 0.48, 0.44, 0.42, 0.51, 0.44, 0.86, 0.32, 0.27, 0.60, 0.21, 0.04, 0.65, 0.59, 0.49, 0.56, 0.54, 0.50, 0.40, 0.52, 0.64, 0.50, 0.54, 0.50}</td></tr></table>

Table 7  
AUC results obtained by the tested decision-makers. Best results in bold.

<table><tr><td>Datasets</td><td>C4.5</td><td>NB</td><td>NAC</td><td>NAC DE</td><td>NAC GA</td><td>NAC NBA</td></tr><tr><td>Bank</td><td>65.97</td><td>70.75</td><td>67.51</td><td>75.04</td><td>75.37</td><td>73.64</td></tr><tr><td>Bank-additional</td><td>69.62</td><td>75.65</td><td>75.61</td><td>80.45</td><td>77.61</td><td>76.36</td></tr><tr><td>Bank-additional-full</td><td>74.64</td><td>75.55</td><td>74.26</td><td>76.25</td><td>75.30</td><td>75.61</td></tr><tr><td>Bank-full</td><td>72.46</td><td>72.55</td><td>70.35</td><td>74.95</td><td>71.20</td><td>74.20</td></tr><tr><td>Banknote</td><td>98.60</td><td>83.50</td><td>85.87</td><td>88.35</td><td>88.29</td><td>88.21</td></tr><tr><td>Bankruptcy</td><td>97.75</td><td>99.20</td><td>99.72</td><td>100.00</td><td>100.00</td><td>100.00</td></tr><tr><td>Credit-approval</td><td>85.30</td><td>76.10</td><td>84.47</td><td>86.47</td><td>86.93</td><td>87.01</td></tr><tr><td>Credit-Australian</td><td>85.30</td><td>76.10</td><td>84.58</td><td>86.82</td><td>86.57</td><td>86.81</td></tr><tr><td>Credit-German</td><td>65.40</td><td>67.85</td><td>69.90</td><td>70.65</td><td>72.20</td><td>72.25</td></tr><tr><td>Default-credit</td><td>63.91</td><td>68.80</td><td>66.01</td><td>69.14</td><td>69.00</td><td>68.01</td></tr><tr><td>Times best</td><td>0</td><td>0</td><td>0</td><td>6</td><td>2</td><td>3</td></tr></table>

## 5.3.2. AUC results obtained in phase 2 by the tested decision-makers

In Table 7, we can see the decision-making results obtained by each of the classification models included in the experiments, as well as the results obtained by the NAC classifier without weights and using the weights generated in phase 1 of the proposed methodology, with the different metaheuristics. Columns NAC DE, NAC GA and NAC NBA show the AUC results of NAC classifier using the weights computed by DE, Genetic Algorithm and Novel Bat Algorithm, respectively.

The results obtained in [16] were taken into account in our experiments. In those results, the performance of the NAC was significantly better than the models RIPPER, MLP, SMO and 1NN, so we discarded those models, and only C4.5 and Naïve Bayes (NB) were considered in our experiments, due to they do not had significant difference in performance with respect to NAC in the experiments of [16].

The AUC results given in Table 6 show that the best performances were obtained with the NAC classifier using the weights generated by the different metaheuristics. Among them, DE obtained the best AUC in six datasets, while NBA obtained the best results for three datasets, and GA only in two datasets.

## 5.4. Discussion: statistical analysis

The Friedman test was developed by Milton Friedman [36,37] and is a nonparametric test, so it does not depend on a probability distribution, and it will allow to determine, if there is or not, a significant difference between the performances obtained with the different classifiers and, specifically, with the different metaheuristics. This test orders each of the algorithms according to statistical measures, and then it is possible to perform a post hoc comparison with which it is possible to determine between which of the algorithms compared in the Friedman test there is difference.

This test assigns to each of the elements to be compared, a probability value p that measures the evidence against null hypotheses. If the pvalue is less than an established level of significance (usually 0.05), then we can reject the idea that the difference between the elements of the comparison is due to random sampling, and we conclude that there is a difference between the elements that are being compared. On the other hand, if the value of p is greater than the established level of significance, it is said that there is no evidence to determine the existence of a difference. In our experiments, the tests were performed using the AUC of each of the classification models with the different datasets.

In order to carry out the Friedman tests, we used the KEEL software [33]. In the Friedman test, there are two hypotheses to determine whether there is a statistically significant difference among the algorithms compared. The first one is the Null hypothesis (h0), which states that there are no differences; and the second, called Alternative hypothesis (h1), indicates the existence of differences. Thus, if p N 0.05, we do not reject the null hypothesis (h0), and consider that there are no significant differences. On the other hand, if $p \leq 0 . 0 5$ , we reject the null hypothesis and state that there are significant differences among the algorithms.

Rankings of the Friedman test comparing the proposed methodology using DE with respect to other decision-makers, and Post Hoc comparison of the best-ranked model (NAC DE) with respect other decision-makers.

<table><tr><td colspan="2">Friedman test</td><td colspan="3">Post hoc test</td></tr><tr><td>Algorithms</td><td>Ranking</td><td>Algorithms</td><td>Unadjusted probability</td><td>p-Holm</td></tr><tr><td>NAC DE</td><td>1.1</td><td>NB</td><td>0.003235</td><td>0.050000</td></tr><tr><td>NB</td><td>2.8</td><td>NAC</td><td>0.000999</td><td>0.025000</td></tr><tr><td>NAC</td><td>3.0</td><td>C4.5</td><td>0.000532</td><td>0.016667</td></tr><tr><td>C4.5</td><td>3.1</td><td colspan="3">Hypothesis with p - Holm ≤ 0.05 are rejected</td></tr></table>

If the test found a significant difference, then we proceed to the application of a post hoc comparison test. The post hoc tests compare the best-ranked algorithm according to the Friedman test, with respect to the other algorithms. Then, because of these comparisons, the significant differences are detected.

We used the Holm post hoc test [38]. For this test, the null hypothesis is rejected if the probability value obtained for the test is lower than a threshold value. We again used the KEEL software [33] for computing the Holm test. Table 8 shows the average ranking obtained after applying the Friedman test to the AUC results obtained with NAC, NAC with DE, C4.5 and NB. As can be observed, the best performance was obtained by the NAC using the weights generated with the proposed methodology, by using the DE metaheuristic. Once the best classification model was determined (Table 8), it shows the results of a post-Hoc comparison, with which it is possible to identify if there is a difference between the best algorithm (NAC with DE) against the other models. In this case, these hypotheses were rejected with p − Holm ≤ 0.05, so there is a difference between NAC using the weights obtained by DE against the other models.

In Table 9, we present the average rankings of the algorithms obtained with the Friedman test, comparing the previously selected models and the NAC classifier using the feature weights obtained by GA. As can be seen, the best performance was obtained by using the proposed methodology. The Post Hoc comparison is also shown, with the objective of determining if there is a significant difference between the performance of the weightless NAC and the NAC using weights obtained by GA. The hypotheses with p − Holm ≤ 0.05 were rejected, so there is a significant difference between the performance of the NAC with GA against the NAC without weights and the other models.

The average rankings of the selected models, the NAC without weights and the NAC using NBA, are shown in Table 10, and as can be observed, the best performance was obtained by the NAC using the weights obtained by the NBA metaheuristic. Table 10 also shows the post Hoc comparison, in which it can be observed that there is a difference between the performance of the NAC algorithm using the feature weights computed by the proposed methodology with NBA against the NAC without weights and the other two classification models. All null hypotheses are rejected, due to p − Holm ≤ 0.05.

In all cases, we can establish that the proposed methodology for automatic calculation of attribute weights, using metaheuristic algorithms, led to an improvement in the performance of the NAC classifier,

## Table 9

Rankings of the Friedman test comparing the proposed methodology using GA with respect to other decision-makers, and Post Hoc comparison of the best-ranked model (NAC GA) with respect other decision-makers.

<table><tr><td colspan="2">Friedman test</td><td colspan="3">Post hoc test</td></tr><tr><td>Algorithms</td><td>Ranking</td><td>Algorithms</td><td>Unadjusted probability</td><td>p-Holm</td></tr><tr><td>NAC GA</td><td>1.4</td><td>NB</td><td>0.037667</td><td>0.050000</td></tr><tr><td>NB</td><td>2.6</td><td>NAC</td><td>0.005584</td><td>0.025000</td></tr><tr><td>NAC</td><td>3.0</td><td>C4.5</td><td>0.005584</td><td>0.016667</td></tr><tr><td>C4.5</td><td>3.0</td><td colspan="3">Hypothesis with p - Holm ≤ 0.05 are rejected</td></tr></table>

Rankings of the Friedman test comparing the proposed methodology using NBA with respect to other decision-makers, and Post Hoc comparison of the best-ranked model (NAC NBA) with respect other decision-makers.

<table><tr><td colspan="2">friedman test</td><td colspan="3">Post hoc test</td></tr><tr><td>Algorithms</td><td>Ranking</td><td>Algorithms</td><td>Unadjusted probability</td><td>p-Holm</td></tr><tr><td>NAC NBA</td><td>1.2</td><td>NB</td><td>0.009375</td><td>0.050000</td></tr><tr><td>NB</td><td>2.7</td><td>NAC</td><td>0.001823</td><td>0.025000</td></tr><tr><td>NAC</td><td>3.0</td><td>C4.5</td><td>0.000999</td><td>0.016667</td></tr><tr><td>C4.5</td><td>3.1</td><td colspan="3">Hypothesis with p - Holm ≤ 0.05 are rejected</td></tr></table>

obtaining in all cases a significant enhancement in the decision-making process. These results support the hypothesis of this research, and allow us to establish that it is possible to increase the performance of DSS in the financial field, through the proposed methodology for the automatic obtaining of weights of the attributes.

After obtaining these results, another test was performed to determine if any of the tested metaheuristics exceeded the others in terms of the performance of the NAC classifier in the decision-making process. For this, we compared the results obtained in the second phase of the proposed methodology, using the weights obtained by DE, Genetic Algorithms and Novel Bat Algorithm. These results are given in Table 11.

Table 11 shows the average rankings of the performances obtained with NAC using the weights calculated with the different metaheuristics, and as it can be observed, the best performance was obtained by NAC using DE. In addition, it shows the post Hoc comparative; the test indicated that hypotheses should be rejected with a p − Holm ≤ 0.025 value. That is, the NAC GA hypothesis is rejected.

With the above results, it is possible to state that the decision-making of the NAC model was improved by the automatic computation of the attribute weights, using the three metaheuristics. Then, with the test to compare the performances of the three metaheuristics, it was possible to determine that there is no difference between the results obtained with DE and NBA, but there is a significant difference with respect to Genetic Algorithms, that is, GA obtained the worst performance.

Considering the execution cost of the methodology by using the different metaheuristics, we carried out a statistical analysis of the execution times. DE obtained the best result, being the first in the Friedman ranking (Table 12).

The post-Hoc comparison between the execution times of DE versus the other two metaheuristics indicated that hypotheses should be rejected with a p − Holm ≤ 0.05, so that the two hypotheses were rejected, i.e. there is a difference in the execution time of DE versus GA and NBA. Thus, the time expended by DE was significantly lower.

As can be seen in the statistical analysis carried out, although between DE and NBA there was no difference in the classification performance obtained with the weights generated with these metaheuristics, there was a significant difference in execution time, so it can be considered that the best metaheuristic to perform the weight adjustment using the proposed methodology was DE.

## 6. Conclusions

In this research, a methodology was proposed to automatically perform the adjustment of attribute weights in financial data sets, and to

## Table 11

Rankings of the Friedman test comparing the proposed methodology using the three tested metaheuristics, and Post Hoc comparison of the best-ranked model (NAC NBA) with respect other metaheuristics.

<table><tr><td colspan="2">Friedman test</td><td colspan="3">Post hoc test</td></tr><tr><td>Algorithms</td><td>Ranking</td><td>Algorithms</td><td>Unadjusted probability</td><td>p-Holm</td></tr><tr><td>NAC DE</td><td>1.6</td><td>NAC NBA</td><td>0.179712</td><td>0.050</td></tr><tr><td>NAC NBA</td><td>2.2</td><td>NAC GA</td><td>0.179712</td><td>0.025</td></tr><tr><td>NAC GA</td><td>2.2</td><td colspan="3">Hypothesis with p - Holm ≤ 0.025 are rejected</td></tr></table>

Table 12  
Rankings of the Friedman test comparing the execution time of proposed methodology using the three tested metaheuristics, and Post Hoc comparison of the fastest model (DE) with respect other metaheuristics.

<table><tr><td colspan="2">Friedman test</td><td colspan="3">Post hoc test</td></tr><tr><td>Algorithms</td><td>Ranking</td><td>Algorithms</td><td>Unadjusted probability</td><td>p-Holm</td></tr><tr><td>DE</td><td>1.5</td><td>GA</td><td>0.179712</td><td>0.050</td></tr><tr><td>GA</td><td>1.5</td><td>NBA</td><td>0.179712</td><td>0.025</td></tr><tr><td>NBA</td><td>3.0</td><td colspan="3">Hypothesis with p - Holm ≤ 0.05 are rejected</td></tr></table>

improve the decision-making process in this area. As can be seen in the results obtained, the performance of the NAC was improved with the weights generated by the three metaheuristics used (DE, Genetic Algorithm and Novel Bat Algorithm), by determining that there is a significant difference in their performances through the Friedman test. This test stipulated that there is no difference between the performance of NAC using weights obtained by DE and Novel Bat Algorithm, but there is a difference with the performance of NAC with Genetic Algorithm, so that, in terms of performance, the best algorithms to generate the weights were DE and Novel Bat Algorithm. Finally, regarding the execution times for the generation of the weights of each of these algorithms, there was a difference between the three metaheuristic according to the results of the Friedman test, being DE the algorithm with the lowest time. Therefore, DE offers a good trade-off between decision-making performance and computational cost.

One of the key limitation of the proposed methodology is that we only tested three metaheuristics, while in the state of art have been proposed more than a thousand. This draws some directions of future works, due to the researchers may select the desired metaheuristic and applied within the proposed methodology, for automatically perform the adjustment of attribute weights in financial data sets.

## Acknowledgements

The authors would like to thank the Instituto Politécnico Nacional (Secretaría Académica, COFAA, SIP, CIDETEC, and CIC), the CONACYT, and SNI for their economic support to develop this work.

## References

[1] D. Murphy, Understanding Risk: The Theory and Practice of Financial Risk Management, Chapman & Hall/CRC, FL, USA, 2008.

[2] F.J.P. García, Financial Risk Management: Identification, Measurement and Management, Springer N, Palgrave Macmillan, Switzerland, 2017.

[3] Y. Villuendas-Rey, C.F. Rey-Benguría, Á. Ferreira-Santiago, O. Camacho-Nieto, C. Yáñez-Márquez. The Naïve Associative Classifier (NAC): a novel. simple, transparent, and accurate classification model evaluated on financial data, Neurocomputing 265 (2017) 105–115, https://doi.org/10.1016/j.neucom.2017.03.085.

[4] R. Apostolik, C. Donohue, Foundations of Financial Risk: An Overview of Financial Risk and Risk-based Financial Regulation, John Wiley & Sons, NJ, USA, 2015.

[5] D. Shirreff, Dealing with Financial Risk, Profile Books Ltd, London, UK, 2008.

[6] F. Burstein, C.W. Holsapple (Eds.), Handbook on Decision Support Systems, Springer-Verlag, Berlin, Germany, 2008

[7] R. Storn, K. Price, Differential evolution - a simple and efficient heuristic for global optimization over continuous spaces, Journal of Global Optimization 11 (1997) 341–359, https://doi.org/10.1023/A:1008202821328.

[8] K. Sastry, D. Goldberg, G. Kendall, Genetic algorithms, in: E.K. Burke, G. Kendall (Eds.), Search Methodol. Introd. Tutorials Optim. Decis. Support Tech, Springer US, Boston, MA 2005, pp. 97–125, https://doi.org/10.1007/0-387-28356-0\_4.

[9] X.-B. Meng, X.Z. Gao, Y. Liu, H. Zhang, A novel bat algorithm with habitat selection and Doppler effect in echoes for optimization, Expert Systems with Applications 42 (2015) 6350–6364 https://doiorg/10.1016/i eswa 2015.04.026

[10] A. Petropoulos, S.P. Chatzis, S. Xanthopoulos, A novel corporate credit rating system based on Student's-t hidden Markoy models Expert Systems with Applications 53 (2016) 87-105 https://doiorg/10.1016/i,eswa,2016.01.015

[11] Y. Yang, J. Gu, Z. Zhou, Credit risk evaluation based on social media, Environmental Research 148 (2016) 582–585, https://doi.org/10.1016/j.envres.2015.12.024.

[12] H.-L. Chen, B. Yang, G. Wang, J. Liu, X. Xu, S.-J. Wang, D.-Y. Liu, A novel bankruptcy prediction model based on an adaptive fuzzy k-nearest neighbor method, Knowledge-Based Systems 24 (2011) 1348–1359, https://doi.org/10.1016/j.knosys.2011. 06.008.

[13] L. Zhou, Performance of corporate bankruptcy prediction models on imbalanced dataset: the effect of sampling methods, Knowledge-Based Systems 41 (2013) 16–25, https://doi.org/10.1016/j.knosys.2012.12.007.

[14] T. Xiong, S. Wang, A. Mayers, E. Monga, Personal bankruptcy prediction by mining credit card data, Expert Systems with Applications 40 (2013) 665–676, https://doi. org/10.1016/j.eswa.2012.07.072.

[15] A. Roy, B. Halder, U. Garain, D.S. Doermann, Machine-assisted authentication of paper currency: an experiment on Indian banknotes, International Journal on Document Analysis and Recognition 18 (2015) 271–285.

[16] R.T. Rust, C. Moorman, G. Bhalla, Rethinking marketing, Harvard Business Review 88 (2010) 94–101.

[17] F. Talla Nobibon, R. Leus, F.C.R. Spieksma, Optimization models for targeted offers in direct marketing: exact and heuristic algorithms, European Journal of Operational Research 210 (2011) 670–683, https://doi.org/10.1016/j.ejor.2010.10.019.

[18] S. Moro, P. Cortez, P. Rita, A data-driven approach to predict the success of bank telemarketing, Decision Support Systems 62 (2014) 22–31, https://doi.org/10.1016/j dss.2014.03.001.

[19] S. Moro, P. Cortez, P. Rita, Using customer lifetime value and neural networks to improve the prediction of bank deposit subscription in telemarketing campaigns, Neural Computing and Applications 26 (2014) 131–139, https://doi.org/10.1007/ s00521-014-1703-0.

[20] J.R. Quinlan, C4.5: Programs for Machine Learning, Morgan Kaufmann Publishers, San Mateo, CA, 1993.

[21] W. Cohen, Fast effective rule induction, Twelfth Int. Conf. Mach. Learn 1995, pp. 115–123.

[22] D.E. Rumelhart, G.E. Hinton, R.J. Williams, Learning representations by backpropagation error, Nature 323 (1986) 533–536.

[23] J.C. Platt, Fast training of support vector machines using sequential minimal optimization, in: B. Schölkopf, C. Burges, A. Smola (Eds.),Adv. Kernel Methods Support Vector Learn, 1998.

[24] D.W. Aha, D. Kibler, M.K. Albert, Instance-based learning algorithms, Machine Learning 6 (1991) 37–66, https://doi.org/10.1007/BF00153759.

[25] R. Duda, P. Hart, Pattern Classification and Scene Analysis, Willey, New York, 1973.

[26] Y. Serrano-Silva, Risk Predictions in the Financial Environment through Unconventional Computational Algorithms, CIC-IPN, 2017.

[27] V. López, A. Fernández, F. Herrera, On the importance of the validation technique for classification with imbalanced datasets: addressing covariate shift when data is skewed, Information Sciences 257 (2014) 1–13, https://doi.org/10.1016/j.ins.2013. 09.038.

[28] J.F. Díez-Pastor, J.J. Rodríguez, C.I. García-Osorio, L.I. Kuncheva, Diversity techniques improve the performance of the best imbalance learning ensembles, Information Sciences 325 (2015) 98–117, https://doi.org/10.1016/j.ins.2015.07.025.

[29] E. Frank, R.R. Bouckaert, Naive Bayes for text classification with unbalanced classes, in: M. Furnkranz, J. Scheffer, T. Spiliopoulou (Eds.), Knowl. Discov. Databases PKDD 2006, Proc, Springer-Verlag Berlin, Heidelberg Platz 3, D-14197 Berlin, Germany 2006, pp. 503–510

[30] I. Brown, C. Mues, An experimental comparison of classification algorithms for imbalanced credit scoring data sets, Expert Systems with Applications 39 (2012) 3446–3453, https://doi.org/10.1016/j.eswa.2011.09.033

[31] M. Sokolova, N. Japkowicz, S. Szpakowicz, Beyond accuracy, F-score and ROC: a family of discriminant measures for performance evaluation, in: A Sattar, B. Kang (Eds.) AI 2006 Ady, Artif, Intell, 19th Aust, It, Conf, Artif, Intell, Hobart, Aust, December 4–8. 2006. Proc, Springer Berlin Heidelberg, Berlin, Heidelberg 2006, pp. 1015–1021 https://doi.org/10.1007/11941439\_114.

[32] M. Lichman, UCI Machine Learning Repository, 2013.

[33] J. Alcalá-Fdez, A. Fernández, J. Luengo, J. Derrac, S. García, L. Sánchez, F. Herrera, KEEL data-mining software tool: data set repository, integration of algorithms and experimental analysis framework, Journal of Multiple-Valued Logic and Soft Computing 17 (2011) 255–287.

[34] X. Yu, M. Gen, Advanced evolutionary algorithms, Introd. to Evol. Algorithms, Springer London, London 2010, pp. 39–132, https://doi.org/10.1007/978-1-84996- 129-5.3

[35] X.-B. Meng, Novel Bat Algorithm (NBA), 2015.

[36] M. Friedman, The use of ranks to avoid the assumption of normality implicit in the analysis of variance, Journal of the American Statistical Association 32 (1937) 674–701, https://doi.org/10.1080/01621459.1937.10503522

[37] M. Friedman, A comparison of alternative tests of significance for the problem of m rankings, Annals of Mathematical Statistics 11 (1940) 86–92.

[38] S. Holm, A. Simple Sequentially, Rejective multiple test procedure, Scandinavian Journal of Statistics 6 (1979) 65–70.

![](/api/attachments/REMFDNX6/fulltext/images/b99861be9ca26a85d2b1cbe3eb9a0cdd4f83c9bdd50e82d84cacf606d9812bd3.jpg)  
Yosimar Oswaldo Serrano-Silva obtained his Bachelor's degree in Computer Engineering in 2014 from the School of Computing of the National Polytechnic Institute and his MSc degree in Computer Science in 2017 from the Center for Computing Research of the same institution. His research interests include classi ers, nancial forecasting, evolutionary algorithms and associative models.

![](/api/attachments/REMFDNX6/fulltext/images/5197feb8e7c28d92afe1f0557f05b45cf5817da639889f67b370c5f5661a2c6c.jpg)  
Yenny Villuendas-Rey obtained his Bachelor and MSc degrees (2005, 2007) on Applied Informatics at Universidad de Ciego de Ávila, Cuba. Her Ph.D. was received at Universidad de Las Villas, Cuba, in 2014. Areas of interest: Metaheuristics, Intelligent Decision Systems, Data Mining, and Software Engineering. Currently, she is with CIDETEC-IPN, Mexico. Member of the National Researchers System (SNI).

![](/api/attachments/REMFDNX6/fulltext/images/9a9963d2dd78f094e9a801f022f7bf2147f07838ff8d32a4284fdae2107b58fc.jpg)

Cornelio Yáñez-Márquez obtained his Bachelor degree (1989) on Physics and Mathematics at National Poly- technics Institute (IPN) Physics and Mathematics Superior School. His MSc (1995) and Ph.D. (2002) degrees were received at IPN Center for Computing Research (CIC). Currently a Researcher Professor, Titular C, at IPN CIC. Member of the National Researchers System (SNI). Areas of interest: Associative Memories, Neural Networks, Mathematical Morphology, and Software Engineering
