---
otero_id: 24717
otero_key: "MC5R4NNP"
title: "A Form-Based Approach to Natural Language Query Processing"
authors: "Nabil R. Adam; Aryya Gangopadhyay; James Clifford"
year: "1994"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1994.11518042"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Form-Based Approach to Natural Language Query Processing

Nabil R. Adam, Aryya Gangopadhyay & James Clifford

To cite this article: Nabil R. Adam, Aryya Gangopadhyay & James Clifford (1994) A Form-Based Approach to Natural Language Query Processing, Journal of Management Information Systems, 11:2, 109-135, DOI: 10.1080/07421222.1994.11518042

To link to this article: http://dx.doi.org/10.1080/07421222.1994.11518042

![](/api/attachments/MC5R4NNP/fulltext/images/6f0d75b2fc20534013bc1faea495a12eb33baf2fc521f8e53fe394624d5a84d1.jpg)

Published online: 14 Dec 2015.

![](/api/attachments/MC5R4NNP/fulltext/images/af7f11ac3535246d02db08a5a822a8e70d32886c28b17c83cd6deae1fbb72efa.jpg)

![](/api/attachments/MC5R4NNP/fulltext/images/d41544e408b539f35379df4627b531c44d9c689d426c9f401ba38b5c01d7da2b.jpg)

View related articles ↗

![](/api/attachments/MC5R4NNP/fulltext/images/7ea4bc3c4b9117230452dcc3fc2a8700a1efc6b71c9beb97c3ecf4e41ff03754.jpg)

Citing articles: 1 View citing articles ↗

# A Form-Based Approach to Natural Language Query Processing

NABIL R. ADAM, ARYYA GANGOPADHYAY, AND JAMES CLIFFORD

NABIL R. ADAM is a Professor of Computers and Information Systems and Chair of the MS/CIS Department at Rutgers University. He is also a member of the Rutgers Graduate Program in Industrial and Systems Engineering. Dr. Adam received a B.S. degree from Cairo University, and M.S., M.Phil, and Ph.D. degrees from Columbia University. Dr. Adam edited or coedited five books and three special journal issues. He has published papers in a wide range of areas, including simulation, scheduling, query optimization, database modeling, object-oriented databases, and concurrency and consistency control in distributed database systems. He has contributed to such journals as IEEE Transactions on Software Engineering, IEEE Transactions on Knowledge and Data Engineering, ACM Computing Surveys, Journal of Management Information Systems, Information Systems, Management Science, and European Journal of Operational Research. He serves on the editorial board of the Journal of Management Information Systems and is currently serving as the Program Chair of the 1994 International Conference on Information and Knowledge Management.

JAMES CLIFFORD is an Associate Professor of Information Systems at the Leonard N. Stern School of Business at New York University, where he has been a member of the faculty since 1982. He earned a B.A. in music from Yale University in 1975, and an M.S. and Ph.D. in computer science (in 1979 and 1982, respectively) from the State University of New York at Stony Brook. His major areas of research have been the development of data models and query languages to support the temporal dimension of data, and the application of artificial intelligence to decision-making problems in business. His latest research interest lies in the area of knowledge discovery in large databases. He has authored or edited numerous articles and several books on these subjects.

ARYYA GANGOPADHYAY is an Assistant Professor in the Department of Information Sciences and Systems of the School of Business and Management at Morgan State University. He received his Ph.D. in computer information systems from Rutgers University in 1993. His research interests include knowledge-based query processing, natural language interfaces, and conceptual database design. Dr. Gangopadhyay has contributed to the International Journal of Intelligent and Cooperative Information Systems, and to several conference proceedings.

Acknowledgments: We would like to thank the three anonymous referees for their valuable comments on an earlier version of the paper. We would also like to thank CAFT and CRAMTD for their support.

ABSTRACT: We describe a methodology for processing data retrieval and update queries using a form-based natural language interface. For the purpose of illustration, we use computer integrated manufacturing (CIM) as the application domain. The interface consists of a set of fourth-generation interface tools (SQL forms), a set of form definitions, a lexicon, and a parser. The forms are developed from the functional and data models of the system. A form definition consists of a form name, a form object, a set of form fields, and a set of fragment grammars. A form object is a single or composite entity that uniquely identifies a form. Form fields consist of database fields whose values can be entered by users (user-defined), and others whose values can be derived by the system (system-defined). Fragment grammars are templates that identify the information requested by user queries. The lexicon consists of all words recognized by the system, their grammatical categories, synonyms, and associations (if any) with database objects and forms. The parser scans a natural language query to identify a form in a bottom-up fashion. The information requested by the user query is determined in a top-down manner by matching the fragment grammars associated with a form against the user query. Extragrammatical inputs with limited deviations from the grammar rules are supported. Elliptical queries are supported by deriving the missing information from those specified in previous queries and forms. Combining a natural language processor with SQL forms allows update queries and prevents violation of database integrity constraints, duplication of records, and invalid data entry.

KEY WORDS AND PHRASES: database management systems, 4GL, natural language interface, query processing.

## 1. Introduction

AN IMPORTANT ASPECT OF AN INFORMATION SYSTEM is the interface through which it interacts with its users. Users may not be part of the systems analysis or development group, and thus may not be familiar with the details of the various aspects of system design. Thus, one issue in the design of the interface is user-friendliness—how easy it is for both informed as well as uninformed users to retrieve the information necessary to carry out various functions. A natural language interface (NLI) (e.g., [20, 21, 23, 24, 25, 27, 34, 35, 40, 44, 46, 48]) has the potential to be among the most effective in user-friendliness, since such an interface would require the least amount of training on the part of end users. A second issue in the design of the interface is its ability to support different types of user requests. Current NLIs are limited to user queries that request specific information from the database. Transactions such as data entry and modification require validation of the data entered and maintenance of database integrity constraints. Such transactions are typically not supported by extant NLIs.

This paper presents an approach for natural language interface to a database management system that makes use of fourth-generation interface tools. The proposed methodology would:

1. Support requests that modify the contents of the database (entering new records into the database, updating existing records, etc.), in addition to information retrieval queries;

2. Process elliptical or incomplete queries by making use of the contextual knowledge of the discourse between the user and the system;

3. Eliminate the intermediate step of translating a natural language query into a formal query language. Most extant NLIs to database management systems (DBMS) process a natural language query by first translating the query into a formal query language, and then processing it;

4. Consist of a natural language query processor and a set of fourth-generation interface tools (SQL forms).

SQL forms are typically developed from functional analysis of the system to which the interface acts as a front end. This ensures that the interface supports the information requirements of all functions associated with the system. A data model of the application domain is then used to develop the domain knowledge of the system. We assume that user queries will pertain to the application modeled in the system. Thus, a well-defined boundary can be established for the natural language understanding system.

For the purpose of illustration and validation of the proposed methodology, we use a computer integrated manufacturing (CIM) system. CIM systems, by integrating the manufacturing processes with engineering design, planning, sales, and marketing, can achieve higher productivity and product quality, lower production cost, and better on-time delivery. CIM systems have been viewed by many (e.g., [15, 17, 30, 50]) as a primary mechanism for productivity improvement and a major growth area in manufacturing industries of the next decade. Currently, the Rutgers Center for Research on Advanced Food Technology (CRAFT) and the Defense Logistics Agency (DLA) are sponsoring the research project: “Combat Ration Advanced Manufacturing Technology Demonstration” (CRAMTD). Several companies in the food manufacturing industry are participating in the CRAMTD project. We use the CRAMTD project as the target application for validating our methodology.

The rest of the paper is organized as follows: in section 2 we discuss some of the relevant works in developing NLIs to DBMSs, in section 3 we describe our target application, the functional and the data model, in section 4 we describe our proposed methodology, and in section 5 we present our conclusions.

## 2. Previous Work

IN ADAM, GANGOPADHYAY, AND GELLER [4], THE VARIOUS APPROACHES to knowledge-based query processing have been divided into the following categories: (a) improving the operational efficiency of the user query (e.g., [7, 8, 9, 22, 28, 29, 32, 41, 42]); (b) developing a data administration front end in a heterogeneous database environment (e.g., [16, 17, 19]); (c) using “preoptimized” queries/views for query processing (e.g., [3, 4, 39]); (d) developing fourth-generation interfaces (e.g., [11, 12, 18]); and (e) developing natural language interfaces (e.g., [13, 21, 23, 24, 25, 26, 34, 35, 40, 44, 46]).

Natural language interfaces have an overwhelming advantage, with respect to user-friendliness, over other types of interfaces, as users of such systems do not require any special training $[44]$ . In contrast with formal query languages that have restricted syntax, the emphasis in natural languages is on semantics. Thus, NLIs are more habitable than interfaces supporting formal query languages. This habitability criterion requires that NLIs allow slightly ungrammatical queries, and queries that are incomplete (elliptical) in their specifications and/or make reference to previous queries.

Typically, most extant NLIs to DBMS act as an interface between natural language queries and formal query languages. Templeton and Burger [44] observe that the fundamental problem in developing natural language interfaces to databases is:

to actually perform the intent of the natural language question by formulating the correct structured query and efficiently navigating through the database to retrieve the right answer.

In this section, we first provide a brief overview of some of the well-known NLIs to DBMS, then discuss the issue of processing elliptical queries.

## 2.1. Some Well-Known Natural Language Interfaces to Database Management Systems

The EUFID [44] (End-User Friendly Interface to Data Management) system uses an approach based on semantic grammars to process user queries. The system consists of three modules: analyzer, mapper, and translator. The analyzer takes an English-language query as input, and generates a parse tree consisting of semantic nodes, using a semantic grammar and dictionary. The mapper takes the output of the analyzer and translates it into an intermediate language (IL). The translator takes the query expressed in the IL and translates it into the query language supported by the DBMS. EUFID can interface with relational and CODASYL databases. As discussed above, two intermediate translations are needed before the query is passed onto the DBMS for processing. This enhances the system's transportability across different DBMSs, but at the same time it requires additional processing, which may adversely affect the system's efficiency.

In LADDER [24] (Language Access to Distributed Data without Error Recovery), a user query in a restricted sublanguage of English is accepted and converted into a formal query language, which is then processed. LADDER's linguistic component, INLAND (Informal Natural Language Access to Data), is developed using a general-purpose, application-oriented natural language interface builder, called LIFER (Language Interface Facility with Ellipsis and Recursion). LIFER consists of a set of interactive language specification functions, and a parser. The language specification functions define the language in which the system would interact with application software (a DBMS, for example). The language specification functions consist of productions, whose left-hand sides consist of metasymbols, and right-hand sides consist of patterns and expressions. A pattern is a list of symbols and metasymbols in the specification language, against which an input query is matched. An expression is an LISP expression whose value is computed and assigned to the metasymbol. The top-level metasymbol is called LTG (LIFER Top Grammar). When the metasymbol LTG is assigned a value, it is returned as the answer to the query. A lexicon associates metasymbols with individual words and phrases. An ATN (Augmented Transition Network)-based, top-down, left-to-right parser translates a natural language query into a query language. The system has an INTERLISP spelling corrector, which attempts to substitute words if the parser fails to match the input with the patterns.

LADDER's ability to handle user queries is restricted to the grammar specified by the application builder. LADDER is also restricted in its ability to handle elliptical queries by relying solely on string substitutions.

The LUNAR [48] system consists of a general-purpose grammar for a large subset of the English language, an ATN-based parser [49], a semantic interpretation component that transforms an input syntactic structure into a semantic representation, and a database component for performing storage, retrieval, and computations on data. In this system, user queries in English are translated into MRL (Meaning Representation Language), a language based on first-order predicate calculus. The LUNAR system performs a complete syntactic analysis of its queries before performing any semantic interpretation. The separation of syntactic and semantic analyses might affect the efficiency of the system. On the other hand, since the syntactic processor is domain-independent, it can be transported to new domains.

The PLANES [46] system is a natural language front end to a large relational database on aircraft flight reservations and maintenance. Natural language queries are processed in four phases: parsing, query generation, evaluation, and response.

The parsing phase consists of putting words and phrases into canonical forms, matching phrases to subnets (ATN phrase parsers that match phrases with a specific meaning), assigning values to context registers for the purpose of resolving pronoun references and ellipsis, and filling missing information in elliptical queries by matching with concept case frames. A natural language query is transformed into an interim query form as the output of the parsing phase.

The query generation phase translates the interim query form into a formal query expression. This includes identifying the relations, attributes, and operations to be performed on the attributes, and an output format. The result is a relational calculus expression, which is posed to the DBMS. The system also includes a paraphrase generator, which paraphrases elliptical queries or those with pronoun references, and feeds them back to the user for approval.

The output format of the data retrieved is determined by the output module. The output could be in a tabular format, a graphical format, or could be sent to a printer, depending on the volume of the output.

In SESAME [40], a natural language query is converted into an ER-based query language called ER-SQL, which is then translated into SQL. Users can either type queries freely, or be guided by a set of menus for constructing queries. SESAME also performs detailed syntactic analysis of user queries. No suggestion has been made in SESAME for processing elliptical queries.

In the System X [34] system, a natural language query is first syntactically processed to form a parse tree. The parse tree is then converted into a semantic representation in which database objects (relations, attributes, etc.) are introduced. The semantic representation is translated into a logical form, expressed in domain relational calculus, which is then translated into the SQL query.

System X, like the LUNAR system, separates the syntactic analysis from the semantic analysis. This introduces redundancies like generating multiple syntactic structures, and comparing syntactic and semantic interpretations. System X also does not support elliptical queries.

TEAM [21] is a transportable natural language interface that can be interfaced with new databases by nonexperts in natural language processing. TEAM is designed to interact with two types of users: database experts, who would be involved in adapting the system to new domains (acquisition mode), and end users, who would be using the system for retrieving relevant information (question-answering mode). In the acquisition mode, the interaction with the system is menu-driven, and the user provides information about database structure and the application domain. The question-answering system consists of the DIALOGIC system, which maps the user query to a logical form, and a schema translator, which translates the logical form into a database query language.

All of the above NLIs go through the intermediate step of translating user requests into an intermediate query language. Also, the issue of processing update queries is not addressed in any of the NLIs.

## 2.2. Handling Ellipsis

An elliptical query is one that has not been specified completely. Elliptical queries are frequently encountered in natural language interfaces. Users would typically expect the system to understand incompletely specified queries from the context of the discourse. Some natural language interfaces to DBMSs do not support elliptical queries at all (e.g., EUFID [44], SESAME [40], System X [34], while others (e.g., [24, 27, 45, 48]) support it with varied degrees of restrictions.

In Janas [26], an elliptical query is completed by referring back to the previous query. Since queries are translated into query graphs, the method comprises of comparing the skeleton of the elliptical query with that of the previous query, and constructing the revised query graph by adding the missing information.

The LUNAR system [48] can handle ellipsis when entire noun-phrases can substitute anaphoric references. For example, if the query, “What is the silicon content of each volcanic sample?” is followed by “What is its magnesium concentration?,” the anaphoric reference “its” in the second query is replaced by the noun-phrase “each volcanic sample,” and the second query is revised to “What is the magnesium concentration of each volcanic sample?” The LUNAR system handles ellipsis by relying solely on the phrases entered by the user.

PLANES [46] handles ellipsis only when noun-phrases are missing. In PLANES, natural language queries are parsed by an ATN-based parser that uses case frames. Register slots in the case frame are filled as the parse progresses. Whenever a mandatory slot in a case frame corresponding to a query is not filled, the query is determined to have an ellipsis, and previous case frames are looked at for substitutes.

In the LIFER system [24], an elliptical query is processed by matching it as a substring of the previous query. For example, the query, "What is the length of Santa Inez?" followed by the query, "of the Kennedy" would result in revising the latter query to "What is the length of the Kennedy?" by replacing the substring "of Santa Inez" with the substring "of the Kennedy."

We summarize our survey of natural language interfaces to database management systems in Table 1. In the first column, we list the various systems for natural language interface. The second column addresses domain independence (dependence) of natural language interfaces. Domain-independent systems can be transported across application domains without the need of extensive reprogramming. Domain-dependent systems, however, are designed to operate in particular domains. NLIs also vary in their ability to process elliptical queries, which we have discussed above. The ability of the natural language interface to support elliptical queries is specified under the column heading, Ellipsis. The fourth column specifies the type of queries that the natural language interface can support. Most NLIs are restricted in their ability to process data retrieval type of queries only. Queries that modify data (enter new data, or change existing data) require ensuring database integrity constraints, and are typically not supported. The fifth column in the table specifies the nature of the grammar rules that are used for processing natural language queries. Thus, some NLIs use grammar rules based on syntactic structures of natural language sentences, while others perform both syntactic as well as semantic analyses separately. Still others use semantic grammars and preclude any syntactic analysis of the natural language query.

## 3. The Functional Model, the Data Model, and the Fourth-Generation Interface

OUR PROPOSED METHOD BUILDS ON THE FUNCTIONAL AND DATA MODELS of the system. Furthermore, we assume that the system uses a fourth-generation interface tool for information retrieval and data entry. We discuss each of these components below.

For the purpose of illustration, we discuss these components in the context of a system that deals with computer integrated manufacturing of packaged food. The products' customers are both military and civilian. The system supports key manufacturing and management functions in four areas:

1. Managing contracts, orders and bidding process, with the following functional requirements:

\- Provide quotations on existing products: This function supports customer inquiries on pricing and delivery times on existing products.

\- Respond to new product inquiry: When the enterprise receives inquiries about new products, the R&D section of the enterprise determines the feasibility of manufacturing the new product, based on the existing production equipment.

\- Respond to DPSC contract solicitations: DPSC (Defense Personnel Supply

Table 1 Summary of Recent NLIs to DBMS

<table><tr><td>Systems</td><td>Domain</td><td>Ellipsis</td><td>Query type</td><td>Grammar</td></tr><tr><td>EUFID [44]</td><td>Independent</td><td>No</td><td>Retrieval</td><td>Semantic</td></tr><tr><td>Janas86 [26]</td><td>Dependent</td><td>Yes</td><td>Retrieval</td><td>Semantic</td></tr><tr><td>Hayes84 [23]</td><td>Dependent</td><td>Yes</td><td>Unspecified</td><td>Semantic</td></tr><tr><td>KID [25]</td><td>Independent</td><td>Unspecified</td><td>Retrieval</td><td>Syn. and sem.</td></tr><tr><td>LADDER [24]</td><td>Dependent</td><td>Yes</td><td>Retrieval</td><td>Semantic</td></tr><tr><td>LUNAR [48]</td><td>Dependent</td><td>Yes</td><td>Retrieval</td><td>Syntactic</td></tr><tr><td>PLANES [46]</td><td>Dependent</td><td>Yes</td><td>Retrieval</td><td>Semantic</td></tr><tr><td>SESAME [40]</td><td>Dependent</td><td>No</td><td>Retrieval</td><td>Syntactic</td></tr><tr><td>System X [34]</td><td>Independent</td><td>No</td><td>Retrieval</td><td>Syn. and sem.</td></tr><tr><td>TEAM [21]</td><td>Independent</td><td>Yes</td><td>Retrieval</td><td>Syntactic</td></tr></table>

Center) is the contracting agency for government contracts. The enterprise responds to bids on these contracts by selecting products that are compatible with business, estimating contract cost, and developing complete proposal for the contracts.

\- Manage current contracts and orders: This includes order entry and the regular monitoring of orders for providing timely information for customer and DPSC inquiries.

## 2. Manufacturing planning, with the following functional requirements:

\- Plan for DPSC contract requirements: This includes getting approvals for products to be produced, and setting production resource and personnel requirements to meet delivery dates.

\- Schedule manufacture of open orders: This activity schedules the line items of each open order based on a one-month time horizon and a next-day time horizon.

\- Plan new product manufacture: This activity includes the approval process for new civilian products.

## 3. Factory floor control, with the following functional requirements.

\- Control incoming material: This function includes the processes by which raw material inventory is replenished and accounted for, and the processes for physical handling and storage of material.

\- Control production process: This activity describes the routing of material in the factory area, the schedules used to control the routing, and the reports generated at each step of the process.

\- Control packaged product: This activity includes washing and drying packages, adding package identification, inspecting for package defects, reworking, and disposing of rejected products.

\- Update daily production record: Reports generated on the shop floor during daily production are used to update inventory records, processing records, and inspection records.

4. Finished goods control, with the following functional requirements.

\- Perform finished product quality assurance: Samples of finished products are taken from the production line and examined.

\- Control finished goods inventory: When a manufactured product leaves the production floor, it goes to either the labeling department or the finished goods inventory. This activity includes storing finished goods, labeling containers, reworking, and disposing of rejected products.

\- Ship finished product and update record: This activity takes products released for shipping, ships products to customers, and updates the appropriate finished goods inventory records.

## 3.1. Functional Model of the System

Here the focus is on developing a model of the information system in terms of the processes that make up the system and the information flow among them. Several functional analysis methods exist, such as SADT diagrams $[43]$ , structured analysis (SA) $[37, 38]$ , and the integrated computer aided manufacturing definition (IDEF0) $[15, 33, 50]$ . A comparative analysis of these methodologies is provided in $[5]$ . In our target application, we have used the IDEF0 methodology since it is the most widely used method in manufacturing systems $[15, 33, 50]$ .

The IDEF0 model of the target application is described in [6]. The IDEF0 technique models a system's activities and the information flow among them. To construct an IDEF0 model, we initially represent the generic activities of the system and then successively decompose each of these activities into greater details. The building blocks of the IDEF0 model are:

\- The activity (function) box: This represents an activity or function of a system. This could be either a generic activity or one of the detailed activities that constitute a generic activity.

\- Arcs: These represent inflow and outflow associated with a given function box. There are four types of arcs:

—Input: Represents the set of inputs, for example, information and materials required to perform the activity. This is depicted by an arrow entering the activity box from the left.

—Output: Represents the outflow from the activity. This is depicted by an arrow leaving the activity box from the right.

—Control: Represents the constraints that govern the process by which the activity is performed. This is depicted by an arrow entering the activity box from the top.

—Mechanism: Represents the human or equipment resources that are required in performing the activity. This is depicted by an arrow entering the activity box from the bottom.

More than 100 activities are identified in our target application area. Figure 1 shows the decomposition of the highest level of the IDEF0 model, Operate a Shelf Stable Food Manufacturing Enterprise (A0), into four generic activities: Manage Contracts, Orders, and Bidding Process (A1), Plan for Manufacture (A2), Manufacture Product (A3), and Control Manufactured Product (A4). See [6] for a detailed description of the IDEF0 model for the application area.

## 3.2. The Data Model

The technique used for data modeling is known as IDEF1X, a semantic data model based on Codd's relational data model $[14]$ and Chen's entity-relationship model $[10]$ . The building blocks of the IDEF1X model are entities, attributes, and relationships. Part of the IDEF1X model of the application is shown in figure 2. The IDEF1X model for our target application is described in more detail in $[1]$ .

Entities are represented by boxes in the IDEF1X model. Identifier-dependent (ID) entities, which are child entities whose existence depends on that of a parent entity, are shown by boxes with round corners. Identifier-independent (II) entities have an independent existence, and are shown by boxes with square corners.

The attributes of an entity are listed inside the entity box. The primary key attributes are listed above a horizontal line inside the entity box. ID entities “inherit” the primary key attributes of their parent entities. Multiple inheritance is allowed in this data model.

Relationships are represented by arcs. If one of the entities connected by an arc is a child entity, then the arc is represented by a bold line (for example, the arc “has” between Product and Material List). The dot at the end of an arc indicates that there is a one-to-many (1:m) relationship between the parent and child entities. If there are no dots, the relationship is one-to-one (1:1). Arcs connecting two entities that do not have a parent–child relationship are represented by a dashed line. Relationships and entities are named by verb and noun phrases respectively. A fully developed IDEF1X model replaces each m:n relationship with an additional entity and two 1:n relationships.

## 3.3. The Fourth-Generation Interface Tools

Form-driven user interfaces are among the most widely used fourth-generation interface tools. A form provides an easy way for non-SQL experts to retrieve, update, add, and delete desired information. In general, forms can be developed from studying user requirements, which include reports and user transactions that need to be supported. Forms can also be developed using CASE tools (such as the ORACLE CASE tools [36]).

Forms have certain desirable properties, including:

![](/api/attachments/MC5R4NNP/fulltext/images/3db1e24c8b2ef8614d3f07782e653d0499b15fe9ffbf4138c0012d467ce6232a.jpg)  
Figure 1. A Part of the IDEFIX Model

\- Familiarity: As mentioned in [11, 12], end users can effectively communicate using forms and interpret the contents of forms, due to familiarity.

\- Table look ups: Forms allow users to look up values for certain attributes during the process of formulating a query.

\- Triggers: Triggers are SQL commands that get activated by certain events. Triggers can be specified in the form definition, thereby incorporating various mechanisms such as validating data entry, calculating and displaying field values, protecting unintended errors such as entry of duplicate records or deletion of vital records, and so on.

A form represents a set of logically related data that provide the information required by a process. Processes are associated with the lowest-level activities (leaf activities) of the system. For example, “review current pricing and material cost” (RCPMC) is a leaf-level activity corresponding to the higher-level activity “provide quotations on existing products” (see figure 1). The processes associated with RCPMC are the functions required to perform that activity. These include:

\- Checking current published prices;

\- Checking current material pricing information (for key ingredients).

To develop a form, we first determine the functions supported by the system. Next, we identify the processes that perform these functions. Finally, we analyze the information requirements for each process. Associated with a given process is a set of information. For example, the set of information associated with the above processes are product and material pricing information. A form is developed for each set of logically related information. For example, there is a form associated with product price that gives the price of a product shown against the order quantity (discounts for larger quantities).

![](/api/attachments/MC5R4NNP/fulltext/images/f53ec662c272ef60b68699fe33a8074ae9be76f747009e27962a18c73a57cabb.jpg)  
Figure 2. A Part of the IDEFIX Model

In our CIM application, we have used the form-driven interface to the ORACLE database management system $[36]$ (referred to as SQL forms). Figure 3 presents an example of the SQL form corresponding to product pricing. Forms consist of several fields for data display and entry. The values corresponding to some of the form fields are entered by the user while others are generated by the system. Associated with each form field are a set of triggers. Triggers are SQL statements that are executed based on some preconditions specified in their definition. For example, there could be a “prefield,” “postfield,” or “postchange” trigger associated with a form field. A prefield trigger is activated before the cursor enters the field. For example, in figure 3, if “product id” is entered by the user, “product name” could be automatically generated by a prefield trigger associated with the field “product name.” A postfield trigger is activated if the cursor leaves that field. Thus, as an alternative arrangement to that described in the previous example, there could be a postfield trigger associated with the field “vendor id,” which retrieves the “vendor name” as soon as the cursor leaves the field “vendor id.” Triggers can be used to prevent violation of database integrity.

Product Price  
![](/api/attachments/MC5R4NNP/fulltext/images/cd90cefd75d0094263e9bd4197463f84a1f67cc4a75074cc2386a39313fd29fa.jpg)  
Figure 3. Product Pricing

constraints and maintain database consistency for transactions involving addition, deletion, and modification of data. For example, if a user enters a vendor id in the purchase order form (corresponding to a purchase-order relation in the database), there could be a postchange trigger associated with that form field, which checks whether such a vendor id exists in the vendor relation. Thus, the foreign-key dependency constraint can be preserved between the two relations “purchase-order” and “vendor.”

## 4. Proposed Methodology

WE USE A HYBRID SYSTEM OF INTERFACE IN A RELATIONAL database environment, where query processing is done by combining a set of fourth-generation interface tools (SQL forms) with a natural language query processor. The architecture of the natural language processing system is shown in figure 4. The two major components of the system are the natural language processor and the set of SQL forms. The natural language processor component consists of a lexicon, a parser, and a set of form definitions. The parser interprets the user query using the lexicon and the set of form definitions, and invokes the appropriate form. The control is returned to the natural language component after the query has been processed. Each of these subcomponents is discussed in detail later in this section.

![](/api/attachments/MC5R4NNP/fulltext/images/1ff7604d8d7d7278f4330783777595fc82ae32cdd15603d159848d3558db2eb3.jpg)  
Figure 4. System Architecture

When a natural language query is issued, the appropriate SQL form is identified. The ability to express a query in a natural language relieves the user from having to navigate through a network of menu screens.

To provide an overview of the proposed methodology, consider the activity “Provide quotations on existing products” (A11 in the IDEF0 model [6]). This activity starts when a customer inquires about a certain product. In response to the customer inquiry, the subactivity, “Review current pricing and material cost” (A111), is initiated. In A111, the sales manager performs the following actions:

1. Refer to the database of current published prices.

2. Since material cost is a large proportion of the total cost, some prices may be subject to the current market cost of a key ingredient. In that case, the material relation is checked for current material prices.

From the above, we surmise the following dialog between the sales manager (hereafter referred to as U) and the system (hereafter referred to as S):

• U1: What is the price of minestrone?

\- S1: The system retrieves the form for product price and processes the query by assigning the value “minestrone” to the form field product name. Figure 3 shows the response of the system.

• U2: Show material pricing.

\- S2: Minestrone's material pricing? (yes/no)

Since the user did not specify the product for which material pricing is required, the system has to derive it from the context of the discourse. From the previous query, the product is inferred to be “minestrone.”

• U3: Yes.

\- S3: The result of processing the query is a breakdown of each material used in minestrone with its unit price, and the total cost of minestrone per container.

In handling natural language queries, the query processor uses contextual knowledge that allows a user to enter into an interactive dialog with the system. As shown above, this allows the user to carry out functions that require multiple, interrelated queries to be processed. The method for using contextual knowledge is discussed in section 4.5.2.

The natural language component takes a user query expressed into a natural language, and maps it to a predefined SQL form that can answer the query. The process of mapping a user query to a form consists of two steps:

1. Determining the information requirements of the user query.

2. Identifying the form that satisfies the information requirements determined in the previous step.

In [2], we described a method for making use of predefined forms. We differ from the approach presented there by avoiding a complete lexical analysis of the user query. Rather, to process the user query, we identify a predefined form by starting from the form definition. We discuss below the three major components of the proposed NLI. This is followed by a discussion of the steps for processing a user query expressed in a natural language.

## 4.1. Parsing

Parsing is the problem of constructing a derivation for a user input from a formal definition of a grammar. Our approach in parsing user input is similar to that of [23], but we differ in that our approach is oriented to processing user queries. In selecting the grammar for such a system, it is important to determine the types of transactions that the system has to support. Our focus here is on developing an NLI for a restricted and well-specified domain. Thus, boundaries can be drawn on both the domain knowledge as well as the types of transactions.

The proposed NLI is developed based on the following hypotheses:

H1: Users will use the system as a tool to perform the functions depicted in the functional model of the system (in our case, it is the IDEFO model which is described in detail in [6]).

The CIM system's functionalities are depicted in the functional model (IDEF0). Since the NLI is an interface to the system, by analyzing the functions in the functional model (IDEF0), we can predict the nature of transactions that need to be supported.

H2: Users would restrict their discourse with the system to the information stored therein.

As a corollary of the above hypothesis, we limit our domain of discourseto the data model (IDEF1X, see [1] for related details), which captures the database semantics.

H3: User queries may contain extragrammatical and/or elliptical inputs, and noise words.

Instead of performing a complete lexical analysis of the user query, we focus only on the relevant part(s) of the query. Noise words like “could you please” and “I would like to” are avoided in processing user queries.

Fragment grammars are stored as part of the form definitions. Once a form has been identified, these fragment grammars are matched against the user query to identify the information requirements of the user query. For example, in the query, "What is the price of minestrone?" we are interested in the noun-phrase, "price of minestrone," where the prepositional-phrase "of minestrone" identifies the object for which the "price" is required.

## 4.2. Form Definition

Corresponding to each form, we develop a form definition in terms of the form fields and surface representations corresponding to the fields. If the surface representation of a form field matches part of the user query, then the form field is assigned a value by using that part of the user query. For example, a form for product information (as depicted in figure 3) has the definition in figure 5.

Each form is uniquely identified by a form name. Associated with each form is a form object that corresponds to one or more identifier-independent entities in the data model. Associated with each form are two lists of form fields: user-defined and system-defined [12]. User-defined fields are those whose values are given by the user. The values corresponding to system-defined fields are derived by the system in response to user queries. A form definition also specifies fragment grammars that correspond to the surface structure of the relevant clause of a user query. Thus, in the product information form, these are ACT, which stands for queries in which the information requested is specified in the active mode. These include both WH-queries (queries starting with “what,” “which,” etc.), as well as commands (queries starting with “list,” “give,” etc.). An example of a WH-query (ACT) is “what is minestrone’s price?” In this query, the subject noun phrase (SUBJ-NOUN) is “minestrone,” which has a suffix “s” (as mentioned in the template) and the object noun phrase (OBJ-NOUN) “price.” A PSV query is one in which the information requested is specified in the passive mode. An example of this type of query is “What is the price of minestrone?” Here the OBJ-NOUN is “price,” which is followed by the preposition “of,” and the SUBJ-NOUN “minestrone.” SUBJQ refers to a query where an entire noun group is the subject (see [47]). An example of this type of query is “How much does minestrone cost.” In this query, the SUBJ-NOUN “minestrone” is preceded by the auxiliary verb(vaux) “does,” and followed by the transitive verb (VTRANS) “cost.” The processing of these queries is discussed in a subsequent section. All of the grammar fragments correspond to the relevant noun clauses in the user query. The templates within pointed brackets (<>) are substitutable by words in the user query that belong to the same grammatical category. Those within square brackets ([ ]) can be omitted, or replaced by words of other grammatical categories in extragrammatical inputs.

```txt
FormName: ProductInformation
FormObject: Product
FormFields:
User-defined: {ProductID, ProductName
System-defined: {NetWt, CanSize, QtyPerCase,
StdRejectRate, BreakQty, Price, PriceValidUntil}
ACT: <SUBJ-NOUN> [suffix (s)] <OBJ-NOUN>
PSV: <OBJ-NOUN> [preposition (of[for)] <SUBJ-NOUN>
SUBJQ: [vaux] <SUBJ-NOUN> <VTRANS>
user-defined: <SUBJ-NOUN>
system-defined: <OBJ-NOUN>
```  
Figure 5. Form Definition: Product Pricing

Another form definition that deals with material pricing is shown in figure 6.

## 4.3. The Lexicon

In addition to the form definitions described above, the system contains a lexicon, where each word recognized by the system is listed in alphabetical order. Corresponding to each word is information about its grammatical category (noun, verb, adjective, etc.), type information (whether it is a value corresponding to a form field, or a form field itself), and whether it uniquely identifies a form. The lexicon contains synonyms of the words that appear in the forms (as form fields) or in the database as values. Part of the lexicon is shown in figure 7.

In the lexicon in figure 7, the grammatical category of the word “cost” could be either noun or transitive verb (vtrans). The word “cost” is synonymous (syn in the lexicon) with the word “price.” Words such as “does” and “how” are not used in processing user queries, and hence the only information stored in the lexicon about such words are their grammatical categories. As mentioned above, forms are uniquely identified by entity names (either composite or single). Thus, the lexicon contains the information of whether or not a word is a form object. For example, the lexicon entry corresponding to the word "material" specifies it to be a form object for the form MaterialPricingInformation. For instances of form objects, the field name as well as the form object is specified. Thus, corresponding to the word "minestrone," the information that it is a value of the form field "product-name," associated with the form object "product," is stored in the lexicon. For entity identifiers ("ids"), instead of storing each "id" individually, we store a template associated with it. For example, the "ids" that are stored in the lexicon corresponding to the entities "customer," "product," and "material" are CU<X>, PR<X>, and ME<X>, respectively, where <X> will match any whole number.

```txt
FormName: MaterialPricingInformation
FormObject: Material
FormFields:
User-defined: {ProductID, ProductName}
System-defined: {MaterialId, MaterialDescription, Cost,...}
ACT-ACT: <SUBJ-NOUN> [suffix(s)] <OBJ1-NOUN>
<OBJ2-NOUN>[<OBJ3-NOUN>]
ACT-PSV: <SUBJ-NOUN> [suffix(s)] <OBJ2-NOUN>
[preposition(of|for)] <OBJ1-NOUN>
PSV-ACT: <OBJ1-NOUN> <OBJ2-NOUN> [<OBJ3-NOUN>]
[preposition(of|for)] <SUBJ-NOUN>
PSV-PSV: <OBJ2-NOUN> [preposition(of|for)] <OBJ1-NOUN>
[preposition(of|for)] <SUBJ-NOUN>
User-defined: <SUBJ-NOUN>
System-defined: <OBJ2-NOUN>.
```  
Figure 6. Form Definition: Material Pricing Information

We restrict the size of the lexicon by storing only those words that the system is likely to encounter. This includes don't-care words (pronouns, intransitive verbs, prepositions, articles, conjunctions, etc., that have no information content in themselves), noun-phrases that constitute values of form fields, transitive verb-phrases that are used as relationships in the data model (IDEF1X) [1], one template corresponding to each identifier-independent entity in the data model (IDEF1X), and synonyms of the noun and verb phrases mentioned above. The number of don't-care words is less than 1,000 (this is typical of NLIs [26]). The average number of user-defined fields for the forms is two. Out of these, about half correspond to values of identifiers. Since we store one template for the identifier of each identifier-independent entity, the number of distinct values of these is equal to the number of identifier-independent entities in the data model (IDEF1X). The rest of the user-defined form fields correspond to descriptor values (e.g., names of vendors for the forms providing vendor

```txt
1. cost: noun, vtrans; syn: price.
2. does: vaux.
3. how: det.
4. is: verb.
5. material: noun; form: MaterialPricingInformation.
6. minestrone: noun; value-of: product-Name; form object: product.
7. minestrone's: root: minestrone; inflection: suffix (s).
8. of: preposition.
9. price: noun.
10. pricing: noun; syn: cost.
11. product: noun; form: ProductInformation.
12. what: det.
```

## Figure 7. A Part of the Lexicon

information). Since the form fields correspond to attributes of identifier-independent entities, and the data model (IDEF1X) does not support multivalued attributes, the maximum number of distinct values of the form fields is equal to the number of tuples of the identifier-independent entities in the data model (IDEF1X). Thus, if the number of identifier-independent entities in the application is n, and the average number of tuples in each of these entities is $n_{t}$ , then the maximum number of descriptor values that we store in the lexicon is $n * n_{t}$ . In addition, we store the names of the entities and relationships in the data model (IDEF1X) and their synonyms. In contrast, each relation for each identifier-independent entity will have additional values corresponding to the other fields of the relation (for example, the vendor relation will store values corresponding to fields like vendor address, contact person, telephone number, etc., in addition to vendor names). The database will also be storing relationship relations (for example, vendor-material cross-reference). Thus, in our methodology, the lexicon will be substantially smaller in size in comparison with the database for any application. In our target application, the size of the database is estimated to be more than 300 times that of the lexicon (see [20] for further detail). It is also shown in [20] that larger databases will have relatively smaller lexicon sizes.

Another issue is the search time of the lexicon. Since the entries in the lexicon are ordered alphabetically, we perform a binary search on the lexicon. Thus, the order of magnitude for the search time is logarithmic in the size of the lexicon.

## 4.4. Processing User Queries

The following steps summarize our methodology for processing user queries:

Step 1: All inflections in the input are removed after noting the type of inflection. The root word is identified from the lexicon, and processed subsequently.

Step 2: The words from step 1 are scanned to determine if any form can be identified. If a word corresponds to a value of a form field, then that form field is used to identify a form. If a word corresponds to a value of a form object, then the corresponding form is identified. If more than one form is identified from the user query, we first try to identify the right form by matching the fragment grammars, and the user and system-defined fields in the form definition with the user query. An example of such a query is described in section 4.6. If no resolution can be made about the right form automatically, the user is consulted.

Step 3: The input is matched against the fragment grammars associated with the form. If a match is found, the templates are instantiated with words in the input. Templates in angle brackets would match any word in the input that belongs to the same grammatical category. The templates in square brackets must either be present as they are in the grammar, or absent completely.

Step 4: If the previous step returns a fragment grammar, then the user-defined and system-defined fields are identified from the templates. The user-defined and system-defined fields, as derived from the input are checked against the lists corresponding to form fields in the form definition. This prevents queries like “What is the employee of minestrone?” from being processed. Since “employee” is not a valid form field, such a query will not be processed even if it satisfies all other requirements. The query is processed by running the form and specifying the values corresponding to the user-defined form fields.

As an example, consider the following user query:

## Q1: "What is the price of minestrone?"

Since there are no inflected words, we go to step 2 of the algorithm. The word “minestrone” is an instance of the form field “ProductName,” which is an attribute of the form object “product.” Thus, we look at the form corresponding to “product”: ProductInformation. In step 3, we try to match the user query with one of the fragment grammars. The nouns in the user query are “price” and “minestrone.” In ACT, SUBJ-NOUN matches “price,” and OBJ-NOUN matches “minestrone,” but there is no suffix to minestrone and there is a preposition “of” in the clause “price of minestrone.” Thus, we reject ACT as a possible grammar, and go to the next one. In PSV, OBJ-NOUN matches “price,” preposition “of” matches “of” in the user query, and SUBJ-NOUN matches “minestrone.” Thus, we return PSV and go to step 4. Since “price” and “ProductID” are valid form fields, we run the form “ProductInformation” with the value of “ProductName” as “minestrone.”

## 4.5. Processing Extragrammatical Inputs

We group extragrammatical inputs into the following categories:

1. Queries with misspelled words.

2. Queries with incorrect grammatical form.

3. Elliptical queries with reference to one or more previous queries.

4. Elliptical queries with no reference.

Typically, the first three categories are dealt with by extant NLIs. We describe our proposal for dealing with these types of queries.

## 4.5.1. Queries with Misspelled Words and Incorrect Grammatical Form

1. Queries with misspelled words: Misspelled words are identified in step 1. If any word is not found in the lexicon, its close neighbors are identified and listed to the user for replacement.

2. Queries with incorrect grammatical form: We hypothesize that extragrammatical queries will occur due to the use of colloquial grammar, truncation of sentences, and mistakes, rather than because of intentional deviations from grammar rules. Thus, a query such as "What is price minestrone" is unlikely. Such inputs will require reformulation with the help of the user. Queries with limited deviations are modified by the system and verified by the user. To illustrate, consider the following query:

## Q2: What price is minestrone?

Following steps 1 and 2, we retrieve the form ProductInformation. In step 3, the fragment grammar ACT is chosen at first. The word "price" matches with SUBJ-NOUN and "minestrone" matches with OBJ-NOUN. Since "is" does not match the suffix, we try the other two fragments. PSV is not matched because "is" does not match a preposition. SUBJQ does not match as there is no VTRANS in Q2. Thus, the query is recognized as an extragrammatical query. We try to match ACT again by replacing suffix (s) with is. This time SUBJ-NOUN matches "price," and OBJ-NOUN matches "minestrone." However, in the user-defined list, "price" does not occur. Therefore, ACT is rejected as a valid choice. Next, in PSV, OBJ-NOUN matches "price" and SUBJ-NOUN matches "minestrone." "Minestrone" is a value of ProductName, which is listed in the user-defined list, and "price" is listed in the system-defined list. Thus, the noun-phrase "price of/for minestrone" is put to the user for verification as an acceptable interpretation. If the user agrees with the rephrased version, the query is processed.

## 4.5.2. Handling Ellipsis

In general, database queries can be classified into “open” and “closed” queries, as suggested in [26]. Closed queries are those that result in yes/no answers. An example of a closed query is: “Does Shop-Rite supply ceci-beans?” Examples of open queries are (but are not limited to) queries with restricted retrieval (e.g., “Find all vendors that supply ceci-beans”), and queries with interrogative pronouns (e.g., “Which vendors supply ceci-beans?”). While ellipsis is a general problem that any natural language understanding system encounters, in database queries the types of ellipsis encountered can be grouped into the following categories [26]:

1. Illocution ellipsis: When the query cannot be determined to be open or closed, it is said to have illocution ellipsis. For example, the query “Bread crumbs?” could mean “Which vendors supply bread crumbs?” (open query), if preceded by the query “Which vendors supply ceci-beans?” or it could mean “Are there any vendors that supply bread crumbs?” (closed query), if preceded by the query “Are there any vendors that supply ceci-beans?” Thus, the query “Bread crumbs?” is said to have illocution ellipsis.

2. Target ellipsis: When an elliptical query can be identified to be an open query, but which database objects (relations, attributes) are referred to by the query cannot be determined, it is said to have target ellipsis. For example, the query "of small business vendors" is an open query that could mean "List some attribute(s) of small business vendors," where the attribute(s) that have to be listed is (are) unspecified. Thus, it has target ellipsis.

3. Complete or partial qualification ellipsis: When it is not clear which object(s) the query is referring to (either incompletely specified, or not specified at all), the query is said to have a partial or complete qualification ellipsis, respectively. For example, the query “address?” when preceded by the query “List the names of all vendors that supply ceci-beans,” may be interpreted as “list the addresses of all vendors that supply ceci-beans.” Here, the object “vendors that supply ceci-beans” is not specified; however, the attribute “address” is specified. Thus, it has a partial qualification ellipsis.

More than one type of ellipsis could be combined in a query. However, it may not be possible to resolve the meaning if certain types of ellipses are combined. Thus, a combination of target and complete qualification ellipsis will be outside the domain of the database and, hence, may not have to be dealt with. A combination of target and partial ellipsis may have multiple interpretations, and thus may have to be resolved by the user.

A more general categorization of anaphoric references is given in [45]:

1. Substitutes and ellipsis: This refers to the process of substituting the meaning of some previously mentioned word, phrase or clause.

2. Definite noun-phrases: definite noun-phrases like “the three red blocks” in SHRDLU [47] require that the objects referred to be identified. Thus, all objects that fit the description “red blocks” are first identified, and then the three most recent red blocks are chosen to be the objects referred to by the definite noun-phrase. In QPROC [45], in addition to words, phrases, and meanings, preset values (like date and time) and previous references are used in filling missing slots.

3. Pronominal reference: These include references to previously mentioned objects. For example, in the two queries, "Which vendors supply ceci-beans?" followed by "Which of these are in small business?" the second query refers back to the “vendors that supply ceci-beans.” The system has to infer which object (for example, vendors and not ceci-beans, in the last example) is being referred to. Because of the definite noun-phrase reference problem, the context should include previous references in addition to just words, phrases, and meanings.

Elliptical queries are processed by revising the query based on the information given in previous queries. The issues that need to be addressed here are: How to identify a query as an elliptical query, how to identify what information is missing in an elliptical query, how to identify the missing information from previous query(s), and how many previous queries should be referred to.

In most extant NLIs, an elliptical query is processed by making use of contextual knowledge. Contextual knowledge usually consists of the information provided by the user in one or more previous queries. We use form definitions as our context. Thus, if the user query has no reference, it can still be answered by looking for the missing information from the form retrieved by that query. If a query, on the other hand, has reference to a previous query(s), the missing information can be obtained from either the form associated with the current query or the form(s) retrieved in answering previous queries. If no form can be identified from the user query, then the user is given a list of the entities for which there is a form definition, and the user is asked to select one. Below, we discuss these cases individually.

1. Elliptical queries with reference to previous queries: In order to illustrate our method, we assume that query Q1 has already been processed, and the following query has been issued after that:

## Q3: Show its material pricing.

The query Q3 has the pronominal reference “its” to “minestrone,” which is mentioned in a previous query (Q1). In processing Q3, step 1 identifies “its” as an inflected word with root “it,” and suffix “s.” In step 2, the word “material” identifies the form MaterialPricingInformation, and “pricing” picks up the synonym “cost.” The clause “its material pricing” matches the grammar fragment ACT-ACT as follows: SUBJ-NOUN matches “it,” the suffix (s) matches the input “s,” OBJ1-NOUN matches “material,” and OBJ2-NOUN matches “pricing.” Since “it,” the SUBJ-NOUN, is not listed in the user-defined field list, the query is identified as an elliptical query. Next, we see if “its” can be substituted by a user-defined field specified in any previous transactions. In Q1, the ProductName was specified to be “minestrone.” Thus, we check with the user whether minestrone is the product referred to. The noun-phrase “minestrone’s material pricing” is suggested to the user. If the user consents, the revised query “minestrone’s material price” is processed.

2. Elliptical queries with no reference: It is possible to have user queries that are incomplete in their specifications, and yet have no previous references. An example of such a query is Q4:

Q4: Product pricing.

In response to Q4, the system retrieves the form "ProductInformation." However, since neither of the user-defined fields (ProductID and ProductName) is mentioned, the form is displayed to the user. Upon entering the value corresponding to a user-defined field, the form retrieves the relevant information.

## 4.6. Update Requests

We divide update requests into two types: data entry and data modification. Certain key words like “enter,” “change,” “modify,” and the like in the input identify the user request as data entry or modification request. These two types of transactions are discussed in more detail below.

1. Data entry: Since the system consists of 4GL forms in addition to a natural language processor, users have the option either to use the forms to enter their requests or to use free English. In fact, for transactions like data entry, it is more useful to use the forms than to enter the data in natural language sentences. Consider the following transaction:

## Q5: Enter material pricing information for minestrone.

In response to Q5, step 2 generates two forms, “MaterialPricingInformation,” corresponding to the form object “material,” and “ProductInformation,” corresponding to the form object “minestrone.” In such cases, we try to match both forms against the information in the input. The order in which the forms are tried is arbitrary. For the purpose of illustration, let us assume that ProductInformation is tried first. Since none of the grammar-fragments contain three consecutive nouns, the match fails. Thus, we proceed to the next form identified from the input. In the form “MaterialPricingInformation,” the fragment PSV-ACT matches the input “material pricing information for minestrone” by instantiating <OBJ1-NOUN> with “material,” <OBJ2-NOUN> with “pricing,” and [<OBJ3-NOUN>] with “information.” The square brackets in the template [<OBJ3-NOUN>] indicate that this template can be omitted in certain queries (as in “material pricing for minestrone”). Furthermore, “pricing” matches the system-defined field “cost” (since it is synonymous), and “mine-strone” matches the user-defined field “ProductName.” Since the user’s input is a data entry request (identified by the keyword “enter”), the form “Material-PricingInformation” is presented to the user. If such information already exists in the database, it is retrieved, and it is up to the user to modify the existing information.

2. Data modification: These requests are identified by key words such as "modify," "change," and the like. Q6 and Q7 are examples of such requests: Q6: Modify material pricing for minestrone.

## Q7: Change the can size of minestrone from #5 to #10.

In both of the above cases, the relevant form is retrieved by making use of the four steps discussed above. The relevant records are retrieved, and the user is requested to make the changes to the existing records through the form.

## 5. Conclusion

WE HAVE DESCRIBED A METHODOLOGY FOR DEVELOPING form-based natural language interfaces to systems in well-defined domains. The interface consists of a set of fourth-generation interface tools (SQL forms), a set of form definitions, a lexicon, and a parser. The forms are developed from the functional and data models of the system. A form definition consists of form name, a form object, a set of form fields, and a set of fragment grammars. A form object can be either a single or composite entity that uniquely identifies a form. Form fields specify the database fields whose values can be entered by the user (user-defined), and others whose values can be derived by the system (system-defined). Fragment grammars are templates that identify the information requested by the user query. The lexicon consists of all words recognized by the system, their grammatical categories, synonyms, and their associations (if any) with database objects and forms. The parser scans a natural language query to identify a form in a bottom-up fashion. The information requested in the user query is determined in a top-down manner by matching the grammar fragments associated with a form against the user query. Extragrammatical inputs with limited deviations from the grammar rules are supported. Elliptical queries are supported by deriving the information missing from the user query by making use of the information specified in previous queries and in the forms. Data entry and update transactions are supported, and database integrity constraints are checked in dealing with such queries.

The framework and architecture presented and illustrated with examples from the CRAMTD project are intended for generalizations to other application areas. In order to apply this framework to a new application area, the following components would need to be constructed: functional and data models for the application, SQL forms for each of the functions to be supported by the system, and the natural language processor for the set of system functions as represented by these SQL forms.

## REFERENCES

1. Adam, N.R.; Boucher, T.O.; Chamberlin, T.; and Weber, J. Informational architecture for packaged food manufacturing. Technical Report TWP 52 CAFT, Rutgers University, April 1992.

2. Adam, N.R.; Boucher, T.O.; and Gangopadhyay, A. A method for natural language query processing in a computer integrated manufacturing system. In V.S. Jacob and H. Pirkul (eds.), Proceedings of the 25th Annual North American Conference of the IBSCUG. July 1992, pp. 53–68.

3. Adam, N.R.; Gangopadhyay, A.; and Geller, J. Design and implementation of a knowledge based query processor. International Journal of Intellignet and Cooperative Information Systems, 2, 2 (1993), 107–125.

4. Adam, N.R.; Gangopadhyay, A.; and Geller, J. Knowledge based query processing using preoptimized queries. In Proceedings of the First International Conference on Information and Knowledge Management. November 1992, pp. 535–544.

5. Batini, C.; Ceri, S.; and Navathe, S.B. Conceptual Database Design: An Entity-Relationship Approach. New York: Benjamin/Cummings, 1992.

6. Boucher, T.O.; Jafari, M.A.; Kim, A.; and McPhail, J. Functional architecture for packaged food manufacturing. Technical Report TWP 37 CAFT, Rutgers University, 1991.

7. Chakravarty, U.S.; Fishman, D.H.; and Minker, J. Semantic query optimization in expert

systems and database systems. In L. Kershberg (ed.), Expert Database Systems: Proceedings from the First International Workshop. 1986, pp. 659–674.

8. Chakravarty, U.S.; Grant, J.; and Minker, J. Logic-based approach to semantic query optimization. ACM Transactions on Database Systems, 15, 2 (1990), 162–207.

9. Chakravarty, U.S.; Minker, J.; and Grant, J. Semantic query optimization: additional constraints and control strategies. In L. Kershberg (ed.), Expert Database Systems: Proceedings from the First International Workshop. 1986, pp. 345–379.

10. Chen, P. The entity-relationship model—toward a unified view of data. ACM Transactions on Database Systems, 1, 1 (1976), 9–36.

11. Choobineh, J. FORMFLEX: a user interface tool for forms definition and management. In J.M. Carey (ed.), Human Factors in Management Information Systems. NJ: Ablex, 1988, pp. 117–133.

12. Choobineh, J.; Mannino, M.V.; and Tseng, V.P. A form-based approach for database analysis and design. Communications of the ACM, 35, 2 (1992), 108–120.

13. Clifford, J. Formal Semantics and Pragmatics for Natural Language Querying. Cambridge: Cambridge University Press, 1990.

14. Codd, E. A relational model for large shared data banks. Communications of the ACM, 13, 6 (June 1970), 377–387.

15. Colquhon, G.J., and Baines, R.W. A generic IDEFO model of process planning. International Journal of Production Research, 29, 11 (1991), 2239–2257.

16. Dilts, D.M. Integration of computer integrated manufacturing databases using artificial intelligence. In M. Oliff (ed.), Expert Systems and Intelligent Manufacturing. New York: Elsevier, 1988, pp. 327–334.

17. Dilts, D.M., and Wu, Wenhua. Using knowledge-based technology to integrate CIM databases. IEEE Transactions on Knowledge and Data Engineering, 3, 2 (1991), 237–245.

18. Embley, D.W. NFQL: the natural forms query language. ACM Transactions on Database Systems, 14, 2 (1989), 168–211.

19. Flatau, U. Designing an information system for integrated manufacturing systems. In Design and Analysis of Integrated Manufacturing Systems. Washington, DC: National Academic Press, 1988, pp. 60–78.

20. Gangopadhyay, A. Using Conceptual Dependencies for Database Design and Query Processing an a CIM Environment. Ph.D. dissertation, Rutgers University, May 1993.

21. Grosz, B.J.; Appelt, D.E.; Martin, P.A.; and Periera, F.C.N. TEAM: an experiment in the design of transportable natural-language interfaces. Artificial Intelligence, 32 (1987), 173–243.

22. Hammer, M., and Zdonik, S.B. Knowledge based query processing. In Proceedings of Very Large Database Conference. 1980, pp. 137–147.

23. Hayes, P.J. Entity-oriented parsing. Proceedings of the 10th International Conference on Computational Linguistics. 1984, pp. 212–217.

24. Hendrix, G.; Sacerdoti, E.; Sagalowicz, D.; and Slocum, J. Developing a natural language interface to complex data. ACM Transactions on Database Systems, 3, 2 (1978), 105–147.

25. Ishikawa, H.; Izumida, Y.; Yoshino, T.; Hoshiaoi, T.; and Makinouchi, A. KID, designing a knowledge-based natural language interface. IEEE Expert, 2, 2 (Summer 1987), 56–71.

Bolc and M. Jarke (eds.), Cooperative Interfaces to Information Systems. New York: Springer-Verlag, 1986, pp. 143–188.

27. Jarke, M. External semantic query simplification: a graph theoretic approach and its implementation in PROLOG. In L. Kershberg (ed.), Expert Database Systems: Proceedings from the First International Workshop. 1986, pp. 675–690.

28. Jarke, M.; Clifford, J.; and Vassiliou, Y. An optimizing PROLOG front-end to a relational query system. In Proceedings of the ACM-SIGMOD Conference. 1984, pp. 296–306.

29. Jarke, M., and Koch, J. Query optimization in database systems. Computing Surveys, 16, 2 (1984), 112–152.

30. Jones, A.; Barkmeyer, E.; and Davis, W. Issues in the design and implementation of a system architecture for computer integrated manufacturing. International Journal of Computer Integrated Manufacturing, 2, 2 (1989), 65–76.

31. King, J. QUIST: a system for semantic query optimization in relational databases. In Proceedings of the Very Large Database Conference. 1981, pp. 510–517.

32. King, J. Query Optimization by Semantic Reasoning. UMI Research Press, 1984.

33. Mackulak, G.T. High level planning and control: an IDEFO analysis for airframe manufacture. Journal of Manufacturing Systems, 3, 2 (1984): 121–133.

34. McFetridge, P.; Hall, G.; Cercone, N.; and Luk, W.S. System X: a portable natural language interface. In R. Goebel (ed.), Proceedings of the Seventh Biennial Conference of the Canadian Society for Computational Studies of Intelligence. 1988, pp. 30–38.

35. Natural Language Inc. Natural Language Retrieval of Database Information. 1986.

36. ORACLE Corporation. CASE Dictionary Reference Guide. Redwood City, CA: 1991.

37. Ross, D. Structured analysis (SA): a language for communicating ideas. IEEE Transactions on Software Engineering, SE-3, 1 (1977), 16–34.

38. Ross, D., and Shoman, K. Structured analysis for requirements definition. IEEE Transactions on Software Engineering, SE-3, 1 (1977), 6–15.

39. Roussopoulos, N. The logical access path schema of a database. IEEE Transactions on Software Engineering, SE-8, 6 (1982), 563–573.

40. Sabbagh, S. SESAME: an application of entity relationship models to a natural language user interface. In H. Kangassalo (ed.), Entity-Relationship Approach: The Core of Conceptual Modeling. New York: North Holland, 1991, pp. 319–331.

41. Shenoy, S.T., and Ozsoyoglu, Z.M. A system for semantic query optimization. In ACM SIGMOD. 1987, pp. 181–195.

42. Shenoy, S.T., and Ozsoyoglu, Z.M. Design and implementation of a semantic query optimizer. IEEE Transactions on Knowledge and Data Engineering, I, 3 (September 1989), 344–361.

43. Softech. An Introduction to SADT. 1978.

44. Templeton, M., and Burger, J. Considerations for the development of natural-language interfaces to database management systems. In L. Bolc and M. Jarke (eds.), Cooperative Interfaces to Information Systems. New York: Springer-Verlag, 1986, pp. 67–99.

45. Wallace, M. Communicating with Databases in Natural Language. Ellis-Horwood, 1984.

46. Waltz, D.L. An English language question answering system for a large relational database. Communications of the ACM, 21, 7 (1978), 526–539.

47. Winograd, T. Understanding Natural Language. New York: Academic Press, 1972.

48. Woods, W.A. Semantics and quantification in natural language question answering. In M. Yotis (ed.), Advances in Computers. New York: Academic Press, 1978, pp. 1–87.

49. Woods, W.A. Transition network grammars for natural language analysis. Communications of the ACM, 13 (1970), 591–602.

50. Young, R.E., and Vesterager, J. An approach to CIM system development whereby manufacturing people can design and build their own CIM systems. International Journal of Computer Integrated Manufacturing, 4, 5 (1991), 288–299.
