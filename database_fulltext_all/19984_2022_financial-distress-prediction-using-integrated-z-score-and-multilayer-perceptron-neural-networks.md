---
otero_id: 19984
otero_key: "5S78JCE5"
title: "Financial distress prediction using integrated Z-score and multilayer perceptron neural networks"
authors: "Desheng Wu; Xiyuan Ma; David L. Olson"
year: "2022"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2022.113814"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Financial distress prediction using integrated Z-score and multilayer perceptron neural networks

![](/api/attachments/5S78JCE5/fulltext/images/657f5aaa8c46e68e2cd9ebb322049be590b8b4ec0fea76149b8b903fe8fa432e.jpg)

Desheng Wu <sup>a,\*</sup>, Xiyuan Ma <sup>a</sup>, David L. Olson <sup>b</sup>

<sup>a</sup> University of Chinese Academy of Sciences, Beijing, People’s Republic of China

Department of Supply Chain Management and Analytics, College of Business, University of Nebraska, Lincoln 68588-4114, UK

## A R T I C L E I N F O

Keywords: Financial risk Chinese banking Artificial neural networks Z-score model

## A B S T R A C T

The COVID-19 pandemic led to a great deal of financial uncertainty in the stock market. An initial drop in March 2020 was followed by unexpected rapid growth over 2021. Therefore. financial risk forecasting continues to be a central issue in financial planning, dealing with new types of uncertainty. This paper presents a stock market forecasting model combining a multi-laver perceptron artificial neural network (MLP-ANN) with the traditional Altman Z-Score model. The contribution of the paper is presentation of a new hybrid enterprise crisis warning model combining Z-score and MLP-ANN models. The new hybrid default prediction model is demonstrated using Chinese data. The results of empirical analysis show that the average correct classification rate of thew hybrid neural network model (99.40%) is higher than that of the Altman Z-score model (86.54%) and of the pure neural network method (98.26%). Our model can provide early warning signals of a company’s deteriorating financial situation to managers and other related personnel, investors and creditors, government regulators, financial institutions and analysts and others so that they can take timely measures to avoid losses

## 1. Introduction

The COVID-19 pandemic has increased financial uncertainty which has increased the possibility of company failure. Stakeholders need better understanding of the financial status of investment opportunities in order for them to assess expected company survival. To further complicate the issue, the international situation is volatile with inten sifying competition. We examine the financial performance of Chinese companies. Based on Straight Flush Big Data, the number of “special treatment” (\*ST and ST) companies in China’s A-share market is increasing year by year, and so is the proportion in the overall listed companies (China Listed Company Health Index Report, 2021). The number of domestically listed companies in the A-share market has increased by about 41.58% from 2016 (2833 listed companies) to 2020 (4011 listed companies). Fortunately, this growth in proportion does not mean the quality of domestic listed companies declines. This can be confirmed by the fact that the number of ST companies fluctuates only slightly between 55 and 61. All of these numbers are shown in Fig. 1. However, the China Listed Company Health Index Report (2021) dem: onstrates the necessity of solving financial management and quality control problems in listed companies, to improve the financial performance in the capital market and maximize the interests of small investors in listed companies.

All of this suggests the need for an enterprise financial forecasting system to maintain social welfare. Machine learning models are commonly applied to corporate risk analysis. Barboza et al. [7] applied support vector machines, bagging, boosting and random forest and compared results with traditional discriminant analysis, logistic regression and neural networks. Hamori et al. [22] used bagging, random forest, and boosting and compared with neural network models., Kim et al. [27] used machine learning algorithms logistic regression, random forest, support vector machine and feedforward neural network models. [33]) used random forest, extreme gradient boosting tree, gradient boosting model, and neural network models. Thus we see that there are many variants of machine learning models applied. Although there have been many studies applying financial distress prediction [10], our study is unique because we integrate Z-Score and MLP-ANN models to predict the health of listed companies in China’s A-share market. We compare the prediction results of Z-Score model. MLP-ANN model and the combined model separately in order to determine the difference in prediction power of each model and suggest which one is most suitable in China stock market.

![](/api/attachments/5S78JCE5/fulltext/images/88edce0ea02f0c7997cd10f292fc71cedc18028aec090121dbbf22eabf64852e.jpg)  
Fig. 1. Listed and ST companies in China by year, 2016–2020).

The contribution of the paper is presentation of a new hybrid en terprise crisis warning model combining Z-score [5] and MLP-ANN models. The new hybrid default prediction model is demonstrated using Chinese data. The results of empirical analysis show that the average correct classification rate of the hybrid neural network model (99.40%) is higher than that of the Altman Z-score model (86.54%) and of the pure neural network method (98.26%). Our model can provide early warning signals of a company’s deteriorating financial situation to managers and other related personnel, investors and creditors, govern ment regulators, financial institutions and analysts and others so that they can take timely measures to avoid losses.

The structure of the paper is organized as follows: Section 1 explains the reasons and background of our research; Section 2 provides a liter ature review, and Section 3 introduces data sets and variables; Section 4 describes the three approaches employed to make risk prediction, the associated calculations and performance evaluations, while Section 5 summarizes results.

## 2. Literature review

For western scholars, bankruptcy is the symbol of financial crisis. Altman [1] argued that the public declaration of bankruptcy is the sole criterion of financial distress [25]. There can be unintended conse quences from common practices intended to improve cash flow (such as offering early payment discounts), that can contribute to cash flow risk [32]. Poston et al. [29] identified corporate bankruptcy as a dynamic process beginning with the appearance of indicators of poor financial condition, followed by management notices and corresponding rem edies, continuing deterioration, and finally the official announcement of bankruptcy when the assets of company can no longer offset assets anymore. Therefore, financial distress can be detected before insolvency or bankruptcy. So far, no listed company in China’s stock market has declared bankruptcy. It is apparently not appropriate to regard bank ruptcy as a sign of financial distress in China in empirical analysis.

In studies where financial failure is not defined as bankruptcy, some specific ratios can be applied to distinguish financial risk of companies. For example, Ninh et al. [11] use the ratio of earnings before interest, tax, and depreciation (EBITDA) and interest payments in their predic tion model applied in Vietnam. In that model, the firm falls into the financial distress zone when the EBITDA ratio is lower than 1. Campbell et al. [13] emphasize cash flow variables and think negative net cash flow from post-interest operations is a better indicator of financial trouble. Jing and Seidmann [24] studied trade credit versus bank credit, finding that bank credit was more effective when production costs were relatively low, while bank credit was more effective otherwise. Many studies define financial distress as a company’s failure to meet its financial obligations [11,19,31].

According to the Listing rules of the Shanghai Stock Exchange [17] (revised in 2019), when a listed company loses money or the market value of net assets fall lower than the par value of the issued stock for two consecutive years, the name of the stock will be marked “ST”; If this situation continues for a third year consecutive, “\*ST” will be added before the abbreviation of the company’s stock, warning stakeholders that there is a risk of delisting at any time. Although some scholars question the accuracy of using this ST label as a classification tool, this classification standard is still widely used in practical research in China. In this study, we use the ST label to distinguish failed companies from non-failed companies.

## 2.1. Traditional quantitative methods

The Altman Z-score model (1968) is one of the most widely applied prediction tools to predict risks. Other methods such as logit models, probit models, decision trees and neural networks have also been used to supplement these prediction methods $[ 1 5 , 1 9 , 2 5 ]$

Research on predicting business failure dates back to the 1930s [20, 28]. Beaver (1966) first introduced single variable analysis to predict bankruptcy but this technique doesn’t provide sufficient information, making decisions on that basis alone imprudent [23]. Therefore, Altman [1] introduced multiple discriminant analysis (MDA) to select five financial ratios from 22 as predictors in his Z-score model, which suc cessfully identified around 97% of financially sound companies and about 94% of failed companies one year prior to the occurrence of real distress. However, since the data used in that research was based on 66 USA manufacturing companies from 1946 to 1965, the model may not be suitable in Chinese market [23]. Altman et al. [3] modified the in dependent variables set to explore a new default prediction model (ZETA), based on the financial data of 111 companies from 1969 to 1975. He improved the original 1968 and 1977 Z-Score models in 2000. Then, Altman (2005) introduced the emerging markets scoring (EMS) model applicable for developing countries (Binh et al., 2018). The EMS model accuracy was evaluated by Al Zaabi and Obaid Saif using UAE data in 2011 [6]. To summarize, the Z-Score model has evolved for special applications over the period 1968 to 2005.

Altman’s [1] Z-Score model and its variants are still widely used. For example, Cleary and Hebb increased Altman’s [1] factors slightly to include bank-specific measures related to loan dependence, loan quality, capital adequacy ratio and off-balance sheet items in using discriminant analysis to predict bank distress [15]. Almamy et al. [6] added cash flow variables to the original Z-Score model, creating the new J-UK model which tested at predictive power of 82.9%.

These traditional statistical methods with simple structure and strong interpretation ability are widely used. However, in practice, the potential assumptions of these methods are not satisfied (Merkevicius et al., 2006). It is rare for early warning indicators to strictly follow a normal distribution, avoid collinearity within variables and provide linearly separable warning samples. In order to overcome these de ficiencies, researchers have explored other functional statistical tools [26].

## 2.2. The application of multilayer perceptron artificial neural networks (MLP-ANNs)

Artificial neural network models (ANN) originated in 1982. Nag and Mitra (1999) first applied an ANN model for early warning prediction, providing more diversified warning models with stronger predictive power (Fioramanti, 2008). An ANN prediction model is based on nonlinear and nonparametric multivariate statistics. The early warning effect of ANN model is superior to parametric and non-parametric models under certain conditions. It overcomes the limitations of tradi tional quantitative prediction methods and has no sample distribution requirements. It can give a nonlinear mapping between input (database) and output (result) to capture the unknown relationship between different variables and finally form a learning model with discriminant ability. There are many types of ANN models, such as multi-layer per ceptron (MLP) and radial basis function (RBF). MLP is usually more

![](/api/attachments/5S78JCE5/fulltext/images/bcb696c3738952a6ee2c4862a408293f53927dea71a66b2ddddb65e72275e057.jpg)  
Fig. 2. A three-layer neural network.

widely accepted [4].

The ANN model is composed of three processing neuron units/nodes: input node, hidden layer node and output node [14]. The input node deals with observations/independent variables from the data Activation functions such as the softmax function to build connections between input nodes and hidden layer nodes. The processed information is passed through hidden layer nodes on to output nodes. Output node results yield model results which are compared with the expected results as a basis to adjust parameters [30]. There can be multiple hidden layer nodes, and prediction accuracy largely depends on the number of hidden layers. Therefore, the number of hidden layers should be determined through continuing training and adjustments. Fig. 2 shows a schematic diagram of a three-tier MLP-ANN.

## 2.3. Integration of traditional quantitative methods and MLP-ANNs model

Even though neural networks are a black box model hiding how data is processed, this MLP-ANNs tool does not restrict the type of data and copes relatively well with nonlinear relationships between variables, with good learning ability and error tolerance ability, prediction ability and strong operability. This is especially useful when the sample in cludes small businesses. MLP-ANNs perform significantly better than traditional quantitative methods [16]. However, MLP-ANNs also have obvious disadvantages: training time is often too long; calculations are complicated, models have low relative stability and insufficient ability to explain; results lack generalization, easily fall into a local optimum and often suffer from over-fitting [34].

New innovative tools can improve management of financial risk. Groth and Muntermann [21] noted that financial risk is one of the most challenging tasks that financial institutions face. They suggested text mining as a useful tool, and discussed data mining tools available to support it. Basole and Bellamy [8] demonstrated the importance of vi sual decision support to aid in risk assessment.

Coats & Fant [12] argued that the combined use of MDA and ANN could correctly classify different enterprises with varying financial po sitions. After reviewing 165 bankruptcy forecasting studies involving general firms and financial institutions since 1985, Bellovary et al. [9] concluded that the application of MDA and ANN methods would be more widely used in future. China is a developing country with an emerging capital market. So when applying MDA and ANN methods in China, some modifications may be required to build a new hybrid default forecasting model. Therefore, maximizing the prediction accu racy of the new hybrid model applied in China will be the key point in this paper. A new hybrid enterprise crisis warning model is constructed by combining Z-Score model with MLP-ANNs model to better predict the performance of Chinese listed companies.

Table 1  
The definition of variables.

<table><tr><td>Variables</td><td>Clarification</td><td colspan="2">Index</td><td>Explanation/Computation</td></tr><tr><td>DV</td><td></td><td>Financial condition</td><td>Y</td><td>Financial distress = 0Others = 1</td></tr><tr><td>IV</td><td>Short-term solvency</td><td>WCTA</td><td>X1</td><td>WC=CA-CLThe more current capital, the less risk of insolvency</td></tr><tr><td>IV</td><td>Profitability</td><td>RETA</td><td>X2</td><td>Firms with high RE/TA ratios have a low default probabilityRE = undistributed profits + surplus reserve</td></tr><tr><td>IV</td><td>Operating capacity</td><td>EBITTA</td><td>X3</td><td>EBIT = Total profits + Financial expensesThis ratio measures the production capacity of an enterprise&#x27;s assets without considering the influence of taxation and financing. The higher the ratio, the better the asset utilization effect and the higher the management level.</td></tr><tr><td>IV</td><td>Capital structure/ Leverage</td><td>MVETL</td><td>X4</td><td>MVE = Market value of stocks*Total number of stocksThis ratio reflects the relative relationship between the capital provided by shareholders and creditors. The higher the ratio, the lower ratio the risk level.</td></tr><tr><td>IV</td><td>Profitability/ Development Capacity</td><td>STA</td><td>X5</td><td>The higher the index, the higher the utilization rate of assets, indicating that enterprises have a good effect in increasing income.</td></tr></table>

Note: WCTA -working capital over total assets, RETA -retained earnings over total assets, EBITTA -earnings before interest and taxes (operating profit) to total assets, MVETL-market value of equity to total liabilities and STA -sales to total assets.

## 3. Data and variables

This paper uses a database obtained from financial statement data of all companies listed on the Shenzhen and Shanghai stock exchanges from 2016 to 2020. By using average values to replace missing values, a total of 17,206 observations were collected. Based on whether the company is marked by \*ST and ST or not, the dataset divides Chinese listed companies into two categories, namely the financially distressed group (coded as 0) and the financial health group (coded as 1). All financial data are obtained from the CSMAR database.

Enterprise performance can be evaluated by solvency, operating capacity, profitability and development capacity. There are many financial ratios used to measure these four concepts and the relative importance of these ratios is still unclear [1]. Almamy et al. [6] pointed out that increase in financial factors does not always improve model explanation ability and predictive accuracy. Previous studies have used principal factor analysis to select financial indicators with signigicant correlation. This paper directly applies five of Altman’s independent variables to predict financial distress. The definition and computation of variables is shown in Table 1.

Table 2  
Description statistics of the dependent variable

<table><tr><td>Classify</td><td>Frequency</td><td>Percent</td><td>Cum.</td></tr><tr><td>0 (ST or *ST)</td><td>293</td><td>1.70</td><td>1.70</td></tr><tr><td>1 (others)</td><td>16,913</td><td>98.30</td><td>100</td></tr><tr><td>Total</td><td>17,206</td><td>100</td><td></td></tr></table>

Table 3  
Summary of statistics for independent variables.

<table><tr><td>Variable</td><td>Observations</td><td>Minimum</td><td>Maximum</td><td>Mean</td><td>Std. Deviation</td></tr><tr><td>WCTA</td><td>17,206</td><td>-147.7538</td><td>0.9587</td><td>0.2237</td><td>1.1835</td></tr><tr><td>RETA</td><td>17,206</td><td>-184.8072</td><td>0.8268</td><td>0.0872</td><td>1.9531</td></tr><tr><td>EBITTA</td><td>17,206</td><td>-29.2880</td><td>8.1491</td><td>0.0373</td><td>0.4102</td></tr><tr><td>MVETL</td><td>17,206</td><td>0.5951</td><td>698.1363</td><td>8.1741</td><td>16.1666</td></tr><tr><td>STA</td><td>17,206</td><td>-0.0502</td><td>11.6019</td><td>0.5967</td><td>0.5080</td></tr></table>

## Table 4

Z-score model.

<table><tr><td>Rating</td><td>Z-score value</td><td>Percentage</td></tr><tr><td>Safe zone</td><td>12,278</td><td>71.36</td></tr><tr><td>Grey zone</td><td>2735</td><td>15.90</td></tr><tr><td>Distress zone</td><td>2193</td><td>12.75</td></tr><tr><td></td><td>17,206</td><td>100</td></tr></table>

## 4. Methodology and computation

In this study, companies marked ST or \*ST are considered as finan cially distressed (failed) companies (293 (1.70%) observations) while 16,913 (98.30%) observations are financially healthy (non-failed) companies, as shown in Table 2. Five predictors (or independent vari ables) are presented in Table 3: WCTA (ratio of working capital to total assets), RETA (ratio of retained earnings to total assets), EBITDA (ratio of EBITDA to total assets), MVETA (ratio of market value of equity to total liabilities) and STA (ratio of sales to total assets). The response variable is the financial condition of the listed company - financial distress (coded as 0) or financial health (coded as 1). We divided the 17,206 datasets in a 7:3 ratio. 12,055 observations will be used as training sample, and the remaining 5151 will be retained as testing sample. The Z-score model, MLP-ANNs model as well as the hybrid model will be implemented using the popular SPSS software. Detailed predictions can be summarized below.

## 4.1. Altman Z-score model

The Altman Z-score model combined five financial ratios with different weights to produce a single Z score number - see formula (1). The Z value represents the overall financial health index of enterprises. The function of the accounting-based Altman Z-score model is shown as follow:

$$
Z = 1. 2 \times 1 + 1. 4 \times 2 + 3. 3 \times 3 + 0. 6 \times 4 + 0. 9 9 \times 5\tag{1}
$$

Altman [2] identified the best threshold for z value is 2.675.

-Z > 2.675: Safe zone, in which firms are financially healthy or no risk of bankruptcy.

\- Z = [1.8, 2.675]: Grey/warning zone. The probability for bank ruptcy exists and management attention is required while the financial condition is acceptable.

\- Z < 1.8: Bankruptcy/danger zone. The default probability is high and financial condition is poor.

Table 4 presents the credit ratings of listed firms using Altman Zscore models in the 2016–2020 period: 87.25% of firms are in the safe and grey zones (non-failed), whereas only 12.75% are in the distress zone (failed).

These statistics are misleading in that they can create a false illusion that the financial conditions of most Chinese firms are stable. We cannot ignore the potentially high motivation for management personnel in Chinese listed companies to manipulate accounting profits and distort financial statements. They prefer to present their investors and super visors with a good face so that they can ensure continued cash inflow from stock market investors [18]. Therefore the validity of analysis may to some extent be affected.

Table 5  
Classification results using Altman Z-score model.

<table><tr><td rowspan="2">Actual class</td><td colspan="2">Classified class</td><td></td></tr><tr><td>Failed</td><td>Not failed</td><td>Total</td></tr><tr><td>Failed</td><td>85 (29%)</td><td>208 (71%)</td><td>293 (100%)</td></tr><tr><td>Not failed</td><td>2108 (12.5%)</td><td>14,805 (87.5%)</td><td>16,913 (100%)</td></tr></table>

Average correct classification rate: 86.54%

## Table 6

Distribution of training and testing sample in MLPANN.

<table><tr><td></td><td></td><td>N</td><td>Percent</td></tr><tr><td rowspan="2">Sample</td><td>Training</td><td>12,055</td><td>70.10%</td></tr><tr><td>Testing</td><td>5151</td><td>29.90%</td></tr><tr><td>Total</td><td></td><td>17,206</td><td>100.00%</td></tr></table>

The predictive power of the Altman Z-score model (1968) is shown in Table 5. We observe that the average correct prediction rate is 86.54%. Furthermore, the percentage of correctly classified failed companies is 29.0%, while the percentage of correctly classified non-failed companies is 87.5%. And the class I error rate is 71.0% and the class II error rate is 12.5%.

## 4.2. Multilayer perceptron artificial neural networks (MLP-ANNs)

Using the MLP-ANN approach, the 17,206 observation samples are divided into 12,055 learning samples and 5151 testing samples in a ratio of 7:3, and 11 financial index data as input data Xi, with 11 input nodes. There is 1 output node with two neurons defining output corresponding to ST and \*ST companies. As stated, \*ST samples are coded as 0, and the output corresponding to other company samples is 1. The excitation function of output layer used is the softmax function. The number of neurons in the hidden layer is determined to be 4 based on cyclic training. The excitation function for hidden layers is the hyperbolic tangent function. After using training samples to get a neural network model with required precision, we use the test samples to further judge its prediction ability. Results are given in Table 6 and Fig. 3 below:

Table 7 summarizes prediction results using the designed MLPANN model. Among the training samples, all 199 observations with ST were misjudged, and the correct rate was 0.00%; 6 of the 11,856 observations without ST were misjudged as in financial distress, and the correct rate was 99.95%; The class I error rate is 100.00% and the class II error rate is 0.05%; The comprehensive correct rate of training samples is 98.30%. Among the testing samples, 93 of the 94 observations with ST were misjudged, and the correct rate was 1.06%; Two of the 5057 observa tions without ST were misjudged, and the correct rate was 99.96%; The class I error rate, class II error rate and comprehensive accuracy rate are 98.94%, 0.04% and 98.16% respectively. These results reflect severely imbalanced data.

From the overall sample, 292 of the 293 observations with ST were misjudged, and the correct rate was 0.34%; eight of the 16,913 obser vations that did not have ST were misjudged, and the correct rate was 99.95%; the class I error rate, class II error rate and the overall comprehensive accuracy of the sample are 99.66%, 0.05% and 98.26% respectively. By comparing the results of Tables 4 and Table 6, MLPANN has the higher average correct classification rate in comparison with the Altman Z-score model approach.

## 4.3. Integrated Z-score and MLP-ANN models

To test the predictive power of the integrated method, 17,206 ob servations in the sample were also divided into training and testing samples respectively, in a proportion of 7:3.

The two-stage hybrid neural discriminant technique uses the Z-score

![](/api/attachments/5S78JCE5/fulltext/images/333f9dc02e3e0199ccfd36f468e19482d84d940f06390fdbe32540e7b40cd6c6.jpg)  
Hidden layer activation function: Hyperbolic tangent Output layer activation function: Softmax  
Fig. 3. The three-layer neural network.

Notes: Inputs definitions: CA – current assets, TA – total assets, CL – current liabilities, TL – total liabilities, SR – surplus reserves, UP – undistributed profits, MVB – market value (B), OI – operating income, FE – financial expenses, TP – total profits, and MVA – market value (A).

Table 7  
Classification results using MLP-ANN model.

<table><tr><td rowspan="2">Sample</td><td rowspan="2">Actual class</td><td>Classified class</td><td></td><td></td></tr><tr><td>Failed</td><td>Not failed</td><td>Total</td></tr><tr><td rowspan="2">Training</td><td>Failed</td><td>0 (0.00%)</td><td>199 (100.00%)</td><td>199 (100%)</td></tr><tr><td>Not failed</td><td>6 (0.05%)</td><td>11,850 (99.95%)</td><td>11,856 (100%)</td></tr><tr><td colspan="5">Average correct classification rate: 98.30%</td></tr><tr><td rowspan="2">Testing</td><td>Failed</td><td>1 (1.06%)</td><td>93 (98.94%)</td><td>94 (100%)</td></tr><tr><td>Not failed</td><td>2 (0.04%)</td><td>5055 (99.96%)</td><td>5057 (100%)</td></tr><tr><td colspan="5">Average correct classification rate: 98.16%</td></tr><tr><td rowspan="2">Overall</td><td>Failed</td><td>1 (0.34%)</td><td>292 (99.66%)</td><td>293 (100%)</td></tr><tr><td>Not failed</td><td>8 (0.05%)</td><td>16,905 (99.95%)</td><td>16,913 (100%)</td></tr><tr><td colspan="5">Average correct classification rate: 98.26%</td></tr></table>

model to select the characteristic variables that can be used to distin guish “failed” and “non-failed” firms, and take these five significant variables in Z-score model, that is, WCTA (X1), RETA (X2), EBITTA (X3), MVETA (X4) and STA (X5), as the input units of the neural network model, and then the default risk prediction model is established, with one input layer containing five input nodes. Companies in the sample were classified into three groups: group of companies in the financially healthy group (2), companies in the grey area (1) and companies in the financially distressed group (0) based on the discriminant result using Zscore model. That is, the output corresponding to financial distress company samples $( Z ~ < ~ 1 . 8 )$ is 0, and the output corresponding to company samples in grey area $( 1 . 8 \leq \mathsf { Z } \leq 2 . 6 7 5 )$ is 1 and the output corresponding to healthy company samples $( \mathsf { Z } > 2 6 7 5 )$ is 2. These three situations are three neuron nodes in the output layer in the hybrid neural network model. The hyperbolic tangent excitation function is used for hidden layers and the softmax activation function used for the output layer. We believe that this model overcomes some defects of simple use of a neural network model or Z-score model. The process of the hybrid model is shown in Fig. 4. And the architecture of the 3-layer 5–5-3

![](/api/attachments/5S78JCE5/fulltext/images/64fa4ab5d07c800f20b09982ac6e4ae2ec56716368d2718ed5c9fe3cf41076b5.jpg)  
Fig. 4. Process of the hybrid model.

![](/api/attachments/5S78JCE5/fulltext/images/9ebf9fda468d907c163c2233a5b8420e3a9361b9819f9901407e6fee50d4d22e.jpg)  
Hidden layer activation function: Hyperbolic tangent  
Output layer activation function: Softmax  
Fig. 5. The three-layer hybrid neural model.

neural network is shown in Fig. 5.

Table 8 presents the credit scoring results using the hybrid model. The average correct classification rate is 99.3% in training sample and

Table 8  
Classification results using hybrid model.

<table><tr><td rowspan="2">Sample</td><td rowspan="2">Actual class</td><td colspan="3">Classified class</td><td></td></tr><tr><td>0</td><td>1</td><td>2</td><td>Total</td></tr><tr><td rowspan="4">Training</td><td>0</td><td>1514(98.2%)</td><td>27 (0.8%)</td><td>0</td><td>1541(100%)</td></tr><tr><td>1</td><td>19 (0.9%)</td><td>1886</td><td>22 (1.1%)</td><td>1927</td></tr><tr><td>2</td><td>0</td><td>(97.9%)</td><td>8584</td><td>(100%)</td></tr><tr><td></td><td></td><td>11 (0.1%)</td><td>(99.9%)</td><td>8595(100%)</td></tr><tr><td colspan="6">Average correct classification rate: 99.3%</td></tr><tr><td rowspan="4">Testing</td><td>0</td><td>644(98.8%)</td><td>8 (1.2%)</td><td>0</td><td>652 (100%)</td></tr><tr><td>1</td><td>8 (0.9%)</td><td>791</td><td>9 (1.0%)</td><td>808 (100%)</td></tr><tr><td>2</td><td>0</td><td>(97.9%)</td><td>3679</td><td>3683</td></tr><tr><td></td><td></td><td>4 (0.1%)</td><td>(99.9%)</td><td>(100%)</td></tr><tr><td colspan="6">Average correct classification rate: 99.4%</td></tr><tr><td rowspan="4">Overall</td><td>0</td><td>2158(98.4%)</td><td>35 (1.6%)</td><td>0</td><td>2193(100%)</td></tr><tr><td>1</td><td>27 (0.9%)</td><td>2677</td><td>31 (1.1%)</td><td>2735</td></tr><tr><td>2</td><td>0</td><td>(97.9%)</td><td>12,263</td><td>(100%)</td></tr><tr><td></td><td></td><td>15 (0.1%)</td><td>(99.9%)</td><td>12,278(100%)</td></tr><tr><td colspan="6">Average correct classification rate: 99.4%</td></tr></table>

Table 9  
Prediction results of the three constructed models.

<table><tr><td>Risk prediction models</td><td>Risk prediction results</td></tr><tr><td></td><td>Average correct classification rate</td></tr><tr><td>Altman Z-score model</td><td>86.54%</td></tr><tr><td>Multilayer Perceptron Artificial Neural Networks</td><td>98.26%</td></tr><tr><td>Integrated Z-score and MLP ANN model</td><td>99.40%</td></tr></table>

99.4% in testing sample respectively and the overall correct classifica tion rate is 99.4%.

Finally, in order to evaluate the prediction capabilities of these three models, summarized results are shown in Table 9. From these results we conclude that the integrated Z-score and MLP-ANNs model has the best prediction power in terms of the average classification rate in compar ison with Altman z-score model and pure ANN models. Note that here dataset imbalance is eliminated by using the Z-score scale.

## 5. Conclusion and areas of future research

China’s economic development and the domestic capital market are under great pressure and instability due to the impact of the trade war between China and the United States as well as the impact of COVID-19. Trading frequency has declined and the financial leverage of firms has reached a new peak, which makes it hard for firms to survive. Increased credit risk events call for an effective risk prediction model so that parties can detect financially unhealthy firms in advance, which indi rectly encourages high-quality cash management and financial trans actions of firms in this special period. Risk prediction technology such as traditional statistical analysis and artificial intelligence techniques have been widely used to successfully predict the possibility of one company falling into financial distress. Among these techniques, two of the most promising modeling tools are the Altman Z-score model and MLP-ANNs.

The purpose of this study is to explore a hybrid model combining Z score model and MLP-ANNs method. The five significant predictors in the Z-score function are regarded as the input variables of the designed hybrid model. The discriminant results of the Z-score model are treated as the output units in the output layer. The empirical results show that the new hybrid model could achieve the highest average correct clas sification rate (99.40%) compared with the Z-score model (86.54%) and the pure neural network method (98.26%). While the MLP-ANN model had a high overall classification success rate, that was biased by applying it to a very imbalanced data set. While that model was not degenerate (calling all cases safe from bankruptcy), it did have rare predicted bankruptcies. The Z-score portion of the integrated model took care of the dataset imbalance problem.

The contribution of the paper is the new hybrid enterprise crisis warning model combining Z-score and MLP-ANN models. Empirical analysis found that the hybrid neural network model fit the data tested slightly better than the Altman Z-score model and the pure neural network method. The implication is that our model can provide early warning signals of a company’s deteriorating financial situation to managers and other related personnel, investors and creditors, govern ment regulators, financial institutions and analysts and others so that they can take timely measures to avoid losses.

There are still some deficiencies in this paper requiring further exploration. First, some variables in the Z-score model are highly correlated and more work is needed to eliminate collinearity. Subse quently, we could introduce a wider variety of variables including qualitative variables for principal component analysis or factor analysis to find significant factors which play the decisive role in determining the financial health level of firms. In addition, we could find more finan cially distressed companies beyond those listed, such as small busi nesses. However, the availability of data of small businesses may be an obvious obstacle for such following research.

## Author contribution

Coauthored by Desheng Wu and Xiyuan Ma of the Chinese Academy of Sciences and David L. Olson of the University of Nebraska.

Xiyuan Ma contributed conceptualization and data curation..

Desheng Wu contributed to formal analysis, methodology, project administration and supervision.

David L. Olson contributed to validation and writing - review and editing.

## Acknowledgements

This work was supported in part by the Ministry of Science and Technology of China under Grant 2020AAA0108400 and 2020AAA0108402, in part by the National Natural Science Foundation of China under Grant 71825007, in part by the Strategic Priority Research Program of CAS under Grant XDA2302020.

## References

[1] E.I. Altman, Financial ratios, discriminant analysis and the prediction of corporate bankruptcy, J. Financ. 23 (4) (1968) 589–609.

[2] E.I. Altman, Revisiting credit scoring models in a Basel 2 environment, in: M. Ong (Ed.). Credit Rating: Methodologies, Rationale and Default Risk, Risk Books London, 2002, pp. 151–167.

[3] E.I. Altman, R.G. Haldeman, P. Naravanan, ZETATM analysis a new model to identify bankruptcy risk of corporations, J. Bank. Financ. 1 (1) (1977) 29–54.

[4] J. Antari, S. Chabaa, A. Zeroual, Modeling nonlinear real processes with ANN techniques, Int. Conf, Multimedia Comput Syst. 2011 (2011) 1–5

[5] E.I. Altman, Applications of distress prediction models: what have we learned after 50 vears from the Z-score models? Int. J. Financ. Stud. 6 (3) (2018) 70.

[6] J. Almamy, J. Aston, L.N. Ngwa, An evaluation of Altman’s Z-score using cash flow ratio to predict corporate failure amid the recent financial crisis: evidence from the UK, J. Corp. Finan. 36 (2016) 278–285.

[7] F. Barboza, H. Kimura, E. Altman, Machine learning models and bankruptcy

[8] R.C. Basole, M.A. Bellamy, Visual analysis of supply network risks: insights from the electronics industry. Decis, Support, Syst, 67 (2014) 109–120

[9] J.L. Bellovary, D.E. Giacomino, M.D.A. Akers, Review of bankruptcy prediction studies: 1930 to present, J. Financ. Educ. (2007) 1–42.

[10] D. Bianchi, M. Büchner, T. Tamoni, Bond risk premiums with machine learning Rev. Financ. Stud. 34 (2) (2021) 1046–1089.

[11] Binh Pham Vo Ninh, Trung do Thanh, Duc Vo Hong, Financial distress and bankruptcy prediction: an appropriate model for listed firms in Vietnam, Econ. Syst. 42 (4) (2018) 616–624.

[12] P.K. Coats, L.F. Fant, Recognizing financial distress patterns using a neural network tool, Financ. Manag. 22 (3) (1993) 142–154.

[13] J.Y. Campbell, J. Hilscher, J. Szilagyi, In search of distress risk, J. Financ. 63 (6) (2008) 2899–2939.

[14] M. Chakraborty, B. Tudu, Comparison of ANN models to predict LDL level in diabetes mellitus type 2, Int. Conf. Syst. Med. Biol. 2010 (2010) 392–396.

[15] S. Cleary, G. Hebb, An efficient and functional model for predicting Bank distress: in and out of sample evidence. J. Bank. Financ. 64 (2016) 101–111.

[16] F. Ciampi, N. Gordini, Small Enterprise default prediction modeling through artificial neural networks: an empirical analysis of Italian small enterprises, J. Small Bus. Manag. 51 (1) (2013) 23–45.

[17] F.C. Cheng, China listed company health index report, in: China Financial and Economic Press, 2021, pp. 420–422.

[18] E. Demers, P. Joos, IPO failure risk, J. Account. Res. 45 (2) (2007) 333–371.

[19] D. Duffie, L. Saita, K. Wang, Multi-period corporate default prediction with stochastic covariates, J. Financ. Econ. 83 (3) (2007) 635–665

[20] P. Fitzpatrick, A comparison of ratios of successful industrial enterprises with those of failed firms, Certif. Public Accountant 1 (1) (1932) 598–605.

[21] S.S. Groth, J. Muntermann, An intraday market risk management approach based on textual analysis, Decis. Support. Syst. 50 (4) (2011) 680–691.

[22] S. Hamori, M. Kawai, T. Kume, Y. Murakami, C. Watanabe, Ensemble learning or deep learning? Application to default risk analysis, J. Risk Financ. Manag. 11 (1) (2018) 1–14.

[23] T.H. Huang, Y. Leu, W.T. Pan, Constructing ZSCORE-based financial crisis warning models using fruit Fly optimization algorithm and general regression neural network, Kybernetes 45 (4) (2016) 650–665.

[24] B. Jing, A. Seidmann, Finance sourcing in a supply chain, Decis. Support. Syst. 58 (2014) 15–20.

[25] S. Jones, D.A. Hensher, Predicting firm financial distress: a mixed Logit model, Account. Rev. 79 (4) (2004) 1011–1038.

[26] S. Khemakhem, Y. Boujelbene, Credit risk prediction: a comparative study between discriminant analysis and the neural network approach, Account. Manag. Inf. Syst. 14 (1) (2015) 60.

[27] H. Kim, H. Cho, D. Ryu, Predicting corporate defaults using machine learning with geometric-lag variables, Invest. Anal. J. 50 (3) (2021) 161–175.

[28] J.A. Ohlson, Financial ratios and the probabilistic prediction of bankruptcy, J. Account. Res. 18 (1) (1980) 109–131.

[29] K.M. Poston, K. Harmon, J.D. Gramlich, A test of financial ratios as predictors of turnaround versus failure among financially distressed firms, J. Appl. Bus. Res. 10 (1) (1994) 41–56.

[30] J.C. Patra, R.N. Pal, B.N. Chatterji, G. Panda, Identification of nonlinear dynamic systems using functional link artificial neural networks. JEEE Transactions on Systems. Man, and Cybernetics. Part B (Cybernetics) 29 (2) (April 1999) 254–262.

[31] Shariq Mohammed, Bankruptcy prediction using the Altman Z-score model in Oman: a case study of Raysut cement company SAOG and its subsidiaries. Australas Account Bus Financ J. 10 (4) (2016)

[32] C.-Y. Tsai, On supply chain cash flow risks, Decis, Support, Syst, 44 (4) (2008) 1031–1042.

[33] J. Xu, Z. Lu, Y. Xie, Loan default prediction of Chinese P2P market: a machine learning methodology, Sci, Rep. 11 (1) (2021) 1–19.

[34] C. Zanchettin, T.B. Ludermir, L.M. Almeida, Hybrid training method for MLP: optimization of architecture and training, IEEE Transactions on Systems, Man, and Cybernetics, Part B (Cybernetics) 41 (4) (Aug. 2011) 1097–1109.

![](/api/attachments/5S78JCE5/fulltext/images/c0feb2e0364a1d840f62c2096605a777d7b94683ac174f6f99086b9043d8bddc.jpg)

David L. Olson is the James & H.K. Stuart Professor and Chancellor's Professor at the University of Nebraska. He has published research in over 200 refereed journal articles, primarily on the topic of multiple objective decision-making, in formation technology, supply chain risk management, and data mining. He teaches in the management information systems, management science, and operations management areas. H has authored over 40 books, to include Decision Aids for Se lection Problems, Introduction to Information Systems Project Management, Managerial Issues of Enterprise Resource Plan ning Systems, Supply Chain Risk Management, and Supply Chain Information Technology. Additionally, he has coauthored the books Introduction to Business Data Mining, En

terprise Risk Management, Advanced Data Mining Techniques, Enterprise Information Systems, Enterprise Risk Management Models, and Financial Enterprise Risk Management. He has served as associate editor of Service Business, Decision Support Systems, and De cision Sciences and co-editor in chief of International Journal of Services Sciences. He has made over 200 presentations at international and national conferences on research topics. He is a member of the Decision Sciences Institute, the Institute for Operations Research and Management Sciences, and the Multiple Criteria Decision Making Society. He was a Lowry Mays endowed Professor at Texas A&M University from 1999 to 2001. He was named the Raymond E. Miles Distinguished Scholar award for 2002, and was a James C. and Rhonda Seacrest Fellow from 2005 to 2006. He was named Best Enterprise Information Systems Educator by IFIP in 2006. He is a Fellow of the Decision Sciences Institute.

![](/api/attachments/5S78JCE5/fulltext/images/9873c355b2cc79b84a68ed45feb506688ff3223f579fb0981f9474a92d369350.jpg)

Desheng Wu is a Distinguished Professor with the Economics and Management School, University of Chinese Academy of Sciences, Beijing, China, and Professor with the Stockholm Business School, Stockholm University, Sweden, He has pub lished over 150 ISI-indexed papers in refereed journals, such as Production and Operations Management, Decision Sciences, Risk Analysis, and the IEEE Transactions on Systems, Man, and Cy bernetics, and 7 books at Springer etc. He has been invited to give plenary lectures and keynote talks in various international conferences more than 20 times. His current research interests include mathematical modeling of systems containing uncer tain and risky situations with special interests in the finance economics operations interface, maximizing operational and

financial goals using the methodologies for game theory, and large-scale optimization. He is Elected Member of Academia Europaea (The Academy of Europe), and Elected Member of European Academy of Sciences and Arts, and Elected Member of International Eurasian Academy of Sciences. Prof. Wu was a recipient of the ten big impact articles in the Journal of the Operational Research Society, 2019 Elsevier Most Cited Researcher, the Top 25 Hottest Article in Elsevier Journals. and the Best Paper Award Most Cited Articles in Human and Ecological Risk Assessment. He has served as an Associate Editor and a Guest Editor fo several journals, such as Risk Analysis, IEEE Transactions on Systems, Man, and Cybernetics, the Annals of Operations Research. Computers and Operations Research. the International Journal of Production Economics, and Omega. He serves as the book series editor or computational risk management at Springer.

Xiyuan Ma is a graduate student in the University of Chinese Academy of Sciences, Bei jing, China.
