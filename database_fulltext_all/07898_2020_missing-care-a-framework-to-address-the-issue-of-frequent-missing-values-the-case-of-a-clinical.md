---
otero_id: 7898
otero_key: "V5FF6CRY"
title: "Missing care: A framework to address the issue of frequent missing values;The case of a clinical decision support system for Parkinson's disease"
authors: "Saeed Piri"
year: "2020"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2020.113339"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
## Journal Pre-proof

Missing care: A framework to address the issue of frequent missing values the case of a clinical decision support system for Parkinson's disease

ELSEVIER Decision Support Systems

## Saeed Piri

![](/api/attachments/V5FF6CRY/fulltext/images/5faf15ef491123e45d837162ffd7acce680155cc5feb92c902d901855b46153c.jpg)

PII: S0167-9236(20)30094-4

DOI: https://doi.org/10.1016/j.dss.2020.113339

Reference: DECSUP 113339

To appear in: Decision Support Systems

Received date: 7 November 2019

Revised date: 1 June 2020

Accepted date: 1 June 2020

Please cite this article as: S. Piri, Missing care: A framework to address the issue of frequent missing values the case of a clinical decision support system for Parkinson's disease, Decision Support Systems (2019), https://doi.org/10.1016/j.dss.2020.113339

This is a PDF file of an article that has undergone enhancements after acceptance, such as the addition of a cover page and metadata, and formatting for readability, but it is not yet the definitive version of record. This version will undergo additional copyediting, typesetting and review before it is published in its final form, but we are providing this version to give early visibility of the article. Please note that, during the production process, errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

© 2019 Published by Elsevier.

TITLE PAGE

# Missing Care: A Framework to Address the Issue of Frequent Missing Values The Case of a Clinical Decision Support System for Parkinson’s disease

Saeed Piria

<sup>a</sup> Department of Operations and Business Analytics, Lundquist College of Business, University of Oregon, Eugene, OR, 97403, USA. Email: spiri@uoregon.edu

#Corresponding author:

Saeed Piri

Assistant Professor of Operations and Business Analytics

Lundquist College of Business

University of Oregon

Eugene, OR, 97403, USA.

P: 541-346-7314

Email: spiri@uoregon.edu

Web: https://business.uoregon.edu/faculty/saeed-piri

# Missing Care: A Framework to Address the Issue of Frequent Missing Values The Case of a Clinical Decision Support System for Parkinson’s disease

## Abstract

In recent decades, the implementation of electronic health record (EHR) systems has been evolving worldwide, leading to the creation of immense data volume in healthcare. Moreover, there has been a call for research studies to enhance personalized medicine and develop clinical decision support systems (CDSS) by analyzing the available EHR data. In EHR data, usually, there are millions of patients records with hundreds of features collected over a long period of time. This enormity of EHR data poses significant challenges, one of which is dealing with many variables with very high degrees of missi ng values. In this study, the data issing Care’ is select the most important variables at an acceptable missing values gree models with high predictive power. Moreover, Missing Care is applied to analyze a unique, large EHR data to develop a CDSS for detecting Besides, there is a lack of acce with Parkinson’s disease in the US remain undiagnosed. The developed CDSS can be integrated into EHR systems or utilized as an independent tool by healthcare practitioners who are not necessarily specialists; therefore, making up for the limited access to specialized care in remote areas.

Keywords: Electronic health records; data missing values; clinical decision support systems; predictive healthcare analytics; imbalanced data learning; Parkinson’s disease

## 1. Introduction

Over the past two decades, the ever-increasing creation of immense data volumes in diverse forms from various sources has inspired and induced industry practitioners and researchers to analyze and exploit the available big data and transform their analysis to competitive advantages and strategic value [1-6]. “Big data analytics”, “business analytics”, “predictive analytics”, and “data-driven decision making” are some of the terms used in the literature for this stream of research. In healthcare, similar to many other fields, such as retail, e-commerce, and media & entertainment, vast amounts of data in different forms have been available owing to process digitalization in the industry [7]. Two prime sources of big data in healthcare are genomic and DNA of an organism and is insurance records, pharmacy prescription, and patient feedback and responses [8].

of EHR systems have been evolving worldwide , and in the US [3, 9]. Jha et al. [10] reported that the adoption of basic or comprehensive EHR raised from 8.7% in EHR creased to 59%, and in 2017, 96% of all nontechnology [11]. Many researchers have studied the nd facilitating EHR assimilation in small physician practices [12, 13], and also the impact and benefit associated with the adoption of EHR [9, 14-18]. As using EHR systems has become ubiquitous, many researchers and clinicians have started using EHR and its data for research purposes [19, 20]. A specific characteristic of an EHR system is that it is a comprehensive system, which links multiple patient level data sources such as demographics, encounters, lab tests, medication, and medical procedures [21]. This comprehensiveness allows for more reliable and robust research that considers many aspects of the healthcare system and patients in this system. The trove of health data available , coupled with the recent advancement in analytics, has created an ideal opportunity for researchers to conduct analytics research and gain valuable insights that improve decision making in healthcare systems [22].

Personalized medicine provides medical care tailored to the unique physiological and medical history of individuals rather than relying on general population information. Personalized medicine leads to earlier diagnosis, more effective interventions and treatments, and lower cost [23]. Developing clinical decision support systems (CDSS) has been outlined as one of the most crucial research directions related to personalized medicine [1, 20, 24, 25]. CDSSs are tools that aid clinicians in making more informed decisions, such as diagnosing various diseases. CDSSs can be integrated into EHR systems and be a part of clinical workflow and, as a result, help clinicians to stratify patients, diagnose diseases, and identify the best candidates for various treatments. One of the most promising directions in developing CDSSs is data mining Baesens et al. [29] have discussed and noted the significance and value of predictive analytics specifically in of a phenomenon, construct operationalization considerations are trivial. Then, they introduced “assessing Dhar [27] argued that in the healthcare domain, prediction could be even more important than explanation (or causality), because of proven benefits of earlier diagnosis, intervention, and treatment.

In EHR data, usually, there are hundreds of thousands, and sometimes millions of patients with many records and features (demographics, laboratory, medications, encounters, and outcomes) collected over a long period of time. Therefore, the enormity and complexity of EHR data pose significant research and practical challenges [3]. One of the most critical challenges is dealing with many variables with very high degrees of missing values [30]. If we consider the laboratory information, there are hundreds of different lab tests in EHR data; however, not every patient takes all of those lab tests. Therefore, for many features (tests), the majority of values are missing (at the level of more than 70% to 90% missing). Baesens et al. [29] mention,

“Access to big data and the tools to perform deep analytics suggests that power now equals information (data) + trust.”

Then, they extensively discuss data quality as a critical and essential topic that is frequently ignored in data analytics. Research has shown that while many analytics and machine learning techniques might yield comparable predictive performance, the best way to enhance this performance is to work on the key element of analytics, data [31]. Data completeness is a vital aspect of data quality [32, 33]. Thus, in analyzing EHR data, we deal with data quality from the completeness point of view [30]. Although many studies, especially in the fields of statistics and machine learning, have focused on imputing missing values, they only consider variables that have reasonable degrees of completeness (roughly below 50% missing) and variables with very [30, 34, 35]. As a result, the challenge of dealing with variables with very high degrees of missingness remains unanswered. To address this challenge, n framework that can be applied to EHR data and other types of data with the same challenge of having many variables with very high degrees of missing values is Usin Missing Care, data analytics researchers will be an acceptable missing values degree to use imputation

Moreover, the proposed framework, Missing Care, is applied to develop a CDSS for detecting and screening for Parkinson’s disease (PD). PD is a chronic and progressive neurological disorder affecting more than 10 million people worldwide. In the US alone, there are about 500,000 patients diagnosed with PD; however, given many undiagnosed or misdiagnosed cases, it is estimated that there are actually about one million patients with PD in the US. Besides patients themselves, PD affects thousands of more spouses, family members, and other caregivers [36]. The fact that the actual number of patients with PD is twice as many as the number of diagnosed patients is a strong indication of an urgent need for a more accessible diagnosis/screening tool for this disease. Hence, developing tools and CDSSs for a more accessible diagnosis of PD is vital. In the US, the total annual direct and indirect costs of PD are about \$52 billion [37]. There is no cure for PD yet, but there are treatment options such as medications and surgery. The primary current diagnostic method for PD is based on the subjective opinion of neurologists reviewing patients’ movement and speaking [38]. Researchers have discussed the challenge of healthcare access, particularly in remote areas, and have urged the need for innovative solutions that are affordable and easy to implement [39-41]. Because of the limited specialty care access, many patients, especially in remote and rural areas, may remain undiagnosed. The developed CDSS can fill this gap and be a solution for the problem of care access in remote areas and, as a result, alleviate the low diagnosis rate for PD.

In this study, by analyzing a unique, large size EHR data, including demographic and routine lab tests, a CDSS for detecting PD is developed. In the development of this CDSS, an imbalanced dataset is analyzed using “synthetic informative minority over-sampling” approach (SIMO) [42], which is an over-sampling algorithm for imbalanced datasets. As Von Alan of research is creating new and innovative artifacts (such as models and systems) to address the real world and applied problems. Harnessing big data in healthcare, using data mining techniques, is consistent with the design science paradigm and has received a lot of attention in recent years. The developed diagnosis/screening CDSS for PD also belongs to this category of research.

This study’s contribution is two-fold. First, to the best of my knowledge , this is the first study that formally discusses the challenge of having many variables with very high degrees of missing values in EHR (and other similar) datasets and addresses it by introducing the Missing Care framework. This framework addresses the issue of data quality as well as trust in big data analytics tools, as discussed by Baesens et al. [29]. Both quality and trust features are discussed in more detail in the methodology section. And, second, from the precision medicine perspective, this study, introduces a CDSS for detecting and screening for PD, a neurological disease with a meager diagnosis rate. This CDSS can be utilized as a tool integrated into EHR systems as well as an independent tool used by healthcare practitioners who are not necessarily specialists;

therefore, making up for the limited access to specialized care in rural and remote areas. The rest of this manuscript is organized as follows. In the next section, the related literature is covered. Next, in the methodology section, the Missing Care framework is introduced. Following that, the data, as well as data pre-processing steps, are presented. Next, in the experiment results section, the results of the analysis in the case of PD are provided. And following that, a series of robustness checks are presented. Finally, the findings, contributions, and implications of this research are discussed.

## 2. Literature Review

## 2.1.Predictive Modeling

The primary purpose of predictive analytics is to predict the outcome of interest for new cases rather than explaining the causal relationships between features and the outcome [28]. Predictive analytics, machine learning, and data mining have been extensively used in the literature. Many researchers have applied customers' repeat visits [44], predicting consumers' purchase timing and choice decisions [45], customer

Social networks, recommendation systems, and process events are other fields that have gained interest from researchers. Examples in this stream are, predicting business process events such as early warning systems [51], and predicting the probability that a social entity will adopt a product [52]. Finally, many research works are related to analyzing unstructured data, such as text, reviews, and blogs [53-56]. For a more extensive review of research in data mining, the readers are referred to Trieu [57].

## 2.2.Healthcare Data Analytics

Kohli & Tan [22] extensively discuss how researchers can contribute to the healthcare transformation in two semantic areas-integration and analytics- using EHR. Healthcare analytics’ primary goal is to predict

medical/healthcare outcomes such as diseases, hospital readmissions, and mortality rates, using clinical and non-clinical data [26]. In healthcare analytics, two types of data sources could be used. First, data collected in clinical trials; these types of datasets are collected explicitly for analysis purposes; however, they are usually small-sized and limited. The other source is secondary data in healthcare, such as EHR data. Data analytics researchers typically deal with datasets from the second source that has its own challenges.

Readmission is defined as being readmitted for the same primary diagnosis within 30 days. Readmissions incur a huge preventable cost to the US healthcare system. Many researchers have developed predictive models to identify and predict patients with a high risk of readmission [34, 58-60]. Another group of researchers has studied online healthcare social platforms and used data analytics to investigate and predict health issues in an online health community [61], predicting the social support in a chronic disease-focused online health community [62], and determining individuals' smoking status [63].

et al. [26] proposed an approa which conditions. Wang et al. [6 work to predict multiple disease risk. Piri et al. [65] developed a CDSS to detect diabetic retinopathy and proposed an ensemble approach to improve the CDSS’s introduced a data-driven framework that integrates multiple machine learning techniques to identify asthma triggers and risk factors. Wang et al. [67] used machine learning to analyze patient-level data and identified patient groups that exhibit significant differences in outcomes of cardiovascular surgical procedures. Ahsen et al. [68] studied breast cancer diagnosis in the presence of human bias. And finally, Hsu [69] proposed an attribute selection method to identify cardiovascular disease risk factors.

Other related healthcare analytics works are on topics such as treatment failures, clinical trials, and patients’ pathways in hospitals. To mention a few, Meyer et al. [70] proposed a machine learning approach to improve dynamic decision making. They applied the proposed method to predict treatment failures for type II diabetic patients. Gómez-Vallejo et al. [71] developed a system to diagnose healthcare-associated infections. Researchers have also used predictive modeling to evaluate the kidney and heart transplant survival [72, 73]. And, Somanchi et al. [74] proposed models to predict whether emergency department patients will be admitted as inpatients or will be discharged.

## 2.3.Parkinson’s disease

The current gold standard for diagnosing PD is a clinical evaluation by a specialist. The criteria for diagnosis have been formalized by the UK Parkinson’s Disease Society Brain Bank [75]. Due to the disease complexity, even the diagnosis by a specialist using the formal criteria is not perfect, and the accuracy is about 90% [76]. Many researchers have studied the association of PD with potential biomarkers and other characteristics of patients. However, most of them are based on studying only one single biomarker in very lower compared to the control group. udied the possibilities of testing tears to find a specific protein that has been Arroyo-Gallego et al. [79] studied 25 PD patients and 27 controls to typing interaction. Another study analyzed the handwriting of 20 PD and 20 controls and performed a discriminant analysis to classify the participant to PD and non-PD [80]. There have been other studies applying machine learning in managing PD, such as using smartphones to monitor PD patients’ movements, calculating a score, and sending it to doctors [81]. The significant difference between these types of works and the current study is that this research focuses on the diagnosis challenge in PD while these studies address the disease management for currently diagnosed patients. There is no proven biomarker for PD [82]; therefore, personalized medicine based on big data analytics could be a potential solution to PD diagnosis challenges.

In summary, none of the previous research studies in predictive analytics and healthcare analytics introduced or used any formal procedure to address the challenge of having many variables with very high degrees of missing values. And this study is the first to propose a formal framework that addresses this common challenge in working with EHR. Besides, to the best of my knowledge, this research, for the first time, introduces a CDSS for detecting and screening for PD that does not require any specific equipment or test and can be used by any primary care provider or nurse. This CDSS can be used as a tool integrated into EHR systems or as a standalone personalized medicine tool, especially in remote areas with limited access to specialists. Moreover, while most of the existing studies only use balanced datasets<sup>1</sup>, in the development of this CDSS, advanced imbalanced data learning techniques are employed to simulate the realistic situation of facing imbalanced distribution of patients with PD and those without PD. Additionally, in this study, an ensemble approach is used to integrate multiple classifiers to achieve the highest possible accuracy in detecting PD.

## 3. Methodology- Missing Care framework

In analyzing datasets similar to EHR data, we face the challenge of having many variables, most of them to 90%). There are two extreme and immediate solutions to this issue. One is to nume records to have records with reasonably populated values. Another tion, in the opposite direction, is first to remove variables remove the records with high missing values and, as a result, end up with a dataset that has completeness that is suitable for using imputation approaches. By pursuing the first solution, we will lose numerous records (in the case of EHR, records correspond to patients or encounter data). And by taking the second solution, we will deprive ourselves of a lot of variables (independent variables) that might indeed be strongly associated with the target variable.

One might say various imputation methods can be used to impute missing values. In fact, there is an extensive literature on missing values imputation methods in statistics and machine learning fields [83-87].

However, imputation methods are only appropriate when there is reasonable completeness in each variable. Acuna & Rodriguez [88] mentioned “rates of less than 1 % missing data are generally considered trivial, 1- 5% are manageable. However, 5-15% requires sophisticated methods to handle, and more than 15% may severely impact any kind of interpretation.” Many data analytics tools such as SAS Enterprise Miner automatically (by default) remove variables with more than 50% missing from further analysis and imputation. The reason is that to impute missing values, we usually need to use the values of other records for the same variable, and when most of the values (or a considerable $\mathrm { p o t } . ^ { \cdot \cdot } \mathrm { n }$ of them) are missing, the missing value degree was 98%, and many features had missing values around 60% to 90%, and imputing these variables with very high degrees of missingness was not appropriate. It needs that Missing Care is not a replacement for imputation methods. In fact, it is a pre-processing framework that prepares the data for more meaningful use of imputation methods when there is a reasonable degree of completeness in the data. In many fields, especially healthcare, even 50% completeness for a variable is not acceptable.

## Table 1. Notations for Missing Care Framework

Baesens et al. [29] extensively discuss data quality and trust in analytics works. Data quality was elaborated on in the introduction section, and here the “trust” part is discussed. The matter of trust in both data and analytics approaches is a critical factor in implementing DSS based on data analytics [29]. This is even more crucial in healthcare; working with physicians and clinicians as data analysts entails a remarkable liability and trust. Even if you use a complete and clean dataset to develop a CDSS, clinicians hardly trust the results, let alone if they learn that you have heavily imputed your data. Therefore, to enhance data-driven decision making in general and more specifically in healthcare, we need $\cdot ^ { \textrm { \tiny { 1 } } }$ gain the organizations’ leaders' trust and one of the prerequisites is to limit the level of imputation.

This challenge is addressed by introducing the Missing Care framework. Missing Care begins by using the initial dataset, ?? with ?? variables and ?? records. Next, kee $\mathbf { t } ^ { \mathsf { i n } \mathsf { \Omega } } \circ$ all variables in the data, only records with a reasonable degree of completeness, say $\delta \% ^ { 2 }$ will be $\nu _ { \in \cdot } \cdot _ { \cdot } ,$ and all other records will be removed. At this stage, we have dataset $D _ { 1 }$ containing all of the initial variables and only records with a high degree of completeness $( N _ { 1 } )$ ; therefore, a considerable number of records are removed. The next step is to identify the variables (features or independent variables) that are strongly associated with the target variable. In Section 3.1, a procedure is recommended for computing an importance level for all the variables and identifying the important ones.

Then, based on the final variables’ importance $( x _ { j } ^ { i m p } )$ top $p ^ { * }$ variables out of initial ?? variables are identifie d and selected for further analysis. In the next step, from the initia l dataset $D ,$ only selected $p ^ { * }$ variables are kept, and all other variables are removed. At this point, we have an updated dataset, $D _ { 2 }$ , which includes only a subset of variables (those that are strongly associated with the target variable) and all original records. The next step is to remove the records with very high missing values and keep only the records with at least ??% completeness. This dataset $( D ^ { * } )$ is the final dataset that will be used to develop the predictive models and has $p ^ { * }$ and $N ^ { * }$ records with $N ^ { * } > N _ { 1 } .$

## 3.1.Computing variables’ importance

Two data mining and machine learning methods for both classification and regression problems are recommended to compute the variables’ importance. Here, it needs to be noted that classification problems are the ones with a binary or categorical target variable, for instance, when we want to detect and diagnose a disease or when we want to predict the success or failure of a project. $\pmb { \Delta } _ { \mathbf { \lambda } \mathbf { \lambda } \mathbf { \lambda } }$ regression problems are the cases with a numeric target variable, which is measurable, such as predicting the value of a house or predicting the length of stay for a patient. At the end of this section, two $M i s , \dot { \cdots } \dot { }$ Care frameworks are presented; one for regression problems, and one for classification problems. If the problem is classification, logistic regression with l1 regularization (the same regularization that las $. 0 \mathrm { ~ } _ { \backprime } \mathrm { ~ } ^ { \overrightarrow { \mathbf { \alpha } } , \mathbf { \sigma } _ { \mathcal { S } } } )$ and random forests classifier [89] are used. And if the problem is regression, lasso, and random forests regressor are used. These methods are recommended for three reasons: first, one is representative of classical statistics (regression), and the other one is a representative of more advanced machine learning techniques (random forests); second, regressions are highly interpretable and random forests are highly accurate and capable of handling a large number of variables when there is a relatively small number of records available [89, 90]; and third, both methods provide some sort of variable importance.

Both logistic regression with l1 regularization and lasso regression train in a way to reduce the number of features in the predictive model and reduce the chance of over-fitting [91]. Where the linear regression is in the form of Eq. 1

$$
y = \beta_ {0} + \beta_ {1} x _ {1} + \dots + \beta_ {p} x _ {p} + \varepsilon\tag{1}
$$

Lasso minimizes the following (Eq. 2) to estimate the coefficients,

$$
M S E + \alpha \sum_ {j = 0} ^ {p} \bigl | \beta_ {j} \bigr |\tag{2}
$$

?????? is the mean squared error, $\beta _ { j }$ are coefficients of ?? features, and ?? is the parameter that adjusts the trade-off between accuracy on training data and the regularization. Higher ?? means forcing more $\beta _ { j }$ to be zero (removing the corresponding features from the model). Therefore, when lasso (or logistic regression with l1 regularization) is used, during the training process, important variables that are strongly associated with the target variable are kept in the model and other less important features will end up having zero coefficients, meaning they will be removed from the model. An importance measure is assigned to each feature included in the model. This importance is based on the R-square reduction (denoted by $R _ { j _ { r e d } } ^ { 2 } )$ after removing the variable from the model and in the end, all of the importance measures are normalized. The importance of variable ?? (denoted by $R e g _ { - } x _ { j } ^ { i m p } )$ is calculated as follows in Eq. 3,

$$
R e g _ {-} x _ {j} ^ {i m p} = \frac {R _ {j} ^ {2} {} _ {r e d}}{R _ {1} ^ {2} {} _ {r e d} + \cdots + R _ {p} ^ {2} {} _ {r e d}}\tag{3}
$$

The same is done for the logistic regression; however, instead of R-square reduction, the area under the chart and takes values between 0 and 1. The AUC reduction after removing variable ?? is denoted by $A U C _ { j _ { r e d } }$

$$
R e g \_ x _ {j} ^ {i m p} = \frac {A U C _ {j _ {r e d}}}{A U C _ {1 _ {r e d}} + \cdots + A U C _ {p _ {r e d}}}\tag{4}
$$

It needs to be noted that $R _ { j _ { r e d } } ^ { 2 }$ and $A U C _ { j _ { r e d } }$ for variables that are not included in the model are equal to zero, and as a result, their importance is zero as well.

In random forests models, the variable importance is calculated based on impurity reduction when a variable is used for splitting [92]. The impurity for regression models is based on the variance at each node and is calculated as shown in Eq. 5 and Eq. 6,

$$
\bar {y} _ {m} = \frac {\Sigma_ {i \in N _ {m}} y _ {i}}{N _ {m}}\tag{5}
$$

$$
v _ {m} = \frac {\sum_ {i \in N _ {m}} (y _ {i} - \bar {y} _ {m}) ^ {2}}{N _ {m}}\tag{6}
$$

Where $y _ { i }$ is the label (target variable value) for record ?? and $v _ { m }$ is variance at node m, with $N _ { m }$ observations. When variable ?? is used in the split in node ?? in a tree, variance reduction (????) is calculated as in Eq. 7,

$$
V R _ {j _ {m}} = v _ {m} - w _ {l e f t} v _ {l e f t \_ m} - w _ {r i g h t} v _ {r i g h t \_ m}\tag{7}
$$

where $w _ { l e f t }$ and $w _ { r i g h t }$ are the proportion of the records in each leaf. Variable $j ^ { \prime } { \bf s }$ importance at each tree is calculated based on the proportion of variance reduction using variable ?? in splits to the total variance reduction in all splits as shown in Eq. 8,

$$
V R _ {-} x _ {j} ^ {i m p} = \frac {\sum_ {m \in a l l n o d e d s p l i t e d u s i n g v a r i a b l e j} V R _ {j _ {m}}}{\sum_ {m \in a l l n o d e s} V R _ {m}}\tag{8}
$$

Next, $V R _ { - } x _ { j } ^ { i m p }$ is normalized using all variables’ importance in the tree (Eq. 9),

$$
N _ {-} V R _ {-} x _ {j} ^ {i m p} = \frac {V R _ {-} x _ {j} ^ {i m p}}{\sum_ {i \in p} V R _ {-} x _ {i} ^ {i m p}}\tag{9}
$$

Finally, the importance of variable $j ^ { \cdot \cdot }$ the random forests model, denoted by $R F _ { - } x _ { j } ^ { i m p }$ is computed based on the average variance reduction in all trees generated in the random forests model as in Eq. 10

$$
R F _ {-} x _ {j} ^ {i m p} = \frac {\sum_ {a l l t r e e s i n R F N _ {-} V R _ {-}} x _ {j} ^ {i m _ {i}}}{n u m b e r o f t r e e s i n R F}\tag{10}
$$

In classification models, the impurity is the Gini index at each node (Eq. 11),

$$
G i n i _ {m} = \sum_ {K} p _ {m k} (1 - p _ {m k})\tag{11}
$$

Where $p _ { m k }$ is the proportion of observation belonging to class ?? at node ?? (there are ?? classes in the data). When variable ?? is used in the split in node ?? in a tree, Gini reduction (???? ) is calculated as in Eq. 12,

$$
G R _ {j _ {m}} = G i n i _ {m} - w _ {l e f t} G i n i _ {l e f t \_ m} - w _ {r i g h t} G i n i _ {r i g h t \_ m}\tag{12}
$$

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
where  $w_{left}$  and  $w_{right}$  are the proportion of the records in each leaf. Variable j's importance at each tree is calculated based on the proportion of Gini reduction using variable j in splits to the total Gini reduction in all splits (Eq. 13),

 $GR\_x_{j}^{imp} = \frac{\sum_{m \in all\ node\ split\ using\ variable\ j^{GR\ j_{m}}}}{\sum_{m \in all\ nodes\ GR_{m}} }$  (13)

Next,  $GR\_x_{j}^{imp}$  is normalized using all variables' importance in the tree (Eq. 14),

 $N\_GR\_x_{j}^{imp} = \frac{GR\_x_{j}^{imp}}{\sum_{i \in p\ GR\_x_{i}^{imp}}}$  (14)

Framework 1- Missing Care Framework for regression problems

Given D, p, N, δ, α

1. Keep all p variables and only records that have at least δ% completeness:

 $D_{1}$  (p variables &amp;  $N_{1}$  records)

2. Train a lasso regression on  $D_{1}$ 

3. Using an appropriate value for α, identify the variables with non-zero coefficient  $p_{1}$ 

4. Calculate  $R_{j\ red}^{2}$  for all variables in  $p_{1}$ 

5. Normalize the values of  $R_{j\ red}^{2}$  and calculate variable importance,  $Reg\_x_{j}^{imp}$  using

 $Reg\_x_{j}^{imp} = \frac{R_{j\ red}^{2}}{R_{1\ red}^{2} + \cdots + R_{p\ red}^{2}}$ 

6. Train a random forests regressor on  $D_{1}$ 

7. Calculate variance reduction,  $VR\_x_{j}^{imp}$  for all variables at each tree

8. Normalize variance reductions using

 $N\_VR\_x_{j}^{imp} = \frac{VR\_x_{j}^{imp}}{\sum_{i \in p}\ VR\_x_{i}^{imp}}$ 

9. Calculate variable importance,  $RF\_x_{j}^{imp}$  based on normalized variance reductions for all trees in random forests using

 $RF\_x_{j}^{imp} = \frac{\sum_{all\ trees\ in\ RF}\ N\_VR\_x_{j}^{imp}}{number\ of\ trees\ in\ RF}$ 

10. Calculate the ultimate variables' importance as

 $x_{j}^{imp} = \frac{w_{Rsq}^{Reg}\ Reg_{x_{j}^{imp}} + w_{Rsq}^{RF}\ RF_{x_{j}^{imp}}}{w_{Rsq}^{Reg} + w_{Rsq}^{RF}}$ 

11. Identify top p* variables out of initial p variables as selected variables based on  $x_{j}^{imp}$ 

12. From D keep only selected p* variables and all records

 $D_{2}$  (p* variables &amp; N records)

13. From  $D_{2}$, keep only the records with at least δ% completeness:

 $D^{*}$  (p* variables &amp; N* records)

 $(N^{*} &gt; N_{1})$ 

14.  $D^{*}$: the final dataset with selected variables and records

Finally, the importance of variable j in the random forests, denoted by  $RF\_x_{j}^{imp}$  is computed based on the average Gini reduction in all trees generated in the random forests model as in Eq. 15
</div>

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$RF\_x_j^{imp} = \frac{\sum_{all\ trees\ in\ RFN\_GR\_x_j^{imp}}}{number\ of\ trees\ in\ RF}$ (15)

At this stage, the variables' importance in both regression and random forests models are available. Next a weight is assigned to each variable importance based on models' R-square for regression problems and models' AUC for classification problems, denoted by $w_{Rsq}^{Reg}, w_{Rsq}^{RF}, w_{AUC}^{Reg}$, and $w_{AUC}^{RF}$ respectively. The final importance of variable j is calculated as Eq. 16 and Eq. 17,

$x_j^{imp} = \frac{w_{Rsq}^{Reg}\text{ Reg }x_j^{imp} + w_{Rsq}^{RF}\text{ Reg }x_j^{imp}}{w_{Rsq}^{Reg} + w_{Rsq}^{RF}}$ for regression problems (16)

$x_j^{imp} = \frac{w_{AUC}^{Reg}\text{ Reg }x_j^{imp} + w_{AUC}^{RF}\text{ Reg }x_j^{imp}}{w_{AUC}^{Reg} + w_{AUC}^{RF}}$ for classification problems (17)

Framework 2-Missing Care Framework for classification problems

Given D, p, N, δ, α
1. From D, keep all p variables and only records that have at least δ% completeness:
$D_1$ (p variables &amp; $N_1$ records)
2. Train a logistic regression with II regularization of $D_1$
3. Using an appropriate value for α, identify the variables with non-zero coefficient $p_1$
4. Calculate $AUC_{j\_red}$ for all variables in $p_1$
5. Normalize the values of $AUC_{j\_red}$ and calculate variable importance, $Reg\_x_j^{imp}$ using
$Reg\_x_j^{imp} = \frac{AUC_{j\_red}}{AUC_{1\_red} + \cdots + AUC_{p\_red}}$
6. Train a random forests classifier of $D_1$
7. Calculate Gini reduction, $GR\_x_j^{imp}$ for all variables at each tree
8. Normalize Gini reduction's using,
$N\_GR\_x_j^{imp} = \frac{GR\_x_j^{imp}}{\sum_{i \in p} GR\_x_i^{imp}}$
9. Calculate $RF\_x_j^{imp}$ based on normalized Gini reductions for all trees in random forests using
$RF\_x_j^{imp} = \frac{\sum_{all\ trees\ in\ RF} N\_GR\_x_j^{imp}}{number\ of\ trees\ in\ RF}$
10. Calculate the ultimate variables' importance as
$x_j^{imp} = \frac{w_{AUC}^{Reg}\text{ Reg }x_j^{imp} + w_{AUC}^{RF}\text{ Reg }x_j^{imp}}{w_{AUC}^{Reg} + w_{AUC}^{RF}}$
11. Identify top p* variables out of initial p variables as selected variables based on $x_j^{imp}$
12. From D keep only selected p* variables and all records
$D_2$ (p* variables &amp; N records)
13. From $D_2$, keep only the records with at least δ% completeness:
$D^*$ (p* variables &amp; N* records)
$(N^* &gt; N_1)$
14. $D^*$: the final dataset with selected variables and records
</div>

Formal pseudo-code for Missing Care for both regression and classification problems are shown in Framework 1 and 2, and the notations are listed in Table 1.

An important point needs to be noted here. Even though the recommended techniques led to better performance compared to other variable selection methods such as relative importance in neural networks, and stepwise regression, it cannot necessarily be the case for all settings and datasets. Therefore, it is best if analysts experiment with various variable selection methods and apply the one that provides the best results for their data.

## 4. Data

In this section, the data, and also the data pre-processing and preparation steps that were taken before developing the final predictive models are described. In this research, a unique data retrieved from the largest relational healthcare data warehouse in the US, Cerner Health Facts® is used. Health Facts® contains more than two decades of data of 84 million unique patients in 133 million encounters from over 500 health care facilities across the US [93]. The initial data included millions of records and hundreds of variables across various tables that needed to be integrated, cleaned, and pre-processed. Figure 1 is a simplified diagram for this data, depicting the tables that are included in it and how they are related. In this diagram, primary and foreign keys that are used to merge various tables are specified; the primary key in each table is bold and Italic, and the foreign key is underlined. The patient table contains demographic information such as age, race, marital status, and gender. The medication table holds a complete set of variables on the medications that patients take; examples are medication name/ID, dosage, ordering physician, order date, unit costs, etc. The diagnosis table is home to the diagnosis information (ICD 9 and 10 codes). The encounter table contains all the variables related to the patients' visits. Variables such as admission and discharge dates, admitting physician, admission type, and admission source are in this table. Information about the patients’ vital signs such as blood pressure, temperature, and respiratory rate and their respective collection date and time is stored in the clinical event table. And finally, the lab procedure table contains all the information about the

patients’ lab tests. This table includes variables such as lab name, lab completion date, and results. Diagnosis and medication tables are used to label patients in the PD and control groups. And, variables in the patient, clinical event, and lab procedure tables are used in developing the models.

Data cleaning/pre-processing, especially for EHR, is a very critical and time-consuming task, and therefore a great deal of time and consideration was dedicated to it. This process also involved consulting with medical professionals to incorporate their expertise. Data retrieval from Health Facts® was based on ICD-9 (International Classification of Diseases) and ICD-10 diagnosis codes. An imbalanced dataset<sup>3</sup> is used in this study to have a fair and factual setting; as in the real world patient population, only a small percentage ith either ICD-9 or ICD-10 PD diagnosis codes were extracted, and that yielded data of 83,393 unique patients from about 1 million the size of 10 times larger than the PD group were extracted, and this yielded 833,921 unique patients having more than 5 million encounters.

![](/api/attachments/V5FF6CRY/fulltext/images/37d6ec10a239392165e69614537667354b83a2bc573652d34c1062ad984ab821.jpg)  
Figure 1-Cerner Data Diagram

Throughout the process, parts of data were discarded because not all information in various tables was available for all patients. The process started with merging the encounter<sup>4</sup> and diagnosis data tables, and this led to having data of 442,556 unique patients, out of which 83,393 were in the PD group and the rest in the control group. This data was from about 3 million encounters for these patients. The imbalanced ratio (number of patients in the PD group divided by the total number of patients) for this data was about 18.8%. In the next step, the PD group was double-checked against ICD-9, and ICD-10 diagnosis codes for PD and 4,203 patients were removed from the PD group because they did not have ICD 9 or ICD 10 diagnosis code for PD. To be as close as possible to the first PD diagnosis, the first encounter with PD diagnosis was kept, t make any changes to the number of

![](/api/attachments/V5FF6CRY/fulltext/images/517ea1f9256466a5b176d3c3547b82e2754b4355502c4223bc34002b94d5e656.jpg)  
Figure 2-Data Selection Steps

Next, the lab procedure table was cleaned and merged removing 40,943 PD patients and 197,951 patients in the control group because there was no lab data for these groups of patients. At this stage, the imbalanced ratio was 19.2%.

Considering only ICD codes to form the PD and control groups might not be entirely accurate because of potential errors such as data entry. To avoid this issue and ensure all patients in the PD group have PD

checking for ICD codes was taken. Reviewing the American Parkinson Disease Association (APDA) website (www.apdaparkinson.org), a list of medications that PD patients could take was formed (see Appendix I). Then, using the Health Facts® medication table that stores the information of all medications patients take, only patients in the PD group that take PD medications were kept, and others were removed. Additionally, all patients in the control group that take any PD medication were excluded. Conducting this two-stage identification using ICD codes and medications, the veracity of all patients in the PD group having PD and all patients in the control group not having PD was confirmed with a high degree of confidence. At this stage, the data was prepared to develop predictive models. This data included 15,669 unique PD and 160,722 unique patients in the control group and had an imbalanced ration of 8.9%. This data is called Master I. Data selection steps are summarized in Figure 2. There were many other data ing/pre-processing steps that

![](/api/attachments/V5FF6CRY/fulltext/images/97ac8b3541ccbc57de36b7acd6471c735da03fc608a4ac8df41886eb984f3d79.jpg)

After having Master I data in hand, Missing Care was applied to have the final data that contains all important variables with a reasonable degree of missing values. Master I included 81 variables, out of which many had very high missing values (as high as 98% missing!). Employing Missing Care, the majority of records with high missing values were removed to keep as many as variable possible with up to 30% missing. This yielded a dataset with 3705 records and 81 variables that is much smaller than Master I. Then, Missing Care was applied to this data to identify variables strongly associated with the target variable. After following Missing Care guidelines, 30 variables were identified as important variables. Then, going back to Master I, and only keeping these 30 variables, records with very high missing values were removed

Figure 3- Data Pre-processing Steps

to reach a reasonable missing values degree for the selected 30 variables. It resulted in a data with 15000 records, out of which 2000 were PD, and the rest belonged to the control group. This data, called Master II, was used to develop the final predictive models. Missingness in Master II was acceptable (maximum missing value was 37%) to apply imputation methods. A descriptive analysis of variables in Master II for both PD and control groups is available in Appendix II. Not employing Missing Care would lead to losing many variables with a strong association with the target. Without applying Missing Care, only the variables with at most 35% missingness (the same missingness threshold that was used for Master II) are kept, and it will result in a dataset with many records (113,759, considerably more than Master II’s records). However, this data will have only 7 variables, because most of the variables have missingness levels of 60% to 90%. This data is called Master III, and it is used to develop models and compare the models’ performance with the ones build on Master II. Data using Missing Care procedure compared to not using Missing Care is shown in Figure 4.

![](/api/attachments/V5FF6CRY/fulltext/images/45131340886151bf71e166063db9e7be5156da7e96010dccc3583efa7b15886b.jpg)  
Figure 4- Using Missing Care vs. Not Using Missing Care

## 5. Experiment Results

In this section, the experimental results of predictive models developed by employing Missing Care and also not employing Missing Care are provided. Logistic regression (LR), linear support vector machine (SVM-L), support vector machine with RBF kernel (SVM-RBF), neural networks (NN), random forests (RF), and gradient boosting (GB) are used to develop predictive models. For SVM and NN that are sensitive to the variables’ scale, all variables are transformed to a 0 to 1 scale. The parameters for each model have been tuned to get the best possible results, and 5-fold cross-validation is used to minimize the effect of data partitioning bias. First, the results of the models built without using Missing Care after over-sampling it

applying SIMO are presented. Then, the results of models developed based on SIMO-oversampled data by applying Missing Care are represented. Next, the results of the two sets of models are compared and the effectiveness of the Missing Care framework is shown. Table 2 shows the results of the models when Missing Care is not applied, and Table 3 represents models after employing Missing Care. As shown, using Missing Care, led to a significant improvement in the models’ performance (5% to 7% AUC increase across various models). Table 4 depicts the significance of this improvement at the level of 99% confidence. The reason is that Missing Care addresses data quality as a critical factor in analytics. Without using Missing Care, many important variables with high predictive power would be discarded from further analysis, and this would deteriorate the models’ performance. The improvement across various models is depicted in Figure 5 as well. It needs to be pointed out that after (and during) applying Missing Care, the data still has missing values. However, the degree of missingness at these stages is manageable by applying imputation methods. In this study, mean and mode were used to impute the missing values for the numeric and categorical variables, respectively. However, any other imputation methods can be used.

Table 2-Models without applying Missing Care (on SIMO-oversampled Master III)

<table><tr><td></td><td>LR</td><td>SVM-1</td><td>SVM-RBF</td><td>NN</td><td>RF</td><td>GB</td></tr><tr><td>AUC</td><td>73.63%</td><td>73.09%</td><td>73.11%</td><td>72.24%</td><td>78.02%</td><td>78.15%</td></tr><tr><td>SENSITIVITY</td><td>66.98%</td><td>64.35%</td><td>66.39%</td><td>66.08%</td><td>70.12%</td><td>70.37%</td></tr><tr><td>SPECIFICITY</td><td>66.08%</td><td>66.22%</td><td>66.13%</td><td>66.00%</td><td>70.15%</td><td>70.28%</td></tr></table>

Table 3- Models after applying Missing Care (on SIMO-oversampled Master II)

<table><tr><td></td><td>LR</td><td>SVM-L</td><td>SVM-RBF</td><td>NN</td><td>RF</td><td>GB</td></tr><tr><td>AUC</td><td>80.63%</td><td>79.87%</td><td>79.36%</td><td>77.63%</td><td>84.30%</td><td>84.63%</td></tr><tr><td>SENSITIVITY</td><td>73.15%</td><td>72.98%</td><td>72.85%</td><td>69.95%</td><td>75.80%</td><td>76.25%</td></tr><tr><td>SPECIFICITY</td><td>72.78%</td><td>72.46%</td><td>72.08%</td><td>69.83%</td><td>75.28%</td><td>75.17%</td></tr></table>

<table><tr><td colspan="7">Table 4-Statistical significance of effectiveness of Missing Care</td></tr><tr><td></td><td>LR</td><td>SVM-L</td><td>SVM-RBF</td><td>NN</td><td>RF</td><td>GB</td></tr><tr><td>AUC difference</td><td>6.998%***</td><td>6.79%***</td><td>6.25%***</td><td>5.39%***</td><td>6.25%***</td><td>6.49%***</td></tr><tr><td>p-value</td><td>4.1E-05</td><td>1.81E-06</td><td>5.46E-05</td><td>4.63E-05</td><td>1.36E-04</td><td>1.18E-04</td></tr><tr><td colspan="7">*** 99% confidence, ** 95% confidence, * 90% confidence---two-sample t-test, unequal variances</td></tr></table>

![](/api/attachments/V5FF6CRY/fulltext/images/e2b222987fb71e2750cb4db967ecbf47fd7c65dc7e2b89cb8c3e2049e8775fe4.jpg)  
Figure 5—AUC for models with and without Missing Care

Among various machine learning techniques, random forests and gradient boosting had the best performance. AUCs for these two models after applying Missing Care on Master II SIMO-oversampled data $\mathrm { i } \mathrm { s } ,$ modeling techniques. As was mentioned in the previous sections, imbalanced data is used in this study. There are various remedies for imbalanced data learning problems, one of which is synthetic informative minority over-sampling (SIMO) with two versions, SIMO and W-SIMO (Weighted-SIMO). Another popular under-sampling approach is random under-sampling (RUS). To have the best results, the performance of the are evaluated. The results of the models based on various over-sampling and under-sampling techniques are presented in Table 5 and Figure 6. In this over-sampling methods, $\mathrm { S I M C } ~ \mathrm { w } _ { \mathrm { a } } \colon$ the best. The significance of the improvement gained from employing SIMO and W-SIMO compared with SMOTE and RUS is shown in Table 6. As evident, not all differences are statistically significant. The results presented are the performance of the models on the validation data, which is in the original imbalanced distribution of the initial dataset.

Table 5-AUC for models built on Master II in various over and under-sampling techniques

<table><tr><td></td><td>LR</td><td>SVM-L</td><td>SVM-RBF</td><td>NN</td><td>RF</td><td>GB</td></tr><tr><td>SIMO</td><td>80.63%</td><td>79.87%</td><td>79.36%</td><td>77.63%</td><td>84.30%</td><td>84.63%</td></tr><tr><td>W_SIMO</td><td>80.53%</td><td>79.68%</td><td>79.20%</td><td>77.67%</td><td>84.34%</td><td>84.45%</td></tr><tr><td>SMOTE</td><td>80.31%</td><td>79.36%</td><td>79.29%</td><td>77.55%</td><td>84.21%</td><td>84.23%</td></tr><tr><td>RUS</td><td>80.08%</td><td>81.01%</td><td>80.26%</td><td>77.24%</td><td>84.12%</td><td>84.15%</td></tr></table>

Table 6- The significance of the difference between SIMO and SMOTE and RUS

<table><tr><td>Difference Between</td><td>RUS</td><td>SMOTE</td></tr><tr><td>GB Model/SIMO</td><td>0.48% *</td><td>0.40%***</td></tr><tr><td>p-value</td><td>0.0943</td><td>0.0016</td></tr><tr><td>RF Model/W_SIMO</td><td>0.22%**</td><td>0.13%</td></tr><tr><td>p-value</td><td>0.0111</td><td>0.2991</td></tr></table>

\*\*\* 99% confidence, \*\* 95% confidence, \* 90% confidence-----two-sample t-test, unequal variances

To further improve the accuracy of the models, multiple predictive models using an ensemble approach called, confidence margin ensemble [65] were combined. Ensemble approaches are the most beneficial when different models, with relatively similar (and good) performance, are combined. As the performance of RF and GB models were much better than LR, SVM, and NN, only RF and GB models were used to develop the confidence margin ensemble models. First, the ensemble models were developed using RF and GB built on is a marginal improvement compared to the individual models, RF and GB; this is observable in Figure 6.

Table 7- Confidence Margin ensemble of RF and GB in various over and under-sampling techniques

<table><tr><td></td><td>RUS</td><td>SMOTE</td><td>W_SIMO</td><td>SIMO</td></tr><tr><td>AUC</td><td>84.62%</td><td>84.65%</td><td>84.82%</td><td>84.97%</td></tr><tr><td>SENSITIVITY</td><td>75.70%</td><td>75.65%</td><td>76.05%</td><td>76.45%</td></tr><tr><td>SPECIFICITY</td><td>75.80%</td><td>75.57%</td><td>75.56%</td><td>75.88%</td></tr></table>

![](/api/attachments/V5FF6CRY/fulltext/images/8e18823c5211c00a289397b078963f21be07a93fbdf4797d057a4fcdb2b7ac11.jpg)  
Figure 6- AUC of RF and GB and their ensembles using various imbalanced data learning techniques

More models were integrated into the ensembles step by step to create even more accurate models. In Table 8 and Figure 7, the first column (point) shows the ensemble of RF and GB models based on SIMOoversampled data. Next, RF and GB models based on W\_SIMO-oversampled data were added to the ensemble, and there was an improvement in the performance. In the next stage, RF and GB models built based on SMOTE-oversampled data were added; at this stage, there were six models in the ensemble, and there was an improvement from AUC of 85.06% to 85.19%. Finally, RF and GB models based on RUS data were added, and the AUC of the ensemble of 8 models was 85.29%. The final ensemble model of 8 models is used in the development of CDSS to diagnose and screen for PD.

Table 8- Confidence Margin ensemble of RF and GB

<table><tr><td>ENSEMBLE OF</td><td>SIMO</td><td>SIMO &amp; W-SIMO</td><td>..., &amp; SMOTE</td><td>..., &amp; RUS</td></tr><tr><td>AUC</td><td>84.97%</td><td>85.06%</td><td>85.19%</td><td>85.29%</td></tr><tr><td>SENSITIVITY</td><td>76.45%</td><td>76.55%</td><td>76.15%</td><td>76.00%</td></tr><tr><td>SPECIFICITY</td><td>75.88%</td><td>75.44%</td><td>76.04%</td><td>76.29%</td></tr></table>

![](/api/attachments/V5FF6CRY/fulltext/images/81789ad4c4a519d9282dbf52987833040d422f6ff1dfc07eb5281d7303eb2ebc.jpg)  
Figure 7-AUC for the ensemble of RF and GB by adding more models

## 6. Robustness Checks

To ensure the Missing Care effectiveness and the proposed CDSS validity to detect PD, a series of robustness checks needed to be conducted. First, the effectiveness of Missing Care and the validity of the CDSS were evaluated for datasets with various imbalanced ratios. These datasets were formed by randomly removing portions of data belonging to the PD group. In this way, datasets with lower PD records’ ratios were created that were more realistic. Table 9 shows the performance of the CDSS in various imbalanced ratios. In each scenario, models are developed as the ensemble of RF and GB over SIMO, W-SIMO, SMOTE, and RUS. This table illustrates the AUC values with and without applying Missing Care, the difference between the two scenarios, and the difference significance.

Table 9- Difference between models with and without applying Missing Care (various imbalanced Ratio)

<table><tr><td>Imbalanced Ratio</td><td>10%</td><td>6.50%</td><td>4%</td><td>1.30%</td></tr><tr><td>Missing Care- AUC</td><td>85.19%</td><td>85.11%</td><td>84.71%</td><td>83.80%</td></tr><tr><td># of PD Patients</td><td>1500</td><td>975</td><td>600</td><td>195</td></tr><tr><td>NO Missing Care- AUC</td><td>78.69%</td><td>78.57%</td><td>78.50%</td><td>77.09%</td></tr><tr><td># of PD Patients</td><td>11376</td><td>7394</td><td>4550</td><td>1479</td></tr><tr><td>Difference btw Missing Care and NO missing Care</td><td>6.51%***</td><td>6.53%***</td><td>6.21%***</td><td>6.71%***</td></tr><tr><td>p-value for Difference</td><td>0.00016</td><td>0.00012</td><td>0.00098</td><td>0.00478</td></tr></table>

\*\*\* 99% confidence, \*\* 95% confidence, \* 90% confidence---two-sample t-test, unequal variances

Second, to confirm the effectiveness of Missing Care, it was applied to another disease, Diabetic Retinopathy (DR). DR is the most common eye complication for diabetic patients. And about 28% of diabetic patients experience this complication [95]. DR data is acquired from the same source (Cerner) as PD, and data preparation steps, similar to what has been done for PD data, are taken to pre-process the data. The data for DR has different characteristics (number of rows, variables, and missingness) compared to the data used for PD. Table 10 shows the characteristics of DR data, and Table 11 depicts the statistically significant improvement achieved by applying Missing Care.

Table 10- DR data characteristics

<table><tr><td># of variable</td><td># of Patients</td><td>Avg. Missing Rate</td><td>Max Missing Rate</td><td>Min Missing Rate</td></tr><tr><td>91</td><td>451,392</td><td>74.1%</td><td>97.8%</td><td>29.8%</td></tr></table>

<table><tr><td colspan="5">Table 11- Difference between models with and without applying Missing Care for DR</td></tr><tr><td>Imbalanced Ratio</td><td>AUC</td><td># of Variables</td><td># of Patients</td><td># of DR Patients</td></tr><tr><td>Missing Care- AUC</td><td>92.83%</td><td>30</td><td>64,562</td><td>9,943</td></tr><tr><td>NO Missing Care- AUC</td><td>88.54%</td><td>9</td><td>176,505</td><td>22,415</td></tr><tr><td>Difference</td><td>4.287%***</td><td></td><td></td><td></td></tr><tr><td>p-value for Difference</td><td>1.80571E-05</td><td colspan="3">*** 99% confidence, ** 95% confidence---two-sample test, unequal variances</td></tr></table>

## 7. Discussion

tools in improving the care for patients and also making care providing more efficient [3, 12, 25]. Widespread adoption of EHR (as an IS/IT tool) in the hospitals and clinics has led to the emergence of EHRbased healthcare predictive analytics research that brings about remarkable practical and medical values [3]. While various studies have shown the value of EHR data in analytics, the challenges associated with analyzing these types of data are rarely addressed in the literature. The prerequisite of a competent data analytics research is to have high-quality data [29]. One important aspect of data quality is data completeness, and EHR data severely suffers from data incompleteness. In this study, by introducing a new framework called Missing Care, this critical challenge is addressed. Using Missing Care, before developing any predictive model, out of numerous features available in EHR data (many of them having very high missing values), we can identify the features that are highly associated with the target variable. And for the rest of the analysis, those selected variables will be involved in the model building. Without employing

Missing Care, many important features with high predictive powers might be discarded, only because the majority of their values in the initial data are missing. In the experimental analysis, the improvement in the prediction accuracy of models after using the Missing Care framework is demonstrated. While Missing Care is introduced in the context of EHR, it can be applied to other datasets with EHR characteristics (many variables with high degrees of missing values). It needs to be emphasized that Missing Care does not deny the importance of imputation techniques, rather it helps preserve variables that could benefit from imputation in later stages of analysis, while they could be discarded at early stages due to very high missingness degrees.

Besides the immense traditional contribution of researchers to healthcare at the level of management and organizations, personalized medicine has received attention in the recent years, and prestigious journals have recognized personalized medicine through CDSSs as one of the promising and impactful streams of research [3, 20, 25, 26, 96]. CDSSs can enhance decision-making capabilities in care management at the patient level rather than the general population. In line with this recent movement in healthcare analytics literature, and consistent with the design science research paradigm that focuses on solving practical problems, a CDSS is undiagnosed neurological disorder. Employing this CDSS benefits. It will provide more information to patients about their health status, thus enabling them to be proactive. It also helps clinics and physicians in being prepared for treatment planning. Finally, it improves the specialty care delivery to patients.

The contributions of this study can be summarized in two categories. First, to the best of my knowledge, this is the first study that formally discusses the data quality issue of incompleteness in EHR data and introduces a framework to address this issue. The benefits of applying this framework are demonstrated through empirical experiments in various predictive modeling techniques. Second, in this study, a CDSS that can aid clinicians in diagnosing PD is developed. The superiority of this CDSS over the existing diagnostic methods is that it can be applied using only demographic and lab test information of the patients, and there is no need for more advanced equipment such as MRI equipment that is scarce in more remote areas.

## 7.1.Practical implications

The proposed framework, Missing Care, can be used in the development of predictive models based on EHR or other similar datasets. These predictive models can be used to enhance decision making in various contexts, including healthcare. The CDSS developed in this study can be employed in different forms and can be beneficial to all stakeholders in healthcare. It can be integrated into EHR systems and automatically provide the risk of having PD for patients. It also can be used as a standalone tool; then, primary care providers and even nurses can use it as a screening tool. Since employ, it can fill that are similar to the US rural areas with regards to healthcare accessibility. This CDSS is easy to use and accurate at the same time. The ensemble models developed in given the complexity of diagnosing PD is a very good accuracy for a screening tool that uses simple blood for patients, and earlier diagnosis can always allow for more effective treatments and interventions, and this could translate to cost-saving both for patients

Another benefit of this CDSS is identifying the risk factors for PD. Among the identified factors, some literature (to the best of my knowledge). These new factors could be potential leads for medical researchers to conduct more controlled clinical studies and evaluate their relationship with PD. Factors identified by the CDSS and medical studies that showed their connection to PD are age, gender [97]; alanine aminotransferase, aspartate aminotransferase, and, glucose [98]; platelet count and lymphocyte [99]; glomerular filtration rate [100]; blood Pressure and heart rate [101]; serum sodium and chloride [102]; blood monocytes [103]; and, white blood cell count [104]. No medical research was found studying the following factors that were identified by the CDSS: mean corpuscular volume, creatinine serum, specific gravity urine, partial thromboplastin time, blood urea nitrogen, basophils percent.

## 7.2.Limitations and future research

This work, similar to other analytics research based on EHR data, has the limitation of the initial labeling of patients to PD and non-PD before training the models. While most of the studies rely only on ICD diagnosis codes, in this study, a reliable measure is taken to mitigate the effect of this limitation by having a two-stage initial identification both based on the ICD diagnosis codes in the data and also the medications that patients take. Future research can be conducted by collecting data specific to the purpose of this research and in a more controlled manner, thereby providing causality inference.

## Acknowledgment

This work was conducted with data from the Cerner Corporation’s Health Facts database of electronic medical records provided by the Oklahoma State University Center for Health Systems Innovation (CHSI). expressed in this material are those of the Yasamin Vahdati, for proofreading the article, and Dr. Delen, Dr. Paiva, and, Dr. Miao from CHSI for providing the data.

## References

1. Goes, PB, Big Data and IS Research. M IS Quarterly, 2014. 38(3): p. iii-viii.

2. Chiang, R.H., et al., Strategic Value of Big Data and Business Analytics. 2018, Taylor & Francis.

3. Chen, H., R.H. Chiang, and VC. Storey, Business intelligence and analytics: From big data to big impact. MIS quarterly, 2012. 36(4).

4. Bertsimas, D., et al., Call for Papers—Special Issue of Management Science: Business Analytics: Submission deadline: September 16, 2012 Expected publication date: First Quarter 2014. Management Science, 2012. 58(7): p. 1422-1422.

5. Seidmann, A., Y. Jiang, and J. Zhang, Introduction to the Special Issue on Analyzing the impacts of advanced information technologies on business operations. Decision Support Systems, 2015. 76(C): p. 1-2.

6. M azón, J.-N., et al., Introduction to the special issue of Business Intelligence and the Web. Decision Support Systems, 2012. 52(4): p. 851-852.

7. Kauffman, R.J., D. Ma, and B. Yoo, Guest editorial: Market transformation to an IT-enabled services-oriented economy. Decision Support Systems, 2015(78): p. 65-66.

8. Miller, K. Big Data Analytics In Biomedical Research 2012 [cited 2019 June 17].

9. Huerta, T.R., et al., Electronic health record implementation and hospitals' total factor productivity. Decision Support Systems, 2013. 55(2): p. 450-458.

10. Jha, A.K., et al., A progress report on electronic health records in US hospitals. Health affairs, 2010. 29(10): p. 1951-1957.

Stat #52].

12. Angst, CM, et al., Social contagion and information technology diffusion: the adoption of electronic medical records in US hospitals. Management Science, 2010. 56(8): p. 1219-1241.

13. Baird, A., E. Davidson, and L. M athiassen, Reflective technology assimilation: facilitating electronic health record assimilation in small physician practices. Journal of Management Information Systems, 2017. 34(3): p. 664-694.

14. Bhargava, H.K. and A.N. Mishra, Electronic medical records and physician productivity: Evidence from panel data analysis. Management Science, 2014. 60(10): p. 2543-2562.

15. Ganju, K.K., H. Atasoy, and P.A. Pavlou, 'Where to, Doc?'Electronic Health Record Systems and the Mobility of Chronic Care Patients. Working paper, 2017. Zalt

16. Atasoy, H., P.-y. Chen, and K. Ganju, The spillover effects of health IT investments on regional healthcare costs. Management Science, 2017. 64(6): p. 2515-2534.

Safer? Management Science, 2018.

18. Lin, Y.-K., M. Lin, and H. Chen, Do Electronic Health Records Affect Quality of Care? Evidence from the HITECH Act. Information Systems Research, 2019.

Systems Research, 2010. 21(4): p. 796-809.

20. Gupta, A. and R. Sharda, Improving the science of healthcare delivery and informatics using modeling approaches. 2013, Elsevier.

21. Moores, T.T., Towards an integrated model of IT acceptance in healthcare. Decision Support Systems, 2012. 53(3): p. 507-516.

2016. 40(3): p. 553-573.

23. Glaser, J., et al., Advancing personalized health care through health information technology: an update from the American Health Information Community's Personalized Health Care Workgroup. Journal of the American Medical Informatics Association, 2008. 15(4): p. 391-396.

24. Johnson, M.P., K. Zheng, and R. Padman, Modeling the longitudinality of user acceptance of technology with an evidence-adaptive clinical decision support system. Decision Support Systems, 2014. 57: p. 444-453.

25. Fichman, R.G., R. Kohli, and R. Krishnan, Editorial overview—the role of information systems in healthcare: current research and future trends. Information Systems Research, 2011. 22(3): p. 419-428.

26. Lin, Y.-K., et al., Healthcare predictive analytics for risk profiling in chronic care: A Bayesian multitask learning approach. M IS Quarterly, 2017. 41(2).

27. Agarwal, R. and V. Dhar, Big data, data science, and analytics: The opportunity and challenge for IS research. Information Systems Research, 2014. 25(3): p. 443–448.

28. Shmueli, G. and O.R. Koppius, Predictive analytics in information systems research. MIS quarterly, 2011: p. 553-572.

29. Baesens, B., et al., Transformational Issues of Big Data And Analytics in Networked Business. M IS quarterly, 2016. 40(4).

30. Jetley, G. and H. Zhang, Electronic health records in IS research: Quality issues, essential thresholds and remedial actions. Decision Support Systems, 2019. 126: p. 113137.

31. Baesens, B., Analytics in a big data world: The essential guide to data science and its applications. 2014: John Wiley & Sons.

32. M oges, H.-T., et al., A multidimensional analysis of data quality for credit risk management: New insights and challenges. Information & Management, 2013. 50(1): p. 43-58.

33. Du, J. and L. Zhou, Improving financial data quality using ontologies. Decision Support Systems, 2012. 54(1): p. 76-86.

34. Bardhan, I., et al., Predictive analytics for readmission of patients with congestive heart failure. Information Systems Research, 2014. 26(1): p. 19-39.

35. Yet, B., et al., Decision support system for Warfarin therapy management using Bayesian networks. Decision Support Systems, 2013. 55(2): p. 488-498.

36. NINDS, Parkinson's Disease: Challenges, Progress, and Promise. 2015, National Institutes of Health.

37. Parkinson's-Foundation. Parkinson's Statistics. [cited 2019 June 20].

38. Inacio, P. Distinct Brain Activity Patterns Captured by EEG May Help in Treating Parkinson’s, Study Suggests. 2019 [cited 2019 June 20].

39. Barjis, J., G. Kolfschoten, and J. M aritz, A sustainable and affordable support system for rural healthcare delivery. Decision Support Systems, 2013. 56: p. 223-233.

40. Li, Y., et al., Designing utilization-based spatial healthcare accessibility decision support systems: A case of a regional health plan. Decision Support Systems, 2017. 99: p. 51-63.

41. Varshney, U., Mobile health: Four emerging themes of research. Decision Support Systems, 2014. 66: p. 20-35.

42. Piri, S., D. Delen, and T. Liu, A synthetic informative minority over-sampling (SIMO) algorithm leveraging support vector machine to enhance learning from imbalanced datasets. Decision Support Systems, 2018. 106: p. 15-29.

43. Von Alan, R.H., et al., Design science in information systems research. M IS quarterly, 2004. 28(1): p. 75-105.

44. Padmanabhan, B., Z. Zheng, and SO. Kimbrough, An empirical analysis of the value of complete information for eCRM models. Mis Quarterly, 2006: p. 247-267.

45. Ma, L., R. Krishnan, and A.L. Montgomery, Latent homophily or social influence? An empirical analysis of purchase within a socia network. Management Science, 2014. 61(2): p. 454-473.

46. Coussement, K., S. Lessmann, and G. Verstraeten, A comparative analysis of data preparation algorithms for customer churn prediction: A case study in the telecommunication industry. Decision Support Systems, 2017. 95: p. 27-36.

47. Saboo, A.R., V. Kumar, and I. Park, Using Big Data to Model Time-Varying Effects for Marketing Resource (Re) Allocation. MIS Quarterly, 2016. 40(4).

48. Abbasi, A., et al., Metafraud: a meta-learning framework for detecting financial fraud. M is Quarterly, 2012. 36(4).

49. Kuzey, C., A. Uyar, and D. Delen, The impact of multinationality on firm value: A comparative analysis of machine learning techniques. Decision Support Systems, 2014. 59: p. 127-142.

approach to de-anonymizing the bitcoin blockchain. Journal of Management Information Systems, 2019. 36(1): p. 37-73.

51. Breuker, D., et al., Comprehensible Predictive Models for Business Processes. MIS Quarterly, 2016. 40(4): p. 1009-1034.

52. Fang, X., et al., Predicting adoption probabilities in social networks. Information Systems Research, 2013. 24(1): p. 128-145.

Mis Quarterly, 2013: p. 1093-1112.

54. Stieglitz, S. and L. Dang-Xuan, Emotions and information diffusion in social media—sentiment of microblogs and sharing behavior. Journal of management information systems, 2013. 29(4): p. 217-248.

55. Bao, Y. and A. Datta, Simultaneously discovering and quantifying risk types from textual risk disclosures. Management Science, 2014. 60(6): p. 1371-1391.

56. Kumar, N., et al., Detecting review manipulation on online platforms with hierarchical supervised learning. Journal of Management Information Systems, 2018. 35(1): p. 350-380.

111-124.

58. Xie, J., et al., Readmission Prediction for Patients with Heterogeneous Hazard: A Trajectory-Based Deep Learning Approach. 2018

59. Ben-Assuli, O. and R. Padman, Trajectories of Repeated Readmissions of Chronic Disease Patients: Risk Stratification, Profiling, and Prediction. MIS Quarterly, 2019(Forthcoming).

60. Zolbanin, H.M. and D. Delen, Processing electronic medical records to improve predictive analytics outcomes for hospital readmissions. Decision Support Systems, 2018. 112: p. 98-110.

online: an empirical study of social support among patients. Information Systems Research, 2014. 25(4): p. 690-709.

62. Chen, L., A. Baird, and D. Straub, Fostering Participant Health Knowledge and Attitudes: An Econometric Study of a Chronic Disease-Focused Online Health Community. Journal of Management Information Systems, 2019. 36(1): p. 194-229.

63. Wang, X., et al., Mining user-generated content in an online smoking cessation community to identify smoking status: A machine learning approach. Decision Support Systems, 2019. 116: p. 26-34.

64. Wang, T., et al., Directed disease networks to facilitate multiple-disease risk assessment modeling. Decision Support Systems, 2019: p. 113171.

65. Piri, S., et al., A data analytics approach to building a clinical decision support system for diabetic retinopathy: Developing and deploying a model ensemble. Decision Support Systems, 2017. 101: p. 12-27.

66. Zhang, W. and S. Ram, A Comprehensive Analysis of Triggers and Risk Factors for Asthma Based on Machine Learning and Large Heterogeneous Data Sources. MIS Quarterly, 2019(Forthcoming).

67. Wang, G., J. Li, and W.J. Hopp, Personalized Health Care Outcome Analysis of Cardiovascular Surgical Procedures. 2017.

68. Ahsen, M.E., M.U.S. Ayvaci, and S. Raghunathan, When algorithmic predictions use human-generated data: A bias-aware classification algorithm for breast cancer diagnosis. Information Systems Research, 2018.

69. Hsu, W.-Y., A decision-making mechanism for assessing risk factor significance in cardiovascular diseases. Decision Support Systems, 2018. 115: p. 64-77.

70. Meyer, G., et al., A machine learning approach to improving dynamic decision making. Information Systems Research, 2014. 25(2): p. 239-263.

71. Gómez-Vallejo, H., et al., A case-based reasoning system for aiding detection and classification of nosocomial infections. Decision Support Systems, 2016. 84: p. 104-116.

72. Dag, A., et al., A probabilistic data-driven framework for scoring the preoperative recipient-donor heart transplant survival. Decision Support Systems, 2016. 86: p. 1-12.

73. Topuz, K., et al., Predicting graft survival among kidney transplant recipients: A Bayesian decision support model. Decision Support Systems, 2018. 106: p. 97-109.

74. Somanchi, S., I. Adjerid, and R. Gross, To Predict or Not to Predict: The Case of Inpatient Admissions from the Emergency Department. Available at SSRN 3054619, 2017.

75. Jankovic, J., Parkinson’s disease: clinical features and diagnosis. Journal of neurology, neurosurgery & psychiatry, 2008. 79(4): p. 368-376.

76. Hughes, A.J., S.E. Daniel, and A.J. Lees, Improved accuracy of clinical diagnosis of Lewy body Parkinson’s disease. Neurology, 2001. 57(8): p. 1497-1499.

77. Fujimaki, M., et al., Serum caffeine and metabolites are reliable biomarkers of early Parkinson disease. Neurology, 2018. 90(5): p. e404-e411.

78. Feigenbaum, D., et al., Tear Proteins as Possible Biomarkers for Parkinson’s Disease (S3. 006). 2018, AAN Enterprises.

79. Arroyo-Gallego, T., et al., Detecting Motor Impairment in Early Parkinson’s Disease via Natural Typing Interaction With Keyboards: Validation of the neuroQWERTY Approach in an Uncontrolled At-Home Setting. Journal of medical Internet research, 2018. 20(3): p. e89.

2361.

81. Zhan, A., et al., Using smartphones and machine learning to quantify Parkinson disease severity: the mobile Parkinson disease score. JAMA neurology, 2018. 75(7): p. 876-880.

82. Rizek, P., N. Kumar, and M S Jog, An update on the diagnosis and treatment of Parkinson disease. Cmaj, 2016. 188(16): p. 1157-1165. 83. Allison, P.D., Missing data. Vol. 136. 2001: Sage publications.

84. Nakai, M. and W. Ke, Review of the methods for handling missing data in longitudinal data analysis. International Journal of Mathematical Analysis, 2011. 5(1): p. 1-13.

85. Wells, B.J., et al., Strategies for handling missing data in electronic health record derived data. Egems, 2013. 1(3).

86. Holan, S.H., et al., Bayesian multiscale multiple imputation with implications for data confidentiality. Journal of the American Statistical Association, 2010. 105(490): p. 564-577.

2019: p. 1-24.

88. Acuna, E. and C. Rodriguez, The treatment of missing values and its effect on classifier accuracy, in Classification, clustering, and data mining applications. 2004, Springer. p. 639-647.

89. Breiman, L., Random forests. Machine learning, 2001. 45(1): p. 5-32.

90. Ishwaran, H., Variable importance in binary regression trees and forests. Electronic Journal of Statistics, 2007. 1: p. 519-537.

91. Tibshirani, R., Regression shrinkage and selection via the lasso. Journal of the Royal Statistical Society: Series B (M ethodological), 1996. 58(1): p. 267-288.

92. Breiman, L., Classification and regression trees. 1984, Belmont, CA: Wadsworth.

93. DeShazo, J.P. and M.A. Hoffman, A comparison of a multistate inpatient EHR database to the HCUP Nationwide Inpatient Sample. BMC health services research, 2015. 15(1): p. 384.

94. Chawla, N.V., et al., SMOTE: synthetic minority over-sampling technique. Journal of artificial intelligence research, 2002. 16: p. 321- 357.

95. Zhang, X., et al., Prevalence of diabetic retinopathy in the United States, 2005-2008. Jama, 2010. 304(6): p. 649-656.

96. Bretthauer, K.M. and S. Savin, Introduction to the Special Issue on Patient‐Centric Healthcare Management in the Age of Analytics. Production and Operations Management, 2018. 27(12): p. 2101-2102.

97. Moisan, F., et al., Parkinson disease male-to-female ratios increase with age: French nationwide study and meta-analysis. J Neurol Neurosurg Psychiatry, 2016. 87(9): p. 952-957.

98. Cereda, E., et al., Low cardiometabolic risk in Parkinson's disease is independent of nutritional status, body composition and fat distribution. Clinical nutrition, 2012. 31(5): p. 699-704.

99. Qin, Y.-H., et al., The role of red cell distribution width in patients with Parkinson’s disease. Int J Clin Exp M ed, 2016. 9(3): p. 6143- 6147.

100.Nam, G.E., et al., Chronic renal dysfunction, proteinuria, and risk of Parkinson's disease in the elderly. Movement Disorders, 2019. 34(8): p. 1184-1191.

101.Norcliffe‐Kaufmann, L., et al., Orthostatic heart rate changes in patients with autonomic failure caused by neurodegenerative synucleinopathies. Annals of neurology, 2018. 83(3): p. 522-531.

102.Mao, C.j., et al., Serum sodium and chloride are inversely associated with dyskinesia in Parkinson's disease patients. Brain and behavior, 2017. 7(12): p. e00867.

103.Grozdanov, V., et al., Inflammatory dysregulation of blood monocytes in Parkinson’s disease patients. Acta neuropathologica, 2014. 128(5): p. 651-663

104.Fisher, P.R. Measuring Altered White Blood Cell Functionality as a Biomarker of Parkinson’s Disease. 2015 [cited 2020 3/22/2020]; Available from: https://www.michaeljfox.org/grant/measuring-altered-white-blood-cell-functionality-biomarker-parkinsons-disease.

## Appendices

Appendix I- List of PD Medications

<table><tr><td>Carbidopa-Levodopa</td></tr><tr><td>Pramipexole</td></tr><tr><td>Ropinirole</td></tr><tr><td>Benztropine</td></tr><tr><td>Amantadine</td></tr><tr><td>Selegiline</td></tr><tr><td>Carbidopa/Entacapone/Levodopa</td></tr><tr><td>Trihexyphenidyl</td></tr><tr><td>Rasagiline</td></tr><tr><td>Ropinirole</td></tr><tr><td>Rotigotine</td></tr><tr><td>Carbidopa</td></tr><tr><td>Tolcapone</td></tr><tr><td>Levodopa</td></tr></table>

Appendix II- Descriptive statistics for the patients in both PD and control groups

<table><tr><td colspan="4">PD PATIENTS</td><td colspan="3">CONTROL PATIENTS</td></tr><tr><td>Variables</td><td>Mean</td><td>STD</td><td>Median</td><td>Mean</td><td>STL</td><td>Median</td></tr><tr><td>Alanine Aminotransferase SGPT</td><td>21.83</td><td>19.46</td><td>18.00</td><td>32.72</td><td>34.70</td><td>26.00</td></tr><tr><td>Alkaline Phosphatase</td><td>85.88</td><td>39.72</td><td>78.00</td><td>93.60</td><td>48.24</td><td>83.50</td></tr><tr><td>Anion Gap</td><td>9.01</td><td>3.08</td><td>9.00</td><td>8.99</td><td>3.16</td><td>9.00</td></tr><tr><td>Aspartate Aminotransferase</td><td>30.91</td><td>33.58</td><td>23.00</td><td>30.87</td><td>59.24</td><td>25.00</td></tr><tr><td>Basophils Percent</td><td>0.51</td><td>0.30</td><td>0.50</td><td>0.55</td><td>0.34</td><td>0.55</td></tr><tr><td>Bilirubin Total</td><td>0.70</td><td>0.46</td><td>0.60</td><td>0.74</td><td>0.70</td><td>0.60</td></tr><tr><td>Blood Pressure, Systolic</td><td>131.08</td><td>14.66</td><td>129.60</td><td>129.71</td><td>16.58</td><td>129.89</td></tr><tr><td>Blood Urea Nitrogen</td><td>21.75</td><td>12.83</td><td>19.00</td><td>18.92</td><td>13.33</td><td>15.00</td></tr><tr><td>Carbon Dioxide</td><td>25.94</td><td>3.85</td><td>20.00</td><td>25.83</td><td>3.86</td><td>25.85</td></tr><tr><td>Chloride Serum</td><td>104.78</td><td>4.92</td><td>105.00</td><td>104.09</td><td>4.71</td><td>104.00</td></tr><tr><td>Creatinine Serum</td><td>1.07</td><td>0.62</td><td>0.90</td><td>1.08</td><td>0.71</td><td>0.90</td></tr><tr><td>Glomerular Filtration Rate</td><td>58.04</td><td>16.64</td><td>10.00</td><td>60.70</td><td>21.52</td><td>60.00</td></tr><tr><td>Glucose Serum</td><td>113.87</td><td>37.40</td><td>104.00</td><td>115.39</td><td>39.72</td><td>104.00</td></tr><tr><td>Heart Rate</td><td>80.54</td><td>10.26</td><td>81.86</td><td>82.07</td><td>11.58</td><td>81.86</td></tr><tr><td>Height</td><td>65.53</td><td>3.54</td><td>65.47</td><td>65.46</td><td>3.60</td><td>65.47</td></tr><tr><td>International Normalized Ratio</td><td>1.27</td><td>0.72</td><td>1.19</td><td>1.25</td><td>0.41</td><td>1.15</td></tr><tr><td>Lymphocyte Percent</td><td>19.91</td><td>7.67</td><td>21.39</td><td>21.62</td><td>10.27</td><td>21.39</td></tr><tr><td>Mean Corpuscular Volume</td><td>91.58</td><td>5.89</td><td>91.80</td><td>89.64</td><td>6.74</td><td>89.90</td></tr><tr><td>Mean Platelet Volume</td><td>8.7</td><td>1.3</td><td>8.7</td><td>8.73</td><td>1.24</td><td>8.7</td></tr><tr><td>Monocyte Percent</td><td>8.12</td><td>2.71</td><td>7.90</td><td>7.87</td><td>2.80</td><td>7.90</td></tr><tr><td>Partial Thromboplastin Time</td><td>32.60</td><td>8.48</td><td>32.00</td><td>32.86</td><td>8.96</td><td>32.79</td></tr><tr><td>Platelet Count</td><td>219.90</td><td>88.24</td><td>208.00</td><td>231.45</td><td>96.67</td><td>222.00</td></tr><tr><td>Prothrombin Time</td><td>14.17</td><td>3.92</td><td>13.60</td><td>14.07</td><td>3.98</td><td>13.60</td></tr><tr><td>Sodium</td><td>139.21</td><td>3.86</td><td>139.00</td><td>138.61</td><td>3.67</td><td>139.00</td></tr><tr><td>Specific Gravity Urine</td><td>1.016</td><td>0.005</td><td>1.015</td><td>1.015</td><td>0.006</td><td>1.015</td></tr><tr><td>Weight</td><td>167.91</td><td>36.40</td><td>176.02</td><td>178.89</td><td>42.28</td><td>177.42</td></tr><tr><td>White Blood Cell Count</td><td>8.27</td><td>3.37</td><td>7.60</td><td>8.57</td><td>3.70</td><td>7.90</td></tr><tr><td>Age</td><td>77.12</td><td>9.22</td><td>78.00</td><td>59.49</td><td>20.06</td><td>61.00</td></tr><tr><td></td><td>Male</td><td>Female</td><td></td><td>Male</td><td>Female</td><td></td></tr><tr><td>Gender</td><td>55%</td><td>45%</td><td></td><td>44%</td><td>56%</td><td></td></tr></table>

## Biographical Note

Saeed Piri (spiri@uoregon.edu) is an Assistant Professor at Lundquist College of Business, University of Oregon. His research interests lie in data analytics with a particular focus on healthcare. His research contributes to both data mining methodologies, such as imbalanced data learning, ensemble modeling, and association analysis and also data analytics applications, such as developing clinical decision support systems and personalized medicine. In addition, Dr. Piri has been studying value-based payment systems in healthcare, online retail platforms, and electronic medical records systems. In his works, he employs advanced machine learning te chniques and also classical empirical methods.

Affiliation and contact information

Saeed Piri

Assistant Professor

Operations and Business Analytics Department

Lundquist College of Business, University of Oregon

Office phone: 541-346-7314

Email: spiri@uoregon.edu

Saeed Piri- Conceptualization; Data curation; Formal analysis; Investigation; Methodology; Project administration; Resources; Software; Validation; Visualization; Roles/Writing.

## Highlights

 Implementation of electronic health record (EHR) systems have been evolving

 In this study, the data quality issue of very high degrees of missing values in EHR data is discussed

 A new framework called ‘Missing Care’ is introduced to address this issue

 A clinical decision support system (CDSS) for Parkinson’s disease is developed

 Advanced imbalanced data learning and ensemble methods are employed to develop the CDSS
