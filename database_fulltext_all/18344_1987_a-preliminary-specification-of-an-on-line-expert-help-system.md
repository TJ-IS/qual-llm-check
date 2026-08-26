---
otero_id: 18344
otero_key: "EHB7ZZ6P"
title: "A preliminary specification of an on-line expert help system"
authors: "Jaya P. Moily; Thomas J. Murray; Ritu Agarwal"
year: "1987"
journal: "Information & Management"
doi: "10.1016/0378-7206(87)90056-5"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Preliminary Specification of an On-Line Expert Help System \*

Jaya P. Moily, Thomas J. Murray,

and Ritu Agarwal

School of Management, Syracuse University, Syracuse, NY 13244, USA

Although research has suggested a number of desirable characteristics for on-line help systems, traditional design approaches have resulted in software containing many inadequacies and limitations. Here the deficiencies of current help systems are discussed and an expert system design approach to on-line help is outlined. The main components of such an expert help system are introduced.

Keywords: Help system, Expert system, On-line help.

![](/api/attachments/EHB7ZZ6P/fulltext/images/6e2d21e5b57e076f39ecda983137a392fbf13aa910cd2815ae7df5139f21f6f9.jpg)

Jaya P. Moily is an Associate Professor of Operations Management at Syracuse University. A former Efficiency Engineer with Indian Oil Corporation (India), Dr. Moily holds Ph.D. and M.B.A. degrees from the University of Wisconsin at Madison, a graduate diploma in Industrial Management from the Indian Institute of Science (India) and a Bachelor's degree in engineering from Mysore University (India). His current research interests are in the areas of manufac expert support systems.

turing management and expert support systems.  
![](/api/attachments/EHB7ZZ6P/fulltext/images/19c43da0efef867a3b05d38f90847f8a15cf8c948429d4479809c7660fed48ce.jpg)

Thomas J. Murray is an Associate Professor of MIS at Syracuse University. He holds BEE, MBA, and MSEE degrees. His Ph.D. is from the University of Massachusetts at Amherst. He held several technical and managerial positions in industry before beginning an academic career. His current research is in the area of knowledge based systems and their applications. He is the author of a textbook and has published in a number of scholarly journals. He is a member of AAAI,

ACM, IEEE Computer Society, and DSI.

## 1. Introduction

Originally intended to provide only basic and rudimentary assistance, on-line help systems have recently evolved into more complex facilities. The increasing importance accorded these systems, both by researchers and users alike, is generally attributed to the expectations of a wider range of users – a typical user is no longer assumed to be highly computer literate. This has been especially true in the case of microcomputers; accordingly, software packages developed for them tend to have better on-line help systems than those developed for mainframes.

In general, an on-line help system is any means provided by the computer to aid in productive use of the software it supports. Thus, the help system consists of supplemental software that may or may not be designed as an integral part of the main software. In this paper, the main software will be referred to as the computer system and the supplemental software as the help system. While there is no universally accepted categorization of available help systems, they can be viewed as variations or combinations of: (1) tutorial systems, which provide help in learning to use the com-

![](/api/attachments/EHB7ZZ6P/fulltext/images/91b2d0376dc3051f58fdfaa733aeded9633427001a64d945abc9edd8daff1902.jpg)

Ritu Agarwal is a Doctoral Candidate in MIS at Syracuse University. She holds a Bachelor's degree in Mathematics from Delhi University, an MBA from the Indian Institute of Management, Calcutta and is pursuing an M.S. in Computer Science along with the doctorate. Her research interests include expert systems, knowledge acquisition and logic programming. She has been a research assistant for the New York State Center for Computer Applications and Software

Engineering at Syracuse University and is a member of AAAI, ACM, and DSI.

puter system, (2) keyword-based systems, which help retrieve on-line documentation on specific features/commands of the computer system, and (3) error assistance systems, which help identify errors when an action by the user is illegal or unintelligible to the computer system.

Tutorial systems guide the user through material that helps build knowledge of the computer system. The text editor on DEC's VAX/UNIX VI and the San Marco Explorer offer such assistance. An obvious advantage of an on-line tutor is that competence can be gained at the user's own pace. Furthermore, it can incorporate the experience of previous users, so that newcomers may learn from past mistakes [4]. However, tutorial systems fail to recognize that a user's short term memory is limited and that assistance is typically required during a task. Accordingly, they need to be augmented by providing assistance that can be accessed during interaction with the computer system so that the user may function productively.

Most key-word based help systems offer some kind of help menu that defines the features/commands of the computer system. The help system on IBM's VM/SP CMS employs such an approach. These types of systems are the easiest to implement and maintain; they function fairly well in environments where users are reasonably familiar with the system. For users unfamiliar with the system and its terminology, such systems are of little use. Furthermore, it has been shown by Landauer et al. [9] that it is not possible to identify a set of commands that means the same to all people. An erroneous command may be selected and recovered through trial and error with a concomitant waste of productive time and effort.

Error assistance systems generally display an error code(s) and/or an error message(s) when an action by the user is illegal. However, these codes/messages are frequently ambiguous, even for an experienced user, and much too cryptic for the novice. Schneiderman [20] has argued that indecipherable error messages erode the confidence of the user by contributing to the belief that the error made was more serious than it actually was. In addition, error messages seldom suggest possible ways to rectify the error; however, some software packages (notably Ashton-Tate's DBASE III) explicitly ask the user if assistance is needed after an error is detected.

In this paper, it is argued that serious deficiencies exist in current help system approaches and a design framework for the development of better help systems based on expert system technology is provided. In the next section, desirable characteristics of help systems as identified in the literature are discussed. In Section 3, a discussion on the deficiencies of current help system approaches is provided. The suitability of the expert system approach to providing user assistance is discussed in Section 4. Section 5 describes a framework for an expert help system. The last section provides a summary of the paper's main thesis and conclusions.

## 2. Desirable Characteristics of On-Line Help Systems

Past research efforts, most notably by Relles et al. [16,17], have identified certain characteristics and guidelines that must be considered while designing on-line help systems. These characteristics are: flexibility, unobtrusiveness, context sensitivity, consistency, robustness, and simplicity in reading level.

Flexibility is the ability of the system to provide help information to individual users according to their level of expertise and need. For example, while a novice may require a detailed explanation about a particular command and its use, an expert probably needs only the bare syntax as a memory jog.

Unobtrusiveness implies that the user should not be required to suspend or abort the task at hand in order to access the help system. As observed by Clark [2], anxiety is caused by a requirement that users explicitly save the task status before requesting help and then return to the task environment. Such an approach is particularly discomforting to users who may doubt their ability to return to the task environment and may cause them to forget why help was originally requested. Accordingly, some systems provide a windowing facility that allows help information to be displayed on the same screen as the user's task in order to allow direct correlation between the two.

Context sensitivity is the capability of the system to provide assistance relevant to the user's context. For example, an error should prompt the system to explain exactly what mistake caused the error if several different mistakes can cause the same error condition. Utilizing contextual information reduces the explicit requests the user has to make. It also serves to imbue the help system with a kind of rudimentary intelligence from the users' perspective and increases their confidence in the system. An attempt at providing such assistance has been reported in the development of the UNIX Expert [19].

Consistency requires the mechanisms for obtaining help to be the same across the entire spectrum of user available software. Otherwise, the user will be required to become familiar with many different help approaches which may lead to confusion and unnecessary errors. This suggests that of the software they support, and that the individual responsible for help systems constantly monitors and updates this integration as new software is installed.

Robustness is the ability of the system to answer questions that are indirectly related to the current task. For example, while in edit mode, the user should be able to ask questions about the language being edited, how programs are compiled and run in that language, etc. The ability to anticipate and make provisions for the entire range of user questions is a difficult but important objective of successful help system design.

Simplicity in reading level implies that help scripts be couched in words easily understood and assimilated by the user [18]. This is particularly true in the case of on-line tutorials, where appropriate language can contribute towards developing positive user attitudes. Houghton [7] recommends that anthropomorphization, i.e. ascribing human qualities to the computer (for example, use of pronouns such as 'I'), should be avoided as it distorts the user's perception of the computer and makes it seem more than a tool to assist the user.

Failure to incorporate these characteristics in help systems can result in user anxiety and loss of confidence in the system [15]. As faith in the system is eroded, the user will be forced to rely on traditional time-consuming forms of assistance, thereby defeating the purpose of on-line help.

## 3. Deficiencies in Current Approaches

Fischer et al. [5] have demonstrated that more than half the operational computer systems are not utilized to their full potential and that, in over 90% of human-computer interactions, the vast majority of the user population is dissatisfied with its help facilities. Due to these serious flaws, users frequently resort to trial and error using long and tedious paths though shorter and more efficient paths are available.

Existing help system approaches are incapable of recognizing varying characteristics and expectations among real-world users; the help facilities tend to be designed for a user population considered largely homogeneous. Experience has shown that the assumption of homogeneity of users is false under almost all circumstances $[1]$ . Moran $[13]$ has shown that user behavior varies with level of expertise. Further, existing help systems do not react with the humanness of the user, i.e. do not deal with the fact that a human user may make simple clerical errors. Ledgard et al. $[10]$ report that users who are not adept at typing spend more time to accomplish their tasks than their lack of experience would warrant. Rigid syntax restrictions do little to increase a user's confidence when serious error messages are displayed at the slip of a key-stroke. Essentially, although many systems have been designed to be user-friendly, they are not user-understanding.

The help expectations of the user vary as the complexity of the task varies. Moran [13] has observed that a user performing a highly structured task requires relatively less detail than one performing an unstructured task. Current help systems are not designed to be task-understanding and, as a result, their responses are identical in detail and format irrespective of the nature of the task being performed.

All existing help systems provide the same response, regardless of the context in which it is requested. For example, they provide identical information about a command whether help is requested within a programming or nonprogramming context. One should expect considerably more information in the former context than in the latter, i.e. existing help systems are not context-understanding in their responses.

Current help systems provide little assistance in resolving ambiguities or evaluating alternatives. If a user has only a fuzzy idea of what needs to be accomplished, and an even less precise idea of how to accomplish it [21], these systems cannot help define the task more precisely. Nor can they assist in resolving ambiguities in system responses, such as those that occur in interpreting error codes and messages. They do not possess the reasoning powers of human consultants, primarily because they do not adopt the problem-solving approach (i.e. generation and evaluation of alternatives) employed by most human consultants [19].

Existing help systems tend to provide few facilities to aid the user in the transition from being a novice to an experienced user. Furthermore, they rarely recognize that the user may be experienced in accomplishing certain tasks but inexperienced in others. Current help systems do not gather, update, and use information about individual users. Accordingly, they are static in response and are not designed to be dynamic or adaptive.

Finally, by providing a clear and logical explanation that facilitates user-learning, the user may avoid errors in the future; however, this is simply beyond the scope of existing help systems. The long term effectiveness of a help system should be measured by the rate at which the user becomes less dependent on it without becoming dependent on other sources of assistance.

## 4. An Expert System Approach

From a user's perspective, three kinds of help are generally needed. First, the system should be able to provide assistance in formulating the command(s) or action(s) necessary for accomplishing the task. Second, it should be able to assist in correcting any command that has been unsuccessfully used. And third, the system should be able to help the user learn from errors and inefficiencies by providing suitable explanations. Accordingly, any help system should be able to answer three basic questions: (1) How do I do it? (2) What did I do wrong? and (3) What is the correct way to do it? Although not provided in existing help systems, a problem-solving approach can be most effective in accomplishing these three levels of assistance.

Such an approach will involve three steps: (1) understanding the user's problem, (2) generating alternative solutions to the problem, and (3) evaluating alternatives to recommend the best solution. Accordingly, the embedding of some reasoning capability is fundamental to develop this type of help system.

Existing help systems generally use traditional algorithmic approaches and their designers have not been able to incorporate reasoning power. However, research in Artificial Intelligence has shown that knowledge-based approaches can be used to develop systems that exhibit problem-solving skills. These are more generally known as Expert Systems (ES). Kulikowski and Weiss [8] highlight the fact that such systems can serve in intelligent problem-solving. They have been successfully developed for diverse areas such as medicine [22], chemical analysis [11], configuration of computer system hardware [12], etc. (For a more complete discussion of application areas, see [3], [6] and [14]). ES technology is particularly suited for application in areas where the supply of human experts falls short of the demand and where the available knowledge is scattered among many sources, as in the case of providing user assistance. Accordingly, we suggest an ES approach for developing better help systems. Such a help system will be termed an Expert Help System (EHS).

It has been pointed out in the previous section that a good help system should be user-understanding, task-understanding, and context-understanding. Accordingly, the EHS must contain three knowledge bases.

The user-knowledge base should include information about individual users such as: degree of familiarity, level of expertise, the types of errors committed and their frequency, synonyms used, etc. Since these characteristics may vary from task to task, they need to be specified for each. The degree of familiarity can be measured by counting the number of times each task has been attempted; the level of expertise may be measured in terms of an aggregate success to failure ratio. The types of errors committed may be categorized into clerical (typographical and spelling), use of extraneous terms, etc. The task-knowledge base should include information about individual tasks/commands, such as: the functionality of the command, its format in varying detail, examples, common mistakes users make in their order of frequency, and so on. A log of user activities during each session can be used to provide the contextual-information base.

An EHS can be made dynamic in its response to the user by constantly updating its knowledge bases. The log of user activities, maintained for the purpose of providing contextual information, can also be used for the purpose of updating the user- and task-knowledge bases at the end of each session.

An EHS is capable of facilitating user-learning as the ES is better at providing explanations of its responses than the traditional approach. For example, the EHS can be designed to aid the user in understanding why a particular error occurred and to provide or guide the user towards the rectified command. This would help the user to profit from mistakes and to become more proficient and productive.

Additional information may be needed in the EHS knowledge bases for evaluating some alternatives. This can be obtained by querying the user. However, requesting additional information from the user has certain disadvantages: (1) the user may perceive the help system to be of poor quality, especially if such information could have been obtained by the system from other sources, and (2) it may distract the user from the task if too many questions are asked. Accordingly, an EHS should be designed to interact with the computer system to obtain its error codes and messages, etc. before seeking additional information from the user.

## 5. A Framework for an Expert Help System

The EHS can be expected to consist of, at least, four major subsystems: (1) Command Assistance, (2) Error Detection and Correction, (3) Information Management, and (4) the Interface.

The Command Assistance Subsystem is expected to help the user identify the command necessary to achieve the particular task, thus providing the first level of assistance. The user should be able to input the details of the task in English. The subsystem will identify the keywords in the user statement to determine which particular one of the available commands is appropriate. If sufficient details are available in the user statement, a properly formulated command can be provided; otherwise, the subsystem may prompt the user for additional information. This subsystem is expected to use task-knowledge of the various commands and their formats, user-knowledge about the use of synonyms, and contextual-knowledge as needed.

The Error Detection and Correction Subsystem would identify the exact error(s) in an unsuccessful user command and provide the corrected command with suitable explanations, thus delivering second and third level assistance. Welty [23] has identified some common user errors. These errors can be classified into (1) extraneous terms used in a command that are not necessary, (2) simple spelling errors in a command that is otherwise correct, (3) use of a synonym, which is not recognized by the system, instead of a keyword, and (4) illegal use of a word recognized by the system. This subsystem is expected to pinpoint the particular error that has occurred, using contextual information generated by the system, and user-and task-knowledge bases.

The Information Management Subsystem is responsible for collecting, maintaining, and updating the user- and task-knowledge bases. Specifically, it maintains a log of user activity and computer system response during the session and then updates the knowledge bases at the end of the session. It also acts as a storehouse of contextual information during the session.

The Interface Subsystem maintains the overall control of the individual subsystems of the EHS and acts as a conduit between the user, the subsystems, and the computer system.

The EHS operates as an active on-line computer consultant, unlike existing help systems which generally act as passive reference sources. Accordingly, even when no help is being requested, the Interface Subsystem is expected to monitor the session to collect a log of user activities for subsequent use. This log allows the EHS to provide assistance that is context-sensitive. The user- and task-knowledge bases enable it to provide assistance at an appropriate level of detail and complexity. Since synonyms are maintained in the user-knowledge base, the user can communicate with the computer system using a larger language subset.

The EHS can be designed to be primarily user-driven when obtaining assistance. This is expected to have a favorable effect on the confidence levels of novice users. The user will have the option of activating assistance from the system either in error or query mode. When the user has only a vague idea of what needs to be done, assistance may be obtained in query mode. When the computer system output results in error messages, the user may activate assistance in error mode. This flexibility will enhance the functionality of the system from the user's perspective. The most significant feature of the EHS is its ability to learn from its experience. This is automatically accomplished by the system through constant update of the user- and task-knowledge bases.

Additional efforts are underway to design such an EHS for the ISQL facility of the SQL/DS relational DBMS on an IBM 3090 operating in the VM/CMS time-sharing environment. ISQL allows the user to leave its environment and enter a CMS subset mode and return to the original ISQL environment. The language chosen to implement the EHS is VMPROLOG. The choice of a logic based language is reasonable in this context, especially because of the facilities provided in VMPROLOG to communicate with SQL/DS; further, structure of the language provides for relatively easy programming of rules and maintenance of knowledge bases.

## 6. Conclusion

Although on-line help systems have become a common component of software, the underlying design philosophies of these systems have been limited. Assistance information provided by these systems is not user, task, and context specific. Nor are these systems designed to be dynamic and adaptive in their responses to individual user needs. It is argued that a problem-solving approach using ES technology can provide a broader design philosophy for developing more effective on-line help systems that will facilitate user-learning. A conceptual framework for developing such Expert Help Systems has been briefly discussed.

## References

[1] J. M. Carroll and J. McKendree, "Interface Issues for Advice Giving Expert System", Communications of the ACM, 30, 1 (January 1987), 14-31.

[2] I.A. Clark, "Software Simulation as a Tool for Usable Product Design", IBM Systems Journal, 20, 3 (1981) 272-293.

[3] E.A. Feigenbaum and P. McCorduck, Artificial Intelligence and Japan's Challenge to the World, Reading, MA: Addison-Wesley, 1983.

[4] R.S. Fenchel, "An Integral Approach to User Assistance", Sigsoc Bulletin (ACM), 13, 2-3, 1981, 98-104.

[5] G. Fischer, A. Lemke and T. Schwab, "Active Help Systems", Readings on Cognitive Ergonomics - Mind and Computers, Proceedings of the 2nd European Conference,

Gmunden, Austria, September 1984, published in Lecture Notes in Computer Science, G. Goos and J. Hartmanis (eds.), New York: Springer-Verlag, 1984.

[6] F. Hayes-Roth, D.A. Waterman and D.B. Lenat (eds.), Building Expert Systems, Reading, MA: Addison-Wesley, 1982.

[7] R.C. Houghton, "On-Line Help Systems – A Conspectus", Communications of the ACM, 27, 2 (February 1984), 126–133.

[8] C. Kulikowski and S.M. Weiss, A Practical Guide to Designing Expert Systems, New York: Rowman and Allanheld, 1984.

[9] T.K. Landauer, K.M. Galotti and S. Hartwell, “Natural Command Names and Initial Learning – A Study of Text Editing Terms”, Communications of the ACM, 26, 7 (July 1983), 495–503.

[10] H. Ledgard, A. Singer and J. Whiteside, Directions in Human Factors for Computer Systems, in Lecture Notes in Computer Science, G. Goos and J. Hartmanis (eds.), New York: Springer-Verlag, 1981.

[11] R.K. Lindsay et al., Applications of Artificial Intelligence for Organic Chemistry: The Dendral Project, New York: McGraw-Hill, 1980.

[12] J. McDermott, "R1: An Expert in the Computer Systems Domain", Proceedings of the First Annual National Conference on Artificial Intelligence, 1980, 269–271.

[13] T.P. Moran, "An Applied Psychology of the User", Computing Surveys, 13, 1 (March 1981), 1–11.

[14] W.B. Rauch-Hindin, Artificial Intelligence in Business, Science and Industry, Vol I and II, Englewood Cliffs, N.J.: Prentice-Hall, 1986.

[15] N. Relles, The Design and Implementation of User Oriented Systems, Computer Science Technical Report, University of Wisconsin-Madison, July 1979.

[16] N. Relles, N.K. Sondheimer and G. Ingargiola, “Recent Advances in User Assistance”, Sigsoc Bulletin, 13, 2–3 (1981), 1–5.

[17] N. Relles, N.K. Sondheimer and G. Ingargiola, "A Unified Approach to On-Line Assistance", Proceedings of AFIPS National Computer Conference, AFIPS Press, 1981, 383–388.

[18] J.M. Roemer and A. Chapanis, “Learning, Performance and Attitudes as a Function of the Reading Grade Level of a Computer Based Tutorial”, Proceedings of the Conference on Human Factors in Computer Systems, ACM Washington DC Chapter, 1982, 239–244.

[19] S.B. Salazar, “UNIX Expert: A Prototype Knowledge-Based Software Development Workstation”, Proceedings of 24th Annual Technical Symposium, ACM Washington DC Chapter, Gaithersburg, M.D., June 1985, 103–108.

[20] B. Schneiderman, “The Future of Interactive Systems and the Emergence of Direct Manipulation”, in Human Factors and Interactive Computer Systems, Proceedings of the NYU Symposium on User Interfaces, New York, May 26–28, 1982, Ablex Publishing Corporation.

[21] S.C. Shapiro and S.C. Kwasny, “Interactive Consulting via Natural Language”, Communications of the ACM, 18, 8 (August 1975), 459–462.

[22] E.H. Shortliffe, Computer Based Medical Consultation: MYCIN, New York: American Elsevier, 1976.

[23] C. Welty, "Correcting User Errors in SQL", International Journal of Man Machine Studies, 22 (1985), 463–477.
