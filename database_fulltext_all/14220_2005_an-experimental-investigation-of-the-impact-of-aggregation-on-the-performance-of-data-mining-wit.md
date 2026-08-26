---
otero_id: 14220
otero_key: "WERBVYXF"
title: "An experimental investigation of the impact of aggregation on the performance of data mining with logistic regression"
authors: "Adam Fadlalla"
year: "2005"
journal: "Information & Management"
doi: "10.1016/j.im.2004.04.005"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An experimental investigation of the impact of aggregation on the performance of data mining with logistic regression

Adam Fadlalla

Department of Computer and Information Science, Cleveland State University, Cleveland, OH 44114, USA

Received 17 October 2002; received in revised form 8 April 2004; accepted 25 April 2004 Available online 24 July 2004

## Abstract

We studied the impact of data aggregation on the performance of logistic regression on predicting the direction of the Dow Jones industrial average (DJIA) stock market index. Data aggregation is a common operation in business, science, engineering, medicine, etc.; it is performed for purposes such as statistical, financial, and sales and marketing analysis — particularly within the context of a data warehouse. We showed experimentally that, for this example, as long as aggregation does not shrink the sample size unduly, it does not significantly impair the performance of the logistic regression model for predicting the direction of the DJIA stock market index. We also observed that aggregation-based models are simpler (less over-parameterized) than detail-based models. We used the receiver operating characteristic (ROC) analysis to evaluate the robustness of such predictive models. Specifically, we used the area under the ROC curve as a summary measure of the overall performance of a given model.

<sup>#</sup> 2004 Elsevier B.V. All rights reserved.

Keywords: Data mining; Aggregation; Logistic regression; Prediction; Predictive modeling; DJIA; ROC; Area under the ROC curve; Model assessment; Model performance; Data warehouse

## 1. Introduction

Data aggregation here refers to any data roll-up process, such as averaging and summing, in which information is expressed in a summary form. It is a common practice in various disciplines; including business, science, engineering, and medicine. Aggregation is performed for purposes such as statistical, financial, and sales and marketing analysis. The impact of data aggregation on the performance of data mining algorithms is of particular relevance to business data within a data warehouse, which we define here as a repository of data that is clean, integrated, complete, and summarized and thus ‘‘sets the stage for effective data mining’’ [16]. Thus understanding the implications of data aggregation on data mining algorithms is of considerable importance for the proper utilization of such data assets.

<table><tr><td colspan="9">(a)</td></tr><tr><td>Price on day 1</td><td>Price on day 2</td><td>Price on day 3</td><td>Price on day 4</td><td>Price on day 5</td><td>Price on day 6</td><td>Price on day 7</td><td>Price on day 8</td><td>...</td></tr><tr><td colspan="9">(b)</td></tr><tr><td colspan="4">Average Price for days 1, 2, 3, 4</td><td colspan="4">Average Price for days 5, 6, 7, 8</td><td>...</td></tr></table>

Fig. 1. (a) Detail-based predictions vs. (b) 4 days aggregation-based predictions.

## 2. Background

## 2.1. Mining the data warehouse

Data warehousing has become a well-established field but numerous definitions of it exist in the literature [8,10,23,42,47,48]. Possibly the most classical definition [17] is a ‘‘subject-oriented, integrated, timevarying, non-volatile collection of data that is used primarily in organizational decision making.’’ From a user’s perspective, a data warehouse should be a collection of cleaned, integrated, summarized data that is available for on-line analytical queries and decision making [48].

Data warehousing formats the data for analytical customer relationship management, data mining, and other business intelligence processes [2,6,15,36]. Quality of data, as in all serious information systems, is important [14]: data mining tools need to work on integrated, consistent, and cleaned data. A data warehouse, however, is not a prerequisite for data mining; rather, it is an effective enabler for it.

## 2.2. Why aggregation?

Data aggregation is a fact of business. Vast amounts of summarized data exist. Its need stems from business analysis considerations, efficiency requirements, etc.

Business analysis considerations: Business decisions vary across the organizational hierarchy — from the operational level, to the control level, and to the executive level. Accordingly, information requirements differ in many aspects, such as, the degree of information detail/aggregation, its source, and its time span. Many decisions require aggregated information.

Aggregation must also fit the needs of the user because some ‘‘will require more extensive data for greater analysis while others will require more summarized data for quicker analysis’’ [22]. The needed aggregation level is thus domain-specific.

Raw detailed data is gathered from operational and possibly non-integrated legacy applications, cleaned, and then presented in the proper aggregated format, within the specific business domain. Aggregation has business rationale — it reflects the ‘‘big picture’’ by reducing dimensionality for better comprehensibility [9] and decision-making process [32]. The major shortcoming of aggregation is the loss of detail, but often the detail is preserved, possibly offline.

Moreover, aggregation enables predictions that go beyond a low granularity. Aggregation-based prediction enables prediction of performance (for sales, stock market index, inventory level, etc.) over the following n days, where n is a function of the aggregation level. For example, using a prediction based on 4- day averages, a given predicted price represents the aggregate (average) price for the next 4 days rather than the single price for the next day. In many business situations, predicting for more than a single day may be frequently needed and more appropriate for the situation. Fig. 1 illustrates the contrast between detailbased (daily) predictions and aggregation-based (4- day average) predictions.

Efficiency requirements: In addition to business considerations, data aggregation is used to save storage space and to provide faster response to analytical queries. The amount of data captured by businesses is ever expanding and can be illustrated by the following example from Amazon.com [44]:

<table><tr><td>Levels of aggregation and analysis</td><td>New data per day</td></tr><tr><td>Web page presentation level</td><td>10+ TB</td></tr><tr><td>Click level</td><td>100 GB, ..., 1 TB</td></tr><tr><td>Session level</td><td>1, ..., 10 GB</td></tr><tr><td>Purchase level</td><td>100, ..., 100 MB</td></tr><tr><td>Customer level</td><td>1 MB</td></tr></table>

To handle the exploding data volume, data warehouse designers must make use of partitioning and aggregation techniques [27]. In some sense, aggregation is a form of data compression. ‘‘Data aggregates are a special kind of aggregate view that improves query execution times by pre-calculating expensive joins and aggregation operations prior to execution and storing the results in a table in the database’’ [33].

Aggregation can have other business justifications. For example, banks and insurance companies aggregate accounts into household units, so that each household receives consistent promotional and marketing material [24]. Aggregation can also be performed to ensure privacy; for example, ‘‘raw socio-demographic, exam, and questionnaire data will not be released for single years of the survey because of concerns about protecting subject confidentiality.’’ [41].

## 2.3. Mining the detail versus mining the aggregation

Data mining could be performed on detailed or on aggregated data. Detail-based data mining may be very resource-intensive. ‘‘Data warehouses starting at 200 GB are no longer rare, yet, at best, our tools can deal with 1 GB at a time.’’ [3]. Mining the vast detail may also lead to random patterns that have statistical backing but do not have business backing. For example, ‘‘it is all too easy to ‘‘find’’ a phenomenon or pattern that looks impressive, even when there is nothing to discover.’’ [35].

Alternatively, aspects of sampling have to be carefully considered — for example, which technique to use to ensure that the sample truly represents the population, etc. [45,46].

Data aggregation may, however, obscure important relationships in the data. In some situations, aggregation may also reduce the noise in the data by smoothing its variability.

## 2.4. Sample problem and data

The problem used here is the prediction of the DJIA stock market index. The stock market is extremely hard to predict, because there are many factors that impact it (economic, social, political) and even investor emotions and whims. In fact, many believe that the behavior is best described as a random walk [25].

We treat the market prediction task as a binary classification problem. Specifically, we predict that the DJIA will move into one of two directions or events, up or down. For example, given today’s prices and volume, total shares traded on a given day, we attempt to predict whether the DJIA will close up (or stay the same) or down on the next day. At the aggregate data level, given n-day average prices and volume, we predict whether the DJIA will on average close up (or the same) or down for the next n days. We are assuming that the various prices and volume are good predictors for the up or down movement of the market index. The data relationships show high correlation between open-, low-, high-price, and volume on one hand and closing price on the other. Obviously the up and down movement of the DJIA are surrogate measures of its closing price.

A more concise statement of the problem is:

$$
\mathrm{UD} _ {t + 1} = f \left(O _ {t}, L _ {t}, H _ {t}, V _ {t}\right),
$$

where $\mathrm { U D } _ { t + 1 } =$ predicted market up/down movement at time t + 1, O = opening price at time $t , L _ { t } = \mathrm { l o w e s t }$ price at time $t , H _ { t } = \mathrm { h i g h e s t }$ price at time $t , V _ { t } = \mathrm { v o l u m e }$ at time t.

Since the problem is formulated as a binary classification, then $\mathrm { U D } _ { t + 1 } \in \{ \mathrm { D } , \mathrm { U } \}$ where, D indicates that the market will close down and U indicates that it will close up compared to the previous time period t.

The up and down values for historical data are derived as follows: $\mathrm { U D } _ { t } = \mathrm { U }$ if $C _ { t } \geq C _ { t - 1 }$ and $\mathrm { U D } _ { t } = \mathrm { D }$ if $C _ { t } < C _ { t - 1 }$ , where $\mathrm { U D } _ { t }$ is the direction of the market index at time $t , C _ { t }$ is its closing price at time t, and $C _ { t - 1 }$ is its closing price at time $t - 1$ ; hence, the up/down direction is a surrogate measure of the closing price.

We downloaded the daily data on the DJIA market index from the following Internet sources: <http:// moneycentral.msn.com>, <http://finance.yahoo.com>.

The data downloaded was for the period 1 December 1995 to 31 December 2000. The structure and type of the downloaded data is shown in Table 1.

The data for December 1995 was downloaded to identify the up/down direction of the first trading period. We merged the two data sets into one data set with six attributes: Date, Open, Low, High, Close, and Volume. We added the attribute (UD) to represent the up/down direction.

We scaled down the open, low, high, and close prices by 100 and the volume by 10,000,000 to bring the numbers within smaller, more readable, ranges, a form of data normalization. We then aggregated the data using 2-, 3-, and 4-day averages. The 2-day average represents two trading days simple, not moving, average of the market parameters. Eq. (1) shows how these averages were calculated.

Table 1  
Downloaded data sets and the experimental data set created from them

<table><tr><td colspan="2">Data set downloaded from http://moneycentral.msn.com</td><td colspan="2">Data set downloaded from http:// finance.yahoo.com</td></tr><tr><td>Date</td><td>MMDDYYYY</td><td>Date</td><td>MMDDYYYY</td></tr><tr><td>High</td><td>Decimal</td><td>Open</td><td>Decimal</td></tr><tr><td>Low</td><td>Decimal</td><td>High</td><td>Decimal</td></tr><tr><td>Close</td><td>Decimal</td><td>Low</td><td>Decimal</td></tr><tr><td>Volume</td><td>Large integer</td><td>Close</td><td>Decimal</td></tr></table>

<table><tr><td colspan="2">Expanded/merged data set from Microsoft and Yahoo data sets</td></tr><tr><td>Date</td><td>MMDDYYYY</td></tr><tr><td>Open</td><td>Decimal</td></tr><tr><td>Low</td><td>Decimal</td></tr><tr><td>High</td><td>Decimal</td></tr><tr><td>Close</td><td>Decimal</td></tr><tr><td>Volume</td><td>Large integer</td></tr><tr><td>UD</td><td>Character</td></tr></table>

Table 2  
Data volumes for the daily, 2-, 3-, and 4-day aggregation levels for the period 1 January 1996–31 December 2000

<table><tr><td>Aggregation granularity</td><td>Number of records</td></tr><tr><td>1-day</td><td>1263</td></tr><tr><td>2-day</td><td>632</td></tr><tr><td>3-day</td><td>421</td></tr><tr><td>4-day</td><td>316</td></tr></table>

$$
A _ {k j} = \frac {1}{k} \sum_ {i = (j - 1) k + 1} ^ {j k} x _ {i}\tag{1}
$$

where $A _ { k j }$ is the jth average value of the aggregated variable when we are aggregating every k days. $x _ { i }$ is the ith detail value of the aggregated variable.

Table 2 shows the data volumes for each of the aggregation granularities.

## 3. Methodology

The following outlines our experimental framework:

(1) Prepare the data.

(2) Partition the data into a 40% random sample for training the model, a 30% random sample for validating the model, and a 30% random sample for testing the model.

(3) Derive a logistic regression model from the detail data to classify the up and down events.

(4) Create 2-day aggregations (averages) from the detailed data, and derive a model as in step 3.

(5) Create 3-day aggregations (averages) from the detailed data, and derive a model as in step 3.

(6) Create 4-day aggregations (averages) from the detailed data, and derive a model as in step 3.

(7) Use the receiver operating characteristic (ROC) curve analysis to assess the individual as well as the comparative performance of these models.

## Fig. 2 summarizes this experimental framework.

## 3.1. Impact of aggregation on basic data characteristics

Apparently there is a relationship between the performance of data mining algorithms and the data characteristics; research has focused mainly on the impact of class distributions on model learning [7,18,20,21,34]. Researchers have also examined the amount of data needed to develop effective predictive models [43]. However, nothing apparently addresses our specific question of the impact of aggregation on the performance of data mining algorithms. In particular, the basic data characteristics we examined were:

 mean;

 standard deviation;

 coefficient of variation (CV); the ratio of the standard deviation to the mean and a measure of relative variability;

 skewness;

 kurtosis; and

 normality (the conformance to a normal distribution), one measure of conformance is the Kolmogorov–Smirnov index.

Side effects of aggregation on data characteristics, if they exist, may contribute to the variation, if any, in the performance of the algorithm when used to mine detail data versus aggregation data; then the variation in algorithm performance may not be fully attributed to aggregation.

![](/api/attachments/WERBVYXF/fulltext/images/668f871b6b352e78ee495a6e2cc44e91047b12675f95e7d1e70f7601fec99c80.jpg)  
Fig. 2. Overview of the experimental framework.

To isolate such side effects, if they exist, we compared the basic characteristics of the aggregated data to the basic characteristics of the detail data. As seen from Table 3, all the variables (Open, Low, High, Volume, Close) maintained the same basic characteristics before aggregation (1-day) and after aggregation (2-, 3-, and 4-day). Therefore, the aggregation process – averaging in this case – has no side effects on the basic characteristics of the data.

## 3.2. Impact of aggregation on the size of the data and the distribution of the target class

A smaller data size due to aggregation, in and by itself, is not a problem for prediction algorithms, unless the data set becomes statistically too small (less than 30). The ratio of the down event, the target class in our case, became smaller with higher aggregation levels as shown by the second column in Table 4 which also shows the number of rows in each data set and the amount (and percent) allocated to each of the training, validation, and test subsets used in deriving the model. An imbalance exists at the detail data level (46.6% down), but the imbalance increased with higher aggregation levels (for example, 41.8% down for the 4-day aggregation). The increased imbalance may be explained by a general upward trend in the DJIA over the experimental period. Imbalances in the distribution of the target class impact the accuracy of the predictive model.

However, imbalance between the up and down classes in our experiment is not as drastic as imbalances in some previous research.

## 3.3. Which aggregation function to use?

Data can be aggregated with many functions. The SQL-92 standard provides five functions to aggregate the data values in a table: COUNT( ), SUM( ), MIN( ), MAX( ), and AVG( ). Beyond these standard aggregation functions, median, standard deviation, variance; financial aggregation functions such as net present value, internal rate of return, future value; and other domain-specific aggregation functions are used. The most commonly used aggregation functions in data warehouses are the average and the sum. It does not matter to the predictive model, logistic regression in this case, whether the sum or the average aggregation function is used. Sums are calculated as follows:

Table 3  
Detailed vs. aggregated data: basic characteristics

<table><tr><td>Variable</td><td>Aggregation level</td><td>Mean</td><td>Standard deviation</td><td>Skewness</td><td>Kurtosis</td><td>Coefficient of variation</td><td>Kolmogorov-Smirnov (P=0.01)</td></tr><tr><td rowspan="4">Open</td><td>1-day</td><td>86.0</td><td>19.4</td><td>-0.2</td><td>-1.3</td><td>0.2</td><td>0.1</td></tr><tr><td>2-day</td><td>85.9</td><td>19.4</td><td>-0.2</td><td>-1.3</td><td>0.2</td><td>0.1</td></tr><tr><td>3-day</td><td>86.0</td><td>19.4</td><td>-0.2</td><td>-1.3</td><td>0.2</td><td>0.1</td></tr><tr><td>4-day</td><td>85.9</td><td>19.4</td><td>-0.2</td><td>-1.3</td><td>0.2</td><td>0.1</td></tr><tr><td rowspan="4">Low</td><td>1-day</td><td>84.8</td><td>19.0</td><td>-0.2</td><td>-1.3</td><td>0.2</td><td>0.1</td></tr><tr><td>2-day</td><td>84.7</td><td>19.0</td><td>-0.2</td><td>-1.3</td><td>0.2</td><td>0.1</td></tr><tr><td>3-day</td><td>84.8</td><td>19.0</td><td>-0.2</td><td>-1.3</td><td>0.2</td><td>0.1</td></tr><tr><td>4-day</td><td>84.7</td><td>19.0</td><td>-0.2</td><td>-1.3</td><td>0.2</td><td>0.1</td></tr><tr><td rowspan="4">High</td><td>1-day</td><td>87.2</td><td>19.9</td><td>-0.2</td><td>-1.3</td><td>0.2</td><td>0.1</td></tr><tr><td>2-day</td><td>87.1</td><td>19.9</td><td>-0.2</td><td>-1.3</td><td>0.2</td><td>0.1</td></tr><tr><td>3-day</td><td>87.2</td><td>19.9</td><td>-0.2</td><td>-1.3</td><td>0.2</td><td>0.1</td></tr><tr><td>4-day</td><td>87.1</td><td>19.9</td><td>-0.2</td><td>-1.3</td><td>0.2</td><td>0.1</td></tr><tr><td rowspan="4">Volume</td><td>1-day</td><td>68.8</td><td>24.9</td><td>0.6</td><td>-0.2</td><td>0.4</td><td>0.1</td></tr><tr><td>2-day</td><td>68.7</td><td>24.1</td><td>0.5</td><td>-0.5</td><td>0.4</td><td>0.1</td></tr><tr><td>3-day</td><td>68.7</td><td>23.7</td><td>0.5</td><td>-0.6</td><td>0.3</td><td>0.1</td></tr><tr><td>4-day</td><td>68.7</td><td>23.4</td><td>0.5</td><td>-0.7</td><td>0.3</td><td>0.1</td></tr><tr><td rowspan="4">Close</td><td>1-day</td><td>86.0</td><td>19.4</td><td>-0.2</td><td>-1.3</td><td>0.2</td><td>0.1</td></tr><tr><td>2-day</td><td>85.9</td><td>19.4</td><td>-0.2</td><td>-1.3</td><td>0.2</td><td>0.1</td></tr><tr><td>3-day</td><td>86.0</td><td>19.4</td><td>-0.2</td><td>-1.3</td><td>0.2</td><td>0.1.</td></tr><tr><td>4-day</td><td>85.9</td><td>19.4</td><td>-0.2</td><td>-1.3</td><td>0.2</td><td>0.1</td></tr></table>

$$
S _ {k j} = \sum_ {i = (j - 1) k + 1} ^ {j k} x _ {i}\tag{2}
$$

where $S _ { k j }$ is the jth sum of the aggregated variable when we are aggregating every k days. $x _ { i }$ is the ith detail value of the aggregated variable.

## 3.4. The logistic regression model

Logistic regression is a popular data mining technique because, in part, it enables the researcher to overcome many of the restrictive assumptions of ordinary linear regression. For example, logistic regression makes none of the following assumptions:

 linear relationship between the dependent and the independent variables;

 normal distribution of the dependent variable(s); and

 normal distribution of the error terms.

Logistic regression utilizes a binary dependent variable. It attempts to predict the probability that a binary target, in this case the direction of the DJIA market index, will acquire the event of interest, in this case the DJIA moving down, as a function of one or more independent variables: opening price, lowest price, highest price, and volume. These independent variables are termed x collectively. Given x, and if $p \ = \ \mathrm { p r o b a b i l i t y } \ ( \mathrm { D J I A } \ = \ \mathrm { d o w n } | x )$ is the probability to be modeled, then the linear logistic model is,

Table 4  
Size and percentage of the down, up, training, validation, and testing cases

<table><tr><td>Aggregation level</td><td>Number down (%)</td><td>Number up (%)</td><td>Total rows</td><td>Size (%), number down, and number up of training set</td><td>Size (%) of validation set</td><td>Size (%) of testing set</td></tr><tr><td>1-day</td><td>587 (46.6)</td><td>675 (53.4)</td><td>1263</td><td>505 (40): 232D, 273U</td><td>379 (30)</td><td>379 (30)</td></tr><tr><td>2-day</td><td>274 (43.4)</td><td>358 (56.6)</td><td>632</td><td>253 (40): 121D, 132U</td><td>190 (30)</td><td>190 (30)</td></tr><tr><td>3-day</td><td>178 (42.3)</td><td>243 (57.7)</td><td>421</td><td>168 (40): 71D, 96U</td><td>126 (30)</td><td>127 (30)</td></tr><tr><td>4-day</td><td>132 (41.8)</td><td>184 (58.2)</td><td>316</td><td>126 (40): 53D, 73U</td><td>95 (30)</td><td>95 (30)</td></tr></table>

$$
\operatorname{logit} (p) = \log \left\{\frac {p}{1 - p} \right\} = \alpha + x ^ {\prime} b
$$

where a is the intercept parameter and b is a vector of slope parameters.

## 4. Results and discussion

## 4.1. Assessment of classifier robustness

The receiver operating characteristic curve is a popular technique used to evaluate a classification model’s robustness. ROC is the plot of the fraction of positive predictions that are truly positive (TP) on the y-axis versus the fraction that are falsely positive (FP) on the x-axis (see Fig. 3). In our experiment, a positive prediction is equivalent to a prediction that the DJIA index will move down.

Some of the most significant points on the ROC curve are:

$P ( 0 , \ 0 ) { \mathrm { : } }$ does not classify any negative case as positive nor any positive case as positive.

 P(0, 1): represents the perfect classifier in which none of the negative cases is incorrectly classified as positive.

 P(1, 1): represents a classifier in which every negative case is incorrectly classified as positive and every positive case is correctly classified as positive.

Each point P(FP, TP) on the ROC curve represents the false positives and the true positives generated by a classifier given a specific threshold that represents a cut-off point above which a case is classified as positive and below which a case is classified as negative or vise versa.

The line where TP = FP = 0.5 (the 458 line) is the line where the classifier is acting randomly. The farther the ROC bends towards the y-axis and above this line, the better the discrimination power of the classifier. Curve A, represents a classifier of excellent discrimination ability, curve B represents a classifier of good discrimination ability, curves $\mathrm { C } _ { 1 }$ and $\mathrm { C } _ { 2 } ,$ being the closest to the random classification line, represent classifiers of fair discrimination ability, and curve D represents a classifier of poor discrimination ability. One would have achieved the same classification outcome of classifier D with random guessing or without a classifier. $\mathbf { A } \mathbf { n }$ ROC curve, $\mathrm { R O C } _ { 1 } ,$ is said to dominate another ROC curve, $\mathrm { R O C } _ { 2 } ,$ if $\mathrm { R O C } _ { 1 }$ is always above ROC . Further detail on ROC analysis may be found in the literature, particularly [1,12,19,28,37–39].

![](/api/attachments/WERBVYXF/fulltext/images/362e2aaf89af858b34176a6a2b37ccb8d4e0a56ad37666b331d7f4cb102cce00.jpg)  
Fig. 3. ROC curves: A (excellent classifier curve), B (good classifier curve), $\mathrm { C } _ { 1 }$ and $\mathrm { C } _ { 2 }$ (average classifier curve), D (poor classifier curve). All ROC curves are bounded by the point P(0, 0), P(0, 1), and P(1, 1).

## 4.1.1. The area under the ROC curve (AUC)

The AUC represents the probability that the classifier will correctly classify a true positive case; this concept has been well researched [4,11,13]. The AUC has been shown to exhibit a number of desirable properties as a measure of the performance of a classifier:

 It is relatively insensitive to small variations in the shape of the ROC curve.

 It is a single non-parametric index summarizing the whole curve.

 It is not dependent on the chosen decision threshold.

 It is insensitive to prior class probabilities (i.e., the prevalence rate).

 It makes no assumptions as to the underlying distributions of the positive and negative events.

The AUC value ranges from 0.5 for a zero-information classifier, to 1.0 for a perfect classifier. The 95% confidence interval for the AUC can be used to test the hypothesis that the AUC is 0.5. If the confidence interval does not include the value 0.5, then there is evidence that the test does have the ability to distinguish between the two groups [11,49].

## 4.2. Impact of aggregation on model’s robustness

We constructed the ROC curves for a detail-based logistic regression model as well as the ROC curves for a 2-, 3-, and 4-day aggregation-based logistic regression models (see Fig. 4). The ROC curve for the random classifier was included in the figure as a point of reference. The ROC curve of the detail-based classifier clearly dominates all the ROC curves of the aggregation-based classifiers, indicating that the detail-based classifier always classifies better than aggregation-based classifiers. The areas under the ROC curves also confirm this. For example, as Table 5 shows, the detail-based model has the highest AUC (0.835). The areas under the aggregation-based models decreased continuously as the aggregation level increased. Compared with the AUC of the detail-based model, the AUC of the 2-, 3-, and 4-day aggregationbased models decreased by 0.58, 11.9, and 12.4% respectively. These findings raise the following questions:

![](/api/attachments/WERBVYXF/fulltext/images/0bf1da1e9f237883d0eaa658607f1fb515b8848af5abe9aa30a88b7c0338e454.jpg)  
Fig. 4. ROC curves for the down event of the DJIA — the aggregation scenario.

 Is the deterioration in the discrimination ability of aggregation-based classifiers, compared to the detail-based classifier, due purely to aggregation or is it due to the reduction of data necessitated by the aggregation process?

Table 5  
AUCs under ROC curves of detail and 2-, 3-, and 4-day aggregations

<table><tr><td>Aggregation level</td><td>Area under the ROC curve</td><td>AUC change relative to detail (%)</td></tr><tr><td>1-day (detail)</td><td>0.835</td><td>0.00</td></tr><tr><td>2-day</td><td>0.830</td><td>-0.58</td></tr><tr><td>3-day</td><td>0.736</td><td>-11.9</td></tr><tr><td>4-day</td><td>0.732</td><td>-12.4</td></tr></table>

 Is the deterioration in the discrimination ability of the aggregation-based classifiers, compared to the detail-based classifier, statistically significant?

 Is there a relationship between aggregation level and classifier performance?

 Are there different characteristics of detail-based and aggregation-based classifiers; for example, in terms of model complexity and model generalization?

## 4.3. Impact of data shrinkage: sampling versus aggregation

Performance of a classification model will not change significantly whether the model is developed and tested on the whole population or on a sample that is truly representative of the underlying population. However the sample size impacts the accuracy of a classification model. There is no universally agreed upon guideline on an optimal sample size for an effective model. Awidely used rule of thumb is to include at least ten observations per independent variable. Since we have four independent variables, this implies that our sample size should be at least forty observations. Our sample size for the training data set ranged from 232 cases for the daily detail to 53 for the 4-day aggregation. It has also been suggested that meaningful qualitative conclusions can be drawn from ROC experiments performed with a total of about 100 observations. A minimum of 50 cases may be required in each of the two (positive and negative) groups, so that one case represents not more than 2% of the observations (http:// www.medcalc.be/roccman.html). Hence, our experiments are sound in terms of sample size.

To address the issue of deterioration in the discrimination ability of the aggregation-based predictive models due to the shrinkage of data that results from aggregation, we performed another experiment on data shrunk equivalently through sampling rather than aggregation. We randomly selected three sample data sets whose sizes were equal to the sizes of the three aggregated data sets. In particular, in addition to the detail (daily) data, we selected three random samples of sizes 632 (same number of records in the 2-day aggregated data set), 421 (same in the 3-day aggregated data set), and 316 (same in the 4-day aggregated data set).

The ROC curves corresponding to the logistic regression models generated from the whole population and from each of the samples are shown in Fig. 5, and the areas under these ROC curves are shown in Table 6. As in the case of the detail-/aggregation-based ROC curves, there is no overall dominating ROC curve among the sample-based ROC curves — indicating that the model performed similarly in the three samples. On the other hand, unlike the detail-based ROC curve dominating the aggregation-based ROC curves, the population-based ROC curve does not dominate the sample-based ROC curves. Such a result is consistent with what is expected if the samples are truly representatives of the population and their sizes are acceptable. Furthermore, unlike the area under the detailbased ROC curve being larger than the areas under the aggregation-based ROC curves, the area under the population-based ROC curve is also not larger than the areas under the sample-based ROC curves.

![](/api/attachments/WERBVYXF/fulltext/images/663c6822cec3eff0cd048d1da90be7109003797641206b879a0bacb1e5b1ba37.jpg)  
Fig. 5. ROC curves for the down event of the DJIA — the sampling scenario.

Table 6  
AUCs under ROC curves of population and samples

<table><tr><td>Sample</td><td>Area under the ROC curve</td><td>AUC change relative to total population (%)</td></tr><tr><td>1263 — total population</td><td>0.835</td><td>0.0</td></tr><tr><td>632 — sample 1</td><td>0.840</td><td>1.0</td></tr><tr><td>421 — sample 2</td><td>0.820</td><td>-1.8</td></tr><tr><td>316 — sample 3</td><td>0.821</td><td>-1.7</td></tr></table>

The sampling process has not considerably impacted the model’s performance in this experiment as reflected by the changes in the area under the various ROC curves.

## 4.4. Statistical significance

To test the statistical significance of the difference between the performance, summarized by the AUC, of the detail-based and the aggregation-based logistic regression models, we computed [11,29,40] the following measures for each model (see Table 7):

(1) The AUC of the detail-based model.

Table 7  
Area under the curve, its standard error, and its 95% confidence interval for the detail data and each aggregation level data

<table><tr><td>Aggregation level</td><td>AUC</td><td>SE (%)</td><td colspan="2">95% CI</td></tr><tr><td>1-day (detail)</td><td>0.834</td><td>2.12</td><td>0.792</td><td>0.875</td></tr><tr><td>2-day</td><td>0.793</td><td>3.42</td><td>0.726</td><td>0.860</td></tr><tr><td>3-day</td><td>0.773</td><td>4.38</td><td>0.687</td><td>0.858</td></tr><tr><td>4-day</td><td>0.731</td><td>5.43</td><td>0.624</td><td>0.837</td></tr></table>

(2) The AUC of the aggregation-based model.

(3) The standard errors (SE) and their 95% confidence intervals.

In addition, we computed the difference between the area under the curve of the logistic regression model derived from the detail data set and the area under the curve of the logistic regression model derived from each of the aggregated data sets. We also computed the standard errors (SE) of these differences and their 95% confidence intervals [26,30,31]. As is seen in Table 8, even though the area under the curve continually decreased, indicating deterioration in the classification ability of the model as the data is aggregated, the decrease was not statistically significant — since the 95% confidence interval overlapped zero (leading to the non-rejection of the null hypothesis that the two are equal).

Apparently, mining data with logistic regression on the DJIA data preserved its robustness on aggregated data, though it is clear that we cannot continue aggregation indefinitely.

In addition, we examined whether aggregation level impacts the performance of the logistic regression predictive model by performing a pair-wise comparison of the areas under the curves derived by the model from the aggregation data sets (see Table 9). Again, as indicated by the overlapping of the zero by the 95% confidence intervals of area differences, the null hypothesis that the two compared areas are equal cannot be rejected at the 5% significance level. Thus we conclude that there is no statistically significant difference between the compared pairs of area. The conclusion that the aggregation level has not impacted the performance of the model in our experiment is further confirmed by the ROC curves intersecting; i.e., none of the curves derived from an aggregated data set dominates another curve derived from another aggregated data set as Fig. 4 shows. In fact, some curves intersect more than once — a clearer indication of lack of dominance of one curve over the others.

Table 8  
Pairwise differences between detail area and areas of various aggregation levels, and the standard errors and 95% confidence intervals of these areas

<table><tr><td>Compared areas</td><td>Difference</td><td>SE of difference</td><td colspan="2">95% CI</td></tr><tr><td>0.834 (1-day AUC)-0.793 (2-day AUC)</td><td>0.041</td><td>0.040</td><td>-0.038</td><td>0.119</td></tr><tr><td>0.834 (1-day AUC)-0.773 (3-day AUC)</td><td>0.061</td><td>0.049</td><td>-0.034</td><td>0.157</td></tr><tr><td>0.834 (1-day AUC)-0.731 (4-day AUC)</td><td>0.103</td><td>0.058</td><td>-0.011</td><td>0.218</td></tr></table>

Table 9  
Table 11  
Table 10  
Pairwise differences between areas of various aggregation levels, and the standard errors and the 95% confidence intervals of these areas

<table><tr><td>Compared areas</td><td>Difference</td><td>SE of difference</td><td colspan="2">95% CI</td></tr><tr><td>0.793 (2-day AUC)-0.772 (3-day AUC)</td><td>0.021</td><td>0.056</td><td>-0.088</td><td>0.130</td></tr><tr><td>0.793 (2-day AUC)-0.730 (4-day AUC)</td><td>0.063</td><td>0.064</td><td>-0.063</td><td>0.189</td></tr><tr><td>0.772 (3-day AUC)-0.730 (4-day AUC)</td><td>0.042</td><td>0.070</td><td>-0.095</td><td>0.179</td></tr></table>

## 4.5. Impact on model’s generalization

The ultimate test of usefulness of a predictive mode is how well it generalizes: how well the model performs on data on which it was not trained. The model manifests poor generalization if it suffers from either under-fitting (resulting from it not being sufficiently complex, omitting important input variables, and thus failing to detect the relationship in a data set) or overfitting (from the model being too complex, including too many parameters, and detecting noise in the data set). Both of these lead to poor performance of a predictive model. A model’s generalization potential is measured by estimating its generalization error and not by its training error. Choosing a model based on training error will cause the most complex model to be chosen, even if it generalizes poorly. We computed the root mean squared errors and the misclassification rates from the test set of each model (see Table 10).

Root mean squared error and misclassification rate of the test data set

<table><tr><td>Aggregation level</td><td>Root mean squared error</td><td>Misclassification rate</td></tr><tr><td>1-day</td><td>0.40</td><td>0.23</td></tr><tr><td>2-day</td><td>0.41</td><td>0.23</td></tr><tr><td>3-day</td><td>0.44</td><td>0.26</td></tr><tr><td>4-day</td><td>0.41</td><td>0.27</td></tr></table>

It is clear from this that the detail-based as well as the aggregation-based models manifest similar generalization measures here.

A better way to estimate generalization error is to adjust the training error for the complexity of the model. Akaike’s information criterion (AIC) and Schwarz’s Bayesian criterion (SBC) [5] are useful for assessing this: the smaller the values of these criteria, the better the generalization of the model.

For large data sets, a practical way to obtain an unbiased estimate of these criteria is to divide the data set into three parts: the training set, the validation set, and the test set. The validation set is used to choose one of the models. The test set, on the other hand, is used to obtain an unbiased estimate of the generalization error of the chosen model. Hence, we partitioned each input data set and computed the Akaike’s Information Criterion (AIC) and the Schwarz Bayesian criterion (SBC) (see Table 11). The SBC penalizes more than AIC for model complexity. An interesting phenomenon is that both AIC and SBC continuously decreased with higher aggregation levels. This clearly indicates that the higher the aggregation level, the simpler the model, at least in our experiment. Maybe that aggregation data has less noise than detail data and, therefore, spurious parameters that are in the detail-based model are not included in the aggregation-based models, which smoothed out some of the noise in the detail data.

Akaike’s information criterion (AIC) and Schwarz–Bayesian criterion (SBC) for the detail and each of the aggregation data sets

<table><tr><td>Aggregation granularity</td><td>Akaike&#x27;s information criterion (AIC)</td><td>Schwarz Bayesian criterion (SBC)</td></tr><tr><td>1-day</td><td>498</td><td>519</td></tr><tr><td>2-day</td><td>271</td><td>289</td></tr><tr><td>3-day</td><td>201</td><td>216</td></tr><tr><td>4-day</td><td>133</td><td>147</td></tr></table>

## 5. Conclusions

Experimental evidence, admittedly on a single problem, has been presented that demonstrates that aggregation-based data mining with logistic regression is statistically as robust as detail-based data mining with logistic regression. The experiment tested the performance of 2-, 3-, and 4-day aggregationbased models against the performance of one based on the complete detail data.

ROC analysis, a well-established technique in diagnostics, was used for model assessment. The study showed, for the test case used here, that the performance of the aggregation-based models was not statistically significantly different from the performance of the detail-based model. If the detail data is aggregateable, then aggregation can be performed within a data preparation phase for data mining, with the advantage of utilizing the whole data in the mining process.

Aggregation in our experiment also lead to more parsimonious models as it smoothed out some of the noise in the detail data. Parameters included in a detail-based model to capture noise in the detail data will not be needed in aggregation-based models.

## References

[1] J.R. Beck, E.K. Shultz, The use of relative operating characteristic (ROC) curves in test performance evaluation, Archives of Pathology and Laboratory Medicine 110, 1986, pp. 13–20.

[2] E. Bendoly, Theory and support for process frameworks of knowledge discovery and data mining from ERP systems, Information & Management 40, 2003, pp. 639–647.

[3] R.J. Brachman, T. Khabaza, W. Kloesgen, G. Piatetsky-Shapiro, E. Simoudis, Mining business databases, Communications of the ACM 39(11), Nov 1996, pp. 41–48.

[4] A.P. Bradley, The use of the area under the ROC curve in the evaluation of machine learning algorithms, Pattern Recognition 30(7), 1997, pp. 1145–1159.

[5] K.P. Burnham, D.R. Anderson, Model Selection and Inference, Springer-Verlag, New York, 1998.

[6] U. Fayyad, G. Piatetsky-Shapiro, P. Smyth, R. Uthurusamy (Eds.), Advances in Knowledge Discovery and Data Mining, AAAI/MIT Press, Cambridge, MA, 1996.

[7] P.K. Chan, S.J. Stolfo, Learning with non-uniform class and cost distributions: effects and a distributed multi-classifier approach, Work Notes KDD-98 Workshop on Distributed Data Mining (1998) 1–9.

[8] S. Chaudhuri, U. Dayal, An overview of data warehousing and OLAP technology, SIGMOD Record 26(1), 1997, pp. 1–10.

[9] J. Gray, S. Chaudhuri, A. Bosworth, A. Layman, D. Reichart, M. Venkatrao, F. Pellow, H. Pirahesh, Data cube: a relation aggregation operator generalizing group-by, cross-tab, and sub-totals, Data Mining and Knowledge Discovery 1, 1997, pp. 29–53.

[10] A. Gupta, I.S. Mumick, Maintenance of materialized views: problems, techniques, and applications, IEEE Data Engineering Bulletin 18(2), 1995.

[11] J.A. Hanley, B.J. McNeil, The meaning and use of the area under a receiver operating characteristic (ROC) curve, Radiology 143(1), April 1982, pp. 29–36.

[12] J.A. Hanley, Receiver operating characteristics (ROC) methodology: the state of the art, Critical Reviews in Diagnostic Imaging 29(3), 1989, pp. 307–335.

[13] J.A. Hanley, B.J. McNeil, A method of comparing the areas under receiver operating characteristic curves derived from the same cases, Radiology 148(1), 1983, pp. 839–843.

[14] M. Hernandez, S. Stolfo, Real-world data is dirty: data cleansing and the merge/purge problem, Data Mining and Knowledge Discovery 2(1), 1998, pp. 9–37.

[15] S.C. Hui, G. Jha, Data mining for customer service support, Information & Management 38, 2000, pp. 1–13.

[16] W.H. Inmon, The data warehouse and data mining, Communications of the ACM 39(11), Nov 1996, pp. 49–50.

[17] W.H. Inmon, Building the Data Warehouse, John Wiley, 1992.

[18] N. Japkowicz, Learning from imbalanced data sets: a comparison of various strategies, AAAI 2000 Workshop on Learning from Imbalanced Data Sets, Technical Report WS-00-05, July 2000.

[19] A.D. Kester, F. Buntix, Meta-analysis of ROC curves, Medical Decision Making 20(4), 2000, pp. 430–439.

[20] M. Kubat, R. Holte, S. Matwin, Learning when negative examples abound, in: Proceedings of the European Conference on Machine Learning, ECML’97, Prague, 1997, pp. 146–153.

[21] M. Kubat, S. Matwin, Addressing the curse of imbalanced training sets: one-sided selection, in: Proceedings of the 14th International Conference on Machine Learning, ICML’97, Nashville, TN, USA, pp. 179–186.

[22] A.L. Lederer, J.R. Smith, Individual differences and decisionmaking using various levels of aggregation of information, Journal of Management Information Systems 5(3), 1988– 1989, pp. 53–69.

[23] D. Lomet, J. Widom (Eds.), Special issue on materialized views and data warehousing, IEEE Data Engineering Bulletin 18 (2) 1995.

[24] S. Madnick, X. Chen, J. Funk, R. Wang, Corporate household data: research directions, in: Proceedings of AMCIS 2001, Boston, MA, 2001.

[25] B.G. Malkiel, A Random Walk Down the Wall Street, W.W. Norton & Company, New York, 2000.

[26] B.J. McNeil, J.A. Hanley, Statistical approaches to the analysis of receiver operating characteristic (ROC) curves, Medical Decision Making 4(2), 1984, pp. 137–150.

[27] M.E. Meredith, A. Khader, Divide and aggregate: designing large warehouses, Database Programming and Design June 1996, pp. 24–30.

[28] C.E. Metz, Basic principles of ROC analysis, Seminars in Nuclear Medicine 8(4), 1978, pp. 283–298.

[29] C.E. Metz, B.A. Herman, C.A. Roe, Statistical comparison of two ROC-curve estimates obtained from partially-paired datasets, Medical Decision Making 18(1), January–March 1998, pp. 110–121.

[30] C.E. Metz, Some practical issues of experimental design and data analysis in radiological ROC studies, Investigative Radiology 24, 1989, pp. 234–245.

[31] C.E. Metz, ROC methodology in radiological imaging, Investigative Radiology 21(9), 1986, pp. 720–733.

[32] A.R. Montazemi, S. Wang, The effects of models of information presentation on decision-making, Journal of Management Information Systems 5(3), 1988–89, pp. 101–127.

[33] Oracle Data Warehousing Reference Manual, 2000, p. 92.

[34] F. Provost, Machine learning from imbalanced data sets 101, http://www.stern.nyu.edu/\~fprovost/Papers/skew.PDF.

[35] S. Salzberg, On comparing classifiers: a critique of current research and methods, Data Mining and Knowledge Discovery 1, 1999, pp. 1–12.

[36] I. Spiegler, Technology and knowledge: bridging a generating gap, Information & Management 40, 2003, pp. 533–539.

[37] J.A. Swets, R.M. Pickett, Evaluation of Diagnostic Systems: Methods from Signal Detection Theory, Academic Press, New York, 1982.

[38] J.A. Swets, R.M. Dawes, J. Monahan, Psychological science can improve diagnostic decisions, Psychological Science in the Public Interest 1(1), May 2000, pp. 1–26.

[39] J.A. Swets, R.M. Dawes, J. Monahan, Better decisions through science, Scientific American 2000, pp. 82–87.

[40] M.L. Thompson, W. Zucchini, On the statistical analysis of ROC curves, Statistics in Medicine 8, 1989, pp. 1277–1290.

[41] U.S. EPA, Handbook for use of data from the national health and nutrition examination surveys (NHANES), National Center for Environmental Assessment, Washington, DC, EPA/ 600/R-02/044, 2003, p. 21.

[42] A. Vavouras, S. Gatziu, K.R. Dittrich, The SIRIUS approach for refreshing data warehouses incrementally, in: Proceedings of the BTW’99, 1999, pp. 80–96.

[43] S. Walczak, An empirical analysis of data requirements for financial forecasting with neural networks, Journal of Management Information Systems 17(4), Spring 2001, pp. 203– 222.

[44] A. Weigend, Analyzing customer behavior at Amazon.com, in: Proceedings of the Ninth ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, Washington, DC, USA, 24–27 August 2003, p. 5.

[45] G.M. Weiss, F. Provost, The effect of class distribution on classifier learning: an empirical study, Technical Report ML-TR-44, Department of Computer Science, Rutgers University, 2 August 2001, pp. 1–26.

[46] G.M. Weiss, F. Provost, The effect of class distribution on classifier learning, Technical Report ML-TR-43, Department of Computer Science, Rutgers University, 11 January 2001, pp. 1–6.

[47] J. Widom, Research problems in data warehousing, Conference on Information and Knowledge Management (CIKM), Baltimore, Maryland, USA, 1995.

[48] M.C. Wu, A.P. Buchmann, Research issues in data warehousing, in: Proceedings of the BTW’97, Ulm, Germany, 1997, pp. 61–82.

[49] M.H. Zweig, G. Campbell, Receiver-operating characteristic (ROC) plots: a fundamental evaluation tool in clinical medicine, Clinical Chemistry 39(4), 1993, pp. 561–577.
