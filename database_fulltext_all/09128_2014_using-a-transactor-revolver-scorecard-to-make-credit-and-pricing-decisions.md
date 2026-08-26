---
otero_id: 9128
otero_key: "PWC6C8AT"
title: "Using a transactor/revolver scorecard to make credit and pricing decisions"
authors: "Mee Chi So; Lyn C. Thomas; Hsin-Vonn Seow; Christophe Mues"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.11.002"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Mee Chi So <sup>a,</sup>⁎, Lyn C. Thomas <sup>a</sup>, Hsin-Vonn Seow <sup>b</sup>, Christophe Mues <sup>a</sup>

<sup>a</sup> Southampton Management School, University of Southampton, Southampton SO17 1BJ, United Kingdom

<sup>b</sup> Nottingham University Business School Malaysia, University of Nottingham Malaysia Campus, Jalan Broga, 43500 Semenyih, Selangor Darul Ehsan, Malaysia

## a r t i c l e i n f o

Article history: Received 14 March 2013 Received in revised form 8 October 2013 Accepted 8 November 2013 Available online 16 November 2013

Keywords: Pricing Risk decision analysis Credit scoring

## a b s t r a c t

In consumer lending the traditional approach is to develop a credit scorecard which ranks borrowers according to their risk of defaulting. Bads have a high risk of default and Goods have a low risk. To maximise the pro<sup>fi</sup>tability of credit card customers, a second classi<sup>fi</sup>cation between revolvers and transactors becomes important. Building a transactor/revolver scorecard together with a Good/Bad scorecard over the revolvers, gives rise to a risk decision system whose ranking of risk is comparable with the standard approach. The paper develops a pro<sup>fi</sup>tability model of card users including the transactor/revolver score leads. This gives more accurate pro<sup>fi</sup>tability estimates than models which ignore the transactor/revolver split

© 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

For many years credit card organisations have split users into transactors and revolvers [8]. Transactors are credit card users who pay off their balance every month and so incur no interest charges. Revolvers are credit card users who do, occasionally or regularly, pay off only part of their monthly balance and so do incur interest charges. Credit card companies currently do not attempt to make this distinction when initially deciding whether to give an applicant a credit card. Instead they estimate the probability the applicant will be Bad — i.e. default or be written off within a given period, usually 12 months. Applicants who are not Bad are considered Good. Lenders develop application scorecards which estimate the probability of the applicant being Good.

The transactor/revolver split affects these Good/Bad estimates because if a transactor pays the balance off every month for a period which is longer than the performance period in the Good/Bad de<sup>fi</sup>nition then all transactors must be Goods. Thus transactor/revolver is a useful segmentation of the population in terms of default risk. In terms of pro<sup>fi</sup>tability the transactor/revolver split is even more important. Transactors do not produce any income to the lender from the interest charged on the card. On the other hand, transactors tend to use their card to fund more expensive purchases than revolvers. Thus for pricing decisions a transactor/revolver scorecard will improve the underlying pro<sup>fi</sup>tability model.

This paper proposes that lenders develop a transactor/revolver score as well as a Good/Bad score to aid their decision on what “price” or interest rate to charge and which applicants to accept for a card. We show how such a transactor/revolver score can be built using logistic regression by applying it to a real credit card data set. Using such a score together with a Good/Bad score based on the revolver segment of the population produces a risk assessment system that compares well with the standard approach of building a Good/Bad scorecard on the whole population.

We also build a pro<sup>fi</sup>tability model for the portfolio of potential credit card applicants. This model includes the chance that the applicants will take the credit card offered and this take probability depends on the interest rate charged on the card and on the riskiness of the applicants. The pro<sup>fi</sup>tability model is applied both with and without a transactor/ revolver score available. We compare the outcomes of these two models on the same numerical example. The results show how much more sophisticated the accept/reject policy is when the transactor/ revolver score is available compared with when it is not available. Moreover the resultant model is more representative of the real situation because the model without a transactor/revolver score overestimates the pro<sup>fi</sup>ts by assuming that all transactors take a long time to pay off their balances. Thus the pricing decision of what interest rate to charge is more robust if the underlying model has a transactor/ revolver score.

The standard approach to building scorecards [1] involves univariate analysis and stepwise regression to identify the borrower characteristics that most impact on the borrower's subsequent Good/Bad status. The important characteristics are then modi<sup>fi</sup>ed using coarse classi<sup>fi</sup>cation. Over the last twenty years, numerous regression, mathematical programming or machine learning techniques have been used by researchers in the <sup>fi</sup>nal step of combining the characteristics into a scorecard that estimate default risk [12,14,17]. In practice, logistic regression is still the most popular techniques [23]. Since the focus of this paper is to propose a new mechanism for making credit and pricing decision but not to benchmark the performance of various techniques, we build all the scorecards using logistic regression.

References to transactors and revolvers are common in the <sup>fi</sup>nancial press but less so in the academic literature. Field and Walker [8] outlined the difference between revolver and transactor. They and other writers commented on the lack of precision in the de<sup>fi</sup>nition of transactor. Over what period should a borrower repay fully every month the balance on his credit card to be deemed a transactor? More recently the <sup>fi</sup>nancial press has looked at whether lenders are favouring transactors [6] or revolvers [4]. The Federal Reserve Bank of Philadelphia [11] studied the characteristics of revolvers and transactors and not surprisingly found transactors to be older and richer than revolvers.

Kim and DeVaney [15] looked at who had credit cards and then among credit card holders what were the characteristics of revolvers and transactors. They applied a Heckman two stage model to identify the important characteristics. The data were taken from the 1998 Survey of Consumer Finances and so many of the important variables were ones that are not available to credit card lenders. These included the amount of liquid and investment assets, the attitudes of the borrowers to using credit for different expenses, and their income expectations. Our transactor/revolver scorecard uses the information normally supplied on a credit card application form or held by a credit bureau. So and Thomas [20] examined the different ways changes in economic conditions affected the default risk of revolvers and transactors. For example the default risk of revolvers reacts much more to changes in the unemployment rate than that of transactors.

Zinman [24] built a neoclassical choice model to explain why some consumers use debit cards while others act as credit card transactors. Initially it would appear the latter is a much more rational choice than the former because of the interest free period that it allows. The paper looks at reasons why it might be rational for a consumer to prefer the former to the latter. Further work on this problem was undertaken by Sprenger and Stavins [21]. Using data from the 2004 Survey of Consumer Finance, they showed that credit card revolvers are more likely to using debit cards if they can.

There is a literature on modelling credit card pro<sup>fi</sup>tability, but with one exception, the models do not involve the transactor/revolver split. The papers split into ones which model the cash <sup>fl</sup>ow between a credit card user and the lender and those which use a sample of credit card users to estimate the relationship between spend or pro<sup>fi</sup>t over a given period and the characteristics of the users and their behaviour.

In the <sup>fi</sup>rst camp, Hussain [13] is the only paper which includes the transactor/revolver split in its model. It includes pro<sup>fi</sup>t from interest payments, merchant service charges, and a <sup>fi</sup>xed fee. However, it assumes that revolvers repay the cost of a purchase over an infinite number of periods and sets the cost of default as a <sup>fi</sup>xed amount for each user. Moreover the model is applied only at the portfolio level. Our model starts at the individual user level and so allows analysis of the optimal accept/reject initial decision on each potential applicant. Oliver and Oliver [16] introduced the take probability of whether a potential used will accept the credit card given the rate of interest offered. This is also a feature of our cmodel, but the cost structure of the Oliver model is of a one-off loan rather than a credit card.

The second stream of papers models the pro<sup>fi</sup>t and the spending using data from a card portfolio. Stewart [22] assumes spend is a function of risk grade and that the pro<sup>fi</sup>t depends on spend and default risk. A spend model is built for each default risk band. Singh et al. [19] use a DEA (Dynamic Envelopment Analysis) approach where the outputs are the revenues from the interest rate charged, the merchant service charge and the <sup>fi</sup>xed fees. The mean and variance of the <sup>fi</sup>xed fees is considerably smaller than the other two sources of income.

Finlay [9] and Andreeva et al. [2] estimate credit card pro<sup>fi</sup>tability by <sup>fi</sup>rst estimating two other quantities and then combining them in a profit formula. Finlay [9] builds a regression model where the dependent variable is a combination of the average payments made in a period and the balance of the account when in arrears. This is compared with a standard default risk based scorecard based. The former gives more accurate rankings in terms of the actual pro<sup>fi</sup>ts than the latter. This approach of estimating the individual aspects of pro<sup>fi</sup>tability before combining them in a pro<sup>fi</sup>t formula was expanded further in Finlay [10]. In that paper the default probability, the bad debt levels and the revenue are estimated using genetic algorithms and neural nets as well as logistic regression. These are combined in a pro<sup>fi</sup>tability formula and the results compared with those from using the standard default risk scorecards. Andreeva et al. [2] looked at a sample of a retailer's credit card accounts. They used the proportional hazards models to estimate the time to default and the time to the next purchase in terms of the user characteristics. The net present value of revenue was then estimated using regression based on the estimates of these two times. Not surprisingly this proved to give a more accurate ranking than that based on a default risk scorecard.

The book by Phillips [18] and the book chapter by Cau<sup>fi</sup>eld [5] describe the current position of credit cards pricing both theoretically and at a practical level. The “price” of credit cards is essentially the interest rate charged, though it could involve the <sup>fi</sup>xed fees if they are charged. Neither Phillips [18] nor Cau<sup>fi</sup>eld [5] refers to credit card models which involve a transactor/revolver split.

The pro<sup>fi</sup>tability model we propose assumes the lender thinks of a revolver as paying off debts in the order they are incurred. The lender <sup>fi</sup>rst sets any payment to repay the oldest debt, and then the second oldest debt and so on until the payment is used up. This is exactly the ordering that credit card companies use when dealing with balance transfer to a new credit card. They set the payments against the balance transferred before using them to pay off the new purchases on the credit card. This approach implies revolvers pay off the interest caused by a speci<sup>fi</sup>c purchase after a few periods provided they have not defaulted in the meantime. Any other assumption would be equivalent to a borrower paying off the interest on a purchase which they have already paid for. Other models in the literature either assume the interest is paid inde<sup>fi</sup>nitely or ignore the interest. Both approaches are unrealistic. Our model also includes the take probability which is how likely applicants will accept the credit card offer made. This is important when considering what optimal interest rate to charge. We will show the pro<sup>fi</sup>tability for a few interest rates and we concentrate on <sup>fi</sup>nding the most pro<sup>fi</sup>table cut-off score on the Good/Bad scorecard under these different interest rates. This allows us to <sup>fi</sup>nd the optimal interest rate to charge.

In the next section, we build a Good/Bad scorecard on a credit card data set from Hong Kong. This will be used as a comparator for the approach to default risk using the transactor/revolver scorecard. In Section 3, we build a transactor/revolver scorecard on the same data set. In Section 4 we develop a Good/Bad scorecard built only on revolvers. This together with the transactor/revolver scorecard produces a risk assessment system. We compare this risk assessment system with the standard approach of Section 2. In Section 5, we describe the credit card pro<sup>fi</sup>tability model when we do not distinguish between transactors and revolvers. We derive the cut-off score that maximises pro<sup>fi</sup>tability and apply the model to a numerical example. Although there is no analytic expression for the optimal interest rate to charge we can <sup>fi</sup>nd this by calculating the pro<sup>fi</sup>tability for different interest rates. In Section 6 we extend the pro<sup>fi</sup>tability model to the case where a transactor/revolver score is available. We again <sup>fi</sup>nd the Good/Bad cut-off strategy which maximises the pro<sup>fi</sup>tability of the portfolio. This is more complicated since the cut-off score is a function of the transactor score. We apply this model to a numerical example which reduces to the numerical example in Section 5 if the transactor/revolver split is ignored. Finally in Section 7 we draw some conclusions from our analysis and some areas for future research concerning the use of transactor/ revolver scorecards.

## 2. Building Good/Bad scorecards

The traditional approach in credit scoring is to build an application scorecard which estimates the probability of an applicant not defaulting within a given time period. The lender chooses a suitable time period, usually one year, and classi<sup>fi</sup>es all those who default or otherwise perform unsatisfactorily in that period as Bads (B). The remaining applicants are classi<sup>fi</sup>ed as Goods (G). A classi<sup>fi</sup>cation technique like logistic regression is then used to relate the characteristics, x, of the applicant to their subsequent Good/Bad status. With logistic regression, the resulting score s(x) is a log odds score where

Table 1 List of variables used in the analysis.

<table><tr><td>Variables</td><td>Details</td></tr><tr><td>Occupation</td><td>C1 (7.4%), C2 (6.8%), C3 (3.7%), C4 (4.3%), C5 (7.9%), C6 (57.6%), unknown (12.3%)</td></tr><tr><td>Education type</td><td>Primary (1.7%), secondary (27.4%), tertiary (9.6%), postgraduate (13.9%), unknown (47.4%)</td></tr><tr><td>Citizenship</td><td>Yes (67.2%), no (26.2%), unknown (6.6%)</td></tr><tr><td>Residential type</td><td>Rent private (6.8%), rent public (5.1%), mortgage (9.9%), owned (10.4%), living with parents (16.0%), company housing (2.2%), others/unknown (49.7%)</td></tr><tr><td>Employment status</td><td>Part-time (0.2%), full-time (85%), housewife (3.5%), retired (1%), Self-employed (2.8%), student (1.7%), others/unknown (6.2%)</td></tr><tr><td>Annual income</td><td>Annual income at application (in HK$1000)</td></tr><tr><td>Months with bank</td><td>Total number of months with the lender at application</td></tr><tr><td>Age</td><td>Card holder&#x27;s age at application</td></tr></table>

$$
s _ {0} (\boldsymbol {x}) = \ln \left(\frac {P (G | \boldsymbol {x})}{P (B | \boldsymbol {x})}\right).\tag{1}
$$

We now apply this to real data to compare the discrimination of this system with one that involves building a transactor/revolver scorecard.

## 2.1. Model 1: a standard scorecard

We used credit card data from a major Hong Kong <sup>fi</sup>nancial institution to conduct the analysis. Accounts opened on or after January 1st, 2002 and before January 1st, 2005 were selected for this analysis. Bads are de-<sup>fi</sup>ned as those who defaulted or were written off by the lender between January 1st and December 31st, 2006. There were 1577 such defaulted accounts. There were 4731 non-default accounts (Goods) from the same period. Table 1 shows the list of variables<sup>1</sup> used in this study.

We examined the weight of evidence to assess the relative default risk of various attributes for all categorical variables (the <sup>fi</sup>rst <sup>fi</sup>ve variables listed in Table 1). For continuous variables, we split the variable into a large number of intervals. We use weight of evidence to coarseclassify these variables into bins with similar default risk by combining adjacent intervals where appropriate [1]. Finally the overall coef<sup>fi</sup>cients were obtained using logistic regression with characteristics entering and leaving the scorecard in a stepwise fashion. We use ten-fold cross validation to obtain unbiased results. We split the dataset into deciles and applied cross validation, by repeatedly leaving out one decile to test the results and building a scorecard on the remaining nine deciles.

The average regression coef<sup>fi</sup>cients of all ten scorecards and the corresponding standard deviation for the standard scorecard are presented in Table 2. Annual Income was not selected by the stepwise logistic regression in any of the cases. In all ten runs, the coef<sup>fi</sup>cients of Age were small and negative which is counter-intuitive and thus it was removed from the model. Employment Status was chosen in only three of the models and in the others was less signi<sup>fi</sup>cant than the other characteristics. In calculating the mean and standard deviation, we assume the coef<sup>fi</sup>cient of Employment Status for the rest of the seven scorecards to equal zero. This explains the high standard deviation for the coef<sup>fi</sup>cient of Employment Status.

Testing the scorecard on the ten holdout datasets gives an average Gini coef<sup>fi</sup>cient of 0.522, as shown in the last row of Table 3. Such a value suggests this is a fairly good application scorecard as application scorecards are considered acceptable if they have Gini coef<sup>fi</sup>cients of 0.5 or more [3].

## 3. Building a transactor/revolver scorecard

There have been few attempts to systematically predict in advance which applicants are likely to be transactors (T) and which are likely to be revolvers (R). One can de<sup>fi</sup>ne a transactor as someone who pays off their balance every month during the performance period. Those who are not transactors are revolvers. One way of predicting who is a transactor is to build a transactor/revolver scorecard in the same way as a Good/Bad scorecard was built in the previous section. This will lead to a log odds score which determines the probability of someone being a transactor in terms of their application characteristics x. This score s (x) satis<sup>fi</sup>es

$$
s _ {t} (\boldsymbol {x}) = \ln \left(\frac {P (T | \boldsymbol {x})}{P (R | \boldsymbol {x})}\right) \Rightarrow P (T | \boldsymbol {x}) = \frac {1}{1 + e ^ {- s _ {t} (\boldsymbol {x})}} \text {   and   } P (R | \boldsymbol {x}) = \frac {1}{1 + e ^ {s _ {t} (\boldsymbol {x})}}.\tag{2}
$$

In fact, to keep the expressions relatively straightforward we will use $t ( x ) = P ( T | \mathbf { x } )$ rather than the transactor score, $s _ { t } ( \mathbf { x } )$ . It is obvious from (2) that we can interchange them at will.

## 3.1. Model 2: a transactor/revolver scorecard

Using the same set of data as that in Model 1, we built a transactor/ revolver scorecard where we take the de<sup>fi</sup>nition of a transactor to be a card holder who pays off the balance for at least 12 months before the sampling time, provided that the card holder has at least one year history, or pays the balance off every period of their history if this is less than 12 months. The distribution of transactor–revolver and Good–Bad customers on the whole data set is shown in Table 4. In this dataset, revolvers (53%) are slightly more common than transactors (47%).

The result for this transactor–revolver scorecard is shown in the second column of Table 2. In this model (Model 2), the variable “Age” and “Annual Income” are included in this scorecard. Herbst-Murphy [11] found “Age” to be a variable whose values were signi<sup>fi</sup>cantly different between transactors and revolvers. All the other characteristics were also signi<sup>fi</sup>cant in the transactor/revolver scorecard. The average Gini for the transactor/revolver scorecard is lower than those of Model 1. However, there is no benchmark to evaluate the performance of this type of scorecard and it will be used in conjunction with a Good/Bad scorecard on the revolvers.

## 4. Risk assessment system using a transactor/revolve scorecard

Since transactors pay off all their balance each period, they cannot default and so all transactors must be Goods. We can then use this to build a new estimate of the risk of default. What is then needed is a Good/Bad score restricted to the revolvers. De<sup>fi</sup>ne this as

$$
\begin{array}{l} s _ {R} (\boldsymbol {x}) = \ln \left(\frac {P (G | \boldsymbol {x} , R)}{P (B | \boldsymbol {x} , R)}\right) \Rightarrow P (G | \boldsymbol {x}, R) = \frac {1}{1 + e ^ {- s _ {R} (\boldsymbol {x})}} \text { and } P (B | \boldsymbol {x}, R) \\ = \frac {1}{1 + e ^ {s _ {R} (\boldsymbol {x})}}. \end{array}\tag{3}
$$

## 4.1. Model 3: a Good/Bad scorecard restricted to revolvers

We then develop this Good/Bad scorecard restricted only to revolvers in the same way as the previous scorecards. The average and standard deviation of the coef<sup>fi</sup>cients are shown in Model 3 of Table 2. As on Model 1, the coef<sup>fi</sup>cients of Age in all ten run were negative and thus it was removed from Model 3. The result also shows that, for revolvers, Annual Income and Employment Status are no longer significant when predicting Good/Bad as they were not picked up by the stepwise models. The discrimination of this scorecard (an average Gini coef<sup>fi</sup>cient of 0.519) is slightly less than that of the Good/Bad scorecard on the full data set (Gini coef<sup>fi</sup>cient 0.522). This is not surprising because the transactors who are the easy cases to recognise as Good have been removed in building this scorecard.

Table 2  
Statistical results for different models (Note that all variables are encoded using weight-of-evidence).

<table><tr><td rowspan="2">Variable (WoE)</td><td colspan="2">Model 1 (Event = good)</td><td colspan="2">Model 2 (Event = transactor)</td><td colspan="2">Model 3 (Event = good)</td></tr><tr><td>Coefficient (Mean)</td><td>Coefficient (S.D.)</td><td>Coefficient (Mean)</td><td>Coefficient (S.D.)</td><td>Coefficient (Mean)</td><td>Coefficient (S.D.)</td></tr><tr><td>Intercept</td><td>1.3929***</td><td>0.0072</td><td>-0.1254**</td><td>0.0053</td><td>0.4291***</td><td>0.0125</td></tr><tr><td>Occupation</td><td>0.7796***</td><td>0.0292</td><td>0.5994***</td><td>0.0209</td><td>0.5287***</td><td>0.0328</td></tr><tr><td>Education type</td><td>1.3961***</td><td>0.0678</td><td>0.4701**</td><td>0.0556</td><td>1.4056***</td><td>0.0745</td></tr><tr><td>Citizenship</td><td>1.2286***</td><td>0.0743</td><td>0.9286***</td><td>0.0255</td><td>0.8748**</td><td>0.0850</td></tr><tr><td>Residential type</td><td>1.1147***</td><td>0.0578</td><td>0.6864***</td><td>0.0391</td><td>0.7486***</td><td>0.0707</td></tr><tr><td>Employment status</td><td>0.1146**a</td><td>0.1848</td><td>0.3951**</td><td>0.0430*</td><td>-</td><td>-</td></tr><tr><td>Months with bank</td><td>1.1741***</td><td>0.0187</td><td>0.7998***</td><td>0.0209</td><td>0.8240***</td><td>0.0259</td></tr><tr><td>Annual income</td><td>-</td><td>-</td><td>0.2150**</td><td>0.0290</td><td>-</td><td>-</td></tr><tr><td>Age</td><td>-</td><td>-</td><td>0.2660**</td><td>0.0291</td><td>-</td><td>-</td></tr></table>

⁎⁎⁎ Signi<sup>fi</sup>cant at 0.0001.  
⁎⁎ Signi<sup>fi</sup>cant at 0.05.  
\* Signi<sup>fi</sup>cant at 0.1.  
a Selected by three models only. For models do not pick up the variable, we assume the coef<sup>fi</sup>cients equal 0.

4.2. Model 4: the risk assessment system based on the transactor/revolver scorecard

With these two scores – transactor/revolver and Good/Bad restricted to revolvers – we can now estimate the chance of an applicant being Good. The point is that no transactor can default. One can then create a “score” which gives the probability the new customer is likely to be Good as follows

$$
P (G | \boldsymbol {x}) = P (T | \boldsymbol {x}) + P (R | \boldsymbol {x}) P (G | \boldsymbol {x}, R).
$$

Table 3  
Cross-validation results.

<table><tr><td rowspan="2"></td><td colspan="4">Gini coefficient</td><td rowspan="2">ROC contrast test results between Model 1 and Model 4</td></tr><tr><td>Model 1</td><td>Model 2</td><td>Model 3</td><td>Model 4</td></tr><tr><td>Validation 1</td><td>0.592</td><td>0.45</td><td>0.596</td><td>0.592</td><td>0.039(0.8434)</td></tr><tr><td>Validation 2</td><td>0.47</td><td>0.394</td><td>0.47</td><td>0.474</td><td>0.5008(0.4791)</td></tr><tr><td>Validation 3</td><td>0.556</td><td>0.45</td><td>0.542</td><td>0.558</td><td>0.0488(0.8251)</td></tr><tr><td>Validation 4</td><td>0.52</td><td>0.42</td><td>0.518</td><td>0.511</td><td>2.1165(0.1457)</td></tr><tr><td>Validation 5</td><td>0.482</td><td>0.426</td><td>0.486</td><td>0.48</td><td>0.0789(0.7788)</td></tr><tr><td>Validation 6</td><td>0.526</td><td>0.4</td><td>0.53</td><td>0.53</td><td>0.3427(0.5583)</td></tr><tr><td>Validation 7</td><td>0.512</td><td>0.428</td><td>0.506</td><td>0.508</td><td>0.9092(0.3403)</td></tr><tr><td>Validation 8</td><td>0.524</td><td>0.44</td><td>0.522</td><td>0.532</td><td>0.057(0.8114)</td></tr><tr><td>Validation 9</td><td>0.548</td><td>0.432</td><td>0.54</td><td>0.542</td><td>0.8449(0.358)</td></tr><tr><td>Validation 10</td><td>0.484</td><td>0.47</td><td>0.48</td><td>0.49</td><td>1.2506(0.2634)</td></tr><tr><td>Average</td><td>0.522</td><td>0.431</td><td>0.519</td><td>0.522</td><td></td></tr></table>

## Table 4

Distribution of transactors and revolvers in the sample dataset

<table><tr><td></td><td>Good</td><td>Bad</td><td>Total</td></tr><tr><td rowspan="2">Transactor (count and column %)</td><td>2958</td><td>0</td><td>2958</td></tr><tr><td>62.5%</td><td>0%</td><td>46.9%</td></tr><tr><td rowspan="2">Revolver (count and column %)</td><td>1773</td><td>1577</td><td>3350</td></tr><tr><td>37.5%</td><td>100%</td><td>53.1%</td></tr><tr><td>Total (count)</td><td>4731</td><td>1577</td><td>6308</td></tr></table>

Substituting (2) and (3) into the equation, we have

$$
P (G | \boldsymbol {x}) = \frac {1}{1 + e ^ {- s _ {t} (\boldsymbol {x})}} + \frac {1}{1 + e ^ {s _ {t} (\boldsymbol {x})}} \frac {1}{1 + e ^ {- s _ {R} (\boldsymbol {x})}}.\tag{4}
$$

This gives an ordering of the applicants and so we can compare the results with the ordering under the original s (x) scorecard. The results are shown as Model 4 in Table 2. The average Gini coef<sup>fi</sup>cients of 0.522 mean it gives reasonable discrimination and is exactly the same as that of Model 1. We have compared Model 1 and Model 4 using the DeLong, DeLong and Clarke–Pearson test [7], as shown in the last column of Table 3. This shows that the difference in their Gini coef<sup>fi</sup>cients is not statistically signi<sup>fi</sup>cant in all ten scorecards. Fig. 1 shows the Receiver Operating Characteristic (ROC) curves<sup>2</sup> for Model 1 and Model 4 when applied to Validation 1 and Validation 4. Not surprisingly the ROC curves are almost the same for the two models.

## 5. Credit card pro<sup>fi</sup>tability model

The two main revenue streams from a credit card are the merchant service charge, and the interest charged on the card balance. The former is a fraction of the value of the purchases made. The latter is charged if the balance is not paid off fully within a given time after the monthly statement being sent. Some cards have other revenue streams, such as an annual fee which may be charged on each card or payment protection which is a monthly fee to cover the premium for an insurance to cover the outstanding balance on the card if the card holder becomes unemployed. However, fees tend to be charged by a minority of cards while payment protection has led to mis-selling scandals and so is now discouraged. Our model only has interchange fees and interest on the balance.

The interchange fee paid is a fraction m of the value of the purchases made using the credit cards. On most cards the time between the purchase and the time when its payment is <sup>fi</sup>rst due is interest free. Thereafter, if the balance is not paid off completely, interest will be charged at a rate of r per billing period (which is usually a month). For simplicity, we take that <sup>fi</sup>rst interest free period also to be one month. We assume the risk free rate for borrowing money by the credit card company is r per month. This is also the rate at which future payments are discounted.

To calculate the expected pro<sup>fi</sup>t on a purchase of a \$1, we look at the income stream and the costs that this \$1 brings to the lender. To do this, we de<sup>fi</sup>ne N to be the average number of periods before the \$1 is paid off where the assumption is that at each repayment the oldest debt is paid off <sup>fi</sup>rst, then the next oldest debt and so on. De<sup>fi</sup>ne

![](/api/attachments/PWC6C8AT/fulltext/images/6114717c8de0685d6dce08dec64e395e266371ef711e5a6d9d776702cb2e49b0.jpg)  
Fig. 1. The average balance, average repayment and average cost.

$$
\begin{array}{l l} B & \text { average   balance   carried   over   per   period   per   customer } \\ P & \text { average   amount   purchased   per   period   per   customer } \\ C & \text { average   repayment   amount   per   period   per   customer. } \end{array}
$$

Since in the long run the balance on a card must remain <sup>fi</sup>nite, we can assume the average expenditure plus the interest paid each month must equal the average repayment, namely

$$
r B + P = C.\tag{5}
$$

Moreover, if the customer makes a purchase of P in a period, we assume the user pays off the costs in the order they are incurred. So the customer must pay-off $( 1 + r ) B$ before the cost of the purchase P is repaid. This implies the user pays off the balance at the start of the month of the purchase and then the interest on the balance for that month before paying off the purchase (it is as if the purchase is made at the end of the month). See Fig. 1 for an illustration. Thus

$$
(1 + r) B + P = C N.\tag{6}
$$

So the cost of a purchase stays in the balance for N months. The <sup>fi</sup>rst of these periods is interest free and an interest rate r is charges on the remaining N − 1 periods.

The credit score for a credit card user on an unsegmented population can, under assumptions of stationarity, be translated into a hazard probability p that the user will not default in any given period given that they have not defaulted in the previous periods. This means the chance the card user will not default during N periods is $p ^ { N } .$ If the credit card user defaults, the loss given default – the fraction of the balance that will eventually be lost at the end of the recovery process – is $l _ { D } .$ Thus the expected pro<sup>fi</sup>t from the P of purchases using the card in a period is calculated as follows. In the period of the purchase one subtracts the cost of the purchase but adds on the merchant service charge. Then one has the repayment of the P plus the interest accrued on it over N period provided the borrower has not defaulted. If the borrower defaults during those N periods then the repayment is the percentage of the defaulted amount that is recovered subsequently. Using the standard de<sup>fi</sup>nition of loss given default, we will assume this percentage recovered on the defaulted amount is assumed to have occurred after the N periods. The expected pro<sup>fi</sup>t on one month's purchase using the credit card is e(r,p), where r is the interest rate per period of the credit card and p is the stationary hazard rate of the borrower not defaulting in the next period (staying Good) given that he has not defaulted so far. Then

$$
\begin{array}{l} e (r, p) = P \left((m - 1) + \frac {(1 + r) ^ {N - 1} p ^ {N}}{(1 + r _ {F}) ^ {N}} + \frac {(1 - l _ {D}) (1 + r) ^ {N - 1} (1 - p ^ {N})}{(1 + r _ {F}) ^ {N}}\right) \\ = P (m - 1) + P (1 + r) ^ {N - 1} d (p) \text {where} d (p) = \frac {(1 - l _ {D} + l _ {D} p ^ {N})}{(1 + r _ {F}) ^ {N}}. \end{array}\tag{7}
$$

The <sup>fi</sup>rst term is the cost of purchase less merchant service charge; the second term is the value of the repayment if the user has not defaulted in the N periods before the purchase is repaid and the third term is the repayment via the collection process if the user has defaulted before the purchase is repaid.

The interest charged on the credit card affects the probability that the borrower will take the credit card in the <sup>fi</sup>rst place. So it is more sensible to look at the expected monthly pro<sup>fi</sup>t averaged over every potential card user including those who refused the credit card when it was offered. Assume that the take function q(r,p) is the probability that a potential borrower whose credit score leads to a hazard rate p of being Good will take a credit card and the interest rate offered is r, then the potential pro<sup>fi</sup>t for this borrower is $q ( r , p ) e ( r , p )$

In order to optimise the pro<sup>fi</sup>t a lender can make from a credit card portfolio, we must also estimate the Good–Bad distribution among the potential card owner population. Take the distribution of the Good hazard rates to be $f ( p ) , 0 \leq p \leq 1$ , then the expected pro<sup>fi</sup>t each month from the credit card spend by those in the prospective credit card portfolio is E(r), where

$$
E (r) = \int_ {0} ^ {1} \max \{e (r, p), 0 \} q (r, p) f (p) d p.\tag{8}
$$

The maximum function (i.e. max $\{ e ( r , p ) , 0 \} )$ re<sup>fl</sup>ects the fact that the lender needs not offer the card to those consumers from whom there is no pro<sup>fi</sup>t.

In operating such a credit card portfolio so as to maximise pro<sup>fi</sup>t, the main decisions are what interest rate to charge on the card and which applicants to accept and which to reject. The latter is done by choosing a cut-off level $p ^ { * }$ of the hazard rate of being Good and only accepting those above this cut-off. This is implemented by calculating the corresponding cut-off score (s\*) on the Good–Bad scorecard, i.e.

$$
p * = \left(\frac {1}{1 + e ^ {- s ^ {*}}}\right) ^ {1 / M}\tag{9}
$$

where the Good–Bad scorecard assumes a Good is someone who does not default over the next M periods.

The optimal cut-off probability p\* must satisf $\begin{array} { l } { \displaystyle { \ d } { \boldsymbol { \prime } } e ( r , p ^ { * } ) = 0 . } \end{array}$ . Substituting this into Eq. (7) gives

$$
\begin{array}{l} m - 1 + \frac {(1 + r) ^ {N - 1}}{(1 + r _ {F}) ^ {N}} \left(1 - l _ {D} + l _ {D} p ^ {N}\right) = 0 \Rightarrow p ^ {*} \\ = \left(\frac {(1 - m) (1 + r _ {F}) ^ {N}}{l _ {D} (1 + r) ^ {N - 1}} + \frac {l _ {D} - 1}{l _ {D}}\right) ^ {1 / N} \end{array}\tag{10}
$$

where

$$
\begin{array}{l} N = \frac {(1 + r) B + P}{C} = \frac {B + C}{C} \\ \text { by(5)and(6). } \end{array}
$$

If the interest rate on the cards is r, the corresponding pro<sup>fi</sup>t from the possible spend each period in the portfolio of potential credit card customers is $E ( r )$ where

$$
E (r) = \int_ {p * (r)} ^ {1} e (r, p) q (r, p) f (p) d p.\tag{11}
$$

One cannot get an analytic expression for the optimal rate to charge as this integral is too complicated to differentiate with respect to r. However, we can repeat the calculation for different interest rates and hence <sup>fi</sup>nd the optimal one.

## 5.1. Example 1: profit model with no transactor/revolver scorecard

This is the pro<sup>fi</sup>t model we use to make a comparison with the transactor/revolver pro<sup>fi</sup>t model. We can calculate the optimal cut-off probability, the pro<sup>fi</sup>t per period from the portfolio of potential customers and hence the optimal interest rate to charge. Phillips [18] and Thomas [23] suggested the simplest form for $q ( r , p )$ is the linear one:

$$
q (r, p) = \operatorname{Min} \{1, \operatorname{Max} [ 0, a - b r - c p ] \}\tag{12}
$$

where a, b, and c are constants. Therefore, we will assume that the take function is a linear one where

$$
q (r, p) = \max \{1 - 1 0 r + 2 (1 - p), 0 \} = 3 - 1 0 r - 2 p, \text {i.e.} a = 3, b = 1 0, c = 2.
$$

This means everyone will take the card if the interest rate is 0% and all those who are certain to default (i.e. $p = 0 )$ will take the card if the interest rate is 20%. More realistically, if the rate is 3%, then the take rate among those whose Good hazard rate is 0.9 per month is 90%.

For this example, the other parameters are:

$$
M = 0. 0 2 (\text { merchant   service   charge })
$$

$$
r = 0. 0 3 (\text { interest   rate   charged   per   period })
$$

$r _ { F } = 0 . 0 1$ (interest rate at which lender can borrow money each period)

$l _ { D } = 0 . 6$ (percentage <sup>fi</sup>nal loss of balance at default on credit card)

P = 51 (average purchase per period using the credit card)

$$
C = 6 0 (\text { average   repayment   per   period })
$$

$$
B = 3 0 0 (\text { average   balance   each   period })
$$

The above values for m, r, r and $l _ { D }$ re<sup>fl</sup>ect the current typical credit values. Also, P, B and C are ball park <sup>fi</sup>gures based on the normalised averages from the credit card dataset.

The distribution of risk in the potential card population is given by $F ( p )$ the distribution function on p the Good hazard rate. Let it be

$$
F (p) = \left\{ \begin{array}{c} 0, p <   0. 5 \\ 2 p ^ {2} - 2 p + 0. 5, 0. 5 \leq p <   1, \\ 1, p = 1. \end{array} \right.\tag{13}
$$

This means there is a 50% chance a user has a hazard rate of 1 and a 50% chance the hazard rate is between 0.5 and 1. This is the marginal p-distribution of the $( p , t )$ distribution which is used and explained more fully in Example 2.

Substituting in the parameter values in $E ( r , p )$ s for the case $r = 0 . 0 3$ gives

$$
e (. 0 3, p) = 5 1 \left(- 0. 9 8 + \frac {(1 . 0 3) ^ {5} (0 . 4 + 0 . 6 p ^ {6})}{(1 . 0 1) ^ {6}}\right).\tag{14}
$$

Table 5 gives the results of these calculations. In fact, we calculate $p ^ { * }$ and $E ( r )$ not just for $r = 0 . 0 3$ but also for other interest rates. For the other values of r, we make $\boldsymbol { B } = \left( \boldsymbol { C } - \boldsymbol { P } \right) / \boldsymbol { r } = 9 / r ,$ so that (5) still holds.

Expected pro<sup>fi</sup>t (i.e. E(r)) and cut-off probabilities (i.e. p\*) as a function of the interest rates (i.e. r) charged for Example 1 (without the revolver/transactor scorecard). Assuming that the de<sup>fi</sup>nition of Good/Bad in the scorecard covers a period of 12 months, then $( { \bf p } ^ { * } ) ^ { 1 2 }$ describes the corresponding optimal cut-off.

<table><tr><td>r</td><td>p*</td><td> $(p^{*})^{12}$ </td><td>E(r)</td></tr><tr><td>0.03</td><td>0.969</td><td>0.687</td><td>2.084</td></tr><tr><td>0.02</td><td>0.983</td><td>0.817</td><td>1.783</td></tr><tr><td>0.04</td><td>0.957</td><td>0.590</td><td>2.040</td></tr></table>

Results show that if the interest rate on the credit card is set at 3%, then the optimal cut-off corresponds to a hazard probability of 0.969. Assuming that the de<sup>fi</sup>nition of Good/Bad in the scorecard covers a period of 12 months, then column three describes the optimal cut-off in terms of the probability of being a good, $( p ^ { * } ) ^ { 1 2 }$ , which is 0.687. The <sup>fi</sup>nal column gives the expected monthly pro<sup>fi</sup>t per month to the credit card organisation on each potential card holder in the population. Note that some of these potential users will refuse to accept cards because the interest rate may be too high. We tried other integer value interest rates namely 2% and 4%. The corresponding expected monthly pro<sup>fi</sup>ts are lower than that of 3%. So an interest rate of 3% roughly achieves the optimal maximum pro<sup>fi</sup>t.

This model overestimates the true values, because the majority of users who have very high probabilities of being Good $( p = 1 \mathsf { s a y } )$ are transactors. These users will not pay any interest on their card but as the model does not discriminate between revolvers and transactors, it assumes they all pay interest for 6 months if $r = 0 . 0 3$ . In the next section, we extend the model by allowing estimates of how likely a user is to be a transactor. This will allow us to calculate a numerical example which has essentially the same data as this one.

## 6. Credit card model if a transactor/revolver score is available

As was argued previously, the reality is that credit card users split into two groups — transactors who only use the card as a payment mechanism and pay off the balance on the card every period and revolvers who do use the card for credit and so do not pay off all the balance each month. In Section 3, we showed that one could construct a score $s _ { t } ( \mathbf { x } )$ which can be translated into the probability, $t ( x ) = P ( T | \mathbf { x } )$ is an applicant with characteristics x will be a transactor. How would the advent of such a transactor/revolver score affect the model of the optimal pro<sup>fi</sup>t of the credit cards and which customers should be accepted or rejected? This then let us calculate what the optimal interest rate to charge is.

Recall that in the general model, one assumes that any money borrowed on the credit card will take N periods before it is repaid. For transactors, by de<sup>fi</sup>nition, N will be 1 period as they pay off the balance in the period they receive the credit card statement. Assume that for revolvers it is $N _ { R }$ periods before they pay off. It is also quite possible that the average amount purchased each period is different for transactors than revolvers. Similarly the outstanding balance and the average repayment each period will be very different for transactors compared with revolvers. We de<sup>fi</sup>ne the relationships between these amounts as follows:

Using the same notation as in Section 4, let

$B _ { R }$ and $B _ { T }$ average balance carried over per period per revolver and transactor respectively;

$P _ { R }$ and $P _ { T }$ average amount purchased per period per revolver and transactor respectively;

$C _ { R }$ and $\mathsf { C } _ { T }$ average repayment amount per period per revolver and transactor respectively.

So for revolvers

$$
\begin{array}{l} r B _ {R} + P _ {R} = C _ {R}, \\ (1 + r) B _ {R} + P _ {R} = C _ {R} N _ {R} \end{array}\tag{15}
$$

while for transactors,

$$
\begin{array}{l} B _ {T} = 0, \\ C _ {T} = P _ {T} \Rightarrow N _ {T} = 1. \end{array}\tag{16}
$$

These values can be connected to the equivalent average values on the whole portfolio, where $P ( T )$ is the percentage of borrowers who are transactors. Let the average balance be B, the average purchase per period be P, the average repayment amount be C and the average number of periods between a purchase and when it is paid off the credit card be N. Then

$$
\begin{array}{l} P = P _ {T} P (T) + P _ {R} (1 - P (T)), \\ C = C _ {T} P (T) + C _ {R} (1 - P (T)), \\ B = B _ {R} (1 - P (T)), \\ N = \alpha N _ {R} (1 - \alpha) w h e r e \alpha = \frac {C _ {R} (1 - P (T))}{C _ {T} P (T) + C _ {R} (1 - P (T))}. \end{array}\tag{17}
$$

Consider the expected pro<sup>fi</sup>t to the lender on an applicant whose transactor score is t and whose Good/Bad score on the revolver segment of the population translates to a Good hazard rate of $p _ { R }$ (just as in Section 2). Let this be $e ( p _ { R } , t )$ . This satis<sup>fi</sup>es

$$
\begin{array}{l} e (p _ {R}, t) = \frac {1}{1 + e ^ {- s _ {t}}} P _ {T} \left((m - 1) + \frac {1}{1 + r _ {F}}\right) + \frac {1}{1 + e ^ {s _ {t}}} P _ {R} \\ \times \left((m - 1) + \frac {(1 + r) ^ {N _ {R} - 1} p _ {R} ^ {N _ {R} ^ {R}}}{(1 + r _ {F}) ^ {N _ {R}}} + \frac {(1 - l _ {D}) (1 + r) ^ {N _ {R} - 1} \left(1 - p _ {R} ^ {N _ {R}}\right)}{(1 + r _ {F}) ^ {N _ {R}}}\right) \\ = t P _ {T} \left((m - 1) + \frac {1}{1 + r _ {F}}\right) + (1 - t) P _ {R} \\ \times \left((m - 1) + \frac {(1 + r) ^ {N _ {R} - 1} p _ {R} ^ {N _ {R} ^ {R}}}{(1 + r _ {F}) ^ {N _ {R}}} + \frac {(1 - l _ {D}) (1 + r) ^ {N _ {R} - 1} \left(1 - q _ {R} ^ {N _ {R}}\right)}{(1 + r _ {F}) ^ {N _ {R}}}\right). \end{array}\tag{18}
$$

Hereafter, we use t rather than s in our analysis. The accept/reject decision is still straightforward. Only accept those who give positive pro<sup>fi</sup>t. However, the choice of which p to take now depends on the transactor “score” t. So the cut-off curve is ${ p _ { R } } ^ { * } ( t )$ where $e ( p _ { R } { } ^ { * } ( t )$ $t ) = 0$ from (18), this corresponds to

$$
\begin{array}{l} \frac {(1 + r _ {F}) ^ {N _ {R}}}{(1 + r) ^ {N _ {R} - 1}} \left(\frac {t P _ {T}}{(1 - t) P _ {R}} \left(1 - m - \frac {1}{1 + r _ {F}}\right)\right) = (m - 1) \frac {(1 + r _ {F}) ^ {N _ {R}}}{(1 + r) ^ {N _ {R}}} + 1 - l _ {D} + l _ {D} p _ {R} * (t) ^ {N _ {R}} \\ p _ {R} * (t) ^ {N _ {R}} = \frac {(1 + r _ {F}) ^ {N _ {R}}}{l _ {D} (1 + r) ^ {N _ {R} - 1}} \left(\frac {t P _ {T}}{(1 - t) P _ {R}} \left(1 - m - \frac {1}{1 + r _ {F}}\right) + 1 - m\right) + \frac {l _ {D} - ^ {D} 1}{l _ {D}} \\ p _ {R} * (t) = \left(\frac {(1 + r _ {F}) ^ {N _ {R}}}{l _ {D} (1 + r) ^ {N _ {R} - 1}} \left(\frac {t P _ {T}}{(1 - t) P _ {R}} \left(1 - m - \frac {1}{1 + r _ {F}}\right) + 1 - m\right) + \frac {l _ {D} - {} ^ {D} 1}{l _ {D}}\right) ^ {1 / N _ {R}}. \end{array}\tag{19}
$$

To calculate the corresponding pro<sup>fi</sup>t from the possible spend each period in the portfolio of potential credit card customers, one needs to know the distribution of Good/Bad and transactor/revolver in the portfolio. Assume this is given by a density function/probability mass function $f ( p , t )$ . If the interest rate charged is r then the pro<sup>fi</sup>t per potential customer is $E ( r )$ where

$$
E (r) = \int_ {- \infty} ^ {\infty} d t \int_ {p * (t)} ^ {1} e (r, p) q (r, p) f (p, t) d p.\tag{20}
$$

We calculate this pro<sup>fi</sup>t for a numerical example which is essentially the same as Example 1. We will then be able to compare the pro<sup>fi</sup>ts and optimal decisions in the two models. The parameters are as follows.

## 6.1. Example 2. Profit model with transactor/revolver scorecard

We use the same take function as those of Example 1:

$$
q (r, p) = \max \{1 - 1 0 r + 2 (1 - p), 0 \} = 3 - 1 0 r - 2 p, i. e. a = 3, b = 1 0, c = 2.\tag{21}
$$

The other parameters are

$$
\begin{array}{l} m = 0. 0 2 \text {(merchant service charge)} \\ r = 0. 0 3 \text {(interest rate charged per period)} \end{array}
$$

The distribution of risk in the potential card population is given by $f ( p , t )$ a joint distribution function on both t, the probability of being a transactor and p the hazard probability of remaining a Good for one more period. Let it be

$$
F (p, t) = \left\{ \begin{array}{l l} 0, p <   0. 5 \\ 2 p ^ {2} - 2 p + 0. 5 & 0. 5 \leq p <   1 2 p - 1 > t \\ 2 t p - t - 0. 5 t ^ {2} & 0. 5 \geq p <   1 2 p - 1 \leq t \\ 1 p = 1, t = 1. \end{array} \right.\tag{22}
$$

This distribution has a point mass of 0.5 at the point $p = 1 , t = 1 ,$ which describes the transactors. The remaining 0.5 is uniformly distributed in the triangular region between $( t = 0 , p = 0 . 5 ) , ( t = 0 , p = 1 )$ and $( t = 1 , p = 1 )$ . The percentage of transactors in the whole population is on average t where

$$
\begin{array}{l} \bar {t} = \int_ {0} ^ {1} t d t \int_ {0} ^ {1} f (p, t) d p = 0. 5 \times 1 + \int_ {0} ^ {1} t (2 (0. 5 - 0. 5 t)) d t \\ = 0. 5 + 0. 1 6 6 6 = ^ {2} / _ {3}. \end{array}\tag{23}
$$

We want to match the average value of purchases and payments to those in Example 1 where we had for the case when $r = 0 . 0 3$

$$
\begin{array}{l} P = 5 1 \text {(average purchase per period using the credit card)} \\ C = 6 0 \text {(average repayment per period)} \\ B = 3 0 0 = (C - P) / r \text {(average balance each period)}. \\ \text {Since} \bar {t} = 2 / 3, \text {we set} \\ P _ {R} = 9 \text {(average purchase per period using the credit card)} \\ C _ {R} = 3 6 \text {(average repayment per period)} \\ B _ {R} = 9 0 0 \text {(average balance each period)} \\ P _ {T} = 7 2 \text {(average purchase per period using the credit card)} \\ C _ {T} = 7 2 \text {(average repayment per period)} \\ B _ {T} = 0 \text {(average balance each period)}. \end{array}
$$

These are again ball park <sup>fi</sup>gures guided by the averages in the data set.

$$
\begin{array}{l} \text { Average   purchase } = \bar {t} P _ {T} + (1 - \bar {t}) P _ {R} (2 / 3) 7 2 + (1 / 3) 9 = 5 1 \\ \text { Average   payment } = \bar {t} C _ {T} + (1 - \bar {t}) C _ {R} = (2 / 3) 7 2 + (1 / 3) 3 6 = 6 0. \end{array}\tag{24}
$$

We can then put these parameter values into (18) and (19) to get the following

$$
\begin{array}{l} E (p _ {r}, t) = 7 2 t \left(- 0. 9 8 + \frac {1}{1 . 0 1}\right) + 9 (1 - t) \\ \times \left(- 0. 9 8 + \frac {(1 . 0 3) ^ {3 5} p ^ {3 6}}{(1 . 0 1) ^ {3 6}} + \frac {(0 . 4) (1 . 0 3) ^ {3 5} \left(1 - p ^ {3 6}\right)}{(1 . 0 1) ^ {3 6}}\right). \end{array}\tag{25}
$$

Note that there is no one cut off probability (or Good/Bad score) but a curve of them depending on the probability of the applicant being a potential transactor.

These are obtained from the calculation

$$
p _ {R} ^ {*} (t) = \left(\frac {(1 . 0 1) ^ {2 6}}{0 . 6 (1 . 0 3) ^ {2 5}} \left(\frac {7 2 t}{9 (1 - t)} \left(- 0. 9 8 - \frac {1}{1 . 0 1}\right) + 0. 9 8\right) - \frac {0 . 4}{0 . 6}\right) ^ {1 / 2 6}.\tag{26}
$$

The results are shown in Table 6 both for the case $r = 0 . 0 3$ and the cases $r = 0 . 0 2$ and $r = 0 . 0 4 .$ . In all cases, the cut off probability p<sup>∗</sup> (t)

Table 6  
Expected pro<sup>fi</sup>t (i.e. E(r)) and cut-off probabilities (i.e. p\*) as a function of interest rates charged (i.e. r) and transactor probability (i.e. t) for Example 2 with a revolver/transactor scorecard. Assuming that the de<sup>fi</sup>nition of Good/Bad in the scorecard covers a period of 12 months, then $( \mathbf { p } ^ { * } ) ^ { \dot { 1 } 2 }$ describes the corresponding optimal cut-off.

<table><tr><td rowspan="2">r</td><td rowspan="2"></td><td colspan="11">t</td><td rowspan="2">E(r)</td></tr><tr><td>0</td><td>0.1</td><td>0.2</td><td>0.3</td><td>0.4</td><td>0.5</td><td>0.6</td><td>0.7</td><td>0.8</td><td>0.9</td><td>1</td></tr><tr><td rowspan="2">0.03</td><td rowspan="2"> $p^*$  $(p^*)^{12}$ </td><td>0.960</td><td>0.959</td><td>0.957</td><td>0.956</td><td>0.953</td><td>0.950</td><td>0.943</td><td>0.929</td><td>0.839</td><td>0.000</td><td>0.000</td><td rowspan="2">0.330</td></tr><tr><td>0.611</td><td>0.603</td><td>0.594</td><td>0.581</td><td>0.563</td><td>0.537</td><td>0.496</td><td>0.416</td><td>0.122</td><td>0.000</td><td>0.000</td></tr><tr><td rowspan="2">0.04</td><td rowspan="2"> $p^*$  $(p^*)^{12}$ </td><td>0.924</td><td>0.922</td><td>0.919</td><td>0.915</td><td>0.909</td><td>0.898</td><td>0.872</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td rowspan="2">0.399</td></tr><tr><td>0.386</td><td>0.375</td><td>0.362</td><td>0.344</td><td>0.318</td><td>0.276</td><td>0.194</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td rowspan="2">0.02</td><td rowspan="2"> $p^*$  $(p^*)^{12}$ </td><td>0.982</td><td>0.981</td><td>0.980</td><td>0.979</td><td>0.977</td><td>0.975</td><td>0.971</td><td>0.963</td><td>0.940</td><td>0.000</td><td>0.000</td><td rowspan="2">0.311</td></tr><tr><td>0.804</td><td>0.797</td><td>0.788</td><td>0.776</td><td>0.760</td><td>0.737</td><td>0.701</td><td>0.636</td><td>0.473</td><td>0.000</td><td>0.000</td></tr></table>

drops from 0.96 at $t = 0 \mathrm { t o } 0 \mathrm { a t } t = 1 .$ . For all interest rates shown one accepts everyone whose transactor probability is at least 0.9 and when the interest rate is 4%, all those whose transactor probability is 0.7 or more are accepted. This makes sense since the higher the transactor score the less important is the Good/Bad probability calculated on revolvers. The cut-off Good/Bad probability drops gently when the Transactor probability is low, but then drops much more steeply until it reaches zero, when the transactor probabilities are higher. The expected optimal pro<sup>fi</sup>t per month on each potential user is around 0.3 compared with the 2.0 found in Example 1. This is not saying that using the transactor/revolver score leads to lower pro<sup>fi</sup>ts but that it gives a much more accurate model. This model does not overestimate the pro<sup>fi</sup>t by assuming transactors repay their purchase over the same period as revolvers. The difference shows the signi<sup>fi</sup>cance of the error of not including the transactor/revolver effect has on the original model. In this case, the rate (assuming an integer value) which maximises pro<sup>fi</sup>tability is 4% with a pro<sup>fi</sup>t of 0.399. Note this is higher than the optimal 3% of Example 2. In that 3% case, the cut-off probability $( p ^ { * } ) ^ { 1 2 }$ when one will accept an applicant is 0.687. In the transactor/ revolver model one is willing to take more risky applicants in terms of their revolver Good rate no matter what their probability of being a transactor. Even if t = 0 (i.e. the applicants are revolvers) in the second example one takes more potential applicants than in the <sup>fi</sup>rst example. This is because the second model correctly recognises how much longer revolvers pay interest on their purchases compared with the average card user. So one can increase the chance of default slightly to allow for this extra revenue. It does seem from this second example that lenders should have a larger portfolio and can charge slightly higher interest rates than those suggested by the <sup>fi</sup>rst example — 4% rather than 3%.

## 7. Conclusions

The idea of thinking of credit card users as transactors or revolvers has been used by practitioners for some time. However, this is the <sup>fi</sup>rst paper to show how to build a scorecard to estimate the chance of each applicant being a transactor and how that makes a difference to pro<sup>fi</sup>tability modelling. Using a real credit card data set we have built and tested such a scorecard. We show how such a scorecard can be part of a default risk assessment system. The resulting system is comparable, with very similar results, to the standard Good/Bad scorecard approach based on the whole population. The similarity of the ROC curves in Fig. 2 con<sup>fi</sup>rms this.

The great improvement in using a transactor/revolver scorecard is in estimating the pro<sup>fi</sup>tability of potential applicants. The paper develops a new pro<sup>fi</sup>tability model for credit card users which re<sup>fl</sup>ects the length of time the cost of purchases stays in the balance. Previous models have either ignored this altogether or assumed the repayment is forever.

We have shown by numerical examples how the results of a pro<sup>fi</sup>tability model which includes estimates of the probability of an applicant being a transactor compare with the results if the model does not have such estimates. We <sup>fi</sup>nd the latter overestimates the pro<sup>fi</sup>tability of an applicant because it believes the Good applicants will take longer to pay back than is the case. The latter model also leads to a much cruder choice of accept/reject decision. The optimal interest rate it suggests is lower than that when one includes the transactor/revolver effect. The advantage of the transactor/revolver model when choosing optimal overall pricing decisions is signi<sup>fi</sup>cant. If the transactor/revolver scorecard is used in making the initial accept decision, then it leads to a more exact model of the pro<sup>fi</sup>tability of the applicants and a more sophisticated acceptance criterion. That in turn means the lender will accept more applicants and so have a larger and more pro<sup>fi</sup>table portfolio.

(a)  
![](/api/attachments/PWC6C8AT/fulltext/images/a74561f487ef9d1a13a6a5eaf28587f633fd1d74963cce6420799810b5071951.jpg)

(b)  
![](/api/attachments/PWC6C8AT/fulltext/images/d70d33d457bf60474e47b2f27a0b83ce392f2de41519ef7d321a5f16eacdeeb6.jpg)  
Fig. 2. ROC curves for Model 1 and Model 4: (a.) Validation 1 (b.) Validation 4.

One issue when developing transactor/revolver scorecards is what the most useful de<sup>fi</sup>nition of a transactor is. If it is someone who has paid off the balance every month over a period, what is an appropriate period? Should the de<sup>fi</sup>nition of a transactor allow for users who occasionally forget to pay on time, make errors in the amount to repay, or refuse to pay initially for some purchase they are questioning? So should one weaken the de<sup>fi</sup>nition of transactor to allow one or two months where not all the balance is paid off during that period. This is an area for further research.

It is not unusual for a credit scoring system to segment the population into segments according to the values of a characteristic like age and to build separate scorecards for each segment. In the data set used here, age and income are signi<sup>fi</sup>cant for the transactor/revolver model but not for the Good/Bad model for revolvers or the Good/Bad model on the whole data set. So maybe splitting on characteristics like age in a standard scoring system could be a surrogate way of dealing with the transactor/revolver split.

It would also be interesting to investigate how a transactor/revolver score would improve churn predictions. Is it transactors or revolvers who are more likely to churn? So there are a number of avenues to follow from this development of transactor/revolver scorecards.

## References

[1] R. Anderson, The Credit Scoring Toolkit, Oxford University Press, Oxford, 2007.

[2] G. Andreeva, J. Ansell, J. Crook, Modelling pro<sup>fi</sup>tability using survival combination scores, European Journal of Operational Research 183 (2007) 1537–1549.

[3] B. Baesens, R.T.V. Gestel, S. Viaene, M. Stepanova, J. Suykens, J. Vanthienen, Benchmarking state-of-the-art classi<sup>fi</sup>cation algorithms for credit scoring, Journal of the Operational Research Society 54 (2003) 627–635.

[4] R. Birch, Card shift: more transactors fewer revolvers, Credit Union Journal 16 (2012) 8.

[5] S. Cau<sup>fi</sup>eld, Consumer Credit Pricing, in: Ö. Özer, R. Phillips (Eds.), Oxford Handbook of Pricing Management, Oxford University Press, Oxford, 2012, pp. 138–153.

[6] E. Dash, Rewards Cardholders Face a Higher Price for Perks, The New York Times, New York http://www.nytimes.com/2010/02/20/business/20rewards.html?pagewanted= all& r=0February 2010

[7] E.R. DeLong, D.M. DeLong, D.L. Clarke-Pearson, Comparing the areas under two or more correlated receiver operating characteristic curves: a nonparametric approach, Biometrics 44 (1988) 837–845

[8] N. Field, C. Walker, Are you a Revolver or Transactor? Money Magazine (Australia), http://<sup>fi</sup>nance.ninemsn.com.au/p<sup>fl</sup>oansandcredit/creditcards/8123045/are-you-arevolver-or-transactorJuly 2004.

[9] S.M. Finlay, Towards pro<sup>fi</sup>tability: a utility approach to the credit scoring problem Journal of the Operational Research Society 59 (2008) 921–931.

[10] S.M. Finlay, Credit scoring for pro<sup>fi</sup>tability objectives, European Journal of Operational Research 202 (2010) 528–537.

[11] S. Herbst-Murphy, Trends and Preferences in Consumer Payments: Lessons from the Visa Payment Panel Study, Discussion paper, Payment Cards Center, Federal Reserve Bank of Philadelphia, Philadelphia, 2010.

[12] Z. Huang, H.C. Chen, C.J. Hsu, W.H. Chen, S.S. Wu, Credit rating analysis with support vector machines and neural networks: a market comparative study, Decision Support Systems 37 (2004) 543–558.

[13] K. Hussain, Valuation of a bank credit-card portfolio, Journal of American Academy of Business 10 (2007) 29–35.

[14] J. Huysmans, K. Dejaeger, C. Mues, J. Vanthienen, B. Baesens, An empirical evaluation of the comprehensibility of decision table, tree and rule based predictive models, Decision Support Systems 51 (2011) 141–154.

[15] H. Kim, S.A. DeVaney, The determinants of outstanding balances among credit card revolvers, Financial Counseling and Planning 12 (2001) 67–78.

[16] B.V. Oliver, R.M. Oliver, Optimal ROE loan pricing with or without adverse selection, Journal of the Operational Research Society (July 11 2012), http://dx.doi.org 10.1057/jors.2012.87(Advance online publication).

[17] Y. Peng, G. Kou, Y. Shi, Z. Chen, A multi-criteria convex quadratic programming model for credit data analysis, Decision Support Systems 44 (2008) 1016–1030.

[18] R.L. Phillips, Pricing and Revenue Optimization, Stanford University Press, Stanford 2005.

[19] S. Singh, B.P.S. Murthi, E. Steffes, Developing a measure of risk adjusted revenue (RAR) in credit card market: implications for customer relationship management, European Journal of Operational Research 224 (2013) 425–434.

[20] M.M.C. So, L.C. Thomas, Modelling and model validation of the impact of the economy on the credit risk of credit card portfolios, Journal of Risk Model Validation 4 (2010) 93–126.

[21] C. Sprenger, J. Stavins, Credit Card Debt and Payment Use, Working Paper 08-2, Federal Reserve Bank of Boston, Boston, 2008

[22] R.T. Stewart, A pro<sup>fi</sup>t-based scoring system in consumer credit: making acquisition decisions for credit cards, Journal of the Operational Research Society 62 (2011) 1719–1725.

[23] L.C. Thomas, Consumer Credit Models; Pricing, Pro<sup>fi</sup>t and Portfolios, Oxford University Press, Oxford, 2009.

[24] J. Zinman, Debit or credit? Journal of Banking & Finance 33 (2009) 358–366

Mee Chi So is a Lecturer in Southampton Management School at the University of Southampton. She obtained her <sup>fi</sup>rst degree and a master's degree in Operational Research from the University of Hong Kong. She was awarded her Ph.D. by the University of Southampton in Management Sciences. Her current research interests are in the areas of marketing analytics and consumer credit risk modelling. She has publications in European Journal of Operational Research, Journal of Operational Research Society, Pattern Recognition, Transportation Research Part E: Logistics and Transportation Review and Journal of Risk Model Validation

Lyn Thomas is Professor of Management Science at the University of Southampton. His interests are in applying Operational Research and statistical ideas in the <sup>fi</sup>nancial area, particularly in credit scoring and risk modelling in consumer lending. He is a founder member of the Credit Research Centre at the University of Edinburgh and one of the principal investigators for the Quantitative Financial Risk Management Centre based at Southampton. He has authored or co-authored nearly 200 research papers and four books in the area, including “Consumer Credit models: Pricing, Pro<sup>fi</sup>t and Portfolios” and “Credit Scoring and its Applications”. He is a Fellow of the Royal Society of Edinburgh, a Past President of the Operational Research Society and was awarded the Beale Medal of that Society in 2008.

Associate Professor Hsin-Vonn SEOW joined the University of Nottingham Malaysia campus in 2006 after finishing her Ph.D. in Management Science at the University of Southampton in the United Kingdom, She is currently the Director of the Ph.D. programme at the Nottingham University Business School Malaysia. Her current research interests are in Operational Research techniques which includes looking at applications of management science techniques in <sup>fi</sup>nance and banking with strong interest in credit scoring and credit control, interactive application channels (internet and telephone banking) for <sup>fi</sup>nancial products and data mining. She is a member of the Operational Research Society in the UK and has publications in the European Journal of Operational Research and the Journal of the Operational Research Society.

Christophe Mues is a senior lecturer at the Management School of the University of Southampton. Prior to his appointment in Southampton, he obtained the degree of Doctor in Applied Economics at KULeuven. His current research interests lie mostly in the areas of credit risk modelling and data mining, where he has applied a series of novel techniques to problem settings ranging from traditional credit scoring to more recent areas such as loss-give-default modelling. He has published his <sup>fi</sup>ndings in various international journals and conference proceedings
