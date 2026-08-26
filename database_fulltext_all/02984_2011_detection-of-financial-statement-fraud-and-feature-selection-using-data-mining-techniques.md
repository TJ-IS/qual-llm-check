---
otero_id: 2984
otero_key: "5MAJW4K8"
title: "Detection of financial statement fraud and feature selection using data mining techniques"
authors: "P. Ravisankar; V. Ravi; G. Raghava Rao; I. Bose"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.11.006"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Detection of <sup>fi</sup>nancial statement fraud and feature selection using data mining techniques

P. Ravisankar <sup>a</sup>, V. Ravi <sup>a,</sup>⁎, G. Raghava Rao <sup>a</sup>, I. Bose <sup>b</sup>

<sup>a</sup> Institute for Development and Research in Banking Technology, Castle Hills Road #1, Masab Tank, Hyderabad 500 057, AP, India <sup>b</sup> School of Business, The University of Hong Kong, Pokfulam Road, Hong Kong

## a r t i c l e i n f o

Article history: Received 20 November 2009 Received in revised form 14 June 2010 Accepted 3 November 2010 Available online 12 November 2010

Keywords: Data mining Financial fraud detection Feature selection t-statistic Neural networks SVM GP

## a b s t r a c t

Recently, high pro<sup>fi</sup>le cases of <sup>fi</sup>nancial statement fraud have been dominating the news. This paper uses data mining techniques such as Multilayer Feed Forward Neural Network (MLFF), Support Vector Machines (SVM), Genetic Programming (GP), Group Method of Data Handling (GMDH), Logistic Regression (LR), and Probabilistic Neural Network (PNN) to identify companies that resort to <sup>fi</sup>nancial statement fraud. Each of these techniques is tested on a dataset involving 202 Chinese companies and compared with and without feature selection. PNN outperformed all the techniques without feature selection, and GP and PNN outperformed others with feature selection and with marginally equal accuracies.

© 2010 Elsevier B.V. All rights reserved.

## 1. Introduction

Financial fraud is a serious problem worldwide and more so in fast growing countries like China. Traditionally, auditors are responsible for detecting <sup>fi</sup>nancial statement fraud. With the appearance of an increasing number of companies that resort to these unfair practices, auditors have become overburdened with the task of detection of fraud. Hence, various techniques of data mining are being used to lessen the workload of the auditors. Enron and Worldcom are the two major scandals involving corporate accounting fraud, which arose from the disclosure of misdeeds conducted by trusted executives of large public corporations. Enron Corporation [17] was an American energy company based in Houston, Texas. Before its bankruptcy in late 2001, Enron was one of the world's leading electricity, natural gas, pulp and paper, and communications companies, with revenues amounting to nearly \$101 billion in 2000. Long Distance Discount Services, Inc. (LDDS) began its operations in Hattiesburg, Mississippi in 1983. The company's name was changed to LDDS WorldCom [18] in

1995, and later it became WorldCom. On July 21, 2002, WorldCom <sup>fi</sup>led for Chapter 11 bankruptcy protection in the largest such <sup>fi</sup>ling in US history at that time.

Financial statements are a company's basic documents to re<sup>fl</sup>ect its <sup>fi</sup>nancial status [3]. A careful reading of the <sup>fi</sup>nancial statements can indicate whether the company is running smoothly or is in crisis. If the company is in crisis, <sup>fi</sup>nancial statements can indicate if the most critical thing faced by the company is cash or pro<sup>fi</sup>t or something else. All the listed companies are required to publish their <sup>fi</sup>nancial statements every year and every quarter. The stockholders can form a good idea about the companies’ <sup>fi</sup>nancial future through the <sup>fi</sup>nancial statements, and can decide whether the companies’ stocks are worth investing. The bank also needs the companies’ <sup>fi</sup>nancial statements in order to decide whether to grant loans to them. In a nutshell, the <sup>fi</sup>nancial statements are the mirrors of the companies’ <sup>fi</sup>nancial status. Financial statements are records of <sup>fi</sup>nancial <sup>fl</sup>ows of a business. Generally, they include balance sheets, income statements, cash <sup>fl</sup>ow statements, statements of retained earnings, and some other statements. A detailed description of the items listed in the various <sup>fi</sup>nancial statements is given below:

## • Balance sheet

A balance sheet is a statement of the book value of an organization at a particular date, usually at the end of the <sup>fi</sup>scal year. A balance sheet has three parts: assets, liabilities, and shareholders' equity. The difference between the assets and the liabilities is known as the 'net assets' or the 'net worth' of the company.

## • Income statement

Income statements, also called Pro<sup>fi</sup>t and Loss Statement for companies indicate how net revenue (money received from the sale of products and services before expenses are subtracted, also known as the ‘top line’) is transformed into net income (the result after all revenues and expenses have been accounted for, also known as the ‘bottom line’). The purpose of the income statement is to show managers and investors whether the company made or lost money during the period under consideration.

## • Cash <sup>fl</sup>ow statement

A cash <sup>fl</sup>ow statement is a <sup>fi</sup>nancial statement that shows incoming and outgoing funds during a particular period. The statement shows how changes in balance sheet and income accounts affect cash and cash equivalents. As an analytical tool the statement of cash <sup>fl</sup>ows is useful in determining the short-term viability of a company, particularly its ability to pay bills.

## • Statement of retained earnings

The statement of retained earnings, also known as ‘statement of owners' equity’ and ‘statement of net assets’ for non-pro<sup>fi</sup>t organizations, explains the changes in company's retained earnings over the reporting period. It breaks down changes affecting the account, such as pro<sup>fi</sup>ts or losses from operations, dividends paid, and any other items charged or credited to retained earnings. Next, we will describe the key characteristics of <sup>fi</sup>nancial fraud that can be observed through the <sup>fi</sup>nancial ratios calculated on the basis of the <sup>fi</sup>nancial statements published by companies.

## 1.1. Financial ratios

Financial ratios are a valuable and easy way to interpret the numbers found in <sup>fi</sup>nancial statements. They can help to answer critical questions such as whether the business is carrying excess debt or inventory, whether customers are paying according to terms, whether the operating expenses are too high, and whether the company assets are being used properly to generate income.

## • Liquidity

Liquidity measures a company's capacity to pay its liabilities in short term. There are two ratios for evaluating liquidity. They are:

1) Current ratio = Total current assets / Total current liabilities

2) Quick ratio =(Cash+Accounts receivable +Any other quick assets) / Current liabilities

The higher the ratios the stronger is the company's ability to pay its liabilities as they become due, and the lower is the risk of default. • Safety

Safety indicates a company's vulnerability to risk of debt. There are three ratios for evaluating liquidity. They are:

1) Debt to equity=Total liabilities/Net worth

2) EBIT/Interest=Earnings before interest and taxes/Interest charges

3) Cash <sup>fl</sup>ow to current maturity of long-term debt=(Net pro<sup>fi</sup>t+ Non-cash expenses)/Current portion of long-term debt

## • Pro<sup>fi</sup>tability

Pro<sup>fi</sup>tability ratios measure the company's ability to generate a return on its resources. There are four ratios to evaluate a company's pro<sup>fi</sup>tability. They include:

1) Gross pro<sup>fi</sup>t margin=Gross pro<sup>fi</sup>t/Total sales

2) Net pro<sup>fi</sup>t margin=Net pro<sup>fi</sup>t/Total sales

3) Return on assets=Net pro<sup>fi</sup>t before taxes/Total assets

4) Return on equity=Net pro<sup>fi</sup>t before taxes/Net worth

## • Ef<sup>fi</sup>ciency

Ef<sup>fi</sup>ciency evaluates how well the company manages its assets. There are four ratios to evaluate the ef<sup>fi</sup>ciency of asset management:

1) Accounts receivable turnover = Total net sales / Accounts receivable

2) Accounts payable turnover =Cost of goods sold / Accounts payable

3) Inventory turnover=Cost of goods sold / Inventory

4) Sales to total assets = Total sales / Total assets

Financial statement fraud may be perpetrated to increase stock prices or to get loans from banks. It may be done to distribute lesser dividends to shareholders. Another probable reason may be to avoid payment of taxes. Nowadays an increasing number of companies are making use of fraudulent <sup>fi</sup>nancial statements in order to cover up their true <sup>fi</sup>nancial status and make sel<sup>fi</sup>sh gains at the expense of stockholders. The fraud triangle is also known as Cressey's Triangle, or Cressey's Fraud Triangle. The fraud triangle seeks to explain what must be present for fraud to occur. The fraud triangle describes the probability of <sup>fi</sup>nancial reporting fraud which depends on three factors: incentives/pressures, opportunities, and attitudes/rationalization of <sup>fi</sup>nancial statement fraud [37,38]. The fraud triangle is depicted in Fig. 1, and it is discussed below.

When <sup>fi</sup>nancial stability or pro<sup>fi</sup>tability is threatened by economic, industry, or entity operating conditions, or excessive pressure exists for management to meet debt requirements, or personal net worth is materially threatened, the management will face the incentives or pressures to resort to fraudulent practice. Pressure can come in the form of peer pressure, living a lavish lifestyle, a drug addiction, and many other aspects that can in<sup>fl</sup>uence someone to seek gains via <sup>fi</sup>nancial fraud. When there are signi<sup>fi</sup>cant accounting estimates that are dif<sup>fi</sup>cult to verify, or there is oversight over <sup>fi</sup>nancial reporting, or high turnover or ineffective accounting internal audit, there are opportunities for fraud. For instance, a cashier can steal money out of the cash register because it is there. If the cashier is required to drop all cash into an underground safe for which he does not know the combination, opportunity will not exist. When inappropriate or inef<sup>fi</sup>cient communication and support of the entity's values is evident, or a history of violation of laws is known, or management has a practice of making overly aggressive or unrealistic forecasts, then there are risks of fraudulent reporting due to attitudes/ rationalization. Rationalization is a grey area in the fraud triangle. Opportunities and incentives exist or they don't. Rationalization depends on the individuals and the circumstances they are facing [19,37]. Understanding the fraud triangle is essential to evaluating <sup>fi</sup>nancial fraud. When someone is able to grasp the basic concept of the fraud triangle, they are able to better understand <sup>fi</sup>nancial frauds, how they occur, why they occur, and what to do to stop them.

## 1.2. Variables related to financial statement fraud

Based on expert's knowledge, intuition, and previous research, it is important to identify some key <sup>fi</sup>nancial items that are relevant for detection of <sup>fi</sup>nancial statement fraud. These are listed below:

• Z-score: The Z-score is developed by Altman [2]. It is a formula for measurement of the <sup>fi</sup>nancial health of a company and works as a tool to predict bankruptcy. It is used to detect <sup>fi</sup>nancial statement fraud as well. The formula for Z-score for public companies is given by:

![](/api/attachments/5MAJW4K8/fulltext/images/f21bf481cecd0aafbc29fd8415ef099dd4ebea56aee9c1df12f3f19db0aa503c.jpg)  
Fig. 1. Components of the fraud triangle.

$$
\begin{array}{r l} \text { Z - score } & = (\text { Working   capital / Total   assets } ^ {*} 1. 2) + (\text { Retained   earnings } \\ & \div \text { Total   assets } ^ {*} 1. 4) + (\text { Earnings   before   income   tax } \\ & \div \text { Total   assets } ^ {*} 3. 3) + (\text { Market   value   of   equity } \\ & \div \text { Book   value   of   total }) + (\text { Liabilities } ^ {*} 0. 6 + \text { Sales } \\ & \div \text { Total   assets } ^ {*} 0. 9 9 9) \end{array}
$$

• A high debt structure increases the likelihood of <sup>fi</sup>nancial fraud as it shifts the risk from equity owner to the debt owner. So the <sup>fi</sup>nancial ratios related to debt structure such as (i) Total debt/Total assets and (ii) Debt/Equity need to be carefully considered when searching for indications of fraud.

• An abnormal value reported as a measure of continuous growth such as sales to growth ratio is also a factor that may be indicative of fraudulent <sup>fi</sup>nancial practice.

• Many items of the <sup>fi</sup>nancial statements such as Accounts receivable, Inventories, Gross margin etc. can be estimated to some degree using subjective methods and different accounting methods can often lead to different values even for the same company.

• According to previous research, many other <sup>fi</sup>nancial ratios can be considered for fraud detection, such as Net pro<sup>fi</sup>t/Total assets, Working capital/Total assets, Net pro<sup>fi</sup>t/Sales, Current assets/ Current liabilities and so on.

• The tenure of CEO and CFO: According to the auditors’ experience and previous research, the high turnover of CEO and CFO may indicate the existence of <sup>fi</sup>nancial fraud in the company.

• Some qualitative variables such as previous auditor's quali<sup>fi</sup>cations can be considered to determine the likelihood of fraudulent book keeping.

Data mining has been applied in many aspects of <sup>fi</sup>nancial analysis. Few areas where data mining techniques have already being used include: bankruptcy prediction, credit card approval, loan decision, money-laundering detection, stock analysis, etc. However, research related to the use of data mining for detection of <sup>fi</sup>nancial statement fraud is limited. The main objective of this research is to predict the occurrence of <sup>fi</sup>nancial statement fraud in companies as accurately as possible using intelligent techniques. Financial accounting fraud can be detected by a human expert by using his/her experiential/ judgemental knowledge, provided he/she has suf<sup>fi</sup>cient expertise. However, in this case, human bias cannot be eliminated and the judgments tend to be subjective. Hence, we resort to data-driven approaches, which solely rely on the past data of fraudulent and healthy companies and their <sup>fi</sup>nancial ratios. When data mining techniques (most of them barring a few statistical ones are arti<sup>fi</sup>cial intelligence based) are employed to solve these problems, they work in an objective way by sifting through the records of fraudulent and healthy companies. In the process, they discover knowledge which can be used to predict whether a company at hand will perpetrate <sup>fi</sup>nancial accounting fraud in future. Data mining techniques have another advantage in that they can handle a large number of records and <sup>fi</sup>nancial ratios ef<sup>fi</sup>ciently. According to Kirkos et al. [23], arti<sup>fi</sup>cial intelligence methods have the theoretical advantage that they do not impose arbitrary assumptions on the input variables. An auxiliary aim of this research is to select the most important <sup>fi</sup>nancial items that can explain the <sup>fi</sup>nancial statement fraud. The results obtained using this research will be useful for auditors engaged in the prediction of <sup>fi</sup>nancial statement fraud. In fact, emerging companies can carefully monitor those <sup>fi</sup>nancial statements for getting long-term advantages in the competitive market. Further, it will be useful for investors who plan to invest in such companies.

The rest of the paper is organized as follows. Section 2 reviews the research done in the area of <sup>fi</sup>nancial statement fraud detection. Section 3 provides an overview of the data mining techniques that are used in this paper. Section 4 describes the feature selection phase of data mining. Section 5 presents the results and discusses the implications of these results. Finally, Section 6 concludes the paper.

## 2. Literature review

There has been a limited use of data mining techniques for detection of <sup>fi</sup>nancial statement fraud. The data mining techniques used include decision trees, neural networks (NN), Bayesian belief networks, case based reasoning, fuzzy rule-based reasoning, hybrid methods, logistic regression, and text mining. Extant research in this direction is reviewed in the following paragraphs.

According to Kirkos et al. [23], some estimates stated that fraud cost US business more than \$400 billion annually. Spathis et al [42] compared multi-criteria decision aids with statistical techniques such as logit and discriminant analysis in detecting fraudulent <sup>fi</sup>nancial statements. A novel <sup>fi</sup>nancial kernel for the detection of management fraud is developed using support vector machines on <sup>fi</sup>nancial data by Cecchini et al. [9]. Huang et al. [20] developed an innovative fraud detection mechanism on the basis of Zipf's Law. The purpose of this technique is to assist auditors in reviewing the overwhelming volumes of datasets and identifying any potential fraud records. Kirkos et al. [23] used the ID3 decision tree and Bayesian belief network to detect <sup>fi</sup>nancial statement fraud successfully.

Sohl and Venkatachalam [41] used back-propagation NN for the prediction of <sup>fi</sup>nancial statement fraud. There are other researchers who used different NN algorithms to detect <sup>fi</sup>nancial reporting fraud. Cerullo and Cerullo [10] explained the nature of fraud and <sup>fi</sup>nancial statement fraud along with the characteristics of NN and their applications. They illustrated how NN packages could be utilized by various <sup>fi</sup>rms to predict the occurrence of fraud. Calderon and Cheh [8] examined the ef<sup>fi</sup>cacy of NN as a potential enabler of business risk based auditing. They employed different methods using NN as a tool for research in the auditing and risk assessment domain. Further, they identi<sup>fi</sup>ed several opportunities for future research that include methodological issues related to NN modeling as well as speci<sup>fi</sup>c issues related to the application of NN for business risk assessment. Koskivaara [25] investigated the impact of various preprocessing models on the forecast capability of NN when auditing <sup>fi</sup>nancial accounts. Further, Koskivaara [26] proposed NN based support systems as a possible tool for use in auditing. He demonstrated that the main application areas of NN were detection of material errors, and management fraud. Busta and Weinberg [7] used NN to distinguish between ‘normal’ and ‘manipulated’ <sup>fi</sup>nancial data. They examined the digit distribution of the numbers in the underlying <sup>fi</sup>nancial information. The data analysis is based on Benford’s law, which demonstrated that the digits of naturally occurring numbers are distributed on a predictable and speci<sup>fi</sup>c pattern. They tested six NN designs to determine the most effective model. In each design, the inputs to the NN were the different subsets of the 34 variables. The results showed that NN were able to correctly classify 70.8% of the data on an average.

Feroz et al. [15] observed that the relative success of the NN models was due to their ability to ‘learn’ what were important. The perpetrators of <sup>fi</sup>nancial reporting frauds had incentives to appear prosperous as evidenced by high pro<sup>fi</sup>tability. In contrast to conventional statistical models replete with assumptions, the NN used adaptive learning processes to determine what were important in predicting targets. Thus, the NN approach was less likely to be affected by accounting manipulations. The NN approach was well suited to predicting the possible fraudsters because the NN ‘learnt’ the characteristics of reporting violators despite managers’ intent to obfuscate misrepresentations. Brooks [6] also applied various NN models to detect <sup>fi</sup>nancial statement fraud with great success. Fanning and Cogger [13] used NN (AutoNet) for detecting management fraud. The study offered an in-depth examination of important publicly available predictors of fraudulent <sup>fi</sup>nancial statements. The study reinforced the ef<sup>fi</sup>ciency of AutoNet in providing empirical evidence regarding the merits of suggested red <sup>fl</sup>ags for fraudulent <sup>fi</sup>nancial statements. Ramamoorti et al. [37] provided an overview of the multilayer perceptron architecture and compared it with a Delphi study. They found that internal auditors could bene<sup>fi</sup>t from using NN for assessing risk. Zhang et al. [46] conducted a review of the published papers that reported the use of NN in forecasting during the time period 1988–98.

Aamodt and Plaza [1] and Kotsiantis et al. [27] used case based reasoning to identify the fraudulent companies. Further, Deshmukh and Talluru [12] demonstrated the construction of a rule-based fuzzy reasoning system to assess the risk of management fraud and proposed an early warning system by <sup>fi</sup>nding out 15 rules related to the probability of management fraud. Pacheco et al. [34] developed a hybrid intelligent system consisting of NN and a fuzzy expert system to diagnose <sup>fi</sup>nancial problems. Further, Magnusson et al. [30] used text mining and demonstrated that the language of quarterly reports provided an indication of the change in the company's <sup>fi</sup>nancial status. A rule-based system that consisted of too many if–then statements made it dif<sup>fi</sup>cult for marketing researchers to understand key drivers of consumer behavior [22]. Variable selection was used in order to choose a subset of the original predictive variables by eliminating variables that were either redundant or possessed little predictive information.

## 3. Methodology

The dataset used in this research was obtained from 202 companies that were listed in various Chinese stock exchanges, of which 101 were fraudulent and 101 were non-fraudulent companies. The data also contained 35 <sup>fi</sup>nancial items for each of these companies. Table 1 lists these <sup>fi</sup>nancial items. Of these, 28 were <sup>fi</sup>nancial ratios re<sup>fl</sup>ecting liquidity, safety, pro<sup>fi</sup>tability, and ef<sup>fi</sup>ciency of companies. We performed log transformation on the entire dataset to reduce its dimension. Then we normalized each of the independent variables of the original dataset during the data preprocessing stage. Furthermore, ten-fold cross-validation is performed to improve the reliability of the result. Then, we analyzed the dataset using six data mining techniques including MLFF, SVM, GP, GMDH, LR, and PNN. The block diagram in Fig. 2 depicts the data flow. We chose the six techniques because MLFF, GMDH and PNN fall under the NN category, SVM comes from statistical learning theory, GP is an evolutionary technique, and logistic regression is a traditional statistical technique for classi<sup>fi</sup>cation. Thus, these methods had varied background and different theories to support them. In this way, we ensured that the problem at hand is analyzed by disparate models, that had varying degree of dif<sup>fi</sup>culty in implementation and also exhibited varying degree of performance on different data mining problems. In other words, the problem is studied and analyzed comprehensively from all perspectives.

It is observed that some of the independent variables turned out to be much more important for the prediction purpose whereas some contributed negatively towards the classi<sup>fi</sup>cation accuracies of different classi<sup>fi</sup>ers. So, a simple statistical technique using the t-statistic is used to accomplish feature selection on the dataset by identifying the most signi<sup>fi</sup>cant <sup>fi</sup>nancial items that could detect the presence of <sup>fi</sup>nancial statement fraud. This is described in Section 4. The features having high t-statistic values were more signi<sup>fi</sup>cant than others. For feature selection, <sup>fi</sup>rst we extracted the top 18 features (more than half of the total 35 <sup>fi</sup>nancial items) from the original dataset. Then the dataset with the reduced feature set (only 18 <sup>fi</sup>nancial items) was fed as input to the above mentioned classi<sup>fi</sup>ers, which resulted in new combinations such as t-statistic-MLFF, t-statistic-SVM, t-statistic-GP, t-statistic-GMDH, t-statistic-LR, and t-statistic-PNN. In order to conduct further analysis, we then extracted the top 10 features and the same process was repeated, i.e., the dataset with the reduced feature set (only 10 <sup>fi</sup>nancial items) was fed as input to all of the above classi<sup>fi</sup>ers. A brief description of the different data mining techniques used in this research is provided below

Table 1 Items from <sup>fi</sup>nancial statements of companies that are used for detection of <sup>fi</sup>nancia statement fraud.

<table><tr><td>No.</td><td>Financial items</td></tr><tr><td>1</td><td>Debt</td></tr><tr><td>2</td><td>Total assets</td></tr><tr><td>3</td><td>Gross profit</td></tr><tr><td>4</td><td>Net profit</td></tr><tr><td>5</td><td>Primary business income</td></tr><tr><td>6</td><td>Cash and deposits</td></tr><tr><td>7</td><td>Accounts receivable</td></tr><tr><td>8</td><td>Inventory/Primary business income</td></tr><tr><td>9</td><td>Inventory/Total assets</td></tr><tr><td>10</td><td>Gross profit/Total assets</td></tr><tr><td>11</td><td>Net profit/Total assets</td></tr><tr><td>12</td><td>Current assets/Total assets</td></tr><tr><td>13</td><td>Net profit/Primary business income</td></tr><tr><td>14</td><td>Accounts receivable/Primary business income</td></tr><tr><td>15</td><td>Primary business income/Total assets</td></tr><tr><td>16</td><td>Current assets/Current liabilities</td></tr><tr><td>17</td><td>Primary business income/Fixed assets</td></tr><tr><td>18</td><td>Cash/Total assets</td></tr><tr><td>19</td><td>Inventory/Current liabilities</td></tr><tr><td>20</td><td>Total debt/Total equity</td></tr><tr><td>21</td><td>Long term debt/Total assets</td></tr><tr><td>22</td><td>Net profit/Gross profit</td></tr><tr><td>23</td><td>Total debt/Total assets</td></tr><tr><td>24</td><td>Total assets/Capital and reserves</td></tr><tr><td>25</td><td>Long term debt/Total capital and reserves</td></tr><tr><td>26</td><td>Fixed assets/Total assets</td></tr><tr><td>27</td><td>Deposits and cash/Current assets</td></tr><tr><td>28</td><td>Capitals and reserves/Total debt</td></tr><tr><td>29</td><td>Accounts receivable/Total assets</td></tr><tr><td>30</td><td>Gross profit/Primary business profit</td></tr><tr><td>31</td><td>Undistributed profit/Net profit</td></tr><tr><td>32</td><td>Primary business profit/Primary business profit of last year</td></tr><tr><td>33</td><td>Primary business income/Last year&#x27;s primary business income</td></tr><tr><td>34</td><td>Account receivable /Accounts receivable of last year</td></tr><tr><td>35</td><td>Total assets/Total assets of last year</td></tr></table>

## 3.1. Support vector machines (SVM)

SVM introduced by Vapnik [44] use a linear model to implement nonlinear class boundaries by mapping input vectors nonlinearly into a high-dimensional feature space. In the new space, an optimal separating hyperplane is constructed. The training examples that are closest to the maximum margin hyperplane are called support vectors. All other training examples are irrelevant for de<sup>fi</sup>ning the binary class boundaries. SVM are simple enough to be analyzed mathematically. In this sense, SVM may serve as a promising alternative combining the strengths of conventional statistical methods that are more theory-driven and easy to analyze, and machine learning methods that are more data-driven, distributionfree and robust. Recently, SVM have been used in <sup>fi</sup>nancial applications such as credit rating, time series prediction, and insurance claim frauds detection. These studies reported that the performance of SVM is comparable to and even better than other classi<sup>fi</sup>ers such as MLFF, case based reasoning, discriminant analysis, and logistic regression.

![](/api/attachments/5MAJW4K8/fulltext/images/dc82bda9c4a866c5c185fd8d8521d805e35f3083df3131ec72bf36c4597c5a1d.jpg)  
Fig. 2. Architecture of different classi<sup>fi</sup>ers

## 3.2. Genetic programming (GP)

GP [28] is an extension of genetic algorithms (GA). It is a search methodology belonging to the family of evolutionary computation. GP randomly generates an initial population of solutions. Then, the initial population is manipulated using various genetic operators to produce new populations. These operators include reproduction, crossover, mutation, dropping condition, etc. The whole process of evolving from one population to the next population is called a generation. A highlevel description of the GP algorithm can be divided into a number of sequential steps [14]:

• Create a random population of programs, or rules, using the symbolic expressions provided as the initial population.

• Evaluate each program or rule by assigning a <sup>fi</sup>tness value according to a prede<sup>fi</sup>ned <sup>fi</sup>tness function that can measure the capability of the rule or program to solve the problem.

• Use the reproduction operator to copy existing programs into the new generation.

• Generate the new population with crossover, mutation, or other operators from a randomly chosen set of parents.

• Repeat the second to the fourth steps for the new population until a prede<sup>fi</sup>ned termination criterion is satis<sup>fi</sup>ed, or a <sup>fi</sup>xed number of generations is completed.

• The solution to the problem is the genetic program with the best <sup>fi</sup>tness within all generations.

In GP, the crossover operation is achieved by reproduction of two parent trees. Two crossover points are then randomly selected in the two offspring trees. Exchanging sub-trees, which are selected according to the crossover point in the parent trees, generates the <sup>fi</sup>nal offspring trees. The offspring trees are usually different from their parents in size and shape. Then, mutation operation is also considered in GP. A single parental tree is <sup>fi</sup>rst reproduced. Then a mutation point is randomly selected from the reproduction, which can be either a leaf node or a sub-tree. Finally, the leaf node or the subtree is replaced by a new leaf node or a randomly generated sub-tree. Fitness functions ensure that the evolution goes toward optimization by calculating the <sup>fi</sup>tness value for each individual in the population. The <sup>fi</sup>tness value evaluates the performance of each individual in the population.

GP is guided by the <sup>fi</sup>tness function to search for the most ef<sup>fi</sup>cient computer program that can solve a given problem. A simple measure of <sup>fi</sup>tness [14] is adopted for the binary classi<sup>fi</sup>cation problem and is given as follows:

## No: of samples classified correctly Fitness No: of samples used for training during evaluation

The major considerations in applying GP to pattern classi<sup>fi</sup>cation are:

• GP based techniques are free of the distribution of the data, and so no a priori knowledge is needed about the statistical distribution of the data.

• GP can directly operate on the data in its original form.

• GP can detect the underlying but unknown relationship that exists among data items and express it as a mathematical expression.

• GP can discover the most important discriminating features of a class during the training phase.

## 3.3. Multi-layer feedforward neural network (MLFF)

MLFF is one of the most common NN structures, as they are simple and effective, and have found home in a wide assortment of machine learning applications. MLFF starts as a network of nodes arranged in three layers—the input, hidden, and output layers. The input and output layers serve as nodes to buffer input and output for the model, respectively, and the hidden layer serves to provide a means for input relations to be represented in the output. Before any data is passed to the network, the weights for the nodes are random, which has the effect of making the network much like a newborn's brain—developed but without knowledge. MLFF are feed-forward NN trained with the standard back-propagation algorithm. They are supervised networks so they require a desired response to be trained. They learn how to transform input data into a desired response. So they are widely used for pattern classi<sup>fi</sup>cation and prediction. A multi-layer perceptron is made up of several layers of neurons. Each layer is fully connected to the next one. With one or two hidden layers, they can approximate virtually any input–output map. They have been shown to yield accurate predictions in dif<sup>fi</sup>cult problems [39].

## 3.4. Group method of data handling (GMDH)

GMDH was introduced by Ivakhnenko [21] in 1966 as an inductive learning algorithm for modeling complex systems. It is a selforganizing approach that tests increasingly complicated models and evaluates them using some external criterion on separate parts of the data sample. GMDH is partly inspired by research in perceptrons and learning <sup>fi</sup>lters. GMDH has in<sup>fl</sup>uenced the development of several techniques for synthesizing (or ‘self-organizing’) networks of polynomial nodes. GMDH attempts a hierarchic solution by trying out many simple models, retaining the best of these models, and building on them iteratively to obtain a composition (or feed-forward network) of functions as the model. The building blocks of GMDH, or polynomial nodes, usually have the quadratic form:

$$
z = w _ {0} + w _ {1} x _ {1} + w _ {2} x _ {2} + w _ {3} x _ {1} ^ {2} + w _ {4} x _ {2} ^ {2} + w _ {5} x _ {1} x _ {2}
$$

where x and x are inputs, w is the coef<sup>fi</sup>cient (or weight) vector w, and z is the node output. The coef<sup>fi</sup>cients are determined by solving the linear regression equation with z=y, where y represents the response vector. The GMDH develops on a data set. The data set including independent variables $\left( x _ { 1 } , \ x _ { 2 } , . . . , \ x _ { n } \right)$ and one dependent variable y is split into a training and testing set. During the process of learning a forward multilayer NN is developed by observing the following steps:

• In the input layer of the network n units with an elementary transfer function y=x are constructed. These are used to provide values of independent variables from the learning set to the successive layers of the network.

• When constructing a hidden layer an initial population of units is generated. Each unit corresponds to the Ivakhnenko polynomial form:

$$
\begin{array}{l} y = a + b x _ {1} + c x _ {2} + d x _ {1} ^ {2} + e x _ {1} x _ {2} + f x _ {2} ^ {2} \text {or} \\ y = a + b x _ {1} + c x _ {2} + d x _ {1} x _ {2} \end{array}
$$

where y is an output variable; x x are two input variables; and a $\mathbf { \nabla } , b , \ldots f$ are parameters.

• Parameters of all units in the layer are estimated using the learning set.

• The mean square error between the dependent variable y and the response of each unit is computed for the testing set.

• Units are sorted in terms of the mean square error and just a few units with minimal error survive. The rest of the units are deleted. This step guarantees that only units with a good ability for approximation are chosen.

• Next the hidden layers are constructed so that the mean square error of the best unit decreases.

• Output of the network is considered as the response of the best unit in the layer with the minimal error.

Table 2  
Top 18 items selected from <sup>fi</sup>nancial statements of companies by t-statistic based feature selection.

<table><tr><td>No.</td><td>Financial items</td></tr><tr><td>1</td><td>Net profit</td></tr><tr><td>2</td><td>Gross profit</td></tr><tr><td>3</td><td>Primary business income</td></tr><tr><td>4</td><td>Primary business income/Total assets</td></tr><tr><td>5</td><td>Gross profit/Total assets</td></tr><tr><td>6</td><td>Net profit/Total assets</td></tr><tr><td>7</td><td>Inventory/Total assets</td></tr><tr><td>8</td><td>Inventory/Current liabilities</td></tr><tr><td>9</td><td>Net profit/Primary business income</td></tr><tr><td>10</td><td>Primary business income/Fixed assets</td></tr><tr><td>11</td><td>Primary business profit/Primary business profit of last year</td></tr><tr><td>12</td><td>Primary business income/Last year&#x27;s primary business income</td></tr><tr><td>13</td><td>Fixed assets/Total assets</td></tr><tr><td>14</td><td>Current assets/Current liabilities</td></tr><tr><td>15</td><td>Capitals and reserves/Total debt</td></tr><tr><td>16</td><td>Long term debt/Total capital and reserves</td></tr><tr><td>17</td><td>Cash and deposits</td></tr><tr><td>18</td><td>Inventory/Primary business income</td></tr></table>

The GMDH network learns in an inductive manner and builds a function (called a polynomial model), that results in the minimum error between the predicted value and expected output. The majority of GMDH networks use regression analysis for solving the problem. The <sup>fi</sup>rst step is to decide the type of polynomial that the regression will <sup>fi</sup>nd. The initial layer is simply the input layer. The <sup>fi</sup>rst layer is created by computing regressions of the input variables and then choosing the best ones. The second layer is created by computing regressions of the values in the <sup>fi</sup>rst layer along with the input variables. This means that the algorithm essentially builds polynomials of polynomials. Again, only the best are chosen by the algorithm. These are called survivors. This process continues until a pre-speci<sup>fi</sup>ed selection criterion is met.

## 3.5. Logistic regression (LR)

According to Panik [35], when dealing with logistic regression, the response variable is taken to be dichotomous or binary (it takes on only two possible values), i.e., $y _ { i } = 0$ or 1 for all $i = 1 , . . . , n$ . For instance, we can have a situation in which the outcome of some process of observation is either a success (we record a 1) or failure (we record a 0), or we observe the presence (1) or absence (0) of some characteristic or phenomenon. In addition, dichotomous variables are useful for making predictions, e.g., we may ask the following: Will an individual make a purchase of a particular item in the near future?

$$
\text { Here } y _ {i} = \left\{ \begin{array}{l} 1, y e s; \\ 0, N o. \end{array} \right.
$$

According to Williams et al. [45], LR is a commonly used approach for performing binary classi<sup>fi</sup>cation. It learns a set of parameters, {w , w}, that maximizes the likelihood of the class labels for a given set of training data. Let $x _ { i } \in R ^ { d }$ denote a (column) vector of d features representing the ith data point, and $y _ { i } \in \{ 0 , 1 \}$ denote its corresponding class label (e.g., clutter or mine). For a labeled (training) data point, $y _ { i }$ is known; for an unlabeled (testing) data point, $y _ { i }$ is unknown. Under the LR model, the probability of label $y _ { i } = 1$ given $x _ { i }$ is given by $\operatorname { E q . }$ . (1):

$$
\psi_ {i} \equiv p (y _ {i} = 1 | x _ {i}) = \frac {\exp \left(w _ {0} + w ^ {T} x _ {i}\right)}{1 + \exp \left(w _ {0} + w ^ {T} x _ {i}\right)}\tag{1}
$$

where $w _ { 0 } \in R$ and $w \in R ^ { d }$ are the LR intercept and coef<sup>fi</sup>cients respectively. For a set of N independent labeled data points, $\{ x _ { i } ,$ $y _ { i } \} _ { i = 1 } ^ { \bar { N } } ,$ , the log-likelihood of the class labels can be written as Eq. (2):

$$
l (w _ {0}, w) = \sum_ {i = 1} ^ {n} \left[ (1 - y _ {i}) l o g (1 - \psi_ {i}) + y _ {i} l o g \psi_ {i} \right]\tag{2}
$$

To maximize the log-likelihood in Eq. (2), a standard optimization approach can be employed, since the gradient (and Hessian) of Eq. (2) with respect to $\{ w _ { 0 } , w \}$ can be readily calculated. Once the LR parameters $\{ w _ { 0 } , w \}$ have been learned, the probability that an unlabeled testing data point $x _ { i }$ belongs to each class can be obtained using Eq. (1).

## 3.6. Probabilistic neural network (PNN)

PNN is a feed-forward NN involving a one pass training algorithm used for classi<sup>fi</sup>cation and mapping of data. PNN was introduced by Specht [43] in 1990. It is a pattern classi<sup>fi</sup>cation network based on the classical Bayes classi<sup>fi</sup>er, which is statistically an optimal classi<sup>fi</sup>er that seeks to minimize the risk of misclassi<sup>fi</sup>cation. Any pattern classi<sup>fi</sup>er places each observed data vector $\mathbf { x } = [ x _ { 1 } , x _ { 2 } , x _ { 3 } \dots x _ { N } ] ^ { T }$ in one of the prede<sup>fi</sup>ned classes $c _ { i } , i = 1 , 2 , \ldots ,$ , m where m is the number of possible classes. The effectiveness of any classi<sup>fi</sup>er is limited by the number of data elements that the vector x can have and the number of possible classes m. The classical Bayes pattern classi<sup>fi</sup>er [40] implements the Bayes conditional probability rule that the probability $P ( c _ { i } | \mathbf { x } )$ of x being in class $c _ { i }$ is given by:

$$
P (c _ {i} | \mathrm{x}) = \frac {P (\mathrm{x} | c _ {i}) P (c _ {i})}{\sum_ {j = 1} ^ {m} P (\mathrm{x} | c _ {j}) P (c _ {j})}\tag{3}
$$

where $P ( \mathbf { x } | c _ { i } )$ is the conditioned probability density function of x given set $c _ { i } , P ( c _ { j } )$ is the probability of drawing data from class $c _ { j } .$ Vector x is said to belong to a particular class $c _ { i , } \operatorname { i f } P ( c _ { i } | \mathbf { x } ) > P ( c _ { j } | \mathbf { x } ) , \forall j = 1 , 2 , . . . ,$ m and $j \neq i .$ . This input x is fed into each of the patterns in the pattern layer. The summation layer computes the probability $P ( c _ { i } | \mathbf { x } )$ that the given input x is included in each of the classes $c _ { i }$ that is represented by the patterns in the pattern layer. The output layer selects the class for which the highest probability is obtained in the summation layer. The input is then made to belong to this class. The effectiveness of the network in classifying input vectors depends on the value of the smoothing parameter.

## 4. Feature selection

Feature selection is critical to data mining and knowledge based authentication. The problem of feature selection has been well studied in areas where datasets with a large number of features are available, including machine learning, pattern recognition, and statistics. Piramuthu [36] observed that about 80% of the resources in a majority of data mining applications are spent on cleaning and preprocessing the data, and developed a new feature selection method based on Hausdorff distance for analyzing web traf<sup>fi</sup>c data. Feature selection is of paramount importance for any learning algorithm which when poorly done (i.e., a poor set of features is selected) may lead to problems related to incomplete information, noisy or irrelevant features, not the best set/mix of features, among others [45]. Mladenic and Grobelnik [31] reviewed various feature selection methods in the context of web mining. Chen and Liginlal [11] developed a maximum entropy based feature selection technique for knowledge based authentication.

In this study, we employed a feature selection phase by using the simple t-statistic technique. t-statistic is one of the ef<sup>fi</sup>cient feature selection techniques. The features are ranked according to the formula shown below [16,29]. In fact, Liu et al. [29] were the <sup>fi</sup>rst to propose t-statistic for the purpose of feature selection in the <sup>fi</sup>eld of bioinformatics.

![](/api/attachments/5MAJW4K8/fulltext/images/6bb225f96a53a38b4092522788450e3c2058c10053c4773760553c0aeac9a10b.jpg)  
Fig. 3. Architecture of different classi<sup>fi</sup>ers after feature selection.

$$
t - \text { statistic } = \frac {\left| \mu_ {1} - \mu_ {2} \right|}{\sqrt {\frac {\sigma_ {1} ^ {2}}{n _ {1}} + \frac {\sigma_ {2} ^ {2}}{n _ {2}}}}\tag{4}
$$

where $\mu _ { 1 }$ and $\mu _ { 2 }$ represent the means of the samples of fraudulent companies and non-fraudulent companies for a given feature respectively, $\sigma _ { 1 }$ and $\sigma _ { 2 }$ represent the standard deviation of the samples of fraudulent companies and non-fraudulent companies for a given feature respectively. n and n represent the number of samples of fraudulent companies and non-fraudulent companies for a given feature. The t-statistic values are computed for each feature and the top 18 features with the highest t-statistic values are considered in the <sup>fi</sup>rst case and the top 10 features are considered in the second case. A high t-statistic value indicates that the feature can highly discriminate between the samples of fraudulent and non-fraudulent companies. The top 18 <sup>fi</sup>nancial features that are selected by the t-statistic based feature selection are shown in Table 2. The feature subset formed with the top 18 features is fed as input to MLFF/SVM/GP/GMDH/LR/PNN for classi<sup>fi</sup>cation purpose in the <sup>fi</sup>rst case. Similarly, the feature subset formed with the top 10 features is fed as input to MLFF/SVM/GP/ GMDH/LR/PNN for classi<sup>fi</sup>cation purpose in the second case. The block diagram for all these combinations is shown in Fig. 3. Ten-fold crossvalidation is used to ensure better validity of the experiments. It should be noted that the t-statistic is employed for feature selection for each fold separately. It is observed that the same set of features did not turn out to be best in each fold. Hence, we followed a frequency based approach, whereby, the frequency of occurrence of each of the features in top slots is computed and the features are then sorted in the descending order of the frequency of occurrences. In this manner, we selected the top 10 and top 18 features and reported them in Table 2.

## 5. Results and discussion

The dataset analyzed in this paper comprised 35 <sup>fi</sup>nancial items for 202 companies, of which 101 were fraudulent and 101 were nonfraudulent. Since the <sup>fi</sup>nancial items had a wide range, we <sup>fi</sup>rst performed natural logarithmic transformation, and then normalization during the data preprocessing phase. We employed the GP as implemented in the tool Discipulus (available at www.rmltech.com and downloaded on 20th August, 2008). For MLFF, GMDH, and PNN, we employed Neuroshell 2.0 [33] and for SVM and LR we used KNIME 2.0.0 [24].

Average results of dataset with all features using 10-fold cross-validation.

<table><tr><td>Classifier</td><td>Accuracy</td><td>Sensitivity</td><td>Specificity</td><td>AUC</td></tr><tr><td>MLFF</td><td>78.36</td><td>80.21</td><td>76.35</td><td>7827.90</td></tr><tr><td>SVM</td><td>70.41</td><td>55.43</td><td>84.13</td><td>6978.00</td></tr><tr><td>GP</td><td>94.14</td><td>95.09</td><td>93.05</td><td>9407.10</td></tr><tr><td>GMDH</td><td>93.00</td><td>91.46</td><td>95.18</td><td>9331.85</td></tr><tr><td>LR</td><td>66.86</td><td>63.32</td><td>70.66</td><td>6699.10</td></tr><tr><td>PNN</td><td>98.09</td><td>98.09</td><td>98.09</td><td>9809.00</td></tr><tr><td>CDA [5]</td><td>71.37</td><td>61.96</td><td>80.77</td><td>7136.5</td></tr><tr><td>C&amp;RT [5]</td><td>72.38</td><td>72.40</td><td>72.36</td><td>7238</td></tr><tr><td>Exhaustive pruning NN [5]</td><td>77.14</td><td>80.83</td><td>73.45</td><td>7714</td></tr></table>

The sensitivity is the measure of the proportion of the number of fraudulent companies predicted correctly as fraudulent by a particular model to the total number of actual fraudulent companies. The speci<sup>fi</sup>city is the measure of the proportion of the number of nonfraudulent companies predicted as non-fraudulent by a model to the total number of actual non-fraudulent companies. In all cases, we presented the average accuracies, sensitivities, speci<sup>fi</sup>cities, and area under the Receiver Operating Characteristic curve (AUC) for the test data, averaged over 10-folds. We ranked the classi<sup>fi</sup>ers based on AUC. First, the results of the 10-fold cross-validation method for the standalone techniques viz. MLFF, SVM, GP, GMDH, LR, and PNN without feature selection are presented in Table 3. From Table 3 we observe that PNN with 98.09% accuracy and 98.09% sensitivity outperformed all other classi<sup>fi</sup>ers (as indicated by bold faced numerals in the Table 3). GP yielded the next best result with 94.14% accuracy and 95.09% sensitivity. We also observe that PNN is the best classi<sup>fi</sup>er among all others in terms of AUC as well. The best results obtained by Bose and Wang [5], who employed canonical discriminant analysis (CDA), classi<sup>fi</sup>cation and regression tree (C&RT) and exhaustive pruning NN on the same dataset are also presented in Table 3 for ease of comparison. From Table 3 we can observe that the results obtained in this study are always superior to the results obtained by them for all cases, except SVM and LR.

As the next step, we used t-statistic for feature selection and extracted the most important features. First, we considered the top 18 features for constructing the reduced feature subset. Later, this feature subset is fed to all the above classi<sup>fi</sup>ers for the purpose of classi<sup>fi</sup>cation. The average results of all the classi<sup>fi</sup>ers over all folds with 18 features are presented in Table 4. From Table 4 we observe that GP outperformed other classi<sup>fi</sup>ers with 92.68% accuracy and 90.55% sensitivity, whereas PNN came close behind with 95.64% accuracy and 91.27% sensitivity (as indicated by bold faced numerals in Table 4). Furthermore, results based on AUC indicated that GP yielded highest accuracy followed by PNN, which yielded marginally less accuracy. This makes us infer that the selected feature subsets have a high discriminatory power and the ‘left-over’ features have very little to contribute to the success of <sup>fi</sup>nancial fraud detection. Furthermore, in order to conduct an exhaustive study over this dataset, in the second set of experiment we considered only the top 10 features (based on the values of the t-statistics) for constructing the reduced feature subset. The top 10 features can be seen in the <sup>fi</sup>rst ten rows of Table 2. We repeated the experiments as in the <sup>fi</sup>rst case. The average results for all the classi<sup>fi</sup>ers over all folds with 10 features are presented in Table 5. From Table 5 we observe that PNN outperformed other classi<sup>fi</sup>ers with 90.77% accuracy and 87.53% sensitivity (as indicated by bold faced numerals in Table 5), whereas GP came second with 89.27% accuracy and 85.64% sensitivity. Moreover, results based on the AUC indicated that PNN yielded the highest accuracy followed by GP, which yielded only marginally less accuracy.

Table 4  
Average results of dataset with reduced features (top 18 features selected by t-statistic) and using 10-fold cross-validation.

<table><tr><td>Classifier</td><td>Accuracy</td><td>Sensitivity</td><td>Specificity</td><td>AUC</td></tr><tr><td>MLFF</td><td>78.77</td><td>76.98</td><td>81.28</td><td>7912.80</td></tr><tr><td>SVM</td><td>73.41</td><td>72.07</td><td>75.04</td><td>7355.55</td></tr><tr><td>GP</td><td>92.68</td><td>90.55</td><td>95.27</td><td>9290.95</td></tr><tr><td>GMDH</td><td>90.68</td><td>93.46</td><td>88.34</td><td>9089.95</td></tr><tr><td>LR</td><td>70.36</td><td>62.91</td><td>78.88</td><td>7089.50</td></tr><tr><td>PNN</td><td>95.64</td><td>91.27</td><td>94.16</td><td>9271.75</td></tr></table>

Table 5  
Table 8  
Average results of dataset with reduced features (top 10 features selected by t-statistic) and using 10-fold cross-validation.

<table><tr><td>Classifier</td><td>Accuracy</td><td>Sensitivity</td><td>Specificity</td><td>AUC</td></tr><tr><td>MLFF</td><td>75.32</td><td>67.24</td><td>82.79</td><td>7501.65</td></tr><tr><td>SVM</td><td>72.36</td><td>73.60</td><td>69.68</td><td>7164.35</td></tr><tr><td>GP</td><td>89.27</td><td>85.64</td><td>93.16</td><td>8939.95</td></tr><tr><td>GMDH</td><td>88.14</td><td>87.44</td><td>89.25</td><td>8834.40</td></tr><tr><td>LR</td><td>70.86</td><td>65.23</td><td>76.46</td><td>7084.45</td></tr><tr><td>PNN</td><td>90.77</td><td>87.53</td><td>94.07</td><td>9079.85</td></tr></table>

In order to <sup>fi</sup>nd out whether the difference in average AUCs is statistically signi<sup>fi</sup>cant or not, we conducted a t-test between the top performer and the remaining classi<sup>fi</sup>ers (i) without feature selection, (ii) with feature selection including top 18 features, and (iii) with feature selection including top 10 features. In case of the dataset without feature selection, the t-statistic values between the average AUCs obtained by PNN and that of other classi<sup>fi</sup>ers are presented in Table 6. From Table 6 we observe that t-statistic values are more than the critical value of the test statistic, which is 1.73 at the 10% level of signi<sup>fi</sup>cance. Thus, we infer that PNN signi<sup>fi</sup>cantly outperformed other classi<sup>fi</sup>ers without feature selection. In case of the dataset with feature selection and considering only the top 18 features, the t-statistic values between the average AUCs obtained by GP and that of other classi<sup>fi</sup>ers are presented in Table 7. From this table we can observe that t-statistic values are more than 1.73 in case of MLFF, SVM and LR, whereas those values are less than 1.73 in case of PNN and GMDH. From these results we can say that the GP signi<sup>fi</sup>cantly outperformed all classi<sup>fi</sup>ers except GMDH and PNN. Considering only the top 10 features, the t-statistic values between the average AUCs obtained by PNN and that of other classi<sup>fi</sup>ers are presented in Table 8. From this table we can observe that t-statistic values are more than 1.73 in case of MLFF, SVM and LR, whereas those values are less than 1.73 in case of GP and GMDH. From these results we can say that PNN outperformed all classi<sup>fi</sup>ers except GP and GMDH

When we take a close look at the top 10 and top 18 features shown in Table 2, we observe that most of these features are associated with the <sup>fi</sup>rm's ability to generate pro<sup>fi</sup>t or income. Among the top 10 features, eight features are associated with the pro<sup>fi</sup>tability of the <sup>fi</sup>rm. A closer looks reveals that among the top 10 features, four are associated with primary business income, and <sup>fi</sup>ve are associated with either gross or net pro<sup>fi</sup>t earned by the <sup>fi</sup>rm. This indicated that a fraudulent <sup>fi</sup>rm usually tried to in<sup>fl</sup>ate the pro<sup>fi</sup>t or the income <sup>fi</sup>gures in order to create an impressive <sup>fi</sup>nancial statement. Any unusual income or pro<sup>fi</sup>t <sup>fi</sup>gures should be a reason for suspicion and further investigation by an auditor.

t-statistic values of average AUCs of PNN compared to that of other classi<sup>fi</sup>ers without feature selection.

<table><tr><td>Classifier compared</td><td>t-statistic at 10% level of significance</td></tr><tr><td>MLFF</td><td>7.84</td></tr><tr><td>SVM</td><td>15.66</td></tr><tr><td>GP</td><td>2.11</td></tr><tr><td>GMDH</td><td>2.49</td></tr><tr><td>LR</td><td>11.58</td></tr></table>

Table 7  
t-statistic values of average AUCs of GP compared to that of other classi<sup>fi</sup>ers with (top 18 features) feature selection.

<table><tr><td>Classifier compared</td><td>t-statistic at 10% level of significance</td></tr><tr><td>MLFF</td><td>5.13*</td></tr><tr><td>SVM</td><td>5.28*</td></tr><tr><td>GMDH</td><td>0.69</td></tr><tr><td>LR</td><td>6.40*</td></tr><tr><td>PNN</td><td>0.08</td></tr></table>

The \* indicates that the result is statistically signi<sup>fi</sup>cant

When the present dataset of 35 dimensions (<sup>fi</sup>nancial items) is visualized using the tool Neucom [32] in the principal component dimensions by plotting the <sup>fi</sup>rst principal component on x-axis and the second principal component on y-axis, we noticed three predominant clusters and nine outliers. This provided a possible reason for the spectacular performance of PNN because PNN is tolerant to outliers [4]. While comparing the dataset with and without feature selection, it is noticed that even after reducing the number of features to almost one third of the original number, the change in accuracies is at most 5% in all the cases except PNN, where the accuracies are reduced by 8%. From this we can infer that the tstatistic is a simple and ef<sup>fi</sup>cient feature selection technique for picking up very signi<sup>fi</sup>cant features that ensured better accuracies. Based on our experiments, we conclude that PNN without feature selection outperformed methods such as MLFF, SVM, GP, GMDH, and LR. After feature selection, GP performed well compared to all other techniques, and PNN yielded marginally less accuracies when top 18 features are selected. Similarly, PNN outperformed all other techniques when top 10 features are selected. Also, we concluded that our results are much superior to an earlier study on the same dataset.

It should be noted that while all the techniques have equal cost, the technique that is preferred and recommended is totally dictated by the dataset at hand. Since accuracy is a major concern for <sup>fi</sup>nancial analysts, we should select that technique which yields less misclassi<sup>fi</sup>cations and consumes less time. This is because the performance of all of these techniques depends on the dataset on which they are used. Having said that, everything else (i.e., accuracies, sensitivity, speci<sup>fi</sup>city, etc.) being equal, we should select that technique which is less cumbersome, easy to understand, and easy to implement.

t-statistic values of average AUCs of PNN compared to that of other classi<sup>fi</sup>ers with (top 10 features) feature selection.

<table><tr><td>Classifier compared</td><td>t-statistic at 10% level of significance</td></tr><tr><td>MLFF</td><td>5.36*</td></tr><tr><td>SVM</td><td>5.69*</td></tr><tr><td>GP</td><td>0.41</td></tr><tr><td>GMDH</td><td>0.83</td></tr><tr><td>LR</td><td>6.35*</td></tr></table>

The \* indicates that the result is statistically signi<sup>fi</sup>cant.

## 6. Conclusion and future research directions

This paper presents the application of intelligent techniques to predict <sup>fi</sup>nancial statement fraud in companies. The dataset consisting of 202 Chinese companies is analyzed using the stand-alone techniques like MLFF, SVM, GMDH, GP, LR, and PNN. Then, t-statistic is used for feature subset selection and top 18 features are selected in the <sup>fi</sup>rst case and top 10 features are selected in the second case. With the reduced feature subset the classi<sup>fi</sup>ers MLFF, SVM, GMDH, GP, LR, and PNN are invoked again. Results based on AUC indicated that the PNN was the top performer followed by GP which yielded marginally less accuracies in most of the cases. Also, the results obtained in this study are better than those obtained in an earlier study on the same dataset. Ten-fold cross-validation is performed throughout the study. Prediction of <sup>fi</sup>nancial fraud is extremely important as it can save huge amounts of money from being embezzled. Our study is an important step in that direction that highlights the use of data mining for solving this serious problem.

With regards to the future research directions, we can extend this work by extracting ‘if–then’ rules from different classi<sup>fi</sup>ers. These rules can be helpful for easy understanding of the prediction process for the end user because they make the knowledge learnt by these techniques transparent. This type of knowledge elicitation can help in providing early warning. In addition to the data mining techniques used in this research, hybrid data mining techniques that combine two or more classi<sup>fi</sup>ers can be used on the same dataset. Also, text mining algorithms for sentiment analysis of the textual description of the <sup>fi</sup>nancial statements can be used together with data mining algorithms for assessing the <sup>fi</sup>nancial items in the <sup>fi</sup>nancial statements to provide better prediction of <sup>fi</sup>nancial statement fraud.

## Acknowledgments

We are very thankful to Mr. Frank Francone for giving us permission to use the Discipulus tool (demo version) for conducting various numerical experiments reported in this paper. We want to thank the three anonymous reviewers for their insightful comments which helped to improve the quality of this paper.

## References

[1] A. Aamodt, E. Plaza, Case-based reasoning: foundational issues, methodological variations, and system approaches, Arti<sup>fi</sup>cial Intelligence Communications 7 (1) (1994) 39–59.

[2] E.I. Altman, Financial ratios, discriminant analysis and prediction of corporate bankruptcy, The Journal of Finance 23 (4) (1968) 589–609.

[3] W.H. Beaver, Financial ratios as predictors of failure, Journal of Accounting Research 4 (1966) 71-111.

[4] D.P. Berrar, C.S. Downes, W. Dubitzky, Multiclass cancer classi<sup>fi</sup>cation using gene expression pro<sup>fi</sup>ling and probabilistic neural networks, Proceedings of the Paci<sup>fi</sup>c Symposium on Biocomputing, vol. 8, 2003, pp. 5–16.

[5] I. Bose, J. Wang, Data mining for detection of <sup>fi</sup>nancial statement fraud in Chinese companies, Working Paper, The University of Hong Kong, 2008.

[6] R.C. Brooks, Neural networks: a new technology, The CPA Journal Online, http:/ www.nysscpa.org/cpajournal/old/15328449.htm1994.

[7] B. Busta, R. Weinberg, Using Benford's law and neural networks as a review procedure, Managerial Auditing Journal 13 (6) (1998) 356–366.

[8] T.G. Calderon, J.J. Cheh, A roadmap for future neural networks research in auditing and risk assessment, International Journal of Accounting Information Systems 3 (4) (2002) 203–236.

[9] M. Cecchini, H. Aytug, G.J. Koehler, and P. Pathak. Detecting Management Fraud in Public Companies. http://warrington.u<sup>fl</sup>.edu/isom/docs/papers/ DetectingManagementFraudInPublicCompanies.pdf

[10] M.J. Cerullo, V. Cerullo, Using neural networks to predict <sup>fi</sup>nancial reporting fraud: Part 1, Computer Fraud & Security 5 (1999) 14–17.

[11] Y. Chen, D. Liginlal, A maximum entropy approach to feature selection in knowledge-based authentication, Decision Support Systems 46 (1) (2008) 388–398.

[12] A. Deshmukh, L. Talluru, A rule-based fuzzy reasoning system for assessing the risk of management fraud, International Journal of Intelligent Systems in Accounting, Finance & Management 7 (4) (1998) 223–241.

[13] K.M. Fanning, K.O. Cogger, Neural network detection of management fraud using published <sup>fi</sup>nancial data, International Journal of Intelligent Systems in Account ing, Finance, and Management 7 (1) (1998) 21–41.

[14] K.M. Faraoun, A. Boukelif, Genetic programming approach for multi-category pattern classi<sup>fi</sup>cation applied to network intrusion detection, International Journal of Computational Intelligence and Applications 6 (1) (2006) 77–99.

[15] E.H. Feroz, T.M. Kwon, V. Pastena, K.J. Park, The ef<sup>fi</sup>cacy of red <sup>fl</sup>ags in predicting the SEC's targets: an arti<sup>fi</sup>cial neural networks approach, International Journal of Intelligent Systems in Accounting, Finance, and Management 9 (3) (2000) 145–157.

[16] X. Fu, F. Tan, H. Wang, Y.Q. Zhang, R. Harrison, Feature similarity based redundancy reduction for gene selection, Proceedings of the International Conference on Data Mining (Las Vegas, NV, USA), June 26–29, 2006.

[17] http://en.wikipedia.org/wiki/Enron.

[18] http://en.wikipedia.org/wiki/MCI\_Inc.

[19] http://www.examiner.com/x-17547-Financial-Fraud-Examiner\~y2009m7d17- Financial-Fraud-101-Understanding-the-Fraud-Triangle.

[20] S.-M. Huang, D.C. Yen, L.-W. Yang, J.-S. Hua, An investigation of Zipf's Law for fraud detection. Decision Support Systems 46 (1) (2008) 70–83

[21] A.G. Ivakhnenko, The group method of data handling—a rival of the method of stochastic approximation, Soviet Automatic Control 13 (3) (1966) 43–55.

[22] Y. Kim, Toward a successful CRM: variable selection, sampling, and ensemble Decision Support Systems 41 (2) (2006) 542–553.

[23] E. Kirkos, C. Spathis, Y. Manolopoulos, Data mining techniques for the detection of fraudulent <sup>fi</sup>nancial statement, Expert Systems with Applications 32 (2007) 995–1003.

[24] KNIME 2.0.0. http://www.knime.org

[25] E. Koskivaara, Different pre-processing models for <sup>fi</sup>nancial accounts when using neural networks for auditing, Proceedings of the 8th European Conference on Information Systems, vol. 1, 2000, pp. 326–3328, Vienna, Austria.

[26] E. Koskivaara, Arti<sup>fi</sup>cial neural networks in auditing: state of the art, The ICFAI Journal of Audit Practice 1 (4) (2004) 12–33.

[27] S. Kotsiantis, E. Koumanakos, D. Tzelepis, V. Tampakas, Forecasting fraudulent <sup>fi</sup>nancial statements using data mining, International Journal of Computational Intelligence 3 (2) (2006) 104–110.

[28] J.R. Koza, Genetic programming: on the programming of computers by means of natural selection, MIT press, Cambridge, MA, 1992.

[29] H. Liu, J. Li, L. Wong, A comparative study on feature selection and classi<sup>fi</sup>cation methods using gene expression pro<sup>fi</sup>les and proteomic patterns, Genome Informatics 13 (2002) 51–60.

[30] C. Magnusson, A. Arppe, T. Eklund, B. Back, H. Vanharanta, A. Visa, The language of quarterly reports as an indicator of change in the company's <sup>fi</sup>nancial status, Information & Management 42 (4) (2005) 561–574.

[31] D. Mladenic, M. Grobelnik, Feature selection on hierarchy of web documents, Decision Support Systems 35 (1) (2003) 45–87.

[32] Neucom, http://www.aut.ac.nz/research/research-institutes/kedri/research-centres/ centre-for-data-mining-and-decision-support-systems/neucom-project-homepage#download.

[33] Neuroshell 2.0, Ward Systems Inc. http://www.wardsystems.com

[34] R. Pacheco, A. Martins, R.M. Barcia, S. Khator, A hybrid intelligent system applied to <sup>fi</sup>nancial statement analysis, Proceedings of the 5th IEEE conference on Fuzzy Systems, vol. 2, 1996, pp. 1007–10128, New Orleans, LA, USA.

[35] M. Panik, Regression Modeling Methods, Theory, and Computation with SAS, CRC Press. 2009

[36] S. Piramuthu, On learning to predict web traf<sup>fi</sup>c, Decision Support Systems 35 (2) (2003) 213-229

[37] S. Ramamoorti, A.D. Bailey Jr., R.O. Traver, Risk assessment in internal auditing: a neural network approach, International Journal of Intelligent Systems in Accounting, Finance & Management 8 (3) (1999) 159–180.

[38] M. Ramos, Auditor's responsibility for fraud detection, Journal of Accountancy 195 (1) (2003) 28–35.

[39] G.E. Rumelhart, G.E. Hinton, R.J. Williams, Learning Internal Representations by Error Propagation, MIT Press, Cambridge, MA, 1986.

[40] M.F. Selekwa, V. Kwigizile, R.N. Mussa, Setting up a probabilistic neural network for classi<sup>fi</sup>cation of highway vehicles, International Journal of Computational Intelligence and Applications 5 (4) (2005) 411–423.

[41] J.E. Sohl, A.R. Venkatachalam, A neural network approach to forecasting model selection, Information & Management 29 (6) (1995) 297–303.

[42] C. Spathis, M. Doumpos, C. Zopounidis, Detecting falsi<sup>fi</sup>ed <sup>fi</sup>nancial statements: a comparative study using multicriteria analysis and multivariate statistical techniques, European Accounting Review 11 (3) (2002) 509–535.

[43] D.F. Specht, Probabilistic neural networks, Neural Networks 3 (1990) 110–118.

[44] V. Vapnik, Adaptive and learning systems for signal processing, in: HaykinS. (Ed.), Statistical Learning Theory, John Wiley and Sons, 1998.

[45] D.P. Williams, V. Myers, M.S. Silvious, Mine classi<sup>fi</sup>cation with imbalanced data, IEEE Geoscience and Remote Sensing Letters 6 (3) (2009) 528–532.

[46] G. Zhang, B.E. Patuwo, M.Y. Hu, Forecasting with arti<sup>fi</sup>cial neural networks: the state of the art, International Journal of Forecasting 14 (1) (1998) 35–62.

Pediredla Ravisankar is working as a Software Engineer in Capgemini, Hyderabad since February, 2010. He obtained his M.Tech (Information Technology) with specialization in Banking Technology and Information Security from UoH and IDRBT, Hyderabad (2009) and M.Sc. (Physics) from UoH, Hyderabad (2007). He has published papers in Knowledge-Based Systems, Information Sciences, International Journal of Data Mining, Modeling and Management and an IEEE conference paper. He is nominated for Marquis Who's Who in the world for 2011, His research interests include data mining soft computing, evolutionary algorithms, neural networks and their applications.

Vadlamani Ravi is an Associate Professor in the Institute for Development and Research in Banking Technology (IDRBT), Hyderabad, since April 2010. He obtained his Ph.D. in Soft Computing from Osmania University, Hyderabad and RWTH Aachen, Germany (2001); MS (Science and Technology) from BITS, Pilani (1991) and M.Sc. (Statistics & Operations Research) from IIT, Bombay (1987). Prior to joining IDRBT, he worked as a Faculty at the Institute of Systems Science (ISS), National University of Singapore for three years. Earlier, he worked as Assistant Director at the Indian Institute of Chemical Technology (IICT), Hyderabad. He was deputed to RWTH Aachen (Aachen University of Technology) Germany under the DAAD Long Term Fellowship to carry out advanced research during 1997–1999. In a career spanning 22 years, Dr. Ravi has worked in the applications of Fuzzy Computing, Neuro Computing, Soft Computing, Data Mining, Global/Multi-Criteria/ Combinatorial Optimization and Multivariate Statistics in Financial Engineering, Software Engineering, Reliability Engineering, Chemical Engineering, Environmental Engineering, Chemistry, Medical Entomology, Bioinformatics and Geotechnical Engineering. He published 93 papers in refereed International / National Journals / Conferences and invited chapters in edited volumes. He edited a Book on “Advances in Banking Technology and Management: Impact of ICT and CRM”, published by IGI Global, USA, 2007. Further, he is a referee for 25 International Journals of repute in Computer Science, Operations Research, Computational Statistics, Economics and Finance. Moreover, he is an Editorial board member of International Journal of Information Systems in the Service Sector (IJISSS), IGI Global, USA, International Journal of Data Analysis Techniques and Strategies (IJDATS), Inderscience Publications, Switzerland, International Journal of Information and Decision Sciences (IJIDS), Inderscience Publications, Switzerland, International Journal of Information Technology Project Management (IJITPM), IGI Global, USA. His current research interests include Bankruptcy Prediction, CRM, Churn Prediction, FOREX rate prediction, Risk Modeling and Asset Liability Management through Optimization, Software reliability prediction, Software development cost estimation. He is listed in Marquis Who's Who in the World 2009, 2010: Marquis Who's Who in Science and Engineering in 2011. Also, he is an Invited Member of the 2000 Outstanding Intellectuals of the 21st Century 2009/2010 and 100 Top Educators in 2009 both published by International Biographical Center, UK.

Gundumalla Raghava Rao is working as Research Associate for IDRBT since May 2009. He holds an M.Tech (Computer Science & Engineering) from National Institute of Technology, Rourkela in 2008. He holds a B.Tech (Computer Science & Engineering) from M.I.T.S, Rayagada under Biju Patnaik University of Technology, Orissa. His research interests include data mining.

Indranil Bose is an associate professor of Information Systems at the School of Business, The University of Hong Kong. Prior to that, he was a faculty member at the University of Texas at Arlington and at the University of Florida. He holds a B.Tech. from the Indian Institute of Technology, MS from the University of Iowa, MS and Ph.D. from Purdue University. His research interests are in telecommunications informatior security, data mining, and supply chain management. His publications have appeared in Communications of the ACM, Communications of AIS, Computers and Operations Research, Decision Support Systems, Electronic Commerce Research & Applications Ergonomics, European Journal of Operational Research, Information & Management, Information Systems and e-Business Management, Journal of the American Society for Information Science and Technology, Journal of Organizational Computing and Electronic Commerce, Operations Research Letters, among others. His research is supported by several grants from academia and industry. He serves as Associate Editor/Editorial Review Board Member of Communications of AIS, Information & Management, Journal of Global Information Technology and Management, Information Resources management Journal, International Journal of Information Systems and Supply Chain Management, Journal of Database Management, etc. He has also served as guest editor fo Communications of AIS, Decision Support Systems, European Journal of Information Systems, and Journal of Organizational Computing and Electronic Commerce.
