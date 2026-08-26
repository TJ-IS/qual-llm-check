---
otero_id: 11240
otero_key: "6GZZ4SDB"
title: "Enabling effective workflow model reuse: A data-centric approach"
authors: "Zhiyong Liu; Shaokun Fan; Harry Jiannan Wang; J. Leon Zhao"
year: "2017"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2016.09.002"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Enabling effective workflow model reuse: A data-centric approach

Zhiyong Liu <sup>a</sup>, Shaokun Fan <sup>b,</sup>⁎, Harry Jiannan Wang <sup>c</sup>, J. Leon Zhao <sup>d</sup>

<sup>a</sup> Faculty of Management and Economics, Dalian University of Technology, China

<sup>b</sup> College of Business, Oregon State University, United States

<sup>c</sup> Lerner College of Business and Economics, University of Delaware, United States

<sup>d</sup> Department of Information Systems, College of Business, City University of Hong Kong, China

## a r t i c l e i n f o

Article history: Received 4 July 2014 Received in revised form 5 September 2016 Accepted 6 September 2016 Available online xxxx

Keywords: Workflow model reuse Workflow model management Data flow perspective Data dependency

## a b s t r a c t

With increasingly widespread adoption of workflow technology as a standard solution to business process management, a large number of workflow models have been put in use in companies in the era of electronic commerce. These workflow models form a valuable resource for workflow domain knowledge, which should be reused to support workflow model design. However, current workflow modeling approaches do not facilitate workflow model reuse as a fundamental requirement, leading to a research gap in effective workflow model reuse. In this paper, we propose a novel approach called Data-centric Workflow Model Reuse framework (DWMR) to provide a solution to workflow model reuse. DWMR compliments existing control-flow-focused workflow modeling approaches by explicitly storing workflow data information, such as data dependency, data task relationships, and data similarity scores. DWMR also provides data-driven work ow model search and composition algorithms to satisfy user query requirements by automatically combining multiple workflow models. We demonstrate the feasibility of the DWMR approach by applying it to data from a well-known industry workflow model repository.

© 2016 Elsevier B.V. All rights reserved.

## 1. Introduction

With increasingly widespread adoption of workflow technology as a standard solution to business process management (BPM), much effort is focused on designing appropriate workflow models that satisfy the business requirements for a given company. Workflow models are designed to support complex process management in many business domains such as supply chain management, knowledge management and e-commerce [1,2]. How to efficiently design workflow models to satisfy particular business requirements is one of the key factors of BPM success [3].

Workflow models are used to capture domain knowledge about business processes in organizations. Many modeling methods have been proposed and applied by both academic researchers and business practitioners, such as Petri nets [4], UML activity diagrams [5], metagraphs [6] and the dataflow-based approach [7]. The dataflowbased approach is a relatively new method, in which designers develop workflow models by analyzing the input and output data of tasks and their dependency relationships [7].Compared with other workflow modeling methods that require users to provide plenty of information about specific processes, such as description of business function, sequence of tasks and structured representation of business rules, dataflow-based modeling methods focus on the input and output data in the business processes. Thus, it is easier to gather information required for the dataflow-based modeling method, because input and output data items are usually contained in the documents that business users deal with on a daily basis.

When designing workflow models for a specific business context, workflow designers always confront with the difficulty of collecting domain knowledge [8]. A typical business process involves many functional departments of an organization, such as purchasing, production, and sales, and requires knowledge from these varied business domains. However, process designers usually possess expertise in modeling, system design or software engineering, but little business domain knowledge like sales or production. Process designers always devote considerable effort to collecting information from workers at the front line. Even though domain knowledge can be acquired from interviews, surveys and field studies, there is always a significant gap between designers' and users' understanding, which is caused by their different knowledge backgrounds.

Rather than starting from scratch, designers can gain valuable insights from the existing process records [9], which can serve as a valuable source of domain knowledge. To a certain degree, the existing models reflect the operational mechanisms of an organization. A formal approach is needed to utilize the knowledge embedded in existing workflow models in a systematic manner. Model reuse will certainly

Z. Liu et al. / Decision Support Systems xxx (2016) xxx–xxx

improve the quality and efficiency of business process design. Business practitioners have documented many workflow models in various business domains based on their knowledge and experiences, called Process Reference Models (PRMs), such as SAP Process Reference Model and Oracle Best Practice Processes [10]. So far, workflow model reuse mainly relies on function or control structure. However, little research has been done on workflow model reuse based on the data dependency, which takes the data flow of workflow models as the focus of model management.

We adopt a data-centric perspective for workflow model reuse for three reasons. First, data flow information can be directly acquired from users. Data collection is the starting point of business requirement collection when building workflow models. The users are usually familiar with the data that they are using and producing on a daily basis. By contrast, the control flow information that reflects complex logic is not explicitly documented in working environments; it is summarized by users based on their domain knowledge. Second, dataflow of workflow models is more intuitive and less error-prone than control flow [11]. The control flow-based models require integrating designers' in-depth understanding of model semantics and logic. Even the error rate of control flow models designed by professional companies is reported to be more than 10% [11]. Third, the data flow information is independent from workflow modeling paradigms and supports crossparadigm model reuse. The solutions for workflow model reuse based on the control flow perspective are vitally influenced by the model specification paradigms [12,13]. The control flow-centric models from different sources can be expressed following different paradigms such as Petri nets [14], UML activity diagram [5] and BPMN. Considerable effort is spent on transforming control flow models and adjusting model management algorithms. Workflow models with different paradigms can be managed in a unified way following a data-centric perspective.

In this paper, we fill the research gap by proposing a framework for data-centric workflow model reuse (DWMR), which consists of model storage, model search and model composition via a data-centric approach. Our contributions are as follows. First, we define the formal data structure of a workflow model repository and propose a datacentric indexing method for workflow models based on data dependency relationships. Second, we propose a method for matching user requirements with candidate workflow models based on data similarity and develop a flooding algorithm to search for model groups that satisfy a particular user query. Third, we develop a formal method to compose candidate groups of models when needed to meet a specific user requirement. We evaluate the approach by applying it to a business case and comparing the DWMR approach with existing approaches and human experts.

## 2. Literature review

## 2.1. Workflow modeling

The control flow perspective of workflow modeling focuses on the sequence and coordination of tasks. The objectives of control flow modeling are controlling, monitoring, optimizing and supporting business processes [14]. Petri nets have become one of the most popular control flow-based modeling paradigms since van der Aalst [14] introduced it into the workflow modeling field. In addition to providing an appropriate language for workflow specification, Petri nets also serve as a powerful analytical tool for verification of workflow models. Several important concepts have been introduced to support the analysis of the correctness of control flow models, such as structuredness [15,16] and soundness [17]. Vanderfeesten et al. [3] introduced cohesion and coupling metrics to evaluate workflow model design. Van der Aalst has extended Petri nets to propose a workflow net concept and the YAWL language [18]. Some extended forms of Petri nets are also proposed to add more data information to workflow models, including colored Petri nets [19] and timed Petri nets [20].

Most of the modeling methods from the control flow perspective or graph-based perspective ignore the importance of data flow. They just focus on the coordination of tasks or rules, while the data requirements of models, data exchange between tasks and data dependency relationships are often overlooked or simplified.

## 2.2. Data flow perspective

The data flow perspective was first proposed in the software engineering field [21,22] and more recently introduced into the business process modeling field to detect data errors and correct workflow models [23,24].

Compared with traditional modeling methods that focus on the structural issues [17], data flow is considered as an important complement to the workflow specification. Sadiq et al. [24] identify the importance of data flow issues to workflow research and introduce modeling [25], specification and validation of data flow. They also illustrate the essential requirements for data flow modeling and seven types of data anomalies. Russell et al. [26] describe a series of workflow data patterns to show the different ways to represent and use data flow in workflow systems. Data flow analysis is a useful tool for workflow verification, which has been used to validate the correctness of control flows. Sun. et al. [7] propose a formal data flow specification and develop algorithms to detect data anomalies based on data dependency. The data flow modeling method is further extended to support process integration [27]. Vanderfeesten et al. [2] introduced a product-based workflow design approach, which adopts a Product Data Model to capture the data dependency relationships. A formal workflow language based on Petri nets and nested relational calculus has been proposed to support data flow modeling [28].

## 2.3. Workflow model reuse

Research on management and reuse of models has a long history in fields such as software engineering [29,30] and operation research [31]. Existing models form an abundant source of domain knowledge and best practices. In the BPM field, they are referred to as Process Reference Models (PRMs) [32]. Many commercial companies have provided packages of their process designs and best practice for different industries, including SAP Process Reference Models and Oracle Best Practice Processes [10]. Reference Models help model designers avoid starting from scratch. These packages cover many business functions that can satisfy most of a company's basic requirements. Because of the unique characteristics of different companies, Process Reference Models must be adapted to fit a particular context before being adopted [33]. Models with a higher abstract level are more generalizable, and more effort is needed to adapt them to meet the specific requirements of the end user.

Researchers have studied workflow model reuse from different angles. Wang and Wu [10] propose a collaborative approach to integrate and manage process reference models (PRMs). Their approach is based on a “spiral” model for organizational knowledge creation and leverages Web 2.0 technologies such as social tagging and classification to maintain PRMs. The model patterns (or model components) are also reusable. Zhuge [34] defines workflow components with four characteristics: independency, encapsulation, completeness and consistency. Thom et al. [35] classify workflow patterns into nine categories, and Altintas et al. [36] abstract workflows into several components according to their service functions. Cao et al. [37] define the workflow components, which consist of function, quality of service, control flow model and business domain.

The model design cases are also a reusable resource. Madhusudan et al. [38] propose a framework to reuse two categories of workflow cases, i.e., prototypical cases and instance cases. They also introduce a similarity-based flooding algorithm to support case retrieval. Similaritybased model matching is another important aspect of model reuse. Madhusudan et al. [38] support case retrieval by matching the NAME properties of nodes in models through language processing and string matching techniques to get the initial similarities. Zhuge [39] calculates the matching degree of two activities with activity-distance. The similarity degree of processes is calculated using matching degree of activities, numbers of activities and numbers of sub-processes of the processes. Their research revealed the wide existence of reusable process units and tested the thresholds for similarity-based search.

Although previous research on workflow model reuse is fruitful, little research has explicitly considered the data-flow perspective, which is a unique feature of this paper. The main difference between our research and existing research are shown in Table 1. The relative advantages of our approach include: (1) utilizing the data flow information, which is a valuable resource and often ignored by existing research; (2) lowering the requirements for users to input requirements; and (3) supporting the search and composition of model groups.

## 3. Data-centric workflow model reuse (DWMR)

## 3.1. DWMR framework

We propose a framework for data-centric workflow model reuse, shown in Fig. 1.

## 3.1.1. Workflow model storage and organization

When a new workflow model is adopted by the company, the model should be organized and stored in the model repository. All models in the model repository should be encoded following a standard format.

## 3.1.2. Workflow model search

A data-centric search mechanism provides users with the most relevant models from the model repository to aid their model design work. The relevance of a workflow model is calculated based on the fit between models in the repository and user requirements.

## 3.1.3. Workflow model composition

When a group of models is found relevant to user requirements, the composition of these models should be presented to designers. The composed workflow model will be obtained by mapping the composed data dependency structure.

## 3.2. An illustrative example

We will illustrate the DWMR approach using two simplified banking processes. A process model repository has been built to store the existing models to facilitate new workflow model design. The two example processes are shown in Figs. 2 and 3 using extended UML activity diagrams as defined in [7].

## Transfer application

After receiving a transfer application form, the bank first checks to make certain that all needed information is provided. If the application form is not complete, additional information will be requested. Then it verifies the application to ensure that the information is accurate. After the application form is verified, it will be formally accepted by the bank. Then the password from the customer is checked before allowing the customer to access the account balance. If there is enough balance, the transfer will be executed and the process is finished.

## Credit payment application

After transaction information and authentication information are received from the client, the bank accepts the credit payment application. Then the customer's credit history record and liquid assets record are checked to create a credit score. The transaction information and credit score are analyzed to give an overall evaluation such as risk level and amount adjustment. Finally, the application with the evaluation result is approved by the officer.

A new workflow model of the Loan Application process needs to be designed, which begins with receiving an application and ends with that application being approved. The requirement can be considered as modeling a process that produces the data entity of an approved application form with an input data entity of the initial application form. Rather than starting from scratch, we can reuse the two aforementioned models because the new Loan Application process is similar to the existing models of credit assessment and approval. If no individual model can fulfill the requirements, composing a group of candidate models may be required.

## 3.3. Model storage and organization

Business data is one of the most essential components of a business process. The actual input data required by a task includes not only the data entities, but also their status. Data entity represents the information object that can be manipulated by agents, such as “Application Form” and “Credit Score.” Note that the data entity in this paper refers to a data item or a workflow form, which is different with the data entity concept in database [43]. Status data reflects the state that the entity has reached. For example, an “Application Form” that is initially filled out by a customer is different from an “Application Form” that is approved by the bank in the example in Section 3.2. Status data reflects the lifecycle of a data entity in a whole business process. According to Workflow Management Coalition's definition [44], “control data is very important for business process modeling and it is described as “state information about each workflow instance and state information about each activity instance” [44]. Thus, we include status information in data definition, because status data is always considered as a part of workflow data.

Definition 1. (Data) A data d in workflow model is defined as a 2-tuple, consisting of data entity and status, namely d = (Data entity, status). Example: data d = (Application form, verified) means “an application form which has been verified.”

Definition 2. (Workflow model) A workflow model (denoted as W) in the repository consists of both control flow information and data flow information. The control flow structure consists of the task set and the set of flows between tasks, while the dataflow structure describes a set of relationships between tasks and data, which contains tasks and

Table 1  
Comparison with existing approaches

<table><tr><td></td><td>Reusable units</td><td>Similarity calculation</td><td>Utilizing data flow information</td><td>User requirements</td><td>Individual model search</td><td>Group model search</td><td>Model composition</td><td>References</td></tr><tr><td>Control flow based approaches</td><td>PatternsModelsCases</td><td>Structure based, content based</td><td>No support</td><td>Sample models with structure and descriptions information</td><td>Support</td><td>No support</td><td>No support</td><td>[26,33–36,40,41][10,32,39,42][38]</td></tr><tr><td>DWMR</td><td>Models, model groups</td><td>Data dependency based</td><td>Support</td><td>Input and output data</td><td>Support</td><td>Support</td><td>Support</td><td></td></tr></table>

Please cite this article as: Z. Liu, et al., Enabling effective workflow model reuse: A data-centric approach, Decision Support Systems (2016), http:// dx.doi.org/10.1016/j.dss.2016.09.002

![](/api/attachments/6GZZ4SDB/fulltext/images/676754a6c8043bb4b45c96787c7ef8d9ce153e050ba8ea0bcbac5b6ee14cc8e9.jpg)  
Fig. 1. The data-centric workflow model reuse (DWMR) framework.

their input and output data. Formally:

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$W = \{\text{Model name WN};\text{Model description MD};\text{Control flow structure} T$ $= \{T,F\} ;Data set D = \{d_i\mid i = 1,2\dots n\} ;Task - data relationship TD$ $= \{(t,D_{in - t},D_{out - t})\mid t\in T\} \}$
</div>

WN is the unique identification of this model. Model description records the information provided by model designers to describe the function of this model. Г is the control flow structure, which consists of tasks and the flows between them. T is a finite set of tasks in W, $T = \{ t _ { i } | i = 1 , 2 . . . m \}$ , t is a specific task in $T \left( t \in T \right)$ . F is a finite set of the flows between tasks in $\begin{array} { r } { T , F = \cup ( t _ { i } \times t _ { j } ) , t _ { i } \in \mathrm { T } , t _ { j } \in T , i \neq j . } \end{array}$ The data items that are used or produced in this model form a data set D. TD describes the relationship between input/output data and tasks; $D _ { i n - }$ and $D _ { o u t - t }$ are the sets of input and output data of task t.

We have developed a formal method to deal with loops in workflow model. The main idea of this solution is to transform a cyclic model to a set of acyclic models, denoted as main path and feedback paths respectively. We introduce the method as follows:

Input: cyclic workflow models; output: a set of acyclic models, which are transformed from the main path and feedback paths of the cyclic models.

Preconditions: (1) All the input workflow models should be structured [17], which promises the errors caused by structure including deadlock and multiple instances are avoided. This is not a strong restriction, because most of the reusable models have been tested in application. Structuredness is a common requirement for most workflow modeling tools. (2) All the models must start with a start node and end with an end node. Every other node must be on a path from the start node to the end node. This is also a simple and common requirement, which ensures that the models are connected [14].

The cyclic model transformation algorithm is as follows. Step 1, omit all of the Split/Join nodes, and transform the models (M) to directed graphs (G) which consist of task nodes (N) and arcs. Step 2, search for a random path (P) from the start node (s) to the end node (e). Set a label with a number for every node on the path. The number for s starts with 0, and every immediate successor node in the path increases its

![](/api/attachments/6GZZ4SDB/fulltext/images/95fba92d09d6d2729744f43dd9878e77808abaec0c085f3b9ee49c778c6fc174.jpg)

Fig. 2. Workflow model of transfer application (Model I).

<table><tr><td>Please cite this article as: Z. Liu, et al., Enabling effective workflow model reuse: A data-centric approach, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.09.002</td></tr></table>

Z. Liu et al. / Decision Support Systems xxx (2016) xxx–xxx

![](/api/attachments/6GZZ4SDB/fulltext/images/d997f1c28b259aae7261151eb3a9aa397d05fc93be0e3f5efeddabfeb48f466d.jpg)  
da: (Transaction Record, received); db: (Authentication Record, received); dc: (Credit Payment Application Form, accepted) dd: (Credit History Record, recorded); de: (Liquid Asset Record, recorded); df: (Credit Score, calculated); $\mathrm { { d } _ { g } \mathrm { { : } } }$ (Evaluation Report, generated); dh: (Credit Payment Application Form, approved)  
Fig. 3. Workflow model of credit payment application (Model II).

number by 1. Step 3, in the remaining part of the graph besides the path, namely G − P. Search for paths (P′), which start from a node in P with a smaller number and ends with a node in P with a bigger number. Increment the path P with $p ^ { \prime } ,$ , namely $P = P + P ^ { \prime }$ . Step 4, repeat Step 3, until no more paths P′ is found. P is defined as the main path, and the remaining paths which exist in G besides P are defined as feedback paths. If there is not any feedback path found, then the original workflow model is acyclic. Step 5, mapping the main path and feedback paths to workflow models, by adding the Split/Join nodes to the corresponding positions.

An illustrative example is shown in Fig. 4. First, we omit all the Split/ Join nodes in the original model, and get the directed graph. Second, we search for a random path from s to e, namely $P \colon s \to A \to E \to F \to$ $I \to J \to D \to e . \operatorname { A }$ number is labeled for every node in P, from 0 to 7. Third, search for the paths (P′) that start from a node labeled with a smaller number and end with a node labeled with a bigger number. Add P′ to P. P′ includes $A \to B \to F , F \to G \to J , A \to B \to C \to G \to J$ and $A \to B \to C \to D .$ . Fourth, until no more P′ are found, denote the final P as the main path, and the remaining paths in the graph as feedback paths. Finally, we give mappings of the main path and feedback path as workflow models by adding the Split/Join nodes to the corresponding positions.

After dividing cyclic models to acyclic paths, we define rules to avoid the possible loops caused by the main path and feedback path pair (Fig. 5). After the model search and model composition stage, the feedback paths and the main path should be composed, to keep the model completeness.

Definition 3. (Data dependency relationship) In a workflow model, if a task produces data item $d _ { 2 }$ with data item $d _ { 1 }$ as input, then there is a direct data dependency relationship between $d _ { 1 }$ and $d _ { 2 } .$ We say that $d _ { 2 }$ directly depends on $d _ { 1 } ,$ , which is denoted as $d _ { 1 }  d _ { 2 } .$

We should note that there is no transitivity for direct data dependency relationships. If $d _ { 1 }  d _ { 2 }$ and $d _ { 2 }  d _ { 3 } ,$ , we cannot get the result $d _ { 1 }  d _ { 3 }$ . However, $d _ { 1 }$ is used to produce $d _ { 2 } ,$ and $d _ { 2 }$ is a precondition for producing $d _ { 3 } .$ When $d _ { 2 }$ is temporarily unavailable, $d _ { 1 }$ may be a necessary input for the system to produce $d _ { 3 } .$ . The system will produce $d _ { 2 }$ with $d _ { 1 }$ , and then produce $d _ { 3 }$ using $d _ { 2 }$ . We call the relation between $d _ { 1 }$ and $d _ { 3 }$ an indirect data dependency relationship.

For a set of data items $\{ d _ { i } \} ( i = 1 , 2 . . . k )$ , when $d _ { 1 }  d _ { 2 } . . . d _ { n \mathrm { ~ - ~ } 1 }  d _ { n }$ $( n = 3 , 4 \ldots k )$ , then there is an indirect data dependency relationship between d and $d _ { n }$ . We define that $d _ { n }$ indirectly depends on $d _ { 1 }$ , denoted as $d _ { 1 } \twoheadrightarrow d _ { n } .$ Transitivity is an important property of indirect data dependency relationships, namely $\mathrm { f } d _ { 1 } \twoheadrightarrow d _ { 2 }$ and $d _ { 2 } \twoheadrightarrow d _ { 3 } ,$ then $d _ { 1 } \nrightarrow d _ { 3 }$ .

Definition 4. (Data dependency distance) Data dependency distance between data items $d _ { 1 }$ and $d _ { 2 }$ is defined as the length of the shortest path of data dependency relationships that generate B from $d _ { 1 } .$ . Given a direct data dependency relationship $d _ { 1 }  d _ { 2 }$ , the data dependency distance between $d _ { 1 }$ and $d _ { 2 }$ is defined as 1, which is denoted as Distance $( d _ { 1 } , d _ { 2 } ) = 1$ . The distance between a node and itself is defined as $0 , \mathrm { D i s t a n c e } ( d _ { 1 } , d _ { 1 } ) = 0$ . For an indirect data dependency relationship $d _ { 1 } \twoheadrightarrow d _ { n }$ the minimum number of direct data dependency relationships

![](/api/attachments/6GZZ4SDB/fulltext/images/9978cb75c1fad61e63acc6379674e29e2058b2054fa6cd8a3449e68fb271c752.jpg)  
Fig. 4. Example of transforming cyclic workflow model.

Please cite this article as: Z. Liu, et al., Enabling effective workflow model reuse: A data-centric approach, Decision Support Systems (2016), http:// dx.doi.org/10.1016/j.dss.2016.09.002

#

Z. Liu et al. / Decision Support Systems xxx (2016) xxx–xxx

![](/api/attachments/6GZZ4SDB/fulltext/images/ddc70c56e32b91383852a2b4e84def8820bae5f03f86e8767aa2f7e4ea3f8904.jpg)  
Fig. 5. Main path and feedback path of transfer application (Model I in Section 3.2).

that constitute this indirect data dependency relationship is defined as the data dependency distance between $d _ { 1 }$ and $d _ { n } .$ The data dependency distance between $d _ { 1 }$ and d is determined by the shortest indirect data dependency relationship, namely Distance $( d _ { 1 } , d _ { 2 } ) \ : = \ : \operatorname* { m i n } ( m , n )$ . If there is not any data dependency relationship between $d _ { 1 }$ and $d _ { 2 } ,$ we define Distance $( d _ { 1 } , d _ { 2 } ) = + \infty$

In Fig. 5, Distance $( d _ { 1 } , d _ { 2 } ) = 1$ , because between $d _ { 1 }$ and d there is a direct dependency relationship. There are three paths from $d _ { 1 } \ t o \ d _ { 4 } ,$ where Lengt $1 ( d _ { 1 } \ \to \ d _ { 2 } \ \to \ d _ { 4 } ) \ = \ 2$ , Lengt $\ h ( d _ { 1 } \ \to \ d _ { 4 } ) \ = \ 1 ,$ Length $( d _ { 1 }  d _ { 3 }  d _ { 4 } ) = 2 .$ . The distance between $d _ { 1 }$ and $d _ { 4 }$ should be the minimum length of all the paths, then Distance $( d _ { 1 } , d _ { 4 } ) =$ min(2, 1, 2) = 1.

We define the distance between two models as the minimum distance between two data items in these two models respectively, namely Distance $( M _ { 1 } , M _ { 2 } ) = \mathrm { m i n } ( \mathrm { D i s t a n c e } ( A _ { i } , B _ { j } ) ) , A _ { i } \in M _ { 1 } , i =$ $1 , 2 , \ldots , n ,$ and $B _ { j } \in M _ { 2 } j = 1 , 2 , . . . , m$ . The distance of one data set is defined as the maximum distance between any two data items in this data set, namely ${ \mathrm { D i s t a n c e } } ( M ) = { \mathrm { m a x } } ( { \mathrm { D i s t a n c e } } ( A _ { i } , A _ { j } )$ | Distance(A , $A _ { j } ) < + \infty ) , A _ { i } , A _ { j } \in M , i , j = 1 , 2 , . . . , m$ . The conditional distance of a model M is defined as the maximum distance of any two data items in M that are involved in a given data dependency relationship set (C), denoted as Distance (M). C is a set of data dependency relationships, $C = \{ ( d _ { i n , I }  d _ { o u t , j } ) \} , D _ { i n } = \cup d _ { i n , i } \mathrm { a n d } D _ { o u t } = \cup d _ { o u t , j } , i = 1 , 2 , . . . , n$ and $j = 1 , 2 , . . . , m$ . Namely, Distance (M) = max(Distance $( A _ { i } , A _ { j } ) )$ where $A _ { i } , A _ { j } \in M ,$ , Distance $( \{ A _ { i } \} , D _ { i n } ) < + \infty$ , Distance({A }, D ) b $+ \infty , i , j = 1 , 2 , \ldots , m$

In the data structure in Fig. 6(a), let us define a model $M 1 { : } \{ d _ { 1 } , d _ { 2 } ,$ $d _ { 3 } \}$ and model $M 2 \colon \{ d _ { 5 } , d _ { 6 } , d _ { 7 } \}$ . The distance between M1 and M2 should be the length of the shortest path between any two nodes from M1 and M2 respectively. Obviously, the shortest path should be $\ " d _ { 2 }  d _ { 4 }  d _ { 5 } \ "$ and ${ } ^ { " } d _ { 3 }  d _ { 4 }  d _ { 5 } { } ^ { " }$ . Then, Distance $\mathbf { \Phi } ( M _ { 1 } , M _ { 2 } ) = 2$ The distance of an individual model is defined as the longest path existing in the model. In M1, the longest path should be $d _ { 1 }  d _ { 2 }$ and $d _ { 1 }  d _ { 3 }$ , then Distance(M1) = 1.

Definition 5. (Data item description) Data item description consists of optional descriptions of the data item, dependency relationships and data–task relationships showing the tasks that use specific data as input or output. Formally:

$$
\begin{array}{l} \text {Data item} = \{\text {Data name DN}; \text {Model name WN}; \text {Data description DD}; \\ \quad \text {Direct dependency DP_{d}} = \{(d \to d _ {i}) \mid d, d _ {i} \in D, i = 1, 2,... \}; \\ \quad \text {Indirect dependency DP_{i}} = \{(d \twoheadrightarrow d _ {j}) \mid d, d _ {j} \in D, j = 1, 2,... \}; \\ \quad \text {Data - task relationship DT} = \{(d, T _ {i}, T _ {o}) \}. \end{array}
$$

d is the identification of this data item. W is the name of the model that d belongs to. $D P _ { d }$ and DP are the sets of direct and indirect data dependency relationships of d respectively. DT records the tasks related to this data item d. T and $T _ { o }$ are the sets of tasks that use d as input and output respectively.

Definition 6. (Data dependency structure) Given a workflow model, a data dependency structure (DDS) is a graph structure in which nodes represent data and edges represent direct data dependency. DDS consists of data set and direct dependency between data, which is denoted as: $S = \{ D , D P _ { d } \}$

For example, in the Transfer Application model, the data set $D = \{ d _ { 1 } ,$ $d _ { 2 } , d _ { 3 } , d _ { 4 } , d _ { 5 } , d _ { 6 } , d _ { 7 } , d _ { 8 } \}$ , the direct dependency $D P _ { d } = \{ ( d _ { 1 }  d _ { 2 } )$ $( d _ { 1 }  d _ { 3 } ) , ( d _ { 1 }  d _ { 4 } ) , ( d _ { 2 }  d _ { 4 } ) , ( d _ { 3 }  d _ { 4 } ) , ( d _ { 4 }  d _ { 5 } ) , ( d _ { 4 }  d _ { 6 } )$ $( d _ { 4 }  d _ { 7 } ) , ( d _ { 4 }  d _ { 8 } ) , ( d _ { 5 }  d _ { 6 } ) , ( d _ { 6 }  d _ { 7 } ) , ( d _ { 7 }  d _ { 8 } ) \}$ . We represent the data items with ovals and indicate the dependency relationship with arrows. The data dependency structure of this model is illustrated in Fig. 6(a). From this visual index of this model, we can intuitively identify the direct and indirect dependency relationships. The data dependency structure of the Credit Payment Application model is created similarly, as shown in Fig. 6(b).

## 3.4. Model search

We show a model search requirement template below. The user describes the possible input and output data for the required model. For the Loan Application process, the search requirement can be expressed as “(Loan Application form, initial) ↠ (Loan Application form, approved).” The expected result could be an individual model that satisfies the user requirements or several models that collectively fulfill the requirements after appropriate composition. According to the different types of expected results, we further classify the data-centric model matching into Individual Model Matching and Group Model Matching.

## User requirement template for data-centric model search

User query: “User input ↠ expected output”

Expected result: matched individual models or model groups.

Note that the users can require the dependency between input and output to follow a certain path, with a query like “User input ↠ intermediate data ↠ expected output”, simply denoted as $" A \twoheadrightarrow B \twoheadrightarrow C "$ . For simplicity, we do not raise cases under this condition. The query will be decomposed as two sub-queries $^ { \prime \prime } A \twoheadrightarrow B ^ { \prime \prime } \mathrm { a n d } ^ { \prime \prime } B \twoheadrightarrow C . ^ { \prime \prime }$ The final result will be the composition of the models returned by the two sub-queries.

The cyclic models are divided into a set of acyclic models in the model search stage, namely the main path and feedback paths. We propose two rules dealing with the main path and feedback paths. Rule 1: the main path and its feedback path(s) cannot be calculated in the same candidate model set during the model search process. Rule 2: if one of the paths of a model is involved in the nal composed work ow

Z. Liu et al. / Decision Support Systems xxx (2016) xxx–xxx

![](/api/attachments/6GZZ4SDB/fulltext/images/cc907ed3c8c9d299e05ed8ba1c5bf18c8fc3337d5027e00a4a615a9f2d5efb78.jpg)  
Fig. 6. Examples of data dependency structure.

model, all the other paths should also be composed to keep the model complete.

## 3.4.1. Individual model matching

We show the user requirement template for individual model matching. $D _ { i n } \left( \operatorname { o r } D _ { o u t } \right)$ is a set of data items the user requires to be the model's input (or output), $d _ { i n }$ and $d _ { o u t }$ are data items, $d _ { i n } \in D _ { i n } ,$ $d _ { o u t } \in D _ { o u t } .$ . The user expects the target model to produce output data $D _ { o u t }$ using input data $D _ { i n }$ . If an individual model satisfies this requirement, then the dependency relationship $" d _ { i n } \twoheadrightarrow d _ { o u t } "$ should exist in the data flow structure of this model.

User requirement template for individual model match

User query: $D _ { i n } \twoheadrightarrow D _ { o u t } .$

Expected result: individual model containing $^ { \ast } d _ { i n } \twoheadrightarrow d _ { o u t } ^ { } , ( d _ { i n } \in D _ { i n } ,$ $d _ { o u t } \in D _ { o u t } ) .$

For example, the user requirement for the Loan Application process can be expressed as follows: $D _ { i n } = \left\{ \begin{array} { r l r } \end{array} \right.$ {(Loan Application form, initial)} and $D _ { o u t } = \{ ( \mathrm { L o a n }$ Application form, approved)}. The expected result is a set of models $W = \{ w _ { i } \}$ . The dependency relationship set of $w _ { i }$ is denoted as $D P _ { w i } ,$ which includes both direct and indirect dependencies in $w _ { i } .$ . The data dependency relationship required by the user, “(Loan Application form, initial) ↠ (Loan Application form, approved),” should belong to $D P _ { w i }$ which means that the target models should be able to produce “(Loan Application form, approved)” with input “(Loan Application form, initial)”.

## User requirement example of individual model match

User query: {(Loan Application form, initial)} ↠ {(Loan Application form, approved)}.

Expected result: $W = \{ w _ { i } \mid { } ^ { * }$ (Loan Application form, initial) ↠ (Loan Application form $a p p r o v e d ) ^ { * } \in w _ { i } , D P , i = 1 , 2 , \ldots \} .$

There may be more than one model that contains $" d _ { i n } \twoheadrightarrow d _ { o u t } "$ . We measure the quality of the result models based on their similarities with user requirements. Extending the definition of similarity measure defined in [45], we define similarity as follows:

Definition 7. (Data set similarity) The data set described in the user requirement is denoted as $D _ { U } ( D _ { U } = D _ { i n } \cup D _ { o u t } ) ,$ , the data set contained in a candidate model is denoted as $D _ { M } .$ The data set similarity is defined as follows:

$$
S I M _ {D a t a} = \frac {\left| D _ {U} \cap D _ {M} \right|}{\left| D _ {U} \cap D _ {M} \right| + \alpha \cdot \left| D _ {U} - D _ {M} \right|}
$$

The data set similarity focuses on the proportion of the common data elements between the user's data set and the model data set. The variable α $( \alpha \ge 0 )$ denotes the weight of the data set that includes the data items in the user requirements but not in the model. In practice, the variable α should be predefined. The initial value of α can be assigned as 1, which means that the common and uncommon data sets between the user requirements and the model have the same importance. Different values can be assigned to α to search for the one leading to best performance, which is beyond the scope of this paper.

Definition 8. (Data dependency similarity) The data dependency relationship set that is described in the user requirements is denoted as $D P _ { U } ,$ , which is a set of dependencies like ${ } ^ { \ast } d _ { i n }  d _ { o u t } { } ^ { \ast } ( d _ { i n } \in { \cal D } _ { i n } , $ $d _ { o u t } \in D _ { o u t } )$ . We can simply express the data dependency relationship set as ${ } ^ { \ " } D P _ { U } = D _ { i n } \twoheadrightarrow D _ { o u t } { } ^ { \prime }$ . The data dependency similarity between a candidate model M and $D P _ { U }$ is defined as follows:

$$
S I M _ {d e p} = \frac {\text { Distance } _ {D P _ {U}} (M)}{\text { Distance } _ {D P _ {U}} (M) + \beta \cdot (\text { Distance } (D _ {i n} , M) + \text { Distance } (M , D _ {o u t}))}
$$

Similar to the definition of data set similarity, data dependency similarity focuses on the common part between the data dependency relationship sets of user requirements and candidate models. The variable β $( \beta \ge 0 )$ denotes the weight of the uncommon data dependency set and should be predefined in practice. Similar to $\alpha , \beta$ is assigned with an initial value of 1 in this study, and the most appropriate value could be obtained after experiments.

We evaluate the similarity between user requirements and candidate models from two aspects: data set and data dependency. The overall similarity should be a synthesis of the above two similarity metrics, which is defined next.

Definition 9. (Synthesized similarity) The synthesized similarity is the weighted sum of data set similarity and data dependency similarity:

$$
S I M = \gamma \cdot S I M _ {d a t a} + (1 - \gamma) \cdot S I M _ {d e p}
$$

For $0 \leq \gamma \leq 1$ , γ and $1 - \gamma$ represent the weights of $S I M _ { d a t a }$ and $S I M _ { d e p }$ respectively, and should be predefined. We assign 0.5 to γ in practice, which means the importance of data set similarity and data dependency similarity is treated equally. In the Loan Application example, we assume that the candidate individual model is the Credit Payment Application model shown in Fig. 3. The user query is described. The common data set between user requirements and the model data set is {(Application form, approved)}, and the uncommon data set is {(Application form, initial)}. $S I M _ { d a t a } = 0 . 5 ~ ( \alpha = 1 )$ . The distance between the model and $D _ { i n }$ and $D _ { o u t }$ are 1 and 0 respectively. The distance of the model under the condition of user requirements is 4. The data dependency similarity between the model and user query is $S I M _ { d e p } = 0 . 8 \ ( \beta = 1 )$ ). Finally, the synthesized similarity between user query and the candidate model is 0.65 $( S I M = 0 . 5 \times 0 . 5 + 0 . 8 \times$ $0 . 5 = 0 . 6 5 , \gamma = 0 . 5 )$

## 3.4.2. Group model matching

When individual model match returns no result or the similarities of returned models cannot reach the threshold value, we can conduct an additional search for model groups that may satisfy the requirements after composition. The user requirement for matching multiple models is described below.

## User requirement template for group model match

User query: $D _ { i n } \twoheadrightarrow D _ { o u t } .$

Expected result: model groups containing $\mathrm { } ^ { \ast } d _ { i n } \twoheadrightarrow \ldots \twoheadrightarrow d _ { k } \twoheadrightarrow \ldots \twoheadrightarrow d _ { o u t } \ ' $ $( \mathrm { i . e . , ~ a ~ }$ model set $S = \{ W _ { i } \mid i = 1 , 2 , . . . , n \}$ , in which $W _ { 1 }$ contains $" d _ { \mathrm { n } } \twoheadrightarrow d _ { o u t } \ "$ , Model W contains $^ { \mathfrak { n } } d _ { n \mathrm { ~ - ~ } 1 } \twoheadrightarrow d _ { n } ^ { \mathfrak { n } } . . .$ , Model $W _ { n }$ contains $^ { \ast } d _ { i n } \twoheadrightarrow d _ { 1 } ^ { \prime \prime } , ( d _ { i n } \in D _ { i n } , d _ { o u t } \in D _ { o u t } ) )$

As illustrated above, the user requirements can be decomposed to a certain level. After finding a model $W _ { 1 }$ which contains $d _ { o u t }$ and when the initial similarity between $W _ { 1 }$ and user requirements exceeds a predefined threshold, we scan $W _ { 1 }$ to get a data set (denoted as $D _ { 1 } )$ where all data items determine $d _ { o u t } .$ For every data item in this data set, e.g., d , the second model $W _ { 2 }$ with a data item $d _ { n \mathrm { ~ - ~ } 1 }$ that satisfies $^ { \ast } d _ { n \mathrm { ~ - ~ } 1 } \twoheadrightarrow _ { \mathrm { ~ - ~ } } d _ { n } ^ { \mathrm { ~ \scriptsize ~ \cdot ~ } }$ can be derived. Then a new data set (denoted as $D _ { 2 } )$ can be found from $W _ { 2 } ,$ in which all data items determine the previous data item $( d _ { n } )$ . The above procedure can be repeated until $d _ { i n }$ appears in a new data set. Because the complexity of this procedure increases sharply when more models are added to the group, a model group size threshold should be predefined to limit the search space. When the number of models in a group exceeds the threshold and the requirement is still unsatisfied, the group should be abandoned with no result returned. We propose a formal algorithm for model searching, shown in Fig. 7.

## 3.5. Model composition

After identifying the candidate model groups, we need to compose the models. In the Loan Application Process design example, two candidate models are the main path of the Transfer Application model (Model I) and the Credit Payment Application model (Model II) shown in Figs. 2 and 3.

In this example, the user requirement is expressed as the data dependency relationship “{(Loan Application form, initial)} ↠ {(Loan Application form, approved)}”. It means that: by using the input of data item “(Loan Application form, initial)”, the composed model should produce data item “(Loan Application form, approved)” as output. In the individual model search phase, using the flooding algorithm, we cannot find any individual model that fulfills this user requirement. After group model search, the dependency relationship “(Transfer Application form, accepted) ↠ (Transfer Application form, approved)” $\left( d _ { c } \twoheadrightarrow d _ { h } \right)$ in Model II and “(Credit Payment Application form, initial) ↠ (Credit Payment Application form, accepted) $" ( d _ { 1 } \twoheadrightarrow d _ { 4 } )$ in Model I are identified, where ${ \mathsf { d } } _ { 4 }$ has the same data fields as $d _ { c } ,$ i.e., $\mathbf { \ddot { \rho } } d _ { 4 } = d _ { c } \mathbf { \vec { \rho } } .$ ” The condition of building a model group of Model I and Model II is satisfied. The resulting model should be a composition of the two models that contain $" d _ { 1 } \twoheadrightarrow d _ { 4 } "$ and $" d _ { c } \twoheadrightarrow d _ { h } "$ ” respectively $( d _ { 4 } = d _ { c } )$

Definition 10. (Linking node and linked node) Assume dependency $\ " d _ { i } \twoheadrightarrow d _ { j } \ " ( i \neq j )$ exists in model $W _ { 1 }$ and dependency $\ ^ { \mathfrak { u } } d _ { p } \twoheadrightarrow d _ { q } ^ { \mathfrak { n } } \left( p \neq q \right)$ exists in model $W _ { 2 }$ . If $d _ { j } = d _ { p } ,$ , then the dependency $\ " d _ { i } \twoheadrightarrow d _ { q } \ "$ can be achieved after composition of $W _ { 1 }$ and $W _ { 2 } .$ . We call $d _ { j }$ and $d _ { p }$ a Linking Node Pair. d and $d _ { p }$ are denoted as Linking Node and Linked Node respectively. For example, $d _ { 4 }$ is called linking node and $d _ { c }$ is called linked node in Fig. 8.

The Data-centric Model Composition algorithm contains three major steps:

Step 1 (Pruning): taking every linking node, $\mathrm { e . g . , } d _ { 4 }$ in Model I in Fig. 8, and the user required output node, e.g., $d _ { h }$ in Model II in Fig. $^ { 8 , }$ as the ending nodes, we search the nodes that are not included in the data dependency relationships of the ending nodes. Delete data items that do not determine the output nodes or the linking nodes, i.e., $d _ { 5 } , d _ { 6 } , d _ { 7 } , d _ { 8 } ,$ , and the associated data dependency relationships. Delete data items that determine linked nodes, $\mathrm { i } . \mathrm { e } . , d _ { a } , d _ { b } ,$ and the associated data dependency relationships. Delete the direct data dependency relationships that end with linked nodes.

Step 2 (Combination): after pruning the unnecessary data set and data dependency relationships, merge the linking node pair with the same data fields as a single node $\mathrm { ( d _ { 4 } ) }$ and $d _ { c } )$ . Replace the linking nodes and linked nodes in the dependency relationships with the merged node. The data dependency structure after combination is shown in Fig. 9.

Step 3 (Mapping): the composition of the data dependency structure helps us design a reference control flow model. We describe the mapping approach simply as follows: first, decide the relationship between any two tasks in the workflow model based on their data dependency relationship. For example, tasks $t _ { 1 }$ and $t _ { 2 }$ produce data $d _ { 1 }$ and $d _ { 2 }$ respectively. If $d _ { 1 } \twoheadrightarrow d _ { 2 } ,$ then $t _ { 1 }$ should be executed earlier than $t _ { 2 } ,$ they should be in sequence relationship. $\operatorname { I f } d _ { 1 }$ and $d _ { 2 }$ have no dependency relationship, then $t _ { 1 }$ and $t _ { 2 }$ should be in parallel; second, because multiple data items can be produced by one task, different relationships can be detected between tasks; third, build the workflow model without parallel first; and finally, add parallel relationships to the model without interrupting the existing sequence relationships. Due to limited space, the formal mapping algorithm is not in the scope of this paper. Please refer to [46], which introduces a formal approach to building workflow models based on their data flow structure. After the model mapping, if a path of a workflow model is involved in the composed model, the other paths should be composed to keep the model complete.

```csv
Algorithm 1: Model Searching Algorithm

Input:
a. User requirements U = (Din, Dout), where Din = {din-i} and Dout = {dout-j}, i,j = {1,2,...}
//User requirements are expressed as the input and output data set of the new model
b. Model set M, where M = {Mi}, the data set of Mi is Dk = {dj} and data dependency set of Mi is DPi = (dpik), where ij,k = {1,2,...}
//The models in repository, their data set and data dependency set
c. Threshold value a and b
Output:
a. Candidate model set S = {Ms1,Ms2,...,Msn}
b. Candidate model group set S' = {G1,G2,...,Gm}, where Gi = {Mi1,Mi2,...,Mi}
1. for each model Mk ∈ M, calculate SIMdata(U, Mk) //Calculate the Data Similarity(Definition 6)
2. if SIM (U, Mk) > a, add Mk to S //If Synthesized Similarity(Definition 8) between model and user requirements reach threshold, return the model
3. end for
4. for each model M_i ∈ S
5. for each model M_j ∈ M-M_i
6. create combined model Mc = (Dc, DPc), Dc = Di ∪ Dj and DPc = DPi ∪ DPj //Data dependency structure combination
7. calculate SIM (U, Mc) //Calculate the Synthesized Similarity
8. if SIM (U, Mc) > b, create model group Gc = (Mi, Mi),
9. define SIM (U, Gc) = SIM (U, Mc), add Gc to S'//Similarity of a model group is defined as similarity of combination of the models in group
10. end for
11. end for
12. for each model group Gi ∈ S'
13. Di = D1 ∪ D2 ∪ ... ∪ Dj, DPi = DP1 ∪ DP2 ∪ ... ∪ DPj, where Mj ∈ Gi, Mj = (Dj, DPj), j = 1,2,...,n //Combine the models in the group
14. for each model Mk ∈ M-Gi //Continuously add new models to existing groups, try to increase the group similarity
15. create combined model Mc = (Dc, DPc), Dc = Di ∪ Dj and DPc = DPi ∪ DPk
16. calculate SIM (U, Mc)
17. if SIM (U, Mc) > SIM (U, Gi), create group Gi' = Gi+Mk, add Gi' to S'
18. end for
19. end for
```  
Fig. 7. Model searching algorithm.

We formulate the model composition algorithm in Fig. 10.

## 4. Case study

We evaluate our DWMR approach in two ways. First, we assess the feasibility of our approach by applying it to a business case. Second, we invite human experts and apply the existing control flow based approach to the same problem and compare those with the result generated by our approach. The performance of our approach will be evaluated by cross-comparison.

## 4.1. Case description

Business process designers are required to design a new process that illustrates budget planning for a company. This process begins with setting the annual business goals in the directors' board meeting, continues across multiple departments and ends with determination of the budget in the financial department. It is extremely difficult for an external designer to design this process model because domain knowledge from multiple departments is required. Without sufficient domain knowledge, designing such a model is often difficult, time consuming and error prone.

In this case, Oracle Best Practice Processes are adopted as the model repository. We show how the data-centric model reuse approach can be used to aid process design by utilizing these existing models. Oracle Best Practice Processes is a package of more than 400 process reference models provided by Oracle. The models are all derived from past experiences and practices, and cover all business functions in an organization. This repository can be considered to be very similar to a private model repository of an organization.

We use our model storage approach to input these models into our repository. According to definition 5, we get the data dependency structure of the model “Defining business strategy”. Due to limited space, we only show an example model from our repository, which are referred to by the results of our approach and human experts (Fig. 11).

## 4.2. Results of DWMR approach

The user query is expressed as “(Business Goal Report, approved) ↠ (Budget Report, approved)”.

First we conduct Individual Model Matching. We show results of the top seven models with the highest similarity scores in Table 2. We set the thresholds for data similarity, data dependency similarity and

```txt
Please cite this article as: Z. Liu, et al., Enabling effective workflow model reuse: A data-centric approach, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.09.002
```

Z. Liu et al. / Decision Support Systems xxx (2016) xxx–xxx

![](/api/attachments/6GZZ4SDB/fulltext/images/cb2181137b0b334059bda89694de0f7fd9bad2f2e619d3a2a7e134232b1e240f.jpg)  
Fig. 8. Prune the unnecessary data and dependency relationships.

synthesized similarity as 0.1, 0.1 and 0.2 respectively. M2, M1 and M3 are the results of individual model matching using DWMR approach. There is not any individual model that possesses a similarity of 1.0, which means the user requirements cannot be fulfilled by reusing only one existing model.

Next, since individual model matching cannot directly fulfill the user requirements, we conduct group model matching. As shown in Table 3, group 1 (M1, M2 and M3) has reached the similarity of 1.0, which is accepted as the candidate result. Although group 6 (M1, M2, M3 and M4) has also reached the highest similarity, it is detected as a superset of

![](/api/attachments/6GZZ4SDB/fulltext/images/2f655fd1a65371809f5cc34c104bf27aaea9be6aaadbe123f433fa18ec5bc3ea.jpg)  
Fig. 9. Composition of data dependency structures and workflow models.

Please cite this article as: Z. Liu, et al., Enabling effective workflow model reuse: A data-centric approach, Decision Support Systems (2016), http:// dx.doi.org/10.1016/j.dss.2016.09.002

```txt
Algorithm 2: Model Composition Algorithm

Input:
a. Model group set S'={G_i}, where G_i={M_ij}, i_j={1,2,...} //Model groups and the models in the groups
b. Model set M, where M=∪G_i={M_k}, where M_k=(D_k, P_k), data set D_k and data dependency set DP_k. //The model set and the data set and data dependency set of every model
Output:
a. Combined model set S'={M_c,i}, where i={1,2,...} //The set of the combined data flow models
b. Combined workflow model set W'={W_j}, where i={1,2,...} //The set of the combined control flow models
1. for each model group G_i ∈ S'
2.    for each model M_j ∈ G_i, where D_j ∩ D_out ≠ Ø // Start with searching the models related to the data output of user requirements
3.    for each model M_k ∈ G_i-M_j
4.    if D_j ∩ D_k ≠ Ø, then //If the model is connected to the previous model
5.    define D_c = D_j ∩ D_k = {d_c1, d_c2, ..., d_ca}
6.    create a new model M_a=(D_a,DP_a), where D_a=D_c, DP_a=Ø //Combine the model with previous model to create a new model
7.    for each d_p ∈ D_a
8.    for each d_q ∈ D_j
9.    if (d_p,d_q) ∈ DP_j, then add d_p and d_q to D_a, add (d_p,d_q) to DP_a
10.    end for
11.    for each d_t ∈ D_k
12.    if (d_t,d_p) ∈ DP_k, then add d_t and d_p to D_a, add (d_t,d_p) to DP_a
13.    end for
14.    end for //Update the data set and data dependency set
15.    add M_a to G_i, delete M_j and M_k from G_i //Update the model group with the combined model
16.    end for
17.    if G_i-M_j=Ø, then add M_j to S'//When all the models in group are combined, return final model
18.    end for
19. end for
20. for each model M_i ∈ S'
21.    define W_i=mapping(M_i) //Mapping the data flow model to control flow model
22.    add W_i to W'
```  
Fig. 10. Model composition algorithm.

group 1, which means that the addition of M4 did not increase the similarity, and group 6 does not contain more useful information than group 1. Therefore, group 6 is rejected as a duplication of group 1. For the same reason, group 5 is rejected as a duplication of group 2. Group

4 (M1 and M3) possesses a high data similarity and it is rejected. This is because M1 and M3 do not have a common data set, which means that the two models are not connected and cannot be composed directly. It cannot serve as a candidate group for model composition. Using

![](/api/attachments/6GZZ4SDB/fulltext/images/2e802dc84611124fd351c8c7d33d8f21bc298ed4b9fb0f00b24a51ddde833c6d.jpg)  
T1: Establish Business Goals; T2: Define Enterprise Performance Measure; T3: Formulate Planning Discipline

DATA ITEMS d1: (Business Goal Report, approved): d2: (Enterprise Performance Report, recorded): d3: (Performance Measure Form, generated); d4: (Planning Discipline Report, recorded)

Fig. 11. Define business strategy (M1).  
```txt
Please cite this article as: Z. Liu, et al., Enabling effective workflow model reuse: A data-centric approach, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.09.002
```

T1: Establish Business Goals: T2: Establish Plan and Forecast Processes and Scenarios: T3: Create Business Plan: T4: Create Financial Forecasts: Ts: Approve and Finalize Business Plan and Forecast; T6: Publish Business Plan and Forecast: T7: Establish Budget Processes and Scenarios: Ts: Create Budget: T9: Approve and Finalize Budget Data Items:

Table 2  
Individual model matching result.

<table><tr><td>Model no.</td><td>Data similarity</td><td>Dependency similarity</td><td>Synthesized similarity</td><td>Rank according to synthesized similarity</td></tr><tr><td>M2</td><td>0.667</td><td>0.625</td><td>0.646</td><td>1</td></tr><tr><td>M1</td><td>0.667</td><td>0.167</td><td>0.417</td><td>2</td></tr><tr><td>M3</td><td>0.333</td><td>0.429</td><td>0.381</td><td>3</td></tr><tr><td>M4</td><td>0.667</td><td>0</td><td>0.333</td><td>Rejected</td></tr><tr><td>M5</td><td>0.667</td><td>0</td><td>0.333</td><td>Rejected</td></tr><tr><td>M6</td><td>0.667</td><td>0</td><td>0.333</td><td>Rejected</td></tr><tr><td>M7</td><td>0</td><td>0</td><td>0</td><td>Rejected</td></tr><tr><td colspan="5"> $\alpha = \beta = 1, \gamma = 0.5$ </td></tr></table>

Models in bold font are selected by the DWMR approach based on the simialrity scores.

data flow-based workflow modeling algorithms (e.g. [46]), the composed process model of M1, M2 and M3 is shown in Fig. 12.

Table 3  
Group model matching result

<table><tr><td>Group no.</td><td>Model</td><td>Data similarity</td><td>Dependency similarity</td><td>Synthesized similarity</td><td>Rank</td></tr><tr><td>G1</td><td>M1, M2, M3</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1</td></tr><tr><td>G2</td><td>M2, M3</td><td>1.0</td><td>0.889</td><td>0.944</td><td>2</td></tr><tr><td>G3</td><td>M1, M2</td><td>0.667</td><td>0.750</td><td>0.709</td><td>3</td></tr><tr><td>G4</td><td>M1, M3</td><td>1.0</td><td>--</td><td>--</td><td>Rejected</td></tr><tr><td>G5</td><td>M2, M3, M4</td><td>1.0</td><td>0.889</td><td>0.944</td><td>Rejected</td></tr><tr><td>G6</td><td>M1, M2, M3, M4</td><td>1.0</td><td>1.0</td><td>1.0</td><td>Rejected</td></tr><tr><td colspan="6"> $\alpha = \beta = 1, \gamma = 0.5$ </td></tr></table>

Models in bold font are selected by the DWMR approach based on the simialrity scores.

## 4.3. Comparison with human experts

Next, we assess the performance of our approach by comparing our results with the results of human experts. Five senior PhD students from the Information Systems Department were invited to serve as human experts. Their confidence of expertise is 4.6 (5-point expertise scale, maximum is 5). The human experts were given the same requirements that we used in the case study. The same model repository was also provided for them. The experts were asked to finish the task in two steps. First, they needed to select the most useful models for the requirements from the repository and rank the usefulness of the models based on their judgment. The models nominated by at least 4 experts are included in the final results. Table 4 shows the comparison between our DWMR results and expert results.

The experts agreed on 4 models that are considered most useful for the model design work. Three of the four models are also recommended by our approach. The precision and recall of our results are 100% and 75% respectively. The experts selected Model M7 which was not in our result. M7 is ranked with lowest usefulness by experts and it is not adopted by any model group for model composition. The reason that M7 is selected by experts in the model search step is that the experts are significantly influenced by the semantic information of the models. The words “Strategy” and “Budget” in M7's name are very close to the expressions in user requirements, which lead the experts to overestimate usefulness of this model.

The results of human experts can be considered as a cross reference to prove the correctness of our results. In the comparison, there is a high consistency between the results of our approach and the decisions made by human experts. This indicates that our approach automatically selected almost the same models (or model groups) as the human experts.

The second task for the experts is to find appropriate compositions of the candidate models to fulfill the requirements. The model groups that at least 4 experts agreed on are included in their final results. The comparison of the results of our approach and the experts is shown in Table 5. The results generated by experts and our approach are almost the same, which makes the precision and recall both 100%. The only difference is the ranks of model groups 2 and 3, which can be explained by the different perspectives adopted by experts and our approach.

The purpose of the cross-comparison is not to prove that our approach outperforms the human experts. The most critical issue in model reuse is the selection of appropriate models (or model groups). By adopting our approach, the similarity of models (or model groups) and the choices of models (or model groups) can be done in an automatic manner. The results of human experts are used as a cross reference to prove the correctness of our results. In the comparison, there is a high consistence between the results of our approach and the decisions made by human experts, indicating that our approach automatically selected almost the same models (or model groups) as the human experts in the reuse-based process design. Thus, we conclude that the approach can assist the process designers in improving decision making efficiency, with little loss on correctness.

## 4.4. Comparison with existing approaches

We also applied existing approaches to this case. Through a comparison of the results, the advantage of our approach can be demonstrated. Most existing approaches are control flow-based, which can be further classified into two categories: structure-based and content-based. These approaches are not capable of processing data flow information, which distinguishes the main advantage of our approach. We manually transform the user requirements to the control flow based form. The

![](/api/attachments/6GZZ4SDB/fulltext/images/7aac29f454db9b5a550153ddf8208eab6fb92da11fe2dfeb59f04fab7cf19db6.jpg)

d1: (Business Goal Report, approved): d2: (Planning Process Document, generated): d3: (Planning Scenario Document, generated); d4: (Enterprise Performance Report, recorded); ds: (Business Plan, initial); d6: (Financial Forecast Form, initial) d7: (Business Plan, approved); ds: (Financial Forecast Form, approved); d9: (Business Plan, published); d1o: (Budget Processes Document, generated); d11: (Budget Report, initial); d12: (Budget Report, generated); d13: (Budget Report, approved)

Fig. 12. Composed workflow model.

Table 4  
Comparison of individual model search results.

<table><tr><td>Model no.</td><td>Model name</td><td>Average usefulness</td><td>Number of nominations</td><td>Rank by experts</td><td>Rank by our approach</td></tr><tr><td>M1</td><td>Defining business strategy</td><td>4.4</td><td>5</td><td>1</td><td>2</td></tr><tr><td>M2</td><td>Creating business plans and forecasts</td><td>3.8</td><td>5</td><td>2</td><td>1</td></tr><tr><td>M3</td><td>Establishing capital and operating budgets</td><td>3.6</td><td>5</td><td>3</td><td>3</td></tr><tr><td>M7</td><td>Defining marketing strategy, plan and budget</td><td>2.8</td><td>4</td><td>4</td><td>-</td></tr><tr><td colspan="6">Precision = 100%, recall = 75%</td></tr></table>

Models in bold font are selected by the DWMR approach based on the similalrity scores.

data flow based expression “(Business Goal Report, approved) ↠ (Budget Report, approved)” is transformed to “Establish Business Goals (Task1) ↠ Approve and Finalize Budget (Task2).” The control flow based approaches are applied to find the models that are similar to the path from Task1 to Task2.

## 4.4.1. Structure-based approach

The similarity of two structures is defined based on the edit distance between them [42]. The edit distance equals the minimum number of basic actions that need be taken to transform one structure to the other. The basic actions include insertion, deletion and substitution of nodes. The similarity of Models M1 and M2 is defined as follows.

$$
\text { SIMs } (M 1, M 2) = 1 - \frac {\text { Edit   distance } (M 1 , M 2)}{\text { Max } (\mid M 1 \mid , \mid M 2 \mid)}
$$

## 4.4.2. Content-based approach

The similarity of two models is calculated based on the similarities of the task labels [40]. The similarity of two labels is simply defined as “Number of common words in two labels/total amount of words in two labels”, where the meaningless function words are not counted. The content-based similarity of Models M1 and M2 is defined as:

$$
\operatorname{SIMc} (M 1, M 2) = \frac {2 \sum_ {\text { label } 1 \in M 1 , \text { label } 2 \in M 2} \operatorname{SIM} _ {l} (\text { label } 1 , \text { label } 2)}{| M 1 | + | M 2 |}
$$

The results of the control flow-based approaches are shown in Table 6. Structure-based and content-based methods cannot process the data flow information automatically. It takes human efforts to transform the information into control flow-based forms. Thus, if a user only provides the data flow information like data input and output, control flow-based approaches will not be effective. The advantage of our approach is lowering the requirement for users' input.

In the results, M2 is ignored by both structure-based and contentbased approaches. However, M2 is accepted by our approach and human experts. The reason is that both control flow-based approaches did not take the data flow information into consideration. M2 has no common tasks or labels, but is closely connected with the user requirements, in terms of data flow. DWMR approach detects this connection through data dependency analysis. The control flow-based approaches rely on the accurate estimate of structures or contents of the process model. Our data-centric approach overcomes this shortcoming.

Both control flow based approaches cannot conduct similarity calculations for model groups with user requirements, and cannot perform model composition. This is another unique advantage of DWMR.

## 5. Discussion

The DWMR framework proposed in this paper aims to support workflow model reuse based on data flow. Our research provides contributions to the research fields of workflow design and data flow modeling. While traditional process design approaches require users to start from scratch [47], our research provides an alternative reusebased approach. Most of the existing reuse-based approaches provide solutions for matching and modification for individual models [10,32, 39,42]. We propose that the connections among individual models can be detected and the groups of connected models can serve as reusable units. Our approach makes important improvement to the existing reuse-based approaches [10,32,39,42].

Our results also enrich the knowledge base of data flow research. Since being introduced to the business process research field, data flow analysis has been mostly applied to error detection and model verification [23,24]. By considering data flow as the interconnection mechanism between business process models, we propose methods for multiple model matching and data flow-driven model composition. To the best of our knowledge, our paper is the first attempt to discuss the application of the data flow perspective to model reuse and model composition.

This study also suffers from several limitations. First, we utilize the Oracle Best Practice Processes to simulate the model repository of a company. This data set is provided by Oracle based on their consulting and system design experiences in real business. The source of this data set guarantees that to a high degree it can reflect the real situation in a business environment. We admit that we have fewer models than that in a real repository of an organization. Second, some variables used in the model searching and model composition algorithms are not easy to determine. For example, the weights of data similarity and dependency similarity are set as the same when calculating the synthesized similarity. The best values of these variables should be determined by continuous tests in a real data environment. These values may be different for process models from different companies, because of the variety of business contexts and data qualities.

## 6. Conclusion

Existing workflow models can be used as a knowledge base for workflow model design. However, developing workflow models based on existing models is challenging because of the volume and complexity of business processes. In order to facilitate workflow model reuse, we proposed a data-centric framework for workflow model reuse (DWMR), which includes three components: a formal data structure for workflow model repository and indexing, a model searching algorithm and a model composition algorithm. We applied DWMR approach to a business case to show its feasibility. Further, we compared the results generated by our approach and human experts, and found that our approach has a high accuracy in terms of precision and recall. Our approach sets up the foundation for automating workflow model storage, search and composition, which enables effective workflow model reuse. DWMR is data-centric and addresses issues caused by control flow-based approaches, such as data information loss, cross-paradigm model integration and errorprone problems.

Table 5  
Comparison of model group results.

<table><tr><td>Group no.</td><td>Models</td><td>Average usefulness</td><td>Numbers of nominations</td><td>Rank by experts</td><td>Rank by our approach</td></tr><tr><td>G1</td><td>M1, M2, M3</td><td>5</td><td>5</td><td>1</td><td>1</td></tr><tr><td>G2</td><td>M1, M2</td><td>3.4</td><td>4</td><td>2</td><td>3</td></tr><tr><td>G3</td><td>M2, M3</td><td>3.2</td><td>4</td><td>3</td><td>2</td></tr><tr><td colspan="6">Precision = 100%, recall = 100%</td></tr></table>

Models in bold font are selected by the DWMR approach based on the similalrity scores.

Table 6  
Comparison with control flow-based approaches.

<table><tr><td>Model no.</td><td>Results of human experts</td><td>Results of our approach</td><td>Structure-based similarity</td><td>Content-based similarity</td></tr><tr><td>M1</td><td>Accepted</td><td>Accepted</td><td>0.333</td><td>0.400</td></tr><tr><td>M2</td><td>Accepted</td><td>Accepted</td><td>0</td><td>0</td></tr><tr><td>M3</td><td>Accepted</td><td>Accepted</td><td>0.250</td><td>0.539</td></tr><tr><td>M4</td><td>Rejected</td><td>Rejected</td><td>0</td><td>0</td></tr><tr><td>M5</td><td>Rejected</td><td>Rejected</td><td>0</td><td>0</td></tr><tr><td>M6</td><td>Rejected</td><td>Rejected</td><td>0</td><td>0</td></tr><tr><td>M7</td><td>Accepted</td><td>Rejected</td><td>0</td><td>0.024</td></tr></table>

Models in bold font are selected by the DWMR approach based on the similalrity scores.

We plan to extend this research in two directions. First, we plan to implement a system to facilitate workflow model design based on DWMR approach and conduct a user study to further evaluate our approach. Second, we will look into the semantics of data items and plan to use semantic techniques to enhance model search accuracy and reduce user interventions in the model matching procedure.

## Acknowledgements

The work described in this study was partially supported by grants from National Natural Science Foundation of China (No. 71431002, 71421001, 71461023, 71573030, 71601027), the Fundamental Research Funds for the Central Universities (No. DUT15RC(3)004), and a JPMorgan Chase Fellowship from the Institute for Financial Services Analytics at the University of Delaware.

## References

[1] E.A. Stohr, J.L. Zhao, Workflow automation: overview and research issues, Information Systems Frontiers 3 (2001) 281–296.

[2] I. Vanderfeesten, H.A. Reijers, W.M.P. van der Aalst, Product-based workflow support, Information Systems 36 (2011) 517–535.

[3] I. Vanderfeesten, H.A. Reijers, W.M.P. van der Aalst, Evaluating workflow process designs using cohesion and coupling metrics, Computers in Industry 59 (2008) 420–437.

[4] T. Murata, Petri nets: properties, analysis and applications, Proceedings of the IEEE 77 (1989) 541-580

[5] M. Dumas, A.H.M. ter Hofstede, UML activity diagrams as a workflow specification language, “UML” 2001 — The Unified Modeling Language. Modeling Languages, Concepts, and Tools, Springer, Toronto, Canada 2001, pp. 76–90.

[6] A. Basu, R.W. Blanning, A formal approach to workflow analysis, Information Systems Research 11 (2000) 17–36.

[7] S.X. Sun, J.L. Zhao, J.E. Nunamaker, O.R.L. Sheng, Formulating the data-flow perspective for business process management, Information Systems Research 17 (2006) 374–391.

[8] P. Trkman, The critical success factors of business process management, International Journal of Information Management 30 (2010) 125–134.

[9] D. Cohn, R. Hull, Business artifacts: a data-centric approach to modeling business operations and processes, Bulletin of the IEEE Computer Society Technical Committee on Data Engineering 32 (2009).

[10] H.J. Wang, H. Wu, Supporting process design for e-business via an integrated process repository, Information Technology and Management 12 (2011) 97–109.

[11] J. Mendling, H.M.W. Verbeek, B.F. van Dongen, W.M.P. van der Aalst, G. Neumann, Detection and prediction of errors in EPCs of the SAP reference model, Data & Knowledge Engineering 64 (2008) 312–329.

[12] H. Zha, W.M. van der Aalst, J. Wang, L. Wen, J. Sun, Verifying workflow processes: a transformation-based approach, Software and Systems Modeling 10 (2011) 253–264.

[13] N. Lohmann, E. Verbeek, R. Dijkman, Petri net transformations for business processes — a survey, Lecture Notes in Computer Science, Springer 2009, pp. 46–63.

[14] W.M.P. van der Aalst, The application of petri nets to work ow management, Journal of Circuits, Systems and Computers 8 (1998) 21–66

[15] R. Liu, A. Kumar, An analysis and taxonomy of unstructured workflows, Conference on Business Process Management, Springer 2005, pp. 268–284

[16] J. Claes, I. Vanderfeesten, F. Gailly, P. Grefen, G. Poels, The structured process modeling theory (SPMT) a cognitive view on why and how modelers benefit from structuring the process of process modeling, Information Systems Frontiers 17 (2015) 1401-1425

[17] B. Kiepuszewski, A.H.M. ter Hofstede, C. Bussler, On structured workflow modelling, Conference on Advanced Information Systems Engineering, Springer, Stockholm, Sweden 2000, pp. 431–445.

[18] W.M.P. van der Aalst, A.H.M. ter Hofstede, YAWL: yet another workflow language, Information Systems 30 (2005) 245–275.

[19] K. Jensen, Coloured petri nets and the invariant-method, Theoretical Compute Science 14 (1981) 317-336

[20] B. Berthomieu, M. Diaz, Modeling and verification of time dependent systems using time Petri nets, IEEE Transactions on Software Engineering 17 (1991) 259–273.

[21] J.B. Kam, J.D. Ullman, Global data flow analysis and iterative algorithms, Journal of the ACM 23 (1976) 158–171

[22] U.P. Khedker, Data Flow Analysis, Taylor & Francis, Boca Raton, 2002.

[23] H. Meda, A. Sen, A. Bagchi, Detecting data flow errors in workflows: a systematic graph traversal approach, 17th Workshop on Information Technolgies and Systems, Montreal, Canada, 2007.

[24] S. Sadiq, M. Orlowska, W. Sadiq, C. Foulger, Data flow and validation in workflow modelling, Proceedings of the 15th Australasian Database Conference, Australian Computer Society, Inc., Dunedin, New Zealand 2004, pp. 207–214.

[25] S. Kumaran, R. Liu, F. Wu, On the duality of information-centric and activity-centric models of business processes, Conference on Advanced Information Systems Engineering, Montpellier, France 2008, pp. 32–47.

[26] N. Russell, A.H.M. ter Hofstede, D. Edmond, W.M.P. van der Aalst, Workflow data patterns: identification, representation and tool support, International Conference on Conceptual Modeling, Springer, Klagenfurt, Austria 2005, pp. 353–368.

[27] X.M. Guo, S.X. Sun, D. Vogel, A data flow perspective for business process integration, International Conference on Information Systems, Paris, 2008

[28] J. Hidders, N. Kwasnikowska, J. Sroka, J. Tyszkiewicz, J. Van den Bussche, DFL: a dataflow language based on Petri nets and nested relational calculus, Information Systems 33 (2008) 261–284

[29] D.R. Dolk, B.R. Konsynski, Knowledge representation for model management systems, IEEE Transactions on Software Engineering 10 (1984) 619–628.

[30] R.W. Blanning, Model management systems: an overview, Decision Support Systems 9 (1993) 9–18.

[31] T. Liang, Development of a knowledge-based model management system, Operations Research 36 (1988) 849–863.

[32] D. Hollingsworth, Workflow management coalition: the workflow reference model, Document Number TC00-1003, WFMC, 1995.

[33] J. Puustjärvi, H. Tirri, J. Veijalainen, Reusability and modularity in transactional workflows, Information Systems 22 (1997) 101–120.

[34] H. Zhuge, Component-based workflow systems development, Decision Support Systems 35 (2003) 517–536.

[35] L.H. Thom, J.M. Lau, C. Iochpe, J. Mendling, Extending business process modeling tools with workflow pattern reuse, International Conference on Enterprise Information Systems, Citeseer, Funchal, Madeira — Portugal, 2007.

[36] I. Altintas, A. Birnbaum, K.K. Baldridge, W. Sudholt, M. Miller, C. Amoreira, Y. Potier, B. Ludaescher A framework for the design and reuse of grid workflows Scientific Applications of Grid Computing, Springer, Beijing, China 2004, pp. 120–133.

[37] J. Cao, Y. Mou, J. Wang, S. Zhang, M. Li, A dynamic grid workflow model based on workflow component reuse, Grid and Cooperative Computing, Springer 2005, pp. 424–429.

[38] T. Madhusudan, J.L. Zhao, B. Marshall, A case-based reasoning framework for workflow model management, Data and Knowledge Engineering 50 (2004) 87–115.

[39] H. Zhuge, A process matching approach for flexible workflow process reuse, Information and Software Technology 44 (2002) 445–450.

[40] F. Pittke, H. Leopold, J. Mendling, G. Tamm, Enabling reuse of process models through the detection of similar process parts, in: M. La Rosa, P. Soffer (Eds.), Business Process Management Workshops, Springer, Berlin Heidelberg 2013, pp. 586–597.

[41] W.M.P. van der Aalst, A.H.M. ter Hofstede, B. Kiepuszewski, A. Barros, Work ow patterns. Distributed and Parallel Databases 14 (2003) 5–51.

[42] R. Dijkman, M. Dumas, L. García-Bañuelos, Graph matching algorithms for business process model similarity search, in: U. Dayal, J. Eder, J. Koehler, H. Reijers (Eds.), Business Process Management, Springer, Berlin Heidelberg 2009, pp. 48–63

[43] E.F. Codd, Extending the database relational model to capture more meaning, ACM Transactions on Database Systems 4 (1979) 397 434.

[44] WfMC, Workflow process definition interface — XML process definition language, WFMC-TC-1025, Work ow Management Coalition, 2002.

[45] A. Tversky, Features of similarity, Psychological Review 84 (1977) 327–352.

[46] S.X. Sun, J.L. Zhao, Formal workflow design analytics using data flow modeling, Decision Support Systems 55 (2013) 270–283.

[47] J. Becker, M. Rosemann, C. Uthmann, Guidelines of Business Process Modeling, in: W. Aalst, J. Desel, A. Oberweis (Eds.), Business Process Management, Springer, Berlin Heidelberg 2000, pp. 30–49

Zhiyong Liu is an Assistant Professor at the Institute of Information Management and Information Systems, Faculty of Management and Economics, Dalian University of Technology, China. He received PhD from a joint program of the University of Science and Technology of China (USTC) and City University of Hong Kong (CityU), in 2014. His research interests include business process management, workflow modeling, data flow analysis, particularly in the context of e-commerce and e-finance.

Shaokun Fan is an Assistant Professor in Business Information Systems, College of Business, Oregon State University. He received his PhD degree from the University of Arizona and M S degree and BS degree from Nanjing University China, His research interests involve business process management and data science. He has published research articles in journals such as Decision Support Systems Data & Knowledge Engineering, and Information Systems Frontiers

Harry Jiannan Wang is an Associate Professor of Management Information Systems (MIS) and JPMorgan Chase Fellow in the Lerner College of Business and Economics at the University of Delaware. He received Ph.D. in Management Information Systems (MIS) from the Eller College of Management at the University of Arizona, USA and B.S. in MIS from Tianjin University, China. His research interests involve business process management, business intelligence and analytics, and enterprise systems. He has published research articles in journals, such as Information Systems Research, Decision Support Systems, ACM Transactions on Management Information Systems, and Information and Management. Dr. Wang has served as associate editor, special issue guest editor, and editorial board member for several journals and organized the 2014 Workshop on business Processes and Service and the 2013 China Summer Workshop on Information Management as a conference co-char. He has also been a program co-chair, program committee member, and track co-chair for numerous conferences.

J. Leon Zhao is Chair Professor in Information Systems and was Head of Information Systems (2009 - 2015), College of Business, City University of Hong Kong. He was Interim Head (2006-2007) and Eller Professor in MIS, University of Arizona. He also taught at HKUST and College of William and Mary previously. He holds Ph.D. from Haas School of

Business, UC Berkeley. His research is on information technology and management with a particular focus on risk management, collaboration and workflow management, and information services for business and finance. His current interests include big data, blockchain, social networks, and FinTech. He is director of Center on Global Internet Finance and Lab on Enterprise Process Innovation and Computing. He has published over 200 academic papers in conferences and journals and held various editorships in several academic journals and chairpersonships in numerous conferences. He received IBM Faculty Award in 2005 and was awarded Chang Jiang Scholar Chair Professorship at Tsinghua University in 2009.
