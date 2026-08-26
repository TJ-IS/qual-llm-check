---
otero_id: 17812
otero_key: "7R8X95J4"
title: "A DBMS architecture for prudent managers"
authors: "John L. Berg"
year: "1978"
journal: "Information & Management"
doi: "10.1016/0378-7206(78)90017-4"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A DBMS Architecture for Prudent Managers

John L. Berg

Building 225, Room A-265, National Bureau of Standards, $^{1}$ Washington, DC 20234, USA

The investment required to use data base technology forces ADP managers to consider carefully DBMS selection and its risks. A manager must consider actions which will anticipate and control future costs. By combining the framework proposed in the ANSI/X3/SPARC Study Group final report with the CODASYL DBMS specifications and adding the administrative control of standards, a manager would have a database environment that offers sufficient flexibility to realize DBMS benefits from existing technology while minimizing later costs in converting to improved technology.

Keywords: Standards, DBMS, ANSI/SPARC, Database, CODASYL.

![](/api/attachments/7R8X95J4/fulltext/images/a989dff3f5791ecacb82cbea3fe1f68c9531e4bfe1f58dd96b2e4f7d5b733057.jpg)

John L. Berg is a senior Computer Scientist within the Systems and Software Division of the Institute for Computer Sciences and Technology at NBS. His responsibilities include data base management systems and privacy issues as they relate to U.S. Federal Government practices. He is currently chairing the ANSI X3/SPARC Data Base Systems Study Group which is responsible for recommending actions to coordinate

ANSI data base activities and for providing liaison with other interested data base system groups. He recently chaired a Federal Information Processing Standards Task Group on DRMS Standards. His 19 years in the computer industry include positions with computer manufacturers, software companies, and consulting firms. His current technical interest is the development of an overall data base system architecture that serves user needs, meets the goals of standardization, and provides a technically sound bridge from current systems into future systems. Readers with similar interests or who have recommendations are invited to correspond with him.

$^{1}$ Contribution of the National Bureau of Standards (not subject to copyright).

## 1. Introduction

## 1.1. Purpose of this paper

Consider the risks faced by a manager considering data base technology. A major pitfall would be to commit to a current DBMS that may soon become obsolete. After the significant investment to construct the database, write the application programs, and train people, how long will he have to amortize this cost? Will it be cheaper to convert to improved data base technology from his current position rather than via an expensive, interim database system? On the other hand, will converting to new hardware from a database environment be easier than from a non-database environment and is hardware change likely within the lifespan of the first base?

This paper proposes a DBMS architecture that permits immediate use of database technology, acceptance of evolutionary improvements to data base systems, and access to several data models.

## 1.2. Context

Is database technology growing or at a plateau which will provide a stable foundation for future implementation decisions? Will new data models continue to be developed at the rate of the previous years [9]? A group of experts surveyed database technology and reported [3] that the most likely future scenario would be continued evolutionary growth with no sudden revolutionary change.

Certainly, the number of proprietary DBMS using a variety of different data models has mushroomed and this indicates a definite market for DBMS. Som may argue that the present proliferation of different data models results from the fact that, "not all people think alike, so that different intellectual tools may appeal to different people. Hence, different data models may be needed" [9]. Others [16] have concluded that "[t]he overconservative stance of the [computer] manufacturer toward data base management software, or "waiting in the weeds" as it is called, to see what the major manufacturer does while they in turn wait to see how CODASYL standards turn out, has allowed the development of a minor industry which is marketing data base management software".

These two widely divergent views suggest important courses of action for the 1-P manager. He should plan to cope with change and he should find a means to insulate himself from vendor product specification changes.

## 1.3. Assumptions

DP manager cannot accept the simple assertion that "more study is necessary." The history of DBMS technology argues that changes are inevitable. Consequently, there will never be a time when a system environment as large and complex as is possible with data base technology will have equally well developed components. Managers facing decisions about the readiness of data base systems will ask pragmatic questions: "If not now, when?", "And what do I gain (or lose) by waiting?" We assume that technological changes in the immediate future will be evolutionary and that standards will exist to manage this evolution.

In order to insure broad implementation of a data base system, its specification must be freely available to any implementor, evolutionary, clear, precise, and subject to continual review by a competent body. Further, one must assume that the development of specifications represents a significant investment of financial and other resources over a substantial period of time: e.g., a year or more.

## 1.4. Goals

A manager would like to use database technology with some knowledge (and acceptable degree of control) of future costs. He wants:

1. To obtain the benefits and cost savings of current database technology.

2. To insure the continued availability of any data committed to the database. It should be possible to back-out of database technology altogether or to convert the database to other database forms and structures at reasonable costs and without loss of information content or reduction of "quality."

3. To know and minimize the costs of rewriting application programs or retraining personnel.

## 1.5. The general concept

Two major approaches aid in achieving these goals: one is technical; the other, administrative.

## 1.5.1. Data independence

“Data Independence” names a technical approach to preserving data and programs over an extended period of time. The ANSI/X3/SPARC DBMS Study Group in their final report [1] describes data independence as “insulat[ing] a user from adverse effects of the evolution of the database environment.” The report asserts, “Change is inevitable. Data independence is not the capability to avoid change; it is the capability to reduce the trauma of change.” Stating its value directly, the Study Group noted that, “...data independence ensures that applications can continue to run, ... if the stored data is reorganized ...”

The Study Group suggested a framework which allows data independence through careful structuring of the components. This structure protects the data over the inevitable evolutionary changes to the database environment. But, as Manola [12] notes, “[T]he framework itself does not solve the problem of providing data independence, it only provides the potentail. Implementations will have to take advantage of this potential by providing the necessary schema description and mapping capabilities”.

Is it possible to implement the Study Group framework and obtain its potential data independence with existing technology? Can utility result from a partial framework? When will a complete implementation be possible? To use existing technology and to manage future change requires developing existing components so that they can be converted in the future.

## 1.5.2. Standards

The goals of standards are:

\- To increase the number of potential suppliers. This insures competition, reduces prices, and insures that the purchaser does not become "locked into" any one vendor.

\- To conduct efficient and informed procurement actions by establishing explicitly what is to be purchased, (thereby reducing negotiation before and after the purchase).

\- To facilitate the evaluation and selection of products.

\- To insure interchangeability of data, programs, and personnel skills within the organization.

Sibley [15] examines the validity of DBMS standards as a management tool and reviews the findings of a working panel on standards [3]. Sibley concludes that candidates for standards and economic advantage to standardizing on them exist. Sibley raises three questions that must be answered for any standards proposal:

— Why is the standard needed?

-- What ia available for standardization?

\- Which types of systems should be standardized? The last part of this paper will address these three questions. In particular, section 4 will address "why", "what", and "which".

## 2. The ANSI/X3/SPARC study group framework

## 2.1. History of ANSI/X3/SPARC study group

In autumn, 1972, the American National Standards Institute (ANSI) committee on Computers and Information Processing (X3) through its Standards Planning and Requirements Committee (SPARC) established a Study Group on Data Base Management Systems with a charter to investigate the potential for standards. The Study Group issued an interim report in 1975 and a final report [1] in July, 1977. After publication of the final report, the Study Group was dissolved. (Since then SPARC has established a new Data Base Systems Study Group which met for the first time in September, 1978.)

## 2.2. Overview

The Study Group identified the scope of the database management system as being, "records, fields, files, etc., and the descriptions for all of those, and all the indices, mapping techniques, access methods, file organizations and end user languages". They presented a framework consisting of three interlinked schemas to provide data independence. This approach isolates the physical description of the stored data (the Internal Schema) from the particular data structures that the application programmer uses (the External Schema) by providing a third (Conceptual) schema into which both the physical and application descriptions must be transformed and correlated. This Conceptual Schema provides the indirection necessary to isolate the physical description from the application viewpoints. Since the Conceptual Schema contains the definitive descriptions, both the Internal and External Schemas must contain descriptions only of objects described in (or mappable from) the Conceptual Schema. The Internal and External Schema need not contain all of the descriptions in the Conceptual Schema. Indeed, any External Schema would normally describe a specific application-oriented subportion.

The existence of multiple and concurrent data descriptions requires processes to match an object's description in each of the three schemas. These matching processes (or "mappings") also require stored representations to permit machine processing.

On the human side, three administrative “roles” within the enterprise the Enterprise, Application System, and Database Administrators, provide the system with the needed descriptions. mappings, and viewpoints. Each interface between a role and the framework needs a language to express the information which represents the descriptions and mappings and permits processing by the transforms.

The following sections discuss the major components of the framework in more detail. Fig. 1 is a condensed form of a larger, more detailed figure in the final report [1]. Hexagons are roles. Rectangles are processors. A bar associated with a circled number is an interface. Lines connecting components indicate the flow of data, control information, programs, and data descriptions. Dashed boxes indicate program preparation and execution subsystems.

## 2.3. Conceptual schema

The Conceptual Schema is a collection of objects representing the entities, properties and relationships of interest in the enterprise. Examples of these objects are "records, irreducible relations, nodes in a graph structure, etc." The Conceptual Schema provides the indirection essential for data independence. "The Conceptual Schema is described explicitly in machine readable form in some well defined and potential standardizable language." Managed by the "Enterprise Administrator" role, the Conceptual Schema has the following purposes:

![](/api/attachments/7R8X95J4/fulltext/images/8c081dcfcef97b66c54cf0d20d3b75c47d376a2f97cffc90dc07cc6f8d66caf4.jpg)  
Fig. 1. Partial schematic (taken from ref. [1]).

\- Provides a description of the information used by the enterprise.

\- Provides a stable platform to which the External and Internal Schemas are correlated.

-Permits Internal Schema modifications without modifying the External Schemas.

\- Permits External Schema modifications without modifying the Internal Schema.

\- Permits control over content and use of the database.

Note that it may describe data not yet in machine-readable form nor ever intended to be in machine-readable form.

## 2.4. Internal schema

The Internal Schema is oriented towards the most efficient use of the computing facility and contains the collected descriptions of the actual data which relates to the objects in the Conceptual Schema. Provided by the Database Administrator, it reflects current storage techniques and permits mappings between these and the Conceptual Schema. The Internal Schema will change to satisfy performance tuning, or "packaging" requirements.

## 2.5. External schema

Several External Schemas provided by the Application Administrator may exist, each containing descriptions of the entities, properties, and relationships of interest to a specific user group in the enterprise. Each External Schema may subset the objects in the Conceptual Schema, and may reflect a different data model view of the objects. Thus, the three major data models (hierarchical, network, and relational) may have different External Schemas mapping to the same Conceptual Schema. The several external viewpoints do not affect the manner in which the data are actually stored as described in the Internal Schema.

## 2.6. System control points

The Study Group proposed a “data dictionary/directory” as the heart of the framework and the “container” in which the various schemas and mappings are stored.

They concluded that the languages at the interfaces are the proper subject for standardization because of the difficulty in standardizing the manner in which components are to work.

## 3. Assigning CODASYL specifications to the framework

## 3.1. Overview

The final report of the NASI/SPARC Study Group was intended to provide a framework useful for considering standardization. However, the final report does not make any recommendations on specifications of the interface languages. The broad and general style of the report left many decisions for implementors and language development groups. Consequently, evaluation of the framework is difficult [10,12].

This section will show how some existing components fit into the overall framework, identify work to be done, and analyse potential benefits.

## 3.2. History of CODASYL DBMS specifications

The Conference on Data Systems Languages (CODASYL) is a voluntary body that first met in April, 1959 and has since, among other works, developed COBOL and guided its development. In 1965, the CODASYL COBOL Committee initiated a "List Processing" Task Group that later changed its name to the Data Base Task Group (DBTG). The DBTG issued a series of reports on a COBOL database facility in 1968, 1969, and 1971. As a result of this work, in 1971 the CODASYL Executive Committee established a Data Description Language Committee (DDLC) and assigned the responsibility of developing a COBOL Data Manipulation Language (DML) to the Programming Language Committee (PLC). The DDLC published a Journal of Development (JOD) in 1973 which contained a detailed specification of the

DDL [6]. Within PLC the Data Base Language Task Group developed a Subschema DDL and DML that appeared in the COBOL Journal of Development-1976. In parallel and utilizing the host language independent nature of the DDL, PLC's FORTRAN Data Base Language Task Group (now a committee) developed a FORTRAN Subschema DDL and DML that was published in January, 1977. Both the PLC (now the COBOL Committee) and the DDLC published coordinated Journals of Development in January, 1978.

## 3.3. Using the CODASYL DBMS specifications

In order to effect the immediate use of database technology, a feasible detailed language specification must be available now. Further, to meet the needs for standardization the specification must be generally available and have been subjected to broad review. Only one set of specifications meets these requirements: the CODASYL DBMS specifications.

What language is appropriate for the Conceptual Schema? The ANSI/SPARC Study Group did “not propose a particular formalism as exceptionally appropriate to express the conceptual view of the database.” Several writers have assessed the feasibility of using the CODASYL schema as the Conceptual Schema. Manola [12] uses the most recent DDL Journal of Development [7] as the basis for evaluation while, Klug and Tschritzis [10] used the earlier version [6]. Ref. [10] reports actual implementation experience in constructing a specific instance of a database environment using the Study Group framework. Manola provides an analysis of each of the CODASYL specifications and evaluates their potential for satisfying the framework’s requirements.

Manola describes the major change in the latest CODASYL DDL JOD as the removal (from the DDL) of numerous language facilities related to database tuning to, "a new language, called the Data Storage Description Language (DSDL)". The DSDL permits tuning without impacting the DDL schema or the applications programs.

The DSDL specification has been published as a draft document to solicit public review and comment. Manola notes, "it is significant that CODASYL has, by publishing official DDL specifications with various tuning facilities removed, adopted the principle of a

DSDL independent from the schema DDL, whatever the final form of the DSDL itself." Thus CODASYL now has a three schema framework (schema, sub-schema, and storage schema) paralleling the Study Group framework.

Manola notes the similarity in several instances of both three schema frameworks. Manola concludes, "the most obvious way of interpreting the two sets of proposals together would involve assuming a correspondence between the CODASYL schema and the conceptual schema, the CODASYL subschema and the external schema, and the CODASYL storage schema and the internal schema." Manola offers his opinion, "that the two three-schema frameworks match well enough for the CODASYL DSDL, schema DDL, and subschema DDL to be considered respectively as candidates for the internal, conceptual, and external levels". I agree with Manola's conclusions.

Klug and Tschritzis [10] considered each of the three major data models as candidates and found none totally satisfactory, but proposed “a general network data model consisting of record types connected by links”. However, the two reasons they cite for not using the CODASYL DDL have been corrected in the latest DDL Journal of Development [7]. These were: (a) the prohibition of the same record type being both “owner” and “member” and (b) the inclusion of language features in the DDL properly in the Internal Schema because of its “physical storage” orientation.

Fig. 2 reproduces Fig. 1 but substitutes the appropriate CODASYL DBMS specifications. Additionally, the triangle representing the "data dictionary" is replaced with a long "busbar" to provide compatibility with subsequent figures. Using the roles defined by the Study Group, the Enterprise Administrator would use the Data Description Language at interface 1. The Database Administrator would use the Data Storage Description Language at interface 13. The Application System Administrator would use (as a specific instance of an External Schema) the COBOL subschema Data Description Language at interface 4. The Application Programmer would use COBOL's Data Manipulation Functions at interface 7 and communicate with the External Schema through interface 6. Note that this, too, represents one specific instance of using the External Schema and one might foresee a relational External Schema which would require a relational data manipulation function set and communications at interfaces 7 and 6, respectively.

![](/api/attachments/7R8X95J4/fulltext/images/4a0827c6e2df6c6ee68748f4d8de520dc9b7979abb98af28ce90cd2157f90132.jpg)  
Fig. 2. Applying CODASYL products to the study group framework.

The framework considers several other roles and interfaces which have not yet been discussed. Three omissions are particularly important: first, a stable and comprehensive definition of the Data Dictionary; second, the query capability or the Inquiry Processor Subsystem; and third, a means to use stored data which pre-existed the DBMS environment.

## 3.4. Data dictionary/directory

Data Dictionaries/Directories, of course, preceded this framework [11,13] but the framework formalizes its role. The Study Group [1] notes that the data dictionary “may also include usage statistics of various database objects and object types; access and security declarations; control structures for restart, recovery, accounting and auditing; descriptions of users; and textual statements relative to the preceding items.”

The Data Dictionary Systems Working Party (DDSWP) of the British Computer Society [2] provides a definition of a Data Dictionary: "a tool for recording and processing information about the structure and usage of data. Usually it will be a computerized system. ... the Data Processing department's own database." The DDSWP report proposes a "conceptual model" which describes all the data held by the enterprise, not just data held in the database, and to all sources of the data." Thus, "a further interface must be identified through which such a model can be entered and viewed". It proposes, "that the ANSI conceptual schema be divided into two parts, the underlying conceptual records (or the conceptual schema) and the derived conceptual records (or derived schema). The derived view is analogous to (say) a CODASYL schema, and the external view is then analogous to the subschema." This recommendation supports the proposed assignment of CODASYL specifications to the framework. It offers the additional notion that the Conceptual Schema should contain all the enterprise data with the machine-readable data as only a part of the entire enterprise model. However, no real need exists to differentiate the derived schema from the Conceptual Schema except to note within the Conceptual Schema description whether the data is available in machine-readable form or not. The Enterprise Administrator can manage this aspect of the database descriptions along with its other functions.

## 3.5. The query interface

Though every existing implementation of CODASYL of CODASYL-like DBMS provides an online, interactive query capacitability, no specification for one has been provided by CODASYL. [1] states, "The inquiry specifier is concerned with external object selection and expects a relatively small volume of output." Fig. 3 presents a portion of the framework taken from fig. 2 and indicates the additional structure necessary to support the Inquiry Processor Subsystem. (The reader may wish to compare this with Figure 2 of [1].)

![](/api/attachments/7R8X95J4/fulltext/images/f46cddb05021ed2e3f1cee32a4af47e17635e5d67ff8a249b57ab21654825efd.jpg)  
Fig. 3. The inquiry processor subsystem.

The Inquiry capability may be realized in several ways:

1. Through specification of a query language using the network model. If this is made freely available to any implementor, it will permit all vendors equal opportunity to respond to procurement requests. The time to develop the language slows the availability of this part by two to three years behind that of other CODASYL specifications. The query language could use existing External Schema specifications and mappings. Users of existing query capabilities will need to convert to a new product but since queries generally have a short life expectancy, this will entail primarily educational costs. Implementor acceptance of this approach will improve if the specification is premised on existing standards and is intended to become a standard itself.

2. By vendors providing an External Schema and mappings from their existing products within the overall framework. The data independence of the three schema framework would preserve their product's utility. The need for a new External Schema will vary as the product data model varies from the network model and the vendor ability to provide a consistent and compatible interface 6, Fig. 2.

3. By developing specifications for different External Schema and supporting Data Manipulation Facilities. For example, a relational query capability would require such an approach and present interest in this data model might justify this work.

The first approach appears the most attractive for any large organization.

## 3.6. Translation of databases

If one accepts the importance of data and the investment it represents, then an obvious need exists to provide a "bridge" from existing databases to a new database environment. [1] does not address database translation and only indirectly addresses the issue of loading data into the system.

However, the framework does permit an “entry point” for translated input. Fig. 4 presents a portion of the framework and indicates the additional structure necessary to support the Database Translation Subsystem. The Database Translator role might be incorporated into the Database Administrator function, but it is treated separately here for clarity of presentation. There may be a specific database translation process for each new source database.

How will the different models be reflected in the approach? In a real sense, the translations will always be from "internal schema to internal schema" even if the source database does not contain such a viewpoint. Major problems, like the existence of "phantom pointers", implicit data structures, special purpose code/encode functions, etc. will require translations at a quite low level with a consequent dependence on the Database Translator role for the intelligence necessary to produce verifiably correct translations.

![](/api/attachments/7R8X95J4/fulltext/images/3d2725ce07a38eaed988c79ac06850f261187b82191dc0ea293aa074011f4f59.jpg)  
Fig. 4. The database translator subsystem.

The CODASYL Data Storage Description Language provides a language for describing an Internal Schema which will be the target for any translation process. The DSDL may also provide the basis for describing the source database but it was not designed with translation in mind. Many of the functions necessary to reflect changes in the Internal Schema descriptions (such as meeting database tuning requirements) would also serve the translation function. However, the translation function will require additional functions and administrative constraints.

A report [4] of the findings of a working panel on conversion technology discribed the conversion state-of-the-art, its impact on databases, and actions one can take to ameliorate future conversions. A panel of experts noted the successes of special purpose conversions and was generally optimistic about the feasibility of generalized conversion techniques being available in the next five to ten years. They pointed to the possibility of special DBMS machines and “backend” data management minicomputers improving the data independence of existing database systems, to the important role standards can play, and to the contributions possible in designing software database system architectures for maximum data independence. They suggested guidelines for following (or avoiding) programming particles that impact data independence and also address the issue of application program conversion.

The report suggests: “[a] standard that is more likely to be accepted is one that affects only the way of interfacing to a DBMS. In particular, from a conversion standpoint, a standard interchange data from (SIDF) will be most useful. A SIDF is a format not unlike a load format for DBMS. Any advanced DBMS has a load utility that requires sequential data stream in a prespecified format. If a standard for this format can be agreed upon, ... then the need for reformatting ... is eliminated”.

Consider figure 4. The logical point for loading the database is through interface T21 (and interface 21 on figure 1). Here the data described by the DSDL is mapped into the internal storage form. A "load mapping" will transform the load form into the more complex internal storage form within the Internal Storage/DSDL transformer. In a translation process, the Database Translator will describe the source database in DSDL and provide a mapping that will transform the source database into the load format.

Interface T13 provides for a translation language to record the data description of the source database. The Database Translator Processor uses this input and the stored Internal Storage Descriptions to transform the source database into a load stream. The resultant data stream is loaded into the database through interface T21. The load format becomes a data interchange format amenable to standardization. And in this proposal, the DSDL would become the language for describing the standard data interchange format.

Note that neither the framework nor this proposal dictates the form of the internal storage and it can be a backend minicomputer as easily as a software structure. The indirection provided by the Conceptual Schema also insulates the External Schemas from changes to a hardware Internal Schema.

## 4. Standards

## 4.1. Overview

Earlier, standards were identified as a form of administrative control to buttress the absence of a technical solution. This section justifies the development of standards to provide immediate access to database technology while controlling future costs. Other benefits may accrue from using standards but they are not considered here. Nor are other supportive standards needed in a database environment.

The arguments for database standards include the fact that they:

\- Permit a stable base for developing other members of the data base family of standards.

\- Reduce the proliferation of slightly different products and replace de facto or vendor standards.

\- Reduce the number of different products from which conversions must be made.

-- Insure improvements are spread over a wide base with a reduction in unit developmental cost and faster payback.

\- Enable all vendors to provide the product.

\- Provide widest possible review of specifications.

\- Provide a known base for development and evaluation of improvements.

\- Facilitate statement of product for procurement.

\- Eliminate need to purchase each member product of the family of standards from the same vendor.

\- Facilitate evaluation and selection of products offered for purchase.

\- Permit interchange of data and programs within the overall organization.

\- Give users, through standards bodies, control over specification changes.

As noted earlier, [15] suggested three questions. We shall answer these next.

## 4.2. Which types?

I have already identified several components needed to provide a useful database environment. These include:

1. Description Language for the Conceptual Schema.

2. Description Language(s) for the External Schemas.

3. Description Language for the Internal Schema.

4 Data Dictionary/Directory System language(s).

5. Inquiry subsystem language.

6. Data Interchange Format.

7. Data Manipulation Language(s) for the application programs.

Of course, these are interrelated, which requires compatibility among them and suggests the possibility of common support functions for the "family" of related standards.

Standards provide a fixed foundation for future DBMS development. Once the family of standards are in place, further development can continue. Conversely, the selection of the three schema approach gives assurance that the standards themselves can evolve in an orderly fashion since changes to the standard for the one schema will have reduced impact:

## 4.3. What is available and why use it?

The following list names the various specification, reviews each assignment in the framework, states the standards action recommended, and gives reasons supporting the recommendations:

1. CODASYL Data Description Language. Used to describe the Conceptual Schema. A single standard reflecting the latest JOD should be immediately implemented. The DDL should be the first standard developed since the DD/D, DSDL, Subschema DDL, and COBOL DML are dependent on it. As the single standard, the DDL will gain the greatest possible usage and greatest acceptance by implementors. This insures a wide base for future developmental efforts, simplifies the conversion if an improved Conceptual Schema language appears, provides a stable base for future development, and will facilitate evaluation of future improvements. It may also contribute to directing research towards such important attributes of all database systems such as consistency, security, auditability, etc.

2. CODASYL COBOL DML and Subschema DDL. Used as the Application Programmer interface and External Schema. A single standard reflecting the latest JOD should be immediately implemented. Availability of the DML as soon as possible will permit applications with foreseeable data independence. Availability of the External Schema and implementation experience with it will permit development of DML's for other host languages. The Inquiry Subsystem will also be dependent on the External Schema. Note that other data models are not foreclosed by this action.

3. CODASYL DSDL. Used as the language for the Internal Schema. Standardization should proceed as soon as possible. A standard DSDL will complete the three schema concept and permit implementation experience. Like the DDL, improvements can be made to the DSDL with the advantage of a stable base for evaluation and conversion. The Database Translator subsystem is dependent on this standard. The DSDL, Database Translator subsystem, and the Standard Interchange Format have interrelated needs.

4. Data Dictionary/Directory. Used as the container of the enterprise data descriptions, mappings, etc. Need not be a standard but all DD/D should provide the standard DDL for interface 1 of the framework. User should be encouraged to use DD/D. Implementor experience will affect future considerations for standardization.

5. Inquiry subsystem. Specification needs to be developed. Need for standardization will depend on the cost, scope, and complexity of user requirements.

6. Database Translator subsystem. Specification needs to be developed. Provision of Standard interchange format and standard Data Storage Language may permit different forms of the translator.

7. Data interchange format. Specification needs to be developed. Standardization should precede the Translator and parallel the Data Storage Description Language.

## 4.4. Timeframe

How soon can the reader anticipate the availability of the proposed components? At the present time, ANSI Technical Committees are considering a Data Description Language and a COBOL Data Manipulation Language based on the CODASYL specifications. Each has a completion date of the middle of 1981. I am quite confident that this schedule will be meet. However, while CODASYL continues work on the DSDL, no committee of ANSI is developing the DSDL, a query capacitability, or the standard data interchange format. The CODASYL data translation work is proceeding slowly.

Neither group is developing specifications for a data dictionary but work continues in the British Computer Society's Data Dictionary Working Party.

## 5. Conclusion

How feasible is such a proposal? There have been an increasing number of papers dealing with the construction of a framework or architecture in which the various data models coexist [5,8]. Some work towards implementing a three schema database environment has been reported [10,14]. This trend evinces a desire to make a flexible database environment that serves the largest number of users. The ideas in this paper further this trend by helping to protect the investment in the existing data and the cost to install the database system.

The proposed approach would permit managers early use of database technology while providing control over future costs. The approach provides sufficient flexibility to support changes to the framework components, the standards supporting the framework, and the technology used to implement the various framework components. The data independence potential in the Study Group framework permits changes to any one of the schemas, implementation of several different external data models, incorporation of technological improvements.

The proposed approach permits immediate efforts in standards to begin with the consequent assurance to implementors and users that investments are protected. By participating in the standards considerations, users can have some control over future costs while assuring themselves of immediate benefits. The standard specifications can accept changes and evolve along with technical improvements.

The development of standards can help the research community and need not be "exclusionary." With the establishment of a "research base," researchers can concentrate on specific database issues. Research efforts can concentrate on needed facilities common to any database system. The family of standards will provide an effective common base for comparing alternative developments and permit rational evaluation and selection of them.

## Acknowledgement

The author gratefully acknowledges the comments of many colleagues within the National Bureau of Standards, the Informal Database Management System workshop, the Federal Information Processing Standards Task Group on DBMS Standards and, in particular, Frank Manola.

## References

[1] The ANSI/X3/SPARC DBMS Framework, Report of the Study Group on Data Base Management Systems, Tsichritzis, Dennis and Klug, Anthony, editors; AFIPS Press, 210 Summit Avenue, Montvale, New Jersey 07645, 1977.

[2] Bristish Computer Society Data Dictionary Systems Working Party Report. Joint publication in SIGMOD Record (December, 1977 Vol. 9, No. 4) and SIGBDP Data Base (Fall, 1977 Vol. 9, No. 2).

[3] J.L. Berg, editor, Data Base Directions: The Next Steps, National Bureau of Standards Special Publication No. 451 (September 1976).

[4] J.L. Berg, editor, Data Base Directions--the conversion

problem, to be published by the National Bureau of Standards.

[5] C.J. Date, An Architecture for High-level Language Data Base Extensions, Proceedings of the SIGMOD Conference, 1976.

[6] Data Description Language Committee Journal of Development. 1973, National Bureau of Standards Handbook 113.

[7] Data Description Language Committee Journal of Development, 1978. Available from the Material Data Management Centre, Canadian Government.

[8] M.H. Kay, An Assessment of the CODASYL DDL for use with a relational subschema, Data Base Description, North-Holland, 1975.

[9] L. Kerschberg, A. Klug, and D. Tsichritzis, A Taxonomy of Data Models. University of Toronto Technical Report CSRG-70, (May 1976)

[10] A. Klug and D. Tsichritzis, Multiple View Support within the ANSI/SPARC Framework. Proceedings of the 3rd Very Large Data Base Conference (October, 1977).

[11] Belkis Leong-Hong and B. Marron, Technical Profile of Seven Data Element Disctionary/Directory Systems, National Bureau of Standards Special Publication 500-3 (February 1977).

[12] F. Manola, An Evaluation of the New CODASYL and ANSI/SPARC Database Proposals, Infotech State of the Art Report: Data Base Technology, 1978.

[13] Survey of Eleven Government-Developed Data Element Dictionary/Director Systems, National Bureau of Standards Special Publication 500-16, 1977.

[14] G.M. Nijssen, EDMS Version 1.0 DDL Reference Manual, October, 1976.

[15] E.H. Sibley, Standardization and Database Systems. Proceedings of the 3rd Very Large Data Base Conference (October, 1977).

[16] K.J. Thurber and P.C. Patton, Data Structures and Computer Architecture, Lexington Books, 1976.
