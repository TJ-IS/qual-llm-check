---
otero_id: 3380
otero_key: "4SUDQFDR"
title: "Processing electronic medical records to improve predictive analytics outcomes for hospital readmissions"
authors: "Hamed M. Zolbanin; Dursun Delen"
year: "2018"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2018.06.010"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

Processing electronic medical records to improve predictive analytics outcomes for hospital readmissions

![](/api/attachments/4SUDQFDR/fulltext/images/651cc39b65cee028c3fb7555d48dd55ef1ffde11b487822b6e2f085d785715d6.jpg)

Hamed M. Zolbanin, Dursun Delen

<table><tr><td>PII:</td><td>S0167-9236(18)30107-6</td></tr><tr><td>DOI:</td><td>doi:10.1016/j.dss.2018.06.010</td></tr><tr><td>Reference:</td><td>DECSUP 12968</td></tr><tr><td>To appear in:</td><td>Decision Support Systems</td></tr><tr><td>Received date:</td><td>17 December 2017</td></tr><tr><td>Revised date:</td><td>25 June 2018</td></tr><tr><td>Accepted date:</td><td>26 June 2018</td></tr></table>

Please cite this article as: Hamed M. Zolbanin, Dursun Delen , Processing electronic medical records to improve predictive analytics outcomes for hospital readmissions. Decsup (2018), doi:10.1016/j.dss.2018.06.010

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# TITLE PAGE

# Processing Electronic Medical Records to Improve Predictive Analytics Outcomes for Hospital Readmissions

Hamed M. Zolbanin<sup>a</sup> and Dursun Delen<sup>b,</sup> <sup>#</sup>

<sup>a</sup> Department of Information Systems and Operations Management, Miller College of Business, Ball State University, Muncie, IN 47306, U.S.A. Email: hmzolbanin@bsu.edu

<sup>b</sup> Department of Management Science and Information Systems, Center for Health Systems Innovation, Spears School of Business, Oklahoma State University, Tulsa, OK 74106, U.S.A. Email: dursun.delen@okstate.edu

<sup>#</sup> Corresponding author:

Spears and Patterson Endowed Chairs in Business Analytics

Department of Management Science and Information Systems

Web: http://spears.okstate.edu/delen

# Processing Electronic Medical Records to Improve Predictive Analytics Outcomes for Hospital Readmissions

## Abstract

Hospital readmissions are costly but largely preventable. In recent years, many researchers have used predictive analytics to build models that can minimize the adverse economic and social consequences of readmissions in chronic diseases. Most of these studies, however, have focused on improving the results either through the development of better models or through employing richer data sets. A very small number of them have focused on a comprehensive data preprocessing to improve the efficacy of analytics individual- and database-level historical information from the medical records to improve the performance of readmission analytics. We test and validate this method using two rather large data sets that belong to chronic diseases with the highest rates of hospital readmissions. We conclude that proper processing of large clinical data sets with analytics and big data technologies can provide competitive advantages to health care organizations.

Keywords: Predictive analytics; hospital readmissions; electronic medical records; data processing, big data technologies

# ACCEPTED MANUSCRIPT

## 1. Introduction

Preventable hospital readmissions comprise a big part of the unnecessary medical expenditures. According to data from the Center for Health Information and Analysis (CHIA), roughly two million patients are readmitted to hospitals each year, costing Medicare \$27 billion, of which \$17 billion is potentially avoidable (Kauffman, 2016). Data-driven analyses show that the largest volume of such readmissions, in which patients are readmitted within 30 days of discharge, occur among patients with chronic diseases. Specifically, heart failure (HF) and chronic obstructive pulmonary disease (COPD) alone account for 9% of all medical admissions, and are among the conditions with the highest readmission rates, ranging between 23% to 26% (Center for Healthcare Quality & Payment Reform, 2013).

Apart from the initiative by the U.S. Centers for Medicare and Medicaid Services (CMS) that penalizes hospitals for avoidable readmissions of certain chronic diseases, practitioners and scholars from related disciplines have also attended to various aspects of ospital readmissions and how to reduce them. Regarding the potentials of analytics in improving health care outcomes through the use of electronic health records (Kohli & Tan, 2016), information systems (IS) and medical informatics researchers have employed data mining and predictive analytics to identify patients at risk of readmission, along with the factors that contribute the most to early rehospitalization. From a broad perspective, these efforts have mainly focused on either improving the prediction results by developing better models or employing richer data sets. A fewer number of them, if any, have used extensive data processing to extract overall and individual historical information from large repositories of electronic medical records (EMR) to build more accurate predictive models. Because small improvements in the performance of analytical models can result in substantial cost savings or profit gains (Baesens, Bapna, Marsden, Vanthienen, & Zhao, 2016), data processing is too important to be overlooked, as it is proven to be the best way to boost the performance of analytical models in terms of discrimination or calibration (Baesens, 2014).

# ACCEPTED MANUSCRIPT

To illustrate the importance of data preparation in readmission analytics, we process two data sets of HF and COPD hospital visits using a novel approach that augments the data sets by updating each record of a patient according to the historical information extracted from the previous records. We input the additional information as new variables to predictive models and illustrate their effect on the final performance. Therefore, this paper has four major contributions:

 It demonstrates the value and importance of data processing in developing predictive analytics models for readmission of patients with chronic diseases.

 It shows how overall and individual historical information, which are an important feature of EMR, can be used to augment patient-level records for better prediction results.

 It improves the prediction of hospital readmissions based on EMR data for patients with HF and COPD.

 It provides an evidence for the competitive advantage of organizations that employ predictive analytics and big data technologies for enhanced decision making in health care.

In the following sections, we start by reviewing prior work on predictive analytics for hospital readmissions. Next, we introduce a data processing approach that allows evaluating each patient’s risk of readmission by considering all previous hospital encounters for similar complications. Subsequently, we assess this approach empirically on data sets obtained from a fairly large repository of HF and COPD hospital visits. Next, we discuss the potential implications of our findings for hospitals and health care delivery organizations. The final section concludes the paper, discusses limitations, and recommends some avenues for future research.

## 2. Prior Work

Since hospital readmissions are associated with high financial costs and poor patient outcomes (Bueno et al., 2010; Colleen K. McIlvennan, Zubin J. Eapen, Larry A. Allen, 2012; Jencks, Williams, & Coleman, 2009), predicting risk of readmission is of great interest to both the health care delivery system and patients who could benefit from care transition interventions (Kansagara et al., 2011). Models built to predict hospital readmissions have either used a real-time or a retrospective approach (Kansagara et al., 2011). In real-time models, variables are available on or shortly after the index hospital admission, whereas in retrospective efforts, variables are mostly known after the patient is discharged. Regarding that many EMR data repositories collect and aggregate data on various aspects of hospital encounters, using such data belong to the retrospective category.

Regarding their focus, retrospective studies on hospital readmissions can be divided into two broad classes. In the first class of these efforts, the main contribution of the study revolves around the development and assessment of novel predictive analytics models for hospital readmissions. For instance, (Bardhan, Oh, Zheng, & Kirksey, 2015, 2011) develop a model that predicts the propensity, frequency, and timing of readmissions of patients with congestive heart failure. In another study, (Lin, Chen, Brown, Li, & Yang, 2017) implement an EMR-based decision support system that profiles patients who suffer from chronic conditions, and enables predicting who may be at risk of adverse health events. Therefore, timely preventive interventions can be provided for patients at higher risk of hospital readmission. Other retrospective modeling efforts have used more common techniques, such as ensembles (Mesgarpour, Chaussalet, & Chahed, 2017; Turgeman & May, 2016), clustering (Veloso et al., 2014), and logistic regression (e.g., Amarasingham et al., 2015; Tsui, Au, Wong, Cheung, & Lam, 2015).

The focal point in the second group of retrospective studies is data, where predictive performance is boosted using novel or richer data sets. Examples of such efforts in the IS and medical informatics literature are the use of data on patients’ creatinine levels (Ben-Assuli, Padman, Leshno, & Shabtai, 2016), combination of clinical and nonclinical risk factors (Amarasingham et al., 2010; Hebert et al., 2014), mining high-dimensional administrative claims data (He, Mathews, Kalloo, & Hutfless, 2014), evaluation of self-reported discharge forms (Inouye et al., 2015), and integration of comorbidity, laboratory, medication and visit history records (Cai et al., 2016; Walsh & Hripcsak, 2014).

# ACCEPTED MANUSCRIPT

There are other studies on hospital readmission whose findings can potentially help improve predictive models. These studies, however, do not take a predictive stance, but rather explore the relationship between certain variables and individuals’ risk of rehospitalization. In an exploration of the antecedents of patients’ readmission, (Ayabakan, Bardhan, & Zheng, 2016) find that nonclinical factors such as patients’ latent health status can impact readmission significantly. Similarly, shorter hospital stays are found to be related to higher chances of early rehospitalization (Oh, Zheng, & Bardhan, 2017).

A noticeable limitation in the extant readmission literature, both among the predictive and nonpredictive studies, is that they all evaluate the strength of association between the predictors and the response, but fall short of extracting valuable information that is hidden in EMR data sets. More specifically, the focus in previous studies has been on variables and patients as individuals, but not on how individuals differ in terms of their history of hospital visits or health care use. Patients with heavy hospital utilization more likely have characteristics that put them at higher risk of readmission or even death after discharge from hospital (van Walraven, Wong, Forster, & Hawken, 2013). While some studies (e.g., Cai et al., 2016; Wang et al., 2016) have processed EMR data to extract patients’ historical information, such as number of days since their last admission or their cumulative length of hospital stay during the previous year, they have not used a comprehensive approach and have not created a risk index that shows how each patient compares to others who were admitted before them. Regarding the value of data processing to the development of enhanced predictive models (Martens, Provost, Clark, & Junqué De Fortuny, 2016), in this paper, we propose an approach to extract such information from EMR data, add the information as new variables to the data sets, and evaluate the method both in terms of its computational complexity and its contribution to improving predictive models for hospital readmissions.

## 3. Methodology

Every record in our data sets is uniquely distinguishable by an encounter identifier. Clearly, different visits of a single patient at different points of time generate records with different encounter identifiers. To keep track of a patient’s visits over time, a separate variable (patient key) is included in each record.

# ACCEPTED MANUSCRIPT

We used “patient key” in our preliminary data processing step to specify whether a certain visit resulted in a future readmission. To this goal, we sorted the data by patient key and admission date/time. If a patient had only one visit recorded in the database, a binary variable representing future readmissions was assigned a value of 0. For patients who had more than one visit recorded, we compared the discharge date/time of the i record for that patient with the admission date/time of the $i ^ { t h }$ $( i + I ) ^ { \mathrm { t h } }$ record. Depending 0. We used this binary variable as the response variable in our effort.

Because EMR data are collected for purposes other than data analytics (Piri, Delen, Liu, & Zolbanin, 2017), processing and analyzing such data involves various challenges and computational constraints (Herland, Khoshgoftaar, & Wald, 2014; Jagadish et al., 2014). Specifically, high dimensionality, sparsity, and class imbalance pose serious impediments to the development of accurate predictive models using EMR data (Jovanovic, Radovanovic, Vukicevic, Van Poucke, & Delibasic, 2016). To minimize the adverse effects of these threats, we performed a preliminary set of variable selection and data cleaning activities that resulted in a smaller number of variables, reduced sparsity, and created balanced data sets. Predictors were selected based on a combination of domain knowledge and empirical evidence of association with the response (Shmueli & Koppius, 2011); sparsity was handled via imputation; and class imbalance was resolved with the application of the synthetic minority oversampling technique (Chawla, Bowyer, Hall, & Kegelmeyer, 2002).

In selecting the variables to be included in our study, we first reviewed the meaning and purpose of each variable from the accompanying documents of the EMR data warehouse. This resulted in identification of several “descriptor” variables that would not add any new information to data mining algorithms. Next, we excluded variables that were not semantically related to the purpose of our study. For instance, we discarded anonymized fields that represented the admitting physician or the hospital. Similarly, we discarded variables that had a single value (e.g., the coding standard used to classify diseases), almost a single value (e.g., acute vs. non-acute status and urban vs. rural status of the hospital), too many different levels (e.g., drug code), or more than 50 percent missing values (e.g., patient’s weight). Finally, using the values of a flag variable, we discarded all those records whose admission and discharge date/times were not accurate. We refer to the data sets that were created through these preliminary steps as the “base data sets”. We use the base data sets as input to our proposed processing method, which is explained next.

## 3.1. Extracting Patients’ Comparative History from EMR Data

Several records may belong to a single patient in EMR data, and some of those records could be readmissions. As we mentioned earlier, because chronic patients’ current health status is not independent from their health background and history of health care use, it is rather simplistic to view medical records of a patient in isolation. Therefore, to build more accurate predictive models for hospital readmission, not only do we need to consider the progression or regression of a patient’s health from a visit to the other, but also we need to compare their health with that of other patients in the data set for more precise risk assessment. Previous studies have found that patients with hospital utilization likely have characteristics that increase the risk of readmission after discharge from hospital (van Walraven et al., 2013), and that there is a relationship between the severity of illness and risk of readmission among patients with chronic conditions (Wang et al., 2016). Hence, patients with more severe diseases have a shorter average time between consecutive visits. Similarly, acute disease stages have been found to be related to longer hospital stays (Nowiński, Kamiński, Korzybski, Stokłosa, & Górecka, 2011). Consequently, we consider the time between two consecutive visits of a patient and their length of stay in hospital to be two indicators of their overall risk of readmission. This means a patient who, on average, returns to hospital in only 25 days has a greater probability of being readmitted within 30 days than another patient who is usually rehospitalized every 250 days. This choice is inspired by a previous study (Cai et al., 2016), where the authors employed patients’ cumulative length of stay (LOS) in the preceding year and the number of days since their last visit to develop models for the real-time prediction of readmissions. However, since they collected this historical information only at the patient level, we extend their approach by considering such information across all prior visits in the data set. This requires a considerable amount of data processing, because EMRs are transaction-based (Chae, Yoo, Kim, & Chae, 2011), rather than aggregated.

With this introduction, now let $P _ { i }$ be patient i, $P _ { i l } V _ { j } J$ represent the $j ^ { t h }$ hospital visit of $P _ { i } ,$ and $P _ { i } / V _ { j } / X J ]$ represent the value of variable X for the $j ^ { t h }$ visit of $P _ { i } .$ . Then, we show the admission and discharge date/time of $P _ { i l } V _ { j } J$ with $P _ { i } [ V _ { j } [ T _ { a d m i s s i o n } ] J ]$ and $P _ { i } [ V _ { j } [ T _ { d i s c h a r g e } ] J ,$ , respectively. We define a new variable, TSLV (standing for time since last visit), and populate it with the following values:

$$
\left\{ \begin{array}{l} \text {. (missing value), if j = 1} \\ \mathrm {P_ {i} [V_ {j + 1} [T_ {admission} ]] - P_ {i} [V_ {j} [T_ {discharge} ]], if j > 1} \end{array} \right.\tag{1}
$$

Therefore, unless a record is a patient’s first ever visit in the EMR data (in which case, TSLV will be assigned a missing value), TSLV will be filled with the number of days between a patient’s previous discharge and current admission.

Regarding the importance of patients’ history of hospitalizations (Cai et al., 2016), using the new variable TSLV and regarding all visits of P<sub>i</sub> prior to $P _ { i l } V _ { j } J ,$ , we next create a new variable that holds the average time between consecutive admissions of $P _ { i } .$ . Values of this variable, which contains average TSLV at the patient level, are obtained from Eq. 2. Based on this equation, a patient’s current average time between visits (i.e., the value of the new variable in a certain record) is calculated by dividing the sum of the time between admissions of that patient in all his prior hospital visits by the number of times that patient has been hospitalized. The current visit $( P _ { i } I V _ { j } J )$ is also considered in this calculation.

$$
\mathrm{P} _ {\mathrm{i}} \left[ \mathrm{V} _ {\mathrm{j}} \left[ \text {avg\_patient\_tslv} \right] \right] = \frac {\sum_ {k = 1} ^ {j} P _ {i} \left[ V _ {k} [ T S L V ] \right]}{j}\tag{2}
$$

Following a similar logic as used in Eq. 2, we define another variable to maintain the total average time between visits throughout the EMR data. The value of this variable in each record, therefore, shows the global average of TSLV across all patients in the data set whose date/time of discharge was earlier than the admission date/time of the current visit of the current patient. We use this variable to obtain a rough estimate of each patient’s overall health (and hence, the likelihood of being readmitted) in comparison to the average in the whole data set. Assuming that the current record belongs to the $m ^ { t h }$ visit of the $n ^ { t h }$ patient $( P _ { n } I V _ { m } J )$ , value of this variable for the current record is determined from Eq. 3.

$$
\mathrm{P} _ {\mathrm{n}} \left[ \mathrm{V} _ {\mathrm{m}} \left[ \text {avg\_total\_tslv} \right] \right] = \frac {\sum P _ {i} \left[ V _ {j} [ T S L V ] \right]}{\operatorname{count} \left(P _ {i} \left[ V _ {j} \right]\right)} \text {where} \mathrm{P} _ {\mathrm{i}} \left[ \mathrm{V} _ {\mathrm{j}} \left[ \mathrm{T} _ {\text {discharge}} \right] \right] \leq \mathrm{P} _ {\mathrm{n}} \left[ \mathrm{V} _ {\mathrm{m}} \left[ \mathrm{T} _ {\text {admission}} \right] \right]\tag{3}
$$

Because TSLV is given a missing value for the first admission of each patient, variable avg\_patient\_tslv contains as many missing records as there are unique patients in the data set. The variable capturing the total average time between visits (avt\_total\_tslv), however, is not as seriously subject to this issue. This is true because the latter variable would only be assigned a missing value if all records in the data set with a discharge date/time earlier than the admission date/time of the current record belonged to first visits of various patients, which is much less likely than is the case for the patient level variable (avg\_patient\_tslv). There are several options to deal with the issue of missingness in these two variables. For example, we can replace missing values with the overall average of TSLV across all the data set. However, since this option would limit the variables’ predictive power, we choose to impute these missing values using a decision tree method.

Similarly, regarding the importance of patients’ historical LOS (Cai et al., 2016), we repeat the procedures used in Eq. 2 and Eq. 3 with LOS as the base variable. In other words, we define two additional variables to specify patients’ average individual LOS for their previous admissions, as well as the overall average LOS across all admissions (by any patient) that occurred before a certain medical record. Values of these new variables are determined according to Eq. 4 and Eq. 5. Since the admission and discharge times of every visit are specified, these variables do not have missingness problems.

$$
\mathrm{P} _ {\mathrm{i}} [ \mathrm{V} _ {\mathrm{j}} [ \mathbf {a v g \_ p a t i e n t \_ l o s} ] ] = \frac {\sum_ {k = 1} ^ {j} P _ {i} [ V _ {k} [ L O S ] ]}{j}\tag{4}
$$

$$
\mathrm{P} _ {\mathrm{n}} \left[ \mathrm{V} _ {\mathrm{m}} \left[ \text {avg\_total} \right. \text {los} ] \right] = \frac {\sum P _ {i} \left[ V _ {j} [ L O S ] \right]}{\operatorname{count} \left(P _ {i} \left[ V _ {j} \right]\right)} \text {where} \mathrm{P} _ {\mathrm{i}} \left[ \mathrm{V} _ {\mathrm{j}} \left[ \mathrm{T} _ {\text {discharge}} \right] \right] \leq \mathrm{P} _ {\mathrm{n}} \left[ \mathrm{V} _ {\mathrm{m}} \left[ \mathrm{T} _ {\text {admission}} \right] \right]\tag{5}
$$

To evaluate how a patient’s history of hospital visits compares with others, in the next step of our data processing approach, we define two short-term and two long-term ratios for each hospital visit in the EMR data. These ratios are calculated based on the patient-level and total averages that were obtained from Eq. 2 through Eq. 5. The values of these ratios are determined by Eq. 6 to Eq. 9.

$$
\text { short\_readmission\_history } = \frac {\text { TSLV }}{\text { avg\_total\_tslv }}\tag{6}
$$

$$
\text { long\_readmissoin\_history } = \frac {\text { avg\_patient\_tslv } ^ {1}}{\text { avg\_total\_tslv }}\tag{7}
$$

$$
s h o r t \_ l o s \_ h i s t o r y = \frac {l o s}{a v g \_ t o t a l \_ l o s}\tag{8}
$$

$$
l o n g \_ l o s \_ h i s t o r y = \frac {a v g \_ p a t i e n t \_ l o s}{a v g \_ t o t a l \_ l o s}\tag{9}
$$

Finally, we standardize the ratios defined in Eq. 6 through Eq. 9 to create four comparative indexes. For the readmission ratios shown in Eq. 6 and Eq. 7, larger values indicate that the patient is at a lower risk of readmission, whereas smaller values denote a greater risk of readmission due to the patient’s poorer health status. Therefore, we use a standardization formula that maps the largest value to zero and the smallest value to one. For the LOS ratios, we assume that smaller values belong to patients who generally have a better health status than patients with larger values. Consequently, we use a standardization formula that maps the smallest value to zero and the largest value to one. The standardization and mapping formulas that define the variables representing patients’ comparative history of health are illustrated in Eq. 10 to $\operatorname { E q . } 1 3 .$ To reduce the skewness of these variables, we next categorize them based on the $1 ^ { \mathrm { s t } } , 5 ^ { \mathrm { t h } } , 1 0 ^ { \mathrm { t h } } , 2 5 ^ { \mathrm { t h } } , 5 0 ^ { \mathrm { t h } } , 7 5 ^ { \mathrm { t h } } , 9 0 ^ { \mathrm { t h } } , 9 5 ^ { \mathrm { t h } }$ , and $9 9 ^ { \mathrm { t h } }$ percentiles to create the comparative indexes.

$$
\text { short\_readmission\_index } = \frac {\max (\text { short\_readmission\_history }) - \text { short\_readmission\_history }}{\max (\text { short\_readmission\_history })}\tag{10}
$$

$$
\text { long\_readmission\_index } = \frac {\max (\text { long\_readmission\_history }) - \text { long\_readmission\_history }}{\max (\text { long\_readmission\_history })}\tag{11}
$$

$$
\text { short\_los\_index } = \frac {\text { short\_los\_history }}{\max (\text { short\_los\_history })}\tag{12}
$$

$$
\text { long\_los\_index } = \frac {\text { long\_los\_history }}{\max (\text { long\_los\_history })}\tag{13}
$$

# ACCEPTED MANUSCRIPT

We add the numerical variables and the categorized indexes created in Eq. 1 to Eq. 13 as additional variables to the base data sets before developing our predictive models for hospital readmission among inpatients with HF and COPD. Distributions of these computed variables, as fed into the predictive models (after transformation for the best results), are presented in Appendix A. Distributions of the untransformed (raw) versions of these variables are shown in Appendix B.

## 3.2. Computational Complexity

In this section, we determine the computational complexity of the proposed data processing approach using the mathematical big O notation. Let f and g be two functions defined on some subset of real numbers. Then, we say $f ( x ) = O ( g ( x ) )$ as $x \to \infty$ if and only if there is a positive constant M such that for all sufficiently large values of $x ,$ the absolute value of $f ( x )$ is smaller than or equal to the absolute value of g(x). That is, $f ( x ) = O ( g ( x ) )$ if and only if there exists a real number M and a real number $x _ { 0 }$ such that $| f ( x ) | \leq M | g ( x )$ | ?????? ?????? $x \ \geq \ x _ { 0 } .$ Clearly, if $f ( x ) = O ( g ( x ) )$ and $g ( x ) \ : = \ : O ( h ( x ) )$ , then $f ( x ) = O ( h ( x ) )$ Therefore, rather than considering every step of the proposed method, we focus our attention to the most complex steps.

The most resource-intensive computations in our proposed approach belong to Eq. 2 through Eq. 5, as for each record in the data, they perform computations on all or on a significant portion of the data set. This is opposed to other equations in which variables from only one or two records are considered in the calculations. Now, let m be the number of unique patients and n be the number of all records in the EMR data. Because some records belong to readmitted patients, we can conclude that $m \ < \ n .$ Furthermore, since the average number of admissions per patient is close to 3 (see Table 1), this average is O(log(n)), which means it is less than or equal to M(log(n)). If we sort the EMR data by patient number and discharge date, the data set would look somewhat like in Figure 1.

For the first visit of the first patient in Eq. 2, the computation requires retrieval of one record from the EMR data; the second visit of the first patients requires two retrievals; and as the data processing proceeds, the $i ^ { t h }$ admission of the first patient requires retrieval of i records from the data set. As a result, the last visit of the first patient, which is the $M / l o g ( n ) J ^ { t h }$ visit, will retrieve M[log(n)] records. Therefore, calculation of avg\_patient\_tslv for each patient in Eq. 2 requires $\scriptstyle \sum _ { i = 1 } ^ { M [ \log ( n ) ] }$ ?? operations on the EMR data. The total time complexity of this equation, therefore, can be obtained from Eq. (14).

∑<sup>??[log(??)]</sup> (??[log(??)])(??[log(??)]+1) = m 2 ????<sup>2</sup>(log[??])<sup>2</sup> = 2 = O((log[n])<sup>2</sup>)

(14)

<table><tr><td>Record Number</td><td>Patient Number</td><td>Variable 1</td><td>Variable 2</td><td>...</td><td>Variable k</td><td>Visit Number</td></tr><tr><td>1</td><td>Patient 1</td><td>...</td><td>...</td><td>...</td><td>...</td><td>1</td></tr><tr><td>2</td><td>Patient 1</td><td>...</td><td>...</td><td>...</td><td>...</td><td>2</td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td>M[log (n)]</td><td>Patient 1</td><td>...</td><td>...</td><td>...</td><td>...</td><td>M[log (n)]</td></tr><tr><td>M[log (n)] + 1</td><td>Patient 2</td><td>...</td><td>...</td><td>...</td><td>...</td><td>1</td></tr><tr><td>M[log (n)] + 2</td><td>Patient 2</td><td>...</td><td>...</td><td>...</td><td>...</td><td>2</td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td>2M[log(n)]</td><td>Patient 2</td><td>...</td><td>...</td><td>...</td><td>...</td><td>M[log (n)]</td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td>n - (M[log(n)] - 1)</td><td>Patient m</td><td>...</td><td>...</td><td>...</td><td>...</td><td>1</td></tr><tr><td>n - (M[log(n)] - 2)</td><td>Patient m</td><td>...</td><td>...</td><td>...</td><td>...</td><td>2</td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td>n - 1</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>M[log (n)] -1</td></tr><tr><td>n</td><td>Patient m</td><td>...</td><td>...</td><td>...</td><td>...</td><td>M[log (n)]</td></tr></table>

Figure 1. A snapshot of the EMR data

To obtain the time complexity of the computation in Eq. 3 we need to pay attention to its difference with the computation performed in Eq. 2. In Eq. 2, we are only interested in prior admissions of a certain patient, whereas in Eq. 3 we want to calculate the average TSLV across all visits by all patients prior to the current record. This means for each record in the EMR data, we need to retrieve a fraction of all the data set, and as the date/time of the admission approaches towards the end of the period represented in the EMR data, this fraction becomes increasingly larger. So, if we sort the data set by the increasing order of discharge date, the procedure represented in Eq. 3 retrieves $^ 1 / _ { n }$ of the data for the first record, ${ } ^ { 2 } / n$ of the data for the second record, and ${ } ^ { n } / n$ or all of the data set for the last record, to calculate the total average TSLV across all admissions that occurred prior to that record. In other words, for the $i ^ { t h }$ record in the sorted data set, Eq. 3 needs to retrieve i records to compute the mean of TSLV. Consequently, time complexity of Eq. 3 can be obtained using the formula given in Eq. 15.

Time complexity of Eq. $\textstyle 3 = \sum _ { i = 1 } ^ { n }$ ??

$$
\begin{array}{l} = (1 + 2 + \dots + n) \\ = (n (n + 1)) \\ = O (n ^ {2}) \end{array}\tag{15}
$$

Due to the similarity of operations in Eq. 2 and Eq. 4, we can conclude that Eq. $4 = \mathrm { O } ( ( \log [ \mathrm { n } ] ) ^ { 2 } )$ . Likewise, Eq. $5 = \mathrm { O } ( \mathrm { n } ^ { 2 } )$ , because of its similarity to Eq. 3. Since $( \log [ \mathsf { n } ] ) ^ { 2 } = \mathbf { O } ( \mathsf { n } ^ { 2 } )$ , our proposed method to process EMR data for improved predictive analytics has a time complexity of $\mathrm { O } ( \mathrm { n } ^ { 2 } )$ , where n is the number of observations in the EMR data. Using a personal computer with a 2.6 GHz Core i7 CPU and 16 GB of RAM, it took the $\mathrm { O } ( \mathrm { n } ^ { 2 } )$ procedures 25:45 and the O(log[n]) procedures 11:16 minutes to complete. Hence, for larger repositories of EMR data with a couple of million records, this method requires the use of big data platforms to obtain the results in a reasonable time. For smaller data sets, however, personal or office computers would perform sufficiently. As we will argue later in the conclusion section, our findings denote that health care organizations with more advanced analytics and big data prowess would have a competitive advantage over others with less developed analytical capabilities.

## 4. The Data

As mentioned earlier, the data we use to evaluate our proposed processing method belong to two chronic conditions with the highest readmission rates. The HF data contains more than 89,500 records from 32,350 unique, anonymized patients who were admitted between January 2001 and December 2015. The

## ACCEPTED MANUSCRIPT

COPD data set includes more than 90,500 records from 31,070 unique, anonymized patients, and contains hospitalizations that occurred within the same period between 2000 and 2015. In preparing the data sets for the study, we included patients with only one admission to calculate the database-level historical variables (i.e., variables represented with odd-numbered equations between Eq. 3 and Eq. 13) for all admissions that succeeded those encounters chronologically. We believe this approach enables the predictive models to make better predictions for new patients in validation sets $( \mathrm { i . e . , }$ patients who do not have any records in the training sets). As explained earlier, values of the response variable are coded depending on whether an index admission would result in a 30-day readmission (response = ‘1’) or not $( \mathrm { r e s p o n s e } = \cdot 0 ^ { , } )$ . Therefore, in both training and validation data sets, the response variable for those records that belong to patients with only one admission is labeled $\mathrm { a s } ^ { \bullet } 0 ^ { \bullet }$ (i.e., the record does not lead to a readmission in the future). Table 1 shows summary statistics of the variables related to patient demographics and hospital region that we use in this study. A summary of the variables created using the Figure 2.

![](/api/attachments/4SUDQFDR/fulltext/images/7c140101143233a66c83fb989b35a34562b800c7f4d036e826518c65fb8e7731.jpg)

![](/api/attachments/4SUDQFDR/fulltext/images/44f8e11f0b16ffa29fd7a9b702b388a489d73ffd6038bbcc78a627e6d88c4cfb.jpg)  
Figure 2. Distributions of the response variables

Table 1. Demographics of the EMR Data

<table><tr><td colspan="2"></td><td>HF</td><td>N. Missing</td><td>COPD</td><td>N. Missing</td></tr><tr><td colspan="2">Number of unique patients</td><td>32,350</td><td></td><td>31,070</td><td></td></tr><tr><td colspan="2">Date of first admission</td><td>10/24/2000</td><td></td><td>10/2/2000</td><td></td></tr><tr><td colspan="2">Date of last admission</td><td>12/27/2015</td><td></td><td>12/28/2015</td><td></td></tr><tr><td colspan="2">Average admissions per patient</td><td>2.77</td><td></td><td>2.91</td><td></td></tr><tr><td rowspan="2">Gender</td><td>Female</td><td>52%</td><td rowspan="2">9</td><td>58%</td><td rowspan="2">11</td></tr><tr><td>Male</td><td>48%</td><td>42%</td></tr><tr><td rowspan="2">Age</td><td>Mean</td><td>71.08</td><td rowspan="2">0</td><td>61</td><td rowspan="2">0</td></tr><tr><td>Std Dev</td><td>12.66</td><td>20.64</td></tr><tr><td rowspan="2">Age (Female)</td><td>Mean</td><td>72.86</td><td rowspan="2">0</td><td>60.6</td><td rowspan="2">0</td></tr><tr><td>Std Dev</td><td>12.47</td><td>20.21</td></tr><tr><td rowspan="2">Age (Male)</td><td>Mean</td><td>69.42</td><td rowspan="2">0</td><td>61.5</td><td rowspan="2">0</td></tr><tr><td>Std Dev</td><td>12.61</td><td>21.2</td></tr><tr><td rowspan="3">Race</td><td>White</td><td>80.90%</td><td rowspan="3">1169</td><td>75.45%</td><td rowspan="3">1041</td></tr><tr><td>Black</td><td>12.40%</td><td>16.40%</td></tr><tr><td>Other</td><td>6.70%</td><td>8.15%</td></tr><tr><td rowspan="4">Hospital&#x27;s Census Region</td><td>Midwest</td><td>2.77%</td><td rowspan="4">0</td><td>3.84%</td><td rowspan="4">0</td></tr><tr><td>Northeast</td><td>62.88%</td><td>75.33%</td></tr><tr><td>South</td><td>33.80%</td><td>20.38%</td></tr><tr><td>West</td><td>0.56%</td><td>0.46%</td></tr></table>

In addition to the variables given in Table 1 and Table 2, the EMR data sets used in this study contain other variables that belong to one of the following categories: patient demographics, encounter, diagnosis, or hospital. Definition and frequencies of these variables are given in Table 3. Such variables accord with those used in other predictive analytics studies on hospital readmissions (e.g., Ayabakan et al., 2016; Bardhan et al., 2015; Cai et al., 2016; Oh et al., 2017), and therefore, are deemed appropriate. It deserves to mention that due to scant variability in some of the hospital-related variables (e.g., acute vs. non-acute status and urban vs. rural status), we did not include them in our analyses.

After describing the variables, we now turn our attention to evaluating the contribution of our proposed processing approach to predicting hospital readmissions using EMR data.

Table 2. Summary Statistic of Created Variables

<table><tr><td>Variable</td><td>Description</td><td>Mean (SD)</td><td>Mean (SD)</td></tr><tr><td>TSLV</td><td>Time since last visit of a patient</td><td>237.3 (433.7)</td><td>295 (487.4)</td></tr><tr><td>Avg_patient_tslv</td><td>Mean TSLV of a patient for visits prior to the current visit</td><td>264.6 (398.5)</td><td>317.2 (443.1)</td></tr><tr><td>Avg_total_tslv</td><td>Mean TSLV for all visits in the EMR data prior to the current visit</td><td>195.6 (79.2)</td><td>230.3 (97.2)</td></tr><tr><td>LOS</td><td>Length of stay in the current visit</td><td>7.44 (8.74)</td><td>6.94 (8.35)</td></tr><tr><td>Avg_patient_los</td><td>Mean LOS of a patient for visits prior to the current visit</td><td>7.33 (7.76)</td><td>6.52 (6.86)</td></tr><tr><td>Avg_total_los</td><td>Mean LOS for all visits in the EMR data prior to the current visit</td><td>7.5 (0.55)</td><td>5.88 (0.13)</td></tr><tr><td>Short_readmission_history</td><td>TSLV / avg_total_tslv</td><td>0.52 (1.34)</td><td>0.60 (1.32)</td></tr><tr><td>Long_readmission_history</td><td>Avg_patient_tslv / avg_total_tslv</td><td>2.99 (1.69)</td><td>0.78 (1.16)</td></tr><tr><td>Short_los_history</td><td>LOS / Avg_total_los</td><td>0.98 (1.16)</td><td>1.19 (1.79)</td></tr><tr><td>Long_los_history</td><td>Avg_patient_los / avg_total_los</td><td>0.97 (1.02)</td><td>1.12 (1.6)</td></tr><tr><td>Short_readmission_index</td><td>See Eq. 10</td><td>0.96 (0.08)</td><td>0.94 (0.12)</td></tr><tr><td>Long_readmission_index</td><td>See Eq. 11</td><td>0.80 (0.11)</td><td>0.93 (0.10)</td></tr><tr><td>Short_los_index</td><td>See Eq. 12</td><td>0.015 (0.017)</td><td>0.008 (0.012)</td></tr><tr><td>Long_los_index</td><td>See Eq. 13</td><td>0.014 (0.015)</td><td>0.007 (0.01)</td></tr></table>

## ACCEPTED MANUSCRIPT

Table 3. EMR Variable Definitions

<table><tr><td rowspan="2">Variable (Average N. Missing)</td><td rowspan="2">Description of variable</td><td rowspan="2">Type</td><td colspan="2">Descriptive statistics</td></tr><tr><td>HF</td><td>COPD</td></tr><tr><td colspan="5">Demographics</td></tr><tr><td>Marital status (8787)</td><td>Patient marital status on the day of discharge</td><td>Nominal</td><td>Married (41%)Widowed (26%)Single (14%)Divorced (8%)Other (11%)</td><td>Married (35%)Widowed (19%)Single (26%)Divorced (10%)Other (10%)</td></tr><tr><td colspan="5">Encounter</td></tr><tr><td>Admission source (0)</td><td>How the patient was referred to the hospital (current admission)</td><td>Nominal</td><td>Emergency room (30%)Physician referral (30%)Transfer (18%)Other (22%)</td><td>Emergency room (32%)Physician referral (42%)Transfer (15%)Other (11%)</td></tr><tr><td>Admission type (0)</td><td>Medical emergency of the admission</td><td>Nominal</td><td>Emergency (58%)Urgent (19%)Elective (9%)Other (14%)</td><td>Emergency (49%)Urgent (13%)Elective (16%)Other (22%)</td></tr><tr><td>Total charges (5135)</td><td>Total charges for the encounter</td><td>Numerical</td><td>$11,488 (mean)</td><td>$11,147 (mean)</td></tr><tr><td>Payer (0)</td><td>How the patient charges will be paid</td><td>Nominal</td><td>Medicare (37%)Medicaid (2.5%)Private/self (12%)Other/missing (58.5%)</td><td>Medicare (20%)Medicaid (3%)Private/self (11%)Other/missing (66%)</td></tr><tr><td>Is readmission (0)</td><td>Whether the current encounter is a readmission</td><td>Binary</td><td>No (86.5%)Yes (13.5%)</td><td>No (86%)Yes (14%)</td></tr><tr><td>First admission (0)</td><td>Whether the current encounter is patient's first admission</td><td>Binary</td><td>No (43%)Yes (57%)</td><td>No (48%)Yes (52%)</td></tr><tr><td>Discharge disposition (0)</td><td>Where the patient was discharged to</td><td>Nominal</td><td>Home (43%)Home with health service (21.5%)Skilled nursing facility (17.5%)Expired (3.5%)Other (14.5%)</td><td>Home (51%)Home with health service (20%)Skilled nursing facility (14%)Expired (2%)Other (13%)</td></tr><tr><td colspan="5">Diagnosis</td></tr><tr><td>Diagnosis code (0)Hospital</td><td>Diagnosis for the encounter (up to 3 diagnoses)</td><td>Nominal</td><td>ICD-9 code</td><td>ICD-9 code</td></tr><tr><td>Bed size range (0)</td><td>Size of the hospital</td><td>Nominal</td><td>6-99 (35%)100-199 (11%)200-299 (19%)500+ (33%)Other (2%)</td><td>6-99 (23%)100-199 (10%)200-299 (30%)500+ (32%)Other (5%)</td></tr><tr><td>Teaching facility (131)</td><td>Whether the hospital is a teaching facility</td><td>Binary</td><td>No (35%)Yes (65%)</td><td>No (24%)Yes (76%)</td></tr></table>

## 5. Analytical Evaluation

To evaluate the contribution of our data processing method to the prediction performance of hospital readmissions, we use temporal validation along with the standard assessment metrics for predictive models. While multiple models have usually been built to find the best performing solution for hospital readmissions, tree-based ensembles have generated acceptable results in both academic and professional experiments (e.g., Futoma, Morris, & Lucas, 2015; Shams, Ajorlou, & Yang, 2015). This is in line with our experience in SAS Enterprise Miner, and as a result, we report the detailed results obtained from the best performing model, which is random forest, along with a summary of the results from other models.

To perform the comparisons, we create two subsets from each data set. The first subset (Original) data processing, and the second subset includes both the original and created variables (Original + Created). We report the results for each “disease – subset” combination by averaging the area under the ROC curve (AUC) and misclassification over 10 randomizations (i.e., different model seeds), in which the preceding 70 percent of the data (in chronological order of admission data/time) is used for model training and the succeeding 30 percent for validation. Table 4 reports the detailed information from each randomization of the random forest model. A summary of the other models is given in Table 5.

Table 4. Validation results from 10 randomizations of random forest for the HF and COPD data

<table><tr><td></td><td> $R_1$ </td><td> $R_2$ </td><td> $R_3$ </td><td> $R_4$ </td><td> $R_5$ </td><td> $R_6$ </td><td> $R_7$ </td><td> $R_8$ </td><td> $R_9$ </td><td> $R_{10}$ </td><td>Mean</td><td>SD</td></tr><tr><td>AUC</td><td>71.3</td><td>71.4</td><td>71.4</td><td>71.4</td><td>71.4</td><td>71.5</td><td>71.4</td><td>71.5</td><td>71.4</td><td>71.5</td><td>71.42</td><td>0.06</td></tr><tr><td>FN</td><td>3605</td><td>3710</td><td>3773</td><td>3743</td><td>3707</td><td>3725</td><td>3696</td><td>3787</td><td>3596</td><td>3713</td><td>3705</td><td>62.57</td></tr><tr><td>TN</td><td>10633</td><td>10764</td><td>10886</td><td>10867</td><td>10815</td><td>10840</td><td>10677</td><td>10867</td><td>10635</td><td>10806</td><td>10779</td><td>97.39</td></tr><tr><td>FP</td><td>4639</td><td>4508</td><td>4386</td><td>4405</td><td>4457</td><td>4432</td><td>4595</td><td>4405</td><td>4637</td><td>4466</td><td>4493</td><td>97.39</td></tr><tr><td>TP</td><td>5633</td><td>5528</td><td>5465</td><td>5495</td><td>5531</td><td>5513</td><td>5542</td><td>5451</td><td>5642</td><td>5525</td><td>5532</td><td>62.57</td></tr><tr><td>MC</td><td>33.63</td><td>33.52</td><td>33.28</td><td>33.24</td><td>33.30</td><td>33.28</td><td>33.82</td><td>33.42</td><td>33.59</td><td>33.37</td><td>33.44</td><td>0.19</td></tr></table>

<table><tr><td></td><td> $R_1$ </td><td> $R_2$ </td><td> $R_3$ </td><td> $R_4$ </td><td> $R_5$ </td><td> $R_6$ </td><td> $R_7$ </td><td> $R_8$ </td><td> $R_9$ </td><td> $R_{10}$ </td><td>Mean</td><td>SD</td></tr><tr><td>AUC</td><td>75</td><td>75.8</td><td>75.6</td><td>75.2</td><td>75.1</td><td>74.9</td><td>75.1</td><td>75.7</td><td>75.1</td><td>74.7</td><td>75.22</td><td>0.36</td></tr><tr><td>FN</td><td>2602</td><td>2761</td><td>2563</td><td>2538</td><td>2533</td><td>2467</td><td>2650</td><td>2657</td><td>2426</td><td>2435</td><td>2563</td><td>107</td></tr><tr><td>TN</td><td>9749</td><td>10296</td><td>9882</td><td>9695</td><td>9771</td><td>9316</td><td>9910</td><td>10049</td><td>9418</td><td>9276</td><td>9736</td><td>325.8</td></tr><tr><td>FP</td><td>5523</td><td>4976</td><td>5390</td><td>5577</td><td>5501</td><td>5956</td><td>5362</td><td>5223</td><td>5854</td><td>5996</td><td>5535</td><td>325.8</td></tr><tr><td>TP</td><td>6636</td><td>6477</td><td>6675</td><td>6700</td><td>6705</td><td>6771</td><td>6588</td><td>6581</td><td>6812</td><td>6803</td><td>6674</td><td>107</td></tr><tr><td>MC</td><td>33.15</td><td>31.56</td><td>32.44</td><td>33.10</td><td>32.77</td><td>34.36</td><td>32.68</td><td>32.15</td><td>33.78</td><td>34.39</td><td>33.03</td><td>0.92</td></tr></table>

<table><tr><td></td><td> $R_1$ </td><td> $R_2$ </td><td> $R_3$ </td><td> $R_4$ </td><td> $R_5$ </td><td> $R_6$ </td><td> $R_7$ </td><td> $R_8$ </td><td> $R_9$ </td><td> $R_{10}$ </td><td>Mean</td><td>SD</td></tr><tr><td>AUC</td><td>62.6</td><td>62.9</td><td>62.8</td><td>62.8</td><td>62.7</td><td>62.9</td><td>62.8</td><td>62.7</td><td>63</td><td>62.7</td><td>62.79</td><td>0.12</td></tr><tr><td>FN</td><td>6616</td><td>6580</td><td>6759</td><td>6663</td><td>6545</td><td>6632</td><td>6715</td><td>6620</td><td>6610</td><td>6682</td><td>6642</td><td>63.76</td></tr><tr><td>TN</td><td>8600</td><td>8653</td><td>8734</td><td>8642</td><td>8530</td><td>8630</td><td>8668</td><td>8647</td><td>8662</td><td>8629</td><td>8639</td><td>51.90</td></tr><tr><td>FP</td><td>4815</td><td>4762</td><td>4681</td><td>4773</td><td>4885</td><td>4785</td><td>4747</td><td>4768</td><td>4753</td><td>4786</td><td>4775</td><td>51.90</td></tr><tr><td>TP</td><td>7252</td><td>7288</td><td>7109</td><td>7280</td><td>7323</td><td>7236</td><td>7153</td><td>7248</td><td>7258</td><td>7186</td><td>7233</td><td>65.43</td></tr><tr><td>MC</td><td>41.89</td><td>41.57</td><td>41.93</td><td>41.91</td><td>41.89</td><td>41.84</td><td>42.01</td><td>41.74</td><td>41.64</td><td>42.03</td><td>41.84</td><td>0.15</td></tr></table>

<table><tr><td></td><td> $R_1$ </td><td> $R_2$ </td><td> $R_3$ </td><td> $R_4$ </td><td> $R_5$ </td><td> $R_6$ </td><td> $R_7$ </td><td> $R_8$ </td><td> $R_9$ </td><td> $R_{10}$ </td><td>Mean</td><td>SD</td></tr><tr><td>AUC</td><td>75.4</td><td>75.5</td><td>75.2</td><td>75.5</td><td>75.6</td><td>75.5</td><td>75.5</td><td>75.6</td><td>74.7</td><td>75.6</td><td>75.41</td><td>0.27</td></tr><tr><td>FN</td><td>4782</td><td>4577</td><td>4686</td><td>4654</td><td>4634</td><td>4676</td><td>4682</td><td>4641</td><td>4642</td><td>4623</td><td>4659</td><td>53.70</td></tr><tr><td>TN</td><td>9627</td><td>9426</td><td>9385</td><td>9561</td><td>9530</td><td>9572</td><td>9512</td><td>9584</td><td>9337</td><td>9497</td><td>9503</td><td>93.28</td></tr><tr><td>FP</td><td>3788</td><td>3989</td><td>4030</td><td>3854</td><td>3885</td><td>3843</td><td>3903</td><td>3831</td><td>4078</td><td>3198</td><td>3840</td><td>244.1</td></tr><tr><td>TP</td><td>9086</td><td>9291</td><td>9182</td><td>9214</td><td>9234</td><td>9192</td><td>9186</td><td>9227</td><td>9226</td><td>9245</td><td>9208</td><td>53.70</td></tr><tr><td>MC</td><td>31.41</td><td>31.39</td><td>31.94</td><td>31.18</td><td>31.22</td><td>31.22</td><td>31.46</td><td>31.05</td><td>31.96</td><td>31.30</td><td>31.41</td><td>0.30</td></tr></table>

R: randomization; FN: False Negative; TN: True Negative; FP: False Positive; TP: True Positive; MC: Misclassification Rate

Table 5. Average AUCs obtained from other models

<table><tr><td>Model</td><td>HF (1)</td><td>HF (2)</td><td>COPD (1)</td><td>COPD (2)</td></tr><tr><td>Bayesian Network</td><td>0.705</td><td>0.733</td><td>0.619</td><td>0.743</td></tr><tr><td>Neural Network</td><td>0.707</td><td>0.728</td><td>0.611</td><td>0.748</td></tr><tr><td>Gradient Boosting</td><td>0.658</td><td>0.722</td><td>0.581</td><td>0.723</td></tr></table>

As it can be seen in Tables 4 and 5, the addition of the calculated variables to the EMR data consistently improves the performance of the predictive models for hospital readmission. Therefore, to keep the discussions concise in the rest of the paper, we focus our attention on the results obtained from the best performing model (i.e., random forest). For the HF data sets, the AUC has risen from an average 71.42 for the original variables to an average 74.22 for the original and created variables. The increase in AUC is even larger for the COPD data sets, where it has increased from 62.79 for the original variables to 75.41 for the combination of the original and calculated variables. To verify that the increases in AUCs are significant, we perform two paired t-tests over the 10 randomizations of the random forest models we built for the HF and COPD data sets. The results of the t-tests (Table 6) confirm the contribution of our data processing approach to the prediction of hospital readmissions for HF and COPD.

Table 6. Two-sample t-tests (unequal variances) for the difference between the average AUCs

<table><tr><td>Data</td><td>t -Test Condition</td><td>Mean</td><td colspan="2">95% CL Mean</td><td>DF</td><td>t-Value</td><td>Pr &gt; |t|</td></tr><tr><td>HF</td><td> $AUC_{(Original + Created)} - AUC_{Original}$ </td><td>3.80</td><td>3.53</td><td>4.06</td><td>9</td><td>30.24</td><td>&lt; .0001</td></tr><tr><td>COPD</td><td> $AUC_{(Original + Created)} - AUC_{Original}$ </td><td>12.62</td><td>12.36</td><td>12.87</td><td>9</td><td>109.4</td><td>&lt;.0001</td></tr></table>

A closer examination of the values given in Table 4 reveals two additional contributions of our data processing approach. First, besides AUC, other model evaluation metrics have also improved with the inclusion of the calculated variables. For instance, misclassification rates have, on average, declined by 0.41 and 10.43 percent for the HF and COPD data, respectively. As it can be seen, this decline is substantial for models built on the COPD data. Similarly, the number of correct classifications (i.e., the true positive and true negative rates) have generally increased, and the number of wrong classifications (i.e., false positive and false negative rates) have generally decreased in the COPD models after the inclusion of the created variables. However, for the HF data sets, while sensitivity (i.e., a model’s ability in predicting the positive outcome) has increased, specificity (i.e., a model’s ability in predicting the negative outcome) has decreased. Since in this context the identification of patients who are at risk of readmission is more important than predicting who is not prone to such a risk, the addition of the calculated variables provides a useful improvement in prediction results.

Although the information provided in Table 4 and Table 5 confirm that predicting hospital readmissions can be improved with comprehensive data processing and aggregation, this information does not identify the most important contributors. To find out which variables, especially among the calculated ones, drive the enhanced predictions, we follow (Delen, Walker, & Kadam, 2005) to perform sensitivity analysis on the various “disease – subset” models built previously (see Table 4). In this approach, we assign an importance score to each variable based on how much the models’ average performances (i.e., AUC) suffer once that variable is removed from the list of inputs. The variable with the greatest effect gets a score of 1.00 and other variables are scored in regards to their contribution to the model performance relative to that of the most important variable. A list of the important variables for these models is given in Table 7.

A simple comparison between the list of the created variables (Table 2) and the important variables (Table 7) determines that most of the created variables (shown in bold), directly or indirectly, contribute to the improved performance of the predictive models. In particular, some of these variables belong to patient-level aggregations (e.g., Avg\_patient\_los and Avg\_patient\_tslv) and others belong to aggregations at the data set level (e.g., long\_los\_history, short\_readmission\_history, long\_readmission\_history, short\_los\_index, and long\_los\_history, short\_readmission\_index). According to these results, data-set-level aggregations, which allow the information available from each patient to be compared to the history of other patients who were previously admitted for similar complications, provide valuable information to classification models for hospital readmissions. Additionally, as it can be seen in Table 7, the inclusion of the calculated variables not only affects the contribution of the original EMR variables, but also changes the order in which they appear in the list. For instance, while total charges of a hospital visit appears as one of the influential factors in identifying high-risk patients in the EMR-based HF models, it loses its predictive importance once the created variables are added to the classification models. This means patients’ history of hospital visits, which as mentioned earlier, can be used as an indicator of their overall health, can potentially have more predictive power for readmissions than some of the demographic or encounter variables. Similarly, age of a patient is not the most valuable predictor of readmission among COPD patients once the calculated variables are added to the data sets (it becomes the 16<sup>th</sup> important variable after the calculated variables are added to the model).

Table 7. Important variables in each “disease – subset” model

<table><tr><td>HF (Original)</td><td>Value</td><td>HF (Original + Created)</td><td>Value</td></tr><tr><td>Discharge disposition</td><td>1.00</td><td>Discharge disposition</td><td>1.00</td></tr><tr><td>Admission source</td><td>0.54</td><td>Admission type</td><td>0.49</td></tr><tr><td>Age</td><td>0.44</td><td>Admission Source</td><td>0.44</td></tr><tr><td>Payer</td><td>0.33</td><td>Age</td><td>0.26</td></tr><tr><td>Total charges</td><td>0.17</td><td>Short LOS history</td><td>0.24</td></tr><tr><td>Census region</td><td>0.07</td><td>Short LOS index</td><td>0.21</td></tr><tr><td>Bed size range</td><td>0.06</td><td>Payer</td><td>0.20</td></tr><tr><td>Census Division</td><td>0.05</td><td>Avg. patient TSLV</td><td>0.19</td></tr><tr><td>Marital status</td><td>0.04</td><td>LOS</td><td>0.18</td></tr><tr><td>Teaching facility</td><td>0.02</td><td>Short readmission history</td><td>0.15</td></tr><tr><td></td><td></td><td>Long readmission history</td><td>0.14</td></tr><tr><td>COPD (Original)</td><td>Value</td><td>COPD(Original + Created)</td><td>Value</td></tr><tr><td>Age</td><td>1.00</td><td>Long readmission index</td><td>1.00</td></tr><tr><td>Diagnosis</td><td>0.84</td><td>Short readmission index</td><td>0.98</td></tr><tr><td>Marital status</td><td>0.79</td><td>Long readmission history(imputed)</td><td>0.78</td></tr><tr><td>Discharge disposition</td><td>0.72</td><td>Avg. patient LOS</td><td>0.70</td></tr><tr><td>Bed size range</td><td>0.61</td><td>LOS</td><td>0.54</td></tr><tr><td>Payer</td><td>0.56</td><td>Short LOS history</td><td>0.47</td></tr><tr><td>Admission source</td><td>0.46</td><td>First admission</td><td>0.45</td></tr><tr><td>Race</td><td>0.35</td><td>Long LOS history</td><td>0.44</td></tr><tr><td>Total charges</td><td>0.35</td><td>Long LOS index</td><td>0.32</td></tr><tr><td>Gender</td><td>0.25</td><td>Payer</td><td>0.29</td></tr><tr><td></td><td></td><td>Avg. patient TSLV</td><td>0.28</td></tr></table>

From the results shown in Table 7 we can also notice the difference in the list of significant variables between the two diseases. This suggests that predictions may be improved through the consideration of idiosyncrasies of each disease and reflecting those peculiarities in processing the EMR be the main drivers of enhanced performance in HF models, COPD models are boosted mainly by the variables related to TSLV. Likewise, after the addition of the new variables, prediction of readmission among COPD patients is mainly driven by the calculated variables, whereas in HF models, encounter and demographic variables hold their importance. As a result, and regarding that the improvement of prediction performance was greater for the COPD models, more emphasis may be exerted on quality assurance and comprehensive processing of EMR data for COPD patients.

Finally, it deserves to point out that with the addition of the variables that extract patients’ history of hospital visits, our models outperform most retrospective studies that predict 30-day readmissions for patients with HF and COPD. A summary of the result of previous studies is presented in Table 8.

Table 8. Summary of previous retrospective models for HF or COPD (30-day readmission)

<table><tr><td>Study</td><td>N</td><td>Disease</td><td>AUC</td><td>Model</td></tr><tr><td>Amarasingham et al. (2010)</td><td>1,372</td><td>HF</td><td>0.72</td><td>Logistic Regression</td></tr><tr><td>Amarasingham et al. (2015)</td><td>39,604</td><td>Multiple</td><td>0.68</td><td>Logistic Regression</td></tr><tr><td>Bardhan et al. (2015)</td><td>65,188</td><td>HF</td><td>0.601</td><td>Beta Geometric Erlang 2</td></tr><tr><td rowspan="2">Futoma et al. (2015)</td><td>25,941</td><td>HF</td><td>0.676</td><td rowspan="2">Deep neural Networks</td></tr><tr><td>31,457</td><td>COPD</td><td>0.711</td></tr><tr><td>Garrison et al. (2016)</td><td>26,279</td><td>Multiple</td><td>0.666</td><td>Logistic Regression</td></tr><tr><td>Hebert et al. (2014)</td><td>3,572</td><td>HF</td><td>0.64</td><td>Logistic Regression</td></tr><tr><td>Kansagara et al. (2011)</td><td>14 studies</td><td>HF</td><td>0.65</td><td>Various</td></tr><tr><td rowspan="2">Turgeman &amp; May (2016)</td><td>20,321</td><td>HF</td><td>0.693</td><td rowspan="2">Ensemble (C5 + SVM)</td></tr><tr><td>142,527</td><td>HF</td><td>0.663</td></tr><tr><td>Yang et al. (2016)</td><td>142,527</td><td>HF</td><td>0.663</td><td>Gradient Boosting</td></tr></table>

## ACCEPTED MANUSCRIPT

<table><tr><td></td><td>107,228</td><td>COPD</td><td>0.706</td><td></td></tr><tr><td rowspan="2">Current study</td><td>89,500</td><td>HF</td><td>0.752</td><td rowspan="2">Random Forest</td></tr><tr><td>90,500</td><td>COPD</td><td>0.754</td></tr></table>

## 6. Discussion

The recent reductions in inpatient prospective reimbursements for hospitals whose readmissions for a set of applicable chronic conditions are above the national average has created a lot of interest in hospital readmissions. As a result, the health care delivery system has initiated an endeavor to identify high-risk patients, and thereby, reduce readmissions. While improving patient education, quality of care, discharge planning, post-discharge follow-up, and/or coordination in care transitions have been found to be helpful (Bradley et al., 2012), data analytics has also shown some promise. As we pointed out earlier in the paper, previous analytic studies have tried to improve the prediction of hospital readmissions by either developing more sophisticated models or combining various data sets. Our focus, however, is on performing thorough data processing to extract historical patient- and database-level information to improve readmission analytics.

We created several variables that extract from the EMR data information about patients’ previous visits and compare each patient’s history of hospital visits with other patients who were admitted earlier. Our results show that the nto the predictive models. Consequently, there are several lessons to be learned from our experiment, as we discuss next.

An important takeaway from our study is a reiteration of the importance of data preparation in from more advanced models or combined data sets. Instead, optimal results can be obtained by collecting and aggregating various data sets, using better models, and performing appropriate data processing. Additionally, our findings suggest that information sharing among affiliated hospitals should be encouraged so that more historical medical records (especially from the recent years) can be easily traced and augmented for better prediction results. Regarding the size of electronic medical records and the sophistication of aggregating and processing such data, another implication of our study may be the underlining of the urgency for hospital systems to invest in their analytical capabilities so that they can make more data-driven decisions on various aspects of providing health care services to their patients. For instance, once they have identified patients that are at a higher risk of readmission, they can use the data they have to prescribe the best course of action for each patient (e.g., whether they should discharge a patient to partner care providers, such as nursing homes). Making such data-driven decisions not only improves the health care outcomes, but also can save hospitals a significant amount of money by lowering their average readmission rates, and thereby, avoiding the reimbursement penalties. Finally, the list of the important variables in Table 7 can be used to ensure the quality of data collected by, or shared among, the hospitals.

## 7. Conclusion

Hospital readmissions are costly for governments, insurance companies, and patients. A portion of these readmissions, however, are avoidable through customized care or care transition interventions (Kansagara et al., 2011; van Walraven et al., 2013). While several studies have addressed this issue through predictive analytics approaches, they have not conducted database-wide data processing, prior to building the models, to improve the performance of the resulting analytical solutions. Most studies instead, have focused on developing new predictive models or on assembling richer data by combining various variables from different sources. In this study, we addressed this gap by illustrating how readmission analytics can benefit from extracting historical information, both at the patient and the database level, from the EMR data.

Our data preparation method offers several strategic values to organizations that are involved with reducing the preventable hospital readmissions. First, it underlines the significance of considering historical data when building predictive models for hospital readmissions. Specifically, it illustrates how each record in a large database of medical encounters can be augmented through comparing the hospitalization history of that patient with that of all other patients admitted previously. Second, it pinpoints important historical information for various conditions. For instance, as explained in Section 5, by extracting historical information from the EMR data, more can be learned about the value of LOS, TSLV, or perhaps other historical parameters, to improved prediction of readmissions for different diseases. And third, it demonstrates why health care organization with advanced analytical or big data capabilities could outperform others with less prowess in such domains. As we pointed out in Section 3.2, the computational requirements of extracting historical information from larger medical databases could become too prohibitive for laggard organizations in terms of analytical capabilities. On the other hand, organizations in which the use of big data analytics has been institutionalized can benefit largely from processing their warehouses for historical information.

This study is not without limitations. For one thing, it could generate better insights if a larger database of EMR is used in the proposed data processing approach. Another limitation of our study is the lack of access to patients’ comorbid conditions. As previous studies have found (Bardhan et al., 2011; Piri, Delen, Liu, & Zolbanin, 2017; Zolbanin, Delen, & Hassan Zadeh, 2015), the inclusion of comorbid diseases can improve the performance of prediction models. Therefore, we surmise that predicting hospital readmissions can become more accurate with the addition of patients’ comorbidities. Similarly, our data did not contain some potentially useful variables that have been shown to improve the results. For example, information on laboratory procedures or patients’ life styles / habits (e.g., sedentary versus active life style, drug use, or alcohol consumption) were not included in our data. Finally, while the computational complexity of the methodology we used might seem too much for EMR data, which normally consist of millions of records, the data processing need not to be applied on all the data set. In the absences of powerful computational capabilities, health care organizations can divide their data into smaller, more manageable segments. For instance, rather than using all the data, they can limit the extraction of historical data to a shorter period, such as three to five years. Our experiments with 20 percent of the data we used above suggests that while the use of smaller data to extract patients’ history still improves the performance of predictive models in contrast to the sheer use of original EMR variables, the difference in performance with the full data set is within 0.9 percent. As another alternative, organizations can use a moving window of three to five years to extract information on patients’ previous visits, rather than considering all prior EMR data. It deserves to mention that such computational complexities are too much only for personal computers, not for big data platforms; and this further underlines the importance of the big data technology for decision-making in the health care industry.

There are several avenues for future research on the extraction of historical data from large EMR data warehouses. A first direction is finding out whether additional variables can be created by sifting through historical hospitalizations for similar conditions. We surmise there are other dimensions that can potentially provide informative variables for predictive models, such as the length of time a patient suffered from comorbid conditions or used certain medications. Researchers can also focus their efforts on finding out whether all historical data should be considered in such data processing endeavors or there is an optimal window for the consideration of historical data, and whether this is different for various diseases. Finally, improving the time complexity of our proposed method can be another area of interest for future explorations.

## Acknowledgement

This study was conducted with the data provided by, and the support from, the Center for Health Systems Innovation (CHSI) at Oklahoma State University (OSU) and the Cerner Corporation. The contents of this of the authors and do not necessarily represent the official views of CHSI, OSU or the Cerner Corporation.

## Appendix A. Distribution of created variables (after transformation)

![](/api/attachments/4SUDQFDR/fulltext/images/cd8ee332a40720e3788723988903558eb1ea2f3c28ea35585b5a22fcaad87716.jpg)  
Transformed Short Readmission History

![](/api/attachments/4SUDQFDR/fulltext/images/7b7803f53faa052d5478dab4c5373439f91e3fd8e94944bfb95a514da46bcf1d.jpg)

![](/api/attachments/4SUDQFDR/fulltext/images/e59c7cdc8ff806036e688800ff2aff54bba7ce74a79e07ea2e7d7f3c482bfb17.jpg)

Transformed Long Readmission History  
![](/api/attachments/4SUDQFDR/fulltext/images/ee623629c992cb64c3a66067949f780aa15bf1e3a2fb5eae2d7d79842e1da050.jpg)

Transformed Short LOS History  
![](/api/attachments/4SUDQFDR/fulltext/images/4b8070be0d1d48de4eecefec3da9c25fea4ef1d7d334438319cb56031d19c95a.jpg)

Transformed Long LOS History  
![](/api/attachments/4SUDQFDR/fulltext/images/080aad457a97340e6d16d1f27eaa6217e4374e468aecf261fe4b3eb1ac97e36a.jpg)

## ACCEPTED MANUSCRIPT

![](/api/attachments/4SUDQFDR/fulltext/images/1ad226b59dd9348f490b58548ddee8e45cdce3da78febd34cd0e216e899ab0c8.jpg)

![](/api/attachments/4SUDQFDR/fulltext/images/f9f140b72bffd65a4de72127b6449544fda24ac4cd44eaa30fa652998eb57e1d.jpg)

Percentage  
![](/api/attachments/4SUDQFDR/fulltext/images/1aca8ad7a5b1faacf188cbfd4b1170867d5689f5fa87311193cec09b310e9ec7.jpg)

![](/api/attachments/4SUDQFDR/fulltext/images/c97ed70cbeab9124632496444b88b33479510cabfce82813dd62f8c428d79714.jpg)

Transformed Avg Patient Readmission  
![](/api/attachments/4SUDQFDR/fulltext/images/625d2eafcd2c6be315bd6375bc1ccf4f15275c60cb68fe7836e8cbbb93579d5f.jpg)

Transformed Avg Patient LOS  
![](/api/attachments/4SUDQFDR/fulltext/images/800b74dcd01446bcbc539ff188eab3bcca0c13b1234985a46835290e95e0cd89.jpg)

## Appendix B. Distribution of raw (untransformed) variables

![](/api/attachments/4SUDQFDR/fulltext/images/58ebd9794dd0b078f3b08674d3f384213048c5e972040fb28cab961bb69d845a.jpg)

![](/api/attachments/4SUDQFDR/fulltext/images/6f0f9399f429c99a155267978fd29505d0779ab4d048bb735490e812030f6250.jpg)

![](/api/attachments/4SUDQFDR/fulltext/images/d22f6768016b6f1e86494ef7838d9773cd8560281241e6c18c84794f8c405c2e.jpg)

![](/api/attachments/4SUDQFDR/fulltext/images/4a002a5994b70937cd13473eeb416daa4aa7be3282938c21ca27c5ebdfe74bf6.jpg)

![](/api/attachments/4SUDQFDR/fulltext/images/b294c71f4030e8bc7ff68264d11ea325a2903bc5e0cf91fd5799b92e84f08bd4.jpg)

![](/api/attachments/4SUDQFDR/fulltext/images/d82b6b08518912c31549e314c7c09131a4a909085a8de019f8e37e6b8291fd44.jpg)

## References

Amarasingham, R., Moore, B. J., Tabak, Y. P., Drazner, M. H., Clark, C. A., Zhang, S., … Halm, E. A. (2010). An Automated Model to Identify Heart Failure Patients at Risk for 30-Day Readmission or Death Using Electronic Medical Record Data. Medical Care, 48(11), 981–988. https://doi.org/10.1097/MLR.0b013e3181ef60d9

Amarasingham, R., Velasco, F., Xie, B., Clark, C., Ma, Y., Zhang, S., … Halm, E. A. (2015). Electronic medical record-based multicondition models to predict the risk of 30 day readmission or death among adult medicine patients: validation and comparison to existing models. BMC Medical Informatics and Decision Making, 15, 39. https://doi.org/10.1186/s12911-015-0162-6

Ayabakan, S., Bardhan, I., & Zheng, E. (2016). What Drives Readmission ? A New Perspective from Hidden Markov Model Analysis. ICIS 2016 Proceedings, 1–19. Retrieved from http://aisel.aisnet.org/cgi/viewcontent.cgi?article=1326&context=icis2016

Baesens, B. (2014). Analytics in a big data world : the essential guide to data science and its applications. Hoboken, NJ: John Wiley & Sons, Inc. https://doi.org/10.1017/CBO9781107415324.004

Baesens, B., Bapna, R., Marsden, J. R., Vanthienen, J., & Zhao, J. L. (2016). Transformational Issues of Big Data and Analytics in Networked Business. MIS Quarterly, 40(4), 807–818. https://doi.org/10.5121/ijgca.2012.3203

Bardhan, I., Oh, J. (Cath), Zheng, Z. (Eric), & Kirksey, K. (2015). Predictive Analytics for Readmission of Patients with Congestive Heart Failure. Information Systems Research, 26(1), 19–39. https://doi.org/10.1287/isre.2014.0553

Bardhan, I., Oh, J., Zheng, Z., & Kirksey, K. (2011). A PROFILING MODEL FOR READMISSION OF PATIENTS WITH CONGESTIVE HEART FAILURE: A MULTI-HOSPITAL STUDY. Retrieved from https://pdfs.semanticscholar.org/7f01/6b177302826137d1333f101430079a6b096a.pdf

Ben-Assuli, O., Padman, R., Leshno, M., & Shabtai, I. (2016). Analyzing Hospital Readmissions Using Creatinine Results for Patients with Many Visits. Procedia Computer Science, 58, 357–361. https://doi.org/10.1016/j.procs.2016.09.054

Bradley, E., Curry, L., Horwitz, L., Simpsma, H., Thompson, J., Elma, M., … Krumholz, H. (2012). Contemporary evidence about hospital strategies for reducing 30-day readmissions: a national study. Journal of the American College of Cardiology, 60(7), 607–614. Retrieved from https://scihub.tw/https://www.sciencedirect.com/science/article/pii/S0735109712018232

Bueno, H., Ross, J. S., Wang, Y., Chen, J., Vidán, M. T., Normand, S.-L. T., … Krumholz, H. M. (2010). Trends in length of stay and short-term outcomes among Medicare patients hospitalized for heart failure, 1993-2006. JAMA, 303(21), 2141–7. https://doi.org/10.1001/jama.2010.748

Cai, X., Perez-Concha, O., Coiera, E., Martin-Sanchez, F., Day, R., Roffe, D., & Gallego, B. (2016). Real-time prediction of mortality, readmission, and length of stay using electronic health record data. Journal of the American Medical Informatics Association, 23(3), 553–561. https://doi.org/10.1093/jamia/ocv110

Center for Healthcare Quality & Payment Reform. (2013). Center for Healthcare Quality and Payment

## ACCEPTED MANUSCRIPT

Reform. Retrieved September 22, 2017, from http://www.chqpr.org/readmissions.html

Chae, Y. M., Yoo, K. B., Kim, E. S., & Chae, H. (2011). The adoption of electronic medical records and decision support systems in Korea. Healthcare Informatics Research, 17(3), 172–7. https://doi.org/10.4258/hir.2011.17.3.172

Chawla, N. V, Bowyer, K. W., Hall, L. O., & Kegelmeyer, W. P. (2002). SMOTE: Synthetic Minority Over-sampling Technique. Journal of Artificial Intelligence Research, 16, 321–357. Retrieved from https://www.jair.org/media/953/live-953-2037-jair.pdf

Colleen K. McIlvennan, Zubin J. Eapen, Larry A. Allen. (2012). Hospital Readmissions Reduction Program. Circulation, 131(20), 1796–1803. https://doi.org/10.1161/CIRCULATIONAHA.114.010270.Hospital

Delen, D., Walker, G., & Kadam, A. (2005). Predicting breast cancer survivability: a comparison of three data mining methods. Artificial Intelligence in Medicine, 34(2), 113–127. https://doi.org/10.1016/j.artmed.2004.07.002

Futoma, J., Morris, J., & Lucas, J. (2015). A comparison of models for predicting early hospital readmissions. Journal of Biomedical Informatics, 56, 229–238. https://doi.org/10.1016/J.JBI.2015.05.016

Garrison, G. M., Robelia, P. M., Pecina, J. L., & Dawson, N. L. (2016). Comparing performance of 30- day readmission risk classifiers among hospitalized primary care patients. Journal of Evaluation in Clinical Practice, 23(3), 524–529. https://doi.org/10.1111/jep.12656

He, D., Mathews, S. C., Kalloo, A. N., & Hutfless, S. (2014). Mining high-dimensional administrative claims data to predict early hospital readmissions. Journal of the American Medical Informatics Association, 21(2), 272–279. https://doi.org/10.1136/amiajnl-2013-002151

Hebert, C., Shivade, C., Foraker, R., Wasserman, J., Roth, C., Mekhjian, H., … Embi, P. (2014). Diagnosis-specific readmission risk prediction using electronic health data: a retrospective cohort study. BMC Medical Informatics and Decision Making, 14(1), 65. https://doi.org/10.1186/1472- 6947-14-65

Herland, M., Khoshgoftaar, T. M., & Wald, R. (2014). A review of data mining using big data in health informatics. Journal Of Big Data, 1(1), 2. https://doi.org/10.1186/2196-1115-1-2

Inouye, S., Bouras, V., Shouldis, E., Johnstone, A., Silverzweig, Z., & Kosuri, P. (2015). Predicting readmission of heart failure patients using automated follow-up calls. BMC Medical Informatics and Decision Making, 15, 22. https://doi.org/10.1186/s12911-015-0144-8

Jagadish, H. V., Gehrke, J., Labrinidis, A., Papakonstantinou, Y., Patel, J. M., Ramakrishnan, R., & Shahabi, C. (2014). Big data and its technical challenges. Communications of the ACM, 57(7), 86– 94. https://doi.org/10.1145/2611567

Jencks, S. F., Williams, M. V., & Coleman, E. A. (2009). Rehospitalizations among Patients in the Medicare Fee-for-Service Program. New England Journal of Medicine, 360(14), 1418–1428. https://doi.org/10.1056/NEJMsa0803563

Jovanovic, M., Radovanovic, S., Vukicevic, M., Van Poucke, S., & Delibasic, B. (2016). Building interpretable predictive models for pediatric hospital readmission using Tree-Lasso logistic regression. Artificial Intelligence in Medicine, 72, 12–21. https://doi.org/10.1016/j.artmed.2016.07.003

Kansagara, D., Englander, H., Salanitro, A., Kagen, D., Theobald, C., Freeman, M., & Kripalani, S. (2011). Risk Prediction Models for Hospital Readmission. JAMA, 306(15), 1688. https://doi.org/10.1001/jama.2011.1515

Kauffman, B. (2016). Readmissions & Medicare: What’s the Cost? - National Investment Center. Retrieved September 22, 2017, from http://www.nic.org/blog/readmissions-medicare-whats-thecost/

Kohli, R., & Tan, S. S.-L. (2016). Electronic Health Records: How can IS Researchers Contribute to Transforming Healthcare? MIS Quarterly, 40(3), 553–573. https://doi.org/10.1016/j.soncn.2011.04.007

Lin, Y.-K., Chen, H., Brown, R. A., Li, S.-H., & Yang, H.-J. (2017). HEALTHCARE PREDICTIVE ANALYTICS FOR RISK PROFILING IN CHRONIC CARE: A BAYESIAN MULTITASK LEARNING APPROACH 1. MIS Quarterly, 41(2), 473–495. Retrieved from http://aisel.aisnet.org/cgi/viewcontent.cgi?article=3355&context=misq

Martens, D., Provost, F., Clark, J., & Junqué De Fortuny, E. (2016). BIG DATA &amp; ANALYTICS IN NETWORKED BUSINESS MINING MASSIVE FINE-GRAINED BEHAVIOR DATA TO IMPROVE PREDICTIVE ANALYTICS 1. MIS Quarterly, 40(4), 869–888. Retrieved from http://pages.stern.nyu.edu/\~fprovost/Papers/MartensProvost2016.pdf

Mesgarpour, M., Chaussalet, T., & Chahed, S. (2017). Ensemble Risk Model of Emergency Admissions (ERMER). International Journal of Medical Informatics, 103, 65–77. https://doi.org/10.1016/j.ijmedinf.2017.04.010

Nowiński, A., Kamiński, D., Korzybski, D., Stokłosa, A., & Górecka, D. (2011). [The impact of comorbidities on the length of hospital treatment in patients with chronic obstructive pulmonary disease]. Pneumonologia I Alergologia Polska, 79(6), 388–96. Retrieved from http://www.ncbi.nlm.nih.gov/pubmed/22028117

Oh, J. C., Zheng, Z. E., & Bardhan, I. R. (2017). Sooner or Later? Health Information Technology, Length of Stay, and Readmission Risk. Production and Operations Management. https://doi.org/10.1111/poms.12748

Piri, S., Delen, D., Liu, T., & Zolbanin, H. M. (2017). A data analytics approach to building a clinical decision support system for diabetic retinopathy: Developing and deploying a model ensemble. Decision Support Systems, 101, 12–27. https://doi.org/10.1016/J.DSS.2017.05.012

Shams, I., Ajorlou, S., & Yang, K. (2015). A predictive analytics approach to reducing 30-day avoidable readmissions among patients with heart failure, acute myocardial infarction, pneumonia, or COPD. Health Care Management Science. https://doi.org/http://dx.doi.org/10.1007/s10729-014-9278-y

Shmueli, G., & Koppius, O. R. (2011). Predictive Analytics in Information Systems Research. MIS Quarterly. Management Information Systems Research Center, University of Minnesota. https://doi.org/10.2307/23042796

## ACCEPTED MANUSCRIPT

Tsui, E., Au, S., Wong, C., Cheung, A., & Lam, P. (2015). Development of an automated model to predict the risk of elderly emergency medical admissions within a month following an index hospital visit: A Hong Kong experience. Health Informatics Journal, 21(1), 46–56. https://doi.org/10.1177/1460458213501095

Turgeman, L., & May, J. H. (2016). A mixed-ensemble model for hospital readmission. Artificial Intelligence in Medicine, 72, 72–82. https://doi.org/10.1016/j.artmed.2016.08.005

van Walraven, C., Wong, J., Forster, A. J., & Hawken, S. (2013). Predicting post-discharge death or readmission: deterioration of model performance in population having multiple admissions per patient. Journal of Evaluation in Clinical Practice, 19(6), 1012–1018. https://doi.org/10.1111/jep.12012

Veloso, R., Portela, F., Santos, M. F., Silva, Á., Rua, F., Abelha, A., & Machado, J. (2014). A Clustering Approach for Predicting Readmissions in Intensive Medicine. Procedia Technology, 16, 1307–1316. https://doi.org/10.1016/j.protcy.2014.10.147

Walsh, C., & Hripcsak, G. (2014). The effects of data sources, cohort selection, and outcome definition on a predictive model of risk of thirty-day hospital readmissions. Journal of Biomedical Informatics, 52, 418–426. https://doi.org/10.1016/j.jbi.2014.08.006

Wang, H., Johnson, C., Robinson, R. D., Nejtek, V. A., Schrader, C. D., Leuck, J., … Zenarosa, N. R. (2016). Roles of disease severity and post-discharge outpatient visits as predictors of hospital readmissions. BMC Health Services Research, 16(1), 564. https://doi.org/10.1186/s12913-016-1814- 7

Yang, C., Delcher, C., Shenkman, E., & Ranka, S. (2016). Predicting 30-Day All-Cause Readmissions from Hospital Inpatient Discharge Data. In 18th International Conference on E-health Networking, Application & Services (HealthCom). IEEE. Retrieved from https://www.cise.ufl.edu/\~cy2/pdf/PID4420953.pdf

Zolbanin, H. M., Delen, D., & Hassan Zadeh, A. (2015). Predicting overall survivability in comorbidity of cancers: A data mining approach. Decision Support Systems, 74, 150–161. https://doi.org/10.1016/j.dss.2015.04.003

## Author Biographical Sketches

![](/api/attachments/4SUDQFDR/fulltext/images/79638f89436f3786911c460217fcfff14fe695ffc9535eccb9e2e5a592adb9e8.jpg)

Dr. Hamed M. Zolbanin is an assistant professor of information systems and the director of business analytics in Miller College of Business at Ball State University. He had several years of professional experience as an IT engineer prior to receiving his Ph.D. in Management Science and Information Systems from Oklahoma State University. His main research interests are healthcare informatics, business and data analytics, and digital entrepreneurship.

![](/api/attachments/4SUDQFDR/fulltext/images/a5e715a95612ab772d4ccb420ad5bc6897533cfb2fad4c76dee9be375b9554c3.jpg)

Dr. Dursun Delen is the holder of William S. Spears and Neal Patterson Endowed Chairs in Business Analytics, Director of Research for the Center for Health Systems Innovation, and Professor of Management Science and Information Systems in the Spears School of Business at Oklahoma State University (OSU). He received his Ph.D. in Industrial Engineering and Management from OSU in 1997. Prior to his appointment as an Assistant Professor at OSU in 2001, he worked for a privately-owned research and

consultancy company, Knowledge Based Systems Inc., in College Station, Texas, as a research scientist for five years, during which he led a number of decision support, information systems and advanced analytics related research projects funded by federal agencies, including DoD, NASA, NIST and DOE. His research has appeared in major journals including Decision Support Systems, Communications of the ACM, Computers and Operations Research, Computers in Industry, Journal of Production Operations Management, Artificial Intelligence in Medicine, Expert Systems with Applications, among others. He recently published eight books in the broader are of Business Analytics. He is often invited to national and international conferences for keynote addresses on topics related to Data/Text Mining, Business Intelligence, Decision Support Systems, Business Analytics and Knowledge Management. He regularly serves and chairs tracks and mini-tracks at various information systems conferences, and serves on several academic journals as senior editor, associate editor and editorial board member. His research and teaching interests are in data and text mining, decision support systems, knowledge management, business intelligence and enterprise modeling.

## Research Highlights:

 Medical records can be augmented with patients’ comparative health status.

 Extracting historical information can improve the prediction of hospital readmissions.

 Comprehensive data processing provides a competitive advantage to the health care organizations.
