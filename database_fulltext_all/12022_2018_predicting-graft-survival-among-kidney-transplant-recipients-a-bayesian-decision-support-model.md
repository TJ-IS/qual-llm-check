---
otero_id: 12022
otero_key: "6ZUT6ZG8"
title: "Predicting graft survival among kidney transplant recipients: A Bayesian decision support model"
authors: "Kazim Topuz; Ferhat D. Zengul; Ali Dag; Ammar Almehmi; Mehmet Bayram Yildirim"
year: "2018"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2017.12.004"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Predicting graft survival among kidney transplant recipients: A Bayesian decision support model

![](/api/attachments/6ZUT6ZG8/fulltext/images/f8fc5403cec2e2bb8b29656639fa5c51c8e160eed1cd3980162a68c7234ced8b.jpg)

Kazim Topuz <sup>a</sup>, Ferhat D. Zengul <sup>b</sup>, Ali Dag <sup>c</sup>, Ammar Almehmi <sup>d</sup>, Mehmet Bayram Yildirim <sup>e,</sup>⁎

<sup>a</sup> Division of Management Information Systems, Price College of Business, University of Oklahoma, USA

<sup>b</sup> Department of Health Services Administration, University of Alabama at Birmingham, USA

<sup>c</sup> Beacom School of Business, University of South Dakota, USA

<sup>d</sup> Interventional Nephrology Program, University of Alabama at Birmingham, USA

<sup>e</sup> Department of Industrial, Systems and Manufacturing Engineering, Wichita State University, USA

## a r t i c l e i n f o

Article history: Received 22 May 2017 Received in revised form 19 November 2017 Accepted 5 December 2017 Available online 9 December 2017

Keywords: Kidney transplantation Information fusion Elastic net Bayesian belief network Healthcare analytics

## a b s t r a c t

Predicting the graft survival for kidney transplantation is a high stakes undertaking considering the shortage of available organs and the utilization of healthcare resources. The strength of any predictive model depends on the selection of proper predictors. However, despite improvements in acute rejection management and shortterm graft survival, the accurate prediction of kidney transplant outcomes remains suboptimal. Among other approaches, machine-learning techniques have the potential to offer solutions to this prediction problem in kidney transplantation. This study offers a novel methodological solution to this prediction problem by: (a) analyzing the retrospective database including N31,000 U.S. patients; (b) introducing a comprehensive feature selection framework that accounts for medical literature, data analytics methods and elastic net (EN) regression (c) using sensitivity analyses and information fusion to evaluate and combine features from several machine learning approaches (i.e., support vector machines (SVM), artificial neural networks (ANN), and Bootstrap Forest (BF)); (d) constructing several different scenarios by merging different sets of features that are optioned through these fused data mining models and statistical models in addition to expert knowledge; and (e) using best performing sets in Bavesian belief network (BBN) algorithm to identify non-linear relationships and the interactions between explanatory factors and risk levels for kidney graft survival. The results showed that the predictor set obtained through fused data mining model and literature review outperformed the all other alternative predictors sets with the scores of 0.602, 0.684, 0.495 for F-Measure, Average Accuracy, and G-Mean, respectively. Overall, our findings provide novel insights about risk prediction that could potentially help in improving the outcome of kidney transplants. This methodology can also be applied to other similar transplant data sets

© 2017 Elsevier B.V. All rights reserved.

## 1. Introduction

Organ transplantation has the potential to provide a better quality of life for patients and improve their survival [1]. According to the World Health Organization (WHO), of the 119,873 organ transplants worldwide, 67% are kidney transplants, and 59% of those are from deceased donors [2]. Due to the shortage in the supply of kidneys, the waiting time to receive a kidney transplantation in dialysis patients is long and arduous. Also, a substantial number of kidney transplantations fail due to graft rejection, which is attributed primarily to chronic allograft rejection related to an inefficient match between donor and recipient [3]. Failures in the transplant process create a dual effect: first, they result in the loss of a viable organ in a time where organ shortage and lengthy wait-times are already a severe issue. Second, the economic effect of a failed transplant, combined with the patient's return to dialysis or the transplant wait-list results, is a burden on the transplant system, healthcare system, and the patient's quality of life. Therefore, in addressing these failures, improvements in the predictive models of graft survival have a positive compounding effect. Even a slight improvement in predictions has the potential to improve the long-term survival of a kidney graft, thus benefiting the recipient's quality of life and increasing the efficient use of healthcare resources in an industry mired with inefficiency.

Predicting graft survival is vital for efficiency in transplant success since it both enables an increase in the utility of the available pool of organs and benefits the healthcare system's resource utilization. Graft survival refers to the length of time that a transplanted kidney (graft) functions to the degree that the patient does not need dialysis or another transplant [3]. Although considerable research has analyzed the clinical predictors of survival in transplant patients [4–9], few studies have attempted to use machine-learning approaches in the kidney transplant population to predict outcomes [6,8,9]. Recent studies have shown that machine-learning models perform reasonably well in predicting graft survival and identifying contributing factors that are not part of current domain knowledge [6]. However, few studies have thoroughly examined the conditional relations among significant predictors or have identified the patient-specific risk category of kidney transplantation [9,10].

In machine-learning methods, probabilistic graphical models (PGMs) play a major role in modeling the complex nonlinear relations among different variables and reasoning under uncertainty [11]. Bayesian belief networks (BBNs) have become popular among PGMs because they can handle previously unknown but potentially useful information embedded in networks. Few studies have developed BBN models in organ transplantation using various survival time frames: kidney (1–3 years) [9] and liver (90 days) [5]. However, current BBN studies of the renal transplantation population have used either relatively smaller and older data sets (i.e., Li et al. [10]), or evaluated kidney transplantation outcomes using a single-center database (i.e., Brown et al. [9]). The ever-increasing amount of data and the continuous addition of new potential predictors into existing data sets demand the use of better, more comprehensive methodologies in extracting useful knowledge from the data. Increased data and predictors require better feature-selection techniques and methodologies that can incorporate existing domain knowledge into new data sets. Leveraging the massive amounts of data collected on patients can lead to better prediction models, which will enable data-driven decision support tools for decision makers and domain experts, augment their knowledge to create better outcomes for patients, and increase efficiency for resource usage in the healthcare industry.

To this effect, the primary goal of this study is to create a comprehensive methodology that combines exhaustive variable selection with machine learning techniques to enable better predictive abilities and identification of important factors that contribute to the risk of graft failure and the probabilistic dependencies among them. To achieve this goal, we apply a novel, comprehensive methodology on kidney graft survival data to predict graft survival and identify contributing factors and patient-specific risk. We have used statistical approaches, such as elastic nets (ENs) combined with machine-learning approaches such as artificial neural networks (ANNs), bootstrap forest (BF), and support vector machines (SVMs) to select essential predictors in the data. These predictors are used to construct a Bayesian belief network for multinomial prediction. The findings from the BBN model are then used to extract hidden conditional dependencies among the different variables.

This study contributes to the graft survival prediction literature by doing the following: (a) developing a comprehensive variable selection framework and creating a multiclass prediction model for accurate prediction, (b) providing insights into important factors leading to graft failure, (c) identifying interactions between explanatory/preoperative factors and risk levels, and (d) performing a patient-specific risk analysis.

We have organized our work in this paper as follows: In Section 2, we provide an overview of existing literature on the topic of graft survival risk prediction with a cursory focus on kidney transplantation in order to provide the reader with a basis with which to compare our proposed methodology; in Section 3, we discuss the methods and analytic framework used in this study; in Section 4, we provide the results of our study; and finally, in Section 5, we discuss the results, limitations, and implications for decision makers, as well as provide some suggestions for future research.

## 2. Background

The ability to predict the post-transplant graft survival after a transplant is one of the key factors in the donor-recipient matching procedure. This matching is critical because the supply of donor organs is limited. An extensive body of research has used data-driven methods to predict post-transplantation graft survival [6,9,12]. These methods can be classified as follows: (a) simulation and operations research, (b) conventional statistics, and (c) data analytic approaches.

Simulation-based organ transplantation studies have a long history [13]. Ruth et al. [14] designed a discrete simulation model to evaluate the impact of the availability of deceased kidney donors on posttransplantation graft survival using state-level data in Michigan [14]. Both blood type and tissue compatibility were included in the matching process. Later studies proposed simulation models for different organs: liver [15], heart-lung [16], and kidney-pancreas [17]. In order to improve the organ transplant matching algorithms, several operations management and research studies have utilized various optimization models and Markov decision models [18–21]. However, the major drawback of these investigations was limiting the matching process to a small number of variables, such as the functional status of the recipient and some donor-recipient characteristics (e.g., blood type).

Conventional statistical studies, including Kaplan-Meier estimates and Cox proportional hazards models, have been used extensively in the medical literature of organ transplantation [4,22–24]. In fact, beginning in 1987, Rana et al. [24] used the Kaplan-Meier survival function to provide an overview of organ (including kidney) transplantation survival. Several other studies have analyzed the effect of patient characteristics (age, sex, and race) [23] and preoperative transplant factors (human leukocyte antigen matching, donor type, cold ischemia time acute rejection, functional status of a graft after transplant) [22,25] on graft outcomes by using the Kaplan-Meier survival function. However, similar to previous analyses, these studies were limited by utilizing a small number of candidate predictors. Accordingly, there is a need to use larger data sets that include a greater number of variables to unmask potential hidden patterns among the different variables, which could affect the clinical outcomes of a kidney transplant. As such, the present study sought to utilize data analytic approaches using scores of candidate predictors to examine the conditional dependency among a large set of variables. While this research uses a kidney transplant graft survival data set, studies of other organ transplants are also highlighted in this literature review, because the methodology proposed in this study is applicable to any transplant data set, and as such, a comparison to current works in this domain is provided for the reader's benefit.

Data mining-based techniques (DTs) can be classified into two groups: one focusing only on accurately predicting the posttransplantation graft survival by identifying the most signi cant predictors [4,25,26], and the other concentrating on extracting the conditional relations among the significant predictors and then identifying the patient-specific category of survival. As an example of the first group of studies, Kusiak et al. [26] compared the effectiveness of two DTs—decision trees and rough sets (RSs)—in predicting the survival of 188 kidney dialysis patients. Although the results of both methods were accurate, it is not clear whether this approach applies to a larger data set. In another study, DTs were also used to predict the prognosis of acute liver failure to enhance the inclusion criteria for liver transplants [27]. To broaden the prediction variables, Akl et al. [8] used demographic, clinical, and pharmaceutical data to compare the performance of an ANN and a statistically derived nomogram in predicting the five-year graft survival after a kidney transplant. They found that the ANN model outperformed the statistically derived nomo gram on an external validation data set. In another study, Lin et al. [25] determined the effect of various predictors on the one- to seven-year kidney survival rate using logistic regression, the Cox proportional hazard model, and multiple-output ANNs. Dag, Oztekin, Yucel, Bulur and Megahed [28] used four classification algorithms (decision trees, ANNs, SVMs and logistic regression) to classify graft survival for heart patients at one, five, and nine years. They used data-balancing algorithms (SMOTE and RUS) to tackle the imbalanced nature of the data. Their study showed that logistic regression coupled with SMOTE gave the best outcome prediction on test data, with area under the curve (AUC) values of 0.624, 0.676, and 0.838 for one-, five-, and nine-year survival, respectively. Oztekin, Kong and Delen [29] used a structural equation modeling-based decision tree methodology to predict the performance of lung transplants. The R<sup>2</sup> value for their model was 0.68, and their method provided “if-then” rules for interpretability of the results. Delen, Oztekin and Tomak [30] used a feature-rich, nationwide database with four machine learning techniques, and they performed sensitivity analysis (SA) on the best-performing model to obtain important prognostic factors. Support vector machines had the best prediction results in their study, with an 87.74% accuracy rate. Taken together, it seems that the common theme among these studies is their ability to successfully predict an outcome using a set of potential explanatory factors.

The second group of studies concentrates on exploring the probabilistic dependencies among different predictors in order to understand the complex structure of the prediction model. In this group, the few studies that do exist [5,9] mainly employ BBNs to design probabilistic/ causal reasoning. The rationale for using BBNs is their ability to predict outcomes and also assist in learning the complex interactions among variables [31]. For instance, Brown et al. [9] proposed an inference diagram using 48 clinical variables and employed a BBN on a sample of 7348 kidney transplant recipients' data, with the intention of predicting the kidney graft survival at one- and three-year periods. In their model, they used a receiver operator characteristic (ROC) curve as a graphical plot of the performance of a binary classifier. Prediction results included the following: sensitivity scores of 24% and 31%, specificity values of 80% and 80%, and areas under the ROC curve of 0.59 and 0.60, for the one- and three-year periods, respectively. In a similar study, Hoot and Aronsky [5] predicted a 90-day liver graft survival by employing a BBN that included 29 variables on a sample of 12,239 liver-transplant recipients. The AUC was 0.681, and the sensitivity and specificity were 30% and 91%, respectively. It is worth noting that the selected variables of the BBN model in these studies were determined mainly by the knowledge of domain experts or obtained from the existing literature.

The purpose of this study is to create a multinomial classification system that can categorize kidney graft survival into three-classes. As evident from the above exploration of currently available literature, most studies have focused on binomial classi cation models, which can limit the actionable information that researchers can extract from the data. Additionally, exploration of the critical factors and their interactions is also limited with a binomial system because the differential focus of the study is on two classes. Our study aims to create a multinomial prediction and exploration framework that can yield additional information by considering three risk classes, which cover graft survival between 0 and 3, 3–7, and 7+ years. Additionally, previous studies either focused on predicting outcomes or exploring dependencies among predictors identified from the existing literature. In our study, we not only combine these two with a comprehensive feature selection methodology, but also provide a patient-specific risk analysis.

Constructing a BBN model using clinical data can be challenging because of noise and irrelevant variables that can cause unnecessary model complexity [32]. Therefore, it is necessary to apply featureselection procedure that captures important features and simultaneously eliminates the trivial ones [33]. Our framework uses multiple sets of variables identified in the existing literature as well, as through the exhaustive application of machine learning algorithms, statistical methods, and domain knowledge. Maximal information is extracted from these sets by recursively combining the sets in a BBN to obtain the best possible predictive power from the model. This novel methodology allows for a very comprehensive exploration of the available features. To accomplish this goal, we undertook the following steps in our study: (a) performed data pre-processing; (b) utilized a comprehensive feature selection process using different resources including medical expert knowledge, conventional statistics, and data mining models with information fusion from a large pool of variables; (c) developed a multiclass survival risk response variable; (e) explored the interactions among explanatory/preoperative factors; and finally (d) constructed a patient's specific risk of graft survival.

## 3. Proposed methodology

In this study, a three-step kidney Bayesian risk model (KBRM) is proposed with a response variable that has three classes (high, medium, and low). Fig. 1 summarizes the methodology that was utilized in this study.

In step 1, the United Network for Organ Sharing (UNOS) data set was preprocessed to eliminate unnecessary, noisy observations and clinically meaningless variables. In step 2, multiple sets of predictors were developed by using three different approaches such as: (a) a comprehensive medical literature review, (b) a combination of data analytic methods, and (c) elastic net. In step 3, a probabilistic graphical model, tree-augmented naive Bayes (TAN), was designed to structure the BBN inference diagram. After examining the performance of these methods, the best-performing candidate set and model was selected for the KBRM (Fig. 1).

## 3.1. Data preparation

The data set used in this study was provided by the United Network for Organ Sharing, a private non-profit organization that incorporates organ procurement professionals, transplants, and volunteers under contract with the federal government [32]. The UNOS data set included information on all kidney waiting-list registrations and transplants that had been recorded in the U.S and reported between June 30, 2004, and March 31, 2015. We opted to choose June 30, 2004, as a starting date, given that the UNOS expanded the collected variables after that time. This data set included information about both deceased and living donor transplants, without disclosing patient or transplant center identifiers. Also, UNOS data contained information on the corresponding kidney transplant such as demographic factors, medical history, funding information, medical conditions during the transplant, and some postoperative factors for both donors and recipients, as well as other factors such as distance from the hospital, graft-failure date, transplant date, dialysis information, etc.

We followed several steps during data preparation: (a) data were filtered by using the variable “organ type transplanted” to eliminate those patients who underwent other types of transplant; (b) deceased donor transplant data was filtered by using the donor type variable; and (c) a nominal risk group variable, or risk level including high-, medium-, and low-risk group categories was calculated. In order to show the risk level of the transplant, we used two variables in the UNOS data set: (a) graft status, which is a binary response variable denoting if the graft has failed or succeeded at the last follow-up time; and (b) graft time, which is a continuous variable referring to the timeframe from the day of transplant to the recipient's death/last follow-up time, in days. These risk levels were grouped into three categories based on the medical literature [34–39] and calculated as follows:

• Transplants with graft status = failed: grouped into three categories with the graft time response variables as follows:

○ Risk group = high risk, if graft time ≤ 1095 days (3 years).

○ Risk group = medium risk, if 1095 b graft time ≤ 2555 days (3–7 years).

○ Risk group = low risk, if graft time N 2555 days (N7 years).

• Transplants with graft status = not failed: grouped into two categories with the graft time response variables as follows:

○ Risk group = low risk, if graft time N 2555 days (N7 years).

○ Discard, if graft time ≤ 2555 days (7 years), because not enough information was available to define the risk group.

The main reason for creating a categorical variable with low-, medium-, and high-risk levels was to create a comprehensive benchmark for the existing binary outcome (graft survival or not) variables in the literature. These binary outcome variables used varying timeperiod considerations (short-term versus long-term) to estimate the graft survival. Both short- and long-term survivals were estimated by using the organ survival at certain cutoff points (i.e., 1, 3, 7, and 9 years) in which a binary (survive or not) response variable was used. However, it is well known that using binary (short- versus longterm) variables provide limited information about the matching quality. For instance, in a short-term survival study that predicts more than oneyear survival, those patients who live 366 days (1 year plus 1 day) or 3650 days (10 years) fall into the same survival category. Alternatively, a long-term study that evaluates the survival at 7 years (2555 days) tends to categorize the patients who live 2554 days in the notsurvived category.

![](/api/attachments/6ZUT6ZG8/fulltext/images/871a7ef6e110094074d8eac4f296fbe241a97f112c147209cf7435f6f60c51cf.jpg)  
Fig. 1. Overview of methodology.

After developing the risk group variables, those variables that did not contribute to the decision-making process were eliminated, including identification type variables (e.g., donor ID, transplant ID), and invariant variables (e.g., organ listed for, recipient transplant data reported). Records that contained erroneous values and outliers (e.g., negative values for days, BMI N 100) were eliminated. Last, variables that had N50% missing observations and were deemed insignificant by clinical experts were excluded from this study. The final data set contained 31,207 transplants.

## 3.2. Feature selection

Three different sets of variables were generated from the preoperative factors. In the following sub-sections, we discuss the selection process used to generate the final set of variables.

## 3.2.1. Features extracted from medical literature

This set of variables included studies of the organ transplantation survival analysis that were used in the medical literature. The common denominator among these studies was their reliance on clinical expertise to determine survival predictors. Reviewing the medical literature revealed 49 variables as potential predictors of the survival of kidney transplant recipients, which are listed in Appendix 1.

3.2.2. Features extracted from data analytic methods—sensitivity analyses and information fusion

In this set of data, cross-validated data sets were used in various data analytic methods, and significant predictors were sorted via sensitivity analysis (see Fig. 1) [40]. In the final step, the information fusion technique was utilized to determine the final set of variables. Brief descriptions of the data analytic methods performed (SVM, ANN, and BF), SA, and information fusion are provided in the next subsections.

3.2.2.1. Support vector machine. SVMs can handle linearly and nonlinearly separable data sets and can provide powerful classification results [41,42]. For nonlinear cases, the data is typically mapped into a higher-dimensional space so that the new data set in the higher dimension becomes linearly separable [43]. This mapping procedure increases the computational complexity, especially with larger data sets. This problem can be overcome efficiently by using one of several kernel functions, as shown in the work of Han and Kamber [42] and Burges [42,43]. In our study, the SVM was the first data analytic method used to identify the potential predictors of survival. This process was started by introducing SVMs to classify the binary response variables and then was extended to multiclass classification by combining several binary classifiers for each class [44].

3.2.2.2. Artificial neural network. ANNs were originally developed to understand how the brain operates [45]. A generic ANN is a computational system that consists of “a highly interconnected set of processing elements,” called neurons, which process information as a response to external stimuli. An artificial neuron is a simplistic representation that emulates the signal integration and threshold firing behavior of biological neurons using mathematical equations [46]. The information flow between artificial neurons, hereafter referred to as neurons, is determined via connections between the peer neurons. More specifically, the flow of information through each neuron occurs in an input-out manner. Some additional details on the mathematical formulation of ANNs used in this paper can be found in the work of Olson and Delen [47]. In our study, the decision to utilize ANNs was based on several reasons: (a) their ability to learn from data, (b) their non-parametric nature, and (c) their capacity to develop generalizations [48]. Additionally, their use also established the necessary comparison points with earlier studies that used ANNs. In this study, we employed a multilayer perceptron neural network (MLP-NN) since it provided us with the best results among other available alternatives, such as radial basis function (RBF).

3.2.2.3. Bootstrap forest. The BF predicts a response value by averaging the predicted response values across many decision trees. Each tree is grown on a bootstrap sample of the training data. A bootstrap sample is a random sample of observations, drawn with replacement. In addition, predictors are sampled at each split in the decision tree. The decision tree is fit using the recursive partitioning methodology. The fitting process for the training set proceeds as follows:

• For each tree, select a bootstrap sample of observations.

• Fit the individual decision tree, using recursive partitioning, as follows:

○ Select a random set of predictors for each split.

○ Continue splitting until a stopping rule that is specified in the Bootstrap Forest specification window is met.

• Repeat steps 1 and 2 until the number of trees specified in the BF specification window is reached or until early stopping occurs.

For more information about bootstrap forests, see Hastie et al. [49].

3.2.2.4. Sensitivity analysis of predictor features. After determining the performance of the different predictive models, the relative importance of each of the independent variables was measured using SA. This phase was indispensable to the analysis for several reasons. First, it uncovers the underlying causal factors for any of the prediction models. This is particularly important for understanding and communicating the results of ANNs [50], which are still considered by many to be black box models [51]. Second, sensitivity analysis provided the framework that helped in capturing the importance of independent variables across different models (see Section 3).

The sensitivity of a speci c predictor variable was calculated by taking the ratio of the error of the model that included this variable to the error of the model when it did not contain this specific variable [52]. The importance of a variable was related to the variance of the predictive error of the classification model in the absence of that specific variable. The same method was followed for all classification models and was used in ranking the relative importance of variables of each classification model according to the sensitivity measure as defined by Saltelli [53]:

$$
S _ {i} = \frac {V _ {i}}{V (y)} = \frac {V (E (y | x _ {i})}{V (y)}\tag{1}
$$

where y is the categorical output variable (graft survival risk levels), V(y) is the unconditional output variance, and E is the expectation operator, which calls for an integral over all predictor variables except $x _ { i } , A$ further integral operator is implied over x by the operator V . The importance of a specific variable is then computed as the normalized sensitivity, as described by Saltelli et al. [54].

3.2.2.5. Information fusion. It is worth mentioning that the prediction models are problem specific, in that no optimum model works for every scenario; therefore, several techniques are available in the prediction literature [55]. A combination of models can be used to improve performance and reduce errors coming from faulty assumptions in a single model [56]. Similarly, several methods can be used to combine different models, where the performance depends on the data set and problem settings. In the present analysis, the predictive models that were developed through SVM, ANN, and BF were combined through information fusion, a technique combining multiple prediction models to minimize the uncertainty and bias, and to maximize the robustness and accuracy of information. We adopted the information fusion technique developed by Delen et al. [57], where the importance of the variables was ordered for feature selection. The expected response (c) for a general prediction model can be given as

$$
\hat {c} = f (v _ {1}, v _ {2}, \dots , v _ {r})\tag{2}
$$

where $\nu _ { 1 } , \nu _ { 2 } , . . . , \nu _ { r }$ are the predictor variables, and f denotes the prediction model, which could be any of the different models (SVM, ANN, or BF, in our case). The fused model is a combination of these models, and is written as

$$
\hat {c} _ {\text { fused }} = \sum_ {i = 1} ^ {r} \beta_ {i} f _ {i} (\mathbf {v}), \text { where } \sum_ {i = 1} ^ {r} \beta_ {i} = 1\tag{3}
$$

where the values of β are the prediction F-measure of each model (SVM, ANN, and BF). Thus, the weight of the model prediction is dependent on the value of its F-measure. If the value is high, then it receives more weight for the predicted variable. The set of variables used in our study is listed in Appendix 1.

## 3.2.3. Features via elastic net

The EN feature selection method uses a convex combination of Lasso and Ridge regression [58]. These two regularization techniques minimize the sum of squared residuals using L1 and L2 norms, respectively, to limit the size of coefficients in the regression model [59]. Lasso regression is used for automatic feature selection and continuous shrinkage for the coefficients of predictors. Ridge regression does not automatically select the features but outperforms Lasso regression when the number of observations is greater than the number of features and high correlations exist between the features.

The EN, proposed by Zou and Hastie [58], automatically selects the features and outperforms the other methods. It can be formulated as

$$
\hat {\beta} = \underset {\beta} {\operatorname{argmin}} \left\{\sum_ {i = 1} ^ {n} \left(y _ {i} - \beta_ {o} - \sum_ {j = 1} ^ {p} \beta_ {j} x _ {i j}\right) ^ {2} + \lambda \sum_ {j = 1} ^ {p} [ \frac {1}{2} (1 - \alpha) \beta_ {j} ^ {2} + \alpha | \beta_ {j} ] \right\}\tag{4}
$$

More information about model parameters is given in the results section.

## 3.3. Bayesian belief network prediction model

It should be noted that the overarching goal of the current study is not only to predict the outcome, but also to discover the conditional dependencies between the predictors (visual network structure) and the outcome by providing the patient-specific risk scores. In such setting, TAN model appears to be the ideal model (to be employed) that can serve the above-mentioned set of goals. Moreover, TAN method has been specifically used for classification purposes in the literature [5,6, 9,11,60–63]. Therefore, in this study, performances of several sets of candidate predictors were compared by employing tree-augmented naive Bayes (TAN). BBNs are powerful tools for representing the graphical dependency structure among the different variables in an explicit and intuitive way. TAN is a directed acyclic graph that represents a probabilistic relationship between a set of variables in which the nodes correspond to variables or predictors, and arcs represent the conditional dependencies between different variables [64,65]. Additionally, BBN is a useful tool to reason under uncertainty and to model complex nonlinear interactions among attributes [11]. In recent years, the use of BBN has become more prevalent in the medical literature, given its ability to handle previously unknown yet potentially useful information related to disease detection, prediction of health outcomes, and determination of optimal treatment alternatives [6,66,67]. Complex probability distributions can be represented in a compact way using the BBN conditional independence formula. Each $x _ { i }$ represents a variable, and $P a _ { x _ { i } }$ is the parent of that variable. The BBN chain rule can be expressed as [11]

$$
P (x _ {1}, \dots , x _ {n}) = \prod_ {i = 1} ^ {n} P \left(x _ {i} \mid P a _ {x _ {i}}\right)\tag{5}
$$

Two methods are available to construct the network: (a) a manual method with the help of an expert, and (b) an analytical method by learning the structure from the data using advanced mathematical methods [11]. Building a manual modest-sized network requires a skilled and knowledgeable engineer spending several hours, since the number of conditional probability estimations of the number of parents in a node is exponential. For instance, a single node with n parents requires a conditional probability table that includes $2 ^ { n + 1 }$ estimated parameters [62]. Also, expert judgment varies widely, and may bring substantial uncertainties and lead to subjective decisions.

The naive Bayes classification is a simple model that assumes conditional independence between all predictor variables with the given class/target to learn the structure [68]. The classification is based on the Bayes rule, where the probability of the class/target value is computed for each given attribute variable, and then the highest prediction is chosen for the structure. The TAN method uses a tree structure and approximates the interactions among predictor variables [63]. In addition, the TAN structure has a class variable with no parents, and each predictor has the class variable as a parent along with, at most, one other attribute. Thus, an arc between the two variables indicates a probabilistic relationship among them. In our current study, the TAN method outperformed the other constraint-based structural learning algorithms such as naive Bayes and Markov blanket (MB). More discussion and details on BBNs, naive Bayes, TAN, and MB can be found in the work of Korb and Nicholson [62].

## 3.4. Performance measures and validation

## 3.4.1. Performance assessment measures for multiclass classification

Several approaches regarding the “true performance” of multiclass response variable models can be found in the literature [55,69]. In order to provide a comprehensive picture of the performance, three comparison categories were adapted: (a) the probability of correctly classified examples (accuracy for each class and average), (b) measures that have the ability to recognize the patient of a certain group (sensitivity, and specificity), and (c) values for evaluating the overall performance (F-measure and G-mean). Most of these metrics were calculated using the confusion matrix. Since our case had a multiclass response variable, the binary confusion matrix was computed for each class (high, medium, and low risk). The variable R is denoted as the response class, where i is equal to high, medium, and low risk in the case, and the number of classes is three. The following were calculated for each class i: true positive (TP ), false negative (FN ), false positive (FP ), and true negative (TN ) [69]. With these values, the aforementioned metrics were calculated as follows:

$$
A c c u r a c y _ {i} = \frac {T P _ {i} + T N _ {i}}{T P _ {i} + T N _ {i} + F P _ {i} + F N _ {i}}
$$

$$
S e n s i t i v i t y _ {i} = \frac {T P _ {i}}{T P _ {i} + F N _ {i}}
$$

$$
\text { Specificity } _ {i} = \frac {T N _ {i}}{T N _ {i} + F P _ {i}}
$$

$$
F \text { measure } _ {i} = \frac {2 \times T P _ {i}}{2 \times T P _ {i} + F P _ {i} + F N _ {i}}
$$

$$
G \text {   mean } _ {i} = \frac {T P _ {i}}{\sqrt {(T P _ {i} + F P _ {i}) (T P _ {i} + F N _ {i})}}
$$

Multiclass performance metrics were a generalization of the metrics. These calculations were based on micro averaging the indices, as detailed in Sokolova and Lapalme [69].

## 3.4.2. K-fold cross validation

In this study, k-fold cross validation was utilized to minimize the bias coming from the random sampling of the data sets [70–72]. In kfold cross validation, a data set is split into k similarly sized and stratified folds, and the machine learning algorithm is trained k times. Each time, one of the folds is held as the test set, and the remaining k – 1 folds are used to train the algorithm. In this manner, each part of the data is used at least once for testing as well as training purposes. This ensures that any sampling biases can be eliminated from the training process. After running the k-fold cross validation process, the performance metrics for each fold can be compared and averaged to obtain an overall biasfree estimate of the performance measures for the learning algorithm. In this study, we have employed five-fold cross validation and the average of the five testing performances was calculated [73].

## 4. Results and discussion

This study included 31,207 kidney transplants performed after June 30, 2004. Originally, there were 450 variables in the UNOS data set, including preoperative, intraoperative, and postoperative variables, as well as the date of the kidney transplant, ID, and some other variables (e.g., donor ID and organ listed). To determine the ideal set of predictors, the following feature selection procedures were utilized: (a) a detailed literature review, where prominent factors were identified; (b) a structured data analytic-based information fusion technique to extract hidden knowledge in the UNOS data set; and (c) the EN regression model. Candidate variable sets were then used in the BBN model.

## 4.1. Feature selection results

After conducting a comprehensive feature selection procedure, a total of 49 variables was chosen from the medical literature: 25 variables from the fused data-mining and 24 variables from EN analysis. There were some overlaps among these different sets of variables. Details of the various variables selected in this study are provided in the following subsections.

## 4.1.1. Medical literature variables

While developing the variable set from the medical literature, we strived to be as inclusive as possible. However, we had to exclude some variables that had a higher percentage of missing data or did not contribute to decision making process, such as recipient acute rejection between transplant and discharge, and recipient dialysis within the first week of transplant. Although these variables were identified as good predictors of graft survival in several studies, their impact on the decision-making processes is limited [8,9]. On the other hand, we included the variables that were not frequently explored in other studies and can be useful in prediction (e.g., recipient functional status and recipient serum creatinine, both at the time of transplantation) [7,26, 74]. A set of 56 variables was extracted from the literature, as shown in Appendix 1.

## 4.1.2. Data analytic models—sensitivity analysis and information fusion variables

SVM and ANN were performed using a five-fold cross-validation. In BF, for an individual tree, the bootstrap sample of observations that is used to fit the tree was drawn with replacement. We specified that 100% of the observations were to be sampled. Since they were drawn with replacement, the expected proportion of unused observations was 1/e, or approximately 36.8%. For each individual tree, these unused observations are referred to as out-of-bag observations. In the final BF model, 100 trees with five repetitions were averaged. For our categorical response, the predicted probability for an observation is the average of its predicted probabilities over the collection of individual trees. The observation is classified into the level for which its predicted probability is the highest.

To evaluate the multiclass response variable (high, medium, and low risk), the F-measure and G-mean were calculated along with the accuracies for each class and the average accuracy. The performance values for each of the five-fold samples in ANN and SVM, and average bootstrap forest values are shown in Table 1, where the best values are underlined.

As shown in Table 1, the bootstrap forest model outperformed the other models. We remind the reader that our main goal in the feature selection step was to identify the important predictors rather than comparing the model performances. The corresponding contribution of the predictors was calculated using sensitivity analysis, as described in Section 2. Since the F-measure is an overall performance matrix in that it includes both sensitivity and specificity in its formulation, it was used to evaluate each model's contribution to the final fused set of predictors. Fig. 2 illustrates the relative contribution of each predictor for different models.

The final fused set of variables (extracted from ANN, SVM, and BF models) was calculated using the information fusion technique, as described in Section 3. The relative contribution of the predictors was ordered after information fusion and selected until the individual contribution was N1%. Fig. 3 illustrates the most significant variables in the fused set. A total of 25 variables was selected through the information fusion technique.

## 4.1.3. Elastic net variables

It is recognized that the selection of alpha depends on the level of multicollinearity in the data set. We adapted a parameter selection procedure from an earlier paper by Topuz et al. [60]. The EN feature selection procedure with searching right alpha value can be summarized as follows:

$$
\begin{array}{l} \text { INITIALIZE: } \\ \hat {\alpha} = 0, \\ \text { ALPHA   SEARCH: } \\ \text { While   } (\hat {\alpha} \leq 1 \text {   do }, \\ \text { For   } r = 1 \text {   to   } K - f o l d, \\ E ^ {(\hat {\alpha}, r)} = \underset {\beta} {\arg \min} f (\beta , \hat {\alpha}, \lambda); \\ \hat {\alpha} = \hat {\alpha} + s t e p s i z e) \end{array}
$$

FEATURE SELECTION: Select variables within one standard deviation of the average cross-validated error (CV-E) for each alpha value, where the parameter value is identified through an alpha search to determine the minimum average CV-E. The final set of features is selected within one standard deviation for employing fewer variables, and thus a more regularized model and better accuracy is achieved, as indicated in the work of Friedman et al. [75]. K-fold cross validation and calculation of the average cross-validated binomial deviance (CV-E) was an integral part of each step. The selected (24) predictors are shown in Appendix 1.

Performance values for data analytic methods.

<table><tr><td rowspan="2">Performance measure</td><td>ANN</td><td>SVM</td><td rowspan="2">BF</td></tr><tr><td colspan="2">Average ± standard deviation</td></tr><tr><td>Accuracy</td><td>0.71 ± 0.009</td><td>0.70 ± 0.004</td><td>0.819</td></tr><tr><td>Accuracy-high</td><td>0.67 ± 0.017</td><td>0.66 ± 0.001</td><td>0.808</td></tr><tr><td>Accuracy-medium</td><td>0.77 ± 0.003</td><td>0.73 ± 0.007</td><td>0.818</td></tr><tr><td>Accuracy-low</td><td>0.69 ± 0.012</td><td>0.70 ± 0.005</td><td>0.831</td></tr><tr><td>Sensitivity</td><td>0.57 ± 0.013</td><td>0.54 ± 0.005</td><td>0.729</td></tr><tr><td>Specificity</td><td>0.78 ± 0.006</td><td>0.77 ± 0.003</td><td>0.853</td></tr><tr><td>F-measure</td><td>0.57 ± 0.013</td><td>0.54 ± 0.005</td><td>0.729</td></tr><tr><td>G-mean</td><td>0.57 ± 0.013</td><td>0.54 ± 0.004</td><td>0.729</td></tr></table>

## 4.2. Creating candidate sets of predictors and BBN model results

After obtaining three sets of important/significant features from three different feature selection mechanisms (i.e., LR, FDM, and EN), the possible combinations of these models were considered. Therefore, four different candidate sets of predictors were constructed by using a simple union operator deployed into the BBN algorithm. These four alternatives ended up being the best alternatives among many (single models, intersections, unions, etc.) that were explored in the preliminary analysis. Table 2 presents the performances obtained through these candidate sets of predictors.

As can be seen in Table 2, the average performance values (of fivefold) of each predictor set were compared by employing a TAN model. As discussed in the earlier sections of this study, the F-measure was considered to be the main evaluation criterion. It should be noted that Set 1, which was simply the union of the features obtained through a literature review and the fused data mining models, outperformed the other alternatives in terms of F-measure. In addition, it was selected to be the best set among four sets, except two measures (i.e., accuracy-medium and sensitivity). Henceforth, we will be focusing on the results through Set 1. In addition, presenting the detailed results of each of the five-folds for each of our eight metrics is necessary in that it provides us with the best fold among five. The rationale behind this is that even though employing the five-fold cross validation approach brings many advantages, such as increasing robustness and decreasing bias, only one of these five models should be used for future prediction cases. The detailed (five-folded) results of Set 1 are presented in Table 3.

One of the goals of this study was to discover the conditional relationships among the predictors in kidney transplant patients. Interrelations between each predictor and the response variable can be highlighted by the BBN. To illustrate these models, we used the first fold to represent the networks, since its F-measure and G-mean were closest to the average value. The final set of predictors (Set 1) was divided into two groups: (a) predictors from the existing literature, i.e., expert knowledge variables; and (b) predictive variables extracted through data analytic models, which appeared in both regression and data-mining methods. Variables in the first group are common for organ transplantation studies.

Fig. 4 displays the constructed BBN model, and the relationships and conditional dependencies among the different predictors. As shown, we removed the edges of the risk level that go to every node in the TAN structure in order to illustrate the interactions clearly. The constructed BBN can be of great benefit to clinical practitioners because it can offer more detailed information using “what-if analysis.” In fact, it is possible to calculate the transplantation-specific risk level probability, which is defined as how likely (posterior probability) the graft would survive, given the values of the other predictors (Fig. 4). When interpreting the BBN model shown in Fig. 4, one should consider the arrows, directions of arrows, interactions, and indirect relationships. For example, the ethnicity category (ETHCAT) and all nodes linked to it are related to low, medium and high risk levels (RSKLVLs). Moreover, while ETHCAT interacts with the UNOS region where it is transplanted (REGION), it also interacts with the donor ethnicity category (ETHCAT\_DON) and the recipient cytomegalovirus (CMV) by using the immunoglobulin M (IGM) test result at the transplant (CMV\_IGM) and kidney pump used (PUMP\_KI) indirectly through the REGION.

## 4.3. Discussion

Different relationships and interactions generated by the BBN model may provide medical practitioners with significant insight into factors that could affect the outcome of kidney transplantations. For example, interactions between the body mass index (BMI\_CALC), the weight of the recipient (WGT\_KG\_CALC), and height of the recipient (HGT\_CM\_CALC) are intuitive, since BMI\_CALC is calculated using the other two metrics.

![](/api/attachments/6ZUT6ZG8/fulltext/images/3fb163219056466d4d5faceb8d4c6e14acd611ea9a38e3fe5b993773094b6e46.jpg)  
Fig. 2. Sensitivity analysis for ML-based feature selection models.

In the BBN model, there are several very interactive predictors that must be discussed in detail. First, the primary diagnosis at the time of listing (DGN\_TCR) has a direct relationship with eight predictors: donor blood type (ABO\_DON), recipient's diabetes at registration (DIAB), number of previous pancreas transplants (NPPAN), recipient treated for rejection within one year (TRTREJ1Y\_KI), human leukocyte antigen HLA mismatch level (HLAMIS), kidney recipient primary diagnosis at transplantation (DIAG\_KI), and the number of previous kidney transplantations (NPKIDs).

Second, the kidney recipient's primary diagnosis at transplantation (DIAG\_KI) has a direct relationship with six predictors: calculated recipient weight (kg) (EGT\_KG\_CALC), number of pre-transplant transfusions (PRE\_TX\_TXFUS), recipient's total serum albumin at registration (TOT\_SERUM\_ALBUM), recipient serum creatinine at time of transplant (CREAT\_TRR), recipient's ethnicity category (ETHCAT), and the primary diagnosis at the time of listing (DGN\_TCR).

Third, the recipient's functional status at registration (FUNC\_STAT\_TCR), defined as the ability to carry out daily activities, has

![](/api/attachments/6ZUT6ZG8/fulltext/images/7a1575204b1b3648f6056ce750cd1cc8167694722eaa1b98f36891d4eb6be62e.jpg)  
Fig. 3. (Fused) importance of union set of predictors based on information fusion model.

Table 2  
Average cross-validated performance values for different candidate sets.

<table><tr><td></td><td>Set 1(LR U FDM)</td><td>Set 2(LR U EN)</td><td>Set 3(EN U FDM)</td><td>Set 4(LR U EN U FDM)</td></tr><tr><td colspan="5">Performance measure</td></tr><tr><td>Accuracy</td><td>0.684</td><td>0.650</td><td>0.682</td><td>0.682</td></tr><tr><td>Accuracy–high</td><td>0.715</td><td>0.628</td><td>0.713</td><td>0.713</td></tr><tr><td>Accuracy–medium</td><td>0.740</td><td>0.753</td><td>0.736</td><td>0.738</td></tr><tr><td>Accuracy–low</td><td>0.592</td><td>0.570</td><td>0.590</td><td>0.591</td></tr><tr><td>Sensitivity</td><td>0.410</td><td>0.443</td><td>0.407</td><td>0.408</td></tr><tr><td>Specificity</td><td>0.836</td><td>0.765</td><td>0.834</td><td>0.834</td></tr><tr><td>F-measure</td><td>0.602</td><td>0.525</td><td>0.599</td><td>0.596</td></tr><tr><td>G-mean</td><td>0.495</td><td>0.482</td><td>0.492</td><td>0.492</td></tr></table>

Table 3  
Performance values for candidate set 1 (LR ∪ FDM) and corresponding five folds.

<table><tr><td></td><td>Average ± standard deviation</td><td>Fold 1</td><td>Fold 2</td><td>Fold 3</td><td>Fold 4</td><td>Fold 5</td></tr><tr><td colspan="7">Performance measure</td></tr><tr><td>Accuracy</td><td>0.68 ± 0.003</td><td>0.684</td><td>0.681</td><td>0.687</td><td>0.687</td><td>0.680</td></tr><tr><td>Accuracy–high</td><td>0.71 ± 0.003</td><td>0.711</td><td>0.718</td><td>0.716</td><td>0.713</td><td>0.711</td></tr><tr><td>Accuracy–medium</td><td>0.74 ± 0.007</td><td>0.745</td><td>0.735</td><td>0.747</td><td>0.752</td><td>0.740</td></tr><tr><td>Accuracy–low</td><td>0.59 ± 0.004</td><td>0.595</td><td>0.589</td><td>0.598</td><td>0.594</td><td>0.590</td></tr><tr><td>Sensitivity</td><td>0.41 ± 0.005</td><td>0.412</td><td>0.408</td><td>0.419</td><td>0.414</td><td>0.408</td></tr><tr><td>Specificity</td><td>0.84 ± 0.003</td><td>0.837</td><td>0.834</td><td>0.839</td><td>0.842</td><td>0.834</td></tr><tr><td>F-measure</td><td>0.60 ± 0.009</td><td>0.601</td><td>0.594</td><td>0.610</td><td>0.612</td><td>0.594</td></tr><tr><td>G-mean</td><td>0.49 ± 0.006</td><td>0.497</td><td>0.492</td><td>0.505</td><td>0.503</td><td>0.492</td></tr></table>

![](/api/attachments/6ZUT6ZG8/fulltext/images/1a06bac1eb63e4b688d69831427c5ea33696bbb7b1e5f0580ec70b51b82ef5ee.jpg)  
Fig. 4. Bayesian risk-level prediction model for fold 4.

a direct relationship to six variables: the primary diagnosis at time of listing (DGN\_TCR), recipient's highest educational level at registration (EDU-CATION), if the recipient works for income at the time of registration (WORK\_INCOME\_TRR), total days on waiting list, including inactive time (DAYSWAIT\_CHRON), deceased donor Epstein-Barr virus by IGG test result (EBV\_IGG\_CAD\_CON), and recipient's functional status at transplant (FUNC\_STAT\_TRR).

Fourth, clinicians can draw useful, practical information from the constructed BBN by using “what-if analysis.” For example, if the total days on the waiting list, including inactive time (DAYSWAIT\_CHRON\_KI), increases from b170 days to N1300 days, then the probability of graft failure for the high-risk category within RSKLV variable increases from 41% to 48%. Furthermore, in the BBN model, one also can observe that the functional status at registration (FUNC\_STAT\_TCR) contributes to the effect of the total days on a waiting list (DAYSWAIT\_CHRON\_KI) has on graft survival. As such, if the FUNC\_STAT\_TCR of the patient is one of the following three categories: (1) “moribund, fatal processes progress,” (2) “very sick, hospitalization necessary: active treatment necessary,” (3) “severely disabled: hospitalization is indicated, death not imminent,” then having shorter waiting days do not have much effect on the risk; on the contrary, it exhibits the RSKLVL as “high” as 80%. However, if the FUNC\_STAT\_TCR of the patient is “fully active, normal,” then the total days on the waiting list (DAYSWAIT\_CHRON\_KI) becomes very important. For instance, when the FUNC\_STAT\_TCR of the patient is “Fully active, normal,” as the total days on the waiting list (DAYSWAIT\_CHRON\_KI) increases from b170 days to N1300 days, the probability of graft failure for the high-risk category within RSKLV variable increases from 30.60% to 53.50%. Our finding of functional status is an important condition that may be useful for clinicians since medical literature also suggests that shorter wait list time [76,77] and better functional [5,9] status leads to improved graft survival. In summary, the BBN models could help the health care providers in examining the interactions among the different variables to develop clinically relevant protocols that could improve clinical outcomes in the transplant population.

## 5. Conclusion, limitations, and future research

“Quality care is the right care, at the right time, every time,” [78] is a well-known adage in the healthcare industry. To facilitate quality care, there is a dire need to create data-driven approaches to augment existing decision-making processes. Large amounts of existing data, which may not have been possible a decade or two ago, can now be capitalized on to create such data-driven methodologies. The current investigation sought to develop such a framework that could enable decision makers to decrease inefficiencies in the organ-matching system by leveraging data and enabling better available organ and resource utilization. The methodology was tested using kidney graft survival data, but the same methodology applies to any other related domains.

To be used in a decision support setting, a predictive model must provide reasonable predictive performance as well as value over and above current decision-making processes. However, the main contribution of our study emerges from the previously underexplored research area on interactions among predictors. Additional interactions between predictors further provide useful knowledge for domain experts and decision makers to consider. The study has also identified a set of predictors significant in the graft-survival prediction yet underexplored in the literature. Domain experts can assess this information, and after careful consideration, a predictive model based on such a methodology can be used to augment domain expert decision-making procedures. Another strength of the present study is the use of additional newer variables that the UNOS team started to collect beginning June 30, 2014, which could improve the prediction process of kidney transplant outcomes.

Our study has some limitations. First, despite our methodological efforts during the data clean-up stage, we know that any retrospective study generated from secondary data sets would only be as reliable as the source material. However, the UNOS data set used in this study is a well-known and frequently used data source by organ transplant researchers. Second, the findings of our study pertaining to predictors and their conditional dependencies should be examined in clinical practice. Medical expertise input cannot be ignored in any medical study, and must be augmented by input from data analytics models. Last, while this study performed and compared BBNs structured by tree-augmented naive Bayes, it should be pointed out that other BBN algorithms could have been utilized here. To address this limitation, we compared TAN with other BBN algorithms such as naive Bayes and Markov blanket. We found that TAN performed better than other constraint-based learning algorithms in all scenarios.

When taken together, the findings of our study can offer useful tools for medical practitioners that they can incorporate into the decision-making process, which potentially could affect the overall survival of kidney transplant recipients.

## Funding

This research did not receive any specific financial assistance from funding agencies in the public, commercial, or not-for-profit sectors.

## Conflict of interest

The authors declare that they have no conflict of interest.

## Appendix 1. Variables/predictors

<table><tr><td>Variable</td><td>Explanation</td><td>Source</td></tr><tr><td> $ABO^a$ </td><td>Recipient blood group at registration</td><td>[9]</td></tr><tr><td> $ABO\_DON^a$ </td><td>Donor blood type</td><td>[9]</td></tr><tr><td> $ACUTE\_REJ\_EPI\_KI^a$ </td><td>Recipient any acute rejection between transplant (TX) and discharge</td><td>[8]</td></tr><tr><td> $AGE^{a,c}$ </td><td>Recipient age (years)</td><td>[7-9]</td></tr><tr><td> $AGE\_DON^{a,b}$ </td><td>Donor age (years)</td><td>[5,7-9]</td></tr><tr><td> $BMI\_CALC^{a,b,c}$ </td><td>Recipient BMI—calculated</td><td>[5,9]</td></tr><tr><td> $BMI\_DON\_CALC^{a,b}$ </td><td>Donor BMI—pre/calculated at donation</td><td>[5,9]</td></tr><tr><td> $BUN\_DON^{a,b}$ </td><td>Deceased donor—terminal blood urea nitrogen</td><td>[7]</td></tr><tr><td> $CARDARREST\_NEURO^{a,b,c}$ </td><td>Deceased donor—cardiac arrest post brain death</td><td>[9]</td></tr><tr><td> $COD\_CAD\_DON^{a,b,c}$ </td><td>Deceased donor—cause of death</td><td>[5,9]</td></tr><tr><td> $COLD\_ISCH\_KI^{a,b}$ </td><td>Kidney cold ischemic time (hours)</td><td>[4,5]</td></tr><tr><td> $CREAT\_DON^{a,b}$ </td><td>Deceased donor—terminal lab creatinine</td><td>[9]</td></tr><tr><td> $CREAT\_TRR^{a,b,c}$ </td><td>Recipient serum creatinine at time of TX</td><td>[5,9]</td></tr><tr><td> $DGN\_TCR^a$ </td><td>Primary diagnosis at time of listing</td><td>[5]</td></tr><tr><td> $DIAB^{a,b,c}$ </td><td>Recipient diabetes @ registration</td><td>[9]</td></tr><tr><td> $DIABETES\_DON^{a,c}$ </td><td>Deceased donor—history of diabetes (Y/N)</td><td>[9]</td></tr><tr><td> $DIAG\_KI^a$ </td><td>Kidney recipient primary diagnosis @ TX</td><td>[5]</td></tr><tr><td> $DIAL\_DUR^{a,b}$ </td><td>Calculated dialysis duration</td><td>[7,74]</td></tr><tr><td> $DIAL\_TRR^a$ </td><td>Recipient pre-transplant dialysis (Y/N)</td><td>[5,9]</td></tr><tr><td> $DRMIS^a$ </td><td>DR locus mismatch level</td><td>[8]</td></tr><tr><td> $END\_CPRA^a$ </td><td>Candidate most recent calculated PRA</td><td>[9]</td></tr><tr><td> $ETHCAT^{a,b,c}$ </td><td>Recipient ethnicity category</td><td>[4,7]</td></tr><tr><td> $ETHCAT\_DON^{a,c}$ </td><td>Donor ethnicity category</td><td>[4,7]</td></tr><tr><td> $FIRST\_WK\_DIAL^a$ </td><td>Recipient dialysis w/in first week of kidney TX</td><td>[4,7,9]</td></tr><tr><td> $FUNC\_STAT\_TCR^{a,b,c}$ </td><td>Recipient functional status at registration</td><td>[5,9]</td></tr><tr><td> $GENDER^a$ </td><td>Recipient gender</td><td>[4,7]</td></tr><tr><td> $GENDER\_DON^{a,b}$ </td><td>Donor gender</td><td>[4,7,9]</td></tr><tr><td> $HGT\_CM\_CALC^{a,b,c}$ </td><td>Calculated recipient height</td><td>[7]</td></tr><tr><td> $HGT\_CM\_DON\_CALC^a$ </td><td>Calculated donor height</td><td>[7]</td></tr><tr><td> $AMIS^b$ </td><td>Locus mismatch level</td><td></td></tr><tr><td> $CMV\_IGM^{b,c}$ </td><td>Recipient—CMV by IGM test result @ TX</td><td></td></tr><tr><td> $DEATH\_CIRCUM\_DON^{b,c}$ </td><td>Deceased donor—circumstance of death</td><td></td></tr><tr><td> $DISTANCE^b$ </td><td>Miles from donor hosp to TX center</td><td></td></tr><tr><td> $EBV\_IGM\_CAD\_CON^{b,c}$ </td><td>Deceased donor Epsten-Barr virus by IGM test result</td><td></td></tr><tr><td> $ECD\_DONOR^b$ </td><td>ECD donor</td><td></td></tr><tr><td> $FUNC\_STAT\_TRR^b$ </td><td>Recipient functional status @ TX</td><td></td></tr><tr><td> $HGT\_CM\_CALC^b$ </td><td>Calculated recipient height (cm)</td><td></td></tr><tr><td> $INIT\_AGE^{b,c}$ </td><td>Candidate age in years at time of listing</td><td></td></tr><tr><td> $INSULIN\_DON^{b,c}$ </td><td>Deceased donor—Was donor given insulin within 24 h pre cross clamp?</td><td></td></tr><tr><td> $KDRI\_RAO^{b,c}$ </td><td>Kidney Donor Risk Index</td><td></td></tr><tr><td> $MALIC^b$ </td><td>Any previous malignancy?</td><td></td></tr><tr><td> $PROTEIN\_URINE^b$ </td><td>Deceased donor protein in urine</td><td></td></tr><tr><td> $SHARE\_TY^b$ </td><td>Allocation type—local/regional/national</td><td></td></tr><tr><td> $TOT\_SERUM\_ALBUM^b$ </td><td>Recipient total serum albumin @ registration</td><td></td></tr><tr><td> $VDRL\_DON^b$ </td><td>Deceased donor—RPR-VDRL result</td><td></td></tr><tr><td> $TRTREJ1Y\_KI^c$ </td><td>Treated for rejection within 1 year</td><td></td></tr><tr><td> $WORK\_INCOME\_TRR^b$ </td><td>Work for income at TX?</td><td></td></tr><tr><td> $HIST\_CIG\_DON^a$ </td><td>Deceased donor—history of cigarettes in past @ &gt;20-pack years</td><td>[9]</td></tr><tr><td> $HIST\_COCAINE\_DON^a$ </td><td>Deceased donor—history of cocaine use in past</td><td>[9]</td></tr><tr><td> $HIST\_DIABETES\_DON^{a,b,c}$ </td><td>Deceased donor—history of diabetes, incl. duration of disease</td><td>[9]</td></tr><tr><td>HIST_HYPERTENS_DONa,b</td><td>Deceased donor-history of hypertension</td><td>[7,9]</td></tr><tr><td>HIST_OTH_DRUG_DONa,b</td><td>Deceased donor-history of other drug use in past</td><td>[9]</td></tr><tr><td>HLAMISa,b,c</td><td>HLA mismatch level</td><td>[4,8]</td></tr><tr><td>KDRI_MEDa,b,c</td><td>Kidney Donor Risk Index median</td><td>[74]</td></tr><tr><td>MED_COND_TRRa,c</td><td>Recipient medical condition pre-transplant</td><td>[5]</td></tr><tr><td>NON_HRT_DONA</td><td>Deceased donor-non-heart beating donor</td><td>[9]</td></tr><tr><td>NPKIDa,b,c</td><td>Number previous TXs-kidney</td><td>[7]</td></tr><tr><td>NPPANa</td><td>Number previous TXs-pancreas</td><td>[7,74]</td></tr><tr><td>NUM_PREV_TXa</td><td>Number of previous TXs</td><td>[7,79]</td></tr><tr><td>ON_DIALYSISa,c</td><td>WL candidate had regularly administered dialysis for ESRD (Y/N)</td><td>[7,74]</td></tr><tr><td>OTH_INF_DONa,b</td><td>Deceased donor infection other source</td><td>[5]</td></tr><tr><td>PERIP_VASCa</td><td>Recipient peripheral vascular disease @ registration</td><td>[9]</td></tr><tr><td>PRE_TX_TXFUSa,c</td><td>Recipient number of pre-TX transfusions</td><td>[8]</td></tr><tr><td>PREV_TXa</td><td>Previous TX involving exact same organ as current TX</td><td>[5]</td></tr><tr><td>PT_DIURETICS_DONa,b</td><td>Deceased donor-diuretics b/n brain death w/in 24 h of procurement</td><td>[8]</td></tr><tr><td>PT_STEROIDS_DONa,b</td><td>Deceased donor-steroids b/n brain death w/in 24 h of procurement</td><td>[8]</td></tr><tr><td>PUMP_KIa,c</td><td>Kidney pump used</td><td>[9]</td></tr><tr><td>REGIONa,c</td><td>UNOS region where transplanted</td><td>[5]</td></tr><tr><td>SERUM_CREATa,b,c</td><td>Recipient creatinine at discharge</td><td>[7,9]</td></tr><tr><td>SGOT_DONa,b</td><td>Deceased donor-terminal SGOT/AST</td><td>[5]</td></tr><tr><td>SGPT_DONa,b,c</td><td>Deceased donor-terminal SGPT/ALT</td><td>[5]</td></tr><tr><td>TBILI_DONa,b</td><td>Deceased donor-terminal total bilirubin</td><td>[5]</td></tr><tr><td>TX_PROCEDUR_TY_KIa,c</td><td>Kidney transplant procedure type</td><td>[7,9]</td></tr><tr><td>VENTILATORa</td><td>Recipient life support type ventilator @ registration</td><td>[5]</td></tr><tr><td>WARM_ISCH_TIME_DONA</td><td>Deceased donor non-heart beating est. warm ischemic time (min)</td><td>[9]</td></tr><tr><td>WGT_KG_CALCa,b,c</td><td>Calculated recipient weight (kg)</td><td>[7]</td></tr><tr><td>WGT_KG_DON_CALCa,b,c</td><td>Calculated donor weight (kg)</td><td>[7]</td></tr><tr><td>CMV_IGGb</td><td>Recipient-CMV by IGG test result @ tx</td><td></td></tr><tr><td>DAYSWAIT_CHRONb,c</td><td>Total days on waiting list including inactive time</td><td></td></tr><tr><td>DEATH_MECH_DONb</td><td>Deceased donor-mechanism of death</td><td></td></tr><tr><td>EBV_IGG_CAD_CONb,c</td><td>Deceased donor Epsten-Barr virus by IGG test result</td><td></td></tr><tr><td>EBV_SEROSTATUSb</td><td>Recipient Epsten-Barr virus status at transplant-adults only</td><td></td></tr><tr><td>EDUCATIONb,c</td><td>Recipient highest educational level @ registration</td><td></td></tr><tr><td>HBSAB_DONb,c</td><td>Deceased donor HBSAB test result</td><td></td></tr><tr><td>HGT_CM_DON_CALCb</td><td>Calculated donor height (cm)</td><td></td></tr><tr><td>INIT_STATb,c</td><td>Initial waiting list status code</td><td></td></tr><tr><td>KDPIb</td><td>Kidney Donor Profile Index (ref. population = 2013)</td><td></td></tr><tr><td>LT_KI_BIOPSYb,c</td><td>Deceased donor-left kidney biopsy at recovery</td><td></td></tr><tr><td>PRI_PAYMENT_TCR_KIb,c</td><td>Recipient-primary projected payment source-KI @ registration</td><td></td></tr><tr><td>RT_KI_BIOPSYb,c</td><td>Deceased donor-right kidney biopsy at recovery</td><td></td></tr><tr><td>TATTOOSb</td><td>Deceased donor-tattoos</td><td></td></tr><tr><td>TXKIDb</td><td>Simultaneous kidney-r, l, e</td><td></td></tr><tr><td>TRTREJ6M_KIc</td><td>Treated for rejection within one year</td><td></td></tr><tr><td>WORK_INCOME_TCRb,c</td><td>Work for income at registration?</td><td></td></tr></table>

<sup>a</sup> Medical literature.

<sup>b</sup> Fused data analytic.

<sup>c</sup> Elastic net variables.

## References

[1] J.M. Grinyó, Why is organ transplantation clinically important? Cold Spring Harb. Perspect, Med. 3 (2013) a014985.

[2] WHO, World Health Organization, Global Observatory on Donation and TransplantationAvailable from httn://www transplant-observatory org (cited 2017 11/6/2017) 2013.

[3] University, of Wisconsin Health, TransplantAvailable from: http:// www.uwhealth.org/transplant/kidney-transplant/10362 (cited 2017 2/27/2017) 2017.

[4] S. Hariharan, C.P. Johnson, B.A. Bresnahan, S.E. Taranto, M.J. McIntosh, D. Stablein, Improved graft survival after renal transplantation in the United States, 1988 to 1996, N. Engl, I. Med, 342 (2000) 605–612.

[5] N. Hoot, D. Aronsky, Using Bayesian networks to predict survival of liver transplant patients, AMIA Annual Symposium Proceedings, American Medical Informatics Association 2005, p. 345.

[6] A. Dag, K. Topuz, A. Oztekin, S. Bulur, F.M. Megahed, A probabilistic data-driven framework for scoring the preoperative recipient-donor heart transplant survival, Decis. Support. Syst. 86 (2016) 1–12.

[7] S. Krikov, A. Khan, B.C. Baird, L.L. Barenbaum, A. Leviatov, J.K. Koford, A.S. Goldfarb-Rumyantzev, Predicting kidney transplant survival using tree-based modeling, ASAIO J. 53 (2007) 592–600

[8] A. Akl, A.M. Ismail, M. Ghoneim, Prediction of graft survival of living-donor kidney transplantation: nomograms or artificial neural networks? Transplantation 86 (2008) 1401–1406.

[9] T.S. Brown, E.A. Elster, K. Stevens, J.C. Graybill, S. Gillern, S. Phinney, M.O. Salifu, R.M. Jindal, Bayesian modeling of pretransplant variables accurately predicts kidney graft survival, Am. J. Nephrol. 36 (2012) 561–569.

[10] J. Li, G. Serpen, S. Selman, M. Franchetti, M. Riesen, C. Schneider, Bayes net classifiers for prediction of renal graft status and survival period, World Acad. Sci. Eng. Technol. 39 (2010).

[11] D. Koller, N. Friedman, Probabilistic Graphical Models: Principles and Techniques, MIT Press, 2009

[12] B. Kaplan, J. Schold, Transplantation: neural networks for predicting graft survival, Nat. Rev. Nephrol. 5 (2009) 190–192

[13] R.W. Klein, R.S. Dittus, S.D. Roberts, J.R. Wilson, Simulation modeling and healthcare decision making, Med. Decis. Mak. 13 (1993) 347–354.

[14] R.I. Ruth, L. Wyszewianski, G. Herline, Kidney transplantation: a simulation model for examining demand and supply, Manag. Sci. 31 (1985) 515–526.

[15] S.M. Shechter, C.L. Bryce, O. Alagoz, J.E. Kreke, J.E. Stahl, A.J. Schaefer, D.C. Angus, M.S. Roberts, A clinically based discrete-event simulation of end-stage liver disease and the organ allocation process, Med. Decis. Mak. 25 (2005) 199–209.

[16] D. Thompson, L. Waisanen, R. Wolfe, R.M. Merion, K. McCullough, A. Rodgers, Simulating the allocation of organs for transplantation, Health Care Manag. Sci. 7 (2004) 331–338.

[17] H.M. Gebel, B.L. Kasiske, S.K. Gustafson, J. Pyke, E. Shteyn, A.K. Israni, R.A. Bray, J.J. Snyder, J.J. Friedewald, D.L. Segev, Allocating deceased donor kidneys to candidates with high panel–reactive antibodies, Clin. J. Am. Soc. Nephrol. (2016)https://doi.org/ 10.2215/CJN.07720715.

[18] O. Alagoz, A.J. Schaefer, M.S. Roberts, Optimizing organ allocation and acceptance, Handbook of Optimization in Medicine, Springer 2009, pp. 1–24.

[19] O. Alagoz, L.M. Maillart, A.J. Schaefer, M.S. Roberts, The optimal timing of livingdonor liver transplantation, Manag. Sci. 50 (2004) 1420–1430.

[20] D. Bertsimas, V.F. Farias, N. Trichakis, Fairness, efficiency, and flexibility in organ allocation for kidney transplantation, Oper. Res. 61 (2013) 73–87.

[21] S.A. Zenios, G.M. Chertow, L.M. Wein, Dynamic allocation of kidneys to candidates on the transplant waiting list, Oper. Res. 48 (2000) 549–569.

[22] F.K. Port, J.L. Bragg-Gresham, R.A. Metzger, D.M. Dykstra, B.W. Gillespie, E.W. Young, F.L. Delmonico, J.J. Wynn, R.M. Merion, R.A. Wolfe, Donor characteristics associated with reduced graft survival: an approach to expanding the pool of kidney donors 1, Transplantation 74 (2002) 1281–1286.

[23] K. Heldal, A. Hartmann, D.C. Grootendorst, D.J. de Jager, T. Leivestad, A. Foss, K. Midtvedt, Benefit of kidney transplantation beyond 70 years of age, Nephrol. Dial. Transplant, 25 (2010) 1680–1687

[24] A. Rana, A. Gruessner, V.G. Agopian, et al., Survival benefit of solid-organ transplant in the united states, JAMA Surg, 150 (2015) 252–259.

[25] R.S. Lin, S.D. Horn, J.F. Hurdle, A.S. Goldfarb-Rumyantzev, Single and multiple timepoint prediction models in kidney transplant outcomes, J. Biomed. Inform. 41 (2008) 944–952.

[26] A. Kusiak, B. Dixon, S. Shah, Predicting survival time for kidney dialysis patients: a data mining approach, Comput. Biol. Med. 35 (2005) 311–327.

[27] N. Nakayama, M. Oketani, Y. Kawamura, M. Inao, S. Nagoshi, K. Fujiwara, H. Tsubouchi, S. Mochida, Algorithm to determine the outcome of patients with acute liver failure: a data-mining analysis using decision trees, J. Gastroenterol. 47 (2012) 664–677.

[28] A. Dag, A. Oztekin, A. Yucel, S. Bulur, F.M. Megahed, Predicting heart transplantation outcomes through data analytics, Decis. Support. Syst. 94 (2017) 42–52.

[29] A. Oztekin, Z.J. Kong, D. Delen, Development of a structural equation modelingbased decision tree methodology for the analysis of lung transplantations, Decis. Support. Syst. 51 (2011) 155–166.

[30] D. Delen, A. Oztekin, L. Tomak, An analytic approach to better understanding and management of coronary surgeries, Decis. Support. Syst. 52 (2012) 698–705.

[31] J. Pearl, Causal inference in statistics: an overview, Statistics Surveys 3 (2009) 96–146.

[32] D. Shih, S. Kim, V.P. Chen, J. Rosenberger, V. Pilla, Efficient computer experimentbased optimization through variable selection, Ann. Oper. Res. 216 (2014) 287–305.

[33] K. Topuz, H. Uner, A. Oztekin, M.B. Yildirim, Predicting pediatric clinic no-shows: a decision analytic framework using elastic net and Bavesian belief network, Ann Oper, Res. (2017).1-21.https://doiorg/10.1007/s10479-017-2489-0

[34] C. Gerstenkorn, S. Balupuri, M.A. Mohamed, D.M. Manas, S. Ali, J. Kirby, D. Talbot, The impact of cytomegalovirus serology for 7-year graft survival in cadaveric kidney transplantation - the Newcastle experience, Transpl. Int. 13 (2000) S372–S374.

[35] D.W. Gjertson, M.J. Cecka, P.I. Terasaki, The relative effects of fk506 and cyclosporine on short- and long-term kidney graft survival, Transplantation 60 (1995) 1384-1388

[36] A. D. LeRoith, I. Vinik, Controversies in Treating Diabetes Clinical and Research Aspects, Humana Press, New Jersey, 2008.

[37] P. Sood, X. Gao, R. Mehta, D. Landsittel, C. Wu, R. Nusrat, C. Puttarajappa, A.D. Tevar, S. Hariharan, Kidney transplant outcomes after primary, repeat and kidney after nonrenal solid organ transplantation: a single-center experience, Transplantat. Direct 2 (2016), e75.

[38] K. Takahashi, K. Saito, S. Takahara, A. Okuyama, K. Tanabe, H. Toma, K. Uchida, A. Hasegawa, N. Yoshimura, Y. Kamiryo, A.B.O.i.K.T.C. Japanese, Excellent long-term outcome of ABO-incompatible living donor kidney transplantation in Japan, Am. J. Transplant. 4 (2004) 1089–1096.

[39] L. Giblin, P. O'Kelly, D. Little, D. Hickey, J. Donohue, J.J. Walshe, S. Spencer, P.J. Conlon, A Comparison of long-term graft survival rates between the first and second donor kidney transplanted—the effect of a longer cold Ischaemic time for the second kidney, Am. J. Transplant. 5 (2005) 1071–1075.

[40] D. Delen, L. Tomak, K. Topuz, E. Eryarsoy, Investigating injury severity risk factors in automobile crashes with predictive analytics and sensitivity analysis methods, J. Transport Health (2017)https://doi.org/10.1016/j.jth.2017.01.009.

[41] A. Mathur, G.M. Foody, Multiclass and binary SVM classification: implications for training and classification users, IEEE Geosci. Remote Sens. Lett. 5 (2008) 241–245.

[42] J. Han, M. Kamber, Data Mining: Concepts and Techniques, 3rd ed. Elsevier, Burlington, MA, 2011.

[43] C.C. Burges, A Tutorial on support vector machines for pattern recognition, Data Min Knowl. Disc, 2 (1998) 121–167

[44] C.-W. Hsu, C.-J. Lin, A comparison of methods for multiclass support vector machines, IEEE Trans. Neural Netw. 13 (2002) 415–425.

[45] M. Sordo, Introduction to neural networks in healthcare, Open Clinical: Knowledge Management for Medical Care, Harvard University, 2002 ([Online], DOI).

[46] M. Sordo, S. Vaidya, L. Jain, Advanced Computational Intelligence Paradigms in Healthcare-3, Springer Science & Business Media, 2008.

[47] D.L. Olson, D. Delen, Advanced data mining techniques, Springer Publishing Company, Incorporated, 2008.

[48] D. Delen, Real-world Data Mining: Applied Business Analytics and Decision Making, Pearson Education LTD, Upper Saddle River, New Jersey, 2015.

[49] T. Hastie, R. Tibshirani, J. Friedman, The Elements of Statistical Learning, Data Mining, Inference and Prediction, Springer, New York, 2009.

[50] G.W. Davis, Sensitivity analysis in neural net solutions, IEEE Trans. Syst. Man Cybern. 19 (1989) 1078–1082.

[51] M. Molaie, R. Falahian, S. Gharibzadeh, S. Jafari, J.C. Sprott, Artificial neural networks: powerful tools for modeling chaotic behavior in the nervous system, Front. Comput. Neurosci, 8 (2014) 40.

[52] J.C. Principe, N.R. Euliano, W.C. Lefebvre, Innovating adaptive and neural systems instruction with interactive electronic books, Proc. IEEE 88 (2000) 81–95.

[53] A. Saltelli, Making best use of model evaluations to compute sensitivity indices Comput. Phys. Commun. 145 (2002) 280–297.

[54] A. Saltelli, S. Tarantola, F. Campolongo, M. Ratto, Sensitivity Analysis in Practice: A Guide to Assessing Scientific Models, John Wiley & Sons, 2004.

[55] E.W. Steyerberg, A.J. Vickers, N.R. Cook, T. Gerds, M. Gonen, N. Obuchowski, M.J. Pencina, M.W. Kattan, Assessing the performance of prediction models: a framework for some traditional and novel measures, Epidimiology 21 (2010) 128.

[56] J.S. Armstrong, Combining forecasts, Principles of Forecasting, Springer 2001, pp. 417-439

[57] D. Delen, R. Sharda, P. Kumar, Movie forecast Guru: a Web-based DSS for Hollywood managers, Decis, Support, Syst, 43 (2007) 1151–1170.

[58] H. Zou, T. Hastie, Regularization and variable selection via the elastic net, J. R. Stat. Soc, Ser, B (Stat Methodol.) 67 (2005) 301–320

[59] R. Tibshirani, Regression shrinkage and selection via the Lasso, J. R. Stat. Soc. Ser. B Methodol. 58 (1996) 267 288.

[60] K. Topuz, H. Uner, A. Oztekin, M.B. Yildirim, Predicting pediatric clinic no-shows: a decision analytic framework using elastic net and Bayesian belief network, Ann. Oper. Res. (2017)https://doi.org/10.1007/s10479-017-2489-0

[61] J. Li, G. Serpen, S. Selman, M. Franchetti, M. Riesen, C. Schneider, Bayes net classifiers for prediction of renal graft status and survival period, Int. J. Med. Health Biomed Bioeng. Pharm. Eng. 4 (2010) 87–94.

[62] K.B. Korb, A.E. Nicholson, Bayesian Artificial Intelligence, CRC Press, 2010.

[63] N. Friedman, D. Geiger, M. Goldszmidt, Bayesian network classi ers, Mach. Learn. 29 (1997) 131–163.

[64] J. Pearl, Bayesian Networks: A Model of Self-activated Memory for Evidential Reasoning(DOI) 1985

[65] J. Pearl, Probabilistic Reasoning in Intelligent Systems, Morgan Kaufmann, 1988.

[66] P.J. Lucas, L.C. van der Gaag, A. Abu-Hanna, Bayesian networks in biomedicine and health-care Artif Intell Med 30 (2004) 201-214

[67] G. Meyfroidt, F. Güiza, J. Ramon, M. Bruynooghe, Machine learning techniques to examine large patient databases, Best Pract. Res. Clin. Anaesthesiol. 23 (2009) 127–143.

[68] P. Domingos, M. Pazzani, Beyond Independence: Conditions for the Optimality of the Simple Bayesian Classifier, Proc. 13th Intl. Conf. Machine Learning, Citeseer, 1996 105.

[69] M. Sokolova, G. Lapalme, A systematic analysis of performance measures for classification tasks Inf Process, Manag, 45 (2009) 427–437.

[70] R. Kohavi, A study of cross-validation and bootstrap for accuracy estimation and model selection JICAL (U S) (1995) 1137–1145

[71] S. Arlot, A. Celisse, A survey of cross-validation procedures for model selection, Statist, Sury, 4 (2010) 40–79

[72] P. Refaeilzadeh, L. Tang, H. Liu, Cross-validation, in: L. Liu, M.T. ÖZsu (Eds.), Encyclopedia of Database Systems, Springer US, Boston, MA 2009, pp. 532–538.

[73] E. Bastı, C. Kuzey, D. Delen, Analyzing initial public offerings' short-term performance using decision trees and SVMs, Decis. Support. Syst. 73 (2015) 15–27.

[74] T. Klair, A. Gregg, J. Phair, L. Kayler, Outcomes of adult dual kidney transplants by KDRI in the United States, Am. J. Transplant. 13 (2013) 2433–2440.

[75] J. Friedman, T. Hastie, R. Tibshirani, Regularization paths for generalized linear models via coordinate descent, J. Stat. Softw. 33 (2010) 1–22

[76] J.R. Scalea, R.N. Barth, R. Munivenkatappa, B. Philosophe, M. Cooper, V. Whitlow, J.C. LaMattina, Shorter waitlist times and improved graft survivals are observed in pa tients who accept hepatitis C virus+ renal allografts, Transplantation 99 (2015) 1192–1196.

[77] K.K. Tennankore, S.J. Kim, H.J. Baer, C.T. Chan, Survival and hospitalization for intensive home hemodialysis compared with kidney transplantation, J. Am. Soc. Nephrol. (2014)https://doi.org/10.1681/ASN.2013111180.

[78] C. Andel, S.L. Davidow, M. Hollander, D.A. Moreno, The economics of health care quality and medical errors, J. Health Care Finance 39 (2012) 39.

[79] OPTN, Organ Procurement and Transplantation Network, A Guide to Calculating and Interpreting the Estimated Post-transplant Survival (EPTS) Score Used in the Kidney Allocation SystemAvailable from https://optn.transplant.hrsa.gov/ ContentDocuments/Guide\_to\_Calculating\_Interpreting\_EPTS.pdf [cited 3/20/2016] Organ Procurement and Transplantation Network, 2014.

![](/api/attachments/6ZUT6ZG8/fulltext/images/f8b526040350b7aef5136089fcb13e2443c843c134c1ae00ffd663572d7d399c.jpg)

Kazim Topuz is a Research Fellow in the Center for Health Systems Innovation at Oklahoma State University. He has received his Ph.D. from Wichita State University in Industrial Engineering. His current research is focused on prediction and survival models in healthcare, and risk analysis in aviation. Most of his work is primarily related to modeling and improving Bayesian Belief Networks. He published several papers in respected journals such as Decision Support Systems, Annals of Operations Research, and Journal of Transportation and Health. He is awarded fellowship from Turkish Republic Ministry of Higher Education and Rutgers University Industrial and Systems Engineering Department in 2009 and 2013, respectively. He is a member of IIE, IN-FORMS, and AMIA.

![](/api/attachments/6ZUT6ZG8/fulltext/images/6a7b6525dcf294f6dfd776d9d6b894a1d1bfe7106ff2d7c3f0a24b0c0fe475cc.jpg)

Ferhat D. Zengul is a full-time Assistant Professor in the Health Care Management Program in the Department of Health Services Administration, School of Health Professions (SHP) at the University of Alabama at Birmingham (UAB) Prior to joining the Health Care Management Program, he worked at UAB Hospital Finance and UABHS Facilities Planning and Capital Projects Of ce. Dr. Zengul's broad research focus is the performance of healthcare organizations with an emphasis on clinical and financial performance. He is par ticularly interested in developing predictive models for the clinical and financial performance of health care organizations. He is currently working on a SQL-based datawarehouse and data-mining infrastructure that is supported by an internal faculty development grant. Recently,

Dr. Zengul's proposal to develop predictive models for liver graft survival by using machine learning approaches was one of only 10 nationwide accepted for the Data Science Rotations for Advancing Discovery (RoAD-Trip) program which is operated by Universit of Southern California and funded by National Institutes of Health's Big Data to Knowledge (BD2K) initiative. Dr. Zengul is interested in continuing his research in predictive analytics with healthcare focus by combining his experience from RoaAD-Trip fellowship and the UAB Clinical and Translational Science 2017 Training Program that he is currently attending.

![](/api/attachments/6ZUT6ZG8/fulltext/images/19c3dabb23c24e0b6fbc203abf87b0dca9d0f3a884befd9eec8b47dfe43b8b00.jpg)

Ali Dag received his Ph.D. from Auburn University in Indus trial and Systems Engineering. He is a full-time Assistant Professor in Beacom School of Business in South Dakota University. His research interests include artificial intelligence, data mining, data visualization, knowledge management and text mining. He is a member of IIE and INFORMS.

![](/api/attachments/6ZUT6ZG8/fulltext/images/b8f04b0bb24d493863809dbee0df187d4a29278b89346e9f2c29c0bc6e6c8cfa.jpg)

Ammar Almehmi is an Associate Professor of Medicine and Radiology at the University of Alabama at Birmingham (UAB) who is board certified by the American Board of Internal Medicine (ABIM) in both Internal Medicine and Nephrology. Further, he is certified in Hemodialysis Vascular Access and Peritoneal Dialysis Catheter management by the American Society of Diagnostic and Interventional Nephrology (ASDIN).During his fellowship at Kansas University, he spent one year as a T32-NIH nephrology research fellow; then he was awarded the prestigious NKF research fellowship grant. Moreover, due to his leadership skills, Dr. Ammar was selected as the Chief Fellow in Nephology. In addition to his doctorate in medicine (MD) from the University of Aleppo, Dr. Ammar Almehmi holds a master'’s degree in public health (MPH) from West Virginia University. Currently, Dr. Almehmi serves as the director of interventional Nephrology program at UAB. He is a member of several medical organizations: ASN, ASDIN, NKF, and ISN. He served on the editorial board of multiple medical journals.

![](/api/attachments/6ZUT6ZG8/fulltext/images/6cd8c871c3235d7a3e233e8705ecbbdeaf99df79325a8cfa796f611206cc48d6.jpg)

Mehmet Bayram Yildirim is a professor in the Department of Industrial, Systems and Manufacturing Engineering at Wichita State University. He received a BS in industrial engineering from Bogazici University. Turkey in 1994: MS degree industrial engineering from Bilkent University, Turkey in 1996; and a PhD in industrial and systems engineering from the University of Florida in 2001. He has research interests in sustainability, energy aware production planning, generation expansion transmission planning, data enabled decision making and asset management
