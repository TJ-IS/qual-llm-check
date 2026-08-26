---
otero_id: 23440
otero_key: "XSZYZ8NM"
title: "Current use of software tools in the development of medical and health services computer applications — a Survey"
authors: "Donald Millington; Iain M Tulloch; Edwin M Gray"
year: "1991"
journal: "Journal of Information Technology"
doi: "10.1057/jit.1991.14"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Current use of software tools in the development of medical and health services computer applications — a survey

DONALD MILLINGTON, IAIN M. TULLOCH and EDWIN M. GRAY

Department of Computer Science, University of Strathclyde, Glasgow

Abstract: A survey was carried out in order to draw on experience in the UK of the use of software tools to develop medical and health service applications. The main objective was to identify the capabilities and characteristics that might be required in software tools created specifically for this area of applications. The work gives some indications of such requirements, but was constrained by the discovery that so far there has been only limited use of the general-purpose software development tools currently available.

## Introduction

Recent years have seen a significant growth in the availability of software tools designed to assist in the development of computer applications software. Such tools may vary between being targeted at one particular aspect of software development, (e.g. creation and maintenance of data flow diagrams, or implementation of user interfaces) or supporting a wide range of tasks over several phases of development. A review of the range of such tools may be found elsewhere, e.g. McClure (1988), Gane (1990) and in-depth comparisons of a wide range of software tools in the market-place have been produced, e.g. Rock-Evans (1989), Development World (1990).

Two of the aims of increased tool support for software development are often identified as: improved software quality, and greater user participation in the work. The latter of these supports the former and both may be aided by having 'high-level' facilities, i.e. languages and methods which relate to the domain of application itself. A prime objective of the survey reported in this paper was to identify ways in which application-oriented software tools might differ from general purpose tools. It was envisaged, for example, that both specification and implementation might benefit by being able to refer to a better set of 'primitive' data objects and processes than those in general use. A simple example of this can be seen in languages for business applications which allow variables of types, date and money, and work with the concept of a 'report'.

The application area selected for the survey — medical and health services — is one with which the authors have many years of experience. It is also the area of collaboration with other partners in a project — called Healthbench — supported under the Advanced Informatics in Medicine (AIM) Programme of The Commission of the European Communities. Indeed, a first version of the survey questionnaire was exercised in a limited way as part of that project, and the present survey was undertaken in order to extend the previously obtained picture in respect of the U.K.

The medical and health applications area exhibits a number of characteristics which would seem to make it a good choice for a study of this nature.

(1) It is a very large user of information processing and if the needs for computer use are to be met, the applications development process must use increasingly automated methods;

(2) Its past, present and future investment in information technology (IT) is a significant budget item at national and international levels and the needs for effective re-usability of applications and components are strong;

(3) There is a very wide range of potential users of information technology and methods/tools for developing user interfaces need to provide flexibility;

(4) There is a very wide range of developers of IT applications, including medical and technical staff as well as professional IT personnel; software methods and tools for use in development need to be 'safe' (quality assuring) as well as easy and effective in use;

(5) It has a wealth of local, or specialist, language which ought not to need re-defining or re-interpreting specifically in every application;

(6) There is a long history of experience in developing IT applications, but frequently implementations are still specific to a particular local environment.

This set of characteristics implies that the medical and health services area of computing should benefit significantly from the use of software tools for developing computer applications. The survey reported here indicates the present situation in the UK.

## Methods

## Design of the questionnaire

The purpose of the questionnaire was to collect information on the use of advanced software tools in the development of medical and health service computer applications. Advanced meant beyond the use of traditional language compilers and program debuggers. Examples mentioned in the introduction to the questionnaire included system modelling tools, CASE (Computer Aided Software Engineering) tools, database management systems, 4GLs (Fourth-Generation Languages) and other new languages, expert system shells and decision support system shells.

Since the level of experience in applying IT in an organization is a significant factor in its choice of methods and tools, and in identifying future needs (Nolan, 1979), the questionnaire was given a two-part structure. Part 1 was at an overall level and included questions about the nature of the organization; part 2 included detailed questions on experience with a particular software tool, and a copy was to be completed for each tool which had been used.

Questions in part 1 were designed to provide data on

(1) The organization's scale of experience, through questions on the number of years experience in health computing, the range of applications implemented and the range of institutions in which they had been implemented;

(2) The approach to applications development, through questions on programming languages and systems development methods in use;

(3) The range of experience with advanced software tools, using a matrix (illustrated later in the Results section) to show for each of a range of tool types the level of use or the reasons(s) for non-use.

The capability to record reasons for not using advanced software tools was a specific addition to an earlier version of the questionnaire used in the Healthbench project; that version had been targeted for organizations expected to be using advanced software tools.

The questions of part 2 sought information which detailed the tool being reported on, the kind of applications for which it had been used, its strengths and weaknesses, and the problems and benefits that resulted. The full version of part 2 ran to 6 pages, but a single page simplified version was also produced. The latter was sent to respondents who in part 1 indicated some use of software tools of a particular type, but had not completed a full part 2, because, or so it was assumed, their experience was not of appropriate depth.

## Use of the questionnaire

The questionnaire was sent out to

(1) All district and regional information or computer managers in the National Health Service in the UK (228 recipients in total);

(2) As many appropriate commercial software companies as could be identified in the UK (26 recipients in total);

(3) One group classified as a research and development organization.

Normally, if the respondents failed to reply no follow-up of the original questionnaire was made. A small number of telephone conversations took place mainly at the instigation of those people completing the questionnaire, who needed further guidance.

Copies of the simplified part 2, mentioned in the previous section, were sent out to a number of respondents who indicated some use of advanced tools, but failed to complete the full part 2 sent out initially.

## Relation to the AIM Healthbench project

The Healthbench Project mentioned previously was a collaborative project with partners in The Netherlands, Portugal and Spain, and The University of Strathclyde. Its main objective was to define requirements for a workbench to be used in developing computer applications in medicine and the health services. One component of that work was to survey experience to date with advanced software tools when developing health IT applications. A questionnaire was used which was an earlier version of the one used in the study reported in this paper. Because of a tight time constraint it was offered to a small number of organizations in a few countries, believed to have specific experience in the use of advanced software tools. Some comments on the results of that survey will be made later for comparison under the Conclusions section of this paper.

## Results of the survey

Table 1 represents the total number of questionnaires sent out and the total number of responses received.

Table 1

<table><tr><td></td><td>Questionnaires sent</td><td>Responses received</td></tr><tr><td>Health authorities</td><td>228</td><td>36</td></tr><tr><td>Software houses</td><td>26</td><td>11</td></tr><tr><td>Research and development</td><td>1</td><td>1</td></tr><tr><td>Total</td><td>(255)</td><td>(48)</td></tr></table>

In subsequent sections responses are grouped over all types of organizations because there were no apparent

distinctions between types. Since some questionnaires were incomplete the numbers in subsequent tables do not necessarily correspond.

## Responses to part 1

Number of years experience in health computing

Fewer than 4: 4; between 4 and 10: 24; more than 10: 13.

## Range of applications implemented

Complete hospital system: 12; some medical applications: 21; patient administration system: 25; other departmental systems: 26.

Range of institutions in which applications have been implemented

Single department: 5; single hospital: 7; multiple hospitals: 36; community services: 28.

## Programming languages used regularly

Approximately two-thirds of the responses to this question indicated use of third generation languages. The most popular was C, followed equally by Mumps and Cobol. The remaining one-third were fourth generation languages.

## System development methods usually employed

Responses to this question indicated that few organizations are using well-established development methodologies. The most frequent was SSADM, which was cited in four of the 15 replied.

## Experience of software tools

The layout shown in Table 2 was used to allow respondents to indicate the scale of their use of software tools in application development, and possible reasons for non-use. The key to the reasons for non-use was as follows:

(1) Inappropriate: Your organization has no use for this type of tool;

(2) Unsuitable: Currently available tools in this category are technically incompatible with or not available on your system or do not support your existing development methodologies;

(3) Cost: The expected associated costs of this type of tool are too high;

(4) Training Overheads: Demands on staff time and training needs (and associated costs) would be too high;

(5) Lack of experience: Your organization has insufficient experienced staff to use this type of tool;

(6) Lack of Information: There is a lack of information about the capabilities and potential of this type of tool.

## Responses to part 2

Table 3 represents the number of completed part 2 questionnaires which were returned. The categories in Table 3 refer to the type of tool as identified by the user.

## Table 2

<table><tr><td>Tool type</td><td colspan="3">Level of use</td><td colspan="6">Reason(s) for non-usage</td></tr><tr><td>Planning</td><td>6</td><td>5</td><td>19</td><td>4</td><td>2</td><td>1</td><td>0</td><td>7</td><td>4</td></tr><tr><td>Project management</td><td>8</td><td>9</td><td>20</td><td>2</td><td>3</td><td>1</td><td>0</td><td>6</td><td>4</td></tr><tr><td>Analysis</td><td>8</td><td>2</td><td>23</td><td>8</td><td>1</td><td>1</td><td>0</td><td>6</td><td>3</td></tr><tr><td>Design</td><td>5</td><td>2</td><td>27</td><td>11</td><td>1</td><td>0</td><td>0</td><td>5</td><td>2</td></tr><tr><td>Database design</td><td>6</td><td>1</td><td>24</td><td>9</td><td>1</td><td>0</td><td>1</td><td>7</td><td>2</td></tr><tr><td>Real-time design</td><td>2</td><td>0</td><td>30</td><td>16</td><td>0</td><td>0</td><td>0</td><td>5</td><td>3</td></tr><tr><td>High-level code generator</td><td>7</td><td>0</td><td>23</td><td>10</td><td>2</td><td>0</td><td>0</td><td>5</td><td>3</td></tr><tr><td>Maintenance</td><td>5</td><td>2</td><td>23</td><td>7</td><td>2</td><td>1</td><td>0</td><td>5</td><td>2</td></tr><tr><td>DBMS (without 4GL)</td><td>9</td><td>0</td><td>21</td><td>9</td><td>1</td><td>0</td><td>0</td><td>4</td><td>2</td></tr><tr><td>4GL (incl. DBMS)</td><td>14</td><td>3</td><td>17</td><td>3</td><td>2</td><td>0</td><td>1</td><td>5</td><td>2</td></tr><tr><td>Expert system shell</td><td>1</td><td>6</td><td>26</td><td>7</td><td>1</td><td>1</td><td>1</td><td>8</td><td>5</td></tr><tr><td>Decision support system</td><td>4</td><td>6</td><td>19</td><td>5</td><td>1</td><td>1</td><td>0</td><td>8</td><td>4</td></tr><tr><td>Statistics package</td><td>10</td><td>7</td><td>15</td><td>1</td><td>1</td><td>1</td><td>1</td><td>6</td><td>2</td></tr><tr><td>Graphical user interface</td><td>9</td><td>6</td><td>16</td><td>2</td><td>2</td><td>0</td><td>0</td><td>5</td><td>3</td></tr></table>

Table 3

<table><tr><td>Type of tool</td><td>Number of part 2 questionnaires completed</td></tr><tr><td>4GL</td><td>12</td></tr><tr><td>Workbench</td><td>6</td></tr><tr><td>Project management</td><td>4</td></tr><tr><td>Statistics package</td><td>2</td></tr><tr><td>DBMS (without 4GL)</td><td>2</td></tr><tr><td>Expert system</td><td>1</td></tr><tr><td>(Total)</td><td>(27)</td></tr></table>

Each of the following subsections describes the part 2 responses received for a particular type of software tool (as categorized above). The user was asked to supply the following information:

(1) The hardware and operating system on which the tool ran;

(2) The main health application(s) developed using the tool;

(3) The formal selection method carried out before acquiring the tool;

(4) What were the expected benefits and were they achieved;

(5) Was cost a significant factor when acquiring the tool;

(6) The tool's weaknesses and strengths in terms of documentation, vendor support and technical capabilities;

(7) The effects of using the tool on the development process and on the implemented system.

The simplified part 2 mentioned in the section on 'Design of the questionnaire' above asked for a more concise set of answers, but included seven in particular. The answers relating to seven are tabulated in Tables 4 and 5, while the other information is presented in the next sections.

## Fourth generation languages (4GLs)

The classification '4GL' is applied to many products on the market, which may differ widely in their characteristics. The tools included here are those categorized as 4GLs by their users. Six responses referred to the same tool (from Oracle), but overall experience did not appear to differ between tools. The hardware used included PCs (both 286 and 386-based), and larger machines from Digital, Sequent, IBM, Sun and Prime. The most popular operating system was MS-DOS. Others specified were AIX, UNIX, VMS, Xenix, Primos and OS/32. Application areas covered a wide range including GP Clinical records, in-house administration records, community information systems, patient records, medical audit, theatre systems and public health databases. Comments on the use of a formal method for selecting the 4GL indicated two 4GLs adopted after reviewing currently available literature. In four cases, evaluation against other similar tools was carried out. No formal selection method was employed in another two instances. Expected benefits included 'increased speed of development' (in four cases), 'ease of use', 'produce a tailor-made system', 'relatively inexpensive development tool', '(applications) modifiable and enhanced by our own staff', 'tailoring by prototyping to our needs', 'integration of complex functions', 'rapid prototyping of user interface', 'operating system independence'. Overall the users indicated that these objectives had been met. However, in one instance speed of development was slower than expected. Two other users questioned the ease of use of their 4GLs. Cost was said to be a significant factor when acquiring the tool in seven cases, and said not to be significant in three cases.

Weaknesses identified were as follows:

(1) Documentation: 'poor', 'simplistic', 'poorly-indexed', 'poor for first-time users', 'reference-material only', 'poor tutorials', 'tutorials omit detailed functions'.

(2) Vendor Support: 'Poor vendor support', 'not sufficient expertise', 'high cost'.

(3) Technical: 'Inefficient data structures', 'database has slow response times', 'limited functionality of first release', 'limited in supporting relational databases and modifying data structures', 'end up writing 3GL code to get round problems ... thus losing advantages of 4GL', 'the need to write large amounts of C for areas not covered by the built-in programming facilities have slowed things down below what might be achieved', 'screen-handling limitations', 'weak graphics and I/O', 'data dictionary insufficient for all needs', 'hard to really customize the user interface', 'high overheads in screen display', '...is a restrictive programming environment for developing user interfaces', 'default messages cannot be changed by user', 'requires co-processor for adequate speed'.

## Strengths identified were:

(1) Documentation: 'Good' (in two cases), 'small, readable manuals', 'consistent layout'.

(2) Vendor Support: 'Excellent', 'support desk very good'.

(3) Technical: 'Good technical capabilities', 'easy to learn', 'very flexible', 'recovery tools', 'screen painting', 'space efficient data-structures', 'flexibility of relational databases', 'fast to develop/modify applications', 'excellent database', 'uses SQL, a standard 4GL', 'easy to access database from remote PCs and dumb

Table 4 Effects of using the tool-on the development process

<table><tr><td></td><td colspan="4">4GL</td><td colspan="4">Workbench</td><td colspan="4">Project management</td><td colspan="4">Statistics package</td><td colspan="4">DBMS</td><td colspan="4">Expert systems</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Score</td><td>-1</td><td>0</td><td>1</td><td>2</td><td>3</td><td>-1</td><td>0</td><td>1</td><td>2</td><td>3</td><td>-1</td><td>0</td><td>1</td><td>2</td><td>3</td><td>-1</td><td>0</td><td>1</td><td>2</td><td>3</td><td>-1</td><td>0</td><td>1</td><td>2</td><td>3</td><td></td><td></td><td></td><td></td></tr><tr><td>Timescale</td><td>1</td><td>-</td><td>2</td><td>4</td><td>4</td><td>-</td><td>-</td><td>-</td><td>2</td><td>3</td><td>1</td><td>-</td><td>-</td><td>2</td><td>-</td><td>-</td><td>-</td><td>2</td><td>-</td><td>-</td><td>-</td><td>-</td><td>1</td><td>1</td><td>-</td><td>-</td><td>-</td><td>-</td><td>1</td></tr><tr><td>Manpower usage</td><td>-</td><td>3</td><td>1</td><td>3</td><td>4</td><td>1</td><td>-</td><td>1</td><td>2</td><td>1</td><td>1</td><td>-</td><td>2</td><td>-</td><td>-</td><td>-</td><td>-</td><td>1</td><td>1</td><td>-</td><td>-</td><td>1</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>1</td></tr><tr><td>Project control</td><td>1</td><td>5</td><td>1</td><td>2</td><td>1</td><td>-</td><td>1</td><td>-</td><td>3</td><td>2</td><td>-</td><td>-</td><td>1</td><td>2</td><td>-</td><td>-</td><td>2</td><td>-</td><td>-</td><td>-</td><td>1</td><td>1</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>1</td><td>-</td></tr><tr><td>Task integration</td><td>-</td><td>4</td><td>3</td><td>-</td><td>2</td><td>-</td><td>1</td><td>-</td><td>2</td><td>3</td><td>-</td><td>1</td><td>1</td><td>1</td><td>-</td><td>-</td><td>-</td><td>2</td><td>-</td><td>-</td><td>-</td><td>1</td><td>1</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>1</td></tr><tr><td>Quality of work</td><td>1</td><td>2</td><td>3</td><td>3</td><td>2</td><td>-</td><td>-</td><td>-</td><td>4</td><td>2</td><td>-</td><td>2</td><td>1</td><td>-</td><td>-</td><td>-</td><td>-</td><td>2</td><td>-</td><td>-</td><td>-</td><td>1</td><td>1</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>1</td></tr></table>

Key: see key to Table 5 below.

Table 5 Effects of using the tool-on the implemented system

<table><tr><td></td><td colspan="4">4GL</td><td colspan="4">Workbench</td><td colspan="4">Project management</td><td colspan="4">Statistics package</td><td colspan="4">DBMS</td><td colspan="4">Expert systems</td><td></td></tr><tr><td>Score</td><td>-1</td><td>0</td><td>1</td><td>2</td><td>3</td><td>-1</td><td>0</td><td>1</td><td>2</td><td>3</td><td>-1</td><td>0</td><td>1</td><td>2</td><td>3</td><td>-1</td><td>0</td><td>1</td><td>2</td><td>3</td><td>-1</td><td>0</td><td>1</td><td>2</td><td>3</td></tr><tr><td>Completeness</td><td>-</td><td>2</td><td>2</td><td>2</td><td>3</td><td>-</td><td>-</td><td>2</td><td>1</td><td>2</td><td>-</td><td>-</td><td>1</td><td>2</td><td>-</td><td>-</td><td>1</td><td>1</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>1</td><td>-</td></tr><tr><td>Integrity</td><td>2</td><td>-</td><td>1</td><td>6</td><td>1</td><td>-</td><td>-</td><td>-</td><td>1</td><td>3</td><td>-</td><td>1</td><td>1</td><td>1</td><td>-</td><td>-</td><td>-</td><td>1</td><td>1</td><td>-</td><td>-</td><td>-</td><td>1</td><td>-</td><td>-</td></tr><tr><td>User-friendliness</td><td>1</td><td>-</td><td>4</td><td>3</td><td>1</td><td>-</td><td>1</td><td>1</td><td>2</td><td>-</td><td>-</td><td>3</td><td>-</td><td>-</td><td>-</td><td>-</td><td>1</td><td>-</td><td>-</td><td>1</td><td>-</td><td>-</td><td>-</td><td>1</td><td>-</td></tr><tr><td>Reliability</td><td>2</td><td>1</td><td>-</td><td>4</td><td>2</td><td>-</td><td>-</td><td>-</td><td>-</td><td>3</td><td>-</td><td>2</td><td>1</td><td>-</td><td>-</td><td>-</td><td>1</td><td>1</td><td>-</td><td>-</td><td>-</td><td>1</td><td>1</td><td>-</td><td>-</td></tr><tr><td>Efficiency</td><td>4</td><td>-</td><td>-</td><td>3</td><td>3</td><td>1</td><td>1</td><td>-</td><td>-</td><td>2</td><td>-</td><td>3</td><td>-</td><td>-</td><td>-</td><td>-</td><td>1</td><td>1</td><td>-</td><td>-</td><td>-</td><td>1</td><td>1</td><td>-</td><td>-</td></tr><tr><td>Maintainability</td><td>1</td><td>1</td><td>1</td><td>1</td><td>6</td><td>-</td><td>-</td><td>-</td><td>2</td><td>2</td><td>-</td><td>3</td><td>-</td><td>-</td><td>-</td><td>-</td><td>1</td><td>1</td><td>-</td><td>-</td><td>-</td><td>1</td><td>1</td><td>-</td><td>-</td></tr></table>

terminals', 'high performance in disk I/O', 'low size in RAM', 'compatibility across operating systems and machines', 'broad range of hardware platforms', 'runs within commonly available windows environments'.

## Workbenches

Tools included in this group support several stages of systems development. One of the questionnaires returned indicated only exploratory use of such a tool. The responses covered six different workbenches. Hardware used included IBM compatible PCs, VAX/PC, mini-computers and a Prime mainframe. Operating systems were MS-DOS, OS/2, Unix, Primos and VMS MV/X. Application areas covered were patient administration systems, hospital information system, order communications, nursing, pathology and clinical computing. In three cases the chosen tool was compared to those of competitors as the formal selection method. In one case, no selection method was employed at all. Expected benefits included ‘increased productivity’ (in three cases), ‘easier and quicker program maintenance’, ‘easier software distribution procedures’, ‘self-documentation’, ‘bug-free code’, ‘reduced development backlog’, ‘reduced project costs’, ‘forced documentation at each stage’, ‘open standards’, ‘ultrareliable/logically correct applications', 'prototyping', 'controllability'. All these benefits were achieved. Cost was said to be a significant factor when acquiring the tool in 3 cases, and said not to be significant in 3 cases.

## Weaknesses identified were:

(1) Documentation: ‘Reference and technical manuals contained inaccuracies, omissions and were badly presented’, ‘user documentation not provided’, ‘on-line help useless’, ‘very limited discussions’.

(2) Vendor Support: 'UK suppliers are a very small firm'.

(3) Technical: 'No screen painting', 'limited GUI', 'limited speed', 'unable to support Gane and Sarson and de Marco methodologies', 'unable to support object-orientation'.

Strengths identified were:

(1) Documentation: 'Good tutorials', 'excellent documentation' (in two cases).

(2) Vendor Support: 'Personal service'.

(3) Technical: 'Good clear diagrams of any size', 'checking enables development of rigorous methods', 'twenty fold increase in productivity', 'errors for generated code reduced by 75 %', 'SQL', 'full referential integrity support', 'complete flexibility', 'bug-free code', 'self-documentation', 'code re-usability'.

## Project management tools

Four part 2 questionnaires described the use of project management tools, (three referred to the same product). The hardware used included Apple Macintosh and PCs running MS/DOS. The application area was simply project management. One user selected a particular tool because it was the 'accepted industry standard'. Another user had looked at various similar tools but the ability to run on the Apple Macintosh was a requirement. Another user indicated no formal selection method. Expected benefits were 'better planning', 'more precise tracking of projects (partially achieved)', 'ease of planning (not achieved)' and 'presentation'. Cost of the tool was a significant factor in two cases, and not significant in another.

Weaknesses identified were:

(1) Vendor Support: 'High cost of vendor support', 'not tried'.

(2) Technical: 'Very hard to set up links between activities', 'laborious screen handling', 'requires improved progress chasing/recording', 'difficult (long-winded) to change a plan', 'uses a lot of paper', 'more explanation required on how it worked internally'.

Strengths identified were mainly of a technical nature, e.g. 'ease of getting started', 'subprojects capability'.

## Statistics packages

Two part 2 questionnaires were completed detailing use of two distinct statistics packages. The application areas cited were patient throughput and clinical surveys. Weaknesses identified were technical, e.g. 'previous versions do not handle memory well'. Strengths identified were also of a technical nature, e.g. 'flexible, integrated and intuitive'.

## DBMS

Two users described the use of a DBMS (without a 4GL). Each completed a 'simplified' version of part 2. These returns were incomplete and gave very little information. Application Areas were 'various small applications, reports, inventories, etc.', 'patient/staff records'. Weaknesses identified were 'occasional unwieldy method of operation'. Strengths identified were 'good integration of database, spreadsheet etc.', 'speed of application development', 'enables previously undoable projects to be performed relatively quickly', 'speeds up searches', 'powerful, compatible industry standard'.

## Expert systems

One part 2 questionnaire was received describing the use of an expert system. The hardware used was a 386-based PC running MS/DOS. Breast Surgery was the application area and formal selection methods included market survey and cost analysis, followed by a feature-by-feature comparison of those shortlisted. Expected benefits involved rapid implementation of prototypes and easy adaptation and modification. These benefits were achieved. Cost was a significant factor in the choice of the tool.

Weaknesses identified were:

(1) Documentation: 'Sketchy', 'inadequate error message documentation'.

(2) Vendor Support: 'UK distributor went bust, delay while we contacted US suppliers'.

(3) Technical: 'Non-intuitive keyboard use in processing', 'integer only certainty factor calculation', 'small spreadsheet size limit', 'small set of data types', 'limited array size 256 × 256', 'lack of Bayesian probability in uncertainty handling', 'limited printer support', 'lack of double precision and complex number data types', 'lack of structure in records', 'lack of list processing'.

The user stated that, for the application involved, only the problem of inadequate error messages was significant.

Strengths identified were:

(1) Documentation: 'Useful quick reference guide'.

(2) Technical: 'Easy integration of all features — DB, IKBS, reports, spreadsheets, etc.', 'easily learnt syntax', 'easy prototyping', 'the ability to call up into operation any feature from within any other feature makes for versatile and powerful systems'.

## Conclusions

Table 2 above provides comment on the state of use of advanced software tools for developing health computer applications in the UK. Included within it are returns from a number of Health Authorities specifically stating that their policy is to buy-in software and not to develop their own (25 of the 36 who responded). It seems probable that the proportion of such authorities amongst those not replying would be higher.

From Table 2, it may be seen that the only tool types to register 'double-figure' usage in the returns are 4GLs and Statistics Packages. For all types of tool there are more non-users than 'production' users, and in almost all cases ‘non-users’ outnumber the total of ‘production’ and ‘exploratory’ users. The non-user figures are inflated through the existence of organizations in which the use of particular tools is inappropriate (most often because they do not perform the type of work for which the tool type is intended). However, even when the ‘inappropriate’ totals are subtracted from the ‘none’ use totals for each tool type, the only tool types showing users outnumbering non-users are 4GLs, Statistics Packages and Graphical User Interfaces (and this is including the numbers of exploratory users). Assuming that the level of use of tools is likely to be higher amongst those responding to the questionnaire than amongst those who failed to respond, the general level of use of development tools in the health services in the UK is low.

Table 2 shows several other features. The entries giving ‘unsuitable’ as the reason for non-use of a tool type indicate a demand that is not being met by presently available tools. ‘Cost’ and ‘training overheads’ appear to be insignificant as reasons for non-use. In respect of ‘cost’ this might be a surprise result in the context of the UK National Health Service. In respect of ‘training overheads’, one explanation may be that the extent of the training needs associated with the introduction of new software tools is not well recognized.

The result represented by the last two columns of Table 2 — non-use because of ‘lack of experience’ or ‘lack of information’ — indicates a significant need for education and training in the area of software tools for systems development. For many of the tool types, for every organization making some use of such tools (either ‘production’ or ‘exploratory’) there is at least one in which ‘lack of experience’ or ‘lack of information’ is the reason for non-use.

The respondents to the questionnaire (18.8 % of those to whom it was sent) are mainly well-established in health computing (at least 4 years experience) and of wide experience (1 out of 48 was concerned only with applications in a single department). It might, therefore, be expected that they are making more than average use of advanced tools for software development and have fewer problems with their use than would the average user. Even so the proportion of users of any tool type is not more than 35 % and often much lower.

4GLs are the most commonly used advanced software tool. While the weight of opinion is that they are beneficial both in the development process and on the implemented system, there are sufficient negative experiences reported that any organization moving to use a 4GL will wish to tread carefully. Workbench tools supporting more than one stage of systems development were almost always beneficial in their effects on the development process and on the implemented system, and expected benefits had been achieved. Minor danger points appear to be the need for more manpower during development and the possibility of a less efficient implemented system.

Project management tools appear to be generally beneficial, but can increase the timescale and manpower required for a project! Little experience was reported of other tool types, but what there was was favourable to them.

The finding of low levels of use of software tools is similar to that of other surveys in the UK and elsewhere. For example a Yankee Group report 'Case: promise and problems of new tools' estimated that at the end of 1988 only 4% of the 580 000 DP professionals in the USA were using CASE tools (quoted in Informatics, January 1989). The survey made within the Healthbench project also showed this. The latter targeted organizations which had extensive experience in health applications development in the countries represented in the project team. However, a very low level of use of advanced software tools was found. In the context of the Healthbench project it was felt that low usage might be a consequence of high costs associated with introducing new tools into use. The present survey shows that lack of experience and lack of information are seen as more important factors than is cost.

The study set out to try to identify ways in which general-purpose software tools are found to be inadequate for medical and health applications development. None of the specific comments made about any of the tools reported on is oriented particularly to this area of applications. This may be because

(1) General-purpose tools can provide everything that may be wished for;

(2) Current users are not yet able to identify all of the capabilities that they might find useful in software tools.

In many spheres of endeavour it is often difficult to identify what would be useful unless you have both much experience of present facilities and the opportunity to reflect on what would be a better way of doing things. A further piece of research might, therefore, be to propose a set of enhancements for some particular type of tool (e.g. a 4GL to include a patient-record type) and seek comments from potential users in respect of the benefits that might be expected.

## Acknowledgement

The authors wish to thank those organizations and individuals who responded to the questionnaire.

## References

Development World, (1990) (Lewes, Sussex).

Gane, C. (1990) Computer-Aided Software Engineering (Prentice-Hall, Englewood Cliffs, N. Jersey).

McClure, C. (1988) CASE is Software Automation (Prentice-Hall, Englewood Cliffs, New Jersey).

McClure, C. (1989) The CASE experience. Byte, 14, 4, 235–244.

Nolan, R.L. (1979) Managing the crises in data processing. Harvard Business Review, LVII.

Rock-Evans, R. (1989) CASE Analyst Workbenches: A Detailed Product Evaluation (Ovum, London).

## Biographical notes

All three authors are on the staff of the Computer Science Department at Strathclyde University, Glasgow. They have common research interests in the areas of systems development methods and tools, with particular reference to health-care applications of I.T. Donald Millington took his Bsc degree in Mathematics at King's College, London and an MSc in Numerical Analysis and Electronic Computing at Liverpool University. He first joined Strathclyde University in 1972, but spent from 1981–1986 at The New University of Ulster (as it was then named) developing the Department of Computer Science. His industrial experience includes some years in ship-building, and his interest and activities in health service computing span more than 20 years. Current interests include 4GLs and software engineering. Iain M. Tulloch graduated in Mathematics and Computing Science from Glasgow University. After working in Computer Security and Systems Programming within a financial institution, he joined the Computer Science Department at Strathclyde University in order to work on the AIM Healthbench project. He is currently a Teaching Assistant in the Department and researching for an MSc in the area of implementation languages for health computer applications. Edwin M. Gray holds a BA with Honours in Economics and an MSc in Computer Science from the University of Strathclyde, Glasgow. He is a corporate member of the British Computer Society (BCS), a member of its Council and chairman of its Glasgow Branch. In addition to over 13 years experience in teaching and research, he has over 7 years experience as a systems analyst developing management information systems and production control systems in the steel industry and in local Government. He is also the author of several books and papers on systems analysis and software engineering, an invited speaker at information systems conferences and workshops and a course tutor in software engineering and database systems for the Open University, UK.

Address for correspondence: Mr D. Millington, Department of Computer Science, University of Strathclyde, Livingstone Tower, 26 Richmond Street, Glasgow G1 1XH UK.
