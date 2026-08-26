---
otero_id: 7412
otero_key: "UXUZ667S"
title: "Collaborative relevance assessment for task-based knowledge support"
authors: "Duen-Ren Liu; I-Chin Wu"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2007.06.015"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dss

# Collaborative relevance assessment for task-based knowledge support

Duen-Ren Liu <sup>a,⁎</sup>, I-Chin Wu <sup>b</sup>

<sup>a</sup> Institute of Information Management, National Chiao Tung University, Hsinchu 300, Taiwan <sup>b</sup> Department of Information Management, Fu Jen Catholic University, Taipei 242, Taiwan

Received 16 April 2004; received in revised form 20 April 2007; accepted 20 June 2007 Available online 27 June 2007

## Abstract

The operations and management activities of enterprises are mainly task-based and knowledge intensive. Accordingly, an important issue in deploying knowledge management systems is the provision of task-relevant information (codified knowledge) to meet the information needs of knowledge workers during the execution of a task. Codified knowledge extracted from previously executed tasks can provide valuable knowledge about conducting the task-at-hand (current task), and is a valuable information source for constructing a task profile that models a worker's task needs, i.e., information needs for the current task. In this paper, we propose a novel task-relevance assessment approach that evaluates the relevance of previous tasks in order to construct a task profile for the current task. The approach helps knowledge workers assess the relevance of previous tasks through linguistic evaluation and the collaboration of knowledge workers. In addition, applying relevance assessment to a large number of tasks may create an excessive burden for workers. Thus, we propose a novel two-phase relevance assessment method to help workers conduct relevance assessment effectively. Furthermore, a modified relevance feedback technique, which is integrated with the taskrelevance assessment method, is employed to derive the task profile for the task-at-hand. Consequently, task-based knowledge support can be enabled to provide knowledge workers with task-relevant information based on task profiles. Empirical experiments demonstrate that the proposed approach models workers' task-needs effectively and helps provide task-relevant knowledge. © 2007 Elsevier B.V. All rights reserved.

Keywords: Information retrieval; Knowledge management; Relevance assessment; Task-based knowledge support; Task profile

## 1. Introduction

In organizations, knowledge management (KM) is an important means of gaining a competitive advantage. To this end, knowledge management systems (KMS) maximize the effectiveness of knowledge assets, thereby increasing an organization's profitability and productivity [17,27]. KMS employs information technologies (IT), such as document management and data mining, to facilitate access to, sharing of, and reuse of knowledge assets within and across organizations [8,22].

Intellectual content is generally codified in an explicit form to facilitate knowledge sharing and reuse [5,26,38]. Textual data, such as articles, reports, and manuals, is treated as valuable and explicit knowledge in organizations. Codifying structured and explicit knowledge into a knowledge repository, especially in document form, is a commonly used strategy for managing knowledge [8,16,38]. Empirical findings indicate that codifying intellectual content into a knowledge repository helps workers exploit existing organizational resources efficiently [15]. Accordingly, knowledge (information) retrieval is a core component of KMS to retrieve codified knowledge. An effective knowledge retrieval function can mitigate the difficulty of obtaining knowledge items from a knowledge repository [11,14]. Information retrieval (IR) techniques are widely used to implement knowledge retrieval functions. Query-based information retrieval is a user-driven approach that accesses knowledge items by translating user information needs into compromised queries. Alternatively, information filtering based on profile construction provides a system-driven approach for proactive delivery of relevant information to users [4].

Since a company's operational and management activities are mainly task-based, workers perform various tasks to achieve business goals. In task-based business environments, an important issue of deploying KMS is the provision of task-relevant information (codified knowledge) to meet the information needs of knowledge workers during the execution of a task. In recent years, information retrieval techniques coupled with workflow management systems (WfMS) have been used to support proactive delivery of task-specific knowledge according to the context of tasks within a process [1,2,11,12]. For example, the KnowMore system maintains task specifications (profiles) that define the process-context of tasks and associated knowledge items [1]. Thus, context-aware delivery of task-specific knowledge can be provided based on the task specifications and the execution context of the current process. The Kabiria system supports knowledgebased document retrieval in office environments by allowing users to retrieve documents according to the operational context of task-associated procedures [6]. In [23], a process meta-model that specifies the knowledge in context is integrated with workflow systems to capture and retrieve knowledge within a process context.

The above works provide an appropriate perspective for designing task-based knowledge support. However, they focus on specifying the process-context of a task to support context-aware or process-aware knowledge retrieval, rather than on a systematic method for constructing a task profile that models a worker's task needs, i.e., information needs for the current task (task-at-hand).

In this work, we focus on providing codified knowledge support for knowledge-intensive tasks within organizations. Examples of knowledge-intensive tasks include thesis-writing and research projects in academic organizations, project management in firms, and research and product development in R&D departments. Because of the nature of knowledge-intensive tasks, a collaborative mechanism is important for developing a knowledge support system [3,40]. Moreover, huge amounts of codified knowledge place an excessive burden on knowledge workers. Intelligent search engines, agentbased techniques, and information filtering have been applied to deliver information relevant to a worker's taskat-hand. Knowledge sharing and intelligent search services support knowledge management in a decentralized global business [34]. Agents cooperate to achieve task-based information filtering within a work process based on user feedback about a document's usefulness to a particular job situation [9]. Alternatively, agents can use inference engines to reason proactively about the needed information in order to provide effective task support [35].

Information filtering with a similarity-based approach is often used to locate knowledge items relevant to the task-at-hand, whereby the relevance of a knowledge item is determined by analyzing the similarity between the concept terms of the knowledge item and the current task [19,37]. The concept terms are usually extracted from the textual descriptions of a knowledge item/task. For example, if the task-at-hand is the development of a software program, the task needs to be a partially written program with comments [37]. However, the major issue is that the comments may not describe the task precisely and completely, so the similarity-based approach may not be able to locate relevant information (software components). Holz et al. [19] propose a task-oriented, similaritybased approach that organizes desktop documents and proactively delivers task-specific information. The effectiveness of this approach also relies on the accuracy of the concept terms of the task-at-hand, which are extracted from the task name and associated relevant documents.

Even though the above works support task execution by using information filtering techniques, they cannot effectively model a worker's initial task-needs (i.e., information needs for the initial phase of a task) when very few or no textual task-descriptions exist for extracting the concept terms of the task-at-hand. Similarity analysis based on concept terms cannot derive appropriate information to meet initial task needs, since the concept terms of the taskat-hand extracted from the textual descriptions do not properly represent the task. In this work, we attempt to resolve the problem by employing a user-based assessment approach to model a worker's initial task-needs.

Historical codified knowledge items, task descriptions, and relevant documents extracted from previously executed tasks provide valuable knowledge sources for supporting task profile construction. Rather than ask knowledge workers to specify task characteristics directly, a systematic approach is preferable to create a task profile, i.e., the concept terms of the current task (task-at-hand), based on the concept terms and the relevance of previous tasks. However, for tasks with very few or no textual descriptions, user assessment is necessary to determine the relevance (similarity) of previous tasks to the current task. Accordingly, we propose a novel task-relevance assessment approach to evaluate a task's relevance in order to construct task profiles that model the worker's information needs for the current task. A modified relevance feedback (RF) technique is employed to derive the task profile based on the degree of relevance and the concept terms of previous tasks. The approach helps knowledge workers assess the relevance of previous tasks through linguistic evaluation and the collaboration of knowledge workers. Even so, applying relevance assessment to a large number of tasks may place an excessive burden on workers. Therefore, we propose a novel twophase relevance assessment method to help workers conduct relevance assessment effectively. Consequently, task-based knowledge support can be enabled to provide knowledge workers with task-relevant information based on task profiles. Our empirical experiments demonstrate that the proposed approach is effective in providing taskbased knowledge support.

The remainder of the paper is organized as follows. Section 2 presents an overview of our approach and describes the architecture of the proposed task-based knowledge support system. Section 3 introduces the basic techniques used in this work. Section 4 describes the process of building the task-oriented repository. Section 5 describes the two-phase collaborative relevance-assessment procedure for generating task profiles. The experiment evaluations are reported in Section 6. Finally, in Section 7, we present our conclusions and indicate the direction of our future work.

## 2. Task-based knowledge support

In this section we present an overview of the proposed approach, and then describe the architecture of the proposed task-based knowledge support system.

## 2.1. Overview of task-based knowledge support

Knowledge workers generally require historical taskrelevant information to accomplish current tasks. Thus, reusing knowledge about previous tasks is the key to providing effective knowledge support for conducting new tasks. Accordingly, the proposed approach manages an organization's codified knowledge by using a task-based categorization scheme to organize tasks into categories.

Codified knowledge is analyzed, categorized, and stored in a knowledge repository. This work broadly defines a task as a unit of work, such as a research project in an organization. A task denotes either an executed task or a current task. An executed-task is a historical task already accomplished within the organization, whereas a current-task is the task at hand. Categories representing the main subjects of organizational activities are defined in order to organize tasks and codify knowledge. A task profile specifies the key concept terms of the current task, and models the information needs of knowledge workers during the task's execution. A task corpus specifies the key concept terms of an executed task. Reference tasks are a subset of executed tasks selected for the construction of a task profile.

As noted earlier, large amounts of codified knowledge place an excessive burden on knowledge workers. Previous works have attempted to solve the problem with information filtering techniques. However, they cannot effectively model a worker's initial task-needs, when very few or no textual descriptions exist to properly represent the current task. In contrast, our approach constructs a task profile that models a worker's information needs for the current task based on the corpus (concept terms) and the relevance of previously executed tasks. A novel task-relevance assessment approach is proposed to determine the relevance of previously executed tasks to the current-task. We then use a modified relevance feedback (RF) technique to derive the task profile based on the degree of relevance and the concept terms of executed tasks.

## 2.1.1. Task relevance assessment

The proposed approach addresses the following three issues that arise during user assessment.

First, assessing the relevance of a task by assigning precise numerical values may be difficult for knowledge workers. Thus, a fuzzy linguistic approach, an approximate technique that models human thinking [39], is used to evaluate a task's relevance by using linguistic terms such as “low” or “high” to express the worker's perception of “Relevance”. The proposed task-relevance assessment method provides a systematic and natural way to analyze the relevance of tasks in the repository. The fuzzy linguistic approach is described in Section 3.3.

Second, for complex and knowledge-intensive tasks, collaboration among knowledge workers and experts is often necessary to facilitate more effective knowledge dissemination. In addition, novices who are less knowledgeable about the current task may have difficulty in assessing the relevance of tasks. Domain experts or experienced workers with valuable implicit knowledge play an important role in helping knowledge workers solve problems or make decisions [12–14]. Accordingly, the proposed assessment approach incorporates a collaborative mechanism that helps knowledge workers, especially novices, determine the relevance of executed tasks. Herein, collaboration means that knowledge workers (e.g., experts and task members) can exchange the evaluation results of knowledge items (e.g., topic taxonomy, task sets, etc.) via a common interface (i.e., task assessment editor) in the proposed task-based workspace. This is similar to the concept of collaborative information retrieval proposed by Hansen and Jarvelin [18] in that we focus on information access behavior related to a specific problem-solving activity, which requires interaction among workers in a common workplace. A collaborative mechanism, on the other hand, refers to the process of conducting assessments and aggregating the relevance results of workers and domain experts to derive a task's relevance in a collaborative workplace. The concept is similar to the collaboration module in the COPLINK workflow model [40]. In this work, however, we activate the collaborative mechanism by loading the evaluation results at the start of the task's execution in order to model a worker's initial task-needs for constructing task profiles, rather than identifying similar search cases to support the search results based on the user's search actions.

Third, applying relevance assessment to a large number of previously executed tasks may create a burden for workers and influence the assessment result. Thus, a novel two-phase relevance assessment procedure is used to reduce the number of tasks to be assessed by conducting category assessment to select a subset of executed tasks as reference tasks for further task assessment. A task categorization scheme is used to group tasks into categories. Identifying a small subset of executed tasks as reference tasks can help knowledge workers conduct further task-relevance assessment without reviewing all previously executed tasks. The reference tasks are selected based on their similarity to the current task using the degree of relevance of a task to the categories.

## 2.1.2. Generating task profiles by modified relevance feedback techniques

The reference tasks are used to extract task-relevant knowledge for the current task. Once the reference tasks have been identified, a modified relevance feedback (RF) technique is used to derive the task profile of the current task based on the degree of relevance and the concept terms of the reference tasks. The knowledge support system uses task profiles to identify relevant information and assist knowledge workers in accessing task-relevant knowledge during the execution of the current task. Relevance feedback, a well-known technique in information retrieval, improves the search effectiveness by automatically reformulating queries [30]. The relevance feedback techniques are described in Section 3.2. Most traditional RF techniques use the concept terms of relevant/irrelevant documents to adjust or reformulate the concept terms of a query. The concept terms of relevant documents have a positive influence on the reformulation, while those of irrelevant documents have a negative influence. The relevance of documents is based on user feedback about the previous query result. We adopt the RF technique to derive the task profiles. However, unlike traditional RF techniques that use direct user feedback about previous query results, the proposed two-phase relevance assessment procedure helps workers determine a task's relevance based on the proposed categorization scheme. In addition, our modified RF approach uses aggregated relevance ratings as the degrees of relevance of reference tasks to adjust the task profile, whereas most RF techniques consider binary relevance, i.e., relevant/irrelevant.

## 2.2. System architecture of task-based knowledge support

Fig. 1 illustrates the architecture of the proposed taskbased knowledge support system. The participants are knowledge workers engaged in specific tasks and domain experts in specific subjects. The system comprises three main modules: the task-oriented information repository, the task profile handler, and the taskoriented retrieval router.

Task-oriented information repository. This module is the knowledge base for task-based knowledge support. Task-oriented repositories are constructed with support from the task-based categorization scheme to ensure that codified knowledge is utilized effectively. The repositories, which store codified knowledge corresponding to a task's execution, contain three databases: the documentindexing database, the task corpus, and the task categorization database. The document-indexing database stores task relevant documents indexed by their concept terms. The key concept terms of knowledge items (documents) are represented as a feature vector of weighted terms using the IR techniques described in Section 3.1. A task corpus contains the key concept terms of an executed task, and is expressed as a feature vector of weighted terms. The task corpus of an executed task is generated by extracting the weighted terms from textual documents of the executed task. This process is described in detail in Section 4.1. Finally, the task categorization database records the relationships between previously executed tasks and categories; that is, the relevance of executed tasks to the categories. The task categorization database helps identify reference tasks based on their similarity to the current task.

![](/api/attachments/UXUZ667S/fulltext/images/7fc2a258033ae51c4725c6e695c52ecaa331c5269b9ebc3e2abe094dd6fee5c3.jpg)  
Fig. 1. The architecture of the task-based knowledge support system.

Task profile handler. The task profile handler comprises the following mechanisms for profile management: profile creation, profile adjustment, and profile adaptation. A task-profile specifies the key concept terms of the current task and is expressed as a feature vector of weighted terms. Task-profiles form the basis for discovering and disseminating task-relevant information to knowledge workers. The system generates profiles based on the task corpus of relevant executed tasks and employs the proposed assessment mechanism for task profile adjustment.

Task-oriented retrieval router. The task-oriented retrieval router matches task profiles with knowledge repositories to streamline knowledge retrieval. The router retrieves and disseminates task-relevant information to provide task-based knowledge support based on task profiles.

## 2.2.1. Process of task-based knowledge support

Fig. 1 also shows the process of the relevance assessment and knowledge support. The task plan or textual descriptions of the current task can be used to extract the concept terms of the task to construct an initial task profile. However, the profile may not effectively model the initial task needs, especially for tasks with very few or no textual descriptions. Using a fuzzy linguistic approach, a two-phase assessment process evaluates a task's relevance based on the collaboration of knowledge workers and domain experts. Knowledge workers can assess the relevance of previously executed tasks to the current task through the collaborative taskbased workplace of our system. The system's assessment interface supports linguistic relevance ratings. In addition, the workplace shows the relevance ratings given by other collaborative workers (experts or task-relevant colleagues). The worker may adopt a collaborative assessment, where the relevance ratings of other workers are combined with his/her own relevance ratings to obtain aggregated relevance ratings.

The task categorization database contains the categorization scheme, including the categories and the degree of relevance of executed tasks to the categories, to support the proposed two-phase task-assessment process. The worker conducts category assessment (phase-1 assessment) based on the category scheme to derive the relevance of the current task to categories. The system then selects a set of reference tasks from previously executed tasks based on the similarity measures derived according to the degree of relevance of executed/current tasks to categories. The reference tasks are displayed on the assessment interface to help workers conduct further task assessments. Thus, the knowledge worker can conduct a task assessment (phase-2 assessment) without reviewing all previously executed tasks. The two-phase relevance assessment procedure is discussed in detail in Section 5.1.

The assessment results and the initial profile are used to generate the worker's task profile based on the modified relevance feedback technique. The technique considers the aggregated relevance ratings and the task corpus of reference tasks to refine the initial task profile. Details are given in Section 5.2. The generated task profile is stored in the task profile database located in the information repository for future knowledge retrieval.

When a worker submits a task-query to retrieve taskrelevant item sets, the task-oriented retrieval router retrieves the task profile of current task from the information repository based on the task-query. The router then matches the task profile with codified knowledge items stored in the repository to retrieve task-relevant items (i.e., relevant documents and tasks) according to the similarity measures of the task profile and the knowledge items. It then disseminates the taskrelevant items to workers to provide task-based knowledge support. Note that all text-related processing, including information extraction and text pre-processing, is performed off-line in the system's back-end by the text-processing server module.

Section 4 describes the construction of a task-oriented information repository. Textual data is analyzed and stored in the task-oriented information repository. Section 5 describes the proposed relevance-assessment approach for generating and adjusting task profiles.

## 3. Preliminary techniques

This section briefly reviews some basic techniques, including information retrieval, the relevance feedback technique, and the fuzzy linguistic approach. In this work, we modify and combine these methods to support task-relevance assessment and construct task profiles. Since retrieving knowledge items from textual data is our primary objective, we adopt information retrieval and information filtering techniques for text pre-processing, indexing, querying, and profiling tasks. Furthermore, using a fuzzy linguistic approach, we incorporate linguistic ratings into the relevance feedback technique.

## 3.1. Information retrieval in a vector space model

The key contents of a codified knowledge item (document) can be represented as a feature vector of weighted terms in n-dimensional space, using a term weighting approach that considers term frequency, inverse document frequency, and normalization factors [31]. The term transformation steps, i.e., case folding, stemming, and stop word removal, are performed during text pre-processing [29,33,36]. Then, term weighting is employed to extract the most discriminating terms [4]. Let d be a codified knowledge item (document), and $\overrightarrow { d } = \langle w ( k _ { 1 } , d ) , w ( k _ { 2 } , d ) , \dots , w ( k _ { n } , d ) \rangle$ be the feature vector of $d ,$ where $w ( k _ { i } , ~ d )$ is the weight of a term $k _ { i }$ that occurs in d. The weight of a term indicates its degree of importance in representing the document (codified knowledge). The well-known $t f { - } i d f$ approach, which is often used for term (keyword) weighting [29], assumes that terms that occur more frequently in one document compared to other documents are better discriminators for representing that document. Let the term frequency $t f ( k _ { i } , d )$ be the frequency that term $k _ { i }$ occurs in $d ,$ and let the document frequency $d f ( k _ { i } )$ represent the number of documents that contain term $k _ { i } .$ The importance of term $k _ { i }$ to a document d is proportional to the term frequency and inversely proportional to the document frequency, as expressed in Eq. (1).

$$
\begin{array}{l} w (k _ {i}, d) = \frac {1}{\sqrt {\sum_ {i} (t f (k _ {i} , d) \times \log (N / d f (k _ {i}))) ^ {2}}} t f (k _ {i}, d) \\ \times \left(\log \frac {N}{d f (k _ {i})}\right), \end{array} \tag {1}
$$

where $N$ is the total the number of documents . The denominator on the right-hand side of the equation normalizes the weight of a term.

## 3.1.1. Similarity measure

The cosine formula is a similarity measure that is widely used to assess the degree of similarity between two items, x and $y ,$ by computing the cosine of the angle between their corresponding feature vectors, ${ \overrightarrow { x } } ^ { * }$ and $\overrightarrow { y , }$ as shown in Eq. (2). The degree of similarity is higher if the cosine similarity is close to 1.

$$
\operatorname{sim} (x, y) = \operatorname{cosine} (\overrightarrow {x}, \overrightarrow {y}) = \frac {\overrightarrow {x} \cdot \overrightarrow {y}}{| \overrightarrow {x} | | \overrightarrow {y} |}\tag{2}
$$

Each document or query/task can be represented as feature vector in a vector space model. Let $\vec { \vec { d } _ { j } }$ represent a vector of a document $d _ { j }$ and let $\overrightarrow { q }$ be a vector of a query/ task $q .$ The similarity between a document $d _ { j }$ and a query/task $q ,$ sim $( d _ { j } , q )$ , can be calculated by Eq. (2).

## 3.2. Relevance feedback techniques

Relevance feedback (RF) improves the search effectiveness through query reformulation [32]. The RF technique reformulates or expands the original query based on partial relevance judgments, i.e., feedback on part of the evaluation set. Relevant documents with positive feedback have a positive influence on the weight of terms, while irrelevant documents with negative feedback have a negative influence on the weight of terms. A refined query vector can be generated by adding the term weights of relevant documents and subtracting the term weights of irrelevant documents. Eqs. (3) and (4) illustrate two classic relevance feedback methods — the standard\_Rocchio and the Ide\_Dec\_Hi methods designed by Rocchio [30] and Ide [20], respectively. A modified query vector $\overrightarrow { \boldsymbol { q } _ { m } }$ is derived using the relevance of documents (as feedback) to adjust the query vector $\overrightarrow { q } \left[ 4 \right]$

$$
\begin{array}{c} \text { Standard\_Rocchio:} \overrightarrow {q _ {m}} = \alpha \overrightarrow {q} + \beta \frac {1}{| D _ {r} |} \sum_ {\forall d _ {j} \in D _ {r}} \overrightarrow {d _ {j}} \\ - \gamma \frac {1}{| D _ {n} |} \sum_ {\forall d _ {j} \in D _ {n}} \overrightarrow {d _ {j}} \end{array}\tag{3}
$$

$$
\begin{array}{c} \text {Ide\_Dec\_Hi}: \overrightarrow {q _ {m}} = \alpha \overrightarrow {q} + \beta \sum_ {\forall d _ {j} \in D _ {r}} \overrightarrow {d _ {j}} \\ - \gamma \max _ {\text {irrelevant}} (\overrightarrow {d _ {j}}) \end{array}\tag{4}
$$

where $D _ { r }$ denotes the set of relevant documents and $D _ { n }$ represents the set of irrelevant documents according to user assessments. $| D _ { r } |$ and $\left| D _ { n } \right|$ represent the number of documents in the sets $D _ { r }$ and $D _ { n }$ respectively; and $\alpha , \beta , \gamma$ are tuning constants. The function max<sub>irrelevant</sub> returns the most irrelevant document. The two methods produce similar results [4].

We modify the standard\_Rocchio and Ide\_Dec\_Hi methods by integrating them with the fuzzy linguistic approach to derive the aggregated degrees of relevance obtained from user assessments (discussed in Section 5.1). The modification considers the relative importance of relevant and irrelevant codified-knowledge from the user's perspective. The details are presented in Section 5.2.

## 3.3. Modeling user perceptions by a fuzzy linguistic approach

Generally, assessing qualitative problems by assigning precise values to them is difficult. A fuzzy linguistic approach, which approximates human perception, makes it easier to evaluate qualitative problems [39]. Linguistic assessment is based on words rather than numbers. A linguistic variable with linguistic terms and their associated meanings needs to be defined for linguistic assessment. A formal definition of a linguistic variable can be found in [39].

In this work, a linguistic variable, Relevance, is defined to represent the degree of relevance between items (tasks or categories) assessed by workers. The linguistic terms “very low”, “low”, “normal”, “high”, “very high”, and “perfect”, are used to express the context of “Relevance”. Let E(Relevance) represent the linguistic terms of the linguistic variable Relevance. E (Relevance) is characterized using a fuzzy set of the universe of discourse $U = [ 0 , 1 ]$ , in which six linguistic terms, $\check { r } \dot { j }$ , and their associated semantic meanings, m(řj), are defined as follows: E(Relevance) = {ř0 = Very Low (VL), ř1 = Low (L), ř2 = Normal (N), ř3 = High (H), ř4 = Very High (VH), ř5 = Perfect (P)}, where $m ( \check { r } i ) <$ m(řj), for $i < j ,$ and all m(řj) are distributed in the range [0,1].

The fuzzy linguistic approach models the semantic meaning of each term by fuzzy numbers [10]. This work employs triangular fuzzy number (TFN), as defined in Appendix A, to express the approximate value of each linguistic term. A triangular fuzzy number is specified by three parameters (l, m, r), with $l { < } m { < } r ,$ , which determine the x-coordinates of the three corners of the triangular membership function.

## 4. Task-oriented information repository

This section describes the two phases of constructing a task-oriented information repository: extracting the task corpus from textual data gathered during a task's execution, and determining the degrees of relevance between executed tasks and categories.

## 4.1. Extracting the task corpus

The task corpus of an executed task $t _ { r }$ is represented as a feature vector of weighted terms derived by analyzing the set of documents generated and accessed by $t _ { r }$ Each document $d _ { j }$ is pre-processed and represented as a feature vector ${ \overrightarrow { d _ { j } } } ,$ as described in Section 3.1. A centroid approach is used to derive the feature vector of a task by averaging the feature vectors of documents generated/accessed by the task. Let $D _ { t _ { r } }$ denote the set of documents generated/accessed by task $t _ { r }$ . The task corpus (feature vector) of task $t _ { r }$ is defined as the centroid vector $\overrightarrow { t _ { r } } ,$ which is obtained by averaging the feature vectors of documents in $D _ { t _ { r } } .$ Eq. (5) defines the centroid vector $\overrightarrow { t _ { r } } .$ The weight of a term $k _ { i }$ in $\overrightarrow { t _ { r } }$ is represented by $w ( k _ { i } , t _ { r } )$

$$
\overrightarrow {t _ {r}} = \frac {1}{| D _ {t _ {r}} |} \sum_ {d _ {j} \in D _ {t _ {r}}} \overrightarrow {d _ {j}}\tag{5}
$$

## 4.2. Task categorization model

Previously executed tasks are categorized such that they may belong to more than one category. The task categorization database records the relationships between executed tasks and categories, namely, the degree of relevance of an executed task to a category. The degree of relevance indicates how well the task fits that category, and is calculated according to the similarity measures between the feature vectors of the categories and the executed tasks. The feature vector of a category is also expressed as a vector of weighted terms, which represents the main subjects of a category.

The categorization procedure comprises two steps: 1) deriving the feature vectors of categories; and 2) deriving the degrees of relevance between executed tasks and categories.

## 4.2.1. Deriving the feature vector of each category

Experts predefine a set of categories to represent the main subjects in the organizational domain. A seedbased approach is then applied to generate the feature vectors of categories. Experts select some previously executed tasks as seed tasks to represent a category. A centroid vector can be derived from the corpus (feature vectors) of seed tasks to denote the category by averaging the feature vectors of corresponding seed tasks.

Let X denote a set of categories, $X = \{ c _ { 1 } , c _ { 2 } , . . . , c _ { m } \}$ , and let $T _ { c _ { i } }$ represent the set of seed tasks of category $c _ { j } .$ . Also let $\overrightarrow { c _ { j } ^ { c } }$ be the centroid vector derived from the task corpus (feature vectors) of seed tasks in $c _ { j } .$ The centroid weight of the term $k _ { i }$ in $\vec { c _ { j } ^ { c } } , w ( k _ { i } , \vec { c _ { j } ^ { c } } )$ is derived by Eq. (6).

$$
w (k _ {i}, \overrightarrow {c _ {j} ^ {c}}) = \frac {1}{| T _ {c _ {j}} |} \sum_ {t _ {r} \in T _ {c _ {j}}} w (k _ {i}, t _ {r})\tag{6}
$$

The centroid vectors are used as the initial feature vectors of weighted terms to represent categories. The initial centroid weight of a term represents the degree of importance of the term in a category, without considering its importance in other categories; that is, its power to discriminate between categories. The weight of a term is further adjusted by considering its discriminating power. Common terms may not be discriminating enough to represent each category, even though they have high weights in some categories. To reduce the weight of such terms, we use the probability distribution of terms across categories to discriminate between the categories. To do this, we adjust the weight of a term in a category by multiplying its initial centroid weight by the probability distribution of the term appearing in the category.

Let $\overrightarrow { c _ { j } }$ be the feature vector of category $c _ { j }$ , which denotes the key concepts of $c _ { j } ,$ and let $w ( k _ { i } , c _ { j } )$ be the weight of term $k _ { i }$ in category $c _ { j } .$ Then $w ( k _ { i } , ~ c _ { j } )$ , the importance of term $k _ { i }$ in representing category $c _ { j } ,$ is proportional to the centroid weight of term $k _ { i }$ and the probability distribution of term $k _ { i }$ appearing in category $c _ { j } ,$ which is expressed as Eq. (7). Note that $P ( k _ { i } , c _ { j } )$ is the probability distribution of term $k _ { i }$ appearing in category $c _ { j }$ , which is computed according to the distribution of centroid weights of term $k _ { i }$ across categories.

$$
\begin{array}{l} w (k _ {i}, c _ {j}) = \frac {1}{\sqrt {\sum_ {i} (w (k _ {i} , \overrightarrow {c _ {j} ^ {c}}) \times P (k _ {i} , c _ {j})) ^ {2}}} w (k _ {i}, \overrightarrow {c _ {j} ^ {c}}) \\ \qquad \qquad \qquad \times P (k _ {i}, c _ {j}) \\ P (k _ {i}, c _ {j}) = w (k _ {i}, \overrightarrow {c _ {j} ^ {c}}) / \sum_ {j = 1} ^ {m} w (k _ {i}, \overrightarrow {c _ {j} ^ {c}}), \end{array}\tag{7}
$$

where m is the number of categories. The denominator on the right-hand side of Eq. (7) normalizes the weight of a term. $P ( k _ { i } , ~ c _ { j } )$ indicates the discriminating power of term $k _ { i } ,$ i.e., its ability to distinguish between categories.

4.2.2. Deriving the degree of relevance of executed tasks to categories

We can derive the relationship (degree of relevance) between categories and executed tasks based on the cosine measure described in Section 3.1. The relevance degree of task $t _ { r }$ to category $c _ { j } , \mu _ { c _ { j } } ( t _ { r } )$ , can be calculated as the similarity between two vectors, $\overrightarrow { t _ { r } }$ and ${ \overrightarrow { c _ { j } } } ,$ namely, cosine $( \overrightarrow { t _ { r } } , \overrightarrow { c _ { j } } )$ . The relevance degree between a task and a category indicates how well the task fits the category. The relevance degrees of task $t _ { r }$ to the m categories can be modeled as a vector $\overrightarrow { t _ { r } ^ { c } }$ expressed in Eq. (8).

$$
\overrightarrow {t _ {r} ^ {c}} = \langle \mu_ {c 1} (t _ {r}), \mu_ {c 2} (t _ {r}), \dots , \mu_ {c m} (t _ {r}) \rangle\tag{8}
$$

The task categorization database records the categorization results. The association between a task $t _ { r }$ and a category is indicated by its relevance degree to that category. The task categorization database supports the proposed two-phase task-assessment approach. Details are given in Section 5.1.

## 5. Task relevance-assessment and knowledge retrieval

The proposed mechanism generates the task profile based on the corpus of previously executed tasks and their relevance to the current task, as evaluated by knowledge workers. Our task-based knowledge support (K-support) system provides a task-based workplace that facilitates collaborative assessment by workers. Collaborative relevancy-assessment means that workers and task experts can conduct relevance assessment (i.e., by giving linguistic ratings to categories or tasks) of the current task in the task-based workplace of the K-support system, as shown in Appendix B. The assessment results of the evaluators (e.g., executors, colleagues, or experts)

are aggregated to derive the relevance of executed tasks to the current task, and integrated with the modified relevance feedback technique to derive the task profile.

Section 5.1 presents the proposed collaborative twophase relevance assessment approach, while Section 5.2 describes the modified RF technique that incorporates the aggregated relevance ratings from user assessments to generate and adjust task profiles. The retrieval of knowledge items based on task profiles is described in Section 5.3.

## 5.1. Two-phase relevance assessment based on the fuzzy linguistic approach

A novel two-phase assessment approach is used to model the relevance assessment procedure used in the collaborative workplace. The approach reduces the number of tasks to be assessed by extracting a set of reference tasks from the task database to help workers conduct task-relevance assessment. The fuzzy linguistic approach is used to assess the degree of relevance of tasks and categories.

5.1.1. Phase 1: Identifying reference tasks based on category assessment

Phase 1 of the assessment determines the degree of relevance between the current task and the categories. The reference tasks are then identified by calculating the similarity measures based on the degree of relevance of the task to the categories.

5.1.1.1. Step 1: Determining the semantic term set and corresponding fuzzy number. To model the workers' perceptions of Relevance, the system defines six linguistic terms, from “very low”, “low”, “normal”, “high”, “very high”, “perfect” to represent the degrees of relevance. Each worker has his/her own perception of the approximate value (fuzzy scale) of each linguistic term. The fuzzy scale of a linguistic term is often modeled as a triangular fuzzy number (l, m, r), as described in Section 3.3. The linguistic terms are used in the front-end of the system to provide knowledge workers a more natural and easier way to assess relevance, while fuzzy numbers are used in the back-end to compute relevance ratings. Clearly, evaluators may not have identical fuzzy numbers for the six linguistic terms of “Relevance”. For example, evaluator $\mathrm { E } _ { 1 } \mathrm { \ ' } \mathrm { s }$ perception of “very high” is (0.6, 0.7, 0.8) on the fuzzy scale, but evaluator $\mathrm { E } _ { 2 } \mathrm { ^ { * } s }$ perception of “very high” is (0.6, 0.75, 0.9). Each evaluator can use the frontend interface to select a fuzzy number for each linguistic term easily, or the default fuzzy number provided by the system can be used instead.

5.1.1.2. Step 2: Collaborative assessment of the relevance of tasks to categories. This step assesses the relevance of the current-task to each category. The executor, namely the knowledge worker responsible for the current task, rates the relevance of the task to each category by linguistic terms. Hereafter, linguistic ratings denote the ratings given to linguistic terms. In addition, task experts or colleagues can rate the relevance of the current task to each category by linguistic terms to achieve collaborative assessment through the collaborative workplace of the system. In collaborative assessment, a rating derived by aggregating the ratings of the task experts or colleagues is especially useful for a worker who is unfamiliar with the current task. However, the linguistic ratings cannot be used by the system to calculate aggregate ratings, and must therefore be transformed into crisp ratings. Linguistic ratings are transformed into crisp ratings in the backend of the system. An example of relevance assessment is shown in Appendix B. Evaluators determine the degree of relevance of the current task $t _ { e }$ to each category using linguistic ratings. The corresponding fuzzy number of each linguistic rating is transformed into a crisp number (rating) by the center-of-area method described in Appendix A. For example, an evaluator's perception of the linguistic term “very high” is (0.6, 0.7, 0.8) on the fuzzy scale. The fuzzy number is transformed into a crisp value, 0.7.

5.1.1.3. Step 3: Aggregating the relevance ratings of evaluators. Evaluators' crisp ratings obtained through collaborative assessment are aggregated in this step. The degree of relevance of the current task to each category is derived by computing the weighted average of the evaluators' crisp ratings for the relevance of the task to the categories. The aggregated relevance of the current task to the categories is expressed as a vector of degrees of relevance to each category. Let $A _ { e _ { i } } ( c _ { i } )$ denote the crisp rating of evaluator $e _ { j }$ for the relevance of the current task $t _ { e }$ to category $c _ { i }$ Also, let $w _ { e _ { j } }$ denote the associated weight, which represents the relative importance (weight) of the rating of evaluator $e _ { j } .$ . The aggregated relevance of the current task to category $c _ { i } , A _ { \mathrm { E } } ( c _ { i } )$ , is $\textstyle \sum _ { j }$ $w _ { e _ { j } ^ { A } e _ { j } } ( c _ { i } )$ . The degree of relevance of task $t _ { e } ~ \mathrm { t o }$ the categories can be modeled as a vector $\overrightarrow { t _ { e } ^ { c } } = \langle A _ { \mathrm { E } } ( c _ { 1 } )$ ; $A _ { \mathrm { E } } ( c _ { 2 } ) , \ldots , A _ { \mathrm { E } } ( c _ { m } ) \rangle$ . If $w _ { e _ { i } } = 1 / n _ { e } ,$ where $n _ { e }$ denotes the number of evaluators, then the aggregated relevance ratings are calculated as the arithmetic mean.

5.1.1.4. Step 4: Selecting reference tasks. This step identifies a subset of previously executed tasks as reference tasks based on their similarity to the current task. The degree of relevance of the current task to the categories is derived by Step 3 of the category assessment procedure, while that of an executed task is derived as described in Section 4.2. A similarity (cosine) measure is adopted to calculate the similarity between the current task and an executed task according to their degrees of relevance to the categories. Based on the similarity measures, the top-N similar executed tasks are chosen as the positive (relevant) reference tasks, and the last-M non-similar executed tasks are chosen as the negative (irrelevant) reference tasks. The reference tasks are used for further task-relevance assessment in phase 2.

The similarity between the current task $t _ { e }$ and an executed task $t _ { r }$ can be computed as the cosine of the angle between two vectors, $\overrightarrow { t _ { e } ^ { c } }$ and $\overrightarrow { t _ { r } ^ { c } } ,$ , namely, cosine $( \overrightarrow { t _ { e } } , \overrightarrow { t _ { r } } ) ; \overrightarrow { t _ { e } }$ is derived by the collaborative relevance assessment described in Step 3, while $\overrightarrow { t _ { r } ^ { c } }$ is derived by the categorization model described in Section 4.2.

## 5.1.2. Phase 2: Assessing the relevance of reference tasks

Phase 2 assesses the relevance of the reference tasks to the current task. The evaluators assess the degree of relevance between the current task and the reference tasks without reviewing all tasks. The task assessment procedure is similar to that of category assessment. The evaluators use linguistic terms to assess the degree of relevance of each reference task to the current task. The aggregated relevance rating of a reference task is derived by computing the weighted average of the evaluators crisp ratings for the relevance of the reference task to the current task. The degrees of relevance of the reference tasks to the current task are then used to construct the task profile of the current task, as described in Section 5.2.

Let $A _ { e _ { j } } ( t _ { r } )$ represent the crisp rating of evaluator $e _ { j }$ for the relevance of a reference task $t _ { r }$ to the current-task. Also, let $w _ { e _ { j } }$ denote the associated weight representing the relative importance (weight) of the rating of evaluator $e _ { j } .$ The aggregated relevance rating of task $t _ { r }$ to the current-task, $A _ { \mathrm { E } } ( t _ { r } )$ is $\textstyle \sum _ { j } w _ { e _ { j } ^ { \boldsymbol { A } } e _ { j } } ( t _ { r } )$ .

## 5.2. Constructing the task profile based on relevance feedback

The task profile of the current task is initially derived by analyzing the task contents (textual descriptions), or alternatively by using the corresponding task corpus. However, the initial task profile may not properly represent the current task. Collaborative task-assessment identifies the degrees relevance of the reference tasks to the current task. The result is used to refine the initial task profile based on the relevance feedback (RF) techniques introduced in Section 3.2.

Two kinds of relevance judgments about reference tasks are considered: positive feedback and negative feedback. The standard RF technique employs binary feedback without considering the degrees of relevance, as shown in Eq. (9). Relevant tasks with positive feedback have a positive influence on the weights of terms, while irrelevant tasks with negative feedback have a negative influence on the weights of terms. A refined task profile can be generated by adding the term weights of relevant tasks and subtracting the term weights of irrelevant tasks. Consequently, the feature vector of new term weights based on the RF technique forms a new task profile for further knowledge retrieval. Relevance feedback shifts the new profile closer to the relevant task set and away from the irrelevant task set. The parameters $\beta$ and $\gamma ,$ respectively, are used to determine the relative influence of the relevant task set compared to the irrelevant task set.

We modify the Rocchio and Ide\_Dec\_Hi methods by considering the degrees of relevance of reference tasks obtained from the aggregated relevance ratings of fuzzy linguistic assessment. The modification considers the relative importance of relevant and irrelevant tasks from the user's perspective. The feature vectors of reference tasks are multiplied by their relevance degrees to reflect their relative contributions to the refinement of the task profile, as expressed in Eq. (10).

Based on above discussions, two RF approaches are used to construct the task profile $\overrightarrow { S _ { e } }$ of the current task $t _ { e } .$ The RF with binary relevance assessment, denoted as B-RA (Eq. (9)), considers binary (relevant and irrelevant) assessment. The RF with fuzzy linguistic relevance assessment, denoted as F-RA (Eq. (10)), considers the degrees of relevance based on user perceptions.

$$
\mathrm{B} - \mathrm{RA}: \overrightarrow {S _ {e}} = \alpha \overrightarrow {S _ {\text { initial }}} + \beta \sum_ {\forall t _ {j} \in T _ {r}} \overrightarrow {t _ {j}} - \gamma \sum_ {\forall t _ {j} \in T _ {n}} \overrightarrow {t _ {j}}\tag{9}
$$

$$
\begin{array}{l} \mathrm{F-RA:} \overrightarrow {S _ {e}} = \alpha \overrightarrow {S _ {\text { initial }}} + \beta \sum_ {\forall t _ {j} \in T _ {r}} (w _ {t _ {j}}) \overrightarrow {t _ {j}} \\ - \gamma \sum_ {\forall t _ {j} \in T _ {n}} (1 - w _ {t _ {j}}) \overrightarrow {t _ {j}}, \end{array}\tag{10}
$$

where $\overrightarrow { S _ { \mathrm { i } } }$ represents the initial profile derived by analyzing the relevant documents, if available, for the current task; and. $T _ { r }$ denotes the set of relevant tasks selected from the positive reference tasks according to the collaborative assessment of experts and workers. $T _ { n }$ represents the set of the last-M irrelevant tasks, which the system selects automatically; $\overrightarrow { t _ { j } }$ is the task corpus of a reference task $t _ { j }$ with an associated weight $w _ { t _ { i } }$ representing the relevance of $t _ { j }$ to the current task; $w _ { t _ { j } }$ is set to

$A _ { \mathrm { E } } ( t _ { j } ) .$ , which is the aggregated relevance rating of task $t _ { j }$ to the current task; $A _ { \mathrm { E } } ( t _ { j } )$ is derived by the task assessment procedure described in Section 5.1.2; and $\alpha , \beta ,$ and $\gamma$ are tuning constants.

The task profile of the current task $t _ { e } ,$ derived from Eq. (9) or (10) can be expressed as a feature vector of weighted terms, $\overrightarrow { S _ { e } } = \langle w ( k _ { 1 } , t _ { e } ) , w ( k _ { 2 } , t _ { e } ) , \ldots , w ( k _ { n } , t _ { e } ) \rangle$ 1 where $w ( k _ { i } , t _ { e } )$ is the weight of a term $k _ { i }$ representing the main concept terms of $t _ { e , } \mathrm { ~ , ~ }$ and n denotes the number of discriminating terms. $S _ { e } ^ { ' }$ is used to retrieve relevant codified knowledge.

## 5.3. Task-based knowledge retrieval

A task-based knowledge support system can be realized with the proposed systematic profile modeling approach. The generated task profile is the system kernel that streamlines knowledge retrieval activity to provide task-based knowledge support. Based on task profiles, the system can recommend/retrieve relevant knowledge from the repository to assist knowledge workers. Workers conducting further search activity are assisted by the highly correlated term set presented in the system interface. The relevant knowledge includes relevant tasks, associated peer groups, relevant documents, and highly correlated term sets.

The similarity between the current task and the codified knowledge items can be calculated to select the top-N relevant tasks or documents from the knowledge repository. The cosine measure of feature vectors, described in Section 3.1, can be used to derive the similarity measure. The task profile can be further adjusted during the task's execution by monitoring the workers' feedback. Our recent paper [25] presented an adaptive task-based profiling approach for modeling workers' dynamic task needs. The codified knowledge that is relevant to the current task can be retrieved based on the adjusted task profile to fit the worker's dynamic information needs. Moreover, knowledge sharing among peer group members with similar interests is important in deploying a KMS. Task-based peer-group members with similar task needs can be identified from the retrieved relevant task set to provide knowledge sharing. The method for identifying task-based peer groups that can support knowledge sharing is also presented in [25].

## 5.3.1. Relevant tasks and peer group recommendations

As the task profile has been derived, retrieving relevant tasks for references would be helpful. The cosine measure is calculated to derive the similarity between the current task and an executed task. The tasks with the top-N similarity measures are recommended as relevant tasks.

These tasks and the knowledge workers engaged in them are recommended for consultation. Effectively codifying tacit knowledge may be difficult. However, the system can locate valuable knowledge sources, such as knowledge workers engaged in relevant tasks, thereby providing a knowledge support platform for gathering and exchanging task-relevant knowledge among workers.

## 5.3.2. Relevant documents and term recommendation

Relevant documents are retrieved using the profile of the current-task. Similarity measurement is also used to select the top-N relevant documents. Documents with top-N similarity measures are selected as the relevant documents for recommendation. Meanwhile, the important term set representing the main concept terms of the current task is derived from the constructed task profile. The system displays the discriminating terms and their associated weights to assist knowledge workers with further retrieval. The term set forms the task corpus of the current task, and can be modified during subsequent stages of the task's execution.

## 6. Experiment evaluations

Three experiments were performed to evaluate the effectiveness of assessment and retrieval based on the proposed methods. Section 6.1 describes the experiment setup, including the experiments' objectives, data, evaluation metrics, and related parameter selection. Section 6.2 presents the experiment results.

## 6.1. Experiment setup

## 6.1.1. Experiment objectives

We conducted the following three experiments to evaluate the effectiveness of the proposed collaborative relevance-assessment approach: (1) Experiment one evaluated whether building task profiles based on binary or fuzzy linguistic relevance assessment method could help knowledge workers retrieve task-relevant information more precisely than the query-based method. The latter method, which simply employs traditional keyword search to access knowledge items without profile generation, is a user-driven approach that enables knowledge workers to express their information needs as queries to search for knowledge items. The experiment also evaluated the effectiveness of fuzzy linguistic assessment for two worker groups: experienced workers and novices. (2) Experiment two evaluated whether the proposed two-phase relevance assessment approach can reduce the assessment load created by a large number of tasks. (3) Experiment three evaluated whether the proposed collaborative relevance-assessment method helps knowledge workers find taskrelevant information more precisely with the aid of domain experts.

## 6.1.2. Data and participants

Experiments were performed using a real application domain, namely, research tasks in the laboratory of a research institute. The tasks consisted of writing research papers or conducting research projects. Using a real application domain restricts the sample size of the data and the number of participants in the experiments. Fifty research tasks were studied: 31 executed tasks and 19 current tasks; and eighteen workers were selected to participate in the experiments. Over 500 documents accessed by the tasks were collected. Information extraction and document pre-processing (e.g., case folding, stemming, and stop word removal) identified an average of 90 distinct terms in each document. The feature vectors of the documents were derived by the method described in Section 3.1. Historical executed tasks were categorized into five categories defined according to the ACM Computing Classification Systems.

Knowledge workers usually require a substantial amount of time (e.g., 1 year) to accomplish knowledgeintensive tasks. However, when the task performance process spans a long period, it is difficult to design experiments relevant to real-world problems. Thus, we chose evaluators according to whether they were familiar or unfamiliar with the current task's execution. Consequently, two worker groups were chosen: experienced workers familiar with the current task, and novices unfamiliar with the current task.

Six current tasks were chosen as the test set for the evaluations. To determine the effectiveness of collaborative relevance-assessment, current tasks in the test set were those in which more than one knowledge worker participated. We also chose current tasks conducted by at least one novice and one experienced worker to evaluate the effectiveness of the proposed methods for different worker groups. We selected one or two experienced workers and one or two novices from each test task as participants in the test set. The limitation of the test set selection for the problem domain restricted the test set size.

## 6.1.3. Performance evaluation metrics

Experiments were conducted to evaluate the effectiveness of our approach for retrieving knowledge items. We adopted the evaluation methodology used in Information Retrieval (IR). The IR evaluation methodology concentrates on the evaluation of quantitative or qualitative data [7]. Retrieval effectiveness is the most commonly used criterion for quantitative evaluation. Qualitative evaluation of an IR system can be conducted based on various criteria, such as user satisfaction, usability and learning ability through the analysis of questionnaires. Our evaluation focused on the effectiveness of retrieval. Thus, various approaches are compared and discussed according to their performance in terms of the evaluation criteria of retrieval effectiveness. Precision and recall are commonly used evaluation metrics to measure the effectiveness of information retrieval [33].

Precision is the fraction of retrieved items (tasks or documents) that are relevant, while recall is the fraction of total known relevant items that are retrieved, defined as Eqs. (11) and (12).

$$
\text { precision } = \frac {| \text { retrieved   items   that   are   relevant } |}{| \text { total   retrieved   items } |}\tag{11}
$$

$$
\text { recall } = \frac {| \text { relevant   items   that   are   retrieved } |}{| \text { total   known   relevant   items } |}\tag{12}
$$

Both the total number of retrieved items and the total number of known relevant items must be greater than zero. Increasing the number of retrieved items tends to reduce precision and increase recall. Generally, precision is high at low recall levels and low at high recall levels. Thus, a recall-precision curve can be used to show the trade-off between precision and recall [4,36]. We evaluate the effectiveness of the proposed knowledge retrieval approach based on the recall-precision curves, which treat precision as a function of recall. The recallprecision curve plots the interpolated precision at each recall level, as follows [4,36]. The recall values are divided into different recall levels with $\operatorname { r v } _ { i } , i \in \{ 1 , 2 , . . . , n \}$ denoting a reference point at the i-th recall level. The interpolated precision, $\mathrm { I P } _ { r } ( \mathrm { r v } _ { i } )$ can thus be expressed as $\mathrm { I P } _ { r } ( \mathrm { r v } _ { i } ) { = } \mathrm { M A X } \ P _ { r } ( \mathrm { r v } )$ for $\mathbf { r v } _ { i } { \leq } \mathbf { r v } { < } \mathbf { r v } _ { i + 1 } ,$ , where $P _ { r } ( \mathbf { r v } )$ represents the precision value given a recall value of rv.

The interpolated precision of each recall level can be derived for each task. The average interpolated precision for evaluating a set of tasks is derived by Eq. (13).

$$
\operatorname{aveIP} _ {r} \left(\mathrm{rv} _ {i}\right) = \sum_ {j = 1} ^ {k} \frac {\mathrm{IP} _ {r} ^ {j} \left(\mathrm{rv} _ {i}\right)}{k}\tag{13}
$$

where $\mathrm { a v e I P } ( \mathrm { r v } _ { i } )$ denotes the average interpolated precision at the i-th recall level; k denotes the number of evaluated tasks; and $\mathrm { I P } _ { r } ^ { j } ( \mathbf { r v } _ { i } )$ denotes the interpolated precision of task j.

## 6.1.4. Parameter selection

We adopt and modify the classical relevance feedback methods to design the proposed relevance feedback methods. Salton and Buckley [32] suggested the steps of a pilot experiment to determine the parameters of the two classical relevance feedback methods. Their results suggest that setting α= 1, $\beta { = } 0 . 7 5$ , and $\gamma { = } 0 . 2 5$ can improve retrieval performance (i.e., a higher precision value). This work uses a similar approach to that suggested by Salton and Buckley to determine the parameter settings.

We conducted a pilot experiment to determine the parameter values of $\alpha , \beta$ and γ in Eqs. (9) and (10). To adjust the relative importance of relevant and irrelevant tasks, we set $\mathsf { \alpha } \mathsf { = } 1$ and $\beta + \gamma = 1$ . Accordingly, only one parameter had to be determined $( \beta \ o \mathrm { o r } \gamma )$ . The experiment was conducted by systematically adjusting the value of $\beta$ in increments of 0.1. The precision metric (given in Eq. (11)) was chosen as the performance measure to evaluate the effectiveness of the methods. The optimal parameter values with the best results (the highest precision values) were chosen as the parameter settings of the proposed equations. The experiment results suggest that the best result can be achieved by setting $\mathsf { \alpha } \mathsf { \alpha } \partial _ { \mathsf { \alpha } } = 1$ $\beta { = } 0 . 8$ , and $\gamma { = } 0 . 2$ . This finding agrees with the conclusion of most previous studies that the information in relevant documents is more important than that in irrelevant documents. Thus, the above parameter settings were adopted in our experiments.

## 6.2. Experiment results

Experiment one compares the binary relevance assessment method (B-RA method) and the fuzzy linguistic relevance assessment method (F-RA method) with the query-based method. B-RA and F-RA are onephase relevance assessment methods that only conduct task-relevance assessment (phase 2), as described in Section 5.2, without employing phase-1 category-relevance assessment and collaborative assessment. Experiment two measures the impact of the assessment load while conducting task-relevance assessment. Accordingly, the two-phase relevance assessment approach (denoted as 2-F-RA) is compared with the one-phase relevance assessment approach, F-RA. The 2-F-RA method conducts both the phase-1 category relevance assessment and the phase-2 task-relevance assessment without employing collaborative assessment. The phase-1 assessment determines the relevance of the current task to the categories, and then identifies the reference tasks by computing the similarity measures based on the degree of relevance of the tasks to the categories. The third experiment evaluates the effectiveness of collaborative two-phase assessment (denoted as Collaborative 2-F-RA) versus non-collaborative two-phase assessment (2-F-RA). Collaborative assessment aggregates the relevance ratings derived from the assessments of experts and collaborative workers.

## 6.2.1. Experiment one: effect of fuzzy linguistic assessment

This experiment evaluates the effectiveness of finding task-relevant information by the query-based method, the B-RA method and the F-RA method. The B-RA method employs binary (relevant and irrelevant) assessment and relevance feedback without considering the degree of relevance. The F-RA method considers the degree of relevance in the assessment and in relevance feedback, i.e., it models the user's perception value by the fuzzy linguistic rating approach. Recall that the B-RA and F-RA methods conduct task-relevance assessment (phase 2) without employing phase-1 categoryrelevance assessment or collaborative assessment.

As noted earlier, six current tasks were chosen as test tasks. The experiment employed two worker groups: experienced workers and novices. Table 1 shows the effectiveness of knowledge support for task-retrieval by listing the average interpolated precision of each recall level, computed over the test tasks, for the three methods and the two worker groups. The recall level $\left[ \mathrm { r v } _ { i } , \mathrm { r v } _ { i + 1 } \right)$ denotes the interval of recall values that satisfy $\mathrm { r v } _ { i } \leq \mathrm { r e c a l l } < \mathrm { r v } _ { i + 1 }$ . The last row shows the average precision values computed over all recall levels.

6.2.1.1. Observations and implications. The average precision values of the B-RA and F-RA methods exceed those of the query-based method for both experienced workers and novices. The results show that building task profiles by assessing the relevance of previously executed tasks can help knowledge workers retrieve task-relevant information. For experienced knowledge workers, the average precision of F-RA is higher than that of B-RA. This result indicates that the F-RA method provides better knowledge support to experienced workers than the B-RA method.

Fig. 2 plots the average recall-precision curves of the three proposed methods, and shows a gradual decrease in the average precision value. E\_F-RA and E\_B-RA denote experienced workers, while and N\_F-RA and N\_B-RA denote “novices”. The experiment results show that the average precision values of F-RA and B-RA for experienced workers exceed those of F-RA and B-RA for novices. Thus, the proposed assessment approach provides experienced workers with better knowledge support than novices.

Interestingly, the average precision values of B-RA and F-RA for novices are similar. Table 2 lists the average precision values of task retrieval for ten novices. In three cases, the average precision value of F-RA is lower than that of B-RA. We observe that some novices cannot obtain better knowledge support from F-RA than they obtain from B-RA. This result implies that experienced workers are knowledgeable about making appropriate assessments regarding the degree of relevance using the fuzzy linguistic approach. However, some novices do not have sufficient knowledge to determine the degree of relevance of the current task and previously executed tasks. Therefore, a simple binary assessment (relevant or irrelevant) may be more appropriate for novices.

Result of knowledge support for task retrieval (B-RA versus F-RA)

<table><tr><td rowspan="3">Recall level</td><td colspan="3">Experience users</td><td colspan="3">Novices</td></tr><tr><td>Query</td><td>B-RA</td><td>F-RA</td><td>Query</td><td>B-RA</td><td>F-RA</td></tr><tr><td>Precision</td><td>Precision</td><td>Precision</td><td>Precision</td><td>Precision</td><td>Precision</td></tr><tr><td>[0.0, 0.2)</td><td>1.000</td><td>1.000</td><td>1.000</td><td>1.000</td><td>1.000</td><td>1.000</td></tr><tr><td>[0.2, 0.4)</td><td>0.745</td><td>0.945</td><td>0.944</td><td>0.670</td><td>0.762</td><td>0.762</td></tr><tr><td>[0.4, 0.6)</td><td>0.645</td><td>0.833</td><td>0.889</td><td>0.566</td><td>0.648</td><td>0.644</td></tr><tr><td>[0.6, 0.8)</td><td>0.502</td><td>0.733</td><td>0.820</td><td>0.458</td><td>0.610</td><td>0.600</td></tr><tr><td>[0.8, 1.0)</td><td>0.497</td><td>0.616</td><td>0.623</td><td>0.403</td><td>0.402</td><td>0.407</td></tr><tr><td>[1.0, 1.0]</td><td>0.333</td><td>0.395</td><td>0.396</td><td>0.359</td><td>0.331</td><td>0.351</td></tr><tr><td>6-pt average precision</td><td>0.620</td><td>0.754</td><td>0.779</td><td>0.576</td><td>0.626</td><td>0.627</td></tr></table>

The data in bold indicates that the value of the method is higher than that of the other method in the comparison.

Table 3 shows the results of knowledge support for document-retrieval based on the B-RA and F-RA methods. The observations and implications of document retrieval are similar to those of task retrieval.

## 6.2.2. Experiment two: effect of two-phase relevance assessment

This experiment evaluates whether reducing the number of tasks for assessment can help workers conduct task relevance assessment. The effectiveness of knowledge support is evaluated by two-phase fuzzy linguistic relevance assessment (2-F-RA) and one-phase fuzzy linguistic relevance assessment (F-RA). Experiment one demonstrates that the average precision values of F-RA method exceed those of the B-RA and query-based methods, especially for the experienced workers. Therefore, we chose the F-RA method instead of the B-RA method or query-based method for comparison with the 2- F-RA method. The 2-F-RA approach reduces the number of tasks by selecting reference tasks based on category assessment (phase 1) described in Section 5.1.1. The onephase F-RA approach conducts task relevance assessment (phase 2) without performing phase-1 assessment.

Tables 4 and 5 show the effectiveness of task-retrieval and document-retrieval, using the F-RA and 2-F-RA methods respectively. Fig. 3 plots the average recall-precision curves of two assessment methods based on Table 4.

6.2.2.1. Observations and implications. The results show that the overall average precision using the 2-F-RA method is higher than that of F-RA method for both worker groups. This implies that two-phase relevance assessment (2-F-RA) provides better knowledge support for task and document retrieval than the F-RA method. Because category assessment (phase 1) reduces the burden of assessing the relevance of a large number of tasks, two-phase assessment can help workers conduct task-relevance assessment more effectively than onephase assessment.

Fig. 3 shows that knowledge support is more effective for experienced workers than for novices. Experienced workers (E\_2-F-RA, E\_F-RA) are more knowledgeable and thus derive more effective knowledge support than novices (N\_2-F-RA, N\_F-RA). However, in Fig. 3, the curves for novices cross at some points. We made a further check of each case and found that, in two cases, the average precision value of 2-F-RA was lower than that of F-RA. In other words, some novices could not obtain better knowledge support from two-phase assessment than from one-phase assessment. On the other hand, the average precision value of 2-F-RA was higher than that of F-RA for each case of experienced workers. The result implies that, for some novices, one method does not help them more than the other in the retrieval of task-relevant knowledge. This is because they are unfamiliar with their tasks and therefore find it difficult to perform task-relevant assessments. Thus, some novices may require assistance with the assessment task.

![](/api/attachments/UXUZ667S/fulltext/images/9f7650bcad88cc1ae28cbb886ced936ffa6c2e89d8ac10b59c8fdffa515fcad6.jpg)  
Fig. 2. Average recall-precision curves for task retrieval by experienced workers and novices.

Table 2  
Results of knowledge support for task retrieval by ten novices

<table><tr><td></td><td> $N_1(T_1)$ </td><td> $N_2(T_2)$ </td><td> $N_3T(2)$ </td><td> $N_4(T_3)$ </td><td> $N_5(T_4)$ </td><td> $N_6(T_4)$ </td><td> $N_7(T_5)$ </td><td> $N_8(T_5)$ </td><td> $N_9(T_6)$ </td><td> $N_{10}(T_6)$ </td></tr><tr><td>B-RA</td><td>0.778</td><td>0.549</td><td>0.643</td><td>0.691</td><td>0.814</td><td>0.577</td><td>0.450</td><td>0.644</td><td>0.571</td><td>0.462</td></tr><tr><td>F-RA</td><td>0.786</td><td>0.559</td><td>0.643</td><td>0.691</td><td>0.805</td><td>0.552</td><td>0.467</td><td>0.647</td><td>0.508</td><td>0.475</td></tr></table>

The data in bold indicates that the value of the method is higher than that of the other method in the comparison.

## 6.2.3. Experiment three: effect of collaborative assessment

The objective of this experiment is to show that collaborative assessment reduces the workload of novices and helps them find task-relevant information. Novices who are less knowledgeable about a task in the initial stages may have difficulty in performing task-relevance assessment. The effect of collaborative assessment is compared with that of non-collaborative assessment. Experiment two showed that two-phase relevance assessment (2-F-RA) provides better knowledge support for task retrieval and document retrieval than the F-RA method. This experiment goes a step further and evaluates the effectiveness of collaborative relevance assessment. Collaborative assessment aggregates the relevance ratings derived from the assessment of experienced workers and novices, as discussed in Section 5.1.2. The individual assessments of novices are considered as non-collaborative assessments to derive the ratings of task relevance.

Table 3

<table><tr><td rowspan="3">Recall level</td><td colspan="2">Experience workers</td><td colspan="2">Novices</td></tr><tr><td>B-RA</td><td>F-RA</td><td>B-RA</td><td>F-RA</td></tr><tr><td>Precision</td><td>Precision</td><td>Precision</td><td>Precision</td></tr><tr><td>[0.0, 0.2)</td><td>0.650</td><td>0.650</td><td>0.669</td><td>0.703</td></tr><tr><td>[0.2, 0.4)</td><td>0.280</td><td>0.306</td><td>0.184</td><td>0.203</td></tr><tr><td>[0.4, 0.6)</td><td>0.238</td><td>0.271</td><td>0.172</td><td>0.189</td></tr><tr><td>[0.6, 0.8)</td><td>0.202</td><td>0.227</td><td>0.155</td><td>0.168</td></tr><tr><td>[0.8, 1.0)</td><td>0.150</td><td>0.168</td><td>0.140</td><td>0.152</td></tr><tr><td>[1.0, 1.0]</td><td>0.129</td><td>0.144</td><td>0.129</td><td>0.134</td></tr><tr><td>6-pt average precision</td><td>0.275</td><td>0.294</td><td>0.242</td><td>0.258</td></tr></table>

Results of knowledge support for document retrieval (B-RA versus F-RA)  
The data in bold indicates that the value of the method is higher than that of the other method in the comparison.

Table 6 shows the effectiveness of knowledge support for task retrieval and document retrieval under collaborative 2-F-RA (by Experienced workers and Novices) and non-collaborative 2-F-RA (by novices). The comparison is based the average interpolated precision at six recall levels and their aggregated average.

6.2.3.1. Observations and implications. The results show that the collaborative 2-F-RA method is more effective than the non-collaborative 2-F-RA method. Thus, novices can obtain more effective knowledge support through collaboration with experienced workers by adopting the collaborative relevance-assessment approach. Collaboration among knowledge workers can also mitigate the difficulty of retrieving task-relevant knowledge from the knowledge repository.

Experiments were conducted to evaluate the effectiveness of the proposed collaborative relevance-assessment approach (Collaborative 2-F-RA). In all, we conducted three experiments to assess the effect of linguistic assessment, two-phase relevance assessment, and collaborative assessment respectively. The results demonstrate that: (1) linguistic relevance assessment (F-RA) provides better knowledge support than binary assessment (B-RA) or the query-based method; (2) two-phase relevance assessment (2-F-RA) provides better knowledge support

## 6.2.4. Discussion

Table 4  
Knowledge support for task-retrieval (2-F-RA versus F-RA)

<table><tr><td rowspan="3">Recall level</td><td colspan="2">Experience workers</td><td colspan="2">Novices</td></tr><tr><td>F-RA</td><td>2-F-RA</td><td>F-RA</td><td>2-F-RA</td></tr><tr><td>Precision</td><td>Precision</td><td>Precision</td><td>Precision</td></tr><tr><td>[0.0, 0.2)</td><td>1.000</td><td>1.000</td><td>1.000</td><td>1.000</td></tr><tr><td>[0.2, 0.4)</td><td>0.944</td><td>0.958</td><td>0.762</td><td>0.812</td></tr><tr><td>[0.4, 0.6)</td><td>0.889</td><td>0.945</td><td>0.644</td><td>0.728</td></tr><tr><td>[0.6, 0.8)</td><td>0.820</td><td>0.883</td><td>0.600</td><td>0.556</td></tr><tr><td>[0.8, 1.0)</td><td>0.623</td><td>0.659</td><td>0.407</td><td>0.461</td></tr><tr><td>[1.0, 1.0]</td><td>0.396</td><td>0.484</td><td>0.351</td><td>0.357</td></tr><tr><td>6-pt average precision</td><td>0.779</td><td>0.822</td><td>0.627</td><td>0.652</td></tr></table>

The data in bold indicates that the value of the method is higher than that of the other method in the comparison.

Table 5  
Knowledge support for document retrieval (2-F-RA versus F-RA)

<table><tr><td rowspan="3">Recall level</td><td colspan="2">Experience workers</td><td colspan="2">Novices</td></tr><tr><td>F-RA</td><td>2-F-RA</td><td>F-RA</td><td>2-F-RA</td></tr><tr><td>Precision</td><td>Precision</td><td>Precision</td><td>Precision</td></tr><tr><td>[0.0, 0.2)</td><td>0.650</td><td>0.803</td><td>0.703</td><td>0.800</td></tr><tr><td>[0.2, 0.4)</td><td>0.306</td><td>0.351</td><td>0.203</td><td>0.226</td></tr><tr><td>[0.4, 0.6)</td><td>0.271</td><td>0.320</td><td>0.189</td><td>0.209</td></tr><tr><td>[0.6, 0.8)</td><td>0.227</td><td>0.241</td><td>0.168</td><td>0.174</td></tr><tr><td>[0.8, 1.0)</td><td>0.168</td><td>0.177</td><td>0.152</td><td>0.149</td></tr><tr><td>[1.0, 1.0]</td><td>0.144</td><td>0.145</td><td>0.134</td><td>0.137</td></tr><tr><td>6-pt average precision</td><td>0.294</td><td>0.340</td><td>0.258</td><td>0.282</td></tr></table>

The data in bold indicates that the value of the method is higher than that of the other method in the comparison.

than one-phase relevance assessment (F-RA); and (3) collaborative relevance assessment (Collaborative 2-F-RA) provides better knowledge support than noncollaborative relevance assessment (2-F-RA). Although the improvement achieved by adding one more factor is not significant, the improvement of the collaborative 2-F-RA method over the query-based method is significant. The results of the query-based method (baseline method) are listed in Table 1, and the results of the collaborative relevance assessment method (Collaborative 2-F-RA) are listed in Table 6. For novices, collaborative 2-F-RA is 25.86% more effective than the query-based method. The results demonstrate that the proposed collaborative relevance-assessment approach can provide effective knowledge support in task-based environments.

As one would expect, experienced workers are more knowledgeable about relevance assessment than novices, and can therefore make appropriate assessments using the fuzzy linguistic approach. In contrast, a simple binary assessment (relevant or irrelevant) approach may be more appropriate for some novices when they are unfamiliar with a task. Novices may also benefit from collaboration with experienced workers when conducting task relevance-assessment.

Our results indicate that two-phase assessment (incorporated with category assessment) can help workers conduct task-relevance assessment more effectively than onephase assessment. In our preliminary experiment, we asked the subjects to evaluate the tasks (i.e., to indicate the degree of relevance by a fuzzy linguistic rating). Unfortunately, we found the assessment was very time-consuming because there were too many task items (fifty-one in our application domain) that needed to be browsed or read in advance. Thus, we sought to classify the tasks into five categories which were predefined by experts to generalize our application domain. In our experiment, we found that two-phase assessment is more effective than one-phase assessment for both types of worker groups, but especially for experienced workers, who can make better assessments than novices. The experiment results suggest that multilevel categorization can further reduce the assessment load. However, we also observed that some novices were confused about the categories. Novices may have difficulty in recognizing the differences between categories and understanding the topic of each category. This observation implies that increasing the levels of categorization structure may also increase a worker's assessment burden.

Table 6  
Results of knowledge support (non-collaborative 2-F-RA versus collaborative 2-F-RA)

<table><tr><td rowspan="3">Recall level</td><td colspan="2">Task retrieval</td><td colspan="2">Document retrieval</td></tr><tr><td>Non-C.2-F-RA(Novice)</td><td>Colla.2-F-RA(E and N)</td><td>Non-C.2-F-RA(Novice)</td><td>Colla.2-F-RA(E and N)</td></tr><tr><td>Precision</td><td>Precision</td><td>Precision</td><td>Precision</td></tr><tr><td>[0.0, 0.2)</td><td>1.000</td><td>1.000</td><td>0.800</td><td>0.863</td></tr><tr><td>[0.2, 0.4)</td><td>0.812</td><td>0.873</td><td>0.226</td><td>0.232</td></tr><tr><td>[0.4, 0.6)</td><td>0.728</td><td>0.868</td><td>0.209</td><td>0.216</td></tr><tr><td>[0.6, 0.8)</td><td>0.556</td><td>0.666</td><td>0.174</td><td>0.181</td></tr><tr><td>[0.8, 1.0)</td><td>0.461</td><td>0.527</td><td>0.149</td><td>0.155</td></tr><tr><td>[1.0, 1.0]</td><td>0.357</td><td>0.415</td><td>0.137</td><td>0.137</td></tr><tr><td>6-pt average precision</td><td>0.652</td><td>0.725</td><td>0.282</td><td>0.296</td></tr></table>

The data in bold indicates that the value of the method is higher than that of the other method in the comparison.

Generally, if the number of categories is large, multilevel categorization may further reduce the burden of category assessment. Based on our observations of the experiments, we address the tradeoff and justification for two-phase assessment from two aspects: width (i.e., the number of categories in each level) and depth (i.e., the levels of categorization). With regard to the width of a multi-level structure, a large number of categories in a level may increase the user's workload when assessing knowledge items; thus, the quality of knowledge retrieval will be reduced. On the other hand, more levels of categorization may reduce the user's assessment load at each level. However, workers need to interact with the system to conduct one assessment phase for each level of categorization. Thus, more categorization levels may increase a user's workload because it means conducting more assessments. In this research, five categories are sufficient to generalize our application domain; thus, we only adopt a two-level categorization structure.

![](/api/attachments/UXUZ667S/fulltext/images/76cf6e9e38c6befcd054c21259011b0c3293ce80410f2bc433d12a6a8ce7ebf3.jpg)  
Fig. 3. Average recall-precision curves for task retrieval by experienced workers and novices.

Multi-level categorization is a complex problem in the fields of information retrieval and machine learning, since it is difficult to determine the proper levels of categorization to describe the problem domain. Furthermore, it is difficult to label categories to properly represent the topics of each node in a multi-level categorization structure. It would be very interesting to investigate the effect of multilevel categorization on the assessment results. Thus, future studies could apply our approach to application domains with more categories to evaluate the effect of multi-level categorization on relevance assessment.

This work addresses the issue of how to effectively model a worker's initial task-needs when there are very few or even no textual descriptions of the task available to extract concept terms for the task-at-hand. Since similarity analysis based on concept terms is not effective in deriving initial task needs, we propose a user-assessment approach that evaluates task relevance for construction of appropriate task profiles that model initial task needs. As a worker's information needs may vary during the performance of a task, task profiles need to be adjusted to model the worker's dynamic information needs. Our evaluations focus on verifying the effectiveness of the proposed assessment approach in generating task profiles without considering the adaptation of the profiles to model the worker's dynamic task needs. The task profile can be further adjusted during the performance of the task by monitoring the worker's feedback. Knowledge items that are relevant to the task can be retrieved based on the adjusted task profile to meet the worker's current information needs. Our recent work [25] presented an adaptive task-based profiling approach for modeling workers' dynamic task needs.

Our experiments were conducted using a real application domain, i.e., research tasks in a research institute's laboratory. The real application domain restricted the sample size of the data and the number of participants in the experiments. Because of this limitation, our proposed approach needs to be further verified on other application domains involving a larger number of workers, tasks and documents. Moreover, our evaluation focused on verifying the effectiveness of the proposed approach for knowledge retrieval, rather than on user satisfaction or the system's usability. In the future, investigation of user satisfaction or a usability study could provide further insights into using our system to provide task-relevant knowledge in task-based environments.

## 7. Conclusions and future work

We employ a fuzzy linguistic approach for conducting relevance assessment by knowledge workers. A twophase assessment process is proposed to reduce the assessment workload, and a modified relevance feedback method is adopted to generate task profiles based on the assessment. Task profiles provide effective knowledge support as they help knowledge workers identify taskrelevant information. Experiment results demonstrate the effectiveness of the proposed approach in providing taskbased knowledge support in task-based environments.

Knowledge workers usually require a substantial amount of time to accomplish knowledge intensive tasks. For such long-term tasks, the information needs of the workers may vary according to different stages of the task. Our experiments were limited to evaluating the proposed approach in terms of knowledge workers' familiarity with a current task, i.e., experienced workers versus novices, without considering their stages of progress during performance of the task. In our future work, we will extend our approach to address issues of providing longterm knowledge support for the various stages of a task.

This work focuses on providing knowledge support for knowledge-intensive tasks such as thesis-writing, research projects, project management, and product development. We have not considered the process-aspect and context awareness, as discussed in [1,11,23]. Process knowledge supports the operations of workflow management systems in managing business processes. Context-based knowledge support, on the other hand, utilizes the context of activities, roles, and work-related skills to provide contextaware knowledge access and retrieval. Future studies could extend the proposed approach to support context-aware or process-aware delivery of task-relevant knowledge.

Moreover, this work focuses on generating task profiles through the collaboration of knowledge workers in order to analyze the relevance of tasks and codified knowledge. Our work is further enhanced by the development of a knowledge support (K-support) system that stimulates knowledge sharing among task-based peer groups. The details of knowledge sharing and peer-group identification were presented in our recent work [25]. Although the K-support system can facilitate collaboration among knowledge workers through collaborative assessment and knowledge-sharing, more computer supported collaborative work (CSCW) is required for successful accomplishment of tasks, especially for complex and volatile tasks. In CSCW environments, groupware is often employed to support collaboration, coordination, and communication among groups of people. This work concentrates on providing task-relevant knowledge without exploring CSCW issues. A future work will integrate the approach proposed in this paper with CSCW technology to provide more effective support for collaboration among knowledge workers. Moreover, as some tasks may involve different organizations, inter-organizational collaboration between knowledge workers is required. Thus, the reuse and exchange of task-relevant knowledge across organizations is another area worthy of investigation.

## Acknowledgement

This research was supported by the National Science Council of Taiwan (Republic of China) under the Grant NSC 93-2416-H-009-011.

## Appendix A. Fuzzy numbers

The fuzzy linguistic approach models the meaning of each term using fuzzy numbers, which play a fundamental role in formulating the semantic meaning of linguistic terms, because they represent approximate values of the linguistic variable. A fuzzy number is defined as follows [10]. A fuzzy number $\tilde { Z }$ is a fuzzy set defined on a real set R. Fuzzy numbers can be used to represent the characteristic functions of linguistic terms. A characteristic function denotes a membership function that maps each element to a membership grade between 0 and 1. Triangular fuzzy numbers are widely used characteristic functions because of their simplicity and solid theoretical basis [28]. The membership function of a triangular fuzzy number $\tilde { Z } = ( l , m , r ) , f _ { \tilde { Z } } ( \tilde { x } ) : \mathbb { R } \longrightarrow [ 0 , 1 ]$ is defined as follows:.

$$
f _ {\tilde {Z}} (x) = \left\{ \begin{array}{l l} (x - l) / (m - l) & l \leq x \leq m \\ (r - x) / (r - m) & m \leq x \leq r \\ 0 & \text { otherwise } \end{array} \right.\tag{14}
$$

To achieve a computational advantage, the crisp ratings (Best Non-fuzzy Performance (BNP) values) are extracted from fuzzy numbers. Various methods can be used to defuzzify fuzzy numbers [21]. This work adopts the center of area (COA) method, because of its simplicity and practicability. The COA method calculates the fuzzy mean under the uniform probability distribution assumption [24]. If the fuzzy number $\tilde { U }$ is triangular, where $\tilde { U } { = } ( l , m , \bar { r } )$ , the crisp rating can be derived by the following equation: $\mathrm { C V } ( \tilde { U } ) { = } [ ( r { - } l ) { + } ( m { - } l ) ] / 3 { + } l .$

Appendix B. Relevance assessment by linguistic ratings  
![](/api/attachments/UXUZ667S/fulltext/images/b8fdf5c8c3401770cecd7aececa213bd16a7c3c70536f73efeb79ad0f7eca5ff.jpg)

## References

[1] A. Abecker, A. Bernardi, K. Hinkelmann, O. Kühn, M. Sintek, Context-aware, proactive delivery of task-specific knowledge: The KnowMore project, International Journal on Information Systems Frontiers (ISF) 2 (3/4) (2000) 139–162.

[2] A. Abecker, A. Bernardi, H. Maus, M. Sintek, C. Wenzel, Information supply for business processes: coupling workflow with document analysis and information retrieval, Knowledge Based Systems 13 (5) (2000) 271–284.

[3] H.J. Ahn, H.J. Lee, K. Cho, S.J. Park, Utilizing knowledge context in virtual collaborative work, Decision Support Systems 39 (2005) 563–582.

[4] R. Baeza-Yates, B. Ribeiro-Neto, Modern Information Retrieval, Addison-Wesley, 1999.

[5] N. Bolloju, M. Khalifa, E. Turban, Integrating knowledge management into enterprise environments for the next generation decision support, Decision Support Systems 33 (22) (June 2002) 163–176.

[6] A. Celentano, M.G. Fugini, S. Pozzi, Knowledge-based document retrieval in office environment: The Kabiria system, ACM Transactions on Information Systems 13 (3) (1995) 237–268.

[7] H. Chen, H. Fan, M. Chau, D. Zeng, MetaSpider: meta-searching and categorization on the web, Journal of the American Society for Information Science 52 (13) (2001) 1134–1147.

[8] T.H. Davenport, L. Prusak, Working Knowledge: How Organizations Manages What They Know, Harvard Business School Press, Boston MA, 1998.

[9] P. De Bra, G.J. Houben, F. Dignum, Task-based information filtering: providing information that is right for the job, Proceed ings of Conferentie Informatie Wetenschappen, Eindhoven, 1997.

[10] D. Dubis, H. Prade, Operations on fuzzy numbers, International Journal of Systems Science 9 (3) (1978) 613–626.

[11] Kurt D. Fenstermacher, Process-aware knowledge retrieval, Proceedings of the 35th Hawaii International Conference on System Sciences, Big Island, Hawaii, USA, 2002, pp. 209–217.

[12] Kurt D. Fenstermacher, C. Marlow, Supporting consultants with task-specific information retrieval, Proceedings of The American Association of Artificial Intelligence, AAAI Press, Orlando Florida, 1999

[13] G. Fischer, J. Ostwald, Knowledge management: problems, promises, realities, and challenges, IEEE Intelligent Systems 16 (1) (2001) 60–73.

[14] Gartner Group, Knowledge management report, Summer 1999.

[15] P.H. Gray, Problem-solving perspective on knowledge management practices, Decision Support Systems 31 (1) (May 2001) 87–102.

[16] P.H. Gray, The impact of knowledge repositories on power and control in the workplace, Information Technology & People 14 (4) (2001) 368–384.

[17] J. Hahn, M. Subramani, A framework of knowledge management systems: issues and challenges for theory and practice, Proceedings of the 21st International Conference on Information Systems, Brisbane, Australia, 2000, pp. 302–312.

[18] P. Hansen, K. Jarvelin, Collaborative information retrieval in an information-intensive domain, Information Processing & Management 41 (2005) 1101–1119.

[19] H. Holz, H. Maus, A. Bernardi, O. Rostanin, A lightweight approach for proactive, task-specific information delivery, Proceedings of the 5th International Conference on Knowledge Management, (I-Know), Graz, Austria, 2005.

[20] E. Ide, New experiments in relevance feedback, in: G. Salton (Ed.), The SMART Retrieval System: Experiments in Automatic

Document Processing, Prentice Hall, Englewood Cliffs, NJ, 1971, pp. 337–354.

[21] J.S. Jang (Roger), C.T. Sun, E. Mizutani, Neuro-Fuzzy and Soft Computing: A Computational Approach to Learning and Machine Intelligence, Prentice-Hall, Upper Saddle River, NJ, 1997.

[22] A. Kankanhalli, F. Tanudidjaja, J. Sutanto, C.Y. Tan (Bernard), The role of IT in successful knowledge management initiatives, Communications of the ACM 46 (9) (2003) 69–73.

[23] M.M. Kwan, P. Balasubramanian, KnowledgeScope: managing knowledge in context, Decision Support Systems 35 (2003) 467–486.

[24] E.S. Lee, R.L. Li, Comparison of fuzzy number based on the probability measure of fuzzy events, Computer and Mathematics with Applications 15 (1988) 887–896.

[25] D.-R. Liu, I.-C. Wu, K.-S. Yang, Task-based K-support system: disseminating and sharing task-relevant knowledge, Expert Systems with Applications 29 (2) (August 2005) 408–423.

[26] M.L. Markus, Toward a theory of knowledge reuse: types of knowledge reuse situation and factors in reuse success, Journal of Management Information Systems 18 (1) (2001) 57–94.

[27] I. Nonaka, A dynamic theory of organizational knowledge creation, Organization Science 5 (1) (1994) 14–37.

[28] W. Pedrycz, Why triangular membership functions? Fuzzy Sets and Systems 64 (1) (1994) 21–30.

[29] M.F. Porter, An algorithm for suffix stripping, Program 14 (3) (1980) 130–137.

[30] J.J. Rocchio, Relevance feedback in information retrieval, in: G. Salton (Ed.), The SMART Retrieval System: Experiments in Automatic Document Processing, Prentice Hall, Englewood Cliffs, NJ, 1971, pp. 313–323.

[31] G. Salton, C. Buckley, Term weighting approaches in automatic text retrieval, Information Processing & Management 24 (5) (1988) 513–523.

[32] G. Salton, C. Buckley, Improving retrieval performance by relevance feedback, Journal of the American Society for Information Science 41 (4) (1990) 288–297.

[33] G. Salton, M.J. McGill, Introduction to Modern Information Retrieval, McGrawHill Book Co., New York, 1983.

[34] M. Spies, A.J. Clayton, M. Noormohammadian, Knowledge management in a decentralized global financial services provider: a case study with Allianz Group, Knowledge Management Research & Practice 3 (1) (2005) 24–36.

[35] S. Staab, H.P. Schnurr, Smart task support through proactive access to organizational memory, Knowledge-Based Systems 13 (5) (2000) 251–260.

[36] I.H. Witten, A. Moffat, T.C. Bell, Managing Gigabytes: Compressing and Indexing Documents and Images, 2nd edn. Morgan Kaufmann Publishers, Los Alto, USA, 1999.

[37] Y. Ye, G. Fischer, Supporting reuse by delivering task-relevant and personalized information, Proceedings of the 24th International Conference on Software Engineering, Orlando, Florida, May 2002, pp. 513–523.

[38] M.H. Zack, Managing codified knowledge, Sloan Management Review 40 (4) (1999) 45–58.

[39] L.A. Zadeh, The concept of a linguistic variable and its application to approximate reasoning, parts 1, 2, and 3. Information Sciences 8 (2) (1975) 199–249; 8 (3) (1975) 301–357; 9 (1) (1975) 43–80.

[40] J.L. Zhao, H. Bi, H. Chen, D. Zeng, C. Lin, M. Chau, Processdriven collaboration support for intra-agency crime analysis, Decision Support Systems: Special Issue on Intelligence and Security Informatics 41 (3) (2006) 616–633.

Dr. Duen-Ren Liu is currently a professor of the Institute of Information Management at the National Chiao Tung University, Taiwan. He received the BS and MS degrees in Computer Science from the National Taiwan University and the PhD degree in Computer Science from the University of Minnesota. His research interests include information systems, knowledge engineering and management, workflow systems, and recommender systems.

Dr. I-Chin Wu is currently an assistant professor of the Department of Information Management at Fu-Jen Catholic University, Taiwan. She received the BS degree in Computer and Information Science from the Soochow University, Taiwan in 1999, and the PhD degree in Information Management from the National Chiao Tung University in 2006. Her research interests include information systems, text mining, knowledge management, and electronic commerce.
