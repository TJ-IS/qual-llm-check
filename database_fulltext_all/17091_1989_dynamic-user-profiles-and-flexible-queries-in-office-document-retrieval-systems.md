---
otero_id: 17091
otero_key: "CTPPUCQK"
title: "Dynamic user profiles and flexible queries in office document retrieval systems"
authors: "F.A. Schreiber; F. Barbic; S. Madeddu"
year: "1989"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(89)90025-0"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Dynamic User Profiles and Flexible Queries in Office Document Retrieval Systems\*

F.A. SCHREIBER, F. BARBIC

and S. MADEDDU

Dipartimento di Elettronica, Politecnico di Milano, 20133 Milano, Italy

The problem of document management in an Office Information System in view of supporting the decision process by a set of users with different knowledge, capabilities and requirements is considered. User profiles are used to improve the retrieval properties and a control system is outlined to automatically update the utility information used by the searching strategies. user requirements are modeled in Dynamic User Profiles in order to maintain accurate knowledge of the most promising approach to document search, of the interest fields, and of the favourite output format. An example of DUP use is provided adopting a flexible query specification to take advantage of database selection, retrieval via keyword, or full text scanning in a multi-strategy query processing approach. Actual queries are redefined by extracting the aspects suitable for each strategy.

Keywords: DBMS, Information Retrieval, Inverted Index, Office Information Systems, Query Language, Search Strategy, Signature, User Profile.

![](/api/attachments/CTPPUCQK/fulltext/images/755e35ada5ace9c45176a8031a1d3e4d61e75d0f2fe888179e9a9e24f3855ea0.jpg)

Fabio A. Schreiber is full professor of Database Systems at the Electronics Department of the Politecnico di Milano. From 1981 to 1986 he was full professor of Computer Science at the Mathematics Department of the Università di Parma. He received the Dr. Ing. degree in Electronic Engineering from the Politecnico di Milano in 1969. His main research interests are in the field of Distributed Informatics and Information Systems. His current researches include perfor-

mance and reliability evaluation of distributed computing systems. He has been involved in the development of a distributed DBMS sponsored by the Italian National Science Council. On these topics he has authored more than fifty papers and has been invited as a speaker to many workshops and conferences.

He has consulted for several companies and university installations on advanced system design. Prof. Schreiber is the Editor-in-Chief of Rivista di Informatica, the journal of the Italian Association for Automatic Computing (AICA) and he is a member of AICA, of ACM, and a Senior Member of IEEE.

\* This work has been partially supported by CNR-CSISEI and EEC ESPRIT project TODOS. We thankfully acknowledge the comments of Dr. Paola Mostacci who provided the feedback on the prototype OMS. We are also grateful to prof. Giampio Bracchi who revised the original version of this paper and provided useful ideas to improve it.

## 1. Introduction

One of the major problems that must be faced designing an Office Information System (OIS) to support decisions in an office environment is related to the nature of the information handled. Since information circulating in offices is often unstructured or ill-structured, the usual approaches become commonly unsuitable.

Data Base Management Systems (DBMS) can efficiently represent and manipulate objects or events of the real world as well as associations between these different entities, but can only process simple types of data, with no or poor semantic content [5]. In fact, a crucial part of the information content of data base records is contained in the structure that is specified at the schema level.

On the other hand, Information Retrieval Systems (IRSs) deal with natural language text documents (books, papers etc...). This kind of documents may be structured, i.e., they may contain

![](/api/attachments/CTPPUCQK/fulltext/images/27de090f5501c70e02a077e94ffa0a193f767cefed343ec36e656fe3206bf211.jpg)

nals. Federico Barbic received a doctorate degree in Electronic Engineering in 1982 from Politecnico di Milano, Italy and is member of ACM and the IEEE Computer Society.

![](/api/attachments/CTPPUCQK/fulltext/images/5b9c5b16e785a087c8da7d59ae4c7d5c5be4401b4aaa6aa88740b5ce7e291eed.jpg)

Federico Barbic is a Booz, Allen & Hamilton management consultant in the Information Technology area since 1987. Before joining Booz Allen & Hamilton, he was Politecnico di Milano and at IBM Almaden Research Center, San Jose, performing research activities in the office and database systems sectors. On these topics, Federico Barbic has authored over twenty articles, presented at International and National conferences and published on international jour-

Stefano Madeddu received the Dr. Ing. degree in Electronic Engineering from the Politecnico di Milano in 1986 discussing a thesis on the Methodologies for Office Systems Design. Since then, he is collaborating with the Electronics Department of the Politecnico as a Research Assistant. His main research interests are in the field of Information Systems Design Techniques, Office Models, Object Oriented Programming Environment, Automatic Support Tools for information sys-

tems design.

attributes and sections. However, information is also contained in the text parts of the documents or in the set of index terms assigned to them. The semantic of the stored data is therefore given by the interpretation of natural language text objects [18]. The office environment has been shown to be a peculiar one which permeates some aspects both from DB systems and from IR systems.

The first prototype implementation of a system for integrating the two technologies shows the feasibility of an approach, the aim of which is to profit from both [2]:

(1) the integration of techniques as frequency analysis [17], inverted index data organization [13], signature extraction [1,20] and database approaches to document storage and retrieval [19] can be easily achieved;

(2) the system resulting from the integration of these techniques allows better performances than allowed by each of them taken separately, in terms of average response time, recall, and precision (refer to Appendix 2 to have a definition of these elements).

Rather than proposing new techniques, our research aims at merging into a unique framework a series of methods that in our opinion are the most suitable for storing and retrieving office documents with structured data and text. The envisaged system can be briefly outlined in the following points (see fig. 1):

(1) A frequency analysis is applied to each received document, in order to extract a list of relevant terms (abstract of the document). The documents are stored in their original form into a Storage File.

(2) A signature method is used to reduce the size of the abstracts. The signatures of the abstracts are stored into the corresponding Signature File.

(3) A document index, inverted with respect to a small list of keywords, is created and stored into the Index File.

(4) A document classification is applied and its result is stored into the document Data Base.

(5) For each user, a Dynamic User Profile is maintained about his retrieval habits and needs.

(6) Depending on the type of query and the user profile, the most promising search strategy is selected, the corresponding access file (either the signature file, the index file, or the data base) is accessed; the relevant documents are then retrieved from the storage file.

![](/api/attachments/CTPPUCQK/fulltext/images/f08db3cc16069ee7ea5a1c54f39656f82be01040103c758fe79f0e3c3c9fd950.jpg)  
Fig. 1. General framework of the multi-strategy system.

(7) During query processing, a Historical File containing information about the relevance of retrieved documents is maintained. The on-line data structures are periodically reorganized using the information of the historical file.

(8) A dynamic control of the user profiles and of the strategy selection process is performed in order to adjust the system behavior to needed changes.

In fig. 1, the general framework of the system is presented. Bold lines refer to standard storage and retrieval aspects. Dashed lines refer to control and evolutionary aspects.

The DUP information could be used to enhance the man-machine interaction in many other ways, such as the adaptation of the output to user preferences or to workstation characteristics, the management of context and interest fields information that allow the system to greatly improve the user-interaction adding the elements that are specific to a particular user to any general query. Anyway, in this paper we will concentrate our attention on the use of DUP information to perform a multistrategy approach to information retrieval.

This approach is introduced in section 2 outlining the adopted model for user profiles and the three retrieval strategies that are supported, namely database selection, retrieval via keywords, and full text scanning via signatures. In section 3 an example of DUP use to enhance the effectiveness of information retrieval is described illustrating the query analysis and query processing method.

## 2. The Multi-Strategy Approach

The role of document handling is of great importance within office activities, but few of the Office Information Systems designed and implemented explicitly address the problems of retrieval by content of ill-structured documents [7].

Actually, different strategies seem promising for office document retrieval, but none of them appears to overcome the other in all circumstances, that is for each type of query and/or characteristics of the issuing user.

Besides, very little attention has been paid to the importance of taking into account that the performance of a particular search strategy (based on a particular document representation) is heavily dependent on the context in which the query is specified and on the peculiar features and habits of the employee that is searching the document base [10,14].

An important point that we want to highlight is that in an office system, the concept of performance in information retrieval must be filtered through the current situations that are being faced. In certain cases, a fast response time is needed regardless of the precision obtained, in other cases a high response time is accepted if the overall user satisfaction can be enhanced. Obviously, when the context is exactly the same, a more efficient technique is more appreciated, but usually the user unsatisfaction depends on the fact that the IRS is too inflexible [15].

The ultimate goal of the system proposed in this paper (sec. 3) is to support the retrieval of office documents by offering different search strategies that are automatically selected on the basis of query and Dynamic User Profile (DUP). A sophisticated control system will regulate the DUP and, hence, the strategy selection process. However, this goal can be attained in four evolution phases with increasing complexity.

In the first phase, the three strategies are available (database selection, retrieval via keywords, and full text scanning), and the user must explicitly specify in the query what kind of strategy he chooses. In this situation the system acts in a way that is similar to several existing systems.

In the second, a supervisor is added that automatically analyzes the query and the status of the selection session (starting, focusing, browsing). On the basis of this analysis, the supervisor can select the most promising strategy.

In a third level of evolution, also the user profile and the current context are taken into consideration. In this situation even the same query issued by two users, or by the same user in different contexts, may be processed in different ways.

The fourth and more sophisticated level of the multi-strategy system refer to the system dynamic reconfiguration, i.e., the ability of modifying the user profiles on the basis of the relevance analysis and the historical file in which the specified queries and the identifiers of the selected documents are collected.

If a particular search strategy is the most indicated for a query issued by a certain user, a flexible system will choose it. Notice that users are often very forgiving for some lack of efficiency if they can realize that some understanding has been achieved toward the right search direction.

![](/api/attachments/CTPPUCQK/fulltext/images/0d4c75511ef9fdb68c6a045a65bb64b11764341fac7f5cbca246d65408decbb7.jpg)  
Fig. 2. Query interpreter.

Our approach, that leads to a four level system, is to allow several search strategies to coexist in the office system. For each user and for each context (current situation and query), it is possible to choose the retrieval strategy that most likely will provide the best performance in that particular moment. Fig. 2 shows a refinement of the Query Interpreter block.

Since Office systems users are essentially the office employees, it is worthwhile to store a user profile for each of them to support the strategy choice.

From the conceptual point of view, the search for the documents dealing with 'hardware products announcements' and the search for 'the orders of customer #100 during 1984' are very similar. However, it is clear that, while the first case should be faced as a 'classical' information retrieval query, the second one allows a more straightforward approach by using a database selection. From the user viewpoint, it is essential that the kind of man-machine interaction be essentially the same, i.e. the system, and not the user, should decide if an information retrieval selection rather than a database inquiry is more suitable. The approach presented in this paper tries to make transparent these system choices.

## 2.1. Concepts

In this section, we introduce the terms at the basis of the multi-strategy approach. We discuss the enterprise thesaurus first, then we distinguish between absolute and relative relevance. Finally we outline the organizational, temporal, and query dimensions of office organizations and the taxonomy of the used strategies.

## Enterprise thesaurus

The Enterprise Thesaurus is a collection of elementary concepts related to the domain of interest of the organization.

The issues related to the construction and the maintenance of thesauri have been presented widely in the Information Science literature. Several contributions give detailed prescriptions for organizing and relating information concepts to generate and maintain library thesauri. The problem of thesaurus automatic building is currently a research problem and some promising techniques have been discussed in [17].

We do not address in this paper the problem of creating and managing the enterprise thesaurus: we simply assume that it exists and it captures the concepts of the domain of interest.

## Absolute and relative relevance

The problem of information retrieval is traditionally dominated by the problem of assigning to each stored document d and for each possible query q, the relevance value R(d, q) of the document to the query, with general criteria. We want to emphasize here that the traditional approach of assigning a level of relevance to documents in correspondence to the queries is reductive and insufficient for the office environment in which the dynamics and the organizational structure justify other dimensions along which to assign the relevance values of documents. Moreover, by considering additional aspects of the retrieval problem that are typical of the office environment, some of the classical difficulties of IR research, such as modeling user profiles for an extremely varying user population, become easier to solve.

We define three dimensions along which to measure the relevance values, namely the organizational dimension, the temporal dimension, and the query dimension. Thus, we distinguish between absolute relevance and relative relevance (i.e. related to a single dimension or to two dimensions). The absolute relevance of a document is the quality of a document to be relevant to at least one organizational unit, for at least one query, and at least one time.

## The organizational dimension

The office environment is composed of several organizational units (OU) devoted to different functions, such as accounting, procurement, or planning. An organizational unit may contain other lower level OUs. The highest level OU is the enterprise itself, while the simplest OUs are the single employees. Each OU has interests and retrieval requirements slightly different from other OUs. This implies that if an overall classification scheme is adopted, it can not be very selective, since it must average the classification requirements of all the OU.

Let us introduce an example that will be used all along the paper: the Italian National Research Council (CNR) is composed of headquarters in Rome, CNR research institutes all over Italy, and several research centers sited at university departments.

The CNR-CSISEI is the CNR research center at the Electronics Department of the Politecnico di Milano. The CSISEI organizational structure, illustrated in fig. 3, is composed of a Director, an Administrative Secretariat, a Technical Secretariat, and several Research Units. The main classes of document types created or utilized by CSISEI are – estimated and final scientific reports,

\- estimates and appropriation accounts,

\- bibliographies of research works,

\- research documents,

\- book-keeping documents (orders, invoices),

\- personnel management documents (attendances, competitions, examinations, scholarships).

\- laws, standards.

Now, as an example of different classifications of the same document, consider an Annual Working Report: it is classified according to the achieved results by the Technical Secretariat, and according to the expense budget by the Administrative Secretariat.

![](/api/attachments/CTPPUCQK/fulltext/images/a18b618eda499ccdb6666bd76f21554a0c321ae917e7278d7f975b959075ce68.jpg)  
Fig. 3. Organizational structure of CNR-CSISEI.

Table 1  
Time constants.

<table><tr><td>Type of Doc</td><td>T</td></tr><tr><td>Newspaper article</td><td>1–3 days</td></tr><tr><td>Business letter</td><td>1 week</td></tr><tr><td>Quarterly business report</td><td>6 months</td></tr><tr><td>Technical report</td><td>6–12 months</td></tr><tr><td>Legal norms</td><td>1–3 years</td></tr><tr><td>Scientific paper</td><td>2 years</td></tr><tr><td>Book (technical)</td><td>3 years</td></tr><tr><td>Book (humanities)</td><td>10 years</td></tr></table>

The problem arises to link the values of the relative relevance of documents with respect to a given OU to the corresponding values of relative relevance for the other OUs. One possibility is to link the levels by assigning the relative relevance value, that is the maximum of the relative relevance values of the lower level OUs, to the higher level OU. However no general rule can be applied to derive the relative relevance values for OUs that are not directly related. We will see that with the use of User Profiles, the relative relevance value derivation becomes easier.

## The temporal dimension

It has been observed, according to intuition, that the interest of a generic OU about a given document is decreasing with time in a rather regular way. The simplest analytic function to describe this behavior is the negative exponential:

$$
\mathrm{R} _ {\overline {{\mathrm{ou}}}, \overline {{\mathrm{d}}}} (\mathfrak {t}) = \mathrm{R} _ {\overline {{\mathrm{ou}}}, \overline {{\mathrm{d}}}} (\mathfrak {t} _ {0}) \exp \left[ \frac {- \mathfrak {t}}{\mathrm{T}} \right].
$$

Where $R_{\overline{ou},\overline{d}}$ is the interest of the unit $\overline{ou}$ for the document d, T is the characteristic time constant of d.

By experiments on a sample of office documents, it was possible to correlate the type of documents to the temporal interest decrease rate.

Table 1 shows the time constant for some types of documents.

The standard profile of relevance of a given document, for a given OU is shown in fig. 4. Occasionally, the level of interest may change abruptly, as in $t_{x}$ in correspondence to some external event (for instance, new directions of management or changes in the external world). In these cases, the profile has a sudden increase (decrease), but the subsequent behavior can still be described by the given expression.

![](/api/attachments/CTPPUCQK/fulltext/images/71bf8f551e729052df445932d48f76a4e88ff98057213f5f9535124de021736f.jpg)  
Fig. 4. Profile of document relevance.

$$
\mathrm{R} _ {\overline {{\mathrm{ou}}}, \overline {{\mathrm{d}}}} (\mathrm{t}) = \mathrm{R} _ {\overline {{\mathrm{ou}}}, \overline {{\mathrm{d}}}} \left(\mathrm{t} _ {\mathrm{x} _ {i}}\right) \exp \left[ \frac {- \left(\mathrm{t} - \mathrm{t} _ {\mathrm{x} _ {i}}\right)}{\mathrm{T}} \right].
$$

## The query dimension

The query dimension is of main interest to this paper. We want to investigate the following issues:

(a) the possibility to identify a continuous formal relationship between queries and relative relevance values of documents, such that small variations to the query cause small variations to the relative relevance values.

(b) the possibility to consistently support different search strategies for the same query, corresponding to different access methods. Each search strategy is the best for a subset of the possible queries, in terms of recall, precision, and response time. The idea is that a given query should be analyzed to identify which search strategy can be applied most successfully.

## Taxonomy of strategies

The possibility of using several different strategies in the search phase claims for a control system by which a tuning can be made on the driving parameters in order to optimally achieve the required goal.

First of all, we must consider the choice of the optimal strategies to answer a given query. Roughly speaking, we could expect from the different strategies the behavior introduced in Table 2 with respect to the three main performance indexes, response time, recall, and precision.

Table 2 shows the relationships between the goal to be achieved for a query submitted by a given user, and the choice of the strategies which can optimize the given goal. The choice of the strategy to be used is driven by the information in the User Profile about the habits and preferences of the user issuing the query.

The retrieval strategies used in our system are: Database selection. The problems here are connected to the way of extracting a formal query, specified with a SQL-like query language, from the query specified by the user according to the syntax of Appendix 1.

This strategy allows high precision and low response time, but low recall if no keyword has been inserted in the query (low level of structure in the query).

In the case of a collection of scientific papers, each document has a Doc-id, a data, a sender, and a title. In addition a set of authors is associated to each document and a set of topics is used to capture the document content. The resulting Database schema is the following:

DOC:(doc-id, date, title, sender)

TOPIC:(doc-id, topic)

AUTHOR:(doc-id, author).

Retrieval via keywords. The problems here are related to the choice of a small set of keywords that can be used for effectively indexing the stored documents. Keywords must be chosen carefully by an expert of the application and periodically maintained.

Table 2  
Performances of retrieval strategies.

<table><tr><td>Type of performance</td><td>Suitable strategies</td></tr><tr><td>Good response time</td><td>IndexingDatabase selection</td></tr><tr><td>Good recall</td><td>IndexingRetrieval via signatures</td></tr><tr><td>Good precision</td><td>Retrieval via signaturesDatabase selection</td></tr></table>

This strategy allows high recall and low response time. However, since only a small set of keywords is assigned to each document because of the rapid growing of storage dimension, exact matches can not be checked and very precise selection conditions in the queries can not be exploited. So the level of precision attainable with this strategy is generally lower than with the other strategies (see table 2).

The partially inverted index organization corresponding to the collection of scientific papers would be:

\- an inverted index built to allow quick access to documents;

\- an entry of the index created for each word occurring in the title of the document or for every other word that the document creator have highlighted with a particular syntactical command in the text.

Full text scanning with signatures. Several studies show that office queries are often difficult to solve because a precise classification is not applicable and it becomes difficult to remember under which dossier or folder a relatively well known document was stored [11].

In general these cases can not be efficiently faced with the previous strategies and it is necessary to provide a more general facility for scanning the document space looking for the matching document(s).

The most obvious solution is to allow a full text scanning of the documents; however performance problems arise because of the size of the document base, unless specialized hardware is used for scanning [13].

In order to solve the trade-off between fast response time and low device cost, we will adopt the signature technique in compressing the document representations and allowing a quicker scanning [2,12].

This strategy allows high recall and precision, supports exact match and partial match. However, it requires a higher response time with respect to the other strategies, because no access structures can be used and the sequential scanning of the signature file is necessary (See table 2).

Then, we can conclude that the DB approach is very powerful when the query is related to objective aspects, i.e. it refers to the attributes of the documents that have been modeled in the schema, but completely inadequate to solve more informal queries.

The partial inverted index organization provides the best access time, but is actually effective only with subjective queries of the type: 'Retrieve all the documents whose authors wanted to emphasize the concepts: C1, C2, ..., CN'.

Full text scanning is the best strategy to answer pure syntactical queries. Syntactical queries are employed when a string matching is desired or when the number or positions of the occurrences of certain words are of interest. A typical case is the retrieval of a document through the knowledge of the presence of a certain sentence. The support for string matching in office document retrieval was studied in the OIMS Project [9].

The problem that lead to the core of the present paper is: which query language is best suited to express the above types of information (objective, subjective, and syntactical). Also, assuming to have defined a language for general query specification, how do we extract the subquery to be executed according to the three above organizations, and in case more than one subquery is extracted, how do we choose the most promising one.

## 2.2. Definitions

In this subsection we introduce the concepts that we shall use in the subsequent part of the paper.

The concepts that we want to define are:

The concepts that we want to define are:
The Office. The office is the general environment in which documents are accessed. A number of papers have been published on office modeling. In this paper we do not address the modeling of static and dynamic aspects of office work.

For the purpose of this paper, information about the office is stored into two lists of keywords OA and OI that are specific of the considered environment.

OA = oa $_{1}$ , ..., oa $_{n}$ contains the basic activities performed in the office.

OI = $oi_{1}i_{n}$ contains the interest fields of the office.

The group (or department). The group is a vertical partition of the office. Usually one or more office functions are assigned to one group and some aspects of the general environment are essential to the group, while other are marginal to it.

In order to capture the interest field, we describe each group by a keywords list $G_{i}$ that is a subset of OI.

$$
\mathbf {G} _ {\mathrm{i}} = \mathbf {g} _ {1}, \dots , \mathbf {g} _ {\mathrm{m}}; \quad \mathbf {g} _ {\mathrm{j}} \in \mathrm{OI}, \quad \bigcup_ {\mathrm{i}} \mathbf {G} _ {\mathrm{i}} = \mathrm{OI}.
$$

The procedure. Procedures are complex sets of activities that can be directly or indirectly put in relation with the attainment of some office goal.

Each procedure is represented by a keyword list $P_{i}$ , that is a subset of OA, each corresponding to an activity executed in order to achieve the procedure goal.

$$
\mathbf {P} _ {\mathrm{i}} = \mathbf {p} _ {1}, \dots , \mathbf {p} _ {\mathrm{q}}; \quad \mathbf {p} _ {\mathrm{j}} \in \mathrm{OA}, \quad \bigcup_ {\mathrm{i}} \mathbf {P} _ {\mathrm{i}} = \mathrm{OA}.
$$

While executing a particular procedure, the user's information needs are very likely related to the activity performed or to the procedure itself. This information can aid the retrieval process.

The employees. The employees are the agents who carry out the procedures and achieve the office goals. Each employee shows different features, and different approaches to the retrieval should be provided and adopted for answering his needs.

For each employee, a Dynamic User Profile (DUP), discussed in the next subsection, is defined. DUPs integrate the above information and realize cross-references between groups and procedures. In fact, DUPs allow the construction of a 3D matrix representing the whole office (fig. 5).

DUP highlighted in fig. 5 specifies that employee E belongs to group G and executes procedure P. An employee, who performs activities in different groups, can use different DUPs in relation to the task he is executing. DUP information is used by the system in selecting the best search strategy.

![](/api/attachments/CTPPUCQK/fulltext/images/ae70839c7a1899648507c731ed58f30c583da91a7753c2b61a9dd176963bda7e.jpg)  
Fig. 5. Representation of office elements.

## 2.3. User profiles

We define in this subsection the basic features of the Dynamic User Profile (DUP). The information that should be embedded into the DUP covers different aspects:

(1) Information about the most common classes of document types most recently accessed (newspaper article, business, letter, technical report, etc...) The documents of these classes are more likely to be relevant to the particular user. In fact, it is very common that the retrieval system in the office is used for selecting the most used documents.

Information 1 can be obtained automatically during the relevance analysis.

(2) Information about the successfulness of the different strategies in the past queries. It seems reasonable that, if an employee considers one strategy very efficient with respect to the others, this particular strategy should be chosen if the translation of user query into that kind of subquery is possible.

Information 2 is obtained asking the user for an evaluation of his satisfaction for the documents presented as answer to his query.

(3) Information about the terms that a user often specifies in his queries. Very common terms have a low discriminating value within a document base. So, if an employee is used to specify certain terms, they become of little significance to his queries because such terms are mostly referred to the general context that the employee wants to explore. The correct way to face this case is to embed the information about the context into the user profile and not to consider whether or not the employee actually specifies those terms in the queries. For instance, if, in different queries, the user searches for 'office information systems', 'information retrieval in office systems', and 'rule based office prototypes', it can be inferred that the office context is of interest. Thus, the corresponding information is stored in the user profile and the queries 'information systems' 'information retrieval', and 'rule based prototypes' will be equivalent to the previous ones when issues by him.

The advantage of this approach, besides making the query specification quicker, is that the user can feel the system presence and learn to exploit its capabilities.

Information 3 can be obtained by analyzing the queries for each user.

(4) Information about the subjective context. This kind of information considers a few properties of each specific user that can influence the choice of the retrieval strategy, or impose additional constraints to the query. We have identified the following properties:

(a) current position within the organization,

(b) current assignment,

(c) frequency of usage.

We provide here a description of the main characteristics of each property:

Current position; the organizational position of the audience waiting for a given document is an important parameter that can affect the retrieval performance. Within an office organization we can identify the following broad positions:

\- support personnel (secretaries),

\- technical and professional personnel (staff members),

\- managers.

The same query issued by four people (two secretaries and two managers) has given the results of relevance analysis presented in table 3 (Recall = 1 means that all relevant documents have been retrieved).

The average level of precision is

$$
0. 2 5 ^ {*} (0. 5 + 0. 5 + 0. 4 + 0. 5) = 0. 4 7 5.
$$

By exploiting the relevance analysis without enforcing the concept of current position, we can improve the precision while still maintaining recall = 1, by reducing the set of retrieved documents and eliminating the documents having scored 0 (doc. n.6). In this way the average level of precision is

$$
0. 2 5 ^ {*} \left(\frac {5}{9} + \frac {5}{9} + \frac {4}{9} + \frac {5}{9}\right) = 0. 5 2 7.
$$

By exploiting the relevance analysis and the current position information, we can further improve the average level of precision by selectively reducing the set of retrieved documents eliminating those having scored 0 in the specific position. The average level of precision is

Table 3
Relevance analysis. $^{a}$

<table><tr><td colspan="5">10 Documents retrieved</td><td colspan="3">recall = 1</td></tr><tr><td colspan="5"></td><td colspan="3">Relevance [%]</td></tr><tr><td>Doc #</td><td>Sec1</td><td>Sec2</td><td>Mgr1</td><td>Mgr2</td><td>global</td><td>Sec</td><td>Mgr</td></tr><tr><td>1</td><td>R</td><td>R</td><td>R</td><td>R</td><td>100</td><td>100</td><td>100</td></tr><tr><td>2</td><td>N</td><td>N</td><td>R</td><td>R</td><td>50</td><td>0</td><td>100</td></tr><tr><td>3</td><td>R</td><td>R</td><td>N</td><td>N</td><td>50</td><td>100</td><td>0</td></tr><tr><td>4</td><td>R</td><td>N</td><td>R</td><td>N</td><td>50</td><td>50</td><td>50</td></tr><tr><td>5</td><td>N</td><td>R</td><td>N</td><td>R</td><td>50</td><td>50</td><td>50</td></tr><tr><td>6</td><td>N</td><td>N</td><td>N</td><td>N</td><td>0</td><td>0</td><td>0</td></tr><tr><td>7</td><td>R</td><td>R</td><td>R</td><td>R</td><td>100</td><td>100</td><td>100</td></tr><tr><td>8</td><td>R</td><td>N</td><td>N</td><td>N</td><td>25</td><td>50</td><td>0</td></tr><tr><td>9</td><td>N</td><td>R</td><td>N</td><td>N</td><td>25</td><td>50</td><td>0</td></tr><tr><td>10</td><td>N</td><td>N</td><td>N</td><td>R</td><td>25</td><td>0</td><td>50</td></tr><tr><td>Av. prec.</td><td>0.5</td><td>0.5</td><td>0.4</td><td>0.5</td><td></td><td></td><td></td></tr></table>

$^{a}$ R = relevant,  
N = non-relevant,  
Av. prec. = average precision.

$$
0. 5 ^ {*} \left(\frac {5}{7} + \frac {5}{7}\right) = 0. 7 1 4
$$

for secretaries (eliminating doc. n.2 and 10) and

$$
0. 5 ^ {*} \left(\frac {4}{6} + \frac {5}{6}\right) = 0. 7 5
$$

for managers (eliminating doc. n.3, 8, and 9).

For this kind of considerations the current position can be precious to improve the retrieval performance.

Current assignment; The current assignment of a specific user can be useful to narrow the scope of a given query. Let us imagine that two users U1 and U2 issue the same query during different procedures; for instance, Q: 'Last year project proposals'. U1 is executing the procedure P1: 'Prepare the technical annex of a new national project proposal', while U2 is executing the procedure P2: 'Compute the amount of funds requested during last year from the CNR (National Research Council)'. The information about the current assignment can be used to transform Q into $Q_{U1}$ and $Q_{U2}$ , where

$Q_{U1}$ = Technical annexes of last year national project proposals,

$Q_{U2} = \text{Administrative annexes of last year's CNR project proposals.}$

A: domain of recall/precision mix when location allows large results

Each assignment corresponds to a set of very specific terms that allows to adapt each query to a particular procedure.

$$
\begin{array}{l} \text {For instance P1 - > Technical, National} \\ \text {P2 - > Administrative,CNR} \end{array}
$$

Frequency of usage; DUPs are updated periodically and every time a retrieval session is completed. In order to realize correctly the periodical update, it is important to know the user frequency of usage.

(5) Information about the objective context. The objective context can influence the retrieval choices in a way that is independent from the characteristics of the peculiar user. The distinction between objective and subjective context is as follows: a property belongs to the subjective context if it is a property peculiar of the individual, a property belongs to the objective context if all individuals of the group share it. For instance, in a distributed environment based on Wide Area Networks (WAN) with high delay and transmission cost, the cost of the query is related to the size of the result (measured as the number of retrieved documents) and so, the relative importance of precision over recall is applicable to all the users. We identified the following properties:

\- Type of workstation (e.g. an alphanumeric display can not show documents with images or graphics).

\- Location of workstation (e.g. to balance precision vs. recall in order to reduce overall transmission costs and delay).

Location information may impact the relative importance of recall and precision. As mentioned before, if the same query is issued in a distributed environment, the transmission cost and delay are related to the size of the result. Assuming an homogeneous allocation of importance to recall and precision in the average case, the location information is responsible of the reallocation of the levels of importance towards high precision (small size results) or high recall (large size results).

As an example, a query from the CNR headquarters in Rome on CNR documents is placed in domain A (fig. 6), corresponding to high recall with large size complete results; instead, a query on the same documents issued by the CSISEI Administrative Office in Milan, owing to the high transmission cost and delay, is in domain C corresponding to high precision and small size and possibly incomplete results.

![](/api/attachments/CTPPUCQK/fulltext/images/17dc06b3deb6a30e6cad0537b02834624c3b6f56d4786e01ba41599b84112436.jpg)  
Fig. 6. Objective domains.

The type of needs of a particular user in a particular query depends not only on his profile, i.e. the personal approach to the search of office documents, but also on the kind of the current context. Typical information that should be considered in the context description is:

\- Current procedure in which the user is involved.

\- Activity within the current procedure (information can be obtained about the relevance of documents related to the current activity).

\- Location of the querying workstation (possibility of quick browsing, cost of transmission, delay).

\- Scheduling constraints (necessity of fast answer or not).

Information 4 and 5 can be automatically obtained if an overall Office Information System is developed which can take into account the relationships among agents, activities, and resources [8]. Otherwise such information should be explicitly specified by the user.

In order to represent the outlined types of information, we need an articulated structure for the user profiles.

In fact, DUP's are composed by four components:

(a) The Accessed Document vector (AD).

$$
\mathbf {A D} = \mathbf {a d} _ {1}, \dots , \mathbf {a d} _ {k}.
$$

In this vector, for each of the main classes of documents, a measure of the number of accesses is maintained (information 1). In order to capture information 1, temporal information is needed to identify the most recently accessed documents classes.

Then the number of accesses to documents of each class is gradually reduced with time. For instance, ad $_{i}$ can be augmented by one unit for each access to a document of class i and reduced by a fixed quantity for each given period of time to avoid saturation. This updating technique will be illustrated in detail in the following.

## (b) The Strategy Satisfaction vector (SS).

$$
\mathbf {S S} = \mathrm{ss} _ {1}, \dots , \mathrm{ss} _ {\mathrm{h}}.
$$

In this vector, for each of the available search strategies, an integer number is maintained as a measure of the satisfaction of the user (information 2). Initially SS $_{i}$ = 0 for all i. Each time a user issues a query, the system provides a possibly empty set of document identifiers. After having examined the result provided by the system, the user is asked to rate his level of satisfaction for the current session. The rating values are very good, good, acceptable, poor, very poor. For instance, if the strategy i has been used, SS $_{i}$ will be set (up to a MAX and down to a MIN) to:

$\mathbf{SS}_i + 2$ if very good

$$
\mathrm{SS} _ {\mathrm{i}} + 1 \text {   if   good   }
$$

$$
\mathrm{SS} _ {i} \text {   if   acceptable   }
$$

$$
\mathrm{SS} _ {\mathrm{i}} - 1 \text {   if   poor   }
$$

$$
\mathrm{SS} _ {\mathrm{i}} - 2 \text {   if   very   poor.   }
$$

In this paper we assume h = 3, since the considered search strategies are database selection, retrieval via keywords, and full text scanning.

(c) The Keywords Descriptor vector (KD).

$$
\mathbf {K D} = \mathrm{kd} _ {1}, \dots , \mathrm{kd} _ {\mathrm{p}}.
$$

This vector has the size of the vector OI whose elements represent the concept of interest for the specific office; KD contains a boolean value for each keyword. The keywords that describe the interests of the user (information 3) are represented by '1' and the not-relevant ones are represented by '0'. That is, each time a search strategy is selected, the relevance analysis is performed and, if necessary, the DUP is affected by the results of the analysis. A continuous control on the content of KD is performed using the Domain of Interest (a vector of positive integers with the size of KD). For a given query, for each relevant document, the following steps are executed:

## 1. retrieve the document keywords;

2. update the domain of interest by adding 1 to the relevance value of each keyword of the document.

Every time interval $T = a/f_{usage}$ , where a is a constant and $f_{usage}$ is the user frequency of usage of the system, the values of the domain of interest are decreased by a fixed quantity D. The personalized evaluation of T is very important. A fixed value for T, say 1 week, would cause a sporadic user (i.e. once in a month) to have his domain of interest re-initialized every time he connects to the system, and a very frequent user (i.e. more time in a day) to have his domain of interest saturated. So, for the sporadic user a T = 4 months could be satisfying and so would be T = 3 days for a frequent user. The decay time is then quicker if the frequency of usage is high.

The typical temporal profiles of the keyword indexes of the domain of interest of a given user are illustrated in fig. 7.

![](/api/attachments/CTPPUCQK/fulltext/images/862bc908ecc61c924a8985fd86fa5e6fdc62839bb5c5cd972483ad4bb13c34f3.jpg)  
Fig. 7. Keyword indexes.

If the index value of a keyword remains for a long time (say 10T) above the threshold ( $WK_{1}$ ), the corresponding element of KD will be set to 1. Instead if the index value of a keyword remains for a long time below the threshold ( $WK_{2}$ ), the corresponding KD element will be reset to 0.

When an index value reaches the saturation level, its value is not further increased; however, the decreasing component remains active and if the index eventually drops and remains for a long time below the threshold level ( $WK_{3}$ ), the keyword value in KD is reset to 0.

The values of the decreasing quantity D and of the threshold level must be chosen carefully. In fact, a high value for D and a threshold near saturation level could cause system instability because index values would switch very frequently from above to below the threshold. Instead, a low value for D and for threshold would cause a large number of keyword indexes to remain above the threshold with a consequent loss of the meaning of this information.

(d) The Context Description vector (CD).

$$
\mathbf {C D} = \mathbf {c d} _ {1}, \dots , \mathbf {c d} _ {r}.
$$

Information 4 and 5 are maintained in this integer vector. Each element of CD is devoted to the representation of one of the previously outlined aspects. For instance, $cd_{1}$ can represent the level of education of the user, while $cd_{i}$ may represent the class of workstation from which the session was started.

The DUP is costantly updated during the use of the system. The displacements of the DUP within the multi-dimensional space of all the DUPs are usually of minor entity because, if the general approach to the retrieval problem does not change, the modifications from the usual field of interest are very little. Such a case is addressed as a Continuous DUP Modification. An option 'Don't care', instead of the retrieval satisfaction, can be specified by the user when he doesn't want the relevance analysis be performed on the results of his query. This option can be useful when queries are submitted for training, experimentation, or demonstration purposes.

On the contrary, a different case is considered in which an external event makes the sub-space of the potential relevant documents to change. For instance, if the role of an office employee changes or if an employee is assigned to another project, the sub-space of relevant documents is deeply modified. Such a case is considered as a Discrete DUP modification.

![](/api/attachments/CTPPUCQK/fulltext/images/79ed1d18cee20d39c208e122dfa7f09fb7fa2c13f34ca3c6d7e0c42955ee82cd.jpg)  
Fig. 8. Relationships between DUP and the other elements.

It is worth noticing that all the behavioral features of the DUP remain unchanged both in continuous and in discrete DUP modification. This is due to the fact that the DUP contains not only information related to the professional context (that can vary slowly or quickly), but also information that are related to the personal approach of the employee toward the stored information (preference of structured information, preference of high recall regardless of the response time etc...). Such a personal approach, which can be inferred from the rating of strategies obtained from SS, is likely to be constant over several years.

In fig. 8 the main relationships between DUP and the other elements of the office system are shown.

## 3. Queries

This section illustrates one of the possible use of DUP information to improve the effectiveness of IR. We show how the SS vector could be used to choose the best retrieval strategy. Future developments of our work will concentrate on the realization of a system exploiting other DUP elements, such as AD and KD, to let the user indicate only the particular elements he is interested in, while the system introduces the elements and the keywords corresponding to user interests or activities.

Queries can be analyzed with respect to different features; the most important being the level of structure of the query and the range of accepted response time.

In our system, each query is composed by (the syntax of the query language can be found in

Appendix 1.): a facultative performance setting part, in which the user can specify one or two parameters (chosen between recall, precision and response time) he wants to maximize, a type specification part, in which a set of document types, whose structure is known to the system, is specified in order to restrict the scope of the search, and an instance value specification part, in which the conditions on the content of the document instances are specified.

For instance, a typical query could be:

```c
/*Begin query*/
{retrieve
/*Performance setting*/
{} 
/*Type specification*/
{from letters
/*Instance value specification*/
where sender match Olivetti
and
date match May 1984
and
text contain M24, personal computer, announcement}}.
/*End query*/
```

The ‘from’ clause is the type specification part, and the ‘where’ clause is the instance specification part. The concept of type in office document systems has been discussed in [3]. With the instance value specification part, the qualifications of the relevant documents are described.

As far as the level of structure of the query is concerned, we can distinguish:

(1) Queries that should be mapped into a database selection subquery: the type specification part allows to restrict the search domain to a reasonable size, and the instance specification part allows a selection (i.e. some 'match' clause exist). In this case, the database query, generated by translating the original query, will be considered satisfying if it's possible to identify at least 40% of the attributes of the DB table corresponding to the type specified. In the above example, the database query would be (in SQL-like):

```txt
{select doc# from LETTER where SENDER = OLIVETTI and DATE = MAY 1984}.
```

Notice that the generated query can be shown to the user for validation. Moreover, the user is acquainted with the dropping of the specification about the text part and with the selected search strategy.

(2) Queries that could be answered using the search strategy via keywords: the instance specification part contains some conditions on the set of office keywords of OI (see sec. 2.2). In this case, a query for the keyword inverted index subsystem is generated by translating the original query. The subquery will be considered satisfying if it extracts at least 50% of the elements specified in the instance value specification part. In the above example, the resulting query would be:

## {select doc#

keywords Olivetti, personal computer, announcement}.

Also in this case the user is informed of the system choices. All documents containing at least one of the keywords are returned.

(3) Queries that are composed by relevant words (keywords or not) and that should be managed with the most general techniques used in full text office retrieval systems [20]: when the above strategies can not be applied successfully, because the level of structure of the query is very low, the full text scanning, always applicable, remains the only effective search strategy.

In the above example, the resulting query would be:

## {select doc#

relevant words Olivetti, May, 1984, M24, personal computer, announcement}.

All the document signature are scanned and the documents containing at least one of the relevant words are returned.

In order to cope with the fourth level of the multi-strategy system, which performs a dynamic reconfiguration of the DUP on the basis of the relavance analysis (sec. 2), we need to perform a deeper evaluation of the user query. This technique, based on the concept of Distance between query and DUP in the n-dimensional document space, is still object of study and will be an interesting topic for further researches, so we introduce here its basic features.

In order to map the query and the user profile into the n-dimensional document space, we use the Keyword Descriptor (KD, a part of the user profile already discussed in subsec. 2.3) and the new vector: the Query Descriptor, QD.

QD is a Boolean vector, of the size of OI, having a '1' if the corresponding keyword was specified in the query and a '0' otherwise.

For evaluating the distance between query and user profile, the keywords specified in the query are explicitly considered, while the DUP keywords that have not been specified are considered neutral, because it is very common that a relevant document contains also some other keywords in addition to the specified ones. [note: this approach can cause in the long run a saturation of DUP keywords, because the keywords not present in DUP are emphasized in the distance. A control based on the keywords use is thus necessary for limiting the number of keywords in each DUP].

For instance, if the complete set of office keywords is:

OI: <personal computer, accounting, maintenance,

announcement, IBM, Olivetti>

and the KD vector for the current user is:

KD: $\langle1,0,1,0,1,1\rangle$

since the QD vector for the current query is:

QD: $\langle1,0,0,1,0,1\rangle$

for evaluating the distance between user profile and the query, the Distance vector, D is computed:

D: $\langle0,0,0,1,0,0\rangle$

where $d_{i}=qd_{i}\not\supset kd_{i}$ ( $qd_{i}$ does not imply $kd_{i}$ )
The distance between DUP and Q is then defined as follows:

distance (DUP, query) = $\Sigma_{i}d_{i}$

In this case the distance between the user profile and the query is 1. When the distance between DUP and query is higher than a threshold value $T_{1}$ for more than $T_{2}$ times, the DUP keyword descriptor is modified in order to cope with the changed interests. It's our opinion that, in future, this technique would allow a reconfiguration of the DUP more effective than that obtained using the Domain of Interest (sec. 2.3).

## 3.1. Query Processing

In the previous section we gave an example of query specification. A query contains a number of elements (matching values, keywords or relevant words) that are likely to be present in the desired document(s). Queries are processed by retrieving all the documents matching at least one of the specified terms and by displaying the retrieved documents ranked in a descending matching order. Information about the relevance of the retrieved documents is then used for updating the DUP and the historical file. Each search strategy makes use of a different access method: if a database selection is executed, the access method of the DBMS is used, if the retrieval via keywords is chosen the access method via inverted index is used, if full text scanning is selected, the document signatures are sequentially accessed.

DUP information and query structure will drive the Query Interpreter (QI) in the choice of the method. The analysis of the query performance setting part defines three different situations corresponding to different behaviors of the QI:

(a) The user doesn't specify any parameter in the performance setting part; the QI deduces that the method with best value in the Strategy Satisfaction (SS) vector of the user DUP, should be the most promising one. So, the QI tries to translate the query into a subquery corresponding to that method.

If the translated subquery is satisfying (it catches enough elements), it is applied, otherwise the QI considers the second value in SS vector and verifies if the second method allows a profitable translation. The last possibility is that the third method must be adopted. Note that, being the sequential scanning strategy always applicable, there is anyway a solution to the problem.

(b) The user specifies one parameter; in relation to the parameter specified, table 2 defines the two strategies that could maximize it. The QI chooses the one with higher value in the SS vector and verifies if the translated subquery is satisfying; otherwise the second method is adopted.

(c) The user specifies two parameters; having two parameters to maximize, table 2 defines one method that the QI applies. If the translation is not possible the specified parameters are ignored and the query is processed as in situation a.

Then the retrieved documents are presented to the user as an answer to his query together with the indication of the adopted strategy and the user is asked for an evaluation of his satisfaction to update the corresponding SS element.

A promising idea refers to the use of more than one method during query processing. The rationale is that in the different cases, it is possible to obtain a total cost that is less than the cost of a single method because some of the terms can be discarded.

From an implementation point of view, we have to distinguish between two possible architecture classes: traditional single-processor systems and multiprocessor or distributed systems. In fact, in the first case it can be reasonable to look for the single strategy representing the best compromise in attaining the required goal. In the second case we can conceive the possibility of using a couple of strategies in parallel during the retrieval phase and then merging the results. While, in principle, the second approach should give better results, at least as far as the recall is concerned, only an experimental evidence on a real system can say if the benefit is worth the cost in complexity.

For instance, if sequential and retrieval via keywords accesses are used, the total resulting cost is lower than the cost of each strategy applied by itself. In fact, using the sequential access method, all the matching documents are retrieval (recall = 1) at the end of the sequential scanning of the access file. Using the retrieval via keyword access method, a subset of the matching documents are retrieved (recall < 1). However, only a small index has been accessed with this method. Hence, the response time can be much lower than that of the sequential access method. The system should show first the documents retrieved with the keyword access method and then the remaining documents found with the sequential access method.

## 4. Conclusions and Future Work

The definition of a Dynamic User Profile has been introduced. DUPs could allow significant improvements in user-machine interaction in office environment. We have presented in this paper, one of the possible utilization of DUPs: a multi-strategy approach to the problem of searching documents. The aim is to interpret dynamically the user queries, and generate subqueries with emphasis on data-base selection, retrieval via keywords, and full text scanning.

A partial prototype system, Office Message System, OMS has been implemented at Politecnico di Milano on a VAX 11/780 using C language. A detailed description of OMS can be found in [2]. The system was experimentally used in an Italian Office. This experiment showed some weak points of the prototype itself, such as the interaction with users required by the document input (in contrast with most IRSs which are completely automatic), the memory and processing overhead, required by system realization. These issues, however, are not of main concern owing to the constant improvement of the performances of office workstations.

On the other hand we proved that the proposed approach for storing and retrieving office documents can be implemented in offices without requiring specialized hardware and software. The possibility of specifying whatever list of words (keywords or not) in queries results very useful in many operational cases. Finally, the use of the historical file for adapting the stored information to the user habits was considered another positive issue.

Future work includes a refinement of the control algorithms, the implementation of the dynamic reconfiguration components of the system and the use of DUPS to personalize the outputs according to the user preferences and capabilities.

## Appendix I

Concise syntax of OMS query language

Query → {Retrieve Query\_spec}
Query\_spec → Performance setting Type\_spec
Performance\_setting → {{response time}
[recall]
[precision]}
Type\_spec → {from Type\_name where Instance\_spec}
Type\_name → string
/\* Whatever type name defined into the system\*/
Instance\_spec → Attr\_spec | (Attr\_spec log\_op Attr\_spec)
[Log\_op Instance\_spec]

Attr\_spec → Attribute\_name Matching\_op Data\_op

Attribute\_name → string

/\* Whatever attribute name defined into the type name \*/

Matching\_op → match |contain |not equal

Data\_op → string [,string] /\*When Data\_op is composed by more than one string, the attribute\_name can match with any of the strings\*/

Log\_op → and |or

## Appendix 2

## Retrieval output

The retrieval output can be described by four parameters related to the retrieved (or dismissed) documents [16] and by the response time.

Let us call:

RR the number of retrieved relevant documents

RN the number of retrieved non-relevant documents
NR the number of not retrieved relevant documents
NN the number of not retrieved non-relevant documents

RT the response time.

Using the first four parameters it is possible to define several evaluation measures like recall, precision, fallout, Q-measure, E-measure, etc. [17,6]. While we refer to the bibliography for the definition of these measures, we mention here only:

recall, defined as $\frac{RR}{RR + NR}$ ,

precision, defined as $\frac{RR}{RR + RN}$ ,

because of their relevance to this paper.

The fifth parameter, i.e. the response time is not explicitly considered in IR literature, but is very important in an end-user environment like the office.

A discussion of the use of these parameters for the definition of a Goal Function and of the characteristics of the retrieval strategies can be found in [4].

## References

[1] Ahuja S.R. and Roberts C.S., "An Associative/Parallel Processor for Partial-Match Retrieval using Superimposed Codes", Annual Symposium on Computer Architecture, pp. 218–227 (1980)

[2] Barbic F. and Illuzzi S., "An Office Message System",

Proc. of the RIAO-85 Conference, pp. 589–612, Grenoble, France (18–20 March 1985)

[3] Barbic F. and Rabitti F., "The Type Concept in Office Document Retrieval", Proc. of the 11th International Conf. on Very Large Data Bases, Stockholm (Aug. 21–23, 1985)

[4] Barbic F. and Schreiber F., "Multi-Strategy Search in Office Document Retrieval Systems", Politecnico di Milano, Internal Report n. 85–21 (July 1985)

[5] Biller H., "On the Architecture of a System Integrating Data Base Management and Information Retrieval", in Lectures notes on Computer Science, Salton (ed.), Berlin (1983)

[6] Bollmann P., "Two Axioms for Evaluation Measures in Information Retrieval", in Proc. of the third joint BCS and ACM symposium, ed. Van Rijsbergen C.J., pp. 233–246, Cambridge University Press, Cambridge (1984)

[7] Bracchi G. and Pernici B., "The design requirements of office systems", ACM Trans. on Office Information Systems, vol. 2, n. 2, pp. 151–170 (April 1984)

[8] Bracchi G. and Pernici B., "SOS: A conceptual model for office information systems", Data Base, vol. 15, n. 2 (Winter 1984)

[9] Choy D., Barbic F., Gueting R., Ruland D. and Zicari R., "Document Managing and Handling", Proc. of the IEEE Office Automation Symposium, Gaithersburg (27–29 April 1987)

[10] Croft W.B. and Thompson R.H., "An Expert Assistant for Document Retrieval", COINS Technical Report 85-05, University of Massachusetts at Amherst (1985)

[11] Faloutsos C. and Christodoulakis S., "Signatures Files: An Access Methods for Documents and its Analytical Performance Evaluation", ACM Trans. on Office Information Systems, vol. 2, n. 4, pp. 267–288 (1984)

[12] Faloutsos C., "Signature Files: Design and Performance Comparison of Some Signature Extraction Methods", in Proc. of the ACM-SIGMOD 1985 International Conference on Management of Data, ed. Navathe S. pp. 63–82, Austin, TX (May 28–31, 1985)

[13] Haskin R.L. and Hollar L.A., "Operational Characteristics of a Hardware-based Pattern Matcher", ACM Trans. Database Syst., vol. 8, n. 1, pp. 15–40 (March 1983)

[14] Korfhage R.R., "Query enhancement by user profiles", Proc. of the third joint BCS and ACM symposium, pp. 111-122, Cambridge University Press, Cambridge (1984)

[15] Morehead D.R. and Rouse W.B., "Models of Human Behavior in Information Seeking Tasks", Information processing & Management, vol. 18, n. 4, pp. 193–205, Pergamon Press (1982)

[16] Van Rijsbergen C.J., Information Retrieval, Butterworths, London, England (1979 2nd edition)

[17] Salton G. and McGill M.J., Introduction to Modern Information Retrieval, McGraw-Hill (1983)

[18] Schek H.J., "Methods for the administration of textual data in database systems", in Information Retrieval Research, ed. R.N. Oddy, Butterworths, London, England (1981)

[19] Tsichritzis D., "OFS: an integrated form management system", VLDB 80, Montreal, Canada (Oct. 1980)

[20] Tsichritzis D. and Christodoulakis S., "Message files", ACM Transactions on Office Information Systems, vol. 1, n. 1 (Jan. 1983)
