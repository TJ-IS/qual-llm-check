---
otero_id: 18980
otero_key: "WUX4UB82"
title: "Forecasting with neural networks"
authors: "Desmond Fletcher; Ernie Goss"
year: "1993"
journal: "Information & Management"
doi: "10.1016/0378-7206(93)90064-z"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Applications

# Forecasting with neural networks An application using bankruptcy data

Desmond Fletcher

The University of Southern Mississippi, Hattiesburg, MS, USA

Ernie Goss

Creighton University, Omaha, NE, USA

In the business environment, Least-Squares estimation has long been the principle statistical method for forecasting a variable from available data with the logit regression model emerging as the principle methodology where the dependent variable is binary. Due to rapid hardware and software innovations, neural networks can now improve over the usual logit prediction model and provide a robust and less computationally demanding alternative to nonlinear regression methods. In this research, a back-propagation neural network methodology has been applied to a sample of bankrupt and non-bankrupt firms. Results indicate that this technique more accurately predicts bankruptcy than the logit model. The methodology represents a new paradigm in the investigation of causal relationships in data and offers promising results.

Keywords: Neural networks; Logistic regression; Forecasting models; Bankruptcy prediction; Neural network forecasting; Back-propagation; Cross-validation.

![](/api/attachments/WUX4UB82/fulltext/images/0c11f9a6e74e5b1df5032378607a9bc98ce97c910ecb685a1b11fbd15b5c9464.jpg)

Desmond Fletcher is an Assistant Professor of Engineering Technology at The University of Southern Mississippi. He received his Master of Architecture degree from The University of Texas at Austin in 1978. Prior to his academic appointment, Mr. Fletcher was president of Earthforms Construction Co., Inc., in central Texas. Current research involves computer augmented analysis and design related to construction and architecture. Mr. Fletcher is Project Direc tor for the Mississippi Residential Radon Survey.

## Introduction

Forecasting bankruptcy from financial ratios is one of the more common probability models encountered and represents one of the earliest attempts to use logit regression to estimate probability models in the business world [1]. Recent empirical research has shown the logit model to be viable for predicting business failure or bankruptcy [3]. Despite the popularity of the logit model, it is our hypothesis that artificial neural networks (ANNs), due to their generalization and abstract mapping capacity, offer forecasting capabilities superior to the logit model.

As an outgrowth of stochastic approximation methodologies, ANNs have been in the development stage for several decades and have been successfully applied to problems ranging from pattern recognition, process control, and image enhancement to data classification and forecasting. These successes in a broad range of fields can be attributed to the development of new ANN mechanisms during the “second wave of artificial intelligence” [13]. Having been previously limited to linearly separable data during the ‘perceptron’ phase, the advent within the last decade of network mechanisms such as backpropagation of error has brought a tremendous

![](/api/attachments/WUX4UB82/fulltext/images/22eb018bb966462227987bff8ff812ea0f34f8355a7e846e1897a9a7b06e9bdd.jpg)  
He is a member of the Editorial Board of The Review of Regional Studies.

Correspondence to: Desmond Fletcher, M. Arch., Assistant Professor, School of Engineering Technology, The University of Southern Mississippi, SS Box 5137, Hattiesburg, Mississippi 39406, USA. Tel. 601-266-5185, Fax 601-266-5829.

resurgence of interest in neural networks as a viable alternative to usual linear regression methods and the more computationally demanding nonlinear regression methods [19].

In the business environment, ANNs have been developed for a variety of applications such as proprietary stock market forecasting, corporate bond rating prediction $[6]$ $[17]$ , emulation of mortgage underwriting judgements $[5]$ , and systems development projects $[11]$ . For example, CREDITVIEW, a hybrid neural network, is used to reduce losses on loans made to public and private corporations. Developed by Chase Manhattan Bank, this model performs three year forecasts that indicate the likelihood of a company being given a risk assignment of good, problematic or charged-off. CREDITVIEW uses historical financial data on good and bad obligators, along with industry norms from COMPUSTAT, to formulate forecasts $[14]$ .

The objective of this study is to illustrate the development of a forecasting model using a particular class of ANNs (Back-Propagation Neural Networks, or BPNNs) in a standard business application. First, the optimal generalizing BPNN model (indexed by $\lambda$ ) is determined from available historical financial data using a v-fold cross-validation technique to estimate prediction risk. Prediction risk is used here as a measure of the expected performance of an estimator on previously unseen data. Second, the results of the BPNN( $\lambda$ ) are compared to the standard logit regression (LR), a widely used prediction and classification methodology. This comparison is made in terms of (1) minimization of prediction risk, (2) efficiency of the estimator, and (3) maximization of the correctness ratios for unseen test data. And finally, a family of mean risk curves are generated from the optimal BPNN( $\lambda$ ) to illustrate forecasting empirical probabilities of bankruptcy.

## Description of application

A typical business forecasting application involves the binary “go, no-go” decision. An example might include the make or buy decision with the dependent variable Y represented as 0 or 1. The dependent variable, whether to make (0) or buy (1), is a function of independent variables such as the cost of capital and other specific opportunity costs. The accuracy of the estimated dependent variable $\hat{Y}$ , and therefore the risk of making a decision, is a function of the amount of information contained within the independent variables and the degree to which the estimator can generalize across the domain of the problem for new data. Typically, a risk cutoff value is selected by the analyst and for categorization purposes is normally between 0.5 and 1. All observations with predicted risks equal to or above this value are categorized as 1 (failed) and 0 (non-failed) when less than this value. The choice of the cutoff value depends on the relative cost of incorrectly categorizing an observation as a 0 when it is not, versus the converse.

Table 1  
Sample of failed and non-failed firms.

<table><tr><td>ID</td><td>Failed (1)</td><td>CR</td><td>QR</td><td>IR</td><td>ID</td><td>Non-failed</td><td>CR</td><td>QR</td><td>IR</td></tr><tr><td>1-1</td><td>Westates Petroleum</td><td>1.39</td><td>0.67</td><td>0.34</td><td>0-1</td><td>Universal</td><td>6.43</td><td>4.49</td><td>0.19</td></tr><tr><td>1-2</td><td>Cott Corp.</td><td>2.00</td><td>0.27</td><td>0.02</td><td>0-2</td><td>MEI corp.</td><td>1.29</td><td>0.33</td><td>0.98</td></tr><tr><td>1-3</td><td>American Mfg. Co.</td><td>3.20</td><td>0.73</td><td>0.93</td><td>0-3</td><td>Gaynor-Stafford</td><td>5.20</td><td>0.78</td><td>-0.20</td></tr><tr><td>1-4</td><td>Scottex Corp.</td><td>1.59</td><td>0.09</td><td>-0.33</td><td>0-4</td><td>Compo Ind.</td><td>3.77</td><td>0.32</td><td>-0.09</td></tr><tr><td>1-5</td><td>Lynnwear</td><td>1.70</td><td>0.24</td><td>0.09</td><td>0-5</td><td>Movie Star Inc.</td><td>2.80</td><td>0.23</td><td>0.13</td></tr><tr><td>1-6</td><td>Nelly Don, Inc.</td><td>1.70</td><td>0.15</td><td>0.13</td><td>0-6</td><td>Decorator Ind.</td><td>3.18</td><td>0.57</td><td>0.02</td></tr><tr><td>1-7</td><td>Mansfield Tire &amp; Rubber</td><td>2.50</td><td>0.09</td><td>0.06</td><td>0-7</td><td>Pope &amp; Talbot</td><td>1.90</td><td>0.15</td><td>0.09</td></tr><tr><td>1-8</td><td>Brody Seating Co.</td><td>2.70</td><td>0.14</td><td>0.01</td><td>0-8</td><td>Ohio-Sealy</td><td>2.60</td><td>0.97</td><td>0.35</td></tr><tr><td>1-9</td><td>Paterson Parchment Paper</td><td>2.41</td><td>0.09</td><td>-0.04</td><td>0-9</td><td>Clevepak Corp.</td><td>3.28</td><td>0.30</td><td>0.42</td></tr><tr><td>1-10</td><td>Rowland Inc.</td><td>1.73</td><td>0.08</td><td>0.02</td><td>0-10</td><td>Park Chemical</td><td>4.97</td><td>1.15</td><td>0.15</td></tr><tr><td>1-11</td><td>Pasco Inc.</td><td>1.51</td><td>0.12</td><td>0.16</td><td>0-11</td><td>Holly Corp.</td><td>1.55</td><td>0.11</td><td>0.37</td></tr><tr><td>1-12</td><td>RAI Inc.</td><td>1.16</td><td>0.01</td><td>0.09</td><td>0-12</td><td>Barry (R.G.)</td><td>3.00</td><td>0.38</td><td>0.15</td></tr><tr><td>1-13</td><td>Gray Mfg. Co.</td><td>3.31</td><td>0.49</td><td>0.11</td><td>0-13</td><td>Struthers Wells</td><td>1.61</td><td>0.21</td><td>0.39</td></tr><tr><td>1-14</td><td>Gladding Corp.</td><td>2.08</td><td>0.04</td><td>0.07</td><td>0-14</td><td>Watkins-Johnson</td><td>4.01</td><td>0.09</td><td>0.19</td></tr><tr><td>1-15</td><td>Merchants, Inc.</td><td>2.73</td><td>0.35</td><td>0.23</td><td>0-15</td><td>Banner Ind.</td><td>2.30</td><td>0.32</td><td>0.19</td></tr><tr><td>1-16</td><td>Shulman Transport</td><td>1.13</td><td>0.13</td><td>0.22</td><td>0-16</td><td>WTC Inc.</td><td>1.17</td><td>0.33</td><td>0.85</td></tr><tr><td>1-17</td><td>Reeves Telecom Corp.</td><td>3.20</td><td>0.63</td><td>0.20</td><td>0-17</td><td>Gross Telecasting</td><td>8.80</td><td>6.91</td><td>0.25</td></tr><tr><td>1-18</td><td>Plaza Group Inc.</td><td>0.91</td><td>0.03</td><td>-1.09</td><td>0-18</td><td>Total Petroleum</td><td>2.15</td><td>0.25</td><td>0.33</td></tr></table>

This binary decision approach is also used to develop an estimator to forecast bankruptcy. In this application, the independent variables are financial ratios as described below. The dependent variable is determined to be 0 for a non-failed firm and 1 for a failed firm. If the information contained within the independent variables is sufficient, the estimated dependent variable $\hat{Y}$ then represents an empirical probability in the range of 0 to 1 of the event occurring. Furthermore, since determining, a firm's trend to bankruptcy is of more interest than categorizing bankruptcy ex post, we are concerned with the accuracy of the model in risk categories less than 0.5.

Data for the empirical tests were drawn from an earlier study by Gentry et al. [8]. In their sample selection, failed companies were matched with a sample of non-failed companies that were in the same industries and approximately the same size in terms of total assets. Additionally, in order to control for general economic conditions, the time frames for the failed and non-failed firms were matched [12]. After the deletion of firms with incomplete data, there were 18 bankrupt firms. Each of the 18 failed companies was then matched with a non-failed firm based on asset size and sales for the fiscal year previous to their bankruptcy.

A listing of the 36 companies used for the empirical analysis is presented in Table 1. The current ratio (CR), quick ratio (QR) and income ratio (IR) of each firm are also presented in the table and defined as follows:

## Dependent Variable (Y):

1 for those companies that failed and 0 for those that did not.

## Independent (Explanatory) Variables:

(1) CR: current ratio [(current assets/current liabilities)].

(2) QR: quick ratio [(cash + other near cash assets)/(current liabilities)].

(3) IR: income ratio [(net income/working capital].

## Model training and selection methodology

Due to the small sample size after matching, direct training-to-test set validation is not advisable. A variation of the cross-validation method known as v-fold cross-validation $(CV_{P})$ was selected to conduct analyses of the models. This method was introduced by Geisser [7] and Wahba et al. [18] and is illustrated in a case study of corporate bond rating predictions by Utans and Moody [17]. The selection of the optimal model( $\lambda$ ) architecture is based on an estimator $CV_{P}$ of the prediction risk $P_{\lambda}$ , which is a measure of generalization ability of model( $\lambda$ ). Using this approach, the data is divided into v=18 subsets of six observations for each test set with three rotationally selected from the failed group and three from the non-failed group for a total of 108 observations in the test sets. This also provides 18 training sets of 30 observations. Each observation is represented three times in the test sets. The cross-validation mean square error of each subset j as defined by

$$
C V _ {P _ {j}} (\lambda) = \frac {1}{N _ {j}} \sum \left(t _ {k} - \hat {\mu} _ {\lambda} (P _ {j}) (x _ {k})\right) ^ {2},\tag{1}
$$

where $t_{k}$ is the actual targeted dependent variable for a given observation in the subset and $\hat{\mu}(P_{j})(x_{k})$ is the expected value generated by an approximation function. The prediction risk is then defined for each model( $\lambda$ ) by

$$
C V _ {P} (\lambda) = \frac {1}{v} \sum_ {j} C V _ {P _ {j}} (\lambda).\tag{2}
$$

As with the LR model, the output (or predicted dependent variable $\hat{Y}$ ) of the BPNN can be constrained to values from 0 to 1. The network is composed of an input layer, a hidden layer and an output layer of nodes (also known as neurons due to biological similarities). Information processing is performed through modification of connection weights ( $W_{\lambda}$ ) as normalized observation patterns are passed along connections from the input through the hidden to the output layer.

![](/api/attachments/WUX4UB82/fulltext/images/70fa4f79189c5a110ce6e34ece74d79b97859fad15cbc27cc86feb2e6ffc8d9b.jpg)  
Fig. 1. Diagram of empirical neural network model.

This distinction between layers can be traced to Rosenblatt's [15] early work, which divided networks into sensory, associative and response units.

In the BPNNs, the input nodes process the independent variables while the output node processes the dependent variable. The input layer distributes the patterns throughout the network and the output layer generates an appropriate response. The middle layer of nodes acts as a collection of associative feature detectors and is termed ‘hidden’ because it does directly process information to or from the user. The state of each node is determined by signals sent to it from all connected nodes. These signals are biased by the value of the connection weights $W_{\lambda}$ between nodes. Appendix 1 contains a summary of the mathematical derivation of the BPNN signals between layers as developed in 1986 by Rumelhart et al. [16].

![](/api/attachments/WUX4UB82/fulltext/images/ef5db78eda557063e4320a004afa5cedf5c4fcca268d5c867edb57837acd6390.jpg)  
Fig. 2. Minimum error in test set vs. learning events.

Figure 1 displays the configuration of the optimal BPNN( $\lambda$ ) developed using the commercial package NeuroShell 4.1. The BPNN model is a single hidden layer feed-forward network which implements an error back-propagation methodology. Back-propagation permits connection weights $W_{\lambda}$ between nodes to be modified in a supervised fashion using gradient descent to minimize the error function. In supervised learning models, known pattern pairs of target outputs and neural network outputs are repeatedly presented to the network to adjust the network $W_{\lambda}$ .

Kolmogorov's Mapping Neural Network Existence Theorem [9] states that any continuous function can be implemented with the network structure described above using $2n + 1$ hidden nodes, where n represents the number of input nodes. This is also the recommendation of Caudill [4]. However, in some cases this may lead to fitting (or memorizing) the training set too well resulting in poor generalization capabilities. In practice, the number of hidden nodes for optimal generalization should be tested in a range from approximately $2\sqrt{n} + m$ to the value $2n + 1$ , where m represents the number of output nodes. Therefore, for the empirical estimations, five BPNN models were developed using three input nodes, each corresponding to an independent variable, one output node, representing the bankruptcy risk index, and hidden nodes ranging from three to seven, respectively. Although neural network research is still in its infancy, this approach appears to provide a principled mechanism for determining the optimal network architecture as the following results will verify.

Each of the BPNN( $\lambda$ ) and LR( $\lambda$ ) were then trained with $\alpha = 0$ and $\eta = 0.01$ . In NeuroShell, a real-time comparison is maintained between the minimum errors of the training sets and hold-out test sets. Figure 2 illustrates a segment of the BPNN learning process at the test set classification error decreases to a minimum error value for one of the test sets at approximately 737,000 learning events. After this optimal point, the classification errors of the test set increase as memorization of the training set begins, generalizing capability declines, and the BPNN is less able to estimate the dependent variable from previously “unseen” data. NeuroShell automatically retains the optimal network $W_{\lambda}$ when the minimum mean square error in the test set has been reached.

## Empirical results

The five BPNN( $\lambda$ ) were then compared to the output of the LR( $\lambda$ ) for each of the 108 test set observations for training efficiency, percent correct per risk category, and model efficiency as determined by estimated prediction risk ( $CV_{P}$ ) and variance of the errors. These results are presented in Table 2. Results for all of the test sets were obtained using an 80486I microprocessor running at approximately 25 megaHertz.

Mean training times and number of learning events completed for the BPNN( $\lambda$ ) above $4_{HN}$ generally increased with model complexity $W_{\lambda}$ and training efficiency decreased. In all cases, training the BPNN( $\lambda$ ) represents a larger development cost than with the logit model. However, as indicated by the neural network training efficiencies, (which are ratios of mean training time to the average number of learning events per minute), the $3_{HN}$ and $4_{HN}$ models are the most efficient at approximately 3.70. In terms of neural network development cost, the BPNN( $4_{HN}$ ) is the most desirable with the least training time.

Table 2  
Model performances.

<table><tr><td>Category</td><td>LR</td><td> $3_{HN}$ </td><td> $4_{HN}$ </td><td> $5_{HN}$ </td><td> $6_{HN}$ </td><td> $7_{HN}$ </td></tr><tr><td>Percent Correctly Predicted</td><td>71.3</td><td>80.5</td><td>82.4</td><td>75.0</td><td>74.1</td><td>75.0</td></tr><tr><td>No. of coefficients ( $W_{\lambda}$ )</td><td>4</td><td>11</td><td>16</td><td>21</td><td>26</td><td>31</td></tr><tr><td>Mean Training Time (minutes)</td><td>0.3</td><td>12.6</td><td>9.8</td><td>14.8</td><td>13.8</td><td>18.8</td></tr><tr><td>Mean Learning Events (thousands)</td><td>NA</td><td>626</td><td>354</td><td>467</td><td>483</td><td>597</td></tr><tr><td>Mean Learning Events per Minute</td><td>NA</td><td>46.9</td><td>35.9</td><td>31.6</td><td>34.8</td><td>31.4</td></tr><tr><td>Training Efficiency Indicator</td><td>NA</td><td>3.70</td><td>3.66</td><td>2.13</td><td>2.52</td><td>1.67</td></tr><tr><td>Variance of error</td><td>0.04</td><td>0.02</td><td>0.02</td><td>0.02</td><td>0.019</td><td>0.02</td></tr><tr><td>Cross-Validation Prediction Risk  $CV_P$ </td><td>0.189</td><td>0.146</td><td>0.143</td><td>0.164</td><td>0.165</td><td>0.165</td></tr></table>

The BPNN( $4_{HN}$ ) model also most accurately predicted previously unseen observations from the test sets. The total is 82.4 percent at a risk cutoff value of 0.5. All of the models, including the LR( $\lambda$ ), predicted approximately 77 percent of the 54 unseen test set observations targeted as 1. However, of the 54 unseen test set observations targeted as 0, the BPNN( $4_{HN}$ ) surpasses all other models with 89 percent accurately predicted. The bar chart in Figure 3 illustrates the comparison of the percentages accurately predicted by BPNN( $4_{HN}$ ) versus the LR( $\lambda$ ) in a range of risk categories with cutoff values from 0.25 to 0.75. The BPNN( $4_{HN}$ ) also predicts a higher percentage of non-failed firms at risk virtually independent of risk category.

The most statistically efficient model is determined from the variance of errors and the prediction risk $CV_{p}$ . As can be seen from Table 2, the variance of the errors for all of the BPNN( $\lambda$ ) is less than for the LR( $\lambda$ ). This indicates that the logit model is a less efficient estimator. Furthermore, of the BPNN( $\lambda$ ), the model with $4_{HN}$ has the least value for $CV_{p}$ . As the number of hidden nodes increases above 4, abstract mapping capabilities appear to decrease and the $CV_{p}$ for the BPNN( $\lambda$ ) approaches that of the LR( $\lambda$ ). The neural network model with $3_{HN}$ does not appear to be able to extract as much information from the independent variables. In terms of prediction risk, model efficiency, and total percent correct, the BPNN( $4_{HN}$ ) performed better than all other models and is selected as the optimal BPNN. Also, with respect to development cost, slow learning rates are critical to minimize the variance of the errors and therefore increase the model efficiency.

A family of risk curves (at the 0.5 cutoff value) was then generated from the optimal BPNN( $4_{HN}$ ) to illustrate the potential use of neural networks in forecasting bankruptcy and graphically assess the impact of each independent variable on $\hat{Y}$ .

![](/api/attachments/WUX4UB82/fulltext/images/07f617efff02385c2682a5f6da07e1a988be546c263b3864bb47809f9d1a3e66.jpg)  
Fig. 3. Comparison of percent correct per risk category.

![](/api/attachments/WUX4UB82/fulltext/images/3a51f33d08b1e919ddc1ee119bcd2f95960f303a1ed1b629408d5a7bfcb45814.jpg)  
Fig. 4. Critical curves for range of current ratio at 0.5 cutoff.

NeuroShell provides a function which calculates the contributions each of the independent variables makes to the modification of $W_{\lambda}$ . The CR, IR, and QR contributed 43.3, 45.4, and 12.3 percent, respectively. This relationship can be readily seen in Figure 4. For a range of CR (1.61 to 3.2), the curves represent the estimated 0.5 cutoff value with respect to the IR and QR. Firms with low current ratios are less tolerant to changes in QR and there is a significant change in the y-intercept as IR increases.

## Summary

These results correspond closely to other studies which have likewise found neural networks better at extracting information from attributes for forecasting purposes. In a neural network application examining bond rating, Dutta and Shekhar [6] show how a neural network is able to forecast more accurately than standard regression. However, their approach did not use a comparison with logit regression as in this research.

As presented in Figure 3 and Table 2, the neural network outperforms the logit function with the BPNN( $4_{HN}$ ) selected as the most efficient predictor. In terms of forecasting capability, not only does this model more accurately predict a higher percentage of firms in the test sets, BPNN( $4_{HN}$ ) has less variance in the errors and lower prediction risk as determined by $CV_{P}$ . This means that BPNN( $4_{HN}$ ) is more statistically efficient and will provide more accurate forecasts in the population. Also, the results indicate that $2\sqrt{n} + m$ hidden nodes is the most appropriate for this application.

Out of the thirty-six firms tested, four were not correctly predicted by any model. This suggests missing explanatory variables for the models( $\lambda$ ). For this reason the BPNN( $4_{HN}$ ) is not regarded as a completed production model. Yet, this research begins to bridge the gap between pure statistical methods and neural networking. It shows neural networks to be a viable alternative to more traditional methods of estimating causal relationships in data and offers a new paradigm of computational capabilities to the business practitioner. The pattern recognition and generalization capabilities of neural networks can enhance decision making in cases where the dependent variable is binary and available data is limited. With over 16,000 neural network systems purchased to date and growth expected to exceed 20% per year [2], business practitioners can expect to see intensified research efforts and benefit from the implementation of such applications as are presented in this paper.

## References

[1] E. Altman, “Financial Ratios, Discriminant Analysis, and the Prediction of Corporate Bankruptcy.” Journal of Finance, September (1968), pp. 589–609.

[2] D. Bailey and D. Thompson, "How to Develop Neural Network Application," AI Expert, June (1990), pp. 38-47.

[3] R. BarNiv and R. Hershbarger, “Classifying Financial Distress in the Life Insurance Industry,” The Journal of Risk and Insurance, Spring (1990), pp. 110–135.

[4] M. Caudill, “Neural Network Training Tips and Techniques,” AI Expert, January (1991).

[5] E. Collins, S. Ghosh and C. Scofield, "An Application of Multiple Neural Network Learning System to Emulation of Mortgage Underwriting Judgements, Working Paper (Nestor, Inc., 1 Richmond Square, Providence, RI, 1989.

[6] S. Dutta, and S. Hekhar. "Bond-Rating: A Non-Conservative Application of Neural Networks," Proceedings of the IEEE International Conference on Neural Networks, Vol. II (1988), San Diego, CA, pp. 443–450.

[7] S. Geisser, “The Predictive Reuse Method with Applications,” Journal of The American Statistical Association, 70(350), June 1975.

[8] J. Gentry, A. Newbold and D. Whitford. "Classifying Bankrupt Firms with Funds Flow Components." Journal of Accounting Research, Vol. 23 (1), Spring (1985), pp. 146–160.

[9] R. Hecht-Nielsen, Neurocomputing, Addison-Wesley Co., New York, 1989.

[10] D. Hillman, “Integrating Neural Nets and Expert Systems,” AI Expert, June (1990), pp. 54–59.

[11] D. Hillman, "AUBREY: A Custom Expert System Environment in LISP." AI Expert, January (1990), pp. 34–39.

[12] H.G. Hunt and J.K. Ord. “Matched Pair Discrimination: Methodology and an Investigation of Corporate Accounting Policies,” Decision Sciences, Vol. 19(2), Spring (1988), pp. 373–382.

[13] D. Levine, “The Third Wave in Neural Networks,” AI Expert, December (1990), pp. 27–31.

[14] R. Marose, “A Financial Neural-Network Application,” AI Expert, May (1990), pp. 50–53.

[15] F. Rosenblatt, Principles of Neurodynamics, D.D. Spartan Books, Washington, 1962.

[16] D.E. Rumclhart, G.E. Hinton and R.J. Williams. "Learning Internal Representations by Error Propagation," in Parallel Distributed Processing Exploration in the Mi-

crostructure of Cognition, Vol. 1, (ed.), D.E. Rumelhart and J.L. McClelland, MIT Press Cambridge, MA, 1986, pp. 318–362.

[17] J. Utans and J. Moody, “Selecting Neural Network Architectures via the Prediction Risk: Application to Corporate Bond Rating Prediction,” Proceedings: First International Conference on Artificial Intelligence Applications on Wall Street, IEEE Computer Society Press, Los Alamitos, CA, 1991.

[18] G. Wahba and S. Wold, "A Completely Automatic French Curve: Fitting Spline Functions by Cross-Validation," Communications in Statistics," 4(1): 1-17, 1975.

[19] H. White, “Neural Network Learning and Statistics,” AI Expert, December (1989), pp. 48–52.

[20] B. Widrow and M.E. Hoff, 1960. “Adaptive Switching Circuits,” IRE, WESCON Convention Record, New York, pp. 96–104.

## Appendix 1

## The feed-forward process

In a back-propagation neural network, as developed by Rumelhart et al. [16], independent variable patterns, or values, are normalized between zero and one at the input layer to produce the signal $O_{i}$ prior to presentation to the hidden node layer. Each connection between the input layer and a hidden node has an associated weight $W_{ij}$ . The net signal $I_{j}$ to an individual hidden node is expressed as the sum of all connections between the input layer nodes and that particular hidden node plus the connection value $W_{gj}$ from a bias node. This relationship may be expressed as:

$$
I _ {j} = \sum W _ {i j} O _ {i} + W _ {g j}.\tag{3}
$$

The signal from the hidden layer is then processed with a sigmoid function which again normalizes the values between 0 and 1 to produce $O_{j}$ prior to being sent to the output layer. The normalization procedure is performed according to:

$$
O _ {j} = \frac {1}{1 + \exp (- I _ {j})}.\tag{4}
$$

The net signal to an output node $I_{k}$ is the sum of all connections between the hidden layer nodes and the respective output node, expressed as:

$$
I _ {k} = \sum W _ {j k} O _ {j} + W _ {g k},\tag{5}
$$

where $W_{gk}$ represents a single connection weight from a bias node with a value of 1 to the output layer.

The net signal is again normalized with the sigmoid function to produce the final output value $O_{k}$ , where

$$
O _ {k} = \frac {1}{1 + \exp (- I _ {k})}.\tag{6}
$$

In terms of bankruptcy modeling, $O_{k}$ represents the risk of bankruptcy of the individual firm.

## The process of error back-propagation

At the output layer the net signal, $O_{k}$ , (estimated dependent variable), is compared to the actual value of the dependent variable, $T_{k}$ , to produce an error signal which is propagated back through the network. Neuroshell 4.1 implements a variant of the Widrow/Hoff [20] or “least mean square” learning rule known as the Generalized Delta Rule where output layer error signals are propagated back through the network to perform the appropriate weight adjustments after each pattern presentation [9]. Rumelhart et al. [16] describe the process of weight adjustment by:

$$
\Delta W _ {j k} (n + 1) = \eta \delta_ {p k} O _ {p j} + \alpha \Delta W _ {j k} (n),\tag{7}
$$

where $\eta$ is a learning coefficient and $\alpha$ is a “momentum” factor. The momentum factor determines the effect of past weight changes on the current direction of movement in weight space and proportions the amount of the last weight change to be added into the new weight change.

The error signal $\delta$ back-propagated to the connection weights between the hidden and output layers is defined as the difference between the target value $T_{pk}$ for a particular input pattern p and the neural network's feed-forward calculations of the signal from the output layer $O_{k}$ as:

$$
\delta_ {p k} = \big (T _ {p k} - O _ {p k} \big) O _ {p k} \big (1 - O _ {p k} \big).\tag{8}
$$

Then connection weights between the input and hidden layers are changed by:

$$
\delta_ {p j} = O _ {p j} \big (1 - O _ {p j} \big) \sum_ {k} \delta_ {p k} W _ {j k}.\tag{9}
$$

The data feed-forward and error back-propagation process is continued until a “stopping” point is reached. This point is determined by comparing the errors in the training set and the test set. This methodology prevents “overlearning” or fitting the training set “too” closely with consequent large errors in the test set.
