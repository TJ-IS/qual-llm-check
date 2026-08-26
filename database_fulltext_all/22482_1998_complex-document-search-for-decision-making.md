---
otero_id: 22482
otero_key: "R4HNJ5M7"
title: "Complex document search for decision making"
authors: "J.Howard Baker; Sumit Sircar; Lawrence L Schkade"
year: "1998"
journal: "Information & Management"
doi: "10.1016/s0378-7206(98)00061-5"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Complex document search for decision making

J. Howard Baker $^{a,*}$ , Sumit Sircar $^{1,b}$ , Lawrence L. Schkade $^{2,c}$

$^{a}$ Department of Computer Information Systems, Northeast Louisiana University, Monroe 71209, USA

$^{b}$ Center for IT Management, The University of Texas at Arlington, Box 19437, Arlington 76019-0437, USA

$^{c}$ Department of Information Systems and Management Science, The University of Texas at Arlington, Box 19437, Arlington 76019-0437, USA

Accepted 30 June 1998

## Abstract

Professionals are often faced with ill-structured and complex decision situations, and they must make choices on the basis of limited information and problem clarity. These decisions are especially difficult when extensive document search is required. Thus, decision makers often satisfy rather than select an optimal alternative. The research reported here applies a cascading index, logical views, hypertext, notation capability, and case-based reasoning to a conceptual design and the prototyping of an electronic retrieval document system (ERDS) that may serve as a valuable tool for decision makers faced with an ill-structured problem and the task of extensive searching.

The ERDS prototype was applied to the problem domain of public accounting professional conduct. It was developed using a portion of the AICPA Professional Standards, which served as the electronic document text. The text was linked by hypertext to real and prototypical cases. A panel of industry experts validated the prototype. The results of analysis and evaluation produced ideas for the extension and wider application of the system. © 1998 Elsevier Science B.V. All rights reserved

Keywords: Ethics; Professional conduct; Decision support; Problem solving; Information search; Information retrieval; Electronic text retrieval; Case-based reasoning; Hypertext; Electronic document

## 1. Introduction

The business environment today is turbulent and complex. Organizations that can rapidly and correctly adapt to the environment have a greater chance of survival and prospering. Organizations adapt and learn by virtue of their responses to events of significance in the environment [8, 22]. The outcomes of these responses need to be codified into organizational memory in order to learn from prior experiences and utilize them in an appropriate manner in the future.

Organizational memory must go beyond rules and procedures and encompass less structured forms of knowledge representation. Rules can provide procedural knowledge to guide the decision maker. However, improvement of rule-based systems may be insufficient to address most real-world ill-structured social-problem domains. Rule-based systems are seldom robust in terms of the depth and breadth of the knowledge structures. This is a significant issue in complex problem domains.

We argue that the case, rather than the rule, is the most fundamental knowledge representation scheme for supporting adaptation strategies. Cases provide contextually rich knowledge through description of prior experience. Decision makers may derive problem solutions from either locating and adopting the solution of a previous case, or by adapting the solutions from previous cases $[25, 28]$ . Therefore, cases are an important form of organizational memory and case-based information systems are an important means of providing storage and retrieval of cases.

Often, decision makers face problems for which useful documentation may be available. However, the reference document may be large, complex, and/or ambiguous, as in the medical or legal profession $[4]$ . Prior experience, in the form of cases, may also be available to help clarify a reference document and offer problem-solving information. We have developed a conceptual design of an information system intended to simplify and structure search when using complex documentation and related cases. To validate this, a demonstration prototype was created. The problem domain chosen for the prototype was in the area of public accounting professional conduct. The prototype uses the portion of the AICPA Professional Standards that address professional conduct. CPAs consider this their primary source of information on professional conduct. A panel of experts evaluated the prototype.

This research introduces a theoretical basis for combining the technologies of a conceptual index (using a cascading menu), logical views of text, hypertext, notation capability, and a case database. It should be noted that this study was exploratory in nature. The prototype system was used by real decision makers with ‘real world’ problems. We did not assess the ‘goodness’ of the approach by comparing it against an alternative system. The only alternative system was the status quo with no computer help.

## 2. Ill-structured problems

Decision theorists often characterize problems by their structure, following the programmed/nonprogrammed problem dichotomy proposed by Simon [29]. There appears to be two defining characteristics of problem structure [32]. First, structure ‘is a continuous rather than a dichotomous attribute of problems’. Thus, problems lie upon a well-structured to ill-structured continuum. The second characteristic is the degree to which the problem’s structure is person-dependent, varying from one solver to the next [31]. “The characterization of a problem as structured or unstructured is representative of the state of our understanding of the problem, rather than any intrinsic property of the problem itself” [4].

Many important ‘real-world’ problems are ill-structured [1, 9, 24]. Ill-structured problems may be described as follows:

\- Essential variables may be symbolic or verbal rather than numeric, and the objective function may be non-quantitative [11].

\- Non-routine and unprogrammable, with delayed feedback and incomplete information.

\- Task objectives (problem solutions) and outcomes may be ambiguous and/or conflicting [5, 6].

\- Difficult to understand the effect of changes on decision outcomes and to predict (in advance) the effect of the actions.

\- Uncertainty exists concerning which actions affect the outcomes.

\- Human decision makers often use imperfect, subjective, and informal methods to process incomplete and imprecise knowledge.

A small subset of such ill-structured problems is characterized by the availability of textual reference documentation that is designed to help in solving them. The legal, medical, and public accounting domains are good examples. In the business world, companies may have code of conduct guidelines (e.g. IBM). Human resource departments must comply with equal opportunity laws and regulations in terms of selection, promotion, compensation, and termination decisions.

## 3. Conceptual design

A comprehensive review of the literature was undertaken [2], focusing on how to structure and simplify ill-structured problems. The following steps

were discovered:

\- Filter out information that is irrelevant to the problem at hand [3, 30].

\- Provide a means of rapidly locating relevant information [33].

\- Clarify the problem by presenting issues for the decision maker to consider at progressively greater levels of detail [7, 12, 23].

\- Provide the user with help to clarify ambiguous statements [35].

\- Enhance the recall of knowledge stored in the subconscious mind of the decision-maker [34, 28].

\- Increase the probability of reasoning from cases that are similar to the current problem [10, 26].

\- Document the decision process to promote self-reflexive thought [14, 15, 21].

An electronic retrieval document system (ERDS) can support these desirable steps. Such a system was prototyped with the following basic components:

\- A graphical user interface.

\- An electronic reference document (text) with embedded hypertext.

\- A case database accessible from the reference document by hypertext links.

\- A notational facility.

As shown in Fig. 1, all the system components exist to augment and support the mental processes of the decision maker. A user interface incorporating a cascading menu (like that adopted by Microsoft for the Windows 95 Start button, located on the Task Bar) was selected for the prototype. In addition, four important theoretical concepts were incorporated in the prototype ERDS design: priming, logical views, hierarchy, and lists.

![](/api/attachments/R4HNJ5M7/fulltext/images/0455efe0db6b94d3122c6ee5d3e2393e2b4b7042c68186c742101a75569f600e.jpg)  
Fig. 1. Conceptual diagram of the ERDS components and interactions.

Priming can help individuals recognize and recall information that may be relevant: some types of stimulus material can influence an individual's decision making performance. A computer-based system may allow problem solvers to be ‘primed’ for problem solving.

A logical view limits the presentation of text from the electronic document to that which is relevant to the problem at hand, and may also present the relevant text fragments in any order. Thus, logical views hide text deemed by domain experts to be irrelevant at the moment. Domain knowledge is knowledge of the expert's domain, such as profession conduct in public accounting. Domain experts are persons who provide domain knowledge. In the current prototype ERDS, domain knowledge from the AICPA Professional Standards is provided by the selection of relevant text fragments that make up a logical view, the ordering of the fragments to be presented, and the hypertext links established from the logical view to relevant cases in professional accounting.

Critical to the success of the ERDS is the knowledge engineering of text fragments into logical views, and the creation of hypertext links from the text to appropriate cases. Logical views, created by domain experts through the process of knowledge engineering for human understanding, provide the decision maker with access only to the text which the experts believe should be examined in a particular decision situation. Irrelevant information is hidden from view. Thus, the electronic document system (EDS) component of the electronic retrieval document system (ERDS) presents predetermined logical views of text tailored to the decision maker's current information needs.

The creation of hierarchies allows multiple levels of abstraction. Hierarchy helps us organize, understand, communicate, and learn about complexity. With too many details, textual information becomes long and cumbersome; when generalized too much, text becomes vague and useless $[17]$ . Hierarchy helps by presenting information at progressively greater levels of detail. Thus, the list of new viewing choices is limited at any level to that which is still pertinent. This, in turn, reduces distraction and simplifies the searching process. Thus, the use of hierarchy provides increased cognitive compatibility.

A list is probably the simplest graphical or visual form of presentation. By its very nature a list is a graphical presentation. We are probably most familiar with the computer presentation of a list in the graphical user interface (GUI) pull-down menu. Herbert Simon suggests a hypothesis that visual memory might be organized as list structures. He says that memory appears to have the right properties to explain the storage of both, visual and symbolic stimuli $[29]$ . This could explain why lists provide an effective way to enhance recall. Regardless of how human memory actually works, it is clear that graphical representations are regularly used to jog our memories, increase recall, and help us comprehend complex subjects.

The prototype developed employs both, a concept hierarchy and a conceptual search facility. The concept hierarchy is implemented through a multilevel cascading menu. The cascading menu is used as a rapid means of accessing the appropriate logical view of text. If the user needs help in equating a familiar word or phrase with an entry in the cascading menu, the user can input the word into the concept search facility. This facility searches an internal synonym table to find an alternative word or phrase that does appear in the cascading menu. Together, these search facilities guide the user's search for the relevant logical view of text within the electronic document. Once the appropriate logical view is obtained, appropriate cases can be obtained by way of the embedded hypertext links. Only cases appropriate to understand the text presented in the current logical view are available through these links.

The electronic document system rapidly provides the user with relevant textual information. The EDS, in turn, supports hypertext links to relevant associated cases in one or more case databases. The case database(s) may be stored on a CD-ROM, a local area network, and/or on the Internet.

## 3.1. Case-based reasoning

One of the most important cognitive issues influencing our design is ‘the phenomenon of reminding’. When we encounter new situations and experiences, they often remind us of previous cases that are stored in our memory [27]. Reasoning by reminding, i.e. reasoning from previous cases, ‘can be a very valuable tool in everyday life’. One of the best tools for learning how to reason through problems is to learn how previous cases were solved [28].

Cases form an important part of organizational memory, and capturing cases for future ‘reasoning’ is part of organizational learning. If the current prototype were implemented as an operational system, the ‘organization’ associated with the ‘learning’ would probably be the AICPA and all its members. It should be noted that organizational learning is applicable for large, virtual organizations as well as traditional organizations.

Through case-based reasoning, the decision maker examines the text of ‘previous solutions’ and other related information stored in the form of ‘cases’ in the case database called a case base. A case base is a special form of a decision-support database. In our research, such cases already existed in various formats and publications. The AICPA and state accountancy boards regularly publish recent professional conduct cases. In creating the prototype, we simply brought a select number of these cases together into a prototypical case database for our research.

To effectively and efficiently expand domain knowledge in a specific, narrowly defined problem area, the decision maker can draw from the database of relevant cases. These cases may contain information or strategies that the decision maker has not yet considered. Through this process, the ERDS assists the decision maker in broadening limited perceptions of the problem. This, in turn, might assist the decision maker to avoid reaching a poor solution.

A key factor in the ultimate success of the case-based reasoning approach is a large corpus of easily accessible knowledge. As with other types of intelligent systems, the strength is in the knowledge base. However, unlike rule-based expert systems (where inferencing takes place using an inference engine), the case-based system depends on the decision maker performing the inferencing in the human mind. Such inferencing uses both, the cases presented and the decision maker's own internal knowledge. Such internal knowledge may be extensive in the case of a professional such as a CPA.

By conveniently providing the decision maker with a system that links relevant text to a case base containing considerable domain-specific experiential knowledge, it is posited that the cost-benefit threshold will be modified and that a comprehensive search will be much more likely to take place. This, in turn, will move the decision maker from satisficing toward the selection of a solution closer to optimum.

## 3.2. Notational facility

Notational facility is similar to a word processor. It is available for the decision maker to articulate and structure the knowledge gained from examining the text in the logical views and cases. The decision maker may even copy and paste highlighted text directly from logical views or cases into notes. The notational facility is important because it promotes self-reflexive thinking and, thus, facilitates a decision maker's awareness of his or her own problem-solving methodology $[16, 19, 20, 13]$ . Through the writing process, a reflexive attitude is encouraged. At the completion of the session, the documentation created in the notational facility can be printed or saved to disk. The documentation created is often valuable in dealing with post-decisional dissonance.

## 4. Field test of the ERDS prototype

The focus of our field work was on obtaining independent and unbiased feedback from expert professionals both, to validate the design and to identify the features that were considered most helpful. This exploratory approach to prototype development is not unusual in what is essentially an engineering endeavor $[18]$ ; there is no alternative ‘benchmark’ other than the status quo. The ‘goodness’ of the design is judged by the reactions of the experts.

## 4.1. Panel of experts

A panel of experts was chosen to evaluate the ERDS prototype. In the evaluation process each expert independently solved a series of professional conduct problems both with, and without, the ERDS. The panel consisted of five certified public accountants (CPAs), who were active in the practice of public accounting. End-users, rather than system developers, were intentionally selected to be evaluated the ERDS. The panel members came from a variety of working backgrounds, representing small, regional and international CPA firms, and included one individual with recent ‘Big Six’ experience. The experts also came from several different geographical areas, ranging from a rural town to a large metropolitan area. This mix ensured that the group had individuals with a variety of work experiences and professional associations.

Each panel member spent approximately three hours on the evaluation effort, including time spent studying the background material mailed prior to the evaluation session. Each panel member was hired and compensated equally to act as an unbiased consultant; the compensation was based on a typical CPA hourly billing rate of a major metropolitan area in Texas. None of the panel members were given information as to the exact nature of the research or the expected results of the evaluation process. All were told that the written evaluation responses would be kept anonymous. However, each evaluation session was video-taped.

## 4.2. Evaluation procedure

The criteria for evaluation were tied directly to design characteristics incorporated in the prototype. The evaluation instrument consisted of seven evaluation criteria as specified on Table 1. The experts were asked to evaluate the degree to which the prototype system met each evaluation criterion on a 5-point Likert scale, with 1 signifying they strongly disagreed that the system met that criterion and 5 that they strongly agreed that it did. Each panel member completed the evaluation instrument in private immediately after working through all the professional conduct problems.

## 5. Results

The evaluation process was designed to determine if the panel of experts perceived that the demonstration prototype ERDS achieved each of the design objectives. The field evaluation yielded good results. All five evaluators responded with an average rating over three. The highest average evaluator response was 4.6 and the lowest - 3.4 on a scale of five. For the seven design criteria, the highest average response of the five evaluators was 4.6 and the lowest 3.2. Of the 35 responses (seven criteria times five evaluators), the average response was 4.14. Three of the seven criteria achieved an average rating of 4.6. Five of the seven criteria scored above four. Table 2 is a summary of the numeric responses made by the five evaluators. Table 3 shows the average response for each evaluation criterion in descending order (ties are equally ranked).

Table 1  
Evaluation criteria used in the evaluation instrument

<table><tr><td>Basis of criteria</td><td>Evaluation criteria</td></tr><tr><td>1. Lack of time contributes to satisficing</td><td>The ERDS provides a rapid means of locating information which is relevant to the problem at hand</td></tr><tr><td>2. Improving interpretation of professional standards leads to better professional decisions</td><td>The ERDS helps to clarify ambiguous statements encountered in the text of the AICPA Code of Professional Conduct</td></tr><tr><td>3. Professionals possess internal knowledge they are not immediately conscious of until ‘primed’</td><td>The ERDS causes the recall of knowledge stored in the subconscious which seems relevant to the problem at hand</td></tr><tr><td>4. Cases are often used by professionals to overcome the difficulty of facing complex and unfamiliar situations</td><td>The ERDS increases the probability of reasoning from previous cases which are similar to the problem at hand</td></tr><tr><td>5. Professional standards are large and complex documents containing considerable information which is irrelevant to any given problem</td><td>The ERDS filters out information which is irrelevant to the problem at hand</td></tr><tr><td>6. Hierarchy helps us organize, understand, communicate, and learn about complexity</td><td>The ERDS helps to clarify the problem at hand by presenting issues to consider at progressively greater levels of detail</td></tr><tr><td>7. Professionals have a need to articulate and document the decision process to meet post-decisional dissonance and the need to legitimate decisions.</td><td>The ERDS eases documentation of the decision process for future justification of the decision</td></tr></table>

There were no ‘strongly disagree’ responses and only three ‘disagree’ responses out of a total of thirty-five responses; two of these were on criterion #2, which addressed whether the prototype ERDS clarified ambiguities in the AICPA Code of Professional Conduct. Both evaluators who expressed disagreement also made written comments that the system did allow them to look at more relevant information. Another evaluator, who expressed agreement with criterion #2, stated that the cases helped clarify the ambiguities.

## 6. Summary and conclusions

The responses of the evaluators indicated that they perceived the system's strongest features were (1) the rapid means of locating information, (2) the increased probability of reasoning from previous cases, and (3) the facilitation of the documentation process for future justification of the decision. One evaluator verbally expressed considerable enthusiasm over the third feature. These three features map to the three major components of the ERDS: (1) the conceptual index facility, (2) the case base facility, and (3) the notational facility. No attempt was made during this study to determine whether the ERDS actually improved professional conduct decision quality.

Table 2  
Summary of the numeric responses of the five evaluators

<table><tr><td>Criterion #</td><td>Evaluator #1</td><td>Evaluator #2</td><td>Evaluator #3</td><td>Evaluator #4</td><td>Evaluator #5</td><td>Average</td></tr><tr><td>1</td><td>5</td><td>4</td><td>4</td><td>5</td><td>5</td><td>4.6</td></tr><tr><td>2</td><td>4</td><td>4</td><td>2</td><td>2</td><td>4</td><td>3.2</td></tr><tr><td>3</td><td>4</td><td>4</td><td>3</td><td>4</td><td>3</td><td>3.6</td></tr><tr><td>4</td><td>5</td><td>4</td><td>4</td><td>5</td><td>5</td><td>4.6</td></tr><tr><td>5</td><td>5</td><td>4</td><td>4</td><td>3</td><td>5</td><td>4.2</td></tr><tr><td>6</td><td>5</td><td>5</td><td>2</td><td>5</td><td>4</td><td>4.2</td></tr><tr><td>7</td><td>4</td><td>4</td><td>5</td><td>5</td><td>5</td><td>4.6</td></tr><tr><td>Total</td><td>32</td><td>29</td><td>24</td><td>29</td><td>31</td><td>29</td></tr><tr><td>Average</td><td>4.6</td><td>4.1</td><td>3.4</td><td>4.1</td><td>4.4</td><td>4.14</td></tr></table>

Table 3  
Average response for each criterion in descending order

<table><tr><td>Criterion #</td><td>Description of criteria</td><td>Rank</td><td>Average</td></tr><tr><td>1</td><td>The ERDS provides a rapid means of locating information which is relevant to the problem at hand</td><td>1</td><td>4.6</td></tr><tr><td>4</td><td>The ERDS increases the probability of reasoning from previous cases which are similar to the problem at hand</td><td>1</td><td>4.6</td></tr><tr><td>7</td><td>The ERDS facilitates documentation of the reasoning process for future justification of the decision</td><td>1</td><td>4.6</td></tr><tr><td>5</td><td>The ERDS filters out information which is irrelevant to the problem at hand</td><td>2</td><td>4.2</td></tr><tr><td>6</td><td>The ERDS helps to clarify the problem at hand by presenting information at progressively greater levels of detail</td><td>2</td><td>4.2</td></tr><tr><td>3</td><td>The ERDS causes the recall of subconscious knowledge relevant to the problem at hand</td><td>3</td><td>3.6</td></tr><tr><td>2</td><td>The ERDS helps to clarify ambiguities in the AICPA Code of Professional Conduct</td><td>4</td><td>3.2</td></tr></table>

Based on the positive results obtained from the evaluation, it seems that the software industry should progress toward a new class of software product that incorporates the features identified in the conceptual design. The use of such software could be applied to various decision-making areas such as finance, law, management, ethics, and human services, as well as public accounting.

Ultimately, case bases containing multimedia cases as well as simple text cases should appear on the Internet. We also believe that eventually a more powerful copy and paste capability will be provided in the Microsoft Windows environment. This more powerful copy-and-paste facility will permit multimedia copy and paste. Multimedia copy and paste would allow the user to copy all or a portion of a multimedia case into the notational facility and integrate it with notes and text copied from logical views.

## References

[1] John R. Anderson, in: Arthur W. Melton (Ed.), Language, Memory and Thought, Experimental Psychology Series, Lawrence Erlbaum Associates, Hillsdale, NJ, 1976.

[2] J. Baker, A. Howard, Conceptual design for simplifying and structuring electronic documents: an application in professional conduct standards, Ph.D. dissertation, The University of Texas at Arlington, 1992.

[3] Ralph Barletta, An Introduction to Case-Based Reasoning, AI Expert, August 1991.

[4] Amit Basu, Imprecise reasoning in intelligent decision support systems, Ph.D. dissertation, University of Rochester, 1986.

[5] John L. Bennett (Ed.), Building Decision Support Systems, Addison-Wesley, Reading, MA, 1983.

[6] J. Bois Samuel, The Art of Awareness: A Textbook on General Semantics, Wm. C. Brown Company Publishers, Dubuque, IA, 1978.

[7] M.J. Culnan, Environmental scanning: the effects of task complexity and source accessibility on information gathering behavior, Decision Sciences, (14) 1983.

[8] Milan J. Dluhy, K. Chen (Eds.), Interdisciplinary Planning: A Perspective for the Future, Center for Urban Policy Research, New Brunswick, NJ, 1986.

[9] Daniel Druckman, Robert A. Bjork (Eds.), In The Mind's Eye; Enhancing Human Performance, National Academy Press, Washington, D.C., 1991.

[10] Michael Gelb, Thinking for a Change, 1st edn., Harmony Books, New York, NY, 1995.

[11] S.I. Hayakawa, Language in Thought and Action, 3rd ed., Harcourt Brace Jovanovich, Inc., New York, NY, 1972.

[12] Patrick J. Hebert, Television reporting of the bereaved: a general semantics approach, Annual Meeting of the Speech Communication Association, November 18–21, San Francisco, CA, 1989.

[13] William Horton, Illustrating Computer Documentation: The Art of Presenting Information Graphically on Paper and Online, John Wiley & Sons, Inc., New York, NY, 1991.

[14] George P. Huber, Organizational learning: the contributing processes and the literatures, Organization Science (2) 1991.

[15] Kenneth G. Johnson, Self-reflexiveness in therapy and education, The Journal of Communication Inquiry (4) 1979.

[16] Zuce Kogan, Essentials in Problem Solving, 2d edn., Arco Publishing Co., Inc., New York, NY, 1956.

[17] Janet L. Kolodner, Extending problem solver capabilities through case-based inference, Proceedings of a Workshop on Case-Based Reasoning in Clearwater, Beach, Florida, May 10–13, 1988, by the Defense Advanced Research Projects Agency and the Information Science and Technology Office, Morgan Kaufmann Publishers, San Mateo, CA, 1988.

[18] David L. Lau, An investigation of the relationship between small group discussion and self-reflexive evaluation, Ph.D. dissertation, Southern Illinois University, 1983.

[19] David Frank Maas, The Images of Order, Peter Lang, New York, NY, 1988.

[20] Norman B. Macintosh, The Social Software of Accounting and Information Systems, John Wiley & Sons, New York, NY, 1985.

[21] Jack R. Meredith, Efraim Turban, Essentials of Management Science, Business Publications, Plano, Texas, 1982.

[22] C.A. O'Reilly, Variations in decision makers use of information sources: the impact of quality and accessibility of information, Academy of Management Journal (25) 1982.

[23] Alistair M. Preston, The problem in and of management information systems, Accounting, Management and Information Technologies (1) 1991.

[24] Christopher K. Riesbeck, Roger C. Schank, Inside Case-based Reasoning, Lawrence Erlbaum Associates, Hillsdale, NJ, 1989.

[25] R. Sabherwal, V. Grover, Computer support for strategic decision-making processes: review and analysis, Decision Sciences (20) 1989.

[26] R. Schank, Conceptual dependency: a theory of natural language understanding, Cognitive Psychology (3) 1982.

[27] Roger Schank, Peter Childers, The Creative Attitude: Learning to Ask and Answer the Right Questions, Macmillan Publishing Company, New York, NY, 1988.

[28] Herbert A. Simon, The Sciences of the Artificial, MIT Press, Cambridge, MA, 1969.

[29] Herbert A. Simon, The role of attention in cognition, in: Sarah L. Friedman, Kenneth A. Klivington, Rita W. Peterson (Eds.), The Brain, Cognition, and Education, Academic Press, Inc., New York, NY, 1986.

[30] Stephen Slade, Case-Based Reasoning: A Research Paradigm, AI Magazine, Springer, 1991.

[31] Gerald Frederick Smith, The effects of management science interventions on the solving of unstructured problems, Ph.D. dissertation, University of Pennsylvania, 1985.

[32] Gerald F. Smith, Towards a theory of managerial problem solving, Decision Support Systems (8) 1992.

[33] John P. Van Gigch, Applied General Systems Theory, 2nd edn., Harper and Row, New York, NY, 1978.

[34] Sue E. Weber, Benn R. Konsynki, Problem management: neglected elements in decision support systems, Journal of Management Information Systems, 4, Winter, 1987.

[35] Vladimir Zwass, Management Information Systems Wm. C. Brown Publishers, 1992.

![](/api/attachments/R4HNJ5M7/fulltext/images/664a04ec7fffab8851a69a22d3fcf93d7e090b824478313acd9e69f9b0ed87f4.jpg)

J. Howard Baker, Ph.D. is Assistant Professor of Computer Information Systems, Northeast Louisiana University. His doctoral degree was earned at The University of Texas at Arlington. Dr. Baker is a Certified Internal Auditor (CIA), Certified Fraud Examiner (CFE), and a certified facilitator for The 7 Habits of Highly Effective People leadership seminar from Franklin Covey, Inc.

His current research interests are creativity facilitation software, creativity in information systems, concept mapping, professional conduct, and learning organizations.

![](/api/attachments/R4HNJ5M7/fulltext/images/1b85520c587003863233633007db696b754477ef2bf1ad9588b9d304fb821252.jpg)

Lawrence L. Schkade, Ph.D. CCP is Jenkins Garrett Professor, Information Systems, University of Texas at Arlington. He is a Fellow, American Association for the Advancement of Science and the Decision Sciences Institute; with many listings including Who's Who in the Computing Industry and Who's Who in the World. His current research concerns communication metrics and electronic commerce. He has over 150

publications, including several books and numerous research articles in over 30 scholarly journals such as Administrative Science Quarterly, Applied Intelligence, Behavioral Science, Communications of the ACM, Decision Sciences, Information and Management, and Journal of the American Medical Association.

![](/api/attachments/R4HNJ5M7/fulltext/images/7f7b1bde6c8ea57aa3f9eb5af86fe9be3842b7604b56955f2940dc4f70c9f522.jpg)

Dr. Sumit Sircar is Director of the Center for Information Technologies Management and Professor of Information Systems and Management Sciences in the College of Business Administration at the University of Texas at Arlington. His doctoral degree was earned at the Harvard Business School and he is also a Certified Computing Professional and Disaster Recovery Planner. Dr. Sircar has published numer-

ous articles in the area of information resource management in a large number of journals, including the Communications of the ACM, Information and Management, and Journal of Database Management.
