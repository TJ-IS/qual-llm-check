---
otero_id: 19747
otero_key: "7WPU8EUY"
title: "Predicting employee absenteeism for cost effective interventions"
authors: "Natalie Lawrance; George Petrides; Marie-Anne Guerry"
year: "2021"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2021.113539"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Predicting employee absenteeism for cost effective interventions

Natalie Lawrance <sup>a,\*</sup>, George Petrides <sup>a,b</sup>, Marie-Anne Guerry <sup>a</sup>

<sup>a</sup> Department of Business Technology and Operations, Vrije Universiteit Brussel, Pleinlaan 2, 1050 Brussels, Belgium <sup>b</sup> Department of Informatics, University of Bergen, Norway

## A R T I C L E I N F O

Keywords: Cost-sensitive learning Classification HR analytics Absenteeism prediction

## A B S T R A C T

This paper describes a decision support system designed for a Belgian Human Resource (HR) and Well-Being Service Provider. Their goal is to improve health and well-being in the workplace, and to this end, the task is to identify groups of employees at risk of sickness absence who can then be targeted with interventions aiming to reduce or prevent absences. To facilitate deployment, we apply a range of existing machine-learning methods to obtain predictions at monthly intervals using real HR and payroll data that contains no health-related predictors. We model employee absence as a binary classification problem with loss asymmetry and conceptualise a misclassification cost matrix of employee sickness absence. Model performance is evaluated using cost-based metrics, which have intuitive interpretation. We also demonstrate how this problem can be approached when costs are unknown. The proposed flexible evaluation procedure is not restricted to a specific model or domain and can be applied to address other HR analytics questions when deployed. Our approach of considering a wider range of methods and cost-based performance evaluation is novel in the domain of absenteeism prediction.

## 1. Introduction

Employee sickness absence or absenteeism, broadly defined as failure to attend scheduled work as a result of ill health, is a pervasive problem disruptive to operations and costly to the economy. The annual cost of worker absenteeism in the countries of the Organisation for Economic Co-operation and Development (OECD) has been estimated to be be tween 1.2 and 2% of their total GDP [1], which in current terms trans lates to between 0.6 and 1 trillion US dollars [2]. It is therefore only natural for employers to seek solutions to this problem.

The motivation for this work was the request of a company in Belgium specialising in Human Resource (HR) Management and Well-Being for the development of a solution to address employee absen teeism using data science. A direction for finding a possible solution stemmed from the fact that as much as 20% of the working-age popu lation in the OECD countries suffers from common mental illnesses such as anxiety and depression disorders [3], and timely application of pre ventive measures is crucial in avoiding transition to long-term illness and disability [1]. Interventions in the form of health management or wellness programs have a long history and several meta-analytic studies have reported strong evidence of their effectiveness at reducing employee absenteeism [4–6]. Examples of such interventions can include individual fitness program, stress-management seminars, private or group therapy sessions, and work flexibility arrangements, to name a few.

Naturally, such wellness programs are costly, both in terms of monetary costs for their implementation (which might not always be available due to budget limitation), and hours spent for participation. Therefore, the simplest solution of applying them to all employees at a workplace might not be the most cost-effective. Instead a design a de cision support system is needed that is able to identify the employees at risk of sickness absence, typically only a small fraction of the workforce, who should then be targeted with a preventive action.

## 1.1. Related work

HR analytics is most commonly applied to talent acquisition [7] or retention [8], rather than maintaining and improving the well-being of employees. As observed in [9], the absenteeism prediction literature to date has mostly been concerned with the explanation and association of various risk factors with employee absenteeism, rather than accuracy of predictions. The majority of contributions to the domain of absenteeism prediction come from the field of occupational health and medicine [10–17]. In this field, statistical techniques such as logistic regression and Cox proportional-hazards models are preferred and training data is collected either in the clinical setting or as part of a nation-wide

household survey.

Another strand of literature focusses solely on predicting sickness absence using algorithmic models. Among those, several studies [18–20] approach employee sickness absence as a regression problem using neural networks that predict hours of absence on the data collected in [20]. [21] uses the same dataset in a multi-class classifica tion setting using decision tree ensembles to predict absences of specific duration.

The main drawback in all of those studies is lack of transparency with regards to their experimental set-up and model selection procedure. Most contributions apply a single algorithm to a single dataset, the rationale behind the model choice and evaluation being rarely dis cussed. In contrast, in this paper we consider a wide range of state-of the-art algorithms and relevant evaluation measures.

Previous studies involved data collection in several waves, usually annually. However, predictions with a horizon of one year are of little relevance to businesses that are trying to reduce direct and indirect costs incurred through loss of productivity and disruption to operations. What is more desirable is the ability of the management to obtain reliable predictions at operationally practical intervals (such as a month or a quarter) preferably with data that is readily available from HR and payroll records. An attempt has been made in [22] to predict sickness absence using only such data from one industry sector, albeit at the impractical one-year prediction horizon. The data we have been pro vided with for this work does not contain health-related or attitudinal information either, but includes several sectors and allows us to consider a more practical prediction horizon of one month.

Finally, as already mentioned, absenteeism is an event of relative rarity with only a small fraction of the population falling out of the workforce in any given period. Most absenteeism prediction papers do demonstrate an imbalanced class distribution of the outcome variable. Not accounting for this class imbalance in predictive models has im mediate negative implications for model performance [23,24]. To the best of our knowledge, [25] is the only paper that recognises the importance of class imbalance correction and models sickness absence as a problem with loss asymmetry where cost of misclassifying an ab sentee is set to the number of non-absentees in the dataset, and viceversa. This heuristic is commonly applied to treat class imbalance alone, but could be suboptimal when real costs can actually be specified. Specifying them is what we attempt to do to simultaneously address class imbalance and cost asymmetry using cost-sensitive learning.

## 1.2. Our contribution

In this work we investigate the use of predictive analytics as a de cision support system for increasing employee well-being in the work place by identifying groups of employees at risk of sickness absence that should be targeted with a wellness intervention.

Firstly, we employ cost-sensitive learning to treat the unequal misclassification costs pertaining absenteeism, something we could not find in the existing literature. Our main contribution is the con ceptualisation of a relevant misclassification cost matrix, which can be generalised to a variety of institutional and legislative contexts, and consequently to other datasets as well. A core element of our cost matrix is information on the effectiveness an intervention has on individuals, which is currently lacking and therefore identified as an important di rection for future research and requires collaboration between academia and industry. We also develop business-friendly cost-based evaluation metrics that have an intuitive interpretation.

Secondly, since our data did not contain information on one of the parameters of our cost matrix, we also consider a cost-insensitive approach. We evaluate performance using balanced accuracy, which assumes that misclassification errors have equal severity, despite the class imbalance.

Finally, we try to illustrate best practices in the domain of absen teeism prediction for the practitioner. For this, we use an anonymised dataset that a Belgian HR and Well-Being company provided us, which contains employee payroll information only, without any health-related data. We specify different cost-matrices by considering different realistic scenarios for interventions and their (fictional) effectiveness, and consider a practical prediction horizon of one month. We follow a rigorous experimental design to prevent over-fitting and develop a flexible algorithm-agnostic evaluation framework. In the end, a selec tion of tree-based classifiers, both cost-sensitive and cost-insensitive, is evaluated on the same cost-matrices, and the advantages and disad vantages of both approaches are discussed.

## 2. Preliminaries

In what follows we will briefly outline the challenges of classification on imbalanced data. Readers familiar with the material are invited to continue to Section 3.

A classifier is a function $\boldsymbol { f } : \boldsymbol { x } { \to } \boldsymbol { \widehat { y } }$ that maps a vector of real-valued predictors $\boldsymbol { x } \in \mathbb { R } ^ { n }$ to a predefined target class $\widehat { \mathbf { y } } \in$ ℝ based on a training set of data with known true class labels $y \in \mathbb { R } .$ . In a binary classification setting, it is common to consider class labels $y , \widehat { y } \in \{ 0 , 1 \}$ , with the rare class referred to as positive and labelled as 1.

Most binary classifiers produce predictions in two stages: First a confidence score ∈ [0,1] is produced for each observation. Then, an instance i is classified as positive $( \widehat { y } _ { i } = 1 )$ if its score is greater than a threshold T, and as negative otherwise. Most classifiers implicitly as sume $T = 0 . 5 ,$ which often results in poor classifier performance under class imbalance [23,26].

The typical loss function adopted to measure a classifier’s prediction accuracy is the 0–1 loss function, which counts the instances of incorrect classification. More detailed error analysis can be conducted using a confusion matrix, an example of which is shown in Table 1. Each entry in the confusion matrix represents the number of observations in the test set that were classified either correctly or incorrectly. The error count is thus split between two error types: false positives and false negatives.

## 2.1. Cost-sensitive decision-making

In most domains different misclassification errors entail different costs, known as cost asymmetry or sometimes cost skew or imbalance, and therefore the question of which of the error types is more costly is determined by the area of application. When the problem under consideration suggests cost asymmetry a cost-sensitive classification approach becomes appropriate [23]. Cost-sensitive learning translates the error-minimisation problem to cost-minimisation, where each pre diction type (as defined in the confusion matrix) is assigned a cost by means of a misclassification cost matrix $\left( \begin{array} { l l } { C _ { T P } } & { C _ { F N } } \\ { C _ { F P } } & { C _ { T N } } \end{array} \right)$ . This matrix can be either class-dependent, where all observations of a class entail identical costs, or they can be record-dependent in which case every observation i has its own cost matrix $\left( \begin{array} { l l } { C _ { T P } ^ { i } } & { C _ { F N } ^ { i } } \\ { C _ { F P } ^ { i } } & { C _ { T N } ^ { i } } \end{array} \right)$ , derived from a given dataset.

An important result derived by Elkan [27] is that in the case where misclassification costs are known, any classifier can be made costsensitive by adopting a decision threshold that incorporates these costs, a method referred to as Direct Minimum Expected Cost Classification (DMECC) [28,29]. Here, the decision threshold is defined as follows:

## Table 1

Confusion matrix. Each entry represents the number of observations in the respective category on a given test set.

<table><tr><td></td><td>Predicted 1</td><td>Predicted 0</td></tr><tr><td>True 1</td><td>True Positive (TP)</td><td>False Negative (FN)</td></tr><tr><td>True 0</td><td>False Positive (FP)</td><td>True Negative (TN)</td></tr></table>

$\begin{array} { r } { T _ { c s } = \frac { C _ { F P } - C _ { T N } } { C _ { F P } - C _ { T N } + C _ { F N } - C _ { T P } } , } \end{array}$ where cs stands for cost-sensitive and the threshold can be either class- or record-dependent. This expression can be simplified to $\begin{array} { r } { T _ { c s } = \frac { C _ { F P } ^ { ' } } { C _ { F P } ^ { ' } + C _ { F N } ^ { ' } } } \end{array}$ if we transform the cost matrix into $\left( \begin{array} { c c } { { C _ { _ { T P } } ^ { ^ { \prime } } = 0 } } & { { C _ { _ { F N } } ^ { ^ { \prime } } = C _ { _ { F N } } - C _ { _ { T P } } } } \\ { { C _ { _ { F P } } ^ { ^ { \prime } } = C _ { _ { F P } } - C _ { _ { T N } } } } & { { C _ { _ { T N } } ^ { ^ { \prime } } = 0 } } \end{array} \right) .$

Another way to make any classifier cost-sensitive is to use an approach called thresholding [30], which performs a search across all scores produced by a given classifier. The score giving the lowest costloss is chosen as the decision threshold. In a situation where costs are unknown, thresholding can be optimised using a suitable loss-metric instead to improve classification performance on imbalanced datasets [31].

## 2.2. Classifier performance evaluation under cost asymmetry

The goal of cost-sensitive learning is to construct a classifier that is aware of the differences in importance between the classes. The advantage of using a cost-matrix is the exact specification of the loss function for any given data input. This, of course, calls for a suitable performance metric. In the cost-sensitive literature classifier perfor mance is typically measured in terms of the total expected misclassifi cation cost $[ 2 7 , 3 2 ]$ which is simply the total cost-weighted classification error. Let $S _ { F P }$ be the set of false positives produced by a given classifier on a given test set, and let $\mathit { S } _ { \mathit { F N } }$ be the set of false nega tives. The total misclassification cost of a given classifier is $\begin{array} { r } { T C = \sum { i \in S _ { F P } C _ { F P } ^ { i } } + \sum { i \in S _ { F N } C _ { F N } ^ { i } } } \end{array}$ . However, how must one evaluate a classi fier when the costs are unknown at the time of estimation? Here we again refer to the importance of the knowledge of the application domain, which can determine whether or not performance on one of the two classes should be favoured. In the domain where both types of misclassification costs are non-negligible, it is preferable to use a metric that incorporates performance with regard to both classes, rather than one that only favours the positive class. Many metrics exist that assess classifier performance [33,34], with most derived from the confusion matrix (see Table 1)

An empirical study of the stability of several such performance metrics under various degrees of class skew concludes that the two metrics that remain unbiased in the presence of class skew are the true positive rate $\begin{array} { r } { T P R = { \frac { T P } { P } } } \end{array}$ and the true negative rate $\begin{array} { r } { T N R \ = \ \frac { T N } { N } } \end{array}$ . Their arithmetic average $\frac { T P R + T N R } { 2 }$ shares these desirable properties [35]. This metric places equal emphasis on each misclassification error type, which, in the absence of information regarding the importance of each of the two classes, is a reasonable choice. It is known under several names in the literature, such as balanced accuracy (BACC) $[ 3 6 , 3 7 ] ,$ bookmaker informedness [35] or weighted accuracy [33] and happens to correspond to a point on the receiver operating characteristic curve (ROC) at a given decision threshold [33,35,37]. In this paper, we also consider the cost-effectiveness of the best models selected using BACC in case the costs were known.

## 3. A cost matrix for employee absenteeism and well-being interventions

In this section we present our conceptualisation of a cost matrix of the direct costs of employee sickness absence in relation to a well-being intervention. We consider this as one of the main contributions of this paper.

In any period $M ,$ an employee is contractually obligated to supply t hours of work in return for remuneration $W ,$ yielding the base hourly rate ${ \frac { W } { t _ { M } } } { 0 . 6 }$ the employee for this period. If in this period the employee is absent due to sickness for a total duration of $t _ { s } \in [ 0 , t _ { M } ]$ hours, the number of worked hours is reduced to $t _ { M } - t _ { s }$ , which are remunerated as usual according to the base rate. However, depending on the legislation of the country of employment, the employer may also be required to remunerate the $t _ { s }$ hours of sickness according to a proportion $r \in [ 0 , 1 ]$ ] of the employee’s base rate<sup>1</sup>. The hourly rate is in this case equal to $\begin{array} { r l } { \frac { \left( t _ { M } - t _ { s } \right) \frac { W } { t _ { M } } + t _ { s } r \frac { W } { t _ { M } } } { t _ { M } - t _ { s } } = } & { { } \left( 1 + \frac { t _ { s } r } { t _ { M } - t _ { s } } \right) \frac { W } { t _ { M } } } \end{array}$ , which is higher than the base rate, reflecting the loss of productivity associated with the employee’s absence.

Suppose now that the employer decides to put the employee through a well-being intervention in an attempt to prevent potential sickness absence. The price of such an intervention per participant is $C ,$ which burdens the employer. In addition, if the intervention requires atten dance (such as a coaching seminar) of duration $t _ { i } ,$ the number of hours worked by the employee is reduced by as much. Therefore, the hourly rate of an employee who was not going to be absent but is put through an intervention is $\frac { W + C } { t _ { M } - t _ { i } }$ , which is also higher than the base rate. If, however, the employee was going to be absent, in addition we expect that the intervention would have a positive effect and result in the reduction of the absence period by $\widetilde t _ { s } \in [ 0 , t _ { s } ]$ hours<sup>2</sup>. The resulting hourly rate is then equal to

$$
\frac {\left(t _ {M} - t _ {s} + \widetilde {t} _ {s}\right) \frac {W}{t _ {M}} + \left(t _ {s} - \widetilde {t} _ {s}\right) r \frac {W}{t _ {M}} + C}{t _ {M} - t _ {s} - t _ {i} + \widetilde {t} _ {s}} = \frac {W + C}{t _ {M} - t _ {s} - t _ {i} + \widetilde {t} _ {s}} - \frac {\left(t _ {s} - \widetilde {t} _ {s}\right) (1 - r)}{t _ {M} - t _ {s} - t _ {i} + \widetilde {t} _ {s}} \frac {W}{t _ {M}}
$$

. Table 2 summarises these hourly rates. Here, just like in the confusion matrix in Table 1, the rows correspond to the true outcomes, and col umns correspond to predicted outcomes. Thus, true positives are ab sentees targeted with an intervention, false positives are non-absentees targeted with an intervention, true negatives are non-absentees not targeted, and finally, absentees not targeted are false negatives.

Remark 1. Clearly, a necessary condition for the intervention to be cost-effective for the employer is that $t _ { i } < \widetilde t _ { s }$

Remark 2. A limiting factor in specifying a concrete cost matrix is the parameter $\widetilde { t } _ { s }$ , which is a priori unknown and no indication of example values can be found in the literature.

## 3.1. The case of Belgium

As we mentioned in the introduction, this work initiated at the request of a Belgian HR and Well-Being Specialist. We therefore adapt Table 2 to the specifics of Belgian legislation.

In Belgium, throughout all sickness absences lasting up to 30 cal endar days, white-collar workers receive full wage equivalent sickness benefits from the employer. As soon as the duration of absence is longer than one calendar month, the benefits are paid by the social security instead. Blue-collar workers receive reduced compensation starting from week two of absence: the employer continues to cover some fraction r of the full wage $W ,$ while the remainder is covered by social security [38].

Our sample contains only white-collar employees. By consequence, the parameter $r = 1$ and $t _ { s }$ is defined as the total hours of sickness ab sences covered by the employer in any given month $M ,$ with the necessary condition that $t _ { s } < t _ { M }$

Using the hourly rates from Table $^ { 2 , }$ and after applying the trans formation as mentioned in Section 2.1, such that the cost of correctly classifying observations is zero, we obtain the following costs:

## Table 2

The cost matrix of employee sickness absence in terms of hourly rates of employee remuneration, when considering well-being intervention. W repre sents the employee’s salary, $t _ { M }$ the expected work hours, $t _ { s }$ is the absence duration in hours, r is the fraction of the base rate $\frac { W } { t _ { M } }$ to which hours of absence are remunerated as guaranteed by law in the form of statutory sick pay $\widetilde { t } _ { s }$ is the reduction in hours of sickness absence because of the intervention, C is the cost of the intervention, and t is the duration of attendance in hours associated with the intervention.

<table><tr><td></td><td>Intervention</td><td>No Intervention</td></tr><tr><td rowspan="2">Absentee</td><td></td><td rowspan="2"> $C_{FN} = \left(1 + \frac{t_s r}{t_M - t_s}\right) \frac{W}{t_M}$ </td></tr><tr><td> $C_{TP} = \frac{W + C}{t_M - t_s - t_i + \tilde{t}_s} - \frac{\left(t_s - \tilde{t}_s\right)(1 - r)}{t_M - t_s - t_i + \tilde{t}_s} \frac{W}{t_M}$ </td></tr><tr><td>Non- Absentee</td><td> $C_{FP} = \frac{W + C}{t_M - t_i}$ </td><td> $C_{TN} = \frac{W}{t_M}$ </td></tr></table>

$$
\left( \begin{array}{c c} C _ {T P} ^ {\prime} = 0 & C _ {F N} ^ {\prime} = \frac {W}{t _ {M} - t _ {s}} - \frac {W + C}{t _ {M} - t _ {s} + \widetilde {t} _ {s} - t _ {i}} \\ C _ {F P} ^ {\prime} = \frac {W + C}{t _ {M} - t _ {i}} - \frac {W}{t _ {M}} & C _ {T N} ^ {\prime} = 0 \end{array} \right)\tag{1}
$$

To simplify notation we omit the superscripts i that indicate that costs are record-dependent.

Remark 3. Note that while $C _ { F P } ^ { \prime }$ is always positive, $C ^ { \prime } { } _ { F N }$ may become negative when $t _ { i } > t _ { s } \geq \widetilde t _ { s }$ . This violates the so called reasonableness condition defined by Elkan [27], which states that the cost of correct predictions should always be less than the cost of misclassifying, otherwise it is more profitable to misclassify than to classify correctly. A negative misclassification cost is a benefit for the employer, meaning that it is more cost-effective not to apply an intervention to that indi vidual (e.g. due to low expected sickness absence hours).

## 4. Experimental framework

In this section we present the experimental procedure that was used to conduct our analysis. Our experiments consist of two parts: in the first instance we predict employee sickness absence using cost-sensitive learning and the cost matrix defined in Eq. (1), we evaluate model performance using custom cost-based metrics. Then, in view of lack of data regarding the $\widetilde { t } _ { s }$ parameter, we additionally predict using costinsensitive models, which we evaluate using the balanced accuracy score. In both cases, we also report standard metrics such as the AUC, FPR, FNR.

## 4.1. Data

Our data contains HR and payroll records from roughly 280 small, medium and large Belgian firms from a variety of industry sectors. The data spans the period between January 2018 and March 2019. We adopt the prospective study design so commonly found in absenteeism pre diction literature, where attributes from period $M _ { t }$ are used to predict the outcome in period $M _ { t + 1 }$ <sub>1</sub>.

## 4.1.1. Target variable

In any given month, each employee’s hours of certified sickness cording to a threshold $T _ { h r s }$ : observations having a total number of hours recorded below $T _ { h r s }$ are coded as $^ { 0 , }$ and the rest as 1. The choice of $T _ { h r s }$ should of course depend on the task at hand. In our case, after consulting the data provider, we decided to set $T _ { h r s } = 0$ . The resulting distribution of our target variable is highly imbalanced, ranging between 7.5% and 16.5% of positives in any given period. Table 3 shows the class imbal ance in our data per prediction period.

## 4.1.2. Predictors

One of the novelties of our work is to exploit the rich absence pattern data at our disposal. The main difficulty we are faced with is the absence of any health-related predictors in our dataset or the reason for absence. Our dataset consists of 66 features.

Demographic features: Employee’s demographic features, such as age, gender, marital status, education etc.

Work environment features: Features that describe various aspects of the work circumstances of employees (wage, contract type, etc.). We also include fatigue inducing factors such as work shift irregularities (e. g. weekend work, overtime, night shifts) as well as patterns of holiday applications (e.g. holiday frequency and duration, number of rejected holiday applications, time since last holiday of a certain duration).

Historic absence patterns: measures of recency (time since last absence) and frequency of illnesses, average hours of sickness absences in the 12 months prior to the prediction period and since the start of employment contract.

## 4.1.3. Data preparation

In continuous numeric variables all values exceeding plausible minima and maxima are removed (e.g. age values below 18 and above 100) and missing values are imputed with sample median. All levels in categorical predictors are transformed to binary variables, including the missing values. In recency variables missing values are replaced with 366 indicating that the last incident was registered more than one cal endar year ago.

## 4.2. Methods

## 4.2.1. Classification algorithms

We adopt a wide range of decision tree ensembles in our framework and combine them with state-of-the-art solutions to the problem of class imbalance. Since a requirement for our decision support system was that it could be readily implemented in the cloud, we apply methods with existing open-source implementations.

The base algorithm adopted in our experiments is a decision tree classifier (specifically CART [39]). Decision trees have been shown to have a number of highly desirable properties: they can handle mixed data types and missing values; they are insensitive to monotone trans formations of the feature space and do not require normalisation of predictors; they can handle irrelevant predictors and are robust to

## Table 3

The class imbalance in our data per prediction period (year/month).

<table><tr><td rowspan="2"></td><td>Attributes period</td><td>Target period</td><td rowspan="2"># employee&#x27;s (from # firms)</td><td rowspan="2"># positives (%)</td></tr><tr><td>period</td><td>period</td></tr><tr><td>1</td><td>2018/01</td><td>2018/02</td><td>50,729 (284)</td><td>8193 (16.15)</td></tr><tr><td>2</td><td>2018/02</td><td>2018/03</td><td>49,459 (281)</td><td>8161 (16.50)</td></tr><tr><td>3</td><td>2018/03</td><td>2018/04</td><td>48,202 (280)</td><td>4268 (8.85)</td></tr><tr><td>4</td><td>2018/04</td><td>2018/05</td><td>51,998 (280)</td><td>4682 (9.00)</td></tr><tr><td>5</td><td>2018/05</td><td>2018/06</td><td>51,483 (280)</td><td>5123 (9.95)</td></tr><tr><td>6</td><td>2018/06</td><td>2018/07</td><td>50,843 (281)</td><td>3845 (7.56)</td></tr><tr><td>7</td><td>2018/07</td><td>2018/08</td><td>51,372 (282)</td><td>3863 (7.52)</td></tr><tr><td>8</td><td>2018/08</td><td>2018/09</td><td>51,738 (282)</td><td>5201 (10.05)</td></tr><tr><td>9</td><td>2018/09</td><td>2018/10</td><td>51,130 (282)</td><td>6340 (12.40)</td></tr><tr><td>10</td><td>2018/10</td><td>2018/11</td><td>50,744 (281)</td><td>5905 (11.64)</td></tr><tr><td>11</td><td>2018/11</td><td>2018/12</td><td>49,659 (268)</td><td>4986 (10.04)</td></tr><tr><td>12</td><td>2018/12</td><td>2019/01</td><td>47,128 (268)</td><td>6256 (13.27)</td></tr><tr><td>13</td><td>2019/01</td><td>2019/02</td><td>52,637 (268)</td><td>8432 (16.02)</td></tr><tr><td>14</td><td>2019/02</td><td>2019/03</td><td>51,751 (268)</td><td>6493 (12.55)</td></tr></table>

outliers [40]. These properties combined with model interpretability make decision trees highly suitable for business applications. While a single decision tree may not show the highest performance because of high variance, combining a collection of trees into an ensemble de creases variance and improves performance, though at the expense of reduced interpretability [41].

All of the algorithms applied in our experiments are cost-insensitive by default, but can be made cost-sensitive in the presence of explicitly defined costs. In this work we limit ourselves to pre-training and posttraining cost-sensitive learning methods as categorised in [42]. We describe these methods below and Table 4 provides a summary.

4.2.1.1. Class imbalance correction. Each of the cost-insensitive decision tree ensembles can be combined with a sampling method in order to compensate for unequal class distribution of the training data. This can be achieved by modifying the training set using cost-sensitive sampling and passing it to a classifier of choice (also referred to as CS-pre SampleEnsemble). Alternatively resampling can be performed at the level of the ensemble (also referred to as CS-SampleEnsemble), where both classes are sampled in appropriate proportions prior to training each of the base classifiers in the ensemble.

We performed cost-sensitive data sampling using average training misclassification costs, defined as follows: $\begin{array} { r } { \overline { { C } } _ { F P } = \frac { 1 } { N } \sum _ { i \in S _ { N } } C _ { F P } ^ { i } , \overline { { C } } _ { F N } = } \end{array}$ $\textstyle { \frac { 1 } { P } } \sum _ { i \in S _ { P } } C _ { F N } ^ { i }$ . Here $s _ { N }$ is the set of negatives (of size N) and $S _ { P }$ is the set of positives (of size $P ) .$ . The cost ratio $\frac { \overline { { C } } _ { F N } } { \overline { { C } } _ { F P } }$ is used to scale the number of positives for over-sampling and $\frac { \overline { { C } } _ { E P } } { \overline { { C } } _ { F N } }$ is used to scale the number of neg atives for under-sampling [42].

When costs are unknown, it is reasonable to assume that the optimal class distribution is uniform and the classes are sampled in equal

Table 4  
Overview of the methods used in our analysis.

<table><tr><td>Our notation</td><td>Method</td><td>Parameter settings</td></tr><tr><td rowspan="2">dt</td><td>AlgorithmsDecision Tree (CART [39])</td><td></td></tr><tr><td>Ensembles</td><td></td></tr><tr><td>bag</td><td>Bagging [43]</td><td>#trees = 100</td></tr><tr><td>rdf</td><td>Random Decision Forest [44]</td><td>#trees = 100</td></tr><tr><td>rf</td><td>Random Forest [45]</td><td>#trees = 100</td></tr><tr><td>xrf</td><td>Extremely Randomized Trees [46]</td><td>#trees = 100</td></tr><tr><td>adab1</td><td>AdaBoost [47]</td><td>#nodes = 1,#trees = 50</td></tr><tr><td>adab2</td><td></td><td>#nodes = 2,#trees = 50</td></tr><tr><td colspan="3">CS-WeightedEnsemble</td></tr><tr><td>wrf</td><td>Weighted Random Forest [48]</td><td>#trees = 100</td></tr><tr><td colspan="3">CS-SampleEnsemble</td></tr><tr><td>bal_rf</td><td>Balanced Random Forest [48]</td><td>#trees = 100</td></tr><tr><td>bal_rdf</td><td>Balanced Random Decision Forest</td><td>#trees = 100</td></tr><tr><td>easy_ensmb</td><td>Easy Ensemble [49]</td><td>#estimators = 50</td></tr><tr><td colspan="3">CS-SampleBoost Methods</td></tr><tr><td>rusboost</td><td>RUSBoost [50]</td><td>#trees = 50</td></tr><tr><td colspan="3">Sampling Methods</td></tr><tr><td>ros</td><td>Random Oversampling</td><td></td></tr><tr><td>rus</td><td>Random Undersampling</td><td></td></tr><tr><td>smote</td><td>SMOTE [51]</td><td>k = 5</td></tr><tr><td colspan="3">Calibration</td></tr><tr><td>isotonic</td><td>Isotonic Regression [52]</td><td></td></tr><tr><td>sigmoid</td><td>Platt [53]</td><td></td></tr><tr><td colspan="3">Post-training methods</td></tr><tr><td> $T = T_{best}$ </td><td>Thresholding [30]</td><td></td></tr><tr><td> $T = T_{cs}^{t}$ </td><td>DMECC [29]</td><td></td></tr></table>

proportions [27].

4.2.1.2. Calibration. As was observed in [29,54], decision tree methods do not produce reliable posterior class membership probability esti mates. This has negative implications for application of post-training methods such as described above, where class membership probabili ties are used for decision-making [52]. In this work, we optionally apply two probability calibration methods to each of the classifiers in our framework: isotonic regression [52] and Platt scaling [53].

4.2.1.3. Post-training methods. When costs are record-dependent and are known at the time of estimation DMECC can be applied to derive the total misclassification cost on a given test set. If costs are unknown, thresholding can be applied to optimise over an error-based loss, which assumes that costs are class-dependent.

All of our experiments consider the default threshold T = 0.5 along with the post-training methods that are simple to implement in practice.

Cost-sensitive models are evaluated at the decision threshold ob tained using the DMECC approach (explained in Section 2.1). For the application of DMECC, both types of misclassification costs from Eq. (1) need to be specified to calculate record-dependent decision thresholds $T _ { c s } ^ { i }$ . Since $t _ { s }$ is unknown at the time of prediction, we estimate this in two ways. First, we set the $t _ { s }$ equal to each record’s individual average sickness duration in 12 months prior to prediction (denoting the resulting model $T _ { c s } ^ { i } - m e a n )$ . Second, we predict $t _ { s }$ using a Random Forest regressor trained on positive records from the same training set that the cost-sensitive classifier is trained on (denoted $T _ { c s } ^ { i } - p o s t r e g ) .$ Cost-insensitive models classify at the optimal decision threshold $T = T _ { b e s t }$ obtained using thresholding (see Section 2).

All of the above experiments were run on the same 13 pairs of training and test data periods. In our experiments we use the combi nation of twelve algorithms, four pre-training options (including no pretraining), three calibration options (including no calibration), which gives us 120 base models to which post-training was optionally applied. Cost-insensitive models were evaluated at two decision thresholds, resulting in 240 models per period. From 120 base models 111 could be made cost-sensitive, each of which were evaluated at three decision thresholds (explained in 4.2.1), resulting in 333 models per period and per combination of $C$ and $t _ { i } ,$ and $\widetilde { t } _ { s }$ (described in 4.4.2). CS-SampleEnsemble and CS-SampleBoost methods, naturally, are only combined with calibration. We note that using the name Balanced Random Forest in both cost-sensitive and cost-insensitive models we abuse the terminology slightly, as in fact cost-sensitive models perform sampling according to the cost matrix.

## 4.3. Software used

All experiments were conducted using Python (version 3.6.6), the majority of implementations come from scikit-learn (version 0.20.2) li brary [55], implementations of all pre-training methods come from imbalanced-learn library [56], post-training methods are our own implementations; the results were processed using Python and csvkit [57].

## 4.4. Experimental set up

## 4.4.1. Data partition

Three datasets, that contain the same set of employees, served as input to the experimental framework. We randomly split the set of employees into three disjoint sets. The first contains 60% of all obser vations and was used for training. The second contains 20% of the total, used for optimal threshold search respectively, where features were from period $M _ { t }$ and labels were from $M _ { t + 1 }$ . The remaining 20% of em ployees were used for testing with features from $M _ { t + 1 }$ and labels from $M _ { t + 2 } .$ This process was repeated 50 times using different random seeds to generate data splits and the results were averaged across iterations.

## 4.4.2. Training costs

The definition of the cost parameters are as introduced in Section 3. The values for $W , t _ { M }$ and $t _ { s }$ are readily available from our data. In the absence of information regarding the effectiveness of chosen in terventions in reduction of sickness absence, we assume some arbitrary values for the parameter $\widetilde { t } _ { s }$ . We consider three alternatives for this parameter: a) $\widetilde { t } _ { s } = t _ { s } ~ , \mathrm { b } ) \widetilde { t } _ { s } = 0 . 5 { \cdot } t _ { s }$ , and $\mathrm { c } ) \ : \widetilde { t } _ { s } ^ { i } = p ^ { i } \cdot t _ { s } ^ { i }$ where $p ^ { i } \in [ 0 , 1 ]$ is an individual percentage of reduction in sickness hours, randomly drawn from a uniform distribution. This parameter was drawn once and was reused across all intervention scenarios. We expect that alternative c) reflects the reality best, but further experiments are needed (see Section 6.1).

We consider three examples of interventions with corresponding price C and duration t :

Case 1. “Fit Check-Up”. Aimed at increasing physical activity levels of employees. A professional coach examines one’s fitness level using specialised equipment and designs a personalised 12-week fitness pro gramme. The parameter settings are as follows: C = 100(EUR), t = 4 (hours).

Case 2. A sleep and fitness tracking device. Aimed at promoting healthy lifestyle choices. The built-in software informs on sleep and activity patterns and encourages participants towards positive change in behaviour. The parameter settings are as follows: C = 30(EUR), t = 0 (hours).

Case 3. Psychotherapy. The employer offers financial support for in dividual psychotherapy sessions to help reduce stress and prevent burn out. The parameter settings are as follows: $C = 6 0 ( \mathrm { E U R } ) , t _ { i } = 1 ( \mathrm { h o u r } )$

## 4.4.3. Evaluation

Cost-sensitive model performance is typically assessed using the model’s total misclassification cost (TC), which sums record-dependent costs on a given test set. In the absence of a decision support system, the employer has two naive solutions, namely not applying any interven tion, and applying the intervention indiscriminately to all employees, with respective costs $T C _ { n o n e }$ and $T C _ { a l l } .$ Any intervention target group proposed by a predictive model (henceforth referred to as the campaign) is worthwhile only if it improves on either of these naive costs, some thing we are trying to capture via the Cost Improvement Score: $C I S = 1 ~ { - }$ $\frac { T C } { m i n ( T C _ { n o n e } , T C _ { a l l } ) }$ , with the following interpretation. $C I S < 0$ indicates that the model’s intervention campaign is more costly than either of the naive approaches. A perfect model that correctly classifies everyone achieves CIS = 1. To evaluate whether or not the size of the model’s intervention campaign prescribed by the model is cost-effective, as well as to compare models with similar cost performance, we use Return On Investment (ROI). In the context of absence prediction, ROI is defined as the intervention profit (benefits minus costs) over intervention costs:

$$
R O I = \sum_ {j \in S _ {P P}} \frac {\widetilde {t} _ {s} ^ {j} \frac {W ^ {j}}{t _ {M} ^ {j}}}{C + t _ {i} \frac {W ^ {j}}{t _ {M} ^ {j}}} - 1
$$

, where $S _ { P P }$ is the set of positives predicted by the model and the index j refers to the fact that both the costs and the profits are recorddependent. $R O I < 0$ indicates that the model’s intervention campaign prescribed by the model is not cost-effective. Both CIS and ROI should be considered in the final model selection. For example, when one model has $C I S = 0 . 7$ and ROI is some positive value A, and another model has CIS = 0.68 with ROI $B > A ,$ , then the second model might be preferred as it requires less budget to be available for similar cost performance.

## 5. Results and discussion

The primary interest of our work lies in applying cost-sensitive learning to the problem of absenteeism prediction on real data, using our newly designed cost matrix. We evaluate model performance per period, based on the two cost metrics: CIS and ROI (defined in Section $4 . 4 . 3 )$ . Related to this are two further questions: first, whether the usage of record-dependent costs offers any advantage over class-dependent costs, and second, whether predicting the value of $t _ { s }$ using a regressor offers any advantage over using mean historic sickness per individual. We also discuss which of the interventions considered offers the lowest misclassification cost. With the given current difficulty in obtaining all the necessary parameters of the cost matrix, we also try to see whether selecting models using a cost-insensitive metric would be a good alter native to cost-sensitive learning.

Analysing the performance of specific algorithms lies outside the scope of this paper.

## 5.1. Cost-sensitive absenteeism prediction

The first part of our experiments provides an illustration of how our proposed misclassification cost matrix of employee absenteeism (defined in Eq. (1)) performs on real world data.

## 5.1.1. Model performance and cost-effectiveness

Our results show that in every prediction period and intervention combination, we find cost-sensitive models with $C I S > 0 ;$ , and with $R O I > 0$

Fig. 1 demonstrates cost performance of the top-ranking models (when ranked by CIS). We note that the largest cost improvement (the difference between the benchmark and the total cost) of the model was achieved under Case 1 and Case 3, while Case 2 - the least expensive intervention - shows only marginal improvement. We also found that DMECC models that use regression predictions to classify, achieved higher cost improvement much more frequently than models that use average hours.

5.1.1.1. Record-versus class-based costs. As was mentioned in Remark 3, in our cost matrix, the reasonableness condition only holds for those individuals $j ,$ whose $\widetilde { t } _ { s } ^ { j } > t _ { i }$ , i.e. when the expected reduction in hours of absence due to the intervention exceeds the duration of the inter vention. The DMECC approach can directly account for this condition, which allow us to avoid targeting individuals for whom an intervention does not pay off. Models that use a constant threshold for classification decision, do not make such a distinction, and are less frequently ranked among the top models.

Another drawback of using class-based costs became apparent when we applied sampling methods in combination with averaged recorddependent costs (explained in Section 4.2.1). We observed that under certain operating conditions, for a number of employees in our sample holds that $C _ { F P } ^ { i } > C _ { F N } ^ { i }$ , and when the proportion of such individuals in the training sample was large enough, this resulted in: $\overline { { C } } _ { F P } > \overline { { C } } _ { F N }$ Under such cost imbalance, an oversampler will oversample the more costly class i.e. the negatives and an undersampler will undersample the less costly class i.e. the positives, which would increase class imbalance, instead of correcting it. Such models failed in the pre-training phase and were not considered in the rankings.

## 5.1.2. Cost-effectiveness of interventions

Another question a practitioner might be interested in is: which intervention offers the highest savings in any given period? To deter mine this, we shortlist the intervention that yield the highest CIS on any given prediction period and $\widetilde { t } _ { s }$ combination. These results are presented in Table 5. We note that the highest CIS is not necessarily associated with a positive ROI, and therefore we restrict ourselves to models that have

Decision Support Systems xxx (xxxx) xxx

Table 5  
![](/api/attachments/7WPU8EUY/fulltext/images/8f8b71a8b44d1ab051647912444ff2b8708d9b390de3c7f31c4a9588525c429a.jpg)  
Fig. 1. Cost performance of the cost-sensitive models across all prediction periods and interventions. The bars represent the total misclassification cost of the top ranking model (ranked by CIS). The solid line shows the cost of the benchmark under the same operating conditions. Here “t\_s\_tilde” is $\widetilde { t } _ { s } / t _ { s }$ and “random” refers to record-dependent $p _ { i } \in [ 0 , 1 ]$

Selecting the most cost-effective intervention. For the final decision of which of the interventions offers the highest cost improvement in any given prediction period, we have selected models with the highest CIS and positive ROI. The column titled “% pos with $C _ { F N } { < } 0 ^ { * }$ shows the percentage of individuals in the test set whose misclassification costs violate the reasonableness conditions (see Remark 3). Rand refers to record-dependent $p _ { i } \in$ [0,1].

<table><tr><td rowspan="2">Target period</td><td colspan="2">Intervention</td><td>Method</td><td rowspan="2">%pos</td><td rowspan="2">%pos with  ${C}_{FN}^{\prime } < 0$ </td><td colspan="2">Error-rates</td><td colspan="4">Cost-based metrics</td></tr><tr><td> ${\widetilde{t}}_{s}/{t}_{s}$ </td><td>Case</td><td>algo_sampling_calib-T</td><td>FNR</td><td>FPR</td><td>CIS</td><td>TC</td><td>Benchmark</td><td>ROI</td></tr><tr><td>2018/03</td><td>1</td><td>1</td><td>xrf_rus_sigmoid- ${T}_{cs}^{i}$ -postreg</td><td>15.62</td><td>7.94</td><td>0.34</td><td>0.46</td><td>0.21</td><td>12,756.80</td><td>16,164.63</td><td>0.21</td></tr><tr><td>2018/03</td><td>0.5</td><td>1</td><td>easy_ensmb_none_none- $T = 0.5$ </td><td>15.62</td><td>26.59</td><td>0.59</td><td>0.19</td><td>0.18</td><td>9545.19</td><td>11,695.74</td><td>0.41</td></tr><tr><td>2018/03</td><td>rand</td><td>1</td><td>dt_ros-isotonic- ${T}_{cs}^{i}$ -postreg</td><td>15.62</td><td>40.61</td><td>0.81</td><td>0.13</td><td>0.98</td><td>384.20</td><td>16,164.63</td><td>1.01</td></tr><tr><td>2018/04</td><td>1</td><td>1</td><td>adab1_smote_sigmoid- ${T}_{cs}^{i}$ -postreg</td><td>8.09</td><td>12.43</td><td>0.54</td><td>0.27</td><td>0.32</td><td>8733.03</td><td>12,789.16</td><td>0.07</td></tr><tr><td>2018/04</td><td>0.5</td><td>1</td><td>xrf_ros-isotonic- ${T}_{cs}^{i}$ -postreg</td><td>8.09</td><td>33.34</td><td>0.84</td><td>0.09</td><td>0.26</td><td>6777.96</td><td>9218.97</td><td>0.48</td></tr><tr><td>2018/04</td><td>rand</td><td>1</td><td>wxrf_ros_sigmoid- ${T}_{cs}^{i}$ -mean</td><td>8.09</td><td>43.55</td><td>0.98</td><td>0.01</td><td>0.55</td><td>3735.29</td><td>8297.38</td><td>13.81</td></tr><tr><td>2018/05</td><td>1</td><td>1</td><td>adab2_rus-isotonic- ${T}_{cs}^{i}$ -postreg</td><td>8.01</td><td>12.51</td><td>0.82</td><td>0.07</td><td>0.26</td><td>9765.23</td><td>13,119.91</td><td>2.39</td></tr><tr><td>2018/05</td><td>0.5</td><td>1</td><td>rusboost_none_none- ${T}_{cs}^{i}$ -mean</td><td>8.01</td><td>36.65</td><td>0.96</td><td>0.02</td><td>0.24</td><td>7596.42</td><td>9939.64</td><td>3.77</td></tr><tr><td>2018/05</td><td>rand</td><td>1</td><td>bal_rf_none_sigmoid- ${T}_{cs}^{i}$ -postreg</td><td>8.01</td><td>48.01</td><td>0.91</td><td>0.02</td><td>0.30</td><td>6588.44</td><td>9386.79</td><td>3.49</td></tr><tr><td>2018/06</td><td>1</td><td>1</td><td>adab2_ros_sigmoid- ${T}_{cs}^{i}$ -postreg</td><td>9.05</td><td>13.88</td><td>0.80</td><td>0.06</td><td>0.23</td><td>13,708.92</td><td>17,892.66</td><td>3.52</td></tr><tr><td>2018/06</td><td>0.5</td><td>1</td><td>adab2_none_sigmoid- ${T}_{cs}^{i}$ -postreg</td><td>9.05</td><td>37.53</td><td>0.91</td><td>0.01</td><td>0.17</td><td>11,569.85</td><td>13,893.63</td><td>6.73</td></tr><tr><td>2018/06</td><td>rand</td><td>1</td><td>adab1_none-isotonic- ${T}_{cs}^{i}$ -postreg</td><td>9.05</td><td>47.53</td><td>0.92</td><td>0.02</td><td>0.67</td><td>4281.80</td><td>13,173.46</td><td>6.24</td></tr><tr><td>2018/07</td><td>1</td><td>1</td><td>adab2_rus-isotonic- ${T}_{cs}^{i}$ -mean</td><td>6.87</td><td>13.34</td><td>0.89</td><td>0.03</td><td>0.20</td><td>7750.51</td><td>9747.05</td><td>5.96</td></tr><tr><td>2018/07</td><td>0.5</td><td>1</td><td>rf_ros_none- ${T}_{cs}^{i}$ -mean</td><td>6.87</td><td>35.85</td><td>0.95</td><td>0.01</td><td>0.18</td><td>5556.31</td><td>9747.05</td><td>13.39</td></tr><tr><td>2018/07</td><td>rand</td><td>3</td><td>xrf_smote-isotonic- ${T}_{cs}^{i}$ -postreg</td><td>6.87</td><td>20.19</td><td>0.59</td><td>0.27</td><td>0.78</td><td>1481.94</td><td>6828.25</td><td>0.11</td></tr><tr><td>2018/08</td><td>1</td><td>1</td><td>xrf_none_none- ${T}_{cs}^{i}$ -postreg</td><td>6.72</td><td>14.15</td><td>0.79</td><td>0.07</td><td>0.15</td><td>9918.14</td><td>11,708.51</td><td>1.90</td></tr><tr><td>2018/08</td><td>0.5</td><td>1</td><td>wrf_none_sigmoid- ${T}_{cs}^{i}$ -postreg</td><td>6.72</td><td>37.27</td><td>0.94</td><td>0.01</td><td>0.16</td><td>7306.00</td><td>8700.07</td><td>11.39</td></tr><tr><td>2018/08</td><td>rand</td><td>1</td><td>bal_rf_none-isotonic- ${T}_{cs}^{i}$ -postreg</td><td>6.72</td><td>47.90</td><td>0.87</td><td>0.02</td><td>0.23</td><td>6174.96</td><td>8053.30</td><td>3.75</td></tr><tr><td>2018/09</td><td>1</td><td>1</td><td>easy_ensmb_none_none- $T = 0.5$ </td><td>9.28</td><td>11.76</td><td>0.50</td><td>0.24</td><td>0.36</td><td>11,172.95</td><td>17,555.27</td><td>0.45</td></tr><tr><td>2018/09</td><td>0.5</td><td>1</td><td>bal_rf_none-isotonic- $T = 0.5$ </td><td>9.28</td><td>33.78</td><td>0.83</td><td>0.05</td><td>0.48</td><td>9062.25</td><td>17,555.27</td><td>2.36</td></tr><tr><td>2018/09</td><td>rand</td><td>1</td><td>bal_rf_none-isotonic- ${T}_{cs}^{i}$ -postreg</td><td>9.28</td><td>45.52</td><td>0.86</td><td>0.04</td><td>0.57</td><td>7594.42</td><td>17,555.27</td><td>2.54</td></tr><tr><td>2018/10</td><td>1</td><td>1</td><td>adab1_rus_sigmoid- ${T}_{cs}^{i}$ -postreg</td><td>11.57</td><td>11.27</td><td>0.45</td><td>0.33</td><td>0.26</td><td>12,463.05</td><td>16,772.53</td><td>0.21</td></tr><tr><td>2018/10</td><td>0.5</td><td>1</td><td>wrf_none_none- ${T}_{cs}^{i}$ -postreg</td><td>11.57</td><td>32.20</td><td>0.92</td><td>0.04</td><td>0.15</td><td>9743.45</td><td>11,519.75</td><td>3.46</td></tr><tr><td>2018/10</td><td>rand</td><td>1</td><td>rdf_smote_sigmoid- ${T}_{cs}^{i}$ -postreg</td><td>11.57</td><td>44.39</td><td>0.91</td><td>0.04</td><td>0.71</td><td>2729.36</td><td>9273.33</td><td>4.47</td></tr><tr><td>2018/11</td><td>1</td><td>1</td><td>xrf_smote_none- ${T}_{cs}^{i}$ -postreg</td><td>10.86</td><td>10.97</td><td>0.65</td><td>0.20</td><td>0.16</td><td>12,671.80</td><td>15,114.80</td><td>0.78</td></tr><tr><td>2018/11</td><td>0.5</td><td>1</td><td>easy_ensmb_none_none- ${T}_{cs}^{i}$ -mean</td><td>10.86</td><td>32.09</td><td>0.95</td><td>0.03</td><td>0.17</td><td>8649.31</td><td>10,381.59</td><td>2.52</td></tr><tr><td>2018/11</td><td>rand</td><td>1</td><td>adab2_none-isotonic- ${T}_{cs}^{i}$ -postreg</td><td>10.86</td><td>43.67</td><td>0.88</td><td>0.05</td><td>0.07</td><td>8496.65</td><td>9133.13</td><td>2.35</td></tr><tr><td>2018/12</td><td>1</td><td>1</td><td>easy_ensmb_none_sigmoid- ${T}_{cs}^{i}$ -postreg</td><td>8.95</td><td>11.37</td><td>0.72</td><td>0.12</td><td>0.17</td><td>9969.19</td><td>12,006.99</td><td>1.47</td></tr><tr><td>2018/12</td><td>0.5</td><td>1</td><td>wrf_none-isotonic- ${T}_{cs}^{i}$ -postreg</td><td>8.95</td><td>31.98</td><td>0.90</td><td>0.02</td><td>0.11</td><td>7109.03</td><td>7964.33</td><td>5.29</td></tr><tr><td>2018/12</td><td>rand</td><td>1</td><td>rf_none_sigmoid- ${T}_{cs}^{i}$ -postreg</td><td>8.95</td><td>45.67</td><td>0.92</td><td>0.00</td><td>0.15</td><td>5932.89</td><td>6994.47</td><td>6.19</td></tr><tr><td>2019/01</td><td>1</td><td>1</td><td>wrf_rus_none- ${T}_{cs}^{i}$ -postreg</td><td>12.37</td><td>9.36</td><td>0.65</td><td>0.24</td><td>0.14</td><td>12,184.36</td><td>14,212.21</td><td>0.64</td></tr><tr><td>2019/01</td><td>0.5</td><td>1</td><td>rdf_none_sigmoid- ${T}_{cs}^{i}$ -postreg</td><td>12.37</td><td>30.17</td><td>0.94</td><td>0.02</td><td>0.04</td><td>8707.68</td><td>9084.91</td><td>9.15</td></tr><tr><td>2019/01</td><td>rand</td><td>1</td><td>adab1_none-isotonic- ${T}_{cs}^{i}$ -postreg</td><td>12.37</td><td>42.44</td><td>0.95</td><td>0.02</td><td>0.72</td><td>2282.78</td><td>8058.50</td><td>7.78</td></tr><tr><td>2019/02</td><td>1</td><td>1</td><td>adab1_rus_sigmoid- ${T}_{cs}^{i}$ -postreg</td><td>14.69</td><td>10.41</td><td>0.52</td><td>0.26</td><td>0.16</td><td>12,839.96</td><td>15,316.98</td><td>0.83</td></tr><tr><td>2019/02</td><td>0.5</td><td>1</td><td>bal_rf_none_sigmoid- ${T}_{cs}^{i}$ -postreg</td><td>14.69</td><td>31.72</td><td>0.79</td><td>0.07</td><td>0.08</td><td>10,378.46</td><td>11,346.17</td><td>2.26</td></tr><tr><td>2019/02</td><td>rand</td><td>1</td><td>adab2_none_sigmoid- ${T}_{cs}^{i}$ -postreg</td><td>14.69</td><td>44.57</td><td>0.84</td><td>0.06</td><td>0.19</td><td>8279.77</td><td>10,169.78</td><td>2.45</td></tr><tr><td>2019/03</td><td>1</td><td>1</td><td>easy_ensmb_none-isotonic- ${T}_{cs}^{i}$ -postreg</td><td>11.62</td><td>12.17</td><td>0.58</td><td>0.19</td><td>0.32</td><td>10,038.56</td><td>14,837.82</td><td>0.89</td></tr><tr><td>2019/03</td><td>0.5</td><td>3</td><td>adab1_ros_sigmoid- ${T}_{cs}^{i}$ -postreg</td><td>11.62</td><td>6.69</td><td>0.36</td><td>0.39</td><td>0.25</td><td>5005.78</td><td>6637.93</td><td>0.23</td></tr><tr><td>2019/03</td><td>rand</td><td>1</td><td>adab2_rus-isotonic- ${T}_{cs}^{i}$ -postreg</td><td>11.62</td><td>47.45</td><td>0.83</td><td>0.08</td><td>0.32</td><td>5653.64</td><td>8300.72</td><td>1.20</td></tr></table>

both $R O I > 0$ and $C I S > 0 .$

## 5.2. Absenteeism prediction when costs are unknown

As mentioned in Remark 2, the value of the paramete $\cdot \widetilde { t } _ { s }$ is currently unknown. In order to provide a viable alternative to the practitioners, we assume equal misclassification costs and perform model selection using the balanced accuracy score (BACC). Table 6 presents the results of the top-performing cost-insensitive models in every prediction period. We note that there is some variation in model performance across pe riods, which we attribute to changes in the class distribution across different months.

When we compare our results to the literature, we find that a number of studies demonstrate higher performance under more severe class imbalance. For example [11] reports AUC 0.76 in a model of predicting sick leave due musculoskeletal disorders at the horizon of 3 month having less than 1% positives in their sample. Their predictors included musculoskeletal complaints, burnout, distress, among others. In [13] measures of depressed mood, distress and fatigue are used, whereas in [12] self-rated health, mental health factors and psychosocial work characteristics are described, and finally, [14] shows the highest per formance AUC 0.86 (10% positives) using an attitudinal predictor called the Work Ability Index. We conclude that when the misclassification costs are unknown, some objective health-related predictors may be necessary to achieve better performance.

## 5.2.1. Cost performance of cost-insensitive models

To investigate the cost performance of the top-ranking cost-insensi tive models, we calculated cost metrics under all nine intervention scenarios. Fig. 2 demonstrates the difference in cost performance ach ieved by the top-ranking cost-insensitive models when ranked by BACC versus top-ranking cost-sensitive models. Despite reasonable perfor mance, when evaluated using error-based metrics, cost-insensitive models rarely have positive CIS and are always inferior to costsensitive models.

Model selection based on BACC does not appear to be a viable so lution once costs are known, based on costs derived using our artificial $\widetilde { t } _ { s }$ . Instead, effort should be put into determining $\widetilde { t } _ { s }$ to facilitate the use of misclassification costs. Of course, once this is done, this statement can be revisited.

## 6. Conclusion

In this paper we describe a potential solution to a real-world prob lem, requested by HR and Well-being specialists. We were provided with an anonymised dataset containing employee payroll information only, without any health-related data. This carried the risk of the resulting models be based on correlations unrelated to health. We therefore emphasise that our conceptual model was developed under the assumption that any intervention considered aims to increase employee well-being. Thus targeting someone erroneously should never lead to a negative outcome for that individual.

Top-model selection when ranking by balanced accuracy. CIS for each combination of intervention an $\widetilde { \iota _ { t _ { s } } }$ are included for reference. Rand refers to record-dependent p ∈ [0,1].

<table><tr><td rowspan="2">Target period</td><td>Method</td><td rowspan="2">%pos</td><td colspan="4">Error-based metrics</td><td rowspan="2"> $\widetilde{t_s}/t_s$ </td><td colspan="3">CIS</td></tr><tr><td>algo_sampling_calibr-T</td><td>FNR</td><td>FPR</td><td>BACC</td><td>AUC</td><td>Case 1</td><td>Case 2</td><td>Case 3</td></tr><tr><td rowspan="3">2018/03</td><td rowspan="3">adab1_none_isotonic-Tbest</td><td rowspan="3">15.57</td><td rowspan="3">0.42</td><td rowspan="3">0.33</td><td rowspan="3">0.62</td><td rowspan="3">0.67</td><td>1</td><td>0.22</td><td>-3.98</td><td>-0.67</td></tr><tr><td>0.5</td><td>0.23</td><td>-2.56</td><td>-0.23</td></tr><tr><td>rand</td><td>0.15</td><td>-2.38</td><td>-0.18</td></tr><tr><td rowspan="3">2018/04</td><td rowspan="3">easy_ensmb_none_none-Tbest</td><td rowspan="3">8.13</td><td rowspan="3">0.40</td><td rowspan="3">0.35</td><td rowspan="3">0.63</td><td rowspan="3">0.67</td><td>1</td><td>0.24</td><td>-1.67</td><td>-0.01</td></tr><tr><td>0.5</td><td>0.12</td><td>-0.96</td><td>0.21</td></tr><tr><td>rand</td><td>0.06</td><td>-0.77</td><td>0.23</td></tr><tr><td rowspan="3">2018/05</td><td rowspan="3">easy_ensmb_none_none-Tbest</td><td rowspan="3">8.0</td><td rowspan="3">0.37</td><td rowspan="3">0.36</td><td rowspan="3">0.63</td><td rowspan="3">0.68</td><td>1</td><td>0.00</td><td>-3.16</td><td>-0.47</td></tr><tr><td>0.5</td><td>-0.19</td><td>-2.53</td><td>-0.28</td></tr><tr><td>rand</td><td>-0.84</td><td>-2.33</td><td>-0.23</td></tr><tr><td rowspan="3">2018/06</td><td rowspan="3">easy_ensmb_none_none-Tbest</td><td rowspan="3">9.12</td><td rowspan="3">0.37</td><td rowspan="3">0.34</td><td rowspan="3">0.65</td><td rowspan="3">0.70</td><td>1</td><td>0.23</td><td>-3.68</td><td>-0.61</td></tr><tr><td>0.5</td><td>0.19</td><td>-2.88</td><td>-0.36</td></tr><tr><td>rand</td><td>0.16</td><td>-2.62</td><td>-0.35</td></tr><tr><td rowspan="3">2018/07</td><td rowspan="3">adab1_none_isotonic-Tbest</td><td rowspan="3">6.87</td><td rowspan="3">0.42</td><td rowspan="3">0.31</td><td rowspan="3">0.63</td><td rowspan="3">0.68</td><td>1</td><td>0.04</td><td>-1.87</td><td>-0.05</td></tr><tr><td>0.5</td><td>-0.16</td><td>-1.29</td><td>0.13</td></tr><tr><td>rand</td><td>-0.30</td><td>-1.12</td><td>0.16</td></tr><tr><td rowspan="3">2018/08</td><td rowspan="3">adab1_ros_none-Tbest</td><td rowspan="3">6.8</td><td rowspan="3">0.42</td><td rowspan="3">0.27</td><td rowspan="3">0.65</td><td rowspan="3">0.71</td><td>1</td><td>0.11</td><td>-2.73</td><td>-0.28</td></tr><tr><td>0.5</td><td>-0.01</td><td>-2.07</td><td>-0.07</td></tr><tr><td>rand</td><td>-0.17</td><td>-1.85</td><td>-0.04</td></tr><tr><td rowspan="3">2018/09</td><td rowspan="3">easy_ensmb_none_none-Tbest</td><td rowspan="3">9.26</td><td rowspan="3">0.45</td><td rowspan="3">0.29</td><td rowspan="3">0.63</td><td rowspan="3">0.68</td><td>1</td><td>0.34</td><td>-3.14</td><td>-0.40</td></tr><tr><td>0.5</td><td>0.45</td><td>-2.23</td><td>-0.12</td></tr><tr><td>rand</td><td>0.49</td><td>-2.08</td><td>-0.05</td></tr><tr><td rowspan="3">2018/10</td><td rowspan="3">adab1_ros_isotonic-0.5</td><td rowspan="3">11.61</td><td rowspan="3">0.42</td><td rowspan="3">0.32</td><td rowspan="3">0.63</td><td rowspan="3">0.68</td><td>1</td><td>0.28</td><td>-3.30</td><td>-0.47</td></tr><tr><td>0.5</td><td>0.14</td><td>-2.23</td><td>-0.14</td></tr><tr><td>rand</td><td>0.10</td><td>-2.06</td><td>-0.09</td></tr><tr><td rowspan="3">2018/11</td><td rowspan="3">adab1_ros_none-0.5</td><td rowspan="3">10.86</td><td rowspan="3">0.41</td><td rowspan="3">0.32</td><td rowspan="3">0.63</td><td rowspan="3">0.68</td><td>1</td><td>0.15</td><td>-3.87</td><td>-0.64</td></tr><tr><td>0.5</td><td>-0.02</td><td>-2.89</td><td>-0.34</td></tr><tr><td>rand</td><td>-0.14</td><td>-2.73</td><td>-0.30</td></tr><tr><td rowspan="3">2018/12</td><td rowspan="3">adab1_none_isotonic-Tbest</td><td rowspan="3">9.04</td><td rowspan="3">0.35</td><td rowspan="3">0.36</td><td rowspan="3">0.64</td><td rowspan="3">0.69</td><td>1</td><td>0.10</td><td>-2.20</td><td>-0.18</td></tr><tr><td>0.5</td><td>-0.15</td><td>-1.45</td><td>0.06</td></tr><tr><td>rand</td><td>-0.19</td><td>-1.17</td><td>0.10</td></tr><tr><td rowspan="3">2019/01</td><td rowspan="3">easy_ensmb_none_sigmoid-Tbest</td><td rowspan="3">12.28</td><td rowspan="3">0.45</td><td rowspan="3">0.31</td><td rowspan="3">0.62</td><td rowspan="3">0.66</td><td>1</td><td>0.12</td><td>-3.81</td><td>-0.61</td></tr><tr><td>0.5</td><td>-0.09</td><td>-2.56</td><td>-0.22</td></tr><tr><td>rand</td><td>-0.23</td><td>-2.35</td><td>-0.13</td></tr><tr><td rowspan="3">2019/02</td><td rowspan="3">easy_ensmb_none_isotonic-Tbest</td><td rowspan="3">14.75</td><td rowspan="3">0.39</td><td rowspan="3">0.35</td><td rowspan="3">0.63</td><td rowspan="3">0.67</td><td>1</td><td>0.15</td><td>-4.54</td><td>-0.85</td></tr><tr><td>0.5</td><td>0.11</td><td>-3.21</td><td>-0.44</td></tr><tr><td>rand</td><td>0.04</td><td>-2.73</td><td>-0.34</td></tr><tr><td rowspan="3">2019/03</td><td rowspan="3">easy_ensmb_none_none-Tbest</td><td rowspan="3">11.71</td><td rowspan="3">0.39</td><td rowspan="3">0.32</td><td rowspan="3">0.65</td><td rowspan="3">0.70</td><td>1</td><td>0.28</td><td>-2.18</td><td>-0.13</td></tr><tr><td>0.5</td><td>0.12</td><td>-1.21</td><td>0.17</td></tr><tr><td>rand</td><td>-0.081</td><td>-1.12</td><td>0.22</td></tr></table>

![](/api/attachments/7WPU8EUY/fulltext/images/6fd71a86c4a6ef1155913a06c816383b3e60cf43793f28ca5625c1b46dc9e2c6.jpg)  
Fig. 2. Comparison of top models’ cost performance across prediction periods and interventions. The solid line represents the best performing cost-sensitive models (ranked by CIS). The dotted line shows the best performing cost-insensitive model (ranked by BACC) under the same operating conditions. The horizontal line shows CIS = 0. Here $\mathrm { ~ } ^ { \mathrm { ~ \tiny ~ \cdot ~ } } \mathrm { t } \underline { { s } } \mathrm { t i l d e } ^ { \mathrm { , , } }$ is $\widetilde { t } _ { s } / t _ { s }$ and “random” refers to record-dependent $p _ { i } \in [ 0 , 1 ]$

Our focus was on developing a flexible, algorithm-agnostic frame work to predict short-term employee sickness absence using HR and payroll data only.

Our definition of the target variable, which depends on the threshold $T _ { h r s }$ of number of hours of sickness absence can be adapted as needed. In fact, it is possible to use the same decision support system with a range of targets to focus on absences of specific duration (e.g. short term versus long term).

Thanks to relying on existing open-source implementations, our model selection and evaluation framework can be readily deployed to the cloud. We provided two alternative evaluation metrics under class and cost imbalance: with and without knowledge of costs. We demon strate that improved cost-effectiveness of intervention campaigns can be achieved by focussing classifiers on the specific operating conditions of the underlying training data.

Our main take-away for practitioners is as follows:

• In the absence of misclassification costs, balanced accuracy allows one to ensure good model performance on both classes, instead of only the positives, but cost-based metrics almost always achieve higher savings.

• Models selected based on BACC are not a cost-effective alternative to those selected on cost-based metrics. Thus efforts should be directed to quantifying the effect interventions have on individuals so that misclassification costs can be specified.

• When the expected response to an intervention is known, DMECC allows to assess the cost-effectiveness of an intervention for each observation resulting in a more profitable intervention campaign.

• Investigating the cost distribution on the available training data can allow one to conduct a preliminary cost and benefit analysis of a given intervention.

## 6.1. Limitations and future research

The experiments presented in this paper are not without limitations, some of which are subject to data availability.

Firstly, the seasonal changes in class imbalance are accounted for by including, for example, sickness absences from other years as features, as well as creating derivative features from that data (e.g. each individual’s average absences in February in all previous years).

Secondly, we assume that the effect of any given intervention does not extend beyond the prediction period. This can be rectified by either considering a longer prediction horizon (e.g. a quarter), or by extending the conceptual model to a dynamic setting. This, combined with the use of panel data to help the model cope with seasonal changes in class imbalance, might be an interesting avenue for future research.

Thirdly, our experiments hinge on the apriori knowledge of the in dividual response to the intervention, which in practice can rarely be obtained. Instead of assigning arbitrary values, this parameter could be estimated, with the help of causal inference models. Causal models es timate individual-level treatment effects from observational data or randomized control trials, an example of algorithmic causal modelling can be found in [58]. We note that in this case, the cost matrix will also depend on the performance of the chosen causal model that predicts <sup>̃</sup>t . Related to that, ways to improve the estimates of expected hours of absence per individual might also be worth revisiting.

Lastly, we assume that employees with varying hours of sickness will have identical response to any given intervention. Without the knowl edge of the true cause of absence, it is not possible to know if the absence is at all preventable. It is not realistic to target, for example, an employee with 10 h of absence caused by a common cold and an employee with 100 h of absence caused by burnout equally. To rectify this, it is highly desirable to collect objective health-related information, such as e.g. the causes of absence. An interesting direction could be to consider multiclass setting, evaluating an array of interventions or to apply costsensitive regression such as in [59,60] but with real costs.

## Acknowledgements

This research was funded by the Institute for the encouragement of Scientific Research and Innovation of Brussels – Innoviris (Project reference: 2017-Explore-61 AI-WHRM).

The data for this research was kindly provided by Attentia, specialist in HR and Well-being.

Computational resources and services were provided by the Shared

ICT Services Centre funded by the Vrije Universiteit Brussel, the Flemish Supercomputer Center (VSC).

We also thank the anonymous reviewers for their useful comments that helped improve this work.

## References

[1] OECD, Sickness, Disability and Work: Breaking the Barriers, 2010, https://doi.org/ 10.1787/9789264088856-en

[2] The World Bank, GDP (current US\$), https://data.worldbank.org/indicator/NY. GDP.MKTP.CD?end=2018 locations=EU-US-CN-OE start=2003. 2021

[3] O. Publishing, Mental Health and Work Fit Mind, Fit Job: From Evidence to Practice in Mental Health and Work, OECD Publishing, 2015, https://doi.org/ 10.1787/9789264228283-en.

[4] S.G. Aldana, N.P. Pronk, Health promotion programs, modifiable health risks, and emplovee absenteeism, J. Occup. Environ. Med. 43 (1) (2001) 36.

[5] T. DeGroot, D.S. Kiker, A meta-analysis of the non-monetary effects of employee health management programs, in: Human Resource Management: Published in Cooperation with the School of Business Administration 42 (1), The University of Michigan and in alliance with the Society of Human Resources Management, 2003, pp. 53–69.

[6] K.M. Parks, L.A. Steelman, Organizational wellness programs: a meta-analysis, J. Occup. Health Psychol. 13 (1) (2008) 58

[7] D. Pessach, G. Singer, D. Avrahami, H.C. Ben-Gal, E. Shmueli, I. Ben-Gal, Employees recruitment: A prescriptive analytics approach via machine learning and mathematical programming, Decis. Support Syst. 134 (2020) 113290.

[8] A. Tursunbayeva, S. Di Lauro, C. Pagliari, People analytics—a scoping review of conceptual boundaries and value propositions, Int. J. Inf. Manag. 43 (2018) 224–247, https://doi.org/10.1016/j.ejor.2018.06.035.

[9] A. Burdorf, Prevention strategies for sickness absence: sick individuals or sick populations? Scand. J. Work Environ. Health 45 (2) (2019) 101–102.

[10] B. Bosman, R. Roelen, H. Heymans, Prediction models to identify workers at risk of sick leave due to low back pain in dutch industry, Eur. J. Pub. Health 26 (2016), https://doi.org/10.1093/eurpub/ckw174.208.

[11] L.C. Bosman, C.A. Roelen, J.W. Twisk, I. Eekhout, M.W. Heymans, Development of prediction models for sick leave due to musculoskeletal disorders, J. Occup. Rehabil. (2019) 1–8, https://doi.org/10.1007/s10926–018-09825-y.

[12] S.F.A. Duijts, I. Kant, J.A. Landeweerd, G.M.H. Swaen, Prediction of sickness absence: development of a screening instrument, Occup. Environ. Med. 63 (8) (2006) 564–569. https://doi.org/10.1136/oem.2005.024521.

[13] M.F.A. van Hoffen, C.J. Joling, M.W. Heymans, J.W.R. Twisk, C.A.M. Roelen. Mental health symptoms identify workers at risk of long-term sickness absence due to mental disorders: prospective cohort study with 2-vear follow-up. BMC Public Health 15 (1) (2015). https://doi.org/10.1186/s12889-015-2580-x.

[14] A. Lundin, O. Leijon, M. Vaez, M. Hallgren, M. Torg´en, Predictive validity of the work ability index and its individual items in the general population, Scand. J. Publ. Health 45 (4) (2017) 350–356, https://doi.org/10.1177/ 1403494817702759.

[15] C.A.M. Roelen, M.W. Heymans, J.W. Twisk, M. Laaksonen, S. Pallesen, N. Magerøy, B.E. Moen, B. Bjorvatn, Health measures in prediction models for high sickness absence: single-item self-rated health versus multi-item sf-12, Eur. J. Publ. Health 25 (4) (2015) 668–672, https://doi,org/10.1093/eurpub/cku192.

[16] Z. Szubert, T. Makowiec-Dabrowska, D. Merecz, W. Sobala, Predictors of short- and long-term sickness absence in female post office workers in poland, Int. J. Occup. Med. Environ. Health 29 (4) (2016) 539–562, https://doi.org/10.13075 ijomeh.1896.00795.

[17] C.A.M. Roelen, C.M. Stapelfeldt, M.W. Heymans, W. van Rhenen, M. Labriola, C. V. Nielsen. U. Bültmann. C. Jensen. Cross-national validation of prognostic models predicting sickness absence and the added value of work environment variables, J. Occup. Rehabil. 25 (2) (2015) 279–287, https://doi.org/10.1007/s10926-014- 9536-3.

[18] V.S. Araujo, T.S. Rezende, A.J. Guimar˜aes, V. Araujo, P. de Campos Souza, A hybrid approach of intelligent systems to help predict absenteeism at work in companies, SN Appl. Sci. 1 (6) (2019) 536.

[19] R.P. Ferreira, A. Martiniano, D. Napolitano, E.B.P. Farias, R.J. Sassi, Artificial neural network and their application in the prediction of absenteeism at work, Int. J. Rec, Sci, Res. 9 (1) (2018) 23332–23334, https://doi,org/10.24327/LJRSR

[20] A. Martiniano, R. Ferreira, R. Sassi, C. Affonso, Application of a neuro fuzzy network in prediction of absenteeism at work, in: 7th Iberian Conference on Information Systems and Technologies (CISTI 2012), IEEE, 2012, pp. 1–4.

[21] Z. Wahid, A. Satter, A. Al Imran, T. Bhuiyan, Predicting absenteeism at work using tree-based learners, in: Proceedings of the 3rd International Conference on Machine Learning and Soft Computing, ACM, 2019, pp. 7–11.

[22] C.R.L. Boot, A. van Drongelen, I. Wolbers, H. Hlobil, A.J. van der Beek, T. Smid, Prediction of long-term and frequent sickness absence using company data, Occup. Med, 67 (3) (2017) 176–181. https://doi.org/10.1093/occmed/kqx014.

[23] G.M. Weiss, Mining with rarity: a unifving framework, ACM Sigkdd Explor Newslett. 6 (1) (2004) 7-19.

[24] G.M. Weiss, F. Provost, Learning when training data are costly: the effect of class

[25] A.-H. Homaie-Shandizi, V.P. Nia, M. Gamache, B. Agard, Flight deck crew reserve: from data to forecasting, Eng, Appl. Artif, Intell. 50 (2016) 106–114. https://doi. org/10.1016/i.engappai,2016.01.028.

[26] D.J. Hand, Measuring classifier performance: a coherent alternative to the are under the roc curve, Mach. Learn. 77 (1) (2009) 103–123.

[27] C. Elkan, The foundations of cost-sensitive learning, in: International Joint Conference on Artificial Intelligence vol. 17, Lawrence Erlbaum Associates Ltd 2001, pp. 973–978

[28] S. Viaene, G. Dedene, Cost-sensitive learning and decision making revisited, Eur. J. Oper. Res. 166 (1) (2005) 212–220.

[29] B. Zadrozny, C. Elkan, Learning and making decisions when costs and probabilities are both unknown. in: Proceedings of the Seventh ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, ACM, 2001, pp. 204–213.

[30] V.S. Sheng, C.X. Ling, Thresholding for making classifiers cost-sensitive, in: AAAI, 2006.

[31] D.R. Velez, B.C. White, A.A. Motsinger, W.S. Bush, M.D. Ritchie, S.M. Williams, J. H. Moore, A balanced accuracy function for epistasis modeling in imbalanced datasets using multifactor dimensionality reduction, Genet. Epidemiol. 31 (4) (2007) 306–315.

[32] G.M. Weiss, K. McCarthy, B. Zabar, Cost-sensitive learning vs. sampling: which is best for handling unbalanced classes with unequal error costs? Dmin 7 (35–41) (2007) 24.

[33] D.M. Powers, Evaluation: from precision, recall and f-measure to roc, informedness, markedness and correlation, J. Mach. Learn. Technol. 2 (2021) 37–63.

[34] A. Tharwat, Classification assessment methods, Appl. Comput. Inform. 17 (1) (2020), https://doi.org/10.1016/j.aci.2018.08.003.

[35] A. Luque, A. Carrasco, A. Martín, A.D.L. Heras, The impact of class imbalance in classification performance metrics based on the binary confusion matrix, Pattern Recogn. 91 (2019) 216–231.

[36] K.H. Brodersen, C.S. Ong, K.E. Stephan, J.M. Buhmann, The balanced accuracy and its posterior distribution, in: 2010 20th International Conference on Pattern Recognition, IEEE, 2010, pp. 3121–3124.

[37] M. Sokolova, N. Japkowicz, S. Szpakowicz, Beyond accuracy, f-score and roc: a family of discriminant measures for performance evaluation, in: Australasian Joint Conference on Artificial Intelligence, Springer, 2006, pp. 1015–1021.

[38] Federal Government of Belgium, Gewaarborgd Loon, https://www.socialsecurity be/citizen/nl/arbeidsongeschiktheid-ongeval-en-beroepsziekte/arbeidsongeschikt -door-ziekte/gewaarborgd-loon., 2021

[39] L. Breiman, J. Friedman, R. Olshen, C. Stone, Classification and Regression Trees, Wadsworth, 1984.

[40] F.J. Hastie, R. Tibshirani, The Elements of Statistical Learning, Springer-Verlag New York, 2009.

[41] L. Breiman, et al., Statistical modeling: the two cultures (with comments and

[42] G. Petrides, W. Verbeke, Misclassification Cost-Sensitive Ensemble Learning: A Unifving Framework, arXiv:2007.07361. 2020

[43] L. Breiman. Bagging predictors. Mach. Learn. 24 (1996) 123–140.

[44] T.K. Ho, The random subspace method for constructing decision forests, IEEE

[45] L. Breiman, Random forests, Mach. Learn. 45 (2001) 5–32.

[46] P. Geurts. D. Ernst. L. Wehenkel. Extremely randomized trees, Mach. Learn, 63 (2006) 3–42.

[47] Y. Freund, R.E. Schapire, A decision-theoretic generalization of on-line learning and an application to boosting, J. Comput. Syst. Sci. 55 (1) (1997) 119–139.

[48] C. Chao, A. Liaw, L. Breiman, Using Random Forest to Learn Imbalanced Data, Tech. Rep. University of California. Berkley, Department of Statistics, 2004.

[49] X.-Y. Liu, J. Wu, Z. Cheng Zhou, Exploratory under-sampling for class-imbalance learning, in: Sixth International Conference on Data Mining (ICDM’06), 2006, pp. 965–969.

[50] C. Seiffert, T.M. Khoshgoftaar, J.V. Hulse, A. Napolitano, Rusboost: a hybrid approach to alleviating class imbalance, IEEE Trans. Syst. Man Cybern. Syst. Hum. 40 (2010) 185–197

[51] N.V. Chawla, K.W. Bowyer, L.O. Hall, W.P. Kegelmeyer, Smote: synthetic minority over-sampling technique J Artif Intell Res, 16 (2002) 321–357

[52] B. Zadrozny, C. Elkan, Transforming classifier scores into accurate multiclass probability estimates, in: KDD, 2002

[53] J. Platt, et al., Probabilistic outputs for support vector machines and comparisons to regularized likelihood methods, Adv. Large Margin Class. 10 (3) (1999) 61–74.

[54] A. Niculescu-Mizil, R. Caruana, Predicting good probabilities with supervised learning, in: ICML, 2005

[55] F. Pedregosa, G. Varoquaux, A. Gramfort, V. Michel, B. Thirion, O. Grisel, M. Blondel, P. Prettenhofer, R. Weiss, V. Dubourg, J. Vanderplas, A. Passos, D. Cournapeau. M. Brucher. M. Perrot. E. Duchesnav. Scikit-learn: machine learning in Python, J. Mach. Learn. Res. 12 (2011) 2825–2830.

[56] G. Lemaître, F. Nogueira, C.K. Aridas, Imbalanced-learn: a python toolbox to tackle the curse of imbalanced datasets in machine learning, J. Mach. Learn. Res. 18 (17) (2017) 1–5.

[57] C. Groskopf, Contributors, csvkit, 2016.

[58] S. Wager, S. Athey, Estimation and inference of heterogeneous treatment effect

[59] M. Czaikowski, M. Czerwonka, M. Kretowski, Cost-sensitive global model trees applied to loan charge-off forecasting, Decis, Support, Syst. 74 (2015) 57–66.

[60] H. Zhao, A.P. Sinha, G. Bansal. An extended tuning method for cost-sensitive

Natalie Lawrance is a Ph.D. candidate at the Vriie Universiteit Brussel. She holds a M.Sc in Economics from KU Leuven. Her research interests lie at the intersection of the fields of Applied Economics and Machine Learning.

George Petrides is a senior researcher at the University of Bergen, Norway. He received his PhD in Mathematics at the University of Manchester (UK, 2006). Previously, he was a senior researcher at VUB, Belgium, and has lectured at various academic institutions in Cyprus and at NTNU in Norway, where he also was a post-doctoral fellow. His research interests lie within the fields of Machine Learning and Cryptology.

Marie-Anne Guerry, is full professor at the Vrije Universiteit Brussel, Belgium. She ob tained her PhD in Sciences in 1992. Currently, she is teaching mathematics at the Faculty of Social Sciences & Solvay Business School of the Vrije Universiteit Brussel. Her research activities are situated in the domain of Manpower Planning. This research covers on the one hand Markov models and their applications in quantitative Human Resources Man agement, and on the other hand HR-analytics and empirical research on career progress and career characteristics.
