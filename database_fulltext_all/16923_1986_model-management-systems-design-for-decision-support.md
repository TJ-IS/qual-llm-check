---
otero_id: 16923
otero_key: "STRFU8HD"
title: "Model management systems: Design for decision support"
authors: "Lynda M Applegate; Benn R Konsynski; Jay F Nunamaker"
year: "1986"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(86)90124-7"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Model Management Systems: Design for Decision Support

Lynda M. APPLEGATE, Benn R. KONSYNSKI and Jay F. NUNAMAKER

Department of Management Information Systems, College of Business and Public Administration, University of Arizona, Tucson, AZ 85721, USA

Changes in computer technology have provided decision makers with the necessary tools for the design and implementation of computerized models for decision support. These models are frequently developed to solve a specific problem for a specific user and lack the flexibility and generalizability necessary to solve unstructured, strategic problems. In addition, problems of model redundancy, inconsistency, integrity and security have prompted an increased interest in the design of model management systems (MMS) that provide for centralized management of organizational models. This paper describes the use of a framework, developed by the authors, to design an MMS for support of planning decisions within an organization. The architecture of the MMS is described in detail and the rationale for the design decisions is presented.

Keywords: Decision Support Systems; Knowledge Representations; Model Management

![](/api/attachments/STRFU8HD/fulltext/images/7e9badb7ea563e10a14c88bb6ef8f9edf9a449a9b4ae3e8634967f18ebd6d0f1.jpg)

Lynda Applegate is completing her doctoral degree requirements in Management Information Systems at the University of Arizona, College of Business and Public Administration. Her major research focus is the design of management support systems to support organizational strategic planning. Her current research interests include management support systems, model management systems, and the use of artificial intelligence theory and methods for decision support.

![](/api/attachments/STRFU8HD/fulltext/images/09d8d184bf73310cab5d28df9ad3793e4debe8e78a83be253228b54ff58903d8.jpg)

Benn Konsynski is an Associate Professor of Management Information Systems in the College of Business and Public Administration at the University of Arizona. He received his Ph.D. in computer science from Purdue University. His major research focus is computer-aided approaches to information systems design and implementation. Current research interests include model management systems, learning paradigms in decision support systems, business dialogues in distrib uted office environments, and design support for local area networks.

## 1. Introduction

The availability of microcomputers, modelling languages and general purpose spreadsheets has resulted in an increase in the use of models for decision making within organizations [7]. Decision makers, using microcomputers on their desks and spreadsheet and modeling software, can create models rapidly. The models, however, are often problem- and user-specific which limits the ability to develop generalized, flexible decision systems (DSS) for use throughout the organization. In addition, the problems with model redundancy, inconsistency, integrity and security have prompted an increased interest in the centralized management of organizational models in a manner similar to the centralized management of organizational data.

Model Management Systems (MMS) have been proposed to provide generalized support for organizational decision making $[9,6]$ and to provide centralized management of organizational models $[3,7,11]$ . A framework that can be used to guide the choice of an internal representation for the MMS design has been developed by the authors $[2]$ . This paper describes the framework and illustrates its use for the design of an MMS for support of strategic decision making within organizations. The MMS design utilizes semantic inheritance networks and frames to represent the decision and modeling knowledge for the system. This design permits representation of the unstruc-

![](/api/attachments/STRFU8HD/fulltext/images/9d4d4dc80901cc5ebaa9fbcbf150aeb67bb107b1a4f19de7b58a922f9d473daa.jpg)

decision support for system analysis and design, performance evaluation of computer systems, and computer-assisted instruction for MIS education.

tured nature and complexity of the strategic planning decision domain and also the wide variety of quantitative and qualitative planning models.

## 2. Framework for MMS Design

An MMS is a software system which provides for the creation, storage, manipulation and access of models. Model storage functions include model representation, model abstraction, physical model storage and logical model storage. Model manipulation functions include model instantiation, model selection and model synthesis. The MMS model manipulation and model storage functions have been compared to similar DBMS functions [8].

Several designs have been proposed for implementing the model manipulation and model storage components of an MMS $[4,6,9,11,12]$ . The majority of these designs make use of artificial intelligence knowledge representation concepts and techniques for the manipulation and storage of models in the system. Model representations have been proposed that utilize formal logic (predicate calculus, production rules and state-space search techniques), semantic networks, frames and relational data management theory to design an MMS. Table 1 presents an overview of the model management system designs which have been proposed in the literature.

Advantages and disadvantages of the proposed model representations are presented in Table 2.

Review of the advantages and disadvantages of the four model representations suggests that different model representations may be selected for the implementation of an MMS depending on the design objectives of the system and the complexity of the model and decision domains for the system.

A framework for evaluating and selecting a model representation for the design of an MMS, based on the system design objectives and the system domain complexity, has been proposed [2].

As discussed in the introduction to the paper, there are two primary objectives for the design of an MMS. These are: (1) to expand and enhance DSS capabilities by providing a flexible, dynamic modeling component for the system; and (2) to enable organizations to centralize model management functions and insure the integrity, consistency, currency and security of model bases. Two functional classes of MMS have been identified to meet these two system design objectives [2]. These are: (1) Decision Processing MMS and (2) Model Processing MMS.

Decision Processing MMS are MMS that serve the primary function of organizational decision support. These systems function to provide a flexible, dynamic modeling component for a decision support system.

Model Processing MMS are MMS that serve the primary function of the management and control of organizational models in a centralized model base. These systems function to insure the integrity, consistency, currency and security of an organizational model base in a manner similar to a centralized DBMS. Table 3 presents a summary of the recommendations for the selection of a model representation for an MMS based on the system design objective and the complexity of the system domain.

The model manipulation and model storage components of Decision Processing MMS and Model\`Processing MMS can usually be implemented without the use of sophisticated representation schemes if the decision and model domains are narrow and relatively uncomplicated. Model

Table 1. Proposed Model Management System Designs

<table><tr><td>Authors</td><td>Model Manipulating Component</td><td>Model Storage Component</td></tr><tr><td>Bonczek, Holsapple, Whinston [6]</td><td>Formal logic resolution and state-space search, techniques.</td><td>Predicate calculus well-formed functions, clauses and rules of inference</td></tr><tr><td>Elam, Henderson, Miller [9]</td><td>Formal logic resolution and state-space search techniques.Semantic inheritance networks.</td><td>Predicate calculus well-formed functions, clauses, axioms and rules of inference stored as nodes in the semantic inheritance network.</td></tr><tr><td>Dolk, Konsynski [7,8]</td><td>Formal logic resolution and state-space search techniques.Model Frames.</td><td>Predicate calculus well-formed functions, clauses, axioms and rules of inference stored within frames.</td></tr><tr><td>Blanning [3-5]</td><td>Relational model query language (MQL).</td><td>Relational model base.</td></tr></table>

Table 2. Advantages and Disadvantages of Proposed Model Representations for Model Management

<table><tr><td>Framework</td><td>Advantages</td><td>Disadvantages</td></tr><tr><td>Formal Logic Production Rules</td><td>Powerful search and selection functions. Past success in AI problem solving systems.</td><td>Poor for handling large volumes of data/models. Large search space. Loss of concept relations.</td></tr><tr><td>Semantic Inheritance Networks</td><td>Powerful classification and categorization functions. Maintains relations among problem, model and data.</td><td>Lack of direct support for multiple levels of logic. Poor for handling complex model and/or decision domains.</td></tr><tr><td>Frames</td><td>Improved ability to represent a complex decision and/or model domain. Permits multiple representations of model characteristics and logic. Predicate calculus formal logic can be used to store a representation of problem/model characteristics in the frame.</td><td>Frames must be predefined in the context of a problem environment. Constrains the selection of alternative useful solutions not defined at the time of the design.</td></tr><tr><td>Relational</td><td>Improved ability to integrate data and model bases. Excellent management and control functions. Powerful relational query language. Past experience with DBMS systems.</td><td>Less suitable for decision processing. Difficult to adapt a data management technique to storage of models that are inherently more complex, dynamic structures.</td></tr></table>

storage can be implemented using subroutine libraries of algorithmic solution procedures. Decision storage (applicable for Decision Processing MMS) is often unnecessary due to the narrow decision domain. Model and decision manipulation can be implemented using a menu-driven command language. Production rules, embedded within the code, can be used to control the limited decision and model manipulation knowledge necessary within the narrow domain of interest. The Statistical Package for the Social Sciences (SPSS-X) and, in a primitive way, the Interactive Financial Planning System (IFPS) are examples of Decision Processing MMS for narrow decision or model domains.

A frame representation can be useful to organize and classify model solution knowledge for complex models within a narrow decision/model domain. This representation was found to be very useful in the development of the Generalized Experimental Mathematical Programming MMS (GXMP) [17,12].

Table 3. Summary of Model Representations for Model Management System Design

<table><tr><td rowspan="2">System Design Objective</td><td colspan="2">System Domain Complexity</td></tr><tr><td>Narrow decision and model domains</td><td>Complex, broad decision and model domains</td></tr><tr><td>DPMMS Manipulation Component</td><td>Production rules and a menu-driven command language can be used for model manipulation. A frame representation can be used to organize the model relationships for complex model relations.</td><td>A semantic inheritance network, combined with a frame representation, can be used to classify and organize decision and model knowledge to improve model knowledge to improve model manipulation efficiency.</td></tr><tr><td>Storage Component</td><td>Model instances can be stored using subroutine libraries. Storage of decisions is frequently unnecessary due to the narrow decision domain.</td><td>Specific models and decisions can be stored as instances of the frame representation. A relational representation can also be used to store decisions for very complex, broad decision domains if the decision and model relations are loosely coupled.</td></tr><tr><td>MPMMS Manipulation Component</td><td>Model manipulation can be implemented using a menu-driven command language and production rules. The use of a frame representation is usually not indicated since there is less need to specify the decision and model relations.</td><td>A relational query language can be used to implement the model description and model manipulation functions. An example is the Model Query Language (MQL) proposed by Blanning.</td></tr><tr><td>Storage Component</td><td>Models can be stored in subroutine libraries. A sophisticated model representation is usually unnecessary.</td><td>A relational representation can be used to store the models within a centralized model base.</td></tr></table>

DPMMS = DECISION PROCESSING MODEL MANAGEMENT SYSTEM
MPMMS = MODEL PROCESSING MODEL MANAGEMENT SYSTEM

Complex system domains, however, require the use of more sophisticated representations to improve the efficiency and scope of the system. A Decision Processing MMS requires a system design that maintains the relationships among the decision and model attributes. The ability to store decision instances within the system, along with the model instances, allows for the development of a decision and modeling history which provides the necessary structure for system learning based upon past decision solutions.

Review of the advantages and disadvantages of the various representations which have been proposed for MMS design suggests that a combination of a semantic inheritance network and frame representation is an excellent representation for the design of a Decision Processing MMS with a complex decision and model domain. The frame representation is useful to organize and describe the relationship between a specific decision (or class of decisions) and a specific model (or class of models). The ability to store the attributes of the model and decision within the frame structure allows the system to select a model based on a description of the current decision problem by the user. The Plexsys Integrated Development Environment is an excellent example of an MMS intended to function within a complex decision and model domain [13,14]. The design of this system is based on a semantic inheritance network and frame representation.

The semantic inheritance network and frame representations provide two levels of organization and classification within the system. Network nodes (frames) function to organize classes of decisions and models at the abstract level and specific decisions and models at the instantial level. Property and membership links connect the concept nodes (denoting a class) of models and decisions to the specific decision and model solution nodes that describe the model and decision attributes, procedures and assertions. The powerful logic capabilities of first order predicate calculus and production rules can be used within the frame to store the attributes, procedures and assertions. Predicate calculus resolution techniques and production rules can also be used to search the network to find the appropriate class of decisions or models. Similar search strategies can then be used to search the class subnet and to drive the frame logic. Techniques, such as network partitioning into 'net spaces' [10] and network clustering techniques [1], can be employed to improve the efficiency of the network functioning.

An MMS that is intended to provide centralized management of an organizational model base (Model Processing MMS) requires a system design that focuses on maintaining the integrity, consistency, security and currency of the model base. Access to the models should be direct, rapid and flexible. The ability to organize models based upon input and output relationships is a key design feature in this class of MMS.

Review of the advantages and disadvantages of the representations which have been proposed for MMS design suggests that the relational representation is an excellent representation for the design of a Model Processing MMS. The ability to store and access models based upon their input/output characteristics provides for optimum manipulation and control of a large number of models for a variety of organizational uses. The power of the relational algebra query language has been well documented for use in data manipulation. Blanning [3] has identified key factors for manipulation of models using a relational Model Query Language (MQL). Identification of the major processing anomalies which can affect the integrity of the model base and the strategies to avoid these processing anomalies have been proposed. The compatibility of the MMS with the centralized organizational DBMS is also enhanced by this representation. Table 4 presents a summary of the major classes of MMS and systems that are representative of each class.

Table 4. Representative Model Management Systems for Decision and Model Processing

<table><tr><td rowspan="2">Design Objectives</td><td colspan="2">Domain Complexity</td></tr><tr><td>Narrow System Domain</td><td>Complex System Domain</td></tr><tr><td>DSS Support</td><td>SPSS-X Statistical model libraryIFPS (primitive)Financial model library</td><td>PLEXSYS Semantic network and frame representation</td></tr><tr><td>Centralized Model Management</td><td>GXMP Frame model representation</td><td>RELATIONAL MMS Relational model representation</td></tr></table>

## 3. Design of a Decision Processing MMS

The remainder of the paper focuses on the design of a Decision Processing MMS. The reader is referred to the work of Blanning for an excellent discussion of the design of a Model Processing MMS using a relational representation [3,4,5].

There are three major components of the Decision Processing Model Management System. These are (1) a decision component, (2) a model component, and (3) a data component. The Decision Processing Model Management System functions with a Dialogue Management System to implement a generalized DSS architecture. Fig. 1 presents of the generalized DSS architecture.

The decision component of the system provides the user with the ability to describe, analyze and store organizational decisions. This component is similar to the Problem Processing System described by Bonczek, Holsapple and Whinston in their work on a Generalized Decision Support System [6].

The decision component accesses the model component to retrieve, sequence and control the organizational models needed for solving a specific decision problem. The model component accesses the data component to retrieve, sequence and control the organizational data needed for implementing a specific model. The decision component checks the consistency, integrity and completeness of the model base and data base for solving a specific decision problem and queries the user through the Dialogue Management System if the data or models needed to solve a given decision problem are inconsistent or incomplete. The user may interactively input data that is not stored in the system. In addition, the user may directly access the model base or data base for model or data management and analysis that is not specifically related to a given decision problem.

![](/api/attachments/STRFU8HD/fulltext/images/88bf4ad546ebff95b10ad2a074bf1427e7427923c3a1e185ce63a18f0d912bff.jpg)  
Fig. 1. Generalized DSS architecture.

The decision component is comprised of a decision manipulation component and a decision storage component. Fig. 2 presents an overview of the decision component of the Decision Processing Model Management System.

The decision manipulation component is composed of a decision net that functions as a decision classification system and allows for the update, storage and retrieval of decision problems. The semantic inheritance decision net links the decision frames that describe the decision attributes and decision solution rules for a given class of decisions. Model selection and sequencing rules are also implemented in the decision manipulation component. Models required for a given decision but not available in the system can be supplied interactively by the user through the Dialogue Management System.

The decision storage component is composed of decision instances that provide a decision history for the organization and the ability of the system to learn from past decisions. Decision integrity, consistency, security and completeness rules are also implemented within this component of the system.

The model component of the Decision Processing MMS is comprised of a model manipulation component and a model storage component. Fig. 3 presents an overview of the model component of the Decision Processing Model Management System.

The model manipulation component is composed of a model net that functions as a model classification system and allows for the update, storage and retrieval of models. The semantic inheritance model net links the model frames that

![](/api/attachments/STRFU8HD/fulltext/images/22e82ba4405190043daf6457f29f361f9c5e33bf6569ac9069d23653eff6dde3.jpg)  
Fig. 2. Decision component of a decision processing model management system.  
Fig. 3. Model component of a decision processing model management system.

described the model attributes and model solution rules for a given class of models (e.g., statistical analysis, financial, strategic planning) and for specific models within each class (e.g., stepwise regression, ROI, critical success factors). Data selection and sequencing rules are also stored within the Model Manipulation Component. Data required for a given decision but not available in the system can be supplied interactively by the user through the Dialogue Management System.

The model storage component is composed of model instances that provide the decision maker with a modeling history for the organization. The ability to store the history of organizational model utilization allows the system to learn from past model use. Model integrity, consistency, security and completeness rules are also contained in the model storage component of the system.

![](/api/attachments/STRFU8HD/fulltext/images/33c30e87cb0a9fb3e517d8cf4a25a9d460fcbe92a7a6f57837aae9bb0d4134e5.jpg)  
Fig. 4. Strategic planning process model.

![](/api/attachments/STRFU8HD/fulltext/images/3a84eec2f924cb91feb2a721a2725c36de6e2da419cc5204fe144bb0c46847b4.jpg)  
Fig. 5. Models for strategic planning.

4. Design of a Strategic Planning Model Management System

A Strategic Planning MMS has been implemented at the University of Arizona. Analysis of strategic planning activities and organizational strategic planning information needs was performed at a Tucson business using an action research methodology [21]. Three categories of strategic planning activities were identified for the study organization.

(1) Organizational Performance Activities
○ Organizational Performance Studies
○ Specific Product/Service/Strategic Business Unit Studies

(2) Expansion of Existing Services Analysis
○ Specific Product/Service/Strategic Business Unit Studies
○ Pilot/Feasibility Studies

(3) New Venture Analysis
○ Pilot/Feasibility Studies
○ Business Plan Development

A model of the strategic planning process was developed based upon the planning and decision process models of Simon [19], Mason and Mitroff [16] and Volkema [22] Fig. 4 presents the model of the strategic planning process that was used for the design of the Strategic Planning MMS.

Three phases have been identified in the strategic planning process. These are: (1) Formulation, (2) Solution/Action Modeling, and (3) Implementation.

The first phase, Formulation, is concerned with the process of discovering that a threat or opportunity exists within the environment and analyzing the threat or opportunity. This activity has been described as problem sensing [16], problem finding [17] and perception [14]. These activities help to formulate the problem or opportunity, defining the boundaries of the situation so that formal models may be developed and tested. The output of this phase is the strategic posture (e.g., competitive, defensive).

The second phase of the strategic planning process, Solution/Action Modeling, is concerned with the generation of solutions and actions that can be used to solve the problem or implement a new venture. Formal modeling of the problem and solutions is performed during this stage of the process [16]. These solutions and actions are evaluated and a single solution or set of solutions is chosen for implementation.

The final phase of the strategic planning process, Implementation, is concerned with the implementation of a plan for carrying out the chosen solution(s). Measurement, monitoring and evaluation of the changes in the organizational structure continue throughout the implementation process and provide feedback to the system as part of the internal and external environmental scanning activities.

![](/api/attachments/STRFU8HD/fulltext/images/bf0cf7e3f73f5a87d5bb7e7722c5a2389e6d544dd809aa32b0202cc6f4fd2dee.jpg)  
Fig. 6. Manipulation component - strategic planning model management system.

Strategic Planning Models Frame

<table><tr><td colspan="12">Strategic Planning ProcessModels Frame</td></tr><tr><td rowspan="4"></td><td colspan="2">FormulationModels Frame</td><td colspan="3">Solution/ActionModels Frame</td><td colspan="2">ImplementationModels Frame</td><td>DescriptiveStatisticsModelsFrame</td><td>RegressionDiagnosticsModelsFrame</td><td>RegressionAnalysisModelsFrame</td><td>CorrelationAnalysisModelsFrame</td></tr><tr><td>DiscoveryModelsFrame</td><td>ExplorationModelsFrame</td><td>GenerationModelsFrame</td><td>EvaluationModelsFrame</td><td>SelectionModelsFrame</td><td>ImplementationModelsFrame</td><td>MeasurementModelsFrame</td><td>SpecificModelSolutionFrame</td><td>SpecificModelSolutionFrame</td><td>SpecificModelSolutionFrame</td><td>SpecificModelSolutionFrame</td></tr><tr><td>SpecificModelSolutionFrame</td><td>SpecificModelSolutionFrame</td><td>SpecificModelSolutionFrame</td><td>SpecificModelSolutionFrame</td><td>SpecificModelSolutionFrame</td><td>SpecificModelSolutionFrame</td><td>SpecificModelSolutionFrame</td><td>SpecificModelSolutionFrame</td><td>SpecificModelSolutionFrame</td><td>SpecificModelSolutionFrame</td><td>SpecificModelSolutionFrame</td></tr><tr><td>SpecificModelSolutionFrame</td><td>SpecificModelSolutionFrame</td><td>SpecificModelSolutionFrame</td><td>SpecificModelSolutionFrame</td><td>SpecificModelSolutionFrame</td><td>SpecificModelSolutionFrame</td><td>SpecificModelSolutionFrame</td><td></td><td></td><td></td><td></td></tr></table>

Fig. 7. Model manipulation component – strategic planning model management. Note: This is only a partial semantic inheritance network/frame representation of the modeling knowledge stored within the system. Other classes of models (e.g. financial models, accounting models, mathematical programming models) are implemented in a similar manner.

Specific strategic planning models used to support the various phases of the strategic planning process were identified for use within the system. Fig. 5 presents the strategic planning models identified for use in each phase of the strategic planning process.

Design of the decision component of the system involved the design of the decision manipulation component (decision net and decision frames) and the decision storage component of the system (decision instances). The decision manipulation component of the Strategic Planning MMS is presented in Fig. 6. It is important to note that the network representation presented above expresses the decision relationships for a specific strategic planning decision domain. It is not intended to represent the decision domain for all Strategic Planning MMS.

The semantic inheritance decision network functions to organize and classify the diverse strategic planning decision frames. The network is defined on four levels. At the first two levels of the network, the frames contain the system control rules for describing the current strategic planning decision and for selecting a class of strategic planning analysis methods. At the third level of the network, the frames contain the system control rules for selecting the specific studies needed for the class of strategic planning analysis and the model classes that will be needed to implement the study. At the fourth level of the network, the frames contain the system control rules for solving the specific decision problem. This includes the rules for selecting and sequencing the specific models needed for the analysis. Network maintenance rules for update, storage and retrieval of the decision problems are present at each level of the network.

The decision history of the organization is stored in the decision storage component of the system. Decision instances are stored as specific implementations of the decision solution frames. The decision storage component also contains the integrity, consistency, security and completeness rules for the decision base.

The strategic planning decision component links to the strategic planning model component through the decision manipulation component and the model manipulation component (see Fig. 7).

The semantic inheritance model network functions to organize and classify the strategic planning model frames. These models are classified according to their role within the strategic planning process and their functional analytic class. This provides access to the models for analysis of a specific phase of the strategic planning process (e.g., alternative generation) and also allows for direct access of the models for functional data analysis (e.g., regression analysis).

The modeling history of the organization is stored in the model storage component of the system. Model instances are stored as specific implementations of the model solution frames. Model integrity, consistency, security and completeness rules are also implemented in the model storage component of the system. Dolk and Konsynski [7] present an example of the implementation of a model solution frame.

## 5. Conclusion

The implementation of MMS provides organizations with the capability for accurate, flexible and responsive modeling. This paper described a framework that can be used to assist system developers in the choice of an internal representation for an MMS based on the system objectives and complexity of the system domain. The framework distinguishes between an MMS that is primarily used to provide support for organizational decision making (a decision processing MMS) and an MMS that is primarily used to provide centralized management of organizational models (a model processing MMS). The use of the framework for the design of a strategic planning MMS, implemented at the University of Arizona, was presented to illustrate the important features of the system architecture of a decision processing MMS.

## References

[1] H. Alshawi, A Clustering Technique for Semantic Network Processing, Conference Proceedings: European Conference on Artificial Intelligence (1982).

[2] L. Applegate, G. Klein, B. Konsynski and J. Nunamaker, Model Management Systems: Proposed Model Representations and Future Designs, Proceedings of the Sixth International Conference on Information Systems (Dec. 1985).

[3] R. Blanning, A Relational Framework for Model Management In Decision Support Systems, DSS-82 Transactions (1982).

[4] R. Blanning, The Existence and Uniqueness of Joins in Relational Model Banks, Owen Graduate School of Management, Vanderbilt University (1982).

[5] R. Blanning, Issues in the Design of Relational Model Management Systems, National Computer Conference (1983).

[6] R.H. Bonczek, C.W. Holsapple, A.B. Whinston, A Generalized Decision Support System Using Predicate Calculus and Network Data Base Management, Operations Research, 29(2): 263–281 (1981).

[7] D. Dolk and B. Konsynski, Knowledge Representations for Mode! Management Systems, IEEE Transactions on Software Engineering, Vol. 10(6): 619–628 (Nov. 1984).

[8] D. Dolk and B. Konsynski, Model Management in Organizations, Management and Information (Fall 1985).

[9] J.J. Elam, J.C. Henderson and L.W. Miller, Model Management Systems: An Approach to Decision Support in Complex Organizations, Proceedings of the First Conference on Information Systems (1980).

[10] G.G. Hendrix, Expanding the Utility of Semantic Networks Through Partitioning, 4th International Joint Conference on Artificial Intelligence (1975).

[11] B. Konsynski, Model Management in Decision Support Systems, Data Base Management: Theory and Applications, (eds) Holsapple, C.W. and Whinston, A.B., Boston: D. Reidel Publ. Co., (1983).

[12] B. Konsynski and D. Dolk, Knowledge Abstractions in Model Management, DSS-82, (1982).

[13] B. Konsynski, J. Kottemann, J. Nunamaker, and J.W. Stott, Plexsys-84: An Integrated Development Environment for Information Systems, Journal of Management Information Systems I(3): 64–104, (Winter 1984).

[14] J. Kotteman and B. Konsynski, Information Systems Planning and Development: Strategic Postures and Methodologies, Journal of Management Information Systems, 1(2): 45–63, (1984).

[15] J. Kotteman and B. Konsynski, Dynamic Metasystems for Information Systems Development, Proceedings of the Fifth International Conference on Information Systems, (Nov. 1985).

[16] R. Mason and I. Mitroff, Challenging Strategic Planning Assumptions, NY: John Wiley and Sons, 1981.

[17] W.F. Pounds, The Process of Problem Finding, International Management Review, (Fall 1969).

[18] M. Scott Morton, Management Decision Systems, Boston: Harvard University Graduate School of Business Administration, (1971).

[19] H. Simon, The New Science of Management Decisions, New York, Harper and Rowe, (1960).

[20] R. Sprague and E. Carlson, Building Effective Decision Support Systems, NJ: Prentice-Hall Inc. (1982).

[21] T.I. Susman and R.D. Evered, An Assessment of the Scientific Merits of Action Research, Administrative Science Quarterly (Dec. 1978) 582–603.

[22] R. Volkema, Problem Formulation in Planning and Design, Management Science, 29(6): 639–652 (June 1983).
