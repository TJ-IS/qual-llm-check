---
otero_id: 18007
otero_key: "8WM5338W"
title: "Computer-aided modeling and analysis techniques for determining business information systems requirements"
authors: "Kweku Ewusi-Mensah"
year: "1982"
journal: "Information & Management"
doi: "10.1016/0378-7206(82)90030-1"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Computer-Aided Modeling and Analysis Techniques for Determining Business Information Systems Requirements \*

Kweku Ewusi-Mensah

Department of Decision Sciences, University of Hawaii Honolulu.
III 06822, USA

The paper deals with the problem of determining the information requirements or needs of a business organization. Characteristics of the problem are discussed and several forms of models based on concepts in elementary matrix algebra and graph theory are described. We construct boolean matrices representing either data usage or creation by a process or function in a business organization. Products of the two matrices are represented as directed graphs to depict the flow of information. Two procedures are described for realizing the solutions obtained from the analysis. The applicability to other related areas of information systems research is discussed and an example is presented.

Keywords: Information Systems, Requirements Analysis, Matrices, Processes, Data Classes, Information Flows.

## 1. Introduction

The proliferation of automated information processing systems in business organizations has seriously suffered from lack of careful analysis of the information needs or management requirements. As Miller [12] succinctly states, “The problem of developing and defining the proper content of an information system has been slighted in the general work of systems analysis and design.” This lack of attention to information systems specification has undoubtedly resulted in the failure of most of the information systems [1,10]. However, some attempts are currently in progress to correct this serious defect [see 2, 3, 5, 6, 13, 14, 16–18].

Some of the problems can be attributed to insufficient research into the 'infological problem' in information systems [10]. This is a problem of determining what information is needed to satisfy the users. Langefors rightly states 'an information system is well designed only if it provides the right information in kind, quality and time when it is needed. The essence of the problem, then, is to develop a methodology which will provide information systems analysts and designers with conceptual models that describe (in sufficient detail) the information needs and problems of the business organization.

![](/api/attachments/8WM5338W/fulltext/images/b000bb1c939af23648d239952f06da16808e442611ad5b5553368f62e733f0ef.jpg)

One such methodology is IBM's Business Systems Planning (BSP). BSP is a procedure for analyzing the information requirements of an organization and developing an information systems architecture to meet those needs. In the BSP approach, both top-down and bottom-up techniques are used [4]. The top-down approach is characterized by its focus on decisions at the managerial level of the organization [12], by analyzing the objectives of the business and the various processes or functions established to achieve those objectives. Then the decisions necessary to manage those functions or processes are identified, together with the necessary information required to support them. The required information is in turn dependent on certain classes or types of data.

The bottom-up approach is characterized by its focus on data at the operational level of the organization [13]. The information requirements are determined by examining all the data classes which management currently uses for decision-making. Finally, an information systems plan is proposed from the results of the analysis.

In this paper, we develop some computer-assisted techniques using boolean matrices and graph theoretical concepts to aid in the information requirements analysis for BSP. We hope to enhance both the consistency and reliability of the results of the study team's analysis.

## 2. Characteristics of the Requirements Analysis

Our approach is motivated by the need to find a requirements model which lends itself to theoretical analysis. With this in mind, we reconstruct BSP's matrices into boolean matrices which describe the relationships among various data classes occurring in a business organization and the operations or processes to achieve the goals. In the management of information, the information analyst's major concern is how to structure the data required by the organization [15]. The matrix model assumes a form in which individual data classes appear as one dimension (e.g. rows) and business operations or processes as the other (e.g. columns) [4]. The entries indicate either data usage or creation (denoted by '1') of a data class by a business operation or process and non-usage or non-creation of a data class by a business operation (denoted by '0').

The important considerations behind this approach can be briefly characterized as follows:

1) The approach must provide a means for the users of the information system to express their requirements in their terms, based on their environment (both internal and external).

2) The methodology must express the requirements of the information systems in terms meaningful to the information systems designers.

3) The results of the data collection and analysis must be stated in terms of those invariant properties of the organization. This allows the development of stable systems which can meet the changing information requirements as its operating conditions change.

## 3. Desirable Attributes

Desirable attributes of the modeling techniques include:

1) Analytical Capabilities. The modeling techniques must allow comprehensive analysis of the data gathered. The model must be able to cope with the complexity of the problem and the large volume of data. This feature will also allow analysts to gain insights into the problems which might escape them in a manual analysis.

2) Flexibility, Stability and Reliability. The models must be stable, reliable, easy to maintain, and flexible. By flexibility, we mean the ability of the models to respond to changing conditions imposed upon them by the environment (without impacting their stability). Stability is the capacity of the models to remain in equilibrium. These two are interrelated. A model may be stable because it is flexible enough to meet the changing demands and thus preserve its equilibrium. Reliability describes the accuracy and consistency of the results obtained from the analysis. Stable and reliable models will enhance the credibility of the analysis and minimize dependence on the imagination of the analysts involved in the study.

3) Interactive Features. The modeling system must be easy to operate in an interactive mode (to accommodate multiple analysts). This capability will encourage the analysts to help in improving the system [15]. The feature will also permit modifications to be carried out and to encourage sensitivity analysis under different environmental constraints.

4) Inquiry Capabilities. This will enable the analysts to interact effectively with the system. The analyst may selectively use the information stored in the computer to answer queries related to the information needs. In this vein, procedures can be developed to locate any additional information which may be needed.

These are the four attributes we consider most desirable for the modeling system.

## 4. The Matrix Model

The primary advantage of the matrix form of documentation and analysis is that it permits the analyst to describe the nature of the relationship between the object types (e.g. data and process) and to make inferences about the various relationships associated with the object types [8,10]. We describe in Appendix A the details of the model.

Our objective in the analysis is to construct the flow of information (e.g. data and process) through a business organization by establishing a link between the data vs. data (i.e. $A_{u}A_{c}^{\mathrm{T}}$ or $\alpha_{/k}^{\prime}$ ) matrix and the process vs. process (i.e. $A_{c}^{\mathrm{T}}A_{u}$ or $\alpha_{/k}$ ) matrix. For visual impact, we use a flowchart to represent the structure of the information flow as a directed graph. The flow progresses from left to right.

From the data vs. data matrix $(\alpha_{ik}^{\prime})$ we obtain the following representation (Fig. 1) which corresponds to Table A4, with the circles and boxes representing data and process respectively. And from the process vs. process ( $\alpha_{/k}$ ) matrix we get the picture of Fig. 2, which corresponds to Table A3. Using the results of the analysis illustrated by Figs. 1 and 2, we can construct the flow of information (i.e., data and process) for the entire organization as shown in Fig. 3.

![](/api/attachments/8WM5338W/fulltext/images/727f8e6620b682a877a016d9dcc305ab780ab57b62db8bb827c0d5138b3a11fa.jpg)  
Fig. 1. Data vs. Data Flow.

![](/api/attachments/8WM5338W/fulltext/images/208c9103bd719ebe9f8c239c2fc0fd2e636209811da7459d8406d618fee9215f.jpg)  
Fig. 2. Process vs. Process Flow Path.

![](/api/attachments/8WM5338W/fulltext/images/b10a192aae1420072a8a09cce78012de8b9623f6040130f654d1a2e12f619841.jpg)  
Fig. 3. Information Flow Path.

In Appendix B we describe an algorithm which enables us to construct the information flow illustrated in Fig. 3, using the information contained in Figs. 1 and 2.

## 5. Data/Process Flow Analysis: An Example

We now illustrate, with examples from sample data, the analysis using these procedures. The type of information (i.e. data-process) flow paths represented by Figs. 1 and 2 are given in Table 1. A sample of the data-process flow paths enumerated as in Fig. 3 is as shown in Table 2.

This type of concise representation makes it possible to store vast amounts of information in a readily usable form. The numbers in the odd-numbered positions (i.e., 1, 3, 5, 7, ...) designate data and those in the even-numbered positions (i.e., 2, 4, 6, ...) represent processes. The first two rows of Table 2 can be read as;

Table 1

<table><tr><td>Data vs. Data Matrix $(\alpha_{tk}^{\prime})$ </td><td>Process vs. Process Matrix $(\alpha_{jk})$ </td></tr><tr><td>1-4-6</td><td>3-2-7</td></tr><tr><td>1-4-7</td><td>3-2-8</td></tr><tr><td>1-4-8</td><td>3-2-4</td></tr><tr><td>1-4-10</td><td>3-2-1</td></tr><tr><td>2-4-6</td><td>3-2-2</td></tr><tr><td>2-9-13</td><td>4-6-12</td></tr><tr><td>3-12-15</td><td>4-10-12</td></tr><tr><td>3-4-7</td><td>4-8-5</td></tr></table>

1. Profit Projections → 4. Financial Reporting → 6. Expenses Actual → 12. Product Cycle Control → 15. Product Tracking and → 17. Product Development Statistics → 33. I/S Service Allocation → 36. Service Actuals.

The information, although sufficient, is regretably inadequate in conveying the degree of interactions among the various data classes and the business processes. In order to overcome this drawback, all the basic information flow paths are presented together in graphical form as an information or data-process tree. This type of representation not only identifies all the major data classes or critical processes, but also presents a better picture of the complexity of the interconnections among the data classes and the processes. Fig. 4 is a tree representation of the information flow paths illustrated in Table 2.

```csv
1-4-6-12-15-33-36
1-4-6-12-17-33-36
1-4-6-5-3-12-15-33-36
1-4-6-5-4-12-15-33-36
1-4-6-5-4-12-15-33-36
1-4-6-5-5-12-15-33-36
1-4-7-12-15-33-36
1-4-7-12-17-33-36
1-4-7-5-3-12-15-33-36
1-4-7-5-4-12-15-33-36
1-4-7-5-5-12-15-33-36
```

![](/api/attachments/8WM5338W/fulltext/images/f3f7a12666217c0432cdeaea3d9c6bdeddf270d772e15c272d13b1d898eecb78.jpg)  
Fig. 4. A Tree Structure Representation of the Information Flow Paths.

## 6. Application to Other Areas

The information requirements modeling and analysis techniques can be applied to other areas of research in studying the information systems of organizations as follows:

1. Current Information Subsystems vs. Business Process Matrix. The information system can first be decomposed into subsystems [see 7]. The construction of such a matrix will show which business processes currently have their information requirements either partially or fully satisfied. The matrix will serve as a basis for identifying any deficiencies in the current information system and thus suggest possible areas of improvements.

2. Current Information Subsystems vs Data Classes Matrix. This matrix shows the nature and degree of interactions between the present information system and the various data classes which serve as either inputs or outputs. The nature of the dependence of the information system on the data classes may also help to uncover some problems such as missing data for some subsystems or unnecessary dependence of a subsystem on other subsystems due to its association with unneeded data.

3. Organization vs Process Matrix. This matrix shows how the processes relate to the various organizational units. The matrix also helps to reveal the responsibilities of the various organizational units with respect to their processes. This is critical if one needs to trace any problems to the organizational units which directly or indirectly affects those processes.

4. Information-Related Problems. In arriving at a design of a comprehensive up-do-date information system which will meet the needs of an organization, it is important to determine the information-related problems (such as, timeliness, tardiness, accuracy, privacy and/or security of any data), associated with the current information system or processes. Once this is accomplished, various interactions such as information problems vs. processes, information problems vs. data classes, information problems vs. organizational units etc. can be determined. For example, the information problems vs. data class matrix shows how the problems associated with any particular data class can be identified. Solutions can then be developed to correct for any deficiencies which may exist in the current information system or the current methods of data collection and/or processing to produce the required information.

## 7. Conclusions

Here we described modeling and analysis techniques to deal with the information requirements problem. It is apparent from the discussions that each of the interactions described serves to inform the analyst about the nature or state of the organization with respect to information, the current information system, the processes and the data classes on which the information requirements ultimately depend. Some redundancies are intentionally incorporated in the analysis as a check - to eliminate any inconsistencies or apparent inaccuracies. The data collected can thus be validated before it is subjected to further analysis.

The ultimate justification for this approach is that it provides a better understanding of the flow of information through an organization. The techniques also serve the purpose of widening the scope and depth of the analysis by the computer in finding solutions to management's information needs and problems. The insight obtained from the analysis, through the use of the computer, may point to the need for more information (e.g., in the case of missing data). The analysis may also help to expose unneeded data. Indeed, the computer can store large amounts of basic information using representations which may prove significant in the long run as the information systems evolves to meet the changing needs of an evolving organization.

## Acknowledgement

I am grateful to Rita Summers and the Editor for helpful comments on an earlier version of this paper and to Fuun Young for the APL programs implementing the procedures. The Advance Technology group in DPMG provided financial support for the work.

## References

[1] R. Ackoff; "Management Misinformation Systems." Management Science, Vol. 14, No. 4, December 1967, P. 147-156.

[2] L. Bally, J. Brittan and K.H. Wagner; "A Prototype Approach to Information System Design and Development" Information and Management, Vol. 1, 1977, p. 21–26.

[3] T.J. Bentley, "Defining Management's Information Needs", Proc. AFIPS. Fall Joint Computer Conf., Vol. 45, 1976, p. 869–876.

[4] Business Systems Planning - Information Systems Planning Guide. IBM 9E20-0527-2, White Plains, New York, October 1978.

[5] E.W. Chadler and P. Nador; "A Technique for Identification of User's Information Requirements, The First Step in Information System Design", IFIP Cong. Proc. Vol, 1971, p. 819–826.

[6] G. Davis; MIS, Conceptual Foundation, Structures and Development, McGraw-Hill, New York, 1974.

[7] K. Ewusi-Mensah, “Criteria for Decomposing an Information System into its Subsystems for Business Systems Planning”, G320-2702, IBM Corporation, Los Angeles Scientific Center Report, March, 1980.

[8] F. Harary, R.Z. Norman and D. Cartwright; Structure Models: An Introduction to the Theory of Directed Graphs, John Wiley, New York, 1965.

[9] E.G. Homer: “A Generalized Model for Analyzing Management Information Systems”, Management Sci., Vol, July 1962. p. 500–516.

[10] B. Langefors, "Information Systems", IFIP Cong. Proc. Vol, 1974, p. 937–945.

[11] I.J. Lieberman; "A Mathematical Model for Analyzing Management Information Systems", Management Sci., Vol. July 1956, p. 327–336.

[12] J.C. Miller; "Conceptual Models for Determining Infor-

mation Requirements", Proc. AFIPS, Spring Joint Computer Conf., Vol. 25, 1964, p. 609–620.

[13] Malcolm C. Munro and Gordon B. Davis; "Determining Management Information Needs: A Comparison of Methods", MIS Quarterly, June 1977, p. 55–66.

[14] D.T. Ross and K.E. Schoman, Jr.; "A Structured Analysis for Requirements Definition", IEEE Trans. on Software Engineering, Vol. SE-3, No. 1, Jan. 1977, p. 6–15.

[15] R. Stamper; Information in Business and Administrative Systems, Halstead Press, John Wiley, New York 1973.

[16] W.M. Taggart, Jr. and M.O. Tharp; "A Survey of Information Requirement Analysis Techniques", Computing Surveys, Vol. 9, No. 4, Dec. 1977, p. 273–290.

[17] W.M. Taggart, Jr. and M.O. Tharp; "Dimensions of Information Requirements Analysis", Data Base, Vol. 7, Sept. 1975, p. 5–13.

[18] D. Teichroew and E.A. Hershey III; "PSL/PSA. A Computer-Aided Technique for Structured Documentation and Analysis of Information Processing Systems", IEEE Trans. on Software Engineering, Vol. SE-3, No. 1, Jan. 1977, p. 41–48.

Table A1

Data-Process Usage Matrix

<table><tr><td rowspan="2">DATA</td><td colspan="21">PROCESS</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Business Planning</td><td>Org. Analysis</td><td>Review &amp; Control</td><td>Financial Plan.</td><td>Capital Acquisit.</td><td>Research</td><td>Forecasting</td><td>Design &amp; Develop.</td><td>Prod. Spec. Maint.</td><td>Purchasing</td><td>Receiving</td><td>Inventory Control</td><td>Workflow Layout</td><td>Scheduling</td><td>Capacity Plan.</td><td>Material Reqmts.</td><td>Operations</td><td>Territory Mgmt.</td><td>Selling</td><td>Sales Admin.</td><td>Order Servicing</td><td>Shipping</td><td>General Acct.</td><td>Cost Planning</td><td>Budget Acct.</td><td>Personnel Plan.</td><td>Recruit Develop.</td><td>Compensation</td><td></td><td></td></tr><tr><td>Planning</td><td></td><td>1</td><td>1</td><td></td><td></td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>Financial</td><td>1</td><td></td><td>1</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td></td><td>1</td><td>1</td><td>1</td><td></td></tr><tr><td>Product</td><td></td><td></td><td></td><td></td><td></td><td>1</td><td>1</td><td></td><td>1</td><td></td><td></td><td>1</td><td>1</td><td></td><td></td><td></td><td></td><td>1</td><td></td><td>1</td><td>1</td><td></td><td>1</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Parts Master</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Bill of Material</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Vendor</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td>1</td><td></td><td></td><td>1</td><td>1</td><td></td><td></td><td></td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>Raw Material Inv.</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Fin. Goods Inv.</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Facilities</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Work in Progress</td><td></td><td></td><td></td><td></td><td>1</td><td></td><td></td><td></td><td></td><td></td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td></td><td></td><td></td></tr><tr><td>Machine Load</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td></td><td></td><td></td><td></td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Open Reqmts.</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td></td><td></td><td></td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Routings</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td></td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Customer</td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td></td><td>1</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Sales Territory</td><td></td><td></td><td></td><td></td><td></td><td>1</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Order</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Cost</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Employee</td><td></td><td></td><td></td><td></td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td>1</td><td>1</td><td>1</td><td></td><td></td><td></td></tr></table>

Appendix A

We define a data class (process) to be a collection or set of data objects (functions or decision-making units) grouped together for administrative purposes. That is, data $d_{t}$ is:

$$
d _ {i} = \left\langle d _ {i} \mid i \in I \right\rangle .
$$

where $I$ is an arbitrary index set defined by some grouping criteria. Similarly, process $p_j$ is:

$$
\boldsymbol {P} _ {j} = \left\{\boldsymbol {p} _ {j} \mid j \in J \right\}.
$$

where J is also an arbitrary index set.

A Data Usage Matrix: $A_{u}$ , illustrated in Table A1, is given by:

$A_{u} = (a_{t})$ where $a_{t} = \left\{ \begin{array}{ll}\mathbf{1} & \text{If data } a_{t}\text{ is used by process } p_{t}\\ 0 & \text{Otherwise} \end{array} \right.$

$A_{u}^{1} = (a_{p})$ ; $a_{p} = \left\{ \begin{array}{ll} 1 & \text{If process } p, \text{ uses data } d, \\ 0 & \text{Otherwise} \end{array} \right.$

$A_{u}^{1}$ is the transpose of $A_{u}$ .

A Data Creation Matrix: $A_{c}$ , illustrated in Table A2, is given by:

$$
\begin{array}{l} A _ {c} = \left(a _ {i j} ^ {\prime}\right); a _ {i j} ^ {\prime} = \left\{ \begin{array}{l l} 1 & \text { If   data } d _ {i} \text { is   created   or } \\ & \text { derived   by   process } p _ {j} - \\ 0 & \text { Otherwise } \end{array} \right. \\ A _ {c} ^ {\mathsf {T}} = \left(a _ {j i} ^ {\prime}\right); a _ {j i} ^ {\prime} = \left\{ \begin{array}{l l} 1 & \text { If   process } p _ {j} \text { creates   or   derives   data } d _ {i} \\ 0 & \text { Otherwise } \end{array} \right. \end{array}
$$

$A_{\mathrm{c}}^{\mathrm{T}}$ is the transpose of $A_{\mathrm{c}}$ .

The Structure of Information Flow is illustrated in Tables A3 and A4. They are given by:
Let

$$
A _ {c} ^ {\dagger} A _ {u} = \sum_ {i} a _ {j t} ^ {\prime} a _ {t k} = (\alpha_ {j k})
$$

where we define

$\alpha_{jk} = \left\{ \begin{array}{ll}1 & \text{or more if and only if process } p, \text{ creates} \\  & \text{any data } d, \text{ which is used by process } p_k - \\ 0 & \text{Otherwise} \end{array} \right.$

Similarly

$$
A _ {u} A _ {c} ^ {\mathrm{T}} = \sum_ {j} a _ {i j} a _ {i k} ^ {\prime} = (\alpha_ {i k} ^ {\prime})
$$

Table A2  
Data-Process Creation Matrix

<table><tr><td rowspan="2">DATA</td><td colspan="19">PROCESS</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Business Planning</td><td>Org. Analysis</td><td>Review &amp; Control</td><td>Financial Plan.</td><td>Capital Acquisit.</td><td>Research</td><td>Forecasting</td><td>Design &amp; Develop.</td><td>Prod. Spec. Maint.</td><td>Purchasing</td><td>Receiving</td><td>Inventory Control</td><td>Workflow Layout</td><td>Scheduling</td><td>Capacity Plan.</td><td>Material Reqmts.</td><td>Operations</td><td>Territory Mgmt.</td><td>Selling</td><td>Sales Admin.</td><td>Order Servicing</td><td>Shipping</td><td>General Acct.</td><td>Cost Planning</td><td>Budget Acct.</td><td>Personnel Plan.</td><td>Recruit Develop.</td><td>Compensation</td></tr><tr><td>Planning</td><td>1</td><td></td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Financial</td><td></td><td></td><td></td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Product</td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Parts Master</td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Bill of Material</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Vendor</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Raw Material Inv.</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Fin. Goods Inv.</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Facilities</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Work in Progress</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Machine Load</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Open Reqmts.</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Routings</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Customer</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Sales Territory</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Order</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Cost</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Employee</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Table A3
Process vs. Process Matrix

<table><tr><td rowspan="2">Process</td><td colspan="26">Process</td><td></td><td></td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td><td>16</td><td>17</td><td>18</td><td>19</td><td>20</td><td>21</td><td>22</td><td>23</td><td>24</td><td>25</td><td>26</td><td>27</td><td>28</td></tr><tr><td>1. Business Plan</td><td></td><td>1</td><td>1</td><td></td><td></td><td></td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>2. Org. Analysis</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3. Review &amp; Control</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4. Financial Plan</td><td></td><td>1</td><td>1</td><td></td><td></td><td></td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>5. Capital Acquis.</td><td>1</td><td></td><td>1</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>6. Research</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>7. Forecasting</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td>1</td><td>1</td><td>1</td><td></td><td></td></tr><tr><td>8. Design &amp; Develop.</td><td></td><td></td><td></td><td></td><td></td><td>1</td><td>1</td><td></td><td>1</td><td></td><td></td><td></td><td>1</td><td>1</td><td></td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>-</td><td></td><td></td></tr><tr><td>9. Prod. Spec. Maint.</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>10. Purchasing</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td></td><td>1</td><td></td><td></td><td>1</td><td>1</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>11. Receiving</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>12. Inventory Control</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>13. Workflow Layout</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td></td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>14. Scheduling</td><td></td><td></td><td></td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td></td><td></td><td></td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>15. Capacity Plan</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td></td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>16. Material Reqmt.</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>17. Operations</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td></td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>18. Territory Mgmt.</td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td>1</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td>1</td><td>1</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>19. Selling</td><td></td><td></td><td></td><td></td><td></td><td>1</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>20. Sales Admin.</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>21. Order Servicing</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>22. Shipping</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>23. Gen. Accounting</td><td></td><td>-</td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>24. Cost Planning</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>25. Budget Account</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td>1</td><td>1</td><td>1</td><td></td><td></td></tr><tr><td>26. Personnel Plan</td><td></td><td></td><td></td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>27. Recruit Delevop</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>28. Compensation</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="28">Table A4Data vs. Data Matrix</td><td></td></tr><tr><td rowspan="2">Data</td><td colspan="27">Data</td><td></td></tr><tr><td>1</td><td></td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td><td>16</td><td>17</td><td>18</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>1. Planning</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td rowspan="18">1</td><td rowspan="18"></td><td></td></tr><tr><td>2. Financial</td><td>2</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td rowspan="17"></td><td></td></tr><tr><td>3. Product</td><td></td><td></td><td></td><td></td><td>1</td><td>1</td><td></td><td></td><td></td><td>1</td><td>1</td><td></td><td>1</td><td></td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4. Parts Master</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>5. Bill of Material</td><td></td><td></td><td></td><td>1</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td></td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>6. Vendor</td><td></td><td></td><td></td><td></td><td>1</td><td>1</td><td></td><td></td><td></td><td></td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td></td></tr><tr><td>7. Raw Material Inv.</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>8. Fin. Goods Inv.</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td></td></tr><tr><td>9. Facilities</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td></td></tr><tr><td>10. Work in Progress</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td></td></tr><tr><td>11. Machine Load</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td></td></tr><tr><td>12. Open Reqmts.</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td></td></tr><tr><td>13. Routings</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td></td></tr><tr><td>14. Customer</td><td></td><td></td><td></td><td>1</td><td>2</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td></td></tr><tr><td>15. Sales Territory</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td></td></tr><tr><td>16. Order</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td></td></tr><tr><td>17. Cost</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td></td></tr><tr><td>18. Employee</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

where we define

$\alpha_{rk}^{\prime}=\left\{\begin{array}{ll}1 & \text{or more if and only if data } d_{k} \text{ is used by} \\ & \text{any process } p_{k} \text{ to create/derive data } d_{k} \\ 0 & \text{Otherwise}\end{array}\right.$

In graph theoretical terms, the matrix $(a_{jk})$ or $(a_{ik}^{\prime})$ describes the existence and number of paths from one process (or data) to another process (or data) through any data (or process), (see, for example [8]).

## Appendix B

## Data/Process Flow Procedure

The objective in this procedure is to construct the flow of information through the business organization by showing the transformations that each data class undergoes through interactions with business processes or functions until the final data results. Any missing data is thus uncovered: if, for example, a process accepts data as input, but does not produce any output from it, there must be a logical error. Such discoveries will be significant in identifying the sources of some of the information needs and problems. The main steps of a procedure for generating the data-process flow paths are:

1) Begin If $\alpha_{i,k}$ is not empty. Then Set Data $I' = Data I_A$ Else
End Procedure;

II) Compare Procedures I and II\_A
If Process I = Process II\_A. Then
Set Process I' = Process II\_A
Go to Step III;

If preceding step is 1. Then
Output Data $I_A \to$ Process $I \to$ Data $I_B$ Return to Step 1 and look for new Data $I_A$

Else
Output the results and pop-up stack P
Return to Step V and continue to look for
New Data I $_{A}$ '' and Process I'' which follows
the current value of a $_{th}$ .

III) For the same Processes I and II,
Compare Data I $_{B}$ and II
If Data I $_{B}$ = Data II, Then
Set Data II' = Data II
Go to Step IV;
Else
If preceding Steps are I and II, Then
Output Data I $_{A}$ → Process I → Data I $_{B}$ Return to Step I and look for new Data I $_{A}$ Else
Output the results and pop-up stack P
Return to Step V and look for new
Data I $_{A}$ " and Process I" which follows the
current value of α $_{ik}'$

IV) Compare Processes II $_{A}$ and II $_{B}$ If Process II $_{A}$ = Process II $_{B}$ , Then
Update: Set Data N = Data II' = Data II
(That is, Data II updates itself, Data II = Data I $_{B}$ )
Output the Result
Return to Step II and look for new Process II $_{A}$ which follows the current value of $\alpha_{jk}$ .

Else
Set Process $II' = Process II_{B}$ push-down Stack D (to save current location and value of $\alpha_{ik}'$ ).
Continue with the search;

V) Compare Data $I_{A}^{\prime\prime}$ and Data $II^{\prime}$ (That is, new Data $I_{A}$ );
If Data $II^{\prime}=$ Data $I_{A}^{\prime\prime}$ and
Process $II^{\prime}\approx$ Process $I^{\prime\prime}$ Then
Set Data $III^{\prime}=$ Data $I_{B}^{\prime\prime}$ Push-down Stack P (to save current location and value of $\alpha_{jk}$ )
(Note: Data $II^{\prime}=$ Data $I_{A}^{\prime\prime}$ and Process $II^{\prime}=$ Process $I^{\prime\prime}$ )
Return to Step II;
Else
Set Final Data = ‘\*\*’ (That is, unknown)
Output the results and pop-up Stack D
If Stack D is empty, Then
Return to Step I
Else
Return to Step II and look for new Process $II_{A}$ which follows the current value of $\alpha_{jk}$ .

VI) Repeat Steps I thru V till the entire paths generated by the matrices $\alpha_{ik}'$ and $\alpha_{jk}$ (That is, Data vs. Data, and Process vs. Process) have been used in constructing the Data-Process Flow paths for the entire organization End: Procedure;

In order to save computational time during the actual program implementation of the above procedure the search is restricted to only two stacks of queues D and P, representing the data vs. data matrix (i.e., $\alpha_{jk}^{\prime}$ ) and the process vs. process matrix (i.e., $\alpha_{jk}$ ) respectively. This restriction appears to be a drawback; however, extensive experimental results demonstrate conclusively that any information path omitted as a result of the restriction is later recovered when the information flow paths generated by the procedure are represented in a tree-structure form.

It has also been observed from sample data analyzed that the flow paths generated by the search procedure do invariably contain some redundant information. This indicates that some information flow paths are later found to be subsets of, or contained in, some other information flow paths.

## Maximal Complete Subgraphs Procedure

This procedure deals with generating maximal complete subgraphs of the data-process flow paths. Each data or process

## 314 Applications

is treated as a node in a directed graph and the procedure essentially looks for a match between corresponding nodes in any two data-process flow paths.

$p_{k}$ is the $k$ th node of the complete subgraph (i.e. the data-process flow path)

M is the total number of complete subgraphs $i = 1, 2, 3, \ldots, N$ is the total number of nodes

$t_{q}(j_{r})$ denotes the qth (rth) complete subgraph for node $i(j)$ , where $q, r = 1, 2, 3, \ldots$

Let

$$
C _ {t _ {q}} = \left\{p _ {2 k + 1}, p _ {2 (k + 1)} \right\} \text { for } k = 1, 2, 3, \dots\tag{1}
$$

denotes the nodes in the complete subgraph C, excluding nodes 1 and 2.

Similarly

$$
T _ {j _ {r}} = \left\{p _ {2 k - 1}, p _ {2 k} \right\} \text { for } k = 1, 2, 3, \dots\tag{2}
$$

denotes nodes in the complete subgraph $T_{j}$ .

The procedure consists of two parts - Forwardtrack and Backtrack. In the former case we look for complete subgraphs which are subsets of complete subgraphs generated earlier. But in the latter case, we look for complete subgraphs which are contained in other complete subgraphs. We now describe the procedure for generating the maximal complete subgraphs of the data-process flow paths enumerated.

## Forwardtrack

For each complete subgraph $C_i$ and $T_{j}$ ,

$T_{J_r} \subset C_{I_q}$ then delete $I_{I_r}$

This implies that for any pair $C_{i_q}$ and $T_{j_r}$ If

$$
p _ {2 k + 1} = p _ {2 k - 1} \text { for } k = 1, 2, 3, \dots
$$

and $p_{2(k + 1)} = p_{2i}$

Then $T_{j_r} \subset C_{I_q}$ and we delete $T_{j_r}$ from $M$

We repeat the search till all subsets $T_{i}$ , have been deleted from M and we are left with $M_{1}$ , where

$$
M _ {1} = M - \sum_ {T _ {i _ {r}} \in C _ {i _ {q}}} T _ {i _ {r}}\tag{3}
$$

Backtrack.

Let

$$
S _ {i _ {q}} = \left\{p _ {2 k + 1} \cdot p _ {2 (k + 1)} \right\}, \text { for } i = N, N - 1, N - 2, \dots , 1
$$

and

$$
C _ {I,} = \left\{p _ {2 k - 1}, p _ {2 k} \right\}
$$

In this case we look for complete subgraphs $S_{t_q}$ and $C_t$ , such that $C_t \supset S_{t_q}$

That is, if

$$
\begin{array}{l} p _ {2 k - 1} = p _ {2 k + 1} \text { for } k = 1, 2, 3, \dots \\ \text { and } \end{array}
$$

$$
P _ {2 k} = P _ {2 k + 1}
$$

Then $C_{j} \supset S_{i,j}$ and we delete $C_{j}$ from $M_{1}$

We repeat the procedure till all subsets $C_{i}$ , have been deleted from $M_{1}$ and we are left with $M_{\max}$ where

$$
M _ {\max} = M _ {1} - \sum_ {C _ {j _ {0}} \supset S _ {i _ {q}}} C _ {j _ {0}}\tag{4}
$$

Upon termination of both the Forwardtrack and Backtrack procedures, all complete subgraphs $M_{max}$ remaining out of the initial M will be maximal and will therefore constitute the maximal complete subgraphs of the data-process flow paths enumerated. That is.

$$
M _ {\max} = M = \sum_ {T _ {i}, \in C _ {i}} T _ {i j} = \sum_ {C _ {i}, \supset S _ {i}} C _ {i j}
$$
