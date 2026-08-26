---
otero_id: 3370
otero_key: "FQZ67C7X"
title: "Formulating the Data-Flow Perspective for Business Process Management"
authors: "Sherry X. Sun; J. Leon Zhao; Jay F. Nunamaker; Olivia R. Liu Sheng"
year: "2006"
journal: "Information Systems Research"
doi: "10.1287/isre.1060.0105"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/FQZ67C7X/fulltext/images/c8c8ee6d9820535f5c2a219b087b66621aeff9e97afd7da6fd46374dc15f5d97.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Formulating the Data-Flow Perspective for Business Process Management

Sherry X. Sun, J. Leon Zhao, Jay F. Nunamaker, Olivia R. Liu Sheng,

## To cite this article:

Sherry X. Sun, J. Leon Zhao, Jay F. Nunamaker, Olivia R. Liu Sheng, (2006) Formulating the Data-Flow Perspective for Business Process Management. Information Systems Research 17(4):374-391. http://dx.doi.org/10.1287/isre.1060.0105

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2006, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/FQZ67C7X/fulltext/images/701c747177883bfab5d42e2e6e891a19d24813c86db6a8aff589f7432cc970bd.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Formulating the Data-Flow Perspective for Business Process Management

Sherry X. Sun, J. Leon Zhao, Jay F. Nunamaker

Department of Management Information Systems, University of Arizona, Tucson, Arizona 85721 {xiaoyun@email.arizona.edu, lzhao@eller.arizona.edu, jnunamaker@eller.arizona.edu}

Olivia R. Liu Sheng Accounting and Information Systems, University of Utah, Salt Lake City, Utah 84112, olivia.sheng@business.utah.edu

W orkflow technology has become a standard solution for managing increasingly complex business processes. Successful business process management depends on effective workflow modeling and analysis. One of the important aspects of workflow analysis is the data-flow perspective because, given a syntactically correct process sequence, errors can still occur during workflow execution due to incorrect data-flow specifi cations. However, there have been only scant treatments of the data-flow perspective in the literature and no formal methodologies are available for systematically discovering data-flow errors in a workflow model. As an indication of this research gap, existing commercial workflow management systems do not provide tools for data-flow analysis at design time. In this paper, we provide a data-flow perspective for detecting data-flow anomalies such as missing data, redundant data, and potential data conflicts. Our data-flow framework includes two basic components: data-flow specification and data-flow analysis; these components add more analytical rigor to business process management.

Key words: workflow modeling; data-flow specification; data-flow anomalies; data-flow verification; dependency analysis; process data diagram

History: Sumit Sarkar, Senior Editor; Amit Basu, Associate Editor. This paper was received on May 2, 2005, and was with the authors 7 <sup>1</sup> months for 3 revisions.

## 1. Introduction

Business processes are considered invaluable organizational assets, and the emerging business process revolution offers companies an opportunity to innovate in the way they do business (Smith and Fingar 2003). As a result, corporations are confronted with the challenges of constantly increasing the productivity and efficiency of their business processes. A business process is defined as “the specific ordering of work activities across time and place, with a beginning, an end, and clearly identified input and output” (Davenport 1993). Organizations implement business processes to produce value for customers (Earl et al. 1995). Typically, a business process involves people from different functional units in the same organization and may go across organizational boundaries for reasons of business partnership, considerably increasing the complexity of managing the process (Stohr and Zhao 2001).

As the information technology for business process automation, workflow systems have become a standard solution for managing complex processes in business domains such as supply chain management, customer relationship management, and knowledge management (Stohr and Zhao 2001, Kumar and Zhao 2002, Sarnikar et al. 2004). Successful business process management depends on effective workflow modeling and analysis. Workflow models can represent a business process from five perspectives: functional, behavioral, informational, operational, and organizational (Curtis et al. 1992, Stohr and Zhao 2001). The functional perspective describes what tasks a workflow performs. The behavioral perspective specifies the conditions for tasks to be executed. The information perspective defines what data are consumed and produced with respect to each activity in a business process. The operational perspective specifies what tools and applications are used to execute a particular task. The organizational perspective describes the relationships among personnel that are qualified to perform various job functions.

Current workflow modeling paradigms mainly focus on activity sequencing and coordination, including Petri nets (van der Aalst 1998, van der Aalst and ter Hofstede 2000) and activity-based workflow modeling (Bi and Zhao 2004, Georgakopoulos et al. 1995). However, many business processes such as insurance claims and loan applications involve creation of intermediate data that are critical for proper process execution. The data-flow perspective is important in workflow management because relationships among data elements may drive the operational constraints that control activity sequencing (Kwan and Balasubramanian 1997). For example, in an auto insurance claim workflow, the estimated repair cost is required for claim authorization. Therefore, the activity vehicle inspection, which produces an output of estimated repair cost, must precede the activity claim authorization, which uses estimated repair cost as input. If claim authorization occurs before vehicle inspection, a data-flow error would occur. Obviously, this type of error can only be detected by incorporating data-flow analysis into workflow modeling. Presently, workflow management systems enable the discovery of data-flow errors only through simulation, which is inefficient and inaccurate. A workflow specification that contains data-flow errors can cause unexpected process interruptions, resulting in high costs to debug and fix at run time.

Several informal and formal modeling tools have been proposed to model and analyze data requirements in workflow systems (Bajaj and Ram 2002, Basu and Blanning 2000, Kappel et al. 1995, Reuter and Schwenkreis 1995), but none has focused on discovering data-flow errors in a workflow model. As the first complete framework to analyze data-flow anomalies in workflow management, this paper formulates the data-flow perspective to enable the detection of dataflow anomalies. Specifically, our research goal is to develop a methodology for determining data-flow errors in a given workflow structure.

The contribution of this paper is threefold. First, we formally define three basic types of data-flow errors: missing data, redundant data, and conflicting data. Second, we propose a method for specifying data flow in a workflow model at a very detailed level. Third and most important, we provide an analytical approach for detecting and eliminating the three types of data-flow errors. Our new approach formally establishes the correctness criteria for data-flow modeling. As a theoretical foundation for data-flow verification, these criteria enable systematic and automatic elimination of data-flow errors. We believe that this paper represents an important step toward a formal methodology for data-flow modeling and analysis in business process management.

In §2 of this paper, we review the relevant literature. Section 3 presents a workflow example, which helps illustrate the ideas in this paper. Section 4 introduces a new method for data-flow specification called data-flow matrix and an extension of the unified modeling language (UML) activity diagram that incorporates data input and output. Section 5 defines the three basic types of data-flow anomalies: missing data, redundant data, and conflicting data. Section 6 proposes a dependency-based approach for dataflow verification. Section 7 concludes the paper with a summary of our contribution and an outline of future research directions.

## 2. Literature Review

A workflow model describes a business process and consists of elements such as roles, actors, tools and applications, activities and processes, rules, and data and documents (Kumar and Zhao 1999, Stohr and Zhao 2001). Currently, most workflow modeling paradigms mainly focus on activity sequencing and coordination, i.e., the control flow perspective, such as Petri nets (van der Aalst 1998, van der Aalst and ter Hofstede 2000), activity-based workflow modeling (Georgakopoulos et al. 1995; Bi and Zhao 2003, 2004), object coordination nets (Wirtz et al. 2001), and rulebased process modeling (Lee et al. 1999).

A Petri net uses four components to represent a workflow model: transitions representing activities or tasks, places representing states, tokens representing cases, and directed arcs connecting transitions and places. As a formalism for workflow modeling, Petri nets provide rigorous methods for analysis and verification of control flow (van der Aalst 1998, van der Aalst and ter Hofstede 2000). Syntactic errors in control flow, such as deadlock, activities without termination or activation, and infinite cycles can be discovered through Petri net modeling and analysis (van der Aalst and ter Hofstede 2000).

Activity-based modeling is another paradigm in workflow modeling. The theories of directed graph and propositional logic have been incorporated into this method, leading to a formal modeling language (Bi and Zhao 2003, 2004; Zhao and Bi 2003). The object coordination nets integrate Petri nets with the object-oriented approach, bridging the gap between the design of a workflow and the implementation of workflow software (Wirtz et al. 2001).

In addition, some other models focus on modeling business rules needed to control activity scheduling and role or actor mapping. For example, as a modeling method focusing on business rules, the knowledgebased workflow model can accommodate changes in organizational structures and business rules (Lee et al. 1999).

The above models do not emphasize the data-flow perspective, suggesting that this is an open area of research. Analyzing both data and activities in one single model adds an extra level of complexity, as opposed to only focusing on activities. Therefore, for the purpose of simplicity, these workflow models focus on control flow, and data requirements are either simplified through abstraction in Petri net modeling (van der Aalst and ter Hofstede 2000) or not incorporated at all in activity-based modeling (Bi and Zhao 2004, Zhao and Bi 2003). However, the data-flow perspective, also known as data-usage analysis, is important because activities cannot be executed properly without sufficient information (Basu and Kumar 2002). As a critical component of business process management, the data-flow perspective complements the control-flow perspective and the organizational perspective. Next, we discuss some research areas that are relevant to data usage analysis.

Data flow diagram (DFD) is widely used in systems analysis and design (Yourdon and Constantine 1979). However, a DFD is not sufficient to support formal analysis of data flow, mainly because it lacks an underlying theoretical foundation. As a wellknown modeling methodology, DFD is used to specify the flow of data from external entities, via various data processing steps, into logical data storages (Yourdon and Constantine 1979). However, a DFD only captures activities that are directly related to data processing; those activities that do not involve any data processing are omitted from the DFD. More importantly, the DFD literature offers no analytical tools for examining the correctness of data-flow models. Our research focuses on data-flow analysis in the context of workflow management and the formal methodology we propose enables automatic detection of data-flow anomalies. Therefore, our work goes significantly beyond the DFD framework.

To support data requirement analysis in workflow management, several informal and formal modeling methods have been developed. For instance, as informal approaches, the data model proposed in the ConTracts project can deal with the long duration of transactions in workflow systems (Reuter and Schwenkreis 1995), and the object-oriented database used by Kappel et al. (1995) is primarily oriented to coping with frequently changing requirements in an organization.

In contrast, some recent modeling methods provide more formal analysis techniques such as the state-entity-activity-model (SEAM) and metagraphs. SEAM, a data model recently developed for workflow management, integrates activities and data objects in a single view (Bajaj and Ram 2002). SEAM enables construction of workflow applications using relational database management systems. However, SEAM focuses on database modeling rather than on data-flow analysis.

Metagraphs have been proposed as a workflowmodeling formalism (Basu and Blanning 2000) that combines the notation of directed graphs and hypergraphs (Basu and Blanning 1994a, b). Metagraphs can provide insight on how sets of elements, such as activities, data, and resources, are interrelated because metagraphs can be used to analyze the connectivity between sets of elements. Thus far, the literature on metagraphs has not emphasized the issue of detecting data-flow errors, although, as a language, metagraphs may be used to verify data flows.

Formal program verification, another relevant stream of work from the field of software engineering, uses mathematical proofs to establish consistency between a program and a particular specification (Berg et al. 1982, Mili 1985, Guaspari et al. 1990). Formal program verification can help determine whether a program meets a specification. However, formal program verification differs significantly from dataflow verification. Instead of verifying consistency between a specification and the related execution results, as in formal program verification, data-flow verification focuses on identifying data-flow errors by means of a set of well-defined correctness criteria. In addition, data-flow analysis and control-flow analysis are two intertwined aspects of workflow analysis, and data-flow analysis can be used to validate the correctness of activity sequencing (Sun and Zhao 2004). This unique feature of data-flow analysis distinguishes it further from formal program verification.

At the conceptual level, a data-flow model is considered correct if it is free from a variety of important errors. Sadiq et al. (2004) have started investigating the different problems of data-flow validation and identified the essential requirements of data-flow modeling in workflow management. They define seven types of data anomalies: redundant data, lost data, missing data, mismatched data, inconsistent data, misdirected data, and insufficient data. However, no concrete solutions to the data-flow validation problems have been reported.

In summary, the presence of several modeling paradigms for analyzing data requirements in business process management provides the foundation for data-flow analysis; however, the issue of systematically discovering data-flow errors has not been emphasized in the literature. It is time to develop a formal methodology for data-flow verification in workflow systems. With the correctness criteria we propose, certain existing workflow modeling paradigms, such as the metagraph approach, may be extended to detect data-flow errors. Consequently, our framework on data-flow analysis fills a critical void in the literature of business process management.

## 3. A Business Process Example

This section introduces a property loan approval process shown as a UML activity diagram<sup>1</sup> in Figure 1.

This example is used to illustrate the concepts in this paper. Below, we examine the key steps of this process, involving business decisions, data processing, and activity routing:

1. An application is received.

2. The completeness of the application is verified.

3. The process is routed based on whether or not the application is complete.

4. If the application is not complete, the missing information is requested.

5. To determine the applicant’s qualifications, the financial services company first verifies the applicant’s employment status.

6. To qualify the applicant, the financial services company checks the applicant’s credit history.

7. The financial services company also checks the applicant’s liquid assets.

8. The process is routed according to the applicant’s qualifications. If the applicant is not qualified, the process terminates.

9. If the applicant is qualified, the current interest rate is locked in for a certain period, as requested by the applicant. The interest rate is based on the amount of money the applicant is eligible to borrow.

10. The financial services company requests the appraisal information.

11. The loan application is evaluated. Given the applicant’s credit score, the appraised value of the property, the loan amount, and the level of risk associated with the loan are calculated.

12. The process is routed according to the risk level.

13. If the risk is higher than the applicable threshold, the loan amount must be adjusted.

14. The financial services company contacts the applicant to discuss the necessary adjustment and other conditions, such as property insurance options.

15. The process is routed according to whether the applicant agrees with the necessary adjustment and other conditions. If the applicant disagrees with the conditions and adjustment, the process ends.

16. If the applicant agrees with everything, the application is forwarded to the loan officer for signature after the applicant signs the application.

17. The process is routed based on the loan amount.

18. When the loan amount is more than \$500,000, the manager’s signature is required.

Figure 1 Property Loan Approval Process  
![](/api/attachments/FQZ67C7X/fulltext/images/015693e1928c91368b258f43d4a1bd5d0b9b88b32eaf2ba5fcc6fc8f13142995.jpg)

Table 1 contains the symbols for the activities and data items in this process.

## 4. Data-Flow Specification

In this section, we develop a method for specifying data flow in a workflow system.

## 4.1. Data-Flow Operations

In a workflow, each activity can perform different operations on a data item. We call these operations data-flow operations. Through these operations, data items are produced, accessed, and modified. We classify the data-flow operations in the property loan approval process into initializing, approving, updating, referring, and verifying, according to the semantic meanings of data-flow operations in the business process environment. From the database implementation point of view, all data-flow operations can be considered as either read or write operations, regardless of their semantic meaning.

When analyzing a data flow, we need to know the input and output data for each activity. Categorizing data-flow operations into read or write operations helps identify the input and output data for each activity. It is intuitive that when activity v reads data item d, d is the input data for v, and when v performs a write operation on $d ,$ d is the output data from v. Moreover, there are two types of write operations: creating the initial value, also called initialization; and overwriting the existing value. It is possible for a data item to be overwritten after it is initialized. However, in the interest of simplicity, the current paper focuses only on the initial write operation because initialization is critical for discovering data-flow anomalies.

## 4.2. Data-Flow Matrices

To specify data flow in workflow applications, we introduce the concept of data-flow matrix, a twodimensional table that records the data-flow operations each activity performs on various data items in a workflow. More formally, data-flow matrix can be defined as follows:

Table 1 Symbols Used in the Property Loan Approval Process

<table><tr><td colspan="6">Data items</td></tr><tr><td> $d_1$ </td><td>Applicant name</td><td> $d_8$ </td><td>Account balance</td><td> $d_{15}$ </td><td>Risk</td></tr><tr><td> $d_2$ </td><td>Loan amount</td><td> $d_9$ </td><td>Account balance verified</td><td> $d_{16}$ </td><td>Amount adjusted</td></tr><tr><td> $d_3$ </td><td>Annual income</td><td> $d_{10}$ </td><td>Applicant qualified</td><td> $d_{17}$ </td><td>Agreed by applicants</td></tr><tr><td> $d_4$ </td><td>Application complete</td><td> $d_{11}$ </td><td>Interest rate</td><td> $d_{18}$ </td><td>Property insured</td></tr><tr><td> $d_5$ </td><td>Application summary</td><td> $d_{12}$ </td><td>Property address</td><td> $d_{19}$ </td><td>Signed by applicants</td></tr><tr><td> $d_6$ </td><td>Employment status verified</td><td> $d_{13}$ </td><td>Current owner of property</td><td> $d_{20}$ </td><td>Signed by loan officer</td></tr><tr><td> $d_7$ </td><td>Credit score</td><td> $d_{14}$ </td><td>Appraised value of property</td><td> $d_{21}$ </td><td>Signed by manager</td></tr><tr><td colspan="6">Activities</td></tr><tr><td> $v_1$ </td><td>Receive application</td><td> $v_7$ </td><td>Verify liquid assets</td><td> $v_{14}$ </td><td>Contact applicants for agreement</td></tr><tr><td rowspan="2"> $v_2$ </td><td rowspan="2">Verify completeness of application</td><td> $v_8$ </td><td>Decision Node 2</td><td> $v_{15}$ </td><td>Decision Node 4</td></tr><tr><td> $v_9$ </td><td>Determine interest rate</td><td> $v_{16}$ </td><td>Forward to loan officer for signature</td></tr><tr><td> $v_3$ </td><td>Decision Node 1</td><td> $v_{10}$ </td><td>Request appraisal info</td><td> $v_{17}$ </td><td>Decision Node 5</td></tr><tr><td> $v_4$ </td><td>Request missing info</td><td> $v_{11}$ </td><td>Evaluate loan application</td><td> $v_{18}$ </td><td>Forward to manager for signature</td></tr><tr><td> $v_5$ </td><td>Verify employment status</td><td> $v_{12}$ </td><td>Decision Node 3</td><td>s</td><td>Start node</td></tr><tr><td> $v_6$ </td><td>Check credit history</td><td> $v_{13}$ </td><td>Adjust loan amount</td><td>e</td><td>End node</td></tr><tr><td colspan="6">Operations</td></tr><tr><td>r</td><td>Read</td><td></td><td></td><td></td><td></td></tr><tr><td>w</td><td>Write</td><td></td><td></td><td></td><td></td></tr></table>

Definition 1 (Data-Flow Matrix). <sub>Given the total</sub> number of activities n and the total number of data items $z$ in a workflow W , data-flow matrix M is a n by z table where the element $( i , j )$ shows the operation that activity $v _ { j }$ performs on the data item $d _ { i } .$ Activity $v _ { j }$ is a logical step of work in a business process that can be scheduled by workflow engine during process enactment. Data $d _ { j }$ is an atomic data element that can be stored in a database.

Table 2 shows the data-flow matrix for the property loan approval process. Note that each cell contains no more than one operation for the purpose of data-flow analysis. It is worth noting that Table 2 also includes a special type of control activity nodes

Table 2 Data-Flow Matrix for the Property Loan Approval Process

<table><tr><td colspan="2">Data objects</td><td> ${V}_{1}$ </td><td> ${V}_{2}$ </td><td> ${V}_{3}$ </td><td> ${V}_{4}$ </td><td> ${V}_{5}$ </td><td> ${V}_{6}$ </td><td> ${V}_{7}$ </td><td> ${V}_{8}$ </td><td> ${V}_{9}$ </td><td> ${V}_{10}$ </td><td> ${V}_{11}$ </td><td> ${V}_{12}$ </td><td> ${V}_{13}$ </td><td> ${V}_{14}$ </td><td> ${V}_{15}$ </td><td> ${V}_{16}$ </td><td> ${V}_{17}$ </td><td> ${V}_{18}$ </td></tr><tr><td> ${d}_{1}$ </td><td>Applicant name</td><td>w</td><td>r</td><td></td><td></td><td>r</td><td>r</td><td>r</td><td></td><td>r</td><td>r</td><td>r</td><td></td><td>r</td><td>r</td><td></td><td>r</td><td></td><td>r</td></tr><tr><td> ${d}_{2}$ </td><td>Loan amount</td><td>w</td><td>r</td><td></td><td></td><td></td><td></td><td></td><td></td><td>r</td><td></td><td>r</td><td></td><td></td><td>r</td><td></td><td>r</td><td>r</td><td>r</td></tr><tr><td> ${d}_{3}$ </td><td>Annual income</td><td>w</td><td>r</td><td></td><td></td><td>r</td><td></td><td></td><td></td><td>r</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> ${d}_{4}$ </td><td>Application complete</td><td></td><td>w</td><td>r</td><td>r</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> ${d}_{5}$ </td><td>Application summary</td><td>w</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>r</td></tr><tr><td> ${d}_{6}$ </td><td>Employment status verified</td><td></td><td></td><td></td><td></td><td>w</td><td></td><td></td><td></td><td></td><td></td><td>r</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> ${d}_{7}$ </td><td>Credit score</td><td></td><td></td><td></td><td></td><td></td><td>w</td><td></td><td></td><td>r</td><td></td><td>r</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> ${d}_{8}$ </td><td>Account balance</td><td>w</td><td>r</td><td></td><td></td><td></td><td></td><td>r</td><td></td><td></td><td></td><td>r</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> ${d}_{9}$ </td><td>Account balance verified</td><td></td><td></td><td></td><td></td><td></td><td></td><td>w</td><td></td><td></td><td></td><td>r</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> ${d}_{10}$ </td><td>Applicant qualified</td><td></td><td></td><td></td><td></td><td>w</td><td>w</td><td>w</td><td>r</td><td></td><td></td><td>r</td><td></td><td></td><td>r</td><td></td><td>r</td><td></td><td>r</td></tr><tr><td> ${d}_{11}$ </td><td>Interest rate</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>w</td><td></td><td>r</td><td></td><td>r</td><td></td><td></td><td>r</td><td></td><td>r</td></tr><tr><td> ${d}_{12}$ </td><td>Property address</td><td>w</td><td>r</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>r</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> ${d}_{13}$ </td><td>Current owner of property</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>w</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> ${d}_{14}$ </td><td>Appraised value of property</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>r</td><td>w</td><td>r</td><td></td><td>r</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> ${d}_{15}$ </td><td>Risk</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>w</td><td>r</td><td>r</td><td></td><td></td><td>r</td><td>r</td><td>r</td></tr><tr><td> ${d}_{16}$ </td><td>Amount adjusted</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>r</td><td></td><td></td><td></td><td>w</td><td>r</td><td></td><td>r</td><td>r</td><td>r</td></tr><tr><td> ${d}_{17}$ </td><td>Agreed by applicants</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>w</td><td>r</td><td>r</td><td></td><td>r</td></tr><tr><td> ${d}_{18}$ </td><td>Property insured</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>r</td><td></td><td></td><td></td><td></td></tr><tr><td> ${d}_{19}$ </td><td>Signed by applicants</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>w</td><td>r</td><td>r</td><td></td><td>r</td></tr><tr><td> ${d}_{20}$ </td><td>Signed by loan officer</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>w</td><td></td><td></td></tr><tr><td> ${d}_{21}$ </td><td>Signed by manager</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>w</td></tr></table>

called decision nodes. A decision node uses a set of data items to decide how to route a workflow instance by choosing an activity for execution from a set of optional activities. For instance, Decision Node 1 $( \mathrm { i . e . , }$ , activity $v _ { 3 } )$ uses $d _ { 4 } ,$ application complete, as input to decide the next activity to be executed. If $d _ { 4 } = \Nu 0 ,$ activity $v _ { 4 } ,$ request missing info, will be executed. Otherwise, activity $v _ { 5 } ,$ verify employment status, activity $v _ { 6 } ,$ check credit history, and activity $v _ { 7 } ,$ verify liquid assets, will be executed. Decision nodes should be included in the data-flow matrix because they require input data. A data-flow matrix can contain activities that do not generate output data. If the primary function of an activity is routing control, the activity may not generate an output data. With a dataflow matrix, we can easily find out how each data item is processed in a workflow.

## 4.3. Integration of Data Flow in the Workflow Model

Data-flow information can be integrated into the control flow model as shown in Figure 2, where the input and output data are shown in the activity diagram. In a UML activity diagram, object flows can be used to describe the input and output for an activity. Each object is connected to one or more activities, indicating an action-object relationship. However, the object flow is insufficient for modeling data flow in workflow management because it provides no details on how different data items associated with one object are processed differently in a workflow. Therefore, we extend the UML activity diagram to show how each individual data item is produced and used in a workflow.

Figure 2 Process Data Diagram for the Property Loan Approval Process  
![](/api/attachments/FQZ67C7X/fulltext/images/8b15852ddac08f89184f0cc41a04d8ab4919909ef20f09d453f8e76d74d3b278.jpg)

Figure 2 provides a graphic representation for the data flow in the loan approval process. In Figure $^ { 2 , }$ each regular activity is associated with two sets of data: the input data set following the symbol I and the output data set following the symbol O. Each decision node uses a set of input data to decide the route for a workflow instance. If an activity v performs a read operation on a data item d in the data-flow matrix, d is shown as an input data of v in Figure 2. If an activity v performs a write operation on a data item d in the data-flow matrix, d is shown as an output data of v in Figure 2. The detailed data-flow specification shown in Figure 2 is a prerequisite for analyzing the correctness of a data flow. The symbol $c _ { i }$ indicates routing conditions that will be detailed in §6.

## 5. Data-Flow Anomalies

In a workflow, each activity contributes to the production of final output data by generating either some intermediate output data or a subset of the final output data. Meanwhile, each activity may need a set of data as input, which may be produced by other activities in the same workflow or by sources external to the workflow. If the data flow is not specified correctly in a workflow system, errors and conflicts can occur, referred to as data-flow anomalies (Sun et al. 2004). Data-flow anomalies can be classified into three types: missing data, redundant data, and conflicting data, as discussed next.

## 5.1. Missing Data

When a data item is accessed before it is initialized, a missing data anomaly occurs. Each of the following scenarios can cause missing data anomalies.

Scenario 1 (Absence of Initialization). <sub>A data</sub> item is never assigned an initial value; however, some activities use it as input or it is required as the final output of the workflow.

<sup>Example</sup> <sup>1.</sup> As Table 2 shows, data item $d _ { 1 8 } ,$ property insured, has never been initialized, but activity $v _ { 1 4 }$ reads it as input data. This is a missing data anomaly.

Scenario 2 (Delayed Initialization). <sub>A</sub> <sub>data</sub> <sub>item</sub> is used by activity v as input, but it is initialized only by another activity that is executed after v is performed.

<sup>Example</sup> <sup>2.</sup> In the property loan approval process, activity $v _ { 9 } ,$ determine interest rate, reads data item $d _ { 1 6 } ,$ amount adjusted, which is initialized by activity $v _ { 1 3 } ,$ adjust loan amount. However, as shown in Figure 2, $v _ { 1 3 }$ is executed after $v _ { 9 } .$ . Therefore, when $v _ { 9 }$ is executed, the data item $d _ { 1 6 }$ has not been initialized, leading to another missing data anomaly.

Scenario 3 (Uncertain Availability). <sub>Given</sub> <sub>two</sub> parallel activities, v and u, v needs an input data item initialized by u. When v is executed, the data item may not have been initialized.

<sup>Example</sup> <sup>3.</sup> In the property loan approval process, to calculate the interest rate, activity $v _ { 9 } ,$ , determine interest rate, reads data item $d _ { 1 4 } ,$ appraised value of property, which is produced by activity $v _ { 1 0 } ,$ request appraisal info (shown in Table 2 and Figure 2). According to the control flow in Figure 2, $v _ { 9 }$ and $v _ { 1 0 }$ are executed in parallel; therefore, when $d _ { 1 4 }$ is read by $v _ { 9 } ,$ there is a chance that $v _ { 1 0 }$ has not initialized $d _ { 1 4 } ,$ leading to another missing data anomaly in this workflow.

Scenario 4 (Improper Routing). <sub>Under</sub> <sub>certain</sub> workflow routing conditions, a data item is not initialized, although it is used by some activities as input.

<sup>Example</sup> <sup>4.</sup> In the property loan approval process, the output data $d _ { 1 7 } ,$ , agreed by applicants, and $d _ { 1 9 } ,$ signed by applicants, are produced by activity $v _ { 1 4 } ,$ contact applicants for agreement, only when the risk is high, as shown in Figure 2. However, even when the risk is low, $d _ { 1 7 }$ and $d _ { 1 9 }$ are also read as input by activities $v _ { 1 5 } ,$ Decision Node 4, $v _ { 1 6 } ,$ forward to loan officer for signature, and $v _ { 1 8 } ,$ forward to manager for signature. Therefore, another missing data anomaly occurs.

## 5.2. Redundant Data

If an activity produces data items that do not contribute to the production of the final output data, then there is a redundant data anomaly. Redundant data cause inefficiency. The two following scenarios can cause redundant data anomalies.

Scenario 5 (Inevitable Redundancy). <sub>A</sub> <sub>data</sub> <sub>item</sub> is produced as an intermediate data output; however, no other activities need it as input data and it is not part of the final output data.

<sup>Example</sup> <sup>5.</sup> In Figure 2, data item $d _ { 1 3 } ,$ current owner of property, produced by activity $v _ { 1 0 } ,$ request appraisal info, is neither used by any other activities in the process nor required as the final data output of the process. Hence, $d _ { 1 3 }$ is redundant and can be eliminated.

Scenario 6 (Contingent Redundancy). <sub>A data</sub> item is produced as an intermediate data output. However, it is used only under some routing conditions. Under other routing conditions, that data item is not used by any activities as input.

<sup>Example</sup> <sup>6.</sup> As shown in Figure 2, data item $d _ { 5 } ,$ application summary, is only required by activity $v _ { 1 8 } ,$ forward to manager for signature, if the loan amount is greater than \$500,000. When the loan amount is less than \$500,000 the application summary is still produced but is not needed by any activities.

## 5.3. Conflicting Data

In a workflow instance, if there exist different versions of the same data item, conflicting data anomalies occur. When conflicting data anomalies occur, it is impossible to decide which version of the data item should be taken unless we have appropriate rules that define the way to draw a final conclusion. The following scenario can cause conflicting data anomalies.

Scenario 7 (Multiple Initializations). <sub>More than</sub> one activity attempts to initialize the same data item in one workflow instance.

<sup>Example</sup> <sup>7.</sup> In Figure 2, activities $v _ { 5 } ,$ verify employment status, $v _ { 6 } ,$ check credit history, and $v _ { 7 } ,$ verify liquid assets, all make decisions on whether the applicant is qualified for the loan, i.e., they all produce data item $d _ { 1 0 }$ as output. When one activity qualifies the applicant and one activity disqualifies the applicant, we have trouble deciding if the applicant is or is not qualified.

This paper takes a minimalist approach and defines three basic data-flow anomalies—missing data, redundant data, and conflicting data—because the definition of these three types of data-flow anomalies is sufficient in analyzing the data-flow requirements at the conceptual level. We can show that the seven types of data-flow anomalies proposed by Sadiq et al.

(2004) can either be represented by these three basic data-flow anomalies or are not a problem at the conceptual level, as follows:

• Missing data and redundant data are defined similarly. Missing data occur when a data item needed by one activity is not available at the time of use, and redundant data occur when an unnecessary data item is produced.

• Lost data occur when an initialization is overwritten by another activity. It is caused by what we refer to as conflicting data.

• Mismatched data arise when the structure of an output data item is incompatible with the structure required by the activity that uses the data item as input. Mismatched data can be regarded as the occurrence of both redundant data and missing data.

• Inconsistent data happen when the initial data input for a workflow is updated externally while the workflow is still being executed, resulting in an inconsistent view of the data. Inconsistent data is not a problem at the conceptual level and should be dealt with at the operational level.

• Misdirected data occur when the data-flow direction is not consistent with the control flow in a workflow model. Misdirected data is classified as missing data in our framework.

• Insufficient data happen when no sufficient data are specified for a successful completion of a workflow. It is an issue due to ill-designed activities and can be categorized into missing data at the semantic level.

In summary, using the three types, instead of seven types, of data-flow anomalies makes data-flow analysis more manageable and covers the key issues of ensuring data-flow integrity at the conceptual level.

## 6. Activity Dependency Analysis for Data-Flow Verification

In this section, we propose a dependency-based approach for data-flow analysis. Table 3 shows all the symbols used in this section.

## 6.1. Basic Concepts

Next, we define the concept of workflow routing constraint that specifies how a workflow instance is routed. The concept of routing constraint is similar to that of routing rules found in (Kumar and Zhao 1999). However, we use a simple predicate logic format rather than following the event-role-object-conditionaction format since the simpler format is sufficient for the purpose of data-flow analysis in this paper.

Table 3 Symbols Used in Data-Flow Verification

<table><tr><td>c, ci</td><td>workflow routing constraint</td><td> $O_v$ </td><td>the set of data items as output of activity v</td></tr><tr><td>s</td><td>start activity</td><td>C</td><td>workflow routing constraint set</td></tr><tr><td>e</td><td>end activity</td><td> $C_w$ </td><td>the routing constraint set for W</td></tr><tr><td>x, y, u, v,  $v_i$ ,  $v_j$ ,  $v_{temp}$ </td><td>any activity</td><td> $C_v^u$ ,  $C_v^d$ ,  $C_v^i$ </td><td>upstream, downstream, or irrelevant routing constraint sets for activity v</td></tr><tr><td>V,  $V_{temp}$ </td><td>a set of activities</td><td> $\lambda_v^u$ </td><td>unconditional data dependency for activity v, and v is any activity including s and e</td></tr><tr><td>W</td><td>control-flow model</td><td> $\lambda_v^c$ </td><td>conditional data dependency for activity v, and v is any activity including s and e</td></tr><tr><td>M</td><td>data-flow matrix</td><td>⇒</td><td>activity dependency</td></tr><tr><td> $I^e$ </td><td>the overall set of external data to W,  $I^e = \bigcup I_i^e$ </td><td> $\Delta^u$ </td><td>unconditional requisite set</td></tr><tr><td> $I_i^e$ </td><td>the set of external data at activity  $v_i$ </td><td> $\Delta^c$ </td><td>conditional requisite set</td></tr><tr><td> $O_0$ </td><td>the set of data items as final output from W</td><td>Γ</td><td>instance set</td></tr><tr><td>d,  $d_i$ </td><td>data item</td><td> $\Gamma_w$ </td><td>all the instance sets of W</td></tr><tr><td> $I_{vi}$ ,  $I_i$ </td><td>the set of data items as input for activity  $v_i$ </td><td> $\bigcup_{i=1}^n I_i$ </td><td>the union of the input data sets of all the activities in W</td></tr><tr><td> $I_v^u$ </td><td>the unconditional input data set for activity v</td><td> $\bigcup_{i=1}^n O_i$ </td><td>the union of the output data from all the activities in W</td></tr><tr><td> $I_v^c$ </td><td>the conditional input data set for activity v</td><td></td><td></td></tr></table>

Definition 2 (Decision Variable). <sub>A</sub> <sub>routing</sub> <sub>deci-</sub> sion can be made based on a set of data items inputted to the decision node. Each of such data items involved in a routing decision is called a decision variable.

In the property loan approval process, Decision Node 1 uses the data item $d _ { 4 } ,$ application complete, to route a workflow instance (Table 2). Therefore $d _ { 4 }$ is a decision variable. The set of possible values for $d _ { 4 }$ is Yes No.

Definition 3 (Routing Constraint). <sub>A</sub> <sub>workflow</sub> routing constraint c is defined as a logic formula used to route a workflow instance where a set of decision variables is quantified.

A decision node can use a set of routing constraints to route a workflow instance, with each routing constraint corresponding to one arc leaving from a decision node. For example, in the property loan approval process, when $d _ { 1 7 } = \mathrm { Y e s }$ and $d _ { 1 9 } = \mathrm { Y e s } _ { \mathrm { \tiny { 1 9 } } }$ , i.e., the loan conditions are agreed on and signed by the applicants, Decision Node 4 routes the application to the loan officer for signature. When $d _ { 1 7 } = \mathrm { N o }$ and $d _ { 1 9 } = \mathrm { N o } ,$ , Decision Node 4 routes the application to the end of the workflow. Therefore, the routing constraint set used by Decision Node 4 is $C = \{ c _ { 7 } = ( d _ { 1 7 } =$ Yes and $d _ { 1 9 } = \mathrm { Y e s } )$ $c _ { 8 } = ( d _ { 1 7 } = \mathrm { N o }$ and $d _ { 1 9 } = \mathrm { N o } ) \}$ Table 4 shows all the routing constraints used in the property loan approval process, each of which can be mapped to an arc as previously illustrated in Figure 2.

Definition 4 (Routing Constraint Set for <sup>Workflow).</sup> Given a workflow W , all its routing constraints (possibly represented in clausal form) constitute the routing constraint set for $W ,$ denoted as $C _ { w } .$

There are a total of seven decision variables in the property loan approval process $( d _ { 2 } , \ d _ { 4 } , \ d _ { 1 0 } , \ d _ { 1 5 } ,$ $d _ { 1 6 } , d _ { 1 7 } ,$ , and $d _ { 1 9 } )$ , collectively configuring a workflow instance. The routing constraint set for this workflow can be written as $C _ { w } = \{ c _ { 1 } \lor c _ { 2 } , c _ { 3 } \lor c _ { 4 } , c _ { 5 } \lor c _ { 6 } ,$ $c _ { 7 } \vee c _ { 8 } , c _ { 9 } \vee c _ { 1 0 } \big \}$ , where $c _ { i } \vee c _ { i } ( i = 1 , 3 , 5 , 7 , 9 ; ~ j =$ $2 , 4 , 6 , 8 , 1 0 )$ indicates that $c _ { i }$ and $c _ { j }$ are mutually exclusive so that only one of them can be triggered.

Definition 5 (Upstream and Downstream Routing Constraint Sets for Activities). <sub>The</sub> <sub>upstream</sub> routing constraint set $C _ { v } ^ { u }$ for activity v is defined as the set of routing constraints needed for workflow $W$ to execute v. The downstream routing constraint set $C _ { v } ^ { d }$ for activity v is defined as the set of routing constraints for W to execute the downstream activities of v, i.e., those activities to be executed after v. Routing constraints not included in $C _ { v } ^ { u }$ or $C _ { v } ^ { d }$ form the irrelevant routing constraint set of $v ,$ denoted as $C _ { v } ^ { i } .$ $C _ { v } ^ { u } , C _ { v } ^ { d } ,$ , and $C _ { v } ^ { i }$ are mutually exclusive.

Table 4 Routing Constraints in the Property Loan Approval Process

<table><tr><td> $c_{1} = (d_{4} = \text{Yes})$ </td><td> $c_{7} = (d_{17} = \text{Yes AND } d_{19} = \text{Yes})$ </td></tr><tr><td> $c_{2} = (d_{4} = \text{No})$ </td><td> $c_{8} = (d_{17} = \text{No AND } d_{19} = \text{No})$ </td></tr><tr><td> $c_{3} = (d_{10} = \text{Yes})$ </td><td rowspan="2"> $c_{9} = ((d_{15} = \text{High AND } d_{16} > 500,000) \text{ OR } (d_{15} = \text{Low AND } d_{2} > 500,000))$ </td></tr><tr><td> $c_{4} = (d_{10} = \text{No})$ </td></tr><tr><td> $c_{5} = (d_{15} = \text{High})$ </td><td rowspan="2"> $c_{10} = ((d_{15} = \text{High AND } d_{16} \leq 500,000) \text{ OR } (d_{15} = \text{Low AND } d_{2} \leq 500,000))$ </td></tr><tr><td> $c_{6} = (d_{15} = \text{Low})$ </td></tr></table>

Table 5 Upstream and Downstream Routing Constraint Sets

<table><tr><td>Activity</td><td> $C_v^u$ </td><td> $C_v^d$ </td><td> $C_v^i$ </td></tr><tr><td> $V_1, V_2, V_3$ </td><td>∅</td><td> $\{C_1, C_2, C_3, C_4, C_5, C_6, C_7, C_8, C_9, C_{10}\}$ </td><td>∅</td></tr><tr><td> $V_4$ </td><td> $\{C_2\}$ </td><td> $\{C_1, C_3, C_4, C_5, C_6, C_7, C_8, C_9, C_{10}\}$ </td><td>∅</td></tr><tr><td> $V_5, V_6, V_7, V_8$ </td><td> $\{C_1\}$ </td><td> $\{C_3, C_4, C_5, C_6, C_7, C_8, C_9, C_{10}\}$ </td><td> $\{C_2\}$ </td></tr><tr><td> $V_9, V_{10}, V_{11}, V_{12}$ </td><td> $\{C_1, C_3\}$ </td><td> $\{C_5, C_6, C_7, C_8, C_9, C_{10}\}$ </td><td> $\{C_2, C_4\}$ </td></tr><tr><td> $V_{13}, V_{14}$ </td><td> $\{C_1, C_3, C_5\}$ </td><td> $\{C_7, C_8, C_9, C_{10}\}$ </td><td> $\{C_2, C_4, C_6\}$ </td></tr><tr><td> $V_{15}$ </td><td> $\{C_1, C_3, C_5 \lor C_6\}$ </td><td> $\{C_7, C_8, C_9, C_{10}\}$ </td><td> $\{C_2, C_4\}$ </td></tr><tr><td> $V_{16}, V_{17}$ </td><td> $\{C_1, C_3, C_5 \lor C_6, C_7\}$ </td><td> $\{C_9, C_{10}\}$ </td><td> $\{C_2, C_4, C_8\}$ </td></tr><tr><td> $V_{18}$ </td><td> $\{C_1, C_3, C_5 \lor C_6, C_7, C_9\}$ </td><td>∅</td><td> $\{C_2, C_4, C_8, C_{10}\}$ </td></tr></table>

Table 5 shows the upstream $( C _ { v } ^ { u } ) _ { \cdot }$ , downstream $( C _ { v } ^ { d } ) ,$ and irrelevant $( C _ { v } ^ { i } )$ routing constraint sets for the activities in the property loan approval process. Some activities, such as $v _ { 1 } , \ v _ { 2 } ,$ and $v _ { 3 } ,$ have the same upstream $\left( C _ { v } ^ { u } \right)$ , downstream $( C _ { v } ^ { d } )$ , and irrelevant $( C _ { v } ^ { i } )$ routing constraint sets, and they are always executed in the same workflow instance. When a loop occurs, the routing constraint c that causes the execution of an activity v in the loop is considered as the upstream routing constraint for v only if c is needed in order to execute v. For example, the routing constraint $c _ { 2 }$ is always needed to execute activity $v _ { 4 } .$ . Thus, $c _ { 2 }$ is the upstream routing constraint for $v _ { 4 } .$ . Furthermore, $c _ { 2 }$ is not the upstream routing constraint for $v _ { 1 }$ and $v _ { 2 }$ because it is possible to execute activities $v _ { 1 }$ and $v _ { 2 }$ with or without $c _ { 2 }$

In a workflow, an activity depends on data produced by other activities, leading to activity dependencies. Next, we define two basic concepts, data dependency and activity dependency. There are two types of dependencies, unconditional and conditional, as defined below.

Definition 6 (Unconditional Input Data Set). The unconditional input data set for activity v is the set of data items that activity v always requires as input in order to produce an output and each of such data items is called an unconditional input data item of v. The unconditional input data set for activity v is denoted as $I _ { v } ^ { u } = [ i _ { 1 } , i _ { 2 } , \ldots , i _ { m } ] .$ , where $i _ { j }$ is the jth unconditional input data item and m is the total count of unconditional input data items needed by v.

Definition 7 (Conditional Input Data Set). <sub>The</sub> conditional input data set for activity v is the set of data items that activity v requires as input only when C is satisfied where $C \subseteq C _ { w }$ and each of such data items is called a conditional input data item of v. The conditional input data set for activity v is denoted as $I _ { v } ^ { c } = [ i _ { 1 } , i _ { 2 } , \ldots , i _ { n } ] .$ , where $i _ { j }$ is the jth conditional input data item and n is the total count of conditional input data items needed by v.

For instance, in the property loan approval process, the activities $v _ { 3 } ,$ Decision Node 1, and $v _ { 4 } ,$ request missing info, always use data item $d _ { 4 } ,$ application complete, as data input. Hence, activities $v _ { 3 }$ and $v _ { 4 }$ have the same unconditional input data set, i.e., the set containing only $d _ { 4 } .$ . It is different for activity $v _ { 1 6 } ,$ forward to loan officer for signature. When the risk level is high, in addition to the other data items that $v _ { 1 6 }$ always needs, $v _ { 1 6 }$ also needs the data item $d _ { 1 6 } ,$ amount adjusted, as input. Hence, the conditional input data set for $v _ { 1 6 }$ is the set containing $d _ { 1 6 } .$

Definition 8 (Unconditional Data Dependency). The unconditional data dependency for activity $v ,$ denoted as $\lambda _ { v } ^ { u } ( I _ { v } ^ { u } , O _ { v } )$ , represents the unconditional dependency of $O _ { v }$ on $I _ { v } ^ { u } ,$ , where $I _ { v } ^ { u }$ is the unconditional input data set for v (Definition 6) and $O _ { v } = \left[ o _ { 1 } , o _ { 2 } , \dots , o _ { k } \right]$ is the set of k output data items produced by v.

Definition 9 (Conditional Data Dependency). The conditional data dependency for activity $v ,$ denoted as $\lambda _ { v } ^ { c } ( I _ { v } ^ { c } , O _ { v } )$ , represents the conditional dependency of $O _ { v }$ on ${ \cal I } _ { v } ^ { c } ,$ where $I _ { v } ^ { c }$ is the conditional input data set for v (Definition 7) and $O _ { v } = \left[ o _ { 1 } , o _ { 2 } , \ldots , o _ { k } \right]$ is the set of k output data items produced by v.

In the property loan approval process, there is a conditional data dependency for activity $v _ { 1 6 } ,$ , forward to loan officer for signature, where the input data item $d _ { 1 6 } ,$ amount adjusted, may be null depending on the risk level. When the risk level is low, activity $v _ { 1 3 } ,$ adjust loan amount, is not activated. Therefore, $d _ { 1 6 }$ is not initialized under this condition, but activity $v _ { 1 6 }$ can still be activated. Hence, $v _ { 1 6 }$ has a conditional dependency on $d _ { 1 6 } , \mathrm { i } . \mathbf { e } . , v _ { 1 6 }$ depends on $d _ { 1 6 }$ only when the risk level is high. This conditional dependency is denoted as $\lambda _ { v _ { 1 6 } } ^ { c } ( [ d _ { 1 6 } ] , [ d _ { 2 0 } ] )$ . Table 6 shows the unconditional and conditional data dependencies in the property loan approval process.

Definition 10 (Activity Dependency2). <sub>Given two</sub> activities, v and u, v is dependent on u, denoted as $u \Rightarrow v$ , if (I) d such that $d \in O _ { u } , d \notin I ^ { e } .$ , and $d \in I _ { v } ,$ or (II) $u \Rightarrow x$ and $x \Rightarrow v$ where x is some activity.

Table 6 Data Dependencies for Property Loan Approval Workflow

<table><tr><td colspan="4">Unconditional data dependencies</td></tr><tr><td> $\lambda_{v_1}^u$ </td><td> $(\phi, [d_1, d_2, d_3, d_5, d_8, d_{12}])$ </td><td> $\lambda_{v_{10}}^u$ </td><td> $([d_1, d_{12}], [d_{13}, d_{14}])$ </td></tr><tr><td> $\lambda_{v_2}^u$ </td><td> $([d_1, d_2, d_3, d_8, d_{12}], [d_4])$ </td><td> $\lambda_{v_{11}}^u$ </td><td> $([d_1, d_2, d_6, d_7, d_8, d_9, d_{10}, d_{11}, d_{14}], [d_{15}]$ </td></tr><tr><td> $\lambda_{v_3}^u$ </td><td> $([d_4], \phi)$ </td><td> $\lambda_{v_{12}}^u$ </td><td> $([d_{15}], \phi)$ </td></tr><tr><td> $\lambda_{v_4}^u$ </td><td> $([d_4], \phi)$ </td><td> $\lambda_{v_{13}}^u$ </td><td> $([d_1, d_{11}, d_{14}, d_{15}], [d_{16}])$ </td></tr><tr><td> $\lambda_{v_5}^u$ </td><td> $([d_1, d_3], [d_6, d_{10}])$ </td><td> $\lambda_{v_{14}}^u$ </td><td> $([d_1, d_2, d_{10}, d_{18}], [d_{17}, d_{19}])$ </td></tr><tr><td> $\lambda_{v_6}^u$ </td><td> $([d_1], [d_7, d_{10}])$ </td><td> $\lambda_{v_{15}}^u$ </td><td> $([d_{17}, d_{19}], \phi)$ </td></tr><tr><td> $\lambda_{v_7}^u$ </td><td> $([d_1, d_8], [d_9, d_{10}])$ </td><td> $\lambda_{v_{16}}^u$ </td><td> $([d_1, d_2, d_{10}, d_{11}, d_{15}, d_{17}, d_{19}], [d_{20}])$ </td></tr><tr><td> $\lambda_{v_8}^u$ </td><td> $([d_{10}], \phi)$ </td><td> $\lambda_{v_{17}}^u$ </td><td> $([d_{15}], \phi)$ </td></tr><tr><td> $\lambda_{v_9}^u$ </td><td> $([d_1, d_2, d_3, d_7, d_{14}], [d_{11}])$ </td><td> $\lambda_{v_{18}}^u$ </td><td> $([d_1, d_2, d_5, d_{10}, d_{11}, d_{15}, d_{17}, d_{19}], [d_{21}])$ </td></tr><tr><td></td><td></td><td> $\lambda_e^u$ </td><td> $([d_{10}], [d_{10}])$ </td></tr><tr><td colspan="4">Conditional data dependency</td></tr><tr><td> $\lambda_{v_9}^c$ </td><td> $([d_{16}], [d_{11}])$ </td><td> $\lambda_{v_{18}}^c$ </td><td> $([d_{16}], [d_{21}])$ </td></tr><tr><td> $\lambda_{v_{14}}^c$ </td><td> $([d_{16}], [d_{17}, d_{19}])$ </td><td> $\lambda_e^c$ </td><td> $([d_1, d_{11}, d_{15}, d_{16}, d_{17}, d_{19}, d_{20}, d_{21}], [d_1, d_{11}, d_{15}, d_{16}, d_{17}, d_{19}, d_{20}, d_{21}])$ </td></tr><tr><td> $\lambda_{v_{16}}^c$ </td><td> $([d_{16}], [d_{20}])$ </td><td></td><td></td></tr><tr><td> $\lambda_{v_{17}}^c$ </td><td> $([d_2, d_{16}], \phi)$ </td><td></td><td></td></tr></table>

Informally, we say that v is unconditionally dependent on u if u provides unconditional input data for activity v. If u provides conditional input data for activity $v ,$ we say that v is conditionally dependent on u. If there is no dependency between u and $v ,$ we denote the nondependency between them as $u \propto v .$ If x depends on u conditionally and v depends on x unconditionally, or if x depends on u unconditionally and v depends on x conditionally, there is conditional dependency between u and v. Mutual dependency, i.e., $u \Rightarrow v$ and $v \Rightarrow u ,$ is not allowed.

Definition 11 (Unconditional Requisite Set). The set of activities $\Delta _ { v } ^ { u }$ is the unconditional requisite set for activity $v \operatorname { i f } ,$ for any activity $x \in \Delta _ { v } ^ { u } ,$ there exists a data item d such that $d \in O _ { x } , d \notin I ^ { e } ,$ , and $d \in I _ { v } ^ { u }$

Definition 12 (Conditional Requisite Set). <sub>The</sub> set of activities $\Delta _ { v } ^ { c }$ is the conditional requisite set for activity v if for any activity $x \in \Delta _ { v } ^ { c }$ there exists a data item $d ,$ such that $d \in O _ { x } , d \notin I ^ { e } ,$ , and $d \in I _ { v } ^ { c }$

Activity dependencies can be derived from data dependencies. For example, the unconditional input data set for activity $v _ { 5 } ,$ verify employment status, includes data item $d _ { 1 }$ and $d _ { 3 } .$ . As shown in Figure $^ { 2 , }$ $d _ { 1 }$ and $d _ { 3 }$ are the data output from activity $v _ { 1 } ,$ receive application. Therefore, activity $v _ { 5 }$ depends on activity $v _ { 1 }$ through $d _ { 1 }$ and $d _ { 3 } .$ . The requisite set for activity v is the set of activities that provide the data set used by activity v as either unconditional input or conditional input. Table 7 shows the requisite sets for the activities in the property loan approval process. From Table $^ { 7 , }$ we know that most activities depend on activity $v _ { 1 } ,$ receive application, to provide necessary input data.

Table 7 Activity Dependencies for the Property Loan Approval Process

<table><tr><td>Activities</td><td>Unconditional requisite set</td><td>Conditional requisite set</td></tr><tr><td> $V_1$ </td><td> $\emptyset \Rightarrow V_1$ </td><td></td></tr><tr><td> $V_2$ </td><td> $\{V_1\} \Rightarrow V_2$ </td><td></td></tr><tr><td> $V_3$ </td><td> $\{V_2\} \Rightarrow V_3$ </td><td></td></tr><tr><td> $V_4$ </td><td> $\{V_2\} \Rightarrow V_4$ </td><td></td></tr><tr><td> $V_5$ </td><td> $\{V_1\} \Rightarrow V_5$ </td><td></td></tr><tr><td> $V_6$ </td><td> $\{V_1\} \Rightarrow V_6$ </td><td></td></tr><tr><td> $V_7$ </td><td> $\{V_1\} \Rightarrow V_7$ </td><td></td></tr><tr><td> $V_8$ </td><td> $\{V_5, V_6, V_7\} \Rightarrow V_8$ </td><td></td></tr><tr><td> $V_9$ </td><td> $\{V_1, V_6, V_{10}\} \Rightarrow V_9$ </td><td> $\{V_{13}\} \Rightarrow V_9$ </td></tr><tr><td> $V_{10}$ </td><td> $\{V_1\} \Rightarrow V_{10}$ </td><td></td></tr><tr><td> $V_{11}$ </td><td> $\{V_1, V_5, V_6, V_7, V_9, V_{10}\} \Rightarrow V_{11}$ </td><td></td></tr><tr><td> $V_{12}$ </td><td> $\{V_{11}\} \Rightarrow V_{12}$ </td><td></td></tr><tr><td> $V_{13}$ </td><td> $\{V_1, V_9, V_{10}, V_{11}\} \Rightarrow V_{13}$ </td><td></td></tr><tr><td> $V_{14}$ </td><td> $\{V_1, V_5, V_6, V_7\} \Rightarrow V_{14}$ </td><td> $\{V_{13}\} \Rightarrow V_{14}$ </td></tr><tr><td> $V_{15}$ </td><td> $\{V_{14}\} \Rightarrow V_{15}$ </td><td></td></tr><tr><td> $V_{16}$ </td><td> $\{V_1, V_5, V_6, V_7, V_9, V_{11}, V_{14}\} \Rightarrow V_{16}$ </td><td> $\{V_{13}\} \Rightarrow V_{16}$ </td></tr><tr><td> $V_{17}$ </td><td> $\{V_{11}\} \Rightarrow V_{17}$ </td><td> $\{V_1, V_{13}\} \Rightarrow V_{17}$ </td></tr><tr><td> $V_{18}$ </td><td> $\{V_1, V_5, V_6, V_7, V_9, V_{11}, V_{14}\} \Rightarrow V_{18}$ </td><td> $\{V_{13}\} \Rightarrow V_{18}$ </td></tr></table>

Moreover, activities $v _ { 9 } , v _ { 1 4 } , v _ { 1 6 } , v _ { 1 7 } ,$ , and $v _ { 1 8 }$ depend on activity $v _ { 1 3 } ,$ adjust loan amount, conditionally.

Definition 13 (Instance Set). <sub>For</sub> <sub>any</sub> <sub>successful</sub> enactment of a workflow, a set of activities is executed in a specified order from the start activity s to the end activity $e ,$ requiring a set of routing constraints $C \subseteq C _ { w }$ to be satisfied. We refer to this set of activities as an instance set, denoted as . The corresponding set C is called the routing constraint set of  .

Table 8 shows some examples of instance sets for the property loan approval process. Essentially, each instance set is the set of activities that are executed in one workflow instance. For example, when a complete application is received but the applicant is not qualified, only the activities in the instance set $\Gamma _ { 1 }$ are executed. Table 8 also shows the corresponding routing constraint set for each instance set.

Table 8 Instance Sets for the Property Loan Approval Process

<table><tr><td>Instance set</td><td>Corresponding routing constraint set</td></tr><tr><td> $\Gamma_1 = \{s, v_1, v_2, v_3, v_5, v_6, v_7, v_8, e\}$ </td><td> $C_1 = \{c_1, c_4\}$ </td></tr><tr><td> $\Gamma_2 = \{s, v_1, v_2, v_3, v_5, v_6, v_7, v_8, v_9,$  $v_{10}, v_{11}, v_{12}, v_{13}, v_{14}, v_{15}, e\}$ </td><td> $C_2 = \{c_1, c_3, c_5, c_8\}$ </td></tr><tr><td> $\Gamma_3 = \{s, v_1, v_2, v_3, v_5, v_6, v_7, v_8, v_9,$  $v_{10}, v_{11}, v_{12}, v_{15}, v_{16}, v_{17}, v_{18}, e\}$ </td><td> $C_3 = \{c_1, c_3, c_6, c_7, c_9\}$ </td></tr></table>

## 6.2. Data-Flow Verification Rules

Data-flow verification is the process of analyzing dataflow requirements and detecting data-flow anomalies in a business process. Next, we present lemmas and theorems that give rise to data-flow verification rules, which lay the foundation for discovering data-flow anomalies in business processes. For the relatively simple lemmas, we only provide an informal discussion, but for the more complex lemmas and theorems, a formal proof is given.

Lemma 1 (Condition for Absence of Initializa-<sup>tion).</sup> Given a data item d that d $\textstyle \left( I ^ { e } \cup ( \bigcup _ { i = 1 } ^ { n } O _ { i } ) \right)$ and $d \in I _ { i } \ ( i = 1 , 2 , \ldots , n )$ or $d \in O _ { 0 } , a$ missing data anomaly occurs in at least one instance of the workflow W .

Discussion. <sub>Given</sub> <sub>d</sub> $\mathbf { \Psi } \cdot \in I _ { i }$ or $d \in O _ { 0 } ,$ , d is used as input by some activities or required as the final output from at least one workflow instance of W . Given $d \not \in ( I ^ { e } \cup ( \bigcup _ { i = 1 } ^ { n } O _ { i } ) )$ , d is neither provided by any external resources nor produced by any activities. Therefore, d would not be initialized, even though it is used as input, leading to a missing data anomaly.

Lemma 2 (Condition for Delayed Initializa-<sup>tion).</sup> Given that data item $d \in O _ { v } , d \notin I ^ { e } .$ , and $d \in I _ { u } ,$ $i . e . , v \Rightarrow u ,$ and  such that $v \in \Gamma , u \in \Gamma ,$ and activity u precedes activity v, a missing data anomaly occurs.

Discussion. <sub>Given that</sub> $d \in O _ { v } , d \notin I ^ { e } ,$ , and $d \in I _ { u } ,$ d is produced as an output by v and used as an input by u. Because u precedes $v ,$ d has not been initialized by v when u uses d as an input. Therefore, a missing data anomaly occurs due to delayed initialization.

Lemma 3 (Condition for Uncertain Availabil-<sup>ity).</sup> Given that data item $d \in O _ { v } , d \notin I ^ { e } .$ , and $d \in I _ { u } , i . e . ,$ $v \Rightarrow u ,$ and  such that the precedence of activity v and activity u cannot be determined until  is enacted at run time, missing data anomalies can occur.

Discussion. <sub>Given</sub> $d \in O _ { v } , d \notin I ^ { e } ,$ , and $d \in I _ { u } ,$ d is produced as an output by v and used as an input by u. Because the precedence of activity v and activity u cannot be determined until run time, it is possible that when u uses d as an input, d has not been initialized by v. Therefore, a missing data anomaly occurs due to uncertain availability.

Lemma 4 (Condition for Improper Routing). <sub>If</sub> there exists two activities x and y such that $C _ { x } ^ { u } \neq C _ { y } ^ { u }$ and we can find a data item d that $d \in O _ { x } , d \notin I ^ { e } .$ , and $\boldsymbol { d } \in I _ { y }$ and a routing constraint $\beta$ that $\beta \in C _ { x } ^ { u }$ but $\beta \notin C _ { y } ^ { u } ,$ , a missing data anomaly occurs.

<sup>Proof.</sup> We prove this lemma by contradiction. Assume that there is no missing data anomaly, meaning that activity x must be executed whenever y is executed in order to pass the input data d from x to y. We call this the coupled execution requirement. However, $\beta \in C _ { x } ^ { u }$ indicates that x is executed only when $\beta$ is satisfied and $\beta \notin C _ { y } ^ { u }$ means that y is executed regardless if $\beta$ is or is not satisfied. Therefore, it is possible that y is executed when x is not. This violates the coupled execution requirement. Thus, a contradiction occurs. Lemma 4 holds. <sup></sup>

Lemma 5 (Finite Instance Sets). <sub>A workflow with</sub> a finite set of activities can only have a finite number of instance sets.

<sup>Discussion.</sup> Given that W is an acyclic workflow with n decision nodes, and at each decision node there exists a maximum of m possible routing branches, then there exists a maximum of $m ^ { n }$ instance activity sets. When W contains cycles, we only need to consider the instance that executes the cycle once, since the instance activity set is the same no matter how many times the cycle is executed. Hence, Lemma 5 is correct.

Theorem 1 (Missing Data Verification). <sub>A work-</sub> flow W is free from missing data anomalies if the following conditions are satisfied: (1) <sub>∀</sub> d if $\begin{array} { r } { d \in ( \bigcup _ { i = 1 } ^ { n } I _ { i } ) \cup O _ { 0 } , } \end{array}$ , then $d \in I ^ { e } \cup ( \bigcup _ { i = 1 } ^ { n } O _ { i } ) ; ( 2 )$ given activity dependency $u \Rightarrow v ,$ $\forall \Gamma _ { w } \ i f \ v \in \Gamma _ { w } ,$ , then $u \in \Gamma _ { w }$ and u precedes v at least once under the routing constraint set $C \ o f \Gamma _ { w } .$

<sup>Proof.</sup> Let Lemmas 1, 2, 3, and 4 be the only conditions under which missing data anomalies can occur. We use enumeration to prove that a workflow W will avoid these four situations if it satisfies the following two conditions: (1) d if $\begin{array} { r } { d \in ( \bigcup _ { i = 1 } ^ { n } I _ { i } ) \cup O _ { 0 } , } \end{array}$ then $d \in I ^ { e } \cup ( \bigcup _ { i = 1 } ^ { n } O _ { i } )$ , and (2) given activity dependency $u \Rightarrow v , \forall \Gamma _ { w } \mathrm { i f } v \in \Gamma _ { w } ,$ then $u \in \Gamma _ { w }$ and u precedes v at least once under the routing constraint set C of $\Gamma _ { w } .$

(1) When $d \in I ^ { e } \cup ( \bigcup _ { i = 1 } ^ { n } O _ { i } )$ holds for every d that satisfies $\begin{array} { r } { d \in ( \bigcup _ { i = 1 } ^ { n } I _ { i } ) \cup O _ { 0 } , } \end{array}$ , every input data item required by each activity and every final output data item from W are either provided by the external data input set $I ^ { e } ( { \mathrm { i . e . , ~ } } d \in I ^ { e } )$ or are produced by certain activities in $W \ ( { \mathrm { i . e . , ~ } } d \in \bigcup _ { i = 1 } ^ { n } O _ { i } )$ . Therefore, W is free from absence of initialization according to Lemma 1.

(2) We prove that W is free from delayed initialization and uncertain availability through contradiction. Suppose that there exists delayed initialization or uncertain availability when the set of routing constrains C is satisfied. Because a missing data anomaly occurs under C, we can find two activities, v and $u ,$ in $\Gamma _ { w } ,$ such that v depends on activity u for some data set $D , { \mathrm { ~ i . e . , ~ } } u \Rightarrow v ,$ , and the precedence of u and v can be either v precedes u (Lemma 2) or the precedence cannot be determined until run time (Lemma 3). In either case, u does not precede v. This contradicts the hypothesis. Hence, when C is satisfied, there exists no delayed initialization or uncertain availability. By Lemma 5, there are a finite number of instance activity sets in W . For each instance activity set $\Gamma _ { w } ,$ if there exists an activity dependency between two activities v and $u ,$ u precedes v. Therefore, we conclude W is free from delayed initialization or uncertain availability under all the routing conditions.

(3) Given the activity dependency $u \Rightarrow v , \forall \Gamma _ { w }$ if $v \in \Gamma _ { w } ,$ , then $u \in \Gamma _ { w }$ and u precedes v at least once under the routing constraint set C of $\Gamma _ { w } .$ . Hence, we cannot find a set of routing constraints under which v is executed whereas u is not when u and v have dependency $u \Rightarrow v$ . Therefore, W is free from improper routing (Lemma 4). Hence, Theorem 1 holds. <sup></sup>

Lemmas 1 to 4 provide mathematical descriptions for the conditions under which the four scenarios, absence of initialization, delayed initialization, uncertain availability, and improper routing, may cause missing data anomalies. Lemma 5 proves that a workflow can only have a finite number of instance sets; therefore, it is possible to examine every instance set in a workflow model. According to Theorem 1, in order for a workflow model to be free of missing data anomalies, the following two conditions must hold for every workflow instance: First, every data item used as input data by an activity or required as the final output data from the workflow needs to be initialized. Second, if activity u produces a data item that is used as input by another activity v, then when v is executed for the first time u must already be executed to guarantee the data item needed by v has been produced.

Lemma 6 (Condition for Inevitable Redun-<sup>dancy).</sup> If the following inequality holds, $( ( \cup _ { i = 1 } ^ { n } O _ { i } ) \cup I ^ { e } ) \backslash$ $( ( \cup _ { i = 1 } ^ { n } I _ { i } ) \cup O _ { 0 } ) \neq \emptyset$ , redundant data anomalies occur in at least one instance of the workflow W .

Discussion. <sub>Given</sub> $( ( \bigcup _ { i = 1 } ^ { n } O _ { i } ) \cup I ^ { e } ) \backslash ( ( \bigcup _ { i = 1 } ^ { n } I _ { i } ) \cup O _ { 0 } ) \neq$ , there exists at least one data item d such that d is either from some external resources or produced as output by some activities in $W ,$ but $d$ is not needed as input by any activities or required as final output in at least one instance . Therefore, d is a redundant data item in .

Lemma 7 (Condition for Contingent Redundancy). <sub>Given</sub> $( ( \bigcup _ { i = 1 } ^ { n } O _ { i } ) \cup I ^ { e } ) \backslash ( ( \bigcup _ { i = 1 } ^ { n } I _ { i } ) \cup O _ { 0 } ) = \emptyset$ , and that satisfies $( ( \bigcup _ { i = 1 } ^ { n } O _ { i } ) \cup I ^ { e } ) \backslash ( ( \bigcup _ { i = 1 } ^ { n } I _ { i } ) \cup O _ { 0 } ) \neq \emptyset ,$ a redundant data anomaly occurs in the workflow W .

Discussion. <sub>Given</sub> $( ( \bigcup _ { i = 1 } ^ { n } O _ { i } ) \cup I ^ { e } ) \backslash ( ( \bigcup _ { i = 1 } ^ { n } I _ { i } ) \cup O _ { 0 } ) \neq$ <sub></sub> in instance set , we know by Lemma 6 there exists at least one redundant data item d for the workflow instance corresponding to .

Theorem 2 (Redundant Data Verification). A workflow W is free from redundant data anomalies if <sub>∀</sub>  : $( ( \bigcup _ { i = 1 } ^ { n } O _ { i } ) \cup I ^ { e } ) \backslash ( ( \bigcup _ { i = 1 } ^ { n } I _ { i } ) \cup O _ { 0 } ) = \emptyset$

<sup>Proof.</sup> Because $( ( \bigcup _ { i = 1 } ^ { n } O _ { i } ) \cup I ^ { e } ) \backslash ( ( \bigcup _ { i = 1 } ^ { n } I _ { i } ) \cup O _ { 0 } ) =$ $\scriptstyle { \mathcal { O } } ,$ , in each instance every output data item is used as input or required as the final output. Therefore, by Lemma $6 ,$ there is no inevitable redundancy and by Lemma 7 there is no contingent redundancy. <sup></sup>

Lemmas 6 and 7 describe the conditions under which redundant data anomalies can occur because of the two scenarios: inevitable redundancy and contingent redundancy. According to Theorem 2, a workflow is free from redundant data anomalies if, for every instance, all the output data items are consumed by other activities or taken as the final output of the workflow.

Lemma 8 (Condition for Multiple Initializa-<sup>tions).</sup> Given two different activities x and y, if $O _ { x } \cap O _ { y } \neq \emptyset$ and $C _ { x } ^ { u } \subseteq C _ { y } ^ { u }$ or $C _ { y } ^ { u } \subseteq C _ { x } ^ { u } .$ , a conflicting data anomaly occurs.

Discussion. <sub>Because</sub> $C _ { x } ^ { u } \subseteq C _ { y } ^ { u } ,$ , x is executed when y is executed. Because $C _ { y } ^ { u } \subseteq C _ { x } ^ { u } , \check { y }$ is executed when x is executed. Therefore, under either $C _ { x } ^ { u } \subseteq C _ { y } ^ { u }$ or $C _ { y } ^ { u } \subseteq C _ { x } ^ { u } .$ it is possible that both x and y are executed. Because of $O _ { x } \cap O _ { y } \neq \emptyset$ , we can assume a data item $d \in ( O _ { x } \cap O _ { y } )$ When both x and y are executed, x and y can initialize d different values. As such, a conflicting data anomaly occurs.

Theorem 3 (Conflicting Data Verification). A workflow W is free from conflicting data anomalies if the following conditions hold: (1) for any two activities x and y $O _ { x } \cap O _ { y } = \emptyset ,$ or (2) given $O _ { x } \cap O _ { y } \neq \emptyset , \forall \Gamma _ { w } \ i f \ x \in \Gamma _ { w } ,$ then $y \notin \dot { \Gamma } _ { w }$

<sup>Proof.</sup> (1) If for any two activities x and $y \ O _ { x } \cap$ $O _ { y } = \mathcal { D } ,$ , then no two activities initialize the same data item. Therefore, W is free from conflicting data anomalies. (2) Given $O _ { x } \cap O _ { y } \neq \emptyset$ , x and y initialize the same data item. However, x and y are executed in different $\Gamma _ { w }$ since $\forall \Gamma _ { w } \mathrm { ~ i f ~ } x \in \Gamma _ { w } ,$ then $y \notin \Gamma _ { w } .$ By Lemma $^ { 8 , }$ we know the workflow is free from conflicting data anomalies. <sup></sup>

Lemma 8 and Theorem 3 specify that in a workflow instance each data item can only be initialized by one activity to avoid conflicting data anomalies. In summary, the three theorems above have established the correctness criteria for a data-flow model. A workflow model with correct data-flow specification should satisfy all these criteria, which can be summarized as (1) any input data item should be initialized before it is used, (2) any output data item should be either used as input for some other activity or required as final output, and (3) no two activities that produce the same data item can be executed in the same workflow instance.

## 6.3. Data-Flow Verification Algorithms

In this section, we present the data-flow verification algorithms that are based on the theorems we have proven in §6.2. The verification algorithms consist of three procedures as shown in Figure 3, which can be used as a road map for implementing a data-flow verification component in a workflow system.

The procedure Checking\_Missing\_Data, based on Theorem 1, first finds the unconditional and conditional requisite sets for each activity v in each instance of a workflow W . If the requisite sets cannot provide all the required data input for v at the time v is performed, or if some activities in the requisite sets are not included in the instance, then missing data is detected. The procedure Checking\_Redundant\_Data, based on Theorem 2, examines each instance set of a workflow. If in an instance some data items are produced, but they are not used as input of other activities or needed as final output, then redundant data are detected. The procedure Checking\_Conflicting\_Data, based on Theorem $^ { 3 , }$ examines each instance for activities that initialize the same data. If such a situation is discovered, then conflicting data are detected.

Next, we give a high-level analysis of computational complexity. First, we examine the procedure Checking\_Missing\_Data. When a workflow has n activities and each activity uses $( n + a )$ data items as input, it takes $n ( n + a )$ steps to find all the unconditional requisite sets for each activity in the workflow. If the workflow has $( n + b )$ instances, it takes $n ( n + a ) ( n + b ) , \mathrm { i . e . , ~ } ( n ^ { 3 } + ( a + b ) n ^ { 2 } + a b n )$ , steps to find the conditional requisite set for each activity and to check whether the activities in the requisite sets of each activity v are executed before v in each instance. Assuming a and b can both be positive or negative and have a small absolute value relative to $n ,$ the complexity of the procedure Checking\_Missing\_ Data is proportional to $\left[ n ( n + a ) + ( n ^ { 3 } + a + b ) n ^ { 2 } + \right.$ abn , which is equivalent to $( n ^ { 3 } + ( a + b + 1 ) n ^ { 2 } +$ $a ( b \ + \ 1 ) n )$ , or approximately $\mathrm { O } ( n ^ { 3 } )$ . In the procedures of Checking\_Redundant\_Data and Checking\_Conflicting\_Data, the number of iterations is determined by the number of instances and the number of activities. Moreover, in the procedure Checking\_Redundant\_Data, the number of iterations is decided by the number of input data items that each activity requires, as opposed to being decided by the number of output data items, as in the procedure Checking\_Conflicting\_Data. Therefore, the complexity for both procedures is approximately $\mathrm { O } ( n ^ { 3 } )$ , similar to that of the procedure of Checking\_Missing\_Data.

## 6.4. Validation of the Data-Flow Verification Framework

In §5, we presented seven examples in which different data-flow anomalies occur for different reasons. Next, we explain how the data-flow verification theorems can help detect the data-flow anomalies in the seven examples.

Detection of Missing Data in Example 1. As shown in Table 2, no activity initializes data item $d _ { 1 8 } ,$ property insured, but activity $v _ { 1 4 }$ reads $d _ { 1 8 }$ as input, i.e., $d _ { 1 8 } \in$ $\textstyle \bigcup _ { i = 1 } ^ { 1 8 } I _ { i }$ and $d _ { 1 8 } \notin I ^ { e } \cup ( \bigcup _ { i = 1 } ^ { 1 8 } O _ { i } )$ , which violates Theorem 1. Therefore, a missing data anomaly is detected.

Detection of Missing Data in Example 2. From Table $^ { 7 , }$ we know that there is an activity dependency $v _ { 1 3 } \Rightarrow v _ { 9 }$ In the instance set $\Gamma _ { 2 } = \{ s , v _ { 1 } , v _ { 2 } , v _ { 3 } , v _ { 5 } , v _ { 6 } , v _ { 7 } , v _ { 8 } ,$ $v _ { 9 } , v _ { 1 0 } , v _ { 1 1 } , v _ { 1 2 } , v _ { 1 3 } , v _ { 1 4 } , v _ { 1 5 } , e \}$ shown in Table $6 , \ v _ { 9 }$ precedes $v _ { 1 3 }$ (Figure 1). Therefore, according to Theorem 1, a missing data anomaly is detected.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Figure 3 Data-Flow Verification Algorithm

Procedure Checking_Missing_Data (W, M, I$^{e}$) {
    Δ$^{u}$ = ∅
    Γ$_{w}$ = findAllInstanceSets(W)
    for i = 1 to n {/* check every activity in a workflow */
    I$_{vi}$ = findUnconditionalInput(M, v$_{i}$)
    /* find the unconditional data input of activity v$_{i}$ from data-flow matrix */
    for each d ∈ I$_{vi}$ and d∉I$^{e}$ {
    V$_{temp}$ = findReqActivity(d)    /* find the activity that sets the initial value of d */
    if (V$_{temp}$ = null)    /* check whether any activity initialize d */
    print “Miss data occurs for activity v$_{i}$”
    /* if d is not initialized, missing data occurs due to absence of initialization */
    /* Violation of the first condition of Theorem 1 */
    else add v$_{temp}$ to Δ$^{u}$    /* find unconditional requisite set for activity v$_{i}$ */}
    for each Γ ∈ Γ$_{w}$ {
    if (v$_{i}$ ∈ Γ) {
    for each v$_{j}$ ∈ Δ$^{u}$ {
    if (v$_{j}$∉Γ or v$_{j}$ is Executed After v$_{i}$ or v$_{j}$ is Parallel With v$_{j}$)
    print “Missing data occurs for v$_{i}$ in Γ”
    /* Violation of the second condition of Theorem 1 */}
    C = findRoutingConstraintSet(W, Γ)    /* find the routing constraint set for Γ */
    I$_{vi}$ = findConditionalInput(M, v$_{i}$, C)    /* find conditional input for v$_{i}$ under C */
    for d ∈ I$_{vi}$ and d∉I$^{e}$ {
    v$_{temp}$ = findReqActivity(d)    /* find the activity that sets the initial value of d */
    if (v$_{temp}$ = null or v$_{temp}$∉Γ or v$_{temp}$ is Executed After v$_{i}$ or v$_{temp}$ is Parallel With v$_{i}$)
    print “Missing data occurs for v$_{i}$ in Γ”
    /* Violation of the second condition of Theorem 1 */}}}}}

Procedure Checking_Redundant_Data(W, M, I$^{e}$, O$_{0}$) {
    Γ$_{w}$ = findAllInstanceSets(W)
    for each Γ ∈ Γ$_{w}$ {/* check each instance set */
    for each v ∈ Γ {D = findOutputData(v, M)    /* find all the output of v */
    add D to I$^{e}$    /* find all the output produced in Γ */}
    for each d ∈ O$_{0}$ if (d ∈ I$^{e}$) remove d from I$^{e}$    /* check if d is required as final output in Γ */
    for each v ∈ Γ {D = findInputData(v, M)    /* find all the input of v */
    for each d ∈ D    /* check if d is used as input by some activities in Γ */
    if (d ∈ I$^{e}$) remove d from I$^{e}$}
    if (I$^{e}$ ≠∅) print “Redundant data occurs for in Γ”    /* Violation of Theorem 2 */}}
Procedure Checking_Conflicting_Data(W, M, O$_{0}$) {
    V$_{temp}$ = ∅
    Γ$_{w}$ = findAllInstanceSets(W)
    for i = 1 to n {/* check every activity in a workflow */
    I$_{vi}$ = findAllOutput(M, v$_{i}$)
    for each d ∈ I$_{vi}$ if (d∉O$_{0}$) add d to O$_{0}$    /* find all output data */}
    for each Γ ∈ Γ$_{w}$
    for each d ∈ O$_{0}$
    V$_{temp}$ = findInitializingActivity(d, Γ)    /* find all the activities that initialize d in Γ */
    if (NumberOfElement(V$_{temp}$) &gt; 1) print “Conflicting data occurs for in Γ”    /* Violation of Theorem 3 */}}
    }
</div>

and $v _ { 1 0 }$ are indeterministic at design time (Figure 1). Therefore, a violation of Theorem 1 is detected.

Detection of Missing Data in Example 3. From Table $^ { 7 , }$ we know that there is an activity dependency $v _ { 1 0 } \Rightarrow v _ { 9 }$ . In both instance sets $\Gamma _ { 2 } = \{ s , v _ { 1 } , v _ { 2 } , v _ { 3 } , v _ { 5 } , v _ { 6 } ,$ $v _ { 7 } , v _ { 8 } , v _ { 9 } , v _ { 1 0 } , v _ { 1 1 } , v _ { 1 2 } , v _ { 1 3 } , v _ { 1 4 } , v _ { 1 5 } , e \}$ and $\Gamma _ { 3 } = \{ s , v _ { 1 } ,$ $v _ { 2 } , v _ { 3 } , v _ { 5 } , v _ { 6 } , v _ { 7 } , v _ { 8 } , v _ { 9 } , v _ { 1 0 } , v _ { 1 1 } , v _ { 1 2 } , v _ { 1 5 } , v _ { 1 6 } , v _ { 1 7 } , v _ { 1 8 } , e \}$ shown in Table $^ { 8 , }$ the execution order between $v _ { 9 }$

Detection of Missing Data in Example 4. From Table $^ { 7 , }$ we know that there is an activity dependency $v _ { 1 4 } \Rightarrow v _ { 1 5 }$ . In the instance set $\Gamma _ { 3 } = \{ s , v _ { 1 } , v _ { 2 } , v _ { 3 } , v _ { 5 } ,$ $v _ { 6 } , v _ { 7 } , v _ { 8 } , v _ { 9 } , v _ { 1 0 } , v _ { 1 1 } , v _ { 1 2 } , v _ { 1 5 } , v _ { 1 6 } , v _ { 1 7 } , v _ { 1 8 } , e \}$ shown in Table 8, $v _ { 1 5 }$ is executed and $v _ { 1 4 }$ is not, leading to a violation of Theorem 1.

Detection of Redundant Data in Example 5. As Table 2 shows, data item $d _ { 1 3 } ,$ current owner of property, produced by activity $v _ { 1 0 } ,$ request appraisal info, is not used by any other activities, i.e., $d _ { 1 3 } \in ( \bigcup _ { i = 1 } ^ { 1 8 } O _ { i } \cup I ^ { e } )$ and $d _ { 1 3 } \not \in ( \bigcup _ { i = 1 } ^ { 1 8 } I _ { i } \cup O _ { 0 } )$ . Therefore, $( ( \bigcup _ { i = 1 } ^ { 1 8 } O _ { i } ) \cup I ^ { e } ) \backslash ( ( \bigcup _ { i = 1 } ^ { 1 8 } I _ { i } ) \cup O _ { 0 } ) \neq \emptyset$ , leading to a violation of Theorem 2. As such, a redundant data anomaly is detected.

Detection of Redundant Data in Example 6. Data item $d _ { 5 } ,$ application summary, is produced by $v _ { 1 } ,$ receive application, and only required by activity $v _ { 1 8 } ,$ forward to manager for signature. Therefore, for the instance sets $\Gamma _ { 1 } = \{ s , v _ { 1 } , v _ { 2 } , v _ { 3 } , v _ { 5 } , v _ { 6 } , v _ { 7 } , v _ { 8 } , e \}$ and $\Gamma _ { 2 } =$ $\{ s , v _ { 1 } , v _ { 2 } , v _ { 3 } , v _ { 5 } , v _ { 6 } , v _ { 7 } , v _ { 8 } , v _ { 9 } , v _ { 1 0 } , v _ { 1 1 } , v _ { 1 2 } , v _ { 1 3 } , v _ { 1 4 } , v _ { 1 5 } ,$ e in Table 8, $( ( \bigcup _ { i = 1 } ^ { 1 8 } { \cal O } _ { i } ) \cup I ^ { e } ) \backslash ( ( \bigcup _ { i = 1 } ^ { 1 8 } I _ { i } ) \cup { \cal O } _ { 0 } ) = \emptyset$ does not hold since $d _ { 5 } \in ( ( \cup _ { i = 1 } ^ { 1 8 } O _ { i } ) \cup I ^ { e } )$ and $d _ { 5 } \not \in ( ( \cup _ { i = 1 } ^ { 1 8 } I _ { i } ) \cup O _ { 0 } )$ Hence, there is a violation of Theorem 2.

Detection of Conflicting Data in Example 7. From Table 2 we know $d _ { 1 0 } \in O _ { 5 } , \ d _ { 1 0 } \in O _ { 6 } ,$ and $d _ { 1 0 } \in O _ { 7 }$ where $O _ { 5 } , O _ { 6 } ,$ and $O _ { 7 }$ are the output data from $v _ { 5 } , v _ { 6 } ,$ and $v _ { 7 } ,$ respectively. For all the three instance sets in Table 8, i.e., $\Gamma _ { 1 } = \{ s , v _ { 1 } , v _ { 2 } , v _ { 3 } , v _ { 5 } , v _ { 6 } , v _ { 7 } , v _ { 8 } , e \} , \ \Gamma _ { 2 } =$ $\{ s , v _ { 1 } , v _ { 2 } , v _ { 3 } , v _ { 5 } , v _ { 6 } , v _ { 7 } , v _ { 8 } , v _ { 9 } , v _ { 1 0 } , v _ { 1 1 } , v _ { 1 2 } , v _ { 1 3 } , v _ { 1 4 } , v _ { 1 5 } ,$ e, and $\Gamma _ { 3 } = \{ s , v _ { 1 } , v _ { 2 } , v _ { 3 } , v _ { 5 } , v _ { 6 } , v _ { 7 } , v _ { 8 } , v _ { 9 } , v _ { 1 0 } , v _ { 1 1 } , v _ { 1 2 } ,$ $v _ { 1 5 } , v _ { 1 6 } , v _ { 1 7 } , v _ { 1 8 } , e \} , \ O _ { 5 } \cap O _ { 6 } \not = \emptyset , \ O _ { 5 } \cap O _ { 7 } \not = \emptyset .$ , and $O _ { 6 } \cap O _ { 7 } \neq \emptyset$ . Therefore, there is a violation of Theorem 3.

## 7. Conclusions

Data-flow specification and analysis constitute the data-flow perspective in business process management. However, the existing literature and commercial workflow systems do not provide analytical tools for discovering the data-flow errors in a workflow model due to the lack of formalisms for dataflow analysis. In this paper, we formulate the dataflow perspective by means of dependency analysis. First, we propose the data-flow matrix and process data diagram to specify the data flow in a business process. A data-flow matrix is a two-dimensional table that shows the operation each activity performs on each data item. With a data-flow matrix, it is easy to identify how each data item is processed in a workflow. A process data diagram extends the UML activity diagram by specifying the input and output data for each activity.

Second, we propose a formal approach to data-flow analysis for discovering data-flow anomalies based on dependency analysis. The data-flow analysis framework we have developed includes lemmas specifying the conditions necessary for different data-flow anomalies to occur and theorems describing the sufficient conditions for a workflow to be free from these data-flow anomalies. Based on the verification rules, we have developed algorithms that can be used as a road map for the implementation of the data-flow perspective. To the best of our knowledge, this research is the first attempt to formally establish the correctness criteria for data-flow analysis in workflow management. We believe our approach will help to significantly improve the state of the art in workflow analysis by eliminating data-flow anomalies systematically.

In this paper, we have limited our attention to the five basic workflow patterns, namely sequence, AND-Split, AND-Join, XOR-Split, and XOR-Join. More advanced workflow patterns (van der Aalst et al. 2003) such as an OR vertex (either Split or Join) can be simulated by a combination of AND and XOR vertices (Bi and Zhao 2004). Therefore, the correctness of data flow where an OR vertex is involved can be determined by analyzing the equivalent constructs consisting of AND and XOR vertices. Due to space limitations, we will deal with the issue of advanced workflow patterns more extensively in a separate paper.

We are currently continuing our work in a number of directions. First, we plan to develop a prototype data-flow manager so that our research results can be tested in real-world applications. Second, we will develop a formal methodology for correcting dataflow anomalies. To correct data-flow anomalies, we need to modify not only the data flow, but also, in some cases, the control flow. Third, we are extending our work toward a new workflow design methodology based on data-flow analysis (Sun and Zhao 2004).

## Acknowledgments

The authors of this paper would like to thank the anonymous referees for their detailed and constructive comments that have helped improve the quality of this paper significantly. The second author also thanks IBM for its support through the 2005 IBM Faculty Award.

## References

Bajaj, A., S. Ram. 2002. Seam: A state-entity-activity-model for a well-defined workflow development methodology. IEEE Trans. Knowledge Data Engrg. 14(2) 415–431.

Basu, A., R. W. Blanning. 1994a. Metagraphs: A tool for modeling decision support systems. Management Sci. 40(12) 1579–1600.

Basu, A., R. W. Blanning. 1994b. Model integration using metagraphs. Inform. Systems Res. 5(3) 195–218.

Basu, A., R. W. Blanning. 2000. A formal approach to workflow analysis. Inform. Systems Res. 11(1) 17–36.

Basu, A., A. Kumar. 2002. Workflow management issues in e-business. Inform. Systems Res. 13(1) 1–14.

Berg, H. K., W. E. Boebert, W. R. Franta, T. G. Moher. 1982. Formal Methods of Program Verification and Specifcation. Prentice Hall, Englewood Cliffs, NJ.

Bi, H. H., J. L. Zhao. 2003. A formal classification of process anomalies for workflow verification. 13th Workshop Inform. Tech. Systems (Dec. 13–14).

Bi, H. H., J. L. Zhao. 2004. Applying propositional logic to workflow verification. Inform. Tech. Management 5(3–4) 293–318.

Curtis, B., M. I. Kellner, J. Over. 1992. Process modeling. CACM 35(9) 75–90.

Davenport, T. H. 1993. Process Innovation. Harvard Business School Press, Cambridge, MA.

Earl, M. J., J. L. Sampler, J. E. Short. 1995. Strategies for business process reengineering: Evidence from field studies. J. Management Inform. Systems 12(1) 31–56.

Georgakopoulos, D., M. Hornick, A. Sheth. 1995. An overview of workflow management: From process modeling to workflow automation infrastructure. Distributed and Parallel Database 3 119–153.

Guaspari, D., C. Marceau, W. Polak. 1990. Formal verification of Ada programs. IEEE Trans. Software Engrg. 16(9) 1058–1075.

Kappel, G., P. Lang, S. Rausch-Schott, W. Retschitzegger. 1995. Workflow management based on objects, rules, and roles. IEEE Data Engrg. Bull. 18(1) 11–18.

Krauskopf, R., F. Rash. 1990. Independent verification and validation. IEEE Potentials 9(2) 12–14.

Kumar, A., J. L. Zhao. 1999. Dynamic routing and operational control in workflow management systems. Management Sci. 35(2) 253–272.

Kumar, A., J. L. Zhao. 2002. Workflow support for electronic commerce applications. Decision Support System 32 265–278.

Kwan, M. M., P. R. Balasubramanian. 1997. Dynamic workflow management: A framework for modeling workflows. Proc.

HICSS 1997, Vol. 4. IEEE Computer Society Press, 367–376.

Lee, H. B., J. W. Kim, S. J. Park. 1999. KWM: Knowledge-based workflow model for agile organization. J. Intelligent Inform. Systems 13 261–278.

Mili, A. 1985. An Introduction to Formal Program Verification. Van Nostrand Reinhold Company, New York.

Reuter, A., F. Schwenkreis. 1995. Contracts: A low level mechanism for building general purpose workflow management systems. IEEE Data Engrg. Bull. 18(1) 41–47.

Sadiq, S., M. Orlowska, W. Sadiq, C. Foulger. 2004. Data flow and validation in workflow modeling. Proc. 15th Australasian Database Conf. (Jan. 18–22) 207–214.

Sarnikar, S., J. L. Zhao, A. Kumar. 2004. Organizational knowledge distribution: An experimental evaluation. Proc. AMCIS 2004 (Aug. 5–8) 2305–2314.

Smith, H., P. Fingar. 2003. IT doesn’t matter? Business processes do. Meghan-Kiffer Press, Tampa, FL.

Stohr, E. A., J. L. Zhao. 2001. Workflow automation: Overview and research issues. Inform. Systems Frontiers 3(3) 281–296.

Sun, S. X., J. L. Zhao. 2004. A data flow approach to workflow design. Proc. WITS 2004 (Dec. 11–12) 80–85.

Sun, S. X., J. L. Zhao, O. R. Sheng. 2004. Data flow modeling and verification in business process management. Proc. AMCIS 2004 (Aug. 6–8) 4064–4073.

van der Aalst, W. M. P. 1998. The application of Petri nets to workflow management. J. Circuits Systems Comput. 8(1) 21–66.

van der Aalst, W. M. P., A. ter Hofstede. 2000. Verification of workflow task structures: A Petri-net-based approach. Inform. Systems 25(1) 43–69.

van der Aalst, W. M. P., A. H. M. ter Hofsted, B. Kiepuszewski, A. P. Barros. 2003. Workflow patterns: Distributed and parallel databases. 14(1) 5–51.

Wallace, D. R., R. U. Fujii. 1989. Software verification and validation: An overview. IEEE Software 6(3) 10–17.

Wirtz, G., M. Weske, H. Giese. 2001. The OCoN approach to workflow modeling in object-oriented systems. Inform. Systems Fron tiers 3(3) 357–376.

Yourdon, E., L. L. Constantine. 1979. Structured Design. Prentice Hall, Englewood Cliffs, NJ.

Zhao, J. L., H. H. Bi. 2003. On the completeness of logic-based workflow verification. 13th Workshop Inform. Tech. Systems (Dec. 13–14).
