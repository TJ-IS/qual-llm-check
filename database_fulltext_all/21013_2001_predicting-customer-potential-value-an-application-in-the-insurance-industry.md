---
otero_id: 21013
otero_key: "3Z7FKKN8"
title: "Predicting customer potential value an application in the insurance industry"
authors: "Peter C. Verhoef; Bas Donkers"
year: "2001"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(01)00110-5"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Predicting customer potential value an application in the insurance industry

Peter C. Verhoef <sup>)</sup>, Bas Donkers <sup>1</sup>

Erasmus UniÕersity Rotterdam, Department of Marketing and Organization, Office H15-12, P.O. Box 1738, NL-3000 DR Rotterdam, The Netherlands

## Abstract

For effective Customer Relationship Management CRM , it is essential to have information on the potential value ofŽ . customers. Based on the interplay between potential value and realized value, managers can devise customer specific strategies. In this article, we introduce a model for predicting the potential value of a current customer. Furthermore, we discuss and apply different modeling strategies for predicting this potential value. q 2001 Elsevier Science B.V. All rights reserved.

Keywords: Customer relationship management; Customer potential; Marketing models; Insurance industry

## 1. Introduction

Since general recognition of the marketing principle that keeping customers is more profitable than attracting new customers 2 , many companies have<sup>w</sup> <sup>x</sup> adopted relationship marketing 7 . In relationship <sup>w</sup> <sup>x</sup> marketing, managers strive to develop and maintain successful customer relationships 16 . Only recently, <sup>w</sup> <sup>x</sup> companies realized that in order to develop such relationships a differentiated approach is needed <sup>w</sup> <sup>x</sup> 3,22 . Instead of treating all customers equally, managers have come to understand that it is more effective to develop customer-specific strategies. As a result, companies are now adopting customer relationship management CRM . CRM means that com-Ž . panies manage relationships with individual customers with the aid of customer databases andŽ . interactive and mass customization technologies 17 .<sup>w</sup> <sup>x</sup> The adoption of CRM has been enhanced by recent developments in Information and Communication Technology e.g., Database Technology, E-com-Ž merce, and the Internet ..

By using customer information contained in databases, companies can invest in the customers that are potentially valuable for the company, butŽ . also minimize their investments in non-valuable customers. Figures on the turnover of each customer or customer profitability are often used as segmentation variables to distinguish between valuable and nonvaluable customers. In this way database analysts construct customer pyramids, as shown in Ref. 19 ,Ž <sup>w</sup> <sup>x</sup> p. 187 . This type of segmentation can be valuable in. a single service setting, but it can also be misleading for multi-service or multi-product providers. These providers are not only interested in the current value of customers, but also attach importance to information on cross-selling opportunities. For example, although a customer may currently purchase only a small number of the services offered by the focal company, he might potentially be very valuable, as he may also purchase many other services. Therefore, we propose to use not only information on the current value of a customer, but also the potential value of a customer 4,12,13 . Potential value is<sup>w</sup> <sup>x</sup> defined as the profit or value delivered by a customer if this customer behaves ideally, i.e., the customer purchases all products or services he currently buys in the market at full prices at the focal company <sup>w</sup> <sup>x</sup> 9,12 . Combining information on a customer’s potential value and a customer’s current value provides the CRM-manager with an opportunity to extend the Acustomer pyramidB segmentation. A two-by-two segmentation, as displayed in Fig. 1, is proposed, which creates a better basis for customer specific strategies. For example, companies can decide to target investments on the customers with a low current value, but high potential value. We will discuss such a segmentation of the customer base in Section 2.

To obtain information on the potential value of a customer, analysts need data on the customer’s purchasing behavior at their own company, as well as at other companies in the market. Usually, companies only have data on customers’ purchasing behavior at their own company in their customer information file Ž . CIF 21 . Hence, models are needed to predict the<sup>w</sup> <sup>x</sup> potential value of a customer, based on the purchasing behavior in the CIF, and on any available sociodemographic data.

<table><tr><td rowspan="2" colspan="2"></td><td colspan="2">CURRENT VALUE</td></tr><tr><td>Low</td><td>High</td></tr><tr><td rowspan="2">CUSTOMER POTENTIAL VALUE</td><td>High</td><td>II</td><td>IV</td></tr><tr><td>Low</td><td>I</td><td>III</td></tr></table>

Fig. 1. Segmentation with current value and customer potential.

Zeithaml 22 states that a lot of work needs to be<sup>w</sup> <sup>x</sup> done on identifying the potential value of current customers. Numerous models have been developed to predict single transactions e.g., Ref. 4 andŽ <sup>w</sup> <sup>x</sup>. some work has been done to predict purchase patterns at the focal supplier 20 . Kim and Kim 15 describe a model that estimates the upselling potential for a one-product or service provider, but apparently, no models are available that predict the potential value of a customer in a multi-service context. An exception is the work of Kamakura et al. 14 ,<sup>w</sup> <sup>x</sup> who describe a model that explains the financial maturity of customers. However, their approach depends critically on the hierarchy of investment objectives, which is not a general feature of multiple product or service industries.

Given the above literature overview on customer potential value models, the objective of our paper is to develop a framework that provides insight into the potential value of customers to CRM-managers in a multi-service industry. We will compare different modeling approaches to find the most informative ones. Specifically, we will compare a choice-based model using Univariate and Multivariate Probit, with a potential value model, based on a linear regression model.

By this paper, we extend the CRM-literature in the following respects. First, in the scientific context, our study is the first to focus on the modeling and prediction of the potential value of customers of a multi-service provider. Thus, we compare the performance of competing models that predict customer potential value. Second, in a managerial context, we provide CRM-managers in multi-service industries with a framework, which can be used to predict customer potential. This framework takes account of the data limitations a company usually has, by using socio-demographic information and transaction information from the customer database solely. The results can then be used as input for customer segmentation, which we will approach more conceptually in Section 2.

The structure of this paper is as follows. In Section 2, we start with a discussion on the potential value of customers and a segmentation based on it. Then we will provide our conceptual framework for customer potential. In Section 3, we describe the methodology and the data requirements for the prediction of customer potential value. In Section 4, we present an application of this methodology in the insurance industry. We also discuss the market segmentation and management implications for this ap plication. Finally, we end with a conclusion, model limitations and directions for future model developments in Section 5.

## 2. Background and model

The first part of this section will be devoted to a discussion on customer potential value and a segmentation method for CRM that uses customer potential value. Next, we will describe the possible antecedents of a customer’s potential value, and we will present our conceptual model.

## 2.1. Potential Õalue

As already mentioned in Section 1, the potential value of a customer refers to the profitability of a customer if that customer buys all purchased products or services from the supplier 12 . Hence, cus-<sup>w</sup> <sup>x</sup> tomer value depends heavily on the number of purchases in the product or service category made by an individual customer 13 . The potential value is com-<sup>w</sup> <sup>x</sup> puted as the total profit margin on all purchases. From a managerial perspective, a customer’s potential profitability is very interesting, since customer specific optimal budgets for relational marketing efforts can be derived from it 3 .<sup>w</sup> <sup>x</sup>

We note that from a CRM-perspective the potential value of a customer reflects not only the current potential, but also the future potential 12 . This is<sup>w</sup> <sup>x</sup> especially true for markets with unstable purchase patterns. Since often no information is available on future purchase patterns, the prediction of this ideal measure of customer potential is difficult. Therefore, we focus on the current potential value of a customer. In our empirical application in the insurance market, purchase patterns are rather stable, so current potential and future potential are strongly linked.

## 2.2. Customer segmentation and customer potential

In CRM, managers develop specific strategies for different segments of their customer base. The customer pyramid is often used as a segmentation method. Using this pyramid, strategies mainly focus on moving promising customers to the top of the pyramid and optimizing revenues from less promising customers by, for example, increasing prices or reducing costs 19 . However, although these strate-<sup>w</sup> <sup>x</sup> gies are useful, using a customer’s current value as segmentation variable solely might lead to sub-optimal strategies. We will illustrate this statement with two examples. First, a customer might belong in the low value segment of the customer pyramid. Hence, companies would strive to optimize revenues by reducing costs that is: lower service levels andŽ marketing expenditures and increasing prices. How-. ever, when considering the potential value of the customer, this might indicate huge cross-selling opportunities, and so a manager should invest in this customer in order to take a larger share of this potential value. Second, again using a customer pyramid, CRM-managers might strive to move customers with a reasonable value into higher tiers of the pyramid. However, these customers might have reached their full potential and no cross-selling opportunities exist. Hence, investments in moving these customers into higher tiers would be wasted. Clearly, a more differentiated approach is needed, which explicitly takes the potential value of a customer into account. Such a differentiation can be derived from a two-by-two segmentation matrix as displayed in Fig. 1. Using this matrix, CRM-managers can formulate better segment specific strategies. Note that this segmentation method can be fine-tuned by distinguishing more groups on each axis. We will briefly discuss the strategies for each segment.

Segment I: Segment I can be regarded as unattractive. It has low potential value and low current value. Therefore, it is expected that future profitability is low. In order to maximize the profitability of this segment, strategies should focus on cost reductions and possibly on price increases i.e., less promo- Ž tions instead of trying to increase the purchase level. .

Segment II: Segment II has high potential value, but the company has not succeeded in taking a large share of this value. Therefore, companies should aim to get a larger part of the customer potential in this segment. Customers in this segment have many opportunities for up-selling activities. Of course, some customers might be more sensitive to such activities than others.

Segment III: Segment III has low potential value and high current value. We are concerned here with relatively loyal customers with low up-selling possibilities. As loyal customers are important for companies 18 , companies should strive to keep these<sup>w</sup> <sup>x</sup> customers. However, up-selling efforts are not likely to be successful.

Segment IV: This segment is the most valuable segment. These customers are loyal and have a large potential value. Losing this group of customers would really harm the company. Management should strive to keep this group of customers using all kinds of relational efforts. This group might, for example, get priority in the service delivery process.

Given the relevance of potential value in CRM, we will continue with a discussion on the antecedents of potential value and a detailed description of our conceptual model.

## 2.3. Antecedents of potential Õalue

In consumer research, consumer needs and the available resources are important drivers of acquisition decisions for products and services 11 . An<sup>w</sup> <sup>x</sup> individual’s needs are affected by factors such as household composition, gender, attitudes e.g. riskŽ attitude and social class 6 . The extent to which. <sup>w</sup> <sup>x</sup> these needs can be satisfied depends on the consumer’s resources. Complete information on needs and resources is hardly ever available, but you could use socio-demographic information relating to tastes, needs, and resources. For example, from research in the financial services industry, it is well known that the family lifecycle is a determinant of the type of services acquired 1 . In addition, Kamakura et al.<sup>w</sup> <sup>x</sup> <sup>w</sup> <sup>x</sup> 14 report that demographic factors, such as income, age, and education, are important determinants in the acquisition of financial services.

To predict the purchasing of different products or services, data on the purchasing of other products or services can also serve as important predictors. For example, Kamakura et al. 14 report strong interde- <sup>w</sup> <sup>x</sup> pendencies between the types of financial services purchased. Although we are not interested in the amount of interdependency, it might be very helpful to use purchase information of other products when predicting purchase decisions. This takes into account the possible information on the interrelationships.

![](/api/attachments/3Z7FKKN8/fulltext/images/7e6ff8fe8754668bc49485a09406e8fb3d3a07441cabf890ae927d756583672c.jpg)  
Fig. 2. Conceptual model underlying DSS.

## 2.4. Conceptual model

The variables that can be used to predict the potential value of a customer in a marketing decision support system depend to a great extent on the availability of data. Spring et al. 21 report that most<sup>w</sup> <sup>x</sup> companies that use a customer database have information on the purchasing behavior of customers at their own company. Often, they also have information on some socio-demographic characteristics. Subjective information on attitudes and lifestyle is typically not available. Therefore, despite the possible effect of this type of variables on the potential value of a customer, these variables, in general, cannot be included in a model for a marketing decision support system. Hence, in our conceptual model, we will consider socio-demographic characteristics and the purchasing behavior at the own company as the determinants of potential value. The conceptual model is displayed in Fig. 2. Note that the information on purchases at the company is also part of the customers potential. We account for this in the estimation strategy.

## 3. Empirical modeling

In this section, we will present the empirical implementation of our conceptual model. We start with a discussion of the data requirements. Next, we will discuss the empirical specification of the models for purchase behavior, for potential value, and a customer base segmentation based on these models.

## 3.1. Data requirements

Information about all of a customer’s product purchases in the company’s markets is needed to derive a customer’s potential value. This information is usually not available, but a survey among customers is an easy way of obtaining this information. Besides complete information on purchase behavior, predictors for these purchase decisions are also needed. From the conceptual model, we concluded that both socio-demographic and actual purchase information at the company can be useful predictors of purchase decisions. Actual purchase information is usually stored in the customer information file CIF .Ž . Some companies also have socio-demographic information in their CIF, but otherwise such information can be obtained from external suppliers, such as CCI.

## 3.2. Estimation procedure

Estimation of potential value can be carried out with models at different levels of aggregation of behavior. A model for purchasing behavior for each product or service uses the data at the lowest level of aggregation. The individual purchases can also be aggregated into an individual specific measure of potential value. This measure of potential value can be modeled with a linear regression model. When interest is restricted to a segmentation of the customer base into a high potential and a low potential segment, the data on potential value can be summarized with the segment memberships of each customer. This can be modeled with a probit model.

The models that use less aggregated information, in general, provide more information about the driving forces of potential value. However, such models do not necessarily result in a better performance in predicting the aggregated variables. A model that is aimed solely at modeling the aggregate variable and not the underlying behavior, such as the probit model for segment membership, might be better.

At each level of aggregation of the data, it would be desirable to use different types of econometric models. At the lowest level of aggregation, the dependent variable is the decision to purchase a certain product or service, which is a binary choice. Usually, a probit model is used to predict the purchases of the various services 10 . However, in many cases, these<sup>w</sup> <sup>x</sup> purchase decisions are made simultaneously, or, at least, they are related. In our empirical application, which deals with the purchases of insurance policies, for example, the unobserved risk attitudes of the customers are likely to result in interdependencies across the decisions to purchase the different insurance policies. For this reason, a multivariate probit model is also estimated. This model allows for correlations between the error terms in the probit equations for each service 5 .<sup>w</sup> <sup>x</sup>

The univariate probit model for purchases ofŽ . product $j , j = 1 , \ldots , J ,$ by customer i is specified as follows.

$$
y _ {i j} ^ {*} = \beta_ {j} X _ {i} + \sum_ {k = 1} ^ {J} \gamma_ {j k} Z _ {i k} + \varepsilon_ {i j},\tag{1}
$$

$$
y _ {i j} = 1 \quad \text { if } y _ {i j} ^ {*} > 0,\tag{2}
$$

$$
y _ {i j} = 0 \quad \text { if } y _ {i j} ^ {*} \leq 0,\tag{3}
$$

where for $i = 1 , \dots N$ and $j = 1 , . . . , J \colon y _ { i j } ^ { \ast } = \mathrm { a n }$ unobserved variable; $y _ { i j } =$ the ownership of product or service j for customer i Ž1 <sup>s</sup> ownership, $0 = { \mathfrak { n } } 0$ ownership survey ; . Ž . X <sup>s</sup>socio-demographic indicators e.g., age, income of customerŽ . Ž i CIF or external ;. $Z _ { i k }$ is the observed ownership of product or service k at company for customer i Ž . CIF and $\varepsilon _ { i j }$ is the error term.

The main assumption underlying the regular probit model is that the errors are independent across individuals, but also across insurance types 10 . The<sup>w</sup> <sup>x</sup> multivariate probit model allows for correlations relating to the purchase decisions for the insurance types. Here, the assumption is that the vector of errors, $\varepsilon _ { i 1 } , \ldots , \varepsilon _ { i J }$ , follows a multivariate normal distribution with an unrestricted covariance matrix <sup>w</sup> <sup>x</sup> 5 . As these correlations result in dependencies relating to the purchase decision for the various services, the multivariate probit model results in probabilities with which a customer purchases a certain portfolio of services.

In our empirical application, both the multivariate probit model with an unrestricted covariance matrix and univariate probits for each type of insurance are used. The models are validated by comparing the hit rate of the models, i.e., the percentage of observations correctly predicted, with the hit rate of a naıve¨ model. The models are tested for predictive accuracy with the test of Franses 8 . The estimation results for<sup>w</sup> <sup>x</sup> the purchase decisions can be used to predict potential value. However, the results can also serve a different purpose. Knowing which customers are more likely to purchase a particular service is also helpful in developing a target selection model for marketing activities for the service concerned.

Using information on the profitability of each product, a customer’s potential value can be predicted with the estimation results of the multivariate probit model. A prediction for the potential value is obtained by multiplying the predicted probability of ownership of each possible service portfolio, by the expected profitability of such a portfolio. Thus, we obtain the following equation to compute the potential value of customer i.

Potential Value<sub>i</sub>

$$
= \sum_ {k = 1} ^ {K} \operatorname{Prob} (\text { customer } i \text { owns   portfolio } k) \operatorname{Profit} _ {k},\tag{4}
$$

where Prob customerŽ . i owns portfolio k <sup>s</sup>the probability of customer i purchasing portfolio k and Profi ${ \bf \Phi } _ { \mathrm { { \bar { \epsilon } } } k } =$ the Profit margin of all services in portfolio $k .$

In the situation without dependence across the different services, this reduces to the more familiar probabilities that result from the traditional probit model

$$
\operatorname{Prob} \left(y _ {i j} = 1\right) = \operatorname{Prob} \left(\varepsilon_ {j i} > - \beta_ {j} X _ {i} - \sum_ {k = 1} ^ {J} \gamma_ {j k} Z _ {i k}\right),\tag{5}
$$

and the following formula for the potential value

$$
\text { Potential   Value } _ {i} = \sum_ {j = 1} ^ {J} \operatorname{Prob} (y _ {i j} = 1) \text { Profit } _ {j}.\tag{6}
$$

The above formulae for predicting the potential value of customer uses detailed information about purchase behavior of the different products. When you are solely interested in a customer’s potential value itself, and not in the services that determine this potential value, a simple regression model can be used to predict the potential value of a customer. Predictions of potential value can then be based on an Ordinary Least Squares estimate of the following regression model

$$
\text { Potential   value } _ {i} = \beta X _ {i} + \sum_ {k = 1} ^ {J} \gamma_ {k} Z _ {k} + \varepsilon_ {i}.\tag{7}
$$

From the resulting estimation results, you can derive which customer characteristics determine potential value, but not how these characteristics influence the purchases of each type of service. Although this insight is lost, the regression model might still be the more appropriate model for predicting potential value as it is designed to model continuous variables.

The models for predicting potential value can be evaluated using well-known criteria like the Mean Absolute Prediction Error MAPE . For comparison,Ž . we also report these measures for the simplest possible prediction of a customer’s potential value, which is the mean potential value in the estimation sample.

When interest is limited to a segmentation of the customer base into a high potential and a low potential segment, a suitable model that can be used is the probit model for segment membership. This method can also be easily generalized for the case with multiple segments with the ordered probit model <sup>w</sup> <sup>x</sup> 10 . The probit model for membership of the high potential value segment is defined as follows, seeŽ also Eqs. 1 – 3Ž . Ž ..

$$
y _ {i} ^ {*} = \beta X _ {i} + \sum_ {k = 1} ^ {J} \gamma_ {k} Z _ {i k} + \varepsilon_ {i},\tag{8}
$$

$$
y _ {i} = 1 \quad \text { if } y _ {i} ^ {*} > 0,\tag{9}
$$

$$
y _ {i} = 0 \quad \text { if } y _ {i} ^ {*} \leq 0.\tag{10}
$$

Here ${ y _ { j } } ^ { * }$ is an unobserved variable, $y _ { i } = 1$ indicates that individual i is in the high potential value segment, while $y _ { i } = 0$ indicates otherwise.

In the empirical application, we use a median split to segment the customer base into two equally sized parts. The estimation results for the probit model for service purchases and the regression model for potential value are also used to segment the customer database into two segments of equal size, at least in the estimation sample.

## 4. Application to the insurance industry

In this section, we present the application of our methodology to an insurance company in the Netherlands. We start with a short description of the data. Then we estimate and evaluate the models for each aspect of behavior we are interested in.

## 4.1. Data

We use data from an insurance company in the Netherlands. This company is a large direct writer and does not use agents. They sell all types of insurance policies, ranging from fire and theft insurances to life insurance. The company aims to have close relationships with their customers and hence possesses a customer database in which information on the purchasing behavior of customers at the company, and some other characteristics, such as age and relationship duration, are stored.

Data on the ownership of different insurance policies were collected by means of a telephone survey among a proportionally stratified sample of about 2300 customers of the insurance company. The bases for stratification are relationship duration, purchase level of insurances and claiming behavior. Using this sampling methodology, we obtain a representative sample on these important characteristics. The survey also includes questions on age, education, household size, income, and home ownership. After deleting cases with missing values, we obtained a final sample of 1612 customers. In line with the profile of customers of this company, our sample can be described as representing rather prosperous and welleducated people. A more detailed description of the sample characteristics is given in Appendix A.

Respondents were asked to indicate whether they had effected 12 types of insurance. To check the reliability of the answers, we compared the reported ownership with the available information from the customer database. It turned out that there was not a single case where ownership was not reported, meaning there were no discrepancies with the customer information file. This indicated that the answers on the ownership questions were reliable.

Table 1 presents ownership rates for each of these 12 insurance types. Because of the confidential nature of our data, we report the insurance types in alphabetical order. The insurance types are: car, damages, disability, funeral, furniture, health, house, liability, legal aid, life, travel, and continuous travel insurance. The reported ownership rates of these insurance types are sorted by ownership rates, so they cannot be linked to the actual insurance types. The numbering introduced here will be used throughout the paper.

## 4.2. Estimation results

For four insurance types, the ownership rates were very close to 100%. To reduce modeling efforts and to save some space, it was assumed that all customers own these four types of insurance. The variation in potential value, we wanted to explain therefore results from the remaining eight types of insurance. In order to capture non-linear effects of the explanatory variables of age, income, and education, we used dummies for the separate classes in our models. The evaluation of the predictions was carried out on a sample that was not used for estimation. We split our sample into an estimation sample with 1000 households. The remaining 612 households were used to validate the models and to evaluate the prediction performance.

Table 1  
Ownership rates for the 12 insurance types Ž . N<sup>s</sup>1612

<table><tr><td>Insurance</td><td>Ownership rate (%)</td><td>Insurance</td><td>Ownership rate (%)</td><td>Insurance</td><td>Ownership rate (%)</td></tr><tr><td>1</td><td>98.7</td><td>5</td><td>88.8</td><td>9</td><td>57.1</td></tr><tr><td>2</td><td>98.0</td><td>6</td><td>71.0</td><td>10</td><td>50.7</td></tr><tr><td>3</td><td>97.6</td><td>7</td><td>65.0</td><td>11</td><td>42.3</td></tr><tr><td>4</td><td>96.3</td><td>8</td><td>63.8</td><td>12</td><td>40.4</td></tr></table>

## 4.3. Prediction of purchases

The prediction results for behavior at the lowest level of aggregation, the purchases of each insurance type, are presented in Table 2. All functions are significant $( p < 0 . 0 5 )$ , except the one for insurance 11 $( p < 0 . 1 0 )$ . We do not report the parameter estimates for the models, but the general conclusion is that socio-demographic variables as well as purchase data from the CIF serve as predictors for ownership. Important socio-demographic predictors are age, income, marital status and the ownership of a house. Besides for the prediction of potential value, the ownership probabilities that result from the probit models can also be used to target direct mail campaigns for an insurance at customers who are more likely to own this insurance.

For each type of insurance, Table 2 presents the fraction of correct predictions in the validation sample for univariate probits, multivariate probit, and for a naıve model that predicts what is most often¨ observed in the estimation sample. The p values in the table correspond to a test of predictive performance, where significant p values imply dependence between realizations and predictions 8 .

From the table, it is clear that for each type of insurance the models predict more than 50% correctly and the p values indicate that there are significant relationships between the predictions and the realizations for most insurance types. For some types of insurance the naıve model outperforms both probit¨ models. However, on average, the hit rates for the probit models are substantially higher, with only a small difference between the two probit models. At first sight, it seems remarkable that the more complicated multivariate probit model does not perform better than the univariate probit model. However, the information about the correlations in the multivariate probit model, that is available through the observed insurance portfolio, is also used in the univariate probit models through the dummies of insurance ownership at the company. This already includes all the information in the data about the possible correlations that is available for prediction.

Table 2  
The fraction of correct predictions for our models and a naive model, with p values from the test of Franses 8<sup>w</sup> <sup>x</sup>

<table><tr><td>Insurance type</td><td>Univariate probit</td><td>Multivariate probit</td><td>Naive model</td></tr><tr><td>5</td><td>0.894 (0.000)</td><td>0.899 (0.000)</td><td>0.892</td></tr><tr><td>6</td><td>0.758 (0.000)</td><td>0.755 (0.000)</td><td>0.733</td></tr><tr><td>7</td><td>0.651 (0.001)</td><td>0.657 (0.000)</td><td>0.658</td></tr><tr><td>8</td><td>0.621 (0.268)</td><td>0.621 (0.224)</td><td>0.635</td></tr><tr><td>9</td><td>0.655 (0.000)</td><td>0.650 (0.000)</td><td>0.547</td></tr><tr><td>10</td><td>0.503 (0.463)</td><td>0.503 (0.411)</td><td>0.464</td></tr><tr><td>11</td><td>0.556 (0.457)</td><td>0.542 (0.721)</td><td>0.577</td></tr><tr><td>12</td><td>0.634 (0.000)</td><td>0.636 (0.000)</td><td>0.570</td></tr></table>

## 4.4. Prediction of potential Õalue

The aim of our paper is not to predict ownership rates, but to estimate potential profitability of the customers and to develop CRM strategies, based on these estimates. From the insurance company, we have information on the average contribution margins of each insurance type. Combining this information with the predicted ownership probabilities of the probit models, each customer’s potential value can be predicted.

Table 3 reports the Mean Absolute Prediction Errors MAPE of the predicted potential valuesŽ . from the multivariate probit model and the regression model.<sup>3</sup> The MAPE of a naıve model that¨ always predicts the mean is also reported for comparison. The MAPE for the three models are all very similar within 0.15% and better than a model with- Ž . out explanatory variables, which is the naıve model ¨ in the table.

The small improvements of our model compared to a naive prediction model for insurance ownership and potential value are to some extent disappointing. From a management perspective, however, the advantage of linking observed characteristics to the observed behavior is that a segmentation of the customer base can be based on the observed characteristics. Such a segmentation can then be used in a decision support system. A segmentation cannot be created with the naive model, as it predicts the same potential value for each customer.

Table 3  
Mean absolute prediction errors MAPE for our models and a naive modelŽ .

<table><tr><td></td><td>Univariate probit</td><td>Multivariate probit</td><td>Regression model</td><td>Naïve model</td></tr><tr><td>MAPE profitability</td><td>19.5%</td><td>19.4%</td><td>19.4%</td><td>20.5%</td></tr></table>

Note: $M A P E = 1 / N \ \textstyle \sum _ { i = 1 } ^ { N } \ ( | Y _ { i } - \hat { Y _ { i } } | ) / ( Y _ { i } ) * 1 0 0 \% .$

## 4.5. Market segmentation and implications

So far, we have discussed the estimation and prediction results for insurance ownership and customer profitability. The remaining question is whether these results can be used to construct a useful segmentation of the customer base.

Our first segmentation is based on potential value only. We distinguish customers with a high and a low potential value using a median split in the estimation sample. This segmentation is often used in marketing practice e.g., heavy users vs. low Ž users 6 . Table 4 presents the average actual poten- . <sup>w</sup> <sup>x</sup> tial value for the high and low potential value segment for each model. Also reported in each cell are the number of customers and the standard deviation of potential profit. For reasons of confidentiality, we have indexed profits, so average profits are 100. The low value segment has, on average, 4–5% lower profit levels, while the high value segment, on average, yields 4% higher profits for the segmentation of the multivariate probit model and the regression model. Surprisingly, the probit model for segment membership does worse in predicting segment membership. This was not expected a priori, as the probit model is specially designed to model binary outcomes. Here, the loss of information due to aggregation becomes visible.

In Section 2, we discussed a segmentation based on customers’ potential value and customer profitability. The results of this segmentation are shown in Table 5 for the customer potential segmentation based on the regression model. The most prominent aspect of the market segmentation for the insurance company under consideration is that it has a large segment of customers with a high potential value, but only a low current value Segment II, top-left in Ž the matrix . Our analysis identifies this segment as a . segment at which one should target up-selling activities, since there are large potential gains in this segment that are not captured by the company. The fact that usually simple and less profitable insurance types are sold by direct writers explains the existence of this large segment.

Table 4  
Actual indexed profitability for different customer segments and the percentage of customers correctly classified

<table><tr><td></td><td></td><td>Probit choice</td><td>Multivariate probit</td><td>Regression model</td><td>Probit segment</td></tr><tr><td rowspan="3">High potential value segment</td><td>Mean</td><td>104.0</td><td>104.0</td><td>104.0</td><td>101.6</td></tr><tr><td>Std. Dev.</td><td>20.1</td><td>19.7</td><td>19.9</td><td>20.3</td></tr><tr><td>N</td><td>311</td><td>308</td><td>318</td><td>326</td></tr><tr><td rowspan="3">Low potential value segment</td><td>Mean</td><td>97.5</td><td>96.0</td><td>95.6</td><td>98.1</td></tr><tr><td>Std. Dev.</td><td>21.4</td><td>21.2</td><td>20.9</td><td>21.3</td></tr><tr><td>N</td><td>301</td><td>304</td><td>294</td><td>286</td></tr><tr><td>% correctly classified</td><td></td><td>53.1%</td><td>54.6%</td><td>55.9%</td><td>51.6%</td></tr></table>

Table 5  
Actual indexed profitability for different customer segments

<table><tr><td rowspan="2"></td><td colspan="4">Current value</td></tr><tr><td colspan="2">Low</td><td colspan="2">High</td></tr><tr><td rowspan="3">High potential value</td><td>Mean</td><td>103.7</td><td>Mean</td><td>106.5</td></tr><tr><td>Std. Dev.</td><td>19.9</td><td>Std. Dev.</td><td>20.2</td></tr><tr><td>N</td><td>183</td><td>N</td><td>135</td></tr><tr><td rowspan="3">Low potential value</td><td>Mean</td><td>94.1</td><td>Mean</td><td>97.9</td></tr><tr><td>Std. Dev.</td><td>21.3</td><td>Std. Dev.</td><td>20.9</td></tr><tr><td>N</td><td>116</td><td>N</td><td>178</td></tr></table>

The information of the customer base segmentation presented in Table 5 can be stored in the CIF. This information can be used to direct customer contacts. For example, in call centers management might give customers in attractive segments priority, e.g., shorter waiting times, in the service delivery process compared to the customers in the less attractive segments.

## 5. Discussion, research limitations and future research

## 5.1. Discussion

Our research mainly focused on the modeling of customer potential value. We discussed and compared different statistical methods to model this value: univariate probit, mulitivariate probit and regression analysis. With respect to the modeling of ownership our models perform somewhat better than the naıve¨ model. However, multivariate probit and univariate probit have similar results. Given these results, it appears more appropriate to use univariate probit, as this technique is easily performed in most statistical packages. This technique does not predict very well, though, as only some specific insurance types could be predicted well with our data. These insurance types, such as legal aid and continuous travel insurances, are typically related to a customer’s socio-demographic characteristics. Ownership of other insurance types with less specific characteristics is more difficult to predict.

With respect to the prediction of potential value, regression analysis appears to have the best predictive power. This is also reflected by the fact that when we predict segment membership that is lowŽ potential value vs. high potential value , regression. analysis also appears to predict better than the other methods.

In general, there is no theoretical reason why one of the models should perform better than the other models. Modeling purchase incidence has the advantage that it provides more insight into the services that drive customer potential value, but it also requires the largest amount of modeling. Models for behavior at higher levels of aggregation require less modeling efforts, but they might suffer from the loss of information due to aggregation. This is the case with the probit model for segment membership in our empirical application. Model validation and comparison of predictive performance is therefore of major importance when deciding on which model to use as input in a decision support system.

## 5.2. Research limitations and future research

Our methodology only considers current potential value, whereas ideally a manager prefers information on current and future potential value of customers. To incorporate future potential value, panel information is needed which was not available. In future research, a longitudinal estimation strategy can be developed. Moreover, as with any segmentation, you can think of finer market segmentations. In addition to the proposed segmentation, you might consider responsiveness to up-selling activities as a third characteristic to include in the segmentation. Finally, our model was developed to predict the value of current customers. Future research can develop models that predict the potential value of new customers.

## Acknowledgements

The authors acknowledge the data support of a Dutch insurance company and helpful comments by Philip Hans Franses and Ernst Verwaal and the two editors of the special issue on CRM.

Appendix A. Sample characteristics ( )N<sup>s</sup>1612

<table><tr><td>Variable</td><td>Mean</td><td>Minimum</td><td>Maximum</td></tr><tr><td>Age</td><td>38.39</td><td>16</td><td>56</td></tr><tr><td>Female</td><td>0.414</td><td>0</td><td>1</td></tr><tr><td>Own house</td><td>0.803</td><td>0</td><td>1</td></tr><tr><td>Own cars</td><td>0.886</td><td>0</td><td>1</td></tr><tr><td>Number of Children</td><td>1.213</td><td>0</td><td>6</td></tr><tr><td>Single</td><td>0.146</td><td>0</td><td>1</td></tr><tr><td>Relationship duration</td><td>6.911</td><td>0</td><td>34</td></tr><tr><td>Education categories</td><td></td><td></td><td></td></tr><tr><td>Low education</td><td>0.105</td><td>0</td><td>1</td></tr><tr><td>Intermediate education</td><td>0.378</td><td>0</td><td>1</td></tr><tr><td>Higher education</td><td>0.518</td><td>0</td><td>1</td></tr><tr><td>Income categories</td><td></td><td></td><td></td></tr><tr><td>Low income</td><td>0.084</td><td>0</td><td>1</td></tr><tr><td>Middle income</td><td>0.330</td><td>0</td><td>1</td></tr><tr><td>High income</td><td>0.213</td><td>0</td><td>1</td></tr><tr><td>Very high income</td><td>0.226</td><td>0</td><td>1</td></tr><tr><td>Income unknown</td><td>0.149</td><td>0</td><td>1</td></tr></table>

## References

<sup>w</sup> <sup>x</sup> 1 G.A. Antonides, W.F. van Raaij, Consumer Behavior A European Perspective. Wiley, Chichester, 1998.

<sup>w</sup> <sup>x</sup> 2 G.R. Bitran, S.V. Mondschein, A comparative analysis of decision making procedures in the catalog sales industry. European Management Journal 15 2 1997 . Ž . Ž .

<sup>w</sup> <sup>x</sup> 3 R.C. Blattberg, J. Deighton, Managing marketing by the customer equity test. Harvard Business Review 75 4 1996 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 4 J.R. Bult, T. Wansbeek, Optimal selection for direct mail. Marketing Science 14 4 1995 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 5 S. Chib, E. Greenberg, Analysis of multivariate probit models. Biometrika 82 2 1998 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 6 J.F. Engel, R.D. Blackwell, P.W. Miniard, Consumer Behavior. The Dryden Press, Forth Worth, 1995.

<sup>w</sup> <sup>x</sup> 7 S. Fournier, S. Dobscha, D.G. Mick, Preventing the premature death of relationship marketing. Harvard Business Review 76 1 1998 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 8 P.H. Franses, A test for the hit rate in binary response models. International Journal of Market Research 42 2Ž . Ž . 2000 .

<sup>w</sup> <sup>x</sup> 9 A.W.H. Grant, L.A. Schlesinger, Realize your customers full profit potential. Harvard Business Review 73 5 1995Ž . Ž . Ž . September–October .

<sup>w</sup> <sup>x</sup> 10 W.H. Greene, Econometric Analysis. 3rd edn., Prentice Hall, New Jersey, 1997.

<sup>w</sup> <sup>x</sup> 11 J.R. Hauser, G.L. Urban, The value priority hypotheses for consumer budget plans. Journal of Consumer Research 12 4Ž . Ž . 1986 .

<sup>w</sup> <sup>x</sup> 12 J.L. Hesket, W.E. Sasser, L.A. Schlesinger, The Service Profit Chain. Free Press, New York, 1997.

<sup>w</sup> <sup>x</sup> 13 J.C. Hoekstra, K.R.E. Huizingh, The lifetime value concept in customer based marketing. Journal of Market Focused Management 3 3Ž . Ž . <sup>r</sup>4 1999 .

<sup>w</sup> <sup>x</sup> 14 W.A. Kamakura, S.N. Ramaswami, R.K. Srivastava, Applying latent trait analysis in the evaluation of prospects for cross-selling of financial services. International Journal of Research in Marketing 8 4 1991 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 15 B.D. Kim, S.O. Kim, Measuring upselling potential of life insurance customers: application of stochastic frontier model. Journal of Interactive Marketing 13 4 1999 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 16 R.M. Morgan, S.D. Hunt, The commitment-trust theory of relationship marketing. Journal of Marketing 58 3 1994Ž . Ž . Ž . July .

<sup>w</sup> <sup>x</sup> 17 D. Peppers, M. Rogers, The One to One Manager: Real-World Lessons in Customer Relationship Management. Doubleday, New York, 1999.

<sup>w</sup> <sup>x</sup> 18 F.F. Reichheld, Loyalty Based Management. Harvard Business School Press, Boston, 1996.

<sup>w</sup> <sup>x</sup> 19 R.T. Rust, V.A. Zeithaml, K. Lemon, Driving Customer Equity: How Customer Lifetime Value is Reshaping Corporate Strategy. The Free Press, New York, 2000.

<sup>w</sup> <sup>x</sup> 20 D.C. Schmittlein, R.A. Peterson, Customer base analysis: an industrial purchase process Application. Marketing Science 13 1 1994 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 21 P.N. Spring, P.C. Verhoef, J.C. Hoekstra, P.S.H. Leeflang, The Commercial Use of Segmentation and Predictive Modeling Techniques for Database Marketing, Working Paper, University of Groningen, 2000.

<sup>w</sup> <sup>x</sup> 22 V.A. Zeithaml, Service quality, profitability and the economic worth of customers. Journal of the Academy of Marketing Science 28 1 2000 . Ž . Ž .

![](/api/attachments/3Z7FKKN8/fulltext/images/f96289463f0f54a62fcf8da7c187d2cfa32655502de030b21d50e6070cbbaa5b.jpg)

Peter C. Verhoef received his Ph.D. from Erasmus University Rotterdam in 2001. He currently has a post doc position at the Department of Marketing and Organization at the School of Economics at that same university. In his disseration, he has investigated determinants of the value of a customer. His other research interests include electronic commerce, waiting times and private labels. His work has been published in the Journal of Retailing, European Journal of Mar-

keting, Journal of Market Focused Management and the Journal of Retailing and Consumer Services.

![](/api/attachments/3Z7FKKN8/fulltext/images/23671e6ffc84bcd7645f3ed83fe3caa69baf215142ddc2613de4af2b615548f3.jpg)

Bas Donkers received his PhD from Tilburg University in 2000. He currently has a post doc position at the Erasmus University Rotterdam. His research interests are in the modeling of individual decision making and, more general, the area of applied econometrics. His work has been published in the Journal of Risk and Uncertainty, Journal of Economic Psychology and Review of Income and Wealth.
