---
otero_id: 9120
otero_key: "JENTWGMG"
title: "Improving prognosis and reducing decision regret for pancreatic cancer treatment using artificial neural networks"
authors: "Steven Walczak; Vic Velanovich"
year: "2018"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2017.12.007"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

Improving prognosis and reducing decision regret for pancreatic cancer treatment using artificial neural networks

![](/api/attachments/JENTWGMG/fulltext/images/eb1900903526cc751a01e479c42f041c8089d3cf7c5893dfcd800befa837f4ff.jpg)

Steven Walczak, Vic Velanovich

<table><tr><td>PII:</td><td>S0167-9236(17)30236-1</td></tr><tr><td>DOI:</td><td>https://doi.org/10.1016/j.dss.2017.12.007</td></tr><tr><td>Reference:</td><td>DECSUP 12908</td></tr><tr><td>To appear in:</td><td>Decision Support Systems</td></tr><tr><td>Received date:</td><td>17 August 2017</td></tr><tr><td>Revised date:</td><td>12 December 2017</td></tr><tr><td>Accepted date:</td><td>12 December 2017</td></tr></table>

Please cite this article as: Steven Walczak, Vic Velanovich , Improving prognosis and reducing decision regret for pancreatic cancer treatment using artificial neural networks. The address for the corresponding author was captured as affiliation for all authors. Please check if appropriate. Decsup(2017), https://doi.org/10.1016/j.dss.2017.12.007

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Improving Prognosis and Reducing Decision Regret for Pancreatic Cancer Treatment Using Artificial Neural Networks

Steven Walczak <sup>a,1</sup>

Vic Velanovich

<sup>a</sup> University of South Florida, School of Information, 4202 E. Fowler Ave., CIS 1040, Tampa, FL 33620

<sup>b</sup> University of South Florida, Department of Surgery, School of Medicine, Tampa, FL

## Abstract

Cancer is a worldwide health problem with extremely high morbidity and mortality. Pancreatic cancer specifically is the fourth leading cause of death by cancer in the United States and is a leading cause of cancer deaths worldwide. The optimal treatment for pancreatic cancer is resection surgery, but even with surgery many patients suffer high morbidity and mortality, leading to regret in physicians over whether or not the optimal course of treatment with regard to the patient’s quality of life was made. Patients also suffer regret concerning the morbidity associated with treatment. An artificial neural network is developed to predict 7-month survival of pancreatic cancer patients that achieves over a 91% sensitivity and an overall accuracy above 70%. The artificial neural network outcome predictions may be used as an additional source of information to assist physicians and patients in selecting the treatment that provides the best quality of life for the patient and reduces treatment decision regret.

Keywords: artificial neural network; cancer; pancreas; regret reduction; survival

## Improving Prognosis and Reducing Decision Regret for Pancreatic Cancer Treatment Using Artificial Neural Networks

## 1. Introduction

Pancreatic cancer is a worldwide chronic health problem. This type of cancer is an illness with very high fatality rates (Fesinmeyer et al., 2005). Patients diagnosed with exocrine pancreatic cancer have their life expectancy measured in months (Li et al., 2004). Pancreatic cancers are the fourth leading cause of cancer deaths in men and the third leading cause of cancer deaths in women in the United States and the European Union, and is a leading cause of cancer deaths worldwide (Gillen et al., 2010; Malvezzi et al., 2013; Rahib et al., 2014). Pancreatic cancers are predicted to become the second leading overall cause of cancer deaths by the year 2030 (Rahib et al., 2014).

Pancreatic cancer also has extremely high morbidity rates (Fesinmeyer et al., 2005). Prior to diagnosis, patients may suffer significant morbidity including: pain, weakness, nausea, vomiting, and weight loss (Freelove & Walling, 2006).

Various treatment options exist for pancreatic cancer patients including: observe/do nothing, adjuvant therapy (chemotherapy and/or radiation), surgery to resect the pancreas, and combined adjuvant therapies with surgery (Dimou et al., 2016). Resection surgery is the best treatment option for pancreatic cancer patients and offers the best prognosis for long term survival (Baxter, Whitson, & Tuttle , 2007; Wagner et al., 2004). Without resection, prior research has shown a median survival of 3.5 months and with resection the median survival increases to 13.3 to 17 months (Cress et al., 2006; Kuhlmann et al., 2004). Even with resection, only 8% of pancreatic cancer patients survive more than five years (Kuhlmann et al., 2004). However, resection surgery is not always a viable option as the cancer may have already metastasized or the patient may simply be too ill to be eligible for surgery (Fesinmeyer et al., 2005).

The decision process to have a resection surgery is complicated by a number of factors that will impact the quality of life of the patient including high morbidity rates and a chance that death may still occur quickly. Perioperative morbidity rates as high as 50% and perioperative mortality rates as high as 15% have been reported (Okano et al., 2015; Vollmer et al., 2012). Additional research has shown that pancreatic cancer surgery post-operative mortality rates are still high up to 3 months from the time of surgery (Swanson et al., 2014). With all of these risk factors, physicians as well as patients may have a difficult time determining the optimal treatment plan for individual patients and may suffer regret from their decision. Recent focus on evidence-based medicine implies that pancreatic cancer data quantities will continue to increase. Utilizing this data effectively through the use of data mining techniques like artificial neural networks (ANNs), can lead to more accurate diagnosis and prediction outcomes which in turn will promote better understanding of these complex procedures and improve patient outcomes (Delen, Oztekin, & Tomak, 2012).

Two types of regret are possible for pancreatic cancer prognosis: regret of omission and regret of commission (Hernandez et al., 2014). Regret of omission is defined as regret felt when resection is not performed, but when the resection could have improved th e long term survival and quality of life of their patient, while regret of commission is regret felt when a resection surgery is performed, but the patient derived no benefit. Commission regret may be partially caused by the inconvenience and comorbidities associated with cancer surgery (Janssen-Heijnen et al., 2007). Research on regret in decision making is relatively new and additional research is needed to further examine how regret may affect cancer treatment decision making (Connolly & Reb, 2005). Benefit to the patient, to counter regret, is determined if the patient survives for 7 months following surgery, or the decision not to resect, which is twice the median survival without resection and also twice the time for the high post-operative mortality rate reported above. “In light of the high mortality rate in severe acute pancreatitis, a system that accurately predicts risk of death is in great demand” (Bartosch‐Härlid et al., 2008, p. 822).

The objective of the research reported in this paper is to develop an artificial neural network (ANN) system to reduce regret in the decision making process for surgical resection to treat pancreatic cancer. Regret reduction is accomplished when the ANN model predicts the 7-month survival or mortality of pancreatic cancer patients for a specific treatment decision, thus enabling physicians and patients to better

# ACCEPTED MANUSCRIPT

estimate the potential benefit of a treatment decision. Performance of the ANN is evaluated using sensitivity and specificity, where sensitivity is accurately predicting 7-month survival for patients who survive and specificity is accurately predicting mortality for patients who do not survive, for a predetermined treatment method. The goal of the current research, based on surgeon preference, is to achieve a sensitivity of at least 90%. If a sensitivity of 90% is achievable, then a secondary goal is to maximize s well for the primary criteria of having a sensitivity over 90% and is also able to achieve specificity results of over 38%. The overall accuracy of the reported system is almost 72% correct predictions.

## 2. Background

Treatment decisions in oncology directly impact not only the chance for survival, but also the quality of life of patients. Four possible treatment options are available to pancreatic cancer patients: surgery, adjunctive therapy (chemo and/or radiation), combined adjunctive therapy and surgery, or wait and see (Dimou et al., 2016). The patient’s quality of life prior to treatment and the probable impact of the treatment on the survival and consequent quality of life for the patient influence physician’s and patient’s perceptions of the value of treatment. It is important for physicians to try and maintain or improve the quality of life of their patients (Schmoll et al., 2012). Patients often feel that they have no real choice or options other than surgery and that clinical models are used only to determine if they are eligible for surgery, not to determine if surgery is a treatment option (Ziebland, Chapple, & Evans, 2015). Another factor to consider is the potential regret of the physician or patient from making an incorrect treatment decision (Hernandez et al., 2014).

Patient quality of life may be evaluated using the SF-36 quality of life short form assessment (McHorney et al., 1994; Ware, 2000; Ware & Sherbourne, 1992)<sup>i</sup>. SF-36 produces eight group or domain values for: physical functioning (PF), role-physical (RP), role-emotional (RE), bodily pain (BP), vitality (VT), mental health (MH), social functioning (SF), and general health (GH) (Velanovich, 2011). The SF-36 domain values may be used as part of a clinical prediction rule to determine if surgery should even be considered as an option (Tetreault et al., 2015). Prior research has shown that the SF-36 in addition to showing the current quality of life status for a patient, may also be used to predict disease prognosis (Robinson et al., 2008) and also treatment outcomes (Polistina et al., 2010; Velanovich, 2011).

Hernandez et al. (2014) introduced a pancreatic cancer treatment decision model that uses a decision curve based on regret theory (Loomes & Sugden, 1982). Using regret-based decision curve analytics (Tsalatsanis et al., 2010). In the Hernandez et al. (2014) regret-based decision curve model, physicians are queried for their omission and commission risk tolerances and these tolerances are then used in the regret decision tree to minimize expected regret while maximizing the utility of the treatment decision. If treatment outcomes can be predicted prior to the treatment instantiation, this would reduce or eliminate regret, based on the accuracy of the outcome prediction model.

ANNs are widely used as clinical decision support tools in the domain of oncology (Lisboa & Taktak, 2006) and pancreatic diseases (Walczak, Pofahl, & Scorpio, 2003). The other common tool for medical prediction models is logistic regression (Dreiseitl & Ohno-Machado, 2002; Mangiameli, West, & Rampal, 2004). Two aspects of ANN models help to improve medical diagnosis and prognosis: they are nonparametric (Dayhoff & DeLeo, 2001), meaning that few a priori conditions exist which must be satisfied to apply this modeling procedure; and they utilize machine learning so that they may produce the optimal model available from a set of input variables (Dreiseitl & Ohno-Machado, 2002). A total of 47 different applications of ANNs in the domain of pancreatic cancer between 1997 and 2009 are reviewed by Bartosch‐Härlid et al. (2008), who review 11 ANN models for diagnosis and prognosis of pancreatic diseases including cancer, and Bartosch-Härlid and Andersson (2010), who review 36 ANN models that examined identification of comorbidities with pancreatic cancer (specifically insulin resistance and diabetes). Applications of ANNs in medicine have been primarily focused on performing or assisting with disease diagnosis (Amato et al., 2013). This is true regarding general ANN usage as diagnostic decision aids in the sub-domain of pancreatic cancer as shown by the examples given in Table 1.

Development of an ANN outcome prediction model requires identification of independent variables to create the input vector, selection of a training algorithm, and determination of the optimal architecture dependent on the training algorithm selected (Walczak & Cerpa, 1999; Zhang, 2007). As may be seen from Table 1, backpropagation is by far the most frequently used training method for ANNs performing pancreatic diagnostic decision support and this is also true in general for ANN diagnostic applications in the field of medicine (Amato et al., 2013). Gorunescu et al. (2011) compare probabilistic, radial basis find the backpropagation algorithm to produce superior performance over the other two training methods. General details of the ANN model development process are not discussed here and readers desiring more information are directed to any ANN textbook [e.g., (Hagan et al., 2014)], and (Walczak & Cerpa, 1999; Zhang 2007).

Table 1. Recent (10 years) ANN Pancreatic Cancer Diagnostic Systems

<table><tr><td>Reference</td><td>Type of diagnostic aid</td><td>NN Training algorithm</td></tr><tr><td>(Chang &amp; Hsu, 2009)</td><td>direct prediction from patient data</td><td>backpropagation</td></tr><tr><td>(Das et al., 2008)</td><td>image analysis</td><td>backpropagation</td></tr><tr><td>(Gorunescu et al., 2011)</td><td>image analysis</td><td>backpropagation</td></tr><tr><td>(Qiong-ying et al., 2010)</td><td>protein biomarkers</td><td>backpropagation</td></tr><tr><td>(Säftoiu et al., 2008)</td><td rowspan="2">image analysis</td><td>multi-layer perceptron</td></tr><tr><td>(Säftoiu et al., 2012)</td><td>(backpropagation)</td></tr><tr><td>(Yang et al., 2013)</td><td>3 protein serum markers</td><td>unspecified</td></tr><tr><td>(Zhang et al., 2010)</td><td>image analysis</td><td>support vector machine</td></tr><tr><td>(Zhu et al., 2013)</td><td>image analysis</td><td>support vector machine</td></tr></table>

## 3. Method

## 3.1. Population data

All of the cases of confirmed pancreatic cancer patients at a large Midwestern teaching hospital between

# ACCEPTED MANUSCRIPT

2000 and 2010 inclusive make up the population data for training and evaluating the ANN model. A total of 283 confirmed pancreatic cancer cases occurred during the respective time period. Confirmation of the diagnosis of pancreatic cancer is performed by histological evaluation, pathological evaluation of any resected specimens, and by imaging. Patient records with incomplete information are automatically excluded, resulting in a total of 219 cases that had complete information and are used in the study.

ANN data is partitioned into training and test/validation sets and commonly employs n-fold crossvalidation in which the data is divided into n equal sized sets (Dreiseitl & Ohno-Machado, 2002). A 2- fold cross-validation approach is used and accordingly, the 219 records are divided into two distinct sets of 110 and 109 cases each, with data samples chosen randomly to serve as the training set or validation set. The validation set members are never used in training and are only presented to the ANN one time for the validation study. Cross-validation requires all data sets to be used as validation sets. When the validation set is switched with the training set in the 2-fold cross-validation the ANN model’s weights are randomized and then trained anew to enable each case to serve as both a training sample and a validation sample, producing an N of 219 for validation of the ANN model.

The study population demographics for the ANN data are: 55.7% male with a mean age of 64.47 (σ = 12.12). The stage of the cancer ranged from stage 1 to stage 3, with a median stage of 1 and mean stage of 1.50 (σ = 0.71). The proportion of resection versus no resection and relation to 7-month mortality is shown in Table 2. The population treatment results from Table 2 are consistent with prior research that shows resection provides the best chance for survival in cases of pancreatic cancer (Baxter, Whitson, & Tuttle, 2007; Cress et al., 2006; Wagner et al., 2004). The specific treatment plans for these 219 patients resulted in 25.6% receiving no treatment (observation), 17.4% receiving only adjuvant therapies, 36.5% receiving only resection surgery, and 20.5% receiving both adjuvant therapies and resection surgery. Overall survival regardless of treatment is 63% for this specific population.

## 3.2. NN design, experiment 1

The purpose of the first part of the research is to develop and demonstrate the efficacy of an ANN

## ACCEPTED MANUSCRIPT

Table 2. Real World Results for Study Population Based on Treatment Received (N=219)

<table><tr><td></td><td>Survived 7 months</td><td>Died</td></tr><tr><td>No resection</td><td>50</td><td>44</td></tr><tr><td>Resection</td><td>88</td><td>37</td></tr></table>

model to predict the 7-month survival or mortality of pancreatic cancer patients. The input vector, as determined by an expert pancreatic physician, to each ANN survival prediction model consists of age, sex, whether or not a resection was performed (for training data, but for real-world usage of the ANN this would be if a resection is planned), whether or not adjunctive therapy was performed, the current stage of the cancer, the time elapsed since diagnosis of cancer, and the eight SF-36 domain values: PF, RP, RE, BP, VT, MH, SF, and GH. Adjunctive therapies are included because they are a treatment option in lieu of or in addition to resection surgery and have been shown to improve opportunities for resection surgery and outcomes (Gillen et al., 2010), but have also been sho to be risky and may increase morbidity and toxicity (Yeo et al., 1997). The SF-36 domain variables approximate the patient’s preoperative quality of life. It should be remembered that the physician may determine that surgery is not an option based on some or all of these SF-36 domain values.

The Pearson correlation values for the 8 SF-36 domain variables are shown in Table 3. All correlations are below 0.68, which is important because ANN input values should not be highly correlated (Smith, 1993; Walczak & Cerpa, 1999), though the cutoff for determining highly correlated values is left open. For example, a cutoff of 0.54 is used to classify small round blue cell tumors using gene expressions with an ANN (Kahn et al., 2001), and an ANN to classify brain tumors with genetic data uses a cutoff of 0.90 (dos Santos Valente, 2015).

The output variable represents survival after 7 months from the specified treatment plan, with real number values ranging from 1.0 (sure survival) to -1.0 (sure mortality). Several training algorithms are selected: general regression, radial basis function, and backpropagation. General regression is used to mimic the wide-spread usage of probabilistic and regression modeling in medical diagnostics (Yet et al.,

2014). Radial basis function is used due to its demonstrated performance when extrapolation is required (Park & Sandberg, 1993). Finally, backpropagation is used due to its long history of being a general purpose problem solver able to approximate arbitrarily complex models (Hornik, 1991; White, 1990). Backpropagation is also the most widely used training method for ANNS in medical decision support systems, which facilitates comparison (Amato et al., 2013; Lisboa & Taktak, 2006).

Table 3. Pearson Correlation Values for SF-36 Domain Variables

<table><tr><td></td><td>PF</td><td>RP</td><td>RE</td><td>BP</td><td>VT</td><td>MH</td><td>SF</td><td>GH</td></tr><tr><td>PF</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>RP</td><td>0.555685</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>RE</td><td>0.497094</td><td>0.616197</td><td>1</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>BP</td><td>0.475787</td><td>0.582908</td><td>0.356616</td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>VT</td><td>0.672644</td><td>0.631822</td><td>0.56247</td><td>0.463769</td><td>1</td><td></td><td></td><td></td></tr><tr><td>MH</td><td>0.449469</td><td>0.324901</td><td>0.494599</td><td>0.362833</td><td>0.568208</td><td>1</td><td></td><td></td></tr><tr><td>SF</td><td>0.624996</td><td>0.67517</td><td>0.550555</td><td>0.576696</td><td>0.672883</td><td>0.492585</td><td>1</td><td></td></tr><tr><td>GH</td><td>0.569735</td><td>0.458763</td><td>0.480935</td><td>0.432736</td><td>0.619127</td><td>0.618939</td><td>0.542843</td><td>1</td></tr><tr><td>Count</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>&gt;0.60</td><td>2</td><td>3</td><td>1</td><td>0</td><td>4</td><td>1</td><td>3</td><td>2</td></tr></table>

Following good ANN architecture design practices (Walczak & Cerpa 1999; Zhang, 2007), several different architectures, including both single and two-hidden layer architectures, are developed in parallel for all of the selected training algorithms. The first hidden layer always started with the same number of neurodes as the input layer, but then this layer was incremented and also decremented by two until prediction performance stopped increasing for two iterations, indicating overlearning (too many neurodes) or inability to learn (too few neurodes). Prediction performance for each ANN is estimated during training using root mean square error (RMSE), which indicates the average error across each epoch (16 randomly chosen samples from the training population) of training samples. Then the two architectures with one additional and one less neurode from the best performing architecture are also evaluated. When a second layer is attempted it always started with half the number of neurodes as the first hidden layer and again was increased by two neurodes at a time until RMSE did not decrease for two iterations. Training for each ANN architecture continues until the RMSE is below 0.05 or the RMSE remains constant for 750 training epochs.

The model selection procedure of Swanson and White (1995) is used to determine the best performing architecture and learning algorithm combination. Performance evaluation is specified below. The general regression learning algorithm ANN models uniformly performed the worst and never achieved a 90% sensitivity, while the backpropagation trained ANNs generally performed the best. It was possible to achieve slightly better sensitivity with the radial basis function learning algorithm, but this was at a cost of having a significantly lower specificity. Therefore, only the backpropagation trained ANN models are discussed further in this paper.

## 3.3. Evaluation criteria

A sensitivity of at least 90% is specified by a domain expert as the minimal acceptable criterion for use in determining treatment decisions for pancreatic cancer that would minimize physicians’ regret. This means that for 90% (or higher if higher sensitivity is achieved) of the time, the ANN model would be able to accurately determine that a patient would live for at least 7 months following the specified treatment. This in turn would reduce both omission and commission regret for physicians and patients. If multiple ANN models are able to satisfy the sensitivity criterion, then consequent maximization of specificity serves as a secondary criterion to select between the ANN survival prediction models. Specificity primarily targets regret of commission, by identifying patients likely not to live 7 months past the specified treatment.

## 3.4. Experiment 2: identifying SF-36 variable contributions

In addition to their direct clinical decision support, ANNs may also be used to evaluate contribution of variables to heuristic clinical decision making (Walczak, 2008). Discovery of the contribution of variables to the medical decision making process in clinical medicine is an important and ongoing research endeavor (Dag et al., 2016; Hunink et al., 2014).

The efficacy of using an ANN to predict 7-month survival may be shown from the first part of this research. The machine learning nature of ANNs enables developers to include non-correlated variables that might have an arbitrary influence on the model’s predictions. The second part of the research attempts to evaluate the contribution of age and also the 8 SF-36 domain variables towards this prediction. This could help reduce the ANN model’s complexity and associated costs if some of the SF-36 variables or other demographic variables can be eliminated. Variable contributions may be assessed using a leave-one-out protocol. New models are created, trained, and validated, but with different combinations of sex and SF-36 variables leaving one or more out of the input vector.

The reduction of the set of SF-36 domain variables is grounded in prior research which has shown that many clinical decision support systems make use of a shortened version of the SF-36 (Brazier et al., 2010) or a partial set of the domain variables. Some examples include the use of just PF, BP, and SF as secondary outcomes for determining treatment in gastrointestinal surgery (Vlug et al., 2011) and the use (Weinstein et al., 2010).

ANN models similar to the one shown in Figure 1, but without the age variable have been created, trained and validated, using the same procedure for identifying the optimal ANN architecture as used for the original model. The optimally performing ageless ANN has an identical architecture, minus the age input variable, identical to the full variable ANN model minus one hidden layer neurode. Based on these results, a short cut is taken for evaluating the SF-36 variable contributions by only testing a single ANN architecture. The architectures for each new SF-36 contribution assessment ANN model have their hidden layer neurodes adjusted according to the number of SF-36 domain variables removed from the input vector.

Each of the SF-36 variables is removed individually from the original ANN model from part 1. Based

# ACCEPTED MANUSCRIPT

on the correlation values shown in Table 3, it is anticipated that VT and likely RP and SF may represent redundant information and could be removed, but this needs to be verified. The results of the 8 new ANNs, each missing a single SF-36 domain variable are compared using a 0 cutoff value against the full ANN using a 0 cutoff value to identify differences in sensitivity, specificity, and overall accuracy. Any variables that demonstrate an improvement in any of these evaluation values are then dropped in paired combinations for new ANN models. Finally, additional combinations reflecting all variables that showed an improvement in any of the criteria and for all variables that showed a non-negative improvement in overall accuracy are also modeled using ANNs. In total, 16 different combinations of SF-36 variables are dropped from the input vector and their ANN outputs compared to the original full variable set ANN.

## 4. Results

## 4.1. Efficacy of an ANN pancreatic cancer survival model

The desired 90% sensitivity performance is achieved by several of the 16 backpropagation trained ANN model architectures. Using the secondary criteria of simultaneously maximizing specificity, a single hidden layer ANN model with 21 hidden layer neurodes is selected as the optimal ANN architecture, from those examined in this study. This architecture is displayed in Figure 1.

An initial (and also intuitive) cutoff value for the ANN survival predictions is 0 (zero), with all positive values indicating survival at 7 months and all negative values indicating mortality prior to 7 months following treatment. The ANN shown in Figure 1 achieves a sensitivity of 91.30% and a specificity of 37.04%, and an overall prediction accuracy of 71.23% at the decision cutoff value of 0. A tradeoff exists, though not necessarily linear, between sensitivity and specificity. Medical research commonly uses receiver operating characteristic (ROC) curves to balance conflicting sensitivity and specificity goals as evaluated using the area under the ROC (AUROC) (Fawcett, 2006). ROC curves may be simulated in an ANN model by making small adjustments in the decision cutoff value and examining how this affects the corresponding sensitivity and specificity. Results of adjusting the survival prediction cutoff value for the pancreatic cancer 7-month survival prediction ANN are shown in Figure 2, with the cutoff value adjustments shown along the x-axis. The balance between sensitivity and specificity evaluated using the AUROC of the ROC curve, estimated using trapezoidal approximation, is shown in Figure 3.

Figure 1. Pancreatic Cancer ANN Optimal Architecture  
![](/api/attachments/JENTWGMG/fulltext/images/88b94e212576cfc2d44af053325e51c2aeade04bb05f4c58a2bd0582b129ade3.jpg)

## ACCEPTED MANUSCRIPT

As shown in Figure 2, the maximum specificity achievable by the current ANN prediction model for the study’s population while maintaining a minimum 90% sensitivity is a specificity of 40.74% at a cutoff value of 0.03155, producing an overall accuracy of 77.98%. Figure 2 also demonstrates that with a very small upward adjustment in the prediction cutoff value to 0.01, the same sensitivity of 91.30% achieved at a cutoff value of 0 is maintained. Furthermore, with a new cutoff value of 0.01, the specificity is increased to 38.27% and the overall accuracy increases to 71.69%, which is the maximum achievable for the current ANN model at any cutoff. If a physician desires to maximize specificity, while still maintaining this maximum overall accuracy and a sensitivity of 90%, this may be achieved with cutoff values between 0.01 and 0.025, which all produce a specificity of 39.51% and an acceptable sensitivity of 90.58%.

Figure 2. Sensitivity Versus Specificity Tradeoff  
![](/api/attachments/JENTWGMG/fulltext/images/e35a520a93c961ec0a585bd6fa1bb045191a2ab16db6b76145cf8c911a697aad.jpg)

As mentioned in the Background section, logistic regression is another commonly used modeling method in the medical domain. A Cox proportional hazards regression model (a type of logistic regression used for survival predictions) is developed and produces an accuracy of 71.56% with a sensitivity of 74.70% and a specificity of 61.54%. While the overall accuracy of the Cox model is similar to the ANN model, it violates the assumption of a required 90% sensitivity. If the Cox model is adjusted to create a 90% sensitivity, then its specificity drops to 34.62% which is 3.6% to 6% less than the ANN model (depending on which cutoff value is used). While the overall accuracy is comparable, the ANN model produces a better specificity value.

Figure 3. Simulated ROC curve  
![](/api/attachments/JENTWGMG/fulltext/images/fbe60f27c3e76b8ab9e94d52444e207ee98998302a61800270d9ac46e237a9ca.jpg)  
Another evaluation of the specified pancreatic cancer ANN is achieved by comparing its accuracy to other ANNs that attempt to predict other types of cancer survival. Zolbanin et al. (2015) develop six ANNs for various types of cancers and comorbid cancers that achieve overall prediction accuracies between 70.39% and 75.35%. The pancreatic cancer ANN achieves slightly better results, depending on the cutoff used with overall prediction accuracies ranging from 71.23% to 77.98%. The Zolbanin et al. (2015) research did not report attempting to maximize either sensitivity or specificity and as such these values are not comparable.

## 4.2. Determining variable contributions

A preliminary estimate of the contribution of variables, or at least the direction of contribution, may be obtained by examining the connection weights from the input variables to the hidden layer in the ANN model. The only definitive information obtainable through the ANN connection weights is that BP, VT, and SF were the only SF-36 input variables that only had negative connection weights. While this does not indicate contribution or lack thereof, it does imply that these three quality of life measurements are negatively associated with survival. The other SF-36 variables all had mixed positive and negative weights on connections to the hidden layer. However, two hidden nodes had multiple positively weighted connections coming from SF-36 input variables: one that connected positively to RE, MH, and GH, and another that connected positively to both MH and GH. While mixed connection weights do not reveal the impact of a variable, these positive connections, especially repeate for the two variable MH and GH indicate a positive overall influence of these SF-36 domain variables on survival.

The new ANN model without any age information performed at nearly identical levels (statistically insignificant change, $p = 0 . 4 3 3 )$ as the original pancreatic cancer treatment survival prediction model, with an increase in overall accuracy of 1.3%, a decrease in sensitivity of 0.6% and an increase in specificity of 5.7%. This indicates that for the ANN model, age did not contribute to the ANN’s survival prediction and thus could be removed. Since older patients naturally tend to have higher surgical mortality rates (Yancik et al., 2001), some caution must be used in interpreting these results as the physicians making the treatment decisions used in the current research may have already incorporated this information into their respective treatment plans.

Results of comparing the differences in accuracy, sensitivity, and specificity for the 8 leave-one-out SF-36 ANN models against the original full variable set ANN from experiment 1, using a cutoff decision value of 0, are given in Table 4. The values in Table 4 represent the change in percentage points between the two ANNs (e.g., if the original ANN has a sensitivity of 91.30% and a new ANN has a sensitivity of 90.01%, then this would be reported as a change of -1.29%).

There are four variables in Table 4 that are able to increase the ANN’s sensitivity or specificity: PF,

# ACCEPTED MANUSCRIPT

RP, VT, and MH, and two of these are also able to improve the overall accuracy. The SF-36 domain variables RP and VT, identified in Table 3 as being correlated with other SF-36 variables at the 0.60 level are two of the four variables able to improve the ANN’s performance in two of the three performance measurements. Removal of the SF variable previously identified was not able to increase the performance of the ANN on any dimension. Further investigation of lack of variable impact is performed by analyzing variables and dropping the 3 variables that produced non-negative overall accuracy changes. The results of these 8 new ANNs are shown in Table 5.

Table 4. ANN Results When Missing One of the SF-36 Domain Variables in the Input Vector

<table><tr><td>Missing variable</td><td>Δ in Accuracy</td><td>Δ in Sensitivity</td><td>Δ in Specificity</td></tr><tr><td>PF</td><td>0</td><td>+4.82%</td><td>-15.39%</td></tr><tr><td>RP</td><td>+0.92%</td><td>+4.82%</td><td>-11.54%</td></tr><tr><td>RE</td><td>-3.67%</td><td>0</td><td>-15.39%</td></tr><tr><td>BP</td><td>-6.42%</td><td>-1.21%</td><td>-23.08%</td></tr><tr><td>VT</td><td>+0.92%</td><td>-1.21%</td><td>+7.69%</td></tr><tr><td>MH</td><td>-3.67%</td><td>-6.02%</td><td>+3.85%</td></tr><tr><td>SF</td><td>-6.42%</td><td>-4.82%</td><td>-11.54%</td></tr><tr><td>GH</td><td>-8.26%</td><td>-9.64%</td><td>-3.85%</td></tr></table>

Only two of the variable combinations dropped out of the ANN input vector are able to produce positive differences and only for sensitivity. This indicates that eliminating two or more of the 4 SF-36 variables identified by the leave-one-out method is not a practical idea, unless the physician’s goal is to maximize sensitivity regardless of costs to specificity and overall accuracy of the model. The results from Table 4 indicate that it might be possible to eliminate a single SF-36 variable and maintain the required 90% sensitivity and improve the overall performance accuracy of the ANN, this should only be considered for the VT variable which maintains a sufficient sensitivity and increases specificity.

Table 5. ANN Results When Missing Combinations of SF-36 Domain Variables

<table><tr><td>Missing variable</td><td>Δ in Accuracy</td><td>Δ in Sensitivity</td><td>Δ in Specificity</td></tr><tr><td>PF &amp; RP</td><td>-0.92%</td><td>+6.02%</td><td>-23.08%</td></tr><tr><td>PF &amp; VT</td><td>-7.34%</td><td>-7.23%</td><td>-7.69%</td></tr><tr><td>PF &amp; MH</td><td>-8.26%</td><td>-8.43%</td><td>-7.69%</td></tr><tr><td>RP &amp; VT</td><td>-5.51%</td><td>-4.82%</td><td>-7.69%</td></tr><tr><td>RP &amp; MH</td><td>-0.92%</td><td>-1.21%</td><td>0</td></tr><tr><td>VT &amp; MH</td><td>0</td><td>+1.20%</td><td>-3.85%</td></tr><tr><td>RP, VT, &amp; PF</td><td>-6.42%</td><td>-6.02%</td><td>-7.69%</td></tr><tr><td>RP, VT, PF, &amp; MH</td><td>-10.09%</td><td>-3.61%</td><td>-30.77%</td></tr></table>

## 5. Discussion

The ANN pancreatic cancer survival prediction tool may reduce regret in two ways. First, by reducing a resection surgery. Commission regret will still occur for the 8.7% of patient whom are incorrectly predicted to survive a resection surgery, but ultimately still die within 7 months. Omission regret is reduced when the ANN model shows that the selected treatment is likely to result in mortality within 7 months and a patient or physician then elects against resection surgery or other adjuvant therapy treatments. The physician and patient may adjust their treatment preferences using the values from the ANN as a decision aid to help overcome their respective decision regret.

As indicated above, using a value of 0 to distinguish between mortality and survival is intuitive and also does not require any additional testing, evaluation, or interpretation of the ANN output value. Since this value produces results that exceed the required minimum sensitivity and also have a reasonably high specificity, it generates very good results with regard to serving as a decision aid to help reduce treatment decision regret. However, different physicians may want to maximize overall accuracy (cutoff = 0.01), or alternately maximize specificity while maintaining a 90% sensitivity (cutoff = 0.03155, as shown in Figure 2).

It is interesting to note that the nonlinear ANN model does not produce linear trade-offs between sensitivity and specificity. Between the values of -0.2 and -0.05, while sensitivity drops from 100% to 93.48%, a change of 6.52%, specificity increases from 0% to 28.4%. While further decreases continue in sensitivity they remain minimal through a cutoff value of 0.125. Realize that the scale of the x-axis is also not linear, so the rapid increases in specificity and decreases in sensitivity shown on the right hand side of the graph appear greatly magnified. Physicians desiring to experiment with the cutoff value must use due diligence to make sure that they capture the optimal values satisfying their regret-based decision making criteria (e.g., specific minimums for either sensitivity, specificity, or overall accuracy, or any combination).

With respect to the data used in this research study, age is found to not contribute significantly to the ANN output value. Two other variables have also been identified (see Table 4) for possible exclusion from the input data set for the ANN, but only one can be removed since removing both (see Table 5) reduces sensitivity, specificity, and accuracy of the ANN 7-month survival prediction model. The choice between RP and VT for possible elimination is dependent on the goals of the physician and through the physician the patient. If increasing specificity while maintaining a sensitivity of at least 90% is desired, then the VT variable may be eliminated. If on the other hand the goal of the physician is to maximize sensitivity, even with a large reduction in specificity, then the RP variable or the combine RP and PF variables result in improved sensitivity.

As highlighted in the discussion above, and as shown in the simulated ROC curve in Figure 2, a sensitivity of 90% or higher is achievable and depending on the cutoff value and also variable selection, differing levels of sensitivity and specificity are achievable. The decision to use a modified cutoff value or selecting an ANN with a reduced input variable set is dependent on a physician’s or patient’s goals with respect to accurately identifying survival versus accurately identifying mortality. Each of these decisions will also be impacted by how the physician or patient desires to ameliorate their various decision regrets.

## 5.1. Limitations

As with any artificial intelligence-based clinical decision support tool, the goal of the presented ANN model is to increase information available to physicians and patients for making optimal treatment decisions. Additionally, the current research demonstrates how the developed ANN can simultaneously reduce decision regret. Physicians should use the ANN with full understanding that incorrect predictions do still occur, less than 29% of the time.

While numerous training methods and ANN architectures were evaluated, the results should be interpreted as a proof of concept demonstrating the minimum achievable sensitivity, specificity, and overall accuracy results. Future research may be able to achieve better results with different architectures or training algorithms.

The current ANN model is developed using data from a single large urban university teaching hospital. The results should generalize well to similar institutions with probabilistically similar outcomes. This is because the survival of patients is due in part to the skill of the physician. Therefore, if the probabilistic survival of patients or the patient and disease demographics differ significantly from those used in developing the current ANN survival prediction model, then the ANN model will need to be trained anew from data for each of these hospitals with significantly differing demographics. These new ANN models could be collected in a library so that potential new users would first search the library of ANN pancreatic cancer survival prediction models to see if any matched their patient, disease, and outcome demographics before training their own model.

## 5.2. Implications for practice

Clinical diagnostic and prognostic decision support ANNs are typically standalone systems (Lisboa & Taktak, 2006). The system reported in this article can certainly operate as a standalone decision support

# ACCEPTED MANUSCRIPT

tool to help physicians and patients determine likely regret from treatment decisions, where commission regret is assumed if the patient is not likely to survive a planned treatment and omission regret is assumed if a patient is likely to survive surgery or another treatment plan that could prolong their life, but which is not currently being considered.

The rapid diffusion and adoption of electronic health record (EHR) systems (Nguyen, Bellucci, & Nguyen, 2014), indicates another means for incorporating ANN clinical decision support systems into a physician’s normal workflow. When EHRs are integrated into clinical workflow the qu y of care improves (van Poelgeest et al., 2017). Furthermore, research has documented that over 65% of all physicians make use of EHRs and CDSS in making treatment decisions (DeMello & Deshpande, 2012). Incorporating the ANN 7-month survival decision support system into the physician workflow would lead to increased utilization (Feldman, Davis, & Chawla, 2015).

Prior research has demonstrated the efficacy of incorporating clinical decision support tools into EHRs (Kuperman et al., 2007). Further research is needed to investigate embedding the ANN 7-month survival prediction model into EHRs for easy access and utilization by physicians and the resulting effect on pancreatic cancer treatment decisions. The demonstrated ANN system is specific to pancreatic cancer. Although various cancer etiologies may differ, treatment of any type of cancer follows similar processes. Future research is also needed to examine if the concepts proven in the pancreatic cancer treatment decision support model can be generalized to other types of cancers.

Hernandez et al. (2014) demonstrate a system to graphically acquire physician (and could also be used for patients) regret tolerances. Either a standalone or EHR embedded ANN decision support system could then use these values along with the sensitivity and specificity levels of the ANN to optimize pancreatic cancer treatment decision making for physicians and patients and furthermore reduce decision regret.

## 5.3. Decision regret reduction examples

Prior research has shown that accounting for patient omission regret is important and that individuals have varying levels of regret for similar decisions (Baron & Ritov, 2004). Furthermore, evidence exists that patients typically regret a negative outcome more if it is caused through action than similar results from inaction (Connolly & Reb, 2005). Research has suggested that this perception of increased regret for action may alternately be due to perception of direct consequences (action) versus indirect consequences (inaction) of a treatment decision (Baron & Ritov, 2004).

For purposes of the examples that follow, assume that the physician has a commission regret for surgery of 30% and an omission regret for surgery of 45%, while the physician’s commission regret for observe and also adjunctive therapies is 15% and omission regret of 20%. Assume also that a patient’s surgical commission regret equal to their $\frac { a g e } { 1 0 0 }$ (so that older patients are more regretful of having surgery with associated morbidities if it fails) and surgical omission regret of $\frac { 2 0 } { a g e }$ (so a 50 year old would have a 50% commission regret and a 40% omission regret) and the patient’s non-surgical omission regret is 20% less than their surgical regret and their commission regret is 15% less than their surgical commission regret.

Example 1: A 95 year old has only chemo-radiation (adjunctive) treatment, but the ANN correctly identifies that this patient will not survive 7-months. The patient’s regret prior to the ANN notification is a commission regret of 80%. The notification of the likely outcome by the ANN could help reduce this patient’s regret to just over 1% immediately, since it would transform it from a commission to an omission regret. This represents an almost complete elimination of regret enabled by the ANN prediction. Additionally, not having the additional morbidities associated with the adjunctive therapies would improve this patient’s quality of life for its duration and thereby might further reduce regret. The physician’s regret remains at 15% to 20% for both types of non-surgical treatment.

Example 2: A 58 year old is being treated as an observation only patient. Since this is observation/do nothing, the patient currently only has regret of omission of 35% for surgery and

15% for adjunctive therapies for a cumulative regret of 50%. The ANN successfully predicts that this patient will not survive 7 months under the current treatment. This information allows the patient and physician to seriously consider other treatment options. If the patient and physician then elect to start adjunctive therapy, the patient’s regret is reduced to a 43% commission regret, reducing overall regret by 7%.

Example 3: A 70 year old is recommended to have resection surgery. The physician’s regret prior to surgery is 30% and the patient’s regret is 70%. The ANN accurately predicts that the patient will survive at least 7 months following surgery, which eliminates the physician’s regret since the surgery will be successful in its goal and also reduces the patient’s regret to at least 29% transforming the regret from commission to omission of other treatments.

Example 4: A 55 year old will be having both adjunctive therapy and resection surgery. The physician’s pre-procedure regret is 15% for the adjunctive therapy and 30% for the surgery. The patient’s regret is 55% for the surgery and 40% for the chemo-radiation treatments. The ANN accurately predicts that this patient will survive at least 7 months, which eliminates the physician’s regret and either eliminates or significantly reduces the patient’s regret (a possible omission regret for do nothing of 16%).

Example 5: This is a set of two counter examples. In the first, a 52 year old about to undergo resection surgery with commission regret of 52% and 38% (combined regret 80%) is predicted by the ANN to die before 7 months, but in fact survives for at least 7 month. While the ANN could not reduce the commission error, it may have caused this patient to subsequently seek alternative and less promising treatments. The second example is for a 78 year old who is being treated with just surgery and the ANN incorrectly predicts that the patient will survive 7 months post-surgery, which would normally have reduced the perceived regret of the physician and patient, until the patient is much closer to dying in which case their regret would return to original levels of 30% for the physician and 78% for the patient or their family (or higher, since this situation might also add in omission regret for other forms of treatment).

# ACCEPTED MANUSCRIPT

The first 4 examples illustrate accurate predictions of the ANN and demonstrate immediate reduction in regret for both survivors and patients suffering mortality, as well as being able to reduce physician regret to 0% for those patients predicted to survive. The last example points out as is already shown in the Limitations subsection that the ANN is not 100% accurate and that incorrect predictions occur, with errant reductions in regret, which might subsequently magnify the original regret.

Future research is needed to explore the further optimization of this ANN design to improve overall accuracy through improvements in both specificity and sensitivity. Additional research could examine extending this ANN outcome prediction technique to other forms of prognostic cancer predictions.

The current ANN was developed to predict the outcome for a specific patient to a specific treatment recommended by their physician. The physician may be incorporating additional medical, historical, and patient specific knowledge when making their initial treatment decision. Therefore the prediction of the ANN, bearing in mind its level of accuracy, may be used by physicians to help overcome their own regret as well as the regrets of their patients for a specific treatment. This current system is not meant to be used as a treatment finder by re-running the ANN prediction for all 4 possible treatment options and then selecting the best outcome. Additional research is need to identify additional variables that will be sufficient to enable the augmented ANN to perform in this manner and therefore transition from a prognostic outcome prediction tool with subsequent reductions in regret to a treatment decision support tool to assist physicians and surgeons in selecting the treatment plans with the highest likelihood of a positive outcome for their patients.

## 6. Conclusion

An ANN model that is capable of predicting 7-month survival following treatment of pancreatic cancer has been developed. This ANN treatment survival prediction model produced a 91.30% sensitivity and a 37.04% specificity, with an overall prediction accuracy of 71.23%. Adjusting the prediction cutoff value slightly, to 0.01, maintains the sensitivity performance and increases specificity to 38.27% and overall model accuracy to 71.69%.

In addition to adjusting the cutoff value to improve desired performance, the age demographic and certain of the SF-36 variables are shown to have an impact on the performance of the ANN when dropped from the input vector.

The survival predictions of the ANN model may be used by physicians and patients to reduce treatment decision regret and to be better informed in making treatment decisions. The overall accuracy of ases, the ANN will be able to provide information that will assist physicians and patients in selecting tments with minimal or no regret, since the ANN predicts the survival outcome for this portion of the population.

## Conflict of Interest Statement

The authors both declare that this research was performed unfunded and that no conflict of interest or other competing interest is present.

## References

Amato, F., López, A., Peña-Méndez, E. M., Vaňhara, P., Hampl, A., & Havel, J. (2013). Artificial neural networks in medical diagnosis. Journal of Applied Biomedicine, 11(2), 47-58.

Baron, J., & Ritov, I. (2004). Omission bias, individual differences, and normality. Organizational

Bartosch‐Härlid, A., Andersson, B., Aho, U., Nilsson, J., & Andersson, R. (2008). Artificial neural networks in pancreatic disease. British Journal of Surgery, 95(7), 817-826.

Bartosch-Härlid, A., & Andersson, R. (2010). Diabetes mellitus in pancreatic cancer and the need for diagnosis of asymptomatic disease. Pancreatology, 10(4), 423-428.

Baxter, N. N., Whitson, B. A., & Tuttle, T. M. (2007). Trends in the Treatment and Outcome of Pancreatic Cancer in the United States. Annals of Surgical Oncology, 14(4), 1320-1326.

Brazier, J. E., Yang, Y., Tsuchiya, A., & Rowen, D. L. (2010). A review of studies mapping (or cross walking) non-preference based measures of health to generic preference-based measures. The European Journal of Health Economics, 11(2), 215-225.

Chang, C. L., & Hsu, M. Y. (2009). The study that applies artificial intelligence and logistic regression for assistance in differential diagnostic of pancreatic cancer. Expert Systems with Applications, 36(7), 10663-10672.

Connolly, T., & Reb, J. (2005). Regret in cancer-related decisions. Health Psychology, 24(4S), S29-S34.

Cress, R. D., Yin, D., Clarke, L., Bold, R., & Holly, E. A. (2006). Survival among patients with 17(4), 403-409.

Dag, A., Topuz, K., Oztekin, A., Bulur, S., & Megahed, F. M. (2016). A probabilistic data-driven framework for scoring the preoperative recipient-donor heart transplant survival. Decision Support Systems, 86, 1-12.

Das, A., Nguyen, C. C., Li, F., & Li, B. (2008). Digital image analysis of EUS images accurately differentiates pancreatic cancer from chronic pancreatitis and normal tissue. Gastrointestinal Endoscopy, 67(6), 861-867.

Dayhoff, J. E., & DeLeo, J. M. (2001). Artificial neural networks. Cancer, 91(S8), 1615-1635.

Delen, D., Oztekin, A., & Tomak, L. (2012). An analytic approach to better understanding and management of coronary surgeries. Decision Support Systems, 52(3), 698-705.

DeMello, J. P., & Deshpande, S. P. (2012). Factors impacting use of information technology by physicians in private practice. International Journal of Healthcare Information Systems and Informatics, 7(2), 17–28.

Dimou, F., Sineshaw, H., Parmar, A. D., Tamirisa, N. P., Jemal, A., & Riall, T. S. (2016). Trends in receipt and timing of multimodality therapy in early-stage pancreatic cancer. Journal of Gastrointestinal Surgery, 20(1), 93-103.

dos Santos Valente, E. S. (2015). Development of computational tools for the integrated analysis of DNA microarray data with applications in cancer research (Doctoral dissertation, University of Minho, Braga, and Guimarães (Portugal)).

Dreiseitl, S., & Ohno-Machado, L. (2002). Logistic regression and artificial neural network classification

models: a methodology review. Journal of Biomedical Informatics, 35(5), 352-359.

Fawcett, T. (2006). An introduction to ROC analysis. Pattern Recognition Letters, 27(8), 861-874.

Feldman, K., Davis, D., & Chawla, N. V. (2015). Scaling and contextualizing personalized healthcare: a case study of disease prediction algorithm integration. Journal of Biomedical Informatics, 57, 377- 385.

Fesinmeyer, M. D., Austin, M. A., Li, C. I., De Roos, A. J., & Bowen, D. J. (2005). Differences in Survival by Histologic Type of Pancreatic Cancer. Cancer Epidemiology and Prevention Biomarkers, 14(7), 1766-1773.

Freelove, R., & Walling, A. D. (2006). Pancreatic cancer: diagnosis and management. American Family Physician, 73(3), 485-492.

Gillen, S., Schuster, T., Zum Büschenfelde, C. M., Friess, H., & Kleeff, J. (2010). Preoperative/neoadjuvant therapy in pancreatic cancer: a systematic review and meta-analysis of response and resection percentages. PLoS Medicine, 7(4), e1000267.

Gorunescu, F., Gorunescu, M., Săftoiu, A., Vilmann, P., & Belciug, S. (2011). Competitive/collaborative neural computing system for medical diagnosis in pancreatic cancer detection. Expert Systems, 28(1), 33-48.

Hagan, M. T., Demuth, H. B., Beale, M. H., & De Jesus, O. (2014). Neural Network Design 2<sup>nd</sup> Edition. Martin Hagan. Y

Hernandez, J. M., Tsalatsanis, A., Humphries, L. A., Miladinovic, B., Djulbegovic, B., Velanovich, V. (2014). Defining Optimum Treatment of Patients With Pancreatic Adenocarcinoma Using Regret-Based Decision Curve Analysis. Annals of Surgery, 259(6), 1208-1214.

Hornik, K. (1991). Approximation capabilities of multilayer feedforward networks. Neural Networks, 4(2), 251-257.

Hunink, M. M., Weinstein, M. C., Wittenberg, E., Drummond, M. F., Pliskin, J. S., Wong, J. B., & Glasziou, P. P. (2014). Decision Making in Health and Medicine: Integrating Evidence and Values. Cambridge: Cambridge University Press.

Janssen-Heijnen, M. L., Maas, H. A., Houterman, S., Lemmens, V. E., Rutten, H. J., & Coebergh, J. W. W. (2007). Comorbidity in older surgical cancer patients: influence on patient care and outcome. European Journal of Cancer, 43(15), 2179-2193.

Kuhlmann, K. F., de Castro, S. M., Wesseling, J. G., ten Kate, F. J., Offerhaus, G. J., Busch, O. R., van Gulik, T. M., Obertop, H., & Gouma, D. J. (2004), Surgical treatment of pancreatic adenocarcinoma:

Kuperman, G. J., Bobb, A., Payne, T. H., Avery, A. J., Gandhi, T. K., Burns, G., Classen, D. C., & Bates, D. W. (2007). Medication-related clinical decision support in computerized provider order entry systems: A review. Journal of the American Medical Informatics Association, 14(1), 29–40.

Li, D., Xie, K., Wolff, R., & Abbruzzese, J. L. (2004). Pancreatic cancer. The Lancet, 363(9414), 1049- 1057.

Lisboa, P. J., & Taktak, A. F. (2006). The use of artificial neural networks in decision support in cancer: A systematic review. Neural Networks, 19(4), 408-415.

Loomes, G., & Sugden, R. (1982). Regret theory: An alternative theory of rational choice under uncertainty. The Economic Journal, 92(368), 805-824.

Malvezzi, M., Bertuccio, P., Levi, F., La Vecchia, C., & Negri, E. (2013). European cancer mortality predictions for the year 2013. Annals of Oncology, 24(3), 792-800.

Mangiameli, P., West, D., & Rampal, R. (2004). Model selection for medical diagnosis decision support systems. Decision Support Systems, 36(3), 247-259.

McHorney, C. A., Ware Jr, J. E., Lu, J. R., & Sherbourne, C. D. (1994). The MOS 36-item Short-Form Health Survey (SF-36): III. Tests of data quality, scaling assumptions, and reliability across diverse patient groups. Medical Care, 32(1), 40-66.

Nguyen, L., Bellucci, E., & Nguyen, L. T. (2014). Electronic health records implementation: an evaluation of information system impact and contingency factors. International Journal of Medical Informatics, 83(11), 779-796.

Okano, K., Hirao, T., Unno, M., Fujii, T., Yoshitomi, H., Suzuki, S., Satoi, S., Takahashi, S., Kainuma,

O., & Suzuki, Y. (2015). Postoperative infectious complications after pancreatic resection. British Journal of Surgery, 102(12), 1551-1560.

Park, J., & Sandberg, I. W. (1993). Approximation and radial-basis-function networks. Neural Computation, 5(2), 305-316.

Polistina, F., Costantin, G., Casamassima, F., Francescon, P., Guglielmi, R., Panizzoni, G., Febbraro, A., & Ambrosino, G. (2010). Unresectable locally advanced pancreatic cancer: a multimodal treatment using neoadjuvant chemoradiotherapy (gemcitabine plus stereotactic radiosurgery) and subsequent surgical exploration. Annals of Surgical Oncology, 17(8), 2092-2101.

Qiong-ying, H., Wang, K. Z., Ding, Y. H., Zheng, L. F., Liang, S. H., Lei, Z. M., Fu, W. G., & Yan, L. (2010). Application of SELDI-TOF-MS coupled with an artificial neural network model to the diagnosis of pancreatic cancer. Laboratory Medicine, 41(11), 676-681.

Rahib, L., Smith, B. D., Aizenberg, R., Rosenzweig, A. B., Fleshman, J. M., & Matrisian, L. M. (2014). Projecting cancer incidence and deaths to 2030: the unexpected burden of thyroid, liver, and pancreas cancers in the United States. Cancer Research, 74(11), 2913-2921.

Robinson Jr, D. W., Eisenberg, D. F., Cella, D., Zhao, N., de Boer, C., & DeWitte, M. (2008). The prognostic significance of patient-reported outcomes in pancreatic cancer cachexia. The Journal of Supportive Oncology, 6(6), 283-290.

Săftoiu, A., Vilmann, P., Gorunescu, F., Gheonea, D. I., Gorunescu, M., Ciurea, T., Popescu, G. L., Iordache, A., Hassan, H., & Iordache, S. (2008). Neural network analysis of dynamic sequences of EUS elastography used for the differential diagnosis of chronic pancreatitis and pancreatic cancer. Gastrointestinal Endoscopy, 68(6), 1086-1094.

Săftoiu, A., Vilmann, P., Gorunescu, F., Janssen, J., Hocke, M., Larsen, M., Iglesias–Garcia, J., Arcidiacono, P., Will, U., Giovannini, M., & Dietrich, C. F. (2012). Efficacy of an artificial neural network–based approach to endoscopic ultrasound elastography in diagnosis of focal pancreatic masses. Clinical Gastroenterology and Hepatology, 10(1), 84-90.

Schmoll, H. J., Van Cutsem, E., Stein, A., Valentini, V., Glimelius, B., Haustermans, K., Nordlinger, B.,

## ACCEPTED MANUSCRIPT

Van de Velde, C. J., Balmana, J., Regula, J., & Nagtegaal, I. D. (2012). ESMO Consensus Guidelines for management of patients with colon and rectal cancer. A personalized approach to clinical decision making. Annals of Oncology, 23(10), 2479-2516.

Smith, M. (1993). Neural Networks for Statistical Modeling. Van Nostrand Reinhold: New York.

Swanson, N. R., & White, H. (1995). A model-selection approach to assessing the information in the term Statistics, 13(3), 265-275.

Swanson, R. S., Pezzi, C. M., Mallin, K., Loomis, A. M., & Winchester, D. P. (2014). The 90-Day Mortality After Pancreatectomy for Cancer Is Double the 30-Day Mortality: More Than 20,000 Resections From the National Cancer Data Base. Annals of Surgical Oncology, 21(13), 4059-4067.

Tetreault, L., Le, D., Côté, P., & Fehlings, M. (2015). The practical application of clinical prediction rules: a commentary using case examples in surgical patients with degenerative cervical myelopathy. Global Spine Journal, 5(6), 457-465.

Tsalatsanis, A., Hozo, I., Vickers, A., & Djulbegovic, B. (2010). A regret theory approach to decision curve analysis: a novel method for eliciting decision makers' preferences and decision-making. BMC Medical Informatics and Decision Making, 10(1), 51.

van Poelgeest, R., van Groningen, J. T., Daniels, J. H., Roes, K. C., Wiggers, T., Wouters, M. W., & Schrijvers, G. (2017). Level of Digitization in Dutch Hospitals and the Lengths of Stay of Patients with Colorectal Cancer. Journal of Medical Systems, 41(5), article 84.

Velanovich, V. (2011), The Association of Quality-of-Life Measures With Malignancy and Survival in Patients With Pancreatic Pathology. Pancreas, 40(7), 1063-1069.

Vlug, M. S., Wind, J., Hollmann, M. W., Ubbink, D. T., Cense, H. A., Engel, A. F., Gerhards, M. F., van Wagensveld, B. A., van der Zaag, E. S., van Geloven, A. A. W., Sprangers, M. A. G., Cuesta, M. A., & Bemelman, W. A. (2011). Laparoscopy in combination with fast track multimodal management is the best perioperative strategy in patients undergoing colonic surgery: a randomized clinical trial (LAFA-study). Annals of Surgery, 254(6), 868-875.

## ACCEPTED MANUSCRIPT

Vollmer, C. M., Sanchez, N., Gondek, S., McAuliffe, J., Kent, T. S., Christein, J. D., & Callery, M. P. (2012). Pancreatic Surgery Mortality Study Group. A root-cause analysis of mortality following major pancreatectomy. Journal of Gastrointestinal Surgery, 16(1), 89-103.

Walczak, S. (2008). Evaluating medical decision making heuristics and other business heuristics with neural networks. In G. Phillips-Wren, N. Ichalkaranje, & L. Jain (Eds.), Intelligent Decision Making: An AI-Based Approach (pp. 259-287). Berlin: Springer.

Walczak, S., Pofahl, W. E., & Scorpio, R. J. (2003). A decision support tool for allocating hospital bed resources and determining required acuity of care. Decision Support Systems, 34(4), 445-456.

Walczak, S., & Cerpa, N. (1999), Heuristic principles for the design of artificial neural networks. Information and Software Technology, 41(2), 107-117.

Wagner, M., Redaelli, C., Lietz, M., Seiler, C. A., Friess, H., & Büchler, M. W. (2004). Curative resection is the single most important factor determining outcome in patients with pancreatic adenocarcinoma. British Journal of Surgery, 91(5), 586-594.

Ware Jr, J. E. (2000). SF-36 health survey update. Spine, 25(24), 3130-3139.

Ware Jr, J. E., & Sherbourne, C. D. (1992). The MOS 36-item short-form health survey (SF-36): I. Conceptual framework and item selection. Medical Care, 30(6), 473-483.

Weinstein, J. N., Tosteson, T. D., Lurie, J. D., Tosteson, A., Blood, E., Herkowitz, H., Cammisa, F., Albert, T., Boden, S., Hilibrand, A., Goldberg, H., Berven, S., & An, H. (2010). Surgical versus nonoperative treatment for lumbar spinal stenosis four-year results of the Spine Patient Outcomes Research Trial (SPORT). Spine, 35(14), 1329-1338.

White, H. (1990). Connectionist nonparametric regression: Multilayer feedforward networks can learn arbitrary mappings. Neural Networks, 3(5), 535-549.

Yancik, R., Wesley, M. N., Ries, L. A., Havlik, R. J., Edwards, B. K., & Yates, J. W. (2001). Effect of age and comorbidity in postmenopausal breast cancer patients aged 55 years and older. Journal of the American Medical Association, 285(7), 885-892.

Yang, Y., Chen, H., Wang, D., Luo, W., Zhu, B., & Zhang, Z. (2013). Diagnosis of pancreatic carcinoma based on combined measurement of multiple serum tumor markers using artificial neural network analysis. Chinese Medical Journal, 127(10), 1891-1896.

Yeo, C. J., Abrams, R. A., Grochow, L. B., Sohn, T. A., Ord, S. E., Hruban, R. H., Zahurak, M. L., Dooley, W. C., Coleman, J., Sauter, P. K., & Pitt, H. A. (1997). Pancreaticoduodenectomy for pancreatic adenocarcinoma: postoperative adjuvant chemoradiation improves survival. A prospective, single-institution experience. Annals of Surgery, 225(5), 621-636.

Yet, B., Perkins, Z., Fenton, N., Tai, N., & Marsh, W. (2014). Not just data: A method for improving prediction with knowledge. Journal of Biomedical Informatics, 48, 28-37.

Ziebland, S., Chapple, A., & Evans, J. (2015). Barriers to shared decisions in the most serious of cancers: a qualitative study of patients with pancreatic cancer treated in the UK. Health Expectations, 18(6), 3302-3312.

Zhang, G. P. (2007). Avoiding pitfalls in neural network research. IEEE Transactions on Systems, Man, and Cybernetics, Part C (Applications and Reviews), 37(1), 3-16.

Zhang, M. M., Yang, H., Jin, Z. D., Yu, J. G., Cai, Z. Y., & Li, Z. S. (2010). Differential diagnosis of pancreatic cancer from normal tissue with digital imaging processing and pattern recognition based on a support vector machine of EUS images. Gastrointestinal Endoscopy, 72(5), 978-985.

Zhu, M., Xu, C., Yu, J., Wu, Y., Li, C., Zhang, M., Jin, Z., & Li, Z. (2013). Differentiation of pancreatic cancer and chronic pancreatitis using computer-aided diagnosis of endoscopic ultrasound (EUS) images: a diagnostic test. PLoS One, 8(5), e63820.

Zolbanin, H. M., Delen, D., & Zadeh, A. H. (2015). Predicting overall survivability in comorbidity of cancers: A data mining approach. Decision Support Systems, 74, 150-161.

Steven Walczak, Ph.D., is an Associate Professor of Health Information Sciences at the University of South Florida in the School of Information. His research interests are in applied artificial intelligence systems, particularly to solve medical domain problems.

Vic Velanovich, M.D., is the Division Director for Surgery in the Morsani College of Medicine at the University of South Florida. He is interested in gastrointestinal and oncological surgical research.

## List of Tables

Table 1. Recent (10 years) ANN pancreatic cancer diagnostic systems

Table 2. Real world results for study population based on treatment received (N=219)

Table 3. Pearson correlation values for SF-36 domain variables

Table 4. ANN results when missing one of the SF-36 domain variables in the input vector

Table 5. ANN results when missing combinations of SF-36 domain variables

## ACCEPTED MANUSCRIPT

Table 1. Recent (10 years) ANN Pancreatic Cancer Diagnostic Systems

<table><tr><td>Reference</td><td>Type of diagnostic aid</td><td>NN Training algorithm</td></tr><tr><td>(Chang and Hsu 2009)</td><td>direct prediction from patient data</td><td>backpropagation</td></tr><tr><td>(Das et al. 2008)</td><td>image analysis</td><td>backpropagation</td></tr><tr><td>(Gorunescu et al. 2011)</td><td>image analysis</td><td>backpropagation</td></tr><tr><td>(Qiong-ying et al. 2010)</td><td>protein biomarkers</td><td>backpropagation</td></tr><tr><td>(Säftoiu et al. 2008)</td><td rowspan="2">image analysis</td><td>multi-layer perceptron</td></tr><tr><td>(Säftoiu et al. 2012)</td><td>(backpropagation)</td></tr><tr><td>(Yang et al. 2013)</td><td>3 protein serum markers</td><td>unspecified</td></tr><tr><td>(Zhang et al. 2010)</td><td>image analysis</td><td>support vector machine</td></tr><tr><td>(Zhu et al. 2013)</td><td>image analysis</td><td>support vector machine</td></tr></table>

## ACCEPTED MANUSCRIPT

<table><tr><td></td><td>Survived 7 months</td><td>Died</td></tr><tr><td>No resection</td><td>50</td><td>44</td></tr><tr><td>Resection</td><td>88</td><td>37</td></tr></table>

Table 2. Real World Results for Study Population Based on Treatment Received (N=219)

Table 3. Pearson Correlation Values for SF-36 Domain Variables

<table><tr><td></td><td>PF</td><td>RP</td><td>RE</td><td>BP</td><td>VT</td><td>MH</td><td>SF</td><td>GH</td></tr><tr><td>PF</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>RP</td><td>0.555685</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>RE</td><td>0.497094</td><td>0.616197</td><td>1</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>BP</td><td>0.475787</td><td>0.582908</td><td>0.356616</td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>VT</td><td>0.672644</td><td>0.631822</td><td>0.56247</td><td>0.463769</td><td>1</td><td></td><td></td><td></td></tr><tr><td>MH</td><td>0.449469</td><td>0.324901</td><td>0.494599</td><td>0.362833</td><td>0.568208</td><td>1</td><td></td><td></td></tr><tr><td>SF</td><td>0.624996</td><td>0.67517</td><td>0.550555</td><td>0.576696</td><td>0.672883</td><td>0.492585</td><td>1</td><td></td></tr><tr><td>GH</td><td>0.569735</td><td>0.458763</td><td>0.480935</td><td>0.432736</td><td>0.619127</td><td>0.618939</td><td>0.542843</td><td>1</td></tr><tr><td>Count</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>&gt;0.60</td><td>2</td><td>3</td><td>1</td><td>0</td><td>4</td><td>1</td><td>3</td><td>2</td></tr></table>

## ACCEPTED MANUSCRIPT

Table 4. ANN Results When Missing One of the SF-36 Domain Variables in the Input Vector

<table><tr><td>Missing variable</td><td>Δ in Accuracy</td><td>Δ in Sensitivity</td><td>Δ in Specificity</td></tr><tr><td>PF</td><td>0</td><td>+4.82%</td><td>-15.39%</td></tr><tr><td>RP</td><td>+0.92%</td><td>+4.82%</td><td>-11.54%</td></tr><tr><td>RE</td><td>-3.67%</td><td>0</td><td>-15.39%</td></tr><tr><td>BP</td><td>-6.42%</td><td>-1.21%</td><td>-23.08%</td></tr><tr><td>VT</td><td>+0.92%</td><td>-1.21%</td><td>+7.69%</td></tr><tr><td>MH</td><td>-3.67%</td><td>-6.02%</td><td>+3.85%</td></tr><tr><td>SF</td><td>-6.42%</td><td>-4.82%</td><td>-11.54%</td></tr><tr><td>GH</td><td>-8.26%</td><td>-9.64%</td><td>-3.85%</td></tr></table>

## ACCEPTED MANUSCRIPT

Table 5. ANN Results When Missing Combinations of SF-36 Domain Variables

<table><tr><td>Missing variable</td><td>Δ in Accuracy</td><td>Δ in Sensitivity</td><td>Δ in Specificity</td></tr><tr><td>PF &amp; RP</td><td>-0.92%</td><td>+6.02%</td><td>-23.08%</td></tr><tr><td>PF &amp; VT</td><td>-7.34%</td><td>-7.23%</td><td>-7.69%</td></tr><tr><td>PF &amp; MH</td><td>-8.26%</td><td>-8.43%</td><td>-7.69%</td></tr><tr><td>RP &amp; VT</td><td>-5.51%</td><td>-4.82%</td><td>-7.69%</td></tr><tr><td>RP &amp; MH</td><td>-0.92%</td><td>-1.21%</td><td>0</td></tr><tr><td>VT &amp; MH</td><td>0</td><td>+1.20%</td><td>-3.85%</td></tr><tr><td>RP, VT, &amp; PF</td><td>-6.42%</td><td>-6.02%</td><td>-7.69%</td></tr><tr><td>RP, VT, PF, &amp; MH</td><td>-10.09%</td><td>-3.61%</td><td>-30.77%</td></tr></table>

## Research Highlights

 ANN developed to predict 7-month survival of pancreatic cancer patients.

 ANN achieves 91.30% sensitivity, 38.27% specificity, and overall accuracy of 71.69%.

 The ANN performs at least as well as Cox-regression and outperforms Coxregression on specificity.

 Treatment decision regret may be reduced for physicians and patients when using the ANN’s survival predictions.

## Endnotes

<sup>i</sup> The SF-36 short form survey is available at: https://www.rand.org/health/surveys\_tools/mos/36- item-short-form/survey-instrument.html for the interested reader.
