---
otero_id: 17404
otero_key: "W38FFNCY"
title: "Towards a computer-aided economic planning support system"
authors: "Motaz Khorshid"
year: "1995"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(93)e0038-f"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Towards a computer-aided economic planning support system

Motaz Khorshid

Cairo University, 5 Tharwat Street, Orman, Giza, Egypt

## Abstract

The purposes of this paper are (i) to outline a conceptual framework of a computer-based DSS directed to support the development planning process, and (ii) to present the main features and structure of a model-based management system designed to assist in formulating and testing medium-term economic plans. The system has proven to be useful for organizing, systemizing and supporting the development planning process. While the economic planning support system (EPSS), described in this paper, has been applied to the Kuwait economy, it was initially established with the aim of creating a generally applicable computer-based system which can be applied to other national economies.

Keywords: Decision support systems (DSS); Development planning; Economywide models.

## 1. Conceptual design of the economic planning support system

The proposed EPSS is a computer-based system designed to help the policy maker and economic planner in improving the effectiveness of the development planning process. The modular design of the EPSS is schematized in Figure 1. The central part of the figure is the planning support management system (PSMS). The PSMS is a software system, which organizes the overall performance of the system and facilitates the access of various users to the three basic subsystems: the information, interpretation and mod-

elling systems.

## 2. The economic information system

The information system consists of the economic database (EDB) which is managed by three software systems; the database management system (DBMS), the data balancing and adjustment software (DBAS), and the statistical program library (SPL).

The EDB includes world-wide, economy-wide and sectoral data required for the development of socio-economic plans. As shown in Figure 1, the domestic database is broken down into three conceptual levels. The first level groups the collected raw data required to construct the socio-economic data systems. In the second level of the EDB, the collected raw data are subjected to validation, adjustment and aggregation processes

to produce the establishment surveys, foreign trade bulletin, household budget survey and the population census. Most of the data management and report generating facilities required for the above surveys are provided by the DBMS. The third level of the economic data framework consists of input/output tables, social accounting matrices (SAM), flows of funds accounts and national income accounts. To construct these accounting systems, programs for data assembly, adjustment and testing are needed. This is accomplished using the data balancing and adjustment software (DBAS) coupled with the DBMS. The DBAS uses a number of analytical tools such as: input/output updating techniques $[1,2]$ , the RAS method $[1,3]$ and other statistical algorithms. Finally, the third software module included in the economic information system is the statistical program library (SPL). The purpose of this SPL is mainly to compute summary statistics, trends and structural parameters and is generally equipped with advanced display capabilities.

During the second half of 1980s, a set of input/output tables and social accounting matrices (SAMs) for the Kuwait economy were constructed [5]. A number of algorithms directed to organize, adjust and test the consistency of the socio-economic data were implemented, and incorporated in the DBAS. Furthermore, a computer-based for constructing and balancing various input/output tables and social accounting matrices was developed. The first part of this system helps the user to build and test the consistency of the SAM using national accounting data.

![](/api/attachments/W38FFNCY/fulltext/images/d37349de3f136199bcfef7a5136cc8bbdb8bba9ad8bb05f17cc8a38d8fe5abc9.jpg)  
Fig. 1. Components of the economic planning support system.

The second part is used to assemble a SAM or an input/output table with the desired level of aggregation.

## 3. The computer-based modelling system

To support the development planning process in Kuwait, a set of economy-wide and sectoral models were formulated and validated. In the first stage of the plan formulation process a four-sector long-term model $[9]$ and an oil/non-oil aggregate computable general equilibrium model $[7]$ was used to test different policy issues and development scenarios for Kuwait up to the year

2015. Based on the selected development scenario, two multisector dynamic computable general equilibrium models [6] were used to project the medium-term performance of the Kuwait economy and to formulate the 1990/91–1994/95 development plan. On the sectoral level, a simulation model for the human resources sector was developed and implemented. An interger programming model was also constructed and used to prepare the long-term plan for the fisheries sector [8].

Given the need to organize and manage the above set of models in a friendly manner, KISR was requested by the Ministry of Planning, in January 1989, to help in the construction of a computer-based modelling system. The modelling system, shown in Figure 1, consists of an economic model base (EMB) and two software systems; the model building language (MBL) and the model-based management system (MBMS).

![](/api/attachments/W38FFNCY/fulltext/images/ed8c72b5f9d107fccf46ef1d1da5adea9419c031395843a1dcb9860f8f3a3af5.jpg)  
Fig. 2. Model execution and display system.

## 3.1. The economic model base

The EMB is divided into three blocks, the economy-wide models directed to capture the major linkages within the economic system and to study the macro-impact of various development scenarios; the specialized or sectoral models that can be used to address a specific economic issue or sector, and the model building blocks which are employed as components of larger models. To create, manage and control the EMB two software system are needed: the model building language (MBL) and the model-based management system (MBMS).

## 3.2. The model building language

A first and important step towards systemizing the model building process is to use an advanced and generalized computer modelling language. The main purpose of a model building language is to enhance the productivity of model builders and to make complicated mathematical models easy to build, modify, understand and solve $[2,4]$ .

All the models included in the economic model base (EMB) are constructed using the general algebraic modelling system (GAMS). GAMS is a computer-based modelling language designed to construct and solve large and complex mathematical programming models in a straightforward and friendly manner $[2]$ . GAMS is equipped with a set of solvers for linear, integer and non-linear programming models. It can also be used to solve linear and non-linear systems of equations. In addition, the recent versions of the GAMS include a software package for building and solving SAM-based economy-wide models. Accordingly, one major advantage of using GAMS in the proposed EPSS is the availability of algorithms required to solve economy-wide and sectoral models.

## 3.3. Model base management systems

The second software system required to organize and manage the set of models stored in the economic model base (EMB) is the model-based management system (MBMS). The concept of model-based management calls for a software package with capabilities similar to that of the DBMS in the database. Accordingly, the MBMS is mainly designed to classify, integrate and manage the set of model input files created by the model building language (MBL). Unfortunately, while there are dozens of commercial DBMS packages, there are no comprehensive model-based management packages currently on the market [11].

Based on the above rationale, KISR team developed an MBMS that can be efficiently used to classify, integrate, select and execute economic models written in GAMS format. This computer-aided system identifies different criteria for selecting a model and directs the user toward the appropriate choice via a menu-driven system. Upon the choice of an economic model, the system helps the user to solve the model and display output results. The software used to incorporate the economic models into the EBM requires two inputs: the GAMS input files of the model, as well as its technical features based on a classification scheme. For instance, the user has to specify the basic model type (economy-wide versus sectoral), the modelling technique (static multiplier, CGE, dynamic simulation or optimization), the planning horizon (short, medium or long-term planning) and the issue of interest (macro-economic management, public finance policy, investment planning program, etc.). The model selection software system directs the user towards the appropriate model given his selection criteria. The user can specify one model or a class of models. Upon the specification of a model class, the model selection system uses the relational database of the model classification criteria, the EMB and the pointers and the linking parameter's library to select the model and display its technical features on the screen.

The model execution and display systems are briefly explained in Figure 2. Upon the request of the user to run the model or conduct some policy experiments, the execution system displays the list of exogenous variables on the screen based on the original GAMS input file. For this purpose, screen management routines are used to display the required information in a more friendly manner. The user can then change the values of the exogenous variables in order to formulate his policy experiment or future scenario. Based on the selected values of the exogenous variables the model execution system creates an updated model input file along with an execution macro and calls the GAMS language to solve the model and generate the solution files. Finally, the output display system uses the solution files and pointers along with the display command entered by the user to prepare and display a list of output tables and figures. The user can then select the set of tables to be displayed on the screen or printed.

## Acknowledgement

This paper is based on the output of a joint project undertaken between the Kuwait Institute for Scientific Researched (KISR) and the Ministry of Planning (MOP) in Kuwait. I am indebted to KISR and the MOP for financial and technical support. I acknowledge with gratitude the substantial assistance of Mounir Ismail who was responsible for the development of the computer system of the MBMS. My dept extends also to Basma Musmar for the implementation of the SAM building and assembly program. I acknowledge finally the substantial encouragement provided by my colleagues at the techno-economics division of KISR.

## References

[1] Bacharach M., Bi-Proportional Matrices and Input-Output Change (Cambridge University Press, Cambrigde, 1970).

[2] Brooke A., Kendrick D., and Meeraus A., Generalized

Algebraic Modelling System - A User's Guide (Scientific Press, New York, 1988).

[3] Byron R.P., The Estimation of Large Social Account Matrices, Statist J.R., Soc. 141 (3) (1987) 359–367.

[4] Geoffrion A.M., An Introduction to Structured Modelling, Management Science 33 (5) (1987) 547–588.

[5] Khorshid M., Dahdah J. and Al-Mussallam N., A consistent Data Framework for the Kuwait Economy: The Social Accounting Matrix of 1983, Kuwait Institute for Scientific Research, Technical Report No. 1 KISR2620, Vol. 2, Kuwait (September 1988).

[6] Khorshid M., A Dynamic Multisector Economy-Wide Model for Kuwait: The Impact on Growth, Welfare and Population Balance, Proceedings of the 6th IFAC/SEDC on Dynamic Modelling and National Economies, Vol. 2, Edinburgh, UK (27–29 June 1989)

[7] Khorshid M., A Dynamic Macro-Economic Model for Kuwait: Analysis of the Medium Term Path, Energy Economics 12 (4) (1990) 389–301.

[8] Khorshid M., and Morgan G.R., A modelling Framework for Fisheries Development planning, Ocean and Shoreline Management 14 (1990) 11–33.

[9] Khorshid M., A Social-Accounting-Matrix Based Long-Term Model for a Gulf Cooperation Council Country: The Kuwait Case, Economic System Research 3 (3) (1991) 299–314.

[10] Stone R., Input-Output Projections: Consistent Prices and Quantity Structures, in: Mathematical Models of the Economy and other Essays (Chapman and Hall, London, 1970).

[11] Turban E., Decision Support and Expert Systems: Management Support Systems, Second Edition (Macmillan, New York, 1990).

![](/api/attachments/W38FFNCY/fulltext/images/b8c5aa1ebd788612f49054b68aebea3ddefd3af13dbfd34030a52bd18f157f86.jpg)

Motaz Khorshid received his B.Sc. degree in Mechanical Engineering from Ain Shams University, his M.Sc. in Industrial Engineering from Cairo University, and his Doctor of Engineering in Computer Simulation Techniques and his Doctor of State in Management Sciences from Paris University. He is currently an associate professor in the Department of Computer and Information Sciences (ISSR) at Cairo University. His re-

search interests include computer simulation methods, economy-wide and sectoral planning models, socio-economic information systems and model-based management systems. He has published in several journals such as the European Journal of Operational Research (EJOR), Economic Systems Research, Energy Economics and Advances in Modelling and Simulation.
