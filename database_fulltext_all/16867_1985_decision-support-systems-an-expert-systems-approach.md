---
otero_id: 16867
otero_key: "FJ7MFVTH"
title: "Decision support systems: An expert systems approach"
authors: "Arun Sen; Gautam Biswas"
year: "1985"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(85)90239-8"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Decision Support Systems: An Expert Systems Approach

Arun SEN $^{+}$ and Gautam BISWAS $^{*}$

$^{+}$ Department of Management Science, College of Business Administration, and $*$ Department of Computer Science, University of South Carolina, Columbia, SC 29208, USA

This paper provides a conceptual framework for designing decision support systems (DSS) using an expert systems approach. Currently there is a significant trend towards the use of knowledge-based systems techniques in DSS design, but a comprehensive framework is yet to be proposed. Our paper addresses this problem and presents such a framework. Efforts are currently underway to design, implement and test a system based on this framework.

Keywords: Decision support systems; Expert systems; Decision support.

![](/api/attachments/FJ7MFVTH/fulltext/images/f8ef35f052104959090d8da46cc2976ee4ba67937ef2891458eaf2358fbc0ba7.jpg)

Gautam Biswas is an Assistant Professor of Computer Science at the University of South Carolina. His primary research interests are in the fields of Artificial Intelligence, Expert Systems, Computer Vision, Pattern Recognition and performance of Parallel algorithms. Dr. Biswas received his B. Tech. degree in Electrical Engineering at the Indian Institute of Technology, Bombay, in 1977 and his M.S. and Ph.D. degrees in Computer Science from Michigan State University in 1979 and

1982, respectively. He has published in the IEEE Transactions on Pattern Analysis and Machine Intelligence, and Pattern Recognition Letters.

![](/api/attachments/FJ7MFVTH/fulltext/images/a461d0afb0cc092b35628a8fc5b7b7c633e27ecd54999f1dc6d588e6bbc9b7b0.jpg)

Arun Sen is an Assistant Professor of Management Science. He received a B.S. in Physics from Bhagalpur University, an M. Tech. in Electronics from Calcutta University, an M.S. in Computer Science from the Pennsylvania State University, and a Ph.D. in Business Administration from the Pennsylvania State University. His teaching and research interests are decision support systems, management information systems, data base systems, distributed processing, artificial intelli

gence and its use in data base systems, business expert systems, office information systems, applied operations research and management science, information resource management, and EDP auditing. He has published in Information Systems, MIS Quarterly, and other journals.

## 1. Introduction

The term ‘decision support’ first began to appear in titles of research papers and in conferences in early 1970s [8]. Computers were usually integrated into such systems as support mechanisms; as a whole, these came to be known as Decision Support Systems.

Traditionally, information management systems have been Electronic Data Processing (EDP) systems, Management Information Systems (MIS), or Decision Support Systems (DSS). Users of these systems are from various levels of the organizational hierarchy: operations, management control, and strategic planning. According to Anthony [3], the strategic planning level is the highest level in the organization. At this level, one decides upon the objectives, and the policies that govern the acquisition, use, and disposition of these resources. Thus, strategic planning is the process of formulating long range plans and policies for the organization. Management control, at the next lower level, deals with a process that assures managers that resources are obtained and used efficiently in the accomplishment of the organizational objectives. At the lowest level, operations control assures that tasks are carried out efficiently.

At each level, according to Simon [33] and Gorry and Scott Morton [21], there are three types of problems that users can expect: structured, semistructed, and unstructured. Structured problems are those that are routine, and can be solved using standard solution techniques. Semi-structured and unstructured problems, however, do not usually fit a standard mold, and are generally solved by examining different scenarios, and asking 'what if' type questions. For the sake of convenience, we group these two types of problems into a 'what if' problem domain. Typically, EDP and MIS are used to support and solve problems in the structured domain for operation and management control people. DSS are designed for solving the rest [1,2,5–9,11,12,32]. These include the 'what-if' domain and the structured problem domain for strategic planners.

In this paper, we focus our efforts on the design aspects of DSS. We propose that although DSS have been implemented traditionally on single and specific problem domains, current expert systems design techniques $[4,13,23]$ can be exploited to develop more domain-independent and user-friendly systems.

DSS need to be user-friendly so that they can be used by managers who are knowledgeable in their fields of expertise, but may have very limited experience in computer usage. This user-friendlines can be accomplished if the DSS has knowledge about the user's domain, the type of problems encountered, and the tools needed to solve them. Domain independence may be achieved, if the domain knowledge component of the system is a 'plug in' type module, which can be replaced by another 'plug in' module to change the domain of expertise. We will call this type of DSS an Expert DSS (or XDSS). The rest of this paper presents a conceptual design for such systems.

## 2. DSS Design Expertise

According to Simon [33], the process of problem-solving and decision making consists of four phases: intelligence, design, choice, and review. The first phase, intelligence activity, involves searching the environment for conditions calling for decisions. The second phase, design activity, consists of inventing, developing and analyzing possible courses of action. The third phase, selecting a particular course of action from these alternatives, is called choice activity. The fourth phase, assessing past choices, is called review activity.

The domain of expert DSS involves the design activity phase. The specialized skills and tools used for modeling the activities in this phase are collectively called the DSS design expertise. There are three components of this expertise: domain expertise, tools expertise, and domain-tools mapping expertise. Domain expertise involves theories and concepts of a particular domain. For example, in the production planning domain, domain expertise will include knowledge about the planning horizon, forecasts of future demand and production center capacity. The tools expertise includes knowledge of planning models, mathematical programming techniques and simulation models needed in problem solving. This expertise also includes knowledge of tools integration, in case several tools may be required to solve a problem. The domain-tools mapping expertise provides ways to map a problem into the appropriate mathematical tools that are required for its solution.

In traditional DSS design [2,5-7,11,19,28,29,34,35] most of the expertise is assumed to reside with human experts, like management scientists, financial analysts, and accountants. DSS research, at present, is mainly involved in tools expertise. For such systems an architecture has been proposed [32], which can be represented as:

$$
\boldsymbol {S} = \left(\boldsymbol {U}, \boldsymbol {D}, \boldsymbol {D} ^ {*}, \boldsymbol {A}, \boldsymbol {R}, \boldsymbol {G}\right)\tag{1}
$$

U is a set of users who can be from the operations level, the management control level, the strategic planning level, or from a combination of these levels [3]. D in addition to representing needed data sets, can also be ad hoc data sets, a database obtained by a logical database design process [37,38] or a knowledge acquisition procedure (MYCIN project [13]), or a mix of all these types. D \* is a data management component, which can be a sophisticated Data Base Management Systems (DBMS), a Knowledge Base System (KBS), or an ordinary file system. A is a set of analytical tools; it can include different OR-models, statistical packages, forecasting techniques, simulation algorithms, and so on. The set R can have various types of output reports; some are predesigned and some are ad hoc. G includes different types of visual displays, such as: one-dimensional plots, multi-dimensional plots, and color graphics.

A general ‘tool-kit’ idea for DSS is very useful. However, a mere collection of tools does not represent a DSS. These tools need to communicate among each other and with the database, to facilitate easy utilization and access by users. This means that the user may have to access the data from a database in order to run a production planning model. When the model finishes execution, the user has to design the desired output formats to print the required reports. In this role the user acts as a tools expert and is responsible for integration of all components of the DSS. Often, as the domain encompassed increases in size, it may be asking too much of a user to provide all the integration information. This problem has long been recognized and several attempts have already been made to integrate the tools in the 6-tuple architecture to varying degrees.

In early DSS, everything was stored in files, and $D^{*}$ was a file management system. The only communication present was between the tools and the data. The data items were accessed first and then the analysis and/or reporting were carried out using R, A, and/or G. These DSS were studied extensively by Alter [1,2]. Integration is the big problem in such systems, usually requiring separate access facilities for different tools.

With the introduction of SPSS (Statistical Package for Social Sciences), SAS (Statistical Analysis System), IFPS (Interactive Financial and Planning System), and others such as in [11,29,32], several packages are now available to users. These packages contain several tools that can be invoked by names. Each, on execution, performs a specific task like analysis, reporting and so on. Input data to an invoked routine is supplied from files maintained jointly by the system and the user. A routine typically has the knowledge of the structure of these data files. For example, SAS usually needs a two-dimensional table for its data input. The users are forced to represent their data in this format. The integration among tools is achieved through this common structure. This type of integration may be characterized as simple physical integration.

Another type of integration has been attempted by Donovan in the GMIS project [15]. This is accomplished by creating a Virtual Machine (VM) manager. If a user wishes to use a model that operates on an APL/EPLAN analytical machine and also needs to access data from a SEQUEL database machine, the accessing request to the appropriate interface machine is automatically sent by the VM manager. Once the data is retrieved by the database machine, it is sent to the interface machine which reformats the information, if necessary, for its use by the analytical machine. This type of integration of tools is much more involved and can be characterized as complex physical integration.

Both approaches to integrate the tools of DSS have been in existence for sometime. While they provide good foundations to DSS design research, they are not complete. DSS, which use 'complex physical integration' are typically domain independent. But such systems assume that users have expertise with these tools. On the other hand, DSS based on 'simple physical integration' often are domain dependent (like IFPS). SAS enforces a common data structure which may not be a desirable feature. These systems also require users to be knowledgeable about tools and their physical forms. In light of these shortcomings, a new type of integration needs to be proposed that will allow DSS to be domain-independent and knowledgeable about its tools. The latter will make the system more user-friendly, as tools expertise will not be a requirement for the use of such a system. Lastly, this new integration should strive for logical independence, and should not explicitly enforce common data file structures on user data.

## 3. Towards Logical Integration

In a classification scheme for DSS designed by Bonczek et al. [7], the importance of data retrieval and analysis of data has clearly been recognized. With respect to data retrieval, they observe a progression from simple data structures, such as those used in lists, tables and files, to the network structuring techniques of artificial intelligence and database management. In data analysis, they report that the trend is toward increasingly complex or comprehensive models. The present-day emphasis is upon coordinated modeling of several problem areas. They think that 'this integration of models is necessary, if support of high-level decision making is to be enhanced, since high-level decision-making (e.g., strategic planning) involves many problem areas' (p. 345 in [7]). Their classification scheme consists of nine categories – A through I. In category A, a DSS requires the user to explicitly specify the procedure for retrieving data and the modeling algorithm. A DSS based on a language like FORTRAN will fall in this category. Category A is one extreme. In the middle is category E, where the invoked model acquires data by naming some reports. These reports are typically implemented as data files in a file-only environment or as subschemas in a DBMS environment. Bonczek et al. [7] feel that the DSS field, with regard to existing languages and software is presently centered in category E. Some examples of these system are SPSS, SAS and GMIS. At the other extreme, the requirements for category I are specified in terms of a problem definition; the system typically analyzes this definition to infer models and data needs. Bonczek et al. [7] speculate that the important advances in DSS software and languages may eventually come from experiences gained in artificial intelligence systems to move us up to category I from the present category E. Similar thoughts have been recorded by several authors, like Keen and Scott Morton [24], Gorry and Krumland [22] and Sprague and Carlson [33]. The latters' 'dialogue management' forms a basis for more natural man-machine interactions.

Several attempts [10,14,16–18,26,36] have been made to introduce knowledge-based system techniques into DSS design so as to move into category I. In a limited scope, Konsynski [26] and Elam [16] have attempted to design model management systems which are subsets of DSS. Konsynski [26] uses mathematical models with equations, elements and solution procedures as data models. The element types include time-series, sets, variables and parameters. Equations can be characterized as recursive, simultaneous, constraint and objective functions. The solution procedures include the range of specific techniques, like Newton's method, simplex method, etc. Each of these components are maintained in a model database and are characterized in a global directory. Once a request is made to do an econometric analysis, the global directory is searched to see which model, needs to be run. Data is obtained from the user and/or reference library.

In Elam's framework [16], a structure is presented to define and describe a model in terms of entity, relation and model types. It also uses model assumptions and model solution techniques as other parameters of the structure. In a somewhat wider context, Elam et al. [18], Elam and Henderson [17], and Dolk et al. [14] have attempted to collect meta information about models and how they are used in a decision-support context. The meta information about a model is collected in frames [14] and in semantic inheritance networks (SI-networks) [17,18]. A frame can be viewed as a set of slots, some of which contain fixed data values about that frame and, therefore, never change, and some of which contain default values which can be overridden by specific data differentiating the current situation from a generic frame. In a conceptual treatment [17,18], an argument has been made for the need of a SI-network. A semantic inheritance network is a directed graph of objects (as nodes) and relationships (as arcs). In a SI-network, a hierarchy of partitions is built in the network to propagate the inheritance of properties.

Bonczek et al. [8,10] offer a predicate-calculus based DSS. They use three systems: a language system (LS), a knowledge system (KS), and a problem processing system (PPS). The language system allows the user to express his query. The PPS analyzes the query and executes each operator (which are mostly model names) in the query. If data is needed, the KS is used. The KS contains knowledge of a problem domain. The analysis is done by the PPS using the 'resolution principle' [31] of mechanized theorem-proving in artificial intelligence.

The above systems suggest that at the strategic planning level there is a great need for different models to analyze and support decisions. These models need to be integrated automatically to make the system more user-friendly. Integration carried out at a physical level makes the resulting package very system dependent and requires that users have a lot of knowledge about implementation details. However, integration of models at the 'logical level' using knowledge-based systems techniques should make the package independent of the particular system they are implemented on.

The development of these systems is a step in the right direction, but the systems are not without problems. First, they all emphasize tools expertise only without much consideration of the entire DSS design problem. Secondly, sometimes, representational structures are arbitrarily chosen to store tools expertise. For example, Elam uses frame structures [16] or SI-networks [17,18]. Also, some systems, like Bonczek et al. [8,10] depend heavily on the resolution principle. It has been observed that systems based totally on the resolution principle often have problems converging to a desired solution, and are slow in execution.

## 4. An Expert Systems Approach

An important aspect common to the decision support systems developed in, or used by, the business community is their need to incorporate the A, R, and G with information-handling capabilities (D and D \*). We argued in the previous section that such integration should be performed at the logical level using knowledge-based systems techniques. This approach to design falls in the realm of expert systems design. An expert system deals with symbol manipulations rather than directly handling actual data values. Instead of being programmed to follow step-by-step procedures like a conventional computer program, a few general procedures for finding solutions to problems are encoded (inference scheme). To solve a particular problem, the system uses facts about the problem supplied by a user, plus its own extensive domain knowledge and general problem solving procedures to find a specific solution to the problem. The key to the systems expert-level decision making is the use of heuristics and the emphasis on knowledge, rather than on formal reasoning methods [23].

Therefore, the design of a DSS using expert system techniques, requires the development of a symbolic reasoning process and a knowledge base. The symbolic reasoning process follows an expert's line of reasoning from the stage of problem definition to its eventual solution. This is a complex process and needs three broad categories of knowledge. They are domain expertise, tools expertise and mapping expertise.

An architecture for a DSS based on expert systems approach (called XDSS) is proposed in Fig. 1. Notice that the knowledge base is made up of a number of components: one handles domain expertise; the tools expertise is distributed over several components according to our 6-tuple architecture presented earlier. These components, although not completely independent of one another, are typically maintained by experts in different areas; e.g., a DBA (Data Base Administrator) can maintain a data dictionary. Once a problem is defined and presented to the XDSS, it uses domain knowledge to understand the problem. The next step involves decomposing the problem into subproblems to be interpreted by the appropriate knowledge base components. Finally, after the results of each subproblem are obtained the XDSS integrated them into a solution.

The steps to accomplish this process are presented in Fig. 2. In the problem acquisition stage, the manager presents the problem to the system in the form of English text, and clarifies the goal of the problem solution. In the problem understanding phase, the XDSS looks at the text and analyzes it using the domain knowledge base component. A natural language (NL) processor is needed to un-

![](/api/attachments/FJ7MFVTH/fulltext/images/8e6732f64b8f5377a06d8b68a1a64009eb31067348d19031c87ff004b4d6729c.jpg)  
Fig. 1. The Architecture of XDSS.

derstand the text. The output from this stage are the data types, model class, output representation, and execution sequence. The data types tell us the type of data that are needed. The D and D \* components in the traditional definition of DSS [1] implied numeric or quantitative data. However, as Ganascia [19] has pointed out, in a number of applications, the reasoning and decision making process involves both quantitative and qualitative data (e.g., the context or conditions under which the quantitative data is collected). Again, expert systems techniques can be successfully used to integrate the two kinds of data [19], something that may be difficult to achieve by traditional methods. The model class suggests the broad category of models to be used in problem solution. The output representation provides the characteristics of the required output in terms of graphics or reports. The execution sequence is needed to chain different models and data accesses.

In the next phase (problem analysis selection), the model class is decomposed, using the model feature knowledge base component, into appropriate models that fit the problem definition. This component contains features of all models, arranged into different categories. The proper output scheme is also selected in a similar manner. The data types are checked against the data dictionary for validity.

![](/api/attachments/FJ7MFVTH/fulltext/images/de78877b7f972f655dc31db7b0515069789e8b11976b3b8d66def39358f1efe6.jpg)  
Fig. 2. Proposed Steps in XDSS.

In the next phase (integrated instance generation) using these components as well as the procedural knowledge for the database, models and output, an abstract representation of the entire analysis process for the problem is developed. Pictorially, this should look like some form of a flowchart. We call this flowchart an instance.

Finally, in the last phase of XDSS, the instance is executed using the execution knowledge stored in the knowledge base. Execution knowledge is needed as there will be various packages that can contain the model or the report.

## 5. Impact on Management

The paper presents a framework to design expert DSS (XDSS). It begins with a discussion on current DSS and argues the need for more user-friendly systems. The design and use of such a system depends upon domain and tools expertise. Domain expertise is the knowledge about the domain in which the DSS is to be used. Tools expertise is the knowledge about tools that the DSS uses. Traditionally, all these are left to 'the analyst' and the systems are designed to match their expertise, and not managers. XDSS framework is proposed to reverse this trend and make DSS useful to managers.

Managers may find the XDSS framework to be far-fetched and esoteric. But they need to look hard. The choice is very clear. On one hand, we have the traditional DSS – which have never been user-friendly; on the other, we have the XDSS. Several researchers in the DSS field have recorded the need for expert system techniques in designing DSS: Sprague et al. [34] in their concluding remarks say:

'Knowledge-base systems to support knowledge workers will be the trend' (p. 315 in [34]). Keen et al. suggest: 'AI may eventually be of direct value to MIS professionals trying to build tools that handle complex problems, that respond intelligently, and that permit the use of natural language' (p. 43 in [24]). Michaelsen et al. warn: Executives who choose to ignore expert systems may find themselves at a competitive disadvantage with the next decade.' (p. 240 in [30].

In our opinion the following are distinct advantages of XDSS:

1. It is user-friendly. As the problem acquisition is done in English and the rest of the system is transparent to the users, XDSS provides a high level of user-friendliness.

2. It can be a good teaching and training tool. As the system will be able to specify its reasoning and analysis process to the users, this can be used as a training device.

3. The system can be developed incrementally. As with all expert systems, XDSS can be started with a small scope. Once the experience is gained with the system, more and more areas can be supported by the XDSS.

4. After the system has become sufficiently knowledgeable through continual refinement, experts may find it useful to consult it when confronted with an unfamiliar issue.

Languages that can be used to implement such a framework are: PROLOG (Programming in Logic), EMYCIN (Extended MYCIN), LISP, OPS5, KRL (Knowledge Representation Language) and so on.

Finally, we conclude this paper by listing out the areas that we see the XDSS will be most helpful. They are:

1. In all areas of modelling and analysis;

2. In auditing;

3. In database management system, especially, in designing natural language interfaces; and

4. In integrating and using office systems.

## References

[1] Alter, S., A Taxonomy of Decision Support System, Sloan Management Review, (1977) 39–56.

[2] Alter, S., Decision Support Systems: Current Practice and Continuing Challenges, Addison-Wesley, Reading MA (1980).

[3] Anthony, R.N., Planning and Control Systems: A Framework for Analysis, Harvard University Press, Boston MA (1975).

[4] Barr, A. and E.A. Feigenbaum (eds.), The Handbook of Artificial Intelligence, William Kaufman, Stanford CA (1982).

[5] Bennett, J.L. (ed.) Building Decision Support Systems, Addison-Wesley, Reading MA (1983).

[6] Bennett, J., Integrating Users and Decision Support Systems. Proc. Sixth, Seventh Annul. Conf. Society for Management Information Systems (1976) 77–86.

[7] Bonczek, R.H., C.W. Holsapple and A.W. Whinston, The Evolving Roles of Models in Decision Support Systems, Decision Sciences, 11 (1980) 337–356.

[8] Bonczek, R.H., C.W. Holsapple and A.W. Whinston, Foundations of Decision Support Systems, Academic Press, New York NY (1981).

[9] Bonczek, R.H., C.W. Holsapple and A.W. Whinston, Future Directions for Developing Decision Support Systems, Decision Sciences, 11 (1980) 616–631.

[10] Bonczek, R.H. C.W. Holsapple and A.W. Whinstone, A Generalized Decision Support System Using Predicate Calculus and Network Data Base Management Management, Operations Research, 29 (1981) 263–281.

[11] Carlson, E.D. An Approach for Designing Decision Support Systems, Database, 10 (1979) 3–15.

[12] Davis, R., A DSS for Diagnosis and Therapy, Database, 8 (1977) 58–72.

[13] Davis, R., and D.B. Lenat Knowledge-Based Systems in Artificial Intelligence, McGraw-Hill, New York NY (1982).

[14] Dolk, D.R. and B.R. Konsynski, Knowledge Representation for Model Management Systems, working paper Univ. of Arizona, Tucson AZ (1983).

[15] Donovan, J.J., Data Base Systems Approach to Management Decision Support, ACM Trans. Database Systems, 1 (1976) 344–369.

[16] Elam, J.J., Model Management System: A Framework for Development, Tech. Report #79-02-04, Depart. Decision Sciences, The Wharton School (Feb. 1979).

[17] Elam, J.J., and J.C. Henderson, Knowledge Engineering Concepts for a Decision Support System Design and Implementation, Proc. Fourteenth Annual Hawaii Conf. System Sciences, 639–643, Western Periodicals, North Hoolywood CA (1980).

[18] Elam, J.J., J.C. Henderson and L.W. Miller, Model Management System: An Approach to Decision Support in Complex Organizations, Proc. First Intl. Conf. Information Systems, 98–110 (Dec. 8–10, 1980).

[19] Ganascia, J.G., Using an Expert System in merging Qualitative and Quantitative Data, Intl. J. Man–Machine Studies, 20 (1984) 319–330.

[20] Gerrity, T.P., Jr., The Design of Man-Machine Decision Systems: An Application to Portfolio Management, Sloan Management Review, 12 (1971) 59–75.

[21] Gorry, G.A. and M.S. Scott Morton, A Framework for Management Information Systems, Sloan Management Review (Fall 1971) 55–70.

[22] Gorry G.A. and R.B. Krumland, Artificial Intelligence Research and Decision Support Systems, in: Building Decision Support Systems, 205–219, J.L. Bennett, (ed.) Addison-Wesley, Reading, MA (1983).

[23] Hayes-Roth, F., D.A. Waterman, and D.B. Lenat (eds.), Building Expert Systems, Addison-Wesley, Reading MA (1983).

[24] Keen, P.G.W. and M.S. Scott Morton, Decision Support Systems: An Organizational Perspective, Addison-Wesley, Reading MA (1978).

[25] King, W.R. and D.E. Cleland, The Design of Management Information Systems: An Information Analysis Approach. Management Sciences, (1975) 286–297.

[26] Konsynski, B.R., On the Structure of a Generalized Model Management System, Proc. Fourteenth Annual Hawaii Conf. Systems Sciences, 630–638 (1980).

[27] Kroebar, D.W., H.J. Watson and R.H. Sprague, Jr., An Empirical Investigation and Analysis of Current State of Information Systems Evolution, Information and Management, 3 (1980) 35–43.

[28] Little, J.D.C., Brandaid, Operations Research, 23 (1973) 628–673.

[29] Meador, C.L. and D.N. Ness, Decision Support System: An Application to Corporate Planning, Sloan Management Review, 15 (1974) 51–68.

[30] Michaelson, R. and D. Michie, Expert Systems in Business Datamation, (Nov. 1983) 240–246.

[31] Robinson, J.A., A Machine-Oriented Logic Based on the Registration Principle, J. Assoc. Comput. Mach. 1 (1965) 23–41.

[32] Sen, A., Decision Support Systems: An Activity-oriented Design, J. Information Science 7 (1983) 23–30.

[33] Simon, H., The New Science of Management Decision, Harper and Row, New York NY (1960).

[34] Sprague, R.H. and E.D. Carlson, Building Decision Support Systems, Prentice-Hall, Englewood Cliffs NJ (1982).

[35] Starmer, C.F. and R.A. Rosate, A DSS for Management of Patients with Chronic Illness, Database 8 (1977) 51–57.

[36] Stohr, E.A. and M.R. Tanniru, A Data Base for Operation Research Models, Policy Analysis and Information Systems, 4 (Dec. 1980).

[37] Tsichritzis, D.C. and F.H. Lochovsky, Data Models, Pre- nctice-Hall, Englewood Cliffs NJ (1982).

[38] Yao, S.B., S.B. Navathe and J.L. Weldon, An Integrated Approach to Logical Data Base Design. Proc. New York University Symp. Data Base Design, 1–24 (May 17–18, 1978).
