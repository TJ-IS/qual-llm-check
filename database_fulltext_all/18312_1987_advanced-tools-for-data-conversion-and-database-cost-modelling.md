---
otero_id: 18312
otero_key: "97EUAGMX"
title: "Advanced tools for data conversion and database cost modelling"
authors: "Kalervo Järvelin; Timo Niemi"
year: "1987"
journal: "Information & Management"
doi: "10.1016/0378-7206(87)90026-7"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Advanced Tools for Data Conversion and Database Cost Modelling

Kalervo Järvelin and Timo Niemi
Dept. of Library and Information Science, Univ. of Tampere,
P.O. Box 607, SF-33101 Tampere, Finland

We consider two topics important to the database administrator: data conversion and database cost modelling. Suitable tools for these topics have been missing or their capabilities are insufficient in many practical situations today. We discuss approaches, principles, concepts and techniques, that can be used to manage these complex issues and pay special attention to factors that can be used to improve software which, in turn, provides the database administrator with a convenient and flexible interface.

Keywords: Cost modelling, Data conversion, Data reformatting, Data restructuring, Database software, File design, File structures, Query processing.

![](/api/attachments/97EUAGMX/fulltext/images/13aee7632ed9edc7069430e120684ecfdd5465637d157c8fe3386c4db4051409.jpg)

Kalervo Järvelin is currently an acting associate professor at the Dept. of Library and Information Science at the University of Tampere and teaches information retrieval. He holds a licentiate's degree in (1985) in computer science and a Ph.D. (1987) in library and information science, both from the University of Tampere. His current research interests cover logic programming and AI applications in information retrieval.

![](/api/attachments/97EUAGMX/fulltext/images/1bd7037b87b46d3debc7fa1cb8ad7a6a1dd80ce0e61257b1f05a27727f6e17e4.jpg)

Timo Niemi is an assistant professor of computer science in the University of Tampere. He received his Ph.D. from the University of Tampere. His research interests are data models, database software specification, data conversion, query languages and data administration. Recent publications have appeared in Information Systems, International Journal of Computer and Information Sciences, and BIT.

North-Holland
Information & Management 13 (1987) 11–24

## 1. Introduction

Modern database management systems (DBMSS) are complex and dynamic. Changes in their environment and in computer technology require that the database administrator (DBA) continuously monitors the environment and the operation of the DBMS and surveys relevant technological developments. When necessary, the content, structure, implementation and the user interfaces of the database must be modified. Such changes pose many difficult problems to the DBA. We consider two: data conversion and database cost modelling, both of which have proven extremely difficult. Existing DBMSS do not support, or their facilities are insufficient in their support of the DBA's job with respect to these. It is therefore highly desirable to provide the DBA with convenient and flexible tools for managing these complex issues.

Due to the dynamic nature of research and development in the computer industry, new hardware and software systems are continuously being added. In the utilization of these new systems, we often must transfer the stored data and existing application programs from one computer system to another. If the systems are incompatible, the existing programs cannot be run and the existing files manipulated without conversion.

Depending on the degree of incompatibility, costs of conversion can be a major factor in transferring to new hardware/software [20]. Furthermore, large and complex conversions can take years [9]. Therefore it is important to develop tools by which application programs and stored data can be converted. Su et al. have introduced a detailed model of how data conversion is associated with application program conversion [61]. Because the content of databases often represents a higher financial investment than the computer system, it is most essential that data conversion can be performed reliably.

Data conversion is a process which transforms data in a given hardware/software (hw/sw) environment into a representation that can be manipulated in the same or another hw/sw environment. The data to be converted are called source data and the converted data is target data.

There are two essential parts: data restructuring and data reformatting (see e.g. [22]). In data restructuring, only structural relationships among logical (user) data are transformed, whereas in data reformatting, changes in the formats of data occur.

By database cost modelling we mean the estimation of the costs – in terms of page accesses or seconds – occurring when transactions are executed $[70,72]$ . Synonymous terms are: database cost estimation $[49]$ , performance analysis $[63]$ , access cost analysis $[63,68]$ , and cost evaluation $[68]$ . It is based on cost equations $[68]$ (cost functions, cost formulae) which attempt to model relevant characteristics of the behavior of files and databases from a cost point-of-view. It is valuable during the initial phase of the database life cycle when the overall structure and detailed file organizations are designed, and during database reorganization when (due to efficiency problems or database conversion) the overall structure and/or file organizations must be modified. Database cost modelling, as well as data conversion, is the responsibility of the DBA.

In a modern database environment, the DBA has multiple file organization types and corresponding access methods available. The data can be divided among files in various ways. When choosing among the alternatives the DBA must recognize how each particular transaction type can be executed in each alternative. The DBA has to master a large set of alternatives and many details about the file organization types, access methods, and hardware properties. In addition, in all but the simplest cases, many calculations are required to model the costs; the number of transaction types considered must be kept small and often modified into simpler equivalents, though this reduces the reliability of the design. Thus the burden must be relieved by suitable tools.

The tools considered in this paper are based on a common principle: describing the underlying tasks formally, precisely and thoroughly in order to reduce the DBA's efforts in using the tools to the minimum. The details of our formal methods have been presented in earlier publications [29,30,32,40,42,43]. In this paper we focus on the approaches, principles, concepts and techniques behind our formal treatment and their practical consequences.

## 2. Database Conversion Tools

There are currently few software tools for data conversion. This is one of the key reasons for conversion projects being expensive and time consuming; e.g. [23], in which many conversion case studies are analyzed. Here, we consider factors which cause conversion problems and attention is paid to features which should be included in advanced tools to support data conversion.

## 2.1 Data Conversion with Data Restructuring

In data restructuring, the logical data relationships change, though the environment remains unchanged. In practice, this kind of conversion arises when the requirements change. Because the software environment in this case does not change, the underlying data model of the DBMS satisfies also the new requirements.

Today's DBMS provide DBAS with options for physical implementation of a database as described in some DDL (Data Description Language). We can describe the change of a physical implementation option as: PHYSICAL DATABASE → UNLOAD → DATABASE IN LOADABLE FORM → RELOAD → PHYSICAL DATABASE. In the reload phase, the new option is stated; but in spite of this, the DBMS's usually do not contain any tools for restructuring. Sometimes the changed user view is drastic; e.g. in a hierarchical database, it is possible that relationships of records must be inverted.

The DBMS's also contain system specific data. Because data restructuring is only concerned with user data, it is desirable that the data restructuring process is performed in a form containing as little system specific data as possible. The unload process removes the internal structures of a particular system. After this, the data are a sequential data stream. In this mode, structural relationships are easy to restructure. After restructuring, the database is reloaded using the load utility of the DBMS. Then the transformation of a source into a target database manipulateable with the same DBMS consists of the following steps: SOURCE DATA → UNLOAD → SOURCE DATA IN LOADABLE FORM → RESTRUCTURING → TARGET DATA IN LOADABLE FORM → LOAD → TARGET DATA.

Although DBMS vendors do not provide data restructuring facilities, many have initiated projects to solve the restructuring problem; university prototypes have also been developed. Usually the data restructuring languages are non-procedural and available for a particular data model.

Honeywell has developed a prototype for restructuring sequential files $[7]$ . Non-procedural languages for restructuring network data structures have been developed in $[12,62,64]$ . CONVERT of IBM $[35,56,57]$ , UMTDL (University of Michigan Translation Definition Language) $[62]$ , CDTL (Common Data Translation Language) of SDC $[55]$ and ADAPT of Bell Laboratories $[6]$ are languages for restructuring hierarchical databases. Shneiderman and Thomas have developed a set of useful restructuring operations for the relational data model $[54]$ ; they propose that implementers should incorporate these functions in an automatic system conversion facility. It is worth noting that many of the proposed restructuring languages and functions have to be implemented.

Usually the existing languages provide a set of high-level restructuring operations. By nesting these the user describes the necessary restructuring. From the viewpoint of a user, this approach has the disadvantage that the descriptions are troublesome: the description and design of a restructuring operation resembles the creation of an algorithm, even though the restructuring languages themselves are non-procedural. In complex restructuring, a user must define several intermediate files.

From the viewpoint of the DBA a restructuring facility should be provided for each DBMS, and the software should be easy to use. In the structural sense the minimal information needed for data restructuring is the source database and the description of the target schema [40]. From this, it is possible to build up for the DBA (or the restructuring user [37]) restructuring software that has a straightforward interface. This is because the restructuring user does not need to express explicitly any restructuring operations, and thus the restructuring software has the burden of finding and performing them.

In [40] we defined a general restructuring process for hierarchical databases. In our approach, the software analyzes the restructuring case and performs the needed operations on the basis of this. The functions deal with the restructuring problem of logical data structures at three essential abstraction levels as identified by Navathe & Fry [38]: at schema, instance, and value levels. At the schema level, the changes in the description of logical data structures are taken into account. These induce changes in the instance structure to make them conform to the modified schema. The change of the structure of the instances reduces into operations which treat data item values; e.g. by regrouping data item values, or by eliminating or duplicating some data item values.

Our restructuring system is able to restructure many different cases. It is able to construct any hierarchical target database that is derivable from the hierarchical source. In practice, a DBA must also integrate many source files or databases into one. Therefore we have specified, using attribute grammars, a software $[43]$ for restructuring many flat source files into one and restructuring of many hierarchical source databases into one.

## 2.2 Data Conversion with Data Reformatting

In this type of data conversion, the environment changes but the logical data structure remains unchanged. In practice, there are several different situations needing this. The substitution of a new version of a DBMS for an older one is a situation where the environment changes slightly. We have a more difficult conversion problem when the environment except for the DBMS changes (e.g. with the replacement of the computer system). For example, changing the TOTAL DBMS from an IBM to a CDC-environment represents this. The most complex case arises when, in addition to the replacement of a computer, the DBMS changes, even when it is based on the same data model (for example, IMS and SYSTEM 2000, both based on the hierarchical model). The common feature of these cases is that, from the viewpoint of users, the logical data structure remains unchanged.

The troubles are due to the lack of standardization and explicit description of the stored data. In spite of progress in standardization of the programming languages, the implementors of DBMS have solved the problems of representation and access methods in different ways. Thus in a new environment, the recompiled application programs can perform correctly but not be able to process files/databases created in the old environment.

With DDL's of DBMS's, programs can be separated from the description of their data. However, data are still dependent on the system which accesses them. Any advanced DBMS should also contain an explicit description of the storage structure. The ANSI/X3/SPARC proposal [2] provides, in order to achieve logical and physical data independence, three separate description levels associated through explicit mappings. In the internal schema one specifies the storing principles of data in detail. Likewise, the DIAM (Data Independent Access Method) model developed by Senko et al. [51] makes a clear distinction between logical data structures and their encodings. Because the existing DBMS's do not contain an explicit description of the storage principles of data, several languages (e.g. [8,58,60]) for describing the stored data have been developed.

One of the ideas of our experimental DBMS [33] is to provide clearly separated levels of data description and the mappings between them. At the lowest data description level, we specify the principles of storing data; e.g. for data items we specify e.g. the character code, the pad character to fill any unused space, justification (left or right) with respect to the allocated space. In other words, we describe the storage transformation which is stable in this environment. In [42] we defined exact encoding functions for flat files and hierarchical databases on the basis of this information. With encoding functions, we build up bit string representations which depend on the environment. Data reformatting changes the data encoding, resulting in changes in the parameters of these functions. Any advanced DBMS should contain a low level description of data and the mappings to this level, because we can then insulate changes in the hw/sw environment to one level.

If one DBMS is changed to another having the same data model but a different implementation, the conversion would be facilitated if the DBMS's had a common input format. From the viewpoint of data conversion, one of the most important tasks is to standardize the input formats for DBMS's based on the same data model (hierarchical, network, relational, etc.) and to obtain the adherence of manufacturers to this standard. This format would serve for interchange between the DBMS's.

## 2.3 Data Conversion with Data Restructuring and Data Reformatting

In this type, both logical data structures and the environment change. It is the most troublesome case occurring in practice. They arise when the computer system is replaced and a new DBMS is installed.

Sometimes this kind of conversion occurs when two or more companies are merged and need to integrate their data processing systems. This, in turn, often requires data conversion between incompatible systems. Furthermore, in distributed database systems using incompatible computers at different nodes, we must both restructure data between different data models and reformat data in transferring data from one node to another.

Here the data restructuring problem is more complex. This is because source databases or files and target databases or files are based on different data models. In database literature, the equivalence of schemas based on different data models has been studied to determine whether or not they represent the same universe of discourse (e.g. [10]). However, little attention had been paid to restructuring data when transforming from one data model into another. Sometimes this is impossible, because certain structural relationships must exist among source data in order to construct the target. Also, the vendors of the existing DBMS's do not usually provide any tools which are able to transform data between data models. However, these kind of tools are very useful when installing a new DBMS.

We have specified software which can restructure data based on flat file and hierarchical data models [43]. This software can restructure the following cases:

\- One or more flat files into one hierarchical database;

\- One or more hierarchical databases into one flat file.

In practice, the first case occurs when acquiring a hierarchical DBMS for a non-DBMS environment (flat files). In this case, we often integrate many flat files into a hierarchical database. Our specification also checks that all necessary structural relationships among source data exist so that the target data structure can be constructed.

A DBA does not need to express any restructuring operations, because the software analyzes the restructuring case and performs the necessary operations on this basis.

We can also consider our specification as a framework which crosses the boundaries between the three data models (hierarchical, network and relational) because in the structural sense, flat files and relations are analogous, and network databases can be split into families of hierarchies [35].

In addition to complex data restructuring, we have a data reformatting problem. General approaches have been attempted, but the solution has proven extremely difficult. Due to this, many theoretical approaches have not been implemented. It will take many years before commercial software is available with powerful data restructuring and data reformatting capabilities and which can be used in many different environments [9].

Prototypes of data converters are generally based on analogous architectures. Usually they consist of the sequence of three main modules: READER, RESTRUCTURER and WRITER (see e.g. [6,13,18,39,60]). The READER-module accesses the source data and transforms it into a form processable by the RESTRUCTURER, which performs the restructuring; the WRITER-module then stores it. Data reformatting is associated with the READER and WRITER modules whereas data restructuring is associated with the RESTRUCTURER module. This divides the complex data conversion problem into more manageable subproblems; furthermore, this architecture affords the possibility of running the modules in different computer environments, if required.

The main modules in question are often split into many sub-modules. Depending on the basic philosophy, the stored data descriptions and the number of intermediate forms of data vary considerably. For example, in $[57,60]$ the READER and the WRITER are distinct from the PHYSICAL READER and the PHYSICAL WRITER, which deal with low-level hardware details. One purpose of this is to allow the READER and WRITER to be used in different hw/sw environments with partial reprogramming only needed for the PHYSICAL READER and the PHYSICAL WRITER.

In this paper, we propose a general data conversion process consisting of the following sequential phases:

$$
\begin{array}{l}\text {PHYSICAL SOURCE DATA} \rightarrow \underline {{\text {UNLOAD}}} \rightarrow \text {SOURCE DATA} _ {\mathrm{UL}} \rightarrow\\\hline \text {Source system}\\\underline {{\text {DATA FORMATTING - 1}}} \rightarrow \text {SOURCE DATA} _ {\mathrm{R}} \rightarrow \underline {{\text {RESTRUCTURING}}} \rightarrow\\\text {(2)} \quad \text {(3)}\\\text {TARGET DATA} _ {\mathrm{R}} \rightarrow \underline {{\text {DATA FORMATTING - 2}}} \rightarrow\\\text {(4)}\\\text {TARGET DATA} _ {\mathrm{I}} \rightarrow \underline {{\text {LOAD}}} \rightarrow \text {PHYSICAL TARGET DATA}\\\hline \text {(5)}\\\text {Target system}\end{array}
$$

These are:

1. The source system, the utility of the source database or file system unloads the source data. Typically the output file (SOURCE DATA $_{UL}$ ) of the unload process is a sequential data stream in a prespecified format which reflects the basic units of the data model used in the source DBMS or file system. The PHYSICAL SOURCE DATA contains control information, such as pointers, overflow chains, delete flags, etc. whereas SOURCE DATA $_{UL}$ mainly contains user data.

2. The DATA REFORMATTING-1 phase changes the format of source data into the form (SOURCE $DATA_{R}$ ) processable by the DATA RESTRUCTURER. In principle $SOURCE_{UL}$ and SOURCE $DATA_{R}$ can reside in different hw/sw environments. This internal form of the restructuring process describes source data generally; i.e. the representation is not bound to any DBMS or file system.

3. The RESTRUCTURER phase changes structural relationships among logical (user) data. TARGET DATA $_{R}$ is in the internal form of the restructuring process.

4. The DATA FORMATTING-2 phase transforms data into the prespecified format of the load utility of the target database management or file system. Data restructuring is performed on the basis of data representation independent of any system; we need a process which produces input data for the specific systems.

5. The Target system uses the load utility of the target system. TARGET DATA $_{L}$ is a sequential data stream in a prespecified format. In the load phase, we construct a physical target database which contains a large amount of control information specific to the target file or database system.

In our model, the load and unload utilities are not included in the data conversion software; these tasks would make the conversion software larger and more complex and are usually available in the environment. The use of these utilities provides a clear and natural interface between the actual conversion software and the source and target environments. For example, in terms of the DIAM model of Senko et al. [51], the load and unload utilities operate at the physical device level (one of the abstraction levels of the DIAM), which places encoded data on the physical storage media. In our approach, the data conversion software deals with the problem at the data encoding level. In turn, this means that we can simplify the data conversion language because the storage mapping need not be included.

In general, data structures can be illustrated in terms of Bachman's diagrams, because they describe data structures independent of any system. Consider a hierarchical database whose schema and one instance (a hierarchical database) are described in Fig. 1. We use IMS (the IBM system) to illustrate this. A physical IMS database is described by a Data Base Description (DBD). A DBD consists of several statements. Explanation of these can be found in the standard literature (see e.g. [15,21,65]) and therefore we shall not describe them here. Let our sample database have the physical DBD of Fig. 2.

Here, DATA FORMATTING-2 builds a representation of the hierarchical database so that a physical database can be created with the IMS load utility: this representation is the input file for the IMS-HISAM load utility.

Consider the bit string representation of the input file (or source) from which the physical database is loaded; we use the notational convention $\mathtt{BS}(\mathtt{value}, i)$ for the encoded data item value or the bit string representation of value when i expresses the number of characters (bytes) allocated for storing it (as expressed in some FIELD statement).

The construction of the representation presupposes the following:

\- Database trees (database records in IMS terminology) are stored sequentially in an input file for the HISAM load utility.

\- In the input file, the records (segments in IMS terminology) are stored in preorder (one of the basic orderings to arrange and retrieve hierarchical data, see [1])

• Each segment must be supplied with a unique segment type code. In an IMS database, segment type codes can vary from 001 to 255. These segment type codes are represented as (zoned) decimal format in the input file for load utility [28]. The numbering of segment type codes is based on the order of segment types in a DBD so that the root segment type has the segment type code 001 and so on. In our sample database the segment types DEPT, PRODUCT, SELLER and PROCESS have the segment type codes 001, 002, 003 and 004, respectively. In our example we show only one database tree. The data stream of the input file for the HISAM load utility consists of the bit string shown in Fig. 3.

![](/api/attachments/97EUAGMX/fulltext/images/2d109aea05238580a0319f9117f586406c21d025be2c1ba6d7e89b6be6378b66.jpg)  
Fig. 1. Hierarchical sample database.

![](/api/attachments/97EUAGMX/fulltext/images/ce33150e4fecc3a79788d91cc2e315023145037568a3185dd89bfa40b277a55c.jpg)  
Fig. 2. The physical IMS database description.

In [42] we show exact functions which encode data item values into bit strings. These functions use information that remains stable for a given environment; e.g. the character code, the pad character, and the justification. By changing the parameters we produce bit string representations for different environments.

Fig. 3 represents the interface between the actual data conversion software and the IMS environment. This would be different, of course, if the restructured data would be transferred to another environment. All data, except for record type codes, are user data. A large amount of the control information specific to the DBMS is created in the loading phase. Next, we characterize briefly those tasks which are performed in the loading phase.

\- Two physical files are created: one is an indexed sequential file which contains the root segments and as many subordinate segments as can fit into the fixed length physical record chosen by a DBA; the other physical file contains those subordinate segments that do not fit.

![](/api/attachments/97EUAGMX/fulltext/images/50932e465e6f0745af3076d7c74d790809a022a2b22771447a70606a99411929.jpg)  
Fig. 3. Bit string representation for the HISAM load utility.

\- The storing policy of segments requires that no segment is split across physical records. This means that there may need to be padding at the end of a physical record.

\- In IMS a prefix area is created for each stored segment. It contains control information, such as record type code, deletion flag, pointers, etc.

## 3. Database Cost Modelling Tools

We now turn to tools that support the DBA in cost modelling. We consider two typical modelling situations: (a) of individual files with respect to search and maintenance transactions, and (b) of general (multifile) database queries. The former is relevant in the detailed design of file organizations and when considering their reorganization. Moreover, search models of individual files are a subproblem of query cost modelling, e.g. for physical database design and reorganization.

We consider cost modelling in the context of the relational data model $[19,66]$ , with file descriptions and storage parameters to represent the files and the hardware/software environment for cost modelling. Therefore we begin with an outline of the parameters.

## 3.1 File Description and Storage Parameters

Fig. 4 shows a sample relational database for marketing data. It has two relations, one for PRODUCTS and one for COMPANIES. The attribute names (or field names) together with some sample data in each of the files are tabulated, with each row in the tableaux representing one record.

Consider the PRODUCTS-file. The number of rows (five are shown) is the file cardinality. It is assumed to be 250000. The file has five attributes (columns) with attribute names PRODUCT-NO, TRADEMARK, TYPE (of the product), MANUF-NO (manufacturer identification), and QSALES (quantity of total sales). Each of the attributes represents some property of the products or some association of products to other entities. By examining the attribute values of PRODUCT-NO, one might state:

\- there are 250000 different values (the attribute selectivity)

<table><tr><td>PRODUCTS (</td><td>PRODUCT-NO</td><td>TRADEMARK</td><td>TYPE</td><td>MANUF-NO</td><td>QSALES)</td></tr><tr><td></td><td>1512</td><td>GILLETTE</td><td>19500</td><td>260011</td><td>502000</td></tr><tr><td></td><td>1586</td><td>GILLETTE</td><td>19190</td><td>260011</td><td>107000</td></tr><tr><td></td><td>376203</td><td>BRAUN</td><td>19190</td><td>7005</td><td>408000</td></tr><tr><td></td><td>95051</td><td>BLUE STRATOS</td><td>19500</td><td>530286</td><td>200000</td></tr><tr><td></td><td>556556</td><td>TABAC</td><td>19500</td><td>1050</td><td>900000</td></tr><tr><td></td><td>•</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>•</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>•</td><td></td><td></td><td></td><td></td></tr><tr><td>COMPANIES (</td><td>COMPANY-NO</td><td>C-NAME</td><td>HQ-LOC</td><td>TURNOVER</td><td>REVENUE</td></tr><tr><td></td><td>260011</td><td>GILLETTE UK</td><td>LONDON</td><td>10000000</td><td>800000</td></tr><tr><td></td><td>7005</td><td>BRAUN AG</td><td>FRANKFURT</td><td>5000000</td><td>500000</td></tr><tr><td></td><td>530286</td><td>SHULTON LTD</td><td>NEW YORK</td><td>8000000</td><td>200000</td></tr><tr><td></td><td>1050</td><td>MÄURER+WIRTZ</td><td>STOLBERG</td><td>7000000</td><td>1000000</td></tr><tr><td></td><td>•</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>•</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>•</td><td></td><td></td><td></td><td></td></tr></table>

Fig. 4. A sample relational database.

\- all values are integers,

\- the lowest value is 1000,

\- the highest value is 999999.

Similarly, TYPE has 17000 different values, all integers, ranging from 100 to 50000, while TRADEMARK has 200000 different character string values.

Further examination might reveal that the PRODUCT-NO of each row uniquely determines all other values in a row or that the TRADEMARK value in any of the rows uniquely determines the MANUF-NO value. These reflect the facts that a TRADEMARK is owned by only one manufacturer or that the product associated with one PRODUCT-NO is manufactured by only one manufacturer. In the terminology of the RDM, these are functional dependencies [66]; i.e. the values of PRODUCT-NO functionally determine all other values of a record.

The PRODUCTS-file could be organized as an indexed file with separate indices on PRODUCT-NO and TYPE, the former containing 250000 different key values and the latter some 17000. Analogous remarks can be made concerning the other file. Let us assume that it contains some 12000 records and is organized as a sequential file sorted on COMPANY-NO.

Cost modelling of database queries requires a systematic and precise file description. Informal descriptions require human interpretation during the modelling process and would lead to the loss of generality and simplicity. Such a file description must be derived on the basis of the data in the database and it must reflect essential characteristics from the cost modelling point-of-view. The features of the files considered above are relevant. Another requirement is the propagateability of the components of the file descriptions. Cost modelling of multioperation queries requires that the intermediate files can be described with the same formalism. Therefore the components of the description must be propagated through the operations. A natural means hereto is the n-tuple representation, used for many purposes in database research e.g. for relational database scheme design [5], for the description of hierarchical data structures [41], and for the formalization of the relational data model [44].

We now consider informally the components of the file description. The exact definitions can be found in [29-32]. It consists of six components:

\- the file name,

\- its cardinality,

\- the attribute description set,

\- the functional dependency set,

\- the organization description, and

\- the cost associated with the file.

By including these components into our file description mechanism, we have aimed at comprehensive treatment of the file and query cost modelling problem. This approach allows systematic and effective analysis of cost modelling situation.

In addition, the hardware/software environment of the database must be described. For this purpose, we have developed a storage parametersdescription; the components of this were selected on the basis of a number of cost modelling studies (e.g. [11,16,52,67,69,71]). The description contains information associated with blocking, buffer and sort characteristics (buffer space, merging), and disk characteristics (e.g. seek time, transfer rate). In total, it consists of fourteen parameters [30,32].

## 3.2 Cost Modelling of Individual Files

When considering file organization, the DBA has some characterization on the file use requirements. It may be rough or detailed, but in either case it consists of transaction types (e.g. search, modify), their parameters, their frequencies and distributions over time, and their response time requirements. The problem is to select a file organization among available alternatives so that requirements can be met as efficiently as possible.

Text books ([26,63,67]) and reports ([14,16,27,34,46,49,53]) typically provide detailed analyses and formulae on the behavior of each file organization type in their typical use. Often these are classified into GET FIRST (or GET UNIQUE) record, GET NEXT, GET SOME, and GET ALL search (or maintenance) cases ([63,67]). The DBA may have handbooks and even packages as aids to cost modelling of file organizations.

With these, the DBA proceeds to classify transactions into cases. Some transaction types may have to be modified or approximated if they cannot be modeled as such. Often this is quite straightforward as illustrated in Table 1. Although not difficult, the classification of such transactions is tedious and requires that the DBA recalls how different file organization types should be accessed.

The DBA should be aided in these classification tasks.

The need for classification tools becomes more apparent if one considers slightly more complex situations. Consider an indexed file with a predicate of type $(P(x) \wedge P(y)) \vee (P(z) \wedge P(v))$ ; e.g. (PRODUCT-NO < 112000 AND TRADEMARK = TABAC) OR (TYPE = 19500 AND MANUF-NO = 556556). Indices can be used for searching the records if there are at least two in the file: one either on x or y and the other either on z or v ([3,25]). In the file PRODUCTS, the indices on PRODUCT-NO and TYPE could be used. The solution requires knowledge of techniques for predicate analysis and detailed consideration of the particular set of indices.

Our cost modelling software specification is designed to analyze the costs of search, delete, modify and insert transactions in pipe files, in non-sorted, sorted and indexed sequential files, in indexed files and in direct files. It forms, in essence, a general, systematic and extensible approach to cost modelling of all non-hierarchical files. It incorporates the traditional cost formulae. However, its distinctive feature is that it automatically classifies any transaction into file access cases and thereby makes it as simple, straightforward and convenient as possible. For example, to evaluate the cost of a search, the DBA essentially has to give only the file name and search predicate (e.g. PRODUCTS: TRADEMARK = TABAC AND TYPE = 19500).

It then uses the file descriptions and storage parameters to recognize the relevant access strategy and to evaluate the search cost. Our system can analyze and manipulate general Boolean predicates. This has many important practical consequences in both cost modelling and the development of access methods and query optimizers. The DBA does not need to bother about the particular strategy. The limitations of a given DBMS with respect to the available access methods and their implementations can be taken into account.

Simple classification examples for search transactions in sorted sequential and indexed files

<table><tr><td>Predicate</td><td>Sorted Sequential File</td><td>Indexed File</td></tr><tr><td rowspan="2"> $K(x)$ </td><td>GET UNIQUE (via file scan) if  $x \neq S$ </td><td>GET UNIQUE (file scan) if  $x \notin I$ </td></tr><tr><td>GET UNIQUE (binary search) if  $x = S$ </td><td>GET UNIQUE (primary key index) if  $x \in I$ </td></tr><tr><td rowspan="2"> $P(x)$ </td><td>GET ALL, if  $x \neq S$ </td><td>GET ALL, if  $x \notin I$ </td></tr><tr><td>GET FIRST/GET NEXTS, if  $x = S$ </td><td>GET SOME (via index on  $x$ ) if  $x \in I$ </td></tr><tr><td rowspan="2"> $P(x) \land P(y)$ </td><td>GET ALL</td><td>GET ALL (file scan) if  $x \notin I \land y \notin I$ </td></tr><tr><td></td><td>GET SOME (via  $x$ ,  $y$ -indices) if  $x \in I \lor y \in I$ </td></tr><tr><td rowspan="2"> $P(x) \lor P(y)$ </td><td>GET ALL</td><td>GET ALL (file scan) if  $x \notin I \lor y \notin I$ </td></tr><tr><td></td><td>GET SOME (via  $x$ ,  $y$ -indices) if  $x \in I \land y \in I$ </td></tr><tr><td colspan="2">Legend:  $x, y$  attribute names</td><td> $s$  the sort attribute name in sorted sequential files</td></tr><tr><td colspan="2"> $K(x)$  unique record predicate on attribute  $x$ </td><td> $I$  the name set of indexed attributes</td></tr><tr><td colspan="2"> $P(x)$  any simple predicate on attribute  $x$ </td><td> $\lor$  disjunction (“OR”)</td></tr><tr><td colspan="2"> $\land$  conjunction (“AND”)</td><td></td></tr></table>

In principle, our method consists of the following steps. The file name and transaction are given. Then the system:

1. recognizes the file name and obtains its description,

2. recognizes the transaction type and validates it: - search, delete: the predicate must be meaningful

\- modify: the attributes to be modified must also belong to the file,

3. analyzes whether the supported access paths (i.e. sort order, indices, hash keys) can be used to access the target records; this requires analysis of both the file organization and the predicate of the transaction,

4. evaluates the most efficient access strategy, if there are alternatives,

5. reports the cost.

Our systems incorporates powerful techniques for the analysis of predicates. These are based on predicate factorization [25] and reduction techniques [31]. Consider the following predicate on the file COMPANIES:

(COMPANY-NO > 5000 AND COMPANY-NO < 10000 AND HQ-LOC = NEW YORK) OR (COMPANY-NO > 7000 AND COMPANY-NO < 20000 AND (HQ-LOC = BALTIMORE OR HQ-LOC = NEWARK))

By analyzing the predicate, one sees that all the target records are within the COMPANY-NO range from 5000 to 20000. Therefore, in principle, the COMPANIES file can be searched by accessing COMPANY-NO = 5000 by binary search and scanning from there until COMPANY-NO = 20000. In our cost modelling system this predicate is automatically modified (for search cost estimation) to the form COMPANY-NO > 5000 AND COMPANY-NO < 20000. This shows that complex predicates can be automatically analyzed and search strategies can be identified. It also shows that our method can find search strategies that cannot be utilized by most present DBMSS and therefore their limitations must be included into the applications of the method.

Due to its modular and rule-based structure, this is no problem. As a byproduct, this shows how the access methods of usual DBMss could be improved.

Consider another example on PRODUCTS-file, the predicate

PRODUCT-NO = 1512 AND TYPE = 19500.

The conventional approach to selecting the access strategy is the maximum use of indices (e.g. [3,16,27,63]); every possible component of the search predicate is evaluated via indices. In the sample case, this would mean using both of the indices on PRODUCT-NO and TYPE. However, in this particular case the predicate PRODUCT-NO = 1512 would yield one unique record identifier from the PRODUCT-NO index and the conjunction with TYPE = 19500 cannot effectively reduce the number of records accessed. In addition, usually the evaluation of TYPE = 19500 takes more time than can be saved by a reduction of one record access. Therefore the maximum use of indices sometimes leads to less than optimal access strategies. The cost model is able to recognize the optimal access path on the basis of its estimate. This, again, shows ways of improving file access; limitations of a particular DBMS can be taken into account.

We have defined all necessary mathematical functions required for the analysis of general Boolean predicates against the six file organization types. As a result, the DBA only needs to specify the transactions as they occur, without having to analyze or modify them to fit a special case. The DBA can use real transaction data (e.g. a set of past transactions) to evaluate file organization alternatives. This makes the cost modelling interface very convenient and straightforward.

## 3.3 Query Cost Modelling

The DBMS must be efficient in evaluating a range of queries generated by application programs and/or users. Therefore the file organizations must be designed from the viewpoint of multifile queries. Query cost modelling is an essential basis for the file design. Another area for query cost modelling tools is for cost estimation prior to query execution, when the user is charged for the query $[16,29,30]$ .

The difficulty lies in the requirement that, in addition to the behavior of individual files, the

DBA must master the query access strategy selection methods. The present query optimizers (e.g. [24,50,70]) are 'quick-and-dirty'; they use rough methods for quick selection of access strategies. The result is an access strategy, not a cost estimate. Much tedious calculation is required if the efficiency of the access strategy selections is assessed for several file organization alternatives.

Because query optimizers are used in the selection of access strategies during regular database use, they should also be used in access strategy selection for query cost modelling $[48]$ . We think that the optimizer output (access strategies) is a meaningful interface to cost modelling. The task of the model then is to evaluate the cost of particular access strategies in the database being designed. This has the following advantages:

1. Cost estimates are based on a real database environment. General models ([68,69]) are too abstract to give real estimates for particular systems.

2. Cost estimates are based on a true multifile approach. Breaking the cases down to individual file considerations ([16,63]) loses the interactions of the files during query execution.

3. The ‘quick-and-dirty’ results of an optimizer can be thoroughly analyzed without manual calculations.

Our software specification $[30-32]$ covers the seven most usual RA operations (divisions are excluded), with one to four implementation alternatives for each. In essence, these implementation alternatives (procedures) are analogous to $[59]$ . The model assumes queries as access strategy selections based on such implementation procedures and some auxiliary procedures (e.g. for sorting). The other approach ([4,11,50,70]) of constructing aggregate procedures for standard operation sequences (e.g. restrict, join, project) are equally well modelled.

The basic philosophy of our approach is the propagation of file descriptions through the query expression. We need mathematical functions that construct all six components of our file description for the intermediate and final results of the implementations of the RA operations. For each distinct implementation procedure, we have defined the procedure cost model that utilizes these functions to construct the file description. The architecture is illustrated in Fig. 5.

Some of the functions in a procedure cost model are common to all procedures for implementing the same operation – denoted by 'op-'. The function types op-card, op-a-descr and op-fd compute the cardinality, attribute description set, and FD-set components. Their argument types are shown besides the arrows. We have defined such functions for the RA in [29]. Some of the functions are common to analogous procedures for implementing distinct RA operations (e.g. merge-join, merge-intersection) and some strictly procedure-specific. These are denoted by 'proc-'. The functions of type proc-od construct the organization description for the result files and the functions of type proc-cost estimate the cost of the procedure [32].

![](/api/attachments/97EUAGMX/fulltext/images/17125c2676a30e0507d1f2cac6f3d4c7c497d15143dc1be89e79305bee3f5ee2.jpg)  
Fig. 5. The query cost model architecture.

The arguments for all these functions are obtained from three sources: the operand file descriptions, the storage parameters, and operation-related parameters. The latter contain (1) the principles of the operations and the procedures for their implementation embodied in the respective functions, (2) the parameters of the operations (o-param, i.e. restriction and join predicates and the names of the projected attributes), and (3) possible additional parameters of the procedures (p-param, e.g. sort-order specifications). The relationships among the functions and their arguments are shown by the labeled arrows, the labels representing the argument types. The FN-component of the result file description will always be $\Lambda$ (for a missing name), because the name of the result is irrelevant.

Consider the following query: "Give the TRADEMARKS owned by SHULTON LTD and the product TYPES sold under these." In RA the query

would be:

$$
\begin{array}{r l} \mathrm{T1} = & \text { RESTRICT } (\text { COMPANIES,C - NAME } = \text { SHULTON } \\ & \text { LTD }) \end{array}
$$

$$
\begin{array}{r l} \mathrm{T2} = & \text { JOIN } (\mathrm{T1}, \text { PRODUCTS }, \text { COMPANY - NO } = \\ & \text { MANUF - NO }) \end{array}
$$

$$
\mathrm{T3} = \text { PROJECT } (\mathrm{T2}, [ \text { TRADEMARK }, \text { TYPE } ]).
$$

The access strategy, given by the optimizer, could be:

1. Scan COMPANIES to find SHULTON LTD; pipeline the result,

2. sort PRODUCTS on MANUF-NO; pipeline the result,

3. merge-join the results from (1) and (2); pipeline the result,

4. perform the projection; pipeline the result.

The cost of this strategy is of the order 3000 sec (50 min) or about 137000 block transfers (2 K each). Both these estimates would be provided by the model. This query would be very inefficient. The DBA could now specify an index on MANUF-NO into the PRODUCTS file description (by 'create a B-tree index on MANUF-NO into PRODUCTS' – our tool could modify the organization description). By retrying optimization, the access strategy would possibly contain a join utilizing this new index on PRODUCTS and the cost model would indicate a cost reduction to some 3.5 sec.

Our cost model performs such cost computations automatically. Any RA query of any complexity can be analyzed in this way. For estimating the costs of individual file accesses, our file cost model is used. Its generality and flexibility is due to the fact that each procedure cost model constructs a full file description that conveys all the file-related parameters to the procedure cost model. If only the cost component were computed then, in a multioperation query, the parameters for estimating the cost of the subsequent operations would have to use an informal, implicit means that hampers the effort. The richness and explicit definition of the file descriptions make them flexible and extensible for many query-cost related problems (e.g. cardinality estimation [29] and file transfer cost estimation).

Because the result is a full file description, we can easily evaluate implementations of different relation schema $[44,66]$ alternatives of the database (e.g. with respect to normalization $[36]$ ). It is easy to derive file descriptions corresponding to the schemas in different degrees of normalization. In other words, if a relation is normalized, we obtain the corresponding file descriptions (containing cardinality estimates, attribute descriptions, functional dependencies, file organization and cost) by the cost model. If we wish to experiment the normalized files with varying organizations, we can modify the organization descriptions flexibly.

## 4. Conclusion

There are many different situations where the DBA requires data conversion and database cost modelling. In this paper we have considered several such situations. At this moment, few tools are available for their treatment. In addition, present tools are insufficient in most practical situations. In this paper, we recommend principles, approaches, and techniques that allow the construction of useful tools with a flexible and convenient interface from the viewpoint of the DBA. Special attention is paid to features which extend the tools' capabilities with respect to conventional approaches.

Data conversion cases have been divided into three categories: those requiring data restructuring, requiring data reformatting, and requiring both. In each, we consider practical situations. Special attention is paid to features which should be included in advanced data conversion software to support the DBA.

Two important database cost modelling cases were considered: file and query cost modelling. In both we emphasize raising the level of automation in the analysis of these cases. This was achieved by combining techniques used in file design, cardinality estimation, query optimization, and predicate analysis. Consequently, the DBA's interface to the cost model becomes convenient: by only describing the files, the hw/sw environment, and the transactions (queries), the costs of transactions can be assessed. The DBA can thus avoid tedious manual calculations and concentrate on database design.

Behind the approaches, concepts, methods and techniques presented in this paper are formal and precise specifications of the underlying tasks. As we see it, this is the only way to manage complex problems in database environments. Complex tasks are easily automated only by formalizing them. This often requires powerful and heavy mathematical techniques. However, when these are available, the DBA need not master their details anymore. He can concentrate productively on improving the usability and efficiency of the database, e.g. through conversion and file design, based on reliable cost estimates.

## References

[1] A.V. Aho, I.E. Hopcroft and J.D. Ullman: Data Structures and Algorithms, Addison-Wesley, 1983.

[2] ANSI/X3/SPARC (Standards Planning and Requirements Committee), Interim Report from Study Group on Database Management System, FDT (Bulletin of ACM SIGMOD), Vol. 7, No. 2, 1975.

[3] M.M. Astrahan and D.D. Chamberlin: Implementation of a Structured English Query Language. Comm. ACM, Vol. 18, No. 10, 1975, pp. 580–588.

[4] M.M. Astrahan et al.: System R: Relational Approach to Database Management. ACM TODS, Vol. 1, No. 2, 1976, pp. 97–137.

[5] G. Ausiello, C. Batini and M. Moscarini: On the equivalence among data base schemata. Proc. Int. Conf. on Data Bases, University of Aberdeen, UK, 1980, pp. 34–46.

[6] M.J. Bach, N.H. Coguen and M.M. Kaplan: The ADAPT system: A Generalized Approach Towards Data Conversion, in Proc. 5th International Conference on Very Large Data Bases, Rio de Janeiro, 1979, 183–193.

[7] D.E. Bakkom and T.A. Behymer: Implementation of Prototype Generalized File Translator, in Proc. ACM Sigmod, San Jose, 1975, 99–110.

[8] B.C.S. CODASYL DDLC Data Base Administration Working Group: Appendix: Draft Specifications of Data Storage Definition Language, Information Systems, vol. 3, No. 4, 1978.

[9] J.L. Berg (editor): Data Base Directions II: The Conversion Problem, Data Base, vol. 12&13, No. 4&1, 1981. (Appeared also in ACM Sigmod Record, vol. 12, No. 2, 1982).

[10] H. Biller: On the Equivalence of Data Base Schemas – A Semantic Approach to Data Translation, Information Systems, vol. 4, No. 1, 1979, pp. 35–47.

[11] M.W. Blasgen and K.P. Eswaran: Storage and Access in Relational Data Bases. IBM Systems Journal, Vol. 16, No. 4, 1977, pp. 363–377.

[12] R.H. Bonczek and A.B. Whinston: A Generalized Mapping Language for Network Data Structures, Information Systems, Vol. 2, 1977, 171–185.

[13] E.W. Briss and J.P. Fry: Generalized Software for Translating Data, in Proc. AFIPS National Computer Conference, 1976, pp. 889–897.

[14] A.F. Cardenas: Analysis and Performance of Inverted Database Structures. Comm. ACM, Vol. 18, No. 5, 1975, pp. 253–263.

[15] A.F. Cardenas: Data Base Management Systems, Allyn and Bacon, 1979.

[16] A.Y. Chan: Index Selection in a Self-Adaptive Relational

Data Base Management System. Report MIT/LCS/TR-166, Lab. for Computer Science, MIT, Cambridge, MA, Sept. 1976.

[17] S. Christodoulakis: Estimating Record Selectivities. Information Systems, Vol. 8, No. 2, 1983, pp. 105–115.

[18] CODASYL Stored Data Definition and Translation Task Group: Stored-Data description and Data Translation: A Model and Language, Information Systems, 3B, 1977, 95–148.

[19] E.F. Codd: A Relational Model for Large Shared Data Banks. Comm. ACM, Vol. 13, No. 6, 1970, pp. 377–387.

[20] Database Program Conversion Task Group of the Codasyl System Committee: Database Program Conversion: a Framework for Research, in Proc. 5th International Conference on Very Large Data Bases, Rio De Janeiro, 1979, p. 299–312.

[21] C.J. Date: An Introduction to Database Systems (3rd edition), Addison-Wesley, 1981.

[22] J.P. Fry and D.W. Jeris: Towards a Formulation and Definition of Data Reorganization, in Proc. ACM Sigmod Conf., Michigan, 1974, 83–100.

[23] L. Gallagher and S. Salazar: Report on Approaches to Database Translation, NBS Special Publication 500–115, 1984.

[24] P.A.V. Hall: Optimization of a Single Relational Expression in a Relational Data Base System. IBM Journal of Research and Development, Vol. 20, No. 3, 1976, pp. 244–257.

[25] P.A.V. Hall and S.J.P. Todd: Factorizations of Algebraic Expressions. Report UKSC0055, IBM UK Scientific Centre, Peterlee, UK, Apr. 1974.

[26] O. Hanson: Design of Computer Data Files. Pitman, London, 1982.

[27] J.A. Hoffer: Methods for Primary and Secondary Key Selection. Q.E.D. Monograph Series, Data Base Management, no. 9, Q.E.D. Information Sciences, Inc., Wellesley, Mass., USA, 1980.

[28] IMS/VS Version 1 Data Base Administration Guide, program number 5740-XX2 release 2, 9th edition, 1981.

[29] K. Järvelin: Cardinality Estimation in Numeric Online Databases, Information Processing and Management, vol. 22, no. 6, 1986, 523–548.

[30] K. Järvelin: User Charge Estimation in Numeric Databases: a Methodology. PhD. thesis. Acta Universitatis Tamperensis ser A vol. 212. University of Tampere, Tampere, Finland, 1986.

[31] K. Järvelin: A Systematic Approach to Modelling the Costs of Flat Files. Dept. of Mathematical Sciences, Univ. of Tampere, report A152, Tampere, Finland, February 1985.

[32] K. Järvelin: A Systematic Approach to Query Cost Modelling. In: H. Kangassalo (ed.), Information Modelling and Database Management. Lecture Notes in Computer Science. Springer-Verlag, Berlin, 1987. (in press).

[33] H. Kangassalo, H. Jaakkola, K. Järvelin, T. Lehtonen and T. Niemi: System D – An Integrated Tool for Systems Design, Implementation and Data Base Management, in Proc. the IFIP WG 8.1 Working Conference on Automated Tools for Information Systems Design and Development, New Orleans, 1982, pp. 137–148.

[34] W.F. King: On the Selection of Indices for a File. Report

RJ 1341, IBM Research Laboratory, San Jose, CA, Jan. 1974.

[35] V.Y. Lum, N.C. Housel and B.C. Housel: A General Methodology for Data Conversion and Restructuring, IBM J. Res. and Develop., vol 20, No. 5, 1976, 483–497.

[36] D. Maier: The Theory of Relational Databases. Pitman, London, 1983.

[37] S.B. Navathe: Schema Analysis for Data Base Restructing, ACM TODS, Vol. 5, No. 2, 1980, 157–184.

[38] S.B. Navathe and J.P. Fry: Restructuring for Large Databases: Three Levels of Abstraction, ACM TODS, Vol. 1, No. 2, 1976, 138–158.

[39] S.B. Navathe and A.G. Merten: Investigations into the Application of the Relational Model to Data Translation, in Proc. ACM Sigmod Conf., San Jose, 1975, pp. 123–138.

[40] T. Niemi: Formal Restructuring Functions for Hierarchical Data Bases, International Journal of Computer and Information Sciences, Vol. 12. No. 6, 1983, 385–411.

[41] T. Niemi: A Seven-Tuple Representation for Hierarchical Data Structures. Information Systems, Vol. 8, No. 3, 1983, pp. 152–157.

[42] T. Niemi: The Specification of Data Reformatting in Data Conversion, Univ. of Tampere, Dept. of Mathematical Sciences, Report A150, 1985.

[43] T. Niemi: Specification of Data Restructuring Software Based on the Attribute Method, International Journal of Computer and Information Sciences, vol. 13, No. 6, 425–460, 1984.

[44] T. Niemi and K. Järvelin: A Straightforward Formalization of the Relational Model. Information Systems, Vol. 10, No. 1, 65–76, 1985.

[45] P. Richard: Evaluation of the Size of a Query expressed in Relational Algebra. in: Y.E. Lien (ed.) Proc. ACM SIGMOD 1981 conf., Ann Arbor, Mich., 1981. pp. 155–163.

[46] M. Schkolnick: Optimizing Partial Inversions for files. Report RJ 1477, IBM Research Laboratory, San Jose, CA, Nov. 1974.

[47] M. Schkolnick: A Survey of Physical Database Design Methodology and Techniques. Proc. 4th VLDB Conf., West Berlin, Sept. 1978, pp. 474–487.

[48] M. Schkolnick and P. Tiberio: Considerations in Developing a Design Tool for a Relational DBMS. Proc. of the IEEE Computer Society's Third International Computer Software & Applications Conference, Chicago, Ill., Nov. 6.-8., 1979, pp. 228–235.

[49] M. Schkolnick and P. Tiberio: A Note on Estimating the Maintenance Cost in a Relational Database. Report RJ 3327 (40084), IBM Research Laboratory, San Jose, CA, Sept. 1981.

[50] P. Selinger et al.: Access Path Selection in a Relational Data Base Management System. In: Bernstein, P.A. (ed.), Proc. ACM-SIGMOD 1979 Conf., Boston, Mass., 1979, pp. 24–34.

[51] M.E. Senko, E.B. Altman, M.M. Astrahan and P.L. Fehder: Data Structures and Accessing in Data Base Systems, IBM Systems Journal, Vol. 12, No. 1, 1973, 30–93.

[52] K.C. Sevcik: Data Base System Performance Prediction Using an Analytical Model. Proc. 7th VLDB Conf., Cannes, France, Sept. 9.-11., 1981, pp. 182-198.

[53] B.A. Shneiderman: Data Structures: Description, Manipulation and Evaluation. Ph.D. Thesis, State University of New York at Stony Brook, NY, 1973.

[54] B. Shneiderman and G. Thomas: An Architecture for Automatic Relational Database System Conversion, ACM TODS, Vol. 7, No. 2, 1982, 235–257.

[55] A. Shoshani: A Logical-Level Approach to Data Base Conversion, in Proc. ACM Sigmod Conf., San Jose, 1975, pp. 112–122.

[56] N.C. Shu, B.C. Housel and V.Y. Lum: Convert: A High-Level Translation Definition Language for Data Conversion, Comm. ACM, Vol. 18, No. 10, 1975, pp. 557–567.

[57] N.C. Shu, B.C. Housel, R.W. Taylor, S.P. Gosh and V.Y. Lum: EXPRESS: A Data EXtraction, Processing, and REStructuring System, ACM TODS, Vol. 2, No. 2, 1977, pp. 134–174.

[58] E.H. Sibley and R.W. Taylor: A Data Definition and Mapping Language, Comm. ACM, Vol. 16, No. 12, 1973, pp. 750–759.

[59] J.M. Smith and P.Y-T. Chang: Optimizing the Performance of a Relational Algebra Database Interface. Comm. ACM, Vol. 18, No. 10, 1975, pp. 568–579.

[60] The Stored-Data Definition and Translation Task Group, Stored-Data Description and Data Translation: A Model and Language, Information Systems, vol. 3 B, 1977, 95–148.

[61] S.Y.W. Su, H. Lam and L. Der Her: Transformation of Data Traversals and Operations in Application Program to Account for Semantic Changes of Databases, ACM TODS, Vol. 6, No. 2, 255–294, 1981.

[62] D. Swartout: An Access Path Specification Language for Restructuring Network Databases, in Proc. ACM Sigmod, Toronto, 1977, 88–101.

[63] T.J. Teorey and J.P. Fry: Design of Database Structures. Prentice-Hall, Englewood Cliffs, NJ, 1982.

[64] G. Thomas and B. Shneiderman: Automatic Database System Conversion: A Transformation Language Approach to Sub-Schema Implementation, in Proc. the IEEE Computer Society's Fourth International Computer Software & Applications Conference, Chicago, 1980, pp. 80–88.

[65] D.C. Tsichritzis and F.H. Lochovsky: Data Base Management Systems, Academic Press, 1977.

[66] J.D. Ullman: Principles of Database Systems. Pitman, London, 1980.

[67] G. Wiederhold: Database Design. McGraw-Hill, NY, 1977.

[68] S.B. Yao: An Attribute Based Model for Database Access Cost Analysis. ACM TODS, Vol. 2, No. 1, 1977, pp. 45–67.

[69] S.B. Yao: Modelling and Performance Evaluation of Physical Data Base Structures. Proc. ACM Annual Conf., Oct. 20–22, 1976, pp. 303–309.

[70] S.B. Yao: Optimization of Query Evaluation Algorithms. ACM TODS, Vol. 4, No. 2, 1979, pp. 133–155.

[71] S.B. Yao and A.G. Merten: Selection of File Organization Using an Analytic Model. Proc. 1st VLDB Conf., Sept. 1975, pp. 255–267.

[72] C.T. Yu and Y.C. Lin: Some Estimation Problems in Distributed Query Processing. IEEE Distributed Computing Systems Conference, 1982, pp. 13–19.
