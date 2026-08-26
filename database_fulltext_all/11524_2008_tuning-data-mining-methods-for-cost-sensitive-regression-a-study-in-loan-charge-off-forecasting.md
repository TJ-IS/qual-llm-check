---
otero_id: 11524
otero_key: "ZAEWHQQU"
title: "Tuning Data Mining Methods for Cost-Sensitive Regression: A Study in Loan Charge-Off Forecasting"
authors: "Gaurav Bansal; Atish P. Sinha; Huimin Zhao"
year: "2008"
journal: "Journal of Management Information Systems"
doi: "10.2753/mis0742-1222250309"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Tuning Data Mining Methods for Cost-Sensitive Regression: A Study in Loan Charge-Off Forecasting

Gaurav Bansal , Atish P. Sinha & Huimin Zhao

To cite this article: Gaurav Bansal , Atish P. Sinha & Huimin Zhao (2008) Tuning Data Mining Methods for Cost-Sensitive Regression: A Study in Loan Charge-Off Forecasting, Journal of Management Information Systems, 25:3, 315-336

To link to this article: http://dx.doi.org/10.2753/MIS0742-1222250309

![](/api/attachments/ZAEWHQQU/fulltext/images/3adca5f24281e43b9d59ce7346279f9ea0fc85a5454ad84f0d968d1776c716ba.jpg)

Published online: 08 Dec 2014.

![](/api/attachments/ZAEWHQQU/fulltext/images/2a50a500987472f2d5e88630da674ea839405546b6d60509450739980437f5e8.jpg)

Submit your article to this journal

![](/api/attachments/ZAEWHQQU/fulltext/images/28fd4e57be55b8d7d93c945b0f48cc95d31aabe9d4e0fbbbfd3e31cb40e5db27.jpg)

Article views: 23

![](/api/attachments/ZAEWHQQU/fulltext/images/7e8e24f7034197ab1ba75333bb1ef9ce3968866c9b5a0b0e1763f264272e1eda.jpg)

View related articles

# Tuning Data Mining Methods for Cost-Sensitive Regression: A Study in Loan Charge-Off Forecasting

Gaurav Bans al, Atis h P. Sin ha, and Huimn Zhao

Gaurav Bansal is an Assistant Professor of MIS/Statistics at the University of Wisconsin–Green Bay. He earned his Ph.D. in MIS from the University of Wisconsin– Milwaukee, M.B.A. from Kent State University, and B.E. in Mechanical Engineering from the Madan Mohan Malaviya Engineering College, University of Gorakhpur, India. His current research interests are in the areas of information privacy, e-commerce, and data mining. He is a member of the AIS.

Atish P. Sinha is a Professor of MIS and Roger L. Fitzsimonds Distinguished Scholar at the Sheldon B. Lubar School of Business, University of Wisconsin–Milwaukee. He earned his Ph.D. in business, with a concentration in artificial intelligence, from the University of Pittsburgh. His current research interests are in the areas of data mining, data warehousing, and component-based software engineering. His research has been published in several journals, including Communications of the ACM, Decision Support Systems, IEEE Transactions on Engineering Management, IEEE Transactions on Software Engineering, IEEE Transactions on Systems, Man, and Cybernetics, Information Systems Research, International Journal of Human–Computer Studies, and Journal of Management Information Systems. Professor Sinha is a member of ACM, AIS, and INFORMS. He served as the cochair of the 16th Workshop on Information Technologies and Systems (WITS) in 2006.

Huimin Zhao is an Associate Professor of MIS at the Sheldon B. Lubar School of Business, University of Wisconsin–Milwaukee. He earned his Ph.D. in MIS from The University of Arizona. His current research interests are in the areas of data mining, data integration, and medical informatics. His research has been published in several journals, including Journal of Management Information Systems, Communications of the ACM, IEEE Transactions on Knowledge and Data Engineering, IEEE Transactions on Systems, Man, and Cybernetics, Information Systems, Data and Knowledge Engineering, Decision Support Systems, and Journal of Database Management. He is a member of IEEE, AIS, IRMA, and INFORMS.

Ab stract: Real-world predictive data mining (classification or regression) problems are often cost sensitive, meaning that different types of prediction errors are not equally costly. While cost-sensitive learning methods for classification problems have been extensively studied recently, cost-sensitive regression has not been adequately addressed in the data mining literature yet. In this paper, we first advocate the use of average misprediction cost as a measure for assessing the performance of a cost-sensitive regression model. We then propose an efficient algorithm for tuning a regression model to further reduce its average misprediction cost. In contrast with previous statistical methods, which are tailored to particular cost functions, this algorithm can deal with any convex cost functions without modifying the underlying regression methods. We have evaluated the algorithm in bank loan charge-off forecasting, where underforecasting is considered much more costly than overforecasting. Our results show that the proposed algorithm significantly reduces the average misprediction costs of models learned with various base regression methods, such as linear regression, model tree, and neural network. The amount of cost reduction increases as the difference between the unit costs of the two types of errors (overprediction and underprediction) increases.

Key words and phrases: asymmetric costs, cost-sensitive regression, data mining, forecasting, loan charge-off, model tuning.

Org aniz ations are increasing ly employing data mining techniques to uncover useful and actionable information from corporate data. The most common type of problem addressed in data mining is prediction, where a dependent variable is predicted based on a set of independent variables. Various data mining techniques have been developed to automatically induce prediction models based on training examples with known outcomes. The trained models can then be applied to predict the outcomes of new problem instances in the future.

There are two types of predictive data mining—classification and regression. In a classification problem, the dependent variable that needs to be predicted is categorical, whereas in a regression problem, the dependent variable is numerical and continuous. The focus of prior research has been on the binary classification problem (where the dependent variable can belong to one of two categories). Studies addressing the binary classification problem in business cover a variety of applications, including workplace Web usage profiling [1], deception detection [28], credit evaluation [18], bankruptcy prediction [13, 20, 21], bank failure prevention [17, 19], and new venture success prediction [11]. Data mining and Bayesian techniques have also been used for the regression problem in applications such as reliability estimation [22], demand forecasting and inventory management [4], and real estate assessment [24].

Real-world prediction problems are often cost sensitive, meaning that different types of prediction errors are not equally costly [8, 14, 22, 26]. In a binary classification problem, the cost of a false positive could be very different from that of a false negative. For example, misclassifying a bankrupt corporation as nonbankrupt is a much more serious mistake than doing the reverse [20, 21]. Similarly, a regression problem may also be characterized by asymmetric costs with respect to overprediction and underprediction. For example, when banks forecast loan losses, underforecasting is considered to be much more costly than overforecasting. In such cost-sensitive forecasting or regression problems, the usual cost-neutral performance measures—such as correlation coefficient or R<sup>2</sup>, relative absolute error, and root relative square error—are not appropriate for assessing the true performance of trained models.

The last decade has witnessed a growing body of work in cost-sensitive classification. Several methods have been developed to convert a regular classification method into a cost-sensitive one. Costs can be directly incorporated into a predictive model during training [6]. For example, Ting [23] used an instance-weighting method for making decision trees cost sensitive, and Tam and Kiang [21] modified the backprop algorithm for neural nets by including prior probabilities and misclassification costs. Elkan [8], on the other hand, recommended that we let classifiers learn from the given training data, and then determine optimal decision thresholds empirically. Sinha and May [18], for example, presented an approach for tuning predictive data mining models post hoc to make them cost sensitive. In their study, the models were trained without factoring in costs. The models were tuned—in an effort to minimize misclassification cost—only after they had been generated.

Finally, there are some base classification methods (e.g., naive Bayes) that are inherently cost sensitive [25] and for which both types of cost-sensitive learning result in similar models. Others, such as decision tree methods, learn very different models when cost information is incorporated during training [23] rather than post hoc [27].

There have been a number of studies relating to cost-sensitive classification, but relatively few studies in the data mining literature have addressed the issue of costsensitive regression. Classical statistical estimation and prediction methods have been extended to deal with particular asymmetric loss functions, such as linlin, linex, and squarex, which are amenable to closed-form solutions [22, 24, 26]. Varian [24] introduced asymmetric linex cost functions, which rise linearly for underestimation and exponentially for overestimation. The cost function was demonstrated for the appraisal of single-family homes, where the county bases its tax on the appraised value. Underestimation is costly because it leads to lower taxes, but overestimation is even more costly because it leads to complaints and court appeals. Hence, while underestimation was represented by a linear cost function, overestimation was represented by an exponential cost function. The normal regression techniques, which are based on quadratic cost functions, assume the over- and undercosts to be equal, and hence are inappropriate. Zellner [26] also extensively investigated linex across several statistical estimation and prediction problems. Later, Thompson and Basu [22], generalizing the linex cost function [24], introduced the asymmetric squarex cost function, where the cost follows an exponential function on one side of the error curve and a square function on the other side. Recently, Crone et al. [4] proposed a method for training a multilayer perceptron under asymmetric loss. However, generic methods that can convert any base regression methods into cost-sensitive learning methods and can deal with any cost functions are yet to be developed.

In this paper, we first advocate the use of average misprediction cost as a measure for assessing the performance of a cost-sensitive regression model. We then propose an efficient algorithm for tuning the regression model post hoc to further reduce its average misprediction cost. The algorithm is generic and can deal with any convex cost functions without modifying the underlying regression methods. We have evaluated the algorithm on a problem in loan-loss forecasting using real bank data. Our results show that the proposed algorithm significantly reduces the average misprediction costs of models learned with the following base regression methods—linear regression, model tree, and neural network. The degree of cost reduction increases as the difference between the unit costs of the two types of errors (overprediction and underprediction) increases.

Our study makes several important contributions to the literature. First, we propose a new measure, average misprediction cost, for the finance and banking domain. Traditionally, cost-insensitive measures, such as $R ^ { 2 }$ and relative absolute error, have been used for regression problems. We show that the use of such measures is inappropriate for situations where costs are asymmetric. Second, to the best of our knowledge, this is the first study to present an approach for tuning data mining models, so as to minimize misprediction costs, for regression problems in a post hoc manner—that is, after the models have already been learned. As discussed later in more detail, this is a big advantage for organizations that operate in environments where the shape and parameters of the cost function could change over time. And, finally, we did not find a single study in the literature comparing the performance of multiple data mining methods for a cost-sensitive regression problem. In this study, we evaluate the performance of three popular data mining methods on a real-world forecasting problem in loan charge-offs.

## Bank Loan-Loss Forecasting

Reg ression studies larg ely dwell upon $R ^ { 2 }$ as the measure of accuracy, assigning equal weights to the deviations from the mean in both directions. This is acceptable when the concern is only with accurate predictions, and deviations in both directions are equally undesirable. This approach fails when deviations are weighted unequally, as in the case of loan charge-off predictions for banks. Underpredicting the loan charge-off amount is much more risky for a bank than overpredicting the same amount because it presents a rosier picture of an otherwise worse scenario. Accurately predicting the actual loan loss (where actual loan loss = loan charge-off – portion of the loan recovered) is important not only for banks but also for regulators and investors. Banks are required to have adequate provisions for loan losses. It is important for banks to have systems in place for forecasting loan losses. Investors and regulators are always interested in knowing whether banks are adequately prepared for their loan losses. Regulators, in particular, want to anticipate a bank’s loan losses and then determine whether the bank is sufficiently prepared to face those losses or not. If the bank does not have sufficient loan-loss reserves, the consequences could be dire. Hence, it is necessary to penalize underpredictions more heavily than overpredictions, thereby discouraging banks from having less than adequate amounts as reserves.

If a bank overpredicts its loan charge-off, it has to maintain extra funds in the loan-loss reserves; hence, a possible problem is that it will experience reduced earnings (because the reserves are directly deducted from earnings), along with possibly a lower credit score from its financial analysts. But in the case of underprediction, it will not only face the wrath of regulators, accountants, and the Securities and Exchange Commission (SEC) but will also likely witness an even greater downturn in its credit ratings.

If banks predict less than what their loan losses finally turn out to be, they are not going to keep aside enough reserves. If they predict more, they are going to land up with higher reserves. Not having enough reserves causes regulatory problems. On the other hand, having higher reserves reduces the income. Of the two, underprediction is more costly because the banking authorities are also concerned about classifying a failing bank as a nonproblem bank [19]. Moreover, inadequate provisioning makes the fluctuations in bank earnings magnify true oscillations in bank profitability [3]. Henderson [10] showed that poor economic performance of minority-owned banks could be the result of underprovisioning for loan losses, reflecting an inadequate assessment of risk. As he points out, “by examining the provision for loan loss, one can assess how a bank manages the choice among risk (loan default) and return” [10, p. 373].

It is important to understand that charge-off is not a forgiveness of the debt in any way. It is only an accounting entry by the one who is owed. A charge-off (or write-off) is the accounting process where a business acknowledges a receivable (an asset or loan) is uncollectible. It considers the lost receivable as a charge against its earnings.

In addition to bank management, outside bodies such as the SEC, accountants, and regulators have a direct voice in the loan-loss reserve creation process. The SEC plays a role in the reserve formation by warning bank holding companies to frequently examine their potential loan losses and to adjust the reserves accordingly. The reserve adequacy is also considered by the financial analysts, especially those who are responsible for the banks’ credit ratings. Cares [2] identifies that the key test of adequacy of the loan-loss reserves is the multiple by which the reserve exceeds the normalized net charge-offs.

## Cost-Sensitive Regression

Just as error rate is not ap ropriate for assessing model performance for costsensitive classification problems [8, 14], cost-neutral performance measures usually adopted in the literature (e.g., correlation coefficient, relative error) are also not appropriate performance measures for cost-sensitive regression problems. Similar to the average misclassification cost measure used for cost-sensitive classification problems (see, e.g., [8, 18]), we propose average misprediction cost as a performance measure for assessing cost-sensitive regression models. We then propose an algorithm for tuning a model learned by regular regression methods to minimize this cost.

## Cost-Sensitive Performance Measure

Consider a regression problem where a continuous dependent variable y needs to be predicted based on a vector of independent variables x. A regression method learns a prediction model, $f \colon x  y .$ , from a training data set consisting of problem instances with known dependent variable values, $S = \{ < x _ { i } , y _ { i } > \mid i = 1 , 2 , . . . , N \}$ . Assuming that a prediction error e incurs a cost characterized by a cost function C(e), we define the average misprediction cost of model f, as estimated on data set S, as

$$
\theta = \frac {1}{N} \sum_ {i = 1} ^ {N} C \left(f (x _ {i}) - y _ {i}\right).\tag{1}
$$

Note that a performance measure estimated on the training data set is not a reliable estimate for the true performance of a learned model; the measure should be estimated on an independent test data set. In our experiments (reported later), we tuned the models using the training data sets, but evaluated the performance of the tuned models using independent test data sets.

Some required properties of the cost function C are

$C ( e ) \geq 0 ;$

$C ( 0 ) = 0 ;$ and

$$
\bullet \quad | e _ {1} | <   | e _ {2} | \wedge e _ {1} e _ {2} > 0 \rightarrow C (e _ {1}) <   C (e _ {2}).
$$

In other words, the cost function is nonnegative, equals zero when there is no error, and is monotonic for each type of error.

The cost function C is necessarily problem dependent. For the bank loan-loss forecasting problem, we assume a simple linlin (linear on both sides) cost function with different slopes for underforecasting and overforecasting (illustrated in Figure 1), after the misprediction error has been normalized by the total loan amount of the bank. More complex nonlinear cost functions are possible in other problems. Conventional performance measures, such as correlation coefficient and relative error, essentially assume that $C ( e ) = C ( - e )$ for any misprediction error e. These measures are thus not suitable in cost-sensitive problems, where $C ( e )$ and $C ( - e )$ are in general different.

## Performance Tuning Algorithm

Regular regression methods, such as linear regression, neural network, and model tree, seek to optimize cost-neutral performance measures during the model induction based on the training data set. The models are therefore not optimized on the average misprediction cost. We propose a method for tuning the performance of a model trained by a regular regression method after the model induction process. Suppose we adjust the prediction of a learned regression model f by an amount of δ and denote the adjusted model $f ^ { \prime } = f + \delta .$ . The average misprediction cost of the adjusted model $f ^ { \prime }$ is the following function of δ (Figure 2 shows an example):

$$
\theta (\delta) = \frac {1}{N} \sum_ {i = 1} ^ {N} C \left(f ^ {\prime} \left(x _ {i}\right) - y _ {i}\right) = \frac {1}{N} \sum_ {i = 1} ^ {N} C \left(\delta + \left(f \left(x _ {i}\right) - y _ {i}\right)\right).\tag{2}
$$

A brute force algorithm can be used to evaluate every possible δ (with a given precision) until all adjusted predictions become over- (or under-) predictions and return the $\delta$ that results in the lowest average misprediction cost—that is, $\delta ^ { * } = a r g m i n \ \theta ( \delta )$ However, because $\theta ( \delta )$ is convex when the cost function C is convex (see Proposition 1 in the Appendix), which we believe is usually the case, a more efficient hill-climbing algorithm can be designed to locate δ<sup>\*</sup>. Figure 3 lists such an algorithm.

![](/api/attachments/ZAEWHQQU/fulltext/images/ec871e7938ce5ba67326e1a1c82197055ae7b0c3b161eb8bc717c16fc4c861b7.jpg)  
Figure 1. A Linlin Cost Function

![](/api/attachments/ZAEWHQQU/fulltext/images/19353a086cb8d68fd3fa37a070605491b984600e8b19c53722624ea85dd32480.jpg)  
Figure 2. Average Misprediction Cost as a Function of the Amount of Adjustment Notes: The cost curve is based on the March 2003 data set for the bank loan-loss forecasting problem. The base regression method used is the M5 model tree. The ratio between the unit cost of underforecasting and that of overforecasting is 100:1.

The algorithm takes a base regression method, a training data set, a cost function, and a given precision of adjustment as inputs and returns an adjusted regression model. First, a regression model is trained using the base regression method, without considering the cost function (line 1). Then, the direction of adjustment, which leads to lower average misprediction cost, is determined (lines 2 to 4). Starting from zero adjustment (line 5), several iterations of hill climbing are then performed to approach the optimal adjustment until the number of climbing steps during an iteration falls below two and no further climbing is promising (lines 6 to 7). During each iteration of hill climbing, several climbing steps are attempted until the performance starts to decrease. To speed up the climbing, the climbing stride starts from the given precision of adjustment and is doubled after every step. Finally, an adjusted regression model with the best found adjustment is returned (line 8).

```txt
Cost_Sensitive_Regression (Γ, S, C, p)
    Γ: A base regression method, e.g., M5.
    S: A training data set, {<x_i, y_i> | i = 1, 2, ..., N}.
    C: A cost function.
    p: A given precision of adjustment. p > 0.

1. Train a regression model f using Γ based on S.
2. If θ(p) < θ(0), /* θ is defined in equation (2). */
2.1 Set the direction of adjustment, d := 1.
3. Else If θ(-p) < θ(0),
3.1 d := -1.
4. Else
4.1 Return f.
5. δ_prev := 0.
6. Loop
6.1 Set the hill-climbing stride, s := 1.
6.2 δ := δ_prev.
6.3 Loop
6.3.1 δ_prev := δ.
6.3.2 δ := δ + s * d * p.
6.3.3 s := s * 2;
6.3.4 δ_next := δ + s * d * p.
6.4 Until θ(δ_next) > θ(δ).
7. Until s ≤ 2.
8. Return an adjusted regression model f' = f + δ.
```  
Figure 3. A Performance Tuning Algorithm for Cost-Sensitive Regression Problems

The algorithm is generic and can be used to tune a model trained with any regression method for any convex cost function. The algorithm is also efficient. It can be shown (see Proposition 2 in the Appendix) that the worst-case time complexity of this algorithm is O([log n]<sup>2</sup>), assuming there are n possible δ values that need to be evaluated by a brute force algorithm.

## Procedure and Empirical Evaluation

We have implemented the proposed performance tuning algorithm by extending the Weka machine learning toolkit [25] and evaluated the algorithm using real data of bank loan losses. We report on some empirical results in this section.

## Implementation

We implemented the proposed performance tuning algorithm in Java as a subclass of the Classifier class in Weka (www.cs.waikato.ac.nz/ml/weka/). The algorithm takes four inputs—base regression method, training data set, cost function, and given precision of adjustment. We used base regression methods and the attribute-relation file format (AR FF) of Weka. We implemented the linlin cost function. We used a 0.01 precision of adjustment, which should provide sufficient precision. Because the base regression method and the cost function are inputs to the tuning algorithm and do not need to be modified by the tuning algorithm, our program can be easily extended to work with wrapped plug-in modules of other cost functions and regression methods from other software packages such as SPSS and SAS. This methodology can therefore be easily applied in practical contexts, which may require special cost functions and particular software packages.

## Base Regression Methods

We used three base regression methods available in Weka: linear regression (LR ), the M5 model tree, and backpropagation neural network (NN). LR implements the standard least-squares linear regression method. M5 [15] follows a “divide and conquer,” recursive partitioning heuristic search strategy and induces a tree with linear regression functions at the leaves. Backpropagation [16] is one of the most widely used neural network learning techniques for classification and regression. We kept Weka’s default settings for all of the parameters.

Weka reports several cost-insensitive performance measures for these regression methods, including correlation coefficient, relative absolute error, and root relative square error. Correlation coefficient is the Pearson linear correlation between the predicted and actual values of the dependent variable. Relative absolute error is the ratio of the mean absolute error of the learned model to the mean absolute error obtained by simply predicting the mean of the training data. Similarly, root relative square error is the ratio of the mean squared error of the learned model to the mean squared error obtained by simply predicting the mean of the training data.

## Data Set

We used the “bank regulatory” data set from Wharton Research Data Services (WRDS).<sup>1</sup> WRDS contains five databases for regulated depository financial institutions. These databases provide accounting data for bank holding companies, commercial banks, savings banks, and savings and loans institutions. The data were acquired from the required regulatory forms that were filed for supervising purposes. We used the commercial banks data set within the Bank Regulatory database for this study. The Commercial Bank database, originating from the Federal Reserve Bank of Chicago (FRB Chicago), contains data of all banks filing the Report of Condition and Income (known as “Call Report”) regulated by the Federal Reserve System, Federal Deposit

Insurance Corporation (FDIC), and the Comptroller of the Currency. These reports include balance sheet, income statements, risk-based capital measures, and off-balance sheet data. The database covers commercial banks and savings banks. The data set used in this study has approximately 8,500 observations for each quarter.

The sample data set we used covers 17 quarters from March $2 0 0 1 ^ { 2 }$ to March 2005. We used one quarter as a training set to predict the next quarter (test set). We also used aggregated four quarters as a training set to predict up to four quarters ahead, one quarter at a time. For example, the aggregated data set from March 2003 to December 2003 is used to predict March 2004, June 2004, September 2004, and December 2004 quarters separately.

## Variables

As noted before, the dependent variable in this study is loan charge-off (RIAD 4635).<sup>3</sup> Based on the relevant literature, we chose a set of independent variables related to size [9], risk, and economy [12]. In addition to these three categories of variables, we also included two other categories—intangible asset variables and loan-specific variables. There are three variables in the size category—total assets, net income, and net interest income. The risk category has two variables—weighted average total assets and subordinated debt. The economy category has two variables—expense on fed funds and equity capital. The intangible asset category has two variables—intangible assets and goodwill. Loan-specific variables are total loans and lease (gross), total loans not accruing, loans 90+ days late, and interest and fee income from loans. The WRDS data set provides the definitions for these variables (summarized in Table 1).

## Cost Information

As discussed earlier, underprediction hides the woes of the bank and presents a rosier picture of an otherwise bad scenario. Overprediction is less costly because the only cost associated with it is the extra provision the bank has to provide in the loan-loss reserves, and this may lead to lowered earnings in that particular quarter. But, compared to the case of underprediction, the financial distress is much less.

We normalized the misprediction error (difference between the predicted and actual loan charge-offs) by the total loan amount of a bank (RCFD 1400) and then applied a linlin cost function on the normalized misprediction error. The normalized misprediction error is

$$
e = \frac {\text {   Predicted   gross   charge - off   } - \text {   Actual   gross   charge - off   }}{\text {   Aggregate   gross   book   value   of   total   loans   }}.
$$

The cost function is

$$
C (e) = c ^ {+} e, \text {   if   } e > 0; c ^ {-} e, \text {   otherwise },
$$

where $c ^ { + }$ and $c ^ { - }$ are the slopes for overprediction and underprediction, respectively.

<table><tr><td colspan="4">Table 1. Variables Used in the Study</td></tr><tr><td>Code</td><td>Variable name</td><td>Definition</td><td>Explanation</td></tr><tr><td> $\text{RCFD}^1$ 1400</td><td>Total loans and leases, gross</td><td>The aggregate gross book value of total loans (before deduction of valuation reserves).</td><td>Belongs to the loan category.Book value—value at which an asset is carried on a balance sheet. For example, a piece of manufacturing equipment is put on the book at its cost when purchased [7].</td></tr><tr><td>RCFD1403</td><td>Total loans and lease finance receivables: nonaccrual</td><td>Includes the outstanding balances of loans and lease financing receivables that the bank has placed in nonaccrual status. Also includes all restructured loans and lease financing receivables that are in nonaccrual status.</td><td>Belongs to the loan category.Receivables—accounts receivable owned by borrowers that are pledged as collateral for a loan made with the bank [5].</td></tr><tr><td>RCFD1407</td><td>Total loans and lease financing receivables: past due 90 days or more and still accruing</td><td>Includes loans and lease financing receivables on which payment is due and unpaid for 90 days or more. Also includes all restructured loans and leases.</td><td>Belongs to the loan category.</td></tr><tr><td>RCFD2143</td><td>Intangible assets</td><td>Includes the unamortized amount of intangible assets.</td><td>Belongs to the intangible assets category.Amortization—accounting procedure that gradually reduces the cost value of a limited-life or intangible asset through periodic changes to income. For fixed assets the term used is depreciation and for wasting assets (natural resources) it is depletion, both terms meaning essentially the same thing as amortization [7].Intangible asset—right or nonphysical resource that is presumed to represent an advantage to the firm's position in the marketplace [7].</td></tr><tr><td>RCFD2170</td><td>Total assets</td><td>It is the sum of all asset items. It equals “total liabilities, limited-life preferred stock, and equity capital.”</td><td>Belongs to the size category.Equity—difference between the amount a property could be sold for and the claims held against it [7].</td></tr><tr><td>Code</td><td>Variable name</td><td>Definition</td><td>Explanation</td></tr><tr><td>RCFD3163</td><td>Goodwill</td><td>Includes the amount (book value) of unamortized goodwill. Represents the excess of the cost of a company over the sum of the fair values of the tangible assets and identifiable intangible assets acquired less the fair value of liabilities.</td><td>Belongs to the intangible assets category.Goodwill—intangible asset representing going concern value in excess value paid by a company for another company in a purchase acquisition [7].</td></tr><tr><td>RCFD3200</td><td>Subordinated notes and debentures</td><td>Includes the amount of outstanding subordinated notes and debentures (including mandatory convertible debt).</td><td>Belongs to the risk category.Subordinated—junior in claim on assets to other debts, that is, repayable only after other debts with a higher claim have been satisfied [7].</td></tr><tr><td>RCFD3210</td><td>Equity capital, total</td><td>The sum of “perpetual preferred stock and related surplus,” “common stock,” “surplus,” “undivided profits and capital reserves,” “cumulative foreign currency translation adjustments” less “net unrealized loss on marketable equity securities.”</td><td>Belongs to the economy category.</td></tr><tr><td>RCFD4010</td><td>Total interest and fee income on loans</td><td>Includes the total of interest and fee income and similar charges levied against all assets classified as loans in condition reports, including fees on overdrafts. Includes investigation and service charges, renewal and past due charges, commitment fees (regardless of whether the loan has been made), and fees charged for the execution of mortgages or agreements securing the bank’s loans.</td><td>Belongs to the loan category.</td></tr><tr><td>RIAD $^{2}$ 4079</td><td>Total noninterest income</td><td>Includes the sum of “income from fiduciary activities,” “service charges on deposit accounts in domestic offices,” “trading gains (losses) and fees from foreign exchange transactions,” “other foreign transaction gains (losses),” “gains (losses) and fees from assets held in trading accounts,” and “other noninterest income.”</td><td>Belongs to the size category.Fiduciary—person, company, or association holding asset in trust for a beneficiary. The fiduciary is charged with the responsibility of investing the money wisely for the beneficiary benefit [7].</td></tr><tr><td>RCFD4180</td><td>Expense of federal funds purchased and securities sold under</td><td>Includes the gross expense of all liabilities included in “federal funds purchased and securities sold under agreements to repurchase.”</td><td>Belongs to the economy category.Federal funds—funds deposited by commercial banks at Federal Reserve banks, including funds in excess of</td></tr></table>

Notes: 1 RCFD: 
RCFD variable—from the 
Report of Condition (W
RDS data set). 2 RIAD: 
RIAD variable—from the 
Report of Income (W
RDS data set).

<sub>as</sub>h <sup>[5]</sup> i<sub>ts</sub> <sub>ab</sub>ili<sub>ty</sub> <sub>to</sub> m<sup>eet</sup> i<sup>ts</sup> li<sup>ab</sup>ili<sup>t</sup>i<sup>es</sup> <sup>to</sup> <sup>dep</sup> <sub>nds</sub> <sub>that</sub> <sub>has</sub> <sub>been</sub> <sub>s</sub>e<sup>t</sup> <sup>as</sup>i<sup>de</sup> <sup>for</sup> <sup>the</sup> <sup>pu</sup> <sub>the</sub> <sub>reserve</sub> <sub>[7]</sub>. <sub>Reserves</sub>—<sup>a</sup> <sup>port</sup>i<sup>o</sup> <sub>x-deduct</sub>i<sub>b</sub>l<sub>e</sub> <sub>charges</sub> <sub>to</sub> i<sub>nco</sub>m<sup>e</sup> <sup>to</sup> <sup>rep</sup> <sub>the</sub> <sub>reserve</sub> <sub>for</sub> <sub>act</sub><sup>ua</sup>l <sup>bad</sup> <sup>debts</sup> <sup>an</sup> <sub>nta</sub>i<sub>ned</sub> <sub>a</sub> <sub>reserv</sub>e <sup>for</sup> <sup>unco</sup>ll<sup>ect</sup>i<sup>b</sup>l<sup>e</sup> <sup>a</sup> i<sub>ona</sub>ll<sub>y</sub>, <sub>co</sub>m<sup>pan</sup>i<sup>es</sup> <sup>and</sup> <sup>financ</sup>i<sup>a</sup>l i<sup>ns</sup> <sub>e</sub> <sub>that</sub> <sub>has</sub> <sub>proven</sub> <sub>un</sub>c<sup>o</sup>ll<sup>ect</sup>i<sup>b</sup>l<sup>e</sup> <sup>and</sup> <sub>ff</sub> <sub>(bad</sub> <sub>debt)</sub>—<sup>open</sup> <sup>account</sup> <sup>ba</sup>l<sup>anc</sup> <sub>rator</sub> <sub>of</sub> <sub>the</sub> <sub>de</sub><sup>pendent</sup> <sup>va</sup>

<sub>o</sub> <sub>est</sub>i<sub>mated</sub> <sup>r</sup>i<sup>sk-we</sup>i<sup>ghted</sup> <sup>ass</sup> <sub>a</sub>i<sub>nta</sub>i<sub>n</sub> <sub>a</sub> <sub>m</sub>i<sub>n</sub>i<sub>m</sub>u<sup>m</sup> <sup>rat</sup>i<sup>o</sup> <sup>of</sup> <sup>est</sup>i<sup>mat</sup> <sub>nd</sub> <sub>Recovery</sub> <sub>Act)-</sub>im<sup>posed</sup> <sup>requ</sup>i<sup>rem</sup> <sub>ed</sub> <sub>cap</sub>i<sub>ta</sub>l <sub>rat</sub>i<sub>o</sub>—<sup>F</sup>I<sup>RREA</sup> <sup>(F</sup>i<sup>nanc</sup>i<sup>a</sup>l I <sub>ngs</sub> <sub>to</sub> <sub>the</sub> <sub>r</sub>is<sup>k</sup> <sup>cate</sup>

## l<sub>ongs</sub> <sub>to</sub> <sub>the</sub> <sub>s</sub>i<sup>ze</sup> <sup>cate</sup>

<sub>us</sub> <sub>reserv</sub><sup>e</sup> <sup>banks</sup> <sub>bas</sub>i<sub>s</sub> <sub>by</sub> <sub>deb</sub>i<sub>t</sub>i<sub>ng</sub> <sub>a</sub>n<sup>d</sup> <sup>cred</sup>i<sup>t</sup>i<sup>ng</sup> <sup>ba</sup>l<sup>anc</sup> <sub>hemse</sub>l<sub>ves</sub> <sub>or</sub> <sub>on</sub> <sub>b</sub><sup>eha</sup>l<sup>f</sup> <sup>of</sup> <sup>custom</sup> <sub>e</sub>. <sub>Me</sub>m<sup>ber</sup> <sup>banks</sup> <sup>may</sup> <sup>a</sup>l<sup>so</sup> <sup>transf</sup> <sub>ach</sub> <sub>other</sub> <sub>on</sub> <sub>an</sub> o<sup>vern</sup>i<sup>ght</sup> <sup>bas</sup>i<sup>s</sup> <sup>at</sup> <sup>th</sup> <sub>erve</sub> <sub>requ</sub>i<sub>rements</sub>. B<sup>anks</sup> <sup>may</sup> l<sup>end</sup>

Consistent with the above logic, we used steeper cost slopes for underprediction as compared to overprediction—that is, $c ^ { - } > c ^ { + }$ . We fixed $c ^ { + }$ at 1 and manipulated c<sup>–</sup>. In particular, we examined the following cost ratios (c<sup>–</sup> to c<sup>+</sup>): 100:1, 50:1, 20:1, and 10:1. For the sake of completeness, we also examined the cost-insensitive case, where the cost ratio is 1:1.

## Results

Table 2 presents the results of the LR , NN, and M5 models built using four-quarter data. The cost figures shown are the mean costs for each base regression method (LR , NN, or M5) and tuning (without or with) combination; the means were computed by averaging the costs across the five cost ratios (1:1, 10:1, 20:1, 50:1, and 100:1). For each method, the costs go down when the models are tuned. M5 is the best performer, followed by NN and LR .

A $3 \times 2$ factorial analysis of variance (ANOVA) procedure with method (3 values) and tuning (2 values) as the factors and average misprediction cost as the dependent variable was conducted to test for the significance of the effects. The cost ratio variable was used as a covariate to control for its effects on cost. Both the main effects were significant at the 0.001 level. The interaction effect between method and tuning was not significant $( p = 0 . 7 2 3 )$ . We can therefore conclude unambiguously that both method $( F = 8 1 . 8 5 7 )$ and tuning $( F = 3 1 . 8 2 3 )$ have a significant influence on misprediction costs. Pairwise comparisons between the methods indicated that M5 was significantly better than LR and NN $( p < 0 . 0 0 1 )$ , and NN was significantly better than LR $( p < 0 . 0 0 1 )$ ). The significance levels were adjusted for multiple comparisons using the Bonferroni method. Also, we found that the tuned models performed significantly better than the untuned ones $( p < 0 . 0 0 1 )$ .

Table 3 presents results analogous to Table 2 but for models using one-quarter data. The results are similar to those of Table 2, with M5 performing the best, followed by NN and LR . The ANOVA produced similar results with both method $( F = 7 7 . 2 0 9 )$ ) and tuning $( F = 2 5 . 5 0 3 )$ turning out to be significant factors influencing cost $( p < 0 . 0 0 1 )$ ; the interaction effect was not significant $( p = 0 . 8 8 4 )$ . Pairwise comparisons between the methods yielded similar results, with M5 significantly better than LR and NN $( p <$ 0.001), and NN significantly better than LR $( p < 0 . 0 0 1 )$ ). As before, the tuned models performed significantly better than the untuned ones $( p < 0 . 0 0 1 )$ .

Tables 2 and 3 were generated by aggregating over all the cost ratios. Tables 4 and 5 show the costs separately for each cost ratio using a specific method and a tuning condition. For the 1:1 cost ratio, tuning is not needed, so only one column is shown for that ratio. For all other cost ratios, we found that costs always go down with tuning, and M5 yields the lowest cost, followed by NN and LR . The results hold for models based on four-quarter data as well as one-quarter data.

Next, we conducted separate statistical tests for each cost ratio (other than 1:1) to examine the effects of method and tuning. In particular, we conducted paired t-tests on the cost results for the same bank across the two tuning scenarios. That is, each pair represents without-tuning and with-tuning costs for a specific bank. All the tests yielded significant results, both for one-quarter and four-quarter data, indicating that tuning significantly improves cost performance.

Table 2. Results Based on Four Quarters Across All Cost Ratios (N = 150)

<table><tr><td rowspan="2">Method</td><td colspan="2">Cost without tuning</td><td colspan="2">Cost with tuning</td></tr><tr><td>Mean</td><td>Standard deviation</td><td>Mean</td><td>Standard deviation</td></tr><tr><td>LR</td><td>5.582</td><td>4.833</td><td>4.552</td><td>4.222</td></tr><tr><td>NN</td><td>3.890</td><td>3.274</td><td>2.685</td><td>2.268</td></tr><tr><td>M5</td><td>2.669</td><td>2.002</td><td>1.823</td><td>1.015</td></tr></table>

Note: Cost values are on a scale of 10<sup>–2</sup>.

Table 3. Results Based on One Quarter Across All Cost Ratios (N = 80)

<table><tr><td rowspan="2">Method</td><td colspan="2">Cost without tuning</td><td colspan="2">Cost with tuning</td></tr><tr><td>Mean</td><td>Standard deviation</td><td>Mean</td><td>Standard deviation</td></tr><tr><td>LR</td><td>5.756</td><td>3.974</td><td>4.620</td><td>3.121</td></tr><tr><td>NN</td><td>3.295</td><td>2.711</td><td>2.376</td><td>1.419</td></tr><tr><td>M5</td><td>2.859</td><td>2.357</td><td>1.921</td><td>1.440</td></tr></table>

Note: Cost values are on a scale of 10<sup>–2</sup>.

Table 6 summarizes the cost-insensitive performance measures reported by Weka for the base regression methods, including correlation coefficient, relative absolute error, and root relative square error. An important thing to note is that none of these coefficients reflects the asymmetric cost function inherent in the problem at hand. Moreover, there is no unanimity on which method is the best. For example, if fourquarter data is used, LR is the best with respect to correlation coefficient, M5 is the best with respect to relative absolute error, and NN is the best with respect to root relative square error.

## Discussion of Results

In this study, we first argue for a measure to assess the performance of cost-sensitive regression models. Given that R<sup>2</sup>—which is based on quadratic squared errors—and other traditional measures are not appropriate when errors on two sides have unequal consequences, we proposed a measure, average misprediction cost, which weights the two types of errors differently. We developed an algorithm for tuning a trained model based on this misprediction cost. We ran a series of experiments using three types of regression models (LR , NN, and M5) on loan charge-off data from U.S. banks and found that tuning significantly reduced the misprediction cost of these models.

<sub>fects</sub> <sub>of</sub> <sub>Tuning</sub> <sub>on</sub> <sub>Costs</sub> <sub>Using</sub> <sup>Four-Qu</sup>

<table><tr><td rowspan="3">Method</td><td colspan="9">Cost ratio</td></tr><tr><td>1:1</td><td colspan="2">10:1</td><td colspan="2">20:1</td><td colspan="2">50:1</td><td colspan="2">100:1</td></tr><tr><td></td><td>Untuned</td><td>Tuned</td><td>Untuned</td><td>Tuned</td><td>Untuned</td><td>Tuned</td><td>Untuned</td><td>Tuned</td></tr><tr><td>LR</td><td>2.937</td><td>3.613</td><td>3.589</td><td>4.364</td><td>4.152</td><td>6.618</td><td>5.364</td><td>10.375</td><td>6.717</td></tr><tr><td>NN</td><td>1.429</td><td>2.058</td><td>1.958</td><td>2.757</td><td>2.395</td><td>4.855</td><td>3.295</td><td>8.351</td><td>4.347</td></tr><tr><td>M5</td><td>0.859</td><td>1.322</td><td>1.268</td><td>1.836</td><td>1.590</td><td>3.379</td><td>2.285</td><td>5.949</td><td>3.113</td></tr><tr><td colspan="10">Note: Cost values are on a scale of  $10^{-2}$ .</td></tr><tr><td colspan="10">Table 5. Effects of Tuning on Costs Using One-Quarter Data</td></tr><tr><td rowspan="3">Method</td><td colspan="9">Cost ratio</td></tr><tr><td>1:1</td><td colspan="2">10:1</td><td colspan="2">20:1</td><td colspan="2">50:1</td><td colspan="2">100:1</td></tr><tr><td></td><td>Untuned</td><td>Tuned</td><td>Untuned</td><td>Tuned</td><td>Untuned</td><td>Tuned</td><td>Untuned</td><td>Tuned</td></tr><tr><td>LR</td><td>3.311</td><td>3.936</td><td>3.898</td><td>4.630</td><td>4.352</td><td>6.714</td><td>5.267</td><td>10.187</td><td>6.272</td></tr><tr><td>NN</td><td>1.221</td><td>1.751</td><td>1.717</td><td>2.340</td><td>2.113</td><td>4.108</td><td>2.953</td><td>7.054</td><td>3.880</td></tr><tr><td>M5</td><td>0.952</td><td>1.440</td><td>1.388</td><td>1.982</td><td>1.719</td><td>3.607</td><td>2.396</td><td>6.316</td><td>3.151</td></tr><tr><td colspan="10">Note: Cost values are on a scale of  $10^{-2}$ .</td></tr></table>

Table 6. Cost-Insensitive Regression Performance Measures

<table><tr><td rowspan="2"></td><td colspan="2">Training data</td></tr><tr><td>One quarter</td><td>Four quarters</td></tr><tr><td colspan="3">Correlation coefficient</td></tr><tr><td>LR</td><td>0.81</td><td>0.85</td></tr><tr><td>M5</td><td>0.88</td><td>0.81</td></tr><tr><td>NN</td><td>0.86</td><td>0.82</td></tr><tr><td colspan="3">Relative absolute error</td></tr><tr><td>LR</td><td>0.70</td><td>0.64</td></tr><tr><td>M5</td><td>0.56</td><td>0.45</td></tr><tr><td>NN</td><td>1.00</td><td>0.55</td></tr><tr><td colspan="3">Root relative square error</td></tr><tr><td>LR</td><td>0.71</td><td>0.59</td></tr><tr><td>M5</td><td>0.68</td><td>0.59</td></tr><tr><td>NN</td><td>0.92</td><td>0.55</td></tr></table>

Note: Cost values are on a scale of 10<sup>–2</sup>.

One major finding is the relative consistency of the tuning algorithm across the different cost ratios, and also across the different methods. The results of the study clearly demonstrate the effectiveness of the approach we used for tuning the models. The models themselves were generated without explicitly incorporating differential costs during training of the models. That is, the trained models are independent of costs. Only after the models were generated were their predictions adjusted to account for costs. The advantage of the approach is that the models would remain invariant even if the cost ratio or the asymmetric cost function changes. For example, if a linex cost function is used instead of linlin, the trained models would remain the same; the tuning algorithm would then find a different adjustment for minimizing the average misprediction cost. There is therefore no need for banks to develop new models for forecasting loan charge-offs when the cost function or cost ratio changes. A regression model has to be generated only once; when the cost function or ratio changes, the model is tuned by adjusting its prediction.

The performance of the tuning algorithm, along with the resultant costs, remained consistent across the two data sets. Models trained on one-quarter data sets performed nearly as well as those trained on four-quarter data sets. Including more quarters in the training data set increases the sample size and enhances training. On the other hand, older data tends to be less predictive than more recent data. Using just the previous quarter to predict the current quarter is thus adequate and computationally more economic.

In general, we found that M5 provides the least “costly” prediction, as compared to NN and LR . In this case, LR had the worst performance. Moreover, M5 was found to consistently perform better across the different cost ratios as well as across the different data sets (one quarter versus four quarters). This is useful to know, especially when

M5 is very efficient for training purposes; the training time for M5 is much smaller than that for other models such as NN.

## Conclusion and Future Research

In this study, we proposed an ap roach for improving the efficacy of data mining methods for cost-sensitive regression problems. More specifically, we considered the case of predicting loan charge-offs for U.S. banks. The results from a detailed empirical evaluation validate the effectiveness of the proposed approach.

Past research in information systems may have ignored misprediction costs because it is difficult to incorporate those costs into regression models during learning. However, we did not explicitly incorporate costs into any of the regression models that were generated using the training data. Rather, we proposed an algorithm that tunes the output of a trained model post hoc. A major contribution of our research is in making a trained regression model cost sensitive. In addition to the fact that regression models, tuned post hoc, do not have to be built every time the cost function or cost ratio changes, it is also true that they are much simpler and easier to implement than those that explicitly incorporate costs. Such a post hoc tuning method can be easily adopted and used by decision makers for addressing real-world forecasting problems. But an advantage of incorporating costs directly into the models during training is that there is no need to go through the two different steps required for post hoc tuning— model building and model tuning. Future studies could examine the effectiveness of the post hoc tuning approach vis-à-vis the cost-incorporated approach for addressing regression problems.

Sinha and May [18] also proposed an approach for tuning data mining models post hoc, but it was restricted to binary classification problems. Our proposed approach, on the other hand, is for regression problems where the dependent variable is continuous, not categorical. Sinha and May assigned unequal costs to false positives and false nega tives. Similarly, we assigned different costs for underprediction and overprediction, but with the difference that our costs were a function of the prediction error, whereas Sinha and May used fixed costs for the two types of misclassification. A final difference between the two studies is in the method used for tuning the models post hoc. For model tuning, Sinha and May identified optimal decision thresholds of the classifiers by using the results of receiver operating characteristic (ROC) curves. In contrast, we adjust the predictions of regression models using a hill-climbing algorithm. In their study, tuning was accomplished by adjusting a parameter (decision threshold), while in our study, it is achieved by adjusting the output (prediction).

We used the linlin cost function to analyze the efficacy of our approach. Different cost ratios were used, and the results compared to identify how the cost ratios could impact the misprediction costs for any method. The results held across all cost ratios and all three methods; tuning the models based on the proposed algorithm invariably resulted in better performance.

The findings of this study have interesting implications for both research and practice. Our study presents an approach to conducting misprediction cost analysis for regression problems. As discussed earlier, studies in cost-sensitive data mining have been largely confined to classification problems, which typically use misclassification cost as the performance measure. The findings of this research may not only be helpful to bank practitioners trying to forecast charge-offs with the minimum possible associated costs, but also to researchers who could exploit the misprediction cost analysis technique discussed in this paper for future research. Practitioners would find the concepts, ideas, and techniques generated in this study to be attractive and potentially applicable for forecasting applications in other business domains.

In this study, we presented an empirical approach to evaluating and tuning data mining models for regression. While most studies have used $R ^ { 2 }$ as the sole measure, we presented a cost-sensitive approach to tuning and evaluating the methods. This paper opens up several avenues for future research. First, while we evaluated the proposed algorithm on one regression problem with the linlin cost function, future research could be conducted to test our approach using other cost-sensitive regression problems, possibly incorporating different cost functions. Second, while we proposed a post hoc tuning method, other methods that can incorporate cost information during training can be further investigated and compared to post hoc methods. Finally, we used three data mining methods for studying the cost-sensitive regression problem. Future studies could be more comprehensive by including other data mining methods and examining if the results hold across different problem domains.

In summary, our study proposes a new measure, average misprediction cost, which is optimized for a data mining model using a post hoc tuning algorithm. The tuning significantly brought down the costs for all the different models across all cost ratios and data sets, thus validating the efficacy of our approach.

## Notes

1. https://wrds.wharton.upenn.edu.

2. Month in this case represents the quarter ending at that month. For example, March 2002 represents the quarter January 2002–March 2002.

3. Variable number as denoted in the WRDS data set.

## References

1. Anandarajan, M. Profiling Web usage in the workplace: A behavior-based artificial intelligence approach. Journal of Management Information Systems, 19, 1 (Summer 2002), 243–266.

2. Cares, D.C. What’s an adequate loan-loss reserve? ABA Banking Journal, 77, 3 (1985), 41–43.

3. Cavallo, M., and Majnoni, G. Do banks provision for bad loans in good times? Empirical evidence and policy implications. Policy Research Working Paper, World Bank, Washington, DC, 2001 (available at http://econ.worldbank.org/external/default/main? pagePK=64165259&theSitePK=469372&piPK=64165421&menuPK=64166322&entity ID=000094946\_01071204123124).

4. Crone, S.F.; Lessmann, S.; and Stahlbock, R. Utility based data mining for time series analysis: Cost-sensitive learning for neural network predictors. In G. Weiss, M. Saar-Tsechansky, and B. Zadrozny (eds.), Proceedings of the First International Workshop on Utility-Based Data Mining. New York: ACM Press, 2005, pp. 59–68.

5. Davids, L.E. Dictionary of Banking and Finance. Lanham, MD: Rowman and Littlefield, 1978.

6. Domingos, P. Meta cost: A general method for making classifiers cost sensitive. In U. Fayyad, S. Chaudhuri, and D. Madigan (eds.), Proceedings of the Fifth ACM SIGKDD International Conference on Knowledge Discovery and Data Mining. New York: ACM Press, 1999, pp. 155–164.

7. Downes, J., and Goodman, J.E. Dictionary of Finance and Investment. Hauppauge, NY: Barron’s Educational Series, 2006.

8. Elkan, C. The foundations of cost-sensitive learning. In B. Nebel (ed.), Proceedings of the Seventeenth International Joint Conference on Artificial Intelligence. San Francisco: Morgan Kaufmann, 2001, pp. 973–978.

9. Handorf, W.C., and Zhu, L. Credit risk management and bank size. Commercial Lending Review, 20, 1 (2005), 27–34.

10. Henderson, C.C. The economic performance of African-American-owned banks: The role of loan loss provisions. American Economic Review, 89, 2 (1999), 372–376.

11. Jain, B.A., and Nag, B.N. Performance evaluation of neural network decision models. Journal of Management Information Systems, 14, 2 (Fall 1997), 201–216.

12. Keeton, W.R., and Morris, C.S. Why do banks’ loan losses differ? Economic Review, 72, 5 (1987), 3–21.

13. Kim, C.N., and McLeod, R. Expert, linear models, and nonlinear models of expert decision making in bankruptcy prediction: A lens model analysis. Journal of Management Information Systems, 16, 1 (Summer 1999), 189–206.

14. Provost, F.; Fawcett, T.; and Kohavi, R. The case against accuracy estimation for comparing induction algorithms. In J.W. Shavlik (ed.), Proceedings of the Fifteenth International Conference on Machine Learning. San Francisco: Morgan Kaufmann, 1998, pp. 445–453.

15. Quinlan, J.R. Learning with continuous classes. In N. Adams and L. Sterling (eds.), Proceedings of the Fifth Australian Join Conference on Artificial Intelligence. Singapore: World Scientific, 1992, pp. 343–348.

16. Rumelhart, D.E.; Hinton, G.E.; and Williams, R.J. Learning internal representations by error propagation. In D.E. Rumelhart and J.L. McClelland (eds.), Parallel Distributed Processing. Cambridge, MA: MIT Press, 1986, pp. 318–362.

17. Sarkar, S., and Sriram, R.S. Bayesian models for early warning of bank failures. Management Science, 47, 11 (2001), 1457–1475.

18. Sinha, A.P., and May, J.H. Evaluating and tuning predictive data mining models using receiver operating characteristic curves. Journal of Management Information Systems, 21, 3 (Winter 2004–5), 249–280.

19. Sinkey, J.F. Identifying “problem” banks: How do the banking authorities measure a bank’s risk exposure? Journal of Money, Credit and Banking, 10, 2 (1978), 184–193.

20. Sung, T.K.; Chang, N.; and Lee, G. Dynamics of modeling in data mining: Interpretive approach to bankruptcy prediction. Journal of Management Information Systems, 16, 1 (Summer 1999), 63–86.

21. Tam, K.Y., and Kiang, M.Y. Managerial applications of neural networks: The case of bank failure predictions. Management Science, 38, 7 (1992), 926–947.

22. Thompson, R.D., and Basu, A.P. Asymmetric loss functions for estimating system reliability. In D.A. Berry, K.M. Chaloner, and J.K. Geweke (eds.), Bayesian Analysis in Statistics and Econometrics. New York: John Wiley & Sons, 1996, pp. 471–482.

23. Ting, K.M. An instance-weighting method to induce cost-sensitive trees. IEEE Transactions on Knowledge and Data Engineering, 14, 3 (2002), 659–665.

24. Varian, H.R. A Bayesian approach to real estate assessment. In S.E. Fienberg and A. Zellner (eds.), Studies in Bayesian Econometrics and Statistics: In Honor of Leonard J. Savage. Amsterdam: North-Holland, 1974, pp. 195–208.

25. Witten, I.H., and Frank, E. Data Mining: Practical Machine Learning Tools and Techniques, 2d ed. San Francisco: Morgan Kaufmann, 2005.

26. Zellner, A. Bayesian estimation and prediction using asymmetric loss functions. Journal of American Statistics Association, 81, 394 (1986) 446–451.

27. Zhao, H. A multi-objective genetic programming approach to developing pareto optimal decision trees. Decision Support Systems, 43, 3 (April 2007), 809–826.

28. Zhou, L.; Burgoon, J.K.; Twitchell, D.P.; Qin, T.; and Nunamaker, J. A comparison of classification methods for predicting deception in computer-mediated communication. Journal of Management Information Systems, 20, 4 (Spring 2004), 139–165.

## Appendix: Propositions

## Proposition 1

The averag e misprediction cost of an adjusted reg ression model, θ(δ), is a convex function with regard to the amount of adjustment, δ, if the cost function, C(e), is a convex function with regard to prediction error, e.

## Proof

Since the adjustment, δ, is applied on a regression model, f, after the model has been trained, the prediction of f on a given problem instance, $f ( x _ { i } ) , i = 1 , 2 , . . . , N ,$ is constant irrespective of δ. The prediction error of f on a problem instance, $f ( x _ { i } ) - y _ { i } , i = 1 , 2 .$ N, is therefore also constant.

If the cost function, C(e), is convex with regard to prediction error, e, the misprediction cost of the adjusted model, $f ^ { \prime } ,$ , on a problem instance, $C ( \delta + ( f ( x _ { i } ) - y _ { i } ) ) , i = 1$ $2 , . . . , N ,$ is convex with regard to the adjustment, δ. The summation

$$
\sum_ {i = 1} ^ {N} C \left(\delta + \left(f (x _ {i}) - y _ {i}\right)\right)
$$

is then convex with regard to δ. The average misprediction cost of the adjusted model,

$$
\theta (\delta) = \frac {1}{N} \sum_ {i = 1} ^ {N} C (\delta + (f (x _ {i}) - y _ {i})),
$$

is therefore convex with regard to δ. Q.E.D.

## Proposition 2

The worst-case time complexity of the performance tuning algorithm listed in Figure 3 is O([log n]<sup>2</sup>), assuming there are n possible $\delta$ values that need to be evaluated by a brute force algorithm.

## Proof

It is apparent that most of the computation time for finding the optimal δ value is spent on the hill-climbing procedure (lines 6 to 7), while the time spent on the initial determination of the climbing direction (lines 2 to 5) is negligible. The training of the original regression model (line 1) is out of the scope of the performance tuning.

The entire hill-climbing procedure consists of several search phases (the outer loop). During each search phase (an iteration of the outer loop), several trials are made (the inner loop, lines 6.3 to 6.4). The stride of each subsequent trial doubles that of the previous trial (line 6.3.3). In the worst case, the last trial reaches the outermost boundary of the current search phase. Similar to binary search, the number of trials during the first search phase is at most log n, assuming there are n possible $\delta$ values that need to be evaluated by a brute force algorithm. Each search phase reduces the search range by at least half. Again, similar to binary search, the number of search phases is also at most $\log _ { 2 } n .$ . The total number of trials over all search phases is at most

$$
\log_ {2} n + \log_ {2} n / 2 + \dots + 1.
$$

The worst-case time complexity of the hill-climbing procedure is therefore

$$
\begin{array}{l} O (\log_ {2} n + \log_ {2} n / 2 + \ldots + 1) \\ = O ([ \log_ {2} n ] [ \log_ {2} n + 1 ] / 2) \\ = O ([ \log_ {2} n ] ^ {2}) \text {(by discarding constant and lower - order terms)} \\ = O ([ \log n ] ^ {2}) \text {(by discarding the base of log)}. \end{array}
$$

Q.E.D.
