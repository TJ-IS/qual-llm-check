---
otero_id: 9272
otero_key: "XBGKEE6Y"
title: "Feature construction for fraudulent credit card cash-out detection"
authors: "Yue Wu; Yunjie Xu; Jiaoyang Li"
year: "2019"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2019.113155"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Feature construction for fraudulent credit card cash-out detection

Yue Wu, Yunjie Xu<sup>⁎</sup>, Jiaoyang Li

School of Management, Fudan University, 670 Guoshun Road, Shanghai, China

## A R T I C L E I N F O

Keywords: Credit card fraud Cash-out detection Feature construction Functional data analysi

## A B S T R A C T

As a type of credit card fraud behavior, fraudulent cash-out causes banks and companies to incur huge losses. Furthermore, such organizations lack efective methods to detect fraudulent cash-out. To detect fraudulent cash out accurately, we construct four feature sets based on domain knowledge from industry experts, tips from fraudsters. related media reports, and the relevant literature. In addition. we construct features using a functional data analysis algorithm to capture the time-dependent behavioral patterns of cardholders. We also con struct a benchmark feature set based on the traditional approach of Whitrow's strategy. We compare these feature sets using a real data set comprising real transactions of 25,000 credit cards with three machine learning methods: eXtreme gradient boosting, random forest, and support vector machine. The results reveal that our proposed features, which consider both snapshot and dynamic behavioral patterns of cardholders, achieve considerably superior performance to that of Whitrow's strategy. The precisions at the top 5%, 10%, 15%, and 20% levels are improved by magnitudes of 0.049, 0.081, 0.053, and 0.046, respectively.

## 1. Introduction

Credit card fraud is a major challenge to banks worldwide. The amount of losses from credit card fraud is staggering. According to The Nilson Report, losses from credit card fraud reached \$21 billion worldwide in 2015 and are forecast to reach \$31 billion by 2020.<sup>1</sup> ACI Worldwide estimated that at least 46% of Americans were victims of credit card fraud in 2012–2016.<sup>2</sup> In China, credit card fraud is also on the rise. Compared with the number of cases in 2015, the number of reported credit card fraud cases in China increased by 3.8% in 2016.³ Therefore, it is imperative that banks and card-related companies undertake measures against credit card fraud.

Our study focuses on the identification of fraudulent cash-out, a major type of credit card fraud. Credit card fraud occurs when a fraudster uses a credit card to obtain unauthorized funds from an account [1,2]. There are many forms of credit card fraud, such as the use of counterfeit cards, identity theft fraud, and card-not-present fraud [3]. Fraudulent cash-out refers to the withdrawal of cash from a credit card through a fake purchase transaction that bypasses the interest charges and credit limits of cash advances set by the issuing bank. For instance, a cardholder might ask store employees to give cash back instead of taking the goods ostensibly purchased with a credit card. The collusive store employee might then give the cardholder cash in return for a percentage of the transaction amount, without following normal cashback practices. The cardholder can thus avoid cash advance limits and higher interest rates that are typically charged for cash advances. Alternatively, a cardholder may engage in fake transactions at virtual point-of-sales (POS) machines to increase the card's creditability. The cardholder may later borrow a larger amount than otherwise withdrawn and then default on this debt [4].

A common practice in credit card fraud detection is to construct a series of features from transaction data and build a model to predict the fraud risk. The quality of the features is crucial to model performance [5]. However, fraudulent behavior is typically strategic and dynamic in the real world, which poses a challenge for fraud detection [6]. Fraudsters often change their behavior frequently to avoid detection. Therefore, introducing features that can capture the dynamic behavior patterns of cardholders and constructing a fraud detection model using these features may help improve the accuracy of detection.

The purpose of this study is to construct efective feature sets for fraudulent cash-out detection based on both domain knowledge and statistical methods. The proposed feature sets cover both snapshot and dynamic behavior patterns of cardholders. They are tested through three popular prediction models: eXtreme gradient boosting (Xgboost), random forest, and support vector machine (SVM). Using a data set comprising real transactions from a major payment channel in China, we first create five feature sets and combinations of these feature sets to capture the snapshot characteristics of a cardholder. In Experiment $^ { 1 , }$ we compare the prediction precision of these feature sets. In Experiment 2, we enrich these feature sets with new features constructed through the functional data analysis (FDA) algorithm to capture the time-dependent behavior patterns of cardholders. We discover that feature sets that integrate both snapshot and dynamic characteristics of a cardholder's behavior achieve superior performance in fraudulent cash-out detection when deployed with a random forest algo rithm.

Our research provides three major contributions. First, prior research on credit card fraud detection has rarely focused on fraudulent cash-out. This study provides a tailored solution. Second, our research proposes a framework of feature construction for fraudulent cash-out. Unlike traditional fraud detection models that use only raw transactional features (e.g., amount, time, and place of consumption) and their statistical transformations (e.g., maximization, averaging, and standard deviation) [7–9], we construct features based on rich domain knowledge comprising relevant prior studies, the experience of industry experts, our study of related news, and tips shared by fraudsters online. Third, most prior studies on the construction of credit card fraud features have focused only on the snapshot behavior of cardholders. By contrast, we apply a statistical method, FDA, to create features to capture cardholders' dynamic behavior patterns.

The rest of this paper is organized as follows. Section 2 reviews the literature on feature engineering in the field of credit card fraud detection. Section 3 introduces the data set examined in this study. Section 4 elaborates on the feature engineering methods. Section 5 introduces two experiments to compare the performance of the feature sets. Finally, Section 6 discusses this paper's contributions and presents our conclusions.

## 2. Literature review

Studies related to credit card fraud detection have adopted two main approaches: classification algorithms and feature construction.

## 2.1. Classification algorithms

Classification algorithms such as the decision tree, association rules, naive Bayes, SVM, artificial neural network (ANN), and random forest models have been widely used in credit card fraud detection [10–15]. Şahin and Duman [1] built decision tree and SVM models to detect fraudulent transactions. They compared the results of these algorithms using a real data set, which revealed that the decision tree model could detect more fraudulent transactions with higher accuracy than SVM. Carneiro [16] applied automatic classification methods to detect fraud in online retail. The results revealed that logistic regression, SVM, and random forest all demonstrated efective performance in practice, but that random forest performed the best. Kültür and Çağlayan [17] combined six popular supervised machine learning models comprising decision tree, random forest. Bavesian network, naive Baves. SVM. and K\* models into an ensemble model for credit card fraud detection. By examining diferent voting strategies (i.e., optimistic, pessimistic, and weighted voting strategies), they discovered that the optimistic strategy led to a minimal false alarm rate and detected fewer cases of fraud, whereas the pessimistic strategy led to a relatively high false alarm rate and detected more cases of fraud. The weighted strategy represented a compromise between the former two strategies. Bayesian belief network, hidden Markov model (HMM), and genetic algorithm have also been revealed to be efective fraud detection solutions [18–21]. Deep learning, which has recently emerged, ofers new potential to achieve improved prediction performance. Jurgovsky et al. [22] applied long short-term memory (LSTM) as a sequence learner for fraud detection and obtained significantly higher accuracy than that of other methods.

Although various algorithms have been applied to credit card fraud detection with satisfactory performance, this stream of research has emphasized comparisons of algorithms instead of feature construction. Such research has mostly used raw variables from transaction data.

## 2.2. Feature construction

The second major stream of research on credit card fraud detection has focused on the construction of efective features from transaction data. Feature construction typically embodies domain knowledge and expertise. Carefully constructed features can greatly improve model performance.

A popular practice in this stream of research has been to transform raw transactions into new features using statistical functions such as maximization (i.e., maximum transaction amount in a single month), average, and standard deviation [18,23,24]. The most widely used of these methods is the aggregation strategy proposed by Whitrow [25]. This strategy aggregates the number and amount of transactions for each credit card by diferent dimensions (e.g., merchant type or country of the transaction) in various time windows. Relevant studies have revealed that a random forest model with features aggregated in 3-day or 7-day windows performs the most efectively [25]. The strength of the aggregation strategy is its ability to take a snapshot of cardholder behavior within the optimal time window. This snapshot can be updated over time. We also adopt the aggregation strategy to construct a feature set as a benchmark.

Another common practice is to construct features to capture the dynamics of cardholder behavior. Although the aggregation strategy provides a snapshot of cardholder behavior, it does not capture the dynamics of cardholder behavior. To overcome this limitation, Bahnsen [26] designed an expanded version of the aggregation strategy and applied the von Mises distribution to extract features of periodic behavior. Compared with raw fields, the addition of aggregated features and periodic features significantly improved model performance and achieved additional loss savings of 287%. Nevertheless, Bahnsen's method only captured the fixed periodic behavior of cardholders (e.g., consumption on a fixed date of every month) and missed many other time-related but less regular behaviors (e.g., a large transaction always being followed by a number of small transactions). Therefore, this study proposes the FDA algorithm to construct features to capture the dynamic behavior of cardholders.

The most relevant studies on feature construction for credit card fraud detection are listed in Table 1. Columns 2–5 present a brief de scription of the type of fraud, feature set, number of features, and classification algorithms examined in each paper, respectively. A few observations can be implied from the literature summarized in Table 1. First, although studies have been numerous, most have surprisingly not reported the exact type of fraud behavior, which increases the dificulty of comparing studies and negatively afects the accumulated research findings. Second, no study has focused on cash-out fraud. Third, most studies have adopted Whitrow's feature construction framework. By contrast, domain knowledge and time-dependent behavioral patterns have seldom been incorporated into feature construction. Fourth, all these feature construction studies have focused on predicting fraud at the transaction level, whereas none have focused on predicting fraud at the card level. Fraudulent cash-out may occur at the transaction level, but the anecdotal incidence of this level of fraudulent cash-out does not pose a major threat to banks. The harm fraudulent cash-out causes often manifests after the card has a high credit limit and the cardholder defaults. Therefore, card-level fraud prediction must be conducted by identifying cardholders who are cultivating increased credit limits in preparation to commit fraud. To fill these research gaps, we construct multiple sets of card-level features tailored to cash-out fraud and propose a new method to derive time-dependent behavior patterns from transaction data.

Main articles related to feature construction on credit card fraud detection. <sub>a</sub><sup>ble</sup> <sup>1</sup>

<table><tr><td>Reference</td><td>Fraud type</td><td>Main features</td><td>Total number of features</td><td>Classification algorithms</td></tr><tr><td>[6]</td><td>Not specified</td><td>Aggregated features: maximum amount, minimum amount, average amount, last transaction amount, transaction time intervals.</td><td>28/53/78/103 (changes with the sliding window size)</td><td>Logistic regression; Random forest; K-means</td></tr><tr><td>[16]</td><td>Chargeback fraud</td><td>Order time, order value, CV2Code_match, AVSCode_match, quantity, category, gender, brand, currency, payment, number cards used, payment attempts, valid user phone, bill country = ship country, bill country = card country, ship country = card country, bill region = ship region, time since first order, similarity (user name/card name), similarity (bill city/ship city), similarity (bill zip/ship zip), ship country risk level, ship city risk level, express shipping, number orders last 10 days same user.</td><td>71 (categorical dummy variables are ignored. Same below)</td><td>Random forest; Support vector machine; Logistic regression</td></tr><tr><td>[25]</td><td>Not specified</td><td>Counts of the number of transactions and the total value of transactions in each category (the type of terminal, transaction success status, PIN use indicator, checks made on the card, merchant type, transaction type).</td><td>Dataset 1: 87; Dataset 2: 91</td><td>Support vector machine; Random forest; Logistic regression; Quadratic discriminant; Naive Bayes</td></tr><tr><td>[26]</td><td>Not specified</td><td>1. Raw feature set: transaction ID, time, account number, card number, transaction type, entry mode, amount, merchant code, merchant group, country, country2, type of card, gender, age, bank.2. Aggregated features: calculate the number of transactions and amount of transactions grouped by country, type of transaction, entry mode, merchant code and merchant group.3. Periodic features: von Mises distribution.</td><td>293</td><td>Decision tree; Logistic regression; Random forest; Cost-sensitive logistic regression; Cost-sensitive decision tree</td></tr><tr><td>[27]</td><td>Not specified</td><td>1. Network features: maximum node degree, the entropy of the degree distribution, assortativity, clustering coefficient, geodesic distance, efficiency, information content.2. Transaction features: transaction size, time since the last transaction, last transaction size, average transaction size, the average time between transactions, same shop, the hour of the day, fraud rate.</td><td>15</td><td>Artificial neural networks</td></tr><tr><td>[28]</td><td>Card-not-present fraud in online credit card transactions</td><td>1. Intrinsic feature: the number of transactions, the amount of money, and the time between two subsequent transactions, if first purchase.2. Dummy variables for three zones, the categories of merchants, the average amount of the transactions during the last week, dummy variables representing the currency in which the transaction occurred.3. Network-based feature: credit cardholder exposure score, merchants exposure score, transaction exposure score on the long, medium and short term.</td><td>6099</td><td>Logistic regression; Neural network; Random forest</td></tr><tr><td>[29]</td><td>Not specified</td><td>Average amount spent per transaction over a month on all transactions up to this transaction, average amount spent over the course of 1 week during past 3 months, average amount spent per day over the past 30 days, amount merchant type over month, average amount per day spent over a 30 day period on all transactions up to this one on the same merchant type as this transaction, total number of transactions with same merchant during past 30 days, average amount spent over the course of 1 week during the past 3 months on same merchant type as this transaction, total amount spent on the same day up to this transaction, total number of transactions on the same day up to this transaction, average amount per day spent over a 30 day period on all transactions up to this one on the same merchant as this transaction, total number of transactions with the same merchant during last month, average amount per day spent over a 30 day period on all transactions up to this one on the same currency type as this transaction, total number of transactions in the same currency during the past 30 days, average amount spent over a 30 day period on all transactions up to this one on the same country as this transaction, total number of transactions in the same country during the past 30 days before this transaction, average amount spent over the course of 1 week during the past 3 months on same merchant as this transaction, total number of transactions with the same merchant during the past 3 months.</td><td>16</td><td>Support vector machine; Random forest; Logistic regression</td></tr></table>

## 3. Data

The data set used in our study is provided by a major credit card payment service firm in China with a role similar to that of Master Card or VISA. The firm marks credit cards as fraudulent or not based on their in-house algorithm and operational confirmations. According to the firm, the percentage of cards utilized in fraudulent cash-out transactions range from 10% to 30%, with a mean of 20%. Hence, we randomly sample fraudulent credit cards and legitimate cards from the firm's database at a ratio of 1:4, resulting in a sample of 5000 fraudulent credit cards and 20,000 legitimate cards from a single city. We treat fraudulent card as positive instances and legitimate card as negative instances. Our data set spans 10 months, from March 1, 2016 to December 31, 2016, and comprises 1,067,010 transactions of 25,000 credit cards.

The raw fields of each transaction comprise card ID, merchant ID, merchant category code, transaction amount, transaction time, and other typical transaction fields. The data are analyzed at the firm's premises under very strict data security policies. For each transaction, the card ID and the merchant ID are anonymized, and the researcher are only allowed to generate an aggregate analysis report.

## 4. Feature engineering method

Our unit of analysis is credit cards rather than transactions. We construct the features of each card in three steps. First, we design potential features based on knowledge from four sources: the relevant literature, industry experts, tips shared by fraudsters online, and characteristics of fraudulent cash-out as reported in the media. We compile a list of common features from the relevant literature. We then conduct interviews with experts in the firm's risk control department and construct additional features that they believe to be useful. However, not all the features from these two sources are specific to cash-out fraud. Hence, we collect tips shared by fraudsters in various online communities and websites. We also collect financial media reports on cash-out fraud and construct features based on the reported practices of fraud sters. Features are designed by brainstorming based on the online tips and news reports. The features from these four sources form our basic feature set (refer to Table 2 for a full list of and rationales for the constructed features).

Second, we derive four new feature sets based on the basic feature set. For feature set 1, the means over the 10-month period are calculated for each basic feature in part 1, part 2, and part 3a of Table 2. For example, the mean of monthly total “amounts” is calculated. For feature set 2, the standard deviations over the 10-month period are calculated for each basic feature in part 1, part 2, and part 3a of Table 2. To ac count for the time factor, feature set 3 measures the difference between the first month and the last month for each feature. A card's level can change during the 10-month period. For feature set 4, we aggregate each basic feature in part 1, part 2, and part 3a (see Table 2) by card level. Feature set 4 measures each feature's diference at the lowest card level and at the highest card level. Part 3b of Table 2 lists the basic features aggregated over 10 months. They are added to each of feature sets 1–4. The composition of each feature set is presented in Table 3. The pseu docode to construct each feature set is presented in the Appendix.

Finally, according to the transaction aggregation strategy proposed by Whitrow [25], we calculate the total number and the total amount of transactions in each city, merchant type, and merchant category code for each card to construct feature set 5, which we regard as a benchmark.

## 5. Experiments

## 5.1. Algorithms

Although the purpose of this study is to test and compare our constructed feature sets, we also compare the performance of the feature sets with diferent algorithms. Such comparisons indicate whether a feature set is generally efective or efective only with certain algorithms.

This study applies three up-to-date classification algorithms for fraud detection: Xgboost, random forest, and SVM. Xgboost is a highly scalable and efective end-to-end tree boosting technique [30]. It has been applied to predict loan default probability, and its maximum K–S value has reached 0.7203, suggesting very efective performance [31]. Random forest is another ensemble algorithm that uses decision trees as base classifiers. It has been applied to various fraud detection tasks, in which it has delivered high prediction accuracy [32–34]. SVM is a supervised machine learning method with a statistical learning technique [35]. Wang et al. applied SVM to credit card fraud prediction and achieved 97.7% precision and 100% recall [10]. SVM also has advantages for solving nonlinear and high-dimensional problems. When utilizing one algorithm to build models with diferent feature sets, we use the same super-parameters to set up the algorithm.

## 5.2. Experiment 1

We randomly divide our data set into two parts, with 80% for training and 20% for testing. After training the models, we calculate the fraud probability of each card in the testing subset and sort them in descending order. We calculate the precision of the top 5%, 10%, 15%, and 20% of the testing subset. We consider precision to be a superior performance indicator of accuracy in an imbalanced data set.<sup>4</sup> We repeat this procedure 10 times, and we then compute the mean and standard deviation of the precision of the 10 trials.

First, we compare the performance of the individual feature set. Fig. 1a illustrates the average precision of the three algorithms using each of feature sets 1–5. Compared with the benchmark feature set 5, feature set 1 has the most efective performance, whereas feature set 3 has the least efective performance.

Second, we test the performance of feature sets 1–4 as an enrichmen of feature set 5. We integrate feature set 5 with each of feature sets 1–4. The results illustrated in Fig. 1b indicate that each combination outperforms feature set 5, suggesting that feature sets 1–4 are useful. Among them, the combination of feature set 4 + 5 performs the most efectively at the top 5%. Feature set 1 + 5 performs most efectively at the top 10%–20% levels.

Fig. 1 presents the overall performance of each feature set across all algorithms, but the performance of each individual feature set difers for each algorithm. Fig. 2 illustrates the precision of each feature set for

Table 2  
Details of basic features.

<table><tr><td colspan="5">Features from related literature (Part 1)</td></tr><tr><td>Feature</td><td>Aggregation level</td><td></td><td>Description</td><td>Literature</td></tr><tr><td>Amount</td><td colspan="2">Each month (for feature sets 1-3, same below); each card level (for the feature set 4, same below)</td><td>The total amount spent</td><td>[18,22,23]</td></tr><tr><td>Std</td><td colspan="2">Each month; each card level</td><td>The standard deviation of transaction amount</td><td>[24]</td></tr><tr><td>Num</td><td colspan="2">Each month; each card level</td><td>The total number of transactions</td><td>[23]</td></tr><tr><td>Max</td><td colspan="2">Each month; each card level</td><td>The maximum of transaction amount</td><td>[6]</td></tr><tr><td>Min</td><td colspan="2">Each month; each card level</td><td>The minimum of transaction amount</td><td>[6]</td></tr><tr><td>Avg</td><td colspan="2">Each month; each card level</td><td>The average of transaction amount</td><td>[6,23]</td></tr><tr><td colspan="5">Features from experts in the industry (Part 2)</td></tr><tr><td>Feature</td><td>Aggregation level</td><td>Description</td><td colspan="2">Assumption</td></tr><tr><td>Maxper</td><td>Each month; each card level</td><td>=Max / Amount</td><td colspan="2">Fraudulent cards are more likely to make an exceptionally large transaction.</td></tr><tr><td>Num_high</td><td>Each month; each card level</td><td>The number of transactions with an amount greater than 100,000</td><td colspan="2">Fraudulent cards are more likely to make transactions of large amount.</td></tr><tr><td>Night_money</td><td>Each month; each card level</td><td>The total amount of transactions in the time period of 00:00 a.m. to 06:00 a.m.</td><td colspan="2">People who make transactions in the time period of 00:00 a.m. to 06:00 a.m.</td></tr><tr><td>Night_money_per</td><td>Each month; each card level</td><td>=Night_money / Amount</td><td colspan="2">have a statistically higher fraud risk.</td></tr><tr><td>Night_n</td><td>Each month; each card level</td><td>The total number of transactions in the time period of 00:00 a.m. to 06:00 a.m.</td><td colspan="2"></td></tr><tr><td>Night_n_per</td><td>Each month; each card level</td><td>=Night_n / Number</td><td colspan="2"></td></tr><tr><td>Weekday_money</td><td>Each month; each card level</td><td>The total amount of transactions on weekdays</td><td rowspan="4" colspan="2">Fraudulent cards are more likely to make transactions on weekdays than normal cards do.</td></tr><tr><td>Weekday_money_per</td><td>Each month; each card level</td><td>=Weekday_money / Amount</td></tr><tr><td>Weekday_n</td><td>Each month; each card level</td><td>The total number of transactions on weekdays</td></tr><tr><td>Weekday_n_per</td><td>Each month; each card level</td><td>=Weekday_n / Number</td></tr><tr><td>Num_high_per</td><td>Each month; each card level</td><td>=Num_high / Number</td><td colspan="2">Fraudulent cards are more likely to make transactions of large amount.</td></tr><tr><td colspan="5">Features from &quot;tips&quot; and news (Part 3a)</td></tr><tr><td>Feature</td><td>Aggregation level</td><td>Description</td><td colspan="2">Assumption</td></tr><tr><td>Num_100</td><td>Each month; each card level</td><td>The total number of transactions with an amount which is an integral multiple of 100</td><td rowspan="2" colspan="2">The amount of a fraudulent transaction is more likely to be an integral multiple of 100.</td></tr><tr><td>Num_100_per</td><td>Each month; each card level</td><td>=Num_100 / Number</td></tr><tr><td>Num_1000</td><td>Each month; each card level</td><td>The total number of transactions with an amount which is an integral multiple of 1000</td><td rowspan="2" colspan="2">The amount of a fraudulent transaction is more likely to be an integral multiple of 1000.</td></tr><tr><td>Num_1000_per</td><td>Each month; each card level</td><td>=Num_1000 / Number</td></tr><tr><td>Highrisk_transtype</td><td>Each month; each card level</td><td>The total amount of transactions of high-risk type</td><td rowspan="4" colspan="2">Transaction type includes purchase, cash withdrawal, money transfer, advance deposit and so on. Fraudulent cards are more likely to make certain transaction types (e.g., cash withdrawal and advance deposit). Therefore, cards with more transactions of a high-risk transaction type are more likely to be fraudulent.</td></tr><tr><td>Highrisk_transtype_n</td><td>Each month; each card level</td><td>The total number of transactions of high-risk type</td></tr><tr><td>Highrisk_transtype_per</td><td>Each month; each card level</td><td>=Highrisk_transtype / Amount</td></tr><tr><td>Highrisk_transtype_n_per</td><td>Each month; each card level</td><td>=Highrisk_transtype_n / Number</td></tr><tr><td>Highrisk_MCC</td><td>Each month; each card level</td><td>The total amount of transactions with high-risk MCC (merchant category code)</td><td rowspan="4" colspan="2">Fraudulent cash-out is more likely to occur in certain MCCs. Based on the distribution of fraud in each MCC, we set the top 10 MCCs as risky MCCs. A card with more transactions in these MCCs is more likely to be fraudulent.</td></tr><tr><td>Highrisk_MCC_n</td><td>Each month; each card level</td><td>The total number of transactions with high-risk MCC</td></tr><tr><td>Highrisk_MCC_per</td><td>Each month; each card level</td><td>=Highrisk_MCC / Amount</td></tr><tr><td>Highrisk_MCC_n_per</td><td>Each month; each card level</td><td>=Highrisk_transid_n / Number</td></tr><tr><td>Highrisk_MCCfst</td><td>Each month; each card level</td><td>The total amount of transactions with high-risk higher-level-MCC</td><td colspan="2">MCCs can be grouped into higher levels.</td></tr><tr><td>Highrisk_MCCfst_n</td><td>Each month; each card level</td><td>The total number of transactions with high-risk higher-level-MCC</td><td rowspan="3" colspan="2">Fraudulent cash-out is more likely to occur in certain higher level MCCs. Based on the distribution of fraud in each higher level MCC, we set the top 10 higher level MCCs as risky MCCs. A card with more transactions in these higher level MCCs is more likely to be fraudulent.</td></tr><tr><td>Highrisk_MCCfst_per</td><td>Each month; each card level</td><td>=Highrisk_MCCfst / Amount</td></tr><tr><td>Highrisk_MCCfst_n_per</td><td>Each month; each card level</td><td>=Highrisk_MCCfst_n / Number</td></tr><tr><td>Pos_per</td><td>Each month; each card level</td><td>=Number / The number of unique POS machine</td><td colspan="2">Fraudulent cards are more likely to have transactions with a fixed set of POS machines.</td></tr><tr><td>MCC_per</td><td>Each month; each card level</td><td>=Number / The number of unique MCCs</td><td colspan="2">Fraudulent cards are more likely to have transactions with a fixed set of MCCs.</td></tr><tr><td>Money_per</td><td>Each month; each card level</td><td>=The number of transactions with unique amount / Number</td><td colspan="2">Fraudulent cards are more likely to have transactions of the same amount.</td></tr></table>

(continued on next page)

Table 2 (continued)

<table><tr><td colspan="4">Features from “tips” and news (Part 3a)</td></tr><tr><td>Feature</td><td>Aggregation level</td><td>Description</td><td>Assumption</td></tr><tr><td>Vc</td><td>Each month; each card level</td><td>The variation coefficient of transaction amount</td><td>Statistical measures</td></tr><tr><td>Kurtosis</td><td>Each month; each card level</td><td>The Kurtosis of the amount of all transactions</td><td></td></tr><tr><td>Skewness</td><td>Each month; each card level</td><td>The skewness of the amount of all transactions</td><td></td></tr><tr><td>Gini</td><td>Each month; each card level</td><td> $=1 - \frac{1}{\text{Number}} * (2 * \sum_{i=1}^{\text{Number}-1} W_i + 1)$ </td><td>The feature measures the degree of inequality (Gini index) in the distribution of transaction amount.</td></tr><tr><td>Mclumpiness</td><td>Each month; each card level</td><td> $=1 + \frac{\sum_{i=1}^{\text{Number}+1} \log(x_i) * x_i}{\log(\text{Number} + 1)}$  $x_i: \text{days lapse between two transactions}$ </td><td>The feature measures the degree of transactions clustering together in the time dimension.</td></tr><tr><td colspan="4">Features from “tips” and news (Part 3b)</td></tr><tr><td>Feature</td><td>Aggregation level</td><td>Description</td><td>Assumption</td></tr><tr><td>Difflevel</td><td>Ten months (forfeature sets 1–4, same below)</td><td>The difference between the lowest and the highest card level</td><td>Some fraudulent cards intentionally cultivate its card level for fast upgrading.This feature captures it.</td></tr><tr><td>Levelchange</td><td>Ten months</td><td>Times of card level changes</td><td>Fraudulent cards are more likely to change its card level, including upgrading and downgrading.Downgrading occurs when a bank detects some fraudulent transactions.</td></tr><tr><td>Monthdiv_std</td><td>Ten months</td><td>The standard deviation of days lapse between the day with the highest amount in the last month and in this month</td><td>Fraudulent cards that use cash-out to pay debt periodically are more likely to have a stable time interval for the largest transaction.</td></tr><tr><td>Monthdiv</td><td>Ten months</td><td>The mean of days lapse between the day with the highest amount in the last month and in this month</td><td>Fraudulent cards that use cash-out to pay debt periodically are more likely to have a large time interval for the largest transaction.</td></tr><tr><td>Difft_month</td><td>Ten months</td><td>The mean of days lapse between the last transaction of the previous month and the first transaction of this month</td><td>Fraudulent cards are more likely to make transactions soon after the repayment date. Therefore, the time interval between the last transaction of the previous month and the first transaction of this month is more likely to be large.</td></tr><tr><td>Difft_month_std</td><td>Ten months</td><td>The standard deviation of days lapse between the last transaction of the previous month and the first transaction of this month</td><td>Fraudulent cards are more likely to make transactions soon after the repayment date. Therefore, the time interval between the last transaction of the previous month and the first transaction of this month is more likely to be stable.</td></tr></table>

the Xgboost, random forest, and SVM algorithms at the top 5% and 20% levels. In general, the relative performance of the algorithms is stable over all feature sets.

Third, we compare the performance of additional combinations of feature sets. Because the combination of feature set 1 + 5 performs most efectively in the previous test, we add the other three feature sets to feature set $\mathbf { \Omega } ^ { 1 } + \mathbf { \Omega } 5 .$ . Model performance based on these new feature set combinations is evaluated in the same way as discussed previously. We also conduct a pairwise t-test between the precision of each feature set combination and that of the benchmark feature set (i.e., feature set 5). The results are presented in Table 4.

The results reveal that feature set $1 + 4 + 5$ exhibits the most ef fective performance when used with random forest. The precision of feature set $1 + 4 + 5$ at the top 5% level reaches 0.950, which is higher than the precision of feature set 5 by a magnitude of 0.054. At the top 20% level, the precision of feature set $1 + 4 + 5$ again surpasses that of feature set 5 by a magnitude of 0.019. Feature set $1 + 2 + 4 + 5$ performs the second most efectively. Its precision is 0.946 at the top 5% and 0.771 at the top 20%, surpassing the precision results of feature set 5 by 0.050 and 0.017, respectively.

Both Fig. 2 and Table 4 illustrate that random forest outperforms Xgboost and SVM in all feature sets. Therefore, we select the random forest algorithm as the classifier to build the models in the subsequent analysis.

## 5.3. Experiment 2

The feature sets proposed in Experiment 1 consider only the snapshot features of cardholders. In Experiment 2, we introduce new features based on the FDA algorithm. The key idea of FDA is to use a curve to approximate the dynamics of each card's transaction amount and to extract the principal components of the curve as new features.

For each cardholder, $i ( i = 1 , 2 , . . . . . . , n ) , \ : \mathrm { y } _ { i j }$ denotes the daily transaction amount at time $t _ { i j } ( i = 1 , 2 , . . . . . . . , n , j = 1 , 2 , . . . . . . , m )$ , where m is the number of days in the study period.

Hence, the daily transaction amount $\begin{array} { r } { \mathbf { y } _ { i j } ( i = 1 , 2 , . . . . . . , n , j = 1 , 2 , } \end{array}$ $\ldots , m )$ of each cardholder i can be regarded as a time series that re presents the dynamics of the daily transaction amount. A cardholder's consumption behavior may exhibit time-dependent patterns. To capture these patterns, we propose a feature engineering strategy based on FDA. FDA, which is widely used in economics, biomedicine, meteorology, and psychology [36], models a time series in functional space and considers the data as a continuous curve instead of a group of discrete observations [37]. We detail the rationale of this method as follows:

Table 3  
Composition of each feature set.

<table><tr><td>Feature set</td><td>Features included</td></tr><tr><td>Feature set 1</td><td>(1) The means over the 10-month period for each basic feature in part 1, part 2 and part 3a of Table 2.(2) All features in part 3b of Table 2.</td></tr><tr><td>Feature set 2</td><td>(1) The standard deviations over the 10-month period for each basic feature in part 1, part 2 and part 3a of Table 2.(2) All features in part 3b of Table 2.</td></tr><tr><td>Feature set 3</td><td>(1) The difference between the first month and the last month for each basic feature in part 1, part 2 and part 3a of Table 2.(2) All features in part 3b of Table 2.</td></tr><tr><td>Feature set 4</td><td>(1) The difference between the lowest card level and the highest card level for each basic feature in part 1, part 2 and part 3a of Table 2.(2) All features in part 3b of Table 2.</td></tr><tr><td>Feature set 5</td><td>(1) The total number and the total amount of transactions in each city, merchant type and merchant category code for each card.</td></tr></table>

![](/api/attachments/XBGKEE6Y/fulltext/images/01097a0c229428b58237c7dd4d1e1e62eb06b364baf4c6d0dd015bb78144321b.jpg)  
(a)

![](/api/attachments/XBGKEE6Y/fulltext/images/c36c039143fe3e08965ff313b46aee22c04980d0e7a4e2576f1a42586042de0e.jpg)  
(b)

Fig. 1. Average precision of feature sets across the three algorithms.  
![](/api/attachments/XBGKEE6Y/fulltext/images/008f924d0a7960e853f4962b3bb709eed304223cf7cdd55190f61cab2e825a07.jpg)  
(a)

![](/api/attachments/XBGKEE6Y/fulltext/images/074eecdce5d867277a7d237d04dd1806b944a0403e0fd40c58c3e0248fd2bdb2.jpg)  
(b)  
Fig. 2. Precision of Xgboost, random forest, and SVM with diferent feature sets.

In the first step, for each cardholder i, daily transactions form a set $\mathbf { y } _ { i } = ( y _ { i 1 } , . . . , y _ { i m _ { i } } ) _ { i }$ , which is modeled as a continuous function with smoothing. Specifically, the transaction amount for each credit card $\mathbf { y } _ { i j }$ can be expressed by a continuous function x (t) at a set of time points $t _ { i j }$ $( j = 1 , 2 , . . . . . . , m )$ such that

$$
y _ {i j} = x _ {i} (t _ {i j}) + \varepsilon_ {i j},\tag{1}
$$

where $x _ { i } ( t _ { i j } )$ represents the value of function $x _ { i } ( t )$ at time $t _ { i j } ,$ and $\varepsilon _ { i j }$ is the error term that represents the disturbance factor in the observation. The objective is to find the most appropriate x (t). In the functional space $F ,$ where $F = s p a n \{ \varphi _ { 1 } , \varphi _ { 2 } . . . , \varphi _ { n _ { b } } \}$ and $\{ \varphi _ { k } \} ( k = 1 , 2 , \cdots , n )$ is a set of basic functions, x (t) can be represented as the linear combination of these basic functions.

Table 4  
The precision of Xgboost, random forest and SVM with various feature sets at the top x% of cards.

<table><tr><td rowspan="2">Classification algorithm</td><td rowspan="2">Feature set</td><td colspan="2">Top 5%</td><td colspan="2">Top 10%</td><td colspan="2">Top 15%</td><td colspan="2">Top 20%</td></tr><tr><td>Precision</td><td>Recall</td><td>Precision</td><td>Recall</td><td>Precision</td><td>Recall</td><td>Precision</td><td>Recall</td></tr><tr><td rowspan="5">Xgboost</td><td>feature set 5</td><td>0.849</td><td>0.212</td><td>0.831</td><td>0.416</td><td>0.795</td><td>0.596</td><td>0.733</td><td>0.733</td></tr><tr><td>feature set 1 + 5</td><td>0.920***</td><td>0.230</td><td>0.878***</td><td>0.439</td><td>0.827***</td><td>0.620</td><td>0.762***</td><td>0.762</td></tr><tr><td>feature set 1 + 4 + 5</td><td>0.916***</td><td>0.229</td><td>0.878***</td><td>0.439</td><td>0.834***</td><td>0.626</td><td>0.761***</td><td>0.761</td></tr><tr><td>feature set 1 + 2 + 4 + 5</td><td>0.920***</td><td>0.230</td><td>0.877***</td><td>0.439</td><td>0.826***</td><td>0.620</td><td>0.761***</td><td>0.761</td></tr><tr><td>feature set 1 + 2 + 3 + 4 + 5</td><td>0.919***</td><td>0.230</td><td>0.879***</td><td>0.440</td><td>0.832***</td><td>0.624</td><td>0.761***</td><td>0.761</td></tr><tr><td rowspan="5">Random forest</td><td>feature set 5</td><td>0.896</td><td>0.224</td><td>0.864</td><td>0.432</td><td>0.816</td><td>0.612</td><td>0.754</td><td>0.754</td></tr><tr><td>feature set 1 + 5</td><td>0.926***</td><td>0.232</td><td>0.895***</td><td>0.448</td><td>0.838***</td><td>0.629</td><td>0.770***</td><td>0.770</td></tr><tr><td>feature set 1 + 4 + 5</td><td>0.950***</td><td>0.238</td><td>0.905***</td><td>0.453</td><td>0.844***</td><td>0.633</td><td>0.773***</td><td>0.773</td></tr><tr><td>feature set 1 + 2 + 4 + 5</td><td>0.946***</td><td>0.237</td><td>0.902***</td><td>0.451</td><td>0.842***</td><td>0.632</td><td>0.771***</td><td>0.771</td></tr><tr><td>feature set 1 + 2 + 3 + 4 + 5</td><td>0.942***</td><td>0.234</td><td>0.902***</td><td>0.451</td><td>0.844***</td><td>0.633</td><td>0.770***</td><td>0.77</td></tr><tr><td rowspan="5">SVM</td><td>feature set 5</td><td>0.880</td><td>0.220</td><td>0.831</td><td>0.416</td><td>0.759</td><td>0.569</td><td>0.689</td><td>0.689</td></tr><tr><td>feature set 1 + 5</td><td>0.925***</td><td>0.231</td><td>0.879***</td><td>0.440</td><td>0.823***</td><td>0.617</td><td>0.748***</td><td>0.748</td></tr><tr><td>feature set 1 + 4 + 5</td><td>0.940***</td><td>0.235</td><td>0.891***</td><td>0.446</td><td>0.831***</td><td>0.623</td><td>0.753***</td><td>0.753</td></tr><tr><td>feature set 1 + 2 + 4 + 5</td><td>0.943***</td><td>0.236</td><td>0.891***</td><td>0.446</td><td>0.828***</td><td>0.621</td><td>0.753***</td><td>0.753</td></tr><tr><td>feature set 1 + 2 + 3 + 4 + 5</td><td>0.940***</td><td>0.235</td><td>0.886***</td><td>0.443</td><td>0.825***</td><td>0.619</td><td>0.753***</td><td>0.753</td></tr></table>

Note: The bold fonts indicate that the feature set performs the best within a classification algorithm and the underlines indicate that the feature set performs the best among all three classification algorithms.  
<sup>⁎⁎⁎</sup> The precision and the corresponding recall is significantly better than the precision of feature set 5 at $\mathsf { p } = 0 . 0 0 1$

![](/api/attachments/XBGKEE6Y/fulltext/images/743f56a85a53657a35f5ea967d17723c9f585c4b343845db569dba2ac4794d99.jpg)  
Fig. 3. Precision of feature sets with and without FDA at top t% using random forest algorithm.

$$
x _ {i} (t) = \sum_ {k = 1} ^ {n _ {b}} c _ {i k} \varphi_ {k} (t),\tag{2}
$$

where $\{ c _ { i k } \} _ { k = 1 } { } ^ { n _ { b } }$ represents the coeficients of the chosen set of basic functions, and n represents the number of basic functions. The most commonly used basic functions are Fourier functions for periodic data and B-splines for nonperiodic data [38]. To estimate the optimal value of $c _ { k } ,$ we minimize the following squared loss function,

$$
\min _ {x \in F} \sum_ {j} (y _ {i j} - x _ {i} (t _ {i j})) ^ {2} + \rho \int [ D ^ {2} x _ {i} (t) ] ^ {2} d t,\tag{3}
$$

where $y _ { i j }$ is the transaction amount of the $i _ { t h }$ cardholder observed at time $t _ { i j } , D ^ { 2 } x _ { i } ( t )$ is the curvature of a function x (t), and ρ is a smoothing parameter that penalizes the roughness of the curve. Because card holder transaction behavior may not be periodic, we apply B-splines as a smoothing method to transform the transaction amounts of each card into a curve.

In the second step, functional principal component analysis (FPCA) is introduced to construct the features. FPCA is an extension of principal component analysis. We use FPCA to extract the principal components of each curve and consider the scores of principal components as the features of each card. These features are denoted as feature set FDA.

We add feature set FDA to the most efective performers in Experiment 1 (i.e., feature set $1 + 4 + 5$ and feature set $1 + 2 + 4 + 5 ) .$ We compare them with feature set FDA, feature set $1 + 4 + 5 + F D A$ and feature set $1 + 2 + 4 + 5 + F D A$ . Following the same process in Experiment 1 and applying the random forest model, we sort the fraud probability of each credit card in the testing set in descending order. Then, we repeat the procedure 10 times and compute the means and standard deviations of precision across all 10 trials. The results are presented in Fig. 3. Although model performance based on feature set FDA is not efective, adding feature set FDA to feature set $1 + 2 + 4 + 5$ significantly improves the precision. Compared with the results of only using feature set $1 + 2 + 4 + 5$ including feature set $1 + 2 + 4 + 5 + F D A$ improves the precision by approximately 0.021, 0.059, 0.038, and 0.037 at the top 5%, 10%, 15%, and 20% levels, respectively. Compared with feature set 5 using the random forest al gorithm in Experiment 1, the improvements of precision are 0.049, 0.081, 0.053, and 0.046 at the top 5%, 10%, 15%, and 20% levels, respectively. From a practical perspective, these improvements are significant.

Table 5  
The accuracy, precision, recall and F1 score of various feature sets with random forest algorithm on a balanced dataset.

<table><tr><td></td><td>Accuracy</td><td>Precision</td><td>Recall</td><td>F1</td></tr><tr><td>feature set 1</td><td>0.912</td><td>0.883</td><td>0.946</td><td>0.913</td></tr><tr><td>feature set 2</td><td>0.900</td><td>0.861</td><td>0.944</td><td>0.901</td></tr><tr><td>feature set 3</td><td>0.809</td><td>0.790</td><td>0.819</td><td>0.804</td></tr><tr><td>feature set 4</td><td>0.892</td><td>0.862</td><td>0.921</td><td>0.891</td></tr><tr><td>feature set 5</td><td>0.905</td><td>0.883</td><td>0.925</td><td>0.904</td></tr><tr><td>feature set 1 + 5</td><td>0.922</td><td>0.896</td><td>0.951</td><td>0.923</td></tr><tr><td>feature set 2 + 5</td><td>0.913</td><td>0.882</td><td>0.949</td><td>0.914</td></tr><tr><td>feature set 3 + 5</td><td>0.910</td><td>0.881</td><td>0.942</td><td>0.910</td></tr><tr><td>feature set 4 + 5</td><td>0.912</td><td>0.884</td><td>0.944</td><td>0.913</td></tr><tr><td>feature set 1 + 4 + 5</td><td>0.920</td><td>0.889</td><td>0.954</td><td>0.920</td></tr><tr><td>feature set 1 + 2 + 4 + 5</td><td>0.923</td><td>0.895</td><td>0.954</td><td>0.924</td></tr><tr><td>feature set 1 + 2 + 3 + 4 + 5</td><td>0.920</td><td>0.890</td><td>0.954</td><td>0.921</td></tr><tr><td>feature set FDA</td><td>0.883</td><td>0.834</td><td>0.959</td><td>0.892</td></tr><tr><td>feature set 1 + 4 + 5 + FDA</td><td>0.945</td><td>0.919</td><td>0.975</td><td>0.946</td></tr><tr><td>feature set 1 + 2 + 4 + 5 + FDA</td><td>0.938</td><td>0.912</td><td>0.970</td><td>0.940</td></tr></table>

Note: The bold fonts indicate that the feature set performs the most efectively and the second most efectively.

## 5.4. Performance in balanced data set

To facilitate a comparison of our study with prior studies, we construct a balanced data set by randomly selecting 3000 fraudulent cards as positive instances and 3000 legitimate cards as negative instances from our data set. We evaluate model performance using four in dicators: accuracy, precision, recall, and F1 score. The results are presented in Table 5. The combination of feature set $1 + 4 + 5 + F D A$ exhibits the most efective performance. Additionally, feature set $1 + 2 + 4 + 5 + F D A$ performs second most efectively (accuracy = 0.938, precision = 0.912, recall = 0.97, F1 = 0.94), and its performance indicators are very close to that of feature set $1 + 4 + 5 + F D A$ . Although prior studies have not reported the type of fraud, and setting of such studies might be diferent, some studies have reported the performance in a balanced data set. Hence, we can make a rough comparison of performance in balanced data sets. For example, one study [41] reported precision levels at 0.20–0.39. Another study [23] reported precision levels of 0.689–0.817 and recall levels of 0.820–0.889; and yet another study [29] reported precision levels of

0.072–0.613 and F scores of 0.131–0.500. In comparison, our study's performance is substantially superior.

## 6. Discussion and conclusions

The main motivation of this study is to construct novel features for fraudulent cash-out detection. To illustrate the contributions of this study, we compare this study with previous feature construction studies on credit card fraud detection based on the following perspectives: fraud type, variety of features, total number of features, and performance. First, although many feature construction studies on credit card fraud detection have been published, most have not reported the specific type of fraud studied. Some such studies have studied chargeback fraud [16], and others have studied card-not-present fraud in online credit card transactions [28], but none have focused on fraudulent cashout. This study presents an initial efort focused on fraudulent cash-out. Second, most relevant studies have employed snapshot features such as raw data fields, aggregated features, periodic features, and network features. By contrast, this study integrates additional features from industry experts, online tips shared by fraudsters online, news reports, and statistical features from FDA to capture the dynamic patterns of credit card transactions. Third, the largest number of features examined by previous studies has been 293 [26]. We have incorporated a larger number of features in this study. Each of feature sets 1–4 has 48 features. Feature set 5 has 41 features and feature set FDA has 306 features. Thus, our approach comprises a total of 521 features, which ofers a rich pool for future feature selection studies. Fourth. compared with feature set 5. which is based on the most popular feature construction technique, feature set $1 + 2 + 4 + 5 + F D A$ can improve precision by 4.6%–8.1% at the top 5%–20% levels. This improvement is economically very substantial. Finally, although we are unable to engage in a fair comparison of our study's detection precision with that of prior studies, a rough comparison indicates that our study performs far more efectively.

The results of this study should be interpreted considering its limitations. First, the data set is from only one country. Fraud behavior can vary by country, and the prediction value of features therefore can vary by country. Second, a fraud detection model in a production system typically employs far fewer features than that in this study. Future research should explore feature reduction techniques based on our pool of features to improve eficiency.

## Declaration of competing interest

None.

## Acknowledgments

This study was supported by the National Natural Science Foundation of China under Grant #71531006 and the Program for Professor of Special Appointment (Eastern Scholar) at Shanghai Institutions of Higher Learning.

## Appendix A. Feature construction process

Input:

Transaction records set $\mathsf { R } = \{ r _ { 1 } , r _ { 2 } \ldots \ldots r _ { n } \} ;$

## Output:

Feature set $\mathrm { F } = \{ f _ { 1 } , f _ { 2 } , f _ { 3 } , f _ { 4 } \} ;$

Begin:

1. Identify the month of transaction for each transaction record based on the time stamp;

2. For to

4. For $m = 3$ to 12

6. Calculate the basic features for each cardholder from part 1, part 2, and part 3a of Table 2 based on each month and obtain the set $x _ { i m } = \big \{ x _ { i m A m o u n t } , x _ { i m S t d } , \ldots \ldots , x _ { i m M c l u m p i n e s s } \big \} ;$

8. Calculate the basic features from part 3b of Table 2 and obtain the set $k _ { i } =$ $k _ { i D i f f \_ m o n t h \_ s t d } \} ;$

9. Calculate the mean of each element in the set $x _ { i m }$ and obtain the set ${ } _ { - } x _ { i } =$ {mean $x _ { i A m o u n t }$ , mean\_Xistd, . .., mean\_XimMclumpines.};

10. Calculate the standard deviation of each element in the set $x _ { i m }$ and obtain the set $s t d _ { - } x _ { i } =$ {std\_xiAmount, std\_xistd, ... , std\_ximMclumpiness}

11. Calculate the difference between the first month and the last month of each element in the set $x _ { i m }$ and obtain the set

13. Form feature set 1 $f _ { 1 } = \{ f _ { 1 1 } , f _ { 1 2 } , \dots \dots , f _ { 1 n } \}$ with each element $f _ { 1 i } = \{ m e a n \_ x _ { i } , k _ { i } \} ;$

14. Form feature set 2 $f _ { 2 } = \{ f _ { 2 1 } , f _ { 2 2 } , \dots \dots , f _ { 2 n } \}$ with each elemen $f _ { 2 i } = \{ s t d \_ x _ { i } , k _ { i } \} ;$

15. Form feature set 3 $f _ { 3 } = \{ f _ { 3 1 } , f _ { 3 2 } , \dots \dots , f _ { 3 n } \}$ with each element $f _ { 3 i } = \{ d i f f m o n t h \_ x _ { i } , k _ { i } \} ;$

20. Calculate the basic features for each cardholder from part 1, part 2 and part 3a of Table 2 based on card level and obtain the set $z _ { i l } = \big \{ z _ { i l A m o u n t } , z _ { i l S t d } , \dots \dots , z _ { i l M c l u m p i n e s s } \big \} ;$

22. Calculate the basic features from part 3b of Table 2 and obtain the set $k _ { i } =$ {kiDif f,levele, iLevelchange, ..... kiDiff \_month\_std};d

23. Calculate the difference of each element in the set $z _ { i l }$ at the lowest card level and at the highest card level and obtain the set

25. Form feature set 4 $f _ { 4 } = \{ f _ { 4 1 } , f _ { 4 2 } , \dots \dots , f _ { 4 n } \}$ with each element $f _ { 4 i } = \{ d i f f c a r d \_ z _ { i } , k _ { i } \} ;$ 26. $\mathrm { F } = \{ f _ { 1 } , f _ { 2 } , f _ { 3 } , f _ { 4 } \}$

27. Output(F);

## References

[1] Y.G. Şahin, E. Duman, Detecting credit card fraud by decision trees and support vector machines, in: S.I. Ao, O. Castillo, C. Douglas, D.D. Feng, J.A. Lee (Eds.), Proceedings of the International MultiConference of Engineers and Computer Scientists, vol. 1, International Association of Engineers, Hong Kong, 2011, pp. 442–447.

[2] F. Fadaei Noghani, M. Moattar, Ensemble classification and extended feature selection for credit card fraud detection, Journal of AI and Data Mining 5 (2) (2017) 235-243

[3] A. Abdallah. M.A. Maarof, A. Zainal. Fraud detection system: a survey, J. Netw Comput, Appl, 68 (2016) 90–113

drocerhcaE# contains a set of raw features (card, card level, transaction amount, transaction time, transaction type, transaction amount, and MCC code).

teserutaefhcaE# contains records where is the number of cardholders.

\# is the number of cardholders

\# The data set spanned 10 months from March to December, 2016.

\# diffmonth $x _ { i j } = x _ { i 1 2 j } - x _ { i 3 j }$

\# is the number of cardholders # is the number of cardholders. # is the number of cardholders. # is the number of cardholders.

\# is the number of card levels of each card

\# is the number of cardholders

[4] Y. Li, Y. Sun, N. Contractor, Graph mining assisted semi-supervised learning for fraudulent cash-out detection, Proceedings of the 2017 IEEE/ACM Internationa Conference on Advances in Social Networks Analysis and Mining (ASONAM 2017) ACM, 2017, pp. 546–553.

[5] P.M. Domingos, A few useful things to know about machine learning, Commun. ACM 55 (10) (2012) 78–87.

[6] C. Jiang, J. Song, G. Liu, L. Zheng, W. Luan, Credit card fraud detection: a novel approach using aggregation strategy and feedback mechanism, IEEE Internet Things J. 5 (5) (2018) 3637–3647

[7] D. Olszewski, Fraud detection using self-organizing map visualizing the user pro files, Knowl.-Based Syst. 70 (2014) 324–334.

[8] M. Zareapoor, P. Shamsolmoali, Application of credit card fraud detection: based on bagging ensemble classifier, Procedia Computer Science 48 (2015) 679–685

[9] Y. Kültür, M.U. Çağlayan, A novel cardholder behavior model for detecting credi card fraud, Intelligent Automation & Soft Computing 24 (4) (2017) 807–817.

[10] C. Wang, D. Han, Credit card fraud forecasting model based on clustering analysis and integrated support vector machine, Clust. Comput. (2018) 1–6, https://doi.org 10.1007/s10586-018-2118-y.

[11] D. Sánchez, M.A. Vila, L. Cerda, J.M. Serrano, Association rules applied to credit card fraud detection, Expert Syst. Appl. 36 (2) (2009) 3630–3640.

[12] S. Xuan, G. Liu, Z. Li, L. Zheng, S. Wang, C. Jiang, Random forest for credit card fraud detection, IEEE 15th International Conference on Networking, Sensing and Control (ICNSC), IEEE, 2018, pp. 1–6.

[13] O.S. Yee, S. Sagadevan, N.H.A.H. Malim, Credit card fraud detection using machine learning as data mining technique, Journal of Telecommunication, Electronic and Computer Engineering 10 (1–4) (2018) 23–27.

[14] J.A. Gómez, J. Arévalo, R. Paredes, J. Nin, End-to-end neural network architecture for fraud scoring in card payments. Pattern Recogn. Lett. 105 (2018) 175–181.

[15] F.N. Ogwueleka, S. Misra, R. Colomo-Palacios, L. Fernandez, Neural network and classification approach in identifying customer behavior in the banking sector: a case study of an international bank, Human Factors and Ergonomics in Manufacturing & Service Industries 25 (1) (2015) 28–42.

[16] N. Carneiro, G. Figueira, M. Costa, A data mining based system for credit-card fraud detection in e-tail, Decis. Support. Syst. 95 (2017) 91–101.

[17] Y. Kültür, M.U. Çağlayan, Hybrid approaches for detecting credit card fraud, Expert. Syst. 34 (2) (2017) e12191.

[18] L. Zheng, G. Liu, C. Yan, C. Jiang, Transaction fraud detection based on total order relation and behavior diversity, IEEE Transactions on Computational Social Systems 99 (2018) 1–11

[19] S. Panigrahi, A. Kundu, S. Sural, A.K. Majumdar, Credit card fraud detection: a fusion approach using Dempster–Shafer theory and Bayesian learning, Information Fusion 10 (4) (2009) 354–363.

[20] A. Srivastava, A. Kundu, S. Sural, A. Majumdar, Credit card fraud detection using hidden Markov model, IEEE Transactions on Dependable and Secure Computing 5 (1) (2008) 37–48.

[21] E. Duman, M.H. Ozcelik, Detecting credit card fraud by genetic algorithm and scatter search, Expert Syst. Appl. 38 (10) (2011) 13057–13063.

[22] J. Jurgovsky, M. Granitzer, K. Ziegler, S. Calabretto, P.E. Portier, L. He-Guelton, O. Caelen, Sequence classification for credit-card fraud detection, Expert Syst. Appl. 100 (2018) 234–245.

[23] S. Nami, M. Shajari, Cost-sensitive payment card fraud detection based on dynamic random forest and k-nearest neighbors. Expert Syst. Appl. 110 (2018) 381–392.

[24] A. Dal Pozzolo, O. Caelen, Y.A. Le Borgne, S. Waterschoot, G. Bontempi, Learned lessons in credit card fraud detection from a practitioner perspective, Expert Syst. Appl. 41 (10) (2014) 4915–4928.

[25] C. Whitrow, D.J. Hand, P. Juszczak, D. Weston, N.M. Adams, Transaction aggregation as a strategy for credit card fraud detection, Data Min. Knowl. Disc. 18 (1) (2009) 30–55.

[26] A.C. Bahnsen, D. Aouada, A. Stojanovic, B. Ottersten, Feature engineering strategies for credit card fraud detection, Expert Syst. Appl. 51 (2016) 134–142.

[27] M. Zanin, M. Romance, S. Moral, R. Criado, Credit card fraud detection through parenclitic network analysis, Complexity 2018 (2018) 57643709 pages https://doi. org/10.1155/2018/5764370.

[28] V. Van Vlasselaer. C. Bravo. O. Caelen. T. Eliassi-Rad. L. Akoglu. M. Snoeck B. Baesens. APATE: a novel approach for automated credit card transaction fraud

detection using network-based extensions, Decis. Support. Syst. 75 (2015) 38–48.

[29] S. Bhattacharyya, S. Jha, K. Tharakunnel, J.C. Westland, Data mining for credit card fraud: a comparative study, Decis. Support. Syst. 50 (3) (2011) 602–613.

[30] T. Chen, C. Guestrin, Xgboost: a scalable tree boosting system, Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, ACM, 2016, August, pp. 785–794.

[31] X. Yu, Machine learning application in online lending risk prediction, (2017) arXiv preprint arXiv:1707.04831.

[32] Y. Li, C. Yan, W. Liu, M. Li, A principal component analysis-based random forest with the potential nearest neighbor method for automobile insurance fraud iden tification, Appl. Soft Comput. 70 (2018) 1000–1009.

[33] C. Liu, Y. Chan, S.H. Alam Kazmi, H. Fu, Financial fraud detection model: based on random forest, Int. J. Econ. Financ. 7 (7) (2015) 178–188.

[34] S. Yaram, Machine learning algorithms for document clustering and fraud detection, International Conference on Data Science and Engineering (ICDSE 2016), IEEE, 2016, pp. 1–6.

[35] C. Cortes, V. Vapnik, Support-vector networks, Mach. Learn. 20 (3) (1995) 273–297.

[36] J.O. Ramsay, B.W. Silverman, Applied Functional Data Analysis: Methods and Case Studies, Springer, New York, 2007.

[37] S. Ullah, C.F. Finch, Applications of functional data analysis: a systematic review, BMC Med, Res, Methodol, 13 (1) (2013) 43–55

[38] S. Curceac, C. Ternynck, T.B. Ouarda, F. Chebana, S.D. Niang, Short-term air temperature forecasting using Nonparametric Functional Data Analysis and SARMA models, Environ. Model Softw. 111 (2019) 394–408

[39] Longadge, R., & Dongre, S. (2013). Class imbalance problem in data mining review arXiv preprint arXiv:1305.1707

[40] M.M. Rahman, D.N. Davis, Addressing the class imbalance problem in medical datasets, International Journal of Machine Learning and Computing 3 (2) (2013) 224.

[41] A. Dal Pozzolo, G. Boracchi, O. Caelen, C. Alippi, G. Bontempi, Credit card fraud detection: a realistic modeling and a novel learning strategy, IEEE transactions on neural networks and learning systems 29 (8) (2017) 3784–3797

Yue Wu is a Ph.D. candidate at department of Information Management and Information Systems, School of Management, Fudan University, Shanghai, China. Her research in terests include credit assessment. fraud detection, and business analytics.

Yunjie Xu is a professor at the School of Management, Fudan University, Shanghai, China. He got his Ph.D. in Management Information Systems from Syracuse University, New York. His research interests cover electronic commerce, knowledge management, and business analytics. His publications appeared in Information Systems Research, Journal of Management Information Systems, Journal of Association for Information Systems, Journal of the American Society for Information Science and Technology, Communication of the ACM, Journal of Retailing, Decision Support Systems, and many more.

Jiaoyang Li a Ph.D. candidate at department of Information Management and Information Systems, School of Management, Fudan University, Shanghai, China. Her research interests include healthcare information technology, online community, and fraud detection. Her study has appeared in the DIGIT Workshop at ICIS.
