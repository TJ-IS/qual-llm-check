---
otero_id: 26422
otero_key: "KHM8QQ2H"
title: "On Heterogeneous Database Retrieval: A Cognitively Guided Approach"
authors: "Ramayya Krishnan; Xiaoping Li; David Steier; Leon Zhao"
year: "2001"
journal: "Information Systems Research"
doi: "10.1287/isre.12.3.286.9711"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/KHM8QQ2H/fulltext/images/fcfeba63de7ac294b594fe0fbbd7451017962fce90fca0f448c80c71c90a6064.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# On Heterogeneous Database Retrieval: A Cognitively Guided Approach

Ramayya Krishnan, Xiaoping Li, David Steier, Leon Zhao,

To cite this article:

Ramayya Krishnan, Xiaoping Li, David Steier, Leon Zhao, (2001) On Heterogeneous Database Retrieval: A Cognitively Guided Approach. Information Systems Research 12(3):286-301. http://dx.doi.org/10.1287/isre.12.3.286.9711

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 2001 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/KHM8QQ2H/fulltext/images/ea795f2f8d424d47aadf49c416eda55a0e41a6326f05bcc4f7fc3bdeb5ba03c6.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# On Heterogeneous Database Retrieval: A Cognitively Guided Approach

Ramayya Krishnan • Xiaoping Li • David Steier • Leon Zhao

The Heinz School, Carnegie Mellon University, Pittsburgh, Pennsylvania 15213

AT&T (China) Company, Bright China Chang An Building, Number 7 Jianguomen Nei Avenue, Beijing 100005 PRC Scient Incorporated, 1 Market Street, San Francisco, California 94105

Department of Management Information Systems, Eller College of Business and Public Administration, The University of Arizona, Tucson, Arizona 85721 rk2x@cmu.edu • lzhao@bpa.arizona.edu

R <sup>etrieving</sup> <sup>information</sup> <sup>from</sup> <sup>heterogeneous</sup> <sup>database</sup> <sup>systems</sup> <sup>involves</sup> <sup>a</sup> <sup>complex</sup> <sup>process</sup> and remains a challenging research area. We propose a cognitively guided approach for developing an information-retrieval agent that takes the user’s information request, identifies relevant information sources, and generates a multidatabase access plan. Our work is distinctive in that the agent design is based on an empirical study of how human experts retrieve information from multiple, heterogeneous database systems. To improve on empirically observed information-retrieval capabilities, the design incorporates mathematical models and algorithmic components. These components optimize the set of information sources that need to be considered to respond to a user query and are used to develop efficient multidatabaseaccess plans. This agent design, which integrates cognitive and mathematical models, has been implemented using Soar, a knowledge-based architecture.

(Global Query Optimization; Heterogeneous Database Systems; Information Integration; Maximal Objects; Soar-Based AI Systems; Universal Relational Model)

## 1. Introduction

The Internet has made the multidatabase problem (i.e., retrieving data from multiple databases) more relevant and challenging. Retrieving information from multiple databases generally involves complexities that do not exist when retrieving information from a single database (Kim et al. 1991). First, query formulation requires knowledge of multiple databases to identify the database sources required to answer the query. Second, dataaccess planning (also referred to as data-access path selection in the database literature) in a multidatabase environment is more complex than in a single database because the order in which information is accessed from multiple component databases can have critical performance implications.

Building on the mediator-based approach (Wiederhold

1992), we propose novel solutions at the logical design level to these two key problems encountered in the development of information-retrieval agents.<sup>1</sup> In contrast to previous work on this topic, our proposals are based on an empirical model of how human experts retrieve information from multiple heterogeneous databases. However, for a variety of well-known reasons, such as bounded rationality, human experts do not display “optimal” problem-solving behavior (Simon 1955). To deal with this limitation, we develop mathematical optimization algorithms and incorporate them into the human process model of information retrieval. To set the context for the rest of the paper, we begin with an example that illustrates the capabilities we desire in our information retrieval agent, InfoB (short for Information Broker).

Consider a set of autonomous relational databases, MillionDollarDirectory, Manufacturers, Distributors, and Bank, whose schemata are shown in Figure 1. For convenience, we refer to this set of component databases as the “commerce-component databases” as they can be used to support commercial transactions.

To find all computer manufacturers whose gross sales are greater than 100 million, the user formulates a query that retrieves “Large Computer Manufacturers” as shown in Figure 2. This query is submitted to InfoB.

Note that the SQL query does not contain the FROM clause. The user, therefore, is not required to be aware of the logical structure of the component databases.

## Figure 1 The Commerce-Component Databases

MillionDollarDirectory Company(Cname, Caddress, Ccity, Czip, Cphone, CEO\_name, SIC, GrossSales, Employee)

Manufacturers Manufacturer(Mname, Maddress, Mcity, Mzip, Mphone#, Mfax#, SIC) Produces(Mname, P#, Annual-Quantity, Mcost) Product(P#, Pname, Pspec) Hires(Mname, CEO-name, Time-period, Salary) CEO(CEO-name, Gender, Age, Education)

Distributors Distributor(D#, Dname, Daddress, Dcity, Dzip, Dphone#, Dfax#) Carries(D#, P#, Mname, Sale-price)

Bank Customer(CusName, CusAdd) Account(Account#, Balance) Keep-account (CusName, Account#) Loan(Loan#, Loan-amount) Take-loan(CusName, Loan#) AcBr(Ac#, Branch#) Lbr(Loan#, Branch#)

## Figure 2 User Query 1—“Large Computer Manufacturers”

<table><tr><td>SELECT</td><td>Company_name</td></tr><tr><td>WHERE</td><td>Company_name = Manufacturer_name</td></tr><tr><td>AND</td><td>Product_name = “Computer”</td></tr><tr><td>AND</td><td>GrossSales &gt; 100,000,000</td></tr></table>

Information Systems Research Vol. 12, No. 3, September 2001

InfoB processes the query and solves the database source identification problem—namely identification of the databases and the specific data objects that need to be accessed to answer the query. For the query in Figure 2, InfoB identifies the MillionDollarDirectory and Manufacturers databases and the tables in these databases as relevant, and formulates the query shown in Figure 3.

We refer to this query as a global query because it references data objects in more than one database. For this reason, it cannot be evaluated directly in a single conventional database. To evaluate the global query, InfoB develops an access plan. It decomposes the global query into subqueries that can be evaluated on each of the relevant databases. It then determines the order in which they should be evaluated and how their results should be combined to respond to the global query. These subqueries are shown in Figure 4. InfoB returns the intersection of the set of company names and manufacturer names determined by these queries as the response to the user query in Figure 2.

Several questions need to be answered to endow

<table><tr><td>Figure 3</td><td>The Global Query for “Large Computer Manufacturers”</td></tr><tr><td>SELECT</td><td>Cname</td></tr><tr><td>FROM</td><td>MillionDollarDirectory.Company,Manufacturers.Manufacturer, Manufacturers.Product,Manufacturers.Produces</td></tr><tr><td>WHERE</td><td>Company.Cname = Manufacturer.Mname</td></tr><tr><td>AND</td><td>Product.Pname = “computer”</td></tr><tr><td>AND</td><td>Company.GrossSales &gt; 100,000,000</td></tr><tr><td>AND</td><td>Manufacturer.Mname = Produces.Mname</td></tr><tr><td>AND</td><td>Produces.P# = Product.P#</td></tr></table>

## Figure 4 Subqueries of “Large Companies” and “Computer Manufacturers”

Subquery 1 (Large Companies): SELECT Cname FROM MillionDollarDirectory.Company WHERE Company.GrossSales  100,000,000

Subquery 2 (Computer Manufacturers): SELECT Mname FROM Manufacturers.Manufacturer, Manufacturers.Product, Manufacturers.Produces WHERE Manufacturer.Mname - Produces.Mname AND Product.Pname - “computer” AND Produces.P# - Product.P#

InfoB with the capabilities illustrated in this example.

1. What knowledge should InfoB have about the component databases for which InfoB serves as a retrieval mediator, and how should this knowledge be structured? How should the different types of knowledge be organized to architect and implement InfoB?

2. Given this knowledge, how should InfoB determine the minimal set of data sources required to answer a given user query correctly?

3. How should InfoB evaluate global queries on these identified data sources to answer the user query?

We use a combination of methods to answer these questions:

• (Question 1) We use the results of an empirical study of information retrieval by human experts to identify the different types of knowledge required by InfoB. This includes metaknowledge about the component databases as well as process knowledge about the key steps involved in answering a user query. The representation scheme used to encode metaknowledge about component databases is derived from the universal relational model (Ullman 1989, Zhao et al. 1995). The process knowledge is encoded using the problem space model provided in Soar (Laird et al. 1983, Newell 1990).

• (Question 2) To improve the efficiency of datasource identification, we develop mathematical models and algorithmic components to determine the minimal set of data sources that are required to answer a user query correctly and efficiently. The models employ constructs derived from the Universal Relation Model, such as the maximal object and global hypergraph, and take into account the cost differences between interdatabase and intradatabase queries (Lu et al. 1992).

• (Question 3) The evaluation of a global query involves the formulation of an access plan. We propose a knowledge-based approach to query evaluation, based on observed human behavior, and we implement it in the Soar development environment.

The rest of the paper is structured as follows: §2 provides an overview of several preliminary concepts including database-integration methodologies, the Universal Relation Model, our protocol analysis of human experts, and the InfoB problem space model. Section 3 discusses the knowledge architecture underlying InfoB. Section 4 describes the global universal relation used to represent the data sources in InfoB. Section 5 presents the mathematical models for the data-source identification problem. Section 6 overviews the statespace approach to access planning for global queries. Section 7 presents our work on validating InfoB through a comparison of its results with the results observed of human experts. Section 8 discusses the contributions and limitations of our study and outlines future research directions.

## 2. Preliminaries

## 2.1. A Brief Literature Review

There has been considerable interest, in both the practitioner and research communities, in addressing the problems encountered in retrieving information from multiple heterogeneous databases. Recent work in this area has focused primarily on problems related to schematic database heterogeneity (Singh 1998) and can be characterized into two broad streams: tight coupling and loose coupling approaches.

The tight coupling approach relies on integrateddatabase schemata. When the multidatabase system is created, a global/integrated schema or a federation of shared schemata are generated by the systems integrator (Sheth and Larson 1990, Zhu and Larson 1996). Examples of such systems include Multibase, Mermaid, Adds, Dataplex, Ingres/Star, Pegasus, WIND, and MDM (Ahmed et al. 1991, Bright et al. 1992, Mostardi and Siciliano 1994, Atzeni and Torlone 1997).

The advantage of the tight coupling approach is that it allows users to transparently access heterogeneous, autonomous, and distributed databases as they would a single database. However, implementing such an approach can be costly. The integrated schema must be redone each time there is a change in the schema of an existing component database or when a new database is added to the accessible pool. This makes the maintenance of the global schema very difficult. In an environment as dynamic as the Internet, it is virtually impossible to maintain such a global schema (Duschka and Genesereth 1997).

In contrast to the tight coupling approach, the loose coupling approach leaves the task of integration to the multidatabase users. Systems adopting this approach aim to provide tools to facilitate the integration task to be carried out by the user. Examples of such tools include the MultiDatabase manipulation language MDSL (Litwin and Abdellatif 1987), ALCHEMIST, an object-oriented tool to build transformations among heterogeneous-database representations (Henry and Lind 1994), and the InfoSleuth project (Bayardo et al. 1997), a system for finding and integrating information in corporate and external networks. Although this approach is very flexible in updating the component databases, it is essentially impossible to find users with all the knowledge required to perform the query formulation task when the number of component databases is large and varying.

The mediation/knowledge-based approach (Jeff and Tenenbaum 1991, Wiederhold 1992) combines elements of both the tight and loose coupling approaches. The basic idea is to replace the global schema with a knowledgeable mediator, primarily to support information retrieval. A mediator or agent in this context is defined as “a software module that exploits encoded knowledge about a certain set of databases to create information for a higher layer of applications” (Wiederhold 1992). It relieves the user from having to deal with database heterogeneity. The user interacts with an agent and expresses information requests in the agent’s language (e.g., modified version of SQL). As illustrated in our motivating example, this only requires domain knowledge (Arens et al. 1993, Kashyap and Sheth 1994). Recently, the mediator-based approach has been applied to address the problem of accessing information sources that contain structured as well as unstructured data (Garcia-Molina et al. 1995, Hammer et al. 1997, Naacke et al. 1998, Vidal et al. 1998).

The applicability of the three approaches described above is determined by the size of the database pool, the extent of heterogeneity, the stability of the databases, and the level of sophistication of the users. In general, the tight coupling approach can be used in an environment where there is a small number of databases whose data schemata do not change much over time, while the loose coupling approach requires sophisticated users or users with the support of database experts. In a dynamic environment such as the Internet, where the number of databases is large and ever changing and users are not sophisticated enough to maintain their own schemata, the knowledge-based mediator approach appears to be the most appropriate. This paper uses a mediator-based approach to design and implement an information-retrieval agent.

## 2.2. The Human Multidatabase Access Model

The process of accessing multiple heterogeneous databases is a knowledge-intensive task. Humans perform this task well. However, a systematic study of how human experts retrieve information from multiple data sources has not been conducted. We conducted protocol analysis to understand both the processes and knowledge used by human experts when retrieving information from multiple databases. The results of the study were used to guide the design of InfoB. Due to space limitations, we highlight the basic findings of the study. Details related to the experiments and the analysis of how human experts access multiple, heterogeneous databases can be found in Li (1996).

2.2.1. Experimental Design. Two database experts participated in the study, a consultant and a professor of database systems. Two experiments were conducted per expert.<sup>2</sup> Five relational databases were used in the experiment. The schemata of four of these five databases is shown in Figure 1. The fifth schemata is not included in the paper because of space limitations. The interested reader is referred to Li (1996). In each experiment, the expert was asked to answer two queries. An example query is shown below.

Example Query. Find a manufacturer who has less than 100 employees but whose total assets in 1993 exceed \$10,000,000.

To understand how schema information was being processed, in the first experiment, database and table names were replaced with abstract symbols (e.g., T45, D23 were labels used to identify a table or a database). However, attribute names (e.g., customer\_name) were not modified. In the second experiment, the experts had access to the schema information without any modifications. We discovered that in both experiments, experts identified relevancy of information sources by matching attribute names in the user query with those in the database schemata.

To observe if different strategies in access planning might be employed with or without physical access to the databases, Expert 1 was asked to answer the queries in the form of an access plan, while Expert 2 was asked to retrieve the data online from databases. In the case of Expert 2, the databases were stored on separate diskettes. He was instructed to treat these databases as being accessible only from different machines. No two databases could be obtained at the same time. The schemata of these databases and two query questions were also given in hard copy. The goal was to try to simulate the cost of accessing each database, thereby providing the expert with incentives to use the minimal set of data sources required to answer a query. We discovered that the experts did not optimize their access plans and used a heuristic process.

2.2.2. Summary of Findings. Throughout the experiments, the experts were asked to vocalize and were videotaped. The verbalizations were transcribed into a sequence of protocol segments. Each segment was assigned a number to record the action sequence. A human multidatabase-access model was then developed based on the analysis of the verbal protocols as shown in Figure 5. The rectangles indicate different processes in the life cycle, while the round-cornered rectangles indicate the subprocesses within a process.

• Task-formulation process. At the start of this process, the information request was given to the human experts as English text. The experts identified a variety of information about the problem while reading the text, and then represented this information in a symbolic form (e.g., a connected graph).

• Target-table identification process. In this process, the experts took the data attributes mentioned in the information request and searched for tables that contained the same attributes. This attribute-matching behavior was observed in all the experiments. The knowledge used in this process consisted of the metainformation about each database and simple pattern matching.

• Access-planning process. Having identified one or more target tables that may be distributed over several databases, experts formed an overall access plan or a global query using a heuristic process. As noted, no attempt was made to optimize the plan.

• Plan-execution process. This is the process where data were actually obtained. Each database was accessed separately to meet conditions specified in the information request, such as “asset - 10 million.”

• Goal-testing process. This was observed in both experts, although their task requirements were somewhat different. Expert 1 was asked to form an access plan, while Expert 2 was asked to actually retrieve the data. Nevertheless, both experts attempted to confirm that the results of their work satisfied the information request.

The protocol analysis provided us with a detailed understanding of the overall process, the symbolic representations employed, and the types of knowledge used in the various steps of the information-retrieval process. This guided the development of the InfoB architecture in Soar (§3).

## 2.3. An Overview of Soar

Soar is both an AI architecture that supports a wide range of tasks (Rosenbloom et al. 1985) and a unified theory of cognition that has been used to explain data on human performance (Newell 1990). For the purposes of this paper, Soar can be thought of as a shell for developing knowledge systems. It has been used widely over the last 15 years for this purpose. Recent agent-based systems developed using Soar include Robocup (a soccer-playing agent, Marsella et al. 1998) and an agent designed to simulate military combat (Hill et al. 1997).

Figure 5 Human Information-Access Processes  
![](/api/attachments/KHM8QQ2H/fulltext/images/724a7efe74ab6be8a577fe678feb96fb6f57ca8ed881ba15dc638a713b087751.jpg)

The Soar environment supports a language and a collection of reasoning mechanisms based on three key concepts:

• Soar theory dictates that all problem solving takes place in problem spaces. A problem space, like in traditional state-space search, consists of an initial state, a goal state, and a collection of operators that represent the means to accomplish the task. Applying an operator to a state generates a new state. Problem solving is accomplished by searching from a given initial state in the problem space, through intermediate states generated by operators, until a desired state is reached. Operators are implemented as production rules in Soar.

• In contrast to traditional state-space search, problem solving in Soar can encounter and resolve impasses. As such, impasses are modeled explicitly in Soar. An impasse arises when there is insufficient knowledge to proceed with problem solving. Impasses are resolved in a new problem space—spawned as a child of the space in which the impasse was encountered. This strategy for dealing with impasses requires a problem-decomposition approach, leading to the development of a problem-space hierarchy.

• Finally, Soar provides support for learning through a mechanism called chunking. A chunk is knowledge—represented as a production rule in a problem space—learnt from the child problem space in which an impasse is resolved.

To develop a system using Soar, a problem-space hierarchy is formulated that captures the process and the organization of knowledge used to solve a problem. Soar provides a language to state these problemspace models and provides a production rule-based system to implement operators. In our implementation of InfoB, the problem-space model encapsulated the information-retrieval process observed in the protocol analysis. The states in the problem spaces encode knowledge about the information sources. InfoB uses constructs derived from the Universal Relation Model for this purpose.

## 2.4. The Universal Relation Model

The Universal Relation Model is intended to provide the database user with a simplified model with which to compose queries without regard to the underlying structure of the relations in the database (Chang and Sciore 1992, Maier and Ullman 1983, Lee et al. 1993, Ullman 1989). This model is especially attractive in a dynamic multidatabase environment, where the user is neither aware of which databases are likely to be relevant, nor are they aware of their underlying database structures.

To ensure that a set of attributes in the user query uniquely determine the answer to a user’s request in the multidatabase system, the Universal Relation Model adopts the relationship uniqueness assumption (Ullman 1989) as given below:

Relationship Uniqueness Assumption. For any two entities A and B in a given set of databases, if there exists a relationship between A and B, there exists one most basic relationship R.

The relationship-uniqueness assumption does not preclude the existence of multiple relationships between two entities in a database, but rather emphasizes that one of the relationships is the most basic one. For instance, between employees and managers, the most basic relationship is that of “manages.”

The Universal Relation Model requires the computation of maximal objects (Maier and Ullman 1983). A set of tables is referred to as a maximal object if joins over these tables or some subset of them are lossless (Ullman 1989). The Universal Relation Model introduces a hypergraph representation of a database scheme and supplies an algorithm that uses information about functional and join dependencies to compute maximal objects in a database. Next, we illustrate the concept of maximal objects; its formal definition is found in Ullman (1989).

Figure 6 illustrates the bank-database schema of Figure 1. The attributes of the bank database form a cyclic hypergraph. Two maximal objects, M1 and M2 (shown by dotted lines), are obtained; each contains

![](/api/attachments/KHM8QQ2H/fulltext/images/3bf69d5ab8f0abd3a0ebcd2322a7914d0edb63a2e4f182715f96815bfc7a1789.jpg)

A → B, BAL L → B, AMT C → ADR

an acyclic hypergraph. While the relationshipuniqueness assumption does lead to certain restrictions on the applicability of the Universal Relation Model, researchers have found that through proper design of the database using semantic abstractions (i.e., object aggregation), the Universal Relation Model can be very effective in many applications (Chang and Sciore 1992).

## 3. The Design of InfoB

As discussed in §§2.2 and 2.3, the problem-space model encodes the process knowledge used in InfoB. Figure 7 shows a fragment of the problem-space model. We formulated the model using the results of the human study. The model organizes the knowledge required to perform the information-retrieval task in a modular manner, with each problem space encapsulating the knowledge required to perform specific tasks.

The Task space is where the information-retrieval task starts and ends. The initial state in this space is the user’s information request and the metainformation about each of the information sources. We refer to this metainformation as source models. There are four operators in this space, Process-database-information, Identify-targets, Form-an-access-plan, and Execute-plan. These correspond to the four main level tasks observed in our study of human experts. The Process-databaseinformation operator maps the source models into hypergraphs of the Universal Relational Model. The other three operators map directly to the processes of

Target-Table-Identification, Access-Planning, and Plan-Execution in the human multidatabase-access model given in §2.2. These three operators are implemented in the Target space, the Plan space, and the Execution space (as shown in Figure 7), respectively.

The goal of the Target space is to identify the information targets necessary to answer the user query. Note that a target-attribute is an attribute mentioned in the user query that exists in a relational database, and a target is a table that contains at least one targetattribute in the user’s request. The operators in this problem space are the Identify-target-attr operator, which gathers all the attributes mentioned in the user query, the Identify-target operator, which matches the target attributes to the database attributes, and the Add-target operator, which adds the matched target to the Target\_list. The final state of this problem space is a list of target tables. The attribute-matching method is based on the behavior observed in the expert study.

The goal of the Plan space is to implement the Forman-Access-Plan operator of the Task space. This module is not based on the empirical study of human experts, but uses mathematical models and computational algorithms described in §5. The initial state of this problem space contains the source models, a list of targets, and a list of cost models for accessing each database. Cost models determine the time required to access a database. We adopt the cost models introduced by Lu et al. (1992). However, our method does not preclude the use of other cost models.

The overall access time depends on factors at two levels, the logical level and the physical level. Factors at the logical level are concerned with the number of databases and tables needed. Factors at the physical level are concerned with the optimal sequencing of transactions so that the least amount of data traffic is required. Two operators in this problem space are designed to deal with these concerns, the Identify-optimalinfo-source operator and the Select-action operator. The Identify-optimal-info-source operator identifies the set of databases from the component databases and a set of tables in these databases that are required to respond to a user query. These databases and tables form an optimal set, which requires the least logical accessing time. The knowledge required to implement the optimal-info-source operator is specified algorithmically and discussed in §5. The Select-action operator discussed in §6 decomposes the global query into singledatabase subqueries within the optimal information set and selects a sequence of information-retrieval actions, Querying-database, Pass-values, and Compose-data, heuristically based on the observed human-planning process. The last operator in this space is the Form-asubquery operator. It formulates a database query that is implemented in the Query-language space. The goal state of this problem space is an execution plan.

Figure 7 The Problem-Space Structure of InfoB  
![](/api/attachments/KHM8QQ2H/fulltext/images/ef6afa47ba571b483a136981acf588a97b51ae91eeee69025cce94bdbd47bd42.jpg)

The Query-language problem space contains knowledge about query languages. The operator in this space is Form-a-relational-database-query. Other databaselanguage operators can be added to this problem space, such as Form-an-object-oriented-database-query. The Execution space implements the Execute operator of the task space by executing the access plan. There are two operators in this problem space, the Query operator and the Compose operator. The Query operator sends out a query to a database, while the Compose operator manipulates intermediate results.

This problem-space model represents the knowledge structure of InfoB. The technical details underlying the model are in the remainder of the paper. The next section details the knowledge-representation scheme used in InfoB to represent metainformation about the component databases in the multidatabase environment. The scheme is an extension of the Universal Relation Model of Ullman (1989) to the multidatabase environment. It is used in the implementation of the Optimal-info-source space shown in Figure 7. Following that, in §5, the mathematical models and algorithmic components used in the Plan space and its subspaces are described.

## 4. Global Universal Relation: The InfoB Metadata Representation

As illustrated in §1.1, when interacting with InfoB, the user is not required to be aware of the logical organization of the underlying multiple databases (i.e., the user query to InfoB does not contain the FROM clause). To facilitate this design, InfoB uses ideas derived from the Universal Relation Model (Ullman 1989). Further, recall that universal relations support the maximal-object construct that permits lossless joins to be computed. This is a desirable property in the InfoB context. In this section, we extend the universal relation concept to the multidatabase setting. We refer to this extended model as the global universal relation. Ideas based on global universal relations can be found in (Zhao et al. 1995, Chang and Sciore 1992).

4.1. The Construction of a Global Hypergraph In the hypergraph representation introduced in Ullman (1989), each attribute in the database schema is a node. Hypergraph edges are sets of attributes. Therefore, each relation (a set of atttributes) is represented as a hypergraph edge. Directionality within a hyperedge depicts a functional dependency, i.e., from the primary key attribute of the relation to the other attributes. Following these rules, a hypergraph representation of each component-database schema can easily be created.

• A global hypergraph is given in Figure 8 that contains three of the Commerce Component Databases, namely, MillionDollarDirectory, Manufacturers, and Distributors database schemas. The global hypergraph essentially merges the hypergraphs of the component databases through two types of links:

• A static interdatabase link merges attribute names that denote the same real-world concept. For example, in Figure 8, the attributes CEO.MillionDollarDirectory and CEO.Manufacturers are merged. Static links are inferred by matching pairs of attribute names that have the same semantic meaning. As component databases are added or deleted, the static links are updated. The matching of attributes can be done either manually or automatically, given the availability of a domain ontology (Lenat 1990, Chandrasekaran 1999,

![](/api/attachments/KHM8QQ2H/fulltext/images/9f585046f85d4a7ae25abf4e564e234c79281b9099bcf5c6bb5241c2351dbc65.jpg)  
<sup>3</sup>Ontologies are theories about the properties of objects and relations between objects in a specific domain of knowledge by clarifying the structure of knowledge and thereby enabling better sharing of knowledge in information retrieval.

Noy and Hafner 2000).<sup>3</sup> An ontology is a formal specification of the conceptualization of a domain that specifies the possible objects or entities about which knowledge can be expressed. Ontologies are tailored to support the needs of inferential tasks. In our context, the inferential task is matching and an ontology used to support this task can be as simple as a list of names or terms that arise in the domain of application and their associated relationships. However, this limits the matching that can be done to exact matches on name. An alternative realization of ontology is to combine a vocabulary of names or terms with rules of formation for terminological structures and rules for valid matching (see Bhargava et al. 1991 for a logic-based approach and Noy and Hafner 2000 for a frame-based approach). This permits a theoretical specification of the properties of terms and their relationships, and can be used to support structure-based matching.

• A dynamic interdatabase link (denoted by shaded arrows) connects attribute names that are stated in the user query to be equivalent. For example, the user may specify an equal relation between “Cname” (company name) and “Mname” (manufacturer name). This link is denoted by a shaded two-way arrow in Figure 8 between the node “Cname” in the company table of the MillionDollarDirectory database and the node “Mname” in the manufacturer table of the Manufacturers’ database.

Thus, a global hypergraph for a multidatabase schema can be constructed by the following procedure:

1. Create hypergraphs for each component-database schema (Ullman 1989).

2. Identify static links. Merge the attributes that are statically linked. Merge the hypergraphs as in Figure 8. For illustrative purposes, use different shades or line-patterned edges to delineate the different database sources.

3. Identify the dynamic links from the user query, and link the attributes in the hypergraph.

The resulting global hypergraph of the multidatabase provides the foundation for constructing maximal objects in the multidatabase environment.

## 4.2. Maximal Objects in a Global Hypergraph

The maximal object of a universal relation consists of those data objects over which lossless joins may be computed. As noted earlier, this is a desirable feature for InfoB because it ensures the correctness of responses to queries. Computing the maximal object in a global hypergraph involves only a minor extension to the algorithm proposed in Ullman (1989). The extended algorithm is given below, using the notation introduced in Ullman (1989).

Algorithm 1: The construction of a maximal object in a multidatabase system.

Input: a collection of objects (tables), a starting object O, functional dependencies on the attributes of those objects, and user-suggested interdatabase links if any.

Output: a collection of objects, M, that forms the maximal object for the input structure.

Let ATTR(M) denote the set of all attributes for the given set of objects M. Let ATTR(R) denote an attribute in a relation R. Let $^ { \prime \prime } \to ^ { \prime \prime }$ stands for “functionally determines.” In the following, user-suggested relation is a relation between attributes specified in a user query.

$$
M := \{O \};
$$

while M changes do

for each relation P such that

$$
(P \cap A T T R (M)) \to P
$$

or (P  ATTR(M)) → ATTR(M)

suggest-relation(p,m) <sup>@</sup> // Interdatabase

$$
(p \rightarrow P) \vee (m \rightarrow A T T R (M)) \} / / \text {   Link   here   }
$$

or $P \mathrm { ~ - ~ } A T T R ( M )$ is disconnected from ATTR(M) – P when

P  ATTR(M) is deleted from the global hypergraph

do M:- M -{P}

## end While

Algorithm 1 is a straightforward extension of the algorithm used in universal relation (Ullman 1989). The extension is accomplished by first representing the multidatabase system as a global hypergraph and then adding a new condition that takes dynamic interdatabase links into account. The essential idea of this algorithm is to ensure that each relation added to the set of maximal objects is a lossless addition. At initialization, O, the relation from which the search for the maximal object begins, is set to be the maximal object by (M:- {O}). The for section of the while-do loop checks the conditions under which the addition of a relation to the maximal object would be lossless. The do section adds the new relation to the maximal object. The principal advantage of deriving the maximal object is that joins taken over the relations in a maximal object or subsets of these relations are guaranteed to be lossless. Applying Algorithm 1 to Figure 8, by starting from the company table, computes a maximal object that contains all the tables in the MillionDollarDirectory, Manufacturers, Distributors schema introduced in Figure 1. In all, the maximal object consists of nine tables.

In general, and as shown in our example (see Figure 6), there can be several maximal objects in a global hypergraph. Each of these can be determined by applying Algorithm 1 using a different starting object. However, one can take advantage of the fact that a maximal object contains its starting object. Thus, if a maximal object that has already been identified contains a candidate starting object, applying Algorithm 1 using the candidate object would be redundant. This observation is formalized as Lemma 1. The proof is given in the Appendix A.

Lemma 1. Let $M _ { n } ( O _ { i } )$ denote a maximal object obtained by applying Algorithm 1 to a set of n objects, $R _ { n }$ with the starting object $O _ { i } .$ . Let $M _ { n } ( O _ { j } )$ denote a maximal object obtained by applying Algorithm 1 to $R _ { n }$ with the starting object $O _ { j \prime }$ where $O _ { j } \ne O _ { i } . I f O _ { j } \in M _ { n } ( O _ { i } )$ and $O _ { i } \in M _ { n } ( O _ { j } ) .$ then ${ \cal M } _ { n } ( O _ { i } ) = { \cal M } _ { n } ( O _ { j } )$

A maximal object M is called a relevant maximal object if $A T T R ( M ) \supseteq A _ { t } ,$ where ATTR(M) denotes all the attributes in M and $A _ { t }$ is the set of target attributes specified in the user query. Given the set of target attributes of User Query 1, namely the set {Cname, Mname, Pname, GrossSales}, the maximal object consisting of all the tables in the MillionDollarDirectory, Manufacturers, and Distributors schema is a relevant maximal object.

Once a maximal object is identified, an InfoB query can be interpreted as it joins over the tables in the relevant maximal object (Ullman 1989). However, to answer a user query in the most efficient manner, it is desirable to have the minimum set of tables selected from among the tables in a relevant maximal object. The following section formulates a mathematical model to identify the optimal set of tables required to answer a user query from a relevant maximal object.

## 5. Optimal Source Identification from Relevant Maximal Objects

In this section, we develop a mathematical model for implementing the Optimal Info Source space of the InfoB architecture shown in Figure 7. This is done to improve efficiency and to guarantee the correctness of the method used to derive the set of data sources required to answer a query.

## 5.1. Mathematical Models

A mathematical model for selecting the optimal set of the tables from those in a maximal object needs to deal with two requirements. First, the tables selected should collectively contain the answer to the query. This means that the set of attributes in the query must be a subset of the attributes in the tables selected. We refer to this as the covering constraint. Second, because joins within a component database are generally cheaper to compute than joins that involve different component databases, the tables selected should be such that they minimize the cost of the joins required to answer the user query. We call this the join-cost-minimization principle. We can state these requirements in the informal model structure shown below.

$$
\text { Min   Cost\_of\_join }\tag{1}
$$

$$
\text { Subject   to }
$$

$$
\text { All\_the\_target\_attributes\_are\_covered }\tag{2}
$$

$$
\text { All\_the\_selected\_tables\_are\_joinable }\tag{3}
$$

To formulate the model mathematically, let X be a binary vector, so that $x _ { \mathrm { i } } = 1$ , if table $T _ { \mathrm { i } }$ is selected to be part of the optimal set or 0, otherwise. Let Cover denote the constant matrix (where $C o v e r _ { \mathrm { i r } } = 1$ if table i contains the $r ^ { \mathrm { t h } }$ target attribute); otherwise 0. Expression (2) can be stated as

$$
\sum_ {i = 1} ^ {n} C o v e r _ {i r} x _ {i} \geq 1 \text { for } r = 1, 2,.., t\tag{4}
$$

where t is the number of target attributes. Because a maximal object is a connected graph by design, Constraint (3) is automatically satisfied. This results in the model structure below.

$$
\text { Min } \quad \text { Cost\_of\_join }\tag{1}
$$

$$
\text { Subject   to } \sum_ {i = 1} ^ {n} C o v e r _ {i r} x _ {i} \geq 1 \text { for } r = 1, 2,.., t\tag{4}
$$

$$
x = 0 \mathrm{or} 1\tag{5}
$$

Constraint (4) is the operative constraint that ensures the selection of a subset of the tables in the maximal object that covers the attributes in the query.

We next formulate the model for the variable Cost\_of\_join mathematically. Consider Figure 9, which represents each table in a maximal object as a node in a graph.

An edge between any two nodes in the graph denotes a lossless join. The weight of the edge represents the cost of the join (Lu et al. 1992). Differences in the cost of joins within a single database and in that between databases are captured by assigning the cost of an interdatabase join to be some order of magnitude larger than the cost of intradatabase joins. If a particular interdatabase join is undesirable, its cost can be made considerably higher than other costs to preclude its inclusion. In general, the specific cost values chosen will depend on the particular multidatabase environment. A subset of the nodes (tables) in this graph correspond to those tables—the covering tables—that cover the attributes in the user query (refer to Constraint (4)). The objective is to determine the least-cost tree of this graph that contains the covering tables. This least-cost tree corresponds to the set of tables that can minimize the cost of the joins required to answer the user query. Computing this least-cost tree is the Steiner tree problem (Hwang et al. 1992) which is an NPcomplete problem.

We propose an alternative, if suboptimal, formulation based on the following observation. The cost of joining the covering tables equals the cost related to the tables themselves (assuming that access to a component database incurs a fixed cost) plus the cost of joining pairs of tables in the set of covering tables. For each pair of selected tables, the least-cost method of joining them is the shortest path between them in the graph. Let $R e a c h _ { i j }$ denote the shortest path (Aho et al.

## Figure 9 Linked Tables in a Maximal Object

![](/api/attachments/KHM8QQ2H/fulltext/images/f2ec41ab984f4b58273d6bf10d1ab0485e5921279ef81ca28cef32b4ac130fe4.jpg)

1974) from node i to node j in the graph. The cost ${ _ - o f _ { - } j o i n }$ variable can be modeled as a sum of the fixed cost of accessing a table (here assumed to be 1) and the cost of joining, using the shortest path, each pair of tables in the covering set.

$$
\sum_ {i = 1} ^ {n} x _ {i} + \sum_ {i j} \operatorname{Reach} _ {i j} x _ {i} x _ {j}\tag{6}
$$

Therefore, we have the model

P1:

$$
\begin{array}{l} \text {Min} \sum_ {i = 1} ^ {n} x _ {i} + \sum_ {i j} \operatorname{Reach} _ {i j} x _ {i} x _ {j} \\ \text {Subject to} \\ \sum_ {i = 1} ^ {n} \operatorname{Cover} _ {i r} x _ {i} \geq 1 \text {for} r = 1, 2,.. t \\ x = 0 \text {or} 1 \end{array}\tag{4}
$$

The constraint set in the model ensures that the selected tables will cover the target attributes. The objective function ensures that the set of selected tables will minimize the overall cost of computing the joins.

The model P1 is a quadratic-integer programming model. However, it can be reformulated as a mixedinteger linear-programming model by introducing the following transformation. Let $z _ { i j } = x _ { i } \ : x _ { j } ,$ where $z _ { i j }$ is a continuous variable (Phillips et al. 1987).

$$
\begin{array}{l} x _ {i} + x _ {j} - z _ {i j} \leq 1 \\ z _ {i j} \leq x _ {i} \\ z _ {i j} \leq x _ {j} \\ z _ {i j} \geq 0 \end{array}
$$

Because Reach $_ { i i } = 0$ and $R e a c h _ { i j } = R e a c h _ { j i } ,$ the objective function can also be reformulated. After rearranging the above expressions, we have:

P2: Min

$$
\sum_ {i = 1} ^ {n} x _ {i} + 2 \sum_ {i j} R e a c h _ {i j} Z _ {i j}
$$

Subject to

$$
\begin{array}{l} \sum_ {i = 1} ^ {n} C o v e r _ {i r} x _ {i} \geq 1 \text { for } r = 1, 2,..., t \\ - x _ {i} - x _ {j} + z _ {i j} \geq 1 \text { for } i <   j \\ x _ {i} - z _ {i j} \geq 0 \text { for } i <   j \\ x _ {j} - z _ {i j} \geq 0 \text { for } i <   j \\ z _ {i j} \geq 0 \\ x = 0 \text { or } 1 \end{array}
$$

Summary:

1. P2 is a mixed-integer linear-programming model. The size of the model instance is small because P2 is used to choose the optimal subset of tables from within a relevant maximal object. In our example, the relevant maximal object has nine tables (the tables in the MillionDollarDirectory, Manufacturers, and Distributors schema of Figure 7). Mixed-integer programming models of small size (8 to 15 tables) can be solved efficiently using one of several commercially available solvers. We used Cplex (Cplex 1997) for this purpose. Because the size of the model instance is small, we did not investigate heuristics to solve Model P2.

2. The parameters of Model P2 are the cover matrix and the reach matrix. The cover matrix is zero to one matrix. Its rows are tables in the relevant maximal object, and the columns are the target attributes. A cell value of one indicates that a table contains a target attribute, otherwise 0. It is generated in a straightforward manner from the relational schema shown in Figure 1. An illustrative fragment of the cover matrix shows that the Manufacturers table covers the Manufacturer\_name attribute but not the Product\_name attribute.

<table><tr><td>Cover</td><td>Manufacturer_name</td><td>Product_name</td></tr></table>

<table><tr><td>Manufacturers</td><td>1</td><td>0</td></tr></table>

3. The reach matrix is a symmetric square matrix whose rows and columns are tables in the maximal object. As discussed, its entries are computed by using the shortest-path algorithm on the representation used in Figure 9. For the example maximal object of Figure 8, an illustrative fragment of the reach matrix is shown below. Note that the first cell represents the cost of a join between two tables within the same database, namely the manufacturers and the produces tables of the manufacturers database. The second cell represents the cost of a join between two tables in different databases, namely the manufacturer table in the manufacturers database and the customer table of the bank database. Note that for the purposes of Model P2 (and logical-level design), detailed cost models of joins over the network are not required. It is sufficient to capture the relevant order-of-magnitude

difference between an intradatabase join and an interdatabase join.

<table><tr><td>Reach</td><td>Manufacturer.Produces</td><td>Bank.Customer</td></tr><tr><td>Manufacturer.Manufacturer</td><td>1</td><td>5</td></tr></table>

4. The X variables are decision variables that specify those tables that are chosen to answer the query. For our example maximal object, X is a vector of size 9 (one for each of the tables in the maximal object).

Recall that there may be more than one relevant maximal object in a global hypergraph. Model P2 needs to be solved for each of these relevant maximal objects. The tables selected from each relevant maximal object are referred to as the relevant-table set.

$$
\begin{array}{l l} \text {SELECT} & \text {Cname} \\ \text {WHERE} & \text {Company\_name = Manufacturer\_name} \\ \text {AND} & \text {Product\_name = "Computer"} \\ \text {AND} & \text {GrossSales > 100,000,000} \end{array}
$$

Applying Algorithm 1 to the global hypergraph in Figure 8 to answer the User Query 1 “large computer manufacturers” (restated above) yields only one relevant maximal object (the tables in the Million-DollarDirectory, Manufacturer, and Distributor schema). Application of Model P2 to this relevant maximal object yields the relevant-table set {company, manufacturers, product, produces}. Next, we present the formulation procedure of the global query corresponding to the user query.

## 5.2. Formulating the Global Query Using Query Templates

A query template is a structured object that consists of attributes that need to be instantiated to formulate a global query. The tables in the FROM clause of the template are the relevant tables computed using Model P2. The retrieve attributes in the select clause are the target attributes in the user query.

```txt
SELECT retrieve-attribute
FROM tables-identified-in-relevant-maximal-object
WHERE user-specified-conditions
AND Natural-join-conditions
```

Following the Universal Relation Model, we interpret the user query to be the union of a set of query templates, one for each set of relevant tables identified using Model P2.

<table><tr><td>SELECT</td><td>retrieve-attribute</td></tr><tr><td>FROM</td><td>tables(classes)-identified-in-relevant-maximal-object- $M_1$ </td></tr><tr><td>WHERE</td><td>user-specified-conditions</td></tr><tr><td>AND</td><td>Natural-join-conditions</td></tr><tr><td colspan="2">Union</td></tr><tr><td>SELECT</td><td>retrieve-attribute</td></tr><tr><td>FROM</td><td>tables(classes)-identified-in-relevant-maximal-object- $M_n$ </td></tr><tr><td>WHERE</td><td>user-specified-conditions</td></tr><tr><td>AND</td><td>Natural-join-conditions</td></tr></table>

For User Query 1—“large computer manufacturers,” because there is only one maximal object identified, only one template query is derived. The global query formulated by InfoB is shown below. In general, it should be noted that there will be one such instantiation of the template query for each relevant maximal object. The tables in the FROM clause are the set of relevant tables. The first three conditions of the WHERE clause are user-specified conditions. The last two conditions are natural-join conditions added by InfoB during query formulation using its knowledge of the merged attributes in the global hypergraph.

```sql
SELECT Cname
FROM MillionDollarDirectory.Company,
Manufacturers.Manufacturer,
Manufacturers.Product, Manufacturers.Produces
WHERE Company.Cname = Manufacturer.Mname
AND Product.Pname = "computer"
AND Company.GrossSales > 100,000,000
AND Manufacturer.Mname = Produces.Mname
AND Produces.P# = Product.P#
```

In general, the global query is not operational, because the tables identified in a relevant maximal object are spread over multiple databases. For example, the global query formulated above involves two databases, the MillionDollarDirectory database and the Manufacturers database. The site autonomy and the system heterogeneity among the databases prevent direct evaluation of these queries (Lu et al. 1992).

## 6. Access Planning

Evaluation of the global query requires that it be decomposed into subqueries that are evaluated on each component database. Each subquery processing task has its preconditions and postconditions, and only a plan that consists of the right sequence of tasks will evaluate the global query correctly. Based on our observation of the human experts, access planning in

InfoB uses a heuristic state-space search process. The search process makes no assumption about the cost model, which may or may not take into account order dependencies.

Planning takes place in the Action-selection problem space in Figure 7. The initial state contains a set of linked tables (i.e., the relevant-table set) in a set of databases and a set of user-specified conditions stated in the global query. The goal state is the state in which the retrieve attributes have known values. The operators to move from the initial state to the goal state are Query-a-database, Pass-attribute-value, and Compose-data. Figure 10 defines preconditions and postconditions of these action operators. The Intersect operator is the operator that composes two sets of values. To fully understand the operators in Figure 10, the following definitions are necessary:

• An attribute is said to be a retrieve\_attribute (denoted by Rattr) if it is an attribute mentioned in the SELECT clause of a user query. For instance, Cname in the User’s query is a retrieve\_attribute.

• An attribute is said to be a border\_attribute (denoted by Battr) if there is an interdatabase link between the attribute and an attribute in another relevant database table in the same maximal object. For instance, Cname in the MillionDollarDirectory database and Mname in the Manufacturers database are border\_attributes.

• A known\_value\_attribute (denoted by Kvattr) is an attribute whose values can be either specified by the user in the user’s information request or obtained by previous actions. Examples of known\_value\_attributes in the user query are GrossSales in the Manufacturers database and Pname in the Product database.

Using these definitions, we present a brief summary of the access-planning operators. The Query-a-db(i) operator states that for a given database i if A is an attribute and its value is unknown, and all the border\_attributes besides attribute A have known values, then the Query\_database operator can be applied. The result of this operator application will assign a value to A. The Pass-attribute operator is used to deal with the case in which the border attribute of an attribute to be assigned a value is known. The Intersect operator is applied when two attributes that are linked have known values. It computes the intersection of the values.

Each operator action has an associated cost. There are many factors that determine the cost function of each action, including network parameters, conditions of the component-database host, the database engine of the component database, the accessibility of a particular database, and the host platform of the agent, InfoB. We do not introduce any new cost functions but note that as long as cost functions are available, our state-space planning approach can accommodate them. We used the cost function described in Lu et al. (1992) to assign costs to the operators in our implementation.

These operators are used in InfoB to perform statespace search. The goal is to minimize the total cost of the operator applications needed to answer the query. Applying these operators to the global query in §5 results in the following three-step access plan.

```sql
(1) Execute Subquery 1 (Large companies):
SELECT Cname
FROM MillionDollarDirectory.Company
WHERE GrossSales.Company > 100,000,000
```

(2) Execute Subquery 2 (Computer manufacturers):

AND Product.Pname - “computer”

(3) Return the intersection of Cname and Mname as the result.

## 7. Validating InfoB

Given our focus on logical design problems and the basis for the work in the human study, we validated

## Figure 10 Action Operators

Action: A  Kvattr, action-cost - Cq

Pass-attribute-values

the models in InfoB by comparing its outputs and its reasoning steps to the data collected in the protocolanalysis experiments. We did not conduct extensive performance comparisons taking into account factors such as caching and replication as they are not within the scope of this paper.

The query task used in this section is the second query used as part of the protocol analysis. The query requires access to the MillionDollarDirectory database, the Manufacturers database, and the Bank database. The global hypergraph of these databases extends the hypergraph of the Bank database (Figure 6) by adding in hyperlinks corresponding to the Manufacturer and MillionDollarDirectory database.

User Query 2. Find all the companies who manufacture computers, bank at Branch #3, and whose annual gross sales are greater than \$100 million.

In response to this query, InfoB generates the output plan shown in Figures 11a and 11b. Groups A and B in the figure refer to the access plans formulated for each of the maximal objects identified in the global hypergraph.<sup>4</sup>

## 7.1. A Comparison Between the Access Plan

To validate the output produced by InfoB we compared the access plan generated by InfoB with that formulated by Expert B1 shown below.

There are four stages in the expert’s plan. In the first stage, all companies that manufacture computers are selected. In the second stage, all companies that bank at Branch 3 are selected. Notice that companies that have an account in the branch and/or have taken a loan from the branch are all customers of the branch. So, the expert first selects those who have an account. At the same time, he selects those who take a loan from Branch 3. Then he takes the union of the two groups to get those companies who are customers of Branch 3. In the third stage, all companies whose gross sales are more than 100 million dollars are selected. Finally, in the fourth stage, the expert takes the intersection of the three groups previously identified to get the information requested by the query.

On the other hand, InfoB divides the query task into three main stages—the first two stages formulate the queries on the two maximal objects identified for the user query, and the third computes the intersection of the results of the first two queries. In the first stage, InfoB selects those companies who meet the conditions

```txt
Figure 11a InfoB Access Plan for User Query 2

Group A
(Tables included:
    company, product, produces, keep_account, account_branch)
    Decomposed into 3 databases queries
    Step 1
    SELECT Cname
    FROM MillionDollarDirectory.company
    WHERE Grosssales > 100,000,000
    Step 2
    SELECT Mname
    FROM Manufacturers.manufacturer,
    Manufacturer.product, Manufacturer.produces
    WHERE manufacturer.Mname = produces.Mname
    AND product.Pname = “computer”
    AND produces.P# = product.P#
    Step 3
    SELECT Cusname
    FROM Bank.keep_account, Bank.account_branch
    WHERE keep_account.Account# = account_branch.Account#
    AND account-branch.Branch# = “3
    Step 4
    Intersect Cname,Mname,Cusname

Group B
(Tables included:
    company, product, produces, take_loan, loan_branch)
    Decomposed into 3 database queries
    Step 1
    SELECT Cname
    FROM MillionDollar Directory.company
    WHERE Grosssales > 100,000,000
    Step 2
    SELECT Mname
    FROM Manufacturers.manufacturer,
    Manufacturer.product, Manufacturer.produces
    WHERE manufacturer.Mname = produces.Mname
    AND product.Pname = “computer”
    AND produces.P# = product.P#
    Step 3
    SELECT Cusname
    FROM take_loan, loan_branch
    WHERE take_loan.loan# = loan_branch.loan#
    Step 4
    Intersect Cname,Mname,Cusname

Union the result from Group A and Group B.
```

## Figure 11b Expert’s Plan for User Query 2

Branch #3\_Customers SELECT Customer\_name FROM Customer,Keep\_account,Take\_loan,Lbr,AcBr WHERE (Lbr.Branch# -“3” AND LBr.Loan# -Take\_loan.Loan# AND Take\_loan.CustomerID - Customer.CustomerID) OR (Lbr.Branch# - “3” AND AcBr.Account#-Keep\_account.Account# AND Keep\_account.CustomerID - Customer.CustomerID)

in the first maximal object, namely, sales greater than \$100 million, manufacturing computers, and having an account at Branch 3. In the second stage, InfoB selects those companies who meet the conditions in the second maximal object, namely, sales greater than \$100 million, manufacturing computers, and taking a loan from Branch 3. In the last stage, InfoB takes the intersection of the two group to get the final information requested by the query.

Is the plan formulated by InfoB the same as the plan formulated by the expert? As shown below, the final result from the expert is:

Computer\_Manuf  Branch#3\_Customers  MillionDollar\_Companies

which is the same as

Computer\_Manuf  (Customers taking loan - Customer having an account at Branch #3)  MillionDollar\_Companies

The final result from InfoB based on its query plan is:

(Computer\_Manuf  Customers taking loan  Million-Dollar\_Companies) - (Computer\_Manuf  Customer having an account at Branch#3  MillionDollar\_Companies).

Using logic manipulation rules, the above can be transformed into:

Computer\_Manuf  (Customers taking loan - Customer having an account at Branch #3)  MillionDollar\_Companies

that is exactly the same as the final results from the expert. Thus, while the expert and InfoB take different approaches, they produce the same result.

## 8. Conclusions

This paper presents an interdisciplinary approach to addressing a problem of considerable importance to the information-systems community. Given the dramatic growth in the number and variety of information sources and innovative applications that package them, such as smart catalogs (Keller 1996), there is a great need for information-retrieval mediators.

In contrast to much of the work in the literature, our approach rests on a human multidatabase-access model that is developed based on an empirical study of database experts. Using the problem space models of Soar (Newell 1990), we identified the principal tasks and the knowledge sources that are needed for data retrieval in multidatabases. While the human multidatabase-access model provided considerable insight, we also found that the observed problem-solving process used in database-source identification and access planning were inefficient. Using the Soar-based architecture as a framework, we developed mathematical models and algorithmic components to address these two problems. We also validated the approach by comparing InfoB’s problem-solving process and outputs with those generated by the human expert.

The principal insight we gained from this work was the value in combining complementary approaches such as protocol analysis, knowledge systems, and algorithmic components (derived from mathematical models) to address a difficult problem. Based on our testing and analysis, we believe that the framework

∴ the “for test” of Algorithm 1 passes

offered by the approach is general and can accommodate refinements. Several of these refinements will necessarily require a study of problems at the physical level that were not addressed by our work on logicallevel problems of database-source identification and access planning. These problems include topics such as query-process planning in terms of the order of operations (selections and joins), buffer management, precomputation and caching, and materialized views. These are active areas of research, and their integration into our framework demands its own in-depth treatment. Given the importance of the problem, we hope that the paper encourages research into this important and relevant problem in the information-systems community.

## Appendix: Proof of the Lemma

Proof. Let $R _ { n }$ be a set of n objects (tables) on which maximal objects are identified. $O _ { a }$ and $O _ { b }$ are two different objects in $R _ { n } . \mathrm { A p p l y - }$ ing Algorithm 1 to $O _ { a } ,$ a maximal object obtained is $M _ { n } ( O _ { a } )$ , while applying Algorithm 1 to $O _ { b } ,$ a maximal object $M _ { n } ( O _ { b } )$ is obtained. We need to establish that if $O _ { b } \ \varepsilon { M } ( O _ { a } ) .$ , then ${ \cal M } ( { \cal O } _ { a } ) \equiv { \cal M } ( { \cal O } _ { b } )$ . We prove this by induction.

When $n = 2 ,$

Apply first step of Algorithm 1 to $O _ { a } ,$ , we have $M _ { 2 } ( O _ { a } ) \colon = \{ O _ { a } \}$ $\Theta { \cal O } _ { b } \ : \varepsilon { \cal M } _ { 2 } ( { \cal O } _ { a } )$

$$
\therefore M _ {2} (O _ {a}) \supset \{O _ {a}, O _ {b} \}
$$

H ${ \mathrm { ~ \ } } n = 2 ,$ after adding $O _ { b }$ to $M _ { 2 } ( O _ { a } )$ , there are no more objects left to test the while test (in Algorithm 1) fails

$$
\therefore M _ {2} (O _ {a}) = \{O _ {a}, O _ {b} \}
$$

Applying first step of Algorithm 1 to $O _ { b } ,$ we get $M _ { 2 } ( O _ { b } ) \colon = \{ O _ { b } \}$

$\Theta M _ { 2 } ( O _ { a } )$ is a maximal object and $M _ { 2 } ( O _ { a } ) = \{ O _ { a } , O _ { b } \}$

$\therefore O _ { a }$ and $O _ { b }$ form lossless joins

Applying do step of Algorithm 1 we get $M _ { 2 } ( O _ { b } ) \colon = \{ O _ { b } \} \cup \{ O _ { a } \} =$ $\{ O _ { b } , O _ { a } \}$

$$
\therefore M _ {2} (O _ {b}) = \{O _ {b}, O _ {a} \} = M 2 (O _ {a})
$$

$$
\text {   When   } n = k, \text {   let   } M _ {k} (O _ {a}) = M _ {k} (O _ {b})
$$

When $n = k + 1$

Let o denote the newly added object, i.e. $R _ { k + 1 } = \{ R _ { k } , o \}$

If o and $M _ { k } ( O _ { a } )$ form lossless joins, then

the for test of Algorithm 1 passes

$$
\text { Applying   do   step,   we   get }
$$

$$
M _ {k + 1} (O _ {a}) := M _ {k} (O _ {a}) \cup \{o \}
$$

$$
\Theta M _ {k} (O _ {a}) = M _ {k} (O _ {b})
$$

If o and $M _ { k } ( O _ { a } )$ form lossless joins, then o and $M _ { k } ( O _ { b } )$ form lossless joins too.

∴ The for test of Algorithm 1 passes for $M _ { k + 1 } ( O _ { b } )$

$$
\therefore M _ {k + 1} (O _ {b}) = M _ {k} (O _ {b}) \cup \{o \}
$$

$$
\therefore M _ {k + 1} (O _ {a}) = M _ {k + 1} (O _ {b})
$$

If o and $M _ { k } ( O _ { a } )$ form lossy joins, then the while test of Algorithm 1 fails

${ \cal M } _ { k + 1 } ( { \cal O } _ { a } ) = { \cal M } _ { k } ( { \cal O } _ { a } )$

If o and $M _ { k } ( O _ { a } )$ form lossy joins, then o and $M _ { k } ( O _ { b } )$ form lossy joins.

∴ The while test of Algorithm 1 fails, ${ \cal M } _ { k + 1 } ( { \cal O } _ { b } ) = { \cal M } _ { k } ( { \cal O } _ { b } )$

H ${ \cal M } _ { k } ( { \cal O } _ { a } ) = { \cal M } _ { k } ( { \cal O } _ { b } )$

$M _ { k + 1 } ( O _ { a } ) = M _ { k + 1 } ( O _ { b } ) \quad \sqcap$

## References

Ahmed, R., P. DeSmedt, W. Du, W. Kent. 1991. The Pegasus heterogeneous multidatabase system. IEEE Comput. 24(22) 19–27.

Aho, A., J. Hopcroft, J. Ullman. 1974. The Design and Analysis of Com puter Algorithms. Addison Wesley, Reading, MA.

Arens, Y., C. Y. Chee, C.-N. Hsu, C. A. Knoblock. 1993. Retrieving and integrating data from multiple information sources. Internat. J. Intelligent and Cooperative Inform. Systems 2(2) 127–158.

Atzeni, P., R. Torlone. 1997. MDM a multiple-data-model tool for the management of heterogeneous database schemes. Proc. 1997 ACM SIGMOD, Tucson, AZ. 528–531.

Bayardo Jr., R. J., W. Bohrer, R. Brice, A. Cichocki. 1997. InfoSleuth: Agent-based semantic integration of information in open and dynamic environments. Proc. 1997 AGM SIGMOD, Tucson, AZ 26(2) 195–206.

Bhargava, H., S. Kimbrough, R. Krishnan. 1991. Unique names violations: A problem for model integration or you say tomato, I say tomahto. ORSA J. Comput. 3(2) 107–121.

Bright, M., A. R. Hurson, H. Pakzad. 1992. A taxonomy and current issues in multidatabase systems. IEEE Comput. 25(3) 50–60.

Chandrasekaran, B., J. R. Josephson, V. R. Benjamins. 1999. What are ontologies, and why do we need them? IEEE Intelligent Systems. 14(1) 20–26.

Chang, T., E. Sciore. 1992. A universal relation data model with semantic abstractions. IEEE Trans. Knowledge and Data Engrg. 4(1) 23–33.

Cplex. 1997. Commercial Mathematical Programming Optimizers. http://www.cplex.com.

Duschka, O. M., M. Genesereth. 1997. Query planning in infomaster, computer science technical report. Proc. 1997 ACM Sympos. in Appl. Comput. San Jose, CA 109–111.

Garcia-Molina, H., Y. Papakonstantinou, D. Quass, A. Rajaraman. 1997. The TSIMMIS approach to mediation: Data models and languages. J. Intelligent Inform. Systems: Integrating Artificial Intelligence and Database Tech. 8(2) 117–132.

Hammer, J., H. Garcia-Molina, S. Nestorov, R. Yerneni. 1997. Template-based wrappers in the TSIMMIS system. Proc. 1997 SIG-MOD, Tucson, AZ 26(2) 532–533.

Henry, T., G. Lind. 1994. ALCHEMIST: An object-oriented tool to build transformations between heterogeneous data representations. Proc. Twenty-Seventh Annual Hawaii Internat. Conf. System Sci. 226–235.

Hill, R., J. Chen, J. Gratch, P. S. Rosenbloom, M. Tumbe. 1997. Intelligent agents for the synthetic battlefield: A company of rotary wing aircraft. Proc. 9th Innovative Appl. Artificial Intelligence. Providence, RI pp. 1006–1012.

Hwang, H., D. Richards, P. Winter. 1992. The Steiner Tree Problem. North Holland Publishers, Amsterdam, The Netherlands.

Jeff, Y.-C. P., J. M. Tenenbaum. 1991. An intelligent agent framework for enterprise integration. IEEE Trans. Systems, Man, and Cybernetics. 21(6).

Kashyap, V., A. Sheth. 1994. Semantics-based information brokering. Proc. 3rd Internat. Conf. Inform. Knowledge Management. Gaithersburg, MD 28(2) 363–370.

Keller, A. M. 1996. Smart catalogs and virtual catalogs. Comput. Sci. Tech. Rep. Stanford University, Stanford, CA.

Kim, W., I. Choi, S. Gala, M. Scheevel. 1993. On resolving schematic heterogeneity in multidatabase systems. Distributed and Parallel Databases. 1(3) 251–279.

Laird, J., A. Newell, P. Rosenbloom. 1983. Soar: An architecture for general intelligence. Artificial Intelligence. 33 1–64.

Lee, S., P. Wang, W. Yang. 1993. A user-friendly universal database retrieval interface. Internat. J. Inform. Management Sci. 4(2) 15– 33.

Lenat, D. B., R. V. Guha, K. Pittman, D. Pratt. 1990. Cyc: Toward programs with common sense. Comm. ACM. 33(8) 30–49.

Li, X. 1996. A cognitively guided approach for model construction and information brokering. Ph.D. Thesis. Carnegie Mellon University, Pittsburgh, PA.

Litwin, W., A. Abdellatif. 1987. An overview of the multi-database manipulation language MDSL. Proc. IEEE. 75(5) 621–632.

Lu, H., B. Ooi, C. Goh. 1992. On global multidatabase query optimization. SIGMOD RECORD. 21(4) 6–11.

Maier, D., J. D. Ullman. 1983. Maximal objects and the semantics of universal relation databases. ACM Trans. Database Systems. 8(1) 1–14.

Marsella, S. Adibi, J. Y. ‘Al-Onaizan, A. Erdem. 1998. Using an explicit teamwork model and learning in RoboCup: An extended abstract. RoboCup ’98: Proc. Second Robot World Cup Competition Conf. Springer Verlag, Paris, France 237–245.

Mostardi, T., C. Siciliano. 1994. An overview of WIND (Wide Interoperatable Networked Databases). Proc. Twenty-Seventh Annual Hawaii Internat. Conf. System Sci. Vol. 2 216–225.

Naacke, H., G. Gardarin, A. Tomasic. 1998. Leveraging mediator cost

models with heterogeneous data sources. Proc. 14th Internat. Conf. Data Engrg. Orlando, FL. 351–60.

Newell, A. 1990. Unified theories of cognition. Harvard University Press, Cambridge, MA.

Noy, N. F., C. D. Hafner. 2000. Ontological foundations for experimental science knowledge bases. Appl. Artificial Intelligence. 14 565–618.

Pan, J. Y. C., J. M. Tenenbaum. 1991. An intelligent agent framework for enterprise integration. IEEE Trans. Systems, Man and Cybernetics 21(6) 1391–1408.

Phillips, D. T., R. Ravindran, J. Solberg. 1987. Operations Research: Principles and Practice, 2nd ed. John Wiley and Sons, Inc., New York.

Rosenbloom, P. S., J. E. Laird, J. McDermott, A. Newell. 1985. R1- Soar: An experiment in knowledge-intensive programming in a problem solving architecture. Pattern Anal. Machine Intelligence. 7 561–569.

Sheth, A., J. Larson. 1990. Federated database systems for managing distributed, heterogeneous, and autonomous databases. ACM Comput. Surveys. 22(3) 83–236.

Simon, H. 1955. A behavioral model of rational choice. Quart. J. Econom. 69 99–118.

Singh, N. 1998 Unifying heterogeneous information models. Comm. ACM. 41(5) 37–44.

Ullman, J. 1989. Principles of Database and Knowledge-Base Systems, Vol. 1 and 2. Computer Science Press, Rockville, MD.

Vidal, M. E., L. Raschid, J.-R. Gruser. 1998. A meta-wrapper for scaling up to multiple autonomous distributed information sources. Proc. 3rd IFCIS Internat. Conf. Cooperative Inform. Systems. New York 148–57.

Wiederhold, G. 1992. Mediators in the architecture of future information systems. Comput. 25(3) 38–49.

Zhao, J. L., A. Segev, A. Chatterjee. 1995. A universal relation approach to federated database management. Proc. 11th Internat. Conf. Data Engrg. Taipei, Taiwan.

Zhu, Q., P.-A. Larson. 1996. Building regression cost models for multidatabase systems. Proc. the 4th Internat. Conf. Parallel and Distributed Inform. Systems. Miami Beach, FL 220–31.

Michael Shaw, Associate Editor. This paper was received on July 15, 1997, and was with the authors 15 months for 3 revisions.
