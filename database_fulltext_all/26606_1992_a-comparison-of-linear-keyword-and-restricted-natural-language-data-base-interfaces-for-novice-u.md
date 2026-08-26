---
otero_id: 26606
otero_key: "9N9HBUWX"
title: "A Comparison of Linear Keyword and Restricted Natural Language Data Base Interfaces for Novice Users"
authors: "Kil Soo Suh; A. Milton Jenkins"
year: "1992"
journal: "Information Systems Research"
doi: "10.1287/isre.3.3.252"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

![](/api/attachments/9N9HBUWX/fulltext/images/89cced81cbb1cc8a77dd6452cd1257d189587b6ab1623f162c29b386044ff917.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# A Comparison of Linear Keyword and Restricted Natural Language Data Base Interfaces for Novice Users

Kil Soo Suh, A. Milton Jenkins,

## To cite this article:

Kil Soo Suh, A. Milton Jenkins, (1992) A Comparison of Linear Keyword and Restricted Natural Language Data Base Interfaces for Novice Users. Information Systems Research 3(3):252-272. http://dx.doi.org/10.1287/isre.3.3.252

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 1992 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/9N9HBUWX/fulltext/images/2205db5d52328ce9f3cf3e778a2cd4c12c981773bd454581f27e267f25337ba5.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# A Comparison of Linear Keyword and Restricted Natural Language Data Base Interfaces for Novice Users

Kil Soo Suh College of Business and Economics

Yonsei University

Seoul, 120-749 Korea

A. Milton Jenkins Merrick School of Business

University of Baltimore

Baltimore, Maryland 21201-5779

This study compares a linear keyword language interface and a restricted natural language interface for data retrieval by a novice user. The comparison focuses on the effect of different data base interfaces on user performance (as measured by query correctness and query writing time) in a query writing task across varying query types and training levels. To accomplish this objective, a laboratory experiment was conducted using a split-plot factorial design using two between-subjects factors and one within-subjects factor. The results indicate that the restricted natural language subjects performed significantly better than the linear keyword language subjects in terms of both query correctness and query writing time.

Query language—Data base—Restricted natural language—Linear keyword language—User interface

## 1. Introduction

data base query language (DBQL) is a special-purpose language in which a user Lis able to issue high-level commands or statements to retrieve information from a data base (Date, 1986, p. 8). A DBOL is primarily intended for use by end-users rather than professional programmers. The rapid increase in end-user computing has triggered research on the development of a suitable DBQL interface for novice endusers (Guimaraes and Ramanujam 1986, Rockart and Flannery 1983, Benjamin 1982). The purpose of research in this area can be classified as (1) to measure ease-ofuse of a DBQL interface, (2) to study controversial issues in DBQL interface design, (3) to provide feedback to designers of DBQL interfaces, (4) to understand and model human behavior in query writing, and (5) to compare two or more DBQL interfaces for ease-of-use (Reisner 1981). This study focuses primarily on the fifth objective, comparing linear keyword and restricted natural language interfaces.

A Linear Keyword Language (LKL) has a restricted syntax involving the use of a limited set of keywords in a predetermined sequence. It is one of the most popular DBQL interfaces available for novice end-users. SQL (Astrahan et al. 1976) is a typical example of an LKL. It is similar to a programming language, but more English-like. However, users still have difficulties retrieving information from a data base because of the syntactic rigidity of LKLs (Barbary 1987). One approach that has been proposed for dealing with this problem is to create a “natural language" interface so that the novice end-user can query the data base system with little or no training. Barbary (1987) argues that traditional DBQLs are not adequately serving the needs of the novice end-users. He suggests that natural language, by permitting users to communicate with the system in their own native language, is an attractive alternative. A complete natural language interface for data base management systems (DBMSs) is not currently available, nor expected in the near future. Restricted natural language (RNL) interfaces, however, have become more common and easier to install and use since the first commercial system was introduced in 1981 (Stevens 1986). The objective of this study is to compare an LKL interface and an RNL interface for data retrieval from the novice end-user's perspective. The comparison focuses on the effect of different DBQL interfaces on user performance (as measured by query correctness and query writing time) in a query writing task across varying query types and training levels.

## 2. Significant Prior Research

In the 1980s a number of studies focused on human factors of DBQLs. Some of them tested the feasibility of natural language interfaces. Several surveys of these studies have appeared in the literature (Shneiderman 1980, Reisner 1981, Jarke and Vassiliou 1985). In the data base area, natural language has been tested as a plausible user interface. For example, Hauptmann and Green (1983) examined three man-machine language interfaces: command language, menu selection, and natural language for computer graphics tasks. They found no effects on user performance due to language difference. More recently, Napier et al. (1989) compared the performance of novices using Lotus HAL, an RNL interface, with the performance of novices using Lotus 1-2-3, a more traditional interface. Lotus HAL was the better user interface in terms of performance than Lotus 1-2-3.

The literature reviewed here concentrates exclusively on those studies that compare linear keyword and natural language data base interfaces. Shneiderman (1980) conducted an experiment to compare the use of Structured Query Language (SQL) and English in formulating valid data base queries. The results showed no significant differences between the number of valid Ènglish and valid SQL queries. But the number of invalid queries for English was significantly more than for SQL. Shneiderman concluded that natural language usage would be extremely difficult without user knowledge of the application domain. However, this experiment had a potential bias which favored the SQL subjects. There were no restrictions on the complexity of queries for natural language subjects. For SQL subjects, on the other hand, a singletable data base was assumed, thus eliminating the need for the FROM clause; further, only simple mapping, AND/OR logic, and five arithmetic functions (SUM, COUNT, AVG, MAX, MIN) were taught. Subjects were asked to formulate their own questions with no restrictions on query complexity. Under these circumstances, the SQL subjects might tend to write easy and simple questions to avoid syntax errors. Since the training was short, all they could write were simple queries. However, the natural language subjects were familiar with English and did not have to worry about syntax errors. Their invalid questions were correct in terms of syntax, but could not be answered from the data base. This was mainly because they were not given any training about data base content.

Small and Weldon (1983) conducted a laboratory experiment using a counterbalanced design to compare a simulated natural language system with SQL. There were no significant differences for language (simulated RNL versus SQL) or for order (RNL-SOL sequence versus SQL-RNL sequence) in terms of the number of errors made. However, SOL produced significantly faster query writing time overall than did English, suggesting that SOL was easier to use. A major problem with this experiment was that the natural language subjects had to provide complete semantics of the query as if they were using SQL. For example, the request “Find the doctors whose age is over 35" was invalid because the table name was missing. A valid query was "Use the staff table to find the doctors over 35 years of age." This was simply an English translation of an SOL command, and was not a natural way of thinking for one who did not know SOL. The above invalid request is perfectly valid in currently available RNL interface systems such as R:Base Clout or Intellect. Another problem, which the authors mentioned, was that more than 40% of the subjects could not complete the experiment “because of slowness or other difficulties with the task,"so the results may apply to only a relatively elite or tenacious group.

Vassiliou et al. (1983) compared a prototype natural language query system, USL (User Specialty Language), with SQL in a laboratory environment. No significant difference in test scores was found between USL and SQL subjects. USL queries were less verbose than SOL queries. SOL subjects took significantly longer to answer questions. This experiment was well organized; however, the authors did not consider the differences across each query type. In this study, there was no significant “overall" difference in the user performance even though there were significant differences in 6 out of 15 questions. USL subjects performed better in 2 questions, and SQL subjects performed better in 4 questions. The results might suggest that one type of interface is better for one type of query and the other is better for another type of query. This is useful information for DBMSs developers and information systems managers.

Turner et al. (1984) conducted a laboratory experiment to test the performance differences between SOL and USL subjects. The primary purpose was to determine whether the subjects had obtained an acceptable level of proficiency to proceed with the next stage of the field experiment. There was no significant difference in terms of performance, but the standard deviation for the USL subject scores was almost twice that of the SOL subiects, suggesting more variation in USL subject performance. After the first test, which produced poor results and thus was not analyzed, subjects were given additional intensive hands-on practice and classroom training. But this training was interrupted by breaks and final exams. Moreover, the results were based on data from only eight subjects, so one must be careful in interpreting the results.

Jarke et al. (1985) presented the design and results of a field evaluation of a natural language system (NLS) used for data retrieval. SQL was chosen as a reference language and a counterbalanced design was used. SQL seemed superior to NLS in terms of user performance, but NLS was more efficient in terms of the length of the query required to accomplish the task. This experiment also had some problems. The NLS was a prototype system: it had many bugs, insufficient DBQL functions, and an unfriendly user interface. The major reasons subjects failed to complete a task were: lack of language functionality (24%) and interface problems (22%) for NLS, and subiect errors in using the language (35%) for SOL. Considering these facts, the finding that SQL was superior to NLS is not surprising.

Linear Keyword & Restricted Natural Language Interfaces

<table><tr><td colspan="6">TABLE 1Human Factors Studies for Natural Language</td></tr><tr><td>Reference</td><td>Shneiderman (1980)</td><td>Small and Weldon (1983)</td><td>Vassiliou et al. (1983)</td><td>Turner et al. (1984)</td><td>Jarke et al. (1985)</td></tr><tr><td>Comparison between</td><td>Natural language (English) vs. LKL (SQL)</td><td>RNL (simulated processor) vs. LKL (SQL)</td><td>RNL (USL) vs. LKL (SQL)</td><td>RNL (USL) vs. LKL (SQL)</td><td>RNL (NLS) vs. LKL (SQL)</td></tr><tr><td>Experiment Type</td><td>Laboratory</td><td>Laboratory</td><td>Laboratory</td><td>Laboratory</td><td>Field</td></tr><tr><td>Subjects</td><td>22 students for novice users</td><td>20 paid subjects for novice users</td><td>61 students for novice users</td><td>8 paid students for novice users</td><td>8 paid students for novice advisors.</td></tr><tr><td>Dependent Variables</td><td>Validness of queries</td><td>Correctness Query writing time</td><td>Correctness Query length Query writing time</td><td>Correctness</td><td>Correctness Query writing time Number of trials</td></tr><tr><td>Tests</td><td>Query generation (pencil-and-paper)</td><td>Query writing (simulated processor)</td><td>Query writing (pencil-and-paper)</td><td>Query writing (pencil-and-paper)</td><td>Problem-solving Query writing (interacting with system)</td></tr><tr><td>Major Results</td><td>Natural language users generated more invalid queries.</td><td>LKL users were faster in terms of query writing time.</td><td>RNL was less verbose. LKL subjects took longer than did RNL subjects.</td><td>No significant difference.</td><td>LKL was superior to RNL in terms of success rate. RNL was more efficient than LKL in terms of input length.</td></tr><tr><td>Major Problems</td><td>Single-table data base was assumed for LKL users. No actual RNL system. No training for natural language users.</td><td>RNL users were required to provide complete semantics of the query. Lost large number of subjects.</td><td>No consideration for the difference within each query type.</td><td>Training was interrupted, and it included a relearning component. Small number of subjects (total 8) were used.</td><td>RNL had many bugs and did not have sufficient DBQL functions.</td></tr></table>

These studies are summarized in Table 1. Keen (1980) emphasizes the necessity of building a cumulative tradition in the MIS field. All the studies employ a prototype or nonexisting RNL interface system. This study extends and adds to the prior research through (1) administering balanced treatments between the LKL and RNL subjects, (2) using an adequate sample size, (3) using real (commercial) DBQL systems, and (4)

analyzing the data with regard to both the overall differences and the differences within each query type. A typology of query types will be introduced in the §3.2.

## 3. Theoretical Framework

The study described in this paper employed a laboratory experiment. The major advantage of laboratory experimentation is that it allows close control over the independent, dependent, and possible confounding variables, thereby achieving a high degree of internal validity (Fromkin and Streufert 1976). On the other hand, a laboratory study can be criticized for the limited generality of its results and its lack of “realism"(Stone 1978).

## 3.1. Research Framework

The effects of two DBQL interfaces on users' performance may be examined from a computer-human interface model developed by Hutchins et al. (1985). They explain the relationship between the cognitive effort required to accomplish a task and the distance between the user's goals and the way these goals must be specified to a system. According to this model, there are two kinds of distance—articulatory distance and semantic distance. Articulatory distance concerns the relationship between the meanings of expressions and their physical form. For example, if the intent is to draw a diagram, an interface which accepts drawing motions as input (using a mouse or light pen) has a shorter articulatory distance than an interface employing any kind of command language from a keyboard. In this study, articulatory distance is not relevant since the subjects did not directly interact with the systems. Thus, the user's cognitive effort to retrieve data from a data base in this study depends only on the semantic distance.

Semantic distance concerns the relationship between the meaning of an expression in the interface language and what the users want to say. Two important questions about semantic distance are: (1) Can the users say what they want to say in this language? In other words, does the language encode the concepts in the domain in the same way that the users think about them? (2) Can the users say what they want in a straightforward fashion, or must they construct a complicated expression to accomplish what they perceive as a conceptually simple task? There are two basic ways to reduce semantic distance—from the system side (using a higher-level languages that is easier for the user) and from the user side (requiring the user to build new mental structures, through training, to bridge the distance). However, semantic distance may interact with the task being accomplished. If the task changes, then the semantic distance of the interface may also change. Hutchins et al. (1985) provides a good analogy for this interaction. Thus, three things—the interface language, training, and the task to be accomplished—interact to influence the semantic distance between a human and a computer. The resulting semantic distance directly changes the cognitive effort required.

Cognitive effort is the percentage of the user's available capacity or resources allocated to a given task. Navon (1984, p. 217) defined resources as “any internal input essential for processing (e.g., locations in mental storage, communication channels) that is available in quantities that are limited at any point in time." When demand for resources exceeds supply (this is usually true for novice users), tasks that require less cognitive effort have a higher probability of success (Mitchell and Hunt 1989). There is therefore an inverse relation between cognitive effort and human performance. In this study, semantic distance and cognitive effort are treated as intervening variables.' The research framework is operationalized into three independent and two dependent variables (see Figure 1).

![](/api/attachments/9N9HBUWX/fulltext/images/3ef0d5250ddd82e06bae5cb673b7d4c7adc22612378d206cc049fb2694b5b0ec.jpg)  
FiGURE 1. Research Framework for the Study

## 3.2. Independent Variables

DBQL interface type (2 levels): LKL interface (SQL) and RNL interface (Clout)

The majority of DBQLs available today are LKLs. These languages are similar to programming languages like COBOL, but are more English-like. The commands have a definite syntax, and only words from a specific reserved list can be used in a predefined sequence. Some examples of LKLs are SQL and QUEL (Stonebraker et al. 1976). For example, a typical data retrieval query in SQL consists of three clauses (SQL reserved words are printed in upper case.):

SELECT column name(s) to be printed

FROM table name containing all the column names found in the query WHERE search condition for information to be printed.

SQL was chosen for the LKL interface. SQL was unanimously approved as the standard language for relational DBMS by the American National Standards Institute (ANSI) data base subcommittee in February 1985 (Baker 1986). In addition, it has been widely adapted into many products and used in the field (McFadden and Hoffer 1988, p. 504). The specific SQL software package used in this study was the SQL interface of Ingres for PCs, version 5.0/02a.

The main objective of RNL interfaces is to enable a user, with minimal training, to obtain information from a data base. Several prototype systems have shown the feasibility of RNL interfaces (Vassiliou et al. 1983, Hendrix et al. 1978, Waltz 1978, Harris 1977, Plath 1976), and some RNL systems are commercially available (e.g., R:Base Clout 1986, Intellect 1982, Online English 1982). These languages employ a natural language (e.g., English), but are still far from conversational (person-to-person) communication. The selection of the RNL interface was not simple because there is no single dominant system. The natural language systems used in prior studies were imaginary or at best prototype systems. It is difficult to measure the performance of natural language users reliably without an actual system because the validity of a query is typically system specific. The use of a commercially available RNL system in this experiment should minimize researcher bias and allow performance to be measured objectively. Among the available RNLs, R:Base Clout and Intellect are the best known products (Clout has about 50,000 installations and Intellect about 500 according to Data Sources 1988). These two products are similar if only the data retrieval function is considered. For this study, R:Base Clout version 3.02 was selected as the RNL interface system because of its widespread use.

Clout is an RNL query system which was developed by Microrim Inc. of Redmond, Washington. An essential component of Clout is its two dictionaries—one user dictionary of special terms users have defined for their data base and one internal dictionary of 300 commonly used words. To be able to respond to words in a query the words must be stored in one of the two dictionaries. A user dictionary may be custom built for each user of Clout. A customized dictionary was not used in this study. The basic user dictionary used in this experiment can be found in Suh (1989).

Even though Clout has many positive features, there are certain limitations. Since blanks within a query indicate separate words, if a query includes a data value consisting of two or more words, the words should be enclosed in quotation marks (e.g., list the customers in “Palo Alto"). Clout cannot recognize many grammatical constraints. For example, verb voice or tense, singular and plural, and nouns and verbs are not distinguished.

## Query type (4 levels): Simple, Built-in-function, And/Or, and Composition

Reisner (1977) classified SQL queries into 11 different types and recommended that SQL be treated as a layered language—the first layer was for novices, the second for more sophisticated users, and the third for data base administrators. The first layer includes 6 of the 11 types of queries. These are: (1) simple mapping which returns the data values in some column which are associated with a known value in another column; (2) selection which returns all data values in a given row; (3) projection which returns all data values in a given column; (4) built-in-function which permits the application of mathematical functions such as +,.-, \*, /, sum, count, average, maximum value, minimum value, and so on; (5) and/or which permits conjunctions and disjunctions within a mapping; and (6) composition which permits the result of one mapping to be used as input to another mapping. Because the first three types—simple mapping, selection, and projection—are similar in structure and represent the simplest query types, they are considered as a single type—called “simple" in this study. The four types of queries used in this experiment are simple, built-in-function, and/or, and composition.

## Training (2 levels): Training and Nontraining

The presence of a main effect of the training factor would be an expected (and uninteresting) result. The reason for including this factor was to investigate its interaction with the DBQL interface type. Training was self paced and manual driven to minimize confounding factors between the training sessions. The training group studied a 34-page manual for one of the two DBQLs at their own pace. Each manual consisted of five sections. The first section provided user knowledge of the application domain, explaining the content of a mail order company's data base. The second through the fifth sections explained the language. Each section contained an explanation of a basic language syntax and examples. Following the examples, similar problems were given to test the subjects' comprehension level. Each manual had a total of 1 1 problems: 4 for simple, 3 for built-in-function, 2 for and/or, and 2 for composition query type. Subjects wrote queries for problems on paper, and they received the actual output from their queries through an intermediary. The intermediary was a doctoral student majoring in MIS and was proficient in using both SQL and Clout systems. The intermediary typed subjects' queries into one of the DBQL systems and explained to the subjects why their queries were wrong when they were not correct.

The SQL manual and Clout manual contained identical examples and problems presented in the same order. Everything independent of language differences was identical in the two manuals. The SQL manual was prepared first, modifying the manual and data base used by Welty (1979). The Clout manual was then developed based on the SQL manual. Only the language details were changed.

The nontraining group received a four-page booklet which contained a basic language syntax for solving problems given in the experiment with a description of the mail order company's data base. These booklets were excerpted from the Ingres Reference Guide and R:Base Clout User's Manual.

## 3.3. Dependent Variables

Query correctness. Whether the subject writes a query that correctly retrieves the required data is the most important dependent variable to measure in query writing tasks. Most human factors studies on DBQL comparison have included query correctness as a major dependent variable (Jarke et al. 1985, Turner et al. 1984, Welty 1979, Reisner 1977).

Query writing time. Query writing time is another major dependent variable in the previous human factors studies on comparisons between DBQLs (Jarke et al. 1985, Small and Weldon 1983, Vassiliou et al. 1983). This data was collected by unobtrusively observing the subject during the experimental task. Subjects participated in the experiment one at a time. A researcher observed every experiment from an observation room with one-way glass and measured the query writing time with a stopwatch. Each problem was contained on a single page so that the researcher could measure the writing time for each query easily.

## 3.4. Control

User. Subjects were limited to novice end-users who had no previous experience with DBQL systems.

Individual differences. Individual differences were controlled through random assignment of subjects into one of the four groups.

Task. The task was limited to query writing. Subjects were given a question stated in English and were required to write a query in the given DBQL. Each question was designed so that the question itself was not biased toward LKL or RNL. The method suggested by Vassiliou et al. (1983) to prevent a question from being a confounding factor was used. Each question consisted of three parts. First, the situation was given. Second, some clues for the query were presented. The specific action to be taken was depicted in the third part. Since the information to compose the query is scattered, the answer is not given away to the RNL subjects.

## 3.5. Hypotheses

This laboratory experiment examines the following hypotheses.

HC1. The RNL subjects will perform significantly better than the LKL subjects in terms of overall query correctness.

HT1. The RNL subjects will take significantly less time than the LKL subjects to write a query.

To list all the supplier names who are in Chicago, SQL (a typical LKL) has only one correct query and no other alternatives:

SELECT SUPPNAME FROM SUPPLIER WHERE SUPPLOC = ‘'CHI-CAGO'.

On the other hand, there are several ways in Clout (a typical RNL) to represent the correct solution. Two examples are:

GIVE ME THE SUPPLIER NAMES WHO ARE LOCATED IN CHICAGO. OBTAIN NAME OF SUPPLIERS WHERE THE SUPPLIER CITY IS CHI-CAGO.

LKL subjects need to know the exact column and table names which have the data for supplier name and location. Further, if supplier name and location are not in the same table, they should combine two or more tables based on a common value. They have to construct a complicated expression to do what appears in their thoughts as a conceptually simple task. Since these cumbersome procedures are not required for RNL subjects, the RNL interface is expected to have a shorter semantic distance than the LKL interface. The shorter semantic distance an interface system has, the less cognitive effort is required, and the better the user performs.

HC2. The difference in overall query correctness between the LKL subjects and the RNL subjects in the nontraining group will be larger than that in the training group.

HT2. The difference in overall query writing time between the LKL subjects and the RNL subjects in the nontraining group will be larger than that in the training group.

Since users can develop competence by building new mental structures to bridge the distance between the system and their goals through training, interaction between DBQL interface type and training is expected. The difference in the semantic distance between LKL and RNL should change through training. The difference in user performance between the LKL and the RNL subjects in the nontraining group will be large. This difference will be smaller in the training group because LKL subjects are expected to quickly make up the distance through training. Previous research (Small and Weldon 1983, Vassiliou et al. 1983, Turner et al. 1984) where subjects were provided with extensive training (ranging from 4 to 24 hours) found no difference in query correctness between RNL and LKL subjects.

HC3. The LKL subjects will have a significantly different pattern of performance in terms of query correctness from the RNL subjects over the four query types.

<table><tr><td rowspan="2">DBQL Interface Type</td><td rowspan="2">Training</td><td colspan="4">Query Type</td></tr><tr><td>Simple</td><td>Function</td><td>And/or</td><td>Composition</td></tr><tr><td rowspan="2">LKL</td><td>Yes</td><td>LKL/T</td><td>LKL/T</td><td>LKL/T</td><td>LKL/T</td></tr><tr><td>No</td><td>LKL/NT</td><td>LKL/NT</td><td>LKL/NT</td><td>LKL/NT</td></tr><tr><td rowspan="2">RNL</td><td>Yes</td><td>RNL/T</td><td>RNL/T</td><td>RNL/T</td><td>RNL/T</td></tr><tr><td>No</td><td>RNL/NT</td><td>RNL/NT</td><td>RNL/NT</td><td>RNL/NT</td></tr></table>

FIGURE 2. Experimental Design

HT3. The LKL subjects will have a significantly different pattern of performance in terms of query writing time from the RNL subjects over the four query types.

It is expected that there will be an interaction between DBQL interface type and query type. The difference in the semantic distance between LKL and RNL varies over the four types of queries. This difference is expected to be small for the simple query type, and larger for the composition query type where the LKL subjects must use more procedures than the RNL subjects.

## 3.6. Experimental Design

The experimental design was a split-plot factorial 22.4² design using two betweensubjects factors and one within-subjects factor. Subjects were randomly assigned to one of the DBQL interface type and training treatment groups, i.e., LKL/Training, LKL/Nontraining, RNL/Training, or RNL/Nontraining. Then, each group was exposed to all levels of the query type. This design is shown in Figure 2.

## 3.7. Subjects

A total of 60 subjects were recruited for this study as volunteers from the undergraduate student population in the School of Business at Indiana University. Students received limited credit in a particular course by participating in the experiment. Students with DBQL experience were not used. Demographic data for the subjects is provided in Table 2. There were no significant differences among the groups on the basis of demographics according to t-tests.

## 3.8. Procedures

The following experimental procedures are summarized in Figure 3.

(1) Subjects participated in the experiment individually and were randomly assigned into one of the four groups. Training group subjects studied a 34-page manual for one of the two DBQLs at their own pace. The average time taken was about 56 minutes for SQL subjects and 47 minutes for Clout subjects. Nontraining group subjects read a four-page booklet for one of the two DBQLs and examined sample data from a given data base at their own pace. It took an average of about 11 minutes for SQL subjects and 10 minutes for Clout subjects.

Suh • Jenkins  
TABLE 2

<table><tr><td rowspan="2"></td><td colspan="4">Demographic Data for Subjects</td></tr><tr><td>LKL/T</td><td>LKL/NT</td><td>RNL/T</td><td>RNL/NT</td></tr><tr><td>Total</td><td>15</td><td>15</td><td>15</td><td>15</td></tr><tr><td>Major</td><td></td><td></td><td></td><td></td></tr><tr><td>Business</td><td>10</td><td>14</td><td>14</td><td>14</td></tr><tr><td>Others</td><td>5</td><td>1</td><td>1</td><td>1</td></tr><tr><td>Sex</td><td></td><td></td><td></td><td></td></tr><tr><td>Female</td><td>8</td><td>10</td><td>9</td><td>8</td></tr><tr><td>Male</td><td>7</td><td>5</td><td>6</td><td>7</td></tr><tr><td>Age</td><td></td><td></td><td></td><td></td></tr><tr><td>16-20</td><td>11</td><td>14</td><td>14</td><td>15</td></tr><tr><td>21-25</td><td>4</td><td>1</td><td>1</td><td>0</td></tr></table>

(2) All the subjects were asked to write queries for 16 questions (four questions for each query type). Subjects were encouraged to consult their manual or booklet at any time during the experiment. A paper-and-pencil method was used to avoid confounding by procedural differences in two systems (e.g., difference in entering data and different uses of function keys). For each question, subjects wrote a query on

![](/api/attachments/9N9HBUWX/fulltext/images/b1812442dd9afbfc39056c8538a7533014e4f955819912ed8092691d7a003a46.jpg)  
FIGURE 3. Experimental Procedures

![](/api/attachments/9N9HBUWX/fulltext/images/0098d6f0fe7c9eab62779750ba3c39714e0f133fadd7a2c70405d75f03fd5ec8.jpg)  
FIGURE 4. Grading of Queries

paper (first try). They submitted these written queries to an intermediary whose only role was to type them verbatim into one of the DBQL systems and return the output from these systems, without comments, to the subjects. Subjects were required to check their output carefully to determine if they had retrieved the correct data. If they received an error message or thought their previous query had retrieved the wrong data, subjects submitted another query (second try). The same procedure was repeated one more time (third try). Thus, subjects could write any query up to three times for a single question.

(3) Subjects completed a debriefing questionnaire.

Overall, the subjects required 113 minutes to complete the experiment. More specifically, the average time taken for each subject was: 139 minutes for the LKL/ Training, 115 minutes for the RNL/Training, 114 minutes for the LKL/Nontraining, and 85 minutes for the RNL/Nontraining group.

## 3.9. Grading

Each query was graded by comparing the data retrieved with the data requested for each question. If the requested data were retrieved by the subject's query at the first try and the subject did not make a second try, the query received a score of 3. It received a score of 2 if the requested data were retrieved at the second try and the subject did not make a third try. It received a score of 1 if the requested data were retrieved at the third try. All other queries received a score of 0 (refer to Figure 4).

This weighted scheme is somewhat arbitrary. However, it provides a more objective grading scheme than those used in previous studies. Most human factors studies comparing two or more DBQL interfaces have used Welty-correctness (1979) or similar schemes for grading. These grading schemes typically require subjective judgement. For example, one of the nine categories of solutions in Welty-correctness says: "The solution was basically correct but had a small error that would be found by a reasonably good translator" (Welty 1979). But how good is “reasonably good"? The grading scheme in this study requires minimal human judgment comparing the data requested in the question and the data actually retrieved; it is more objective.

Another potential problem with some of the previous grading schemes is a lack of realism. They regard a certain minor error, such as a misspelled column name, as an essentially correct solution, and leaving out a needed condition as incorrect (a major error). However, it was observed in this experiment that some subjects could not correct a misspelled column name given three tries, while other subjects corrected a major error in the next try. We believe it is more realistic to give subjects the chance to revise their query at least twice for every question.

## 3.10. Analysis of Data

Data were analyzed using a split-plot factorial 22.4 analysis of variance (ANOVA). This is a special form of ANOVA which takes into consideration the fact that the same subjects are measured at different levels of the independent variable (Huck et al. 1974, p. 104). However, the model underlying the F test for the split-plot design does not include a term for carry-over or sequence effects. This ANOVA is appropriate where the sequence effects are likely to be small relative to the treatment effects (Winer 1971, pp. 518–519). In this experiment, the query type effects were expected to be much greater than the sequence effects. Further, the query types were randomly ordered, and the output was not provided until subjects finished all the queries, so the sequence or learning effects were minimal.

## 4. Results

The significance level, alpha, for testing differences in means was set at 0.01. Although a conservative significance level was used, the probability values for all F tests are provided so that the reader may interpret the results according to any alpha setting.

## 4.1. Query Correctness

All three independent variables impact query correctness as shown in Tables 3 and 4. The research hypotheses are scrutinized below.

HC1. The RNL subjects will perform significantly better than the LKL subjects in terms of overall query correctness.

A statistically significant main effect was obtained as expected (F = 17.05, p < 0.01; see Table 3). With only two levels associated with the DBQL interface type, a simple comparison of the two main effect means was sufficient to determine which was significantly larger. The mean score of the RNL subjects was 2.21 and that of the LKL subjects was 1.60 (see Table 4). Thus, this hypothesis was supported. According to our model, the RNL interface has shorter semantic distance, which requires less cognitive effort, and thus results in higher mean scores than the LKL interface.

HC2. The difference in overall query correctness between the LKL subjects and the RNL subjects in the nontraining group will be larger than that in the training group.

Linear Keyword & Restricted Natural Language Interfaces

<table><tr><td colspan="7">TABLE 3Analysis of Variance of Query Correctness</td></tr><tr><td>Source</td><td>SS</td><td>df</td><td>MS</td><td>F</td><td>p</td><td>Related Hypothesis</td></tr><tr><td>Between Subjects</td><td>2,328.74</td><td>59</td><td></td><td></td><td></td><td></td></tr><tr><td>DBQL Type (A)</td><td>360.15</td><td>1</td><td>360.15</td><td>17.05</td><td>0.00*</td><td>HC1</td></tr><tr><td>Training (B)</td><td>770.42</td><td>1</td><td>770.42</td><td>36.46</td><td>0.00*</td><td></td></tr><tr><td>A × B</td><td>15.00</td><td>1</td><td>15.00</td><td>0.71</td><td>0.40</td><td>HC2</td></tr><tr><td>Error-Between</td><td>1,183.17</td><td>56</td><td>21.13</td><td></td><td></td><td></td></tr><tr><td>Within Subjects</td><td>1,763.00</td><td>180</td><td></td><td></td><td></td><td></td></tr><tr><td>Query Type (C)</td><td>708.90</td><td>3</td><td>236.30</td><td>59.13</td><td>0.00*</td><td></td></tr><tr><td>A × C</td><td>160.22</td><td>3</td><td>53.41</td><td>13.36</td><td>0.00*</td><td>HC3</td></tr><tr><td>B × C</td><td>182.48</td><td>3</td><td>60.83</td><td>15.22</td><td>0.00*</td><td></td></tr><tr><td>A × B × C</td><td>40.03</td><td>3</td><td>13.34</td><td>3.34</td><td>0.02</td><td></td></tr><tr><td>Error-Within</td><td>671.37</td><td>168</td><td>4.00</td><td></td><td></td><td></td></tr><tr><td>Total</td><td>4,091.74</td><td>239</td><td></td><td></td><td></td><td></td></tr></table>

The effect was statistically significant at the 0.01 level.

Even though the gap between the LKL and the RNL' subjects was larger in the nontraining group (0.74) than in the training group (0.49), it was not statistically significant (F = 0.71, p = 0.40; see Table 3 and Figure 5). Thus, this hypothesis was not supported. This result might be explained by the short training time. Since the LKL subiects reduced the semantic distance through training more rapidly than the RNL, subiects, we suspect that this hypothesis would be supported if the subjects received more extensive training.

HC3. The LKL subiects will have a significantly different pattern of performance in terms of query correctness from the RNL subjects over the four query types.

There was a statistically significant interaction among the two DBQL interfaces and the four query types (F = 13.36, p < 0.01; see Table 3). Thus, this hypothesis was supported. When a statistically significant interaction is present in a factorial AN-OVA. comparisons of the main effects may have little importance. Instead of comparing the overall main effects, a comparison of simple main effects should be per-

TABLE 4  
Mean Scores of Query Correctness

<table><tr><td>Group</td><td>Query</td><td>Simple</td><td>Function</td><td>And/Or</td><td>Composition</td><td>Mean</td></tr><tr><td rowspan="3">LKL</td><td>T</td><td>2.68 (0.35)</td><td>2.02 (0.98)</td><td>1.93 (0.90)</td><td>1.82 (1.08)</td><td>2.11 (0.73)</td></tr><tr><td>NT</td><td>2.03 (0.87)</td><td>0.72 (0.69)</td><td>1.15 (1.01)</td><td>0.47 (1.00)</td><td>1.09 (0.74)</td></tr><tr><td>Mean</td><td>2.36 (0.73)</td><td>1.37 (1.06)</td><td>1.54 (1.02)</td><td>1.14 (1.23)</td><td>1.60 (0.89)</td></tr><tr><td rowspan="3">RNL</td><td>T</td><td>2.85 (0.23)</td><td>2.30 (0.50)</td><td>2.60 (0.46)</td><td>2.65 (0.32)</td><td>2.60 (0.30)</td></tr><tr><td>NT</td><td>2.68 (0.48)</td><td>0.55 (0.56)</td><td>2.22 (0.64)</td><td>1.87 (0.64)</td><td>1.83 (0.39)</td></tr><tr><td>Mean</td><td>2.77 (0.38)</td><td>1.43 (1.03)</td><td>2.41 (0.58)</td><td>2.26 (0.64)</td><td>2.21 (0.52)</td></tr></table>

The potential maximum score in a cell is 3.00 which denotes that all of the subjects in the treatment group wrote the correct query on the first try. The numbers inside the parentheses indicate standard deviations.

![](/api/attachments/9N9HBUWX/fulltext/images/7583f8e228d2db550998aa653b2c170053e1f8c1a70e56016fc0f31050618813.jpg)  
FIGURE 5. Mean Scores for the LKL and the RNL Subjects with and without Training

formed. This procedure involves comparing the various levels of one factor at each separate level of the other factor (Huck et al. 1974, p. 88). A simple main effects analysis (i.e., a one-way ANOVA for the two DBQL interfaces at a particular level of the query type factor) indicated that the differences for the simple query type, the and/or query type, and the composition query type were statistically significant $( F = 7 . 4 1 , p < 0 . 0 1 ; F = 1 6 . 3 6 , p < 0 . 0 1 ; F = 1 9 . 4 1 , p < 0 . 0 1$ , respectively; see Figure 6). The RNL subjects showed better and more even performance in terms of query correctness on the simple queries, and/or queries, and composition queries than the LKL subjects. In particular, the RNL subjects performed much better than the LKL subjects on the composition queries since RNL requires fewer procedures than LKL for a multitable task. However, all subjects performed poorly on the built-in-function queries since they all had problems in writing algebraic equations for percentage calculations. It is possible that more sophisticated interface languages which can understand general concepts (e.g., percentage) will shorten semantic distance and produce better user performance.

![](/api/attachments/9N9HBUWX/fulltext/images/efd5b688d9c0a77cf60ca04f9b1b4ed25a91ab08e32e3b6c36d893c28c782d9a.jpg)

<table><tr><td>Difference (RNL - LKL)</td><td>0.41</td><td>0.06</td><td>0.87</td><td>1.12</td></tr><tr><td>F</td><td>7.41</td><td>0.05</td><td>16.36</td><td>19.41</td></tr><tr><td>p</td><td>0.01*</td><td>0.83</td><td>0.00*</td><td>0.00*</td></tr></table>

\*: The simple main effect was statistically significant at the 0.01 level.  
FiGURE 6. Mean Scores for the LKL and the RNL Subjects on the Four Query Types and Simple Main Effect Analysis

Linear Keyword & Restricted Natural Language Interfaces

<table><tr><td colspan="7">TABLE 5Analysis of Variance of Query Writing Time</td></tr><tr><td>Source</td><td>SS</td><td>df</td><td>MS</td><td>F</td><td>p</td><td>Related Hypothesis</td></tr><tr><td>Between Subjects</td><td>2,621.09</td><td>59</td><td></td><td></td><td></td><td></td></tr><tr><td>DBQL Type (A)</td><td>517.69</td><td>1</td><td>517.69</td><td>14.89</td><td>0.00*</td><td>HT1</td></tr><tr><td>Training (B)</td><td>151.87</td><td>1</td><td>151.87</td><td>4.37</td><td>0.04</td><td></td></tr><tr><td>A × B</td><td>5.18</td><td>1</td><td>5.18</td><td>0.15</td><td>0.70</td><td>HT2</td></tr><tr><td>Error-Between</td><td>1,946.35</td><td>56</td><td>34.76</td><td></td><td></td><td></td></tr><tr><td>Within Subjects</td><td>3,561.48</td><td>180</td><td></td><td></td><td></td><td></td></tr><tr><td>Query Type (C)</td><td>1,065.83</td><td>3</td><td>355.28</td><td>33.07</td><td>0.00*</td><td></td></tr><tr><td>A × C</td><td>335.84</td><td>3</td><td>111.95</td><td>10.42</td><td>0.00*</td><td>HT3</td></tr><tr><td>B × C</td><td>317.00</td><td>3</td><td>105.67</td><td>9.84</td><td>0.00*</td><td></td></tr><tr><td>A × B × C</td><td>37.87</td><td>3</td><td>12.62</td><td>1.17</td><td>0.32</td><td></td></tr><tr><td>Error-Within</td><td>1,804.94</td><td>168</td><td>10.74</td><td></td><td></td><td></td></tr><tr><td>Total</td><td>6,182.57</td><td>239</td><td></td><td></td><td></td><td></td></tr></table>

The effect was statistically significant at the 0.01 level.

## 4.2. Query Writing Time

Two independent variables, DBQL interface type and query type, have impacts on query writing time, as shown in Tables 5 and 6. Statistics related research hypotheses are scrutinized below.

HT1. The RNL subjects will take significantly less time than the LKL subjects to write a query.

The analysis indicated that the main effect was statistically significant (F = 14.89, p < 0.01; see Table 5). It took a mean time of 1.94 minutes to write a query for the RNL subjects and 2.68 minutes for the LKL subjects (see Table 6). Thus, this hypothesis was supported. Again, according to our model, the RNL interface has shorter semantic distance, which requires less cognitive effort, and results in shorter writing time than the LKL interface.

HT2. The difference in overall query writing time between the LKL subjects and the RNL subjects in the nontraining group will be larger than that in the training group.

TABLE 6  
Mean Query Writing Times (Minutes)

<table><tr><td>Group</td><td>Query</td><td>Simple</td><td>Function</td><td>And/Or</td><td>Composition</td><td>Mean</td></tr><tr><td rowspan="3">LKL</td><td>T</td><td>1.60 (0.68)</td><td>2.45 (0.56)</td><td>1.88 (0.52)</td><td>4.13 (1.10)</td><td>2.52 (0.47)</td></tr><tr><td>NT</td><td>2.02 (0.72)</td><td>3.62 (1.91)</td><td>2.28 (1.47)</td><td>3.44 (1.25)</td><td>2.84 (1.09)</td></tr><tr><td>Mean</td><td>1.81 (0.72)</td><td>3.04 (1.51)</td><td>2.08 (1.10)</td><td>3.79 (1.21)</td><td>2.68 (0.84)</td></tr><tr><td rowspan="3">RNL</td><td>T</td><td>1.41 (0.43)</td><td>1.77 (0.61)</td><td>1.56 (0.51)</td><td>2.09 (1.61)</td><td>1.71 (0.54)</td></tr><tr><td>NT</td><td>2.02 (0.64)</td><td>3.07 (1.37)</td><td>1.54 (0.41)</td><td>2.08 (0.88)</td><td>2.18 (0.70)</td></tr><tr><td>Mean</td><td>1.72 (0.62)</td><td>2.42 (1.23)</td><td>1.55 (0.45)</td><td>2.09 (1.27)</td><td>1.94 (0.66)</td></tr></table>

![](/api/attachments/9N9HBUWX/fulltext/images/5095da618d2f26d2dd4e71fd8508e599a07923f7cc57647707a83f10c6a36c5f.jpg)  
FIGURE 7. Mean Writing Times for the LKL and the RNL Subjects with and without Training

This hypothesis was not supported. In fact, the gap between the LKL and the RNL subjects was larger in the training group (0.81 minutes per query) than in the nontraining group (0.66), although this difference was not statistically significant $( F = 0 . 1 5 , p = 0 . 7 0 ;$ see Table 5 and Figure 7). The nontraining group left the query incomplete or wrote the query in their own (of course wrong) syntax for the questions which they did not know. In this way they spent much less time than expected. This was especially true for the LKL/Nontraining group.

HT3. The LKL subjects will have a significantly different pattern of performance in terms of query writing time from the RNL subjects over the four query types.

The analysis indicated that the interaction was statistically significant $( F = 1 0 . 4 2 , p$ $\mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \Lambda } } } } } } } \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \Lambda } } } } } \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \Lambda } } } } } \mathbf { \mathbf { \mathbf { \mathbf { \Lambda } } } } \mathbf { \mathbf { \mathbf { \mathbf { \Lambda } } } } \mathbf { \mathbf { \mathbf { \Lambda } } } < \mathbf { 0 . 0 1 } ;$ see Table 5). Thus, this hypothesis was supported. Since the interaction was statistically significant, a subsequent analysis of the simple main effects was performed. The LKL and the RNL subjects had a significantly different performance in terms of query writing time only on the composition query type $( F = 2 8 . 1 1 , p < 0 . 0 1 ;$ see Figure 8). The LKL subjects spent significantly more time writing the composition queries than the RNL subjects, but no statistically significant differences in time were found between the two groups in writing the other three query types. In a pattern similar to the results for query correctness, the RNL subjects showed better and more even performance in terms of query writing time. Again, the RNL subjects performed much better than the LKL subjects on the composition queries, but both the LKL and the RNL subjects performed poorly on the built-in-function queries.

## 5. Conclusions

The results from this study provide strong empirical evidence that RNL data base interfaces can improve user performance in retrieval tasks in certain circumstances. These results can be explained by a model in which differences in semantic distance associated with the languages induce differences in cognitive effort. The experiment supports that RNL has shorter semantic distance than LKL for novice users who receive limited training for the query writing task. Thus it requires less cognitive effort resulting in better performance in terms of query correctness and query writing time. This was especially true with the simple query type, the and/or query type, and the composition query type for query correctness. If only query writing time was considered, RNL had an advantage over LKL in the composition query type. RNL was most effective compared to LKL in the composition query type. This suggests the difference in semantic distance between the two interface languages for this type of query is the largest, as expected. Training also reduces the semantic distance between users and the system by making users think in the same language as the system.

![](/api/attachments/9N9HBUWX/fulltext/images/e425de8ff967edc3eb37a424c4b30dca12d883bb6d148a061a5501597154b4ef.jpg)

<table><tr><td>Difference (RNL - LKL)</td><td>0.09</td><td>0.62</td><td>0.53</td><td>1.70</td></tr><tr><td>F</td><td>0.28</td><td>3.00</td><td>5.99</td><td>28.11</td></tr><tr><td>p</td><td>0.60</td><td>0.09</td><td>0.02</td><td>0.00*</td></tr></table>

\*: The simple main effect was statistically significant at the 0.01 level.  
FIGURE 8. Mean Writing Times for the LKL and the RNL Subjects on the Four Query Types and Simple Main Effect Analysis

These results imply that an organization could utilize the RNL interface for its novice end-users to improve their data retrieval performance without increasing training time. Considering that the user dictionary of the RNL system in this experiment was not customized for each user, the potential advantage of an RNL interface is expected to be even greater than was shown in this study. However, the additional resources needed to purchase an RNL interface and the time to develop a user dictionary should be considered as well.

## 6. Limitations and Future Research

Internal validity is necessary to test hypotheses. This experiment was carefully conducted and controlled, providing the desired degree of internal validity. Conversely, laboratory experiments have limited external validity, and over-generalization should be avoided. Among the factors that may influence external validity are: this study used student subjects in a laboratory setting, the task was limited to writing relatively simple queries, the input was by paper-and-pencil, feedback was not instantaneous, and the study was limited to two DBQL interfaces, SQL and Clout.

This study may be extended in various ways to enhance the generalizability of the results. The experiment involved novice users and four types of queries. More sophisticated users writing advanced types of queries could be studied. Direct interaction with various DBOL interfaces to solve real problems in a field environment could be examined. The time between training and testing could be expanded to measure retention and relearning ability of users for each DBQL interface type. Finally, this study employed only two DBQL systems, SQL and Clout. Other popular LKL and RNL such as Ingres, R:Base, or Intellect could be tested.

Additional research is also needed to examine the research model presented here. Semantic distance and cognitive effort were treated as intervening variables in this study. To further test the research framework introduced here, these variables should be measured. The theoretical construct of cognitive effort has a long and venerable history in psychology (Bettman et al. 1990). Further, there have been a number of measurement techniques proposed for the related concept of mental workload (Wickens 1984). Finally, these concepts have application to the information systems field beyond query languages.\*

\* Edward Stohr, Associate Editor. This paper was received on April 13, 1990, and has been with the authors 8 months for 3 revisions.

Appendix: Comparison of Weighted and Unweighted Grading Methods for Query Correctness Mean Scores

Weighted Grading Methods: See Table 4.

Unweighted Grading Methods: See below.\*

<table><tr><td>Group</td><td>Query</td><td>Simple</td><td>Function</td><td>And/Or</td><td>Composition</td><td>Mean</td></tr><tr><td rowspan="3">LKL</td><td>T</td><td>0.93</td><td>0.70</td><td>0.72</td><td>0.67</td><td>0.75</td></tr><tr><td>NT</td><td>0.77</td><td>0.30</td><td>0.43</td><td>0.20</td><td>0.43</td></tr><tr><td>Mean</td><td>0.85</td><td>0.50</td><td>0.58</td><td>0.43</td><td>0.59</td></tr><tr><td rowspan="3">RNL</td><td>T</td><td>0.98</td><td>0.82</td><td>0.92</td><td>0.92</td><td>0.91</td></tr><tr><td>NT</td><td>0.98</td><td>0.28</td><td>0.83</td><td>0.78</td><td>0.72</td></tr><tr><td>Mean</td><td>0.98</td><td>0.55</td><td>0.88</td><td>0.85</td><td>0.81</td></tr></table>

\* The potential maximum score in a cell is 1.00 which denotes that all of the subjects in the treatment group wrote the correct query in three tries.

Hypotheses Test

<table><tr><td>Method Hypothesis</td><td>Weighted</td><td>Unweighted</td></tr><tr><td>HC1</td><td>Confirmed ( $p < 0.01$ )</td><td>Confirmed ( $p < 0.01$ )</td></tr><tr><td>HC2</td><td>Not confirmed ( $p = 0.40$ )</td><td>Not confirmed ( $p = 0.18$ )</td></tr><tr><td>HC3</td><td>Confirmed ( $p < 0.01$ )</td><td>Confirmed ( $p < 0.01$ )</td></tr></table>

## References

Artificial Intelligence Co., Intellect Query System Reference Manual, Boston, MA, 1982.

Astrahan, M. M., M. W. Blasgen, D. D. Chamberlin, K. P. Eswaran, J. N. Gary, P. P. Griffiths, W. F. King R. A. Lorie, P. R. McJones, J. W. Mehl, G. R. Putzolu, I. L. Traiger, B. W. Wade and V. Watson, "System R: Relational Approach to Database Management," ACM Transactions on Database Systems 1, 2 (June 1976), 97–137.

Baker, J., “SQL: A New Standard," Computerworld Focus (February 1986), 55–58.

Barbary, C., “A Database Primer on Natural Language," Journal of Systems Management (April 1987) 20-25.

Benjamin, R. I., "Information Technology in the 1990's: A Long Range Planning Scenario," MIS Quar terly, 6, 2 (June 1982), 11–31.

Bettman. J. R., E. J. Johnson and J. W. Payne, “A Componential Analysis of Cognitive Effort in Choice," Organizational Behavior and Human Decision Processes, 45 (1990), 111–139.

Cullinet Co., Online English User's Guide, Westwood, MA, 1982.

Date, C. J., An Introduction to Database Systems (4th Ed.), Vol. I, Addison-Wesley, Reading, MA, 1986

Fromkin, H. L. and S. Streufert, "Laboratory Experimentation," Handbook of Industrial Psychology M. D. Dunnette (Ed.), Rand McNally, Chicago, IL, 1976, 415–465.

Guimaraes, T. and V. Ramanujam, “Personal Computing Trends and Problems: An Empirical Study," MIS Quarterly, 10, 2 (June 1986), 179–187.

Harris, L. R., "User Oriented Database Query with the ROBOT Natural Query System," International Journal of Man-Machine Studies, 9, 6 (1977), 697–713.

Hauptmann, A. G. and B. F. Green, "A Comparison of Command, Menu-Selection and Natural-Language Computer Programs." Behavior and Information Technology. 2, 2 (1983), 163–178.

Hendrix, G. G., E. D. Sacerdoti, D. Sagalowicz and J. Slocum, "Developing a Natural Language Interface to Complex Data," ACM Transactions on Database Systems, 3, 2 (June 1978), 105–147.

Huck, S. W., W. H. Cormier and W. G. Bounds, Jr., Reading Statistics and Research, Harper & Row, New York, NY, 1974.

Hutchins, E. L., J. D. Hollan and D. A. Norman, "Direct Manipulation Interfaces," Human-Computer Interaction, 1 (1985), 311–338.

Jarke, M., J. A. Turner, E. A. Stohr, Y. Vassiliou, N. H. White and K. Michielsen, “A Field Evaluation of Natural Language for Data Retrieval," IEEE Transactions on Software Engineering (SE-11: 1), (January 1985), 97–114.

Jarke, M. and Y. Vassiliou, “A Framework for Choosing a Database Query Language," Computing Surveys. 17, 3 (September 1985), 313–340.

Keen, P. G. W., “MIS Research: Reference Disciplines and a Cumulative Tradition," Proceedings of the First International Conference on Information Systems (December 1980), 9–18.

McFadden, F. R. and J. A. Hoffer, Data Base Management (2nd Ed.), Benjamin/Cummings Publishing Co., Menlo Park, CA, 1988.

Microrim Inc., R:Base Clout User's Manual, Redmond, WA, 1986.

Mitchell, D. B. and R. R. Hunt, "How Much Effort Should Be Devoted to Memory?" Memory and Cognition, 17, 3 (1989), pp. 337–348.

Napier, H. A., D. M. Lane, R. R. Batsell and N. S. Guadango, "Impact of a Restricted Natural Language Interface on Ease of Learning and Productivity," Communications of the ACM, 32, 10 (October 1989), 1190-1198.

Navon, D., “Resources—A Theoretical Soapstone?" Psychological Review, 91 (1984), 216-234.

Plath, W. J., “REOQUEST: A Natural Language Question-Answering System," IBM Journal of Research and Development, 20, 4 (July 1976) 326–335.

Reisner, P., "Use of Psychological Experimentation as an Aid to Development of a Query Language," IEEE Transactions on Software Engineering (SE-3), (May 1977), 218–229.

"Human Factor Studies of Database Query Languages," Computing Surveys, 13, 1 (March 1981), 13–31.

Relational Technology Inc., Ingres Reference Guide, Alameda, CA, 1987.

Rockart, J. F. and L. S. Flannery, "The Management of End User Computing," Communications of the ACM, 26, 10 (October 1983), 776–784.

Shneiderman, B., Software Psychology, Winthrop Publishers, Cambridge, MA, 1980.

Small, D. W. and L. J. Weldon, “An Experimental Comparison of Natural and Structured Query Language," Human Factors, 25, 3 (1983), 253–263.

Stevens, L., “Getting Data in Plain English," Computer Decisions, 18, 9 (April 22, 1986), 42–47.

Stone, E., Research Methods in Organization Behavior, Scott, Foresman & Co., Glenview, IL, 1978.

Stonebraker, M., E. Wong, P. Kreps and G. Held, "The Design and Implementation of Ingres," ACM Transactions on Database Systems, 1, 3 (September 1976), 189–222.

Suh, K. S., “A Comparison of Linear Keyword and Restricted Natural Language for Data Retrieval," Ph.D. Dissertation, Indiana University, 1989.

Turner, J. A., M. Jarke, E. A. Stohr, Y. Vassiliou and N. H. White, "Using Restricted Natural Language for Data Retrieval—A Plan for Field Evaluation," Human Factors and Interactive Computer Systems, Y. Vassiliou (Ed.), Ablex, Norwood, NJ, 1984, 163–190.

Vassiliou, Y., M. Jarke, E. A. Stohr, J. A. Turner and N. H. White, "Natural Language for Database Queries: A Laboratory Study," MIS Quarterly, 7, 4 (December 1983), 47–61.

Waltz, D. L., "An English Language Question Answering System for a Large Relational Database,"Com munications of the ACM, 21, 7 (July 1978), 526–539.

Welty, C., “A Comparison of a Procedural and a Non-procedural Query Language: Syntactic Metrics and Human Factors," Ph.D. Dissertation, Computer Science Dept., University of Massachusetts, Amherst, MA, 1979.

Wickens, C. D., Engineering Psychology and Human Performance, Charles E. Merrill, Columbus, OH 1984.

Winer, B. J., Statistical Principles in Experimental Design (2nd Ed.), McGraw-Hill, New York, NY, 1971

Ziff-Davis Publishing Co., Data Sources, 8, 2, Software 1st Ed., New York, NY, 1988.
