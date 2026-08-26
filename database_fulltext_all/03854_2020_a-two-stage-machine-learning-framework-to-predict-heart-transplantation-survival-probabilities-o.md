---
otero_id: 3854
otero_key: "YHTAZB7Y"
title: "A two-stage machine learning framework to predict heart transplantation survival probabilities over time with a monotonic probability constraint"
authors: "Hamidreza Ahady Dolatsara; Ying-Ju Chen; Christy Evans; Ashish Gupta; Fadel M. Megahed"
year: "2020"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2020.113363"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A two-stage machine learning framework to predict heart transplantation survival probabilities over time with a monotonic probability constraint

![](/api/attachments/YHTAZB7Y/fulltext/images/46158910957600f6e777bb976992df4c960fe0e248adf8d9ae239eb3572e531b.jpg)

Hamidreza Ahady Dolatsara<sup>a</sup>, Ying-Ju Chen<sup>b</sup>, Christy Evans<sup>c</sup>, Ashish Gupta<sup>d</sup>, Fadel M. Megahed<sup>e,⁎</sup>

<sup>a</sup> School of Management, Clark University, Worcester, MA 01610, USA

<sup>b</sup> Department of Mathematics, University of Dayton, Dayton, OH 45469, USA

<sup>c</sup> Department of Biological Sciences, Auburn University, Auburn, AL 36849, USA

<sup>d</sup> Harbert College of Business, Auburn University, Auburn, AL 36849, USA

<sup>e</sup> Farmer School of Business, Miami University, Oxford, OH 45056, USA

## A R T I C L E I N F O

Keywords. Data mining Heart transplant Isotonic regression Medical informatics Multi-period forecasting United network for organ sharing

## A B S T R A C T

The overarching goal of this paper is to develop a modeling framework that can be used to obtain personalized data-driven and monotonically constrained probability curves. This research is motivated by the important problem of improving the predictions for organ transplantation outcomes, which can inform updates made to organ allocation protocols, post-transplantation care pathways, and clinical resource utilization. In pursuit of our overarching goal and motivating problem, we propose a novel two-stage machine learning-based framework for obtaining monotonic probabilities over time. The first stage uses the standard approach of using independent machine learning models to predict transplantation outcomes for each time-period of interest. In the second stage, we calibrate the survival probabilities over time using isotonic regression. To show the utility of our framework, we applied it on a national registry of U.S. heart transplants from 1987 to 2016. The first stage produces an area under the receiver operating curve (AUC) between 0.60 and 0.71 for years 1–10. While the 1- year prediction AUC result is comparable to the reported results in the literature, our 10-year AUC of 0.70 is higher than the current state-of-the-art results. More importantly, we show that the application of isotonic regression to calibrate the survival probabilities for each patient over the 10-year period guarantees mono tonicity, while capitalizing on the data-driven and individualized nature of machine learning models. To promote future research, our code and analysis are publicly available on GitHub. Furthermore, we created a web app titled “H-TOP: Heart Transplantation Outcome Predictor” to encourage practical applications.

## 1. Introduction

There exists numerous applications where a decision-maker is in: terested in evaluating the probabilities of observing a terminal state of a process or a system at multiple time periods. Recent studies have examined applications such as (a) the time-taken to complete a higher education degree [1], where the probability of completing the degree by the end of the $n ^ { t h }$ year will be less than or equal to the completion probability by the $( n \dot { + } 1 ) ^ { t h }$ year; (b) churn prediction in the energy [2], higher education [3], and telecommunications [4] sectors, where the probability of client's churn is montonically increasing with time; (c) supply-chain servicing probabilities are monotonically increased with increases in delivery window sizes [5]; and (d) surgical applications, e.g., lung [6], heart [7,8], and kidney [9] transplants where patients survival probabilities monotonically decrease over time. The utility of a decision support system in such applications hinges on accurate multiperiod predictions, where the predicted outcome probabilities are monotonic over time.

There are two common approaches for achieving monotonic survival probabilities. The first approach involves the use of populationbased survival analysis techniques using Kaplan-Meier estimates [10], which are not well suited for applications involving a large number of potential predictors and/or when an individualized prediction is important (e.g., organ-allocation decisions). On the other hand, machine learning methods (ML) are used in the second approach to estimate the survival, or any outcome of interest, probability for each time-period being investigated. The utility of existing ML applications for multiperiod prediction is limited since current approaches (a) develop independent ML models for each time-period [8,11], which do not guarantee the expected monotonic probability outcomes over time; (b)

utilize a sequential prediction approach where the “survival” probabilities from time periods $1 , 2 , 3 , . . . ,$ t are inputs to predict the survival at time t + 1 [12,13], however, such approaches also do not guarantee monotonicity as the utilized ML models do not include a hard constraint on the predicted probabilities due to their assumption-free nature; or (c) apply the ML approach to predict the outcome probability for one time-period and use the population's survival outcomes to calibrate other periods' probabilities [14]. This particular drawback limits the changes in the outcome probabilities to those captured by the population averages, and hence, may not be efective when the case being investigated has predictors that deviate significantly from the average case. This is not uncommon in healthcare applications, and is an important driving factor for the recent developments in personalized medicine [15].

The overarching goal of this paper is to develop and comprehen sively describe a modeling framework that can be used to obtain personalized, data-driven and monotonically constrained probability curves. Our research is motivated by the important and open-research problem of predicting organ transplantation outcomes based on solely pre-operative data in order to provide decision making assistance for organ-allocation protocols [6,9], post-transplantation clinical and care pathways [16], and clinical resource utilization [16]. In pursuit of these objectives and with the limitations in existing transplantation literature in mind [8,11–14], we propose a novel two-stage machine learningbased framework for obtaining monotonic “survival” probabilities over time. The first stage utilizes the standard approach of using independent machine learning models to predict survival outcomes for each time-period of interest [e.g., see [8,11]]. The primary objective in this stage is to select the most predictive/eficient machine learning model based on a predefined performance measure (e.g., area under the receiving operating characteristics curve, AUC). However, as mentioned earlier, this approach sufers from the drawback that the ob tained survival probabilities from stage-one are not guaranteed to be monotonically decreasing. Therefore, in the second stage, we calibrate the survival probabilities over time using isotonic regression [17], which constrains the survival probabilities (p) such that $p _ { t + 1 } \leq p _ { t }$ , ∀ t. Thus, isotonic regression ensures that the survival probabilities are monotonically decreasing and that the results are personalized based on the donor and recipient's characteristics.

The remainder of this paper is organized as follows. Section 2 provides an overview of our proposed two-stage framework for multiperiod monotonic probabilistic outcome predictions. Section 3 describes the significance of the heart transplantation problem, the need for risk stratification, and the decisions made throughout the transplantation process. Section 4 explains how the proposed two-stage framework can be applied to multi-period predictions of heart transplantation survival probabilities. Section 5 describes the results of our application. Finally, Section 6 describes the implications of those results to advancing heart transplantation research/practice as well as providing opportunities for future research in applied machine learning. In the supplementary materials section, we provide a link to a web-based decision support system, which can facilitate the use of the proposed framework in informing organ-allocation protocols and post-transplantation clinical pathways. Furthermore, we share a link of our R Markdown document that includes our code and analyses to facilitate the adoption and integration of our proposed methodology in future research.

## 2. The two-stage framework for obtaining monotonic prediction probabilities over time

The data revolution has popularized the use of data-driven predictive models that significantly departed from the traditional empirical modeling approach in Information Systems [18,19]. Nevertheless, as noted by Shmueli and Koppius [18, p. 554], data-driven predictive modeling is a “core scientific activity” that is “useful for generating new theory, developing new measures, comparing competing theories, improving existing theories, assessing the relevance of theories, and assessing the predictability of empirical phenomena.” To reap the benefits of predictive models, one must strive to (a) have accurate and precise results, (b) be able to present the right information with the required level of granularity [19], and (c) not capitalize on chance [20].

This paper proposes a generic framework for multi-period monotonic probabilistic outcome predictions. The goals of our framework are to enable: (a) accurate and precise results by enabling the use of any statistical, machine or deep learning method for predicting the outcome probability for a given time period; (b) presenting the right information with the required granularity through the emphasis on data-driven and personalized/individualized predictions; and (c) not capitalizing on chance (where we avoid over-fitting and ensure that the outcomes are monotonic through the incorporation of a hard mathematical constraint on the magnitude of the probability outcomes for each period). To ensure that the framework is “generic”, our framework does not require the use of a specific machine learning algorithm to obtain the probability estimates since their utility may difer by problem (e.g., variations in number of variables, observations, computational processing requirements and/or requirements for prediction accuracy and interpretation). Furthermore, we have considered an approach for guaranteeing monotonic outcomes for any t > 1 time periods, which makes our approach efective even when only two periods are considered.

Our framework addresses two major shortcomings of existing frameworks in the literature: the non-existence of a framework that i comprehensive enough to be readily applied by analysts over multiple time periods, yet generic enough to be applicable across various domains. These two characteristics of our framework allow for the utili zation of machine learning results in informing decision making in response to multi-period information. The flexibility and comprehensiveness of a decision-making framework are key requisites for its successful integration in practice [21,22].

In the first stage of our proposed framework, independent statistical, machine and/or deep learning models are applied to predict the prob ability of the binary outcome for each time-period of interest. As such, this stage will involve the following standard data analytic steps: (a) data collection, (b) data preparation, (c) choosing a set of candidate models, (d) training the models, (e) evaluating the models based on one or more performance metrics of interest, (f) parameter tuning, and (g) model selection based on the performance of the tuned-models on one or more holdout/test dataset. For the sake of conciseness, we do not cover these steps in greater detail here since they are well-documented in the literature and standard textbooks [e.g. see 23]. These steps are repeated for each time-period of interest; therefore, the output from this stage is a computed probability of an event (e.g., a client's churn, an organ's failure, or a patient's survival post surgery) for the diferent time-periods. This output can be represented by $\begin{array} { r } { p = p _ { 1 } , p _ { 2 } , . . . , p _ { t } , } \end{array}$ where $p _ { t }$ is the computed outcome probability at period t as obtained from the selected model.

In Stage 2, we propose the use of isotonic regression to calibrate and ensure that the elements in p are monotonic. For example, if we were to consider were the required outcome should be monotonically decreasing, this can be achieved by solving the following optimization problem

$$
\begin{array}{c c} \min & \sum_ {i = 1} ^ {t} w _ {i} (y _ {i} - p _ {i}) ^ {2} \\ \text {subject to} & y _ {m a x} = y _ {1} \geq y _ {2} \geq ... \geq y _ {t} = y _ {m i n}, \end{array}\tag{1}
$$

where w is a strictly positive weight and $y _ { i }$ denotes the calibrated probability at time $i ( \mathrm { i . e . , }$ , the $y _ { s }$ are the decision variables obtained from the optimization model). We use $w _ { i } = 1$ , ∀ i since this corresponds to the squared Euclidean distance $( \mathrm { i . e . } _ { \cdot }$ , the objective function would have a physical interpretation). The reader should note that in our framework we preferred isotonic regression to other possible calibration approaches (e.g., the sigmoid smother used in support vector machine [24]) since it (a) works well for any t > 1 period; (b) is a non-parametric approach, which requires no further tuning; (c) is computationally eficient since the optimization problem can be solved in ( )n time using the pool adjacent violators algorithm (PAVA) [25]; and (d) can be easily adapted for non-decreasing probabilities (by changing the constraint to $y _ { m i n } = y _ { 1 } \leq y _ { 2 } \leq \ldots \leq y _ { t } = y _ { m a x } ) .$

Proposed framework using isotonic regression to calibrate multi-period ML probabilities  
![](/api/attachments/YHTAZB7Y/fulltext/images/ede2431de6090ef8041f53ff8b214cd88ecd225d9fd5cd54d028ce9a27ccce4b.jpg)  
Fig. 1. An animated illustration of how isotonic regression is used to calibrate multi-period ML probabilities. To view the animation, the reader is referred to the online version of the article. Alternatively, the reader can also view the animation on our Markdown document (see the supplementary materials).

Fig. 1 provides an overview of how isotonic regression can be used to calibrate the outcome probabilities obtained from the Stage 1. In the figure, we chose to simulate the case where the researcher is interested in computing an organ's failure probabilities over a 20 year time-period post-transplant to illustrate the utility of our approach to a non-decreasing prediction problem. Hereafter, we will only consider the opposite case where one would like to predict the survival probability post transplant (i.e., the probabilities would be monotonically decreasing over time).

## 3. Problem description

Heart failure is a serious medical condition, which can be characterized by the heart not being able to pump enough blood and oxygen to support other organs [26]. It is “a global pandemic afecting at least 26 million people worldwide and is increasing in prevelance” [26]. For example, in the U.S., the number of heart failure patients was 5.7 million in 2009–2012, which has increased to 6.2 million in 2013–2016 and is expected to increase to 8 million by 2030 [27]. Despite the ad vancements in treatment protocols, the outlook for heart failure patients remains poor as (a) “heart failure has no cure” [28] and (b) the 5- year mortality is ≈50% [27], which is worse than the five-year rate for patients sufering from various cancers such as bowl, breast, colon and prostate cancers [29].

Heart transplantation is the most efective treatment for patients with end-stage heart failure. For adult recipients, the median survival time after a heart transplant is 9.5 years, which is significantly better than the median survival of 2.3 years for wait-listed patients who do not receive a transplant [27]. In the U.S., there were 3552 heart transplants performed in 2019 [30], with an additional 3527 wait-listed candidates as of May 28, 2020 [31]. Fig. 2 depicts the five phases of the U.S. heart transplantation process, which are based on the descriptions in the United Network for Organ Sharing (UNOS) matching procedure [32].

In phase I, an eligible end-stage heart failure patient is accepted to a transplant hospital as a transplant candidate. At this point, the candidate is wait-listed and their medical data (e.g., height, weight, blood type, medical urgency) as well as the hospital's location are added to the UNOS database [32]. Phase II initiates when (a) a donor heart is available in a localized geographic area such that preservation and transport time are feasible, and (b) the candidate is deemed compatible with donor heart based on blood type, height, weight, and other medical factors [32]. At this point, the candidate is referred to as a potential transplant recipient (PTR). The UNOS algorithmic allocation protocol [32] would perform a “match run” of all PTRs and rank them based on (i) medical urgency considerations, (ii) geographic proximity to the donor's hospital, and (iii) pediatric status. The organ is ofered to transplant centers in the order of the “match run”; it is not uncommon that a PTR would go back to the first phase of being wait-listed (e.g., if not highly ranked by the “match run”) [32]. Consequently, the PTR only advances to the third phase (transplantation) if they were selected by the “match run” and the transplant ofer is accepted by the transplant hospital (i.e., after additional medical prognoses). The patient, at this point, is referred to as the recipient. Phase IV is comprised of the inhospital post-transplant care, where the recovery and discharge are governed by the respective policies, procedures and pathways set by the hospital and/or transplantation team. Phase V captures the out-patient post-transplant process, where the recipient adopts the prescribed life style and protocols in order to prolong the lifetime of the graft and return to society. The recipient is examined regularly in phase V for possible complications; in the case of a graft failure, the recipient would be evaluated for re-transplantation and is returned to phase I [33].

![](/api/attachments/YHTAZB7Y/fulltext/images/5dbd4a344175f32f632126aac229e053f9cb62eacc010c790355d9fa26b37dc6.jpg)  
Fig. 2. An overview of the decisions made throughout the transplantation process.

The stated goals of the UNOS “policies and computerized network [are to] match donated organs with transplant candidates in ways that save as many lives as possible and provide transplant recipients with the best possible chance of long-term survival” [32]. With these goals in mind, proposed changes to the UNOS policies are periodically examined [e.g., see 34], and merited proposals are adopted [35] to con tinuously improve the transplantation outcomes. By analyzing and modeling the UNOS data, we aim at improving the utility of the existing approaches for multi-period heart transplantation prediction [8,11–14], described in Section 1. Our two-stage framework allows for the use of any machine learning method to obtain individualized, monotonically decreasing multi-period survival probabilities for any PTR at the “match run” phase. The implications of our approach to risk stratification are three-fold: (a) improving predictive accuracy (allowing for the incorporation of best practices to data cleaning, model selection, and tuning) and a more precise calibration of the survival probabilitie over time (accounting for the specific parameters' values of evaluated cases); (b) providing UNOS with a benchmark to compare the expected outcomes from a match, which in the long-run can potentially inform the policies and algorithms governing phase II of the transplantation process; and (c) informing the protocols prescribed by the transplan tation team in phases IV and V based on the estimated survival risk.

## 4. Application of the two-stage framework to predict transplantation survival outcomes

Fig. 3 provides an overview of the application of our two-stage framework for obtaining monotonically decreasing survival probabilities. Our goals for Stage I are to select an appropriate model based on its predictive performance and examine how the selected variables importance change over time. Stage I is comprised of the following steps: (a) raw data undergoing detailed data preparation that explains how missing data is handled and how indicator variables are generated; (b) use subsampling techniques to handle the imbalance between graft survivals and failures at a given time point; (c) use of a structured variable selection technique to improve the performance of machine learning models [7,8]; and (d) use of machine learning (ML) models to predict survival probabilities for the various time periods. In our application, we examine 11 prediction periods one-month posttransplant, and 1–10 years post-transplant. These periods were selected to capture the acute rejection period (typically at one-month posttransplant [36]), short-term survival (< 3 years post-transplant [8]), medium-term survival (typically at 3–5 years post-transplant [8]), and long-term survival (typically at 9+ years, post-transplant [8]). In Stage II, we calibrate the survival probabilities such that they are monotonically decreasing over time. Stage II has two steps: (a) combining outputs from all time points derived from Stage I models and forming a probability matrix, and (b) the application of isotonic regression to calibrate the probability function.

4.1. Stage I: Using ML methods to obtain a survival probability at each time point

## 4.1.1. Data description

Our UNOS dataset covered 103,570 heart transplant events up to and including September 30, 2016. The dataset has been anonymized by UNOS and contains 494 variables, capturing various pre-, intra-, and post-transplant information. Note that variables/records within the UNOS dataset have a large number of missing data. In our case, more than 30% of the “data-table cells” had missing values for various reasons. For example, the start date of data collection for 327 of the 494 variables (66.19%) had a start date of 1990 or after. Moreover, some of the variables had missing-at-random values due to possible data entry and collection problems; a variable is not considered to be missing-at random $\operatorname { i f } , \operatorname { e . g . }$ , the frequency of missing data changes significantly by transplant year. Thus, a prerequisite to analyzing the UNOS dataset is a detailed data cleaning/preparation procedure that will facilitate reproducible analyses.

![](/api/attachments/YHTAZB7Y/fulltext/images/9d2165226748fc235630b639a2fd005b20270346c0d61ae4b1b0843f3ac6f35d.jpg)  
Fig. 3. Adopting the proposed two-stage framework to obtain monotonically decreasing heart transplantation survival probabilities over time.

## 4.1.2. Data preparation/cleaning

Our procedure for cleaning the UNOS dataset was comprised of six steps. The first step focused on reducing the dimensionality of the data by removing the following sets of variables: (a) intra- and post-transplant variables, where we have only kept G-TIME (a continuous variable capturing the time in days from transplant to graft failure) and G-STATUS (a binary variable, denoting if the graft has failed or not at the last follow-up time) as they are used in constructing the dependent survival outcome at a given time point; (b) variables with an end data collection-date since they cannot be used in future PTR evaluations; (c) variables with a recent data-collection-date, where we only included variables that were added before 2000; and (d) any variable that had ≥90% missing since imputation techniques would produce biased results. We refer the reader to our R Markdown document, which contains our code and analysis and whose link is provided in the Supplementary Materials Section of this paper.

The second step involved determining whether a record should be used for analysis (for a given time point). Any transplantation event was censored if we did not have information pertaining to a patient's survival at the time point of interest $( \boldsymbol { \mathrm { e . g . , } }$ , a recipient was alive at day 300 post-transplant, would not explain whether he/she would have survived to the end of year 1). Our censoring procedure followed the approach of Dag et al. [8], capitalizing on both G-TIME and G-STATUS. Specifically, the data was censored if and only if the G-TIME was less than the number of days required for the time-point analysis and the G-STATUS indicates that the recipient was still alive. Accordingly, the dichotomous outcome for the $i ^ { \star h ^ { \star } }$ recipient at time t was coded based on

$$
o _ {i, t} = \left\{ \begin{array}{l l} 1, & \text { if   the   } i ^ {t h} \text {   recipient   was   alive   at   time   } t \\ 0, & \text { if   the   } i ^ {t h} \text {   recipient   was   dead   at   time   } t \end{array} \right..\tag{2}
$$

The third step in our recommended data preparation procedure generated medically-relevant features that have been shown as important/predictive in the literature. These features were computed by combining information from two or more independent variables. In our analysis, we created the following features based on [7,8,14]: (a) pul monary vascular resistance (PVR), (b) ischemia time in minutes, (c) mismatch in Extracorporeal membrane oxygenation (ECMO) for recipient between registration and transplant, (d) percent change in the recipient's body mass index (BMI) between registration and transplant, (e) percent change in the recipient's weight between registration and transplant, (f) percent change in the recipient's height between registration and transplant, (g) the absolute diference in age between donor and recipient, and (h) the absolute diference in BMI between donor and recipient. For additional detail on how each feature was generated, we refer the reader to our R Markdown document.

The fourth step related to the handling of missing data. In the first step of our data cleaning process, we removed any categorical variable that has ≥90% missing values, numerical variable that has ≥30% missing values, and categorical variables which are almost invariant (> 90% of the values are in one level). Note that we have allowed a larger threshold for categorical variables since we imputed these values as “unknown” in one of our categorical imputation procedures. We do acknowledge that other thresholds could have been used (and their choice can possibly afect our prediction performance); however, we did not explore other values in our analysis as our prediction results were reasonable and we examined a large number of imputation, encoding, sub-sampling and algorithm combinations. We utilized the following imputation strategy (a) correctly defining independent vari able types in the analytical software, and (b) comparing the predictive performance of the models with no imputation and the models with imputation (median/mean and mode imputation for numeric and categorical variables, respectively). This performance comparison would suggest if data imputation can lead to improvements in the prediction results and whether a more computationally intensive imputation technique was warranted.

In the fifth step, the levels of categorical variables were regrouped. We attempted to reduce the number of levels, by removing any level, which has a limited number of observations, and re-coding the values such that they are added to the level corresponding to “other”. The purpose of this step was three-fold: (a) avoiding over-fitting, (b) reducing the possibility of errors due to factor levels not observed in the training of the model, and (c) reducing the dimensionality/complexity of the developed model (especially for tree-based approaches such as random forests). Additionally, many implementations of machine learning algorithms require the categorical variables to be encoded either using label or one-hot encoding.

The sixth step of data preparation involved splitting the data randomly into a training (80%) and a hold-out (20%) set. We used a 5-fold cross validation approach for selecting an appropriate model from the training set since (a) it is more computationally eficient than 10-fold cross validation, and (b) both $k = 5$ and $k = 1 0$ “have been shown empirically to yield test error rate estimates that sufer neither from excessively high bias nor from very high variance” [23, p. 183].

## 4.1.3. Variable selection

Variable selection approaches attempt to (a) reduce the computational burden by reducing the dimensionality of the feature space, (b) improve the prediction performance by focusing only on important variables, and (c) improve the generalizability of the developed prediction models. Variable selection approaches can be categorized into three main groups: [37] (a) filter methods, where univariate statistical approaches are typically used to select features based on their relationship to the response, (b) wrapper methods, where the important features are kept based on their prediction performance, and (c) embedded methods, which involve the use of methods such as LASSO and random forests for selecting the most predictive features. In our case study, we compared the performance of fast feature selection, LASSO, and random forests for feature selection.

## 4.1.4. Sub-sampling approaches for imbalanced data

On average, the expected survival probability for heart transplan tation recipients decreases by about 3–4% per post-transplant year [38]. Moreover, the aforementioned censoring approach would result in the removal of recipients who are currently surviving, but have not reached the time-point of interest. Consequently, we expect that the short time intervals (e.g., 1 month, 1 year, etc.) will have a much larger number of survivals than deaths, and the longer time-periods (e.g., 9- and 10- years post-transplant) will have a higher ratio of deaths to survivals. In the data mining literature, sub-sampling methodologies are typically deployed to improve the prediction performance when the underlying training dataset is imbalanced [39]. We considered five subsampling strategies:

(A) No sub-sampling (None), which can be considered as the baseline for comparison;

(B) Random under-sampling (DOWN), where the majority class is sampled without replacement such that the number of observations in both classes (i.e. 0 and 1) are equal;

(C) Random over-sampling (UP), where the minority class is sampled with replacement such that the number of observations in both classes (i.e. 0 and 1) are equal;

(D) Synthetic minority oversampling technique (SMOTE), where the minority class is over-sampled by “taking each minority class data point and introducing synthetic examples along the line segments joining any or all of the k-minority class nearest neighbors” [40,p.

342], and repeating the process until the number of observations per class is approximately equal; and

(E) ROSE, where a statistical approach based on the smoothed bootstrap sub-sampling technique of Menardi and Torelli [41] is used for handling the class imbalance problem.

Note that these approaches were selected since they are widely used in machine learning practice due to their implementation within the popular “caret” package in R.

## 4.1.5. Application of statistical and machine learning algorithms

As mentioned in Section 1, our primary goal is to develop a framework that can calibrate the survival probabilities obtained from machine learning (ML) algorithms over multiple time points. From this point of view, our approach (in Stage II) is designed to work with any machine learning methodology that can be used for two-class problems. In our experience with the UNOS dataset, the utility of a given ML algorithm can difer significantly based on the data preparation methodology utilized. Algorithms for predicting dichotomous outcomes can be categorized into:

(A) Statistical models, which are not assumption free. Logistic regression (LR) is the most frequently utilized approach in the literature [see e.g., 8, 11, 42]. Linear discriminant analysis (LDA) also showed good predictive performance in the literature [43].

(B) Single (data-driven) classifiers, which include a large group of assumption-free machine learning approaches. Commonly used algorithms include artificial neural networks (ANNs) [8,11,12,42], decision trees (CART) [7,8], and support vector machines (SVM) [8]; and

(C) Ensemble approaches, where single classifiers' predictions are combined using voting schemes. In our analysis, we examined random forests (RF) and eXtreme Gradient Boosting (XGB).

We considered all the aforementioned seven ML algorithms (LR, LDA, ANN, CART, SVM, RF and XGB) in the prediction of the heart transplantation survival probabilities.

## 4.1.6. Evaluation and model selection

Based on our Stage I description, we considered six modeling fac tors, with the following levels;

(A) 2 categorical imputation strategies (drop and impute missing as “unknown”);

(B) 2 numerical imputation strategies (drop and median imputation);

(C) 2 categorical variable encoding approaches (label and one-hot);

(D) 3 variable selection approaches (fast feature selection, LASSO, and random forests);

(E) 5 sub-sampling methods (none, DOWN, UP, SMOTE and ROSE); and

(F) 7 machine learning models (LR, LDA, ANN, CART, SVM, RF and XGB).

Furthermore, we followed the recommendation of James et al. [23] in using 5-fold cross validation in model selection. To examine short, mid- and long-term survival, we stated that we would examine 11 prediction time-periods to generate the survival probability curve. Consequently, the enumeration of these combinations would result in $2 \times ~ 2 ~ \times ~ 2 ~ \times ~ 3 ~ \times ~ 5 ~ \times ~ 7 ~ \times ~ 5 ~ \times ~ 1 1 ~ = ~ 4 6 { , } 2 0 0$ runs. These runs correspond to running a general factorial experiment to compute the main factor efects and all high order interactions for the settings associated with each step of our framework.

We reduced the computational burden to 4200 runs by comparing the predictive performance of those combinations based on the 1-year prediction period. We have chosen 1-year since it (i) provided us with the largest sample size (with the exception of the 1-month time period where the focus is on acute organ rejection prediction), and (ii) it is a commonly used period in the literature [e.g., see 8, 14, 11]. The selected modeling approach will then be trained for all other periods for the sake of demonstrating the need and utility of our isotonic regression calibration approach in Stage II.

Table 1  
Confusion matrix for the heart transplantation prediction application

<table><tr><td rowspan="2" colspan="2"></td><td colspan="2">Predicted outcomes</td></tr><tr><td>0</td><td>1</td></tr><tr><td rowspan="2">Actual class</td><td>0</td><td>true negative (TN)</td><td>false positive (FP)</td></tr><tr><td>1</td><td>false negative (FN)</td><td>true positive (TP)</td></tr></table>

For model selection and evaluation, we reported five common performance metrics that are suited for two class classification pro blems. To present these metrics, let us consider the confusion matrix in Table 1. Based on this confusion matrix, the five metrics can be defined as follows:

$$
a c c u r a c y = \frac {T N + T P}{T N + F P + F N + T P},\tag{3}
$$

$$
s e n s i t i v i t y = \frac {T P}{T P + F N},\tag{4}
$$

$$
s p e c i f i c i t y = \frac {T N}{T N + F P}, \mathrm{and}\tag{5}
$$

$$
G - m e a n = \sqrt {s e n s i t i v i t y \times s p e c i f i c i t y}.\tag{6}
$$

The receiver operating characteristics (ROC) curve can be plotted with the sensitivity on the y-axis versus 1 − specificity on the x-axis. The area under the curve (AUC) captures how well the model predicts actual survival as survivals and actual deaths as deaths. AUC is our fifth metric.

In this paper, we used G − Mean as the primary metric for model selection since it (a) is suitable for unbalanced classification problems, and (b) penalizes models where there is a large discrepancy between sensitivity and specificity (i.e., more suitable than AUC when similar values for sensitivity and specificity performances are preferred). Thus, we would select the combination of categorical imputation, numerical imputation, categorical variable encoding, sub-sampling and machine learning model with the highest average G − Mean across the five cross-validation models.

## 4.1.7. Application of selected ML model to remaining 10 time periods

From our two-stage framework's perspective, isotonic regression can be applied to survival probabilities obtained from diferent models. However, for the sake of convenience, in this paper we are applying it to probabilities obtained from the selected modeling approach based on Section 4.1.6. This means that, we would re-train our machine learning approach for each time-period, while maintaining the data preparation procedure selected from the comparison of the 4200 runs for the firstyear post-transplant analysis. Based on this step, we would compute a survival probability for each of the 11 time-periods in order to construct the survival probability curve.

## 4.2. Stage II: calibrating the stage I prediction probabilities

For a given transplantation event, let $\pmb { p } = p _ { 0 } , p _ { 1 } , p _ { 2 } , . . . , p _ { 1 0 }$ correspond to the obtained survival probabilities from Stage I, where 0 reflects the first month and 1 → 10 denote the number of years posttransplant. Isotonic regression can be used to ensure that the elements within p are non-increasing based on the formulation and solution approach presented in Section 2.

Table 2  
Important variables selected with the corresponding frequency using LASSO.

<table><tr><td>Selected</td><td>Variables</td></tr><tr><td>11</td><td>AGE DON, BMI CALC, COD CAD DON, CREAT TRR, DIAG, FUNC STAT TRR, INIT HGT CM CALC, ISCHTIME, MED COND TRR, REGION, TBILI, TCR DGN</td></tr><tr><td>10</td><td>CMV DON, DAYS STAT1A, DIAB, DRMIS, ETH MAT, ETHCAT, PRI PAYMENT TCR, PRI PAYMENT TRR, THORACIC DGN, TRANSFUSIONS, VENT SUPPORT AFTER LIST</td></tr><tr><td>9</td><td>CARD SURG, GENDER MAT, HCV SEROSTATUS, LIFE SUP TRR, PROC TY HR</td></tr><tr><td>8</td><td>PRIOR CARD SURG TCR, SUD DEATH</td></tr><tr><td>7</td><td>DOPAMINE, FUNC STAT TCR, HBV CORE, HGT CM TCR, INFECT IV DRUG TRR, PT T4 DON, PULM CATH DON</td></tr><tr><td>6</td><td>AMIS, DAYS STAT1, EDUCATION, HEPARIN, HGT CM CALC, INOTROP VASO CO TRR, LIFE SUP TCR, PRIOR CARD SURG TYPE TCR, TBILI DON</td></tr><tr><td>5</td><td>BUN DON, CHEST XRAY DON, HIV SEROSTATUS, IMPL DEFIBRIL, INOTROP VASO PCW TRR, INOTROP VASO SYS TCR, OTHER INF DON, PT DIURETICS DON, STERNOTOMY TRR</td></tr><tr><td>4</td><td>BRONCHO LT DON, CONTIN CIG DON, EBV SEROSTATUS, ETHCAT DON, HEMO SYS TCR, HEMO SYS TRR, HLAMIS, HTLV2 OLD DON, LAST INACT REASON, SHARE TY</td></tr><tr><td>3</td><td>CORONARY ANGIO, DAYS STAT1B, GENDER DON, HBV SUR ANTIGEN, INIT AGE, INOTROP VASO MN TRR, PULM INF DON, TATTOOS, WGT KG DON CALC</td></tr><tr><td>2</td><td>AGE, ANCEF, ANTIHYPE DON, BMIS, CLIN INFECT DON, CONTIN OTH DRUG DON CRSMATCH DONE, DAYSWAIT CHRON, HGT CM DON CALC, HIST OTH DRUG DON, INIT BMI CALC, INIT STAT, INOTROPIC, PRIOR CARD SURG TRR, PVR, SGOT DON</td></tr><tr><td>1</td><td>ABO DON, AGE MAT, BRONCHO RT DON, END STAT, GENDER, HEMO PA DIA TRR, INOTROP VASO SYS TRR, INOTROPES TRR, PROTEIN URINE, VASODIL DON</td></tr></table>

The UNOS variables are defined at https://www.srtr.org/requesting-srtr-data/saf-data-dictionary/. Due to page limits we do not redefine them here.

## 5. Results

5.1. Stage I results: using ML methods to obtain survival probabilities for the 11 time periods

## 5.1.1. Data cleaning results

Per our data cleaning procedure described in Section 4.1.2, we have 8 total scenarios (2 categorical imputations × 2 numerical imputations $\times \_ 2$ categorical encoding methods). Based on these scenarios, the number of observations and independent variables varied between $2 6 , 8 2 9 \ - \ 4 5 , 0 8 9$ and 90 − 269, respectively. In our R Markdown document, we provide the following details: (a) number of preoperative variables in the dataset, (b) distribution/frequency of percent missing in the pre-operative variables, (c) variables that were not included in the analysis, (d) percent cells changed by imputing unknown, and (e) total number of indicator variables after applying one hot encoding.

## 5.1.2. Predictor variable importance over the 11 time periods

Table 2 summarizes the important variables according to the number of times selected. Twelve variables were selected for 11 perjods: (a) the donor's age: (b) recipient's body mass index: (c) deceased donor's cause of death; (d) recipient's serum creatinine level at transplant; (e) recipient's primary diagnosis; (f) recipient's functional status at transplant; (g) the recipient's calculated height at listing; (h) ischemic time; (i) recipient's medical condition at transplant; (j) UNOS region where transplanted; (k) serum total bilirubin at transplant time; and (l) candidate diagnosis at listing.

## 5.1.3. Comparison of the ML algorithms' results

Table 3 presents an overview of the prediction performance of the seven machine learning algorithms (with the best data preparation/ preprocessing approach for a given algorithm). We have arranged the table in descending order based on G − Mean since we prefer to have a model that penalizes large discrepancies between sensitivity and specificity. Note that, irrespective of our pre-algorithm preparation procedure, SVM did not converge. Therefore, we do not report any results for SVM. Based on Table 3, logistic regression (LR) presented the best G − Mean performance with (a) median imputation for missing numeric values, (b) imputing missing categories as “unknown”, (c) onehot encoding for categorical variables, (d) LASSO for feature selection, and (e) UP sampling. While the results are not statistically significant when compared to other approaches, we believe LR is the best approach since it is the quickest to run and most understandable by health-professionals. We only discuss the LR results, with (a)-(e) preprocessing, hereafter.

We present the ROC curves for Years 1 − 9 in Fig. 4. Our model yields an AUC value between 0.634 − 0.700 and 0.596 − 0.705 for the training and test sets, respectively. To present a complete picture of the model's hold-out performance, we provide the values for accuracy, specificity, sensitivity, AUC, and G − Mean in Table 4. These values capture the performance of the LR modeling approach, with (a)-(e) settings, for the hold-out dataset, which was limited to those observations where the recipients' survival statuses are available for all time periods.

In standard machine learning applications, the results shown in Fig. 4 and Table 4 are suficient to describe the performance of the model. However, in our case, we are interested in presenting an individualized survival probability curve for each recipient. As a first step toward this goal, we have to evaluate the precision of our predicted probabilities, which we depict in Fig. 5. To ensure that we have a

Table 3  
The best average holdout performance and the corresponding 95% confidence interval among all scenarios for each algorithm, for the 1-year prediction time-frame.

<table><tr><td>Alg.</td><td>Num. Imp.</td><td>Cat. Imp.</td><td>Encoding</td><td>Feature Selection</td><td>Sub-sampling</td><td>G-Mean</td><td>AUC</td><td>Spec.</td><td>Sens.</td><td>Acc.</td></tr><tr><td>LR</td><td>Median</td><td>Unknown</td><td>One-Hot</td><td>LASSO</td><td>UP</td><td>0.610(0.599, 0.621)</td><td>0.655(0.645, 0.664)</td><td>0.593(0.575, 0.611)</td><td>0.629(0.618, 0.639)</td><td>0.624(0.614, 0.633)</td></tr><tr><td>XGB</td><td>Median</td><td>Drop</td><td>One-Hot</td><td>LASSO</td><td>DOWN</td><td>0.607(0.597, 0.618)</td><td>0.649(0.636, 0.662)</td><td>0.585(0.567, 0.602)</td><td>0.631(0.619, 0.642)</td><td>0.625(0.615, 0.635)</td></tr><tr><td>LDA</td><td>Median</td><td>Unknown</td><td>One-Hot</td><td>LASSO</td><td>UP</td><td>0.606(0.598, 0.615)</td><td>0.648(0.641, 0.656)</td><td>0.593(0.575, 0.610)</td><td>0.621(0.611, 0.631)</td><td>0.617(0.609, 0.625)</td></tr><tr><td>RF</td><td>Median</td><td>Unknown</td><td>One-Hot</td><td>LASSO</td><td>DOWN</td><td>0.606(0.600, 0.613)</td><td>0.649(0.642, 0.657)</td><td>0.598(0.590, 0.607)</td><td>0.614(0.597, 0.631)</td><td>0.612(0.598, 0.626)</td></tr><tr><td>ANN</td><td>Drop</td><td>Unknown</td><td>One-Hot</td><td>LASSO</td><td>UP</td><td>0.587(0.564, 0.609)</td><td>0.616(0.575, 0.656)</td><td>0.619(0.537, 0.700)</td><td>0.562(0.471, 0.653)</td><td>0.569(0.497, 0.642)</td></tr><tr><td>CART</td><td>Median</td><td>Unknown</td><td>Label</td><td>LASSO</td><td>UP</td><td>0.577(0.560, 0.594)</td><td>0.599(0.578, 0.619)</td><td>0.546(0.507, 0.584)</td><td>0.611(0.593, 0.630)</td><td>0.602(0.589, 0.616)</td></tr></table>

![](/api/attachments/YHTAZB7Y/fulltext/images/9a33d9f3a9d549535208f1b59861be5aff9e8737d5026ab8d632039867669656.jpg)  
Fig. 4. ROC plots for our logistic regression's training and hold-out datasets for Years 1 − 9. The light blue and dark blue correspond to the training and hold-out performances, respectively. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

Holdout performance of the UP-LASSO-logistic regression implementation.

<table><tr><td></td><td>Month 1</td><td>Year 1</td><td>Year 2</td><td>Year 3</td><td>Year 4</td><td>Year 5</td><td>Year 6</td><td>Year 7</td><td>Year 8</td><td>Year 9</td><td>Year 10</td></tr><tr><td>AUC</td><td>0.608</td><td>0.581</td><td>0.571</td><td>0.594</td><td>0.619</td><td>0.631</td><td>0.654</td><td>0.671</td><td>0.698</td><td>0.703</td><td>0.702</td></tr><tr><td>Accuracy</td><td>0.547</td><td>0.537</td><td>0.541</td><td>0.558</td><td>0.586</td><td>0.594</td><td>0.615</td><td>0.629</td><td>0.64</td><td>0.634</td><td>0.627</td></tr><tr><td>Sensitivity</td><td>0.542</td><td>0.522</td><td>0.532</td><td>0.548</td><td>0.599</td><td>0.618</td><td>0.659</td><td>0.684</td><td>0.723</td><td>0.743</td><td>0.752</td></tr><tr><td>Specificity</td><td>0.589</td><td>0.590</td><td>0.565</td><td>0.579</td><td>0.562</td><td>0.559</td><td>0.558</td><td>0.569</td><td>0.561</td><td>0.541</td><td>0.533</td></tr><tr><td>G-Mean</td><td>0.565</td><td>0.555</td><td>0.548</td><td>0.564</td><td>0.58</td><td>0.588</td><td>0.607</td><td>0.624</td><td>0.636</td><td>0.634</td><td>0.633</td></tr></table>

![](/api/attachments/YHTAZB7Y/fulltext/images/23f246d3139d55c3c0fd9c3f5c218935f92e827eca4a75314c863e98df2cef7a.jpg)  
Fig. 5. Plots of the observed versus forecast survival probabilities for Years 1 − 9 (before isotonic regression). The light blue line correspond to the baseline case of a perfect match between both probabilities. The dark blue line correspond to the results obtained from our machine learning model. To create each plot, we grouped the recipients in our holdout set based on their forecast probability (in 0.1 increments) and we then calculated the observed average as: (#Survivals for year - from group)/(Total # recipients for year from group). (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

suficiently large sample size for inference, we have only plotted probabilities when the number of observed cases within that probability range was ≥100. The plot shows that our forecast survival probabilities underestimate the observed averages for the first 5 years (based on their respective holdout data sets). For the later years, the predicted probabilities are relatively close to the observed ones. This finding is consistent with the metrics reported in Table 4.

## 5.2. Stage II results: calibrating the stage I survival probabilities

A closer examination of the individualized survival probabilities over time revealed a non-monotonic behavior of the curves (see sample UNOS patients 1, 3, and 4 in Fig. 6). To alleviate this problem, we used isotonic regression in stage II to ensure the monotonicity for each recipient's survival probability curve. Fig. 6 shows the survival prob abilities before and after the calibration with isotonic regression.

![](/api/attachments/YHTAZB7Y/fulltext/images/62029cf3cca689a8f38c60986b1b60add230d4ecb8e202afc10e630fbd423755.jpg)  
Fig. 6. Plots of the forecast probabilities for four sample patients at years 1 − 10 post transplant. The light and dark blue lines show the probabilities before and after the application of isotonic regression, respectively. Note when the dark blue line is not shown, this equates to a perfect overlap with the light blue line. We do not show month 1 here, for aesthetic purposes, since it is on a diferent time scale when compared to the yearly data. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

We evaluate the precision of our calibrated probabilities in Fig. 7. Similar to Fig. 5, this figure shows the observed averages against the forecast survival probability in Year 1, 2…9 after isotonic regression is applied. The overall pattern in each plot is consistent with the corre sponding plot in Fig. 5.

In Table 5, we quantify the diferences in prediction performance after the application of isotonic regression, where the bold font shows that the prediction was greater than or equal to the pre-isotonic regression values. From the table, one can see that the AUC and G − Mean values were bolded for the majority of the time periods (i.e. the results typically improved with the application of isotonic regression to calibrate the survival probabilities). However, and more importantly, the application of isotonic regression leads to results that are consistent with the medical expectation of decreasing survival prob abilities over time, and individualized to each recipient.

## 6. Discussion, contributions and conclusions

## 6.1. Contextualizing the prediction results based on the transplantation literature

Prior to discussing our prediction results, it is important to compare the consistency between our models' important variables and those found in the literature. The majority of the literature, where ML methods were used for predicting transplantation outcomes, examined one [e.g., see 7,14,44–46] or at most three time periods [8,11]. Thus, from our analysis, we can gain additional insights into the contribution of a variable to predicting graft rejection, short-term, medium-term, and long-term survival. This is not possible for studies that have focused on one time-period. Moreover, the study of Dag et al. [8] did not include 1-month acute transplant rejection period and the study of Yoon et al. [11] has only investigated 1-, 3-, and 5- year survival outcomes. To illustrate whether our important predictors have been reported in the previous literature, let us consider Table 6 where we provide a summary of whether the variables selected for all 11 time-periods through our LASSO implementation have been selected in $[ 7 , 8 , 1 4 ]$ . We have selected these three references as a representative sample of the literature since (a) Dag et al. [8] examined three time periods, (b) Dag et al. [7] focused on long-term survival outcomes, and (c) Medved et al. [14] used state-of-the-art deep learning methods for short-term survival predictions.

From Table 6, there are three observations to be made. First, the donor's age and the recipient's medical condition at transplant were the two variables where our model agreed with the three papers. Second, our model was the only methodology, where the body mass index for the recipient was found important. Third, all other variables were also selected by at least one paper. Note that the diferences between the models can be attributed to (a) diferences in data cleaning procedures, (b) utilization of diferent variable selection methodologies, (c) difer ences in sample size of dataset used for training (e.g., other papers might not have used the entire UNOS dataset and/or did not include results up to 2016), and/or (d) correlation among one or more in dependent variables in the UNOS dataset. As we show below, our prediction results are consistent with the literature, and thus, the differences shown in Table 6 may not be significant from a prediction perspective.

![](/api/attachments/YHTAZB7Y/fulltext/images/7e00e31a89c7aa3dd04ee1c179a8f8a60d1b7dc4774ab31b501ac9a6561beac4.jpg)  
Fig. 7. Plots of the observed versus forecast survival probabilities for Years 1 − 9 (after isotonic regression is applied). The light blue line correspond to the baseline case of a perfect match between both probabilities. The dark blue line correspond to the results obtained from our machine learning model. To create each plot, we grouped the recipients in our holdout set based on their forecast probability (in 0.1 increments) and we then calculated the observed average as: (#Survivals for year from group)/(Total # recipients for year from group). (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

Table 5  
Diferences (after isotonic regression – before isotonic regression) in Holdout performance of the UP-LASSO-logistic regression implementation.

<table><tr><td></td><td>Month 1</td><td>Year 1</td><td>Year 2</td><td>Year 3</td><td>Year 4</td><td>Year 5</td><td>Year 6</td><td>Year 7</td><td>Year 8</td><td>Year 9</td><td>Year 10</td></tr><tr><td>Δ AUC</td><td>0.008</td><td>0.017</td><td>0.029</td><td>0.021</td><td>0.011</td><td>0.007</td><td>0.001</td><td>0.001</td><td>0.000</td><td>0.002</td><td>0.001</td></tr><tr><td>Δ Accuracy</td><td>0.125</td><td>0.083</td><td>0.061</td><td>0.042</td><td>0.017</td><td>0.007</td><td>-0.005</td><td>-0.008</td><td>-0.006</td><td>0.001</td><td>0.008</td></tr><tr><td>Δ Sensitivity</td><td>0.150</td><td>0.136</td><td>0.110</td><td>0.083</td><td>0.032</td><td>0.007</td><td>-0.037</td><td>-0.061</td><td>-0.102</td><td>-0.130</td><td>-0.161</td></tr><tr><td>Δ Specificity</td><td>-0.114</td><td>-0.105</td><td>-0.064</td><td>-0.047</td><td>-0.009</td><td>0.008</td><td>0.034</td><td>0.050</td><td>0.087</td><td>0.112</td><td>0.134</td></tr><tr><td>Δ G-Mean</td><td>0.009</td><td>0.010</td><td>0.019</td><td>0.016</td><td>0.010</td><td>0.007</td><td>0.000</td><td>-0.003</td><td>-0.003</td><td>-0.001</td><td>-0.005</td></tr></table>

Table 6  
A comparison of whether variables selected for all of our 11 time periods have been identified as important in previous literature.

<table><tr><td>Important Predictors</td><td>Definition of variable per UNOS&#x27;s data sheet [47]</td><td>[8]</td><td>[7]</td><td>[14]</td></tr><tr><td>AGE DON</td><td>Donor&#x27;s age in years</td><td>√</td><td>√</td><td>√</td></tr><tr><td>BMI CALC</td><td>Calculated body mass index for recipient</td><td>-</td><td>-</td><td>-</td></tr><tr><td>COD CAD DON</td><td>Deceased donor&#x27;s cause of death</td><td>-</td><td>-</td><td>√</td></tr><tr><td>CREAT TRR</td><td>Recipient&#x27;s serum creatinine at transplant</td><td>-</td><td>-</td><td>√</td></tr><tr><td>DIAG</td><td>Recipient&#x27;s primary diagnosis</td><td>√</td><td>√</td><td>-</td></tr><tr><td>FUNC STAT TRR</td><td>Recipient&#x27;s functional status at transplant</td><td>√</td><td>√</td><td>-</td></tr><tr><td>INIT HGT CM CALC</td><td>Calculated candidate height in cm at listing</td><td>-</td><td>-</td><td>√</td></tr><tr><td>ISCHTIME</td><td>Ischemic time in hours</td><td>-</td><td>-</td><td>√</td></tr><tr><td>MED COND TRR</td><td>Recipient&#x27;s medical condition pre-transplant at transplant time</td><td>√</td><td>√</td><td>√</td></tr><tr><td>REGION</td><td>UNOS region where transplanted/listed</td><td>√</td><td>√</td><td>-</td></tr><tr><td>TBILI</td><td>Most recent serum total bilirubin at transplant</td><td>-</td><td>-</td><td>√</td></tr><tr><td>TCR DGN</td><td>Candidate diagnosis at listing</td><td>√</td><td>-</td><td>-</td></tr></table>

If we focus on the prediction results in Stage I, our model is (at least) comparable to the prediction outcomes reported in the literature that utilize the UNOS dataset. For example, for the 1-year survival outcomes, our utilized model results in specificity, sensitivity, AUC and G − Mean values of 0.590, 0.522, 0.581, and 0.555, respectively (as shown in Table 4). Our AUC value, for the full, non-censored data in Fig. 4, of 0.614 is similar to the AUC values reported in Dag et al. [8] (0.624), Yoon et al. [11] (0.641 for their best model), Medved et al. [14] (0.61 for their IMPACT model which was developed using the UNOS dataset), Miller et al. [45] (who reported AUC values of 0.613, 0.59, and 0.663 for three diferent transplantation eras), and Villela et al. [46] (whose auto-ML model had an AUC of 0.66). However, the results in Dag et al. [8] can be considered much worse in practice since their average sensitivity was only 0.128 for their validation data sets, which means that their model was not able to predict deaths for the first year. None of the other cited works reported sensitivity or G − Mean results and thus, it is not clear if their models sufer from such a performance discrepancy as well. To further demonstrate the performance of our model, let us consider the 10-year end-point of our prediction period, our model results in specificity, sensitivity, AUC and G − Mean values of 0.533, 0.752, 0.702, and 0.633, respectively (as shown in Table 4). Our AUC value is better than the 0.631 reported by Yoon et al. [11]. Perhaps more importantly, none of the cited papers presented a detailed description of their data cleaning procedure, which makes reproducing their work dificult in practice. Thus, while our prediction results are comparable to the published literature, we believe they can be more useful in practice since we make our code and analysis publicly available through our R Markdown document.

In the second stage of our application, we constructed a monotonically decreasing survival probability curve for each patient using isotonic regression. Overall, the application of isotonic regression did not afect the overall shape of the curve as evident from Figs. 5 and 7. However, the results are medically compelling due to the non-increasing survival probabilities. Furthermore, the individualized nature of the predictions brings us a step closer to personalized medicine [15].

## 6.2. Contributions to heart transplantation research and practice

In Section 6.1, we have shown that the stage I predictive perfor mance of the proposed framework is in line or better than the results reported in the literature. The proposed framework has several merits as it (a) provides personalized results to a given “match case”, (b) is guaranteed to be monotonic, (c) is explainable due to the use of logistic regression, (d) is easy to implement through the provided code, and (e) is flexible since it can easily incorporate any data preparation, variable selection and ML modeling procedure in Stage I of the framework. Furthermore, as stated in Section 2, by examining the UNOS data we are able to

• develop a flexible framework, which can result in accurate and precise heart transplantation outcome predictions;

provide UNOS with a benchmark to compare the expected outcomes from a match, which can inform the policies and algorithms governing phase II of the transplantation process; and

• inform the protocols prescribed by medical professionals in phases IV and V of the transplantation process based on the estimated survival risk.

The first aim is achieved based on the obtained results from the application of our framework. To accomplish the second and third aims, we have created a web application (app) titled “Heart Transplantation Outcome Predictor (H-TOP)” that allows UNOS and transplant teams to utilize the proposed framework on prospective “match cases”. Our approach can be used on prospective cases since we (i) do not include any variables that UNOS no longer collects, (ii) do not use transplant year as a predictor, and (iii) present a comprehensive approach that can be used for data preparation, which is illustrated by our detailed data cleaning, encoding and imputation procedures.

![](/api/attachments/YHTAZB7Y/fulltext/images/513ee3df3e91433af8a3f1ee5f91853afba0c8d57bfe0dc1549a5fa16b6af8f5.jpg)  
Fig. 8. The workflow of the H-TOP app.

We have created and deployed the app using the R “shiny” package. The app can be accessed at http://dataviz.miamioh.edu/Heart-Transplant/monotonic/. To facilitate using the app, it contains an instructional video showing how one can use the app to make predictions. The app allows users to utilize one of two scenarios for inputting data (a) manual entry, where dropdown menus are provided for categorical variables and text inputs are provided for numeric variables; or (b) a CSV upload, where practitioners should load a CSV file based on a provided template. Once the data is inputted, the app (a) performs basic checks on the quality of the imported data, (b) implements the trained logistic regression model for the 11 time points, (c) calibrates the obtained survival probability curves using isotonic regression, and (d) provides a table and a plot of the calibrated survival probabilities. An overview of the app's workflow is presented in Fig. 8. In our estimation, the app is user-friendly and it requires no machine learning background for usage.

## 6.3. Contributions to the data-driven decision-making and support research communities

While we have applied our framework to the problem of predicting heart transplantation outcomes, our proposed two-stage framework presents a generic and flexible methodology that can be applied to any multi-period prediction application where ML methods are used and monotonic outcomes are required. In Section 1, we have presented several decision-making applications that can benefit from our proposed framework. In the context of ML methodologies, our framework represents an extension to the use of “hybrid” methodologies. Existing “hybrid” methods typically incorporate two or more approaches for the purposes of improving prediction accuracy [e.g., see 48]. However, our proposed framework introduces the idea of using a hybrid approach to constrain the predictions from the initial ML modeling stage, which can influence the development of other “hybrid” approaches where dif ferent criteria for calibration are to be enforced.

## 6.4. Limitations and future research opportunities

The limitations of our study provides opportunities for future research. First, the goal of this study was to present a methodological machine learning based framework that uses isotonic regression to calibrate and guarantee the monotonicity of outcome probabilities over time. While we examined a large number of modeling approaches, we did not attempt to optimize the prediction performance (e.g., through a detailed investigation of parameter tuning or through examining more complex data imputation schemes). We examined these scenarios to show that even with the “best” modeling approach, non-monotone probability curves can be obtained. Future research could optimize the findings of our research to broader decision making domains. Second, we examined a limited number of few machine learning models and their parameterizations in Stage I. Thus, we cannot guarantee that logistic regression will be superior when compared to ensemble or hybrid models that were not considered in our analysis. Future research could investigate the use of methodologies excluded from this study. The selection of LR could have also difered if other data cleaning procedures, time-samples of the UNOS data, and criteria for balancing predictive accuracy and interpretation (which will difer from one application to another) were used. Third, we did not consider how to optimize the calibration of the survival curve obtained from Stage I. We have only considered the use of isotonic regression for obtaining monotonic survival probability curves. Future work can examine the use of other approaches to achieve monotonicity, while having a smoother function (e.g., the use of an exponential curve).

Specific to heart transplantation application, there are some additional issues that need to be emphasized. The secondary and retrospective nature of our analysis from a registry database means that we cannot account for “the quality of the source data, the number of missing data, and the lack of standardization associated with multicenter studies (such as diferent immunosuppressive regimens and different matching criteria)” [14,p. 6]. In addition, we have no control over whether the variables included in our model will continue to be collected in the future. Exclusion of these variables from the UNOS data collection protocol will require future researcher to retrain our models. By sharing our detailed code for data cleaning, we explicitly show how we handled missing data, observations where we identified data quality issues, and how we removed all variables that had an ending data per the time of our data acquisition. While our eforts cannot guarantee suitability for future changes in UNOS's data collection protocol, it allows researchers to easily build on our analysis if needed. The results depicted in Figs. 5 and 7, where our approach consistently underestimates the survival probabilities (when compared to observed rates) for the first four years. There are two important considerations that need to be emphasized (a) it is unclear whether the previous methods in the literature would have similar performance characteristics since this type of analysis has not been done before (only metrics for the dichotomous classification are typically reported); and (b) the utility of our approach in practice is not diminished from this limitation. Specifically, from a practitioner's perspective knowing with a high degree of certainty that the prediction probabilities at 5+ years from transplant is accurate, is suficient to obtain a lower bound on the survival probabilities for the earlier time-periods. That being said, future research should examine how to reduce the bias in the predictions for ≤4 years.

## 6.5. Concluding remarks

In conclusion, through our two-stage machine learning framework, we obtained data-driven and individualized survival probability curves for each transplantation event. This represents a significant contribution when compared to previous literature that: (a) had non-monotonic predictions over time [8,11]; (b) attempted to account for the nonmonotone predictions through features in their machine learning model [12,13], which is an improvement over the methods in (a), however, such an approach does not guarantee monotonicity; and (c) achieved monotonic predictions through the use of a population adjustment approach [e.g., see 14], which can potentially limit the utility of the approach (if personalized predictions are important). By providing our detailed code, we are encouraging future research on improving the predictions obtained from the UNOS heart transplantation dataset. Our detailed code can also facilitate the adoption of our framework in other application domains. Our web-based application (app) can inform the current UNOS organ allocation policies and protocols prescribed to heart transplant recipients. Furthermore, we have encouraged the DSS community to use any/all chunks of code from our app (e.g., it can be used in other applications for educational and/or commercial purposes) by making the app's code in the public domain through a CC0 - “No Rights Reserved" license.

## Supplementay materials

Code and analysis: Our code, analysis and results are detailed in an

R Markdown document, which can be accessed at https://ying-ju. github.io/heart\_transplant.github.io/. Our web app can be found online at http://dataviz.miamioh.edu/Heart-Transplant/monotonic/. Note that both our R Markdown document and app are in the public domain through a CCO - “No Rights Reserved” license.

## Funding

The modeling approach, analysis and computational resources were supported in part by the Ohio Supercomputer Center [PMIU0166] and the National Science Foundation [CMMI-1635927]. Dr. Megahed's work was supported by the Neil R. Anderson Endowed Assistant Professorship at the Farmer School of Business at Miami University. The authors would also like to thank the Department of Statistics at Miami University for hosting our web application.

## Declaration of Competing Interest

None.

## Acknowledgments

The UNOS registry was supported in part by Health Resources and Services Administration contract 234-2005-37011C. The content is the responsibility of the authors alone and does not necessarily reflect the views or policies of the Department of Health and Human Services.

## References

[1] V.L. Miguéis, A. Freitas, P.J. Garcia, A. Silva, Early segmentation of students ac cording to their academic performance: a predictive modelling approach, Decis. Support. Syst. 115 (2018) 36–51.

[2] J. Moeyersoms, D. Martens, Including high-cardinality attributes in predictive models: a case study in churn prediction in the energy sector, Decis. Support. Syst. 72 (2015) 72–81.

[3] D. Olaya, J. Vásquez, S. Maldonado, J. Miranda, W. Verbeke, Uplift Modeling for preventing student dropout in higher education, Decis. Support. Syst. (2020), https://doi.org/10.1016/j.dss.2020.113320 (In Press).

[4] K. Coussement, S. Lessmann, G. Verstraeten, A comparative analysis of data pre paration algorithms for customer churn prediction: a case study in the tele communication industry, Decis, Support, Syst, 95 (2017) 27–36

[5] Z.-H. Hu, Z.-H. Sheng, A decision support system for public logistics information service management and optimization, Decis. Support. Syst. 59 (2014) 219–229.

[6] A. Oztekin, Z.J. Kong, D. Delen, Development of a structural equation modelingbased decision tree methodology for the analysis of lung transplantations, Decis. Support. Syst. 51 (1) (2011) 155–166.

[7] A. Dag, K. Topuz, A. Oztekin, S. Bulur, F.M. Megahed, A probabilistic data-driven framework for scoring the preoperative recipient-donor heart transplant survival, Decis, Support, Syst, 86 (2016) 1–12

[8] A. Dag, A. Oztekin, A. Yucel, S. Bulur, F.M. Megahed, Predicting heart transplan tation outcomes through data analytics. Decis, Support. Syst. 94 (2017) 42–52.

[9] K. Topuz, F.D. Zengul, A. Dag, A. Almehmi, M.B. Yildirim, Predicting graft survival among kidney transplant recipients: a Bayesian decision support model, Decis. Support. Syst, 106 (2018) 97–109.

[10] B. Efron, Logistic regression, survival analysis, and the Kaplan-Meier curve, J. Am. Stat, Assoc 83 (402) (1988) 414–425

[11] J. Yoon, W.R. Zame, A. Banerjee, M. Cadeiras, A.M. Alaa, M. van der Schaar, Personalized survival predictions via trees of predictors: an application to cardiac transplantation. PLoS One 13 (3) (2018) e0194985.. https://doi,org/10.1371 journalpone.0194985

[12] L. Ohno-Machado, M.A. Musen, Sequential versus standard neural networks for pattern recognition: an example using the domain of coronary heart disease, Comput, Biol, Med, 27 (4) (1997) 267–281,

[13] L. Ohno-Machado, M.A. Musen, Modular neural networks for medical prognosis: quantifying the benefits of combining neural networks for survival prediction, Connect. Sci. 9 (1) (1997) 71–86.

[14] D. Medved, M. Ohlsson, P. Höglund, B. Andersson, P. Nugues, J. Nilsson, Improvin prediction of heart transplantation outcome using deep learning techniques. Sci. Rep, 8 (1) (2018) 1–9

[15] L.H. Goetz, N.J. Schork, Personalized medicine: motivation, challenges, and pro gress, Fertil. Steril. 109 (6) (2018) 952–963.

[16] M. Pavlakis, D.W. Hanto, Clinical pathways in transplantation: a review and

examples from Beth Israel Deaconess Medical Center, Clin. Transpl. 26 (3) (2012) 382–386.

[17] R.E. Barlow, H.D. Brunk, The isotonic regression problem and its dual, J. Am. Stat. Assoc. 67 (337) (1972) 140–147.

[18] G. Shmueli, O.R. Koppius, Predictive analytics in information systems research, MIS Q. 35 (3) (2011) 553–572.

[19] R. Agarwal, V. Dhar, Editorial—big data, data science, and analytics: the oppor tunity and challenge for IS research, Inf. Syst. Res. 25 (3) (2014) 443–448.

[20] A. Gelman, E. Loken, The Garden of Forking Paths: Why Multiple Comparisons Can Be a Problem, Even when there Is no “Fishing Expedition” or “P-Hacking” and the Research Hypothesis Was Posited Ahead of Time, Department of Statistics, Columbia University, 2013, https://stat.columbia.edu/gelman/research unpublished/p\_hacking.pdf (Online, last accessed May 26, 2020).

[21] S. Nestorov, B. Jukić, N. Jukić, A. Sharma, S. Rossi, Generating insights through data preparation, visualization, and analysis: framework for combining clustering and data visualization techniques for low-cardinality sequential data, Decis. Support. Syst. 125 (2019) 113119., https://doi.org/10.1016/i.dss.2019.113119

[22] J. Kazmaier, J.H. van Vuuren, A generic framework for sentiment analysis: leveraging opinion-bearing data to inform decision making, Decis. Support. Syst. (2020), https://doi.org/10.1016/j.dss.2020.113304 In Press

[23] G. James, D. Witten, T. Hastie, R. Tibshirani, An Introduction to Statistical Learning, Springer, 2013 ISBN 978-1-4614-7137-0.

[24] J.C. Platt, Probabilistic outputs for support vector machines and comparisons to regularized likelihood methods, in: A.J. Smola, P.J. Bartlett, B. SchÃlkopf, D. Schuurmans (Eds.), Advances in Large Margin Classifiers, Chap. 5, MIT Press, 2000, pp. 61–74.

[25] M.J. Best, N. Chakravarti, Active set algorithms for isotonic regression; a unifying framework. Math. Program. 47 (1990) 425–439.

[26] G. Savarese, L.H. Lund, Global public health burden of heart failure, Cardiac Fail. Rev. 3 (1) (2017) 7–11.

[27] E.J. Benjamin, P. Muntner, A. Alonso, M.S. Bittencourt, C.W. Callaway, et al., Heart disease and stroke statistics-2019 update a report from the American Heart Association. Circulation 139 (10) (2019) e56–e528

[28] National Heart, Lung, and Blood Institute (NHLBI), Heart Failure (Online, last ac cessed May 31, 2020),, 2018. https://www.nhlbi.nih.gov/health-topics/heart failure.

[29] C. Allemani, T. Matsuda, V. Di Carlo. R. Harewood. M. Matz, et al., Global surveillance of trends in cancer survival 2000–14 (CONCORD-3): analysis of individual records for 37 513 025 patients diagnosed with one of 18 cancers from 322 po pulation-based registries in 71 countries. Lancet 391 (10125) (2018) 1023–1075.

[30] United Network for Organ Sharing, Transplant Trends – UNOS (Online, last accessed May 31. 2020).. 2020. https://unos.org/data/transplant-trends/.

[31] United Network for Organ Sharing, National Data - UNOS (Online, last accessed May 31. 2020).. 2020. https://optn,transplant.hrsa,gov/data/view-data-reports national-data/

[32] United Network for Organ Sharing, How We Match Organs, UNOS (Online, las accessed May 31, 2020)., 2020. https://unos.org/transplant/how-we-match organs/.

[33] A. Alba, E. Bain, N. Ng, M. Stein, K. Brien, Complications after heart transplantation: hope for the best, but prepare for the worst, Int. J. Transplant. Res. Med. 2 (2) (2016) 022.

[34] The OPTN/UNOS Ad Hoc Geography Committee, OPTN ׀ UNOS Proposed Organ Distribution Frameworks (Online, last accessed May 31, 2020),, 2018. https://unos. org/wp-content/uploads/unos/Proposed-Distribution-Frameworks-v5.pdf.

[35] United Network for Organ Sharing, Questions & Answers About Heart Allocation for Adult Transplant Candidates, UNOS Transplant Living (Online, last accessed May 31, 2020),, 2018. https://transplantliving.org/organ-facts/heart/heart-faq/.

[36] P.J. Thuluvath, H.Y. Yoo, R.E. Thompson, A model to predict survival at one month, one year, and five years after liver transplantation based on pretransplant clinical characteristics, Liver Transpl. 9 (5) (2003) 527–532.

[37] I. Guvon, A. Elisseeff, An introduction to variable and feature selection, J. Mach Learn. Res. 3 (2003) 1157–1182.

[38] M.J. Wilhelm, Long-term outcome following heart transplantation: current perspective, J. Thoracic Dis. 7 (3) (2015) 549–551.

[39] H. He, E.A. Garcia, Learning from imbalanced data, IEEE Trans. Knowl. Data Eng. 21 (9) (2009) 1263–1284.

[40] N.V. Chawla, K.W. Bowyer, L.O. Hall, W.P. Kegelmeyer, SMOTE: synthetic minority over-sampling technique, J. Artif, Intell, Res, 16 (2002) 321–357

[41] G. Menardi, N. Torelli, Training and assessing classification rules with imbalanced data, Data Min. Knowl. Disc. 28 (1) (2014) 92–122.

[42] J. Lasserre, S. Arnold, M. Vingron, P. Reinke, C. Hinrichs, Predicting the outcome of renal transplantation. J. Am. Med. Inform. Assoc. 19 (2) (2012) 255–262.

[43] A. Decruvenaere, P. Decruvenaere, P. Peeters, F. Vermassen, T. Dhaene, et al.. Prediction of delayed graft function after kidney transplantation: comparison between logistic regression and machine learning methods. BMC Med. Inform Decision Making 15 (1) (2015) (Article No, 83)

[44] D. Delen. A. Oztekin. Z.J. Kong, A machine learning-based approach to prognostic analysis of thoracic transplantations, Artif. Intell. Med. 49 (1) (2010) 33–42.

[45] P.E. Miller, S. Pawar, B. Vaccaro, M. McCullough, P. Rao, et al., Predictive abilities of machine learning techniques may be limited by dataset characteristics: insights from the UNOS database, J. Card. Fail, 25 (6) (2019) 479–483.

[46] M. Villela. C. Bravo. M. Shah. S. Patel. U. Jorde, et al., Prediction of outcomes after

39 (4) (2020) S295–S296.

[47] Scientific Registry of Transplant Recipients, SAF Data Dictionary (Online, last accessed May 31, 2020)., 2020. https://www.srtr.org/requesting-srtr-data/saf-datadictionary/.

[48] B. Weng, W. Martinez, Y.-T. Tsai, C. Li, L. Lu, J.R. Barth, F.M. Megahed, Macroeconomic indicators alone can predict the monthly closing price of major US indices: insights from artificial intelligence, time-series analysis and hybrid models, Appl. Soft Comput. 71 (2018) 685–697.

Dr. Hamidreza Ahady Dolatsara is an Assistant Professor in the School of Management at Clark University. He received his Ph.D. and MS degrees in Industrial & System Engineering from Auburn University. In addition, he received an MS in Information Systems Management from Auburn University and an MS in Transportation Engineering from Western Michigan University. His research interests are in healthcare, transporta tion, and finance.

Dr. Ying-Ju (Tessa) Chen is an Assistant Professor in the Department of Mathematics at the University of Dayton. Her expertise is in applied machine learning, high performanc computing, statistical modeling, and survival analysis. Her work has been funded by several foundations and government agencies.

Christy Evans graduated from Auburn University with a bachelor's degree in biomedical sciences and then received her master's degree in Industrial and Systems Engineering with a focus in occupational safety and ergonomics. During graduate school, Christy worked as a graduate research assistant for projects related to burnout in the healthcare field. She is now an incoming medical student.

Dr. Ashish Gupta is an Associate Professor of Analytics in Raymond J. Harbert College of Business and Harbert Advisory Council Faculty Fellow at Auburn University. His research interests are in the areas of artificial intelligence, machine learning, natural language processing, healthcare informatics, IoT, sports analytics, organizational and individual performance. His recent research has appeared in journals such as DSS, EJIS, DSJ, EJOR, JAMIA, etc. He has also published 5 edited research books. Dr. Gupta's research has been supported by various grant agencies such as THEC, DHS, NSF, DOD, etc.

Dr. Fadel M. Megahed is the Neil R. Anderson Endowed Assistant Professor in the Farmer School of Business at Miami University. His current research focuses on creating new tools to store, organize, analyze, model, and visualize the large heterogeneous dat sets associated with modern manufacturing, healthcare and service environments.
