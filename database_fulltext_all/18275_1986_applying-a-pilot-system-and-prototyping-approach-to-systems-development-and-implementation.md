---
otero_id: 18275
otero_key: "8BQN87YX"
title: "Applying a pilot system and prototyping approach to systems development and implementation"
authors: "Marius Janson"
year: "1986"
journal: "Information & Management"
doi: "10.1016/0378-7206(86)90084-4"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Applying a Pilot System and Prototyping Approach to Systems Development and Implementation

Marius Janson

University of Missouri-St. Louis,

8001 Natural Bridge Road, St. Louis, MO 63121, USA

The acquisition and implementation of standard software packages carries with it a need for compromise between the software's capabilities and user information needs. The likelihood for successfully meeting the user's needs, as evidenced by this case study, can be greatly increased by employing a combination of pilot systems and prototypes in the implementation process.

Keywords: Pilot System, Prototype, System Design, Evolutionary design, User Participation, End-User Computing.

![](/api/attachments/8BQN87YX/fulltext/images/8ae1cddb1414639f47c0f2e25317a90d3a14c8cf59aedcce369f21e8d1684616.jpg)

Marius A. Janson received his Ph.D. from the University of Minnesota. He is Assistant Professor of Management Information Systems in the department of Management Science and Information Systems at the University of Missouri-St. Louis. Dr. Janson has worked for the N.V. Philips Gloeilampen Fabrieken (The Netherlands), Honeywell, and Research Inc. His publications have appeared in various journals including Management Information Systems Quarterly, Decision

Sciences, and Information & Management.

## 1. Introduction

Implementing standard application software packages has been proposed by Gremillion [4] as a solution to the problem of long systems development lead times. A key to successfully implementing this approach is finding an appropriate match between the capabilities of already existing software packages and the user's information needs. Standard software offers limited degrees of freedom for change and therefore preference is given to adjusting user information needs over modifying software specifications in situations where an appropriate match is not found. This is in sharp contrast with traditional systems development methods, where systems are specifically designed to match user information needs as closely as possible. What is needed, therefore, is a unique implementation approach that exploits the advantages of standard software packages and avoids the problem of installing information systems that are inadequate in meeting the user's information requirements.

The objectives of this article are to present a method for implementing standard application software packages and to illustrate this method with a case study. First, the author discusses the use of pilot systems and prototypes in the implementation effort. The nature and characteristics of pilot systems and prototypes are compared and contrasted, resulting in the identification of the different tasks that each can accomplish. Second, the implementation and failure of a decision support system for energy conservation, discussed by Dickson and Janson [3] elsewhere, are reviewed. The findings of these authors are placed in context by prescribing the manner in which an integrated approach consisting of pilot systems and prototypes could have prevented the systems failure, thus providing a general method for standard software implementation. Finally, in reference to this case where implementation had failed, the author discusses the possibility of salvaging the system by using pilot systems and prototypes.

## 2. A Method for Systems Implementation

Standard application software represents in effect a completed information system with limited possibilities for change, demanding different implementation approaches than are required for systems specifically designed to meet user needs. Implementing standard software, Welke [10] argues, should always be preceded by systems testing involving all the affected parties. Testing may, however, be prohibitively expensive, especially in the case of complex systems using large quantities of data. The combination of pilot systems and prototypes provides an approach to systems implementation that allows user testing at greatly reduced cost. A major objective of pilot systems is to verify that systems specifications are in sufficient agreement with the user's need. Prototypes, on the other hand, offer a method for a partial systems redesign in cases where the disparity between the software capabilities and the user's needs is irreconcilable. The nature and characteristics of pilot systems and prototypes are discussed in turn.

## 2.1. Pilot Systems

A pilot system, in the context of information systems, is defined as a scaled-down version of a proposed application package. It offers a subset of capabilities present in the total system without sacrificing robustness, completeness, or reliability. Robustness implies that the pilot system does not yield unreasonable answers when operating with operational, and, therefore at times, erroneous data. Completeness means that important parts of the system have not been left out from the pilot systems. Finally, reliability indicates that the pilot system operates as intended under many circumstances. These concepts have been studied in greater detail by Little [6] in connection with models for managerial decision making. These characteristics make it possible to install the pilot system in its intended environment and enable the user to test the proposed application package using normal data, under regular operating conditions, and at greatly reduced cost.

The purpose for installing pilot systems can be any of the following:

\* to allow the user to test all major system components that are crucial to its success within the organization,

\* to enable the user to detect organizational resistance to the system, or

\* to provide training for staff members who will be using the system.

The major purpose, then, of a pilot system is to allow the user to verify that a standard software package meets the organization's information needs, with at most only minor changes. A second important objective is to observe organizational reactions to the pilot systems. Critically evaluating these reactions helps one to formulate better implementation strategies of the complete information system. Any required changes can be either organizational adjustments or modifications of the standard software package. Often, changes to existing software can most easily be made through the use of prototypes.

## 2.2. The Prototyping Process

The application of prototyping to the development of information systems has recently received a great deal of attention [1], [2], [7]. Naumann and Jenkins [7] discuss prototyping in its most general form by defining four process steps: (1) identifying basic system requirements, (2) developing a working prototype, (3) implementing and using the prototype, and (4) revising and enhancing the prototype. Basic systems requirements are established through close consultation with system users and these in turn determine the functional properties of the prototype. Prototype construction should focus on its intended purpose, which is often directed toward user evaluation rather than toward long-term use. This implies that system efficiency, data robustness, validity, and accuracy are often not a major concern during the prototype design. The process of implementing and using a prototype includes testing and evaluation, which are crucial to the success of this method, and therefore the construction of a prototype should be preceded by detailed test plans.

Table 1  
A Comparison Between Pilot System and Prototype

<table><tr><td></td><td>PILOT SYSTEM</td><td>PROTOTYPE</td></tr><tr><td>PURPOSESYSTEMSDEVELOPMENT</td><td>NO</td><td>YES</td></tr><tr><td>REQUIRED ACTIONADJUST USER NEEDTO MATCH SYSTEM</td><td>YES</td><td>NO</td></tr><tr><td>ADJUST SYSTEM TOMATCH USER NEED</td><td>NO</td><td>YES</td></tr><tr><td rowspan="3">APPLICATION AREAUSER TRAININGSYSTEM TESTINGIMPLEMENTATION</td><td>YES</td><td>NO</td></tr><tr><td>BY USER</td><td>BY DESIGNER</td></tr><tr><td>YES</td><td>NO</td></tr><tr><td>CHARACTERISTICROBUST</td><td>YES</td><td>NO</td></tr><tr><td>COMPLETE</td><td>YES</td><td>NO</td></tr><tr><td>RELIABLE</td><td>YES</td><td>YES</td></tr><tr><td rowspan="2">OPERATING CONDITIONSEXPECTED LIFE</td><td>UNDER USERCONTROL</td><td>UNDER DESIGNERCONTROL</td></tr><tr><td>LONG</td><td>SHORT</td></tr></table>

Although Naumann and Jenkins [7] describe prototyping as a general method for information systems design, it can, however, also be employed in the more limited task of modifying standard software packages. Integrating prototypes with pilot systems is advantageous in situations where software changes are needed because organizational changes alone cannot assure a reconciliation between user needs and standard software capabilities. The differences and similarities between the characteristics of pilot systems and prototypes are summarized in Table 1.

This article relates the implementation and failure of a standard software package designed to support energy conservation measures. It illustrates how pilot systems and prototypes can play a role in preventing failure by modifying existing software packages cost effectively.

## 3. A DSS for Energy Conservation

The decision support system under consideration was implemented by the energy agency of a midwestern state in response to the enactment of state and federal energy conservation laws. The agency's objective was to make a preliminary identification of buildings that could benefit from energy conservation measures. A second goal, contingent on the first, was to formulate specific recommendations to reduce energy consumption. Given its limited financial resources, the agency required an information system that accomplished these objectives in the most cost effective manner.

## 3.1. System Development

The strategy proposed by the agency was to send out questionnaires to collect data representative of building energy consumption. After the questionnaire was completed by a member of the building staff, it was returned to the agency for processing and data analysis. The energy efficiency of each building was analyzed by comparing its actual consumption against predetermined standards for buildings of similar construction. Central to the analysis was a model that could predict energy consumption for any given building.

Detailed reports were generated for each building, specifying possible energy conservation measures, investment payback periods, and expected yearly energy savings. The conservation measures included changes in building operating procedures but did not suggest major structural changes for the building. These reports were forwarded to individual building owners or operators for further action. The reports also contained information useful to energy agency personnel in deciding future energy conservation steps, including more detailed energy audits requiring on-site walkthroughs by agency personnel.

The agency was operating under severe constraints, lacking both sufficient time and personnel to undertake systems development. Consequently, the decision was made to implement a standard application software package acquired from an outside consulting firm and purportedly designed for the task at hand. The heart of the software package was a deterministic model that predicted energy consumption based on building characteristics and which, in turn, compared this prediction with the energy actually consumed. Energy conservation measures were called for when actual consumption was in excess of model predictions.

## 3.2. Systems Implementation and Failure

The system was purchased and installed and data were collected on several thousand buildings, each with over 300 data items. Subsequent analysis of these data did not result in useful information because of inadequacies in the information system and in the data. These factors prematurely ended the energy conservation effort.

Initial contacts with the consulting firm should have alerted energy agency personnel to the existence of implementation problems at several levels. The primary interest of the energy agency was the preliminary identification of high energy consuming buildings simply and inexpensively. The consulting firm, however, was actively engaged nationally in highly sophisticated energy consumption studies. As a result, the information system provided to the energy agency required large quantities of data and had a level of complexity entirely inappropriate for the agency's limited objective.

A different source of implementation problems arose from the sheer quantity of data collected. This caused needless loss of time, both for complementing the questionnaire and for keying the data into the agency's database. It also created a high level of frustration for the building staff responsible for data collection. This frustration, combined with the laborious data handling procedures, affected that data quality to such a degree that the database contained many erroneous data items, as well as missing observations.

Moreover, after the results of model runs on a large number of buildings were reported it was discovered that the application package, as initially installed, did not reflect conservation measures already in place, nor was it suitable for midwestern climatic conditions. This necessitated many model modifications, additional data collection efforts, and time consuming reruns.

These problems occurred at different times during the period, starting at the contract negotiations and continuing well into the systems installation phase. The resolution of these problems required frequent communication between the agency and the consulting firm, thus straining the working relationship. In fact, agency personnel felt that the consulting firm became increasingly uncooperative as time went along. These problems discussed have a technical and behavioral origin and either can be resolved or mitigated by employing pilot systems.

## 4. An Alternative Approach to Systems Implementation

A synergistic approach to systems implementation combining pilot systems and prototypes seems to be called for here. The pilot system is a proposal for what should have been done by the energy agency, although it was never implemented. The prototype represents a proposal for a systems redesign, and was built and tested by Janson and Willis [5].

## 4.1. A Pilot System for Energy Conservation

Table 2 illustrates a proposal for a pilot system for energy conservation and contrasts it with the full-scale software package provided by the consulting firm. The reader may recall that a pilot system is defined as a scaled-down version of a proposed application software package, offering a nontrivial subset of its features. The pilot system's database contains data on 40 buildings, acquired with standard production data collection instruments, which were completed by building staff members. The database also contains a reference data set, duplicating the previous data set, but with a low error rate and high integrity because it was collected by energy agency staff members during on-site walkthroughs. These data items are evenly divided over four building types of interest to the energy agency. In contrast, the full-scale system features a model base containing many different building types and a database for over 5000 buildings. All other pilot system components, including data collection, validation, and input procedures, as well as system operating procedures and output reports, are identical to those of the full-scale energy conversation system.

Because the reference data set is considered to be error free, a contrast of the two sets identifies erroneous observations contained in the standard data set. It thus provides a check on the quality and the integrity of the information collected by the questionnaires. It also reveals whether data input and validation procedures are adequate in detecting erroneous and missing observations.

Additional information can be gained by using the two data sets independently. For example, model completeness, simplicity, and reliability can be tested by evaluating the system's performance based on the reference data set. This test would have alerted the agency staff that the conservation system provided by the consulting firm was overly complicated and required data on too many superfluous variables. Model robustness (which means that the model does not give absurd answers when operating on erroneous data) is tested by studying the system performance on the data set contained on the standard questionnaires.

The results of system runs using both data sets give a good indication whether the full-scale conservation system operates as intended by the energy agency and meets its objectives. Because the testing process requires close communication and coordination between the energy agency and the consulting firm, it establishes the degree of cooperation and the quality of the working relationship. This, in turn, is very important because system changes are likely to occur when the system is installed in its full-scale version. Most importantly, this is achieved with a minimum of cost in time and money.

A Comparison Between Pilot System and Complete System

<table><tr><td>COMPONENT</td><td>PILOT SYSTEM</td><td>COMPLETE SYSTEM</td></tr><tr><td>MODEL BASE</td><td>4 BUILDING TYPES</td><td>MANY BUILDING TYPES</td></tr><tr><td>DATA BASE</td><td>40 BUILDINGS</td><td>OVER 5000 BUILDINGS</td></tr><tr><td>DATA COLLECTION PROCEDURES</td><td>FINALIZED</td><td>FINALIZED</td></tr><tr><td>DATA VALIDATION PROCEDURES</td><td>FINALIZED</td><td>FINALIZED</td></tr><tr><td>SYSTEM OPERATING PROCEDURES</td><td>FINALIZED</td><td>FINALIZED</td></tr><tr><td>SYSTEM CONTROL</td><td>UNDER USER CONTROL</td><td>UNDER USER CONTROL</td></tr><tr><td>SYSTEM REPORTS AND OUTPUT</td><td>FINALIZED</td><td>FINALIZED</td></tr></table>

![](/api/attachments/8BQN87YX/fulltext/images/6742d2015d658d9d73b3cb4ab587ce0baa22014242e5b53a97726b41c6ab6b77.jpg)  
Fig. 1. The Prototyping Process.

## 4.2. A Prototype for Systems Redesign

Given that the energy conservation information system as supplied by the consulting firm failed to meet the agency's needs, the possibility of salvaging the energy conservation effort cost effectively would be of interest to the energy agency. A prototype approach to a systems redesign is one way of achieving this objective. Figure 1 illustrates the initial exploratory stage of the prototyping process, in which the function of a prototype is to determine: (1) whether the data as previously collected can be used as guidelines for energy conservation measures, and (2) whether they can support the construction of energy predictive models and the estimation of energy model parameters using some minimal set of variables.

Following the procedure depicted in Figure 1, Janson and Willis [5] selected a subset of variables from the database and subjected these to validation and error correction routines. The selection process was based on engineering principles to ensure that the variables chosen would be relevant in predicting energy consumption. This set of variables became the input for a statistically based energy modeling effort. The development of a model for energy prediction was carried out using a combination of robust linear regression and regular least squares. The outcome of the prototyping activity was a model that reflected structural and operational building characteristics making use of previously collected data to support energy conservation decisions.

Table 3 contrasts the exploratory prototypical model with the final model needed to support a full-scale conservation effort. The models differ on important characteristics. First, the prototypical model is small compared to the final model in the number of building types, the number of buildings within building types, and the number of variables. Second, because of its exploratory nature, the prototypical model does not perform tasks required of an operational model such as data validation and the calculation of realizable energy savings. Finally, an important difference is in the type of software used in both models. The prototyping effort is supported by SAS [9], [10], which offers a wide range of statistical techniques and data handling, as well as programming capabilities using macros. The full-scale information system requires software that features a database and a procedural language with database query capability.

Table 3  
A Comparison Between Prototype and Final Model

<table><tr><td>CHARACTERISTIC</td><td>PROTOTYPE</td><td>FINAL MODEL</td></tr><tr><td>BUILDING TYPES</td><td>1</td><td>MANY</td></tr><tr><td>DATA SET SIZE</td><td>SMALL</td><td>LARGE</td></tr><tr><td>NUMBER OF VARIABLES</td><td>SMALL</td><td>LARGER</td></tr><tr><td>DATA BASE</td><td>NO</td><td>YES</td></tr><tr><td>DATA VALIDATION</td><td>NO</td><td>YES</td></tr><tr><td>HANDLING OF EXCEPTIONAL CASES</td><td>NO</td><td>YES</td></tr><tr><td>MODEL TYPE</td><td>STATISTICAL</td><td>STATISTICAL/DETERMINISTIC</td></tr><tr><td>IDENTIFY ENERGY INEFFICIENT BUILDING</td><td>YES</td><td>YES</td></tr><tr><td>REALIZABLE ENERGY SAVING ESTIMATED BTU/YR/SQRFT</td><td>YES</td><td>YES</td></tr><tr><td>OPERATIONAL CHANGES SPECIFIED</td><td>NO</td><td>YES</td></tr><tr><td>REALIZABLE ENERGY SAVING ESTIMATED DOLLAR/YR/SQRFT</td><td>NO</td><td>YES</td></tr><tr><td>SOFTWARE</td><td>SAS</td><td>SASDATA BASE QUERY LANGUAGEPROCEDURAL LANGUAGE</td></tr></table>

## 5. Conclusion

Implementation failure is often analyzed in situations where the system has been specifically designed to meet user information needs. This article analyzed the implementation of standard software packages where the likelihood of failure is increased by the necessity of adjusting user need to the system's capabilities. The problem was aggravated by communication difficulties cause by geographic location, as well as by the disparity in objectives between the software supplier and the users and the varying degrees of commitment by all parties to the system's success. Applying a pilot system for selecting and implementing the software package would have resulted in identifying the causes of these failures, thus greatly improving the likelihood of the system's success. Therefore, the combined use of pilot systems and prototypes outlined in this article forms a paradigm for implementing standard software packages.

## References

[1] Alavi, M. "An Assessment of the Prototyping Approach to Information Systems Development," Communications of the ACM, Vol. 27, No. 6, 1984, pp. 556–563.

[2] Boar, B.H. Application Prototyping, Wiley, New York, New York, 1984.

[3] Dickson, G.W., and Janson, M.A. "The Failure of a DSS for Energy Conservation: A Technical Perspective," Systems Objectives Solutions, Vol. 4, No. 2, 1984, pp. 69–72.

[4] Gremillion, L. "Breaking the systems development bottleneck," Harvard Business Review, Vol. 61, No. 2, 1983, pp. 130–137.

[5] Janson, M.A., and Willis, R.E. "Robust Methods Applied to Energy-Consumption Data," Decision Sciences, Vol. 16, No. 4, 1985, pp. 343–356.

[6] Little, J.D.C. "Models and Managers: The Concept of a

Decision Calculus," Management Science, Vol. 16, No. 6, 1970, pp. B466–B485.

[7] Naumann, J.C., and Jenkins, M.A. “Prototyping: The New Paradigm for Systems Development,” MIS Quarterly, Vol. 6, No. 3, 1982, pp. 29–44.

[8] SAS Institute Inc., SAS User's Guide: Basics, 1982 Edition, Cary, North Carolina, SAS Institute Inc., 1982.

[9] SAS Institute Inc., SAS User's Guide: Statistics, 1982 Edition, Cary, North Carolina, SAS Institute Inc., 1982.

[10] Welke, L.A. "Buying Software," in Systems Analysis and Design, W.W. Cotterman, J.D. Cougar, N.L. Enger and F. Haroki, (eds.), Elsevier North-Holland, Amsterdam, The Netherlands, 1981. pp. 400-416.
