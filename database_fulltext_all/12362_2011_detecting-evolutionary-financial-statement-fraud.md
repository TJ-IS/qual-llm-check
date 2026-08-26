---
otero_id: 12362
otero_key: "V2B5WKM6"
title: "Detecting evolutionary financial statement fraud"
authors: "Wei Zhou; Gaurav Kapoor"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.08.007"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Detecting evolutionary <sup>fi</sup>nancial statement fraud

Wei Zhou <sup>a,</sup>⁎, Gaurav Kapoor <sup>b</sup>

<sup>a</sup> Information Systems and Technologies, ESCP Europe, 75543 Paris cedex 11, France

<sup>b</sup> Information Systems and Operations Management, University of Florida, Gainesville, Florida 32611, USA

## a r t i c l e i n f o

Available online 24 August 2010

Keywords: Financial statement fraud Data mining technique Neural networks

## a b s t r a c t

A fraudulent <sup>fi</sup>nancial statement involves the intentional furnishing and/or publishing of false information in it and this has become a severe economic and social problem. We consider Data Mining (DM) based <sup>fi</sup>nancial fraud detection techniques (such as regression, decision tree, neural networks and Bayesian networks) that help identify fraud. The effectiveness of these DM methods (and their limitations) is examined, especially when new schemes of <sup>fi</sup>nancial statement fraud adapt to the detection techniques. We then explore a self-adaptive framework (based on a response surface model) with domain knowledge to detect <sup>fi</sup>nancial statement fraud. We conclude by suggesting that, in an era with evolutionary <sup>fi</sup>nancial frauds, computer assisted automated fraud detection mechanisms will be more effective and ef<sup>fi</sup>cient with specialized domain knowledge.

© 2010 Elsevier B.V. All rights reserved

## 1. Introduction

Since the booming of the Internet and the invention of other modern technologies, there has been a dramatic increase in fraudulent schemes associated with all facets in the business world. Some of these commonly observed schemes include credit card fraud, <sup>fi</sup>nancial statement fraud, e-commerce transaction fraud, insurance fraud, money laundering, computer intrusion fraud, telecommunications fraud, and subscription fraud. Statistic and machine learning based technologies have been shown to be an effective way to deter and detect fraud, but fraudsters are adaptive and are usually able to <sup>fi</sup>nd ways to circumvent them. Existing fraud detection techniques for most of the situations involving fraud usually share very similar data mining principles, but they can differ in many aspects with specialized domain knowledge [5].

Financial statement fraud in particular has cast rapidly increasing adverse impact not only on individual investors but the overall stability of global economies. Although there are minor variations in its de<sup>fi</sup>nition, a <sup>fi</sup>nancial statement fraud is de<sup>fi</sup>ned by the Association of Certi<sup>fi</sup>ed Fraud Examiners as “The intentional, deliberate, misstatement or omission of material facts, or accounting data which is misleading and, when considered with all the information made available, would cause the reader to change or alter his or her judgment or decision.” In practice, <sup>fi</sup>nancial statement fraud might involve: (1) manipulation of <sup>fi</sup>nancial records, (2) intentional omission of events, transactions, accounts, or other signi<sup>fi</sup>cant information from which <sup>fi</sup>nancial statements are prepared, or (3)

misapplication of accounting principles, policies, and procedures used to measure, recognize, report, and disclose business transactions [20].

Many techniques based on data mining have been investigated and implemented to detect <sup>fi</sup>nancial statement fraud, including regression, decision trees, neural networks and Bayesian belief networks [12]. These techniques have been shown to be successful in their early stages. However, there is no agreement on which data features and techniques are best for detection. Also, while supervised learning techniques have been among the dominant methods used for detecting <sup>fi</sup>nancial statement fraud, a majority of related implementations do not keep track of new variations in the methods designed for committing fraud. Moreover, <sup>fi</sup>nancial fraud is becoming more and more dif<sup>fi</sup>cult to detect using the current detection techniques. A CEO who is truly knowledgeable and wants to really commit a crime has the necessary resources to easily outwit the system and is able to fool any detection mechanism [7].

Despite the increased of time and effort that has been spent to detect the same, the number of detected frauds<sup>1</sup> and the detection rate<sup>2</sup> have largely decreased [7]. When the executives who are involved in <sup>fi</sup>nancial fraud are well aware of the fraud detection techniques and software, which are usually public information and are easy to obtain, they are likely to adapt the methods in which they commit fraud and make it dif<sup>fi</sup>cult to detect the same, especially by existing techniques. There exists an urgent need for new methods that is not only ef<sup>fi</sup>cient but effective to catch up with these probable newly emerged or adaptive <sup>fi</sup>nancial shenanigans. We (1) consider existing detection techniques based on data mining, (2) provide an overview of existing <sup>fi</sup>nancial shenanigans and their trend, and (3) suggest a new framework to detect evolutionary <sup>fi</sup>nancial statement fraud.

The remainder of this paper is organized as follows. We review the application of regression, decision trees, neural networks and Bayesian belief networks in <sup>fi</sup>nancial statement fraud detection in the next section. We survey the history and trend of contemporary <sup>fi</sup>nancial fraud in Section 3. We analyze the effectiveness and limitation of existing fraud detection technologies in Sections 4 and 5 and then suggest a framework that addresses the problem when emerging <sup>fi</sup>nancial fraud is evolutionary. Section 6 concludes the paper with a brief discussion on the insights garnered and possible future research.

## 2. Review on detection techniques

Classi<sup>fi</sup>cation has been the most popular and the only way used so far to identify fraudulent <sup>fi</sup>nancial statements [8]. Most <sup>fi</sup>nancial statement fraud (FSF) auto-detection programs use supervised machine learning methodologies [1,3,4,9–11,14,18,21,22] that usually have a two-stage procedure, where in the <sup>fi</sup>rst stage a model is trained by using a training sample. The training sample is organized in tuples and attributes, with the class label attribute containing values indicating the pre-de<sup>fi</sup>ned class to which each tuple belongs. In the second stage, objects are classi<sup>fi</sup>ed through the model obtained from the <sup>fi</sup>rst stage. After reviewing relevant research in data mining-based <sup>fi</sup>nancial statement fraud detection literature, we observe that the following <sup>fi</sup>ve methods have been used so far in this general area. These methods include regression, decision trees, neural networks, Bayesian networks and support vector machines.

Regression is the most widely used method to detect <sup>fi</sup>nancial statement fraud [1,3,4,11,18,21,22]. Transformations of variables in regression models have also been studied in the context of fraud detection, including logit, stepwise-logistic, multi-criteria decision aid method and exponential generalized beta two. For example, Spathis [21] used a collection of data from 76 <sup>fi</sup>rms that include 38 fraudsters and 38 non-fraudulent <sup>fi</sup>rms in Greece. They use ten <sup>fi</sup>nancial variables and logistic multivariate regression to identify the relationship among factors associated with <sup>fi</sup>nancial statement fraud. A total of ten financial ratios such as the net profit to total assets ratio. the ratio of total debt to total assets, <sup>fi</sup>nancial distress, the inventories to sales ratio, and the working capital to total assets ratio are selected for examination as potential predictors of FSF. The results indicate that companies with high inventories with respect to sales, high debt to total assets, low net pro<sup>fi</sup>t to total assets, low working capital to total assets and high <sup>fi</sup>nancial stress are more likely to manipulate <sup>fi</sup>nancial statements.

A neural network is another popular data mining technique that has been successfully used to detect <sup>fi</sup>nancial statement fraud [6,9,14,16,24]. Neural network doesn't assume an attribute's independence and is capable of mining inter-correlated data and is a suitable alternative for problems where some of the assumptions associated with regression are not valid. White [24], nonetheless, has shown that feed-forward neural networks, which require no prespeci<sup>fi</sup>ed functional form, perform the same stochastic approximation as nonlinear regression. Back propagation neural network allows the network to adapt and has become one of the most popular techniques for prediction and classi<sup>fi</sup>cation problems. The back propagation learning process works in small iterative steps that continuously make small changes to the weights in each neural network layer, which are calculated to reduce the systematic error. The iteration is repeated until the overall error value drops below some pre-determined threshold [13]. Drawbacks of implementing neural networks to discover FSF is that neural network is not accurate if the data is volatile or if the causal functionality evolves in a direction that is not pre-de<sup>fi</sup>ned.

The objective of decision trees is classi<sup>fi</sup>cation by dividing observations into mutually exclusive and exhaustive subgroups by properly selecting attributes that best separate the sample. Koh and Low [13] construct a decision tree to predict the hidden problems in <sup>fi</sup>nancial statements by examining the following six variables: quick assets to current liabilities, market value of equity to total assets, total liabilities to total assets, interest payments to earnings before interest and tax, net income to total assets, and retained earnings to total assets.

The above mentioned data mining techniques have generally been shown to be effective in detecting <sup>fi</sup>nancial statement fraud. However, they are not without limitations. For example, while these techniques are well developed for predictive modeling, they are not as well developed for effect assessment. In particular, test statistics for assessing the effects of independent variables on dependent variables have not yet been constructed for some data mining techniques. Incidentally, this shortcoming also demands with the challenge to develop more effective mechanisms especially in an adaptive economic environment where <sup>fi</sup>nancial fraudsters learn to circumvent existing automated detection systems.

## 3. Detection with domain knowledge on FSF

Financial statement fraud, including motivations, opportunities, and rationalizations for management to commit such fraud, has been extensively studied by researchers in <sup>fi</sup>nance. Loebbecke et al. [15] suggest a model consisting of three variables that may explain <sup>fi</sup>nancial statement fraud: (C) the degree to which conditions are such that a <sup>fi</sup>nancial fraud could be committed, (M) the degree to which the management has a reason or motivation to commit <sup>fi</sup>nancial fraud, and (A) the degree to which the management has an attitude or set of ethical values such that they would allow themselves to commit management fraud. These three variables together form the assessment model such that the possibility of having <sup>fi</sup>nancial statement fraud (FSF) can be described as a function.

$$
P (F S F) = f (C, M, A)\tag{1}
$$

where if C or M or $\mathsf { A } = \mathsf { 0 } ,$ then $\mathrm { P } ( \mathrm { F S F } ) = 0 .$

According to Rezaee [19], fraud accomplishment can be explained by three variables: (1) conditions, (2) corporate structure and (3) choice. The suf<sup>fi</sup>cient incentives and opportunities for a company to commit <sup>fi</sup>nancial statement fraud can be interpreted by the pattern exhibited by these three variables. We, however, believe that certain combination of the variables mentioned in this model also leads to certain suitable fraud strategies and, by measuring the pattern among the variables and integrating the <sup>fi</sup>ndings in auto-detection heuristics, we should be able to pinpoint the unique shenanigans and their underlying dynamic to commit fraud.

We <sup>fi</sup>rst review possible variables that can be utilized in an autodetection system. In Rezaee's[19] 3C's model as shown in Fig. 1, “conditions” refers to the economic and <sup>fi</sup>nancial pressures that a corporation faces. Financial pressures, such as pressure to meet analysts' earning estimates, can be a key factor stimulating earnings management and resulting in <sup>fi</sup>nancial statement fraud. The principle underlying this variable is that <sup>fi</sup>nancial statement fraud will most probably occur if the bene<sup>fi</sup>ts for fraudulent management outweigh the associated costs. Management compares the bene<sup>fi</sup>t, in terms of possible increase in the company's stock price or the possible savings related to preventing share price from decreasing, with the possible cost of committing fraud in terms of probability and consequences of detection. Financial pressures, such as the inability to meet analysts' earning estimates or decline in quality and quantity of earnings, are often motivations for management commitment in <sup>fi</sup>nancial frauds.

“Capital structure” refers to the existence of an effective corporate governance mechanism (such as internal control structure and audit committees) that could discourage management from committing fraud. The role of corporate governance devices can also be discussed in relation to other social and economic characteristics of different countries where fraud can be committed. It is also important to explain to what extent an effective corporate governance system can help to prevent and detect fraud.

![](/api/attachments/V2B5WKM6/fulltext/images/f7d1bbb0290fe1028836938dc43d0b2b2faa24f65311b6b749ae434645ab289d.jpg)  
Fig. 1. Rezaee's 3C <sup>fi</sup>nancial statement fraud model.

“Choices” refer to the management's option, which could either be ethical strategies of continuous improvements of earnings or illegal earning manipulations, to deal with various <sup>fi</sup>nancial situations. Financial statement fraud is simply one of the choices. Regardless of the corporate structure or environmental pressure, management could use <sup>fi</sup>nancial statement fraud simply as a strategic tool according to its own characteristics in terms of aggressiveness or lack of moral principles.

Both the CMA model [15] and the 3Cs model [19] mentioned above explain the <sup>fi</sup>nancial statement fraud by examining selected parameters, such as the motivations, conditions of pressure, corporate structure, management's attitude and the choices. These variables may each function separately, and careful selection and combination of variables, however, are more likely to help explain the degree and pattern of <sup>fi</sup>nancial statement fraud, thus providing insightful and immediate reference for an FSF auto-detection system.

The strategy that the management utilizes to commit <sup>fi</sup>nancial statement fraud is in<sup>fl</sup>uenced by the economic circumstances as well as many other variables that have been taken into consideration by the fraudster. Schilit [20] provides an extensive examination of the <sup>fi</sup>nancial statement fraud techniques and categorizes them into seven groups: recording revenue too soon or of questionable quality, recording bogus revenue, boosting income with one-time gains, shifting current expenses to a later or earlier period, failing to record or improperly reducing liabilities, shifting current revenue to a later period, and shifting future expenses to the current period as a special charge. The COSO report [2], by analyzing 204 cases of fraud presented in the SEC's Accounting Auditing Enforcement Releases (AAERs) from 1987 to 1997, lists common <sup>fi</sup>nancial statement fraud techniques in the following categories: improper revenue recognition, overstatement of assets other than accounts receivable, understatement of expenses/ liabilities, misappropriation of assets, inappropriate disclosure and other miscellaneous techniques.

## 4. Limitations of current detection techniques

Despite increasingly stringent legislation such as the Foreign Corrupt Practices Act and the Sarbanes–Oxley Act aimed at combating fraud – and despite increasingly growing number of fraud autodetection systems – <sup>fi</sup>nancial statement fraud is becoming a more and more severe public concern. Doloitte [7] reviews around 1300 Accounting and Auditing Enforcement Releases (AAER) that the SEC released from January 2000 to December 2006 and sorts each company into one of the following nine industries: aviation and transport services manufacturing; consumer business; public sector; energy and resources; real estate; <sup>fi</sup>nancial services; technology, media, and telecommunications; life sciences; and health care. Doloitte [7] reports that the number of <sup>fi</sup>nancial statement frauds that the SEC issued has decreased from 77 in 2003 to 44 in 2006. Although the number of reported frauds has decreased dramatically after the Sarbanes–Oxley Act was introduced in 2002, it is arguable whether the real number has decreased by that much. In reality, we have seen more fraudulent behaviors since 2008 when the economy has been going towards the lowest point since the great depression in 1929.

It leads us to believe that fraud types and industry patterns changed over time. It is important to understand how fraud schemes have evolved and it is more important to predict by any means possible, the direction of the change and keep the automatic fraud detection techniques up-to-date. The <sup>fi</sup>ndings may have signi<sup>fi</sup>cance to develop more robust business processes as well as adaptive fraud detection mechanism for managing/deterring/detecting the risk of fraud. The ef<sup>fi</sup>cacy of such processes will depend on knowing the fraud schemes typically committed and industry-by-industry differences in those schemes.

A majority of data mining-based <sup>fi</sup>nancial statement fraud detection techniques are primarily based on classi<sup>fi</sup>cation, which is the process of explaining and differentiating data classes in order to predict the class of objects whose class label is unknown. As compared to association rule mining that deals with existing data items, the classi<sup>fi</sup>cation rule mining deals with attributes and its values, clusters the attributes, and uses time-series mining or outlier detection to recognize the new mode for <sup>fi</sup>nancial statement fraud detection.

Despite the early success of these pioneering FSF auto-detection systems and algorithms, the rate of successful detection has continuously decreasing over the past several years. Although it is certainly possible that ethical standards have greatly improved since 2000, given the fact that the severity and quantity of law suits for <sup>fi</sup>nancial statement frauds have increased recently, we are more inclined to believe that managements have adapted certain ways to avoid being identi<sup>fi</sup>ed by automated detection systems.

Although according to the No-Free-Lunch theorem, existing data mining search techniques, including random search, should perform equally well on average, some techniques would have more accurate estimation than others when appropriate domain knowledge can be identi<sup>fi</sup>ed and integrated. In the next section, we propose a framework that utilizes domain knowledge to facilitate the detection of <sup>fi</sup>nancial statement fraud in a constantly evolving economic environment.

## 5. Adaptive FSF detection framework and methodologies

## 5.1. Framework to detect adaptive financial fraud

Similar to traditional classi<sup>fi</sup>cation procedure, in general we consider two stages in our framework (Fig. 2). In the <sup>fi</sup>rst stage, relevant external and internal variables that differentiate the industries, economic conditions, management's choice, timing considerations and any other factors that have the potential to form domain knowledge are selected and experimented. In the second stage, the <sup>fi</sup>nancial data of the <sup>fi</sup>rm in question is analyzed based on this domain knowledge learned from the previous step. Certain detection strategy is formed accordingly and the data is further analyzed using data mining techniques.

To realize the general model described above and to catch the real world dynamics and possible new methods to commit <sup>fi</sup>nancial statement fraud, we propose an adaptive learning framework (Fig. 3). We consider, but are not limited to, exogenous parameters described in existing literature, such as capital structure, conditions, choices, management attitudes, etc. The mechanism works as follows: based on external and internal economical circumstances, management chooses their action on whether or not to commit <sup>fi</sup>nancial statement fraud at the year end. Financial data and statements of concern are audited and examined by a fraud detection unit. Resulting audit reports are further evaluated and learned by a self-adaptive module to collect relevant patterns and trends of each company in different industries. In the meanwhile, an adaptive fraud discovery module keeps evolving with exogenous parameters to discover unknown but possible pattern of <sup>fi</sup>nancial statement fraud. New discoveries were also evaluated and learned to prepare the knowledge base for future fraud detection.

![](/api/attachments/V2B5WKM6/fulltext/images/3d4b7ff8f78f5ebc9baee308b5eb7f91770a699498631f9f5ef3bf519d42725d.jpg)  
Fig. 2. Proposed two-stage framework.

To increase detection relevancy and to reduce computational complexity, we also propose adaptive feature selection that <sup>fi</sup>ts speci<sup>fi</sup>c domain to choose the proper parameters for companies with similar internal and external <sup>fi</sup>nancial environment [13]. Once relevant parameters are selected, we opt to proper methodology and data mining technique to detect <sup>fi</sup>nancial fraud that evolves. As discussed in the previous section, no single data mining-based FSF detection technique is perfect and each of them is subject to its own handicaps. We propose response surface methodology to construct the foundation in order to <sup>fi</sup>nd the right data mining-based detection technique.

## 5.2. Adaptive financial fraud detection with RSM

Response Surface Methodology (RSM), a method for constructing global approximations to system behavior based on results calculated at various points in the design space [23], is a natural <sup>fi</sup>t to estimate the relationships between the variables and the <sup>fi</sup>nancial statement fraud techniques. RSM provides statistically validated predictive models that can be manipulated for <sup>fi</sup>nding the probability of different forms of possible <sup>fi</sup>nancial statement frauds.

RSM is extensively applied in various situations where output performance or service quality, which is called response, is in<sup>fl</sup>uenced by a list of several input variables, which may or may not be complete and are called independent variables. Independent variables are subject to the control of the experiment designer. Approximation of the relationship between the response and independent variables can be visualized by RSM, which consists of three factors: (1) the experimental strategy for exploring the space of independent variables, (2) empirical statistical modeling to develop an appropriate approximating relationship between the response and the independent variables, and (3) optimization methods for <sup>fi</sup>nding the values of the process variables that produce desirable values of response.

Theoretically, the appropriate approximating model between the response y and independent variables $x _ { 1 } , x _ { 2 } , . . . x _ { n }$ can be constructed as $y = f ( x _ { 1 } , x _ { 2 } , . . . x _ { n } ) + \varepsilon ,$ where the form of the true real-time response function f is unknown and may be complex. ε, which usually includes measurement error on response and other unpredictable noise, is a random term that represents the variability not caught by the response function. If we assume that it has a normal distribution with zero mean, $Y { = } E ( y ) { = } f ( x _ { 1 } , x _ { 2 } { , } { . . . } x _ { n } )$ . With the form of the true response function f kept unknown, the designer has to approximate it and further utilize it to locate the possible response with discovered independent variables.

Feature selection can be implemented to identify a relevant list of variables that the designer may further utilize to construct the response surface. Once we have a <sup>fi</sup>rm in question, we are able to <sup>fi</sup>nd the possibility of certain <sup>fi</sup>nancial statement frauds based on the response surface estimation. Then, we select data mining techniques that suit the pro<sup>fi</sup>le that we have learned from the previous step.

RSM provides statistical tools for analysis of historical data and selection of variables aimed at better prediction. The objectives for using RSM in the context of <sup>fi</sup>nancial statement fraud detection are to <sup>fi</sup>nd the optimum response and to understand how the response changes in a given direction by adjusting the design variables [17]. When there are constraints on the design data, then the variable selection and experimental design has to meet requirements of the constraints. In general, the response surface can be visualized graphically and the graph, if in fewer than three dimensions, is helpful to navigate over the response surface to reach the desired outcome.

![](/api/attachments/V2B5WKM6/fulltext/images/73e6464dc75c151171c7d6ef47795275231b771d501ff2092a6c6edf662995a7.jpg)  
Fig. 3. FSF detection strategy selection to detect adaptive <sup>fi</sup>nancial

In a simple form, a function $f ( x _ { 1 } , x _ { 2 } )$ can be plotted versus the levels of x and x , and this three-dimensional graph forms a response surface plot (Fig. 3). This <sup>fi</sup>gure shows an adaptive learning framework to detect evolutionary <sup>fi</sup>nancial statement frauds using a response surface method (Fig. 4). We proceed by <sup>fi</sup>rst selecting relevant variables that could either be the three parameters in the CMA model [15], the parameters in a 3C's model [19], a mixture from both models, or any other parameters that have some causal relationship to <sup>fi</sup>nancial statement frauds. The selected variables are denoted as

$$
V _ {a}, V _ {b}, \dots V _ {n}\tag{2}
$$

respectively, so the probability of committing <sup>fi</sup>nancial statement fraud in the form of k can be described as Eq. (2) that is subject to Eqs. (3) and $4 ( 4 )$ . We assume that the <sup>fi</sup>rst n forms of <sup>fi</sup>nancial statement fraud have been discovered and that the number of possible forms is in<sup>fi</sup>nity, such that

$$
P (F S F _ {k}) = f (V _ {a}, V _ {b}, \dots V _ {n})\tag{3}
$$

which is subject to

$$
\sum_ {k = 1} ^ {n} P (F S F _ {k}) <   1.\tag{4}
$$

## 6. Conclusion

In recent years, data mining has gained widespread attention and increasing popularity in the <sup>fi</sup>nancial world. Successful data mining applications have been reported and recent surveys have found that data mining has grown in usage and effectiveness. Professional accounting bodies have also identi<sup>fi</sup>ed data mining as an important technology for the new century. Implementing straightforward data mining techniques to discover <sup>fi</sup>nancial statement fraud, however, has many disadvantages and limits of usage. After exhaustive literature review, we <sup>fi</sup>nd that a majority of existing data mining techniques to detect <sup>fi</sup>nancial fraud have their domain of usage and limitations.

Furthermore, when <sup>fi</sup>nancial statement fraudsters have found ways to circumvent the automatic detection programs, there is an urgent need for a mechanism that is able to learn and use the industrial domain knowledge to facilitate the data mining techniques. We propose such a framework that is based on the response surface method to automatically pivot the program in accordance with the unique circumstances of the <sup>fi</sup>rm in question. Unlike traditional <sup>fi</sup>nancial fraud detection techniques that are based on historical <sup>fi</sup>nancial data, we further propose an innovative way, the active discovery module that evolves ahead of possible fraudsters. Preparing the intelligent detection system in anticipation before any unknown or future fraud happens enables us to effectively detect <sup>fi</sup>nancial statement frauds that adapt.

Future research is needed to design the active discovery module that is both effective and ef<sup>fi</sup>cient. Furthermore, although we have suggested the response surface method to extract the domain knowledge and to adaptively learn the changes from fraudsters, there may exist alternatives that have equal or better performance than the RSM. Research is also needed to examine the circumstances under which our suggested framework performs better than other techniques.

![](/api/attachments/V2B5WKM6/fulltext/images/eda16d58dad5fb2377e0fd2443140e120e82d53d66b80fa2da81652f4e2e4c1c.jpg)  
Fig. 4. Adaptive learning and detecting <sup>fi</sup>nancial statement fraud using a response surface method.

## References

[1] M.S. Beasley, An empirical analysis of the relation between the board of director composition and <sup>fi</sup>nancial statement fraud, The Accounting Review of Finance 71 (4) (1996) 443–465.

[2] M.S. Beasley, J.V. Carcello, D.R. Hermanson, Fraudulent Financial Reporting 1987–1991: An Analysis of U.S. Public Companies, The CoSo Report, 1999.

[3] T.B. Bell, J.V. Carcello, A Decision aid for assessing the likelihood of fraudulent <sup>fi</sup>nancial reporting, Auditing 19 (1) (2000) 169–184

[4] R.A. Bernardi, Fraud detection: the effect of client integrity and competence and auditor cognitive style, Auditing: A Journal of Practice & Theory, Supplement 13 (1994) 68–84.

[5] R.J. Bolton, D.J. Hand, Statistical fraud detection: A review, Statistical Science 17 (3) (2002) 235–249.

[6] W.-S. Chen, Y.-K. Du, Using neural networks and data mining techniques for the <sup>fi</sup>nancial distress prediction model, Expert Systems with Applications Part 2 36 (2) (March 2009) 4075–4086.

[7] Deloitte, Ten things about <sup>fi</sup>nancial statement fraud: a review of SEC enforcement releases 2000–2006, Deloitte Forensic Center, June 2007.

[8] Y. Dianmin, W. Xiaodan, W. Yunfeng, L. Yue, C. Chao-Hsien, A review of data mining-based <sup>fi</sup>nancial fraud detection research, International Conference on Wireless Communications, Networking and Mobile Computing, 2007, pp. 5519–5522.

[9] K. Fanning, K.O. Cogger, R. Srivastava, Detection of management fraud: a neural network approach, 11th Conference on Arti<sup>fi</sup>cial Intelligence for Applications 1995, pp. 220–223.

[10] E.H. Feroz, M.K. Taek, V.S. Pastena, K. Park, The Ef<sup>fi</sup>cacy of red <sup>fl</sup>ags in predicting the sec's targets: an arti<sup>fi</sup>cial neural networks approach, International Journal of Intelligent Systems in Accounting, Finance & Management 9 (2000) 145–157.

[11] J.V. Hansen, J.B. McDonald, W.F. Messier, A generalized qualitative-response model and the analysis of management fraud, Management Science 42 (1997) 1022–1032.

[12] E. Kirkos, C. Spathis, Y. Manolopoulos, Data mining techniques for the detection of fraudulent <sup>fi</sup>nancial statements, Expert Systems with Applications 32 (4) (2007) 995–1003.

[13] H.C. Koh, C.K. Low, Going concern prediction using data mining techniques, Managerial Auditing Journal 19 (3) (2004) 462–476.

[14] K.O.C., Kurt M. Fanning, Neural network detection of management fraud using published <sup>fi</sup>nancial data, Intelligent Systems in Accounting, Finance & Management 7 (1) (1998) 21–41.

[15] J.K. Loebbecke, M.M. Eining, J.J. Willingham, Auditors' experience with material irregularities: frequency, Nature, and Detectability, Auditing: A Journal of Practice and Theory 9 (1989) 1–28.

[16] M.D. Odom, R. Sharda, A neural network model for bankruptcy prediction, IJCNN International Joint Conference on Neural Networks, 1990, pp. 163–168.

[17] G.W. Oehlert, Design and Analysis of Experiments: Response Surface Design, W.H. Freeman and Company, New York, 2000.

[18] O. Persons, Using <sup>fi</sup>nancial statement data to identify factors associated with fraudulent <sup>fi</sup>nancing reporting, Journal of Applied Business Research 11 (1995) 38–46.

[19] Z. Rezaee, Financial Statement Fraud-Prevention and Detection, John Wiley & Sons, Inc., 2002

[20] H.M. Schilit, Financial Shenanigans, McGraw-Hill, New York, NY, 2002

[21] C. Spathis, Detecting false <sup>fi</sup>nancial statements using published. data: some evidence from Greece, Managerial Auditing Journal 17 (4) (2002) 179–191.

[22] C. Spathis, M. Doumpos, C. Zopounidis, Detecting falsi<sup>fi</sup>ed <sup>fi</sup>nancial statements: a comparative study using multicriteria analysis and multivariate statistical techniques, European Accounting Review 11 (3) (2002) 509–535.

[23] N.S.R.T.H., W.J. Roux, Response surface approximations for structural optimization, 1998, pp. 517–534.

[24] H. White, Learning in arti<sup>fi</sup>cial neural networks: a statistical perspective, Neural Computation 1 (1989) 425–464.

![](/api/attachments/V2B5WKM6/fulltext/images/71ab5841066287e3e27f2fe0595fd019720f151153888049fa0fb23faca6525b.jpg)

Wei Zhou is an Assistant Professor in the Information and Operations Management department at ESCP Europe. His research interests include Internet advertising, RFID — enabled item-level information visibility, data mining and its application in supply chain management. His work has appeared in Decision Support Systems, European Journal of Information Systems, European Journal of Operational Research, IEEE transaction on Geosciences and Remote Sensing, International Journal of Electronic Commerce and Optical Engineering, among others.

Gaurav Kapoor received his Ph.D. in Information Systems from the University of Florida. His research interests include RFID systems.
