---
otero_id: 16330
otero_key: "MPCF8DMJ"
title: "Minimizing the data quality problem of information systems: A process-based method"
authors: "Qi Liu; Gengzhong Feng; Xi Zhao; Wenlong Wang"
year: "2020"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2020.113381"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Minimizing the data quality problem of information systems: A processbased method

![](/api/attachments/MPCF8DMJ/fulltext/images/f3634f5b6f14b3fa15498ced7bd2f4fa96ac7532049ab35af976301c469fbe01.jpg)

Qi Liu<sup>a,b</sup>, Gengzhong Feng<sup>a,b,⁎</sup>, Xi Zhao<sup>a,b</sup>, Wenlong Wang

<sup>a</sup> School of Management, Xi'an Jiaotong University, NO. 28 Xianning Road, Xi'an Shaanxi, 710049, China

<sup>b</sup> The Key Lab of the Ministry of Education for Process Control and Eficiency Engineering, NO. 28 Xianning Road, Xi'an Shaanxi 710049, China]

<sup>c</sup> School of Management, Xi'an University of Architecture and Technology, NO. 13 Yanta Road, Xi'an Shaanxi 710055, China

## A R T I C L E I N F O

Keywords: Data quality Information system Petri net Optimization model Process mode

## A B S T R A C T

The low quality of data in information systems poses enormous risks to business operations and decision making. In this paper, a single-period resource allocation problem for controlling the information system's data quality problem is considered. We develop a Data-Quality-Petri net to capture the process through which data quality problem generates, propagates, and accumulates in the information system. The net considers not only the factors leading to the production of the data quality problem by the data operation nodes and the data flow structure, but also the data transfer ratio of the nodes. Then, we propose a nonlinear programming optimization model with control resource constraints. The result of the model provides an optimal strategy to allocate resources for minimizing the expected data quality problem of an information system. Further, we examine the impact of the data flow structure on optimal resource allocation. The result shows that the optimal resource input level for a data operation node is proportional to its potential for downstream propagation. A warehouse management system of an e-commerce company is utilized to illustrate the model. Our study provides a method for data managers to control the information system's data quality problem by employing a process perspective.

## 1. Introduction

Companies build information systems to facilitate their routine work; more importantly, the information systems record a large amount of data, such as consumer and product data, about companies' opera tions [1,2]. The survey conducted by Experian [3] indicated that more than half of the companies believe that data will prove to be a vital source of business opportunity in the near future. However, data quality problems impede companies from obtaining the best value from data [4]. The terms data quality have been used to characterize the mismatches between the view of the world provided by an information system and the reality of the world [5]. Prior studies often adopt three types of data errors: inaccuracy, incompleteness, and mismembership as the neglect indicators to reflect the data quality in the field of information systems [5,6]. We define these three types of data errors as data quality problems in this paper. The ubiquitous data quality problems pose a considerable risk (e.g., monetary loss, operational ineficiencies) for companies that make decisions based on data [7,8]. Gartner's 2017 survey showed that poor data quality was responsible for an average annual loss of USD 15 million [9]. However, improving the data quality of information systems requires a substantial investment in human and material resources; out of the 160 CIOs surveyed, 75% believed that controlling the data quality problem is costly for enterprises [10]. Therefore, how to eficiently control the data quality problem of the information system is a key issue worth studying.

Although there is extensive research on the management of data quality in information systems, scholars have seldom studied how to rationally allocate limited resources (e.g., human beings or equipment) to achieve the purpose of optimizing the data quality of information systems. In this paper, we propose a data quality optimization model to identify the optimal control strategy that minimizes the data quality problem under resource constraints. This model includes two improvements over the previous research [8,11]. First, the model constructs a Data-Quality-Petri (DQ-Petri) net to assess the data quality problem of an information system. Based on the Petri net, the DQ-Petri net introduces two new parameters, namely the data quality problem produced by the data operation nodes and the data transfer ratio of the nodes. The data transfer ratio of a node denotes the ratio of the amount of data transferred from the node to its downstream node and the amount of data received by its downstream node per unit time. It reflects the proportion of data transferred by the node. The DQ-Petri net makes the quantification of the propagation and accumulation of the data quality problem possible and improves the rationality of resource allocation. Second, the model takes the overall data quality problem of an information system as the optimization goal that can be objectively quantified. The result generated by the model provides process-based control support for enterprises to carry out the data quality management of information systems.

![](/api/attachments/MPCF8DMJ/fulltext/images/1aac338a2f88826752d461ac9c84a085f748a0a8cd79fc2786d63db1de27ed44.jpg)  
Fig. 1. Data flow in WMS of an e-commerce company.

The remainder of the paper is organized as follows. Section 2 reviews the literature. Section 3 uses a warehouse management system (WMS) of an e-commerce company as an illustrative example to introduce the research problem. Section 4 develops a process-based model to manage the data quality of an information system. Section 5 studies the impact of data flow structures on optimal resource alloca tion. Section 6 applies the model to a WMS and discusses the results. Conclusions are presented in section 7.

## 2. Literature review

Some scholars have recognized that data is a product, and an in formation system is a type of product manufacturing system [12,13], which mainly emphasizes that the idea and method of product quality management can be tried to manage data quality. Our work attempts to use the opinion of process-based product quality management to control the data quality of the information system.

## 2.1. Data quality

Data quality research has developed rapidly in the past ten years and has become a hot research topic. The early definition of data quality is limited to accuracy [14]. Wang and Strong [15] analyzed the perspective of data users to study data quality and summarized more than 100 properties of data quality into four categories that include accuracy, relevancy, representation and accessibility. Tayi and Ballou [16] suggested that the selection of data quality dimensions should be adapted to local conditions. In this study, we adopt the following three data quality dimensions that are commonly used in the information systems field: inaccuracy, incompleteness and mismembership [5,17]. The main reason for choosing these three is that they are essential data quality indicators of information systems and could be measured in an objective manner [6].

## 2.2. Process management

Process-based modeling is a method for constructing explanatory models of dynamical systems from knowledge and data [18]. For example, the Petri net was applied in the modeling of discrete manufacturing systems and risk assessment [19,20]. Business process mode and notation (BPMN) was developed as a standard for modeling business processes [21]. Data Flow Diagram (DFD) graphically expresses the logical flow of data within the system and the logical transformation process from the perspective of data transfer and processing [22]. Based on the Petri net, the DQ-Petri net is developed in our work to model the propagation and accumulation of the data quality problem in information systems.

## 2.3. Data quality improvement in information systems

Research on data quality improvement of information systems could be divided into two streams according to the strategies employed. The first uses the data-driven improvement strategy that replaces lowquality values with high-quality values by particular means or methods. For example, Du and Zhou [23] proposed an ontology-based framework to solve data inconsistency problems in online financial data. Liu, Feng, Wang and Tayi [24] introduced data-mining technology to enhance data quality. Xu, Lei and Li [25] proposed an incorrect data detection method based on an improved local outlier factor to improve data quality.

Another improvement strategy is process-driven and is used to control and improve the data process. For example, Shankaranarayan, Ziad, Wang and Siau [26] proposed an Information Product Map (IP-MAP) method that emphasizes the management of data quality in the data process. Bai, Nunez and Kalagnanam [10] proposed a method for managing data quality risk in accounting information systems by analyzing the flow of accounting information systems. Song, Sun, Wan and Liang [11] built a two-stage model with local and global optimization of data quality as the constraints and cost as the goal. Our work develops a process-based optimization model that considers the impact of data flow and the data transferred ratio by the data operation node on the accumulation of data quality problems. The model aims to provide optimal resource allocation strategies to improve data operation behavior in the data flow to achieve the purpose of optimizing the data quality of information systems.

## 3. Problem description

In this section, we choose a WMS of an e-commerce company as an illustrative example to introduce our research problem. Fig. 1 presents the data flow in the WMS by using IP-MAP.

## 3.1. Data operation nodes

As shown in Fig. 1, this information system is initiated by the following four main businesses related to it: sale, procurement, replen ishment and inventory. Businesses generate new data daily; this is finally stored in a database through a series of data operation nodes (e.g., add/query order information and add customer information). Data operation nodes are called ‘node’ or ‘nodes’ for short in the following sections. The links between these nodes represent the flow of data.

## 3.2. Sources of the data quality problem

In the absence of data error, the data stored in the WMS database accurately reflect the information of the real entity. However, the negligent work, omissions, and fraudulent behavior of system users or outdated software design may lead to data error at each node. In other words, the node adds the data quality problem. Then the data quality problem may afect downstream nodes in the information system and are eventually stored in the database. For example, if the system user fills purchase quantity incorrectly in the node of ‘Add/Query order information’, the order with wrong purchase quantity information might lead to downstream mismatched inventory inspection in the node of ‘Adequate inventory check’ and would be finally stored in the database.

We adopt the following three error types that are most commonly used in information systems literature: inaccuracy, incompleteness and mismembership $[ 6 , 1 7 ]$ . Inaccuracy occurs when any one attribute of the tuple is not an accurate representation of the corresponding real-world value. Incompleteness occurs when the tuple that should exist in the system is dropped. Mismembership occurs when the tuple that should not exist in the system is recorded. Meanwhile, we refer to them as in stances of data quality problems in this paper.

## 3.3. Assessment procedure

Data quality assessment refers to comparing the measured value of the data with the reference value for quality diagnosis [27]. In our study, the purpose of the assessment procedure is not only to calculate the error rates $( \mathrm { i . e . } ,$ , inaccuracy, incompleteness and mismembership) produced by each node, but also to evaluate the propagation and accumulation of the error rates in the information system. Through the assessment procedure, managers could clear the influence of each node on the data quality problem of the information system, which assists managers in executing the control procedure.

## 3.4. Control procedure

The data manager selects the appropriate node for data quality control according to the data quality assessment result. This process is called the control procedure. Control procedures are considered an improvement in the behavior of nodes by investing in specific resources (human or material). As in the previous study [7,10], we only consider controls that directly reduce the number of error incidences introduced by the nodes. Examples include reviewing data collection and adding data acquisition equipment. In general, resource input of data quality is the basis for implementing the data quality control procedure. The number of resources invested and control eficiency will commonly afect the results of the improvement.

## 3.5. Optimal control strategy

Managers need to ensure that the cost of data quality control is within a range acceptable to the organization, and this decision will depend on the organization's existing resources. It means that organizations are looking to implement appropriate resource allocation strategies in their budgets to reduce data quality problems. The optimal control strategy is to achieve the goal of optimizing the data quality of an information system by rationally allocating resources under resource constraints. It needs to weigh the costs and benefits of alternative allocations [8]. For example, the organization must decide whether to allocate people to check order work or assist in inventory checks? In the next section, we model the problem.

## 4. The model

In this section, we first develop a DQ-Petri net to capture the data quality problem propagation and accumulation in the information system. Based on the net, we further propose an optimization model to generate the optimal control strategy. In this paper, a single period decision problem is considered. To quantify the data quality, we will use the probability of data quality problems to reflect the status of data quality. That is, we will design the model with the goal of minimizing the probability of data quality problems of information system.

4.1. Modeling the data quality problem propagation and accumulation in an information system

Based on the Petri net, we propose the DQ-Petri net by introducing the related factors of data quality problems.

Definition 1. (DQ-PETRI NET) A DQ-Petri net consists of four-element $\{ P , T , F , O \}$ , in which

$P = \{ P _ { 1 } , P _ { 2 } , \cdots , P _ { n } \}$ represents the data operation node in the in formation system;

$T = \{ t _ { i , i + 1 } \} , i = 1 , 2 ,$ ⋯ is a finite non-empty transition set used to describe the process of data quality problem propagation;

$F \subseteq ( P \times T ) \cup ( T \times P )$ is a set of directed arcs, indicating the flow direction of the data;

O denotes the starting point of the initiated functional requirements, represented by a hollow circle.

In general, the data flow in an information system consists of the three net structures shown in Fig. 2 below. Generally, any kind of net can be formed from these three basic nets.

## 4.1.1. The data quality problem and transition probability

Each transition $t _ { i , i + 1 }$ consists of two key parameters: ${ L _ { i } } ^ { k }$ and $p _ { i , j } . L _ { i } ^ { k }$ represents the $k ^ { \mathrm { { t h } } }$ dimension of data quality problem generated by the $i ^ { \mathrm { { t h } } }$ node. $k = 1 , 2 ,$ , and 3 correspond to inaccuracy, incompleteness and mismembership, respectively. We suppose that it obeys a $e _ { i , \mathrm { ~ } }$ probabilistic distribution, that ${ \mathrm { i } } s ,$ if the probability of the $k ^ { \mathrm { t h } }$ dimension of the data quality problem caused by the $i ^ { \mathrm { { t h } } }$ node is 20%, then $e _ { i , \ k } = 2 0 \%$ Next, we will show how to quantify these three dimensions.

Consider a conceptual relation T consisting of all the relevant objects from the real world without any error and a relation S is the realistic record of T. If there are no errors, then $s \ = \ T .$ . However, in reality, S may contain some errors. Tuples in T belong to three categories as follows: $T _ { A } ,$ the set of instances in T that are correctly captured into $S ; T _ { I } ,$ the set of instances in T that are captured into S, but one or more of their non-identifying attribute values are inaccurate or null; and $T _ { C } ,$ the set of instances in T that have not been captured into S and therefore form the incomplete dataset for S. Moreover, S may contain a mismember set $S _ { M }$ that does not have corresponding instances in T. To sum up, $| T | ~ = ~ | ~ S ~ | ~ + ~ | ~ T _ { C } ~ | ~ - ~ | ~ S _ { M } | .$ , where ∣X∣ refers to the size of relation X.

![](/api/attachments/MPCF8DMJ/fulltext/images/f2176b1fc6712f63d071ed7afa93c3a4c859211136dd3d0781239465522664a2.jpg)  
Fig. 2. Basic net structures.

Inaccuracy o $^ { \cdot } s ,$ measured as $\beta _ { S } = \ | \ T _ { I } | / | \ S |$ , is the probability that a tuple in S is inaccurate.

Incompleteness of $^ { \cdot } s ,$ , measured as $\chi _ { S } = \mid T _ { C } \mid / ( \mid S \mid ~ - ~ \mid S _ { M } \mid ~ + ~ \mid T _ { C } \mid ) _ { \ L }$ , is the probability that an entity instance in the real world is not cap tured in S.

Mismembership of $s ,$ measured as $\mu _ { S } = \mid S _ { M } \mid / \mid S \mid$ ，is the probability that a tuple in S is a mismember.

The method to calculate the actual values of these metrics could be found in [5]. On this basis, the value of ${ L _ { i } } ^ { k }$ can be obtained by com paring the changes in data quality problems before and after the $i ^ { \mathrm { { t h } } }$ node.

The second parameter $p _ { i , j }$ denotes the ratio of the amount of data transfer from the $i ^ { \mathrm { { t h } } }$ node to the $j ^ { \mathrm { t h } }$ node per unit time and the amount of data received by the node j per unit time. $p _ { i , j } = N _ { i , j } / I N _ { j } ,$ where $N _ { i , ~ j }$ denotes the amount of data transfer from the $i ^ { \mathrm { t h } }$ node to the $j ^ { \mathrm { t h } }$ node per unit time, and $I N _ { j }$ represents the amount of data obtained by the $j ^ { \mathrm { t h } }$ node per unit time. The unit time can be a day, week, month, or year. In this paper, we refer to it as the data transfer ratio.

4.1.2. The influence of data flow structures on the propagation of the data quality problem

This section will examine the impact of diferent data flow struc tures on the propagation and accumulation of the data quality problem. Definition 2. Let $\boldsymbol { D Q P _ { i , \ j } } ^ { k }$ be the $k ^ { \mathrm { t h } }$ dimension of the data quality problem propagation from the $i ^ { \mathrm { { t h } } }$ node to the $j ^ { \mathrm { t h } }$ node.

Next, we will analyze the impact of diferent data flows structure (see Fig. 2) on $D Q P _ { i , j } \stackrel { \bar { k } } { }$

Proposition 1. For the sequence structure, $D Q P _ { 1 , n } { } ^ { k } i s$ as follows,

$$
D Q P _ {1, n} ^ {k} = \sum_ {j = 1} ^ {n - 1} \left(L _ {j} ^ {k} \times \prod_ {r = j} ^ {n - 1} p _ {r, r + 1}\right)\tag{1}
$$

Proposition 1 shows that, for the given sequence structure and assuming that the data quality problem caused by each node is the same $( \mathrm { i . e . , ~ } \bar { L _ { j } ^ { k } } = L , \forall j = \bar { 1 } , . . . , \bar { n } )$ , the data quality problem caused by the upstream node has a greater impact on the downstream node when the upstream node is closer to the downstream node. For example, the downstream node n receives the data quality problem produced by the $( j \mathrm { ~ + ~ } 1 ) ^ { \mathrm { t h } }$ node $( \mathrm { i . e . , ~ } L _ { j + 1 } ^ { k } \times \prod _ { r = j + 1 } ^ { n - 1 } p _ { r , r + 1 } )$ is not smaller than the $j ^ { \mathrm { t h } }$ node $( \mathrm { i . e . , \ } L _ { j } ^ { k } \times \prod _ { r = j } ^ { n - 1 } p _ { r , r + 1 } )$ because $p _ { r , \ r + 1 } \ \leq \ 1 , \forall \ r .$ Next, we will use up stream and downstream to describe the order of nodes in the data flow. If there is no other node between the two nodes, the upstream node can be considered as the input node of the downstream node, while the downstream node can be considered as the output node of the upstream node.

Proposition 2. For the split structure, let F be the set of the downstream nodes, $D Q P _ { 1 , ~ F } { } ^ { k } i s$ as follows:

$$
D Q P _ {1, F} ^ {k} = \sum_ {f \in F} (L _ {1} ^ {k} \times p _ {1, f})\tag{2}
$$

Proposition 2 shows that, for the split structure, the more branches a node passes through (i.e., the larger the set $\mathbf { F } ) ,$ the greater the data quality problem it propagates.

Proposition 3. For the join structure, let U be the set of upstream nodes， $D Q P _ { U , \ n } { } ^ { k }$ is as follows:

$$
D Q P _ {U, n} ^ {k} = \sum_ {u \in U} (L _ {u} ^ {k} \times p _ {u, n})\tag{3}
$$

Proposition 3 shows that, for the joint structure, the total data quality problem received by the downstream node is the weighted sum of the data quality problem caused by the upstream nodes. Note that $\sum _ { \nu = \tau \tau } p _ { u , n } = \sum _ { \nu = \tau \tau } ( N _ { u , n } / N _ { n } ) , N _ { n }$ consists of $N _ { u , \ n } , \ s o \ p _ { u , \ n } ( \forall u )$ affect each u U u U other and are not independent. In special circumstance, when $N _ { n } = \sum _ { u \in U } N _ { u , n } \ , \ \sum _ { u \in U } p _ { u , n } = 1$ . Therefore, the data quality problem received by the downstream node is not proportional to the number of upstream branches. This result is diferent from the outcome seen in the split structure.

4.1.3. Accumulation of the data quality problem in the information system Based on the above findings, this section will explore the accumulation of the data quality problem in information systems.

1) The accumulation of the data quality problem generated by nodes in the information system

This section will study the accumulation of the data quality problem in the information system. Let $D Q P _ { i } ^ { k }$ denotes the cumulative result of the $k ^ { \mathrm { { t h } } }$ dimension of the data quality problem generated by the $i ^ { \mathrm { { t h } } }$ node in information system; $D Q P _ { i } ^ { k }$ is given as follows:

Proposition 4. Suppose the number of the data flows between the $i ^ { t h }$ node and the database is m and each data stream has ${ n _ { l } } ( l = 1 , 2 , . . . , m )$ nodes. Then, for any one net structure of information system,

$$
D Q P _ {i} ^ {k} = \sum_ {l = 1} ^ {m} \left(L _ {i} ^ {k} \times \prod_ {j = 1} ^ {n _ {l} - 1} p _ {j, j + 1} ^ {i, l}\right)\tag{4}
$$

where $p _ { j , j + 1 } { } ^ { i , l }$ denotes the ratio of data transfer per unit time between the upstream and downstream nodes $( j a n d j + 1 )$ on the $l ^ { t h }$ data stream of the $i ^ { \stackrel { \star } { t h } }$ node. We define the sum of the data transfer ratio products on each data stream between the node and the database $( \mathrm { i . e . , ~ } \sum _ { l = 1 } ^ { m } \prod _ { j = 1 } ^ { n _ { l } - 1 } p _ { j , j + 1 } ^ { i , l } )$ as the potential for downstream propagation $o f$ the $i ^ { \mathrm { { t h } } }$ node. The greater the value of $D Q P _ { i } ^ { k }$ , the greater the impact on the data quality of the information system on which the data manager needs to focus. According to $\operatorname { E q . } ( 1 )$ and $\operatorname { E q . } ( 4 )$ , we can infer that $D Q P _ { i } ^ { k } \ = \ D Q P _ { i }$ ${ _ { D B } } ^ { k } \mathrm { ~ - ~ } D Q P _ { i + 1 , D B } { ^ k }$ , where DB represents the database of the information system. This shows that the impact of the data quality problem generated by a node on the data quality of information system is independent of the previous process of this node; that ${ \mathrm { i } } s ,$ the problem caused by node has no afterefect.

2) Accumulation of the overall data quality problem in the information system

We use $D Q P { \mathrm { - a } }$ negative indicator of the data quality of information system—to denote the accumulation of the overall data quality problem in the information system. Then, $D Q P$ is given as follows:

$$
D Q P = \sum_ {i, k} D Q P _ {i} ^ {k}\tag{5}
$$

## 4.2. Modeling control procedures

To study clearly the resources acquired by diferent nodes, we let the resource input to a node be a variable $x _ { i , \ k } ( 0 \leq x _ { i , \ k } \leq 1 )$ , which denotes the input level of the control resource at the $i ^ { \mathrm { { t h } } }$ node for the $k ^ { \mathrm { { t h } } }$ dimension of the data quality problem and is the decision variable of the optimization model. It is the ratio of the actual number of humans and equipment involved in the control procedures to the total number of humans and equipment available. In particular, when no control resource is applied to the $i ^ { \mathrm { { t h } } }$ node for the $k ^ { \mathrm { { t h } } }$ dimension of the data quality problem, $x _ { i , \ k } = 0 ;$ when all available control resources are applied to the $i ^ { \mathrm { { t h } } }$ node for the $k ^ { \mathrm { { t h } } }$ dimension of the data quality problem, then $x _ { i , \ k } = \ 1$ . For an information system, the sum of the resources invested in all nodes cannot exceed the total resources; thus, $\Sigma _ { i , \ k } x _  i , $ $\kappa \leq 1$

Control efectiveness refers to the reduction ratio in the data quality problem produced by the nodes after executing the control procedure. If the control procedure is applied after the assessment procedure, the data quality problem may be reduced. For example, when the inaccuracy generated by a node is 20%, and the efectiveness of the application control on the node is 50%, then the resulting inaccuracy is 10%. We denote the efectiveness of a control procedure on the $k ^ { \mathrm { { t h } } }$ dimension of the data quality problem for $i ^ { \mathrm { { t h } } }$ node as $\eta _ { i , k } ; 0 \le \eta _ { i , k } \le 1 _ { : }$ ∀i, k denotes the proportion of the data quality improved by the procedure. In this paper, we assume that the efectiveness of a control procedure is independent of the efectiveness of any other control procedure. As diferent nodes have diverse ways of controlling and diferent levels of efectiveness, despite being located at the same control resource, we choose $\eta _ { i , \mathrm { ~ } }$ to be a Cobb-Douglas function of the input level of control resources; the function can be either concave or convex, depending on the application context:

$$
\eta_ {i, k} (x _ {i, k}) = g _ {i, k} x _ {i, k} ^ {\tau_ {i, k}}, \tau_ {i, k} > 0\tag{6}
$$

where the control eficiency range is [0,1]; the parameter $g _ { i , k }$ reflects a positive correlation between control resources and control eficiency; and $0 \leq g _ { i , k } \leq 1$ . The exponent $\tau _ { i , \ k }$ measures the efectiveness elasticity of control and $\tau _ { i . \ k } \ > \ 0$ . The Douglas function is suitable for the eficiency function setting because it has the following characteristics. First, $\eta _ { i , \ I }$ and $x _ { i , \ast }$ correspond one-to-one in the domain [0,1]. Second, the parameter $\tau _ { i , \ k } \mathrm { ~ c a n ~ }$ change the concavity and convexity, which, in turn, makes the eficiency function capture reality accurately. When

$0 ~ < ~ \tau _ { i . ~ k } ~ < ~ 1$ , the control eficiency $\eta _ { i , \ k }$ is a concave function. As the control resources increase, the marginal utility gradually decreases. When $\tau _ { i . k } = 1 , \eta _ { i , i }$ is a linear function. When $\tau _ { i . k } > 1 , \eta _ { i , }$ <sub>k</sub> is a convex function. As control resources increase, the marginal utility gradually increases.

## 4.3. Modeling the data quality problem of the information system

In this paper, the data quality problem of the information system is adopted as the target of data quality control in the information system. The total data quality problem of the information system is created by the accumulation of the data quality problem in the information system. Therefore, the mean of the information system's data quality problem can be written as:

$$
\operatorname{E} (D Q P) = \sum_ {i, k, l} \left(e _ {i, k} \times \prod_ {j = 1} ^ {n _ {l} - 1} p _ {j, j + 1} ^ {i, l}\right)\tag{7}
$$

where i represents the sequence number of the data operation node; k represents the data quality dimension; l is the number of the data stream between each node and the database; $e _ { i , \ k }$ denotes the prob ability of the $k ^ { \mathrm { { t h } } }$ dimension of the data quality problem caused by the $i ^ { \mathrm { { t h } } }$ node; and $\prod _ { i = 1 } ^ { n _ { l } - 1 } p _ { j , j + 1 } ^ { i , l }$ denotes the data transfer proportional product of the $i ^ { \mathrm { { t h } } }$ node on the $l ^ { \mathrm { t h } }$ data stream.

After the control procedures are executed, the data quality problem generated by the nodes in the information system can be reduced. The mean of the total data quality problem of the post-control information system is expressed as follows:

$$
\mathrm{E} (D Q P (x _ {i, k})) = \sum_ {i, k, l} \left(e _ {i, k} \times (1 - \mathsf {g} _ {i, k} x _ {i, k} ^ {\tau_ {i, k}}) \times \prod_ {j = 1} ^ {n _ {l} - 1} p _ {j, j + 1} ^ {i, l}\right),\tag{8}
$$

where $e _ { i , \ k } \times \ ( 1 \ - \ g _ { i , \ k } x _ { i , \ k } \tau _ { i , \ k } )$ represents the probability of the $k ^ { \mathrm { { t h } } }$ dimension of the data quality problem generated by the $i ^ { \mathrm { t h } }$ node after control.

## 4.4. Problem formulation

According to the above description, the optimization model takes the input level of the control resource $x _ { i , \textit { k } }$ as the decision variable, and minimizes the data quality problem of the information system as the objective function, while taking the enterprise's existing resources as the constraint condition. The model is given as follows:

$$
\underset {x} {\text {Min}} \quad \sum_ {i, k, l} \left(e _ {i, k} \times (1 - \mathrm{g} _ {i, k} x _ {i, k} ^ {\tau_ {i, k}}) \times \prod_ {j = 1} ^ {n _ {l} - 1} p _ {j, j + 1} ^ {i, l}\right)
$$

s.t.

$$
\sum_ {i, k} x _ {i, k} \leq 1\tag{9}
$$

$$
0 \leq x _ {i, k} \leq 1, \quad \forall i, k\tag{10}
$$

(11)

$$
0 \leq g _ {i, k} \leq 1, \quad \forall i, k\tag{12}
$$

$$
\tau_ {i. k} > 0, \quad \forall i, k\tag{13}
$$

$$
0 \leq p _ {j, j + 1} ^ {i, l} \leq 1, \quad \forall i, j, l\tag{14}
$$

$$
i = 1, 2, \dots ; j = 1, 2, \dots ; l = 1, 2, \dots ; k = 1, 2, 3\tag{15}
$$

Eq. (9) refers to the objective function of the model, which is the mean of the data quality problem of the information system. Eq. (10) shows that the total amount of input of control resources needs to be less than the total resources. Eq. (11) means that the resource allocation in each dimension is neither more than one nor less than zero. Eq. (12) reflects the range of the positive correlation of the ratio of control efficiency and resources. Eq. (13) reflects the fact that control resources are positively correlated with control eficiency. Eq. (14) represents the fact that the data transfer ratio is in the range [0,1].

## 5. The impact of data flow structures on optimal control resources allocation

In this section, we investigate the impact of the data flow structures on optimal control allocation. To focus on the structural factor, we set the data quality problem caused by each node and the parameters in the control eficiency function that are not related to the data flow structure to be the same (i.e., ${ L _ { i } } ^ { k } = L , { \eta } _ { i , \ k } = \eta$ and $\tau _ { i , \ k } = \tau , \forall \ i , \ k )$

Proposition 5. For an arbitrary process structure, the optimal input level of the control resources for the $i ^ { t ^ { h } }$ node that minimizes the expected data quality problem is proportional to the potential for downstream propagation of the i<sup>th</sup>node:

$$
x _ {i} ^ {*} \propto \sum_ {l} ^ {m} \prod_ {j = 1} ^ {n _ {l} - 1} p _ {j, j + 1} ^ {i, l}
$$

Proposition 5 reflects the fact that under the optimal control strategy, the control resource acquired by the node is proportional to the sum of the data transfer ratio products on each data stream between the node and the database. The larger the value, the greater the impact of the node on the data quality of the information system. Therefore, when the data manager undertakes control resource configuration, it is necessary to pay attention to the nodes with many downstream bran ches and those that have a large data transfer ratio.

Next, we investigate the efect of the basic structures shown in Fig. 2. For a sequence structure and any node i and its downstream node $( i ~ + ~ s )$ (s is a positive integer greater than zero).

Corollary 1. For a sequence structure flow, holding all other parameters the same, the ratio of the optimal control resources input between the $i ^ { t h }$ and the $( i ~ + ~ s ) ^ { \mathrm { t h } }$ nodes that minimizes the expected data quality problem is as follows:

$$
\frac {x _ {i} ^ {*}}{x _ {i + s} ^ {*}} = \left(\prod_ {i} ^ {i + s - 1} p _ {i, i + 1}\right) ^ {\frac {1}{1 - \tau}}, \forall i, s.
$$

Resource allocation ratio of the two nodes $( x _ { i } ^ { * } / { x _ { i + s } } ^ { * } )$ reflects the relative importance of node i and its downstream node $( i ~ + ~ s )$ to the data quality of the information system. It can be seen that the value of this ratio is related to the unit time data transfer proportional product between the $i ^ { \mathrm { { t h } } }$ node to the $( i + s ) ^ { \mathrm { t h } }$ node and the elastic coeficient (τ) of the control resource. Specially, when the marginal utility of control is decremented $( \mathrm { i } . \mathbf { e } . , \tau \ < \ 1 )$ , the optimal control strategy is to configure more resources in the downstream node $( \mathrm { i . e . , } x _ { i } ^ { \ast } \leq x _ { i + 1 } ^ { } ^ { \ast } )$ . The reason for this result is that we assume that the data quality problem caused by each node is independent of that caused by others. Under the as sumption that each node causes the same problem, the number of records with the data quality problem caused by the downstream node is not less than the upstream node (because the downstream node may create new data). Therefore, the downstream node requires more con trol resources to correct records with quality issues.

When the information system has a ‘1-n’ data flow structure for the upstream node 1 and the downstream nodes set F, the optimal resource allocation ratio exists for the purpose of minimizing the data quality problem of information system has the following characteristics.

Corollary 2. For a split structure flow, holding all other parameters the same, the ratio of the optimal control resources input between the upstream node 1 and the downstream node set F that minimizes the expected data quality problem is as follows:

$$
\frac {x _ {1} ^ {*}}{x _ {F} ^ {*}} = \left(\frac {\sum_ {f \in F} p _ {1 , f} \cdot p _ {f , \mathrm{DB}}}{\sum_ {f \in F} p _ {f , \mathrm{DB}}}\right) ^ {\frac {1}{1 - \tau}},
$$

where $p _ { 1 , }$ denotes the proportion of data that is transmitted per unit time by the $i ^ { t h }$ node to the downstream nodes set $F ,$ and $p _ { f , D B }$ denotes the proportion of data that is transmitted per unit time by the $f ^ { t h }$ node to the database represented by ‘DB’. In particular, when the marginal utility of control is decremented $( \mathsf { i . e . , } \tau \ < \ 1 )$ , under the optimal control strategy, the total number of resource configurations of the downstream nodes set F should be no less than its upstream node $1 \ ( \mathrm { i . e . , } \ x _ { 1 } ^ { \ * } \ \leq \ x _ { F } ^ { \ * } )$

When the information system has the $\cdot _ { n - 1 } \cdot$ data flow structure for the upstream nodes set U and the downstream node n, the optimal resource allocation ratio has the following characteristics under the goal of minimizing the data quality problem of information system.

Corollary 3. For a join structure flow, holding all other parameters the same, the ratio of the optimal control resources input between the upstream nodes set U and the downstream node n that minimizes the expected data quality problem is as follows,

$$
\frac {x _ {U} ^ {*}}{x _ {n} ^ {*}} = \left(\sum_ {u \in U} p _ {u, n}\right) ^ {\frac {1}{1 - \tau}}
$$

The resource allocation ratio $( { x _ { U } } ^ { * } / { x _ { n } } ^ { * } )$ of the upstream nodes set U and the downstream node n reflects the relative importance of the nodes set U and its downstream node n to the data quality problem of an information system. In particular, when the marginal utility of control is decremented $( \mathsf { i } . \mathsf { e } . , \tau \ : < \ : 1 )$ , under the optimal control strategy, the total number of resource configurations of the downstream node n should be no less than those in its upstream nodes set $U ( { \mathrm { i . e . , } } x _ { U } { } ^ { * } \leq x _ { n } { } ^ { * } )$

## 6. Case study

In this section, we validate our model by using the data from a WMS of an e-commerce company. Fig. 1 shows the detailed data flow of the system. Applying the model to guide resources allocation involves the following steps:

Step 1. Construction of the DQ-Petri net of the information system. The data manager needs first to clarify the data operations in the information system, as well as the data flow, and then develop the corresponding DQ-Petri net.

Step 2. Determination of the DQ-Petri net parameters, including $e _ { i , \astrosun }$ k generated by each node and the data transfer ratio $p _ { i , j } .$

Step 3. Data quality assessment of information system. Based on the DQ-Petri net, the propagation and accumulation of the data quality problem in the information system are evaluated.

Step 4. Control eficiency assessment. Identify control measures and possession of control resources, and assess the eficiency of data quality control on each node through internal control logs and external audit reports.

Step 5. Applying the model to obtain the optimization result. Input the corresponding data and the constructed model data into the MATLAB software, and get the solution of the model, that is, the optimal resource allocation strategy.

Next, we illustrate the application process with a specific case.

## 6.1. Related Data

Based on the data flow of the WMS shown in Fig. 1, the DQ-Petri net is drawn as shown in Fig. 3. We choose the hollow circle as the starting point to represent the four main processes: sale, procurement, replenishment and inventory. Meanwhile, each data operation in Fig. 1 is represented by $\mathrm { { P _ { i } } }$ in the DQ-Petri net. The correspondence is shown in

Table 1  
![](/api/attachments/MPCF8DMJ/fulltext/images/0c7580478cc0ceb290a65809bb0d6a06a1aaad2940635a5381fd40abd5f7e55b.jpg)  
Fig. 3. DQ-petri net of the WMS.

Table 1. To keep the figure simple, we omit the representation of the relevant parameters $( \mathrm { i } . { \bf e } . , e _ { i , k }$ and $p _ { i , j } ) .$ . The values of these two parameters can be found in Table 2 and Table $^ { 3 , }$ respectively.

Based on random sampling and statistics method, we randomly and respectively select five days of data related to each node from historical data and analyze the changes of the data quality problem (for quanti tative method see section 4.1.1) before and after the operation of the node. Then we can get the results of the data quality problem generated by each node (see Table 2). Further, we calculate the values of the data transfer ratio (see Table 3) by its definition in 4.1.1.

$D Q P _ { i } ^ { k }$ can be calculated according to $\operatorname { E q . } ( 4 )$ and we take the inaccuracy caused by node $1 ~ ( \mathrm { i . e . , } ~ D Q P _ { 1 } { } ^ { 1 } )$ as an example. As can be seen from Fig. 3, there are four data streams from node 1 to DB :

Stream 1: $\mathrm { P _ { 1 } \cdot \mathrm { ~ > ~ } ~ P _ { 2 } \cdot \mathrm { ~ > ~ } ~ P _ { 3 } \cdot \mathrm { ~ > ~ } ~ P _ { 4 } \cdot \mathrm { ~ > ~ } ~ P _ { 5 ^ { - } } ~ > ~ D B _ { 1 } ; }$ Stream $2 \colon \mathrm { P } _ { 1 }$ $\begin{array} { r } { \mathrm { ~  ~ { ~ > ~ } ~ } \mathrm { P } _ { 2 } \mathrm { ~  ~ { ~ > ~ } ~ } \mathrm { P } _ { 3 } \mathrm { ~  ~ { ~ > ~ } ~ } \mathrm { P } _ { 4 } \mathrm { ~  ~ { ~ > ~ } ~ } \mathrm { P } _ { 6 ^ { - } } \mathrm { ~  ~ { ~ > ~ } ~ } \mathrm { P } _ { 7 ^ { - } } \mathrm { ~  ~ { ~ > ~ } ~ } \mathrm { D } \mathrm { B } _ { 1 } \mathrm { ; } } \end{array}$

Stream $3 { \mathrm { : ~ P _ { 1 } - > ~ P _ { 2 } - > ~ P _ { 4 } - > ~ P _ { 5 } - > ~ D B _ { 1 } ; } }$ ; Stream 4: $\mathsf { P } _ { 1 } - \mathsf { \Omega } > \mathsf { P } _ { 2 }$ $\mathrm { ~  ~ { ~ \mathsf ~ { ~ \Sigma ~ } ~ } ~ } > \mathrm { ~ \mathsf { P } ~ } _ { 4 } \mathrm { ~  ~ { ~ \mathsf ~ { ~ \Sigma ~ } ~ } ~ } > \mathrm { ~ \mathsf { P } ~ } _ { 6 } \mathrm { ~  ~ { ~ \mathsf ~ { ~ \Sigma ~ } ~ } ~ } > \mathrm { ~ \mathsf { P } ~ } _ { 7 ^ { - } } \mathrm { ~  ~ { ~ \mathsf ~ { ~ \Sigma ~ } ~ } ~ } > \mathrm { ~ \mathsf { D } ~ } \mathsf { B } _ { 1 }$

Table 2 shows the probability of inaccuracy caused by $P _ { 1 }$ . According to Eq. (4), we can get

$$
\begin{array}{c} D Q P _ {1} ^ {1} = 0. 0 8 \cdot (1 \cdot 1 \cdot 0. 1 1 \cdot 1 \cdot 0. 1 2 + 1 \cdot 1 \cdot 0. 1 1 \cdot 1 \cdot 1 \cdot 0. 3 2 + 1 \cdot 0. 8 9 \cdot 1 \cdot 0. 1 2 + 1 \cdot 0. 8 9 \\ \cdot 1 \cdot 1 \cdot 0. 3 2) = 3. 5 2 e - 2 \end{array}
$$

According to the above steps, the results of $D Q P _ { i } ^ { k }$ are shown in Table 4.

The control procedures we performed include auditing input data, correcting old data errors and configuring data collection equipment. The control resources used in this project include humans and equipment. The proportion of control resources invested in each node is tested at three levels $( x _ { i , k } = \{ 0 . 1 , 0 . 2 , 0 . 2 5 \} , \forall i , k )$ , and each level takes five days of data to calculate the probability of the data quality problem generated by the nodes before and after control. Then, we calculate the

Corresponding data operation explanation.  
Table 2  
Data quality problem generated by each node.

<table><tr><td>Node (i)</td><td> $e_{i,1}$ </td><td> $e_{i,2}$ </td><td> $e_{i,3}$ </td><td>Node (i)</td><td> $e_{i,1}$ </td><td> $e_{i,2}$ </td><td> $e_{i,3}$ </td></tr><tr><td>1</td><td>0.08</td><td>0.1</td><td>0.03</td><td>12</td><td>0.06</td><td>0.05</td><td>0.01</td></tr><tr><td>2</td><td>0</td><td>0.01</td><td>0.008</td><td>13</td><td>0.09</td><td>0.1</td><td>0.02</td></tr><tr><td>3</td><td>0.12</td><td>0.16</td><td>0.03</td><td>14</td><td>0</td><td>0.01</td><td>0.02</td></tr><tr><td>4</td><td>0</td><td>0.003</td><td>0.01</td><td>15</td><td>0</td><td>0.04</td><td>0.004</td></tr><tr><td>5</td><td>0.06</td><td>0.03</td><td>0.006</td><td>16</td><td>0.003</td><td>0.04</td><td>0.008</td></tr><tr><td>6</td><td>0.03</td><td>0.003</td><td>0.001</td><td>17</td><td>0.02</td><td>0.05</td><td>0.007</td></tr><tr><td>7</td><td>0.02</td><td>0.1</td><td>0.03</td><td>18</td><td>0</td><td>0.002</td><td>0.005</td></tr><tr><td>8</td><td>0.001</td><td>0.002</td><td>0.0005</td><td>19</td><td>0.001</td><td>0.006</td><td>0.001</td></tr><tr><td>9</td><td>0.006</td><td>0.004</td><td>0.0008</td><td>20</td><td>0.08</td><td>0.08</td><td>0.08</td></tr><tr><td>10</td><td>0</td><td>0.001</td><td>0.003</td><td>21</td><td>0.2</td><td>0.1</td><td>0.08</td></tr><tr><td>11</td><td>0.01</td><td>0.07</td><td>0.004</td><td>DB1</td><td>0</td><td>0</td><td>0</td></tr></table>

Note: $e _ { i , \ 1 } , e _ { i , \ 2 } ,$ and $e _ { i , \ 3 }$ denote the probability of inaccuracy, incompleteness, and mismembership, respectively, generated by the $i ^ { \mathrm { { t h } } }$ node.

Table 3  
Data transfer ratio.

<table><tr><td>(i, j)</td><td> $p_{i, j}$ </td><td>(i, j)</td><td> $p_{i, j}$ </td><td>(i, j)</td><td> $p_{i, j}$ </td></tr><tr><td>[1, 2]</td><td>1</td><td>[8, 9]</td><td>1</td><td>[15, 16]</td><td>1</td></tr><tr><td>[2, 3]</td><td>1</td><td>[9, 10]</td><td>1</td><td>[15, 17]</td><td>0.41</td></tr><tr><td>[2, 4]</td><td>0.89</td><td>[10, 11]</td><td>1</td><td>(16,DB1)</td><td>0.05</td></tr><tr><td>[3, 4]</td><td>0.11</td><td>[10, 12]</td><td>0.93</td><td>[17, 18]</td><td>1</td></tr><tr><td>[4, 5]</td><td>1</td><td>[11, 12]</td><td>0.07</td><td>[18, 19]</td><td>1</td></tr><tr><td>[4, 6]</td><td>1</td><td>(12,DB1)</td><td>0.11</td><td>[18, 20]</td><td>0.93</td></tr><tr><td>(5,DB1)</td><td>0.12</td><td>[13, 14]</td><td>1</td><td>[19, 20]</td><td>0.07</td></tr><tr><td>[6, 7]</td><td>1</td><td>[14, 15]</td><td>1</td><td>(20,DB1)</td><td>0.12</td></tr><tr><td>(7,DB1)</td><td>0.32</td><td>[14, 17]</td><td>0.59</td><td>(21,DB1)</td><td>0.28</td></tr></table>

Accumulation of the data quality problem generated by nodes in the information system.

<table><tr><td>Node(i)</td><td> $DQP_{i}^{1}$ </td><td> $DQP_{i}^{2}$ </td><td> $DQP_{i}^{3}$ </td><td>Node(i)</td><td> $DQP_{i}^{1}$ </td><td> $DQP_{i}^{2}$ </td><td> $DQP_{i}^{3}$ </td></tr><tr><td>1</td><td>3.52e-2</td><td>4.40e-2</td><td>1.32e-2</td><td>12</td><td>6.60e-3</td><td>5.50e-3</td><td>1.10e-3</td></tr><tr><td>2</td><td>0</td><td>4.40e-3</td><td>3.50e-3</td><td>13</td><td>1.53e-2</td><td>1.70e-2</td><td>3.40e-3</td></tr><tr><td>3</td><td>5.80e-3</td><td>7.70e-3</td><td>1.50e-3</td><td>14</td><td>0</td><td>1.70e-3</td><td>3.40e-3</td></tr><tr><td>4</td><td>0</td><td>1.30e-3</td><td>4.40e-3</td><td>15</td><td>0</td><td>4.00e-3</td><td>3.97e-4</td></tr><tr><td>5</td><td>7.20e-3</td><td>3.60e-3</td><td>7.20e-4</td><td>16</td><td>1.50e-4</td><td>2.00e-3</td><td>4.00e-4</td></tr><tr><td>6</td><td>9.60e-3</td><td>9.60e-4</td><td>3.20e-4</td><td>17</td><td>2.40e-3</td><td>6.00e-3</td><td>8.40e-4</td></tr><tr><td>7</td><td>6.40e-3</td><td>3.20e-2</td><td>9.60e-3</td><td>18</td><td>0</td><td>2.40e-4</td><td>6.00e-4</td></tr><tr><td>8</td><td>1.10e-4</td><td>2.20e-4</td><td>5.50e-5</td><td>19</td><td>8.40e-6</td><td>5.04e-5</td><td>8.40e-6</td></tr><tr><td>9</td><td>6.60e-4</td><td>4.40e-4</td><td>8.80e-6</td><td>20</td><td>9.60e-3</td><td>9.60e-3</td><td>9.60e-3</td></tr><tr><td>10</td><td>0</td><td>1.10e-4</td><td>3.30e-4</td><td>21</td><td>5.60e-2</td><td>2.80e-2</td><td>2.24e-2</td></tr><tr><td>11</td><td>7.70e-5</td><td>5.39e-4</td><td>3.08e-5</td><td></td><td></td><td></td><td></td></tr></table>

control eficiency by Eq. (6); the corresponding results can be found in Appendix B. The parameter matrices $g _ { i , k }$ and $\tau _ { i , \astrosun }$ can be obtained by the method of parameter estimation [28].

<table><tr><td>Process</td><td>Nota-tion</td><td>Data operation</td><td>Process</td><td>Nota-tion</td><td>Data operation</td></tr><tr><td rowspan="7">Sale</td><td> $P_1$ </td><td>Add/Query order information</td><td>Inventory</td><td> $P_{13}$ </td><td>Add goods receipt information</td></tr><tr><td> $P_2$ </td><td>New customer check</td><td></td><td> $P_{14}$ </td><td>Exemption check</td></tr><tr><td> $P_3$ </td><td>Add customer information</td><td></td><td> $P_{15}$ </td><td>Qualified check</td></tr><tr><td> $P_4$ </td><td>Adequate inventory check</td><td></td><td> $P_{16}$ </td><td>Add return information</td></tr><tr><td> $P_5$ </td><td>Add purchase information</td><td></td><td> $P_{17}$ </td><td>Add transfer information</td></tr><tr><td> $P_6$ </td><td>Generate an order</td><td></td><td> $P_{18}$ </td><td>Differences exist check</td></tr><tr><td> $P_7$ </td><td>Add outbound information</td><td></td><td> $P_{19}$ </td><td>Correct transfer information</td></tr><tr><td rowspan="5">Replenish-ment</td><td> $P_8$ </td><td>Query purchase information</td><td></td><td> $P_{20}$ </td><td>Add warehousing information</td></tr><tr><td> $P_9$ </td><td>Supplier option</td><td>Procurement</td><td> $P_{21}$ </td><td>Add/Modify inventory information</td></tr><tr><td> $P_{10}$ </td><td>New supplier check</td><td></td><td></td><td></td></tr><tr><td> $P_{11}$ </td><td>Add supplier information</td><td>Database</td><td> $DB_1$ </td><td></td></tr><tr><td> $P_{12}$ </td><td>Add order information</td><td></td><td></td><td></td></tr></table>

Table 5  
Results of the expected data quality problem under the three control strategies.

<table><tr><td>Control strategy</td><td>Expected data quality problem</td><td>Resource consumption ratio</td></tr><tr><td>No control</td><td>4.00e-1</td><td>0</td></tr><tr><td>Random control</td><td>3.37e-1</td><td>100%</td></tr><tr><td>Optimal control</td><td>3.00e-1</td><td>100%</td></tr></table>

$0 . 0 6 3 \times 1 0 0 \% )$ better than that under random control. It shows that the efective utilization of resources will increase significantly under optimal control.

Fig. 4(a) and Fig. 4(b) show the probability density distribution (PDF) and the cumulative distribution (CDF), respectively, of the data quality problem under the three control strategies.

The results of Fig. 4(a) show that the optimal control strategy can not only make the probability distribution of data quality problem

<table><tr><td> $\tau_{i,k} = \left[ \begin{array}{ccccccccccccccccccccc} 0.60 & 0 & 0.29 & 0 & 0.31 & 0.27 & 0.19 & 0.30 & 0.23 & 0 & 0.24 & 0.35 & 0.24 & 0 & 0 & 0.25 & 0.17 & 0 & 0.23 & 0.28 & 0.30 \\ 0.44 & 0.56 & 0.37 & 0.31 & 0.26 & 0.25 & 0.42 & 0.45 & 0.22 & 0.21 & 0.23 & 0.19 & 0.15 & 0.38 & 0.38 & 0.31 & 0.16 & 0.47 & 0.25 & 0.38 & 0.22 \\ 0.33 & 0.32 & 0.30 & 0.20 & 0.52 & 0.35 & 0.24 & 0.23 & 0.33 & 0.19 & 0.15 & 0.24 & 0.18 & 0.37 & 0.37 & 0.27 & 0.21 & 0.18 & 0.24 & 0.30 & 0.26 \end{array} \right]^{\mathrm{T}}$ </td></tr></table>

$g _ { i , \ k } \ < \ 1 \ ( \forall i , k )$ indicates that even if all the control resources are invested in a node, the data quality problem generated by the node cannot be completely eliminated. $\tau _ { i , \textit { k } } < \textit { 1 } ( \forall i , k )$ indicates that the control eficiency exhibits diminishing marginal efectiveness. We use the optimization toolbox in MATLAB (R2018a) software to solve the model and perform ten times for the random control and optimal control, respectively. We will show the optimal value and its corresponding resource allocation strategy in the next section.

## 6.2. Model optimization results

In this section, we compare the following three control strategies: no control, random control, and optimal control.

## 1) Results of the objective

Under the no control, random control, and optimal control strategies, the corresponding expected values of the data quality problem of the information system are shown in Table 5.

Table 5 shows that for the same resource consumption $( \mathrm { i . e . , ~ } \Sigma _ { i , ~ k } x _ { i , }$ $_ k = 1 0 0 \% )$ , the expected value of the data quality problem under the random control strategy is 0.063 less than that under the non-control strategy. Under the optimal control strategy, the expected data quality problem is 0.1 better than that under the non-control strategy. Thus, the data quality under optimal control is 58.7% $( { \mathrm { i . e . , ~ } } ( 0 . 1 { \mathrm { ~ - ~ } } 0 . 0 6 3 ) /$ move in the negative direction (i.e., the data quality problem of in formation system decreases), but also constrain the results of the data quality problem $( \mathrm { i . e . }$ , the data quality problem variance is smaller). It means the optimal control strategy can make the uncertainty of data quality problems smaller, which, in turn, helps data managers to control the risks caused by fluctuations in the data quality problem. The results of Fig. 4(b) show that, under the optimal control strategy, the cumulative distribution function of the data quality problem has a larger slope in the middle of the function. Because of the aggregation efect of the optimal control strategy on the distribution of the density function, the cumulative distribution function can converge faster to the probability of one in the middle of the function.

![](/api/attachments/MPCF8DMJ/fulltext/images/2b87161775756700eed15a72cd071910273ffc04925f7fcefe9a2e49d6ee7737.jpg)  
(a) PDF of the data quality problem

Table 6  
Resource allocation under the optimal control strategy.

<table><tr><td>Node (i)</td><td> $x_{i,1}$ </td><td> $x_{i,2}$ </td><td> $x_{i,3}$ </td><td> $\Sigma_kx_{i,k}$ </td></tr><tr><td>1</td><td>18.2e-2</td><td>21.0e-2</td><td>3.43e-2</td><td>42.6e-2</td></tr><tr><td>2</td><td>0</td><td>0.11e-2</td><td>0.33e-2</td><td>0.44e-2</td></tr><tr><td>3</td><td>0.94e-2</td><td>0.89e-2</td><td>0.17e-2</td><td>2.00e-2</td></tr><tr><td>4</td><td>0</td><td>0.06e-2</td><td>0.77e-2</td><td>0.83e-2</td></tr><tr><td>5</td><td>0.86e-2</td><td>0.42e-2</td><td>0.01e-2</td><td>1.29e-2</td></tr><tr><td>6</td><td>1.48e-2</td><td>0.08e-2</td><td>0.02e-2</td><td>1.58e-2</td></tr><tr><td>7</td><td>1.05e-2</td><td>11.0e-2</td><td>1.66e-2</td><td>13.7e-2</td></tr><tr><td>8</td><td>0.01e-2</td><td>0.01e-2</td><td>0.01e-2</td><td>0.03e-2</td></tr><tr><td>9</td><td>0.05e-2</td><td>0.04e-2</td><td>0.01e-2</td><td>0.10e-2</td></tr><tr><td>10</td><td>0</td><td>0.01e-2</td><td>0.04e-2</td><td>0.05e-2</td></tr><tr><td>11</td><td>0.01e-2</td><td>0.04e-2</td><td>0.01e-2</td><td>0.06e-2</td></tr><tr><td>12</td><td>0.67e-2</td><td>0.70e-2</td><td>0.11e-2</td><td>1.48e-2</td></tr><tr><td>13</td><td>3.82e-2</td><td>3.45e-2</td><td>0.41e-2</td><td>7.68e-2</td></tr><tr><td>14</td><td>0</td><td>0.08e-2</td><td>0.39e-2</td><td>0.47e-2</td></tr><tr><td>15</td><td>0</td><td>0.29e-2</td><td>0.02e-2</td><td>0.31e-2</td></tr><tr><td>16</td><td>0.01e-2</td><td>0.16e-2</td><td>0.03e-2</td><td>0.20e-2</td></tr><tr><td>17</td><td>0.31e-2</td><td>0.70e-2</td><td>0.08e-2</td><td>1.09e-2</td></tr><tr><td>18</td><td>0</td><td>0.01e-2</td><td>0.06e-2</td><td>0.07e-2</td></tr><tr><td>19</td><td>0.01e-2</td><td>0.01e-2</td><td>0.01e-2</td><td>0.03e-2</td></tr><tr><td>20</td><td>1.09e-2</td><td>1.28e-2</td><td>1.09e-2</td><td>3.46e-2</td></tr><tr><td>21</td><td>11.2e-2</td><td>5.45e-2</td><td>5.94e-2</td><td>22.6e-2</td></tr></table>

![](/api/attachments/MPCF8DMJ/fulltext/images/f9df323713aa3ed06627f884e1723e30bac87d1b6df05c70d8c0b7805264eb18.jpg)  
(b) CDF of the data quality problem  
Fig. 4. The PDF and CDF of the data quality problem based on the three control allocation strategies

## 2) Optimal resource allocation

Table 6 shows the resource allocation scheme under the guidance of the optimal control strategy, where $x _ { i , \ 1 } , \ x _ { i , \ 2 } ,$ and $x _ { i , \ 3 }$ denote the re source allocation ratios on the inaccuracy, incompleteness and mis membership dimensions, respectively.

Table 6 shows that node 1, node 21, and node 7, which are the top three nodes in terms of resource allocation, have values of 42.6e-2, 22.6e-2, and 13.7e-2, respectively. We could find that these three nodes may cause a large data quality problem (such as node 21 and node 1) or account for a large proportion of the data transfer ratio (node 7). For diferent dimensions of data quality problems of the same node, the number of resource configurations is proportional to the level of the data quality problem. For example, the value of inaccuracy, incompleteness and mismembership caused by node 1 is 3.52e-2, 4.40e-2, and 1.32e-2, respectively, and the corresponding resource proportion is 18.2e-2, 21.0e-2, and 3.43e-2.

## 3) Sensitivity analysis

We analyze the impact of the key parameters in the model on the objective of the model $( \boldsymbol { \mathrm { i . e . } } ,$ , the data quality problem of the information system) under diferent control strategies. In this paper, two parameters, the control eficiency function parameter $g _ { i , \ k }$ and the control eficiency elasticity coeficient $\tau _ { i , k } ,$ are selected for sensitivity analysis. Holding the other parameters fixed, we change the values of these two parameters. To keep the values of the two parameters within their domain, we set the range of the two parameters as {−100%,……, +20%}, and the data quality problem of the information system under the optimal control and random control strategies is solved.

Fig. 5 shows the efect of the parameter g<sub>i,</sub> <sub>k</sub> changes on the expected

![](/api/attachments/MPCF8DMJ/fulltext/images/c1de982f922c24ebf4944596cc5acbb16791d64f9ffd028e3764841779bbf3cd.jpg)  
Fig. 5. Sensitivity analysis of parameter g .

![](/api/attachments/MPCF8DMJ/fulltext/images/61ae0d24791c868b53670e96ef1cea5601cdc56804be8caf0e7bc7815b2a8f64.jpg)  
Fig. 6. Sensitivity analysis of parameter $\tau _ { i , \ i }$ <sub>k</sub>.

data quality problem under random and optimal control strategies.

Fig. 5 shows that the expected data quality problem of the information system under each control strategy decreases as the parameter $g _ { i , \ k }$ increases. The expected data quality problem under the optimal control strategy will fall faster than that under the stochastic control strategy. It means that with the improvement of control measures (using fewer resources, while achieving greater control eficiency), the advantages of the optimal control strategy will become more and more obvious. In other words, under the guidance of the optimal control strategy, the returns from the improvement in control procedures will increase.

Fig. 6 shows the efect of changes in parameter $\tau _ { i , k }$ on the expected data quality problem under random and optimal control strategies.

Fig. 6 shows that the expected data quality problem of the information system under any control strategy increases as $\tau _ { i , k }$ increases. From the results of the two control strategies, we find that the fluctuation in the optimal control strategy is smaller than that in the random control strategy when parameter $\tau _ { i , k }$ changes. It means that the robustness of the optimal control strategy is better than that of the random control strategy.

## 7. Conclusions

In recent years, data quality management has attracted much attention. Although conceptual models of process-driven data quality management are proposed, formal methodologies need further study [29]. Our work contributes to the related literature by integrating data quality management with data process modeling and analysis. In this paper, we develop a process-based model to find a cost-efective resource-allocation strategy to minimize the data quality problem of information systems. The built model introduces the idea of process management and focuses on controlling the data operation behavior to manage data quality. Further, we develop a DQ-Petri net to quantitative analysis the data quality problem propagation and accumulation in an information system, which extends the application of Petri net in the field of data quality management. The result demonstrates that the data flow structures influence the data quality problem propagation and accumulation, and optimal control resources allocation.

Our work also has important practical implications. First, our model requires to estimate the data quality problems caused by each node based on historical logs and sample method. On the one hand, it will find the nodes that have a high impact on the information system's data quality, reminding managers to focus on it. On the other hand, the results can be used to assist in the performance evaluation of system operators. Second, the model will provide managers with solutions to maximize the use of existing resources to improve the data quality of information systems.

The model proposed in this paper can be embedded in IT support tools in the future by using existing visualization tools such as Apache NiFi. At present, the model can only analyze the data quality dimension measured by probability. Thus, it cannot handle some dimensions such as objectivity, ease of understanding, accessibility, etc. Future work can extend some of the findings. First, the model does not take into account the dynamic adjustment in the configuration that can be considered when real-time data acquisition and analysis equipment are used to capture the data quality problem in the process of an information system. Second, the current assessment and control procedures are based on the assumption of a single period, so the long-term efect of control measures is not considered. It is necessary to view this efect when considering the multi-period optimization problem in the future.

Third, the thought of process-based data quality management can be used in other scenarios, such as enterprise data lakes, but some issues need further study. For example, how to assess the data quality problem of the unstructured data and quantify the relationship between the data quality of data sources and data lake.

## Acknowledgements

The research presented in this paper is supported by China Postdoctoral Science Foundation (2019M663767), the Fundamental Research Funds for the Central Universities (SK2020022), the National Natural Science Foundation Project of China (71572145), Soft Science Research Project of Shaanxi Provincial Department of Science and Technology (2020KRM206), and Humanity and Social Science Youth Foundation of Ministry of Education of China (19XJC630012).

## Appendix A

## A.1. Proof of Proposition 1

We prove it by induction. When $n = 2 ,$ according to the Definition 2, the cumulative of the $k ^ { \mathrm { { t h } } }$ dimension data quality problem from node $P _ { 1 }$ to $P _ { 2 }$ is $D Q P _ { 1 , ~ 2 } { } ^ { k } = L _ { 1 } { } ^ { k } \times p _ { 1 , ~ 2 } ,$ proposition is founded. Suppose the proposition is founded when $n = \nu ,$ that is $D Q P _ { 1 , \nu } ^ { k } = \sum _ { j = 1 } ^ { \nu - 1 } \left( L _ { j } ^ { k } \times \prod _ { r = j } ^ { \nu - 1 } p _ { r , r + 1 } \right) .$

When $n = \nu + 1$ , according to the Definition $^ { 2 , }$ we could get ${ \cal D } Q P _ { 1 , \ \nu + 1 } { } ^ { k } = { \cal D } Q P _ { 1 , \ \nu } { } ^ { k } + { \cal D } Q P _ { \nu , \ \nu + 1 } { } ^ { k }$

that is $D Q P _ { 1 , \nu + 1 } ^ { k } = \sum _ { j = 1 } ^ { \nu - 1 } \left( L _ { j } ^ { k } \times \prod _ { r = j } ^ { \nu - 1 } p _ { r , r + 1 } \right) + L _ { \nu } ^ { k } \times p _ { \nu , \nu + 1 } = \sum _ { j = 1 } ^ { \nu } \left( L _ { j } ^ { k } \times \prod _ { r = j } ^ { \nu } p _ { r , r + 1 } \right) .$

Thus, the proposition is founded when $n = \nu + 1$

## A.2. Proof of Proposition 2

Since the data quality problem propagated by each stream is independent of each other, that is, $p _ { 1 , \ 2 } , p _ { 1 , \ 3 } , \ldots , \mathrm { o r } p _ { 1 , \mathrm { ~ n ~ } }$ is independent of each other. So according to $\mathtt { E q . ( 1 ) } ,$ we know, $\overset \vartriangle { D Q P _ { 1 , F } ^ { k } } = \boldsymbol { L } _ { 1 } ^ { k } \times \boldsymbol { p } _ { 1 , 2 } + \boldsymbol { L } _ { 1 } ^ { k } \times \boldsymbol { p } _ { 1 , 3 } ^ { \cdot } + \cdots + \boldsymbol { L } _ { 1 } ^ { k } \times \boldsymbol { p } _ { 1 , n } = \underset { t \in F } { \sum } ( \boldsymbol { L } _ { 1 } ^ { k } \times \overset { \cdot \cdot \cdot } { \boldsymbol { p } _ { 1 , f } } ) .$

## A.3. Proof of Proposition 3

Let the number of tuples generated by the $n ^ { \mathrm { t h } }$ node per unit time be $N _ { n }$ and the number of tuples that the $\boldsymbol { u } ^ { \mathrm { t h } }$ node will pass to the $n ^ { \mathrm { t h } }$ node in unit time be $N _ { u , n } , u = 1 , . . . , n - 1$ . Then, the number of tuples with the $k ^ { \mathrm { { t h } } }$ dimension of data quality problem passed to the $n ^ { \mathrm { t h } }$ node per unit time is $\sum \ ( L _ { u } ^ { k } \times \dot { N } _ { u , n } )$ . The impact of these tuples with data quality problems on the $n ^ { \mathrm { t h } }$ node is $\sum _ { u \in U } ^ { \bullet } ( L _ { u } ^ { k ^ { * } } \times N _ { u , n } ) / N _ { n }$ , that is, $D Q P _ { U , n } ^ { k } = \sum _ { u \in U } \mathsf { \bar { ( L } } _ { u } ^ { k } \times p _ { u , n } )$ u U

## A.4. Proof of Proposition 4

For node 1, its general structure and its equivalent net structure are shown in the following figure,

![](/api/attachments/MPCF8DMJ/fulltext/images/806ef2eaebbaf0ca214c4981b91ad9929652a7e2b9fd654a2192647fe512bed2.jpg)

According to $\operatorname { E q . } ( 1 ) , \operatorname { E q . } ( 2 )$ and $\operatorname { E q . } ( 3 )$ , we can get $D Q P _ { i } ^ { k } = \sum _ { l = 1 } ^ { m } \left( e _ { i , k } \times \prod _ { j = 1 } ^ { n _ { l } - 1 } p _ { j , j + 1 } ^ { i , l } \right) .$

## A.5. Proof of Proposition 5

Let $A _ { i , k } = e _ { i , k } \mathbf { g } _ { i , k } \sum _ { l } ^ { m } \prod _ { j = 1 } ^ { n _ { l } - 1 } p _ { j , j + 1 } ^ { i , l }$ , then the optimization model could be rewritten as follows. Max $\sum _ { i , k } A _ { i , k } x _ { i , k } ^ { \tau _ { i , k } }$ s t s.t.

$$
\sum_ {i, k} x _ {i, k} \leq 1; 0 \leq x _ {i, k} \leq 1, \forall i, k; 0 \leq g _ {i, k} \leq 1, \forall i, k; \tau_ {i. k} > 0, \forall i, k; 0 \leq p _ {j, j + 1} ^ {i, l} \leq 1, \forall i, j, l
$$

When $\tau _ { i , \ k } = \tau , \forall i , k ,$ the model has a closed set solution, then the Lagrange function of the above model is as follows,

$$
L (x, \lambda) = \sum_ {i, k} A _ {i, k} x _ {i, k} ^ {\tau} + \lambda \left(1 - \sum_ {i. k} x _ {i, k}\right) s. t. x _ {i, k} \geq 0.
$$

Then the gradients of the objective function and the constraint function are:

$$
\frac {\partial L (x , \lambda)}{\partial x} = A _ {i, k} \tau x _ {i, k} ^ {\tau - 1} - \lambda ; \partial L (x, \lambda) / \partial \lambda = 1 - \sum_ {i, k} x _ {i, k}
$$

Let $x ^ { * }$ be the point of Kuhn-Tucker, the K-T conditions for this problem can be written as follows:

$$
\left\{ \begin{array}{l} A _ {i, k} \tau (x _ {i, k} ^ {*}) ^ {\tau - 1} - \lambda^ {*} = 0 \\ \lambda^ {*} \bigg (1 - \sum_ {i. k} x _ {i, k} ^ {*} \bigg) = 0 \\ \lambda^ {*} \geq 0 \end{array} \right.
$$

then

$$
x _ {i, k} ^ {*} = \left\{ \begin{array}{l l} \left(\frac {\lambda^ {*}}{A _ {i , k} \tau}\right) ^ {\frac {1}{\tau - 1}}, & \text { if } \tau <   1 \text { and } \frac {\lambda^ {*}}{A _ {i , k} \tau} <   1 \\ \text { Not   feasible }, & \text { else } \end{array} \right.
$$

where, $\lambda ^ { * } = \left( \sum _ { i , k } \frac { 1 } { ( A _ { i , k } \tau ) ^ { \frac { 1 } { \tau - 1 } } } \right) ^ { 1 - \tau } .$

For boundary conditions, ${ { \lambda } ^ { * } } = 0 ,$ , then ${ x _ { i } } _ { k } { ^ * } = 1$

$$
\text {So} x _ {i, k} ^ {*} = \left\{ \begin{array}{l l} \left(\frac {\lambda^ {*}}{A _ {i , k} \tau}\right) ^ {\frac {1}{\tau - 1}}, & \text {if} \tau <   1 \quad \text {and} \quad \frac {\lambda^ {*}}{A _ {i , k} \tau} <   1; \\ & 1, \qquad \text {else} \end{array} \right. \text {where,} \lambda^ {*} = \left(\sum_ {i, k} \frac {1}{(A _ {i , k} \tau) ^ {\frac {1}{\tau - 1}}}\right) ^ {1 - \tau}.
$$

When we let the factor $e _ { i , \ k }$ and g<sub>i,</sub> <sub>k</sub> be constant, we can abbreviate a function that is only related to the data flow structure that is $x _ { i } ^ { * } = \sum _ { k } x _ { i , k } ^ { * } = B { \left( \sum _ { l } \prod _ { j = 1 } ^ { n _ { l } - 1 } p _ { j , j + 1 } ^ { i , l } \right) } ^ { \frac { 1 } { 1 - \tau } }$ , where, B is a constant, because $\tau \ < \ 1$ then $x _ { i } ^ { * } \propto \sum _ { l } ^ { m } \prod _ { j = 1 } ^ { n _ { l } - 1 } p _ { j , j + 1 } ^ { i , l } .$

A.6. Proof of Corollary 1

As can be seen from the proof of Proposition $^ { 5 , }$ when the other variables are the same, then $x _ { i } ^ { * } = B \left( \sum _ { l } \prod _ { j = 1 } ^ { n _ { l } - 1 } p _ { j , j + 1 } ^ { i , l } \right) ^ { \frac { 1 } { 1 - \tau } }$ . Because it is a sequence structure, there is only one data stream in the information system, the resource allocation for the $i ^ { \mathrm { { t h } } }$ node can be abbreviated as $x _ { i } ^ { * } = B { \Bigg ( } \prod _ { i = 1 } ^ { n - 1 } p _ { i , i + 1 } { \Bigg ) } ^ { \frac { 1 } { 1 - \tau } }$ Then $\frac { x _ { i } ^ { * } } { x _ { i + s } ^ { * } } = \left( \prod _ { i } ^ { i + s - 1 } p _ { i , i + 1 } \right) ^ { \frac { 1 } { 1 - \tau } }$

## A.7. Proof of corollaries 2–3

The proof is similar as Corollary 1.

The following three matrices are the values of control eficiency $\left( \eta _ { i , \ k } \right)$ corresponding to $x _ { i , \ k } \ = \ 0 . 1 ( \mathrm { t o p } ) , \ x _ { i , \ k } \ = \ 0 . 2 ( \mathrm { m i d d l e } )$ and $x _  i , $ = 0.25(bottom), respectively

<table><tr><td> $\eta_{i,k}(0.1) = \left[ \begin{array}{ccccccccc} 0.2 & 0 & 0.38 & 0 & 0.29 & 0.33 & 0.45 & 0.27 & 0.33 & 0 & 0.39 & 0.25 & 0.44 & 0 & 0 & 0.33 & 0.45 & 0 & 0.39 & 0.25 & 0.21 \\ 0.27 & 0.20 & 0.25 & 0.21 & 0.34 & 0.34 & 0.26 & 0.19 & 0.38 & 0.33 & 0.28 & 0.37 & 0.53 & 0.24 & 0.24 & 0.29 & 0.37 & 0.19 & 0.27 & 0.26 & 0.33 \\ 0.35 & 0.29 & 0.38 & 0.49 & 0.22 & 0.29 & 0.37 & 0.42 & 0.35 & 0.48 & 0.56 & 0.37 & 0.39 & 0.32 & 0.32 & 0.29 & 0.37 & 0.41 & 0.36 & 0.25 & 0.38 \end{array} \right]^{\mathrm{T}}$ </td></tr><tr><td> $\eta_{i,k}(0.2) = \left[ \begin{array}{ccccccccc} 0.34 & 0 & 0.47 & 0 & 0.34 & 0.39 & 0.52 & 0.35 & 0.40 & 0 & 0.45 & 0.34 & 0.55 & 0 & 0 & 0.38 & 0.53 & 0 & 0.49 & 0.32 & 0.29 \\ 0.38 & 0.31 & 0.37 & 0.28 & 0.41 & 0.39 & 0.39 & 0.28 & 0.45 & 0.41 & 0.33 & 0.42 & 0.62 & 0.33 & 0.33 & 0.40 & 0.42 & 0.28 & 0.35 & 0.35 & 0.41 \\ 0.54 & 0.37 & 0.54 & 0.58 & 0.38 & 0.44 & 0.45 & 0.49 & 0.50 & 0.54 & 0.63 & 0.45 & 0.46 & 0.48 & 0.48 & 0.35 & 0.44 & 0.47 & 0.42 & 0.31 & 0.51 \end{array} \right]^{\mathrm{T}}$ </td></tr><tr><td> $\eta_{i,k}(0.25) = \left[ \begin{array}{cccccccccccc} 0.67 & 0 & 0.67 & 0 & 0.52 & 0.55 & 0.65 & 0.49 & 0.52 & 0 & 0.62 & 0.50 & 0.71 & 0 & 0 & 0.53 & 0.62 & 0 & 0.62 & 0.44 & 0.39 \\ 0.64 & 0.59 & 0.54 & 0.39 & 0.56 & 0.55 & 0.61 & 0.40 & 0.59 & 0.51 & 0.44 & 0.54 & 0.72 & 0.51 & 0.51 & 0.55 & 0.51 & 0.48 & 0.45 & 0.55 & 0.52 \\ 0.72 & 0.72 & 0.60 & 0.73 & 0.65 & 0.61 & 0.60 & 0.66 & 0.70 & 0.69 & 0.75 & 0.60 & 0.56 & 0.69 & 0.69 & 0.49 & 0.56 & 0.59 & 0.57 & 0.45 & 0.65 \end{array} \right]^{\mathrm{T}}$ </td></tr></table>

## References

[1] K.C. Laudon, Data quality and due process in large interorganizational record sys tems, Commun. ACM 29 (1986) 4–11. https://doi,org/10.1145/5465.5466.

[2] A. Parvari, R. Anvari, N.N. binti A. Mansor, M. Jafarpoor, M. Parvari, Technology acceptance model, organizational commitment and turnover intention: a con ceptual framework, Rev. Eur. Stud. 7 (2015) 146–152, https://doi.org/10.5539/

res.v7n12p146.

[3] T. Schutz, The 2018 Global Data Management Benchmark Report, Experian Data Quality, Boston, 2018https://www.edq.com/globalassets/white-papers/2018- global-data-management-benchmark-report pdf

[4] B. Heinrich, M. Klier, A. Schiller, G. Wagner, Assessing data quality – a probabilitybased metric for semantic consistency, Decis. Support. Syst. 110 (2018) 95–106,

[5] A. Parssian, S. Sarkar, V.S. Jacob, Assessing data quality for information products:

impact of selection, projection, and cartesian product, Manag. Sci. 50 (2004) 967–982, https://doi.org/10.1287/mnsc.1040.0237.

[6] D. Dey, S. Kumar, Data quality of query results with generalized selection conditions, Oper. Res. 61 (2013) 17–31, https://doi.org/10.1287/opre.1120.1128.

[7] X. Bai, A mathematical framework for data quality management in enterprise sys tems, Informs J. Comput. 24 (2011) 648–664, https://doi.org/10.1287/ijoc.1110. 0475.

[8] X. Bai, R. Krishnan, R. Padman, H.J. Wang, On risk management with information flows in business processes, Inf. Syst. Res. 24 (2013) 731–749, https://doi.org/10. 1287/isre.1120.0450.

[9] S. Moore, Poor quality data weakens an organization's competitive standing and undermines critical business objectives, (2018). https://www.gartner.com smarterwithgartner/how-to-stop-data-quality-undermining-your-business (accessed April 27, 2020).

[10] X. Bai, M. Nunez, J.R. Kalagnanam, Managing data quality risk in accounting information systems, Inf. Syst. Res. 23 (2012) 453–473, https://doi.org/10.1287/isre. 1110.0371.

[11] Z. Song, Y. Sun, J. Wan, P. Liang, Data quality management for service-oriented manufacturing cyber-physical systems, Comput. Electr. Eng. 64 (2017) 1339–1351, https://doi.org/10.1016/j.compeleceng.2016.08.010.

[12] R.Y. Wang, A product perspective on total data quality management, Commun. ACM 41 (1998) 58–65, https://doi.org/10.1145/269012.269022.

[13] R. Taymanov, K. Sapozhnikova, A. Ionov, Topical metrology problems in the era of cyber-physical systems and internet of things, in: 18th Int. Congr. Metrol., EDP Sciences, 2017: p. 09006. doi: https://doi.org/10.1051/metrology/201709006.

[14] C. Batini, M. Scannapieco, Concept, Methodologies and Techniques, Springer, Berlin, 2006, https://doi.org/10.1007/3-540-33173-5\_1.

[15] R.Y. Wang, Beyond accuracy: what data quality means to data consumers, J. Manag. Inf. Syst. 12 (1996) 5–34, https://doi.org/10.1080/07421222.1996.11518099.

[16] G.K. Tayi, D.P. Ballou, Examining Data Quality, Commun. ACM 41 (1998) 54–57, https://doi.org/10.1145/269012.269021.

[17] A. Parssian, S. Sarkar, V.S. Jacob, Impact of the union and diference operations on the quality of information products, Inf. Syst. Res. 20 (2009) 99–120, https://doi. org/10.1287/isre.1070.0161.

[18] J. Tanevski, N. Simidjievski, L. Todorovski, S. Džeroski, Process-based modeling and design of dynamical systems, in: Lect. Notes Comput. Sci. (Including Subser. Lect. Notes Artif. Intell. Lect. Notes Bioinformatics), 2017: pp. 378–382. doi:https://doi.org/10.1007/978-3-319-71273-4\_35.

[19] J.A. Cecil, K. Srihari, C.R. Emerson, A review of petri-net applications in manufacturing, Int. J. Adv. Manuf. Technol. 7 (1992) 168–177, https://doi.org/10.1007 BF02601620.

[20] J.F. Aubry, N. Brinzei, M.H. Mazouni, Systems Dependability Assessment: Benefits of Petri Net Models, 2016. doi: https://doi.org/10.1002/9781119262114.

[21] B.S.S. Onggo, N.C. Proudlove, S.A. D’Ambrogio, A. Calabrese, S. Bisogno, N. Levialdi Ghiron, A BPMN extension to support discrete-event simulation for healthcare applications: an explicit representation of queues, attributes and datadriven decision points, J. Oper. Res. Soc. 69 (2018) 788–802, https://doi.org/10. 1057/s41274-017-0267-7.

[22] R.S. Aguilar-Savén, Business process modelling: review and framework, Int. J. Prod. Econ. 90 (2004).129–149, https://doi.org/10.1016/S0925-5273(03)00102-6

[23] J. Du, L. Zhou, Improving financial data quality using ontologies, Decis. Support Syst. 54 (2012) 76–86, https://doi.org/10.1016/j.dss.2012.04.016.

[24] Q. Liu, G. Feng, N. Wang, G.K. Tayi, A multi-objective model for discovering highquality knowledge based on data quality and prior knowledge, Inf. Syst. Front. 20 (2018) 401–416, https://doi.org/10.1007/s10796-016-9690-6.

[25] X. Xu, Y. Lei, Z. Li, An incorrect data detection method for big data cleaning of machinery condition monitoring, IEEE Trans. Ind. Electron. 67 (2020) 2326–2336, https://doi.org/10.1109/TIE.2019.2903774.

[26] G. Shankaranarayan, M. Ziad, R.Y. Wang, Managing data quality in dynamic de cision environments: an information product approach, J. Database Manag. 14 (2003) 14–32, https://doi.org/10.4018/jdm.2003100102.

[27] C. Batini, C. Cappiello, C. Francalanci, A. Maurino, Methodologies for data quality assessment and improvement, ACM Comput. Surv. 41 (2009) 1–52, https://doi.org 10.1145/1541880.1541883

[28] R.C. Aster, B. Borchers, C.H. Thurber, Parameter Estimation and Inverse Problems (2013). doi:https://doi.org/10.1016/C2009-0-61134-X.

[29] P. Glowalla, A. Sunyaev, Process-driven data quality management: a critical review on the application of process modeling languages, J. Data Inf. Qual. 5 (2014), https://doi.org/10.1145/2629568

Qi Liu is a Research Associate of Research Center of China Economic Reform Innovation and Assessment at the School of Management, Xi'an Jiaotong University, P. R. of China. He obtained his Ph.D. from Xi'an Jiaotong University. His research interests include in formation system management, big data, data quality and information sharing in supply chains. He has been published his research results in the journals such as Information Systems Frontiers.

Gengzhong Feng is a Professor of Information Management and EBusiness at the School of Management, Xi'an Jiaotong University, P. R. of China. He obtained the B.S. degree in computer science in 1987, the M.S. degree in systems engineering in 1990, and the Ph.D. degree in management engineering in 1993, all from Xi'an Jiaotong University of China. His research interests include logistics and supply chain management, information system management, big data and information quality. His research has been published in the journals such as Journal of the Association for Information Systems, European Journal of Operational Research, Omega-International Journal of Management Science, International Journal of Production Research and Expert Systems with Applications.

Xi Zhao is a Professor of Information Management and EBusiness at the School of Management, Xi'an Jiaotong University, P. R. of China. He has published more than 50 articles in the interdisciplinary fields of information systems, artificial intelligence, data mining, psychology, and big data behavior and decision-making. Such as IEEE TPAMI, IEEE TCybernatics, DSS and TM.

Wenlong Wang received his Ph.D. degree in business management from Xi'an Jiaotong University. Xi'an. China, in 2018. After graduation. he holds the position of Postdoctoral Research in Xi'an University of Architecture and Technology. His research interests in clude supply chain management and innovation.
