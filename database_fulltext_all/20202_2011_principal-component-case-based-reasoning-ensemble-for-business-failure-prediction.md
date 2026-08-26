---
otero_id: 20202
otero_key: "3RQVBDE3"
title: "Principal component case-based reasoning ensemble for business failure prediction"
authors: "Hui Li; Jie Sun"
year: "2011"
journal: "Information & Management"
doi: "10.1016/j.im.2011.05.001"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Principal component case-based reasoning ensemble for business failure prediction

Hui Li <sup>a,b,</sup>\*, Jie Sun <sup>a</sup>

<sup>a</sup> School of Economics and Management, Zhejiang Normal University, P.O. Box 62, 688 YingBinDaDao, Jinhua, Zhejiang 321004, China <sup>b</sup> College of Engineering, The Ohio State University, 470 Hitchcock Hall, 2070 Neil Avenue, Columbus, OH 43210, USA

## A R T I C L E I N F O

Article history: Received 17 January 2011 Accepted 23 April 2011 Available online 13 May 2011

Keywords: Business failure prediction (BFP) Principal component case-based reasoning ensemble (PC-CBR-E) Multiple models combination

## A B S T R A C T

Case-based reasoning (CBR) has several advantages for business failure prediction (BFP), including ease of understanding, explanation, and implementation and the ability to make suggestions on how to avoid failure. We constructed a new ensemble method of CBR that we termed principal component CBR ensemble (PC-CBR-E): it, was intended to improve the predictive ability of CBR in BFP by integrating the feature selection methods in the representation level, a hybrid of principal component analysis with its two classical CBR algorithms at the modeling level and weighted majority voting at the ensemble level. We statistically validated our method by comparing it with other methods, including the best base model, multivariate discriminant analysis, logistic regression, and the two classical CBR algorithms. The results from a one-tailed significance test indicated that PC-CBR-E produced superior predictive performance in Chinese short-term and medium-term BFP.

\- 2011 Elsevier B.V. All rights reserved.

## 1. Introduction

Computer support systems for bank employees who are making credit-granting decisions and for monitoring the bank’s current status are critical in today’s competitive economic environment. Business failure prediction (BFP) techniques coded in these systems should obviously be accurate in order to avoid significant bank losses. Commonly used models today include multivariate discriminant analysis (MDA) [5], logistic regression (Logit) [6,9], neural network (NN) [18], case-based reasoning (CBR) [12], rough sets theory [1,14], Bayesian network [23], data envelopment analysis [2,17,19], association rules [8], and support vector machine (SVM) [4,7]. These models all predict business failure using a single predictive model.

There are two other categories of methods emerging for forecasting business failure. One was to predict business failure through decision-aiding techniques. Sun and Li [22] proposed a group decision-making approach based on experts’ knowledge and both financial and other information. The case study of the failure of a real company indicated that this qualitative method was an effective supplement to the quantitative methods in BFP. However, it was difficult to provide empirical evidence for a qualitative method. The other method attempted to predict business failure through ensembles of predictive models, assuming that the ensemble would provide a more accurate solution than a single model. Previous studies are summarized in Table 1.

West et al. [25] investigated three recent ensemble strategies with the base model of a multilayer neural network (MLP) NN, and found that the prediction of the ensemble was superior to that of the single best model for BFP. Cortes et al. [3] applied boosting techniques to improve the classification tree’s predictive accuracy in BFP for European firms, finding that the tree ensemble decreased the prediction error by thirty percent. In another study, Sun and Li [21] put forward an ensemble method for BFP by integrating MDA, Logit, NN, classification tree, SVM, and CBR. The results showed that the ensemble improved the average value of prediction accuracy and stability. Finally, Ravi et al. [20] investigated the feasibility of combining various techniques to predict business failure, with the conclusion that the ensemble was able to reduce the prediction error rate. However, ensembles were not always superior to single models in BFP [24].

The common drawback of ensembles is that the combined approach makes the BFP tool more difficult to understand, explain, implement and interpret, especially when base models, for example, SVM and NN, require time for training and validating. Thus, the complex nature of ensembles makes the use of BFP tools ineffective. Meanwhile, the accuracy may not always be improved, although ensembles may indeed potentially improve the performance of predictive models in BFP and most studies provide evidence of this

CBR is a problem-solving methodology that uses previous cases to solve new problems [13]. It is a product of cognitive science and is an imitation of the problem-solving mechanism of human beings. It has characteristics of nonparametric estimation, ease of understanding, explanation, and implementation, which make it more applicable in BFP. Thus, improving CBR’s predictive ability is important. The CBR ensemble is a potentially feasible means of doing this. The concept of the model ensemble is similar to the inside mechanism of CBR, that is, k nearest neighbor (kNN). Under this principle, Li and Sun [11] proposed a multiple CBR combination for BFP by integrating four independent CBRs on the same dataset with majority voting. The total predictive accuracy of the CBR ensemble was not always superior to its best base model, although the ensemble produced a superior performance from the analytic view on various statistic indices, that is, minimum, maximum, mean, median, and variance. Specifically, the best CBR ensemble did not outperform the best base model in terms of mean accuracy. Given that total predictive accuracy is one of the key indices when assessing predictive tools, one of the potential significant problem was how to construct effective CBR ensembles to ensure high accuracy.

Previous research of ensemble-based BFP.

<table><tr><td>Reference No.</td><td>Predicting models for ensemble</td><td>Is ensemble the most accurate?</td></tr><tr><td>[25]</td><td>NN</td><td>Yes</td></tr><tr><td>[3]</td><td>DT</td><td>Yes</td></tr><tr><td>[24]</td><td>NN</td><td>Sometimes</td></tr><tr><td>[21]</td><td>MDA, Logit, NN, SVM, CBR, DT</td><td>Yes</td></tr><tr><td>[20]</td><td>NN, SVM, DT, Fuzzy rule</td><td>Yes</td></tr><tr><td>[15]</td><td>NN, SVM, nearest neighbor</td><td>Sometimes</td></tr><tr><td>[11]</td><td>CBR</td><td>Sometimes</td></tr></table>

The objective of our research was thus to improve CBR’s predictive ability and explore an accurate ensemble forecasting method, that is, the principal component CBR ensemble (PC-CBR-E). Combining CBR, principal component analysis (PCA), and ensemble with majority voting was significant for the following reasons: (1) compared to other intelligent methods of BFP, CBR is easily understood by industrial users. It is reasonable to assume that companies with similar business indices have similar business states. If company A is similar to company B and company A has failed, company B may be very likely to fail; (2) a potential factor resulting in CBR’s relatively low predictive performance in BFP is that there may be some noisy data. This is always true when dealing with real-world problems. As a proposed solution, PCA, one of the chief techniques provided by statistic toolkits such as SPSS, is designed to find principal components from available data. Using this method, the influence of noisy data may be reduced. Thus, investigating the combination of PCA and CBR was a significant step in improving CBR’s predictive performance in BFP; (3) ensemble with majority voting is an effective and easily understandable way of making a more precise decision. The inside mechanism of CBR, kNN, can be regarded as a variation of majority voting. Thus, investigating the combination of CBR with the ensemble principle of majority voting can potentially improve CBR’s predictive ability.

## 2. Why combine CBR, PCA and majority voting?

Aside from the possibility of improving CBR’s predictive accuracy, major advantages are:

(1) CBR in BFP can provide suggestions suggesting to managers if they find that their companies are likely to fail. The core principle of CBR in BFP is to retrieve sample companies similar to the target company and use their business states to predict the future of the target company.

(2) The goal of PCA is to reduce the dimension of the business data. The lower-dimensional space retains those characteristics of the data that contribute most to its variance. Lower-order components are kept, as they often contain the most important aspects of the data. The core algorithm of CBR is k-NN, which is a lazy learning algorithm. When making predictions with CBR, all similarities between the target case and each experienced case are calculated, entailing much time. Using PCA reduces the dimensions of business data and thus reduces the time required for similarity calculation. Thus, our method used PCA to help CBR produce predictions for the ensemble. Tens of principal component CBRs (PC-CBRs) were constructed as base models.

(3) The mechanism of majority voting is most often employed by influential decision-making bodies. It is a useful rule for protecting the interest of the majority group. The task of BFP could thus be considered as a binary decision. The output of the CBR for BFP is either failure or non-failure.

## 3. The method of principal components case-based reasoning ensemble (PC-CBR-E)

## 3.1. The idea of model ensemble for BFP

The combination of multiple models for BFP is shown in Fig. 1. Use of an ensemble of various models can integrate their advantages and thus provide a stable and superior prediction.

We chose the family of CBR for the construction of the base models. If all base models are the same, the ensemble will make no difference in predictive performance. Thus, using diverse models producing different predictions on same samples are critical to the ensemble. There are two effective ways of producing diverse base models: (1) to use various datasets which are used as inputs into the same predictive model; (2) to use different predictive models with the same dataset.

For the combination of base models, consensus of the majority and opinions concerning good base models should be protected. This treatment can provide strong evidence of how the prediction is made and can assure that the ensemble produces good results. For the binary classification problem of BFP, almost all other methods can be viewed as variations of majority voting to adjust weights in voting.

## 3.2. The principle constructing PC-CBR-E

We attempted to use the two methods to produce various predictive models. Feature selection methods were used to generate various datasets. Different implementations of CBR were used to produce various predictive models. The principle of PC-CBR-E is illustrated in Fig. 2.

First, various datasets are used to represent cases with various feature selection methods. The ‘features’ are financial ratios in BFP. Different case representations produce different input spaces. In the process of case retrieval, various CBR algorithms were used to generate CBR models. Thus, PCA is independently used to make various CBRs extract effective information from input spaces. Thus, several specific implementations of PC-CBRs can be produced by reusing solutions of similar cases. Finally, the ensemble principle was used to reach agreement on predictive results among the models.

## 3.3. The structure of PC-CBR-E

The process of implementing the principle of PC-CBR-E is illustrated in Fig. 3. The detailed structure of PC-CBR-E, consisting of three levels, as illustrated in Fig. 4.

The input of PC-CBR-E is business data collected for BFP composed of all available features representing cases and usefu sample values of corresponding features. The representation level is used to produce four representations for CBR to predict business failure: stepwise MDA, stepwise Logit and t-test were used to select optimal features from the initial ones. Thus, four different datasets in the representation level: initial data represented by all available features, those represented by features from stepwise MDA, those from stepwise Logit, and those from t-test were all used to produce the input for the predicting model of CBR.

![](/api/attachments/3RQVBDE3/fulltext/images/71ddaf65f69f25545023b1e00bd7959fa37f64aafb275459af8e3c4962a4ea70.jpg)  
Fig. 1. The structure of ensemble.

The predicting model level was used to process data and make predictions for BFP. PCA was used to extract principal information for the four cases. This was then used as input to CBR with Euclidean metrics (ECBR) and CBR with Manhattan metrics (MCBR); thus, pre-forecasting was achieved and the output of the base models was known to be either correct or wrong for BFP.

If the filter of stepwise MDA was used for a model, we add an ‘M’ before its name. If the filter of stepwise Logit is used, we add an ‘L’ before its name. If the t-test was used, we added a $\mathrm { ^ { 1 \prime } , }$ and if PCA was used we added a ‘P’. Thus, we obtained eight different implementations of PC-CBR

Since the algorithm of classical CBRs is kNN, then it was necessary to determine the value of k. As indicated by [16], 1, 3, 5, 7, and 9 are commonly used in CBR. However the nearest neighbor (k = 1) is not robust to noisy data. Thus all four kNNs were integrated into the process to generate more base models. Accordingly, we constructed 32 models (eight PC-CBR - four algorithms of kNN) to produce pre-forecasting for BFP, and these were combined at the ensemble level.

Not all base models produced good results. Obviously only good models should be used in the ensemble. Thus, we only combined models with the accuracy values above the mean accuracy values of all the models. Each component of the structure of PC-CBR-E fulfills different key roles in the task of BFP. Thus, PC-CBR-E can potentially integrate the advantages of the eight CBRs to produce a stable and superior performance.

## 3.4. The process of extracting principal information

In the predicting model level, one key process was to extract principal information from the four different case representations. By using a linear transformation, PCA can map a case representation to a lower-dimensional space. In determining the best lowerdimensional space, the best eigenvectors of the covariance matrix were used to identify the best principal components. Let a case for BFP be expressed by N features, that is, $f _ { 1 } , f _ { 2 } , . . . , f _ { N } ,$ and let $x _ { i j }$ express the value of the jth case on the ith feature. If the number of cases is $M , x _ { 1 } , x _ { 2 } , . . . ,$ x are vectors of size N. The process of extracting the principal information is illustrated in Fig. 5. We used principal information that met the condition $\lambda > 1$

## 3.5. Similarity calculation

The two classical algorithms of CBR are used to produce predictions. The key process of CBR-based BFP was the similarity measure, based on the Euclidean and the Manhattan metrics. Assuming that $x ^ { \prime }$ expresses the K vector representing cases, the calculation of similarity between each pair of cases in ECBR is was:

$$
\begin{array}{r l} E S i m (c _ {a}, c _ {b}) & = \frac {1}{1 + E u c l i d e a n d i s (c _ {a} , c _ {b})} \\ & = \frac {1}{1 + \sqrt {\sum_ {i = 1} ^ {K} \left[ w _ {i} (x _ {i a} ^ {\prime} - x _ {i b} ^ {\prime}) \right] ^ {2}}} \end{array}\tag{1}
$$

where, $w _ { i }$ is the weight of the ith feature, while $x _ { i a } ^ { \prime }$ and $x _ { i b } ^ { \prime }$ express the value of case a and case $b ,$ respectively, on the ith feature. The calculation of similarity between each pair of cases in MCBR was:

$$
\begin{array}{r l} M S i m (c _ {a}, c _ {b}) & = \frac {1}{1 + M a n h a t t a n d i s (c _ {a} , c _ {b})} \\ & = \frac {1}{1 + \sum_ {i = 1} ^ {K} \left[ w _ {i} (x _ {i a} ^ {\prime} - x _ {i b} ^ {\prime}) \right]} \end{array}\tag{2}
$$

## 3.6. Prediction ensemble

The most similar cases were then retrieved and reused to predict the likelihood of business failure or non-failure of the target case. Class labels of the most similar cases were used to vote for the label. After the eight PC-CBR models had produced predictions on the business state, consensus resulting from PC-CBRs was calculated by majority voting. It is reasonable that the CBR with higher accuracy should be given more importance in the ensemble. Thus:

$$
l \left(c _ {a}\right) = \underset {z} {\operatorname{argmax}} \sum_ {\left(p c c b r _ {j}, l \left(p c c b r _ {j}\right) \in D\right)} a c c _ {j} \times L \left(z = l \left(p c c b r _ {j}\right)\right),\tag{3}
$$

where L() is an indicator function that only returns 1 or $0 ; D$ is the set of PC-CBRs with the condition that its accuracy value is larger than the mean accuracy value; z is a class label; pccbr expresses the prediction produced by jth PC-CBR; and acc<sub>j</sub> is the accuracy produced by the PC-CBR. Finally, predictions can be made with PC-CBR-E.

![](/api/attachments/3RQVBDE3/fulltext/images/5e3e7c66d8e13c906d32c2daac8270cf692c49d7bce040f2dd928bfea9531e1e.jpg)  
Fig. 2. The principle of constructing PC-CBR-E.

![](/api/attachments/3RQVBDE3/fulltext/images/4b04a0e9d0310a5a244147f0108043120e3f75abb7aa15211d2128f08190a05d.jpg)  
Fig. 3. Implementing the principle of PC-CBR-E.

## 4. Empirical research on Chinese BFP

## 4.1. Performance assessment

We determined whether the PC-CBR-E could achieve better accuracy than the classical CBRs. We used total accuracy in assessment and did not distinguish between Type I (predicting unhealthy companies as healthy ones) and Type II (predicting healthy companies as healthy ones) errors. Thus, we used total predictive accuracy, rather as the means of assuring good quality of suggestions and to exclude noisy sample companies.

## 4.2. Data and initial features

Listed Chinese companies are specially treated (ST) by the China Securities Supervision and Management Committee (CSSMC) for two reasons: a company has had negative net profit for two consecutive years or a company’s net capital per share is lower than its face value.

We collected 135 pairs of samples from the Shanghai and Shenzhen Stock Exchanges, including companies in business both failure and non-failure. We performed data preprocessing to

![](/api/attachments/3RQVBDE3/fulltext/images/b510ed5e46e75c73188662b747af314792eaf99e47a7b9adf3e4a1d664841820.jpg)  
Fig. 4. The structure of PC-CBR-E.

![](/api/attachments/3RQVBDE3/fulltext/images/597cca9a7c9705ea338eaa47fe52010896bce15215d339673a43302a15ddb87d.jpg)  
Fig. 5. The process of extracting principal information.

eliminate outliers and missing values, after which we had 153 sample companies for Chinese short-term BFP. We also obtained 216 sample companies for Chinese medium-term BFP. Initial features included eight profitability ratios, six activity ratios, seven liability ratios, four structure ratios, two growth ratios, and three per share items and yields. Initial features selected for Chinese short-term [10] and medium-term BFP by stepwise MDA, stepwise Logit, and t-test are listed in Table 2.

## 4.3. Empirical design

Two statistical methods (MDA and Logit) have been used for comparisons in BFP and were used as our benchmark methods. ECBR and MCBR were also used. For benchmarking purposes, stepwise MDA was used to select optimal features, since this filter has been found to be an optimal approach for Chinese BFP [12]. Obviously, whether PC-CBR-E is superior to its best base model was of interest. For classical CBRs, we used 7NN to produce predictions because this is an optimal model. All data were scaled into the range of [0,1] with min–max standardization.

Table 2  
Initial features and those selected for Chinese BFP.

<table><tr><td rowspan="2">FeaturesNo.</td><td colspan="4">Short-term BFP</td><td colspan="3">Medium-term BFP</td></tr><tr><td>Name</td><td>Stepwise MDA</td><td>Stepwise Logit</td><td>t-test</td><td>Stepwise MDA</td><td>Stepwise Logit</td><td>t-Test</td></tr><tr><td>1</td><td>Equity/fixed assets</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2</td><td>Current liability/total liability</td><td></td><td></td><td>0</td><td></td><td></td><td>0</td></tr><tr><td>3</td><td>Account payable turnover</td><td></td><td></td><td></td><td>0</td><td>0</td><td></td></tr><tr><td>4</td><td>Cash flow per share</td><td></td><td></td><td>0</td><td></td><td></td><td>0</td></tr><tr><td>5</td><td>Total assets turnover</td><td>0</td><td></td><td>0</td><td></td><td></td><td>0</td></tr><tr><td>6</td><td>Current assets turnover</td><td></td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>7</td><td>Ebit/total asset</td><td></td><td></td><td>0</td><td></td><td></td><td>0</td></tr><tr><td>8</td><td>Net assets per share</td><td></td><td>0</td><td>0</td><td></td><td></td><td>0</td></tr><tr><td>9</td><td>Growth rate of primary business</td><td></td><td></td><td>0</td><td></td><td></td><td></td></tr><tr><td>10</td><td>Gross income/sales</td><td></td><td></td><td>0</td><td></td><td></td><td>0</td></tr><tr><td>11</td><td>Net profit/current assets</td><td></td><td></td><td>0</td><td>0</td><td></td><td>0</td></tr><tr><td>12</td><td>Fixed assets turnover</td><td></td><td></td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>13</td><td>Asset-liability ratios</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>14</td><td>Net income/sales</td><td></td><td></td><td>0</td><td></td><td></td><td>0</td></tr><tr><td>15</td><td>Net profit/fixed assets</td><td></td><td></td><td>0</td><td></td><td></td><td></td></tr><tr><td>16</td><td>Interest coverage ratio</td><td></td><td></td><td></td><td></td><td></td><td>0</td></tr><tr><td>17</td><td>Inventory turnover</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>18</td><td>Net profit/total assets</td><td></td><td></td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>19</td><td>Current ratio</td><td></td><td></td><td>0</td><td></td><td></td><td>0</td></tr><tr><td>20</td><td>Current assets/total assets</td><td></td><td></td><td></td><td></td><td></td><td>0</td></tr><tr><td>21</td><td>Fixed assets/total assets</td><td></td><td></td><td></td><td></td><td></td><td>0</td></tr><tr><td>22</td><td>Profit margin</td><td></td><td></td><td>0</td><td></td><td></td><td>0</td></tr><tr><td>23</td><td>Net profit/equity</td><td></td><td></td><td>0</td><td>0</td><td></td><td>0</td></tr><tr><td>24</td><td>Account receivable turnover</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>25</td><td>Equity/debt ratio</td><td></td><td></td><td>0</td><td></td><td>0</td><td>0</td></tr><tr><td>26</td><td>Liability/equity market value</td><td></td><td></td><td>0</td><td></td><td></td><td>0</td></tr><tr><td>27</td><td>Cash to current liability</td><td></td><td></td><td>0</td><td></td><td></td><td>0</td></tr><tr><td>28</td><td>Growth rate of total assets</td><td>0</td><td></td><td>0</td><td></td><td></td><td>0</td></tr><tr><td>29</td><td>Liability/tangible net asset</td><td></td><td></td><td>0</td><td></td><td></td><td>0</td></tr><tr><td>30</td><td>Earning per share</td><td>0</td><td>0</td><td>0</td><td></td><td></td><td>0</td></tr></table>

![](/api/attachments/3RQVBDE3/fulltext/images/f4d02002e927d555687650eb2866fe8703c0a619076365c96525a90a2348532e.jpg)  
Fig. 6. The empirical design.

In order to obtain evidence on the predictive performance of our new ensemble method in BFP, we randomly split the dataset 50 times. At each split, the entire dataset was randomly split into two. One part, 70%, was used as the training. The other part, 30%, was used as the test dataset. The empirical design is illustrated in Fig. 6.

## 4.4. Research hypotheses

We wished to investigate whether the predictive performance of PC-CBR-E was significantly better than that of the compared methods. Thus, a one-tailed significance test was used. Our hypotheses were as follows:

H : The performance of PC-CBR-E is significantly better than that of M-MDA.

H : The performance of PC-CBR-E is significantly better than that of M-Logit.

H : The performance of PC-CBR-E is significantly better than that of M-ECBR.

H : The performance of PC-CBR-E is significantly better than that of M-MCBR.

H<sub>5</sub>: The performance of PC-CBR-E is significantly better than that of the BEST base PC-CBR.

## 5. Empirical results and analysis

## 5.1. Predictive results

The results of mean predictive accuracies, standard deviations, median accuracy, maximum accuracy, minimum accuracy, and the best times of statistic indices for Chinese BFP are shown in Tables 3 and 4. We tested the hypotheses. The results are presented in Tables 5 and 6.

## Table 3

Statistics of predictive accuracies for Chinese short-term BFP.

<table><tr><td>Methods</td><td>Mean</td><td>SD</td><td>Median</td><td>Maximum</td><td>Minimum</td><td>Best times</td></tr><tr><td colspan="7">Comparative models</td></tr><tr><td>M-MDA</td><td>88.93</td><td>4.17</td><td>88.89</td><td>100.0</td><td>80.00</td><td>1</td></tr><tr><td>M-Logit</td><td>87.51</td><td>4.64</td><td>86.67</td><td>100.0</td><td>73.33</td><td>1</td></tr><tr><td>M-ECBR</td><td>88.84</td><td>3.90</td><td>88.89</td><td>97.78</td><td>77.78</td><td>0</td></tr><tr><td>M-MCBR</td><td>88.36</td><td>3.88</td><td>88.89</td><td>100.0</td><td>80.00</td><td>1</td></tr><tr><td colspan="7">The best base PC-CBR</td></tr><tr><td>M-P-ECBR with 9NN</td><td>90.13</td><td>4.47</td><td>91.11</td><td>100.0</td><td>75.56</td><td>2</td></tr><tr><td colspan="7">Ensemble</td></tr><tr><td>PC-CBR-E</td><td>91.87</td><td>3.26</td><td>91.11</td><td>100.0</td><td>86.67</td><td>5</td></tr></table>

Values in bold means that they are the largest.

## Table 4

Statistics of predictive accuracies for Chinese medium-term BFP.

<table><tr><td>Methods</td><td>Mean</td><td>SD</td><td>Median</td><td>Maximum</td><td>Minimum</td><td>Best times</td></tr><tr><td colspan="7">Comparative models</td></tr><tr><td>M-MDA</td><td>83.72</td><td>3.93</td><td>84.38</td><td>90.63</td><td>71.88</td><td>0</td></tr><tr><td>M-Logit</td><td>83.16</td><td>3.70</td><td>82.81</td><td>90.63</td><td>73.44</td><td>1</td></tr><tr><td>M-ECBR</td><td>84.50</td><td>3.40</td><td>84.38</td><td>92.19</td><td>73.44</td><td>3</td></tr><tr><td>M-MCBR</td><td>83.94</td><td>3.59</td><td>84.38</td><td>90.63</td><td>73.44</td><td>1</td></tr><tr><td colspan="7">The best base PC-CBR</td></tr><tr><td>L-P-MCBR with 9NN</td><td>84.91</td><td>3.94</td><td>85.94</td><td>92.19</td><td>68.75</td><td>2</td></tr><tr><td colspan="7">Ensemble</td></tr><tr><td>PC-CBR-E</td><td>85.72</td><td>3.80</td><td>85.94</td><td>92.19</td><td>71.88</td><td>3</td></tr></table>

Values in bold means that they are the largest.

Table 6  
Table 5  
One-tailed significance test for Chinese short-term BFP.

<table><tr><td>Methods</td><td>Mean accuracy</td><td>t statistic and p values</td><td>Significance test on difference</td><td>Hypothesis</td></tr><tr><td>PC-CBR-E</td><td>91.87</td><td>-4.97(0.000)***</td><td>Significant at the level of 1%</td><td>Accept H1</td></tr><tr><td>M-MDA</td><td>88.93</td><td></td><td></td><td></td></tr><tr><td>PC-CBR-E</td><td>91.87</td><td>-6.64(0.000)***</td><td>Significant at the level of 1%</td><td>Accept H2</td></tr><tr><td>M-Logit</td><td>87.51</td><td></td><td></td><td></td></tr><tr><td>PC-CBR-E</td><td>91.87</td><td>-5.48(0.000)***</td><td>Significant at the level of 1%</td><td>Accept H3</td></tr><tr><td>M-ECBR</td><td>88.84</td><td></td><td></td><td></td></tr><tr><td>PC-CBR-E</td><td>91.87</td><td>-6.40(0.000)***</td><td>Significant at the level of 1%</td><td>Accept H4</td></tr><tr><td>M-MCBR</td><td>88.36</td><td></td><td></td><td></td></tr><tr><td>PC-CBR-E</td><td>91.87</td><td>-2.74(0.004)***</td><td>Significant at the level of 1%</td><td>Accept H5</td></tr><tr><td>P-CBR</td><td>90.13</td><td></td><td></td><td></td></tr></table>

Values in bold means that they are the largest.

## 5.2. Hypothesis evaluation

## 5.2.1. Accuracy

The results show that PC-CBR-E produced the best mean accuracy of 91.9% in terms of short-term BFP. This value was superior to others in terms of absolute value. This means that PC-CBR-E reduces the error rates of the comparative models by at least 17.3%. The SD value of predictive accuracies of PC-CBR-E was 3.2; this could be considered as the best of all predictive methods. Also, PC-CBR-E achieved the best ratio of all the five statistic indices indicating that PC-CBR-E is superior to all other models in terms of predictive ability and stability in Chinese short-term BFP.

The results also show that PC-CBR-E produced the best mean accuracy of 85.7% in terms of medium-term BFP. This was superior to all others, meaning that PC-CBR-E had the least error rate of all. Also, PC-CBR-E had the best ratio of the five statistic indices for best mean accuracy, best median accuracy, and best maximum accuracy. Thus PC-CBR-E was superior to all other models in terms of predictive ability and stability in Chinese medium-term BFP.

M-MDA also performed best with its mean accuracy of 88.9% for short-term BFP. In addition, M-ECBR performed the best with the mean accuracy of 84.50% for medium-term BFP. This finding suggests that the predictive models may be sample-dependent. However, PC-CBR-E performed consistently better than other methods indicating that the CBR ensemble may reduce any sample dependency to some extents.

## 5.2.2. Significance test

The results of the hypotheses of predictive performance between PC-CBR-E and other methods indicated that all five hypotheses in their alternate forms were accepted: null forms were rejected. This shows that the performance of PC-CBR-E was significantly better than the other models for predicting Chinese short-term BFP. PC-CBR-E also significantly outperformed M-MDA, M-Logit, M-ECBR, and M-MCBR at the 1% level and outperformed the best base model at a significant level of 10% for Chinese medium-term BFP. These findings prove that PC-CBR-E outperformed all other models.

## 5.3. Analysis

On the whole, the results indicated that the CBR ensemble can effectively improve CBR’s predictive accuracy. This can be attributed to the employment of PCA and majority voting to combine classical CBRs. We found that PCA with filters could reduce the influence of noisy data in BFP; this helps the kNN algorithm in CBR to provide better performance. Majority voting helps CBR achieve better predictive accuracy. Various similar sample companies are retrieved inside each base CBR because it provides suggestions of how to avoid a disaster.

Consensus in similar companies of the group of base CBRs for the ensemble can provide a company strong support in dealing with its current affairs. The company can refer to the other similar companies for suggestions on how to deal with the current risk of business failure.

In addition, a business organization will not only be able to refer to why and how similar sample companies fail and avoid similar failures, but also refer to senior managers of retrieved companies for detailed advice and analysis, and even employ them as consultants. With this treatment, a company may not only be informed on whether the company is at high risk of business failure but also be given suggestions and a thorough understand ing of why, how and what to do. As a result, managers and government supervisors will know how to improve the operation and management of the company. Meanwhile, those companies that are predicted to be at a low risk of business failure can refer to similar companies on how to maintain their current business state.

One-tailed significance test for Chinese medium-term BFP.

<table><tr><td>Methods</td><td>Mean accuracy</td><td>t statistic and p values</td><td>Significance test on difference</td><td>Hypothesis</td></tr><tr><td>PC-CBR-E</td><td>85.72</td><td>-3.60(0.000)***</td><td>Significant at the level of 1%</td><td>Accept H1</td></tr><tr><td>M-MDA</td><td>83.72</td><td></td><td></td><td></td></tr><tr><td>PC-CBR-E</td><td>85.72</td><td>-4.90(0.000)***</td><td>Significant at the level of 1%</td><td>Accept H2</td></tr><tr><td>M-Logit</td><td>83.16</td><td></td><td></td><td></td></tr><tr><td>PC-CBR-E</td><td>85.72</td><td>-2.54(0.001)***</td><td>Significant at the level of 1%</td><td>Accept H3</td></tr><tr><td>M-ECBR</td><td>84.50</td><td></td><td></td><td></td></tr><tr><td>PC-CBR-E</td><td>85.72</td><td>-3.51(0.001)***</td><td>Significant at the level of 1%</td><td>Accept H4</td></tr><tr><td>M-MCBR</td><td>83.94</td><td></td><td></td><td></td></tr><tr><td>PC-CBR-E</td><td>85.72</td><td>-1.46(0.076)*</td><td>Significant at the level of 10%</td><td>Accept H5</td></tr><tr><td>P-CBR</td><td>84.91</td><td></td><td></td><td></td></tr></table>

Values in bold means that they are the largest.

## 6. Conclusion and limitations

We have shown that CBR’s predictive ability outperforms the best base CBR and all comparative models in terms of accuracy. A one-tailed significance test provided evidence that our new method is applicable in BFP. Using data collected for Chinese short-term and medium-term BFP, PC-CBR-E outperformed the two classical statistical methods of MDA and Logit, the two classical algorithms of CBR (ECBR and MCBR) and the best base model at the 1% level of significance; however, PC-CBR-E outperformed the best single base model of the ensemble for Chinese medium-term BFP at the 10% significance level. Thus CBR ensemble makes up for the shortcoming of classical CBRs.

With the evidence that the CBR ensemble can provide high predictive accuracy, businesses can use data from similar companies as the sources for their analysis of their risk of business failure.

In general, the contribution of this research is that it provides a new way for forecasting business failure and provides an accurate and easy tool for users. This research, however, has some limitations: (1) it demonstrated the feasibility of using PC-CBR-E to predict Chinese business failures: however we have not shown that this is generalizable world-wide; (2) we assumed that any business decision should be economically rational and that the economic aspects of business are directly related to business failure. However, decision-psychological characteristics of top business managers also influence business failure; we did not consider the psychological aspect of decision-making; (3) we were not able to distinguish Type I and Type II errors.

The authors gratefully thank Prof. Edgar H. Sibley (editor-inchief), the associate editor, and the three anonymous referees for their editing and review work, constructive comments and recommendations. This research is partially supported by the National Natural Science Foundation of China (No. 70801055) and the Zhejiang Provincial Natural Science Foundation of China (No. Y7100008).

[1] I. Bose, Deciding the financial health of dot-coms using rough sets, Information & Management 43 (7), 2006, pp. 835–846.

## Acknowledgements

[2] A. Cielen, L. Peeters, K. Vanhoof, Bankruptcy prediction using a data envelopment analysis, European Journal of Operational Research 154 (2), 2004, pp. 526–532.

## References

[3] E.A. Cortes, M.Z. Martinez, N.G. Rubio, A boosting approach for corporate failure prediction, Applied Intelligence 27 (1), 2007, pp. 526–532.

[4] Y. Ding, X. Song, Y. Zeng, Forecasting financial condition of Chinese listed companies based on support vector machine, Expert Systems with Application 34 (4), 2008, pp. 3081–3089.

[5] J.S. Grice, R.W. Ingram, Tests of the generalizability of Altman’s bankruptcy prediction model, Journal of Business Research 54 (1), 2001, pp. 53–61.

[6] D.A. Hensher, S. Jones, Forecasting corporate bankruptcy: optimizing the performance of the mixed logit model, ABACUS 43 (3), 2007, pp. 241–264.

[7] Z. Hua, Y. Wang, X. Xu, B. Zhang, L. Liang, Predicting corporate financial distress based on integration of support vector machine and logistic regression, Expert Systems with Applications 33 (2), 2007, pp. 434–440

[8] D. Janssens, G. Wets, T. Brijs, et al., Adapting the CBR algorithm by means of intensity of implication, Information Sciences 173, 2005, pp. 305–318.

[9] S. Jones, D.A. Hensher, Predicting firm financial distress: a mixed Logit model Accounting Review 79 (4) 2004 pp. 1011–1038

[10] H. Li, H. Adeli, J. Sun, J. Han, Hybridizing principles of TOPSIS with case-based reasoning for business failure prediction, Computers and Operations Research 38, 2011, pp. 409–419.

[11] H. Li, J. Sun, Majority voting combination of multiple case-based reasoning of financial distress prediction, Expert Systems with Applications 36 (3), 2009, pp. 4363–4373.

[12] H. Li, J. Sun, Hybridizing principles of the Electre method with case-based reasoning for data mining, European Journal of Operational Research 197 (1), 2009, pp. 214–224.

[13] C.-H. Liu, L.-S. Chen, C.-C. Hsu, An association-based case reduction technique for case-based reasoning, Information Sciences 178 (17), 2008, pp. 3347–3355.

[14] T.E. McKee, Rough sets bankruptcy prediction models versus auditor signaling rates, Journal of Forecasting 22 (8), 2003, pp. 569–586.

[16] R. Pan, Q. Yang, J. Pan, Mining competent case bases for case-based reasoning Artificial Intelligence 171 (16–17), 2007, pp. 1039–1068.

[15] L. Nanni, A. Lumini, An experimental comparison of ensemble of classifiers for bankruptcy prediction and credit scoring, Expert Systems with Applications 36 (2), 2009, pp. 3028–3033.

[17] P.C. Pendharkar, A potential use of data envelopment analysis for the inverse classification problem, Omega 30 (3), 2002, pp. 243–248.

[18] P.C. Pendharkar, A threshold-varying artificial neural network approach for classification and its application to bankruptcy prediction problem, Computers and Operations Research 32, 2005, pp. 2561–2582.

[19] I.M. Premachandra, G. Bhabra, T. Sueyoshi, DEA as a tool for bankruptcy assessment: a comparative study with logistic regression technique, European Journal of Operational Research 192 (2), 2009, pp. 412–424.

[20] V. Ravi, H. Kurniawan, P. Thai, et al., Soft computing system for bank performance prediction, Applied Soft Computing 8, 2008, pp. 305–315.

[21] J. Sun, H. Li, Listed companies’ financial distress prediction based on weighted majority voting combination of multiple classifiers, Expert Systems with Appli cations 35 (3), 2008, pp. 818–827

[22] J. Sun, H. Li, Financial distress early warning based on group decision making, Computers and Operations Research 36 (3), 2009, pp. 885–906.

[23] L. Sun, P.P. Shenoy, Using Bayesian networks for bankruptcy prediction: Some methodological issues, European Journal of Operational Research 180 (2), 2007, pp. 738–753.

[24] C.-F. Tsai, J.-W. Wu, Using neural network ensembles for bankruptcy prediction and credit scoring, Expert Systems with Applications 34 (4), 2008, pp. 2639–2649

[25] D. West, S. Dellana, J. Qian, Neural network ensemble strategies for financial decision applications, Computers and Operations Research 32, 2005, pp. 2543– 2559.

![](/api/attachments/3RQVBDE3/fulltext/images/e80e9579d16e72267b39aa247f839fcb60eed420d1ce3697d684d4546a7d25a5.jpg)

Hui Li is an associate professor in School of Economics and Management of Zhejiang Normal University, China, and was a visiting scholar in College of Engineering of The Ohio State University US He received the BS MS and PhD degrees from Harbin Institute of Technology, China. His research interests include: case-based reasoning, business intelligence, business computing, business data mining, and business forecasting, among others. His has published some papers, which appeared or will appear on some leading or reputable journals such as: Applied Soft Computing, Computers & Industria Engineering Computers &τ Operations Research. Furopear

Journal of Operational Research, Expert Systems with Applications, Information & Management, Information Sciences, Journal of Forecasting, Knowledge-Based Systems, among others. He is a young researcher of World Federation on Soft Computing, and a member of Associations for Information Systems. He received the award of Outstanding Young Talents in Zhejiang Province, and the Science Research Award of Zhejiang Provincial Universities.

![](/api/attachments/3RQVBDE3/fulltext/images/663c83eec8a0c7c7e4657dad1c91421e8dd87b5da735792c5d862a76de818c2f.jpg)

Jie Sun is an associate professor in School of Economic and Management of Zhejiang Normal University, China. She received her BS, MS, and PhD degrees from Harbin Institute of Technology, China. Her research interests are financial risk management, neural networks in economics, support vector machine in economics, concept drift, and financial intelligence. Her researches were published on Applied Soft Computing, Computers & Operations Research, European Journal of Operational Research, Expert Systems with Applications, Information Sciences, Journal of Forecasting, Knowledge-Based Sys tems, among others. She received the Science Research

Award of Zhejiang Provincial Universities, and the Social Science Research Award of Jinhua.
