---
otero_id: 8122
otero_key: "FKU98QRH"
title: "A decision-making mechanism for assessing risk factor significance in cardiovascular diseases"
authors: "Wei-Yen Hsu"
year: "2018"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2018.09.004"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
<table><tr><td>PII:</td><td>S0167-9236(18)30155-6</td></tr><tr><td>DOI:</td><td>doi:10.1016/j.dss.2018.09.004</td></tr><tr><td>Reference:</td><td>DECSUP 12990</td></tr><tr><td>To appear in:</td><td>Decision Support Systems</td></tr><tr><td>Received date:</td><td>12 March 2018</td></tr><tr><td>Revised date:</td><td>22 August 2018</td></tr><tr><td>Accepted date:</td><td>21 September 2018</td></tr></table>

## Accepted Manuscript

A decision-making mechanism for assessing risk factor significance in cardiovascular diseases

Decision Support Systems

![](/api/attachments/FKU98QRH/fulltext/images/13aa60ad7eb5dccd044ae4444aa11ecf1d03a4630419082e1472cc7eb605baa0.jpg)

Wei-Yen Hsu

Please cite this article as: Wei-Yen Hsu , A decision-making mechanism for assessing risk factor significance in cardiovascular diseases. Decsup (2018), doi:10.1016/ j.dss.2018.09.004

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# A decision-making mechanism for assessing risk factor significance in cardiovascular diseases

Wei-Yen Hsu<sup>1,2,3,</sup>\*

<sup>1</sup>Department of Information Management, National Chung Cheng University

No.168, Sec. 1, University Rd., Minhsiung Township, Chiayi County 621, Taiwan

<sup>2</sup>Advanced Institute of Manufacturing with High-tech Innovations, National Chung Cheng University,

Minhsiung, Chiayi, Taiwan

<sup>3</sup>Center for Innovative Research on Aging Society (CIRAS), National Chung Cheng University,

Minhsiung, Chiayi, Taiwan

\*Corresponding author: Wei-Yen Hsu

Email: shenswy@gmail.com; shenswy@mis.ccu.edu.tw

Tel: +886-5-2720411 #34621

Fax: +886-5-2721501

# ACCEPTED MANUSCRIPT

## Abstract

Cardiovascular diseases (CVDs) are severe diseases whose growing incidence worldwide has spurred increased national healthcare spending. Despite numerous diagnostic and treatment suggestions, CVDs continue to merit investigation due to their diverse risk factors, some of which are positively, negatively, or not correlated. To assist doctors and researchers in identifying the significance of CVD risk factors, in this study we propose a novel ranking and attribute (or feature) selection algorithm. We applied seven popular machine learning technologies to generate attribute-ranked datasets in order to identify the ideal number of factors/attributes for each classifier. Above all, the results of the comparisons indicate that the performance of parts of factors after ranking and attribute selection was significantly better than the performance of whole factors and that of several state-of-the-art algorithms. Since such knowledge can aid the proper selection of factors of CVD patients and thereby assist doctors in making better decisions in diagnostics and treatment, our results can reduce treatment costs and thus lower the economic burden of healthcare.

Keywords: Decision support systems; medical decision making; cardiovascular diseases; feature ranking; radial basis function network

## 1. Introduction

Cardiovascular diseases (CVDs) rank among the most severe diseases worldwide and deserve researchers’ attention; CVDs’ prevalence and mortality rates increase every year [1]. CVDs include hypertension, hyperglycemia, stroke, myocardial infarction, heart attack, low blood pressure, thrombosis, and arteriosclerosis, among others, all of which have similar causes, processes, and therapeutic treatments. Depending on which organ or system needs treatment, care for CVDs can require cardiologists, thoracic surgeons, vascular surgeons, neurologists, and/or interventional radiologists.

Worldwide, roughly 16.5 million people die of CVDs each year [2]. In Taiwan, for example, 2015 statistics from the national Department of Health revealed that approximately 1.45 million people in Taiwan have heart disease, one in 19 people older than 15 years develops a CVD or other heart disease, and one in five people older than 65 years is a patient for heart disease. At a global scale, although cancer continues to be the top cause of death, until 2011 CVDs ranked second or third among the 10 most common causes of death for the previous 25 years. Unlike certain types of cancer, most CVDs are easy to ignore because their symptoms can be unobtrusive, but CVDs are nevertheless severe, often fatal

# ACCEPTED MANUSCRIPT

diseases.

In research on CVDs, low-density lipoprotein cholesterol (LDL-C) is generally regarded as “bad” cholesterol because it attaches to the vascular wall [3, 4]. Since low-density lipoproteins transport cholesterol to arteries, high levels of LDL-C can result in CVDs, including atherosclerosis, myocardial infarction, and stroke, as well as peripheral arterial diseases.

C-reactive protein (CRP), an acute-phase reactant protein originally used as an index for inflammation, responds to pneumococcal C polysaccharide [5, 6]. Recently, various epidemiological clinical experiments have confirmed that CRP is an independent factor for diagnosing or predicting atherosclerosis and CVDs. An increasing number of studies have also found that high-sensitivity CRP (hsCRP) can detect trace increases of blood CRP [7], which is a risk marker of CVDs [8–10]. In short, the higher the hsCRP, the greater the risk of stroke and myocardial infarction; critical values provided by the American Heart Association indicate that hsCRP < 0.1 mg/dL represents low risk, 0.1–0.3 mg/dL represents moderate risk, and >0.3 mg/dL represents great risk [11, 12]. At the same time, numerous large-scale studies have identified other CVD risk factors, including age, gender, obesity, family history, smoking, hypertension, diabetes, and high cholesterol. General tests can detect many other factors, although not all of them influence CVDs.

## 1.1. Motivation

Detecting CVD factors is even more complex in today’s era of information overload. Amid the countless data that CVDs produce at once, extracting useful information can be extremely difficult. With the accumulation of time, such data will become even more numerous and complex, which will further complicate the process of identifying useful, accurate information within limited timeframes. Moreover, traditional data analysis techniques and tools can hardly manage such large quantities of data; otherwise, those techniques and tools can be incompatible with the information in the datasets.

Consequently, grouping and classifying data are important directions in research on ways to compile and access information. The quality of the grouping or classification results depends primarily on the attributes of the data used in classification, whose contributions to classification are not always beneficial. Promoting an appropriate rate of classification is therefore an appropriate means of screening attributes for analysis.

Among the possible solutions to that end is feature selection [13, 14], also known as subset of attributes selection. Common in machine learning, feature selection, when combined with a learning algorithm, can optimize efficiency by selecting attributes with differential capacities relative to the original attribute set, which can thereby aid in determining the best attribute subset [15, 16]. In simpler terms, for further research, users need to filter out invalid, influential, repetitive, or noisy attributes via feature selection in order to retain the attributes that actually affect the performance indicators.

An asset in that process is the improved minimum redundancy maximum relevance (mRMR) b mRMR, we aimed to provide a basis for minimizing diversions, reducing the sizes of the datasets, and increasing operational efficiency, all to help medical staff and researchers to more easily determine the significance of attributes—namely, risk factors—and reduce time costs. We also sought to verify the accuracy of the method by using certain attributes that were previously judged as critical by researchers or doctors.

In this study, we propose a novel feature selection algorithm, improved mRMR, to optimally identify the most influential risk factors among the plethora of CVD risk factors, including age, weight, hypertension, and smoking. In doing so, we aimed to help researchers to judge the attribution of risk factors for CVDs toward maintaining, if not improving, accuracy with parts of the attributes that are identical or superior to whole attributes. By extension, we wanted to help physicians to confirm the importance and contributions of attributes in order to more efficiently gauge the influence of specific factors.

## 1.2. Related work

## 1.2.1. hsCRP

Atherosclerosis, a chronic inflammatory disease characterized by thickened blood vessel walls due to vascular fibrosis and lipid deposition, can cause stroke, myocardial infarction, and surrounding vascular obstruction. Some inflammation-related biomarkers that are detectable during the development of atherosclerosis appear in CRP, which is the cheapest, most convenient, most widely available, and longest-studied inflammation index for clinical use. Several studies have shown CRP’s power in estimating atherosclerosis-related diseases, whereas others have explored measurements for trace CRP, including hsCRP.

After acute tissue injury, increased CRP concentration signifies inflammation. Though neither exclusive nor indicative of causes, hsCRP can reflect low-grade chronic inflammation and be directly

# ACCEPTED MANUSCRIPT

involved in the promotion of atherosclerosis. Several studies have proposed that hsCRP can be divided into three classes: hsCRP < 1 mg/dL represents low risk, 1–3 mg/dL represents moderate risk, and >3 mg/L represents high risk of developing atherosclerosis. Numerous studies have also shown that, in healthy males without obvious symptoms, an increased degree of CRP is positively associated with the risk of primary myocardial infarction. In risk stratification analysis, the predictive value of hsCRP remains quite high, even in females without any family history of hypertension, diabetes, hyperlipidemia, smoking, or CVDs.

## 1.2.2. Framingham score and Reynolds risk score

CVDs are caused by a variety of pathological factors, and several studies have confirmed that increased hsCRP is associated with a higher risk of coronary heart disease. The Framingham heart study proposed the Framingham score, which is currently recommended in Europe and the United States, for which parameters (i.e., hypertension, total cholesterol, age, gender, high-density lipoprotein [HDL], and smoking) are used to calculate the incidence of coronary heart disease in the next 10 years. The Reynolds risk score, on the other hand, is used to measure the correlation between hsCRP and other risk factors (i.e., age, gender, systolic pressure, smoking history, total cholesterol, HDL, and family history) to calculate the risk of heart attack, stroke, or other significant heart diseases.

Groups identified as high risk (i.e., 10-year coronary heart disease event ≧20%) or low risk (i.e., <10%) by using the Framingham score should receive positive prevention or follow-up for 3–5 years. Although no specific advice exists for the other 25–40% of patients in the moderate-risk group (i.e., 10-year coronary heart disease event of 10–20%), 70% of coronary heart disease events have occurred in that group. It is helpful to add the hsCRP value when using the Framingham score to predict the degree of risk of 10-year coronary heart disease; in that way, hsCRP can be used as a predictive tool for coronary heart disease in healthy people.

The Reynolds risk score is the method of adding the hsCRP value and patient’s parents’ history of myocardial infarction before 60 years of age to the Framingham score. In that method, approximately 40–50% of patients at risk of CVDs (i.e., original 5–20%, 10-year risk) determined by the Framingham score were reassigned to the low- or high-risk group [33]. Thus far, however, the Reynolds risk score is not universal.

# ACCEPTED MANUSCRIPT

## 1.2.3. Clinical applications of hsCRP

hsCRP can predict the occurrence and degree of risk of further CVD, and numerous studies have recently confirmed the influence of rising hsCRP on the risk of developing CVDs, including coronary heart disease, stroke, and atherosclerosis. Moreover, hsCRP is critical for the diagnosis of acute coronary syndrome. For patients with stable angina or non-ST-segment elevation myocardial infarction, increased hsCRP indicates the risks of adverse CVDs. If hsCRP continues to increase when the patient is discharged artery syndrome increases dramatically. In short, previous work has suggested that hsCRP is an independent predictor of CVD risk.

## 1.2.4. Risk factors of CVDs

To more accurately predict myocardial infarction, epidemiological studies have explored a series of new risk factors for coronary artery disease, many of which are important for particular patients. Among the factors (Table 1), fibrinogen and hsCRP have received the most attention [34].

Table 1 Potential indexes of risks of vascular infarction.

<table><tr><td rowspan="7">Concentration markers</td><td>Fibrinogen</td></tr><tr><td>tPA</td></tr><tr><td>PAI-1</td></tr><tr><td>Factor V, VII, and VIII</td></tr><tr><td>Lipoprotein(a)</td></tr><tr><td>Homocysteine</td></tr><tr><td>von Willebrand factor antigen</td></tr><tr><td rowspan="7">Process markers</td><td>tPA/PAI-1 complex</td></tr><tr><td>Plasmin--antiplasmin complex</td></tr><tr><td>Prothrombin fragment 1 + 2</td></tr><tr><td>Thrombin-antithrombin III complex</td></tr><tr><td>Fibrinopeptide A</td></tr><tr><td>Fibrin degradation products</td></tr><tr><td>D-dimer</td></tr><tr><td rowspan="3">Functional markers</td><td>Activated protein C resistance</td></tr><tr><td>Factors VIIc and VIIa</td></tr><tr><td>Thrombin</td></tr><tr><td>Global marker</td><td>Clot lysis time</td></tr><tr><td rowspan="4">Inflammatory markers</td><td>High-sensitivity C-reactive protein [35]</td></tr><tr><td>Serum amyloid A</td></tr><tr><td>Interleukins</td></tr><tr><td>Vascular and cellular fibrinogen adhesion molecules</td></tr><tr><td>Platelet markers</td><td>Platelet size and volume</td></tr></table>

However, given the current clinical application of new CVD indexes in healthy people, three important problems identified in the research merit consideration. First, clinical chemists need to reach a consensus regarding the diagnostic test for the indexes of interest. If it is impossible to test the attributes, then discussion is the best way to measure an ongoing index; in terms of clinically useful advice, it is impossible to test high risk. Second, a consistent prospective epidemiological study showing that new indexes of interest can test patients before the onset of clinical disease is necessary. Some prospective studies have indicated that it is crucial to determine the correctness of the relationship between a new risk factor and subsequent myocardial infarction or stroke. Third, evidence is needed to support the evaluation of whether new indexes can increase the accuracy of risk prediction of various CVD risk factors [36]. The determined predictive ability of a given index in univariate analysis is insufficient for a recommendation of clinical application because the observed correlation might be affected by other traditional risk factors. In that sense, it is arguably more important that the new index can at least help to predict the risk factors of coronary heart disease.

Table 2 Evaluation of clinical application of new cardiovascular disease indexes.

<table><tr><td>Indicators</td><td>Are the experimental conditions standardized?</td><td>Are the perspective studies consistent?</td><td>Was the assessment performed with HDL cholesterol?</td></tr><tr><td>Lipoprotein(a)</td><td>No</td><td>Yes/ No</td><td>Yes/ No</td></tr><tr><td>Total homocysteine</td><td>Yes/ No</td><td>Yes/ No</td><td>Yes/ No</td></tr><tr><td>Tissue-type plasminogen activator and plasminogen activator inhibitor</td><td>Yes/ No</td><td>Yes</td><td>Yes/ No</td></tr><tr><td>Fibrinogen</td><td>Yes/ No</td><td>Yes</td><td>Yes</td></tr><tr><td>HsCRP</td><td>Yes</td><td>Yes</td><td>Yes</td></tr></table>

Standards (Table 2) can be used to analyze attributes and the consistency of prospective epidemiological studies as well as to assign an index in order to increase the total predictive value. It is necessary to adopt new risk assessment indexes for patients with personal or family histories of premature arterial thrombosis caused by metabolic abnormalities or unknown reasons. Such indexes can be used to predict myocardial infarction and explore the future risk of the condition. Those data are satisfying because they improve the measurement of new coronary heart disease indexes and can significantly expand our current capacities to predict the risk of a heart attack.

## 1.2.5. Decision support systems and medical decision making

A wide variety of decision support systems have been presented to apply to different fields, such as finance [37, 38], business process [39], online social networks [40], healthcare and clinical applications [41, 42], medical emergency management [43], and etc.. In financial decision making, a study [37] estimates the perceived role for the decision-making of investment counselors in banking decision support system. Both of analytical hierarchy processing and Neumann-Segev are used for data analyses. The results indicate the most important information components in decision support system are customer and investment risk classifications, whereas other important decision-support-system components are the customer goals and nature of investment. Another decision support system regarding finance [38] is also present a new approach to improve financial decision-making via automatic feature weighting. After doing that, it results in an obvious improvement in the performance of financial decision-making on financial data, which are critical to financial decision support systems and be beneficial to the development of financial systems at the same time.

In addition, the decision making in business processes is also an important topic in the applications of decision support systems. Business processes make an enormous number of decisions affecting their business performance. However, these decisions are not usually optimized and formally specified. A approach [39] is developed to enhance the business performance of processes by deriving the criteria of decisions from the experience gained via past process executions. Data mining techniques are used to identify the relationships between path decisions, process outcomes, and context. The decision rules are derives from these relationships. The results show that it has the potential to improve the business performance through the generated rules.

Finally, medical decision making is a relatively larger portion of applications in decision support systems. It includes the applications of health online social networks [40], healthcare [41], evidence-based medicine and clinical areas [42], medical emergency management [43], and etc.. The potential of health online social networks [40] is explored using netnography as a tool for the process of decision-making The results affirm that health online social networks support and empower users during the process of decision-making in three inherit key phases (intelligence, design and choice) and two new phases (emotional support and sharing experiences). It produces important practical implications for the design of online social networks support in blended decision making processes. Several healthcare decision

# ACCEPTED MANUSCRIPT

support systems are developed to help decision maker in each decision level [41]. Part of them are briefly described as follows. Firstly, a novel clustering approach based on principal component analysis is proposed to find groups of elderly persons living in nursing houses automatically that permit decision makers to enhance the social and nursing service planning and organization. Secondly, the problem of districting applied to home health care structures is a decision in strategy that consists of grouping of patients to districts according to relevant criteria. Thirdly, a new approach of modeling the interactions develop a general decision making tool to assist the managers and pharmacists to organize the processes of medication use.

A multi-agent architecture combined with privacy preserving methods [42] is proposed to facilitate data sharing when preserving privacy. The artifact of design is able to overcome the challenges, thereby facilitating data sharing while knowledge discovery in healthcare and supporting clinical decision making and evidence based medicine via improving predictive models. The processes of evaluating and developing a domain ontology for mass gatherings are stated when focusing on medical emergency management [43], and a decision support based on for emergency medical management in mass gatherings is implemented to illustrate the ontology potential for overcoming terminology inconsistencies and the usefulness of supporting communication between medical emergency personnel in mass gatherings.

Moreover, a technology namely “Information fusion-based sensitivity analysis [44, 45]” has been well-established to tackle with the variable importance ranking in machine learning models and can handle the issue of nonlinearity, dependence, and non-normal statistical distribution. Information fusion-based sensitivity analyses on the models of data mining [44], which use a machine learning approach to decide critical factors of success by analyzing the dataset of a focus course and provides several guidelines to educators to improve their teaching effectiveness, produce an unbiased weighting scheme for the order of ranking of the factors that greatly aid to predict students’ comprehension level. It resolves the problems that most business students in the university find the quantitatively oriented courses challenging to comprehend the course material to a degree necessary to develop confidence level and capability to solve business problems. A decision of critical factors influencing performance in these courses is important to designing the instructions of class.

In this study, a novel ranking and attribute selection algorithm is proposed to assist doctors and

# ACCEPTED MANUSCRIPT

researchers for medical decision-making in identifying the significance of CVD risk factors. After combining with the machine learning technologies, the attribute-ranked datasets that identify the ideal number of factors is generated. The results indicate that such knowledge can aid the proper selection of factors of CVD patients and thereby assist doctors in better medical decision-making in diagnostics and treatment, which can greatly reduce treatment costs and thus lower the economic burden of healthcare.

The rest of the paper proceeds as follows. We explain the main concepts concerning our work in framework for feature selection, and in Section 5, we detail our experimental evaluation. Lastly, in Section 6, we present our conclusions and recommendations for future research along similar lines.

## 2. Proposed framework

The flowchart of the proposed framework representing the implementation is illustrated in Fig. 1. After important factors are selected by senior doctors and suggested by the literature from whole CVD risk factors of original medical datasets, the chosen attributes are processed and subjected to feature ranking with the proposed improved mRMR algorithm. In addition, the procedure of attribute ranking is not relative to the used classifiers.

More specifically, the attribute-ranked process seeks to identify the best attribute ranking according to the evaluation criteria, which minimize redundancy and simultaneously maximize correlations. The sorted factors/attributes corresponding to the best rank performed by the improved mRMR algorithm are used across all whole datasets. Lastly, the ranked attributes are discriminated with several classifiers, including bagging, NBTree, BayesNet, RBFNetwork, Kstar, Random Forest, and J48, to discern the ideal numbers and positions of attributes for each classifier.

Attribute ranking is computed by the proposed algorithm from the datasets, and a line of classification accuracy for each classifier on different numbers of ordered attributes is constructed, which allows the evaluation of the performance of the proposed method. In real operation applications, doctors or researchers can submit a dataset to the system, which will return the attribute ranking and the best numbers/positions of attributes, wherein the numbers/positions are associated with a classifier. Such characteristics can be used to support decision making for medical purposes.

![](/api/attachments/FKU98QRH/fulltext/images/912d3fa8e9857a5c598049d630ded4e2f56826794ee8fb5827341cb90756f759.jpg)  
Find out the Best Numbers/Position of Attributes  
Fig. 1. Flowchart of the proposed framework.

## 2.1. Materials

We obtained medical datasets from Mackay Memorial Hospital in Taipei, Taiwan, which consisted of the attributes of patients’ healthy examinations and nearly 70 CRP attributes from original medical datasets derived from more than 7,000 patients. Important characteristic factors/attributes (n = 21) suitable for further analysis were chosen by senior doctors and screened for recommendation in related studies. Per the suggestions of the doctors and literature, the dependent variable hs\_crp was predefined in three classes. The research variables and dependent variable appear in Table 3.

Table 3 Research variables and dependent variable.  
(a) Research variables

<table><tr><td>Attribute names</td><td>Definition</td><td>Data Types</td><td>Data Distribution</td></tr><tr><td>Sex</td><td>0(female) /1(male)</td><td>Categorical (Binary)</td><td></td></tr><tr><td>Age</td><td></td><td>Continuous</td><td>49.0 ± 11.4</td></tr><tr><td>height</td><td>cm</td><td>Continuous</td><td>165.6 ± 8.6</td></tr><tr><td>weight</td><td>kg</td><td>Continuous</td><td>67.1 ± 12.5</td></tr><tr><td>bmi</td><td>0(&lt;19) /1(20-25) /2(26-29) /3(&gt;30)</td><td>Continuous</td><td>24.4 ± 3.5</td></tr><tr><td>sbp</td><td>0(&lt;130) /1(&gt;130)</td><td>Continuous</td><td>122.0 ± 16.8</td></tr><tr><td>dbp</td><td>0(&lt;85) /1(&gt;85)</td><td>Continuous</td><td>75.2 ± 10.7</td></tr><tr><td>pulse_rate</td><td></td><td>Continuous</td><td>74.8 ± 10.4</td></tr><tr><td>temp</td><td>Centigrade</td><td>Continuous</td><td>36.7 ± 0.4</td></tr></table>

## ACCEPTED MANUSCRIPT

<table><tr><td>body_fat</td><td>man &lt;18, 18-25, &gt;25woman &lt;25, 25-31, &gt;31</td><td>Continuous</td><td>26.3 ± 7.0</td></tr><tr><td>waist</td><td>cm</td><td>Continuous</td><td>83.4 ± 9.9</td></tr><tr><td>buttock</td><td>cm</td><td>Continuous</td><td>94.5 ± 6.7</td></tr><tr><td>wbc_count</td><td>0(&lt;3.54) /1(3.54-9.06) /2(&gt;9.06)</td><td>Continuous</td><td>6.1 ± 1.6</td></tr><tr><td>glucose_ac</td><td>0(&lt;70) /1(70-100) /2(&gt;100)</td><td>Continuous</td><td>101.1 ± 24.4</td></tr><tr><td>glucose_pc</td><td>0(&lt;140) /1(&gt;140)</td><td>Continuous</td><td>123.4 ± 51.2</td></tr><tr><td>Hbalc</td><td>0(&lt;3.8) /1(3.8-6.0) /2(&gt;6.0)</td><td>Continuous</td><td>5.8 ± 0.9</td></tr><tr><td>bun</td><td>0(&lt;7) /1(7-20) /2(&gt;20)</td><td>Continuous</td><td>12.1 ± 4.1</td></tr><tr><td>uric_acid</td><td>0(&lt;2.5) /1(2.5-8.0) /2(&gt;8.0)</td><td>Continuous</td><td>5.9 ± 1.5</td></tr><tr><td>creatinine</td><td>0(&lt;0.6) /1(0.6-1.5) /2(&gt;1.5)</td><td>Continuous</td><td>0.9 ± 0.3</td></tr><tr><td>total_cholesterol</td><td>0(&lt;200) /1(&gt;200)</td><td>Continuous</td><td>199.8 ± 36.2</td></tr><tr><td>triglyceride</td><td>0(&lt;20) /1(20-200) /2(&gt;200)</td><td>Continuous</td><td>135.2 ± 100.7</td></tr><tr><td>ldl</td><td>0(&lt;65) /1(65-120) /2(&gt;120)</td><td>Continuous</td><td>128.5 ± 32.4</td></tr><tr><td>hdl</td><td>0(&lt;35) /1(&gt;35)</td><td>Continuous</td><td>53.0 ± 14.6</td></tr><tr><td>sgpt</td><td>0(&lt;6.0) /1(6-45) /2(&gt;45)</td><td>Continuous</td><td>30.1 ± 24.7</td></tr><tr><td>tsh</td><td>0(&lt;0.4) /1(0.4-4.0) /2(&gt;4.0)</td><td>Continuous</td><td>2.3 ± 2.2</td></tr><tr><td>free_t4</td><td>0(&lt;0.89) /1(0.89-1.79) /2(&gt;1.79)</td><td>Continuous</td><td>1.3 ± 0.2</td></tr><tr><td>t3</td><td>0(&lt;78) /1(78.0-182.0) /2(&gt;182.0)</td><td>Continuous</td><td>114.2 ± 25.5</td></tr><tr><td>insulin</td><td>0(&lt;5) /1(5-20) /2(&gt;20)</td><td>Continuous</td><td>7.2 ± 6.1</td></tr><tr><td>homa_ir</td><td>0(&lt;1) /1(&gt;1)</td><td>Continuous</td><td>1.9 ± 1.8</td></tr><tr><td>homocysteine</td><td>0(&lt;4) /1(4-17) /2(&gt;17)</td><td>Continuous</td><td>8.7 ± 3.5</td></tr><tr><td>egfr</td><td>0(&lt;60) /1(60-90) /2(90-120) /3(&gt;120)</td><td>Continuous</td><td>88.4 ± 17.3</td></tr></table>

(b) Dependent variable

<table><tr><td>hs_crp</td><td>0(&lt;0.1) /1(0.1-0.3) /2(&gt;0.3)</td><td>Continuous</td><td>0.2 ± 0.4</td></tr></table>

## 2.2. Data preprocessing

After we normalized the attributes of the datasets (Table 3), we ranked and then selected the significant subfeatures by using the proposed improved mRMR algorithm for subsequent analysis and the discrimination of various classifiers. The improved mRMR algorithm minimized redundancy and maximized correlations in order to obtain an arrangement of attributes and identify important ones.

## 2.3. Attribute ranking

## 2.3.1. Feature selection

Feature selection is an important step for data mining [17] that is typically used to remove irrelevant and redundant attributes and reduce the quantity of attributes in order to improve the accuracy of classification and similarity searches and reduce computation costs [15, 16, 18]. Under the standards of optimization, feature selection screens out attributes from the original attribute set D that benefit classification in order to generate an attribute subset d, which is used for machine learning, pattern recognition, and adaptive control, among other tasks.

Feature selection can be divided into two primary types: filter- and wrapper-based selections [19]. On the one hand, filter-based feature selection selects attributes regardless of the model statistics. It works based only on several characteristics, such as the correlation between the attributes, to select. In addition, filter-based feature selection suppresses the attributes that are the least interesting. That is, the other attributes would be a portion of the model used to further classify. Filter-based feature selection is effective in computation cost. However, it usually selects redundant variables because of not considering the relationships between attributes.

On the other hand, wrapper-based feature selection aims to calculate the attribute subset with an optimization algorithm. Common wrapper-based feature selection methods involve genetic algorithms and particle swarm optimization, among other techniques. Wrapper-based methods are more suitable for data mining than filter-based ones given the attributes that they select, but they often entail a higher computational cost.

Altogether, feature selection is often used in machine learning, in which it, along with a learning algorithm, not only selects effective attributes with differential ability from the origin attribute set according to specific performance evaluation indicators, but also determines the optimal attribute subset, all toward optimizing performance indicators.

## 2.3.2. Mutual information

Mutual information (MI) is a measure of information [20, 21] that is often used in research [e.g., 22, 23]. Since interdependence occurs between variables or sets, variables are often symmetric and non-negative. MI with a value of 0 represents independent variables, whereas MI with non-zero values represents dependent variables. Two discrete random variables, $X = ( x _ { 1 } , x _ { 2 } , . . . , x _ { k } )$ and $Y = ( y _ { 1 } , y _ { 2 } , . . . , y _ { k } )$ are defined as:

$$
I (X; Y) = \sum_ {y \in Y} \sum_ {x \in X} p (x, y) \log \frac {p (x , y)}{p (x) p (y)}\tag{1}
$$

$( x _ { 1 } , x _ { 2 } , . . . , x _ { k } )$ and $( y _ { 1 } , y _ { 2 } , . . . , y _ { k } )$ are values of the discrete variables X and $Y , p ( x , y )$ is a joint density function, and p(x) and $p ( y )$ form the marginal density function. MI can also be expressed as:

$$
\begin{array}{r l} I (X; Y) & = \sum_ {x \in X} p (x) \sum_ {y \in Y} p (y / x) \log \frac {p (y / x)}{p (y)} \\ & = \sum_ {x \in X} p (x) \sum_ {y \in Y} p (y / x) \log p (y / x) - \sum_ {y \in Y} p (y) \log p (y) \end{array}\tag{2}
$$

We used MI to extract attributes from the algorithm.

## 2.3.3. mRMR algorithm

The mRMR algorithm is a filter-based feature selection algorithm used to estimate the maximum correlation [24–26], which can, in turn, detect the specific approximate value of MI between joint distribution and classification variables [27, 28]. In the algorithm, maximum correlation and minimum redundancy are defined as

$$
\min _ {E \subset S} \frac {1}{| E | ^ {2}} \sum_ {i, j \in E} I (f _ {i}, f _ {j})\tag{3}
$$

in which $/ E /$ is the number of features in the subset, I(f<sub>i</sub>, f<sub>j</sub>) is the MI between $f _ { i }$ and $f _ { j } \left( \mathrm { i } . \mathrm { e } . \right.$ , the two feature sets), and S is the space for all feature sets.

$$
\min _ {E \subset S} \frac {1}{| E | ^ {2}} \sum_ {i \in E} I (C, f _ {j})\tag{4}
$$

$I ( C , f _ { i } )$ quantifies attribute set $f _ { i }$ and the set of target category $c = \{ c _ { I } , c _ { 2 } , . . . . , c _ { k } \}$ . In greater detail, the algorithm involves four steps:

1. Initialization establishes the initial sets of $\mathbf { F } {  } n$ features, wherein $\mathbf { F } = \{ f _ { I } , f _ { 2 } , \ldots , f _ { n } \}$ . The intended set $\scriptstyle \mathbf { S }  \{ \} $ is initialized.

2. I $( \mathbf { C } , f _ { i } )$ is calculated according to Eq. (2), output class $\mathbf { C } ,$ and input feature set $\forall f _ { i } \in \mathbf { F }$

3. The selection of the first feature finds the largest value of $\mathrm { I } \left( \mathrm { C } , f _ { i } \right)$ in the entire feature collection and set $\mathbf { F } \gets \mathbf { F } \setminus \{ \{ f _ { i } \} , \mathbf { S } \gets \{ f _ { i } \}$ , in which $\mathbf { F } \setminus \{ f _ { i } \}$ seeks to remove feature $f _ { i }$ from F collection.

4. Greedy selection is repeated until the predefined number of features is selected.

a) For the calculation of the MI value between features, $\operatorname { I } ( f _ { i } , f _ { s } )$ is calculated for all feature pairs $( f _ { i } , f _ { s } )$ in which $f _ { i } \in \mathbf { F }$ and $f _ { s } \in \mathbf { S }$

b) The selection of the next feature involves selecting feature $f _ { i } \in \mathbf { F }$ to make $\mathbf { G } = \operatorname { I } ( \mathbf { C } ; f _ { i } ) - ( \frac { 1 } { \left| S \right| } ) \boldsymbol { \Sigma } _ { \mathrm { f s } \in \mathrm { S } }$ $\operatorname { I } ( f _ { i } ; f _ { s } )$ in the situation that G is the maximum. Set $\mathbf { F }  \mathbf { F } \backslash \{ f _ { i } \}$ and $\mathbf { S } \gets \mathbf { S } \cup \{ f _ { i } \}$

In mRMR feature selection methods, since each pair involves only two variables, using paired joint probability assures greater robustness. In some cases, the algorithm might underestimate the usefulness of attributes because it does not detect the interaction between attributes in order to increase the correlation, regardless of method. Nevertheless, the overall algorithm is more efficient and will produce an attribute set with very little redundancy.

## 2.3.4. Attribute ranking with the improved mRMR algorithm

Our improved mRMR algorithm is a modification of the mRMR algorithm. Similar to the mRMR algorithm, the improved version is a filter-based selection method that uses a measure to score the feature subset, which is independent of specific classifiers, and the average normalized MI is computed quickly to capture the useful feature set. However, the improved mRMR algorithm is less computationally intensive and produces a feature set that is not tuned to a specific type of classifier. Since the feature set does not contain any assumptions of a specific classifier, it is more useful for exploring the relationships among features. The improved mRMR algorithm replaces substep b of step 4 described in Section 2.3 with:

b) Selection of the next feature $f _ { i } \in \mathbf { F }$ to yield

$$
\mathbf {G} = I (\mathbf {C}; f _ {i}) - \left(\frac {1}{| S |}\right) \Sigma_ {\mathrm{fs} \in \mathrm{S}} I \left(f _ {i}; f _ {s}\right) \left(H \left(f _ {i}\right) + H \left(f _ {s}\right)\right) / \left(2 H \left(f _ {i}\right) H \left(f _ {s}\right)\right)\tag{5}
$$

when $G$ is the maximum. Set $\mathbf { F }  \mathbf { F } \backslash \{ f _ { i } \}$ , and Set $\mathbf { S } \gets \mathbf { S } \cup \{ f _ { i } \}$

The proposed algorithm normalizes MI-based feature selection by means of mixed-entropy $\left( H ( f _ { i } ) + H ( f _ { s } ) \right) / \left( 2 H ( f _ { i } ) H ( f _ { s } ) \right)$ from features f and $f _ { s } .$ As a modification of the mRMR algorithm, it evaluates the correlation with the MI between pairs of features. Compared to the conventional mRMR algorithm, the improved version reduces the bias of MI toward multivalued attributes and restricts the value of MI to a specific interval. Moreover, it has an adaptive redundancy penalization term that does not require any parameters to be adjusted in the algorithm. More specifically, the MI between $f _ { i }$ and $f _ { s }$ is normalized by the harmonic mean of the entropies of both features:

$$
N I \left(f _ {i}; f _ {s}\right) = \frac {I \left(f _ {i} ; f _ {s}\right)}{\frac {2}{\frac {1}{H \left(f _ {i}\right)} + \frac {1}{H \left(f _ {s}\right)}}} = \frac {I \left(f _ {i} ; f _ {s}\right) \left(H \left(f _ {i}\right) + H \left(f _ {s}\right)\right)}{2 H \left(f _ {i}\right) H \left(f _ {s}\right)}\tag{6}
$$

We used the average normalized MI to measure the redundancy between feature $f _ { i }$ and subset ${ \bf S } =$ $\{ f _ { s } \}$ of selected features,

$$
(\frac {1}{| S |}) \Sigma_ {\mathrm{fs} \in \mathrm{S}} N I (f _ {i}; f _ {s})\tag{7}
$$

in which $| S |$ stands for the cardinality of set S. Eq. (7) represents the measure of correlation; when the value is low, feature $f _ { i }$ and subset S are more independent, whereas when the value is large, $f _ { i }$ is highly correlated with S. Feature selection and rank criteria are determined by selecting the feature that maximizes measure G in Eq. (5).

## 2.4. Classification methods

Along with physicians’ judgments, several classification methods serve as the basis for evaluation.

## 2.4.1. Support vector machine

Initially proposed by Vapnik et al. [29], the support vector machine (SVM) algorithm is a method of supervised learning that is widely used in statistical classification and regression. For classification problems across spatial vectors, SVM maps exercise data in high-dimensional spaces in order to detect the decision boundary for the classification problem with a hyperplane and, in turn, to divide data with the best partition mode. By contrast, for the nonlinear classification problem, the SVM algorithm calculates a soft margin to separate the hyperplane, thereby allowing exercise errors and the transfer of data to high-dimensional space for division.

## 2.4.2. Bayesian network

Bayesian networks, also called Bayesian belief networks, are directed cyclic graphs based on conditional probability. In general, Bayesian networks work with continuous data by discretizing them with cluster analysis before performing the Bayesian network algorithm [30]. Bayesian networks are widely used in medical diagnostics, credit card fraud detection, marketing strategies, financial forecasting, and expert system designs.

## 2.4.3. Radial basis function

The radial basis function (RBF) neural network, also known as the radius-type neural network [31], is a learning algorithm that is chiefly characterized by the stimulation of the local adjustment function of the brain cortex axon and good mapping ability. The RBF belongs to the basic feedforward neural network, which consists of an input layer, a single hidden layer, and an output layer. The chief goals of

RBF are to construct several amplitude-based functions and identify the mapping relationship of the input and output with curve fitting. Pattern classification problems in high-dimensional space more often conform to the linear separation trend than those problems do in low-dimensional space. Accordingly, RBFs often have high-dimensional hidden space, meaning that more neurons are in the hidden layer; however, the number of neurons in the hidden layer directly affects the input and output mapping relationship in network construction, and higher-dimensional hidden space can generate more accurate approximate estimates.

## 2.4.4. Bagging

Bagging is an integration approach that trains multiple decision trees via sampling with replacement and obtains its final results by voting. In bagging, several training datasets with the same quantity of data points are first selected randomly from the training dataset. Data sampling is then replaced and deleted in order to avoid having the same data in multiple datasets. Second, for each training dataset, a data mining algorithm is used to establish a classification model to generate N classification models for N training datasets. Lastly, to classify unknown data, the data should be sent to every established classifier for classification. The categories of those data are decided by classifier voting, in which the category with the most votes is the final classification result [32].

## 2.4.5. Classification methods of evaluating the improved mRMR algorithm

We obtained results with various classifiers according to the order of the attributes that were sorted and selected with the improved mRMR algorithm. The classifiers included bagging, NBTree, BayesNet, RBFNetwork, Kstar, Random Forest, and J48, among others. We ranked the attributes in a sequence of descending importance according to the proposed algorithm. We then discriminated the ranked factors (i.e., attributes) with each classifier to identify the best numbers and positions of attributes for each.

## 2.5. Classification accuracy of ranked attributes using the improved mRMR algorithm

After sorting the attributes with the improved mRMR algorithm, we obtained the order of the importance of attributes, which we relayed to doctors for their professional judgments of reasonableness. We discussed any situation that was deemed unreasonable with the doctors to determine whether we should remove the factor (i.e., attribute), after which we performed an additional round of sorting. Once doctors approved the factor, the classification rates of datasets with attribute ranking are listed in Table 4.

After obtaining the rank order of the attributes’ importance with the improved mRMR algorithm at one shot, we added the attributes, concatenated them (beginning with the highest-ranked attribute), and classified them to obtain their accuracy (Table 4). The order of attributes from first to last ranges from left to right. The attribute bmi represents the attribute used for classification only, body\_fat represents both bmi plus body\_fat used for classification after adding the attribute body\_fat, and etc..

Table 4 An example of classification accuracy with the attribute ranking.

<table><tr><td colspan="12">Data set (All Attributes)</td></tr><tr><td>Attributes</td><td>bmi</td><td>body_fat</td><td>waist</td><td>buttock</td><td>dbp</td><td>sbp</td><td>t3</td><td>insulin</td><td>hdl</td><td>...</td><td>egfr</td></tr><tr><td>Classification Accuracy (%)</td><td>86.3</td><td>92.5</td><td>93.5</td><td>94.2</td><td>95.9</td><td>95.9</td><td>95.9</td><td>94.2</td><td>94.2</td><td>...</td><td>90.9</td></tr></table>

We also proposed a procedure to generate a ranked order of features and incorporated the features one-by-one by considering three combinations in order to construct a feature subset to suit the greedy search. As an example, all features up to and including the attribute dbp produced the best classification performance for a particular classifier (Table 4b); when their classification performance was identical (i.e., “all features up to and including dbp” and “all features up to and including sbp”), three combinations were considered. The first involved adding sbp after dbp (i.e., the original case), the second involved replacing dbp with sbp, and the third considered only dbp without sbp. From the three combinations, the proposed framework selected the combination that possessed the best classification performance. The results indicated that the best classification accuracy (95.9%) of the original nine attributes could be achieved by using only the first five attributes of the datasets with the improved mRMR algorithm; in other words, in the example provided, the final four attributes were redundant.

## 2.6. Performance measures

We used eight performance measures for the three-class classification models, including the true positive (TP) rate, false positive (FP) rate, precision, recall, F-measure, Matthews correlation coefficient (MCC), area under the ROC curve (AUC), and precision-recall curve (PRC) area. The TP rate, or the hit rate, determines the classification performance of a system or method as the ratio of TP to all positives, whereas the FP rate, or the false alarm rate, determines the classification performance as the ratio of FP to all negatives. Precision, or the positive predictive value, measures the proportion of true positives to the

# ACCEPTED MANUSCRIPT

sum of true positives and false positives, whereas recall assesses the proportion of true positives to the sum of true positives and false negatives. F-measure combines precision and recall by calculating their harmonic mean. MCC has a range of -1 to 1, in which -1 and 1 represent completely wrong and completely correct classifications, respectively. MCC can gauge how well the classification model or system performs. In contrast, the AUC evaluates the area under the ROC curve created by plotting the TP rate against the FP rate at various thresholds, whereas the PRC area computes the area under the represent the measures in mathematical formulas:

$$
T P \text { rate } = \frac {T P}{T P + F N}\tag{8}
$$

$$
F P \text { rate } = \frac {F P}{F P + T N}\tag{9}
$$

$$
P r e c i s i o n = \frac {T P}{T P + F P}\tag{10}
$$

$$
R e c a l l = \frac {T P}{T P + F N}\tag{11}
$$

$$
F - M e a s u r e = 2 \frac {\text { Precision } \cdot \text { Recall }}{\text { Precision } + \text { Recall }}\tag{12}
$$

$$
M C C = \frac {T P \cdot T N - F P \cdot F N}{\sqrt {(T P + F P) (T P + F N) (T N + F P) (T N + F N)}}\tag{13}
$$

In addition, the metrics, which measure the performance that is deduced from the confusion matrix, are rectified according to 3-class classification problems [46]. The modified metrics demonstrate the measures, including Accuracy (the accuracy of the model), Precision $C l a s s I - 3$ (the precision for class 1-3), $\mathrm { S e n s i t i v i t y } _ { C l a s s I - 3 }$ (the sensitivity for class 1-3), and Specificity $C l a s s I - 3$ (the specificity for class 1-3). We applied our proposed method to conduct analyses and used the total 12 performance measures to rank the system based on its performance. As such, the 12 performance measures can be used to report the system’s overall performance.

## 2.7. Statistical evaluation

We performed statistical evaluation with two-way analysis of variance (ANOVA) to estimate whether the difference of performance was significant for the two factors, classifiers, attribute ranking, and selection method. The confidence interval of the test was 0.99.

# ACCEPTED MANUSCRIPT

## 3. Results and discussion

We used 6,848 patient cases from the dataset in experiments after data cleaning and preprocessing. Because the original dataset contained too many factors (i.e., attributes), prior to analysis we selected potentially influential factors that were suitable for analysis per the recommendations of senior doctors at Mackay Memorial Hospital and the research of Ridker [34], Mayo Clinic (i.e., a nonprofit medical research unit) and Boudi [47] in order to avoid the interference of irrelevant factors and noise. Ultimately, 21 factors/attributes were included: height, weight, bmi, sbp, waist, wbc\_count, glucose\_ac, creatinine, triglyceride, ldl, hdl, smoking, exercise, stroke\_hx, age, sex, htn\_med\_hx, dm\_med\_hx, lipid\_med\_hx, cvd\_med\_hx, and egfr. Next, we used seven classifiers (i.e., bagging, NBTree, BayesNet, RBFNetwork, Kstar, Random Forest, and J48) for the classification of attributes to obtain correct rates; in this step we did not perform our attribute-ranking method. Table 5(a) presents the classification results (including the correct rate, AUC, TP rate, FP rate, precision, recall, F-Measure, and MCC) of the 21 factors/attributes for each classifier. With the seven classifiers, the 21 factors/attributes yielded an average correct rate of 49.50%, average AUC of 0.586, and etc.. In addition, an experiment that randomly sorts the attributes and is then applied to the classification step is performed. More specifically, we perform randomly sorting the attributes and applying to the classification step 10 times, and then calculate its average and standard deviation, as listed in Table 5(b).

Table 5  
(a) Classification results of 21 factors/attributes for each classifier

<table><tr><td>Classifier</td><td>Correct Rate</td><td>AUC</td><td>TP Rate</td><td>FP Rate</td><td>Precision</td><td>Recall</td><td>F-Measure</td><td>MCC</td></tr><tr><td>Bagging</td><td>49.70%</td><td>0.580</td><td>0.497</td><td>0.623</td><td>0.422</td><td>0.497</td><td>0.416</td><td>0.053</td></tr><tr><td>NBTree</td><td>50.33%</td><td>0.623</td><td>0.503</td><td>0.548</td><td>0.466</td><td>0.503</td><td>0.469</td><td>0.099</td></tr><tr><td>BayesNet</td><td>50.52%</td><td>0.623</td><td>0.505</td><td>0.544</td><td>0.469</td><td>0.505</td><td>0.473</td><td>0.103</td></tr><tr><td>RBFNetwork</td><td>51.79%</td><td>0.620</td><td>0.518</td><td>0.562</td><td>0.483</td><td>0.518</td><td>0.477</td><td>0.108</td></tr><tr><td>Kstar</td><td>48.19%</td><td>0.559</td><td>0.482</td><td>0.663</td><td>0.341</td><td>0.482</td><td>0.370</td><td>0.045</td></tr><tr><td>Random Forest</td><td>46.29%</td><td>0.553</td><td>0.463</td><td>0.618</td><td>0.395</td><td>0.463</td><td>0.387</td><td>0.058</td></tr><tr><td>J48</td><td>49.70%</td><td>0.542</td><td>0.497</td><td>0.586</td><td>0.444</td><td>0.497</td><td>0.441</td><td>0.076</td></tr><tr><td>Average</td><td>49.50%</td><td>0.586</td><td>0.495</td><td>0.592</td><td>0.431</td><td>0.495</td><td>0.433</td><td>0.077</td></tr></table>

(b) Classification results of 21 factors/attributes in random ranking for each classifier

<table><tr><td>Classifier</td><td>Correct Rate(Avarge ± Standard deviation)</td></tr><tr><td>Bagging</td><td>49.93% ± 0.002188</td></tr><tr><td>NBTree</td><td>50.44% ± 0.001367</td></tr><tr><td>BayesNet</td><td>50.29% ± 0.001439</td></tr><tr><td>RBFNetwork</td><td>51.57% ± 0.002044</td></tr><tr><td>Kstar</td><td>48.38% ± 0.001826</td></tr><tr><td>Random Forest</td><td>45.88% ± 0.002579</td></tr><tr><td>J48</td><td>49.59% ± 0.001087</td></tr><tr><td>Average</td><td>49.44%</td></tr></table>

Next, we sorted the order of factors/attributes with the improved mRMR algorithm, which yielded an attribute ranking, from first to last, of age, exercise, weight, height, waist, egfr, ldl, bmi, glucose\_ac, sbp, sex, smoking, htn\_med\_hx, triglyceride, wbc\_count, hdl, cvd\_med\_hx, lipid\_med\_hx, dm\_med\_hx, creatinine, and stroke\_hx. Lastly, we discriminated the ranked attributes with the same seven classifiers to determine the best numbers and positions of the attributes for each classifier, as described in Section 4.5. To do that, we selected the first factor/attributes for classification first, after which we chose the first two factors/attributes for classification, and thus classified all 21 factors/attributes.

All the experimental results for the seven classifiers appear in Tables 6-12, respectively. We divided the results for the seven classifiers into three groups for subsequent discussion. The first group contained the classifiers NBTree, J48, and BayesNet. The results with those three classifiers indicate that the largest weight, height, waist, egfr, ldl, bmi, and glucose\_ac) were used for classification. Detailed results, including a confusion matrix, eight performance measures and four modified performance measures, of the classification of those nine factors for the three classifiers are shown in Tables 6-8, respectively.

Table 6 Detailed classification results of the first 9 factors/attributes for NBTree.

<table><tr><td rowspan="3">Class</td><td colspan="11">NBTree</td></tr><tr><td colspan="3">Confusion Matrix</td><td rowspan="2">TP Rate</td><td rowspan="2">FP Rate</td><td rowspan="2">Precision</td><td rowspan="2">Recall</td><td rowspan="2">F-Measure</td><td rowspan="2">MCC</td><td rowspan="2">AUC</td><td rowspan="2">PRC Area</td></tr><tr><td>0</td><td>1</td><td>2</td></tr><tr><td>0</td><td>931</td><td>154</td><td>44</td><td>0.825</td><td>0.571</td><td>0.638</td><td>0.825</td><td>0.719</td><td>0.278</td><td>0.680</td><td>0.704</td></tr><tr><td>1</td><td>363</td><td>176</td><td>59</td><td>0.294</td><td>0.168</td><td>0.419</td><td>0.294</td><td>0.346</td><td>0.143</td><td>0.606</td><td>0.363</td></tr><tr><td>2</td><td>165</td><td>90</td><td>72</td><td>0.220</td><td>0.060</td><td>0.411</td><td>0.220</td><td>0.287</td><td>0.210</td><td>0.681</td><td>0.310</td></tr><tr><td>Weighted Average</td><td></td><td></td><td></td><td>0.574</td><td>0.372</td><td>0.538</td><td>0.574</td><td>0.542</td><td>0.228</td><td>0.658</td><td>0.542</td></tr></table>

(a)

<table><tr><td rowspan="3">Class</td><td colspan="7">NBTree</td></tr><tr><td colspan="3">Confusion Matrix</td><td rowspan="2">Accuracy</td><td rowspan="2">Sensitivity $_{Class}$ </td><td rowspan="2">Specificity $_{Class}$ </td><td rowspan="2">Precision $_{Class}$ </td></tr><tr><td>0</td><td>1</td><td>2</td></tr><tr><td>0</td><td>931</td><td>154</td><td>44</td><td></td><td>0.638</td><td>0.825</td><td>0.429</td></tr><tr><td>1</td><td>363</td><td>176</td><td>59</td><td>0.574</td><td>0.419</td><td>0.294</td><td>0.832</td></tr><tr><td>2</td><td>165</td><td>90</td><td>72</td><td></td><td>0.411</td><td>0.220</td><td>0.940</td></tr></table>

(b)  
Table 7 Detailed classification results of the first 9 factors/attributes for J48.

<table><tr><td rowspan="3">Class</td><td colspan="11">J48</td></tr><tr><td colspan="3">Confusion Matrix</td><td rowspan="2">TP Rate</td><td rowspan="2">FP Rate</td><td rowspan="2">Precision</td><td rowspan="2">Recall</td><td rowspan="2">F-Measure</td><td rowspan="2">MCC</td><td rowspan="2">AUC</td><td rowspan="2">PRC Area</td></tr><tr><td>0</td><td>1</td><td>2</td></tr><tr><td>0</td><td>988</td><td>105</td><td>36</td><td>0.875</td><td>0.678</td><td>0.612</td><td>0.875</td><td>0.720</td><td>0.239</td><td>0.629</td><td>0.634</td></tr><tr><td>1</td><td>432</td><td>121</td><td>45</td><td>0.202</td><td>0.129</td><td>0.392</td><td>0.202</td><td>0.267</td><td>0.093</td><td>0.542</td><td>0.327</td></tr><tr><td>2</td><td>195</td><td>83</td><td>49</td><td>0.150</td><td>0.047</td><td>0.377</td><td>0.150</td><td>0.214</td><td>0.155</td><td>0.604</td><td>0.237</td></tr><tr><td>Weighted Average</td><td></td><td></td><td></td><td>0.564</td><td>0.418</td><td>0.510</td><td>0.564</td><td>0.508</td><td>0.183</td><td>0.600</td><td>0.481</td></tr></table>

(a)

<table><tr><td rowspan="3">Class</td><td colspan="7">J48</td></tr><tr><td colspan="3">Confusion Matrix</td><td rowspan="2">Accuracy</td><td rowspan="2">SensitivityClass</td><td rowspan="2">SpecificityClass</td><td rowspan="2">PrecisionClass</td></tr><tr><td>0</td><td>1</td><td>2</td></tr><tr><td>0</td><td>988</td><td>105</td><td>36</td><td></td><td>0.612</td><td>0.875</td><td>0.322</td></tr><tr><td>1</td><td>432</td><td>121</td><td>45</td><td>0.564</td><td>0.392</td><td>0.202</td><td>0.871</td></tr><tr><td>2</td><td>195</td><td>83</td><td>49</td><td></td><td>0.377</td><td>0.150</td><td>0.953</td></tr></table>

Table 8 Detailed classification results of the first 9 factors/attributes for BayesNet.

<table><tr><td rowspan="3">Class</td><td colspan="11">BayesNet</td></tr><tr><td colspan="3">Confusion Matrix</td><td rowspan="2">TP Rate</td><td rowspan="2">FP Rate</td><td rowspan="2">Precision</td><td rowspan="2">Recall</td><td rowspan="2">F-Measure</td><td rowspan="2">MCC</td><td rowspan="2">AUC</td><td rowspan="2">PRC Area</td></tr><tr><td>0</td><td>1</td><td>2</td></tr><tr><td>0</td><td>931</td><td>154</td><td>44</td><td>0.825</td><td>0.572</td><td>0.638</td><td>0.825</td><td>0.719</td><td>0.277</td><td>0.680</td><td>0.703</td></tr><tr><td>1</td><td>363</td><td>176</td><td>59</td><td>0.294</td><td>0.167</td><td>0.420</td><td>0.294</td><td>0.346</td><td>0.144</td><td>0.606</td><td>0.363</td></tr><tr><td>2</td><td>166</td><td>89</td><td>72</td><td>0.220</td><td>0.060</td><td>0.411</td><td>0.220</td><td>0.287</td><td>0.210</td><td>0.680</td><td>0.310</td></tr><tr><td>Weighted Average</td><td></td><td></td><td></td><td>0.574</td><td>0.372</td><td>0.538</td><td>0.574</td><td>0.542</td><td>0.228</td><td>0.658</td><td>0.542</td></tr></table>

(a)

<table><tr><td rowspan="3">Class</td><td colspan="7">BayesNet</td></tr><tr><td colspan="3">Confusion Matrix</td><td rowspan="2">Accuracy</td><td rowspan="2">SensitivityClass</td><td rowspan="2">SpecificityClass</td><td rowspan="2">PrecisionClass</td></tr><tr><td>0</td><td>1</td><td>2</td></tr><tr><td>0</td><td>931</td><td>154</td><td>44</td><td></td><td>0.638</td><td>0.825</td><td>0.428</td></tr><tr><td>1</td><td>363</td><td>176</td><td>59</td><td>0.574</td><td>0.420</td><td>0.294</td><td>0.833</td></tr><tr><td>2</td><td>166</td><td>89</td><td>72</td><td></td><td>0.411</td><td>0.220</td><td>0.940</td></tr></table>

(b)

The second group included three classifiers: Kstar, bagging, and Random Forest. The results with those three classifiers indicate the highest classification accuracy occurs only when the first three or four factors (i.e., age, exercise, weight, and height) are used for classification. Therefore, those three or four attributes are speculated to be important factors for the evaluation and prediction of CVDs. Tables 9-11 list the detailed results, including a confusion matrix, eight performance measures and four modified performance measures, of the classification with those three or four factors for the three classifiers, respectively.

Table 9 Detailed classification results of the first 4 factors/attributes for Kstar.

<table><tr><td rowspan="3">Class</td><td colspan="11">Kstar</td></tr><tr><td colspan="3">Confusion Matrix</td><td rowspan="2">TP Rate</td><td rowspan="2">FP Rate</td><td rowspan="2">Precision</td><td rowspan="2">Recall</td><td rowspan="2">F-Measure</td><td rowspan="2">MCC</td><td rowspan="2">AUC</td><td rowspan="2">PRC Area</td></tr><tr><td>0</td><td>1</td><td>2</td></tr><tr><td>0</td><td>1084</td><td>45</td><td>0</td><td>0.960</td><td>0.862</td><td>0.576</td><td>0.960</td><td>0.720</td><td>0.176</td><td>0.649</td><td>0.682</td></tr><tr><td>1</td><td>523</td><td>74</td><td>1</td><td>0.124</td><td>0.067</td><td>0.430</td><td>0.124</td><td>0.192</td><td>0.093</td><td>0.578</td><td>0.346</td></tr><tr><td>2</td><td>274</td><td>53</td><td>0</td><td>0.000</td><td>0.001</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.010</td><td>0.636</td><td>0.240</td></tr><tr><td>Weighted Average</td><td></td><td></td><td></td><td>0.564</td><td>0.493</td><td>0.442</td><td>0.564</td><td>0.452</td><td>0.122</td><td>0.627</td><td>0.513</td></tr></table>

(a)

<table><tr><td rowspan="3">Class</td><td colspan="7">Kstar</td></tr><tr><td colspan="3">Confusion Matrix</td><td rowspan="2">Accuracy</td><td rowspan="2">SensitivityClass</td><td rowspan="2">SpecificityClass</td><td rowspan="2">PrecisionClass</td></tr><tr><td>0</td><td>1</td><td>2</td></tr><tr><td>0</td><td>1084</td><td>45</td><td>0</td><td></td><td>0.576</td><td>0.960</td><td>0.138</td></tr><tr><td>1</td><td>523</td><td>74</td><td>1</td><td>0.564</td><td>0.430</td><td>0.124</td><td>0.933</td></tr><tr><td>2</td><td>274</td><td>53</td><td>0</td><td></td><td>0.000</td><td>0.000</td><td>0.999</td></tr></table>

(b)

Table 10 Detailed classification results of the first 4 factors/attributes for Bagging.

<table><tr><td rowspan="3">Class</td><td colspan="11">Bagging</td></tr><tr><td colspan="3">Confusion Matrix</td><td rowspan="2">TP Rate</td><td rowspan="2">FP Rate</td><td rowspan="2">Precision</td><td rowspan="2">Recall</td><td rowspan="2">F-Measure</td><td rowspan="2">MCC</td><td rowspan="2">AUC</td><td rowspan="2">PRC Area</td></tr><tr><td>0</td><td>1</td><td>2</td></tr><tr><td>0</td><td>1003</td><td>117</td><td>9</td><td>0.888</td><td>0.736</td><td>0.596</td><td>0.888</td><td>0.713</td><td>0.197</td><td>0.647</td><td>0.673</td></tr><tr><td>1</td><td>464</td><td>120</td><td>14</td><td>0.201</td><td>0.147</td><td>0.359</td><td>0.201</td><td>0.258</td><td>0.066</td><td>0.571</td><td>0.333</td></tr><tr><td>2</td><td>217</td><td>97</td><td>13</td><td>0.040</td><td>0.013</td><td>0.361</td><td>0.040</td><td>0.072</td><td>0.074</td><td>0.630</td><td>0.256</td></tr><tr><td>Weighted Average</td><td></td><td></td><td></td><td>0.563</td><td>0.450</td><td>0.489</td><td>0.553</td><td>0.478</td><td>0.139</td><td>0.622</td><td>0.508</td></tr></table>

(a)

<table><tr><td rowspan="3">Class</td><td colspan="7">Bagging</td></tr><tr><td colspan="3">Confusion Matrix</td><td rowspan="2">Accuracy</td><td rowspan="2">SensitivityClass</td><td rowspan="2">SpecificityClass</td><td rowspan="2">PrecisionClass</td></tr><tr><td>0</td><td>1</td><td>2</td></tr><tr><td>0</td><td>1003</td><td>117</td><td>9</td><td>0.563</td><td>0.596</td><td>0.888</td><td>0.264</td></tr></table>

<table><tr><td>1</td><td>464</td><td>120</td><td>14</td><td>0.359</td><td>0.201</td><td>0.853</td></tr><tr><td>2</td><td>217</td><td>97</td><td>13</td><td>0.361</td><td>0.040</td><td>0.987</td></tr></table>

(b)

Table 11 Detailed classification results of the first 3 factors/attributes for Random Forest.

<table><tr><td rowspan="3">Class</td><td colspan="11">Random Forest</td></tr><tr><td colspan="3">Confusion Matrix</td><td rowspan="2">TP Rate</td><td rowspan="2">FP Rate</td><td rowspan="2">Precision</td><td rowspan="2">Recall</td><td rowspan="2">F-Measure</td><td rowspan="2">MCC</td><td rowspan="2">AUC</td><td rowspan="2">PRC Area</td></tr><tr><td>0</td><td>1</td><td>2</td></tr><tr><td>0</td><td>1013</td><td>106</td><td>10</td><td>0.897</td><td>0.736</td><td>0.598</td><td>0.897</td><td>0.718</td><td>0.211</td><td>0.637</td><td>0.665</td></tr><tr><td>1</td><td>465</td><td>118</td><td>15</td><td>0.197</td><td>0.140</td><td>0.366</td><td>0.197</td><td>0.257</td><td>0.071</td><td>0.562</td><td>0.332</td></tr><tr><td>2</td><td>216</td><td>98</td><td>13</td><td>0.040</td><td>0.014</td><td>0.342</td><td>0.040</td><td>0.071</td><td>0.069</td><td>0.630</td><td>0.252</td></tr><tr><td>Weighted Average</td><td></td><td></td><td></td><td>0.558</td><td>0.448</td><td>0.490</td><td>0.557</td><td>0.481</td><td>0.148</td><td>0.614</td><td>0.502</td></tr></table>

(a)

<table><tr><td rowspan="3">Class</td><td colspan="7">Random Forest</td></tr><tr><td colspan="3">Confusion Matrix</td><td rowspan="2">Accuracy</td><td rowspan="2">SensitivityClass</td><td rowspan="2">SpecificityClass</td><td rowspan="2">PrecisionClass</td></tr><tr><td>0</td><td>1</td><td>2</td></tr><tr><td>0</td><td>1013</td><td>106</td><td>10</td><td></td><td>0.598</td><td>0.897</td><td>0.264</td></tr><tr><td>1</td><td>465</td><td>118</td><td>15</td><td>0.558</td><td>0.366</td><td>0.197</td><td>0.860</td></tr><tr><td>2</td><td>216</td><td>98</td><td>13</td><td></td><td>0.342</td><td>0.040</td><td>0.986</td></tr></table>

(b)

The third group contained only the classifier RBFNetwork. Compared to the previous two groups, the third group had the greatest number of factors: 15 in total. However, it also reduced the factors since the redundant factors in the group are the last six ones. Table 12 presents the detailed results, including a confusion matrix, eight performance measures and four modified performance measures, of the classification of those 15 factors for RBFNetwork.

Table 12 Detailed classification results of the first 15 factors/attributes for RBFNetwork.

<table><tr><td rowspan="3">Class</td><td colspan="11">RBFNetwork</td></tr><tr><td colspan="3">Confusion Matrix</td><td rowspan="2">TP Rate</td><td rowspan="2">FP Rate</td><td rowspan="2">Precision</td><td rowspan="2">Recall</td><td rowspan="2">F-Measure</td><td rowspan="2">MCC</td><td rowspan="2">AUC</td><td rowspan="2">PRC Area</td></tr><tr><td>0</td><td>1</td><td>2</td></tr><tr><td>0</td><td>961</td><td>153</td><td>15</td><td>0.851</td><td>0.605</td><td>0.632</td><td>0.851</td><td>0.725</td><td>0.279</td><td>0.693</td><td>0.716</td></tr><tr><td>1</td><td>382</td><td>191</td><td>25</td><td>0.319</td><td>0.183</td><td>0.417</td><td>0.319</td><td>0.362</td><td>0.148</td><td>0.618</td><td>0.380</td></tr><tr><td>2</td><td>178</td><td>114</td><td>35</td><td>0.107</td><td>0.023</td><td>0.467</td><td>0.107</td><td>0.174</td><td>0.164</td><td>0.680</td><td>0.306</td></tr><tr><td>Weighted Average</td><td></td><td></td><td></td><td>0.578</td><td>0.390</td><td>0.543</td><td>0.578</td><td>0.532</td><td>0.223</td><td>0.669</td><td>0.553</td></tr></table>

(a)

<table><tr><td>RBFNetwork</td></tr></table>

## ACCEPTED MANUSCRIPT

<table><tr><td rowspan="2">Class</td><td colspan="3">Confusion Matrix</td><td rowspan="2">Accuracy</td><td rowspan="2">SensitivityClass</td><td rowspan="2">SpecificityClass</td><td rowspan="2">PrecisionClass</td></tr><tr><td>0</td><td>1</td><td>2</td></tr><tr><td>0</td><td>961</td><td>153</td><td>15</td><td></td><td>0.632</td><td>0.851</td><td>0.395</td></tr><tr><td>1</td><td>382</td><td>191</td><td>25</td><td>0.578</td><td>0.417</td><td>0.319</td><td>0.817</td></tr><tr><td>2</td><td>178</td><td>114</td><td>35</td><td></td><td>0.467</td><td>0.107</td><td>0.977</td></tr></table>

(b)

Altogether, the experimental results of the three groups demonstrate that no matter which kind of classifier is used for classification, the discrimination of only parts of the 21 factors can achieve the best correct rate with the use of the improved mRMR algorithm.

Tables 6-12 present the details of the performance of the system with the medical datasets. As the experimental results illustrate, RBFNetwork outperformed the other six classification approaches with both whole (51.79%) and selected factors (57.79%) that were ordered by the proposed improved mRMR algorithm, whereas Random Forest achieved the worst correct rate with both whole (46.29%) and selected factors (55.84%). The second- and third-greatest classification accuracies were achieved with BayesNet and NBTree with all and selected factors, respectively. The results also indicate that the classification accuracy increased, at most, up to 9.55% for Random Forest after the use of the improved mRMR algorithm, whereas the classification accuracy increased by at least 6.00% for RBFNetwork.

RBFNetwork also outperformed the other classifiers in terms of AUC with selected factors (0.669), whereas NBTree and BayesNet were superior to the others in terms of AUC with whole factors (0.623). J48 obtained the worst AUC with both all (0.542) and selected factors (0.6). Therefore, RBFNetwork can aid doctors and researchers in providing more effective factors for the diagnoses of patients. The second-largest AUC was achieved with the RBFNetwork and “BayesNet and NBTree” classifiers with all and selected factors, respectively. The AUC improved by up to 0.068 with Kstar with the use of the improved mRMR algorithm, whereas it improved by at least 0.035 for both NBTree and BayesNet.

Lastly, the least number of selected factors for bagging under the condition of the best correct rate was four, whereas the highest number of the selected factors for RBFNetwork was 15. Those 15 factors were age, exercise, weight, height, waist, egfr, ldl, bmi, glucose\_ac, sbp, sex, smoking, htn\_med\_hx, triglyceride, and wbc\_count.

In addition, an experiment is also performed to validate whether our method is robust to the distinct initial order of attributes/features. In this experiment, all 21 attributes/features are randomly sorted with a random sequence generator, and these 21 randomly sorted attributes are then ranked their significance

# ACCEPTED MANUSCRIPT

with the improved mRMR algorithm. It is repeated 10 times. It shows that the results of these 10 time sorting with our method are all the same, and the ranking of attributes is “age, exercise, weight, height, waist, egfr, ldl, bmi, glucose\_ac, sbp, sex, smoking, htn\_med\_hx, triglyceride, wbc\_count, hdl, cvd\_med\_hx, lipid\_med\_hx, dm\_med\_hx, creatinine, and stroke\_hx”. The results indicate that our method is accurately robust to the attributes/features in distinct initial order.

Our method not only decreases the number of characteristic factors, but also improves the classification accuracy and AUC by sorting those factors. The method can therefore effectively achieve a higher correct rate and AUC with part of the whole factors than with the whole factors. We also compared our method with several state-of-the-art feature selection algorithms, including MIFS [48], MIFS-U [49], PSO [50], mRMR [51], and OFS-MI [52]. The results of the correct rates among the nine different algorithms (e.g., whole features and MIFS and MIFS-U algorithms for different $\beta$ parameter setups) appear in Fig. 2 for the seven different classifiers, whereas the results of comparing the AUC of the seven different classifiers with the nine algorithms appear in Fig. 3. Moreover, as Figs. 2 and 3 show, the correct rates and AUCs of the seven different classifiers used all of the features and the subsets of features selected by MIFS, MIFS-U, PSO, mRMR, OFS-MI, and our method as inputs. The results indicate that our method achieved better performance than MIFS, MIFS-U, PSO, mRMR, and OFS-MI in terms of both correct rates and AUC.

We performed two-way ANOVA and multiple comparison tests to estimate whether the results of the proposed attribute ranking and selection differed significantly from those of whole features and other approaches. The results indicate that the improved performance was significant $( p < . 0 0 1$ for whole features, MIFS $[ \beta = 0 . 4 , 0 . 8 ] , \mathrm { M I F S - U } [ \beta = 0 . 4 , 0 . 8 ]$ , and $\mathrm { P S O } ; p < . 0 1$ for mRMR and OFS-MI) in terms of correct rates, whereas for the improved AUC, the results indicate that performance was also significant $( p < . 0 0 1$ for whole features, MIFS $( \beta = 0 . 4 , 0 . 8 )$ , MIFS-U $( \beta = 0 . 4 ) ; p < . 0 1$ for MIFS-U $( \beta = 0 . 8 )$ , PSO, mRMR, and OFS-MI). Accordingly, our method can effectively sort and keep important attributes from whole ones in order to substantially improve performance.

![](/api/attachments/FKU98QRH/fulltext/images/d51b0468db290a4738d29efbffd365fdb7a1de3b0241b3cba48e0f9ff11a4c3a.jpg)  
Fig. 2. Comparison of correct rates for seven different classifiers among nine different algorithms (including whole features and the MIFS and MIFS-U algorithms for different β parameter setups).

![](/api/attachments/FKU98QRH/fulltext/images/49b2a32259592a2005afe7360e7574e78ce0092b83dc9841dc84e1e1d46559ab.jpg)  
Fig. 3. Comparison of the AUC for seven different classifiers among nine different algorithms.

## 4. Managerial implications

This study presents a novel decision-making mechanism for the significance assess of risk factors in CVDs. The proposed decision-making system contemplates ranking that perform medical, clinical and healthcare-related attribute/feature sorting and selection. Hence, this model provides a useful tool to support medical analysis in various fields. The identification of significant risk factors is performed in a consistent manner and is first recommended by senior doctors or chosen from the related literatures, and is then ranked and selected by the proposed method via the combined classifier, which conduct the performance and behavior of this system at a higher level in assessing their significance in CVDs. Therefore, one of the contributions of our proposal is to create individualized lengths of the attributes for

# ACCEPTED MANUSCRIPT

each classifier in the assess of significance of risk factors in CVDs. In practice, the decision-making mechanism attains a higher rate of correct rate and AUC compared to several state-of-the-art approaches of analyzing factors from CVDs. The result indicates that it obtains a larger acceptance by the medical community in this kind of decision-making system in the identification of critical risk factors.

The ranking and number of risk factors is an important issue to be considered in the solution due to the flexibility of model. The proposed system aids to overcome intrinsic ambiguities, which are inherent prioritize the ranking involving the most significant attributes from the medical point of view.

CVDs are severe diseases growing incidence worldwide has greatly increased national healthcare spending. CVDs continue to merit investigation due to their diverse risk factors despite a wide variety of studies. In this study, we have improved the quality of selected risk factors used for diagnostic and treatment suggestions because each doctor has his/her own peculiarities and may even make a decision according to his/her past experiences despite having provided the suggested factors. Hence, we believe that the good use of chosen factors, instead of adopting factors from his/her past experiences, makes it to facilitate for the doctors to comprehend the meaning of new factors acquired from the proposed method. Such knowledge can benefit the proper selection of CVD risk factors and thereby assist doctors in making better decisions in diagnostics and treatment. The merit and contribution of this study can effectively reduce treatment costs and further lower the economic burden of healthcare. In addition, the proposed method can be generic to be also applicable at various medical, biomedical, financial fields to assist doctors/researchers in further improving the efficiency and efficacy of their work.

## 5. Conclusions and future work

In recent decades, attribute sorting, ranking, and selection in medical dataset processing have declined. In response, we identified potential influential factors that were suitable for analysis as recommended by senior doctors or the related literature. We then sorted and arranged the selected factors with the improved mRMR algorithm. After sorting, the factors were discriminated by a classifier to obtain a line of correct rates for ordered factors with different numbers, given the benefit of identifying the best numbers and positions of attributes with the most correct rates. Although the number of original attributes was 21 per the recommendations of the doctors and literature, the average number of attributes for obtaining the best classification accuracy from seven different classifiers was 7.43. The results therefore

# ACCEPTED MANUSCRIPT

indicate that the proposed system can effectively provide auxiliary decision-making support for physicians and researchers to further improve the efficiency and efficacy of the evaluation and prediction of CVDs. The improved mRMR algorithm yielded the number of attributes and factors required for seven different classifiers (Fig. 4). In addition, a pseudo-Pareto approach (80-20 rule) [53] is also applied to keep track of the changes that how many variables cause how much of accuracy change (Fig. 5).

![](/api/attachments/FKU98QRH/fulltext/images/577f203b77e968721763b9740f26bbfe43632e49e59864d089c38f4ed7af3135.jpg)  
Fig. 4. Number of factors/attributes required for seven different classifiers under the use of the present improved mRMR algorithm.

![](/api/attachments/FKU98QRH/fulltext/images/a92b02619b75490db92c6b099cdcf190da611b9d6292833217d3f3d3b49ad847.jpg)  
Fig. 5. Keeping track of the changes that how many variables cause how much of accuracy change with a pseudo-Pareto approach (80-20 rule).

The proposed methods are applicable to datasets or big data in various biomedical and financial fields to assist users in improving the efficiency and efficacy of their work or research. The results of such studies can also be further verified if the datasets are large enough.

In future work, we plan to enhance the efficiency of the proposed method by introducing other approaches (e.g., particle swarm optimization) into the improved mRMR algorithm and exploring their synergies, which are inspired by Oztekin et al. [54]. We also plan to integrate the textual information of patients’ clinical histories and examinations into the search for significant factors/attributes.

## Acknowledgments

This work was supported by the Ministry of Science and Technology, Taiwan [grant numbers: MOST105-2410-H-194-059-MY3]. The author would like to express his sincere appreciation to Dr. Hung and Dr. Yun, Taipei Mackay Memorial Hospital, Taiwan for their assistance to provide the medical data sets of CVDs, and Bing-Ting Tsai for his assistance to handle part materials.

## References

[1] J.L. Reishtein, Obstructive sleep apnea: a risk factor for cardiovascular disease, Journal of Cardiovascular Nursing 26 (2) (2011) 106-116.

[2] G. Santulli, Epidemiology of cardiovascular disease in the 21st century: updated numbers and updated facts, J Cardiovasc Dis 1 (1) (2013) 1-2.

[3] W.T. Friedewald, R.I. Levy, D.S. Fredrickson, Estimation of the concentration of low-density lipoprotein cholesterol in plasma without use of the preparative ultracentrifuge, Clinical Chemistry 18 (6) (1972) 499-502.

[4] P.K. Mehta, J. Baer, C. Nell, L.S. Sperling, Low-density lipoprotein apheresis as a treatment option for hyperlipidemia, Current Treatment Options in Cardiovascular Medicine 11 (4) (2009) 279-288.

[5] D.A. Morrow, N. Rifai, E.M. Antman, D.L. Weiner, C.H. McCabe, C.P. Cannon, E. Braunwald, C-reactive protein is a potent predictor of mortality independently of and in combination with troponin T in acute coronary syndromes: a TIMI 11A substudy, Journal of the American College of Cardiology 31 (7) (1998) 1460-1465.

[6] T.A. Pearson, G.A. Mensah, R.W. Alexander, J.L. Anderson, R.O. Cannon, M. Criqui, F. Vinicor, Markers of inflammation and cardiovascular disease application to clinical and public health practice: a statement for healthcare professionals from the centers for disease control and prevention and the American Heart Association, Circulation 107 (3) (2003) 499-511.

[7] J.P. McCormack, G.M. Allan, Measuring hsCRP-an important part of a comprehensive risk profile or a clinically redundant practice?, PLoS Medicine 7 (2) (2010) e1000196.

[8] G. Kong, D.L. Xu, R. Body, J.B. Yang, K. Mackway-Jones, S. Carley, A belief rule-based decision support system for clinical risk assessment of cardiac chest pain, European Journal of Operational Research 219(3) (2012) 564-573

[9] P.M. Ridker, Clinical application of C-reactive protein for cardiovascular disease detection and prevention, Circulation 107 (3) (2003) 363-369.

[10] P.M. Ridker, J.E. Buring, N.R. Cook, N. Rifai, C-reactive protein, the metabolic syndrome, and risk of incident cardiovascular events an 8-year follow-up of 14 719 initially healthy American women, Circulation 107 (3) (2003) 391-397.

[11] P.M. Ridker, C.H. Hennekens, J.E. Buring, N. Rifai, C-reactive protein and other markers of inflammation in the prediction of cardiovascular disease in women, New England Journal of Medicine 342 (12) (2000) 836-843.

[12] P.M. Ridker, N. Rifai, L. Rose, J.E. Buring, N.R. Cook, Comparison of C-reactive protein and low-density lipoprotein cholesterol levels in the prediction of first cardiovascular events, New England Journal of Medicine 347 (20) (2002) 1557-1565.

[13] S. Maldonado, J. Pérez, C. Bravo, Cost-based feature selection for Support Vector Machines: An application in credit scoring, European Journal of Operational Research 261(2) (2017) 656-665.

[14] G.V. Lashkia, L. Anthony, Relevant, irredundant feature selection and noisy example elimination, IEEE Transactions on Systems, Man, and Cybernetics, Part B: Cybernetics 34 (2) (2004) 888-897.

[15] M.A. Sodenkamp, M. Tavana, D. Di Caprio, Modeling synergies in multi-criteria supplier selection and order allocation: An application to commodity trading, European Journal of Operational Research 254(3) (2016) 859-874.

[16] L. Yu, H. Liu, Efficient feature selection via analysis of relevance and redundancy, Journal of Machine Learning Research 5 (2004) 1205-1224.

[17] M. Zorrilla, D. García-Saiz, A service oriented architecture to provide data mining services for non-expert data miners,

Decision Support Systems 55 (1) (2013) 399-411.

[18] W. Wang, P. Jones, D. Partridge, A comparative study of feature-salience ranking techniques, Neural computation 13 (7) (2001) 1603-1623.

[19] Z. Zhu, Y.S. Ong, M. Dash, Wrapper-Filter Feature Selection Algorithm Using a Memetic Framework, IEEE Transactions on Systems, Man, and Cybernetics- Part B: Cybernetics 37(1) (2007) 70-76.

[20] R. Battiti, Using mutual information for selecting features in supervised neural net learning, IEEE Transactions on Neural Networks 5 (4) (1994) 537-550.

[21] P.A. Estévez, M. Tesmer, C.A. Perez, J.M. Zurada, Normalized mutual information feature selection, IEEE Transactions on Neural Networks 20 (2) (2009) 189-201.

[22] F. Maes, D. Vandermeulen, P. Suetens, Medical image registration using mutual information, Proceedings of the IEEE 91 (10) (2003) 1699-1722.

[23] H. Peng, F. Long, C. Ding, Feature selection based on mutual information criteria of max-dependency, max-relevance, and min-redundancy, IEEE Transactions on Pattern Analysis and Machine Intelligence 27 (8) (2005) 1226-1238.

[24] S.F. Da Silva, M.X. Ribeiro, J.D.E. Batista Neto, C. Traina-Jr, A.J. Traina, Improving the ranking quality of medical image retrieval using a genetic feature selection method, Decision Support Systems 51 (4) (2011) 810-820.

[25] S. Acid, L.M. De Campos, M. Fernández, Minimum redundancy maximum relevancy versus score-based methods for learning Markov boundaries, 11th International IEEE Conference in Intelligent Systems Design and Applications (ISDA) (2011) 619-623.

[26] X. Jin, E.W. Ma, L.L Cheng, M. Pecht, Health monitoring of cooling fans based on Mahalanobis distance with mRMR feature selection, IEEE Transactions on Instrumentation and Measurement 61 (8) (2012) 2222-2229.

[27] H. Rabiu, M.I. Saripan, S. Mashohor, M.H. Marhaban, 3D facial expression recognition using maximum relevance minimum redundancy geometrical features, EURASIP Journal on Advances in Signal Processing 213 (2012) 1-8.

[28] S. Cang, H. Yu, Mutual information based input feature selection for classification problems, Decision Support Systems 54 (1) (2012) 691-698.

[29] V. Vapnik, The Nature of Statistical Learning Theory, Springer-Verlag (1995) New York.

[30] K.B. Irani, Multi-interval discretization of continuous-valued attributes for classification learning, Machine Learning (1993) 1022-1027.

[31] S.S. Haykin, Neural networks: a comprehensive foundation, Tsinghua University Press (2001).

[32] L. Breiman, Bagging predictors, Machine Learning 24 (2) (1996) 123-140.

[33] P.M. Ridker, J.E. Buring, N. Rifai, N.R. Cook, Development and validation of improved algorithms for the assessment of global cardiovascular risk in women: the Reynolds Risk Score, Journal of the American Medical Association (JAMA) 297 (6) (2007) 611-619.

[34] P.M. Ridker, Evaluating novel cardiovascular risk factors: can we better predict heart attacks?, Annals of Internal Medicine 130 (11) (1999) 933-937.

[35] I.S. Ockene, C.E. Matthews, N. Rifai, P.M. Ridker, G. Reed, E. Stanek, Variability and classification accuracy of serial high-sensitivity C-reactive protein measurements in healthy adults, Clinical Chemistry 47 (3) (2001) 444-450.

[36] G. Zanini, E. Gorga, F.D. Magro, B. Okunuga, F. Pasini, Cardiovascular Risk Factors, Diet and Lifestyle among a Group of

Italian Young Adults Students, International Journal of Clinical Cardiology 2(1) (2014) 018.

[37] O. Ben-Assuli, Assessing the perception of information components in financial decision support systems, Decision Support Systems 54(1) (2012) 795-802.

[38] Y.O. Serrano-Silva, Y. Villuendas-Rey, C. Yáñez-Márquez, Automatic feature weighting for improving financial Decision Support Systems, Decision Support Systems 107 (2018) 78-87.

[39] J. Ghattas, P. Soffer, M. Peleg, Improving business process decision making based on past experience, Decision Support Systems 59 (2014) 93-107.

[40] V. Sadovykh, D. Sundaram, S. Piramuthu, Do decision-making structure and sequence exist in health online social networks?, Decision Support Systems 74 (2015) 102-120.

[41] N. Meskens, A. Guinet, Decision making in healthcare, Decision Support Systems 55(2) (2013) 577.

[42] H. Wimmer, V.Y. Yoon, V. Sugumaran, A multi-agent system to support evidence based medicine and clinical decision making via data sharing and data privacy, Decision Support Systems 88 (2016) 51-66.

[43] P.D. Haghighi, F. Burstein, A. Zaslavsky, P. Arbon, Development and evaluation of ontology for intelligent decision support in medical emergency management for mass gatherings, Decision Support Systems 54(2) (2013) 1192-1204.

[44] A. Oztekin, M.R. Khan, A business-analytic approach to identify critical factors in quantitative disciplines, Journal of Computer Information Systems 54(4) (2014) 60-70.

[45] M. Bogaert, M. Ballings, R. Bergmans, D. Van den Poel, Predicting Movie Watching Behavior using Facebook data and Information-fusion Sensitivity Analysis, 39th ISMS Marketing Science Conference (2017).

[46] L. Al-Ebbini, A. Oztekin, Y. Chen, FLAS: Fuzzy lung allocation system for US-based transplantations, European Journal of Operational Research 248(3) (2016) 1051-1065.

[47] F.B. Boudi, Noncoronary atherosclerosis overview of atherosclerosis, Medscape (2014).

[48] R. Battiti, Using mutual information for selecting features in supervised neutral net learning, IEEE Transactions Neural Networks 5 (1994) 537-550

[49] N. Kwak, C.H. Choi, Input feature selection for classification problems, IEEE Transactions Neural Networks 13 (2002) 143-159.

[50] J. Kennedy, Particle swarm optimization, Encyclopedia of machine learning, Springer US (2011) 760-766.

[51] H. Peng, F. Long, C. Ding, Feature selection based on mutual information: criteria of max-dependency, max-relevance and min-redundancy, IEEE Transactions on Pattern Analysis and Machine Intelligence 27(8) (2005) 1226-1238.

[52] T.W. Chow, D. Huang, Estimating optimal feature subsets using efficient estimation of high-dimensional mutual information, IEEE Transactions Neural Networks 16(1) (2005) 213-224.

[53] A. Oztekin, D. Delen, A. Turkyilmaz, S. Zaim, A machine learning-based usability evaluation method for eLearning systems, Decision Support Systems 56 (2013) 63-73.

[54] A. Oztekin, L. Al-Ebbini, Z. Sevkli, D. Delen, A decision analytic approach to predicting quality of life for lung transplant recipients: A hybrid genetic algorithms-based methodology, European Journal of Operational Research 266(2) (2018) 639-651.

# ACCEPTED MANUSCRIPT

## Author Biography

Wei-Yen Hsu received the Ph.D. degree in the Department of Computer Science and Information Engineering, National Cheng Kung University, Tainan, Taiwan, in 2008. He is a professor in the Department of Information Management, National Chung Cheng University now. His research interests include data mining, machine learning, and big data analysis. He is also a Founding Member of Brain-Computer Interface Society, and Associate Editors of two journals, “Medicine” and “BMC Medical Informatics and Decision Making”.

# ACCEPTED MANUSCRIPT

## Highlights

1. Despite numerous diagnostic and treatment suggestions, cardiovascular diseases continue to merit investigation due to their diverse risk factors.

2. To assist doctors and researchers in identifying the significance of CVD risk factors, in this study we propose a novel ranking and attribute (or feature) selection algorithm.

3. We applied seven popular machine learning technologies to generate attribute-ranked datasets in order to identify the ideal number of factors/attributes for each classifier.

4. The results of the comparisons indicate that the performance of the proposed method was significantly better than the performance of whole factors and that of several state-of-the-art algorithms.

5. Since such knowledge can assist doctors in making better decisions in diagnostics and treatment as well as reduce treatment costs and thus lower the economic burden of healthcare.
