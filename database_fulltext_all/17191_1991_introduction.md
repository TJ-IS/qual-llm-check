---
otero_id: 17191
otero_key: "Z885XYSH"
title: "Introduction"
authors: "Robert W. Blanning; David R. King"
year: "1991"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(91)90059-k"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Introduction

Robert W. Blanning and David R. King

Robert W. Blanning is Professor of Management (Information Systems) at the Owen Graduate School of Management at Vanderbilt University. He holds a B.S. in Physics from the Pennsylvania State University, an M.S. in Operations Research from the Case Institute of Technology, and a Ph.D. from the University of Pennsylvania, specializing in operations research and management information systems. He has been a member of the faculties of the School of Business at New York University and the Wharton School at the University of Pennsylvania. His teaching and research interests are in model management systems, information economics, and the management applications of artificial intelligence. He has published in such journals as Management Science, Decision Sciences, Communications of the ACM, Naval Research Logistics Quarterly, Decision Support Systems, Information and Management, Omega, Policy Analysis and Information Systems, International Journal of Policy and Information, Human Systems Management, Journal of Information Science, Long Range Planning, and Technological Forecasting and Social Change. He has presented papers at such conferences as the National Computer Conference, the International Conference on Decision Support Systems, the Hawaii International Conference on Systems Sciences, the International Workshop on Expert Database Systems, and the International Workshop on Artificial Intelligence in Economics and Management. He is a member of the Board of Editors of the Journal of Management Information Systems, a member of the Editorial Boards of Decision Support Systems and Information Systems Research, and Associated Editor of Information and Decision Technologies, an Associated Editor in the Decision Support Systems Department of Management Science, and a member of the Board of Editors of Journal of Management Information Systems.

David R. King is the Director of Advanced Product Design and Development at Execucom Systems Corporation (Austin, TX). He holds a B.A., M.S. and Ph.D. in Sociology with a minor in mathematical statistics from the University of North Carolina, specializing in statistics and research methodology. He has been a member of the faculties of the Department of Sociology at the University of South Carolina, the University of Maryland at Baltimore County and Old Dominion University. His research and development interests involve the integration of artificial intelligence technologies and tools with decision support and database systems and intelligent user interfaces. He has published articles in the areas of expert systems applications in decision and database support, the use of natural language frontends and the use of expert system explanation facilities with financial planning systems. Current and upcoming articles will appear in Expert Systems for Business and Management, Expert Systems for Business and Accounting and in International Journal of Expert Systems with Applications. He is a member of the Association for Computing Machinery, the Institute of Information Management, and the American Association for Artificial Intelligence; has served as an Associate Editor for Management Science; is a Contributing Editor for the International Journal of Expert Systems with Applications and is the current Chairman for the Institute of Management's College of Artificial Intelligence for Management (TIMS/CAIMS).

In recent years researchers and practitioners have argued for combining knowledge based systems with conventional decision support systems (DSS) [1,2]. While standalone DSSs provide a wide variety of tools for creating and manipulating mathematical models of the activities of an enterprise, they offer little in the way of automated assistance, interpretation and explanation. The addition of knowledge based technology to a DSS has the potential to extend the functionality of the DSS by providing capabilities which could

\- Help with the formulation of problems and models for analysis.

\- Select appropriate procedures for analysis based on problem specifications.

\- Interpret and explain modeling results.

\- Draw conclusions from model results and provide supportive justifications for those conclusions.

\- Diagnose problem situations and formulate of remedial plans of action.

\- Monitor variances between model results and user expectations and assumptions.

\- Determine whether user-specified courses of action will result in desired goals.

In essence a system combining knowledge base and decision support technologies could provide users with “intelligent assistance” at various stages of the decision making process (from model specification to analysis to strategy formulation).

To date two basic approaches have been used to couple these technologies. In the first approach the DSS serves as a sophisticated (financial) calculator which passes its results to an expert system for analysis. These systems have been labeled “management expert systems.” [3] In the second approach, various knowledge base technologies are embedded at selective points in the DSS. These systems have been called “intelligent” or “active” DSS [4].

Most of the effort to combine these technologies have produced standalone “management expert systems.” Here, the expert system contains the knowledge of one or more experts or specialists in a specific application domain such as finance, accounting, marketing, logistics, etc. [5]. In these systems the DSS provides data describing the problem being solved, while the ES does the actual analysis. The FINEX system [6], designed to detect financial problems in petroleum companies, is a case in point. Here, a DSS (spreadsheet) is used to calculate standard financial ratios. The ratios are passed to ES which performs a variety of diagnostic tests and makes recommendations based on these tests.

In a management expert system the two systems can be either “loosely” or “tightly” coupled $[7]$ . In a loosely coupled system the DSS writes its results to an external file which are then read by the ES. A tightly coupled system combines into a single system the capabilities of an ES shell with those of a DSS. MDBS’ Guru product is a good example of a tightly coupled system $[8]$ . Here, the product contains spreadsheet, database and ES shell facilities. This avoids the inefficiencies of a communication link and only requires the user to learn a single command syntax rather than two or three. Yet, in either type of system the modeling or spreadsheet component is still rather “passive” in nature and serves a secondary role in the resulting knowledge base system.

While there has been a great deal of conceptual discussion about “intelligent” or “active” DSSs, there are very few examples of working systems. Unlike a management expert system, in an intelligent or active DSS the focus is on the DSS. Here, the function of the knowledge base component(s) is to “assist” the user. Assistance has been provided in one of two ways. In some intelligent or active DSSs, an expert system sits between the user and the DSS, acting as an intelligent frontend or help system. Probably the best example of this type of system is REX (the Regression Expert [9]) which is an expert help system offering advice to the users of the regression module in the “S” statistical package. In other cases, “demons” [10] are embedded in the system. A “demon” is a software interrupt that monitors changes in a system and activates whenever certain pre-specified events occur. “Demons” can be used to alert the user to specific results, to stimulate the user’s thinking by suggesting new ideas or approaches, or to determine the user’s goals and intentions and to offer criticism or support where appropriate.

The papers in this special issue exemplify the research being done in the area of “intelligent” or “active” DSS. All of the papers describe prototypical systems based on one or both of the above architectures.

The first two papers examine the use of “intelligent” frontends to the modeling process. In this respect, they follow in the tradition of the REX system. “PDM: A Knowledge-Based Tool for Model Construction” by Ramayya Krishnan describes a Prolog-based tool that helps “nonexpert” users construct Linear Programming models. “An Active Modeling System for Econometric Analysis” by Daniel Dolk and Donald Kridel discusses the PERM (Progressive Econometric Modeling) system which is designed to assist users with econometric estimation techniques. The basic structure of this system derives from Manheim’s original concept of an active DSS and employs not only an intelligent interface but also demon-based structures.

The next two papers describe systems where the knowledge base component is used to formulate and integrate model components. “Object-Oriented Model Integration in MIDAS” by Dempster and Ireland details a system for corporate debt planning in which the system integrates optimization and simulation modeling to produce borrowing plans designed to meet forecasted cash requirements. Similarly, in “Adapting the Behavior of a Job-Shop Scheduling System” by Collinot and Le Pape, the authors describe a system consisting of a series of knowledge base components used to automatically adjust (constraint-based) scheduling models based on unanticipated events occurring on the factory floor.

The systems discussed in the first four papers all assume that the user is a “non-expert.” Implicitly, this means that the user is unable to use the system to its fullest extent (if at all) without the aid of the knowledge base. The systems described in the last two papers take a different approach. These latter systems are based on “co-operative” processing in which the user and the system are either co-equals or the user maintains more control. “A Conceptual Framework for Knowledge-Based Critic Systems” discusses a series of systems which are based on a “critiquing” model. The first of these critics offers programming advice to Lisp programmers, a second provides advice to the designers of window based user interfaces, and the final system offers recommendations to architectural designers. The last paper in the issue, “JANUS: A Paradigm for Active Decision Support” by Raghavan, also discusses a collaborative system aimed at stimulating and critiquing the ideas of the decision maker during the decision making process. A novel element of the system is a series of agents with “mind-expansion” personalities that encourage a user to explore a problem from different viewpoints depending on the personality.

The pioneers of the DSS movement felt that computers had frequently been used to replace, rather than support, managerial judgement and thus were becoming decision makers rather than decision support tools. This led to the conviction that DSS designers should take special pains to ensure that DSSs not be allowed to dominate the decision process. There are ways, however, in which a DSS can be an intelligent and active partner in the decision making process without exercising domination. The papers in this special issue examine and illustrate some of the possibilities.

Initial versions of the papers in this issue appeared in the Proceedings of the Decision Support and Knowledge-Based Systems Track of the Twenty-Second Annual Hawaii International Conference on Systems Sciences (HICSS-22 [11]). The papers were selected from a group of the “best” papers at the conference and have been substantially revised for this issue. The systems described in the papers have been modified to reflect some of the discussion and suggestions aimed at the earlier versions of the papers.

## References

[1] Turban, E. and Watkins, P. Integrating Expert Systems and Decision Support Systems, MIS Quarterly (Nov. 1986).

[2] Federowicz, J. and Williams, G. Representing Modeling Knowledge in an Intelligent Decision Support System, Decision Support Systems 2 (March 1986) 3–14.

[3] Ernst, C. (ed) Management Expert Systems (Addison-Wesley, Reading, MA, 1986).

[4] Manheim, M. and Isenberg, D. A Theoretical Model of Human Problem-Solving and Its Use for Designing Decision Support Systems, in: Proc. of the Twentieth Hawaii International Conference on Systems Sciences: Vol. I – Architecture, Decision Support Systems and Knowledge Based Systems (1987) 614–627.

[5] Blanning, R.A Survey of Issues in Expert Systems for Management, in: B. Silverman, Ed., Expert Systems for Business (Addison-Wesley, Reading, MA, 1987).

[6] Kershberg, L. FINEX: A PB-based Expert Support System for Financial Analysis, in: C. Ernst, Ed., Management Expert Systems (Addison-Wesley, Reading, MA, 1986).

[7] King, D. Modeling and Reasoning: Integrating Decision Support with Expert Systems, in: J. Liebowitz, Ed., Expert Systems for Business and Management (Prentice-Hall, Englewood Cliffs, NJ, 1990).

[8] Holsapple, C. and Whinston, A. Expert Systems Using Guru (Dow Jones-Irwin, Homewood, IL, 1986).

[9] Gale, W. REX Review, in: W. Gale, Ed., Artificial Intelligence and Statistics (Addison-Wesley, Reading, MA, 1986).

[10] Holsapple, C. Adapting Demons to Knowledge Management Environments, Decision Support Systems 3 (Dec. 1987) 289–298.

[11] Blanning, B. and King, D. (eds) Proc. of the Twenty-Second Annual Hawaii International Conference on Systems Sciences: Volume III – Decision Support and Knowledge Based Systems, IEEE Computer Society Press, Washington, DC (1989).
