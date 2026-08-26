---
otero_id: 14370
otero_key: "FY6RNHBH"
title: "Directed disease networks to facilitate multiple-disease risk assessment modeling"
authors: "Tingyan Wang; Robin G. Qiu; Ming Yu; Runtong Zhang"
year: "2020"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2019.113171"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Directed disease networks to facilitate multiple-disease risk assessment modeling

Tingyan Wang<sup>a,b</sup>, Robin G. Qiu<sup>c,⁎</sup>, Ming Yu<sup>a</sup>, Runtong Zhang

<sup>a</sup> Health Care Services Research Center, Department of Industrial Engineering, Tsinghua University, Beijing 100084, China

<sup>b</sup> Nufield Department of Medicine, University of Oxford, South Parks Road, Oxford OX1 3SY, United Kingdom

<sup>c</sup> Big Data Lab, Division of Engineering and Information Science, The Pennsylvania State University, Great Valley, Malvern, PA 19355, United States

<sup>d</sup> Department of Information Management, School of Economics and Management, Beijing Jiaotong University, Beijing 100044, China

## A R T I C L E I N F O

Keywords: Multiple-disease risk prediction Health risk assessment Disability adjusted life year Directed network Disease temporal relations

## A B S T R A C T

We investigate multiple disease risk prediction modeling, aimed at assessing future disease risks for an individual who is ready for discharge after hospitalization. We propose a novel framework that combines directed disease network and recommendation system techniques to substantially enhance multiple disease risk predictive modeling. Firstly, a directed disease network considering temporal information is developed. Then based on this directed disease network, we look into diferent disease risk score computing approaches. We validate the proposed approaches with two real-world datasets from two independent hospitals. The predicted results can be promisingly utilized as a reference for medical experts to ofer efective healthcare guidance for both inpatients and outpatients. The proposed framework can also be utilized for developing an innovative tool that helps individuals create and maintain a better healthcare plan over time.

## 1. Introduction

Identification of disease risks and intervention at the earliest stage can lead to better medical results and lower medical cost [1]. Knowing disease risks in time helps not only improve healthcare services but also reduce re-admission rate [2], which facilitates building strong and healthy communities over time. However, currently millions of individuals sufer from late-diagnosed chronic diseases [3], which causes heavy burdens to the society [4]. Recently, the assessment of health risks has drawn much attention in academia and practice, yet the accuracy of health risk evaluation remains one of the main challenges in healthcare research [1]. Therefore, to improve the accuracy of health risk assessment for an individual, it is essential to study multi-disease risk prediction modeling in a systematic way.

As hospital information systems are widely adopted, there is a tremendous amount of health-related information in electronic health records (EHRs), which could be well utilized to benefit patient-centered healthcare. For example, medical records containing information con cerning disease correlations and progression are particularly funda mental to multiple disease risk evaluations [5–9]. Many researchers have exploited comorbidity relationships among diseases based on medical histories of patients for multiple disease risk prediction modeling [10–14], which focused on disease prediction modeling through investigating concurrence of diseases while excluding their temporal relations among aflicted diseases. Researchers recently started to take into account temporal information to study directed disease networks [6,7] or directly incorporate disease temporal relations into disease risk predictive modeling [4,15,16]. However, there is limited literature studying multiple disease prediction modeling using directed disease networks to fully mine and leverage the temporal information in EHRs.

In this study, we formulate the multiple disease prediction as a medical recommendation system problem and propose a novel framework that combines directed disease network and recommendation system techniques for multiple disease risk prediction modeling. To validate the applicability of the framework, we apply the proposed framework to two archived medical datasets provided by two general hospitals in Beijing and Shenzhen, China, respectively.

The remaining paper is organized as follows. Section 2 presents the problem under study. Section 3 reviews the related literature. Section 4 then details the proposed multiple disease risk modeling. Data analysis and results based on hospital datasets are presented in Section 5. Lastly, Section 6 discusses the application of the proposed framework, and the contributions and limitations of this study, and Section 7 concludes this study.

Table 1  
A sample of medical records of a patient.

<table><tr><td>Patient ID</td><td> $n^{th}$  visit</td><td>Diagnosis codes</td></tr><tr><td>P1</td><td>1</td><td>N18.001, I10, I15.101, N03.801, J92.901, J98.401, E83.501, D64.802, N28.101</td></tr><tr><td>P1</td><td>2</td><td>N18.001, I10, I15.101 N03.801, J92.901, D64.802</td></tr><tr><td>P1</td><td>3</td><td>N18.001, I10, I15.101, N03.801, E04.101, D64.802</td></tr></table>

## 2. Problem statement

In general, there are two diferent ways of conducting disease prediction modeling: (a) single disease prediction modeling, which involves only one type of disease in risk assessment, (b) multiple disease prediction modeling, which aims to identify all diseases that an individual might develop. The former is a disease-centric model that predicts the likelihood of an individual getting a specific disease regardless of whether other diseases will occur to this individual. The latter is a patient-centric model that focuses on assessing multiple dis ease risks for an individual simultaneously. In this study, we concentrate on multiple disease prediction modeling. It is worth men tioning that some studies involve several diseases. However, their prediction approaches are either based on one disease at a time [17] or a limited number of specific diseases simultaneously [18,19]. Because this study focuses on simultaneously assessing all the future disease risks for a patient, their studies are diferent from our work.

Many patients experienced hospital re-admissions due to suboptimal healthcare, chronic conditions, or sufering additional diseases [2,20]. Each hospital visit of a patient produces a set of medical diagnoses. As shown in Table 1, each row represents a hospital visit of a patient. The first column indicates the patient's identification, the second column denotes the sequence number of each hospital visit. and the third column includes the patient's diagnosis in each hospital visit. Patients diagnoses in the raw datasets under study have been encoded according to the 10th Revision of International Statistical Classification of Dis eases and Related Health Problems (ICD-10) [21,22].

In this study, the question is how to predict disease risks of a patient over time based on the patient's medical history. This question is motivated by the fact that doctors are interested in knowing which diseases a patient might sufer in the future so that better medical advice can be provided to the patient when she/he gets discharged from the hospital. In this study, we formulate this prediction problem as a recommenda tion system rather than a multi-label classification problem. The input to our model is medical records of patients, and the output is a list of ordered diseases that the target patient may be aflicted with on the subsequent hospital visit. As an excessively long recommended list of diseases would be inappropriate in practice, we provide a recommended list with a fixed length, denoted as Q that can be changed, depending on the needs of medical experts, professionals, or the patients.

## 3. Related work

Lots of researchers have studied single disease prediction modeling, e.g., heart disease prediction [23]. The methods used for a single dis ease prediction problem are classifiers, such as neural networks, deci sion tree, Naïve Bayes, random forest, logistic regression, support vector machine, Bayesian network, deep learning and so on [17,24–26]. Two metrics, relative risk and odds ratio, are frequently used in single disease risk assessment to quantify the relationship between an independent variable and the dependent variable of interest, i.e., the causal efect or exposure efect for a single disease [27,28].

To clearly show how we enrich the literature in addressing multiple disease prediction problems, we summarize the state-of-the-art in the field in Table 2. It shows that there are limited studies using directed disease networks to leverage temporal information in multi-disease prediction modeling. Next, the studies in Table 2 are reviewed in detail.

<table><tr><td></td><td>Recommendation algorithms</td><td>Undirected disease network</td><td>Directed disease network</td><td>Other methods</td></tr><tr><td>Without incorporating temporal information</td><td>Davis et al. [10]; Chawla and Davis [2]; Dasgupta and Chawla [29]</td><td>Steinhaeuser and Chawla [11]; Folino et al. [34]; Folino and Pizzuti [13]; Lakshmi and Vadivu [9]</td><td>-</td><td>Folino and Pizzuti [12]; McCormick et al. [35]; Rider and Chawla [14]; Chang et al. [18]; Wang et al. [36]; Li et al. [37]; Bayati et al. [1]; Maxwell et al. [19]</td></tr><tr><td>Incorporating temporal information</td><td>Davis et al. [30]; Ji et al. [31–33]; Nasiri et al. [4]</td><td>-</td><td>Our study; Jensen et al. [6]; Kannan et al. [7]</td><td>Folino and Pizzuti [16,17]; Miotto et al. [39]; Choi et al. [40]; Razavian et al. [41]; Kim et al. [42]; Ma et al. [43]; Nguyen et al. [44]</td></tr></table>

Note: the studies are listed in the order of their published time.  
Studies for multiple disease prediction.

Future disease risk assessments for an individual using recommendation algorithms while without considering disease temporal information have been exploited. Davis et al. [10] proposed a model called Collaborative Assessment and Recommendation Engine (CARE), which is considered as one of the earliest studies that applied collaborative filtering to predict multi-disease risks. They identified top disease risks for a patient by comparing the patient's profile with similar patients' profiles. They also developed an iterative version to enhance CARE, called ICARE. The results demonstrate that collaborative filtering has practical potential in multiple disease prediction. Chawla and Davis [2] promoted the application of CARE and ICARE for personalized healthcare. By incorporating medication information, Dasgupta and Chawla [29] developed medCARE and combinedCARE based on CARE and articulated that combinedCARE improved outcomes.

By contrast, with the support of recommendation algorithms other researchers have been trying to directly incorporate temporal information among diseases for multiple disease prediction. Davis et al. [30] extended ICARE to time-sensitive ICARE by leveraging long itudinal EHRs data. Ji et al. [31–33] proposed a framework using col laborative filtering that not only predicts medical condition incidences but also reveals disease progression trajectories. Nasiri et al. [4] designed a recommendation algorithm based on tensor factorization to predict disease risks for patients. By incorporating the time dimension, this algorithm shows better results compared with ICARE.

To take advantage of the phenotypic information of diseases, some researchers have tried to develop a multi-disease risk prediction model through construction of disease networks using patients' medical histories. Steinhaeuser and Chawla [11] built an undirected disease network, in which nodes are the diseases and each edge weight is assigned with the ratio of co-occurrence of two diseases by the same patient. Then nearest neighbor method and depth-first search technique were applied to assess disease risks for a patient. Similarly, Folino et al. [34] designed an undirected phenotypic disease network, in which each edge is labeled with the number of patients who share the same diseases. Then they applied association rule analysis to find disease frequent patterns. Folino and Pizzuti [13] also constructed a comorbidity network of diseases and applied link prediction approaches to inferring new disease correlations among their study cohort. Lakshmi and Vadivu [9] developed a method based on weighted association rule mining to predict disease comorbidities using both clinical and molecular data. Although the undirected network-based methods can incorporate the comorbidity relations of diseases, unfortunately, models based on un directed networks can't integrate the temporal information between diseases.

In addition to recommendation algorithms and undirected disease network, there are some other methods without incorporating temporal information, such as association rule analysis [12,33], topic model [14], classifiers [1,18,36,37] and deep learning [39], proposed for the multiple disease prediction. Folino and Pizzuti [12] developed a system called CORE (COmorbidity-based Recommendation Engine), by clustering patients' medical records first and then applying association rule analysis in the disease risk prediction modeling. Rider and Chawla [14] proposed a modified Dirichlet process mixture model to allow aggregating distinct EHR datasets so as to enhance the performance of disease risk predictions; McCormick et al. [35] proposed a hierarchical association rule model to generate association rules for predicting future medical conditions; Maxwell et al. [19] used deep neural networks to predict 8 types of disease risks. However, models based on classifiers are generally like ‘black boxes’, which lack interpretability [3,38].

To incorporate the temporal information, Folino and Pizzuti [15,16] proposed CORE<sup>+</sup> by integrating Markov models and sequential pattern mining instead of frequent pattern mining into CORE. With combining more models and considering the hospital visit sequence of a patient, CORE<sup>+</sup> is superior to CORE with respect to the prediction accuracy.

Recently, scholars have begun to leverage deep learning classification algorithms to predict multi-disease risks or a specific set of diseases: Miotto et al. [39] used unsupervised deep learning to derive a patient representation from various types of medical records in EHRs for predicting disease risks; Choi et al. [40] applied gated recurrent units based recurrent neural network (RNN) to predict the diagnoses and medications of the subsequent visit for a patient; Razavian et al. [41] used neural networks to predict disease onsets based on longitudinal measurements of lab tests; Kim et al. [42] applied deep attention networks to predict vascular diseases based on diagnosis and pharmacy codes; Ma et al. [43] employed bidirectional RNNs to predict diagnosis codes; Nguyen et al. [44] modeled the sequences of patients' visits using RNN to predict disease risks for patients with diabetes and mental health problems. The achievements from these studies based on RNN were remarkable to some extent. However, RNN-based approaches may not fully leverage all the previous visit information of patients, which requires further investigations [43].

Recently, some researchers have explored clinical relationships and disease trajectories by constructing directed networks: Jensen et al. [6] derived disease trajectories by investigating temporal patterns among pairs of diagnoses; Kannan et al. [7] introduced a causal information fraction measure to determine the directionality of disease trajectories. In this study, rather than only focusing on disease trajectories, we use a directed disease network to facilitate multiple disease prediction modeling. With combining directed disease network and recommendation system techniques, we can fully incorporate and leverage chronological orders between patients' successive hospital visits.

## 4. Methodology

In this section, we introduce our multi-disease prediction modeling based on our preliminary study [45]. Fig. 1 depicts the modeling flow and main activities in the proposed modeling methodology. In the following sections, we describe each step of the proposed methodology in detail.

## 4.1. Grouping and ranking diseases with disability-adjusted life year

Let's firstly explain the reason for grouping and ranking diseases. ICD-10 is a standard dictionary for the classification of diseases and related health problems. Each disease has a code in the dictionary. The top categories of ICD-10 codes and the code descriptions are available online [22].

According to ICD-10, there are over ten thousand diseases marked with four characters (excluding the decimal point). However, from the perspective of health risk management, there is no need for us to conduct disease risk analysis at this excessively detailed level. In other words, diseases can be systematically categorized into levels for easy interpretation and management in hospitals.

Since severity levels of disease risks vary with countries or geographical regions, they should be identified within the group or population under study. Therefore, country-based severity levels can help identify what diseases afect patients more severely and how those diseases can be geographically controlled and managed in an efective manner. In light of this, we aggregate diseases into groups using Disability-Adjusted Life Year (DALY), which is a comprehensive metric of disease burdens designed by WHO [46]. DALY has been widely promoted by WHO to quantify the burden of disease from mortality and morbidity. As defined by WHO, “DALY for a disease or health condition are calculated as the sum of the Years of Life Lost due to premature mortality in the population and the Years Lost due to Disability for people living with the health condition or its consequences”. One DALY can be thought of as one lost year of “healthy” life due to the afliction of a disease. Hence, DALY is an excellent reference used to assess the burden or severity of a disease.

![](/api/attachments/FY6RNHBH/fulltext/images/051b8028c21b9041984f8649a5fb53b8c559d709ccaec6e6a2f1cdb6aac64bf2.jpg)  
Fig. 1. The process overview of multiple disease prediction modeling in this study.

DALY has been applied to estimating disease burdens. Particularly, DALY has been used to classify diseases into categories easily manageable in hospitals. WHO Global Health Estimates (GHE) provides datasets of DALY estimates for all WHO members [47]. Hence, we adopt DALY in our multiple disease risk prediction modeling. Essentially, each category of DALY estimates represents a group of diseases, i.e., a set of ICD codes. There are 125 disease groups sorted by the DALY estimates for China population, which can be represented in a descending order, such as $D _ { 1 } , D _ { 2 } , \cdots , D _ { 1 2 5 }$ . These ranked disease groups will then be used as nodes to construct a directed network. Apparently, the proposed methods can be easily extended to other countries or globally.

## 4.2. Data preprocessing methods

Two steps are used for preprocessing a raw dataset before a model can be developed:

(1) Mapping patients' diagnostic results to the ranked disease groups of DALY

As for raw medical records, the ICD-10 codes of medical diagnoses have more than 4 characters (excluding the decimal point) in length, covering over ten thousand diseases. To use the ranked disease groups of DALY as the nodes of a directed network, these medical diagnostic results need to be aggregated and mapped into the above-mentioned ranked disease groups. As a result, each patient has a set of diseases with ranked numbers in a chronological order.

## (2) Data transformation for directed disease network design

To construct a directed disease network, we must transform the data in a way of showing the temporal relations between a patient's two consecutive hospital visits. As illustrated in Fig. 2, the column named id denotes the hospital identification of a patient; the column named $n ^ { t h }$ indicates the $n ^ { t h }$ visit of the patient's hospital visits. For the column $D _ { i } ,$ $i = 1 , 2 , \cdots , 1 2 5 .$ , the value is 1 if a patient sufers from disease $D _ { i } ,$ and 0 otherwise.

In Fig. $^ { 2 , }$ for matrix U, we merge the records of the $n ^ { t h }$ and the $( n + 1 ) ^ { t h }$ hospital visit into one record, thus we obtain matrix V. For example, as illustrated in Fig. 2, the records of the first visit and the second visit of the first patient can be merged into one record. Therefore, with the data transformation by converting two records of con secutive visits into one, matrix V can clearly describe the temporal relations of diseases between a patient's two consecutive visits.

## 4.3. Directed disease network design

In this section, we illustrate how to develop a directed network by leveraging chronological orders between successive hospital visits to investigate temporal relations among diseases.

A directed disease network can be easily developed. A vertex x in the network denotes a disease. A directed arc $( x , y )$ indicates disease x pointing to disease y, which is constructed from patients' two consecutive visits. The flow of the directed arc $( x , y )$ , called the outflow of vertex x to vertex y, shows that the number of patients with disease x for a hospital visit and then with disease $y$ diagnosed in their subsequent visits. The total outflows of vertex x are equal to the flows coming out from this vertex to other vertices.

To make it easy to understand, we use a simplified network to explain the developed disease network under study. As displayed in Fig. 3(a), there are three vertices, which represent stroke, liver cancer, and diabetes mellitus. The numbers beside directed arcs indicate flows among various vertices. For example, the outflows from stroke to liver cancer are 11, which means that there are 11 patients with stroke in their last visits and liver cancer in their current visits. The total number of outflows of stroke is 2201, which includes flows to other vertices that are not shown in the simplified network. It is worth mentioning that in this study directed arcs in the network are not causal links, i.e., the flows among disease nodes simply stand for the correlations from their temporal perspectives rather than their causal relationships. Fig. 3(b) shows the network of top 20 disease groups under study. Particularly, the thickness of each edge denotes the intensity of an outflow or an inflow. Obviously, it gets more complicated and dificult to read if we draw all the disease groups to build a complete network. Therefore, the figure for the network with all disease groups is omitted here

With the complexity of the temporal relations among diseases, the question now is how to assess disease risks that an individual will have on his/her next hospital visit.

![](/api/attachments/FY6RNHBH/fulltext/images/261b82d094039df0f8facd0b676681c4e69214097619ab8963994c90f035ff3b.jpg)  
Fig. 2. Transforming data to construct a directed disease network.

## 4.4. Disease risk score computing for disease risk predictions

Based on the disease relations developed in the directed network and the medical history of patient i, two scoring approaches are first investigated to calculate the likelihoods of developing diferent diseases by the target patient i. Then an ordered list of diseases, which are sorted by the risk scores, can be predicted for the target patient i.

nodes in the network, which is denoted as Approach 1 or disease temporal link method (DTLM). Based on the diseases in a patient's medical history, we can compute the likelihoods of the next developing diseases of the patient. Considering patient i with M diseases in the medical history, denoted as $H = \{ h _ { 1 } , h _ { 2 } , \cdots , h _ { M } \}$ , the basic idea of Approach 1 is that the risk score of the target patient i developing a disease k is computed according to the relations between disease k and each disease in the patient's medical history, i.e.,

## 4.4.1. Approach 1: disease temporal link method

The first approach directly leverages the temporal relations between

$$
S c o r e _ {k} ^ {(i)} = g (r _ {h _ {m} \to k})\tag{1}
$$

![](/api/attachments/FY6RNHBH/fulltext/images/35c8ed8d3bbf806d860151a90b8098535697560e2c8241280dc75a82425ecd75.jpg)  
(a) A simplified view of three diseases with outflows

![](/api/attachments/FY6RNHBH/fulltext/images/7f8f8b0bd58f59d511031211241ff069421ac9e7fb88aa1869126f57e198b6a0.jpg)  
(b) The network of top 20 diseases in the dataset under study  
Fig. 3. Sub-graph of the directed network in the dataset under study.

![](/api/attachments/FY6RNHBH/fulltext/images/975f34f6deb03b667cb1689db6df09b57965877f5e6e954a4598bac07a7967cf.jpg)  
Fig. 4. illustration of a patient's disease temporal link.

where $h _ { m } \in H , \ r _ { h _ { m } \to k }$ indicates a defined temporal relation between disease $h _ { m }$ and disease $k ,$ and $g ( \cdot )$ represents a function of disease temporal relations.

In Approach 1, we use the flows between a disease in a patient's medical history and other diseases to define the temporal relations between nodes. Fig. 4 shows a directed sub-graph with outflows on vertices and arcs. The total outflows of the vertices $h _ { 1 } , h _ { 2 } , \cdots , h _ { M } \mathsf { a r e } O _ { h _ { 1 } } ,$ $O _ { h _ { 2 } } , \cdots , O _ { h _ { M } }$ respectively, and their outflows to vertex k are $O _ { h _ { 1 }  k } , O _ { h _ { 2 }  k }$ $\cdots , O _ { h _ { M }  k } .$ . The disease temporal link approach is that we compute the risk score of vertex k using the outflow of each node in the set H di recting to vertex k. Accordingly, Eq. (1) can be rewritten as the average risk score of patient i developing disease k on the next hospital visit, which is calculated as follows:

$$
S c o r e _ {k} ^ {(i)} = \frac {1}{M} \sum_ {m = 1} ^ {M} \frac {O _ {h _ {m} \rightarrow k}}{O _ {h _ {m}}}\tag{2}
$$

where $h _ { m } \in H , O _ { h _ { n } }$ denotes the total outflows of vertex $h _ { m } , m = 1 , . . . , M ,$ and $O _ { h _ { m }  k }$ indicates the outflow from disease $h _ { m }$ to disease k

## 4.4.2. Approach 2: aggregated disease temporal links method

Rather than only incorporating the temporal relations between single nodes, we consider the temporal relations between each subset of the target patient's medical history and disease $k ,$ and then derive the risk score of developing disease k by aggregating risk scores from all the subsets. We denoted this approach as Approach 2 or aggregated disease temporal links method (ADTLM).

Like in Approach 1, we consider patient i with M diseases in the medical history, denoted as $H = \{ h _ { 1 } , h _ { 2 } , \cdots , h _ { M } \}$ . In Approach 2, we first figure out all the subsets of the target patient's medical history and then calculate the score for each subset. Finally, we aggregate the scores of these subsets with diferent weights and obtain the risk score of the target patient developing disease k:

$$
S c o r e _ {k} ^ {(i)} = f (w _ {H _ {s u b}} \bullet S u b S c o r e _ {H _ {s u b} \rightarrow k} ^ {(i)})\tag{3}
$$

where $H _ { s u b } \subseteq H , H _ { s u b } \to k$ indicates a defined temporal relation between the subset $H _ { s u b }$ and disease $k , w _ { H _ { s u b } }$ are weights derived according to the sizes of subsets of the target patient's medical history, $S u b S c o r e _ { H _ { s u b }  k } ( i )$ indicates the score derived from each subset and $f ( \cdot )$ represents a function that combines scores from different subsets

A subset is defined as a set of the same disease(s) sufered by the target patient and other patients. The size of a subset indicates the number of diseases that other patients share with the target patient in their medical histories. In this study, we define a similarity metric only based on patients' medical histories, called “medical history similarity”, which is diferent from the similarity based on demographic information that is commonly used in a recommendation system. The metric “medical history similarity” between two patients is quantified as the set size of the shared diseases in these two patients' medical histories. Obviously, the more diseases shared by two patients in the medical histories, the more similar their medical histories are. As mentioned before, the basic idea of Approach 2 is to leverage the temporal relations between subsets of the target patient's medical history and disease k to derive the risk score of the target patient developing disease k. Therefore, the larger the medical history similarity between the target patient and another patient is, the greater the likelihood that the target patient will develop an identical disease with this patient. Correspondingly, we assign diferent weights to subsets with various sizes for Approach 2 according to the medical history similarity.

To assign diferent weights to subsets with diferent sizes, it is necessary to group medical history subsets with the same size into an identical category. Given patient i with the medical history $H = \{ h _ { 1 } , h _ { 2 } , \cdots , h _ { M } \}$ , we get the subsets of the medical history, such as $\{ h _ { 1 } \} _ { : }$ $\{ h _ { 2 } \} , ~ \cdots , ~ \{ h _ { 1 } , h _ { 2 } \} , ~ \{ h _ { 1 } , h _ { 3 } \} , ~ \cdots , ~ \{ h _ { 1 } , h _ { 2 } , h _ { 3 } \} , ~ \{ h _ { 1 } , h _ { 2 } , h _ { 4 } \} , ~ \cdots ,$ $\{ h _ { 1 } , h _ { 2 } , \cdots , h _ { M } \}$ . Then these medical history subsets are classified into multiple categories $J _ { 1 } , J _ { 2 } , \cdots , J _ { M }$ according to their sizes. For example, $J _ { 1 }$ is a category of subsets, which has only one element. By the same token, $J _ { m } , m = 1 , 2 , \cdots , M ,$ is a category of subsets, which has m diseases. Mathematically, we have

$$
J _ {m} = \{A \subseteq H \mid C a r d (A) = m \}\tag{4}
$$

where $m = 1 , 2 , \cdots , M ,$ Card(A) is the number of elements in set A.

In Approach 2, we use the flows between subsets in a patient's medical history and disease k to define temporal relations (Fig. 5). For each subset $s u b _ { j } \in J _ { m } , ~ j = 1 , ~ 2 , ~ \cdots , ~ C a r d ( J _ { m } ) _ $ , we figure out the total outflow, and their outflows directing to vertex k. Thus, the average score of each category is:

$$
S u b S c o r e _ {J _ {m} \rightarrow k} ^ {(i)} = \frac {1}{C a r d (J _ {m})} \sum_ {j = 1} ^ {C a r d (J _ {m})} \psi (s u b _ {j} \rightarrow k)\tag{5}
$$

$$
\psi (s u b _ {j} \to k) = \left\{ \begin{array}{c} \frac {O _ {s u b _ {j} \to k}}{O _ {s u b _ {j}}}, O _ {s u b _ {j}} \neq 0 \\ 0, o t h e r w i s e \end{array} \right.\tag{6}
$$

where $s u b _ { j } \in J _ { m } , \ O _ { s u b _ { j } }$ indicates the total outflow of the subset $s u b _ { j } ,$ $O _ { s u b _ { i }  k }$ denotes the outflow from the subset sub to disease $k ,$ and Card $\left( J _ { m } \right) ^ { \prime }$ is the number of subsets in category $J _ { m } , m = 1 , 2 , \cdots , M .$

As we have classified medical history subsets with an identical number of elements into the same category, medical history subsets in the same category are then assigned with the same weights. In this study, the weights are calculated based on an exponential function of the sizes of subsets. In detail, given m denotes the size of a medical history subset, i.e., the number of the diseases in the medical history that another patient sharing with the target patient $i ,$ then the weight of the category is $e ^ { m }$ . Correspondingly, the normalized weight of each category is

![](/api/attachments/FY6RNHBH/fulltext/images/470a746e50d4c9b5ff82048105eabe9ae8462d88c0dec4352894c942b0737aa8.jpg)  
Fig. 5. illustration of a patient's aggregated disease temporal links.

$$
w _ {J _ {m}} = \frac {e ^ {m}}{\sum_ {m = 1} ^ {M} e ^ {m}}\tag{7}
$$

where $m = 1 , 2 , \cdots , M .$ . Thus, the risk score of patient i with disease k in the next hospital visit is:

$$
\operatorname{Score} _ {k} ^ {(i)} = \sum_ {m = 1} ^ {M} \left(w _ {J _ {m}} \cdot \operatorname{SubScore} _ {J _ {m} \rightarrow k} ^ {(i)}\right)\tag{8}
$$

Based on Eqs. (5), (6), and (7), Eq. (8) can be further defined as:

$$
S c o r e _ {k} ^ {(i)} = \frac {1}{\sum_ {m = 1} ^ {M} e ^ {m}} \cdot \sum_ {m = 1} ^ {M} \left[ \frac {e ^ {m}}{C a r d (J _ {m})} \cdot \sum_ {j = 1} ^ {C a r d (J _ {m})} \psi (s u b _ {j} \rightarrow k) \right]\tag{8-1}
$$

$$
\psi (s u b _ {j} \to k) = \left\{ \begin{array}{c l} \frac {O _ {s u b _ {j} \to k}}{O _ {s u b _ {j}}}, & O _ {s u b _ {j}} \neq 0 \\ 0, & o t h e r w i s e \end{array} \right.\tag{8-2}
$$

In summary, in Approach 1 (DTLM) we simply use the links among single nodes to derive risk scores. By contrast, in Approach 2 (ADTLM) we consider a more complex way based on the relationship of disease sets and disease nodes to calculate risk scores, which fully leverages the temporal disease relation information of other similar patients to assess disease risks for the target patient.

## 4.4.3. Predicted diseases list generation

Through the above-discussed risk score computing schemes, we can generate a set of disease scores for patient $i , \quad \mathrm { i . e . , }$ $\{ S c o r e _ { 1 } ^ { ( i ) } , S c o r e _ { 2 } ^ { ( i ) } , \cdots , S c o r e _ { K } ^ { ( i ) } \}$ . Let ${ \langle S c o r e _ { ( 1 ) } } ^ { ( i ) } , S c o r e _ { ( 2 ) } ^ { ( i ) } , \cdots , S c o r e _ { ( K ) } ^ { ( i ) } \rangle$ denote the sequence of the scores ${ S c o r e _ { k } } ^ { ( i ) } , k = 1 , 2 , \cdots , K ,$ , then we can obtain a corresponding sequence of diseases, denoted as $\varphi ^ { ( i ) } = \langle { \varphi _ { 1 } } ^ { ( i ) } , { \varphi _ { 2 } } ^ { ( i ) } , \cdots , { \varphi _ { K } } ^ { ( i ) } \rangle .$ . As mentioned in the problem statement, we provide a predicted list with a fixed length of Q. In other words, only top Q diseases in the sequence $\varphi ^ { ( i ) } = \langle \bar { \varphi _ { 1 } } ^ { ( i ) } , \varphi _ { 2 } ^ { ( i ) } , \cdots , \varphi _ { K } ^ { ( i ) } \rangle$ of patient i will be finally recommended to healthcare professionals.

## 4.5. Evaluation metrics

The result of our prediction model is an ordered list of disease risks for a patient. It needs an assessment method to evaluate the accuracy of each recommended list with respect to the corresponding true values in the dataset. We adopt an accuracy evaluation approach based on the half-life accuracy evaluation [48]. The basic idea of the half-life accu racy method is to assign diferent weights to various positions on the recommended list.

A set of diseases that patient i will have when visiting the hospital next time, is called a true value set of patient i, denoted as $\boldsymbol { \theta } ^ { ( i ) } = \{ \theta _ { 1 } ^ { ( i ) } , \theta _ { 2 } ^ { ( i ) } , \cdots , \theta _ { G } ^ { ( i ) } \}$ . The whole predicted list can be denoted as $\varphi ^ { ( i ) } = \langle \varphi _ { 1 } ^ { ( i ) } , \varphi _ { 2 } ^ { ( i ) } , \cdots , \varphi _ { K } ^ { ( i ) } \rangle$ , while as mentioned earlier only top Q dis eases on the list will be recommended. The value of a position on the recommended list for patient i is obtained as follows:

$$
L i s t _ {k} ^ {(i)} = \left\{ \begin{array}{c c} 1 & \text {if} \varphi_ {k} ^ {(i)} \in \theta^ {(i)} \\ 0 & \text {otherwise} \end{array} \right.,\tag{9}
$$

where $k = 1 , 2 , \cdots , Q .$ . In other words, $\boldsymbol { L i s t _ { k } } ^ { ( i ) }$ is 1 if patient i indeed sufers the disease recommended by the model on the next hospital visit and 0 if otherwise. Note that the half-life accuracy score for a recommendation list is $\begin{array} { r } { \sum _ { k = 1 } ^ { Q } 2 ^ { - k / c } \bullet L i s t _ { k } ^ { ( i ) } } \end{array}$ , where k represents the position on the recommended list, $2 ^ { - k / c }$ represents the weight of the $k ^ { t h }$ positions on the recommended list, and c is a constant that can be adjusted as needed. Without normalization for weight $2 ^ { - k / c }$ , the half-life accuracy score is not equal to 1 even when the first G diseases on the recommended list are identical to the true values. Hence, we introduce normalization for the half-life accuracy score, $\mathrm { i . e . , }$ the adapted normalized weight function becomes $\begin{array} { r } { 2 ^ { - k / c } / \sum _ { g = 1 } ^ { G } 2 ^ { - g / c } . } \end{array}$ Hence, the mean accuracy score of all the samples in a test dataset is:

$$
M e a n A c c u r a c y = \frac {1}{N} \sum_ {i = 1} ^ {N} \sum_ {k = 1} ^ {Q} \frac {2 ^ {- k / c}}{\sum_ {g = 1} ^ {G} 2 ^ {- g / c}} \cdot L i s t _ {k} ^ {(i)}\tag{10}
$$

where $\boldsymbol { L i s t _ { k } } ^ { ( i ) }$ represents the value of the $k ^ { t h }$ position on the recommended list, G is the number of diseases that patient i actually have on the subsequent hospital visit, Q is the number of diseases recommended, N is the size of the samples in a test dataset. If all the G diseases in the test dataset appear exactly in the top G positions on a recommended list, then the accuracy score is equal to 1 for this recommended list, i.e., $\begin{array} { r } { \sum _ { k = 1 } ^ { Q } \frac { 2 ^ { - k / c } } { \sum _ { g = 1 } ^ { G } 2 ^ { - g / c } } \bullet L i s t _ { k } ^ { ( i ) } = 1 , i = 1 , 2 , 3 , \cdots , N . } \end{array}$ . The ratio of recommended lists with accuracy score equal to 1 is denoted as $R a t i o _ { 1 S c o r e } .$ . In addition, precision and recall can also be used to evaluate the performance of the proposed methods [49].

## 5. Validation of the proposed approaches using hospital datasets

This section first shows the analytical results of the proposed approaches when they are applied to two independent real-world datasets. Then we compare the performance of our proposed methods with several baseline methods. The impact of patients' demographic characteristics on the performance of the proposed method has also been investigated.

## 5.1. Data preprocessing and training-test schemes

## 5.1.1. Description of datasets and data preprocessing

Datasets for validation were collected from two general hospitals respectively in Beijing and Shenzhen, China, which are denoted as dataset A and dataset B. Dataset A includes 52.312 inpatients from January 01st 2015 to December 31st 2015, and dataset B includes 32,260 inpatients from January 01st 2016 to November 5th 2016. Information collected regarding each hospital visit includes patient identification, the sequence number of a hospital visit, age, gender, and diagnoses. Noted that dataset A does not include patients' demographic information such as age and gender while dataset B includes patients basic demographic information.

As our goal is to predict a list of diseases that a patient might have on the next hospital visit, a patient who has only one hospital visit is removed from the datasets. Note that diagnoses in the raw datasets are clearly described using ICD-10 codes. Based on the ICD-10 codes, we mapped the diagnoses in the datasets to the DALY disease groups $D _ { 1 : }$ $D _ { 2 } , \cdots , D _ { 1 2 5 }$ derived in Section 4.1. The processed datasets ready for model validation are summarized in Table 3.

There are 84 and 82 disease groups in the processed dataset A′ and dataset B′, respectively. Datasets A′ and B′ have 78 DALY disease groups in common, while their union set covers 88 DALY groups. It is worth mentioning that many disease groups were removed from the datasets as they are acute (i.e., resulting in no second visit) or never included in

Summary of the processed datasets for validation.

<table><tr><td>Dataset</td><td>Number of inpatients</td><td>Number of hospital visits</td><td>Number of hospital visits per patient (mean ± SD, range)</td><td>Number of diagnoses per visit (mean ± SD, range)</td><td>Number of DALY groups covered</td></tr><tr><td>Dataset A&#x27;</td><td>7989</td><td>24,466</td><td>3.06 ± 1.67, 2–22</td><td>4.87 ± 2.48, 1–21</td><td>84</td></tr><tr><td>Dataset B&#x27;</td><td>4131</td><td>13,063</td><td>3.16 ± 1.98, 2–17</td><td>4.99 ± 2.83, 1–11</td><td>82</td></tr></table>

![](/api/attachments/FY6RNHBH/fulltext/images/826f14288746ef851818864a71f276bd94c41ddd5883d20270473d333725126b.jpg)

(a) training-test scheme 1  
![](/api/attachments/FY6RNHBH/fulltext/images/54d070cffb51e31c43e54698231718adcb58887b1c9e828fbd1f80857d11c5bc.jpg)  
(b) training-test scheme 2

![](/api/attachments/FY6RNHBH/fulltext/images/b99650c880b3e7228deb6054252e20a4044939b33fb97731b97e9479e1cca081.jpg)  
(c) training-test scheme 3  
Fig. 6. Training-test schemes for datasets in the validation process.

the datasets in the first place.

## 5.1.2. Training-test schemes used in validation

To compare the overall accuracy of two diferent proposed methods, 10-fold cross-validation (CV) is applied to datasets A′ and B′. As shown in Fig. $^ { 6 , }$ three diferent training-test schemes based on the 10-fold CV could be used in our model validation process.

The first training-test scheme (Fig. 6(a)) is to conduct the 10-fold CV on each dataset respectively. The second training-test scheme (Fig. 6(b)) is to combine dataset A′ and dataset B′ first and then perform the 10-fold CV on the combined dataset. The third one (Fig. 6(c)) is that dataset A′ is used as the training set and dataset B′ is used as the testing set, or vice versa. Based on the information about datasets in Table 3, the DALY disease groups covered by those two hospitals are diferent. Therefore, the third training-test scheme is not appropriate in this study.

## 5.2. Validation results of the proposed methods

In this study, we set Q = 10. Table 4 shows some examples of the lists predicted using ADTLM. In Table 4, the first column represents patients' identification. The second column shows true value set, which is the corresponding disease groups of the true diagnoses for a patient on the next visit. For each true value $s \mathrm { e t , }$ elements are in no particular order. The third column of Table 4 provides ordered predicted lists. In other words, the predicted diseases are sorted using the descending order of risk scores. Obviously, if the position of a disease in a true value set is much closer to the top of the corresponding recommenda tion list, the better result it obtains in the prediction (i.e., reflecting a more accurate disease risk assessment on the list).

Table 4  
Examples of the true value sets and the lists predicted using ADTLM

<table><tr><td>Patients</td><td>True value set</td><td colspan="10">Recommended list</td></tr><tr><td>P1</td><td> $\{G_{10}\}$ </td><td> $\mathbf{G}_{10}$ </td><td> $G_{14}$ </td><td> $G_{16}$ </td><td> $G_9$ </td><td> $G_{24}$ </td><td> $G_2$ </td><td> $G_{40}$ </td><td> $G_{13}$ </td><td> $G_{34}$ </td><td> $G_{48}$ </td></tr><tr><td>P2</td><td> $\{G_{16}, G_{49}\}$ </td><td> $\mathbf{G}_{49}$ </td><td> $\mathbf{G}_{16}$ </td><td> $G_9$ </td><td> $G_2$ </td><td> $G_{24}$ </td><td> $G_{22}$ </td><td> $G_{48}$ </td><td> $G_{40}$ </td><td> $G_{11}$ </td><td> $G_{13}$ </td></tr><tr><td>P3</td><td> $\{G_4, G_{14}, G_{34}, G_{40}, G_{60}\}$ </td><td> $G_{24}$ </td><td> $\mathbf{G}_{40}$ </td><td> $\mathbf{G}_{34}$ </td><td> $\mathbf{G}_4$ </td><td> $\mathbf{G}_{60}$ </td><td> $G_{84}$ </td><td> $\mathbf{G}_{14}$ </td><td> $G_9$ </td><td> $G_{73}$ </td><td> $G_{46}$ </td></tr><tr><td>P4</td><td> $\{G_9, G_{16}, G_{49}\}$ </td><td> $\mathbf{G}_{49}$ </td><td> $\mathbf{G}_{16}$ </td><td> $\mathbf{G}_9$ </td><td> $G_2$ </td><td> $G_{24}$ </td><td> $G_{48}$ </td><td> $G_{46}$ </td><td> $G_{11}$ </td><td> $G_{40}$ </td><td> $G_{22}$ </td></tr><tr><td>P5</td><td> $\{G_4, G_{16}, G_{34}\}$ </td><td> $\mathbf{G}_4$ </td><td> $\mathbf{G}_{16}$ </td><td> $G_{14}$ </td><td> $G_9$ </td><td> $\mathbf{G}_{34}$ </td><td> $G_2$ </td><td> $G_{40}$ </td><td> $G_{13}$ </td><td> $G_{24}$ </td><td> $G_{11}$ </td></tr></table>

Using training-test Scheme 1 and 2, we have obtained accuracy scores of the recommended lists in all the training-test runs. Table 5 shows the ratio of recommended lists with 1 score and the means of accuracy scores of all the recommended lists.

As shown in Table 5, if scheme 1 is used, $R a t i o _ { 1 S c o r e }$ gets improved by approximately 6.97% and 15.50% for dataset A′ and dataset B′ respectively when ADTLM is compared with DTLM. The mean accuracy score using ADTLM is higher than using DTLM by 1.56% with dataset A′ and 5.13% with dataset B′. If scheme 2 is applied, $R a t i o _ { 1 S c o r e }$ using ADTLM is also higher than using DTLM by about 10.49%, while the mean accuracy score using ADTLM is higher than using DTLM by 3.02%. In summary, ADTLM performs better than DTLM or disease temporal link approach. The results reveal that a prediction model leveraging more patient information will perform better. Therefore, we recommend ADTLM for application in the real world.

Table 5  
Performances of the proposed approaches with two training-test schemes.

<table><tr><td>Training-test schemes</td><td>datasets</td><td>methods</td><td> $Ratio_{1Score}$ (mean ± SD)</td><td>MeanAccuracy(mean ± SD)</td></tr><tr><td rowspan="4">Scheme 1</td><td rowspan="2">Dataset A&#x27;</td><td>DTLM</td><td>0.6442 ± 0.0086</td><td>0.8831 ± 0.0061</td></tr><tr><td>ADTLM</td><td>0.7139 ± 0.0095</td><td>0.8987 ± 0.0034</td></tr><tr><td rowspan="2">Dataset B&#x27;</td><td>DTLM</td><td>0.3812 ± 0.0176</td><td>0.8083 ± 0.0096</td></tr><tr><td>ADTLM</td><td>0.5362 ± 0.0166</td><td>0.8596 ± 0.0093</td></tr><tr><td rowspan="2">Scheme 2</td><td rowspan="2">Dataset A&#x27; + Dataset B&#x27;</td><td>DTLM</td><td>0.5511 ± 0.0093</td><td>0.8575 ± 0.0046</td></tr><tr><td>ADTLM</td><td>0.6560 ± 0.0088</td><td>0.8877 ± 0.0047</td></tr></table>

## 5.3. Performance compared with other methods

## 5.3.1. Baselines

We compare the proposed method with three types of baseline methods, recommendation algorithms, multi-label classifiers and sequential pattern mining (SPM). Regarding recommendation algorithms, collaborative filtering (CF) is used as a baseline in this study, which had been applied to multiple disease predictive modeling [10] and is the classic benchmark method in the field of multi-disease risk prediction study [27,28]. Since the multi-disease risk prediction problem under study is diferent from a traditional recommendation problem, it is necessary to briefly introduce how collaborative filtering is used in the multi-disease risk prediction problem.

If a patient has disease k, then the patient has a score of 1 for disease k; if the patient does not have disease $k ,$ then the patient has a score of 0 for disease k. The similarity between patients is calculated based on the cosine distance. Thus, the similarity between a target patient i and any other patient a is calculated as follows:

$$
S i m _ {i, a} = \frac {\overrightarrow {r _ {i}} \cdot \overrightarrow {r _ {a}}}{\| \overrightarrow {r _ {i}} \| * \| \overrightarrow {r _ {a}} \|} = \frac {\sum_ {k} r _ {i , k} r _ {a , k}}{\sqrt {\sum_ {k} r _ {i , k} ^ {2}} \sqrt {\sum_ {k} r _ {a , k} ^ {2}}}\tag{11}
$$

In Eq. (11), $\overrightarrow { r _ { i } }$ represents the score vector of patient i for all diseases, $r _ { i , \ k }$ denotes the kth component of $\overrightarrow { r _ { i } }$ . And the dimension size of $\overrightarrow { r _ { i } }$ indicates the number of diseases in the recommendation system. The meaning of $\overrightarrow { r _ { a } }$ and $r _ { a , \ k }$ is the same as $\overrightarrow { r _ { i } }$ and $r _ { i , \ast }$ .

The risk score of the target patient i sufering disease k in the future, i.e., Score $\boldsymbol { \mathbf { \rho } } _ { k } ^ { ( i ) }$ , is calculated based on two parts [10]. One is the average prevalence of disease $k ,$ and the other is derived from medical histories of other patients who is similar to the target patient i.

$$
S c o r e _ {k} ^ {(i)} = \bar {r} _ {k} + \rho (1 - \bar {r} _ {k}) \sum_ {a \in S e t _ {k}} S i m _ {i, a}\tag{12}
$$

In Eq. (12), r represents the average prevalence of disease k in the training dataset, $S e t _ { k }$ represents the set of patients with disease k in the training dataset, ρ is the normalization coeficient, $\begin{array} { r } { \rho = 1 / \sum _ { a \in S e t _ { t r a i n } } S i m _ { i , a } , } \end{array}$ and $S e t _ { t r a i n }$ represents the set of all the patients in the training dataset. According to the recommendation list genera tion described in Section 4.5, the risk scores of diseases for the target patient i are sorted, then a list of ordered diseases is obtained. Finally, the first Q diseases are recommended to patient i.

From the perspective of classification, the problem in this study is a multi-label classification problem. Therefore, two classical multi-label classifiers are used to compare, i.e., K-nearest neighbor (KNN) [50] and decision tree (DT) [51]. Since the output of a classifier is a list of probabilities of developed diseases, we first sort these probabilities using a descending order and then generate an ordered recommendation list. Finally, the first Q diseases are recommended to patient i.

## 5.3.2. Performance compared with baseline

The performance comparisons between the proposed method and the baseline methods are shown in Tables 6-8. Note that all the results are obtained from 10-fold CV experiments.

Table 6 shows the 10-fold CV results derived from dataset A'. The proposed method ADTLM performs better than collaborative filtering by about 7.0%, 20.0%, 1.1%, 2.2% and 1.7% with respect to the metrics, MeanAccuracy, $R a t i o _ { 1 S c o r e } ,$ Precision, Recall, and F1 Score, respec tively. Compared to K-nearest neighbor, ADTLM has about 1.0%, 3.0%, 1.3%, 4.8%, and 2.0% improvement with respect to those metrics, respectively. ADTLM also performs better than decision tree by about

1.5%, 1.3%, 1.2%, 3.0%, and 1.8% with respect to those metrics, respectively. Compared to sequential pattern mining, ADTLM has about 4.4%, 32.5%, 4.0%, 11.0%, and 6.2% improvement with respect to those metrics, respectively.

Table 7 provides the 10-fold CV results derived from dataset B′. The proposed method ADTLM performs better than collaborative filtering by about 7.5%, 25.3%, 3.5%, 8.2%, and 5.0% with respect to the metrics MeanAccuracy, $R a t i o _ { 1 S c o r e } ,$ Precision, Recall, and F1 Score, respectively. Compared to KNN, ADTLM has about 0.1%, 2.1%, 1.2%, 4.3%, and 1.9% improvement with respect to those metrics, respectively. ADTLM also performs better than decision tree by about 2.6%, 2.3%, 2.2%, 5.1%, and 3.1% with respect to those metrics, respectively. Compared to sequential pattern mining, ADTLM has about 2.6%, 31.6%, 6.0%, 14.5%, and 8.6% improvement with respect to those metrics, respectively.

Table 8 has the results derived from the combined dataset. The proposed method ADTLM performs better than collaborative filtering by about 6.7%, 21.8%, 2.2%, 5.3%, and 3.3% with respect to the me trics MeanAccuracy, Ratio , Precision, Recall, and F1 Score, respectively. Compared to K-nearest neighbor, ADTLM has about 1.0%, 3.5%, 1.4%, 4.9%, and 2.2% improvement with respect to those metrics, respectively. Again, ADTLM performs better than decision tree by about 1.7%, 1.6%, 1.4%, 3.4%, and 2.1% with respect to those metrics. Compared to sequential pattern mining, ADTLM has about 4.3%, 31.4%, 5.2%, 13.1%, and 7.9% improvement with respect to those metrics, respectively.

In summary, ADTLM performs better than the compared baseline methods, including collaborative filtering, K-nearest neighbor, decision tree, and sequential pattern mining in this study.

## 5.4. The impact of patients' demographic characteristics

To further explore the impact of patients' demographic characteristics on the prediction performance of the proposed methodology, patients are classified into subgroups based on age and gender. Note that dataset B′ contains the demographic information of patients. Fig. 7 shows the distribution of patients by age and gender in dataset B′.

## 5.4.1. Grouping by gender

Table 9 gives the data summary of dataset B′ grouped by gender. We perform the proposed ADTLM on these two patient subgroups using the 10-fold CV, the results are shown in Table 10.

As shown in the 2nd and 3rd column in Table 10, the performance on the female subgroup is superior to that on the male subgroup by 1.5%, 9.1%, and 1.3% in terms of MeanAccuracy, Ratio $1 S c o r e$ and Recall, while the male group shows a better performance on Precision and F1 Score.

To investigate if it afects the overall predictive performance on a dataset clustered by gender, the last two columns in Table 10 provide the weighted average performance of subgroups and the 10-fold CV performance without grouping. The diferences are 0.0042, 0.0053, 0.0008, 0.0032, and 0.0019 for the used metrics and the diferences are within the standard deviations, which shows that clustering by gender has no substantial impact on the overall predictive performance on dataset B′.

## 5.4.2. Grouping by age

According to the age grouping standard of WHO (0–45, $4 5 { - } 4 9 { , } 7 5 { - } 8 9 , \geq 9 0 )$ ) and the age structure of population (0–14, 15–64, ≥ 65) provided by China statistical yearbook, we divide dataset B′ into four groups: 0–14, 15–44, 45–64, ≥ 65 by considering the age distribution in dataset B′. Table 11 gives the data summary of dataset B′ grouped by age.

As there is a small number of patients in the subgroup where patients were less than 14 years old (Table 11), this age group is thus excluded from the following comparison. There are 69, 71, and 72

Table 6  
Comparison with the baseline methods: Dataset A′ (training-test scheme 1).

<table><tr><td>Metrics (mean ± SD)</td><td>CF</td><td>KNN</td><td>DT</td><td>SPM</td><td>ADTLM</td></tr><tr><td>MeanAccuracy</td><td>0.8292 ± 0.0030</td><td>0.8889 ± 0.0052</td><td>0.8833 ± 0.0041</td><td>0.8546 ± 0.0048</td><td>0.8987 ± 0.0034</td></tr><tr><td> $Ratio_{1Score}$ </td><td>0.5138 ± 0.0110</td><td>0.6837 ± 0.0136</td><td>0.7013 ± 0.0093</td><td>0.3890 ± 0.0127</td><td>0.7139 ± 0.0095</td></tr><tr><td>Precision</td><td>0.1943 ± 0.0028</td><td>0.1930 ± 0.0035</td><td>0.1942 ± 0.0036</td><td>0.1654 ± 0.0032</td><td>0.2057 ± 0.0035</td></tr><tr><td>Recall</td><td>0.9238 ± 0.0048</td><td>0.8972 ± 0.0068</td><td>0.9153 ± 0.0029</td><td>0.8359 ± 0.0054</td><td>0.9456 ± 0.0038</td></tr><tr><td>F1 Score</td><td>0.3211 ± 0.0038</td><td>0.3177 ± 0.0048</td><td>0.3204 ± 0.0048</td><td>0.2762 ± 0.0049</td><td>0.3379 ± 0.0046</td></tr></table>

DALY disease groups covered by the last three age subgroups of $^ { \omega } 1 5 { - } 4 4 ^ { \prime \prime } , ^ { \omega } 4 5 { - } 6 4 ^ { \prime \prime } \mathrm { a n d ~ } ^ { \omega } \geq 6 5 ^ { \prime \prime }$ , respectively. It is worth mentioning that in total there are 80 disease groups covered by the last three age subgroups, while there are only 59 common disease groups across these three age subgroups. This finding clearly indicates that patients within diferent age groups sufer diferent diseases.

The proposed ADTLM was performed on the last three age sub groups using the 10-fold CV. As shown in the 2nd, 3rd, and 4th column in Table 12, the performance on the subgroup $^ { \ d } { } ^ { \dag } 1 5 \mathrm { - } 4 4 ^ { \dag }$ is superior to the performance on other two subgroups in terms of MeanAccuracy, Ra-$t i o _ { 1 S c o r e }$ and Recall, respectively, while the subgroup $^ { \infty } \geq 6 5 ^ { \gamma }$ shows a better performance on Precision and F1 Score.

To investigate if it afects the overall predictive performance on a dataset clustered by age, the last two columns in Table 12 show the weighted average performance of age subgroups and the 10-fold CV performance without grouping. The diferences are 0.0048, 0.0073, 0.0013, 0.0036, and 0.0043 for the used metrics and the diferences are again within the standard deviations, which means that clustering by age has no substantial impact on the overall predictive performance on dataset B′.

In summary, there indeed exists a small diferent prediction per formance on subgroups when clustering by gender or age. However, whether patients are grouped by gender/age or not has little impact on the overall predictive performance, which shows the robustness of the proposed method.

## 6. Discussions

In this section, we first discuss how the proposed framework can be appropriately employed in facilitating the decision-making process in a hospital setting. Then we summarize the contributions and highlight the limitations of our study.

## 6.1. Promising application in the real world

Accurate disease risk assessments can be used as a reference by medical professionals to provide patients efective healthcare guidance at the point of need. For example, the proposed ADTLM can be developed as a module embedded in a hospital information system. Once it becomes part of a decision-making support tool for medical professionals, better health intervention plans than ever before can be developed for patients to improve the medical outcomes in the long run. Fig. 8 shows such a potential application scenario.

As illustrated in detail in Fig. 8, a decision support system for multiple disease risk assessment can be developed, which consists of software modules and a database storing data derived from ICD dictionary, DALY estimates, and EHRs data. The included software modules realize the functions required by the proposed approach. When a patient is ready for discharge, the system can recommend a list of diseases ordered by risk scores based on the patient's medical history. In addition to using personal clinical experience and medical knowledge, a medical professional can reference the recommended list to adjust and confirm his/her judgement and make a health intervention regimen for the patient. The length of a recommended list can be adiusted as needed. Medical professionals could also provide their feedback on disease risk rankings, which can be used by the system to further en hance the risk score computing module over time. Promisingly, the system can help avoid certain prejudices in decision-making. It is well recognized that medical professionals' personal clinical experience and medical knowledge can vary from one to another. As the above-mentioned system learns from massive electronic health records, therefore, it generates recommendation results in a consistent and unbiased manner for a patient.

In fact, the proposed framework can be implemented in a broader manner as patients' diagnoses today are most likely encoded as ICD codes or the like. Because the approach is robust for various data sources or code schemes, the predictive results from the applications of the approach can be well used to help health policy decision-makers understand the health risks of communities so as to help them develop optimal plans for resources and fiscal allocations.

## 6.2. Contributions and limitations

Although directed disease networks have been exploited in this field, there is still a gap to fill. For example, the studies by Jensen et al. [6] and Kannan et al. [7] focused on using directed disease networks either to derive disease trajectories or to determine the directionality of disease trajectories for a targeted population rather than assessing disease risks for an individual patient. The developed multiple disease prediction approach in this study filled the gap by focusing on systematically assessing future disease risks for a patient.

The most important contribution of our study lies in combining directed disease network and recommendation system techniques to facilitate multiple disease prediction modeling. By doing so, we can fully incorporate massive temporal disease relations in EHRs. As a result, we can improve the performance of developed models substantially when compared to the existing approaches in the current literature. Particularly, compared with baseline methods in our evaluations, ADTLM has realized significantly higher Recall and $R a t i o _ { 1 s c o r e } ,$ which are critical when predicting multiple disease risks for inpatients. Finally, the results from our conducted validations and early discussion show that the proposed methodology is robust and can be easily adopted in the real world.

Table 7  
Comparison with baseline methods: Dataset B′ (training-test scheme 1)

<table><tr><td>Metrics (mean ± SD)</td><td>CF</td><td>KNN</td><td>DT</td><td>SPM</td><td>ADTLM</td></tr><tr><td>MeanAccuracy</td><td>0.7844 ± 0.0083</td><td>0.8584 ± 0.0073</td><td>0.8339 ± 0.0094</td><td>0.8340 ± 0.0086</td><td>0.8596 ± 0.0093</td></tr><tr><td> $Ratio_{1Score}$ </td><td>0.2830 ± 0.0104</td><td>0.5149 ± 0.0163</td><td>0.5133 ± 0.0184</td><td>0.2202 ± 0.0110</td><td>0.5362 ± 0.0166</td></tr><tr><td>Precision</td><td>0.2472 ± 0.0035</td><td>0.2700 ± 0.0037</td><td>0.2602 ± 0.0034</td><td>0.2226 ± 0.0043</td><td>0.2822 ± 0.0068</td></tr><tr><td>Recall</td><td>0.8390 ± 0.0082</td><td>0.8781 ± 0.0051</td><td>0.8705 ± 0.0064</td><td>0.7758 ± 0.0090</td><td>0.9211 ± 0.0097</td></tr><tr><td>F1 Score</td><td>0.3819 ± 0.0042</td><td>0.4129 ± 0.0046</td><td>0.4007 ± 0.0043</td><td>0.3459 ± 0.0058</td><td>0.4320 ± 0.0077</td></tr></table>

Table 8  
Comparison with baseline methods: Dataset $A ^ { \prime } +$ Dataset B′ (training-test scheme 2).

<table><tr><td>Metrics (mean ± SD)</td><td>CF</td><td>KNN</td><td>DT</td><td>SPM</td><td>ADTLM</td></tr><tr><td>MeanAccuracy</td><td>0.8206 ± 0.0049</td><td>0.8779 ± 0.0065</td><td>0.8707 ± 0.0060</td><td>0.8447 ± 0.0051</td><td>0.8877 ± 0.0047</td></tr><tr><td> $Ratio_{1Score}$ </td><td>0.4379 ± 0.0088</td><td>0.6214 ± 0.0153</td><td>0.6398 ± 0.0108</td><td>0.3425 ± 0.0094</td><td>0.6560 ± 0.0088</td></tr><tr><td>Precision</td><td>0.2104 ± 0.0014</td><td>0.2188 ± 0.0039</td><td>0.2184 ± 0.0037</td><td>0.1806 ± 0.0012</td><td>0.2327 ± 0.0027</td></tr><tr><td>Recall</td><td>0.8840 ± 0.0049</td><td>0.8878 ± 0.0058</td><td>0.9028 ± 0.0046</td><td>0.8064 ± 0.0050</td><td>0.9371 ± 0.0027</td></tr><tr><td>F1 Score</td><td>0.3399 ± 0.0018</td><td>0.3511 ± 0.0053</td><td>0.3517 ± 0.0049</td><td>0.2942 ± 0.0023</td><td>0.3728 ± 0.0034</td></tr></table>

![](/api/attachments/FY6RNHBH/fulltext/images/ba156dd08f671cc1f9707a988a84e84b9cf4f384cc3f1462d5cfc5bff6edb7be.jpg)  
(a) Distribution of patients by age

![](/api/attachments/FY6RNHBH/fulltext/images/4fc293590400eafdff336a222cab591baf60230cd12da58d120599bf34bb5fa0.jpg)  
(b) Distribution of patients by gender  
Fig. 7. The distribution of patients by age and gender in dataset $\mathbf { B } ^ { ' . }$

Table 9  
Summary of dataset B′ grouped by gender

<table><tr><td></td><td>Dataset B&#x27;</td><td>Male</td><td>Female</td></tr><tr><td>The number of individuals</td><td>4131</td><td>1842</td><td>2289</td></tr><tr><td>Age (mean ± SD)</td><td>56.81 ± 17.66</td><td>60.31 ± 16.91</td><td>53.99 ± 17.74</td></tr><tr><td>Average number of visits per patient (mean ± SD)</td><td>3.16 ± 1.98</td><td>3.11 ± 1.90</td><td>3.19 ± 2.04</td></tr><tr><td>DALY disease groups covered</td><td>82</td><td>73</td><td>77</td></tr></table>

Moreover, our proposed methodology improves the interpretability of the results derived from multiple disease prediction modeling. The risk score computed in our method is based on the ratios of flows among diseases, i.e., the proportion of patients diagnosed with the same disease(s), which is more explainable from the medical perspective than classifiers or similarity calculation based on the cosine distance in collaborative filtering. With two diferent methods proposed, i.e., DTLM and ADTLM, we prove that the more disease relationship information a model can capture, the more accurate in terms of performance it can realize.

One limitation of our study is that the numbers of diseases in our datasets were limited, which didn't include all the diseases described in the ICD dictionary. Another limitation is that the similarity calculation in our medical recommendation system is only based on patients' medical histories while not including their ethnicity, medication, social behaviors, etc., due to limited information in our datasets. It will be interesting to further incorporate these factors into risk score computing to understand those factors' impact on the outcomes.

While the sequence information of hospital visits is considered in our model, the time intervals between consecutive visits have not been investigated as the information is missing in our datasets for most patients. Apparently, the proposed model can be flexibly extended if richer information becomes available. It will be also interesting to explore how big data and deep learning techniques can be fully leveraged in the proposed framework to further improve the overall performance.

## 7. Conclusion

In this study, we proposed a novel framework that integrates directed disease networks with recommendation system techniques for multiple disease risk prediction modeling. By taking into consideration patients' disease sequence information between successive hospital visits, the proposed directed disease networks successfully incorporated temporal relations among diseases into the proposed disease risk prediction models, which makes the proposed models easy to adapt over time. We investigated two disease risk score computing approaches, i.e., disease temporal link approach and aggregated disease temporal links approach, to generate an ordered list of diseases risks for a patient. The proposed approaches were validated using two independent realworld datasets. The results show that the proposed aggregated disease temporal links approach or ADTLM outperforms baseline methods, such as collaborative filtering, K-nearest neighbors, decision tree, and sequential pattern mining. Additionally, we investigated the impact of patients' demographic characteristics on the performance of the proposed methodology by clustering patients into subgroups based on age or gender. The results indicate that the clustering has little impact on the overall predictive performance, which shows the robustness of the proposed methodology.

Table 10  
Prediction performance of dataset B′ grouped by gender

<table><tr><td>Metrics (mean ± SD)</td><td>Male subgroup</td><td>Female subgroup</td><td>Weighted average of subgroups</td><td>Performance without grouping</td></tr><tr><td>MeanAccuracy</td><td>0.8469 ± 0.0113</td><td>0.8622 ± 0.0103</td><td>0.8554</td><td>0.8596 ± 0.0093</td></tr><tr><td> $Ratio_{1Score}$ </td><td>0.4806 ± 0.0147</td><td>0.5713 ± 0.0179</td><td>0.5309</td><td>0.5362 ± 0.0166</td></tr><tr><td>Precision</td><td>0.3063 ± 0.0142</td><td>0.2614 ± 0.0082</td><td>0.2814</td><td>0.2822 ± 0.0068</td></tr><tr><td>Recall</td><td>0.9107 ± 0.0054</td><td>0.9237 ± 0.0066</td><td>0.9179</td><td>0.9211 ± 0.0097</td></tr><tr><td>F1 Score</td><td>0.4582 ± 0.0156</td><td>0.4074 ± 0.0098</td><td>0.4301</td><td>0.4320 ± 0.0077</td></tr></table>

Table 11  
Data summary of dataset B′ grouped by age

<table><tr><td></td><td>≤14</td><td>15–44</td><td>45–64</td><td>≥ 65</td></tr><tr><td>The number of individuals</td><td>48</td><td>938</td><td>1673</td><td>1472</td></tr><tr><td>Male:female</td><td>35:13</td><td>235:703</td><td>796:877</td><td>776:696</td></tr><tr><td>Age (mean ± SD)</td><td>4.54 ± 4.70</td><td>33.20 ± 6.21</td><td>55.81 ± 5.61</td><td>74.68 ± 6.99</td></tr><tr><td>Average number of visits per patient (mean ± SD)</td><td>2.33 ± 1.39</td><td>2.79 ± 1.64</td><td>3.48 ± 2.16</td><td>3.04 ± 1.92</td></tr><tr><td>DALY disease groups covered</td><td>23</td><td>69</td><td>71</td><td>72</td></tr></table>

Table 12  
Prediction performance of dataset B′ grouped by age.

<table><tr><td>Metrics (mean ± SD)</td><td>15–44</td><td>45–64</td><td>≥65</td><td>Weighted average of subgroups</td><td>Performance without grouping</td></tr><tr><td>MeanAccuracy</td><td>0.8809 ± 0.0224</td><td>0.8687 ± 0.0174</td><td>0.8225 ± 0.0157</td><td>0.8548</td><td>0.8596 ± 0.0093</td></tr><tr><td> $Ratio_{1Score}$ </td><td>0.6933 ± 0.0490</td><td>0.5806 ± 0.0269</td><td>0.3745 ± 0.0214</td><td>0.5289</td><td>0.5362 ± 0.0166</td></tr><tr><td>Precision</td><td>0.1856 ± 0.0103</td><td>0.2648 ± 0.0042</td><td>0.3612 ± 0.0094</td><td>0.2835</td><td>0.2822 ± 0.0068</td></tr><tr><td>Recall</td><td>0.9430 ± 0.0155</td><td>0.9334 ± 0.0099</td><td>0.8901 ± 0.0064</td><td>0.9247</td><td>0.9211 ± 0.0097</td></tr><tr><td>F1 Score</td><td>0.3100 ± 0.0143</td><td>0.4125 ± 0.0054</td><td>0.5138 ± 0.0097</td><td>0.4277</td><td>0.4320 ± 0.0077</td></tr></table>

![](/api/attachments/FY6RNHBH/fulltext/images/f1f11e72668085271c3d831fa9a88ad9d79620d5dbb5e5789b4326aa8642dc0f.jpg)  
Fig. 8. Application scenario: decision support system provided to medical experts

## Acknowledgements

This project was partially supported by the key project of National Natural Science Foundation of China (Big Data Driven Innovation and

Management of Intelligent Healthcare, Grant No.: 71532002), IBM Faculty Awards (RDP-Qiu2016 and RDP-Qiu2017), and Penn State ICS Seed Grants (Deep Learning, 2018–19 and Reinforcement Learning, 2019–2020).

## References

[1] M. Bavati, S. Bhaskar. A. Montanari, Statistical analysis of a low cost method for multiple disease prediction, Statistical Methods in Medical Research 27 (8) (2018) 2312–2328.

[2] N.V. Chawla, D.A. Davis, Bringing big data to personalized healthcare: a patientcentered framework, Journal of General Internal Medicine 28 (3) (2013) 660–665.

[3] A.J. Frandsen, Machine Learning for Disease Prediction, Brigham Young University, Master thesis, 2016.

[4] M. Nasiri, B. Minaei, A. Kiani, Dynamic recommendation: disease prediction and prevention using recommender system, International Journal Basic Scientific Medicine 1 (1) (2016) 13–17

[5] C.A. Hidalgo, N. Blumm, A.L. Barabási, et al., A dynamic network approach for th study of human phenotypes, PLoS Computational Biology 5 (4) (2009) e1000353.

[6] A.B. Jensen, P.L. Moseley, T.I. Oprea, et al., Temporal disease trajectories condensed from population-wide registry data covering 6.2 million patients, Nature Communications 5 (2014).1–10

[7] V. Kannan, F. Swartz, N.A. Kiani, et al., Conditional disease development extracted from longitudinal health care cohort data using layered network construction, Scientific Reports 6 (2016).1–14.

[8] D. Gligorijevic, J. Stojanovic, Z. Obradovic, Improving Confidence while Predicting Trends in Temporal Disease Networks, Preprint at, 2018. https://arxiv.org/abs 1803.11462.

[9] K.S. Lakshmi, G. Vadivu, A novel approach for disease comorbidity prediction using weighted association rule mining, Journal of Ambient Intelligence and Humanized Computing (2019), https://doi.org/10.1007/s12652-019-01217-1 Online access at.

[10] D.A. Davis, N.V. Chawla, N. Blumm, N.A. Christakis, A.L. Barabási, Predicting individual disease risk based on medical history, Proceedings of the 17th ACM Conference on Information and Knowledge Management, ACM, Napa Valley, 2008, pp. 769–778.

[11] K. Steinhaeuser, N.V. Chawla, A network-based approach to understanding and predicting diseases, Social Computing and Behavioral Modeling, Springer US, 2009, pp. 209–216.

[12] F. Folino, C. Pizzuti, A comorbidity-based recommendation engine for disease prediction, Proceedings of 2010 IEEE 23rd International Symposium on Computer Based Medical Systems (CBMS), IEEE, Bentley, Australia, 2010, pp. 6–12.

[13] F. Folino, C. Pizzuti, Link prediction approaches for disease networks, Proceeding of International Conference on Information Technology in Bio-and Medical Informatics, Springer Berlin Heidelberg, Vienna, Austria, 2012, pp. 99–108.

[14] A.K. Rider, N.V. Chawla, An ensemble topic model for sharing healthcare data and predicting disease risk, Proceedings of the International Conference on Bioinformatics, Computational Biology and Biomedical Informatics, ACM. Washington, 2013, pp. 333–337.

[15] F. Folino. C. Pizzuti. Combining Markoy models and association analysis for disease prediction, Proceedings of International Conference on Information Technology in Bio-and Medical Informatics, Springer Berlin Heidelberg, Toulouse, France, 2011, pp. 39–52.

[16] F. Folino, C. Pizzuti, A recommendation engine for disease prediction, Information Systems and E-Business Management 13 (4) (2015) 609–628.

[17] M. Khalilia, S. Chakraborty, M. Popescu, Predicting disease risks from highly imbalanced data using random forest, BMC Medical Informatics and Decision Making 11 (1) (2011) 1–13.

[18] C.D. Chang, C.C. Wang, B. Jiang, Using data mining techniques for multi-diseases prediction modeling of hypertension and hyperlipidemia by common risk factors, Expert Systems with Applications 38 (5) (2011) 5507–5513.

[19] A. Maxwell, R. Li, B. Yang, et al., Deep learning architectures for multi-label classification of intelligent health risk prediction. BMC Bioinformatics 18 (14) (2017) 523–533.

[20] J. Billings, I. Blunt, A. Steventon, A. Steventon, T. Georghiou, G. Lewis, M. Bardsley, Development of a predictive model to identify inpatients at risk of re-admission within 30 days of discharge (PARR-30). BMJ Open 2 (4) (2012) 1–10.

[21] S.K. Thygesen, C.F. Christiansen, S. Christensen, et al., The predictive value of ICD 10 diagnostic coding used to assess Charlson comorbidity index conditions in the population-based Danish National Registry of patients, BMC Medical Research Methodology 11 (1) (2011) 1–6.

[22] World Health Organization, International statistical classification of diseases and related health problems, 10th revision, Retrieved January 8, 2017. Available at, 2016. http://apps.who.int/classifications/icd10/browse/2016/en.

[23] C.S. Dangare, S.S. Apte, Improved study of heart disease prediction system using data mining classification techniques. International Journal of Computer Applications 47 (10) (2012) 44–48.

[24] L. Chen, X. Li, Y. Yang, H. Kurniawati, Q.Z. Sheng, H.Y. Hu, N. Huang, Personal health indexing based on medical examinations: a data mining approach, Decision Support Systems 81 (2016) 54–65.

[25] M. Langarizadeh, F. Moghbeli, Applying naive bayesian networks to disease pre diction: a systematic review. Acta Informatica Medica 24 (5) (2016) 364–369.

[26] Y. Hao, M. Usama, J. Yang, et al., Recurrent convolutional neural network based multimodal disease risk prediction, Future Generation Computer Systems 92 (2019) 76–83.

[27] D.A. Martínez-Bello. A. López-Ouílez, A.T. Prieto. Relative risk estimation of dengue disease at small spatial scale. International Journal of Health Geographics 16 (1) (2017) 31.

[28] T.M. Loux, C. Drake, J. Smith-Gagen, A comparison of marginal odds ratio esti mators, Statistical Methods in Medical Research 26 (1) (2017) 155–175

[29] D. Dasgupta, N.V. Chawla, MedCare: Leveraging medication similarity for disease prediction, Proceedings of 2016 IEEE International Conference on Data Science and Advanced Analytics, IEEE, Montreal, Canada, 2016, pp. 706–715.

[30] D.A. Davis, N.V. Chawla, N.A. Christakis, A.L. Barabási, Time to CARE: a collaborative engine for practical disease prediction, Data Mining and Knowledge Discovery 20 (3) (2010) 388–415.

[31] X. Ji, S. Chun, J. Geller, A collaborative filtering approach to assess individua condition risk based on patients’ social network data, Proceedings of the 5th ACM Conference on Bioinformatics. Computational Biology, and Health Informatics ACM, California, 2014. pp. 639–640

[32] X. Ji, S.A. Chun, J. Geller. V. Oria. Collaborative and traiectory prediction models of medical conditions by mining patients' social data. Proceedings of 2015 JEEE International Conference on Bioinformatics and Biomedicine, IEEE, Washington, 2015. pp. 695–700.

[33] X. Ji, S.A. Chun, J. Geller, Predicting comorbid conditions and trajectories using social health records, JEEE Transactions on Nanobioscience 15 (4) (2016) 371–379

[34] F. Folino, C. Pizzuti, M. Ventura, A comorbidity network approach to predict disease risk, Proceedings of Information Technology in Bio-and Medical Informatics, Springer Berlin Heidelberg, Bilbao, Spain, 2010, pp. 102–109.

[35] T.H. McCormick, C. Rudin, D. Madigan, Bayesian hierarchical rule modeling fo predicting medical conditions, The Annals of Applied Statistics 6 (2) (2012) 652–668.

[36] X. Wang, F. Wang, J. Hu, A multi-task learning framework for joint disease risk prediction and comorbidity discovery, Proceedings of 2014 22nd Internationa Conference on Pattern Recognition, IEEE, Stockholm, Sweden, 2014, pp. 220–225.

[37] R. Li, H. Zhao, Y. Lin, et al., Multi-label classification for intelligent health risk prediction, Proceedings of 2016 IEEE International Conference on Bioinformatic and Biomedicine, IEEE, Shenzhen, China, 2016, pp. 986–993.

[38] R. Bellazzi, B. Zupan, Predictive data mining in clinical medicine: current issues and guidelines, International Journal of Medical Informatics 77 (2) (2008) 81–97.

[39] R. Miotto, L. Li, B.A. Kidd, et al., Deep patient: an unsupervised representation to predict the future of patients from the electronic health records, Scientific Reports 6 (2016) 1–10.

[40] E. Choi, M.T. Bahadori, A. Schuetz, et al., Doctor ai: Predicting clinical events via recurrent neural networks, Proceedings of the 1st Machine Learning for Healthcare Conference, 56 PMLR, 2016, pp. 301–318.

[41] N. Razavian, J. Marcus, D. Sontag, Multi-task prediction of disease onsets from longitudinal laboratory tests, Proceedings of the 1st Machine Learning for Healthcare Conference, 56 PMLR, 2016, pp. 73–100.

[42] Y.J. Kim, Y.G. Lee, J.W. Kim, et al., High Risk Prediction from Electronic Medical Records Via Deep Attention Networks, Preprint at, 2017. https://arxiv.org/abs 1712.00010.

[43] F. Ma, R. Chitta, J. Zhou, et al., Dipole: Diagnosis prediction in healthcare via attention-based bidirectional recurrent neural networks, Proceedings of the 23rd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, ACM. Canada. 2017, pp. 1903–1911

[44] P. Nguyen, T. Tran, S. Venkatesh, Resset: A recurrent model for sequence of sets with applications to electronic medical records. Proceedings of 2018 International Joint Conference on Neural Networks (IJCNN), IEEE, Brazil, 2018, pp. 1–9.

[45] T. Wang, R.G. Qiu, M. Yu, Multiple-disease risk predictive modeling based on directed disease networks, 2019 INFORMS Conference on Service Science, INFORMS Nanjing, China, 2019.

[46] A. Chen, K.H. Jacobsen, A.A. Deshmukh, et al., The evolution of the disability adjusted life year (DALY), Socio-Economic Planning Sciences 49 (2015) 10–15

[47] World Health Organization, Estimated DALYs by cause, sex and WHO member state: 2016, Available at, 2018. https://www.who.int/healthinfo/global\_burden disease/estimates/en/index1.html.

[48] J.L. Herlocker, J.A. Konstan, L.G. Terveen, et al., Evaluating collaborative filtering recommender systems. ACM Transactions on Information System 22 (1) (2004) 5–53.

[49] A. Gunawardana, G. Shani, A survey of accuracy evaluation metrics of recommendation tasks, Journal of Machine Learning Research 10 (2009) 2935–2962.

[50] M.L. Zhang, Z.H. Zhou, A review on multi-label learning algorithms, IEEE Transactions on Knowledge and Data Engineering 26 (8) (2014) 1819–1837.

[51] A. Clare, R.D. King, Knowledge discovery in multi-label phenotype data, European Conference on Principles of Data Mining and Knowledge Discovery, Springer, Berlin, 2001, pp. 42–53.

Tingyan Wang received a Ph.D. in Management Science and Engineering from Tsinghua University in June 2018. She is now a postdoctoral researcher in the Nufield Department of Medicine at the University of Oxford. She is currently also appointed in an honorary capacity as Data Analyst by Oxford University Hospitals NHS Trust. Most of her work has been focused on patients' electronic health records analysis and risk predictive modeling by leveraging statistics, machine learning and deep learning techniques. Her research interests include Healthcare Analytics, Medical Informatics, Disease Risk Prediction, Longitudinal Data Analysis, and Patient Care Process Analysis.

Robin Oiu holds a Ph.D. in Industrial Engineering and a Ph.D. (minor) in Computer Science both from The Pennsylvania State University. He is currently Director of Big Data Lab and Professor of Information Science at Penn State. He has had over 180 peer-reviewed publications, including 3 books. He is on the advisory board of Service Science and serves as an associate editor of JFEE Transactions on Systems. Man and Cybernetics and JFFE Transactions on Industrial Informatics. He was the Editor-in-Chief of Service Science and the Editor-in-Chief of International Journal of Services Operations and Informatics. He was the founding chair of the Logistics and Services Technical Committee. JEEE Intelligent Transportation Systems Society and the founding chair of Service Science Section of the INFORMS. His research interests include Big Data, Data Analytics, Smart Service Systems, Service Science, Service Operations and Management, Information Systems, and Manufacturing and Supply Chain Management.

Ming Yu holds a Ph.D. Ph.D. in Industrial Engineering from the National University of Ireland. He is currently Associate Professor in the Department of Industrial Engineering at Tsinghua University. He has been studying how to use industrial engineering especially information technology to the healthcare field from 2004 and he has intensive cooperation with multiple hospitals in China. He has publications in Journal of biomedical informatics, BMC Medical Informatics, and Decision Making. He has been working on the coding system development of the ICD-10 simplified version applied in Asia Pacific area for WHO Family of International Classifications (WHO-FIC) from 2015 He was an active member of the Program Board in several international conferences. He has been a Professional Member in Chinese Mechanical Engineering Association (CMES), and Institute Engineering, Ireland (MIEI). His research interests include Medical Informatics, Natural Language Processing, System Engineering, and Management Information System.

Runtong Zhang was born in November 1963, in Chaoyang, Liaoning, China. He got his

Ph.D. in Production Engineering and Management from Technical University of Crete in Greece in 1996, and his B.S. in Computer Science and Automation from the Dalian Maritime University in China in 1985, respectively. He is presently a professor and head of the Department of Information Management at Beijing Jiaotong University, China. H was also with the Swedish Institute of Computer Science as a senior researcher, and th

Port of Tianjin Authority as an engineer. His current research interests include big data, health-care management, operations research and artificial intelligence. He has published over 300 papers in referenced journals and conferences, and 40 books. He has been a PI for over 100 research projects and is a holder of 9 patents. He has been Senior Member, IEEE and a general chair or co-chair for over 10 IEEE sponsored international conferences.
