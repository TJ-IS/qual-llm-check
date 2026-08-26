---
otero_id: 17755
otero_key: "YWNGCJS5"
title: "A probabilistic reasoning model: Formulation and control strategy"
authors: "Sumit Sarkar; Deb Ghosh"
year: "1996"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(96)00010-3"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A probabilistic reasoning model: Formulation and control strategy

Sumit Sarkar, Deb Ghosh

Department of Information Systems and Decision Sciences, College of Business Administration, Louisiana State University, Baton Rouge, LA 70803, USA

## Abstract

It has been recognized that past experiences of a decision maker often plays a pivotal role in solving new problem instances. Therefore, the ability to model human reasoning processes has become an important subject of research in recent years. In many applications, the reasoning process must deal with uncertainty inherent in the problem domain. This research addresses the issue of supporting the model formulation and data acquisition processes for situations that (i) operate under uncertain conditions, and (ii) utilize evidential information that is gathered in stages. A theoretical framework is presented for the probabilistic formulation of the reasoning process that incorporates past experiences. The model is validated by testing its performance on simulated data, and is shown to work well when a sufficiently large number of cases are available for estimating probabilities. The probabilistic reasoning system can revise beliefs in an intuitively appealing and theoretically sound manner when information is acquired in an incremental fashion. Two dynamic information gathering strategies are discussed for such a reasoning system, one using information theoretic techniques, and the other using decision theoretic techniques.

Keywords: Reasoning under uncertainty; Expert systems; Sequential information acquisition; Belief revision; Decision analysis; Information theory

## 1. Introduction

The model formulation process transforms the description of a real world problem into a form that can be interpreted and executed by available modelling tools $[24]$ . Review of the literature reveals a wide array of techniques that have been suggested to assist and support this formulation process. These techniques range from mechanical construction of linear programming models $[18]$ to logic based approaches $[5,6]$ . In addition, recent studies $[7,17,24]$ have investigated case-based reasoning approaches to support the modelling activity. The primary motivation behind these studies is the recognition (and subsequent incorporation) of the pivotal role played by past experiences of the decision maker.

In general, the ability to model human reasoning processes has become an important subject of research in recent years. Kolodner states $[11]$ : “Case-based reasoning suggests a model of reasoning that incorporates problem solving, understanding, and learning and integrates all with memory processes.” In many applications, the reasoning process must deal with uncertainty inherent in the problem domain. For instance, when evaluating loan applications in banks, a loan officer utilizes a ‘model’ and examines an applicant’s details to evaluate the likelihood that the loan will be recovered by the bank. Stock market analysts employ models to predict the movement of stock prices based on indicators that only partially determine the future stock price. Therefore, in these situations, the reasoning mechanism should explicitly incorporate the uncertainty in the problem domain.

In this research, we address the issue of supporting the model formulation and data acquisition processes for situations that (i) operate under uncertain conditions, and (ii) utilize evidential information that is gathered in stages. It is important to note that a cost benefit analysis is inherent in any sequential information acquisition strategy. The sequential acquisition and analysis of evidence is a common phenomena in many business applications $[5,16]$ . For instance, in auditing a firm's statements, an auditor begins with an initial set of facts about the firm, and then obtains new evidence when some aspect of the firm's performance is not well understood $[2]$ . New information that is obtained (at added cost) is assimilated with information already available and subsequently used to analyze alternate courses of action. The information gathering and assimilation process continues until the available information leads to a reliable prediction, or all possible information sources have been exhausted. Such an approach allows the decision maker to gather the 'right' amount of information before making a decision $[4]$ .

One of the major motivations for this research stems from supporting the new vendor selection problem at a multinational organization. Basic financial data about a vendor is readily available from a fact sheet filled by the vendor. Additional information, particularly those related to the vendors' process quality, can be gathered but is time consuming and expensive and typically involve site visits and audits. In the past, a single individual used his judgement to gather whatever additional data he thought was necessary, and subjectively selected new vendors. Upon this individual's departure from the company, various spreadsheet-based scoring models have been utilized. It is interesting to note that, for this organization, subjective vendor selection actually outperformed the scoring models that were used later. Consequently, the major task was to support the new vendor selection problem incorporating past experiences, and in addition, formulate a strategy for sequential information gathering.

The primary objective of this research is to present a theoretical framework for a probabilistic formulation of models that (i) incorporate past experiences, and (ii) require sequential information gathering and assimilation. The remainder of this paper is organized as follows. In the next section, we present the probabilistic scheme. In Section 3, the probabilistic model is validated by testing its performance on simulated data. The model is shown to work well when a reasonably large number of cases (e.g., 100 or more) are available for estimating probabilities. Section 4 discusses how the proposed system revises beliefs regarding the feasible solutions, when new information is obtained in a sequential manner. We show that the procedure to evaluate probabilities is invariant to the order in which evidence has been accumulated. A procedure to 'undo' the effect of evidence already assimilated is presented and shown to be computationally efficient. Section 5 presents an information gathering strategy that guides the question-answer process when evaluating a new situation. We show how information theoretic considerations can be used to determine which of the unknown pieces of information is the most informative at any given time, and consequently should be acquired next. A decision theoretic approach for the information gathering strategy is developed for those applications where benefits and losses associated with different outcomes are available. Section 6 concludes this paper.

## 2. Estimation of probabilities

In this section, we discuss how probabilities are used to evaluate a new problem instance based on past experiences. We use the problem of evaluating new vendors to illustrate this process. In the vendor selection problem, a probabilistic estimate must be determined about the ability of a new vendor to be considered as a future supplier. The primary objective is to evaluate vendors as 'Good' if they demonstrate the potential to fulfill their contracts in a timely manner by providing products of requisite quality within pre-determined prices. If they do not display this potential, they are evaluated as 'Poor'. The evaluation is made based on an economic and qualitative assessment of the vendor. The economic assessment involves examining some important financial ratios from the vendors profit and loss statements in order to judge the stability of the company. Qualitative criteria that are considered include factors such as does the vendor have ISO 9000 certification, does the vendor have production capabilities to supply the required quantities, does the vendor carry necessary amounts of inventory, etc. In some cases, the evaluation can be easily made based on the information available about the vendor. However, often a clear decision cannot be made based on the available information. In such cases, it is important to determine the probability that the vendor is 'Good', and if necessary, obtain additional information that will help to make a final decision.

In order to estimate the probability that the vendor under consideration is ‘Good’, the profiles of vendors who have supplied goods in the past are examined. The rationale behind this is that if a vendor has a profile (in terms of the evaluation factors) that is similar to other vendors who have performed well, then the new vendor is likely to perform well also. Similarly, if the profile more closely matches the suppliers who could not fulfil their contract(s) adequately, then the new vendor is unlikely to perform well and should be disqualified. Therefore, all of the factors that are known about existing vendors are stored and used for estimating probabilities about new vendors. Also stored along with the data for an existing vendor is the outcome of using that vendor, i.e. whether the vendor was found to be ‘Good’ or ‘Poor’. Some of the factors that are considered in the evaluation are discrete in nature (e.g. ISO 9000 certification), while others are continuous (e.g. financial ratios). To ease the task of estimating probabilities, all factors that are continuous in nature are converted to discrete using some appropriate transformation rules. For instance, each financial ratio for a vendor is classified as either ‘Above Average’ or ‘Below Average’ by comparing it to the average for companies with the same SIC code.

When a new vendor is to be evaluated, the system estimates the probability that the vendor is of type 'Good', based on the information available about the vendor. Let the set of factors (also termed attributes) that are available be $X_{1}, \ldots, X_{n}$ , and A be the outcome variable. If the vendor under consideration has the attribute values, $X_{1} = x_{1}, \ldots, X_{n} = x_{n}$ , then the probability estimate required is: $P(A = 'Good' | X_{1} = x_{1}, \ldots, X_{n} = x_{n})$ . A problem encountered in estimating this probability is that there may not be multiple historical instances with exactly the same set of attribute values $X_{1} = x_{1}, \ldots, X_{n} = x_{n}$ . However, the notion of conditional independence allows us to estimate the required probability without requiring multiple instances with the same attribute values. We demonstrate with an example how the conditional independence property is used to evaluate the probability measures for the two outcomes. Two important factors that are used to evaluate a vendor are (i) the Turnover ratio, TRatio, which is the ratio of the projected sales amount to the total turnover of the vendor (when the TRatio is less than 10% it is considered a good sign, as it indicates that the vendor has a large base of existing customers), and (ii) ISO 9000 certification. The two factors are conditionally independent of each other with respect to the ability of the vendor when, for a given ability, the probability that the ratio is 'Good' (or 'Poor') is independent of whether the vendor has the quality certification. The probabilistic representation of this property is shown below:

$$
\mathrm{P} \left(\text {TRatio} = ^ {\prime} \text {Good} ^ {\prime} | \text {Ability} = ^ {\prime} \text {Good} ^ {\prime} \& \text {ISO} 9000 = ^ {\prime} \text {True} ^ {\prime}\right) = \mathrm{P} \left(\text {TRatio} = ^ {\prime} \text {Good} ^ {\prime} | \text {Ability} = ^ {\prime} \text {Good} ^ {\prime}\right).
$$

The use of the conditional independence property allows us to evaluate the required probabilities associated with different outcome states even when the attribute values known about a new vendor do not completely match the corresponding attribute values for existing vendors. Using the well-known Bayes rule, the desired probability terms can be estimated using the following expressions (the derivation is provided in Appendix 1):

$$
\mathrm{P} (\text {Ability} = ^ {\prime} \text {Good} ^ {\prime} | \text {TRatio} = ^ {\prime} \text {Good} ^ {\prime} \& \& 9 0 0 0 = ^ {\prime} \text {True} ^ {\prime})
$$

$$
= \frac {1}{K} \cdot P (T R a t i o = ^ {\prime} G o o d ^ {\prime} | A b i l i t y = ^ {\prime} G o o d ^ {\prime}) \cdot P (I S O 9 0 0 0 = ^ {\prime} T r u e ^ {\prime} | A b i l i t y = ^ {\prime} G o o d ^ {\prime}) \cdot P (A b i l i t y = ^ {\prime} G o o d ^ {\prime})
$$

$$
\begin{array}{l} \mathrm {P(Ability = 'Poor'|TRatio = 'Good'\&\&9000 = 'True'}) \\ = \frac {1}{K} \cdot P (T R a t i o = ' G o o d ^ {\prime} | A b i l i t y = ' P o o r ^ {\prime}) \cdot P (I S O 9 0 0 0 = ' T r u e ^ {\prime} | A b i l i t y = ' P o o r ^ {\prime}) \cdot P (A b i l i t y = ' P o o r ^ {\prime}), \end{array}
$$

where K is the sum of the numerators in the two expressions, called the normalization factor.

All component probability terms in the above expressions can be estimated from the data on known vendors. The above procedure is easily extended to the case where multiple attributes of the new vendor are available. If the attributes and corresponding values are given by $X_{1}=x_{1},\ldots,X_{n}=x_{n}$ , then the probability estimates are:

$$
\begin{array}{l} \mathrm {P(Ability = `Good'|X_ {1} = x_ {1} ,\ldots, X_ {n} = x_ {n})} \\ \quad = \frac {1}{K} \cdot P (X _ {1} = x _ {1} | A b i l i t y = ` G o o d ^ {\prime}) \dots P (X _ {n} = x _ {n} | A b i l i t y = ` G o o d ^ {\prime}) \cdot P (A b i l i t y = ` G o o d ^ {\prime}), \\ \text { and } \\ \mathrm {P(Ability = `Poor'|X_ {1} = x_ {1} ,\ldots, X_ {n} = x_ {n})} \\ \quad = \frac {1}{K} \cdot P (X _ {1} = x _ {1} | A b i l i t y = ` P o o r ^ {\prime}) \dots P (X _ {n} = x _ {n} | A b i l i t y = ` P o o r ^ {\prime}) \cdot P (A b i l i t y = ` P o o r ^ {\prime}), \end{array}
$$

where K is the appropriate normalization factor.

In practice, all of the factors that are considered may not be conditionally independent of each other, given the outcome state (i.e., Vendor Ability). For instance, two financial ratios that are considered to be important are the Quick Ratio (QR) and the Current Ratio (CR). These two ratios provide an indication of the vendor's Liquidity, and are usually not conditionally independent of each other for a given outcome. For this reason, these two ratios are treated as a compound attribute when used to estimate the required probabilities. Therefore, if in addition to knowledge about ISO 9000 certification for a new vendor, these two ratios were known (e.g., QR = 'Above Average' and CR = 'Above Average'), the probability estimates would be obtained as follows:

$$
\begin{array}{r l} & \mathrm {P(Ability = `Good'|QR > Avg\& CR > Avg\& ISO 9000 = `True')} \\ & = \frac {1}{K} \cdot \mathrm {P(QR > Avg\& CR > Avg|Ability = `Good')\cdot P(ISO 9000 = `True'|Ability = `Good')} \\ & \cdot \mathrm {P(Ability = `Good'),} \end{array}
$$

and

$$
\begin{array}{r l} & \mathrm {P(Ability = 'Poor'|QR > Avg\& CR > Avg\& ISO 9000 = 'True')} \\ & \quad = \frac {1}{K} \cdot \mathrm {P(QR > Avg\& CR > Avg|Ability = 'Poor')\cdot P(ISO 9000 = 'True'|Ability = 'Poor')} \\ & \quad \cdot \mathrm {P(Ability = 'Poor').} \end{array}
$$

Other financial ratios that are used to evaluate a vendor are also clubbed together where appropriate. For instance, the ratios Return on Net Worth, Return on Total Assets, and Before Tax Margin are indicators of the vendors Profitability and are considered as part of the same compound attribute. The use of compound attributes leads to more accurate probability estimates. Some of the compound attributes used for the vendor selection problem and their component simple attributes are shown in Table 1.

Table 1  
Some compound attributes and their components

<table><tr><td>Compound attribute</td><td>Component simple attributes</td></tr><tr><td>Liquidity</td><td>Current ratio, quick ratio, inventory to current assets, historical analysis</td></tr><tr><td>Profitability</td><td>Return on net worth, return on total assets, before tax margin, historical analysis</td></tr><tr><td>Activity</td><td>Turnover ratio, inventory turnover, receivables turnover, historical analysis</td></tr><tr><td>Available facility</td><td>Observed capacity after site visit</td></tr><tr><td>Ext. references</td><td>Dunn &amp; Bradstreet rating, bank references, customer references</td></tr><tr><td>Quality</td><td>ISO 9000 certification, existing formal quality program, quality audit</td></tr><tr><td>Safety</td><td>OSHA incidence, lost workday injury rate, formal safety program</td></tr></table>

A prospective vendor submits a fact sheet along with its financial statements for the most recent year. Many of the attributes listed above are directly obtained from the fact sheet and the financial statement (e.g. financial ratios, ISO 9000 Certification, OSHA Incidence, etc.). In some instances, the company performs a more detailed analysis of the vendor's financial situation by examining its statements for the last three years (summarized by the attribute Historical Analysis). This is usually necessary when the most recent year's data does not provide a clear indication of the vendor's financial situation. Some of the attributes, like determining if the vendor's existing production capacity is adequate, can be observed from making site visits. Yet other information is obtained from external sources like the vendor's bank, references from prior customers of the vendor, and the Dunn and Bradstreet Rating for the vendor.

In summary, the general expression for the probability estimate is obtained as follows. Let $Y_{1}, Y_{2}, \ldots, Y_{r}$ be the specified set of compound attributes that are available for a new vendor. Then, the resulting probability for the outcome state A = ‘Good’ and A = ‘Poor’ are obtained as:

$$
\mathrm{P} \left(\mathrm{A} = ^ {\prime} \text {Good} ^ {\prime} \mid Y _ {1} = y _ {1}, Y _ {2} = y _ {2}, \dots , Y _ {r} = y _ {r}\right) = \frac {\mathrm{P} \left(\mathrm{A} = ^ {\prime} \text {Good} ^ {\prime}\right)}{\mathrm{K}} \prod_ {j = 1, r} \mathrm{P} \left(Y _ {j} = y _ {j} \mid \mathrm{A} = ^ {\prime} \text {Good} ^ {\prime}\right),
$$

and

$$
\mathrm{P} \left(\mathrm{A} = ^ {\prime} \text {Poor} ^ {\prime} \mid Y _ {1} = y _ {1}, Y _ {2} = y _ {2}, \dots , Y _ {r} = y _ {r}\right) = \frac {\mathrm{P} \left(\mathrm{A} = ^ {\prime} \text {Poor} ^ {\prime}\right)}{\mathrm{K}} \prod_ {j = 1, r} P \left(Y _ {j} = y _ {j} \mid \mathrm{A} = ^ {\prime} \text {Poor} ^ {\prime}\right),
$$

where

$$
K = \mathrm{P} (\mathrm{A} = ^ {\prime} \text {Good} ^ {\prime}) \prod_ {j = 1, r} \mathrm{P} (Y _ {j} = y _ {j} | \mathrm{A} = ^ {\prime} \text {Good} ^ {\prime}) + \mathrm{P} (\mathrm{A} = ^ {\prime} \text {Poor} ^ {\prime}) \prod_ {j = 1, r} P (Y _ {j} = y _ {j} | A = ^ {\prime} \text {Poor} ^ {\prime}).
$$

Operationally, all simple attributes are stored as before; they are treated as a compound attribute only when used to assess the necessary probabilities. The number of realizations for a compound attribute is the cartesian product of the number of realizations of each of its component simple attributes. The probability measure associated with an outcome state is determined by first estimating the probability of each component in the right hand side (evaluated from existing cases) and then obtaining their product. Once the products for all possible outcomes have been evaluated, they are normalized to calculate the necessary conditional probabilities.

The procedure to estimate probabilities is computationally efficient. Consider a situation where r compound attributes $Y_{1}, Y_{2}, \ldots, Y_{r}$ consisting of a total of n simple attributes are used to estimate the desired probabilities. Let b be the number of different outcomes, $a_{1}, \ldots, a_{b}$ for which probabilities are to be estimated. Then, the following expression is to be evaluated for each i:

$$
\mathrm{P} \left(\mathrm{A} = \mathrm{a} _ {i} \mid Y _ {1}, Y _ {2}, \dots , Y _ {r}\right) \propto \mathrm{P} \left(Y _ {1} \mid \mathrm{A} = \mathrm{a} _ {i}\right) \times \dots \times \mathrm{P} \left(Y _ {2} \mid \mathrm{A} = \mathrm{a} _ {i}\right) \times \mathrm{P} (\mathrm{A} = \mathrm{a} _ {i}).
$$

A component term in the right hand side of the above expression of the form $\mathrm{P}(Y_{j}|\mathrm{A}=\mathrm{a}_{i})$ is evaluated by determining the frequency of occurrences of $(Y_{j}=y_{j}\&\mathrm{A}=\mathrm{a}_{i})$ , and, of occurrences of $(\mathrm{A}=\mathrm{a}_{i})$ , in the existing cases. Obtaining these counts require $c\cdot(d+1)$ comparisons, where c is the number of existing cases and d is the number of simple variables in the compound attribute. Since similar counts are required for each compound attribute, they can be obtained by sequentially reading each case and incrementing the count of all the necessary numerators and denominators. Therefore, the total number of operations to obtain the counts are of the order $\mathrm{O}(c\cdot(n+1))$ . To evaluate the necessary conditional probability terms, a total of $r\cdot b$ operations are required. Calculating the evaluation functions require another $r\cdot b$ number of operations, followed by the normalization of the products which is of order $\mathrm{O}(b)$ . Therefore, the overall time complexity is no worse than $\mathrm{O}(c\cdot(n+1)+r\cdot b)$ .

## 3. Accuracy of estimated probabilities

When estimating probabilities associated with uncertain outcomes, an important question is how close are the probability estimates to the actual uncertainty about the outcome (subsequently referred to as the ‘true’ probability distribution) inherent in the problem domain. Clearly, closer the probability estimates to the 'true' probability distribution, better will be the decisions that are made using that information. A practical difficulty associated with comparing probability estimates obtained from our model with the 'true' probabilities is that the latter is hard to obtain for real world problems. It has been widely noted that decision makers are notoriously poor at verbalizing probability estimates accurately, even when they are able to make good decisions in a consistent manner $[22,25]$ . For this reason, we have used simulated data to examine the accuracy of the probabilistic model by testing its ability to predict the correct outcome. In this section, we describe how these tests were performed, and then present the results of these tests.

The tests are performed on data that were generated using Monte Carlo simulation techniques. There were two stages in generating the data used for testing purposes. In the first stage, we randomly generated an underlying probability model for the outcome variable and the attributes associated with it. This involved identifying which factors belong to the same compound attribute, and then generating the joint distribution across the outcome variable and the compound attributes. Consider the situation where 10 different attributes are used to make predictions about the outcome. Then, a feasible set of compound attributes that may be generated is:

$$
Y _ {1} = \left\{X _ {1}, X _ {2} \right\}; Y _ {2} = \left\{X _ {3}, X _ {4}, X _ {5}, X _ {6} \right\}; Y _ {3} = \left\{X _ {7} \right\}; \text {and} Y _ {4} = \left\{X _ {8}, X _ {9}, X _ {1 0} \right\}.
$$

Once the compound attributes are generated, the underlying probabilistic dependency between each compound attribute and the outcome variable is simulated. This requires specifying a joint probability distribution across each compound attribute $Y_{i}$ and the outcome A. Such a joint distribution for a compound attribute $Y_{i}$ is specified by providing the probability masses associated with each feasible realization across $Y_{i}$ and A. Thus, if we assume all variables are binary, then we need 8 probability masses to specify the joint distribution across $Y_{1}$ and A, 32 probability masses for the joint distribution across $Y_{2}$ and A, etc. For each compound attribute, we generated the requisite number of random numbers between 0 and 1, and then normalized them to obtain the desired probability distributions.

In the second stage, we used the probability model to generate the actual cases that are used to estimate probabilities. Each case used for estimation is generated in the following manner. A realization for outcome A is randomly drawn based on the probability associated with the outcome. For each compound attribute, a set of realizations for each component attribute is randomly generated based on the realization of the outcome, and the joint distribution associated with that compound variable and the outcome. In order to examine the predictive ability of the probabilistic model, we generated two sets of cases. The first set of cases generated was used to obtain probability estimates. For each case in the second set, the probabilities of the outcome states were estimated based on the realizations of the other attributes. The outcome state predicted by the probabilistic model was one with the largest estimated posterior probability. The predicted outcome was then compared with the true outcome in order to verify the accuracy of the estimation technique.

To keep the experiments relatively simple, we assumed all variables to be binary in nature. Further, we restricted the size of each compound attribute to consist of at most four variables. Clearly, we would expect the accuracy of the probability estimation technique to improve when a larger number of cases were used for estimation. We conducted experiments by varying the number of cases used for estimation from as few as 20 to as many as 1000 cases. Another factor that could affect the predictive ability of the technique is the number of factors used for predicting the outcome variable. To examine this effect, we conducted experiments using 5, 10, 15, 20, 25, and 30 attributes, respectively. In each experiment, the outcome state was predicted for 100 cases with unseen outcomes. Since the ability to predict the outcome could depend on the underlying probability distribution (i.e., the generated ‘true’ distribution), each experiment was repeated for 10 different underlying distributions, and the ability to predict the correct outcome was averaged over all these underlying distributions. The different experiments and their results are summarized in Table 2.

The fourth row in Table 2 shows that when 20 attributes were considered, and 20 cases used to estimate probabilities for outcome states, the outcome state for unseen cases was correctly predicted in 83.6 percent of those cases. When 30 cases were used to estimate probabilities, 88.8% of unseen cases were correctly identified. As the number of cases increased, the predictively ability also improved. When 1000 cases were provided for estimation purposes, the correct outcome was predicted in 97.1% of the cases. A similar trend was observed for the experiments that were run with different numbers of attributes used for prediction.

Table 2  
Percentage of correct predictions

<table><tr><td rowspan="2">Number of attributes</td><td colspan="6">Number of cases</td></tr><tr><td>20</td><td>30</td><td>50</td><td>100</td><td>500</td><td>1000</td></tr><tr><td>5</td><td>78.3</td><td>79.4</td><td>80.3</td><td>82.1</td><td>83.1</td><td>82.5</td></tr><tr><td>10</td><td>78.9</td><td>83.0</td><td>86.3</td><td>90.4</td><td>93.5</td><td>93.3</td></tr><tr><td>15</td><td>76.4</td><td>83.3</td><td>87.1</td><td>91.0</td><td>94.8</td><td>95.2</td></tr><tr><td>20</td><td>83.6</td><td>88.8</td><td>91.2</td><td>94.6</td><td>97.1</td><td>97.1</td></tr><tr><td>25</td><td>78.4</td><td>83.7</td><td>90.0</td><td>94.4</td><td>96.6</td><td>97.4</td></tr><tr><td>30</td><td>68.5</td><td>76.3</td><td>85.0</td><td>92.7</td><td>97.8</td><td>98.3</td></tr></table>

The improvement in predictive ability was less marked when the number of attributes used for prediction was increased from 5 to 30. When the number of cases used for estimation was relatively high (500 and 1000 cases, respectively), the predictive ability did improve with a larger set of attributes. For smaller sets of cases (less than 100), the accuracy in predictive ability appeared to improve and then deteriorate as the number of variables increased. On detailed examination of the probability estimates, the following phenomena was observed. The probability estimates for relatively larger compound attributes (i.e. those with three or four component attributes) were more prone to error when sample sizes used were less than or equal to 100. This results from the fact that there were relatively few samples that matched the realizations of such compound attributes for the cases being tested. For example, a compound attribute with four binary variables could have potentially 16 different realizations. Clearly, a sample size of 50 or less would provide, on average, very few samples for each possible realization. This leads to less accurate probability estimates. Since the number of large compound attributes were higher for problems with a larger number of variables, this counteracted the increased predictive ability from a larger set of variables.

Overall, the experiments show that the probabilistic approach predicted outcomes accurately when the number of cases available for estimating probabilities exceeded 100. For such sample sizes, the prediction was accurate at least 90% of the time when 10 or more predictive variables were available. Thus, for applications where hundreds of cases are available, the probabilistic approach is appropriate. When fewer cases are available, the probabilities estimated are less accurate, and may not be acceptable for making critical decisions.

An important feature of the probabilistic reasoning technique is that it provides the probability estimates that are used to make a prediction, and not just the predicted outcome state. These probability estimates can provide a decision maker additional insight regarding the accuracy of a prediction. For instance, if the recommended outcome state has a probability estimated as 0.9, this would indicate that under the observed circumstances, the predicted outcome state should materialize around 90% of the time. Similarly, if the outcome state is predicted with probability only 0.6, we would expect the outcome state to materialize correspondingly less frequently. Clearly, a probability estimate of 0.9 should lead to a much stronger belief regarding the occurrence of an outcome state than an estimate of 0.6. Thus, it is important to know if the predicted probability estimates are reliable indicators of the eventual outcome state. We examined the experimental results to observe the following: (i) how often does the reasoning system provide predictions with a probability estimate greater than 0.9 about the outcome based on the observed data; and (ii) what is the proportion of correct predictions when the probability estimate provided is greater than 0.9. Table 3 provides a summary of the percentage of cases that were predicted with a final probability estimate greater than 0.9 for each of the experiments described above. Table 4 presents a summary of the accuracy of predictions that were made with a probability estimate of greater than 0.9, while Table 5 summarizes the accuracy of predictions that were made with a probability estimate of less than 0.9.

Table 3  
Percentage of cases predicted with estimated probability $\geq 0.9$

<table><tr><td>Number of attribute</td><td colspan="6">Number of cases</td></tr><tr><td>s</td><td>20</td><td>30</td><td>50</td><td>100</td><td>500</td><td>1000</td></tr><tr><td>5</td><td>22.3</td><td>32.5</td><td>40.0</td><td>42.3</td><td>44.6</td><td>46.7</td></tr><tr><td>10</td><td>33.2</td><td>42.5</td><td>48.1</td><td>62.4</td><td>73.9</td><td>75.7</td></tr><tr><td>15</td><td>43.3</td><td>47.5</td><td>62.5</td><td>71.6</td><td>83.6</td><td>83.5</td></tr><tr><td>20</td><td>58.6</td><td>66.5</td><td>75.0</td><td>83.6</td><td>88.2</td><td>90.5</td></tr><tr><td>25</td><td>58.0</td><td>64.0</td><td>74.6</td><td>83.1</td><td>90.3</td><td>90.4</td></tr><tr><td>30</td><td>69.8</td><td>72.5</td><td>78.2</td><td>87.0</td><td>94.8</td><td>95.8</td></tr></table>

Table 4  
Percentage of correct predictions for cases with estimated probability $\geq$ 0.9

<table><tr><td rowspan="2">Number of attributes</td><td colspan="6">Number of cases</td></tr><tr><td>20</td><td>30</td><td>50</td><td>100</td><td>500</td><td>1000</td></tr><tr><td>5</td><td>92.38</td><td>95.69</td><td>97.00</td><td>96.45</td><td>96.64</td><td>95.50</td></tr><tr><td>10</td><td>93.98</td><td>95.29</td><td>96.26</td><td>97.28</td><td>99.46</td><td>98.81</td></tr><tr><td>15</td><td>89.61</td><td>93.05</td><td>96.32</td><td>97.91</td><td>98.44</td><td>98.80</td></tr><tr><td>20</td><td>94.88</td><td>96.84</td><td>98.00</td><td>98.56</td><td>99.55</td><td>99.45</td></tr><tr><td>25</td><td>88.62</td><td>91.88</td><td>95.98</td><td>98.56</td><td>99.34</td><td>99.34</td></tr><tr><td>30</td><td>72.78</td><td>84.41</td><td>92.84</td><td>96.90</td><td>99.58</td><td>99.58</td></tr></table>

In general, the number of cases that are predicted with probability greater than 0.9 increased with both the number of variables used for prediction, as well as, the number of cases used to estimate probabilities. Table 3 shows that when 10 or more variables were used, and 100 or more cases were used for estimating probabilities, then in each experiment at least half the predictions were made with a probability estimated at greater than 0.9. When 30 variables and 1000 cases were used for estimation, the outcome states for 95.8% of all unseen cases were predicted with a probability estimate greater than 0.9. These results help to illustrate that the probabilistic technique provides sharp probability predictions when either 10 or more variables are used, or, a large number of cases are available for prediction, or both.

Table 4 shows the proportion of correct predictions made when the probability estimate for the predicted outcome state was greater than 0.9. Clearly, for the estimates to be reliable, we would expect correct predictions for those cases to be between 90% and 100%. The results show that to be the case for all but a few. The exceptions occur when the number of cases used for estimation are 30 or fewer. Similarly, when the predicted outcome has a probability estimate less than 0.9, we find from Table 5 that the percentage of correct predictions lie between 50% and 90% for every experiment conducted. These results show that the probability estimate is a reliable indicator of the uncertainty associated with different outcome states.

Table 5  
Percentage of correct predictions for cases with estimated probability < 0.9

<table><tr><td rowspan="2">Number of attributes</td><td colspan="6">Number of cases</td></tr><tr><td>20</td><td>30</td><td>50</td><td>100</td><td>500</td><td>1000</td></tr><tr><td>5</td><td>74.26</td><td>71.56</td><td>69.17</td><td>71.58</td><td>72.20</td><td>71.11</td></tr><tr><td>10</td><td>71.41</td><td>73.92</td><td>77.07</td><td>78.98</td><td>76.62</td><td>76.14</td></tr><tr><td>15</td><td>66.31</td><td>72.57</td><td>71.73</td><td>73.58</td><td>76.24</td><td>76.98</td></tr><tr><td>20</td><td>67.63</td><td>72.84</td><td>70.80</td><td>74.41</td><td>78.79</td><td>74.71</td></tr><tr><td>25</td><td>64.29</td><td>69.16</td><td>72.44</td><td>73.94</td><td>71.09</td><td>79.13</td></tr><tr><td>30</td><td>58.61</td><td>54.92</td><td>56.88</td><td>64.59</td><td>65.35</td><td>69.10</td></tr></table>

We note that the necessary probability estimates were obtained in a very short amount of time for each of the above experiments. For instance, less than one minute was needed by a C compiler running on an Unix based RS 6000 processor to estimate the desired probabilities for all of the 100 new cases in the second set, when 30 variables and 1000 cases from the first set were used to estimate probabilities.

## 4. Belief revision

We have shown how probability measures associated with different outcome states can be evaluated for a new case when some of its attribute values are known. However, in many instances, a final decision can only be made after obtaining additional evidence, and using the evidence to refine beliefs about the outcome states. For example, when evaluating a prospective vendor, a site visit may be required to determine if the vendor has adequate production capacity for handling large orders. Such a site visit is performed only after the data supplied by the vendor is found to meet required standards. Similarly, if the vendor supplies non-standard items, references from prior customers may be obtained before making a final decision. In this section, we first discuss how the probabilistic reasoning system revises beliefs regarding outcome states when new information (attribute value) is obtained in an incremental manner. Next, we show that the procedure to update beliefs is invariant of the order in which the evidence is assimilated. Finally, we present a procedure to ‘undo’ the effect of evidence already assimilated, and the procedure to revise beliefs when the outcome of some evidence is changed during the assimilation process (which we call the ‘redo’ procedure). Both the ‘undo’ and the ‘redo’ procedure are shown to be computationally efficient.

## 4.1. Incremental belief revision

Let A be the outcome variable and W = w be the set of variables that have already been observed and assimilated by the system. The beliefs regarding the different outcome states $a_{i}$ are given by $P(A = a_{i}|W = w)$ , and are assumed to have been evaluated earlier. Let X be a new variable that is observed. Two cases must be considered for the belief revision procedure.

Case I: The new piece of information, X, is the only component of a compound attribute, or, is one of multiple components of a compound attribute, none of which have been observed yet.

Consider the situation, where X is the only component of a compound attribute (e.g., Observed Capacity for the vendor evaluation problem). In that case, it is conditionally independent of all other attributes with respect to A. It then follows that (derivation shown in Appendix B):

$$
\mathrm{P} \left(\mathrm{A} = \mathrm{a} _ {i} | \mathrm{X} = \mathrm{x}, \underline {{W}} = \underline {{w}}\right) = \frac {\mathrm{P} \left(\mathrm{X} = \mathrm{x} | \mathrm{A} = \mathrm{a} _ {1}\right)}{\mathrm{P} \left(\mathrm{X} = \mathrm{x} | \underline {{W}} = \underline {{w}}\right)} \cdot \mathrm{P} \left(\mathrm{A} = \mathrm{a} _ {i} | \underline {{W}} = \underline {{w}}\right) \forall i.
$$

Since the denominator is the same for all values of A, $P(A = a_{i}|X = x, W = w)$ is obtained by normalizing the product $P(X = x|A = a_{i}) \cdot P(A = a_{i}|W = w) \forall i$ . $P(A = a_{i}|W = w)$ is the belief accorded to the different outcome states as a result of the prior information W = w, and is already available to the system. The other expression, $P(X = x|A = a_{i})$ , is the likelihood of observing the realization X = x for different outcome states. This is easily estimated from the cases once X is observed. From the discussion on time complexity presented in Section 2, it follows that the necessary computations are of order no worse than $O(c + r \cdot b)$ .

An identical procedure is used to revise beliefs when the new piece of information, X, is one of multiple components of a compound attribute, none of which have been observed. Since the variable X is conditionally independent of the set of observed variables W with respect to A, the above analysis holds.

Case II: The new piece of information, X, is one of multiple components of a compound attribute, some of which have already been observed.

In this case, X is part of a compound attribute $Y_{i}$ , and one or more other components of $Y_{i}$ have already been observed. For instance, this is the case when a Quality Audit is required for a prospective vendor who has already supplied information on other Quality related attributes like ISO 9000 Certification. Let Z = z be the set of variables that are part of $Y_{i}$ and have been observed. Further, let $W' = w'$ be the other observed variables (i.e., $Z \cup W' = W$ ). As shown in Appendix B, we then have:

$$
\mathrm{P} \left(\mathrm{A} = \mathrm{a} _ {i} | \mathrm{X} = \mathrm{x}, W = w\right) = \frac {\mathrm{P} \left(\mathrm{X} = \mathrm{x} | Z = z , \mathrm{A} = \mathrm{a} _ {i}\right)}{\mathrm{P} \left(\mathrm{X} = \mathrm{x} | \underline {{{W}}} = \underline {{{w}}}\right)} \cdot \mathrm{P} \left(\mathrm{A} = \mathrm{a} _ {i} | \underline {{{W}}} = \underline {{{w}}}\right) \forall i.
$$

Once again, the denominator $P(X = x|W = w)$ is the same for all i. The revised belief $P(A = a_{i}|X = x,W = w)$ is obtained by multiplying the prior belief $P(A = a_{i}|W = w)$ with the likelihood $P(X = x|Z = z,A = a_{i})$ for each outcome state $a_{i}$ , and suitably normalizing this product.

The procedure to revise beliefs is very easy to implement. When Case I is applicable, then the system has to estimate afresh only the probabilities $P(X = x|A = a_i)$ for each i, in order to evaluate the new posterior distribution. This can be accomplished easily from the existing cases, and does not depend on the set W of observed evidence. For situations in Case II, the probabilities $P(X = x|A = a_i, Z = z)$ have to be evaluated from the cases. This expression is dependent only on the subset Z of the realized variables W. When many information items have already been observed, Z is small compared to W, and will lead to an efficient and robust estimation of $P(X = x|A = a_i, Z = z)$ . The time complexity for this case is no worse than $O(c \cdot (d + 1) + r \cdot b)$ .

## 4.2. Invariance of the revision procedure to the order of information acquisition

The procedure to update probabilities based on new evidence demonstrates some very desirable properties. We show that when multiple pieces of evidence have been observed and assimilated by the system, it arrives at the same posterior distribution for the outcome A irrespective of the order in which the evidence was obtained. Let W be the set of variables that have been assimilated, and X and U be two new pieces of evidence. We show that $P(A = a_{i}|X = x, U = u, W = w)$ is the same irrespective of whether X or U is first used to revise beliefs about A. The following two cases cover the possible scenarios.

Case I: $X$ and $U$ belong to different compound attributes

Let X be part of the compound attribute $Y_{X}$ , and $Z_{X}$ be the set of variables that are part of $Y_{X}$ and have been observed. Similarly, let U be part of the compound attribute $Y_{U}$ , and $Z_{U}$ be the set of variables that are part of $Y_{U}$ and have been observed. Finally, let $W' = w'$ be the other observed variables (i.e., $Z_{X} \cup Z_{U} \cup W' = W$ ). The posterior probability for $A = a_{i}$ can be expressed by the following expression, irrespective of the order in which X and U are observed (proof is provided in Appendix C).

$$
\begin{array}{l} \mathrm{P} (\mathrm{A} = \mathrm{a} _ {i} | \mathrm{U} = \mathrm{u}, \mathrm{X} = \mathrm{x}, \underline {{W}} = \underline {{w}}) \\ = \frac \mathrm{P} (\mathrm{U} = \mathrm{u} | \underline {{Z _ {\mathrm{U}}}} = \underline {z _ {\mathrm{U}}} , \mathrm{A} = \mathrm{a} _ {i}) \cdot \mathrm{P} (\mathrm{X} = \mathrm{x} | \underline {{Z _ {\mathrm{X}}}} = \underline {{z _ {\mathrm{X}}} , \mathrm{A} = \mathrm{a} _ {i}) \cdot \mathrm{P} (\mathrm{A} = \mathrm{a} _ {i} | \underline {{W}} = \underline {{w}})}\sum_ {i} \mathrm{P} (\mathrm{U} = \mathrm{u} | \underline {{Z _ {\mathrm{U}}}} = \underline {{z _ {\mathrm{U}} , \mathrm{A} = \mathrm{a} _ {i}}}) \cdot \mathrm{P} (\mathrm{X} = \mathrm{x} | \underline {{Z _ {\mathrm{X}}}} = \underline {{z _ {\mathrm{X}}} , \mathrm{A} = \mathrm{a} _ {i}) \cdot \mathrm{P} (\mathrm{A} = \mathrm{a} _ {i} | \underline {{W}} = \underline {{w}})}. \end{array}
$$

In the above expression, the term $\mathrm{P}(\mathrm{U}=\mathrm{u}|Z_{\mathrm{U}}=z_{\mathrm{U}},\mathrm{A}=\mathrm{a}_{i})$ does not depend on X, and the term $\mathrm{P}(\mathrm{X}=\mathrm{x}|Z_{\mathrm{X}}=z_{\mathrm{X}},\mathrm{A}=\mathrm{a}_{i})$ does not depend on U. Therefore, the expression for the posterior probability $\mathrm{P}(\mathrm{A}=\mathrm{a}_{i}|\mathrm{U}=\mathrm{u},\mathrm{X}=\mathrm{x},W=w)$ is not dependent on the order in which X and U are used to update beliefs.

Case II: Both X and U belong to the same compound attribute

Let X and U belong to the compound attribute $Y_{i}$ , and Z = z be the set of variables that are part of $Y_{i}$ and have been observed. Further, let $W' = w'$ be the other observed variables (i.e., $Z \cup W' = W$ ). When X is observed first, followed by U, we have (proof in Appendix C):

$$
\begin{array}{l} \mathrm{P(A=u|U=u,X=x,W=w)} \\ = \frac {\mathrm{P(U=u|X=x,Z=z,A=a_{i})\cdot P(X=x|Z=z,A=a_{i})\cdot P(A=a_{i}|W=w)}}\sum_ {i} \mathrm{P(U=u|X=x,Z=z,A=a_{i})\cdot P(X=x|Z=z,A=a_{i})\cdot P(A=a_{i}|W=w)}. \end{array}
$$

Similarly, when U is observed first, followed by X, we have:

$$
\begin{array}{l} \mathrm{P} (\mathrm{A} = \mathrm{a} _ {i} | \mathrm{X} = \mathrm{x}, \mathrm{U} = \mathrm{u}, \underline {{W}} = \underline {{w}}) \\ = \frac {\mathrm{P} (\mathrm{X} = \mathrm{x} | \mathrm{U} = \mathrm{u} , \underline {{Z}} = \underline {{z}} , = \mathrm{A} = \mathrm{a} _ {i}) \cdot \mathrm{P} (\mathrm{U} = \mathrm{u} | \underline {{Z}} = \underline {{z}} , \mathrm{A} = \mathrm{a} _ {i}) \cdot \mathrm{P} (\mathrm{A} = \mathrm{a} _ {i} | \underline {{W}} = \underline {{w}})}{\sum_ {i} \mathrm{P} (\mathrm{X} = \mathrm{x} | \mathrm{U} = \mathrm{u} , \underline {{Z}} = \underline {{z}} , \mathrm{A} = \mathrm{a} _ {i}) \cdot \mathrm{P} (\mathrm{U} = \mathrm{u} | \underline {{Z}} = \underline {{z}} , \mathrm{A} = \mathrm{a} _ {i}) \cdot \mathrm{P} (\mathrm{A} = \mathrm{a} _ {i} | \underline {{W}} = \underline {{w}})}. \end{array}
$$

Since $\mathrm{P}(\mathrm{U} = \mathrm{u}|\mathrm{X} = \mathrm{x},Z = z,\mathrm{A} = \mathrm{a}_i)\cdot \mathrm{P}(\mathrm{X} = \mathrm{x}|Z = z,\mathrm{A} = \mathrm{a}_i) = \mathrm{P}(\mathrm{X} = \mathrm{x}|\mathrm{U} = \mathrm{u},Z = z,\mathrm{A} = \mathrm{a}_i)\cdot \mathrm{P}(\mathrm{U} = \mathrm{u}|Z = z,\mathrm{A} = \mathrm{a}_i)\forall i$ , the posterior probability evaluates to the same irrespective of whether U or X is observed first.

$= a_{i}) \forall i$ , the posterior probability evaluates to the same irrespective of whether U or X is observed first. The invariance of the belief revision process to the order in which evidence is assimilated is very desirable. This overcomes what has been a common problem in many heuristic approaches to belief revision (notably the Certainty Factors calculus in traditional rule-based expert system) [8].

## 4.3. Undo and redo the effect of assimilated evidence

The belief revision procedure is very robust and can easily handle situations where the user may want to undo the effect of one or more observed pieces of evidence, or, change the value of an observed variable. Consider the situation where a piece of information was considered to be known and assimilated by the system, and is subsequently found to be not known. This may be due to a mistaken observation, or a test result that is invalidated for some reason. The effect of such an observation can be undone without having to perform the belief revision process from scratch.

Let the set of observed attributes be $W \cup X$ , and let Z indicate the observed attributes which belong to the same compound attribute as X. We first examine the case where we need to undo the effect of evidence X. What we have at this point are the probabilities $P(A = a_{i}|X = x, W = w)$ for each value of i, and what we wish to obtain is the vector of probabilities $P(A = a_{i}|W = w)$ . From Eq. (2) in Appendix B, we have:

$$
\mathrm{P} \left(\mathrm{A} = \mathrm{a} _ {i} | W = w\right) = \frac {\mathrm{P} \left(\mathrm{A} = \mathrm{a} _ {i} | \mathrm{X} = \mathrm{x} , W = w\right)}{\mathrm{P} \left(\mathrm{X} = \mathrm{x} | Z = z , \mathrm{A} = \mathrm{a} _ {i}\right)} \cdot \mathrm{P} (\mathrm{X} = \mathrm{x} | W = w) \forall i.
$$

Since $P(X = x|W = w)$ does not depend on i, we need to evaluate the expression $\frac{P(A = a_{i}|X = x,W = w)}{P(X = x|Z = z,A = a_{i})}$ for each i, and then normalize these terms to obtain the desired probabilities. The term $P(X = x|Z = z,A = a_{i})$ is easily evaluated. When $Z = \phi$ , then the term $P(X = x|A = a_{i})$ is used in the denominator of the above expression.

Next, consider the case when the value of attribute X is being changed (e.g. from $x_{1}$ to $x_{2}$ ). The change may be viewed as comprising of two steps; first undoing the effect of $X = x_{1}$ , and then adding a new piece of evidence $X = x_{2}$ . As a result, we have:

$$
\begin{array}{r l} \mathrm{P} (\mathrm{A} = \mathrm{a} _ {i} | \mathrm{X} = \mathrm{x} _ {2}, W = w) & = \frac {\mathrm{P} (\mathrm{X} = \mathrm{x} _ {2} | Z = z , \mathrm{A} = \mathrm{a} _ {i})}{\mathrm{P} (\mathrm{X} = \mathrm{x} _ {2} | W = w)} \cdot \mathrm{P} (\mathrm{A} = \mathrm{a} _ {i} | W = w) \\ & = \frac {\mathrm{P} (\mathrm{X} = \mathrm{x} _ {2} | Z = z , \mathrm{A} = \mathrm{a} _ {i})}{\mathrm{P} (\mathrm{X} = \mathrm{x} _ {2} | W = w)} \cdot \frac {\mathrm{P} (\mathrm{A} = \mathrm{a} _ {i} | \mathrm{X} = \mathrm{x} _ {1} , W = w)}{\mathrm{P} (\mathrm{X} = \mathrm{x} _ {1} | Z = z , \mathrm{A} = \mathrm{a} _ {i})} \cdot \mathrm{P} (\mathrm{X} = \mathrm{x} _ {1} | W = w) \\ & = \frac {\mathrm{P} (\mathrm{X} = \mathrm{x} _ {2} | Z = z , \mathrm{A} = \mathrm{a} _ {i})}{\mathrm{P} (\mathrm{X} = \mathrm{x} _ {1} | Z = z , \mathrm{A} = \mathrm{a} _ {i})} \cdot \mathrm{P} (\mathrm{A} = \mathrm{a} _ {i} | \mathrm{X} = \mathrm{x} _ {1}, W = w) \cdot \frac {\mathrm{P} (\mathrm{X} = \mathrm{x} _ {2} | W = w)}{\mathrm{P} (\mathrm{X} = \mathrm{x} _ {1} | W = w)}. \end{array}
$$

The term $\frac{\mathrm{P}\left(\mathrm{X} = \mathrm{x}_2|W = w\right)}{\mathrm{P}\left(\mathrm{X} = \mathrm{x}_1|W = w\right)}$ is constant for all $i$ and serves as the normalization factor. Thus, the expression $\frac{\mathrm{P}\left(\mathrm{X} = \mathrm{x}_2|Z = z,\mathrm{A} = \mathrm{a}_i\right)}{\mathrm{P}\left(\mathrm{X} = \mathrm{x}_1|Z = z,\mathrm{A} = \mathrm{a}_i\right)}\cdot \mathrm{P}(\mathrm{A} = \mathrm{a}_i|\mathrm{X} = \mathrm{x}_1,W = w)$ needs to be evaluated for all $i$ and the results normalized in order to obtain the correct posterior probabilities. The probability terms required to perform this update involves just the compound attribute to which X belongs, and the associated time complexity is of order $\mathrm{O}(\mathbf{c}\cdot +r\cdot \mathbf{b})$ . The above procedure is not restricted to the most recently acquired piece of information and is applicable for any assimilated evidence.

## 5. Information gathering strategy for evaluating new problem instances

The previous analysis lays the groundwork for the information gathering strategy for probabilistic reasoning systems. In Section 5.1, we present a completely general information gathering strategy based on information theoretic considerations. We discuss how the system can measure the predictive information content of an attribute whose value is not known, and use this measure to determine which piece of information to obtain next at an intermediate stage of the information gathering process. When benefits and losses associated with different outcomes are available, a decision theoretic approach can be adopted to design the information gathering strategy. This approach is developed in Section 5.2.

## 5.1. Selecting the next piece of information based on information theoretic considerations

When a new case is to be evaluated, there is often a considerable amount of uncertainty associated with the different feasible outcome states. A decision maker examines evidence that is predictive about the outcome in order to reduce the uncertainty about the outcome state. For example, the fact sheet and financial statement supplied by a vendor does not contain many items of information that could potentially reduce the risk of placing orders with the vendor. As discussed in Section 2, the decision maker could choose to obtain additional information from one of many external references, make a site visit to observe the production capacity of the vendor, perform a detailed analysis of the vendor's financial statements for multiple years, etc. From an information theoretic perspective, the piece of information that is most useful at an intermediate stage of the decision making process is the one that most significantly reduces, at that juncture of the decision making process, the uncertainty associated with the different outcome states. The entropy function has been shown to demonstrate desirable properties as a measure of uncertainty for events with probabilistic outcomes [20]. For discrete distributions, the entropy function is the highest when all outcomes are equally likely, and zero when one outcome is known to be true with certainty (the probability of that outcome is one, and all other outcomes have zero probability). For the above reasons, we consider the choice of the information item to obtain next as the one that results, on average, in the greatest decrease in the entropy function. Thus, if item $X_{1}$ reduces the entropy by a larger amount than does item $X_{2}$ (on average), then $X_{1}$ is considered to convey more information about the outcome than item $X_{2}$ . The entropy function H(A) for outcome A, and, the information I(A;X) conveyed by an attribute X about the outcome A, are mathematically expressed as follows [3]:

$$
\mathrm{H} (\mathrm{A}) = - \sum_ {i} \mathrm{P} (\mathrm{A} = \mathrm{a} _ {i}) \log \mathrm{P} (\mathrm{A} = \mathrm{a} _ {i}),
$$

$$
\mathrm{I} (\mathrm{A}; \mathrm{X}) = \sum_ {j} \mathrm{P} (\mathrm{X} = \mathrm{x} _ {j}) \cdot \mathrm{H} (\mathrm{A} | \mathrm{X} = \mathrm{x} _ {j}) = \sum_ {j} \sum_ {i} \mathrm{P} (\mathrm{A} = \mathrm{a} _ {i}, \mathrm{X} = \mathrm{x} _ {j}) \frac {\log \mathrm{P} (\mathrm{A} = \mathrm{a} _ {\mathrm{i}} , \mathrm{X} = \mathrm{x} _ {j})}{\mathrm{P} (\mathrm{A} = \mathrm{a} _ {i}) \cdot \mathrm{P} (\mathrm{X} = \mathrm{x} _ {j})}.
$$

The information I(A;X) is also called the mutual information across A and X, and is bounded by H(A). When the attribute X completely specifies A, then I(A;X) = H(A). If X does not convey any information whatsoever about A then I(A;X) = 0, which usually implies independence between A and X.

The expression for mutual information as stated above indicates the amount of information conveyed by attribute X about the outcome A, when no other information is available. When evidence is gathered and evaluated in a sequential manner, then we wish to identify that piece of information which is most informative about the outcome A, at an intermediate stage of the information gathering process (i.e., we wish to obtain that piece of information next which is the most discriminating, given the current state of information). Thus, if the set of variables W has already been observed, then we are interested in the additional information conveyed by an unknown variable X about the outcome A, given the fact that W = w. The mutual information between A and X, conditioned on W = w, is as shown below:

$$
\operatorname{I} \bigl (\mathrm{A}; \mathrm{X} | W = w \bigr) = \sum_ {j} \sum_ {i} \mathrm{P} \Bigl (\mathrm{A} = \mathrm{a} _ {i}, \mathrm{X} = \mathrm{x} _ {j} | W = w \Bigr) \frac {\log \mathrm{P} \bigl (\mathrm{A} = \mathrm{a} _ {\mathrm{i}} , \mathrm{X} = \mathrm{x} _ {j} | W = w \bigr)}{\mathrm{P} \bigl (\mathrm{A} = \mathrm{a} _ {i} | W = w \bigr) \cdot \mathrm{P} \bigl (\mathrm{X} = \mathrm{x} _ {j} | W = w \bigr)}.
$$

Once again, conditional independence properties across compound attributes makes this expression tractable. Procedures for the two cases discussed in Section 4.1 are presented below:

Case I: The new piece of information, X, is the only component of a compound attribute, or, is one of multiple components of a compound attribute, none of which have been observed yet.

This is the case where the attribute X is conditionally independent of W with respect to A. We show, in Appendix D, the following:

$$
\mathrm{I} (\mathrm{A}; \mathrm{X} | W = w) = \sum_ {j} \sum_ {i} \mathrm{P} \left(\mathrm{X} = \mathrm{x} _ {j} | \mathrm{A} = \mathrm{a} _ {i}\right) \cdot \mathrm{P} \left(\mathrm{A} = \mathrm{a} _ {i} | W = w\right) \log \frac {\mathrm{P} \left(\mathrm{X} = \mathrm{x} _ {j} | \mathrm{A} = \mathrm{a} _ {i}\right)}{\sum_ {i} \mathrm{P} \left(\mathrm{X} = \mathrm{x} _ {j} | \mathrm{A} = \mathrm{a} _ {i}\right) \cdot \mathrm{P} \left(\mathrm{A} = \mathrm{a} _ {i} | W = w\right)}.
$$

Therefore, to evaluate $\mathrm{I}(\mathrm{A};\mathrm{X}|W = w)$ , we need the following: (i) $\mathrm{P}(\mathrm{A} = \mathrm{a}_i|W = w)$ for all $i$ ; and (ii) $\mathrm{P}(\mathrm{X} = \mathrm{x}_j|\mathrm{A} = \mathrm{a}_i)$ for all $i,j$ . $\mathrm{P}(\mathrm{A} = \mathrm{a}_i|W = w)$ is already available when this analysis is to be performed. As discussed in Section 4.1, $\mathrm{P}(\mathrm{X} = \mathrm{x}_j|\mathrm{A} = \mathrm{a}_i)$ can be easily estimated from sample data.

Case II: The new piece of information, X, is one of multiple components of a compound attribute, some of which have already been observed. Here, X is part of a compound attribute $Y_{i}$ , and Z = z is the set of variables which are part of $Y_{i}$ that have already been observed. In this case we have (proof in Appendix D):

$$
\begin{array}{l} \mathrm{P} \left(\mathrm{A} = \mathrm{a} _ {i}, \mathrm{X} = \mathrm{x} _ {j} | W = w\right) \\ = \sum_ {j} \sum_ {i} \mathrm{P} \left(\mathrm{X} = \mathrm{x} _ {j} | \mathrm{A} = \mathrm{a} _ {i}, Z = z\right) \cdot \mathrm{P} \left(\mathrm{A} = \mathrm{a} _ {i} | W = w\right) \log \frac {\mathrm{P} \left(\mathrm{X} = \mathrm{x} _ {j} | \mathrm{A} = \mathrm{a} _ {i} , Z = z\right)}{\sum_ {i} \mathrm{P} \left(\mathrm{X} = \mathrm{x} _ {j} | \mathrm{A} = \mathrm{a} _ {i} , Z = z\right) \cdot \mathrm{P} \left(\mathrm{A} = \mathrm{a} _ {i} | W = w\right)}. \end{array}
$$

As in Case I, $P(A = a_{i}|W = w)$ is already available when this analysis is to be performed. The expression $P(X = x_{j}|A = a_{i}, Z = z)$ remains to be evaluated from the historical cases. This expression is dependent only on the subset Z of the realized variables.

The mutual information associated with unknown attributes can be efficiently evaluated. The expression for Case II shows that for any such attribute X, we need to estimate $P(X = x_{j}|A = a_{i}, Z = z)$ for all i and j, and then evaluate $I(A; X|W = w)$ . Estimating $P(X = x_{j}|A = a_{i}, Z = z)$ from the historical data requires determining the frequency of the occurrences of $(X = x_{j}, A = a_{i}, Z = z)$ for all i and j, which can be accomplished in one examination of the data file. The maximum number of comparisons required will be of the order $O(c \cdot (d + 1))$ , where c is the total number of cases, and d is the maximum number of simple attributes in any compound attribute. The computational requirement for evaluating $I(A; X|W = w)$ once the probability estimates are available is of the order $O(b^{2})$ , where b is the maximum number of states that any indexing or outcome variable can have. The computational complexity is lower when Case I is applicable. Therefore, the overall complexity of evaluating $I(A; X|W = w)$ is bounded by $O(c \cdot (d + 1) + b^{2})$ . Since there are at most n attributes for which this analysis is required, the worst case complexity is $O(n \cdot c \cdot (d + 1) + n \cdot b^{2})$ .

## 5.1.1. Stopping rule

The primary objective of obtaining new information is to reduce uncertainty about the outcome states. Therefore, as long as new pieces of information can significantly reduce this uncertainty, they should be considered. When that is no longer the case, observing additional attribute values will usually be uninformative. Therefore, if none of the remaining unobserved attributes are significantly informative, then the information gathering process should halt, and the system will make a recommendation based on the current set of beliefs. A statistical significance test based on the likelihood-ratio test can be used to determine when new information is not worth pursuing [1]. According to this test, a new piece of information X is statistically significant at a level $\alpha$ if $I(A;X|W=w) > \frac{\aleph^{2}(\alpha,d)}{2 \cdot s}$ , where s is the number of cases that are used to estimate $I(A;X|W=w)$ , and $\aleph^{2}(\alpha,d)$ is the Chi-square statistic at significance level $\alpha$ and d degrees of freedom associated with the test. An alternate rule of thumb would be to assign certain threshold values for probabilities associated with different outcome states. Whenever the threshold is crossed for any one of the outcome states, the system would make a recommendation based on the information available.

## 5.2. Selecting the next piece of information based on decision theoretic considerations

In the problem of evaluating new vendors, it was felt that the benefits (or losses) were different for different outcomes. When an approved vendor was unable to deliver as required, then the company could end up incurring substantial additional costs to procure the product from other vendors within a short time frame. This phenomenon of asymmetric costs and benefits associated with different outcomes is true for many other application domains as well. In such situations, the gains from obtaining a new piece of evidence can be evaluated in terms of the expected additional value associated with a decision made with the new information. Since probability measures are used to evaluate new problem instances, traditional decision theoretic techniques can be readily used to evaluate the expected value of new information $[9,13–15]$ .

Let $V_{ij}$ be the value associated with a true outcome i when state j is predicted. Typically, this value will be positive when i = j, and is negative when $i \neq j$ . Further, let W = w be the set of variables already observed. The expected value of making a prediction $A = a_j$ without obtaining more information is:

$$
\operatorname{EV} \left(\mathrm{A} = \mathrm{a} _ {j}; W = w\right) = \sum_ {i} \mathrm{P} \left(\mathrm{A} = \mathrm{a} _ {i} | W = w\right) \cdot \mathrm{V} _ {i j}.
$$

The best prediction is one that maximizes the associated expected value. Therefore, the best decision is:

$$
\mathrm{EV} ^ {*} (\mathrm{A}; W = w) = \operatorname{Max} _ {j} \left\{\sum_ {i} \mathrm{P} \left(\mathrm{A} = a _ {i} | W = w\right) \cdot \mathrm{V} _ {i j} \right\}.
$$

If a new variable X is observed to have the value $x_{r}$ , the probabilities associated with the different outcome states are easily obtained using the procedure outlined in Section 4.1. The expected value of making a decision with this information is:

$$
\mathrm{EV} ^ {*} (A; W = w, X = x _ {r}) = \operatorname{Max} _ {j} \left\{\sum_ {i} P (A = a _ {i} | W = w, X = x _ {r}) \cdot V _ {i j} \right\}.
$$

Now, consider the situation where the variable X has not yet been observed, and is being considered as a piece of information to obtain next. The expected value of making a decision after observing X is obtained by evaluating the weighted average of the expected value of observing $X = x_{r}$ for all feasible values of r. The weights to be used are the probabilities associated with observing each value of X under the current state of information (i.e., $P(X = x_{r} | W = w)$ ). Therefore:

$$
\mathrm{EV} ^ {*} (\mathrm{A}; W = w, \mathrm{X}) = \sum_ {r} \mathrm{P} (\mathrm{X} = \mathrm{x} _ {r} | W = w) \cdot \left[ \operatorname{Max} _ {j} \left\{\sum_ {i} \mathrm{P} (\mathrm{A} = \mathrm{a} _ {i} | W = w, \mathrm{X} = \mathrm{x} _ {r}) \cdot \mathrm{V} _ {i j} \right\} \right],
$$

where $\mathrm{P}(\mathrm{X}=\mathrm{x}_{r}|W=w)=\sum_{i}\mathrm{P}(\mathrm{X}=\mathrm{x}_{r}|Z_{\mathrm{x}}=z_{\mathrm{x}},\mathrm{A}=\mathrm{a}_{i})\cdot\mathrm{P}(\mathrm{A}=\mathrm{a}_{i}|W=w)$ and $Z_{x}$ is the set of variables which belong to the same compound attribute as X and have already been observed.

The net benefit of observing X is:

$$
\operatorname{GAIN} (X; W = w) = \operatorname{EV} ^ {*} (A; W = w, X) - \operatorname{EV} ^ {*} (A; W = w).
$$

The above analysis shows that the expected gains from observing a new piece of evidence can be easily evaluated at any stage of the information gathering process if reliable estimates are available for $V_{ij}$ . This analysis can be performed for each unseen variable, and the variable that leads to the maximum gain is identified as the one to observe next. Computationally, this procedure is also quite efficient. Evaluating $EV^{*}(A;W=w)$ is of order $O(b^{2})$ . Evaluating $P(A=a_{i}|W=w,X=x_{r})$ for all feasible values of i and r is of the order $O(c\cdot(d+1))$ , and evaluating $P(X=x_{r}|W=w)$ is of the order $O(c\cdot d\cdot(d+1))$ . Once these probabilities are estimated, evaluating $EV^{*}(A;W=w,X)$ requires additional computations of the order $O(b^{3})$ . Therefore, the overall worst case complexity for identifying the variable that leads to the maximum gain is of the order $O(n\cdot c\cdot(d+1)+n\cdot c\cdot d\cdot(d+1)+n\cdot b^{3}+n\cdot b^{2})\sim O(n\cdot c\cdot d\cdot(d+1)+n\cdot b^{3})$ .

In some situations, there are significant costs associated with obtaining new information. Further, these costs may differ widely among different information items. For instance, performing a site visit to ensure that a vendor has adequate production facilities is much more time consuming and expensive than obtaining references by phone from prior customers of the vendor. In such situations, we can also incorporate the cost of acquiring evidence when examining which piece of evidence to acquire next. The system must be provided with the GAIN(A;X|W=w)

expected cost of obtaining each new piece of information, and the gain per unit cost, $\frac{\text{GAIN}(A; X|W = w)}{C(X)}$ , can be used to identify the information item to be acquired next. A natural stopping rule in this case is when the expected gains is less than the expected costs of acquiring new information, i.e., $\operatorname{Max}_X\left\{\frac{\operatorname{GAIN}(A; X|W = w)}{C(X)}\right\} \leq 1$ .

The cost of obtaining new information can be used even when dollar values for benefits and losses associated with different predictions are not available (i.e., when the GAIN function cannot be evaluated). In that case, the system must evaluate which of the unknown variables provides the largest amount of information about the outcome variable per unit cost. The expression $I(A;X|W=w)$ is evaluated for each evidence under consideration, and then the ratio $\frac{I(A;X|W=w)}{C(X)}$ is used to rank the available items.

## 5.3. The control strategy algorithm

The information gathering and evaluation strategy based on the information theoretic technique presented in Section 5.1 is shown below.

Algorithm

Initialize $W = \phi$

```txt
While Stopping Rule is not met do
    Determine I(A;U|W = w) for all U ∈ X - W
    Select U* that maximizes {I(A;U|W = w)}
    If U* is significant Then do
    Ask user to provide the value of U*
    Revise P(A|U*,W)
    Set W = U* ∪ W
    If (U* is not significant) OR (X - W = φ) then recommend solution
End While
```

The algorithm can be easily modified to incorporate the gain function and costs, in order to use the appropriate control strategy. We note that the procedure outlined is greedy in nature in that it evaluates pieces of information one at a time. It is possible that a collection of s information items taken together may be more predictive than any other set of s attributes. However, when considered individually, an attribute that is not in the best set may evaluate as most informative. The above algorithm can be further modified to consider sets of variables at each information gathering stage. For that case, the computational effort associated with identifying the next set of attributes to observe would increase at a rate that is exponential to the size of the sets being considered. Therefore, the procedure would be feasible when the number of variables being considered in each set are reasonably low. When response times are stringent, or computational resources are limited, evaluating information items individually would be appropriate.

## 6. Discussion

In many decision making scenarios, the reasoning process must deal with uncertainty inherent in the problem domain, and, data must be gathered and assimilated in a sequential manner to arrive at a final decision. This research addresses the formulation of a probabilistic scheme for such applications. The probabilistic model is validated by testing its performance on simulated data, and shown to work well when a reasonably large number of cases are available for estimating probabilities. When reasoning under uncertain conditions, an important aspect of expert human behavior is the ability to gather and assimilate new information in an efficient manner, based on the currently available information. We have shown how the probabilistic scheme can modify beliefs regarding the outcome states when information is presented to it in an incremental fashion. The use of probability measures leads to information gathering strategies based on sound theoretic principles. We have presented two schemes that allow evaluation of each potential new piece of information, in order to recommend which evidence should be observed next. The first is based on information theoretic principles, where the system will recommend that information item which is most predictive about the outcome for a given situation. The second is based on decision theoretic analysis, and identifies that information item which leads to the most gain, i.e. the most increase in expected value of making a prediction. In either case, the system is very flexible in that the user is not bound to obtain the information that is recommended in order to further examine a new case. Irrespective of the user's actions, the system is able to revise the beliefs in the different outcome states and provide guidance for the next piece of information to be obtained. All of the evaluation and belief revision techniques are shown to be efficient and can be easily applied in practice.

The choice of which strategy to use for a given application will be largely dictated by the availability of reliable estimates for benefits and losses associated with making correct and incorrect specifications, and costs associated with acquiring evidence. When such values are available, the decision theoretic technique will be more appropriate. However, in some applications, users are not able to assign' dollar values' to the different benefits and losses in a reliable manner [12]. In addition, different users of such a system may have different assessments for these values. For example, a loan officer who is trying to maximize the loan amount generated for a given period may assign a low loss amount for misclassifying an applicant with poor credit rating as having a good rating. On the other hand, the manager of a bank who may be ultimately responsible for recovering these loans at a future date may assign a much higher loss amount to such a misclassification. Further, the loss amount may depend on the amount of loan applied for, and will be different from one case to the next. When reliable estimates are not available for these values, the information theoretic analysis is appropriate.

A limitation of the technique we have presented is that it requires all attribute values to be available in discrete form. As a result, attribute values of a continuous nature are converted into discrete data. This, of course, leads to loss of some amount of information when evaluating new cases. In principle, it is possible to convert data of a continuous nature into a large number of categories to minimize this loss of information $[19,21,23]$ . In practice, this requires a large number of historical cases to provide accurate probability estimates. It is recommended that designers of such systems compare the loss of information that result from coarse categories with the difficulty in obtaining robust probability estimates when a finer categorization is used in order to arrive at the desired level of granularity. When all of the predictive data items are continuous in nature, and demonstrate (approximate) multivariate normality, then the well-known discriminant analysis can be used to make robust predictions $[10]$ . We should emphasize that such an analysis does not readily allow users to formally evaluate the value of new information, and is therefore not appropriate for applications where data acquisition is sequential in nature.

## Acknowledgements

We wish to thank the Guest Editors Arun Sen and Ajay Vinze and the anonymous referees for their constructive comments and suggestions which greatly improved the quality of the paper. This research was partly funded by the Council on Research of Louisiana State University and the College of Business Administration at Louisiana State University.

## Appendix A

$$
\begin{array}{r l} & \mathrm {P(Ability = 'Good'|Ratio = 'Good'\& ISO 9000 = 'True')} \\ & = \frac {\mathrm {P(TRatio = 'Good' & ISO 9000 = 'True'|Ability = 'Good')\cdot P(Ability = 'Good')}}{\mathrm {P(TRatio = 'Good' & ISO 9000 = 'True')}} \\ & = \frac {\mathrm {P(TRatio = 'Good'|Ability = 'Good')\cdot P(ISO 9000 = 'True'|Ability = 'Good')\cdot P(Ability = 'Good')}}{\mathrm {P(TRatio = 'Good' & ISO 9000 = 'True')}} \end{array}
$$

(follows from the conditional independence property).

Similarly, we have:

$$
\begin{array}{r l} & \mathrm {P(Ability = 'Poor'|TRatio = 'Good' \& ISO 9000 = 'True')} \\ & = \frac {\mathrm {P(TRatio = 'Good'|Ability = 'Poor')\cdot P(ISO 9000 = 'True'|Ability = 'Poor')\cdot P(Ability = 'Poor')}}{\mathrm {P(TRatio = 'Good' \& ISO 9000 = 'True')}}. \end{array}
$$

The denominator is the same in the above expressions and is the sum of the numerators of the two expressions. Representing this term by K, we get:

$$
\begin{array}{r l} & \mathrm {P(Ability = `Good' | TRatio = `Good' \& ISO 9000 = `True'}) \\ & \quad = \frac {1}{K} \cdot P (TRatio = `Good' |Ability = `Good') \cdot P (ISO 9000 = `True' |Ability = `Good') \cdot P (Ability = `Good') \end{array}
$$

and

$$
\begin{array}{r l} & \mathrm {P(Ability = 'Poor'|TRatio = 'Good' \& ISO 9000 = 'True'}) \\ & = \frac {1}{K} \cdot \mathrm {P(TRatio = 'Good'|Ability = 'Poor')\cdot P(ISO 9000 = 'True'|Ability = 'Poor')\cdot P(Ability = 'Poor').} \end{array}
$$

## Appendix B

Case I: The new piece of information, X, is the only component of a compound attribute, or, is one of multiple components of a compound attribute, none of which have been observed yet.

Consider the situation where X is the only component of a compound attribute. It then follows that:

$$
\begin{array}{r l} \mathrm{P(A=a_i|X=x,W=w)} & = \frac {\mathrm{P(X=x,W=w|A=a_i)} \cdot \mathrm{P(A=a_i)}}{\mathrm{P(X=x,W=w)}} \\ & = \frac {\mathrm{P(X=x|A=a_i)} \cdot \mathrm{P(W=w|A=a_i)} \cdot \mathrm{P(A=a_i)}}{\mathrm{P(X=x|W=w)} \cdot \mathrm{P(W=w)}} \\ & = \frac {\mathrm{P(X=x|A=a_i)}}{\mathrm{P(X=x|W=w)}} \cdot \mathrm{P(A=a_i|W=w)} \forall i. \end{array}\tag{1}
$$

An identical procedure is used to revise beliefs when the new piece of information, X, is one of multiple components of a compound attribute, none of which have been observed.

Case II: The new piece of information, X, is one of multiple components of a compound attribute, some of which have already been observed.

In this case, X is part of a compound attribute $Y_{i}$ , and one or more other components of $Y_{i}$ have already been observed. Z = z is the set of variables that are part of $Y_{i}$ and have been observed, and, $W' = w'$ are the other observed variables (i.e., $Z \cup W' = W$ ). Then:

$$
\begin{array}{r l} \mathrm{P(A=a_i|X=x,W=w)} & = \frac {\mathrm{P(X=x,W=w|A=a_i)} \cdot \mathrm{P(A=a_i)}}{\mathrm{P(X=x,W=w)}} \\ & = \frac {\mathrm{P(X=x,Z=z,W' = w'|A=a_i)} \cdot \mathrm{P(A=a_i)}}{\mathrm{P(X=x,W=w)}} \\ & = \frac {\mathrm{P(X=x,Z=z|A=a_i)} \cdot \mathrm{P(W' = w'|A=a_i)} \cdot \mathrm{P(A=a_i)}}{\mathrm{P(X=x,W=w)}} \\ & = \frac {\mathrm{P(X=x|Z=z,A=a_i)} \cdot \mathrm{P(Z=z,W' = w'|A=a_i)} \cdot \mathrm{P(A=a_i)}}{\mathrm{P(X=x,W=w)}} \end{array}
$$

$$
\begin{array}{l} = \frac {\mathrm{P} (\mathrm{X} = \mathrm{x} | Z = z , \mathrm{A} = \mathrm{a} _ {i}) \cdot \mathrm{P} (W = w | \mathrm{A} = \mathrm{a} _ {i}) \cdot \mathrm{P} (\mathrm{A} = \mathrm{a} _ {i})}{\mathrm{P} (\mathrm{X} = \mathrm{x} | W = w) \cdot \mathrm{P} (W = w)} \\ = \frac {\mathrm{P} (\mathrm{X} = \mathrm{x} | Z = z , \mathrm{A} = \mathrm{a} _ {i})}{\mathrm{P} (\mathrm{X} = \mathrm{x} | W = w)} \cdot \mathrm{P} (\mathrm{A} = \mathrm{a} _ {i} | W = w) \forall i. \end{array}\tag{2}
$$

## Appendix C

Case I: X and U belong to different compound attributes

X is part of the compound attribute $Y_{X}$ , and $Z_{X}$ is the set of variables that are part of $Y_{X}$ and have been observed. Similarly, U is part of the compound attribute $Y_{U}$ , and $Z_{U}$ is the set of variables that are part of $Y_{U}$ and have been observed. $W' = w'$ is the set of other observed variables (i.e., $Z_{X} \cup Z_{U} \cup W' = W$ ). We derive the expression for the posterior probability for $A = a_{i}$ when X is observed first, followed by U. The derivation for the expression obtained when U is observed first is very similar and is not presented. When X is observed first, we have:

$$
\mathrm{P} \left(\mathrm{A} = \mathrm{a} _ {i} | \mathrm{X} = \mathrm{x}, W = w\right) = \frac {\mathrm{P} \left(\mathrm{X} = \mathrm{x} \mid Z _ {\mathrm{X}} = z _ {\mathrm{X}} , \mathrm{A} = \mathrm{a} _ {i}\right)}{\mathrm{P} (\mathrm{X} = \mathrm{x} \mid W = w)} \cdot \mathrm{P} \left(\mathrm{A} = \mathrm{a} _ {i} \mid W = w\right) \forall i.
$$

After U is observed next, we get:

$$
\mathrm{P} \left(\mathrm{A} = \mathrm{a} _ {i} | U = u, \mathrm{X} = \mathrm{x}, W = w\right) = \frac {\mathrm{P} \left(\mathrm{U} = \mathrm{u} \mid Z _ {\mathrm{U}} = z _ {\mathrm{U}} , \mathrm{A} = \mathrm{a} _ {i}\right)}{\mathrm{P} \left(\mathrm{U} = \mathrm{u} \mid \mathrm{X} = \mathrm{x} , W = w\right)} \cdot \mathrm{P} \left(\mathrm{A} = \mathrm{a} _ {i} \mid \mathrm{X} = \mathrm{x}, W = w\right)
$$

since $(\mathrm{U},Z_{\mathrm{U}})$ is conditionally independent of $(\mathrm{X},Z_{\mathrm{X}},W^{\prime})$ given A, the above follows from (1).

$$
\mathrm{Now} \mathrm{P(U=u|X=x,W=w)=} \Sigma i \mathrm{P(U=u,A=a} _ {i} | \mathrm{X=x,Z=z})
$$

$$
\begin{array}{l} = \Sigma_ {i} \mathrm{P} \big (\mathrm{U} = \mathrm{u} | \mathrm{X} = \mathrm{x}, Z _ {\mathrm{X}} = z _ {\mathrm{X}}, Z _ {\mathrm{U}} = z _ {\mathrm{U}}, W ^ {\prime} = w ^ {\prime}, \mathrm{A} = \mathrm{a} _ {i} \big) \cdot \mathrm{P} \big (\mathrm{A} = \mathrm{a} _ {i} | \mathrm{X} = \mathrm{x}, Z _ {\mathrm{x}} = z _ {\mathrm{X}}, Z _ {\mathrm{U}} = z _ {\mathrm{U}}, W ^ {\prime} = w ^ {\prime} \big), \\ = \Sigma_ {i} \mathrm{P} \big (\mathrm{U} = \mathrm{u} | Z _ {\mathrm{U}} = z _ {\mathrm{U}}, \mathrm{A} = \mathrm{a} _ {i} \big) \cdot \mathrm{P} \big (\mathrm{A} = \mathrm{a} _ {i} | \mathrm{X} = \mathrm{x}, W = w \big), \\ = \Sigma_ {i} \mathrm{P} \big (\mathrm{U} = \mathrm{u} | Z _ {\mathrm{U}} = z _ {\mathrm{U}}, \mathrm{A} = \mathrm{a} _ {i} \big) \cdot \frac {\mathrm{P} \big (\mathrm{X} = \mathrm{x} | Z _ {\mathrm{X}} = z _ {\mathrm{X}} , \mathrm{A} = \mathrm{a} _ {i} \big)}{\mathrm{P} (\mathrm{X} = \mathrm{x} | W = w)} \cdot \mathrm{P} \big (\mathrm{A} = \mathrm{a} _ {i} | W = w \big). \end{array}
$$

Therefore:

$$
\begin{array}{l} \mathrm {P(A = a_ {i} |U = u,X = x,W = w)} \\ = \frac {\mathrm {P(U = u|Z_ {U} = z_ {U} ,A = a_ {i})\cdot \frac {P(X = x|Z_ {X} = z_ {X} ,A = a_ {i})}{P(X = x|W = w)} \cdot P(A = a_ {i} |W = w)}}{\Sigma_ {i} P(U = u|Z_ {U} = z_ {U} ,A = a_ {i}) \cdot \frac {P(X = x|Z_ {X} = z_ {X} ,A = a_ {i})}{P(X = x|W = w)} \cdot P(A = a_ {i} |W = w)}. \end{array}
$$

$P(X = x|W = w)$ does not depend on i and is therefore a constant term in the denominator of the above expression. Hence:

$$
\mathrm{P} \left(\mathrm{A} = \mathrm{a} _ {i} | \mathrm{U} = \mathrm{u}, \mathrm{X} = \mathrm{x}, W = w\right) = \frac {\mathrm{P} \left(\mathrm{U} = \mathrm{u} \mid Z _ {\mathrm{U}} = z _ {\mathrm{U}} , \mathrm{A} = \mathrm{a} _ {i}\right) \cdot \mathrm{P} \left(\mathrm{X} = \mathrm{x} \mid Z _ {\mathrm{x}} = z _ {\mathrm{x}} , \mathrm{A} = \mathrm{a} _ {i}\right) \cdot \mathrm{P} \left(\mathrm{A} = \mathrm{a} _ {i} \mid W = w\right)}{\sum_ {i} \mathrm{P} \left(\mathrm{U} = \mathrm{u} \mid Z _ {\mathrm{U}} = z _ {\mathrm{U}} , \mathrm{A} = \mathrm{a} _ {i}\right) \cdot \mathrm{P} \left(\mathrm{X} = \mathrm{x} \mid Z _ {\mathrm{x}} = z _ {\mathrm{x}} , \mathrm{A} = \mathrm{a} _ {\mathrm{i}}\right) \cdot \mathrm{P} \left(\mathrm{A} = \mathrm{a} _ {i} \mid W = w\right)}.
$$

Case II: Both $X$ and $U$ belong to the same compound attribute

Here, X and U belong to the compound attribute $Y_{i}$ , and Z = z is the set of variables that are part of $Y_{i}$ and have been observed. $W' = w'$ is the set of other observed variables (i.e., $Z \cup W' = W$ ). When X is observed first, we have:

$$
\mathrm{P} \left(\mathrm{A} = \mathrm{a} _ {i} | \mathrm{X} = \mathrm{x}, W = w\right) = \frac {\mathrm{P} \left(\mathrm{X} = \mathrm{x} | Z = z , \mathrm{A} = \mathrm{a} _ {i}\right)}{\mathrm{P} \left(\mathrm{X} = \mathrm{x} | W = w\right)} \cdot \mathrm{P} \left(\mathrm{A} = \mathrm{a} _ {i} | W = w\right) \forall i.
$$

When U is subsequently used to revise the belief in A, we have:

$$
\mathrm{P} \left(\mathrm{A} = \mathrm{a} _ {i} | \mathrm{U} = \mathrm{u}, \mathrm{X} = \mathrm{x}, W = w\right) = \frac {\mathrm{P} \left(\mathrm{U} = \mathrm{u} | \mathrm{X} = \mathrm{x} , Z = z , \mathrm{A} = \mathrm{a} _ {i}\right)}{\mathrm{P} \left(\mathrm{U} = \mathrm{u} | \mathrm{X} = \mathrm{x} , W = w\right)} \cdot \mathrm{P} \left(\mathrm{A} = \mathrm{a} _ {i} | \mathrm{X} = \mathrm{x}, W = w\right) \left\{\text {follows from (2)} \right\}.
$$

Now $\mathrm{P(U = u|X = x,W = w) = \Sigma_i P(U = u,A = a_i|X = x,Z = z)}$

$$
\begin{array}{l} = \Sigma_ {i} \mathrm{P} \big (\mathrm{U} = \mathrm{u} | \mathrm{X} = \mathrm{x}, Z = \mathrm{z}, W ^ {\prime} = w ^ {\prime}, \mathrm{A} = \mathrm{a} _ {i} \big) \cdot \mathrm{P} \big (\mathrm{A} = \mathrm{a} _ {i} | \mathrm{X} = \mathrm{x}, Z = z, W ^ {\prime} = w ^ {\prime} \big), \\ = \Sigma_ {i} \mathrm{P} \big (\mathrm{U} = \mathrm{u} | \mathrm{X} = \mathrm{x}, Z = z, \mathrm{A} = \mathrm{a} _ {i} \big) \cdot \mathrm{P} \big (\mathrm{A} = \mathrm{a} _ {i} | \mathrm{X} = \mathrm{x}, Z = z, W ^ {\prime} = w ^ {\prime} \big), \\ = \Sigma_ {i} \mathrm{P} \big (\mathrm{U} = \mathrm{u} | \textsf {X} = \textsf {x}, Z = z, \mathrm{A} = \mathrm{a} _ {i} \big) \cdot \frac {\mathrm{P} \big (\textsf {X} = \textsf {x} | Z = z , \mathrm{A} = \mathrm{a} _ {i} \big)}{\mathrm{P} (\textsf {X} = \textsf {x} | W = w)} \cdot \mathrm{P} \big (\mathrm{A} = \mathrm{a} _ {i} | W = w \big). \end{array}
$$

Substituting this expression for $\mathrm{P}(\mathrm{U} = \mathrm{u}|\mathrm{X} = \mathrm{x}, W = w)$ , we get:

$$
\begin{array}{r l} & \mathrm {P(A = a_ {i} |U = u,X = x,W = w)} \\ & = \frac {\mathrm {P(U = u|X = x,Z = z,A = a_ {i})\cdot \frac {P(X = x|Z = z,A = a_ {i})}{P(X = x|W = w)} \cdot P(A = a_ {i} |W = w)}}{\sum_ {i} \mathrm {P(U = u|X = x,Z = z,A = a_ {i})\cdot \frac {P(X = x|Z = z,A = a_ {i})}{P(X = x|W = w)} \cdot P(A = a_ {i} |W = w)}} \\ & = \frac {\mathrm {P(U = u|X = x,Z = z,A = a_ {i})\cdot P(X = x|Z = z,A = a_ {i})\cdot P(A = a_ {i} |W = w)}}{\sum_ {i} \mathrm {P(U = u|X = x,Z = z,A = a_ {i})\cdot P(X = x|Z = z,A = a_ {i})\cdot P(A = a_ {i} |W = w)}.} \end{array}
$$

When U is observed first, we get, in an analogous fashion:

$$
\begin{array}{r l} & \mathrm{P(A=a_i|X=x,U=u,W=w)} \\ & = \frac {\mathrm{P(X=x|U=u,Z=z,A=a_i)} \cdot \mathrm{P(U=u|Z=z,A=a_i)} \cdot \mathrm{P(A=a_i|W=w)}}{\sum_ {i} \mathrm{P(X=x|U=u,Z=z,A=a_i)} \cdot \mathrm{P(U=u|Z=z,A=a_i)} \cdot \mathrm{P(A=a_i|W=w)}}. \end{array}
$$

## Appendix D

Case I: The new piece of information, X, is the only component of a compound attribute, or, is one of multiple components of a compound attribute, none of which have been observed yet.

Here, the attribute X is conditionally independent of W with respect to A. We have:

$$
\begin{array}{r l} \mathrm{I} (\mathrm{A}; \mathrm{X} | W = w) & = \sum_ {j} \sum_ {i} \mathrm{P} (\mathrm{A} = \mathrm{a} _ {i}, \mathrm{X} = \mathrm{x} _ {j} | W = w) \log \frac {\mathrm{P} (\mathrm{A} = \mathrm{a} _ {i} , \mathrm{X} = \mathrm{x} _ {j} | W = w)}{\mathrm{P} (\mathrm{A} = \mathrm{a} _ {i} | W = w) \cdot \mathrm{P} (\mathrm{X} = \mathrm{x} _ {j} | W = w)} \\ & = \sum_ {j} \sum_ {i} \mathrm{P} (\mathrm{X} = \mathrm{x} _ {j} | \mathrm{A} = \mathrm{a} _ {i}) \cdot \mathrm{P} (\mathrm{A} = \mathrm{a} _ {i} | W = w) \log \frac {\mathrm{P} (\mathrm{X} = \mathrm{x} _ {j} | \mathrm{A} = \mathrm{a} _ {i}) \cdot \mathrm{P} (\mathrm{A} = \mathrm{a} _ {i} | W = w)}{\mathrm{P} (\mathrm{A} = \mathrm{a} _ {i} | W = w) \cdot \mathrm{P} (\mathrm{X} = \mathrm{x} _ {j} | W = w)} \end{array}
$$

$$
\begin{array}{l} = \Sigma_ {j} \Sigma_ {i} P (X = x _ {j} | A = a _ {i}) \cdot P (A = a _ {i} | W = w) \log \frac {P (X = x _ {j} | A = a _ {i})}{P (X = x _ {j} | W = w)} \\ = \Sigma_ {j} \Sigma_ {i} P (X = x _ {j} | A = a _ {i}) \cdot P (A = a _ {i} | W = w) \log \frac {P (X = x _ {j} | A = a _ {i})}{\Sigma_ {i} P (X = x _ {j} , A = a _ {i} | W = w)} \\ = \Sigma_ {j} \Sigma_ {i} P (X = x _ {j} | A = a _ {i}) \cdot P (A = a _ {i} | W = w) \log \frac {P (X = x _ {j} | A = a _ {i})}{\Sigma_ {i} P (X = x _ {j} | A = a _ {i}) \cdot P (A = a _ {i} | W = w)}. \end{array}
$$

Case II: The new piece of information, X, is one of multiple components of a compound attribute, some of which have already been observed.

Here, X is part of a compound attribute $Y_{i}$ , and Z = z is the set of variables which are part of $Y_{i}$ that have already been observed. Then:

$$
\begin{array}{r l} \mathrm{P} \big (\mathrm{A} = \mathrm{a} _ {i}, \mathrm{X} = \mathrm{x} _ {j} | W = w \big) & = \mathrm{P} \big (\mathrm{X} = \mathrm{x} _ {j} | \mathrm{A} = \mathrm{a} _ {i}, W = w \big) \cdot \mathrm{P} \big (\mathrm{A} = \mathrm{a} _ {i} | W = w \big) \\ & = \mathrm{P} \big (\mathrm{X} = \mathrm{x} _ {j} | \mathrm{A} = \mathrm{a} _ {i}, Z = z, W ^ {\prime} = w ^ {\prime} \big) \cdot \mathrm{P} \big (\mathrm{A} = \mathrm{a} _ {i} | W = w \big) \\ & = \mathrm{P} \big (\mathrm{X} = \mathrm{x} _ {j} | \mathrm{A} = \mathrm{a} _ {i}, Z = z \big) \cdot \mathrm{P} \big (\mathrm{A} = \mathrm{a} _ {i} | W = w \big) \text {for all i,j}. \end{array}
$$

Therefore:

$$
\begin{array}{l} \mathrm {I(A;X|W = w) = \sum_ {j} \sum_ {i} P(A = a_ {i} , X = x_ {j} |W = w)\log \frac {P(A = a_ {i} , X = x_ {j} |W = w)}{P(A = a_ {i} |W = w)\cdot P(X = x_ {j} |W = w)}} \\ \qquad = \sum_ {j} \sum_ {i} P (X = x _ {j} | A = a _ {i}, Z = z) \cdot P (A = a _ {i} | W = w) \log \frac {P (X = x _ {j} | A = a _ {i} , W = w)}{P (X = x _ {j} | W = w)} \\ \qquad = \sum_ {j} \sum_ {i} P (X = x _ {j} | A = a _ {i}, Z = z) \cdot P (A = a _ {i} | W = w) \log \frac {P (X = x _ {j} | A = a _ {i} , W = w)}{\sum_ {i} P (X = x _ {j} , A = a _ {i} | W = w)} \\ \qquad = \sum_ {j} \sum_ {i} P (X = x _ {j} | A = a _ {i}, Z = z) \\ \qquad \cdot P (A = a _ {i} | W = w) \log \frac {P (X = x _ {j} | A = a _ {i} , Z = z)}{\sum_ {i} P (X = x _ {j} | A = a _ {i} , Z = z) \cdot P (A = a _ {i} | W = w)}. \end{array}
$$

## References

[1] A. Agresti, Categorical Data Analysis (Wiley, New York, 1990).

[2] S.K. Asare and W.F. Messier, A Review of Audit Research Using the Belief-Adjustment Model, in: L.A. Ponemon and D.R.L. Gabhart, Eds., Auditing: Advances in Behavioral Research (Springer-Verlag, Berlin, 1991) 75–91.

[3] R. Ash, Information Theory (Wiley, New York, 1965).

[4] J.O. Berger, Statistical Decision Theory and Bayesian Analysis (Springer-Verlag, Berlin, 1985).

[5] R.H. Bonczek, C.W. Holsapple and A.B. Whinston, A Generalized Decision Support System using Predicate Calculus and Network Database Management, Operations Research 29, No. 2 (1981) 263–281.

[6] A. Dutta and A. Basu, An Artificial Intelligence Approach to Model Management in Decision Support Systems, IEEE Computer 17, No. 9 (1984) 89–97.

[7] A.K. Goel, Integrating Case-Based and Model-Based Reasoning, AI Magazine (1992) 50–54.

[8] D. Heckerman, Probabilistic Interpretation of MYCIN's Certainty factors, in: J. Lemmer and L. Kanal, Eds., Uncertainty in Artificial Intelligence (North-Holland, NY, 1986) 167–196.

[9] R. Howard, Information Value Theory, IEEE Transactions on Systems Science and Cybernetics SSC-2, No. 1 (1966) 22–26.

[10] R.A. Johnson and D.W. Wichem, Applied Multivariate Statistical Analysis (Prentice Hall, New Jersey, 1992).

[11] J.L. Kolodner, Case-Based Reasoning (Morgan Kaufmann Publishers, San Mateo, CA, 1993).

[12] M. Machina, Decision-Making in the Presence of Risk, Science (1987) 537–543.

[13] J.E. Matheson, The Economic Value of Analysis and Computation, IEEE Transactions on Systems Science and Cybernetics SSC-4, No. 3 (1968).

[14] V.S. Mookerjee and B.L. Dos Santos, Inductive Expert System Design: Maximizing System Value, Information Systems Research 4, No. 2 (1993) 111–140.

[15] J.C. Moore and A.B. Whinston, A Model of Decision-Making With Sequential Information Acquisition-Part I, Decision Support Systems 2 (1986) 285–307.

[16] J.C. Moore and A.B. Whinston, A Model of Decision-Making With Sequential Information Acquisition-Part II, Decision Support Systems 3 (1987) 47–72.

[17] T. Mukhopadhyay, S. Vicinanza and M.J. Prietula, Examining the Feasibility of a Case-Based Reasoning Model for Software Effort Estimation, MIS Quarterly (1992) 155–170.

[18] F.H. Murphy and E.A. Stohr, An Intelligent System for Formulating Linear Programs, Decision Support Systems 2 (1986) 39–47.

[19] J.R. Quinlan, C4.5: Programs for Machine Learning (Morgan Kaufmann Publishers, 1993).

[20] C.E. Shannon, A Mathematical Theory of Communication, The Bell System Technical Journal 27 (1948) 379–423 & 623–656.

[21] M.J. Shaw, Applying Inductive Learning to Enhance Knowledge-Based Expert Systems, Decision Support Systems 3 (1987) 319–332.

[22] A. Tversky and D. Kahneman, Judgement Under Uncertainty: Heuristics and Biases, Science 185 (1974) 1124–1131.

[23] R. Uthurusamy, U.M. Fayyad and S. Spangler, Learning Useful Rules from Inconclusive Data, in: G. Piatetsky-Shapiro and W.J. Frawley, Eds., Knowledge Discovery in Databases (1991) 141–157.

[24] R.C. Vellore, A.S. Vinze and A. Sen, Modeller, Incorporating Experiences to Support Model Formulation — A Case-Based Planning Approach, Expert Systems with Applications 6 (1993) 37–56.

[25] R.L. Winkler and R.M. Poses, Evaluating and Combining Physicians' Probabilities of Survival in an Intensive Care Unit, Management Science 39, No. 12 (1993) 1526–1543.

Deb Ghosh is an Associate Professor of MIS in the Information Systems and Decision Sciences Department at Louisiana State University, Baton Rouge. He received his Bachelor of Technology in Electronics Engineering from Indian Institute of Technology, Kharagpur, India in 1983 and a Ph.D. in MIS from Syracuse University in 1988. Ded Ghosh's research publications have appeared in journals such as Operations Research, European Journal of Operational Research, Annals of OR, OMEGA, Computers and OR, etc. He has presented papers in various national and international meetings.

![](/api/attachments/YWNGCJS5/fulltext/images/89bdbf92a222d5dfa22ee14bbe8234e4aff1c1cecdafe434be20fc3bc44bd750.jpg)

Sumit Sarkar is Associate Professor of Management Information Systems in the College of Business at Louisiana State University. He received his M.S. and Ph.D. degrees in Computers and Information Systems from the University of Rochester. His current research interests include decision-making under uncertain conditions, the representation of uncertainty in expert systems and databases, the design of knowledge-based systems, and the economics of information systems. He is a member of AAAI, ACM, INFORMS and IEEE Computer Society.
