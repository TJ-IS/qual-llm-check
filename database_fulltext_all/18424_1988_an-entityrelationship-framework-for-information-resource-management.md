---
otero_id: 18424
otero_key: "XV2XD2MZ"
title: "An entity—relationship framework for information resource management"
authors: "Robert W. Blanning"
year: "1988"
journal: "Information & Management"
doi: "10.1016/0378-7206(88)90042-0"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# An Entity-Relationship Framework for Information Resource Management \*

Robert W. Blanning

Owen Graduate School of Management, Vanderbilt University, Nashville, Tennessee 37202, USA

We outline a framework for information resource management based on the relational and entity–relationship models of data base management. They are enlarged to encompass the variety of information resources now found in many organizations – including data files, data analysis procedures, text files, decision models, expert systems and knowledge bases, and human information resources (both individuals and groups).

Keywords: Stored relations, Virtual relations, data bases, Model banks, Knowledge bases, Human information resources, Unnormalized relations.

## 1. Introduction

In order to accomplish their objectives, organizations must acquire, maintain, and make productive use of many different types of resources, such as cash, inventories, fixed assets, human resources, etc. The acquisition, maintenance, and productive application of these resources is often called resource management. Specialists in the management of various types of resources frequently attempts to develop theories that explain how they might effectively be managed and disciplines that guide managers in their management; they then use these theories and disciplines to construct formal information systems that assist in the

![](/api/attachments/XV2XD2MZ/fulltext/images/2ac3a17044926d8314ede316e96bc2bc134daf79f3004c4257c30562597a8cbf.jpg)

Robert W. Blanning is Associate Professor of Management at the Owen Graduate School of Management at Vanderbilt University. He has a B.S. in Physics from the Pennsylvania State University, an M.S. in Operations Research from the Case Institute of Technology, and a Ph.D. from the University of Pennsylvania, specializing in operations research and management information systems. He has been a member of the faculties of the Schools of Business at New York Uni management of the resources. Thus, we have theories and disciplines for portfolio management, cash management, and human resources management, along with portfolio management systems, cash management systems, and human resources management systems. We will call the basic structure underlying the theory, discipline, and system for the management of a resource a framework for resource management.

Many organizations have begun to recognize that information is a valuable resource; this has led to an increasing interest in the development of a comprehensive framework for information resource management [14,22]. One factor that has inhibited the formation of such a framework is the wide variety of information resources found in modern organizations. These resources include data files, data analysis procedures, text files, decision models, expert systems and knowledge bases, and human information resources (such as committees, departments, and divisions). Of course, a framework for information resource management (IRM) need not describe all aspects of these resources, but it should describe their salient characteristics and the important interactions between them.

A promising candidate for such a framework is one based on the concept of a relation. A relational model has been developed for data base management, and it appears promising for other types of information management as well. A semantic extension of this and the network model, the entity–relationship model, has also gained wide acceptance. We examine the development of a relational and entity–relationship framework that includes the many information resources available to support management decision making.

## 2. A Relational View of Information Resources

We first present a relational view of six information resources: (formatted) data files, data analysis procedures, (unformatted) text files, (causal) decision models, expert systems and knowledge bases, and human information resources (to include individuals and groups).

The relational model of data has been and continuous to be thoroughly investigated [16,24]. A data base is viewed as a system of relations, each of which is a subset of the Cartesian product of a set of domains corresponding to the key and content attributes of a file, where the content is functionally dependent on the key. The principal issues of interest are: (1) the allocation of attributes to relations in a way that will not lead to anomalies in data storage, (2) the properties of relationally complete database query languages, and (3) the integration of files, which is accomplished by performing joins across relations.

A relational view of data analysis procedures has not been investigated in the literature and is presented here for the first time. The input to a data analysis procedure (e.g., a regression package) is a data file and a set of instructions (e.g., identification of the dependent variable), and the output is a set of parameter estimates. The relational view of data analysis procedures differs from that of stored data in two important respects. First, a procedure is a virtual relation, not a stored relation. Second, since the domain identifying the input file is non-atomic, the relation is unnormalized. These characteristics will appear in some of the other information resources described below, and they differentiate the framework presented here from the established entity–relationship data model.

The relational view of text files has been investigated briefly [17]. Since text is sequential and relations are (unordered) sets, the relational representation of text consists of words (which are unformatted sequences of characters) and a sequence number denoting the position of the word. The relational operations of interest include editing, formatting, indexing, searching, abstracting, etc., all of which map a text relation into another text relation.

The relational view of decision models has been investigated in some detail [4.7]. A model relation is a normalized virtual relation and is a subset of the Cartesian product of a set of domains corresponding to the input and output attributes of a model, where the output is functionally dependent on the input. There are four principal differences between data and model relations: (1) as mentioned, model relations are virtual, (2) the criteria for model bank organization do not depend on storage anomalies, since no tuples are stored, but on anomalies in model bank processing, (3) the criteria for relational completeness of data and model bank query languages differ, and (4) when a model bank cannot be represented by a directed acyclic graph, a fixed point algorithm must be used to integrate the model bank.

Since a relational view of an expert system accessing a knowledge base is similar to that of a causal decision model accessing a data file, the interesting question is: is what would be a relational view of a knowledge base? Three views have been presented in the literature. The first is a relational view of assertions in sentential calculus, in which the relations are modified truth tables [8]. The second is an entity–relationship view of rule-based systems, in which facts and rules are entity sets, and facts are assigned to antecedents and consequents by relationship sets [18]. The third is a view of a frame-based systems, in which slots and values (and especially inheritance structures) are contained in a relational database [1].

The final type of information resource is human information resources. Some attention has been paid to the notion that people and groups of people, when viewed as information resources, can be represented in relational form [2,5]. In this respect they are similar to decision models; they are normal relations with input and output attributes. That is, they receive certain information (e.g., product and pricing information) and are asked to provide other information (e.g., a sales forecast). However, an important difference between the relational view of human information resources and the others is that the former can have any of the other relations as inputs, including other human information resources. This is how groups and their members can be represented in a single framework.

The notion that many different types of information resources can be represented in relational form should not be surprising, since all receive information as input and provide information as output, and the relationships between input and output can be viewed as a set of tuples defined over the input and output. The principal differences between the relational representations of the different information resources are whether the relations are stored or virtual and whether they are normalized or not. There are also substantial differences in the criteria for relational completeness for languages that process these relations, but here we will not be concerned with that issue; we will focus on the way in which the relations should be represented.

## 3. An Entity-Relationship Model for Information Resource Integration

The two principal concepts in the entity–relationship (E–R) model of stored data is that of an entity set and a relationship set [9,10,12]. An entity set is a set of real-world entities, such as employees or spare parts, and each entity corresponds to a tuple in a relation – that is, a record in a file, such as a payroll file or a spare parts inventory file. A relationship set provides semantic information about a relationship between two or more entity sets. For example, a department will contain employees and a department will be managed by an employee. Therefore, there are two relationships between department and employee entity sets, one of membership and one of management, and these are represented by two relationship sets.

In the E-R approach as applied to model management an entity set corresponds to a model viewed as a virtual relation, and a relationship set describes the interactions between models when the outputs of some models are inputs to others [6]. An entity set describes a single entity in the real world (the entity being modeled), and the tuples in its relation describe the causal relationship between the input and output attributes of the model. In addition, models may form cycles (e.g., the output of one model may be the input to another, and vice versa), in which case a relationship set may represent both relationships. In this paper, we refine this view by creating a special type of relationship set, called a synthesis set, to describe the interactions between models in a cycle.

In the enclosed E-R framework, the entity sets will denote any of the six information resources. The principal difference between the E-R framework for stored data and decision models and this is that the enlarged framework must accommodate both normalized and unnormalized relations. This difference will be represented by enlarging the concept of a relationship set to include normalized (relationship) sets (which correspond to the relationship sets in traditional E-R theory), unnormalized sets (for the more complex case), and synthesis sets for cyclic model banks. The symbolic representation is shown in Fig. 1.

These symbols are used in an entity-relationship diagram (ERD) that displays the entity and relationship sets. The symbols in the ERDs used here are similar to those used in normal ERDs except that (1) there are three types of relationships sets rather than one, and (2) the entity type is written above the entity set. The entity types are FILE, PROCEDURE, TEXT, MODEL, ES/KB (expert system/knowledge base), and HIR (human information resource). When there is more than one example of a particular entity type, they are indexed (e.g., FILE-1, FILE-2, etc.). By convention we use a heavy vertical line in an entity set to separate input (or key) attributes from output (or content) attributes, with the inputs to the left. A thin vertical line separates two or more attributes of the same type (i.e., inputs or outputs).

![](/api/attachments/XV2XD2MZ/fulltext/images/6bda01df543e73c852fdaa83796b50c842e8c701f437bd8ee18c822c52ed8f2c.jpg)  
Fig. 1. Entity and relationship symbols.

We describe and illustrate the concepts outlined above with three simple examples. The attributes names used in these examples appear in Table 1. The first example, shown in Fig. 2, illustrates the use of normalized and unnormalized relationship sets. A file containing price and volume information is input to a procedure that uses the file to calculate parameter estimates in the price-volume relationship. These are input to a model along with a proposed price; the model then calculates the volume expected for the proposed price.

![](/api/attachments/XV2XD2MZ/fulltext/images/23236c448b0a2373ecc0a71a2c9d7d623701d1cca7e063c4f40485c834f7dd55.jpg)  
Fig. 2. Normalized and unnormalized relations.

![](/api/attachments/XV2XD2MZ/fulltext/images/03fb85c6c706772eeaef560479e0f7de2d6b2388f5844a6aa34416683e19b2ed.jpg)  
Fig. 3. Integration of human information resources.

Fig. 3 illustrates the integration of two human information resources and a model. HIR-1 estimates the net income that will result from any given price and volume, and the model calculates the expected volume. HIR-2 uses these two information resources to determine the price, the resulting volume, and the net income; this may lead to some appropriate tradeoffs – for example, if the price is too low, there may be a price war, and if volume is too high, a capacity increase may be necessary. Although HIR-1 and the model are a part of HIR-2 for the purpose of determining an acceptable tradeoff between price, volume, and net income, the ERD makes it clear that these two information resources are identifiable components of HIR-2 or are separate resources available to

![](/api/attachments/XV2XD2MZ/fulltext/images/12c17cc61df0e3ad427dc1044a257c1cf302d9f04c7a12578d36384d2375f03a.jpg)  
Fig. 4. A cyclic model bank.

HIR-2 for the purpose of determining the trade-offs.

Fig. 4 illustrates the use of a synthesis set. (This is a simplified description of an energy modeling system developed by the U.S. government [13].) MODEL-1 is an econometric model that calculates a vector of volume of energy products resulting from a vector of supply prices for the products: MODEL-2 is a linear programming model that calculates the supply prices (in the form of dual variables) that would result from a given set of demands, and MODEL-3 calculates the economic and environmental impacts resulting from a given set of prices and volumes. The first two models are run interactively until a price/volume equilibrium is obtained and the values are entered into MODEL-3, which determines the economic and environmental impacts of the equilibrium prices and volumes.

We note that a synthesis set can be used for information resources other than models. It might be used to describe the interactions between models and human information resources, as when a person uses a simulation iteratively until the inputs result in optimal outputs. It might also be used to describe an iterative negotiation process between two human information resources; e.g., a negotiation between manufacturing and marketing departments to arrive at acceptable inventory levels and production lead times.

## 4. Possible Extensions to the Framework

The principal point of this paper is that when the E-R framework is enlarged to encompass information resources other than data and models, it must be modified to include relations not in first normal form and this requires an expansion of the concept of a relationship set. We outline briefly several other enhancements that might be made.

One is to enlarge the types of relationships sets that may appear in an ERD. This has already been done in the context of stored data. The seminal work on E-R models recognized that different relationship sets might be used to distinguish between one-to-one, one-to-many, and many-to-many relationships between entity sets. Other types of relationship sets have been identified. For example, a recent model includes such expansions as relationship sets that distinguish mandatory and optional set membership [23]. It is quite possible that the addition of these other types of information resources – especially, human information resources – will require more types of relationship sets.

Another possible enhancement is an explicit consideration of the dynamics of information resource integration – that is, an understanding of the process by which information resources communicate. Two paradigms have been suggested for doing this. The first is based on expert systems: an information resource may be viewed as a rule in a rule-based system in which the antecedent is the input to the resource and the consequent is the output of the system, where the communication pattern is backward chaining [2,5]. The second paradigm is based on object-oriented programming, in which each information resource is a data object. Information hiding and encapsulation are used to describe formal bureaucratic or technological boundaries between information resources, communication is accomplished by message passing, and inheritance is used to model the hierarchical structure found in most organizations [3]. It may be possible to combine these approaches to develop a common framework for both the representation of information resources and the processing of information.

The ability of object-oriented systems to instantiate data objects dynamically suggests another possible enhancement - the construction of a higher-level ERD that describes when new information resources will be created. Surprisingly, our framework should make that possible, because the process of creating a new information resource corresponds to an entity set with a non-atomic output domain. Consider the example of Fig. 5, which describes a part of an organization that has many product lines. Whenever the volume a product exceeds a threshold, a new department is created to plan for the product line, and the planning department is responsible for determining the net income that would result from a given sales volume. In this (extremely simple) example, HIR-2 is the new department, and HIR-1 decides when it should be created. We can represent this event because the output of HIR-1 is an entity set, rather than an attribute.

![](/api/attachments/XV2XD2MZ/fulltext/images/cbcbb875a57222965b0cd09b6d5360577172f2071259e588a800853904ce6897.jpg)  
Fig. 5. Creation of a new information resource.

Finally, it may be desirable to expand the concept of an entity set beyond information resources. An example is the event-state model, in which events (which correspond to the invocation of information resources) are supplemented with states [20,21]. A state is an attribute, but usually a Boolean attribute (e.g., an out of stock condition or the arrival of an order). This approach appears useful in modeling the forms flow and information processing procedures found in office information systems.

## 5. Conclusion

The management of any resource, including information, is made more effective by the development of (1) a theory of resource acquisition, maintenance, and use, (2) a discipline based on the theory that guides managers in the process of acquisition, maintenance, and use of the resource, and (3) systems that help managers to apply the discipline. We now ask – how might the framework be helpful in theory, discipline, and system development?

The principal point of this paper is that an E-R approach to information resource management must accommodate relations that are not in first normal form. Therefore, a comprehensive theory of IRM must be based on notions of unnormalized relations. (They may be called something else, but they will be unnormalized relations.) Attempts are being made to develop such a theory, in the context not of information resource management, but of computer science. Some investigators interested in bringing artificial intelligence and database management closer together (sometimes called 'expert database systems') believe that extending the notion of a relation may be useful in integrating data bases and knowledge bases [11,15,19]. It is not clear where this line of research will go, but it may provide insights to those who wish to construct theories of IRM.

The development of a discipline to guide managers in the application of the theory and systems that assist managers in the implementation of the discipline must await at least some theoretical results, and possibly the incorporation of additional considerations. But one thing is clear. It is possible to view many apparently different types of information resources in a common framework, and the fundamental characteristics of that framework are clear. What is not clear is how these fundamentals will have to be embellished and what theoretical and practical results will ensue.

## References

[1] Abarbanel, Robert M. and Williams, Michael D., "A relational Representation for Knowledge Bases," Proceedings of the First International Conference on Expert Database Systems, Charleston, April 1986 (also published as Expert Database Systems, ed. by Larry Kerschberg, Benjamin Cummings, Menlo Park, 1988).

[2] Blanning, Robert W., "Expert Systems as an Organizational Paradigm," Proceedings of the Eighth Annual International Conference on Information Systems, Pittsburgh, December 1987, pp. 232-240.

[3] Blanning, Robert W., "An Object-Oriented Paradigm for Organizational Behavior," DSS-87 Transactions, June 1987, pp. 87–94.

[4] Blanning, Robert W., "A Relational Theory of Model Management," Chapter 2 in: Decision Support Systems: Theory and Application, ed. by Clyde W. Holsapple and Andrew B. Whinston, Springer-Verlag, Berlin, 1987, pp. 19–53.

[5] Blanning, Robert W., "The Application of Metaknowledge to Information Management," Human Systems Management, Vol. 7, 1987, pp. 49–57.

[6] Blanning, Robert W., "An Entity-Relationship Approach to Model Management," Decision Support Systems, Vol. 2, No. 1, March 1986, pp. 65–72.

[7] Blanning, Robert W., "A Relational Framework for Information Management," in: Decision Support Systems: A Decade in Perspect e, ed. by Ephraim R. McLean and Henk G. Sol, North-Holland, Amsterdam, 1986, pp. 25-40.

[8] Blanning, Robert W., "A Relational Framework for Assertion Management," Decision Support Systems, Vol. 1, No. 2, April 1985, pp. 167–172.

[9] Chen, Peter Pin-Shen, "The Entity-Relationship Model - A Basis for the Enterprise View of Data," Proceedings of the National Computer Conference, 1977, pp. 77–84.

[10] Chen, Peter Pin-Shen, "The Entity-Relationship Model - Toward a Unified View of Data," ACM Transactions on Database Systems, Vol. 1, No. 1, March 1976, pp. 9–36.

[11] Fischer, Patrick C. and Thomas, Stan J., "Operators for Non-First-Normal-Form Relations," Proceedings of The 7th International Computer Software Applications Conference, November 1983, pp. 464–475.

[12] Flavin, Matt, Fundamental Concepts of Information Modeling, Yourden, New York, 1981.

[13] Hogan, William W., "Energy Policy Models for Project

Independence," Computers & Operations Research, Vol. 2, Nos. 3/4, December 1975, pp. 251–271.

[14] Horton, Forest W., Information Resources Management: Concepts and Cases, Association for Systems Management, Cleveland, 1979.

[15] Korth, Henry F., "Extending the Scope of Relational Languages," IEEE Software, Vol. 3, No. 1, January 1986, pp. 19–28.

[16] Maier, David, The Theory of Relational Databases, Computer Science Press, Rockville, 1983.

[17] Merrett, T.H., "First Steps to Algebraic Processing of Text," in: New Applications of Data Bases, ed. by G. Gardarin and E. Gelenbe, Academic Press, London, 1994, pp. 109-127.

[18] Monarchi, David E., "The Representation of Rules in the ER Model," paper presented at the Rocky Mountain Conference on Artificial Intelligence, Boulder, June 1986.

[19] Roth, Mark A., Korth, Henry F., and Silberschatz, Abraham, "Theory of Non-First-Normal-Form Relational

Databases," Technical Report 84-36, Department of Computer Sciences, University of Texas at Austin, December 1984.

[20] Sen, Arun and De, Prabudda, "A Formal Procedure for Requirement Analysis in Data Base Design." Proceedings of the Fourteenth Hawaii International Conference on System Sciences, January 1981, pp. 127-136.

[21] Sen, A. and Kerschberg, L., "Enterprise Modeling for Database Specification and Design," Data & Knowledge Engineering, Vol. 2, No. 1, March 1987, pp. 31-58.

[22] Synnot, William R. and Gruber, William H., Information Resource Management: Opportunities and Strategies for the 1980s, Wiley, New York, 1981.

[23] Teorey, Toby J., Yang, Dongqing, and Fry, James P., "A Logica? Design Methodology for Relational Databases Using the Extended Entity-Relationship Model," Computing Surveys, Vol. 18, No. 2, June 1986, pp. 197–222.

[24] Yang, Chao-Chih, Relational Databases, Prentice-Hall, Englewood Cliffs, 1986.
