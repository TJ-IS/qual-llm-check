---
otero_id: 17544
otero_key: "5RX82H33"
title: "A natural language processing based group decision support system"
authors: "Sumali P Conlon; Brian J Reithel; Milam W Aiken; Ashraf I Shirani"
year: "1994"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)90002-7"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A natural language processing based group decision support system

Sumali P. Conlon \*, Brian J. Reithel, Milam W. Aiken and Ashraf I. Shirani

Department of Management and Marketing, School of Business Administration, University of Mississippi, University, MS 38677, USA

Group Decision Support Systems (GDSSs) are currently used primarily as surface-level discussion tools. That is, current GDSSs do not allow group members to easily access information in deeper levels, such as the data base, model base, and application programs. This paper describes ways in which GDSSs can be improved by using a natural language interface to allow group members to communicate with deeper-level information systems using human languages. The system consists of database, model base, application programs and natural language interface system. The system is designed to both route questions to appropriate subsystems and translate these questions into the computer language controlling these subsystems. Finally, experimental results demonstrate the feasibility of the technique.

Keywords: Group decision support systems; Artificial intelligence; Information retrieval; Natural language processing; Computational linguistics; Lexical database; Lexicon; Semantics; Database; Model base; Data directory

![](/api/attachments/5RX82H33/fulltext/images/3d09775dabafb9bf582e1ae2ff4d3e2634d3ae9d8a1aef73ba18f948a829a072.jpg)

Sumali P. Conlon is Assistant Professor of Management Information Systems at the University of Mississippi. She received a B.A. in statistics from Thammasat University, Thailand, an M.S. in Mathematics from University of Nebraska-Kearney and a Ph.D. in Computer Science from the Illinois Institute of Technology, Chicago, Illinois. Her research interests include Natural Language Processing, Knowledge Representation, Expert Systems, Databases, Information Retrieval,

Group Decision Support Systems and Software Engineering.

## 1. Introduction

A growing body of research has shown that Group Decision Support Systems (GDSS) improve decision efficiency and effectiveness $[7,8,9,10,12,13,18]$ . However, most current GDSS tools support group meetings at the surface level only.

![](/api/attachments/5RX82H33/fulltext/images/b8813a170f7b3d3010a356f64483796ba065b8e39607d5d90a1438fd67e36bb8.jpg)

Brian J. Reithel is an Assistant Professor in Management Information Systems at the University of Mississippi, University, MS 38677. He has been the author of several papers for regional, national, and international conferences. His current research interests are in the areas of quality of user-developed applications, strategic use of information systems, multiple-criteria decision-making aids, and computer-aided software engineering. He received a PhD (Management In formation Systems) and an MBA from Texas Tech University. He earned the BBA from Eastern New Mexico University.

![](/api/attachments/5RX82H33/fulltext/images/935642e6148f5f5cd331e9b5837ab4237713534a43c806734d543b39d839029d.jpg)

Milam Aiken received the B.S. degree in Engineering and the M.B.A. degree from the University of Oklahoma, the B.A. degree in Computer Science and the B.S. degree in Business from the State University of New York, and the Ph.D. degree in Management from the University of Arizona. He is currently an Assistant Professor of Management information Systems in the Department of Management and Marketing at the University of Mississippi. His re- Artificial Intelligence and Group De

search interests include Artificial Intelligence and Group Decision Support Systems.  
![](/api/attachments/5RX82H33/fulltext/images/cdfa76eb385fac33db045573e13fff0a077028317d692fd9fe63ed515387fbba.jpg)

Ashraf Shirani is a doctoral candidate in Management Information Systems at the University of Mississippi. He received the master degree in international development from Cornell University, and the Master of Business Administration degree from the University of Arkansas. His research interests include group decision support systems, information technology markets, and information systems for global competitiveness.

These tools typically support idea generation, issue identification, policy formulation, voting, and other tasks. Very little research has mentioned the other three important parts of GDSSs: the database, model base, and application programs $[1,2,9,15]$ . It would be very useful if group members could, with little effort, take advantage of information already possessed by the organization to improve the effectiveness of their discussion and decision-making. Such information can be in the form of data in databases, or statistical models, linear programming models, or graphics in the model base.

Currently, it is very difficult for group members to access the deeper information needed for effective decision-making. Group members must ask the group facilitators to help them if they need information available through the system; many times, there may not be enough human facilitators to help all group members when they need help.

In this paper, we present ways in which a natural language processing system (NLP) can serve as both an interface and a facilitator for a GDSS. This system can help group members retrieve data from the database and model base as well as use application programs. The system will accept human language commands presented by group members, analyze the commands to determine which part of the information system each command should be directed to, convert the natural language command into the language that controls this part of the information system, and send the converted command to the appropriate part of the system. This will make it easier to use the system and increase meeting efficiency. At the same time, it will increase the quality and quantity of useful information available to users. The NLP interface will also free up the human facilitator's time to allow the facilitator to focus on problems that the interface cannot solve.

Section 2 describes some of the obstacles to an ideal, easy-to-use GDSS. NLP technology and some current business applications are described in Section 3. The overall model of the NLP-GDSS is presented in Section 4. Section 5 describes aspects of how the system decides where to direct user inquiries. Section 6 presents an example of how the system handles inquiries in a GDSS session based upon a laboratory experiment, and Section 7 concludes the paper.

## 2. Why is it difficult for group members to use information bases?

GDSS researchers try to improve the quality of GDSSs by developing tools to help group members in the meeting and to reduce the work load of the human facilitators. As mentioned earlier, existing tools support only the surface level (meeting or discussion tools). The three important components of a decision support system – data base, model base, and application programs – have been neglected by GDSS research. Most current GDSSs do not include tools which help group members use these components easily. In attempting to use other DSS components, group members encounter the following difficulties:

(1) Available information: group members may not know what data is available in the database and model base.

(2) The complexity of the information system: the information system might be too complex for members to know how it is organized (e.g., whether the information is in the database, model base, application programs, or some combination).

(3) Technical knowledge: group members may not know how to operate each individual software package (DBMS, IFPS, spreadsheets, SAS, or custom application programs).

These obstacles can be overcome if the GDSS is well-organized and controlled by an intelligent interfacing system that allows group members to gain access to information easily via natural language requests.

## 3. Natural Language Processing systems (NLP)

The most convenient way for people to communicate with each other is by using their own language [3]. In this paper, we suggest a natural language processing system that allows users to communicate with each other, and also with information systems using their own language (such as English). This system allows group members to request information from the information base by themselves, without having to ask the facilitators for assistance.

Natural Language Processing is the subarea of artificial intelligence that attempts to make it possible for humans to communicate with computers using human languages. This is a very

difficult area, because human languages are extremely large and complicated. In order for computers to be able to understand and generate languages, complex systems are necessary, that include advanced artificial intelligence techniques (searching algorithms, heuristic methods, knowledge representations techniques, etc.) and large knowledge bases, containing information about every word, as well as knowledge about subject areas dealt with by the system (content and context).

In the process of analyzing languages, NLP systems must use information about syntax (sentence structure), semantics (sentence and word meaning) and pragmatics (context). The major parts of NLP systems consist of:

![](/api/attachments/5RX82H33/fulltext/images/e111f75080535396587494033c81a4485e5571d1160b71d45aa95d65ffa3075f.jpg)  
Fig. 1. Natural language interface-group decision support system architecture.

(a) the lexicon, which contains information such as correct word spelling, a word's part of speech, syntactic behavior, and semantic roles;

(b) the parser, which analyzes sentences and converts them into parse trees that are easier for the computer to process;

(c) the language understanding system, which analyzes the parse trees to find the meanings of the corresponding sentences;

(d) the text generation system, which generates either computer language or natural language text;

Current research in NLP focuses on Natural Language Interfaces $[16,17,19]$ (interfaces to databases, expert systems, and other application programs), Natural Language Understanding, Text Generation, Tutoring Systems (which teach people in some specific subject area), and Machine Translation Systems (which translate text in one language into other languages). In this paper, we will discuss the Natural Language Interface (NLI), because this is the area that may be the most useful for GDSS developers.

NLI systems allow users to interact with databases and model bases using human language $[6,19]$ . The NLI system translates human language input into the language that the DBMS and model base systems can understand. A sample query like “Who is the manager of the sales division in the area that made the most sales last year?” can be translated into the relational database language SQL (Structured Query Language) as:

SELECT EMP\_NAME FROM SALE, EMPLOYEE

WHERE AMOUNT\_SALE = (SELECT MAX (AMOUNT\_SALE) FROM SALE)

AND SALE.REGION = EMPLOYEE. REGION

AND EMPLOYEE.POSITION = 'MANAGER'

AND SALE.YEAR = 1992

## 4. A Natural Language Processing-Group Decision Support System (NLP-GDSS)

In this section, we describe a model of a GDSS which incorporates an NLP system interface. This system must be intelligent enough to understand what group members are asking (that is, it must understand their questions/sentences). It must also know where information is stored (whether in the database or model base, and in which part of the relevant subsystem). Finally, it should know what language the users' questions should be translated into (data base, model base, or programming languages) and be able to translate questions into the appropriate languages. To handle these problems, system developers must understand how NLP systems work. They must also understand how software packages are developed. These two types of knowledge will allow developers to develop a GDSS interface which is user-friendly and efficient. Figure 1 shows the architecture for an NLP-GDSS system.

The following narrative describes each part:

(1) Meeting Tools. This part serves as the discussion tool for the surface level. It might consist of Electronic Brainstorming, Voting, Policy Formulation, Enterprise Analyzer, or Discussion (tools found in the University of Arizona's Group Systems) [9,18]. These tools allow group members to interact with each other just as they do in current GDSS.

(2) Natural Language Processing System. When group members need information in the database or model base, or want to use available application programs, they can ask the system through the NLP interface. Group members can simply type a normal sentence such as “I want to know the names of sales representatives in the northern region.” The NLP system will then analyze this sentence, find out where the needed information is stored, translate the sentence into the relevant system language, and then send the question to that system.

(3) Database. A database is a collection of interrelated data organized in such a way that it corresponds to the needs and structure of an organization. Databases are usually organized by database management systems (DBMS).

(4) Model base. A model base is a software package that includes statistical, financial, marketing, accounting, and other quantitative models that provide the system's analytical abilities. Model base tools include spreadsheets, Interactive Financial Planning Systems (IFPS), and Evaluation Planning Systems.

(5) Application Programs. This part consists of programs built by system developers to deal with problems which other parts cannot handle.

## 5. How does the system work?

In this section, we discuss how the NLP system can determine which part of the GDSS a group member wants to communicate with. At any given point in time, a group member may want to communicate with other group members, the database, the model base, or application programs. Because group members use their own language (English, for example) to communicate with the system, it could potentially be very difficult for the NLP system to determine the intended receivers of a given sentence. The following describes how the NLP interface could decide where to send messages:

(1) Should questions be sent to other group members or the information system?

There are at least two conceivable ways to handle this problem. First the NLP system could analyze every sentence and decide whether a sentence is intended for other group members or the information system. This approach makes the system very slow, because parsing takes a lot of CPU time and memory space. Furthermore, if the parser cannot find every word from the input sentence in the lexicon, it will reject the sentence. Thus, the system will face two problems: time loss and system failure.

In the second approach, the user specifies in the comment whether or not the question is directed to the system or to the group as a whole through a signal such as “!SYS” or “??” somewhere in the text. When the NLP interface finds a sentence that starts with “!SYS” or ends with “??,” it will analyze this sentence. Thus, the NLP interface will not have to process unnecessary sentences. This will improve system efficiency.

(2) Should questions be sent to the database, model base, or application programs?

This problem can be solved through a data directory, which indicates where each type of information is stored. The data directory will work with the lexicon in providing information to the NLP system. The directory may contain information such as:

customer DB T(customer)
customer name DB T(customer) ATT(cust\_name)
effect of wages MB (financial model of firm)
regression MB (SAS)

This indicates that information about “customer” is in the database, in a table named “CUSTOMER.” Similarly, the “customer name” is also in the database, in a table named “CUSTOMER” and with an attribute name “CUST\_NAME.” On the other hand, “effect of wages” is in the model base, in a simulation model called “financial model of firm,” which may be written in a spreadsheet such as LOTUS 1-2-3. The results of a “regression” can be found by using the statistical package “SAS.”

(3) How would the system understand different words that represent the same thing?

Normally, group members could use a number of different expressions to talk about one thing. For example, a user might use the word “buyer” for the concept which corresponds to the word “customer” in the data directory. In such a case, it is necessary to somehow translate the user’s request into terms that can be related to the data directory. This could be accomplished with the help of the lexicon.

The basic types of information that a lexicon contains include syntax, semantics, and pragmatics $[4,5]$ . Two types of information which are especially helpful for supporting the data directory include synonyms (buyer SYN customer), and taxonomy (manager ISA employee). This information can help NLP systems analyze sentences and determine what type of information the user wants. The following shows some types of lexical-semantic information that a lexicon can contain:

Manager ISA employee buyer SYN customer secretary ISA employee total SYN sum programmer ISA employee average SYN mean

This type of information will help the NLP system connect words used by group members to words listed in the data directory. The data directory could then be used to determine where the desired information is located. For example, the system could use the lexicon to conclude that the category “employee” includes managers, secretaries, and programmers. This means that, if a group member needs information about programmers, the NLP system can search for information about “employee.”

It should also be noted that sometimes the structure of questions may suggest which part of the system a question should go to. For example, questions which begin “What is…” may be more likely to be directed towards the database, while questions which begin “What would be the effect of…” may be more likely to be directed towards the model base.

Finally, the system could reduce errors if, after relating a question to terms used in the data directory, it paraphrased the question using the terms from the directory. For example, if the user asks, “Who was the biggest buyer last year?” the system could ask back, for example, “Do you want to know the customer with the largest purchases in 1992 (y/n)?”

After the system knows which part of the system a group member's request should go to, the command generator will start to generate the associated commands for that subsystem. The result will be returned from the component that contains the information requested. If the system cannot find the requested information, the NLP system may ask the group member for a more detailed statement of the question.

## 6. Examples of NLP use

Incorporation of an NLP interface allows group members to communicate with the database and model base components of the GDSS. User interactions in the GDSS environment can proceed in the usual ways, allowing Electronic Brainstorming, Voting, Policy Formulation, and Discussion $[18]$ . However, users can also ask for information from the database and model base and use the application programs. A typical interaction might proceed as follows:

(1) I think our company needs to increase wages in order to attract more qualified workers.

(2) What would this do to costs?

(3) I'm not sure. !SYS What would happen to costs if we raised wages by \$0.50 per hour?

The NLP system will know that the third sentence is a sentence that requests information from the information system. The parser in the NLP system will parse the sentence “What would happen to costs if we raised wages by \$0.50 per hour?” The “what would happen…” structure of the question might suggest that the question is directed towards the model base. Then, by using information in the lexicon and data directory, the key words “costs” and “wages” might suggest that the question should be directed to a financial model of the firm in the model base, if one exists.

If a financial model of the firm capable of relating wages to costs exists in the model base, the interface will translate the question into commands capable of controlling this model. If the question is too vague, the system might ask for more details, such as year or type of worker.

An experiment was conducted using the GDSS-based NLP data retrieval system. Twenty-one undergraduate Management Information Systems students (split into two groups) who had never used a GDSS used the system to discuss MIS curriculum changes. Two supporting ASCII text files of information (a course catalog and business student records) were used by the data retrieval system to enhance the discussion. Excerpts from the transcript of the meeting appear in Figure 2. In this figure, questions directed to the NLP data retrieval system are specified with “??” appearing at the ends of the comments, and the system’s responses are enclosed in “<>”.

The hypotheses under investigation were:

$H_{0}$ : The NLP system retrieves information faster than humans can retrieve information.

$H_{A}$ : The NLP system retrieves information slower than humans can retrieve information.

Table 1 shows human and computer performance results from the experiment. Before the

![](/api/attachments/5RX82H33/fulltext/images/849f7a2136671aee055c712a52d22fe90dabbc284b096b585707fbb726ecea9a.jpg)  
Fig. 2. Brainstorm screen showing edit feature.

Table 1
Performance of the system

<table><tr><td rowspan="2"></td><td rowspan="2">Computer</td><td colspan="4">Human</td></tr><tr><td>Min</td><td>Max</td><td>Avg</td><td>StdDev</td></tr><tr><td>Task 1 (secs)</td><td>0.168</td><td>5</td><td>414</td><td>107.8</td><td>114.6</td></tr><tr><td>Task 2 (secs)</td><td>0.172</td><td>10</td><td>270</td><td>71.1</td><td>69.0</td></tr><tr><td>Task 3 (secs)</td><td>0.223</td><td>18</td><td>123</td><td>74.0</td><td>30.9</td></tr><tr><td>Task 4 (secs)</td><td>0.219</td><td>3</td><td>80</td><td>31.2</td><td>23.4</td></tr></table>

All time differences between the human and computer were significant at p < .001.  
Task 1: What courses are offered by Computer Science?  
Task 2: What courses are required by MIS?  
Task 3: What is the average GPA of MIS students?  
Task 4: What is the number of MIS students?

GDSS session, participants were asked to retrieve information from the two text files to answer four questions. Even though the participants were told the names and locations of the text files and how to access them, their retrieval times were significantly greater than the computer's retrieval times (as determined by a matched-pairs T-Test on the 21 observations), lending support for $H_{0}$ . Further, the text files were very small (less than 20 records each). In an actual meeting, participants would not be expected to know where the information was located or how to access it, consequently greatly increasing the data retrieval times.

Table 2 shows participants' perceptions on the relevance of the queries and the understandability of the NLP system's answers. On average, participants thought the questions were relevant, and they were able to understand the system's answers.

Table 3 shows participants' satisfaction with the discussion and the system. The group members were moderately satisfied with the discussion and the GDSS and most preferred using the enhanced GDSS (with the NLP-based retrieval system) over using a standard GDSS. Group members were more certain that the NLP system provides faster, more accurate answers and that the system will enhance the productivity of a group. The only significant correlation among these measures occurred between question #4 “preference for using the system” and question #5 “perception that the system provided faster, more accurate answers” (R = 0.48, p = 0.027).

Understanding and relevance

<table><tr><td rowspan="2">Task</td><td colspan="3">Understood</td><td colspan="3">Relevant</td></tr><tr><td>Min</td><td>Max</td><td>Avg</td><td>Min</td><td>Max</td><td>Avg</td></tr><tr><td>1</td><td>3</td><td>5</td><td>4.6</td><td>2</td><td>5</td><td>4.0</td></tr><tr><td>2</td><td>3</td><td>5</td><td>4.52</td><td>2</td><td>5</td><td>4.52</td></tr><tr><td>3</td><td>3</td><td>5</td><td>4.43</td><td>1</td><td>5</td><td>3.8</td></tr><tr><td>4</td><td>3</td><td>5</td><td>4.38</td><td>2</td><td>5</td><td>3.75</td></tr></table>

Was the computer's answer understandable?  
Were the question and answer relevant to the discussion?  
Task 1: What courses are offered by Computer Science?  
Task 2: What courses are required by MIS?  
Task 3: What is the average GPA of MIS students?  
Task 4: What is the number of MIS students?  
Scale: 1 = strongly disagree, 2 = moderately disagree, 3 = neutral 4 = moderately agree, 5 = strongly agree.

Satisfaction with the system

<table><tr><td>Question</td><td>Min</td><td>Max</td><td>Avg</td><td>StdDev</td></tr><tr><td>1.</td><td>1</td><td>5</td><td>3.76</td><td>0.99</td></tr><tr><td>2.</td><td>1</td><td>5</td><td>2.28</td><td>1.31</td></tr><tr><td>3.</td><td>3</td><td>5</td><td>4.11</td><td>0.81</td></tr><tr><td>4.</td><td>1</td><td>5</td><td>3.67</td><td>1.46</td></tr><tr><td>5.</td><td>1</td><td>5</td><td>4.14</td><td>1.35</td></tr></table>

Questions Asked of 21 Group Members:  
1. I am very satisfied with the group discussion.  
2. I am very dissatisfied with the GDSS.  
3. The data retrieval program will enhance the productivity of the group.  
4. I would prefer using the GDSS with the retrieval program over using the GDSS without the retrieval program.  
5. The data retrieval program provides more accurate answers, faster than I can provide them.  
Scale: 1 = strongly disagree, 2 = moderately disagree, 3 = neutral, 4 = moderately agree, 5 = strongly agree.

## 7. Conclusions

This paper suggests a way to improve GDSSs by inclusion of a natural language interface. The system design is also presented. In particular, the role of the data directory and lexicon in the information routing process is described. Finally, the paper presents experimental results which show that an NLP data retrieval system is significantly faster than manual retrieval, and group participants are generally satisfied with the automated support.

The combination of natural language processing techniques with current GDSS technology can improve the usefulness of GDSS significantly. An NLP-GDSS system allows group members to use information in the information base more frequently. This improves the quality of the discussion because group members have easy access to a large amount of relevant information. In addition, the NLP interface will reduce the amount of query-handling required of the facilitators, and so, allow facilitators to focus on problems which the interface cannot handle.

Thus, group members, who may not have technical knowledge, will be able to take advantage of the organization's currently existing information system, as an important tool for improving the quality of the group discussion.

Acknowledgements: This research has been supported in part by the University of Mississippi's School of Business Administration Summer Research Grant Program. We would like to thank Dr. John Conlon for his substantial comments and contributions to this paper.

## References

[1] M. Aiken and J. Carlisle, An Automated Idea Consolidation Tool for Computer Supported Cooperative Work, Information and Management, Vol. 23, 1992. pp. 373–388.

[2] M. Aiken, O. Liu Sheng and D. Vogel, Integrating Expert Systems with Group Decision Support Systems, ACM Transactions on Information Systems, Vol. 9, No. 1, January 1991, pp. 75–95.

[3] M. Aiken, J. Martin, A. Shirani and T. Singleton, A Group Decision Support System for Multicultural and Multilingual Communication, Decision Support Systems, forthcoming.

[4] S. Conlon, M. Evens, T. Ahlswede and R. Strutz, Developing a Large Lexical Database for Information Retrieval, Parsing and Text Generation Systems, Information Processing and Management, Vol. 29, No. 4, 1993, pp. 415–431.

[5] S. Conlon and M. Evens, A Lexical Database for Nouns to Support Parsing, Text Generation and Information

Retrieval, Research in Humanities Computing, Oxford: Oxford University Press, forthcoming.

[6] J. Davidson and S. Kaplan, Natural Language Access to Databases: Interpreting Update Requests, American Journal of Computational Linguistics, Vol. 9, No. 2, 1983, pp. 57–68.

[7] G. DeSanctis and J. Courtney, Toward User Friendly MIS Implementation, Communications of the ACM, Vol. 26, No. 10, October 1983, pp. 732–738.

[8] G. DeSanctis and B. Gallupe, A Foundation for the Study of Group Decision Support Systems, Management Science, Vol. 33, No. 5, May 1987, pp. 589–609.

[9] J. George, J. Nunamaker and J. Valacich, Electronic Meeting Systems as Innovation: A Study of the Innovation Process, Information and Management, Vol. 22, No. 3, March 1992, pp. 187–195.

[10] P. Gray, Group Decision Support Systems, Decision Support Systems, Vol. 3, 1987.

[11] J. Holt, Cases and Applications in Lotus 1-2-3 with HAL, 2nd ed., Irwin, 1988.

[12] G. Huber, Issues in the Design of Group Decision Support Systems, MIS Quarterly, Vol. 8, No. 3, September 1984, pp. 195–204.

[13] R. Johansen, Groupware: Computer Support for Business Teams, Free Press, New York, 1988.

[14] O. Liu Sheng, C. Amaravadi, M. Aiken and J. Nunamaker, IOIS: A Knowledge-Based Architecture for an Integrated Office Information System, Decision Support Systems, Vol. 8, No. 3, June 1992, pp. 269–286.

[15] T. Malone, K. Grant, F. Turbak, S. Brobst, M. Cohen, Intelligent Information Sharing Systems, Communications of the ACM, Vol. 30, No. 5, May 1987, pp. 390–402.

[16] K. McKeown, Generating Goal-Oriented Explanations, International Journal of Expert Systems, Vol. 1, No.4, 1988. pp. 377–395.

[17] K. McKeown, Natural Language for Expert Systems: Comparisons with Database Systems, Proceedings of the International Conference on Computational Linguistics, 1984, pp. 190–193.

[18] J. Nunamaker, A. Dennis, J. Valacich, D. Vogel and J. George, Electronic Meeting Systems to Support Group Work, Communications of the ACM, Vol. 34, No. 7, July 1991, pp. 40–61.

[19] R. Perraut and B. Grosz, Natural Language Interface, Annual Review of Computer Science, 1986, pp. 47–82.
