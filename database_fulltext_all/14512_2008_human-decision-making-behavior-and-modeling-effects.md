---
otero_id: 14512
otero_key: "PU2HM29E"
title: "Human decision-making behavior and modeling effects"
authors: "Choong Nyoung Kim; Kyung Hoon Yang; Jaekyung Kim"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2007.06.011"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Human decision-making behavior and modeling effects

Choong Nyoung Kim <sup>a,⁎</sup>, Kyung Hoon Yang <sup>b</sup>, Jaekyung Kim <sup>c</sup>

<sup>a</sup> Department of Management, University of Seoul, Dongdaemun-Gu Jeonnong-Dong 90 Seoul, South Korea Department of Information Systems, University of Wisconsin-La Crosse, 1725 State Street, La Crosse, WI, USA <sup>c</sup> Department of Management, University of Nebraska–Lincoln, Lincoln, NE, USA

Available online 23 June 2007

## Abstract

Previous research indicates that the human decision-making process is quite non-linear and that non-linear models would be more suitable than linear models for developing advanced decision-making models. In our study, we tested this generally held hypothesis by applying linear and non-linear models to experts' decision-making behavior and measuring the predictive accuracy (predictive validity) and valid non-linearity. As a result, we found that non-linearity in the decision-making process is positively related to the predictive validity of the decision. Secondly, in modeling the human decision-making process, we found that valid non-linearity is positively related to the predictive validity of non-linear models. Thirdly, we found that the more non-linearity is inherent in the decision-making process, the more non-linear models are effective. Therefore, we suggest that a preliminary analysis of the characteristics of expert decision-making is needed when knowledge-based models such as expert systems are being developed. We also verify that the lens model is effective in evaluating the predictive validity of human judgment and in analyzing the validity and non-linearity of the human decision-making process. © 2007 Elsevier B V All rights reserved

Keywords: Valid non-linearity and predictive validity in human decision-making behavior; Modeling effect; Predictive accuracy; Human judgment; Lens model analysis

## 1. Introduction

A great number of studies on human decisionmaking and judgment have been made in the field of social science, and a variety of methodologies have been researched [9]. Understanding the human decisionmaking process and the modeling of the decisionmaking process is one of the goals of this discipline [17]. Studies on decision-making can be classified into two categories: the study of decision modeling and the study of decision process tracing [19,30].

Decision modeling studies the human decisionmaking mechanism and tries to build models that predict human decisions. This field has been researched under the name of expert systems in the discipline of management, and the findings are abundant [5,8,14, 22,31]. Examples of findings include the development of new algorithms for building decision-making models and the development of methodologies for a knowledge base. In the past, studies were focused on modeling that resembled expert decisions and judgment. However, using enormous amounts of real data, recent studies have rigorously investigated the modeling of rules and associations. The application of these results has been expanded to a variety of areas, such as finance $( \mathrm { e . g . }$ bankruptcy prediction and stock price index prediction), marketing, account auditing, credit rating, and venture investment decision-making [33,34,36].

Decision process tracing, the other paradigm of study for human decision-making, focuses on the process of judgment and decision-making. To measure the predictive validity of human judgment, this research has introduced various methods for the analysis of the decision-making process [13] these methods include probability scoring rules, log transformation, and the lens model. In probability scoring rules, mean probability scores (MPS) are viewed as efficient tools for measuring the level of uncertainty [19,35]. Einhorn [11,12] suggested log transformation to classify types of human decision strategies. The lens model, proposed by Brunswick [6] and developed by Tucker [32], describes decision-making behavior in terms of linearity and nonlinearity. This model also provides the tools to measure the predictive validity of the linear and non-linear parts of decision-making behavior. The effectiveness of the lens model has been verified by various empirical studies [17,19,28,37].

Decision modeling and decision process tracing are not independent because the research in both fields has a common goal which is to improve decision quality by analyzing and understanding human decisionmaking behaviors. Therefore, a combination of these two areas of research presents several meaningful issues. First, decision process tracing methods can be used in evaluating the predictive validity of decisionmaking models. Second, an extensive analysis of the decision process tracing methods can help develop an advanced decision-making model. Third, this combined approach may explain the reasons why non-linear models and statistical linear models show contradictory results for the same problem. Even though many researchers [19] insist that non-linear models, such as the neural network model, show better performance in some studies, much research still shows that statistical linear models are better in many fields. When we take into account the fact that the performance of a model depends on the input data as well as the model itself, it would be reasonable to include characteristics of the input data, in addition to the features of decision-making behaviors when evaluating the model's predictive validity. This inclusion would be helpful in explaining the contradictory results between previous behavioral accounting studies, which assert the superiority of the statistical linear model, and recent studies, which assert the superiority of the non-linear model. Also, this contradiction might have occurred, not because of the model, but because of the input data. If the predictive validity of the decision-making model is affected by the level of the linearity/non-linearity of the problem and by the validity of the input data, this should be taken into account in the selection of model development techniques.

In respect to these issues, we analyzed decision-making, studied model building and evaluation, and investigated the relationship between the characteristics of decisionmaking behavior (non-linearity and its validity) and the predictive validity of the models.

## 2. Literature review

## 2.1. Decision process tracing

The analytical framework needed to understand the human decision-making process was borrowed from studies on human judgment in the cognitive psychology discipline [36]. The decision-making process is a major branch of decision-making studies. Finding the key factors affecting the decision-making process has been a core research topic of previous studies. As a consequence of this research, types and characteristics of decision-making behavior and measuring methods and/ or models have been developed [13,24]. For instance, mean probability scores (MPS) were considered a useful method to measure predictive accuracy [19]. MPS is a function of squares of the deviation score between predicted values and actual outcome values. The formula of MPS is shown in Fig. 1.

MPS, which is an error measurement method, is widely used for assessing human predictive validity along with the hit ratio [19]. The value of MPS is between 0 and 1, and $\mathrm { ^ { 6 6 } M P S = 0 ^ { 3 9 } }$ means that all predictions are accurate, while $\mathbf { \hat { M P S } } = 1 \mathbf { \ ' }$ means that all predictions are inaccurate. For example, if a certified public accountant (CPA) predicted the possibility of bankruptcy for two banks, A and B, with the possibility 0.7 and 0.6 respectively, and they actually bankrupted later, the hit ratio is 100%, and the MPS is 0.125 $( [ ( 1 - 0 . 7 ) ^ { 2 } + ( 1 - 0 . 6 ) ^ { 2 } ] / 2 )$

Einhorn [11], [12] assumed that human decisionmaking behavior is non-linear rather than linear.

$$
M P S = \frac {\sum (\text { outcome   -   prediction }) ^ {2}}{N}
$$

where

Outcome: actual result with values 0 or 1

Prediction: probabilistic prediction with values between 0 and 1

Fig. 1. Mean probability score.

Furthermore, they provided methods for classifying human decision-making behavior into two types conjunctive and disjunctive. This classification has been verified by several researchers [18].

First proposed by Brunswick [6], the lens model has been developed by others [15,32] to investigate the use of non-linearity in human decision-making behavior. Many behavioral accounting researchers have discussed the use of the lens model with regard to the examination of a human judgment [21]. A detailed description of the lens model appears in Kim and McLeod [17].

## 2.2. Research on the decision-making model

Since the 1960s, research on decision-making has been explored in accounting and management sciences, as well as in many other fields. Main concerns were how to mimic human decision-making and determine if a model predicts better than human experts do. This is why the research in this field was called “Judgmental Bootstrapping.” A number of empirical results support the value of judgmental bootstrapping [23]. Key modeling methods are linear, such as linear regression analysis and discriminant analysis. Although there is research that shows otherwise [8,20,27], most experimental studies found that linear models predict the actual outcome more accurately than human experts do [10,19]. Previous researchers in this field state that these kinds of positive results are due to the simple linearity of the model, which reduces the judgmental inconsistency of human decision-making behavior [17,29].

Since the late 1970s, studies on decision-making models in the field of management have continued with expert system and artificial intelligence research. Several modeling methodologies and algorithms have been researched to extract expert knowledge and decision-making behavior. One of these methodologies is the inductive learning approach, which treats input data as non-linear. Quinlan's [26] ID3 (also evolved to C5 later) is the most widely used algorithm in inductive learning approaches. ID3 represents the human decision process as a tree-structured model and shows a very prominent prediction accuracy compared to traditional statistical approaches. ID3 shows a higher prediction accuracy, especially when sample data are stable with less noise [17]. In its earlier stage of development, ID3 could only treat discrete data and make a binary classification; however, as it has evolved, it can also handle continuous data, making more sophisticated classifications possible. The other approach is neural network, which is broadly applied in modeling management decision-making. Neural network models are widely used in a variety of applications because they are free from statistical assumptions, making it easy to find nonlinear relationships among input and output variables. Furthermore, they show better performance in dealing with noisy sample data.

2.3. Comparative studies for the linear and non-linear models

The decision-making model is mainly applied to classification and/or prediction problems. Most classification researchers have used hit ratio for the performance evaluation criterion. They have also used statistical models, such as regression analysis, discriminant analysis, and logistic analysis, which are based on linear relationships among variables [8]. These statistical models have been used mainly to analyze and model expert decision-making behavior in behavioral sciences such as psychology and behavioral accounting, where they have proved their prowess [3,7,10]. Non-linear models, such as neural network and tree structure have been evaluated by comparing their results with those of statistical linear models, which have been considered reliable [8].

However, Chung and Silver [8] argued that the comparison of non-linear and linear models was only based on input data without considering the type of tasks or decision-making behavior to which the methods were applied. Previous research on expert systems also committed these kinds of mistakes without considering circumstantial factors such as the characteristics of input data and the expert's behavior in the research model design. Characteristics of data or those of an algorithm in models may also distort the model performance. For example, the degree of linearity and non-linearity of input data can distort the performance of a model when a linear model analyzes the non-linearity of input data or a non-linear model analyzes the linearity of input data.

Therefore, a comparison study should consider both the linearity/non-linearity of the input data and the linearity/non-linearity of the model. An analysis of environmental factors, such as the characteristics of input data and the participating expert's behavior, should come first; and the result of the preliminary analysis should be used in the performance evaluation of models.

There is a second issue. In previous research, hit ratio was popularly used as a performance index in expert systems. In this case, much information can be lost since the decision is always “0” or “1”. Therefore, the hit ratio may not be appropriate as a performance measurement because it does not reflect the level of uncertainty and/or competence of the expert's knowledge, experience, or judgment. To overcome this limitation, an additional performance index is required to measure the predictive validity more accurately.

Consequently, it is believed that when evaluating model performance, the model should include environmental factors such as the characteristics of input data and the participating expert's behavior, as well as the uncertainty and competence of the expert's knowledge, experience, or judgment.

## 2.4. Research objectives

It seems that a combination of research on decisionmaking modeling and on decision process tracing would be valuable not only theoretically but also practically, as Svenson [30] has insisted. But, despite his intention to that effect, there has been a lack of effort put into this kind of research. In this study, we analyze the findings and methods of both types of research and combine them to overcome the weakness of each. Through our analysis, we expect to find a relationship between characteristics of decision-making behavior and modeling methods. This study focuses on human decision-making behavior and the validity of the decision-making behavior. More specifically, linear and non-linear behavior is differentiated, and the validity of non-linear behavior is examined. To do this, the C index of lens model analysis is used, which is intended to represent the valid non-linearity in decision-making behavior [3,17,19].

This study has three objectives. First, we analyze the experts' decision-making strategies in terms of linearity, non-linearity, and validity of non-linearity with the C index of lens model analysis. A high C index value indicates the existence of valid non-linearity in decisionmaking behavior, which contributes to the predictive validity of the human decision maker. Second, predictive models for each human subject are built based upon one linear and two non-linear algorithms, and model performance is compared in terms of MPS as well as hit ratio. The correlations between the predictive validity of models and the C index of each subject are examined. Third, this study analyzes the argument of the previous research [17,20] concerning the relationship between the model performance and the human experts: “The more valid (accurate) human subject modeled, the less bootstrapping by linear models is likely because linear models cannot capture the valid non-linear decision behavior of the human subject.” We seek to find which type of model is more valid for prediction when valid non-linearity is inherent in decision-making behavior. This approach may reveal that the conflicting results of previous comparative studies [7,8,10,18,19,22] between statistical linear models and non-linear models were caused by the non-linear characteristics of decisionmaking behavior or the non-linear properties of the input data.

## 2.5. Research model and hypotheses

Two hypotheses concerned with the objectives were developed.

Hypothesis 1. Valid non-linearity of decision-making is positively related to the predictive accuracy of a nonlinear model, but not positively related to the predictive accuracy of a linear model.

This hypothesis is based on the presumption that human decision-making is basically non-linear [2,4,11, 18,20,21], and the validity of decision-making is decided by valid non-linearity [12,20]. Validity means the predictive accuracy of decision-making, and valid nonlinearity is defined as the non-linear portion that affects the accuracy of decision-making. We expect that, since valid non-linearity of decision-making is explained better by a non-linear model, a non-linear model leads to better predictive validity than a linear model if there is valid non-linearity decision-making behavior. To examine the valid non-linearity in the subjects' decisionmaking behavior, C index is a useful and general measure [17–19,32]. Since the valid non-linearity should be captured more successfully by non-linear algorithms, a high C index value should be correlated with the predictive validity of non-linear models.

Hypothesis 2. As the validity of a subject's decisionmaking increases, the modeling effect of a linear model significantly decreases to a greater extent than the modeling effect of a non-linear model.

Hypothesis 2 is concerned with Libby's argument [20], which asserts the limitation of linear algorithms in simulating or modeling human experts' decisionmaking behavior. To test the argument [20], the concept of modeling effect is used [17,20]. The modeling effect is defined as the improvement of the predictive validity by modeling the human decision-making behavior. It is expressed as the incremental accuracy of the model over the accuracy of a human subject (computed by subtracting the validity of a human subject from the accuracy of the model of the human subject) [17].

By testing the two hypotheses, we can explore the relationship between the model's predictive validity and decision-maker's behavioral characteristics. Fig. 2 depicts our research model and hypotheses.

![](/api/attachments/PU2HM29E/fulltext/images/a9a5a930f431c62f701842d4efb5495ce02326b7ddbf01b2e316efa8031d5485.jpg)  
Fig. 2. Research model.

## 3. Research method

## 3.1. Task: bankruptcy prediction

We chose bankruptcy prediction as the experimental task to test our research hypotheses. Bankruptcy prediction has been one of the most frequently studied human decision-making tasks since Altman's research [1]. As a result, we can compare our study to many previous studies. Bankruptcy prediction is also directly related to many applications, such as credit ratings, bank loans, and venture investment decisions [17,22,31,36].

## 3.2. Data and participants

Our data was obtained from thirty bankrupted and thirty non-bankrupted companies in the U.S. in 1985. To maintain the consistency of data quality, we extracted sample companies from the same industry (manufacturing) with a similar size of about \$50 million in average assets. We used financial data for the two years prior to bankruptcy for each company. We kept the names of the companies anonymous. The ten most frequently used financial ratios from previous studies [16,17] were considered: 1) net income / total assets (profitability), 2) current assets / sales (Activity), 3) current assets / current liability (liquidity ratio), 4) current assets / total assets (asset balance), 5) cash/ total assets (cash position), 6) total debt / total assets (financial leverage), 7) [current assets − current liability] / total assets (relative working capital), 8) sales / total assets (sales-generating ability of assets), 9) retained earnings / total assets (cumulative profitability), 10) [current assets / current liability] / sales (working capital turnover).

Participants were selected from two groups: One group consisted of 16 experts who worked as certified public accountants (CPAs) or as financial CEOs who have CPA experience; the other consisted of 24 graduate students majoring in finance and accounting. To increase reliability, we adopted the test–retest approach. First, participants were asked to predict the bankruptcy/ no-bankruptcy status of 70 cases. They were asked 10 cases twice, for a total 60 different cases. The participants whose prediction rate for the ten duplicated cases was lower than 80% consistent were eliminated. Eight students were eliminated, and 32 participants were selected. We expected that the prediction accuracy and the decision-making behaviors of the two groups would be different.

## 3.3. Experiment procedure

The experiment in this study consists of three steps. In the first step, each participant predicts the bankruptcy possibility of 60 sample companies. Each participant makes two types of predictions: a binary decision and a probability prediction. In the binary decision, each company is labeled as either “0” (bankruptcy) or “1” (no-bankruptcy). In the probability prediction, each company is labeled by a ten-level, quasi-continuous scale based on the participant's confidence in the decision. If a participant predicts bankruptcy for a company, he/she may choose from “0.0” to “0.4,” where “0.0” implies the highest confidence and “0.4” the lowest confidence of bankruptcy.

If a participant predicts no-bankruptcy, he/she chooses a value from $^ { \mathrm { 6 6 } } 0 . 6 ^ { \circ }$ to “1.0,” where $^ { 6 6 } 1 . 0 ^ { 5 }$ means the highest confidence and $^ { \mathrm { 4 6 } } 0 . 6 ^ { \circ }$ the lowest confidence of no-bankruptcy. The reason that we use both the binary decision and the probability prediction is that certain types of algorithms cannot be fairly evaluated if the object variable is considered as either discrete or continuous.

In the second step, the prediction performance of each participant is evaluated by the hit ratio and MPS. The portion of non-linearity in the decision-making and the validity of non-linearity are also examined by the lens model's C index and $R _ { \mathrm { a } }$ [17,23]. The lens model consists of two types of linear models. One is the linear regression model of a participant's bankruptcy prediction and the independent variables of ten financial ratios, and the other is the regression model of the actual result of bankruptcy and the independent variables. The quasicontinuous value of a participant's prediction confidence was used as a dependent variable in the regression model.

In the third step, prediction models are developed based on each participant's prediction. Statistical linear regression is adopted for the linear model, and Quinlan's [26] C4.5 and the back-propagation paradigm of neural network are adopted for the non-linear model. It is known that the number of hidden layers is positively related to the overfitting of training, and it is recommended to use fewer hidden layers than the number of input nodes [25] in building the neural network model. Though there is no rule for the exact number of hidden layers, many previous studies used one hidden layer [17]. In our research, the neural network model consists of ten input nodes, five hidden nodes in one hidden layer, and one output node. The sigmoid function was used for the transfer function, and the delta rule was used for the learning algorithm. We repeatedly used this network model 32 times for each participant. The participant's prediction confidence level was used as the objective variable in the training samples, while actual bankruptcy was used in the testing samples. This makes it possible to divide training samples and testing samples and to use both hit ratio and MPS for the measurement of predictive validity of linear or non-linear models.

## 4. Analysis and results

## 4.1. Analysis of decision-making

The prediction accuracies of 32 participants were measured by hit ratio, MPS, and $R _ { \mathrm { a } }$ of the lens model.

Table 1  
Prediction accuracy analysis of participants

<table><tr><td>Participant</td><td> $R_a$ </td><td>Hit ratio (%)</td><td>MPS</td><td>C index</td><td>C index (t-statistics)</td></tr><tr><td>1</td><td>0.552</td><td>78</td><td>0.1767</td><td>0.245</td><td>**1.92451</td></tr><tr><td>2</td><td>0.630</td><td>80</td><td>0.1548</td><td>0.528</td><td>**4.73494</td></tr><tr><td>3</td><td>0.657</td><td>83</td><td>0.1430</td><td>0.534</td><td>**4.81005</td></tr><tr><td>4</td><td>0.573</td><td>77</td><td>0.1757</td><td>0.287</td><td>**2.28171</td></tr><tr><td>5</td><td>0.579</td><td>75</td><td>0.1708</td><td>0.236</td><td>**1.84956</td></tr><tr><td>6</td><td>0.511</td><td>73</td><td>0.2057</td><td>0.244</td><td>**1.91616</td></tr><tr><td>7</td><td>0.546</td><td>78</td><td>0.1758</td><td>0.186</td><td>*1.44169</td></tr><tr><td>8</td><td>0.447</td><td>73</td><td>0.2105</td><td>0.104</td><td>0.79635</td></tr><tr><td>9</td><td>0.584</td><td>80</td><td>0.1655</td><td>0.310</td><td>**2.48322</td></tr><tr><td>10</td><td>0.426</td><td>68</td><td>0.2180</td><td>0.026</td><td>0.19807</td></tr><tr><td>11</td><td>0.489</td><td>70</td><td>0.2115</td><td>0.289</td><td>**2.299061</td></tr><tr><td>12</td><td>0.517</td><td>75</td><td>0.1963</td><td>0.15</td><td>1.155439</td></tr><tr><td>13</td><td>0.609</td><td>77</td><td>0.1708</td><td>0.359</td><td>**2.929339</td></tr><tr><td>14</td><td>0.496</td><td>75</td><td>0.1962</td><td>0.203</td><td>*1.578876</td></tr><tr><td>15</td><td>0.399</td><td>70</td><td>0.232</td><td>-0.051</td><td>-0.38891</td></tr><tr><td>16</td><td>0.517</td><td>68</td><td>0.2048</td><td>0.281</td><td>**2.229879</td></tr><tr><td>17</td><td>0.558</td><td>72</td><td>0.1802</td><td>0.209</td><td>*1.627642</td></tr><tr><td>18</td><td>0.496</td><td>73</td><td>0.1933</td><td>0.048</td><td>0.365979</td></tr><tr><td>19</td><td>0.488</td><td>72</td><td>0.1932</td><td>0.157</td><td>1.210691</td></tr><tr><td>20</td><td>0.363</td><td>65</td><td>0.2648</td><td>0.154</td><td>1.186989</td></tr><tr><td>21</td><td>0.532</td><td>70</td><td>0.1948</td><td>0.259</td><td>**2.04217</td></tr><tr><td>22</td><td>0.569</td><td>73</td><td>0.1732</td><td>0.201</td><td>*1.562662</td></tr><tr><td>23</td><td>0.483</td><td>70</td><td>0.2083</td><td>0.253</td><td>**1.991584</td></tr><tr><td>24</td><td>0.394</td><td>70</td><td>0.2553</td><td>0.057</td><td>0.434806</td></tr><tr><td>25</td><td>0.307</td><td>63</td><td>0.261</td><td>0.004</td><td>0.030463</td></tr><tr><td>26</td><td>0.342</td><td>63</td><td>0.2277</td><td>-0.101</td><td>-0.77315</td></tr><tr><td>27</td><td>0.425</td><td>68</td><td>0.2473</td><td>0.051</td><td>0.388911</td></tr><tr><td>28</td><td>0.444</td><td>70</td><td>0.2072</td><td>-0.097</td><td>-0.74223</td></tr><tr><td>29</td><td>0.338</td><td>67</td><td>0.2643</td><td>0.202</td><td>*1.570767</td></tr><tr><td>30</td><td>0.363</td><td>68</td><td>0.2587</td><td>0.157</td><td>1.210691</td></tr><tr><td>31</td><td>0.249</td><td>62</td><td>0.2768</td><td>-0.111</td><td>-0.85061</td></tr><tr><td>32</td><td>0.348</td><td>72</td><td>0.2475</td><td>-0.001</td><td>-0.00762</td></tr></table>

<sup>⁎</sup> αb0.1, <sup>⁎⁎</sup> αb0.05.

The valid non-linearity of a participant's decisionmaking behavior was measured with C index of the lens model. Hit ratios for most of the participants are around 70%, and the highest is 83% (participant # 3). Most MPS measures are around 0.2. Values of $R _ { \mathrm { a } }$ are greater than the values of previous studies [17]. We assume the reason for this is because the predictive variable is not discretely measured, but rather quasi-continuously measured, with ten-level prediction confidence. C index shows the validity of the non-linearity of 12 participants' decisions, with a significant level of $\alpha = . 0 5$ , and of 5 participants' decisions, with a significant level of $\alpha { = } 0 . 1$ . The results of the prediction accuracy of 32 participants are summarized in Table 1.

Table 2 shows the correlation among $R _ { \mathrm { a } } ,$ hit ratio, MPS, and C index. The correlation coefficient between $R _ { \mathrm { a } }$ and hit ratio is relatively high at 0.8701. This means that $R _ { \mathrm { a } } ,$ which is used to measure predictive validity in the lens model, might be an appropriate measurement for prediction accuracy. Correlation coefficients between $R _ { \mathrm { a } }$ and MPS and between hit ratio and MPS both are −0.8598. This high correlation may come from the fact that MPS also measures prediction accuracy. MPS shows the negative relationships with other indexes because it uses the prediction error that caused the negative sign.

Table 2  
Correlation between C index and prediction accuracy

<table><tr><td></td><td>Hit ratio</td><td>MPS</td><td>C index (p-value)</td></tr><tr><td> $R_a$ </td><td>0.8701</td><td>-0.8598</td><td>0.8026 (p&lt;0.0001)</td></tr><tr><td>Hit ratio</td><td>-</td><td>-0.8598</td><td>0.7129 (p&lt;0.0001)</td></tr><tr><td>MPS</td><td>-</td><td>-</td><td>-0.6889 (p&lt;0.0001)</td></tr></table>

Correlation coefficients between C index (measuring valid non-linearity) and prediction accuracy measurements are high: the $R _ { \mathrm { a } }$ is 0.8026, the hit ratio is 0.7129, and the MPS $\mathrm { i s \textrm { -- } 0 . 6 8 8 9 }$ . They are also statistically significant at α = .01 level. Therefore, as expected, we can conclude that valid non-linearity is highly correlated with the validity of decision-making.

These results support the findings of previous studies [19]: Valid non-linearity is an important factor contributing to predictive validity. These results also mean that valid non-linearity can be used to measure predictive validity. To examine the value of C index as an evaluation index of prediction accuracy, we classified the samples as valid (with 0.2 or higher C index value) and invalid (less than 0.2) and compared the two groups prediction accuracy. The two groups have statistically different (p-value b 0.001) prediction accuracies in terms of $R _ { \mathrm { a } } .$ , hit ratio, and MPS; and this result shows that valid non-linearity-based classification is consistent with the classification based on predictive accuracy. Table 3 shows the results in detail.

## 4.2. Model construction and evaluation

The decision-making models applied to 32 participants were developed using a linear regression model, a tree structure model using C4.5, and a neural network model using back propagation. Hit ratio and MPS are used as evaluation criteria. In the linear regression and neural network models, we used the value 0.4 as a threshold to evaluate hit ratio because prediction values are continuous values in these two models. For consistency purposes, this threshold is also used for the tree structure model. It is reasonable that the value 0.4 is counted as a threshold because we classified the nonbankrupt company with a prediction confidence of greater than 0.6 and the bankrupt company with less than 0.4 in the training sample. 0–0.4 means bankruptcy and 0.6–1.0 means non-bankruptcy. In the previous researches, the tree structure model may have been evaluated more unfairly than the linear regression model or neural network model when measuring MPS because its objective variables is discrete, while the objective variable of the linear regression model and neural network model is continuous. However, in this study, we calculated MPS under the assumption that the objective variable of the tree structure model is continuous because the objective variable is measured by quasicontinuous scale values (0.0–1.0).

Table 3  
Prediction accuracy of participants (group average)

<table><tr><td>Group</td><td>C index</td><td> $R_a$ </td><td>Hit ratio</td><td>MPS</td></tr><tr><td>Valid group(n=16,C index&gt;0.2)</td><td>0.290</td><td>0.542</td><td>74.25%</td><td>0.187</td></tr><tr><td>Invalid group(n=16,C index&lt;0.2)</td><td>0.046</td><td>0.409</td><td>69.38%</td><td>0.229</td></tr><tr><td>t-statistics(p-value)</td><td>6.781(p&lt;0.001)</td><td>4.865(p&lt;0.001)</td><td>2.998(p&lt;0.001)</td><td>3.980(p&lt;0.001)</td></tr></table>

Table 4  
Group performance comparison among prediction models

<table><tr><td rowspan="2">Group</td><td colspan="2">Linear regression model</td><td colspan="2">Tree structure model</td><td colspan="2">Neural network model</td></tr><tr><td>Hit ratio</td><td>MPS</td><td>Hit ratio</td><td>MPS</td><td>Hit ratio</td><td>MPS</td></tr><tr><td>Valid group (n=16, C index&gt;0.2)</td><td>61.14%</td><td>0.195</td><td>71.46%</td><td>0.187</td><td>73.23%</td><td>0.187</td></tr><tr><td>Invalid group (n=16, C index&lt;0.2)</td><td>57.08%</td><td>0.201</td><td>67.10%</td><td>0.210</td><td>65.94%</td><td>0.228</td></tr><tr><td>t-value</td><td>2.206*</td><td>-0.88</td><td>1.697*</td><td>-2.34*</td><td>4.883*</td><td>-3.95*</td></tr></table>

<sup>⁎</sup>αb0.05.

In Table 4, we classified participants into groups of valid and invalid based on the C index and analyzed the two groups by linear regression, tree structure, and neural network. After that, we calculated the average prediction accuracy of the models for each group. Since the purpose of this study is not model comparison but the investigation of the effect of valid non-linearity in modeling, we skipped the model performance comparison. The difference between groups indicates that valid non-linearity of decision-making behavior is directly related to the predictive validity of the model. The results of the two groups, which are classified by C index, show significant differences in the hit ratio and MPS between the tree structure model and the neural network model. However, the hit ratio in the linear regression model also shows a significant difference between the two groups. Therefore, we cannot accept Hypothesis 1, which states that valid non-linearity of decision-making is positively related to the predictive accuracy of a non-linear model, but not positively related to the predictive accuracy of a linear model. We can only infer that the valid non-linearity has an effect on predictive validity based upon the results of nonlinear models. We may also assume that MPS is more suitable than the hit ratio because MPS is used for continuous value. If the above assumption is correct, and if we could give more weight to MPS than hit ratio, we might conjecture that no significant relationship exists between valid non-linearity and the predictive validity of the linear model.

Table 5  
Top ten ranking of prediction accuracy using hit ratio

<table><tr><td>Participant/Model</td><td>Hit ratio (%)</td><td>Rank</td></tr><tr><td>Tree structure model (Participant 3)</td><td>83.3</td><td>1</td></tr><tr><td>Participant 3 (C index: 0.534)</td><td>83.0</td><td>2</td></tr><tr><td>(1st ranked participant in prediction accuracy)</td><td></td><td></td></tr><tr><td>Neural network model (Participant 9)</td><td>80.0</td><td>3</td></tr><tr><td>Tree structure model (Participant 9)</td><td>80.0</td><td>3</td></tr><tr><td>Participant 9 (C index: 0.310)</td><td>80.0</td><td>3</td></tr><tr><td>(2nd ranked participant in prediction accuracy)</td><td></td><td></td></tr><tr><td>Participant 2 (C index: 0.528)</td><td>80.0</td><td>3</td></tr><tr><td>(3rd ranked participant in prediction accuracy)</td><td></td><td></td></tr><tr><td>Neural network model (Participant 1)</td><td>78.3</td><td>7</td></tr><tr><td>Neural network model (Participant 13)</td><td>78.3</td><td>7</td></tr><tr><td>Tree structure model (Participant 2)</td><td>78.3</td><td>7</td></tr><tr><td>Participant 1 (C index: 0.245)</td><td>78</td><td>10</td></tr><tr><td>(4th ranked participant in prediction accuracy)</td><td></td><td></td></tr></table>

## 4.3. Comprehensive comparison

Table 5 shows the top ten predictive models and human participants based on hit ratio. Four participants and six models — three tree structure models and three neural network models — are included, but none of the linear regression models is included. It can be interpreted that as an expert's predictive accuracy increases, the modeling effect of linear models decreases. The highest hit ratio (83.3%) is achieved by the tree structure model for participant #3, and this value is even higher than actual human judgment for this participant. The predominance of a model over human judgment is also found for participant 1, whose neural network model (7th) outperforms human prediction (10th). C indexes of participants (#1, #2, #3, #9, and #13), whose models are ranked in the top 10, are the highest values among the 32 participants.

Table 6 lists the top ten predictive models and human participants based on MPS. The result is similar to Table 5. Three human experts (participants #2, #3, and #9) and seven non-linear models (four tree structure models and three neural network models) are included. However, none of the linear models is included. The highest predictive accuracy was achieved by the tree structure model of participant #3, the same result is shown in Table 5. The predominance of models over human experts was found in the case of participant #3, where his/her model (1st) outperforms his/her judgment (2nd), and in the case of participant #9, whose neural network model (6th) outperforms his/her judgment (8th). The same participants (#1, 2, 3, and 9) whose models are ranked top ten in Table 5 are also listed in Table 6. The results of Tables 5 and 6 show that there is valid non-linearity contributing to predictive accuracy in decision-making behavior and that non-linear models reflect non-linearity of behavior better than the linear model.

To shed light on this analysis, we measured the correlation between the predictive accuracy of all the participants (n = 32) and that of each decision model of the participants by hit ratio and $R _ { \mathrm { a } } .$ We also measured the correlation between participants' predictive accuracy and the modeling effect of each decision model. Modeling effect is measured as the incremental difference between the model's predictive accuracy and the participant's predictive accuracy. Hence, it shows to what degree the accuracy of the model is greater than the accuracy of the human participant. Generally, it is believed that the higher the participant's predictive accuracy, the lower the modeling effect would be. Therefore, analyzing the correlation between a participant's predictive accuracy and modeling effect allows us to find out which modeling effect significantly decreases as the participant's predictive accuracy increases. In this analysis, MPS is not used because it has a negative relationship to other prediction measurements. In addition, MPS is very highly correlated (−0.8598 in Table 2) with the hit ratio and $R _ { \mathrm { a } } ,$ which we do use in our analysis.

Top ten ranking of prediction accuracy using MPS

<table><tr><td>Model/participant</td><td>MPS</td><td>Rank</td></tr><tr><td>Tree structure model (Participant 3)</td><td>0.1387</td><td>1</td></tr><tr><td>Participant 3 (C index: 0.534)</td><td>0.1430</td><td>2</td></tr><tr><td>(Top ranked participant in prediction accuracy)</td><td></td><td></td></tr><tr><td>Neural network model (Participant 3)</td><td>0.1434</td><td>3</td></tr><tr><td>Tree structure model (Participant 2)</td><td>0.1548</td><td>4</td></tr><tr><td>Participant 2 (C index: 0.528)</td><td>0.1548</td><td>4</td></tr><tr><td>(2nd ranked participant in prediction accuracy)</td><td></td><td></td></tr><tr><td>Tree structure model (Participant 9)</td><td>0.1583</td><td>6</td></tr><tr><td>Neural network model (Participant 2)</td><td>0.1608</td><td>7</td></tr><tr><td>Neural network model (Participant 9)</td><td>0.1647</td><td>8</td></tr><tr><td>Participant 9 (C index: 0.310)</td><td>0.1655</td><td>9</td></tr><tr><td>(3rd ranked participant in prediction accuracy)</td><td></td><td></td></tr><tr><td>Tree structure model (Participant 1)</td><td>0.1672</td><td>10</td></tr></table>

Correlation between participants' prediction accuracy and modeling effect

<table><tr><td rowspan="2" colspan="2">Model prediction accuracy and modeling effect</td><td colspan="2">Participants&#x27; prediction accuracy</td></tr><tr><td>Hit ratio</td><td> $R_a$ </td></tr><tr><td rowspan="3">Model prediction accuracy</td><td>Linear regression model</td><td>0.5866</td><td>0.5318</td></tr><tr><td>Tree structure model</td><td>0.6005</td><td>0.5521</td></tr><tr><td>Neural network model</td><td>0.8729</td><td>0.8006</td></tr><tr><td rowspan="3">Modeling effect</td><td>Linear regression model</td><td>-0.3925*</td><td>-0.3172*</td></tr><tr><td>Tree structure model</td><td>-0.1063</td><td>-0.0557</td></tr><tr><td>Neural network model</td><td>-0.1105</td><td>-0.0127</td></tr></table>

<sup>⁎</sup> b0.1.

Table 7 shows the results of the analysis. The neural network model is most affected by the participant's predictive accuracy (correlation coefficient of 0.8729 with hit ratio and 0.8006 with $R _ { \mathrm { a } } ) _ { \cdot }$ Generally, the modeling effect is negatively related to the participant's predictive accuracy. However, this negative correlation is found to be statistically significant only in the linear regression model (−0.3925 in hit ratio and −0.3172 in $R _ { \mathrm { a } } )$ . This is consistent with the results found in Table 5 and Table 6, implying that the modeling effect of a linear model significantly deteriorates when the predictive validity of human judgment is high. We could interpret that this happens because the linear model can not reflect valid non-linearity, which ensures the predictive validity of the human judgment (or experts). This leads us to accept our second hypothesis: As the validity of a subject's decision-making increases, the modeling effect of a linear model significantly decreases to a greater extent than the modeling effect of a non-linear model.

## 5. Conclusion

It is believed that human decision-making behavior is quite non-linear and that using a non-linear model would be more effective in decision-making [12,17,19,24]. In this study, to test this hypothesis, we developed an expert decision-making model that shows how human experts use linear and/or non-linear models; and we investigated the relationship between valid non-linearity and predictive accuracy. We discovered several interesting results. First, we found a significant relationship between valid non-linearity and predictive accuracy through the analysis of human decision-making behavior using hit ratio, MPS, and C index of the lens model analysis. Second, non-linear models showed a higher predictive accuracy than linear models when valid non-linearity was inherent in human decision-making behavior. Third, through analyzing the modeling effects, we found that there is a significant negative relationship between the valid nonlinearity of human decision-making behavior and the incremental predictive accuracy of linear models. We interpreted the negative correlation to mean that the more valid non-linearity there is in human judgment, the less effective the use of linear models would be. Hence, the negative correlation supports Libby's argument [20], that as expert validity increases, the advantage of using linear models decreases. The negative correlation could also present a possible explanation for the conflicting results concerning superiority of linear models in human judgment-modeling research. It seems that linear models outperformed non-expert judgment and non-linear models for non-experts for two reasons: There was significant noise in the input data and/or the human subjects used in the research were not domain experts. Consequently, it would be better to select the modeling algorithm based on the analysis of the characteristics of input data and/or the consideration of human expert decisionmaking behavior.

We believe the results of our research raises research issues in the field of expert systems and decision models. First, the lens model divides prediction accuracy into linear and non-linear components and provides different evaluation criteria. A lens model can answer the question of whether a non-linear model can show better predictive accuracy than a linear model or even human expert judgment.

The second issue involves knowledge management. Knowledge base is the core component of knowledgebased models. The fact that the predictive validity of experts, which provides a knowledge base, conveys a critical role in the predictive accuracy of the model has been proven by much research [19,21,37]. Using a lens model, we verified the predictive validity and valid nonlinearity of experts. Based on our results, we believe that training experts could improve their predictive validity, which would eventually improve the predictive accuracy of the decision-making model.

Decision-making research, combined with expert system research, can expand to a variety of applications such as finance, medical science, and credit rating. However, more advanced decision model development requires systematic and synthesized study, which includes empirical studies of various areas and circumstantial factors affecting a system's predictive accuracy.

We hope that this research will be helpful to future research in considering additional circumstantial factors.

However, two limitations of this research should be noted. First, this research simplified the task of bankruptcy prediction by using only ten financial ratios. Such qualitative factors as management reputation and economic situation could not be included in this research design. In reality, such factors may play a critical role in predicting bankruptcy of a firm. Second, the evaluation of the case examples by the participants from the field (16 CPAs) was executed independently without our control. Since the task (the evaluation of 70 cases) was extremely time-consuming, it is possible that consistency during the whole evaluation process was not to be maintained. This limitation constrains the generalizability of the results.

## Acknowledgements

The authors thank Professor Andrew B. Whinston, Professor Jae Kyu Lee, Professor Ho Gun Lee and anonymous referees for their helpful comments on earlier drafts of the paper. All errors are those of the authors. This paper is supported by the Research Fund of the University of Seoul in 2006.

## References

[1] E. Altman, Financial ratios, discriminant analysis and the prediction of corporate bankruptcy, Journal of Finance 23 (4) (1968).

[2] L. Beach, T. Mitchell, A contingency model for the selection of decision strategies, Academy of Management Review 3 (3) (1978).

[3] A. Belkaoui, Lens studies in accounting, in: A. Belkaoui (Ed.), Human Information Processing in Accounting, Quorum Books, 1989.

[4] R. Billings, S. Marcus, Measures of compensatory and noncompensatory models of decision behavior, Organizational Behavior Human Performance 31 (3) (1983).

[5] H. Braun, J. Chandler, Predicting stock market behavior through rule induction, Decision Sciences 18 (3) (1987).

[6] E. Brunswick, The Conceptual Framework of Psychology, University of Chicago Press, 1952.

[7] C.J. Casey, Prior probability disclosure and loan officers' judgment: some evidence of the impact, Journal of Accounting Research 21 (1) (1983).

[8] H.M. Chung, M.S. Silver, Rule-based expert systems and linear models: an empirical comparison of learning-by-examples methods, Decision Sciences 23 (3) (1992).

[9] R. Cooksey, Judgment Analysis: Theory, Methods, and Applications, 1996 California, San Diego.

[10] R. Dawes, B. Corrigan, Linear models in decision-making, Psychological Bulletin 81 (2) (1974).

[11] H. Einhorn, The use of nonlinear, noncompensatory models in decision-making, Psychological Bulletin 77 (3) (1970).

[12] H. Einhorn, Expert measurement and mechanical combination, Organizational Behavior Human Performance 20 (2) (1972).

[13] H. Einhorn, D. Kleimuntz, B. Kleimuntz, Linear regression and process — tracing models of judgment, Psychological Review 86 (6) (1979).

[14] D.H. Fisher, K.B. McKusick, An empirical comparison of ID3 and back-propagation, Technical Report CS-88-14, Dept. of Computer Science, Vanderbilt University, 1989.

[15] K. Harmond, C. Hursch, F. Todd, Analyzing the components of clinical inference, Psychological Review 71 (6) (1964).

[16] C. Harris, An Expert Decision Support Systems for Auditor Going Concern Evaluation, PhD Dissertation, University of Texas at Arlington (1989).

[17] C.N. Kim, R. McLeod Jr., Expert, linear models, and nonlinear models of expert decision-making in bankruptcy prediction, Journal of Management Information Systems 16 (1) (1999).

[18] C.N. Kim, M. Chung, D. Paradice, Inductive learning of expert decision-making: a decision strategy perspective, Decision Support Systems 21 (2) (1997).

[19] K. Levi, Expert systems should be more accurate than human experts, IEEE Transactions on Systems, Man, and Cybernetics 19 (3) (1989).

[20] R. Libby, Man versus model of man: some conflicting evidence, Organizational Behavior Human Performance 16 (1) (1976).

[21] R. Libby, Accounting and Human Information Processing: Theory and Applications, 1981 New Jersey, Englewood.

[22] W. Messier, J. Hansen, Inducing rules for expert system development: an example using default and bankruptcy data, Management Science 34 (12) (1988).

[23] M. O'Connor, W. Remus, K. Lim, Improving judgmental forecasts with judgmental bootstrapping and task feedback support, Journal of Behavioral Decision Making 18 (2005).

[24] R.W. Olshavsky, Task complexity and contingent processing in decision-making: a replication and extension, Organizational Behavior Human Performance 24 (3) (1979).

[25] E. Patuwo, M. Hu, M. Hung, Two-group classification using neural networks, Decision Sciences 24 (4) (1993).

[26] J. Quinlan, Discovering rules by induction from large collection of examples, in: D. Michie (Ed.), Expert Systems in Microelectronic Age, 1979, England, Edinburgh.

[27] A. Schepanski, Tests of theories of information processing behavior in credit judgment, Accounting Review 58 (3) (1983).

[28] T. Stewart, Judgmental analysis: procedures, in: B. Brehmer, R.B. Joyce (Eds.), Human Judgment: The SJT View, North-Holland, Amsterdam, 1988.

[29] T. Stewart, Improving reliability of judgmental forecasts, in: J.S. Armstrong (Ed.), Principles of Forecasting: A Handbook for Researchers and Practitioners, 2001, Massachusetts, Boston.

[30] O. Svenson, Process descriptions of decision-making, Organizational Behavior Human Performance 23 (1) (1979).

[31] K. Tam, M. Kiang, Managerial applications of neural networks: the case of bank failure predictions, Management Science 38 (7) (1992).

[32] L.R. Tucker, A suggested alternative formulation in the development of Hursch, Hammond, and Hursch, and by Hammond, Hursch, and Todd, Psychological Review 71 (6) (1964).

[33] A. Velido, P. Lisboa, J. Vaughan, Neural networks in business: a survey of applications (1992–1998), Expert Systems with Applications 17 (1999).

[34] B. Wong, V. Lai, J. Sam, A bibliography of neural network business applications research: 1994–1998, Computers & Operations Research 27 (2000).

[35] J.F. Yates, External correspondence: decompositions of the mean probability score, Organizational Behavior Human Performance 30 (1982).

[36] A. Zacharakis, G. Meyer, A lack of insight: do venture capitalists really understand their own decision process, Journal of Business Venturing 13 (1998).

[37] I. Zimmer, A lens study of the prediction of corporate failure by bank loan officers, Journal of Accounting Research 18 (2) (1980).

Choong Nyoung Kim (cnkim27@uos.ac.kr) is a professor in the Management Department at the University of Seoul. He received his M.B.A. from the University of Missouri at Columbia and his PhD from Texas A&M University. His research interests include decision support systems and expert systems, human information processing, and machine learning. His research findings have been published in Decision Support Systems, the Journal of Global Information Management, and the Journal of Management Information Systems.

Kyung Hoon Yang (yang.kyun@uwlax.edu) is currently an assistant professor in the Department of Information Systems at the University of Wisconsin–La Crosse. He received his PhD in management information systems from Purdue University and was a professor at Chungang University in Korea. His major research interests include knowledge transfer and knowledge-based organization. He has published more than 15 articles in journals, which include Expert Systems with Applications and Omega.

Jaekyung Kim (jkim6@unl.edu) is a PhD candidate in Information Systems at the University of Nebraska–Lincoln. He received his M.B.A. from Miami University of Ohio. His research focuses on decision support systems, electronic commerce, and knowledge management. His work has been published in journals such as Omega, Expert Systems with Applications and the International Journal of Knowledge Management.
