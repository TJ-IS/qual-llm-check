---
otero_id: 16919
otero_key: "YR5YR39D"
title: "An entity-relationship approach to model management"
authors: "Robert W Blanning"
year: "1986"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(86)90122-3"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An Entity-Relationship Approach to Model Management

Robert W. BLANNING

Owen Graduate School of Management, Vanderbilt University, Nashville, TN 37203, U.S.A.

An important purpose of the research being done on decision support systems is to develop a theory of information management that is as independent as possible of the way in which the information is stored and processed. This has important consequences for any proposed theory of model management, for it suggests that a theory of model management should not only help a manager or analyst to organize and access model banks, but it should do so in a way that allows models and stored data to be viewed as complementary sources of information. We present herein an extension of the entity-relationship framework for database organization and processing to include the organization and processing of model banks.

Keywords: Entity; Relationship; Model Bank; Partially-Ordered Set; Fixed Point; Entity-Relationship Diagram

![](/api/attachments/YR5YR39D/fulltext/images/bdc6dfc962b7ec3dfab697a7fd70ebcf03555b7cd7dfa99ff7308840f904b724.jpg)

Robert W. Blanning is Associate Professor of Management (Information Systems) at the Owen Graduate School of Management at Vanderbilt University. His teaching and research interests are in information economics, model management, and intelligent decision support systems, and he has published on these topics in Management Science, Decision Sciences, Communications of the ACM, Naval Research Logistics Quarterly, Omega, Information & Management, Technologi cal Forecasting and Social Change, Long Range Planning, Simulation, and Human Systems Management.

## 1. Introduction

An important purpose of the research being done on decision support systems (DSS) is to develop a theory of information management that is as independent as possible of the way in which the information is stored and processed [9]. Much of the literature on model management has contributed to this objective by presenting frameworks for model management that are similar to some of the established frameworks for data management, which suggests that a synthesis of these two areas might be possible. For example, the early literature on model management points out similarities between stored data and decision models as sources of management information [24,21] and more recent work has identified the need for DSS generators that perform both modeling and data retrieval and analysis functions [19,20,23]. In addition, frameworks for model management, similar to the CODASYL DBTG framework for data management, have been developed [17,22], and a relational framework for model management, which is similar to the existing relational framework for data management, has been developed in detail [3,10].

In this paper we carry this process one step further by presenting an entity-relationship (ER) framework for model management. This framework is based on the established ER model of data that attempts to generalize the network-based data models (i.e., the hierarchical and CODASYL DBTG models) and the relational model [14,13,16]. The purpose of the ER data model is to provide an enterprise view of data that is independent of storage and processing methods. We will present an ER-based enterprise view of decision models and show how it can be integrated with the ER-based view of data to produce a single framework for data and model management.

We begin in the following section by examining the enterprise view of decision models - a relational view that is independent of physical storage structure and processing procedures. In Section 3 we present an ER framework for model banks, which is then combined with the ER framework for data bases in Section 4. In the concluding section we examine promising areas for further research.

## 2. The Enterprise View of Decision Models

The relational review of decision models, like the relational view of stored data, is a logical view of information that insulates the users of the information from the physical aspects of information storage and processing. A model is viewed as a virtual relation – that is, as a subset of the Cartesian product of a set of domains corresponding to input and output attributes – just as a file in relational database theory is viewed as a stored subset of the Cartesian product of a set of domains corresponding to key and content attributes.

There are three principal areas of research in relational model management, and these are similar to much of the research being done in relational database theory. The first concerns the organization of model banks. There are normal forms for model banks that are similar, but not identical, to the normal forms of relational data management [7]. The differences result from the fact that the tuples in a model relation do not exist in stored form and are not individually updated; therefore, storage anomalies do not exist and cannot be eliminated by projection into a normal form. However, there are anomalies, called processing anomalies, that affect the organization of a model bank, and they lead to a sequence of normal forms not unlike those relevant to stored data. For example, transitive dependencies in a relation (i.e., functional dependencies affecting only the output attributes) lead to processing anomalies in model management, just as they lead to storage anomalies in data management, and they can be eliminated by projection into an appropriate normal form.

The second topic is the relational completeness of model bank query languages. There are three operations that make up the criteria for relational completeness in model management. The first is execution, which corresponds to selection and projection in relational data management. The second is optimization of a single output attribute over one or more input attributes. The third is sensitivity analysis - determining the rate of change of an output attribute with respect to an input attribute. It has been shown that the first order predicate calculus is relationally complete for model management and that these operations can be described by languages similar to SQL and Query-by-Example [6,8].

It is also possible, within limits, to combine these operations with each other and with themselves. An examples the compound operation of imbedded optimization, in which one optimization is performed in anticipation of another optimization. Consider a model with two inputs, a sale price for the product produced by the company being modeled and the unit cost of raw materials used in the production of the product. Let the outputs of the model be total raw material expense and net income (i.e., revenues net of raw material and any other expenses). An example of optimization is the calculation of a sale price that will maximize net income for a given raw material price. An example of imbedded optimization is the calculation of a raw material price that will maximize raw material expense given that the sale price will then be set to maximize net income. This operation might be performed by the supplier of raw materials who wishes to select the raw material price that will maximize his revenues (and hence, his customer's raw material expense), knowing that his customer will set the sale price for his product to maximize net income at that raw material price.

Imbedded optimization is of interest because of its self-referential property. In this respect it is similar to an operation that serves as an unofficial test query in relational database theory. The query is Find all employees who earn more than their supervisors, applied to a file containing three fields: employee identifier, the identifier of the employee's supervisor, and the employee's salary. Imbedded optimization may serve a similar function in evaluating query languages for model management systems.

We note that imbedded optimization is an example of a relational mapping. That is, the maximization of net income over the sale price for each raw material price produces as its output a virtual relation specifying the optimal sale price for each raw material price. This is then used in the second operation, the maximization of expense over raw material price. We point out below that relational mappings are not needed in model management to implement joins, because joins are transparent to the user (there are no lossy joins). However, relational mappings are useful in implementing compound operations such as imbedded optimization.

The third topic is the implementation of joins in model banks. It has been shown that the lossy join problem does not arise in model management [5]. The reason is that the sets of output attributes of the models in a model bank are pairwise disjoint – that is, if one model calculates a quantity (such as net income), then that quality cannot be calculated by any other model (i.e., there can be only one net income). From this premise, it can be shown that lossy joins do not occur. In addition, the existence and uniqueness of joins in model banks have been investigated, although much work needs to be done in this area [4].

Thus, the relational framework for model management provides a view of decision models that is independent of storage and processing considerations. We will now extend this theory to include an ER framework for model management and then show how it can be integrated with the existing ER framework for data management.

## 3. An Entity-Relationship Approach to Model Bank Organization

Four important concepts in the ER model of data are (1) entity set, (2) relationship set, (3) attribute, and (4) value set. An entity set is a collection of real-world objects or activities that generally correspond to a file (relation). For example, in Fig. 1 there are three entity sets: STUDENT, COURSE, and PARTICIPATION (i.e., the act of student participation in a course). Each of these entity sets has attributes (which are realized as fields in a file) and value sets (which correspond to domains in relational database theory). In Fig. 1 the attributes are student number, course number, data about students and courses, and grades. The relationship set, represented by a diamond, exists because there is information common to students and courses (i.e., grades). The diagram in Fig. 1 is called an Entity-Relationship Diagram (ERD). We note that this ERD would be represented in a CODASYL DBTG framework by a confluent hierarchy (i.e., two sets with different owners but a common member) and in the relational framework by three separate flat files (normalized relations) with appropriate commonality among their key attributes. Thus, the ER approach combines the simplicity of the relational framework with the graphical character of the CODASYL DBTG set structure.

We now ask whether this approach might be applied to model management and if so, in what way it might have to be modified. The principal modification is conceptual – in model management an entity set corresponds not to a set of entities in the real world, but rather to a single entity. For example, a model of a factory corresponds to a single entity – the factory. The tuples in the virtual relation that provides the relational view of the model do not correspond to separate real-world entities; instead they describe a causal relationship between certain attributes of the factory (e.g., production level and production cost). This explains why sensitivity analysis is widely used in model management but is hardly ever found in data management. For example, one does not use a payroll file to determine the sensitivity of salary to social security number, but one might use a model to calculate the sensitivity of production cost to production level (i.e., the marginal cost of production). In data management, on the other hand, there is an entity in the real world corresponding to each tuple in the relation (e.g., a person receiving a salary). Changing a person's social security number does not change the person, and hence, does not change his salary; and sensitivity analysis is of no use in this case [11].

![](/api/attachments/YR5YR39D/fulltext/images/51840832264db236df953738e0810c82567d366ec11eafc1dbb955a75f0e72f9.jpg)  
Fig. 1. An ERD for a Confluent Hierarchy

Another difference between the ER approaches to data and to models is illustrated in Fig. 2, in which there are three entities. The model corresponding to the MARKET entity calculates volume sold as a function of price charged. The model corresponding to the FACTORY entity calculates production expense as a function of volume sold, and the model corresponding to the FINANCIAL STRUCTURE entity calculates net income as a function of price, volume, and expense. We note that the two relationship sets denote interfaces between the models corresponding to the entities. The upper relationship set corresponds to the relationship between the MARKET and FACTORY models (i.e., that the output of the former is the input to the latter), and the lower one denotes the fact that the inputs and outputs of the MARKET and FACTORY models are inputs to the FINANCIAL STRUCTURE model.

There is one complication that arises in the ER approach to model management that is not found in data management. This occurs whenever the models in the model bank, ordered by their input and output attributes, do not form a partially ordered set – that is, when there are cycles in the set. In this case there is a simultaneity relationship between two or more of the models in the set, and a consistent set of input and output attributes cannot be obtained by recursive execution of the models in the model bank. This is illustrated in Fig. 3. The model bank illustrated here is the same as that illustrated in Fig. 2, with one exception. A new entity (and hence a new model), representing the company's pricing policy, has been added (e.g., price may be a mark-up of unit expense). In this case the (single) relationship set represents both the simultaneous relationship involving the FACTORY, MARKET, and PRICING POLICY entities and also the sequential relationship between them and the FINANCIAL STRUCTURE entity. Methods for resolving the simultaneity problem, which require the identification of a fixed point for one or more attributes in the model bank (in this case, either the price or the volume), are discussed in [4,5]. For example, if simultaneity is to be resolved by finding a fixed point for the price, then the following algorithm would be used:

![](/api/attachments/YR5YR39D/fulltext/images/40d73c5312144c6f771d607601409638ff0834751bdc0a2f6c7cdbfda65e3589.jpg)  
Fig. 2. An ERD for an Acyclic Model Bank

Financial Structure  
![](/api/attachments/YR5YR39D/fulltext/images/2573e57ea8f30f7f8d0e6d97d03c32513b1b905a3140c2da524e7b6e7fa8f47c.jpg)  
Fig. 3. An ERD for a Cyclic Model Bank

(1) Posit a price

(2) Enter the price into MARKET to calculate volume

(3) Enter the volume into FACTORY to calculate expense

(4) Enter the volume and expense into PRICING POLICY to calculate price

(5) If the price calculated by PRICING POLICY in Step 4 is sufficiently close to the price entered into MARKET in Step 2, then go to Step 6. Otherwise, posit a new price (e.g., by splitting the difference between the two prices) and to Step 2.

(6) Enter the price, volume, and expense into

FINANCIAL STRUCTURE to calculate net income.

Thus, when the model bank is cyclic (i.e., contains one or more cycles), it is necessary to find a fixed point for one or more of the attributes. As a result, the relationship sets involving these attributes correspond not only to a physical medium of communication between the mdoels, but also to the implementation of one or more fixed point algorithms.

## 4. An Entity-Relationship Approach to Data and Model Integration

We now consider a data/model bank in which entity sets correspond to collection of entities in the real world about which data are stored, entities correspond to physical objects or processes for which models have been constructed, and relationship sets represent relationships of the type described in Section 3. We expect the following conditions to obtain in a data/model bank:

(1) All relations will be in third normal form. That is, there should be no functional dependencies among the content attributes in files corresponding to entity sets, nor among the output attributes in models corresponding to entities.

(2) The output attributes in models corresponding to entities will be pairwise disjoint.

(3) Relationship sets may correspond to any of the following:

(a) The relationships between the entities in two or more entity sets (e.g., a student may take a course)

(b) The interfaces between models corresponding to two or more entities (i.e., the output of a model may be the input to another model)

(c) The interfaces between one or more files corresponding to entity sets and one or models corresponding to entities (i.e., data from the files may be inputs to the models or the outputs of the models may be written to the files)

(d) A fixed point algorithm needed to find a consistent set of attribute values for two or more models that do not form a partially ordered set

An example of a data/model bank appears in Fig. 4. This is a simplified ERD of a mathematical programming system that contains data files, interface files, data manipulation procedures, and model solution techniques [18]. In this ERD the stored data are found in files corresponding to three entity sets - BASECASE, CHANGES, and SIDECASE. These files contain data tables describing the process (i.e., the operations of a refinery, transportation network, etc.) being optimized. The relationship set R1 represents the interface between these entity sets and the MATRIX GENERATOR, which transforms the data tables into a mathematical programming matrix. The output of the matrix generator is written to a MATRIX FILE, which is operated on by the MATHEMATICAL PROGRAMMING ALGORITHM to produce the optimal tableau in the OUTPUT FILE, which is then read by the REPORT WRITER. The interfaces between these matrix-oriented entities and entity sets is represented by the relationship set R2. Finally, the relationship set R3 denotes the interface between the REPORT WRITER and the REPORT, which is the output of the system.

![](/api/attachments/YR5YR39D/fulltext/images/0150bda2cab8189601d25479f68a72fbc5372f13077f17be3f0da56c16af80b2.jpg)  
Fig. 4. An ERD for a Data/Model Bank

There are many other types of data/model banks. For example, files containing operating data may provide inputs to statistical analysis packages, the outputs of which may be accessed by Monte Carlo simulations. In addition, some planning models transform a portion of a company's data base into a pro-forma data base, which is accessed by a report writer to produce pro-forma reports. (For specific examples, see Ref. 12.) In each case an ER approach may help to describe the entities being modeled, the entity sets about which information is recorded, and the relationships between them.

## 5. Conclusion

We have seen that the ER approach to data base design can be enlarged to encompass the design of model banks. However, there are several questions yet to be answered, and these questions suggest topics for further research. We conclude by examining briefly five such topics.

The first is the translation of general data/model bank descriptions into ERDs. Chen [14,13] discusses the translation of data structure diagrams into ERDs, and Chung, Nakamura and Chen [15] discuss the translation of ERDs into relational schemes. However, something more general will be needed when models are present, because relationship sets perform functions in model management that are not needed in data management.

The second topic is the development of normal forms for data/model banks. Normal forms have been developed for relational model banks [7], and normal forms for ER data bases have also been developed [15]. An integration of these two approaches will be necessary. This may be as simple as a proscription concerning transitive dependencies, as is suggested above, or it may be more complex.

The third topic is the relational completeness of ER data/model query languages. Criteria for relational completeness of model query languages have been developed [6,8] and were discussed briefly in Section 2. In addition, criteria for relational completeness of ER database query languages have been developed [1]. A synthesis of these approaches may result in the specifications of a general linguistic structure for data/model banks.

The fourth topic is the incorporation of integrity constraints into an ER data/model framework. The incorporation of integrity constraints into the ER data framework is discussed by Chen [14], and similar constraints (e.g., that a price must be positive) may be applied to models as well.

The fifth topic is the possible existence of null attribute values, which will occur if an attribute value is unknown or does not exist. In some cases these may be represented as integrity constraints; for example, if the volume is unknown whenever the price falls below a certain value, then the price could be constrained to be at or above that value. In other cases it may not be known whether a null value will exist until the model is executed and an anomaly (e.g., an attempt to divide by zero or to take the square root of a negative number) is encountered. The existence of null values has been investigated for data relations (see for example, Ref. 2), and similar investigations will probably take place with regard to ER data/model banks.

Although it is possible to extend the ER framework to include decision models as well as stored data, whether this will be useful in the design, evaluation, documentation, and operation of DSS is not yet clear. But it is clear that a unifying framework is needed for the organization of the variety of information sources used for decision support. The ER approach appears promising as a theoretical framework, a practical tool, and a stimulus for further research into the integration of stored data and decision models in DSS.

## Acknowledgment

This research was funded by the Dean's Fund for Faculty Research of the Owen Graduate School of Management of Vanderbilt University.

## References

[1] P. Atzeni and P.P. Chen, Completeness of Query Languages for the Entity-Relationship Model, in Entity-Relationship Approach to Information Modeling and Analysis, P. Chen, (ed.), North-Holland, Amsterdam (1983) pp. 109–121.

[2] J. Biskup, A Formal Approach to Null Values in Relational Databases, in Advances in Data Base Theory, Vol. 1, H. Gaillaire, J. Minker, and J.M. Nicholas, (eds.), Plenum Press, New York (1981) pp. 299–341.

[3] R.W. Blanning, A Relational Theory of Model Management, to be presented at the NATO ASI program on Decision Support Systems in Maratea, Italy (June 1985).

[4] R.W. Blanning, The Existence and Uniqueness of Joins in Relational Model Banks, International Journal on Policy and Information, Vol. 9, No. 1, (June 1985) pp. 73–95.

[5] R.W. Blanning, A Relational Framework for Join Implementation in Model Management Systems, Decision Support Systems, Vol 1, No. 1 (Jan. 1985), pp. 69–81.

[6] R.W. Blanning, Language Design for Relational Model Management, in Management and Office Information Systems, S.K. Chang, (ed.), Plenum Press, New York (1984) pp. 217–235.

[7] R.W. Blanning, A Relational Framework for Model Bank Organization, Proceedings of the IEEE Workshop on Languages for Automation, (Nov. 1984) pp. 148–154.

[8] R.W. Blanning, TQL: A Model Query Language Based on the Domain Relational Calculus, Proceedings of the IEEE Workshop on Languages for Automation (Nov. 1983) pp. 141–146.

[9] R.W. Blanning, What is Happening in DSS? Interfaces, Vol. 13, No. 5 (Oct. 1983) pp. 71–80.

[10] R.W. Blanning, Issues in the Design of Relational Model Management Systems, Proceedings of the National Computer Conference (June 1983) pp. 395–401.

[11] R.W. Blanning, Data Management and Model Manage-

ment: A Relational Synthesis, Proceedings of the ACM Twentieth Annual Southeast Regional Conference (April 1982) pp. 139–147.

[12] R.W. Blanning, Model-based and Data-based Planning Systems, Omega, 9, No. 2 (Feb. 1981) pp. 163–168.

[13] P.P. Chen, The Entity-Relationship Model - A Basis for the Enterprise View of Data, Proceedings of the National Computer Conference (1977) pp. 77-84.

[14] P.P. Chen, The Entity-Relationship Model - Toward a Unified View of Data, ACM Transactions on Data Base Systems, Vol. 1, No. 1 (March 1976) pp. 9-36.

[15] I. Chung, F. Nakamura and P.P. Chen, A Decomposition of Relations Using the Entity-Relationship Approach, in Entity-Relationship Approach to Information Modeling and Analysis, ed. by Peter P. Chen, North-Holland, Amsterdam (1983) pp. 149–171.

[16] M. Flavin, Fundamental Concepts of Information Modeling, Yourden Press, New York (1981).

[17] B.R. Konsynski, On the Structure of a Generalized Model Management System, Proceedings of the Fourteenth Hawaii International Conference on System Sciences, Vol. 1 (Jan. 1980) pp. 630–638.

[18] K.H. Palmer, N.K. Boudwin, H.A. Patton, A.J. Rowland,

J.D. Sammes and D.M. Smith, A Model-Management Framework for Mathematical Programming, Wiley, New York (1984).

[19] R.H. Sprague, Jr., A Framework for the Development of Decision Support Systems, MIS Quarterly, Vol. 4, No. 4 (Dec. 1980) pp. 1–26.

[20] R.H. Sprague, Jr. and E.D. Carlson, Building Effective Decision Support Systems, Prentice-Hall, Englewood Cliffs, 1982.

[21] R.H. Sprague, Jr. and H.J. Watson, Model Management in MIS, Proceedings of the Seventeenth National AIDS (Nov. 1975) pp. 213–215.

[22] E.A. Stohr, and M. Tanniru, A Database for Operations Research Models, International Journal of Policy Analysis and Information Systems, Vol. 4, No. 1 (1980) pp. 105–121.

[23] M.S. Wang and J.F. Courtney Jr., Design and Implementation of the MAGIC/ROC Decision Support System Generator, DSS-82 Transactions (June 1982) pp. 37–49.

[24] H.J. Will, Model Management Systems, in Information Systems and Organization Structure, E. Grochla and N. Szyperski (eds.), Walter de Gruyter, Berlin (1975) pp. 468–482.
