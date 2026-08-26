---
otero_id: 25268
otero_key: "6U8F32HA"
title: "A Query-Driven Approach to the Design and Management of Flexible Database Systems"
authors: ""
year: "2002"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2002.11045739"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Query-Driven Approach to the Design and Management of Flexible Database Systems

Andrew N. K. Chen , Paulo B. Goes & James R. Marsden

To cite this article: Andrew N. K. Chen , Paulo B. Goes & James R. Marsden (2002) A Query-Driven Approach to the Design and Management of Flexible Database Systems, Journal of Management Information Systems, 19:3, 121-154, DOI: 10.1080/07421222.2002.11045739

To link to this article: http://dx.doi.org/10.1080/07421222.2002.11045739

![](/api/attachments/6U8F32HA/fulltext/images/4f2e64fab3a6bbf095b19088b4ea6bbc4fdd39059919a585de7b367e780bcfd3.jpg)

Published online: 23 Dec 2014.

![](/api/attachments/6U8F32HA/fulltext/images/d238bb459a88df75d35090217dcb59bb9d7dd26bd1f7b50694e8ff22d9aac85e.jpg)

Submit your article to this journal

![](/api/attachments/6U8F32HA/fulltext/images/2f4d6b5039e036cf07b97f3c2f107b0a32634ac66f7010dc828f8625340069af.jpg)

Article views: 20

![](/api/attachments/6U8F32HA/fulltext/images/ced93fe7df17a40e1b2ef31a3d0a7845031561b181d2158b229846f028a2fd22.jpg)

View related articles

![](/api/attachments/6U8F32HA/fulltext/images/12ec6244f46a52dc815787378b8f3c6123e94a0dbb57ec900b1114e3bfe4036b.jpg)

Citing articles: 1 View citing articles

# A Query-Driven Approach to the Design and Management of Flexible Database Systems

ANDREW N.K. CHEN, PAULO B. GOES, AND JAMES R. MARSDEN

ANDREW N.K. CHEN joined Arizona State University as an Assistant Professor in 1999. He received his Bachelor of Business Administration from Soochow University in Taiwan, M.S. in Accountancy from George Washington University, and Ph.D. in Operations and Information Management from the University of Connecticut. His current teaching and research interests include electronic commerce, database management, knowledge management, and business and Web programming applications. His research work has appeared in or has been accepted by the Journal of Management Information Systems, Decision Support Systems, Journal of Electronic Commerce Research, and international conferences such as ICIS, AMCIS, and DSI.

PAULO B. GOES is an Associate Professor and Gladstein Professor of Information Technology and Innovation, Co-Director of the Treibick Electronic Commerce Initiative (TECI) and Associate Director of CITI (Connecticut Information Technology Institute), Department of Operations and Information Management, University of Connecticut. Dr. Goes received his M.S. and Ph.D. degrees in Computers and Information Systems from the University of Rochester. He also has a M.S. degree in production Engineering from the Federal University of Rio de Janeiro, Brazil. His research interests are in the areas of Internet technologies and electronic commerce, design and evaluation of models for e-business, online auctions, database recovery and security, and computer networking and technology. Dr. Goes joined the University of Connecticut in 1990. His publications have appeared in several leading journals including Management Science, Decision Sciences, Operations Research, Communications of the ACM, IEEE Transactions on Communications, IEEE Transactions on Computers, INFORMS Journal on Computing, and Decision Support Systems. He is a member of ACM and INFORMS.

JAMES R. MARSDEN came to the University of Connecticut in 1993 as Professor and Head, Department of Operations and Information Management, School of Business Administration. He was part of a three-person concept-development team that initi ated and oversaw the development of the Connecticut Information Technology Institute and is currently serving as its Executive Director. He developed and implemented the Treibick Electronic Commerce Initiative that is funded through a generous gif provided by Richard Treibick and the Treibick Family Foundation. Dr. Marsden also serves as Director of the OPIM/SBA MIS Research Lab and is a member of the Advisory Board and Steering Committee of CIBER (Center for International Business Education and Research). He was a member of the edgelab development team and currently serves on the edgelab Steering Committee, which selects and resources projects and oversees operations. Dr. Marsden is a two-time winner of the Chancellor’s Award for IT Excellence and a cowinner of the Team Connecticut Program Award from the Office of Economic Development. He has a lengthy research publication record in market innovation and analyses, economics of information, artificial intelligence, and production theory. His research work has appeared in Management Science, Journal of Management Information Systems, IEEE Transactions on Systems, Man, and Cybernetics, American Economic Review, Journal of Economic Theory, Journal of Political Economy, Computer Integrated Manufacturing Systems, Decision Support Systems, and numerous other academic journals. He was part of the IT Visioning and IT Planning Groups for the University and has played a leading role in developing the School of Business Administration as both a campus and national leader in IT education and research. Professor Marsden received his A.B. from the University of Illinois and his M.S. and Ph.D. from Purdue University. Having completed his J.D. while at the University of Kentucky, he has been admitted to both the Kentucky and Connecticut Bar.

ABSTRACT: The need for timely information in the e-business world provides the impetus to develop a flexible database system with the capability to adapt and maintain performance levels under changing queries and changing business environments. Recognizing the importance of providing fast access to a variety of read-only appli cations in today’s e-business world, we introduce the systems architecture for devel oping and implementing a flexible database system to achieve considerable gains in processing times of read queries. The key component of a flexible database system is query mining, the concept of determining relationships among query properties, alternative database structures, and query processing times. We validate the flexible database system concept through extensive laboratory experiments, where we embed learning tools to demonstrate the implementation of query mining.

KEY WORDS AND PHRASES: database management, database querying, data mining, inductive learning, information retrieval, neural networks.

THE ENVIRONMENT OF TODAY’S E-BUSINESS WORLD is that dozens of applications spanning supply chain management (SCM), enterprise resource planning (ERP), and customer relationship management (CRM) are integrated. For most companies operating in this environment, reading the data is their principal database activity, with writing comprising a much smaller proportion of database operations.As more end users are given Web access to read data from these enterprise-wide information systems, the database systems are subject to an increasing number of unpredictable and complex queries. This causes significant performance degradation and can interrup business operations.

Consider Wal-Mart. Over a single year, its database system has grown to more than 100 terabytes and is second in capacity only to that of the Pentagon [18]. Each terabyte is the equivalent of 250 million pages of text. More than 7,000 suppliers and 11,000 other users currently access Wal-Mart’s database system, making more than 120,000 queries a week. Through the system, buyers and vendors query information and analyze sales trends by item and by store to make informed decisions on replenishment.

They look at customer buying trends, analyze seasonal buying trends, make mark down decisions, and react to merchandise volume and movement at any time [49]. With more than 30 applications running on the system, users can ask virtually any question, predictable or unpredictable. Slow query processing for this type of database system can seriously affect not only Wal-Mart’s operations but also those business operations of all other users. We also note that commercial solutions aiming at handling unpredictable queries are gaining in popularity [14].

It is well recognized that relational databases, which are designed in third norma form (3NF), typically perform well in a predictable transaction-oriented, update-in tensive environment [32, 50]. To achieve and maintain good performance in such environments, a number of performance-enhancing techniques have been proposed and are generally available to database administrators [22, 43]. These techniques include performance tuning utilities and query optimization engines. Performance tun ing utilities investigate database operational parameters (such as buffer size, caching management, and indexes) that might affect database performance (such as eliminate performance bottlenecks). Query optimization engines select the most efficient way to process the query operations by the physical database given the logical characteristics of the query.

However, it is well established by researchers and practitioners that a transactionoriented 3NF database suffers from serious limitations when subjected to read queries of a different nature (such as decision-oriented) or queries that require that severa base tables be joined [2, 13, 20, 27, 31, 51]. The reality is that no single database structure, regardless of how carefully it might have been designed and operationally tuned, is able to provide acceptable performance levels to every possible query in today’s e-business environment of several integrated applications.

One attempt to address the related issue of dealing with certain types of decision support read-only queries has been data warehousing. The data warehouse, an addi tional structure, is maintained in parallel to the operational system to provide the means to answer those decision-oriented queries that the operational database system is poor at answering. There is vast literature on the issues concerning planning, designing, building, using, and managing data warehouses. Good overviews of the issues are Blaha [4], Bonifati et al. [5], Chaudhuri and Dayal [9], Gardener [15], Inmon [21], and Rundensteiner et al. [42]. Because data warehouses are typically built along prespecified dimensions of the underlying database, they work well for answering aggregate queries along those very dimensions, such as total sales by quarter, location, or product line. There are substantial performance issues associated with answering ad hoc queries whose requested data items have not been appropriately materialized along the dimensions of the underlying data warehouse structure [1, 51].

Another important example of making available additional database structures for read-only access in parallel with the transaction-oriented structure comes from today’s implementation of Web-based applications. For obvious security and performance reasons, these applications commonly maintain a separate database as the source of data for the Web access. Replicating the transaction database for read-only purposes allows users of Web-based applications to browse large volumes of data without interfering with the transaction system. Delta Airlines’ new DNS (Delta Nervous System) implements this concept through various read-only data stores that are fed through a middleware layer [45]. All major database vendors currently provide replication solutions aimed at read-only snapshots, which tend to be created to suppor specific Web applications.

We propose a flexible database system (FDS) to better address today’s e-business environment of several types of end users posing a wide variety of ad hoc queries and using dozens of integrated applications. We seek to provide an alternative preferable to the current approach of constructing application-specific, read-only images or materialized views of the transaction-oriented database. We provide a query-driven method that utilizes intelligent design and selects read-only components to provide the fastest possible read access for a wide variety of queries, including unanticipated queries.

Our contribution lies in presenting an architecture for a flexible database system to solve the problem of speeding up the processing of read-only queries in environments, such as the Web environment of integrated supply chain, which are characterized by (1) extreme high frequency of read-only queries as compared to write queries, often reaching a read:write ratio of 1000:1; (2) enormous disparity of how queries are formulated due to the complexity of the underlying information content and differences in the objectives of the user population; and (3) dynamic nature of the query access, which can lead to queries that are labeled unpredictable relative to the curren database structure. We follow the approach of providing “proof of concept” to the proposed architecture, along the lines of developing a prototype and conducting thorough experimentation, in the same vein as Kumar et al. [30] and Purao et al. [35].

We propose query mining as the concept of determining relationships among quer properties, alternative database structures, and query processing times. Query mining intelligently assigns an incoming read query to the most appropriate database structure (that is, the database structure that provides the fastest processing). Query mining uses learning tools to study relationships between query properties, alternative database structures, and query processing time. Finally, it provides the means for the FDS to continuously learn and adapt if the pattern of submitted queries drastically changes over time.

## Flexible Database Systems and Query Mining

## The Flexible Database System Conceptual Architecture

IN OUR PROPOSED APPROACH, THE FLEXIBILITY of being able to yield high performance (speed) while answering different types of read queries is achieved by having several database structures concurrently active at any point in time, as shown in Figure 1. The read-only structures are designed and implemented so that the differen types of read-only queries can be answered within acceptable time. These read-only structures are fed with updates received by a separate transaction-oriented database structure that is specifically designed and implemented to capture the update activity of the system. Alternatively, the company could choose to keep their operational legacy systems as the update structure, in which case a middleware would need to be in place to transfer the updates to the read-only structures. Updates would be reflected onto the read-only structures through periodic refresh operations. The database adminis trator (DBA) can also trigger updates to the read-only structures at any point in time or they can be automatically executed when specific conditions are met.

![](/api/attachments/6U8F32HA/fulltext/images/75dfc6fff6d30f4ec4072114b865e983d92e8bc37d593391e8ce0d8796eac5e5.jpg)  
Figure 1. Conceptual Architecture of Flexible Database Systems

Figure 1 describes the conceptual architecture for the operation of our flexible database system. $\mathrm { D B S } _ { 0 }$ is the structure that will receive and reflect all the updates. We envision DB $\mathrm { \sf S } _ { 0 }$ being designed following the conventional relational database design methodology to 3NF, and constantly tuned to improve the performance of operational transactions. The set $\{ \mathrm { D B S } _ { 1 } , . . . , \mathrm { D B S } _ { n } \}$ represents the structures that are specifically designed for information retrieval purposes. At specified intervals, or as determined by system conditions, the updates collected by $\mathrm { D B S } _ { 0 }$ are reflected into $\{ \mathrm { D B S } _ { 1 } , . . . , \mathrm { D B S } _ { n } \}$

Our Query Analyzer module first analyzes a query submitted to the system. If the query is an update query, the Scheduler forwards it to $\mathrm { D B S } _ { 0 } ,$ . If the query is a retrieva query, it is assigned to the structure in $\{ \mathrm { D B S } _ { 0 } , \mathrm { D B S } _ { 1 } , . . . , \mathrm { D B S } _ { n } \}$ that provides the fastest processing time. The Query Analyzer keeps a knowledge base derived from query mining that assists in the assignment decision. For each query, along with its structural characteristics (that is, selection criteria, referred fields, and so on), the pair [actual processing time, selected database structure] is collected and stored in the

Query Analyzer. Query mining is used to identify queries of “similar performance characteristics” and to provide prediction or classification rules that assign queries to the most appropriate active structure. The Performance Monitor module keeps track of read-only query performance variations and flags substantial changes in the nature of the query mixes submitted to the database. It also recommends the restructuring of any of the structures in $\{ \mathrm { D B S } _ { 1 } , . . . , \mathrm { D B S } _ { n } \}$ , if that action will significantly improve the overall performance of the system.

To further present our idea, we outline the following seven steps as the overal process associated with the design and implementation of an FDS:

1. Design of the update structure. As mentioned above, the update structure $\mathrm { D B S } _ { \mathrm { 0 } }$ will be designed following the “conventional” approach of database design that is directed at improving the performance of update transactions. It is expected that designs geared toward 3NF implementations will be used here in conjunction with the continuous application of performance-tuning utilities. Step 1 starts with a logical representation of the information contents of the database, where an Entity-Relationship (ER) model [12] or a Unified Model ing Language (UML) [29] model can be used. This conceptual model is important as reference to the design of the read-only structures in Step 2.

2. Design of the read-only candidate structures. To design the set of database structures that will cover the widest range of possible queries, one needs to first have a thorough understanding of the underlying information content. The conceptual/logical representation captured in Step 1 is helpful at this point. The first goal is to list possible categories of queries that can be posed to a database with such information content. These queries vary from straightfor ward and predicted operational queries to queries that increasingly integrate different portions of the information content. There are two activities involved in the categorization of queries:

a. Exhaustive generation of queries. Originally, it is useful to generate queries using the reference (normalized) structure $\mathrm { D B S } _ { 0 } .$ For each possible information source of the normalized structure (every table, every feasible join of tables), queries are created by randomly varying the following parameters: selection criteria, number of conditions in the selection criteria concatenated by $\mathbf { \ddot { \mu } } _ { \mathrm { A N D } } \mathbf { \vec { \mu } }$ or “OR,” number of attributes selected.

b. Categorization of queries. After the synthetic generation of queries, we broadly categorize them with the use of variables associated with query properties such as: input source (which $\mathrm { D B S } _ { \mathrm { 0 } }$ table or combination of tables are necessary to process the query), number of $\mathrm { D B S } _ { \mathrm { 0 } }$ tables that need to be joined and selectivity factor. These parameters have been identified in previous research [6, 16, 23, 24, 28, 46] as explanatory of query performance and indicative of the query complexity. In the experiments we describe in the next section we show how we categorize queries using input source.

After formulating an exhaustive list of possible query types for the information content displayed by $\mathrm { D B S } _ { 0 } ,$ the second goal of this step is to create a set of feasible candidate read-only structures. The approach used by Chen [10] starts from the normalized structure $\mathrm { ( D B S _ { \mathrm { 0 } } ) }$ and constructs alternative structures of equivalent information content by exhaustively joining two tables at a time. The idea is to investigate how the several possible combinations of denormal ized tables will perform against various types of queries that refer to multiple normalized tables. Results of this approach are reported in Chen et al. [11] with a strong indication that one only needs to consider those structures that contain joins of no more than two tables. Also, the extensive experiments conducted in Chen et al. [11] with environments that are similar in nature to bench mark databases proposed in Gray [17], suggest that the ideal number of candidate structures that deliver robust performance to a wide variety of access patterns is between five and ten. We are currently conducting research to be able to prescribe the best way to identify such structures. At this point, we recommend the following approach:

a. Complete enumeration of all possible combinations of denormalized tables, if feasible;

b. Scale down the database and synthetically emulate the original environment by means of constructing a prototype in which the complete enumeration is feasible; and

c. Use expert knowledge from database designers and administrators to construct five to ten alternative structures to populate the consideration set. struct five to ten alternative structures to populate the consideration set

Other possible approaches for selecting candidate structures that have been proposed in the literature include working with alternate structures that are not completely substitutable [36] and using view materialization techniques [3, 8, 37, 52].

3. Building and maintaining the knowledge base: query mining. The starting points in this step are the outcomes of Step 2: (1) a list of possible categories (types) of queries for the information content at hand, and (2) the set of all candidate structures to be evaluated. Query mining is based on learning tools and is computational in nature. At the end of this step, prediction rules are compiled in order to indicate which database structure provides the fastest processing time to a query based on its characteristics. This step is detailed later in this section, with experimental results reported in the remaining sections of this paper.

4. Decision on which read-only structures to keep active. Given all the possible candidate structures that are generated in Step 2, and the classification rules derived by query mining in Step 3, one does not need to keep all the structures active at the same time to achieve good overall performance. In Chen [10] and Chen et al. [11], comprehensive experiments and a statistical method for selecting robust structures given various combinations of query mixes are presented. A robust structure is defined as one that performs well across various possible query mixes.

5. Assigning queries to the most appropriate structure. The outcome of query mining is a set of classification or prediction rules that associate query characteristic with the most appropriate available structure in terms of processing time. These rules are implemented in the proposed architecture in the Query Analyzer, which use them to determine to which structure to send the query. Before sending the query to the Scheduler, its Structured Query Language (SQL) statement is translated from the original $\mathrm { D B S } _ { \mathrm { 0 } }$ version to the appropriate DBS $( i = 1 , . . . . , n )$ ) version. The translation rules are straightforward and are kept in the Query Analyzer module. In the third section we demonstrate through two comprehensive experiments how this can be carried out.

6. The refresh operation. The refresh operation reflects the updates received by $\mathrm { D B S } _ { \mathrm { 0 } }$ onto the read-only structures. The frequency of this operation is determined by both the update intensity experienced by $\mathrm { D B S } _ { \mathrm { 0 } }$ and the urgency of providing the latest data to the end users. Automatic triggering of the refresh operation upon meeting certain conditions can also be programmed.

7. The restructuring operation. From time to time, the Performance Monitormodule may detect that one of the structures in $\{ \mathrm { D B S } _ { 1 } , . . . , \mathrm { D B S } _ { n } \}$ is not providing satisfactory performance for the current pattern of query mixes that the system is subject to. That structure will then be replaced by one of the structures from the candidate pool that is best suited to perform well under the new query pattern. The decision about which new structure to materialize is made based on the information of the knowledge base developed in the Query Analyzer.

Clearly, there are substantial costs associated with implementing and operating an FDS. Since it involves running several concurrent database structures, there are addi tional storage costs. The update costs associated with the refresh operations may be substantial. The incidence of these operations depends on the currency needs dictated by the applications. In addition, we must consider the restructuring costs of replacing one of the active structures with another that performs better under the current condi tions. Of course, the frequency of this operation depends on the volatility of the query environment. The fourth section illustrates an example of quantification of costs in the specific environments that are the focus of our simulation and experimentation.

## Query Mining

Query mining, a process based on data mining principles, identifies and analyzes the relationships between queries (based on query properties), query processing time, and alternative database structures. At the core of Step 3 outlined in the previous subsection, query mining is a critical element in the initial design of the FDS. The first input to query mining is a list of possible categories (types) of queries that are allowed by the underlying information content of the database. The second input is the set of candidate structures that are considered.

For two key reasons, each query is initially written based on the reference structure $\mathrm { D B S } _ { 0 }$ :

1. DB $S _ { \mathrm { 0 } }$ will always be part of the FDS. Its data definition is not likely to change very frequently. It thus provides a “fixed” set of arguments to be used in the syntax of all queries. Later on during the operation of the FDS, all applications and end users will submit queries written for $\mathrm { D B S } _ { 0 } .$ . The Query Analyzer will automatically convert these queries to the appropriate structure syntax.

2. By having all queries written for the same structure, we are able to assess a proxy measure for the complexity of each query. As will be seen in the third section, we use the number of $\mathrm { D B S } _ { \mathrm { 0 } }$ tables needed by each query as the proxy for query complexity.

The process results in the identifying or capturing of important query properties that affect the processing time. For example, in the pilot studies we present in the next section we used the following properties (the rationale behind these choices and more details are presented in the third section): input source, selectivity factor, size of the result tuple, number of indexed fields in the selection criteria, and number of selection criteria.

The query properties for each query are captured. Each query is rewritten in severa versions, one for each database structure that is available. The appropriate version of each query is then run against each database structure and the processing time is recorded. This is done through setting up all the candidate database structures in a lab environment so that the necessary data for query mining is collected for each query and each database structure. The outcome of the lab experiments is the determination of the best database structure that is available to process each query. This information, along with the query properties, constitutes the input to the classification phase of query mining.

The queries are divided into two sets: (1) a training set used as input to the learning tool in the derivation of the prediction/classification models, and (2) a testing set used for cross-validation of the models. The classification/prediction models obtained in the training phase provide pairings of queries and corresponding efficient database structures in the form of rules, as in the following example:

IF Selectivity Factor > 0.0432

AND Number of Tables Joined = 3

AND Number of Indexed Keys = 1

THEN Assign Query to DBS7

If validation conditions are satisfied with the testing set of queries (such as better than a required efficiency rate), we adopt these models in subsequent phases. An “efficiency rate” is measured by the percentage of accurate classifications of the queries in the testing set to be processed by the corresponding “best” database structure. That is, if there are 100 queries in the testing set and the “required efficiency rate” is 90 percent, a derived classification model will meet the validation condition when the model accurately predict at least 90 queries of the testing set to be processed by the corresponding “best” database structure.

After the FDS is implemented, query mining continues. Information on queries and on processing results continually update the knowledge base embedded in the system to store pairings of queries (query mixes) and corresponding efficient database structures.

## Learning

In this initial study of query mining for demonstration purposes, we use inductive learning and neural networks as the learning tools. At this point, we do not attempt to justify either inductive learning or neural networks as a “best learning tool” for query mining. Instead, we use these tools to demonstrate the concept. Future studies can focus on comparing prediction performance of various learning tools, human expertise, and simulations in order to identify the “best” tools for query mining implementation.

## Inductive Learning

Inductive learning utilizes instance-to-class generalization. This technique has been applied widely in areas such as classification/mining [41, 44] and financial analysis [26]. This technique classifies given examples to different classes based on the examples’ properties (attributes). The classification of interest here is the pairing of queries (query mixes) and corresponding efficient database structures. To apply inductive learning in this fashion, we start with one-trial learning from examples based on the existing database environment and queries.

In this study, we use C4.5 (refined ID3) [38, 39, 40, 41] to conduct inductive learning applications. C4.5 constructs decision trees and generates production rules<sup>2</sup> from the given training examples (a detailed description of C4.5 can be found in Quinlan [40]). C4.5 utilizes a pre-pruning technique and a post-pruning technique to derive a fairly small decision tree without sacrificing prediction accuracy in order to save future computing time for prediction purposes since the problem of finding the smallest decision tree consistent with a training set is NP-Complete [19]. These pruning techniques discard one or more potential or existing subtrees and replace them with leaves (classes). The derived decision trees are much smaller and simpler than those without pruning. C4.5 also generates production rules as an alternative form of classification model in order to make the classification model more understandable to human beings. A production rule has the form of A ®B. That is, if a case (example) has property A or property set A, this case belongs to class B.

## Neural Networks

A neural network, sometimes termed an “artificial neural network,” is a model tha mimics a biological neural network. This technique has been applied in several areas including data mining [44] and financial analysis [33, 47, 48]. A neural network is a set of connected nodes called neurons. Each neuron receives input(s), processes necessary summation and transformation of input(s), and delivers a single output. The learning process actually occurs through repeated adjustments of “weights” on connections among neurons in attempts to make the output value match the target value for all training examples. The learning process of a neural network tries to recognize patterns and relationships in the data it processes. In this study, we use California Scientific Software’s Brainmaker as our neural network tool.

Brainmaker uses the back propagation rule for learning. The neural network starts the learning process by randomly assigning weights at some levels for connections among neurons. After each training run with input examples, the neural network incrementally changes the weights and tries to minimize the difference (called delta) between the actual output (class) and the target output. The learning process stops when we reach a desired delta. We can use the trained neural network to predict the classes for new examples.

## Proof of Concept—Pilot Experiments on the Flexible Database System Approach

IN THIS SECTION WE PRESENT two experimental studies to illustrate and provide “proof of concept” of our FDS approach. The first experiment utilizes a rather simple database application, whereas the second study moves on to a more complex, higher-end database engine. We use the step-by-step methodology introduced in the second section to illustrate how the approach is carried out in each study. Specifically, we are able to implement and demonstrate Steps 1 (design of normalized structure), 2 (design of read-only structure), 3 (data mining), and 5 (assignment of queries to most appropriate structure). As noted earlier, the techniques necessary to complete Step 4 (decision on which read-only structures to keep active) are presented in Chen [10] and Chen et al. [11]. Step 6 (refresh operation) is straightforward with the timing being applicationdriven. Step 7 (restructuring operation) is the focus of currently ongoing research.

## Experiment I

## Step 1—Design of the Reference Normalized Structure

Figure 2 presents the entity-relationship (ER) design of the underlying application for Experiment I. It also shows the 3NF design of the reference structure, DBS0, consisting of four tables, each with several fields that are numerical or text. All the primary and foreign keys are indexed.

## Step 2—Design of Read-Only Structures

We elected to construct the alternative read-only structures with the exact same information content presented by DBS0 in Figure 2. By exhaustively considering pairwise joins of the tables in DBS0 we obtained seven other database structures (DBS1 – DBS7). For example, joining original Relation1 and Relation2 of DBS0 forms a new relation (table) called Relation12. The combination of {derived Relation12, Relation3, Relation4} forms an alternative read-only structure termed DBS1. The set of candidate database structures is presented in Table 1.

Design of Queries. Based on DBS0 we constructed 400 read (selection) queries tha were designed to comprehensively represent the set of possible queries of interest for the underlying information content. Four general categories (types) were used, with 100 queries in each. Using the original database structure, DBS0, as reference, we constructed 100 queries in each of four categories: (1) single-relation queries, (2) two-relation queries, (3) three-relation queries, and (4) four-relation queries. Each query could have up to nine selection criteria (that is, conditions that records from tables have to meet in order to be selected as the output).

<sub>Designofthe</sub>R<sup>eferenceStructureDBS0forE</sup>  
<sub>d</sub> <sub>by</sub> <sub>[University</sub> <sub>of</sub> <sub>Flor</sub><sup>ida]</sup> <sup>at</sup> <sup>11:34</sup> <sup>05</sup> <sup>Au</sup>  
![](/api/attachments/6U8F32HA/fulltext/images/1c7c281d0cccf20c03f57cc447271de8ea180a6ee44b4eb1c4c21f7256b9239e.jpg)

Table 1. Eight Database Structures for Experiment I

<table><tr><td>Database structure</td><td>Explanation</td></tr><tr><td>DBS0</td><td>Four relations (original design, normalized).</td></tr><tr><td>DBS1</td><td>Three relations. Relation12 (combining Relation1 and Relation2 as one new relation), original Relation3, and original Relation4.</td></tr><tr><td>DBS2</td><td>Three relations. Relation13 (combining Relation1 and Relation3 as one new relation), original Relation2, and original Relation4.</td></tr><tr><td>DBS3</td><td>Three relations. Relation24 (combining Relation2 and Relation4 as one new relation), original Relation1, and original Relation3.</td></tr><tr><td>DBS4</td><td>Two relations. Relation13 (combining Relation1 and Relation3 as one new relation) and Relation24 (combining Relation2 and Relation4 as another new relation).</td></tr><tr><td>DBS5</td><td>Two relations. Relation123 (combining Relation1, Relation2, and Relation3 as one new relation), and original Relation4.</td></tr><tr><td>DBS6</td><td>Two relations. Relation124 (combining Relation1, Relation2, and Relation4 as one new relation), and original Relation3.</td></tr><tr><td>DBS7</td><td>One relation. Relation1234 (combining Relation1, Relation2, and Relation3, and Relation4 as one new relation).</td></tr></table>

Note that the above-defined two-relation, three-relation, and four-relation queries might become single-relation queries if applied on other database structures listed in Table 1. This general classification is intended to give a broad sense of the complexity of a query in terms of number of tables needed to be joined, which in turn reflects the underlying number of fundamental entities or relationships involved. Each query constructed for DBS0 was written in seven other versions, to be applied against each corresponding structure DBS1 to DBS7.

Operating Environment. Eight personal computers with Intel Pentium-based microprocessors and identical configurations were used in the experiments. Given the simplicity of the database, Microsoft Access was used as the database management system. Programs written with Access Basic were used to run the queries. Experiment II used Oracle in a more complex database environment.

Each query was run on each of the eight database structures with processing times recorded for each. Our measurements of query processing times did not include display time to a computer monitor.

Preliminary Analysis. Before applying query mining and the two selected learning techniques to the data compiled after running all queries against all candidate structures, we completed the following preliminary analysis. By comparing processing times for each query/database structure pair, we identified the database structures that provided the shortest processing times for each query. We present the results in Table 2, where queries are grouped according to the classification (single-relation queries, two-relation queries, and so on) presented above. Table 2 provides the following results for each database structure: total number of queries from each category (type) that had the shortest processing time, total processing time for each category (type) of query, and the average additional processing time (in percentage) in comparison with the shortest time for each category (type).

For example, DBS0 provided shortest processing times for 94 out of 100 single relation queries. The total time used to process all one-relation queries with DBS0 was 641 seconds, and, on average, DBS0 used 11.4 percent more time to process al the single-relation queries than the time used if each one of the queries was sent to and processed by the corresponding efficient database structure for that query.

This preliminary analysis provides several insights that differ from what we migh expect a priori and further solidifies our argument for an FDS. Commonsense database practice would have indicated that the normalized structure is best suited to process all the single-relation queries. We could also expect that, in general, an n-relation query is best processed by structures that materialize the join of those n base tables together.

The experiment results confirmed the commonsense expectations for 94 percent of the single-relation queries, but the confirmation rate fell rapidly as the number of relations in a query increased. For the two-relation queries, 74 percent of the commonsense expectations held. For the three-relation queries, the rate fell to 46 percent and reached only 38 percent for the four-relation queries. A series of mean comparison tests were conducted for average processing times of these commonsense expectations and best possible processing results for each of these four query catego ries. In each case (see Table 3), we found statistically significant differences (in each case at very small p-values < 0.05). The only case that we might say common sense holds close to true is for single-relation queries. For the single-relation queries, using DBS0 might be marginally satisfactory (good enough) since the statistically signifi cant difference shows a p-value smaller than 0.05, but greater than 0.01.

DBS0 was indeed the structure that provided the shortest processing time for the most queries (that is, 148) from the set of 400 queries. However, this held true for only 37 percent of the queries. The experiment results suggest two key points: (1) a priori “commonsense” expectations should not be used to design structures for queries that are join-intensive, especially if these queries come from an unpredictable dynamic environment; and (2) even the best overall structure is perhaps best for only for a minority of possible queries (for instance, in our example, only one-third of the queries). The results, in fact, support the points raised above that a fixed structure is not likely to be an apt choice for today’s dynamic business environment where queries of various join complexities are commonplace.

<table><tr><td colspan="9">Distribution of queries to corresponding database structures providing shortest processing time</td></tr><tr><td>(in number of queries)</td><td>DBS0</td><td>DBS1</td><td>DBS2</td><td>DBS3</td><td>DBS4</td><td>DBS5</td><td>DBS6</td><td>DBS7</td></tr><tr><td>Single-relation queries</td><td>94</td><td>3</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Two-relation queries</td><td>25</td><td>20</td><td>23</td><td>20</td><td>11</td><td>1</td><td>0</td><td>0</td></tr><tr><td>Three-relation queries</td><td>17</td><td>17</td><td>2</td><td>15</td><td>1</td><td>18</td><td>28</td><td>2</td></tr><tr><td>Four-relation queries</td><td>12</td><td>6</td><td>1</td><td>7</td><td>25</td><td>1</td><td>10</td><td>38</td></tr><tr><td>Total</td><td>148</td><td>46</td><td>27</td><td>43</td><td>38</td><td>20</td><td>38</td><td>40</td></tr><tr><td colspan="9">Absolute total processing time of database structures with different types of queries</td></tr></table>

<table><tr><td>(in seconds)</td><td>DBS0</td><td>DBS1</td><td>DBS2</td><td>DBS3</td><td>DBS4</td><td>DBS5</td><td>DBS6</td><td>DBS7</td></tr><tr><td>Single-relation queries</td><td>641</td><td>774</td><td>759</td><td>755</td><td>832</td><td>1539</td><td>971</td><td>2126</td></tr><tr><td>Two-relation queries</td><td>1400</td><td>1525</td><td>1493</td><td>1211</td><td>1334</td><td>2207</td><td>1517</td><td>2347</td></tr><tr><td>Three-relation queries</td><td>2509</td><td>1936</td><td>2662</td><td>2110</td><td>2252</td><td>2927</td><td>1850</td><td>2502</td></tr><tr><td>Four-relation queries</td><td>3261</td><td>2695</td><td>2975</td><td>2628</td><td>2191</td><td>3259</td><td>2361</td><td>2339</td></tr><tr><td>Total</td><td>7811</td><td>6930</td><td>7889</td><td>6704</td><td>6609</td><td>9932</td><td>6699</td><td>9314</td></tr><tr><td colspan="9">Relative average percentage of extra processing time compared to shortest processing time</td></tr></table>

<table><tr><td>(in percentage)</td><td>DBS0</td><td>DBS1</td><td>DBS2</td><td>DBS3</td><td>DBS4</td><td>DBS5</td><td>DBS6</td><td>DBS7</td></tr><tr><td>Single-relation queries</td><td>11.4</td><td>42.8</td><td>39.4</td><td>36.6</td><td>54.9</td><td>179.4</td><td>85.4</td><td>310.7</td></tr><tr><td>Two-relation queries</td><td>76.2</td><td>83.3</td><td>82.6</td><td>59.2</td><td>69.7</td><td>161.5</td><td>95.4</td><td>201.3</td></tr><tr><td>Three-relation queries</td><td>86.7</td><td>47.6</td><td>109.9</td><td>51.5</td><td>78.3</td><td>147.0</td><td>36.9</td><td>108.1</td></tr><tr><td>Four-relation queries</td><td>74.3</td><td>55.0</td><td>75.7</td><td>41.3</td><td>28.1</td><td>103.5</td><td>34.0</td><td>43.3</td></tr><tr><td>Average</td><td>62.2</td><td>57.2</td><td>76.9</td><td>47.2</td><td>57.7</td><td>147.9</td><td>62.9</td><td>165.8</td></tr></table>

Table 3. Summary of Statistical Tests for Each Query Category (t-test: paired two sample for means)

<table><tr><td></td><td>Common sense</td><td>Best possible</td></tr><tr><td colspan="3">Single-relation queries</td></tr><tr><td>Mean</td><td>6.474</td><td>5.737</td></tr><tr><td>Variance</td><td>21.485</td><td>15.871</td></tr><tr><td>t-statistic (p one-tail)</td><td>2.348 (0.01526)</td><td></td></tr><tr><td colspan="3">Two-relation queries</td></tr><tr><td>Mean</td><td>12.240</td><td>9.040</td></tr><tr><td>Variance</td><td>73.607</td><td>32.123</td></tr><tr><td>t-statistic (p one-tail)</td><td>3.128 (0.00229)</td><td></td></tr><tr><td colspan="3">Three-relation queries</td></tr><tr><td>Mean</td><td>17.333</td><td>13.708</td></tr><tr><td>Variance</td><td>98.580</td><td>62.303</td></tr><tr><td>t-statistic (p one-tail)</td><td>4.271 (0.00014)</td><td></td></tr><tr><td colspan="3">Four-relation queries</td></tr><tr><td>Mean</td><td>26.906</td><td>21.188</td></tr><tr><td>Variance</td><td>85.314</td><td>126.093</td></tr><tr><td>t-statistic (p one-tail)</td><td>4.312 (0.00008)</td><td></td></tr></table>

One could also deduce from Table 2 a set of preliminary rough rules for an FDS. By looking at the total processing time of each query category and the average percent age of extra processing time, one could infer the following rules: single-relation queries go to DBS0; two-relation queries go to DBS3; three-relation queries go to DBS6; and four-relation queries go to DBS4. It is directly observable that such a system provides a great improvement from a fixed structure approach. However, it is also clear from Table 2 that the choices are not clear-cut. These preliminary results reinforced the need for conducting a more detailed data mining exercise in which other query characteristics are considered in the assignment of queries to the correspond ing efficient database structure.

## Step 3—Query Mining

Query Properties. For the more comprehensive query mining exercise, we consid ered six query properties that have been generally used in previous research to relate queries to query execution speed [6, 16, 23, 24, 28, 46].

1. Input sources. This query property represents the input sources of data that is needed to answer the query. We use as reference the tables of DBS0. This is a discrete variable since each query only falls into one of these ten categories: A1, A2, A3, A4, A12, A13, A24, A123, A124, and A1234. For example, category A1 contains queries that generally refer to information originally contained in Relation1 of DBS0. Category A12 refers to queries that concurrently need information from the original Relation1 and Relation2.

2. Selectivity factor. Selectivity factor used in the experiments is the expected proportion of tuples from a table to be selected as the output for a query. This is a continuous variable with a range from zero to one. For example, the data values in Field1-5 have the range from one to 1,000; so, the selectivity factor for the query (SELECT Field1-2, Field1-3 FROM Relation1 WHERE Field1-5 > 100) is 0.9. For each query we compute the selectivity factor using the reference structure DBS0. In general, selectivity factors can be estimated from the statistics that are routinely collected by the database management systems (DBMS).

3. Size of a result tuple. This query property is an integer variable that measures the size, in bytes, of the output tuple. For example, the size of a result tuple of the query (SELECT Field1-2, Field1-3 FROM Relation1 WHERE Field1-5 > 100) is six bytes (sum of four bytes for Field1-2 and two bytes for Field1-3).

4. Number of relations joined. This query property measures the number of relations that need to be joined to provide output for the query. This is a discrete variable since each query only falls into one of these four mutually exclusive categories: D1—only from one table; D2—could be from one table or two tables; D3—could be from one table, two tables, or three tables; D4—could be from one table, two tables, three tables, or four tables.

For example, the query SELECT Field1-2, Field1-3 FROM Relation1 WHERE Field1-5 > 100 could get information from Relation1 if posed to DBS0, from Relation12 if posed to DBS1, from Relation123 if posed to DBS5, and from Relation1234 if posed to DBS7. In all these possibilities, information for this query only comes from one table in any database structure, so the query has the property labeled D1. Consider a query that needs information from Relation1 and Relation2, if posed to DBS0 (from two tables), but only needs information from Relation12 if posed to DBS1 or from Relation123 if posed to DBS5 (from one table in each of these latter cases). This query would then have the property labeled D2.

5. Number of indexed keys in selection criteria. This query property represents the number of fields that are indexed among all fields in the selection criteria. In our design of database, we had seven indexed fields that were either primary keys (Field1-1, Field2-1, Field3-1, and Field4-1) or foreign keys (Field2-2, Field2-9, and Field3-3). This is a discrete variable since each query will only have one of these eight mutually exclusive numbers: 0, 1, 2, 3, 4, 5, 6, or 7. For example, the query (SELECT Field1-2, Field1-3 FROM Relation1 WHERE Field1-5 > 100) has only one selection criterion involving Field1-5. Since Field1-5 is not indexed, the query has “0” for this property.

6. Number of selection criteria. This query property measures the number of selection criteria in a query. This is a discrete variable since each query only falls into one of these ten mutually exclusive possibilities: 0, 1, 2, 3, 4, 5, 6, 7, 8, or 9.

Query properties can impact input cost (read input data), output cost (write outpu data), or processing cost (CPU [central processing unit] calculations and join processing) for query processing. These effects are described in Table 4.

Table 4. Query Properties and Their Effects on Query Processing-Related Costs

<table><tr><td>Query property</td><td>Rationale</td></tr><tr><td>Input relation(s)</td><td>Affects input and processing cost</td></tr><tr><td>Selectivity factor</td><td>Affects output and processing cost</td></tr><tr><td>Size of result tuple</td><td>Affects output cost</td></tr><tr><td>Number of table joined</td><td>Affects processing (join) cost</td></tr><tr><td>Number of indexed key in selection criteria</td><td>Affects processing (join) cost</td></tr><tr><td>Number of selection criteria</td><td>Affects input and processing cost</td></tr></table>

We utilized these six query properties as explanatory factors. There are certainly factors other than these query properties that might influence the processing time (input, output, and join costs) for a query [34], including: (1) type of join (such as natural, semi, or outer join), (2) implementation of join (such as nested-loops, sortmerge, or hash join), (3) join partitioning function (such as complete, disjoint, variable overlap, or minimum overlap), (4) hardware characteristics (such as CPU power, I/O [input/output] bandwidth, and buffer size), and (5) query optimization strategy. In our experiments, all these factors were treated as fixed because we used the same database management system (same type of join, same implementation of join, same join partitioning function, and same query optimization strategy) and hardware envi ronment (same hardware characteristics) for query processing. These factors are usually environment and system specific.

As we mentioned in the subsection “Query Mining,” the queries are divided into two sets: (1) a training set used as input to the learning tool in the derivation of predic tion and classification models, and (2) a testing set used for cross-validation of the models. In our experiment, we constructed 400 read (selection) queries. These 400 queries were divided into two sets—a training set of 300 queries and a testing set of 100 queries. As suggested by Quinlan [40] and California Scientific Software [7], a portion of cases should be randomly selected to form a testing set to validate derived classification models. In our experiment, 100 queries were randomly selected to form the testing set.

A case with the six properties (described previously in this section) of a query along with the corresponding “best” database structure for processing the query was inputted to the learning tools. The learning tools derived classification models based on the 300 cases of the training set and were validated with the 100 cases of the testing set. The derived classification models can then be used to predict which database structure is the corresponding “best” for a future query with a specific combina tion of those six properties.

Inductive Learning. We used C4.5 as the inductive learning tool to generate classification models in the forms of a decision tree and production rules. Twenty-five percent was used as the confidence level to prune the decision trees and production rules. For a given confidence level, the upper limit on this probability can be found from the confidence limits for the binomial distribution. C4.5 simply equates the predicted error rate at a leaf with this upper limit, on the argument that the tree has been constructed to minimize the observed error rate. If replacement of a subtree with a leaf, or with its most frequently used branch, would lead to a lower predicted error rate, then the tree is pruned accordingly [40]. We also required that any test used must have at least two outcomes with a minimum two cases (query examples) in each outcome to ensure the predictive power. This can avoid deriving a complex decision, which has as many leaves as query examples, that is, each leaf representing only one specific query example.

Neural Networks. The neural network used for the experiment was structured with two hidden layers. We chose to use two hidden layers since we found that, for our experiment, using two hidden layers to train the data and classification models performed better than using either one hidden layer or three hidden layers. A standard sigmoid transfer function (having the form $1 / ( e ^ { - 1 } + 1 )$ ), where I is the activation or output value) with a low saturation limit of zero and a high saturation limit of one was used. The training tolerance was set at 0.1, which implies that the output value must be within 10 percent of the range of the training pattern to be considered acceptable. The networks were set up to continue training until all training facts meet the 0.1 tolerance rate or to stop after 1,000 training runs.

## Step 5—Assignment of Queries to Corresponding Efficient Database Structures

The three learning models (C4.5 decision tree, C4.5 production rules, and neura networks) each provided a classification schema to assign each query to the corresponding efficient database structure. Here we present analyses of the efficiency of the assignments prescribed by each technique.

We compared query processing results for the following scenarios:

1. Each query was processed with specific database structures that actually provided the shortest processing time for each corresponding query.

2. Each query was assigned using each of the three classification models (two inductive learning models—production rules and decision trees, and neura network prediction model) for assigning queries to corresponding (predicted) efficient database structures.

3. All queries were processed using the “rough rules” devised for four structures, as outlined in the previous section.

4. All queries were processed with one “best” individual database structure. This “best” individual database structure had the smallest average processing time among the eight database structures in the experiment.

5. All queries were processed with the “worst” individual database structure. This “worst” individual database structure had the largest average processing time among the eight database structures in the experiment.

The performance of the assignments was measured using processing efficiency rate (PER), average processing time (APT), mean absolute deviation (MAD) of best quer processing time, and mean percentage deviation (MPD) from the best query processing time. The PER is the percentage of queries that were processed with the shortest processing time (with specific database structure[s] used in our experiment) if a specific scenario was applied. APT is the average time of processing each query in the query set. The MAD of best query processing time is the average absolute deviation of individual query processing time from the possible shortest query processing time. The MPD of best query processing time is the average percentage deviation of indi vidual query processing time from the possible shortest query processing time. The results for 100 random queries in the testing/validation set are presented in Table 5.

The results shown in Table 5 are generally consistent on all four criteria. That is, if a database structure for processing queries has a higher PER than another database structure, the more efficient database structure also has a shorter APT, a smaller MAD, and a lower MPD than another database structure. From an analysis of variance (ANOVA) F-test for comparisons of means with the GLM procedure, we find that the APTs for these scenarios are significantly different from each other (see part a of Table 6). In addition, we did three mean comparison tests:

1. inductive learning production rule versus best assignment;

2. best individual structure versus inductive learning production rule; and

3. worst individual structure versus best individual structure.

In each case (see part b of Table 6), we found statistically significant differences (in each case at very small p-values). “Best assignment” is theoretically the best one can achieve, but is practically impossible to implement because, in addition to the continuous maintenance of all structures, one needs complete information about all the queries and the corresponding best structure all the time. We use it here as a top benchmarking measure.

We emphasize three particular outcomes:

1. Using any single fixed database structure to process all varieties of queries yields poor performance.

a. the best individual database structure (DBS4) had only a 12 percent efficiency rate—the best structure provided shortest processing time for only 12 out of every 100 queries;

b. the best individual database structure (DBS4) had a 56.1 percent MPD—for the 88 percent of queries for which the best individual structure did not yield shortest processing time, results indicated that processing times were more than 56.1 percent off optimal; and,

c. the worst individual database structure (DBS5) had only a 4 percent efficiency rate and a 148.1 percent MPD.

2. Using learning tools to assign different queries to corresponding efficient database structures outperforms assigning all queries to any one individual database structure.

The processing efficiency rate (60 percent) of using inductive learning production rules is five times higher than that (12 percent) of using the best individual database structure and 15 times higher than that (4 percent) of using the worst individual database structure. In our study, the two inductive learning models (decision tree and production rules) performed better than the neural network. The production rules model performed better than the decision tree model. This finding confirms the resul in Quinlan [39]. Our expectation is that higher efficiency rates can be achieved when the size of training data increases, as it would in real world applications.

<sub>d</sub> <sub>by</sub> <sub>[University</sub> <sub>of</sub> <sub>Flor</sub><sup>ida]</sup> <sup>at</sup> <sup>11:34</sup> <sup>05</sup> <sup>Au</sup>  
<sub>arisonAmongDiferent</sub>M<sup>ethodsforProcessingQueries(</sup>

<table><tr><td></td><td>Actual best assigned structures</td><td>Inductive learning production rules</td><td>Inductive learning decision tree</td><td>Neural network prediction</td><td>Rough rules</td></tr><tr><td>PER</td><td>100.0%</td><td>60.0%</td><td>54.0%</td><td>45.0%</td><td>40.0%</td></tr><tr><td>APT</td><td>13.4</td><td>15.2</td><td>15.9</td><td>17.0</td><td>16.5</td></tr><tr><td>MAD</td><td>0</td><td>1.76</td><td>2.52</td><td>3.60</td><td>3.04</td></tr><tr><td>MPD</td><td>0%</td><td>24.0%</td><td>28.3%</td><td>31.9%</td><td>36.9%</td></tr><tr><td colspan="6">Note: All numbers (except percentage) are in seconds</td></tr><tr><td></td><td>DBS0</td><td>DBS1</td><td>DBS2</td><td>DBS3</td><td>DBS4*</td></tr><tr><td>PER</td><td>35.0%</td><td>10.0%</td><td>7.0%</td><td>12.0%</td><td>12.0%</td></tr><tr><td>APT</td><td>24.2</td><td>20.3</td><td>23.3</td><td>18.9</td><td>18.3</td></tr><tr><td>MAD</td><td>10.8</td><td>6.91</td><td>9.88</td><td>5.47</td><td>4.83</td></tr><tr><td>MPD</td><td>75.0%</td><td>58.7%</td><td>82.3%</td><td>45.8%</td><td>56.1%</td></tr></table>

Table 6. Summary of Statistical Tests for Experiment I  
(a) Summary of ANOVA table with GLM procedure

<table><tr><td>Source</td><td>Degrees of freedom</td><td>Sum of squares</td><td>Mean square</td><td>F value</td><td>Pr &gt; F</td></tr><tr><td>Model</td><td>12</td><td>24005.48</td><td>2000.4567</td><td>9.29</td><td>&lt; 0.0001</td></tr><tr><td>Error</td><td>1,287</td><td>277279.55</td><td>215.4464</td><td></td><td></td></tr><tr><td>Corrected total</td><td>1,299</td><td>301285.03</td><td></td><td></td><td></td></tr><tr><td></td><td>R-square</td><td>Coefficient of variance</td><td>Root mean square error</td><td>Mean</td><td></td></tr><tr><td></td><td>0.079677</td><td>74.77378</td><td>14.67809</td><td>19.63000</td><td></td></tr></table>

(b) t-test: paired two sample for means

<table><tr><td></td><td>Inductive learning rules</td><td>Best assigned</td></tr><tr><td>Mean</td><td>15.180</td><td>13.420</td></tr><tr><td>Variance</td><td>105.745</td><td>100.327</td></tr><tr><td>t-statistic (p one-tail)</td><td>5.089 (&lt; 0.00001)</td><td></td></tr><tr><td></td><td>Best individual</td><td>Inductive learning rules</td></tr><tr><td>Mean</td><td>18.250</td><td>15.180</td></tr><tr><td>Variance</td><td>171.785</td><td>105.745</td></tr><tr><td>t-statistic (p one-tail)</td><td>4.113 (0.00004)</td><td></td></tr><tr><td></td><td>Worst individual</td><td>Best individual</td></tr><tr><td>Mean</td><td>28.930</td><td>18.250</td></tr><tr><td>Variance</td><td>329.823</td><td>171.785</td></tr><tr><td>t-statistic (p one-tail)</td><td>7.813 (&lt; 0.00001)</td><td></td></tr></table>

3. Using the rough rules identified in the preliminary analysis to assign queries correspondingly to four structures yields substantial improvement over assigning all queries to any one individual database structure.

Even without any data mining to intelligently assign queries to the corresponding efficient database structures, just running a flexible system with parallel structures is better than one single structure. However, the application of query mining, especially through inductive learning methods, provides superior performance.

## Experiment II

We worked with a larger and more sophisticated database environment for Experiment II, conducting the experiment with Oracle, the most popular commercially used database management system, in an attempt to replicate a real-world setting closely. Due to the complexity of the underlying application, we also investigated a much larger number of candidate database structures and more variations of query catego ries (types).

## Step 1—Design of Reference 3NF Database Structure DBS0

The database schema of the underlying application is portrayed in Figure 3 with the implementation details of the 3NF design presented in Table 7. We created a relational database with seven tables at 3NF. Each table has 10 to 40 attributes (fields). Each table has from 625 to 6,250 tuples (records). Values of numerical fields in tables were randomly generated within each field domain (data range). Contents of textual fields in tables are fixed sixteen-byte text.

We set the first field of each table as the primary key (for example, Field101 of Table1 and Field201 of Table2). Field216, Field406, Field605, and Field708 are foreign keys associated with Table1 and link with Field101. Field308 is a foreign key associated with Table2 and links with Field201. Field308 is a foreign key associated with Table2 and links with Field201. Field416 and Field705 are foreign keys associated with Table5 and link with Field501. All primary keys in tables were indexed as clustered and unique. All foreign keys were indexed as noncluster and nonunique.

## Step 2—Design of Read-Only Structures

By joining different original tables to make larger tables, we developed 96 different database structures (including the original normalized structure) with the same information content. These structures are named as DBS0-DBS95. For example, Table1 and Table2 are joined into Table12. Table12 has all fields from Table1 and Table2. Table12 also has indexes on any field that originally is a primary key or a foreign key of Table1 and Table2. Table12 along with original Table3, Table4, Table5, Table6, and Table7 is treated as one new database structure named DBS1. All possible 95 database structures (structures DBS1 through DBS95) were exhaustively and exclu sively constructed (again, in this study, we did not consider the possibility of materialized views, data marts, or joining partial tables together as one new relation).

Queries. We wrote a Visual Basic program to randomly generate 520 queries and designed the query generation process based on 52 possible input sources. The inpu source, as introduced in the previous section, specifies from which table(s) a quer retrieves data. In Experiment II, given its database layout of Figure 3, there are 52 possible input sources that are exhaustive. These are obtained from DBS0 (see Figure 3) by enumerating all tables that can be generated by joining one table at a time, two tables at a time, three tables at a time, and so on. We generated ten queries (SQL statements) for each possible input source.

![](/api/attachments/6U8F32HA/fulltext/images/ba7ca6eae0f3619495b247b1d302c1808840176062691feb29c5d2d1934b4012.jpg)  
Figure 3. Database Layout for Experiment II

Each query may have one to ten requested attributes and one to five selection criteria in an SQL statement. All requested attributes in a query are unique (that is, no duplicated attributes in a query). To complete the experiment in a reasonable length of time and not lose the general nature of a query, we used only the “AND” logic operator since the “OR” logic operator would extend query processing time much longer. For the same reason, we used only “>”, “<“, “>=”, “<=”, and “=” comparison operators since “<>” (not equal to) and other wild card operators (such as “like,” “\*”) would increase query processing time. The number of requested attributes in a query, number of criteria in a query, comparison operators in a query’s selection criteria, and values in selection criteria were all randomly generated by the Visual Basic program that we developed.

As noted above, we generated ten queries for each possible input source. We did not assign any textual attribute in selection criteria since these textual attributes al have fixed content and fixed length by design. Each query had 96 versions to be run against each alternate database structure. All queries were run on each of the 96 database structures.

Computing Environment. Eight Dell Dimension servers with Pentium II 233 MHz processors, 64MB of RAM, and the same hardware and software configurations were used. Each computer had exactly the same hardware and software setting. Oracle 8.0.4 package was used as the database management system.

<sub>aseSchemaofThirdNo</sub><sup>rmalFormDesignDetailsforE</sup>

<table><tr><td></td><td>Table1</td><td>Table2</td><td>Table3</td><td>Table4</td><td>Table5</td><td>Table6</td><td>Table7</td></tr><tr><td>Number of attributes</td><td>40</td><td>30</td><td>15</td><td>20</td><td>35</td><td>25</td><td>10</td></tr><tr><td>Number of tuples</td><td>625</td><td>2,500</td><td>6,250</td><td>3,750</td><td>1,250</td><td>1,875</td><td>5,000</td></tr><tr><td>Table size (reserved) (KB)</td><td>160</td><td>526</td><td>668</td><td>608</td><td>270</td><td>318</td><td>494</td></tr><tr><td>Data size (actual) (KB)</td><td>140</td><td>456</td><td>570</td><td>442</td><td>250</td><td>268</td><td>304</td></tr><tr><td>Index size (KB)</td><td>2</td><td>36</td><td>78</td><td>134</td><td>2</td><td>30</td><td>134</td></tr><tr><td>Construction time (seconds)</td><td>95</td><td>507</td><td>1,278</td><td>1,218</td><td>375</td><td>336</td><td>1,019</td></tr><tr><td>Number of links</td><td>4</td><td>2</td><td>1</td><td>2</td><td>2</td><td>1</td><td>2</td></tr><tr><td>Tables linked</td><td>2, 4, 6, 7</td><td>1, 3</td><td>2</td><td>1, 5</td><td>4, 7</td><td>1</td><td>1, 5</td></tr><tr><td colspan="8">Notes: Database size: 3,824,000 bytes reserved, 2,546,000 bytes as data, 466,000 bytes as indices.</td></tr></table>

## Step 3—Query Mining

The same query properties of Experiment I were used for Experiment II:

input source: 52 possible values;

selectivity factor: between 0 and 1, computed for each query;

size of the result tuple: computed for each query;

number of tables joined: between 1 and 7;

number of indexed fields in selection criteria: between 0 and 5; and

number of selection criteria: between 1 and 5.

Like Experiment I, C4.5 decision trees and production rules, as well as neural networks, were employed as learning tools. For training, 364 queries were used and 156 queries were used for validation. Due to space limitations we do not present the assign ment results here. The interested reader is welcome to obtain them from the authors.

## Step 5—Assignment of Queries to Structures

Performance measures of each assignment technique are presented in Table 8. Again we computed PER, APT, and MAD of best query processing time, and MPD from the best query processing time.

We again completed three mean comparison tests:

1. inductive learning production rule versus best assignment;

2. best individual structure versus inductive learning production rule; and

3. worst individual structure versus best individual structure.

In each case (see Table 9), we found significant differences. The results for comparisons (2) and (3) again were significant at very low p-values. Comparison (1), while still indicating a significant difference, was much closer than for our simpler first experiment. We conjecture that in more complex environments, the inductive learning production rule approach will provide even closer results to the theoretical and impractical best assignment method.

The query mining scenarios provide substantial efficiency improvements over the best overall structure, in terms of the percentage of queries that were processed with the shortest time. Gains in terms of the APT are observed for the inductive learning approaches, but not for the neural network method. Overall, the results of Experiment II confirm that using any single fixed database structure to process all varieties of queries yields poor performance and using inductive learning tools to assign different queries to corresponding efficient database structures outperforms assigning all queries to any one individual database structure. The results of Experiment II also confirm the choice of inductive learning production rules as the most favorable query mining technique that we studied.

<sub>arisonAmongDiferent</sub>M<sup>ethodsforProcessingQueries(E</sup>

<table><tr><td></td><td>Actual best assigned structures</td><td>Inductive learning production rules</td><td>Inductive learning decision tree</td><td>Neural network prediction</td><td>Best individual structure</td><td>Worst individual structure</td></tr><tr><td>PER</td><td>100%</td><td>58.5%</td><td>45.0%</td><td>47.5%</td><td>2.5%</td><td>0.8%</td></tr><tr><td>APT</td><td>1.6</td><td>2.0</td><td>2.3</td><td>5.3</td><td>2.7</td><td>751.5</td></tr><tr><td>MAD</td><td>0</td><td>0.48</td><td>0.75</td><td>3.48</td><td>1.10</td><td>749.90</td></tr><tr><td>MPD</td><td>0%</td><td>48.3%</td><td>75.0%</td><td>146.2%</td><td>110.4%</td><td>74,990.0%</td></tr><tr><td colspan="7">Note: All numbers (except percentage) are in seconds.</td></tr></table>

Table 9. Summary of Statistical Tests for Experiment II (t-test: paired two sample for means)

<table><tr><td></td><td>Inductive learning rules</td><td>Best assigned</td></tr><tr><td>Mean</td><td>2.032</td><td>1.550</td></tr><tr><td>Variance</td><td>79.992</td><td>29.931</td></tr><tr><td>t-statistic (p one-tail)</td><td>2.949 (0.00167)</td><td></td></tr><tr><td></td><td>Best individual</td><td>Inductive learning rules</td></tr><tr><td>Mean</td><td>2.654</td><td>2.032</td></tr><tr><td>Variance</td><td>88.314</td><td>79.992</td></tr><tr><td>t-statistic (p one-tail)</td><td>7.641 (&lt; 0.00001)</td><td></td></tr><tr><td></td><td>Worst individual</td><td>Best individual</td></tr><tr><td>Mean</td><td>751.450</td><td>2.654</td></tr><tr><td>Variance</td><td>2,515,105.945</td><td>88.314</td></tr><tr><td>t-statistic (p one-tail)</td><td>10.769 (&lt; 0.00001)</td><td></td></tr></table>

## Discussion of Experimental Results and Cost Considerations

IN THE EXPERIMENTS ABOVE WE INVESTIGATED the use of an FDS with alternative structures in parallel and used query mining techniques to determine the best assign ment of queries to structures. In comparison with using one single “best structure,” the gains in query processing time from using an FDS incorporating a query mining tool such as inductive learning with production rules were substantial.

In our analysis, the top benchmark was provided by considering the assignment of each incoming query to the structure that is most efficient at processing that query. This would, of course, require the continuous maintenance of all structures in addition to complete information on processing times for each query against each structure. As seen in the third section, our method outperforms the best individual structure. Similarly, our method, though certainly less costly than the assignment method, falls statistically significantly short of reaching the “best possible benchmark” provided by individual assignment of each and every arriving query. Our current efforts are directed at closing this gap by utilization of additional learning techniques beyond the three analyzed here and by considering maintenance of a small set of robust structures.

In analyzing the efficiency of the assignments, we consider the entire sets of queries in which each query is run once against the FDS. In other words, the results are for a scenario where all queries are treated equally. Ideally, in a real-world applica tion, we would work with the concept of query patterns in which some queries or query types are more frequent than others. Query mining becomes an ongoing effort to determine the assignments for the query patterns as they dynamically evolve. The identification of changes in the incoming patterns is key to the successful operation of the FDSs. This function is carried out by the Performance Monitor component illustrated in Figure 1.

## Cost Considerations

As the results of our proof of concept experiments demonstrate, considerable gains measured in time reduction in the query processing can be achieved by the FDS. However, as evidenced by the architecture described in the second section, the imple mentation of an FDS is complex in nature and there are several additional costs tha need to be evaluated, including:

1. storage costs for the additional read-only structures;

2. refresh costs for updating the read-only structures; and,

3. restructuring costs, when the system detects the changes in the query patterns are significant enough to warrant a restructuring operation.

Consider the FDS of Experiment I operating under inductive learning with produc tion rules. In a preliminary cost justification of the FDS, we present here a “back of envelope” mean value analysis, using the following parameters:

storage size of different database structures;

<table><tr><td>structure</td><td>DBS0</td><td>DBS1</td><td>DBS2</td><td>DBS3</td><td>DBS4</td><td>DBS5</td><td>DBS6</td><td>DBS7</td></tr><tr><td>size (MB)</td><td>17.862</td><td>21.442</td><td>19.832</td><td>19.342</td><td>21.312</td><td>39.992</td><td>22.922</td><td>46.592</td></tr></table>

period in consideration—1 day;

unit storage cost—\$0.01/(period ´ MB);

number of queries per period—1,000;

unit cost of query processing time—\$100/hour; and,

cost to update (refresh) structures—\$0.1/MB.

Without considering restructuring costs, since all eight structures will be concur rently active, we also assume the refresh operation takes place off line, taking the system one hour to complete. A comparison of costs of one day for the FDS, the system with only the DBS0 (the original 3NF structure), the system with only the DBS4 (the best structure), and the system with only the DBS5 (the worst structure) is provided in Table 10. For example, as shown in Table 10, the costs for the FDS is calculated as: query processing costs: 1,000 queries ´ 15.2 seconds ´ \$100 ¸ 3,600 seconds = \$422.22/day; data storage costs: 209.296 MB ´ \$0.01 = \$2.09/day; data refresh costs: 209.296 MB ´ \$0.1 = \$20.93/day; and, total costs: \$422.22 + \$2.09 + \$20.93 = \$445.24/day.

This analysis, albeit simple, indicates that substantial gains can be obtained by using the FDS approach in environments with a high intensity of read queries. Our two experiments show that using an FDS, an average 40 percent reduction in processing times can be realized. The sheer time value that is saved in processing thousands of read queries in, say, a day, can easily offset any additional storage or refresh costs in typical e-business environments where the read:write ratio can be as high as 1,000:1 (for every single update, there will be an average of 1,000 reads of the same item).

Table 10. A Comparison of Costs Incurred by Individual Database Structures with That of FDS (per day)

<table><tr><td></td><td>FDS</td><td>DBS0 only</td><td>DBS4 only</td><td>DBS5 only</td></tr><tr><td>Query processing costs</td><td>$422.22</td><td>$672.22</td><td>$508.33</td><td>$802.78</td></tr><tr><td>Data storage costs</td><td>$2.09</td><td>$0.18</td><td>$0.21</td><td>$0.40</td></tr><tr><td>Data refresh costs</td><td>$20.93</td><td>$1.79</td><td>$2.13</td><td>$4.00</td></tr><tr><td>Total costs</td><td>$445.24</td><td>$674.19</td><td>$510.67</td><td>$807.18</td></tr><tr><td>Savings from FDS</td><td></td><td>$228.95</td><td>$65.43</td><td>$361.94</td></tr></table>

It is important to notice that even greater savings can be obtained by proactively targeting specific query patterns that can be discovered by query mining. Our analy sis so far has focused on the overall set of possible queries, without aggregating them in groups or patterns.

Another critical source of processing time reduction in our approach is the fact tha queries can be processed in parallel by multiple structures, thus reducing the conges tion of the system. This aspect will be investigated in future research.

## Conclusion and Future Research

THE SOLUTION PRESENTED IN THIS PAPER centers on making available several intelligently designed read-only structures in parallel with the transaction-oriented, update intensive structure. The gist of our approach is to provide fast response to a wide variety of read-only requests. In current e-business information dissemination settings, the ratio of reads-to-writes can be as high as 1,000:1. We have shown in this paper that there is a tremendous opportunity to dramatically improve the read compo nent of databases in such environments.

We follow a seven-step process that entails the use of query mining and learning tools to search through queries to identify useful patterns and relationships among query properties, alternative database structures, and query processing time. Query mining outcomes are then used as a guide to restructure the database or assign queries to alternative database structures in pursuit of high-performing query processing. We use inductive learning and neural networks to demonstrate our methods and illustrate potential benefits from implementation.

Our goal has been to set forth the FDS design utilizing the query mining concept, to provide “proof of concept” experiment outcomes, and to detail initial procedures for implementation. Results of our two experiments (a basic system utilizing Access and a more complex system utilizing Oracle) suggest the potential gains from our approach and provide a set of counterintuitiveoutcomes that help emphasize the importance of careful database design. In each case we found that our method resulted in processing times that were statistically significantly lower than those obtained with the best performing individual structure. Initial cost calculations were provided to help illustrate the type of valuation process to determine the incremental cost of our method in a given application environment.

For applications of significant size, it is not practical to maintain all possible database structures. Our current research focuses on making our FDS approach imple mentable by operationalizing steps 4 and 7 of our method:

1. Development of an effective process for identifying an appropriate subset of database structures to maintain. The question to be addressed is: out of al possible available structures, what is the core set of structures that can provide good performance to queries across the board?

2. Development of a robust query categorization method, possibly using multi variate statistical clustering techniques using the input parameters identified in this study.

3. Development of the “restructuring” operation. The key issues here are the detection of changes in the query patterns. We believe we can extend query mining to address this. Another crucial issue is to develop an optimization mode [25], which will identify the points in time to restructure and will select the structure to be phased out and the new structures to become active.

It is worth noting that materialized views (the stored derived relations [data] from the results of previously posed queries) can be naturally integrated with our approach. Considering alternative database structures with materialized views is likely to provide a broader base to select good candidates for processing queries. Given that materialized views are especially beneficial to process queries in a distributed environment, we suggest a network environment extension of the techniques presented here. The learning tools for query mining would be used to identify query mixes and environment changes in order to reallocate data fragments, compose efficient materialized views, assign queries to be processed by the most suitable server, and restructure databases to maintain performance on query processing in a network environment. All these will require increased query property analysis and extensive experimentation, but the process follows the basic setup set out in this paper.

In addition to integrated environments of supply chain and CRM, an interesting application of FDSs is to the information market. An information provider is likely to find our approach a plus on its balance sheet if it

1. can reject queries with less likely benefits and process the queries with greater likely benefits (that is, improve its yield management);

2. can determine the optimal processing sequence for certain query mixes in order to optimize scheduling and lower costs; and

3. can determine the optimal update frequency in a database while meeting the requirement of customers’ requests for “real-time” information.

We began with a key, and yet rather simple observation: success in today’s dynamic business environment calls for the ability to rapidly adapt. The choice of a single database structure is against the grain of the “gains by adaptability” mantra. As in al business decisions, the key is selecting processes that maximize net return. We have detailed a method that incorporates the “rapidly adapt” principle so critical to success in today’s business world.

Acknowledgments: This research was partially supported by the Treibick Electronic Commerce Initiative, Department of Operations and Information Management, School of Business, Uni versity of Connecticut. The authors thank the referees, the associate editor, and the editor-inchief for valuable suggestions that considerably enhanced the quality of this paper.

## NOTES

1. See, for example, the discussion of Oracle’s solution at technet.oracle.com and Microsoft’s SQL Server solution at msdn.microsoft.com/library.

2. In this section we keep the C4.5 terminology of “production rules” to be consistent with the technique. In other parts of the paper we use the terms prediction rules and classification rules interchangeably.

## REFERENCES

1. Armstrong, R. Data warehousing: Dealing with the growing pains. In A. Gray and P.-A. Larson (eds.), Proceedings of Thirteenth International Conference on Data Engineering. Los Alamitos, CA: IEEE Computer Society Press, 1997, pp. 199–205.

2. Barquin, R., and Edelstein, H. (eds.). Planning and Designing the Data Warehouse Upper Saddle River, NJ: Prentice Hall, 1997.

3. Batra, D. A method for easing normalization of user views. Journal of Management Information Systems, 14, 1 (Summer 1997), 215–234.

4. Blaha, M. Data warehouses and decision support systems. Computer, 34, 12 (2001), 38–39.

5. Bonifati, A.; Cattaneo, F.; Ceri, S.; Fuggetta, A.; and Paraboschi, S. Designing data marts for data warehouses. ACM Transactions on Software Engineering and Methodology, 10, 4 (2001), 452–483.

6. Braunmuller, B.E.; Kriegel, M.; and Sander, H.P. Multiple similarity queries: A basic DBMS operation for mining in metric databases. IEEE Transaction on Knowledge and Data Engineering, 13, 1 (2000), 79–95.

7. California Scientific Software. BrainMaker User’s Guide and Reference Manual. Ne vada City, CA: California Scientific Software, 1993.

8. Chan, G.K.Y.; Li, Q.; and Feng, L. Design and selection of materialized views in a data warehousing environment: A case study. In I.-Y. Song and T.J. Thorey (eds.), Proceedings of the Second ACM International Workshop on Data Warehousing and OLAP. New York: ACM Press, 1999, pp. 42–47.

9. Chaudhuri, S., and Dayal, U. An overview of data warehousing and OLAP technology. SIGMOD Record, 26, 1 (1997), 65–74.

10. Chen, A. Improving database performance in a changing environment with uncertain and dynamic information demand: An intelligent database system approach. Ph.D. dissertation, University of Connecticut, Storrs, 1999.

11. Chen, A.; Goes, P.; Gupta, A.; and Marsden, J. Supporting timely managerial decisionmaking—Methods for selecting robust database structures with dynamic query patterns. Working paper, University of Connecticut, Storrs, 2000.

12. Chen, P.S.P. The entity-relationshipmodel—Toward a unified view of data. ACM Transactions on Database Systems, 1, 1 (1976), 9–36.

13. Date, C.J. The normal is so . . . interesting. Database Programming & Design, 10, 1 (1997), 23–25.

14. Dynamic Information Systems. Predictable versus un-predictable queries. Dynamic In formation Systems Corporation, Boulder, CO, 2001 (www.disc.com/predict.html).

15. Gardener, S.R. Building the data warehouse. Communications of the ACM, 41, 9 (1998), 52–60.

16. Goes, P.; Gopal, R.; and Chen, A.N.K. Query evaluation management design and prototype implementation. Decision Support Systems, 19, 1 (1997), 23–42.

17. Gray, J. (ed.). The Benchmark Handbook for Database and Transaction Processing Sys tems, 2d ed. San Mateo, CA: Morgan Kaufmann, 1993.

18. Huey, J. Discounting dynamo: Sam Walton. Time.com, Builders and Titans, 2002 (www.time.com/time/time100/builder/profile/walton.html).

19. Hyafil, L., and Rivest, R.L. Constructing optimal binary decision trees is NP-complete. Information Processing Letters, 5, 1 (1982), 15–17.

20. Inmon, W.H. What price normalization? Computerworld (October 1988), 27–31.

21. Inmon, W.H. Building the Data Warehouse, 3d ed. New York: Wiley and Sons, 2002.

22. Jarke, M., and Koch, J. Query optimization in database systems. ACM Computing Sur veys, 16, 2 (1984), 111–152.

23. Jarvelin, K. A methodology for user charge estimation in numeric online databanks, Par I. Journal of Information Science, 14, 1 (1988), 3–16.

24. Jarvelin, K. A methodology for user charge estimation in numeric online databanks, Part II. Journal of Information Science, 14, 1 (1988), 77–92.

25. Karlapalem, K.; Navathe, S.B.; and Ammar, M. Optimal redesign policies to support dynamic processing of applications on a distributed relational database system. Information Systems, 21, 4 (1996), 353–367.

26. Kim, C.N., and McLeod, R. Expert, linear models, and nonlinear models of expert deci sion making in bankruptcy prediction: A Lens model analysis. Journal of Management Infor mation Systems, 16, 1 (Summer 1999), 189–207.

27. Kimball, R., and Strehlo, K. Why decision support fails and how to fix it. SIGMOD Record, 24, 3 (1995), 92–97.

28. King, J.J. Query optimization by semantic reasoning. Ph.D. dissertation, Stanford University, 1981.

29. Kobryn, C. UML 2001: A standardization odyssey. Communications of the ACM, 42, 10 (1999), 29–37.

30. Kumar, A.; Van Der Aalst, W.; and Verbeek, E. Dynamic work distribution in workflow management systems: How to balance quality and performance.Journal of Management Infor mation Systems, 18, 3 (Winter 2001–2), 157–193.

31. Lee, C.; Shih, C.-S.; and Chen, Y.-H. Optimizing large join queries using a graph-based approach. IEEE Transaction on Knowledge and Data Engineering, 13, 2 (2001), 298–315.

32. Lee, H. Justifying database normalization: A cost/benefit model. Information Processing & Management, 31, 1 (1995), 59–67.

33. Meade, N. Neural network time series forecasting of financial markets. Internationa Journal of Forecasting, 11, 4 (1995), 601–602.

34. Mishra, P., and Eich, M.H. Join processing in relational databases. ACM Computing Surveys, 24, 1 (1992), 63–113.

35. Purao, S.; Jain, H.K.; and Nazareth, D.L. An approach to distribution of object-oriented applications in loosely coupled networks. Journal of Management Information Systems, 18, 3 (Winter 2001–2), 195–234.

36. Qian, X. Query folding. In S.Y.W. Su (ed.), Proceedings of the Twelfth Internationa Conference on Data Engineering. Los Alamitos, CA: IEEE Computer Society Press, 1996, pp. 48–55.

37. Qiu, S.G., and Ling, T.W. Index filtering and view materialization in ROLAP environment. In H. Paques, L. Liu, and D. Grossman, Proceedings of the Tenth International Conference on Information and Knowledge Management.New York: ACM Press, 2001, pp. 334–340.

38. Quinlan, J.R. Induction of decision trees. Machine Learning, 1, 1 (1986), 81–106.

39. Quinlan, J.R. Simplifying decision trees. International Journal of Man-Machine Stud ies, 27, 3 (1987), 221–234.

40. Quinlan, J.R. C4.5 Programs for Machine Learning.San Mateo, CA: Morgan Kaufmann, 1993.

41. Ruggieri, S. Efficient C4.5. IEEE Transaction on Knowledge and Data Engineering, 14, 2 (2002), 438–444.

42. Rundensteiner, E.A.; Koeller, A.; and Zhang, X. Maintaining data warehouses over chang ing information sources. Communications of the ACM, 43, 6 (2000), 57–62.

43. Shasha, D.E. Tuning databases for high performance. ACM Computing Surveys, 28, 1 (1996), 113–115.

44. Spangler, W.E.; May, J.H.; and Vargas, L.G. Choosing data-mining methods for multiple classification: Representational and performance measurement implications for decision sup port. Journal of Management Information Systems, 16, 1 (Summer 1999), 37–62.

45. Tillett, S., and Schwartz, J. Delta syncs data, ops. InternetWeek, June 22, 2001 (www.internetweek.com/newslead01/lead062201.htm)

46. Tombros, A., and van Rijsbergen, C.J. Query-sensitive similarity measures for the calculation of interdocument relationships. In H. Paques, L. Liu, and D. Grossman, Proceedings of the Tenth International Conference on Information and Knowledge Management. New York: ACM Press, 2001, pp. 17–24.

47. Walczak, S. Gaining competitive advantage for trading in emerging capital markets with neural networks. Journal of Management Information Systems, 16, 2 (Fall 1999), 177–200

48. Walczak, S. An empirical analysis of data requirements for financial forecasting with neural networks. Journal of Management Information Systems, 17, 4 (Spring 2001), 203–222.

49. Westerman, P. Data Warehousing: Using the Wal-Mart Model, 1st ed. San Francisco: Morgan Kaufmann, 2000.

50. Westland, J.C. Economic incentives for database normalization. Information Processing & Management, 28, 5 (1992), 647–662.

51. Zaharioudakis, M.; Cochrane, R.; Lapis, G.; Pirahesh, H.; and Urata, M. Answering complex SQL queries using automatic summary tables. SIGMOD Record, 29, 2 (2000), 105–116.

52. Zhang, C.; Yao, X.; and Yang, J. An evolutionary approach to materialized views selection in a data warehouse environment. IEEE Transactions on Systems, Man, and Cybernetics, 31, 3 (2001), 282–294.
