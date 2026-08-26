---
otero_id: 18096
otero_key: "YPGVDDNW"
title: "Management applications of expert systems"
authors: "Robert W. Blanning"
year: "1984"
journal: "Information & Management"
doi: "10.1016/0378-7206(84)90026-0"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Management Applications of Expert Systems

Robert W. Blanning

Owen Graduate School of Management, Vanderbilt University, Nashville, TN 37203, USA

The development of expert systems for such professionals as doctors diagnosing and treating infectious diseases and geologists exploring for mineral deposits has led to suggestions that expert systems be developed for managers in public and private organizations who make manufacturing, marketing, financial, personnel, and other decisions. This paper describes briefly some of the systems of this type that have already been developed, with an emphasis on the logic expressions used in them, examines other fruitful areas for system development, and identifies software requirements for the implementation of such systems.

Keywords: Expert Systems, Knowledge-Based Systems, Heuristic Rules, Resource Allocation, Problem Diagnosis, Scheduling, Assignment, Decision Models.

![](/api/attachments/YPGVDDNW/fulltext/images/83049575517f5e9fcc3adf486554e36e343c14a35b8695180182bc6bec27dc3a.jpg)

Robert W. Blanning is Associate Professor of Management at the Owen Graduate School of Management at Vanderbilt University. He received a B.S. in Physics from the Pennsylvania State University, an M.S. in Operations Research from the Case Institute of Technology, and a Ph.D. from the University of Pennsylvania, specializing in operations research and management information systems. He has been a member of the faculty of the Schools of Business at New York

University and the Wharton School at the University of Pennsylvania. His principal research and teaching interests are in model management systems and the applications of artificial intelligence to decision support systems.

## 1. Introduction

The application of artificial intelligence techniques to the development of expert systems for established professionals, such as doctors diagnosing and treating infectious diseases and geologists exploring for mineral deposits, has led to the suggestion that expert systems be developed to help managers in organizations make better decisions. An expert system for managers (herein denoted ESM) is defined here as a system that captures the specialized knowledge that managers bring to bear on the decision-making tasks they perform, and it uses this knowledge to diagnose potential or actual problems, make recommendations, and offer explanations of its diagnoses and recommendations. Several ESMs have been implemented and are described below.

There are two principal differences between managers and the other people for whom expert systems have been developed (e.g., doctors, geologists). The first is that management problems appear to be less structured than many of the other types of problems which have led to the development of expert systems; for although some management problems such as production scheduling are relatively well structured, there are many other problems, like setting an advertising budget for a new product or deciding whether to attempt to penetrate a new market, where the goals, the possible actions of managers, and the relationship between management decisions and their consequences are not easily made explicit. Attempts have been made to identify a consistent framework for solving problems of this type [23], but they have not yet met with sufficient success to allow solution of a broad variety of management problems. Thus, various ESMs differ substantially from each other, which may create problems in knowledge acquisition and in the transfer of technology from one domain to another.

The second difference concerns the managers' environment. A large number of computer-based decision aids have been designed and implemented to assist line managers and staff analysts in decision making. These systems are generally called decision support systems; they provide convenient access to decision models, such as models of the production or distribution system, the market, or the financial structure of a firm. Such model-based systems differ from expert systems in that the models they contain are causal models (ones of systems that the managers are trying to influence or control, such as a market) rather than judgemental models. However, it is likely that the designers of ESMs will have to recognize the existence of such models and to provide interfaces between them and the ESMs.

To understand how these two characteristics might affect the design, we begin by examining three categories of ESM.

## 2. Existing and Possible ESMs

The first category of ESMs deal with the allocation of resources – especially financial resources – to projects, departments or investments. The second is for diagnosing problems that have symptoms which appear in management reports (e.g., the firm's financial reports). The third is for scheduling (e.g., production or distribution) and assignment of resources (e.g., of personnel).

## 2.1. Resource Allocation

One of the earliest expert systems simulated a trust officer in a bank preparing a portfolio for a bank client $[10]$ . Its input was a set of financial statistics for a variety of stocks, information about the economy, and certain characteristics of the client, and its output was a recommended portfolio. The system was based on protocols obtained from a bank trust officer and contained heuristics that he had found useful. More recently, Davis $[12]$ illustrated TEIRESIAS (a system for building and maintaining expert systems) with a simple financial example. It contains rules and associated certainty factors of the form:

\- “If the area of the investment is not known, the desired return on the investment is greater than 10%, and the time scale of the investment is long-term, then AT&T is a likely (0.4) choice for the investment."

\- “If the time scale of the investment is long-term, the desired return on investment is greater than 10%, and the risk class of the investment is speculative, then there is evidence (0.6) that the investment should be high-technology.”

These rules and certainty factors are combined to determine an investment strategy appropriate to the objectives of the investor. Although the example was only illustrative, it appears that similar systems could be developed to capture the expert judgement of portfolio managers.

Because resource allocation is an important managerial function, ESMs will probably be developed to support other types of resource allocation decisions – for example, the allocation of a research and development budget to proposed projects, the preparation of a governmental agency budget (i.e., the allocation of funds to government departments), and the preparation of a capital budget for a firm. However, it may be necessary to integrate these ESMs with some of the computer-based planning systems now being used for investment analysis. A number of corporations are using commercially available planning languages – such as EMPIRE, IFPS and SIMPLAN – to simulate their financial and operating structures [24]. The inputs to the simulations are proposed investment or other possible alternatives, and the outputs are pro-forma financial and operating statements describing the likely consequences of the actions. Planning languages are based on higher-order programming languages (usually FORTRAN), but they also contain:

1. Input generators that make it easy to perform sesntivity analyses;

2. Report writers that make it easy to format pro-forma reports that are similar to the post-hoc financial and operating statements used by the company;

3. Subprograms that perform financial and statistical calculations often used in the simulations. In addition, certain constrained optimization techniques (collectively called mathematical programming) are sometimes used in resource allocation. Thus, it will be necessary to utilize planning models and mathematical programming packages in some ESMs.

An example with some of these characteristics is DECMAK, a tree-structured system in which rules are used at each level to give variable values at the next level [3]. Suppose a three-level tree for evaluating a computer system contains the rules:

\- “If SECURITY is high and COMFORT is very good, then TECHNICAL-CHARACTERISTICS are very good.”

\- “If ECONOMIC-CHARACTERISTICIS are acceptable, TECHNICAL CHARACTERISTICIS are good, and PERSONNEL-CHARACTERISTICS are acceptable, then SYSTEM is acceptable.”

DECMAK provides the user with an evaluation of various investment alternatives, with an explanation of how they were computed. Limited features are also available for snesitivity analysis and report generation.

Systems of this type might be extended to include environmental considerations, such as laws, contractual requirements, government regulations, and accounting rules, and these might be described by logic expressions. Sergot [28] suggests that laws and regulations may be analyzed by logic programming, and Gardner [17] reports progress on a rule-guided system for analyzing legal problems. Thus, it should be possible to develop ESMs that contain a comprehensive description of the knowledge needed to support a variety of resource allocation decisions.

## 2.2. Prpoblem Diagnosis

One important function of management is the anticipation of potential problems, such as an incipient cost overrun or decline in customer satisfaction, with a view to correcting them before they get out of control. There are two principal sources used by managers to detect such problems: personal observation and discussion (i.e., plant tours and conversations with important customers) and management reports published periodically (monthly, quarterly, yearly) for performance evaluation (e.g., a budget variance report, which compares budgeted with actual revenues and expenses for the reporting period) where indicators of inchoate problems are often found [29].

An ESM that helps managers to detect and diagnose problems might contain rules of the following type (where a and b are parameters):

\- If the cost of raw materials is $X\%$ below budget and the cost of labor is $Y\%$ above budget, then there is evidence $(1 - \exp(-aX - bY))$ that substandard materials are being purchased and excess labor is being devoted to reworking them.

\- If net selling price is more than \$2 below budget, sales volume is more than 10000 units above budget, and profit contribution is more than 5% below budget, then these is evidence (0.7) that price discounts are excessive.

These rules could be supplemented with others that specify appropriate management actions, such as requiring that purchasing agents increase minimum standards for raw materials or instructing the sales force to offer fewer discounts. The rules could also suggest that further information be obtained – for example, that raw materials be sampled and inspected for quality or that a report be prepared summarizing any price discounts and the reasons for granting them.

Unfortunately, systems of this type have not yet been developed, possibly because they would be too specific to a company or industry. However, there are two ESMs that perform similar diagnostic tasks. The first is an expert system that simulates an auditor making bad-debt decisions – that is, determining whether delinquent customer credit accounts should be reported as collectable in a company's financial statements [14]. The system contains rules that use numerical indicators (called positive weights, negative weights, degrees of belief, certainty values, and probabilities), and these are combined in complex ways to produce a bad-debt decision. The rules are of the following type:

\- “Although a portion of this customer’s total balance is still delinquent, payments are being received, and he continues to be an active customer. Positive Weight is -2.0, Negative Weight is 3.0”.

\- “Despite the presence of this delinquent item, newer items have been fully paid. Positive Weight is 1.5, Negative Weight is 0.0”.

The second system simulates the reasoning processes of an analyst evaluating the financial health of a company [8]. The input to the system is a large volume of published financial data about the company and its industry, which is converted into qualitative factors (increase or decrease, above or below industry norm, etc.), and then into evaluations of the form:

\- “I think the company has the following problem: Capacity is too low. Capacity too low explains amount produced too low, which again explains units sold too low, and which also explains finished goods inventory too low."

\- “I do not see any problem, the company looks very healthy to me”.

The two systems just described are based on protocols obtained from auditors and financial analysts (respectively), and their outputs compare quite favorably with the judgements of these professionals. With regard to system integration: it will probably be necessary to integrate ESMs for auditing and financial analysis with data management systems to facilitate access to input data, and an ESM for budget variance analysis might productively be integrated with financial planning models of the type described above and with budget variance investigation models [21].

## 2.3. Scheduling and Assignment

During the past thirty years, substantial effort has been devoted to constructing algorithms for such logistical activities as production and distribution scheduling and, more generally, the assignment of personnel, facilities and materials to jobs or tasks [11]. To some extent, problems of this type can be considered problems in resource allocation, because people, machines, etc. can be viewed as resources to be allocated to job assignments, manufacturing tasks, etc., and some of the mathematical programming techniques used in resource allocation are also used in scheduling and assignment. However, we will be concerned here with those problems that are complex and need more sophisticated methods for their solution.

The complexity has generated some AI research on the application of “if-then” rules and “frames” to assignment and scheduling (respectively). OMEGA [1] is a personnel assignment system based on rules of the type:

\- If person X is experienced for assignment Y and person X is schooled for assignment Y, then person X is qualified for assignment Y.

OMEGA contains contradiction-handling facilities that allow the user to begin with stringent requirements for a set of assignments (which include not only job qualifications, but other factors, such as the availability of travel funds needed to effect a reassignment) and to relax these requirements if the initial goals cannot be achieved.

Another system of this type is ODYSSEY [16], which helps a user to schedule a business trip by prompting the user to fill out travel forms and resolving ambiguities and inconsistencies between data in the various forms and the system. Another frame-based system, NUDGE, helps a user to schedule a meeting [18]. This system is of special interest because it is integrated with a domain-independent search algorithm (called BARGAIN) that resolves scheduling conflicts. The integration of ESMs with other computer-based systems is one of the topics examined in the following section.

## 3. Software Requirements for ESMs

There are two issues in the design of software for ESMs. The first is the design of or enhancement to a language for programming their logic expressions. The second is the integration of modules written in an ESM design language with those written in other languages, such as the planning languages previously described.

## 3.1. Language Enhancement

There are two types of languages commonly used in artificial intelligence: list processing languages such as LISP and logic programming languages such as PROLOG. There are three enhancements to a list processing or logic programming language that would make it more useful in ESM design. The first is the incorporation of control structures of the type found in ALGOL or PASCAL and the arithmetic operations found in these and other higher-order prgoramming languages such as FORTRAN or APL. To some extent this has already been done. GLISP is an extension of LISP that contains such constructions as IF ... THEN ... ELSE ... statements, WHILE ... DO ... and REPEAT ... UNTIL ... loops, and CASE statements [26]. ICON is a string processing language with some of the same enhancements [20]. Both have infix arithmetic operators.

The second enhancement is the incorporation of sensitivity analysis (or “what if”) commands; these, which are commonly found in planning languages [24], allow users to change one or more inputs to a model and to observe the resulting change in outputs. For example, in EMPIRE, a system commercially available from ADR Inc., the command “WHAT IMPACTS PROFIT” (where PROFIT is the name of an output variable and WHAT IMPACTS are reserved words) will cause each input variable (such as various costs and prices) separately to be incremented by 1%; the system reports the new value of PROFIT for each such change, the magnitude of the change, and the percent change in profit. Surveys [25] and case studies [7] concerning the way managers use decision models have shown that these models are used primarily to perform sensitivity analyses, and this will almost certainly be true of ESMs as well.

The third enhancement is the incorporation of a report writer similar to those found in planning languages. Report writers for planning languages are separate from planning models, so that several report writers (e.g., one for a summary report and one for a detailed report) can be used with s single model. Report writers have simple commands for tabular operations (e.g., a row of quarterly profits is a row of revenues minus a row of expenses), plots (e.g., quarterly profits vs. quarter), centering of titles, etc.; their purpose is to allow the designer of a decision support system to format an output report so that a manager can easily read and understand it.

Most planning languages also have default report writers. Since few managers are willing to spend their time trying to interpret poorly presented reports, this is an essential feature, and it will probably also be an essential feature of a logic programming language for ESMs.

In summary, an ESM prerogramming language should have five features:

1. An ability to process logical expressions, especially if-then rules;

2. A vareity of algebraic operators;

3. ALGOL-like or PASCAL-like control structures;

4. Convenient sensitivity analysis features similar to those found in planning languages;

5. A report writer similar to those found in planning languages.

## 3.2. Model Integration

Since managers already have access to a variety of decision models, many ESMs will not be standalone systems but will be integrated in one way or another with these models. For example, ESMs might access and provide data to mathematical programming models, financial and logistical simulations, forecasting models, etc., and this might be done with a software system, a “model management system”. The purpose of this to insulate a user from the physical details of model bank organization and processing, just as a database management system insulates a user from the physical details of database storage, organization and processing. The model management literature (e.g., [2,4,22,30]) suggests that model management systems, in addition to containing facilities for model bank organization and model query processing, should also contain procedures for selecting the models and data files needed to respond to a particular user query. These procedures may be based on logic programming. The application of the resolution principle to the answering of queries requiring retrieval of stored data [19] has been extended to the case where the queries require the execution of decision models [6,27]. Relationships between models and files are described by rules of the type “INPUT-FILE & MODEL → OUTPUT-FILE”, and the collection of files and models needed to respond to a particular query are selected and organised by resolution. Other techniques suggested for this purpose are AND/OR graphs [5], connection graphs [9], semantic nets [15], and frames [13]. Thus, the inferential techniques of artificial intelligence may serve not only as the foundation of an ESM but also as the foundation of a system that integrates a variety of computer-based decision aids with an ESM and with each other.

## 4. Conclusion

During the past forty years the field of management has offered to economists, mathematicians, behavioral scientists, management scientists and computer scientists an unusual opportunity to uncover and investigate interesting problems and to make important contributions to the well-being of organizations. This has resulted in the development and widespread implementation of data-processing systems, management information systems, decision models and decision support systems, as well as several new academic disciplines. Developers of management information systems and decision support systems will certainly find in expert-system technology a fertile field for research and practice, and developers of expert systems will certainly find in management applications a fertile field for research and practice.

## Acknowledgement

This research was supported by the Dean's Fund for Faculty Research of the Owen Graduate School of Management of Vanderbilt University.

## References

[1] G. Barber, Supporting Organizational Problem Solving with a Work Station, ACM Transactions on Office Information Systems, Vol. 1, No. 1, January, 1983, pp. 45–67.

[2] R.W. Blanning, Issues in the Design of Relational Model Management Systems, AFIPS Conference Proceedings 1983 National Computer Conference, June 1983, pp. 395–401.

[3] M. Bohanek, I. Bratko and V. Rajkovic, An Expert System for Decision Making, in: H.G. Sol, ed., Processes and Tools for Decision Support, North-Holland, Amsterdam, 1983, pp. 235–248.

[4] R.H. Bonczek, C.W. Holsapple and A.B. Whinston, The Evolution from MIS to DSS: Extension of Data Management to Model Management, in: M.J. Ginzberg, W. Reitman and E.A. Stohr, eds., Decision Support Systems, North-Holland, Amsterdam, 1982, pp. 61–78.

[5] R.H. Bonczek, C.W. Holsapple and A.B. Whinston, Foundations of Decision Support Systems, Academic Press, New York, 1981.

[6] R.H. Bonczek, C.W. Holsapple and A.B. Whinston, A Generalized Decision Support System Using Predicate Calculus and Network Data Base Management, Operations Research, Vol. 9, No. 2, March-April, 1981, pp. 263–281.

[7] J.B. Boulden, Computer-Assisted Planning Systems, McGraw-Hill, New York, 1975.

[8] M. Bouwman, Human Diagnostic Reasoning by Computer: An Illustration from Financial Analysis, Management Science, Vol. 29, No. 6, June, 1983, pp. 653–672.

[9] M.C. Chen, J.E. Fedorowicz and L.J. Henschen, Deductive Processes in Databases and Decision Support Systems, Proceedings of the North Central ACM 82 Conference, 1982, pp. 81–100.

[10] G.P.E. Clarkson, A Model of the Trust Investment Process, in: E.A. Feigenbaum and J. Feldman, eds., Computers and Thought, McGraw-Hill, New York, 1963, pp. 347–371.

[11] E.G. Coffman, Jr., ed., Computer and Job Shop Scheduling Theory, Wiley, New York, 1976.

[12] R. Davis, Interactive Transfer of Expertise: Acquisition of New Inference Rules, Artificial Intelligence, Vol. 12, No. 2, August, 1979, pp. 121–157.

[13] D.R. Dolk and B.R. Konsynski, Knowledge Representation for Model Management Systems, Naval Postgraduate School, Monterey, CA, 93950, 1982.

[14] C.W. Dungan, A Model of Audit Judgement in the Form of an Expert System, Ph.D. Thesis, University of Illinois, Urbana, 1983.

[15] J.J. Elam, J.C. Henderson and L.W. Miller, Model Management Systems: An Approach to Decision Support in Complex Organizations, Proceedings of the First International Conference on Information Systems, December, 1980, pp. 98–110.

[16] R.E. Fikes, Odyssey: A Knowledge-Based Assistant, Artificial Intelligence, Vol. 16, No. 3, July, 1981, pp. 331–361.

[17] A. v.d. L. Gardner, The Design of a Legal Analysis Program, Proceedings of the National Conference on Artificial Intelligence, August, 1983, pp. 114–118.

[18] I.P. Goldstein and B. Roberts, Using Frames in Scheduling, in: P.H. Winston and R.H. Brown, eds., Artificial Intelligence: An MIT Perspective, Vol. 1, The MIT Press, Cambridge, 1982, pp. 257–284.

[19] C. Green, Theorem Proving by Resolution as a Basis for Question Answering Systems, in: B. Meltzer, D. Mitchie and M. Swann, eds., Machine Intelligence 4, American Elsevier, New York, 1969, pp. 183–205.

[20] R.E. Griswold and M.T. Griswold, The ICON Programming Language, Prentice-Hall, Englewood Cliffs, 1983.

[21] R.S. Kaplan, The Significance and Investigation of Cost Variances: Survey and Extensions, Journal of Accounting Research, Vol. 13, No. 2, Autumn, 1975, pp. 311–337.

[22] B.R. Konsynski, Model Management in Decision Support Systems, in: C.W. Holsapple and A.B. Whinston, eds., Data Base Management: Theory and Applications, D. Reidel, Dordrecht, 1983, pp. 131–154.

[23] H. Mintzberg, D. Raisinghani and A. Theoret, The Structure of ‘Unstructured’ Decision Processes, Administrative Science Quarterly, Vol. 21, No. 2, June, 1976, pp. 246–275.

[24] T.H. Naylor and M. Mann, Computer Based Planning Systems, Planning Executives Institute (5500 College Corner Pike, Oxford, Ohio, 45056), 1982.

[25] T.H. Naylor and H. Schauland, A Survey of users of Corporate Planning Models, Management Science, Vol. 22, No. 9, May, 1976, pp. 927–937.

[26] G.S. Novak, Jr., GLISP: A Lisp-based Programming System with Data Abstraction, The AI Magazine, Vol. 4, No. 3, Fall, 1983, pp. 37–47.

[27] G.P. Schell, Knowledge Representation and Knowledge Manipulation in Decision Support Systems, Ph.D. Thesis, Purdue University, West Lafayette, Indiana, 1983.

[28] M. Sergot, Prospects for Representing the Law as Logic Programs, in: K.L. Clarck and S.-A. Tarnlund, eds., Logic Programming, Academic Press, London 1982, pp. 33–42.

[29] G.A. Welsch, Budgeting, Profit Planning and Control, Prentice-Hall, Englewood Cliffs, 1982.

[30] H.J. Will, Model Management Systems, in: E. Gorchla and N. Szyperski, eds., Information Systems and Organization Structure, Walter de Gruyter, Berlin, 1975, pp. 468–482.
