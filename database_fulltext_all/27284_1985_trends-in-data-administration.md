---
otero_id: 27284
otero_key: "BBSN7TRF"
title: "Trends in Data Administration"
authors: "Mark L. Gillenson"
year: "1985"
journal: "MIS Quarterly"
doi: "10.2307/249232"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Trends in Data Administration
Author(s): Mark L. Gillenson
Source: MIS Quarterly, Vol. 9, No. 4 (Dec., 1985), pp. 317-325
Published by: Management Information Systems Research Center, University of Minnesota
Stable URL: http://www.jstor.org/stable/249232

Accessed: 25/06/2014 09:55

Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at http://www.jstor.org/page/info/about/policies/terms.jsp

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

# Trends in Data Administration

By: Mark L. Gillenson
IBM Systems Research Institute
205 East 42nd Street
New York, New York

## Abstract

The field of data administration originated as an adjunct to the expanding use of database management systems. With the increasing amount of data that data processing personnel are faced with managing, and the realization that data is an important corporate resource, the concept of data administration has continued to evolve and change. At several points in time over the last few years field surveys have been conducted to determine the state of practice of the data administration function. Using data derived from those surveys (and emphasizing the two which were conducted by this author) as well as empirical evidence, this article traces the development of the concept of data administration, concentrating on the period from 1981 to 1985.

Keywords: Database, data administration, data dictionary, database administration.

ACM Categories: H.2.7, K.6.0.

## The Data Administration Concept

In the mid-1960s, the increasing volumes of data in data processing systems sparked an interest in the development of more efficient ways to store and retrieve that data. By the 1970s those increases became explosions, and the concept of the database management system (DBMS) came into popular use. During the first half of the 1980s the use of DBMSs expanded as part of a natural increase in the sophistication of the data processing environment. One realization in that increasing sophistication is that the use of a DBMS is only one aspect of the management of data. On a much broader scale the management of data today implies treating an organization's data as a true corporate resource which must be managed as such. The term associated with that function is “data administration.”

The original work in this area [5, 6, 7] was done by the IBM users' group known as GUIDE. According to GUIDE, data administration (DA) is the name given to the top level function or department that manages data. In theory this includes all of an organization's data, but in practice it involves primarily the data accessible by the database management system.

According to GUIDE, data administration is made up of two components which may or may not be organized as subordinate departments. One of those components, data management (DM), is primarily a planning and analysis type of function. It may be responsible for data planning, accountability, training, policy development, standards setting, database design, and liaison support to application development groups. Data management personnel are often taken from the ranks of systems analysts or programmers, and are referred to as “data analysts.”

The other subordinate department, database administration (DBA), is responsible for managing the data on a day-to-day, operational level. Its responsibilities may include performance monitoring, troubleshooting, security monitoring, control block generation, coordination of database activities with systems programming and operations personnel, database design, and liaison support to application development groups. Database administration personnel are former programmers, usually systems programmers, and are often called database systems programmers.

## Data Administration Surveys

The earliest attempts at creating distinct functions that we might today call data administration date back to the late 1960s. However, growth of the concept was slow and was confined to very large data processing organizations that were early users of DBMSs. Early surveys in the field [2, 10, 11, 13, 14, 15, 16] found the typical data administration group to be quite new in the organization, to have only a few employees (5 or fewer was common), and to be placed low in the hierarchy of departments within the data processing function. Also, it was found to have responsibility for immediate technical concerns of the database management system environment, as opposed to more global concerns about data in the organization in general (“database administration” vs. “data management” in GUIDE terminology).

## The 1981 Survey

In early 1981 we undertook an extensive survey among the account systems engineers of IBM's database software customers [3, 4]. The database management systems involved were Information Management System (IMS), used in larger computer systems, and Data Language/I (DOS DL/I), used in medium sized systems. Most of the remarks to follow will pertain to the larger, IMS environments. The user organizations ran the gamut from manufacturing firms of all product types, to banking, insurance, and brokerage firms, service and transportation concerns, and government data processing departments. While only one DBMS (in two implementations) was involved in the study, we feel strongly that the key issue was large scale management of data, not the technical differences between hierarchical and network DBMSs (which were all that were available at that time). As Munzenberger noted in discussing the results of his survey [13] which did involve different vendors' DBMSs, "No direct relation could be identified between the package being used and the size of the DBA staff or the range/type of tasks."

The 1981 survey, from which we received 581 returns, was divided into three sections: database and data processing background, data administration, and data dictionary. The returns were categorized by system type (IMS or DOS DL/I) and communications driver (IMS/DC or CICS), and by whether the respondent felt that the data administration function, as it was organized, was successful.

We found a generally strong and increasing commitment to the database concept. When asked to estimate the percentage of the installation's “computing activity” done using IMS, the large systems respondents replied 27%, with a projected increase in one year to 37%. In that same group, those shops that considered themselves successful reported average daily IMS transaction rates approaching and breaking the 100,000 mark within that year. In terms of size, there were many reports of single databases well into the millions of records.

Data administration departments were present in 84% of the large system environments and in 42% of the medium sized ones. Across the board, about three-quarters considered themselves either successful or partially successful in improving their company's data processing efficiency (most of the rest were undecided). The average DA department in the large systems environment had seven people in it, including one manager, and had been in existence for four years. The most common job categories were data analyst and database systems programmer. The largest group had seventy-five people in three levels of management, and some of the groups dated back to the late 1960's. Where there were several groups they were usually split along the lines of database administration, data management, and, occasionally, data dictionary groups. Typically the department manager had come from a programming or systems analysis background. In most cases the database management system had been in place before the DA department was formed.

In 90% of the cases there was one DA department for the company or the division of the company being surveyed. Almost half of those departments were placed two levels of management down from the chief data processing officer and reported to a technical services or support manager. In the larger multi-division or multi-site companies, there were situations of several DA departments on a one per division or one per site basis. In some cases they operated independently; in other cases they either reported to or took guidance from a higher level corporate DA group.

As for responsibilities, among the large systems respondents 14% said that they were responsible for data in other database management systems in addition to the data in IMS, and 24% indicated responsibility for flat-file data. Over 80% strictly controlled the IMS environment. Sixty-seven percent were involved in performance tuning, but only 34% installed new releases of IMS, implying that the systems programming department retained some responsibility in the IMS area. Over 90% served as liaison to application development groups in matters concerning data and database design. Most managed the data dictionary, if one was present. More than half were involved with matters such as education, security, and backup and recovery.

A very interesting point concerned long range planning. The questionnaire asked about current and future responsibilities. While only 41% indicated that they were then involved in long range planning, 18% said that they hoped to get involved with it in the future. That 18% was the single largest response for additional future activities of any of the activity categories. While the DA departments spent most of their time working on the day-to-day activities associated with database administration, many were hoping to move toward data management activities in the future.

There was a check-off type question which asked about problems that the DA groups might have been experiencing. About 40-50% of them checked too heavy a workload, responsibilities without the corresponding power, resistance by other departments to changing job responsibilities, lack of management support, the DA function not being placed high enough in the data processing hierarchy, and resistance by others to data sharing. In fact, the only questions not marked frequently were lack of responsibility and inadequate salary schedules. Additionally, several people wrote in that they were understaffed, that it was hard to find qualified staff, and that there was a fundamental lack of understanding on the part of management of the data administration concept.

As for major directions, many DA groups hoped that their responsibilities would increase with time. Many also expected new or increased use of a data dictionary. Others expected an increase in database activity, including more data sharing, and that the DA group would move from a database administration posture to more of a true data administration orientation.

In analyzing the results of the survey, it was tempting to try to characterize what made some DA departments successful and others not. That was not possible. It is clear that any implementation of the concept of data administration must be tailored to the technical and political realities of the individual firm. As a general rule we did find that the successful DA departments tended to be larger, older, have more responsibilities, be associated with higher daily database transaction rates and have fewer complaints. The conclusion that we drew, in that regard, was that there appeared to be a learning curve associated with the development of DA functions. It takes a certain period of time for a new DA group to develop skills and to gain the confidence of management, users, and other people in the data processing organization before it can realize a significant potential.

## The 1983 Follow-Up Survey

In most fields, two years would seem like too short a period of time to detect broad and significant managerial changes. But the rapid changes occurring in the use of computers in general, and the fact that the 1981 survey found the average data administration department to be only four years old, made it important to look into the changes that had taken place in data administration over the two year period from 1981 to 1983.

In May 1983, we conducted a telephone follow-up of the survey with the IBM systems engineers associated with forty of the original respondents.

Almost all of those forty DA groups were from the large systems category. We reviewed the entirety of the survey form with them, reminding them of the original responses, and asking them about the current state of affairs.

As shown in Table 1, we found a marked increase in database activity as measured by the volume of daily IMS transactions.

There is an interesting point to be made in comparing the increases in the number of IMS transactions per day with the increases in the amount of IMS activity as a percentage of the total computing activity. While one has to be careful about the inferences drawn in comparing two different (albeit related) sets of statistics, we developed a strong feeling in talking to the systems engineers that the marked increases in the

Table 1. Change in Daily IMS Transaction Rate

<table><tr><td>Number of Groups</td><td>Change in Volume of Daily IMS Transactions</td></tr><tr><td>5 (14%)</td><td>300% Increase</td></tr><tr><td>8 (22%)</td><td>200% Increase</td></tr><tr><td>9 (24%)</td><td>100% Increase</td></tr><tr><td>8 (22%)</td><td>50% to 100% Increase</td></tr><tr><td>5 (14%)</td><td>Small Increase</td></tr><tr><td>1 (3%)</td><td>Same</td></tr><tr><td>1 (3%)</td><td>Decrease</td></tr><tr><td>37 responding</td><td></td></tr></table>

Most reported that the number of databases had increased over the two year period. One third indicated that the size of the largest database in the installation had further increased. Eighteen percent said that IMS progressed from sharing a CPU with other work to having a CPU dedicated to it. Several reported an increase in the use of such IMS facilities as logical relationships and secondary indexes.

There was a rather broad question which asked about the amount of IMS activity as a percentage of the total data processing activity in the installation. Table 2 shows the changes that took place.

numbers of IMS transactions per day were not matched by the increases in the amount of IMS activity as a percentage of the total data processing activity. In fact, five of the respondents to this follow-up survey specifically remarked that while the amount of activity involving IMS had increased, the rate of increase of other computing activities (for example APL and fourth generation languages) had been proportionately greater.

Changing the focus to the data administration groups themselves, it was clear that their growth was well below the growth rate of the databases, as shown in Table 3. That may seem like comparing “apples to oranges” at first glance, but it is significant. One might infer that increased proficiency and efficiency among the DA personnel, coupled with increasing stability of the growing databases, allowed the same number of people to handle much larger amounts of data.

Table 2. IMS as a Percentage of Total Data Processing Activity

<table><tr><td>Number of Groups</td><td>Change in Amount of IMS Activity</td></tr><tr><td>3 (8%)</td><td>300% Increase or More</td></tr><tr><td>4 (11%)</td><td>200% Increase</td></tr><tr><td>5 (14%)</td><td>100% Increase</td></tr><tr><td>2 (6%)</td><td>50% to 100% Increase</td></tr><tr><td>10 (28%)</td><td>0% to 50% Increase</td></tr><tr><td>8 (22%)</td><td>Same</td></tr><tr><td>4 (11%)</td><td>Decrease</td></tr><tr><td>36 responding</td><td></td></tr></table>

Table 3. Size of Data Administration Group

<table><tr><td>Number of Groups</td><td>Change in Size of DA Group</td></tr><tr><td>2 (6%)</td><td>250% Increase</td></tr><tr><td>2 (6%)</td><td>100% Increase</td></tr><tr><td>2 (6%)</td><td>75% Increase</td></tr><tr><td>5 (14%)</td><td>50% Increase</td></tr><tr><td>3 (8%)</td><td>25% Increase</td></tr><tr><td>17 (47%)</td><td>Same</td></tr><tr><td>3 (8%)</td><td>0% to 50% Decrease</td></tr><tr><td>2 (6%)</td><td>Greater than 50% Decrease</td></tr><tr><td>36 responding</td><td></td></tr></table>

Other DA function factors remained largely unchanged. Such indicators as perceptions of success in the data administration approach, responsibilities of the DA groups, and DA group structure and placement in the data processing organization, all remained about the same.

At the same time there was some small positive movement in terms of the problems that the DA departments faced (Table 4), although it must be emphasized that in most groups the problems remained the same. The one exception to that was the substantial improvement shown in management support for the data administration concept. The systems engineers who mentioned that in the telephone survey went out of their way to emphasize the point, which speaks well of the improved perception of value of the data administration concept.

By 1983 the surveyed DA groups were six years old on the average, and were still in a period of organizational experimentation. Some modifications were reported in the follow-up survey. One group's reporting path was changed from application development to systems programming. In a couple of cases responsibilities were shifted between the database administration and data management subfunctions. In two companies, DBA-type personnel were added to application development groups to work full time on a particular application. There were cases of separate DA groups being consolidated, and cases that represented just the opposite; a DA group being split into smaller units, either along functional or along geographic lines. There was one situation where database performance responsibility was moved from the DA group to the technical support group and another in which it was moved to systems programming, but four of the DA groups took on new or increased database performance responsibilities. Two

Table 4. Data Administration Group Problem Improvement

<table><tr><td>Improvement Cited in the Area of:</td><td>% of Original Cases Citing Improvement</td></tr><tr><td>• Too heavy a workload</td><td>13%</td></tr><tr><td>• Lack of organizational power</td><td>13%</td></tr><tr><td>• Resistance by others to changing job responsibilities</td><td>14%</td></tr><tr><td>• Resistance by others to sharing data</td><td>12%</td></tr><tr><td>• Lack of management support for the data administration concept</td><td>30%</td></tr></table>

DA groups increased their activity in long range planning; one decreased such activity. Almost all of these DA groups were involved with a data dictionary to some degree, as they had been in 1981.

## Other Recent Surveys

Two other data administration surveys have been conducted recently. Both involved user organizations in a wide range of business categories and size. Neither had any restriction on the specific DBMS(s) in use in the companies and neither remarked about any differences in data administration based on the specific DMBS in use.

In late 1982, Kahn [9] surveyed the data administrators in a small, non-scientific sample of 56 large companies from a wide range of industries. Unfortunately, her terminology differs from GUIDE's in that she uses the term data administration to mean the higher level, global functions of “establishment and enforcement of policies and procedures for managing the company's data as a corporate resource,” which is essentially what GUIDE called data management. In turn, she uses the term information resource management (IRM) to describe the top level function that GUIDE called data administration.

She found that 48% of the firms had both database administration and data management departments (the combination of which is data administration, returning now to the GUIDE terminology), 24% had database administration only, and 28% had neither. The presence of a data management department seemed to encourage a concern for setting data standards and other higher level data management activities. Confirming our results, she found that larger companies were more likely to have a data management department than smaller ones. On the other hand, her sample seemed to consist of smaller and younger departments than ours, with more reporting directly to the chief data processing officer.

Kahn made an interesting attempt to compare the data administration function's satisfaction of its own success with its actual effectiveness in promoting the concepts of data efficiency. She found that the data administration people considered themselves overwhelmingly successful, although in terms of data management specifically they were more likely to characterize themselves as partially successful. But in “comparing those activities that were identified as being improved as a result of IRM with those that were identified as being performed effectively,” the results showed that only a few activities, including data documentation, consistency, design, and sharing were actually improved. Those and other results in the Kahn study, especially considering the comparatively young and small data administration groups involved, are in keeping with our findings that older and larger data administration groups tend to be more successful.

During 1982 and 1983, the Data Administration User's Group conducted an extensive study of several hundred data administration departments in companies of all size and industry descriptions [1]. Again, there were no limitations on which DMBS was in use. The respondents were divided about equally into groups that were more than 4 years old, between 1 and 3 years old, and less than 1 year old. Forty percent indicated that the function had more than five people in it, with the age of the function positively correlated with the number of people in it. Similar to our findings, about one third of the groups were part of a technical support organization and reported two levels down from the chief data processing officer. There was significant emphasis on the data dictionary and the concept of treating data as a resource.

An interesting aspect of this survey was an attempt to distinguish different perceptions of the functions' success depending on who might be asked the question. It was estimated that among the data administration personnel, 50% felt that it was successful, 33% felt that it was too early to tell, less than 10% felt that it was unsuccessful, and 5% were not sure. Management breakdowns were similar, however 10% were unaware of the existence of the function. Among application development teams, 33% felt that it was successful, 33% too early to tell, 10% moderately unsuccessful, and 5% totally unsuccessful.

Other general comments were derived from this survey. The number one problem complained about in data administration was not enough staff, followed by too heavy a workload and resistance to data sharing. In terms of the uses of a data dictionary, the most important, in order, were as a documentation tool, to generate data specifications in programs, to generate database control blocks, and as a change control tool.

Overall, the survey indicated a lack of commitment from management and a lack of acceptance from the application development community. An interesting comment was that in many companies the major resistance to data planning came from middle management within data processing.

## New Technologies And The Future

Since the early 1970s there has been tremendous growth in the use of databases and database management systems. The implementation of the concept of data administration began on the database administration side and gained with the addition of data management activities. The last two years have been a time of constancy or modest growth in size. It has also been a time of some experimentation in organization and function. But mostly it has been a time of sharpening skills and becoming a more accepted part of the data processing milieu in the eyes of management and the rest of the data processing staff.

Until comparatively recently, the data processing environment that data administration evolved in included hierarchical and network-based DBMSs, traditional application development departments and techniques, and centralized computing power. But the advent and increasing use of relational DBMSs, fourth generation languages, personal computers, and information centers affect all aspects of data processing including data administration. If there is a common thread through those new technologies, it is that they all tend to move the power of the computer to the end user. The question here is how that affects the management of data and the concept of data administration.

Relational databases are increasingly forming the data platform from which end users, often using fourth generation languages as interfaces, can satisfy many of their own information needs without going through the traditional application development process. One of the advantages of relational and fourth generation systems is the ability for an end user to design and populate his own files. But in another sense, this environment demands a serious data administration effort, as pointed out in the commentary that is part of the Data Administration Users Group survey results and in another recent report $[1, 14]$ . If each user attempts to create his own files, the data redundancy and duplication of effort can quickly become serious problems. And if users are to share data there must be a competent, impartial data administration group to plan for, design, and manage that data in all respects. Furthermore, the environment encourages people to make more use of the computing power available which, in turn, means that more and more data is created. Keeping track of all of that data, both from the management and end user standpoint demands the use of a data dictionary and a data administration group to control it.

Personal computers impact on the concept of data administration takes two forms. One is the issue of whether or not data administration should be concerned with any of the data that users are creating on their own and storing on their own diskettes for personal use. The answer, rather clearly, is that today's data administration groups have their hands full trying to manage the large shared databases and cannot possibly worry about what everyone is creating with their PCs.

A related issue involves the downloading of data from a mainframe to a PC. That data may then be modified on the PC, at which point data administration has no control over its accuracy, even though at some later time it may be represented as data that has the stamp of approval of the data administration group. We have observed two ways of trying to manage this situation. One is for the data administration people to keep a log of the events of downloading data from the mainframe to PCs. In that way a record can be kept of the points at which the data was up to the data administration standards before possible modification on PCs. The other is to download the data in a coded form, with only certain PCs having the hardware decoding device necessary to use the data. Control can then be kept to the degree that data administration can limit who has access to the downloaded data (although presumably nothing stops the copying of the data once it has been decoded on the PC).

The information center is the management concept purporting to provide users with easy access to data. But if that activity implies some degree of managing data, how does it relate to data administration's management of data? The only thing clear about that situation is that there is no clear answer. The best solutions we have seen thus far are to have the information center report to data administration, or to have data administration and the information center report to the same manager, perhaps a manager of technical support.

The next few years will be very interesting in terms of the evolution of the data administration concept. The movement of data administration from primarily database administration to a true data administration posture will proceed as a necessary management evolution, prodded by the new technologies that we have discussed. One point is clear; every development now taking place points to the increasing consideration of data as a legitimate and critical corporate resource.

## References

[1] Data Administration User's Group. "Data Administration Survey Report," Bayonne, New Jersey, November 1984.

[2] De Blasis, J.-P. and Johnson, T.H. “Data Base Administration — Classical Pattern, Some Experiences and Trends,” Proceedings of the 1977 AFIPS-NCC, Dallas, Texas, June 13-16, 1977, pp. 1-7.

[3] Gillenson, M.L. “1981 SRI Data Administration Survey Report,” IBM Systems Research Institute, IBM Technical Report TR73-022, New York, New York, June 1981.

[4] Gillenson, M.L. “The State of Practice of Data Administration — 1981,” Com-

munications of the ACM, Volume 25, Number 10, October 1982, pp. 699-706.

[5] GUIDE International Corporation. “Establishing the Data Administration Function,” Chicago, Illinois, 1977.

[6] GUIDE International Corporation. “Data Administration Methodology,” Chicago, Illinois, 1978.

[7] GUIDE International Corporation. “Data Administration in a Distributed Data Environment,” Chicago, Illinois, 1982.

[8] Hammond, L.W. “Management Considerations for an Information Center,” IBM Systems Journal, Volume 21, Number 2, April 1982, pp. 131-161.

[9] Kahn, B.K. “Some Realities of Data Administration,” Communications of the ACM, Volume 26, Number 10, October 1983, pp. 794-799.

[10] McCririck, I.B. A Survey of the Data Administration Function in Large Canadian Organizations, Master's Thesis, University of British Columbia, Vancouver, British Columbia, Canada, June 1979.

[11] McCririck, I.B. and Goldstein, R.C. “What Do Data Administrators Really Do?” Datamation, Volume 26, Number 8, August 1980, pp. 131-134.

[12] Mock, R.E. “Personnel Roles in an IBM Database 2 (DB2) and Query Management Facility (QMF) Environment,” IBM, IBM Technical Report TR 03.246, San Jose, California, 1984.

[13] Munzenberger, H. “Database Administration — Experience from a European Survey,” Proceedings of the European Conference on Evaluation and Implementation of Database Systems, Brussels, Belgium, September 25-26, 1980, pp. 85-94.

[14] Supper, K.O. “The Use of Data Dictionaries: A Survey,” Proceedings of the European Conference on Evaluation and Implementation of Database Systems, Brussels, Belgium, September 25-26, 1980, pp. 29-45.

[15] Weldon, J.-L. “Organizing for Data Base Administration,” Center for Research on Information Systems, Working Paper CRIS 6, New York University, New York, New York, January 1979.

[16] Weldon, J.-L. “The Changing Role of Data Base Administration,” Center for Research

on Information Systems, Working Paper CRIS 7, New York University, New York, New York, November 1979.

## About the Author

Mark L. Gillenson is a senior faculty member of the IBM Systems Research Institute in New York City, where he teaches and consults in systems analysis and computer graphics. He holds a B.S. in mathematics from Rensselaer Polytechnic Institute, and an M.S. and Ph.D. in computer and information science from Ohio State University, and the C.D.P. His books include Strategic Planning, Systems Analysis, and Database Design: The Continuous Flow Approach (with R. Goldberg), 1984, and DATABASE Step-by-Step, 1985, both published by John Wiley & Sons.
