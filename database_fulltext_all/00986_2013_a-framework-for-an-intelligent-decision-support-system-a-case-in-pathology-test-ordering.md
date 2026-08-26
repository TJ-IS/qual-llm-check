---
otero_id: 986
otero_key: "RQXX5NA2"
title: "A framework for an intelligent decision support system: A case in pathology test ordering"
authors: "Zoe Y. Zhuang; Carla L. Wilkin; Andrzej Ceglowski"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.10.006"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A framework for an intelligent decision support system: A case in pathology test ordering

Zoe Y. Zhuang, Carla L. Wilkin ⁎, Andrzej Ceglowski <sup>1</sup>

Department of Accounting and Finance, Monash University, PO Box 197 Caulfield East, Victoria 3145, Australia

a r t i c l e i n f o

Available online 5 October 2012

Keywords: Decision support Knowledge discovery Case-based reasoning Pathology ordering General practice

## a b s t r a c t

Decision context, knowledge management, decision makers, and decision strategy are fundamental components for understanding decision support systems (DSSs). This paper describes the speci<sup>fi</sup>c case of designing a framework for an intelligent DSS in the context of pathology test ordering by general practitioners (GPs). In doing so it illustrates the processes of discovering practical and relevant knowledge from pathology request data generated and stored in a professional pathology company, investigates and understands the decision makers (GPs) through a survey about their current practices in test ordering and their requirements for decision support, and <sup>fi</sup>nally proposes an intelligent decision support framework as the decision strategy to support GPs in ordering pathology tests more effectively and appropriately. The process and framework developed through this case contributes effective guidance for practitioners and theoretical understanding concerning intelligent decision support in a complex environment.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

Ordering of pathology tests by general practitioners (GPs) contributes signi<sup>fi</sup>cantly to the rising costs of health care [48]. Over the past decade Australia has witnessed a considerable rise in the number of and expenditure on pathology requests by GPs. This increase is the consequence of: improved communication between patients and GPs; government incentives for longer consultations; the shift of health services to a community environment; increased concern about medical litigation; and/or increased patient expectations [11,29,48]. Other external factors include the introduction of new Medicare Bene<sup>fi</sup>ts Schedule (MBS) items and increased computerization [12]. Globally there is a perception that pathology tests are not used appropriately [49,65,67,75,76,80], although there are concerns with the rigor in some studies and associated weak supporting evidence [45,64,74].

Evidence-based medicine indicates that tools like computerized clinical decision support systems (DSS) can improve the quality and effectiveness of clinicians' decisions [16,18,28,34]. For Australian GPs, although government promotion and incentives have resulted in increased use of “medical desktop” software as the referral point for primary care during patient consultations, particularly for prescribing medications (98%), checking for drug–drug interactions (88%), ordering laboratory tests (85%), running recall systems (78%) and recording progress notes (64%), the current application of computerized clinical DSSs is limited [33,47,78]. For example, with respect to pathology requests, the most common practices involve ordering laboratory tests (85%), receiving or storing pathology test results (79%) and running the recall system for routine tests (78%) rather than investigating the suitability of available options.

Evidence from some studies show that a high percentage of realtime clinical decision support suggestions are being over-ridden or ignored due to disruptions to work<sup>fl</sup>ow, time restraints and a perceived lack of relevant suggestions [52,69,77]. Hence, in designing a pertinent DSS, it is crucial to take account of contextual factors.

The aim of this paper is to develop a framework for a DSS that can assist GPs in ordering pathology tests more effectively and appropriately. In so doing we establish the merit of an integrated approach that combines knowledge discovery and case-based reasoning (CBR) mechanisms to capture the contextual requirements for an evidence-based, situationally relevant, flexible and interactive DSS, which we call an intelligent DSS.

The contributions of this study are three-fold. Firstly, by discovering and extracting practical and relevant knowledge from past pathology request data, we provide fresh understanding about the use of pathology tests from both patient-centric and clinical situation-centric perspectives. Secondly, results from our online survey provide comprehensive understanding about the appropriateness of GPs' ordering behavior as well as their needs of and requirements for intelligent decision support. Finally, this study shows how an integrated approach can be used to create an evidence-based, situationally relevant, flexible and interactive DSS that suits complex environments.

The remainder of the paper is structured as follows. Section 2 discusses the limitations of existing support for GPs in ordering pathology tests, while the components involved in decision making in the context of pathology ordering are outlined in Section 3. Section 4 describes the processes deployed to discover and extract useful knowledge/evidence from past ordering behavior that can be used to inform the decision making process, while Section 5 reviews the decision makers' (i.e. GPs') needs of and requirements for support in ordering pathology tests. These ideas are synthesized in Section 6 where the research proposes and reviews a framework for an intelligent DSS as a strategy to support GPs in ordering pathology tests more effectively and appropriately. In Section 7 we highlight implications for future research and present our conclusions.

## 2. Background

In prescribing drugs, guidelines are generally presented to GPs as a series of brief prompts targeted at managing individual patients [2]. In contrast, decision guidelines for pathology ordering are primarily disease-focused and contain low levels of evidence. Even when a high degree of evidence is available in a disease setting, information about the application of laboratory investigations in speci<sup>fi</sup>c patient situations is often limited [66]. At present, when GPs order pathology tests, the clinical guidelines are commonly presented as text, in paper or static electronic form. While this extends GPs' own knowledge and experience, given that most clinical guidelines have not been developed in a format that allows easy incorporation into computerized clinical DSSs, <sup>fl</sup>exible and interactive guidelines are yet to become reality [37].

General feedback provided by pathology companies to a GP on pathology ordering typically contains general and brief information on the overall volume of tests ordered by that GP during a given period of time, without detailed and speci<sup>fi</sup>c information like the tests ordered for a particular group of patients with a particular kind of disease. As this omits patient characteristics, there is no patient-speci<sup>fi</sup>c or situationally relevant evidence to assist GPs. Thus, it is unsurprising that studies have shown that GPs' everyday behavior can be based on less than effective clinical memory [20].

General practice centers on the individual patient–doctor relationship [73]. Given that in the decision making context of pathology ordering, the current decision support provided to GPs has very limited interactivity, <sup>fl</sup>exibility, situational relevance, and evidence base, we propose to address these de<sup>fi</sup>ciencies through development of a framework for an intelligent DSS. This enables more situationally effective ordering of pathology. Before detailing the framework we introduce the theoretical foundations of the study.

## 3. Theoretical foundation: decision making in the context of pathology ordering

Using the context of GPs' ordering pathology tests, we now discuss the theoretical underpinnings of the framework for the aforementioned intelligent DSS. Herein, decision support activities can be broadly de-<sup>fi</sup>ned as the set of activities within unstructured or semi-structured decision contexts that aim to support rather than replace the decision maker, facilitate learning on the decision maker's behalf, and use underlying data and models to focus on the effectiveness of the decision making process [46]. Given a DSS, in the context of decision making, is a tool, key components requiring appreciation include:

• the decision context (see Section 3.1);

• how knowledge is used (see Section 3.2);

• the decision makers (see Section 3.3); and

• the typical decision strategies (see Section 3.4) [36].

These components are outlined below.

## 3.1. Decision context

Decisions are not produced in a vacuum. They are made within a speci<sup>fi</sup>c environmental context, with the broader context in which decisions are made needing to be adequately considered [26]. As summarized in Fig. 1 (see below), decision making is a multi-step process comprising problem recognition, information search, problem analysis, alternative evaluation and choice [22].

Based on appreciation of speci<sup>fi</sup>c patient characteristics like demographics, past clinical history (including past pathology tests) and existing symptoms or diseases, the decision making process begins with problem recognition related to a need to order certain tests for a particular patient. To support decision making, in the information search process, standardized guidelines or protocols are consulted and combined with subjective personal knowledge or experience. Through this problem analysis GPs derive a meaningful list of plausible tests to be ordered. These alternative tests are then evaluated (alternative evaluation) before a choice is made regarding the particular types of tests to be ordered. This choice can be in<sup>fl</sup>uenced by internal factors (such as a clinical need for screening, diagnosis, disease monitoring or prognosis) and external factors (such as patient pressure, defensive behavior, clinical guidelines and government economic and cost considerations) [43,44,79].

## 3.2. Knowledge

According to Burstein and Carlsson [14, p. 104], knowledge management is the “continuous process of acquiring and deploying knowledge to improve decision making”. Knowledge over<sup>fl</sup>ow contributes to the decision makers' need for relevant and reliable knowledge to make ‘the right decision’ [36].

Presently, sources of knowledge to support GPs in ordering pathology tests include clinical guidelines (e.g. the Manual of Use and Interpretation of Pathology Tests) and educational material (e.g. the Common Sense Pathology series) [56,57]. However, their impact is limited [56] because the information is often regarded as too diverse, inaccessible, overwhelming and/or dif<sup>fi</sup>cult to contextualize [32,36,61,70]. The question that arises is how can knowledge be identi<sup>fi</sup>ed and structured so that GPs can access the “right” information in the “right” format at the “right” time i.e. providing information that works at an individual patient level, rather than as general guidelines.

In the course of modern pathology, massive amounts of pathology ordering data are generated and stored by professional pathology companies. This means that the data required to build such a knowledge base already exists, which creates the potential to extract the practical and relevant knowledge/evidence required to support GPs. In achieving our aim, we use the knowledge discovery techniques of data and text mining to extract patient- and situation-centric knowledge from past pathology ordering practices (see Section 4).

![](/api/attachments/RQXX5NA2/fulltext/images/17b2a0a2048b0d0fdcc794265e9aebcb1d08f1be3405c1ae320ce59f7465127f.jpg)  
Fig. 1. The decision context. Framework adapted from [22,84].

## 3.3. Decision makers

At the center of the decision-making process is the decision maker — an individual with speci<sup>fi</sup>c experience, skill, values and perspective who can reach a decision in a problem solving situation [30,36] by drawing upon resources like experience, education, relationship networks, knowledge of past successes and historic individual preferences together with knowledge of related external and internal environmental pressures [8]. Contextually, GPs are the decision makers responsible for choosing appropriate pathology tests for speci<sup>fi</sup>c patients in speci<sup>fi</sup>c situations.

Research shows that despite GPs' widespread use of computers and computerized clinical packages, the application of currently available computerized clinical DSSs is limited [78]. Herein a high percentage of real-time clinical decision support suggestions is over-ridden or ignored in primary care situations [52,69,77] due to work<sup>fl</sup>ow disruptions, time restraints and the lack of directly relevant suggestions. Thus, we argue that preceding the design of an effective DSS, there is a need to study GPs' needs of and requirements for such a DSS so that there is positive endorsement:

1. that GPs indicate the need for support in effectively and appropriately ordering pathology tests; and

2. with respect to the kind of support they require.

Investigation of GPs' views on these issues is reported in Section 5.

## 3.4. Decision strategy

There are various strategies that may assist a decision maker in reaching a choice. These include “recommended for” (a recommendation concerning which alternative the decision maker should choose); “recommended against” (which alternative not to choose); “information” (providing information about alternatives); and “decision support” (displaying information and structuring problems/issues to facilitate appropriate choices) [21].

As the modern approach to decision support assumes greater autonomy for the decision maker [14], recommendations (both for and against) may be less preferable than providing decision makers with relevant information and effective ways (decision support) to reach a choice. The main strategy today requires various types of information to be provided to support GPs in ordering pathology tests. As outlined in Section 3.2, the impact of information materials (e.g. clinical guidelines and educational material) is limited for practical reasons like irrelevance of information, lack of effective accessibility and time constraints. Decision support strategies that provide decision makers with effective, timely ways to access relevant information and to structure complex problems are yet to be realized in the clinical practice of ordering pathology tests. Our framework for the proposed intelligent DSS (Section 6) facilitates such decision making strategies.

Leveraging this understanding of the four components (decision context, knowledge, decision makers and decision strategy), we begin to detail design of the framework for the intelligent DSS. Based on understanding related to the decision context, we analyze daily transactional data from a pathology company to discover relevant and practical knowledge (see Section 4). Then through a survey we investigate and understand the current practice of decision makers (i.e. GPs) in ordering pathology tests and their requirements for decision support (see Section 5). We conclude by proposing a framework for an intelligent DSS as the decision strategy to support GPs in this complex environment (see Section 6).

## 4. Knowledge discovery through data mining and text mining

The aim of this section is to demonstrate how data mining (Section 4.1) and text mining (Section 4.2) techniques were used to discover and extract useful knowledge/evidence from past pathology requests. This ensures that decision makers (GPs) have the necessary context and knowledge in an intelligent DSS to formulate effective strategies to order pathology tests related to patient treatment.

## 4.1. Building knowledge for the decision context through data mining

Using data mining techniques we explored the pathology ordering practices of GPs from a patient-centric perspective. The data provided by an Australian pathology company, XYZ Pathology (a pseudonym), contained 1,548,122 records of GPs' pathology requests from 01 May 2003 to 30 April 2004. Each record represented an individual request for one or a group of pathology tests for a patient. The objective was to discover homogenous patient clusters based on patients' characteristics and pathology consumption patterns.

There are many clustering techniques available, ranging from simple clustering methods such as the k-means algorithm, to more sophisticated and pro<sup>fi</sup>cient ones such as Self-Organizing Maps (SOM) and the Expectation-Maximization (EM) algorithm [31]. Due to the large size of the dataset (over one and a half million records) and the lack of obvious relationships among variables, we selected Kohonen's Self-Organizing Maps (SOM) [7,38–40] to explore the data and discover relationships.

SOM is an unsupervised neural network approach to data clustering and visualization, with simultaneous clustering and projection capabilities. It identi<sup>fi</sup>es hidden relationships by looking for input patterns that are similar and should be grouped together (or clustered). Similarity in input patterns is determined by examining the distance between inputs in the (multidimensional) input space [38–40]. In this study the software package Viscovery SOMine [23] was used to model the data. It has advanced data visualization capabilities that permit the data to be projected into two-dimensional maps, which permit easier analysis and understanding of the results. Features of the data and dependencies between the variables can be identi<sup>fi</sup>ed and evaluated from such maps [25].

The process commenced with processing the pathology request data. Herein the population was de<sup>fi</sup>ned as a collection of individually assigned unique patient records that included attributes like age, gender, number of requests per year, number of tests ordered per year and average service lags per year (a service lag is de<sup>fi</sup>ned as the time lag between the date of referral and date of service). Secondly, independent random samples were drawn from the population. For each sample, the Viscovery SOMine implementation of the SOM methodology was consistently and independently applied. The aim was to discover distinctive clusters based on patients' attributes. Thirdly, quality of the clustering was assessed using both quantitative [10] and qualitative criteria [62] and the most informative grouping structure was chosen. Finally, the selected clustering structure was analyzed in detail to discover useful knowledge (see [82] for further details).

Basic statistics about the seven clusters [82].

<table><tr><td rowspan="2"></td><td>C 1</td><td>C 2</td><td>C 3</td><td>C 4</td><td>C 5</td><td>C 6</td><td>C 7</td></tr><tr><td>Young female</td><td>Old female</td><td>Old male</td><td>Young male</td><td>High user</td><td>Slow user</td><td>Old frequent slow high user</td></tr><tr><td>Matching records</td><td>14,650</td><td>9,727</td><td>7,048</td><td>6,284</td><td>4,531</td><td>2,959</td><td>828</td></tr><tr><td>Matching records (%)</td><td>31.83</td><td>21.13</td><td>15.31</td><td>13.65</td><td>9.84</td><td>6.43</td><td>1.8</td></tr><tr><td>Patient age (years)</td><td>30.60</td><td>63.16</td><td>65.07</td><td>32.18</td><td>56.89</td><td>54.92</td><td>69.84</td></tr><tr><td>Patient gender (1-female)</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0.86</td><td>0.63</td><td>0.51</td></tr><tr><td>Number of orders/year</td><td>1.20</td><td>1.45</td><td>1.69</td><td>1.22</td><td>4.36</td><td>1.84</td><td>18.58</td></tr><tr><td>Number of tests/year</td><td>4.66</td><td>5.06</td><td>9.18</td><td>5.74</td><td>21.32</td><td>9.34</td><td>31.19</td></tr><tr><td>Service lag (days)</td><td>0.96</td><td>1.34</td><td>2.84</td><td>0.77</td><td>2.31</td><td>58.59</td><td>53.23</td></tr></table>

![](/api/attachments/RQXX5NA2/fulltext/images/7dc0ab20f0746f29f7c7ad31f5041d505b9400ebefc26e291347051e58ae7ad4.jpg)  
Fig. 2. Mean and total number of tests ordered by each of the seven clusters [82].

Results from the data mining stage yielded seven patient clusters. Each cluster was given a semantic name (e.g. “Young female cluster” and “High user cluster”) based on the patients' characteristics and their pathology consumption patterns (e.g. patient age, gender, and number of tests ordered per year) in that particular cluster. Basic statistics about the seven clusters is shown in Table 1, with the average and total number of pathology tests consumed by cluster illustrated in Fig. 2.

The variables of interest, namely the most frequently ordered individual tests and frequently encountered clinical problems, were then super-imposed onto the seven clusters. The elements of knowledge generated from this process are shown in Table 2.

It is noteworthy that even though some of the patient clusters discovered using data mining were relatively obvious (e.g. “young female users” and “old female users”), other clusters (e.g. “high users”, “slow users” and “old frequent slow high users”) and their pathology consumption patterns were less obvious and could not have otherwise been explicitly and objectively understood by GPs.

Frequently ordered tests and common clinical problems by cluster.

<table><tr><td>Cluster</td><td>Frequently ordered tests</td><td>Common clinical problems</td></tr><tr><td>C 1 young female user</td><td>PAP smearHepatitis tests</td><td>Urinary tract infectionsPregnancies</td></tr><tr><td>C 2 old female user</td><td>PAP smearINR warfarin</td><td>Urinary tract infectionsLipid disorders</td></tr><tr><td>C 3 old male user</td><td>PSA (prostate specific antigen)</td><td>DiabetesLipid disorders</td></tr><tr><td>C 4 young male user</td><td>Hepatitis tests</td><td>Lipid disordersFatigue</td></tr><tr><td>C 5 high user</td><td>Full blood countLipidsGlucoseLiver function testsEUC (electrolytes, urea and creatinine)ESR (erythrocyte sedimentation rate)</td><td>DiabetesLipid disordersThyroid problemsUrinary tract infections</td></tr><tr><td>C 6 slow user</td><td>LipidsThyroid function tests</td><td>Lipid disordersDiabetes</td></tr><tr><td>C 7 old frequent slow high user</td><td>INR warfarin</td><td>DiabetesLipid disordersThyroid problems</td></tr></table>

## 4.2. Building knowledge for the decision context through text mining

The text mining technique was used to investigate the clinical purposes and issues related to pathology ordering by Australian GPs as captured in the clinical notes attached to pathology requests. While many text mining algorithms are in use, the dominant clustering algorithm is feature map algorithms based on SOM [39]. In our study we used High Dimensional Growing Self Organizing Maps with Randomness (HDGSOMr) to mine the clinical notes, because this algorithm is capable of producing good clusters from very large collections of text in a reasonably short time [3,4].

The unsupervised nature of HDGSOMr leads to grouping text based on the notion of similarity. The process commenced with preprocessing the text data set to correct spelling [3,4]. Then commonly used words such as “a”, “is” and “the” were removed using a stop word list. Next the text was broken down into individual words and stemmed using Porter's stemming algorithm [54] to obtain the root form of words. The resulting text was then converted to a normalized vector using the Term Frequency-Inverse Document Frequency (TF-IDF) method [58].

After pre-processing the text records and then presenting them for clustering by the HDGSOMr algorithm, a map was produced that has clusters organized in such a way that related clusters (nodes) were placed close to each other. A hypertext map was then produced from the algorithm, which was used as the user interface for the technique. By clicking on a hyperlink in the map, the data analyst could navigate to records associated with the chosen cluster. Finally, records associated with the cluster were extracted and a summary of the other associated <sup>fi</sup>elds and full texts were presented (see [83] for detailed information).

A total of 213 nodes were generated from the text mining process. Each node represented a cluster of request records with similar input patterns of clinical notes by GPs and was accompanied by size, average quantization error (AQE) and the top <sup>fi</sup>ve keywords with relative percentage. Based on the percentages of the top 5 keywords, we separated the clusters into Distinctive and Fuzzy nodes. Distinctive nodes have at least one of the top 5 keywords covering 100% of the records, while Fuzzy nodes do not have any keyword dominating 100% of the records in the node. A summary of the node groupings is presented in Table 3 below.

Two special groupings of distinctive nodes were “Pap smear” and “Warfarin” related requests. These two groupings were large in size and exhibited unique test ordering patterns. Other groups with distinctive textual patterns were classi<sup>fi</sup>ed according to the particular type of associated clinical indication. These types of clinical indications included “clinical conditions”, “clinical problems”, “medications”, “nature of ordering”, “sample descriptions”, “previous test results” and “management issues”. Requests related to “clinical problems” were further sub-classi<sup>fi</sup>ed according to the speci<sup>fi</sup>c clinical problem with which the request was associated. The clinical problems included “hyperten sion”, “pain”, “lipid disorder”, “diabetes”, “UTI”, “infection”, “pregnancy”, “chest problem”, “prostate problem” and “abdominal problem”.

Table 3  
Summary of node groupings [83].

<table><tr><td colspan="2">Node groupings</td><td>Description</td><td>No. of nodes</td><td>Absolute size (no. of records)</td><td>Relative size (%)</td></tr><tr><td rowspan="2">Special distinctive nodes</td><td>Pap smear</td><td>Nodes with “smear” or related terms as dominant keywords.</td><td>68</td><td>259,401</td><td>22.51</td></tr><tr><td>Warfarin</td><td>Nodes with “warfarin” or related terms as dominant keywords.</td><td>14</td><td>177,026</td><td>15.36</td></tr><tr><td>Other distinctive nodes</td><td></td><td>Nodes with other distinctive dominant keywords.</td><td>78</td><td>315,502</td><td>27.37</td></tr><tr><td>Fuzzy nodes</td><td></td><td>Nodes with no distinctive dominant keywords.</td><td>53</td><td>400,676</td><td>34.76</td></tr><tr><td>Total</td><td></td><td></td><td>213</td><td>1,152,605</td><td>100</td></tr></table>

In summary, while data mining allowed us to discover distinctive patient groups and their unique pathology utilization patterns, text mining allowed us to identify patterns of clinical indications concerning the purpose for ordering pathology tests. The knowledge acquired was used in two ways.

1. Together with an optimization mechanism and input from a domain expert, we used this knowledge to generate hypothetical clinical cases that were included in a subsequent survey to investigate GPs' test ordering behaviors and their requirements for an intelligent DSS (see Section 5).

2. It formed the foundation for the framework of the intelligent DSS (see Section 6).

## 5. Decision makers: understanding GPs' pathology ordering practices and DSS requirements

This section describes the online survey, which we developed and administered through the Royal Australian College of General Practice (RACGP). The survey (see Appendix A for a summary) was used to establish GPs' need for support in effectively and appropriately ordering pathology tests and the kind of support required to facilitate this (see Section 3.3).

## 5.1. The survey

In particular the survey aimed to:

• Test the effectiveness and appropriateness of GPs ordering of pathology tests by presenting them with 20 hypothetical clinical cases, which were compared with a senior pathologist's views; and

• Investigate GPs' perceptions of and requirements for an intelligent DSS through direct questioning using a 5-point Likert scale.

## 5.1.1. Section 1 of the survey: the 20 hypothetical clinical cases

Using knowledge generated by the data/text mining processes, an optimization mechanism, and input from a pathologist (a domain expert), we constructed 20 synthetic hypothetical cases. These represented typical scenarios that were used to examine GP's decision processes and determine the accuracy of their pathology ordering practices. The data and text mining processes provided fundamental understanding about patient types (i.e. patient clusters), and clinical problems; the literature review [e.g. 43,44,72] identi<sup>fi</sup>ed medical and contextual reasons for ordering; while the optimization mechanism assigned these information elements (i.e. patient type, clinical problem, and reasons for ordering) into the most common clinical situations. Input from the domain expert (pathologist) <sup>fi</sup>nalized the cases.

Content validity was ensured as the cases embraced the most common clinical situations, with each case contextually embracing information regarding a particular patient type, a clinical problem and two prominent reasons (i.e. one medical and one contextual) for ordering (see below for an example).

“A 65 year old woman with mild diabetes, treated with oral hypoglycaemic agents. Over the last year she has demonstrated a stable HbA1c of around 7.0% with an excellent lipid profile and no evidence of microalbuminuria on the last 4 quarterly reviews. She is looking forward to seeing that her next set of results are just as good.”

There were two reasons for using hypothetical cases to investigate the ordering behavior of GPs instead of existing cases out of the large dataset. Firstly, the optimization mechanism used to generate the hypothetical cases ensured that each hypothetical case represented a particular clinical situation with a unique combination of patient type, clinical problem and two reasons for ordering, while a typical case may or may not have existed among the real cases stored in the large dataset. Secondly, existing cases contained valuable information about patient types and clinical problems for ordering pathology tests, but the reasons for ordering (especially contextual reasons) were rarely recorded in the dataset. In contrast the hypothetical cases contained both medical and contextual reasons for ordering that were identi<sup>fi</sup>ed from the literature.

For each hypothetical case GPs were asked what, if any, tests they would order and why. After submitting each case, the GP received case-speci<sup>fi</sup>c feedback that included comments from the domain expert (i.e. pathologist), references to clinical guidelines and statistics about past pathology ordering. This aimed to predispose GPs to situationally relevant decision support (see Section 5.1.2).

5.1.2. Section 2 of the survey: GPs' perceptions of/requirements for an intelligent DSS

The three components of the survey that explored GPs' requirements for and perceptions of intelligent decision support to enhance their pathology ordering practices were:

1. Experience with computer systems;

2. Use of current decision support tools; and

3. Perceptions of intelligent decision support.

## 5.1.3. Reliability and validity of the survey

Various approaches were used to enhance the reliability and validity of the survey instrument. For example, to ensure reliability, questions included in the survey were carefully designed with input from domain experts (namely, a pathologist and two GPs); were presented in a structured format using a 5-point Likert scale; and were both pre-tested and pilot tested on GPs. Validity was ensured via a literature review [e.g. 13,19,24,27,42,44,47] that identi<sup>fi</sup>ed components to be included in the survey, rigorous design of the 20 hypothetical clinical cases, and various incentives to increase the response rate, with participation from the RACGP.

## 5.2. Survey results

As the survey was conducted through the auspices of the RACGP, preliminary information about the survey was posted on their website and an email was sent to every member GP to invite participation. Further, to improve the response rate, GPs were informed that education points could be gained by completing the online survey. From 18,172 active GPs recognized in Australia, 168 attempted the survey. Of these attempts, 85 responses were usable because the GPs had completed all 20 hypothetical cases included in the survey. About half (50.6%) of the respondents were male and the majority (66%) were from urban or regional practices.

![](/api/attachments/RQXX5NA2/fulltext/images/8c71e6b5f90d7c60be793eab7bc2987f61e064dfcd776991d999560f88843c98.jpg)  
Fig. 3. Simpli<sup>fi</sup>ed framework for intelligent decision support.

## 5.2.1. Appropriateness of pathology ordering by GPs

In this study appropriate testing refers to ordering the maximum number of “necessary” tests required and the minimum number of “unnecessary” or “unsuitable” tests as indicated by clinical guidelines. In our survey, in instances where at least one pathology test should be ordered (17 of the 20 cases), the dominant pattern was that GPs ordered part of the “necessary” tests and some “unnecessary” or “unsuitable” tests. Responses showed that the drivers were internal/medical rather than external/contextual reasons. Of the contextual reasons, “guidelines” and “cost considerations” were the most signi<sup>fi</sup>cant.

In cases where, according to published clinical guidelines, it was not “necessary” to order pathology tests (3 of the 20 cases), most GPs still did so. Similarly, based on published guidelines, a considerable quantity of pathology requests were regarded as “unsuitable”, with the strongest driver being diagnosis. Patient pressure and defensive behavior were not considered by GPs as strong drivers. These outcomes indicate that:

• Internal/medical factors were stronger drivers for ordering pathology tests than external/contextual factors. Thus, there is potential to in<sup>fl</sup>uence and improve GPs' practices through the provision of accessible evidence-based resources like our intelligent DSS.

• Pathology tests were shown to be not optimally utilized by Australian GPs, leading to wasted health resources and/or risks for patients' health. This further supports the need for an intelligent DSS.

## 5.2.2. GPs' perceptions of/requirements for decision support

The majority of GPs who participated in the online survey considered themselves experienced with computer systems. Use of currently available decision support tools (e.g. electronic ordering, results downloading) seemed common practice, with the most highly valued DSS being active systems such as patient-speci<sup>fi</sup>c reminders, dynamic disease-speci<sup>fi</sup>c guidelines, and patient-speci<sup>fi</sup>c prompts. Passive decision support like static electronic libraries or guidelines was less valued.

GPs' comments indicated that common barriers to the use of DSS at the point of care included time, accessibility and reliability issues, and that they required an easy, fast, relevant and <sup>fl</sup>exible DSS. Further, they reacted positively to the situationally relevant feedback provided to them after completing each hypothetical case in the survey. These outcomes indicate that:

• Current decision support tools have been commonly used by GPs, which provides a foundation for more sophisticated DSS.

• GPs prefer active, relevant and <sup>fl</sup>exible decision support rather than passive, static decision support, a <sup>fi</sup>nding which means that evidence-based decision support provided at the “right” time in the “right” format is more likely to be valued.

Given this broad support for the research aim, the next step involved developing the framework for the intelligent DSS to support GPs' decision strategies related to pathology test ordering.

## 6. Decision strategy: towards building an integrated intelligent DSS

Synthesizing the knowledge discovery processes (data and text mining) outlined in Section 4, with outcomes from the survey of GPs ordering behavior and requirements for a DSS (see Section 5), we now propose our framework for an intelligent DSS.

Consistent with the literature [e.g. 2,50,60,61,63,78], our <sup>fi</sup>ndings from the survey showed four requirements for an intelligent DSS. These requirements, which may also be relevant to other domains where intelligent decision support is required, include:

1. Evidence base. An intelligent DSS should provide rigorous research/practice evidence to GPs to convince them to change their ordering behavior — this ensures perceived reliability.

2. Situational relevance. A DSS should address the speci<sup>fi</sup>c clinical situation in which the GP is seeking support — this ensures perceived relevance.

3. Flexibility. A DSS should be <sup>fl</sup>exible and cater to GPs' daily decisionmaking logic so support does not intrude on their daily work<sup>fl</sup>ow or impose an unreasonable time burden — this ensures ef<sup>fi</sup>ciency.

Table 4

4. Interactivity. Intelligent decision support should guide GPs to <sup>fi</sup>nd the most desired support through continuous interaction between the system and the GP — this ensures effectiveness.

With these fundamental requirements established, the design, subsequent evaluation and implementation issues associated with our framework for an intelligent DSS are now conceptualized.

6.1. The merits of integrating data/text mining and CBR in our framework for an intelligent DSS

Integrating the four requirements with use of text/data mining for clustering and CBR approaches, we present initial steps towards construction of our framework, which has speci<sup>fi</sup>c relevance for complex issues in case-based classi<sup>fi</sup>cation and case retrieval. The underlying philosophy is to support problem solving in new cases through establishment of a peer-group based knowledge base of past experiences of pathology ordering using relevant knowledge extracted from past data retrieved and reused by the CBR cycle. While data mining techniques (including clustering) have previously been combined with CBR for ef<sup>fi</sup>cient case retrieval and case-based maintenance [81], automated case generation [17] and improved case-based classi<sup>fi</sup>cation [5], the novelty of our framework is in addressing the four DSS requirements through linking data mining, text mining and CBR. The <sup>fi</sup>rst step involves adding a CBR engine to the DSS. Drawing on the principles contained in a general model of clinical DSS reported in the literature [9], the knowledge base forms the heart of the model. Linked to this is data/text mining, which provide data about patient clusters and clinical situations; a CBR engine that allows similar past cases to be matched and retrieved; and input and output capabilities. These capabilities provide a pathway for re<sup>fi</sup>nement of raw historic data (input) into structured subsets that re<sup>fl</sup>ect groupings of records based on common attributes. A simpli<sup>fi</sup>ed graphical depiction of the framework is presented in Fig. 3.

The CBR engine is fundamental. By accessing knowledge contained in the knowledge base, instead of relying on general knowledge about a problem domain or making associations through generalized relationships between problem descriptors and conclusions, our CBR approach utilizes speci<sup>fi</sup>c knowledge of actual problem situations (cases) [1,41]. This is consistent with recent research showing use of CBR in the medical domain for diagnosis, classi<sup>fi</sup>cation, tutoring, and planning including therapy support [51].

A typical CBR cycle may be generalized as four processes: retrieval of the most similar case(s) (including the tasks of situation assessment, initial match and <sup>fi</sup>nal selection); reuse of information and knowledge in the retrieved case (by either copying or adapting solutions for that case to suggest a solution to the current problem); revision of the proposed solution for the new case (which includes some evaluation); and retention of experiences for future problem solving [1]. Attempts to apply the complete CBR cycle to the medical domain are rather exceptional [59], with the most challenging task being adaptation of past solutions to new cases. Consequently, prior solutions have tended to focus on situations that involve retrieving similar cases and presenting them as information to the user. This is because:

• in medical applications it is too complicated/even impossible to acquire suf<sup>fi</sup>cient adaptation knowledge; and

• GPs are interested in information about prior relevant cases, but prefer to reason the current situation themselves.

Given that separate application of either data mining/text mining or CBR principles cannot fully achieve the four requirements for decision support, our framework, with its focus on case retrieval and provision of relevant evidence for decision support, links the complimentary merits of these approaches (see Table 4).

Having established the merits of integrating CBR as the reasoning engine and data/text mining to create the knowledge base, the next stage involved formulation of the proposed framework and related issues like validation and implementation.

6.2. Our framework for an intelligent DSS in the context of pathology test ordering

A detailed overview of our proposed framework for an intelligent DSS is presented in Fig. 4. As shown, the structures of patient clusters/ clinical situations are speci<sup>fi</sup>ed by the data and text mining stages, with this information used to support the CBR (see Table 5 for an overview of this).

Consistent with the literature [1], our CBR cycle shown above (see Fig. 4) includes case retrieval, case reuse, case revision and case retention, with the outcomes written to the case base. Table 5 provides an overview of these steps.

The CBR structure deployed in this framework (see Fig. 4 and Table 5) means case retrieval is <sup>fl</sup>exibly possible at two levels. Firstly, GPs can see patient clusters which are similar in terms of age, gender and past pathology ordering patterns. This assists in determining the tests that are most frequently ordered for such patients. Secondly, GPs can re<sup>fi</sup>ne their search criteria to identify a limited number of cases that best match the presenting patient. While these levels of questioning are possible using both data and text mining, the latter requires extensive preparatory work in order to populate descriptions of the clusters.

As previously mentioned, our approach is not intended to replace the decision maker. Rather it is designed to support GPs in pathology ordering at the point of care (the GPs' judgment is required to re-live the logic and rationale behind the solutions to past cases and translate previous ordering experiences into the current scenario). While the immediate task ends after GPs use information about past cases and decide what tests should be ordered, the whole CBR process may (and indeed should) continue until a new case is evaluated by a pathologist and that information is stored in the pathology-request database. This progression affords the opportunity for future research into an integrated CBR system that incorporates the work<sup>fl</sup>ows of test ordering in general practice and feedback from pathology laboratories.

Merits of the data/text mining and CBR approaches in our integrated framework.

<table><tr><td>Requirement criteria</td><td>Merits of data/text mining</td><td>Merits of CBR</td></tr><tr><td>Evidence base</td><td>Provides relevant evidence based on past pathology ordering practices of a large group of peer GPs. Regular updates of the knowledge base by iterative data/text mining means the information is updated in a timely manner.</td><td>Enables the GP to retrieve and reuse the evidence generated by data/text mining processes and facilitates extension of the knowledge base through retaining new cases that contain pathologist evaluation and comments on GPs ordering practices.</td></tr><tr><td>Situational relevance</td><td>Prepares knowledge from both a patient and a clinical situational perspective.</td><td>Caters well to a particular patient and clinical situation.</td></tr><tr><td>Flexibility</td><td>Provides situationally relevant information that can be used flexibly by GPs at the point of care.</td><td>Assists the GP to collect information flexibly from the system about similar prior individual cases at two-levels (see the discussion following Table 5 below).</td></tr><tr><td>Interactivity</td><td>Facilitates generation of a structured knowledge base that can be readily accessed by GPs via a user friendly, interactive interface linked to the CBR engine.</td><td>Permits the GP to interactively retrieve past knowledge to support decision making regarding the current case.</td></tr></table>

![](/api/attachments/RQXX5NA2/fulltext/images/41c5112f0ccf232f2f342a44bef6654d589c322cb387398b6354fde0a4cd9d03.jpg)  
Fig. 4. Framework for the proposed intelligent DSS.

## 6.3. Evaluation of the proposed framework

While there are no formal methods for validating or evaluating a conceptual model [55], descriptive evaluation may be performed on an information technology artifact such as a DSS framework [35]. In line with Hevner et al.'s model [35] and based on the purpose of ensuring that the framework is suf<sup>fi</sup>ciently accurate for the task at hand [15], we descriptively evaluate our framework (through making informed arguments and scenarios) against the requirements for an intelligent DSS articulated by the GPs (see Table 6).

Any design is inherently an iterative process [35], so our evaluation is not the end of the design process. Instead, like the function ing of our DSS itself, this evaluation contributes feedback and information about this artifact which would enhance its further development [71].

## 6.4. Implementation issues

In progressing to implementation of the DSS, one particular critical success factor concerns the key stakeholders of the system, namely GPs. It is essential to recognize that GPs often face information overload [28]. Consequently, acceptance would be enhanced if our DSS correlated with their ordering patterns. In line with earlier research that has established this as a process comprising seven stages, we believe our DSS can accommodate these requirements (see Table 7).

The stages, from evidence to practice, would seem to justify con<sup>fi</sup>- dence that our DSS has potential to <sup>fi</sup>rstly meet the needs of GPs for pathology ordering and secondly achieve a reduction in unnecessary/ unsuitable tests (see Table 7). Both are important goals, but implementation is best realized if key success factors are consciously accommodated. Common to most technological initiatives, these success factors include: a shared vision; executive leadership; CEO support; and decision involvement [6,53,68]. Some factors have already been appreciated as we evolved the framework for the DSS. For example, the online survey was conducted with the support of RACGP and the responding GPs acknowledged the need for improvement in pathology ordering and a more accessible, timely and relevant support process. This contributes to the vision that key stakeholders were involved in decisions that led to the design of the framework for the intelligent DSS.

Table 5 Steps in the CBR process.

<table><tr><td>Step</td><td>Objective</td><td>Activities</td><td>Note</td></tr><tr><td>Case retrieval</td><td>To achieve the best match between a new case and similar cases available in the case base</td><td>(a) Assess the new case in terms of cluster-specific profiles; (b) Find the cluster with the best match for the new case; and (c) Select information about past cases at a “whole-cluster” or “best match” (individual case) level</td><td>Parameters used in case retrieval may include patient related parameters (such as patient age, gender, number of orders last year, number of tests ordered last year, and average service lags last year), and/or clinically related parameters (such as the presenting clinical problem, the clinical condition of the patient, nature of the ordering, and medications the patient is taking)</td></tr><tr><td>Case reuse</td><td>To effectively reuse past solutions in new case settings</td><td>The solution for the retrieved case(s) is either directly copied or adapted to the settings of the new case</td><td>Clinical judgment of the GP is required to reuse the past solution in the settings of the new case</td></tr><tr><td>Case revision</td><td>To evaluate the quality of the decision made for the new case</td><td>Provide expert feedback on the quality of the solution for the new case</td><td>Comments provided by the pathologist about the tests ordered can be considered as an evaluation of the GP&#x27;s decision about the new case</td></tr><tr><td>Case retaining</td><td>To maximize the amount of useful knowledge about the new case</td><td>Incorporate the evaluation feedback into the new case</td><td>Pathologist&#x27;s comments are retained and integrated into the new case</td></tr><tr><td>Case base</td><td>To maximize the amount of knowledge in the case base</td><td>Add the complete case to the appropriate cluster in the case base</td><td>The case base is updated with the case that includes pathologist&#x27;s comments. The new data/case base can serve as the starting point of the next data mining stage</td></tr></table>

Table 7  
Table 6  
Evaluation of the merit of the proposed framework.

<table><tr><td>Criteria</td><td>Outcome</td></tr><tr><td>Evidence base</td><td>Massive amounts of pathology ordering data are generated and stored by pathology companies. As demonstrated, we found potential in exploring and using this data, supplemented with input (i.e. evaluation and comments) from pathologists, to support CBR. From a practical (maintenance) perspective, it noteworthy that as new data becomes readily available, it only takes a single run of a data/text mining cycle to generate updated clusters - an activity that should be supported by either the business analysts within the relevant commercial pathology company or by public health authorities, not individual GPs. The outcome of these practices is solid evidence, which is stored in a pathology request database. This knowledge, which is retained via the CBR process and periodically updated via data and text mining, reflects the past pathology ordering practices of a large group of peer GPs and contains pathologist evaluation and comments on these GPs ordering practices.</td></tr><tr><td>Situational relevance</td><td>As information related to pathology requests is easily transferable through normal electronic means, evidence such as patient groups and patient records best matching current patient characteristics and clinical situations, can potentially be made available online via our intelligent DSS (which in turn can be accessed through a link incorporated into popular clinical information systems such as Medical Director). This practice ensures ready accessibility to past cases, which provide patient oriented and/or clinical situationally oriented perspectives that cater to GPs&#x27; daily practice.</td></tr><tr><td>Flexibility</td><td>The intelligent DSS allows GPs to enter patient characteristics and retrieve past cases flexibly, at the level of either clusters or individual cases, in a timely and reliable manner. Specifically, it allows GPs to engage with the data to see patient clusters that are similar in terms of patient characteristics and past pathology ordering patterns, and drill into the data to reveal details about the most relevant individual cases.</td></tr><tr><td>Interactivity</td><td>The interaction with GPs that is permitted by the proposed intelligent DSS ensures optimum matching of cases against patient and clinical criteria. Some of this interaction is evident in the processes described above related to flexibility, wherein GPs can interact with the system to retrieve past cases. Other interactivity is provided as the knowledge base is upgraded through runs of text/data mining that updates patient clusters and reinforces the CBR cycle. Most importantly, while the system provides evidence of common practice, with which GPs can interact, it does not prescribe what to order - GPs need to apply their judgment based on their knowledge of the patient. As GPs often care for patients for protracted periods of time, the DSS would allow them to remain interactively at the forefront of alternative testing options and maintain the relevance of their knowledge. A possible future extension could be to generate reminders for GPs about tests, alternative options and timing. Finally, given that the data related to pathology requests is fed (after evaluation and commenting by a pathologist) back into the database, this means that the DSS is user-centered since GPs themselves contribute to ongoing development of the database.</td></tr></table>

The next step is to obtain executive support, or in this case ministerial support, as government funding is required to take the prototype framework from conceptualization to instantiation. Other support needs to come: from the pathology services sector, to ensure that all the relevant information or evidence (such as pathologists‘ reports on past orderings, normality or abnormality of test results, patient outcomes and relevant clinical guidelines) can be added to our DSS when available; and from the health care sector and associated bodies like RACGP to champion the advantages of the DSS in reducing demands on public health funding through more effective use of resources.

Performance issues are another area that requires consideration. To improve acceptance and utilization, a feedback mechanism needs to be included in the system where GPs can enter comments or suggestions for improvement that are regularly reviewed and fed into future design cycles. Further, usage needs to be encouraged and monitored.

## 7. Conclusion and future research directions

The aim of our study was to design a framework for an intelligent DSS to optimize GPs' practices in pathology test ordering. Here the optimal (or appropriate) choice involves ordering the maximum number of “necessary” tests and the minimum number of “unnecessary” and “unsuitable” tests as indicated by clinical guidelines within constraints including patient pressure, limited consultation times and cost considerations. Given that the existing knowledge sources for GPs were found to be dif<sup>fi</sup>cult to access, we mined patient and clinical data contained in past pathology requests to extract patient- and clinical situation-centric knowledge. Then, through an online survey and literature review, we established GPs' needs for a DSS that is evidence-based, situationally relevant, <sup>fl</sup>exible and interactive. Such a DSS offers the “right” knowledge in the “right” format at the “right” time to GPs at the point of test ordering.

Consideration of the stages in Glasziou and Haynes' [28] research-to-practice pipeline and its relevance to implementation of our intelligent DSS.

<table><tr><td>Stages from research to action [24]</td><td>Implication</td><td>Relevance to our intelligent DSS</td></tr><tr><td>Awareness</td><td>The need to achieve awareness of relevant/valid evidence against the information glut.</td><td>The DSS can provide precise, regularly updated and relevant information in an integrated and interactive manner. It enables GPs to access the ‘right’ information in the ‘right’ format at the ‘right’ time.</td></tr><tr><td>Acceptance</td><td>The need to be offered unbiased evidence vs. marketing, reciprocity etc.</td><td>Given the range of material gleaned by text/data mining and CBR, together with the expert panel appraisal by pathologists, GPs should reasonably have confidence in the lack of bias conveyed in the evidence in the DSS.</td></tr><tr><td>Applicable</td><td>The need to target correct groups and convey evidence of a range of related factors.</td><td>The unique combination of text/data mining and CBR techniques ensures that information about particular patient groups with distinctive characteristics and related factors can be accessed and retrieved by GPs with minimum time and effort.</td></tr><tr><td>Available and able</td><td>Provision of availability and supporting evidence related to options.</td><td>The DSS is designed in such a way that it is evidence-based, situationally relevant, flexible and interactive. It enables GPs to access the most relevant evidence with ease and confidence.</td></tr><tr><td>Acted on Agreed to</td><td>Provision of reminders for medical/clinical management. Facilitation of patient agreement to treatment.</td><td>At this initial stage of development of the DSS, this option is an area for future research. Given the GP will have ready access to range of options and supporting evidence, the capacity to respond to patient queries quickly and authoritatively will be enhanced.</td></tr><tr><td>Adhered to</td><td>Facilitation of patient adhering to treatment through provision of succinct and effective advice and reminders.</td><td>Through the upgrade cycle, GPs can become aware of new alternatives more easily.</td></tr></table>

Methodologically, the advantage of the proposed integrated approach is its ability to use the available information at the cluster level to form a generalized case based on a set of similar cases. This presents a new perspective on the use of prototypes through case aggregation — one of the current trends of medical CBR systems according to a recent overview of medical CBR systems and system development [51]. Adopting this perspective better equips the designers of a DSS to address the most challenging task for the CBR method — namely adaptation. In medical applications it is almost impossible to generate adaptation rules that consider all possible important differences between current and past similar cases. Therefore, some adaptation solutions have been developed that are rather typical for medical domains [59], one being to generalize from single cases into abstracted prototypes or classes, since a problem for adaptation is the extreme speci<sup>fi</sup>city of single cases. This can be achieved by retrieving past cases at the cluster level as described in the “case retrieval” step detailed in this study.

It is noteworthy that the generic nature of the proposed approach provides enough <sup>fl</sup>exibility to customize it to other domains including, for example, customer relationship management and customer care. This and the applicability and useability of our DSS for other complex settings and countries, constitute interesting and promising directions for future research. Moreover, further research could explore external evaluation of the framework with experts and users.

In conclusion, our framework for the proposed intelligent DSS draws together a new operative and robust methodology that can be used to generate the required evidence to support GPs' decision making and achieve more effective and appropriate pathology test ordering. Further, our process and framework contribute effective guidance for practitioners as well as theoretical understanding concerning intelligent decision support in a complex environment.

## Appendix A. Overview of the survey instrument

The survey commenced by asking general information about the participants. For example, gender, age group, and practice location, Section 1 then posed, case by case, the 20 hypothetical clinical cases, followed by feedback, while Section 2 focused on GPs' perceptions of/requirements for an intelli gent DSS. For illustrative purposes we have shown a screen shot of hypothetical case 1 below.

Case 1  
A 65 vear old woman with diabetes is being treated with oral hypoglycaemic agents, Over the 6 months she has demonstrated a stable HbA1c of 7.5% and also has a good lipid profile apart from triglycerides which remain over 3 mmol/L. Her creatinine level was normal 9 months ago and there has been no evidence of microalbuminuria on the last 2 tests this year. She is looking forward to seeing that her next set of results remain good.

<table><tr><td colspan="4">Q1: What tests would you order?</td></tr><tr><td>Full blood examination</td><td>ESR</td><td>Multibiochemical analysis</td><td>Uric acid - serum</td></tr><tr><td>Lipid profile</td><td>INR for warfarin</td><td>Serum glucose</td><td>Histology</td></tr><tr><td>Plasma glucose</td><td>TSH</td><td>Iron studies</td><td>Hepatitis serology</td></tr><tr><td>LFTs</td><td>Pap smear</td><td>HbA1c</td><td>CRP</td></tr><tr><td>Urea electrolytes creatinine</td><td>Urine MC&amp;S</td><td>PSA</td><td>Hormone profile</td></tr></table>

Q2: Why do you order these test (Please select the power of Opinion) Suggestion: You can select the reasons below for detailed explanation.

<table><tr><td></td><td>1 (Very strong)</td><td>2</td><td>3</td><td>4</td><td>5 (Not strong)</td></tr><tr><td>Screening</td><td>○</td><td>○</td><td>○</td><td>○</td><td>○</td></tr><tr><td>Diagnosis</td><td>○</td><td>○</td><td>○</td><td>○</td><td>○</td></tr><tr><td>Monitoring</td><td>○</td><td>○</td><td>○</td><td>○</td><td>○</td></tr><tr><td>Prognosis</td><td>○</td><td>○</td><td>○</td><td>○</td><td>○</td></tr><tr><td>Patient pressure</td><td>○</td><td>○</td><td>○</td><td>○</td><td>○</td></tr><tr><td>Defensive behavior</td><td>○</td><td>○</td><td>○</td><td>○</td><td>○</td></tr><tr><td>Guidelines</td><td>○</td><td>○</td><td>○</td><td>○</td><td>○</td></tr><tr><td>Cost consideration</td><td>○</td><td>○</td><td>○</td><td>○</td><td>○</td></tr></table>

Other reasons (if any):

Submit

back to case index

## References

[1] A. Aamodt, E. Plaza, in: Case-Based Reasoning: Foundational Issues, Methodological Variations, and System Approaches, AI Commun., 7(1), IOS press, 1994, pp. 39–59.

[2] M.D. Ahearn, S.J. Kerr, General practitioners' perceptions of the pharmaceutical decision-support tools in their prescribing software, The Medical Journal of Australia 179 (2003) 34–37.

[3] R. Amarasiri, D. Alahakoon, M. Premaratne, K. Smith, HDGSOMr: a high dimensional growing self organizing map using randomness for ef<sup>fi</sup>cient web and text mining, in: Proceedings of IEEE/ACM/WIC Conference on Web Intelligence Paris France 2005 pp. 215–221

[4] R. Amarasiri, J. Ceddia, D. Alahakoon, Exploratory data mining lead by text mining using a novel high dimensional clustering algorithm, in: Proceedings of 4th inter national Conference on Machine Learning Applications (ICMLA '05), Los Angeles, California, USA, 2005, pp. 267–272.

[5] N. Arshadi, I. Jurisica, Data mining for case-based reasoning in high-dimensional biological domains, IEEE Transactions on Knowledge and Data Engineering 17 (8) (2005) 1127–1136.

[6] M.B. Ayed, H. Lti<sup>fi</sup>, C. Kolski, A.M. Alimi, A user-centered approach for the design and implementation of KDD-based DSS: a case study in the health care domain, Decision Support Systems 50 (1) (2010) 64–78.

[7] N.L. Beebe, J.G. Clark, G.B. Dietrich, M.S. Ko, D. Ko, Post-retrieval search hit clustering to improve information retrieval effectiveness: two digital forensics case studies, Decision Support Systems 51 (4) (2011) 732–744.

[8] A. Bennet, D. Bennet, The decision-making process in a complex situation, in: F. Burstein, C.W. Holsapple (Eds.), Handbook on Decision Support Systems, Springer, Berlin, 2008, pp. 3–20.

[9] In: E.S. Berner (Ed.), Clinical Decision Support Systems: Theory and Practice, Springer, New York, 2007.

[10] N. Bolshakova, F. Azuaje, Improving expression data mining through cluster validation, in: Proceedings of the 4th Annual IEEE Conference on Information Technology Applications in Biomedicine, 2003, pp. 19–22.

[11] H. Britt, An analysis of pathology test use in Australia, A Paper by the Australian Association of Pathology Practices Inc., Family Medicine Research Centre, University of Sydney, 2008.

[12] H. Britt, S. Knox, G.C. Miller, Changes in pathology ordering by general practitioners in Australia 1998–2001, in: AIHW Cat. No. GEP 13. A joint report by the University of Sydney and the Australian Institute of Health and Welfare (General Practice Series No. 13), 2003.

[13] H. Britt, G.C. Miller, J. Charles, Y. Pan, L. Valenti, J. Henderson, C. Bayram, J. O'Halloran, S. Knox, General Practice Activity in Australia 2004-05. (AIHW cat. no. GEP 19) Australian Institute of Health and Welfare, Canberra, 2007. (General Practice Series No. 19).

[14] F. Burstein, S.A. Carlsson, Decision support through knowledge management, in: F. Burstein, C.W. Holsapple (Eds.), Handbook on Decision Support Systems, Springer, Berlin, 2008, pp. 103–120.

[15] J.S. Carson, Convincing users of model's validity is challenging aspect of modeler's job, Industrial Engineering 18 (6) (1986) 74–85.

[16] B. Chaudhry, J. Wang, S. Wu, M. Maglione, W. Mojica, E. Roth, S.C. Morton, P.G. Shekelle, Systematic review: impact of health information technology on quality, ef<sup>fi</sup>ciency, and costs of medical care, Annals of Internal Medicine 144 (2006) 742.

[17] P. Clerkin, C. Hayes, P. Cunningham, Automated case generation for recommender systems using knowledge discovery techniques, in: Trinity College Dublin Computer Science Department Technical Report, April, 2002.

[18] E. Coiera, J.I. Westbrook, J.C. Wyatt, The safety and quality of decision support systems, in: IMIA Yearbook of Medical Informatics, 2006, pp. 20–26.

[19] T.D. Cook, D.T. Campbell, Quasi-experimentation: Design & Analysis Issues for Field settings, Rand McNally College Pub, Chicago, 1979.

[20] K. Cox, Evidence-based medicine and everyday reality, The Medical Journal of Australia 175 (2001) 382–383.

[21] R.S. Dalal, S. Bonaccio, What types of advice do decision-makers prefer? Organizational Behavior and Human Decision Processes 112 (2010) 11–23.

[22] D. Davis, R.M. Cosenza, Business Research for Decision Making, Wadsworth, Belmont, California, 1993.

[23] G. Deboeck, T. Kohohnen, Visual Explorations in Finance with Self-Organizing Maps, Springer-Verlag, London, 1998.

[24] A. Enno, M. Foster, P. Hines, Quality use of pathology by general practitioners, in: Final Report to the Hunter Urban Division of General Practice (HUDGP), 2000, (Available at http://www.hudgp.org.au. Accessed 17 May 2004).

[25] Eudaptics Software Gmbh, Viscovery Somine (Standard Edition 3.0), Edaptics Software Gmbh, Wein, 1999.

[26] E. Fantino, S. Stolarz-Fantino, Decision-making: context matters, Behavioural Processes 69 (2005) 165–171.

[27] M. Foster, M. Cahill, J. Harris, Building on quality, in: Final report to the Hunter Urban Division of General Practice (HUDGP), 2001, (Available at http://www. hudgp.org.au. Accessed 07 September 2004).

[28] P. Glasziou, B. Haynes, The pathos from research to improved health outcomes, Evidence-Based Medicine 10 (2005) 4–7.

[29] R. Guibert, S. Wicker, M. Horrocks, Background reading for QUP-GP workshop, the development of a research proposal to address the appropriate use of pathology to general practice — stage 1, in: The Royal Australian College of General Practitioners Research and Practice Support Directorate, prepared, 31 August-1 September 2001.

[30] D.J. Hall, Decision makers and their need for support, in: F. Burstein, C.W. Holsapple (Eds.) Handbook on Decision Support Systems Springer, Berlin 2008 pp, 83–102

[31] J. Han, M. Kamber, Data Mining: Concepts and Techniques, second ed. Morgan Kaufmann, San Francisco, 2006.

[32] K. Hannes, M. Leys, E. Vermeire, B. Aertgeerts, F. Buntinx, A.M. Depoorter, Implementing evidence-based medicine in general practice: a focus groups based study, BMC Family Practice 6 (2005) 37.

[33] J. Henderson, H. Britt, G. Miller, Extent and utilization of computerization in Australian general practice, The Medical Journal of Australia 185 (2006) 84–87.

[34] W. Hersh, Health care information technology: progress and barriers, JAMA : The Journal of the American Medical Association 292 (18) (2004) 2273–2274.

[35] A.R. Hevner, S.T. March, J. Park, S. Ram, Design science in information systems research, MIS Quarterly 28 (1) (2004) 75–106.

[36] C.W. Holsapple, Decisions and knowledge, in: F. Burstein, C.W. Holsapple (Eds.), Handbook on Decision Support Systems, Springer, Berlin, 2008, pp. 21–53.

[37] M.R. Kidd, D. Mazza, Clinical practice guidelines and the computer on your desk, The Medical Journal of Australia 173 (2000) 373–375.

[38] T. Kohonen, Self-organized formation of topologically correct feature maps, Biological Cybernetics 43 (1982) 59–69.

[39] T. Kohonen, The self organizing map, IEEE Proceedings 78 (9) (1990) 1464–1480.

[40] T. Kohonen, Self Organizing Maps, third ed. Springer, Berlin, 2001.

[41] J.L. Kolodner, Case-Based Reasoning, Morgan Kaufmann Publishers, San Mateo, CA, 1993.

[42] M. Legg, I. Cheong, A Study of the Impact of the Use of General Practice Computer Systems on the Ordering of Pathology, Department of Health and Ageing, 2004.

[43] G.D. Lundberg, Perseveration of laboratory test ordering: a syndrome affecting clinicians, JAMA : The Journal of the American Medical Association 249 (5) (1983) 639.

[44] G.D. Lundberg, Changing physician behaviour in ordering diagnostic tests, JAMA : The Journal of the American Medical Association 280 (23) (1998) 20–36.

[45] G.D. Lundberg, The need for an outcomes research agenda for clinical laboratory testing, JAMA : The Journal of the American Medical Association 280 (6) (1998) 565–566.

[46] G.M. Marakas, Decision Support Systems in the 21st Century, second ed. Prentice Hall, London, 2003.

[47] D.K. Mclnnes, D.C. Saltman, M.R. Kidd, General practitioners' use of prescribing and electronic health records: results from a national survey, The Medical Journal of Australia 185 (2006) 88–91.

[48] Medicare Statistics Department of Health and Ageing. Available at: http://www. health.gov.au2008(accessed 20 May 2009).

[49] S. Miyakis, G. Karamanof, M. Liontos, T.D. Mountokalakis, Factors contributing to inappropriate ordering of tests in an academic medical department and the effect of an educational feedback strategy, Postgraduate Medical Journal 82 (2006) 823–829.

[50] H.J. Murff, T.K. Gandhi, A.K. Karson, E.A. Mort, E.G. Poon, S.J. Wang, D.G. Fairchild, D.W. Bates, Primary care physician attitudes concerning follow-up of abnormal test results and ambulatory decision support systems, International Journal of Medical Informatics 71 (2–3) (2003) 137–149.

[51] M. Nilsson, M. Sollenborn, Advancements and trends in medical case-based reasoning: an overview of systems and system development, in: Proceedings of the 17th International FlAIRS Conference, Special Track on Case-Based Reasoning, American Association for Arti<sup>fi</sup>cial Intelligence, Miami, USA, 2004, pp. 178–183.

[52] J.M. Overhage, W.M. Tierney, X.H. Zhou, C.J. McDonald, A randomized trial of corollary orders to prevent errors of omission, Journal of the American Medical Informatics Association 4 (1997) 364–375.

[53] C.K. Page, Critical success factors for implementing clinical information system, Nursing Economics 18 (5) (2000) 255–261.

[54] M. Porter, An algorithm for suf<sup>fi</sup>x stripping, Program 14 (3) (1980) 130–137.

[55] S. Robinson, Simulation model verification and validation: Increasing the uses' confidence, Proceedings of the 1997 Winter Simulation Conference. Edited by S. Andradottir. K.I. Healy. D.H. Withers, and B.I Nelson.

[56] Royal College of Pathologists of Australasia, Revision of manual of use and interpretation of pathology tests, in: Final Progress Report to the Commonwealth Department of Health and Ageing, Department of Health and Ageing, 2004.

[57] Royal College of Pathologists of Australasia, Common-sense pathology, in: Final Report to the Commonwealth Department of Health and Ageing, Department of Health and Ageing, 2006.

[58] G. Salton, C. Buckley, Term-waiting approaches in automatic text retrieval, Information Processing and Management 24 (5) (1998) 513–523.

[59] R. Schmidt, S. Montani, R. Bellazzi, L. Portinale, L. Gierl, Case-based reasoning for medical knowledge-based systems, International Journal of Medical Informatics 64 (2001) 355–367.

[60] D. Short, M. Frischer, J. Bashford, Barriers to the adoption of computerized decision support systems in general practice consultations: a qualitative study of GPs' perspectives, International Journal of Medical Informatics 73 (2004) 357–362

[61] K. Shuval, A. Shachak, S. Linn, M. Brezis, P. Feder-bubis, S. Reis, The impact of an evidence-based medicine educational intervention on primary care physicians: a qualitative study, Journal of General Internal Medicine 22 (2007) 327–331.

[62] E.-G. Siew, K. Smith, L. Churilov, M. Ibrahim, A neural clustering approach for iso-resource grouping for acute healthcare in Australia, in: Proceedings of the 35 Annual Hawaii International Conference on Systems Science (HICS 35), IEEE Computer Society, Hawaii USA, 2002.

[63] D.F. Sittig, M.A. Krall, R.H. Dykstra, A. Russell, H.L. Chin, A survey of factors affecting clinician acceptance of clinical decision support, BMC Medical Informatics and Decision Making 6 (2006) 6.

[64] W.S.A. Smellie, Appropriateness of test use in pathology: a new era or reinventing the wheel? Annals of Clinical Biochemistry 40 (2003) 585–592.

[65] W.S.A. Smellie, M.J. Galloway, D. Chinn, Benchmarking general practice use of pathology services: a model for monitoring change, Journal of Clinical Pathology 53 (2000) 476–480.

[66] W.S.A. Smellie, D.I. Finnigan, D. Wilson, D. Freedman, C.A.M. McNulty, G. Clark, Methodology for constructing guidance, Journal of Clinical Pathology 58 (2005) 249–253.

[67] P.J. Stuart, S. Crooks, M. Porton, An interventional program for diagnostic testing in the emergency department, The Medical Journal of Australia 177 (2002) 131–134.

[68] M.R. Sumner, J. Bradley, CSF's for implementing ERP within SME's, in: Proceedings of the Fifteenth Americas Conference on Information Systems: paper 550, Association of Information Systems, San Francisco CA, 2009.

[69] W.M. Tierney, J.M. Overhage, M.D. Murray, L.E. Harris, X.H. Zhou, G.J. Eckert, F.E. Smith, N. Nienaber, C.J. McDonald, F.D. Wolinsky, Effects of computerized guidelines for managing heart disease in primary care, Journal of General Internal Medicine 18 (2003) 967–976.

[70] C.S. Tracy, G.C. Dantas, R. Moineddin, R.E.G. Upshur, Contextual factors in clinical decision making: national survey of Canadian family physicians, Canadian Family Physicians 51 (2005) 1106–1107.

[71] V. Vaishnavi, W. Kuechler, Design science research in information systems (January 20, 2004). last updated September 30, 2011. URL: http://desrist.org/desrist.

[72] T. van der Weijden, M.A. van Bokhoven, G.J. Dinant, C.M. van Hasselt, R.P.T.M. Grol, Understanding laboratory testing in diagnostic uncertainty: a qualitative study in general practice, British Journal of General Practice 52 (485) (2002) 974–980.

[73] M.B. van der Weyden, Databases and evidence-based medicine in general practice, The Medical Journal of Australia 170 (1999) 52–53.

[74] C. van Walraven, C.D. Naylor, Do we know what inappropriate laboratory utilization is? A systematic review of laboratory clinical audits, JAMA : The Journal of the American Medical Association 280 (1998) 550–558.

[75] C. van Walraven, M. Raymond, Population-based study of repeat laboratory test ing, Clinical Chemistry 49 (2003) 1997–2005.

[76] T.J. Wang, E.A. Mort, P. Nordberg, Y. Chang, M.E. Cadigan, L. Mylott, L.V. Ananian, B.T. Thompson, M. Fessler, W. Warren, A. Wheeler, M. Jordan, M. Fifer, A utilization management intervention to reduce unnecessary testing in the coronary care unit, Archives of Internal Medicine 162 (2002) 1885–1890.

[77] S.N. Weingart, M. Toth, D.Z. Sands, M.D. Aronson, R.B. Davis, R.S. Phillips, Physicians' decisions to override computerized drug alerts in primary care, Archives of Internal Medicine 163 (21) (2003) 2625–2631.

[78] L. Wells, Role of information technology in evidence based medicine: advantages and limitations, The Internet Journal of Healthcare Administration 4 (2) (2007).

[79] B.G. Wertman, S.V. Sostrin, Z. Pavlova, G.D. Lundberg, Why do physicians order laboratory tests? A study of laboratory test request and use patterns, JAMA : The Journal of the American Medical Association 243 (1980) 2080–2082.

[80] J.A. Weydert, N.D. Nobbs, R. Feld, J.D. Kemp, A simple, focused, computerized query to detect overutilization of laboratory tests, Archives of Pathology & Laboratory Medicine 129 (9) (2005) 1141–1143.

[81] Q. Yang, J. Wu, Keep it simple: a case-base maintenance policy based on clustering and information theory, in: Proceedings of the Canadian AI Conference, 2000, pp. 102–114.

[82] Z.Y. Zhuang, L. Churilov, K. Sikaris, Uncovering the patterns in pathology ordering by Australian general practitioners: a data mining perspective, in: Proceedings of the 39th Annual Hawaii International Conference on System Sciences (HICSS 39), IEEE Computer Society, Washington DC USA, 2006.

[83] Z.Y. Zhuang, R. Amarasiri, L. Churilov, D. Alahakoon, K. Sikaris, Exploring the clinical notes of pathology ordering by Australian general practitioners: a text mining perspective, in: Proceedings of the 40th Annual Hawaii International Conference on System Sciences (HICSS 40), IEEE Computer Society, Washington DC USA, 2007.

[84] Z.Y. Zhuang, L. Churilov, F. Burstein, K. Sikaris, Combining data mining and case-based reasoning for intelligent decision support for pathology ordering by general practitioners, European Journal of Operational Research 195 (3) (2009) 662–675.

Zoe Y. Zhuang is a member of the Department of Accounting and Finance, Faculty of Business and Economics, Monash University, Australia. She holds a BArts from Nanjing University, China and a MBA and PhD from Monash University. A major theme of her research concerns the appropriate use of pathology ordering in Australia. Dr Zhuang has published in journals such as European Journal of Operations Research and conferences including the Hawaii International Conference on System Sciences.

Carla L. Wilkin is an Associate Professor of Accounting Information Systems in the Department of Accounting and Finance, Faculty of Business and Economics, Monash University, Australia. She holds a BCom (Hons) and a PhD from Deakin University and a Grad Cert Higher Ed from Monash University. Dr Wilkin's major research interests concern: governing IT; system use, appropriation, innovation, diffusion and infusion; measurement of the value of IT; and risk in business processes. She has published in outlets such as European Journal of Information Systems, IT & People, Electronic Commerce Research, Journal of Information Systems, International Journal of Accounting Information Systems, Electronic Journal of Information Systems Evaluation, Communications of the ACM, Data Base for Advances in Information Systems and the Journal of Organizational and End User Computing. Further, she is on the editorial board of the International Journal on IT/Business Alignment and Governance, Journal of Organizational and End User Computing, and International Journal of Accounting Information Systems.

Andrzej Ceglowski is a Senior Lecturer in the Department of Accounting and Finance, Faculty of Business and Economics, Monash University, Australia. He holds a BSc from the University of KwaZulu-Natal and a MBSys (res) and PhD from Monash University. His research interests include business strategy, healthcare modeling and applications of arti<sup>fi</sup>cial intelligence in management, which have evolved from his PhD thesis about Emergency Hospital Management. Dr Ceglowski has published in outlets including the International Journal of Healthcare Information Systems and Informatics, and the Journal of the Operational Research Society.
