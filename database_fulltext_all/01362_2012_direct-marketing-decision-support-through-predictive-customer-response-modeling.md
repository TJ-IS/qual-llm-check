---
otero_id: 1362
otero_key: "BPXWZ942"
title: "Direct marketing decision support through predictive customer response modeling"
authors: "David L. Olson; Bongsug(Kevin) Chae"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.06.005"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Direct marketing decision support through predictive customer response modeling

David L. Olson <sup>a</sup>, Bongsug(Kevin) Chae <sup>b,</sup>⁎

<sup>a</sup> Department of Management, University of Nebraska, Lincoln, NE 68588-0491, United States

<sup>b</sup> Department of Management, Kansas State University, Manhattan, KS 66506, United States

## a r t i c l e i n f o

Article history: Received 8 June 2011 Received in revised form 12 May 2012 Accepted 19 June 2012 Available online 3 July 2012

Keywords: Customer response predictive mode Knowledge-based marketing RFM Neural networks Decision tree models Logistic regression

## a b s t r a c t

Decision support techniques and models for marketing decisions are critical to retail success. Among different marketing domains, customer segmentation or pro<sup>fi</sup>ling is recognized as an important area in research and industry practice. Various data mining techniques can be useful for ef<sup>fi</sup>cient customer segmentation and targeted marketing. One such technique is the RFM method. Recency, frequency, and monetary methods provide a simple means to categorize retail customers. We identify two sets of data involving catalog sales and donor contributions. Variants of RFM-based predictive models are constructed and compared to classical data mining techniques of logistic regression, decision trees, and neural networks. The spectrum of tradeoffs is analyzed. RFM methods are simpler, but less accurate. The effect of balancing cells, of the value function, and classical data mining algorithms (decision tree, logistic regression, neural networks) are also applied to the data. Both balancing expected cell densities and compressing RFM variables into a value function were found to provide models similar in accuracy to the basic RFM model, with slight improvement obtained by increasing the cutoff rate for classi<sup>fi</sup>cation. Classical data mining algorithms were found to yield better prediction, as expected, in terms of both prediction accuracy and cumulative gains. Relative tradeoffs among these data mining algorithms in the context of customer segmentation are presented. Finally we discuss practical implications based on the empirical results.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

The role of decision support techniques and models for marketing decisions has been important since the inception of decision support systems (DSSs) [25]. Diverse techniques and models (e.g., optimization, knowledge-based systems, simulation) have emerged over the last <sup>fi</sup>ve decades. Many marketing domains, including pricing, new product development, and advertising, have bene<sup>fi</sup>ted from these techniques and models [16]. Among these marketing domains, customer segmentation or pro<sup>fi</sup>ling is recognized as an important area [18,19,26,43]. There are at least two reasons for this. First, the marketing paradigm is becoming customer-centric [41] and targeted marketing and service are suitable. Second, unsolicited marketing is costly and ineffective (e.g., low response rate) [15,30]. Along with these reasons, there are increasing ef forts on collecting and analyzing customer data for better marketing decisions [9,26,30]. The advancement of online shopping technologies and database systems has accelerated this trend.

Data mining has been a valuable tool in this regard. Various data mining techniques, including statistical analysis and machine learning algorithms, can be useful for ef<sup>fi</sup>cient customer segmentation and targeted marketing [4,26,38]. One such technique is RFM, standing for recency, frequency, and monetary. RFM analysis has been used for marketing decisions for a long time and is recognized as a useful data mining technique for customer segmentation and response models [3,30]. A survey [43] also shows that RFM is among the most popular segmentation and predictive modeling techniques used by marketers.

RFM relies on three customer behavioral variables (how long since the last purchase by customer, how often the customer purchases, how much the customer has bought) to <sup>fi</sup>nd valuable customers or donors and develop future direct marketing campaigns. Having a reliable and accurate customer response model is critical for marketing success since an increase or decrease in accuracy of 1% could have a signi<sup>fi</sup>cant impact on their pro<sup>fi</sup>ts [1]. While there could be many other customer-related factors [e.g.,42], previous studies have shown that RFM alone can offer a powerful way of predicting the future customer purchase [1,3,17].

Our research builds customer response models using RFM variables and compares them in terms of customer gains and prediction accuracy. The paper aims to increase understanding of how to <sup>fi</sup>nd knowledge hidden in customer and transactional databases using data mining techniques. This area is called knowledge-based marketing [26]. The next section brie<sup>fl</sup>y reviews various data mining techniques for building customer response or predictive models. Section 3 describes methodology. All the response models will be built upon the three RFM variables, while different data mining techniques are used. Then, we present a research design, including two direct marketing data sets with over 100,000 observations, a process of predictive modeling building, and methods to measure the performance of models. Section 4 includes analysis and results. There could be different methods to increase the prediction performance of an RFM-based predictive model and sophisticated data mining techniques (decision tree, logistic regression, and neural networks) appear to outperform more traditional RFM. These <sup>fi</sup>ndings are further discussed in Section 5, comparing results with previous studies of customer response models and in the broad contexts of knowledge-based marketing. We also discuss practical implications from the <sup>fi</sup>ndings and offer conclusions.

The contribution of this study is to demonstrate how RFM model variants can work, and supports general conclusions consistently reported by others that RFM models are inferior to traditional data mining models. This study shows that RFM variables are very useful inputs for designing various customer response models with different strengths and weaknesses and the ones relying on classical data mining (or predictive modeling) techniques can signi<sup>fi</sup>cantly improve the prediction capability in direct marketing decisions. These predictive models using RFM variables are simple and easy to use in practice than those with a complex set of variables. Besides descriptive modeling techniques popular in practice [43], thus, marketers should adopt those advanced predictive models in their direct marketing decisions.

## 2. Customer response models using data mining techniques

## 2.1. Marketing DSS and customer response models

The use of DSS in marketing goes back to the 1960s and 1970s [22,44] and has been applied in various areas, including marketing strategy, pricing, new product development, and product analysis and management [16]. There has been an increase of DSS use in customer-side marketing activities, such as customer segmentation (or pro<sup>fi</sup>ling), direct marketing, database marketing, and targeted advertising. This re<sup>fl</sup>ects advances in database management and complex model building [11,16,35]. More convenient methods are available for the acquisition and storage of large amounts of customer and transactional data. In addition, knowledge-based systems or intelligent systems using data mining techniques (e.g., neural networks) [37] have emerged in the marketing domain.

This trend is broadly termed knowledge-based marketing. Knowledge-based marketing is both data-driven and model-driven: that is the use of sophisticated data mining tools and methods to <sup>fi</sup>nd knowledge discovery from customer and transactional databases [26]. Overall, this leads to more ef<sup>fi</sup>cient and effective communication with potential buyers and an increase in pro<sup>fi</sup>ts. An important approach to knowledge-based marketing is to understand customers and their behavioral patterns. This requires such transactional characteristics as recency of purchases, frequency of purchases, size of purchases, identifying customer groups, and predicting purchases [35]. The RFM model and other data mining-based customer response models have proven useful to marketers.

## 2.2. Data mining techniques for customer response models

## 2.2.1. RFM

R represents the period since the last purchase. F is the number of purchases made by a customer during a certain period. M is the total purchase amount by a customer over that period. It is common practice for each R, F, and M to have <sup>fi</sup>ve groups or levels and thus there are 125 $( = 5 * 5 * 5 )$ customer segmentation groups. Each customer is segmented into one cell or group. This model allows markets to differentiate their customers in terms of three factors and to target the customer groups that are likely to purchase products or services. This technique is known as the benchmark model in the area of database marketing [3].

Since its introduction in a major marketing journal [5], RFM has received a great deal of interest from both academic and industry communities [3,17]. Many studies [1,13,17] have recognized these three variables as important to predict the future responses by customers to potential direct marketing efforts. Certain limitations in the original RFM model have been recognized in the literature [31,45]. Some previous studies have extended the original RFM model either by considering additional variables (e.g., socio-demographics) [1] or by combining with other response techniques [6,7]. Because of the high correlation between F and M, Yang [45] offered a version of RFM model collapsing the data to a single variable ${ } ^ { \mathrm { * } } \mathrm { V a l u e ^ { \mathrm { * } } } { = } \mathrm { M } / \mathrm { R } .$ To overcome the problem of data skewed in RFM cells, Olson et al. [31] proposed an approach to balance observations in each of the 125 RFM cells.

Other variables that may be important include customer income, customer lifestyle, customer age, product variation, and so on [14]. That would make traditional data mining tools such as logistic regression more attractive. However, RFM is the basis for a continuing stream of techniques to improve customer segmentation marketing [12]. RFM has been found to work relatively well if expected response rate is high [24]. Other approaches to improve RFM results have included Bayesian networks [1,8] and association rules [46].

## 2.2.2. Classical data mining tools

Common data mining practice in classi<sup>fi</sup>cation is to gather a great number of variables and apply different standard algorithms. Given the set of prede<sup>fi</sup>ned classes and a number of attributes, these classi-<sup>fi</sup>cation methods can provide a model to predict the class of other unclassi<sup>fi</sup>ed data. Mathematical techniques that are often used to construct classi<sup>fi</sup>cation methods are binary decision trees, neural networks, and logistic regression. By using binary decision trees, a tree induction model with “Yes–No” format can be built to split data into different classes according to its attributes. Such a model is very easy to apply to new cases, although the algorithms often produce an excessive number of rules. Neural networks often <sup>fi</sup>t nonlinear relationships very well, but are dif<sup>fi</sup>cult to apply to new data. Logistic regression models are easy to apply to new data, although the problem of a cutoff between classes can be an issue [32].

Relative performance of data mining algorithms has long been understood to depend upon the speci<sup>fi</sup>c data. Since data mining software is widespread, common practice in classi<sup>fi</sup>cation is to try the three basic algorithms (decision trees, neural networks, logistic regression), and use the one that works best for the given data set. Studies have compared these algorithms with RFM. Levin and Zahavi [20] compared RFM with decision trees (speci<sup>fi</sup>cally CHAID), pointing out that decision trees are more automatic (RFM requires extensive data manipulation), but involve modeling issues such as controlling tree size and determining the best split for branches and leaves. Kim and Street [19] proposed a neural network model and applied feature selection mechanisms to reduce input variables, enabling focus upon the most important variables. Baesens et al. [1] also applied neural networks to customer response models (adding customer pro<sup>fi</sup>le indicators to RFM), obtaining better prediction accuracy. That is a consistent <sup>fi</sup>nding — data mining algorithms will be expected to better predict customer response than RFM. However, RFM remains interesting because it relies upon the three fundamentally basic inputs that are readily available.

## 3. Methodology

## 3.1. Problem description and data set

This research design includes two studies (Study 1 and Study 2 hereafter) using two datasets obtained from the Direct Marketing Educational Foundation. Study 1 uses a dataset including 101,532 individual purchases from 1982 to 1992 in catalog sales. Study 2 is based on the data of 1,099,009 individual donors' contributions to a non-pro<sup>fi</sup>t organization collected between 1991 and 2006. The purchase orders (or donations) included ordering (or donation) date and ordering amount. The last four months (Aug–Dec) of the data were used as the target period: Aug–Dec 1992 for Study 1 and

Aug–Dec 2006 for Study 2. The average response rates in Studies 1 and 2 are 0.096 and 0.062 respectively.

Data preparation and manipulation are an important stage of knowledge discovery and learning in knowledge-base marketing [35]. Fig. 1 describes our approach. The raw data contained customer behavior represented by account, order (or donation) date, order (donation) dollars, and many other variables. We followed the general coding scheme to compute R, F, and M [17]. Various data preparation techniques (e.g., <sup>fi</sup>ltering, transforming) were used during this process. The order date of last purchase (or the date of last donation) was used to compute R (R1, R2, R3, R4, R5). The data set contained order (or donation) history and order dollars (or donation amounts) per each customer (or donor), which were used for F (F1, F2, F3, F4, F5) and M (M1, M2, M3, M4, M5). We also included one response variable (Yes or No) to the direct marketing promotion or campaign.

## 3.2. Predictive models

## 3.2.1. RFM

RFM analysis typically divides the data into 125 cells, designated by the 5 groups. The most attractive group would be 555, or Group 5 for each of the 3 variables [17].

## 3.2.2. RFM with balanced cells

Dividing customers or donors into 125 cells tends to result in the skewness that the data is not evenly distributed among those cells. This skewness has been recognized as one of the problems with RFM [13,27,31]. Our approach to this issue was through more equal density (size-coding) to obtain data entries for all RFM cells. We accomplished this by adjusting cell limits to obtain more equal counts for cells in the training set.

## 3.2.3. RFM with Yang's value function

Previous studies [19] have pointed out a strong correlation between F and M as a limitation of RFM. The value function [45] compresses the RFM data into one variable — V=M/R.

## 3.2.4. Logistic regression (LR)

The purpose of logistic regression is to classify cases into the most likely category. Logistic regression provides a set of β parameters for the intercept (or intercepts in the case of ordinal data with more than two categories) and independent variables, which can be applied to a logistic function to estimate the probability of belonging to a speci<sup>fi</sup>ed output class [32]. Logistic regression is among the most popular data mining techniques in marketing DSS and response modeling [24].

## 3.2.5. Decision tree (DT)

Decision trees in the context of data mining refer to the tree structure of rules. They have been applied by many in the analysis of direct marketing data [39,40]. The data mining decision tree process involves collecting those variables that the analyst thinks might bear on the decision at issue, and analyzing these variables for their ability to predict outcome. Decision trees are useful to gain further insight into customer behavior, as well as lead to ways to pro<sup>fi</sup>tably act on results. One of a number of algorithms automatically determines which variables are most important, based on their ability to sort the data into the correct output category. The method has relative advantage over neural network and genetic algorithms in that a reusable set of rules are provided, thus explaining model conclusions.

## 3.2.6. Neural networks (NN)

Neural networks are the third classical data mining tool found in most commercial data mining software products, and have been applied to direct marketing applications [4,8,19,36]. NN are known for their ability to train quickly on sparse data sets. NN separates data into a speci<sup>fi</sup>ed number of output categories. NN are three layer networks wherein the training patterns are presented to the input layer and the output layer has one neuron for each possible category.

## 3.3. Performance evaluation measures

There are different methods to assess customer response model performances. We use prediction accuracy and cumulative gains to discuss the performance of different predictive customer response models. Gains show the percentage of responders in each decile. Marketers can <sup>fi</sup>gure out how many responders (or what proportion of responders) can be expected in a speci<sup>fi</sup>c decile. For example, we can say that given a same mailing size (e.g., 40% of the total customers) a model capturing 70% of the responders is better than a model capturing only 60% of the responders [47]. Through cumulative gain values we can evaluate the performances of different data mining techniques [21]. Another way is using prediction accuracy rate of each technique. The data set employed in this research has the information about who responded to the direct marketing or campaign. Using R, F, and M as three predictive variables, each data mining technique will develop a binary customer response model based on the training data set and apply the model to the test data set. This will generate prediction accuracy rate — the percentage of customers classi<sup>fi</sup>ed correctly [21]. The model building process is shown in Fig. 1.

## 4. Analysis and results

The analysis process consisted of model building using each data mining technique and model assessment. For Study 1, customer response models were developed using RFM, RFM with balanced cells, RFM with Yang's value function, logistic regression (LR), decision tree (DT), and neural networks (NN). Model assessment is presented with gains and predictive accuracy.

## 4.1. Study 1

An initial correlation analysis was conducted, showing that there was some correlation among these variables, as shown in Table 1.

![](/api/attachments/BPXWZ942/fulltext/images/23e9bfdac20b8cf1f3f4ca3fb3ff49e9f1fa42cd9ac62b99b1bb26ad497d81d1.jpg)  
Fig. 1. Research design building predictive models using RFM variables.

All three variables were signi<sup>fi</sup>cant at the 0.01 level. The relationship between R and customer response is negative, as expected. In contrast, F and M are positively associated with customer response. R and F are stronger predictors for customer response.

RFM was initially applied, dividing the scales for each of the three components into <sup>fi</sup>ve groups based upon the scales for R, F, and M. This was accomplished by entering bin limits in SPSS. Table 2 shows boundaries. Group 5 was assigned the most attractive group, which for R was the minimum, and for F and M the maximum.

Note the skewness of the data for F, which is often encountered. Here the smaller values dominate that metric. Table 3 displays the counts obtained for these 125 cells.

The proportion of responses (future order placed) for the data is given in Table 4.

In the training set, 10 of 125 possible cells were empty, even with over 100,000 data points. The cutoff for pro<sup>fi</sup>tability would depend upon cost of promotion compared to average revenue and rate of pro<sup>fi</sup>t. For example, if cost of promotion were \$50, average revenue per order \$2000, and average pro<sup>fi</sup>t rate \$0.25 per dollar of revenue, the pro<sup>fi</sup>tability cutoff would be 0.1. In Table 4, those cells with return ratios greater than 0.1 are shown in bold. Those cells with ratios at 0.1 or higher with support (number of observations) below 50 are indicated in italics. They are of interest because their high ratio may be spurious. The implication is fairly self-evident — seek to apply promotion to those cases in bold without italics. The idea of dominance can also be applied. The combinations of predicted success for different training cell proportions are given in Table 5.

The RFM model from the Excel spreadsheet model yields predictive model performance shown in the Appendix A for the line Basic on 0.1 (because the cutoff used was a proportion of 0.1) along with results from the other models. This model was correct (13,961+1337= 15,298) times out of 20,000, for a correct classi<sup>fi</sup>cation rate of 0.765. The error was highly skewed, dominated by the model predicting 4113 observations to be 0 that turned out to respond. An alternative model would be degenerate — simply predict all observations to be 0. This would have yielded better performance, with 18,074 correct responses out of 20,000, for a correct classi<sup>fi</sup>cation rate of 0.904. This value could be considered a par predictive performance. This data is included in the Appendix A, where we will report results of all further models in terms of correct classi<sup>fi</sup>cation.

Increasing the test cutoff rate leads to improved models. We used increasing cutoffs of 0.2, 0.3, 0.4, and 0.5, yielding the results indicated in the Appendix A. Only the model with a cutoff rate of 0.5 resulted in a better classi<sup>fi</sup>cation rate than the degenerate model. In practice, the best cutoff rate would be determined by <sup>fi</sup>nancial impact analysis, re<sup>fl</sup>ecting the costs of both types of errors. Here we simply use classi-<sup>fi</sup>cation accuracy overall, as we have no dollar values to use.

The correlation across F and M (0.631 in Table 1) can be seen in Table 3, looking at the R=5 categories. In the M=1 column of Table 3, F entries are 0 for every F5 category, usually increasing through M=2 through M=5 columns. When F=5, the heaviest density tends to be in the column where M=5. This skewness is often recognized as one of the problems with RFM [13,27,31]. Our approach to this issue was through more equal density (size-coding) to obtain data entries for all RFM cells. We accomplished this by setting cell limits by count within the training set for each variable. We cannot obtain the desired counts for each of the 125 combined cells because we are dealing with three scales. But we can come closer, as in Table 6. Dif<sup>fi</sup>culties arose primarily due to F having integer values. Table 6 limits were generated sequentially, starting by dividing R into 5 roughly equal groups. Within each group, F was then sorted into groups based on integer values, and then within those 25 groups, M divided into roughly equally sized groups.

Variable correlations.

<table><tr><td></td><td>R</td><td>F</td><td>M</td><td>Ordered</td></tr><tr><td>R</td><td>1</td><td></td><td></td><td></td></tr><tr><td>F</td><td>-0.192**</td><td>1</td><td></td><td></td></tr><tr><td>M</td><td>-0.136**</td><td>0.631**</td><td>1</td><td></td></tr><tr><td>Ordered</td><td>-0.235**</td><td>0.241**</td><td>0.150**</td><td>1</td></tr></table>

Correlation is signi<sup>fi</sup>cant at the 0.01 level (2-tailed).

Table 2 RFM boundaries.

<table><tr><td>Factor</td><td>Min</td><td>Max</td><td>Group 1</td><td>Group 2</td><td>Group 3</td><td>Group 4</td><td>Group 5</td></tr><tr><td>R</td><td>12</td><td>3810</td><td>1944+</td><td>1291-1943</td><td>688-1290</td><td>306-687</td><td>12-305</td></tr><tr><td>Count</td><td></td><td></td><td>16,297</td><td>16,323</td><td>16,290</td><td>16,351</td><td>16,271</td></tr><tr><td>F</td><td>1</td><td>39</td><td>1</td><td>2</td><td>3</td><td>4-5</td><td>6+</td></tr><tr><td>Count</td><td></td><td></td><td>43,715</td><td>18,274</td><td>8206</td><td>6693</td><td>4644</td></tr><tr><td>M</td><td>0</td><td>4640</td><td>0-20</td><td>21-38</td><td>39-65</td><td>66-122</td><td>123+</td></tr><tr><td>Count</td><td></td><td></td><td>16,623</td><td>16,984</td><td>15,361</td><td>16,497</td><td>16,067</td></tr></table>

The unevenness of cell densities is due to uneven numbers in the few integers available for the F category. The proportion of positive responses in the training set is given in Table 7.

If M=5, this model predicts above average response. There is a dominance relationship imposed, so that cells 542 and better, 532 and better, 522 and better, 512 and better, 452 and better, 442 and better, and 433 and better are predicting above average response. Cells 422, 414, and 353 have above average training response, but cells with superior R or F ratings have below average response, so these three cells were dropped from the above average response model. The prediction accuracy ((13,897+ 734) /20,000) for this model was 0.732 (see the balance on 0.1 row in the Appendix A). In this case, balancing cells did not provide added accuracy over the basic RFM model with unbalanced cells. Using the cutoff rate of 0.5, the model is equivalent to predict the combination of R=5, F=4 or 5, and M=4 or 5 as responding and all others not. This model had a correct classi<sup>fi</sup>cation rate of 0.894, which was inferior to the degenerate case. For this set of data, balancing cells accomplished better statistical properties per cell, but was not a better predictor.

Since F is highly correlated with M (0.631 in Table 1), the analysis is simpli<sup>fi</sup>ed to one dimension. Dividing the training set into groups of 5%, sorted on V, generates Table 8.

Count by RFM cell – training set.

<table><tr><td>RF</td><td>R</td><td>F</td><td>M1</td><td>M2</td><td>M3</td><td>M4</td><td>M5</td></tr><tr><td>55</td><td>R 12-305</td><td>F 6+</td><td>0</td><td>0</td><td>16</td><td>151</td><td>1761</td></tr><tr><td>54</td><td></td><td>F 4-5</td><td>2</td><td>18</td><td>118</td><td>577</td><td>1157</td></tr><tr><td>53</td><td></td><td>F 3</td><td>9</td><td>94</td><td>363</td><td>756</td><td>671</td></tr><tr><td>52</td><td></td><td>F 2</td><td>142</td><td>616</td><td>1012</td><td>1135</td><td>559</td></tr><tr><td>51</td><td></td><td>F 1</td><td>2425</td><td>1978</td><td>1386</td><td>938</td><td>387</td></tr><tr><td>45</td><td>R306-687</td><td>F 6+</td><td>0</td><td>1</td><td>11</td><td>101</td><td>1018</td></tr><tr><td>44</td><td></td><td>F 4-5</td><td>0</td><td>16</td><td>87</td><td>510</td><td>927</td></tr><tr><td>43</td><td></td><td>F 3</td><td>6</td><td>88</td><td>316</td><td>699</td><td>636</td></tr><tr><td>42</td><td></td><td>F 2</td><td>150</td><td>707</td><td>1046</td><td>1140</td><td>616</td></tr><tr><td>41</td><td></td><td>F 1</td><td>2755</td><td>2339</td><td>1699</td><td>1067</td><td>416</td></tr><tr><td>35</td><td>R688-1290</td><td>F 6+</td><td>0</td><td>1</td><td>5</td><td>70</td><td>799</td></tr><tr><td>34</td><td></td><td>F 4-5</td><td>1</td><td>16</td><td>122</td><td>420</td><td>832</td></tr><tr><td>33</td><td></td><td>F 3</td><td>9</td><td>88</td><td>319</td><td>706</td><td>589</td></tr><tr><td>32</td><td></td><td>F 2</td><td>163</td><td>697</td><td>1002</td><td>1128</td><td>645</td></tr><tr><td>31</td><td></td><td>F 1</td><td>2951</td><td>2567</td><td>1645</td><td>1078</td><td>437</td></tr><tr><td>25</td><td>R1291-1943</td><td>F 6+</td><td>0</td><td>0</td><td>9</td><td>56</td><td>459</td></tr><tr><td>24</td><td></td><td>F 4-5</td><td>0</td><td>22</td><td>72</td><td>372</td><td>688</td></tr><tr><td>23</td><td></td><td>F 3</td><td>9</td><td>95</td><td>290</td><td>678</td><td>501</td></tr><tr><td>22</td><td></td><td>F 2</td><td>211</td><td>749</td><td>1096</td><td>1128</td><td>561</td></tr><tr><td>21</td><td></td><td>F 1</td><td>3377</td><td>2704</td><td>1660</td><td>1108</td><td>478</td></tr><tr><td>15</td><td>R 1944+</td><td>F 6+</td><td>0</td><td>0</td><td>3</td><td>22</td><td>170</td></tr><tr><td>14</td><td></td><td>F 4-5</td><td>1</td><td>11</td><td>74</td><td>243</td><td>409</td></tr><tr><td>13</td><td></td><td>F 3</td><td>9</td><td>122</td><td>261</td><td>511</td><td>380</td></tr><tr><td>12</td><td></td><td>F 2</td><td>268</td><td>878</td><td>1108</td><td>995</td><td>522</td></tr><tr><td>11</td><td></td><td>F 1</td><td>4145</td><td>3177</td><td>1641</td><td>908</td><td>449</td></tr><tr><td></td><td>Totals</td><td></td><td>16,623</td><td>16,984</td><td>15,361</td><td>16,497</td><td>16,067</td></tr></table>

Table 4 Response ratios by cell.

<table><tr><td>RF</td><td>R</td><td>F</td><td>M1</td><td>M2</td><td>M3</td><td>M4</td><td>M5</td></tr><tr><td>55</td><td>R 12-306</td><td>F 6+</td><td>-</td><td>-</td><td>0.687</td><td>0.563</td><td>0.558</td></tr><tr><td>54</td><td></td><td>F 4-5</td><td>0</td><td>0.500</td><td>0.415</td><td>0.426</td><td>0.384</td></tr><tr><td>53</td><td></td><td>F 3</td><td>0.111</td><td>0.426</td><td>0.342</td><td>0.381</td><td>0.368</td></tr><tr><td>52</td><td></td><td>F 2</td><td>0.296</td><td>0.289</td><td>0.281</td><td>0.283</td><td>0.256</td></tr><tr><td>51</td><td></td><td>F 1</td><td>0.173</td><td>0.196</td><td>0.201</td><td>0.158</td><td>0.152</td></tr><tr><td>45</td><td>R307-687</td><td>F 6+</td><td>-</td><td>0</td><td>0.273</td><td>0.238</td><td>0.193</td></tr><tr><td>44</td><td></td><td>F 4-5</td><td>-</td><td>0.125</td><td>0.092</td><td>0.112</td><td>0.123</td></tr><tr><td>43</td><td></td><td>F 3</td><td>0</td><td>0.091</td><td>0.082</td><td>0.089</td><td>0.101</td></tr><tr><td>42</td><td></td><td>F 2</td><td>0.060</td><td>0.075</td><td>0.069</td><td>0.081</td><td>0.078</td></tr><tr><td>41</td><td></td><td>F 1</td><td>0.047</td><td>0.049</td><td>0.052</td><td>0.053</td><td>0.041</td></tr><tr><td>35</td><td>R688-1286</td><td>F 6+</td><td>-</td><td>1.000</td><td>0</td><td>0.100</td><td>0.125</td></tr><tr><td>34</td><td></td><td>F 4-5</td><td>0</td><td>0.063</td><td>0.107</td><td>0.107</td><td>0.103</td></tr><tr><td>33</td><td></td><td>F 3</td><td>0.111</td><td>0.023</td><td>0.066</td><td>0.059</td><td>0.075</td></tr><tr><td>32</td><td></td><td>F 2</td><td>0.049</td><td>0.047</td><td>0.061</td><td>0.063</td><td>0.060</td></tr><tr><td>31</td><td></td><td>F 1</td><td>0.030</td><td>0.031</td><td>0.029</td><td>0.026</td><td>0.021</td></tr><tr><td>25</td><td>R1287-1943</td><td>F 6+</td><td>-</td><td>-</td><td>0.111</td><td>0.054</td><td>0.078</td></tr><tr><td>24</td><td></td><td>F 4-5</td><td>-</td><td>0.091</td><td>0.028</td><td>0.065</td><td>0.060</td></tr><tr><td>23</td><td></td><td>F 3</td><td>0</td><td>0.053</td><td>0.048</td><td>0.049</td><td>0.064</td></tr><tr><td>22</td><td></td><td>F 2</td><td>0.043</td><td>0.020</td><td>0.039</td><td>0.041</td><td>0.039</td></tr><tr><td>21</td><td></td><td>F 1</td><td>0.018</td><td>0.021</td><td>0.018</td><td>0.020</td><td>0.019</td></tr><tr><td>15</td><td>R 1944+</td><td>F 6+</td><td>-</td><td>-</td><td>0.000</td><td>0.045</td><td>0.041</td></tr><tr><td>14</td><td></td><td>F 4-5</td><td>0</td><td>0.091</td><td>0.024</td><td>0.025</td><td>0.039</td></tr><tr><td>13</td><td></td><td>F 3</td><td>0.111</td><td>0.041</td><td>0.050</td><td>0.033</td><td>0.053</td></tr><tr><td>12</td><td></td><td>F 2</td><td>0.019</td><td>0.046</td><td>0.036</td><td>0.031</td><td>0.044</td></tr><tr><td>11</td><td></td><td>F 1</td><td>0.021</td><td>0.015</td><td>0.016</td><td>0.020</td><td>0.016</td></tr></table>

Lift is the marginal difference in a segment's proportion of response to a promotion and the average rate of response. Target customers are identi<sup>fi</sup>ed as the small subset of people with marginally higher probability of purchasing. Lift itself does not consider pro<sup>fi</sup>tability. In practice, this needs to be considered. For our purposes, we demonstrate without dollar values (which are not available), noting that the relative cost of marketing and expected pro<sup>fi</sup>tability per segment will determine the optimal number of segments to market. Fig. 2 shows lift by value ratio.

In Fig. 2, the most responsive segment has an expected return of slightly over 20%. The lift line is the cumulative average response as segments are added (in order of response rate).

Using the value ratio as a predictive classi<sup>fi</sup>er, the training data was used to identify cells with better responses. Model <sup>fi</sup>t is shown in the Appendix A in the row value function. This model has a correct classi<sup>fi</sup>cation rate of 0.721. This is inferior to a degenerate model that would simply classify all cases as no response, indicating that the value function was non-productive in this case. While it is easier to manipulate than the RFM model, in this case the <sup>fi</sup>t was inferior to the basic RFM model.

Data mining is rich in classi<sup>fi</sup>cation models [2,23]. Three classical data mining classi<sup>fi</sup>cation models were applied to the data: logistic regression, decision trees, and neural networks. We next applied these three basic data mining algorithms using SPSS.

Table 5  
Basic RFM models by cutoff.

<table><tr><td>Cutoff</td><td>R</td><td>F</td><td>M</td></tr><tr><td rowspan="5">0.1</td><td>R=5</td><td>Any</td><td>Any</td></tr><tr><td>R=4</td><td>F=5</td><td>M=3, 4, or 5</td></tr><tr><td>R=3</td><td>F=4</td><td>M=4 or 5</td></tr><tr><td></td><td>F=3</td><td>M=5</td></tr><tr><td></td><td>F=4 or 5</td><td>M=3, 4, or 5</td></tr><tr><td rowspan="2">0.2</td><td>R=5</td><td>F=2, 3, 4, or 5</td><td>Any</td></tr><tr><td>R=4</td><td>F=5</td><td>M=3, 4, or 5</td></tr><tr><td>0.3</td><td>R=5</td><td>F=3, 4, or 5</td><td>M=2, 3, 4, or 5</td></tr><tr><td>0.4</td><td>R=5</td><td>F=4 or 5</td><td>M=2, 3, 4 or 5</td></tr><tr><td>0.5</td><td>R=5</td><td>F=5</td><td>M=3, 4, or 5</td></tr></table>

Table 6  
Balanced group cell densities—training set.

<table><tr><td>RF</td><td>M1</td><td>M2</td><td>M3</td><td>M4</td><td>M5</td></tr><tr><td>55</td><td>186</td><td>185</td><td>149</td><td>223</td><td>187</td></tr><tr><td>54</td><td>185</td><td>186</td><td>185</td><td>185</td><td>186</td></tr><tr><td>53</td><td>187</td><td>185</td><td>188</td><td>186</td><td>187</td></tr><tr><td>52</td><td>184</td><td>184</td><td>185</td><td>184</td><td>185</td></tr><tr><td>51</td><td>186</td><td>187</td><td>186</td><td>187</td><td>186</td></tr><tr><td>45</td><td>268</td><td>265</td><td>270</td><td>289</td><td>246</td></tr><tr><td>44</td><td>269</td><td>269</td><td>268</td><td>274</td><td>264</td></tr><tr><td>43</td><td>272</td><td>267</td><td>280</td><td>251</td><td>296</td></tr><tr><td>42</td><td>263</td><td>263</td><td>265</td><td>245</td><td>283</td></tr><tr><td>41</td><td>268</td><td>261</td><td>261</td><td>259</td><td>277</td></tr><tr><td>35</td><td>331</td><td>330</td><td>349</td><td>316</td><td>330</td></tr><tr><td>34</td><td>324</td><td>325</td><td>322</td><td>325</td><td>324</td></tr><tr><td>33</td><td>332</td><td>331</td><td>329</td><td>332</td><td>335</td></tr><tr><td>32</td><td>330</td><td>330</td><td>330</td><td>331</td><td>330</td></tr><tr><td>31</td><td>323</td><td>324</td><td>323</td><td>326</td><td>324</td></tr><tr><td>25</td><td>733</td><td>730</td><td>735</td><td>737</td><td>733</td></tr><tr><td>24</td><td>735</td><td>736</td><td>735</td><td>737</td><td>734</td></tr><tr><td>23</td><td>747</td><td>746</td><td>751</td><td>749</td><td>748</td></tr><tr><td>22</td><td>705</td><td>704</td><td>707</td><td>704</td><td>707</td></tr><tr><td>21</td><td>731</td><td>733</td><td>730</td><td>735</td><td>732</td></tr><tr><td>15</td><td>1742</td><td>1746</td><td>1739</td><td>1740</td><td>1744</td></tr><tr><td>14</td><td>1718</td><td>1715</td><td>1713</td><td>1713</td><td>1716</td></tr><tr><td>13</td><td>1561</td><td>1809</td><td>1689</td><td>1675</td><td>1684</td></tr><tr><td>12</td><td>1768</td><td>1775</td><td>1771</td><td>1779</td><td>1762</td></tr><tr><td>11</td><td>1830</td><td>1831</td><td>1832</td><td>1824</td><td>1839</td></tr></table>

A logistic regression model was run on RFM variables. The model results were as shown in Table 9. The beta values of R and F are found to be signi<sup>fi</sup>cant.

Note that F was not included at all. This is explainable by the high correlation between M and F, and the dominance of R in obtaining a better <sup>fi</sup>t. This model did very well on the test data, with a correct classi<sup>fi</sup>cation rate of 0.984.

The neural network model used a popular architecture called multilayer perceptron (MLP) [10]. This model built a hidden layer. The rate of neural network was 0.911, as shown in the Appendix A.

Another performance measure used in this study is gains, which is a useful tool for evaluating the value of predictive models in direct marketing [21]. We use gains to compare the performance of RFM score model and classical data mining-based predictive models. Table 11 displays cumulative gains for different deciles for RFM score model, decision tree, logistic regression, and neural networks. This gain-value information is well aligned with the prediction accuracy. The predictive response models based on decision, logistic regression, and neural network signi<sup>fi</sup>cantly outperformed RFM score model. For example, if only 10% of the total customers are selected for direct marketing promotion, the RFM-based predictive model can include only 32.1% of actual respondents in that sampling customer group, those of logistic and neural network are 38.7% and 42.9% respectively. With selecting a group of only 20% of customers, the decision tree-based predictive model can include almost 95% of actual buyers.

Table 7  
Training set proportion of responses by cell.

<table><tr><td>RF</td><td>M1</td><td>M2</td><td>M3</td><td>M4</td><td>M5</td></tr><tr><td>55</td><td>0.129</td><td>0.178</td><td>0.101</td><td>0.673</td><td>0.818</td></tr><tr><td>54</td><td>0.059</td><td>0.118</td><td>0.189</td><td>0.541</td><td>0.629</td></tr><tr><td>53</td><td>0.064</td><td>0.130</td><td>0.287</td><td>0.392</td><td>0.647</td></tr><tr><td>52</td><td>0.076</td><td>0.103</td><td>0.200</td><td>0.424</td><td>0.605</td></tr><tr><td>51</td><td>0.054</td><td>0.102</td><td>0.274</td><td>0.406</td><td>0.527</td></tr><tr><td>45</td><td>0.037</td><td>0.109</td><td>0.141</td><td>0.211</td><td>0.378</td></tr><tr><td>44</td><td>0.041</td><td>0.108</td><td>0.116</td><td>0.281</td><td>0.417</td></tr><tr><td>43</td><td>0.033</td><td>0.052</td><td>0.125</td><td>0.072</td><td>0.483</td></tr><tr><td>42</td><td>0.049</td><td>0.118</td><td>0.098</td><td>0.073</td><td>0.544</td></tr><tr><td>41</td><td>0.045</td><td>0.038</td><td>0.092</td><td>0.116</td><td>0.531</td></tr><tr><td>35</td><td>0.045</td><td>0.067</td><td>0.138</td><td>0.060</td><td>0.458</td></tr><tr><td>34</td><td>0.052</td><td>0.043</td><td>0.059</td><td>0.080</td><td>0.448</td></tr><tr><td>33</td><td>0.042</td><td>0.048</td><td>0.058</td><td>0.093</td><td>0.433</td></tr><tr><td>32</td><td>0.027</td><td>0.045</td><td>0.058</td><td>0.097</td><td>0.379</td></tr><tr><td>31</td><td>0.050</td><td>0.040</td><td>0.062</td><td>0.080</td><td>0.414</td></tr><tr><td>25</td><td>0.037</td><td>0.051</td><td>0.056</td><td>0.084</td><td>0.254</td></tr><tr><td>24</td><td>0.024</td><td>0.046</td><td>0.052</td><td>0.076</td><td>0.309</td></tr><tr><td>23</td><td>0.051</td><td>0.047</td><td>0.055</td><td>0.080</td><td>0.273</td></tr><tr><td>22</td><td>0.027</td><td>0.040</td><td>0.055</td><td>0.068</td><td>0.246</td></tr><tr><td>21</td><td>0.027</td><td>0.038</td><td>0.048</td><td>0.076</td><td>0.242</td></tr><tr><td>15</td><td>0.017</td><td>0.021</td><td>0.025</td><td>0.051</td><td>0.146</td></tr><tr><td>14</td><td>0.016</td><td>0.017</td><td>0.033</td><td>0.054</td><td>0.167</td></tr><tr><td>13</td><td>0.010</td><td>0.019</td><td>0.034</td><td>0.052</td><td>0.156</td></tr><tr><td>12</td><td>0.018</td><td>0.021</td><td>0.036</td><td>0.043</td><td>0.137</td></tr><tr><td>11</td><td>0.016</td><td>0.022</td><td>0.014</td><td>0.044</td><td>0.154</td></tr></table>

Table 8  
V values by cell.

<table><tr><td>Cell</td><td>Min V</td><td>UL</td><td>Hits</td><td>N</td><td>Success</td></tr><tr><td>1</td><td>0.0000</td><td>4077</td><td>91</td><td>4076</td><td>0.0223</td></tr><tr><td>2</td><td>0.0063</td><td>8154</td><td>69</td><td>4077</td><td>0.0169</td></tr><tr><td>3</td><td>0.0097</td><td>12,231</td><td>116</td><td>4077</td><td>0.0285</td></tr><tr><td>4</td><td>0.0133</td><td>16,308</td><td>109</td><td>4077</td><td>0.0267</td></tr><tr><td>5</td><td>0.0171</td><td>20,385</td><td>120</td><td>4077</td><td>0.0294</td></tr><tr><td>6</td><td>0.0214</td><td>24,462</td><td>119</td><td>4077</td><td>0.0292</td></tr><tr><td>7</td><td>0.0263</td><td>28,539</td><td>151</td><td>4077</td><td>0.0370</td></tr><tr><td>8</td><td>0.0320</td><td>32,616</td><td>174</td><td>4077</td><td>0.0427</td></tr><tr><td>9</td><td>0.0388</td><td>36,693</td><td>168</td><td>4077</td><td>0.0412</td></tr><tr><td>10</td><td>0.0472</td><td>40,770</td><td>205</td><td>4077</td><td>0.0503</td></tr><tr><td>11</td><td>0.0568</td><td>44,847</td><td>258</td><td>4077</td><td>0.0633</td></tr><tr><td>12</td><td>0.0684</td><td>48,924</td><td>256</td><td>4077</td><td>0.0628</td></tr><tr><td>13</td><td>0.0829</td><td>53,001</td><td>325</td><td>4077</td><td>0.0797</td></tr><tr><td>14</td><td>0.1022</td><td>57,078</td><td>360</td><td>4077</td><td>0.0883</td></tr><tr><td>15</td><td>0.1269</td><td>61,155</td><td>408</td><td>4077</td><td>0.1001</td></tr><tr><td>16</td><td>0.1621</td><td>65,232</td><td>542</td><td>4077</td><td>0.1329</td></tr><tr><td>17</td><td>0.2145</td><td>69,309</td><td>663</td><td>4077</td><td>0.1626</td></tr><tr><td>18</td><td>0.2955</td><td>73,386</td><td>827</td><td>4077</td><td>0.2028</td></tr><tr><td>19</td><td>0.4434</td><td>77,463</td><td>1134</td><td>4077</td><td>0.2781</td></tr><tr><td>20</td><td>0.7885</td><td>81,540</td><td>1686</td><td>4070</td><td>0.4143</td></tr><tr><td>Total/avg</td><td></td><td></td><td>7781</td><td>81,532</td><td>0.0954</td></tr></table>

For Study 1, we used J48, one of the most popular decision tree algorithms. The J48 decision tree algorithm using 10 fold cross-validation [10] was applied to the dataset. The resultant decision tree was as shown in Table 10.

## 4.2. Study 2

An initial correlation analysis was conducted, showing that there was signi<sup>fi</sup>cant correlation among these variables, as shown in Table 12.

F and M appear to have a strong correlation [45]. R and F appear to be strong predictors for customer response [1]. Table 13 shows RFM limits for this dataset and cell counts.

We built an RFM model by following the same procedures described in Study 1. An RFM model using a cutoff rate of 0.1 was built on half of the dataset, and tested on the other half. This yielded a model with a correct classi<sup>fi</sup>cation rate of 0.662, as reported in the Appendix A. This was far worse than any of the other models tested.

![](/api/attachments/BPXWZ942/fulltext/images/95a51388a755614bc1a980dbd19778f2868226df24243c83fecb4a0d6d920f15.jpg)  
Fig. 2. Lift by value ratio cell.

Table 9  
Regression betas for logistic regression

<table><tr><td>Variable</td><td>Beta</td><td>Significance</td></tr><tr><td>Constant</td><td>-1.5462</td><td>0.05</td></tr><tr><td>R</td><td>-0.0015</td><td>&lt;0.05</td></tr><tr><td>F</td><td>0.2077</td><td>&lt;0.05</td></tr><tr><td>M</td><td>-0.0002</td><td></td></tr></table>

Dif<sup>fi</sup>culties arose in balancing cells due to F being only a few integer values (1, 2, 3, 4, 5+) and highly skewed, letting a majority of the data assigned into F group1.

Fig. 3 displays the lift chart for the V models. The lift chart shows that the 5% of cases with the most likely response is much more likely to respond than the least responsive 50%. The proportion of responses in the test set for the 5% highest training set V scores had a response ratio of 0.311, compared to less than 0.010 for the worst 50%. We applied different V levels (0.05 and up; 0.10 and up; 0.15 and up; 0.20 and up; 0.25 and up; and 0.30 and up). These six models had very consistent results as shown in the Appendix A, just slightly inferior to the degenerate model. When datasets are highly skewed as this is, with roughly only 5% responding, the degenerate model becomes very hard to beat.

All three predictive data mining models (DT, LR, NN) were built as in Study 1. The result is that those three models are performed equally in terms of accuracy (0.938), as shown in Appendix A. We also performed the gain analysis reported in Table 14. The predictive models using decision tree, logistic regression, and neural networks outperformed the RFM Score model. The performance gap is more signi<sup>fi</sup>cant when a small sample size (e.g., 20%) is chosen for donor solicitation.

## 5. Discussion and conclusion

Marketing professionals have found RFM to be quite useful [17,18,35,43], primarily because the data is usually at hand and the technique is relatively easy to use. However, previous research suggests that it is easy to obtain a stronger predictive customer response model with other data mining algorithms [e.g., 1, 19, 20, 24]. RFM has consistently been reported to be less accurate than other forms of data mining models, but that is to be expected, as the original RFM model segmenting customers/donors into 125 cells and is prescriptive rather than predictive.

Table 10  
J48 Decision Tree.

<table><tr><td>R</td><td>M</td><td>Yes</td><td>Total</td><td>P (yes)</td><td>P (no)</td><td>Conclusion</td><td>Error</td></tr><tr><td>0-36</td><td></td><td>1</td><td>1</td><td>1.000</td><td></td><td>Yes</td><td></td></tr><tr><td>37-152</td><td></td><td>41</td><td>619</td><td>0.066</td><td>0.934</td><td>No</td><td>41</td></tr><tr><td>153</td><td></td><td>605</td><td>606</td><td>0.998</td><td>0.002</td><td>Yes</td><td>1</td></tr><tr><td>154-257</td><td></td><td>53</td><td>1072</td><td>0.049</td><td>0.951</td><td>No</td><td>53</td></tr><tr><td>258-260</td><td></td><td>449</td><td>500</td><td>0.898</td><td>0.102</td><td>Yes</td><td>51</td></tr><tr><td>261-516</td><td></td><td>0</td><td>2227</td><td>0.000</td><td>1.000</td><td>No</td><td></td></tr><tr><td>517-519</td><td></td><td>119</td><td>144</td><td>0.826</td><td>0.174</td><td>Yes</td><td>25</td></tr><tr><td>520-624</td><td></td><td>0</td><td>1219</td><td>0.000</td><td>1.000</td><td>No</td><td></td></tr><tr><td>625</td><td></td><td>206</td><td>227</td><td>0.907</td><td>0.093</td><td>Yes</td><td>21</td></tr><tr><td>626-883</td><td></td><td>0</td><td>2047</td><td>0.000</td><td>1.000</td><td>No</td><td></td></tr><tr><td>884</td><td></td><td>51</td><td>68</td><td>0.750</td><td>0.250</td><td>Yes</td><td>17</td></tr><tr><td>885-989</td><td></td><td>0</td><td>1116</td><td>0.000</td><td>1.000</td><td>No</td><td></td></tr><tr><td>990</td><td></td><td>135</td><td>160</td><td>0.844</td><td>0.156</td><td>Yes</td><td>25</td></tr><tr><td>991-1248</td><td></td><td>0</td><td>1773</td><td>0.000</td><td>1.000</td><td>No</td><td></td></tr><tr><td>1249</td><td></td><td>31</td><td>37</td><td>0.838</td><td>0.162</td><td>Yes</td><td>6</td></tr><tr><td>1250-1354</td><td></td><td>0</td><td>985</td><td>0.000</td><td>1.000</td><td>No</td><td></td></tr><tr><td>1355</td><td></td><td>85</td><td>108</td><td>0.787</td><td>0.213</td><td>Yes</td><td>23</td></tr><tr><td>1356-1612</td><td></td><td>0</td><td>1290</td><td>0.000</td><td>1.000</td><td>No</td><td></td></tr><tr><td>1613-1614</td><td></td><td>17</td><td>28</td><td>0.607</td><td>0.393</td><td>Yes</td><td>11</td></tr><tr><td>1615-1720</td><td></td><td>0</td><td>786</td><td>0.000</td><td>1.000</td><td>No</td><td></td></tr><tr><td>1721</td><td></td><td>36</td><td>36</td><td>1.000</td><td>0.000</td><td>Yes</td><td></td></tr><tr><td>1722-2084</td><td></td><td>14</td><td>1679</td><td>0.008</td><td>0.992</td><td>No</td><td>14</td></tr><tr><td>2085-2086</td><td></td><td>18</td><td>18</td><td>1.000</td><td>0.000</td><td>Yes</td><td></td></tr><tr><td>2087-2343</td><td></td><td>0</td><td>831</td><td>0.000</td><td>1.000</td><td>No</td><td></td></tr><tr><td>2344-2345</td><td></td><td>7</td><td>7</td><td>1.000</td><td>0.000</td><td>Yes</td><td></td></tr><tr><td>2346-2448</td><td></td><td>0</td><td>404</td><td>0.000</td><td>1.000</td><td>No</td><td></td></tr><tr><td>2449-2451</td><td>M&gt;44</td><td>21</td><td>24</td><td>0.875</td><td>0.125</td><td>Yes</td><td>3</td></tr><tr><td></td><td>M&lt;=44</td><td>8</td><td>12</td><td>0.667</td><td>0.333</td><td>No</td><td>8</td></tr><tr><td>2452-2707</td><td></td><td>0</td><td>665</td><td>0.000</td><td>1.000</td><td>No</td><td></td></tr><tr><td>2708-2710</td><td></td><td>3</td><td>5</td><td>0.600</td><td>0.400</td><td>Yes</td><td>2</td></tr><tr><td>2711+</td><td></td><td>26</td><td>1306</td><td>0.020</td><td>0.980</td><td>No</td><td>26</td></tr><tr><td>Total</td><td></td><td>1926</td><td>20,000</td><td>0.096</td><td>0.904</td><td></td><td>327</td></tr></table>

Table 12  
Table 11 Gains.

<table><tr><td></td><td>10%</td><td>20%</td><td>30%</td><td>40%</td><td>50%</td></tr><tr><td>RFM score</td><td>32.12</td><td>49.83</td><td>62.24</td><td>72.26</td><td>81.05</td></tr><tr><td>LR</td><td>38.79</td><td>61.67</td><td>70.67</td><td>79.01</td><td>84.85</td></tr><tr><td>DT</td><td>89.62</td><td>95.67</td><td>96.94</td><td>98.21</td><td>99.48</td></tr><tr><td>NN</td><td>42.95</td><td>60.28</td><td>70.21</td><td>79.12</td><td>84.80</td></tr></table>

That expected result was con<sup>fi</sup>rmed in this research. RFM helped nicely structure millions of records in each dataset into 125 groups of customers using only three variables. The model offers a well-organized description of people based on their past behaviors, which helps marketers effectively identify valuable customers or donors and develop a marketing strategy. However, this descriptive approach is less accurate in predicting future behavior than more complex data mining models.

There have been proposed improvements to RFM. In the models seeking to improve RFM, our study showed that increasing the cutoff limit will lead to improvement in prediction accuracy. However, RFM models at any cutoff limit have trouble competing with degenerate models. Degenerate models have high predictive accuracy for highly skewed datasets, but provide no bene<sup>fi</sup>t as they simply conclude it is not worth promoting to any customer pro<sup>fi</sup>le.

Balancing cell sizes by adjusting the limits for the three RFM variables is sound statistically, but did not lead to improved accuracy in our tests. In both Study 1 and Study 2, the basic RFM model signi<sup>fi</sup>- cantly underperformed other predictive models, except the V function model in Study 1. These results indicate that balancing cells might help improve <sup>fi</sup>t, but involves signi<sup>fi</sup>cant data manipulation for very little predictive improvement in the data set we examined.

Using the V ratio is an improvement to RFM that is useful in theory, but in our tests the results are mixed. In Study 1, the technique did not provide better predictive accuracy. In Study 2, it did yield an improved classi<sup>fi</sup>cation rate but underperformed the degeneracy model. Thus, this technique deserves a further inquiry. Overall, the results above indicate that some suggested alternatives to the traditional RFM have limitations in prediction.

The primary conclusion of our study, as was expected, is that classical data mining algorithms outperformed RFM models in terms of both prediction accuracy and cumulative gains. This is primarily because decision tree, logistic regression, and neural networks are often considered the benchmark “predictive” modeling techniques [4,10,29,42]. The demand of predictive modeling or analytics is in high demand in many industries [9], including direct marketing [4]. This implies that marketers can make more effective marketing decisions by embracing advanced predictive modeling techniques, besides popular descriptive models. It often is the case that decision tree, logistic regression, and neural networks vary in their ability to <sup>fi</sup>t speci<sup>fi</sup>c sets of data [34]. Furthermore, there are many parameters that can be used with neural network models and decision trees. All three of these model types have the advantage of being able to consider external variables in addition to R, F, and M. Here, we applied them to these three variables without adding other explanatory variables. All three model types did better than the degenerate case, or any of the other variants we applied.

Variable correlations.

<table><tr><td></td><td>R</td><td>F</td><td>M</td><td>Response</td></tr><tr><td>R</td><td>1</td><td></td><td></td><td></td></tr><tr><td>F</td><td>-0.237**</td><td>1</td><td></td><td></td></tr><tr><td>M</td><td>-0.125**</td><td>0.340**</td><td>1</td><td></td></tr><tr><td>Response</td><td>-0.266**</td><td>0.236**</td><td>0.090**</td><td>1</td></tr></table>

Correlation is signi<sup>fi</sup>cant at the 0.01 level (2-tailed).

![](/api/attachments/BPXWZ942/fulltext/images/750a5e94c395504f4f68bdcf451b35210450d104467ded3028c3d19925ab3dcb.jpg)  
Fig. 3. Lift chart for study 2.

The best overall predictive <sup>fi</sup>t was obtained using the decision tree model. This model also outperformed other predictive models in cumulative gains in both studies. Decision tree tends have advantages over low dimensionality datasets [34] like those used in this research. This characteristic of decision tree may explain this result. Thus, we do not contend that decision tree will always be best. However, there is a major relative value for decision trees that they provide an easily understandable model. For example, Table 10 presents the decision tree rule sets obtained in Study 1, which amounts to enumerating ranges of R that had high densities of response. There was only one range where M was used (R=2449 to R=2451). And looking at Table 10, the <sup>fi</sup>t would have been improved if the decision tree had not differentiated and called all of these cases Yes. (There would have been 4 fewer errors out of 20,000, yielding essentially the same <sup>fi</sup>t with the same correct response of 0.984.) There is the downside for decision trees that they often over<sup>fi</sup>t the data (as they did in Table 10), and can yield an excessive number of rules for users to apply. Table 15 presents a comparison of methods based on inferences from our two studies.

While our study uses predication accuracy along with cumulative gains for model comparison, in practice the type of error can be considered in terms of relative costs, thus enabling in<sup>fl</sup>uence on pro<sup>fi</sup>t. For example, our study shows that increasing the cutoff level between predicting response or not can improve correct classi<sup>fi</sup>cation. However, a more precise means to assess this would be to apply the traditional cost function re<sup>fl</sup>ecting the cost of the two types of error. This is to be a consideration in evaluating other predictive models as well. Thus, speci<sup>fi</sup>c models should be used in light of these relative costs.

The good performance of those data mining methods (particularly decision tree), in terms of prediction accuracy and cumulative gains, indicates that three variables (R, F, and M) alone can be useful for building a reliable customer response model. This echoes the importance of RFM variables in understanding customer purchase behavior and developing response models for marketing decisions [17,18,33,35]. Previous research [e.g., 1] also shows that inclusion of non-RFM attributes (e.g., income) is likely to slightly improve the model performance.

Table 13 REM boundaries

<table><tr><td>Factor</td><td>Min</td><td>Max</td><td>Group 1</td><td>Group 2</td><td>Group 3</td><td>Group 4</td><td>Group 5</td></tr><tr><td>R</td><td>1</td><td>4950</td><td>2811+</td><td>1932-2811</td><td>935-1932</td><td>257-935</td><td>1-257</td></tr><tr><td>Count</td><td></td><td></td><td>220,229</td><td>219,411</td><td>220,212</td><td>219,503</td><td>219,654</td></tr><tr><td>F</td><td>1</td><td>1027</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5+</td></tr><tr><td>Count</td><td></td><td></td><td>599,637</td><td>190,995</td><td>95,721</td><td>57,499</td><td>155,157</td></tr><tr><td>M</td><td>0</td><td>100,000</td><td>0-9</td><td>10-24</td><td>25-39</td><td>40-89</td><td>90+</td></tr><tr><td>Count</td><td></td><td></td><td>248,639</td><td>343,811</td><td>77,465</td><td>209,837</td><td>219,257</td></tr></table>

Table 14 Gains.

<table><tr><td></td><td>10%</td><td>20%</td><td>30%</td><td>40%</td><td>50%</td></tr><tr><td>RFM score</td><td>40.38</td><td>62.39</td><td>84.66</td><td>95.63</td><td>97.90</td></tr><tr><td>LR</td><td>43.24</td><td>66.22</td><td>86.10</td><td>95.75</td><td>99.75</td></tr><tr><td>DT</td><td>44.68</td><td>70.75</td><td>87.41</td><td>96.63</td><td>97.96</td></tr><tr><td>NN</td><td>43.64</td><td>67.58</td><td>86.12</td><td>95.75</td><td>99.77</td></tr></table>

However, a sophisticated model with too many variables is not very effective for marketing practitioners [19] and reducing variables is important for practical use of predictive models [28]. Marketers should be aware of this tradeoff between a simple model (with fewer variables) and a sophisticated model (with a large number of variables) and develop a well-balanced model using their market and product knowledge.

To repeat the contributions of this paper given in the Introduction, we have demonstrated how RFM models and variants can be implemented. RFM models have the relative advantage that they are simple in concept, and thus understandable to users. However, they can easily be improved in terms of predictive accuracy (or pro<sup>fi</sup>tability, given situational data) by using classical data mining models. Of these traditional data mining models, decision trees are especially attractive in that they have easily understood output. These advanced predictive models are much bene<sup>fi</sup>cial in the practice of direct marketing since they can use only three behavioral input variables and generate the results signi<sup>fi</sup>cantly better than the traditional RFM model and other variants.

Table 15  
Comparison of methods.

<table><tr><td>Model</td><td>Relative advantages</td><td>Relative disadvantages</td><td>Inferences</td></tr><tr><td>Degenerate</td><td>Tends to have high accuracy when outcome highly skewed</td><td>Mindless Simply says no Provides no marginal value</td><td>If cost of missing good responses is low, don&#x27;t do anything</td></tr><tr><td>Basic RFM</td><td>Widely used Data readily available Software obtainable</td><td>Predictive accuracy consistently weak</td><td>Can do better using conventional data mining (RFM implicitly a special case)</td></tr><tr><td>RFM with balanced data</td><td>Better statistical practice</td><td>May not actually improve accuracy</td><td>Not worth the trouble</td></tr><tr><td>Value function</td><td>Easy to apply (uses 2 of the 3 RFM variables, so data readily available) Focuses on uncorrelated variables</td><td>Not necessarily more accurate</td><td>Value function is superior to RFM</td></tr><tr><td>Logistic regression</td><td>Can get better fit Can include many variables Model statistically interpretable</td><td>Logistic output harder to interpret than OLS for managers</td><td>Decision trees easier to interpret</td></tr><tr><td>Neural network</td><td>Can get better fit Can include many variables</td><td>Output not conducive to interpretation Can&#x27;t apply model outside of software used to build model</td><td>Decision trees easier to interpret</td></tr><tr><td>Decision trees</td><td>Can get better fit Can include many variables Output easily understandable by managers</td><td>Model may involve an excessive number of rules</td><td>Best option, if can control the number of rules obtained (through minimum required response parameter)</td></tr></table>

Appendix A. Comparative model results — Study 1

<table><tr><td>Model</td><td>Actual no response, model response</td><td>Actual response, model no response</td><td>Correct response</td><td>Overall correct classification</td></tr><tr><td>Degenerate</td><td>0</td><td>1926</td><td>18,074</td><td>0.904</td></tr><tr><td>Basic RFM on 0.1</td><td>4113</td><td>589</td><td>15,298</td><td>0.765</td></tr><tr><td>Basic RFM on 0.2</td><td>1673</td><td>999</td><td>17,328</td><td>0.866</td></tr><tr><td>Basic RFM on 0.3</td><td>739</td><td>1321</td><td>17,940</td><td>0.897</td></tr><tr><td>Basic RFM on 0.4</td><td>482</td><td>1460</td><td>18,058</td><td>0.903</td></tr><tr><td>Basic RFM on 0.5</td><td>211</td><td>1643</td><td>18,146</td><td>0.907</td></tr><tr><td>Balance using 0.5</td><td>1749</td><td>379</td><td>17,872</td><td>0.894</td></tr><tr><td>Value function</td><td>623</td><td>4951</td><td>14,426</td><td>0.721</td></tr><tr><td>Logistic regression</td><td>1772</td><td>91</td><td>18,137</td><td>0.907</td></tr><tr><td>Neural network</td><td>119</td><td>1661</td><td>18,220</td><td>0.911</td></tr><tr><td>Decision tree</td><td>185</td><td>142</td><td>19,673</td><td>0.984</td></tr></table>

## Comparative model results — Study 2

<table><tr><td>Model</td><td>Actual no response, model response</td><td>Actual response, model no response</td><td>Correct response</td><td>Overall correct classification</td></tr><tr><td>Degenerate</td><td>0</td><td>34,598</td><td>515,123</td><td>0.9371</td></tr><tr><td>Basic RFM</td><td>4174</td><td>181,357</td><td>364,190</td><td>0.6625</td></tr><tr><td>Value function &gt;5</td><td>6212</td><td>30,418</td><td>513,091</td><td>0.9334</td></tr><tr><td>Value function&gt;10</td><td>3344</td><td>31,830</td><td>514,547</td><td>0.9360</td></tr><tr><td>Value function&gt;15</td><td>2296</td><td>32,475</td><td>514,950</td><td>0.9367</td></tr><tr><td>Value function&gt;20</td><td>1712</td><td>32,867</td><td>515,142</td><td>0.9371</td></tr><tr><td>Value function&gt;25</td><td>1400</td><td>33,136</td><td>515,185</td><td>0.9372</td></tr><tr><td>Value function&gt;30</td><td>1153</td><td>33,330</td><td>515,238</td><td>0.9373</td></tr><tr><td>Logistic regression</td><td>821</td><td>32,985</td><td>515,915</td><td>0.9385</td></tr><tr><td>Neural network</td><td>876</td><td>32,888</td><td>515,957</td><td>0.9386</td></tr><tr><td>Decision tree</td><td>393</td><td>33,373</td><td>515,955</td><td>0.9386</td></tr></table>

## References

[1] B. Baesens, S. Viaene, D. den Poel, J. Vanthienen, Bayesian neural network learning for repeat purchase modelling in direct marketing, European Journal of Opera tional Research 138 (2002) 191–211.

[2] N. Belacel, H. Raval, A. Punnen, Learning multicriteria fuzzy classi<sup>fi</sup>cation method PROAFTN from data, Computers and Operations Research 34 (7) (2007) 1885–1898

[3] R. Blattberg, B. Kim, S. Neslin, Database Marketing: Analyzing and Managing Cus tomers, Chapter 2 RFM Analysis, Springer, New York, 2008

[4] I. Bose, X. Chen, Quantitative models for direct marketing: a review from systems perspective, European Journal of Operational Research 195 (2009) 1–16.

[5] J. Bult, T. Wansbeek, Optimal selection for direct mail, Marketing Science 14 (4) (1995) 378–394

[6] C. Cheng, Y. Chen, Classifying the segmentation of customer value vis RFM model and RS theory, Expert Systems with Applications 36 (3) (2009) 4176–4184.

[7] W. Chiang, To mine association rules of customer values via a data mining procedure with improved model: an empirical case study, Exper Systems with Applications 38 (2011)1716-1722

[8] G. Cui, M. Wong, H. Lui, Machine learning for direct marketing response models: Bayesian networks with evolutionary programming, Management Science 52 (4) (2006) 597–612.

[9] T. Davenport, J.G. Harris, R. Morison, Analytics at Work: Smarter Decisions, Better Results Harvard Business Press Boston MA 2010

[10] D. Delen, A comparative analysis of machine learning techniques for student retention management, Decision Support Systems 49 (2010) 498–506.

[11] E. Eisenstein, L. Lodish, Marketing decision support and intelligence systems: precisely worthwhile or vaguely worthless? In: in: B. Weitz, R. Wensley (Eds.), Hand book of Marketing, Sage Publication, London, 2002.

[12] R. Elsner, M. Krafft, A. Huchzemeier, Optimizing Rhenania's main-order business through dynamic multilevel modeling, Interfaces 33 (1) (2003) 50–66.

[13] P. Fader, B. Hardie, K. Lee, RFM and CLV: using iso-value curves for customer base analysis, Journal of Marketing Research 42 (4) (2005) 415–430.

[14] M. Fitzpatrick, Statistical analysis for direct marketers — in plain English, Direct Market 64 (4) (2001) 54–56

[15] R. Gopal, Ad mediation: new horizons in effective email advertising, Communications of the ACM 19 (1) (2001) 17–30.

[16] M. Hart, Systems for supporting marketing decisions, In: in: F. Burstein, C. Holsapple (Eds.), Handbook on Decision Support Systems, 2, Springer, 2008, pp. 395–418.

[17] A. Hughes, Strategic Database Marketing, Third ed. McGraw-Hill, New York, 2006

[18] J. Jonker, N. Piersma, R. Potharst, A decision support system for direct mailing deci sions, Decision Support Systems 42 (2006) 915–925.

[19] Y. Kim, W. Street, An intelligent system for customer targeting: a data mining approach, Decision Support Systems 37 (2004) 215–228.

[20] N. Levin, J. Zahavi, Predictive modeling using segmentation, Journal of Interactive Marketing 15 (2) (2001) 2–22.

[21] G. Linoff, M. Berry, Data Mining Techniques, Wiley, Indianapolis, 2011.

[22] J. Little, Decision support systems for marketing managers, Journal of Marketing 43 (3) (1979) 9–26.

[23] N. Mastrogiannis, B. Boutsinas, I. Giannikos, A method for improving the accuracy of data mining classi<sup>fi</sup>cation algorithms, Computers and Operations Research 36 (10) (2009) 2829–2839.

[24] J. McCarthy, M. Hastak, Segmentation approaches in data-mining: a comparison of RFM, CHAID, and logistic regression, Journal of Business Research 60 (6) (2007) 656–662.

[25] R. McDaniel, Management strategies for complex adaptive systems, Performance Improvement Quarterly 20 (2) (2007) 21–42.

[26] B. McKelvey, Avoiding complexity catastrophe in coevolutionary pockets: strategies for rugged landscape, Organization Science 10 (3) (1999) 294–321.

[27] J. Miglautsch, Application of RFM principles: what to do with 1-1-1 customers? Journal of Database Marketing 9 (4) (2002) 319–324.

[28] P. Naik, M. Hagerty, C. Tsai, A new dimension reduction approach for data-rich marketing environments, Journal of Marketing Research 37 (1) (2000) 88–101.

[29] E.W.T. Ngai, L. Xiu, D.C.K. Chau, Application of data mining techniques in customer relationship management: a literature review and classi<sup>fi</sup>cation, Expert Systems with Applications 36 (2) (2009) 2592–2602.

[30] C. O'Reilly III, J. Harreld, M. Tushman, Organizational ambidexterity: IBM and emerging business opportunities, California Management Review 51 (4) (2009) 75–99.

[31] D. Olson, Q. Cao, C. Gu, D. Lee, Comparison of customer response models, Service Business 3 (2) (2009) 117–130.

[32] D.L. Olson, D. Delen, Advanced Data Mining Techniques, Springer, Heidelberg, 2008.

[33] P. Rossi, R. McCulloch, G. Allenby, The value of purchase history data in target marketing, Marketing Science 15 (4) (1996) 321–340.

[34] G. Seni, J. Elder, Ensemble Methods in Data Mining: Improving Accuracy Through Combining Predictions, Morgan & Claypool, 2010.

[35] M. Shaw C. Subramaniam G. Tan M. Welge Knowledge management and data mining for marketing, Decision Support Systems 31 (2001) 127–137.

[36] K.A. Smith, J. Gupta, Neural networks in business: techniques and applications for the operations researcher, Computers and Operations Research 27 (11/12) (2000) 1023–1044.

[37] E. Turban, J. Aronson, T. Liang, Decision Support Systems and Intelligent Systems, 7th ed. Prentice Hall, Upper Saddle River, NJ, 2004.

[38] E. Turban, R. Sharda, D. Delen, D. King, Business Intelligence: A Managerial Approach, 2nd ed Prentice Hall New York, 2011

[39] B. Van den Berg, T. Breur, Merits of interactive decision tree building: part 1, Journal of Targeting, Measurement and Analysis for Marketing 15 (3) (2007) 137–145.

[40] B. Van den Berg, T. Breur, Merits of interactive decision tree building: part 2: how to do it journal of targeting, Measurement & Analysis for Marketing 15 (4) (2007) 201–209.

[41] S. Vargo, R. Lusch, Evolving to a new dominant logic for marketing, Journal of Marketing 68 (2004) 1–17.

[42] G. Verhaert, D. Poel, Empathy as added value in predicting donation behavior, Journal of Business Research 64 (2011) 1288–1295

[43] P. Verhoef, P. Spring, J. Hoekstra, P. Lee<sup>fl</sup>ang, The commercial use of segmentation and predictive modeling techniques for database marketing in the Netherlands, Decision Support Systems 34 (2002) 471–481.

[44] B. Wierenga, The past, the present and the future of marketing decision models, In: in: B. Wierenga (Ed.), Handbook of Marketing Decision Models, Springer, 2008, pp. 3–20.

[45] A. Yang, How to develop new approaches to RFM segmentation, Journal of Targeting, Measurement and Analysis for Marketing 13 (1) (2004) 50–60.

[46] H. Yun, D. Ha, B. Hwang, K. Ryu, Mining association rules on signi<sup>fi</sup>cant rare data using relative support, Journal of Systems and Software 67 (181–191) (2003).

[47] J. Zahavi, N. Levin, Applying neural computing to target marketing, Journal of Direct Marketing 11 (1) (1997) 5–22.

David L. Olson is the James & H.K. Stuart Professor in MIS and Chancellor's Professor at the University of Nebraska. He has published research in over 100 refereed journal articles, primarily on the topic of multiple objective decision-making and information technology. He has authored 17 books, is associate editor of Service Business and co-editor in chief of International Journal of Services Sciences. He has made over 100 presentations at international and national conferences on research topics. He is a member of the Decision Sciences Institute, the Institute for Operations Research and Management Sciences, and the Multiple Criteria Decision Making Society. He was a Lowry Mays endowed Professor at Texas A&M University from 1999 to 2001, He was named the Raymond E. Miles Distinguished Scholar award for 2002, and was a James C. and Rhonda Seacrest Fellow from 2005 to 2006. He was named Best Enterprise Information Systems Educator by IFIP in 2006. He is a Fellow of the Decision Sciences Institute.

Bongsug (Kevin) Chae is Associate Professor in Information & Operations Management at Kansas State University. He has published papers in such areas as business analytics, supply chain management, service innovation, and knowledge discovery. He has made presentations in universities and global companies in several countries, primarily on the topic of business analytics and intelligence, supply chain management, and service innovation. He is a recipient of the Ralph Reitz Teaching Award and a nominee of several other teaching awards at Kansas State University.
