---
otero_id: 17884
otero_key: "VZYKATCQ"
title: "Database design practices for inverted files"
authors: "Jeffrey A. Hoffer"
year: "1980"
journal: "Information & Management"
doi: "10.1016/0378-7206(80)90021-x"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Database Design Practices for Inverted Files

Jeffrey A. Hoffer

Associate Professor of Operations and Systems Management, Indiana University, Bloomington, Indiana 47405, USA

Database research literature has proposed many procedures, both manual and automated, for database design; selection of secondary indexes for inverted file type database management systems (DBMS) has been repeatedly addressed. The empirical study reported here indicates that practical inverted file design has been relatively unaffected by this research.

This paper characterizes the actual database design process used at inverted file DBMS installations along such dimensions as: types of secondary keys constructed, the individuals who make index design decisions, the decisions that are changed (and when) after the initial database implementation, the factors that are considered in indexing decisions, and the literature which is used in the process. The study shows that key selection (as one example of a design decision) is addressed by ad hoc procedures and well conceived procedures are not used. Further, the results indicate that database design is dominated by users and systems analysts, indexes are frequently changed and a wide range of database performance and convenience factors are influential in practice. The paper concludes with some recommendations for database design support tools.

Keywords: Database design, inverted files, secondary indexes, database design practice, database management systems, database design tools

![](/api/attachments/VZYKATCQ/fulltext/images/e740ec7a0c2fe54759c11b213a672ef711e14f335957f9fb6bf71d5336a652fd.jpg)

Jeffrey A. Hoffer is an Associate Professor of Operations and Systems Management in the School of Business at Indiana University. He received his Ph.D. in Operations Research from Cornell University and has been on the faculty of Case Western Reserve University. His publications on database design, database integrity and MIS have been published in Very Large Data Base and SIGMOD Conference Proceedings, Information Sciences, Information & Management and the IEEE Transactions on Software Engineering.

## 1. Introduction

Many professionals feel that a database is essential for the realization of a true MIS [7,16,18,22]. If this is so, then an understanding of proper database design methods is necessary for the delivery of an efficient and effective MIS or decision support system (DSS).

Not surprisingly, there is an active literature which prescribes methods for database design. Each database architecture has its own problems; for example, the Data Base Task Group network model [5] has spawned development of procedures to determine set ownership, useful network arcs or paths, and physical record placement [10,11,20,27,28]. The hierarchical model, such as that of IBM's IMS package, has design issues such as hierarchical record segment placement and segment storage location to minimize access cost of shared segments [15,25]. And the design of a relational database can be optimized for candidate unique tuple identifiers which satisfy certain properties [2,4,6,8].

Effective logical database design procedures for one data model can often be transferrable to other data models (see [19] and [4]). This paper specializes in inverted file database design and attempts to describe how inverted files are designed in practice and how this relates to the methods prescribed in the literature.

## 2. Technology overview

The inverted file database architecture is one of the simplest of data models to understand and use. Figure 1 depicts this architecture. "Inverted" means that data is retrievable by content (values for attributes). Values for attributes which classify, order, relate or otherwise identify records are called keys and can be tabled in separate directories, or indexes similar to the subject, title, and author indexes used in libraries. A key that refers to no more than one database record is called a primary key; all other keys are called secondary keys. Records can be accessed using indexes for these keys; for example, a query for Figure 1 could be:

"List names and telephone numbers of all customers whose orders are to be shipped today (11/08/79) using UPS "

Typically the DBMS would develop two lists, one for the relevant Shipment Data and one for the relevant

Carrier (see Figure 2). These lists would then be intersected to find the common record numbers in both lists. Only these shipment records would be accessed, and the customer number can then be used to access, using the customer number index, the associated record in the customer file to provide the name and telephone number. Such accesses are normally performed automatically by the DBMS upon execution of the query statement. The DBMS also maintains the indexes automatically.

Design of an inverted database involves the decision whether or not to create an index for potential

![](/api/attachments/VZYKATCQ/fulltext/images/d333347eaf52d8b302f86d4ca0594c0f1155135a25ad358f49e7e53f097990b3.jpg)  
Figure 1. Example Data Base.

<table><tr><td colspan="3">Shipment File Access</td></tr><tr><td colspan="3">Shipment Date = 11/08/79 and Carrier = UPS gives Records to Access</td></tr><tr><td>2</td><td>1</td><td>3</td></tr><tr><td>3</td><td>3</td><td>257</td></tr><tr><td>150</td><td>80</td><td></td></tr><tr><td>257</td><td>257</td><td></td></tr><tr><td colspan="3">Customer File Access</td></tr><tr><td colspan="3">Customer No. = 5276 or 1687 (Records to Access)</td></tr><tr><td colspan="3">a</td></tr><tr><td colspan="3">y</td></tr></table>

Figure 2. Query Processing.

keys. The determination of candidate keys is not trivial since a key can be the concatenation of several attributes or even subsets of characters of attributes. For example, in Figure 1, if queries which use both Shipment Date and Carrier were frequently submitted, then it might be effective to construct an index for the concatenated key of Figure 3. A wide variety of useful keys are possible: refs. [13] and [14].

![](/api/attachments/VZYKATCQ/fulltext/images/54aa8caad6da0262dbf8a9d81d57bae9ee240ae002e77e15e5fa8e36e99d0b4e.jpg)  
Figure 3. Concatenated Key.

Researchers have considered one time decision models [1,9,17]; models which adapt to changing database content with reindexing [12] have been proposed. Each approach assumes certain database performance criteria (often query time/cost) and certain query representations (usually a probabilistic model). Some approaches predict database performance (e.g., [1,3,14]), others derive properties of a given set of candidate keys ([23,24]); in some limited cases, the actual optimal indexing structure is developed. The determination of candidate keys has been addressed by a few authors [2,13,19].

However, this research has only considered the mechanics of inverted file design. The remainder of this paper describes, as comprehensively as possible, the key selection process and the methods used by those who actually design inverted database; comparisons will be made between the practice of design and proposed methodologies of the research literature.

## 3. Data base design practice

## 3.1. Survey demographics

Seventy-one (71) users of six commercially available DBMS with secondary indexing capabilities responded to a mail survey (see Table 1). Some questions provide fewer than 71 response because of missing data. The questionnaires were completed by individuals with MIS positions ranging from Data Base Administrator to MIS Manager to programmer. The results (derived using [21]) indicate to a wide range of experience, database strategies and perceptions among the surveyed firms.

Table 2 summarizes some of the notable database characteristics from the sampled sites. The Model 204 and System 2000 users sampled have used their packages longer, on the average, than users of the other packages and consequently have constructed more complex databases. There does appear to be an increase in the size of database the longer a DBMS is used (the often quoted evolution benefit). ADABAS users tend to have fewer databases and, hence, probably more files per database.

Some surprisingly small and large databases were represented in the sample. Since the survey was anonymous, no motive or misinterpretation could be discovered for why one Datacom/DB user has an inverted file with only one data element per record. However, records with very few elements also occur in data bases from users of other packages. Users of three of the four primary packages had files with as few as ten records. The databases are used to support a variety of data processing applications (see Table 3). A large percentage of the inverted files support transaction processing.

Table 1  
Number of Survey Samples for Each DBMS

<table><tr><td>DBMS</td><td>Number of Responses</td></tr><tr><td>ADABAS</td><td>18</td></tr><tr><td>Datacom/DB</td><td>21</td></tr><tr><td>Model 204</td><td>10</td></tr><tr><td>System 2000</td><td>16</td></tr><tr><td>CDCS</td><td> $3^{a)}$ </td></tr><tr><td>QU</td><td> $\frac{3}{71}^{a)}$ </td></tr></table>

## 3.2. Types of Keys Used

Hoffer [13,14] has described and discussed a wide variety of primary and secondary key types. Each surveyee was asked to indicate usage of these key types $^{1}$ (see Table 4). In addition, under “other,” one ADABAS user reported that databases are fully inverted, i.e., an index is constructed on each attribute.

Model 204 users appear to have the greatest variety of key types. However, using a Chi Squared test of significant statistical independence, only two key types (types 5 and 8) showed a clear distinctive utilization across DBMS. Some Model 204 and ADABAS users do not create primary key indexes, although Model 204 can distinguish a primary key from secondary keys. Further, although a high percentage of users of each package construct traditional secondary keys (key type 2), a small percentage of each user population does not do so. Overall, the least used key type, partial attribute values (e.g., the first 8 characters of a Customer name), was used by some users of each package.

Table 4 shows that inverted file design practice considers a diverse range of potential key types. Consequently, many potential keys are candidates. Further, index selection must consider combination of indexes, not just each index independently, since a pair of keys or one concatenated combination are alternative implementations. Thus, the total number of feasible solutions grows combinationally and mathematical search procedures become prohibitively expensive. In order to assist an actual database design, database design tools must have ways to eliminate large numbers of solutions; neither the database designer nor an automated search could consider all key combinations.

Table 2
Database Characteristics

<table><tr><td rowspan="2">Database Characteristic</td><td colspan="4">Users of</td><td rowspan="2">All Responses Combined</td></tr><tr><td>ADABAS</td><td>Datacom/DB</td><td>Model 204</td><td>System 2000</td></tr><tr><td>Average Years of Use</td><td>2.3</td><td>2</td><td>4</td><td>3.75</td><td>2.5</td></tr><tr><td>Average No. of Databases</td><td>1.8</td><td>1.6</td><td>13.7</td><td>23.7</td><td>10.5</td></tr><tr><td>Range of No. of Databases</td><td>1-4</td><td>1-28</td><td>1-50</td><td>2-75</td><td>1-75</td></tr><tr><td>Average No. of Files in All Databases</td><td>17.6</td><td>23.7</td><td>32.2</td><td>132.8</td><td>38.6</td></tr><tr><td>Range of No. of Files in All Databases</td><td>1-70</td><td>1-54</td><td>7-100</td><td>3-400</td><td>1-400</td></tr><tr><td>Median No. Records per File</td><td>15 000</td><td>40 000</td><td>2775</td><td>800</td><td>10 000</td></tr><tr><td>Range of No. of Records Per File</td><td>10-5 M</td><td>10-3 000 000</td><td>450-80 000</td><td>10-1 M</td><td>10-5 M</td></tr><tr><td>Average No. Data Elements per File</td><td>38.6</td><td>11.8</td><td>10.4</td><td>76 5</td><td>32.8</td></tr><tr><td>Range of No. of Data Elements per File</td><td>3-170</td><td>1-47</td><td>4-20</td><td>2-200</td><td>1-200</td></tr></table>

## 3.3. Designers of Inverted Files

Designers can be divided into two categories: (1) Those who identify potential keys, and (2) Those who decide to index a potential key. Only the first of these is addressed below and in Table 5, since no striking differences were found between the analysis for each; Hoffer [14] presents the results for both in detail.

Most notable was the fact that all Model 204 users indicated that system programmers were involved in key identification and this was a significant departure from the practice for users of other packages. To a lesser degree, Model 204 installations do not use DBA's for this task whereas ADABAS sites do. Across all packages, the system analyst is a major source of insight into potential keys; programmers have the least significant role to play. Thus, database design support tools can not be intended for use by technical database experts. Rather, the tools must be usable by those interested in the functionality of the database. Tools which require knowledge of database internal architecture will probably not be used unless more technical staff members are part of the database design team.

Data Processing Applications Supported by Inverted Files

<table><tr><td rowspan="2">Application</td><td colspan="5">% of Users Who Use Database to Support the Application</td></tr><tr><td>ADABAS</td><td>Datacom/DB</td><td>Model 204</td><td>System 2000</td><td>All Respondents</td></tr><tr><td>Transaction Processing</td><td>77.8</td><td>100</td><td>70</td><td>62.5</td><td>80</td></tr><tr><td>Reporting and Inquiry</td><td>94.4</td><td>85.7</td><td>100</td><td>100</td><td>93</td></tr><tr><td>General Business</td><td>66.7</td><td>71.4</td><td>60</td><td>50</td><td>62</td></tr><tr><td>Financial Planning</td><td>16.7</td><td>33.3</td><td>40</td><td>43.8</td><td>31</td></tr><tr><td>Research</td><td>16.7</td><td>0</td><td>40</td><td>25</td><td>18</td></tr><tr><td>Text Processing</td><td>0</td><td>4.8</td><td>20</td><td>12.5</td><td>8.5</td></tr><tr><td>Manufacturing</td><td>22.8</td><td>23.8</td><td>20</td><td>12.5</td><td>18.3</td></tr><tr><td>Accounting</td><td>44.4</td><td>66.7</td><td>40</td><td>68.8</td><td>57.7</td></tr><tr><td>Human Resources</td><td>16.7</td><td>4.8</td><td>40</td><td>37.5</td><td>23.9</td></tr><tr><td> $Engineering^a)$ </td><td>0</td><td>0</td><td>0</td><td>0</td><td> $7 (6/71)^b)$ </td></tr><tr><td> $Education^a)$ </td><td>0</td><td>0</td><td>10 (1/10)</td><td>6.3 (1/16)</td><td>2.8 (2/71)</td></tr><tr><td>Correspondence</td><td>0</td><td>0</td><td>20 (2/10)</td><td>0</td><td>2.8 (2/71)</td></tr><tr><td>Other</td><td>11.1</td><td>0</td><td>10 (1/10)</td><td>37.5 (6/16)</td><td>19.7 (14/71)</td></tr></table>

a) These application types were not on the questionnaire but were specified by some respondents under the "Other" category; consequently, other "Other" responses given without specifications may include these applications.  
b) All of these observations are from the CDC package.

Table 4
Key Types Used in Practice

<table><tr><td rowspan="2">Key Type</td><td colspan="6">% of Respondents Who Use the Key Type</td></tr><tr><td>ADABAS</td><td>Datacom/DB</td><td>Model 204</td><td>System 2000</td><td>All Respondents</td><td>Significance Level</td></tr><tr><td>1) Primary key/ record identifier</td><td>88.9</td><td>100</td><td>90</td><td>100</td><td>94.4</td><td>(0.15)</td></tr><tr><td>2) Single non-unique attribute</td><td>88.9</td><td>81</td><td>90</td><td>93.8</td><td>84.5</td><td>(0.13)</td></tr><tr><td>3) Link records from different files</td><td>66.7</td><td>71.4</td><td>80</td><td>37.5</td><td>63.4</td><td>(0.26)</td></tr><tr><td>4) Link records in same file</td><td>27.8</td><td>42.9</td><td>70</td><td>43.8</td><td>40.8</td><td>(0.22)</td></tr><tr><td>5) Descriptive record categorization based on a few values for one attribute</td><td>50</td><td>33.3</td><td>70</td><td>68.8</td><td>47.9</td><td>(0.03)</td></tr><tr><td>6) Concatenated attributes</td><td>77.8</td><td>85.7</td><td>50</td><td>56.3</td><td>69</td><td>(0.15)</td></tr><tr><td>7) Record sorting</td><td>61.1</td><td>57.1</td><td>60</td><td>43.8</td><td>57.7</td><td>(0.6)</td></tr><tr><td>8) Partial attribute value</td><td>44.4</td><td>33.3</td><td>70</td><td>18.8</td><td>35.2</td><td>(0.04)</td></tr></table>

Table 5  
Who Identifies Potential Keys

<table><tr><td rowspan="2">Identifier</td><td colspan="6">% of Respondents Where Particular Job Categories Are Identifiers of Potential Keys</td></tr><tr><td>ADABAS</td><td>Datacom/DB</td><td>Model 204</td><td>System 2000</td><td>All Respondents</td><td>Significance Level</td></tr><tr><td>Data Base</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Administrator</td><td>83.3</td><td>61.9</td><td>40</td><td>62.5</td><td>62</td><td>(0.17)</td></tr><tr><td>System Programmer</td><td>5.6</td><td>47.6</td><td>100</td><td>12.5</td><td>22.5</td><td>(0.003)</td></tr><tr><td>Application</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Programmer</td><td>44.4</td><td>38.1</td><td>40</td><td>37.5</td><td>40.8</td><td>(0.95)</td></tr><tr><td>User</td><td>61.1</td><td>52.4</td><td>70</td><td>56.3</td><td>54.9</td><td>(0.36)</td></tr><tr><td>Systems Analyst</td><td>94.4</td><td>90.5</td><td>90</td><td>93.8</td><td>85.9</td><td>(0.95)</td></tr></table>

Table 6  
Who Jointly Works to Identify Keys

<table><tr><td rowspan="2">Identifier of Keys</td><td colspan="4">Identifier of Keys (% Both Work on Key Identification a))</td></tr><tr><td>Systems Programmer</td><td>Applications Programmer</td><td>Systems Analyst</td><td>User</td></tr><tr><td>Data Base Administrator</td><td>12.7</td><td>25.4</td><td>53.5</td><td>35.2</td></tr><tr><td>Systems Programmer</td><td></td><td>-(0.24)</td><td>-(0.06)</td><td>-(0.19)</td></tr><tr><td></td><td></td><td>5.6</td><td>15.5</td><td>8.5</td></tr><tr><td>Applications Programmer</td><td></td><td></td><td></td><td>(0.08)</td></tr><tr><td></td><td></td><td></td><td>35.2</td><td>28.2</td></tr><tr><td>Systems Analyst</td><td></td><td></td><td></td><td>(0.006)</td></tr><tr><td></td><td></td><td></td><td></td><td>53.5</td></tr></table>

a) The value in (·) represents the level of significance when testing the statistical independence of the pair of individuals being involved in key selection.

When one examines the database design group composition, Table 6 indicates the strong statistical correlation $^{1}$ between the use of systems analysts and users for key identification. In 53.5% of all responses, both systems analysts and users were involved and a Chi Squared test of statistical independence indicates strongly that if one individual is used, then it is very likely that the other is also used and if one is not used then the other is not likely to be used. Further, the survey indicated that not only are system and application programmers least likely to be involved in key identification, but that technical support is not even sought by users and systems analysts.

It was also discovered that certain individuals favor certain key types. For example, Table 7 shows that in 59.2% of all survey responses, the DBA was involved in key identifications AND primary keys were constructed. The strongest dependence is one of disfavor where the presence of system programmers usually means that partial attribute value keys (e.g., first 8 characters of customer name) are not constructed. Further, systems analysts, not users, are the real culprits in index proliferation. Possibly, users do not in general yet understand the power of secondary indexing whereas the analyst who understands the technology and user needs tries to satisfy the user (look good) with a powerful content addressability.

## 3.4. Index Dynamics

System 2000 has the largest percentage of users purging indexes but not for all possible reasons (see Table 8). However, the reindexing by purging is done exclusively for performance (space and index maintenance) reasons under S2000. On the other hand, Datacom/DB and Model 204 users create indexes that have a definite life span either due to a periodic data processing cycle, generations of database or a clean break between a database used during testing (possibly a prototype) and used for final data processing productive work.

<table><tr><td rowspan="2">Identifier of Keys</td><td colspan="8">% Key Type Is Used by Those Respondents in Which Particular Job Classifications Are Involved in Key Identificationsa)</td></tr><tr><td>Primary</td><td>Single Secondary</td><td>Link Different Files</td><td>Link Same File</td><td>Categorize</td><td>Concatenated</td><td>Record Sorting</td><td>Partial Attribute</td></tr><tr><td>Database Administrator</td><td>59.2</td><td>54.9</td><td>39.4</td><td>22.5</td><td>29.6-(0.22)</td><td>42.3</td><td>38.0</td><td>19.7</td></tr><tr><td>Systems Programmer</td><td>22.5</td><td>16.9</td><td>14.1</td><td>11.3</td><td>7.0</td><td>16.9</td><td>12.7</td><td>1.4</td></tr><tr><td>Applications Programmer</td><td>39.4</td><td>36.6(0.07)</td><td>29.6</td><td>18.3</td><td>15.5(0.02)</td><td>29.6(0.08)</td><td>23.9</td><td>18.3(0.03)</td></tr><tr><td>Systems Analyst</td><td>81.7</td><td>76.1</td><td>54.9</td><td>35.2</td><td>46.5</td><td>63.4</td><td>47.9</td><td>35.2</td></tr><tr><td>User</td><td>53.5</td><td>49.3</td><td>33.8</td><td>23.9</td><td>29.6</td><td>36.6</td><td>29.6</td><td>22.5</td></tr></table>

Table 7
Association Between Key Identifiers and Key Types

Table 8
Index Purging

<table><tr><td rowspan="3"></td><td colspan="5">% of Respondents Who Purge Indexes</td></tr><tr><td>ADABAS</td><td>Datacom/DB</td><td>Model 204</td><td>System 2000</td><td>All Respondents</td></tr><tr><td>55.6</td><td>42.9</td><td>50</td><td>75</td><td>50.7</td></tr><tr><td>Reasons</td><td colspan="5">% of Those Respondents Who Do Purge, Who Purge for Reason</td></tr><tr><td>1) Index no longer necessary - save space</td><td>41.7</td><td>10</td><td>25</td><td>27.3</td><td>27</td></tr><tr><td>2) Improve efficiency of batch-update programs</td><td>16.7</td><td>10</td><td>0</td><td>18.2</td><td>13.5</td></tr><tr><td>3) Index not used frequently enough</td><td>8.3</td><td>10</td><td>0</td><td>27.3</td><td>13.5</td></tr><tr><td>4) Database reorganization for over. all efficiency/improvement</td><td>0</td><td>40</td><td>0</td><td>27.3</td><td>18.9</td></tr><tr><td>5) Time dependent (e.g., month log)</td><td>0</td><td>10</td><td>0</td><td>0</td><td>2.7</td></tr><tr><td>6) New (evolved) database</td><td>0</td><td>10</td><td>0</td><td>0</td><td>2.7</td></tr><tr><td>7) Change from Database in test to production modes</td><td>0</td><td>0</td><td>25</td><td>0</td><td>2.7</td></tr></table>

Table 9 shows that Model 204 and S2000 users exhibit a noticeably higher tendency to create new indexes than do other users. Datacom/DB users add frequently for performance (e.g., response time) reasons. Also as before, Model 204 users exhibit an evolutionary database environment where a growing database with new files and attributes requires the creation of new indexes.

Model 204 users were distinguishable in their greater tendency to temporarily create and purge indexes (see Table 10) although they undertake this form of dynamic indexing less frequently than they did the other two forms. ADABAS users cited a recurring need to create and purge; i.e., each time an infrequently run report was produced. Also as above, Model 204 users gave a reason related to database evolution; this time transient indexes are used during database testing or new program (presumably retrieval) testing to provide access to a sample database.

Table 9
Dynamic Index Creation

<table><tr><td rowspan="3"></td><td colspan="5">% of Respondents Who Add Indexes After Data Base Established</td></tr><tr><td>ADABAS</td><td>Datacom/DB</td><td>Model 204</td><td>System 2000</td><td rowspan="2">All Respondents 66.2</td></tr><tr><td>55.6</td><td>52.4</td><td>90</td><td>93.8</td></tr><tr><td>Reasons</td><td colspan="5">% of Those Respondents Who Do Add, Who Add for Reason</td></tr><tr><td>1) New, unanticipated data selection requirement</td><td>66.7</td><td>18.2</td><td>62.5</td><td>61.5</td><td>52.2</td></tr><tr><td>2) Reorganize database for overall performance improvement</td><td>0</td><td>45.5</td><td>12.5</td><td>15.4</td><td>17.4</td></tr><tr><td>3) Improve update response time</td><td>0</td><td>9.1</td><td>0</td><td>0</td><td>2.2</td></tr><tr><td>4) Repair a damaged index</td><td>0</td><td>9.1</td><td>0</td><td>7.7</td><td>4.3</td></tr><tr><td>5) New data base contents</td><td>0</td><td>0</td><td>12.5</td><td>0</td><td>4.3</td></tr><tr><td>6) Speed-up response time for ad hoc queries</td><td>0</td><td>0</td><td>0</td><td>7.7</td><td>2.2</td></tr><tr><td>7) Overall faster response time</td><td>0</td><td>0</td><td>0</td><td>7.7</td><td>2.2</td></tr></table>

Table 10 Temporary Indexes

<table><tr><td rowspan="3"></td><td colspan="5">% of Respondents Who Temporarily Create and Destroy Indexes for Transient Needs</td></tr><tr><td>ADABAS</td><td>Datacom/DB</td><td>Model 204</td><td>System 2000</td><td>All Respondents</td></tr><tr><td>11.1</td><td>10</td><td>30</td><td>12.5</td><td>14.3</td></tr><tr><td>Reasons</td><td colspan="5">% of Those Respondents Who Do Temporarily Create, Who Do So for Reason</td></tr><tr><td>1) One-time requirement</td><td>14.3</td><td>0</td><td>25</td><td>50</td><td>20</td></tr><tr><td>2) Low periodicity report</td><td>14.3</td><td>0</td><td>0</td><td>0</td><td>5</td></tr><tr><td>3) Database loading</td><td>0</td><td>25</td><td>0</td><td>0</td><td>5</td></tr><tr><td>4) Transaction during update</td><td>0</td><td>25</td><td>0</td><td>0</td><td>10</td></tr><tr><td>5) Report sorting</td><td>0</td><td>0</td><td>25</td><td>0</td><td>5</td></tr><tr><td>6) Sample database for testing</td><td>0</td><td>0</td><td>25</td><td>0</td><td>5</td></tr></table>

The following correlated events or activities were also discovered:

1) The participation of the DBA in key identification and the subsequent temporary creation/purging of indexes (the direction of the relationship could not be determined)

2) The participation of users and the subsequent purging of indexes (the strongest direction was from user to purging which might suggest that users overstate their needs).

The above suggests that the so called “adaptive” tools $[12]$ which can deal well with incremental changes in database architecture may be the most useful in practice. Further, since most analytical tools tend to consider equally all database processing over some planning horizon, transient needs may be overlooked, yet, the usefulness is real. For this reason, totally automated index selection tools are not appropriate. Finally, this data clearly indicates that database design includes monitoring and redesign and that to be useful, a database design tool must not only accept estimates of future activity but also be tied into current, changing programs. This final point is reinforced in the next section.

## 3.5. Factors in the Design Process

The survey dealt with three process issues: (1) a general characterization including when in the information systems development cycle indexes are selected (Table 11), (2) the database performance measures considered when evaluating potential keys (Table 12) and (3) the influence of unknown or Ad Hoc queries in key selection (Table 13). Table 11 indicates that user stated needs and projections of data use by programs now in development or expected in the future are the primary general characterizations of the key selection process. Only Model 204 users seem to use all approaches with a high frequency.

For all DBMS groups, except ADABAS, indexes are usually chosen early in systems specification (functional systems specification) when users are most closely linked into the design. But later, after all functional specifications have been made, index decisions are also often considered at the time programs are physically designed and database structures/organizations are chosen. Indexes are selected at different points in systems development and, one could assume, that decisions made early are reconsidered in later stages. A few respondents also indicated that they on occasion delay indexing decisions until database load time.

As indicated in Table 12, no one performance factor seems to dominate although the various maintenance costs for the created indexes are important.

Table 11  
General Key Selection Process Description

<table><tr><td rowspan="2">Characterization</td><td colspan="5">%</td></tr><tr><td>ADABAS</td><td>Datacom/DB</td><td>Model 204</td><td>System 2000</td><td>All Respondents</td></tr><tr><td>Analyze existing programs</td><td>50</td><td>57.1</td><td>80</td><td>46.7</td><td>54.3</td></tr><tr><td>Project future programs</td><td>88.9</td><td>85.7</td><td>90</td><td>93.3</td><td>88.6</td></tr><tr><td>Data structural analysis</td><td>44.4</td><td>38.1</td><td>70</td><td>33.3</td><td>42.9</td></tr><tr><td>User stated needs</td><td>95.4</td><td>95.2</td><td>90</td><td>80</td><td>88.6</td></tr><tr><td>Timing</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>During user requirements analysis</td><td>50</td><td>66.7</td><td>70</td><td>66.6</td><td>60.9</td></tr><tr><td>During detailed functional specification</td><td>27.8</td><td>26.6</td><td>30</td><td>26.7</td><td>27.5</td></tr><tr><td>During physical systems design, coding</td><td>61.1</td><td>42.9</td><td>50</td><td>40</td><td>47.8</td></tr></table>

Table 12  
Performance Factors Which Influence Index Selection

<table><tr><td rowspan="2">Factor</td><td colspan="5">%</td></tr><tr><td>ADABAS</td><td>Datacom/ΓB</td><td>Model 204</td><td>System 2000</td><td>All Respondents</td></tr><tr><td>Index storage space</td><td>55.6</td><td>66.7</td><td>90</td><td>46.7</td><td>60</td></tr><tr><td>Ad hoc retrieval query speed</td><td>50</td><td>38.1</td><td>60</td><td>73.3</td><td>50</td></tr><tr><td>Known retrieval program speed</td><td>55.6</td><td>61.9</td><td>70</td><td>73.3</td><td>61.4</td></tr><tr><td>Index maintenance</td><td>88.9</td><td>85.7</td><td>90</td><td>86.7</td><td>81.4</td></tr><tr><td>On-line update program speed</td><td>55.6</td><td>81</td><td>70</td><td>53.3</td><td>60</td></tr><tr><td>On-line update program cost</td><td>33.3</td><td>71.4</td><td>70</td><td>33.3</td><td>47.1</td></tr><tr><td>Batch update program speed</td><td>38.9</td><td>33.3</td><td>60</td><td>53.3</td><td>42.9</td></tr><tr><td>Ease of programming</td><td>38.9</td><td>47.6</td><td>80</td><td>40</td><td>52.9</td></tr></table>

Ease of programming (and, hence, the reduced cost of programming) is not often cited in the literature as a benefit of indexing, yet, numerous respondents checked this as a factor in index selection. Except for \$2000 respondents, the cost for index storage space slightly dominated Ad Hoc and known retrieval program execution speed factors. This implies that database designers would not be content to take the easy solution of indexing all attributes but do wish to seriously consider each candidate key.

Table 13  
Ad Hoc Query Characterization

<table><tr><td>Is Ad Hoc Query Support Considered in Index Selection</td><td>ADABAS</td><td>Datacom/DB</td><td>Model 204</td><td>System 2000</td><td>All Respondents</td></tr><tr><td>Yes</td><td>50</td><td>28.6</td><td>50</td><td>81.3</td><td>46.5</td></tr><tr><td>How Characterized</td><td colspan="5">% of Those Who Said Yes Above</td></tr><tr><td>Probabilities of key use</td><td>77.8</td><td>66.7</td><td>57.1</td><td>69.2</td><td>68.6</td></tr><tr><td>Subjective nonquantitative way</td><td>33.3</td><td>16.7</td><td>57.1</td><td>38.5</td><td>37.1</td></tr></table>

S2000 users (100% of whom use a query language) design inverted database for Ad Hoc queries (see Table 13); other DBMS user groups do as well but to a lesser degree. Further, for those respondents who do design in light of future data processing, designers try to quantify this unknown world through estimating probabilities of key use.

Several other associations have been tested:

1) Database administrators seem to cause a higher tendency to analyze existing programs. This relationship was (statistically) significant for ADABAS and S2000 respondent classes whereas this relationship was not strong in other environments. In addition, for only S2000 users, an analysis of the data itself (i.e., its structure and meaning) was less likely to be performed if the DBA was involved.

2) A DBA appears to reduce the likelihood of hasty decisions and to require an information system to be more fully specified before indexing decisions are made. In fact, if a DBA is involved in identifying potential keys, it is much more likely that the actual decision to index will be delayed until physical database and program design has occurred. When application programmers participate, the actual decision on indexing is more likely to be delayed until physical systems design (since this is when the programming job really begins). More surprising was the fact that this same relationship held between the participation of users and the tendency to delay indexing decisions until physical systems specifications.

3) The presence of a DBA in key identification increased significantly the likelihood that index maintenance considerations, especially from batch up-date programs, would influence indexing decisions. Systems analysts have a similar effect.

4) Systems programmers, for some reason, tend to ignor on-line, Ad Hoc retrieval programs when selecting indexes; the presence of application programmers and/or users, however, increase the chances that on-line, update programs influence which indexes are constructed. Application programmers also interject ease of programming considerations into the index selection process whereas system analysts have a negative effect on considering this factor.

5) Users, more than other parties, consider on-line, Ad Hoc retrieval queries as important factors in

making indexing decisions.

6) A data analysis (structure, "inherent" content characteristics) method, when applied to key identification/selection process, increases the likelihood that indexes will be purged, added and dynamically created/destroyed after the database goes into operation. Data analysis was the least used of all methods and, apparently, justifiably so.

7) Selecting indexes early in the data processing system development cycle (closer user contact) also is statistically related to the subsequent adding of new indexes after database creation. However, there is no statistical relationship between early index selection and purging or transient indexes. On the other hand, delaying the indexing decision until detailed functional specification is associated with adding indexes during operation and creation of temporary indexes. Making indexing choices during physical design and programming has no statistical association with the dynamic nature of indexes.

8) Purging and creating new indexes seem to occur more frequently when on-line, Ad Hoc retrieval queries are considered as a factor in index selection. This seems natural since the materialization of these queries would be what would induce designers to reconsider indexing choices.

The conclusions from all of this in relation to a database design methodology are:

a) A multi-criteria objective function which can display or trade-off a wide variety of performance measures is essential and that the component measures must be combined with variable weights since different uses favor different benefits.

b) Both current and future programs must be considered in the analysis (whereas, most previously developed methods model all programs together as an Ad Hoc query). Data structure analysis does not appear to be helpful for secondary key selections in practice (in contrast to Martin's [19] content analysis method of bubble charts and canonical views).

## 3.6. Importance of Index Selection

Table 14 suggests that respondents desired support tools for key identification and a manual procedure rather than an automated utility program was preferred. However, only 8.6% of all respondents now have any such procedure. Likewise, when asked whether a procedure for index selection would be useful, a manual version again was preferred. An even lower percentage than above, 2.9%, now have such a procedure for index selection.

Table 14
Index Selection Importance and Support

<table><tr><td rowspan="2">Question</td><td colspan="5">% Yes</td></tr><tr><td>ADABAS</td><td>Datacom/DB</td><td>Model 204</td><td>System 2000</td><td>All Respondents</td></tr><tr><td colspan="6">Want to use a key identification procedure</td></tr><tr><td>Manual</td><td>72.2</td><td>47.6</td><td>70</td><td>46.2</td><td>58.5</td></tr><tr><td>Automated</td><td>33.3</td><td>28.6</td><td>50</td><td>23.1</td><td>30.8</td></tr><tr><td>Currently have such a utility</td><td>27.8</td><td>0</td><td>10</td><td>0</td><td>8.6</td></tr><tr><td colspan="6">Want to use an index selection procedure</td></tr><tr><td>Manual</td><td>47.1</td><td>45</td><td>70</td><td>30.8</td><td>47.6</td></tr><tr><td>Automated</td><td>41.2</td><td>25</td><td>50</td><td>38.5</td><td>34.9</td></tr><tr><td>Currently have such a utility</td><td>11.8</td><td>0</td><td>0</td><td>0</td><td>2.9</td></tr><tr><td colspan="6">Published Literature</td></tr><tr><td>Vendor Manuals</td><td>11.1</td><td>19</td><td>10</td><td>18.8</td><td>14.1</td></tr><tr><td>Martin: Computer Data-base Organization</td><td>0</td><td>9.5</td><td>0</td><td>0</td><td>2.8</td></tr><tr><td>Date: Intro. to Database Systems</td><td>11.2</td><td>0</td><td>0</td><td>0</td><td>2.8</td></tr><tr><td>Wiederhold: Database Design</td><td>5.5</td><td>0</td><td>0</td><td>0</td><td>1.4</td></tr></table>

Currently, users of the DBMS surveyed rely on vendor documentation and reference manuals for clues on when to index. Only slightly more than one-fifth of all respondents refer to any literature at all. Most revealing is that no one cited any of the scientific or “scholarly” works on index selection (see, e.g., [1,3,9,12,17,23,24]). The only non-vendor publications mentioned were three, general database management textbooks which provide, for the most part, insight into database architectures and access, data definition languages.

The conclusions to be reached from this data are (1) that key indentification and index selection are perceived to be important issues to those database and data processing professionals who completed the questionnaire but (2) these decision makers are poorly supported by either in-house decision aids or published procedures.

## 4. Conclusions

The results of the survey reported above indicate that the theory and practice of inverted file design are not consistent. Practical database design is multi-criteria, ad hoc, and done in isolation from the normative literature. Further, databases and database design are adaptive and design decisions require a trigger to indicate the time for a reassessment as well as a procedure to consider incremental, not comprehensive redesigns. Databases must be designed to meet both known, current applications as well as anticipated but imprecisely known future requirements. To support these applications, an inverted file designer must consider a wide range of key types where the numer of potential keys implies a need for systematic evaluation of alternatives by support tools (index all keys were viewed implicitly as undesirable by most designers). Database design tools must not be designed for use solely by technicians; rather, it is more likely that functionally oriented individuals will actually design in teams. This implies that satisficing [26] not optimal solutions are acceptable and possibly the only ones tolerated (if the effort to achieve an optimal over a satisficing solution is "too great").

Database design in practice (as evidenced in inverted file environments) is not unlike other decision processes. It is recurring and evolutionary due to changing conditions and recapitulation. Databases must be designed to support not only on-going operations but also transient, yet, important activities.

Database design support systems (DDSS to coin a phrase [10]) are desired but practically non-existent. Possibly due to not satisfying the necessary characteristics suggested above, current tools proposed in the literature are not used in practice. If databases are the foundation of the operation of an MIS, then well supported database design is necessary and work should continue to produce more usable design tools. It is hoped that this paper has given insight into what characteristics usable tools might possess.

## References

[1] Henry D. Anderson, and P. Bruce Berra, "Minimum Cost Selections of Secondary Indexes for Formatted Files," ACM-Transactions on Data-Base Systems, 2, 1 (March 1977), 68-90.

[2] Phillip A. Bernstein, "Synthesizing Third Normal Form Relations from Functional Dependencies," ACM-TODS, 1, 4, (December 1976), pp. 277-298.

[3] Alfonso F. Cardenas, "Analysis and Performance of Inverted Data Base Structures," CACM, 8, 5 (May 1975), 253-263.

[4] Peter Chen, "The Entity-Relationship-Approach to Logical Database Design." Wellesley, Mass.: Q.E.D. Information Sciences, Inc.; Monograph No. 6 in Data Base Management, 1978.

[5] CODASYL, CODASYL Data Base Task Group Report, April, 1971 (published by ACM).

[6] E.F. Codd, "A Relational Model of Data for Large Shared Data Banks," CACM 13, 6 (June 1970), 377-387.

[7] John J. Donovan, "Database System Approach to Management Decision Support," ACM-TODS, 1, 4, (December 1976), pp. 344-365.

[8] Ron Fagin, "Multivalued Dependencies and a New Normal Form for Relational Databases," ACM-TODS, 2, 3 (Sept. 1977) 262-278.

[9] J.H. Farley, and S.A. Schuster, "Query Execution and Index Selection for Relational Data Base," Very Large Data Base Conference Proceedings, September 1975 and Technical Report CSRG-53, Computer Systems Research Group, University of Toronto, 1975.

[10] Thomas J. Gambino, and Rob Gerritson, "A Data Base Design Decision Support System," Very Large Data

Base Conference Proceedings, 1977, pp. 534-544.

[11] Rob Gerritsen, "A Preliminary System for the Design of DBTG Data Structures," ACM-SIGMOD Conference Proceedings, 1975, pp. 166.

[12] Michael Hammer, and A. Chen, "Index Selection in a Self-Adaptive Data Base Management System, ACM-SIGMOD Conference Proceedings, 1976, Washington, D.C., 1-8.

[13] Jeffrey A. Hoffer, "A Survey of Primary and Secondary Keys Through a Case Study," Information & Management, 2, 3 (September 1979), pp. 99-107.

[14] Jeffrey A. Hoffer, "Primary and Secondary Key Selection Methods." Wellesley, Mass.: QED. Information Sciences, Inc.; Monograph in Data Base Management, 1980.

[15] G. Hubbard, and N. Raver, "Automating Logical File Design," Very Large Data Base Conference Proceedings 1975, pp. 227-253.

[16] Charles H. Kriebel, "The Future MIS," Infosystems, June, 1972.

[17] Y. Vincent Lum, and H. Ling, "An Optimization Problem in the Selection of Secondary Keys," Proc. of ACM 1971 Annual Conference, 349-356.

[18] James Martin, Principles of Data-Base Management. Englewood Cliffs: Prentice-Hall, Inc., 1976.

[19] James Martin, Computer Data-Base Organization. Englewood Cliffs: Prentice-Hall, Inc., 2nd Edition, 1977.

[20] Michael F. Mitoma, and Kelie B. Irani, "Automated Data Base Schema Design and Optimization," Very Large Data Base Conference Proceedings, 1975, pp. 286-321.

[21] Norman H. Nie, et al., Statistical Package for the Social Sciences, 2nd Edition. New York: McGraw-Hill Book Company, 1975.

[22] Richard L. Nolan, "Computer Databases: The Future Is Now," Harvard Business Review, 51, 5 (September-October 1973), pp. 98-114.

[23] F.P. Palermo, "A Quantitative Approach to the Selection of Secondary Indexes," IBM Research, RJ730, San Jose, July, 1970.

[24] Mario Scholnick, "The Optimal Selection of Secondary Indices for Files," Research Report, Department of Computer Science, Carnegie-Mellon University, Nov., 1974.

[25] Mario Scholnick, "A Clustering Approach for Hierarchical Structures," ACM-TODS, 2, 1, (March 1977), pp. 27-44.

[26] H.A. Simon, The New Science of Management Decision. New York: Harper & Row, 1960.

[27] S.B. Yao, "An Attribute Based Model for Database Access Cost Analysis," ACM-TODS, 2, 1, (March 1977), pp. 45-67.

[28] S.B. Yao, and A.G. Merter., "Selection of File Organization Using an Analytical Model," Very Large A Data Base Conference Proceedings, 1975, pp. 255-267.
