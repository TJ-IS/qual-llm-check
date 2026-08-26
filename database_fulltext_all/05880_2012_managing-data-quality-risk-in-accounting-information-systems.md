---
otero_id: 5880
otero_key: "KPZWGQQV"
title: "Managing Data Quality Risk in Accounting Information Systems"
authors: "Xue Bai; Manuel Nunez; Jayant R. Kalagnanam"
year: "2012"
journal: "Information Systems Research"
doi: "10.1287/isre.1110.0371"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [132.177.228.65] On: 04 March 2015, At: 16:06 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

# Information Systems Research

## HSR

![](/api/attachments/KPZWGQQV/fulltext/images/fce2d9866226faeb9af512beb5eb37552d2b2f5725d9a55b7f2f929d95cf8355.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Managing Data Quality Risk in Accounting Information Systems

Xue Bai, Manuel Nunez, Jayant R. Kalagnanam,

To cite this article:

Xue Bai, Manuel Nunez, Jayant R. Kalagnanam, (2012) Managing Data Quality Risk in Accounting Information Systems. Information Systems Research 23(2):453-473. http://dx.doi.org/10.1287/isre.1110.0371

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2012, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/KPZWGQQV/fulltext/images/12f4750e1293c3c4e405b26a569c5f073b4309bce26ba603276cdb3e723010ea.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Managing Data Quality Risk in Accounting Information Systems

Xue Bai, Manuel Nunez

Department of Operations and Information Management, School of Business, University of Connecticut, Storrs, Connecticut 06269 {xue.bai@business.uconn.edu, manuel.nunez@business.uconn.edu}

Jayant R. Kalagnanam IBM T. J. Watson Research Center, Yorktown Heights, New York 10598, jayant@us.ibm.com

he quality of data contained in accounting information systems has a significant impact on both internal Tbusiness decision making and external regulatory compliance. Although a considerable body of literature exists on the issue of data quality, there has been little research done at the task level of a business process to develop effective control strategies to mitigate data quality risks. In this paper, we present a methodology for managing the risks associated with the quality of data in accounting information systems. This methodology first models the error evolution process in transactional data flow as a dynamical process; it then finds optimal control policies at the task level to mitigate the data quality-related risks using a Markov decision process model with risk constraints. The proposed Markov decision methodology facilitates the modeling of multiple dimensions of error dependence, captures the correlated impact among control procedures, and identifies an optimal control policy. A revenue realization process of an international production company is used to illustrate this methodology.

Key words: data quality; risk; audit; control; accounting information systems; constrained Markov decision processes

History: Alok Gupta, Senior Editor; Vijay Mookerjee, Associate Editor. This paper was received on September 16, 2008, and was with the authors 11 months for 3 revisions. Published online in Articles in Advance June 16, 2011.

## 1. Introduction

The importance of the quality of data in accounting information systems has long been recognized (Cushing 1974, Ham et al. 1985, Lea et al. 1992, Nado et al. 1996, Krishnan et al. 2005). According to research by Gartner, Inc. (Moore 2007), more than 25% of critical data in the world’s top companies are and will continue to be flawed—that is, inaccurate, incomplete, or duplicated—over the next several years. In 2002, the Sarbanes-Oxley Act was passed in response to a number of high-profile financial scandals in corporate America that resulted in billions of dollars of losses for investors. Sarbanes-Oxley requires CEOs and CFOs of all public companies not only to certify the reliability and integrity of both financial reports and the information systems that produced these reports, but also to establish, maintain, and routinely evaluate an internal control system for financial reporting. The high cost of clean data has been ranked as one of the top barriers to strategic business plans (Richter 2007) by 75% of the CIOs of major public companies in North America and Europe. For instance, Krishnan et al. (2008) found that the mean and the median total annual costs of compliance to Sarbanes-Oxley Section 404 per enterprise are \$2.2 million and \$1.2 million, respectively, with even higher figures for companies that had disclosed internal control problems in the previous year, creating a vicious cycle (Hoitash et al. 2008). Similar data quality risk issues have arisen in the health care sector. For instance, the Institute of Medicine reports that medication errors injure 1.5 million people and cost billions of dollars annually (Bootman et al. 2007). Patient safety as a casualty of data flaws has emerged as a national concern, as first attested by a widely publicized report on errors in health care systems from the National Academy Press (Kohn et al. 2000), and has since become a major issue in the health care sector across nations (Pittetl and Donaldson 2006).

Poor quality data leads to potential monetary loss, legal penalties, and operational inefficiencies. We define these negative impacts caused by flawed data as the data quality risks (Marinos 2004). For instance, corporations can experience lost revenue from overpayments, or discounts lost to lack of consistency on payment terms. Missing payment and sales information can severely undermine vendor contract negotiation, contract compliance monitoring, and managerial reporting. Fraudulent financial statements may lead to legal penalties. Inaccurate and incomplete transactional data result in efforts and resources diverted to inquiry and reporting functions. Inaccuracies in customer records can have a negative impact on customer service and customer satisfaction. Assuring high-quality data by mitigating data quality risks has emerged as one of the important priorities for executives across industries.

A considerable body of literature exists on the issue of data quality assessment in the accounting literature and the information systems literature. However, most work in the accounting literature has approached data quality assessment by viewing the accounting information system as a “black box” that transforms raw data into outcome information and performance metrics (Cushing 1974, Ham et al. 1985, Lea et al. 1992, Nado et al. 1996). All these studies have focused on developing metrics for ex post estimation of the accounting information quality by looking at the aggregated accounting data in various ledgers (Knechel 1985). This approach works well from the perspective of an auditor who is interested in assessing the reliability with which the accounting information system performs at the aggregate level. Because the transactional data in a business process are actually produced and transformed at the task level, a task-level approach to data quality control would be more effective and practical than the traditional “black box” approach. In other words, tasks are the potential sources of both error introduction and error propagation. Control strategies developed at the task level are able to mitigate the data quality risks at the root causes by eliminating the sources of the introduction and propagation of data errors.

Similarly, research in information systems literature has also approached data quality issues by viewing the system as a whole. Earlier work in information systems has focused on the identification of the important characteristics that define the quality of data (Wand and Wang 1996, Wang 1998). The practical issue of data quality assurance in business processes has only recently been identified as a critical problem (Krishnan et al. 2005, Bagchi et al. 2006, Sun et al. 2006, Bai et al. 2007). Most of the existing work describes the conceptual criteria necessary for the information systems design to improve or achieve good data quality. To the best of our knowledge, there has been no research done at the task level, examining how poor data quality impacts both operational activities and strategic initiatives. We consider these issues to be critical from the practical perspective of business control framework design and data quality management.

## 1.1. Research Overview

This research adopts key concepts and definitions of data quality from the accounting and information systems literature, develops a modeling framework that enables mathematical formulations to compute optimal control policies at the task level of a business process, and ultimately achieves data quality risk management objectives in accounting information systems. Finding optimal control strategies at the task level poses several challenges. First, errors may be introduced by different tasks in the information flow from mistakes, omissions, delays, software glitches, or fraud. Tasks are dependent on each other by the nature of the task operations and resources involved, as well as by their execution sequences. Second, error instances may affect different aspects of transactional data. These aspects are enumerated in different error classes in the accounting literature (Lea et al. 1992). For instance, missing payment information is categorized as a completeness error; duplicated order information is considered as an existence error; and a numerical inaccuracy in customer records is considered as a valuation error. Therefore, the occurrence of error instances can be correlated across both tasks and error classes. Third, control procedures that are designed to prevent, detect, and correct the errors in the information flow may have different implications for error detection and reduction capabilities, depending on deployment location. Furthermore, the effectiveness of control procedures may vary and be correlated with multiple tasks when applied or combined with other procedures.

In this paper, we propose a constrained Markov decision model to mitigate data quality risks in accounting information systems. The model identifies an optimal, task-level control policy to meet the target risk while minimizing the cost. Our approach is novel in the following dimensions. First, it separately models the two evolutionary aspects of errors, error growth over time periods and error propagation among tasks within a time period. Second, it distinguishes the two functional components of the data quality control mechanism: audit and control, where auditing is a mandated step in public accounting systems (ISACA 2007) and control decisions are specific, resource-requiring actions to be optimized. Third, our model extends the basic formulations of constrained Markov decision models—by including the damping control element—that have been successfully applied to risk management in finance and manufacturing. To the best of our knowledge, this is the first attempt at managing data quality risk in accounting information systems and enterprise systems in general.

The Markov decision approach suits our problem setting well: it captures the error introduction and propagation dynamics in the transaction data flow; it accommodates error dependence, including the correlation among error classes and the dependence through task relations; it takes into consideration the correlated impact among control procedures across tasks; and it finds an optimal stationary control policy. Such a policy requires a single deployment of business controls over multiple periods of time; hence, control resources, such as personnel, can be chosen well in advance for a planned time horizon. In practice, a single deployment of control resources is desirable, as it is more cost-effective and easier to implement than time-dependent control policies.

Our research makes methodological contributions. From a process-modeling perspective, our model extends the formal, process-oriented ontology of an accounting information system introduced by Krishnan et al. (2005) by including attributes about error introduction and propagation dynamics at the task level, along with the cost and effectiveness of control procedures. This extension enables quantitative assessments of risks associated with data errors and design of optimal control policies that meet the targeted risk threshold at minimum cost. From a data quality risk perspective, our research represents a first attempt to address data quality risks at the root causes, by eliminating error introduction and propagation sources, ultimately mitigating the risk. Our methodology synthesizes research from previous literature on data quality to provide a practical framework for managing data quality-associated risks. As such, we respond to the general call for more research on data quality risks in enterprise systems from both research and practice.

## 1.2. Outline

The remainder of the paper is organized as follows. Section 2 surveys relevant literature. Section 3 introduces the process model that represents the structure of a business process, the characteristics of the flow of information and errors therein, and the control mechanisms for detecting and reducing errors. An illustrative example of a revenue realization process is introduced in this section. Section 4 introduces a Markov model for the error generation and propagation through the system and the error accumulation in the target measures. A Markov decision process model with risk constraints is developed to control errors in the key performance indicators (KPIs) in enterprises. We develop an linear programming (LP) formulation for solving the model. Section 5 applies the model to a revenue realization process of an international production company, and discusses computational results. We conclude in §6 with a discussion of additional applications and future directions.

## 2. Relevant Work

Two streams of literature on data quality are relevant to our study: the accounting literature and the information systems literature. We discuss them here and highlight our contributions to each piece of the relevant work respectively.

## 2.1. The Definition of Data Quality

The concept of data quality has originally been defined from the perspective of accuracy. Recent research has identified data quality as encompassing multiple dimensions (Huang et al. 1999). Though there is no uniform standard definition in the data quality research literature, the general definition of quality data is “data that are fit for use by data consumers.” Wang and Strong (1996) formally introduced a set of data quality dimensions that have been commonly accepted: accuracy, completeness, consistency, timeliness, believability, and security. Strong et al. (1997) presented a set of data quality dimensions that consists of not only the intrinsic data quality, such as accuracy, completeness, and consistency, but also the quality metrics from a data-consumer perspective. The consumer-centric metrics include user accessibility, contextual quality, and representational quality. They argued that data quality assessment should incorporate the task context of users and the processes by which users access and manipulate data to meet their task requirements. Pipino et al. (2002) introduced three functional forms of data quality: simple ratio, min or max operators, and weighted average. Based on these functional forms, they developed the illustrative metrics for important data quality dimensions and presented an approach that combines the subjective and objective assessments of data quality, demonstrating how the approach can be used effectively in practice.

The accounting information system is seen as a subsystem of the management information system. The major function of an accounting information system is to process financial transactions, as well as nonfinancial transactions that directly affect the processing of financial transactions (Siegel and Shim 1998, Hall 1998). In accounting systems, where internal control systems require maximum reliability of data at minimum cost, the key data quality dimensions have been identified by Ballou and Pazer (1985) and Ballou et al. (1993) to consist of completeness, existence, valuation, presentation and disclosure, and rights and obligations. These five dimensions have been reasonably widely accepted in the accounting literature. Therefore, data quality in this paper refers to these five dimensions, which are formally defined in §5.1.3.

## 2.2. Data Quality in Accounting Literature

The literature in accounting has studied the assessment of data quality and control since the early 1970s (Cushing 1974, Ham et al. 1985, Lea et al. 1992, Nado et al. 1996). Cushing (1974) was the first to develop a mathematical formulation for measuring the reliability of an accounting system. He used the probability that the system makes no output errors of any kind as the measure of system reliability. From that he derived a measure taking into consideration both the cost of executing error correction controls and the risk of undetected errors in the system. Cushing’s control model, however, considered the control allocations as fixed, and it did not provide solutions to meet a threshold reliability measure with cost constraints. Our research adopts the same basic concept of reliability proposed in his work, but further extends it to address the issue of data quality risk management.

Ham et al. (1985) conducted an empirical study of the error characteristics in accounting systems across industries. The study focused on the empirical distributions of two types of error rates: those that are defined in terms of the frequency of erroneous transactions and those defined in terms of the magnitude of erroneous monetary value, or taint. We adopt the concept of taint to measure the magnitude of the errors in our model.

Lea et al. (1992) studied how risks of error at the level of the various transaction streams, which are related to the risk of error at the account balance level to which these streams contribute. Our model adopts their idea of decomposing an account balance into its constituent transaction streams and extends their simple model framework to include (a) the volume of transactions in the various streams and (b) the stochastic aspects of error evolution through a Markov process. These extensions allow us to account for the accumulated impact of errors in the various transaction streams over time.

Nado et al. (1996) developed a process-based reasoning system, COMET, to analyze the effectiveness of control systems. The accounting system was modeled as a hierarchically structured graph, with nodes representing the transaction processing activities and collection points. The work studied the “potential for failure” in each activity that affects the accounting ledgers. Controls were modeled in terms of the probability of a control not being able to cover the failures. However, the model focused only on the probability of system failure and implicitly assumed identical and fixed costs for all controls. Our model adopts the basic process-modeling concepts introduced in their work and extends them to develop a quantitative framework.

## 2.3. Data Quality in Information Systems Literature

Traditional research on data quality in information systems literature has focused on the theoretical characteristics that define the quality of data (Wand and

Wang 1996, Wang 1998). Recent studies have developed ontological models and artifacts that are necessary from a systems design perspective to improve or achieve good data quality (Krishnan et al. 2005, Sun et al. 2006).

Wand and Wang (1996) studied data quality in the context of information systems design. Their work suggests rigorous definitions of data quality dimensions by anchoring the analyses of quality in ontological foundations. They demonstrated that such dimensions can provide guidance to systems designers on data quality issues.

Wang (1998) developed a Total Data Quality Management methodology. This methodology presents a set of concepts, principles, and procedures for Total Data Quality Management. Wang (1998) illustrated how this methodology can be applied in practice to facilitate the implementation of an organization’s overall data quality policy as formally expressed by top management.

Sun et al. (2006) developed a model for detecting such data flow anomalies as missing or redundant data and potential data conflicts in business processes. Their model includes two components: data flow specification and data flow analysis. These components expand existing analytical tools for business process management by enabling the systematic detection of data flow errors in a workflow model.

Krishnan et al. (2005) developed a process-level notation set for accounting information systems and demonstrated how this notation could be used to support audit and control planning using a set-covering decision model. We adopt their modeling elements about accounting systems in order to characterize quantitative attributes of the flow of transactions, the stochastic nature of error introduction events at the level of tasks, and the cost and effectiveness of control procedures that are placed to detect and correct errors. This modeling framework enables both quantitative assessments of data quality related risks and control policy optimization.

## 3. Business Processes

Our model adopts the process-oriented ontology of an accounting information system developed in Krishnan et al. (2005), because it is simple but provides essential modeling constructs for quantitative analysis of error dynamics and the risk associated with errors in the information flow. We extend the ontology by introducing the following elements: transaction sources, error sources, audit targets, audits, and controls. A network of links connects the transaction sources, error sources, and audit targets. Control systems are implemented at the error sources to reduce the incidence of errors and ultimately the risks to data quality. This network representation of a business process provides the basic structure from which we develop the modeling framework for data quality risk management. Next, we use a revenue realization process as the illustrative example to introduce the elements of our process model. The revenue realization process example will be used as the illustrative example throughout the rest of the paper.

Figure 1 The High-Level Modeling Diagram of the Revenue Realization Process  
![](/api/attachments/KPZWGQQV/fulltext/images/03f7d0ab61882ece390f3ee402b4ce1858550036b6b255ef3069723d93f00985.jpg)

## 3.1. Illustrative Case: A Revenue Realization Process

As an example of a business process, consider a revenue realization process of an international production company (Figure 1). Figure 1 shows the diagram of the high-level process. There are six subprocesses in the process: “sales,” “contract establishment,” “order management,” “contract update,” “backlog management,” and “revenue realization.” The links between these subprocesses represent the flows of transactional data. The fully expanded diagram is available on request.

3.1.1. Transaction Sources. The revenue process is initiated by a client’s request for a quotation, which is the transaction source of the process. A starting event in a process is labeled as a transaction source. This is the origination point of a transaction in which an error has not yet been introduced.

3.1.2. Error Sources. After a request is received, the process begins. Each individual transaction flows through the six subprocesses, as shown in Figure 1. The tasks in each subprocess may be potential error sources. An error source is a task that operates on a transaction and may introduce errors into the transactional data with certain probabilities. The data contained in each transaction have multiple dimensions. For example, in a purchase order, the data dimensions include “product name,” “quantity ordered,” “unit price,” “shipping time,” and “payment options.” We define an error as any difference between the actual value and the recorded value in any dimension of the transactional data. The definition includes cases in which transactions are lost or spurious transactions are introduced.

3.1.3. Audit Targets. Transactional data and business information are stored in information repositories of the enterprise system. An audit target is an information repository in the business process where transactions can be stored and retrieved. They could be accounting ledgers that contain financial data that are aggregated into KPIs and used by the company in its decision making. They could also be used to generate quarterly and annual financial reports for such external parties as shareholders and regulatory agencies. In the revenue realization process, a transaction eventually reaches the “general ledger” and “accounts receivables,” which are the audit targets. As shown in Figure 1, the two audit targets are at the right end of the diagram. As the figure suggests, an error introduced at a single source may propagate and reach multiple audit targets. A single audit target may contain errors introduced by multiple error sources.

3.1.4. Audits. Internal audits are mandated procedures performed in each auditing period to estimate data quality matrices at the audit targets. Examples of audit procedures include the KPI assessment and performance reviews (ISACA 2007). The purpose of audits is to assess the potential risk due to data errors and provide data quality indicators for managers. Appropriate control decisions are then made based on the audited results and control policies. An effective audit system is able to monitor transactions, observe error states, provide accurate information for control decisions, and ultimately maintain process performance.

Figure 2 The Graphical Representation of the Revenue Realization Process  
![](/api/attachments/KPZWGQQV/fulltext/images/cbc750ec989bd422a6c7fcf913736d777eedc6ce700d7678c361106312ae9f79.jpg)  
Note. The S node denotes the transaction source and the $T _ { 1 : 2 }$ nodes denote the two audit targets. The six subprocesses are organized into columns.

3.1.5. Controls. Control procedures are applied to identify and correct errors at error sources when the control policy recommends a control action, and ultimately mitigate the risk associated with errors in the transactional data flow. Typically, a business process has a range of available control procedures. Examples of control procedures include manual or automated checks, restricted access, or segregation of duties (ISACA 2007). The control procedures working together may be able to cover all the possible error types and eventually achieve risk mitigation. Our study focuses on information transformation-related controls.

An error source that allows the placement of at least one control procedure is a feasible control location. Error reduction may be achieved by sending an erroneous transaction back to an earlier point where the error was introduced, for reprocessing, or by fixing errors directly at the control point. Three types of control procedures are commonly used in control practice (COSO 2004, ISACA 2007). Preventive controls are applied to prevent errors from being introduced. Feed-forward controls are applied to detect and correct errors after they have been introduced at previous error sources. Feedback controls only report errors without correcting them. Our work focuses on preventive controls and feed-forward controls, as these two types of controls have direct error reduction and cost implications.

3.1.6. Risk Management Objective. The objective of data quality risk management in the revenue realization process is to ensure that the correct amount of revenue is realized in the right ledgers for the right fiscal period. The accuracy of this information is critical not only for external purposes, such as meeting the financial reporting obligation of public companies, but also for internal purposes in various departments, such as the sales division that views this information on business dashboards and makes tactical sales decisions involving promotions, discounts, and channel management.

## 3.2. Graphic Representation of Business Processes

Our graphic representation of a business process is as follows: the process is modeled as a directed graph. A node in the graph represents a transaction source, a task that is a potential error source, or an audit target. A directed arc between two nodes represents the flow of transactional data from one task to another. Some of the nodes may also be subprocesses that may be expanded into their own directed graphs. The graphs may be cyclic as well as hierarchical. Our research focuses on the information flow and data transformation aspects of a process.

Figure 2 shows the graphical representation of the revenue realization process in Figure 1. (The description of each task is detailed in Table 4 in the case study.) In the diagram, the gray node at the starting point represents the transaction source, and the two endpoints represent the two information repositories, which in our case are the “general ledger” and the “accounts receivables.” These two ledgers are the audit targets. The nodes that are located between transaction sources and information repositories in a process graph represent the tasks that are potentially error sources. The simple graphic representation is then extended to permit nodes and arcs with attributes such as error variances. Later, when control actions are introduced, the model is further extended to include attributes of control policies at each task.

## 3.3. Path Relations of Information Flow

A volume of transaction data originating from transaction sources flows through the process. For a business process with S transaction sources, I tasks that are error sources, and J information repositories that are assigned to be the audit targets, we develop the information volume transition matrix V to model the path relations of the information flow. The V matrix is an $( S + I + J ) \times ( S + I + J )$ -dimensional matrix. The first S rows and the first S columns represent the transaction sources; the last J rows and the last J columns represent the information repositories. An entry of $V , \ v _ { s i }$ represents the volume ratio between the outflow of the transaction data from a transaction source s and the inflow of the transaction data to a task i. An entry $v _ { i j }$ represents the volume ratio between the outflow of the transaction data from a task i and the inflow of the transaction data to an audit target j. The entries in V are used to compute the error propagation in the error dynamical model in §4. An online appendix<sup>1</sup> demonstrates in detail how the pair-wise parameters in V are able to model information flows in various workflow patterns.

Next, we use a simple order management process to illustrate how the information volume transition matrix is computed.

3.3.1. Example: An Order Management Process. Consider a simple order management process. It consists of three tasks that work together to achieve the order management function. The description for the three tasks is in Table 1. The process is triggered by a client placing an order for medication. The information in this order is processed by three tasks in the order management process and stored in the order database. Figure 3 shows the diagrams of the order management process that represent two different scenarios of information flows in the order management process.

Consider a volume of orders being placed within a fixed time period (for example, monthly orders). Some of the orders may come from existing clients and others from new clients for whom new accounts need to be created. Orders from the new clients are processed differently in the two scenarios. Let $V _ { 1 }$ be the volume transition matrix of Scenario 1 and $V _ { 2 }$ be the volume transition matrix of Scenario 2. Suppose 20% of the monthly orders are new clients’ orders in both scenarios. In Scenario 1 (the process graph on the left), the order management system needs to acquire the insurance information and billing information (task 2) before checking the credit history (task 3). The process pathway is $t _ { 1 }  t _ { 2 }  t _ { 3 } $ database. In Scenario 2 (the process graph on the right), the orders from new clients are sent to tasks 2 and 3 simultaneously: the insurance information and billing information are acquired (task 2) at the same time that the credit is checked (task 3). Two process pathways for an order of a new client are $t _ { 1 } \bar {  } t _ { 2 }  \bar { t } _ { 3 } $ database and $t _ { 1 }  t _ { 3 } $ database. At each task, a copy of the order is registered in the work log. Orders from an existing client are processed the same way: task 2 is skipped and the process pathway is $t _ { 1 }  t _ { 3 } $ database. The two volume transition matrices corresponding to the two diagrams in Figure 3 are $V _ { 1 }$ and $V _ { 2 }$

Table 1 Task Descriptions in the Order Management Process

<table><tr><td>Task number</td><td>Task description</td></tr><tr><td>Task 1</td><td>Enter order information.</td></tr><tr><td>Task 2</td><td>Set up an account; i.e., establish insurance and billing information for a new client.</td></tr><tr><td>Task 3</td><td>Check credit status; enter valid orders into the database.</td></tr><tr><td>Audit target</td><td>Order databases.</td></tr></table>

$$
V _ {1} = \left[ \begin{array}{c c c c c} 0 & 1 & 0 & 0 & 0 \\ 0 & 0 & 0. 2 & 0. 8 & 0 \\ 0 & 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 & 0 \end{array} \right], \quad V _ {2} = \left[ \begin{array}{c c c c c} 0 & 1 & 0 & 0 & 0 \\ 0 & 0 & 0. 2 & 1 & 0 \\ 0 & 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 & 0 \end{array} \right].
$$

The only cell entry that is different between $V _ { 1 }$ and $V _ { 2 }$ is the one at row 2, column 4; $V _ { 1 } ( 2 , 4 ) = 0 . 8$ indicates that only orders from the existing clients go directly from task 1 to task 3 (Scenario 1). $V _ { 2 } ( 2 , 4 ) =$ 1 indicates that all the orders, regardless the clients’ history, go directly from task 1 to task 3 (Scenario 2). The volume transition matrix V is used in Section 4 to compute the cumulated error variances through propagation.

## 4. Model Formulation

In this section, we develop a dynamic model of the error evolution over time periods and a model of error propagation within a time period. Using this framework, we establish a constrained Markov decision process (CMDP) to determine an optimal control policy that minimizes expected discounted control cost while keeping expected discounted risk below a given threshold. Finally, we formulate a linear program to find an optimal stationary policy for the CMDP.

## 4.1. Dynamic Model for Error

In the dynamic model, audit and control are treated as two separate procedures. Audit procedures monitor transactions, observe error states in the audit targets,

## Figure 3 Two Scenarios of the Information Flow Patterns and the Corresponding Volume Transition Parameters in the Order Management Subprocess (Described in Table 1)

![](/api/attachments/KPZWGQQV/fulltext/images/3875e8b8b121468b21e04e3f53cc6914f9fb238e77568b2e8ff917c88f5c8bde.jpg)  
Note. Left: Scenario 1; Right: Scenario 2.

and provide information for control decisions. However, audit procedures do not take actions to retrieve errors at the error source and correct the errors. Controls take actions at the error sources to identify and correct errors. Controls have associated cost and risk reduction implications and are generally more expensive than audits. Hence, in our setting we assume that the company can afford periodic audits, but controls can only be sparingly applied. In other words, at the end of a time period, audits are always conducted, whereas applying controls is a case-by-case decision.

We consider a dynamic system in which an audit is executed after a time period and then, depending on an error state, a decision is made to apply or not apply a control to fix the errors. A time period is a constant time interval (daily, weekly, monthly, or annual, etc.), at the end of which the firm always performs the audits. An error in our setting is defined as a discrepancy between the recorded information and the actual information in the transactional data that will result in a misstatement in the accounting ledgers. The idea of postponing the application of control procedures to correct errors has been studied in the software development field (Ji et al. 2005), but as far as we know, this idea has not been explored in the accounting domain.

Concretely, suppose that Q transactions arrive and are processed at node i between times t 1 and t. At time t those transactions are audited and their recorded values $\hat { y } _ { q } , \ q = 1 , \ldots , Q ,$ , are observed and compared to their corresponding true book values $y _ { q } .$ We consider the difference between $\hat { y } _ { q }$ and $y _ { q }$ an error, that is,

$$
\hat {y} _ {q} - y _ {q} = \gamma_ {q},\tag{1}
$$

where the errors $\gamma _ { q } ,$ for $q = 1 , \ldots , Q ,$ are independent and identically distributed random variables with zero mean and common variance denote by $\tau _ { i } ^ { 2 } .$

For the case of the revenue realization process, we use the notion of taint from the accounting literature to define the magnitude of the errors (Ham et al. 1985) introduced in one period. The taint by an error in a single transaction is defined as the the absolute difference between the recorded book value and the actual book value. Taint is an important measure of data quality and an informative indicator of risk associated with data quality. Intuitively, the greater in magnitude and variance the taints are, the less reliable the data are, and therefore, the higher the risk of bad corporate decisions based on unreliable business performance data that are aggregated from erroneous data at the transaction level. We formally define the taint between times t 1 and t at node i as

![](/api/attachments/KPZWGQQV/fulltext/images/6f9923b1dc12b6f7df707a93c7904a79d93bbdc846846197fb1d5b76d9dd1e19.jpg)

$$
\rho_ {i} := \frac {1}{Q} \sum_ {q = 1} ^ {Q} \frac {| \hat {y} _ {q} - y _ {q} |}{y _ {q}} = \frac {1}{Q} \sum_ {q = 1} ^ {Q} \frac {| \gamma_ {q} |}{y _ {q}}.\tag{2}
$$

The taint is the average relative error of the transactions processed at a given node, and it accumulates from period to period as long as no control is applied.

If control is applied immediately after the audit to eliminate observed errors, the control action may reduce the accumulated taint. The amount of error reduction will depend on the effectiveness of the control procedure. We summarize the effectiveness of a control procedure at node i by a constant $\beta _ { i } ,$ with $0 \leq$ $\beta _ { i } \leq 1 .$ , where $\beta _ { i }$ is the proportion of errors eliminated by the procedure. Let $\epsilon _ { i } ( t )$ be the accumulated taint up to time t at node $i ,$ and let $\theta _ { i } ( t ) = 1 - \beta _ { i }$ if control is applied at node i at time t and $\theta _ { i } ( t ) = 1$ otherwise. We assume $\epsilon _ { i } ( 0 ) = 0$ for all i. After incorporating controls, we obtain

$$
\epsilon_ {i} (t + 1) = \epsilon_ {i} (t) + \theta_ {i} (t) \rho_ {i}.\tag{3}
$$

4.2. Error Propagation Within a Time Period Within a time period, a continuous volume of transactions flows through the process. For instance, in the revenue realization process in Figure 1, the average volume of monthly orders is 1,200. Therefore, there is a continuous flow of transactions among tasks in the process within a time period. Errors propagate from one task to another as an erroneous transaction moves from one task to another. We define the movement that a single transaction makes from one task to another as a process step. Next we explain how the errors propagate through process steps during a time period.

Figure 4 A Simple Task Network  
![](/api/attachments/KPZWGQQV/fulltext/images/23548b0310fa417d1fc0134447fd92c96c3be365970a89ad3703888b54724aa3.jpg)

We model a business process as a directed graph $( N , A )$ with node set $N { \overset { - } { = } } \left\{ 1 , \dots , n \right\}$ and arc set $A \subset$ $N \times N$ . Nodes represent tasks in the process. Arcs represent information flow between tasks. We denote by $V = [ v _ { i j } ]$ the volume transition matrix and assume that $v _ { i j } > \dot { 0 }$ for $( i , j ) \in A$ and $v _ { i j } = 0$ for $( i , j ) \notin A$ . We denote by $\mathcal { V } ( i )$ the set of nodes that directly flow in to node $i ;$ that is, $\mathcal { V } ( i ) = \{ j : ( j , i ) \in A \}$ . The value of $v _ { i j }$ can also be interpreted as the probability that a transaction processed at node i will flow to node j.

The error $\gamma _ { i q }$ of transaction q at node i is a combination of an intrinsic error introduced at the node and a propagated error introduced by the immediate previous nodes where the transaction was processed. For example, consider a simple network as depicted in Figure $^ { 4 , }$ where transactions are first processed at task 1 and then, on the average, 70% of them go to be further processed at task 2 and 30% exit the system. We take a sample of 10 transactions processed during the same time period. Table 2 shows the sample results after being processed at task 1. Notice that in four of the transactions, an error of one unit was introduced, representing at most 0.66% relative error each. The average taint (average of the relative errors) of the 10 transactions is 0.23% at task 1.

Table 3 illustrates the final value of the transactions after either flowing to task 2 or out of the system. In the table, transactions 1, 4, 5, 7, 8, 9, and 10 flowed from task 1 to task 2. We assume that when a transaction goes from task 1 to task 2, a new value is computed at task 2 and then added to the transaction value computed at task 1. The table shows the intrinsic errors introduced at task 2 when computing the new values, the errors propagated from task 1, and the final errors from combining the two values for each transaction. The last column of Table 3 shows the overall relative errors at task 2, with a corresponding average taint of 0.25%, slightly higher than at task 1 even though only two of the new values computed at task 2 had intrinsic errors.

Table 2 Sample of Transactions After Processed at Task 1

<table><tr><td>Transaction</td><td>Observed value</td><td>True value</td><td>Relative error (%)</td></tr><tr><td>1</td><td>154</td><td>154</td><td>0.00</td></tr><tr><td>2</td><td>196</td><td>195</td><td>0.51</td></tr><tr><td>3</td><td>153</td><td>152</td><td>0.66</td></tr><tr><td>4</td><td>158</td><td>158</td><td>0.00</td></tr><tr><td>5</td><td>195</td><td>195</td><td>0.00</td></tr><tr><td>6</td><td>161</td><td>161</td><td>0.00</td></tr><tr><td>7</td><td>163</td><td>164</td><td>0.61</td></tr><tr><td>8</td><td>181</td><td>182</td><td>0.55</td></tr><tr><td>9</td><td>197</td><td>197</td><td>0.00</td></tr><tr><td>10</td><td>152</td><td>152</td><td>0.00</td></tr><tr><td>Average</td><td></td><td></td><td>0.23</td></tr></table>

Table 3 Sample of Transactions After Processed at Task 2

<table><tr><td rowspan="2">Transaction</td><td colspan="2">Introduced by task 2</td><td colspan="2">Propagated task 1</td><td colspan="2">Combined values</td><td rowspan="2">Relative error (%)</td></tr><tr><td>Observed</td><td>True</td><td>Observed</td><td>True</td><td>Observed</td><td>True</td></tr><tr><td>1</td><td>74</td><td>74</td><td>154</td><td>154</td><td>228</td><td>228</td><td>0.00</td></tr><tr><td>2</td><td>54</td><td>54</td><td>0</td><td>0</td><td>54</td><td>54</td><td>0.00</td></tr><tr><td>3</td><td>70</td><td>70</td><td>0</td><td>0</td><td>70</td><td>70</td><td>0.00</td></tr><tr><td>4</td><td>75</td><td>75</td><td>158</td><td>158</td><td>233</td><td>233</td><td>0.00</td></tr><tr><td>5</td><td>62</td><td>62</td><td>195</td><td>195</td><td>257</td><td>257</td><td>0.00</td></tr><tr><td>6</td><td>77</td><td>76</td><td>0</td><td>0</td><td>77</td><td>76</td><td>1.32</td></tr><tr><td>7</td><td>87</td><td>87</td><td>163</td><td>164</td><td>250</td><td>251</td><td>0.40</td></tr><tr><td>8</td><td>74</td><td>75</td><td>181</td><td>182</td><td>255</td><td>257</td><td>0.78</td></tr><tr><td>9</td><td>71</td><td>71</td><td>197</td><td>197</td><td>268</td><td>268</td><td>0.00</td></tr><tr><td>10</td><td>61</td><td>61</td><td>152</td><td>152</td><td>213</td><td>213</td><td>0.00</td></tr><tr><td>Average</td><td></td><td></td><td></td><td></td><td></td><td></td><td>0.25</td></tr></table>

Let $\delta _ { i q }$ denote the intrinsic error of transaction q made at node i. We assume that $\delta _ { i q }$ has zero mean and a variance denoted by $\sigma _ { i } ^ { 2 }$ . The observed error of transaction q at node i is expressed as

$$
\gamma_ {i q} = \delta_ {i q} + \sum_ {j \in \mathcal {V} (i)} v _ {j i} \delta_ {j q}.\tag{4}
$$

Furthermore, we can relate to the variance $\tau _ { i } ^ { 2 }$ of $\gamma _ { i q }$ as follows

$$
\begin{array}{c} \tau_ {i} ^ {2} = \sigma_ {i} ^ {2} + \sum_ {j \in \mathcal {V} (i)} v _ {j i} ^ {2} \sigma_ {j} ^ {2} + \sum_ {j \in \mathcal {V} (i)} v _ {j i} \sigma_ {j i} \\ + \sum_ {j, j ^ {\prime} \in \mathcal {V} (i), j \neq j ^ {\prime}} v _ {j i} v _ {j ^ {\prime} i} \sigma_ {j j ^ {\prime}}, \quad \forall k. \end{array}\tag{5}
$$

In expression (5), $\sigma _ { j j ^ { \prime } }$ is the covariance between the errors at nodes j and j. This is the expression that relates the errors introduced at each task to the errors propagated from preceding tasks and the correlations among these errors (error dependencies).

## 4.3. Constrained Markov Decision Process

We formulate a discrete-time finite-state CMDP to model the stochastic control process for error propagation discussed in the preceding section. The process evolves as follows:

1. At the end of period t 1 (or the beginning of period t), an audit is conducted at the audit targets.

2. For each node $i ,$ the taint $\rho _ { i }$ during the period $t - 1$ and the accumulated taint $\epsilon _ { i } ( t - 1 )$ are computed.

3. The accumulated taint $\epsilon _ { i } ( t - 1 )$ is classified into one of K bins according to its level of severity, where 1 represents no or minimal errors and K represents the most severe errors. The level of severity represents the state of the node.

4. Based on the states of the nodes, a decision is made at each node to apply or not to apply the control procedure associated with the node, that is, the $\theta _ { i } ( t - 1 )$ are computed.

5. If a control procedure is applied at a node, the cost of the procedure is realized.

6. The risk is realized at each node and reduced according to the effectiveness of the control procedure (if any) applied to the node.

7. The process repeats itself beginning with step 1 above.

Next we provide details of each of the features of the CMDP.

4.3.1. State Space. Because the dynamic process concerning the accumulated taints is a continuousstate process, we first discretize the values of that process to obtain a (new) finite-state space. To do so, the accumulated taints $\epsilon _ { i } ( t )$ at node i are observed at time t and classified into K levels of severity, denoted by $1 , \ldots , K ,$ , ranging from no or minimal error (level 1) to very severe error (level K). The state $Z _ { i } ( t )$ of the system at node i at time t represents the level of error severity in the process.

More specifically, if we let $0 = \phi _ { 0 } < \phi _ { 1 } < \cdot \cdot \cdot$ < $\phi _ { K - 1 } < \infty$ be $K ,$ given fixed constants, then $Z _ { i } ( t )$ is determined as follows:

$$
Z _ {i} (t) = \left\{ \begin{array}{l l} 1 & \text {if} \phi_ {0} \leq \epsilon_ {i} (t) <   \phi_ {1}, \\ 2 & \text {if} \phi_ {1} \leq \epsilon_ {i} (t) <   \phi_ {2}, \\ \dots \\ K & \text {if} \phi_ {K - 1} \leq \epsilon_ {i} (t) <   \infty , \end{array} \right.\tag{6}
$$

for all $i \in N$ . We denote by $Z ( t ) : = [ Z _ { 1 } ( t ) , \ldots , Z _ { K } ( t ) ]$ the n-dimensional vector state of the system at time t. The value $\phi _ { 1 }$ is the minimum detectable error level.

We denote by $\mathcal { Z } : = \{ Z ( t ) : ~ t \geq 0 \}$ the corresponding stochastic process. The state space is given by $\bar { \mathcal { K } } : = \{ z = [ z _ { 1 } , \ldots , z _ { n } ] \colon z _ { i } \in \{ 1 , \ldots , K \bar { \} } \}$ , that is, the set of n-dimensional vectors with entries in $\{ 1 , \ldots , K \}$ Notice that K consists of $K ^ { n }$ vector states.

4.3.2. Control Actions. The evolution of process Z depends on whether control is applied at each node at the end of a period. In other words, after computing $\epsilon _ { i } ( t ) .$ , a binary decision (action) $a _ { i } ( t ) \in$ $\{ 0 , 1 \}$ is made, where 0 means no action and 1 means that errors are corrected. We denote by $a ( t ) : =$ $[ a _ { 1 } ( t ) , \ldots , a _ { n } ( t ) ]$ the vector of actions chosen at time t.

The amount of error reduction at node i is related to the decision as follows:

$$
\theta_ {i} (t) = (1 - \beta_ {i}) a _ {i} (t) + (1 - a _ {i} (t)) = 1 - \beta_ {i} a _ {i} (t),\tag{7}
$$

for all $i \in N$ and $t \geq 0$ . The action space is given by $\mathfrak { A } : = \{ a = [ a _ { 1 } , \ldots , a _ { n } ] : a _ { i } \in \{ 0 , 1 \} \}$ , that is, the set of $n -$ dimensional vectors with entries in $\{ 0 , 1 \}$ . Notice that A consists of $2 ^ { n }$ action vectors.

4.3.3. Transition Probabilities. Let $a ( t ) = [ a _ { 1 } ( t )$ $\ldots , a _ { n } ( t ) ]$ denote a vector of actions and $s , s ^ { \prime }$ denote vector states of the process Z. We denote by $\mathcal { P } _ { 0 } ( s _ { i } ^ { \prime } , s _ { i } )$ and $\mathcal { P } _ { 1 } ( s _ { i } ^ { \prime } , s _ { i } )$ the one-step transition probabilities from state $s _ { i }$ to state $s _ { i } ^ { \prime }$ at node i when the actions are $a _ { i } ( t ) = 0$ and $a _ { i } ( t ) = 1$ , respectively. The one-step transition probabilities for the vector states $\mathcal { P } _ { a } ( s ^ { \prime } , s )$ are then given by

$$
\mathcal {P} _ {a} (s ^ {\prime}, s) = \prod_ {i \in N} \mathcal {P} _ {a _ {i} (t)} (s _ {i} ^ {\prime}, s _ {i}),\tag{8}
$$

where s and $s ^ { \prime }$ are n-dimensional vectors with $s _ { i } , s _ { i } ^ { \prime } \in$ $\{ 1 , \ldots , K \}$ . Notice that according to (6) we have

$$
\begin{array}{c} \mathcal {P} _ {a} (s ^ {\prime}, s) = \prod_ {i \in N} \mathcal {P} \bigl \{\phi_ {s _ {i} ^ {\prime} - 1} \leq | \epsilon_ {i} (t + 1) | <   \phi_ {s _ {i} ^ {\prime}} \text {given} \\ \phi_ {s _ {i} - 1} \leq | \epsilon_ {i} (t) | <   \phi_ {s _ {i}} \text {and} a _ {i} (t) \bigr \}. \end{array}\tag{9}
$$

According to (2) the probability distribution of $\rho _ { i }$ is independent of t. Therefore, it follows from (9) that the transition probabilities are stationary and Z is a finite-state Markov chain for any given sequence of vector decisions $\{ a ( t ) \colon t \geq 0 \}$

4.3.4. Control Cost and Risk Due to Errors. We denote by $c _ { i } ( s _ { i } , 1 )$ the cost when a control action $a _ { i } =$ 1 is executed at node i, and node i is in state $s _ { i } \in$ $\{ 1 , \ldots , K \}$ . We assume that $c _ { i } ( s _ { i } , 0 ) = 0 ;$ ; that is, the cost of not executing a control action at node i is zero. We measure risk as a function of the variance of the taint, as follows:

$$
\begin{array}{c} d _ {i} (s _ {i}, a _ {i}) := r (\mathrm{Var} [ \theta_ {i} \rho_ {i} ]) = r (\theta_ {i} ^ {2} \mathrm{Var} [ \rho_ {i} ]) \\ = r ((1 - \beta_ {i} a _ {i}) ^ {2} \mathrm{Var} [ \rho_ {i} ]), \end{array}\tag{10}
$$

where $r ( \cdot )$ is a concave, real-valued function.

In our experiments we consider two types of risk functions, linear $( r ( x ) = x )$ and quadratic $( r ( x ) =$ $x ^ { 2 } )$ , for risk-neutral and risk-averse decision makers, respectively. The linear risk function implies risk neutrality because larger error variances are considered to be as risky as smaller ones. By contrast, the quadratic risk function implies risk aversion because larger error variances are considered riskier than smaller error variances.

4.3.5. Policies. A randomized decision rule $\pi ^ { ( t ) }$ is an n-dimensional vector function such that if the state at time t at node i is $Z _ { i } ( t ) = s _ { i } .$ , then the decision maker chooses action $a _ { i } ( t ) = 1$ with probability $\pi _ { i } ^ { ( t ) } ( s _ { i } )$ and chooses action $a _ { i } ( t ) = 1$ with probability $1 - \pi _ { i } ^ { ( t ) } ( s _ { i } )$ . A (randomized) policy  is an infinite sequence of randomized decision rules $\pi = \{ \pi ^ { ( t ) } \colon t \geq 0 \}$ , which indicates what decision rule to use at each time period t. A stationary Markov policy is a policy $\pi$ where the same decision rule is used for all time periods, that is, $\pi ^ { ( 0 ) } = \pi ^ { ( 1 ) } = \pi ^ { ( 2 ) } = \cdot \cdot \cdot$ . When referring to a stationary Markov policy we will use the same notation $\pi$ to identify the policy as well as the common decision rule used by the policy.

For a discount factor $\alpha ,$ where $0 < \alpha < 1$ , the discounted cost of a stationary policy $\pi$ is given by

$$
C _ {\alpha} (\pi) := \sum_ {t = 0} ^ {\infty} \alpha^ {t} \sum_ {s, s ^ {\prime}} \bigg (\sum_ {i = 1} ^ {n} c _ {i} (s _ {i}, 1) \mathscr {P} _ {1} (s _ {i} ^ {\prime}, s _ {i}) \pi_ {i} (s _ {i}) \bigg).\tag{11}
$$

Similarly, we obtain the discounted risk of a stationary policy as

$$
\begin{array}{c} D _ {\alpha} (\pi) := \sum_ {t = 0} ^ {\infty} \alpha^ {t} \sum_ {s, s ^ {\prime}} \biggl (\sum_ {i = 1} ^ {n} d _ {i} (s _ {i}, 1) \mathcal {P} _ {1} (s _ {i} ^ {\prime}, s _ {i}) \pi_ {i} (s _ {i}) \\ + \sum_ {i = 1} ^ {n} d _ {i} (s _ {i}, 0) \mathcal {P} _ {0} (s _ {i} ^ {\prime}, s _ {i}) (1 - \pi_ {i} (s _ {i})) \biggr). \end{array}\tag{12}
$$

4.3.6. Optimization Problem. The optimization problem seeks to identify an optimal control policy such that the total discounted risk is bounded by a desired risk threshold value R at minimum control cost. The corresponding CMDP optimization problem is as follows:

$$
\begin{array}{l l} \text {(CMDP)} & \min _ {\pi} C _ {\alpha} (\pi) \\ & \text {s.t.} D _ {\alpha} (\pi) \leq R, \end{array}
$$

where R is a given threshold risk value.

## 4.4. LP Formulation

Let $Y _ { i k 0 }$ denote the unconditional steady-state probability that the process is in state k at node i and decision $a _ { i } = 0$ is made. Analogously, let $Y _ { i k 1 }$ denote the unconditional steady-state probability that the process is in state k at node i and decision $a _ { i } = 1$ is made. Then, finding the optimal stationary Markov policy that solves the CMDP is equivalent to solving the following linear program:

$$
\begin{array}{l l} \text {(LP)} & \min \sum_ {i = 1} ^ {n} \sum_ {k = 1} ^ {K} (c _ {i} (k, 0) Y _ {i k 0} + c _ {i} (k, 1) Y _ {i k 1}) \\ & \text {s.t.} \sum_ {i = 1} ^ {n} \sum_ {k = 1} ^ {K} (d _ {i} (k, 0) Y _ {i k 0} + d _ {i} (k, 1) Y _ {i k 1}) \leq R, \end{array}
$$

$$
\begin{array}{l} \sum_ {k = 1} ^ {K} (Y _ {i k 0} + Y _ {i k 1}) = 1, \quad \forall   i \\ Y _ {i l 0} + Y _ {i l 1} - \alpha \sum_ {k = 1} ^ {K} (Y _ {i k 0} \mathcal {P} _ {0} (l, k) + Y _ {i k 1} \mathcal {P} _ {1} (l, k)) \\ = \delta_ {l}, \quad \forall   i, l \\ Y _ {i k 0}, Y _ {i k 1} \geq 0; \end{array}
$$

where $\delta _ { l } = 1$ if l = 1 and $\delta _ { l } = 0$ otherwise.

As usual (Altman 1999), an optimal stationary Markov policy can be found by setting

$$
\pi_ {i} (k) = \frac {Y _ {i k 1}}{Y _ {i k 0} + Y _ {i k 1}},\tag{13}
$$

for all i and k.

Problem LP has 2nK decision variables and $n K +$ $n + 1$ constraints; hence its complexity will depend on the number of bins used in the discretization of the process $\epsilon ( t )$ ; that is, it will depend on granularity of the intervals defined by the constants $\phi _ { k }$ in (6).

If the LP is feasible, then there exists an optimal stationary policy for the CMDP (Altman 1999). In the case study in $\ S { \dot { 5 } } ,$ we show that the corresponding LP is feasible. Therefore, there exists an optimal stationary policy for the case.

## 5. Case Study: Revenue Realization Process Revisited

In this section, we demonstrate how the CMDP model may be applied to data quality risk analysis and management in practice. The data used for model calibration for the revenue realization process are provided by an international production company.

## 5.1. Model Calibration

The high-level modeling diagram of the revenue realization process is shown in Figure 1. There are six subprocesses and a total of 23 tasks involved in the revenue realization process. Each rectangular box in the diagram in Figure 1 represents a subprocess. Within each subprocess, a sequence of tasks is performed to fulfill the function of the subprocess.

5.1.1. The Tasks. The revenue realization process is triggered by a client’s request for quotation, hence the total number of transaction sources $S = 1$ . Once in the process, the request first reaches the sales department, where terms and conditions of an offering are proposed. The order may be placed and the contract established. The order is then fulfilled, and the transactional data finally reach the accounting department where revenues are realized. As shown in Figure 1, there are two audit targets at the end of the process diagram. The total number of audit targets J is $^ { 2 , }$

Table 4 Subprocesses and Tasks in the Revenue Realization Process

Subprocesses Tasks (or error sources) Sales 1. Formalize offering terms and conditions 2. Review nonstandard terms, conditions, and amended terms 3. Send order terms and conditions to contract establishment Contract establishment 4. Determine offering price and submit contract configurations 5. Legal review of contract 6. Submit purchase order pricing 7. Create an account if new customer 8. Send order information to order management Order management 9. Submit credit check 10. Receive credit decision and contract terms and conditions 11. Enter order information 12. Prepare shipping information 13. Send order, shipping, and credit information to contract update and backlog management Contract update 14. Compile contract information, purchase order information, and credit information 15. Submit to client the updates in the contract 16. Review signed contract and update contract status Backlog management 17. Compile order information, shipping information, and approved credit information 18. Confirm firm order policy 19. Prepare invoice and update order package 20. Ship ordered items and update shipping information Revenue realization 21. Receive shipping confirmation and release billing 22. Create and submit accounting information and close order 23. Update the “general ledger” and “accounts receivables”

where j = 1 indicates “general ledger” and j = 2 indicates “accounts receivables.” Throughout the revenue realization process, a transaction is processed by the 23 tasks listed in Table 4. Figure 2 shows the path relations of the tasks in the process.

5.1.2. The Volume Transition Matrix. At the aggregate level, the transition of transactions from one task to another is encoded in the volume transition matrix $V ,$ of size $2 6 \times 2 6$ . An element $v _ { i j }$ of the volume transition matrix captures the percentage of transactions processed by task i that reach task j. The sum of the elements on each row, $v _ { i } = \textstyle \sum _ { j } v _ { i j }$ can be greater than 1, as the same transaction processed at task i can be duplicated and forwarded to multiple other tasks in the process (see §3.3). The full specification of the $V _ { 2 6 \times 2 6 }$ matrix corresponding to the revenue realization process is given in Online Appendix B.

5.1.3. Error Classes. Errors may affect different aspects of transactional data. To capture the different aspects of error impact, we adopt the concept of error classes from the accounting literature (Lea et al. 1992). We consider five error classes commonly used in the financial accounting practice: completeness, existence, valuation, presentation and disclosure, and rights and obligations. Completeness errors occur when not all relevant information that should be reported is reported, e.g., missing accounting information. Existence errors are present when some of the reported transactions are spurious or should not be reported in accounting ledgers, e.g., duplicated orders. Valuation errors occur when the quantitative value of an otherwise valid transaction is incorrect, e.g., incorrect quantity of sales. Presentation and disclosure errors occur if an account is not properly classified and described in the financial statements, or if required information is not disclosed in the financial statements or in the footnotes thereto. Rights and obligations errors occur when the company does not have certain rights to recorded assets or liabilities at a given date. In Table 5, we use the abbreviations C, E, V, PD, and RO to refer to these five error classes, respectively.

We consider a set of error incidences that had been reported for the revenue realization process. From the modeling standpoint, different error incidences can be distinguished from one another in terms of (a) the subset of error classes that an error contributes to, (b) the subset of tasks where an error may be introduced, and (c) the historical variance of the taint that an error has introduced. Table 5 summarizes the salient characteristics of the errors that are relevant to our analysis. The first column briefly describes the nine error incidences. The second column lists the tasks where each error incidence may be introduced. For instance, the error “Revenue not realized in the correct period” may be introduced by tasks 13, 19, and 21; the error “Not a reasonable expectation of payment” may be introduced by tasks 9, 10, and 17. The third column lists the estimated variance of the taint $\sigma _ { i } ^ { 2 }$ that an error incidence can introduce at tasks. The estimation of the taint variances is based on the quarterly sales reports and the control logs of the monthly testing procedures by the internal auditing department of the company. The last five columns identify the corresponding error classes (C, E, V, PD, and RO, as defined above) to which each error incidence contributes.

Note that not every task in the process may introduce errors. For instance, tasks 1, 2, 3, 5, 6, 7, and 8 are not associated with any error because the reported error incidences introduced by these tasks were estimated to be negligible.

Table 5 A Catalog of Error Classes for the Revenue Realization Process

<table><tr><td rowspan="2">Description of error incidences</td><td rowspan="2">Tasks</td><td rowspan="2">Variances of taint</td><td colspan="5">Error classes</td></tr><tr><td>C</td><td>E</td><td>PD</td><td>V</td><td>RO</td></tr><tr><td>Revenue not realized in the correct period</td><td>13, 19, 21</td><td>0.01</td><td>1</td><td>1</td><td></td><td></td><td>1</td></tr><tr><td>Revenue realized for shipments remaining uninstalled</td><td>23</td><td>0.02</td><td>1</td><td>1</td><td></td><td></td><td>1</td></tr><tr><td>Firm order guidelines not met</td><td>18</td><td>0.02</td><td>1</td><td>1</td><td>1</td><td>1</td><td></td></tr><tr><td>Not a reasonable expectation of payment</td><td>9, 10, 17</td><td>0.02</td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>Incorrect or unauthorized pricing</td><td>15, 22</td><td>0.05</td><td>1</td><td></td><td>1</td><td>1</td><td></td></tr><tr><td>Contracted revenue criteria not met</td><td>11, 14</td><td>0.07</td><td>1</td><td>1</td><td>1</td><td>1</td><td></td></tr><tr><td>Revenue adjustments per contract being done incorrectly</td><td>16</td><td>0.05</td><td>1</td><td>1</td><td>1</td><td></td><td></td></tr><tr><td>Revenue not realized correctly because of shipments mistake</td><td>12, 20</td><td>0.01</td><td>1</td><td>1</td><td></td><td></td><td>1</td></tr><tr><td>Revenue allocation between divisions being done incorrectly</td><td>4</td><td>0.01</td><td></td><td></td><td>1</td><td></td><td></td></tr></table>

5.1.4. Dependencies Among Error Classes. The CMDP model developed in §4 accommodates multiple dimensions of error dependence, including the correlation among taints contributed by different errors with their corresponding classes and the dependence of error magnitudes induced by error propagation through tasks.

Relevant to the calibration process is the error dependence that arises from the possible correlation among taints contributed by different error classes. As discussed above, taints introduced by each task compound inaccuracies from (up to) five distinct error classes. At time $t ,$ we have $\begin{array} { r } { \rho _ { i } ( t ) = \sum _ { k } \rho _ { i k } ( t ) \cdot I _ { ( k \sim i ) } , } \end{array}$ where the index k runs across the five error classes. The indicator function I simply asserts that the taints introduced at task i contribute to error class $k ;$ that is, the indicator function takes value 1 when the event $( k \sim i )$ is true and 0 when false. One quantity of interest in the CMDP model is the variance of taints, which can expressed as

$$
\begin{array}{l} \operatorname{Var} [ \rho_ {i} (t) ] = \sum_ {k} \operatorname{Var} [ \rho_ {i k} (t) ] \cdot I _ {(k \sim i)} \\ - \sum_ {k, j} \operatorname{Cov} [ \rho_ {i k} (t), \rho_ {i j} (t) ] \cdot I _ {(k \sim i)} \cdot I _ {(j \sim i)}. \end{array}\tag{14}
$$

Correlation among error classes is introduced in the model by specifying a nonzero value for the covariances, $\bar { \mathrm { C o v } [ } \bar { \rho } _ { i k } ( \bar { t } ) , \bar { \rho _ { i j } } ( t ) ]$ . As the estimated magnitude of these covariances from historical records is negligible, we set all these covariance terms to be 0. Column 3 of Table 5 lists the estimated values of the variances $\mathrm { V a r } [ \rho _ { i k } ( t ) ]$ . The data used to derive the variance estimates $\rho _ { i }$ (the third column of Table 5) are from taint reports provided by the international production company.

5.1.5. Control Cost and Effectiveness. Control procedures retrieve and correct errors in the transactional data at feasible control locations in the process, and they ultimately mitigate the risk associated with errors in the data flow. Table 6 summarizes the available control procedures for each subprocess and each feasible control location. The first column lists relevant subprocesses of the revenue realization process. The second column lists the tasks that are both sources of errors and feasible control locations. The third column lists the available control procedure for each feasible control location. The fourth column provides a brief description of the control procedures. The estimates of control costs come from the quarterly testing of the controls as required by the internal auditing department; the estimates of control effectiveness come from quarterly testing reports by external auditing services.

The effectiveness of a control procedure $\beta _ { i }$ at task i is defined as its ability to reduce variances of errors in transactional data flow at task i. As shown in Table $^ { 6 , }$ each control procedure can be applied to a prespecified subset of tasks. For instance, the procedure OBP010 only detects and corrects the error “Revenue not realized in the correct period.” This error occurs at tasks 13, 19, and 21. OBP010 is able to correct errors at tasks 19 and 21 with the same effectiveness parameter $\beta _ { 1 9 } = \beta _ { 2 1 } = 0 . 8 9$ . The fifth column of Table 6 lists the estimates of effectiveness for each control procedure at their feasible task locations. The estimates of control effectiveness are from quarterly testing reports by external auditing services. When an error incidence is eliminated at a specific task, we assume that its presence is simultaneously eliminated in all of the corresponding error classes. Therefore, control procedures reduce the variance of error classes introduced by the same task i with equal effectiveness rates.

We measure the cost of a control procedure as the average cost of control on a dollar book value. We define the cost of control at task i in terms of a function, $c ( s _ { i } , a _ { i } )$ , which is a function of the state variable $s _ { i }$ and the control action $a _ { i } .$ For instance, the cost of control is zero if no control procedure is executed; that is, $c ( s _ { i } , a _ { i } = 0 ) = 0$ for each control procedure in the revenue realization process. The cost of control is independent of the time, as the cost of executing a control procedure remains stable over a fairly long time period. The estimates of $c ( s _ { i } , a _ { i } = 1 )$ for each control procedure in the revenue realization process are listed in the sixth column of Table 6. The estimates of control are based on the quarterly testing of the controls as required by the internal auditing department.

Table 6 Control Procedures in the Revenue Realization Process

<table><tr><td>Subprocesses</td><td>Task</td><td>Control procedures</td><td>Description of control actions</td><td>Effectiveness (%)</td><td>Cost</td></tr><tr><td>Contract establishment</td><td>4</td><td>PRI 550</td><td>Review and correct errors in proposed offering price</td><td>89</td><td>0.110</td></tr><tr><td rowspan="5">Order management</td><td>9</td><td>OBP 020</td><td>Review and correct errors in credit and pay trend</td><td>83</td><td>0.010</td></tr><tr><td>10</td><td>DIR 020</td><td>Review and correct errors in credit decision</td><td>97</td><td>0.043</td></tr><tr><td>11</td><td>DIR 060</td><td>Ensure documents are complete</td><td>88</td><td>0.760</td></tr><tr><td>12</td><td>BPM 409</td><td>Ensure documents are complete</td><td>97</td><td>0.01</td></tr><tr><td>13</td><td>OBP 072</td><td>Review and correct errors in shipping information</td><td>83</td><td>0.010</td></tr><tr><td rowspan="3">Contract update</td><td>14</td><td>DIR 060</td><td>Review and correct errors in contract/purchase order</td><td>88</td><td>0.760</td></tr><tr><td>15</td><td>DIR 030</td><td>Validate price in the contract updates; correct errors if any</td><td>97</td><td>0.110</td></tr><tr><td>16</td><td>DIR 090</td><td>Review and correct errors in a signed contract</td><td>86</td><td>0.110</td></tr><tr><td rowspan="4">Backlog management</td><td>17</td><td>DIR 020</td><td>Review for approved credit check</td><td>97</td><td>0.043</td></tr><tr><td>18</td><td>DIR 010</td><td>Ensure and confirm a firm order</td><td>89</td><td>0.110</td></tr><tr><td>19</td><td>OBP 010</td><td>Review firm policy</td><td>89</td><td>0.043</td></tr><tr><td>20</td><td>OBP 082</td><td>Review and correct errors in ship-to override</td><td>94</td><td>0.010</td></tr><tr><td rowspan="3">Revenue realization</td><td>21</td><td>OBP 010</td><td>Ensure key fields are complete</td><td>89</td><td>0.043</td></tr><tr><td>22</td><td>OBP 030</td><td>Review and correct errors in price overrides</td><td>93</td><td>0.010</td></tr><tr><td>23</td><td>BPM 410</td><td>Check if products uninstalled for &gt;30 days</td><td>93</td><td>0.110</td></tr></table>

## 5.2. Computational Results

We apply the CMDP model to the revenue realization process and present the computational results and analyses. Holding all other factors constant, we examine the impact of the risk attitudes of a decision maker according to the risk function $r ( \cdot )$ and the threshold risk $R ,$ on the resulting optimal policies and corresponding objective values.

5.2.1. Experimental Design. We explore the effects of two parameters: the risk function $r ( \cdot )$ , linear versus quadratic; and the risk bound R, low versus high. We implemented a complete grid design that involves four sets of experiments, each corresponding to a combination of risk function and risk bound: (a) linear risk, low bound; (b) linear risk, high bound; (c) quadratic risk, low bound; and (d) quadratic risk, high bound. To measure the effects of the optimal policy over a moderate time horizon, we propagated a continuous flow of transactions—corresponding to simulated monthly orders—through the revenue realization process. We recorded the state of the system for the first 100 time periods. To classify the level of severity of the accumulated taints, we use equally spaced intervals of size $\Delta \phi ;$ that is, $\phi _ { k } - \phi _ { k - 1 } = \Delta \phi$ for $1 \leq k \leq K - 1$ . The full calibration of the revenue realization process is summarized in Table 7.

To find an optimal policy we used the LP model discussed in §4.4. We estimated values for the transition probabilities $\mathcal { P } _ { 0 } ( s _ { i } ^ { \prime } , s _ { i } )$ and $\mathcal { P } _ { 1 } ( s _ { i } ^ { \prime } , s _ { i } )$ based on historical data and simulations. The LP has 4,600 decision variables and $^ { 2 , 3 2 4 }$ constraints (not including nonnegativity constraints). The LP model was solved and the experiments were conducted in Matlab<sup>TM</sup>.

Table 7 Parameter Calibration for the Revenue Realization Process

<table><tr><td>Parameters</td><td>Calibration</td></tr><tr><td> $n$ </td><td>23</td></tr><tr><td> $K$ </td><td>100</td></tr><tr><td> $\phi_{1}$ </td><td>0.01</td></tr><tr><td> $\Delta\phi$ </td><td>0.01</td></tr><tr><td> $V$ </td><td>Appendix B</td></tr><tr><td> $\alpha$ </td><td>0.8</td></tr><tr><td> $\sigma_{i}^{2}$ </td><td>Estimates in column 3 of Table 5</td></tr><tr><td> $\beta_{i}$ </td><td>Estimates in column 5 of Table 6</td></tr><tr><td> $c(s_{i}, 1)$ </td><td>Estimates in column 6 of Table 6</td></tr><tr><td> $R$ </td><td>0.2 (low) and 1 (high)</td></tr></table>

For each set of experiments, we compare the following:

(a) the process-level realtime risk at each time period t with the threshold risk R,

(b) the process-level real-time control cost at each time period t with the total discounted cost $C _ { \alpha } ( \pi ^ { * } )$ over time, and

(c) the number of controls executed at each task. For each set of experiments, we also report (a) the evolution of task-specific taint variances over 100 time periods with optimal control policies $\pi ^ { * } .$ , (b) the dynamics of task-specific control actions, and (c) the taskspecific control frequencies versus taint variances. Finally, we compare process-level risk under three different control policies: no control policy, a random control policy with an equal total-discounted cost $( C _ { \alpha } ( \pi ^ { * } ) )$ , and the optimal control policy $\pi ^ { * }$

## 5.2.2. Results.

The Risk-Averse Scenario. Figure 5 presents the computational results for both low risk tolerance

![](/api/attachments/KPZWGQQV/fulltext/images/d2fc1be3b847e2f332361c7873881df479e11bc9ef8ce7a3e334e8a1d9f5623a.jpg)  
Figure 5 Process-Level Risk, Process-Level Cost, and Task-Specific Frequency of Control in the Risk-Averse Scenario

Note. Process-level risk (left column), process-level cost (middle column), and task-specific frequency of control (right column), with low risk bound $R = 0 . 2$ (top row) and high risk bound R <sub>=</sub> 1 (bottom row).

R <sub>=</sub> 02 (panels in the top row) and high risk tolerance R <sub>=</sub> 1 (panels in the bottom row).

The panels in the left column of Figure 5 show the temporal evolution of real-time process-level risk over 100 time periods (solid line) and compare it to the risk tolerance threshold R (dashed line). The evolution of the process-level risk itself is not particularly informative. There is a surprise, however, because the realtime process-level risk is strictly below the risk tolerance threshold R, independently of the value of R. This is counterintuitive, as the total discounted risk $D _ { \alpha } ( \pi ^ { * } )$ achieved by the optimal stationary policy is practically the same as, albeit slightly lower than, the risk tolerance threshold R.

The panels in the middle column of Figure 5 show the temporal evolution of real-time process-level cost over 100 time periods (solid line) and compare it to the optimal discounted cost $C _ { \alpha } ( \pi ^ { * } )$ achieved by the optimal stationary policy (dashed line). The panels in the right column of Figure 5 show the average frequency of control for each task over time. In the risk-averse scenario, the standard deviation of task-specific control frequency is lower for high risk threshold (0.0182) than for the low risk threshold (0.0190). In addition, the total discounted cost is lower for the high risk threshold (\$134) than that for the low risk threshold (\$148). As expected, when the risk threshold is low, a risk-averse decision maker has greater pressure to meet the risk threshold; the optimal policy tends to apply controls most frequently at tasks that have highest volume of inflows or outflows. These tasks are considered to be crucial in the sense that errors cumulate rapidly at such task locations. For instance, controls at tasks 14 and 17 are crucial for the revenue realization process because of the high volume of data inflow and outflow through them (see Figure 2). By contrast, when risk threshold is high, the risk-averse decision maker is less constrained by the risk bound. Hence the controls in optimal policy are more evenly distributed, and result in a lower total discounted cost.

Figure 6 presents the taint variance evolution at each task over 100 time periods. The set of 23 panels on the left corresponds to low risk tolerance $\bar { R = } 0 . 2$ and the set of panels on the right corresponds to high risk tolerance R 1. Each panel shows the dynamics of the task-level error variance status on the Y axis over time periods on the X axis. The shades in each panel correspond to intervals of taint variance values, where the optimal stationary policy is to perform a control, should the expected taint variance fall inside the interval. Intuitively, each task comes with a deterministic policy that works very much as a control chart, but it may be specified by more than one interval, and it works on expected, rather than observed, taints. We shall refer to the intervals as task-specific policy bands. These sets of taint variance time series offer a more detailed view of what happens in the revenue realization process we are interested in studying. Although the process-level risk in Figure 5 (left panel) is stably below the preset risk tolerance R, the risk level at task i easily escapes the policy band of task i. The control, however, is exercised by a combination of controls at task i and its preceding tasks together with their beneficial effects through the volume transition matrix V .

Figure 6 Evolution of Task-Specific Taint Variances in the Risk-Averse Scenario  
![](/api/attachments/KPZWGQQV/fulltext/images/9554837f93a0473fbfe68b01bd9f334137b4808d1ee74200c61896798457a854.jpg)  
Note. Evolution of task-specific taint variances with low risk bound R  02 (set of 23 panels on the left), and with high risk bound R  1 (set of 23 panels on the right).

Figure 7 presents the temporal sequence of taskspecific controls for each task. The Y axis indicates the tasks, and the X axis indicates the time periods. The left panel of Figure 7 shows the temporal sequence of controls for the low risk tolerance R 02; and the right panel of Figure 7 shows the temporal sequence of controls for the high risk tolerance R 1. As shown in both panels, the control trails are not synchronized across tasks, despite the fact that the task-specific policy bands for both high and low R are very similar (see Figure 6). The control trails also start by a first control at task 14, although this first control happens earlier, when the risk tolerance is low, as expected. In addition, the control trails for the same task differ for the two risk threshold settings; the average number of times the two control trails overlap at each task is less than 30% of the total procedures performed for each risk threshold scenario.

A closer look at the control trails in Figure 7 reveals an interesting pattern. We explain this pattern in Figure 8. Figure 8 shows the number of controls for each task, on the Y axis, versus its stabilized variance, on the X axis. The more crucial tasks are characterized by a higher taint variance and are controlled more often. A regression analysis (dashed line) shows that this relation holds on the average (both the slope and the intercept coefficients are significant, with pvalue < 005) with some exceptions—notably tasks 1 and 2. Intuitively, the optimal stationary policy specifies a fixed periodic schedule according to which each task is applied with control. The periodicity is shorter

Figure 7 Dynamics of Task-Specific Controls in the Risk-Averse Scenario  
![](/api/attachments/KPZWGQQV/fulltext/images/ad14efb5a67ee09ae9dd29de3573b99ee09c1e85956c65ced903f13065bf924f.jpg)

![](/api/attachments/KPZWGQQV/fulltext/images/c94a123bc1a7530a1b846cf7fd06fc3045c63c49557e2d79cdad24533875e778.jpg)  
Note. Dynamics of task-specific controls with low risk bound R <sub>=</sub> 02 (left panel) and high risk bound R <sub>=</sub> 1 (right panel).

## Figure 8 Task-Specific Control Frequencies vs. Taint Variances in the Risk-Averse Scenario

![](/api/attachments/KPZWGQQV/fulltext/images/eac6e209dc4bedfd5aa3bc86cc9b65e34acd5b2c8e9130b3169cebadcae51c35.jpg)

![](/api/attachments/KPZWGQQV/fulltext/images/232d275ea6a7a4fbbbf11dafec946a1a2f1fe7974c34e697bec4ec57041536ac.jpg)  
Note. Task-specific control frequencies versus taint variances for low risk threshold R 02 (left panel) and high risk threshold R 1 (right panel).

Figure 9 Process-Level Risk, Process-Level Cost, and Task-Specific Frequency of Control in the Risk-Neutral Scenario  
![](/api/attachments/KPZWGQQV/fulltext/images/3971739b95ae27d9d9fd69ba3ca5ec6e1c66c91db297e9e331b36880f9b2e2d6.jpg)

![](/api/attachments/KPZWGQQV/fulltext/images/366735327b04cfaa06a1d3721f060410d232b17e0a79f090f3153c1d569a44ed.jpg)

![](/api/attachments/KPZWGQQV/fulltext/images/49626420f44b8c3064c0116627bbd4018f1540a9ea173af4322c4b6f1d664efe.jpg)

![](/api/attachments/KPZWGQQV/fulltext/images/816c281425f13154ca714b3d031de52ff4f58ea75e80dc2aa16aa392d3e426c5.jpg)

![](/api/attachments/KPZWGQQV/fulltext/images/27d7524a70023829cceceaf445696f3db8df886a23f3adfb62c998a71b882f77.jpg)

![](/api/attachments/KPZWGQQV/fulltext/images/4443ccf3b6b04ab870c83848550a84d665f05a7d963ef386bb03c25675ce13e7.jpg)  
Note. Process-level risk (left column), process-level cost (middle column), and task-specific frequency of control (right column), with low risk threshold R 02 (top row) and high risk threshold R 1 (bottom row).

for more crucial tasks, leading to a larger number of controls.

The Risk-Neutral Scenario. The results for the riskneutral scenario confirm the insights we gained in the risk-averse case, with minor differences. We briefly discuss them.

As with the risk-averse scenario, the process-level statistics for both low risk tolerance (panels in the top row) and high risk tolerance (panels in the bottom row) thresholds are shown in Figure 9. The panels in the left column show the temporal evolution of the real-time process-level risk (solid line) and the threshold risk (dashed line). The panels in the middle column present the temporal evolution of real-time process-level control cost (solid line) and the optimal discounted cost (dashed line). The panels in the right column show the frequency of control at each task over 100 time periods. In contrast to the risk-averse scenario, here we observe that the standard deviation of the task-specific control frequencies is about the same for both high risk (0.0223) and low risk thresholds (0.0224). This pattern indicates that the threshold risk does not have significant impact on a risk-neutral decision maker’s optimal policy.

Figure 10 Evolution of Task-Specific Taint Variances in the Risk-Neutral Scenario  
![](/api/attachments/KPZWGQQV/fulltext/images/d43c27c496e7b2c9d325ad8d50279eb5744fc7761fc56bf5d0c024f0b59d7b4e.jpg)  
Note. Evolution of task-specific taint variances with low risk bound R 02 (set of 23 panels on the left) and high risk bound R 1 (set of 23 panels on the right).

Figure 10 presents the taint variance evolution at each task over 100 time periods. The set of 23 panels on the left corresponds to the low risk threshold $R =$ 02, and the panels on the right corresponds to the high risk threshold R 1.

The temporal sequences of controls for each task is shown in Figure 11. The left panel presents the results corresponding to a low risk threshold, and those corresponding to a high risk threshold are shown in the right panel. Similar to those in Figure 7, the control trails are synchronized neither across tasks within the same panel nor across panels. However, compared to the risk-averse scenario, some differences in the control trails here are seen. The central tasks 14 and 17 are now equivalently crucial in terms of risk. Accordingly, the first set of controls is performed around the eighth period at both of these tasks simultaneously, independently of the risk tolerance threshold R. Additionally, in the case where the threshold is low, the first set of controls includes task 13 as well. More generally, the control trails in the risk-neutral scenario reveal a similar pattern to that in Figure 8.

Figure 12 shows the number of controls for each task on the Y axis, versus its variance on the X axis. A regression analysis (dashed line) shows that more crucial tasks are controlled more often, on average (both coefficients are significant, with p-value < 005). The same intuition holds as before: the optimal stationary policy specifies a fixed periodic control schedule, with shorter periodicity for more crucial tasks, leading to a larger number of controls.

Process-Level Risk Under Different Control Policies. Figure 13 presents the comparative results of the process-level risk under three different control policies: (a) no control policy; (b) a random control policy with a process-level cost equal to $C _ { \alpha } ( \pi ^ { * } )$ , and (c) the optimal control policy $\pi ^ { * }$ . We present four plots that illustrate the process-level risk evolution for the four risk scenarios.

The top left panel in Figure 13 shows the temporal evolution of real-time process-level risk over 100 time periods for the linear risk and low bound scenario (R 02). The starred line shows the real-time process-level risk in the absence of a control policy. The dashed line shows the risk from a policy that is exactly as expensive as the optimal policy, but carried out according to a set of random decision rules. We use these two policies as the benchmark to evaluate the optimal control policy. The real-time process-level risk generated by the optimal policy is represented by a solid line.

Figure 11 Dynamics of Task-Specific Controls in the Risk-Neutral Scenario  
![](/api/attachments/KPZWGQQV/fulltext/images/6561e1f74a147b0781be94b2b18581d07a5b7574dd0a9c5ac1fadae6519c5407.jpg)

![](/api/attachments/KPZWGQQV/fulltext/images/5ebdbcd9a6af31a209e335b5d5b4b20039c707d621d433d3484b53b212366ee0.jpg)  
Note. Dynamics of task-specific controls with low risk bound R <sub>=</sub> 02 (left panel), and with high risk bound R <sub>=</sub> 1 (right panel).

Figure 12 Task-Specific Control Frequencies vs. Taint Variances in the Risk-Neutral Scenario  
![](/api/attachments/KPZWGQQV/fulltext/images/40b0fb06d45d6201415a845ec24d8a6382d34d99291744aa21613234c8d90d09.jpg)

![](/api/attachments/KPZWGQQV/fulltext/images/7ffbfb5056d3fe8216ee93325f9fb76600d60cd4541ddf5644937c5a29805598.jpg)  
Note. Task-specific control frequencies versus taint variances for low risk threshold R 02 (left panel) and high risk threshold R 1 (right panel).

As shown in the plot, in the absence of control, the risk grows quickly. The difference of the resulting total discounted risks between the absence of control policy and the optimal control policy is 219, which is almost 1100% of the risk threshold. The random policy schedules controls to tasks uniformly at random. The real-time process-level risk by this policy increases more slowly than those with no control policy, but it quickly grows beyond the risk bound. The difference of the resulting total discounted risks between the random control policy and the optimal control policy is 0094, which is 47% of the risk threshold. The same patterns hold for the other three plots. The results suggest that the optimal control policy identified by the CMDP model is able to effectively reduce the process-level risk both in real-time and on a long-term horizon. Our model offers cost-effective solutions to data quality risk control in accounting systems under various risk settings.

## 6. Conclusion

The model proposed in this paper provides an effective and viable means for managing the risk associated with data quality in auditable transactional data. This model accommodates possible error correlations and captures the error generation and propagation dynamics in transactional data flows in business processes. The most valuable aspect of the solution our methodology offers to risk management practice is the stationary optimal control policies. In practice, such policies are desirable, as they allow for a single deployment of control resources over a fixed period of time, so it is more cost-effective and easier to implement than previous approaches proposed for data quality risks.

Our model works well for corporate settings where some stability in the process parameters can be expected because of a high volume of transactions, and where monitoring logs are required and their reliability certified by external companies. In such settings, the parameters of the proposed model, including the process structure, periodic transaction volumes, error probabilities, audit frequency, and control cost and effectiveness, are readily obtainable. The implementation of our model follows a few steps: (a) calibrating the parameters of the model with reasonable confidence using historical data and monitoring logs, as illustrated in §5.1; (b) deriving an optimal stationary control policy by solving the optimization problem developed in §4.4; (c) applying the optimal policy at the task level; and (d) testing the effectiveness of the

Figure 13 Comparative Results of the Process-Level Risks  
![](/api/attachments/KPZWGQQV/fulltext/images/66420ac95ad8833caa1a2866319b33ed6da991e03805fcfecd692a4f12723388.jpg)  
(b) Linear risk and high bound

(c) Quadratic risk and low bound  
![](/api/attachments/KPZWGQQV/fulltext/images/5f3e235a5c6dfc8b27441bb6878a10eaaab3d3ff92678eef32efb345aaffbce9.jpg)  
Note. The low risk bound R  02; the high risk bound R  1.

One desirable feature of the optimal control policy is that it is preventive rather than reactive. The policy recommends control actions based on the anticipated taints at the end of a period. At the time periods where the taint variance is expected to reach a critical value, the policy will recommend a control action and correct the situation. Corrections at a task reduce error propagation in all subsequent tasks. Findings from the computational analysis of the model behavior under the optimal policies in four types of risk settings suggest that, in the risk-averse case, the lower the risk tolerance threshold is, the more a policy should concentrate controls on the most crucial tasks, such as compile contract information. At higher risk optimal policies by replicating computational analysis in §5.2 in what-if scenarios.

![](/api/attachments/KPZWGQQV/fulltext/images/a9cb56dbfb0d88a616b9996d9a450ec7497d666c4adcb9054c05d728d6df40d9.jpg)

(d) Quadratic risk and high bound  
![](/api/attachments/KPZWGQQV/fulltext/images/91a28561b68c31d7531b7bdf7fec217c9d58ab88f73ab020fbfda0e00c821790.jpg)

tolerance thresholds, the risk-averse decision maker can allow more resources to control less crucial tasks. However, the optimal strategy for the risk-neutral decision maker does not seem to depend on the risk tolerance threshold values.

Although the model and analysis presented in this study have been motivated by the types of transaction errors and error-correcting controls in the accounting domain, this model may be extended to other domains and definitions of data quality. For example, we can consider a scenario in which “error sources” introduce uncertainty, rather than mistakes, into the transaction data. Sources of uncertainty could be prices of raw material, customer demand, product development times, service delivery times, and so forth. We can then adapt the error propagation techniques developed in this paper to model and control the propagation of these uncertainties to the data repositories. We can also consider analogues of “controls” that may reduce these uncertainties at a cost. For example, uncertainties about prices of raw materials can be reduced by establishing long-term contracts or hedging with options. Variability in delivery times may be reduced by automating processes. The actions taken to reduce uncertainties come at a cost. In such settings, our methodology provides a practical approach to assessing the trade-off of costs with the consequent data quality risks from uncertainties in data repositories.

In conclusion, the proposed methodology offers a new perspective on risk management based on data quality in accounting information systems. This methodology distinguishes the two evolutional aspects of errors, separates the two functional components of data quality control mechanisms, and extends the basic formulations of CMDP models by including a damping control element. Compared to the existing methods for data quality management in the literature, our methodology enables optimization formulations at the task level that leads to effective and viable risk management strategies in practical settings. Our model lends itself to implementations within process modeling workbenches and adds analytical rigor to existing process modeling tools. Our work applies not only to the literature and practice of financial accounting, but also to business decisionsupport systems in general.

## Electronic Companion

An electronic companion to this paper is available as part of the online version at http://dx.doi.org/10.1287/ isre.1110.0371.

## References

Altman, E. 1999. Constrained Decision Processes. Chapman & Hall/CRC, London.

Bagchi, S., X. Bai, J. Kalagnanam. 2006. Data quality management using business process modeling. Proc. IEEE Internat. Conf. Services Comput. (SCC’06), Chicago, 398–405.

Bai, X., R. Krishnan, R. Padman. 2007. Design of risk management strategies in business process information flow. Proc. Internat. Conf. Inform. Systems (ICIS 2007). Paper 28, http://aisel.aisnet .org/icis2007/28, Montréal, Québec.

Ballou, D. P., H. L. Pazer. 1985. Modeling data and process quality in multi-input, multi-output information systems. Management Sci. 31(2) 150–162.

Ballou, D. P., R. Y Wang, H. L. Pazer, L. K. Taylor. 1993. Modeling data manufacturing systems to determine data product quality. Technical Report 9, MIT Sloan School of Management, Cambridge, MA.

Bootman, J. L., L. R. Cronenwett, D. W. Bates, R. M. Califf. 2007. Comprehensive strategies for reducing drug-related mistakes. Report, Committee on Identifying and Preventing Medication Errors, Institute of Medicine, National Academies Press, Washington, DC.

COSO. 2004. Enterprise risk management—Integrated framework: Executive summary. Committee of Sponsoring Organizations of the Treadway Commission (COSO), American Institute of CPAs, New York.

Cushing, B. E. 1974. A mathematical approach to the analysis and design of internal control systems. Accounting Rev. 49(1) 24–41.

Moore, S. 2007. “Dirty data” is a business problem, not an IT problem. Gartner, Inc., Stamford, CT. http://www.gartner.com/it/ page.jsp?id=501733.

Hall, J. A. 1998. Accounting Information Systems, 2nd ed. South Western College Publishing, Boston.

Ham, J., D. Losell, W. Smieliauskas. 1985. An empirical study of error characteristics in accounting populations. Accounting Rev. 60(3) 387–406.

Hoitash, R., U. Hoitash, J. C. Bedard. 2008. Internal control quality and audit pricing under the Sarbanes-Oxley Act. Auditing: J. Practice Theory 27(1) 105–126.

Huang, K. T., Y. W. Lee, R. Y. Wang. 1999. Quality Information and Knowledge. Prentice Hall, Upper Saddle River, NJ.

ISACA. 2007. Control objectives for information and related technology (COBIT). ISACA and IT Governance Institute, Rolling Meadows, IL.

Ji, Y., V. S. Mookerjee, S. P. Sethi. 2005. Optimal software development: A control theoretic approach. Inform. Systems Res. 16(3) 292–306.

Knechel, W. R. 1985. An analysis of alternative error assumptions in modeling the reliability of accounting systems. J. Accounting Res. 23(1) 194–212.

Kohn, L. T., J. M. Corrigan, M. S. Donaldson. 2000. To err is human: Building a safer health system. Report, Committee on Quality of Health Care in America, Institute of Medicine, National Academies Press, Washington, DC.

Krishnan, J., D. Rama, Y. Zhang. 2008. Costs to comply with SOX Section 404. Auditing: J. Practice Theory 27(1) 169–186.

Krishnan, R., J. Peters, R. Padman, D. Kaplan. 2005. On data reliability assessment in accounting information systems. Inform. Systems Res. 16(3) 307–326.

Lea, R. B., S. J. Adams, R. F. Boykin. 1992. Modeling of the audit risk assessment process at the assertion level within an account balance. Auditing: J. Practice Theory 11(Supplement) 152–179.

Marinos, G. 2004. Data quality: A risk-based approach. Technical report, PricewaterhouseCoopers, San Jose, CA.

Nado, R., M. Chams, J. Delisio, W. Hamscher. 1996. COMET: An application of model-based reasoning to accounting systems. Proc. 8th Innovative Appl. Artificial Intelligence Conf., AAAI Press, 1482–1490.

Pipino, L. L., Y. W. Lee, R. Y. Wang. 2002. Data quality assessment. Comm. ACM 45(4) 211–218.

Pittetl, D., L. Donaldson. 2006. Challenging the world: Patient safety and health care-associated infection. Internat. J. Quality Health Care 18(1) 4–8.

Richter, A. 2007. The high cost of clean data. CFO Magazine for Senior Financial Executives, CFO Publishing LLC, accessed September 20, 2007, http://www.cfo.com/article.cfm/9705501 ?f=search.

Siegel, J. G., J. K. Shim. 1998. Accounting Handbook. 2nd ed. McGraw-Hill, New York.

Strong, D. M., W. L. Yang, R. Y. Wang. 1997. Data quality in context. Commun. ACM 40(5) 103–110.

Sun, S. X., J. L. Zhao, J. F. Nunamaker, O. R. L. Sheng. 2006. Formulating the data-flow perspective for business process management. Inform. Systems Res. 17(4) 374–391.

Wand, Y., R. Y Wang. 1996. Anchoring data quality dimensions in ontological foundations. Comm. ACM 39(11) 86–95.

Wang, R. Y. 1998. A product perspective on total data quality management. Comm. ACM 41(2) 58–65.

Wang, R. Y. Y., D. M. Strong. 1996. Beyond accuracy: What data quality means to data consumers. J. Management Inform. Systems 12(4) 5–34.
