---
otero_id: 18063
otero_key: "ZSSSSMUZ"
title: "Information independent evaluation of information systems"
authors: "Levent Orman"
year: "1983"
journal: "Information & Management"
doi: "10.1016/0378-7206(83)90039-3"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Independent Evaluation of Information Systems

Levent Orman

Cornell University, Graduate School of Business and Public Administration, Ithaca, NY 14853, USA; Tel. (607) 256-4728

Information systems are characterized and their desirable features are identified. Information independence is proposed as a major architectural characteristic underlying many desirable features. Two types of information independence are identified and an approach to quantifying the degree of independence is introduced. Information independence is suggested as a useful and quantifiable measure of the value of an information system.

Keywords Information System, System Evaluation, System Architecture, Information Independence

![](/api/attachments/ZSSSSMUZ/fulltext/images/c0c2904a5dc23918d0ac22ae036f1acf1a5e29e124d272feb37c49ca567562e6.jpg)

Levent Orman is Assistant Professor of Information Systems at Cornell University, Graduate School of Business and Public Administration. He has received M.M. and Ph.D. degrees from Northwestern University, Graduate School of Management. His professional interests include design, specification and evaluation of information system with particular emphasis on databases. His recent articles appeared in Information Systems, and Journal of Policy Analysis and Information Systems.

## 1. Evaluation of Information Systems

Information systems are human-machine systems designed to collect, store, retrieve, process and present information. These systems usually represent large, long term capital investments and their development is usually preceded by comprehensive analysis and evaluation. Unfortunately, the tools available for these purposes are primitive and sometimes misleading. The analysis phase and the problems associated with its tools have been studied extensively [6,10,13,46,47]. The emphasis in this article is on the evaluation problem with an assessment of the alternative approaches in terms of the identification and measurement of relevant variables. There are three general approaches to information system evaluation:

a. evaluation in terms of the system output;

b. evaluation in terms of the system behavior;

c. evaluation in terms of the system architecture.

Evaluation in terms of output is the most common approach. An information system outputs information; consequently, it is only natural to evaluate it in terms of the quality and the quantity of information it provides. Both the quality and the quantity of information are intuitively relevant variables to the system value, and both are of considerable theoretical interest, but of little practical value since neither can be defined or measured with acceptable precision. The quality of information is defined in terms of its contribution to the quality of the decisions it aids and it is highly influenced by the style and the behavior of the information user [15,24], and the state of the environment [12,20]. Consequently, the measurement of the value is possible only when the decision making process is well understood and programmed [42], and even then the analysis is highly complex and decision dependent [4,21,44]. The quantity of information has been studied extensively in terms of the load on communication channels [40]; but this is of little relevance when human-machine interaction is involved where information load is not quite proportional to the number of bits transmitted, but highly dependent on the organization of the information [8]. Some attempts have been made to measure information quantity in terms of its surprise content (through a Bayesian analysis) without much practical success [43]. In addition to measurement problems, use of information value to evaluate an information system can be misleading. The economic value of an information system is different from the value of its information content, just as the value of a candy machine is different from the value of the candy is dispenses. It is rather the contribution of the system to the value of information flowing through the system (i.e. the added value), and obviously this is even more difficult to measure than the value of information produced. In light of these difficulties, a practical avenue to evaluate information systems is to identify the behavioral characteristics which consistently lead to the production of higher quality and quantity information per unit investment, and use those characteristics as proxy variables.

The variables involved in evaluation through behavior are more difficult to identify since they are relevant only in terms of their effect on the value of information produced. This indirect evaluation may be desirable if the behavioral variables are easier to measure. Such an approach is common in performance evaluation of hardware components, since their behavioral characteristics (such as response time and interface requirements) are usually provided by the vendor. A similar approach is sometimes taken in evaluating the human components, especially in an uncertain environment where the information demands on the system are not predictable. A typical example of this is a high level managerial position since managerial work can be viewed as information processing. Managerial work consists of information processing and decision making [26]. We will consider managers primarily as information processors since decisions can be viewed as a special type of information (information that directly leads to action), and decision making can be viewed as a special type of information processing. Obviously, behavioral characteristics such as intelligence, initiative, congeniality and enthusiasm are sought in most managerial candidates irrespective of the type of information to be processed. The behavioral characteristics may also be used as intermediate goals to identify the desirable architectural characteristics of an information system as those that produce desirable behavior.

The architectural variables in evaluation are extremely difficult to identify, since their influence on the organization is very indirect, i.e. by causing desirable behavior which generates valuable information which in turn contributes to the quality of the organizational decision making process. The advantage of using architectural characteristics in evaluation is the ease with which they can be observed, measured, and even controlled. The thesis of this paper is that it is possible and practical to identify desirable architectural characteristics and measure them for information system evaluation. A two stage approach is taken, in the first of which behavioral characteristics are identified and used as intermediate goals. 'Flexibility' and 'performance' are identified as major desirable behavioral features leading to production of higher quality information.

In the second stage architectural characteristics producing desirable behavior are identified. Information independence is proposed as a major architectural determinant of information system value and an approach to measure it is outlined.

## 2. Behavioral Characteristics of Information Systems

The ability of an information system to handle a given piece of information flowing through the system is called its performance and it is determined by two behavioral factors:

a. efficiency with which the system handles the information;

b. usability of the information when finally presented to a user.

Efficiency is measured by the cost of handling information and usability is the system's ability to carry the information to an appropriate user, at an appropriate time, in an easily usable form by that user. Usability characterized in this fashion can be defined as the contribution of the system to the value of information.

While the analysis above applies to a given piece of information, the information system exists over a long period of time and handles a variety of information in a changing environment. Consequently, the overall value of an information system depends on its ability (in terms of efficiency and usability) to handle a variety of changing information. This ability is called the flexibility of an information system. The importance of flexibility can be appreciated easily by analyzing the problems associated with the development and maintenance of current information systems. Both the development and maintenance activities are extremely costly and time consuming with usually less than satisfactory outcomes, mainly due to lack of flexibility. The development of an inflexible system requires a complete and detailed specification of information requirements before even attempting the development. This places unreasonable demands on the designers since the information requirement of decision makers cannot be completely determined and precisely specified for the following reasons:

a. the decision making process in general is not well understood and structured [17,42]

b. decision makers have different styles and different information needs [37]

c. information needs change in time as the environment and tl. organization change [3,28].

vironment and the organization change [3,28]. The maintenance of an inflexible system is also problematic. It usually consists of a series of major redevelopment processes which results in considerably higher maintenance costs than the cost of original development [28] and/or a rapid rate of obsolescence, especially in the dynamic environment of modern organizations. The arguments in favor of inflexible systems are potential for higher efficiency in relatively static environments and lack of tools to build flexible systems, although some major attempts have been made recently to remedy the latter (see Section 5).

It is possible to identify two major types of flexibility. Generality is the variety of information a system can handle at a given time. Adaptability is the ability to handle changes in information content and structure through the lifetime of the system. Generality and adaptability combined with efficiency and usability characterize the behavior of an information system. Unfortunately, the objective measurement of these variables poses considerable difficulty since behavior is basically the interaction of the system with its environment; consequently, measurement in isolation from the environment and the users would be impractical; and measurement in the context of a specific environment would not be useful since the very essence of this article is the dynamic and unpredictable nature of the organizational environment.

## 3. Architectural Characteristics of Information Systems

The desirable behavioral characteristics identified above are sometimes used directly to evaluate some information system components (such as hardware). This is done by roughly measuring them in normally expected or extreme environments to determine average, best or worst performance. However, the major impact of identifying behavioral characteristics on information system evaluation is in their use as intermediate goals to identify easily measurable architectural characteristics. The correspondence between individual behavioral and architectural characteristics is usually straightforward. The difficulty lies in identifying architectural characteristics that produce combinations of desired behavior since an architectural characteristic producing one type of desirable behavior is usually in conflict with another characteristic producing another type of desirable behavior. It is easy to observe for example that an architecture leading to higher levels of generality or adaptability usually reduces the usability and/or efficiency [33]. In an attempt to study the production of combinations of desired behavior, Figure 1 shows a classification of behavioral characteristics along the dimensions of performance and flexibility, and a list of architectural characteristics each corresponding to a pairwise combination of behavioral characteristics.

<table><tr><td rowspan="2"></td><td colspan="2">Flexibility</td></tr><tr><td>Generality</td><td>Adaptability</td></tr><tr><td colspan="3">Performance</td></tr><tr><td>Usability</td><td>User view Isolation</td><td>Stability</td></tr><tr><td>Efficiency</td><td>Centralized Optimization</td><td>Dynamic Reorganization</td></tr></table>

Fig. 1. Architectural Characteristics Corresponding to Pairwise Combinations of Behavioral Characteristics.

The architectural characteristics user view isolation and stability measure the ability to maintain usability in a general and adapting system. User view isolation is the ability to minimize the knowledge required from a user of the needs and demands of other users sharing the same general system. Stability is the ability to maintain the user interfaces while the system is changing and hide the changes from the user unless they are directly relevant. The characteristics centralized optimization and dynamic reorganization measure the ability to maintain efficiency in a general and adapting system. Centralized optimization is the ability to combine all user requirements into a single efficient structure to avoid suboptimization and redundancy. Dynamic reorganization is the ability to maintain the overall efficiency in a dynamic environment through incremental reoptimization.

At this stage, it is possible to identify information independence as the major intrinsic architectural characteristic of an information system underlying all of the above mentioned characteristics. Information independence is defined as the degree to which an information system can handle information, independent of its type and structure, and independent of other existing information. There are two types of information independence:

3. Vertical information independence is the ability to handle a given piece of information in various levels of abstraction in different structures and roles, independent of its original type and structure.

b. Horizontal information independence is the ability to handle a piece of information independent of the existence and structure of other information in the system.

The horizontal information independence can be viewed as the characteristic underlying user view isolation and stability by separating and isolating a user's view of the system from other users' views and changes in those views. The vertical information independence can be viewed as the characteristic making centralized optimization and dynamic reorganization possible without undermining usability. This task is accomplished by introducing layers of abstraction to view a given piece of information in terms of various levels of detail and a variety of structures and roles where the lower levels are used to insure efficiency through centralized optimization and dynamic reorganization while the upper levels maintain the user interaction and usability independent of changes in lower levels.

## 4. Measurement of Information Independence

Information independence as an intrinsic architectural characteristic of an information system can be easily observed, measured and even controlled independent of the environment and users. One approach to measurement involves counting functions comprising and information system. A function is a (possibly multivalued) mapping between two sets (called input and output, source and target, domain and range, argument and value, etc., depending on the context). A function can be viewed as a unit of information since all data models and computational models of an information system can be expressed in terms of functions [2,33,41]. As a matter of fact, all processes (manual or automated) can be regarded as functions from their inputs to their outputs. Moreover, functions and similar concepts such as binary associations have already been suggested and studied as the smallest units of information in the context of database management systems [5,30,39]. Once the function concept is accepted as a viable unit of information, both the vertical and the horizontal information independence can be measured in terms of function counts.

Assertion 1: The degree of horizontal information independence can be measured by the average number of functions a user has to know to execute or modify a single function. This assertion follows from the observation that the better the isolation of a user's view from the rest of the system, the smaller the number of functions he has to know to execute or modify a single function, leading to ease of use and stability.

Assertion 2: The degree of vertical independence can be measured by the average number of functions that are triggered to execute a single function. This assertion follows from the fact that the number of functions triggered by a single function measures the level of abstraction and the conceptual distance between the user functions and the primitive functions of the system, where a primitive function is one that is directly executable without triggering any other function.

Definition 1: The functions that are triggered to execute a given function $f$ are called the descendants of $f$ and denoted by $D_f$ . Consequently, the vertical independence is equal to

$$
\frac {1}{n} \sum_ {j \in F} | D _ {j} |
$$

where n is the number of functions in the system, F is the set of all functions, and $|D_{f}|$ is the cardinality of the set $D_{f}$ .

Assertion 3: The degree of vertical independence can also be measured by the average number of functions that are affected by a modification to a single function. This assertion follows from the observation that the functions affected by a modification to a given function f are the functions that trigger and use f in their execution. Consequently, this measure is similar to the previous one in that it measures the same concept in the opposite direction.

Definition 2: The functions that are affected by modifications to a single function f are called its ascendants and denoted by $A_{f}$ . Consequently, the vertical independence is equal to

$$
\frac {1}{n} \sum_ {j \in F} | A _ {j} |
$$

where $n$ is the number of functions in the system, $F$ is the set of all functions, and $|A_{f}|$ is the cardinality of the set $A_{f}$ .

Theorem: The two measures of vertical independence given in assertions 2 and 3 are equivalent. In other words:

$$
\frac {1}{n} \sum_ {f \in F} | A _ {f} | = \frac {1}{n} \sum_ {f \in F} | D _ {f} |.
$$

Proof: See Appendix.

The intuition behind this theorem is that if a function f triggers m different functions to execute, then a modification of any of those m functions potentially affects the outcome of f. Consequently, the measurement of either variable (the number of functions triggered, or the number of functions affected by a modification) will produce the same result.

## 5. An Evaluation of Historical Trends

The historical trends in information system development techniques have been a continual increase in information independence supporting the major thesis of this article. These trends can be observed by analyzing the information system, in three generations:

## 5.1. Data Processing Systems

The first generation information systems are usually referred to as data processing systems. They are distinguished from their predecessors by separation of data and computational functions, and an appreciation of data as a resource to be acquired, maintained and even shared among the computational functions. This is clearly an improvement on horizontal independence compared to earlier development techniques where data was always specific to a single computational function and it was an integral part of it. The increased horizontal independence is due to the ability to modify the data and computational functions independently, and especially the ability to execute the same computational function with different sets of data. Other concepts such as modular programming also contributed to horizontal independence in this generation. Modular programming created collections of fairly independent computational functions, similar to the concept of data files creating collections of fairly independent data functions. In summary, this generation is characterized by emphasis on horizontal independence.

## 5.2. Management Information Systems

The second generation information systems are usually referred to as management information systems reflecting the primary emphasis on managerial support. This generation is characterized by the recognition that different levels of management need the same information in different forms. In particular, the higher levels of management need highly aggregated and processed information in contrast to lower levels where detail and accuracy provided by raw data are more important. To meet these diverse needs and still maintain consistency and efficiency, the second generation systems concentrated on vertical independence. In particular, the emphasis on data, introduction of centralized data bases with two [9], three [1] of four [11] levels of abstraction, and appreciation of data as a shared organization wide resource with a structure to meet all foreseeable and even some unforeseen information demands characterize this generation. The increase in vertical independence follows directly from the introduction of multiple levels of abstraction into data models.

## 5.3. Decision Support Systems

The third generation information systems are usually called decision support systems to reflect the change in emphasis from managerial control to supporting the decision making process. Decision making at the functional and especially at the strategic level require a great deal of processing, computation and analysis. Consequently, the emphasis of third generation systems is on the computational models as opposed to the emphasis on data in the previous generation. To meet the diverse needs of decision makers for highly processed information, third generation systems concentrated on vertical independence in computational functions by introducing layers of abstraction into application software. Top down design [13,47], very high level programming languages [14], and specification languages [31,32,36,38] are all attempts in this direction increasing vertical independence. Despite these attempts, vertical independence is still a current research area and far from a standard practice. Development of tools to build vertically independent software systems has been painfully slow despite the fact that the advantages of such systems have long been recognized especially when the interfaces between layers of abstraction is automated [28,45]. It is interesting to note that in the absence of such tools many substitutes have been suggested. One of them is heuristic development [3] and it involves simulating a vertically layered environment by initially implementing the user interaction (which is basically 'the top layer of a vertically layered system) and subjecting it to user review before the actual system development starts. The advantage of a review phase is obviously the ability to use and modify the top level of the abstraction hierarchy independent of the (non existent) lower levels.

## 6. Conclusions

Information independence is an architectural characteristic of an information system underlying many desirable behavioral characteristics and leading to the production of higher quality information. Consequently, information independence is proposed as a practical evaluation tool. Two major advantages of using information independence for evaluation are observed:

a. Information independence is easily quantifiable and measurable since it relates to the architecture of the system rather than its behavior. An architectural characteristic is easier to measure since it is an intrinsic property of the system independent of its environment and users.

b. Information systems are currently evaluated in terms of the users' perception of the value of information produced, or the value of behavioral characteristics. Unfortunately, the users' perceptions are formed over long periods of time and after the system is developed; and consequently they are of little use to the designers of the system. Information independence on the other hand, should provide clear guidelines to the designers and the users as to the value of the system and alternatives, before it is built, since it is an architectural variable independent of the users and their perceptions.

Future research is suggested in two main areas. Detailed procedures have to be developed to measure information independence of individual systems. These procedures have to be tested through empirical work and compared to more conventional evaluation techniques, such as user perceptions of the value of information or behavior. The second research area would be the identification of other architectural variables underlying some of the behavioral characteristics ignored in this article such as reliability and security. This research area would eventually lead to a complete evaluation strategy based on architectural characteristics.

## Appendix

Theorem:

$$
\frac {1}{n} \sum_ {f \in F} | A _ {f} | = \frac {1}{n} \sum_ {f \in F} | D _ {f} |.
$$

Proof: Assume the system contains no cycles, i.e. the same function cannot be both an ascendant and a descendant of another function, and observe the following identities:

$$
\begin{array}{l} \left| A _ {f} \right| = \sum_ {g \in F} a _ {g f} \text {where} a _ {g f} = \left\{ \begin{array}{l l} 1 & \text {if} g \in A _ {f} \\ 0 & \text {otherwise} \end{array} \right. \\ \left| D _ {f} \right| = \sum_ {g \in F} d _ {g f} \text {where} d _ {g f} = \left\{ \begin{array}{l l} 1 & \text {if} g \in D _ {f} \\ 0 & \text {otherwise} \end{array} \right. \end{array}
$$

$a_{gf}$ is called the ascention function since it has the value 1 whenever g is an ascendant of f. $d_{gf}$ is called the descention function for a similar reason. $a_{gf} = d_{fg}$ follows from the definition of ascendants and descendants. Using these identities:

$$
\begin{array}{r l} \sum_ {f \in F} | A _ {f} | & = \sum_ {f \in F} \sum_ {g \in F} a _ {g f} = \sum_ {f \in F} \sum_ {g \in F} d _ {f g} \\ & = \sum_ {g \in F} \sum_ {f \in F} d _ {f g} = \sum_ {g \in F} | D _ {g} | \end{array}
$$

and hence

$$
\frac {1}{n} \sum_ {f \in F} | A _ {f} | = \frac {1}{n} \sum_ {f \in F} | D _ {f} |.
$$

## References

[1] ANSI/X3/SPARC Study Group on Data Base Management Systems. DBMS Framework. D. Tsichritzis and A. Klug (eds.), AFIPS Press, Montvale, NJ, 1977.

[2] J. Backus, Can programming be liberated from the von Neumann style? A functional style and its algebra of programs. Comm. ACM 21, 8, 613-641, 1978.

[3] T.R. Berrisford and J.C. Wetherbe, Heuristic development. A redesign of systems design. MIS Quarterly 3, 1, 1979.

[4] D.F. Boyd and H.S. Krasnow, Economic evaluation of management information systems. IBM Systems Journal 2, 1, 2–23, 1963.

[5] G. Bracchi, P. Paolini and G. Pelagatti, Binary logical associations in dat·modeling, in Modeling in Data Base Management Systems, G.M. Nijssen (ed.), North Holland Publishing Company, Amsterdam, 1976.

[6] W.M. Carlson, Business Information Analysis and Integration Technique (BIAIT)-The new horizon. Data Base 10, 4, 3–9, 1979.

[7] N.L. Chervany and G.W. Dickson, Economic evaluation of management information systems: An analytical framework. Decision Sciences 1, 3, 296–308, 1970.

[8] N.L. Chervany and G.W. Dickson, An experimental evaluation of information overload in a production environment. Management Science 20, 10, 1335–1344, 1974.

[9] Codasyl Data Base Task Group. April '71 Report, ACM NY 1977.

[10] J.D. Cougar, M.A. Colter and R.W. Knapp, Advanced System Development/Feasibility Techniques. John Wiley & Sons, Inc., NY, 1982.

[11] P. De, W.D. Haseman and Y.H. So, Four schema approach: An extended model for database architecture. Information Systems 6, 1, 117–124, 1981.

[12] J.C. Emery, Cost-Benefit Analysis of Information Systems. SMIS Workshop Report No. 1, The Society for Management Information Systems, 1973.

[13] C. Gane and T. Sarson, Structured Systems Analysis: Tools and Techniques. Prentice Hall, Inc., Englewood Cliffs, NJ, 1979.

[14] M.M. Hammer et al., A very high level language for data processing applications. Comm. ACM 20, 11, 832–840, 1977.

[15] R. Hilton, The determinants of information value: Synthesizing some general results. Management Science 27, 1, 1981.

[16] P.G.W. Keen, Computer based decision aids: The evaluation problem. Sloan Management Review 16, 3, 17–29, 1975.

[17] P.G.W. Keen, M.S.S. Morton. Decision Support Systems: An Organizational Perspective. Addison Wesley Reading MA, 1978.

[18] J. King, E. Schrems. Cost-benefit analysis in information systems development and operation. Computing Surveys 10. 1, 1972.

[19] J.P.C. Kleijnen. Computers and Profits: Quantifying Financial Benefits of Information. Addison Wesley, Reading, MA, 1980.

[20] K.E. Knutsen, R.L. Nolan. Assessing computer costs and benefits. Journal of Systems Management 25, 2, 28–34, 1974.

[21] C.H. Kriebel. Information processing and programmed decision systems. Management Science 16, 3, 149–164, 1969.

[22] CR. Litecky. Intangibles in cost-benefit analysis. Journal of Systems Management 15–17, February, 1981.

[23] J Marschak. Economics of information systems. Journal of American Statistical Association 66, 333, 192–219, 1971.

[24] R.O. Mason, I.I. Mitroff. A program for research on management information systems. Management Science, 22, 10, 1087-1096, 1976.

[25] G. Matlin. What is the value of investment in information systems: MIS Quarterly 3, 3, 5–34, 1979.

[26] A.M. McDonough, Information Economics and Management Systems. McGraw Hill, Inc., NY, 1963.

[27] F.R. McFadden, J.D. Suver. Costs and benefits of a database system. Harvard Business Review 56, 1, 131–139, 1978.

[28] E. McLean. End users as application developers. MIS Quarterly 3, 4, 1979.

[29] T. A. Naylor. Management is drowning in numbers. Business Week. Industrial Edition No. 2682, 14–16, 1981.

[30] I. Orman. A familial model of data for a multilevel schema framework. Information Systems 7, 4, 1982.

[31] L. Orman. An array theoretic specification environment for decision support systems. Policy Analysis and Information Systems 6. 4. 1982.

[32] L. Orman. A familial specification language for database application systems. Computer Languages, forthcoming.

[33] L. Orman. A multilevel design architecture for decision

support systems. Cornell University BPA Working Paper, 1982.

[34] M.M. Parker, Enterprise information analysis. Cost benefit analysis and the data managed system. IBM Systems Journal 21, 1, 108–123, 1982.

[35] A.D. Pendleton, BMT: A Business Modeling Technology, in The Economics of Information Processing, Vol. 1, John Wiley & Sons, Inc., NY, 1981.

[36] N.S. Prywes, A. Pnveli and S. Shastry. Use of nonprocedural specification language and associated program generator in software development. ACM Transactions on Programming Languages and Systems 1, 2, 196–217, 1979.

[37] J.F. Rockart. Chief executives define their own data needs. Harvard Business Review 57, 2, 81–93, 1979.

[38] J.T. Schwartz. Principles of specification language design with some observations concerning the utility of specification languages, in Algorithm Specification, R. Rustin (ed.), Prentice Hall, Inc., Englewood Cliffs, NJ, 1971.

[39] M.E. Senko. A query maintenance language for the data-independent accessing model. Information Systems 5, 4, 257–272, 1980.

[40] C.E. Shannon. A mathematical theory of communication. Bell System Technical Journal 27, 623–656, July, 1948.

[41] D.W. Shipman. The functional data model and the data language DAPLEX. ACM Transactions on Database Systems 6, 1, 140–173, 1981.

[42] H.A. Simon. The New Science of Management Decision. Harper & Row, NY, 1960.

[43] R.K. Stamper. Some ways of measuring information. Computer Bulletin 15, 12, 432–436, 1971.

[44] E.A. Stohr. Information systems for observing inventory levels. Operations Research 27, 2, 242–259, 1979.

[45] D. Teichroew, H. Sayani. Automation of system building. Datamation 25–30, August, 1971.

[46] D. Teichroew, E.A. Hershey III. PSL/PSA: Computer-aided technique for structured documentation and analysis of information processing systems. IEEE Transactions on Software Engineering 3, 1, 41–48, January, 1977.

[47] J.A. Zachman. Business Systems Planning and Business Information Control Study: A Comparison. IBM Systems Journal 21, 1, 1982.
