---
otero_id: 18552
otero_key: "F8VQ98TT"
title: "Logical design of data base systems"
authors: "G. Pangalos"
year: "1989"
journal: "Information & Management"
doi: "10.1016/0378-7206(89)90052-9"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Logical Design of Data Base Systems

G. Pangalos

Greek Productivity Centre, Athens 10682, Greece

The importance of a conceptual schema for a successful data base design is widely accepted today. Its development remains however a major problem during the logical design of a data base system. A number of problems related to the role, structure and implementation of a conceptual schema for an enterprise are briefly discussed in this article and a conceptual schema structure and design methodology is proposed that should help meet the requirements of the users in an optimal way. An appropriate data base model structure is also proposed; it provides the necessary underlying structure for the conceptual schema and helps overcome some of the problems currently encountered.

Keywords: Logical database design, Conceptual schema, Data models, Relational schema synthesis, Relational schema design.

![](/api/attachments/F8VQ98TT/fulltext/images/8a25fbba4a02cc9c75fb5dda24ce397d026f81e13703e901688e9854885a49a6.jpg)

George J. Pangalos has a B. Sc. degree in Mathematics from the University of Athens (1973). He also has a Master's degree (1974) in I.T. and a Doctor's degree (1979) from the University of London in Informatics. Today he is the manager of the informatics and organization division of the Greek Productivity Center (ELKEPA). He also teaches informatics at the University of the Aegean. He is currently the president of the Confederation of European Computer User's Association (CECUA). He has also been presiden (1985–88) of the permanent working group on education and research of the Greek Computer society. His interest include the areas of Data Base Technology and computer based Information Systems. He has been involved as project leader in a number of major Greek and EEC projects in the above areas. He has also carried out a number of projects for the greek government. He has written a number of books published in Greece on I.T. subjects and has published a significant number of articles in international journals. He also publishes often in various Greek journals.

## 1. Introduction

The description of an enterprise in the form of a conceptual data base schema represents a major problem during the logical design of a relational data base (2,5,14). In the overall data base design process (fig. 1) this step immediately follows the data and process analysis of the enterprise (13). The need for a conceptual schema in the context of a three schema framework for data base management systems was identified over a decade ago (1). Subsequent papers have also emphasized its importance to users and designers of data base systems (16, 17). The importance of the conceptual schema for a successful data base design is widely accepted today. Despite its importance, however, no generally acceptable definition of the precise structure and design methodology of a conceptual schema for an enterprise seems to exist as yet.

![](/api/attachments/F8VQ98TT/fulltext/images/337aae4ea8ddde9affda1eb292b41966f80bed92ed228dff125ace961d04c61a.jpg)  
Fig. 1. Overview of the data base design process.

A number of problems related to the role, structure and implementation of a good conceptual schema for an enterprise are briefly discussed and a conceptual schema structure and design methodology is proposed which should help overcome some of the problems currently encountered. An appropriate data base model structure is also proposed that provides the necessary underlying structure for the conceptual schema. The proposed design methodology has already been used successfully for the design of integrated data base systems in a number of cases (15).

## 2. The Conceptual Schema Structure

The conceptual view, as originally exposed by the ANSI/SPARC ad hoc data base study group (1), concentrates on the meaning of the information, described in the conceptual schema, which therefore contains a unique central description of the various information that may be in a data base. This includes the description of what actions, such as updates and retrievals, are permissible. However the detailed definition of the structure and functions of the conceptual schema remains a problem (11, 14, 16). According to the well known ANSI/SPARC report, a conceptual schema ‘represents the enterprise’s view of the structure it is attempting to model in the data base. This view is that which is informally invoked when there is a dispute between the user and the programmer over exactly what is meant by program specifications… (1).

A conceptual schema, as perceived here, has a wider scope. It is seen as the final result of the systems analysis process or the end product of the modeling process. It provides a formal description of the real world enterprise and its operations of interest to the designer and can be used as a framework around which the enterprise information system is developed. It stands between the perceivable reality of the enterprise, from which the systems analysis for the data base design starts, and the final description of the data base in computer dependent terms. It can therefore be regarded as an interface between the analysed and implemented structures.

Thus, the conceptual schema for an enterprise should describe:

(a) The conceptual structure of the enterprise (static view).

This includes a description of the object types permanently associated with the enterprise, their properties and the relationships existing between them. It also includes specification of the constraints and other semantic information that define the valid states of the data.

(b) The rules for the evolution of the data base (dynamic view).

This describe the set of permissible operations that can modify the structure of the data base, to reflect changes in the organization and activities of the enterprise.

Much of the past research on the conceptual schema has concentrated on the static aspects; i.e. on defining the concepts used to describe valid states of a conceptual schema and the data base. However, the conceptual schema should also cover the dynamic aspects: It must be able to be changed to reflect variation in the real world. Also, dynamic aspects are involved in describing those manipulations which are needed to keep the data base in phase with the conceptual schema.

In some cases, the changes in the real world and the corresponding changes in the conceptual schema and the data base need not be closely linked: changes may be recorded in the conceptual schema and the data base retrospectively. However sometimes timely response to change is so necessary that the conceptual schema and data base must rapidly reflect the real world; the description of this interaction must also be part of the dynamic aspects. However no clear boundary has been defined between static and dynamic aspects. It may well be found to vary from one approach to another, or even to be non-existent. It must also be noted that these ideas have not yet been widely debated. For example it is not yet clear whether different methods should be used to describe static and dynamic aspects, or whether, at least sometimes, the same concepts may fulfill both purposes.

The conceptual schema is beneficial in many ways. Since it contains no implementation dependent details, the resulting design is independent of the configuration of the computer system and of the data base model (relational, network etc.) used for the implemented structures. Its introduction also provides a systematic method, of better understanding the reel world semantics of the enterprise and provides a means of communication between the people and procedures. Finally, it bridges the gap between the analysis phase and the final data base schema, and encourages a new, powerful approach to the entire design process.

It is necessary to provide two other interfaces. The first deals with the external representation forms (the user view); these are described in external schemata. An external interface is thus the actual interface between a user in the environment and the implemented information system.

The second deals with such matters as the internal (physical) representation forms: the storage facilities, the computer process efficiency, the control of concurrent use, e.t.c. These interfaces are defined in an internal schema. It can be defined as the statement of the internal representation forms of the collections of information in the data base, including their manipulation aspects. An internal interface is thus the interface between the implemented information system and the physical data storage facilities.

## 3. The Data Model Structure

Since the conceptual schema is to be an interface between the needs and the implemented data structure, it is important to use a data model to provide the underlying structure; this will help to understand, analyse and describe the real world enterprise, and deal with the logical view of data.

Research in data modeling has produced a number of papers, each expounding the merits of a specific method or conceptual schema model. Earlier methods concentrated mainly on the forms of the data, while more recent modeling techniques stress the importance of modeling the meaning (semantics) of the information. Each has a number of advocates and each is a distinct way of viewing the problem: abstract data types, binary relationship models, conceptual graphs, deep structure sentence models, entity relationship models, function-oriented models, N-ary relationships models, network models, object-role models, process interaction models, relational models, semantic nets, set theoretic models e.t.c. Based on the concepts and characteristics of each of the methods, we identify three major groups: the Entity-Attribute-Relationship approaches, the Binary and Elementary $N$ -ary Relationship approaches and the Interpreted Predicate Logic approaches.

The Entity Attribute Relationship Approaches (EAR), as introduced and further developed by Bachman, Chen et al. (3), are based on the use of four basic concepts: entities and relationships among entities, attributes (associations between values and entities, or between values and relationships) and Values. They also make use of the notions of type and occurrence. They are oriented towards the definition of static aspects. Therefore, generally speaking, they can describe only partially the various rules of the real world [or universe or discourse). The EAR approaches often imply special kinds of propositions that are grouped together and expressed in single macro constructs and they do not provide for explicit distinction between lexical and non-lexical entities.

The Binary and Elementary N-ary Relationship Approaches (BER) have their roots in certain approaches in artificial intelligence and linguistics, dealing with ‘semantic networks’ and other similar notions (6). They distinguish entities from entity names but do not distinguish between attributes and relationships. Furthermore, only binary relationships are recognised. The BR approaches are based on three primitive concepts: entities, entity names, and binary relationships. They also make use of the notions of type and occurrence applied.

The Binary Relationship approaches started with the capability of defining static aspects, but in recent years they have been extended to handle dynamic aspects also. BR approaches are now able to describe all rules that are relevant for the real world. Variants of these approaches distinguish between lexical and non-lexical entities. Developments in the mid seventies resulted in the so-called n-ary relationship approach, which do not restrict an elementary proposition to be about exactly two entities, but allow description of elementary propositions involving one, two or more entities.

The Interpreted Predicate Logic Approaches (IPL) as proposed by authors such as sTeel, perceive the real world as solely consisting of entities, for which propositions hold. The conceptual schema constitutes a description consisting solely of a set of sentences encoded in some formal language based on formal logic. Such sentences are composed of: terms and variables, predicates, logical connectives and quantifiers. The terms and variables refer to the entities in the real world and the sentences express the proposition about those entities.

The essence of this group is the establishment of an interpreted, axiomatized, deductive, formal system of logic describing the real world without placing any modeling constraint on it. The basic principles of these approaches are equally well applied to both static and dynamic aspects of the real world. They also provide for explicit distinction between lexical and non-lexical entities. Some variants of these approaches apply a very limited set of elementary constructs and use them to “generate” and construct the full conceptual schema for the chosen environment, while others include more complex constructs and capabilities in their basic set to increase the ease and convenience of a user in expressing all kinds of propositions about the real world. Several also provide for dynamically extending the expressive power of the language.

## 4. The Conceptual Schema Design

In the vast majority of the published work, the conceptual schema is usually dedicated to describing the real world. That is, it mainly defines the semantics of the information and, therefore, the interpretation of all representation forms thereof. It is expected that future data base management systems will include a component for handling conceptual view has usually to be 9 manually) converted to a ‘common data base view’ expressed in convenient computer oriented data structures and constructs.

The selection of an appropriate data base model on which the information system will be implemented is therefore very important today. In order to facilitate the selection of such an appropriate data base model, we identify the following four levels of logical views of data:

Level 1:

Information concerning entities and relationships, as perceived by the real world enterprise. This information exists in our minds, and it is at this level that the analysis of the enterprise ought to start (e.g., a supplier).

Level 2:

Information represented by data. Here the entities and relationships of the real world enterprise are represented by data (e.g., supplier 2372).

Level 3:

Data structures independent of implementation considerations. However, no access paths, indexing, search techniques, or any other implementation dependent details are involved here (e.g., relation: supplier).

Level 4:

Data structures dependent on implementation considerations (e.g., the set of all supplier).

Since the data itself may be implemented in any one of a number of ways [various data base management systems (DBMS's)], a satisfactory data base model ought to be able to cope i with all four levels. Nevertheless, none of the currently implemented DBMS's do this in a satisfactory way. The Entity model, for example, is mainly concerned with levels one and two though it claims to cover all four levels, while the Network model only with levels three and four with emphasis on four (6): it is almost applicable to a CODASYL/NDL, but not quite.

The well known Relational model, as introduced by Codd (6, 7, 8), is basically concerned with levels two and three. As a result, another compatible data model has to be used at level one, during the design process. Also the Relational model, does not provide adequate details on how the proposed data structures will be implemented on the machine (level four). The various mappings and implementation strategies adopted by individual data base management system have therefore to be used for this level. For the design of an experimental hospital data base, for example, facilities provided by the RDBMS were used at this level (14).

It should also be noted that the relational model does not conveniently support the definition of mandatory relationships in a generalized, conceptual manner; e.g., there is no ‘relational’ diagramming convention analogous to Bachman’s or

Chen's. The diagramatic representation of domain constraints further defies representation.

Although the relational model has some inadequacies, it was selected for several important reasons: it is easy to understand and manipulate and has a sound theoretical basis. The model itself also possesses a considerable body of theory, for example the theory of relation completeness, by which the expressive power of a language can be tested or various candidate languages compared. It provides symmetry and types of non-redundancy by using a normal forms and the power to manipulate groups of data in the attribute of a relation. Finally, relations are easy to manipulate and the result of a relational operation is again a relation; this allows the construction of nested expressions in a relational language.

For these reasons, and despite the difficulties at level one and four, the relational model of data, supplemented by an auxiliary data base model was chosen to form the basic underlying structure for our conceptual schema.

## 5. The Auxiliary Data Base Model Structure

The following basic concepts, which constitute the building blocks for the entire data base model, have been selected as the basic elements of the proposed auxiliary data base model.

1. Entity. This is the basic concept. It can be defined as something that can be distinctly identified or anything that has reality and distinctness being in fact or in thought. Examples of entity are Jonew which is a patient, Evans who is a customer, etc.

2. Entity set. When entities are put into context, they can be classified into entity sets. There is a membership characteristic associated with each entity set, which can be tested to determine whether an entity belongs to the set or not. Example entity sets are: patients of ward 24 A, suppliers of part B. The concept of an entity set is particularly useful during the structural analysis of the enterprise.

3. Property. Entities have properties or attributes. There are some named properties associated with each entity; where an instance of an entity occurs, the value of these properties is known. Some properties or attributes of the entity patient could be patient-name, patient-age and patient-number.

4. Relationship. A relationship is an association between entities. Activities in an enterprise create relationships; e.g., patient – ward, supplier – product. For the sake of simplicity of the model, relationships are not allowed to have properties. As Hall et al. (9) noted, this does not affect the basic expressive power of the model. Relationships can also be classified into relationship sets.
5. Value. A value is data about an entity or relationship obtained by observation or measurement, e.g. age '35', year '1564', forename 'John'. Values can be classified into value sets; e.g., integer, name, real. A property can thus also be defined as a mapping from an entity or relationship set to a value set.

The above basic concepts were selected because

(a) From the real world semantics point of view, immediate experience of the real world leads people to recognise that it may be described using entities, properties and associations between them.

(b) Systems theory, on which the structural analysis will be based, uses similar concepts when describing models of the real world (4).

(c) From the implementation point of view, the above concepts are suitable since most models of data, use identical, similar or compatible concepts.

Although these basic concepts are rather simple, it is not always easy to decide which ones to use when modelling the real world. It may be difficult to choose between an entity, and a relationship or between an entity and an attribute. The ownership of a house, for example, looks like a relationship (owner–house) and may be so, but to a government department, this ownership could very well be regarded as an entity in its own right. This has been discussed in many articles from the 60s on.

## 6. The Relational Data Base Schema Design

The subsequent design of the appropriate relational schemas which will satisfy the information processing requirements of the users, is a significant problem during the logical design of a relational data base. In the context of the overall data base design process, this step immediately follows the conceptual schema design process.

The relational schema design methodologies that have been proposed provide a number of useful tools for the design of schemas. They all impose, however, some undesirable limitations to the data designer. A brief evaluation of their potentials and limitations, based on the experience obtained during the development and subsequent use of an experimental relational hospital data base, can be found, in (14). However, despite the progress, the provision of a strategy and specific guidelines for the selection of an appropriate set of attributes, the formulation of the initial set of relations and the early stages of their breakdown, still remains a problem.

In future, it may be possible to apply various mechanical synthesis algorithms automatically without human intervention. Today, using existing implementations, human intervention is necessary in the selection of the appropriate alternative. When the relational hospital data base schemas were synthesized, a long time was spent going back and forth on theoretically equivalent schemas, until, with the user's help and participation, an acceptable relational schema was provided.

In practice there are problems with synthesis algorithms. For example, relations with more than a few dozens of attributes were not allowed in the experimental data base, because they proved to be inconvenient for the users and because of implementation restrictions. On the other hand, many small relations with few attributes were equally undesirable, since answering a query would then involve many JOIN operations, which complicate the queries and are slower. Furthermore, only a limited number of relations could practically be joined at one a time; this is a problem when information is required from more than a few basic relations and temporary relations are not available.

## 7. Conclusions

The development of an appropriate conceptual data base schema to satisfy the information processing requirements of the users, is a major problem during the logical design of a relational data base. A number of problems related to the role, structure, and implementation of a conceptual schema have been discussed and a conceptual schema structure and design methodology has been proposed. These should help overcome some of the problems currently encountered and meet the requirements of the users in the best possible way. An appropriate data base model has also been proposed. It provides the necessary underlying structure for the conceptual schema and deals with the logical views of the data.

## References

[1] ANSI/X3/SPARC. Interim Report: Study Group on Data Base Management Systems. ACM SIGMOD Newsletter, Vol. 7, No. 2, 1975.

[2] Benci, E., Bodart, F., Bogaert, H., and Cabanes, A. Concepts for the design of a conceptual schema. Modelling in Data Base Management Systems, Nijssen, G.M. Editor, North-Holland, 1976, pp. 181–201.

[3] Chen, P.P. The entity–relationship model – towards a unified view of data. ACM Transactions on Database Systems, Vol. 1, No. 1, 1976, pp. 9–36.

[4] Churchman, C.W. The Systems Approach, Delta Publ. Co., 1968.

[5] Codd, E.F. A relational model of Data for large shared data banks. Communications of the ACM. Vol. 13, No. 6, 1970, pp. 377–387.

[6] Codd, E.F. Further Normalization of database sublanguages. Data Base Systems, R. Rustin Editor, Prentice-Hall, 1972, pp. 33–64.

[7] Codd, E.F. Relational completeness of database sublanguages. Data Base Systems, R. Rustin Editor, Prentice-Hall, 1972, pp. 65–98.

[8] Codd, E.F. Recent investigations in relational database systems. Information Processing 74, North-Holland, 1974, pp. 1017–1021.

[9] Hall, P.A. et al. Relations and entities. Modelling in Databases, Nijssen, G.M. Editor, North-Holland, 1976, pp. 201–219.

[10] Hitchock, F.P. conceptual systems analysis: an introduction, IBM (UK) Scientific Centre Report (draft), July 1976.

[11] Moulin, P., et al. Conceptual model as a database design tool. Modelling in Data Base Management Systems (April 1976), Nijssen, G.M. Editor, North-Holland, 1976, pp. 221–239.

[12] Tsichritzis, D.C. and Lochovsky, F.H. Data Base Management Systems. Academic Press, 1977.

[13] Pangalos, G. Design and implementation of relational data base systems. Ph.D. Thesis, University College, University of London, 1980.

[14] Pangalos, G. Conceptual data base schema design, Information Age, Vol. 8, No. 3, pp. 162–167, 1986.

[15] Pangalos, G. Design of integrated hospital data bases, Medical Informatics, Vol. 11, No. 2, pp. 159–166, 1986.

[16] ISO/TR 9007, Concepts and terminology for the Conceptual Schema and the Information Base, ISO 1987.

[17] Olle T.W., Sol H.G., Verrijn Stuart A.A., Information Systems design methodologies: a comparative review, IFIP WG 8.1 CRIS I, North Holland, 1982.

[18] CODASYL Programming Language Committee DBIG proposal February 1973. Available from ACM.

[19] CODASYL Data Description Language Committee. DDL Journal of Development 1978. Material data management branch, Department of Supply and Services, Quebec, Canada, 1978.

[20] Florentin, J.J. Databases representation of application models. Computer Journal, Vol. 19, No. 1, 1976, pp. 13–16.

[21] Kechsberq, L., Klug, A. and Tsichritzis, D. A taxonomy of data models. Systems for Largew Databases, Lackleman, P.C. and Neuhold, E.J. Editors North-Holland, 1976, pp. 43–81.

[22] Lyon, J.K. An Introduction to Database Design. Interscience, 1971.

[23] Stamper, R. Identifiers of physical objects: an aspect of the semantic model of the LEGOL system. LEGOL Project publication, London School of Economics, 1976.

[24] Atre, S., Structure techniques for database design, performance and management, Willey and Sons Inc., N.Y., 1980.

[25] Beri, C. and Bernstein, P. A sophisticated's introduction to data base normalization theory. Proceedings 4th International Conference on Very Large Data Bases, Yao, S.B. Editor, IEEE, pp. 113–124, 1978.

[26] Bernstein, P.S. Synthesizing Third Normal Form relations from functional dependencies, ACM Transactions on Data base Systems, Vol. 1, No. 4, pp. 277–298, 1976.

[27] Bramhill, A., and Taylor, G. Data base design. Data base Journal, Vol. 6, No. 12, pp. 18–23, 1976.

[28] Date, C.J. An Introduction to Data base Systems (Second edition). Addison-Wesley, 1977.

[29] Fagin, R. Multivalued dependencies and a new normal form for relational data bases. ACM Transactions on Data base Systems, Vol. 2, No. 3, pp. 262–278, 1977.

[30] Garret, R.D. Hospitals - A Systems Approach. Auerbach Pub. Co., Philadelphia, 1973.

[31] Panqalos, G. Information-oriented approach to structured analysis and design. Information Age, Vol. 8, No. 1, pp. 43–47, 1986.

[32] Sundgren, B. Data base design in theory and practice. Proceedings 4th International Conference on Very Large Data Bases, Yao. S.B. Editor, IEEE, pp. 3–16, 1978.

[33] Zaniolo, C. Analysis and Design of Relational Schema for Data base Systems, Ph.D. Thesis, Computer Science Department, School of Engineering and applied Science, University of California, 1976.

[34] Mac Donald I.G., Information Engineering – An Improved, Automatable Methodology for the Desing of Data Systems, Proc IFIP WG 8.1 Working Conference on Comparative Review of Information Systems Desing Methodologies: Improving the practice, Noordwijkerhout, The Netherlands, 5–7 May, 1986.

[35] Olle T.W., Sol H.G., and Tully C.J., Information systems design methodologies: a feature analysis IFIP WG 8.1 CRIS II, North Holland, 1983.

[36] Olle T.W., Sol H.G., Verrijn-Stuart A.A., “Information Systems Design Methodologies: Improving the Practice”, Proc IFIP WG 8.1 Working Conference on Comparative Review of Information Systems Design Methodologies: Improving the Practice, Noordwijkerhout, The Netherlands, 5–7 May, 1986.

[37] Ross D.T. & Schoman, "Structured Analysis for requirements definition", IEEE Trans SE 3 (1) pp. 1-65, 1977.

[38] Verheijen G. & Van Bekkum J, NIAM: an information analysis method. in ISDM, a comparative review, North Holland, IFIP, 1982.
