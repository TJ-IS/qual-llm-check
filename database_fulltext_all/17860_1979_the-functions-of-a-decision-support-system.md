---
otero_id: 17860
otero_key: "UWDPZC8E"
title: "The functions of a decision support system"
authors: "Robert W. Blanning"
year: "1979"
journal: "Information & Management"
doi: "10.1016/0378-7206(79)90039-9"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# The Functions of a Decision Support System

Robert W. Blanning

Assistant Professor of Decision Sciences, The Wharton School, University of Pennsylvania, PA 19174, USA

The growing literature on decision support systems outlines their principal characteristics and presents case studies of successful systems. This paper reviews the literature, describes six functions that a decision support system may perform for a manager or staff analyst, and introduces a new technique, functional mapping, for representing these systems.

Keywords: Decision support systems, planning, data management, planning models.

![](/api/attachments/UWDPZC8E/fulltext/images/31f0469d10921e4fcdc378c3ccb14b5a78793cbbdce50ec0a33aa18bfc280343.jpg)

Robert W. Blanning is Assistant Professor of Decision Sciences at The Wharton School, University of Pennsylvania. He received a B.S. in physics from the Pennsylvania State University, an M.S. in operations research from the Case Institute of Technology, and a Ph.D. from the University of Pennsylvania, specializing in operations research and management information systems, and he has taught in the Schools of Management

at New York University. He has also worked as a nuclear engineer for the General Electric Company and a research analyst in the Corporate Operations Research Group of the Mobil Oil Corporation. His teaching and research interests are in the use of decision support systems in industry and government.

## 1. Introduction

The past 20 years has witnessed the rapid growth of two important sciences — information science and management science — that are beginning to have a significant impact on the ways in which managers make decisions and implement them. The impact of these sciences arises in part from their individual contributions, but increasingly it stems from their collective ability to provide managers with rapid access to selected data and their analyses. A set of procedures that provides such access – a decision support system (DSS) – may store and retrieve data, process the data, and in some cases perform analyses such as linear programming and simulation on them. The growing literature on DSS describes these separate applications and discusses the design of different types of systems. The purpose of this paper is to classify these systems in terms of the functions they perform for a manager and to examine the characteristics of the DSS that perform these different functions.

## 2. What is a DSS?

Most discussions of DSS center on the differences between such a system and (1) decision models and (2) management information systems. For example, the papers presented at a recent conference on DSS [1] emphasized four characteristics of a DSS:

1. A DSS facilitates interaction between computers and decision-makers. For example, a DSS is "designed to impact the management function more directly," is "an effort to bring the computer closer to the decision maker," and is "put at the direct and personal disposal of the manager."

2. A DSS assists managers in making unstructured or partially structured decisions in which judgmental issues are paramount. For example, DSS "are designed to support mainly nonstructured decisions for which relevant data and solution processes are difficult to define in advance," "are designed to function as a consultant," and "allows a decision maker to ask ad hoc questions in a nonprocedural English-like query language."

3. A DSS is comprehensive with regard to the types of decision processes supported and/or with regard to the functions it can perform. For example, a DSS is described as “supporting the planning, finance, marketing, and operating functions,” “servicing a wide variety of multivariate modelbuilding techniques,” and “providing information for operational and budget planning.”

4. A DSS is useful. That is, it “applies to the subset of management information systems that truly support decision-making processes.” The implication is that many management information systems (and possibly that many management science efforts as well) have not been successful in this regard.

This thinking is consistent with that described in a recent book [2] on DSS, which states that these systems “(1) assist managers in their decision processes in semistructured tasks, (2) support, rather than replace, managerial judgment, and (3) improve the effectiveness of managerial decision making rather than its efficiency.” This text also points out that in addition to computer science (and MIS) and management science, several other disciplines are relevant to the design and implementation of a DSS-specifically, behavioral science, information economics, and management.

## 3. The Functions of a ISS

Although the properties outlined above describe certain important characteristics of a DSS, they do not describe the specific functions that a DSS performs for a line manager or a staff analyst. However, this can be inferred by examining the examples of DSS given in the references and in other literature that present frameworks for describing management information systems [3–6] and DSS [7,8]. Such an examination suggests that a DSS may perform one or more of six functions, as follows:

1. Selection of data from a data base. This function is not as widely used as the others, primarily because the requirements for a DSS outlined above (such as assisting in nonstructured decision making and providing a comprehensive view of an organization) are most frequently accomplished not by retrieving data but by performing analyses of the data, as performed by the following DSS functions. Where used, this function may be facilitated by data base management systems [9–13] and query languages that are somewhat restricted subsets of natural language.

2. Aggregation of data into totals, averages, frequency distributions, etc. This is more useful than the first. In fact, some of the literature on management information systems suggests that an important function of the DSS is to present summaries of data acquired by transaction processing systems (e.g., see [14,15]). These systems include financial reporting and many production and distribution control systems. A DSS performing such a function is of limited use in solving unstructured problems, but it can help to identify problem areas (such as cost overruns and low service levels) for further investigation. It also meets the comprehensiveness requirement, because it provides consolidated financial and other statements.

3. Estimation of the parameters in a probability distribution. This is accomplished by performing statistical analyses of data to determine relationships between important variables, and it is sometimes accomplished not only by means of statistical packages [16], but also by means of interactive data analysis packages [17]. A DSS performing this function is often used when relationships between important variables are difficult to determine but data resulting from processes governed by these relationships are available. Examples are statistical analyses of marketing data [18] and economic data [19,20].

4 Simulation to calculate the anticipated consequences of proposed decisions and/or of possible changes in the corporate environment. This technique has been widely used at the lower levels of corporations to address well structured logistical problems [21,22], and increasingly it is being used to address problems at the corporate level. (See the examples described 23–26] and the surveys reported in [27–30].) The widespread use of simulation has given rise to an abundance of computer languages for constructing and solving logistical simulations [31–33] and planning simulations. The latter languages, called planning languages [34], are usually based on existing scientific languages, but provide input generation, report writing, and sensitivity analysis capabilities. These languages include PLANCODE [35,36], a PL/1-based language, EMPIRE [37,38], a FORTRAN-based language, and FPS [39], APL-based language, and FALCON/FORECAST [40,41], a FORTRAN-based financial consolidation and simulation system. Although these languages are primarily used in industry, some are also used in government. For example, SIMPLAN [42] has been used both in industry [43] and government [44].

A DSS containing a corporate simulation fulfills the requirements of the previous section in three principal ways. First, it generally takes a comprehensive view of the organization – that is, it is usually not very detailed but is broad in scope. Second, planning languages may improve the interaction between computers and decisionmakers. Third, the process of constructing the model will often lead to useful insights into often poorly understood interactions between divisions or departments and between the corporation and its environment (e.g., raw material prices, government regulations, competitors' pricing policies, etc.).

5. Equalization to calculate decisions whose consequences will meet certain consistency conditions. This is typically accomplished by simultaneous linear equations describing balances in the financial and material flows in a corporation (e.g., that a balance sheet must balance and the inventory at the end of any period must be the inventory at the start of the next period) [45–47] and by interindustry economic models that balance the supply and demand in each of several industries [48,49]. The advantages of a DSS performing equalization are the same as those of simulation except that most planning languages do not facilitate the resolution of simultaneous relationships.

6. Optimization to determine decisions that will maximize or minimize a single measure of performance or cost without violating constraints on other such measures. In most cases, this consists of a mathematical programming algorithm that minimizes operating costs within logistical constraints [50,51], but some of the newer systems maximize a measure of financial performance (net income, increase in retained earnings) with appropriate constraints on capital structure, production capacity, etc. [52,53]. An increasingly prominent source of constraints in corporate models is legislation and other government regulation. The computer support for a DSS performing this function is similar to that for a simulation except that planning languages are not as useful. However, interactive matrix generation and report writing languages are sometimes used to facilitate interaction with users [54].

## 4. Functional Mapping of a DSS

A DSS (such as those described in [55–59]) will often perform more than one of the above functions, while the subsystems performing various functions may be found in several parts of the organization implementing the DSS; they may even be found outside the organization. Thus, it is not necessary, and in some cases not possible, for all of the components of a DSS to be under the immediate control of either its designer or users.

If a DSS performs more than one function, it may be useful to construct a representation of the DSS that specifies: (1) the functions that it performs, (2) the relationships between them, defined in terms of interfunctional information flows, and (3) the organizational responsibilities for implementing the functions. This will be called a functional mapping of the DSS. A functional mapping can be represented by a matrix with the six DSS functions along one dimension, the organizational units along the other dimension, the functional components in the cells, and the interfunctional information flows by arrows.

The functional mapping approach to DSS design may help to address three concerns of managers about the application of information processing technology to decision-making. The first is the time needed to develop, implement, and use these systems $[60–62]$ , which has led to the development of interactive systems $[63,64]$ and to methodologies for developing such systems $[65,66]$ . The second is the fragmentation of information systems efforts in many large organizations, which has led to suggestions that these systems and efforts be coordinated $[67,68,69]$ , despite the assertion that total or integrated information systems cannot be constructed $[70]$ . The third concerns the justification of proposed DSS efforts to ensure that costs are commensurate with anticipated benefits $[71]$ , which has resulted from the realization that information is an economic resource $[72,73]$ and that more information need not result in better decision-making and may be detrimental $[74]$ .

Functional mapping may help to address the first two concerns -- time and fragmentation -- by structuring DSS modules, making explicit the responsibilities for their implementation, and identifying existing sources of information that may contribute to the DSS. Thus, it may facilitate such design methodologies as Little's decision calculus [75] and Hayes and Nolan's inside out approach [76] (an evolutionary alternative to top down and bottom up design), and it may provide a framework for the implementation of software that is directed towards systems integration, such as data management systems and model management systems [77,78]. Functional mapping may also be useful in the evaluation of DSS costs and benefits, especially when the DSS contains decision models (the last three of the six functions); one can use a decision model to estimate the value of its inputs by performing sensitivity analysis [79], and the sensitivity analyses produced by several interdependent models may be integrated into sensitivity analyses for the entire set of models [80].

The functional mapping approach and some of its uses can be illustrated in an example. The vertically-integrated division of a manufacturing corporation was concerned about the size of its product line and the growth in its inventories. A DSS was constructed to determine the financial and logistical impact of proposed changes in its product line and the level of its safety stock. (The marketing impact was determined separately.) The DSS, which consisted primarily of a simulation of the production-inventory process containing an optimal order quantity model and a sales forecasting model, satisfied several of the criteria for a DSS listed above. It helped to structure a component of a more general unstructured problem, and it was fairly comprehensive. It also satisfied the criterion of usefulness. It showed that an elimination of certain slow moving items in the product line would reduce revenues at a much lower rate than production costs (approximately 40%), but that any financially significant reduction in the safety stock of the remaining products would bring about an unacceptable reduction in customer service. The results were presented to management on a Friday morning, and the division's product line committee met on Monday to discuss specific reductions in the product line.

A functional mapping of the DSS appears in Figure 1. The functional components are as follows: (1) sales history, aggregated by the marketing department; (2) sales forecast, prepared by exponential smoothing; (3) unit costs, calculated by the manufacturing department; (4) cost of capital, furnished by the corporate headquarters and used to calculate inventory holding costs; (5) reorder point and optimal order quantity calculations, using a standard inventory model; and (6) simulation – that is, a deterministic simulation calculating total production and inventory costs using the information from the other components. (For a description of a similar but simpler system, see [81].)

![](/api/attachments/UWDPZC8E/fulltext/images/855cfa03ecc034eb2d9fde423c01fea19d66883ba3ba14661a7fa4afaa989f9c.jpg)  
Fig. 1. A Functional Mapping.

The functional mapping approach was useful in addressing the three management concerns identified above. It helped to reduce the development time for the project by identifying existing modules that could be modified for inclusion in the system, such as the sales forecasting and reorder point modules, which greatly reduced the development time. It also helped to coordinate the project by making explicit the responsibilities for modifying the modules. Although responsibility for designing the system was assumed by a team of consultants (of which the author was a member), the programming, file formatting, etc., was done by company personnel, and it was necessary to arrive at an explicit partitioning of responsibilities. The mapping was only of limited use in addressing the second concern — fragmentation — because the evolutionary design methodologies identified above were not employed on this project. That is, once the system was used for the product line and inventory policy analyses, it was not adapted for use in other studies. The mapping was also useful in justifying the project and its results to management, but not in the way described above (i.e., by a formal cost/benefit analysis). Rather, it was used to demonstrate that many of the components of the system were taken from existing sales forecasting, production scheduling, and inventory control programs which had been in use for years. The effectiveness of this approach is consistent with a recent theory that managers evaluate decision models not by deductively inferring their characteristics from a cost/benefit analysis, but by inductive inference based on observation of similar models in similar circumstances [82].

## 5. Summary

A decision support system is described here in terms of the functions it performs for a manager or staff analyst. A new form of representation, functional mapping, is presented as a way of describing these functions, their interrelationships, and the organizational responsibilities for implementing them. This approach is especially useful in designing systems whose components perform a variety of functions and are located in different parts of an organization, because it illustrates graphically the interactions between the functions and the organizational responsibilities for implementing them. Although the functional mappings are quite complex for systems of this type, they are also relatively simple descriptions of quite complex systems. In this respect, a functional mapping is similar to a flowchart, decision table, data structure diagram, etc. That is, it describes from a particular point of view, the important components of a system and the interactions between them.

## References

[1] E.D. Carlson, ed. "Proceedings of a Conference on Decision Support Systems", Data Base 8(3), Winter 1977.

[2] P.G.W. Keen and M.S. Scott Morton, Decision Support Systems: An Organizational Perspective (Addison-Wesley, Reading, 1978).

[3] G.A. Gorry and M.S. Scott Morton, "A Framework for Management Information Systems", Sloan Management Review 13(1), Fall 1971, pp. 55–70.

[4] C.R. Sprague, "Barriers to Progress in Information System Design: Technological or Not", Data Base 5 (2, 3, and 4), Winter 1973, pp. 115–120.

[5] F.W. McFarlan, R.L. Nolan, and D.P. Norton, Information Systems Administration (Holt, Rinehart and Winston, New York, 1973). See especially Chapter 3: "Frameworks for Information Systems Design", pp. 32–53.

[6] J.V. Hansen, L.J. McKell, and L.E. Heitger, "Decision-Oriented Frameworks for Management Information System Design", Information Processing and Management 13(4), 1977, pp. 215-225.

[7] S.L. Alter, "How Effective Managers Use Information Systems", Harvard Business Review 54(6), November-December 1976, pp. 97–104.

[8] S. Alter, "A Taxonomy of Decision Support Systems", Sloan Management Review 19(1), Fall 1977, pp. 39-56.

[9] C.J. Date, An Introduction to Database Systems (Addison-Wesley, Reading, 1975).

[10] E.H. Sibley, ed., "Special Issue: Data Base Management Systems", Computing Surveys 8(1), March 1976.

[11] C. Mohan, "An Overview of Recent Data Base Research", Data Base 10(2), Fall 1978, pp. 3–24.

[12] B. Sneiderman, "Design, Development and Utilization Perspectives on Database Management Systems", Information Processing and Management 13(1), 1977, pp. 23–33.

[13] J.L. Berg, "Data Base Directions: The Next Steps", Data Base 8(4), November 1976.

[14] J.D. Aron, "Information Systems in Perspective", Computing Surveys 1(4), December 1969, pp. 213-236.

[15] J.C. Emery, Organizational Planning and Control Systems: Theory and Technology (Macmillan, New York, 1969): Chapter 3: "The Technology of Information Systems", pp. 34–65.

[16] W.R. Schucony, B.S. Shannon, Jr., and P.D. Minton, "A Survey of Statistical Packages", Computing Surveys 4(2), June 1972, pp. 65–79.

[17] S.G. Swordlow, "Interactive Data Reduction in Planning", Chapter 10 in: H. Sackman and R.L. Citrenbaum, eds., Online Planning: Towards Creative Problem Solving (Prentice Hall, Englewood Cliffs, 1972), pp. 365–384.

[18] W.R. King, Marketing Management Information Systems (Petrocelli/Charter, New York, 1977). See especially Chapter 3: "Information and Decision Models", pp. 49–64.

[19] L.R. Klein, A Textbook of Econometrics (Prentice-Hall, Englewood Cliffs, 2d ed., 1974).

[20] L.J. Parsons and R.L. Schultz, Marketing Models and Econometric Research (North-Holland Publishing Company, Amsterdam, 1976).

[21] D.M. Chorafas, Systems and Simulation (Academic Press, New York, 1965).

[22] J.R. Emshoff and R.L. Sisson, Design and Use of Computer Simulation Models (Macmillan, New York, 1970).

[23] G W. Gerschefski, "Building a Corporate Financial Model", Harvard Business Review 47(4), July-August 1969, pp. 61–72.

[24] A.N. Schrieber, ed., Corporate Simulation Models (University of Washington, Seattle, 1970).

[25] B.B. Jackson, Computer Models in Management (Richard D. Irwin, Inc., Homewood, 1979).

[26] P.H. Grinyer and C.D. Batt, "Some Tentative Findings in Corporate Financial Simulation Models", Operational Research Quarterly 25(1), March 1974, pp. 149–167.

[27] G.W. Gerschefski, "Corporate Models-The State of the Art", Management Science 16(6), February 1970, pp. B303-B312.

[28] T.H. Naylor and H. Schauland, "A Survey of Users of Corporate Planning Models", Management Science 22(9), May 1976, pp. 927–937.

[29] P.H. Grinyer and J. Woller, "Computer Models for Corporate Planning", Long Range Planning 8(1), February 1975, pp. 14–25.

[30] J.C. Higgins and R. Finn, "Planning Models in the U.K.: A Survey", Omega 5(2), February 1977, pp. 133–148.

[31] D. Teichrow and J.F. Lubin, "Computer Simulation-Discussion of the Technique and Comparison of Languages", Communications of the ACM 9(10), October 1966, pp. 723–741.

[32] H.S. Krasnow and R.A. Merikallio, "The Past, Present and Future of General Simulation Languages", Management Science 11(2), November 1964, pp. 236–267.

[33] G. Gordon, System Simulation (Prentice-Hall, Englewood Cliffs, 1969).

[34] E.G. Hurst, Jr., "Interactive Planning Systems: Their Characteristics, Use, and Future", presented at the Second Interamerican Conference on Systems and Informatics, Mexico City, November 1974. (Also Working Paper 74-11-04, Decision Sciences Department, The Wharton School, University of Pennsylvania, 1974).

[35] IBM System/370 Planning, Control and Decision Evaluation System (PLANCODE), General Information Manual, GH19-1103-1, IBM Corporation, 1975.

[36] IBM System/370 Planning, Control and Decision Evaluation System/Standard (PLANCODE/S), Program Reference Manual, SH19-1106-2, IBM Corporation, 1975.

[37] EMPIRE Modeling, Reporting, and Analysis System: An Introduction, ADR Services, Inc., 1978.

[38] EMPIRE Modeling, Reporting and Analysis: Version 2, ADR Services, Inc., 1978.

[39] APL Financial Planning System, Program Description/Operations Manual, SB21-1340-1, IBM Corporation, 1975.

[40] Financial Consolidation and Reporting, the FALCON System, User's Manual (Hackins and Sells, New York, 1975).

[41] Financial Modeling and Forecasting System (FORECAST), Forecast Guide for Management Planning Reports (Haskins and Sells, New York, 1977).

[42] SIMPLAN: Command Descriptions, Social Systems, Inc., Chapel Hill, June 1976.

[43] R.B. Mayo and Social Systems, Inc., Corporate Planning and Modeling with SIMPLAN (Addison-Wesley, Reading, 1979).

[44] J.H. Naylor, H.E. Glass, J. Wall, and D.N. Milstein, Simplan: A Computer Based Planning System for Government (Duke University Press, Durham, 1977).

[45] W.A. Sherden, "Origin of Simultaneity in Corporate Models", Proceedings of the Winter Simulation Conference, Washington, D.C., December 1976, pp. 449-457.

[46] J.M. Warren and J.P. Shelton, "A Simultaneous Equation Approach to Financial Planning", The Journal of Finance XXVI(5), December 1971, pp. 1123-1142.

[47] D. Schendel and G.R. Patton, "A Simultaneous Equation Model of Corporate Strategy", Management Science 24 (15), November 1978, pp. 1611–1621.

[48] W. Leontief, Input-Output Economics (Oxford University Press, New York, 1966).

[49] W.H. Miernyk, The Elements of Input-Output Analysis (Random House, New York, 1965).

[50] R.C. Pfaffenberger and D.A. Walker, Mathematical Programming for Business and Economics (Iowa State University Press, Ames, 1976).

[51] D.J. Wilde and C.S. Bleightler, Foundations of Optimization (Prentice-Hall, Englewood Cliffs, 1967).

[52] W.F. Hamilton and M.A. Moses, "An Optimization Model for Corporate Financial Planning", Operations Research 22(3), May-June 1973, pp. 677–692.

[53] D.M. Rychel, "Capital Budgeting with Mixed Integer Linear Programming: An Application", Financial Management VI(4), Winter 1977, pp. 11-19.

[54] D.I. Steinberg, "ALPS - An Easy to Use Mathematical Programming Package", paper presented at ORSA/TIMS Conference, November 1977.

[55] J.J. McSweeney, "Strategic Management Systems", Proceedings of the Fourth Annual Conference, Society for Management Information Systems, 1972, pp. 87–111.

[56] W.F. Hamilton and M.A. Moses, "A Computer-Based Corporate Planning System", Management Science 21(2), October 1974, pp. 148–159.

[57] J.B. Boulden, Computer-Assisted Planning Systems (McGraw-Hill, New York, 1975). See especially Chapter 7: "Strategic Planning/Potlatch Corporation," pp. 99-119.

[58] R.A. Seaberg and C. Seaberg, "Computer Based Decision Systems in Xerox Corporate Planning", Management Science 29(4), December 1973 (Part II), pp. 575-584.

[59] G.D. Brewer, Politicians, Bureaucrats, and the Consultant (Basic Books, New York, 1973).

[60] C.J. Grayson, "Management Science and Business Practice", Harvard Business Review 51(4), July-August 1973, pp. 41–48.

[61] J. Dearden, "Myth of Real-Time Management Information", Harvard Business Review 44(3), May-June 1966, pp. 123–132.

[62] J. Darden, "Computers: No Impact on Divisional Control", Harvard Business Review 45(1), January-February 1967, pp. 99–104.

[63] M.S. Scott Morton, Management Decision Systems (Division of Research, Graduate School of Business Administration, Harvard University, Boston, 1971).

[64] C.L. Meador and D.N. Ness, "Decision Support Systems: An Application to Corporate Planning", Sloan Management Review 15(2), Winter 1974, pp. 51–68.

[65] A.M. Geoffrion, J.S. Dyer, and A. Feinberg, "An Interactive Approach to Multi-Criterion Optimization", Management Science 19(4), December 1972, pp. 357-368.

[66] S. Alter, "Why is Man-Computer Interaction Important for Decision Support Systems", Interfaces 7(2) February 1977, pp. 109–115.

[67] T.R. Prince, Information Systems for Management Planning and Control (Irwin, Homewood, 1975).

[68] A. Ishikawa, Corporate Planning and Control Model Systems (New York University Press, New York, 1975).

[69] T. Hanold, "The Executive View of Management Information Systems", Special Report, The Society for Management Information Systems, 1972, pp. 1–12.

[70] J. Dearden, "MIS is a Mirage", Harvard Business Review 50(1), January-February 1972, pp. 90--99.

[71] J.L. King and E.L. Schrems, "Cost-Benefit Analysis in Information Systems Development and Operation", Computing Surveys 10(1), March 1978, pp. 19–34.

[72] J.C. Emery, "Cost/Benefit Analysis of Information Systems", in: J.D. Couger and R.W. Knapp, eds., Systems Analysis Techniques (Wiley, New York, 1974), pp. 395–425.

[73] R.L. Nolan, "Computer Data Base: The Future is Now", Harvard Business Review 51(5), September-October 1973, pp. 98–114.

[74] R.L. Ackoff, "Management Misinformation Systems", Management Science 14(4), December 1967, pp. B147-B156.

[75] J.D.C. Little, "Models and Managers: The Concept of a Decision Calculus", Management Science 16(8), April 1970, pp. B466–B485.

[76] R.H. Hayes and R.L. Nolan, "What Kind of Corporate Modeling Functions Best?" Harvard Business Review 52(3), May-June 1974, pp. 102-112.

[77] H.J. Will, "Model Management Systems", in: E. Grochla and N. Szyperski, eds., Information Systems and Organization Structure (Walter de Gruyter, Berlin, 1975), pp. 467–482.

[78] J.J. Elam, "Model Management Systems: A Framework for Development", Working Paper 79-02-04, The Wharton School, University of Pennsylvania, 1979.

[79] J.C. Emery, "Decision Models", Datamation 16(10), September 1, 1970, pp. 32–36, and 16(11), September 15, 1970, pp. 59–64.

[80] R.W. Blanning and R.H. Crandall, "Budget Planning and Heuristic Models", Urban Systems 3(2/3), 1978, pp. 101–116.

[81] B.B. Jackson and B.P. Shapiro, "New Way to Make Product Line Decisions", Harvard Business Review 57(3), May-June 1979, pp. 139–149.

[82] R.W. Blanning, "How Managers Decide to Use Planning Models", to be published in Long Range Planning, tentatively scheduled for Winter 1979.
