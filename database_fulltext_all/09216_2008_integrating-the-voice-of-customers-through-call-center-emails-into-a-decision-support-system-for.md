---
otero_id: 9216
otero_key: "9WJAT3YK"
title: "Integrating the voice of customers through call center emails into a decision support system for churn prediction"
authors: "Kristof Coussement; Dirk Van den Poel"
year: "2008"
journal: "Information & Management"
doi: "10.1016/j.im.2008.01.005"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Integrating the voice of customers through call center emails into a decision support system for churn prediction

Kristof Coussement, Dirk Van den Poel <sup>\*</sup>

Ghent University, Faculty of Economics and Business Administration, Department of Marketing, Tweekerkenstraat 2, 9000 Ghent, Belgium Received 9 October 2006; received in revised form 7 August 2007; accepted 21 January 2008 Available online 17 March 2008

## Abstract

We studied the problem of optimizing the performance of a DSS for churn prediction. In particular, we investigated the beneficial effect of adding the voice of customers through call center emails – i.e. textual information – to a churn-prediction system that only uses traditional marketing information. We found that adding unstructured, textual information into a conventional churn-prediction model resulted in a significant increase in predictive performance. From a managerial point of view, this integrated framework helps marketing-decision makers to better identify customers most prone to switch. Consequently, their customer retention campaigns can be targeted more effectively because the prediction method is better at detecting those customers who are likely to leave.

Keywords: Customer relationship management (CRM); Data mining; Churn prediction; Text mining; Call center email; Voice of customers (VOC); Binary classification modeling

## 1. Introduction

In the past, companies focused on selling products and services with little knowledge or strategy concerning the customers who bought the products. Today business is evolving from this ‘product-centered’ to a ‘customercentered’ environment. Companies need to find ways to capture and enhance market share while reducing costs [7]. Consequently, existing companies must reconsider the business relationships with their customers [24].

Customer relationship management (CRM) is becoming a critical success factor in today’s business environment [2,16]. Data mining is being implemented to gain customer knowledge from organizational data warehouses [35]. A way to manage customer churn is to predict which customers are most likely to leave and then target them with incentives to stay. Consequently, these IS support marketing-decision makers to generate marketing campaigns for the right customers. A field experiment by Burez and Van den Poel [9] has already shown that companies can boost profitability by shifting from mass to focused marketing strategies. It is more profitable to keep and satisfy existing customers than to attract new ones with a high attrition rate [26]. Identifying customers most prone to switch, is thus important [17]. In order to develop an effective customer retention program, the company must build a model that is as accurate as possible; indeed Van den Poel and Larivie\`re [36] showed that a small change in retention rate can result in a significant change in profitability.

We decided it was necessary to incorporate the voice of customers (VOC) through call center emails into a traditional churn-prediction model in order to provide a better model: one with a higher predictive performance. The rapid development of IT and the Internet has made it easier for customers to communicate with the company. Call centers are expanding rapidly in scope, number and size [1], because many firms rely on them to address customer concerns and provide product information [25]. However, marketing managers tend to neglect this valuable information because (i) it is not directly applicable in a traditional marketing context, (ii) there is seldom in-house knowledge on how to convert this (textual) information into an analyzable form and (iii) no ready-to-use framework is available to integrate the information. We developed a DSS for churn prediction; it integrates free-formatted, textual information from customer emails with information derived from the marketing database. Although previous research used the VOC in understanding customers’ needs and behavior (e.g. Refs. [10,11,21]), no prior work has used VOC in a churn-prediction model.

## 2. Methodology

Fig. 1 shows how the integration of information types in a churn-modeling system was achieved.

## 2.1. Data collection

Structured marketing information can be extracted from a common marketing database in which all transactional and marketing-related information has been stored. In contrast, call center emails are highly unstructured. Thus, extracting information from emails requires meticulous pre-processing to capture the relevant details for inclusion in a churn detection/prediction DSS.

## 2.2. Pre-processing

## 2.2.1. Data and text pre-processing

The structured information is internally available at a very low cost and available for pre-processing and integration into our model. However, the original emails are unformatted by nature. They are converted into a structured representation using the vector-space of Salton’s SMART [31]: an email is represented as a vector of weighted frequencies of designated words. Thus emails are ndimensional vectors, with n the number of distinct terms in the dictionary. Each vector component reflects the importance of the corresponding term with respect to the semantics of the email [6] and each component has a weight if the term is present or zero otherwise. Thus a collection of emails is represented as a term-by-email matrix. Fig. 2 shows the steps in this pre-processing phase whereby raw emails become a term-by-email matrix.

In the first step, raw text cleaning, special characters and punctuation are removed from words and spelling errors are corrected by comparing with words in a reference dictionary using a synonym data set. Tokenization converts the input stream into tokens or words. It uses blanks as delimiters for words which are then converted to lower case (case conversion). Part-of-speech tagging gives words their syntactic category: informative (nouns, verbs, adjectives and adverbs) or non-informative.

Next, terms are replaced by their stem, e.g. connect is the stem for connected, connecting, connection, etc., Stemming reduces the number of terms significantly [5] and increases retrieval performance [19]. A dictionary-based stemmer is used. When a term is unrecognizable, standard decision rules are applied to give the term a correct stem.

![](/api/attachments/9WJAT3YK/fulltext/images/de6c4992bda3d0e25040f849874f2265c17c822c711aa538b44babcda1ae5ca3.jpg)  
Fig. 1. An integrated churn-modeling system that uses structured, database-related information and free-formatted, textual information.

![](/api/attachments/9WJAT3YK/fulltext/images/5ea30927ca27ca9823ecfacc43dd00bf51a27f014b46d68422eaa40321ea82a0.jpg)  
Fig. 2. Different steps in the text pre-processing phase.

The result of this process is a high-dimensional term-byemail matrix having many distinct terms. This matrix is reduced by applying term filtering: rare words are eliminated because they seldom help in future classifications. Word frequencies follow a Zipf distribution [37]: thus half of them appear only once or twice. Eliminating words under those thresholds often yield great savings [22]. Stopwords, (e.g. ‘the’ or ‘a’) are also removed. Next, the non-informative parts of speech are left out from the analysis. A last step in the term-filtering phase is removing irrelevant terms by manually checking the temporary dictionary.

In the term vector-weighting phase, a weighted term vector for every email is constructed. By now, the values in the term-by-email matrix are simply the raw frequencies of appearance for a term in an email. Spark Jones [33] showed significant improvements in retrieval performance when using weighted term vectors. Term weighting is often done by determining the product of the term frequency (tf) and the inverse email frequency (idf) [27–29,34]. The result is a high-dimensional, weighted term-by-email matrix. Appendix A describes the term vector-weighting phase in detail.

In the final step, an aggregated term-by-email matrix is generated (i.e. email vector aggregation). The aim is to make an aggregation of the email vectors that belong to the same customer. This is necessary because a customer can send more than one email during the observation period, while from a prediction point of view, a prediction is made per individual customer. As such an aggregation of the information for all emails from the same customer is needed.

The aggregated weight of term i for all emails belonging to subscription $j ~ ( A w _ { i j } )$ is

$$
A w _ {i j} = \sum_ {k = 1} ^ {r} w _ {i k}\tag{1}
$$

with $w _ { i k }$ equal to the weight of term i in email k and r equal to the number of emails belonging to the same observation.

Using each distinct term as a feature in the churnmodeling phase would lead to an unmanageable number of explanatory variables. Moreover, due to the high dimensionality of the feature space, most weights are zero for a single email. Thus, using a large and sparse term-by-emai matrix would be counterproductive in the predictive modeling context.

## 2.2.2. Dimension reduction

The dimension of the aggregated (weighted) term-byemail matrix is reduced by using Latent Semantic Indexing (LSI). It reduces the dimensionality of the feature space b grouping together related terms [12]. Deerwester et al. [12] used singular value decomposition (SVD) to form semantic generalizations from emails. It uses the fact that certain terms appear in similar emails to establish relationships between the terms. Consequently, SVD projects emails from the high-dimensional term space to an orthonormal, semantic, latent subspace by grouping together similar terms into concepts. As such, each concept can be described using many different keywords as it has a high discriminatory power to other concepts in the reduced feature space. See Appendix B for more detailed information about LSI using SVD.

## 2.2.3. Optimal dimension selection

The intensity of dimension reduction during the SVD phase is critical. Ideally, the number of concepts k, must be large enough to fit all the underlying, relevant concepts in the email collection, but small enough to prevent the model from fitting sampling errors and unimportant details. Moreover, the obtained optimal k must be workable from a prediction point of view. In the factor-analytic literature, such choices are still an unanswered question. Deerwester et al. [12] propose using an operational criterion, i.e. a value of k that yields good performance. In our application, we are especially interested in the predictive performance of the SVD output.

It is not possible to know what value of k will lead to an optimal solution when validating the predictive model initially. As such, improper selection of the parameter k is ineffective if too few concepts are included or computational expensive if too many irrelevant concepts are incorporated. Consequently, a parameter-selection procedure is needed. We construct several rank-k models and the most favorable rank-k model (based on the cross-validated performance) is retained for further analysis. As such, the optimal value of k is obtained using a fivefold cross-validation on the training set. The training set is divided into five subsets of equal size.

Iteratively, each part is used for validation, while the other parts are used for training. So finally, each case in the training set is predicted once. The cross-validation performance better reflects the real performance when validating the classifier for unseen data. In the end, it is possible to select the optimal value of k based on the most favorable cross-validated model. Kim [18] stated that it is very important for data analysts to consider the relationship between the amount of information and the complexity of predictive models because compact information models show great improvement in terms of predictive performance and robustness.

## 2.3. Modeling

## 2.3.1. Modeling technique and variable selection

Logistic regression is used. In applying it, a maximumlikelihood function is produced and maximized in order to become an appropriate fit to the data [3]. With a training set of $\mathrm { T } = \{ ( \mathbf { x } _ { i } , \mathbf { y } _ { i } ) \}$ and $i = \{ 1 , 2 , . . . , N \}$ and input data $\mathbf { X } _ { i } \in \mathbf { R } ^ { n }$ and corresponding binary target labels $y _ { i } \in \{ 0 , 1 \}$ , logistic regression is used to estimate the probability $P ( y = 1 { \big | } \mathbf { x } )$ given by

$$
P (y = 1 | \mathbf {x}) = \frac {1}{1 + \exp (- (w _ {0} + \mathbf {w x}))}\tag{2}
$$

with $\mathbf { x } \in \mathbf { R } ^ { n }$ an n-dimensional input vector, w the parameter vector and $w _ { 0 }$ the intercept.

This technique is used because it is conceptually simple [8], a closed-form solution for the posterior probabilities is available and Neslin et al. [23] stated that it provides quick and robust results in a churn-prediction context.

Variable selection is the process of choosing a subset of the original variables by eliminating some variables based on their predictive performance. Kim [18] stated that there are three main reasons for using a variable-selection technique: saving computational time and cost by extracting as much information with the smallest number of variables, improving the comprehensibility of the resulting models and making the model generalize better.

Our study employs a forward-selection procedure: the algorithm added one variable at a time. The first variable to enter the model is that with the highest $\chi ^ { 2 } .$ -statistic. At each step, the remaining variables are considered for inclusion in the final model. Forward selection adds variables until a stopping rule is satisfied. The choice of this standard variable-selection technique makes it easy for implementation, while more sophisticated algorithms are computationally more expensive and require additional parameter settings.

## 2.3.2. Evaluation criteria

To evaluate the performance of classification models, two commonly used criteria are used: the lift and the area under the receiving operating curve (AUC).

Lift is the most commonly used performance measure for evaluating classification models. It reflects the increase in density of the churn event relative to the density of churners in the total database. The higher the lift, the better the predictive model. In marketing applications, it is interesting to increase the density of churners, especially in the top 10% cases most likely to churn. Marketing-decision makers are typically interested in only 10% of the entire marketing database because budgets are often limited and actions to reduce churn typically involve only 10% of the entire customer database. Practically, all cases are sorted from most likely to churn to least likely to churn. Afterwards, the density of churners from the top 10% cases most likely to churn is compared with the density of churners in the entire customer collection. This increase in density is called the top-decile lift. Intuitively, a top-decile lift of two means that the density of churners in the top 10% cases most likely to churn is twice the density of churners in the entire database.

The AUC takes into account the predicted class of an event with the real class of that event, considering all possible cut-off values. Consequently, the AUC takes into account the individual class performance for a range of possible thresholds. If true positives (TP) are the number of positives that are correctly identified, false positives (FP) are the number of negatives that are classified as positives, false negatives (FN) are the number of positive cases that are identified as negatives and true negatives (TN) are the number of negative cases that are classified as negatives, then

 the sensitivity is (TP/(TP+FN)): the proportion of positive cases that are predicted to be positive;

 the specificity is (TN/(TN + FP)): the proportion of negative cases that are predicted to be negative.

These vary when the threshold value is varied. The receiver operation characteristics curve (ROC) is a twodimensional plot of the sensitivity versus (1-specificity). In order to compare the performance of two or more classification models, the area under the receiver operating characteristics curve is calculated. This measure is used to evaluate the performance of a binary classification system [15]. In order to test if two AUCs are significantly different, one can apply the non-parametric test of Delong et al. [13].

## 3. Empirical verification

## 3.1. Research data

In our study, we used data obtained from a large Belgian newspaper publishing company. Subscribers have to pay a fixed price for their newspapers, depending on the length of subscription and the promotional offer given. The company does not allow subscribers to end their subscription before the expiry date. The churn-prediction problem therefore involves predicting whether a subscription will be renewed during the 4-week period after maturity. During this period, the newspaper publishing company still delivers the newspapers in order to allow subscribers time to renew their subscription. The company has a structured, marketing database where transactional and subscription related information is stored and they save all customer emails sent to the call center. Fig. 3 shows the time window of analysis in our study.

![](/api/attachments/9WJAT3YK/fulltext/images/a41aca3843046580f25ccc092e920c889815d59c5f1453366507397c474d40b7.jpg)  
Fig. 3. Time window of analysis.

Subscription data from January 2002 to September 2005 was analyzed. Consequently, it is possible to define the dependent and the explanatory variables. All renewal points between July 2004 and July 2005 were considered. A customer was seen as a ‘churner’ when the subscription was not renewed in a 4-week period following the maturity date. The explanatory variables were constructed from the two available types of information. These were used to predict whether a subscription would be renewed.

The first type of variables contained information from the structured, marketing database. These variables contained information on a 30-month period. They were subdivided into four categories (see Appendix C):

 client/company interaction variables,

 subscription related variables,

 renewal specific variables and

 socio-demographics.

The second type of information consisted of all information sent by the subscriber via email during the last period of his/her subscription. Because this information is highly unstructured, the emails were preprocessed to represent them in our churn-prediction model.

In order to compare the beneficial effect of unstructured information from call center emails in a churnprediction model, subscriptions with at least one email sent during the last term of the subscription were considered.

Tables 1 and 2 summarize the data characteristics for the randomly split training and test set. The training set was used to obtain the optimal SVD dimension and the model estimates, while the test set is used to validate and compare the different models.

Table 1

Overview of the marketing data characteristics

<table><tr><td></td><td>Number of subscriptions</td><td>Relative percentage</td></tr><tr><td colspan="3">Training set</td></tr><tr><td>Subscriptions not renewed</td><td>1777</td><td>18.50</td></tr><tr><td>Subscriptions renewed</td><td>7826</td><td>81.50</td></tr><tr><td>Total</td><td>9603</td><td>100.00</td></tr><tr><td colspan="3">Test set</td></tr><tr><td>Subscriptions not renewed</td><td>593</td><td>18.76</td></tr><tr><td>Subscriptions renewed</td><td>2568</td><td>81.24</td></tr><tr><td>Total</td><td>3161</td><td>100.00</td></tr></table>

## 3.2. Optimal dimension selection

The text pre-processing phase resulted in a highdimensional term-by-email matrix. This was unworkable from a prediction point of view. Its optimal reduced rank was obtained by applying a cross-validation procedure on the training data. Fig. 4 shows the results of this crossvalidation; the x-axis has the number of concepts and the yaxis represents the cross-validated AUC. It is clear that in the range of 1–100 concepts, the cross-validated performance was increasing rapidly. From 100 concepts on, the crossvalidated AUC was growing less rapidly, while in the region around 170 concepts, the cross-validated performance was stabilizing. Including more than 170 concepts resulted in a more complex churn model, while the predictive perfor mance hardly increased. Thus 170 concepts was chosen as the optimal number for representing the textual information in our study. At this point, a good balance was achieved between the number of concepts and the predictive performance.

Table 2  
Overview of the call center emails characteristics

<table><tr><td></td><td>Number of emails</td><td>Average number of mails per subscription</td><td>Average number of words per email</td><td>Average number of words per sentence</td><td>Average number of unique words per email</td></tr><tr><td>Training set</td><td>14,083</td><td>1.47</td><td>113.27</td><td>28.98</td><td>72.54</td></tr><tr><td>Test set</td><td>4,694</td><td>1.48</td><td>116.33</td><td>29.33</td><td>72.49</td></tr></table>

![](/api/attachments/9WJAT3YK/fulltext/images/721c8e310435d4f3e9a4ba947a76b126b00475f5e68de3c4e561c8acbea5f700.jpg)  
Fig. 4. The cross-validated AUC during the optimal dimension selection phase.

## 3.3. Defining the best subset of the structured marketing variables

Before comparing the predictive performance of the model with structured marketing information only (Mod-Struc) to the performance of the model that combined the structured marketing information and textual information (ModStruc–Unstruc), the optimal set of structured marketing variables was found by employing the forward-selection procedure. It resulted in a best subset of 20 marketing variables (see Table 3).

Best subset of marketing variables employed by the forward-selection procedure

<table><tr><td>Step</td><td>Variable name</td></tr><tr><td>1</td><td>Elapsed time since the last complaint</td></tr><tr><td>2</td><td>Monetary value</td></tr><tr><td>3</td><td>Elapsed time since last suspension</td></tr><tr><td>4</td><td>The length of the current subscription</td></tr><tr><td>5</td><td>The average positioning of complaints in the current subscription (with 0 = start of the subscription and 1 = end of subscription)</td></tr><tr><td>6</td><td>Whether the previous subscription was renewed before the expiry date</td></tr><tr><td>7</td><td>Whether the subscriber is a woman</td></tr><tr><td>8</td><td>The variance in the number of days the previous subscriptions are renewed before expiry date</td></tr><tr><td>9</td><td>The number of renewal points</td></tr><tr><td>10</td><td>Whether the newspaper edition is ‘X1’</td></tr><tr><td>11</td><td>Whether the subscriber is a public institution</td></tr><tr><td>12</td><td>How many days before the expiry date, the previous subscription was renewed</td></tr><tr><td>13</td><td>The number of suspensionsx</td></tr><tr><td>14</td><td>The average suspension length (in number of days)x</td></tr><tr><td>15</td><td>The number of suspensions</td></tr><tr><td>16</td><td>The average suspension length (in number of days)</td></tr><tr><td>17</td><td>Whether the purchase motivator is a direct marketing campaign</td></tr><tr><td>18</td><td>Whether the newspaper is picked up at the shop</td></tr><tr><td>19</td><td>Elapsed time since last conversion in payment method</td></tr><tr><td>20</td><td>The conversions made in payment methodx</td></tr></table>

x: variable corrected for the length of subscription.

Modstruc was built using the 20 marketing variables, while ModStruc–Unstruc was a combination of those 20 marketing variables with those variables representing the textual information—i.e. 170 additional variables.

## 3.4. Comparing predictive performance

Table 4, Figs. 5 and 6 show that the predictive performance of ModStruc–Unstruc significantly outperformed that of ModStruc. The AUC increased from 73.80 to 77.75 by adding textual information to a traditional churnprediction model. This improvement was significant $( \chi ^ { 2 } = 2 3 . 1 , \ \mathrm { d . f . } = 1 , \ p < 0 . 0 0 1 )$ . The ROC curve of Mod-Struc–Unstruc is located further from the random model than that of ModStruc, thus the area under the ROC of ModStruc– Unstruc is larger than that of ModStruc. ModStruc–Unstruc was thus able to better distinguish churners from nonchurners. Moreover, the beneficial effect of textual information on predictive performance was confirmed in terms of top-decile lift. The cumulative lift curve of ModStruc-Unstuc laid above that of ModStruc. ModStruc–Unstruc is able to identify more customers truly at risk than ModStruc within a specific decile. Lift in the first decile or the 10% top-decile – i.e. the 10% point – increased from 2.69 to 3.07.

Our study provided a realistic framework that increased the predictive performance of a churn model for subscribers

The performance of ModStruc and ModStruc–Unstruc: AUC and top-decile lift on the test set

<table><tr><td></td><td>AUC</td><td>Top-decile lift</td></tr><tr><td>ModStruc</td><td>73.80</td><td>2.69</td></tr><tr><td>ModStruc–Unstruc</td><td>77.75</td><td>3.07</td></tr></table>

![](/api/attachments/9WJAT3YK/fulltext/images/b6d84fa1c9a00fa2bd830bd7b6fb3585a76efd98f583a65f3e364427e7e5e13b.jpg)  
Fig. 5. The ROC curves for ModStruc, ModStruc–Unstruc and the random model (or the zero-information model).

whose textual information is available. Since ModStruc and ModStruc–Unstruc were built on a selective sample of subscribers who contacted the company at least once per email, one may suggest including more subscribers—i.e. those who did not send an email. One should verify whether a separate churn model of subscribers who sent at least one email is the best strategy in obtaining optimal predictive performance. Practically, the current training set of subscribers was extended by randomly selecting subscriptions of customers who had not send any email (ModStruc-k, with k the number of randomly selected subscriptions whereby $k = \{ 0 ; 5 0 0 0 ; 1 0 , 0 0 0 ; . . . ; 1 0 0 , 0 0 0 \}$ with the intent of building a churn model with better predictive performance on the current test set. Fig. 7 graphically indicates the results. The horizontal lines indicating the performance of ModStruc and ModStruc–Unstruc are included for reasons of comparability, despite the fact that they were independent of k.

As one observes from Fig. 7, it was indeed better to build a separate model for subscribers who sent at least one email. The predictive performance of ModStruc was always higher than ModStruc-k. This clearly pointed out that subscribers from whom textual information was available have a unique churn pattern. The performance of ModStruc–Unstruc dominated those of ModStruc and ModStruc-k.

![](/api/attachments/9WJAT3YK/fulltext/images/0966b7e0e5d3105fe064bfb40ea889601d63dcfdf74cce83cd33fb087a466175.jpg)  
Fig. 6. The cumulative lift charts of ModStruc and ModStruc–Unstruc.

![](/api/attachments/9WJAT3YK/fulltext/images/9d9c58dc28bae34d1d1a759772ab30ec71e5189e4946a296eca4cc15b9d8fa2d.jpg)  
Fig. 7. The AUC performance of ModStruc–Unstruc, ModStruc and ModStruc-k.

## 4. Conclusion

Adding the VOC by means of call center emails into a standard churn-prediction system helps marketing-decision makers to identify with a higher precision those customers most prone to switch. Consequently, retention campaigns to these customers can become more targeted. The framework integrated textual information from call center emails with traditionally used marketing information. Converting the unstructured call center emails into a structured form suitable for churn prediction, required specialized preprocessing and dimension reduction steps.

Moreover, our study confirmed the importance of a wellconsidered email handling strategy. It provided a methodology that may increase the profitability of the call center by offering a model for marketing-decision makers using customers of whom textual information is available. By enriching the churn model with this unstructured information from call center emails, marketing managers may improve the effectiveness of their retention campaigns.

## Acknowledgments

We would like to thank the anonymous Belgian Company for their efforts in providing us with their data. Moreover, we also like to thank (1) BOF (01D26705) for funding the PhD project of Kristof Coussement, (2) BOF (011B5901) for funding the computing infrastructure and (3) Jonathan Burez, Bart Larivie\`re and Ilse Bellinck for their insights and suggestions during this project. This project was realized using SAS v9.1.3, SAS Text Miner v5.2 and Matlab v7.0.4.

## Appendix A. Term vector-weighting phase

The term frequency (tf) measures the frequency of occurrence of an index term in the email text. The more a term is present, the more important this term is in characterizing the content of that email. As such the frequency of occurrence of a content word is used to indicate term importance for content representation [4,20,30]. In ou study, the tf was obtained by taking a logarithmic transformation of the original term frequency. Taking the logarithmic transformation reduced the importance of the raw tf, which was important for email collections of varying length.

The inverse document frequency (idf) was incorporated so that the more rare a term occurred in the collection of emails, the more discriminating it was. Therefore, the weight of a term was inversely related to the number of emails in which the term occurred—i.e. the frequency of the term [14,32]. The logarithm of the idf was taken to decrease the effect of the raw idf-factor.

Finally the weight of term i in an email $j \left( w _ { i j } \right)$ was given by

$$
w _ {i j} = \operatorname{tf} _ {i j} \operatorname{idf} _ {i}\tag{A.1}
$$

with $\mathrm { t f } _ { i j }$ equal to the term frequency of term i in email j; idf is equal to the inverse email frequency of term i.

Mathematically,

$$
\mathrm{tf} _ {i j} = \log_ {2} (n _ {i j} + 1)\tag{A.2}
$$

with $n _ { i j }$ equal to the frequency of term i in email j and

$$
\mathrm{idf} _ {i} = \log_ {2} \left(\frac {n}{d f _ {i}}\right) + 1\tag{A.3}
$$

with n equal to the total number of emails in the entire email collection and $d f _ { i }$ equal to the number of emails where term i was present.

## Appendix B. Dimension reduction using LSI via SVD

A high-dimensional term-by-email matrix A was constructed so that location $( i , j )$ indicated $w _ { i j }$ the weight of term i for email j. SVD factorized A into three distinct matrices by

$$
A = U \Sigma V ^ {t}\tag{B.1}
$$

with S equal to a diagonal matrix containing the singular values of matrix A, U equal to the term-concept similarity matrix and V equal to the concept-email similarity matrix.

Mathematically, $\Sigma = \mathrm { d i a g } ( \lambda _ { 1 } , ~ \lambda _ { 2 } , ~ . ~ . ~ . , ~ \lambda _ { r } )$ was the singular-values matrix where $\lambda _ { 1 } \geq \lambda _ { 2 } \geq \lambda _ { 3 } \geq . . . \geq \lambda _ { r } ~ U$ and V were column-orthonormal matrices. The weights of the original matrix depended on the latent concepts by

$$
w _ {i j} = \sum_ {x = 1} ^ {r} U _ {i x} \Sigma_ {x} d _ {j x}\tag{B.2}
$$

LSI based on SVD allowed a simple strategy to approximate the original matrix A with rank r by A<sup>ˆ</sup> with rank k where $k \leq r .$ Therefore, LSI ignored the smaller lambda values in S by retaining only the first predetermined singular values equal to or greater than k, i.e. $\lambda _ { 1 } \geq \lambda _ { 2 } \geq \lambda _ { 3 } \geq . . . \geq \lambda _ { k } ,$ while only the first k columns of U and V were retained.

$$
\hat {A} _ {k} = U _ {k} \Sigma_ {k} V _ {k} ^ {t}\tag{B.3}
$$

with $U _ { k , \ } \Sigma _ { k }$ and $V _ { k }$ were equal to the k-rank approximation of U, S and V, respectively.

Matrix $V _ { k }$ is the approximated k-rank concept-email similarity matrix. A cell in the matrix $V _ { k }$ represented the loading for a specific email on one of the k concepts. This matrix contained information on how well a certain email loads on the different k concepts. The concepts reflected the hidden patterns in the textual data. Consequently, these concepts were used as explanatory variables in the churnprediction model because they represented the latent semantic patterns of the textual information.

It is important that the concept loadings from the training vectors were comparable with those from the test vectors. The meaning of the concepts during testing should stay the same as those during training. Consequently, emails of the test set were projected into the same semantic latent subspace as created during training.

In order to compare a test email d with the training emails, its term vector $A _ { d }$ was derived using the same preprocessing steps. Deerwester et al. [12] proposed projecting each new term vector into the same latent semantic subspace as that created during training by

$$
V _ {d} = A _ {d} ^ {\prime} U _ {k} \Sigma_ {k} ^ {- 1}\tag{B.4}
$$

with $U _ { k }$ the k-rank concept-term similarity matrix and $\Sigma _ { k }$ the diagonal singular value matrix in rank k, both of the original SVD. $V _ { d }$ was the new concept-email vector which was comparable to the concept-email vectors of the matrix $V _ { k } .$

However, the choice of k was critical for optimal predictive performance.

## Appendix C. Overview of structured marketing information

Client/company-interaction variables: variables describ ing the client/company relationship:

 The number of complaints.

 Elapsed time since the last complaint.

 The average cost of a complaint (in terms of compensation newspapers).

 The average positioning of the complaints in the current subscription.

 The purchase motivator of the subscription.

 How the newspaper is delivered.

 The number of conversions made in distribution channel, payment method and edition.

 Elapsed time since last conversion in distribution channel, payment method and edition.

 The number of responses on direct marketing actions.

 The number of suspensions.

 The average suspension length (in number of days).

 Elapsed time since last suspension.

 Elapsed time since last response on a direct marketing action.

 The number of free newspapers.

Renewal-related variable: variables containing renewalspecific information:

 Whether the previous subscription was renewed before the expiry date.

 How many days before the expiry date, the previous subscription was renewed.

 The average number of days the previous subscriptions are renewed before expiry date.

 The variance in the number of days the previous subscriptions are renewed before expiry date.

 Elapsed time since last step in company retention procedure.

 The number of times the customer did not renew a subscription.

Socio-demographic variables: variables describing the subscriber:

 Age.

 Whether the age is known.

 Gender.

 Physical person (is the subscriber a company or a physical person).

 Whether contact information (telephone, mobile number, email) is available.

Subscription-describing variables: group of variables describing the subscription:

 Elapsed time since last renewal.

 Monetary value.

 The number of renewal points.

 The length of the current subscription.

 The number of days a week the newspaper is delivered (intensity indication).

 Which edition the subscriber has (X1, X2, X3).

 The month of contract expiration.

## References

[1] M. Adria, S.D. Chowdhury, Centralization as a design consideration for the management of call centers, Information and Management 41 (4), 2004, pp. 497–507.

[2] K. Alajoutsijarvi, K. Mannermaaa, H. Tikkanen, Customer relationships and the small software firm: a framework for understanding challenges faced in marketing, Information and Management 37 (3), 2000, pp. 153–159.

[3] P.D. Allison, Logistic Regression using the SAS System: Theory and Application, SAS Institute Inc., Cary, NC, 1999.

[4] P.B. Baxendale, Machine-made Index for technical literature—an experiment, IBM Journal of Research and Development 2 (4), 1958, pp. 354–361.

[5] C. Bell, K.P. Jones, Toward everyday language information retrieval systems via minicomputers, Journal of the American Society for Information Sciences 30, 1979, pp. 334–338.

[6] M.W. Berry, Z. Drmac, E. Jessup, Matrices, vector spaces, and information retrieval, SIAM Review 41, 1999, pp. 335–362.

[7] I. Bose, R.K. Mahapatra, Business data mining—a machine learning approach, Information and Management 39 (3), 2001, pp. 211–225.

[8] R.E. Bucklin, S. Gupta, Brand choice, purchase incidence and segmentation: an integrated modeling approach, Journal of Marketing Research 29 (2), 1992, pp. 201–215.

[9] J. Burez, D. Van den Poel, CRM at a pay-TV company: using analytical models to reduce customer attrition by targeted marketing for subscription services, Expert Systems with Applications 32 (2), 2007, pp. 277–288.

[10] R.G. Cooper, E.J. Kleinschmidt, Determinants of timeliness in product development, Journal of Product Innovation Management 11 (5), 1994, pp. 381–396.

[11] J.J. Cristiano, J.K. Liker, C.C. White, Customer-driven product development through quality function deployment in the US and Japan, Journal of Product Innovation Management 17 (4), 2000, pp. 286–308.

[12] S. Deerwester, S. Dumais, G. Furnas, T. Landauer, R. Harshman, Indexing by latent semantic analysis, Journal of the American Society for Information Science 41 (6), 1990, pp. 391–407.

[13] E.R. DeLong, D.M. DeLong, D.L. Clarke-Pearson, Comparing the areas under two or more correlated receiver operating characteristic curves: a nonparametric approach, Biometrics 44 (3), 1988, pp. 837– 845.

[14] W.R. Greiff, A theory of term weighting based on exploratory data analysis, in: W.B. Croft, A. Moffat, C.J. van Rijsbergen, R. Wilkinson, J. Zobel (Eds.), in: Proceedings of the 21st SIGIR Conference, New York:ACM, 1998, pp. 11–19.

[15] J.A. Hanley, B.J. McNeil, The meaning and use of the area under a receiver operating characteristic (ROC) curve, Radiology 143 (1), 1982, pp. 29–36.

[16] B. Karakostas, D. Kardaras, E. Papathanassiou, The state of CRM adoption by the financial services in the UK: an emperical investigation, Information and Management 42 (6), 2005, pp. 853– 863.

[17] S. Keaveney, M. Parthasarathy, Customer switching behavior in online services: an exploratory study of the role of selected attitudinal, behavioral and demographic factors, Journal of the Academy of Marketing Science 29 (4), 2001, pp. 374–390.

[18] Y.S. Kim, Toward a successful CRM: variable selection, sampling and ensemble, Decision Support Systems 41 (2), 2006, pp. 542–553.

[19] W. Kraaij, R. Pohlmann, Viewing Stemming as Recall Enhancement, in: Proceedings of the 19th Annual International ACM SIGIR Con ference on Research and Development in Information Retrieval, Zurich, Switzerland, 1996, pp. 40–48.

[20] H.P. Luhn, A statistical approach to mechanized encoding and searching of literary information, IBM Journal of Research and Development 4 (4), 1957, pp. 600–605.

[21] K. Matzler, H.H. Hinterhuber, How to make product development projects more successful by integrating Kano’s model of customer satisfaction into quality function deployment, Technovation 18 (1), 1998, pp. 25–38.

[22] G.A. Miller, E.B. Newman, Tests of a statistical explanation of the rank-frequency relation for words in written English, American Journal of Psychology 71 (23), 1958, pp. 209–218.

[23] S.A. Neslin, S. Gupta, W. Kamakura, J. Lu, C. Mason, Defection detection: measuring and understanding the predictive accuracy of customer churn models, Journal of Marketing Research 43 (2), 2006, pp. 204–211.

[24] S.L. Pan, J.N. Lee, Using e-CRM for a unified view of the customer, Communications of ACM 46 (4), 2003, pp. 95–99.

[25] M. Pontes, C. Kelly, The identification of inbound call center agents competencies that are related to callers’ repurchase intentions, Journal of Interactive Marketing 14 (3), 2000, pp. 41–49.

[26] W. Reinartz, V. Kumar, The impact of customer relationship characteristics on profitable lifetime duration, Journal of Marketing 67 (1), 2003, pp. 77–99.

[27] G. Salton, A Theory of Indexing, J.W. Arrowsmith, Bristol, UK, 1975.

[28] G. Salton, Automatic text processing: the transformation, Analysis and Retrieval of Information by Computer, Reading MA: Addison-Wesley, 1989.

[29] G. Salton, C. Buckley, Term-weighting approaches in automatic text retrieval, Information Processing & Management 24 (5), 1988, pp. 513–523.

[30] G. Salton, M.J. Mcgill, Introduction to Modern Information Retrieval, Mcgraw-Hill, New York, 1983.

[31] G. Salton, The SMART Retrieval System: Experiments in Automatic Document Processing, Prentice Hall, Englewood Cliffs, NJ, 1971.

[32] G. Salton, C.S. Yang, Specification of term values in automatic indexing, Journal of Documentation 29 (4), 1973, pp. 351–372.

[33] K. Sparck Jones, A statistical interpretation of term specificity and its application in retrieval, Journal of Documentation 28 (1), 1972, pp. 11–21.

[34] K. Sparck Jones, Index term weighting, Information Storage and Retrieval 9 (11), 1973, pp. 619–633.

[35] I. Spiegler, Technology knowledge: bridging a ‘‘Generating’’ gap, Information and Management 40 (6), 2003, pp. 533–539.

[36] D. Van den Poel, B. Larivie\`re, Customer attrition analysis for financial services using proportional hazard models, European Journal of Operational Research 157 (1), 2004, pp. 196–217.

[37] G.K. Zipf, Human Behaviour and the Principle of Least Effort, Addison-Wesley, Cambridge, MA, 1949

![](/api/attachments/9WJAT3YK/fulltext/images/ce55b9a64f316717e5bd6cb149d19d333aca9d4d15fe130d430c3ea5b733b7a9.jpg)  
Expert Systems with Applications.

Kristof Coussement is a PhD candidate in economics and business administration at Ghent University (Belgium). He received his master degree in applied economics as well as his master after master degree in marketing analysis at Ghent University (Belgium). During his PhD thesis, he investigated the impact of client/company interactions through verbalized information sources on CRM (churn analysis). His works are published in Decision Support Systems and

![](/api/attachments/9WJAT3YK/fulltext/images/13f70c0deceacf34e8d31f623e0afdaedb8364650254f9303d9812de4dd77804.jpg)

Dirk Van den Poel is professor of marketing at the Faculty of Economics and Business Administration of Ghent University, Belgium. He heads a competence center on analytical customer relationship management (aCRM). He received his degree of management/business engineer as well as his PhD from K.U. Leuven (Belgium). His main interest fields are the quantitative analysis of consumer behavior (CRM), data mining (genetic algorithms, neural networks, random forests, random multinomial logit:

RMNL), text mining, optimal marketing resource allocation (DIMAR-OPT) and operations research. His works are published in Decision Support Systems, Journal of Business Research, European Journal of Operational Research, Journal of the Operational Research Society, International Journal of Intelligent Systems and Expert Systems with Applications.
