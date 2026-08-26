---
otero_id: 19686
otero_key: "B7AZXNG6"
title: "A cross-domain recommender system through information transfer for medical diagnosis"
authors: "Wenjun Chang; Qian Zhang; Chao Fu; Weiyong Liu; Guangquan Zhang; Jie Lu"
year: "2021"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2020.113489"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A cross-domain recommender system through information transfer for medical diagnosis

![](/api/attachments/B7AZXNG6/fulltext/images/e7d24d616a0bb5ff04cb19bc5c1b699fab83446acf62fe0d17a3af66a9a30370.jpg)

Wenjun Chang <sup>a,b,1</sup>, Qian Zhang <sup>b,1</sup>, Chao Fu <sup>a</sup>, Weiyong Liu <sup>c</sup>, Guangquan Zhang <sup>b</sup>, Jie Lu <sup>b,\*</sup>

<sup>a</sup> School of Management, Hefei University of Technology, PR China

<sup>b</sup> Center for Artificial Intelligence, University of Technology Sydney, Australia

<sup>c</sup> Department of Ultrasound, The First Affiliated Hospital of USTC, PR China

## A R T I C L E I N F O

Keywords: Recommender systems Cross-domain Collaborative filtering Medical diagnosis

## A B S T R A C T

The electronic diagnostic records of patients, primarily collected by hospitals, comprise valuable data for the development of recommender systems to support physicians in predicting the risks associated with various diseases. For some diseases, the diagnostic record data are not sufficient to train a prediction model to generate recommendations; this is referred to as the data sparsity problem. Cross-domain recommender systems offer a solution to this problem by transferring knowledge from a similar domain (source domain) with sufficient data for modeling to facilitate prediction in the current domain (target domain). However, building a cross-domain recommender system for medical diagnosis presents two challenges: (1) uncertain representations, such as the symptoms characterized by interval numbers, are often used in medical records, and (2) given two different diseases, the feature spaces of the two diagnostic domains are often disparate because the diseases are only likely to share a few symptoms. This study addresses these challenges by proposing a cross-domain recommender system, named information transfer for medical diagnosis (ITMD), to provide physicians with personalized recommendations for disease risks. In ITMD, a novel dissimilarity measurement was performed for diagnosis, represented as interval numbers. The space alignment technique eliminated the feature space divergence caused by different symptoms between two diseases, and the development of collective matrix factorization enabled knowledge transfer between the source and target domains. Experiments and a case study using real-world data demonstrated that ITMD outperforms four baselines and improves the accuracy of recommendations for disease risks in patients to support physicians in determining a final medical diagnosis

## 1. Introduction

In clinical medicine, medical diagnosis is often the first step in pre dicting and preventing the possible onset of a disease [1]. Early diag nosis helps in preventing further deterioration and increases the possibility of complete healing, especially for cancer. For example, breast tumors are a common malignant neoplasm in women, and over 60% of patients with breast tumors are incurable [2]. However, breast cancer is preventable and curable if the tumor is diagnosed in its early stages. Electronic medical records comprise significant information that could help physicians in diagnosing several diseases accurately in the early stage. Because the symptoms and situations vary among patients, personalized recommendations are required for medical diagnosis by physicians. Recommender systems are an effective tool to provide personalized decision support for medical diagnosis, such as chronic disease [3], heart disease [4], and right heart catheterization [5]. In a recommender system for medical diagnosis, a user is represented by a patient, an item is represented by the level of disease risks, and the probability of a patient to a disease risk is represented by a rating of the user to an item given by the physician or a prediction model.

Although recommender systems can provide medical diagnosis support, they encounter the data sparsity problem [6–9]. Data sparsity in medical diagnosis occurs owing to insufficient medical records of some diseases because the incidence of these diseases is low or physi cians are inexperienced; it can also be attributed to the limited access to medical records. Decision support with sparse data in the medical field may generate inaccurate results for disease diagnosis. For example, tetanus is a rare but life-threatening disease. It is difficult to use medical records to support physicians in providing more accurate diagnoses when the available data are insufficient and outdated for tetanus. The use of such insufficient data to estimate the relations between symptoms (e.g., age, pattern, severity, and interventions) in the diagnosis of tetanus is inconclusive; thus, the deductions generated with insufficient data are not permitted to support the diagnosis of this disease [10]. Recommender systems built in domains without sufficient data fail to provide accurate recommendations to physicians.

To alleviate the problem of data sparsity, a feasible strategy involves the adoption of transfer learning. Transfer learning has been widely used to manage data sparsity in medical diagnosis [11–13]. In recommender systems for medical diagnosis, transfer learning can be combined with collaborative filtering to extract knowledge from a source domain with sufficient data and transfer it to the target domain, known as crossdomain recommender systems [14]. In medical diagnosis, two types of disease diagnoses are considered to be of two similar domains when there are three perspectives of similarity between them [15–17]; that is, (a) the organs in which the two diseases occur belong to one type, such as the gland, abdomen, and superficial organs; (b) in general, the cyt opathy and pathogenesis of the two diseases are similar; and (c) the two diseases are diagnosed by similar standards. Owing to the three per spectives of similarity, two similar diseases will lead to similar relations between their symptoms, which are considered as the knowledge transferred from the source disease to the target disease. To transfer the relations between symptoms across two similar diseases, the over lapping symptoms serve as a bridge to align these relations. The extracted relations between symptoms are used to generate recom mendations of the target disease.

A cross-domain recommender system for medical diagnosis uses the knowledge extracted from relatively sufficient symptom observation data of one disease (source domain) to support physicians in making decisions regarding the diagnosis of another disease with sparse symp tom data (target domain). The establishment of such recommender system generally faces two challenges. (1) Medical records contain un certain representations of symptoms and disease risks. For example, five diagnostic categories of disease risks are represented as interval numbers in the diagnosis of thyroid cancer, as {TIRADS 3, TIRADS 4A, TIRADS 4B, TIRADS 4C, TIRADS 5} = {[0, 0.03], (0.03, 0.25], (0.25, 0.75], (0.75, 0.95], (0.95, 1]}. TI-RADS 5 means the physician evaluates the thyroid legions to have a 95–100% chance of being malignant, which strongly indicates thyroid cancer, while TI-RADS 4A indicates a 3–25% chance of malignancy. The prediction of diagnoses as a disease risk with an interval number and measuring the differences between diagnosis predictions with interval numbers between two domains are urgent problems that require solutions. (2) The feature (symptom) spaces of two different diseases in the source and target domains are different and mismatched. Considering breast cancer as the source domain and tophus as the target domain, the five symptoms of a breast lump suggest the presence of breast cancer, such as the margin, contour, echogenicity, calcification, and vascularity. In contrast, tophus is assessed against six symptoms, i.e., the number, size, contour, echogenicity, calcification, and halo. Thus, the two diagnoses only share three symptoms. Addi tionally, the severity values related to the shared symptoms may not be in the same distribution, which also needs to be considered before knowledge extraction.

To address these two challenges, this study develops a new crossdomain recommendation method, called information transfer for med ical diagnosis (ITMD), to provide personalized recommendations for the risk level of particular diseases to support physicians in diagnosing pa tients with insufficient medical records. In the ITMD method, after normalization, two transformation matrices are learned to align the symptom space of the source domain with that of the target domain. A novel dissimilarity is proposed to measure the difference in disease risks indicated in the diagnostic categories. The symptom relations between two domains are then learned as shared knowledge by minimizing the dissimilarities between the diagnoses and their predictions in the two domains simultaneously. In summary, the main contributions of this study are as follows:

(1) A new dissimilarity measurement is developed to characterize the discrepancies between diagnoses with interval numbers corre sponding to challenge (1). This measurement is more suitable for diagnostic tasks than distance measurement because it fully re flects the risk intervals associated with each diagnostic category.

(2) A space alignment method is established to deal with the mismatch of two different symptom spaces corresponding to challenge (2). This method eliminates the differences in the number of symptoms and their data distributions in the symptom spaces of the source and target domains.

(3) The ITMD method is proposed, which is a new cross-domain recommender system to recommend suitable medical di agnostics; it can effectively predict the risk level of patients for particular diseases. With constraints of condition number on collective matrix factorization, this method transfers knowledge from the source domain for support decision making in the target domain. The proposed dissimilarity measurement and space alignment method are used in the recommender system.

(4) A set of comprehensive experiments and a real-world case study (with thyroid cancer and breast cancer as the source and target domains, respectively) are performed, which demonstrated the accuracy and effectiveness of the proposed ITMD method for recommending disease risks in comparison to four baselines. The results of the case study particularly indicate the effectiveness considering decision support for real-world diagnosis for four physicians.

The remainder of this paper is organized as follows. Section 2 pre sents the work related to this study. Section 3 introduces the medical diagnosis problems based on the interval number in one domain and formally defines the problem being examined in this study. In Section 4, the ITMD method is proposed. Section 5 details the experiments conducted in two cases: one where the symptom spaces are the same, and the other where they are different. The results show that our method performs better than the four baseline methods. Section 6 illustrates how the proposed method works in a real-world scenario as a case study. The conclusions and directions for further research are provided in Section 7.

## 2. Related work

This section first presents a review of the relevant work on recom mender systems and their applications in the medical domain, followed by a summary of the current state-of-the-art cross-domain recommender systems.

## 2.1. Recommender systems and their applications in medical domain

Because a large number of electronic health records have been collected by hospitals, the information extracted from these data is used to develop recommender systems that can support the decision-making process of physicians for diagnosing diseases. For example, a recom mendation system framework was developed to support physicians with personalized prescriptions to improve their efficiency and reduce the risk of making errors in daily clinical consultation with patients [18]. Another example involves the use of a collaborative filtering technique with clustering to provide medical advice to cardiac patients [19]. Measurement between treatments and a unified recommendation method were proposed in [20] to recommend treatments to new patients according to their demographic information and disease severity.

In addition, recommender systems have been developed to support diagnosis in different domains of disease diagnosis based on collaborative filtering. Hussein et al. [3] proposed a chronic disease diagnosis recommender system approach based on a hybrid method using multiple classifications and unified collaborative filtering to pro vide high-accuracy disease risk prediction and medical recommenda tion. Hassan and Syed [4] built a collaborative filtering framework to achieve high accuracy in predicting sudden cardiac death and recurrent myocardial infarction by concurrently matching new cases to historical records as well as patient demographics to adverse outcomes. Davis et al. [21] presented a recommender system that used collaborative filtering to predict the potential disease risks of a patient based on sufficient medical history and that of similar patients.

The aforementioned recommender systems and their key character istics are summarized in Table 1. The existing recommender systems in the medical domain, for example, [3,4] and [18–20], cannot manage the challenges of interval data and data sparsity, which commonly occur in practice.

## 2.2. Cross-domain recommender systems

Cross-domain recommender systems can be divided into two broad categories. i.e.. user-item matrix-based methods and additional information-based methods.

## 2.2.1. Cross-domain recommender systems with user-item rating matrix

Cross-domain recommender systems with a user-item rating matrix can have non-overlapping, partially overlapping, or fully overlapping users/items. Non-overlapping users/items implies that all users and items in the source and target domains are different. Here, users and items are usually clustered into groups, and shared knowledge is extracted at the group level. Li et al. [22] provided a generative rating matrix model by transferring a shared cluster-level rating matrix across domains. Gao et al. [23] created a novel cross-domain recommendation model that transferred rating patterns at a common cluster level. Zhang et al. [24] extracted the shared group-level knowledge based on consistent user/item group information, adjusted by a domain adapta tion technique.

Partially overlapping users/items refer to situations where some of the users or items are common to both domains. These methods usually adopt matrix factorization models and implement shared knowledge transfer based on overlapping users or items. Pan et al. [25] established a coordinate system transfer method based on sparse matrix trifactorization to reduce the effect of data sparsity, while Pan and Yang [26] constructed a transfer framework based on collective factorization with sparse data by transferring explicit binary rating information from the source to the target domain. Zhang et al. [27] proposed a crossdomain recommender system that used kernel-induced knowledge transfer to manage partially overlapping entities. The entity correlations of the overlapping entities were determined via domain adaptation and diffusion kernel completion methods, which also served as constraints to generate a new matrix factorization technique.

## 2.2.2. Cross-domain recommender systems with additional information

Some cross-domain recommender systems connect two domains through additional information, instead of user-item ratings [28], such as social network information, tagging information, review information, and metadata. Chen et al. [29] established a cross-domain recommender system that fused social network information and cross-domain rating data to improve recommendations. The cluster-level tensor was considered as shared information in the source and target domains. Jiang et al. [30] proposed a hybrid random walk method to transfer knowledge from auxiliary item domains to the target domain using so cial network data to create a star-structured hybrid graph. Shi et al. [31] used shared tags as bridges to connect the source and target domains. To study the correlations between tags from different domains, Fang et al. [32] constructed a tag matrix transfer model to obtain rating patterns by transferring the shared tag co-occurrence matrix information in multiple domains. The user-tag-item relation was factorized into user-tag and item-tag relations. Hao et al. [33] regularized joint matrix factorization with the constraints of inter-domain and intra-domain correlations, built based on the tagging information. Xin et al. [34] proposed a nonlinear cross-domain recommendation framework with review information. Joint tensor factorization [35] was modeled to transfer the review in formation in cross-domain recommendations. Fern´andez-Tobías et al. [36] developed cross-domain hybrid matrix factorization models that exploited metadata as a bridge between items across domains.

These cross-domain recommender systems and their key character istics are summarized in Table 1. The existing cross-domain recom mender systems, for example, [21–27] and [29–36], are not specifically designed for medical diagnosis problems; thus, they cannot be applied directly to the problem being investigated in this study. Moreover, the interval data that are commonly observed in medical diagnosis cannot be addressed by any existing study.

Table 1  
Summary of related works.

<table><tr><td rowspan="3"></td><td colspan="3">Data</td><td colspan="3">Domain</td><td colspan="2">User/item overlap</td><td colspan="2">Field</td></tr><tr><td colspan="2">User-item rating</td><td rowspan="2">Additional information</td><td rowspan="2">Single</td><td rowspan="2">Two</td><td rowspan="2">Multiple</td><td rowspan="2">Non-overlap</td><td rowspan="2">Overlap</td><td rowspan="2">Medical</td><td rowspan="2">Non-medical</td></tr><tr><td>Discrete value</td><td>Interval number</td></tr><tr><td>[18]</td><td>×</td><td></td><td></td><td>×</td><td></td><td></td><td>-</td><td>-</td><td>×</td><td></td></tr><tr><td>[19]</td><td>×</td><td></td><td></td><td>×</td><td></td><td></td><td>-</td><td>-</td><td>×</td><td></td></tr><tr><td>[20]</td><td>×</td><td></td><td></td><td>×</td><td></td><td></td><td>-</td><td>-</td><td>×</td><td></td></tr><tr><td>[3]</td><td>×</td><td></td><td></td><td>×</td><td></td><td></td><td>-</td><td>-</td><td>×</td><td></td></tr><tr><td>[4]</td><td>×</td><td></td><td></td><td>×</td><td></td><td></td><td>-</td><td>-</td><td>×</td><td></td></tr><tr><td>[21]</td><td>×</td><td></td><td></td><td>×</td><td></td><td></td><td>-</td><td>-</td><td>×</td><td></td></tr><tr><td>[22]</td><td>×</td><td></td><td></td><td></td><td></td><td>×</td><td>×</td><td></td><td></td><td>×</td></tr><tr><td>[23]</td><td>×</td><td></td><td></td><td></td><td></td><td>×</td><td>×</td><td></td><td></td><td>×</td></tr><tr><td>[24]</td><td>×</td><td></td><td></td><td></td><td>×</td><td></td><td>×</td><td></td><td></td><td>×</td></tr><tr><td>[25]</td><td>×</td><td></td><td></td><td></td><td>×</td><td></td><td></td><td>×</td><td></td><td>×</td></tr><tr><td>[26]</td><td>×</td><td></td><td></td><td></td><td>×</td><td></td><td></td><td>×</td><td></td><td>×</td></tr><tr><td>[27]</td><td>×</td><td></td><td></td><td></td><td>×</td><td></td><td></td><td>×</td><td></td><td>×</td></tr><tr><td>[29]</td><td>×</td><td></td><td>×</td><td></td><td>×</td><td></td><td>×</td><td></td><td></td><td>×</td></tr><tr><td>[30]</td><td>×</td><td></td><td>×</td><td></td><td>×</td><td></td><td></td><td>×</td><td></td><td>×</td></tr><tr><td>[31]</td><td>×</td><td></td><td>×</td><td></td><td></td><td>×</td><td>×</td><td></td><td></td><td>×</td></tr><tr><td>[32]</td><td>×</td><td></td><td>×</td><td></td><td></td><td>×</td><td>×</td><td></td><td></td><td>×</td></tr><tr><td>[33]</td><td>×</td><td></td><td>×</td><td></td><td>×</td><td></td><td>×</td><td></td><td></td><td>×</td></tr><tr><td>[34]</td><td>×</td><td></td><td>×</td><td></td><td>×</td><td></td><td></td><td>×</td><td></td><td>×</td></tr><tr><td>[35]</td><td>×</td><td></td><td>×</td><td></td><td>×</td><td></td><td></td><td>×</td><td></td><td>×</td></tr><tr><td>[36]</td><td>×</td><td></td><td>×</td><td></td><td>×</td><td></td><td></td><td>×</td><td></td><td>×</td></tr><tr><td>ITMD</td><td></td><td>×</td><td>×</td><td></td><td>×</td><td></td><td>×</td><td></td><td>×</td><td></td></tr></table>

## 3. Problem definition

This section first presents the problem formulation for medical diagnosis with interval number in one domain. Then, we formally describe the cross-domain medical diagnosis problem under study.

## 3.1. Medical diagnosis with interval number in one domain

In medical diagnosis, physicians diagnose the likely cause of the conditions of a patient based on their symptoms. A formal definition of this medical diagnosis problem for a group of patients is presented below.

Consider three lists, $P = \{ P _ { 1 } , . . . , P _ { M } \} , S = \{ S _ { 1 } , . . . , S _ { L } \}$ , and $C = \{ C _ { 1 } ,$ $\dots , C _ { N } \}$ , where P is a list of patients, S is a list of symptoms, and C is a list of diagnostic categories. Each symptom, $\begin{array} { r } { S _ { l } , } \end{array}$ has N levels of severity, as L $( S _ { l } ) = \{ L _ { n } ( S _ { l } ) , n = 1 , . . . , N _ { l } \} = \{ [ L _ { 1 } ^ { - } ( S _ { l } ) , L _ { 1 } ^ { + } ( S _ { l } ) ] , ( L _ { 2 } ^ { - } ( S _ { l } ) , L _ { 2 } ^ { + } ( S _ { l } ) ] , . . . , ( L _ { N } ^ { - } ( S _ { l } ) ) \} = 0 .$ , L<sup>+</sup> (S )]}, where $L _ { 1 } ^ { - } ( S _ { l } ) = 0 , L _ { N l } ^ { + } ( S _ { l } ) = 1 , L _ { n } ^ { + } ( S _ { l } ) = L _ { n + 1 } ^ { - } ( S _ { l } ) , n = 1 , . . . , N _ { l } - 1$ , and $\cup _ { n = 1 } ^ { N _ { l } } L _ { n } ( S _ { l } ) = \ [ 0 , 1 ]$ . The relations between patients, symptoms, and diagnostic categories were recorded in three matrices. $\pmb { U } = ( u _ { m l } ) _ { M \times L }$ denotes the patient-symptom matrix, where $u _ { m l } { \in } L ( S _ { l } )$ is the level of a symptom, $s _ { l s }$ in patient $P _ { m } . \pmb { V } = ( \nu _ { l n } ) _ { L \times N }$ denotes the symptom-category matrix, where $\nu _ { l n } { \in } [ 0 , 1 ]$ and $\begin{array} { r } { \sum _ { n = 1 } ^ { N } \nu _ { l n } = 1 . ~ R = ( r _ { m n } ) _ { M \times N } } \end{array}$ is the patientcategory matrix, where $r _ { m n } \in [ 0 ,$ , 1] and $\begin{array} { r } { \sum _ { n = 1 } ^ { N } r _ { m n } = 1 } \end{array}$ . These matrices correspond to the reasoning followed by a physician when making a diagnosis; i.e., relate a patient to some symptoms, relate those symptoms to a diagnostic category, and then relate the patient to that diagnostic category. Thus, the diagnosis problem involves the determination of matrix R from matrices U and V.

A recommender system is used to assist physicians to provide the patient-category matrix R, which can be simply formulated as $\widehat { \pmb R } =$ $f ( U \mid V )$ . The following example can help in understanding the details of this problem.

Example 1. Suppose a physician needs to diagnose whether eight patients $P _ { m } \left( m = 1 , . . . , 8 \right)$ have breast cancer. This requires assessing the suspected breast nodules against five symptoms S $( l = 1 , . . . , 5 ) , \mathrm { i . e . , }$ margin, contour, echogenicity, calcification, and vascularity. Here, the same levels $L ( S _ { l } ) = \left\{ [ 0 , 0 . 0 3 ] , ( 0 . 0 3 , 0 . 2 5 ] , ( 0 . 2 5 , 0 . 7 5 ] , ( 0 . 7 5 , 0 . 9 5 ] \right.$ (0.95, 1]} are applied to symptoms. A patient-symptom matrix, U= $( u _ { m l } ) _ { 8 \times 5 } ,$ , is presented in Table 2.

The physician then relates these symptoms to the five diagnostic categories {TI-RADS 3, 4A, 4B, 4C, and 5} denoted as $C _ { n } \left( n = 1 , . . . , 5 \right) ;$ this produces the symptom-category matrix, $\pmb { V } = ( \nu _ { l n } ) _ { 5 \times 5 } ,$ , as depicted in Table 3.

Matrices U and V now provide a basis for relating the eight patients to the five diagnostic categories; i.e., matrix $\pmb { R } = ( r _ { m n } ) _ { 8 \times 5 } ,$ , as presented in Table 4.

Thus, the diagnosis of breast cancer is the process of determining matrix R from matrices U and V.

## 3.2. Cross-domain recommender systems for medical diagnosis

To formally define this medical diagnosis problem as it relates to our cross-domain setting, we assume that there are two related but different disease domains. One domain, the target domain, does not contain enough records to provide adequate diagnostic support; however, the other, the source domain, has an abundance of records. The problem under study, therefore, involves determining the usage of records from the source domain to improve diagnostic support in the target domain. First, a symptom space must be defined with interval numbers to describe the problem.

Patient-symptom matrix for eight patients with breast nodules.

<table><tr><td></td><td> $S_1$ </td><td> $S_2$ </td><td> $S_3$ </td><td> $S_4$ </td><td> $S_5$ </td></tr><tr><td> $P_1$ </td><td>(0.03, 0.25]</td><td>(0.95, 1]</td><td>(0.25, 0.75]</td><td>(0.95, 1]</td><td>(0.03, 0.25]</td></tr><tr><td> $P_2$ </td><td>[0, 0.03]</td><td>[0, 0.03]</td><td>[0, 0.03]</td><td>[0, 0.03]</td><td>(0.03, 0.25]</td></tr><tr><td> $P_3$ </td><td>(0.25, 0.75]</td><td>(0.95, 1]</td><td>(0.25, 0.75]</td><td>(0.25, 0.75]</td><td>(0.95, 1]</td></tr><tr><td> $P_4$ </td><td>(0.03, 0.25]</td><td>(0.95, 1]</td><td>(0.25, 0.75]</td><td>(0.25, 0.75]</td><td>(0.95, 1]</td></tr><tr><td> $P_5$ </td><td>(0.25, 0.75]</td><td>(0.25, 0.75]</td><td>(0.75, 0.95]</td><td>(0.95, 1]</td><td>[0, 0.03]</td></tr><tr><td> $P_6$ </td><td>(0.03, 0.25]</td><td>(0.03, 0.25]</td><td>[0, 0.03]</td><td>[0, 0.03]</td><td>(0.03, 0.25]</td></tr><tr><td> $P_7$ </td><td>[0, 0.03]</td><td>[0, 0.03]</td><td>(0.25, 0.75]</td><td>(0.95, 1]</td><td>(0.03, 0.25]</td></tr><tr><td> $P_8$ </td><td>(0.03, 0.25]</td><td>(0.25, 0.75]</td><td>(0.25, 0.75]</td><td>(0.03, 0.25]</td><td>(0.95, 1]</td></tr></table>

Table 3  
Symptom-category matrix of the five symptoms and five diagnostic categories.

<table><tr><td></td><td> $C_1$ </td><td> $C_2$ </td><td> $C_3$ </td><td> $C_4$ </td><td> $C_5$ </td></tr><tr><td> $S_1$ </td><td>0.2</td><td>0.15</td><td>0.35</td><td>0.15</td><td>0.15</td></tr><tr><td> $S_2$ </td><td>0.3</td><td>0.3</td><td>0.25</td><td>0.05</td><td>0.1</td></tr><tr><td> $S_3$ </td><td>0.25</td><td>0.3</td><td>0.2</td><td>0.15</td><td>0.1</td></tr><tr><td> $S_4$ </td><td>0.1</td><td>0.15</td><td>0.3</td><td>0.25</td><td>0.2</td></tr><tr><td> $S_5$ </td><td>0.3</td><td>0.25</td><td>0.2</td><td>0.2</td><td>0.05</td></tr></table>

Patient-category matrix showing the correspondences of the eight patients to the five diagnostic categories

<table><tr><td></td><td> $C_1$ </td><td> $C_2$ </td><td> $C_3$ </td><td> $C_4$ </td><td> $C_5$ </td></tr><tr><td> $P_1$ </td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td></tr><tr><td> $P_2$ </td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td> $P_3$ </td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td></tr><tr><td> $P_4$ </td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td></tr><tr><td> $P_5$ </td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td></tr><tr><td> $P_6$ </td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td></tr><tr><td> $P_7$ </td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td></tr><tr><td> $P_8$ </td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td></tr></table>

Suppose that $\boldsymbol { S } = \{ S _ { 1 } , . . . , S _ { N } \}$ represents a list of symptoms in a medical diagnosis problem with interval numbers. The symptom space for the diagnosis is generated by the associations between symptoms $S _ { l }$ and $s _ { k } ,$ where $l , k \in \{ 1 , . . . , N \}$ , which describe the influences o $\cdot _ { s _ { l } }$ and $S _ { k }$ on the disease risks. When the symptoms in the source and target do mains have the same number and distribution, the symptom spaces are the same in the two domains; otherwise, the symptom spaces are different. In this study, we focus on the latter, which is more challenging. Accordingly, the medical diagnosis problem under study is formally described.

Suppose that $( U _ { s } = ( u _ { m l } ^ { s } ) _ { M s \times L s } , V _ { s } = ( \nu _ { l n } ^ { s } ) _ { L s \times N s } , R _ { s } = ( r _ { m n } ^ { s } ) _ { M s \times N s } )$ and $\begin{array} { r } { ( U _ { t } { = } ( u _ { m l } ^ { t } ) _ { M t \times L t } , V _ { t } { = } ( \nu _ { l n } ^ { t } ) _ { L t \times N t } , R _ { t } { = } ( r _ { m n } ^ { t } ) _ { M t \times N t } ) } \end{array}$ represent the patientsymptom matrix, symptom-category matrix, and patient-category ma trix in the source and target domains, respectively. Here, $M _ { s }$ and $M _ { t }$ denote the number of patients, $L _ { s }$ and $L _ { t }$ are the number of symptoms, and $N _ { s }$ and $N _ { t }$ are the number of symptoms in the two domains. When the symptom spaces in the two domains are different, a cross-domain recommender system extracts knowledge from the source domain and predicts medical diagnoses in the target domain by $\widehat { \pmb R } _ { t } =$ $g ( R _ { s } , \ U _ { s } , \ V _ { s } , \ U _ { t } , \ V _ { t } )$

## 4. Cross-domain recommender system through information transfer for medical diagnosis

In this section, we present the proposed ITMD recommendation method. The ITMD method transfers the shared information contained in the symptom spaces from the source domain to the target domain when the symptom spaces in the two domains are different. The pro cedure of the ITMD method is presented in Fig. 1, which consists of five steps. (1) The patient-symptom matrices in the source and target do mains are normalized. (2) Symptom space alignment is designed to generate consistent symptom spaces in the two domains. (3) A new dissimilarity measurement is used to calculate the dissimilarities be tween the diagnoses and their predictions. (4) Information transfer is conducted based on the constraints on the symptom relation matrix. (5) Medical diagnosis support in the target domain is enabled. Next, we further demonstrate the ITMD method in detail

![](/api/attachments/B7AZXNG6/fulltext/images/5fdf38b9fa82d8a818881f629208401c4d5a1a96b6e679ed856780c1183a7fd0.jpg)  
Fig. 1. Five steps of the ITMD framework.

## 4.1. Step 1: Normalizing the patient-symptom matrix

To normalize the patient-symptom matrices $\pmb { U _ { s } }$ and $\scriptstyle { U _ { t } , }$ the interval valued matrices must be transformed into numerical matrices. Because all elements in $U _ { s }$ and $\scriptstyle { U _ { t } }$ are drawn from the interval sets L(S ), $\pmb { U _ { s } }$ and $\scriptstyle { U _ { t } }$ can be converted into averaged matrices $\overline { { U } } _ { s } = \left( \overline { { u } } _ { m l } ^ { s } \right) _ { M _ { s } \times L _ { s } }$ and $\begin{array} { r } { \overline { { U } } _ { t } ~ = } \end{array}$ $\left( \overline { { u } } _ { m l } ^ { t } \right) _ { M _ { t } \times L _ { t } }$ , respectively. Here, $\begin{array} { r } { \overline { { u } } _ { m l } ^ { s } = \frac { u _ { m l } ^ { s - } + u _ { m l } ^ { s + } } { 2 } ; } \end{array}$ , where $u _ { m l } ^ { s - }$ and $u _ { m l } ^ { s + }$ denote the lower and upper bounds of $u _ { m l s } ^ { s }$ , respectively. Likewise, $\begin{array} { r } { \overline { { u } } _ { m l } ^ { t } = \frac { u _ { m l } ^ { t - } + u _ { m l } ^ { t + } } { 2 } } \end{array}$ where $u _ { m l } ^ { t - }$ and $u _ { m l } ^ { t + }$ denote the lower and upper bounds of $u _ { m l } ^ { t }$ respectively.

Demonstrating the rationality of converting $u _ { m l } ^ { s }$ and $u _ { m l } ^ { t }$ into $\overline { { u } } _ { m l } ^ { s }$ and $\overline { { u } } _ { m l } ^ { t } ,$ , respectively, involves generalizing the relations between them as two propositions, as presented below.

Proposition 1. Consider a list of intervals $I _ { n } , n = 1 , . . . , N$ that satisfy

$$
\begin{array}{l} I _ {1} = \left[ I _ {1} ^ {-} I _ {1} ^ {+} \right] = \left[ 0 I _ {1} ^ {+} \right], \\ I _ {n} = \left(I _ {n} ^ {-} I _ {n} ^ {+} \right], n = 1, \dots , N - 1, \\ I _ {N} = \left(I _ {N} ^ {-} I _ {N} ^ {+} \right] = \left(I _ {N} ^ {-} 1 \right], \\ 0 \leq I _ {n} ^ {-} <   I _ {n} ^ {+} \leq 1, n = 1, \dots , N, \\ I _ {n} ^ {+} = I _ {n + 1} ^ {-}, n = 1, \dots , N - 1, \text { and } \\ \cup_ {n = 1} ^ {N} I _ {n} = [ 0 1 ], \end{array}\tag{1}
$$

and suppose that ${ \overline { { I } } } _ { n }$ denotes the average of $I _ { n } ( n = 1 , . . . , N ) ;$ it is calcu lated by $\begin{array} { r } { \overline { { I } } _ { n } = \frac { I _ { n } ^ { - } + I _ { n } ^ { + } } { 2 } , n = 1 , . . . , N . } \end{array}$ Then, it follows that $I _ { m } = I _ { n } \mathrm { i f f } \bar { I } _ { m } = \bar { I } _ { n } , m _ { \mathrm { \scriptscriptstyle m } }$ $n = 1 , . . . , N .$

The proof of Proposition 1 can be easily obtained. From Proposition 1, it is evident that there is a one-to-one correspondence between $I _ { n }$ and ${ \overline { { I } } } _ { n } .$ However, is the difference in size between $I _ { m }$ and $I _ { n }$ consistent with that between $\overline { { I } } _ { m }$ and $\textstyle { \overline { { I } } } _ { n } ?$ This is determined by measuring the possibility degree of $I _ { m }$ being superior to $I _ { n } \ [ 3 7 ]$ as follows:

$$
\begin{array}{l} p (I _ {m} > I _ {n}) \\ = \left\{ \begin{array}{l l} 1, & I _ {m} ^ {-} \geq I _ {n} ^ {+} \\ \frac {\left(I _ {m} ^ {+} - I _ {n} ^ {-}\right) ^ {2} - \left(I _ {m} ^ {+} - I _ {n} ^ {+}\right) ^ {2} - \left(I _ {m} ^ {-} - I _ {n} ^ {-}\right) ^ {2}}{2 \cdot \left(I _ {m} ^ {+} - I _ {m} ^ {-}\right) \cdot \left(I _ {n} ^ {+} - I _ {n} ^ {-}\right)}, & I _ {n} ^ {-} \leq I _ {m} ^ {-} <   I _ {n} ^ {+} \leq I _ {m} ^ {+} \\ 0. 5 \cdot \frac {\left(I _ {m} ^ {+} - I _ {n} ^ {-}\right) \cdot \left(I _ {m} ^ {+} - I _ {n} ^ {-}\right)}{\left(I _ {m} ^ {+} - I _ {m} ^ {-}\right) \cdot \left(I _ {n} ^ {+} - I _ {n} ^ {-}\right)}, & I _ {m} ^ {-} \leq I _ {n} ^ {-} <   I _ {m} ^ {+} \leq I _ {n} ^ {+} \\ \frac {I _ {m} ^ {+} - I _ {n} ^ {+}}{I _ {m} ^ {+} - I _ {m} ^ {-}} + 0. 5 \cdot \frac {I _ {n} ^ {+} - I _ {n} ^ {-}}{I _ {m} ^ {+} - I _ {m} ^ {-}}, & I _ {m} ^ {-} \leq I _ {n} ^ {-} <   I _ {n} ^ {+} \leq I _ {m} ^ {+} \\ \frac {I _ {m} ^ {-} - I _ {n} ^ {-}}{I _ {n} ^ {+} - I _ {n} ^ {-}} + 0. 5 \cdot \frac {I _ {m} ^ {+} - I _ {m} ^ {-}}{I _ {n} ^ {+} - I _ {n} ^ {-}}, & I _ {n} ^ {-} \leq I _ {m} ^ {-} <   I _ {m} ^ {+} \leq I _ {n} ^ {+} \\ 0, & I _ {n} ^ {-} \geq I _ {m} ^ {+} \end{array} \right. \end{array}\tag{2}
$$

From Eq. $( 1 ) _ { : }$ , there are three possible correlations between $I _ { m }$ and $I _ { n } \colon$ 1) I<sup>−</sup> <I<sup>+</sup>≤I<sup>−</sup> <I<sup>+</sup>; 2) $I _ { n } { = } I _ { m } { < } I _ { m } ^ { + } { = } I _ { n } ^ { + } ;$ ; and 3) $I _ { m } ^ { - } { < } I _ { m } ^ { + } { \leq } I _ { n } ^ { - } { < } I _ { n } ^ { + }$ . Accordingly, Eq. (2) can be transformed into:

$$
p (I _ {m} > I _ {n}) = \left\{ \begin{array}{l l} 1, & \quad I _ {n} ^ {-} <   I _ {n} ^ {+} \leq I _ {m} ^ {-} \leq I _ {m} ^ {+} \\ 0. 5, & \quad I _ {n} ^ {-} = I _ {m} ^ {-} <   I _ {m} ^ {+} = I _ {n} ^ {+} \\ 0, & \quad I _ {m} ^ {-} <   I _ {m} ^ {+} \leq I _ {n} ^ {-} <   I _ {n} ^ {+} \end{array} \right.
$$

Proposition 2. Given a list of intervals $\left\{ I _ { n } , n = 1 , . . . , N \right\}$ } that satisfy $\mathtt { E q } .$ (1), suppose ${ \cal { I } } _ { n }$ is the average of $I _ { n } .$ . Then, it follows that.

$$
\begin{array}{l} \text {(1)} p (I _ {m} > I _ {n}) = 1 \text {   iff   } I _ {m} ^ {-} > I _ {n} ^ {-}; \\ \text {(2)} p (I _ {m} > I _ {n}) = 0. 5 \text {   iff   } I _ {m} ^ {-} = I _ {n} ^ {-}; \text {   and } \\ \text {(3)} p (I _ {m} > I _ {n}) = 0 \text {   iff   } I _ {m} ^ {-} <   I _ {n} ^ {-}. \end{array}
$$

The proof of Proposition 2 can be easily obtained. From Proposition $^ { 2 , }$ it can be deduced that the difference in size between $I _ { m }$ and $I _ { n }$ is consistent with that between $I _ { m }$ and ${ \cal { I } } _ { n } ^ { - }$ .

From Propositions 1 and $^ { 2 , }$ it is reasonable to transform $U _ { s }$ and $\scriptstyle { U _ { t } }$ into $\overline { { U } } _ { s }$ and $\overline { { U } } _ { t } ,$ , respectively.

## 4.2. Step 2: Aligning the symptom spaces

Once the patient-symptom matrix is normalized, the patientcategory matrices in the two domains, $\pmb { R _ { s } }$ and $\scriptstyle { R _ { t } }$ can be factorized. However, first, a symptom matrix for a single domain must be defined to demonstrate the relation between symptoms.

Definition 1 (symptom matrix) Given the medical diagnosis problem presented in Section $^ { 3 , }$ the symptom matrix $\pmb { { \cal D } } = ( d _ { i j } ) _ { L \times L }$ is defined to represent the degree of influence of symptom $S _ { i }$ on the disease risks of symptom $S _ { j } ,$ resulting in the diagnostic categories, where $d _ { i j }$ satisfies $d _ { i j } \in [ 0 , 1 ] , d _ { i j } = d _ { j i } ,$ and $\begin{array} { r } { \sum _ { j = 1 } ^ { L } d _ { i j } = 1 } \end{array}$

According to Definition $1 , R _ { s }$ and $\pmb { R } _ { t }$ can be factorized as $\pmb { R _ { s } } = \overline { { U } } _ { s } \pmb { D } _ { s } \pmb { V } _ { s }$ and $R _ { t } = \overline { { U } } _ { t } D _ { t } V _ { t } .$ , respectively, where $D _ { s } { = } ( d _ { i j } ^ { s } ) _ { L s \times L s }$ denotes the symptom matrix in the source domain and $\pmb { D _ { t } } = ( d _ { i j } ^ { t } ) _ { L t \times L t }$ in the target domain. It should be noted that the patient-symptom matrices $\pmb { U _ { s } }$ and $\scriptstyle { U _ { t } , }$ the symptom-category matrices $\pmb { V _ { s } }$ and $\mathbf { } { \mathbf { } } \mathbf { } { \mathbf { } } \mathbf { } v _ { t } ,$ and the patient-category matrices $\pmb { R _ { s } }$ and $\scriptstyle { R _ { t } }$ in the source and target domains can be obtained from medical records. If the medical records in the target domain are insufficient, the symptom relation matrix $D _ { s }$ learned from $\pmb { R _ { s } } = \overline { { U } } _ { s } \pmb { D } _ { s } \pmb { V } _ { s }$ may be impre cise. To obtain more precise $D _ { s } ,$ , sufficient records in the source domain can be used to help learn $D _ { s }$ using the connection of the symptom relation matrices $D _ { s }$ and $\scriptstyle D _ { t } .$ When both symptom spaces in the source and target domains are the same, any or all information in the source domain $D _ { s }$ can be transferred to the target domain $\scriptstyle D _ { t } .$ Otherwise, the symptom spaces in the two domains must be aligned first.

Aligning the symptom spaces involves the process of factorizing the symptom matrix in the source domain $D _ { s }$ into three matrices, $D _ { s } = $ ${ M } _ { 1 } { D } _ { s } ^ { 1 } { M } _ { 2 } ,$ , where $\pmb { M } _ { 1 } = ( m _ { i j } ^ { 1 } ) _ { L s \times L t }$ with $m _ { i j } ^ { 1 } \in [ 0 _ { : }$ , 1] and $\begin{array} { r l r } { \sum _ { j = 1 } ^ { L _ { s } } m _ { i j } ^ { 1 } = 1 , \pmb { M _ { 2 } } = } \end{array}$ $( m _ { i j } ^ { 2 } ) _ { L t \times L s }$ with m<sub>i</sub><sup>2</sup> $\in [ 0 ,$ , 1] and $\begin{array} { r } { \sum _ { j = 1 } ^ { L _ { s } } m _ { i j } ^ { 2 } = 1 } \end{array}$ are the two transformation matrices, and $\boldsymbol { D } _ { s } ^ { 1 } \big ( \boldsymbol { d } _ { i j } ^ { s 1 } ) _ { L t \times L t }$ is the new symptom matrix. Matrices $D _ { s } ^ { 1 }$ and $D _ { t }$ share the same symptom space. Thus, matrix $\pmb { R _ { s } }$ is factorized into five matrices, $. . . , R _ { s } = \overline { { U } } _ { s } M _ { 1 } D _ { s } ^ { 1 } M _ { 2 } V _ { s }$

## 4.3. Step 3: Calculating the dissimilarity for symptom relation matrix extraction

Information cannot be transferred from the source domain to the target domain without knowing the dissimilarity between $\pmb { R _ { s } }$ and $\widehat { \pmb R } _ { s }$ and that between $\pmb { R } _ { t }$ and $\widehat { \pmb R } _ { t }$ . To obtain the dissimilarities, the disease risks indicated in the diagnostic categories must be considered. For a list of diagnostic categories $C = \{ C _ { 1 } , . . . , C _ { N } \}$ , we denote their risk intervals as $\{ p ( C _ { n } ) , n { = } 1 , . . . , N \} = \{ [ p ^ { - } ( C _ { 1 } ) , p ^ { + } ( C _ { 1 } ) ] , ( p ^ { - } ( C _ { 2 } ) , p ^ { + } ( C _ { 2 } ) ] , . . . , ( p ^ { - } ( C _ { N } )$ , $p ^ { + } ( C _ { N } ) ] \} \mathrm { s u c h t h a t } p ^ { - } ( C _ { 1 } ) = 0 , p ^ { + } ( C _ { N } ) = 1 , 0 \leq p ^ { - } ( C _ { n } ) < p ^ { + } ( C _ { n } ) \leq 1 , n = 1 , . . . ,$ $N , p ^ { + } ( C _ { n } ) { = } p ^ { - } ( C _ { n + 1 } ) , n = 1 , . . . , N { - } 1$ , and $\cup _ { n = 1 } ^ { N } p ( C _ { n } ) = \left[ 0 , \right.$ 1]. Following Propositions 1 and $2 , p ( C _ { n } ) , n = 1 , . . . , N$ can be transformed into their averages, $\begin{array} { r } { \overline { { p } } ( C _ { n } ) = \frac { p ^ { - } ( C _ { n } ) + p ^ { + } ( C _ { n } ) } { 2 } ; } \end{array}$ , and $n = 1 , . . . , N ;$ accordingly, a new dissimilarity measurement is constructed that describes the dissimilarity between R and its prediction ${ \widehat { R } } ,$ which is formally defined as follows.

Definition 2 (dissimilarity of diagnoses with risk intervals) Suppose tha ${ \bf \nabla } [ p ( C _ { n } ) ]$ , where $\pmb { n } = 1 , . . . , N$ denotes the risk intervals of the diagnostic categories $C _ { n } , n = 1 , . . . , N .$ . A dissimilarity measurement between a diagnostic matrix $\pmb { R } { = } ( r _ { m n } ) _ { M \times N }$ and its predicted matrix $\widehat { \pmb { R } } = \left( \widehat { r } _ { m n } \right) _ { M \times N } .$ is defined as.

$$
\begin{array}{l} d (\boldsymbol {R}, \widehat {\boldsymbol {R}}) = \\ \frac {\sum_ {m = 1} ^ {M} \sqrt {\sum_ {l = 1} ^ {N - 1} \sum_ {k = l + 1} ^ {N} \left(r _ {m l} - \widehat {r} _ {m l}\right) ^ {2} \cdot \left(r _ {m k} - \widehat {r} _ {m k}\right) ^ {2} \cdot (\overline {{p}} (C _ {k}) - \overline {{p}} (C _ {l})) ^ {2}}}{M \cdot (\overline {{p}} (C _ {N}) - \overline {{p}} (C _ {1}))}, \end{array}\tag{3}
$$

where ${ \overline { { p } } } ( C _ { n } )$ denotes the average of $p ( C _ { n } )$

The dissimilarity measurement between R and $\widehat { R }$ constructed in Definition 2 is distinct from other distance measures, such as the Euclidean distance [38], Manhattan distance [39], or Chebyshev dis tance [40], because it considers $\overline { { { p } } } ( C _ { n } ) ( n { = } 1 , . . . , N )$ such that $0 < \overline { { { p } } } ( C _ { 1 } ) < \overline { { { p } } } ( C _ { 2 } ) < . . . < \overline { { { p } } } ( C _ { N } ) \leq 1$ . Hence, using $\overline { { p } } ( C _ { k } ) - \overline { { p } } ( C _ { l } ) ( l = 1 , . . . , N , h$ k $= l { + } 1 , . . . , N )$ distinguishes the dissimilarities between $( r _ { m l } , r _ { m k } )$ and $( \widehat { \boldsymbol { r } } _ { m l } ,$ $\widehat { r } _ { m k } )$ . The following example can help in explaining the construction of this dissimilarity measurement.

Example 2. Suppose that there are five diagnostic categories, $C _ { n } , n =$ $1 , . . . , 5 ,$ in a medical diagnosis problem. Given the risk intervals defined in the diagnostic categories $\{ p ( C _ { n } ) , n = 1 , . . . , 5 \} = \{ [ 0 , 0 . 0 3 ] , ( 0 . 0 3 ,$ $0 . 2 5 ] , ( 0 . 2 5 , 0 . 7 5 ] , ( 0 . 7 5 , 0 . 9 5 ] , ( 0 . 9 5 , 1 ] \}$ }, assume that R = (1 0 0 0 0) and the two predictions are $\widehat { \mathbf { R } } _ { 1 } = \left( 0 1 0 0 0 \right)$ and $\widehat { R } _ { 2 } = ( 0 0 0 0 1 )$

The averages of {p(C ), n = 1, …, 5} are $\{ \overline { { { p } } } ( C _ { n } ) , n = 1 , . . . , 5 \} =$ {0.015, 0.14, 0.5, 0.85, 0.975}. From Eq. $( 3 ) , d ( R , \widehat { R } _ { 1 } )$ ) and $d ( R , \widehat { R } _ { 2 } )$ are calculated as.

$$
d \left(\boldsymbol {R}, \widehat {\boldsymbol {R}} _ {1}\right) =
$$

$$
\frac {\sum_ {m = 1} ^ {1} \sqrt {\sum_ {l = 1} ^ {4} \sum_ {k = l + 1} ^ {5} \left(r _ {m l} - \widehat {r} _ {m l} ^ {1}\right) ^ {2} \cdot \left(r _ {m k} - \widehat {r} _ {m k} ^ {1}\right) ^ {2} \cdot (\overline {{p}} (C _ {k}) - \overline {{p}} (C _ {l})) ^ {2}}}{(\overline {{p}} (C _ {5}) - \overline {{p}} (C _ {1}))}
$$

$$
= 0. 3 9 7 \text {   and   } d (\boldsymbol {R}, \widehat {\boldsymbol {R}} _ {2}) =
$$

$$
\frac {\sum_ {m = 1} ^ {1} \sqrt {\sum_ {l = 1} ^ {4} \sum_ {k = l + 1} ^ {5} \left(r _ {m l} - \widehat {r} _ {m l} ^ {2}\right) ^ {2} \cdot \left(r _ {m k} - \widehat {r} _ {m k} ^ {2}\right) ^ {2} \cdot (\overline {{p}} (C _ {k}) - \overline {{p}} (C _ {l})) ^ {2}}}{(\overline {{p}} (C _ {5}) - \overline {{p}} (C _ {1}))} = 1.
$$

To ascertain whether our dissimilarity measurement $\left( \operatorname { E q } . \left( 3 \right) \right)$ is more reasonable than the Euclidean, Manhattan, or Chebyshev distance, we compared all three distances between R and $\widehat { \pmb R } _ { 1 } \mathrm { o r } \widehat { \pmb R } _ { 2 }$ . Each distance was calculated as follows:

Euclidean distance: d (R, ${ \widehat { R } } _ { 1 } ) = { \sqrt { 2 } }$ and $d _ { E } ( R , \widehat { R } _ { 2 } ) = \sqrt { 2 } ;$

Manhattan distance: $d _ { M } ( R , \widehat { R } _ { 1 } ) = 2$ and $d _ { M } ( R , \widehat { R } _ { 2 } ) = 2 ;$ and.

Chebyshev distance: $d _ { C } ( R , \widehat { R } _ { 1 } ) = 1$ and $d _ { C } ( R , \widehat { R } _ { 2 } ) = 1$

Thus, we conclude that $d _ { E } ( { \pmb R } , \widehat { \pmb R } _ { 1 } ) = d _ { E } ( { \pmb R } , \widehat { \pmb R } _ { 2 } ) , d _ { M } ( { \pmb R } , \widehat { \pmb R } _ { 1 } ) = d _ { M } ( { \pmb R } , \widehat { \pmb R } _ { 2 } ) ,$ and $d _ { C } ( R , \widehat { R } _ { 1 } ) = d _ { C } ( R , \widehat { R } _ { 2 } )$ . Because $0 < \overline { { p } } ( C _ { 1 } ) < \overline { { p } } ( C _ { 2 } ) < \ldots < \overline { { p } } ( C _ { 5 } ) < 1 , \widehat { R } _ { 1 }$ is closer to $\pmb R$ than ${ \widehat { R } } _ { 2 } ,$ which supports the use of our dissimilarity measurement.

The properties of the dissimilarity measurement between R and $\widehat { R }$ are summarized below.

Property 1. Suppose that $d ( R , { \widehat { R } } )$ represents the dissimilarity between two matrices $\pmb { R } { = } ( r _ { m n } ) _ { M \times N }$ and $\widehat { \pmb { R } } \mathrm { = } \left( \widehat { \pmb { r } } _ { m n } \right) _ { M \mathrm { \times } N }$ provided in Definition 2. Then, it follows that.

$$
0 \leq d (\boldsymbol {R}, \widehat {\boldsymbol {R}}) \leq 1\tag{4}
$$

$$
d \Big (\boldsymbol {R}, \widehat {\boldsymbol {R}} \Big) = d \Big (\widehat {\boldsymbol {R}}, \boldsymbol {R} \Big)\tag{5}
$$

$$
d (\boldsymbol {R}, \widehat {\boldsymbol {R}}) = 0 \text {   iff   } \boldsymbol {R} = \widehat {\boldsymbol {R}}\tag{6}
$$

$$
d \left(\boldsymbol {R}, \widehat {\boldsymbol {R}}\right) = 1 \text {   iff   } r _ {m 1} = 1 \text {   and   } \widehat {r} _ {m N} = 1 \text {   or   } r _ {m N} = 1 \text {   and   } \widehat {r} _ {m 1} = 1, m = 1,..., M.\tag{7}
$$

The proof of Property 1 is given in Appendix A. Using the dissimi larity measurement shown in $\operatorname { E q } . \ ( 3 )$ , the dissimilarity between $\pmb { R _ { s } }$ and $\widehat { \pmb R } _ { s }$ and that between $\scriptstyle { R _ { t } }$ and $\widehat { \pmb R } _ { t }$ can be obtained by $d ( R _ { s } , \widehat { R } _ { s } )$ ) and $d ( R _ { t }$ $\widehat { R } _ { t } )$ , respectively.

4.4. Step 4: Transferring information through constraints on the symptom matrix

The process of transferring information differs depending on whether the symptom spaces in the source and target domains are the same. We first consider the more challenging of the two cases, where the symptom spaces are different.

As discussed in Step 2, when the symptom spaces are different, the patient-category matrices $\pmb { R _ { s } }$ and $\scriptstyle { R _ { t } }$ must be factorized into $\pmb { R _ { s } } =$ $\overline { { U } } _ { s } M _ { 1 } D _ { s } ^ { 1 } M _ { 2 } V _ { s }$ and $R _ { \mathrm { t } } = \overline { { U } } _ { t } D _ { t } V _ { t } ,$ , respectively, and the symptom relation matrices $D _ { s } ^ { 1 }$ and $\scriptstyle { D _ { t } }$ share one symptom space. To further characterize the symptom space, we introduce the definition of the condition number of a matrix with the Frobenius norm, which describes the influence of the input variations in a matrix function on the output variations.

Definition 3 (condition number of matrix) [41] Given matrix A $= ( a _ { i j } ) _ { L 1 \times L 2 } , L _ { 1 } , L _ { 2 } { \in } \mathbb { N } ^ { + }$ , the condition number of A with the Frobenius norm is defined as $c o n d ( { \pmb A } ) = \| { \pmb A } \| _ { F } \cdot \| { \pmb A } ^ { + } \| _ { F } ,$ , where $\begin{array} { r } { \| \pmb { A } \| _ { F } { = } \sqrt { \sum _ { i = 1 } ^ { L _ { 1 } } \sum _ { j = 1 } ^ { L _ { 2 } } { a _ { i j } } ^ { 2 } } } \end{array}$ and $A ^ { + }$ is the generalized inverse matrix of A.

It is evident that cond(A) ≥ 1. The condition numbers of $\scriptstyle { D _ { t } }$ and $D _ { s } ^ { 1 }$ are denoted by cond(D ) and cond(D<sup>1</sup>), respectively. Now, we must analyze the influence of cond $\mathbf { \delta D _ { t } } )$ on the matrix factorization of $R _ { t } = \overline { { U } } _ { t } D _ { t } V _ { t }$ and that of cond(D<sup>1</sup>) on $R _ { s } = \overline { { U } } _ { s } M _ { I } D _ { s } ^ { I } M _ { 2 } V _ { s }$ . The influence of cond(D ) on the sensitivity of the relative error of $\pmb { R } _ { t }$ to that of $\overline { { U } } _ { t }$ or $\pmb { V _ { t } }$ in the target domain is demonstrated below.

Theorem 1. If $R _ { t } = \overline { { U } } _ { t } D _ { t } V _ { t } ,$ the following two conclusions are satisfied.

(1) If $\Delta \overline { { U } } _ { t }$ and $\Delta R _ { t }$ satisfy $R _ { t } + \Delta R _ { t } = \bigg ( \overline { { U } } _ { t } + \Delta \overline { { U } } _ { t } \bigg ) D _ { t } V _ { t } ,$ , then

$$
\frac {1}{\operatorname{cond} \left(\boldsymbol {D} _ {t}\right) \cdot \operatorname{cond} \left(\boldsymbol {V} _ {t}\right)} \cdot \frac {\left\| \Delta \overline {{\boldsymbol {U}}} _ {t} \right\| _ {F}}{\left\| \overline {{\boldsymbol {U}}} _ {t} \right\| _ {F}} \leq \frac {\left\| \Delta \boldsymbol {R} _ {t} \right\| _ {F}}{\left\| \boldsymbol {R} _ {t} \right\| _ {F}} \leq \operatorname{cond} \left(\boldsymbol {D} _ {t}\right) \cdot \operatorname{cond} \left(\boldsymbol {V} _ {t}\right) \cdot \frac {\left\| \Delta \overline {{\boldsymbol {U}}} _ {t} \right\| _ {F}}{\left\| \overline {{\boldsymbol {U}}} _ {t} \right\| _ {F}},\tag{8}
$$

where $\frac { \| \varDelta R _ { t } \| _ { F } } { \| R _ { t } \| _ { F } }$ and $\frac { \left\| \Delta \overline { { U } } _ { t } \right\| _ { F } } { \left\| \overline { { U } } _ { t } \right\| _ { F } }$ represent the relative error of $\scriptstyle { R _ { t } }$ and $\overline { { U } } _ { t ; }$ , respectively.

(2) If $\Delta { V } _ { t }$ and $\Delta R _ { t }$ satisfy $R _ { t } + \varDelta R _ { t } = \overline { { U } } _ { t } D _ { t } ( V _ { t } + \Delta V _ { t } ) .$ , then

$$
\frac {1}{c o n d (\boldsymbol {D} _ {t}) \cdot c o n d \left(\overline {{\boldsymbol {U}}} _ {t}\right)} \cdot \frac {\| \Delta \boldsymbol {V} _ {t} \| _ {F}}{\| \boldsymbol {V} _ {t} \| _ {F}} \leq \frac {\| \Delta \boldsymbol {R} _ {t} \| _ {F}}{\| \boldsymbol {R} _ {\mathbf {t}} \| _ {F}} \leq c o n d (\boldsymbol {D} _ {t}) \cdot c o n d \left(\overline {{\boldsymbol {U}}} _ {t}\right) \cdot \frac {\| \Delta \boldsymbol {V} _ {t} \| _ {F}}{\| \boldsymbol {V} _ {t} \| _ {F}},\tag{9}
$$

where ${ \widehat { \pmb { R } } } _ { s } = \left( { \widehat { \pmb { r } } } _ { m n } ^ { s } \right) _ { M _ { s } \times N _ { \epsilon } } = { \overline { { U } } } _ { s } M _ { 1 } { \cal D } _ { s } ^ { I } M _ { 2 } V _ { s } , \widehat { \pmb { R } } _ { t } = \left( { \widehat { \pmb { r } } } _ { m n } ^ { t } \right) _ { M , \times N _ { t } } = { \overline { { U } } } _ { t } D _ { t } V _ { t } , \overline { { U } } _ { s }$ and $\overline { { U } } _ { t }$ are the average matrices of $\pmb { U _ { s } }$ and $\pmb { U } _ { t s }$ respectively, and λ is a parameter such that $0 \leq \lambda \leq 1$ . Based on Eq. $( 1 0 ) , D _ { s } ^ { 1 } , D _ { t } , M _ { 1 } ,$ , and $\pmb { M _ { 2 } }$ are learned by the following optimization problem:

min J.

$$
\text { s.t. } \operatorname{cond} (D _ {s} ^ {1}) = \operatorname{cond} (\boldsymbol {D} _ {t}).
$$

$$
\mathbf {0} \leq D _ {s} ^ {I},   D _ {t} \leq \mathbf {1},   D _ {s} ^ {\mathbf {1}} = \left(D _ {s} ^ {\mathbf {1}}\right) ^ {\mathrm{T}},   D _ {t} = D _ {\mathbf {t}} ^ {\mathrm{T}},   \sum_ {j = 1} ^ {L _ {s}} \left(\mathbf {D} _ {\mathbf {s}} ^ {\mathbf {1}}\right) _ {j} = \mathbf {1},   \sum_ {j = 1} ^ {L _ {t}} (\mathbf {D} _ {\mathbf {t}}) _ {j} = \mathbf {1},
$$

$$
\mathbf {0} \leq M _ {1}, M _ {2} \leq \mathbf {1}, \sum_ {j = 1} ^ {L _ {t}} (M _ {1}) _ {j} = \mathbf {1}, \sum_ {j = 1} ^ {L _ {t}} (\mathbf {M} _ {2}) _ {j} = \mathbf {1},
$$

where $( D _ { s } ^ { 1 } ) _ { j } , ( M _ { 1 } ) _ { j }$ , and $( M _ { 2 } ) _ { j }$ denote each column of $D _ { s } ^ { 1 } , { \pmb M } _ { 1 ; }$ , and $M _ { 2 } ,$ respectively.

This is a sequential quadratic programming problem [42] that can be solved by several existing solvers. The information transfer between the source and target domains is summarized in Algorithm 1.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 1: Information transfer

Input:  $R_{s}$ ,  $U_{s}$ ,  $V_{s}$ , patient-category matrix, patient-symptom matrix, and symptom-category matrix of source domain
 $R_{t}$ ,  $U_{t}$ ,  $V_{t}$ , patient-category matrix, patient-symptom matrix, and symptom-category matrix of target domain

Output:  $D_{s}^{1}$ , aligned symptom matrix of source domain
 $D_{t}$ , symptom matrix of target domain
 $M_{1}$ ,  $M_{2}$ , transformation matrices for symptom space alignment

1 INITIALIZE  $D_{s}^{1}$ ,  $D_{t} \in i^{L_{t} \times L_{t}}$ ,  $M_{1} \in i^{L_{s} \times L_{t}}$ ,  $M_{2} \in i^{L_{t} \times L_{s}}$ ,  $J_{min} \leftarrow 0$ ,  $J \leftarrow 0$ 

2 WHILE J = 0 OR  $J - J_{min} &gt; \varepsilon$  DO

3 FOR  $D_{s}^{1}$ ,  $D_{t}$ ,  $M_{1}$ ,  $M_{2}$  in each iteration

4 UPDATE  $D_{s}^{1}$ ,  $D_{t}$ ,  $M_{1}$ ,  $M_{2}$  using the sequential quadratic programming method

5 ENDFOR

6 UPDATE J as in Eq. (10)

7 IF  $J_{min} &gt; J$ 

8  $J_{min} = J$ 

9 ENDIF

10 ENDWHILE

11 RETURN  $D_{s}^{1}$ ,  $D_{t}$ ,  $M_{1}$ ,  $M_{2}$
</div>

where $\frac { \lVert \varDelta R _ { t } \rVert _ { F } } { \lVert R _ { t } \rVert _ { F } }$ and $\frac { \| \Delta V _ { t } \| _ { F } } { \| V _ { t } \| _ { F } }$ represent the relative error of $\scriptstyle { R _ { t } }$ and $\mathbf { } \mathbf { } \mathbf { } V _ { t s }$ respec tively. The proof of Theorem 1 is given in Appendix B. From Eqs. (8) and $( 9 ) ,$ we can conclude that the smaller the value of cond(D ), the narrower the range of the relative error of $\scriptstyle R _ { t } ,$ which indicates that the relative error of $\scriptstyle { R _ { t } }$ is more controllable. In the source domain, the in fluence of $c o n d ( D _ { s } ^ { 1 } )$ on the sensitivity of the relative error of $\pmb { R _ { s } }$ to that of $\overline { { U } } _ { s } M _ { 1 }$ or ${ \pmb { M } } _ { 2 } { \pmb { V } } _ { s }$ can similarly be deduced from Theorem 1. When $D _ { s } ^ { 1 }$ and $\scriptstyle { D _ { t } }$ share the same symptom space, we have $c o n d ( D _ { s } ^ { 1 } ) = c o n d ( D _ { t } ) . D _ { s } ^ { 1 } , D _ { t } ,$ $M _ { 1 } ,$ , and ${ \pmb M } _ { 2 }$ can be learned by minimizing $d ( R _ { s } , \overline { { U } } _ { s } M _ { 1 } D _ { s } ^ { I } M _ { 2 } V _ { s } )$ and d $\scriptstyle \mathbf { R } _ { t _ { s } }$ $\overline { { U } } _ { t } \mathbf { D } _ { t } V _ { t } )$ . Minimizing the difference between $D _ { s } ^ { 1 }$ and $\scriptstyle { D _ { t } }$ also needs to be considered. Thus. the cost function is constructed as follows:

$$
J = d \left(\boldsymbol {R} _ {s}, \widehat {\boldsymbol {R}} _ {s}\right) + d \left(\boldsymbol {R} _ {t}, \widehat {\boldsymbol {R}} _ {t}\right) + \frac {\lambda}{2 L ^ {2}} \cdot \sqrt {\sum_ {i = 1} ^ {L _ {t}} \sum_ {j = 1} ^ {L _ {t}} \left(d _ {i j} ^ {t} - d _ {i j} ^ {s 1}\right) ^ {2}}\tag{10}
$$

The ITMD method can also be used to support medical diagnosis with the same symptom spaces. In this situation, suppose that $\pmb { D } _ { s } \mathrm { = } ( d _ { i j } ^ { s } ) _ { L \times I }$ and $\pmb { D } _ { t } = ( d _ { i j } ^ { t } ) _ { L \times L }$ . Because $D _ { s }$ and $\scriptstyle { D _ { t } }$ are aligned, $\pmb { R _ { s } }$ is factorized as $\pmb { R _ { s } } ~ =$ $\overline { { U } } _ { s } D _ { s } V _ { s } ;$ that is, ${ \pmb M } _ { 1 }$ and $\pmb { M _ { 2 } }$ are not required. Because the optimization problem of solving $D _ { s }$ and $\scriptstyle { D _ { t } }$ is similar to Eq. (10), the details are omitted.

## 4.5. Step 5: Generating recommendations in the target domain

Diagnostic support in the target domain is generated by $\widehat { \pmb { R } } _ { t } = \overline { { \pmb { U } } } _ { t } \pmb { D } _ { t } \pmb { V } _ { t } ,$ where $\widehat { \pmb R } _ { t }$ is the predicted diagnostic category of patients; $\overline { { U } } _ { t }$ is the average matrix of $\scriptstyle { U _ { t } , }$ which denotes the relations between the patients and symptoms; $\mathbf { } _ { \mathbf { } } \mathbf { v } _ { t }$ represents the relations between the symptoms and diagnostic categories; and $\scriptstyle { D _ { t } }$ is the symptom matrix in the target domain. The highest prediction of diagnosis is the recommendation for physicians.

The ITMD method is presented in Algorithm 2.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 2: ITMD method
Input: $R_s$, $U_s$, $V_s$, patient-category matrix, patient-symptom matrix, and symptom-category matrix of source domain
$R_t$, $U_t$, $V_t$, patient-category matrix, patient-symptom matrix, and symptom-category matrix of target domain
Output: $C_m$, recommendation of target domain for patient $p_m$
1 Normalize $U_s$ and $U_t$ with $\bar{U}_s$ and $\bar{U}_t$
2 IF $L_s = L_t$
3 INITIALIZE $D_s \in i^{L_s \times L_s}$, $D_t \in i^{L_t \times L_t}$
4 $\hat{R}_s \leftarrow \bar{U}_s D_s V_s$
5 $\hat{R}_t \leftarrow \bar{U}_t D_t V_t$
6 CALCULATE $d(R_s, \hat{R}_s)$ and $d(R_t, \hat{R}_t)$ as in Eq. (3)
7 CALCULATE $J$ as in Eq. (10) with $\hat{R}_s = \bar{U}_s D_s V_s$
8 LEARN $D_s, D_t$ using the sequential quadratic programming method
9 ELSE IF
10 INITIALIZE $D_s^1, D_t \in i^{L_t \times L_t}$, $M_1 \in i^{L_s \times L_t}$, $M_2 \in i^{L_t \times L_s}$
11 $\hat{R}_s \leftarrow \bar{U}_s M_1 D_s^1 M_2 V_s$
12 $\hat{R}_t \leftarrow \bar{U}_t D_t V_t$
13 LEARN $D_s^1, D_t, M_1, M_2$ using Algorithm 1
14 ENDIF
15 $\hat{R}_t \leftarrow \bar{U}_t D_t V_t$
16 RETURN $C_m$ for patient $p_m$ using $C_m = \max_{i=1,\ldots,N_t} \left\{ \hat{r}_{mn}^t \right\}$
</div>

without loss of generality, the two probability distributions are assumed to be $( p ( u _ { m l } ^ { s } = L ( S _ { 1 } ) ) , . . . , p ( u _ { m l } ^ { s } = L ( S _ { 5 } ) ) = ( 0 . 3 , 0 . 2 , 0 . 3 , 0 . 1 , 0 . 1 )$ and (p $( u _ { m l } ^ { t } { = } L ( S _ { 1 } ) ) , ~ . . . , p ( u _ { m l } ^ { t } { = } L ( S _ { 5 } ) ) = ( 0 . 4 , 0 . 1 , 0 . 1 , 0 . 2 , 0 . 2 ) .$ . Based on the

## 5. Experiments and analyses

Owing to the privacy and inaccessibility of diagnostic data for most diseases, it is necessary to generate synthetic data to investigate the effectiveness of the ITMD method. The generation of synthetic data should adequately reflect the characteristics of medical diagnosis at the risk intervals. We conducted two sets of experiments where the symptom spaces were either the same in the two domains or different. First, we explain the process of generating synthetic data, followed by the eval uation metrics and the baselines for comparison. Finally, the results are presented.

## 5.1. Synthetic datasets

To ensure that the synthetic data can reflect the structure of real medical records, they are generated based on the essential information for disease diagnosis. They include a set of patients $P = \{ P _ { 1 } , . . . , P _ { M } \}$ , a set of symptoms $S = \{ S _ { 1 } , . . . , S _ { L } \}$ , a set of diagnostic categories $C = \{ C _ { 1 } , . . . ,$ $C _ { N } \}$ with risk intervals $p ( C _ { n } ) \ ( n { = } 1 , . . . , N )$ , and the levels of severity of symptoms $L ( S _ { l } ) ( l = 1 , . . . , L ) .$

For the first group of experiments, thyroid cancer and breast cancer were considered as the source and target domains, respectively. Both domains contain five symptoms, $\mathrm { i . e . , } S _ { s }mathrm { = } S _ { t } = \{ S _ { 1 } , . . . , S _ { 5 } \} = \{ \mathrm { m a r g i n } ,$ contour, echogenicity, calcification, vascularity}, and five diagnostic categories denoted by $C _ { s } { = } C _ { t } { = } \left\{ C _ { 1 } , . . . , C _ { 5 } \right\} \left[ 4 3 \right]$ . The risk intervals of the diagnostic categories and the levels of severity of symptoms in the two domains are $\{ p ( C _ { n } ) , n = 1 , . . . , 5 \} = \{ L ( S _ { l } ) , l = 1 , . . . , 5 \} = \{ [ 0 , 0 . 0 3 ] , ( 0 . 0 3 _ { l }$ 0.25], (0.25, 0.75], (0.75, 0.95], (0.95, 1]} [44]. Suppose that the di agnoses of patients on the symptoms in the two domains $U _ { s = ( } u _ { m l } ^ { s } ) _ { M s \times L s }$ and ${ \pmb U } _ { t = } ( { \boldsymbol u } _ { m l } ^ { t } ) _ { M t \times L t }$ follow two different probability distributions, and essential information and possibility distributions in the two domains, 40,000 and 10,000 diagnostic records (patient-symptom ratings) were generated for the two domains, respectively. The parameter λ was set to 0.5. The number of records with the same symptom space in this group of experiments is listed in Table 5.

For the second group of experiments, gastric cancer and liver cancer were considered as the source and target domains, respectively. The diagnosis of gastric cancer involves six symptoms, $S _ { s } = \{ S _ { 1 } ^ { s } , . . . , S _ { 6 } ^ { s } \} =$ {margin, contour, echogenicity, depth, lymph node metastases, size} [45], and eight diagnostic categories denoted by $C s = \{ C _ { 1 } ^ { s } , . . . , C _ { 8 } ^ { s } \}$ . The diagnosis of liver cancer includes five symptoms, ${ \cal S } _ { t } = \{ { \cal S } _ { 1 } ^ { t } , ~ . . . , { \cal S } _ { 5 } ^ { t } \} =$ {margin, echogenicity, contour, vascularity, size} [46], and five diag nostic categories denoted by $C t = \{ C _ { 1 } ^ { t } , . . . , C _ { 5 } ^ { t } \}$ . The TNM system of the American Joint Committee on Cancer/International Union Against Cancer Classification (AJCC/UICC) is used to represent the risk intervals of the diagnostic categories and the severity of symptoms in the diag nosis of gastric cancer; that is, $\{ p ( C _ { n } ^ { s } ) , n { = } 1 , . . . , 8 \} = \{ L ( S _ { l } ^ { s } ) , l { = } 1 , . . . , 8 \} =$ {[0, 0.261], (0.261, 0.413], (0.413, 0.584], (0.584, 0.717], (0.717, 0.84], (0.84, 0.884], (0.884, 0.951], (0.951, 1]} [47]. Correspondingly, the risk intervals of the diagnostic categories and the levels of severity of symptoms in the diagnosis of liver cancer are described by the risk stages of laparoscopic ultrasonography in the evaluation of liver nodules, which are $\{ p ( C _ { n } ^ { t } ) , n = 1 , . . . , 5 \} = \{ L ( S _ { l } ^ { t } ) , l = 1 , . . . , 5 \} = \{ [ 0 , 0 . 1 8 ] , ( 0 . 1 8 _ { l } ^ { t } )$ 0.24], (0.24, 0.3], (0.3, 0.84], (0.84, 0.1]} [48]. Suppose that $\pmb { U _ { s = } } ( u _ { m l } ^ { s } ) _ { M s \times L s }$ and ${ \pmb U } _ { t = } ( { \boldsymbol u } _ { m l } ^ { t } ) _ { M t \times L t }$ follow two different probability distri butions, and without loss of generality, they were assumed to be (p $( u _ { m l } ^ { s } \mathrm { - } L ( S _ { 1 } ^ { s } ) ) , ~ . . . , p ( u _ { m l } ^ { s } \mathrm { - } L ( S _ { 8 } ^ { s } ) ) = ( 0 . 1 , 0 . 1 5 , 0 . 1 , 0 . 1 , 0 . 1 5 , 0 . 1 , 0 . 1 , 0 . 2 )$ and $( p ( u _ { m l } ^ { t } { = } L ( S _ { 1 } ^ { t } ) ) , . . . , p ( u _ { m l } ^ { t } { = } L ( S _ { 5 } ^ { t } ) ) = ( 0 . 4 , 0 . 1 , 0 . 1 , 0 . 2 , 0 . 2 ) . \mathrm { B a s e d }$ on the essential information and distributions in the two domains, 40,000 and 10,000 diagnostic records (patient-symptom ratings) of the two domains were generated. The parameter λ was set to 0.5. The number of records with the same symptom space in this group of experiments is listed in Table 5.

Table 5  
Number of records for five groups of records with same and different symptom spaces.

<table><tr><td rowspan="2">Symptom spaces</td><td rowspan="2">Group ID</td><td colspan="2">1:1</td><td colspan="2">2:1</td><td colspan="2">3:1</td><td colspan="2">4:1</td></tr><tr><td>Source</td><td>Target</td><td>Source</td><td>Target</td><td>Source</td><td>Target</td><td>Source</td><td>Target</td></tr><tr><td rowspan="5">Same</td><td> $G_1$ </td><td>2000</td><td>2000</td><td>4000</td><td>2000</td><td>6000</td><td>2000</td><td>8000</td><td>2000</td></tr><tr><td> $G_2$ </td><td>4000</td><td>4000</td><td>8000</td><td>4000</td><td>12,000</td><td>4000</td><td>16,000</td><td>4000</td></tr><tr><td> $G_3$ </td><td>6000</td><td>6000</td><td>12,000</td><td>6000</td><td>18,000</td><td>6000</td><td>24,000</td><td>6000</td></tr><tr><td> $G_4$ </td><td>8000</td><td>8000</td><td>16,000</td><td>8000</td><td>24,000</td><td>8000</td><td>32,000</td><td>8000</td></tr><tr><td> $G_5$ </td><td>10,000</td><td>10,000</td><td>20,000</td><td>10,000</td><td>30,000</td><td>10,000</td><td>40,000</td><td>10,000</td></tr><tr><td rowspan="5">Different</td><td> $G_6$ </td><td>2000</td><td>2000</td><td>4000</td><td>2000</td><td>6000</td><td>2000</td><td>8000</td><td>2000</td></tr><tr><td> $G_7$ </td><td>4000</td><td>4000</td><td>8000</td><td>4000</td><td>12,000</td><td>4000</td><td>16,000</td><td>4000</td></tr><tr><td> $G_8$ </td><td>6000</td><td>6000</td><td>12,000</td><td>6000</td><td>18,000</td><td>6000</td><td>24,000</td><td>6000</td></tr><tr><td> $G_9$ </td><td>8000</td><td>8000</td><td>16,000</td><td>8000</td><td>24,000</td><td>8000</td><td>32,000</td><td>8000</td></tr><tr><td> $G_{10}$ </td><td>10,000</td><td>10,000</td><td>20,000</td><td>10,000</td><td>30,000</td><td>10,000</td><td>40,000</td><td>10,000</td></tr></table>

In all experiments, the test set was obtained from the target domain; then, we performed five-fold cross-validation to generate the training and test data, as demonstrated in [49,50]. Five-fold cross-validation was applied to the dataset in the target domain, and the entire dataset in the source domain was used for training.

## 5.2. Evaluation metrics and baselines

We selected the prediction accuracy as our evaluation metric, which is calculated as $A R _ { t } = 1 - d ( { \pmb R } _ { | Y | } , \widehat { { \pmb R } } _ { | Y | } ) .$ , where Y is the test set in the target domain, |Y| is the number of test sets, and $\pmb { R } _ { | Y | }$ and $\widehat { R } _ { | Y | }$ represent the true values and predictions of diagnoses in the test set, respectively. The greater the prediction accuracy, the better the performance.

We selected four non-transfer learning methods as the baselines for comparison, named $B _ { 1 } [ 5 1 ] , B _ { 2 } [ 4 4 ] , B _ { 3 } [ 5 2 ]$ , and $B _ { 4 }$ for simplicity. For baselines $B _ { 1 }$ and $B _ { 2 } ,$ , the diagnoses were generated using a linear com bination of the relations between patients and symptoms (denoted by $\begin{array} { r } { u _ { m l } = [ u _ { m l } ^ { - } , u _ { m l } ^ { + } ] , m = 1 , . . . , M , l = 1 , . . . , L } \end{array}$ , where M and L are the number of patients and symptoms, respectively) and the relative weights of symptoms (denoted by $w _ { l } , l = 1 , . . . , L )$ . Thus, the risk intervals for pa tients denoted by $\begin{array} { r } { p _ { m } = { } [ p _ { m } ^ { - } , } \end{array}$ , p<sup>+</sup>] can be predicted by $\widehat { p } _ { m } = \widehat { \sf { p } } _ { m } ^ { - } ,$ $\begin{array} { r } { \widehat { p } _ { m } ^ { + } ] = \sum _ { l = 1 } ^ { L } u _ { m l } \cdot w _ { l } . } \end{array}$ The distances between $p _ { m }$ and $\widehat { p } _ { m }$ in the two baselines were respectively calculated with.

$$
d _ {1} \left(p _ {m}, \widehat {p} _ {m}\right) = \sqrt {\left(\overline {{{{p}}}} _ {m} - \overline {{{{\widehat {\bar {p}}}}}} _ {m}\right) ^ {2} + \frac {1}{1 2} \cdot \left((l (p _ {m})) ^ {2} + \left(l (\widehat {p} _ {m})\right) ^ {2}\right) - \frac {1}{6} \cdot (l (d _ {m})) ^ {2}}
$$

and

$$
d _ {2} \left(p _ {m} \widehat {p} _ {m}\right) = \left| \overline {{{{p}}}} _ {m} \cdot \left(1 - \frac {1}{\sqrt {1 2}} \cdot l (p _ {m})\right) - \overline {{{{\widehat {p}}}}} _ {m} \cdot \left(1 - \frac {1}{\sqrt {1 2}} \cdot l (\widehat {p} _ {m})\right) \right|,
$$

where $\overline { { { p } } } _ { m } = 0 . 5 \cdot \left( p _ { m } ^ { - } + p _ { m } ^ { + } \right) , \ \overline { { { \widehat { p } } } } _ { m } = 0 . 5 \cdot \left( \widehat { p } _ { m } ^ { - } + \widehat { p } _ { m } ^ { + } \right) , \ l ( p _ { m } ) \ = \ p _ { m } ^ { + } \ - \ p _ { m } ^ { - }$ $l \biggl ( \widehat { p } _ { m } \biggr ) = \widehat { p } _ { m } ^ { + } - \widehat { p } _ { m } ^ { - } ;$ , and $l ( d _ { m } ) = \left( p _ { m } \cap \widehat { \cal p } _ { m } \right) ^ { + } - \left( p _ { m } \cap \widehat { \cal p } _ { m } \right) ^ { - }$ . For base line $B _ { 3 } ,$ the relation between patients and symptoms, $u _ { m l s }$ was replaced by their averages $\overline { { u } } _ { m l } ;$ they were subsequently used to generate the diagnostic predictions by linearly combining the relative weights of symptoms $w _ { l } , l = 1 , . . . , L$ . That is, the average risk intervals for patients denoted by $q _ { m } , m { = } 1 , \ldots ,$ M can be predicted by $\begin{array} { r } { \widehat { q } _ { m } = \sum _ { l = 1 } ^ { L } \overline { { u } } _ { m l } { \cdot } w _ { l } . } \end{array}$ . The distance between $q _ { m }$ and $\widehat { \boldsymbol { q } } _ { m }$ was calculated using $d _ { 1 } ( q _ { m } , \widehat { q } _ { m } ) = \left| q _ { m } - \widehat { q } _ { m } \right|$ $B _ { 4 }$ is a non-transfer learning variant of the ITMD method. The prediction model is the matrix factorization of $R = { \overline { { U } } } D V .$ All methods were eval uated using the same test set. The averages and standard deviations of the experimental results from 20 random initializations are reported.

## 5.3. Experimental results

A comparison of the two sets of test results for the five different ratios is presented in Table 5 and Figs. 2 and 3. The experimental results indicate that the ITMD method exhibited the best performance for each group of records. In addition, the performance of the ITMD method improved as the source: target domain data ratio increased from 1:1 to 4:1. These results provide solid support for the effectiveness of knowl edge transfer, both when the symptom spaces are the same and when they are not. The following four highlights can be derived from Tables 6 and 7.

(1) Baseline $B _ { 4 } ,$ the non-transfer learning variant of the ITMD method, performed better than the other three baselines, which did not incorporate knowledge transfer. However, compared with the ITMD method, the performance of the four baselines was poor, indicating that the transfer of shared information from the source domain to the target domain significantly improves the final result.

(2) The standard deviations for $B _ { 1 } , \ B _ { 2 } ,$ and $B _ { 3 }$ were significantly larger than those for $B _ { 4 }$ and the ITMD method, which means that $B _ { 1 } , B _ { 2 } ,$ and $B _ { 3 }$ lost some stability when the target domain had insufficient records, whereas $B _ { 4 }$ and the ITMD method did not.

(3) In the experiments for all five groups of records, the ITMD method exhibited superior performance than the baselines. Further, the larger the ratio of data between the source and target domains, the better the ITMD method performed. The largest improvements in the ITMD method in comparison to the base lines are presented in Table 7. The largest improvements in the prediction accuracy of the ITMD method with the same and different symptom spaces were 0.0973 and 0.0827, respectively.

(4) As the number of records in the target domain increased. the performance of the ITMD method gradually decreased. Table 7 demonstrates that the maximum improvement rate for the ITMD method decreased from 13.43% to 8.15%, with the same symp tom spaces, and from 11.3% to 8.85%, with different symptom spaces as the number of records increased from 2000 to 10,000. This is reasonable because, with more data, the ITMD method does not need to provide as much support.

## 6. Real-world case study

This section presents a case study to demonstrate the operation and performance of the proposed ITMD method in practical situations. Thyroid cancer and breast cancer were considered as the source and target domains, respectively; additionally, real-world datasets of medi cal diagnoses were used for each domain.

Table 6  
![](/api/attachments/B7AZXNG6/fulltext/images/b1a02e6a42013e02d0e34743772765b21d093c826d4747ac82901ccc2346ebae.jpg)  
(a) Same symptom spaces

![](/api/attachments/B7AZXNG6/fulltext/images/304a9f2b308d2c0df8fe8bff3c6692a72b6e997f6cba62c0cd438927094071ab.jpg)  
(b) Different symptom spaces  
Fig. 2. Prediction accuracy of all methods for $G _ { 1 } – G _ { 1 0 }$ with same and different symptom spaces.

![](/api/attachments/B7AZXNG6/fulltext/images/a028abae2448678ef0790e37d9e938de56e79124cf988cbac4e25da3fb562c60.jpg)

![](/api/attachments/B7AZXNG6/fulltext/images/adb3445736f78bb8bb291e32cdea26112684179922aa42d629c51177442ea71f.jpg)  
(b) Different symptom spaces  
Fig. 3. Average prediction accuracy of all methods with same and different symptom spaces.

(a) Same symptom spaces  
Prediction accuracy for five groups of records with same and different symptom spaces.

<table><tr><td rowspan="2">Group ID</td><td rowspan="2"> $B_1$ </td><td rowspan="2"> $B_2$ </td><td rowspan="2"> $B_3$ </td><td rowspan="2"> $B_4$ </td><td colspan="4">ITMD</td></tr><tr><td>1:1</td><td>2:1</td><td>3:1</td><td>4:1</td></tr><tr><td> $G_1$ </td><td>0.7243±0.0215</td><td>0.7361±0.0236</td><td>0.7436±0.0217</td><td>0.7756±0.0108</td><td>0.7926±0.0069</td><td>0.8022±0.0083</td><td>0.8163±0.0113</td><td>0.8216±0.0102</td></tr><tr><td> $G_2$ </td><td>0.7357±0.0233</td><td>0.7457±0.0214</td><td>0.7538±0.0233</td><td>0.7791±0.0096</td><td>0.7873±0.0088</td><td>0.7976±0.0073</td><td>0.8052±0.0082</td><td>0.8231±0.0066</td></tr><tr><td> $G_3$ </td><td>0.7536±0.0218</td><td>0.7413±0.0243</td><td>0.7563±0.0211</td><td>0.7828±0.0045</td><td>0.7996±0.0077</td><td>0.8066±0.0089</td><td>0.8127±0.0061</td><td>0.8202±0.0073</td></tr><tr><td> $G_4$ </td><td>0.7499±0.0238</td><td>0.7468±0.0211</td><td>0.7456±0.0178</td><td>0.7903±0.0079</td><td>0.8044±0.0041</td><td>0.8067±0.0063</td><td>0.8111±0.0046</td><td>0.8179±0.0087</td></tr><tr><td> $G_5$ </td><td>0.7547±0.0213</td><td>0.7501±0.0137</td><td>0.7589±0.0205</td><td>0.8018±0.0063</td><td>0.8041±0.0046</td><td>0.8062±0.0073</td><td>0.8091±0.0059</td><td>0.8112±0.0074</td></tr><tr><td> $G_6$ </td><td>0.7348±0.0176</td><td>0.7401±0.0201</td><td>0.7319±0.0219</td><td>0.7786±0.0043</td><td>0.7952±0.0066</td><td>0.8027±0.0052</td><td>0.8067±0.0069</td><td>0.8146±0.0023</td></tr><tr><td> $G_7$ </td><td>0.7403±0.0198</td><td>0.7429±0.0211</td><td>0.7504±0.0168</td><td>0.7902±0.0062</td><td>0.8041±0.0046</td><td>0.8087±0.0035</td><td>0.8101±0.0042</td><td>0.8144±0.0064</td></tr><tr><td> $G_8$ </td><td>0.7476±0.0161</td><td>0.7394±0.0143</td><td>0.7490±0.0157</td><td>0.7961±0.0069</td><td>0.8015±0.0037</td><td>0.8043±0.0054</td><td>0.8082±0.0041</td><td>0.8151±0.0022</td></tr><tr><td> $G_9$ </td><td>0.7510±0.0214</td><td>0.7433±0.0153</td><td>0.7469±0.0188</td><td>0.7989±0.0073</td><td>0.8038±0.0033</td><td>0.8069±0.0025</td><td>0.8110±0.0051</td><td>0.8155±0.0048</td></tr><tr><td> $G_{10}$ </td><td>0.7488±0.0139</td><td>0.7505±0.0123</td><td>0.7444±0.0149</td><td>0.8017±0.0047</td><td>0.8043±0.0026</td><td>0.8073±0.0035</td><td>0.8088±0.0019</td><td>0.8103±0.0036</td></tr></table>

## 6.1. Description of real-world case

This case was obtained from a tertiary-level hospital in China. It is famous for the diagnosis of thyroid cancer; however, it is inadequate in the diagnosis of breast cancer. Thus, the data related to the diagnosis of breast cancer are significantly less than those related to the diagnosis of thyroid cancer. Thyroid and breast cancers both have a high incidence rate, and both use ultrasound as a common means of early diagnosis. The ultrasonic diagnoses of thyroid and breast cancers mainly have three perspectives of similarity, as presented below.

(1) Both thyroid and breasts are superficial organs. Based on this, a high-frequency linear ultrasound probe with the same frequency of L14-5WU was used to check the structure, echogenicity, and vascularity of the two organs [53].

Table 7  
Improvement of the ITMD method for five groups of records with same and different symptom spaces.

<table><tr><td>Group ID</td><td>1:1</td><td>2:1</td><td>3:1</td><td>4:1</td><td>Max improvement rate</td></tr><tr><td> $G_1$ </td><td>0.0683</td><td>0.0779</td><td>0.0920</td><td>0.0973</td><td>13.43%</td></tr><tr><td> $G_2$ </td><td>0.0516</td><td>0.0619</td><td>0.0695</td><td>0.0874</td><td>11.88%</td></tr><tr><td> $G_3$ </td><td>0.0583</td><td>0.0653</td><td>0.0714</td><td>0.0789</td><td>10.64%</td></tr><tr><td> $G_4$ </td><td>0.0588</td><td>0.0611</td><td>0.0655</td><td>0.0723</td><td>9.7%</td></tr><tr><td> $G_5$ </td><td>0.0540</td><td>0.0561</td><td>0.0590</td><td>0.0611</td><td>8.15%</td></tr><tr><td> $G_6$ </td><td>0.0633</td><td>0.0708</td><td>0.0748</td><td>0.0827</td><td>11.3%</td></tr><tr><td> $G_7$ </td><td>0.0688</td><td>0.0734</td><td>0.0748</td><td>0.0791</td><td>10.76%</td></tr><tr><td> $G_8$ </td><td>0.0621</td><td>0.0649</td><td>0.0688</td><td>0.0757</td><td>10.24%</td></tr><tr><td> $G_9$ </td><td>0.0605</td><td>0.0636</td><td>0.0677</td><td>0.0722</td><td>9.71%</td></tr><tr><td> $G_{10}$ </td><td>0.0599</td><td>0.0629</td><td>0.0644</td><td>0.0659</td><td>8.85%</td></tr></table>

Table 8  
TI/BI-RADS used in the hospital.

<table><tr><td>Categories</td><td>Findings</td><td>Cancer risk</td></tr><tr><td>3</td><td>Probably benign</td><td>[0, 0.03)</td></tr><tr><td>4A</td><td>Undetermined</td><td>(0.03, 0.25]</td></tr><tr><td>4B</td><td>Suspicious</td><td>(0.25, 0.75]</td></tr><tr><td>4C</td><td>High suspicious</td><td>(0.75, 0.95]</td></tr><tr><td>5</td><td>Probably malignant</td><td>(0.95, 1]</td></tr></table>

(2) Both thyroid and breasts are endocrine glands. In the two glands, a malignant tumor is generally created due to lesions and nec rocytosis of the endocrine cells. The external features of the le sions include the burr of margin, calcification, and definition of contour [54].

(3) The criteria for assessing nodules and stratifying risks in thyroid and breast cancers are similar. BI-RADS was published by the American College of Radiology to help physicians in making uncertain diagnosis of breast cancer. Based on BIRADS, TIRADS was developed for the diagnosis of thyroid cancer [44].

From the first and second perspectives of similarity, the diagnostic process generally starts with detecting the thyroid and breast nodules by ultrasound and examining them according to five characteristics (symptoms): margin, contour, echogenicity, calcification, and vascu larity. For the third perspective of similarity, both TI-RADS and BI-RADS include eight diagnostic categories, five of which are uncertain intervalvalued symptoms.<sup>2</sup> The five diagnostic categories are generally used by physicians in hospitals; that is, TI/BI-RADS 3, 4A, 4B, 4C, and 5. Details regarding TI-RADS and BI-RADS used in the ultrasonic department of the hospital are presented in Table 8. Physicians use the aforementioned five diagnostic categories to evaluate the tumor on each symptom. By using TI/BI-RADS to express the evaluations of symptoms and the di agnoses of cancer risks, the relations between symptoms are consistent in the diagnoses of thyroid and breast cancers.

In clinical practice, physicians transform the observations on the five symptoms into TIRADS categories and further the risk intervals {[0, 0.03], (0.03, 0.25], (0.25, 0.75], (0.75, 0.95], (0.95, 1]}, which are used to describe the relations between patients and symptoms. Five diag nostic categories may be recommended to patients, and their cancer risk intervals are used to determine the relations between patients and diagnostic categories. For example, when a radiologist evaluates a nodule of thyroid and breast on the five symptoms (TI/BI-RADS 3, TI/BI-RADS 4A, TI/BI-RADS 4B, TI/BI-RADS 3, TI/BI-RADS 4A), the overall diagnosis of the thyroid and breast nodules will be TI/BI-RADS 4A, which is generated by synthetically considering the evaluation of symptoms. Thus, the high similarity between the diagnoses of thyroid and breasts results in consistent relations between the symptoms of the two diseases, and such relations can be used as the shared knowledge transferred across the two diseases.

Our datasets comprise the diagnostic assessments of ultrasonic ex amination collected by four physicians from 2017 to 2019. The statis tical information is presented in Table 9. Similar to Section $^ { 5 , }$ both records in the source and target domains are used to train the proposed model discussed in Section 4.4. The dataset in the target domain is divided into two parts using five-fold cross-validation.

The four methods, $B _ { 1 } , B _ { 2 } , B _ { 3 } ,$ and $B _ { 4 } ,$ mentioned in Section 5 were selected as the baselines for comparison with the ITMD method. The experiments for the ITMD method were conducted with four ratios of records between the source and target domains, which were set to 1:1, 2:1, 3:1, and 4:1, respectively. The regularization factor was set to 0.5. The experiments for all compared methods were conducted on the same test sets. The results reported denote the averages with standard de viations from 20 random initializations.

## 6.2. Case study results and analysis

The results are presented in Table 10 and a visual comparison is shown in Fig. $^ { 4 , }$ which leads to the following observations:

(1) The ITMD method performed better than the four baselines with the datasets of all four physicians. Table 11 indicates that in comparison to the four baselines, the largest improvement in prediction accuracy using the ITMD method was 0.1221 and its improvement rate was 16.69%.

(2) $B _ { 1 }$ , $B _ { 2 } ,$ and $B _ { 3 }$ performed so poorly that they would not be acceptable for diagnosing breast cancer without more data. Moreover, with such few data, none of the three methods could maintain stability.

(3) The ITMD method became more accurate as the ratio of records increased. From Table 11, when the source: target ratio increased from 1:1 to 4:1 for physician $F _ { 1 } ,$ the improvement of prediction accuracy with the ITMD method increased from 0.0608 to 0.1095 in comparison to the four baselines. Similar results were observed for the other three physicians.

To further demonstrate the performance of the ITMD method, we conducted experiments when the symptom relation matrix was directly learned from the dataset in the source domain without adjustments. Table 12 presents the prediction results only with the datasets in the source domain.

By comparing the results in Tables 11 and 13, we found that the use of the dataset in the source domain for generating recommendations will have minimal effect on the improvement of the prediction accuracy in the target domain. Meanwhile, although there are only a few labels in the target domain, the results indicate that they can significantly improve the prediction accuracy.

In addition to the prediction accuracy of the ITMD method, we wanted to assess the effectiveness of our new dissimilarity measurement. Table 13 presents the different distance measurements applied to the $B _ { 4 }$ baseline on the four sets of medical records. Our dissimilarity mea surement clearly led to more accurate predictions than other distance measures.

We also examined the influence of λ with a record ratio of 4:1; the results are shown in Fig. 5. As illustrated, the prediction accuracy monotonically increases when λ varies from 0 to 0.5, with no significant change in accuracy from 0.5 to 1.

## 7. Conclusion and future study

In this study, we proposed a new cross-domain recommender system called ITMD to provide personalized recommendations to physicians to determine the disease risks of patients for various diseases. The ITMD method was developed by solving the two challenges of uncertainty in medical diagnosis data and mismatched symptom spaces. A new dissimilarity measurement was developed for diagnosis with interval numbers to depict the dissimilarities between the diagnoses and their predictions to manage the first challenge. A space alignment technique was adopted to align the different symptom spaces of the two domains to manage the second challenge. A collective matrix factorization tech nique was constructed using the ITMD method based on the new mea surement and space alignment technique to implement shared information transfer from the source domain to the target domain. The proposed ITMD method can provide effective decision support in the domain of disease diagnosis with insufficient records. A set of experiments were conducted on synthetic data and a case study was conducted with real-world data for the diagnoses of thyroid cancer and breast cancer. The results suggested that the ITMD method exhibits su perior performance and can provide personalized recommendations to support physicians with diagnosing the risks associated with various diseases. The significance of the results in this paper lies in providing a novel recommendation method in both theoretical and practical way. 1) Theoretically, this paper solves the data sparsity problem in medical diagnosis with the solution of a cross-domain recommendation method that is able to effectively transfer knowledge from a similar domain. The proposed method is able to deal with two theoretical issues: uncertain and heterogeneous representations. 2) Practically, the problem is derived from a real-world scenario occurs in hospital and our solution can be directly used to support the radiologists with insufficient expe riences and help improve their diagnostic accuracy.

Table 9  
Statistics for the diagnostic records of four physicians.

<table><tr><td rowspan="2">Physician ID</td><td rowspan="2">Serving periods</td><td colspan="2">Number of patients</td><td colspan="2">1:1</td><td colspan="2">2:1</td><td colspan="2">3:1</td><td colspan="2">4:1</td></tr><tr><td>Thyroid</td><td>Breast</td><td>Source</td><td>Target</td><td>Source</td><td>Target</td><td>Source</td><td>Target</td><td>Source</td><td>Target</td></tr><tr><td> $F_1$ </td><td>2017–2019</td><td>627</td><td>153</td><td>143</td><td>143</td><td>286</td><td>143</td><td>429</td><td>143</td><td>572</td><td>143</td></tr><tr><td> $F_2$ </td><td>2017–2019</td><td>632</td><td>166</td><td>153</td><td>153</td><td>306</td><td>153</td><td>459</td><td>153</td><td>612</td><td>153</td></tr><tr><td> $F_3$ </td><td>2017–2019</td><td>685</td><td>138</td><td>125</td><td>125</td><td>250</td><td>125</td><td>375</td><td>125</td><td>500</td><td>125</td></tr><tr><td> $F_4$ </td><td>2017–2019</td><td>475</td><td>107</td><td>91</td><td>91</td><td>182</td><td>91</td><td>273</td><td>91</td><td>364</td><td>91</td></tr></table>

Table 10  
Prediction accuracy for the datasets of four physicians.

<table><tr><td rowspan="2">Physician ID</td><td rowspan="2"> $B_1$ </td><td rowspan="2"> $B_2$ </td><td rowspan="2"> $B_3$ </td><td rowspan="2"> $B_4$ </td><td colspan="4">ITMD</td></tr><tr><td>1:1</td><td>2:1</td><td>3:1</td><td>4:1</td></tr><tr><td> $F_1$ </td><td>0.7384±0.0069</td><td>0.7262±0.0058</td><td>0.7307±0.0045</td><td>0.7767±0.0030</td><td>0.7870±0.0082</td><td>0.7999±0.0059</td><td>0.8179±0.0073</td><td>0.8357±0.0014</td></tr><tr><td> $F_2$ </td><td>0.7028±0.0306</td><td>0.6943±0.0401</td><td>0.6897±0.0346</td><td>0.7384±0.0018</td><td>0.7464±0.0085</td><td>0.7582±0.0063</td><td>0.7720±0.0023</td><td>0.7777±0.0042</td></tr><tr><td> $F_3$ </td><td>0.7180±0.0067</td><td>0.7003±0.0095</td><td>0.7185±0.0257</td><td>0.7766±0.0006</td><td>0.7837±0.0016</td><td>0.7945±0.0029</td><td>0.8016±0.0027</td><td>0.8076±0.0028</td></tr><tr><td> $F_4$ </td><td>0.7381±0.0093</td><td>0.7317±0.0024</td><td>0.7423±0.0157</td><td>0.8273±0.0018</td><td>0.8356±0.0011</td><td>0.8399±0.0018</td><td>0.8451±0.0011</td><td>0.8538±0.0019</td></tr></table>

Table 13

Prediction accuracy on the target domain with different distance measurements.  
![](/api/attachments/B7AZXNG6/fulltext/images/8ebabc438e2b29fea3ee73931be50441c0ae40d4bdf1499f62c21284a8f9fb92.jpg)  
Fig. 4. Average prediction accuracy for all methods.

Improvement of the ITMD method for five groups of records with same and different symptom spaces.

<table><tr><td>Physician ID</td><td>1:1</td><td>2:1</td><td>3:1</td><td>4:1</td><td>Max improvement rate</td></tr><tr><td> $F_1$ </td><td>0.0608</td><td>0.0737</td><td>0.0917</td><td>0.1095</td><td>15.08%</td></tr><tr><td> $F_2$ </td><td>0.0567</td><td>0.0685</td><td>0.0823</td><td>0.0880</td><td>12.76%</td></tr><tr><td> $F_3$ </td><td>0.0834</td><td>0.0942</td><td>0.1013</td><td>0.1073</td><td>15.32%</td></tr><tr><td> $F_4$ </td><td>0.1039</td><td>0.1082</td><td>0.1134</td><td>0.1221</td><td>16.69%</td></tr></table>

Table 12  
Prediction accuracy for the datasets of four physicians in the source domain.

<table><tr><td rowspan="2">Physician ID</td><td colspan="4">Prediction accuracy</td></tr><tr><td>1:1</td><td>2:1</td><td>3:1</td><td>4:1</td></tr><tr><td> $F_1$ </td><td>0.7816±0.0018</td><td>0.7852±0.0028</td><td>0.7895±0.0027</td><td>0.7919±0.0039</td></tr><tr><td> $F_2$ </td><td>0.7246+0.0027</td><td>0.7332±0.0041</td><td>0.7350±0.0014</td><td>0.7432±0.0030</td></tr><tr><td> $F_3$ </td><td>0.7790±0.0003</td><td>0.7797±0.0010</td><td>0.7815±0.0011</td><td>0.7868±0.0010</td></tr><tr><td> $F_4$ </td><td>0.8258±0.0020</td><td>0.8262±0.0012</td><td>0.8296±0.0010</td><td>0.8314±0.0014</td></tr></table>

<table><tr><td></td><td>Euclidean distance</td><td>Manhattan distance</td><td>Chebyshev distance</td><td>Dissimilarity measurement</td></tr><tr><td> $F_1$ </td><td>0.5917±0.0057</td><td>0.6428±0.0043</td><td>0.6435±0.0029</td><td>0.7767±0.0030</td></tr><tr><td> $F_2$ </td><td>0.6076±0.0054</td><td>0.6174±0.0050</td><td>0.6116±0.0065</td><td>0.7384±0.0018</td></tr><tr><td> $F_3$ </td><td>0.6349±0.0015</td><td>0.6463±0.0036</td><td>0.6450±0.0042</td><td>0.7766±0.0006</td></tr><tr><td> $F_4$ </td><td>0.6140±0.0042</td><td>0.6083±0.0010</td><td>0.6072±0.0010</td><td>0.8273±0.0018</td></tr><tr><td> $\overline{F}$ </td><td>0.6120±0.0042</td><td>0.6287±0.0035</td><td>0.6268±0.0036</td><td>0.7798±0.0018</td></tr></table>

![](/api/attachments/B7AZXNG6/fulltext/images/79c9059bfc5cdf17dae34e4f7736779234c7176f3969ae446b967a4f81aa518b.jpg)  
Fig. 5. Prediction accuracy for the four physicians with changes in λ.

In future study, we intend to focus on extending the principles of the ITMD method to more complex settings, such as the transfer of hetero geneous diagnostic data across domains. We will also consider other salient aspects of medical diagnoses, such as patient privacy, the attitudes of physicians toward risks, and the gold standards in medical diagnosis.

## CRediT authorship contribution statement

Wenjun Chang: Methodology, Software, Validation, Writing - orig inal draft. Qian Zhang: Methodology, Software, Writing - original draft. Chao Fu: Conceptualization, Validation, Funding acquisition. Weiyong Liu: Data curation. Guangquan Zhang: Supervision, Funding acquisition, Idea discussion. Jie Lu: Supervision, Conceptualiazation, Writing - re view & editing, Funding acquisition.

## Acknowledgments

This work was partially supported by the Australian Research Council (ARC) under the Australian Laureate Fellowship [FL190100149] and the National Natural Science Foundation of China (Grant Nos. 71622003 and 71571060).

## Appendix A. Proof of Property 1

Proof. Eqs. (4)–(7) are verified in A.1–4.

A.1. Because $\Biggl ( r _ { m l } - \widehat { r } _ { m l } \Biggr ) ^ { 2 } \cdot \Biggl ( r _ { m k } - \widehat { r } _ { m k } \Biggr ) ^ { 2 } \cdot \left( \overline { { { p } } } ( C _ { k } ) - \overline { { { p } } } ( C _ { l } ) \right) ^ { 2 } \ \geq \ 0$ and $\overline { { { p } } } ( C _ { N } ) - \overline { { { p } } } ( C _ { 1 } ) ~ > ~ 0$ in Eq. (3), it follows tha $d ( R , { \widehat { R } } ) \geq 0 .$ . In addition, $\begin{array} { r } { \sum _ { l = 1 } ^ { N - 1 } \sum _ { k = l + 1 } ^ { N } \bigg ( r _ { m l } - \widehat { r } _ { m l } \bigg ) ^ { 2 } \cdot \bigg ( r _ { m k } - \widehat { r } _ { m k } \bigg ) ^ { 2 } \cdot \big ( \overline { { p } } ( C _ { k } ) - \overline { { p } } ( C _ { l } ) \big ) ^ { 2 } \leq \big ( \overline { { p } } ( C _ { N } ) - \overline { { p } } ( C _ { 1 } ) \big ) ^ { 2 } . } \end{array}$

Thus, we can deduce that

$$
\frac {\sum_ {m = 1} ^ {M} \sqrt {\sum_ {l = 1} ^ {N - 1} \sum_ {k = l + 1} ^ {N} \left(r _ {m l} - \widehat {r} _ {m l}\right) ^ {2} \cdot \left(r _ {m k} - \widehat {r} _ {m k}\right) ^ {2}} \cdot (\overline {{p}} (C _ {k}) - \overline {{p}} (C _ {l})) ^ {2}}{M \cdot (\overline {{p}} (C _ {N}) - \overline {{p}} (C _ {1}))} \leq \frac {\sum_ {m = 1} ^ {M} \overline {{p}} (C _ {N}) - \overline {{p}} (C _ {1})}{M \cdot (\overline {{p}} (C _ {N}) - \overline {{p}} (C _ {1}))} = 1
$$

Correspondingly, we have $0 \leq d ( R , { \widehat { R } } ) \leq 1$ , which verifies $\operatorname { E q . }$ (4).

A.2. Eq. (5) is easily proved.

A.3. Two things must be verified in Eq. (6)

(1) If $\scriptstyle \mathbf { R } = { \widehat { R } } ,$ we have $\begin{array} { r } { r _ { m n } = \widehat { r } _ { m n } , m { = } 1 , . . . , M , n { = } 1 , . . . , N . } \end{array}$ By substituting this into Eq. (3), we obtain $d ( R , { \widehat { R } } ) = 0$

(2) According to Eq. (3), we deduced from d(R, R<sup>̂</sup>) = 0 that $\begin{array} { r } { \Big ( r _ { m l } - \widehat { r } _ { m l } \Big ) ^ { 2 } \cdot \Big ( r _ { m k } - \widehat { r } _ { m k } \Big ) ^ { 2 } \cdot ( \overline { { p } } ( C _ { k } ) - \overline { { p } } ( C _ { l } ) ) ^ { 2 } { = } 0 , m { = } 1 , . . . , M , l { = } 1 , . . . , N - 1 , k { = } l { + } 1 , . . . , N . } \end{array}$ Because $\overline { { { p } } } ( C _ { k } ) \ : - \ : \overline { { { p } } } ( C _ { l } ) > 0 , l = 1 , . . . , N - 1 , k = l + 1 , . . . , N ,$ we can conclude that $\boldsymbol { r } _ { m n } = \widehat { \boldsymbol { r } } _ { m n } , m { = } 1 , . . . , M , n = 1 , . . . , N , \mathrm { i } . \mathrm { e } . , R = \widehat { R }$ . Thus, Eq. (6) is verified.

## A.4. Two things must be verified in Eq. (7)

(1) Under the condition that $r _ { m 1 } { = } 1 \mathrm { a n d } \widehat { r } _ { m N } { = } 1 ( m { = } 1 , { \ldots } , M )$ , we can infer from $\begin{array} { r } { \sum _ { n = 1 } ^ { N } r _ { m n } = 1 \mathrm { { a n d } } \sum _ { n = 1 } ^ { N } \widehat { r } _ { m n } = 1 \mathrm { { t h a t } } r _ { m n } = 0 , n = 2 , . . . , N \mathrm { { a n d } } \widehat { r } _ { m n } = 0 , } \end{array}$ $\pmb { n } = 1 , . . . , N { - 1 }$ . Then, $d ( R , { \widehat { R } } )$ can be calculated as $\begin{array} { r } { d ( R , \widehat { R } ) = \frac { \sum _ { m = 1 } ^ { M } \sqrt { \Big ( r _ { m 1 } - \widehat { r } _ { m 1 } \Big ) ^ { 2 } \cdot \Big ( r _ { m N } - \widehat { r } _ { m N } \Big ) ^ { 2 } \cdot ( \overline { { p } } ( C _ { N } ) - \overline { { p } } ( C _ { 1 } ) ) ^ { 2 } } } { M \cdot ( \overline { { p } } ( C _ { N } ) - \overline { { p } } ( C _ { 1 } ) ) } = 1 } \end{array}$ . Conditioned on $r _ { m N } { = } 1$ and $\widehat { r } _ { m 1 } = 1 ( m =$ $1 , . . . , M ) , d ( R , \widehat { R } ) { = } 1$ can be similarly verified.

(2) Because $\overline { { p } } ( C _ { N } ) - \overline { { p } } ( C _ { 1 } )$ is the maximum value $\begin{array} { r } { \mathfrak { q } \overline { { p } } ( C _ { k } ) - \overline { { p } } ( C _ { l } ) , l = 1 , . . . , N \mathfrak { q } , k = l \mathrm { + } 1 , . . . , N , } \end{array}$ we prioritize the assignment of $r _ { m l }$ and $\widehat { r } _ { m l } \ : ( l = 1 , . . . ,$ L) to $\biggl ( r _ { m 1 } - \widehat { r } _ { m 1 } \biggr ) ^ { 2 } \cdot \biggl ( r _ { m N } - \widehat { r } _ { m N } \biggr ) ^ { 2 }$ for achieving the maximum value of d(R, R<sup>̂</sup>), i.e., 1. This implies that when $d ( R , { \widehat { R } } ) = 1$ $\bigg ( r _ { m 1 } - \widehat { r } _ { m 1 } \bigg ) ^ { 2 } \cdot \bigg ( r _ { m N } - \widehat { r } _ { m N } \bigg ) ^ { 2 } = 1$ is satisfied, which indicates that ${ \biggl ( } r _ { m 1 } - { \widehat { r } } _ { m 1 } { \biggr ) } ^ { 2 } { = } 1 { \mathrm { ~ a n d ~ } } { \biggl ( } r _ { m N } - { \widehat { r } } _ { m N } { \biggr ) } ^ { 2 } { = } 1$ . Then, we have $( r _ { m 1 } { = } 1 ,  { \stackrel {  } { r } } _ { m N } { = } 1 )$ or $( r _ { m N } { = } 1 ,  { \widehat { r } } _ { m 1 } { = } 1 )$ ). Thus. Eq. (7) is verified. Accordingly. Property 1 is verified.

## Appendix B. Proof of Theorem 1

Proof. Two things must be verified for Eq. (8):

$$
\frac {\| \Delta R _ {t} \| _ {F}}{\| R _ {t} \| _ {F}} \geq \frac {1}{\text {cond} (D _ {t}) \cdot \text {cond} (V _ {t})} \cdot \frac {\left\| \Delta \overline {{U}} _ {t} \right\| _ {F}}{\left\| \overline {{U}} _ {t} \right\| _ {F}} \quad \text {and} \quad (2) \frac {\| \Delta R _ {t} \| _ {F}}{\| R _ {t} \| _ {F}} \leq \text {cond} (D _ {t}) \cdot \text {cond} (V _ {t}) \cdot \frac {\left\| \Delta \overline {{U}} _ {t} \right\| _ {F}}{\left\| \overline {{U}} _ {t} \right\| _ {F}}.
$$

(1) Suppose that $\Delta D _ { t }$ has a small value and satisfies $\| \Delta D _ { t } D _ { t } ^ { + } \| _ { F } < 1$ , where the symbol “+” represents the generalized inverse of a matrix, and R<sub>t</sub> + ΔR<sub>t</sub> = U<sub>t</sub> + ΔU<sub>t</sub> (D<sub>t</sub> + ΔD<sub>t</sub>)V<sub>t</sub>. (B.1)

From Eq. (B.1), we deduce that

$$
\Delta \overline {{{U}}} _ {t} (D _ {t} + \Delta D _ {t}) V _ {t} = \Delta R _ {t} - \overline {{{U}}} _ {t} \Delta D _ {t} V _ {t} \Rightarrow \Delta \overline {{{U}}} _ {t} (D _ {t} + \Delta D _ {t}) V _ {t} V _ {t} ^ {+} D _ {t} ^ {+} = \left(\Delta R _ {t} - \overline {{{U}}} _ {t} \Delta D _ {t} V _ {t}\right) V _ {t} ^ {+} D _ {t} ^ {+}
$$

$$
\Rightarrow \Delta \overline {{{U}}} _ {t} = \left(\Delta R _ {t} V _ {t} ^ {+} - \overline {{{U}}} _ {t} \Delta D _ {t}\right) D _ {t} ^ {+} (I + \Delta D _ {t} D _ {t} ^ {+}) ^ {+}.\tag{B.2}
$$

Because $\| - \Delta D _ { t } \pmb { D } _ { t } ^ { + } \| _ { F } = \| \Delta \pmb { D } _ { t } \pmb { D } _ { t } ^ { + } \| _ { F } < 1$ , we have

$$
\left\| \left(\boldsymbol {I} + \Delta \boldsymbol {D} _ {t} \boldsymbol {D} _ {t} ^ {+}\right) ^ {+} \right\| _ {F} \leq \frac {1}{1 - \left\| \Delta \boldsymbol {D} _ {t} \boldsymbol {D} _ {t} ^ {+} \right\| _ {F}} \leq \frac {1}{1 - \left\| \Delta \boldsymbol {D} _ {t} \right\| _ {F} \left\| \boldsymbol {D} _ {t} ^ {+} \right\| _ {F}}.\tag{B.3}
$$

According to Eqs. (B.2) and (B.3), we can conclude that

$$
\left\| \Delta \overline {{U}} _ {t} \right\| _ {F} = \left\| \left(\Delta R _ {t} V _ {t} ^ {+} - \overline {{U}} _ {t} \Delta D _ {t}\right) D _ {t} ^ {+} (I + \Delta D _ {t} D _ {t} ^ {+}) ^ {+} \right\| _ {F} \leq \left(\frac {\| \Delta R _ {t} \| _ {F} \| V _ {t} ^ {+} \| _ {F}}{\left\| \overline {{U}} _ {t} \right\| _ {F} \| D _ {t} \| _ {F}} + \frac {\| \Delta D _ {t} \| _ {F}}{\| D _ {t} \| _ {F}}\right) \frac {\left\| \overline {{U}} _ {t} \right\| _ {F} \| D _ {t} \| _ {F} \| D _ {t} ^ {+} \| _ {F}}{1 - \| \Delta D _ {t} \| _ {F} \| D _ {t} ^ {+} \| _ {F}}.\tag{B.4}
$$

Because $R _ { t } = \overline { { U } } _ { t } D _ { t } V _ { t } ;$ , we have

$$
\left\| \boldsymbol {R} _ {t} \right\| _ {F} \leq \left\| \overline {{{{\boldsymbol {U}}}}} _ {t} \right\| _ {F} \left\| \boldsymbol {D} _ {t} \right\| _ {F} \left\| \boldsymbol {V} _ {t} \right\| _ {F}.\tag{B.5}
$$

From Eqs. (B.4) and (B.5), we can deduce that

$$
\frac {\left\| \Delta \overline {{U}} _ {t} \right\| _ {F}}{\left\| \overline {{U}} _ {t} \right\| _ {F}} \leq \left(\frac {\| \Delta R _ {t} \| _ {F} \| V _ {t} \| _ {F} \| V _ {t} ^ {+} \| _ {F}}{\| R _ {t} \| _ {F}} + \frac {\| \Delta D _ {t} \| _ {F}}{\| D _ {t} \| _ {F}}\right) \cdot \frac {\| D _ {t} \| _ {F} \| D _ {t} ^ {+} \| _ {F}}{1 - \| \Delta D _ {t} \| _ {F} \| D _ {t} ^ {+} \| _ {F}} = \left(\frac {\| \Delta R _ {t} \| _ {F}}{\| R _ {t} \| _ {F}} \cdot c o n d (V _ {t}) + \frac {\| \Delta D _ {t} \| _ {F}}{\| D _ {t} \| _ {F}}\right) \cdot \frac {c o n d (D _ {t})}{1 - \| \Delta D _ {t} \| _ {F} \| D _ {t} ^ {+} \| _ {F}}.
$$

Suppose that $\Delta D = O ;$ , then it can be deduced into $\begin{array} { r } { \frac { \| \Delta R _ { t } \| _ { F } } { \| R _ { t } \| _ { F } } \geq \frac { 1 } { c o n d ( D _ { t } ) \cdot c o n d ( V _ { t } ) } . \frac { \left\| \Delta \overline { { U } } _ { t } \right\| _ { F } } { \left\| \overline { { U } } _ { t } \right\| _ { F } } } \end{array}$

(2) Because $R _ { t } + \Delta R _ { t } = \bigg ( \overline { { U } } _ { t } + \Delta \overline { { U } } _ { t } \bigg ) D _ { t } V _ { t }$ and $R _ { t } = \overline { { U } } _ { t } D _ { t } V _ { t } ,$ we have $\Delta R _ { t } = \Delta \overline { { U } } _ { t } D _ { t } V _ { t } .$ . Thus, $\begin{array} { r } { \| \Delta \pmb { R } _ { t } \| _ { F } \le \left\| \Delta \overline { { U } } _ { t } \right\| _ { F } \| \pmb { D } _ { t } \| _ { F } \| V _ { t } \| _ { F } , } \end{array}$ , which indicates that <sup>⃦</sup><sub>⃦ΔU</sub> F ≥ ‖ΔR<sub>t</sub>‖ <sup>⃦</sup><sub>⃦Ut</sub><sup>⃦</sup><sub>⃦</sub> <sub>‖Dt‖F</sub> <sub>‖Vt‖F</sub><sup>⃦</sup><sub>⃦Ut</sub><sup>⃦</sup><sub>⃦</sub>

From $R _ { t } = \overline { { U } } _ { t } D _ { t } V _ { t } ,$ , we have $\overline { { U } } _ { t } = R _ { t } { V _ { t } } ^ { + } { D _ { t } } ^ { + }$ , which infers $\left\| \overline { { U } } _ { t } \right\| _ { F } \leq \| R _ { s } \| _ { F } \| V _ { s } + \| _ { F } \| D _ { s } + \| _ { F }$ . Combining the two inequations, we have $\begin{array} { r l } & { \frac { \left\| \Delta \overline { { U } } _ { t } \right\| _ { F } } { \left\| \overline { { U } } _ { t } \right\| _ { F } } \ge } \end{array}$

$$
\frac {\| \Delta \boldsymbol {R} _ {t} \| _ {F}}{\| \boldsymbol {D} _ {t} \| _ {F} \| \boldsymbol {V} _ {t} \| _ {F} \| \boldsymbol {R} _ {t} \| _ {F} \| \boldsymbol {V} _ {t} ^ {+} \| _ {F} \| \boldsymbol {D} _ {t} ^ {+} \| _ {F}} = \frac {\| \Delta \boldsymbol {R} _ {t} \| _ {F}}{\operatorname{cond} (\boldsymbol {D} _ {t}) \operatorname{cond} (\boldsymbol {V} _ {t}) \| \boldsymbol {R} _ {t} \| _ {F}}; \text {   that   is,   } \frac {\| \Delta \boldsymbol {R} _ {t} \| _ {F}}{\| \boldsymbol {R} _ {t} \| _ {F}} \leq \operatorname{cond} (\boldsymbol {D} _ {t}) \cdot \operatorname{cond} (\boldsymbol {V} _ {t}) \cdot \frac {\left\| \Delta \overline {{U}} _ {t} \right\| _ {F}}{\left\| \overline {{U}} _ {t} \right\| _ {F}}.
$$

Thus, $\operatorname { E q . }$ (8) is verified. Similarly, $\operatorname { E q . }$ (9) is proved and, correspondingly, Theorem 1 is verified.

## References

[1] A.H. Shahid, M.P. Singh, Computational intelligence techniques for medical diagnosis and prognosis: problems and current developments, Biocybern. Biomed. Eng, 39 (2019) 638–672

[2] Y. Gao, P.G. Church, Improving molecular cancer class discovery through sparse non-negative matrix factorization, Bioinformatics 21 (21) (2005) 3970–3975.

[3] A.S. Hussein, W.M. Omar, X. Li, M. Ati, Efficient chronic disease diagnosis prediction and recommendation system, in: IEEE EMBS Conference on Biomedical

[4] S. Hassan, Z. Syed, From Netflix to heart attacks: collaborative filtering in medical datasets, in: Proceedings of the 1st ACM International Health Informatics Symposium, ACM, 2010, pp. 128–134.

[5] N.T. Thong, L.H. Son, HIFCF: an effective hybrid model between picture fuzzy clustering and intuitionistic fuzzy recommender systems for medical diagnosis, Expert Syst. Appl. 42 (2015) 3682–3701.

[6] M. Mao, J. Lu. G. Zhang, J. Zhang. Multirelational social recommendations via multigraph ranking, IEEE Trans. Cybern. 47 (12) (2017) 4049–4061.

[7] J. Son. S.B. Kim. Academic paper recommender system using multilevel simultaneous citation networks, Decis, Support, Syst, 105 (2018) 24–33

[8] S. Bag, S. Kumar, A. Awasthi, M.K. Tiwari, A noise correction-based approach to support a recommender system in a highly sparse rating environment, Decis. Support, Syst, 118 (2019) 46–57.

[9] J. Lu. D. Wu, M. Mao, W. Wang, G. Zhang, Recommender system application developments: a survey, Decis. Support. Syst. 74 (2015) 12–32

[10] C.A.N. Okoromah, A.F.E. Lesi, Diazepam for treating tetanus, Cochrane Database Syst, Rev, 19 (2004). CD003954.

[11] H. Younis, M.H. Bhatti, M. Azeem, Classification of skin cancer dermoscopy images using transfer learning, in: 2019 15th International Conference on Emerging Technologies (ICET), IEEE, 2019, pp. 1–4.

[12] A. Ramcharan, K. Baranowski, P. Mccloskey, B. Ahmed, J.P. Legg, D.P. Hughes, Deep learning for image-based cassava disease detection, Front. Plant Sci. 8 (2017) 1852.

[13] K. Zhou, W. He, Y. Xu, G. Xiong, J. Cai, Feature selection and transfer learning for Alzheimer’s disease clinical diagnosis, Appl. Sci. 8 (8) (2018) 1372.

[14] Q. Do, W. Liu, J. Fan, D. Tao, Unveiling hidden implicit similarities for crossdomain recommendation, IEEE Trans. Knowledge Data Eng. 33 (1) (2019) 302–315.

[15] S.W. Dubrey, K. Cha, M. Skinner, M.P. Lavalley, R.H. Falk, Familial and primary (AL) cardiac amyloidosis: echocardiographically similar diseases with distinctly different clinical outcomes, Heart 78 (1) (1997) 74–82.

[16] T. Imasawa, M. Tanaka, N. Maruyama, T. Kawaguchi, Y. Yamaguchi, R. Rossignol, H. Kitamura, M. Nishimura, Pathological similarities between low birth weight related nephropathy and nephropathy associated with mitochondrial cytopathy, Diagn. Pathol. 9 (2014) 181.

[17] C.Y. Ok, K.P. Patel, G. Garcia-Manero, M.J. Routbort, J. Peng, G. Tang, M. Goswami, K.H. Young, R. Singh, L.J. Medeiros, H.M. Kantarjian, R. Luthra, S. A. Wang, TP53 mutation characteristics in therapy-related myelodysplastic syndromes and acute myeloid leukemia is similar to de novo diseases, J. Hematol. Oncol. 8 (2015) 45.

[18] Q. Zhang, G. Zhang, J. Lu, D. Wu, A framework of hybrid recommender system for personalized clinical prescription, in: 2015 10th International Conference on Intelligent Systems and Knowledge Engineering (ISKE), IEEE, 2015, pp. 189–195.

[19] A. Mustaqeem, S.M. Anwar, M. Majid, A modular cluster based collaborative recommender system for cardiac patients, Artif. Intell. Med. 102 (2020) 101761.

[20] L. Sun, C. Liu, C. Guo, H. Xiong, Y. Xie, Data-driven automatic treatment regimen development and recommendation, in: Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, ACM, 2016, pp. 1865–1874.

[21] D.A. Davis, N.V. Chawla, N. Blumm, N. Christakis, A.L. Barabasi, Predicting individual disease risk based on medical history, in: Proceedings of the 17th ACM Conference on Information and Knowledge Management, ACM, 2008, pp. 769–778.

[22] B. Li, Q. Yang, X. Xue, Transfer learning for collaborative filtering via a rating matrix generative model, in: Proceedings of the 26th Annual Internationa Conference on Machine Learning, ACM, 2009, pp. 617–624.

[23] S. Gao, H. Luo, D. Chen, S. Li, P. Gallinari, Z. Ma, J. Guo, A cross-domain recommendation model for cyber physical systems, IEEE Trans. Emerging Top. Comput, 1 (2) (2013) 384–393.

[24] O. Zhang. D. Wu, J. Lu. F. Liu. G. Zhang, A cross-domain recommender system with consistent information transfer. Decis. Support. Syst. 104 (2017) 49–63

[25] W. Pan, E.W. Xiang, N.N. Liu, Q. Yang, Transfer learning in collaborative filtering for sparsity reduction, in: The 24th AAAI Conference on Artificial Intelligence. ACM. 2010, pp. 230–235

[26] W. Pan, Q. Yang, Transfer learning in heterogeneous collaborative filtering domains. Artif, Intell, 197 (2013) 39–55.

[27] Q. Zhang, J. Lu, D. Wu, G. Zhang, A cross-domain recommender system with kernel-induced knowledge transfer for overlapping entities, IEEE Trans. Neural Netw. Learn. Syst. 30 (7) (2019) 1998–2012.

[28] Y. Shi, M. Larson, A. Hanjalic, Collaborative filtering beyond the user-item matrix: (2014) 1–45.

[29] W. Chen, W. Hsu, M.L. Lee, Making recommendations from multiple domains, in: Proceedings of the 19th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, ACM, 2013, pp. 892–900.

[30] M. Jiang, P. Cui, X. Chen, F. Wang, W. Zhu, S. Yang, Social recommendation with cross-domain transferable knowledge, IEEE Trans. Knowledge Data Eng. 27 (11) (2015) 3084–3097.

[31] Y. Shi, M. Larson, A. Hanjalic, Tags as bridges between domains: improving recommendation with tag-induced cross-domain collaborative filtering, in: Proceedings of the 19th International Conference on User Modeling, Adaptation, and Personalization, ACM, 2011, pp. 305–316.

[32] Z. Fang, S. Gao, B. Li, J. Li, J. Liao, Cross-domain recommendation via tag matrix transfer, in: IEEE International Conference on Data Mining Workshop, IEEE, 2015,

[33] P. Hao, G. Zhang, L. Martinez, J. Lu, Regularizing knowledge transfer in recommendation with tag-inferred correlation, IEEE Trans. Cybern. 49 (1) (2019) 83–96.

[34] X. Xin, Z. Liu, C.Y. Lin, H. Huang, X. Wei, P. Guo, Cross-domain collaborative filtering with review text, in: Proceedings of the Twenty-Fourth International Joint Conference on Artificial Intelligence, ACM, 2015, pp. 1827–1833

[35] T. Song, Z. Peng, S. Wang, W. Fu, X. Hong, P.S. Yu, Review-Based Cross-Domain Recommendation through Joint Tensor Factorization. International Conference on Database Systems for Advanced Applications, Springer, 2017, pp. 525–540.

[36] I. Fern´andez-Tobías, I. Cantador, P. Tomeo, V.W. Anelli, T. Di Noia, Addressing the user cold start with cross-domain collaborative filtering: exploiting item metadata in matrix factorization, user model. User-Adapt. Interact. 29 (2019) 443–486.

[37] C. Jiang, X. Han, G.R. Liu, G.P. Liu, A nonlinear interval number programming method for uncertain optimization problems, Eur. J. Oper. Res. 188 (1) (2008) 1–13.

[38] D.D. Lee, H.S. Sebastian, Algorithms for non-negative matrix factorization, in: Proceedings of the 13th International Conference on Neural Information Processing Systems, ACM, 2000, pp. 535–541.

[39] W. Wang, G. Zhang, J. Lu, Member contribution-based group recommender system, Decis. Support. Syst. 87 (2016) 80–93.

[40] G. Adomavicius, Y.O. Kwon, New recommendation techniques for multicriteri rating systems, IEEE Intel. Syst. 22 (3) (2007) 48–55.

[41] A.K. Cline, C.B. Moler, G.W. Stewart, J.H. Wilkinson, An estimate for the condition number of a matrix, SIAM J. Numer. Anal. 16 (2) (1979) 368–375.

[42] P.T. Boggs, J.W. Tolle, Sequential Quadratic Programming, Acta Numer. (1995) 199–242.

[43] B.K. Chan, T.S. Desser, I.R. McDougall, R.J. Weigel, R.B. Jeffrey, Common and uncommon sonographic features of papillary thyroid carcinoma, J. Ultrasound Med. 22 (10) (2003) 1083–1090.

[44] C. Fu, W. Chang, W. Liu, S. Yang, Data-driven group decision making for diagnosis of thyroid nodule, Sci. China Info. Sci. 62 (11) (2019), 212205.

[45] K. Akahoshi, Y. Chijiwa, S. Hamada, I. Sasaki, H. Nawata, T. Kabemura, D. Yasuda, H. Okabe, Pretreatment staging of endoscopically early gastric cancer with a 15 MHz ultrasound catheter probe, Gastrointest. Endosc. 48 (1998) 470–476.

[46] T. Yoshida, H. Matsue, N. Okazaki, M. Yoshino, Ultrasonographic differentiation of hepatocellular carcinoma from metastatic liver cancer, J. Clin. Ultrasound 15 (1987) 431–437

[47] H.S. Ahn, H.J. Lee, S. Hahn, W.H. Kim, K.U. Lee, T. Sano, S.B. Edge, H.K. Yang, Evaluation of the seventh American joint committee on Cancer/International Union against Cancer classification of gastric adenocarcinoma in comparison with the sixth classification, Cancer 116 (2010) 5592–5598.

[48] G. Torzilli, M. Makuuchi, Intraoperative ultrasonography in liver cancer, Surg. Oncol. Clin. N. Am. 12 (2003) 91–103.

[49] P. Memar, F. Faradji, A novel multi-class EEG-based sleep stage classification system, IEEE Trans. Knowledge Data Eng. 32 (8) (2020) 1586–1594.

[50] I. Cantador, I. Fernandez-Tobías, ´ S. Berkovsky, P. Cremonesi, Cross-domain recommender systems, in: F. Ricci, L. Rokach, B. Shapira (Eds.), Recommende systems handbook, Springer, Boston, MA, 2015, pp. 919–959.

[51] C. Fu, W. Chang, D. Xu, S. Yang, An evidential reasoning approach based on criterion reliability and solution reliability, Comput. Ind. Eng. 128 (2019) 402–417.

[52] A. Sengupta, T.K. Pal, Fuzzy Preference Ordering of Interval Numbers in Decision Problems, Springer, New York, 2009.

[53] X. Liang, J. Yu, J. Liao, Z. Chen, Convolutional neural network for breast and thyroid nodules diagnosis in ultrasound imaging, Biomed. Res. Int. 1763803 (2020).

[54] D. Schottenfeld. The relationship of breast cancer to thyroid disease. J. Chronic Dis 21 (5) (1968) 303–313.

Wenjun Chang received the master degree from Hefei University of Technology, China, in 2017. He is currently a Ph.D. student in School of Management, Hefei University of Technology. His research interests include data-driven decision analysis, uncertain multi criteria decision making, recommender system, and medical auxiliary diagnosis.

Qian Zhang is a Postdoc Research Fellow and a member of the Decision Systems and e-Service Intelligent (DeSI) Research Laboratory at the Centre for Artificial Intelligence, Faculty of Engineering and Information Technology, University of Technology Sydney, Australia. She received her PhD degree from University of Technology Sydney, Australia, in 2018. Her research interests include recommender systems and personalized tech niques. She specializes in cross-domain recommender systems.

Chao Fu received the Ph.D. degree from Hefei University of Technology, China, in 2009. He is currently a professor in School of Management, Hefei University of Technology. He has published more than 40 articles in international journals. such as JEEE Journal of Biomedical and Health Informatics, European Journal Of Operational Research and Journal of the Operational Research Society. His research interests include data-driven decision analysis, data-driven behavioural analysis, evidential reasoning, belief rule base. and medical auxiliary diagnosis.

Weiyong Liu received the Ph.D. degree from Shanghai Jiaotong University, China, in 2017. He is currently a doctor in Department of Ultrasound, The First Affiliated Hospital of USTC, Division of Life Sciences and Medicine, University of Science and Technology of China. His research interests include ultrasonic diagnosis and data-driven auxiliary diagnosis.

Guangquan Zhang is an Associate Professor and Director of the Decision Systems and e-Service Intelligent (DeSI) Research Laboratory at the Centre for Artificial Intelligence, Faculty of Engineering and Information Technology, University of Technology Sydney, Australia. He received his PhD in applied mathematics from Curtin University of Tech nology, Australia, in 2001. His research interests include fuzzy machine learning, fuzzy optimization, and machine learning and data analytics. He has authored four monographs, five textbooks, and 450 papers in Artificial Intelligence Journal, Machine Learning Jour nal, IEEE Transactions on Fuzzy Systems and other refereed journals and conference proceedings. Dr. Zhang has won seven Australian Research Council (ARC) Discovery Project grants and many other research grants. He was awarded an ARC QEII Fellowship in 2005. He has served as a member of the editorial boards of several international journals, as a guest editor of eight special issues for IEEE Transactions and other international journals and cochaired several international conferences and workshops in the area of fuzzy decision-making and knowledge engineering.

Jie Lu (F’18) is a Distinguished Professor and the Director of the Centre for Artificial Intelligence at the University of Technology Sydney, Australia. She received her PhD de gree from Curtin University of Technology, Australia, in 2000. Her main research interests are in the areas of fuzzy transfer learning, concept drift, decision support systems, and recommender systems. She is an IEEE fellow, IFSA fellow and Australian Laureate fellow. She has published six research books and over 450 papers in refereed journals and con ference proceedings; has won over 20 ARC Laureate, ARC Discovery Projects, government and industry projects. She serves as Editor-In-Chief for Knowledge-Based Systems (Elsevier) and Editor-In-Chief for International journal of computational intelligence systems. She has delivered over 25 keynote speeches at international conferences and chaired 15 international conferences. She has received various awards such as the UTS Medal for Research and Teaching Integration (2010), the UTS Medal for Research Excel lence (2019), the Computer Journal Wilkes Award (2018), the IEEE Transactions on Fuzzy Systems Outstanding Paper Award (2019), and the Australian Most Innovative Engineer Award (2019).
