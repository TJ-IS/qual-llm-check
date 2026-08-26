---
otero_id: 4464
otero_key: "KW9BHKGB"
title: "Development of a structural equation modeling-based decision tree methodology for the analysis of lung transplantations"
authors: "Asil Oztekin; Zhenyu James Kong; Dursun Delen"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.12.004"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Development of a structural equation modeling-based decision tree methodology for the analysis of lung transplantations

Asil Oztekin <sup>a</sup>, Zhenyu James Kong <sup>a</sup>, Dursun Delen <sup>b,</sup>⁎

<sup>a</sup> School of Industrial Engineering and Management, Oklahoma State University, 322 Engineering North, Stillwater, OK 74078, USA

<sup>b</sup> Spears School of Business, Oklahoma State University, 700 N. Greenwood Ave., Tulsa, OK 74106, USA

## a r t i c l e i n f o

Article history: Received 25 August 2010 Received in revised form 22 November 2010 Accepted 7 December 2010 Available online 13 December 2010

Keywords: Lung transplantation UNOS Structural equation modeling PLS path model Decision trees

## a b s t r a c t

Lung transplantation has a vital role among all organ transplant procedures since it is the only accepted treatment for the end-stage pulmonary failure. There have been several research attempts to model the performance of lung transplants. Yet, these early studies either lack model predictive capability by relying on strong statistical assumptions or provide adequate predictive capability but suffer from less interpretability to the medical professionals. The proposed method described in this paper is focused on overcoming these limitations by providing a structural equation modeling-based decision tree construction procedure for lung transplant performance evaluation. Speci<sup>fi</sup>cally, partial least squares-based path modeling algorithm is used for the structural equation modeling part. The proposed method is validated through a US nation-wide dataset obtained from United Network for Organ Sharing (UNOS). The results are promising in terms of both prediction and interpretation capabilities, and are superior to the existing techniques. Hence, we assert that a decision support system, which is based on the proposed method, can bridge the knowledge-gap between the large amount of available data and betterment of the lung transplantation procedures.

© 2010 Elsevier B.V. All rights reserved.

## 1. Introduction

## 1.1. Motivation

Organ transplantation is regarded as a viable treatment for the chronic failure of major organs and is an inevitable option for the endstage pulmonary failure, namely lung patients [15]. Although lung transplantation is the accepted optimal treatment for eligible patients, the shortage of organs seriously limits this option. Additionally, a signi<sup>fi</sup>cant number of organs are rejected due to a suboptimal match between the donor and the recipient. Bene<sup>fi</sup>t-driven organ allocation schemes, where post-transplant outcome is taken into account as a performance criterion, are very attractive approaches because they are targeted at ensuring that organs are not wasted on patients who would not bene<sup>fi</sup>t from them [54]. Recently, the demand for organ transplantation has drastically increased whereas the number of donors has remained almost the same, which, in turn, caused longer lists of patients waiting for transplantation [51]. Therefore, outcome prediction (i.e. transplant success) has emerged as a critical issue in organ transplantation. Moreover, when a resource (the donor organ in this case) is scarce, the need for an accurate outcome prediction becomes acute [53]. Especially prediction of survival and the quality of life are clinically important but challenging problems [37]. However, the design of such schemes is very complex, even more dif<sup>fi</sup>cult to validate and to control the outcome of the transplantation [54]. Therefore, modeling such a system necessitates effective procedures for the selection of optimal organ recipients since currently it is not possible to satisfy all organ demands.

Voluminous data has been collected from lung transplant procedures and analyzed to evaluate the organ allocation process [46]. Attempts to analyze lung transplants with this huge amount of data have focused on identifying the characteristics of lung transplant recipients and their associated post-transplant outcomes [24]. However, they have not analyzed the allocation procedure in a cause-and-effect relationship perspective. To <sup>fi</sup>ll this gap, our study handles bene<sup>fi</sup>t-driven organ allocation schemes in terms of “causality” perspective because such a methodology would give clearer interpretability as well as a better prediction accuracy of the transplant success. While the former is extremely important to the medical professionals, the latter is critical to establish a satis<sup>fi</sup>cing optimal allocation scheme [52].

## 1.2. Related research

Numerous studies have focused on analyzing transplant processes in terms of statistical perspective [1,13,21,25,27,28,31,36,59]. They have mainly utilized Chi-square test, student's t-test, or Mann– Whitney U-test to compare the demographic and characteristic variables, pre-transplant, and intra-operative variables between arti<sup>fi</sup>cially-categorized patient groups (e.g. younger and older than a speci<sup>fi</sup>c age). Thereafter, they make use of conventional statistical prediction techniques such as Kaplan–Meier method, Mantel–Haenszel log-rank test, or traditional linear regression to predict patient (or graft) survivability after transplantation takes place. Molhazn et al. [39] examined the perceived quality of life (QOL) of patients with end stage renal disease by incorporating patients' medical characteristics, their health status, functional status, ability to work, and ability to perform activities. Signi<sup>fi</sup>cant direct effects of these variables on QOL were determined. Smith et al. [55] conducted a survey to reveal whether or not quality of life and health status are distinct constructs. Using three functioning domains (mental, physical, and social) they found out that these two are different measures and hence, should be analyzed through separate questionnaires. Devins et al. [17] devised a novel scale named illness intrusiveness ratings scale (IIRS) by pooling responses from separate studies concerning quality of life in renal, heart, liver, and lung transplants among many others. The study was aimed at investigating the factor structure underlying the IIRS. By using exploratory and con<sup>fi</sup>rmatory factor analyses in a step-by-step fashion, they <sup>fi</sup>rst identi<sup>fi</sup>ed the factor structure and then con<sup>fi</sup>rmed it against various patient groups (i.e. renal, heart, lung transplants and etc.). Two more recent studies [9,20] have analyzed the quality of life after liver transplant as well as chronic heart failure, respectively. Castaldo et al. [9] examined the effect of preoperative and postoperative factors on the model for end-stage liver disease (MELD score), which is mainly used for organ allocation decisions by predicting short-term mortality of patients. This research has revealed that increasing MELD score can be attributed to improved physical healthrelated QOL (HRQOL) whereas it does not have an association with mental HRQOL. On the other hand, Faller et al. [20] focused on the chronic heart failure patients with the question whether depression affects only the psychological domain of patients' HRQOL or it is broader and may affect the physical domain of HRQOL. The analysis results suggest that the depression has an independent impact on both physical and psychological domains of HRQOL in patients with chronic heart failure while the heart failure severity affects only physical HRQOL. These initial studies in the medical <sup>fi</sup>eld [9,17,20,39,55] utilize structural equation modeling technique but they rely on limited source of data records collected through surveys/ questionnaires rather than a nation-wide dataset. Structural equation modeling (SEM) is a statistical technique that is able to examine causal variables [33]. In SEM, data is handled differently from the conventional statistical techniques such as multiple regression. The parameters of the SEM model refer to connection strengths or path coef<sup>fi</sup>cients between different variables. An algorithm that minimizes the difference between the observed covariance and that presented by a structural/path model is employed to estimate the SEM model parameters [38]

The integration of the factor analysis and the regression can be referred to as structural equation modeling [38]. SEM is aimed at simultaneously expressing the relationship of a set of latent (unobserved) constructs, each measured by one or more observed variables (OVs). The observed variables are directly collected from test participants through data collection methods. In contrast to this situation, latent variables are theoretical and/or conceptual and are not directly observed. Instead, they are causally related to the observed variables, and hence can only be calculated as a combination of their corresponding OVs. Examples of latent constructs could be usability index, customer satisfaction, or quality. In conducting SEM, the latent variables are grouped as exogenous and endogenous constructs. The causal relationship between the endogenous and exogenous constructs is explained by linear regression equations. The fundamental difference between factor analysis and SEM modeling is that in factor analysis the observed variables can load on any factors (constructs). This is also referred to as explanatory factor analysis. Yet, when using SEM, the observed variables can load only on particular <sup>fi</sup> in advance based on the domain knowledge, which is also known as con<sup>fi</sup>rmatory factor analysis. SEM is especially preferable if one dependent variable affects another dependent variable at the same time as well. Also, SEM is an effective modeling technique in handling multi-collinearity. These advantages make SEM more powerful than factor analysis and multiple linear regression. Therefore, it has been widely used in the information systems (IS), information technology (IT), and operations management (OM) areas [2,3,41,43,60], yet have not been very popular in the medical <sup>fi</sup>eld as widely.

Although abovementioned studies reveal very useful initial knowledge for the organ transplantation <sup>fi</sup>eld based on the classical statistical assumptions adopted, they still have some limitations as follows: (1) They implicitly ignore the fact that the predictive variables may not necessarily be independent of each other. On the contrary, they mostly do affect each other. These predictor variables can be categorized into higher level classes as a group which they refer to. (2) Following the <sup>fi</sup>rst explanation, grouped and aggregated variables may have a nonlinear relationship and/or additive interaction effects with the outcome measures of the transplant. However, such features cannot be revealed through the existing methods. (3) In the state-of-the-art, transplant performance measure is evaluated based on a single metric. The transplant success should not be a single metric to be predicted (e.g. only survival time) to satisfy various bene<sup>fi</sup>ts of the organ allocation. Instead, it should be the combination of various metrics (e.g. survival time, quality of life, and etc.).

## 1.3. The organization of the paper

In order to address the abovementioned limitations, this paper proposes a structural equation model-based decision tree for analyzing lung organ transplant success. The paper is organized as follows. In Section 2, the proposed research methodology is presented in details, which consists of a <sup>fi</sup>ve-step procedure. For comparison purpose, an existing method (i.e. universal structure modeling) is brie<sup>fl</sup>y introduced as well. Section 3 presents the case study and the results of our methodology. A comparison of the proposed method and the existing methods is also presented. Section 4 concludes the study along with managerial implications and potential future research directions.

## 2. Proposed methodology

The related research work summarized in Section 1.2 studied the organ transplant success by using the data obtained through the patient surveys. Such an approach broadens the scope of voluminous datasets to a small set of predictors by bringing the previous data collection efforts to naught. Also, the relationships among the aggregated constructs are limited to linearity which may not hold true in reality. Although structural equation modeling presents a clear depiction of causality, it lacks prediction accuracy since it is a modeltesting approach rather than a prediction method. That is, there is a trade-off between model prediction accuracy and interpretability. In order to better handle this trade-off, we propose a structural equation modeling-based decision tree construction. Such a method can identify the causality with high prediction accuracy. Thus, it would satisfy the medical professionals by its clear interpretability and predictability for a bene<sup>fi</sup>t-driven allocation scheme considering the expected transplant success.

In this study, taking the <sup>fi</sup>ndings of our previous work [16,42] into account we chose 27 variables from the UNOS database to predict the transplant success. In the previous work, data mining-based survival analysis methodology was conducted to select this subset of variables. Among these 27 variables, GTIME (graft lifespan from transplant to death) and FUNC\_STAT\_TRF (functional status after the transplant) re<sup>fl</sup>ect the success rate of the organ transplantation. GTIME is a continuous variable which refers to the graft survival time after the

transplant. FUNC\_STAT\_TRF is an ordinal categorical variable which indicates the functional status of the patient after the transplant. (Note that although more variables could have been utilized to model the transplant success, in this study we are restricted by these two, which were the only outcome measures provided by UNOS dataset as described in Section 2.1). Hence, these two variables will be combined to create the performance measure, namely transplant success for organ transplantation in this study. This relationship is shown by Model 1 in Fig. 1. The remaining 25 variables are considered as the causal indicators, which are associated with the three main determinative factors used by the medical professionals to model the organ transplantation. These 25 variables are listed in Table 1 along with their brief explanations. Three determinative factors include (1) recipient's profile, (2) donor's profile, and (3) match level. Although these three determinative factors cannot be found from the UNOS database directly, they are related to the 25 variables chosen from the database. The mapping between these three determinative factors and the 25 variables from the UNOS database is constructed based on our discussions with the medical experts in the organ transplantation area. Their quantitative relationship can be obtained using formative modeling which is explained in Section 2.2.1. Thus, we also call these three determinative factors as composite variables. We can consider that these three determinative factors are in fact the composite variables hidden behind the 25 causal indicators. These composite variables and their underlying causal indicators are pictorially summarized as Model 2 in Fig. 1. Note that in this study latent composite variables are always written in lower case to discriminate them from their corresponding causal indicators (all of which are written in upper case). To model the underlying causal relationship between these three determinative factors and their corresponding 25 causal indicators and between transplant success and its items (GTIME and FUNC\_STAT\_TRF), we use partial least squares (PLS) path modeling technique because it allows to construct the formative models (as well as re<sup>fl</sup>ective relations), both of which are required in this study. In mapping these 25 causal indicators with their constructs, medical experts from the Integris Nazih Zuhdi Transplant Institute were also consulted. In formative modeling, the causal indicators affect their corresponding composite variable as shown in Model 2 of Fig. 1. In other words, in formative modeling the composite variable would be constituted and caused by its causal indicators. In contrast, in re<sup>fl</sup>ective modeling the latent variable drives its indicators. In other words, the indicators are affected by their latent variables. To exemplify, referring to Model 1 in Fig. 1 if the transplant has been conducted successfully (referring to transplant success), the patient would live for a long time (referring to GTIME) with a high quality of life (referring to FUNC\_STAT\_TRF). On the other hand, referring to Model 2 of Fig. 1, for example recipient's profile can be determined by considering his/her age, medical condition before the transplant, weight and etc. Finally, the model that discloses the relationship between the three determinative factors with the organ transplantation performance variable (i.e. transplant success) is developed using the decision tree predictive approach, which is shown as Model 3 in Fig. 1. The details regarding these relations through Model 1 and Model 2 are presented in Section 2.2.1. Using Model 2 results as inputs and Model 1 result as output, Model 3 would construct a decision tree prediction model, which is explained in Section 2.2.2

Based on the three models shown in Fig. 1, we propose a <sup>fi</sup>ve-step approach which is depicted in Fig. 2 to achieve interpretability and predictability simultaneously.

The <sup>fi</sup>rst step in the methodology is to prepare the dataset to be used in further modeling. The second step is to create the measurement model explaining the cause-and-effect relation between the latent/composite variables and their corresponding indicators as shown in Fig. 1 (Model 1 and Model 2). In the second step, medical experts' opinion is also consulted. Then the composite scores for each latent/composite variable can be calculated through the measurement models as a third step. In the third step, re<sup>fl</sup>ective models can be estimated through Eqs. (a1–a3) and formative models can be estimated as in Eq. ((b) referring to models (a) and (b) in Fig. 2.

$$
x _ {1} = \pi_ {1 0} + \pi_ {1} \xi_ {1} + \varepsilon_ {1}\tag{a1}
$$

$$
x _ {2} = \pi_ {2 0} + \pi_ {2} \xi_ {1} + \varepsilon_ {2}\tag{a2}
$$

$$
x _ {3} = \pi_ {3 0} + \pi_ {3} \xi_ {1} + \varepsilon_ {3}\tag{a3}
$$

$$
\xi_ {1} = \beta_ {1} x _ {1} + \beta_ {2} x _ {2} + \beta_ {3} x _ {3} + \delta_ {1}\tag{b}
$$

The details of these re<sup>fl</sup>ective and formative measurement models will be further explained in Section 2.2.1. The composite scores are then normalized to an interval of [0–1] as the fourth step. The <sup>fi</sup>fth step is to implement decision tree construction by using the composite scores of the latent/composite variables as the predictors/ inputs and the performance variable, namely transplant success, as output. Employing a decision tree model between the three determinative factors and the transplant success would hypothetically capture the nonlinear and interaction effects lying under the data. These steps are presented in Sections 2.1 and 2.2 in detail.

![](/api/attachments/KW9BHKGB/fulltext/images/001a042589a26eb0e07875ef1faf47ac47aff2ce8cebb92a3c66692b6fb11545.jpg)  
Fig. 1. Causal relationships diagram for the proposed modeling.

Table 1  
Explanation of indicators and their corresponding composite variables.

<table><tr><td>Indicators</td><td>Explanation</td><td>Variable type</td><td>Composite variable</td></tr><tr><td>AGE</td><td>Recipient&#x27;s age (years)</td><td>Continuous</td><td>Recipient&#x27;s profile</td></tr><tr><td>DAYSWAITCHORN</td><td>Active days on waiting list</td><td>Continuous</td><td></td></tr><tr><td>FUNC_STAT_TRR</td><td>Recipient functional status @ transplant</td><td>Ordinal</td><td></td></tr><tr><td>HGT_CM_TRR</td><td>Recipient height @ transplant</td><td>Continuous</td><td></td></tr><tr><td>MED_COND_TRR</td><td>Recipient medical condition pre-transplant @ transplant</td><td>Ordinal</td><td></td></tr><tr><td>STERNOTOMY_TRR</td><td>Events occurring between listing and transplant: sternotomy</td><td>Ordinal</td><td></td></tr><tr><td>WGT_KG_TRR</td><td>Recipient weight (kg) @ transplant</td><td>Continuous</td><td></td></tr><tr><td>ABO_MAT</td><td>Donor-recipient ABO match level</td><td>Ordinal</td><td>Match level</td></tr><tr><td>AMAT</td><td>A locus match level</td><td>Ordinal</td><td></td></tr><tr><td>BMAT</td><td>B locus match level</td><td>Ordinal</td><td></td></tr><tr><td>DRMAT</td><td>DR locus match level</td><td>Ordinal</td><td></td></tr><tr><td>EINT</td><td>Ethnicity interaction between donor and recipient</td><td>Binary</td><td></td></tr><tr><td>GINT</td><td>Gender interaction between donor and recipient</td><td>Binary</td><td></td></tr><tr><td>HLAMAT</td><td>HLA match level</td><td>Ordinal</td><td></td></tr><tr><td>AGE_DON</td><td>Donor age (years)</td><td>Continuous</td><td>Donor&#x27;s profile</td></tr><tr><td>HGT_CM_DON</td><td>Donor height (cm)</td><td>Continuous</td><td></td></tr><tr><td>HIST_ALCOHOL_OLD_DON</td><td>Deceased donor-history of alcohol dependency</td><td>Binary</td><td></td></tr><tr><td>HIST_CANCER_DON</td><td>Deceased donor-history of cancer</td><td>Binary</td><td></td></tr><tr><td>HIST_CIG_DON</td><td>Deceased donor-history of cigarettes in past</td><td>Binary</td><td></td></tr><tr><td>HIST_COCAINE_DON</td><td>Deceased donor-history of cocaine use in past</td><td>Binary</td><td></td></tr><tr><td>HIST_DIABETES</td><td>Deceased donor-history of diabetes</td><td>Binary</td><td></td></tr><tr><td>HIST_HYPERTENS_DON</td><td>Deceased donor-history of hypertension</td><td>Binary</td><td></td></tr><tr><td>HIST_IV_DRUG_DON</td><td>Deceased donor-history of IV drug use in past</td><td>Binary</td><td></td></tr><tr><td>HIST_MI</td><td>Deceased donor-history of previous Myocardial Infarction</td><td>Binary</td><td></td></tr><tr><td>WGT_KG_DON</td><td>Donor weight (kg)</td><td>Continuous</td><td></td></tr></table>

## 2.1. Data source and data preparation

In this study, the data source used to validate the proposed method was lung organ transplant dataset provided by UNOS (United

Network for Organ Sharing), which is a tax-exempt, medical, scienti<sup>fi</sup>c, and educational organization that operates the national Organ Procurement and Transplantation Network under the contract to the Division of Organ Transplantation of the Department of Health and Human Services [26]. The data <sup>fi</sup>les were obtained from UNOS using a formal data requisition procedure (which includes submission of speci<sup>fi</sup>c data needs, purpose of the study, and a data use agreement). These data <sup>fi</sup>les are named as UNOS Standard Transplant Analysis and Research (STAR) <sup>fi</sup>les for heart, lung, and simultaneous heart-lung transplants. Each transplant STAR <sup>fi</sup>le consists of information on all lung transplants that had been performed in the US and reported to UNOS since October 1, 1987. It includes both deceasedand living-donor transplants. None of the <sup>fi</sup>les include any speci<sup>fi</sup>c patient or transplant hospital identi<sup>fi</sup>ers due to the privacy and security issues. However, there is a patient identi<sup>fi</sup>cation number, unique to each patient, which allows linking multiple <sup>fi</sup>les and tracking the patient. Considering these features, UNOS's data <sup>fi</sup>les are perceived to be the most comprehensive source of information available in any single <sup>fi</sup>eld of medicine and for organ transplantation in US [14].

![](/api/attachments/KW9BHKGB/fulltext/images/03927ddb8d7cdaeb61db4fd5a3692248e1119c53c2e157b258ec8fde10966435.jpg)  
Fig. 2. Steps of the proposed method.

There are two datasets involved in our study, which are regular dataset and follow-up dataset. The regular dataset contains all information of donors and recipients before transplantation occurred, and the follow-up dataset provides all information of donors and recipients after the transplantation. The TRR\_ID variable (transplant identi<sup>fi</sup>er) is the common variable between these two datasets and the one which is proposed by UNOS to merge and integrate these two datasets. Therefore, we combined these two datasets (i.e. regular and follow-up) in a relational database environment using the link (a.k.a. primary key) of TRR\_ID.

Overall, the complete dataset consisted of 16,771 records and 442 variables. These variables include the socio-demographic and healthrelated factors with regard to both the donor and the recipients. There are also procedure-related factors among the dataset. To assign indicators of transplant success, there were four possible variables which are called PSTATUS, PTIME, GSTATUS, and GTIME. Whether or not the patient died after the transplantation took place is referred to as PSTATUS (with dead=1 and alive=0). A very similar variable was GSTATUS, referring to whether or not graft has failed (1 denoting “failed” and 0 denoting “succeeded”). The variable PTIME denotes patient follow-up time (in days) from transplant to death time. Similarly, GTIME is explained as graft lifespan from transplant to death time. Since the goal of this study is to develop models that predict the transplant success solely based on the lung transplant, one of the indicators of the transplant success was assigned as GTIME. This assignment was done to discriminate the patients who died solely due to the lung graft incompatibility from the ones who died from other reasons. Therefore, the rest of the potential variables (PSTATUS, PTIME, and GSTATUS) were eliminated from the dataset. To be able to claim that a transplant has been conducted successfully, namely a sati<sup>fi</sup>cing match has been performed. not only the length of survival after transplant but also how well the recipient feels after the transplant should be considered. This is referred to as functional status (i.e. ability to work and ability to perform activities of daily living) or as “quality of life” [39]. Hence, in addition to GTIME we incorporated FUNC\_STAT\_TRF variable (functional status after the transplant, which is an ordinal variable) as a causal indicator of the transplant success. The causal indicators of the other composite variables, their de<sup>fi</sup>nitions, and variable types in UNOS dataset are tabulated in Table 1.

UNOS dataset also included some identi<sup>fi</sup>cation variables (e.g., Donor ID) which help track the recipient patient anonymously, identify the lung transplant procedure, or link records from multiple data <sup>fi</sup>les to each other. Since these types of identi<sup>fi</sup>cation variables do not have any information content related to the prediction capability of the models, after linking and integrating the <sup>fi</sup>les they were excluded from the analysis dataset. Moreover, the name of transplantation type was recorded in the dataset as a variable named “Dataset” which had only one value (TH, referring to thoracic) and the date of data processing is recorded as a variable named “Date of Run” both of which are useful for data integration purposes but has no information to contribute to the prediction and interpretation and, hence are also excluded from the analysis dataset. Similarly, other variables having only one possible value for all records in the dataset are also eliminated from the predictive modeling since they do not have any variability.

This dataset had excessive number of missing values which render some of the records and variables seemingly unusable. Case-wise deletion method excludes all records (cases) that have missing data in at least one of the selected variables [4]. We applied this method considering the 27 indicators as our reference in hand, which ended up with 6512 records. Instead of other missing value imputation techniques, this technique was purposefully implemented here mainly because a sample size of 6512 is satisfactory considering the fact that the PLS-based path analysis can be conducted with relatively small sample sizes [29]. As a general rule of thumb, Chin and Newsted [10] suggested using a minimum sample size of ten times the maximum number of paths aiming at any latent/composite variable in the PLS path model, which renders 6512 records far beyond this heuristic threshold value for our model.

## 2.2. Structural equation modeling-based decision tree construction

The structural equation model can be described by two models: (1) a measurement (a.k.a outer) model explaining the relationship between the observed variables (already existing variables in the UNOS database for our case) and their corresponding composite/ latent variables. (2) a structural (a.k.a inner) model explaining the relationship between some (or all) of the composite/latent variables (i.e. the determinative factors such as recipient's pro<sup>fi</sup>le to predict transplant performance) with other composite/latent variables (i.e. the transplant performance variable, transplant success). What follows next in Section 2.2.1 is a short description of these models with a partial least squares path modeling algorithm summarized from Tenenhaus et al. [58].

## 2.2.1. The measurement (outer) model

A latent variable ξ is an unobservable variable (a.k.a. construct, component or composite variable) which is indirectly described by a set of observable variables (x ) (a.k.a. indicators). There are two ways of explaining the relationship between the latent/composite and observable variables: re<sup>fl</sup>ective and formative models.

2.2.1.1. Reflective modeling of transplant success (Model 1 in Fig. 1). In re<sup>fl</sup>ective model, the latent variable is assumed to underlie or cause its related causal indicators (observable variables). Each is attributed to its latent variable by a simple linear regression as in Eq. (1).

$$
x _ {h} = \pi_ {h 0} + \pi_ {h} \xi + \varepsilon_ {h}\tag{1}
$$

where $x _ { h }$ is the causal indicator, $\pi _ { h 0 }$ is the constant intercept, $\pi _ { h }$ is the item loading, ξ is the latent variable, and $\varepsilon _ { h }$ is the measurement error/ residual. The index h refers to the hth causal indicator which would be related to its latent variable. Here ξ has a mean of m and a standard deviation of one. It is interpreted as each causal indicator $x _ { h }$ re<sup>fl</sup>ects its latent variable ξ. Eq. (1) is solved based on the main assumption that the residual $\varepsilon _ { h }$ has a zero mean and is uncorrelated with the latent variable ξ. This is called the predictor speci<sup>fi</sup>cation condition and is shown by Eq. (2).

$$
E (x _ {h} | \xi) = \pi_ {h 0} + \pi_ {h} \xi\tag{2}
$$

In this study, the latent variable transplant success affects its causal indicators, namely GTIME and FUNC\_STAT\_TRF. Considering Fig. 1, these re<sup>fl</sup>ective models can be formed and predicted as shown by Eqs. (3) and (4).

$$
G T I M E = \pi_ {1 0} + \pi_ {1} * \text { TransplantSuccess } + \varepsilon_ {1}\tag{3}
$$

$$
F U N C \_ S T A T \_ T R F = \pi_ {2 0} + \pi_ {2} * T r a n s p l a n t S u c c e s s + \varepsilon_ {2}\tag{4}
$$

2.2.1.2. Formative modeling for the predictors of the transplant success (Model 2 in Fig. 1). In this model, it is assumed that the composite variable is formed or caused by its causal indicators. The composite variable is a linear function of its causal indicators plus a residual term as shown in Eq. (5).

$$
\xi_ {k} = \sum_ {h} \beta_ {k h} x _ {k h} + \delta_ {k}\tag{5}
$$

where $\beta _ { k h }$ is the regression weight and $\delta _ { k }$ is the residual error. The subscripts kh refer to the kth composite variable with its hth causal indicator in sequence. Note that for formative models ‘composite variable’ is the preferred generic term instead of ‘latent variable’.

Eq. (5) is solved under the assumption that the residual vector $\delta _ { k }$ has a zero mean and is uncorrelated with the indicators $x _ { h } .$ This assumption is called the predictor speci<sup>fi</sup>cation condition and hypothesized by Eq. (6).

$$
E \Big (\xi | x _ {1}, \dots , x _ {p _ {j}} \Big) = \sum_ {h} \beta_ {h} x _ {h}\tag{6}
$$

Referring to Fig. 1 and Table 1, the three formative models of this study corresponding to the composite variables recipient's profile, donor's profile, and match level can be constructed as in Eqs. (7.1)– (7.3), respectively.

$$
R e c i p i e n t ^ {\prime} s P r o f i l e = \beta_ {1 1} * A G E + \dots + \beta_ {1 7} * W G T \_ K G \_ T R R + \delta_ {1}\tag{7.1}
$$

$$
\begin{array}{c} D o n o r ^ {\prime} s P r o f i l e = \beta_ {2 1} * A G E \_ D O N + \ldots + \beta_ {2 (1 1)} \\ * W G T \_ K G \_ D O N + \delta_ {2} \end{array}\tag{7.2}
$$

$$
\text { Match   Level } = \beta_ {3 1} * A M A T + \dots + \beta_ {3 7} * H L A M A T + \delta_ {3}\tag{7.3}
$$

Note that the simultaneous use of numerical and categorical variables for measurement (outer) models is well-established in PLS path modeling literature [30,57], and hence the construction of Eqs. (3), (4), and (7.1)–(7.3) is allowable in our case. Since the indicators were on different measurement scales, we implemented a scale transformation as in Eq. (8) so as to have an interpretable reference scale to compare the individual scores to each other.

$$
\begin{array}{l} x _ {h (n e w)} = \frac {x _ {h (o l d)} - x _ {m i n (o l d)}}{x _ {m a x (o l d)} - x _ {m i n (o l d)}} \Big (x _ {\text { desired\_max(new)}} - x _ {\text { desired\_min(new)}} \Big) \\ + x _ {\text { desired\_min(new)}} \end{array}\tag{8}
$$

The next step is to estimate the standardized composite variables $y _ { k }$ (given by $y _ { k } { = } \xi _ { k } { - } m _ { k } )$ . The unstandardized composite variable $\xi _ { \mathrm { k } }$ and its mean $m _ { k }$ are estimated by Eqs. (9) and (10), respectively.

$$
\hat {\xi} _ {\mathrm{k}} = \sum \tilde {\beta} _ {k h} x _ {k h}\tag{9}
$$

$$
\hat {m} _ {k} = \sum \tilde {\beta} _ {k h} \bar {x} _ {k h}\tag{10}
$$

where $\tilde { \beta } _ { k h }$ refers to the estimated regression weight between the kth composite variable with its hth causal indicator and $x _ { k h }$ is the mean of the hth causal indicator that loads onto the kth composite variable. By using Eqs. (9) and (10), the standardized composite variables y can then be estimated as combinations of their causal indicators as shown in Eq. (11).

$$
y _ {k} = \sum \tilde {\beta} _ {k h} \left(x _ {k h} - \bar {x} _ {k h}\right)\tag{11}
$$

2.2.2. The structural (inner) model (Model 3 in Fig. 1)

In conventional structural equation modeling, the structural model is composed of linear equations relating the latent variables with other latent variables. This is formulated as in Eq. (12).

$$
\xi_ {j} = \beta_ {j 0} + \sum_ {i} \beta_ {j i} \xi_ {i} + v _ {j}\tag{12}
$$

where $\xi _ { j }$ is the latent/composite variable that has a path from another latent/composite variable, i.e. $\xi _ { i } . \beta _ { j 0 }$ is the constant intercept, $\beta _ { j i }$ is the path coef<sup>fi</sup>cient from ξ to $\xi _ { j } ,$ and $\nu _ { j }$ is the residual error. Although this modeling approach is very powerful in terms of causality explanation, it relies on a strong assumption that the relationships among the latent/composite variables are linear. Therefore, for the structural model part we propose to employ decision trees which are effective nonlinear data mining techniques. The composite scores of the latent/ composite variables can be calculated by the re<sup>fl</sup>ective and formative modeling as explained in Section 2.1.1. These normalized composite scores are then used to construct the decision tree to predict the transplant success. This proposed structural model with decision treebased construction should hypothetically be more effective than a linear regression-based structural model since it is capable of revealing the nonlinear relationships.

Decision trees recursively split the data in branches according to a preset criterion (e.g. information gain) to maximize the prediction accuracy resulting in a tree-like structure [48]. To achieve this, they use mathematical algorithms (such as information gain, Gini index, and Chi-squared test) to identify a pair of variable and its threshold that splits the input observation into two or more subgroups. This step is repeated at each leaf node until the complete tree is constructed. The objective of the splitting algorithm is to <sup>fi</sup>nd a variable–threshold pair that maximizes the homogeneity (order) of the resulting two or more subgroups of samples. Popular decision tree algorithms include Quinlan's ID3, C4.5, C5, M5 [47–49], Breiman et al.'s CART [6], and CHAID introduced by Kass [34]. Compared with other machine learning methods, decision trees have the advantage that they are explicit models (as opposed to black box models) and hence can easily be interpreted and summarized as rules. This advantage makes decision trees widely used in medicine [18]. If the dependent (output) variable is categorical or ordinal, the decision tree is speci<sup>fi</sup>cally called classi<sup>fi</sup>cation tree; if the dependent variable is continuous (as in our case) the resulting decision tree is called regression tree. Regression trees are one of a group of relatively <sup>fl</sup>exible and computer-intensive statistical techniques [19]. These methods use repeated re-sampling of the data to develop empirical sampling distributions of the relevant statistics in place of the more restrictive distributional assumptions in classical statistical methods. Popular regression trees are CART, CHAID, and M5 all of which can be used as classi<sup>fi</sup>cation and regression trees. Based on the favorable prediction results we have obtained from preliminary runs in our case study, we chose to use CART algorithm as the regression tree method.

2.3. Universal structure modeling: Bayesian neural networks-based PLS path modeling

As a benchmark to our methodology, we compare and contrast our case study results with the universal structure modeling (USM) which was developed by Buckler and Hennig-Thurau [7,8]. The reason that USM was chosen in this study as a benchmark is that it does capture the nonlinearity perfectly and hence achieves high prediction accuracy, yet it lacks interpretability since it uses a black-box model, namely neural networks. Additionally, it requires high computational time to reveal potential nonlinear and latent variable interaction effects on each other through the bootstrapping method. What follows next is a short description of USM. Similar to our approach, the USM also limits the nonlinear relations only to the structural model and it assumes that the measurement model part is linear. In other words, measurement model portion of USM is the same as described in Section 2.2.1. As for the structural model, USM substitutes the linear least squares regression with Bayesian neural networks. This enables the model to discover unproposed structural paths, nonlinearity, and interaction effects. The estimator ξ̂ of the latent variable ξ is de<sup>fi</sup>ned as the output of multilayer perceptron (MLP) architecture and shown as in Eq. (13).

$$
\widehat {\xi} ^ {j} = f _ {A c t 2} \left(\sum_ {h = 1} ^ {H} w _ {h}. f _ {A c t 1} \left(\sum_ {i = 1} ^ {I} w _ {i h}. S _ {i} ^ {j}. \xi^ {i} + b _ {1 h}\right) + b _ {2}\right)\tag{13}
$$

where $f _ { A c t 1 }$ is the activation function of the hidden neural units and $f _ { A c t 2 }$ is the output neural unit. H is the number of hidden neural units, I is the number of latent input variables ξ, w's are the weights and b's are the biases for the neural network. S<sup>j</sup> is the apriori likelihood that a variable i in<sup>fl</sup>uences another variable j. To prevent the over<sup>fi</sup>tting in the neural network model, USM minimizes the error function E for each latent variable i of the structural model. E refers to the overall error of the respective variable's neural network and shown as in Eq. (14).

$$
E _ {i} = \beta . \sum_ {n = 1} ^ {N} \left(\widehat {\xi_ {t - 1 , n} ^ {i}} - \widehat {\xi_ {t , n} ^ {i}}\right) ^ {2} + \sum_ {h = 1} ^ {H} \alpha_ {t, h}. \sum_ {p = 1} ^ {P} w _ {p h} ^ {2}\tag{14}
$$

where n refers to the individual cases, N is the total number of cases, and p is the index for the weights, w. On the other hand, <sup>i</sup> is the conditional estimate of the latent variable i in the current estimation step, t, calculated from the structural model by the Bayesian neural network, and $\boldsymbol { \xi } _ { t - 1 , n } ^ { i }$ is the estimate of the previous iteration for the same latent variable. If the case is the <sup>fi</sup>rst step for this estimation, $\xi _ { t - 1 , n } ^ { i }$ would then refer to the initial composite score received from the measurement model. The hyperparameters α and β prevent over<sup>fi</sup>tting of the neural network model. They are updated in every iteration of the learning process and are given by Eqs. (15) and (16).

$$
\alpha_ {h} = \frac {\gamma}{2 \sum_ {n = 1} ^ {N} w _ {n h} ^ {2}}\tag{15}
$$

$$
\beta = \frac {N - \gamma}{2 \sum_ {n = 1} ^ {N} \left(\xi_ {n} ^ {i} - \widehat {\xi_ {n} ^ {i}}\right) ^ {2}}\tag{16}
$$

where N is the total number of records and $\begin{array} { r } { \gamma = \sum _ { p = 1 } ^ { P } { \frac { \lambda _ { p } } { \lambda _ { p } \ + \ \alpha _ { L - 1 } } } . \lambda _ { p } } \end{array}$ are the eigenvalues of the Hessian matrix of the error function in Eq. (14) and $\alpha _ { L I } .$ <sub>1</sub> is the hyperparameter α from the previous learning iteration.

## 3. Case study results and discussion

To con<sup>fi</sup>rm the measurement model and determine the composite scores of the latent and composite variables, SmartPLS<sup>®</sup> software [50] was used. It is a component-based structural equation modeling software which implements partial least squares estimation in contrast to the covariance-based technique such as Lisrel<sup>®</sup> [32]. PLS was preferred in this study because it does not place much importance on the sample size and data distribution assumptions [11]. Additionally, it can handle the formative measurement models which are required in our approach. The results for the re<sup>fl</sup>ective part of the model, namely the part of the model pertaining to transplant success (Model 1 in Fig. 1) are presented in Table 2.

Internal consistency, reliability, and convergent validity measures.

<table><tr><td>Latent variable</td><td>CR</td><td>Cronbach&#x27;s alpha</td><td>AVE</td><td>Items and their loadings</td></tr><tr><td>Transplant success</td><td>0.736</td><td>0.728</td><td>0.699</td><td>GTIME → 0.841FUNC_STAT_TRF → 0.994</td></tr></table>

Composite reliability (CR) is a criterion of scale reliability. It can assess the internal consistency of the item and is given by Eq. (17) following the same parameters from Eq. (1) [22].

$$
C R _ {\xi_ {h}} = \frac {\left(\sum \pi_ {h}\right) ^ {2}}{\left(\sum \pi_ {h}\right) ^ {2} + \sum \xi_ {h}}\tag{17}
$$

On the other hand, Cronbach's alpha measures the extent to which the observable variables can explain their corresponding latent variable and is also supportive reliability measurement criterion [44]. For this latent variable (transplant success) CR measure was found to be 0.736 and Cronbach's alpha was 0.728, both of which pass the widely accepted threshold value of 0.7 [61]. These two measures ensure that this latent variable is internally consistent i.e. reliable and stable. On the other hand, to check the convergent validity of the latent variables the average variance extracted (AVE) should be calculated as in Eq. (18).

$$
\mathrm{AVE} = \frac {\sum \pi_ {h} ^ {2}}{\sum \pi_ {h} ^ {2} + \sum 1 - \pi_ {h} ^ {2}}\tag{18}
$$

AVE should exceed the 0.5 threshold value as a rule-of-thumb [61], which was 0.699 in our results for the latent variable, transplant success. Also, all item loadings should be at least 0.70 and were observed to be 0.841 for GTIME and 0.994 for FUNC\_STAT\_TRF in our analysis.

The measurement models pertaining to the three composite variables, i.e. recipient's pro<sup>fi</sup>le, donor's pro<sup>fi</sup>le, and match level (Model 2 in Fig. 1) are constructed by formative models because all item measures are independent of one another and are viewed as items that constitute their corresponding composite variables. In formative model cases, abovementioned internal consistency, reliability, and convergent validity criteria (i.e. Cronbach's alpha, CR, and AVE) are not deemed appropriate [12,23]. In assessing formative models, Petter et al. [45] place great importance on prior data collection phase and rather propose to assess content validity essentially by “evaluating if the set of indicators under-specify the domain of the construct based on explicated facets in the theory base”. For formative models, PLS weights represent a comparable effect of indicators on composite variables [5]. Construct validity can be assessed by eliminating the non-signi<sup>fi</sup>cant items in expense of losing the content validity to some extent or alternatively non-signi<sup>fi</sup>cant items can be kept to preserve the content validity [45]. Formative model results of our model are presented in Table 3 in detail.

Note that considering the t-statistics in Table 3, all of the indicators were found to be signi<sup>fi</sup>cant at the 0.05 signi<sup>fi</sup>cance level, and therefore kept in the model. Negative PLS weights indicate the fact that the individual variable affects in a negative direction in its corresponding composite variable. In other words, for example the total days a patient waited for a transplant on the waiting list (DAYSWAITCHORN) has a negative impact on the recipient's pro<sup>fi</sup>le quanti<sup>fi</sup>ed by the PLS weight of −0.527, which in turn negatively affects his/her strength to undergo a successful transplant. All the negative and positive signs of the other indicators are to be interpreted in the same fashion.

As for the structural portion of our model, we used normalized composite scores of the latent/composite variables received from PLS path model as inputs to the regression tree models which were implemented with CHAID, CART, and M5. Based on the favorable results provided by CART we present the results of PLS-based CART model and compare to the others as in Table 4. The reason for selecting sole PLS and sole CART as benchmark methods is that the former provides a clear interpretability and the latter provides high prediction accuracy. Yet, each lacks the aspect that the other one performs well. However, the proposed integration in this paper (PLSbased CART model) handles this tradeoff by means of a clearer interpretation and higher accuracy simultaneously. This simultaneous success was the main intended target of the USM model, but since it makes uses of black box model with Bayesian neural networks it still lacks the interpretability of the model. Our proposed PLS-based CART model overcomes this limitation of USM with a clearer depiction of “if–then” rules. Additionally, it provides considerably high prediction accuracy with a 0.68 of $R ^ { 2 }$ value as opposed to 0.73 of $\cdot _ { R ^ { 2 } }$ value by the USM.

Formative model results for composite variables.

<table><tr><td>Indicators</td><td>Composite variables</td><td>PLS weights</td><td>t-statistic</td></tr><tr><td>AGE</td><td>Recipient&#x27;s profile</td><td>-0.301</td><td>6.529</td></tr><tr><td>DAYSWAITCHORN</td><td></td><td>-0.527</td><td>2.396</td></tr><tr><td>FUNC_STAT_TRR</td><td></td><td>0.113</td><td>8.739</td></tr><tr><td>HGT_CM_TRR</td><td></td><td>-0.182</td><td>4.269</td></tr><tr><td>MED_COND_TRR</td><td></td><td>0.624</td><td>6.954</td></tr><tr><td>STERNOTOMY_TRR</td><td></td><td>0.018</td><td>5.343</td></tr><tr><td>WGT_KG_TRR</td><td></td><td>-0.475</td><td>7.885</td></tr><tr><td>ABO_MAT</td><td>Match level</td><td>0.413</td><td>6.957</td></tr><tr><td>AMAT</td><td></td><td>0.082</td><td>5.691</td></tr><tr><td>BMAT</td><td></td><td>0.276</td><td>3.098</td></tr><tr><td>DRMAT</td><td></td><td>0.037</td><td>7.738</td></tr><tr><td>EINT</td><td></td><td>0.593</td><td>2.131</td></tr><tr><td>GINT</td><td></td><td>0.727</td><td>4.799</td></tr><tr><td>HLAMAT</td><td></td><td>0.073</td><td>5.325</td></tr><tr><td>AGE_DON</td><td>Donor&#x27;s profile</td><td>-0.929</td><td>7.694</td></tr><tr><td>HGT_CM_DON</td><td></td><td>-0.228</td><td>6.746</td></tr><tr><td>HIST_ALCOHOL_OLD_DON</td><td></td><td>-0.032</td><td>7.348</td></tr><tr><td>HIST_CANCER_DON</td><td></td><td>-0.015</td><td>9.718</td></tr><tr><td>HIST_CIG_DON</td><td></td><td>-0.106</td><td>8.047</td></tr><tr><td>HIST_COCAINE_DON</td><td></td><td>-0.034</td><td>2.106</td></tr><tr><td>HIST_DIABETES_DON</td><td></td><td>-0.029</td><td>5.541</td></tr><tr><td>HIST_HYPERTENS_DON</td><td></td><td>-0.073</td><td>3.698</td></tr><tr><td>HIST_IV_DRUG_DON</td><td></td><td>-0.049</td><td>7.379</td></tr><tr><td>HIST_MI_DON</td><td></td><td>-0.051</td><td>8.432</td></tr><tr><td>WGT_KG_DON</td><td></td><td>-0.088</td><td>6.454</td></tr></table>

The results in Table 4 are based on the testing dataset. In order to minimize the bias associated with the random sampling of the training and testing datasets, researchers tend to use k-fold crossvalidation [35]. In k-fold cross-validation (a.k.a. rotation estimation) the complete dataset (D) is randomly split into k mutually exclusive subsets (the folds: $D _ { 1 } , D _ { 2 } , . . . , D _ { k } )$ of approximately equal size. The prediction model is trained and tested k times. Each time $( t { \in } \{  1 , 2 , . . . ,$ $k \}$ , it is trained on all but one fold $( D _ { t } )$ and tested on the remaining single fold $( D _ { t } )$ . The cross-validation estimate of the overall performance criteria is calculated as simply the average of the k individual performance measures as in Eq. (19),

$$
\mathrm{CV} = \frac {1}{k} \sum_ {i = 1} ^ {k} P M _ {i}\tag{19}
$$

where CV stands for cross-validation, k is the number of folds used, and PM is the performance measure for each fold, in our case the $R ^ { 2 }$ value [40].

Comparison of $R ^ { 2 }$ values from each model.

<table><tr><td rowspan="2">Performance measure</td><td colspan="4">Prediction models</td></tr><tr><td>Sole PLS</td><td>Sole CART</td><td>PLS-based CART (proposed in this paper)</td><td>USM</td></tr><tr><td> $R^2$  value</td><td>0.34</td><td>0.56</td><td>0.68</td><td>0.73</td></tr></table>

In this study, to estimate the performance of the prediction models a 10-fold cross-validation approach was used. Empirical studies showed that 10 seems to be an optimal number of folds (that optimizes the time it takes to complete the test while minimizing the bias and variance associated with the validation process) [35]. In 10- fold cross-validation the entire dataset is divided into 10 mutually exclusive subsets (or folds). Each fold is used once to test the performance of the prediction model that is generated from the combined data of the remaining nine folds, leading to 10 independent performance estimates. The results presented in Table 4 are the 10- fold cross-validated results for each model. In a 2 GHz Intel Core 2 $\boldsymbol { \mathrm { D u o } } ^ { \otimes }$ PC, USM model with Matlab-based Neusrel<sup>®</sup> [7] required 27 h to complete 50-sample bootstrapping whereas the analysis using our proposed structural equation modeling-based CART model (with IBM SPSS Modeler<sup>®</sup> [56]) was completed within a few minutes (\~3– 4 min).

In this study, variable importance measures were also investigated to judge the relative importance of each composite variable. Variable importance ranking in decision trees uses surrogate splitting to produce a scale (a relative importance measure) for each predictor variable included in the analysis. The computational details regarding these measures can be found in Breiman et al. [6]. 10-fold crossvalidated variable importance ranking for sole PLS, sole CART, and PLS-based CART model results are illustrated in Fig. 3. Regarding the sole PLS variable ranking, path coef<sup>fi</sup>cients are reported all of which were found to be signi<sup>fi</sup>cant at 0.05 level. Note that in Fig. 3, our proposed structural equation model-based decision tree model and the universal structure modeling ranked the variables exactly in the same order. This consistency between the two models could be attributed to the fact that both models are capable of discovering nonlinear relationships among the predictors, which was not possible to capture with sole partial least squares-based path modeling. These two models agree that in predicting the transplant success the ascending rank order of composite variables is as follows: donor's profile, match level, and recipient's profile. Based on this consistency in Fig. 3and high prediction accuracy provided by the two models as in Table 4, we can conclude that the most important predictors of transplant success would be ranked as such.

Likewise, when all predictor variables are tapped into the CART model, nine topmost important variables (WGT\_KG\_DON, HIST\_CIG\_ DON, HIST\_IV\_DRUG\_DON, ABO\_MAT, AMAT, AGE\_DON, DRMAT, GINT, HLAMAT) also belong to the top-ranked two composite variables, namely donor's profile and match level with a 10-fold cross-validated variable importance ranking approach. In the USM model, nonlinear relations were sought, and at 0.05 signi<sup>fi</sup>cance level transplant success was revealed to have a signi<sup>fi</sup>cant nonlinear relationship with the donor's pro<sup>fi</sup>le. In Fig. 4 the causing composite variable, donor's pro<sup>fi</sup>le, is represented against the affected latent variable, transplant success. The line getting through the observed cases is the additive function explaining the nonlinear cause of donor's pro<sup>fi</sup>le on transplant success. Note that the 0–100 bandwidth of x-axis is the scale of the normalized latent variable of donor's pro<sup>fi</sup>le. The y-axis represents the variation in transplant success caused by the causing variable, i.e. donor's pro<sup>fi</sup>le. High nonlinearity observed here explains why sole PLS model could not reveal the high impact of the composite variable donor's pro<sup>fi</sup>le while ranking the composite variables in terms of their importance.

Interaction effect (IE) of two independent latent/composite variables $( \xi ^ { j }$ and $\xi ^ { k } )$ on $\boldsymbol { \xi } ^ { i }$ (shortly $I E _ { j k } ^ { i } )$ is expressed as the portion of variable $\xi ^ { i } { \sf s }$ explained variance that can be attributed to the interaction between $\boldsymbol { \xi } ^ { j }$ and $\boldsymbol { \xi } ^ { k }$ and is given by Eq. (20) [8].

$$
I E _ {j k} ^ {i} = \frac {\sum_ {n = 1} ^ {N} \left| \frac {\widehat {z _ {j k} ^ {i}} - \widehat {a _ {j}} - \widehat {a _ {k}}}{\widehat {\xi} - \overline {{\xi}}} \right|}{N}\tag{20}
$$

![](/api/attachments/KW9BHKGB/fulltext/images/cbd29ff19575ac3c73e63447c11cd4ec08310d2546f550bd6ec9ecd75ad5e502.jpg)

![](/api/attachments/KW9BHKGB/fulltext/images/c7525b2b9892989ee915ddaff0e1a525c94eb3d4e9f05e14406f2d6c4b97b188.jpg)

![](/api/attachments/KW9BHKGB/fulltext/images/0903295b059163ef9b661a992c441b6182d6847663b40a237295453f11643330.jpg)

![](/api/attachments/KW9BHKGB/fulltext/images/0482a504aa3653ea13b47367755827a303bc4d763b974bf2204494235bae9e10.jpg)  
Fig. 3. Variable importance ranking by different models.

where $\hat { a }$ is the additive score of a polynomial regression of $\xi$ on a and ^z is the outcome of a universal regression with the two latent variables j and k as regressors on $z _ { j k } ^ { i } .$ Here a and z can be given by Eqs. (21) and (22), respectively.

$$
a _ {j} ^ {i} = f ^ {i} \left(\xi^ {1},..., \xi^ {j},..., \xi^ {n}\right) - f ^ {i} \left(\xi^ {1},..., \overline {{\xi}} ^ {j},..., \xi^ {l}\right)\tag{21}
$$

where $a _ { j } ^ { i }$ is the change in $\boldsymbol { \xi } ^ { i }$ caused by the additive effect of $\xi ^ { j } , j$ f is the neural network function, and $\boldsymbol { \xi } ^ { 1 }$ and $\boldsymbol { \xi } ^ { n }$ are the latent variables. By setting the value of $\cdot \varsigma ^ { j }$ to its mean value $( \ \xi ^ { j } )$ , the change in $\boldsymbol { \xi } ^ { i }$ which is provided by $\boldsymbol { \xi } ^ { j }$ can be captured. Similarly, Eq. (22) represents the change in $\boldsymbol { \xi } ^ { i }$ caused by the interactive effect of $\boldsymbol { \xi } ^ { j }$ and $\boldsymbol { \xi } ^ { k }$ .

$$
z _ {j k} ^ {i} = f ^ {i} \left(\xi^ {1}, \dots , \xi^ {j}, \dots , \xi^ {k}, \dots , \xi^ {l}\right) - f ^ {i} \left(\xi^ {1}, \dots , \overline {{\xi^ {j}}}, \dots , \overline {{\xi^ {k}}}, \dots , \xi^ {l}\right)\tag{22}
$$

![](/api/attachments/KW9BHKGB/fulltext/images/a02d6f94d7ebc21bbdd00c9db9f0599d622fcc68330668302a123606ec525270.jpg)  
Fig. 4. Nonlinearity revealed by the USM model.

In our analysis, only one such an interaction effect on transplant success was observed at 0.05 signi<sup>fi</sup>cance, which was caused by the interaction of recipient's pro<sup>fi</sup>le and match level as shown in Fig. 5.

The IE value of this effect through Eq. (19) was 0.82. This is translated into that 82% of the explained variance of the latent variable transplant success has been explained by the interaction effect caused by recipient's pro<sup>fi</sup>le and match level. In other words, referring to Table 4, 82% of the explained variance by USM with 73% can be attributed to the interaction effect and the rest is explained by individual effects of all composite variables, i.e. recipient's pro<sup>fi</sup>le, donor's pro<sup>fi</sup>le, and match level.

The <sup>fi</sup>nal structural equation modeling-based CART model is also pictorially presented in Fig. 6. One of the most straightforward sample rules extracted by this <sup>fi</sup>nal model is as follows: if the donor's pro<sup>fi</sup>le score is higher than 0.766 and match level score is higher than 0.841, then transplant success would be 94.6%. The rest of the rules can also be visualized in Fig. $6 .$

## 4. Managerial implications and conclusions

Medical experts are trained to reason “medically” whereas data miners place more importance on model's performance, e.g. prediction accuracy. Since research designs vary in both areas, such differences grow even more later on [52]. In addition to this con<sup>fl</sup>ict of interests, some machine learning methods (e.g. neural networks) are powerful in terms of predictive ability, yet they are black boxes. Namely, they give no (or very limited) explanation of the “reasoning” used behind the scene to achieve high predictive accuracy. Therefore, their acceptance by the medical experts is limited [52]. Our proposed method balances this trade-off and overcomes aforementioned issues that have been faced in collaboration between medical experts and data miners. Our integrated method with structural equation modeling and decision trees is proven to be fairly capable in terms of predictive accuracy with an $R ^ { 2 }$ value of 0.68 as well as interpretability with a much lower computational time requirement compared to Bayesian neural networks-based USM technique.

![](/api/attachments/KW9BHKGB/fulltext/images/2fa17461c3a3ea7c2c6854a855a1c3a56aa2ddb79fd8d10d2d334cd50e7a2611.jpg)  
Fig. 5. Interaction effect of treatment and match level on transplant success.

Proposed method not only covers nonlinear relations among various variables but also brings more explanation into the scene to make the lung transplant procedure more understandable and transparent in terms of variables used for modeling and prediction. It provides concise rules which can be visualized in the <sup>fi</sup>nal decision tree.

A main future research stream of this study might be to create a decision support system equipped with a user-friendly frontend and a near-transparent backend application which would help medical professionals to deal with voluminous data more effectively and ef<sup>fi</sup>ciently (e.g. providing reliable results in a very short time period).

![](/api/attachments/KW9BHKGB/fulltext/images/e96c09d99f4622316c3d437aae145efbe88fdb06c934478b8d793993df8ebe47.jpg)  
Fig. 6. The <sup>fi</sup>nal PLS-based CART model.

Having entered hundreds of predictive variables into the system, a medical professional can then visualize the summarized information through our proposed method and make decisions for the upcoming transplants. In other words, having a potential donor organ on hand a medical expert could make a rapid decision as to which potential recipient patient to allocate the donor organ. As explained in this paper, this could be achieved by utilizing the most critical variables which are related to recipient's and donor's pro<sup>fi</sup>les and their match level information as opposed to using couple of hundreds of variables.

## References

[1] J. Aguero, L. Almenar, L. Martinez-Dolz, J. Moro, M.T. Izquierdo, O. Cano, A. Salvador Differences in clinical pro<sup>fi</sup>le and survival after heart transplantation according to prior heart disease, Transplantation Proceedings 39 (2007) 2350–2352.

[2] R. Arakji, R.B. Fich, M. Koufaris, Exploring contributions of public resources in social bookmarking systems, Decision Support Systems 47 (3) (2009) 245–253.

[3] J.S. Benamati, A.L. Lederer, Decision support systems unfrastructure: the root problems of the management of changing IT, Decision Support Systems 45 (4) (2008) 833–844.

[4] M. Biewen, Item nonresponse and inequality measurement: evidence from the German earnings distribution, Allgemeines Statistisches Archiv 85 (2001).

[5] K. Bollen, R. Lennox, Conventional wisdom on measurement: a structural equation perspective, Psychological bulletin 110 (1991) 305–314

[6] L. Breiman, J.H. Friedman, R.A. Olshen, C.J. Stone, Classi<sup>fi</sup>cation and regression trees, Wadsworth & Brooks/Cole Advanced Books & Software, Monterey, CA, 1984.

[7] F. Buckler, Neusrel–Neuer Kausalanalyseansatz auf Basis Neuronaler Netze als Instrument der Marketingforschung, Cuvillier, Göttingen, Germany, 20018 http:// neusrel.com/.

[8] F. Buckler, T. Hennig-Thurau, Identifying hidden structures in marketing's structural models through universal structure modeling: an explorative bayesian neural network complement to LISREL and PLS, Marketing, Journal of Research and Management 4 (2008) 47–66.

[9] E.T. Castaldo, Correlation of health-related quality of life after liver transplant with the model for end-stage liver disease score, Archives of Surgery 144 (2) (2009).

[10] W.W. Chin, P.R. Newsted, Structural equation modeling analysis with small samples using partial least squares, in: R. Hoyle (Ed.), Statistical Strategies for Small Sample Research, Sage Publications, Beverly Hills, CA, 1999.

[11] W.W. Chin, The partial least squares approach to structural equation modeling, in: G.A. Marcoulides (Ed.), Modern Methods for Business Research, Lawrence Erlbaum, Mahway, NJ, 1998, pp. 295–336.

[12] W.W. Chin, The partial least squares approach to structural equation modeling, in: G.A. Marcoulides (Ed.), Modern Methods for Business Research, U.K, London, 1998, pp. 295–336.

[13] J.T. Cope, A.K. Kaza, C.C. Reade, K.S. Shockey, J.A. Kern, C.G. Tribble, I.L. Kron, A cost comparison of heart transplantation versus alternative operations for cardiomy opathy, Annual thoracic Surgery 72 (2001) 1298–1305.

[14] S.A. Cupples, L. Ohler, Transplantation Nursing Secrets, Hanley & Belfus Publication, 2002.

[15] S. Daar, D.R. Salomon, R.M. Ferguson, J.H. Helderman, P. Macchiarini, New directions for organ transplantation, Nature 392 (1998) 11–12.

[16] D. Delen, A. Oztekin, Z.J. Kong, A machine learning-based approach to prognostic analysis of thoracic transplantations, Arti<sup>fi</sup>cial Intelligence in Medicine 49 (1) (2010) 33–42.

[17] G.M. Devins, Structure of lifestyle disruptions in chronic disease: a con<sup>fi</sup>rmatory factor analysis of the analysis of the illness intrusiveness ratings scale, Medical Care 39 (10) (2001).

[18] S. Dreiseitl, L. Ohno-Machado, Logistic regression and arti<sup>fi</sup>cial neural network classification models: a methodology review Journal of Biomedical Informatics 35 (2002) 352–359.

[19] B. Efron, R. Tibshirani, Statistical data analysis in the computer age, Science 253 (1991) 390–395.

[20] H. Faller, Depression and disease severity as predictors of health-related quality of life in patients with chronic heart failure–a structural equation modeling approach, Journal of Cardiac Failure 15 (4) (2009).

[21] J. Fernandez-Yanez, J. Palomo, E.G. Torrecilla, D. Pascual, G. Garrido, J.J.G. de Diego, M. Dominguez. I. Almendral. Prognosis of heart transplant candidates stabilized on medical therapy, Revista Española de Cardiología 58 (2005) 1162-1170.

[22] C. Fornell, D.F. Larcker, Evaluating structural equation models with unobservable variables and measurement error, Journal of Marketing Research 18 (1981) 39–50.

[23] D. Gefen, D. Straub, M. Boudreau, Structural equation modeling and regression: guidelines for research practice, Communications of AIS 7 (2000) 1–78.

[24] F.L. Grover, M.L. Barr, L.B. Edwards, F.J. Martinez, R.N. Pierson, B.R. Rosengard, S. Murray, Thoracic transplantation, American Journal of Transplantation 3 (2003) 91–102.

[25] S. Hariharan, C.P. Johnson, B.A. Bresnahan, S.E. Taranto, M.J. McIntosh, D. Stablein, Improved Graft Survival after Renal Transplantation in the United States, 1988 to 1996, The New England Journal of Medicine 342 (2000) 605–612.

[26] A.M. Harper, S.E. Taranto, E.B. Edwards, O.P. Daily, An update on a successful simulation proiect: the UNOS liver allocation model. Proceedings of the Winter Simulation Conference USA. 2000 pp 1955–1962

[27] J.I. Herrero, J.F. Lucena, J. Quiroga, B. Sangro, F. Pardo, F. Rotellar, J. Alvarez-Cienfueodos, J. Prieto, Liver transplant recipients older than 60 years have lower survival and higher incidence of malignancy, American Journal of Transplantation 3 (2003) 1407–1412.

[28] Z. Hong, J. Wu, G. Smart, K. Kaita, S.W. Wen, S. Paton, M. Dawood, Survival analysis of liver transplant patients in Canada, Transplantation Proceedings, 2006, pp. 2951–2956.

[29] S.H. Hsu, W.H. Chen, M.J. Hsieh, Robustness testing of PLS, LISREL, EQS and ANNbased SEM for measuring customer satisfaction, Total Quality Management 17 (3) (2006).

[30] E. Jacobowicz, C. Derquenne, A modi<sup>fi</sup>ed PLS path modeling algorithm handling re<sup>fl</sup>ective categorical variables and a new model building strategy, Computational Statistics and Data Analysis 51 (8) (2007) 3666–3678.

[31] P.C. Jenkins, M.F. Flanagan, K.J. Jenkins, J.D. Sargent, C.E. Canter, R.E. Chinnock, R.N. Vincent A.N.A. Tosteson GT. O'Connor Survival analysis and risk factors for mortality in transplantation and staged surgery for hypoplastic left heart syndrome, Journal of the American College of Cardiology 36 (2000) 1178–1185.

[32] K. Jöreskog, D. Sorbom, LISREL 8.8: User's Reference Guide, Scienti<sup>fi</sup>c Software International, Inc, Chicago, 2008.

[33] K.G. Jöreskog, A general method for analysis of covariance structure, Biometrika 57 (2) (1970) 239–251.

[34] G.V. Kass, An exploratory technique for investigating large quantities of categorical data, Applied Statistics 29 (1980) 119–127.

[35] R. Kohavi, A study of cross-validation and bootstrap for accuracy estimation and model selection, Proceedings of the 14th International Conference on AI (IJCAI), Morgan Kaufmann, San Mateo, CA, 1995, pp. 1137–1145.

[36] H.M. Lin, H.M. Kaufmann, M.A. McBride, D.B. Davies, J.D. Rosendale, C.M. Smith, E. B. Edwards, O.P. Daily, J. Kirklin, C.F. Shield, L.G. Hunsicker, Center-Speci<sup>fi</sup>c Graf and Patient Survival Rates: 1997 UNOS Report, JAMA 280 (1998) 1153–1160.

[37] R.S. Lin, S.D. Horn, J.F. Hurdle, S. Goldfarb-Rumyantzev, Single and multiple timepoint prediction models in kidney transplant outcomes, Journal of Biomedical Informatics 41 (2008) 944–952

[38] A.R. McIntosh, F. Gonzalez-Lima, Structural equation modeling and its application to network analysis in functional brain imaging, Human Brain Mapping 2 (1–2) (1994) 2–22.

[39] A.E. Molhazn, H.C. Northcott, L. Hayduk, Quality of life of patients with end stage renal disease: a structural equation model, Quality of Life Research 5 (4) (1996).

[40] D.L. Olson, D. Delen, Advanced data mining techniques, Springer-Verlag, Berlin-Heidelberg, 2008.

[41] A. Oztekin, A. Nikov, S. Zaim, UWIS: an assessment methodology for usability of web-based information systems, The Journal of Systems and Software 82 (12) (2009) 2038–2050.

[42] A. Oztekin, D. Delen, Z.J. Kong, Predicting the graft survival for heart-lung transplantation patients: an integrated data mining methodology, International Journal of Medical Informatics 78 (12) (2009) e84–e96.

[43] A. Oztekin, Z.J. Kong, O. Uysal, UseLearn: a novel checklist and usability evaluation method for eLearning systems by criticality metric analysis, International Journal of Industrial Ergonomics 40 (4) (2010) 455–469

[44] E.J. Pedhazur, L.P. Schmelkin, Measurement, design and analysis: an integrated approach, Lawrence Erlbaum, Hillsdale, 1991.

[45] S. Petter, D. Straub, A. Rai, Specifying formative constructs in information systems research MIS Ouarterly 31 (4) (2007) 623–656.

[46] R.N. Pierson, M.L. Barr, K.P. McCulluough, T. Egan, E. Garrity, M. Jessup, S. Murray, Thoracic organ transplantation, American Journal of Transplantation 4 (2004) 93–105.

[47] J. Quinlan, C4.5: programs for machine learning, Morgan Kaufmann, San Mateo, CA, 1993.

[48] J. Quinlan, Induction of decision trees, Machine Learning 1 (1986) 81–106

[49] J. Quinlan, Learning with continuous classes, in: Adams, Sterling (Eds.), Proceedings of 5th Australian Joint Conference on Arti<sup>fi</sup>cial Intelligence, World Scienti<sup>fi</sup>c, Singapore, 1992, pp. 343–348.

[50] C.M. Ringle, S. Wende, S. Will, Smartpls 2.0 (M3) Beta, 20058 http://www. smartpls.de.

[51] R.J. Ruth, L. Wysezewianski, G. Herline, Kidney transplantation: a simulation model for examining demand and supply, Management Science 31 (1985) 515–526.

[52] M. Schmitt, H.N. Teodorescu, A. Jain, S. Jain, L.C. Jain, Computational intelligence processing in medical processing, Studies in Fuzziness and Soft Computing, Springer-Verlag, 2002.

[53] D. Sheppard, D. McPhee, C. Darke, B. Shretha, R. Moore, A. Jurewitz, A. Gray, Predicting cytomegalovirus disease after renal transplantation: an arti<sup>fi</sup>cial neural network approach, International Journal of Medical Informatics 54 (1999) 55–76.

[54] J.M.A. Smith, J. Vanhaecke, A. Haverich, E. De Veries, L. Roels, G. Persijn, G. Laufer, Waiting for a thoracic transplant in eurotransplant, Transplant International 19 (2006).

[55] K.W. Smith, N.E. Avis, S.F. Assman, Distinguishing between Quality of Life and Health Status in Quality of Life Research: a meta-analysis, Quality of Life Research 8 (1999).

[56] IBM SPSS Modeler, A comprehensive data/text mining software environment, version 14.0 URL: http://www.spss.com/software/modeling/modeler. Accessed on August 15.2010

[57] StatModel, http://www.statmodel.com/features3.shtml8 Accessed on May 15, 2010].

[58] M. Tenenhaus, V.E. Vinzi, Y.M. Chatelin, C. Lauro, PLS path modeling, Computational Statistics and Data Analysis 48 (1) (2005) 159–206

[59] Y.S. Tjang, G.J.M.G. Heijdan, G. Tenderich, D. Grobbee, R. Korfer, Survival analysis in heart transplantation: results from an analysis of 1290 cases in a single center, European Journal of Cardio-Thoracic Surgery 33 (2008) 856–861.

[60] J. Wang, R. Chen, T. Herath, H.R. Rao, Visual e-mail authentication and identi<sup>fi</sup>cation services: an investigation of the effects on e-mail use, Decision Support Systems 48 (1) (2009) 92–102.

[61] M.Y. Yi, F.D. Davis, Developing and validating an observational learning model of computer software training and skill acquisition, Information Systems Research 14 (2) (2003) 146–169.

![](/api/attachments/KW9BHKGB/fulltext/images/f100a6b356deb718e23eac7e55b06b47c0c64610a3f67086a85ea8c166c736ba.jpg)

Asil Oztekin received the B.S. degree from Yildiz Technical University, Istanbul, Turkey, in 2004, and the M.S. degree from Fatih University, Istanbul, Turkey, in 2006, both in industrial engineering. He also completed the Ph.D. degree in the School of Industrial Engineering and Management at Oklahoma State University (OSU), Stillwater, in 2010. He is currently working as a Visiting Assistant Professor in the Department of Statistics at Oklahoma State University. His research interests include quality improvement in complex service and manufacturing systems, human–computer interaction, medical informatics, and data mining techniques. His work has been published in Decision Support Systems, International Journal of Production Research, International Journal of Medical Informatics, Artificial Intelligence in Medicine, International Journal of Industrial Ergonomics, Journal of Systems and Software, IEEE Transactions on Semiconductor Manufacturing, and Journal of Manufacturing Science and Engineering. He has reviewed manuscripts for Decision Support Systems, International Journal of Production Research, Computers in Industry, and Journal of Systems and Software. Mr. Oztekin is a member of ASQ, IIE, and INFORMS and is currently serving as the president of Oklahoma State University ASQ student chapter. Mr. Oztekin was the recipient of the Alpha Pi Mu Outstanding Industrial Engineering and Management Research Assistant Award from OSU in November 2009.

![](/api/attachments/KW9BHKGB/fulltext/images/7cc422b90f1ee5c9e545985b48deab07a829e40e8261587661daed03ff4756e2.jpg)

Zhenyu (James) Kong received the B.S. and M.S. degrees in mechanical engineering from the Harbin Institute of Technology, China, in 1993 and 1995, respectively, and the Ph.D. degree from the Department of Industrial and System Engineering, University of Wisconsin–Madison in 2004. Currently, he is an Assistant Professor with the School of Industrial Engineering and Management, Oklahoma State University (OSU), Stillwater, since August 2006. Before joining OSU, he was a Senior Research Engineer with Dimensional Control Systems Inc., MI (2004–2006). He has authored or coauthored a number of articles in various journals. His research is sponsored by the National Science Foundation the Oklahoma Transportation Center, and Dimensional Control Systems Inc. His research focuses on automatic quality control for large and complex manufacturing processes/systems. Dr. Kong is a member of the Institute of Industrial Engineers, INFORMS, the American Society of Mechanical Engineers, and SME.

![](/api/attachments/KW9BHKGB/fulltext/images/6c970e20c4ce5952edaad8d85e952cfe81e945b10d0649232361ec3e87295a06.jpg)

Dursun Delen is an Associate Professor of Management Science and Information Systems in the Spears School of Business at Oklahoma State University (OSU). He received his Ph.D. in Industrial Engineering and Management from OSU in 1997. Prior to his appointment as an Assistant Professor at OSU in 2001, he worked for a privately-owned research company, Knowledge Based Systems Inc., in College Station, Texas, as a research scientist for <sup>fi</sup>ve years, during which he led a number of decision support and other information systems related research projects funded by federal agencies such as DoD, NASA, NIST and DOE. His research has appeared in major journals including Decision Support Systems, Expert Systems with Applications

Expert Systems, Communications of the ACM, Computers and Operations Research, Computers in Industry, Journal of Production and Operations Management, Artificial Intelligence in Medicine, and many others. He is the author of two books: “Advanced Data Mining Techniques” with Springer and “Decision Support and Business Intelligence Systems” with Prentice Hall. He is an associate editor for the International Journal of RF Technologies: Research and Applications, and serves on the editorial boards of the Journal of Information and Knowledge Management, International Journal of Intelligent Information Technologies, International Journal of Service Sciences, and Journal of Emerging Technologies in Web Intelligence. His research interests are in decision support systems, expert systems, data and text mining, knowledge management, business intelligence and enterprise modeling.
