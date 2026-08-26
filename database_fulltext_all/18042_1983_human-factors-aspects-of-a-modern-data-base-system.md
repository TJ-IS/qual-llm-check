---
otero_id: 18042
otero_key: "BC4DX388"
title: "Human factors aspects of a modern data base system"
authors: "John D. Joyce; David R. Warn"
year: "1983"
journal: "Information & Management"
doi: "10.1016/0378-7206(83)90017-4"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Human Factors Aspects of a Modern Data Base System

John D. Joyce and David R. Warn
Computer Science Department, General Motors Research Laboratories Warren, Michigan 48090, USA

The focus of this work is to develop tools and procedures so that non-computer specialists can more effectively manage and use data. The results of several research projects over a number of years have given a spectrum of approaches to make data systems easier to use. In our work, the relational model of data was simplified so that novice users could easily understand their data relationships. An algebraic relational command language was developed to bring the power of relational data manipulation to non-programmers. This research was followed by development of an extended command system that allows users to name and describe their data in English words rather than in cryptic abbreviated forms. In parallel with this, a menu interface to a relational system was developed. The degree of completeness of these approaches, the overall effectiveness in actual operation, some data collected from users, and the ease of learning have been analyzed and are reported.

Keywords: Human factors, relational databases, command languages, menu interfaces, user feedback

![](/api/attachments/BC4DX388/fulltext/images/aef30518c82e93248e4d42ad27e958418f93baba0b7b1f96d127f66cfb583c3d.jpg)

John Joyce is a Senior Staff Research Engineer in the Computer Science Department of General Motors Research Laboratories. He holds a B.S. degree from Queen's University (Kingston, Ontario, Canada) and M.S.E. degree from University of Michigan, both in Electrical Engineering. He has been involved in developing relational data base technology and, in particular, developing good user interfaces to bring modern data base techniques to non-computer specialists. He is currently investigating the development and potential uses of knowledge based expert systems.

## 1. Introduction

Several different interfaces to a relational data base system have been implemented at General Motors Research Laboratories over the past decade. The relational data base system we discuss here is called Regis (Relational General Information System [1]). This report highlights the human factors aspects, the benefits, and the limitations of each interface approach. These observations are based on production use of Regis since 1975 by over 200 users in 15 General Motors divisions with over 50 different applications. An estimated 70,000 Regis sessions have been run, over 98% of them have been interactive. In addition to observations and feedback from users, data on some aspects of human factors has also been collected and reported.

At first, relational technology was provided to a new class of users through simplified terminology and a relational algebraic command language. These new users knew their application areas well, but their main tasks were non-programming tasks. These users will be called “end users” when it is useful to distinguish them from others. The second approach is an enhancement of the first. Significant extensions of naming capabilities and the addition of comment facilities within the data base provide an interface that is more compatible with human interactions. A third approach provides a menu interface to virtually all of the relational capabilities in the first two. This interface includes a number of unique features not usually found in menu systems. A fourth approach, which is in initial stages of research and development, provides natural English query support. Only very preliminary observations can be made about this, since no end users have tested it.

![](/api/attachments/BC4DX388/fulltext/images/08f3d4003ab3fdae9d9dca98536743d889e97cdae7a2f800305af18be3ec9dde.jpg)  
machine communication.

The human factors discussed here will focus on those factors directly related to the handling of data bases. Although aspects related to terminal hardware, computer operating systems and surrounding environment are important, the reader should refer to $[2.3]$ for discussion of these.

## 2. Characteristics of Interactive Data Base Applications

Three major classes of operations with data bases are identified from the perspective of their users. These classes have some different and some overlapping human factors needs that are important to recognize in providing suitable user tools.

## 21 Data Input

This class of operations includes the conventional input of data, modification or correction of existing data, and deletion of obsolete or erroneous data. In most applications input of data is the most time consuming: it can be highly repetitive and its cost is frequently underestimated for a new application. Applications have even been abandoned because the effort of keeping data bases current proved more cumbersome than their value.

Data modification needs are very dependent on the quality of source documents. In a recent application, the source documents were repair records that were not only voluminous but were fraught with errors and plagued with missing data. The efforts to get the information entered and corrected (as much as practical) constituted more of the entire project than the ensuing data manipulation and output phases. Even with these apparent disadvantages, this particular project was highly successful. Other applications with high quality source documents, very accurate input operators, or machine generated inputs may make the data editing problem simple.

## 2.2. Data Manipulation

In a number of applications, the most important feature was the ability to carry out, under end user control, sophisticated data analysis, relating data in a variety of ad hoc ways, and condensing large quantities of data into a few important trends or numerical values. Ease of use, power, flexibility, and understanding of the available tools are important criteria for successful data manipulation.

## 2.3. Data Output

To some extent, the role of data output pervades the data input and manipulation operations. Display of information during the input phase can greatly influence the efficiency of entering similar data or of finding and correcting errors. During interactive data manipulation, the quality, ease of use, accessibility and variety of output is a strong factor in getting the job done. The need for high quality output became evident after the relational data management system had been successfully used in several applications. Although a reasonable level of formatting was provided for tabular output and an interactive graph plotting package was available, users wanted to match existing formats and to produce presentation quality reports and graphics. Although an interim solution was to provide a report generator, it became apparent that well labelled information should be the standard output mode, not just for final reports. Presentation style graphics should also be standard, if response time and costs are acceptable.

## 3. Some Human Factors Considerations

## 3.1. Characteristics of Regis

Regis (RElational General Information System) [1,4] is an implementation which supports nearly all of the relational operations originally defined in [5]. It uses an algebraic relational language. In addition, commands for data manipulation, data input, data revisions, graphic output, report formatting, basic statistics, general control, and data output provide users with considerable generality and flexibility. The basic data structure for a user is a set of tables which may be related through data values in designated columns. A single table consists of fixed width columns and a set of rows. The rows can be sorted on any combination of columns. In a deviation from relational theory (as with many other practical implementations), duplicate rows are permitted. In this case, if order or row identification is important, an additional column may be defined and numbered with sequential values. Fig. 1 shows two related data tables that illustrate the basic structures that a user must understand: user named tables, user named columns in each table, and rows of data.

The Regis system was designed to be interactive. Commands are interpreted as they are entered and the results are immediately available to users. For most commands, the results are stored in tables that can be listed, plotted, and saved either temporarily or permanently for future analysis. The following commands are samples of the language that a user has available for data manipulation and analysis. Command words and keywords are shown in upper case and user names for tables and columns and data values are shown in lower case. The names "complete" and "blues" are user named tables that hold the results of the JOIN and SUBSET commands respectively

![](/api/attachments/BC4DX388/fulltext/images/3ad018e0a20f8c3f592af0dfd2df73f992f093bde6abdae99c3a1d0e10f7eb81.jpg)  
Fig. 1. Sample Tables.

## LIST articles

complete = articles JOIN prices type MATCH costtype

SORT complete cost

blues = SUBSET complete WHERE color = blue

Command sequences that are used repetitively can be stored in a file, parameterized, and executed on demand. Commands can also be used in batch mode. Users do most of their work interactively and use command files extensively. Both local high speed terminals and slower remote dial terminals are supported. A majority of interactions occur at remote sites.

## 3.2. Observations on Human Factors Aspects of Regis

Since the standard Regis command system was our first approach to human factors, we now have several years of experience and observations from a variety of people using the system for day-to-day productive operations.

## 3.2.1. Terminology for Selected Data Base Concepts

An initial decision to change the original relational terminology from terms like “relations”, “domains”, and “n-tuples” to “tables”, “columns”, and “rows” has proven to be excellent for the users. This simple terminology conveys enough meaning and relates to terms users have known for years.

The success of this terminology is counterbalanced by the difficulty in teaching end users the differences between two kinds of "files". In an "external file", data are stored on permanent disk storage in character form which may be viewed or edited with a text editor. In an "internal file", the data are stored as exact images of the tables in active computer memory and are only accessible by Regis commands. For internal files, the I/O time is reduced by several orders of magnitude. End users who were not previously programmers have difficulty grasping these concepts.

## 3.2.2. Naturalness of Data Base Operations

Design decisions were made to choose command words and other keywords whose normal English meaning would correspond closely to the data base operation. This approach has been quite successful. A synonym capability was provided to allow users to rename commands or to generate abbreviations. This has been used only sparingly, which might indicate that users are not aware of the synonym facility, but we believe it indicates that users prefer the standard names.

## 3.2.3. Other Syntactical Considerations

Other design decisions were to require full command names and keywords without abbreviations, except for synonyms. This was to insure that users would have better documentation of commands saved for future reference (such as in command files or on hard copy terminals). We believe, from our interactions with users, that this has been beneficial, but we have no experiments to show that it is better than the reduced keystrokes for abbreviations.

No “noise” words are allowed to improve the readability of a command. This rigidity, along with some positional requirements has posed difficulties for some people. The consistency of syntax from one command to another could have been better. This deficiency has also contributed to some user difficulties. Menu approaches, along with sophisticated English query facilities, may be of help to these people.

## 3.2.4. Response Time

All Regis commands are interpretively executed as they are entered. No pre-compilation capabilities have been provided. When the computer systems are not severely overloaded, response times for operations on tables containing a few thousand rows or less has been in the range of 1 to 10 seconds, depending on the table sizes. Very large tables take longer to process, but users expect this. The overhead of parsing individual commands or even small groups of commands in files (typically 1 to 3 milliseconds per command on an IBM 3033) and the use of virtual memory paging for high speed I/O to/from the data base has given good response. The value of good response time has been documented elsewhere [6].

## 3.2.5. User Data Names

User data names are restricted to 8 characters for tables and columns. Although numerous meaningful names fit within this limit, a strong need has been observed for multiple word phrases. Approximately one third of user assigned names are meaningful and nonabbreviated and are certainly preferable to system assigned names (such as V1, V2, V3). Users frequently try to condense abbreviations of phrases into 8 characters and end up with names that are gibberish. Users then make errors typing them or cannot remember the precise names that were used. Some users resort to meaningless names such as X or TEMP or ABC. Providing space for 16 or 32 character names as a single string is only incrementally better than 8.

## 3.2.6. Error Detection and Recovery

Although most commands have good error detection, recovery and informative messages, some commands are poorly diagnosed. Observations on the time lost when errors are not handled properly both for the user and the provider of consultation services indicate that the importance of good error handling can hardly be over-emphasized. A spelling corrector, limited to command names, has been very popular with users. If keyboard errors are made in commands, up to 3 or 4 suggestions are made to the user. Usually the first suggestion is the correct one. It would be useful to extend this facility to all keywords and user assigned table and column names. For correct commands, no overhead is incurred.

## 3.2.7. Data Input and Editing Facilities

A number of the data input and editing facilities are rather weak in the original Regis. Data input for tables that are either predominantly numerical or that have few columns works well. However, data input for tables with many columns or numerous character strings with embedded blanks result in frequent user errors. Data revision commands work more easily on single values or single columns rather than on randomly located values. Application-specific command files have been set up by a number of users to handle their own data input or editing. Their own nomenclature and error checking are usually incorporated in the command files. Better human factored data input and editing facilities have been designed and could be added to Regis without any major modifications. Full screen input and editing facilities would be a welcome addition. In most of the applications, the data manipulation, analysis, and data presentation capabilities have been more important to the users than elaborate data entry or editing facilities.

## 3.2.8. Overall Effectiveness

The overall effectiveness of the Regis system has been high from several perspectives. It has met the goals of bringing data base application development and ad hoc analysis facilities directly to end users. Numerous non-programmers have learned all that was necessary to do their entire data analysis jobs with minimal training and consultation assistance during the course of their projects. Over 20,000 sessions were logged on two computer systems during a recent twelve month period by approximately 70 different users. A few users have had some programming background but most had little or none. The elimination of data processing personnel as intermediaries has greatly speeded the completion and increased the effectiveness of most of the projects. The expertise of the data processing personnel has continued to be focused on large applications, whereas most of the applications on Regis have been relatively small, sometimes transient in nature. However, some medium sized applications have flourished on Regis, because of the ability of the users, with a somewhat more data-independent high level language, to adapt as application demands change.

Several users with previous computer experience have reported a productivity gain of 10:1 to 20:1 for getting a project completed using Regis compared to a conventional approach using a programming language, such as PL/I or Cobol. The relative ease of use of the language, the high level capabilities, the interpretive execution with the ability for immediate corrections or changes, and the relative data-independence are considered to be the main contributing factors.

## 4. An Extended Command Language

## 4.1. The Nature of the Extensions

The Regis command language recently has been extended to handle multiple word names separated by blanks (as in normal English) for all table and column names. Commands that define tables or columns can also include comments associated with them. Since nearly all commands reference a table and possible one or more columns, and since blanks or commas are delimiters in the Regis command language, the command parser had to be extended to handle position dependent information. The multiple word names were allowed a maximum of forty total characters including blanks. A dictionary of names is constructed because individual words may be a part of different table or column names. Only a subset of words that constitute a full name is required in a command to refer to a table or column. A minimally unique set of words in any order will be processed automatically. Less than the minimal set of words to identify a name uniquely will result in a request for the user to choose which name (among two or more) is the correct one.

As one step to reduce the need to deal with file names, the user names a data base, which consists of one or more files containing tables. The user gives the name of this data base at the beginning of a session and does not need to refer to existing files. The dictionary contains, for each table, the name of each file in which the table is located. Reference to any table will automatically reference the file (as needed) without user intervention. Although this approach eliminates the need to remember file names when referencing existing tables, the user must still be aware of files and placement of tables within files when new tables are created. The relationship among the data base, files, tables and columns is strictly hierarchical.

## 4.2. Some Human Factors of Extended Naming

## 4.2.1. Conciseness Versus Natural Meanings

Since many users of computer systems are not expert typists, reducing the amount of typing will reduce the keying errors. Provision of capabilities implemented in both the standard Regis system and the Extended Command System.

<table><tr><td colspan="6">The first 2 rows of table SURV379</td></tr><tr><td>PE. #1</td><td>MAVING</td><td>CITYREG</td><td>OVERECON</td><td>LOCLECON</td><td>PERSECON</td></tr><tr><td>(%)</td><td>41</td><td>95</td><td>2</td><td>2</td><td>2</td></tr><tr><td>%</td><td>41</td><td>93</td><td>2</td><td>2</td><td>2</td></tr><tr><td>YEAR</td><td>THOUSAN1</td><td>THOUSAN2</td><td>GOOPBADT</td><td>NO1PROBN</td><td>NEEDCAN</td></tr><tr><td>1</td><td>3</td><td>$</td><td>3</td><td>19</td><td>5</td></tr><tr><td>2</td><td>3</td><td>$</td><td>2</td><td>2</td><td>5</td></tr><tr><td>16-14</td><td>61MONTH</td><td>TIMEKEEP</td><td>MAKESERS</td><td>SZPURCH</td><td>PLNTOVST</td></tr><tr><td>1</td><td>5</td><td>15</td><td>128</td><td>18</td><td>5</td></tr><tr><td>2</td><td>3</td><td>17</td><td>59</td><td>13</td><td>5</td></tr></table>

Fig. 2. Names Limited to 8 Characters.  
for long names runs counter to a goal of conciseness. From our observations, users desire conciseness, but this is overshadowed by the need to express and document ideas in meaningful phrases. Numerous requests for report generator capabilities originated from a need to label reports in English for management or peer review rather than from the needs to format and summarize information according to aesthetic guidelines.

The Extended Command System has only been used to a limited extent because it is new. Fig. 2 shows a table from a survey data base, where names were constrained to 8 characters. In contrast, Fig. 3 illustrates the use of English words to convey much more meaning [7]. This example is one of the few where a user application has been

<table><tr><td colspan="6">The first row of table MARCH 1979 CONSUMER SURVEY</td></tr><tr><td></td><td>SAVE NUMBER</td><td>CITY AND REGION</td><td>OVERALL ECONOMY</td><td>LOCAL ECONOMY</td><td>PERSONAL ECONOMY TODAY</td></tr><tr><td>1</td><td>41</td><td>43</td><td>7</td><td>2</td><td>2</td></tr><tr><td>2</td><td>41</td><td>43</td><td>2</td><td>2</td><td>2</td></tr><tr><td>3</td><td>$1000MILKALLANCE# #1</td><td>$1000MILKALLANCE# #2</td><td>ARE THESE GOOD OR BAD TIMES?</td><td>NUMBER ONE PROBLEM TODAY</td><td>NEED A CAR?</td></tr><tr><td>4</td><td>5</td><td>$</td><td>3</td><td>19</td><td>5</td></tr><tr><td>5</td><td>6</td><td>$</td><td>2</td><td>2</td><td>5</td></tr><tr><td>6</td><td>FOR FERTIT OF PAYING WITHIN SIX MONTHS</td><td>HOW LONG DO YOU KEEP A NEW CAR?</td><td>MAKE AND SERIES YOU PLAN TO PURCHASE</td><td>SIZE OF CAR YOU PLAN TO PURCHASE</td><td>PLAN VISIT TO DEALER IN NEXT TWO WEEKS?</td></tr><tr><td>7</td><td>5</td><td>15</td><td>128</td><td>18</td><td>5</td></tr><tr><td>8</td><td>5</td><td>17</td><td>59</td><td>13</td><td>5</td></tr></table>

Fig. 3 Names with Multiple Words.

<table><tr><td>Names of Columns</td><td>Number of Columns</td><td>Number of Words</td><td>Words per Name</td><td>Percent English Words</td></tr><tr><td>Single Word Name With 8 Characters Maximum</td><td>183</td><td>183</td><td>1.0</td><td>35%</td></tr><tr><td>Multi-Word Names With 40 Characters Maximum</td><td>143</td><td>347</td><td>2.4</td><td>93%</td></tr></table>

Fig. 4. Use of English Words as Column Names.

Fig. 4 gives an indication of early trends in the changing use of names when better facilities are available. It also shows the use of names in the standard Regis system, where names are constrained to 8 characters. The data for the single word names were taken from a random sampling of users doing production types of work in operating divisions. Only slightly more than a third of the names assigned by users for table and column names were normal English. From observation on the names used, it appeared that the non-English names were often abbreviations of phrases of 2 to 4 words.

Initial data from a few data bases that include both table and column names indicate that users are using phrases that average 2.5 words per name and that 80 to 90% of these words are English words. This data is very similar to that in Fig. 4. These figures may be biased, since early users may be more motivated to use English words.

If the names have little repetitive use of words, 1 or 2 words will suffice to identify the correct table or column. It is not known yet how much this may be used to reduce typing of full multi-word names. The full names are always used for output.

## 4.2.2. Documentation Aids

As previously indicated, facilities are available to attach descriptions to any or all files, tables, and columns in a data base, when using the Extended Command system. Preliminary results indicate that this facility is being exercised. It is too early to tell how extensively this documentation facility will be used or how meaningful the descriptions will be.

## 4.2.3. Response Time

For individual interactive commands or small command files, response times are comparable to the standard Regis system. Clearly, there is additional overhead for parsing commands and some additional cost for resolving ambiguities with the name dictionary. This overhead is typically 1 or 2 milliseconds per command. For applications that execute a few hundred commands for each interaction, response times degrade noticeably compared to the standard Regis system. Both the menu system and the Regis Report Generator were written with Regis commands and suffer response degradation with extended names.

## 4.2.4. Overall Effectiveness

The previous conclusions about the overall effectiveness of the standard Regis system all apply to the Extended Command system. In addition, initial experience indicates that less formal report generation is needed now, since the data is descriptively labeled routinely. Although a formal study of error rates in remembering data names has not been made, we expect measurable increases in effectiveness.

## 5. A Menu Approach to Relational Systems

## 5.1. Highlights of DO-IT Menu system

The DO-IT system provides access to Regis capabilities through a menu interface. Users do not have to learn or remember commands; they simply make choices from a menu. As an indication of the flexibility of the Regis commands, most of the menu system has been written in Regis command files with only small high use portions written in PL/I. Fig. 5 is an example of the top level menu. The menus are all defined in Regis tables for flexibility in developing and modifying the menu system. This technique allows the user to tailor the menu system to particular applications. Each menu option is typically supported by one or more command files.

There are three methods of getting to a desired menu selection. The first is the obvious one of making choices, hierarchically descending through menus and returning by the same route. The second method is to specify a sequence of numeric menu selections. This permits an experienced user to skip menus or jump to a selection on a different branch.

```txt
******** DO-IT ******** MENU O
DATA MANAGEMENT AND ANALYSIS
1. TABLE MANAGEMENT
2. TABLE EDITOR
3. SELECT ROWS
4. COMBINE TABLES
5. ANALYZE DATA
6. DISPLAY RESULTS
7. FILE MANAGEMENT
8. CUSTOM MENU FACILITY
L. LIST CURRENT TABLE = "UNKNOWN"
T. SPECIFY CURRENT TABLE = "UNKNOWN"
F. SPECIFY CURRENT FILE TO CONTAIN NEW TABLES
S. SAVE CURRENT FILE = "WORKFILE"
? . HELP.
R. RETURN.
ENTER SELECTION:
```  
Fig. 5. Top Level Menu.

The third method is the most novel and frequently the most useful. Instead of giving a numeric selection or sequence, the user can enter a keyword (or character string) that is thought to be present in one of the menus. The system automatically creates a dynamic menu which includes all the selections containing that keyword. These selections may actually be from several different menus. For example, the various "delete" options for rows, columns, tables or files are in different menus. "Delete" selects all choices in which "delete" appears and constructs a menu as shown in Fig. 6. After the operations selected from this menu are completed, the user returns to the previous menu.

Some of the other features of the menu system will be brought out as we discuss various human factors of this approach.

```txt
DELETE
1. DELETE TABLES.
2. DELETE ROWS.
3. DELETE COLUMNS.
4. DELETE A RANGE OF ROWS.
5. DELETE SELECTED ROWS.
6. DELETE ROWS WITH DUPLICATE VALUES IN SPECIFIED COLUMNS
T. SPECIFY CURRENT TABLE = "UNKNOWN"
R. RETURN.
ENTER "DELETE" SELECTION
```  
Fig.6. Dynamically Created "DELETE" Menu.

5.2. Some Human Factors of the DO-IT Menu System

## 5.2.1. Ease of Learning

The DO-IT menu system is very easy to use. With the combination of menus defined with meaningful English phrases and liberal availability of "help" messages, users have had little trouble becoming effective users. Nearly all function of Regis are available through menus. Users primarily need to learn the functions that can be performed with tables since the commands and syntax are hidden. One application was implemented in part by a law clerk who had only a few minutes of supervised training and no computer background. More than 40,000 rows of data in 38 tables were entered verified, and corrected. Restructuring of the data base was done by adding or rearranging columns between tables as the application progressed. The added feedback when entering or modifying data and prompting for choices was all the assistance needed by the clerk. Less consultation was required on this application than any done with the Regis command language.

## 5.2.2 Conciseness of Input

Data base functions, table and column names are normally all selected by a single key stroke. This not only makes it easy to use, but also practically eliminates typographical errors. Utility selections are available from all menus to provide access to frequently needed functions, such as "listing a table". Many shortcuts are provided for experienced users, so that the menus do not get in the way. For example, when multiple selections can be made from a menu, a list of choices can be given.

## 5.2.3. Built-in Context

Knowledge of the data structure and underlying commands is used to present only those choices which are valid in a given context. This is also used to determine when to prompt for selections of file names, table names, or column names. The appropriate list of valid choices are presented. In certain commands, columns containing numeric data may be the only correct ones; then only numeric column names will be displayed.

When results of an operation are stored in a table, that table becomes the current table for the next operation. This usually matches the demand patterns. For those commands in which it is known that two input tables are required, menus automatically prompt the user for the second table name, and provide the user with a list of tables from which to select. This both reduces the number of selections to consider and eliminates the possibility of an invalid choice.

## 5.2.4. Error Checking

Error checking facilities are built into the menu system to check data entries or parameters in the appropriate context. For example, data input values entered by the user are checked against the data type of the corresponding column. Invalid entries are rejected (with an appropriate message to the user) before they are added to the table. The overall philosophy is error prevention rather than error detection. These capabilities are easily extended for application dependent error checking.

## 5.2.5. User Terminology Via Custom Menus

Frequently, users do not need all the generality of the standard menu system. To tailor applications, a custom menu building facility has been provided. Users design their own menus in their own terminology using the standard menu system. These menus can be supported by either standard system or user written command files. Users may then operate exclusively with their own menus or with a combination of their own and standard menus.

## 5.2.6. Flexibility Among Approaches

The DO-IT menu system has provided flexibility in several flavors. Although the system is designed as a self-sufficient front end, the ability to switch interchangeably between Regis commands and menus is available from nearly all menus. The operating system command language can also generally be invoked. DO-IT is also compatible with both the standard version of Regis as well the Extended Command version.

## 5.2.7. Response Times

The menu system was written almost entirely in

Regis commands, with the exception of a few high use functions programmed in PL/I. Since a single data base command and its parameters are often selected by interactions with several menus, it is vitally important that the response time for processing a single menu choice and displaying the next menu be very short. We have observed that under conditions of heavy load the response time of the menu system is inadequate. The overhead of interpreting numerous Regis commands for each menu is too great, particularly if the Extended Command system is also being used. Extra references to the name dictionary incur additional paging and computer time overhead.

During periods of normal or light loading, the menu system performs well. We believe that if the menu system were programmed in PL/I (as Regis is), the reduction in overhead would give good response time.

## 5.2.8. Overall Effectiveness of a Menu System

As long as reasonable response times are maintained, the menu system is very effective. The considerable reduction of errors and the much reduced need to remember command names, keywords, table names, column names, and parameters make the menu system a very user-friendly interface. With CRT terminals connected by high speed lines to the computer, the menu system does a good job of sending much information to the eyes, (which have a high bandwidth), while at the same time requiring a very minimum of keyboard input (which matches the low input bandwidth of unskilled typists). For slow hardcopy terminals, an option is provided to eliminate repetition of the same menu, etc.

The overall experiences to date from user feedback indicates that menus are a very effective way to communicate with relational data bases.

## 6. Observations on Various Approaches

## 6.1. Algebraic Command Language

The algebraic command language approach, as implemented, has provided an easy method for many end users to develop, modify, and operate their own applications. These users have been given an increased capability to develop data processing procedures directly and to carry out ad hoc analyses on their data. This capability could not be provided in a timely fashion even by high quality programming staff in conventional computer languages. Bypassing the data processing department has enabled numerous applications to be completed more quickly and freed up programming staff to concentrate on large complicated applications.

However, the users must have an aptitude for logic and be able to pay attention to details. Some users need considerable training, while others adapt easily.

## 6.2. Extended Command System

Fundamentally, the Extended Command system uses the same technology as the algebraic relational language. The data we have collected to date, however, indicates that the use of multiple words for table and column names more than doubles the percentage of English words used (80 to 90% compared to less than 40% in the standard Regis language with single word 8 character names). While the ultimate increase in user effectiveness of this facility is unknown, the intuitive observations of users indicate better communication with other people interested in the same data base information, better recall of nicely labelled data when a user returns to the data, and reduction in errors. This facility has resulted in an upgrade in the readability of output.

## 6.3. DO-IT Menu System

The menu system has its greatest impact on new or infrequent users. They can quickly become productive with a minimal amount of learning. This conclusion is based on the amount of consultation provided to help users. It appears that the menu system provides considerably improved data input and editing for all users. Unless the menus are processed very quickly, the experienced user will revert to the command language. This appears to be an indictment of the implementation approach and system load rather than the menu interface itself.

## 7. Areas of Future Study

Research work is underway to provide capabilities to decode typed English for a variety of queries and data manipulations against a relational data base. We have not progressed far enough for any experimental use of such a system. This step is expected to be a valuable part of a spectrum of approaches. It is not, however, considered the ultimate method of communicating, even if English can be processed very well. We believe that a user should be able to intermix a variety of modes of communication.

Experiments would be very useful for studying the important human factors of using computers with different approaches. Quantifying the effects on learning time, retention time, problem solving ability and the time to get jobs done are important [8]. We now have approaches to compare and a set of production users. A considerable amount of instrumentation has been built into Regis which can be easily extended to gather other human factors data. Among the impediments are: difficulties in designing “controlled” experiments, inability to extrapolate results to other environments, differences between individuals, and a reluctance to allocate user time for any “controlled” experiments which do not contribute directly to their own job. Getting productive users to solve the same problems two ways for comparison is hard to accomplish.

## Acknowledgements

Numerous people have made significant contributions to the design, implementation and the evaluation of approaches described in this paper. Carole Hafner has been a major contributor to the design and implementation. Jim Apsey has provided feedback from his contacts with users.

## References

[1] J.D. Joyce and N.N. Oliver, REGIS - A Relational Information System With Graphics and Statistics, in Proceedings of the AFIPS National Computer Conference, Volume 45 (1976), 839-844.

[2] M. Marcotty, Human Factors and Productivity, in Share Secretary Distribution, Proceedings of Share 56, General Session (March 1981).

[3] T. Gilb, G.M. Weinberg, Humanized Input (Winthrop Publishers, Inc., Cambridge, Massachusetts, 1977).

[4] J.D. Joyce and N.N. Oliver, Preliminary Users Manual for REGIS Information System, Research Publication GMR-2008, General Motors Research Laboratories, Warren, Michigan (October 1975).

[5] E.F. Codd, A Relational Model of Data for Large Shared Data Banks, Communications of the ACM, Vol. 13, No. 6 (1970) 377–387.

[6] W.J. Doherty, Commercial Significance of Man-Computer Interaction, IBM Research Report RC 7297, IBM Thomas J. Watson Research Center, Yorktown Heights, NY (1978).

[7] C.D. Hafner, Incorporating English Descriptions Into a Relational Data Base, Information Systems, Vol. 7, No. 2 (1982).

[8] P. Reisner, Human Factors Studies of Database Query Languages: A Survey and Assessment, ACM Computing Surveys, Vol. 13, No. 1 (March 1981) 13–32.
