---
otero_id: 11096
otero_key: "FFY8GSDA"
title: "Electronic health records in IS research: Quality issues, essential thresholds and remedial actions"
authors: "Gaurav Jetley; He Zhang"
year: "2019"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2019.113137"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Electronic health records in IS research: Quality issues, essential thresholds and remedial actions

![](/api/attachments/FFY8GSDA/fulltext/images/cc38f39f5d3ee396cddbc396ac0250554232f4592b4c6fc76ded2faf51d6705f.jpg)

Gaurav Jetley<sup>⁎</sup>, He Zhang

Muma College of Business, University of South Florida, Tampa, FL 33620, United States of America

## A R T I C L E I N F O

Keywords: Electronic health records Data quality issues Quality thresholds Remedial actions

## A B S T R A C T

The increase in adoption of Electronic Health Record (EHR) systems by healthcare organizations has led to the proliferation of the use of EHR as a secondary data source in both IS and supporting fields. It is imperative that EHR data is exploited appropriately, which would lead to high quality results and enhanced reproducibility. However, the quality of the EHR data being used can vary significantly and can have repercussions for research outcomes. In this paper, we first discuss four major data quality issues present in EHR data. These issues are: (a) non-standard coding schemes, (b) missing data, (c) inconsistencies and (d) aggregation and augmentation of EHR data. Then, we discuss quality thresholds that need to be met in order to avoid the negative impacts of quality issues. Lastly, we discuss some remedial actions that researchers can take to enhance the quality of EHR data to meet the quality thresholds. The discussed issues, thresholds and remedial actions can also apply to a much wider set of data sources when used as secondary data in research.

## 1. Introduction

Due to recent advances in healthcare technologies and changes in policies put forth by governments (i.e. HITECH Act¹), the use of Electronic Health Records (EHR) in healthcare organizations (HCOs) has seen a dramatic increase in the past decade [1]. This increased use of EHR systems has led to the capture of massive amounts of patient data, opening avenues for its utilization as a secondary data source in research. In information systems (IS), we have seen EHR data used for research in hospital workflow, disease management, clinical decision support systems and patient centric care, among others [2–4]. While there is great emphasis given to the modeling tasks in studies employing EHR data, the data quality is often not discussed in detail in research involving EHR data in IS. Like most types of observational data, EHR data can sufer from quality issues such as inaccuracy and missing values, which lead to issues downstream in research. Therefore, the use of EHR data in IS research needs more well-defined quality thresholds.

Marsden and Pingry [5] pointed out the seven elements, what, when where, how, which and why, that need to be addressed for the accuracy and validity of the data being used and reproducibility of the research being conducted. In many situations, EHR data can fail to address these W's due to data quality issues such as the presence of missing data and logical contradictions. EHR data used in IS literature [6–8] can be from various components of the system (audit, laboratory, radiology, pharmacy, clinical physician order entry (CPOE) system, clinical texts/notes and administrative components) and can suffer from quality issues ranging from missing data to issues in medical coding schemes used to record the data. These issues have repercussions for the reproducibility of the research as well as the accuracy of the findings. In this paper, we provide a compelling case for cautious use of EHR data in IS research by: (1) discussing four major data quality issues when using EHR data, (2) providing quality thresholds to address each issue and (3) discussing some remedial actions to improve the quality of EHR data to meet the quality thresholds.

The rest of the paper is organized as follows. In Section 2, we provide a brief overview of EHR systems and the use of EHR data in research. In Section 3, we discuss four major data quality issues in EHR data. In Section 4, we discuss the data quality thresholds that need to be met. In Section 5, we discuss the remedial actions that can help meet the quality thresholds. Concluding remarks are presented in Section 6.

## 2. Electronic health records and research

In the past decade, we have seen a widespread adoption of EHR systems. In 2011, 84% of hospital emergency departments (EDs) and

73% of outpatient departments (OPDs) used at least a basic EHR system.<sup>2</sup> Modern EHR systems include multiple components such as clinical notes and laboratory results. EHR systems typically record clinical information of patients visiting the institution in a longitudinal format. However, EHR systems don't capture the history of the patients across HCOs. Even inside an HCO, there can be disparate systems that do not interact with the main EHR system and/or may record data that is in diferent medical coding schemes or in diferent data formats (i.e. structured or unstructured data). Moreover, EHR systems capture data for clinical purposes, not for research, which makes the recording less careful than that for research purposes [9].

In the field of IS, EHR data has been used for research on clinical decision support systems [10,11] and quality of care improvements [12] among many other research topics. However, most research using EHR data focuses more on the development of methods or the research findings and less on supplying details on the quality issues that existed in the EHR data and how those issues were resolved. In this paper, we will provide a systematic discussion about major quality issues, quality thresholds and remedial actions for the usage of EHR data in IS research.

## 3. EHR data quality issues

In this section, we will cover four main EHR data quality issues, namely: (1) non-standard medical coding schemes, (2) missing data, (3) representational and semantic inconsistency and (4) aggregated and augmented EHR data. For each data quality issue, we are going to briefly describe the data quality issue with some typical examples, its negative outcomes, impacted W's and common causes.

## 3.1. Non-standard medical coding schemes

One of the major data quality issues with the use of EHR data in research is linked to the use of medical coding schemes [13,14]. In general, coding schemes are used to describe and define the data, which involves assigning raw observations into categories representing particular themes or topics based on similarities or diferences between the observations. Based on the scheme being used, data can be coded quite diferently than in other schemes. Naturally, having multiple coding schemes can introduce data quality issues such as incorrectness and impreciseness.

Similarly, medical coding involves the conversion of concepts such as medical conditions (diagnosis) and services (procedures) to predefined codes (medical coding schemes) [15]. There are a variety of medical coding schemes available worldwide and the use of a medical coding scheme can not only vary between EHR datasets (guided by factors such as EHR provider, etc.), but also within EHR datasets. Having a data attribute coded in multiple coding schemes, no coding scheme or a combination of both [16,17] can create data quality issue if not dealt with appropriately. For example, the recording of patient diagnosis in free-form text (no coding scheme) can introduce in correctness due to coding errors and impreciseness due to the lack of rigorous definitions [14,18]. Fig. 1 provides an overview of the key elements of this data quality issue.

## 3.2. Missing data

The second major data quality issue in EHR data is linked to missing attributes, missing data within attributes and longitudinal truncations for observations. Completeness of data is described as the presence of the complete truth regarding an observation being present in the data [19]. Missing attributes, missing data within attributes and longitudinal truncation of observations hinder the data from providing the complete truth about the afected observations. For example, if we have missing date and time information for a medication prescription to a patient, it is hard to establish the truth about when the prescription was given and if the patient is still on the medication. EHR data can sufer from truncation when there is unobserved data before the start, during or after the end of the observation period for a patient in the EHR dataset [20]. For example, missing information on disease diagnosis and associated timestamps for a patient transferring from another facility is often not recorded in EHR datasets.

Incompleteness in EHR data can introduce data quality issues such as the ambiguity due to missing values which may lead to bias in conclusions and a large amount of missing values in the data which may lead to insuficient data for analysis [21]. Fig. 2 lists the key elements of this data quality issue.

## 3.3. Representational and semantic inconsistency

The third major data quality issue is inconsistency. Weiskopf and Weng [19] describe consistency as the agreement in data attributes, where two or more attributes recording the same information for an observation should have the same values (also known as representational consistency) [22] and the information regarding observations contained in the attributes should be logically sound (also known as semantic consistency) [19,22].

Representational consistency is violated when there is variation in data due to multiple formats, units, granularities and measurement protocols [23,24]. For example, inconsistencies can occur when having weights of patients recorded in both pounds and kilograms or using both a 3-point and a 5-point Likert scale to record pain levels [25]. Semantic consistency is violated when the data has logical contra dictions [22] such as records of hospital visits by a deceased patient. Having representational and/or semantic inconsistency in data can lead to issues such as implausibility [19,22] of data due to logical contradictions, which can be related to lab reports being outside of the range of plausible values for a human being. Fig. 3 provides an overview of this data quality issue.

## 3.4. Data aggregation and augmentation

With the scarcity of EHR data sources coupled with the need for larger sample sizes or a richer set of attributes, it is not uncommon for the researchers to aggregate data from multiple sites and augment data with more/transformed attributes from multiple information sources [26]. Data aggregation is a process of combining information from multiple sources for the purpose of creating a larger dataset, for example, aggregating patient information (i.e. demographics, disease diagnosis, medication prescriptions, etc.) from multiple small EHR datasets to form one large dataset. Data augmentation, on the other hand, is the process of enriching the data with external information or manip ulating the data in order to make it easier to analyze [27], for example, augmenting the drug prescriptions recorded in an EHR dataset by including a new attribute for active drug ingredients sourced from an external dataset.

Data in individual and disparate EHR systems can be very heterogeneous with respect to the medical coding schemes being used, missing values in the data, inconsistencies in the data and the reasons for data collection [28]. For example, aggregation of multiple EHR datasets holding patient information will be challenging because of the existence of multiple formats of patient information. This will be the case even if the EHR datasets and external datasets used for augmentation are free of the quality issues individually. Fig. 4 provides an overview of this data quality issue.

## 4. Quality thresholds

In this section, we discuss data quality thresholds for EHR data being used for research in IS and supporting disciplines. The threshold we discuss in this section correspond to the four data quality issues discussed in Section 3.

<table><tr><td>Brief Description:EHR data attributes recorded in multiple medical coding schemes, no medical coding scheme or a combination of the two.Typical Examples:Patient condition of back pain being coded interchangeably within the same attribute as: (a) “724.5” using International Classification of Diseases, 9th revision, coding scheme (See Appx. A); (b) “T-D2100” and “F-A26000” using the Systematized Nomenclature of Medicine coding scheme (See Appx. A) or; (c) “Back Pain” using free-form textual input (no coding scheme).</td><td>Negative Outcomes:Incorrectness and impreciseness concerns.W’s Impacted:What is being recorded andwhichcoding scheme was used to record the data.Common Causes:Changes in the EHR system provider, evolutionary changes in the coding schemes and recording in free-form text.</td></tr></table>

Fig. 1. Overview of data quality issue due to non-standard coding schemes.

<table><tr><td>Brief Description:Missing values in data attributes and missing longitudinal information for observations.Typical Examples:Missing diagnosis date for a patient diagnosis or missing historical diagnosis information for a patient being transferred from another facility.</td><td>Negative Outcomes:Ambiguity, sufficiency and inaccuracy concerns.W’s Impacted:What is and isn’t recorded in the data;Whenthe data was recorded;Wherewas the data not recorded;Howwas the data recorded and why are there missing values.Common Causes:Receiving care at multiple HCOs, refusal to provide information, data recording failure and attributes relevance only in certain situations</td></tr></table>

Fig. 2. Overview of data quality issue due to missing data.

<table><tr><td>Brief Description: Contradictory information in EHR data such as mismatch between two attributes that record the same data or logical errors in the recorded data. Variation in measurement protocols, granularities, scales, etc. for recording a single attribute.Typical Examples:Mismatch between the diagnosis dates recorded in two separate tables for a patient, a diagnosis recorded after death of patient, weight being recorded in pounds and kilograms.</td><td>Negative Outcomes:Incorrectness and inaccuracy concerns.W’s Impacted:What is being recorded, when was it recorded, how was the data recorded and which instruments and protocols were used in recording the data.Common Causes:Changes in EHR system providers, phased rollout of the EHR system, data entry as free form text and change in procedure protocols.</td></tr></table>

Fig. 3. Overview of data quality issue due to representational and semantic inconsistency.

<table><tr><td>Brief Description:EHR dataset that is being aggregated or external information that is being used to augment the EHR data having the first three data quality issues.Typical Examples:Aggregating multiple EHR datasets together which have attributes recorded in different formats. Augmenting EHR dataset with external data on a common attribute which is formatted differently in both.</td><td>Negative Outcomes:Incorrectness, impreciseness, ambiguity, sufficiency, and inaccuracy concerns.W’s Impacted:All W’s in Sections 3.1 - 3.3.Common Causes:Presence of the first three data quality issues in individual or aggregated and/or augmented dataset(s).</td></tr></table>

Fig. 4. Overview of data quality issue due to aggregation and augmentation of EHR data.

## 4.1. Formal medical coding schemes

Data quality thresholds for the non-standard coding scheme issue have been extensively covered in previous literature [14,29,30]. The Ofice of the National Coordinator for Health Information Technology<sup>3</sup> (ONC) recommends the use of standard medical coding schemes for recorded information (i.e. patient diagnosis, procedures, etc.) and having limited free-form text fields in the data [31] to reduce potential data quality issues. For example, the International Classification of Diseases, 9th and 10th revisions, clinical modification<sup>4</sup> (ICD9-CM and ICD10-CM), maintained by the World Health Organization, is a popular coding standard for recording disease diagnosis and medical procedures in EHR systems across the world [14]. This coding standard is also heavily used in health informatics research and IS [12,32]. Definitions for the most commonly used coding schemes for recording diagnosis, medications and laboratory reports are provided in Appx. A. For more details on most globally recognized coding schemes, please see [33].

Using EHR data that follows formal medical coding schemes used in previous literature and recommended by agencies such as ONC will not only help increase the reproducibility of the research but also significantly reduce the quality issues that arise due to the presence of non-standard medical coding schemes [19]. Thus, the first threshold that EHR data needs to meet in order to avoid the negative impacts of the presence of non-standard coding schemes is:

Threshold 1. EHR data used for research should follow formal medical coding schemes.

EHR data meeting Threshold 1 precisely describes and defines what is being recorded in the data according to the coding scheme used. This threshold also increases the accuracy and removes ambiguity in the data due to the lack of free-form text entry.

## 4.2. Completeness

The second data quality threshold we discuss is concerned with the presence of missing data, which has been heavily discussed in previous literature [21,31]. Literature tackling the issue of missing data in EHR datasets used in research points out the negative consequences of missing data. These consequences include the inability of running certain analytical methods because of missing data, reduced power due to a larger proportion of missing data and bias in the study outcomes due to systematic underlying reasons for the missing data or misinterpretation of the missing value [21,34,35]. Most literature that use EHR data for research drops the observations that have missing values or plausible longitudinal truncations to avoid the reparations of this data quality issue [11,12]. Thus, following previous literature on missing data in EHR datasets, we suggest that the second threshold that good quality EHR data needs to meet is:

Threshold 2. EHR data used for research should have no missing values in key attributes; no longitudinal truncation in observations for temporal/trajectory analysis; no ambiguity for missing data in non key attributes.

EHR data that meets Threshold 2 reduces the negative consequences of missing data such as bias [21,34,35] and thus increases the data accuracy and study reproducibility.

## 4.3. Representational and semantic consistency

The third data quality threshold that EHR data needs to meet is the representational and semantic consistency of the EHR dataset being used in research. Consistency in EHR data is another data quality threshold that has been extensively discussed in the field of health in formatics [19]. Researchers should only have data corresponding to observations which are consistent before using the data in any study, as inconsistencies can lead to bias and other negative repercussions [36].

The ONC suggests that good quality EHR data needs to be consistent and suggests several ways to ensure representational and semantic consistency, such as standardized formats, field definitions and reference ranges [31]. Literature also suggests that inconsistencies between and within EHR data attributes pose serious problems for the efective use of EHR data in research [24]. The majority of researchers using EHR data perform careful deletion of inconsistent data such as data outside the range of a particular therapeutic range [11] to avoid the negative consequences of the presence of inconsistencies. Thus, we suggest:

Threshold 3. EHR data being used in research must be representationally and semantically consistent.

EHR data that meets Threshold 3 improves the correctness in EHR data because of consistency in formats and increases the plausibility of data by not having any contradictions in the EHR data.

## 4.4. Accurate aggregation and augmentation

Researchers should be extremely careful in how they aggregate and augment the datasets as it can lead to all the data quality issues discussed in Sections 3.1 – 3.3. Thresholds 1, 2 and 3 are all applicable when researchers are aggregating multiple EHR datasets. Meeting these thresholds is critical as the coding schemes, missing values, and representational and semantic inconsistencies between datasets can difer even more than within EHR datasets [37]. Moreover, even if the EHR datasets are free of quality issues individually, the act of aggregation itself can introduce the above data quality issues. Hence, we suggest the following threshold when using multisite data for aggregation and external data for augmentation:

Threshold 4.a. When aggregating EHR data or augmenting EHR data with external data, the first three thresholds for data quality must be met for each individual and the aggregated/augmented dataset.

Additionally, augmentation of EHR data with external data sources brings about additional challenges and issues. Common attributes used for matching EHR and external data which are not in the same coding scheme or which have diferent units/formats of recording contributes to the complexity of using EHR datasets for secondary research [38]. We suggest one additional threshold for data augmentation:

Threshold 4.b. When augmenting EHR data with an external data source, the matching between the two data sources should be done on common attributes recorded using the same coding scheme or in the same format.

Aggregated and augmented EHR data meeting the above thresholds will resolve all the issues that the other thresholds help with.

## 5. Remedial actions for meeting lower thresholds

In this section, we discuss some methods and techniques which researchers can exploit to meet the lower thresholds when there are one or more data quality issues (Section 3) present in their EHR data. Table 1 lists some methods and techniques that can be used to increase the quality of

EHR data while still allowing researchers to keep most of the observations and attributes present in their dataset(s). It should be noted that all the remedial actions mentioned in this section should only be performed under the supervision of medical professionals and experts.

To achieve Threshold 1 when there are multiple coding schemes present in an attribute, researchers can exploit external mappings<sup>5</sup> for conversion between coding schemes [40]. For example, Metathesaurus<sup>6</sup> provides mappings between over 200 medical coding schemes. Researchers can exploit methods in the field of natural language processing (NLP) to convert free-form text to a formal medical coding scheme [19,41]. Researchers can also take the help of healthcare professionals to manually convert to a formal medical coding scheme [29], however, this may be very resource intensive.

To meet Threshold 2 when there is missing information in the EHR data, researchers can exploit information sources that are not traditionally used in research such as clinical notes which house patient information in an unstructured format. NLP tools and techniques such as The SPECILIST Lexicon [42] provided by UMLS can be used to selectively extract missing information in a well-documented fashion.

Table 1  
Remedial actions to meet lower thresholds for EHR data quality.

<table><tr><td>Threshold</td><td>Remedial action(s)</td></tr><tr><td>1</td><td>(a) When multiple coding schemes are present in a single attribute, external mappings between coding schemes can be used to convert the attribute to a single coding scheme [13,39,40].(b) When free-form text is present in attributes: (1) natural language processing (NLP) techniques can be used to convert to a formal coding scheme [14,19,24,41] or (2) manual mapping of free-form text to a formal coding scheme can be performed [29].</td></tr><tr><td>2</td><td>(a) When additional patient information is present in the form of free-form text such as clinical notes, researchers can use: (1) information extraction techniques [42] and (2) manual information extraction to fill in missing values [42,43].(b) External data sources such as clinical registries can be exploited to fill in missing patient information [24,44].(c) If (a) and (b) cannot be used, careful deletion using appropriate techniques can be employed [11,45].</td></tr><tr><td>3</td><td>Manual intervention by healthcare professionals or deletion techniques to resolve representational and semantic inconsistencies [11].</td></tr><tr><td>4.a</td><td>Performing the remedial actions for Thresholds 1, 2 &amp; 3 on individual and aggregated/augmented datasets.</td></tr><tr><td>4.b</td><td>(a) Mappings between coding schemes can be used to convert the common attributes used for augmentation to a single coding scheme [39].(b) Careful deletion of observations that are not augmented properly [45].</td></tr></table>

These conversion methods, however, are not 100% accurate and need supervision by healthcare professionals and experts [24]. Information from the clinical notes can also be manually extracted, however, as with any manually conducted technique, it can be very resource intensive. External sources of information such as national cancer registries [24,44] can be used to fill in missing information such as cancer diagnosis. In the case where the missing data in not retrievable from either clinical notes or external data sources, deletion techniques can be used [11].

To meet Threshold 3, representational inconsistencies such as multiple formats, measures, granularities and recording procedures in attributes and semantic inconsistencies like contradictory data can be resolved with the help of healthcare experts using manual intervention. If the inconsistencies in certain attributes cannot be resolved or if the inconsistencies are too numerous to be resolved manually, then careful deletion of those observations can be performed with a healthcare professional's guidance [11].

To make EHR data meet Threshold 4.a when aggregating and/or augmenting EHR data, researchers can repeat the remedial actions for Thresholds 1, 2 and 3 on each individual and aggregated/augmented dataset(s). Additionally, to meet Threshold 4.b when augmenting EHR data with an external dataset, researchers can use mappings between medical coding schemes to convert the common attributes used for augmentation to a single coding scheme. Careful deletion of observations that were not augmented properly is another option that researchers can use.

## 6. Conclusions

In this paper, we discuss four major data quality issues that arise when EHR data is used in research. We first discuss how these issues impact data quality in terms of the identifiability of the seven W's [5]. Next, we provide researchers with four data quality thresholds that EHR data needs to meet when being used for research. We also investigate some remedial actions that researchers can employ to make the EHR data meet the quality thresholds.

The issues, thresholds and remedial actions presented in this paper are by no means comprehensive and there are likely to be more issues that can impact EHR data quality when used for research purposes. These EHR data quality thresholds will not only apply to research in IS, but other disciplines as well, and produce more reliable results and help in curtailing the reproducibility crisis in the healthcare research [46]. Though we focus solely on EHR data in this article, the scope of implications is much wider, as EHR data is used across industries and research streams. The four issues, thresholds and remedial actions that we discuss in this paper can apply to a wider variety of observational data for IS research.

Appendix A. Definitions of some common medical coding schemes used in EHR systems

<table><tr><td>Medical coding scheme</td><td>Definition</td></tr><tr><td>ICD-9-CM and ICD-10-CM</td><td>International Classification of Diseases, 9th and 10th revisions, clinical modification, are used to code medical diagnosis and procedures from physician offices and inpatient/outpatient records. These codes are commonly used for billing, reporting and morbidity statistics.</td></tr><tr><td>SNOMED-CT</td><td>Systematized Nomenclature of Medicine, Clinical Terms, is the most comprehensive and precise multilingual medical coding terminology and can be mapped to a variety of other coding systems such as ICD-9-/10CM.</td></tr><tr><td>RxNorm</td><td>RxNorm is a standardized nomenclature for clinical drugs and is intended to cover all human use approved drugs in the United States with certain exceptions for inclusion of international drugs as well. RxNorm provides standardized names for clinical drugs and dosages.</td></tr><tr><td>LOINC</td><td>The Logical Observation Identifiers Names and Codes terminology is used for the recording of laboratory results for clinical care, reporting and research. LOINC provides standardized names and structured codes for laboratory and clinical observations.</td></tr></table>

## References

[1] I.R. Bardhan, M.F. Thouin. Health information technology and its impact on the quality and cost of healthcare delivery. Decision Support Systems 55 (2) (2013) 438-449.

[2] G. van Valkenhoef, et al., ADDIS: a decision support system for evidence-based medicine, Decision Support Systems 55 (2) (2013) 459–475.

[3] M.P. Johnson, K. Zheng, R. Padman, Modeling the longitudinality of user acceptance of technology with an evidence-adaptive clinical decision support system, Decision Support Systems 57 (2014) 444–453.

[4] A. Gupta, R. Sharda, Improving the science of healthcare delivery and informatics using modeling approaches, Decision Support Systems 55 (2) (2013) 423–427.

[5] J.R. Marsden, D.E. Pingry, Numerical data quality in IS research and the

implications for replication, Decision Support Systems 115 (2018) A1–A7.

[6] S. Walczak, V. Velanovich, Improving prognosis and reducing decision regret for pancreatic cancer treatment using artificial neural networks, Decision Support Systems 106 (2018) 110–118.

[7] A. Sen, A. Al Kawam, A. Datta, Emergence of DSS eforts in genomics: past contributions and challenges, Decision Support Systems 116 (2019) 77–90.

[8] A.L. Rector, Clinical terminology: why is it so hard? Methods of Information in Medicine 38 (04/05) (1999) 239–252

[9] M.G. Weiner, P.J. Embi, Toward reuse of clinical data for research and quality improvement: the end of the beginning? Annals of Internal Medicine 151 (5) (2009) 359–360.

[10] Z.Y. Zhuang, C.L, Wilkin, A. Ceglowski, A framework for an intelligent decision support system: a case in pathology test ordering. Decision Support Systems 55 (2) (2013) 476–487

[11] B. Yet, et al., Decision support system for Warfarin therapy management using Bayesian networks, Decision Support Systems 55 (2) (2013) 488–498.

[12] I. Bardhan, et al., Predictive analytics for readmission of patients with congestiv heart failure, Information Systems Research 26 (1) (2014) 19–39.

[13] J. Millar, The need for a global language - SNOMED CT introduction, Studies in Health Technology and Informatics 225 (2016) 683–685.

[14] Laur, E.J.M., #237, and A.D. March, Combining Bayesian text classification and shrinkage to Automate healthcare coding: a data quality analysis. Journal of Data and Information Quality, 2011. 2(3): p. 1–22.

[15] Y. Yan, et al., Medical coding classification by leveraging inter-code relationships, Proceedings of the 16th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, ACM, Washington, DC, USA, 2010, pp. 193–202.

[16] J.R. Campbell, et al., Phase II evaluation of clinical coding schemes: completeness, taxonomy, mapping, definitions, and clarity. CPRI work group on codes and structures, Journal of the American Medical Informatics Association 4 (3) (1997) 238–251.

[17] E.F. Codd, Data models in database management, ACM SIGMOD Record 11 (2) (1981) 112–114.

[18] F. González Bernaldo de Quirós, C. Otero, D. Luna, Terminology services: standard terminologies to control health vocabulary. Yearbook of Medical Informatics. 27(1 2018. pp. 227–233.

[19] N.G. Weiskopf, C. Weng, Methods and dimensions of electronic health record data quality assessment: enabling reuse for clinical research, Journal of the American Medical Informatics Association 20 (1) (2013) 144–151

[20] C.M. Hazelbag, et al., Left truncation results in substantial bias of the relation between time-dependent exposures and adverse events, Annals of Epidemiology 25 (8) (2015) 590–596.

[21] B.K. Beaulieu-Jones, et al., Characterizing and managing missing structured data in electronic health records: data analysis, JMIR Medical Informatics 6 (1) (2018) e11.

[22] B. Heinrich, et al., Assessing data quality–a probability-based metric for semantic consistency, Decision Support Systems 110 (2018) 95–106.

[23] Kahn, M.G., et al., A pragmatic framework for single-site and multisite data quality assessment in electronic health record-based clinical research. Medical Care, 2012. 50 Suppl(0): p. S21-S29.

[24] T. Botsis, et al., Secondary use of EHR: data quality issues and informatics oppor tunities, Summit on Translational Bioinformatics, 2010, 2010, pp. 1–5.

[25] S.L. Feder, Data quality in electronic health records research: quality domains and assessment methods, Western Journal of Nursing Research 40 (5) (2018) 753–766.

[26] Y. Gong, H. Kang, Usability and clinical decision support, in: E.S. Berner (Ed.), Clinical Decision Support Systems: Theory and Practice, Springer International Publishing, Cham, 2016, pp. 69–86.

[27] M.A. Tanner, W.H. Wong, The calculation of posterior distributions by data augmentation, Journal of the American Statistical Association 82 (398) (1987) 528–540.

[28] J. van der Lei, Use and abuse of computer-stored medical records, Methods of Information in Medicine 30 (2) (1991) 79–80.

[29] A.D. March, E.J. Laura, J. Lantos, Automated icd9-cm coding employing bayesian machine learning: a preliminary exploration, Simposio de Informtica y Salud, 2004.

[30] D.A. Ariosto, et al., Population health: a nursing action plan, JAMIA Open 1 (1) (2018) 7-10

[31] B.N.L. Guide, Capturing high quality electronic health records data to support performance improvement. Implementation Obiective. 2 2013. p. 16.

[32] D. Bertsimas, et al., Algorithmic prediction of health-care costs. Operations Research 56 (6) (2008) 1382–1392.

[33] U.S. National Library of Medicine, UMLS Metathesaurus vocabulary documentation, [cited 2019 May 16]; Available from, 2019, May 6. https://www.nlm.nih.gov research/umls/sourcereleasedocs/index.html.

[34] B.J. Wells, et al., Strategies for handling missing data in electronic health record derived data, EGEMS (Washington, DC) 1 (3) (2013) 1035.

[35] P.D. Allison, Missing data, 136 Sage Publications, 2001.

[36] K.B. Bayley, et al., Challenges in using electronic health record data for CER: experience of 4 learning organizations and solutions applied, Medical Care 51 (2013) S80–S86.

[37] R.E. Hirschtick, Copy-and-paste, JAMA 295 (20) (2006) 2335–2336.

[38] M.R. Cowie, et al., Electronic health records to facilitate clinical research, Clinica Research in Cardiology 106 (1) (2017) 1–9.

[39] A.R. Aronson, Efective mapping of biomedical text to the UMLS Metathesaurus: the MetaMap program, Proceedings of the AMIA Symposium, American Medica Informatics Association, 2001.

[40] O. Bodenreider, The unified medical language system (UMLS): integrating biome dical terminology, Nucleic Acids Research 32 (suppl\_1) (2004) D267–D270.

[41] H. Xu, et al., Facilitating cancer research using natural language processing of pa thology reports, Studies in Health Technology and Informatics 107 (Pt 1) (2004) 565–572.

[42] A.C. Browne, A.T. McCray, S. Srinivasan, The SPECIALIST lexicon (2018 revision), National Library of Medicine Technical Reports, 2018.

[43] G.K. Savova, et al., Automated discovery of drug treatment patterns for endocrine therapy of breast cancer within an electronic medical record, Journal of the American Medical Informatics Association 19 (e1) (2012) e83–e89.

[44] J.M.I.H. Gho, et al., An electronic health records cohort study on heart failure following myocardial infarction in England: incidence and predictors, BMJ Open 8 (3) (2018) e018331.

[45] T.J. Spaulding, et al., Event sequence modeling of IT adoption in healthcare, Decision Support Systems 55 (2) (2013) 428–437.

[46] F.S. Collins, L.A. Tabak, Policy: NIH plans to enhance reproducibility, Nature News 505 (7485) (2014) 612

![](/api/attachments/FFY8GSDA/fulltext/images/750df4e1574a54093397599c0a00e9d3e8f4d9a939257dce76de7846b3d79145.jpg)

Gauray Jetley is a doctoral candidate in the Information Systems and Decision Sciences department at University of South Florida. Prior to joining the Doctoral program in Information Systems, Gaurav earned a Bachelor's in Commerce with a major in Computing and Information Systems from the Sobey School of Business at Saint Mary's University and a MS in Management Information Systems from University of South Florida. His research interests include applications of machine learning in healthcare, health informatics impacts of multimodal information on decision making and economics of information systems.

![](/api/attachments/FFY8GSDA/fulltext/images/831aa554e5a74809006d77c3615a8aba8dcfa00779788be1133809fa63829fdd.jpg)

He Zhang is an assistant professor in the Information Systems and Decision Sciences department in the Muma College of Business at the University of South Florida. His research interests include healthcare information manage ment, Big Data, and production and inventory management. Zhang's research has been published in journals including Mathematical Programming, Decision Support Systems and ACM Transactions on Management Information Systems.
