---
otero_id: 17587
otero_key: "BCU4EGQU"
title: "Bankruptcy prediction using neural networks"
authors: "Rick L. Wilson; Ramesh Sharda"
year: "1994"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)90024-8"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Bankruptcy prediction using neural networks

Rick L. Wilson and Ramesh Sharda
Oklahoma State University, Stillwater, OK, USA

Prediction of firm bankruptcies have been extensively studied in accounting, as all stakeholders in a firm have a vested interest in monitoring its financial performance. This paper presents an exploratory study which compares the predictive capabilities for firm bankruptcy of neural networks and classical multivariate discriminant analysis. The predictive accuracy of the two techniques is presented within a comprehensive, statistically sound framework, indicating the value added to the forecasting problem by each technique. The study indicates that neural networks perform significantly better than discriminant analysis at predicting firm bankruptcies. Implications of our results for the accounting professional, neural networks researcher and decision support system builders are highlighted.

Keywords: Neural network applications; Bankruptcy prediction; Discriminant analysis; Classification techniques

![](/api/attachments/BCU4EGQU/fulltext/images/8bad7e381e5eab535704cbb28d7d527678edbeb4f59bf59ef41163650ff504ff.jpg)

Rick L. Wilson is currently an Assistant Professor of Management Science and Information Systems at Oklahoma State University. He received his Ph.D. in MIS from the University of Nebraska-Lincoln. Dr. Wilson has published in journals such as Information and Management, International Journal of Production Research, International Journal of Production and Operations Management, among others. He is a member of Decision Sciences Institute, The Institute of

Management Science, and Operations Research Society of America. His current research interests include neural networks, decision support systems and integrated management science applications.

## 1. Introduction

The ability to predict firm bankruptcies has been extensively studied in the accounting literature. Creditors, auditors, stockholders and senior management all have a vested interest in utilizing and developing a methodology or model that will allow them to monitor the financial performance of a firm via accounting ratios. This “failure analysis” can be helpful in identifying internal problems, firm evaluation by investors, and as a tool used by auditors to assist them in their job.

Typically, a number of financial ratios are used in a multivariate discriminant analysis approach in an attempt to predict firm bankruptcies. Discriminant analysis is a statistical technique used to construct classification schemes so as to assign previous unclassified observations to the appropriate group $[15]$ . However, it may be a valid technique only under certain restrictive assumptions, including the requirement for the discriminating variables to be jointly distributed according to a multivariate normal distribution. Should this not be the case, results obtained by the discriminant analysis procedure may be erroneous.

Neural Networks represents a field of study within the Artificial Intelligence area where re-

![](/api/attachments/BCU4EGQU/fulltext/images/3311f315a2a942e05330260301d1779cceb2713b121ad7bfef98cbc0adb43ae9.jpg)  
puter Advances on Operations Research, and Knowledge-Based Systems and Neural Networks: Techniques and Applications. He is a member of The Institute of Management Science, Operations Research Society of America and the Decision Sciences Institute. His current research interests include decision support systems, forecasting, optimization on microcomputers, neural networks and expert systems.

Ramesh Sharda is the Conoco/DuPont Professor of Management of Technology at Oklahoma State University. Professor Sharda received his Ph.D. from the University of Wisconsin-Madison. His publications have appeared in major academic journals such as Management Science, Interfaces, Computers and Operations Research, Journal of Intelligent Manufacturing and Socio-Economic Planning Sciences. In addition, he has coedited two books: Impacts of Recent Comsearchers are studying a “biologically inspired” way of processing information. To this point, neural networks have proven to be good at solving some real-world problems, especially in the areas of forecasting and classification decision problems.

The exploratory study presented in this paper contrasts neural network predictive accuracy with that of discriminant analysis for the decision problem of firm bankruptcy prediction. Using a resampling methodological design, a series of experiments was conducted to investigate the effect of the training and testing (holdout) set composition on predictive accuracy. These predictive results were then contrasted with the accuracy obtained by classical discriminant analysis to determine the conditions where neural network models are significantly better predictors.

The major objectives of this paper are the following. First, we report the results of a comprehensive, statistically sound comparison of discriminant analysis and a neural network model. Second, we utilize in this analysis measures of the validity of any classification technique which have been used extensively in the psychology literature. These measures allow researchers to assess the true value added by a technique. Third, we conclude with a brief conjecture on how neural networks may affect decision support systems.

Our objective is not to examine speed of a new algorithm, or study a new architecture, but rather to test a neural network's effectiveness in performing classifications as contrasted against the incumbent techniques. Better algorithms should only improve the performance. In this sense, our results should provide a lower bound of the neural network model's predictive performance in bankruptcy prediction.

Section 2 briefly reviews bankruptcy prediction and the neural network literature. Section 3 describes our comparison procedure. Section 4 presents the results, while section 5 discusses implications of our results for researchers from three areas: bankruptcy prediction, neural networks, and decision support systems.

## 2. Brief review of relevant research

## 2.1. Bankruptcy risk prediction

In the present days of economic turmoil, it is not surprising that the bankruptcy prediction problem remains of great interest to researchers as well as creditors, shareholders and auditors. Firm insolvency is a problem throughout the industrialized countries of the world [4]. Creditors have a vested interest in this decision problem in that they wish to identify negative developments of their borrowers. Stockholders hold similar monetary concerns. Auditors, as a normal responsibility, must evaluate the financial position of a client to determine whether or not the firm's operating ability is endangered [3]. Thus, senior management of a firm and the board of directors can attempt to avert the crisis [34]. For all parties, it is essential that an objective opinion on the risk of bankruptcy can be formed as early as possible.

Predicting bankruptcy has been studied extensively in the accounting literature. The first studies were performed to determine whether financial ratios provide useful information $[1,5]$ . There have been many different studies since $[5]$ utilizing financial ratios for bankruptcy prediction, a majority of which use a multivariate discriminant analysis approach $[1,2,4,7,12,25,32]$ . The major evolution in these studies is to identify financial and economic variables which improve predictive performance. Two statistical techniques appear to have been used the most: discriminant analysis and logistic regression $[6]$ . No technique clearly provides substantially better results. We have chosen to study discriminant analysis as a comparative classification technique because of its repeated use in many other problem areas.

Discriminant analysis is a statistical technique used to classify objects into distinct groups on the basis of an object's observed characteristics. Basically, a linear discriminant function is developed which will compute a “score” for an object. This function is a weighted linear combination of the object's observed values on discriminating characteristics. These weights represent, in essence, the relative importance and impact of the various characteristics. On the basis of its discriminant score, an object is then classified. Often, computer software packages compute the probability of group membership on the basis of this procedure [39].

Multivariate discriminant analysis is subject to a number of restrictive assumptions, including the requirement for the discriminating variables to be jointly multivariate normal. This multivariate normality of the variables is critical to the discriminant analysis procedure; otherwise, results obtained may be erroneous [25]. This theoretical assumption often cannot be realized in practice [4].

## 2.2. Neural network applications

Multi-layer, feed forward neural networks have been applied to many problem domains in and outside the business field. For instance, neural networks have been successfully trained to determine whether loan applications should be approved [20]. Similarly, neural networks have been shown to predict mortgagee applicant solvency better than mortgage writers [11].

Predicting rating of corporate bonds and attempting to predict their profitability is another area where neural networks have been applied successfully $[14,21]$ . Neural networks outperformed regression analysis and other mathematical modeling tools in predicting bond rating and profitability. The main conclusion reached was that neural networks provided a more general framework for connecting financial information of a firm to the respective bond rating.

Fraud prevention is another area of neural network applications in business. Credit card fraud, a costly and difficult problem faced by banks, was addressed by Chase Manhattan Bank of New York by neural networks [33]. These models were shown to be much more successful than traditional regression analysis. Additionally, neural networks have been used in the validation of bank signatures [19,30]. These networks identified forgeries significantly better than any human ‘expert’.

Several people have tested the applicability of neural networks in financial markets. Collard [10] states that this neural network model for commodity trading would have resulted in significant profits over other trading strategies. Kamijo and Tanigawa [24] used a neural network to chart Tokyo Stock Exchange data. Their finding were that the results of the model would beat a 'buy and hold' strategy. Additionally, a neural model for predicting percentage change in the S&P 500 five days ahead using a variety of economic indicators has been developed [18]. The authors claim that the model has provided more accurate prediction than alleged experts in the field using the same indicators.

There have been many other applications of neural networks in non-business related fields such as speech recognition, robotics, radar detection and many others. Additionally, other network paradigms have been useful in solving other types of decision problems. Discussion of these other applications and approaches is beyond the scope of this paper.

Most of the studies which have compared neural networks with statistical techniques report the results on the basis of either a single experiment or in an anecdotal form. There is a need for a thorough comparison using sound statistical procedures. Our study is based on a resampling technique to assess the effectiveness of neural networks on a statistical basis. Further, we borrow some measures from the psychology literature to isolate the value added by a classification technique. We argue that such measures ought to be used in determining alleged superiority of any such model.

## 3. Method

## 3.1. Financial ratios and data collection

The basic intent of this study is to compare and contrast the predictive performance of classical multivariate discriminant analysis to that of neural networks for firm bankruptcy. The Altman study $[1]$ has been used as the standard of comparison for subsequent bankruptcy classification studies using discriminant analysis. Most follow-up studies have identified several other attributes to improve prediction performance. In this exploratory study, we wanted to see if the neural networks can come close to the traditional techniques. More sophisticated inputs to the neural network model should not worsen its performance. Thus, this could establish a lower bound on neural network performance in bankruptcy prediction. For these reasons, we used the same financial ratios as Altman $[1]$ . These ratios were:

$X_{1}$ : Working Capital/Total Assets

$X_{2}$ : Retained Earnings/Total Assets

$X_{3}$ : Earnings before Interest and Taxes/Total Assets

$X_{4}$ : Market Value of Equity/Total Debt

$X_{5}$ : Sales/Total Assets

The sample of firms for which these ratios were obtained consisted of firms that either were in operation or went bankrupt between 1975 and 1982. The sample, obtained from Moody's Industrial Manuals, consisted of a total of 129 firms, 65 of which went bankrupt during the period and 64 non bankrupt firms matched on industry and year. Data used for the bankrupt firms is from the last financial statements issued before the firms declared bankruptcy. Thus, the prediction of bankruptcy is to be made about one year in advance.

## 3.2. Data set generation

In assessing the predictive accuracy of discriminant analysis as compared to neural networks, it is necessary to create two distinct sets of data; a data set to develop the discriminant function (similarly, to train the neural network, often referred to as the training set) and a holdout sample to validate the derived discriminant function (in neural network terminology, the testing set). Because the decision of splitting the original 129 firms could affect the results of the comparison, this study utilizes the concept of Monte Carlo resampling techniques to generate multiple subsamples from the original firms in order to gain a better measure of predictive accuracy (see [37], for example).

The results of this study could be affected by the proportion of non-bankrupt firms to bankrupt firms in both the training and testing sets. That is, the population of all firms contains a certain proportion of firms on the verge of bankruptcy. A proportion of interest in any population is sometimes referred to as the base rate. The base rate may have an impact on a prediction technique's performance in two ways. First, a technique may not work well when the firms of interest (bankrupt) constitute a very small percentage of the population (low base rate). This would be due to a technique's inability to identify the features necessary for classification.

A second effect of the base rate is in terms of differences in base rates between training samples and testing samples. If a classification model is built using a training sample with a certain base rate, does the model still work when the base rate in the test population is different? This issue is important for one more reason. If a classification model based on a certain base rate works across other proportions, it may be possible to build a model using a higher proportion of cases of interest than actually occur in the population.

Table 1  
Number of observations in training and testing sets

<table><tr><td rowspan="2">Training set composition</td><td colspan="3">Testing set composition</td></tr><tr><td>50%/50%</td><td>80%/20%</td><td>90%/10% *</td></tr><tr><td>50%/50%</td><td></td><td></td><td></td></tr><tr><td>TRAIN:</td><td>44/44</td><td>44/44</td><td>44/44</td></tr><tr><td>test:</td><td>20/20</td><td>20/5</td><td>20/2</td></tr><tr><td>80%/20%</td><td></td><td></td><td></td></tr><tr><td>TRAIN:</td><td>44/11</td><td>44/11</td><td>44/11</td></tr><tr><td>test:</td><td>20/20</td><td>20/5</td><td>20/2</td></tr><tr><td>90%/10% *</td><td></td><td></td><td></td></tr><tr><td>TRAIN:</td><td>44/5</td><td>44/5</td><td>44/5</td></tr><tr><td>test:</td><td>20/20</td><td>20/5</td><td>20/2</td></tr></table>

where for each cell:  
TRAIN: (nonbankrupt/bankrupt) firms in training set  
TEST: (nonbankrupt/bankrupt) firms in testing set  
\* Approximately 90%/10% ratio

To study the effects of this proportion on the predictive performance of the two techniques, we created three proportions (or base rates) for each of the training and testing set compositions. The first factor level (or base rate) was a 50/50 proportion of bankruptcy to non bankrupt cases, the second level was a 80/20 proportion (80% non-bankrupt, 20% bankrupt), and the third factor level, an approximate 90/10 proportion (approximately 90% non-bankrupt; this proportion is not exact due to required round-off to integer number of firms). We do not really know the actual proportion of firms going bankrupt. The 80/20 and 90/10 cases should be close. The 50/50 scenario is utilized to investigate the possibility of a better model by using a high base rate in the training set.

Utilizing a full two-factor design, there were nine different experimental cells, whose composition is indicated in Table 1. Within each cell, 20 different training-testing set pairs were generated via Monte Carlo resampling from the original 129 firms. Thus, a total of 180 distinct training and testing data set pairs were generated from the original data. In each case, the training set and test set pairs contained unique firms; i.e., no overlap was allowed. This restriction provides a stronger test of a technique's performance.

## 3.3. Implementation of comparative methods

SYSTAT [39], a personal computer-based statistical package, was used for discriminant analysis. SYSTAT fits the standard multivariate general linear model in performing discriminant analysis and also uses information regarding the prior probability specification of the training set in determining the discriminant function. In this study, the training sets were used to set up initial discriminating functions, which were, in turn, evaluated by the corresponding testing sets. All variables were included in each discriminant analysis conducted in the study. Tests were not undertaken to determine whether the discriminating variables were distributed according to a joint multivariate normal distribution. However, previous research has indicated that neural networks can also perform well in cases of multivariate normal distributions [13]; thus, the distribution of the data used in our study is not a relevant issue in considering robust predictive accuracy.

BRAINMAKER [35], a personal computer-based neural network software package which implements the aforementioned back propagation training algorithm, was used to construct and test trained neural network models. For each network trained in the study, a structure of 5 input neurons (one for each financial ratio), 10 hidden neurons and 2 output neurons (one indicating bankrupt firm, the other indicating non-bankrupt firm) was used. Such a network structure was chosen on the basis of previously espoused heuristic guidelines [8,9,36]. Figure 1 pictorially illustrates this network.

As training cases are presented to the network, the output neuron values are examined by the training procedure. For instance, consider a bankrupt training case that had its bankrupt output node valued at 0.85 and its non-bankrupt node at 0.17. When training a neural network, a certain amount of variation away from the desired values of 0 and 1 (indicating bankrupt or non-bankrupt) is typically allowed at the output layer when determining whether adjustments should be made in network weights via back propagation. This allowable variation is referred to as the training tolerance. Thus, a training tolerance of .2 would allow the training procedure .2 variation of each output node away from the desired value. Thus, the previous example would satisfy the training tolerance (i.e., 1 - 0.85 < 0.2, and 0.17 - 0 < 0.2) and no network weight correction would take place.

![](/api/attachments/BCU4EGQU/fulltext/images/07f5b255d6cc7922147ada0bb45f6e6018cd39b576d1913a3dc03bc66aff08fa.jpg)  
Fig. 1. A typical NN model for bankruptcy prediction.

In training the networks, a heuristic back propagation algorithm was used to ensure convergence (all firms in the training set classified correctly). A stringent training tolerance was initially used in training the network (a small value of 0.1) and gradually relaxed until such a point was reached when all training cases satisfied the training tolerance criteria. Then, the training tolerance was incrementally lowered (made more stringent) and the network was trained until convergence occurred at this level. This was repeated until no further reductions of the training tolerance could occur. In all 180 subsamples generated, the neural network models were able to obtain 100% classifications of the training set cases. By using a relaxed tolerance, memorization or overtraining should have been avoided.

## 3.4. Dependent variable: correct predictions

The intent of this study was to compare the predictive capability of discriminant analysis and neural networks. Thus, the number that each method correctly predicts in the testing data sets is the chief measure of predictive success. Other measures are described as introduced.

SYSTAT, in using the multivariate general linear model, utilizes Mahalanobis distances [39] to calculate posterior probabilities for each case, indicating the likelihood of group membership for each group. Additionally, prior probabilities were incorporated based upon the composition (base rate) of the training sets. The group with the highest posterior probability, therefore, is used as the discriminant analysis prediction for that case. This is the manner in which correct and incorrect classifications were determined for the discriminant analysis method.

When evaluating the predictive capability of neural networks, a testing threshold, similar to training tolerance, is specified. This testing threshold identifies how stringent the allowable variation in output neurons can be when predicting group membership. In this study, a testing threshold of 0.499 was used; thus, if one output neuron exceeded 0.5 (and the other neuron value was <0.5), the network classified the case as the corresponding group associated with the first neuron. Cases where double classifications were indicated (both neurons >0.5) were automatically counted as incorrect classifications. It is on this basis that correct and incorrect classifications were determined for the neural network models.

Each data set was evaluated by both discriminant analysis and neural networks. Two different measures of accuracy could be determined; the number of correct classifications that the particular procedure provided on the training set (“learning”) and the number of correct classifications that the specific procedure provided on the testing set (“generalization”).

## 4. Results

## 4.1. Training sets - "Learning"

The first results to be presented display the learning performance of the discriminant function and the neural network model. Table 2 shows the aggregated percentage of correct classifications of training cases by the two approaches across the three different combinations of training sets. Table 2 also distinguishes between the learning accuracy of non-bankrupt and bankrupt training cases.

It is not surprising that the neural network approach outperforms discriminant analysis, since the neural network training algorithm employed will not cease until all members of the training set are correctly classified. Thus, on the basis of strictly learning a set of bankrupt and non-bankrupt firms, neural networks appear to have learned more than classical multivariate discriminant analysis.

Training set - correct classifications $(\%)$ (grouped by like composition)

<table><tr><td rowspan="2">Training set ratio</td><td colspan="2">Combined accuracy</td><td colspan="2">Non-bankrupt cases</td><td colspan="2">Bankrupt cases</td></tr><tr><td>NN</td><td>DA</td><td>NN</td><td>DA</td><td>NN</td><td>DA</td></tr><tr><td>50/50</td><td>100</td><td>88.65</td><td>100</td><td>94.54</td><td>100</td><td>82.76</td></tr><tr><td>80/20</td><td>100</td><td>90.33</td><td>100</td><td>97.69</td><td>100</td><td>60.91</td></tr><tr><td>90/10</td><td>100</td><td>94.59</td><td>100</td><td>99.13</td><td>100</td><td>54.67</td></tr></table>

NN - Neural network  
DA - Multivariate discriminant analysis

## 4.2. Testing sets - "Generalization"

Perhaps a better measure of accuracy comparison between the two techniques is their performance in classifying cases in the holdout samples, or the testing sets. Table 3 represents the average percentage of correct classifications (irrespective of type of firm) when utilizing the two different techniques to evaluate the 20 holdout samples for each combination of base rates. When the training sets contained an equal number of bankrupt and non-bankrupt cases, and the testing sets also contained an equal number of the two cases, neural networks correctly classified 97.5% of the holdout cases, while multivariate discriminant analysis was correct 88.25% of the time. Similarly, when the training sets contained a balanced number of bankrupt and non-bankrupt firms but the testing sets contained 20 percent bankrupt firms, neural networks classified at a 95.6% correct rate, while discriminant analysis correctly classified 91.8%. Table 3 indicates that in every combination of factor levels neural networks performed better at generalization than discriminant analysis.

Table 3  
Testing set - correct classification $(\%)$ (all cases)

<table><tr><td rowspan="3">Training set composition</td><td colspan="6">Testing set composition</td></tr><tr><td colspan="2">50/50</td><td colspan="2">80/20</td><td colspan="2">90/10</td></tr><tr><td>NN</td><td>DA</td><td>NN</td><td>DA</td><td>NN</td><td>DA</td></tr><tr><td rowspan="2">50/50</td><td>97.5**</td><td>88.25</td><td>95.6**</td><td>91.8</td><td>95.68*</td><td>93.32</td></tr><tr><td colspan="2">(p &lt; 0.001)</td><td colspan="2">(p = 0.005)</td><td colspan="2">(p = 0.046)</td></tr><tr><td rowspan="2">80/20</td><td>82.0**</td><td>75.875</td><td>91.0</td><td>89.0</td><td>95.68**</td><td>91.59</td></tr><tr><td colspan="2">(p = 0.002)</td><td colspan="2">(p = 0.126)</td><td colspan="2">(p = 0.001)</td></tr><tr><td rowspan="2">90/10</td><td>72.625</td><td>72.0</td><td>86.25</td><td>85.8</td><td>94.55**</td><td>91.81</td></tr><tr><td colspan="2">(p = 0.318)</td><td colspan="2">(p = 0.069)</td><td colspan="2">(p = 0.008)</td></tr></table>

\* -Significant at 0.05 level  
\*\*-Significant at 0.01 level

Table 4  
Testing set - correct classifications $(\%)$ bankrupt cases

<table><tr><td rowspan="3">Training set composition</td><td colspan="6">Testing set composition</td></tr><tr><td colspan="2">50/50</td><td colspan="2">80/20</td><td colspan="2">90/10</td></tr><tr><td>NN</td><td>DA</td><td>NN</td><td>DA</td><td>NN</td><td>DA</td></tr><tr><td rowspan="2">50/50</td><td>97.0**</td><td>79.75</td><td>92.0**</td><td>82.0</td><td>92.5</td><td>90.0</td></tr><tr><td colspan="2">(p &lt; 0.001)</td><td colspan="2">(p = 0.025)</td><td colspan="2">(p = 0.282)</td></tr><tr><td rowspan="2">80/20</td><td>62.25**</td><td>54.25</td><td>62.0</td><td>54.0</td><td>70.0**</td><td>45.0</td></tr><tr><td colspan="2">(p = 0.002)</td><td colspan="2">(p = 0.115)</td><td colspan="2">(p = 0.06)</td></tr><tr><td rowspan="2">90/10</td><td>47.00</td><td>46.25</td><td>49.0</td><td>35.0</td><td>67.5**</td><td>45.0</td></tr><tr><td colspan="2">(p = 0.439)</td><td colspan="2">(p = 0.022)</td><td colspan="2">(p = 0.036)</td></tr></table>

A non-parametric test, the Wilcoxon test for paired observations, was undertaken to assess whether the different correct classification percentages for the two different techniques were significantly different. The critical values of this test are also reported in Table 3. Those experimental cells that are statistically significant are highlighted by asterisks. In general, neural networks were statistically significant better predictors of firm bankruptcies in the holdout sample than discriminant analysis.

Tables 4 and 5 provide a more detailed look at the classification results, breaking down the correct percentages in terms of bankrupt firm predictions and non-bankrupt firm predictions. It is apparent from Table 4 that it is in the classification of bankrupt firms where neural networks significantly outperform discriminant analysis. This is important since it is widely accepted in terms of predicting bankrupt firms that it is more costly to classify a failed firm as non-failing than the converse [38].

As with the overall aggregate classification data, the Wilcoxon paired observation test was used to assess the significance of the differences of the two prediction techniques. The critical values of this test are given, and those significant noted by asterisks. Again, for predicting bankrupt cases, note that neural networks predicted better than discriminant analysis at every factor level combination. For instance, where training and test set composition was equal among the two different classes of firms, neural networks correctly predicted 97.0% of the bankrupt firms, while discriminant analysis predicted only 79.75%.

Table 5  
Testing set - correct classifications $(\%)$ non-bankrupt cases

<table><tr><td rowspan="3">Training set composition</td><td colspan="6">Testing set composition</td></tr><tr><td colspan="2">50/50</td><td colspan="2">80/20</td><td colspan="2">90/10</td></tr><tr><td>NN</td><td>DA</td><td>NN</td><td>DA</td><td>NN</td><td>DA</td></tr><tr><td rowspan="2">50/50</td><td>98.0*</td><td>96.75</td><td>96.5</td><td>94.25</td><td>96.0*</td><td>93.5</td></tr><tr><td colspan="2">(p &lt; 0.029)</td><td colspan="2">(p = 0.071)</td><td colspan="2">(p = 0.038)</td></tr><tr><td>80/20</td><td>98.75(p = 0.080)</td><td>97.5</td><td>98.25(p = 0.304)</td><td>97.75</td><td>98.25(p = 0.061)</td><td>92.5</td></tr><tr><td>90/10</td><td>98.25(p = 0.240)</td><td>97.75</td><td>98.0(p = 0.263)</td><td>98.5</td><td>97.25(p = 0.289)</td><td>96.5</td></tr></table>

\* - Significant at 0.05 level  
\*\* - Significant at 0.01 level

Similarly, Table 5 presents the results for the prediction of non-bankrupt cases by the two techniques. Significance is tested and reported as mentioned previously. Both methods appear to predict non-bankrupt firms quite well, though the neural network model predicts better than discriminant analysis in all but a single combination of factor levels (training set of 90-10, testing set of 80-20, and the difference is negligible and statistically not significant).

Table 6 summarizes the prediction classification results for all test sets at each level of the training set base rate and also differentiates between the different categories of firms. From this and the previous tables, it is apparent that neural networks represent a better predictive approach than multivariate discriminant analysis. When considering all 60 cases where a balanced training set was used, the neural network model correctly predicted 95.74% of the bankrupt firms and 96.83% of the non-bankrupt firms in the holdout samples; as compared to 80.92% of bankrupt firms and 94.83% of non-bankrupt firms that discriminant analysis predicted. While the percentage of correct classifications of bankrupt firms decreased with the increased imbalance of the training cases, the general trend of neural network prediction superiority remained.

Table 6  
Training composition effect on classification (%)

<table><tr><td rowspan="2">Training set composition</td><td colspan="2">Bankrupt cases</td><td colspan="2">Non-bankrupt cases</td><td colspan="2">Total cases</td></tr><tr><td>NN</td><td>DA</td><td>NN</td><td>DA</td><td>NN</td><td>DA</td></tr><tr><td>50/50</td><td>95.74</td><td>80.92</td><td>96.83</td><td>94.83</td><td>96.49</td><td>90.51</td></tr><tr><td>80/20</td><td>65.00</td><td>53.52</td><td>98.42</td><td>95.92</td><td>88.05</td><td>82.76</td></tr><tr><td>90/10</td><td>48.89</td><td>44.07</td><td>97.83</td><td>97.58</td><td>82.64</td><td>80.97</td></tr><tr><td></td><td></td><td></td><td colspan="2">Total overall cases</td><td>90.56</td><td>85.87</td></tr></table>

## 4.3 Further assessment of predictive capabilities

While the results have clearly shown that neural networks outperformed discriminant analysis in predicting firm bankruptcies, our study must now address whether the neural network prediction results are better than what can be expected by pure chance $[22,31]$ . We will employ tests originally proposed in $[29]$ and further clarified in $[22]$ for studying discriminant analysis classification rates. Because our study uses cross-validation (i.e., testing sets) for measuring classification success and utilizes different base rates for the training and testing set, we will further modify these tests to fit our study.

The underlying concept in comparing a classification or prediction technique to pure chance is to consider what one could do by simply guessing at the predictions. For instance, if the base rate was 50% for a two group problem, guessing would result, in average, 50% correct predictions. Similarly, if the base rate was skewed (80%-20%), one could blindly predict with 80% accuracy by predicting all cases to belong to the more frequent class [28,29]. It has been shown that to achieve significant levels of predictive validity, the proportion of correct positive predictions (bankrupt firms, in our case) to all positive bankrupt predictions must exceed the base rate of the more frequent class [17,29].

In Table 7, this proportion is calculated for both neural networks and discriminant analysis. Thus, when both the training and testing sets contained a balanced number of bankrupt and non-bankrupt firms (base rate of 50%), a neural network model forecasting a bankrupt firm was correct 98% of the time, while discriminant analysis was correct 94.9%. Note that neural networks outperformed discriminant analysis irrespective of factor levels (base rates). Also note that, with the exception of measuring prediction with test sets having 90 percent non-bankrupt firms, neural networks also exceeded the base rate of the most frequent class, indicative of good predictive validity.

Table 7  
Percent predicted as bankrupt that were bankrupt

<table><tr><td rowspan="3">Training set composition</td><td colspan="6">Testing set composition</td></tr><tr><td colspan="2">50/50</td><td colspan="2">80/20</td><td colspan="2">90/10</td></tr><tr><td>NN</td><td>DA</td><td>NN</td><td>DA</td><td>NN</td><td>DA</td></tr><tr><td>50/50</td><td>98.0</td><td>94.9</td><td>86.8</td><td>78.1</td><td>69.8</td><td>58.1</td></tr><tr><td>80/20</td><td>98.0</td><td>95.6</td><td>89.9</td><td>85.7</td><td>80.0</td><td>37.5</td></tr><tr><td>90/10</td><td>96.4</td><td>95.4</td><td>86.0</td><td>85.4</td><td>71.0</td><td>56.3</td></tr></table>

However, this analysis used the base rates of the testing sets, information not available to the classification technique. Only the base rate of the training set is ‘learned’ by the classification device. Thus, a pure chance technique, exposed to 90% non-bankrupt cases in training, would randomly declare 90% of testing cases to be non-bankrupt, irrespective of the testing set composition. In further investigating the value added by discriminant analysis and neural networks to the classification problem, our standard normal test statistics will be based on only information known to the classification techniques (base rate of the training sets).

The test statistic utilized will be based upon the proportional chance criterion $[22]$ . This criterion implies that prediction by guessing can achieve a correct rate for each group involved equal to the proportion of that group (base rate) in the training set. Thus, for those training sets with a balanced number of bankrupt and non-bankrupt firms, 50% correct predictions could be achieved by chance, while when there are 90% non-bankrupt firms, 90% correct predictions of non-bankrupt firms could be achieved by chance. The following standard normal test statistic is calculated as

$$
\frac {(O - E) * N ^ {1 / 2}}{(E * (N - E)) ^ {1 / 2}},\tag{1}
$$

Predictive validity of classifications

<table><tr><td rowspan="2">Training set composition</td><td colspan="2">Bankrupt</td><td colspan="2">Non-bankrupt</td><td colspan="2">Total</td></tr><tr><td>NN</td><td>DA</td><td>NN</td><td>DA</td><td>NN</td><td>DA</td></tr><tr><td>50/50</td><td>2.88(p = 0.002)</td><td>1.86(p = 0.031)</td><td>4.19(p &lt; 0.001)</td><td>4.00(p &lt; 0.001)</td><td>5.19(p &lt; 0.001)</td><td>4.36(p &lt; 0.001)</td></tr><tr><td>80/20</td><td>3.11(p &lt; 0.001)</td><td>2.31(p = 0.011)</td><td>2.06(p = 0.020)</td><td>1.73(p = 0.042)</td><td>2.57(p = 0.005)</td><td>2.33(p = 0.010)</td></tr><tr><td>90/10</td><td>3.89(p &lt; 0.001)</td><td>3.41(p &lt; 0.001)</td><td>1.17(p = 0.121)</td><td>1.13(p = 0.129)</td><td>1.88(p = 0.030)</td><td>1.70(p = 0.045)</td></tr></table>

where g = groups (bankrupt and non-bankrupt), $n_{g}$ = number of test cases in group g, $b_{g}$ = training base rate of group g, $o_{g}$ = observed correct predictions for group g (refer to Table 4), $e_{g}$ = expected correct predictions for group g by chance ( $n_{g} * b_{g}$ ), O = total correct prediction ( $\Sigma o_{g}$ ), E = total correct predictions obtainable by chance ( $\Sigma e_{g}$ ), N = total number of cases ( $\Sigma n_{g}$ )

Another approach useful in assessing a prediction method is determining how much better a classification approach predicts compared to

Thus, this statistic will indicate whether predictive results obtained by neural networks and discriminant analysis differ greatly from those that can be obtained by chance. Additionally, one can also calculate a similar statistical measure for each separate classification group. Using the same notation as above, the standard normal test statistics for each group (illustrating whether the predictive results obtained by a classification technique significantly differs from chance) is

$$
\frac {\left(o _ {g} - e _ {g}\right) * n _ {g} ^ {1 / 2}}{\left(e _ {g} * \left(n _ {g} - e _ {g}\right)\right) ^ {1 / 2}}.\tag{2}
$$

As Table 8 indicates, the predictive validity of neural networks and discriminant analysis is extremely significant. Aggregately, both methods are significantly better than pure chance regardless of the base rate of the training sets. Considering the predictive validity by specific groups, the only non-significant result occurs when predicting non-bankrupt firms when the training set base rate is 90%, though it is still considerably better than chance. Not surprisingly, as previous results have already shown, neural networks are judged more statistically significant than chance as compared to discriminant analysis in every case.

chance assignment. An index useful in such a setting is the improvement-over-chance or reduction-in-error index [22,26],

$$
I = \frac {H _ {o} - H _ {e}}{1 - H _ {e}},\tag{3}
$$

where $H_{o}$ is the observed rate of correct predictions and $H_{e}$ is the correct prediction rate expected by chance. Using the previous notation, $H_{e}$ is defined as $(\Sigma(b_{g} * n_{g})) / N$ for the aggregate case, and $b_{g}$ for each separate group. The index I represents a reduction-in-error statistic in that 100 \* 1% fewer prediction errors result using the classification rule than would be expected by chance.

Table 9 provides this calculation for the neural network and discriminant analysis predictions aggregately across firm type, as well as the improvement-over-chance index for both bankrupt and non-bankrupt cases. Thus, when the 50-50 training set is used to train a neural network, the network model provides 92.98% fewer classification errors than would occur by blind guessing. Also, as another example, the improvement-over-chance for the prediction of bankrupt firms with neural networks trained on a balanced training set is 91.48%. Also of interest is that even on the 90% base rate where neural networks did not indicate significant differences over chance predictions for non-bankrupt cases, the improvement-over-chance percentage is still a relatively high 78.3%.

Table 9  
Reduction-in-error of classifications

<table><tr><td rowspan="2">Training set composition</td><td colspan="2">Bankrupt</td><td colspan="2">Non-bankrupt</td><td colspan="2">Total</td></tr><tr><td>NN</td><td>DA</td><td>NN</td><td>DA</td><td>NN</td><td>DA</td></tr><tr><td>50/50</td><td>91.5</td><td>61.8</td><td>93.7</td><td>89.7</td><td>93.0</td><td>81.0</td></tr><tr><td>80/20</td><td>56.2</td><td>41.9</td><td>92.1</td><td>79.6</td><td>69.1</td><td>55.4</td></tr><tr><td>90/10</td><td>43.2</td><td>37.8</td><td>78.3</td><td>75.8</td><td>50.2</td><td>45.4</td></tr></table>

Table 10  
ANOVA - Bankrupt cases

<table><tr><td>Source</td><td>Sum of squares</td><td>DF</td><td>Mean-square</td><td>F Ratio</td><td>P</td></tr><tr><td>Train</td><td>49246.942</td><td>2</td><td>24623.471</td><td>49.401</td><td>0.000</td></tr><tr><td>Test</td><td>2663.610</td><td>2</td><td>1331.805</td><td>2.672</td><td>0.072</td></tr><tr><td>Interaction</td><td>3397.222</td><td>4</td><td>349.305</td><td>1.704</td><td>0.151</td></tr><tr><td>Error</td><td>85233.750</td><td>171</td><td>498.443</td><td></td><td></td></tr></table>

$\mathbf{R} = 0.627\mathbf{R}^2 = 0.394$

4.4. Effect of training and testing set composition on generalization

In order to further assess the effect on accuracy of classifications that the factor levels of training and testing set composition have on neural network model predictions, two two-factor ANOVA's were undertaken, one using the percentage of correct classifications of non-bankrupt firms as the dependent variable, another utilizing correct predictions of bankrupt firms as the dependent variable. The results of these two ANOVA's are presented in Tables 10 and 11. Similar analysis was not undertaken for the discriminant analysis results since the neural network approach clearly dominates its' performance.

The composition of the training set was significant in determining the neural network prediction accuracy of the bankrupt test cases. This result further reinforces the intuitive thought that to properly train a network (or any model) to recognize two different concepts, utilizing an equal number of examples of each concept is desirable [23].

Table 11  
ANOVA - Non-bankrupt cases

<table><tr><td>Source</td><td>Sum of squares</td><td>DF</td><td>Mean-square</td><td>F Ratio</td><td>P</td></tr><tr><td>Train</td><td>76.944</td><td>2</td><td>38.472</td><td>3.492</td><td>0.033</td></tr><tr><td>Test</td><td>41.944</td><td>2</td><td>20.972</td><td>1.904</td><td>0.152</td></tr><tr><td>Interaction</td><td>15.556</td><td>4</td><td>3.889</td><td>0.353</td><td>0.842</td></tr><tr><td>Error</td><td>1883.750</td><td>171</td><td>11.016</td><td></td><td></td></tr></table>

$\mathbf{R} = 0.258\mathbf{R}^2 = 0.067$

The moderately significant effect of the testing set composition is not as easily explained. Contrasting the different factor levels, only the difference between the 80/20 and 90/10 evaluation sets were significant (p = 0.0286). From Table 3, it can be seen that similarly trained networks were evaluated more favorable when the testing set was composed of 90 percent non-bankrupt cases and 10 percent bankrupt firms. The 80/20 and 50/50 testing sets showed comparable measures of prediction accuracy across different training factor levels. This variation can perhaps be explained by the small number of bankrupt cases found in the holdout samples of factor level 90/10 (2 cases). By having such a small number of test cases, the random generation of cases may have led to this experimental finding.

Table 11, the ANOVA on the non-bankrupt cases, shows that only the composition of the training set significantly effects neural network predictions. Upon closer contrast analysis among the three different factor levels, the only significant difference between levels is between the 50/50 and 80/20 composition (p = 0.010). In fact, predictive accuracy of networks trained by the 80/20 composition sets provided more accurate results in classifying non-bankrupt cases than the 50/50 training sets.

## 5. Discussion

From the results of this experiment, it is apparent that for the bankruptcy prediction problem, neural networks offer a viable alternative approach. With simple data (five variables), neural networks showed extreme promise by correctly predicting as high as a 97% accuracy level (when both the training and testing base rates were 50/50). This level is as good as or better than other studies. In every instance, neural networks outperformed discriminant analysis in classification accuracy, especially in the prediction of bankrupt firms, the more difficult and, arguably, the more important classification problem [38]. It stands to reason that neural networks will perform as well or better with the inclusion of more variables in the analysis. Thus, the results of this exploratory study could be considered to offer a lower bound on the predictive accuracy one can expect with a neural network model for bankruptcy prediction. Of course, the results of any study are bound by the limitations of the data and methodology.

Discriminant analysis classification rules often incorporate prior probabilities that account for both the assumed base rate and the costs associated with misclassification errors if different $[16,27]$ . In our comparison study, prior probabilities were calculated from the base rates of the training sets. By using the base rates as the prior probabilities, the discriminant analysis procedure in this study actually incorporates significant unequal misclassification costs (i.e., misclassifying a bankrupt firm is a more costly error), since the true population of bankrupt firms is probably less than the training set base rate. Even so, neural networks continually predicted bankrupt firms more accurately using symmetric costs (testing threshold of 0.499). The major dilemma in utilizing the discriminant analysis model is in estimating the unequal misclassification costs. Future research investigating performance adjustments given explicit values for asymmetric misclassification costs for both discriminant analysis and neural networks may be warranted.

The investigation of the effects of different training and testing set composition on the predictive results lead to further implications for the decision maker and neural network researcher. Results indicated that the composition of the training set was a significant determinant of neural network predictive accuracy. Basically, it was shown that neural networks provide better understanding and differentiation between two concepts (bankrupt firms and non-bankrupt firms) when an equal number of examples of each concept is used in the learning procedure. This result is not dissimilar to one's intuition and previous results in discriminant analysis $[23]$ .

While all prediction errors are undesirable in a specific methodology, it is generally accepted that the incorrect prediction of a bankrupt firm as non-bankrupt is the most costly error. Results have indicated that prediction of the bankrupt firms poses the largest problem to the two different techniques. Neural networks were shown to perform well in predicting both bankrupt firms and non-bankrupt firms when presented with equal numbers of examples in the learning phase. Thus, a more accurate classification model will result when developed with an equal number of instances of each category. Since in the real-world, the decision maker may not have control over the composition of historical data necessary in the predictive model development, it appears that “smoothing” the distribution of the training set, irrespective of the actual distribution, will provide a better model.

It is true that neural network performance is less impressive as the proportion of non-bankrupt to bankrupt firms diverge. However, neural network models continue to outperform discriminant analysis. If one follows the recommendation of a 50-50 training set, neural network performance does not deteriorate significantly. Bankrupt firms are predicted correctly in the 92% to 97% range, with similar accuracy for non-bankrupt firms, given a balanced training set.

One caution to this approach in developing the training set is also indicated in the experimental results. Significance of testing set composition in bankrupt firm prediction may have indicated over-reported accuracy due to the small number of bankrupt firms in the 90-10 test sets. Thus, this study indicates that a potential trade-off exists when creating training and testing sets from the pool of existing problem data. A better predictive neural network model can be created by using a balanced training set; however, if too few of the hard-to-classify or more important cases exist in the cross-validation set, the model performance could be over or under reported. Either way, this will significantly effect the accuracy of decision maker confidence in the prediction model.

The results of predicting non-bankrupt cases improved as the imbalance of bankrupt to non-bankrupt firms increased in the training sets. This can be attributed to significant fewer number of bankrupt firms in the training sets. This phenomenon illustrates that, at the expense of “learning” about bankrupt firms, the network “memorizes” and becomes very good at recognizing (i.e., predicting) non-bankrupt firms. While overall predictive accuracy may remain high, the classification accuracy of bankrupt firms is seriously reduced. Thus, one would be significantly sacrificing the prediction performance of one important category to marginally increase the prediction performance on the other, easier predicted category. In firm bankruptcy predictions, this is obviously not desirable. Thus, great care must be taken when creating the training and cross-validation sets when developing a neural network prediction model.

From a decision support systems perspective, this study has illustrated that neural networks are a viable model that should be included in the model base of a DSS. Predictive accuracy obtained in this study illustrates the potential of neural networks from a data reduction standpoint. With only five simple ratios, neural networks predicted at a high rate of classification accuracy; thus, these models may provide excellent results with less data requirements than other approaches to the problem.

Discriminant analysis is not the only tool that has been postulated for use in classification problems $[13]$ . However, all other models do have limitations with regard to successful and appropriate use. In the case of discriminant analysis, limitations include the requirement that the variables should be jointly distributed according to a multivariate normal distribution, prior probability specification, and so forth. Neural networks have no such potential restrictive assumptions or requirements; they are more robust prediction techniques. Thus, neural networks offer additional benefits in reducing managerial concern over choosing the appropriate model in the decision support context.

Much additional research needs to be done regarding neural networks for bankruptcy prediction. The effect of network architecture, network training algorithms and learning paradigms need to be examined to provide more prescriptive results on implementing a neural network prediction model. As previously mentioned, this exploratory study uses only a small amount of variables to achieve its' high level of predictive accuracy; other variables should be included in the neural network model $[2]$ . Notable omissions include the size of the firm, and time series data (more than just one years' previous financial data), among others. Additionally, using matched firms by industry and year has been postulated to bias results in predicting bankruptcy $[40]$ . Neural networks may or may not be affected by this, but additional research should study this issue.

## 6. Conclusion

This paper has compared the predictive capability of neural networks with that of classical multivariate discriminant analysis within the context of forecasting firm bankruptcies on the basis of a small number of financial ratios. In this study, neural networks clearly outperformed discriminant analysis in prediction accuracy of both bankrupt and non-bankrupt firms under varying training and testing conditions. Additionally, it was shown that neural networks offer a significant improvement in prediction over pure chance, and that their use in prediction can reduce errors in this problem domain by as much as 93% over chance.

Neural networks, therefore, represent a classification technique that is a robust and promising approach in the prediction of firm stability. While this study is exploratory in nature and has some limitations as noted, it has shown the promise of neural networks through the use of a set of solid statistical analyses that should be utilized as research continues in this area.

## Acknowledgments

The authors wish to sincerely thank Marcus Odom and Nik Dalal for their help and assistance in data collection and in their insightful comments on previous drafts of this paper. Also, the paper has greatly benefitted from comments and suggestions from the anonymous referees.

## References

[1] Altman, E.I., Financial Ratios, Discriminant Analysis and the Prediction of Corporate Bankruptcy, The Journal of Finance, (September 1968), 589–609.

[2] Altman, E.I., Haldeman, R.G. and Narayanan, P., Zeta Analysis, Journal of Banking and Finance, (June 1977), 22–51.

[3] Altman, E.I., Accounting Implications of Failure Prediction Models, Journal of Accounting Auditing and Finance, (Fall 1982), 4–19.

[4] Baetge, J., Huss, M. and Niehaus, H., The Use of Statistical Analysis To Identify The Financial Strength Of Corporations In Germany, Studies in Banking and Finance, Vol. 7 (1988), 183–196.

[5] Beaver, W.H., Financial Ratios as Predictors of Failure, Empirical Research in Accounting: Selected Studies (1966), 71–111.

[6] Bell, T., Ribar, G. and Verchio, J., Neural Nets vs. Logistic Regression: A Comparison of Each Model's Ability to Predict Commercial Bank Failures, working paper, Peat Marwick Co., (May 1990).

[7] Blum, M., Failing Company Discriminant Analysis, Journal of Accounting Research, (Spring 1974), 1–25.

[8] Caudill, M., Neural Network Primer: Part III, AI Expert, (June 1988) 53–59.

[9] Caudill, M., Neural Network Training Tips and Techniques, AI Expert, (January 1991), 53–59.

[10] Collard, J.E., Commodity Trading with a Neural Net, Neural Network News, Vol. 2, No. 10 (October, 1990).

[11] Collins, E., Ghosh, S. and Scofield, C., An Application of a Multiple Neural Network Learning System to Emulation of Mortgage Underwriting Judgments, working paper, Nestor, Inc. (1989).

[12] Deakin, E.B., A Discriminant Analysis of Predictors of Business Failures, Journal of Accounting Research, (Spring 1972), 167–179.

[13] Denton, J., Hung, M. and Osyk, B., A Neural Network Approach to the Classification Problem, Expert Systems With Applications, Vol. 1, (1990), 417–424.

[14] Dutta, S. and Shekhar, S., Bond-Rating: A Non-Conservative Application of Neural Networks, Proceedings of the IEEE International Conference on Neural Networks, San Diego, (1988) 443–450.

[15] Eisenbeis, R. and Avery, R., Discriminant Analysis and Classification Procedures. (Lexington Books, Lexington MA, 1972).

[16] Eisenbeis, R., Pitfalls in the Application of Discriminant Analysis in Business, Finance and Accounting, Journal of Finance, (June 1977) 875–900.

[17] Farrington D.P. and Tarling, R., Prediction in Criminology. (State University of New York Press, Albany, NY, 1985).

[18] Fishman, M., Barr, D. and Loick, W., Using Neural Networks in Market Analysis, Technical Analysis of Stocks and Commodities, (April 1991) 18–25.

[19] Francett, B., Neural Nets Arrive, Computer Decisions, (Jan. 1989) 58–62.

[20] Gallant, S.I., Connectionist Expert Systems, Communications of the ACM, (February 1988), 152–169.

[21] Goodman, R.M., Miller, J.W. and Smyth, P., An Information Theoretic Approach to Rule-Based Connectionist Systems, in Advances in Neural Information Processing Systems I, D.S. Touretsky ed., (Kaufman Publishing: San Mateo, CA, 1989) 356–364.

[22] Huberty, C.J., Issues in the Use and Interpretation of Discriminant Analysis, Psychological Bulletin, Vol 95 (1984), 156–171.

[23] Jain, A. and Chandrasekaran, B., Dimensionality and Sample Size Considerations in Pattern Recognition Practice, in Handbook of Statistics, Vol. 2, P. Krishnaiah and Kanal, L. eds. (North-Holland, 1982), 835–855.

[24] Kamijo, K. and Tanigawa, T., Stock Price Pattern Recognition: A Recurrent Neural Network Approach, International Joint Conference on Neural Networks, San Diego, (June 1990).

[25] Karels, G.V. and Prakash, A., Multivariate Normality and Forecasting of Business Bankruptcy, Journal of Business Finance and Accounting, (Winter 1987), 573–593.

[26] Klecka, W.R., Discriminant Analysis. (Sage Publishing: Beverly Hills, CA, 1980).

[27] Lachenbruch, P., Discriminant Analysis. (Hafner Press: NY, NY, 1975).

[28] Meehl, P.E., Clinical versus Statistical Prediction: A Theoretical Analysis and a Review of the Evidence. (University of Minnesota Press: Minneapolis, 1954).

[29] Meehl, P.E. and Rosen, A., Antecedent Probability and the Efficiency of Psychometric Signs, Patterns or Cutting Scores, Psychological Bulletin, 52, (1955) 194–216.

[30] Mighell, D., Back-Propagation and its Application to Handwritten Signature Verification, in Advances in Neural Information Processing Systems I, D.S. Touretsky ed. (Kaufman Publishing: San Mateo, CA, 1989) 340–347.

[31] Morrison, D.G., On the Interpretation of Discriminant Analysis, Journal of Marketing Research, Vol. 6, (1969), 156–163.

[32] Moyer, R.C., Forecasting Financial Failure: A Reexamination, Financial Management, (Spring 1977), 11–17.

[33] Rochester, J. (ed.) New Business Uses For Neurocomputing, I/S Analyzer, (Feb 1990), 1–17.

[34] Siegel, J.G., Warning Signs of Impending Business Failure and Means to Counteract such Prospective Failure, The National Public Accountant, (April 1981), 9–13.

[35] Stanley, J. and Bak, E., Introduction to Neural Networks. (California Scientific Software, Sierra Madre, CA, 1989).

[36] Surkan, A. and Singleton, J., Neural Networks For Bond Rating Improved by Multiple Hidden Layers, International Joint Conference on Neural Networks, San Diego, (June 1990).

[37] Teebagy, N. and Chatterjee, S., Inference in a Binary Response Model with Applications to Data Analysis, Decision Sciences, Vol. 20, No. 2, (1989), 393–403.

[38] Watts, R.L. and Zimmerman, J.L., Positive Accounting Theory. (Prentice-Hall, 1986).

[39] Wilkinson, L., SYSTAT: The System for Statistics. (SYSTAT, Inc., Evanston, IL, 1989).

[40] Zmijewski, M.E., Methodological Issues Related to the Estimation of Financial Distress Prediction Models, Journal of Accounting Research, Vol. 22 Supplement (1984), 59–82.
