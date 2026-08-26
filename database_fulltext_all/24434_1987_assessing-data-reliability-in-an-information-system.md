---
otero_id: 24434
otero_key: "TCQCMEJ2"
title: "Assessing Data Reliability in an Information System"
authors: "Nachman Agmon; Niv Ahituv"
year: "1987"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1987.11517792"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Assessing Data Reliability in an Information System

## Nachman Agmon & Niv Ahituv

To cite this article: Nachman Agmon & Niv Ahituv (1987) Assessing Data Reliability in an Information System, Journal of Management Information Systems, 4:2, 34-44, DOI: 10.1080/07421222.1987.11517792

To link to this article: http://dx.doi.org/10.1080/07421222.1987.11517792

![](/api/attachments/TCQCMEJ2/fulltext/images/80b73a4a0c4159b3e37e505294d3dd782d0faab8e51105490a10468176b29b07.jpg)

Published online: 23 Dec 2015.

![](/api/attachments/TCQCMEJ2/fulltext/images/64662a7d763ad682e14383db3ef3f45328ae40c8606fdd7694791682cc62f8b7.jpg)

Submit your article to this journal ↗

![](/api/attachments/TCQCMEJ2/fulltext/images/b13a2416d1374db969c6df5d71b0caa256d2ccb3010e49e4d11f5d335853b793.jpg)

View related articles ↗

![](/api/attachments/TCQCMEJ2/fulltext/images/17cd4998aa214cf4b68e478f4898a43b5d081bddc99e4dd93163fa3935c7e38b.jpg)

Citing articles: 3 View citing articles ↗

# Assessing Data Reliability in an Information System

NACHMAN AGMON and NIV AHITUV

NACHMAN AGMON received an M.Sc. degree in Computers and Information Systems from Tel Aviv University (1985), where he specialized in the field of data reliability. His B.Sc. degree is in industrial engineering and management from Tel Aviv University. Mr. Agmon has long practical experience in the information systems industry. He specializes in planning and control of management information systems and management support systems, particularly in the field of personnel management. He has published and lectured in many professional conferences.

NIV AHITUV is an Associate Professor and Chairperson of the Computers and Information Systems Program at the Faculty of Management, Tel Aviv University. He has also taught at the University of Calgary, Claremont Graduate School, the University of British Columbia, New York University, and the Technion-Israel Institute of Technology and has managed the data processing department at the Bank of Israel. He holds degrees of B.Sc. in mathematics and M.B.A., M.Sc., and Ph.D. in information systems. His articles appeared in Computers and Operations Research, the Computer Journal, Information and Management, MIS Quarterly, Interfaces, Decision Sciences, the Journal of Systems Management, and others. He is a member of the editorial board of Human Systems Management. He has co-authored a book, Principles of Information Systems for Management. His main areas of interest are economics of computers, information economics, and information systems management and development.

ABSTRACT: Information is valuable if it derives from reliable data. However, measurements for data reliability have not been widely established in the area of information systems (IS).

This paper attempts to draw some concepts of reliability from the field of quality control and to apply them to IS. The paper develops three measurements for data reliability: internal reliability—reflects the “commonly accepted” characteristics of various data items; relative reliability—indicates compliance of data to user requirements; and absolute reliability—determines the level of resemblance of data items to reality.

The relationships between the three measurements are discussed, and the results of a field study are displayed and analyzed. The results provide some insightful information on the “shape” of the database that was inspected, as well as on the degree of rationality of some user requirements. General conclusions and avenues for future research are suggested.

KEYWORDS AND PHRASES: Data reliability, quality control of information systems, data validity.

## 1. Introduction

EVALUATION OF INFORMATION SYSTEMS (IS) usually centers on the benefits of the information to a user who is normally a decision maker who must rely on the information for his or her decision-making process [1]. A prerequisite for the information to be trustworthy is the validity of the data from which the information derives. This issue of data reliability, however, has traditionally been left to data processing (DP) practitioners (for earlier academic works, see [8, 12]).

Theoretical studies in is distinguish between data and information by stating that data are “objective” descriptions of facts [11], whereas information is the “subjective” interpretation of data in the view of a particular decision maker. This distinction is illustrated in Table 1.

For data to become information, some conditions must be met $[3, 7, 15]$ : the data should be meaningful and understandable; they should be relevant to the decision problem; they should be perceived by the decision maker as serving his or her objectives; they should be accessible.

Even when all these conditions have been satisfied, there still remains the question of data reliability (DR), namely, can we believe in the data? An assessment of DR should, in fact, precede any examination of the above conditions; for instance, had the actual age of the applicant (in Table 1) been 14 rather and 40, the attitudes of all three decision makers would have changed. Nevertheless, an assessment of DR can be made only if an operational measurement for DR is available.

This is, in fact, the major issue of this paper. It will propose three measurements for DR, describe the relationships between the three measurements, and summarize the findings of a pilot field study that was performed to validate the proposed measurements.

The next section discusses the general concept of reliability as adhered to in industrial engineering and examines whether it is possible to tie the general concept of reliability to 1s. Section 3 presents some factors typifying the reliability of data. Section 4 suggests three measurements for DR and hypothesizes the relationships among them. Section 5 presents the results of an empirical study. The last section provides some conclusive remarks.

## 2. Reliability

THE ORIGIN OF THE CONCEPT of reliability was in industrial engineering, or, more specifically, in the field of quality control. Robertson [13] defined reliability as the ability of a product to function successfully under required conditions for a predesignated period. Vaughn [14, p. 198] added the notion of probability and defined reliability as “the probability of function within certain specified limits for a required length of time under given environmental conditions."

Table 1 Distinctions between Data and Information

<table><tr><td>Datum</td><td>Decision maker</td><td>Interpretation</td></tr><tr><td rowspan="3">Temperature is 32°F (0°C).</td><td>1. Israeli</td><td>Very cold weather</td></tr><tr><td>2. Mid-west farmer</td><td>Not-so-bad weather</td></tr><tr><td>3. Inuit</td><td>Warm weather</td></tr><tr><td rowspan="3">Applicant is 40 years old.</td><td>1. High school principal</td><td>Too old to be admitted</td></tr><tr><td>2. Chairperson of a Ph.D. program</td><td>Mature but reasonable</td></tr><tr><td>3. Senior-citizen dwelling manager</td><td>Too young</td></tr><tr><td rowspan="3">Military rank of an officer is major.</td><td>1. Novice soldier</td><td>Very high officer</td></tr><tr><td>2. Another major</td><td>A colleague</td></tr><tr><td>3. 3-Star general</td><td>‘One of those majors’</td></tr></table>

The reliability concept is not limited only to individual items, but is also applicable to a whole system $[5]$ . Common measurements of reliability are mean time between failures (MTBF) and mean time to failure (MTTF). The former measures the average time between two consecutive failures, while the latter accounts for the time elapsing from the beginning of operation to the detection of the first failure $[5]$ .

Kivenson [10] proposed an empirical method to assess reliability: let $N_{t}$ be the number of items tested over a period t, and suppose $N_{f}$ items have failed. Assuming the sample is sufficiently large, then the probability of a failure, $P_{f}$ , is $P_{f} = N_{f}/N_{t}$ . The reliability, R, is defined as $R = 1 - P_{f}$ , namely, the probability of success.

When one attempts to apply these concepts to is, a number of questions immediately arise. First, data are meant to capture reality and to reflect facts occurring in the environment $[9, 11]$ . Hence, a data item that has been recorded can be either correct or erroneous, so the concept of MTTF is not very adequate. Second, an erroneous data item remains so forever, unless replaced by a new, correct item; hence the possibility of applying the concept of MTBF is questionable. Similar arguments hold for the definition of reliability during a “test period” (i.e., the definition of R above); there is no test period after which one would tolerate errors. Data should remain correct forever (or at least for a very long time).

Despite these reservations, the above concepts do contribute to the understanding of the notion of DR, particularly with the introduction of probability into the analysis. Of great importance is the definition of R; it provides a measurement for the resemblance of data to reality (see also [2]), and this can be useful even when the time dimension (i.e., test period) is neutralized. We shall make use of the R measurement later in this paper.

The next section characterizes the unique traits of data that should be taken into account when reliability measurement is considered.

## 3. Traits of Data

THE ANCIENT BIBLICAL WRITERS used to adjoin data and their corresponding titles. For instance, one finds in the Bible records such as “thirty horses,” “two hundred soldiers,” and “fifty nuggets of gold,” rather than flat files such as $\{30, 200, 50\}$ separated from their entities which are $\{horse, soldier, gold nugget\}$ .

In computers, data typically are divorced from their meanings. Measuring DR primarily depends on the ability to cross-refer data to corresponding titles. For example, the figure 10,000 makes sense when it is associated with the balance of a savings account of a university professor; it is inconceivable if it describes the number of golden nuggets the professor possesses.

It is common in is to distinguish between four levels of data validation $[2, 4]$ depending on the profundity of the validation check. The four levels are: validity of an individual data item, relationships among items in an individual record, relationships among items in several input records, and relationships between new data and existing files. These four levels can be grouped into two major categories: self-validity and relative validity. Self-validity depends only on the relationship between the datum and its title; for example, 3 students is a valid datum; AB3 students is not. Relative validity examines relationships between various data items. Many types of relationships may exist:

1. Redundancy: the same fact is expressed by more than one data item; for example, the name of a professor is stored in the payroll database as well as in the file of courses currently offered.

2. Complementariness: two (or more) items complement each other; for example, if a student name is mentioned in the list of graduates of a certain program and the same name was written in the list of students enrolled to that program, it is assumed that the person has been participating in the program.

3. Contradiction: two (or more) items are inconsistent; for example, a widow has been divorced.

4. Indifference: two (or more) items do not relate to each other; for example, employee A was hired, and employee B was promoted.

5. Ambiguity: the dependency between data items is not clearly defined; for example, an employee whose gender is “male” and whose marital status is “single” has a new child.

The reliability of a database should be examined in light of all the above conditions. The conditions are set by users in order for the database ideally to reflect reality. Reality, however, is not necessarily defined in a rigorous manner, and this, in turn, may reflect on the definition of reliability. These problems are discussed in the next section.

## 4. Reliability Assessment

ALONG THE PROCESS of recording reality onto computer-readable media there are a number of points that might introduce distortions. First, the means of recording might lack the required sensitivity to the variety of pertinent facts. For example, it took a long time for many organizations to redesign their forms to accommodate the five classes of marital status; the traditional forms allowed for “single,” “married," "divorced," and "widow(er)," whereas only recently has the "separate" status been added. In such cases, a distortion occurs as soon as one wishes to record a fact that is not provided for by the recording medium.

Another cause of distortion emerges from disparity in the ways different users perceive factual data. For example, a record indicating that a certain person has more than one spouse will not be perceived as valid in many societies; however, there are places where such data will not raise eyebrows.

Consequently, the criteria by which data reliability is assessed are not rigid. They do depend on the particular users who set them, and they may have to adapt to the dynamics of the perception of reality. It is proposed, therefore, to assign three measurements to DR: internal reliability, relative reliability, and absolute reliability. We shall soon define these three measurements; however, we should like first to propose a general formula for reliability assessment.

Let N be the number of data items in a database, and let $N_{r}$ be the number of correct items in the database. Then the reliability R is defined as $N_{r}/N$ . The term “reliability” here holds for any of the above three measurements. The distinction between them is based on a different definition of the notion “correct”; in other words, the value of $N_{r}$ may vary. Note that the definition is similar to the one presented in Section 2, except that here we do not account for the time dimension. Note also that the definition is based on an implicit assumption that the data items possess the same value to the user; that is, the “worth” of each correct datum is the same (otherwise, a weighting function should be introduced; it is omitted here for simplicity [2]).

The three distinct measurements of DR are defined as follows:

1. Internal reliability: Reliability whose assessment is based on commonly accepted criteria (universal criteria) about the characteristics of the data items.

Notation: $R_{\mathrm{I}}$

Examples: Quantities of items in a warehouse may not be negative; “salary” cannot contain alphabetic characters; “day-of-the-month” may not exceed 31.

Explanation: $R_{I}$ is measured by employing criteria that do not have to rely on user requirements, nor are they modified over time. They are inherent to the titles and nature of the data; they are universal and almost “eternal.” A computerized system can be programmed to validate the compliance of the data to these criteria without anyone having to interrogate users about their perception of reality.

2. Relative reliability: Reliability of the data in view of the user requirements.

Notation: $R_{\mathbb{R}}$

Examples: The manager of a warehouse is not prepared to tolerate records that lack some of the fields, for instance, a vendor name; consequently, every record whose data are incomplete is rejected even if most of the data items are correct. A company policy is to hire programmers who are at least college graduates; therefore, when an employee record shows that his or her position is “programmer” but the record does not indicate a possession of an academic degree, the record is assumed to be erroneous.

Explanation: $R_{R}$ is measured by comparing the data to the requirements imposed on the database by the users. In other words, users have certain perceptions of reality, or what they believe reality should look like. Their beliefs and values dictate how $R_{R}$ is assessed. Therefore, $R_{R}$ is a subjective assessment whose value derives from users' views and organizational policies that are imposed on the database content. (Note that $R_{R}$ is not in contradiction to $R_{I}$ ; we shall discuss later the relationships among the three measurements.)

3. Absolute reliability: Reliability which is measured by performing direct comparisons between the content of the database and reality.

Notation: $R_{\mathrm{A}}$

Examples: Count the number of items in a warehouse and compare the results to the balances recorded in the inventory control system. Read the names of all the students present in the classroom and check whether all the names are indeed recorded in the class list.

Explanation: $R_{A}$ is measured by observation. The auditor who wishes to measure it deliberately disregards all the data validation routines and turns back to the origin of the data, reality. Measuring $R_{A}$ is not always feasible and is likely costly, but it will certainly provide the best evaluation of DR.

It appears that there must be some relationships among the three measurements of DR. Relative reliability $(R_{\mathrm{R}})$ is more demanding than internal reliability $(R_{\mathrm{I}})$ since it imposes user requirements on the data items in addition to the technical (universal) characteristics that are commonly accepted by almost all the users. Hence, it is expected that, for a given database, the relationship $R_{R} \leq R_{I}$ will prevail.

Unlike $R_{R}$ and $R_{I}$ , which are measured by inspecting only the database itself, absolute reliability ( $R_{A}$ ) is obtained through comparisons of the database with reality. It is likely that such comparisons will reveal more discrepancies than any inspection limited only to the database. For example, a balance of 3 items will be found wrong only by visual inspection; the computer can tell only that “3” is a valid character. Hence, it is expected that $R_{A}$ will yield a lower (worse) ratio than $R_{R}$ (and $R_{I}$ as well). In summary the following multiple relationship is expected to prevail:

$$
R _ {\mathrm{A}} \le R _ {\mathrm{R}} \le R _ {\mathrm{I}}
$$

These had been our expectations prior to conducting the field study. Some of the expectations were later refuted. This is discussed in the next section.

## 5. Field Study

EACH OF THE THREE reliability measurements has to be assessed in a different manner. Internal reliability is computed by running a program that replicates the validity checks usually performed on the input data to weed out errors occurring during recording and keying; for example, numerical data should not include alphabetic characters, and “month” should not exceed 12.

Relative reliability is assessed in a similar fashion. However, the program that is employed checks for a larger set of conditions; for example, the time elapsing between the occurrence of a transaction and its recording in the database should not exceed four working days, and a change in marital status from single to widow is not acceptable.

Absolute reliability is obtained by observing the population whose data are recorded in the database. Computer printouts are to be compared with reality by sending questionnaires to the pertinent parties and asking them to verify the content of the enclosed printouts. If the population is very large, a sample should be taken. The statistical distribution pertaining to such cases is binomial (the data item is either right or wrong); however, for a sufficiently large sample an approximation to normal distribution may be applied [6]. Consequently, one can obtain not only $R_{A}$ , but also a confidence interval.

A possible problem in a field study is that various data items might be subject to different requirements and characteristics entailing different levels of reliability. For instance, the item “Social-Security-Number” is almost untouched once it has been keyed in; the item “salary” may be subject to a number of updates. It is not advisable to check the reliability of one of them and deduce anything about the reliability of the other. However, checking the reliability of all the variety of data items might be very costly in large databases. It is therefore recommended to select a few items that represent the characteristics of all the others (for a discussion on information attributes, see [1]).

For the sake of this research, we have conducted a pilot field study on a very large personnel database (more than 100,000 records). The database belongs to a large organization distributed over many locations; nevertheless, the database is centralized and is updated daily by transactions arriving mostly in batch but also in on-line mode.

Two data items were selected for reliability assessment: the location of employee and his or her health status (this is indicated by a set of numerical codes). The two items are highly distinct in terms of update frequency: on the average there are 810 daily update transactions of employee-location, compared to an average of 153 daily transactions of health-status. This was the main reason for selecting these particular data items, since the major criterion into which we wished to inquire was compliance to the user requirements regarding the currency of the data [1]. We had assumed that a significant difference in update frequency would affect the relative reliability associated with currency level.

The internal reliability was measured by means of a computer program that scanned the two data items through the entire database. The program was written ad hoc for this research by employing a report generator software package. The results were:

$$
\begin{array}{r} {R _ {\mathrm{I}} (\text { employee - location }) = 98.34 \%} \\ {R _ {\mathrm{I}} (\text { health - status }) = 99.94 \%} \end{array}
$$

The relative reliability was checked against only one user requirement—that an update shall not be deferred for more than four days from the time a pertinent event occurs. This was inspected by an ad hoc computer program (using, again, a report generator package) that compared the transaction date to the update date over the entire database and flagged out differences of more than four days. The results were:

$$
\begin{array}{r} R _ {\mathrm{R}} (\text { employee - location }) = 5 9. 7 9 \% \\ R _ {\mathrm{R}} (\text { health - status }) = 1 3. 5 0 \% \end{array}
$$

(this is not a typographical error!)

The absolute reliability was assessed by a random sample of 2% of the population. A computer printout showing the database content on each member of the sample was mailed to the sample population. The participants were asked to verify it. The response rate was 75%. The results were:

$$
R _ {\mathrm{A}} (\text { employee - location }) = 94.20 \%;
$$

confidence interval at 5% significance level was 93.22%–95.18%

$$
R _ {\mathrm{A}} (\text { health - status }) = 98.50 \%;
$$

confidence interval at 5% significance level was 98.24%–98.76%.

Table 2 summarizes the findings.

It is clear that the internal reliability $(R_{I})$ is higher than any other reliability for both data items. This finding was expected and is easily explained by the fact that internal validity checks are less inclusive than any other check because the criteria are limited to technical features.

Another observation that can be intuitively understood is the difference in the values of $R_{I}$ between the two data items; the value measured for health-status was higher than the value measured for employee-location. This is due to the different update frequencies; the higher the frequency, the more likely the associated data item is to be “polluted.” Similar arguments explain why $R_{A}$ of employee-location is worse than that of health-status.

Table 2 Field Study Results

<table><tr><td>Data item</td><td>Average daily updates</td><td> $R_I$ </td><td> $R_R$ </td><td> $R_A$ </td></tr><tr><td>employee-location</td><td>820</td><td>98.34%</td><td>59.79%</td><td>94.20%</td></tr><tr><td>health-status</td><td>153</td><td>99.94%</td><td>13.50%</td><td>98.50%</td></tr></table>

In contrast to these findings, the values for relative reliability $(R_{\mathrm{R}})$ are apparently incomprehensible. Three questions arise:

1. Why are the figures so low in comparison with the others?

2. Why is the relative reliability of employee-location better than that of health-status?

3. Why is $R_{\mathbb{R}}$ worse than $R_{\mathrm{A}}$ ?

The answers to the three questions were provided only after the findings underwent a thorough investigation. It was discovered that the user requirement of updating the database within four days from the occurrence of an event is beyond the capacity of the persons who operate the system. Consequently, many of the transactions came in late, thus decreasing the relative reliability of the data (recall that $R_{R}$ reflects the subjective view of the users).

The answer to the second question lies in the disparity between the processes of generating input for the two types of transactions. A change in an employee-location is usually recorded on a simple form after a relatively straightforward process terminating when the employee reports to a clerk at the new location. Since the organizational policy puts much emphasis on the need to know where each individual is located, the clerks are overly instructed to rush the input data for prompt data entry. This is certainly not the case when a change in health-status occurs. Such a change involves a prolonged procedure culminating in a committee decision and producing a number of involved forms. A prompt submission of forms for keying-in is not perceived as imperative by the pertinent personnel. This in our opinion explains why $R_{R}$ of health-status falls behind that of employee-location.

The answer to the third question was quite simple. It took some time for the questionnaires to be mailed and then to be filled out. During that time, updates were made, so the computer printouts had already managed to reflect reality. The respondents had to verify only the facts described in the printouts; they were not asked to comment on the time it took to update the database. Therefore, in most cases their responses confirmed that the data were indeed accurate.

A direct conclusion deriving from the above findings is that the requirement of four days from event occurrence to file update does not seem feasible. User management may either relax this requirement or enhance the system so that it will be able to comply to it. Enhancement can be achieved by adding personnel, adding input facilities, short-cutting manual procedures, and, most of all, providing guidance and control.

The next section provides more general conclusions.

## 6. Conclusions

THIS PAPER SUGGESTED three measurements to assess data reliability. Internal reliability indicates whether the data conform to commonly accepted criteria of validity. It is measured by screening the data through a validation program. Relative reliability reflects compliance with user requirements. It is much more subjective than the other measures; it derives from organizational policies and practices. It can be measured by means of a computer program. Absolute reliability examines how closely the data represent reality. It is obtained through observation and sampling.

A field study has demonstrated that obtainment of the three measurements is feasible. The findings can be of great value to users as well as to the information system department. The importance of the findings is twofold: First, the value of each individual measurement carries information of note to the interested parties. If it is too low, it implies that some procedures are ill designed or improperly controlled. For example, low internal reliability reflects poor quality of the input validation routines; low relative reliability indicates noncompliance with user requirements; low absolute reliability identifies deficiencies in the process of data recording and keying-in.

The second benefit of the three measurements lies in comparative analysis of the results. The a priori expectations are that $R_{A} \leq R_{R} \leq R_{I}$ . If these relationships do not hold true, as was the case in the pilot study, it would imply that something went wrong in the operationalization of user requirements. This may imply that the requirements are not realistic, that they have been misunderstood, or that control is not adequately exerted.

Even when the initial expectations are satisfied, the gaps between the three values must be examined. If they are too large, it is likely that some activities in the process of data recording-keying-validation-storing-updating-securing are malfunctioning.

Future research in this area should concentrate on a number of issues: refining the reliability measurements, establishing permanent measurement tools, honing the process of deducing conclusions from the reliability values, and devising a model for analyzing reliability over time.

## REFERENCES

1. Ahituv, N. A systematic approach toward assessing the value of an information system. MIS Quarterly, 4, 4 (December 1980), 61–75.

2. Ahituv, N. A theoretical framework for cost/benefit analysis of data entry and validation systems. Proceedings of the 3rd Annual International Conference on Information Systems. Ann Arbor, Michigan, December 1982, 47–55.

3. Ahituv, N.; Munro M. C.; and Wand, Y. The value of information in information analysis. Information and Management, 4, 3 (July 1981), 143–150.

4. Ahituv, N., and Neumann, S. Principles of Information Systems for Management. 2nd ed. Dubuque, Iowa: W. C. Brown, 1986.

5. Anderson, T., and Lee, P. A. Fault Tolerance. Englewood Cliffs, N.J.: Prentice-Hall, 1981.

6. Clelland, R. C.; Decanti, J. S.; and Brown, F. E. Basic Statistics with Business Applications. New York: Wiley, 1973.

7. Foy, N. S. Computers and Commonsense. London: Longman, 1972.

8. Gilb, T. Reliable Data Systems. Oslo: Universitetsforlaget, 1971.

9. Kent, W. Data and Security. Amsterdam: North Holland, 1978.

10. Kivenson, B. Durability and Reliability in Engineering Decision. New York: Hayden, 1971.

11. Langefors, B., and Samuelson, K. Information and Data in Systems. New York: Petrocelli-Charter, 1976.

12. Mace, D. R.; Crowe, T.; and Jones, J. H. The econometrics of data validation. Management Datamatics, 5, 2 (April 1976), 65–72.

13. Robertson, A. G. Quality Control and Reliability. London: Thomas Nelson, 1971.

14. Vaughn, R. C. Quality Control. Iowa: Iowa State University Press, 1974.

15. Yamatoku, Y. A conceptual framework for the quality of information. Working paper, Faculty of Science, Konan University, Kobe, Japan, 1977.
