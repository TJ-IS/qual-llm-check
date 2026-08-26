---
otero_id: 21439
otero_key: "EHK8BWWV"
title: "Schema coordination in federated database management: a comparison with schema integration"
authors: "J. Leon Zhao"
year: "1997"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(97)00005-5"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Schema coordination in federated database management: a comparison with schema integration $^{1}$

J. Leon Zhao $^{a,b,*}$

$^{a}$ School of Business and Management, Hong Kong University of Science and Technology, Clear Water Bay, Kowloon, Hong Kong $^{b}$ Information and Computing Sciences Division, Lawrence Berkeley Laboratory, Berkeley, CA 94720, USA

## Abstract

We have introduced a new approach, termed schema coordination, as an alternative to the well-known schema integration approach for processing cooperative queries in federated database systems. The schema coordination approach is based on the attribute correspondence matrix that links similar attributes in all component databases. In this paper, we compare the schema coordination approach with the schema integration approach for both metadata management and cooperative query processing. We demonstrate that schema coordination offers a much simpler methodology that enables logical data independence and is especially better suited for database federations consisting of many competing databases with ever-evolving metadata. © 1997 Elsevier Science B.V.

Keywords: Federated database systems; Metadata management; Multi-organizational information systems; Query translation; Schema coordination; Schema integration; Universal relation

## 1. Introduction

The recent surge of corporate interests in electronic commerce has brought the need for interorganizational data communications to a new level of importance and urgency [1]. As a result, more and more companies are willing to put selected business data on-line to take advantage of networked electronic media such as the Internet [2-4]. The immediate consequence of this new trend is a dramatic increase in the scale of federated database manage ment systems (FDBMs). Within a single firm, the number of participating databases (or component databases) in an FDBM is usually half a dozen or so; however, in a multi-organizational environment, the number of such databases can be tens or hundreds. Conventional FDBMs have been largely based on the well-known schema integration approach, which requires the resolution of both semantic and structural differences among the component databases [5–11]. As we show in this paper, schema integration is difficult to maintain, and consequently lacks flexibility and scalability.

We have proposed a new approach, called schema coordination, as a better alternative, for federated database systems in multi-organizational environments $[12,13]$ . In this paper, we compare the main features of schema coordination with those of the schema integration approach. As detailed later, schema coordination can be regarded as the minimal mapping approach that enables data access to multiple heterogeneous databases without resorting to structural mapping between component databases.

Processing queries in a federation of multiple databases requires some form of integrated metadata in order to formulate the queries and derive the query results. As we will discuss in the body of this paper, schema coordination and schema integration provide very different solutions to metadata integration and query processing – the two fundamental aspects of the interoperability problem. The objective of this paper is to establish that schema coordination is a viable alternative, and in many cases a preferred approach to schema integration, especially in a federation of databases managed by separate organizations. Multi-organizational settings favour the schema coordination approach for two additional reasons:

1. In a multi-organizational environment, databases are competitive in nature as they frequently contain similar information, but serve separate business interests. Users of competing databases often need to know the database owners in order to access databases selectively based on some business factors. We call this issue location non-transparency, which contradicts the conventional wisdom that a distributed database management system must hide the database identity from users, i.e., the location transparency principle [14]. This traditional view came from the single organization perspective and has been the basis for schema integration. However, the location transparency principle cannot be applied to the multi-organizational environment. We show how to deal with this issue under the schema coordination approach.

2. Logical data independence is a very important issue in a multi-organizational system since its metadata can change frequently and uncontrollably for two reasons: (1) its component databases are managed autonomously by separate and competing organizations, and (2) the number of its component databases can be tens or even hundreds, and, therefore, occasional changes of metadata in each component database results in frequent changes in the metadata of the multi-organizational system. We will show that while queries under the schema integration approach may be invalidated for the change of a component metadata, the schema coordination approach ensures that all queries remain valid under any metadata changes.

The next section introduces the schema coordination approach and discusses the main ideas on its metadata model and query translation procedure. Section 3 describes the procedure of schema integration. Section 4 compares the two approaches with respect to metadata management and cooperative query processing. Their strengths and limitations are discussed in terms of the new research perspectives, namely, large federation scale, database competitiveness, and location non-transparency. Finally, Section 5 concludes the paper and indicates several research directions.

## 2. Schema coordination

Schema coordination is developed to support co-operative queries in federated database systems without integrating all database schemas into an integrated schema. Its basic premises are as follows. (1) The number of component databases in a multi-organizational environment is large so that integrating all database schemas into a single one is a formidable task. (2) The metadata of the component databases evolves constantly so that the federated metadata must be modified frequently. (3) Many of the component databases are similar and therefore competitive, and the identities of databases must be made explicit to users. (4) Similar databases cannot be merged because their identities must be maintained.

In this section, we first presents the federated metadata model and then discuss the federated query language and query translation procedure under schema coordination.

## 2.1. Metadata management

The fundamental problem of metadata management in federated database systems is to provide a single database image so that users can conduct queries without having to know the schemas of individual component databases. The schema coordination approach solves this problem by mapping the component attributes with federated attributes.

In schema coordination, federated metadata is built on a new instrument called attribute correspondence matrix (ACM), which is essentially a flat table containing all attributes in the federation. In addition to the ACM, the export schemas of component databases are also used to specify their logical data structures individually. The attribute correspondence matrix and the export schemas together represent the federated metadata needed for cooperative query processing. The ACM utilizes the notion of universal relation as the underlying concept.

## 2.1.1. Federated universal relation

Universal relation is both a concept and an implementation framework $[15–19]$ . As a concept, it refers to a super relation that is comprised of all attributes in a database. In effect, universal relation creates an illusion to the user that there is only a single relation in the database and hides from the user the existing logical database structure. As an implementation framework, universal relation provides a higher-level query language to make the database more accessible by allowing the user to mention only attribute names of interest in the query. This results in queries that are more easily written so that problems in expressing conventional SQL queries can be avoided $[20]$ .

In the schema coordination approach, we extend the universal relation concept to federated database systems. Because previous work on universal relation invariably imposes certain standards on database design, many critical concepts and constructs in the literature are rendered ineffective or invalid in the federated database system.

For purposes of discussion, we assume that there exists a federation whose members have determined the data contents to be exported to the federated database system. Furthermore, it is reasonable to assume that there exists a collection of component data dictionaries specifying the definitions of all data attributes in the federation. The first task of applying the universal relation concept is to determine the set of attributes that subsume all attributes in the federation. The equivalence among all attributes is achieved by applying the concept of attribute semantic, defined next. Once the equivalence is determined, the federated attributes can be readily named.

## 2.1.2. Attribute semantic

It is necessary to distinguish the attribute name from the attribute semantic. An attribute name is what is chosen to represent the attribute. For instance, “place of storage” can be an attribute semantic, while “warehouse” is a chosen attribute name. However, for the same example, “depot” can be used as the alternative attribute name. This states that different attribute names can be chosen for the same attribute semantic. Consequently, name conflicts occur in heterogeneous databases as their schemas are based on attribute names, not on attribute semantics.

Name conflicts can be resolved by examining the attribute semantics. A federated universal attribute (or simply federated attribute) should be named according to its attribute semantic, which should be made visible to database users. In the next subsection, we discuss how the federated attributes are derived by relating all attribute names to their attribute semantics.

## 2.1.3. Attribute correspondence matrix

Example 1. Fig. 1 illustrates a federated database system consisting of three component databases A, B, and C. Notice that there are two access paths between the Part and Manager relations in component database A. But, there are no multiple access paths between any two relations in component databases B and C.

As discussed above, the concept of attribute semantic refers to the virtue definition of the attribute. In practice, federated attribute semantics can be determined by collecting the attribute definitions in all databases, and deriving a common list of attribute definitions as the attribute semantics. For this example, we obtain the list of attribute semantics along with their given federated names (Table 1). In a real world federation, this list of attribute semantics and federated names should be obtainable based on an agreement among members of the federation. Once the federated attributes are determined, one can easily find the correspondence between the federated and component attributes by comparing their semantics.

![](/api/attachments/EHK8BWWV/fulltext/images/cf1859559e9256f6f02da1e7ab50bc60267c3914fde2bdc22f98062ba9976760.jpg)  
(c) Component Database C  
Fig. 1. Component database schemas.

The federated universal relation and all component attributes can be placed in a flat table, which will be referred to as the attribute correspondence matrix (ACM). In the matrix, the first column consists of the list of federated attributes, and the first row less the first cell contains the names (or identifiers) of all component databases. Each non-blank entry of the matrix intersects a federated attribute and a component database. An entry in the attribute correspondence matrix is blank if there is no corresponding attribute in its component database.

Table I  
The attribute semantic and federated attributes semantic

<table><tr><td>Attribute semantic</td><td>Federated name</td></tr><tr><td>Identifier of machine parts</td><td>Part ID</td></tr><tr><td>Manufacturer&#x27;s name for the part</td><td>Part Name</td></tr><tr><td>Listing price in US dollars</td><td>Price</td></tr><tr><td>Current storage location of the part</td><td>Part Store</td></tr><tr><td>Name of the storage</td><td>Store Name</td></tr><tr><td>Street address of the storage</td><td>Address</td></tr><tr><td>Name of the storage manager</td><td>Store Manager</td></tr><tr><td>Name of the team designed the part</td><td>Design Team</td></tr><tr><td>Part identifier as listed in the design</td><td>Design Part</td></tr><tr><td>Name of the manager for the design team</td><td>Design Manager</td></tr><tr><td>Name of a manager</td><td>Manager Name</td></tr><tr><td>Phone number of the manager</td><td>Phone</td></tr><tr><td>Name of the secretary for the manager</td><td>Secretary</td></tr><tr><td>Mailbox of the manager</td><td>Mailbox</td></tr></table>

Table 2 illustrates the attribute correspondence matrix for the example.

## 2.1.4. Export schemas

Schema coordination does not integrate the export schemas into an integrated one; it maintains all export schemas in a format illustrated in Table 3, using database B as an example. The export schema has three columns: (1) attribute names as they appear in the local database; (2) attribute types (key, non-key, or foreign key); and (3) attribute pointers that represent the logical database structure. To correctly construct the attribute pointers, a non-key attribute must point to its key attribute and a key attribute point to its foreign keys, if any.

## 2.2. Federated query processing

## 2.2.1. Federated SQL

The implementation of schema coordination requires an extended SQL to allow the specification of target databases in the FROM clause. This extension is a simple, but important facility as users need to query only selected component databases.

Table 2  
The attribute correspondence matrix for Example 1

<table><tr><td>Fed attribute</td><td>A</td><td>B</td><td>C</td></tr><tr><td>Part ID</td><td>Part.partID</td><td>Product.ID</td><td>Parts.part#</td></tr><tr><td>Part Name</td><td>Part.pname</td><td>Product.name</td><td>Parts.pname</td></tr><tr><td>Price</td><td>Part.price</td><td>Product.price</td><td></td></tr><tr><td>Part Store</td><td>Part.store</td><td>Product.warehouse</td><td>Parts.location</td></tr><tr><td>Store Name</td><td>Store.sname</td><td>Warehouse.wname</td><td>Depot.dname</td></tr><tr><td>Address</td><td>Store.address</td><td>Warehouse.address</td><td>Depot.address</td></tr><tr><td>Store Manager</td><td>Store.manager</td><td>Warehouse.manager</td><td>Depot.dmanager</td></tr><tr><td>Design Team</td><td>Design.team</td><td></td><td></td></tr><tr><td>Design Part</td><td>Design.partID</td><td></td><td></td></tr><tr><td>Design Manager</td><td>Design.manager</td><td></td><td></td></tr><tr><td>Manager Name</td><td>Manager.name</td><td>Manager.name</td><td></td></tr><tr><td>Phone</td><td>Manager.phone</td><td>Manager.phone</td><td></td></tr><tr><td>Secretary</td><td>Manager.secretary</td><td></td><td></td></tr><tr><td>Mailbox</td><td></td><td>Manager.box</td><td></td></tr></table>

SELECT federated attributes

FROM databases

WHERE selection and interdatabase join conditions

Although the component databases can have many structural and naming variations, the user is only required to specify the federated attributes and the component databases. The burden of translating the federated query to appropriate subqueries is therefore transferred from the user to the FDBS. As a result, the user does not have to know the structural and naming heterogeneities in component databases. In other words, the federated SQL deals with the structural heterogeneity problem by releasing the user from knowing the access paths within the same database and the naming heterogeneity problem by allowing users to use only the federated attributes.

Table 3  
Export schema for database B

<table><tr><td>B.attribute</td><td>B.type</td><td>B.pointer</td></tr><tr><td>Product.ID</td><td>Key</td><td>Product.warehouse</td></tr><tr><td>Product.name</td><td>Non-key</td><td>Product.ID</td></tr><tr><td>Product.price</td><td>Non-key</td><td>Product.ID</td></tr><tr><td>Product.warehouse</td><td>Foreign key</td><td>Warehouse.wname</td></tr><tr><td>Warehouse.wname</td><td>Key</td><td>Warehouse.manager</td></tr><tr><td>Warehouse.address</td><td>Non-key</td><td>Warehouse.wname</td></tr><tr><td>Warehouse.manager</td><td>Foreign key</td><td>Manager.name</td></tr><tr><td>Manager.name</td><td>Key</td><td></td></tr><tr><td>Manager.phone</td><td>Non-key</td><td>Manager.name</td></tr><tr><td>Manager.box</td><td>Non-key</td><td>Manager.name</td></tr></table>

Consider a federated query: “find the price of parts in databases A and B that have the same names as those stored in warehouse ‘d1’ in database C, and print the names and mailboxes of managers managing the warehouse”. Refer to Fig. 1 for the database schemas related to the query. This federated query is written as (see also Table 4):

SELECT [Part Name], [Price], [Store Manager], [Mailbox]

FROM A., B., C.

WHERE C.[Part Name] = (A,B).[Part Name]

AND C.[Store Name] = “d1”

where the federated attributes are enclosed within brackets. A database name in the FROM list is followed by a dot to indicate that it is a database, not a relation. Another unique syntax is that database names are used to represent the interdatabase join conditions. The term (A, B) denotes that joins are done between databases C and A as well as between databases C and B, and the last selection condition applies only to database C.

Notice that an access path within the same database is achieved through a foreign key join, which links a foreign key attribute, such as B.Product.warehouse, to its home key attribute, i.e., B.Warehouse.wname. Foreign key joins are the result of relational normalization and can be inferred by the system using the structural pointers in the export schemas. That is, foreign key joins are inferable because they are structure dependent. Notice that interdatabase joins do not depend on database structures, but on the user's information demand. They must be specified by users since the system has no way of knowing what is the user's intention on interdatabase joins for a particular query.

Table 4  
The query translation process

<table><tr><td rowspan="4">Query issued</td><td>SELECT</td><td>[Part Name], [Price], [Store Manager], [Mailbox]</td></tr><tr><td>FROM</td><td>A., B., C.</td></tr><tr><td>WHERE</td><td>C.[Part Name] = (A,B).[Part Name]</td></tr><tr><td>AND</td><td>C.[Store Name] = “d1”</td></tr><tr><td rowspan="6">Subquery created</td><td>DATABASE</td><td>B, C</td></tr><tr><td>SELECT</td><td>[Part Name], [Price], [Store Manager], [Mailbox]</td></tr><tr><td>FROM</td><td></td></tr><tr><td>WHERE</td><td>C.[Part Name] = B.[Part Name]</td></tr><tr><td>AND</td><td>C.[Store Name] = “d1”</td></tr><tr><td>DATABASE</td><td>B, C</td></tr><tr><td rowspan="4">Attributes converted</td><td>SELECT</td><td>C.Parts.pname, B.Product.price, B.Manager.name, B.Manager.box</td></tr><tr><td>FROM</td><td></td></tr><tr><td>WHERE</td><td>C.Parts.pname = B.Product.name</td></tr><tr><td>AND</td><td>C.Parts.location = “d1”</td></tr><tr><td rowspan="7">Intradatabase joins specified</td><td>DATABASE</td><td>B, C</td></tr><tr><td>SELECT</td><td>C.Parts.pname, B.Product.price, B.Warehouse.manager, B.Manager.box</td></tr><tr><td>FROM</td><td></td></tr><tr><td>WHERE</td><td>B.Product.name = C.Parts.pname</td></tr><tr><td>AND</td><td>C.Parts.location = “d1”</td></tr><tr><td>AND</td><td>B.Product.warehouse = B.Warehouse.wname</td></tr><tr><td>AND</td><td>B.Warehouse.manager = B.Manager.name</td></tr><tr><td rowspan="7">Source relations identified</td><td>DATABASE</td><td>B, C</td></tr><tr><td>SELECT</td><td>C.Parts.pname, B.Product.price, B.Warehouse.manager, B.Manager.box</td></tr><tr><td>FROM</td><td>B.Product, B.Manager, B.Warehouse, C.Parts</td></tr><tr><td>WHERE</td><td>C.Parts.pname = B.Product.name</td></tr><tr><td>AND</td><td>C.Parts.location = “d1”</td></tr><tr><td>AND</td><td>B.Product.warehouse = B.Warehouse.wname</td></tr><tr><td>AND</td><td>B.Warehouse.manager = B.Manager.name</td></tr></table>

## 2.2.2. Query translation

The translation of a federated query into sub-queries to component databases is done in four steps:

1. Query split. Create one subquery per group of dependent component database needed to process the subquery. The FROM clause becomes empty after a query split is done. One of the subqueries involving databases B and C is shown in the second row of Table 4.

2. Attribute conversion. For each subquery, convert each federated attribute in the SELECT and WHERE clauses to its component attribute according to the ACM. This step can be easily done by looking up entries in the attribute correspondence matrix. Row three of Table 4 shows the subquery after attributes have been converted.

3. Join specification. Determine all foreign key join conditions needed to access the attributes in the SELECT clause. Foreign key joins can be identified using the key pointers in the export schema (Table 3). For instance, given the Product.price attribute, one can find in Table 3 that it is a non-key attribute, and its key attribute is Product.ID. The Product.ID attribute, on the other hand, points to a foreign key attribute Product.warehouse, which in turn points to the key attribute Warehouse.wname. This defines a join condition “Product.warehouse = Warehouse.wname”. Similarly, another join condition is identified as “Warehouse.manager = Manager.name” as given in the fourth row of Table 4.

4. Source object identification. Extract the relation names from the component attributes found in the SELECT and WHERE clauses and place them in the FROM clause. The relation names are obtained from the component attributes found in both SELECT and WHERE clauses, and added to the FROM clause. The last row of Table 4 contains the resulting subquery in conventional SQL. The generic algorithm for query translation is presented in Fig. 2 for a federated query.

## 2.2.3. Potential ambiguous queries

Similarly, queries need to be formulated for databases A and C. From Fig. 1, it is easy to determine that there are two possible access paths between relations Part and Manager in component database A, namely:

1. Part.store $\leftrightarrow$ Store.sname $\leftrightarrow$ Store.manager $\leftrightarrow$ Manager.name

2. Part.partID $\leftrightarrow$ Design.partID $\leftrightarrow$ Design.manager $\leftrightarrow$ Manager.name

Design.manager $\leftrightarrow$ Manager.name
where the attributes are either key or foreign key attributes. Queries on this database can be potentially ambiguous because different results will be obtained depending on the access path(s) taken. The first path gives the managers who manage the storage facility where a part is stored, while the second path defines the managers who led the team that designed the part. This problem of potential ambiguous queries can be prevented using a user interface tool. This tool informs the user of the multiple access paths and their semantic meanings, and assists the user with the creation of correct federated queries [21]. The user interface must be intuitive and does not require special training to use, such as the one in [22]. The example in Table 4 is non-ambiguous because the user's intention is clearly stated in the query as “the warehouse manager”, and the federated query has restricted the access path by placing the federated attribute [Store Manager] in the federated SQL.

## 2.3. The schema coordination procedure

The procedure of schema coordination is as follows:

1. Collection of export schemas. First, each component database determines the portion of its local schema to be exported to the federation, using the format similar to the example in Table 3.

2. Determination of the federated attributes. Unique attribute semantics in all export schemas are identified, and the federated attributes are named. The set of the federated attributes institutes the federated universal relation.

3. Creation of the Attribute Correspondence Matrix. The ACM is created by (1) creating a matrix, one row per federated attribute and one column per component database, and (2) inserting each component attribute into the cell intersecting the row of the related federated attribute and the column of its component database.

4. Translation of federated queries. At the time of query, each federated query is translated into a set of subqueries using the query translation procedure in Fig. 2.

## 2.4. Basic features of schema coordination

Schema coordination approach integrates heterogeneous databases at the attribute level through the attribute correspondence matrix. In this approach, attribute equivalence is solely based on attribute semantic; that is, the domain and behavioral differences between attributes are not considered.

This approach does not try to resolve the conflicts in object names, integrity constraints, data domains, and logical database structures among component databases so as to provide interoperability without getting into the trouble of over regulating. The semantic differences are resolved by the system by annotating the resulting data with semantic information.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
1. given a federated query $Q(D, A, C)$, where $D$ is the set of component databases, $A$ is the set of federated attributes, and $C$ is the set of selection and interdatabase join conditions.
2. derive subqueries $q_i(d_i, A, C)$ for $i = 1$ to $n$, $n$ is the number of subqueries.
    IF $D$ contains no interdatabase joins, THEN $d_i$ is the $i^{th}$ component database in $D$, ELSE $d_i$ is a set of dependent component databases in $D$ with respect to the interdatabase joins in $Q$.
3. FOR EACH subquery $q_i$,
(a) FOR EACH federated attribute in $A$,
    FOR EACH database in $d_i$,
    IF the component attribute exists in the Attribute Correspondence Matrix,
    THEN convert each FederatedAttribute to its corresponding Database.Relation.ComponentAttribute
    ELSE the FederatedAttribute is ignored.
    The results of attribute conversion is $a_i$.
(b) FOR EACH federated attribute in $C$,
    FOR EACH database in $d_i$,
    IF the component attribute exists in the Attribute Correspondence Matrix,
    THEN convert each FederatedAttribute (or Database.FederatedAttribute) to its corresponding Database.Relation.ComponentAttribute
    ELSE $q_i$ is removed since its constraint cannot be evaluated.
    The results of attribute conversion is $c_i$.
4. FOR EACH $q_i$,
    FOR EACH Database in $d_i$
    FOR EACH unique attribute in $a_i \cup c_i$,
    DO a pointer chasing in its Expert Schema to identify all foreign key joins.
    append all unique joins to $c_i$.
5. FOR EACH $q_i$,
    FOR EACH unique Database.Relation expression in $a_i \cup c_i$
    append to the FROM clause of $q_i$
</div>

Fig. 2. The Generic algorithm for query translation.

Schema coordination is built on the notion of universal relation which requires the system to translate the federated SQL into subqueries in conventional SQL. The coordination approach resolves the problem of potential ambiguous queries that universal relation faces in single databases using a user-interface tool [21]. The basic idea of disambiguation is to inform the user of the multiple access paths at the conceptual level and assist the user to express the desired query.

## 3. Schema integration

This section revisits the schema integration approach in order to compare it with the schema coordination approach. Although schema integration is complex, its basic idea is to determine the differences in component schemas and to develop a unified representation in an integrated schema.

## 3.1. The schema integration procedure

We adopt the five step model of schema integration in [23], which is similar to models found in other work on schema integration such as [6,10,11].

1. Collection of export schemas. In this first step, each site decides on the subset of its local schema it is willing to share with other sites. These subsets of local schemas are referred to as export schemas.

2. Schema transformation. Each export schema is translated into an equivalent schema in an intermediate common data model. This resulting schema is called the common-model export schema. The object-oriented data models have been chosen by many as good candidates for a common data model since they are semantically rich enough to subsume most local data models.

3. Conflict identification. This is the most labour-intensive step in which all common-model export schemas are analyzed and compared to identify possible conflicts, including conflicts on naming, type, key, operations, domain, structural, and scaling [24,10]. The work involved in this step is enormous since all export schemas must be compared with one another. The total amounts of work is exponential to the number of schemas being integrated.

4. Conflict resolution. After all conflicts are identified, resolutions must be made to unify the different representations. In this step, user involvement is essential to clarify the semantics of each schema [23].

5. Schema merging. The common-model export schemas are merged into an integrated schema. Work involved in this step is not simply to gather the objects together; additional tasks are needed to guarantee completeness and correctness, eliminate duplications, and improve understandability [11].

## 3.2. A schema integration example

Next, we review the schema integration approach using two component databases: Purchase and Warehouse. Database integration is necessary in this case as the two databases are managed by separate departments.

Example 2. Fig. 3 illustrates the schema for the Purchase database in the form of entity relationship diagram. The database is composed of two objects, Company and Units, which are linked through the Produce relationship. This database contains information on the Units and on the Companies who produce the Units. The Warehouse database is given in Fig. 4, consisting of the Material and the Parts objects.

The two databases are to be integrated so that users can access information on materials, parts, and their manufacturers as though they are all contained in the same database. This example signifies a situation where information is scattered in different databases due to management and historical reasons. Notice that we are not specifying the physical data models for the Purchase and Warehouse databases, which could be relational, hierarchical, or object-oriented. We assume that the entity-relationship diagrams represent the common-model export schemas.

![](/api/attachments/EHK8BWWV/fulltext/images/43175074aff7adfc2efde209f158d067110c0e0d1621e087131679d2b3faa00e.jpg)  
Fig. 3. The purchase database schema.

Several conflicts exist in this example:

1. Structural conflict. The attribute material in the Purchase database is represented as an entity in the Warehouse database.

2. Naming conflict. The Units entity in the Purchase database is semantically equivalent to the Parts entity in the Warehouse database, and the attribute part\_ID in the Purchase database is semantically equivalent to the attribute serial# in the Warehouse database.

To integrate the two schemas, the following resolutions are done:

1. Rename the Units entity in the Purchase database to Parts.

![](/api/attachments/EHK8BWWV/fulltext/images/5e700079a9384ff8b3dba891fdd92b631c7c72587108fae6f51cacdb8817f31b.jpg)  
Fig. 4. The warehouse database schema.

![](/api/attachments/EHK8BWWV/fulltext/images/013fcfb05b5fa8d983556e5907304238251161fa9c305b6ff3c9222ca4a5769f.jpg)  
Fig. 5. The modified purchase database schema.

2. Convert the material attribute in the Purchase database into the Material entity plus the code attribute. Link the code attribute to the Material entity via the Use relationship.

3. Rename the part\_ID attribute in the Purchase database to serial#.

The resulting ER diagram is shown in Fig. 5.

Fig. 6 shows the entity relationship model after the two schemas have been merged together. This common-model integrated schema will be mapped to the implementation model chosen by each user group. For instance, the integrated model looks like the schema shown below if the relational model is the choice. Notice that the key attributes are in boldface and foreign keys are in italic.

Materials (code, name, maker, hardness, density)
Parts (serial#, weight, inventory, company\_ID, code)

Company (company\_ID, company\_name, revenue)

![](/api/attachments/EHK8BWWV/fulltext/images/f081b1fb60221e2b3e3e8f884c938ae1dcb23e553cc4f3aa5ce5dee05ca413f3.jpg)  
Fig. 6. The integrated database schema.

## 3.3. Federated query processing

The integrated schema serves the purpose of presenting the overall data contents in the system, and assists the user to create federated queries. However, each federated query must be decomposed into subqueries to its relevant component databases $[23]$ . The decomposition must be done in reference to export schemas. We omit details of the query decomposition procedure in this paper.

## 3.4. Basic features of schema integration

In the schema integration approach, an implicit assumption is that data from different databases can be merged logically into a single database. This is apparent in the example illustrated in Table 5, where schema integration is possible because the two databases are complementary. The integrated schema in Fig. 6 can present a homogeneous image of the merged data because data from the two databases collectively describe wider business operations.

Schema integration requires detailed comparison of database schemas in order to determine the heterogeneity instances in attribute and object naming and in database structures. In some research proposals, schema integration involves the comparison of attribute domain, and integrity constraints [9,25]. The amount of work in schema comparison is exponential to the number of databases, which can reach tens or hundreds in a multi-organizational environment.

Table 5  
Attribute correspondence matrix for Example 2

<table><tr><td>Fed attributes</td><td>Purchase</td><td>Warehouse</td></tr><tr><td>Company ID</td><td>Company.company_ID</td><td></td></tr><tr><td>Company Name</td><td>Company.company_name</td><td></td></tr><tr><td>Company Revenue</td><td>Company.revenue</td><td></td></tr><tr><td>Part ID</td><td>Units.part_ID</td><td>Parts.serial#</td></tr><tr><td>Part Material</td><td>Units.material</td><td>Material.code</td></tr><tr><td>Part Weight</td><td>Units.weight</td><td></td></tr><tr><td>Part Inventory</td><td></td><td>Parts.inventory</td></tr><tr><td>Part Maker</td><td>Company.company_ID</td><td></td></tr><tr><td>Material Name</td><td></td><td>Material.name</td></tr><tr><td>Material Maker</td><td></td><td>Material.maker</td></tr><tr><td>Material Hardness</td><td></td><td>Material.hardness</td></tr><tr><td>Material Density</td><td></td><td>Material.density</td></tr></table>

In the case of many similar databases, the integrated schema is merely one of the many possible representations of the database structure and names. The integrated schema must be mapped to each component schema, which is quite a challenging task. For instance, one object in the integrated schema may be represented with several objects in a component schema; conversely, several objects in the integrated schema may be subsumed by one object in another component schema. In the case of competing databases, the database identity must be made explicit to the user. All these problems makes it difficult to apply the schema integration approach.

## 4. A comparison of schema coordination and schema integration

In this section, we first define complementary and competing databases and then compare the strengths and limitations of schema coordination and schema integration based on those concepts.

## 4.1. Complementary and competing databases

From Table 2, we can see that the three databases in Example 1 contain similar data about product information. However, they differ in the levels of details captured in the database. For instance, database A contains information on design teams while database C does not. Furthermore, since these databases are assumed to belong to separate organizations, they are also competitive in nature because they provide similar information on machine parts even though the specifics of information may vary. Consequently, we can say that the databases in Example 1 are similar and competing databases.

Table 5 is the ACM for the Purchase and Warehouse databases in Example 2 (see Figs. 3 and 4). We can say that the two databases are very different: the Purchase database contains information on the manufacturers of parts while the Warehouse database contains information on the parts in storage such as inventory and material characteristics. Further, since the two databases belong to the same organization and each covers a different areas of operation, they are complementary to each other as the sum of the attributes in the two databases results in a conceptually larger database in the same organization. In this case, we say that the databases are dissimilar and complementary.

In general, users of competing databases would like to identify data ownerships in order to use the databases selectively for reasons such as quality of service. However, this violates the location transparency principle for distributed databases. Furthermore, data from competing databases cannot be merged logically into one as identities would be lost if merging is done.

## 4.2. Schema coordination versus schema integration

To provide interoperability among multiple databases, some form of metadata integration is inevitable. In the relational model, metadata is also referred to as database schemas. A database schema describes the database contents in terms of attributes (naming and semantics), objects, data domains, integrity constraints, and logical database structures [26].

Schema mapping can be done in various levels of detail. Most schema integration approach maps attributes, objects, and logical database structures [23], and some also consider data domains [9] and integrity constraints [25]. In contrast, schema coordination is a minimal mapping approach that maps only the component attributes based on semantic similarity as it: (1) does not map logical database structures in schema mapping, but uses the export schemas during query translation; (2) needs not to consider integrity constraints during schema mapping as it mainly concerns query processing while integrity concerns are mainly related to update operations; and (3) does not consider data domains but annotates differences in data domains when presenting the query results to the user [13].

Table 6 highlights the basic features of schema coordination and schema integration that are considered important to users, developers, and administrators of federated database systems. A more detailed comparison on these factors are given below:

\- Schema mapping tasks. As explained above.

Table 6  
A comparison of basic features between schema coordination and schema integration

<table><tr><td></td><td>Schema coordination</td><td>Schema integration</td></tr><tr><td>Schema mapping tasks</td><td>Attribute mapping only</td><td>Attribute mapping;object mapping;structural mapping</td></tr><tr><td>Query processing tasks</td><td>Attribute conversion;Structural retrieval</td><td>Attribute conversion;structural conversion</td></tr><tr><td>Types of databases</td><td>Competing databases; complementary databases</td><td>Complementary databases</td></tr><tr><td>Logical data independency</td><td>High</td><td>Low</td></tr><tr><td>Extensibility</td><td>Need to add new columns in ACM</td><td>Must modify the integrated schema</td></tr><tr><td>Scalability</td><td>Need to organize conceptually the federated attributes</td><td>Challenged for dynamic environment</td></tr><tr><td>Maintenance</td><td>ACM can be modified using simple SQL</td><td>Integrated schema is more complex to modify</td></tr><tr><td>Administration</td><td>Autonomous databases</td><td>Semi-autonomous databases</td></tr></table>

schema coordination only maps the attributes in component databases to the federated attributes; in contrast, schema integration not only maps attributes, but also objects. Furthermore, schema integration must resolve structural conflicts as well when creating the integrated schema. The fundamental assumption in schema integration is that a query written with respect to the integrated schema can be easily translated into queries for individual component schemas; this has not been proven theoretically or empirically. Although not shown in the table, both schema coordination and schema integration require some forms of export schemas.

Query processing tasks. For query processing, both schema coordination and schema integration need to convert federated attributes to their local counterparts. Schema coordination does this through the attribute correspondence matrix (ACM), while schema integration maintains the mapping information in its integrated schema. The main difference is that schema coordination uses the database structures in the export schemas on an individual basis for query translation, whereas schema integration combines component schemas into an integrated database structure. In comparison, schema coordination does much less work than schema integration at the metadata management stage since it uses the minimal mapping approach. The implication is that metadata management in schema coordination is much simpler since initialization and maintenance of the federated metadata in a flat table are quite straightforward. However, schema coordination does pay a price for the problem of potential ambiguous queries that require additional solutions as outlined in Section 2.

\- Types of databases. As discussed in the previous subsection, schema coordination is suitable for complementary databases as well as competing databases; however, schema integration can only be used for complementary databases. This leads to the conclusion that schema coordination has a broader application domain than schema integration.

\- Logical data independency. Schema coordination can support high logical data independence because its query translation algorithm take into account changes in federated metadata automatically. Therefore, modifications to existing databases or additions of new databases do not affect existing queries. The key point is that the federated schema in schema coordination is based on universal relation and therefore have a simple and stable logical structure. In contrast, queries in schema integration have low logical data independence since modifications to database structures in component schemas can lead to changes to the structure of the integrated schema, making existing federated queries obsolete.

Extensibility. Schema coordination has high extensibility as adding a new database amounts to adding a new column to its ACM. Furthermore, the addition of a new database does not affect other existing databases, and therefore, new databases can be added without disturbing continuous database operations. When a new database is added, it can be put in use instantaneously by simply informing the query translator the new column in the ACM. In contrast, under schema integration, adding a new database to an integrated schema is more complex. This is because addition of subschemas may alter the integrated schema as illustrated in Section 3. Switching over to the newly integrated schema may require the modification of existing queries and applications as the logical data independence is not guaranteed. Consequently, schema coordination is likely to offer better extensibility than schema integration.

Maintenance. In schema coordination, flat tables are used for the attribute correspondence matrix and the export schemas, and therefore naming and structural changes can be easily made by relational operations. In contrast, modifying the integrated schema in schema integration is more complex and requires elaborate procedures.

Scalability. The scalability of schema coordination and integration are bounded by different factors. Schema coordination can be potentially scaled to hundreds of component databases due to its simple and adaptive metadata structure. However, since its ACM is based on the universal relation concept, it needs to organize the federated attributes for ease of understanding when the number of attributes gets very large. Solution is being developed based concept hierarchies that is not confined to any specific logical database structure [21]. On the other hand, schema integration is bounded by the ability to integrate and manage a large integrated schema. The primary challenge to the schema integration approach is to maintain integrated schemas for large and dynamic federations consisting of many databases with ever evolving metadata.

\- Administration. Schema integration based approaches invariably impose certain restrictions to the modifications of component schemas to ensure that the integrated schema is manageable. This can be said to be semi-autonomy, which is tolerable as most schema integration examples in the literature have been for single organizations. On the other hand, schema coordination can afford a high degree of freedom to its component databases since the export schemas are not integrated into its federated metadata. Consequently, it is expected that administration of the federated databases in schema coordination would be less complex than in schema integration.

In summary, schema integration applies the same metadata paradigm as single databases to the multiple database environment. Its strength is that the conventional database management facilities can be easily extended to heterogeneous databases. However, the weaknesses of schema integration stems from the fact that managing changes to schemas are more complex and difficult, thereby resulting in more complex maintenance and administration procedures, and low logical data independence, extensibility and scalability. Conversely, schema coordination takes a minimal mapping paradigm that is designed to reduce the complexity of integrating databases for query purposes. Its strength lies in its simpler maintenance and administration procedures, leading to high logical data independence, extensibility and scalability. However, schema coordination cannot be used to support updates to component databases using the federated metadata as it is not designed to do so. Furthermore, the query translation process may be less efficient in schema coordination since it requires the access of logical database structures in individual export schemas. All in all, schema coordination supports a loose integration of heterogeneous databases so that it is more flexible and more suited for dynamic situations, whereas schema integration supports a tight integration and is therefore more rigid and harder to deal with frequent changes.

## 5. Conclusions

The advent of electronic commerce has made the interoperability of databases in multiple organizations a critical issue. Meanwhile, the typical size of federated database systems has increased from a half dozen databases in a single organization to hundreds of databases in multiple organizations. Consequently, interoperating heterogeneous databases in a large and dynamic environment is challenging the feasibility of the well-known schema integration approach.

In this paper, we introduced the schema coordination approach, a new methodology for processing cooperative queries in a multi-organizational environment. The novelty of this new approach is its minimal schema mapping paradigm based on the notion of universal relation, thus accomplishing database integration without resolving conflicts in logical database structures and in other factors such as data domains and integrity constraints.

The main advantages of schema coordination in comparison to schema integration are: (1) it has a simple format for its federated metadata and is therefore easy to maintain; (2) its federated SQL is user-friendly as users do not have to know the heterogeneous database structures; (3) it achieves logical data independence for the federated queries because the system can adopt schema changes automatically through query translation; and (4) it is suitable for a multi-organizational environment with a large number of ever-changing component schemas because of its simple format, high scalability, and logical data independence.

Additional work is being pursued in the following directions: (1) an analysis of the schema coordination approach for more complex database systems in a business environment; (2) an experimental demonstration that schema coordination is cost effective and flexible; and (3) an implementation of the schema coordination approach in a prototype system.

## References

[1] J.M. Tenenbaum, C. Medich, A.M. Schiffman, W.T. Wong. Commercenet: spontaneous electronic commerce on the internet. Digest of Papers, COMPCON'95: Technologies for the Information Superhighway, IEEE Computer Society Press (1995) 38–43.

[2] C. Cunningham, C. Tynan, Electronic trading, inter-organizational systems and the nature of buyer-seller relationships: the need for a network perspective, International Journal of Information Management 13 (1) (1993) 3–28.

[3] V. Grover, An empirically derived model for the adoption of customer-based interorganizational systems, Decision Sciences 24 (3) (1993) 603–640.

[4] N.S. Levinson, Interorganizational information systems: new approaches to global economic development, Information and Management 26 (5) (1994) 257–263.

[5] R. Ahmed et al., The Pegasus heterogeneous multidatabase system, IEEE Computer 24 (12) (1991) 19–27.

[6] M. Batini, C. Lenzirini, S.B. Navathe, A Comparative Analysis of Methodologies for Database Schema Integration, ACM Computer Surveys 18 (4) (1986) 323–363.

[7] Y. Breitbart, Multidatabase Interoperability, ACM SIGMOD Record 19 (3) (1990) 53–60.

[8] Y. Breitbart, P.L. Olson, G.R. Thompson, Database integration in a distributed heterogeneous database system. Proceedings of the Second International Conference on Data Engineering, February 1986, pp. 301–310.

[9] J.A. Larson, S.B. Navathe, R. Elmasri, A theory of attribute equivalence in databases with application to schema integration, IEEE Transactions on Software Engineering 15 (4) (1989) 449–463.

[10] M.P. Reddy, B.E. Prasad, P.G. Reddy, A. Gupta, A methodology for integration of heterogeneous databases, IEEE Transactions on Knowledge and Data Engineering 6 (6) (1994) 920–933.

[11] A.P. Sheth, J.A. Larson, Federated database systems for managing distributed heterogeneous, and autonomous databases, ACM Computer Surveys 22 (3) (1990) 183–235.

[12] J.L. Zhao, Schema coordination in federated database systems. Proceedings of the 4th Annual Workshop on Information Technologies and Systems (WITS'94), Vancouver, December 1994.

[13] J.L. Zhao, A. Segev, A. Chatterjee, A universal relation approach to federated database management. Proceedings of the 11th International Conference on Data Engineering, Taipei, Taiwan, March 1995.

[14] D.M. Kroenke, Database Processing. Prentice Hall, Englewood Cliffs, NJ, 1995.

[15] V. Brosda, G. Vossen, Update and retrieval in a relational database through a universal schema interface, ACM Transactions on Database Systems 13 (4) (1988) 449–485.

[16] T.-H. Chang, E. Sciore, A universal relation data model with semantic abstractions, IEEE Transactions on Knowledge and Data Engineering 4 (1) (1992) 23–33.

[17] R. Fagin, A.O. Mendelzon, J.D. Ullman, A simplified universal relation assumption and its properties, ACM Transactions on Database Systems 7 (3) (1982) 343–360.

[18] F. Leymann, A survey of the universal relation model, Data and Knowledge Engineering 4 (1989) 305–320.

[19] D. Maier, J.D. Ullman, Maximal objects and the semantics of universal relation databases, ACM Transactions on Database Systems 8 (1) (1983) 1–14.

[20] D. Greenblatt, J. Waxman, A study of three database query languages, in: B. Schneiderman (Ed.), Database: Improving

Usability and Responsiveness Academic Press, New York, 1987.

[21] J.L. Zhao, A. Segev, A. Chatterjee. A coordination-based query processing paradigm for interorganizational information systems. Technical Report LBL-38135, Lawrence Berkeley National Laboratory, CA 94720, 1996.

[22] D. Maier, D. Rozenshtein, S. Salveter, J. Stein, D.S. Warren, PIQUE: a relation query language without relations, Information Systems 12 (3) (1987) 317–335.

[23] M.N. Kamel, N.N. Kamel, Federated database management system: requirements, issues and solutions, Computer Communications 15 (4) (1992) 270–278.

[24] W. Kim, J. Seo, Classifying schematic and data heterogeneity in multidatabase systems, IEEE Computer 24 (12) (1991) 12–18.

[25] V. Ramesh, S. Ram, A methodology for interschema relationship identification in heterogeneous databases. Proceedings of the 28th Hawaii International Conference on System Sciences, vol. 3, January 1995, Wailea, Hawaii, pp. 263–272.

[26] J.D. Ullman, Principles of Database and Knowledge-base Systems, vol. I, Computer Science Press, 1988.

![](/api/attachments/EHK8BWWV/fulltext/images/a4e92ed7491841f4dbd8342cbb8775e558185cd4b844d730253dae704f5976c0.jpg)

Dr. J. Leon Zhao is currently an Assistant Professor at the Department of Information and Systems Management, School of Business and Management, the Hong Kong University of Science and Technology (HKUST). He graduated from the Haas School of Business, University of California, Berkeley in 1992 and taught at the School of Business, the College of William and Mary before joining HKUST. He has published in Management Science, IEEE

Transactions on Knowledge and Data Engineering, Journal of Intelligent Information Systems as well as in numerous refereed conference proceedings such as Very Large Data Bases, Data Engineering, Information and Knowledge Management, Scientific and Statistical Database Management, and the Hawaii International Conference on Systems Sciences. His research interests include Intelligent Information Systems, Heterogeneous Database Systems, Workflow Management, and Electronic Commerce.
