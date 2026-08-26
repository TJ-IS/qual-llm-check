---
otero_id: 20989
otero_key: "KGQNQX9T"
title: "The effects of information request ambiguity and construct incongruence on query development"
authors: "A.Faye Borthick; Paul L. Bowen; Donald R. Jones; Michael Hung Kam Tse"
year: "2001"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(01)00097-5"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# The effects of information request ambiguity and construct incongruence on query development

A. Faye Borthick <sup>a,)</sup>, Paul L. Bowen <sup>b,1</sup>, Donald R. Jones <sup>a,2</sup>, Michael Hung Kam Tse <sup>c,3</sup>

<sup>a</sup> School of Accountancy, Georgia State UniÕersity, POB 4050, Atlanta GA 30302-4050, USA

<sup>b</sup> Department of Commerce, The UniÕersity of Queensland, Brisbane, Queensland, 4072, Australia

<sup>c</sup> Corporate Finance, JP Morgan, Jardine House, 1 Connaught Place, Central, Hong Kong, China

## Abstract

This paper examines the effects of information request ambiguity and construct incongruence on end user’s ability to develop SQL queries with an interactive relational database query language. In this experiment, ambiguity in information requests adversely affected accuracy and efficiency. Incongruities among the information request, the query syntax, and the data representation adversely affected accuracy, efficiency, and confidence.

The results for ambiguity suggest that organizations might elicit better query development if end users were sensitized to the nature of ambiguities that could arise in their business contexts. End users could translate natural language queries into pseudo-SQL that could be examined for precision before the queries were developed. The results for incongruence suggest that better query development might ensue if semantic distances could be reduced by giving users data representations and database views that maximize construct congruence for the kinds of queries in typical domains. q 2001 Elsevier Science B.V. All rights reserved.

Keywords: Query development; Requirements ambiguity; Construct congruence; Web front end

## 1. Introduction

Even before Web front ends to legacy data on mainframes were created, managers and staff members were experiencing the need to retrieve and analyze data from various sources. They could not rely on IS professionals for ad hoc data retrieval and analysis because of the demands on IS professionals time for developing organizational systems. With Web front ends, however, data can be accessible to anyone with a Web browser 9,16 . In some organi-<sup>w</sup> <sup>x</sup> zations, young staff members, writing their own queries, are driving the business with their analyses <sup>w</sup> <sup>x</sup> 10 . Thus, in self-defense, managers and staff members are discovering that their competitiveness depends on their ability to develop database queries.

Web front ends may have made more data accessible and the actual querying easier, but perennial problems with database querying remain—the difficulties associated with understanding data structures from textual or graphical representations and mapping the meaning of a query into the interface language 4,5,18,30,32 . This research investigates the<sup>w</sup> <sup>x</sup> query development difficulties associated with varying semantic distance, i.e., the distance between the information users want and the expression in the query interface language that will produce that information 17 . The distance is manipulated in two <sup>w</sup> <sup>x</sup> ways: through the level of ambiguity of information requests and through the extent of congruence between constructs of the data representation and the interface language.

Potential benefits of this research include improved communication, e.g., between management and knowledge workers, and improved query support tools. Communication improvements might result from clearer statements of information requirements, more informed analysis of information requests, and greater use of divide and conquer strategies to ensure that information provided matches the information desired. Improved query support tools might entail enhancements to query front ends, e.g., to highlight potential ambiguities, and the creation of graphical data models and database views that facilitate typical queries by specific groups of end users.

This study extends prior research on end user query performance 4,5,18,30,32 . Prior research typ-<sup>w</sup> <sup>x</sup> ically compared different query languages or different forms of data representations. This research builds and tests a theory to explain why ambiguity and incongruence adversely affect end user query performance. Methodological improvements over prior studies include a more realistic business setting, direct interaction between experimental participants and the computerized information system, complete interactive capture of this interaction, and a detailed analysis of the errors made by participants.

## 2. Ambiguity and incongruence as impediments to query development

In general, because humans are limited information processors, more effective problem solving results when less cognitive effort is required 22 . In<sup>w</sup> <sup>x</sup> Norman’s 23,24 model of user query performance, <sup>w</sup> <sup>x</sup> users exert cognitive effort to bridge the semantic distance between their query objectives and the way they must specify these objectives to the information system. Thus, the cognitive effort required to formulate successful queries increases with increasing semantic distance 17 . Consistent with this model, <sup>w</sup> <sup>x</sup> empirical evidence indicates that information requests with shorter semantic distances require less cognitive effort and lead to better performance in terms of query correctness and query development time 2,30,32 . Two aspects that could affect seman-<sup>w</sup> <sup>x</sup> tic distance are the ambiguity of the information request and the congruence of the information request with the syntax of the query language and the data representation.

## 2.1. Model of the query process

Formulating a query requires transforming an information request into query components 19 . It <sup>w</sup> <sup>x</sup> requires knowledge in three domains: knowledge of the information needed, knowledge of the database structure, and knowledge of the query language 20 . <sup>w</sup> <sup>x</sup> Ineptness in one or more of these domains generates user errors 25 that produce erroneous information<sup>w</sup> <sup>x</sup> and lead to inappropriate decisions 8,27 .<sup>w</sup> <sup>x</sup>

Fig. 1 illustrates a conceptualization of how end users formulate queries. First, users identify required constructs by filtering out unnecessary components from and adding missing or implied components to the statement of the information request. Second, they examine the data representation to identify the tables and attributes needed to obtain the required constructs. These two processes result in a mental model of the information request in terms of the available data. Third, end users translate their mental models into the query language syntax required to satisfy their mental model of the information requirements.

![](/api/attachments/KGQNQX9T/fulltext/images/1d2a8349f8518b593e1872f9a8478abeea79fcb425afc182c24f40f0de92808c.jpg)  
Fig. 1. Model of end users’ query formulation processes.

Difficulties and errors result from discrepancies between the user’s mental model and the other representations, i.e., the information request, the data representation, and the query language syntax. These discrepancies can be conceptualized as semantic distances. The semantic distance between query objectives and correct queries has two aspects: the information requirement distance and the data representation distance. The information requirement distance denotes the gap between the statement of the information request and the operations operators Ž . available in the query language path 1 and 3 in Ž Ž . Ž . Fig. 1 . The data representation distance signifies the. gap between the data representation and the constructs operands required to formulate the appropri- Ž . ate query path 2 and 3 in Fig. 1 . GreaterŽ Ž . Ž . . cognitive effort is required when either semantic distance increases, and users may or may not be aware of mismatches between the information request and the query syntax and between the information request and the data representation.

## 2.2. Ambiguity of information requests

One problem in transforming a natural language request to an appropriate statement in the query language, i.e., of traversing the information requirement distance, is resolving the ambiguity of information requests 1,7,26,31 . Information requests that <sup>w</sup> <sup>x</sup> are ambiguous cause end users to be uncertain about the intent of the information request. This uncertainty, i.e., multiple possible desired outcomes of the information request, will lead to one-to-many mappings from words in the natural language to the syntax operators in the query language. That is, a Ž . natural language information request may have multiple interpretations such that several query statements may appear to be possible solutions. The existence of multiple possibilities is inherent in organizational situations, especially given that requests can come from external and internal stakeholders such as customers, suppliers, regulators, co-workers, and managers.

End users can reduce ambiguity of information requests by translating them into a less ambiguous form, i.e., performing a stepwise refinement of the information request. Because of the smaller semantic distances 23,24 , end users are likely to find it easier<sup>w</sup> <sup>x</sup> to resolve ambiguity in their own language than in a computer language. Consider, for example, the natural language information request for a transportation information system:

Manager-English: Management wants to know the routes that each truck is not permitted to travel.

or the same request in language that is closer to the syntax of the query language:

Pseudo-SQL: List all truck numbers and, where applicable, the route numbers where the truck violates height or weight constraints.

The manager-English version is the more ambiguous of the two statements because it could be mapped to several different pseudo-SQL statements 1,7,<sup>w</sup> 26,31 . To make the lexical transformations from<sup>x</sup> manager-English to pseudo-SQL 28 , users would <sup>w</sup> <sup>x</sup> need to understand the query in a business context in which trucks are not permitted to travel on routes for which they violate height or weight constraints. The existence of multiple interpretations increases the information load 3 , increasing the cognitive effort<sup>w</sup> <sup>x</sup> users must expend to develop a correct query. For this query, the manager-English request does not explicitly state that determining acceptable routes involves height or weight constraints or both. In this example, users of the manager-English request are more likely to make query errors of omission than users of the pseudo-SQL request.

Because the manager-English request acknowledges the existence of one or more categories of permissions that are required for a truck to travel a route, users must search their memory or consult some other source, e.g., a route table, to determine what the applicable constraints are. Then, if they want to compare their query with the manager-English request, users may create the list of constraints again. These search and compare processes take time, which would decrease a user’s efficiency compared to formulating the query for the pseudo-SQL version of the information request.

Because query accuracy, efficiency, and confidence are often related, it is common to assess them jointly 33 . Users working with the more ambiguous<sup>w</sup> <sup>x</sup> manager-English request may identify multiple interpretations of the information requested and of the applicable constraints. Hence, they are likely to be less confident in their queries than users of the pseudo-SQL request. The combined correctness, efficiency, and confidence effects are the first hypothesis:

H1. User query performance correctness, efficiency,Ž and confidence will be inversely related to the. ambiguity of information requests.

## 2.3. Incongruence

A second major problem in creating a query that correctly satisfies the information request is identifying the correct data elements, the ways they need to be related to each other, and the restrictions that need to be imposed on them. Successfully negotiating this data representation distance requires correctly mapping between real world constructs and their representation in the information system. The greater the mismatch between the real world constructs and their representation in the information system, the greater will be the cognitive effort that users will have to exert to construct a correct query and the more likely it will be that the queries contain errors.

For a specific query, if the real world constructs perfectly match their representation in the information system, there would be a one-to-one match between the two, i.e., the real world constructs and the information system would be construct congruent. Greater construct incongruence implies degraded Task-Technology-Fit 11 , which is associated with<sup>w</sup> <sup>x</sup> worse performance 12,34 . As construct incongru-<sup>w</sup> <sup>x</sup> ence increases, the complexity of a query also increases, which increases the time and cognitive effort required to develop a correct query.

With respect to queries, construct incongruence occurs when the representations in the information system must be reconstituted in some way before they can be incorporated into the query clauses that actually produce the desired result. For example, queries whose successful construction requires users to create temporary views, develop new relationships, or perform outer joins exhibit construct incongruence.

Database administrators typically strive to create data structures that minimize incongruence between the real world constructs and the database by making the data structures match the schemas of the predominate uses of the data. They are, however, constrained to only one physical representation of the database. Thus, construct incongruence may arise in connection with uses of the database that are infrequent or were not anticipated by the database administrator. Because the conditions that prompt new uses of existing data evolve over time in organizations, it is not realistic for the database administrator to be expected to anticipate all possible uses of the database.

Users confronted with construct incongruity are likely to detect cues that alert them to inadequately developed queries. Each time users compare the information request with a newly developed query is an occasion on which they could detect mismatches between the information request and the query syntax and between the information request and the data representation. To the extent this comparison process identifies query errors, users get confirmation that they have not developed a usable query, which ought to undermine their confidence in the correctness of their queries. Thus, user’s confidence in their queries should be inversely related to the degree of construct incongruence.

For example, consider two information requests. First, compare:

Pseudo-SQL: List the driver’s name and the trip number for trips where drivers were assigned trucks that violate the height constraint for the prescribed route.

with its corresponding query see the data structure Ž in Fig. 2 ,.

select surname, firstname, trip.trip\_no from driver, trip\_driver, trip, route, truck where driver.license\_no = trip\_driver.license\_no and

trip\_driver.trip\_no = trip.trip\_no and trip.route\_no = route.route\_no and trip.truck\_no = truck.truck\_no and height > height\_constraint;

![](/api/attachments/KGQNQX9T/fulltext/images/5f0097a67da6852eebda35231e5202e7a95d3fd8315a8fae80774f555110265c.jpg)  
Fig. 2. Entity-relationship diagram.

Second, compare:

Pseudo-SQL: List all truck numbers and, where applicable, the route numbers where the truck violates height constraints.

with its corresponding query see the data structure Ž in Fig. 2 ,.

create view truckviolation as select truck\_no, route\_no from route, truck where height > height\_constraint;

select truck.truck\_no, route\_no from truck, truckviolation where truck.truck\_no = truckviolation.truck\_no (+);

For the first information request, a relatively good task-technology fit exists between the information request, the entity-relationship diagram ERD , andŽ . the required query. For example, the first join of the query involves the tables driÕer and trip dri<sub>–</sub> Õer. On the ERD, these tables are adjacent to each other and the foreign key necessary for a natural join of the two tables, license no <sub>–</sub> , is readily apparent. Hence, end users can relatively easily derive the required join, driÕer.license no<sub>– – –</sub><sup>s</sup>trip driÕer.license no.

Conversely, the second information request does not exhibit a good task-technology fit between the information request, the ERD, and the required query. The query needs a new view, a Cartesian product, and an outer join, none of which are obvious from the ERD. End users must recognize that a view will facilitate obtaining the information requested. They must then determine what tables and attributes are required to construct the view truckÕiolation including the foreign key necessary to join the view with the truck table. This view is atypical in that it does not contain a join restriction but retains the full Cartesian product of the route and truck tables. Furthermore, to ensure that the query reports all trucks, a left outer join is required between truck and truckÕiolation. Hence, relative to the first information request, the second information request exhibits greater construct incongruence, which will require more cognitive effort to represent in the query, which is likely to lead to poorer end user query performance.

The combined effects of accuracy, efficiency, and confidence related to construct congruence comprise the second hypothesis:

H2. User query performance accuracy, efficiency, Ž and confidence will be inversely related to construct. incongruence.

## 2.4. Query complexity

The effects of task complexity have been studied extensively 3,35 . More complex tasks, e.g., more <sup>w</sup> <sup>x</sup> complex queries, place greater cognitive demands on persons undertaking the tasks and reduce their performance 3 . For computing tasks including queries, <sup>w</sup> <sup>x</sup> complexity is often measured using Halstead’s 15<sup>w</sup> <sup>x</sup> difficulty measure 18 . In this research, the measure<sup>w</sup> <sup>x</sup> is a function of the number of mental discriminations required to write a query. To confirm the expected relationship between performance as manifested by accuracy, efficiency, and confidence, the third hypothesis is:

![](/api/attachments/KGQNQX9T/fulltext/images/a641b3715a7153bb834b9c17a6d003ed3ca7c4b2f57f09356440c8c1c5c0c8d0.jpg)  
Fig. 3. Query performance model.

H3. User query performance accuracy, efficiency, Ž and confidence will be inversely related to query. complexity.

Fig. 3 summarizes the hypothesized relationships of ambiguity, incongruence, and query complexity with performance.

## 3. Method

## 3.1. Design

The hypotheses were tested in a two-factor within-subjects laboratory experiment in which participants composed and executed queries in Oracle SQL. The ambiguity factor had two levels: information requests posed in pseudo-SQL low ambiguityŽ . or manager-English high ambiguity . The congru-Ž . ence factor had two levels: information requests that were construct congruent or construct incongruent. The traditional approach to testing query performance has been with pencil and paper with or Ž without an intermediary to return results or simu-. lated systems that did not reveal results to participants 4,5,13,14,18,21,30,32 . As in Ref. 6 , the<sup>w</sup> <sup>x</sup> <sup>w x</sup> testing approach in this experiment incorporates a higher level of realism in that participants had the opportunity to work on their queries until they were satisfied with the query results from the database system.

## 3.2. Participants

Participants were 23 graduate business students enrolled in an information systems course. Five percent of their course grade was based on performance in the experiment. Before the experiment, participants received training in interpreting ERDs and formulating SQL queries. Because they were intelligent, had computing experience, and had training in query development, the participants were appropriate surrogates for casual users that are beginning to develop their own database queries. Table 1 summarizes demographic data for the two groups.

<table><tr><td colspan="3">Demographic data</td></tr><tr><td>Variable</td><td>Group 1</td><td>Group 2</td></tr><tr><td>Gender</td><td></td><td></td></tr><tr><td>Female</td><td>3</td><td>5</td></tr><tr><td>Male</td><td>9</td><td>6</td></tr><tr><td>Degree</td><td></td><td></td></tr><tr><td>Graduate information systems</td><td>11</td><td>11</td></tr><tr><td>Graduate business administration</td><td>1</td><td>0</td></tr><tr><td>GPA (7-point scale)</td><td></td><td></td></tr><tr><td>Mean</td><td>5.33</td><td>5.20</td></tr><tr><td>Standard deviation</td><td>1.0112</td><td>0.9970</td></tr></table>

Table 1

## 3.3. Procedure and Õariables

To ensure the equivalence of the two groups needed for the research design 29 , participants were <sup>w</sup> <sup>x</sup> divided into two equivalent groups based on a ranking of their information systems competence, which was determined by examining their information systems experience, education, and GPA. An information systems expert ranked the participants. The participant considered to have the most competence in information systems was ranked number 23, the person with the next most competence was ranked 22, etc. The participant with the highest ranking was assigned to group A, the participant with the next highest ranking, to group B, followed by B, A, A, B, B, etc. The groups were then randomly assigned to the two treatments.

At the beginning of the 2-h experimental session, participants received instructions, an ERD<sup>4</sup> representing the database Fig. 2 , and 16 information Ž . requests Appendix A shows the 10 informationŽ requests that participants completed, the responses to which are the basis for the analysis here to satisfy.

Table 2  
Experimental results: summary by information request

<table><tr><td rowspan="2">Variable</td><td colspan="4">Mean (standard deviation) by condition</td></tr><tr><td>Congruent/unambiguous</td><td>Congruent/ambiguous</td><td>Incongruent/unambiguous</td><td>Incongruent/ambiguous</td></tr><tr><td>Question 1</td><td>N = 11</td><td>N = 12</td><td>N = 0</td><td>N = 0</td></tr><tr><td>Complexity</td><td>5.7400 (0.0000)</td><td>5.7400 (0.0000)</td><td></td><td></td></tr><tr><td>Micro</td><td>0.0000 (0.0000)</td><td>1.0000 (2.3355)</td><td></td><td></td></tr><tr><td>Macro</td><td>0.0000 (0.0000)</td><td>0.16667 (0.3892)</td><td></td><td></td></tr><tr><td>Time</td><td>5.4545 (3.4165)</td><td>6.5833 (3.5022)</td><td></td><td></td></tr><tr><td>Attempts</td><td>1.3636 (0.6742)</td><td>2.1667 (1.7495)</td><td></td><td></td></tr><tr><td>Confidence</td><td>6.7273 (0.4671)</td><td>6.5833 (0.6686)</td><td></td><td></td></tr><tr><td>Question 2</td><td>N = 0</td><td>N = 0</td><td>N = 12</td><td>N = 11</td></tr><tr><td>Complexity</td><td></td><td></td><td>4.4700 (0.0000)</td><td>4.4700 (0.0000)</td></tr><tr><td>Micro</td><td></td><td></td><td>3.1667 (10.9695)</td><td>1.6364 (5.4272)</td></tr><tr><td>Macro</td><td></td><td></td><td>0.0833 (0.2887)</td><td>0.1818 (0.6030)</td></tr><tr><td>Time</td><td></td><td></td><td>6.5000 (7.5978)</td><td>7.0909 (7.0207)</td></tr><tr><td>Attempts</td><td></td><td></td><td>2.2500 (1.2881)</td><td>2.0909 (1.7003)</td></tr><tr><td>Confidence</td><td></td><td></td><td>6.5833 (0.6686)</td><td>6.0909 (1.2210)</td></tr><tr><td>Question 3</td><td>N = 12</td><td>N = 11</td><td>N = 0</td><td>N = 0</td></tr><tr><td>Complexity</td><td>10.0500 (0.0000)</td><td>10.0500 (0.0000)</td><td></td><td></td></tr><tr><td>Micro</td><td>1.0000 (3.4641)</td><td>0.8182 (1.9400)</td><td></td><td></td></tr><tr><td>Macro</td><td>0.0833 (0.2887)</td><td>0.1818 (0.4045)</td><td></td><td></td></tr><tr><td>Time</td><td>8.9167 (3.7528)</td><td>7.5455 (2.2962)</td><td></td><td></td></tr><tr><td>Attempts</td><td>2.2500 (1.2881)</td><td>2.1818 (1.4709)</td><td></td><td></td></tr><tr><td>Confidence</td><td>6.1667 (1.1146)</td><td>6.3636 (1.2060)</td><td></td><td></td></tr><tr><td>Question 4</td><td>N = 0</td><td>N = 0</td><td>N = 11</td><td>N = 11</td></tr><tr><td>Complexity</td><td></td><td></td><td>7.7400 (0.0000)</td><td>7.7400 (0.0000)</td></tr><tr><td>Micro</td><td></td><td></td><td>18.6364 (14.0519)</td><td>22.9091 (10.5305)</td></tr><tr><td>Macro</td><td></td><td></td><td>0.8182 (0.4045)</td><td>1.1818 (0.4045)</td></tr><tr><td>Time</td><td></td><td></td><td>13.9091 (9.4282)</td><td>11.0000 (5.4037)</td></tr><tr><td>Attempts</td><td></td><td></td><td>3.7273 (2.2843)</td><td>5.3636 (2.4606)</td></tr><tr><td>Confidence</td><td></td><td></td><td>5.1818 (1.6624)</td><td>4.8182 (2.5226)</td></tr><tr><td>Question 5</td><td>N = 10</td><td>N = 11</td><td>N = 0</td><td>N = 0</td></tr><tr><td>Complexity</td><td>18.5600 (0.0000)</td><td>18.5600 (0.0000)</td><td></td><td></td></tr><tr><td>Micro</td><td>2.7000 (4.3218)</td><td>11.3636 (9.7188)</td><td></td><td></td></tr><tr><td>Macro</td><td>0.5000 (0.7071)</td><td>1.5455 (0.9342)</td><td></td><td></td></tr><tr><td>Time</td><td>11.8000 (6.9570)</td><td>14.2727 (12.2400)</td><td></td><td></td></tr><tr><td>Attempts</td><td>4.4000 (2.4585)</td><td>7.1818 (4.5347)</td><td></td><td></td></tr><tr><td>Confidence</td><td>5.2000 (1.7512)</td><td>5.0909 (1.5136)</td><td></td><td></td></tr><tr><td>Question 6</td><td>N = 0</td><td>N = 0</td><td>N = 9</td><td>N = 11</td></tr><tr><td>Complexity</td><td></td><td></td><td>14.0000 (0.0000)</td><td>14.0000 (0.0000)</td></tr><tr><td>Micro</td><td></td><td></td><td>32.0000 (15.2561)</td><td>30.1818 (16.3757)</td></tr><tr><td>Macro</td><td></td><td></td><td>1.1111 (0.3333)</td><td>1.0909 (0.5394)</td></tr><tr><td>Time</td><td></td><td></td><td>10.8889 (6.6039)</td><td>12.1818 (9.0423)</td></tr><tr><td>Attempts</td><td></td><td></td><td>4.2222 (2.6822)</td><td>5.6364 (4.8015)</td></tr><tr><td>Confidence</td><td></td><td></td><td>3.6667 (2.2913)</td><td>5.1818 (1.7787)</td></tr><tr><td>Question 7</td><td>N = 8</td><td>N = 11</td><td>N = 0</td><td>N = 0</td></tr><tr><td>Complexity</td><td>21.5100 (0.0000)</td><td>21.5100 (0.0000)</td><td></td><td></td></tr><tr><td>Micro</td><td>1.0000 (2.8284)</td><td>0.7273 (2.4121)</td><td></td><td></td></tr><tr><td>Macro</td><td>0.2500 (0.7071)</td><td>0.0909 (0.3015)</td><td></td><td></td></tr><tr><td>Time</td><td>7.3750 (4.1726)</td><td>7.5455 (3.8565)</td><td></td><td></td></tr><tr><td>Question 7</td><td>N = 8</td><td>N = 11</td><td>N = 0</td><td>N = 0</td></tr><tr><td>Attempts</td><td>3.8750 (3.8336)</td><td>3.8182 (2.9939)</td><td></td><td></td></tr><tr><td>Confidence</td><td>5.5000 (1.6036)</td><td>5.7273 (1.4206)</td><td></td><td></td></tr><tr><td>Question 8</td><td>N = 0</td><td>N = 0</td><td>N = 11</td><td>N = 9</td></tr><tr><td>Complexity</td><td></td><td></td><td>16.5200 (0.0000)</td><td>16.5200 (0.0000)</td></tr><tr><td>Micro</td><td></td><td></td><td>8.9091 (9.8230)</td><td>10.5556 (19.1645)</td></tr><tr><td>Macro</td><td></td><td></td><td>0.8182 (0.4045)</td><td>1.3333 (0.5000)</td></tr><tr><td>Time</td><td></td><td></td><td>7.4545 (3.9080)</td><td>9.4444 (3.5395)</td></tr><tr><td>Attempts</td><td></td><td></td><td>9.4444 (3.0000)</td><td>5.8889 (3.8550)</td></tr><tr><td>Confidence</td><td></td><td></td><td>4.0000 (3.0000)</td><td>5.8889 (3.8550)</td></tr><tr><td>Question 9</td><td>N = 9</td><td>N = 7</td><td>5.7273 (1.2721)</td><td>4.3333 (2.5981)</td></tr><tr><td>Complexity</td><td>30.3700 (0.0000)</td><td>30.3700 (0.0000)</td><td>N = 0</td><td>N = 0</td></tr><tr><td>Micro</td><td>6.8889 (9.5975)</td><td>27.5714 (9.9307)</td><td></td><td></td></tr><tr><td>Macro</td><td>0.7778 (0.8333)</td><td>2.8571 (0.3780)</td><td></td><td></td></tr><tr><td>Time</td><td>11.2222 (4.2947)</td><td>11.4286 (3.9521)</td><td></td><td></td></tr><tr><td>Attempts</td><td>3.7778 (3.0732)</td><td>6.2857 (3.1472)</td><td></td><td></td></tr><tr><td>Confidence</td><td>5.4444 (1.3333)</td><td>4.5714 (2.0702)</td><td></td><td></td></tr><tr><td>Question 10</td><td>N = 0</td><td>N = 0</td><td>N = 7</td><td>N = 8</td></tr><tr><td>Complexity</td><td></td><td></td><td>22.5300 (0.0000)</td><td>22.5300 (0.0000)</td></tr><tr><td>Micro</td><td></td><td></td><td>34.1429 (17.4683)</td><td>40.8750 (23.2406)</td></tr><tr><td>Macro</td><td></td><td></td><td>1.1429 (0.3780)</td><td>(0.0000) (0.0000)</td></tr><tr><td>Time</td><td></td><td></td><td>13.7143 (6.7259)</td><td>10.3750 (3.5832)</td></tr><tr><td>Attempts</td><td></td><td></td><td>7.0000 (6.8069)</td><td>4.6250 (3.0208)</td></tr><tr><td>Confidence</td><td></td><td></td><td>4.2857 (2.5635)</td><td>5.1250 (1.6421)</td></tr></table>

with SQL queries. Odd-numbered requests had low construct congruence; even-numbered requests had high construct congruence. Each request had two versions: pseudo-SQL and manager-English. Each group received equal numbers of requests posed in each version, but for different requests, i.e., for each request, one group received the pseudo-SQL version and the other group, the manager-English version. After executing a query, participants were permitted to modify the query or move to the next query after indicating their level of confidence in the correctness of the query. All computer interactions and time stamps were recorded in log files.

Table 3  
Experimental results: summary by variable

<table><tr><td rowspan="3">Measurement</td><td colspan="4">Mean (standard deviation) by condition</td></tr><tr><td>N = 50</td><td>N = 52</td><td>N = 50</td><td>N = 50</td></tr><tr><td>Congruent/unambiguous</td><td>Congruent/ambiguous</td><td>Incongruent/unambiguous</td><td>Incongruent/ambiguous</td></tr><tr><td>Complexity</td><td>16.2950 (8.7427)</td><td>16.0152 (8.2891)</td><td>12.0842 (6.2541)</td><td>12.3446 (6.2797)</td></tr><tr><td>Micro</td><td>2.1800 (5.2980)</td><td>6.6731 (10.9754)</td><td>17.3600 (17.5415)</td><td>20.4800 (20.2154)</td></tr><tr><td>Macro</td><td>0.3000 (0.6145)</td><td>0.8077 (1.1209)</td><td>0.7400 (0.5272)</td><td>1.1000 (0.7354)</td></tr><tr><td>Time</td><td>8.9000 (5.0679)</td><td>9.2692 (6.8431)</td><td>10.1400 (7.5404)</td><td>10.0200 (6.3132)</td></tr><tr><td>Attempts</td><td>3.0200 (2.5674)</td><td>4.1346 (3.5260)</td><td>3.9800 (3.4905)</td><td>4.6800 (3.5135)</td></tr><tr><td>Confidence</td><td>5.8600 (1.3704)</td><td>5.7692 (1.5031)</td><td>5.2400 (1.9332)</td><td>5.1400 (2.0204)</td></tr></table>

![](/api/attachments/KGQNQX9T/fulltext/images/5627ecc4e1c49955793bc52f44e186e3fc16022e31a98f5bad98a534a8240d21.jpg)  
Fig. 4. Types of micro errors average and ambiguity. Ž .

Without knowledge of the identity of the participant or the version of the request the participant received, two researchers independently coded the accuracy of each query based on the last query Ž attempt by reference to standard query solutions and. resolved differences. Accuracy was assessed in two ways: in terms of the number of macro errors errors Ž involving row, column, and aggregation errors and . micro errors the count of the minimum number ofŽ changes required to transform an actual query into a correct query . Appendix B contains an example of . the accuracy coding for one information request. Efficiency was measured as the total time spent on a query and as the number of query attempts. Confidence was measured as participants’ self-report after each query.

A complexity measure for each query was calculated as Halstead’s 15 difficulty measure as illus-<sup>w</sup> <sup>x</sup> trated in Appendix C, and the information request pairs were arranged so that the difficulty of the congruent request of each pair was always equal to or greater than the difficulty of the incongruent request. The query performance data were analyzed in separate analysis of covariance ANCOVA mod-Ž . els for macro performance, micro performance, elapsed time, number of query attempts, and confidence. In each case, performance was analyzed as a function of ambiguity coded 0-1 as a nested com-Ž . ponent by request, incongruence coded 0-1 , andŽ . complexity covariate . Because of the 2-h time con-Ž . straint, few participants attempted information requests 11 to 16. All statistical analyses are based on the 202 responses to information requests one to ten. The information requests and model SQL queries are shown in Appendix A.

![](/api/attachments/KGQNQX9T/fulltext/images/44d741ae25612fabf755907374f0e5387c976f4555201a725c4fda7e0f1c82c9.jpg)  
Fig. 5. Micro errors by clauses average and ambiguity. Ž .

![](/api/attachments/KGQNQX9T/fulltext/images/8d840f48cb8443afd197745aeb52527ee8259fb90965b5402fbd16dc1fcdc823.jpg)  
Fig. 6. Types of micro errors average and incongruency. Ž .

## 4. Results

## 4.1. Summary statistics

Table 2 shows experimental results summarized by information request, and Table 3 summarizes the results by experimental variable. Table 3 verifies that the average complexity of the congruent information requests is higher than that of the incongruent information requests, i.e., that the information requests are biased against finding the hypothesized inverse relationship between incongruence and performance.

Average performance for accuracy micro and macro Ž errors shows noticeable degradation when informa-. tion requests are more ambiguous or incongruent. Average efficiency time and attempts and averageŽ . confidence measures, however, show only slight degradation as ambiguity and incongruence increase.

Figs. 4 and 6 display the types of micro errors made by participants for the different levels of ambiguity and incongruence, respectively. Figs. 5 and 7 present micro errors by clauses for the different levels of ambiguity and incongruence.

Fig. 4 shows that, except for Values and Set Operators, information requests formulated in manager-English, on average, resulted in more micro errors for each category. The difference in accuracy between manager-English and pseudo-SQL is especially pronounced for Symbol and Attribute errors. Fig. 5 reveals that information requests formulated in manager-English, on average, resulted in more micro errors for seven of eight different classes of SQL clauses. The difference between manager-English and pseudo-SQL is most evident for Select errors. The higher average number of Attribute and Select errors for manager-English formulations indicate that participants experienced difficulty in identifying what information was required from information requests that were more ambiguous. That is, the experimental participants experienced more difficulty identifying the correct columns than recognizing the appropriate row restrictions.

![](/api/attachments/KGQNQX9T/fulltext/images/e79136cf8e00d9bcff3c44d5c9d19c286a654a4b8a99636e7e48a01f182b8635.jpg)  
Fig. 7. Micro errors by clauses average and incongruency. Ž .

Fig. 6 illustrates the effects of incongruence on types of micro errors. The negative effects of incongruence on participants’ performance was especially pronounced for errors related to Attributes, Tables, Relational Operators, Symbols, and Keywords. Fig. 7 shows that queries with greater construct incongruence resulted in more errors for six of eight classes of SQL clauses. Performance differences were most evident for errors in the Where Condition, Where Join, From, and Select clauses.

## 4.2. Tests of hypotheses

Regression results appear in Table 4 and are summarized in Table 5. For H1, that accuracy, effi-

ANCOVA results for performance components  
Cells with ‘<sup>)</sup> ’ are ambiguity parameter estimates that are available from the authors by information request.

<table><tr><td>Source (n = 202)</td><td>df</td><td>Mean square</td><td>F value</td><td>p Value</td><td>Parameter estimate</td><td>Standard error of estimate</td><td> $R^2$ </td></tr><tr><td>Model: accuracy micro errors</td><td>12</td><td>2232.0830</td><td>15.55</td><td>0.0001</td><td></td><td></td><td>0.4967</td></tr><tr><td>Error</td><td>167</td><td>143.5789</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Intercept</td><td></td><td></td><td></td><td>0.0210</td><td>-7.0402</td><td>3.0992</td><td></td></tr><tr><td>Complexity</td><td>1</td><td>1812.7555</td><td>12.63</td><td>0.0005</td><td>0.5658</td><td>0.1592</td><td></td></tr><tr><td>Incongruence</td><td>1</td><td>7151.2602</td><td>49.81</td><td>0.0001</td><td>17.5626</td><td>2.4885</td><td></td></tr><tr><td>Ambiguity</td><td>10</td><td>874.6809</td><td>6.09</td><td>0.0001</td><td>*</td><td>*</td><td></td></tr><tr><td>Model: accuracy macro errors</td><td>12</td><td>7.5652</td><td>29.60</td><td>0.0001</td><td></td><td></td><td>0.6527</td></tr><tr><td>Error</td><td>167</td><td>0.25562</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Intercept</td><td></td><td></td><td></td><td>0.0210</td><td>-0.3043</td><td>0.1308</td><td></td></tr><tr><td>Complexity</td><td>1</td><td>7.7867</td><td>30.46</td><td>0.0001</td><td>0.0371</td><td>0.0067</td><td></td></tr><tr><td>Incongruence</td><td>1</td><td>8.2400</td><td>32.24</td><td>0.0001</td><td>0.5962</td><td>0.1050</td><td></td></tr><tr><td>Ambiguity</td><td>10</td><td>4.3835</td><td>17.15</td><td>0.0001</td><td>*</td><td>*</td><td></td></tr><tr><td>Model: efficiency time</td><td>12</td><td>70.5968</td><td>1.76</td><td>0.0580</td><td></td><td></td><td>0.1004</td></tr><tr><td>Error</td><td>167</td><td>40.1697</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Intercept</td><td></td><td></td><td></td><td>0.0003</td><td>6.0487</td><td>1.6393</td><td></td></tr><tr><td>Complexity</td><td>1</td><td>173.3585</td><td>4.32</td><td>0.0391</td><td>0.1750</td><td>0.0842</td><td></td></tr><tr><td>Incongruence</td><td>1</td><td>90.6014</td><td>2.26</td><td>0.1348</td><td>1.9768</td><td>1.3163</td><td></td></tr><tr><td>Ambiguity</td><td>10</td><td>46.0172</td><td>1.15</td><td>0.3305</td><td>*</td><td>*</td><td></td></tr><tr><td>Model: efficiency number of attempts</td><td>12</td><td>42.7901</td><td>4.71</td><td>0.0001</td><td></td><td></td><td>0.2302</td></tr><tr><td>Error</td><td>167</td><td>9.0853</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Intercept</td><td></td><td></td><td></td><td>0.3762</td><td>0.6915</td><td>0.7796</td><td></td></tr><tr><td>Complexity</td><td>1</td><td>115.6110</td><td>12.73</td><td>0.0005</td><td>0.1429</td><td>0.0401</td><td></td></tr><tr><td>Incongruence</td><td>1</td><td>56.5460</td><td>6.22</td><td>0.0135</td><td>1.5617</td><td>0.6260</td><td></td></tr><tr><td>Ambiguity</td><td>10</td><td>22.3305</td><td>2.46</td><td>0.0088</td><td>*</td><td>*</td><td></td></tr><tr><td>Model: confidence</td><td>12</td><td>7.6835</td><td>2.80</td><td>0.0015</td><td></td><td></td><td>0.1510</td></tr><tr><td>Error</td><td>167</td><td>2.7423</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Intercept</td><td></td><td></td><td></td><td>0.0001</td><td>7.0094</td><td>0.4283</td><td></td></tr><tr><td>Complexity</td><td>1</td><td>28.1709</td><td>10.27</td><td>0.0016</td><td>-0.0705</td><td>0.0220</td><td></td></tr><tr><td>Incongruence</td><td>1</td><td>19.4967</td><td>7.11</td><td>0.0083</td><td>-0.9170</td><td>0.3439</td><td></td></tr><tr><td>Ambiguity</td><td>10</td><td>1.8109</td><td>0.66</td><td>0.7601</td><td>*</td><td>*</td><td></td></tr></table>

Table 5 ANCOVA results summary

<table><tr><td rowspan="2">Measurement</td><td colspan="3">Results consistent with hypotheses</td></tr><tr><td>H1: Ambiguity</td><td>H2: Incongruence</td><td>H3: Confidence</td></tr><tr><td colspan="4">Accuracy</td></tr><tr><td>Micro errors</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Macro errors</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td colspan="4">Efficiency</td></tr><tr><td>Time</td><td>No</td><td>No</td><td>Yes</td></tr><tr><td>Number of attempts</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Confidence</td><td>No</td><td>Yes</td><td>Yes</td></tr></table>

ciency, and confidence are inversely related to the ambiguity of information requests, the results support the hypothesis for accuracy as measured by micro and macro errors and for efficiency as measured by the number of attempts. Confidence was not significantly associated with ambiguity.

For H2, that accuracy, efficiency, and confidence are inversely related to construct congruence, the results support the hypothesis for accuracy as assessed by micro and macro errors, for efficiency as assessed by the number of attempts, and for confidence. Eventhough efficiency, as measured by the number of attempts, was significant for both hypotheses, elapsed time was not significant for either one. This suggests that elapsed time may be driven by factors that are independent of a user’s ability to formulate correct queries. As expected, H3, that query performance will be inversely related to query complexity, was supported by all measures of accuracy, efficiency, and confidence.

## 5. Discussion

The results of this study support the idea that the interaction among information requests, the query language, and the data representation affect individuals’ ability to formulate correct queries. Specifically, ambiguity in information requests adversely affects accuracy and efficiency. Incongruence among the information request, the query syntax, and the data representation adversely affects accuracy, efficiency, and confidence. Because these effects are in addition to the complexity effect, it may be appropriate to include ambiguity and incongruence as well as complexity in future research on improving query development.

## 5.1. Implications arising from ambiguity results

The results for ambiguity suggest that organizations might elicit better query development from casual users if they were sensitized to the nature of the kind of ambiguities that could arise in their business contexts and were trained to translate natural language queries into pseudo-SQL that could be examined for precision before the queries were developed. For example, database professionals and users together could identify archetype ambiguities inherent in specific user’s queries. Once sensitized to specific ambiguities, users could clarify the meanings of the information requests.

From Fig. 4, ambiguity is associated with errors in attributes, keywords, and, to a lesser extent, relational operators and tables. From Fig. 5, ambiguity is associated with errors in select, where condition, group by, and having clauses. Using currently available tools and techniques, organizations can take a number of steps to reduce these ambiguity-induced errors. For example, the user responsible for formulating a query could focus on more clearly identifying the attributes and columns needed to satisfy the request and on the conditions the data must satisfy. Users could work on improving their communications with the people making the information requests and following a more structured stepwise refinement process when converting the information requests to SQL queries. Users could develop pseudo-SQL representations of the information request and discuss that intermediate formulation with the information requestor.

Database owners could improve the data dictionary to enhance definitions and descriptions of both tables and attributes within the tables. Organizations could train users responsible for formulating queries to be more conscientious and insightful when developing queries. For example, information requestors typically want to see the values of the attributes used in the restrictions even if they do not explicitly identify them when stating the attributes they want. Organizations could also cross train their employees. That is, given the importance to most organizations of exploiting their information system resources, information requestors need to improve their understanding of the data stored in their organization’s information systems, and information providers per-Ž sons responsible for formulating the queries need to. improve their understanding of the organization.

Using specification languages such as VDM, $Z ,$ and B could help reduce ambiguity between information system analysts and programmers. To informa tion requestors, however, these languages are likely to be even less understandable than query languages such as SQL and QBE. Future research could develop and test a specification language to facilitate clearer communications between information requestors and information providers.

## 5.2. Implications arising from incongruence results

The results for incongruence suggest that better query development might ensue if semantic distances could be reduced by giving users data representations and database views that maximize construct congruence for the kinds of queries in their domains. For example based on the ERD in Fig. 2 , users thatŽ . often developed queries requiring the Driver and Client tables to be joined on PostCode question 2 as Ž explained in Appendix A could be given a view. with that join.

From Figs. 6 and 7, incongruence is associated with substantial increases in errors for almost all types and almost all clauses. The typical way of viewing the data structure and its relationships, e.g., via an ERD, creates and reinforces a powerful mental model of an information system. This mental model acts as an anchor that can inhibit an information provider from formulating a query that correctly satisfies the information request. In addition to the improvements recommended to reduce problems arising from ambiguity, organizations could develop or encourage their database management system provider to develop an adaptive data structure interface, e.g., an adaptive ERD interface.

There are several ways that using an adaptive ERD interface might promote improved query performance. For example, ERDs could be tailored to the requirements of specific groups of users. In such settings, users would rarely need to perform joins in their queries, which would make them less complex and thus less error prone.

Because it is not possible to anticipate every information need in advance, tailored ERDs would not be feasible in every situation. Instead, an adaptive interface could show or list the tables comprising an information system rather than displaying an ERD with the typical relationships and foreign keys. Individual tables could be expanded to display their attributes or be designated as part of the subsystem necessary to satisfy the information request. After selecting the tables deemed relevant to the information request, users could then specify the foreign keys between those tables. If the underlying database management system provided domain support, the adaptive interface could inform users of possible foreign keys and issue warnings about attempts to use foreign keys with incompatible domains.

Formulating queries in any query interface would be facilitated by consistent naming practices, i.e., using the same name for the same attribute in different tables and avoiding using the same name for attributes that are actually different. An even better practice would be to use a data dictionary to resolve such inconsistencies.

Future research could investigate the desirable characteristics of a knowledge-based interface that assists users in formulating queries. Such an interface might request a natural language formulation of the information request, help users build their queries, warn users of likely errors, check the queries against natural language formulations for completeness, and suggest ways to enhance queries.

## Acknowledgements

The authors are indebted to Jon Heales, Ron Weber, program committee members and participants at The Pacific Asia Conference on Information Systems 2000, and anonymous reviewers for helpful comments.

## Appendix A. Information requests and model SQL queries

1. Congruent; Halstead Difficulty<sup>s</sup>6.06

1m. Management wants the names of personal clients and their credit limits. 1p. List client names and credit limits where the clients are personal clients.

surname, firstname, credit limit

select surname, firstname, credit\_limit from client, personal\_client where client.client\_no = personal\_client.client\_no;

## 2. Incongruent Ž . missing relationship ; Halstead Difficulty<sup>s</sup> 5.25

2m. Management wants to know the names of drivers with the same post code as clients. 2p. List names of drivers where the post code of the driver is the same as the post code of a client.

surname, firstname

select surname, firstname

from driver, client

where driver.postcode = client.postcode;

The incongruence in question 2 is the missing direct relationship between the two tables in the join. The typical congruent relationship between tables is illustrated in question 1, i.e., in Fig. 2, the Client andŽ . Personal Client tables are adjacent with the obvious foreign key of Client No. In contrast, the two tables in question 2 are not adjacent. In fact, the minimum path between the Driver and Client tables involves a minimum of three intermediate tables. Furthermore, because the attribute Postcode is not the primary key of either table, the foreign key between the Driver and Client tables is more difficult to determine than for question 1, where Client No is the primary key for both of the tables involved in the join.<sub>–</sub>

## 3. Congruent Ž . aggregation ; Halstead Difficulty<sup>s</sup>10.25

3m. Management wants the names of bill-to clients who are persons and their total delivery charges. Clients with larger charges should be listed first.

3p. List the client numbers of bill-to clients who are persons and their total delivery charges with clients having larger charges listed first.

## surname, firstname, sum(deliver charges)

select surname, firstname, sum(deliver\_charges) from personal\_client, bill\_of\_lading where personal\_client.client\_no = bill\_of\_lading.bill\_client\_no group by surname, firstname order by 3 desc;

4. Incongruent Ž . subquery, cartesian product, or, negation, missing relationship ; Halstead Difficulty<sup>s</sup>8.27 4m. Management wants to know the trucks that can travel all routes.

4p. List the truck numbers of trucks where the truck does not exceed either the height or weight constraints for any route.

truck no

select truck\_no from truck where truck\_no not in (select truck\_no from route, truck where (height > height\_constraint or empty\_weight > weight\_constraint));

The incongruencies in question 4 are subquery, Cartesian product, negation, and missing relationship. Although the query for question 4 does not involve identifying a foreign key, the effects of a missing relationship were examined in the discussion of question 2. Contrast the query for question 4 with the query for question 7. While the query for question 7 involves more tables and several joins, it involves adjacent tables, positive relationships, and natural joins. All conditions address restrictions on a single collection of data. The query for question 4, however, involves two collections of data, i.e., one collection for the primary query and another collection for the subquery. The join in the subquery remains a Cartesian product rather than a more typical natural join. Cartesian products are especially difficult to conceptualize because they require matching each and every record in one table with each and every record in a second table. Cartesian products typically produce an extremely large number of records. Furthermore, many people find negative logic, e.g., not in, more difficult, i.e., less congruent with the way they normally think than positive logic.

## 5. Congruent Ž . aggregation ; Halstead Difficulty<sup>s</sup>19.35

5m. Management wants to know the names of clients who are persons that are over their credit limit.

5p. List the names of clients who are persons where the sum of their unpaid delivery charges exceeds their credit limit.

## surname, firstname, credit limit, sum(deliver charges)

select surname, firstname, credit\_limit, sum(deliver\_charges)

from personal\_client, bill\_of\_lading, client

where client.client\_no = bill\_of\_lading.bill\_client\_no and

client.client\_no = personal\_client.client\_no and date\_paid is null

group by surname, firstname, credit\_limit

having sum(deliver\_charges) > credit\_limit;

6. Incongruent Ž . missing relationships, cartesian product, outer join ; Halstead Difficulty<sup>s</sup> 16.36

6m. Management wants to know all trucks and the routes that each truck is not permitted to travel.

6p. List all truck numbers and where applicable the route numbers where the truck violates height or weight constraints.

truck no, route no

create view truckviolation as

select truck\_no, route\_no

from route, truck

where (height > height\_constraint or

empty\_weight > weight\_constraint);

select truck.truck\_no, route\_no

from truck, truckviolation

where truck.truck\_no = truckviolation.truck\_no (+);

The incongruencies in question 6 are Cartesian product, missing relationship, view, and outer join. The effects of a missing relationship were examined in the discussion of question 2. The effects of a Cartesian product were examined in the discussion of question 4. A view produces at least two mental incongruencies. First, like the subquery examined in question 4, views create an additional collection of data. Second, the user has to mentally add the view to the ERD and determine the foreign keys to the adjacent tables. Outer joins, while not as mentally incongruent as Cartesian products, require more cognitive effort than natural joins. Users must determine which table contains the data that must be retained and which table may not contain tuples that match tuples in the first table.

## 7. Congruent; Halstead Difficulty<sup>s</sup>21.13

7m. Management wants to know the names of drivers and the trip numbers where the truck exceeded the height constraint.

7p. List the driver’s name and the trip numbers where the truck’s height exceeded the height constraint for that route.

surname, firstname, trip no

select surname, firstname, trip.trip\_no

from route, trip, truck, trip\_driver, driver

where trip.trip\_no = trip\_driver.trip\_no and

trip\_driver.license\_no = driver.license\_no and

trip.truck\_no = truck.truck\_no and

trip.route\_no = route.route\_no and

height > height\_constraint;

8. Incongruent Ž . outer join, missing relationship, aggregation ; Halstead Difficulty<sup>s</sup>16.88

8m. Management wants to know all the destinations and their city and state and the number of clients atŽ . each of the destinations.

8p. For all destinations same city and state , list the destination number, city, state, and total number ofŽ . clients at that city and state.

```sql
select trip.trip_no, trip.truck_no, legal_max_weight, empty_weight,
    sum(unit_weight * qty) + empty_weight
from bill_of_lading, trip, truck, cargo_item
where trip.truck_no = truck.truck_no and
    trip.trip_no = bill_of_lading.trip_no and
    bill_of_lading.bol_no = cargo_item.bol_no
group by trip.trip_no, trip.truck_no, legal_max_weight, empty_weight
having sum(unit_weight * qty) + empty_weight > legal_max_weight;
```

destination no, city, state, count(client no)

select destination\_no, destination.city, destination.state, count(client\_no) from destination, client where destination.city = client.city (+) and destination.state = client.state (+) group by destination\_no, destination.city, destination.state;

The incongruencies in question 6 are missing relationship and outer join. The effects of a missing relationship were examined in the discussion of question 2. The effects of an outer join were examined in the discussion of question 6. The outer join in question 8 is even more incongruent than question 6 because of the concatenated foreign key between Destination and Client. Because of the concatenated foreign key, two outer joins are required.

## 9. Congruent Ž . aggregation, aggregation restriction ; Halstead Difficulty<sup>s</sup>30.37

9m. Management wants to know the trip number, truck number, and maximum and minimum weight of the trucks for the trips where the trucks weighed more than their legal maximum weight.

9p. List the trip number, truck number, and the maximum and minimum weight of trucks for the trips where the cargo weight plus the truck’s empty weight exceeds its legal maximum weight.

trip no, truck no, legal max weight, empty weight. sum(unit weight \* qty) + empty weight

10. Incongruent Ž . view, missing relationship, cartesian product, outer join ; Halstead Difficulty<sup>s</sup> 23.19

10m. Management wants to know all drivers and the trucks that each driver is licensed to drive as of 8 Sept 1998.

10p. Assume today is 8 Sept 1998. For all drivers, list license number, driver name, and truck number where the driver’s license meets or exceeds the requirements for the truck and the license has not expired.

license no, surname, firstname, truck no

create view legaltruck as

select license\_no, truck\_no

select driver.license\_no, surname, firstname, truck\_no

from driver, legaltruck

where driver.license\_no = legaltruck.license\_no (+);

The incongruencies in question 10 are Cartesian product, missing relationship, view, and outer join, which have been examined in the discussions of previous questions.

## Appendix B. Example of error marking for accuracy in queries

Information request 3: Management wants the names of bill-to clients who are persons and their total delivery charges. Clients with larger charges should be listed first.

Correct solution:

select surname, firstname, sum(deliver\_charges) from personal\_client, bill\_of\_lading where bill\_of\_lading.bill\_client\_no = personal\_client.client\_no group by surname, firstname order by 3 desc;

Sample actual solution:

select surname, sum(deliver\_charges) from bill\_of\_lading, personal\_client where bill\_of\_lading.deliver\_client\_no = personal\_client.client\_no group by surname;

The semantic errors in the response are:

v Missing the attribute firstname in the select clause: this error is recorded at the micro level as one A Attributes Select B error and one A Symbols Select B error for the extra A,B that is required. At the macro level, this error is recorded as a A ColumnsB error.

v Incorrect join the between bill of lading and the personal client tables: at the micro level, to make the query correct requires the following elements to be deleted and inserted: delete .deliÕer client no<sub>– –</sub> , which is one A Symbols Where JoinB error and one A Attributes Where JoinB error; and insert .bill client no<sub>– –</sub> , which is one A Symbols Where JoinA error and one A Attributes Where JoinB error. At the macro level, this is error is recorded as a A RowsB error because an incorrect join affects the rows that are retrieved by the query.

v Missing the attribute firstname in the group by clause: this error is recorded at the micro level as one A Attribute Group byB error and one A Symbols Group byB error for the extra A,B that is required. At the macro level, this in not a macro error because this error originated from the error in the select clause.

v Missing the order by statement: at the micro level, to make the query correct requires the following elements to be inserted: order by 3 desc, which is two A Keyboards Order byB errors and one A Attribute Order byB error. At the macro level, this error is recorded as a A RowsB error because the order of the data retrieved by the query is affected.

Performance, in terms of accuracy, was measured by the total number of micro errors and the total number of macro errors. This example had 11 micro errors and 2 macro errors. The following error counting sheet contains the micro errors and the macro errors for this example query.

<table><tr><td colspan="3">Error Counting Sheet</td></tr><tr><td>Name</td><td>Information Request Number</td><td>Attempts</td></tr><tr><td></td><td></td><td></td></tr></table>

## MICRO ERRORS

Keyboards

<table><tr><td>View</td><td>Select</td><td>From</td><td>Where Join</td><td>Where Cond</td><td>Group by</td><td>Having</td><td>Order by</td></tr><tr><td></td><td>1</td><td></td><td></td><td></td><td></td><td></td><td>2</td></tr></table>

Symbols

<table><tr><td>View</td><td>Select</td><td>From</td><td>Where Join</td><td>Where Cond</td><td>Group by</td><td>Having</td><td>Order by</td></tr><tr><td></td><td>1</td><td></td><td>2</td><td></td><td>1</td><td></td><td></td></tr></table>

Logical Operators

<table><tr><td>View</td><td>Select</td><td>From</td><td>Where Join</td><td>Where Cond</td><td>Group by</td><td>Having</td><td>Order by</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Relational Operators

<table><tr><td>View</td><td>Select</td><td>From</td><td>Where Join</td><td>Where Cond</td><td>Group by</td><td>Having</td><td>Order by</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Tables

<table><tr><td>View</td><td>Select</td><td>From</td><td>Where Join</td><td>Where Cond</td><td>Group by</td><td>Having</td><td>Order by</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Attributes

<table><tr><td>View</td><td>Select</td><td>From</td><td>Where Join</td><td>Where Cond</td><td>Group by</td><td>Having</td><td>Order by</td></tr><tr><td></td><td></td><td></td><td>2</td><td></td><td>1</td><td></td><td>1</td></tr></table>

Values

<table><tr><td>View</td><td>Select</td><td>From</td><td>Where Join</td><td>Where Cond</td><td>Group by</td><td>Having</td><td>Order by</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Set Operators

<table><tr><td>Where</td><td>Union</td><td>Intersect</td><td>Minus</td></tr><tr><td></td><td></td><td></td><td></td></tr></table>

MACRO ERRORS

<table><tr><td>Columns</td><td>Rows</td><td>Aggregation</td></tr><tr><td>1</td><td>1</td><td></td></tr></table>

## Appendix C. Example calculation of Halstead complexity measure

Halstead’s 15 difficulty measure was chosen as the complexity measure for this research. The formula is: <sup>w</sup> <sup>x</sup>

$$
D = V / V ^ {*} = \left(N \log_ {2} n\right) / \left(n ^ {*} \log_ {2} n ^ {*}\right)
$$

where: $N = \mathrm { p r o g r a m }$ length $= N _ { 1 } + N _ { 2 } ; \ N _ { 1 } =$ total operators; $N _ { 2 } = \mathrm { t o t a l }$ operands; n<sup>s</sup>vocabulary si $\begin{array} { r } { z \mathrm { e } = n _ { 1 } ~ . } \end{array}$ q $n _ { 2 } ; n _ { 1 } = \mathrm { u n i q u e }$ operator count; $n _ { 2 } = \mathrm { u n i q u e }$ operand count; $n ^ { * } =$ Ž . potential minimum vocabulary $= n _ { 1 } ^ { * } + n _ { 2 } ^ { * }$ ; $n _ { 1 } ^ { * } =$ Ž . potential minimum operator count; $n _ { 2 } ^ { \mathrm { * } } = \mathrm { p o t e n t i a l }$ minimum operand count.Ž .

For any SQL query, $n ^ { * }$ , the potential minimum vocabulary is always 5 because the minimum query is: Ž .

Select <sup>)</sup> From table;

The solution to information request 3 is:

Select surname, firstname, sum(deliver\_charges) From personal\_client, bill\_of\_lading Where personel\_client.client\_no = bill\_of\_lading.client\_no Group by surname, firstname Order by 3 desc;

<table><tr><td>Operators</td><td>Count</td><td>Operands</td><td>Count</td></tr><tr><td>Select</td><td>1</td><td>surname</td><td>2</td></tr><tr><td>, (comma)</td><td>4</td><td>firstname</td><td>2</td></tr><tr><td>sum</td><td>1</td><td>deliver_charges</td><td>1</td></tr><tr><td>()</td><td>1</td><td>personal_client</td><td>2</td></tr><tr><td>From</td><td>1</td><td>bill_of_lading</td><td>2</td></tr><tr><td>Where</td><td>1</td><td>client_no</td><td>2</td></tr><tr><td>. (period)</td><td>2</td><td>3</td><td>1</td></tr><tr><td>= (equal sign)</td><td>1</td><td></td><td></td></tr><tr><td>Group by</td><td>1</td><td></td><td></td></tr><tr><td>Order by</td><td>1</td><td></td><td></td></tr><tr><td>desc</td><td>1</td><td></td><td></td></tr><tr><td>; (semicolon)</td><td>1</td><td></td><td></td></tr><tr><td> $n_1 = 12$ </td><td></td><td> $n_2 = 7$ </td><td></td></tr><tr><td> $N_1 = 16$ </td><td></td><td> $N_2 = 12$ </td><td></td></tr><tr><td colspan="4"> $D = (28\log_219)/(5\log_25) = 10.25$ </td></tr></table>

## References

<sup>w</sup> <sup>x</sup> 1 H. Almuallim, Y. Akiba, T. Yamazaki, S. Kaneda, Learning verb translation rules from ambiguous examples and a large semantic hierarchy, in: S.J. Hanson, G.A. Drastal, R.L. Rivest Ž . Eds. , Computational Learning Theory and Natural Learning Systems, vol. 4, MIT Press, Boston, 1994, pp. 323–336.

<sup>w</sup> <sup>x</sup> 2 D.A. Boehm-Davis, R.W. Holt, M. Koll, G. Yastrop, R. Peters, Effects of different data base formats on information retrieval. Human Factors 31 5 1989 579–592.Ž . Ž .

<sup>w</sup> <sup>x</sup> 3 D.J. Campbell, Task complexity: a review and analysis. Academy of Management Review 13 1 1988 40–52.Ž . Ž .

<sup>w</sup> <sup>x</sup>4 H.C. Chan, B.C.Y. Tan, K.K. Wei, Three important determinants of user performance for database retrieval, International Journal of Human-Computer Studies 51 1999 895–918.Ž .

<sup>w</sup> <sup>x</sup>5 H.C. Chan, K.K. Wei, K.L. Siau, User–database interface: the effect of abstraction levels on query performance, MIS Quarterly 17 4 1993 441–464.Ž . Ž .

<sup>w</sup> <sup>x</sup> 6 H.C. Chan, K.K. Wei, K.L. Siau, The effect of a database feedback system on user performance, Behaviour and Information Technology 14 3 1995 152–162.Ž . Ž .

<sup>w</sup> <sup>x</sup> 7 J. Davidson, S.J. Kaplan, Natural language access to data bases: interpreting update requests, American Journal of Computational Linguistics 9 2 1983 57–68.Ž . Ž .

<sup>w</sup> <sup>x</sup> 8 J.S. Davis, Experimental investigation of the utility of data structure and E-R diagrams in database query, International Journal of Man-Machine Studies 32 4 1990 449–459.Ž . Ž .

<sup>w</sup> <sup>x</sup> 9 S. Deck, Are You Weary of Warehouses? Computerworld, 1999 May 31 , 61, http: Ž . <sup>rr</sup>www.computerworld.com<sup>r</sup> home<sup>r</sup>print.nsf<sup>r</sup>all<sup>r</sup>990531AADE.

<sup>w</sup> <sup>x</sup> 10 J. Gantz, The New World of Enterprise Reporting Is Here, Computerworld, 1999 Feb. 1 , 34, http:Ž . <sup>rr</sup>www.computerworld.com<sup>r</sup>home<sup>r</sup>print.nsf<sup>r</sup>all<sup>r</sup>9902018D36.

<sup>w</sup> <sup>x</sup> 11 D.L. Goodhue, Understanding user evaluation of information systems, Management Science 41 12 1995 1827–1844.Ž . Ž .

<sup>w</sup> <sup>x</sup> 12 D.L. Goodhue, R.L. Thompson, Task-technology fit and individual performance, MIS Quarterly 19 2 1995 213–Ž . Ž . 236.

<sup>w</sup> <sup>x</sup> 13 S.L. Greene, L.M. Gomez, S.J. Devlin, A cognition analysis of database query production, Proceedings of the Human Factors Society 30th Annual Meeting, vol. 2, 1986, pp. 9–13.

<sup>w</sup> <sup>x</sup>14 S.L. Greene, S.J. Devlin, P.E. Cannata, L.M. Gomez, No Ifs, ANDs, or Ors: a study of database querying, International Journal of Man-Machine Studies 32 3 1990 303–326.Ž . Ž .

<sup>w</sup> <sup>x</sup> 15 M.H. Halstead, Elements of Software Science. Elsevier, Amsterdam, 1977.

<sup>w</sup> <sup>x</sup> 16 E. Horwitt, Webifying the Mainframe, Computerworld, 1999 Ž . Jan. 25 , 76–79, http:<sup>rr</sup>www.computerworld.com<sup>r</sup>home<sup>r</sup> print.nsf<sup>r</sup>all<sup>r</sup>9901258B66.

<sup>w</sup> <sup>x</sup> 17 E. Hutchins, J.D. Hollan, D.A. Norman, Direct manipulation interfaces. in: D.A. Norman, S.W. Draper Eds. , User Cen-Ž . tered System Design: New Perspectives on Human-Computer Interaction, Erlbaum, Hillsdale, NJ, 1985.

<sup>w</sup> <sup>x</sup> 18 J.W.K. Jih, D.A. Braford, C.A. Snyder, N.G.A. Thompson, The effects of relational and entity-relationship data models on query performance of end-users, International Journal of Man-Machine Studies 31 3 1989 257–267.Ž . Ž .

<sup>w</sup> <sup>x</sup> 19 C. Katzeff, System demands on mental models for a fulltext database, International Journal of Man-Machine Studies 32 Ž .1990 483–509.

<sup>w</sup> <sup>x</sup> 20 R.L. Leitheiser, S.T. March, The influence of database structure representation on database system learning and use 12 Ž . Ž .4 1996 187–213.

<sup>w</sup> <sup>x</sup> 21 F.H. Lochovsky, D.C. Tsichritzis, User performance considerations in DBMS selection, Proceedings of ACM SIGMOD. 1977, pp. 128–134.

<sup>w</sup> <sup>x</sup> 22 D.B. Mitchell, R.R. Hunt, How much effort should be devoted to memory? Memory and Cognition 17 3 1989Ž . Ž . 337–348.

<sup>w</sup> <sup>x</sup>23 D.A. Norman, Cognitive engineering. in: D.A. Norman, S.W. Draper Eds. , User Centered System Design, Erlbaum, Hills- Ž . dale, NJ, 1986, pp. 31–61.

<sup>w</sup> <sup>x</sup> 24 D.A. Norman, The Psychology of Everyday Things, Basic Books, New York, 1988.

<sup>w</sup> <sup>x</sup> 25 W.D. Ogden, R. Korenstein, J.B. Smelcer, An Intelligent Front-End for SQL, IBM, San Jose, CA, 1986.

<sup>w</sup> <sup>x</sup> 26 R.C. Parkison, K.M. Colby, W.S. Faught, Conversational language comprehension using integrated pattern-matching and parsing, Artificial Intelligence 9 2 1977 111–134.Ž . Ž .

<sup>w</sup> <sup>x</sup> 27 R.E. Podhorn, H.J. Pikner, The trend to end-user computing, Internal Auditing 7 1 1991 80–83.Ž . Ž .

<sup>w</sup> <sup>x</sup> 28 P. Reisner, Use of psychological experimentation as an aid to development of a query language, IEEE Transactions on Software Engineering 3 3 1977 218–229.Ž . Ž .

<sup>w</sup> <sup>x</sup> 29 P. Reisner, Human factors studies of database query languages: a survey and assessment, Computing Surveys 13 1Ž . Ž . 1981 13–31.

<sup>w</sup> <sup>x</sup> 30 S. Rho, S.T. March, An analysis of semantic overload in database access systems using multi-table query formulation, Journal of Database Management 8 2 1997 3–14.Ž . Ž .

<sup>w</sup> <sup>x</sup> 31 S. Sekine, J.J. Carroll, S. Ananiadou, J. Tsujii, Automatic learning for semantic collocation, Proceedings of the Third Conference on Applied Natural Language Processing, 1992, pp. 104–110.

<sup>w</sup> <sup>x</sup>32 K.S. Suh, A.M. Jenkins, A comparison of linear keyword and restricted natural language database interfaces for novice users, Information Systems Research 3 3 1992 252–272.Ž . Ž .

<sup>w</sup> <sup>x</sup> 33 I. Vessey, Cognitive fit: a theory-based analysis of the graphs versus tables literature, Decision Sciences 22 1991 219–Ž . 241.

<sup>w</sup> <sup>x</sup> 34 I. Vessey, D. Galletta, Cognitive fit: an empirical study of information acquisition, Information Systems Research 2 1Ž . Ž . 1991 63–84.

<sup>w</sup> <sup>x</sup> 35 R.E. Wood, Task compexity: definition of the construct, Organizational Behavior and Human Decision Processes 37 Ž . 1986 60–82.

![](/api/attachments/KGQNQX9T/fulltext/images/6cd43f523a106d44eb102cd2c7ee464a27fa2462f3eccb8dffcacc555c474158.jpg)

A. Faye Borthick, DBA, CMA, CPA, CISA, is Professor of Accountancy and Director of the Teaching and Learning with Technology Center, Georgia State University, Atlanta, GA, USA. For several decades, she has been working at the fault line of technology shifts in business and education. For courses in accounting and information systems, she has been developing new approaches to improving technology-enabled learning experiences, prompting students to solve

problems with technology tools, and engaging students in their learning. She has been teaching completely online courses since 1997.

![](/api/attachments/KGQNQX9T/fulltext/images/5caa073ddd78117cb7ccd01a218ee9c303797ab172827c81b24b1c0098130759.jpg)

Paul L. Bowen, PhD, is Senior Lecturer in Information Systems, University of Queensland, Brisbane, Australia, where he teaches information systems and auditing. His primary research includes developing analytical models of data quality, measuring the impact of data errors on decision quality, and applying artificial intelligence techniques to the identification and classification of data errors. He also has research interests in database design, internal control, and software

reliability. He has been a systems analyst and project manager at Oak Ridge National Laboratory and has taught at The University of Tennessee and Auburn University. http:<sup>rr</sup>www.commerce. uq.edu.au<sup>r</sup>staff<sup>r</sup>bowen.html.

![](/api/attachments/KGQNQX9T/fulltext/images/5b834fa520c5505b3812570049927031b43d251f51a6fdfba9e0d22cb705875f.jpg)

Donald L. Jones, PhD, is Assistant Professor of Accountancy, Georgia State University, Atlanta, GA, USA. His PhD is in information systems from the University of Texas at Austin. His principal research interest is how information technology affects decision making. He has published in journals such as Organizational BehaÕior and Human Deci sion Processes, Journal of Information Systems, and Auditing: A Journal of Practice and Theory. He is currently on

the editorial board of the Journal of Information Systems. http:<sup>rr</sup> www.gsu.edu<sup>r ;</sup>accdrj<sup>r</sup>.

![](/api/attachments/KGQNQX9T/fulltext/images/29264426456764ecdcc6140f35a507d1720f9e31cd59886596aa79b1aaeede53.jpg)  
Michael H.K. Tse, BCom Hons , BArts,Ž . works in the Communication, Medias and Internet team, JP Morgan Corporate Finance, Hong Kong. He has worked on cellular M&A transactions in the Asia-Pacific region. He has also worked in the Chase JF Financial Institutions Group. He graduated from The University of Queensland with a Bachelor of Commerce First Class Honours and aŽ . Bachelor of Arts, where he won The Queensland Investment Corporation

Prize and The Thomas Brown and Sons Award for research in SQL query performance.
