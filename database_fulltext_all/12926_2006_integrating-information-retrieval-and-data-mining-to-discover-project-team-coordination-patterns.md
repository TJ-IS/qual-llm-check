---
otero_id: 12926
otero_key: "9WACRXFW"
title: "Integrating information retrieval and data mining to discover project team coordination patterns"
authors: "Fu-ren Lin; Kuen-jin Huang; Nian-shing Chen"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2005.04.003"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Integrating information retrieval and data mining to discover project team coordination patterns

Fu-ren Lin <sup>a,\*</sup>, Kuen-jin Huang <sup>b</sup>, Nian-shing Chen <sup>b</sup>

<sup>a</sup>Institute of Technology Management, National Tsing Hua University, 101 Sec. 2 Kuang-fu Rd., Hsinchu 300, Taiwan <sup>b</sup>Department of Information Management, National Sun Yat-sen University, 70 Lien-hai Rd., Kaohsiung, 804, Taiwan

Received 21 June 2004; received in revised form 17 April 2005; accepted 28 April 2005 Available online 6 September 2005

## Abstract

This study integrates information retrieval and data mining techniques to discover project team coordination patterns from project documents written in Chinese. The coordination pattern of a project team describes the project execution process, including task category, execution sequence and duration, as well as the team member cooperation. The integration comprises two phases. The first phase extracts the most relevant keywords describing tasks executed by projects from unstructured or semi-structured documents using the mutual information estimate and the term weighting system. A concept hierarchy tree generated using the hierarchical clustering technique represents multiple levels of task categories. The second phase discovers project team coordination patterns through sequential pattern analysis. The proposed approach obtains encouraging results by mining coordination patterns from information system development projects. In the present era of the knowledge economy, the application of groupware to facilitate team coordination and collaboration streamlines the collection and analysis of project documents throughout the project life cycle. A project manager can visualize the project execution process of a team, and can anticipate the project outcomes based on discovered team coordination patterns. Accordingly, the proposed approach can be adapted to team projects that share certain characteristics with information system development projects. <sup>D</sup> 2005 Elsevier B.V. All rights reserved.

Keywords: Information retrieval; Data mining; Sequential pattern analysis; Coordination pattern

## 1. Introduction

A teamwork approach for executing projects involves various roles and tasks conducted within a period of time. Numerous business practices, for example new product development, information system development, and so on, adopt the teamwork approach. Applying groupware to facilitate team coordination and collaboration streamlines the collection and analysis of project documents throughout the project life cycle. Team coordination patterns can be retrieved from these electronic documents, which may be either semi-structured or unstructured. The coordination pattern of a project team describes the project execution process, including the task category, sequence and duration, and the cooperation degree among team members. For example, consider an information system (IS) development project, which generally includes such tasks as requirement determination, modeling data and processes, database and interface design, implementation, testing, installation, and documentation [11], that has been completed by seven team members (e.g., $A _ { 1 } , ~ A _ { 2 } , ~ . . . , ~ A _ { 7 } )$ in six weeks. During the first two weeks, two system analysts $( \mathrm { e } . \mathrm { g } . , A _ { 1 } , A _ { 2 } )$ worked together to identify customer requirements, and design data flow diagrams (DFD) and entity relation diagrams (ERD). The next two weeks were used for prototyping the system after designing the database and completing the structure charts. The other four members $( \mathrm { e } . \mathrm { g } . , A _ { 2 } , A _ { 3 } , A _ { 4 } , A _ { 5 } )$ took charge of these tasks. During the final two weeks, the finished system was tested, installed, and cut over to users. The main tasks, namely system testing, document editing, and user training, were performed by team members $A _ { 1 } , \ A _ { 6 }$ and $A _ { 7 } .$ . The discovery of coordination patterns may help the project management to assign tasks, allocate resources, and evaluate performance.

Techniques adopted for identifying team coordination patterns require joint efforts from researchers on information retrieval and data mining. Efforts to design methods for retrieving information from unstructured documents were presented in the Text Retrieval Conference (TREC, http://trec.nist.gov/). Data mining involves the exploration and analysis of large quantities of data to discover meaningful patterns and rules using automatic or semiautomatic methods [2]. Knowledge discovery in databases (KDD) is a nontrivial process of identifying valid, novel, potentially useful, and ultimately understandable patterns in data [7]. The KDD process can be divided into five phases: selection, preprocessing, transformation, data mining, and interpretation and evaluation. Common model functions in the current data mining practice include classification, regression, clustering, summarization, dependency modeling, link analysis, and sequential pattern analysis. However, KDD research has focused on structured data; thus existing KDD tools are of limited usefulness in mining knowledge from unstructured or semi-structured documents [8,9].

This work attempts to integrate information retrieval and data mining techniques for generalizing, visualizing, and forecasting project team coordination patterns. The integration of information retrieval and data mining techniques is conducted in two phases. During the first phase, approaches developed in research on information retrieval are employed to label each document with a set of keywords that represent the main concepts extracted from the document. These keywords are converted to a structured format, and represent the tasks, participants, resources, and time involved in the project execution. After obtaining the structured project description, the second phase is conducted, which applies sequential pattern analysis to generalize the coordination patterns, and then displays them in graphic user interfaces. Sequential pattern analysis is a data mining technique that generalizes sequential patterns from transactions occurring in different time periods. A project manager can compare the progress of on-going projects with the generalized coordination patterns to predict the project outcomes. The integration of information retrieval and data mining techniques contributes to the discovery of project team coordination patterns by using sequential pattern analysis. The integration of the aforementioned two techniques for mining knowledge from unstructured or semi-structured documents sheds light on project management.

Research on the PLANMINE system relates closely to the present study [23]. The PLANMINE sequence mining algorithm predicts plan failures based on extracted event patterns. Each plan is labeled as good or bad depending on whether it succeeds or fails to achieve its goals. PLANMINE attempts to find event sequences that can be used to confidently predict plan failure. First, the planner uses simulation to generate a database of good or bad plans. These plans are fed into the mining engine to identify event patterns of bad plans, which are used to fix the plan and prevent failures. The pattern generation and plan modification loop is executed repeatedly until no further improvement is obtained. Second, the high confidence patterns are used to generate a plan monitor that notifies a plan manager before the failure of a new plan. PLANMINE was demonstrated using two planning applications: TRIPS and IMPROVE. TRIPS is a collaborative planning system for designing an evacuation plan by using simulation and data mining for plan analysis. IMPROVE first simulates a plan repeatedly and calls PLANMINE to extract high confidence rules for predicting plan failure. IMPROVE then applies qualitative reasoning and plan adaptation techniques to suggest actions for reducing the likelihood of failure. In summary, PLANMINE generates and simulates candidate plans to discover high frequency patterns among the bad plans. On the contrary, the approach proposed in this paper gathers documents from the project execution, and integrates information retrieval and sequence pattern mining techniques to generate project team coordination patterns.

This study presents the proposed integration approach by discovering the coordination patterns from documents written in Chinese in information system (IS) development projects. The progress reports and meeting minutes from the project execution provide rich sources for a project manager not only to identify project status but also to generalize team coordination patterns to predict project performance. Since project composition generally includes tasks, resources, time schedule, and performance evaluation, the proposed approach can be applied to other business processes with similar settings to identify their coordination patterns, and in turn, to improve their performance. The rest of this paper is organized as follows. Section 2 describes techniques for information retrieval and data mining used in this study. The framework for discovering coordination patterns from project documents then is presented in Section 3. Next, Section 4 demonstrates the effectiveness of the proposed approach in discovering coordination patterns from IS development projects. Finally, Section 5 concludes this research and identifies directions for future research.

## 2. Information retrieval and data mining techniques

Mining coordination patterns from project documents consists of two major phases: information retrieval and data mining. This section introduces methods used for retrieving keywords from documents, comparing keyword similarity, clustering keywords into hierarchical concepts, and mining sequential patterns.

## 2.1. Information retrieval methods

## 2.1.1. Term extraction from documents

In information retrieval, attributes used to identify the documents are often words or terms. Terms extracted from documents are used as content identifiers, so that a document can be represented by a set of terms [20]. Since no explicit separators exist between Chinese characters in a document to indicate the term boundary, the mutual information measure is used to determine the term boundary used to extract terms from a document [4,5,22]. The mutual information $M I \left( x , y \right)$ between characters x and y is defined as $l o g _ { 2 } ( p ( x , y ) /$ $p ( x ) p ( y ) )$ , where p(x) denotes the probability of observing character $x , p ( y )$ represents the probability of observing character y, and $p ( x , y )$ is the probability of observing both characters x and y. Two algorithms are usually used to segment words [22]. One approach is to employ the nature of a priori information to allocate segmented words by iteratively calculating the MI of each bi-gram, tri-gram, and n-gram. Meanwhile, the other approach is to calculate the MI of each bi-gram just once, and to find the proper segment points at the whole sentence according to the MI distribution. The term set is refined by removing word suffixes, high frequency terms, and synonymous terms [19,21].

A set of terms, $t _ { \mathrm { i } 1 } , t _ { \mathrm { i } 2 } , . . . , t _ { \mathrm { i m } } ,$ can be used as content identifiers to represent the main concepts of a document $d _ { \mathrm { i } } ,$ and also to distinguish this document from others. A term-weight $w _ { \mathrm { i j } } ,$ , ranging between 0 and 1, represents the degree of importance of term $t _ { \mathrm { i j } }$ in document $d _ { \mathrm { i } \cdot \mathrm { A } }$ term weight close to one indicates that the term is important to the document. Three typical termweighting components, term frequency, document frequency, and normalization, are used by the termweighting systems [13,14]. A short-term vector represents a short document, whereas a long-term vector represents a long document. When a large number of terms are used for document representation, there is a high chance of matching terms between queries and documents. Thus, long documents are more likely to be retrieved than short ones. However, all relevant documents should be treated as equally important for retrieval purposes. Consequently, a normalization factor is incorporated into the term-weighting formula to equalize the length of the document vectors.

The most effective document term-weighting method for calculating a term weight is to multiply its within-document term frequency (tf) by its inverse document frequency $( i d f )$ , and then normalize the product using the cosine measure [16]. The resulting formula is denoted as $t f ^ { * } i d f / ( \sum _ { i = 1 } ^ { \bar { m } } \left( t f _ { i } ^ { * } i d f _ { i } \right) ^ { 2 } ) ^ { \frac { 1 } { 2 } }$ 4 where a vector of m terms $\langle t _ { \mathrm { i } 1 } , t _ { \mathrm { i } 2 } , . . . , t _ { \mathrm { i m } } \rangle$ is calculated using $t f _ { \mathrm { i } }$ and idf<sub>i</sub> $( 1 \leq i \leq m )$ . Since this is the best fully weighted system, this method is applied to extract key terms for representing documents.

## 2.1.2. Document similarity analysis

A document $d _ { \mathrm { i } }$ in a document set can be represented by a m-dimensional vector $\langle t _ { \mathrm { i 1 } } , t _ { \mathrm { i 2 } } , . . . , t _ { \mathrm { i m } } \rangle$ , where m indicates the number of terms extracted from the document set. Accordingly, document $d _ { \mathrm { i } }$ corresponds to the vector $\left. w _ { \mathrm { i } 1 } \ w _ { \mathrm { i } 2 } , \dots . . . , w _ { \mathrm { i m } } \right.$ , where each $w _ { \mathrm { i j } }$ indicates the weight or existence of term $t _ { \mathrm { i j } }$ in document $d _ { \mathrm { i } \cdot \mathrm { A } }$ set of n documents can be mapped into an $n \times n$ document similarity matrix (or dissimilarity matrix) by a selected mapping process, and each element $s _ { \mathrm { i j } }$ of this matrix indicates the similarity of documents $d _ { \mathrm { i } }$ and $d _ { \mathrm { j } }$ [17].

A similarity measure using cosine measure for two documents, $\mathrm { e . g . , ~ } d _ { \mathrm { j } }$ and $d _ { \mathrm { k } } ,$ is defined as similarity $\begin{array} { r } { \left( d _ { j } , d _ { k } \right) = \sum _ { i = 1 } ^ { m } w _ { j i } w _ { k i } } \end{array}$ , where $w _ { \mathrm { j i } }$ and $w _ { \mathrm { k i } }$ denote the term weights of $\dot { t } _ { \mathrm { j i } }$ and $t _ { \mathrm { k i } } ,$ respectively [3]. The cosine measure calculates the angle between two vectors in an $n \times n$ matrix to quantify the similarity between the two documents $d _ { \mathrm { j } }$ and $d _ { \mathrm { k } }$ . Two popular normalization measures, normalized and Jaccard, are generally used for representing the similarity in the desired range. This study uses the Jaccard similarity to calculate the similarity between two documents. The Jaccard coefficient for calculating the similarity between two documents, $d _ { \mathrm { j } }$ and $d _ { \mathrm { k } } ,$ is defined as

Jaccard similarity $\left( d _ { j } , d _ { k } \right)$

$$
= \frac {\sum_ {i = 1} ^ {m} w _ {j i} w _ {k i}}{\sum_ {i = 1} ^ {m} \left(w _ {j i}\right) ^ {2} + \sum_ {i = 1} ^ {m} \left(w _ {k i}\right) ^ {2} - \sum_ {i = 1} ^ {m} w _ {j i} w _ {k i}}
$$

([10]. p. 20).

## 2.1.3. Clustering methods

Terms extracted from documents to indicate tasks executed in projects can be used to categorize tasks by clustering techniques [6]. Two typical techniques are commonly used for document clustering: partitioning and hierarchical methods [12,15]. A partitioning method constructs k clusters by dividing the data into k groups. Meanwhile, common partitioning algorithms include k-means, PAM, CLARA, and FANNY.

The hierarchical method transforms a proximity matrix into a sequence of nested partitions, which can be categorized into agglomerative and divisive algorithms. An agglomerative algorithm begins with the disjoint n clusters, and each cluster contains a single document, assuming that the document set contains n documents. The agglomerative clustering algorithm determines how to hierarchically merge two or more of these trivial clusters until a single cluster contains all n documents. The agglomerative algorithms include AGNES, Ward’s method, and the weighted average linkage. The linkage methods can be further divided into three methods: single linkage, complete linkage, and average linkage. Additionally, the divisive algorithm hierarchically divides documents into clusters with the reverse order from the agglomerative ones. Two algorithms that belong to the divisive algorithm category are DIANA and MONA.

No preliminary knowledge of the optimal cluster number excludes the use of partitioning methods. Among hierarchical methods, this study applies the average linkage algorithm in the agglomerative approach by virtue of the bottom-up nature of grouping documents to a hierarchical tree. The average linkage treats the distance between two clusters as the average distance between all item pairs. The steps of the agglomerative hierarchical clustering algorithm for grouping n objects (items or variables) are listed below.

1. Begin with n clusters located in an $n \times n$ symmetric matrix of distances, $\mathbf { D } { = } \{ d _ { \mathrm { i k } } \}$ , where $d _ { \mathrm { i k } }$ denotes the distance between objects i and k. Notably, each cluster contains a single object at this stage.

2. Search the distance matrix to identify the nearest pair of clusters. $d _ { \mathrm { u v } }$ denotes the distance between the most similar clusters $C _ { \mathrm { u } }$ and $C _ { \mathrm { v } }$

3. Merge clusters $C _ { \mathrm { u } }$ and $C _ { \mathrm { v } }$ Label the newly formed cluster as $C _ { \mathrm { u v } } .$ Update the entries in the distance matrix by deleting the rows and columns corresponding to clusters $C _ { \mathrm { u v } } ,$ and then add a row and a column containing the distances between the new cluster $C _ { \mathrm { u v } }$ and the remaining clusters.

4. Repeat Step 2 and 3 a total of $n - 1$ times. Record the identity of merged clusters and the levels at which the mergers take place.

In Step 3 of the general agglomerative algorithm, the distances between $C _ { \mathrm { u v } }$ and any other cluster $C _ { \mathrm { w } }$ are determined by $d _ { u \nu , w } = \frac { \sum \sum d _ { i k } } { N _ { u \nu N _ { w } } } ,$ <sub>,</sub> where $d _ { \mathrm { i k } }$ denotes the distance between object i in cluster $C _ { \mathrm { u v } }$ and object k in cluster $C _ { \mathrm { w } }$ and $N _ { \mathrm { u v } }$ and $N _ { \mathrm { w } }$ represent the number of items in $C _ { \mathrm { u v } }$ and $C _ { \mathrm { w } }$ respectively.

## 2.2. Sequential pattern analysis

A sequence is an ordered list of itemsets, where an itemset is a non-empty set of items. An itemset i is denoted as $( i _ { 1 } , i _ { 2 } , \ldots , i _ { \mathrm { m } } )$ , where $i _ { \mathrm { j } }$ represents an item $j ,$ and a sequence S is $\left. s _ { 1 } , s _ { 2 } , \ldots , \ s _ { \mathrm { n } } \right.$ , where $s _ { \mathrm { k } }$ denotes an itemset k. Individual items can occur only once in an itemset, but can occur multiple times in different itemsets in a sequence. An itemset is denoted by the transaction time, and transaction times differ for any two itemsets in a sequence. Generally, algorithms for mining sequential patterns do not consider the frequency with which items occur in a transaction.

The objective of sequential pattern analysis is to identify all sequential patterns using a user-specified minimum support, where the support of a sequential pattern is the occurrence frequency of a sequence of itemsets containing that pattern. A sequence of itemsets with a rate of occurrence that equals or exceeds the minimum support is called a large sequence. AprioriAll, AprioriSome and DynamicSome are common algorithms used to discover the generalized sequential pattern [1]. The Generalized Sequential Pattern (GSP) algorithm derived from the ApriorAll algorithm discovers the generalized sequential patterns [18].

## 3. Framework for mining team coordination patterns

The discovery of the project team coordination patterns can be viewed from two perspectives. One perspective is to summarize the coordination pattern of an individual project team. The other is to compare team coordination patterns in terms of task category, participant, and time duration. The discovery of project teams’ coordination patterns resembles the sequential pattern analysis, as project tasks can be viewed as transaction items. However, the discovery of a coordination pattern attributed by task category, involved agent, and time duration may require different representations from the sequential pattern analysis. One more effort in this study is to convert semistructured text into structured data for mining project team coordination patterns. This section describes the framework of mining coordination patterns in two phases.

## 3.1. Process of keyword extraction and task categorization

The main task in the information retrieval phase is to transfer text documents into structured data used for discovering coordination patterns. A project consists of a set of tasks, and each task can be described based on its objective, work scope, major and supporting agents, duration, and required resources. The task objective is used as the criteria for assessing project task similarity. Similar tasks are assigned to the same category. A concept hierarchy tree organizes tasks hierarchically, with non-leaf nodes representing task categories and leaf nodes representing tasks. A project manager can view project tasks on different levels of abstraction using the concept hierarchy tree.

Fig. 1 illustrates the framework for keyword extraction and task categorization. The concept hierarchy tree is generated through a series of stages, for example, keyword extraction, similar task analysis, and task clustering. Different tasks can be distinguished using keywords identified from documents. For simplicity, the syntax and semantics of the document are ignored. Keyword extraction and task categorization involve statistical term extraction, stop word elimination, morphological analysis, termweight assignment, vector space model, and average linkage, while the statistical approach extracts keywords and the remaining techniques refine these extracted keywords.

![](/api/attachments/9WACRXFW/fulltext/images/5893bb1a549c66f2cd0b41e0b524ba422231a662e448bbbb2371dbab0a8106ee.jpg)  
Fig. 1. Framework of keyword extraction and task categorization.

The statistical term extraction approach is executed via the following procedure [22]:

1. Calculate the occurrence frequency for all Chinese characters in the document set.

2. Calculate the occurrence frequency for all Chinese bi-grams in the document set.

3. Compute the mutual information for all Chinese bi-grams.

4. Segment the text into words according to the threshold value given by the user, and generally, the number of bi-grams decreases with increasing threshold value.

5. Repeat Steps 3 and 4 until there are no more bigrams with positive mutual information value.

The statistical approach is used to extract keywords to create the primitive keyword set K from documents. That is, $K = \{ k _ { 1 } , k _ { 2 } , . . . , k _ { \mathrm { n } } \} , i \neq j \Rightarrow k _ { \mathrm { i } } \neq k _ { \mathrm { j } }$ . Keywords are extracted from a document D to describe the task features denoted as ${ \pmb D } _ { \mathrm { m } } { = } \{ k _ { 1 } , ~ k _ { 2 } , ~ . . . , ~ k _ { \mathrm { n } } \}$ where $\pmb { { \cal D } } _ { \mathrm { m } } \subseteq \pmb { { \cal K } }$ and 0 Vm V#(documents). English and Chinese document texts are processed separately. In extracting Chinese keywords, a consecutive sequence of Chinese characters is considered as a phrase, while non-Chinese characters in the text are ignored. In extracting English keywords, a consecutive sequence of English words is considered to be a phrase. For instance, the sentence <sup>b</sup> DFD context<sup>Q</sup> in a document comprises the bi-gram (draw), and the occurrence frequency of each character is f( )=41, f( )=75, and f( )=25. The document set includes 44178 characters. The mutual information value for the bi-gram is calculated by [(25/44178) /(41/44178) (75/44178)]=8.489. Moreover, the mutual information value exceeds the threshold value 3, and thus the bi-gram is counted as a keyword. A total of four primitive keywords, <sup>b</sup> <sup>Q</sup>, <sup>b</sup>DFD<sup>Q</sup>, <sup>b</sup> <sup>Q</sup>, and <sup>b</sup>context<sup>Q</sup>, are obtained for representing the document.

The primitive keyword set includes many problems. First, non-significant words consume additional computational resources in the process. Second, synonymy affects the accuracy of the task clustering. This study uses the stop word and synonymy dictionaries to obtain representative keywords for documents.

In eliminating stop words, this study removes Chinese words which are adjectives, adverbs, and pronouns from the extracted terms. For example, words such as (of), (it), (and), (and), (has), (again), and (will) frequently appear in Chinese documents, but convey little task related information. The morphological analysis deals with the synonymy existing in the extracted keywords. From the synonym dictionary, the synonymous keywords are eliminated from the primitive keyword set in the morphological analysis process. For instance, terms synonymous with (writing) are (editing) or (scribing). In this case, (writing) substituted for (editing) and (scribing).

Based on the vector space model theory, each document is represented by the most relevant keywords extracted from the above process to represent tasks. In this study, each document describes an individual task, so that keywords extracted from the document represent task related concepts. Consequently, a task–keyword matrix can be used to denote keywords for each task. Based on the task–keyword matrix and vector space model, the similarity index between two tasks is calculated by Jaccard coefficient. The task–task similarity matrix is thus obtained. The similarity index approaches one if two tasks are similar, and approaches zero if they are different. The diagonal index is one since a task is identical to itself.

After obtaining the mutual similarity index among tasks, this study generates the concept hierarchy tree using the average linkage method. Fig. 2 shows an example of a concept hierarchy tree, in which a leaf node denoted by a rectangle represents a task, and a non-leaf node labeled by a circle represents a category generalized from similar tasks using the average linkage method. The concept hierarchy tree is very useful for viewing the granularity of a task from bottom to top. For example, $T _ { 1 }$ and $T _ { 4 }$ are clustered to category B, while categories A and $T _ { 2 }$ are clustered to category C, and categories B and C are clustered to category D.

![](/api/attachments/9WACRXFW/fulltext/images/055c8ecf13c9dfa0281024cd2ce5cc4babf6c268448bba8e176ff713d2fe5dd8.jpg)  
Fig. 2. Concept hierarchy tree.

![](/api/attachments/9WACRXFW/fulltext/images/63a7335938c144b7095e77dacd0990d56434ad56010e86cf52b407e08ffc7d78.jpg)  
Fig. 3. Process of mining project coordination pattern.

## 3.2. Process of mining coordination patterns

The process of mining coordination patterns resembles the Apriori family of sequence mining algorithms. However, owing to possible time overlapping among project tasks and the use of additional attributes for task description, for example the participants, duration, and resources, this study uses the unit time window and attribute encoding method to represent the time sequence, task categories, and cooperation degree for the coordination pattern. The unit time window is defined as the smallest time period in which tasks executed within the time period are viewed as occurring simultaneously. The attribute encoding method transforms the time sequence, task category and cooperation degree into a string of symbols to denote items for mining sequential patterns. Following the transformation, the sequence mining algorithms, such as AprioriAll, ApprioriSome, and so on, can be employed to discover the project team coordination patterns. To analyze the coordination pattern of an individual project, this study visualizes the project execution process in graphical user interfaces. The discovered coordination patterns can also be used for predicting on-going project outcomes by matching the most similar pattern from the pattern base.

Fig. 3 illustrates the process of visually summarizing individual project execution, and mining coordination patterns to predict new project outcomes. First, the string matching approach is applied to convert unstructured documents into structured task descriptions using the extracted keywords. The structured description is formed as a data schema comprising task identification, starting time, ending time, number of agents, involved agents, and the referred document. The detailed description can be seen in an example shown in the following section. Second, the project can be summarized in graphic user interface based on the data schema and the concept hierarchy tree. Third, the task category, cooperation degree, and time window are encoded to represent project tasks. Sequential pattern analysis subsequently is applied to discover the coordination pattern. The coordination patterns then are stored in the coordination pattern base. Fourth, similarity analysis can be used to seek the most similar pattern from the pattern base based on the new project features. Fifth, the matched coordination pattern is used to forecast the possible outcomes of the on-going project.

Set of task descriptions retrieved from the documents shared by the second team

<table><tr><td>Start time</td><td>End time</td><td>Total time</td><td> $Task^a$ </td><td># of agents</td><td> $A1^b$ </td><td>A2</td><td>A3</td><td>A4</td><td>A5</td><td>A6</td><td>File name</td></tr><tr><td>10/20/98</td><td>10/23/98</td><td>4</td><td>0</td><td>6</td><td>2</td><td>2</td><td>2</td><td>1</td><td>2</td><td>2</td><td>P285420291.txt</td></tr><tr><td>10/26/98</td><td>10/30/98</td><td>5</td><td>1</td><td>6</td><td>2</td><td>2</td><td>2</td><td>1</td><td>2</td><td>2</td><td>P285420292.txt</td></tr><tr><td>11/2/98</td><td>11/6/98</td><td>5</td><td>2</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>P285420293.txt</td></tr><tr><td>1/4/99</td><td>1/5/99</td><td>2</td><td>38</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>P2854203811.txt</td></tr><tr><td>1/4/99</td><td>1/5/99</td><td>2</td><td>39</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>P2854203911.txt</td></tr></table>

<sup>a</sup> Values in task column denote the task identification.  
<sup>b</sup> A<sub>i</sub> denotes the agent i in the team. The value 0, 1, and 2 indicate that agent A<sub>i</sub> is absent from the task, a major participant, and a supporting force respectively.

## 4. An example: mining coordination patterns of information system development project teams

This section uses the documents gathered from information system (IS) development projects to illustrate the process of mining project team coordination patterns. Undergraduate students, enrolled in an information system analysis and design course in a university in Taiwan, were grouped into eight project teams, and asked to perform IS development projects. Each team contained six students. Each team member completed a weekly progress report, while each team submitted weekly meeting minutes electronically.

Each project progress report, describing one task, contains items such as main task participants, task description, starting time, ending time, and supporting forces. Tasks involved in IS development can be reviewed as activities performed by different project members (called agents) across a sequence of stages with different time durations. This study uses agent, task description, and duration (starting time, ending time, total time) for task description.

## 4.1. Generation of the concept hierarchy tree and the structured task description

Keywords for describing a task are obtained from the information retrieval phase. The time required to complete a task is defined as the time duration between task initiation and completion. This study identifies agents and calculates the number of agents from the document paragraph describing major participants and supporting forces. Table 1 lists the structured task retrieved from the documents submitted by the second team.

Fig. 4 illustrates a portion of the concept hierarchy tree derived from the documents submitted by the second team. The number followed by $\mathbf { \tilde { C } } \mathbf { \Psi }$ denotes the category identification. For example, the concept hierarchy tree in Fig. 4 can be used to identify that: (1) task category 5005C denotes interface design tasks, which takes 7.5% of the project time, (2) task category 5012C denotes the task of designing and modifying DFD, which takes 15% of the project time, (3) task category 5018C denotes the tasks of designing and modifying ERD, which take 18.3% of the project time, (4) task category 5026C denotes the tasks of interviewing, project scheduling and discussion, which take 20.4% of the project time, and (5) task category 5035C denotes the implementation tasks, which take 26.88 % of the project time. The concept hierarchy tree represents six project team task categories.

![](/api/attachments/9WACRXFW/fulltext/images/fb9e1befd6648f3e5b26f4608c69c336df9f17d85fcba1697181f7964dc999b5.jpg)  
Fig. 4. A portion of a concept hierarchy tree for the second team.

## 4.2. Visualization of individual project team coordination patterns

According to the structured task description and the concept hierarchy tree, this study summarizes tasks executed by project teams using graphical user interfaces. This visualization can be viewed from two perspectives. The project execution process can be understood from the team perspective by browsing the task category, involved agents, time duration, degree of cooperation, and detailed task information. By viewing from the agent perspective, this study can identify how agents acted in project execution in terms of task categories they performed as primary or supporting roles, and the cooperation durations.

A project manager can probe the coordination pattern of a project from either the team or the agent perspective. Fig. 5 shows the coordination pattern of the second team from the team perspective. The y-axis denotes the task category and the x-axis represents the task execution duration. The information in task 1 belonging to task category identification 5000 is extracted from the document file P285420292.txt. Six agents, A1, A2, A3, A4, A5, and A6, were involved in the task.

Fig. 6 illustrates the roles of Agent 2 that were performed in the second team. For example, Agent 2 is a major participant in Task 2, and also plays a supporting role in Task 3. This study also identifies that Agent 2 performed most of the tasks in task category 5015 since most of the tasks performed by Agent 2 appear in category 5015.

The visualization reveals the degree of the team coordination on the upper left corner of the screen shown in Fig. 6. Based on the number of agents participating in each task, the cooperation degree is divided into low (below 33.3% of the team members), medium (33.3% to 66.6%), and high levels (above 66.6%). The proportion of project tasks executed by

![](/api/attachments/9WACRXFW/fulltext/images/c55066bc085323bac46686370bab45df4574730dafc5deb3b1999fb01c14da9b.jpg)  
Note.合作程度: cooperation degree;低: low;中:medium;高: high;組内分析圖: analysis chart人數: team size;總共工作人數: total workingforce;文件檔名:document file name;工作類別: taskcategory;参與工作者: participant  
Fig. 5. Coordination pattern of the second team.

[5090] [5090] [5084] [5084] [5084] [5084]

![](/api/attachments/9WACRXFW/fulltext/images/3ee9a9b3a9c77ac82c443ff2f2e5f7fce254fa01ba30725d5ec33464afd66e64.jpg)  
Note.合作程度: cooperation degree;低: low;中:medium;高: high;組内分析圖: analysis chart;人數: team size;總共工作人數: total working force;文件檔名: document file name;工作類別: taskcategory;参與工作者: participant.  
Fig. 6. Roles performed by agent 2 (major or supporting) in the second team.

low cooperation degree is determined by dividing the total project time by the time spent by low cooperation degree on task completion. The percentages of medium and high degrees of cooperation are calculated similarly. For example, in the second team, 59.13% of tasks are performed by low cooperation degree, 22.58% by medium, and 18.27% by high as shown in Fig. 6.

## 4.3. Generalization of the project team coordination pattern

Tasks are aligned by the task starting time to represent their time sequence. Meanwhile, the unit time window is set to one week. A task executed across more than one week is divided into different tasks with different task identifications, which are represented as items in sequential pattern analysis. Consequently, the problem can be reduced to that of the sequential pattern analysis. This study uses the sequential pattern analysis function provided by the IBM Intelligent Miner, a data mining tool, to discover the coordination pattern based on these six project teams. In mining coordination patterns, Table 2 shows the frequent task sequence in task category with a support rate of 50%.

Second, this study uses the sequence of task categories and the degree of cooperation to represent a coordination pattern, with the results listed in Table 3. Low degree of cooperation is encoded as 5, medium as 6, and high as 7. For instance, in Task 7104 in Table 3, the first digit, 7, denotes that task identification 104 is performed with a high degree of cooperation. Accordingly, over 66.6% of team members participate in designing and analyzing ERDs. Different similarity threshold values can be set in the

[5018] [5018] [5018] [5018] [5067] [5067] [5067]

[5018] [5084] [5084] [5084] [5084]

[5018] [5018] [5018] [5018] [5099]

[5090] [5090] [5090] [5090] [5090] [5018] [5084] [5084] [5084] [5084]

[5090] [5090] [5090] [5090] [5090] [5062] [5018] [5084] [5084]

5018: design ERD. 5062: create data table. 5067: design Web pages.

5084: programming. 5099: build database server. 5090: project schedule.

Coordination pattern for considering task category and cooperation degree

<table><tr><td>Threshold</td><td>Support</td><td>Coordination pattern</td></tr><tr><td>0.1</td><td>33.33%</td><td>[7072] [7072] [7072] [5072] [5072] [5072]</td></tr><tr><td>0.2</td><td>50%</td><td>[7076] [7076] [7076] [7076] [5076]</td></tr><tr><td>0.3</td><td>66.67%</td><td>[7104] [7104] [7104] [5104] [5104] [7104]</td></tr><tr><td>0.4</td><td>50%</td><td>[7087] [6087]</td></tr><tr><td></td><td>50%</td><td>[7087] [7087] [7087] [7087] [5087] [5087]</td></tr></table>

072:design and alter DFD. 076:plan, control and schedule projects. 104:design and analyze ERD 087:design and code Web pages.

concept hierarchy tree to view tasks in different category levels. Moreover, in a similarity threshold, different support rates can be set to obtain different sequences of task categories with different degrees of cooperation.

Third, this study represents the coordination pattern using task category, cooperation degree, and time duration. Fig. 7 illustrates an example of the resulting coordination pattern, where tasks are performed in a sequence of [02724], [03728], [04721], [04708], [05721], [09721], [09707], [10720], [10707], [12707], [13712], [13700], and [18724]. Each task is encoded in five digits, TTHCC, where TT denotes the time window, H the degree of cooperation, and CC the task category. For example, in Task 03711, <sup>d</sup>03<sup>T</sup> denotes the third unit time window (i.e., week three in this case), <sup>d</sup>7<sup>T</sup> denotes high degree of cooperation, and <sup>d</sup>11<sup>T</sup> denotes the task category number. Therefore, Task 03711 denotes a task belonging to category 11 with high degree of cooperation, and is performed during the third week.

![](/api/attachments/9WACRXFW/fulltext/images/47b63b84cede361bf46577435364f4008cd248b71e4a56872444df980e3f624f.jpg)  
Fig. 8. Framework of predicting project outcomes.

## 4.4. Prediction of project team coordination pattern

To demonstrate how to adopt the coordination pattern to predict new project outcomes, this study synthesized experimental data based on the prediction framework in Fig. 8. Types G and B were used to represent good and bad project outcomes, respectively in the experiment. Teams in Type G were assumed to perform better than those in Type B. First, in predicting project outcome, tasks, agents, and time durations were generated for ten Type G teams and ten Type B teams using the synthetic data generator according to the task category sequence. Task categories were enumerated based on task category identification 00, 01, . . ., 29. The task categories of a Type G team during the first week were chosen randomly from categories 00, 01, . . ., 04, those in the second week were chosen from categories 05, 06, . . ., 09, and so on. Moreover, the task categories of a Type B team in each week were randomly assigned from 00 to 29. Each team had ten participants, and produced 150 documents in 120 workdays. Each task could not exceed five days. The time window size was set to seven days, so that the time sequence number started from 01 to 18; that is, there were a total of 18 time intervals.

![](/api/attachments/9WACRXFW/fulltext/images/f1b971a9613c685c142cbb943c8ecfc821aaaa931031525234b3114942bac347.jpg)  
Fig. 7. Coordination pattern denoted by task category, cooperation degree, and time window.

Second, this study used the sequential pattern analysis function in the IBM intelligent Miner to obtain the coordination patterns for Type G and B teams, respectively. The support rates of Type G teams were 60%, 70%, 80%, 90%, and 100%. Additionally, the support rates of Type B teams were 30%, 40%, and 50%. Third, distinct sequences were obtained by deleting duplicated sequences and those sequences that were subsets of other sequences. The obtained distinct sequences are also called maximal coordination patterns. Therefore, a maximal coordination pattern is a large sequence that does not contain any other large sequences. Finally, whether a team belongs to a Type G or B team can be predicted based on the coordination patterns of Type G and B teams.

The similarity index of one query pattern ( P) with coordination patterns (PTRN) in a pattern base is defined as sim $\begin{array} { r } { ( P , P T R N ) = \sum _ { i = 1 } ^ { n } { w _ { i } \cdot r _ { i } } / \sum _ { i = 1 } ^ { n } { w _ { i } } } \end{array}$ where $r _ { \mathrm { i } }$ denotes the similarity value by dividing the number of the matching items between P and $P T R N _ { \mathrm { i } }$ by the number of items in PTRN<sub>i</sub>, and w<sub>i</sub> represents the weight value by dividing the number of items in PTRN by the maximum number of items in PTRN. The denominator component suggests that a normalization factor should be incorporated into the similarity index formula.

The similarity index can be used as a basis for labeling a team as either a Type G or Type B team. To evaluate the prediction accuracy, this study randomly selected five teams from Type G and B teams, and then predicted their types. Table 4 lists the prediction results, and only the second testing team was incorrectly predicted. The similarity index ranges from zero to one. Furthermore, if the testing team pattern more closely resembles Type G team pattern, the similarity value is significantly closer to one. For instance, the similarity index between the first team and Type G team patterns is 0.184, and that with Type B is 0.090, as listed in Table 4. Since 0.184 is larger than 0.090, this team is labeled as a

Table 4  
Prediction accuracy based on coordination patterns

<table><tr><td></td><td>1st testing team</td><td>2nd testing team</td><td>3rd testing team</td><td>4th testing team</td><td>5th testing team</td></tr><tr><td>Similarity with Type G team patterns</td><td>0.184</td><td>0.151</td><td>0.196</td><td>0.197</td><td>0.00</td></tr><tr><td>Similarity with Type B team patterns</td><td>0.090</td><td>0.118</td><td>0.100</td><td>0.017</td><td>0.09</td></tr><tr><td>Correct type</td><td>Type G</td><td>Type B</td><td>Type G</td><td>Type G</td><td>Type B</td></tr><tr><td>Predicted type</td><td>Type G</td><td>Type G</td><td>Type G</td><td>Type G</td><td>Type B</td></tr></table>

Type G team. A project manager can gather documents generated from team projects to discover their coordination patterns. The project manager can also predict the outcomes of on-going projects by referring to these coordination patterns. Furthermore, project managers can prevent possible project failure through task-resource alignment after foreseeing its possible outcomes.

## 5. Conclusions and future research

This study demonstrates the integration of information retrieval and data mining techniques for discovering project team coordination patterns. Information retrieval techniques, such as keyword extraction, task similarity analysis, and concept hierarchy tree generation, are used to transform unstructured or semi-structured project documents into structured data schema attributed by task category, sequence, duration, and participants. Project coordination patterns represented by the structured data schema are discovered using the sequential pattern analysis method.

A project manager can use the discovered patterns to visualize the task execution sequence, duration, and cooperation degree of a project team. A project manager can also forecast the outcomes of an ongoing project by matching the project with existing patterns. An example application on discovering coordination patterns from information system development projects was used to illustrate the proposed methods. This study sheds lights on the performance improvement of information system development projects by learning from past project execution experiences. Other team projects with similar settings can adopt the proposed approach to enhance project management.

This study has some limitations. First, this study may not accurately capture concepts from documents when ignoring syntax and semantics in extracting terms from documents. Second, a task that spans consecutive time windows was encoded as different tasks owing to the limitations of the sequential pattern analysis method that only deals with discrete events. Third, setting a unit time as a window size depends heavily on the task characteristics, and limits pattern transfer to other tasks which have different time spans.

Future research can apply the proposed approach to enterprise information system development projects, where uneven project scope, duration, and interaction may create the need for new structured data encoding methods or the extension of sequence pattern analysis methods. Second, the key term extraction during the information retrieval stage can be improved by developing information retrieval methods, for example semantic key terms extraction, ontology-based extraction, and so on. Third, the proposed approach can be applied to team projects other than information system development to eval uate its general applicability.

## References

[1] R. Agrawal, S. Srikant, Mining sequential patterns, Proceedings of the International Conference on Data Engineering (ICDE), IEEE Computer Society Press, Taipei, Taiwan, 1995 (March).

[2] M.J. Berry, G. Linoff, Data Mining Techniques: for Marketing, Sales, and Customer Support, John Wiley and Sons Inc., New York, 1997.

[3] T. Biru, A. EL-Hamdouchi, R.S. Rees, P. Willett, Inclusion of relevance information in the term discrimination model, Journal of Documentation 45 (2) (1989) 85 – 100.

[4] A. Chen, J. He, L. Xu, Chinese text retrieval without using a dictionary, Proceedings of ACM-SIGIR Conference on Research and Development in Information Retrieval, 1997, pp. 42– 49.

[5] K.W. Church, P. Hanks, Word association norms mutual information, and lexicography, Computational Linguistics 16 (1) (1990) 22–29.

[6] R.C. Douglass, R.K. David, O.P. Jan, W.T. John, Scatter/ gather: a cluster-based approach to browsing large document collections, ACM 15th ANN Int’l SIGIR ’92, ACM Press, Denmark, 1992 (June), pp. 318– 329.

[7] U.F. Fayyad, G. Piatetsky-Shapiro, S. Smyth, The KDD process for extracting useful knowledge from volumes of data, Communications of the ACM 39 (11) (1996) 27– 34.

[8] R. Feldman, H. Hirsh, Exploiting background information in knowledge discovery from text, Journal of Intelligent Information Systems 9 (1) (1997) 83 – 97.

[9] R. Feldman, H. Hirsh, Mining text using keyword distributions, Journal of Intelligent Information Systems 10 (3) (1998) 281–300.

[10] D.A. Grossman, O. Frieder, Information Retrieval: Algorithms and Heuristics, Kluwer Academic Publishers, Boston, 1998.

[11] J.A. Hoffer, J.F. George, J.S. Valacich, Modern Systems Analysis and Design, The Benjamin/Cummings Publishing Company Inc., Menlo Park, CA, 1996.

[12] A.K. Jain, R.C. Dubes, Algorithms for Clustering Data, Prentice Hall, Englewood Cliffs, New Jersey, 1988.

[13] K.S. Jones, A statistical interpretation of term specificity and its application in retrieval, Journal of Documentation 28 (1) (1972) 11 –21.

[14] H.K. Kang, K.S. Choi, Two-level document ranking using mutual information in natural language information retrieval, Information Processing & Management 33 (3) (1997) 289 – 306.

[15] L. Kaufman, P.J. Rousseeuw, Finding Groups in Data: an Introduction to Cluster Analysis, John Wiley and Sons Inc., 1990.

[16] G. Salton, C. Buckley, Term-weighting approaches in automatic text retrieval, Information Processing & Management 24 (5) (1998) 513 – 523.

[17] G. Salton, A. Wang, Generation and search of clustered files, ACM Transactions on Database Systems 3 (4) (1978) 321 – 346.

[18] S. Srikant, R. Agrawal, Mining sequential patterns: generalizations and performance improvements, Proceedings of the Fifth International Conference on Extending Database Technology (EDBT), Springer-Verlag, Heidelberg, 1996.

[19] N.G. Venkat, V.R. Vijay, I.G. William, K. Rajesh, Information retrieval on the World Wide Web, IEEE Internet Computing, 1997 (Sept./Oct.), pp. 58 – 68.

[20] V.R. Vijay, S.K.M. Wong, A critical analysis of vector space model for information retrieval, Journal of the American Society for Information Science 37 (5) (1986) 279– 287.

[21] K.F. Wong, W. Li, Intelligent Chinese information retrieval— why is it so difficult? Proceedings of the First Asia Digital Library Workshop, 1998, pp. 47 – 56.

[22] C.C. Yang, J. Yen, S.K. Yung, A.K.L. Chung, Chinese indexing using mutual information, Proceedings of the First Asia Digital Library Workshop, 1998, pp. 57 – 63.

[23] M.J. Zaki, N. Lesh, M. Ogihara, PLANMINE: sequence mining for plan failures, 4th International Conference on Knowledge Discovery and Data Mining (KDD), ACM Press, New York, 1998 (August).

Dr. Fu-ren Lin (Professor) received his Ph.D. in Information Systems from the University of Illinois at Urbana-Champaign in 1996. He taught in the Department of Information Management, National Sun Yat-sen University since 1996 before joining the Institute of Technology Management, National Tsing Hua University in 2004. His research works have appeared in IEEE Transactions on Engineering Management, Decision Support Systems, IEEE Intelligent Systems, Journal of Technology Management, etc. His current research focuses on e-business management, data/text mining, and professional community.

Mr. Kuen-jin Huang received his master degree from the Department of Information Management, National Sun Yat-sen University in 1999.

Dr. Nian-Shing Chen received the Ph.D. degree in computer science from National Tsing-hua University in 1990. He currently is a professor at the Department of Information Management of National Sun Yat-Sen University. He research interests include computer networks, e-learning, and knowledge management.
