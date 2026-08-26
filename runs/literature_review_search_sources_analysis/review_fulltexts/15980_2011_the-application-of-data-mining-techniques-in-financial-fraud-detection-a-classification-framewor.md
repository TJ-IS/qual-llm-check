---
otero_id: 15980
otero_key: "S2EV9SE8"
title: "The application of data mining techniques in financial fraud detection: A classification framework and an academic review of literature"
authors: "E.W.T. Ngai; Yong Hu; Y.H. Wong; Yijun Chen; Xin Sun"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.08.006"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# The application of data mining techniques in <sup>fi</sup>nancial fraud detection: A classi<sup>fi</sup>cation framework and an academic review of literature

E.W.T. Ngai <sup>a</sup>, Yong Hu <sup>b,</sup>⁎, Y.H. Wong <sup>a</sup>, Yijun Chen <sup>b</sup>, Xin Sun <sup>b</sup>

<sup>a</sup> Department of Management and Marketing, The Hong Kong Polytechnic University, Kowloon, Hong Kong, PR China

<sup>b</sup> Institute of Business Intelligence and Knowledge Discovery, Department of E-commerce, Guangdong University of Foreign Studies, Sun Yat-Sen University, Guangzhou 510006, PR China

## a r t i c l e i n f o

Available online 19 August 2010

Keywords: Financial fraud Fraud detection Literature review Data mining Business intelligence

## a b s t r a c t

This paper presents a review of — and classi<sup>fi</sup>cation scheme for — the literature on the application of data mining techniques for the detection of <sup>fi</sup>nancial fraud. Although <sup>fi</sup>nancial fraud detection (FFD) is an emerging topic of great importance, a comprehensive literature review of the subject has yet to be carried out. This paper thus represents the <sup>fi</sup>rst systematic, identi<sup>fi</sup>able and comprehensive academic literature review of the data mining techniques that have been applied to FFD. 49 journal articles on the subject published between 1997 and 2008 was analyzed and classi<sup>fi</sup>ed into four categories of <sup>fi</sup>nancial fraud (bank fraud, insurance fraud, securities and commodities fraud, and other related <sup>fi</sup>nancial fraud) and six classes of data mining techniques (classi<sup>fi</sup>cation, regression, clustering, prediction, outlier detection, and visualization). The <sup>fi</sup>ndings of this review clearly show that data mining techniques have been applied most extensively to the detection of insurance fraud, although corporate fraud and credit card fraud have also attracted a great deal of attention in recent years. In contrast, we <sup>fi</sup>nd a distinct lack of research on mortgage fraud, money laundering, and securities and commodities fraud. The main data mining techniques used for FFD are logistic models, neural networks, the Bayesian belief network, and decision trees, all of which provide primary solutions to the problems inherent in the detection and classi<sup>fi</sup>cation of fraudulent data. This paper also addresses the gaps between FFD and the needs of the industry to encourage additional research on neglected topics, and concludes with several suggestions for further FFD research.

Crown Copyright © 2010 Published by Elsevier B.V. All rights reserved.

## 1. Introduction

In recent years, <sup>fi</sup>nancial fraud, including credit card fraud, corporate fraud and money laundering, has attracted a great deal of concern and attention. The Oxford English Dictionary [55], p. 562] de<sup>fi</sup>nes fraud as “wrongful or criminal deception intended to result in <sup>fi</sup>nancial or personal gain.” Phua et al. [58] describe fraud as leading to the abuse of a pro<sup>fi</sup>t organization's system without necessarily leading to direct legal consequences. Although there is no universally accepted de<sup>fi</sup>nition of <sup>fi</sup>nancial fraud, Wang et al. [78], p. 1120] de<sup>fi</sup>ne it as “a deliberate act that is contrary to law, rule, or policy with intent to obtain unauthorized <sup>fi</sup>nancial bene<sup>fi</sup>t.”

Economically, <sup>fi</sup>nancial fraud is becoming an increasingly serious problem. A striking case in point is the Ponzi scheme perpetuated by former NASDAQ chairman Bernard Madoff, which has led to the loss of approximately US\$50 billion worldwide [34]. Another example is that of Joseph Hirko, former co-chief executive of<sup>fi</sup>cer of Enron Broadband

Services (EBS), who has avowed to forfeit approximately US \$8.7 million in restitution to Enron victims through the U.S. Securities and Exchange Commission's Enron Fair Fund after pleading guilty to wire fraud [34]. According to a 2007 BBC news report [8], fraudulent insurance claims cost UK insurers a total of 1.6 billion pounds a year. The overall losses caused by <sup>fi</sup>nancial fraud are incalculable.

Financial fraud detection (FFD) is vital for the prevention of the often devastating consequences of <sup>fi</sup>nancial fraud. FFD involves distinguishing fraudulent <sup>fi</sup>nancial data from authentic data, thereby disclosing fraudulent behavior or activities and enabling decision makers to develop appropriate strategies to decrease the impact of fraud.

Data mining plays an important role in FFD, as it is often applied to extract and uncover the hidden truths behind very large quantities of data. Bose and Mahapatra [14] de<sup>fi</sup>ne data mining as a process of identifying interesting patterns in databases that can then be used in decision making. Turban et al. [73] de<sup>fi</sup>ne data mining as a process that uses statistical, mathematical, arti<sup>fi</sup>cial intelligence, and machinelearning techniques to extract and identify useful information and subsequently gain knowledge from a large database. Frawley et al. [35] state that the objective of data mining is to obtain useful, non-explicit information from data stored in large repositories. Kou et al. [47] highlight that an important advantage of data mining is that it can be used to develop a new class of models to identify new attacks before they can be detected by human experts. Phua et al. [58] point out that fraud detection has become one of the best established applications of data mining in both industry and government. Various data mining techniques have been applied in FFD, such as neural networks [18,27,31,38,45,75], logistic regression models [10,54,65,85], the naïve Bayes method [11,77], and decision trees [45,46], among others.

Over the past few years, a number of review articles have appeared in conference or journal publications. Bolton and Hand [13], for example, have reviewed statistical methods of detecting fraud, including credit card fraud, money laundering, telecommunications fraud, etc. Zhang and Zhou [88] have surveyed <sup>fi</sup>nancial applications of data mining including stock market and bankruptcy predictions and fraud detection. Phua et al. [58] present a survey of data mining-based fraud detection research, including credit transaction fraud, telecoms subscription fraud, automobile insurance fraud and the like. Others have reviewed insurance fraud [24] and <sup>fi</sup>nancial statement fraud [86]. However, the survey presented herein is an up-to-date, comprehensive and state-of-the-art review of data mining applications in FFD.

This paper has three objectives. The <sup>fi</sup>rst is to develop a framework for classifying the applications of data mining to FFD. The second is to provide a systematic and comprehensive review of existing research articles on the applications of data mining to FFD. The third is to use the review and framework to generate a roadmap for researchers and practitioners seeking to better comprehend this <sup>fi</sup>eld.

The remainder of this article is structured as follows. Section 2 presents the methodological framework for research. Section 3 provides our classi<sup>fi</sup>cation framework for the application of data mining in FFD. Section 4 analyzes FFD research according to this classi<sup>fi</sup>cation framework. Section 5 concludes our research and suggests further research directions.

## 2. Methodological framework for research

The methodological framework for this research can be divided into three essential phases: research de<sup>fi</sup>nition, research methodology, and research analysis, as depicted in Fig. 1.

In phase 1, we determine the research area, the expected research goal, and the research scope. The research area is academic research on

FFD that applies data mining techniques. The research goal is to create a classi<sup>fi</sup>cation framework for the data mining techniques applied to FFD and to suggest directions for future research. The research scope is the literature on the applications of data mining to FFD published between 1997 and 2008, which is summarized to aid the further creation and accumulation of knowledge in this area. As the research on this topic is relatively recent, the scope of this investigation is limited to the time frame of 1997 to 2008, but this 12-year period is deemed to be representative of the application of data mining to FFD.

In phase 2, we de<sup>fi</sup>ne the criteria for searching for and selecting articles, and create a framework to classify the selected articles. Nine online academic databases were searched to provide a comprehensive listing of journal articles, as the nature of FFD and data mining research makes it dif<sup>fi</sup>cult to con<sup>fi</sup>ne the search to speci<sup>fi</sup>c disciplines. These databases cover most academic journals in English available in full text versions.

• ABI/INFORM Database

• Academic Search Premier

• ACM

• Business Source Premier

• Emerald Full text

• IEEE Transactions

• Science Direct

• Springer-Link Journals

• World Scienti<sup>fi</sup>c Net

This literature search was based on the descriptors “<sup>fi</sup>nancial fraud,” “data mining” and “business intelligence.” We used Boolean expressions to apply these terms to a search of online databases, which originally produced approximately 1200 articles. The review and classi<sup>fi</sup>cation process was carefully and independently veri<sup>fi</sup>ed by the co-authors, and only articles that were related to data mining and FFD were included. Each article was carefully examined to ensure that it met the three selection criteria. First, the articles must have been published in academic journals for which the full text versions are available. Conference articles, master or doctoral dissertations, textbooks, and unpublished working papers were excluded, largely for reasons of availability. Second, the articles had to have been published between 1997 and 2008. Third, the articles had to present data mining techniques and discuss their application to <sup>fi</sup>nancial fraud.

![](/api/attachments/S2EV9SE8/fulltext/images/a747c0af679e0eef36759ce76c7659359a892074139a2b97e8c2a1e6e26e432c.jpg)  
Fig. 1. Methodological framework for research.

Forty-nine articles were selected for classi<sup>fi</sup>cation. Each was classi<sup>fi</sup>ed according to the following steps [53].

• Classify the articles selected by one of the co-authors.

• Verify the classi<sup>fi</sup>cation with another co-author and double check with another independent co-author.

• Approve the categories assigned to the article if the classi<sup>fi</sup>cation results are consistent, or hold a discussion among the researchers to reach a consensus otherwise.

In the last phase, we analyzed the selected articles to draw some conclusions and identify some future research directions. The details of the analysis are presented in Section 4.

## 3. Classi<sup>fi</sup>cation framework on data mining and <sup>fi</sup>nancial fraud detection

In this section, we propose a graphical conceptual classi<sup>fi</sup>cation framework for the available literature on the applications of data mining techniques to FFD. The classi<sup>fi</sup>cation framework, which is shown in Fig. 2, is based on a literature review of existing knowledge on the nature of data mining research [3,52], fraud detection research [13,24,58,86,88], and the <sup>fi</sup>nancial crime framework of the U.S. Federal Bureau of Investigation [33] which is summarized and presented in Table 1.

Our proposed classi<sup>fi</sup>cation framework for <sup>fi</sup>nancial fraud is based on the <sup>fi</sup>nancial crime framework of the U.S. Federal Bureau of Investigation [33], because it is one of the best established frameworks for FFD. The classi<sup>fi</sup>cation of <sup>fi</sup>nancial fraud comprises two levels, as shown in Table 1. The higher level comprises financial fraud based (FF-based) categories, which include bank fraud, insurance fraud, securities and commodities fraud, and other related <sup>fi</sup>nancial fraud, whereas the lower level comprises fraudulent activities, including mortgage fraud, asset forfeiture/money laundering, healthcare fraud, insurance fraud, securities and commodities fraud, corporate fraud, and mass marketing fraud.

Fig. 2 consists of two layers, the <sup>fi</sup>rst comprising the aforementioned <sup>fi</sup>nancial fraud based categories and the second comprising the six data mining application classes of classi<sup>fi</sup>cation, clustering, prediction, outlier detection, regression, and visualization [13,24,32,48,58,61,74,76], supported by a set of algorithmic approaches to extract the relevant relationships in the data [73]. We provide a brief description of our conceptual framework with references, and of the six data mining application classes (classi<sup>fi</sup>cation, clustering, outlier detection, prediction, regression and visualization), each component of which is discussed in more detail in the following sections.

![](/api/attachments/S2EV9SE8/fulltext/images/1d7b71a78d4ace941f5a6b3cb79f1931059231587390af001750fa2c54c32417.jpg)  
Fig. 2. Conceptual framework for classifying the applications of data mining to FFD.

Table 1  
Classi<sup>fi</sup>cation for <sup>fi</sup>nancial fraud based on FBI [33].

<table><tr><td>Financial fraud based categories</td><td>Fraudulent activities</td></tr><tr><td>Bank fraud</td><td>Mortgage fraud, Asset forfeiture/money laundering</td></tr><tr><td>Insurance fraud</td><td>Healthcare fraud, Insurance fraud</td></tr><tr><td>Securities and commodities fraud</td><td>Securities and commodities fraud</td></tr><tr><td>Other related financial fraud</td><td>Corporate fraud, Mass marketing fraud</td></tr></table>

## 3.1. Classification for financial fraud

As previously mentioned, in this study, <sup>fi</sup>nancial fraud is classi<sup>fi</sup>ed into four broad categories. They are:

Bank fraud. According to Connell University Law School (CULS) [22], bank fraud is de<sup>fi</sup>ned as “whoever knowingly executes, or attempts to execute, a scheme or arti<sup>fi</sup>ce (1) to defraud a <sup>fi</sup>nancial institution; or (2) to obtain any of the moneys, funds, credits, assets, securities, or other property owned by, or under the custody or control of, a <sup>fi</sup>nancial institution, by means of false or fraudulent pretenses, representations, or promises.”

In this study, bank fraud includes credit card fraud, money laundering, and mortgage fraud, where mortgage fraud is de<sup>fi</sup>ned as “material misstatement, misrepresentation, or omission relating to the property or potential mortgage relied on by an underwriter or lender to fund, purchase or insure a loan” [33] and credit card fraud is de<sup>fi</sup>ned as the unauthorized usage of a card, unusual transaction behavior, or transactions on an inactive card [70]. According to the FBI [33], money laundering is the process by which criminals conceal or disguise the proceeds of their crimes or convert those proceeds into goods and services. It allows criminals to inject their illegal money into the stream of commerce, thus corrupting <sup>fi</sup>nancial institutions and the money supply and giving criminals unwarranted economic power. Gao and Ye [36] similarly de<sup>fi</sup>ne money laundering as the process by which criminals “wash dirty money” to disguise its illicit origin and make it appear legitimate and “clean.”

Insurance fraud. Insurance fraud can occur at many points in the insurance process (e.g., application, eligibility, rating, billing, and claims), and can be committed by consumers, agents and brokers, insurance company employees, healthcare providers, and others [21,44]. In this study, insurance fraud includes crop, healthcare, and automobile insurance fraud. FBI [33] states that healthcare fraud is carried out by many segments of the healthcare system using various methods, with some of the most prevalent types of fraud including “Billing for Services not Rendered, Upcoding of Services, Upcoding of Items, Duplicate Claims, Unbundling, Excessive Services, Medically Unnecessary Services and Kickbacks” [33]. Crop insurance fraud is committed by purchasers of crop insurance who fake or overstate either the loss of their crops due to natural disasters or the loss of revenue due to declines in the price of agricultural commodities. Automobile insurance fraud comprises a set of fraudulent activities that include staged accidents, super<sup>fl</sup>uous repairs, and faked personal injuries.

Securities and commodities fraud. The FBI [33] provides brief descriptions of some of the most prevalent securities and commodities frauds encountered today, for example, “Market Manipulation, High Yield Investment Fraud, The Ponzi Scheme,

The Pyramid Scheme, Prime Bank Scheme, Advance Fee Fraud, Hedge Fund Fraud, Commodities Fraud, Foreign Exchange Fraud, Broker Embezzlement and Late-Day Trading.” According to another de<sup>fi</sup>nition by CULS [22], securities frauds include theft from manipulation of the market, theft from securities accounts, and wire fraud.

Other related <sup>fi</sup>nancial fraud. Our <sup>fi</sup>nal category is made up of types of <sup>fi</sup>nancial fraud other than those in the aforementioned categories, such as corporate fraud and mass marketing fraud. Again, according to FBI [33], “corporate fraud investigations involve the following activities: (1) falsi<sup>fi</sup>cation of <sup>fi</sup>nancial information, (2) self-dealing by corporate insiders, and (3) obstruction of justice designed to conceal any of the abovenoted types of criminal conduct.” The Bureau further states that “mass marketing fraud is a general term for types of fraud that exploit mass-communication media, such as telemarketing, mass mailings, and the Internet.”

## 3.2. Classification of data mining applications and techniques

Each of the six data mining application classes is supported by a set of algorithmic approaches to extract the relevant relationships in the data [73]. These approaches differ in the classes of problems that they are able to solve (see [40]). The classes are as follows.

Classi<sup>fi</sup>cation. Classi<sup>fi</sup>cation builds up and utilizes a model to predict the categorical labels of unknown objects to distinguish between objects of different classes. These categorical labels are prede<sup>fi</sup>ned, discrete and unordered [39,71]. Zhang and Zhou [88] state that classi<sup>fi</sup>cation and prediction is the process of identifying a set of common features and models that describe and distinguish data classes or concepts. Common classi<sup>fi</sup>cation techniques include neural networks, the naïve Bayes technique, decision trees and support vector machines. Such classi<sup>fi</sup>cation tasks are used in the detection of credit card, healthcare and automobile insurance, and corporate fraud, among other types of fraud, and classi<sup>fi</sup>cation is one of the most common learning models in the application of data mining in FFD.

Clustering. Clustering is used to divide objects into conceptually meaningful groups (clusters), with the objects in a group being similar to one another but very dissimilar to the objects in other groups. Clustering is also known as data segmentation or partitioning and is regarded as a variant of unsupervised classi<sup>fi</sup>cation [39,71]. According to Yue et al. [86], p. 5520], “clustering analysis concerns the problem of decomposing or partitioning a data set (usually multivariate) into groups so that the points in one group are similar to each other and are as different as possible from the points in other groups.” Further, Zhang and Zhou [88] argue that each cluster is a collection of data objects which are similar to one another within the same cluster but dissimilar to those in other clusters. The most common clustering techniques are the K-nearest neighbor, the Naïve Bayes technique and self-organizing map techniques.

Prediction. Prediction estimates numeric and ordered future values based on the patterns of a data set [3,12]. Han and Kamber [39] note that, for prediction, the attribute for which the values are being predicted is continuous-valued (ordered) rather than categorical (discrete-valued and unordered). This attribute can be referred to simply as the predicted attribute. Neural networks and logistic model prediction are the most commonly used prediction techniques.

Outlier detection. Outlier detection is employed to measure the “distance” between data objects to detect those objects that are grossly different from or inconsistent with the remaining data set [39]: “Data that appear to have different characteristics than the rest of the population are called outliers” [2], p. 521]. Yamanishi et al. [82] point out that the problem of outlier/anomaly detection is one of the most fundamental issues in data mining. A commonly used technique in outlier detection is the discounting learning algorithm.

Regression. Regression is a statistical methodology used to reveal the relationship between one or more independent variables and a dependent variable (that is continuous-valued) [39]. Many empirical studies have used logistic regression as a benchmark [1,28,62,76,79]. The regression technique is typically undertaken using such mathematical methods as logistic regression and linear regression, and it is used in the detection of credit card, crop and automobile insurance, and corporate fraud.

Visualization. Visualization refers to the easily understandable presentation of data and to methodology that converts complicated data characteristics into clear patterns to allow users to view the complex patterns or relationships uncovered in the data mining process [63,73]. Eick and Fyock [29] report that researchers at Bell and AT&T Laboratories have exploited the pattern detection capabilities of the human visual system by building a suite of tools and applications that <sup>fl</sup>exibly encode data using color, position, size and other visual characteristics. Visualization is best used to deliver complex patterns through the clear presentation of data or functions.

## 4. Analysis of FFD research based on the proposed classi<sup>fi</sup>cation framework

This paper provides a state-of-the-art review of the applications of data mining to FFD. Fig. 3, which is based on Fig. 2, dissects and organizes this review of the literature. For the classi<sup>fi</sup>cation of <sup>fi</sup>nancial fraud, we divide the articles among the categories of bank fraud, insurance fraud, securities and commodities fraud, and other related <sup>fi</sup>nancial fraud. In the second level of the classi<sup>fi</sup>cation, we make a further categorization based on fraudulent activities (e.g., asset forfeiture/money laundering). For the data mining classi<sup>fi</sup>cation, we <sup>fi</sup>rst identify six data mining application classes, and then in the second level of classi<sup>fi</sup>cation make a further categorization using a set of algorithmic approaches (e.g., neural networks).

The distribution of the 49 articles classi<sup>fi</sup>ed into the proposed classi<sup>fi</sup>cation framework is given in Table 2. Table 2 lists the applications of data mining to FFD by the FF-based categories and fraudulent activities, and identi<sup>fi</sup>es the data mining application classes and techniques used with reference to the problems addressed. Some of the selected applications in the review address more than one FDD problem, and thus we categorized these applications by the dominant problem addressed.

A complete list of the 49 selected articles is presented in Tables 3–5. The <sup>fi</sup>rst column of Tables 3–5 present the important literature studied in our research. The second column gives a brief description of the articles and their main objectives. The following subsections present further analysis of data mining techniques in FFD.

## 4.1. Distribution of articles by data mining application classes

The classi<sup>fi</sup>cation of the 49 articles by data mining application classes is shown in Table 6.

Judging by the numbers of published papers (see Table 6), we can clearly see that the focus of data mining applications has most often been on automobile insurance fraud and corporate fraud (17 or 34.7% each), followed by credit card fraud (7 or 14.3%). Overall, insurance fraud is the most prominent area for the application of data mining techniques in FFD (49%). It is worth noting that there is no published article related to mortgage fraud, securities and commodities fraud and mass marketing fraud within our selection criteria; thus they are not listed in the above-mentioned table.

![](/api/attachments/S2EV9SE8/fulltext/images/9b5147de755fa21360afcd7c07bb80c5f0f78a89de5aaebca1e478b6f165d457.jpg)  
Fig. 3. Framework for dissection and organization of the review of articles.

It can be clear that classi<sup>fi</sup>cation is the most frequently used data mining application class, accounting for 61.2% of the total (30 of the 49 articles), and that outlier detection and visualization are the least common, accounting for only 2.0% each (1 out of 49 each). Given that outlier detection is a signi<sup>fi</sup>cant method of fraud detection, which has characteristics that confer comparative advantages over other techniques, more attention should be paid to it in future research.

## 4.2. Distribution of articles by data mining techniques

To determine the main algorithms used for FFD, we present a simple analysis of FFD and the data mining techniques identi<sup>fi</sup>ed in the articles in Table 7. Twenty-six data mining techniques have been applied to the detection of <sup>fi</sup>nancial fraud. Mortgage fraud, securities and commodities fraud, and mass marketing fraud are not listed in the table because the techniques identi<sup>fi</sup>ed in our research have not been applied to these problems. The most frequently used techniques are logistic models, neural networks, the Bayesian belief network, and decision trees, all of which fall into the “classi<sup>fi</sup>cation” category. Of these techniques, logistic models are the most popular, being used in 21.3% (16 of 75) of the studies reviewed, followed by neural networks, used in 13.3% (10 of 75), and then the Bayesian belief network and decision trees, both used in 6.7% (5 of 75) of studies. These four techniques are discussed in more detail in the following paragraphs.

Logistic model. Logistic model is a generalized linear model that is used for binomial regression in which the predictor variables can be either numerical or categorical [65,84]. It is principally used to solve problems caused by automobile insurance and corporate fraud.

Neural networks. The neural network is a technique that imitates the functionality of the human brain using a set of interconnected vertices [37,84]. It is widely applied in classi<sup>fi</sup>cation and clustering, and its advantages are as follows. First, it is adaptive; second, it can generate robust models; and third, the classi<sup>fi</sup>cation process can be modi<sup>fi</sup>ed if new training weights are set. Neural networks are chie<sup>fl</sup>y applied to credit card, automobile insurance and corporate fraud.

Bayesian belief network. The Bayesian belief network (BBN) represents a set of random variables and their conditional independencies using a directed acyclic graph (DAG), in which nodes represent random variables and missing edges encode conditional independencies between the variables [45,57]. The Bayesian belief network is often adopted in credit card, automobile insurance, and corporate fraud detection.

Decision trees. Decision trees are predictive decision support tools that create mapping from observations to possible consequences [39,49]. These trees can be planted via machine-learning-based algorithms such as the ID3, CART and C4.5. Predictions are represented by leaves, and the conjunctions of features by branches. Decision trees are commonly used in credit card, automobile insurance, and corporate fraud.

Table 3 Bank fraud  
Table 2  
Research on data mining techniques in FFD.

<table><tr><td>FF-based categories</td><td>Fraudulent activities</td><td>Data mining application class</td><td>Data mining techniques</td><td>References</td></tr><tr><td rowspan="2">Bank fraud</td><td rowspan="2">Credit card fraud</td><td>Classification</td><td>Ada boost algorithm, decision trees, CART, RIPPER, Bayesian Belief Network, Neural networks, discriminant analysisK-nearest neighbor, logistic model, discriminant analysis, Naïve Bayes, neural networks, decision treesSupport vector machine, evolutionary algorithms</td><td>[19][27][84]</td></tr><tr><td>Clustering</td><td>Hidden Markov ModelSelf-organizing map</td><td>[20][67][60,87]</td></tr><tr><td rowspan="8">Insurance fraud</td><td>Money laundering</td><td>Classification</td><td>Network analysis</td><td>[36]</td></tr><tr><td>Crop insurance fraud</td><td>Regression</td><td>Yield-switching modelLogistic model, probit model</td><td>[6][43]</td></tr><tr><td rowspan="3">Healthcare insurance fraud</td><td>Classification</td><td>Association rulePolymorphous (M-of-N) logicSelf-organizing map</td><td>[83][51][41]</td></tr><tr><td>Visualization</td><td>Visualization</td><td>[64]</td></tr><tr><td>Outlier detection</td><td>Discounting learning algorithm</td><td>[82]</td></tr><tr><td rowspan="3">Automobile insurance fraud</td><td>Classification</td><td>Logistic modelNeural networksPrincipal component analysis of RIDIT(PRIDIT)Logistic modelLogistic model, decision trees, neural networks, support vector machine,K-nearest neighbor, Naïve Bayes, Bayesian belief networkFuzzy logicLogistic modelLogistic model, Bayesian belief networkSelf-organizing mapNaïve Bayes</td><td>[17][75][16][74][76]</td></tr><tr><td>Prediction</td><td>Evolutionary algorithmsLogistic modelProbit modelLogistic modelProbit model</td><td>[56][4,5][11][15][77]</td></tr><tr><td>Regression</td><td>Probit modelLogistic modelProbit model</td><td>[68][72][59][23,80][9]</td></tr><tr><td rowspan="4">Other related financial fraud</td><td rowspan="4">Corporate fraud</td><td>Classification</td><td>Neural networks, decision trees, Bayesian belief networkMulticriteria decision aid (MCDA), UTilite&#x27;s Additives DIScriminantes (UTADIS)Evolutionary algorithmsFuzzy logicNeural networksNeural networks, logistic modelLogistic modelCARTDecision trees, neural networks, Bayesian belief network, K-nearest neighbor,RIPPER, support vector machine, stacking variant methodology</td><td>[45][66][81][25,26][31,38][50][10][7][46]</td></tr><tr><td>Clustering</td><td>Naïve Bayes</td><td>[42]</td></tr><tr><td>Prediction</td><td>Neural networks</td><td>[18]</td></tr><tr><td>Regression</td><td>Logistic modelLogistic modelLogistic model</td><td>[85][65][30]</td></tr></table>

<table><tr><td>Reference</td><td>Main objectives</td></tr><tr><td>[19]</td><td>To use Ada Boost, C4.5, CART, Ripper, Bayes and ID3 methods to determine whether combining multiple learned fraud detectors under a “cost model” could reduce losses from fraud</td></tr><tr><td>[20]</td><td>To use a binary support vector system (BSVS) based on the support vectors in support vector machines (SVM) and the genetic algorithm (GA) to solve problems of credit card fraud that had not been well identified</td></tr><tr><td>[27]</td><td>To present an on-line system for fraud detection in credit card operations based on a neural classifier</td></tr><tr><td>[36]</td><td>To propose a framework for data mining-based network analysis in anti-money laundering research</td></tr><tr><td>[60]</td><td>To focus on real-time fraud detection and present a new model based on self-organizing maps to better understand spending patterns</td></tr><tr><td>[67]</td><td>To build a Hidden Markov Model for the sequence of operations in credit card transaction processing</td></tr><tr><td>[84]</td><td>To consider the case of customer default payments in Taiwan and compare the predictive accuracy of the probability of default among six data mining methods: K-nearest neighbor, logistic regression, discriminant analysis, Naïve Bayesian, neural networks and classification trees</td></tr><tr><td>[87]</td><td>To propose a self-organizing map algorithm to create a model of typical cardholder behavior and to analyze deviations in transactions, thus identifying suspicious ones</td></tr></table>

## 4.3. Distribution of articles by year

Table 8 presents the distribution of articles by <sup>fi</sup>nancial fraud and publication year. It can be seen from this table that research studies on corporate fraud and automobile insurance fraud are the most prominent, and we believe that this will continue to be the case.

As shown in Table 8, we identi<sup>fi</sup>ed only one application article for money laundering and none for mortgage fraud, securities and commodities fraud and mass marketing fraud. We believe that this is because of the dif<sup>fi</sup>culty of collecting such data for analysis and because publication of the <sup>fi</sup>nding may be prohibited due to the highly sensitive nature of the topic.

## 4.4. Distribution of articles by journal

Table 9 shows the distribution of the articles by the journal in which they appeared. The articles related to the use of data mining techniques for FFD are distributed across 29 journals that cover a wide range of <sup>fi</sup>elds, including information systems, auditing and <sup>fi</sup>nance, etc., which means that the application of such techniques for FFD has attracted considerable interest from scholars in different disciplines. The Journal of Risk and Insurance contained the most relevant articles (16.3%, or 8 of the 49 articles), followed by Expert Systems with Applications (12.2%, or 6 articles) and the Managerial Auditing Journal (8.2%, or 4 articles).

Table 4 Insurance fraud.

<table><tr><td>Reference</td><td>Main objectives</td></tr><tr><td>[4]</td><td>To present discrete-choice models of fraudulent behavior and estimate the influence of insured and claims characteristics on the probability of fraud</td></tr><tr><td>[5]</td><td>To develop binary choice models for fraud detection and for the misclassification of the response variables in automobile insurance</td></tr><tr><td>[6]</td><td>To create predictions for a yield-switching model to identify producers whose reported yield patterns are consistent</td></tr><tr><td>[9]</td><td>To develop a probit model to aid insurance companies in their decision making and to ensure that they are better equipped to fight fraud</td></tr><tr><td>[11]</td><td>To develop an asymmetric or skewed logit model using Bayesian analysis for fraud detection in the Spanish insurance market</td></tr><tr><td>[15]</td><td>To apply a self-organizing feature map to classify automobile bodily injury claims fraud</td></tr><tr><td>[16]</td><td>To introduce the statistical and a priori classification and principal components analysis of RIDIT score (PRIDIT) methods to detect fraud in the automobile insurance industry</td></tr><tr><td>[17]</td><td>To build a fraud detection model based on a logit model and the EM algorithm to estimate an AAG model</td></tr><tr><td>[23]</td><td>To use a linear regression model to examine the optimal claims settlement strategy for a liability insurer</td></tr><tr><td>[41]</td><td>To propose Kohonen&#x27;s self-organizing map to classify medical general practitioners who have been classified by expert consultants</td></tr><tr><td>[43]</td><td>To propose a score test to help in deciding whether to use a logit or a probit model in predicting insurance fraud probabilities</td></tr><tr><td>[51]</td><td>To build an EFD system to integrate expert knowledge with a statistical information assessment to identify cases of unusual provider behavior and to use the machine-learning method to develop new rules and improve the identification process</td></tr><tr><td>[56]</td><td>To develop a fuzzy-based expert system to identify and evaluate whether elements of fraud are involved in insurance claims settlements</td></tr><tr><td>[59]</td><td>To use a two-equation model (a bivariate probit model) for audit and fraud detection in automobile insurance</td></tr><tr><td>[64]</td><td>To use visualization tools to help investigators to recognize new and unusual patterns of activity, thus allowing a better understanding of the direction and use of limited health care fraud detection and investigation resources</td></tr><tr><td>[68]</td><td>To propose a cultural algorithm to detect fraudulent automobile insurance claims, non-fraudulent claims, false positive claims (non-fraudulent claims predicted to be fraudulent), and false negative claims</td></tr><tr><td>[72]</td><td>To use an econometric logistic model to investigate the role of claims auditing in the automobile insurance market</td></tr><tr><td>[74]</td><td>To use logistic regression to score claims and detect fraud using real-life data in the automobile insurance industry</td></tr><tr><td>[75]</td><td>To explore the explicative capabilities of neural network classifiers for personal injury protection in automobile insurance claims fraud detection</td></tr><tr><td>[76]</td><td>To use logistic regression, C4.5, neural network, least-squares support vector machine, K-nearest neighbor, Naïve Bayes and tree-augmented Naïve Bayes methods for the detection of fraud in PIP automobile insurance claims</td></tr><tr><td>[77]</td><td>To apply AdaBoosted Naïve Bayes scoring to insurance claims fraud</td></tr><tr><td>[80]</td><td>To apply a Tobit regression model to explore the potential for reducing unwarranted claims payments</td></tr><tr><td>[82]</td><td>To build a SmartSifter system based on the on-line unsupervised learning of a probabilistic model (using a finite mixture model) to detect outliers in an on-line process</td></tr><tr><td>[83]</td><td>To propose an adaptable and extendable detection model to the concept of clinical pathways to facilitate automatic and systematic construction</td></tr></table>

## 5. Conclusion, research implications and limitations

A critical part of any new research venture is the construction of a good classi<sup>fi</sup>cation framework and the establishment of a reference collection of relevant literature. The research area of FFD is no exception. Although the importance of data mining techniques in the detection of <sup>fi</sup>nancial fraud has been recognized, a comprehensive classi<sup>fi</sup>cation framework or a systematic review of their application in

Other related <sup>fi</sup>nancial fraud.

<table><tr><td>Reference</td><td>Main objectives</td></tr><tr><td>[7]</td><td>To introduce classification and regression trees to identify and predict the impact of fraudulent financial statements</td></tr><tr><td>[10]</td><td>To develop a logistic regression model to estimate fraudulent financial reporting for an audit client</td></tr><tr><td>[18]</td><td>To use neural networks to predict the occurrence of corporate fraud at the management level</td></tr><tr><td>[25]</td><td>To provide a fuzzy sets model to assess the risk of managerial fraud</td></tr><tr><td>[26]</td><td>To build a rule-based fuzzy reasoning system to assess the risk of managerial fraud</td></tr><tr><td>[30]</td><td>To build an expert system applying the logit statistical model to enhance user engagement and increase reliance on the aid</td></tr><tr><td>[31]</td><td>To use neural networks to develop a model for detecting managerial fraud</td></tr><tr><td>[38]</td><td>To develop a neural network fraud classification model employing endogenous financial data in corporate fraud</td></tr><tr><td>[42]</td><td>To identify disgruntled employee systems fraud risk through Naïve Bayes text mining</td></tr><tr><td>[45]</td><td>To explore the effectiveness of neural networks, decision trees and Bayesian belief networks in detecting fraudulent financial statements (FFS) and to identify factors associated with FFS</td></tr><tr><td>[46]</td><td>To apply a hybrid decision support system using stacking variant methodology to detect FFS</td></tr><tr><td>[50]</td><td>To evaluate the utility of an integrated fuzzy neural network model for corporate fraud detection</td></tr><tr><td>[54]</td><td>To explore the logit regression model to detect corporate fraud in New Zealand</td></tr><tr><td>[65]</td><td>To use logistic regression to examine published data and develop a model to detect the factors associated with FFS</td></tr><tr><td>[66]</td><td>To explore the Multicriteria Decision Aid (MCDA) and UTilite&#x27;s Additives DIScriminantes (UTADIS) for detecting FFS and identifying the factors associated with FFS</td></tr><tr><td>[81]</td><td>To use genetic algorithms to aid the decisions of Defense Contractor Audit Agency (DCAA) auditors when they are estimating the likelihood of contracts fraud</td></tr><tr><td>[85]</td><td>To employ a logistic regression model to test the effects of managerial compensation and market competition on financial fraud among listed companies in China</td></tr></table>

Distribution of articles by data mining application classes

<table><tr><td>FF-based categories</td><td>Fraudulent activities</td><td>Data mining application classes</td><td>Amount</td></tr><tr><td rowspan="6">Bank fraud</td><td rowspan="3">Credit card fraud</td><td></td><td>7 (14.3%)</td></tr><tr><td>Classification</td><td>4</td></tr><tr><td>Clustering</td><td>3</td></tr><tr><td rowspan="3">Money laundering</td><td></td><td>1 (2.0%)</td></tr><tr><td>Classification</td><td>1</td></tr><tr><td></td><td>8</td></tr><tr><td rowspan="11">Insurance fraud</td><td rowspan="2">Crop Insurance fraud</td><td></td><td>2 (4.1%)</td></tr><tr><td>Regression</td><td>2</td></tr><tr><td rowspan="4">Healthcare insurance fraud</td><td></td><td>5 (10.2%)</td></tr><tr><td>Classification</td><td>3</td></tr><tr><td>Outlier Detection</td><td>1</td></tr><tr><td>Visualization</td><td>1</td></tr><tr><td rowspan="5">Automobile insurance fraud</td><td></td><td>17 (34.7%)</td></tr><tr><td>Classification</td><td>11</td></tr><tr><td>Prediction</td><td>2</td></tr><tr><td>Regression</td><td>4</td></tr><tr><td></td><td>24</td></tr><tr><td rowspan="6">Other related financial fraud</td><td rowspan="6">Corporate fraud</td><td></td><td>17 (34.7%)</td></tr><tr><td>Classification</td><td>11</td></tr><tr><td>Clustering</td><td>1</td></tr><tr><td>Prediction</td><td>1</td></tr><tr><td>Regression</td><td>4</td></tr><tr><td></td><td>17</td></tr><tr><td>Total</td><td></td><td>49 (100%)</td><td>49</td></tr></table>

Statistics of articles on <sup>fi</sup>nancial fraud and data mining techniques.

<table><tr><td rowspan="2">No.</td><td rowspan="2">Techniques</td><td colspan="2">Bank fraud</td><td colspan="3">Insurance fraud</td><td>Other related financial fraud</td><td rowspan="2">Total</td></tr><tr><td>Credit card fraud</td><td>Money laundering</td><td>Crop insurance fraud</td><td>Healthcare insurance fraud</td><td>Automobile insurance fraud</td><td>Corporate fraud</td></tr><tr><td>1</td><td>Logistic model</td><td>1</td><td></td><td>1</td><td></td><td>9</td><td>5</td><td>16</td></tr><tr><td>2</td><td>Neural networks</td><td>2</td><td></td><td></td><td></td><td>2</td><td>6</td><td>10</td></tr><tr><td>3</td><td>Bayesian belief network</td><td>1</td><td></td><td></td><td></td><td>2</td><td>2</td><td>5</td></tr><tr><td>4</td><td>Decision trees</td><td>2</td><td></td><td></td><td></td><td>1</td><td>2</td><td>5</td></tr><tr><td>5</td><td>Naïve Bayes</td><td>1</td><td></td><td></td><td></td><td>2</td><td>1</td><td>4</td></tr><tr><td>6</td><td>Evolutionary algorithms</td><td>1</td><td></td><td></td><td></td><td>1</td><td>1</td><td>3</td></tr><tr><td>7</td><td>K-nearest neighbor</td><td>1</td><td></td><td></td><td></td><td>1</td><td>1</td><td>3</td></tr><tr><td>8</td><td>Probit model</td><td></td><td></td><td>1</td><td></td><td>2</td><td></td><td>3</td></tr><tr><td>9</td><td>Self-organizing map</td><td>1</td><td></td><td></td><td>1</td><td>1</td><td></td><td>3</td></tr><tr><td>10</td><td>Support vector Machine</td><td>1</td><td></td><td></td><td></td><td>1</td><td>1</td><td>3</td></tr><tr><td>11</td><td>CART</td><td>1</td><td></td><td></td><td></td><td></td><td>1</td><td>2</td></tr><tr><td>12</td><td>Discriminant analysis</td><td>2</td><td></td><td></td><td></td><td></td><td></td><td>2</td></tr><tr><td>13</td><td>Fuzzy logic</td><td></td><td></td><td></td><td></td><td>1</td><td>1</td><td>2</td></tr><tr><td>14</td><td>RIPPER</td><td>1</td><td></td><td></td><td></td><td></td><td>1</td><td>2</td></tr><tr><td>15</td><td>Ada boost algorithm</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td>1</td></tr><tr><td>16</td><td>Association rule</td><td></td><td></td><td></td><td>1</td><td></td><td></td><td>1</td></tr><tr><td>17</td><td>Discounting learning algorithm</td><td></td><td></td><td></td><td>1</td><td></td><td></td><td>1</td></tr><tr><td>18</td><td>Hidden Markov Model</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td>1</td></tr><tr><td>19</td><td>Multicriteria decision aid (MCDA)</td><td></td><td></td><td></td><td></td><td></td><td>1</td><td>1</td></tr><tr><td>20</td><td>Network analysis</td><td></td><td>1</td><td></td><td></td><td></td><td></td><td>1</td></tr><tr><td>21</td><td>Polymorphous (M-of-N) logic</td><td></td><td></td><td></td><td>1</td><td></td><td></td><td>1</td></tr><tr><td>22</td><td>Principal component analysis of RIDIT (PRIDIT)</td><td></td><td></td><td></td><td></td><td>1</td><td></td><td>1</td></tr><tr><td>23</td><td>Stacking variant methodology</td><td></td><td></td><td></td><td></td><td></td><td>1</td><td>1</td></tr><tr><td>24</td><td>UTilite&#x27;s Additives DIScriminantes (UTADIS)</td><td></td><td></td><td></td><td></td><td></td><td>1</td><td>1</td></tr><tr><td>25</td><td>Visualization</td><td></td><td></td><td></td><td>1</td><td></td><td></td><td>1</td></tr><tr><td>26</td><td>Yield-switching model</td><td></td><td></td><td>1</td><td></td><td></td><td></td><td>1</td></tr><tr><td></td><td>Total</td><td>17</td><td>1</td><td>3</td><td>5</td><td>24</td><td>25</td><td>75</td></tr></table>

FFD research studies is lacking. In this study, we conduct an extensive review of academic articles and provide a comprehensive bibliography and classi<sup>fi</sup>cation framework for the applications of data mining to FFD. Our intention is to inform both academics and practitioners of the areas in which speci<sup>fi</sup>c data mining techniques can be applied to FFD, and to report and compile a systematic review of the burgeoning literature on FFD. Although our study cannot claim to be exhaustive, we believe that it will prove a useful resource for anyone interested in FFD research, and will help simulate further interest in the <sup>fi</sup>eld.

The results of our study lead to the following conclusions.

• Of the four FF-based categories, Insurance fraud has attracted the greatest attention from researchers. Phua et al. [58] point out that insurance fraud is more likely to be committed by offenders, which may be why this type of fraud has gained so much research attention. Insurance fraud is also the area of FFD to which data mining techniques are most commonly applied (24 articles out of 49, or 49%), with automobile insurance fraud in particular being described in 17 out of the 24 articles. Artís et al. [5] argue that this is a subject of major concern for both companies and consumers.

• There are only a few studies on money laundering, mortgage fraud, mass marketing fraud, and securities and commodities fraud. Further, there is only one article that discusses the application of data mining to the detection of money laundering, and no articles reporting its application to the other three fraud types. Nevertheless, these fraudulent activities are important and deserve more research. Gao and Ye [36] emphasize that antimoney laundering research is of critical signi<sup>fi</sup>cance to national <sup>fi</sup>nancial stability and international security, and the UN Of<sup>fi</sup>ce on Drugs and Crime (UNODC) estimates that the total amount of “black” money circulating worldwide reached 320 billion dollars in 2008 [69].

• The data mining techniques of outlier detection and visualization have seen only limited use. The lack of research on the application of outlier detection techniques to FFD may be due to the dif<sup>fi</sup>culty of detecting outliers. Indeed, Agyemang et al. [2] point out that outlier detection is a very complex task akin to <sup>fi</sup>nding a needle in a haystack. Distinct from other data mining techniques, outlier detection techniques are dedicated to <sup>fi</sup>nding rare patterns associated with very few data objects. In the <sup>fi</sup>eld of FFD, outlier detection is highly suitable for distinguishing fraudulent data from authentic data, and thus deserves more investigation. Similarly, visualization techniques have a strong ability to recognize and present data anomalies, which could make the identi<sup>fi</sup>cation and quanti<sup>fi</sup>cation of fraud schemes much easier [64].

We suggest that one of the reasons for the limited number of relevant journal articles (49) published between 1997 and 2008 is the dif<sup>fi</sup>culty of obtaining suf<sup>fi</sup>cient research data. Fanning and Cogger [31] highlight the challenge of obtaining fraudulent <sup>fi</sup>nancial statements, and note that this creates enormous obstacles in FFD research. The most urgent challenge facing FFD is to bridge the gap between practitioners and researchers. The existing FFD research concentrates on particular types of data mining techniques or models, but future research should direct its attention toward <sup>fi</sup>nding more practical principles and solutions for practitioners to help them to design, develop, and implement data mining and business intelligence systems that can be applied to FFD.

Classi<sup>fi</sup>cation of articles by the categories of <sup>fi</sup>nancial fraud and publication year.

<table><tr><td>FF-based categories</td><td>Fraudulent activities</td><td>1997</td><td>1998</td><td>1999</td><td>2000</td><td>2001</td><td>2002</td><td>2003</td><td>2004</td><td>2005</td><td>2006</td><td>2007</td><td>2008</td><td>Total</td></tr><tr><td rowspan="2">Bank fraud</td><td>Credit card fraud</td><td>1</td><td></td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td>2</td><td></td><td>3</td><td>7</td></tr><tr><td>Money laundering</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td></td><td>1</td></tr><tr><td rowspan="3">Insurance fraud</td><td>Crop insurance fraud</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td>1</td><td></td><td></td><td>2</td></tr><tr><td>Healthcare insurance fraud</td><td>1</td><td></td><td></td><td></td><td>1</td><td>1</td><td></td><td>1</td><td></td><td>1</td><td></td><td></td><td>5</td></tr><tr><td>Automobile insurance fraud</td><td>1</td><td>2</td><td>1</td><td>1</td><td></td><td>5</td><td></td><td>1</td><td>3</td><td></td><td>2</td><td>1</td><td>17</td></tr><tr><td>Other related financial fraud</td><td>Corporate fraud</td><td>3</td><td>3</td><td>1</td><td>1</td><td></td><td>3</td><td>1</td><td></td><td></td><td>1</td><td>1</td><td>3</td><td>17</td></tr><tr><td>Total</td><td></td><td>6</td><td>5</td><td>3</td><td>2</td><td>1</td><td>9</td><td>1</td><td>2</td><td>4</td><td>5</td><td>4</td><td>7</td><td>49</td></tr></table>

Table 9  
Distribution of articles by journal title.

<table><tr><td>Journal title</td><td>Number</td><td>Percentage (%)</td></tr><tr><td>Journal of Risk and Insurance</td><td>8</td><td>16.3</td></tr><tr><td>Expert Systems with Applications</td><td>6</td><td>12.2</td></tr><tr><td>Managerial Auditing Journal</td><td>4</td><td>8.2</td></tr><tr><td>International Journal of Intelligent Systems in Accounting, Finance and Management</td><td>3</td><td>6.1</td></tr><tr><td>Auditing: A Journal of Practice &amp; Theory</td><td>3</td><td>6.1</td></tr><tr><td>Insurance: Mathematics and Economics</td><td>2</td><td>4.1</td></tr><tr><td>American Journal of Agriculture Economics</td><td>1</td><td>2.0</td></tr><tr><td>Applied Economics</td><td>1</td><td>2.4</td></tr><tr><td>Computer Fraud and Security</td><td>1</td><td>2.4</td></tr><tr><td>Data Mining and Knowledge Discovery</td><td>1</td><td>2.4</td></tr><tr><td>Decision Support Systems</td><td>1</td><td>2.4</td></tr><tr><td>European Accounting Review</td><td>1</td><td>2.4</td></tr><tr><td>European Journal of Operational Research</td><td>1</td><td>2.4</td></tr><tr><td>Geneva Papers on Risk and Insurance</td><td>1</td><td>2.4</td></tr><tr><td>IEEE Intelligent Systems</td><td>1</td><td>2.4</td></tr><tr><td>IEEE Transactions on Dependable and Secure Computing</td><td>1</td><td>2.4</td></tr><tr><td>IEEE Transactions on Evolutionary Computation</td><td>1</td><td>2.4</td></tr><tr><td>IEEE Transactions on Knowledge and Data Engineering</td><td>1</td><td>2.4</td></tr><tr><td>IEEE Transactions on Neural Networks</td><td>1</td><td>2.4</td></tr><tr><td>Information and Security</td><td>1</td><td>2.4</td></tr><tr><td>International Journal of Computational Intelligence</td><td>1</td><td>2.4</td></tr><tr><td>International Journal of Information Technology and Decision Making</td><td>1</td><td>2.4</td></tr><tr><td>International Journal of Management</td><td>1</td><td>2.4</td></tr><tr><td>International Journal of Pattern Recognition and Artificial Intelligence</td><td>1</td><td>2.4</td></tr><tr><td>Journal of Law and Economics</td><td>1</td><td>2.4</td></tr><tr><td>Journal of Money Laundering Control</td><td>1</td><td>2.4</td></tr><tr><td>Managerial Finance</td><td>1</td><td>2.4</td></tr><tr><td>Risques</td><td>1</td><td>2.4</td></tr><tr><td>Topics in Health Information Management</td><td>1</td><td>2.4</td></tr><tr><td>Total</td><td>49</td><td>100</td></tr></table>

We predict that increasing amounts of privacy-preserving <sup>fi</sup>nancial data will be publicly available in the near future due to increased collaboration between practitioners and researchers, and that this should lead to more investigations of data mining techniques that can be applied to privacy-preserving data.

A further problem faced by FFD is that of cost sensitivity. The cost of misclassi<sup>fi</sup>cation (false positive and false negative errors) differs, with a false negative error (misclassifying a fraudulent activity as a normal activity) usually being more costly than a false positive error (misclassifying a normal activity as a fraudulent activity) [58]. Few studies have explicitly included cost in their FFD modeling [74], but future research on the application of data mining techniques to FFD problems should take into account cost sensitivity considerations.

This study has two major limitations. First, our review applied several keywords to search only nine online databases for articles published between 1997 and 2008. A future review could be expanded in scope. Second, we considered only articles written in English. Future research could be expanded to include relevant articles published in other languages.

## Acknowledgements

The authors gratefully acknowledge the associate editor and reviewers' constructive comments on an earlier version of the paper.

This research was partly supported by the National Natural Science Foundation of China (NSFC, project no.: 70801020), the Science and Technology Planning Project of Guangdong Province, China(project no.: 2010B010600034) and The Hong Kong Polytechnic University under a research grant number G-YX71 and the “211 Project” of Guangdong University of Foreign Studies.

## References

[1] A. Agresti, Categorical Data Analysis, Wiley Series in Probability and Mathematical Statistics, Wiley, New York, 1990.

[2] M. Agyemang, K. Barker, R. Alhajj, A comprehensive survey of numeric and symbolic outlier mining techniques, Intelligent Data Analysis 10 (6) (2006) 521–538.

[3] S.R. Ahmed, Applications of data mining in retail business, International Conference on Information Technology: Coding and Computing 2 (2) (2004) 455–459.

[4] M. Artı́s, M. Ayuso, M. Guillén, Modelling different types of automobile insurance fraud behaviour in the Spanish market, insurance, Mathematics and Economics 24 (1) (1999) 67–81.

[5] M. Artı́s, M. Ayuso, M. Guillén, Detection of automobile insurance fraud with discrete choice models and misclassi<sup>fi</sup>ed claims, The Journal of Risk and Insurance 69 (3) (2002) 325–340.

[6] J.A. Atwood, J.F. Robinson-Cox, S. Shaik, Estimating the prevalence and cost of yield-switching fraud in the federal crop insurance program, American Journal of Agricultural Economics 88 (2) (2006) 365–381.

[7] B. Bai, J. Yen, X. Yang, False <sup>fi</sup>nancial statements: characteristics of China's listed companies and CART detecting approach, International Journal of Information Technology & Decision Making 7 (2) (2008) 339–359.

[8] BBC News, http://news.bbc.co.uk/1/hi/business/6636005.stm

[9] E.B. Belhadji, G. Dionne, F. Tarkhani, A model for the detection of insurance fraud, The Geneva Papers on Risk and Insurance 25 (4) (2000) 517–538.

[10] T.B. Bell, J.V. Carcello, A decision aid for assessing the likelihood of fraudulent <sup>fi</sup>nancial reporting, Auditing: A Journal of Practice & Theory 19 (1) (2000) 169–174.

[11] L. Bermúdez, J.M. Pérez, M. Ayuso, E. Gómez, F.J. Vázquez, A. Bayesian Dichotomous, Model with asymmetric link for fraud in insurance, Insurance: Mathematics and Economics 42 (2) (2008) 779–786.

[12] M.J.A. Berry, G.S. Linoff, Data Mining Techniques: for Marketing, Sales, and Customer Relationship Management, Second ed.Wiley, New York, 2004

[13] R.J. Bolton, D.J. Hand, Statistical fraud detection: a review, Statistical Science 17 (3) (2002) 235–255.

[14] I. Bose, R.K. Mahapatra, Business data mining — a machine learning perspective, Information Management 39 (3) (2001) 211–225.

[15] P.L. Brockett, X. Xia, R.A. Derrig, Using Kononen's self-organizing feature map to uncover automobile bodily injury claims fraud, The Journal of Risk and Insurance 65 (2) (1998) 245–274.

[16] P.L. Brockett, R.A. Derrig, L.L. Golden, Fraud classi<sup>fi</sup>cation using principal component analysis of RIDITS, The Journal of Risk and Insurance 69 (3) (2002) 341-371.

[17] S.B. Caudill, M. Ayuso, M. Guillén, Fraud detection using a multinominal logit model with missing information, The Journal of Risk and Insurance 72 (4) (2005) 539–550.

[18] M.J. Cerullo, V. Cerullo, Using neural networks to predict <sup>fi</sup>nancial reporting fraud, Computer Fraud & Security May/June (1999) 14–17.

[19] P.K. Chan, W. Fan, A.L. Prodromidir, S.L. Stalfo, Distributed data mining in credit card fraud detection, IEEE Intelligent Systems Nov/Dec (1999) 67–74.

[20] R. Chen, T. Chen, C. Lin, A new binary support vector system for increasing detection rate of credit card fraud, International Journal of Pattern Recognition and Arti<sup>fi</sup>cial Intelligence 20 (2) (2006) 227–239.

[21] Coalition against Insurance Fraud, “Learn about fraud,” http://www.insurancefraud.org/learn\_about\_fraud.htm

[22] CULS, Cornell University Law School, White-Collar Crime: an overview, http:// topics.law.cornell.edu/wex/White-collar\_crime (2009)

[23] K.J. Crocker, S. Tennyson, Insurance fraud and optimal claims settlement strategies, Journal of Law and Economics 45 (2002) 469–507.

[24] R.A. Derrig, Insurance fraud, The Journal of Risk and Insurance 69 (3) (2002) 271–287.

[25] A. Deshmukh, J. Romine, P.H. Siegel, Measurement and combination of red <sup>fl</sup>ags to assess the risk of management fraud: a fuzzy set approach, Managerial Finance 23 (6) (1997) 35–48.

[26] A. Deshmukh, L. Talluru, A rule-based fuzzy reasoning system for assessing the risk of management fraud, International Journal of Intelligent Systems in Accounting, Finance & Management 7 (4) (1998) 223–241.

[27] J.R. Dorronsoro, F. Ginel, C. Sánchez, C.S. Cruz, Neural fraud detection in credit card operations JEEE Transactions on Neural Networks 8 (4) (1997) 827-834

[28] R.O. Duda, P.E. Hart, E.G. Stock, Pattern Classi<sup>fi</sup>cation, Wiley, New York, 2001.

[29] S.G. Eick, D.E. Fyock, Visualizing corporate data, AT&T Technical Journal 75 (1) (1996) 74–86.

[30] M. Eining, D.R. Jones, J.K. Loebbecke, Reliance on decision aids: an examination of auditors' assessment of management fraud, Auditing: A Journal of Practice & Theory 16 (2) (1997) 1–19.

[31] K.M. Fanning, K.O. Cogger, Neural network detection of management fraud using published <sup>fi</sup>nancial data, International Journal of Intelligent Systems in Accounting, Finance & Management 7 (1) (1998) 21–41

[32] T. Fawcett, F. Provost, Adaptive fraud detection, Data Mining and Knowledge Discovery 1 (3) (1997) 291–316.

[33] FBI, Federal Bureau of Investigation, Financial Crimes Report to the Public Fiscal Year, Department of Justice, United States, 2007, http://www.fbi.gov/publications/<sup>fi</sup>nancial/fcs\_report2007/<sup>fi</sup>nancial\_crime\_2007.htm.

[34] FBI, Federal Bureau of Investigation New York Division, Department of Justice, United States, 2008, http://newyork.fbi.gov/dojpressrel/pressrel08/nyfo121108.htm

[35] W.J. Frawley, G. Piatetsky-Shapiro, C.J. Matheus, Knowledge discovery in databases: an overview, AI Magazine 13 (3) (1992) 57–70.

[36] Z. Gao, M. Ye, A framework for data mining-based anti-money laundering research, Journal of Money Laundering Control 10 (2) (2007) 170–179.

[37] S. Ghosh, D.L. Reilly, Credit card fraud detection with a neural-network, 27th Annual Hawaii International, Conference on System Science 3 (1994) 621–630.

[38] P. Green, J.H. Choi, Assessing the risk of management fraud through neural network technology, Auditing: A Journal of Practice & Theory 16 (1) (1997) 14–28.

[39] J. Han, M. Kamber, Data Mining: Concepts and Techniques, Second ed, Morgan Kaufmann Publishers, 2006, pp. 285–464.

[40] M. Haskett, An Introduction to Data Mining, Part 2, Analyzing the Tools and Techniques, Enterprise System Journal, 2000.

[41] H. He, J. Wang, W. Graco, S. Hawkins, Application of neural networks to detection of medical fraud, Expert Systems with Applications 13 (4) (1997) 329–336.

[42] C. Holton, Identifying disgruntled employee systems fraud risk through text mining: a simple solution for a multi-billion dollar problem, Decision Support Systems 46 (4) (2009) 853–864.

[43] Y. Jin, R.M. Rejesus, B.B. Little, Binary choice models for rare events data: a crop insurance fraud application, Applied Economics 37 (7) (2005) 841–848.

[44] J.L. Kaminski, Insurance Fraud, OLR Research Report, http://www.cga.ct.gov/2005/ rpt/2005-R-0025.htm. 2004

[45] E. Kirkos, C. Spathis, Y. Manolopoulos, Data mining techniques for the detection of fraudulent <sup>fi</sup>nancial statements, Expert Systems with Applications 32 (4) (2007) 995–1003.

[46] S. Kotsiantis, E. Koumanakos, D. Tzelepis, V. Tampakas, Forecasting fraudulent <sup>fi</sup>nancial statements using data mining, International Journal of Computational Intelligence 3 (2) (2006) 104–110.

[47] Y. Kou, C. Lu, S. Sirwongwattana, Y. Huang, Survey of fraud detection techniques, IEEE International Conference on Networking, Sensing & Control (2004) 749–754.

[48] W. Lee, S. Stolfo, Data Mining Approaches for Intrusion Detection, 7th USENIX Security Symposium, San Antonio, TX, 1998.

[49] J. Li, K. Huang, J. Jin, J. Shi, A survey on statistical methods for health care fraud detection, Health Care Management Science 11 (3) (2008) 275–287.

[50] J.W. Lin, M.I. Hwang, J.D. Becker, A fuzzy neural network for assessing the risk of fraudulent <sup>fi</sup>nancial reporting, Managerial Auditing Journal 18 (8) (2003) 657–665.

[51] J.A. Major, D.R. Riedinger, EFD: a hybrid knowledge/statistical-based system for the detection of fraud, The Journal of Risk and Insurance 69 (3) (2002) 309–324.

[52] S. Mitra, S.K. Pal, P. Mitra, Data mining in soft computing framework: a survey, JEEE Transactions on Neural Networks 13 (1) (2002) 3–14

[53] E.W.T. Ngai, L. Xiu, D.C.K. Chau, Application of data mining techniques in customer relationship management: a literature review and classification. Expert Systems with Applications 36 (2) (2009) 2592–2602.

[54] S. Owusu-Ansah, G.D. Moyes, P.B. Oyelere, P. Hay, An empirical analysis of the likelihood of detecting fraud in New Zealand, Managerial Auditing Journal 17 (4) (2002) 192–204.

[55] Oxford Concise English Dictionary, Tenth ed, Publisher, 1999.

[56] J. Pathak, N. Vidyarthi, S.L. Summers, A fuzzy-based algorithm for auditors to detect elements of fraud in settled insurance claims, Managerial Auditing Journal 20 (6) (2005) 632–644.

[57] J. Pearl, Probabilistic Reasoning in Intelligent Systems, Morgan Kaufmann, 1988.

[58] C. Phua, V. Lee, K. Smith, R. Gayler, A comprehensive survey of data mining-based fraud detection research, Arti<sup>fi</sup>cial Intelligence Review (2005) 1–14.

[59] J. Pinquet, M. Ayuso, M. Guillén, Selection bias and auditing policies for insurance claims, The Journal of Risk and Insurance 74 (2) (2007) 425–440.

[60] J.T.S. Quah, M. Sriganesh, Real-time credit card fraud detection using computational intelligence, Expert Systems with Applications 35 (4) (2008) 1721–1732.

[61] D. Sánchez, M.A. Vila, L. Cerda, J.M. Serrano, Association rules applied to credit card fraud detection, Expert Systems with Applications 36 (2) (2009) 3630–3640.

[62] S. Sharma, Applied Multivariate Techniques, Wiley, New York, 1996.

[63] M.J. Shaw, C. Subramaniam, G.W. Tan, M.E. Welge, Knowledge management and data mining for marketing, Decision Support System 31 (1) (2001) 127–137.

[64] L. Sokol, B. Garcia, J. Rodriguez, M. West, K. Johnson, Using data mining to <sup>fi</sup>nd fraud in HCFA health care claims, Topics in Health Information Management 22 (1) (2001) 1–13.

[65] C.T. Spathis, Detecting false <sup>fi</sup>nancial statements using published data: some evidence from Greece, Managerial Auditing Journal 17 (4) (2002) 179–191.

[66] C.T. Spathis, M. Doumpos, C. Zopounidis, Detecting falsi<sup>fi</sup>ed <sup>fi</sup>nancial statements: a comparative study using multicriteria analysis and multivariate statistical techniques, The European Accounting Review 11 (3) (2002) 509–535.

[67] A. Srivastava, A. Kundu, S. Sural, A.K. Majumdar, Credit card fraud detection using hidden Markov model, IEEE Transactions on Dependable and Secure Computing 5 (1) (2008) 37–48.

[68] M. Sternberg, R.G. Reynolds, Using cultural algorithms to support re-engineering of rule-based expert systems, in dynamic performance environments: a case study in fraud detection, IEEE Transactions on Evolutionary Computation 1 (4) (1997) 225–243.

[69] stopthedrugwar.org, http://stopthedrugwar.org/chronicle/570/costa\_UNODC\_- drug, trade banks. 30 Jan. 2009

[70] M. Syeda, Y. Zhang, Y. Pan, Parallel granular neural networks for fast credit card fraud detection, 2002, IEEE International Conference on Fuzzy Systems 1 (2002) 572–577.

[71] P. Tan, M. Steinbach, V. Kumar, Introduction to Data Mining, First ed.Addison-Wesley Longman Publishing Co., Inc, 2005.

[72] S. Tennyson, P. Salsas-Forn, Claims auditing in automobile insurance: fraud detection and deterrence objectives, The Journal of Risk and Insurance 69 (3) (2002) 289–308.

[73] E. Turban, J.E. Aronson, T.P. Liang, R. Sharda, Decision Support and Business Intelligence Systems, Eighth ed Pearson Education 2007

[74] S. Viaene, M. Ayuso, M. Guillén, D. Van Gheel, G. Dedene, Strategies for detecting fraudulent claims in the automobile insurance industry, European Journal of Operational Research 176 (1) (2007) 565–583.

[75] S. Viaene, G. Dedene, R.A. Derrig, Auto claim fraud detection using bayesian learning neural networks, Expert Systems with Applications 29 (3) (2005) 653–666.

[76] S. Viaene, R.A. Derrig, B. Baesens, G. Dedene, A comparison of state-of-the-art classi<sup>fi</sup>cation techniques for expert automobile insurance claim fraud detection, The Journal of Risk and Insurance 69 (3) (2002) 373–421.

[77] S. Viaene, R.A. Derrig, G. Dedene, A case study of applying boosting naive Bayes to claim fraud diagnosis, IEEE Transactions on Knowledge and Data Engineering 16 (5) (2004) 612–620.

[78] J. Wang, Y. Liao, T. Tsai, G. Hung, Technology-based <sup>fi</sup>nancial frauds in Taiwan: issue and approaches, IEEE Conference on: Systems, Man and Cyberspace Oct (2006) 1120–1124.

[79] A. Webb, Statistical Pattern Recognition, Arnold, London, 1999

[80] H.I. Weisberg, R.A. Derrig, Quantitative methods for detecting fraudulent automobile bodily injury claims, Risques 35 (1998) 75–101.

[81] J. Welch, T.E. Reeves, S.T. Welch, Using a genetic algorithm-based classi<sup>fi</sup>er system for modeling auditor decision behavior in a fraud setting, International Journal of Intelligent Systems in Accounting, Finance & Management 7 (3) (1998) 173–186.

[82] K. Yamanishi, J. Takeuchi, G. Williams, P. Milne, On-line unsupervised outlier detection using <sup>fi</sup>nite mixtures with discounting learning algorithms, Data Mining and Knowledge Discovery 8 (3) (2004) 275–300.

[83] W. Yang, S. Hwang, A process-mining framework for the detection of healthcare fraud and abuse, Expert Systems with Applications 31 (1) (2006) 56–68.

[84] I. Yeh, C. Lien, The comparisons of data mining techniques for the predictive accuracy of probability of default of credit card clients, Expert Systems with Applications 36 (2) (2008) 2473–2480.

[85] J. Yuan, C. Yuan, X. Deng, C. Yuan, The effects of manager compensation and market competition on <sup>fi</sup>nancial fraud in public companies: an empirical study in China, International Journal of Management 25 (2) (2008) 322–335.

[86] Yue, X. Wu, Y. Wang, Y. Li, C. Chu, A review of data mining-based <sup>fi</sup>nancial fraud detection research, international conference on wireless communications Sep, Networking and Mobile Computing (2007) 5519–5522

[87] V. Zaslavsky, A. Strizhak, Credit card fraud detection using self-organizing maps, Information & Security 18 (2006) 48-63.

[88] D. Zhang, L. Zhou, Discovering golden nuggets: data mining in <sup>fi</sup>nancial application, IEEE Transactions on Systems, Man and Cybernetics 34 (4) (2004) Nov.

![](/api/attachments/S2EV9SE8/fulltext/images/2e8c5ca25b07f71807a5ccb636ab12c42d83b129628afc6eef3920775b0deee0.jpg)

Prof. Eric Ngai is a Professor in the Department of Managementand Marketing at The Hong Kong Polytechnic University. His current research interests are in the areas of E-commerce, Supply Chain Management, Decision Support Systems and RFID Technology and Applications. He has published papers in a number of international journals including MIS Quarterly, Journal of Operations Management, Decision Support Systems, IEEE Transactions on Systems, Man and Cybernetics, Information & Management, Production & Operations Management, and others. He is an Associate Editor of European Journal of Information Systems and serves on editorial board of six international journals. Prof. Ngai has attained an h-index of 13 and received 510 citations, ISI Web of Science.

![](/api/attachments/S2EV9SE8/fulltext/images/4fbeedbc360eeda90fa953a11e400605003f66573ff6089f51cd1a2ad0461e1d.jpg)

Dr. Yong Hu is currently an Associate Professor and Chair in the Department of E-commerce, and Director of Institute of Business Intelligence and Knowledge Discovery at the Guangdong University of Foreign Studies He received his B Sc in Computer Science M Phil and Ph D in Management Information Systems from Sun Yat-Sen University. His research interests are in the areas of business intelligence software project risk management, e-commerce and decision support systems. He has published in a number of journals and conferences such as DSS, ESWA, JECO and IEEE ICDM. Dr. Hu's research is supported by the National Natural Science Foundation, the Science and Technology Planning Project of Guangdong Province, and “211 Project” of the Guangdong University of Foreign Studies.

![](/api/attachments/S2EV9SE8/fulltext/images/cf42470f8fdc69d1ca8b3548bdf1f2b7eeeb2cd7a03564a8a7b36ecba6ccb467.jpg)

Dr. Y. H. Wong is associate professor, Department of Management and Marketing, The Hong Kong Polytechnic University. His publications include 3 books, Guanxi: Relationship Marketing in a Chinese Context, Handbook of Research on Ubiquitous Commerce for Creating the Personalized Marketplace, Financial Planning and Wealth Management and refereed journal articles, such as, Industrial Marketing Management, International Business Review, European Journal of Marketing, Journal of Services Marketing and Journal of Business Ethics, etc.

![](/api/attachments/S2EV9SE8/fulltext/images/ffb9dd47a686250e8aba6315046570e6ef4860463e13a1a559e345e80dbc4838.jpg)

Xin Sun is an M.Phil student in Guangdong University of Foreign Studies and working as an assistant researcher in Institute of Business Intelligence and Knowledge Discovery. She has received her BSc in Mathematics and Applied Mathematics from Sun Yat-Sen University. Her research interest is software project risk management and business intelligence.

![](/api/attachments/S2EV9SE8/fulltext/images/8d9d786ea798adc850825f695328a447a7e31136a6cf1ed22baa26af0e3c9fcf.jpg)

Yi-Jun Chen is an M.Phil student in Department of Computing and Decision Science, Lingnan University, Hong Kong S.A.R of China. He received his BSc degree in information and computational science from Sun Yat-Sen University. His research interest includes data mining Bayesian networks and business intelligence.
