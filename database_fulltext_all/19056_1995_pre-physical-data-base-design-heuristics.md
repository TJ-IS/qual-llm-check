---
otero_id: 19056
otero_key: "CFXCHEUX"
title: "Pre-physical data base design heuristics"
authors: "Narciso Cerpa"
year: "1995"
journal: "Information & Management"
doi: "10.1016/0378-7206(94)00054-m"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Research

# Pre-physical data base design heuristics

Narciso Cerpa $^{*}$ ,1

School of Computer Science and Engineering, Faculty of Engineering, University of New South Wales, Sydney 2052, NSW, Australia

## Abstract

Data base design encompasses both business and technical aspects. Conceptual data modelling creates a conceptual schema to abstract the user view of data within the business context. This conceptual schema is mapped to the logical data model structure in order to obtain a set of normalized relations. These ensure the integrity of the data by avoiding update anomalies. Regardless of the methodology used, the process or transaction model will impact on the data base design process and its refinement. Since the process or transaction model will reflect the business requirements and specific users view of the data, it will determine the relevance of having a fully normalized set of data, or the need for trading off some degree of normalization, with the aim of improving performance in the query process. The model will also indicate the activity requirements on the relations in the logical data model, their frequency, and characteristics. A pre-physical design step is described, and a set of heuristics is proposed in order to obtain a refined data base design.

Keywords: Data base; Data base design; Data model; Data base management; Physical design; System design; Design improvement; Denormalization; Design refinement

## 1. Introduction

The design of data base applications requires a high degree of business and technical skills. Over the past fifteen years there has been considerable literature written on data base theory, concepts, techniques and implementation. The commercial arena has used three kinds of data base management systems (hierarchical, network, relational). A new wave of object-oriented data base management systems is now reaching the market, and it is likely that they will be very attractive to practitioners, due to the richness of their data model in capturing data semantics [5]. The main purpose of this paper is to discuss those practical issues of data base design, that have been classified as part of an intermediate step between logical and physical design [26]. This we shall call pre-physical design. The step permits removal of any inflexibility from the logical schema, based on application process requirements and user view of the data.

The issues discussed here, apply to any of the three data base models, but we will concentrate on the relational model, since this is more current and is utilized by a large number of applications currently implemented in the market.

The aim of this paper is to present some design heuristics, that can be applied to the logical schema for refining the data base design prior to the physical design. This refinement process requires a high level of expertise on the part of the data base designer, as well as appropriate knowledge of application requirements. This seems a contradiction to normal relational data base design. Non-expert users often believe that the relational model has taken the burden from the data base designer, and that no decisions need to be made on how the data should be accessed. Such a belief is misconceived, because even though the relational model provides a level of abstraction not provided by its predecessors, it is vital to understand the technicalities underlying the model in order to achieve a good design.

## 2. Normalization

The process of normalization was first introduced by Codd with the purpose of improving data base design, by not allowing update anomalies to occur. These were classified as insertion, deletion, and modification anomalies. Normalization decreases data redundancy and provides flexibility of updates, providing a theoretically sound basis for logical data base design practices $[3]$ . Normalization is also a powerful tool for analyzing the minimality, completeness, and consistency of data models $[16]$ . Normalization is a property of relations, and we say that a relation is in normal form if it satisfies a number of properties. The first three normal forms are given in Figure 1.

Normalized relations provide an appropriate logical structure for data base design, especially when given in third normal form.

In certain physical implementations, normalization will offer performance advantages, since it entails splitting a relation into two or more parts, resulting in fewer columns per relation. Some DBMSs have the page as their basic unit of input/output. The number of rows per page depends on the row length, which in turn depends on the number of columns per row. Therefore, normalized relations could fit more rows per page than unnormalized relations, requiring less input/output operations for the same number of rows, if the columns required reside in just one of the normalized relation [27].

![](/api/attachments/CFXCHEUX/fulltext/images/dd1db870d4e10d246bae05d424b39287ed54cb8a385f355d01c3e9e08e48fae5.jpg)  
Fig. 1. The first three normal forms [7].

Normalization avoids update anomalies, and also accelerates the update process, because the insertion and deletion of an entity occurrence, or the modification of the attributes of an entity occurrence, happen in only one place.

However, normalization can slow down query processing, because the data requested by a query transaction, may be spread across different relations. If columns from those different relations are required, join operations are needed to obtain them, requiring extra processing and temporary space [22].

Denormalization can be described as the process of reducing the degree of normalization with the aim of improving query processing performance. While there are strong arguments in favor of normalization, there may be cases, where the application requirements call for some degree of denormalization $[24]$ . Data base design is an evolutionary process: as requirements change, the data base design should adapt to these changes $[20]$ . Hence, the decision as to the degree of normalization required is not so straightforward and definitive as it may seem, because data base design is a dynamic process.

## 3. Data base design

We will concentrate on the description of the data base design presented by Elmasri and Navathe, which embraces the phases required for a complete data base design life cycle.

The systems development life cycle (SDLC) embraces the process summarized in Figure 2, in conjunction with the process or function design activities [12]. Methodologies, based on an information engineering approach [14], are driven by the design of data models instead of process or transaction models, which are typical of the methodologies based on structured techniques [10]. Data modelling techniques have evolved in conjunction with the software engineering approach and improvements in data base management technology, providing an appropriate framework for systems analysis and design [18].

![](/api/attachments/CFXCHEUX/fulltext/images/5025bacfc8a94d9fef5504c2e9e6a950f258527cc41597d7d2905c02238f91c0.jpg)  
Fig. 2. Data base design process [11].

The transaction or process model validates the representativeness and completeness of the data model at any stage of development $[17]$ , as well as providing input for its logical refinement and further physical optimization.

In the data base design process we can distinguish three design levels: conceptual, logical or mapping, and physical.

Conceptual design involves development of a data model to represent the structure of the information and of operators allowed to perform on the information, specifying the restrictions placed upon the information during these operations $[9,22]$ . The ANSI/SPARC framework presents the conceptual schema as one that describes an application in an implementation independent manner $[2]$ .

The ANSI/SPARC framework also proposes direct mapping from the conceptual schema to the internal and external schemas. However, the internal schema can be highly dependent on the specific DBMS used. Since a conceptual schema could be mapped to DBMSs with different data model structures (hierarchical, network, relational), it is essential to have a logical design step for mapping to the logical data model structure in an implementation independent manner. For the purpose of this study, a conceptual model is an entity-relationship model (ER) [6] in 3NF. Mapping an ER model to the relational model has been clearly described in the literature [4,15].

The output from our data model mapping (step 4) are relations in 3NF (logical model), which require a refinement process to satisfy the application performance requirements efficiently. Since the step following model mapping is the physical data base design, several of the logical refinement issues are physical aspects affecting the logical model. Therefore we present some design heuristics as part of a pre-physical data base design process.

## 4. Pre-physical data base design

This new step in the data base design life cycle, is between the data model mapping and the physical data base design. We have separated this step since it involves aspects that are neither purely logical nor purely physical. The main objective of this step is the refinement of the logical design model, taking into account the application performance requirements and users' view of data as specified in the process model.

The refinement process should lead to a refined data base design, that satisfies most of the criteria specified in Figure 3.

We emphasize criterion six, since the achievement of the first five criteria should not compromise ease of development and maintenance of the application as well as maintenance of the data base design.

These criteria for data base design refinement address logical and physical issues. At this stage of design, both issues are strongly related, therefore the input (application processing requirements) provided by the process or transaction model is relevant to meeting the design objectives. Pre-physical design involves evaluating the effectiveness and efficiency of the logical model implementation to satisfy application requirements, keeping in mind the major criteria. This requires analysis of the advantages and disadvantages of possible model implementations.

![](/api/attachments/CFXCHEUX/fulltext/images/8460db9308f4d61763f13f84efc562b132367c003cb04edcc346c4539c9fa0eb.jpg)  
Fig. 3. Criteria for refined data base design.

As in any refinement process, it is sometimes impossible to achieve a completely refined design that satisfies all the criteria specified. In such cases the data base designer should have the appropriate knowledge of the application requirements needed, to evaluate the degree of importance of each of the criteria in conflict, as well as to compromise according to their importance and produce the most satisfactory design. A typical example of compromising is the dilemma that is sometimes presented by queries and updates requirements.

The dynamic of systems applications requires that a data base design should be reviewed following maintenance to or enhancements of the application system. Logical data base design refinement helps to reduce the data base access cost, which is affected by data base activity, computer system characteristics, and physical factors $[21]$ .

During physical design, the data base designer must evaluate the possible access paths through which data could be accessed from the data base. For example, an employee relation, where the primary access key is the employee number, may need to be sequentially scanned to find all the employees that work in the sales department (deptcode = 01). However, a different access path could be added by implementing an index on the department code (deptcode) to speed up the access.

However, these types of decisions are meaningless without knowledge of the cardinality of the relation. The storage requirements of each relation will be instrumental in determining whether to create a new index or to opt for sequential scanning. These issues have been researched in order to estimate the cost of accessing and/or updating relational databases $[1,25]$ and to provide the tools for making the appropriate decisions on indices during physical design. This has resulted in the creation of data base design tools that can automatically evaluate, access, and/or update costs, and provide the appropriate design solution [13]. Most of these tools are not widely available and, in the best cases, they are DBMS implementation dependent, since they make use of the DBMS particular access optimizer software. Use of the optimizer software as part of the design tool is logical, because if there are any further changes to the access optimizer software there will be no need to change the design tool. Some general guidelines for the scanning versus index decision are:

(1) In very small tables, sequential scanning can be as fast or faster than using an index, because of the extra access cost of the index and also the burden of maintaining such an index.

(2) In very large tables, storage limitations should be considered, as well as the cost of maintaining an index, from the data base management system, and data base administration perspectives (recoveries, reorganizations, etc.).

We have introduced a new variable affecting data base design: data base administration. Data bases must be reorganized from time to time in order to avoid performance degradation due to files fragmentation and other technical reasons. The design should take into account these reorganization requirements. For example, a data base containing very large tables (millions of rows) with several indices per table can take many hours to reorganize, and therefore, would need large outages when the data base is unavailable. Some applications are critical and cannot afford such down-time.

There are other variables that a data base designer needs to consider, and these may be hardware and/or software dependent. Some examples are: data storage limitations (disk sizes, pack sizes, etc.), software locking system, storage allocation system, file organization system, system access methods, and access optimization software. There are numerous physical aspects affecting data base design.

Here we provide a list of those variables that affect the logical data base refinement process and should be taken into account during pre-physical data base design. This list is not exhaustive, but all the issues mentioned here are relevant to obtaining an improved design based on criteria previously specified. They were compiled from the literature (e.g. [8,13]), and are as follows:

1. Application performance criteria

2. Application development and maintenance considerations

3. Volatility of application requirements

4. Transactions and relations involved

5. Transaction type (update, query, report)

6. Frequency of transactions

7. Modules called by each transaction

8. Access paths needed by each transaction/module

9. Relations accessed by each transaction/module

10. Number of rows accessed by each transaction/module

11. Cardinality of each relation.

Previous research has proposed solutions to problems such as query efficiency, by materializing the join. In other words, making redundant use of those attributes needed by a query. This entails adding these attributes to an existing relation, so that all the attributes needed by the query reside in the relation accessed by it. The data base designer must evaluate the pros and cons of these approaches, based on the application requirements. The side effects of this redundancy, are the increase of storage requirements, update and referential integrity costs, denormalization cost, loss of integrity, and program transformation on the materialized joins.

Other approaches, are the vertical and horizontal partitioning of relations. Vertical partitioning subdivides the relation attributes into groups, with each assigned to a new relation. Horizontal partitioning subdivides the tuples (instances) into groups (subsets), all of them having the same attributes as the original relation [23]. Each subset will form a new relation. In both kinds of partitioning, the original relation is usually replaced by the newly created ones [19]. This is an approach widely used in distributed data base design. It can also be used in other data base environments to satisfy business, security, and other specific requirements.

![](/api/attachments/CFXCHEUX/fulltext/images/8c5b782758a35894d7ea2fad861ba5a5a9d181634a26056e214e0f66c75a8c53.jpg)  
Fig. 4. A set of heuristics for pre-physical data base design.

## 5. Pre-physical data base design heuristics

The considerable complexity of the decision making process arising from the need to satisfy most of the criteria for refined data base design, highlights the fundamental role that the designer's experience plays. We present some guidelines to follow during pre-physical data base design; they are based on practical experience in designing relational databases (Figure 4). These steps could provide a useful set of heuristics to complement a potential expert system capable of evaluating physical design alternatives. These kinds of expert systems have already been implemented in research projects.

(1) Identification of relations and their cardinalities: All relations should be identified and their cardinalities determined. This will permit evaluation of potential size effects and provide a global picture for making design decisions.

(2) Identification of transactions / modules and relations being accessed by them: All transactions/modules should be identified and the relations being accessed by them determined. The type of transaction access should also be identified (update, query, report). Transactions can be decomposed to the program module level for accuracy. For example, some specific modules (common to several transactions) frequently access large amounts of data from critical relations. This usually reflects lack of modularity and in general poor system design.

(3) Identification of access paths required by each transaction / module: All transactions/modules should be included and their required access paths identified. This will permit determination of the need for refinement, and also be useful, during physical design, in determining the indices required to satisfy access requirements.

(4) Choosing the appropriate key order: All composed keys, primary and secondary, should be ordered in such a manner as to satisfy the majority of the transactions access requirements (e.g., suppose that primary key is composed of bin-number and part-number to make it unique; if there is no requirement to access by bin-number but there are requirements to access by part-number, the order should be part-number followed by bin-number).

(5) Identify sub-groups within data of each relation: Identify the existence of sub-groups within the data of a relation, particularly those based on the primary key or alternative keys. This could help determine the possibility of splitting relations into two or more parts, depending on access requirements (horizontal partitioning). For example, data from a specific branch should only be accessed by staff from that branch; in such a case, the relation could be split into several parts, one for each branch. This approach should be considered for performance and business security requirements. While this may be seen as a physical issue, it can also be driven by business needs. However, it should be carefully evaluated, since complexity will increase.

(6) Identify need for sub-dividing relations based on their columns: Identify the need for splitting relations based on their requirements for access. While this approach will increase the storage required (the key must be present in all relations resulting from the split), it can improve concurrency if the columns implemented in the newly created relations are required by different transactions (vertical partitioning). As in case (5), this approach should also be considered for performance and business security improvement. However, it should be carefully evaluated, since program transformation will be needed and update complexity will increase.

(7) Identify subclasses in relationships between relations: Identification of subclasses, a small subset of the dependent relation, can help organize a different kind of access for such subclasses, avoiding the scanning of all occurrences in the class. (e.g., all teachers per school (class); casual teachers per school (subclass); if we provide an access path for casual teachers, we do not need to scan all the occurrences in the teacher relation or access the whole index by school). This approach is very useful in relations with many occurrences, and where the subclass represents a small subset requiring frequent access. In our example, this is physically implemented by adding a secondary index on the school and type (casual) attributes in the teacher relation to specify those who are casual teachers for each school.

(8) Identify additional access paths between relations: Identify the need for additional access paths for application process driven requirements. This will determine the need for additional indices; e.g., all teachers per school in alphabetical order; all teachers per school in teaching grade order. This is physically implemented by adding a secondary index on the alternative access path.

(9) Analyze need for duplication of data in specific cases: There are cases where the duplication of attributes from the parent relation in the dependent relation can be useful and speed up access but at the expense of increasing the complexity of the update process. This potentially involves denormalization, and therefore should only be done if an evaluation of the advantages and disadvantages reveals that the design is better by doing so. For example, an attribute which could only be obtained by joining several relations (using their respective foreign and primary keys), could be duplicated in the first relation if its update is infrequent, its access very frequent, and the cardinality of the relations considerable.

(10) Identify need for derived attributes and organize their implementation: There are situations where derived data can be used to avoid frequent access to many occurrences of a particular relation or to many different relations. For example, when statistical data, such as totals or averages, are calculated from values obtained from different relation occurrences. The average mark of a student, calculated from different occurrences of the student-subject relation, could be calculated and stored in the student relation every time the attribute mark is updated in the student-subject relation. This speeds up the queries, with only a small update cost if the raw data, the attribute mark in this case, is not updated very frequently.

Derived attributes can also be status data, which can avoid traversing (using joins) through different relations in order to find a specific condition. In such cases, if the frequency of querying the condition is high, a status attribute can be added to the first relation (rule of thumb) accessed by such a query. This status attribute will change every time that an update to the relations involved changes the condition. The cost of updating the status attribute can be very low compared with the cost of joining several relations during queries. This example emphasizes the need for logical data base refinement in those cases where the application requires high frequency of queries, and low frequency of updates.

(11) Identify need for derived relations and organize their implementation: There are cases where new relations can be derived from existing relations to satisfy application requirements efficiently. For example, requirements of sub-totals per region or branch could justify the creation of a new relation to hold those sub-totals, if the original relations have a large cardinality and the sub-total values are frequently accessed and hence calculated each time. These relations are sometimes missed during conceptual data modelling, whereas they might seem obvious when refining the logical data model based on the process model.

(12) Identify possibility of combining relations: There are situations where normalization provides a level of flexibility in the model, that is not really required. In such cases, it is often easy to find relations that need not exist in their own right and can be combined with another relation. For example, the typical address relation, which contains the addresses of each client, can be superfluous if all clients do not have more than one or two addresses. The client and address relations can be combined, but the system will be limited to a number of client's addresses, as attributes were specified in the combined relation.

(13) Identify the need for direct access between relations involved in a many-to-many relationship: In the relational model, many-to-many relationships are represented by a new relation containing the key identifiers of both relations and having, as attributes, those data elements that are representative of the relationship. These can hold large amounts of historic data making fast access to current data difficult. For example, the driver-bus relationship relation contains data on the buses assigned to drivers, with attributes such as the starting and ending date of assignment. This relation was created from a many-to-many relationship between the driver and bus relations. If we want to know the current assignment of a driver (i.e. bus #), we could implement a one-to-one direct access path between the two relations. In other words the driver relation should contain the current assignment attribute.

(14) Verify implementation of foreign keys to support referential integrity: This will verify the existence of foreign keys in dependent relations to support referential integrity, as well as to identify the need for indices to support the creation and maintenance of those foreign keys.

(15) Determine need to satisfy other special requirements from business processes: The data base designer should consider and evaluate the underlying aspects of business requirements, with the purpose of identifying the most appropriate solutions. An example is a financial data capturing system, that was intended to capture data into a transaction relation containing data representative of the financial transaction processed. Once the system was in production, it was noticed that the system was slowing down the users by using one relation to store the data captured. The performance problem was overcome by creating temporary relations for each workstation; these were copied to the permanent transaction relation at intervals, while other temporary relations were available to the users.

Most of the data obtained by following each of these design heuristics can be easily represented in a spreadsheet. For example, the spreadsheet's columns could contain the name of each relation, and the rows the transactions and/or modules names. One column entry can be created for each different access path required for a relation. In other words each relation will have as many entry columns in the spreadsheet, as there are access paths to the relation. The cell indicated by the intersection between the transaction or module (spreadsheet row) and the relation access path (spreadsheet column) should contain the number of rows in the relation that are required by the transaction or module by using that access path. This cell should also specify if the access is a query or update. While this rudimentary approach is not the solution to data base design, it can help to organize the variables involved in making decisions and also be used as documentation from the refinement process.

## 6. Summary: the design refinement process

The design heuristics presented here do not take into account complex issues such as those encountered in distributed data base design. This paper only provides a practical view of logical data base refinement before the physical design, and provides hints that should be considered in order to achieve a good data base design.

There will be some differences in the restrictions presented by different DBMSs with regard to the implementation of file locking systems, file organization systems, data access method, access optimization software, referential integrity amongst relations, etc., but the design heuristics will in the main not be affected.

We have suggested an intermediate step between logical and physical modelling; it analyses the functionality of the design with regards to the applications requirements criteria. When this step has been successfully undertaken, we should proceed to implement our logical data base model based on the output from this new step and the physical limitations and requirements of the DBMS and hardware.

The high level of complexity of the data base design problem calls for automated tools that can provide the required support to the data base designer. The data base design problem is in the class of NP-hard problems, and some of its subproblems are in the NP-complete class, since they can only be algorithmically verified in polynomial time, but not solved. This level of complexity, and need for an evolutionary approach to data base design with the aim of successfully responding to changing business environments, emphasizes the need for automated tools.

## References

[1] Ahad, R., Bapa Rao, K.V. and McLeod, D. "On Estimating the Cardinality of the Projection of a Database Relation," ACM Transactions on Databases, Vol. 14, No. 1, March 1989, pp. 28–40.

[2] ANSI/X3/SPARC Study Group Data Base Management Systems, Framework Report on Data Base Management Systems, Montvale, NJ: AFIPS Press, 1978.

[3] Arora, K.A. and Carlson, C.R. “Normalization Could be Useful,” The Computer Journal, Vol. 27, No. 1, 1984, pp. 57–61.

[4] Azar, N. and Pichat E. “Translation of an Extended Entity-Relationship Model into the Universal Relation with Inclusion Formalism,” Proceedings 5th International Conference on Entity Relationship Approach, 1986.

[5] Cerpa, N. and Dean, R. "A Review of Object Oriented Database Concepts and Their Implementation," Australian Journal of Information Systems, Vol. 1, No. 1, September 1993, pp. 13–23.

[6] Chen, P.P.S. "The Entity-Relationship Model – Towards a Unified View of Data," ACM Transactions on Database Systems, Vol. 1, No. 1, March 1976, pp. 9–36.

[7] Codd, E.F. “Further Normalization of the Data Base Relational Model,” in Data Base Systems, R. Rustin, ed., Prentice-Hall, 1972.

[8] Dabrowski, C.E., Jefferson, D.K. Carlis, J.V. and March, S.T. “Integrating a Knowledge-Based Component into a Physical Database Design System,” Information and Management, Vol. 17, 1989, pp. 71–86.

[9] Davis, K.H. “Need for ‘Flexibility’ in the Conceptual Model,” Information and Management, Vol. 18, 1990, pp. 231–241.

[10] DeMarco, T., Structured Analysis and System Specification, Englewood Cliffs, New York: Yourdon Press/Prentice Hall, 1978.

[11] Elsmasri, R. and Navathe, S.B., Fundamentals of Database Systems, New York: Benjamin/Cummings, 1989.

[12] Filteau, M.C., Kassicieh, S.K. and Tripp, R.S. “Evolutionary Database Design and Development in Very Large MIS,” Information and Management, Vol. 15, 1988, pp. 203–212.

[13] Finkelstein, S., Schkolnick, M. and Tiberio, P. “Physical Database Design for Relational Databases,” ACM Transactions on Database Systems, Vol. 13, No. 1, March 1988, pp. 91–128.

[14] Fry, J.P. and Sibley, E.H. “Evolution of Data-Base Management Systems,” ACM Computing Surveys, Vol. 8, No. 1, March 1976, pp. 7–41.

[15] Furtado, A.L., Casanova, M.A. and Tucherman, L. “The CHRIS consultant,” Proceedings of 6th International Conference on Entity-Relationship Approach, 1987, pp. 479–496.

[16] Halassy, B. “Normal Forms and Normalization: Practical Designer’s View,” Information and Software Technology, Vol. 33, No. 6, July/August 1991, pp. 451–461.

[17] McLaughlin, M.E., Hill, K.B., Brown, D.D., Rogers, M.A., Howell, A.M. and Hatch, P.P. "An Integrated Methodology and Toolset For Database Design," ACM SIGMOD RECORD, Vol. 17, No. 4, December 1988.

[18] Martin, J., Information Engineering, Vols. 1–3, Englewood Cliffs, New York: Prentice Hall, 1990.

[19] Navathe, S., Ceri, S., Wiederhold, G. and Dou, J. "Vertical Partitioning Algorithms for Database Design," Transactions on Database Systems, Vol. 9, No. 4, December 1984.

[20] Oertly, F. and Schiller, G. “Evolutionary Database Design,” Proceedings of IEEE Conference on Data Engineer

ing, February 1989, Los Angeles, California, USA, pp. 618–624.

[21] Palvia, P. “Sensitivity of the Physical Database Design to changes in Underlying Factors,” Information and Management, Vol. 15, 1988, pp. 151–161.

[22] Pangalos, G. “Logical Design of Data Base Systems,” Information and Management, Vol. 17, 1989, pp. 23–29.

[23] Pernul, G. “An Unnormalized Relational Data Model Based on User Views,” ACM SIGMOD RECORD, Vol. 16, No. 2, September 1987.

[24] Schkolnick, M. and Sorenson, P. "DENORMALIZATION: A performance oriented database design technique", in Proceedings of the AICA 1980 Congress, Bologna, Italy, AICA Brussels, 1980, pp. 363-377.

[25] Schkolnick, M. and Tiberio, P. “Estimating the cost of Updates in a Relational Database,” ACM Transactions on Database Systems, Vol. 10, No. 2, June 1985, pp. 163–179.

[26] Teorey, T.J., Yang, D. and Fry, J.P. "A Logical Design Methodology for Relational Databases Using the Extended Entity-Relationship Model," Computing Surveys, Vol. 18, No. 2, June 1986, pp. 197–222.

[27] Wiorkowski, G. and Kull, D., DB2 Design and Development Guide, 2nd Edn., New York: Addison Wesley, 1990.

![](/api/attachments/CFXCHEUX/fulltext/images/d80b49585bdab13768cc0b6636d142101b33c0699f89815e139ee15271b9143e.jpg)  
Narciso Cerpa is an Associate Lecturer in the School of Computer Science and Engineering at the University of New South Wales, in Australia. He has 15 years of business experience in software development in Chile and Australia. His research interests include software engineering methodologies, data base design, strategic technology management, and cognitive science.
