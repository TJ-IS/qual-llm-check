---
otero_id: 3382
otero_key: "T5YPFZH7"
title: "Adapting domain ontology for personalized knowledge search and recommendation"
authors: "Yuh-Jen Chen; Hui-Chuan Chu; Yuh-Min Chen; Chung-Yueh Chao"
year: "2013"
journal: "Information & Management"
doi: "10.1016/j.im.2013.05.001"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

Title: Adapting Domain Ontology for Personalized Knowledge Search and Recommendation

Author: Yuh-Jen Chen Yuh-Min Chen Hui-Chuan Chu Chung-Yueh Chao

![](/api/attachments/T5YPFZH7/fulltext/images/40c9e77aeadcf8d8311220979a2a6e88468af11188b6fa2ce2af0c588b89ab6a.jpg)

PII: S0378-7206(13)00041-4

DOI: http://dx.doi.org/doi:10.1016/j.im.2013.05.001

Reference: INFMAN 2629

To appear in: INFMAN

Received date: 30-3-2012

Revised date: 8-4-2013

Accepted date: 7-5-2013

Please cite this article as: Y.-J. Chen, Y.-M. Chen, H.-C. Chu, C.-Y. Chao, Adapting Domain Ontology for Personalized Knowledge Search and Recommendation, Information & Management (2013), http://dx.doi.org/10.1016/j.im.2013.05.001

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Adapting Domain Ontology for Personalized Knowledge Search and Recommendation

\*Yuh-Jen Chen, Associate Professor and Chairperson Department of Accounting and Information Systems National Kaohsiung First University of Science and Technology Kaohsiung, Taiwan, ROC

Yuh-Min Chen, Professor Institute of Manufacturing Information and Systems National Cheng Kung University Tainan, Taiwan, ROC

Hui-Chuan Chu, Associate Professor Department of Special Education National University of Tainan Tainan, Taiwan, ROC

Chung-Yueh Chao, Graduate Associate Institute of Manufacturing Information and Systems National Cheng Kung University

Corresponding author:

\*Yuh-Jen Chen, Ph.D.

Department of Accounting and Information Systems

National Kaohsiung First University of Science and Technology

Kaohsiung, Taiwan, ROC.

Email: yjchen@nkfust.edu.tw

Tel: +886-7-6011000 ext. 4316

Fax: +886-7-6011158

#

## Abstract

This paper presents research on the development of a system of domain ontology adaptation for personalized knowledge search and recommendation to adapt a suitable domain ontology according to previous browsing and reading behavior of users (i.e., usage history log). An adaptive domain ontology can satisfy the future requirements of users and promote use value. In developing the system, a domain ontology adaptation model is first designed. Based on the designed adaptation model, a methodology for domain ontology adaptation is developed. Subsequently, a domain ontology adaptation system is implemented with an illustrative example of securities trading. Finally, a system evaluation for user satisfaction and a methodology evaluation are conducted to demonstrate the developed methodology and system worked efficiently.

The results of this research facilitate personalized knowledge search and recommendation. They also promote the accuracy of domain ontology to satisfy the domain knowledge requirements of users, and consequently boost the use value of domain ontology.

Keywords: Personalization, Knowledge management, Ontology, Ontology adaptation

## 1. Introduction

Because of the vigorous development of the knowledge economy in the $2 1 ^ { \mathrm { s t } }$ century, knowledge has become the root for enterprises to maintain competitive advantage. Therefore, how to implement knowledge management effectively has become a crucial factor contributing to the operational success of an enterprise. However, successful knowledge management relies on constructing, applying, and knowledge formation and description in a specific domain [23][25][35][40][41] to enable enterprises to realize effective management and application of domain knowledge.

Recently, various methods using domain ontology have been developed [5][6][9][12][19][33][38][39][48][49][50]. Chen and Kuo (2000) proposed an adaptive information retrieval system embedded in an intelligent feedback tuning mechanism to capture the personal notions of query terms. Velardi et al. (2001) described OntoLearn, a text-mining tool devised to improve human productivity during the process of ontology construction. Navigli and Velardi (2004) presented a method and a tool, OntoLearn, aimed at the extraction of domain ontologies from web sites, and more generally from documents shared among the members of virtua organizations. Hyvönen et al. (2004) showed how the benefits of the view-based search method, developed within the information retrieval community, can be extended with ontology based search, developed within the Semantic Web community, and with semantic recommendations. Castells et al. (2005) presented a comprehensive personalized retrieval framework where the advantages of ontologies are exploited in different parts of the retrieval cycle: query-based relevance measures, semantic user preference representation, automatic preference update, and personalized result ranking. Rostami et al. (2008) proposed an ontology-based index (OI) to facilitate the query search on peer-to-peer (P2P) networks. Erozel et al. (2008) designed a video data model for a video storage format, and developed a natural language-based video searching method by utilizing semantic similarity computation. Cheung et al. (2009) developed an OWL-based Matseek federated search interface that integrates critical material science databases as the knowledge-searching basis of nanotechnologist studies for material scientists. Wang and Lin (2009) analyzed the user behavior characteristics on Internet and proved the feasibility for the user profile model built in search engine. Vesin et al. (2012) presented new approach to perform effective personalization highly based on Semantic web technologies performed in new version of the tutoring system, named Protus 2.0. This comprises the use of an ontology and adaptation rules for knowledge representation and inference engines for reasoning. Riaño et al. (2012) introduced an ontology for the care of chronically ill patients and

#

implemented two personalization processes and a decision support tool. The first personalization process adapts the contents of the ontology to the particularities observed in the health-care record of a given concrete patient, automatically providing a personalized ontology containing only the clinical information that is relevant for health-care professionals to manage that patient. The second personalization process uses the personalized ontology of a patient to automatically transform intervention

However, these recent studies have not reflected appropriate searching results according to the use requirements of individual users. This situation creates a bottleneck that is substantially lower the value of domain ontology reuse because the domain ontology cannot meet the requirements of individual users. Additionally, there are differences between construction and maintenance methods within the domain ontology [3][8][28]. Baneyx et al. (2005) utilized two methods of distributional analysis and recognition of semantic relationships to extract keywords from certain documents for constructing a medical ontology. Li and Ko (2007) developed a hierarchical clustering algorithm and used domain concepts selected by experts to build a food ontology based on a bottom-up system. Chen et al. (2008) collected domain-related web pages from the Internet, and selected keywords through HTML tags, to construct a domain ontology through web page analysis, singular vector decomposition, recursive adaptive resonance training network, and Boolean analysis. These related studies belong to one-time domain ontology construction or maintenance, and their representation models are all static structures. This type of representation model simplifies the complexity and difficulty of domain ontology construction and maintenance; however, it cannot accurately reflect the change in content of practical domain knowledge with the passage of time.

This paper develops a mechanism for domain ontology adaptation for personalized knowledge search and recommendation to adapt a suitable domain ontology according to the previous browsing and reading behavior of users (i.e. usage history log). The adaptive domain ontology can satisfy the future requirements of users, and thus promote the use value of domain ontology. The following tasks obtain the objective: (i) design a domain ontology adaptation model, (ii) develop a methodology for domain ontology adaptation, and (iii) implement and evaluate a domain ontology adaptation methodology and system. Steps involved in the design of the model for domain ontology adaptation include designing a model of adaptation factor analysis for domain ontology as well as establishing a usage context analysis model and personalized adaptation model for users. The methodology for domain ontology adaptation comprises adaptation factor analysis, user preference analysis, requirement-based concept clustering, and personalized adaptation.

#

The results of this work facilitate personalized knowledge search and recommendation and promote the accuracy of domain ontology to satisfy the domain knowledge requirements of users, and consequently boost the use value of domain ontology.

The remainder of this paper is organized as follows. Section 2 designs the adaptation model for domain ontology. Section 3 develops the methodology for domain ontology adaptation. Section 4 shows the results of implementing a prototype of a system for domain ontology adaptation and experiment with an application example. Section 5 provides conclusions and directions for future work.

## 2. Design of Domain Ontology Adaptation Model

This section designs an adaptation model for domain ontology, which involves a model for adaptation factor analysis, a context analysis model for users, and a personalized adaptation model. Each element is described as follows.

## 2.1 Adaptation Factor Analysis Model for Domain Ontology

Various context requirements and motivations generate diverse application interfaces and services in a user information system [24][26]. Hence, this study treats the usage context as the basis of use requirement of domain ontology.

Traditional use requirement of domain ontology must rely on the active input of users for judging the system [16]. Although, such domain ontology can accurately judge user requirements, but there is a lack of intelligent and real-time qualities for system operations. Moreover, it is easy to produce the error intention of use requirement for users who are not familiar with a certain application domain. Conversely, the usage history log records behavioral characteristics of users in an active, real-time, and objective way [16][22]. Therefore, this section induces the individual requirement and behavior of users through exploring literatures on the usage history log and using these results to conduct adaptation factors for domain ontology.

Information retrieval (IR) [22][42][47] is widely adopted as a search quality measure (SQM) to determine the search result satisfaction of users. This method analyzes the visited content and browsing time of users to judge whether the user is suitable for, or familiar with, that content. Then, how the user has used that content and the usage frequency are recorded to judge the importance of that content. Web mining [21][29] analyzes and computes the non-idle state of the user, and adjusts the weights of travel time and use action to validate that the content can meet use requirements. In marketing management [7], customer value analysis (CVA) goes beyond merely evaluating customer (user) satisfaction. It illustrates the “how” and “why” of customer (user) satisfaction, allowing you to pinpoint the changes needed for increasing market share and profit. Generally, CVA uses three elements as the value measurement of customers to determine valuable customers and their preferences. These three elements are recent consuming time (Recently, R), consuming frequency during a certain period (Frequency, F), and consuming amount during a certain period (Monetary Amount, M) respectively. Meanwhile, the recent consuming time (Recently, R) can be explained as the user’s attentive time to each ontology concept node, while the consuming frequency during a certain period (Frequency, F) can be explained as the visited times to each ontology concept node for a user. The consuming amount during a certain period (Monetary Amount, M) can be viewed as the number of instances that are mapped to each visited ontology concept node.

Based on the exploration of literatures given above, this study induced five ontology adaptation factors to facilitate the design of an adaptation factor analysis model for domain ontology, as listed in Table 1.

Table 1. Important Adaptation Factors for Domain Ontology from Literature

<table><tr><td>Adaptation Factor</td><td>Explanation</td></tr><tr><td>Visited Content (VC)</td><td>All visited ontology concept nodes from user</td></tr><tr><td>Travel Time (TT)</td><td>User&#x27;s attentive time to each ontology concept node</td></tr><tr><td>Requirement Quantity (RQ)</td><td>The number of instances that are mapped to each visited ontology concept node</td></tr><tr><td>Visited Frequency (VF)</td><td>The visited times to each ontology concept node</td></tr><tr><td>User Action (UA)</td><td>Usage of the knowledge content that is mapped to the visited ontology concept node from user</td></tr></table>

Based on the adaptation factors for domain ontology from Table 1, the adaptation factor analysis model for domain ontology is designed, as shown in Fig. 1. This proposed model has the following elements:

![](/api/attachments/T5YPFZH7/fulltext/images/f72351076d03c68a9324e334d0df58997fdfe566434a5ad12e4c6b9e5d6fdb00.jpg)  
Figure 1. Adaptation Factor Analysis Model for Domain Ontology

(i) Feature extraction: Based on user features in user profiles (including user name, age, education level, occupation, industry, and salary), the concept of entropy [10] is employed to compute the information gain of each user feature. Through the method, the user features with higher identification can be found to describe the various user features. These user features are then stored in the user features repository to facilitate the establishment of a usage context analysis model for users.

(ii) Usage history recording: The ontology usage histories of users are first derived from their application interfaces. Subsequently, their usage history logs are created to calculate the values of adaptation factors for domain ontology. These values are the significant basis for adapting domain ontology.

## 2.2 Usage Context Analysis Model of Users

Due to a diverse usage context in the requirements of users [13][27], this study established the usage context analysis model for domain ontology users to effectively represent the use requirements of users, as shown in Fig. 2. The usage context analysis model includes three portions, namely user preference analysis, requirement-based concept clustering, and user pattern formation. Each portion is explained as follows.

![](/api/attachments/T5YPFZH7/fulltext/images/a1f7c90cded94afa8e8a7a27cfaa1e6c4a621b122c1a50e382a463aad8c1c096.jpg)  
Figure 2. Usage Context Analysis Model for Domain Ontology Users

(i) User preference analysis: The user preference analysis involves two steps of usage history tracing and log path mapping, introduced below.

(a) Usage history tracing: This step obtains the preference of users to certain concept nodes in the domain ontology by tracing the use action of users and determining the values of adaptation factors from the usage history log.

(b) Log path mapping: This step maps the results from tracing usage history with the concept nodes from the domain ontology to transfer use action into a sequence formed with concept nodes of domain ontology. Then, this sequence is stored in the log paths of users to facilitate clustering for use requirement-based concepts.

(ii) Requirement-based concept clustering: The requirement-based concept clustering includes three steps, namely path association computing, domain ontology modeling, and use requirement range setting. Each step is described below.

(a) Path association computing: Based on the acquired sequence in log path mapping, the association support and the confidence among concepts in the domain ontology are obtained by using association rule mining [43].

(b) Domain ontology modeling: Based on the results from path association computing as well as path length and path depth of domain ontology, the domain ontology is modeled through social network [14]. The social network-based domain ontology can obviously represent one specific concept node cluster and the relation strengths among these concepts, while the user is using the domain ontology.

(c) Use requirement range setting: According to concepts in the social network-based domain ontology, hierarchical clustering [18][45] is conducted to cluster these concepts. The clustering results are treated as the use requirement range for domain ontology users. However, this use requirement range changes based on the usage history log to promptly present the variances in use requirement of domain ontology.

(iii) User pattern formation: The user pattern describes the requirement detail of using the domain ontology. The results from the requirement-based concept clustering are used to match with user features to form a user pattern. Subsequently, the association rules determine the support degree of user pattern formation. Finally, the support degree of user pattern formation is used to evaluate if the user pattern meets the threshold value of user pattern formation. The qualified user pattern is stored in the user pattern library.

## 2.3 Personalized Adaptation Model

Based on the adaptation factor analysis model for domain ontology in Section 2.1 and the usage context analysis model in Section 2.2, this section establishes the personalized adaptation model to help users obtain an appropriate user pattern, shown in Fig. 3. This personalized adaptation model includes two portions of user confirmation and pattern recommendation. Each portion is discussed as follows.

![](/api/attachments/T5YPFZH7/fulltext/images/062ee42cba74a67fe3f5f06951ad49dfc8ac1a84f5859a5435b4c12208d74672.jpg)  
Figure 3. Personalized Adaptation Model

(i) User confirmation: The user confirmation judges whether the user is a new user according to the user history log and the user profile. If the user is a new user, the user preference analysis is performed. Conversely, the user information is first imported from the user profiles repository. Then, the user preference analysis is executed to generate a user log path.

(ii) User pattern recommendation: The user pattern recommendation comprises two steps of pattern mapping and pattern projection, introduced as follows.

(a) Pattern mapping: Pattern mapping matches user log paths with the user pattern library to find out similar user patterns. Subsequently, the confidence values from similar user patterns are ranked.

(b) Pattern projection: By utilizing the results of user preference analysis and user patterns, the preference degree and requirement range of domain ontology usage for the individual user are represented respectively. Through combining with the domain ontology, the personalized domain ontology is projected and recommended to users. This personalized domain ontology is adopted to build or update the user profile. Based on the user profile, the support degree of user pattern formation can be calculated to consider if this user pattern meets the threshold value of user pattern formation. If the user pattern satisfies the threshold value, it is stored in the user pattern library as the recommended basis of user pattern for all users.

Additionally, domain ontology provides essential terms and correlative forms in the specific areas which can be identified by the computer. It is intended to enable the machine to reach a consensus on the related or similar terms [34][46]. The following five steps are provided to construct the domain ontology:

(1) Determine the scope and purpose of the domain ontology

This stage clarifies the aim, the scope, and the function which the domain ontology are constructed. The domain ontology adaptation provides certain semantic help to improve the efficiency of information retrieval. Thus, the semantic relationship of the concept should be provided as much as possible to improve the ontology-based information service.

(2) Collect and analyze the domain information

When the domain information and understanding the domain knowledge were fully collected, it is able to construct an available and correct ontology with sufficient amount of information. To construct the domain ontology with the versatility, the contents of the domain ontology have the authority and standards, and its terms must have the accuracy and completeness.

(3) Define the classes and the class hierarchy

A top-down approach was applied to construct the domain ontology, which first defines the most general concepts in the domain, and then gradually subsequent specialization of the concepts.

#

## (4) Define the properties of classes

Once some of the classes were identified, the properties of classes must be described. Initially, it is important to get a comprehensive list of terms between concepts they represent, relations among the terms, or any property that the concepts may have. These terms contain object properties and data-type properties. All the subclasses inherit the properties of the classes.

## (5) Create instances

Defining an individual instance of a class requires choosing a class, creating an individual instance of that class, and filling in the slot values.

## 3. Development of Domain Ontology Adaptation Methodology

Based on the designed domain ontology adaptation model in Section 2, this section constructs the procedure and the methodology for domain ontology adaptation. The methodology includes adaptation factor analysis, user preference analysis, requirement-based concept clustering and personalized adaptation, discussed in the following subsections.

## 3.1 Domain Ontology Adaptation Procedure for Personalized Knowledge Search and Recommendation

By integrating the adaptation factor analysis in Section 2.1, the model for usage context analysis in Section 2.2, and the personalized adaptation model in Section 2.3, the procedure of domain ontology adaptation is constructed to facilitate development of the method of domain ontology adaptation for personalized knowledge search and recommendation. As shown in Fig. 4, the procedure for domain ontology adaptation consists of domain ontology adaptation factor analysis, usage context analysis, and personalized adaptation.

##

![](/api/attachments/T5YPFZH7/fulltext/images/f13437c4a25db9b8402d38cb4c7258170c1ce438ac24dd58bb794b89447be797.jpg)  
Figure 4. Domain Ontology Adaptation Procedure for Personalized Knowledge Search and Recommendation

## 3.2 Adaptation Factor Analysis Method

Two parts in domain ontology adaptation factor analysis include feature extraction and usage history recording of users, introduced below.

(i) Feature extraction: Feature extraction uses entropy to calculate the information gain [43] for each user feature based on user features in the user profiles. The user features with higher identification describe the difference of user features, and are stored in the user features repository. Equation (1) presents the formula for entropy.

$$
\operatorname{Entropy} (t) = - \sum_ {i = 0} ^ {c - 1} p (i \mid t) \log_ {2} p (i \mid t)\tag{Equation (1}
$$

where c denotes the number of events and $p ( i \mid t )$ denotes the probability for the i-th type user feature value appearing under the t-th user feature; the smaller entropy value represents the higher user difference under that user feature.

(ii) Usage history recording: According to the domain ontology adaptation factors defined in Section 2.1 and the object-oriented representation [4], the structure of the usage history log for the user is designed, shown in Fig. 5. For the user actions in the designed structure of the usage history log, the user action level and type is then defined by observing knowledge use behavior for users [16][22] to accurately analyze the adaptation information in the usage history log. As shown in Table 2, the action level can be classified into four levels, namely “Important”, “Preferable”, “Careless” and “Useless”. Accounting to the defined action levels and action types, the weightiness of action type can be ranged between -3 and 6. Lastly, the action worth each time is obtained by calculating the weighted mean for user actions and travel time. The formula for the weighted mean is shown in Eq. (2).

$$
A W _ {i} = A _ {1} \cdot \frac {T _ {1} ^ {\prime}}{T _ {\text { Summary }}} + A _ {2} \cdot \frac {T _ {2} ^ {\prime}}{T _ {\text { Summary }}} + \dots + A _ {n} \cdot \frac {T _ {n} ^ {\prime}}{T _ {\text { Summary }}} \quad \text { Equation(2) }
$$

where $A _ { n }$ is the weightiness of n-th action in user actions;

$T _ { s u m m a r y }$ is the total browsing time of users;

$T _ { n } ^ { \prime }$ is the active time spent by the n-th user action in user’s total browsing time $T _ { s u m m a r y }$

![](/api/attachments/T5YPFZH7/fulltext/images/a409974342c09cdf343ddc7e72ecdef2d090203d249a6acad87b8971c0bd4400.jpg)

<sub>n</sub>T is the ratio of the active time spent by the user for $n { - } t h$ <sub>Summary</sub>T user action in user’s total browsing time $T _ { s u m m a r y }$ that

![](/api/attachments/T5YPFZH7/fulltext/images/cec769b4e8e006f738fdd25d4f872626aff1394dbbcbea4f37dcb7c42d8dc60b.jpg)  
Figure 5. The Structure of User’s Usage History Log

Table 2. User Action Level

<table><tr><td>Action Level</td><td>Description</td><td>Action Type</td><td>Weightiness</td></tr><tr><td rowspan="3">Important</td><td rowspan="3">Users believe the concept is very important</td><td>Download</td><td>6</td></tr><tr><td>Print</td><td>5</td></tr><tr><td>Communicate</td><td>4</td></tr><tr><td rowspan="3">Preferable</td><td rowspan="3">Users prefer to the concept</td><td>Read</td><td>3</td></tr><tr><td>Scan</td><td>2</td></tr><tr><td>Search</td><td>1</td></tr><tr><td rowspan="2">Careless</td><td rowspan="2">Users care about the concept slightly</td><td>Skip</td><td>0.1</td></tr><tr><td>Idle</td><td>-1</td></tr><tr><td rowspan="2">Useless</td><td rowspan="2">The concept does not match users&#x27; requirements</td><td>Cancel</td><td>-2</td></tr><tr><td>Abandon</td><td>-3</td></tr></table>

NOTE: Higher weightiness value indicates the user has higher use requirement or preference to a certain concept node

In calculating the weighted mean through Eq. (2), an unlimited increase in user actions would cause an unlimited extension of the computational process. In such a case, the numerical range of computing the action worth of a user would be unlimited. Therefore, this study used the e-logistic model [1][2][17] with restricted growth to conquer the unlimited growth problem of user actions. The equation of the e-logistic model is defined as Eq. (3).

$$
f (t) = \frac {a}{1 + b e ^ {- k t}}
$$

Equation (3)

where a, b and k are positive constants. Meanwhile, the constant a is the limit to growth, while the constants b and k are appropriately chosen real numbers. These constants are used for adjusting the suitability of the e-logistic model.

To specify the practical application of the aforementioned method, Fig. 6 illustrates an example of securities trading ontology.

![](/api/attachments/T5YPFZH7/fulltext/images/60d5ca0c093b863114157a82cff962939cd80928136b01ad52e8ae2e4249f5e0.jpg)  
Figure 6. Securities Trading Ontology

Suppose there is one user searching for stock knowledge in the securities trading ontology (Fig. 6), the created usage history log records that that the user has browsed the concept “Stock\_Exchange” and its sub-concept “Opening\_Quotation”. Meanwhile, the total browsing time for the concept “Stock\_Exchange” is 90 seconds, including 37 seconds for the user action “Read”, 20 seconds for the user action “Scan”, 15 seconds for the user action “Skip”, and 18 seconds for the user action “Idle”; while the total browsing time for the concept “Opening\_Quotation” is 70 seconds, including 60 seconds for the use actions “Read” and “Download”, and 10 seconds for the use action “Idle”.

According to the above-mentioned usage history log, the action worth of users for the concept “Stock\_Exchange” and its sub-concept “Opening\_Quotation” are respectively calculated as below:

‧The action worth of users for the concept “Stock\_Exchange”:

$$
A W _ {1} = 3 \cdot \frac {3 7}{9 0} + 2 \cdot \frac {2 0}{9 0} + 0. 1 \cdot \frac {1 5}{9 0} + (- 1) \cdot \frac {1 8}{9 0} = 1. 2 3 + 0. 4 4 + 0. 0 2 - 0. 2 = 1. 4 9
$$

‧The action worth of users for the concept “Opening\_Quotation”:

$$
A W _ {2} = (6 + 3) \cdot \frac {6 0}{7 0} + (- 1) \cdot \frac {1 0}{7 0} = 7. 7 1 - 0. 1 4 = 7. 5 7
$$

Because there is no specific numerical range for the aforementioned action worth calculations, the numerical range of action worth calculation is limited in the interval [0, 1] (i.e., the value of constant a is set as 1) by Eq. (3). The adjusted equation of action worth is shown in Eq. (4).

$$
A W ^ {\prime} = \frac {1}{1 + b \cdot e ^ {- 1 \times t}}
$$

Equation (4)

where the constant b represents the number of use actions, while t represents the original action worth of users, such as $A W _ { 1 }$ and $A W _ { 2 }$

‧The adjusted action worth of users for the concept “Stock\_Exchange”:

$$
A W _ {1} ^ {\prime} = \frac {1}{1 + 4 \cdot e ^ {- 1 * 1 . 4 9}} = 0. 5 2 5 9 (a = 1, b = 4, k = 1)
$$

‧The adjusted action worth of users for the concept “Opening\_Quotation”:

$$
A W _ {2} ^ {\prime} = \frac {1}{1 + 3 \cdot e ^ {- 1 * 7 . 5 7}} = 0. 9 9 8 4 (a = 1, b = 3, k = 1)
$$

## 3.3 Usage Context Analysis

Usage context analysis involves user preference analysis and requirement-based concept clustering. The former includes usage history tracing and log path mapping, while the latter includes path association computation, domain ontology modeling, and use requirement range setting. These techniques are developed as follows.

## 3.3.1 User Preference Analysis

(i) Usage history tracing: Based on the usage history log, the usage history of users is traced to acquire the adaptation factors of the used knowledge concept from the single use requirement of users. These acquired adaptation factors are stored in an attribute-relation file format (ARFF) [52].

(ii) Log path mapping: The above action worth of users and three adaptation factors (including visited content (VC), visited frequency (VF), and requirement quantity (RQ)) obtained from the usage history tracing are compiled. Based on the compiled results, the RFM model [7] is adopted to conduct comprehensive analysis of adaptation factors to obtain user preference values to the concepts of domain ontology.

In the above comprehensive analysis of adaptation factors using the RFM model, the obtained preference values might experience unlimited grown without numerical range limitations or not possess any analytic meaning because the influence of a single index is greater than other indexes. Consequently, this study modified the numerical ranges of the adaptation factors “visited frequency (VF)” and “requirement quantity (RQ)” using the e-logistic model [1][2][17] with the characteristic of restricted growth, as below.

(a) Visited frequency (VF): To set the value of visited frequency within the interval [1/3,1], the value of constant a in the e-logistic model is set to 1. Additionally, due to the numerical range of average frequency prior to a smaller adjustment, the values derived from the e-logistic model are all close to 1, making it impossible to compare them. Hence, this study adjusted the e-logistic model from visited frequency (VF). The adjusted equation is shown in Eq. (5).

$$
V F ^ {\prime} = \frac {1}{1 + 2 \cdot e ^ {- 2 R \times A v e r a g e F r e q u e n c y}}\tag{Equation (5}
$$

where R=latest application time/average application time; Average Frequency=concept used time/user actions;

(b) Requirement quantity (RQ): The parametric value of requirement quantity from the usage history log is decided according to the quantity of existing instances; the variable range of requirement quantity is greater than other adaptation factors. This study applied the hyperbolic tangent function tanh(t) (Eq. (6)) to solve the problem of gathering around the limit value for all the calculated values from the requirement quantity. Equation (7) presents the adjusted formula for requirement quantity.

$$
f (t) = \frac {e ^ {k t} - e ^ {- k t}}{e ^ {k t} + e ^ {- k t}}\tag{Equation (6}
$$

$$
R Q ^ {\prime} = \frac {e ^ {2 \times \text { QuantityRate }} - e ^ {- 2 \times \text { QuantityRate }}}{e ^ {2 \times \text { QuantityRate }} + e ^ {- 2 \times \text { QuantityRate }}}\tag{Equation (7}
$$

where Quantity Rate=used instance quantity for a concept/used instance quantity for a usage history log;

According to the above adjusted comprehensive analysis indexes $A W ^ { \prime } , \ V F ^ { \prime }$ and $R Q ^ { \prime }$ for user preference, the comprehensive analysis model for the adaptation factor is designed using the RFM model, shown in Fig. 7. The $X { - } A x i s , \ Y { - } A x i s ,$ and $Z { - } A x i s$ represent three indexes $A W ^ { \prime } , \ V F ^ { \prime }$ and $R Q ^ { \prime }$ respectively, while the coordinate $( \mathrm { V a l u e } _ { A W } ,$ , Value<sub>VF’</sub>, $\mathrm { V a l u e } _ { \mathrm { R } Q ^ { \prime } } )$ ) represents the value of the adaptation factor. The distance between one coordinate and the origin indicates the value of user preference to a certain concept. The longer distance expresses the higher preference value; on the contrary, the shorter distance expresses the lower preference value.

![](/api/attachments/T5YPFZH7/fulltext/images/7214637b740bf1aeea223ffb62cda0c605cd53b3177291b133595c7cc294c189.jpg)  
Figure 7. Comprehensive Analysis Model for the Adaptation Factor

Based on the comprehensive analysis model for the adaptation factor and the visited content of users, one sequence composed of concept nodes is created to represent the user log path, shown in Eq. (8).

$$
\begin{array}{l} \text {Sequence} _ {\text {user\_id}} ^ {i} \\ = ((\text {Concept\_Name} _ {1}, p _ {1}), (\text {Concept\_Name} _ {2}, p _ {2}), \dots , (\text {Concept\_Name} _ {n}, p _ {n})) \end{array}
$$

Equation (8)

where i denotes the i-th time visited content;

user\_id denotes a certain user;

Concept $N a m e _ { n }$ denotes the $n { - } t h$ concept in the i-th time visited content from a certain user;

$p _ { n }$ denotes user preference value to a certain concept;

An example of securities trading ontology in Fig. 6 illustrates the application of user preference analysis, as follows:

Assume that the latest application time to the concept “Stock\_Exchange” from user A is 75 seconds, the average application time is 100 seconds, the ratio R of the latest application time to the average application time is 0.75, and the average frequency is 0.3, then the adjusted visited frequency $V F ^ { \prime }$ is calculated as:

$$
V F ^ {\prime} = \frac {1}{1 + 2 \cdot e ^ {- 2 * 0 . 7 5 * 0 . 3}} = 0. 4 3 9 5
$$

Suppose user A uses the sub-concept “Open\_Quotation” for the first time, thus, there are no records related to the latest application time, the average application time, and the average frequency. The adjusted visited frequency $V F ^ { \prime }$ is calculated as: $V F ^ { \prime } { = } \frac { 1 } { 1 { + } 2 { \cdot } e ^ { - 2 { * } 0 { * } 0 } } { = } 0 . 3 3$

Finally, suppose user A uses 7 and 15 documents for the concept “Stock\_Exchange” and its sub-concept “Open\_Quotation” respectively, then their quantity rates are determined as 0.32 and 0.68. Using Eq. (7), the adjusted requirement quantity $R Q ^ { \prime }$ is derived below.

‧The adjusted requirement quantity for the concept “Stock\_Exchange”:

$$
R Q ^ {\prime} = \frac {e ^ {2 * 0 . 3 2} - e ^ {- 2 * 0 . 3 2}}{e ^ {2 * 0 . 3 2} + e ^ {- 2 * 0 . 3 2}} = 0. 5 6 4 9
$$

‧The adjusted requirement quantity for the concept “Opening\_Quotation”:

$$
R Q ^ {\prime} = \frac {e ^ {2 * 0 . 6 8} - e ^ {- 2 * 0 . 6 8}}{e ^ {2 * 0 . 6 8} + e ^ {- 2 * 0 . 6 8}} = 0. 8 7 6 4
$$

For the above results of $A W ^ { \prime } , V F ^ { \prime }$ and $R Q ^ { \prime }$ for the concept “Stock\_Exchange” and its sub-concept “Opening\_Quotation”, the user preference values of these two concepts can be determined through the comprehensive analysis model for the adaptation factor, calculated in the following:

‧The user preference value to the concept “Stock\_Exchange”:

Preference of Concept “Stock\_Exchange” :

(0.5259, 0.4395, 0.5649)

$$
\mathrm{P} _ {1} = \sqrt {0 . 5 2 5 9 ^ {2} + 0 . 4 3 9 5 ^ {2} + 0 . 5 6 4 9 ^ {2}} = 0. 8 8 8 2
$$

‧The user preference value to the concept “Opening\_Quotation”:

![](/api/attachments/T5YPFZH7/fulltext/images/c70bc46d88d507a3275d92df3814fb3509af98b5c1f133094afd190b8e1821b9.jpg)

$$
\mathrm{P} _ {2} = \sqrt {0 . 9 9 8 4 ^ {2} + 0 . 3 3 3 3 ^ {2} + 0 . 8 7 6 4 ^ {2}} = 1. 3 6 9 7
$$

According to the calculated results of preference value, user A demonstrates higher preference to the concept “Opening\_Quotation” than to the concept

$$
\text { Sequence } _ {\text { userA }} ^ {1} = ((\text { Stock\_Exchange }, 0. 8 8 8 2), (\text { Opening\_Quotation }, 1. 3 6 9 7))
$$

## 3.3.2 Requirement-based Concept Clustering

In Section 3.3.1, the concept order relationship of sequence represents the use requirement of domain ontology and the relation between concepts in user preference. Therefore, this subsection clusters the concepts with higher usage relationship from all sequences and treats the clustering results as use requirements. The developmental procedure is detailed as follows.

(i) Path association computation: The relationship between concepts is regarded as the use rule of domain ontology. Applying the association rule mining determines the confidence and support of associated concepts. The confidence decides whether the associated degree of the use rule is high or low, while the support decides whether the associated concept is widely used by the user. The equations of confidence and support are defined as Eqs. (9) and (10) respectively.

$$
\begin{array}{c} \text {Confidence} (X \Rightarrow Y) = P (X \cup Y) \\ \text {Support} (X \Rightarrow Y) = P (X / Y) \end{array}
$$

Equation (9)

Equation (10)

where X and Y are concepts.

(ii) Domain ontology modeling: To enhance accuracy for the confidence and support, the concept similarity matching method [31] is used to calculate the path length and depth between the concepts of domain ontology. Subsequently, the e-logistic model is used to adjust the path length and depth between concepts, shown in Eqs. (11) and Eq. (12).

$$
f _ {l e n g t h} (l) = e ^ {- \alpha \cdot l}
$$

Equation (11)

$$
f _ {d e p t h} (d) = \frac {e ^ {\beta \cdot d} - e ^ {- \beta \cdot d}}{e ^ {\beta \cdot d} + e ^ {- \beta \cdot d}}
$$

Equation (12)

where l is the path length between concepts;

d is the same path depth between concepts;

$\alpha$ and $\beta$ are appropriately chosen real numbers, which are used for adjusting the path length and depth between concepts;

The above path length and depth between concepts and the association confidence value between concepts can be represented as a coordinate through the comprehensive analysis model introduced in Subsection 3.3.1. Based on the coordinate, the distance between the coordinate and the origin is determined to accurately represent the practical association degree between concepts, depicted in Fig. 8.

![](/api/attachments/T5YPFZH7/fulltext/images/f9bd6eb1defd8609851eb0889cb1c41b6b04d5dc574b130ec5e96787c354df04.jpg)  
Figure 8. Practical Association Degree between Concepts

(iii)Use requirement range setting: The practical association degree between concepts from domain ontology modeling is conducted to compute the association between all concepts in domain ontology to obtain distance values (distance formula) between each concept and other concepts. Table 3 lists the computation results for 9 concepts taken from the example of securities trading ontology in Fig. 6.

Table 3. Practical Association Degrees between Concepts in the Securities Trading Ontology

<table><tr><td>Concept No. &amp; Name</td><td>1. Stock_Market</td><td>2. Secondary_Market</td><td>3. Circulation_Market</td><td>4. Stock_Exchange</td><td>5. Share</td><td>6. Share_Right</td><td>7. Ordinary_Stock</td><td>8. Opening_Quotation</td><td>9. Ending_Quotation</td></tr><tr><td>1. Stock_Market</td><td></td><td>0.41</td><td>0.91</td><td>1.26</td><td>0.32</td><td>0.27</td><td>1.01</td><td>0.58</td><td>0.49</td></tr><tr><td>2. Secondary_Market</td><td>0.41</td><td></td><td>0.76</td><td>0.18</td><td>0.12</td><td>1.50</td><td>1.49</td><td>0.89</td><td>0.97</td></tr><tr><td>3. Circulation_Market</td><td>0.91</td><td>0.76</td><td></td><td>1.43</td><td>1.33</td><td>0.74</td><td>0.88</td><td>1.21</td><td>0.10</td></tr><tr><td>4. Stock_Exchange</td><td>1.26</td><td>0.18</td><td>1.43</td><td></td><td>0.71</td><td>0.65</td><td>0.61</td><td>1.39</td><td>0.99</td></tr><tr><td>5. Share</td><td>0.32</td><td>0.12</td><td>1.33</td><td>0.71</td><td></td><td>1.24</td><td>0.13</td><td>0.23</td><td>0.15</td></tr><tr><td>6. Share_Right</td><td>0.27</td><td>1.50</td><td>0.74</td><td>0.65</td><td>1.24</td><td></td><td>1.58</td><td>0.26</td><td>0.19</td></tr><tr><td>7. Ordinary_Stock</td><td>1.01</td><td>1.49</td><td>0.88</td><td>0.61</td><td>0.13</td><td>1.58</td><td></td><td>0.17</td><td>0.55</td></tr><tr><td>8. Opening_Quotation</td><td>0.58</td><td>0.89</td><td>1.21</td><td>1.39</td><td>0.23</td><td>0.26</td><td>0.17</td><td></td><td>1.12</td></tr><tr><td>9. Ending_Quotation</td><td>0.49</td><td>0.97</td><td>0.10</td><td>0.99</td><td>0.15</td><td>0.19</td><td>0.55</td><td>1.12</td><td></td></tr></table>

According to the practical association degrees between concepts in Table 3, the proximities between each concept and other concepts can be determined by Eq. (13) [18][43]. Decreased ranking of these proximities generates the hierarchical clustering result, presented in Fig. 9.

$$
\text { proximity } (C _ {i}, C _ {j}) = \frac {\sum_ {x \in c _ {i} , y \in c _ {j}} \text { proximity } (x , y)}{m _ {i} \cdot m _ {j}} \quad \text { Equation   (13) }
$$

where $C _ { i }$ or $C _ { j }$ indicate the concept clustering;

x indicates the node in the concept clustering $C _ { i } ;$

$y$ indicates the node in the concept clustering $C _ { j } ;$

$m _ { i }$ indicates the number of nodes in the concept clustering $C _ { i } ;$

$m _ { j }$ indicates the number of nodes in the concept clustering $C _ { j }$ ;

![](/api/attachments/T5YPFZH7/fulltext/images/f54eda653e9a9f8cacf5035495780ce793443817c5eafb2e39d90b7542a796b0.jpg)  
Figure 9. Hierarchical Clustering of Practical Association between Concepts

The above hierarchical clustering method clusters concepts in the domain ontology based on the preference and requirement of user action. In hierarchical clustering, each concept clustering possesses the same or similar use requirement. As shown in Fig. 9, the use requirements from the bottom level are a gathering of two concepts and the expression is shown in $E q . \ ( l 4 ) .$ . The use requirements from the upper levels are a gathering of a use requirement from the bottom level and the other concept or use requirement, and their expressions are shown in Eqs. (15) and (16) respectively. Figure 10 shows the clustered securities trading ontology.

$$
\text { Use   Requirement } _ {i} = \{C _ {i}, C _ {j} \}
$$

Equation (14)

$$
\text { Use   Requirement } _ {i + 1} = \{C _ {k}, \text { Use   Requirement } _ {i} \}
$$

Equation (15)

$$
\mathbf {t} _ {i + 3} = \{\text { Use   Requirement } _ {i + 2}
$$

Equation (16)

![](/api/attachments/T5YPFZH7/fulltext/images/47383acd32c96eb4688e1d813927f7933cf6d44e692bf805e658a3a5ef68c710.jpg)  
Figure 10. Clustered Securities Trading Ontology

## 3.4 Personalized Adaptation Method

The personalized adaptation method involves user pattern formation, pattern mapping, and pattern projection, described below.

(i) User pattern formation: The use requirement of users obtained from Subsection 3.3.2 is matched with user features obtained from Section 3.2. The association rule mining [30][44] are then employed to calculate the confidence and support for the matching results (Eqs. (9) and (10)). Based on these calculated results of confidence and support, the matching rules with higher confidence that pass the threshold of support are identified and defined as the user pattern. As shown in Fig. 11, the user pattern can be classified into three types. The first type of user pattern represents specific concepts used by a specific user, while the second type of user pattern represents specific concept clusterings used by a specific user. The third type of user pattern represents the use requirements with higher association in the domain ontology. The establishment of matching rule for each type is described as below.

![](/api/attachments/T5YPFZH7/fulltext/images/a7ac8ff88669777cebe05d22d4ebd939a2b433f9df8c2dd87f8ed20cea50d010.jpg)  
Figure 11. User Pattern Types

(a) User pattern type 1 (user↔concept): The matching rule is built by a user and his/her use concepts.

(b) User pattern type 2 (user↔use requirement): The matching rule is built by a user and his/her use requirements.

(c) User pattern type 3 (use requirement↔use requirement): The matching rule is built by use requirements with higher association.

(ii) Pattern mapping: Using the domain ontology, the used concepts are compared with user patterns in the user pattern library to find user patterns with higher association to the use requirement of users. User patterns can help users acquire suitable content in the domain ontology.

(iii) Pattern projection: User preference gained from Subsection 3.3.1 is mapped with the results gained from pattern mapping to represent user preference to each concept. Based on the preference ranking of users for each concept, the preference order for domain ontology contents is conducted. As the example of securities trading ontology in Fig. 6, Table 4 displays the preference values for each concept for user A, while Table 5 displays the results of personalized adaptation for user A.

Through the method developed above, the partial suitable domain ontology is projected to satisfy the various requirements of users in the domain ontology, and to ultimately increase the use value of domain ontology.

Table 4. Preference Values for each Concept from User A

<table><tr><td>UserA</td><td>UserNameConcept</td></tr><tr><td>0.89</td><td>Stock_Market</td></tr><tr><td>--</td><td>Circulation_Market</td></tr><tr><td>--</td><td>OTC_Market</td></tr><tr><td>--</td><td>Primary_Market</td></tr><tr><td>--</td><td>Secondary_Market</td></tr><tr><td>--</td><td>Stock_Exchange_Market</td></tr><tr><td>0.52</td><td>Stock_Exchange</td></tr><tr><td>1.37</td><td>Opening_Quotation</td></tr><tr><td>0.61</td><td>Ending_Quotation</td></tr><tr><td>0.72</td><td>Stock</td></tr><tr><td>0.68</td><td>Share_Rights</td></tr><tr><td>--</td><td>Shares</td></tr><tr><td>--</td><td>Commercial_Paper</td></tr><tr><td>--</td><td>Government_Bond</td></tr><tr><td>--</td><td>Corporate_Bond</td></tr><tr><td>--</td><td>Originary_Stock</td></tr><tr><td>--</td><td>Preferred_Stock</td></tr><tr><td>--</td><td>Share_Issue</td></tr></table>

Table 5. Personalized Adaptation Results for User A

<table><tr><td>Sorting</td><td>Concept Name</td><td>Preference</td><td>User Pattern</td><td>Confidence</td></tr><tr><td>1</td><td>Opening_Quotation</td><td>1.3697</td><td>Null</td><td>Null</td></tr><tr><td>2</td><td>Stock_Market</td><td>0.8882</td><td>Null</td><td>Null</td></tr><tr><td rowspan="2">3</td><td rowspan="2">Stock</td><td rowspan="2">0.7205</td><td>Stock→Stock_Exchange</td><td>0.17</td></tr><tr><td>Stock→Share_Rights</td><td>0.17</td></tr><tr><td>4</td><td>Share_Rights</td><td>0.6811</td><td>Share_Rights→Stock</td><td>0.56</td></tr><tr><td>5</td><td>Ending_Quotation</td><td>0.6130</td><td>Null</td><td>Null</td></tr><tr><td>6</td><td>Stock_Exchange</td><td>0.5259</td><td>Stock_Exchange→Stock</td><td>0.34</td></tr></table>

## 4. System Implementation with a Case Study

Based on proposed techniques for domain ontology adaptation, this section presents a system for domain ontology adaptation for personalized knowledge search and recommendation. The implementation environment, results of a security trading case, an experimental analysis for methodology evaluation, and a system evaluation for user satisfaction are described in the following subsections.

## 4.1 Implementation Environment

This study implemented a prototype of the domain ontology adaptation at the Knowledge Engineering and Management Laboratory at National Kaohsiung First University of Science and Technology. The implementation environment was as follows. Computer hardware consisted of a Pentium CPU 3.0 GHz PC. Software was Microsoft Windows XP SP3, Apache 2.2.14 (IPV6 enabled), My SQL 5.1.41, and PHP 5.3.1. Figure 12 illustrates the framework of the domain ontology adaptation system, which includes three layers of user service, business service, and knowledge service. Figure. 13 shows the configuration of the entire domain ontology adaptation system.

![](/api/attachments/T5YPFZH7/fulltext/images/9c74d03e78e65426f9f660acf0a5d0129db6dda34f970a99cd564100fad54b6f.jpg)  
Figure 12. Framework of the Domain Ontology Adaptation System

![](/api/attachments/T5YPFZH7/fulltext/images/f7643fb93ae7ede3fc55da702a38e8389c7900672804dfc20fdc7c7ceb90f419.jpg)  
Figure 13. Organization of the Domain Ontology Adaptation System

## 4.2 Implementation Results

This section adopts the example of securities trading ontology in Fig. 6 to explain the implementation results of the system of domain ontology adaptation for personalized knowledge search and recommendation. Figure 14 shows the screen of the securities trading knowledge sharing system, while Fig. 15 lists the results of usage history tracing for user A from 03/22/2010 to 04/13/2010. Figures 16 and 17 present the results of feature extraction and log path mapping for user A. Meanwhile, the feature extraction includes age range, join data, education level, occupation, industry, and salary range. Figures 18 and 19 summarize the results of path association and use requirement range setting for user A. Finally, Figs. 20 and 21 depict the results of personalized adaptation and securities trading knowledge search and recommendation for user A. The results describe that user A’s preference for knowledge concepts includes “Opening\_Quotation”, “Stock\_Market”, “Stock”, “Ending\_Quotation” and “Stock\_Exchange”, and the recommended knowledge include articles of “European shares edge lower after Alcoa results”, “Employee stock

![](/api/attachments/T5YPFZH7/fulltext/images/656391a3349f3f3030b7068b3a72ce6466caaf90e358838a97d07bbe9d15e621.jpg)  
Figure 14. Securities Trading Knowledge Sharing System Interface

![](/api/attachments/T5YPFZH7/fulltext/images/a9f443cb2ad12b3f3053da092c4a5e4f69d8475c7a77c051a01daaf39f542ef8.jpg)  
Figure 15. Results of Usage History Tracing for User A

![](/api/attachments/T5YPFZH7/fulltext/images/bba032df7a7736f9c1e5a3ec7fd9f78648faad6f907790b3fecf0566b005fe7c.jpg)  
Figure 16. Results of Feature Extraction for User A

![](/api/attachments/T5YPFZH7/fulltext/images/242c71dafebdd29955c2d26c16a4f6b8874e4951fe92521a73b13b8e254caddc.jpg)  
Figure 17. Results of Log Path Mapping for User A

![](/api/attachments/T5YPFZH7/fulltext/images/226ad52bed0f5f79b6dd9396467aaa6c2022e7304bbfa72bfae0f471bbfa73be.jpg)  
Figure 18. Results of Path Association Computation for User A

<table><tr><td></td><td>Stock_Market</td><td>Circulation_Market</td><td>OTC_Market</td><td>Primary_Market</td><td>Secondary_Market</td><td>Stock_Exchange_Market</td><td>Stock_Exchange</td><td>Opening_Quotation</td><td>Ending_Quotation</td><td>Stock</td><td>Share_Rights</td><td>Shares</td><td>Commercial_Paper</td><td>Government_Bond</td><td>Corporate_Bond</td><td>Originary_Stock</td><td>Preferred_Stock</td><td>Share_Issue</td></tr><tr><td>Stock_Market</td><td>---</td><td>0.87</td><td>0.88</td><td>0.87</td><td>0.87</td><td>0.75</td><td>0.69</td><td>0.6</td><td>0.54</td><td>0.79</td><td>0.66</td><td>0.56</td><td>0.63</td><td>0.64</td><td>0.69</td><td>0.54</td><td>0.54</td><td>0.6</td></tr><tr><td>Circulation_Market</td><td>0.87</td><td>---</td><td>0.76</td><td>0.73</td><td>0.75</td><td>0.62</td><td>0.63</td><td>0.47</td><td>0.47</td><td>0.66</td><td>0.54</td><td>0.47</td><td>0.58</td><td>0.54</td><td>0.58</td><td>0.61</td><td>0.47</td><td>0.47</td></tr><tr><td>OTC_Market</td><td>0.88</td><td>0.74</td><td>---</td><td>0.73</td><td>0.73</td><td>0.63</td><td>0.59</td><td>0.49</td><td>0.48</td><td>0.7</td><td>0.55</td><td>0.47</td><td>0.54</td><td>0.59</td><td>0.55</td><td>0.48</td><td>0.47</td><td>0.49</td></tr><tr><td>Primary_Market</td><td>0.87</td><td>0.73</td><td>0.73</td><td>---</td><td>0.73</td><td>0.73</td><td>0.62</td><td>0.54</td><td>0.54</td><td>0.98</td><td>0.86</td><td>0.77</td><td>0.86</td><td>0.86</td><td>0.86</td><td>0.77</td><td>0.77</td><td>0.77</td></tr><tr><td>Secondary_Market</td><td>0.87</td><td>0.74</td><td>0.73</td><td>0.73</td><td>---</td><td>0.98</td><td>0.88</td><td>0.79</td><td>0.79</td><td>1.05</td><td>0.86</td><td>0.8</td><td>0.86</td><td>0.86</td><td>0.87</td><td>0.77</td><td>0.77</td><td>0.79</td></tr><tr><td>Stock_Exchange_Market</td><td>0.76</td><td>0.62</td><td>0.64</td><td>0.73</td><td>0.98</td><td>---</td><td>1.09</td><td>0.98</td><td>0.99</td><td>1.08</td><td>0.88</td><td>0.79</td><td>0.86</td><td>0.87</td><td>0.87</td><td>0.79</td><td>0.78</td><td>0.77</td></tr><tr><td>Stock_Exchange</td><td>0.63</td><td>0.54</td><td>0.54</td><td>0.54</td><td>0.86</td><td>1.09</td><td>---</td><td>1.17</td><td>1.18</td><td>1.04</td><td>0.91</td><td>0.85</td><td>0.9</td><td>0.9</td><td>0.9</td><td>0.85</td><td>0.85</td><td>0.85</td></tr><tr><td>Opening_Quotation</td><td>0.57</td><td>0.47</td><td>0.48</td><td>0.47</td><td>0.79</td><td>0.98</td><td>1.17</td><td>---</td><td>1.07</td><td>0.96</td><td>0.85</td><td>0.82</td><td>0.85</td><td>0.85</td><td>0.85</td><td>0.81</td><td>0.84</td><td>0.81</td></tr><tr><td>Ending_Quotation</td><td>0.54</td><td>0.47</td><td>0.47</td><td>0.47</td><td>0.78</td><td>0.98</td><td>1.18</td><td>1.07</td><td>---</td><td>0.94</td><td>0.86</td><td>0.82</td><td>0.85</td><td>0.85</td><td>0.87</td><td>0.81</td><td>0.82</td><td>0.82</td></tr><tr><td>Stock</td><td>0.73</td><td>0.62</td><td>0.63</td><td>0.98</td><td>0.99</td><td>0.98</td><td>1</td><td>0.91</td><td>0.91</td><td>---</td><td>1.11</td><td>0.99</td><td>1.09</td><td>1.09</td><td>1.09</td><td>0.98</td><td>0.99</td><td>0.99</td></tr><tr><td>Share_Rights</td><td>0.64</td><td>0.54</td><td>0.54</td><td>0.86</td><td>0.86</td><td>0.86</td><td>0.92</td><td>0.85</td><td>0.86</td><td>1.25</td><td>---</td><td>1.17</td><td>0.98</td><td>0.98</td><td>0.98</td><td>0.91</td><td>0.92</td><td>0.91</td></tr><tr><td>Shares</td><td>0.54</td><td>0.47</td><td>0.47</td><td>0.77</td><td>0.79</td><td>0.77</td><td>0.86</td><td>0.82</td><td>0.82</td><td>1.04</td><td>1.17</td><td>---</td><td>0.91</td><td>0.91</td><td>0.96</td><td>0.88</td><td>0.85</td><td>0.86</td></tr><tr><td>Commercial_Paper</td><td>0.64</td><td>0.56</td><td>0.54</td><td>0.86</td><td>0.86</td><td>0.86</td><td>0.9</td><td>0.85</td><td>0.85</td><td>1.12</td><td>0.99</td><td>0.91</td><td>---</td><td>0.98</td><td>1.02</td><td>0.91</td><td>0.91</td><td>0.9</td></tr><tr><td>Government_Bond</td><td>0.63</td><td>0.54</td><td>0.58</td><td>0.86</td><td>0.86</td><td>0.86</td><td>0.91</td><td>0.85</td><td>0.85</td><td>1.11</td><td>0.98</td><td>0.91</td><td>0.98</td><td>---</td><td>1.01</td><td>0.9</td><td>0.9</td><td>0.9</td></tr><tr><td>Corporate_Bond</td><td>0.65</td><td>0.54</td><td>0.54</td><td>0.86</td><td>0.86</td><td>0.86</td><td>0.91</td><td>0.85</td><td>0.87</td><td>1.09</td><td>0.98</td><td>0.95</td><td>0.99</td><td>1</td><td>---</td><td>1.17</td><td>1.17</td><td>1.17</td></tr><tr><td>Originary_Stock</td><td>0.54</td><td>0.51</td><td>0.48</td><td>0.77</td><td>0.77</td><td>0.78</td><td>0.85</td><td>0.81</td><td>0.81</td><td>1.01</td><td>0.91</td><td>0.89</td><td>0.91</td><td>0.9</td><td>1.17</td><td>---</td><td>1.08</td><td>1.09</td></tr><tr><td>Preferred_Stock</td><td>0.54</td><td>0.47</td><td>0.47</td><td>0.77</td><td>0.77</td><td>0.77</td><td>0.87</td><td>0.86</td><td>0.84</td><td>1.11</td><td>0.93</td><td>0.85</td><td>0.91</td><td>0.9</td><td>1.17</td><td>1.08</td><td>---</td><td>1.07</td></tr><tr><td>Share_Issue</td><td>0.56</td><td>0.47</td><td>0.48</td><td>0.77</td><td>0.78</td><td>0.77</td><td>0.86</td><td>0.81</td><td>0.83</td><td>1.08</td><td>0.91</td><td>0.86</td><td>0.9</td><td>0.9</td><td>1.17</td><td>1.09</td><td>1.07</td><td>---</td></tr></table>

Figure 19. Results of Use Requirement Range Setting for User A

![](/api/attachments/T5YPFZH7/fulltext/images/29445a032b9b1648537b577882db3aaf3eb59f7e960ea35465b46da9e42c4992.jpg)  
Figure 20. Results of Personalized Adaptation for User A

![](/api/attachments/T5YPFZH7/fulltext/images/d0cfecdd7146dfc438c88a9d12a4b7da94e068e8c451a74c8f15fc02bdc81b38.jpg)  
Figure 21. Results of Securities Trading Knowledge Search and Recommendation for User A

## 4.3 Experiment Results for Methodology Evaluation

To evaluate the proposed methodology, the two traditional ontology-based systems were used to compare with the domain ontology adaptation system developed in the study.

Securities trading and cost management ontologies were taken to compare the three systems. Meanwhile, the amount of information about securities trading is 36. 31 is obtained by the first traditional ontology-based system, and 27 of 31 is correct. 26 is obtained by the second traditional ontology-based system, and 23of 26 is correct. 34 is obtained by the domain ontology adaptation system, and 33 of 34 is correct. The recall ratio and precision ratio about securities trading of the three systems were calculated as shown in Tables 6 and 7, respectively. The experiment results show that the recall ratio and the precision ratio of the domain ontology adaptation model are higher than that of the traditional ontology-based information retrieval scheme.

Based on Table 6, recall ratio raised 10.16% at most, and raised 10.03 at least, and recall ratio raised an average of about 10.11. Based on Table 7, precision ratio raised about 5.8% at the highest of times, raised 4.6% at the lowest of times, and precision ratio raised an average of about 5.2%. By analyzing the traditional ontology-based system and the domain ontology adaptation system, the domain ontology adaptation system can obtain more accurate information, because it considers previous browsing and reading behavior of users except the concepts and the relationship of different concepts, the adaptive domain ontology can be satisfied for different users, which is impossible for the traditional ontology-based system.

Table 6. The Result of Recall Ratio by Different Retrieval System

<table><tr><td>Options</td><td>Recall Ratio by Traditional Ontology-based System (I)</td><td>Recall Ratio by Traditional Ontology-based System (II)</td><td>Recall Ratio by Domain Ontology Adaptation System</td></tr><tr><td>Securities Trading</td><td>0.8033</td><td>0.8046</td><td>0.9049</td></tr><tr><td>Cost Management</td><td>0.8058</td><td>0.8062</td><td>0.9073</td></tr></table>

Table 7. The Result of Precision Ratio by Different Retrieval System

<table><tr><td>Options</td><td>Recall Ratio by Traditional Ontology-based System (I)</td><td>Recall Ratio by Traditional Ontology-based System (II)</td><td>Recall Ratio by Domain Ontology Adaptation System</td></tr><tr><td>Securities Trading</td><td>0.8698</td><td>0.8711</td><td>0.9177</td></tr><tr><td>Cost Management</td><td>0.8769</td><td>0.8819</td><td>0.9354</td></tr></table>

## 4.4 System Evaluation from the User Satisfaction Perspective

In measuring user satisfactions [11][15][32][36], the Delphi method has become a widely used tool for acquiring a consensus-based opinion from a panel of experts. Therefore, this study conducts the Delphi method to investigate the user’s satisfaction for using the proposed system. In this case, twenty users are randomly selected using

By using the designed questionnaire shown in Fig. 22, the finding indicates that over eighty percent of users satisfied the results for personalized knowledge search and recommendation in the adapted domain ontology, as shown in Table 8.

Additionally, due to most of the existing application systems using domain ontology provide only functions for knowledge extraction, construction and retrieval, and none tackles the issues of adaptation on knowledge (i.e., domain ontology adaptation). Therefore, the measurement of user satisfaction in Table 8 can also be compared with other novel methods for domain ontology adaptation that may be developed in the future.

<table><tr><td>1.</td><td>The degree to which system function “domain ontology adaptation” supports users in searching and recommending personalized knowledge.□Very Useful (5) □Useful (4) □No Comment (3) □Useless (2) □Very Useless (1)</td></tr><tr><td>2.</td><td>The degree to which the system function “domain ontology adaptation” assists users in reducing search time of personalized knowledge within the domain ontology.□Very Useful (5) □Useful (4) □No Comment (3) □Useless (2) □Very Useless (1)</td></tr><tr><td>3.</td><td>User interfaces take less time than that by manual evaluation.□Very Useful (5) □Useful (4) □No Comment (3) □Useless (2) □Very Useless (1)</td></tr><tr><td>4.</td><td>The user interface is easy to use.□Very Useful (5) □Useful (4) □No Comment (3) □Useless (2) □Very Useless (1)</td></tr><tr><td>5.</td><td>The user interface useful for identification.□Very Useful (5) □Useful (4) □No Comment (3) □Useless (2) □Very Useless (1)</td></tr></table>

Table 8. User Satisfactions Results

<table><tr><td>Question Item</td><td>Very Useful</td><td>Useful</td><td>No Comment</td><td>Useless</td><td>Very Useless</td><td>Total</td><td>Satisfaction</td></tr><tr><td>Q(1)</td><td>8</td><td>9</td><td>2</td><td>1</td><td>0</td><td>20</td><td>85%</td></tr><tr><td>Q(2)</td><td>10</td><td>8</td><td>1</td><td>1</td><td>0</td><td>20</td><td>90%</td></tr><tr><td>Q(3)</td><td>11</td><td>6</td><td>3</td><td>0</td><td>0</td><td>20</td><td>85%</td></tr><tr><td>Q(4)</td><td>8</td><td>8</td><td>4</td><td>0</td><td>0</td><td>20</td><td>80%</td></tr><tr><td>Q(5)</td><td>9</td><td>7</td><td>3</td><td>1</td><td>0</td><td>20</td><td>85%</td></tr><tr><td>Average</td><td>9.2</td><td>7.6</td><td>2.6</td><td>0.6</td><td>0</td><td>20</td><td>84%</td></tr></table>

## 5. Conclusions and Further Work

This work proposed novel enhancements in domain ontology adaptation for personalized search and recommendation through designing an adaptation model, and developing an adaptation methodology, as well as a domain ontology adaptation system. The methodology for domain ontology adaptation contains adaptation factor analysis, user preference analysis, requirement-based concept clustering, and personalized adaptation. Finally, this study implemented a system for domain ontology adaptation based on the aforementioned techniques. The main results and contributions of this work are summarized as follows:

(1) Domain ontology adaptation model: According to the previous browsing and reading behavior of users and related literatures of domain ontology maintenance, the domain ontology adaptation model is designed to satisfy the future requirements of users and thus promote the use value of domain ontology.

(2) Domain ontology adaptation methodology: Based on the proposed domain ontology adaptation model, the structural methodology for domain ontology adaptation is developed to facilitate the implementation of the domain ontology adaptation system.

#

(3) Domain ontology adaptation system: The implemented domain ontology adaptation system for personalized knowledge search and recommendation can instantaneously record and analyze the usage history log while a user uses the domain ontology and then can create a user pattern to obtain the required domain ontology content.

From the results of the system evaluation in Section 4.3, this work can facilitate personalized knowledge search and recommendation and promote the accuracy of and consequently boost the use value of domain ontology.

Based on the proposed model and methodology in this study, further work will address three directions. This study used the association rules and the hierarchical concept clustering method to indirectly adjust the structure of domain ontology. However, this method has not considered the growth of domain ontology due to continuous improvement of technology and technique. Thus, future domain ontology adaptation should analyze and capture new domain ontology. Additionally, this study explored the association of user action in domain ontology using the data mining method to continuously train and establish the association rules for the usage history log of the new user. However, this type of exploration method creates a cold start while initiating the system, causing lower accuracy of user patterns established in the initial phase of the system. Therefore, a technology for knowledge concept navigation should be developed to facilitate learning and verification of mechanism for domain ontology adaptation, and ultimately enhance user pattern accuracy and the integrity. Finally, a more thorough evaluation of the proposed methodology can be conducted to extend the theoretical contribution.

## Acknowledgements

The authors would like to thank the National Science Council of the Republic of China, Taiwan, for financially supporting this research under Contract No. NSC99-2221-E-327-036. The authors are grateful for the anonymous reviewers who made constructive comments.

## References

[1] A. Agresti, Categorical data analysis, Wiley, New Jersey, 2002, pp. 165-211.

[2] T. Amemiya, Advanced econometrics, Harvard University Press, 1985, pp. 135-255.

[3] A. Baneyx, J. Charlet, M. C. Jaulent, Building an ontology of pulmonary diseases with natural language processing tools using textual corpora,

International Journal of Medical Informatics 76 (2/3), 2007, pp. 208-215.

[4] M. Broy, M. V. Cengarle, B. Rumpe, Semantics of UML- towards a system model for UML: The state machine model, Tech. Report TUM-I0711, TUM, pp. 2007, pp. 4-11.

[5] P. Castells, M. Fernandez, D. Vallet, P. Mylonas, Y. Avrithis, Self-tuning personalized information retrieval in an ontology-based framework, LNCS 3762, 2005, pp. 977-986.

[6] P. M. Chen, F. C. Kuo, An information retrieval system based on a user profile, Journal of Systems and Software 54(1), 2000, pp. 3-8.

[7] Y. L. Chen, M. H. Kuo, S. Y. Wu, K. Tang, Discovering recency, frequency, and monetary (RFM) sequential patterns from customers’ purchasing data, Electronic Commerce Research and Applications 8 (5), 2009, pp. 241-251.

[8] R. C. Chen, J. Y. Liang, R. H. Pan, Using recursive ART network to construction domain ontology based on term frequency and inverse document frequency, Expert Systems with Applications 34 (1), 2008, pp. 488-501.

[9] K. Cheung, J. Hunter, J. Drennan, MatSeek: an ontology-based federated search interface for materials scientists, Semantic Scientific Knowledge Integration 24 (1), 2009, pp. 47-56.

[10] H. L. Chieu, H. T. Ng, A maximum entropy approach to information extraction National Conference on Artificial Intelligence, 2002, pp. 786-791.

[11] C. Chou, Developing the e-Delphi system: a web-based forecasting tool for educational research, British Journal of Educational Technology 33 (2), 2002, pp. 234-236.

[12] G. Erozel, N. K. Cicekli, I. Cicekli, Natural language querying for video databases, Information Sciences 178 (12), 2008, pp. 2534-2552.

[13] S. Figge, Situation-dependent services? a challenge for mobile network operators, Journal of Business Research 57 (12), 2004, pp. 1416-1422.

[14] L. Freeman, The development of social network analysis, Empirical Press, 27 (3), 2004, pp. 101-136.

[15] J. L. Herlocker, J. A. Konstan, L. G. Terveen, J. T. Riedl, Evaluating collaborative filtering recommender systems, ACM Trans. Inf. Syst. 22 (1), 2004, pp. 5-53.

[16] J. Hong, E. H. Suh, J. Kim, S. Y. Kim, Context-aware system for proactive personalized service based on context history, Expert Systems with Applications 36 (4), 2009, pp. 7448-7457.

[17] D. W. Hosmer, S. Lemeshow, Applied logistic regression, Wiley, pp. 1-31, 2000.

[18] C. C. Hsu, C. L. Chen, Y. W. Su, Hierarchical clustering of mixed data based on distance hierarchy, Information Sciences 177 (20), 2007, pp. 4474-4492.

[19] E. Hyvönen, S. Saarela, K. Viljanen, Application of ontology techniques to view-based semantic search and browsing, The Semantic Web: Research and Applications 3053, 2004, pp. 92-106.

[20] A. Kayed, E. El-Qawasmeh, Z. Qawaqneh, Ranking web sites using domain ontology concepts, Information & Management 47 (7/8), 2010, pp. 350-355.

[21] N. Khasawneh, C. C. Chan, Active user-based and ontology-based web log data preprocessing for web usage mining, Proceedings of the 2006 IEEE/WIC/ACM International Conference on Web Intelligence, 2006, pp. 325-328.

[22] A. Komlodi, G. Marchionini, D. Soergel, Search history support for finding and using information: user interface design recommendations from a user study, Information Processing and Management 43 (1), 2007, pp. 10-29.

[23] R. L. Kumar, M. A. Smith, S. Bannerjee, User interface features influencing overall ease of use and personalization, Information & Management 41 (3), 2004, pp. 289-302.

[24] O. Kwon, A social network approach to resolving group-level conflict in context-aware services, Expert Systems with Applications 36 (5), 2009, pp. 8967-8974.

[25] L. F. Lai, A knowledge engineering approach to knowledge management, Information Sciences 177 (19), 2007, pp. 4072-4094.

[26] W. P. Lee, Deploying personalized mobile services in an agent-based environment, Expert Systems with Applications 32 (4), 2007, pp. 1194-1207.

[27] I. Lee, J. Kim, J. Kim, Use contexts for the mobile Internet: a longitudinal study monitoring actual use of mobile internet services, International Journal of Human-Computer Interaction 18 (3), 2005, pp. 269-292.

[28] H. C. Li, W. M. Ko, Automated food ontology construction mechanism for diabetes diet care, Proceedings of the Sixth International Conference on Machine Learning and Cybernetics, Hong Kong, 2007.

[29] Y. F. Lia, N. Zhong, Web mining model and its applications for information gathering, Knowledge-Based Systems 17 (5), 2004, pp. 207-217.

[30] C. W. Liao, Y. H. Perng, T. L. Chiang, Discovery of unapparent association rules based on extracted probability, Decision Support Systems 47 (4), 2009, pp. 354-363.

[31] M. Liu, W. Shen, Q. Hao, J. Yan An weighted ontology-based semantic similarity algorithm for web service, Expert Systems with Applications 36 (10), 2009, pp. 12480-12490.

[32] C. D. Manning, P. Raghavan, H. Schutze, Introduction to information retrieval, Cambridge University Press, 2008, pp. 45-59.

[33] R. Navigli, P. Velardi, Learning domain ontologies from document warehouses

and dedicated web sites, Computational Linguistics 30 (2), 2004, pp. 151-179.

[34] Q. Niu, B. Qiu, S. Xia, Ontology-based learning resources in the field of semantic search model, Computer Application Research, 25, 2008, pp. 1977-1982.

[35] P. Plessers, O. De Troyer, Resolving inconsistencies in evolving ontologies, Lecture Notes in Computer Science 4011, 2006, pp. 200-214.

[36] P. Pu, L. Chen, P. Kumar, Evaluating product search and recommender systems for E-commerce environments, Electronic Commerce Research 8 (1), 2008, pp. 1-27.

[37] T. T. Quan, S. C. Hui, A. C. M. Fong, T. H. Cao, Automatic fuzzy ontology generation for semantic web, IEEE Transactions on Knowledge and Data Engineering 18 (6), 2006, pp. 842-856.

[38] D. Riaño, F. Real, J. A. López-Vallverdú, F. Campana, S. Ercolani, P. Mecocci, R. Annicchiarico, C. Caltagirone, An ontology-based personalization of health-care knowledge to support clinical decisions for chronically ill patients, Journal of Biomedical Informatics 45 (3), 2012, pp. 429-446.

[39] H. Rostami, J. Habibi, E. Livani, Semantic routing of search queries in P2P networks, Journal of Parallel and Distributed Computing 68 (12), 2008, pp. 1590-1602.

[40] M. Shamsfard, A. A. Barforoush, Learning ontologies from natural language texts, International Journal of Human-Computer Studies 60 (1), 2004, pp. 17-63.

[41] M. Stanojevic, S. Vraneš, Knowledge representation with SOUL, Expert Systems With Applications 33 (1), 2007, pp. 122-134.

[42] M. M. Sufyan Beg, A subjective measure of web search quality, Information Sciences 169 (3), 2005, pp.365-381.

[43] P. N. Tan, M. Steinbeach, V. Kumar, Introduction to data mining, Addison Wesley, 2006, pp.158-162.

[44] P. N. Tan, M. Steinbeach, V. Kumar, Introduction to data mining, Addison Wesley, 2006, pp.328-330.

[45] P. N. Tan, M. Steinbeach, V. Kumar, Introduction to data mining, Addison Wesley, 2006, pp.515-523.

[46] T. Y. Tao, M. Zhao, An ontology-based information retrieval model for vegetables E-commerce, Journal of Integrative Agriculture, 11 (5), 2012, pp. 800-807.

[47] X. Tian, X. Y. Du, H. Hu, H. H. Li, Modeling individual cognitive structure in contextual information retrieval, Computers and Mathematics with Applications 57 (6), 2009, pp. 1048-1056.

[48] P. Velardi, P. Fabriani, M. Missikoff, Using text processing techniques to

automatically enrich a domain ontology, in Proceedings of the international conference on Formal Ontology in Information Systems 2001, New York, NY, USA, 2001, pp. 270-284.

[49] B. Vesin, M. Ivanovic, A. Klasnja-Milicevic, Z. Budimac, Protus 2.0: Ontology-based semantic recommendation in programming tutoring system, Expert Systems with Applications 39 (15), 2012, pp. 12229-12246.

[50] W. Wang, K. Lin, Ontology-based user profile model used in information retrieval, Journal of Computational Information Systems 5(3), 2009, pp. 1613-1621.

[51] S. S. Weng, H. J. Tsai, S. C. Liu, C. H. Hsu, Ontology construction for information classification, Expert System with Applications 31 (1), 2006, pp. 1-12.

[52] I. H. Witten, E. Frank, Data mining: practical machine learning tools and techniques (Second Edition), Morgan Kaufmann, 2005, pp. 4-35.
