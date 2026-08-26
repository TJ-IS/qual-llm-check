---
otero_id: 17304
otero_key: "S257BP2U"
title: "Model management systems"
authors: "Robert W. Blanning"
year: "1993"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(93)90019-y"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Model management systems An overview

Robert W. Blanning

Vanderbilt University, Nashville, TN 37203, USA

During the past fifteen years, model management has grown from a few suggestions that data management be enlarged to include decision models to an established but still growing field of study. We examine three central topics in model management. The first is model base structure and its correspondence to network and relational data base structures. The second is model base processing and the application of artificial intelligence to model interfacing, integration, construction, and interpretation. The third is the organizational environment of model management systems and the contribution of model management systems to organizational intelligence.

Keywords: Model management, Data management, Network systems, Relational systems, Artificial intelligence, Enterprise modeling, Organizational intelligence.

## 1. Introduction

During the past fifteen years there has been an evolution in the type of information sources used in DSS from an emphasis on stored data and data analysis to an increased reliance on decision models $[37,88,159]$ . This has led to a growing discipline of model management $[5,17,59,65,95]$ , as well as an increasing number of experimental and commercially implemented model management systems $[3,148]$ .

This evolution began in 1975 with the suggestion that decision models, like stored data, are an important organizational information resource

![](/api/attachments/S257BP2U/fulltext/images/23ccdcab594974719a0cb618b7c98ac8f6b29edf55a59312fbbff1bdcfb88a3f.jpg)

Robert W. Blanning is Professor of Management at the Owen Graduate School of Management at Vanderbilt University. He has a B.S. in Physics from the Pennsylvania State University, an M.S. in Operations Research from the Case Institute of Technology, and a Ph.D. from the University of Pennsylvania, specializing in operations research and management information systems. He has been a member of the faculties of the Schools of Business of New York University and

The Wharton School at the University of Pennsylvania. His teaching and research interests are in model management systems, information economics, and the management applications of artificial intelligence. He has published in Management Science, Decision Sciences, Communications of the ACM, Naval Research Logistics Quarterly, Decision Support Systems, Information and Management, Omega, Policy Analysis and Information Systems, International Journal on Policy and Information, Human Systems Management, Journal of Information Science, Long Range Planning, Technological Forecasting and Social Change and the Concise Encyclopedia of Information Processing in Systems and Organizations. He has presented papers at such conferences as the National Computer Conference, the International Conference on Decision Support Systems, the International Conference on Information Systems, the Hawaii International Conference on System Sciences, the International Conference on Information Resources Management, the International Workshop on Expert Database Systems, and the International Workshop on Artificial Intelligence in Economics and Management. He is an Associate Editor of Decision Sciences and Information and Decision Technologies, a member of the Editorial Boards of Decision Support Systems and Information Systems Research, and a member of the Board of Editors of Journal of Management Information Systems. He is editor of the text Foundations of Expert Systems for Management, published by Verlag Rheinland in 1990.

that should be managed effectively and that specialized information systems — that is, model management systems — should be developed for this purpose $[160,171]$ . The purpose of a model management system is to insulate the users of a DSS from the physical aspects of model base storage and processing, just as the purpose of a data management system is to insulate users from the physical aspects of data base storage and processing. This suggests a duality between stored data and decision models $[58,111]$ , and the purpose of model management research is to extend our existing knowledge of data management by investigating the properties of systems in which the information objects of interest are not files but rather are algorithms used to support decision processes.

In the following three sections we examine three topics of importance in model management. The first is the structure of model bases. Two structures have been proposed, one based on networks and one on relations, which correspond to the network and relational structures of data management. The second topic is model base processing. There have emerged during the past decade a variety of techniques, most of them based on artificial intelligence, for (1) interfacing models with their users; (2) integrating models with each other; (3) helping users to construct models; and (4) helping users to interpret model outputs. The third topic is the organizational environment of model management systems, in which notions of intelligence are also of interest. Specifically, we examine the contribution of model management systems to organizational intelligence.

## 2. Model base structure

Much of the early work on model management paralleled existing work on data management, and especially the network and relational approaches to data base organization. The most prominent first effort was an extension of the CODASYL standard for network data bases to include model bases $[39,40,96,161]$ . Another such effort is structural modeling, in which the components of a model or a model base are organized around a user's visual picture of a decision problem $[151]$ .

A more recent effort is structured modeling, in which important modeling concepts are organized in a directed acyclic graph, and these are mapped into the leaves of a tree representing a hierarchical decomposition of the modelling software $[74–76]$ . This provides a framework not only for model structuring but also for (1) model base documentation $[56]$ ; (2) the development of libraries of reusable model components $[77]$ ; and (3) object-oriented model management $[110]$ . Object-oriented systems provide two vehicles for model base communication, message passing and inheritance, and may serve as a platform for both models and their supporting data files $[54,87,105,129,165]$ .

A second approach to model management is based on the relational approach to data management $[131]$ and on notions of computed and virtual relations $[123]$ and the relational description of algorithms $[153]$ . A model is viewed as a virtual relation whose tuples do not exist in stored form but are generated on demand by stored algorithms, and model management is the organization and processing of virtual relations $[18,22,29,33]$ . The operations of relational data management are extended to include models — for example, a join of two models occurs when the output of one model is the input to another model $[27]$ . One problem in performing joins is that the models, ordered by their input and output attributes, may not form a partially-ordered set — that is, there may be cycles in the set. For example, in an economic modeling system with separate supply and demand models a cycle will exist, requiring the simultaneous (rather than sequential) calculation of equilibrium prices and volumes $[85]$ . The important issues here are the graphical representation of such model banks $[9]$ and the existence and uniqueness of equilibrium solutions $[1,26]$ .

The study of model base structure includes not only the syntactical issues address by networks and relations, but also certain issues in model semantics. In data management, an important approach to capturing data semantics is the entity-relationship model, in which interactions between files are made explicit and named [50]. This notion has been extended to model management, in which inter-model relationships are also identified and named [24]. The determination of network and relational model base structure also has implications for model base processing and specifically, for the linguistic interface between a model management system and its users. Several languages have been developed for network model banks $[41,48,64,100,167]$ , and linear and graphical languages, similar to SQL and QBE, have been proposed for relational model banks, $[28,32]$ . However, most advances in model base processing, including the design of user interfaces, requires that some intelligence be incorporated in a model management system. This is examined below.

## 3. Model base processing

Systems have been constructed for model base processing, in which the emphasis is on model sequencing and the relationship between model components $[44,48,100,140]$ . However, it has recently been suggested that the field of artificial intelligence may make substantial contributions to this area $[66,91,119,137,166]$ , and the resulting systems have sometimes been called “expert modelbase systems” $[15,21]$ , by comparison with the more established field of expert database systems. we examine four tasks performed by these systems: (1) interfacing models with users; (2) integrating models or components of models with each other; (3) constructing models or components of models; and (4) interpreting model outputs.

User interfaces with models have traditionally consisted of command line and iconic input and printed and graphical output, but they have also begun to include natural language front ends that emphasize user-oriented rather than system-oriented dialogue $[31]$ . Systems have been developed for such communication in the domains of queuing simulation $[83]$ , linear programming $[79]$ , and static simulation $[23,25]$ . Systems have also been developed to facilitate communication between users and both models and their supporting data file in the domains of both linear programming $[57,73,156]$ and simulation $[118,130,135]$ . More generally, some systems allow users to communicate not only with models and files, but also with each other $[3,94,132,168]$ , and this may lead to an integration of model management and group decision support systems $[115,145]$ . In addition, consideration has been given to the development of user-friendly model documentation systems as a way of facilitating model usage [133].

The second task, model integration, consists of identifying and properly combining models and other DSS components (such as data files and data analysis procedures) needed to respond to a specific query. This may require the use of intelligent software, since integration may be viewed as inferring a query schema from a set of information schemas $[38]$ . Intelligent systems have been developed for this purpose based on logic programming $[36,107,114]$ , connection graphs $[49]$ , AND/OR graphs $[154]$ , heuristic search $[93,116,117]$ , rules $[19]$ , semantic nets $[65]$ , frames $[60]$ , and connection graphs combined with frames $[70]$ . Some of these ideas have been extended to the integration of distributed model bases $[139]$ .

In the third area, intelligent systems have been developed both for selecting a model from a set of existing models to solve a specific problem $[8,93]$ and for constructing models when no existing model is appropriate to the task at hand $[90]$ . These systems have been specialized to certain problem domains. For example, systems have been designed or developed for selecting an appropriate statistical technique $[4,125]$ , a forecasting model $[104,120,132]$ , or an econometric model $[55]$ , and for constructing linear programming models by means of logic programming $[11,30,101,102,141]$ , frames $[12,13]$ , hierarchies $[43]$ , decision trees $[157,158]$ , and semantic nets $[174]$ . Protocols have been taken of persons formulating linear programming models $[158]$ , and consideration has been given to the use of case-based reasoning in the construction of such models $[113]$ . This work has been extended to include integer programming $[175]$ and multi-criteria optimization $[86]$ . More generally, systems have been developed for verifying model correctness $[152]$ , controlling redundancy in model bases $[147]$ , and supplementing linguistic interfaces with graphical interfaces $[121,122]$ .

The-fourth area is interpretation of model outputs. One such system, REX, helps users to perform least squares regression by uncovering anomalies and suggesting variable transformations that will eliminate them $[72]$ . Another system, ERGO, helps users to interpret anomalies in the output of spreadsheet models $[92,98,99,172]$ . In the domain of linear programming, the discipline of computer assisted analysis is concerned with the analysis of model structures [81,82], and this has lead to ANALYZE, a system that helps users to uncover the causes of anomalies in outputs [79,80].

The application of artificial intelligence to model base processing — that is, to interfacing, integration, construction, and interpretation — has been extended to cover additional sources of information, including the environment of the organization [67], the decision processes of individual managers [46,47], the interactions between managers [14,45], and the messaging systems within organizations [53,124]. This suggests a relationship between research in intelligent systems and the view that organizations may be considered purposeful, adaptive, and intelligent entities. We now examine this more general view.

## 4. The organizational environment

During the past 5–10 years researchers in computer science, management science, and the social sciences have begun to explore the proposition that human organizations may be considered intelligent systems and that concepts from cognitive science and artificial intelligence can be useful in modeling certain facets of their behavior [20,127,170,173]. This stems from and may contribute to research on organizational learning [52,112,155], on the contribution of information systems to organizational learning [51,109], on the impact of information processing technology on organization behavior [89,146], and on the relationship between information processing in living organisms and in human organizations [71].

The intelligence of human systems has been modeled in several areas. Intelligent models have been constructed for government bureaucracies $[10]$ , foreign policy decision making $[2,162–164]$ , social systems $[7,66]$ , monetary systems $[126]$ , auctions, $[84,134]$ , markets $[106,108]$ , production economies $[103]$ , logistical systems $[149,150]$ , and primitive economies $[61]$ . In addition, the garbage can model of organizational choice has been cast into a heuristic search $[128]$ and a connectionist $[169]$ framework, and several contingency theories of organizations have been modeled as sets of IF/THEN rules and combined in a rule-based expert system $[6]$ .

The view that organizations and other human systems possess intelligence may provide guidance in the analysis of model management systems. The view that organizations are intelligent entities suggests that model management systems should contribute to their intelligence, even in those cases in which the model management systems are not themselves intelligent. A unifying principle for the examination of model management systems and human organizations to be examined in a common framework is the physical symbol hypothesis, which states that “... physical symbol systems have the necessary and sufficient means for general intelligent action” [144, p. 116]. Physical symbol systems which consist of symbols, symbol structures (i.e., expressions), and transformations from one set of structures to another form the basis for most cognitive models of human intelligence [142,143]. Since human organizations possess a rich symbolic content [78,138], it seems reasonable to view human organizations as physical symbol systems to which the physical symbol hypothesis applies [16,35]. One objection to this point of view is that it defines intelligence too narrowly, in terms of puzzle-solving or problem-solving, and not in terms of intuitive experience-based behavior [62]. An alternative, which has arisen from robotics research, is the physical grounding hypothesis, which states that “... to build a system that is intelligent it is necessary to have its representations grounded in the physical world” [42, p. 5].

## 5. Conclusion

The diversity of ideas in this paper mirrors the diversity of ideas in model management and the variety of research opportunities in this field. We began by examining model management as an extension of data management, which was the dominant point of view when research in this area began. However, the increasing emphasis on intelligent DSS that has taken place in the past ten years has also become a part of model management and has offered many opportunities for research. Finally, the view that intelligence is a property of model management systems and also of the organizations in which they are found suggests that there may be interesting relationships between two types of systems: those in which the information sources are decision models and those in which the information sources are decision makers. The investigation of these relationships may' also be a fruitful area of research.

## Acknowledgements

This work was supported by the Dean's Fund for Faculty Research of the Owen Graduate School of Management of Vanderbilt University.

## References

[1] B.-h. Ahn, and W.W. Hogan, On Convergence of the PIES Algorithm for Computing Equilibria, Operations Research 30, No. 2 (March–April 1982) pp. 281–300.

[2] P.A. Anderson, and S.J. Thorson, Artificial Intelligence Based Simulations of Foreign Policy Decision Making, Behavioral Science 25, No. 2 (April 1982) pp. 176–193.

[3] L.M. Applegate, B.R. Konsynski, and J.F. Nunamaker, Model Management Systems: Design for Decision Support, Decision Support Systems 2, No. 1 (March 1986) pp. 81–91.

[4] S. Athey, “A Consultant to Assist Students in Solving Statistics Problems, Proceedings of the Twenty-Second Annual Hawaii International Conference on System Sciences III: Decision Support and Knowledge Based Systems Track (January 1989) pp. 439–448.

[5] A.A. Baldwin, D. Baldwin, and T.K. Sen, The Evolution and Problems of Model Management Research, Omega, 19, No. 6, (1991) pp. 511–528.

[6] H.H. Baligh, R.M. Burton, and B. Obel, Designing Organization Structures: An Expert System Method, in: Economics and Artificial Intelligence, ed. by Jean-Louis Roos (Pergamon Press, Oxford, 1985) pp. 177–181.

[7] Sanjoy Banerjee, Reproduction of Social Structures: An Artificial Intelligence Model, Journal of Conflict Resolution 30, No. 2, (June 1986) pp. 221–252.

[8] Snehamay Banerjee, and A. Basu, A Knowledge Based Framework for Selecting Management Science Models, Proceedings of the Twenty-Third Annual Hawaii International Conference on System Sciences III: Decision Support and Knowledge Based Systems Track (January 1990) pp. 484–493.

[9] A. Basu, and R.W. Blanning, Enterprise Modeling Using Metagraphs, Working Paper 91-27, Owen Graduate School of Management, Vanderbilt University (1991).

[10] J. Bendor, and T.M. Moe, An Adaptive Model of Bureaucratic Politics, American Political Science Review 79, No. 3 (September 1985) pp. 755–774.

[11] H.K. Bhargava, and R. Krishnan, A Formal Approach for Model Formulation in a Model Management System. Proceedings of the Twenty-Third Annual Hawaii International Conference on System Sciences III: Deci

sion Support and Knowledge Based Systems -Track (January 1990) pp. 453–462.

[12] M. Binbasioglu, and M. Jarke, Domain Specific DSS Tools for Knowledge-Based Model Building, Decision Support Systems 2, No. 3 (September 1986) pp. 213–223.

[13] M. Binbasioglu, and M. Jarke, Knowledge-Based Formulation of Linear Programming Models, in: Expert Systems and Artificial Intelligence in Decision Support Systems, ed. by Henk G. Sol, Cees A.Th. Takkenberg, and Pieter F. De Vries Robbe, D. Reidel (Dordrecht, 1987) pp. 113–136.

[14] R.W. Blanning, Organization Design as Expert System Design, Proceedings of the Twenty-Fourth Annual Hawaii International Conference on System Sciences IV: Organizational Systems and Technology Track, (January 1991) pp. 3–12.

[15] R.W. Blanning, Expert Systems for Managers: Design Issues, in: Concise Encyclopedia of Information Processing in Systems & Organizations, ed. by Andrew P. Sage (Pergamon Press, Oxford, 1990). pp. 167–174.

[16] R.W. Blanning, Knowledge, Metaknowledge, and Explanation in Intelligent Organizational Models, presented at the International Workshop on Artificial Intelligence in Organization and Management Theory, Amsterdam, June 1990. (Proceedings to be published, ed. by Michael Masuch and Massimo Warglien.)

[17] R.W. Blanning, Model Management Systems, Chapter 11 of Decision Support Systems: Putting Theory into Practice, (2nd ed.), ed. by Ralph H. Sprague, Jr. and Hugh J. Watson, (Prentice-Hall, Englewood Cliffs, 1989) pp. 156–169.

[18] R.W. Blanning, A Relational Theory of Model Management, Chapter 2 of Decision Support Systems: Theory and Application, ed. by Clyde W. Holsapple and Andrew B. Whinston (Springer–Verlag, Berlin, 1987) pp. 19–53.

[19] R.W. Blanning, The Application of Metaknowledge to Information Management, Human Systems Management. 7, No. 1 (1987) pp. 49–57.

[20] R.W. Blanning, Expert Systems as an Organizational Paradigm, Proceedings of the Eighth International Conference on Information Systems (December 1987) pp. 232–240.

[21] R.W. Blanning, A Framework for Expert Modelbase Systems. Proceedings of the National Computer Conference (June 1987) pp. 13–17.

[22] R.W. Blanning, A Relational Framework for Information Management, in Decision Support Systems: A Decade in Perspective, ed. by Ephraim R. McLean and Henk G. Sol (North-Holland, Amsterdam, 1986) pp. 25-40.

[23] R.W. Blanning, A System for Natural Language Communication Between a Decision Model and its Users, in: Artificial Intelligence in Economics and Management, ed. by L.F. Pau (North-Holland, Amsterdam, 1986) pp. 77–85.

[24] R.W. Blanning, An Entity-Relationship Approach to Model Management, Decision Support Systems 2, No. 1 (March 1986) pp. 64–72.

[25] R.W. Blanning, A Framework for Structured/Natural Language Model Query Processing, Proceedings of the

Nineteenth Hawaii International Conference on System Sciences (January 1986) pp. 487–493.

[26] R.W. Blanning, The Existence and Uniqueness of Joins in Relational Model Banks, International Journal on Policy and Information 9, No. 1 (June 1985) pp. 73–95.

[27] R.W. Blanning, A Relational Framework for Join Implementation in Model Management Systems, Decision Support Systems 1, No. 1 (January 1985) pp. 69–82.

[28] R.W. Blanning, Language Design for Relational Model Management, in Management and Office Information Systems, ed., by S-K. Chang (Plenum, New York, 1984) pp. 217–235.

[29] R.W. Blanning, A Relational Framework for Model Bank Organization, Proceedings of the IEEE Workshop on Languages for Automation (November 1984) pp. 148–654.

[30] R.W. Blanning, A PROLOG-Based Framework for Model Management, Proceedings of the First International Workshop on Expert Database Systems (October 1984) pp. 633–642.

[31] R.W. Blanning, Conversing with Management Information Systems in Natural Language, Communications of the ACM 27, No. 3 (March 1984) pp. 201–207.

[32] R.W. Blanning, TQL: A Model Query Language Based on the Domain Relational Calculus, Proceedings of the IEEE Workshop on Language for Automation (November 1983) pp. 141–146.

[33] R.W. Blanning, Issues in the Design of Relational Model Management Systems, Proceedings of the National Computer Conference (June 1983) pp. 395–401.

[34] R.W. Blanning, Data Management and Model Management: A Relational Synthesis, Proceedings of the ACM Twentieth Annual Southeast Regional Conference (April 1982) pp. 139–147.

[35] R.W. Blanning, J.R. Marsden, D.E. Pingry, and A.C. Séror, Intelligent Models of Economic and Social Systems, in: Cybernetics and Applied Systems, ed. by Constantin V. Negoita (Marcel Dekker, New York, 1992) pp. 163–171.

[36] R.H. Bonczek, C.W. Holsapple, and A.B. Whinston, Specification of Modeling Knowledge in Decision Support Systems, in Processes and Tools for Decision Support, ed. by Henk G. Sol (North-Holland, Amsterdam) 1983, pp. 65–78.

[37] R.H. Bonczek, C.W. Holsapple, and A.B. Whinston, The Evolution from MIS to DSS: Extension of Data Management to Model Management, in Decision Support Systems, ed. by Michael J. Ginzberg, Walter Reitman, and Edward A. Stohr (North-Holland, Amsterdam, 1982) pp. 61–78.

[38] R.A. Bonczek, C.W. Holsapple, and A.B. Whinston, Foundations of Decision Support Systems, (Academic Press, New York, 1981).

[39] R. Bonczek, C. Holsapple, and A. Whinston, Mathematical Programming Within the Context of a Generalized Data Base Management System, R.A.I.R.O. Recherche Opérationelle / Operations Research 12, No. 2 (May 1978) pp. 117–139.

[40] R.H. Bonczek, C.W. Holsapple, and A.B. Whinston, Data Base Management Techniques for Mathematical Programming, Proceedings of the SIGMAP Bicentennial

Conference on Mathematical Programming (November 1976).

[41] G.H. Bradley, and R.D. Clemence, Jr., Model Integration with a Typed Executable Modeling Language, Proceedings of the Twenty-First Annual Hawaii International Conference on System Sciences III: Decision Support and Knowledge Based Systems Track (January 1988) pp. 403–410.

[42] R.A. Brooks, Elephants Don't Play Chess, Robotics and Autonomous Systems 8 (1990) pp. 3–15.

[43] C.E. Brown, and T.G. Lewis, HELM: Hierarchical Environment for Linear Modeling (Part 1: The Schema), Proceedings of the Twenty-Second Annual Hawaii International Conference on System Sciences III: Decision Support and Knowledge Based Systems Track (January 1989) pp. 440–458.

[44] M.I. Bu-Hulaiga, and H.K. Jain, An Interactive Plan-Based Procedure for Model Integration in DSS, Proceedings of the Twenty-First Annual Hawaii International Conference on System Sciences III: Decision Support and Knowledge Based Systems Track (January 1988) pp. 428–434.

[45] K.M.C. Carley, Coordinating for Success: Trading Information Redundancy for Task Simplicity, Proceedings of the Twenty-Third Annual Hawaii International Conference on Systems Sciences IV: Emerging Technologies and Applications Track (January 1990) pp. 261–270.

[46] D.A. Carlson, and S. Ram, Hyperintelligence: The Next Frontier, Communications of the ACM4l 33, No. 3 (March 1990) pp. 311–321.

[47] D.A. Carlson, and S. Ram, Modeling Organizations as a Social Network of Distributed Knowledge-Based Systems, Proceedings of the Twenty-Third Annual Hawaii International Conference on Systems Sciences IV: Emerging Technologies and Applications Track (January 1990) pp. 271–280.

[48] S. Chari, and R. Krishnan Towards a Logical Reconstruction of Structured Models, Proceedings of the Twenty-Third Annual Hawaii International Conference on System Sciences III: Decision Support and Knowledge Based Systems Track (January 1990) pp. 524–543.

[49] M.C. Chen, J.E. Fedorowicz, and L.J. Henschen, Deductive Processes in Databases and Decision Support Systems, Proceedings of the North Central ACM 82 Conference (1982) pp. 81–100.

[50] P.P.-S. Chen, The Entity-Relationship Model-Toward a Unified View of Data, ACM Transactions on Data Base Systems 1, No. 1 (March 1976) pp. 9–36.

[51] C. Ching, C.W. Holsapple, and A.B. Whinston, Concurrent Problem Solving and Organizational Learning, Proceedings of the Twenty-Second Annual Hawaii International Conference on System Sciences, III: Decision Support and Knowledge Based Systems Track (January 1989) pp. 483–491.

[52] M.D. Cohen, and L.S. Sproull, (eds.) Organization Science, Special Issue on Organizational Learning 2, No. 1 (February 1991).

[53] M.E. Culnan, Transaction Processing Applications as Organizational Message Systems: Implications for the Intelligent Organization, Proceedings of the Twenty-Second Annual Hawaii International Conference on system

Sciences III, Decision Support and Knowledge Based Systems Track (January 1989j pp. 525–531.

[54] M.A.H. Dempster, and A.M. Ireland, Object-Oriented Model Integration in MIDAS, Proceedings of the Twenty-Second Annual Hawaii International Conference on System Sciences, III: Decision Support and Knowledge Based Systems Track (January 1989) 612–620.

[55] D.R. Dolk, and D.J. Kridel, Toward a Symbiotic Expert System for Econometric Modeling, Proceedings of the Twenty-Second Annual Hawaii International Conference on System Sciences, III: Decision Support and Knowledge Based Systems Track (January 1989) pp. 3–13.

[56] D.R. Dolk, Model Management and Structured Modeling: The Role of an Information Resource Dictionary System, Communications of the ACM 31, No. 6 (June 1988) pp. 704–718.

[57] D.R. Dolk, A Generalized Model Management System for Mathematical Programming, ACM Transactions on Mathematical Software 12, No. 2 (June 1986) pp. 92–126.

[58] D.R. Dolk, Data as Models: An Approach to Implementing Model Management, Decision Support Systems 2, No. 1 (March 1986) pp. 73–80.

[59] D.R. Dolk, and B.R. Konsynski. Model Management in Organizations, Information and Management. 9, No. 1 (August 1985) pp. 35–47.

[60] D.R. Dolk, and B.R. Konsynski, Knowledge Representation for Model Management Systems, IEEE Transactions on Software Engineering, SE-1O, No. 6 (November 1984) pp. 619–628.

[61] J. Doran, Distributed Artificial Intelligence and the Modeling of Socio-Cultural Systems, in: Intelligent Systems in a Human Context, ed. by Linda A. Murray and John T.E. Richardson (Oxford University Press, Oxford, 1989) pp. 71–91.

[62] H.L. Dreyfus, and S.E. Dreyfus. Mind Over Machine: The Power of Human Intuition and Expertise in the Era of the Computer (The Free Press, New York, 1986).

[63] A. Dutta, and A. Basu, An Artificial Intelligence Approach to Model Management in Decision Support Systems, IEEE Computer 17, No. 9 (September 1984) pp. 89–97.

[64] R.D. Eck, A. Philippakis, and R. Ramirez, Solver Representation for Model Management Systems, Proceedings of the Twenty-Third Annual Hawaii International Conference on System Sciences, III: Decision Support and Knowledge Based Systems Track (January 1990) pp. 474–483.

[65] J.J. Elam, J.C. Henderson, and L.W. Miller, Model Management Systems: An Approach to Decision Support in Complex Organizations, Proceedings of the First International Conference on Information Systems (December 1980) pp. 98–110.

[66] J.J. Elam, and B. Konsynski, Using Artificial Intelligence Techniques to Enhance the Capabilities of Model Management Systems, Decision Sciences, 18, No. 3 (Summer 1987) pp. 487–502.

[67] G. Elofson, and B. Konsynski, Delegation Technologies: Environmental Scanning with Intelligent Agents, Journal of Management Information Systems 8, No. 1 (Summer 1991) pp. 37–62.

[68] R. Ennals. Artificial Intelligence: Applications to Logical

Reasoning and Historical Research (Ellis Horwood, Chichester, 1985).

[69] G.T. Fadok, Effective Design of CODASYL Data Base (Macmillan, New York, 1985).

[70] J. Fedorowicz, and G.D. Williams, Representing Modeling Knowledge in an Intelligent Decision Support System, Decision Support Systems 2, No. 1 (March 1986) pp. 3–14.

[71] M.S. Fox. An Organizational View of Distributed Systems, IEEE Transactions on Systems, Man, and Cybernetics SMC-11, No. 1 (January 1981) pp. 70–80.

[72] W.A. Gale, (ed.), Artificial Intelligence & Statistics (Addison-Wesley, Reading, 1986).

[73] A.M. Geoffrion, FW/SM: A Prototype Structured Modeling Environment, Working Paper 377, Western Management Science Institute, University of California, Los Angeles (May 1990).

[74] A.M. Geoffrion, A Taxonomy of Indexing Structures for Mathematical Programming Modeling Languages, Proceedings of the Twenty-Third Annual Hawaii International Conference on System Sciences, Ill: Decision Support and Knowledge Based Systems Track (January 1990) pp. 463–473.

[75] A.M. Geoffrion, The Formal Aspects of Structured Modeling, Operations Research 37, No. 1 (January-February 1989) pp. 30–51.

[76] A.M. Geoffrion, An Introduction to Structured Modeling, Management Science 33, No. 5 (May 1987) pp. 547–588.

[77] A.M. Geoffrion, Reusing Structured Models via Model Integration, Proceedings of the Twenty-Second Annual Hawaii International Conference on System Sciences III: Decision Support and Knowledge Based Systems Track (January 1989) pp. 601–611.

[78] D.A. Gioia, Symbols, Scripts, and Sensmaking, Chapter 2 of The Thinking Organization: Dynamics of Organizational Social Cognition, ed. by Henry P. Sims, Jr. (Dennis A. Gioia, and Associates, Jossey-Bass, San Francisco, 1986) pp. 4974.

[79] H.J. Greenberg, A Natural Language Discourse Model to Explain Linear Programming Models and Solutions, Decision Support Systems 3, No. 4 (December 1987) pp. 333–342.

[80] H.J. Greenberg, A Functional Description of ANALYZE: A Computer Assisted Analysis System for Linear Programming Models, ACM Transactions on Mathematical Software 9, No. 1 (March 1983) pp. 18–56.

[81] H.J. Greenberg, A Tutorial on Computer-Assisted Analysis, in: Advanced Techniques in the Practice of Operations Research, ed. by Harvey J. Greenberg, Frederick H. Murphy, and Susan H. Shaw (North-Holland, New York, 1982) pp. 212–249.

[82] H.J. Greenberg, and J.S. Maybee, Computer-Assisted Analysis and Model Simplification (Academic Press, New York, 1981).

[83] G.E. Heidorn, Simulation Programming Through Natural Language Dialogue, in: Logistics, ed. by Murray A. Geisler (North-Holland, Amsterdam, 1975) pp. 71–83.

[84] E. Hoffman, V.S. Jacob, J.S. Marsden, and A. Whinston, Artificial Intelligence in Economics—Expert Systems Modelling of Microeconomic Issues, in: Artificial

Intelligence in Economics and Management, ed. by L.F. Pau (North-Holland, Amsterdam, 1986) pp. 1–9.

[85] W.W. Hogan, Energy Policy Models for Project Independence, Computers and Operations Research 2, No. 3/4 (December 1975) pp. 251–171.

[86] I. Hong, and D.R. Vogel, Data and Model Management in Generalized MCDM-DSS, Decision Sciences, 22, no. 1 (Winter 1991). pp. 1–25.

[87] S.N. Hong, M.V. Mannino, and B.S. Greenberg, Inheritance and Instantiation in Model Management, Proceedings of the Twenty-Third Annual Hawaii International Conference on System Sciences, III: Decision Support and Knowledge Based Systems Track (January 1990) pp. 424–432.

[88] W.C. House, (ed.) Decision Support Systems: A Data-Based Model-Oriented. User-Developed Discipline (Petrocelli, New York, 1983).

[89] G.P. Huber, A Theory of the Effects of Advanced Information Technologies on Organization Design, Intelligence, and Decision Making, Academy of Management Review 15, No. 1 (January 1990) pp. 41–71.

[90] S. Hwang, Automatic Model Building Systems: A Survey, DSS-85 Transactions (April 1985) pp. 22–32.

[91] M. Jarke, and F.J. Radermacher, The AI Potential of Model Management and Its Central Role in Decision Support, Decision Support Systems 4, No. 4 (December 1988) pp. 387–404.

[92] D. King, The ERGO Project: A Natural Language Query Facility for Explaining Financial Results, DDS-86 Transactions (April 1986) pp. 131–150.

[93] G. Klein, Developing Model Strings for Model Managers, Journal of Management Information Systems III, No. 2 (Fall 1986) pp. 94–110.

[94] G. Klein, B. Konsynski, and P.O. Beck, A Linear Representation for Model Management in DSS, Journal of Management Information Systems II, No. 2 (Fall 1985) pp. 40–54.

[95] B.R. Konsynski, Model Management in Decision Support Systems, in Data Base Management: Theory and Applications, ed., by Clyde W. Holsapple and Andrew B. Whinston (D. Reidel, Dordrecht, 1983) pp. 131–154.

[96] B.R. Konsynski, On the Structure of a Generalized Model Management System, Proceedings of the Fourteenth Hawaii International Conference on System Sciences, 1 (January 1980) pp. 630–638.

[97] B.R. Konsynski, J.E. Kottemann, J.F. Nunamaker, and J.W. Stott, PLEXSYS-84: An Integrated Development Environment for Information Systems, Journal of Management Information Systems I, No. 3 (Winter 1984–85) pp. 64104.

[98] D.W. Kosy, and B.P. Wise, Overview of ROME: A Reason-Oriented Modeling Environment, in: Artificial Intelligence in Economics and Management, ed. by L. F. Pau (North-Holland, Amsterdam, 1986) pp. 21-30.

[99] D.W. Kosy, and B.P. Wise, Self-Explanatory Financial Planning Models, Proceedings of the National Conference on Artificial Intelligence (August 1984) pp. 176–181.

[100] J. Kottemann, and D.R. Dolk, Process-Oriented Model Integration, Proceedings of the Twenty-First Annual Hawaii International Conference on System Sciences, III:

Decision Support and Knowledge Based Systems Track (January 1988) pp. 396–402.

[101] R. Krishnan, A Logic Modeling Language for Automated Model Construction, Decision Support Systems 6, No. 2 (May 1990) pp. 123–152.

[102] R. Krishnan, PDM: A Knowledge-Based Tool for Model Construction, Proceedings of the Twenty-Second Annual Hawaii Conference on System Sciences, III: Decision Support and Knowledge Based Systems Track (January 1989) pp. 467–474.

[103] R. Krishnan, D.A. Kendrick, and R.M. Lee, A Knowledge-Based System for Production and Distribution Economies, Computer Science in Economics and Management 1, No. 1 (1988) pp. 53–72.

[104] S. Kumar, and C. Hsu, An Expert System Framework for Forecasting Method Selection, Proceedings of the Twenty-First Annual Hawaii International Conference on System Sciences, III: Decision Support and Knowledge Based Systems Track (January 1988) pp. 86–95.

[105] R. Lazinny, A Deductive Approach for Problem Representation and Modeling Support: Conceptual Schema and Object-Oriented Models, Proceedings of the Twenty-Fourth Annual Hawaii International Conference on Systems Sciences, III: Decision Support and Knowledge Based Systems Track (January 1991) pp. 291–305.

[106] R.M. Lee, A Logic Model for Electronic Contracting, Decision Support Systems 4, No. 1 (March 1988) pp. 27–44.

[107] R.M. Lee, and L.W. Miller, A Logic Programming Framework for Planning and Simulation, Decision Support Systems 2, No. 1 (March 1986) pp. 15–25.

[108] R.M. Lee, and G.R. Widmeyer, Shopping in the Electronic Marketplace, Journal of Management Information Systems II, No. 4 (Spring 1986) pp. 21–35.

[109] S. Lee, and J.F. Courtney, Jr., Organizational Learning Systems, Proceedings of the Twenty-Second Annual Hawaii International Conference on System Sciences III: Decision Support and Knowledge Based Systems Track (January 1989) pp. 492–503.

[110] M.L. Lenard, An Object-Oriented Approach to Model Management, Proceedings of the Twentieth Annual Hawaii International Conference on System Sciences, I (January 1987) pp. 507–515.

[111] M. Lenard, Representing Models as Data, Journal of Management Information Systems II, No. 4 (Spring 1986) pp. 36–48.

[112] B. Levitt, and J.G. March, Organizational Learning, Annual Review of Sociology 14 (1988) pp. 319–340.

[113] T.-P. Liang, Modeling by Analogy: A Case-Based Approach to Linear Program Formulation, Proceedings of the Twenty-Fourth Annual Hawaii International Conference on System Sciences, III: Decision Support and Knowledge Based Systems Track (January 1991) pp. 276–283.

[114] T.-P. Liang, Development of a Knowledge-Based Model Management System, Operations Research 36, No. 6 (November–December 1988) pp. 849–863.

[115] T.-P. Liang, Model Management for Group Decision Support, MIS Quarterly 12, No. 4 (December 1988) pp. 667–680.

[116] T.-P. Liang, Reasoning in Model Management Systems, Proceedings of the Twenty-First Annual Hawaii International Conference on System Sciences III: Decision Support and Knowledge Based Systems Track (January 1988) pp. 461–470.

[117] T.-P. Liang, A Graph-Based Approach to Model Management, Proceedings of the Seventh International Conference on Information Systems (December 1986) pp. 136–151.

[118] T.-P. Liang, Integrating Model Management with Data Management in Decision Support Systems, Decision Support Systems 1, No. 3 (September 1985) pp. 221–232.

[119] J.I. Liu, D.Y.Y. Yun, and G. Klein, An Agent for Intelligent Model Management, Journal of Management Information Systems 7, No. 1 (Summer 1990) pp. 101-122.

[120] P.C.C. Luan, R.G. Ramirez, and R.D. St. Louis, Expert Systems that Satisfy Model-Solver-Data Independence, Proceedings of the Twenty-Third Annual Hawaii International Conference on System Sciences III: Decision Support and Knowledge Based Systems Track (January 1990) pp. 287–292.

[121] P.C. Ma, F.H. Murphy, and E.A. Stohr, Graphics Interface for Linear Programming, Communications of the ACM 32, No. 8 (August 1989) pp. 996–1012.

[122] P.C. Ma, F.H. Murphy, and E.A. Stohr, Semantic Structures in Linear Programs, Proceedings of the Twenty-Second Annual Hawaii International Conference on System Sciences III: Decision Support and Knowledge-Based Systems Track (January 1989) pp. 459–466.

[123] D. Maier, The Theory of Relational Databases (Computer Science Press, Rockville, 1983).

[124] T.W. Malone, K.R. Grant, F.A. Turbak, S.A. Brobst, and M.D. Cohen, Intelligent Information Sharing Systems, Communications of the ACM 30, No. 5 (May 1987) pp. 390–402.

[125] G.A. Marcoulides, An Expert System for Statistical Consulting, Proceedings of the 1987 Annual Meeting of the Decision Sciences Institute (November 19873 pp. 1182–1183.

[126] R. Marimon, E. McGrattan, and T.J. Sargent, Money as a Medium of Exchange in an Economy with Artificially Intelligent Agents, Working Papers in Economics E-89-28, Domestic Studies Program, Hoover Institution, Stanford University (August 1989).

[127] J.R. Marsden, and D.E. Pingry, The Intelligent Organization: Some Observations and Alternative Views, Proceedings of the Twenty-First Annual Hawaii International Conference on System Sciences III: Decision Support and Knowledge Based Systems Track (January 1988) pp. 19–24.

[128] M. Masuch, and P. LaPotin, Beyond Garbage Cans: An AI Model of Organizational Choice, Administrative Science Quarterly 34, No. 1 (March 1989) pp. 38–67.

[129] S.C. McIntyre, and L.F. Higgins, Object-Oriented Systems Analysis and Design: Methodology and Application, Journal of Management Information Systems 5, No. 1 (Summer 1988) pp. 25–35.

[130] S.C. McIntyre, B.R. Konsynski, and J.F. Nunamaker,

Jr., Automating Planning Environments: Knowledge Integration and Model Scripting, Journal of Management Information Systems II, No. 4 (Spring 1986) pp. 49–69.

[131] T.H. Merrett, Relational Information Systems (Reston Publishing Co., Reston, 1984).

[132] M. Milanese, A. Vicino, and P. Borodoni, Integration of Modeling and AI Techniques in KBDSS Generators: The EDIPUSS System, Information and Decision Technologies 17, No. 2 (1991) pp. 125–131.

[133] F. Mili, and F.A. Cjoch, Documenting Decision Models for Informed and Confident Decisions, Proceedings of the Twenty-Third Annual Hawaii International Conference on System Sciences III: Decision Support and Knowledge Based Systems Track (January 1990) pp. 494–503.

[134] R.M. Miller, On Distributing the Intelligence of Economic Processes, in Economics and Artificial Intelligence, ed. by Jean-Louis Roos (Pergamon Press, Oxford, 1987) pp. 161–162.

[135] L.W. Miller, and N. Katz, A Model Management System to Support Policy Analysis, Decision Support Systems 2, No. 1 (March 1986) pp. 55–63.

[136] R.P. Minch, and J.R. Burns, Conceptual Design of Decision Support Systems Containing Management Science Models, IEEE Transactions on Systems. Man. and Cybernetics SMC-13, No. 4 (July/August 1983) pp. 549–557.

[137] R.P. Minch, Hypermedia Knowledge Management for Intelligent Organizations, Proceedings of the Twenty-Third Annual Hawaii International Conference on Systems Sciences IV: Emerging Technologies and Applications Track, pp. 300–306.

[138] G. Morgan, P.J. Frost, and L.R. Pondy, Organizational Symbolism, in Organizational Symbolism, ed. by Louis R. Pondy, Peter J. Frost, Gareth Morgan, and Thomas Dandridge (JAI Press, Greenwich, 1983) pp. 3–35.

[139] W.A. Muhanna, Issues in Distributed Model Management Systems, Proceedings of the Eleventh International Conference on Information Systems (December 1990) pp. 231–242.

[140] W.A. Muhanna, and R.A. Pick, Composite Models in SYMMS, Proceedings of the Twenty-First Annual Hawaii International Conference on System Sciences III: Decision Support and Knowledge Based Systems Track (January 1988) pp. 418–427.

[141] F.H. Murphy, and E.A. Stohr, An Intelligent System for Formulating Linear Programs, Decision Support Systems 2, No. 1 (March 1986) pp. 39–47.

[142] A. Newell, Unified Theories of Cognition (Harvard University Press, Cambridge, 1990).

[143] A. Newell, Physical Symbol Systems, Cognitive Science 4, No. 2 (April–June 1980) pp. 135–183.

[144] A. Newell, and H.A. Simon, Computer Science as Empirical Inquiry: Symbols and Search, Communications of the ACM 19, No. 3 (March 1976) pp. 113–126.

[145] J.F. Nunamker, L.M. Applegate, and B.R. Konsynski, Computer-Aided Deliberation: Model Management and Group Decision Support, Operations Research 36, No. 6 (November–December 1988) pp. 826–848.

[146] W.J. Orlikowski, and D. Robey, Information Technology and the Structuring of Organizations, Information Systems Research 2, No. 2 (June 1991) pp. 143–169.

[147] L. Orman, Flexible Management of Computational Models, Decision Support Systems 2, No. 3 (September 1986) pp. 225–234.

[148] K.H. Palmer, N.K. Boudwin, H.A. Patton, A.J. Rowland, J.D. Sammes, and D.M. Smith, A Model Management Framework for Mathematical Programming (Wiley, New York, 1984).

[149] H. Van Dyke Parunak, J. Kindrick, and B. Irish, A Connectionist Model for Material Handling, Robotics & Computer Integrated Manufacturing 4, No. 3/4 (1988) pp. 643–654.

[150] H. Van Dyke Parunak, J. Kindrick, and B. Irish, Material Handling: A Conservative Domain for Neural Connectivity and Propagation, Proceedings of the Sixth National Conference on Artificial Intelligence 1 (July 1987) pp. 307–311.

[151] W.E. Pracht, and J.F. Courtney, A Visual User Interface for Capturing Mental Models in Model Management Systems, Proceedings of the Nineteenth Annual Hawaii International Conference on System Sciences II (January 1986) pp. 535–541.

[152] Y.Y. Reddy, The Role of Introspective simulation in Management Decision Making, DSS-85 Transactions (April 1985) pp. 18–21.

[153] J.G. Sanderson, A Relational Theory of Computing, Lecture Notes in Computer Science 82 (Springer-Verlag, Berlin, 1980).

[154] M.J. Shaw, P.-L. Tu, and P. De, Applying Machine Learning to Model Management in Decision Support Systems, Decision Support Systems 4, No. 3 (September 1988) pp. 285–305.

[155] P. Shrivastava, A Typology of Organizational Learning Systems, Journal of Management Studies 20, No. 1 (January 1983) pp. 7–28.

[156] I.S. Singh, and S. Sadagopan, A Support System for Optimization Modelling, Decision Support Systems 3, No. 2 (June 1987) pp. 165–178.

[157] M.M. Sklar, and R.A. Pick, A Knowledge Engineered Linear Programming Formulation Assistant, Proceedings of the Twenty-Third Annual Hawaii International Conference on System Sciences III: Decision Support and Knowledge Based Systems Track (January 1990) pp. 269–278.

[158] M.M. Sklar, R.A. Pick, G.B. Vesprani, and J.R. Evans, Eliciting Knowledge Representation Schema for Linear Programming Formulation, in Operations Research and Artificial Intelligence: The Integration of Problem Solving Strategies, ed., by Donald E. Brown and Chelsea C. White, III (Kluwer, Norwell, 1990) pp. 279–613.

[159] R.H. Sprague, Jr., and E.D. Carlson, Building Effective Decision Support Systems (Prentice-Hall, Englewood Cliffs, 1982).

[160] R.H. Sprague, Jr., and H.J. Watson, Model Management in MIS, Proceedings of the Seventeenth National AIDS (November 1975) pp. 213–215.

[161] E.A. Stohr, and M.R. Tanniru, A Database for Operations Research Models, International Journal of Policy Analysis and Information Systems 4, No. 1 (1980) pp. 105–121.

[162] D.A. Sylvan, Supplementing Global Models with Computational Models: An Assessment and an Energy Example, Behavioral Science 32, No. 3 (July 1987) pp. 212–231.

[163] D.A. Sylvan, A. Goel, and B. Chandrasekaran, Analyzing Political Decision Making from an Information Process Perspective: JESSE, American Journal of Political Science 34, No. 1 (February 1990) pp. 74–123.

[164] S.J. Thorson, Intentional Inferencing in Foreign Policy: An AI Approach, in: Foreign Policy Decision Making: Perception. Cognition, and Artificial Intelligence, ed. by Donald A. Sylvan and Steve Chan (Praeger, New York, 1984) pp. 280–309.

[165] L. Tung, R.G. Ramariz, and R.D. St. Louis, Model Integration in an Object-Oriented Model Management System, Proceedings of the Twenty-Fourth Annual Hawaii International Conference on Systems Sciences III: Decision Support and Knowledge Based Systems Track (January 1991) pp. 284–290.

[166] K. van Hee, and A. Lapinsky, OR and AI Approaches to Decision Support Systems, Decision Support Systems 4, No. 4 (December 1988) pp. 447–459.

[167] K.M. van Hee, L.J. Somers, and M. Voorhoeve, A Modeling Environment for Decision Support Systems, Decision Support Systems 7, No. 3 (August 1991) pp. 241–251.

[168] M.S.-Y. Wang, and J.F. Courtney, Jr., A Conceptual Architecture for Generalized Decision Support System Software, IEEE Transactions on systems. Man, and Cybernetics SMC-14, No. 5 (September/October 1984) pp. 701–711.

[169] M. Warglien, Learning by Choosing in a Garbage Can Situation: A Connectionist Approach (Centre de Sociologie des Organisations, Paris, October 1988).

[170] E.S. Weber, Y.I. Liou, M. Chen, and J.F. Nunamaker, Jr., Toward More Intelligent Organizations, Proceedings of the Twenty-Third Annual Hawaii International Conference on System Sciences IV: Emerging Technologies and Applications Track (January 1990) pp. 290–299.

[171] H.J. Will, Model Management Systems, in Information Systems and Organization Structure, ed. by Edwin Grochia and Norbert Szyperski (Walter de Gruyter, Berlin, 1975) pp. 468–482.

[172] B.P. Wise, and D.W. Kosy, Model-Based Evaluation of Long-Range Resource Allocation Plans, in: Artificial Intelligence in Economics and Management, ed. by L.F. Pau (North-Holland, Amsterdam, 1986) pp. 93–102.

[173] S. Woolgar, Why Not a Sociology of Machines? An Evaluation of Prospects for an Association Between Sociology and Artificial Intelligence, in: Intelligent Systems in a Human Context, ed. by Linda A. Murray and John T.E. Richardson, (Oxford University Press, Oxford, 1989) pp. 53–70.

[174] S.B. Yadav, and D.R. Chand, An Expert Modeling Support System for Modeling an Object to Specify its Information Requirements, Decision Support Systems 5, No. 1 (March 1989) pp. 29–45.

[175] F. Zahed, A Knowledge Base for Integer Programming —A Meta-OR Approach, in Operations Research and Artificial Intelligence: The Integration of Problem Solving Strategies, ed. by Donald E. Brown and Chelsea C. White, III (Kluwer, Norwell, 1990) pp. 317–367.
