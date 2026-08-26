---
otero_id: 2034
otero_key: "GDFJD5TF"
title: "Using data envelopment analysis and decision trees for efficiency analysis and recommendation of B2C controls"
authors: "Sangjae Lee"
year: "2010"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.06.002"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Using data envelopment analysis and decision trees for ef<sup>fi</sup>ciency analysis and recommendation of B2C controls

Sangjae Lee

College of Business Administration, Sejong University, 98 Kunja-dong, Kwangjin-gu, Seoul 143-747, Republic of Korea

## a r t i c l e i n f o

Article history: Received 11 September 2009 Received in revised form 30 March 2010 Accepted 12 June 2010 Available online 17 June 2010

Keywords: B2C applications B2C controls Data envelopment analysis (DEA) Decision trees Implementation of B2C applications

## a b s t r a c t

Appropriate guidelines for controls in B2C (business-to-consumer) applications (hereafter B2C controls) should be provided such that these guidelines accomplish ef<sup>fi</sup>ciency of controls in the context of speci<sup>fi</sup>c system environments, given that many resources and skills are required for the implementation of such controls. This study uses a two-step process for the assessment of B2C controls, i.e., ef<sup>fi</sup>ciency analysis and recommendation of controls. First, using a data envelopment analysis (DEA) model, the study analyzes the ef<sup>fi</sup>ciency of B2C controls installed by three groups of organizations: <sup>fi</sup>nancial <sup>fi</sup>rms, retail <sup>fi</sup>rms, and information service providers. The B2C controls are composed of controls for system continuity, access controls, and communication controls. DEA model uses B2C controls as input and three variables of implementation of B2C applications, i.e., volume, sophistication, and information contents as output. Second, decision trees are used to determine ef<sup>fi</sup>cient <sup>fi</sup>rms and generate rules for recommending levels of controls. The results of the investigation of the DEA model indicate that retail <sup>fi</sup>rms and information service providers implement B2C controls more ef<sup>fi</sup>ciently than <sup>fi</sup>nancial <sup>fi</sup>rms do. Controls for system continuity are implemented more ef<sup>fi</sup>ciently than access controls. In <sup>fi</sup>nancial <sup>fi</sup>rms, controls for system continuity, communication controls, and access controls, in a descending order, are ef<sup>fi</sup>ciently adopted in B2C applications. Every company can determine its relative level of reduction in each component of controls in order to make the control system ef<sup>fi</sup>cient. The <sup>fi</sup>rms that ef<sup>fi</sup>ciently implement B2C controls are determined using a decision tree model. The decision tree model is further used to recommend the level of controls and suggest rules for controls recommendation. This suggests the possibility of using decision trees for controls assessment in B2C applications. © 2010 Elsevier B.V. All rights reserved

## 1. Introduction

As organizations rely increasingly on IS (information Systems) for strategic advantage and operations, management needs to pay more attention to IS security issues due to a corresponding increase in the impact of IS security abuses. Controls of e-business applications should ensure the security, integrity, auditability, and controllability of the con<sup>fi</sup>gured software, data, and support organization [16].

As controls are not only expensive to put in place and operate, but also increase audit efforts and slow down the execution of business processes, it is necessary to automate controls in an optimum manner from a cost and regulatory perspective [28]. How internal auditors or security administrators make decisions of controls assessment or adjustment is in large part a matter of judgment and experience. Thus, it is necessary to devise a systematic approach for controls assessment for security management that relies on a series of subjective judgments of internal auditors or security administrators.

Gordon and Loeb [13] have shown an economic model to determine the optimal level of investment in information security. Cavusoglu et al.

[7] suggested a model based on game theory for strategic investment decisions in security controls; in the IT security problem, the <sup>fi</sup>rm and hacker are players and the <sup>fi</sup>rm's payoff from security investment depends on the extent of hacking it is subjected to. Industry characteristics such as system vulnerability to security risks and availability of value added networks can affect the ef<sup>fi</sup>ciency of EDI (Electronic Data Interchange) controls [21]. Pareek [27] used an optimization algorithm based on a linear programming model to identify controls that need to be tested to address the risks.

The law of diminishing returns posits that, beyond a certain point, the effectiveness of protection provided by additional controls will diminish and no longer improve the quality of the information systems [9]. Guidance can be provided by analyzing the data collected from questionnaires used to measure controls. In view of the state of implementation, and given the high cost and resources needed to develop controls embedded in the system, it is necessary to analyze the ef<sup>fi</sup>ciency of controls in B2C (business-to-consumer) applications (hereafter B2C controls). Depending on who performs the analysis, however, a wide range of security measures may be implemented, resulting in either too few or too many B2C controls. This study intends to investigate the assessment of B2C controls, i.e., ef<sup>fi</sup>ciency analysis and recommendation of controls, using a data envelopment analysis (DEA)

model and decision trees. Previous studies have combined the use of DEA and decision trees in analyzing organizational units [30,31,34]. Using decision trees may support IS managers and convince them of the kinds of control measures that are necessary under given system circumstances. The <sup>fi</sup>rms that ef<sup>fi</sup>ciently implement B2C controls are determined using a decision tree model. The decision tree model is further used to recommend the level of controls and to suggest rules for controls recommendations. This suggests the possibility of using decision trees for controls assessment in B2C applications.

## 2. Theoretical background

## 2.1. Process of controls assessment

Audit management staff members face a constant need to cut time in completing controls assessment and testing. Automated data mining tools are capable of investigating a large amount of information and searching for patterns that may not be identi<sup>fi</sup>ed easily by manual means [26]. The US Sarbanes-Oxley Act has already had a signi<sup>fi</sup>cant in<sup>fl</sup>uence on the assessment and evaluation of internal controls [4]. Section 404 demands that management annually conducts an assessment of the design and operation of the company's internal controls and procedures for <sup>fi</sup>nancial reporting. The objective of controls assessment is to assure customers, stakeholders, and government agencies that controls are in place and effective.

Too few security measures make the <sup>fi</sup>rm's IT environment vulnerable to a wide range of potentially damaging risks, and too many security measures lead to an increase in costs, to slowdowns and to delays in processing applications [9]. The assessment of controls done is to ensure adequacy of controls for a balance between costs incurred for implementing controls and the resulting bene<sup>fi</sup>ts derived.

Controls assessment provides a method for management to determine the current status of their information security programs; this assessment involves controls improvement, if necessary through the timely detection and correction of weak controls [4]. Assessment offers a means of identifying problems of controls and recommendations for improvement. Further, assessment is done to reduce or eliminate costly and inef<sup>fi</sup>cient controls while creating valuable alternatives.

The examples of controls assessment models includes the NIST (National Institute of Standards and Technology) model from the US National Institute of Standards and Technology, the COBIT (Control Objectives for Information and Related Technology) model from the Information Systems Audit and Controls Association, and the Business Process Model. The NIST model suggested a questionnaire to be applied for any organization. The COBIT model is an IT governance tool that helps organizations understand and manage the risks associated with IT. The Business Process Model is based on the identi<sup>fi</sup>cation of risks associated with each business process. Sound knowledge of business processes, information control objectives, and company environments are crucial factors in the success of introduction of the controls assessment model.

## 2.2. DEA analysis

Assessing an IT security investment has been a sticking point, and a rational methodology is required to analyze security investments [7]. This study used DEA to analyze the ef<sup>fi</sup>ciency of B2C controls. DEA is a mathematical programming formulation based technique that provides an ef<sup>fi</sup>cient frontier to suggest an estimate of the relative ef<sup>fi</sup>ciency of each decision making unit (DMU) in a problem set [10]. DEA is developed around the concept of evaluating the ef<sup>fi</sup>ciency of a decision alternative based on its performance of creating outputs in means of input consumption. The ef<sup>fi</sup>ciency of each DMU, relative to its peers, is de<sup>fi</sup>ned as the ratio of that member's weighted sum of outputs to its weighted sum of inputs. No functional form relating the input to output variables is necessary. The parametric approach, such as regression equation and discriminant analysis, however, requires speci<sup>fi</sup>c assumptions about the functional form and the distribution of error terms (e.g., independently or normally distributed). Those DMUs not on the frontier are scaled against a convex combination of the DMUs on the frontier facet closest to them.

DEA is used in a wide range of contexts, such as software projects [23], information technology investments [33], technology commercialization projects [34], EDI controls [21], Internet companies [32], branches of banks [37], service delivery processes [31], data warehouse operations [24] and supplier evaluation and selection ([8].

## 2.3. Decision trees

In order to ensure successful audits, organizations should maintain a minimized list of controls that is manageable and easy to understand [3]. For instance, network security (especially, updated <sup>fi</sup>rewalls and secure wireless connections), virus and spyware protection, and backup procedures are the three most important controls for a small business [6]. Auditors can use data mining techniques such as statistical modeling to uncover patterns that can help organizations identify process improvements, detect fraud, and improve risk management [26]. As auditing based on data mining may require additional resources to ensure management data analysis for a continuous assurance process, auditors should plan adequately and have a reasonable perspective before embarking on a data mining exercise.

Decision trees are a rapid and effective method of classifying data set entries, and can offer good decision support capabilities. A decision tree is a tree in which each non-leaf node denotes a test on an attribute of cases, each branch corresponds to an outcome of the test, and each leaf node denotes a class prediction. The quality of a decision tree depends on both its classi<sup>fi</sup>cation accuracy and its size.

Classi<sup>fi</sup>cation using decision trees categorizes a set of cases in a database into different classes according to a classi<sup>fi</sup>cation model. Two kinds of data sample are used for the classi<sup>fi</sup>cation task. A training sample (i.e., a set of cases whose class labels are known) is <sup>fi</sup>rst analyzed and a classi<sup>fi</sup>cation model is constructed based on the features available in the data of the training sample. Such a classi<sup>fi</sup>cation model is then used to categorize a test sample (i.e., a set of cases whose class labels are unknown). For example, we can use the classi<sup>fi</sup>cation model learned from the existing customers' data to predict what services a new customer would like.

A case in the training sample set consists of multiple attributes (independent and dependent factors) and a known class label associated with them. The independent factors are represented as an attribute-value vector, $\mathbf { x } = ( \chi _ { 1 } \chi _ { 2 } , . . . , \chi _ { \mathrm { j } } )$ . Assume that the cases can fall into j classes, that is, ${ \mathsf { C } } = ( \mathsf { c } _ { 1 } \mathsf { c } _ { 2 } , . . . , \mathsf { c } _ { \mathrm { j } } ) .$ Then, a training sample can be denoted by $\begin{array} { r } { \mathbf { M } = \{ ( \mathbf { x } _ { \mathrm { m } } , \mathbf { y } _ { \mathrm { m } } ) \} } \end{array}$ where $\mathbf { \boldsymbol { x } } _ { \mathrm { { m } } } { \in } \mathbf { \boldsymbol { X } }$ (all possible attribute space) and ${ \tt y } _ { \mathrm { m } } { \in } C ( \mathrm { a l l }$ possible cases), $\mathrm { m } { = } 1 , { \ldots } M$ (the size of the model set). On the other hand, since all the cases in a test sample have no known class levels, a test sample is denoted by ${ \sf S } = \{ ( { \sf X } _ { \mathrm { E } } , { \sf y } _ { \mathrm { E } } ) \}$ } where $\mathbf { \boldsymbol { x } } _ { s } \in \mathbf { \boldsymbol { X } }$ and $\mathsf { y } _ { s } \in \emptyset , s = 1 , . . . , S$ (the size of the test sample). A decision tree can be induced that will make it possible to assign a class to the dependent factor of a new case in the test sample based on the values of independent factors.

Applications of a decision tree based classi<sup>fi</sup>cation include target marketing, churn prediction, medical diagnosis, and so on. For instance, Bernstein and Provost [5] used decision trees in the development of a knowledge discovery assistant, in order to categorize different methods used to solve a speci<sup>fi</sup>c problem. Endou and Zhao [12] investigated a decision tree implementation method that relied on an evolution of the training data set used. The training data set was developed to give the best coverage of the domain knowledge. Markey et al. [25] adapted a simple decision tree to the classi<sup>fi</sup>cation for lung cancer patients of clinical specimens as diseased/non-diseased. Zmazek et al. [39] used decision trees to predict radon gas concentration from other environmental factors, leading to a possible future earthquake prediction system. Chen et al. [11] used decision trees to design a new classi<sup>fi</sup>cation algorithm to classify multi-valued and multi-labeled data to predict in what tours a new customer of a tour company would be interested.

## 3. Proposed framework

The relationships among environments, B2C controls, and implementation are depicted in Fig. 1. The proposed framework of controls assessment is composed of two steps, as displayed in Fig. 2. The <sup>fi</sup>rst step is to utilize DEA with multiple inputs of B2C controls and multiple outputs of B2C implementation. DEA classi<sup>fi</sup>es DMUs, i.e., B2C adopters, into categories of ef<sup>fi</sup>cient and inef<sup>fi</sup>cient based on the resulting ef<sup>fi</sup>ciency scores. The second step applies decision trees where factors affecting B2C controls are composed of organization related factors, system related factors, and infrastructure related factors. Rules for the determination of the level of controls in ef<sup>fi</sup>cient adopters are determined.

## 3.1. Input of DEA model

The objective of B2C controls is to ensure that an organization achieves its goals through B2C applications. If users are not sure about the advantages of the system, B2C applications cannot be adopted and implemented; before B2C applications are implemented, management should demand assurance that adequate controls are in place. Thus, for B2C implementation, B2C controls should be designed ef<sup>fi</sup>ciently indicating that B2C should be considered as input of DEA model.

B2C controls have three parts, i.e., controls for system continuity, access controls, and communication controls (Table 1):

(1) Controls for system continuity

• Contingency planning controls (C1\_1)

• Backups of data and programs (C1\_2)

(2) Access controls

• Access controls for B2C applications (C2\_1)

• Controls of user activity in processing (C2\_2)

(3) Communication controls

• Detection controls for processing integrity (C3\_1)

• Correction controls for processing integrity (C3\_2)

• Prevention controls using message authentication and encryption in processing (C3\_3)

A questionnaire containing an extensive measure of controls was used to determine systematically the extent of controls. Measures for B2C controls are newly developed based on various sources [14,15,36] (see Appendix). The wording and interpretation of the <sup>fi</sup>rst version of the measures of B2C controls were reviewed through an interview with ten B2C application practitioners (one from each company); three IS professors made a <sup>fi</sup>nal review. Respondents answered questions about the extent to which they agreed or disagreed with each statement about controls. The answers were placed on a seven-point Likert-type scale (1=Totally disagree, 7=Totally agree). Average value was used for multi-item measure. The data used in validating the research model was gathered as part of a larger investigation concerning B2C controls.

## 3.2. Output of DEA model

Implementation of B2C applications has three dimensions: volume, sophistication, and information contents. The implementation success of B2C applications is de<sup>fi</sup>ned by the extent of implementation of B2C applications, as represented by volume, sophistication, and information contents. Volume in B2C applications corresponds to the percentage of an organization's transactions with consumers that are handled through B2C applications. Volume represents the proportion to which a <sup>fi</sup>rm's information exchange and processing are handled through B2C applications or need a parallel system to be performed.

Sophistication in B2C applications represents the level of sophistication in the use of different types of business functions that are handled through B2C applications; it is measured using seven-point Likert-type scales. IS sophistication indicates the extent of system usage in the organization, since each function set demands a separate system component. Sophistication in B2C applications also includes the extent to which an organization's business processes, i.e., its electronic payment system, customer database system, accounting system, inventory, and logistics system are integrated with B2C applications. This level of sophistication is measured using seven-point Likert-type scales.

![](/api/attachments/GDFJD5TF/fulltext/images/6ee3e31db208dc8bd00eebc5904f31a306d844791e3bee463fd0ad7528b5c39d.jpg)  
Fig. 1. System environments, B2C controls, and B2C implementation.

![](/api/attachments/GDFJD5TF/fulltext/images/6a93bb621c5e820eab40d58261075d81bff37c8c9ed28a9cd8ffddf6b63d9a67.jpg)  
Fig. 2. The assessment process of B2C controls using DEA and decision trees.

Information contents indicate the extent to which various information related to products and services is provided effectively to customers. This concept highlights how the organization's adoption of B2C applications improved the presentation of information. This includes the extent to which search and browse functions are implemented, and how product and service information is provided to facilitate information exchange and a greater volume of information output.

## 3.3. Factors affecting controls in decision trees

The recommendation of B2C controls can be conducted based on the relationship between system environments and B2C controls. Lee and Han [19] proposed factors affecting internal and external controls of interorganizational systems in the context of EDI. Using the theories of innovation adoption, some researchers have suggested various factors that have an effect on security adoption such as <sup>fi</sup>rm size, industry type, top management support, moral compatibility, peer in<sup>fl</sup>uence, and computing capacity [22]. Industry type and organizational use of IT were regarded as the two factors that in<sup>fl</sup>uence security adoptions [38]. Previous studies suggest that the business risk level is related to the current <sup>fi</sup>rm concern about security risk [18] and propose relationships among organizational factors, IS security measures, and IS security effectiveness [17]. The relationship between system environments and controls can be used to design controls [20].

Firm and attack characteristics of Internet security breaches such as <sup>fi</sup>rm size and type are factors affecting the market value of breached <sup>fi</sup>rms [2]. Achieving a balance among the organization, people, process and technology is crucial for effective information security [1].

Factors affecting B2C controls are composed of organization related factors, system related factors, and infrastructure related factors:

(1) Organization related factors

• Organizational size (E1) (number of employees)

• Type of industry (E2) (1=<sup>fi</sup>nancial <sup>fi</sup>rms, 2=retail <sup>fi</sup>rms, 3=information service providers)

B2C controls.

<table><tr><td>Controls class</td><td>Controls</td><td>Objectives</td><td>Description</td></tr><tr><td>Controls for system continuity</td><td>Contingency planning controls (C1_1)Backups of data and programs (C1_2)</td><td>Availability</td><td>Procedures for the recovery of information systems department&#x27;s services following unanticipated interruptions and the backup of critical resources.</td></tr><tr><td>Access controls</td><td>Access controls for B2C applications (C2_1)Controls of user activity in processing (C2_2)</td><td>Integrity,confidentiality</td><td>Procedures designed to ensure that access to data and programs is controlled and authenticated.</td></tr><tr><td>Communication controls</td><td>Detection controls for processing integrity (C3_1)Correction controls for processing integrity (C3_2)Prevention controls using message authentication and encryption in processing (C3_3)</td><td>Integrity,confidentiality</td><td>Procedures used by company to ensure security in inbound and outbound transactions. Procedures designed to ensure that error are detected and corrected during input of data and the process of data is authorized and appropriate during communication.</td></tr></table>

(2) System related factors

• Type of services provided (E3)

• Type of B2C applications (E4) (1= shopping malls 2=intermediaries, 3 =information service)

• Years after system adoption (E5)

• Type of information provided (E6) (1=text only, 2=text and graphics, 3=text, graphics, and pictures, 4=text, graphics, and pictures, audio, video)

(3) Infrastructure related factors

• IS infrastructure (E7) (Likert-type scale)

• IS expertise (E8) (Likert-type scale)

• Requirements for IS security (E9) (Likert-type scale)

Respondents chose one of the following states in order to determine type of services provided (E3):

(1) B2C applications that provide company information including some information about products or services.

(2) B2C applications that provide company information including some information (e.g., price details) about products or services. However, only conventional purchasing is possible.

(3) B2C applications that provide company information including some information (e.g., price details) about products or services and on-line purchasing facilities. However, billing occurs conventionally.

(4) B2C applications that provide company information including some information (e.g., price details) about products or services and on-line purchasing and billing facilities.

(5) B2C applications that provide information on speci<sup>fi</sup>c business purpose.

(6) B2C applications that play an intermediary role between various parties (e.g., consumers, business organizations).

(7) Others.

## 4. Data description

The main data collection method was a structured interview of respondents from B2C applications adopters. The data was collected as part of a larger study on B2C controls [20]. A questionnaire is used as a guide for thoroughly evaluating the status of B2C controls, system environments, and implementation of B2C applications. This will help develop a general understanding of where security needs improvement [4]. The sample data were <sup>fi</sup>lled with past cases that were collected from interviews and discussions with IS personnel. One or two IS staff members participated in the study. The sample data consisted of 120 companies that had successfully implemented B2C applications; data were drawn from a population of more than 2000 companies in Korea that have adopted B2C applications. The population covers a wide range of businesses that have initiated business-to-consumer e-commerce. The measures for variables were adapted from related literature; those measures for these variables are suggested in the Appendix. They were measured on seven-point Likert-type scales.

Since all of the control items were newly developed and their description is quite lengthy, it was important to know whether the questions could be appropriately answered by B2C application practitioners. Further, some questions could require the release of sensitive information about security and data integrity issues. These questions can be better answered by a structured interview than by any other data collection method. One or two members of the B2C applications staff or management took part in the interview. They were believed to have suf<sup>fi</sup>cient knowledge about their implementation. The data was collected as part of a larger investigation concerning B2C controls. The full questionnaire for variables is shown in the Appendix. One goal of this study was to analyze the differences in control ef<sup>fi</sup>ciency among <sup>fi</sup>rms in different industries. This study uses three groups of <sup>fi</sup>rms, i.e., <sup>fi</sup>nancial <sup>fi</sup>rms, retail <sup>fi</sup>rms, and information service providers. The number of adopters of B2C applications in each group is shown in Table 2. The total number of <sup>fi</sup>rms in the sample is 32 <sup>fi</sup>nancial <sup>fi</sup>rms, 59 retail <sup>fi</sup>rms, and 29 information service providers. DMU is an individual B2C applications adopter.

Table 2  
The industry distribution of companies adopting B2C applications.

<table><tr><td></td><td>Financial firms</td><td>Retail firms</td><td>Information service providers</td><td>Total</td></tr><tr><td>No. of companies</td><td>32</td><td>59</td><td>29</td><td>120</td></tr><tr><td>Percent</td><td>26.7</td><td>49.2</td><td>24.2</td><td>100</td></tr></table>

## 5. Results and discussions

## 5.1. Measurement properties of variables

Reliability and validity tests of controls and output variables was performed for the collected data. The Cronbach's alphas are shown in Table 3. All scales exceed 0.6, which shows moderate to high reliability. The content validity of the items was established through the adoption of constructs that have been validated by other researchers and through a pretest with 10 IS professionals. Further, extensive precautions were taken during the previous stages of development and pilot testing of the items. This study adapts the measures used by previous studies and pretests them with practitioners and experts to enhance the content validity of the instrument.

## 5.2. Test results of DEA model

Warwick-DEA software by Thanassoulis and Emrouznejad [35] was used to code the DEA model in the PC version. In order to analyze the ef<sup>fi</sup>ciency of <sup>fi</sup>rms adopting B2C controls, this study used radial improvement and constant returns as the means to scale the DEA model. This model attempts to provide a radial improvement in both inputs and outputs. DEA enabled a series of analyses of the differences in the ef<sup>fi</sup>ciency in various combinations of inputs and outputs and the amount of reduction needed in speci<sup>fi</sup>c modes of controls. DEA identi<sup>fi</sup>ed ef<sup>fi</sup>cient and inef<sup>fi</sup>cient B2C applications adopters when all seven variables of the B2C controls and three variables of the implementation of B2C applications and performance were used. Separate ef<sup>fi</sup>ciency analyses were applied for <sup>fi</sup>nancial <sup>fi</sup>rms, retail <sup>fi</sup>rms and information service providers. The percentage of ef<sup>fi</sup>cient <sup>fi</sup>rms and the average ef<sup>fi</sup>ciency are presented in Table 4. The average ef<sup>fi</sup>ciency of information service providers and retail <sup>fi</sup>rms is higher than that of <sup>fi</sup>nancial <sup>fi</sup>rms.

Measurement properties of factors and controls.

<table><tr><td>Controls</td><td>Items</td><td>Mean</td><td>Individual item reliability</td></tr><tr><td rowspan="3">Contingency planning controls (C1_1)</td><td>C1_1_1</td><td>5.3</td><td>0.89</td></tr><tr><td>C1_1_2</td><td>4.9</td><td></td></tr><tr><td>C1_1_3</td><td>4.8</td><td></td></tr><tr><td rowspan="2">Backups of data and programs (C1_2)</td><td>C1_2_1</td><td>5.2</td><td>0.72</td></tr><tr><td>C1_2_2</td><td>6.0</td><td></td></tr><tr><td rowspan="3">Access controls for B2C applications (C2_1)</td><td>C2_1_1</td><td>5.5</td><td>0.93</td></tr><tr><td>C2_1_2</td><td>5.0</td><td></td></tr><tr><td>C2_1_3</td><td>5.0</td><td></td></tr><tr><td rowspan="2">Controls of user activity in processing (C2_2)</td><td>C2_2_1</td><td>4.6</td><td>0.81</td></tr><tr><td>C2_2_2</td><td>4.7</td><td></td></tr><tr><td rowspan="3">Detection controls for processing integrity (C3_1)</td><td>C3_1_1</td><td>4.9</td><td>0.93</td></tr><tr><td>C3_1_2</td><td>4.9</td><td></td></tr><tr><td>C3_1_3</td><td>5.0</td><td></td></tr><tr><td rowspan="2">Correction controls for processing integrity (C3_2)</td><td>C3_2_1</td><td>4.8</td><td>0.80</td></tr><tr><td>C3_2_2</td><td>4.5</td><td></td></tr><tr><td rowspan="3">Prevention controls using message authentication and encryption in processing (C3_3)</td><td>C3_3_1</td><td>4.8</td><td>0.81</td></tr><tr><td>C3_3_2</td><td>3.8</td><td></td></tr><tr><td>C3_3_3</td><td>5.3</td><td></td></tr><tr><td rowspan="7">Sophistication (IMP2)</td><td>E12_1</td><td>4.0</td><td>0.89</td></tr><tr><td>E12_2</td><td>4.8</td><td></td></tr><tr><td>E12_3</td><td>2.9</td><td></td></tr><tr><td>E12_4</td><td>3.9</td><td></td></tr><tr><td>E12_5</td><td>4.5</td><td></td></tr><tr><td>E12_6</td><td>3.5</td><td></td></tr><tr><td>E12_7</td><td>3.4</td><td></td></tr><tr><td rowspan="4">Information contents (IMP3)</td><td>E13_1</td><td>5.4</td><td>0.87</td></tr><tr><td>E13_2</td><td>5.1</td><td></td></tr><tr><td>E13_3</td><td>5.0</td><td></td></tr><tr><td>E13_4</td><td>5.1</td><td></td></tr></table>

Table 4 DEA ef<sup>fi</sup>ciency results.

<table><tr><td>Type of firms</td><td>Financial firms</td><td>Retail firms</td><td>Information service providers</td></tr><tr><td>Number of efficient firms (percentage)</td><td>3 (9.4)</td><td>19 (32.2)</td><td>11 (37.9)</td></tr><tr><td>Number of inefficient firms (percentage)</td><td>29 (90.6)</td><td>40 (67.8)</td><td>18 (62.1)</td></tr><tr><td>Average efficiency</td><td>70.7</td><td>82.8</td><td>84.4</td></tr></table>

Table 5  
Average ef<sup>fi</sup>ciency in speci<sup>fi</sup>c class of input (number in parenthesis indicates the number of ef<sup>fi</sup>cient <sup>fi</sup>rms. Peer scaling method is contribution to targets).

<table><tr><td colspan="4">Input class</td></tr><tr><td>Type of firms</td><td>Financial firms</td><td>Retail firms</td><td>Information service providers</td></tr><tr><td>Controls for system continuity</td><td>64.2 (3)</td><td>73.8 (6)</td><td>73.6 (4)</td></tr><tr><td>Access controls</td><td>52.9 (0)</td><td>60.4 (9)</td><td>63.3 (4)</td></tr><tr><td>Communication controls</td><td>56.7 (1)</td><td>63.3 (11)</td><td>68.3 (6)</td></tr></table>

Table 5 shows the number of ef<sup>fi</sup>cient <sup>fi</sup>rms and the average ef<sup>fi</sup>ciency when speci<sup>fi</sup>c classes of input variables were used. Input variables were divided into three classes of controls, controls for system continuity, access controls, and communication controls. The output variable was the implementation of B2C applications (volume, sophistication, information contents). The average ef<sup>fi</sup>ciencies were produced when speci<sup>fi</sup>c variables of input and output were used (Table 6).

As the statistical signi<sup>fi</sup>cance of the differences among applications needs to be shown, the average ef<sup>fi</sup>ciencies were produced and the paired Wilkoxon Test was performed to see whether average ef<sup>fi</sup>ciency was different (Tables 7 and 8). The retail <sup>fi</sup>rms and information service providers develop B2C controls more ef<sup>fi</sup>ciently than <sup>fi</sup>nancial <sup>fi</sup>rms do. Controls for system continuity are developed more ef<sup>fi</sup>ciently than access controls and communication controls.

The results indicate that the level of controls in retail <sup>fi</sup>rms and information service providers is considered as more appropriate (or ef<sup>fi</sup>cient) than that in <sup>fi</sup>nancial <sup>fi</sup>rms. The extent of controls in <sup>fi</sup>nancial <sup>fi</sup>rms is more excessive than demanded by system requirements. The control requirements for <sup>fi</sup>nancial <sup>fi</sup>rms are generally stronger due to the nature of <sup>fi</sup>nancial transactions involving cash <sup>fl</sup>ow; the level of controls in <sup>fi</sup>nancial <sup>fi</sup>rms should be higher compared to other industries under the condition of the same extent of B2C implementation. Users in the sample, on the other hand, due to their belief in controls, are less concerned about the extent of controls in <sup>fi</sup>nancial <sup>fi</sup>rms than those in other industries. This lowers the required level and ef<sup>fi</sup>ciency of controls, which is the slack of controls compared to a required level of controls. It would be inef<sup>fi</sup>cient to implement expensive controls in the system if the sensitivity and vulnerability of the system were not perceived to be high. B2C controls should be appropriately implemented for the security and integrity of the system using limited resources and expertise. Thus the ef<sup>fi</sup>ciency is dependent on the nature of users' perception of controls and users' belief in controls; the greater the belief in controls, the lower the ef<sup>fi</sup>ciency of B2C controls.

Table 6  
Average ef<sup>fi</sup>ciency of <sup>fi</sup>rms (number in parenthesis indicates the number of ef<sup>fi</sup>cient <sup>fi</sup>rms).

<table><tr><td rowspan="2">Input class</td><td rowspan="2">Input variables</td><td rowspan="2">Output variable</td><td>Financial firms</td><td>Retail firms</td><td>Information service providers</td></tr><tr><td>Mean</td><td>Mean</td><td>Mean</td></tr><tr><td rowspan="6">Controls for system continuity</td><td rowspan="3">Contingency planning controls</td><td>Volume</td><td>28.2 (1)</td><td>35.1 (2)</td><td>36.5 (1)</td></tr><tr><td>Sophistication</td><td>54.3 (1)</td><td>50.8 (1)</td><td>49.5 (1)</td></tr><tr><td>Information contents</td><td>48.2 (0)</td><td>52.5 (1)</td><td>55.9 (2)</td></tr><tr><td rowspan="3">Backups of data and programs</td><td>Volume</td><td>21.5 (0)</td><td>31.7 (3)</td><td>29.1 (0)</td></tr><tr><td>Sophistication</td><td>45.8 (0)</td><td>47.0 (2)</td><td>43.9 (1)</td></tr><tr><td>Information contents</td><td>37.0 (0)</td><td>57.3 (3)</td><td>49.4 (0)</td></tr><tr><td rowspan="6">Access controls</td><td rowspan="3">Access controls for B2C applications</td><td>Volume</td><td>17.1 (0)</td><td>33.3 (3)</td><td>23.8 (0)</td></tr><tr><td>Sophistication</td><td>26.3 (0)</td><td>31.8 (3)</td><td>28.7 (0)</td></tr><tr><td>Information contents</td><td>16.9 (0)</td><td>28.8 (3)</td><td>24.4 (0)</td></tr><tr><td rowspan="3">Controls of user activity in processing</td><td>Volume</td><td>21.5 (0)</td><td>31.4 (2)</td><td>33.4 (1)</td></tr><tr><td>Sophistication</td><td>32.9 (0)</td><td>40.4 (2)</td><td>44.1 (1)</td></tr><tr><td>Information contents</td><td>28.9 (0)</td><td>33.3 (2)</td><td>44.1 (1)</td></tr><tr><td rowspan="9">Communication controls</td><td rowspan="3">Detection controls for processing integrity</td><td>Volume</td><td>17.5 (0)</td><td>32.8 (1)</td><td>36.0 (3)</td></tr><tr><td>Sophistication</td><td>35.8 (0)</td><td>31.1 (1)</td><td>37.5 (2)</td></tr><tr><td>Information contents</td><td>46.2 (1)</td><td>28.5 (1)</td><td>44.0 (1)</td></tr><tr><td rowspan="3">Correction controls for processing integrity</td><td>Volume</td><td>18.2 (0)</td><td>29.7 (1)</td><td>33.1 (2)</td></tr><tr><td>Sophistication</td><td>37.3 (0)</td><td>29.0 (2)</td><td>38.3 (1)</td></tr><tr><td>Information contents</td><td>21.2 (0)</td><td>23.3 (2)</td><td>27.2 (1)</td></tr><tr><td rowspan="3">Prevention controls using message authentication and encryption in processing</td><td>Volume</td><td>20.2 (0)</td><td>36.1 (2)</td><td>34.3 (1)</td></tr><tr><td>Sophistication</td><td>44.5 (1)</td><td>36.5 (1)</td><td>41.5 (1)</td></tr><tr><td>Information contents</td><td>33.5 (0)</td><td>32.5 (2)</td><td>40.8 (1)</td></tr></table>

Table 7  
Test of ef<sup>fi</sup>ciency difference between <sup>fi</sup>rms. Values in the parenthesis indicate t-value and signi<sup>fi</sup>cance $( ^ { * } p < 0 . 1 , ^ { * * } p < 0 . 0 5 ^ { * * * } p < 0 . 0 1 ) .$

<table><tr><td>Input Class</td><td>Financial firms-Retail firms</td><td>Financial firms-information service providers</td><td>Retail firms-information service providers</td></tr><tr><td>Controls for system continuity</td><td>-9.6 (-2.55, 0.013**)</td><td>-9.4 (-2.20, 0.032**)</td><td>0.2 (0.08, 0.936)</td></tr><tr><td>Access controls</td><td>-7.5 (-1.78, 0.079*)</td><td>-10.4 (-2.16, 0.036**)</td><td>-2.9 (-0.54, 0.591)</td></tr><tr><td>Communication controls</td><td>-6.6 (-1.52, 0.133)</td><td>-11.6 (-2.40, 0.020**)</td><td>-5 (-0.93, 0.355)</td></tr></table>

Table 8  
Test of ef<sup>fi</sup>ciency difference between controls. Values in the parenthesis indicate t-value and signi<sup>fi</sup>cance $( ^ { * } p < 0 . 1 , ^ { * * } p < 0 . 0 5 ^ { * * * } p < 0 . 0 1 ) .$

<table><tr><td>Input Class</td><td>Controls for system continuity-access controls</td><td>Controls for system continuity-communication controls</td><td>Access controls-communication controls</td></tr><tr><td>Financial firms</td><td>11.3 (5.00, 0.000*** )</td><td>7.5 (2.98, 0.006*** )</td><td>-3.8 (-2.55, 0.016** )</td></tr><tr><td>Retail firms</td><td>13.4 (4.35, 0.000*** )</td><td>10.6 (2.99, 0.004*** )</td><td>-2.9 (-1.51, 0.137)</td></tr><tr><td>Information service providers</td><td>10.3 (2.44, 0.021** )</td><td>5.3 (1.14, 0.263)</td><td>-5 (-1.46, 0.155)</td></tr></table>

In three industries, controls for system continuity are implemented more ef<sup>fi</sup>ciently than those for access. Communication controls are developed more ef<sup>fi</sup>ciently than access controls in <sup>fi</sup>nancial <sup>fi</sup>rms while controls for system continuity are implemented more ef<sup>fi</sup>ciently than communication controls in <sup>fi</sup>nancial and retail <sup>fi</sup>rms. Thus, in <sup>fi</sup>nancial <sup>fi</sup>rms, controls for system continuity, communication controls, and access controls, in descending order, are ef<sup>fi</sup>ciently established in B2C applications. This indicates the relative importance of the three classes of controls in <sup>fi</sup>nancial <sup>fi</sup>rms. The implementation of controls for system continuity is ef<sup>fi</sup>cient due to the high perceived importance placed on these controls. Controls for system continuity, such as contingency planning and backups of data and programs, are the most crucial in <sup>fi</sup>nancial <sup>fi</sup>rms compared to other <sup>fi</sup>rms. In Internet based <sup>fi</sup>nancial applications such as Internet banking and cyber stock trading, communication controls are perceived to be more important than application controls due to an increased concern over security issues, which leads to the investment of more resources in communication controls such as detection, correction, and prevention controls in communication networks.

Table 9 shows the slack of controls for the 32 <sup>fi</sup>nancial <sup>fi</sup>rms (the number of ef<sup>fi</sup>cient <sup>fi</sup>nancial <sup>fi</sup>rms is three). The inef<sup>fi</sup>ciency of each con<sup>fi</sup>guration of controls is provided in Table 9. The amount of decrease in inputs shows potential improvements of the inef<sup>fi</sup>cient DMUs without worsening the other inputs or outputs. Every company can identify the level of relative amount of reduction in each component of controls in order to make the control system ef<sup>fi</sup>cient. As an example, the needed reduction of controls is greater than three for <sup>fi</sup>rm 80 in controls, C2\_1, C2\_2, C3\_1, C3\_2 (see Table 1 for the explanation of the notation of controls). For Firm 96, C2\_1, C2\_2, C3\_1 need to be reduced more than three. The usage level for these controls should be reduced to a greater extent than that for the other controls. Firm 95 requires a reduction of less than 1.0 in every input variable except C1\_2. On average, DEA analysis shows that the controls for system continuity require less reduction of the usage level than access controls and communication controls do. B2C application adopters should reduce the usage level of access and communication controls more than controls for system continuity.

The sources of inef<sup>fi</sup>ciency may be identi<sup>fi</sup>ed to provide a direction for controls assessment. Internal auditors should be especially interest ed in identifying the speci<sup>fi</sup>c mode or component of controls that adversely affect implementation of B2C applications or performance. Ef<sup>fi</sup>ciency of B2C applications systems can be increased by reducing the use of inef<sup>fi</sup>cient controls and selecting the resource-minimizing mix.

Table 9  
Slack analysis of controls for <sup>fi</sup>nancial <sup>fi</sup>rms. Input: B2C controls, output: B2C implementation. Firms (DMUs) are ordered in ascending order of ef<sup>fi</sup>ciency.

<table><tr><td>Firm</td><td>Efficiency</td><td>Contingency planning controls</td><td>Backups of data and programs</td><td>Access controls for B2C applications</td><td>Controls of user activity in processing</td><td>Detection controls for processing integrity</td><td>Correction controls for processing integrity</td><td>Prevention controls using message authentication and encryption in processing</td></tr><tr><td>Firm 71</td><td>41.76</td><td>4.1</td><td>4.1</td><td>5.3</td><td>4.6</td><td>4.1</td><td>5.7</td><td>4.2</td></tr><tr><td>Firm 68</td><td>42.88</td><td>4</td><td>4.4</td><td>5.2</td><td>4.5</td><td>4</td><td>2.8</td><td>4.1</td></tr><tr><td>Firm 66</td><td>50.31</td><td>2.6</td><td>4.3</td><td>5.3</td><td>4.3</td><td>3.5</td><td>5.2</td><td>3.9</td></tr><tr><td>Firm 80</td><td>56.2</td><td>2.6</td><td>2.6</td><td>3.7</td><td>3.4</td><td>3.1</td><td>3.3</td><td>2.9</td></tr><tr><td>Firm 96</td><td>56.97</td><td>2.7</td><td>2.8</td><td>3.4</td><td>3</td><td>3.8</td><td>2.4</td><td>3.1</td></tr><tr><td>Firm 75</td><td>60.66</td><td>2.4</td><td>2.4</td><td>3.4</td><td>2</td><td>2.1</td><td>3.5</td><td>2.3</td></tr><tr><td>Firm 62</td><td>61.03</td><td>2</td><td>2.5</td><td>3.9</td><td>4.3</td><td>3.5</td><td>3.7</td><td>3.3</td></tr><tr><td>Firm 110</td><td>61.79</td><td>3.4</td><td>2.7</td><td>3.8</td><td>3.3</td><td>2.7</td><td>1.5</td><td>1.8</td></tr><tr><td>Firm 63</td><td>62.63</td><td>2.2</td><td>2.8</td><td>1.4</td><td>1.7</td><td>2.8</td><td>4</td><td>2.2</td></tr><tr><td>Firm 74</td><td>62.88</td><td>1.9</td><td>3.6</td><td>4.3</td><td>3.6</td><td>2.6</td><td>4.5</td><td>3.1</td></tr><tr><td>Firm 87</td><td>63.59</td><td>2.2</td><td>2.5</td><td>2.5</td><td>2.2</td><td>2.1</td><td>2.3</td><td>3.1</td></tr><tr><td>Firm 73</td><td>63.95</td><td>1.9</td><td>2.3</td><td>2.1</td><td>1.8</td><td>2.7</td><td>3.7</td><td>2.4</td></tr><tr><td>Firm 88</td><td>64.34</td><td>2.2</td><td>2.1</td><td>3.7</td><td>2.6</td><td>2.6</td><td>2</td><td>1.7</td></tr><tr><td>Firm 77</td><td>64.96</td><td>2.6</td><td>2.5</td><td>3.5</td><td>1.5</td><td>2.9</td><td>2.2</td><td>1.7</td></tr><tr><td>Firm 76</td><td>65.04</td><td>2.2</td><td>2.1</td><td>1.9</td><td>1.4</td><td>2.4</td><td>3.2</td><td>1.3</td></tr><tr><td>Firm 89</td><td>65.45</td><td>1.8</td><td>2.1</td><td>2.1</td><td>2.8</td><td>2.1</td><td>2.3</td><td>2.3</td></tr><tr><td>Firm 78</td><td>68.69</td><td>1.2</td><td>2.2</td><td>2</td><td>2.2</td><td>1.9</td><td>3.6</td><td>2.5</td></tr><tr><td>Firm 70</td><td>69.65</td><td>2.1</td><td>2</td><td>3.1</td><td>2.4</td><td>1.8</td><td>1.8</td><td>2.1</td></tr><tr><td>Firm 107</td><td>70.46</td><td>1.8</td><td>1.9</td><td>2.1</td><td>2.7</td><td>1.8</td><td>2.5</td><td>2.9</td></tr><tr><td>Firm 82</td><td>71.09</td><td>1.4</td><td>1.3</td><td>1.7</td><td>1.4</td><td>1.9</td><td>1.3</td><td>2.2</td></tr><tr><td>Firm 83</td><td>72.39</td><td>1.6</td><td>1.8</td><td>2.6</td><td>3.2</td><td>2</td><td>1.5</td><td>2.8</td></tr><tr><td>Firm 44</td><td>74.59</td><td>1.8</td><td>1.5</td><td>2.1</td><td>1.3</td><td>1.8</td><td>1.9</td><td>1.3</td></tr><tr><td>Firm 81</td><td>74.98</td><td>1</td><td>1.3</td><td>2.2</td><td>2.7</td><td>1.9</td><td>2</td><td>1.8</td></tr><tr><td>Firm 67</td><td>79.4</td><td>1.1</td><td>1.2</td><td>1.9</td><td>0.7</td><td>3.5</td><td>4.2</td><td>1</td></tr><tr><td>Firm 86</td><td>80.52</td><td>1.7</td><td>0.9</td><td>0.9</td><td>1.8</td><td>0.8</td><td>0.6</td><td>1.3</td></tr><tr><td>Firm 69</td><td>83.65</td><td>2.1</td><td>0.9</td><td>2.3</td><td>2.5</td><td>3</td><td>0.3</td><td>3.1</td></tr><tr><td>Firm 104</td><td>87.84</td><td>0.8</td><td>1.3</td><td>0.9</td><td>0.8</td><td>1.3</td><td>0.8</td><td>1.6</td></tr><tr><td>Firm 95</td><td>89.48</td><td>0.5</td><td>1.5</td><td>0.6</td><td>0.8</td><td>0.6</td><td>0.6</td><td>0.6</td></tr><tr><td>Firm 91</td><td>94.73</td><td>0.3</td><td>0.3</td><td>1.3</td><td>1.5</td><td>1.8</td><td>1.1</td><td>2.8</td></tr><tr><td>Firm 79</td><td>100</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Firm 90</td><td>100</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Firm 101</td><td>100</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr></table>

## 5.3. Test results of decision trees model

A popular tree building algorithm is Quinlan's ID3 (Iterative Dichotomizer 3) [29]. The tree building process starts by selecting an attribute to place at the root node and at each succeeding level the subsets generated by preceding levels are further partitioned until the process reaches a relatively homogenous terminal node or leaf node consisting of a majority of the examples in a single class. An extension of ID3 includes Quinlan's C4.5 and C5, which model both discrete and continuous variables [29]. Additional modi<sup>fi</sup>cation includes handling of missing values, pruning of the decision tree, and rule derivation. This study used a C4.5 learning scheme implemented using Visual Basic in an Excel spreadsheet.

There are three criteria for stopping growing the tree and splitting a node: minimum node size, maximum purity (% of records in the node with majority class), and maximum depth. This study sets these criteria as 5 records, 100%, and 20, respectively. This setting allows the suf<sup>fi</sup>cient training of the decision tree. The training of decision trees using different criteria does not greatly affect the classi<sup>fi</sup>cation performance of the decision tree. Further, the purpose of this study is to use a decision tree and extract rules in controls recommendation rather than to obtain a high classi<sup>fi</sup>cation ratio.

Two responses are excluded from further analysis because they consist of minority group in the categories of type of services provided and it is dif<sup>fi</sup>cult to train decision trees with these responses. Numbers of training data and test data are 108 and 10, respectively. Test data are randomly selected from the sample.

Table 10 shows the rules for tree A and B: 1) tree A is to determine ef<sup>fi</sup>cient <sup>fi</sup>rms; 2) tree B is to recommend the level of B2C controls (contingency planning controls). Tree A has 42 nodes, 28 leaf nodes, and seven levels. In tree A, percent of misclassi<sup>fi</sup>ed is 7.6% for training data, and 38.5% for test data. Tree B has 39 nodes, 24 leaf nodes, and 10 levels. Tree B has 10.2 and 40.0% of misclassi<sup>fi</sup>cation for training data and test data, respectively.

Three measures of rules are suggested in Table 10: Support, Confidence, and Capture. Support is the percent of training data for which the Left Hand Side (LHS) of the Rule is true. If for an observation the LHS of the rule is true, the rule applies for that observation. This measures how widely applicable the rule is. Confidence is the percent of data out of the training data for which the (LHS) of the Rule is true for which the Right Hand side is also true. This means the percent of data for which the rule is true out of the data in which the rule applies. This measures the accuracy of the rule. 1 minus Confidence is equal to the percent of the miss classi<sup>fi</sup>cation. Capture is the percent of cases correctly captured by this rule out of the data that satis<sup>fi</sup>es the Right Hand Side of Rule (RHS). This is more of a re<sup>fl</sup>ection of the structure of the problem. A rule with Capture close to 100% indicates that the rule has been able to capture that part of the predictor space very well. If there is a rule with Capture close to 100%, that means, in the predictor space, all observations with this class sit close to each other.

For example, consider a rule: IF IS expertise ≥ 5.8 and IS infrastructureb6 then Contingency planning controls = 3. In the context of the above rule, the quality metrics are explained as follows. There are 108 cases in the training data, out of which 54 cases satisfy the Right Hand Side of Rule (RHS) (i.e., contingency planning controls=3). The above rule applies to four cases, and out of these, four cases satisfy RHS. Then, Support is 3.7% (=4/108) and Confidence is 100% (=4/4). Capture is 7.4% (=4/54).

An illustrative example of tree B is shown in Fig. 3. The node characteristics are presented in Table 11. For example, the recommendation from Node 17 in Fig. 3 can be represented by the following rule: IF IS infrastructureb4.17 and type of services provided=7 and organizational requirements for IS security≥4.75 then contingency planning controls=2. There are 108 cases in the training data, out of which 45 cases satisfy the Right Hand Side of Rule (RHS) (i.e., Contingency planning controls=2). The above rule applies to eight cases, and out of these, seven cases satisfy RHS. Then, Support is 7.4% (=8/108) and Confidence is 87.5% (=7/8). Capture is 15.6% (=7/45). Percent of misclassi<sup>fi</sup>cations is 1 minus Confidence or 12.5% (100−87.5%). Nodes 12 and 13 and have the greatest Confidence, i.e., 100%. Among these three nodes, Node 12 has the greatest Support and Capture. This indicates that the recommendation based on Node 12 is the most widely applicable and has the greatest accuracy. Further, in order to predict the level 1 of the contingency planning controls, it is appropriate to make a recommendation based on Node 12 as this node predicts 44.4% of the data that has level 1 of contingency planning controls.

Suppose there is a new case that has the following values of factors: organizational size (E1)=30, type of industry (E2)=3, type of services

Table 10  
Rules generated from decision tree A and B. 1) Tree A is to determine ef<sup>fi</sup>cient <sup>fi</sup>rms. 2) Tree B is to recommend the level of B2C controls (contingency planning controls).

<table><tr><td>Trees</td><td>Rules</td><td>Contents</td><td>Support (%)</td><td>Confidence (%)</td><td>Capture (%)</td></tr><tr><td rowspan="12">Tree A</td><td>Rule 1</td><td>If type of services provided = 2 then not efficient</td><td>2.9</td><td>66.7</td><td>2.6</td></tr><tr><td>Rule 2</td><td>If requirements for IS security ≥ 6.25 then not Efficient</td><td>51.4</td><td>83.3</td><td>57.7</td></tr><tr><td>Rule 3</td><td>If type of information provided = 2 then not efficient</td><td>13.3</td><td>92.9</td><td>16.7</td></tr><tr><td>Rule 4</td><td>If type of information provided = 3 Then Not efficient</td><td>51.4</td><td>74.1</td><td>51.3</td></tr><tr><td>Rule 5</td><td>If type of services provided = 6 then not efficient</td><td>6.7</td><td>57.1</td><td>5.1</td></tr><tr><td>Rule 6</td><td>If type of services provided = 7 then not efficient</td><td>30.5</td><td>90.6</td><td>37.2</td></tr><tr><td>Rule 7</td><td>If organizational size &lt; 8 then efficient</td><td>6.7</td><td>71.4</td><td>18.5</td></tr><tr><td>Rule 8</td><td>If organizational size ≥ 8 then not efficient</td><td>93.3</td><td>77.6</td><td>97.4</td></tr><tr><td>Rule 9</td><td>If organizational size &lt; 800 then not efficient</td><td>83.8</td><td>71.6</td><td>80.8</td></tr><tr><td>Rule 10</td><td>If organizational size ≥ 800 then not efficient</td><td>16.2</td><td>88.2</td><td>19.2</td></tr><tr><td>Rule 11</td><td>If IS expertise ≥ 3 then not efficient</td><td>82.9</td><td>77.0</td><td>85.9</td></tr><tr><td>Rule 12</td><td>If organizational size ≥ 70 then not efficient</td><td>50.5</td><td>88.7</td><td>60.3</td></tr><tr><td rowspan="10">Tree B</td><td>Rule 1</td><td>If IS infrastructure ≥ 6 then contingency planning controls = 3</td><td>22.2</td><td>95.8</td><td>42.6</td></tr><tr><td>Rule 2</td><td>If IS expertise ≥ 5.8 and IS infrastructure &lt; 6 then contingency planning controls = 3</td><td>3.7</td><td>100.0</td><td>7.4</td></tr><tr><td>Rule 3</td><td>If IS infrastructure &lt; 4.17 then contingency planning controls = 2</td><td>29.6</td><td>59.4</td><td>42.2</td></tr><tr><td>Rule 4</td><td>IF years after system adoption ≥ 2.5 then contingency planning controls = 3</td><td>41.7</td><td>66.7</td><td>55.6</td></tr><tr><td>Rule 5</td><td>If IS infrastructure &lt; 5 then contingency planning controls = 2</td><td>47.2</td><td>58.8</td><td>66.7</td></tr><tr><td>Rule 6</td><td>If type of information provided = 2 then contingency planning controls = 3</td><td>11.1</td><td>58.3</td><td>13.0</td></tr><tr><td>Rule 7</td><td>If type of information provided = 3 then contingency planning controls = 2</td><td>53.7</td><td>51.7</td><td>66.7</td></tr><tr><td>Rule 8</td><td>If type of services provided = 5 then contingency planning controls = 3</td><td>49.1</td><td>52.8</td><td>51.9</td></tr><tr><td>Rule 9</td><td>If IS infrastructure ≥ 5 then contingency planning controls = 3</td><td>52.8</td><td>71.9</td><td>75.9</td></tr><tr><td>Rule 10</td><td>If organizational size ≥ 78 then contingency planning controls = 3</td><td>46.3</td><td>64.0</td><td>59.3</td></tr></table>

Tree A: tree for determination of ef<sup>fi</sup>cient <sup>fi</sup>rms, # of nodes=42, # of leaf nodes=28, and number of levels=7. % of misclassi<sup>fi</sup>ed=7.6% (training data), 38.5% (test data).  
Tree B: tree for recommendation of controls level, # of nodes=39, # of leaf nodes=24, number of levels=10.  
% of misclassi<sup>fi</sup>ed=10.2% (training data), 40.0% (test data).

![](/api/attachments/GDFJD5TF/fulltext/images/a0f2b603dcd6fbdb8022ab723f104009a84ddd8e31276da5499ef1fba9663805.jpg)  
Fig. 3. An illustrative example of decision trees for recommendation of controls level. NA: not applicable.

provided (E3)=7, type of B2C applications (E4)=3, years after system adoption (E5)=2, type of information provided (E6)=4, IS infrastructure (E7)=4, IS expertise (E8)=5.2, and requirements for IS security (E9)=3.5. Then, the recommended level of contingency planning controls is three using the new input case. Auditors or security administrators can use decision trees to suggest the required level of controls in their organization using decision trees.

## 6. Conclusions and implications

Security breaches of web-based, B2C applications, which applications are often integrated with mission-critical <sup>fi</sup>nancial reporting applications in enterprise resource planning (ERP), are increasing at an alarming rate. Assurance that the controls are in place and effective is important, and this assurance can be given through control assessment.

Table 11  
The characteristics of nodes in decision tree of Fig. 3. NA: not applicable.

<table><tr><td>Nodes</td><td>Percent of miss classification</td><td>Number of records</td><td>Percent of records having: contingency planning controls = 1</td><td>Percent of records having: contingency planning controls = 2</td><td>Percent of records having: contingency planning controls = 3</td></tr><tr><td>Node 1</td><td>46.4</td><td>84</td><td>9.5</td><td>53.6</td><td>36.9</td></tr><tr><td>Node 3</td><td>40.6</td><td>32</td><td>25.0</td><td>59.4</td><td>15.6</td></tr><tr><td>Node 4</td><td>50.0</td><td>52</td><td>0</td><td>50.0</td><td>50.0</td></tr><tr><td>Node 5</td><td>50.0</td><td>2</td><td>50.0</td><td>50.0</td><td>0</td></tr><tr><td>Node 6</td><td>33.3</td><td>6</td><td>66.7</td><td>33.3</td><td>0</td></tr><tr><td>Node 7</td><td>40.0</td><td>15</td><td>13.3</td><td>60.0</td><td>26.7</td></tr><tr><td>Node 8</td><td>22,2</td><td>9</td><td>11.1</td><td>77.8</td><td>11.1</td></tr><tr><td>Node 9</td><td>NA</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Node 12</td><td>0</td><td>4</td><td>100</td><td>0</td><td>0</td></tr><tr><td>Node 13</td><td>0</td><td>2</td><td>0</td><td>100</td><td>0</td></tr><tr><td>Node 16</td><td>0</td><td>1</td><td>0</td><td>0</td><td>100</td></tr><tr><td>Node 17</td><td>12.5</td><td>8</td><td>12.5</td><td>87.5</td><td>0</td></tr></table>

Firms, however, cannot install every possible control, as such a strategy is not economically feasible. Considering the ef<sup>fi</sup>ciency of controls, the extent of B2C controls can be adjusted in relation to the extent of the implementation of B2C applications. Then, system environments can be examined in order to recommend the appropriate level of controls. This study conducts a controls assessment in two parts: determination of ef<sup>fi</sup>ciency of B2C controls using DEA and recommendation of level of controls using decision trees. The proposed methods can result in a greater return on the auditor's time and expense because the company need not request business management to supply unnecessary supporting documentation. After the analysis is completed for the <sup>fi</sup>rst time, future assessments of controls will need much less effort as the completed questionnaire establishes a baseline.

DEA can validate the ef<sup>fi</sup>ciency of controls for the implementation of B2C applications. The scienti<sup>fi</sup>cally and rationally applied approach may lessen the burden of retro<sup>fi</sup>tting security measures, saving resources in areas of auditing and security management. DEA can help identify <sup>fi</sup>rms adopting controls ef<sup>fi</sup>ciently and can signal inef<sup>fi</sup>cient controls that need to be reduced to be ef<sup>fi</sup>cient. The study further investigated the ef<sup>fi</sup>ciency differences among industries and control classes, performing multiindustry and multi-class controls investigation to determine the ef<sup>fi</sup>ciency of B2C controls. The results of the investigation of the DEA model indicate that retail <sup>fi</sup>rms and information service providers implement B2C controls more ef<sup>fi</sup>ciently than <sup>fi</sup>nancial <sup>fi</sup>rms do. Controls for system continuity are implemented more ef<sup>fi</sup>ciently than access controls. In <sup>fi</sup>nancial <sup>fi</sup>rms, controls for system continuity, communication controls, and access controls, in a descending order, are ef<sup>fi</sup>ciently established in B2C applications. Decision trees support auditors by creating two kinds of rules, i.e., rules for determining <sup>fi</sup>rms that ef<sup>fi</sup>ciently implemented B2C controls and rules for recommending the level of B2C controls.

This study of the ef<sup>fi</sup>ciency of B2C controls has signi<sup>fi</sup>cant implications for researchers and practitioners. As studies that examine ef<sup>fi</sup>ciency in controls and security have been lacking, this study provides insight to researchers by suggesting an overall normative approach to the evaluation and design of controls in terms of ef<sup>fi</sup>ciency analysis of controls and decision analysis framework to evaluate the <sup>fi</sup>t between system environments and controls. This study does not evaluate the impact of controls on risk reduction, and the relation between risks and controls of B2C applications should be further examined in order to enhance our understanding of B2C control strategy and to mitigate security risks.

Further, the study results may help practitioners such as auditors and security administrators by providing a systematic approach for the determination of the mode and level of controls in the process of implementation of B2C applications. Every company can determine the relative amount of reduction in each component of controls in order to make the control system ef<sup>fi</sup>cient. Auditors can align controls with system environments and implementation of B2C applications. This enables the control strategy to achieve a balance with organization, system, infrastructure related factors, and utilization of B2C applications. Considering the security incidences, limited internal audit resources, and legal requirements such as the Sarbanes-Oxley Act, the proposed methods will help establish action plans to de<sup>fi</sup>ne what controls must be introduced, enhanced or removed. The action plan is demanded for controls that are rated as limited, de<sup>fi</sup>cient or excess.

Actual and objective measures of information security performance such as data loss and number of fraudulent transactions are good output variables. At this time, the study sample does not include those variables. It will be better to include them in the sample in a future study.

## Appendix

Respondents answer the extent to which they agree or disagree with each statement about controls. The seven-point Likert-type scales are used.

## 1. System environments

1) IS infrastructure (E7)

Our <sup>fi</sup>rm has a good telecommunications infrastructure. Or <sup>fi</sup>rm shares our databases for various applications, rather than having a separate database for each application.

There is integrated IS applications encompassing different functional areas.

Our <sup>fi</sup>rm manages <sup>fi</sup>rm-wide communication network services.

Our <sup>fi</sup>rm maintains large-scale data processing facilities. Our <sup>fi</sup>rm manages <sup>fi</sup>rm-wide messaging services.

2) IS expertise (E8)

The employees are generally aware of the functions of advanced technology and methodology in IS (e.g., Internet, telecommunications, enterprise resource planning, knowledge management).

There exist many experts on advanced technology and methodology in IS.

The employees' understanding of advanced technology and methodology in IS is very good compared with other <sup>fi</sup>rms in the same industry.

The employees are well trained in advanced technology and methodology.

The employees are well educated in advanced technology and methodology in their school days.

3) Requirement for IS security (E9)

The vulnerabilities can always occur from the lack of security in internal application system.

The vulnerabilities can always occur from the lack of security in communication system connected with external networks.

The vulnerabilities can always occur by the advertent or inadvertent misbehaviors by employees.

The vulnerabilities can always occur by the advertent or inadvertent misbehaviors by persons that are not employees of our <sup>fi</sup>rm.

The responsibility related to IS security is very important, as it affects the organizational performance.

The loyalty of customers is greatly affected by the incidents of security violations.

Security control procedures should be applied strictly for overall system performance.

System performance is very sensitive to errors and system failures.

2. B2C controls

1) Contingency planning controls (C1\_1)

Our <sup>fi</sup>rm maintains appropriate contingency planning procedures to ensure system and network continuity in a timely fashion.

The procedures for error logging, incident reporting are appropriately maintained for correction of errors.

The timely review procedure exists to ensure that the unauthorized processing is followed up.

2) Backups of data and programs (C1\_2)

Our <sup>fi</sup>rm maintains the procedures for recording messages for the correction of errors and reprocessing of corrected messages.

The backups of the critical data and program <sup>fi</sup>les are always maintained.

3) Access controls for B2C applications (C2\_1)

System login is appropriately controlled by access control procedures such as passwords.

Access to sensitive <sup>fi</sup>les and programs is effectively controlled using access controls software.

Automated authentication procedures embedded in system effectively ascertain the identity of system users.

4) Controls of user activity in processing (C2\_2)

The content of user activities is appropriately authenticated while they are using system.

The security violations of users automatically lead to the suspension of system access (e.g., the disability of terminal, microcomputer, or data entry device activity).

5) Detection controls for processing integrity (C3\_1)

Transaction messages are checked for duplication, omission or inaccuracies before the messages are processed in the application.

Transaction messages are checked for duplication, omission or inaccuracies after they are generated and before being transmitted.

Embedded software checks correctness of data <sup>fi</sup>elds before received messages are processed in internal applications.

6) Correction controls for processing integrity (C3\_2)

Our <sup>fi</sup>rm retransmits messages if the messages are omitted, duplicated, or inaccurate.

Our <sup>fi</sup>rm maintains network software that helps promptly correct corrupt and improper transaction messages.

7) Prevention controls using message authentication and encryption in processing (C3\_3)

The receiver or sender of transaction messages is appropriately authenticated after the messages are generated or received.

Our <sup>fi</sup>rm attaches message identi<sup>fi</sup>cation codes or digital signatures to effectively authenticate the messages.

High risk data (e.g., customer credit card number, password) are encrypted using the encryption tools of our <sup>fi</sup>rm during their transmission.

3. B2C implementation

1) Volume (IMP1)

The proportion (%) that a company uses B2C applications. Business transaction can be processed using other complementary means such as e-mail, fax, or phone. It is measured as the proportion that a <sup>fi</sup>rm's information exchange and processing are handled through B2C applications.

2) Sophistication (IMP2)

B2C applications provide sophisticated authentication service (e.g., digital signature) for the security of transaction data.

It is very easy to order products.

B2C applications greatly provide video image in interface display.

Transaction data can be directly processed within four applications (payment system, customer database system, accounting system, logistics and inventory system) without human intervention.

3) Information contents (IMP3)

B2C applications provide sophisticated product browse function.

B2C applications provide sophisticated functions that search products/services using various conditions.

B2C applications provide much company information.

B2C applications provide much information concerning maintenance and use of products/service.

## References

[1] K. Anderson, Business model for information security, Information Systems Control Journal 3 (2008) 51–52.

[2] F.K. Andoh-Baidoo, K.-M. Osei-Bryson, Exploring the characteristics of Internet security breaches that impact the market value of breached <sup>fi</sup>rms, Expert Systems With Applications 32 (2007) 703–725.

[3] A. Bakman, If compliance is son critical, why are we still failing audits? Information Systems Control Journal 5 (2007) 37–40.

[4] S. Bakshi, Control self-assessment for information and related technology Information Systems Control Journal 1 (2004) 55–62.

[5] A. Bernstein, F. Provost, An intelligent assistant for the knowledge discovery process, New York University – Leonard Stern School of Business, Center for Digital Economy Research, CeDER Working Paper # IS-01-01, 2001.

[6] B. Busta, J. Strong, Expert consensus on the top IT controls for a small business, Information Systems Control Journal 6 (2006) 22–24.

[7] H. Cavusoglu, B. Mishra, S. Raghunathan, A model for evaluating IT security investments, Communications of the ACM 47 (7) (2004) 87–92.

[8] D. Çelebi, D. Bayraktar, An integrated neural network and data envelopment analysis for supplier evaluation under incomplete information, Expert System with Applications 35 (4) (2008) 1698–1710.

[9] M.J. Cerullo, V. Cerullo, Threat assessment and security measures justi<sup>fi</sup>cation for advanced IT networks, Information Systems Control Journal 1 (2005) 35–43.

[10] A. Charnes, W. Cooper, A. Lewin, L. Seiford, Data Envelopment Analysis Theory, Methodology and Applications, Kluwer Academic Publishers, London, 1995.

[11] Y.L. Chen, C.L. Hsu, S.C. Chou, Constructing amulti-valued and multi-labeled decision tree, Expert Systems with Applications 25 (2) (2003) 199–209.

[12] T. Endou, Q.F. Zhao, Generation of comprehensible decision trees through evolution of training data, Proceedings of IEEE congress on evolutionary computation (CEC'2002), 2002, pp. 1221–1225.

[13] L. Gordon, M. Loeb, The economics of information security investment, ACM Transactions on IS Security 5 (4) (2002) 438–457.

[14] [14]ISACA, EDI Control Guide, EDI Council of Australia, Sydney Chapter, Information Systems Audit and Control Association, 1990.

[15] [15]ISACA, COBIT 4.1, Information Systems Audit and Control Association, www. isaca.org, 2008

[16] K. Jansen, Siebel's ebusiness application and controls, Information Systems Control Journal 2 (2002) 43–50.

[17] A. Kankanhalli, H.H. Teo, B.C.Y. Tan, K.K. Wei, An integrative study of information systems security effectiveness, International Journal of Information Management 23 (2003) 139–154.

[18] A.G. Kotulic, J.G. Clark, Why there aren't more information security research studies, Information & Management 41 (2004) 597–607.

[19] S. Lee L. Han The impact of organizational contexts on EDL controls International Journal of Accounting Information Systems 1 (2000) 153–177.

[20] S. Lee, K. Kim, Using case based reasoning for the design of controls for Internetbased information systems, Expert Systems With Applications 36 (3) (2009) 5582–5591.

[21] S. Lee, K. Lee, I. Kang, Ef<sup>fi</sup>ciency analysis of controls in EDI applications, Information & Management 42 (3) (2005) 425–439.

[22] Y. Lee, K.A. Kozar, Investigating factors affecting the adoption of anti-spyware systems, Communication of the ACM 48 (8) (2005) 72–78.

[23] M.A. Mahmood, K.J. Pettingell, A.I. Shaskevich, Measuring productivity of software projects: a data envelopment analysis approach, Decision Sciences 27 (1) (1996) 57–80.

[24] M. Mannino, S.N. Hong, I.J. Choi Ef<sup>fi</sup>ciency, Evaluation of data warehouse operations, Decision Support Systems 44 (4) (2008) 883–898.

[25] M.K. Markey, G.D. Tourassi, C.E. Floyd, Decision tree classi<sup>fi</sup>cation of proteins identi<sup>fi</sup>ed by mass spectrometry of blood serum samples from people with and without lung cancer, Proteomics 3 (2003) 1678–1679.

[26] J. Ott, A. MacLeod, K.M. Fan, Computer-assisted audit techniques: value of data mining for corporate auditors, Information Systems Control Journal 3 (2008) 45–48.

[27] M. Pareek, Optimizing controls to test as part of a risk-based audit strategy, Information Systems Control Journal 2 (2006) 39–41.

[28] M. Pareek, Automating controls, Information Systems Control Journal 3 (2007) 45–47.

[29] J.R. Quinlan, C4.5: Programs for Machine Learning, Morgan Kaufman, San Mateo CA, 1992.

[30] S. Samoilenko, K.-M. Osei-Bryson, Increasing the discriminatory power of DEA in the presence of the sample heterogeneity with cluster analysis and decision trees, Expert Systems with Applications 34 (2) (2008) 1568–1581

[31] H. Seol, J. Choi, G. Park, Y. Park, A framework for benchmarking service process using data envelopment analysis and decision tree, Expert Systems with Applications 32 (2) (2007) 432–440.

[32] C. Serrano-Cinca, Y. Fuertes-Callén, C. Mar-Molinero, Measuring DEA ef<sup>fi</sup>ciency in Internet companies, Decision Support Systems 38 (4) (2005) 557–573.

[33] B.B.M. Shao, W.T. Lin, Technical ef<sup>fi</sup>ciency analysis of information technology investments: a two-stage empirical investigation, Information & Management 39 (5) (2002) 391–401.

[34] S.Y. Sohn, T.H. Moon, Decision Tree based on data envelopment analysis for effective technology commercialization, Expert Systems with Applications 26 (2) (2004) 279-284

[35] E. Thanassoulis, A. Emrouznejad, Warwick Windows DEA Version 1.02: User's Guide, Warwick Business School, University of Warwick, Conventry, United Kingdom. 1996 First Print

[36] R. Weber, Information Systems Control and Audit, Prentice Hall Inc, Upper Saddle River, New Jersey, 1999.

[37] D. Wu, Z. Yang, L. Liang, Using DEA-neural network approach to evaluate branch ef<sup>fi</sup>ciency of a large Canadian bank, Expert Systems with Applications 31 (1) (2006) 108–115.

[38] Q.-J. Yeh, A.J.-T. Chang, Threats and countermeasures for information system security: a cross-industry study, Information & Management 44 (5) (2007) 480–491.

[39] B. Zmazek, L. Todorovski, S. Dzˇeroski, A. Vaupoticˇ, I. Kobal, Application of decision trees to the analysis of soil radon data for earthquake prediction, Applied Radiation and Isotopes 58 (2003) 697–706.

Sangjae Lee is a professor at the School of Management in Sejong University. He received his Ph.D. in Management Information Systems from the Graduate School of Management, Korea Advanced Institute of Science and Technology. He is a certi<sup>fi</sup>ed information systems auditor (CISA). His research interests include electronic commerce, information systems control and audit.
