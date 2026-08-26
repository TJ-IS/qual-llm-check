---
otero_id: 25367
otero_key: "WVRFA8CQ"
title: "Evaluating and Tuning Predictive Data Mining Models Using Receiver Operating Characteristic Curves"
authors: "ATISH P. SINHA; JERROLD H. MAY"
year: "2004"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2004.11045815"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Evaluating and Tuning Predictive Data Mining Models Using Receiver Operating Characteristic Curves

ATISH P. SINHA & JERROLD H. MAY

To cite this article: ATISH P. SINHA & JERROLD H. MAY (2004) Evaluating and Tuning Predictive Data Mining Models Using Receiver Operating Characteristic Curves, Journal of Management Information Systems, 21:3, 249-280

To link to this article: http://dx.doi.org/10.1080/07421222.2004.11045815

![](/api/attachments/WVRFA8CQ/fulltext/images/05145fa12ff442966a359f209680613f9def82b02f32345245a1643c63e8f197.jpg)

Published online: 08 Dec 2014.

![](/api/attachments/WVRFA8CQ/fulltext/images/5fc27a4a14589322a19489aced143d18684c5c6beaa7e1be936c1b7386e09c20.jpg)

Submit your article to this journal

![](/api/attachments/WVRFA8CQ/fulltext/images/598108656a9b0e594c02548ef4d72862319a9cc839a4cd279582e286cf961e20.jpg)

Article views: 21

![](/api/attachments/WVRFA8CQ/fulltext/images/a33b1b4f3f73534adfbfc9804b3925a0ef1d42b949b7d0d7926be87f0c374428.jpg)

View related articles

![](/api/attachments/WVRFA8CQ/fulltext/images/ebbc4b9c410836a0e507dca3a1fd309f8ed51960ef2a4c52cd5dfa074ba59d36.jpg)

Citing articles: 1 View citing articles

# Evaluating and Tuning Predictive Data Mining Models Using Receiver Operating Characteristic Curves

ATISH P. SINHA AND JERROLD H. MAY

ATISH P. SINHA is an Associate Professor of MIS at the School of Business Administration, University of Wisconsin–Milwaukee. He earned his Ph.D. in Business, with a concentration in Artificial Intelligence, from the University of Pittsburgh. His current research interests are in the areas of data mining, data warehousing, and object-oriented software engineering. His research has been published in several journals, including Communications of the ACM, IEEE Transactions on Software Engineering, Information Systems Research, International Journal of Human-Computer Studies, and Journal of Management Information Systems. Professor Sinha is a member of ACM, AIS, and INFORMS.

JERROLD H. MAY is a Professor of Decision Sciences and of Intelligent Systems at the Katz Graduate School of Business, University of Pittsburgh, and is also the Director of the Artificial Intelligence in Management Laboratory there. His current work focuses on modeling, planning, and control problems, the solutions to which combine management science, statistical analysis, and artificial intelligence. Dr. May’s work has been published in journals such as Communications of the ACM, Information Systems Research, IEEE Transactions on Systems, Man and Cybernetics, European Journal of Operational Research, Mathematical Programming, and Operations Research. He is a member of AAAI, ACM SIGKDD, and INFORMS.

ABSTRACT: In this study, we conduct an empirical analysis of the performance of five popular data mining methods—neural networks, logistic regression, linear discriminant analysis, decision trees, and nearest neighbor—on two binary classification problems from the credit evaluation domain. Whereas most studies comparing data mining methods have employed accuracy as a performance measure, we argue that, for problems such as credit evaluation, the focus should be on minimizing misclassification cost. We first generate receiver operating characteristic (ROC) curves for the classifiers and use the area under the curve (AUC) measure to compare aggregate performance of the five methods over the spectrum of decision thresholds. Next, using the ROC results, we propose a method for tuning the classifiers by identifying optimal decision thresholds. We compare the methods based on expected costs across a range of cost–probability ratios. In addition to expected cost and AUC, we evaluate the models on the basis of their generalizability to unseen data, their scalability to other problems in the domain, and their robustness against changes in class distributions. We found that the performance of logistic regression and neural network models was superior under most conditions. In contrast, decision tree and nearest neighbor models yielded higher costs, and were much less generalizable and robust than the other models. An important finding of this research is that the models can be effectively tuned post hoc to make them cost sensitive, even though they were built without incorporating misclassification costs.

KEY WORDS AND PHRASES: binary classification, credit evaluation, data mining, decision analysis, misclassification costs, performance evaluation and tuning, predictive models, ROC curves.

THE GOAL OF PREDICTIVE DATA MINING is to learn decision criteria for predicting the outcomes of new cases based on the known outcomes of past cases [11, 28]. There are two types of predictive modeling: classification and value prediction (regression). Whereas a classification model classifies a new case into one of a finite set of predetermined categories (e.g., low risk, high risk), a value prediction model estimates the value of a continuous numeric variable (e.g., product sales) for a new case.

Classification accuracy has been the most commonly used performance measure for evaluating predictive data mining methods. The focus has been on finding the method that generates the lowest number of errors. In many real-world situations, however, different types of misclassification have unequal costs and, therefore, using accuracy as the performance criterion, under the assumption of equal costs, is not valid. In problems such as credit scoring, bankruptcy prediction, insurance underwriting, and fraud detection, misclassification costs are typically not equal. In such situations, the focus should be on minimizing overall misclassification cost, not on minimizing misclassification error rates [7, 20]. Hand et al. underscore this point:

Error rate treats the misclassification of all objects as equally serious. However, this is often (some argue almost always) unrealistic. Often, certain kinds of misclassification are more serious than other kinds. For example, misdiagnosing a patient with a curable but otherwise lethal disease as suffering from some minor illness is more serious than the reverse. In this case, we may want to attach costs to the different kinds of misclassification. In place of simple error rate, then, we seek a model that will minimize overall loss. [11, p. 361]

Decision analysis allows us to make classifiers cost sensitive. In a binary classification problem, a specific instance or case can belong to one of two classes: positive or negative. Tests are conducted to detect if a case is positive (e.g., breast cancer, bankrupt firm, bad credit, etc.) or negative. A false positive results when the test results are positive, but the case does not actually belong to the positive class. A false negative results when the test is negative, but the case actually belongs to the positive class. For such problems, it is important for a classifier to correctly identify true positives and true negatives; the objective should be to minimize overall misclassification cost.

We employ decision analysis and receiver operating characteristic (ROC) curves to examine the performance of five data mining methods on two binary classification problems from the credit evaluation domain. An ROC curve plots the true positive rate of a classifier against its false positive rate, and those values can be used to compute the expected cost of the classifier for a given decision threshold. An ROC curve visually depicts classifier performance across a spectrum of decision thresholds.

Unfortunately, costs are often difficult to estimate or are unknown. In such a case, “an alternative strategy is to integrate over all possible values of the ratio of one cost to the other” [11, p. 361]. The integration is provided by the area under the curve (AUC) measure, which can be used to compare the performance of data mining methods at an aggregate level.

In this study, we first use ROC curves and AUC to examine the performance of five data mining methods—neural network (NN), logistic regression (LR), linear discriminant analysis (LDA), decision tree (DT), and case-based reasoning (CBR)—in making decisions on auto loans.

We next examine if the results are scalable to another application in the credit evaluation domain. We develop predictive models using the German credit data set, which is larger in size and has been employed extensively in past research. We use all the methods that were used for auto loans except case-based reasoning, because the limited expertise needed to build such a system was not available. Instead of casebased reasoning, we used the k nearest neighbor (kNN) method, which, like casebased reasoning, is a distance-based method, but uses a statistical distance measure to identify the nearest neighbors. As before, we use the AUC metric to evaluate the methods.

When the cost for each type of misclassification and prior probabilities are known, we can use the points on an ROC curve to compute the expected cost across the spectrum of thresholds. Using the German credit data set, we describe how we can empirically determine the optimal threshold for a given situation and use that threshold to tune a model. We evaluate the performance of the tuned models with respect to expected misclassification cost across different combinations of prior probabilities and costs. We next examine the generalizability of the five methods by assessing whether the results achieved during training the models map to unseen test sets. We also analyze the robustness of the methods against changes in assumptions on prior probabilities.

Our study presents an empirical approach to evaluating predictive data mining models using a variety of measures, with an emphasis on misclassification cost. It presents an approach for tuning the models post hoc to make them cost sensitive. The findings of the study have important implications for both research and practice in the field.

## Background

SEVERAL DATA MINING METHODS ARE AVAILABLE for classification problems. But most studies limit the choices to a few tried and tested methods. Weiss and Indurkhya [28], for example, review some of the strongest and most widely used prediction methods by categorizing them based on the type of solutions they provide: math, logic, and distance. They review linear discriminant analysis, neural networks, and nonlinear statistical regression under math solutions, kNN under distance solutions, and decision trees/rules under logic solutions.

Several prior studies have empirically examined the performance of data mining methods on binary classification problems. In the business domain, the areas of application include bankruptcy prediction [16, 25], management fraud detection [8], new venture success prediction [13], and credit classification [15].

The data mining methods examined by prior research include discriminant analysis, logistic regression, kNN, neural networks, decision tree/rule induction, and genetic algorithms. In terms of performance, there seems to be no universal agreement on which method is best, though, in most cases, neural networks performed better than other methods.

Tam and Kiang [25] compared neural networks, discriminant analysis, logit, kNN, and ID3 (decision tree/rule induction) methods and found that neural networks produced more accurate bankruptcy predictions than the other four. The data sample for the study consisted of bank data one year and two years prior to bankruptcy. For training the models, balanced samples (equal number of failed and nonfailed banks) were used for each period. The authors first compared the accuracy of neural networks with discriminant analysis models on the training data using different prior probabilities and misclassification costs. The original back-propagation algorithm for neural networks was modified to include prior probabilities and misclassification costs. For both time periods, neural networks performed better than discriminant analysis models in terms of resubstitution risk across all combinations of prior probabilities and misclassification costs.

Tam and Kiang then compared all the five methods based on an equal cost assumption, because logit, kNN, and ID3 cannot explicitly include expected misclassification costs. They tested the models on a separate holdout sample and found that, in the oneyear period, neural networks performed the best with respect to type II and total errors, followed by discriminant analysis, logit, ID3, and kNN. For the two-year period, however, logit was the best, followed by neural networks, discriminant analysis, kNN and ID3. Because a random train-and-test partition may be biased, the authors subsequently used the jackknife method, which provides unbiased estimates for the probability of misclassification. This method involves leaving one case out at a time from the training set and then testing the trained model on that case. For both time periods, neural networks performed the best, followed by discriminant analysis, logit, ID3, and kNN.

Fanning and Cogger [8] found that neural networks performed better than traditional statistical methods in detecting management fraud. Jain and Nag [13] found that neural networks consistently outperformed logit models in predicting success for new ventures. In the bankruptcy prediction domain, Kim and McLeod [16] developed four data mining models—discriminant analysis, logistic regression, ID3, and neural networks—based on human experts’ judgment, not on actual outcomes, and found that all the models predicted the actual outcomes quite well. But for modeling valid nonlinear strategies, the nonlinear models (ID3 and neural network) performed better than the two statistical models.

Using decision trees, Sung et al. [24] developed bankruptcy models suitable for both normal and crisis situations. The decision tree models were evaluated for predictive accuracy, using discriminant analysis as a benchmark. They found that decision trees were slightly more accurate than discriminant analysis models under normal conditions, and quite better under crisis conditions. Recognizing that misclassification of bankrupt corporations as nonbankrupt is a more serious mistake than the opposite, they also analyzed the sensitivity of the models—that is, the proportion of correctly predicted cases among the actual bankrupt cases. However, instead of tuning a model to account for the differences in misclassification, they used a cutoff that maximized the overall accuracy.

Zhu et al. [32] compared the classification accuracy of three data mining methods—neural networks, inductive learning (C4.5), and rough sets—in detecting network intrusion. The study also examined the effects of two other factors—data proportion and data representation—on performance. Two data representation formats (binary and integer) and two data proportion schemes (balanced and unbalanced) were used. Data mining method had the maximum influence on performance. Rough sets performed the best, followed by neural networks and inductive learning. Performance using balanced data sets was significantly better than that with unbalanced data sets. Data representation did not have any significant influence on classification accuracy.

Doumpos et al. [5] investigated the applicability of a new discrimination method called MHDIS (multigroup hierarchical discrimination) in credit risk assessment. The method is based on the multicriteria decision aid methodology and employs a hierarchical discrimination procedure. The authors compared the method with discriminant analysis, logit, and probit. The total error was computed as the average of the type I and type II error rates. MHDIS produced low error rates in both training and holdout samples; type I error was significantly higher than type II error. However, the authors did not incorporate the different misclassification costs associated with the two types of errors. Both discriminant analysis and probit yielded consistently higher error rates than MHDIS, whereas logit’s performance was similar to that of MHDIS for the training sample. However, for the holdout sample, logit’s performance was inferior.

There have been few studies examining the performance of classifiers under unequal costs for different types of misclassification. Among those studies, the focus has been on examining a single method (e.g., [1]) or on comparing two methods (e.g., [25]). Berardi and Zhang [1] investigated the effect of unequal misclassification costs on neural networks for a three-group classification problem. Fuller and Kohers [10] used misclassification costs to obtain a decision rule for a discriminant analysis model built for predicting financial failure. As noted before, Tam and Kiang [25] compared the performance of neural networks and discriminant analysis models across different misclassification cost ratios.

Chung and Gray [4] identify several issues that need to be addressed, including quality of the discovered knowledge, whether the same method produces the same results, whether different methods are suitable for different domains, and factors affecting performance. According to Chung and Gray, “How the quality of an algorithm is assessed, its robustness, scalability, preprocessing, generalizability, and reliability are critical issues. The way model performance is measured is an important consideration” [4, p. 15].

Elkan [7] reviews the problem of optimal learning and decision-making under different misclassification costs. Based on the investigation of a two-class problem, he concludes that changing the balance of positive and negative examples has little effect on Bayesian and decision tree classifiers. For applying any of those methods, Elkan’s recommendation is to learn the classifiers from the training data as given, and then determine optimal decision thresholds empirically.

Researchers in the field of machine learning have started using ROC curves for analyzing a classifier’s performance [2, 20, 27]. ROC curves, which were originally used in signal detection theory, have proved to be useful for visualizing a classifier’s performance [9].

Bradley [2] describes the use of the area under the ROC curve (AUC) as a single measure of classifier performance. He presents the results of an experimental study using AUC as a measure for evaluating six learning algorithms on six medical diagnostics data sets. The use of AUC is justified based on the fact that it is invariant with respect to the decision threshold selected and prior probabilities, and could be extended to incorporate cost/benefit analysis.

Arguing that “accuracy maximization is not an appropriate goal for many of the real-world tasks,” Provost et al. use ROC analysis to “investigate whether an algorithm that generates high-accuracy classifiers is generally better because it also produces low-cost classifiers for the target cost scenario” [20, pp. 446–447]. They investigate whether a dominating model exists in ROC space; if such a model does not exist, none of the models under investigation can be considered to be best under all target scenarios.

## Objectives of the Study

THE INCREASING RELIANCE OF FIRMS on data mining methods raises the issue of how well those methods actually perform. For credit evaluation problems, we know whether a given credit application is good or bad. That outcome could then be used to examine the predictions made by the methods under investigation. However, unequal costs and prior probabilities of the two classes should be factored in before making the assessments. The focus of the study is on examining how well the data mining methods perform in terms of minimizing misclassification cost. As noted before, the emphasis of prior studies has been on minimizing misclassification error rates (maximizing accuracy), which is not a realistic performance measure to use in many situations. The methods we compare include three math solutions (linear discriminant analysis, neural network, and logistic regression), one distance solution (case-based reasoning/kNN), and one logic solution (decision tree).

Because the costs are often difficult to determine or are unknown, we first assess the performance of the classifiers by integrating their performance across the spectrum of thresholds. For that purpose, we utilize ROC curves, which represent the performance of classifiers with variable thresholds. The AUC measure is used to conduct pairwise comparisons of the models so that the best models can be identified.

We address the issue of scalability by using two data sets from the credit evaluation domain: auto loan and German credit. We build models using the data mining methods for the auto loan data set and examine if the results scale up to the larger German credit data set.

Another objective of our study is to tune the classifiers for optimal performance. Most of the prior studies have used a default threshold (usually 0.5) for classification, without any attention to tuning. Because we are dealing with unequal costs and priors, performance is measured in terms of expected misclassification cost, rather than simple error rates. We assess the generalizability of the classifiers by testing empirically if the effects of tuning the model on training data transfer effectively to independent test data. For each model, we examine if there is a significant difference in expected cost across the two sets. We also examine the fit between the cutoffs derived from the training results with those derived from the test results.

We compare the performance (expected cost) of the models across a wide range of cost–probability ratios. For analyzing classifier performance, we used 5 different costs for a false negative (classifying bad credit as good) and 5 different prior probabilities for the positive class (bad credit), resulting in 25 cost–probability ratios. The expected cost of each classifier (see below) was analyzed across these ratios. For each ratio, we can therefore identify the model with the minimum expected cost.

The final objective is to evaluate the robustness of the models. Our goal is to explore if slight changes in assumptions relating to prior probabilities result in significant changes in the outcome. The intent is to test which classifiers are sensitive to such changes in assumptions and which are more robust.

## Credit Evaluation Applications

THE PROBLEM THAT WE STUDY FIRST is that of bank loans for automobiles. A real data set was obtained from a bank for our study. We also interviewed an expert with over ten years of lending experience to identify the main concepts of the domain. The concepts we identified can be grouped into two categories: application attributes and credit bureau attributes.

Attributes of the loan application itself are called application attributes. Examples include years in current residence, years in previous residence, monthly income, monthly payments, and so on. Values of some of the application attributes are derived from the values of other attributes. For example, “debt-to-income ratio” is calculated by dividing the monthly payments by monthly gross income, and “percentage-tofinance” is calculated by dividing the amount to finance by the auto price.

Credit bureau attributes are not directly present in the application itself, but come from the Credit Bureau Report. The “number of satisfactory trades” attribute, for example, represents the number of satisfactory trades that the applicant has had. A “trade line” stores the vital statistics of each instance of borrowing. For example, an installment loan obtained by the applicant would be listed on the credit report and the payment history would continue to be updated each month, or sometimes less frequently. A new trade line is added only when the borrower obtains a different loan.

Trades with sufficient payment history get rated on a scale of 1 to 9. Satisfactory trades are defined as those for which all payments were received in a timely manner; that is, none of them was received more than 29 days past the due date. Such loans receive a rating of 1, the best rating possible. If one of the payments for a loan was late by more than 29 days, but by less than 60 days, the loan would be classified as “minor” with a rating of 2. A loan for which any of the payments was received 60 days or more past the due date is classified as “major” with a rating of 3 or more, depending on how bad the payment history is. If the loan was “charged off,” then it gets a rating of 9. The “worst rating” attribute corresponds to the highest rating among all the trade lines in the applicant’s credit report.

A balanced sample of 220 auto loan cases was used for the study; 110 were “approved goods,” and the other 110 were “approved bads.” Each case represents an approved loan with more than two years of payment history, and includes loan application and credit history data. The two categories are defined as follows: (1) approved good—the bank considers a case as “approved good” if the loan was approved and it has a good payment history, and (2) approved bad—the bank considers a case as “approved bad” if the loan was approved, but the payment history is bad.

The auto loan data set has 11 input attributes, 10 of which are numeric and 1 (bankruptcy) binary. The output variable is binary, with 0 indicating a bad loan and 1 a good loan.

The second application we focus on in this study is the German credit data set from the well-known Statlog project (see [19]). The data set has the following input attributes:

Continuous numeric: duration of loan in months amount of credit installment rate as percentage of disposable income number of years applicant has lived at current address age of applicant number of credits applicant has at this bank number of applicant’s dependents Binary: applicant has telephone applicant is a foreign worker Unordered categorical: existing checking account balance purpose of loan savings accounts/bonds balance personal status and gender other assets

other lines of credit housing Ordered categorical: loan repayment history years employed at current job loan guarantors applicant’s job type

The output variable, credit risk, is binary, with 0 indicating that the applicant’s risk class is bad and 1 indicating that it is good. The goal of a classifier, then, is to predict if the credit risk of the applicant is good or bad.

The data set has several categorical/symbolic attributes, out of which seven are unordered. The binary and ordered categorical attributes were coded as integer. Unordered categorical attributes were coded as dummy variables. For example, the “purpose of loan” attribute, which has 10 possible values (0 = new car, 1 = used car, 2 = furniture/equipment, . . . , 10 = other), will have 10 corresponding dummy variables, with 0 indicating absence and 1 indicating presence of a given value.

The German credit data set has 1,000 cases, with 700 being good risk and 300 being bad. In the cost matrix provided with the original data set, the cost of misclassifying a bad credit case as good was five times more than that of misclassifying a good credit case as bad.

## Model Development

IN THIS SECTION, WE DESCRIBE HOW WE DEVELOPED models for the two applications, auto loan and German credit, using the five methods. The 220 loan cases in the auto loan data set were divided randomly into five mutually exclusive partitions of 44. Each partition was used as a test set, while the remaining 176 cases were used to develop models for the five methods. For each method, therefore, five model instances were generated corresponding to the five partitions. This approach is known as 5-fold cross-validation and is described later in more detail.

Because the German credit data set was much larger, we used the train-and-test method to evaluate the performance of the classifiers. There were 700 cases used for training, and the remaining 300 cases were reserved for testing.

## Case-Based Reasoning

The case-based reasoning model for the auto loan application was developed in Visual Basic; it stores its cases in an Access database. To make a decision on a new case, it first uses a serial index to ensure that the retrieved (base) cases match the general characteristics of the target case. This is similar to an exclusion step, which discards those cases that can be predicted to be not useful based on their differences from the target case [17]. The attributes used in the serial index were bankruptcy, number of major trades, and debt-to-income ratio. An exact match was required for bankruptcy, and ranges were specified for the other two attributes. After retrieving cases using the serial index, the case-based reasoning model uses a variant of the nearest neighbor matching method to compute the distance of each base case from the target case and then identifies the one having the minimum distance as the nearest neighbor [23].

The matching method calculates a “distance” score for each of the cases retrieved using the serial index. The distance score reflects how close a base case is to the target, with smaller distances indicating better matches. The case-based reasoning model first scores distance individually for each attribute on a 0-to-5 scale, with 0 signifying no difference and 5 maximum difference. For some of the attributes, the algorithm uses multiple scales to handle regions that are more sensitive to changes in attribute values than others.

The expert weighted the attributes on a scale of 1 to 3 based on importance with respect to the lending decision. Attributes that are very critical, such as debt-to-income ratio and number of major trades, were assigned a weight of 3, and less important attributes were assigned lower weights. After finding the individual distances, the model computes a weighted average of those distances to find the overall distance based on the following formula:

$$
d = \frac {\sum_ {i = 1} ^ {n} w _ {i} * d i s t _ {i} (\text { target,   base })}{\sum_ {i = 1} ^ {n} w _ {i}},
$$

where d is the distance of base from target, w is the weight of attribute i; and dist (target, base) is the distance of base from target on attribute i. For example, if the debt-toincome ratio for the target case is 0.21 and that for the base case is 0.27, the difference of 0.06 in that range translates to a distance of 2. Because the weight of the debt-toincome attribute is 3, the weighted distance is 6. The weighted distances for the other attributes are determined in a similar manner and used to compute the overall distance.

After computing the distance for each retrieved case, the case-based reasoning model identifies those that are within a distance less than or equal to 25 from the target as neighbors. If the case-based reasoning model does not find any neighbors within the cutoff distance, it identifies the one that is nearest to the target case, irrespective of how large the distance may be, and uses that for making the decision. Next, it computes a certainty factor, which is equal to the ratio of the number of approved goods to the number of neighbors.

## k Nearest Neighbor

Another distance-based method, kNN, was used on the German credit data set. Nearest neighbor methods assign a new case to the majority class among the k closest cases in the training set [11]. As with case-based reasoning, the objective is to identify the cases that are similar to the new case and then classify the new case based on the outcome of the majority of its neighbors. There are three components of a nearest neighbor solution: the set of stored cases, the distance metric used to compute the distance between cases, and the value of k [28].

Many applications use the Euclidean distance metric. If Y is the input vector corresponding to the new case, and X is the input vector for a stored case, then the squared Euclidean distance between them is $\Sigma _ { j } ( X _ { j } - Y _ { j } ) ^ { 2 }$ , where $j = 1 , 2 , . . . , n$ represents an input variable. We used the Weka data mining package [31] and selected the Euclidean distance metric to develop the kNN model. Because the input variables are measured in different units, implying that they will be weighted differently, we normalized the inputs before computing distance. We used a value of 3 for k, because that tended to produce the best results on independent test sets.

## Neural Network

A neural network consists of several processing elements or neurons. The processing elements are arranged in a number of layers, with the first and last layers being known as input and output layers, respectively. Intermediate layers are known as hidden layers. A processing element sums the input values it receives, and converts the sum to an output value through a transfer function. When the output value exceeds a threshold level, the processing elements are activated and the output is transferred to the processing elements of the next layer through connection weights.

The learning or training of a neural network consists of presenting samples of historical data randomly a large number of times. For each sample case, the error in the output is analyzed and fed back to the inputs to adjust the weight parameters that caused the error. The weights are then adjusted in a user-determined epoch, which is the number of trials before the adjustment takes place.

We used a three-layered back-propagation network with one hidden layer for the auto loan problem. In a three-layered neural network consisting of n input nodes, a hidden layer with k nodes, and a single output node, the signal received by a hidden layer node from the input layer is of the form

$$
I _ {j} = \sum w _ {j i} X _ {i}, \quad i = 1, \dots , n, \quad j = 1, \dots , k,
$$

where $X _ { i }$ is the input signal from node i and $w _ { j i } ,$ is the weight of the connection between input node i and middle layer node j. The combined input $I _ { j }$ is then modified by a transfer function $f ( \rho )$ to yield

$$
Y _ {j} = f \left(I _ {j}\right) = f \left(\sum w _ {j i} X _ {i}\right),
$$

where $Y _ { j }$ is the output of node j. The output value from each hidden layer node j becomes an input to the output node. A transfer function is applied similarly to the weighted sum of the inputs to generate an output for the network. We used the sigmoid transfer function,

$$
f (z) = \frac {1}{1 + e ^ {- Z}},
$$

which produces a value between 0 and 1.

A back-propagation network learns by updating the connection weights based on information propagated back through the network. The aim is to minimize a global error function $E ,$ which is based on the squared difference between the desired output and the actual output, at the output node. The neural network models were developed using the Neural Works Professional II/PLUS software package. The normalize cumulative delta learning rule was selected for the back-propagation algorithm.

For the auto loan problem, we developed a network with 11 input nodes, 1 for each domain attribute, and 1 output node representing the lending decision. We used three nodes in the hidden layer. We set the learning rate and momentum values at relatively low values in the initial stages, and reduced them progressively to much lower values as training proceeded. To compensate for the resultant slow learning, a high learning cycle of 120,000 iterations was used.

Using 5-fold cross-validation meant that we had to develop five neural network model instances. The average RMS (root mean square) error for the five neural network instances on completion of the training was 0.1762. Because we used the sigmoid transfer function, the outputs varied between 0 and 1.

For the German credit problem, we recoded the unordered categorical attributes into dummy variables, resulting in 48 input attributes. The back-propagation network had one hidden layer with three nodes, and one output node representing the risk class. The network was trained in 50,000 iterations. The transfer function and other parameters were the same as those used for the auto loan application. The RMS error on the training set was 0.1886.

## Decision Tree

A decision tree consists of nodes and arcs, in which the nodes are of three types: the root of the tree; terminal nodes, indicating a selected class; and “decision” nodes that specify a test to be carried out as part of the process of successively separating a group into two or more subgroups. The arcs indicate the sequence by which the splits are to be carried out. The subgroups resulting from carrying out a test are intended to be more homogeneous than was their union before the test was performed.

Quinlan’s ID3 algorithm [21] used an entropy-based “gain” criterion, an information theory construct, to split the data using values of a single attribute at a time. ID3’s behavior was refined in C4.5 [22]. The latest version is C5.0, which is more efficient and accurate than C4.5 for generating rule sets. For this study, we employed See5, the Windows version of the C5.0 algorithm.

See5 constructs a decision tree in two phases. First, it builds a large tree to fit the data closely. Next, it prunes the tree by removing parts that are predicted to have a relatively high error rate. For both data sets, we used the default value of 25 percent as the pruning certainty factor. Smaller values would have resulted in more pruning of the initial tree, while larger values would have resulted in less pruning. To constrain the degree to which the initial tree can fit the data, See5 provides an option to specify the minimum number of training cases that must follow at least two of the branches at every branching point. We used the default value of 2 cases as the minimum for both data sets.

In See5, unordered categorical attributes are represented as discrete values. There was no need, therefore, to introduce any dummy variables. See5 also supports explicit representation of ordered categorical attributes.

## Logistic Regression

Logistic regression is a statistical method that is frequently employed for two-category classification problems. In its general form, a logistic regression model specifies as output the probability of an event occurring as

$$
\operatorname{Prob} (\text { event }) = \frac {1}{1 + e ^ {- Z}},
$$

where Z is the linear combination

$$
Z = b _ {0} + b _ {1} X _ {1} + b _ {2} X _ {2} + \ldots + b _ {n} X _ {n}.
$$

The relationship between the independent variables $X _ { 1 } , X _ { 2 } , . . . . , X _ { n }$ and the probability of the event is nonlinear. The parameters of the model are estimated from the data using the maximum-likelihood method. The method selects the coefficients $b _ { 0 } , b _ { 1 }$ $b _ { 2 } , . . . , b _ { n }$ such that the observed results are most likely. For the bank lending problem, the event is a loan turning out to be good, so the output of the model for a given case is interpreted as the probability that the loan would prove to be good if approved.

We employed the SPSS for Windows to develop models for the two applications. We chose the backward stepwise elimination method, using the likelihood ratio test for removal of variables. The model is estimated by eliminating each variable in turn and considering the change in log likelihood. The likelihood ratio—that is, the likelihood of the reduced model divided by the likelihood for the full model—is used to test the null hypothesis that the coefficients of the variables removed are 0. If the significance level of the test exceeds a cutoff value, the variable is deleted. The cutoff probability for removal of a variable was set at 0.10 and that for entry into the model was set at 0.05. For the German credit data set, the unordered categorical attributes were coded as categorical covariates.

## Linear Discriminant Analysis

Discriminant analysis, first introduced by Fisher, is the statistical technique most commonly used to distinguish among several mutually exclusive groups and to predict group membership for new cases whose group membership is unknown [14]. A linear discriminant function is optimal if each group is a sample from a multivariate normal population, and if the population covariance matrices are all equal.

In discriminant analysis, a linear combination of the independent variables is formed and it serves as the basis for assigning observations to groups. The information contained in the n independent variables is summarized in a single index, the weighted average of the independent variables, the values of which are used to distinguish the groups from each other. The weights are estimated so that they result in the “best” separation among the groups.

The linear discriminant equation is similar to multiple linear regression, except for the dependent variable. As in regression, sample information is used to compute $b _ { 0 }$ through $b _ { n } .$ The bs are chosen so that the values of the discriminant function differ as much as possible between the groups, or so that for the discriminant scores, the ratio of between-groups sum of squares to within-groups sum of squares is maximized. The bs are computed by first finding the mean values for each of the independent variables in each group, and the sample covariance matrix, under the assumption that the groups all have the same covariance matrix. The bs are given by the differences between the group means, appropriately weighted by the covariance matrix.

We employed the discriminant function in SPSS to develop linear discriminant analysis models for both applications. As in logistic regression, we used the stepwise method for eliminating variables, with probability for removal set at 0.10 and for entry at 0.05. In the SPSS discriminant analysis function, prior probabilities can be estimated from the sizes of the different groups or can be assumed to be equal. Because the auto loan data set is balanced, the two options are equivalent. For the German credit data set, we assumed equal prior probabilities; the unordered categorical attributes were coded as dummy variables.

## Evaluation Methodology

WE EVALUATE THE PERFORMANCE OF the five data mining methods with a focus on minimizing misclassification cost. The methods are assessed based on different criteria, including AUC, misclassification cost, generalizability, scalability, and robustness. We now describe the evaluation process in detail.

The train-and-test method, also known as the holdout method, is commonly used for estimating model performance. The sample is split into two independent sets; one is used for training the model, and the other is held out for testing. This method works well for large sample sizes, but for moderately sized samples, it is subject to the idiosyncrasies of a single random train-and-test partition and provides a relatively pessimistic estimate of the true error rate [29]. The limitation can be addressed by using the cross-validation approach, which averages the results from multiple random train-and-test experiments.

We applied the cross-validation error estimation method [29] to evaluate the performance of the data mining models on the auto loan data set. In particular, we used 5-fold cross-validation, with the 220 loan cases divided randomly into 5 mutually exclusive test sets of 44 cases each. Each of those test sets was used in turn to evaluate a model trained with the remaining 176 cases—that is, those not in the given test set. For each mining method, therefore, the training was done in five iterations, with each iteration generating a separate model instance. All the cases in the sample were used for testing, as well as for training.

![](/api/attachments/WVRFA8CQ/fulltext/images/a8bcc1c2b7a4ddd3ef91b1d1601f13baa1faa7a4c97cc9ffb9dce43cfdf6bc7e.jpg)  
Figure 1. Evaluation of Data Mining Methods

Because the size of the German credit data set was much larger, we applied the holdout method. The first 700 cases (493 good and 207 bad) were used for training, and the remaining 300 cases (207 good and 93 bad) were reserved for testing. The proportions of good and bad cases in the two sets were roughly equal to the proportion (0.7:0.3) in the original data set.

Figure 1 depicts the process of evaluating data mining methods. Each model was generated by applying a learning method to a training set. We then evaluated the models on an independent test set using performance measures such as misclassification cost, AUC, generalizability, scalability, and robustness. Because we used 5-fold crossvalidation on the auto loan data set, the figure represents the evaluation process over one iteration. The test set corresponds to one of the five partitions, and the training set comprises all the cases not in that partition.

For credit decisions, the equal cost assumption for false positives (rejecting good loans) and false negatives (approving bad loans) rarely holds. Typically, bad loans incur higher costs to a bank than good loans. Also, for a profitable bank, bad loans are usually much less prevalent than good loans. Therefore, both costs and prior probabilities need to be taken into account.

Decision analysis allows us to make classifiers sensitive to costs and prior probabilities. In clinical decision-making [26], medical tests are conducted to detect the presence of a disease in a patient. The patient either tests positive (e.g., for breast cancer) or negative. A false positive results when the test is positive but the patient does not actually have the disease. A false negative results when the test is negative but the patient actually has the disease.

Table 1. Confusion Matrix

<table><tr><td rowspan="2">True class</td><td colspan="2">Predicted class</td></tr><tr><td>Positive</td><td>Negative</td></tr><tr><td>Positive</td><td>TP</td><td>FN</td></tr><tr><td>Negative</td><td>FP</td><td>TN</td></tr></table>

In the domain of credit evaluation, a classifier’s job is to identify loans that are likely to turn bad. Here, bad loans form the positive class. A false positive then results when a good loan is classified as bad; a false negative occurs when a bad loan is classified as good. Table 1 shows a confusion matrix with rows representing the true class and columns representing the predicted class. The overall accuracy of the classifier is given as

$$
\text { Accuracy } = (T P + T N) / (T P + F P + F N + T N),
$$

where TP is the number of true positives; TN is the number of true negatives; $F P$ is the number of false positives; and FN is the number of false negatives.

Accuracy, as defined in the formula above, is not an appropriate measure to use for many classification problems (e.g., breast cancer, bankruptcy, etc.). A classifier’s ability to correctly identify true positives, true negatives, and the resultant misclassification cost could be more appropriate performance criteria. ROC analysis, originating in signal detection theory, is a method that could be used for evaluating such criteria. An ROC curve plots the true positive rate of a classifier against its false positive rate, where

$$
\text { True   Positive   Rate } = T P / (T P + F N)
$$

and

$$
\text { False   Positive   Rate } = F P / (F P + T N),
$$

where $T P + F N$ is the total number of actual positives and $F P + T N$ is the total number of actual negatives.

The terms sensitivity and specificity are often used to characterize classifier performance. Sensitivity is nothing but the true positive rate:

$$
\text { Sensitivity } = T P / (T P + F N),
$$

whereas specificity is the complement of the false positive rate:

$$
\text { Specificity } = T N / (T N + F P).
$$

An ROC curve, therefore, is a plot of sensitivity and $( 1 - s p e c i f i c i t y )$ values.

![](/api/attachments/WVRFA8CQ/fulltext/images/bf8b1949ed38c8e9e7cb88b956e60049e5f2d3ebd52e716538226ac033bc64b4.jpg)  
Figure 2. ROC Curves on Auto Loan Test Set

An ROC curve is plotted by varying the threshold or cutoff for the classification model’s output (see Figure 2), which is a probability estimate. For example, a threshold of 0.5 would correspond to one point in the curve. Each point in an ROC curve corresponds to a specific threshold for the model’s output. The point (0, 0) corresponds to a classifier that never predicts the positive class, and the point (1, 1) corresponds to a classifier that always predicts the positive class. The straight line joining those two points represents the strategy of randomly guessing the class.

Any classification model should be better than the random guess strategy, with an ROC curve above the diagonal. The point (0, 1) in the upper left corner of Figure 2 represents perfect classification. A point to the upper left of another point in the ROC space (i.e., higher true positive rate and lower false positive rate) therefore corresponds to a better classifier. Plotting ROC curves for different classification models allows us to visually compare model performance across the spectrum of thresholds, independently of prior probabilities and misclassification costs. If the ROC curve for a given model dominates that for another model across the entire spectrum, then we can conclude that the former model is better than the latter. However, as is typically the case, one model may be better than another in certain regions and may be inferior in other regions.

Because ROC curves are independent of class distributions and costs, they can be used to evaluate classifier performance when prior probabilities and misclassification costs are difficult to estimate a priori or are prone to changes. In such situations, the AUC is an appropriate performance measure to use [2]. AUC is an aggregate performance measure that assesses the performance of a classifier across the entire range of decision thresholds. Higher AUC indicates better aggregate performance.

The areas under two ROC curves can be compared statistically by considering the correlation between the areas induced by the paired data [12]. The critical value $z =$ $( A _ { 1 } - A _ { 2 } ) / \sqrt { S E _ { 1 } ^ { 2 } + S E _ { 2 } ^ { 2 } - 2 r S E _ { 1 } S E _ { 2 } }$ is computed, where $A _ { 1 }$ and $A _ { 2 }$ are the two AUCs, $S E _ { 1 }$ and $S E _ { 2 }$ are the estimated standard errors of those two areas, and r is the estimated correlation between $A _ { 1 }$ and $A _ { 2 } .$ . The significance level associated with z can then be determined by looking up tables of normal distribution.

Each point on an ROC curve corresponds to a pair of values for sensitivity and $( 1 -$ specificity). For any point, the expected cost can be computed based on decision analysis. If $c _ { 1 0 }$ is the cost of a false positive and $c _ { 0 1 }$ is the cost of a false negative, then the expected cost for a medical test or predictive model is given as

$$
\operatorname{Cost} = p _ {0} * c _ {1 0} * (1 - \text { specificity }) + p _ {1} * c _ {0 1} * (1 - \text { sensitivity }),
$$

where $p _ { 1 }$ and $p _ { 0 }$ are the prior probabilities of the positive class (e.g., breast cancer or bad loan) and the negative class, respectively.

For analyzing classifier performance, we used five different costs for a false negative (classifying bad credit as good), $c _ { 0 1 } \colon 1 , 2 , 3 , 4 ,$ , and 5. The cost for a false positive (classifying good credit as bad), $c _ { 1 0 } ,$ was fixed at 1. Note that, for a bank loan, the cost of a false negative is typically much higher than that of a false positive. Five different prior probabilities for the positive class (bad credit) were used, $p _ { 1 } = 0 . 1 , 0 . 2 , 0 . 3 , 0 . 4 ,$ and 0.5. The misclassification costs were combined with the prior probabilities to generate 25 cost–probability ratios, where cost–probability ratio is defined as $( p _ { 1 }$ \* $c _ { 0 1 } ) { : } ( p _ { 0 } ^ { \mathrm { ~ * ~ } } c _ { 1 0 } )$ . The expected cost of each classifier was analyzed across these ratios.

## Evaluation Results

FIGURE 2 SHOWS THE ROC CURVES GENERATED using the test results for the five methods on the auto loan data set. The results from all the five test folds were pooled to produce an ROC curve for each method. Neural network and logistic regression yield high AUCs (0.851 and 0.849, respectively), followed closely by linear discriminant analysis (0.836), and then by decision tree (0.804) and case-based reasoning (0.769).

We found that the AUC for case-based reasoning is significantly lower than that for neural network $( z = 2 . 7 , p < 0 . 0 1 )$ , logistic regression $( z = 2 . 6 3 , p < 0 . 0 1 )$ , and linear discriminant analysis $( z = 2 . 1 6 , p < 0 . 0 5 )$ . The AUC for decision tree is lower but not significantly different from that for neural network $( z = 1 . 5 2 , p = 0 . 1 3 )$ , logistic regression $( z = 1 . 4 6 , p = 0 . 1 4 )$ , and linear discriminant analysis $( z = 1 . 0 5 , p = 0 . 3 )$ . The area for decision tree was higher than case-based reasoning, but the difference was not significant $( z = 1 . 0 9 , p = 0 . 2 8 )$ .

Figure 2 also shows that neural network, logistic regression, and linear discriminant analysis dominate decision tree and case-based reasoning across almost the entire spectrum, implying that they perform better irrespective of prior probabilities and costs. Case-based reasoning dominates decision tree for low false positive rates (< 0.25), but beyond that, decision tree dominates case-based reasoning. There is no clear dominance among neural network, logistic regression, and linear discriminant analysis, but closer inspection of the figure reveals that neural network and logistic regression perform the best over the possible range of cutoffs.

![](/api/attachments/WVRFA8CQ/fulltext/images/953776a6a28ba299455c482ea998c358217247c73a9998d7c82827f068f5055c.jpg)  
Figure 3. ROC Curves on German Credit Training Set

Figure 3 shows the ROC curves generated using the five different methods (neural network, logistic regression, linear discriminant analysis, decision tree, and kNN) on the German credit training set. kNN dominates neural network, logistic regression, and linear discriminant analysis across the entire range, with sensitivity approaching 1 at a false positive rate (1 – specificity) of around 0.4. Decision tree dominates kNN for low false positive rates $( < 0 . 2 5 )$ , but for higher values kNN dominates decision tree. Neural network, logistic regression, and linear discriminant analysis yield similar ROC curves, but linear discriminant analysis is dominated by neural network and logistic regression across almost the entire spectrum. Decision tree dominates neural network, logistic regression, and linear discriminant analysis for low false positive rates (< 0.3), but is dominated by the other three for higher rates.

Figure 4 shows the ROC curves generated using the test set. Neural network, logistic regression, and linear discriminant analysis dominate kNN and decision tree across the range of values. kNN and decision tree yield similar curves, with kNN appearing to be slightly better. There is no clear winner among neural network, logistic reasoning, and linear discriminant analysis. Neural network and logistic reasoning have the highest AUC (0.807 and 0.806, respectively), followed by linear discriminant analysis (0.793), kNN (0.736), and decision tree (0.723). The AUC for decision tree is significantly lower than that for neural network $( z = 3 . 0 3 , p < 0 . 0 1 )$ , logistic regression $( z = 2 . 8 7 , p < 0 . 0 1 )$ , and linear discriminant analysis $( z = 2 . 4 4 , p < 0 . 0 5 )$ . The AUC for kNN is significantly lower than that for neural network $( z = 2 . 5 1 , p < 0 . 0 5 )$

![](/api/attachments/WVRFA8CQ/fulltext/images/4c437e3b98b356a8e255a2a02b89359257b4a3d7090fe1693e88b9a9f830a91d.jpg)  
Figure 4. ROC Curves on German Credit Test Set

and logistic regression $( z = 2 . 4 0 , p < 0 . 0 5 )$ , but the difference with linear discriminant analysis is weakly significant $( z = 1 . 9 4 4 , p = 0 . 0 5 2 )$ . There is no significant difference between kNN and decision tree $( z = 0 . 3 8 , p = 0 . 7 0 )$ .

The outputs from a model can be treated as probabilities that a given credit application is good. Therefore, a low output would indicate that a case belongs to the positive class (bad credit). Each point on an ROC curve yields sensitivity and specificity values corresponding to a specific probability cutoff. For each cutoff, therefore, the expected cost can be easily computed using the formula given above.

For each combination of $c _ { 0 1 }$ and $p _ { 1 } ,$ we determined the cutoffs that minimize the expected cost for the five models on the training set. For each method, those cutoffs are shown in Table 2 with a \_TRAIN postfix. We then applied those cutoffs to determine the sensitivity and specificity values from the ROC curves on the test set. Those values were then used to compute the expected costs for the test set. For any model, the cutoff that minimizes the expected cost on the training set would be expected to result in a relatively low cost when applied to the test set.

Under the equal misclassification cost scenario $( c _ { 0 1 } = 1 , p _ { 1 } = 0 . 5 )$ , it is interesting to note that only for linear discriminant analysis, the cutoff that resulted in minimum expected cost was close to 0.50, the default cutoff for predictive models. For all other models, the corresponding cutoffs were much higher (0.65 for neural network, 0.74 for logistic regression, 0.65 for decision tree, and 0.83 for kNN), suggesting that even when misclassification costs are not important, the models need to be tuned for boosting their performance.

Figures 5 and 6 depict the cost performance of the five models on the training set and the test set, respectively, across 15 different cost–probability ratios (corresponding to $c _ { 0 1 } = 1 , 3 , 5$ and $p _ { 1 } = 0 . 1 , 0 . 2 , 0 . 3 , 0 . 4 , 0 . 5 )$ . For low values of $c _ { 0 1 } ^ { \phantom { } } .$ , decision tree generally yields much lower costs on the training set than the other models. However, when decision tree is applied to the test set, its performance degrades considerably, resulting in the highest cost for most scenarios. Another model that does relatively well on the training set, but nowhere as well on the test set, is kNN. Figures 7 and 8 provide a graphic comparison of decision tree and kNN performance across training and test sets. Compared to these two models, logistic regression, linear discriminant analysis, and neural network display relatively low variations in costs across the two sets. In terms of generalizability, logistic regression’s performance is the most impressive across the scenarios, followed by neural network and linear discriminant analysis. Logistic regression yields the lowest cost in most situations, with neural network producing lower costs in some and linear discriminant analysis in a few situations.

. <sub>Opti</sub>m<sup>al</sup> <sup>Training</sup> <sup>and</sup> <sup>Test</sup>

<table><tr><td> $c_{01}$ </td><td> $p_1$ </td><td>LR_TRAIN</td><td>LR_TEST</td><td>LDA_TRAIN</td><td>LDA_TEST</td><td>NN_TRAIN</td><td>NN_TEST</td><td>DT_TRAIN</td><td>DT_TEST</td><td>KNN_TRAIN</td><td>KNN_TEST</td></tr><tr><td>1</td><td>0.1</td><td>0.0950</td><td>0.0975</td><td>0.1217</td><td>0.1397</td><td>0.2412</td><td>0.2677</td><td>0.2600</td><td>0.0000</td><td>0.1670</td><td>0.0000</td></tr><tr><td>1</td><td>0.2</td><td>0.3688</td><td>0.3097</td><td>0.1836</td><td>0.2012</td><td>0.3752</td><td>0.3900</td><td>0.5000</td><td>0.1600</td><td>0.5000</td><td>0.0000</td></tr><tr><td>1</td><td>0.3</td><td>0.5423</td><td>0.4670</td><td>0.3416</td><td>0.2012</td><td>0.5316</td><td>0.4400</td><td>0.5000</td><td>0.6100</td><td>0.5000</td><td>0.5000</td></tr><tr><td>1</td><td>0.4</td><td>0.5423</td><td>0.4718</td><td>0.3896</td><td>0.3686</td><td>0.5316</td><td>0.4451</td><td>0.5000</td><td>0.7300</td><td>0.5000</td><td>0.5000</td></tr><tr><td>1</td><td>0.5</td><td>0.7444</td><td>0.7561</td><td>0.4971</td><td>0.4560</td><td>0.6477</td><td>0.7206</td><td>0.6450</td><td>0.8400</td><td>0.8330</td><td>0.8330</td></tr><tr><td>2</td><td>0.1</td><td>0.3688</td><td>0.3097</td><td>0.1476</td><td>0.2012</td><td>0.3381</td><td>0.3900</td><td>0.5000</td><td>0.0000</td><td>0.5000</td><td>0.0000</td></tr><tr><td>2</td><td>0.2</td><td>0.5423</td><td>0.4718</td><td>0.3416</td><td>0.2012</td><td>0.5316</td><td>0.4451</td><td>0.5000</td><td>0.6100</td><td>0.5000</td><td>0.5000</td></tr><tr><td>2</td><td>0.3</td><td>0.6535</td><td>0.7474</td><td>0.4760</td><td>0.4453</td><td>0.6477</td><td>0.5969</td><td>0.6450</td><td>0.8400</td><td>0.8330</td><td>0.5000</td></tr><tr><td>2</td><td>0.4</td><td>0.7444</td><td>0.7561</td><td>0.4971</td><td>0.6072</td><td>0.6572</td><td>0.7206</td><td>0.6950</td><td>0.8400</td><td>0.8330</td><td>0.8330</td></tr><tr><td>2</td><td>0.5</td><td>0.8164</td><td>0.8601</td><td>0.7909</td><td>0.6536</td><td>0.8509</td><td>0.7206</td><td>0.7300</td><td>0.8850</td><td>0.8330</td><td>0.8330</td></tr><tr><td>3</td><td>0.1</td><td>0.5207</td><td>0.3706</td><td>0.2615</td><td>0.2012</td><td>0.5316</td><td>0.4400</td><td>0.5000</td><td>0.1600</td><td>0.5000</td><td>0.0000</td></tr><tr><td>3</td><td>0.2</td><td>0.6467</td><td>0.5309</td><td>0.3896</td><td>0.3686</td><td>0.5316</td><td>0.4451</td><td>0.6450</td><td>0.8400</td><td>0.8330</td><td>0.5000</td></tr><tr><td>3</td><td>0.3</td><td>0.7444</td><td>0.7561</td><td>0.4971</td><td>0.6072</td><td>0.6572</td><td>0.7206</td><td>0.6950</td><td>0.8400</td><td>0.8330</td><td>0.8330</td></tr><tr><td>3</td><td>0.4</td><td>0.8164</td><td>0.8601</td><td>0.7909</td><td>0.6536</td><td>0.8509</td><td>0.7206</td><td>0.7300</td><td>0.8850</td><td>0.8330</td><td>0.8330</td></tr><tr><td>3</td><td>0.5</td><td>0.8902</td><td>0.8769</td><td>0.7909</td><td>0.8086</td><td>0.8741</td><td>0.8892</td><td>0.7300</td><td>0.8850</td><td>0.8330</td><td>0.8330</td></tr><tr><td>4</td><td>0.1</td><td>0.5423</td><td>0.4670</td><td>0.3416</td><td>0.2012</td><td>0.5316</td><td>0.4400</td><td>0.5000</td><td>0.6100</td><td>0.5000</td><td>0.5000</td></tr><tr><td>4</td><td>0.2</td><td>0.7444</td><td>0.7561</td><td>0.4971</td><td>0.4560</td><td>0.6477</td><td>0.7206</td><td>0.6450</td><td>0.8400</td><td>0.8330</td><td>0.8330</td></tr><tr><td>4</td><td>0.3</td><td>0.7832</td><td>0.7561</td><td>0.5719</td><td>0.6536</td><td>0.6572</td><td>0.7206</td><td>0.7300</td><td>0.8850</td><td>0.8330</td><td>0.8330</td></tr><tr><td>4</td><td>0.4</td><td>0.8902</td><td>0.8769</td><td>0.7909</td><td>0.8086</td><td>0.8509</td><td>0.8243</td><td>0.7300</td><td>0.8850</td><td>0.8330</td><td>0.8330</td></tr><tr><td>4</td><td>0.5</td><td>0.8902</td><td>0.9166</td><td>0.7909</td><td>0.8086</td><td>0.8741</td><td>0.8892</td><td>1.0000</td><td>1.0000</td><td>0.8330</td><td>1.0000</td></tr><tr><td>5</td><td>0.1</td><td>0.5423</td><td>0.4718</td><td>0.3416</td><td>0.2012</td><td>0.5316</td><td>0.4451</td><td>0.5000</td><td>0.6100</td><td>0.5000</td><td>0.5000</td></tr><tr><td>5</td><td>0.2</td><td>0.7444</td><td>0.7561</td><td>0.4971</td><td>0.6072</td><td>0.6477</td><td>0.7206</td><td>0.6950</td><td>0.8400</td><td>0.8330</td><td>0.8330</td></tr><tr><td>5</td><td>0.3</td><td>0.8685</td><td>0.8601</td><td>0.7909</td><td>0.6536</td><td>0.8509</td><td>0.8243</td><td>0.7300</td><td>0.8850</td><td>0.8330</td><td>0.8330</td></tr><tr><td>5</td><td>0.4</td><td>0.8902</td><td>0.8769</td><td>0.7909</td><td>0.8086</td><td>0.8741</td><td>0.8892</td><td>0.7750</td><td>1.0000</td><td>0.8330</td><td>1.0000</td></tr><tr><td>5</td><td>0.5</td><td>0.8988</td><td>0.9166</td><td>0.7909</td><td>0.8086</td><td>0.9155</td><td>0.9989</td><td>1.0000</td><td>1.0000</td><td>0.8330</td><td>1.0000</td></tr></table>

Cost Results on Training Set (c01 = 1)  
![](/api/attachments/WVRFA8CQ/fulltext/images/b1a0db1ae804d9f007d596904899283f538cfec3a394bf90415c8779c09fa197.jpg)

Cost Results on Training Set (c01 = 3)  
![](/api/attachments/WVRFA8CQ/fulltext/images/e1e81cc741bb66304ddbcf178de7f1e59a03b08d31755642699f2b3219d6732d.jpg)  
Cost Results on Training Set (c01 = 5)

![](/api/attachments/WVRFA8CQ/fulltext/images/7c1cb18ff4d14366fceba82816d79de99ed6becb0f16efa61f03c62019777556.jpg)  
Figure 5. Costs on German Credit Training Set Across Different Cost Ratios

Cost Results on Test Set (c01 = 1)  
![](/api/attachments/WVRFA8CQ/fulltext/images/6e6f7e6656ec67cc78957f51e92fcc4268f35a566605870bc6c0f8cd4e0393b8.jpg)

Cost Results on Test Set (c01 = 3)  
![](/api/attachments/WVRFA8CQ/fulltext/images/69416449d73229d0d350a170c8cb41a299902ae27e872bf4f030de4270742b81.jpg)

Cost Results on Test Set (c01 = 5)  
![](/api/attachments/WVRFA8CQ/fulltext/images/3808fae9097fb7d41ac54d9581038f1b244d0501d971a004d1e297282c93a820.jpg)  
Figure 6. Costs on German Credit Test Set Across Different Cost Ratios

Decision Tree (c01 = 1)  
![](/api/attachments/WVRFA8CQ/fulltext/images/985b4f94c331ed0a2cd17ae2e2b3ee62819fbd74060826bdfc6236d0c9a92e63.jpg)

Decision Tree (c01 = 3)  
![](/api/attachments/WVRFA8CQ/fulltext/images/d15cd316e708aed63a482aeb4f6034a0bc7a0b4cc5bcd1faf7be9804c20c9381.jpg)  
Decision Tree (c01 = 5)

![](/api/attachments/WVRFA8CQ/fulltext/images/dc6c3ef6ff212abc606ed5903e4e80da2ac9825380c7be1bb2800bcacf48f34a.jpg)  
Figure 7. Performance of Decision Tree Across Training and Test Sets

We also evaluated the robustness of the models with respect to assumptions on class distributions. We explored if slight changes in class distributions result in significant changes in the outcome. If a model’s expected cost is sensitive to small changes in the priors, then the model is not robust with respect to the priors.

The results of the sensitivity analysis are shown in Figure 9, which graphically captures how expected cost varies across different priors $( p _ { 1 } )$ for three different values of $c _ { 0 1 } .$ . The higher the slope of a line in a certain region, the higher is the sensitivity of the model to changes in $p _ { 1 } .$ For instance, when $c _ { 0 1 } = 3$ , while the costs for logistic regression remain flat for points in the $p _ { 1 } > 0 . 2$ region, the costs for decision tree rise sharply. Over this range, therefore, logistic regression is much more robust against changes in priors than decision tree. For $c _ { 0 1 } = 1$ , there is not much difference in robustness among neural network, logistic regression, and linear discriminant analysis; decision tree is the least robust among the five models in the $p _ { 1 } > 0 . 3$ region. Decision tree is also very sensitive to changes in priors for $c _ { 0 1 } = 3$ and 5. Logistic regression and kNN appear to be more robust than neural network and linear discriminant analysis when $p _ { 1 } > 0 . 2$ . But when $c _ { 0 1 } = 5$ , kNN becomes more sensitive to changes in $p _ { 1 } ;$ logistic regression appears to be the least sensitive. Overall, all the models are fairly sensitive for low values of $p _ { 1 }$ (between 0.1 and 0.2). For low values of $c _ { 0 1 } \left( 1 \right)$ , except for decision tree, the models are fairly robust for $p _ { 1 } > 0 . 3$ . For higher values of $c _ { 0 1 }$ (3 and 5), logistic regression tends to be the most robust.

k Nearest Neighbor (c01 = 1)  
![](/api/attachments/WVRFA8CQ/fulltext/images/74475f312f7903773626aca6d0101333143f2170471170f6cf6aa9008912b0d4.jpg)

k Nearest Neighbor (c01 = 3)  
![](/api/attachments/WVRFA8CQ/fulltext/images/86dea3f03ad7d3c334be6204a682770c135ac229cd7e27a6b482eb226b4beaa4.jpg)

k Nearest Neighbor (c01 = 5)  
![](/api/attachments/WVRFA8CQ/fulltext/images/f3c2b0fc679b491b81a4f60c831045737e30806bddd4fec39e3183d28f8406fd.jpg)  
Figure 8. Performance of kNN Across Training and Test Sets

![](/api/attachments/WVRFA8CQ/fulltext/images/8fd0f724c7ecde44052c767f857ff5626adbdb3ba103dcbfbebb6459f1bd3204.jpg)

![](/api/attachments/WVRFA8CQ/fulltext/images/3bddb0af913912162f244273f88431e47b83164567767e109ccd29f88d7fd6cf.jpg)

![](/api/attachments/WVRFA8CQ/fulltext/images/7337243896930df7c71afdb84d7787633bbeb8d8edb3a2fd8ae3755d9beff346.jpg)  
Figure 9. Sensitivity Analysis of Classifiers

As described before, the decision threshold of a classifier was chosen such that it minimized the expected cost on the training set. However, there is no guarantee that the selected cutoff would minimize the cost on the test set, even though we would expect the cost to be near minimal. For each model, we independently determined the cutoff that would minimize the cutoff on the test set. Sufficiently close training and test cutoffs would support the notion of external validity of a model.

Table 2 shows the training cutoffs and tests cutoffs (shown with \_TEST postfix) for the five models, corresponding to the 25 cost–probability ratios. Pearson’s correlation coefficients between training and test cutoffs were determined for each model. Logistic regression had the highest correlation (0.977) between training and test cutoffs, followed by linear discriminant analysis (0.934), neural network (0.932), kNN (0.830), and decision tree (0.796). All the correlations were significant at the 0.01 level.

In an ideal scenario, the test cutoffs would be identical to the training cutoffs, and a linear regression model of the two would yield a line with a slope of 1 and an intercept of 0. For each data mining model, we conducted a regression analysis using the two sets of cutoffs. The regression lines for neural network and linear discriminant analysis were closest to the ideal, with both having an intercept of –0.02 and slopes of 1.01 and 0.99, respectively. The line for logistic regression was also close, with a slope of 1.12 and an intercept of –0.10. In contrast, decision tree and kNN had slopes of 1.48 and 1.41 and intercepts of –0.25 and –0.36, respectively.

The findings of our study can be summarized as follows:

• in general, neural network, logistic regression, and linear discriminant analysis dominate decision tree and case-based reasoning/kNN;

• in terms of aggregate performance (AUC), neural network and logistic regression are the best;

• decision tree and kNN are prone to overfitting, whereas the performance of logistic regression, neural network, and linear discriminant analysis are relatively invariant across the training and test sets;

• logistic reasoning yields the minimum cost in most situations and neural network in some;

• in general, logistic regression is the most robust against changes in priors, whereas decision tree is the most sensitive;

• the approach we used for tuning the models is effective.

## Discussion of Results

THE STUDY EMPHASIZES THE USE OF ROC curves for evaluating and tuning alternative data mining methods. We used several performance measures, including AUC, misclassification cost, robustness, scalability, and generalizability, to analyze the performance of the methods.

One major finding is the relative consistency of the methods for the two credit problems. When the four common methods are ranked with respect to AUC, the order is the same for both problems: neural network, logistic regression, linear discriminant analysis, decision tree. In both cases, neural network and logistic regression have almost identical areas, with linear discriminant analysis following closely behind and decision tree lagging by a wider margin. For both problems, the distance-based methods performed poorly, with case-based reasoning ranking last for auto loans and kNN second to last for German credit. These findings indicate that the results are scalable across problems in the credit evaluation domain.

The overall performance of each classifier was better for the auto loan problem than for the German credit problem, despite the fact that the former had a much smaller sample size. That result could be attributed to the much higher dimensionality of the German credit data set compared to that of the auto loan data set. Higher complexity may have adversely affected classifier performance, with decision tree experiencing the maximum decline. Another possible reason is that having recourse to a domain expert helped us identify the relevant variables for the auto loan data set.

The evaluation results demonstrate the pitfalls associated with extrapolating from the results on the training set. Although decision tree and kNN performed well on the training set, their performance deteriorated drastically on the test set. Decision tree is somewhat limited in its ability to generalize to unseen problems because of its tendency to overfit the training data [3]. The performance of logistic regression, neural network, and linear discriminant analysis remains relatively consistent across training and testing. The strong fit between the training and test cutoffs of these three methods provides further support for their external validity.

The results of the study clearly demonstrate the effectiveness of the approach we used for tuning the models. The models themselves were generated without explicitly incorporating misclassification costs. That is, the trained models are independent of costs. Only after the models were generated, the decision thresholds were tuned to account for costs and prior probabilities. Even under the equal cost assumption, we found that tuning was needed for optimizing model performance.

In general, we found that logistic regression was the most robust against changes in priors, while decision tree was the most sensitive. In situations where class probabilities are not known in advance with sufficient precision or are prone to changes, using decision tree could lead to unanticipated consequences. On the other hand, logistic regression is relatively robust and using it would not lead to big surprises when conditions change.

Except for case-based reasoning and kNN, all the models in this study derive their parameters from the data set. Case-based reasoning and kNN, in contrast, do not train in that sense, but try to find a set of neighbors when a classification task is given. One of the shortcomings of nearest neighbor methods—sometimes called “lazy” methods—is that they do not actually build a model, depending instead on cases available in the training sample [11]. The reliability of such models would improve with more and more cases, covering a wider range of loans, added to its memory.

## Conclusions and Future Directions

IN THE INFORMATION SYSTEMS (IS) FIELD, most of the studies in data mining have used accuracy or misclassification rate as a metric for evaluating performance. We argue in this paper that misclassification cost, not misclassification rate, is a more appropriate measure to use in many domains, including the one we studied. We examined the relative cost performance of five different methods in the study.

One of the reasons IS researchers may have ignored costs is because methods such as logistic regression, case-based reasoning, and kNN cannot explicitly incorporate costs during learning. In our study, we did not explicitly incorporate costs into any of the models that we built based on the training data. Rather, costs were indirectly incorporated into a model by determining the threshold that minimized the expected cost. Making a trained model cost sensitive is a major contribution of our research. From a practical standpoint, this has important implications. Firms need not build new models when costs or priors change. A model has to be built only once; when costs or priors change, the model is tuned by adjusting its threshold.

We used ROC curves to analyze classifier performance over a range of decision thresholds. The AUC was determined to judge the aggregate performance of each method across the entire range. In contrast to a simple accuracy measure, which is predicated on a default threshold, AUC is not tied to any specific threshold; rather, it can be treated as an aggregate measure of classifier performance.

Our research demonstrates how to assess the robustness of a classifier by studying the effects of a variable threshold on expected cost. The more sensitive a model is with respect to small changes in prior probabilities, the less attractive is it going to be, particularly in situations where all the conditions are difficult to determine a priori. For many firms, robustness could be an important issue because of their aversion toward uncertainty.

The study also explores the issue of scalability by using data sets for two problems in the same domain. The German credit data set is larger in size and dimensionality than the auto loan data set. The findings—in particular, the classifier rankings—are quite consistent despite the differences in size, dimensionality, and sample prevalence rates.

Our research contributes to the existing literature by studying the fit, or lack thereof, between outputs from training and testing. The fact that the performance of some methods is relatively invariant across the two sets compared to others may be a factor in selecting a classifier. Also, stronger correlations and closer fits between training cutoffs and test cutoffs would inspire higher confidence in a model.

We tried to keep the comparison among the methods as fair as possible by employing default settings while building the models. However, we had to take additional steps or specify additional values for model parameters when necessary. For example, we applied backward stepwise elimination for feature selection in logistic regression and linear discriminant analysis, and we specified the cutoff distance for case-based reasoning, k for kNN, and the number of hidden units for neural network. When such variations exist, the question is whether it is fair to compare the methods. From a practical perspective, though, what we need to consider is what works best, based on how the methods have been employed in the past [29].

We compared the performance of five different data mining methods. The performance of each model developed was assessed separately. But there is rarely one foolproof technique for any given application, and new and hybrid algorithms are always being proposed [3]. A combination of several methods may produce the best results [28]. A new hybrid approach, which uses a combination of models, could be explored.

The models investigated in this study were derived from data, not from human expertise. In a domain such as bank lending, where experts exist, it is possible to elicit domain knowledge from the experts in the form of rules, which could then be implemented as an expert system. However, there has been very little work addressing the issue of incorporating domain knowledge into data mining [6, 18]. An interesting future direction would be to explore if the fusion of a knowledge-based expert system with a data mining method leads to better performance. Weiss et al. [30] provide a good example by combining an expert system with rule induction to develop inexpensive decision rules for sales leads.

In this study, we have presented an empirical approach to evaluating and tuning predictive data mining models using ROC curves. While most studies have used accuracy as the sole measure, we include a variety of measures—AUC, expected cost, robustness, scalability, and generalizability—to evaluate the methods. From a research standpoint, in addition to the future directions identified above, it would be worth exploring if our approach yields similar results in other problem domains. Our study also has important implications for practice, especially with respect to selecting a data mining method or tool.

## REFERENCES

1. Berardi, V.L., and Zhang, G.P. The effect of misclassification costs on neural network classifiers. Decision Sciences, 30, 3 (1999), 659–682.

2. Bradley, A.P. The use of the area under the ROC curve in the evaluation of machine learning algorithms. Pattern Recognition, 30, 7 (1997), 1145–1159.

3. Cabena, P.; Hadjinian, P.; Stadler, R.; Verhees, J.; and Zanasi, A. Discovering Data Mining: From Concept to Implementation. Upper Saddle River, NJ: Prentice Hall, 1998.

4. Chung, H.M., and Gray, P. Special section: Data mining. Journal of Management Information Systems, 16, 1 (Summer 1999), 11–16.

5. Doumpos, M.; Kosmidou, K.; Baourakis, G.; and Zopounidis, C. Credit risk assessment using a multicriteria hierarchical discrimination approach: A comparative analysis. European Journal of Operational Research, 138, 2 (2002), 392–412.

6. Dybowski, R.; Laskey, K.B.; Myers, J.W.; and Parsons, S. Introduction to the special issue on the fusion of domain knowledge with data for decision support. Journal of Machine Learning Research, 4 (July 2003), 293–294.

7. Elkan, C. The foundations of cost-sensitive learning. In B. Nebel (ed.), Proceedings of the Seventeenth International Joint Conference on Artificial Intelligence. San Francisco: Morgan Kaufmann, 2001, pp. 973–978.

8. Fanning, K., and Cogger, K.O. Neural network detection of management fraud using published financial data. Intelligent Systems in Accounting, Finance and Management, 7, 1 (1998), 21–41.

9. Fawcett, T. ROC graphs: Notes and practical considerations for data mining researchers. HPL-2003–4, Intelligent Enterprise Technologies Lab, Hewlett-Packard, Palo Alto, CA, January 7, 2003.

10. Fuller, P., and Kohers, T. Developing a decision rule to predict failure: The case of savings and loan associations. Journal of Economics and Finance, 18, 1 (1994), 43–54.

11. Hand, D.; Mannila, H.; and Smyth, P. Principles of Data Mining. Cambridge, MA: MIT Press, 2001.

12. Hanley, J.A., and McNeil, B.J. A method of comparing the areas under receiver operating characteristic curves derived from the same cases. Radiology, 148 (September 1983), 839–843.

13. Jain, B.A., and Nag, B.N. Performance evaluation of neural network decision models. Journal of Management Information Systems, 14, 2 (Fall 1997), 201–216.

14. Johnson, R.A., and Wichern, D.W. Applied Multivariate Statistical Analysis, 3d ed. Englewood Cliffs, NJ: Prentice Hall, 1992.

15. Joos, P.; Vanhoof, K.; and Sierens, N. Credit classification: A comparison of logit models and decision trees. In G. Nakhaezadeh and E. Steurer (eds.), Proceedings of ECML Workshop on Applications of Machine Learning and Data Mining in Finance. Forschung, Germany: Technical University of Chemnitz, 1998, pp. 59–73.

16. Kim, C.N., and McLeod, R. Expert, linear models, and nonlinear models of expert decision making in bankruptcy prediction: A lens model analysis. Journal of Management Information Systems, 16, 1 (Summer 1999), 189–206.

17. Kolodner, J. Case-Based Reasoning. San Mateo, CA: Morgan Kaufmann, 1993.

18. Kopanas, I.; Avouris, N.M.; and Daskalaki, S. The role of domain knowledge in a large scale data mining project. In I.P. Vlahavas and C.D. Spyropoulos (eds.), Methods and Applications of Artificial Intelligence. Berlin: Springer-Verlag, 2002, pp. 288–299.

19. Michie, D.; Spiegelhalter, D.J.; and Taylor, C.C. (eds.). Machine Learning, Neural, and Statistical Classification. New York: Ellis Horwood, 1994.

20. Provost, F.; Fawcett, T.; and Kohavi, R. The case against accuracy estimation for comparing induction algorithms. In J.W. Shavlik (ed.), Proceedings of the Fifteenth International Conference on Machine Learning. San Francisco: Morgan Kaufmann, 1998, pp. 445–453.

21. Quinlan, J.R. Discovering rules by induction from large collections of examples. In D. Michie (ed.), Expert Systems in the Micro Electronic Age. Edinburgh, UK: Edinburgh University Press, 1979, pp. 168–201.

22. Quinlan, J.R. C4.5: Programs for Machine Learning. San Mateo, CA: Morgan Kaufmann, 1993.

23. Sinha, A.P., and Richardson, M.A. A case-based reasoning system for indirect bank lending. Intelligent Systems in Accounting, Finance and Management, 5, 4 (1996), 229–240.

24. Sung, T.K.; Chang, N.; and Lee, G. Dynamics of modeling in data mining: Interpretive approach to bankruptcy prediction. Journal of Management Information Systems, 16, 1 (Summer 1999), 63–85.

25. Tam, K.Y., and Kiang, M.Y. Managerial applications of neural networks: The case of bank failure predictions. Management Science, 38, 7 (1992), 926–947.

26. Weinstein, M.C., and Fineberg, H.V. Clinical Decision Analysis. Philadelphia: W.B. Saunders, 1980.

27. Weiss, G.M., and Provost, F. The effect of class distribution on classifier learning: An empirical study. Technical Report ML-TR-44, Department of Computer Science, Rutgers University, New Brunswick, NJ, August 2, 2001.

28. Weiss, S.M., and Indurkhya, N. Predictive Data Mining: A Practical Guide. San Francisco: Morgan Kaufmann, 1998.

29. Weiss, S.M., and Kulikowski, C.A. Computer Systems that Learn: Classification and Prediction Methods from Statistics, Neural Nets, Machine Learning, and Expert Systems. San Mateo, CA: Morgan Kaufmann, 1991.

30. Weiss, S.M.; Buckley, S.J.; Kapoor, S.; and Damgaard, S. Knowledge-based data mining. In Proceedings of the Ninth ACM SIGKDD International Conference on Knowledge Discovery and Data Mining. New York: ACM Press, 2003, pp. 456–461.

31. Witten, I.H., and Frank, E. Data Mining: Practical Machine Learning Tools and Techniques with Java Implementation. San Francisco: Morgan Kaufmann, 2000.

32. Zhu, D.; Premkumar, G.; Zhang, X.; and Chu, C. Data mining for network intrusion detection: A comparison of alternative methods. Decision Sciences, 32, 4 (2001), 635–660.
