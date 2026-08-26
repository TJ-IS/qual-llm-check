---
otero_id: 18459
otero_key: "8MSHWJGY"
title: "Characteristics and implementation of decision support systems"
authors: "Rommert J. Casimir"
year: "1988"
journal: "Information & Management"
doi: "10.1016/0378-7206(88)90062-6"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Characteristics and Implementation of Decision Support Systems \*

Rommert J. Casimir

Tilburg University, P.O. Box 90153, 5000 LE Tilburg, The Netherlands, R974CASI@HTIKUB5.BITNET

Three types of information systems related to DSS's. termed genuine DSS's, are defined: the traditionally built DSS, the MIS prototype, and the spurious DSS. The latter uses DSS tools and techniques for other purposes than decision support, such as control. It is shown that a number of features facilitate building genuine DSS's.

Keywords: DSS, Control information system, spurious DSS, expert system, accuracy, security.

![](/api/attachments/8MSHWJGY/fulltext/images/f1c4a8591d271cc5bdd2315a8bc03d65572cbb8d856b82ca30c1fc89f3749197.jpg)

Rommert J. Casimir is a lecturer in Information Systems at Tilburg University. Previously he was a lecturer in Computer Science at Erasmus University, and a Systems Programme with Electrologica. He received his M.A. in Business Economics in 1970. His papers appeared in Information and Management and in national journals, such as Bedrijfskunde, MAB, Informatie and I&I. His current interests are in Management Games and Decision Support Systems. He is also a computer hobbyist specializing in Logic Programming.

\* A preliminary version of this paper was presented at the Working Conference on Decision Support Systems of DDSS, Lisse, The Netherlands, 3-4 June 1987.

## 1. Introduction

In the literature, Decision Support Systems (DSS's) are distinguished from other information systems (IS's) by three characteristics [2,23,33,34]. First, the purpose of a DSS is to help managers in decision making. Originally, the application of DSS's to strategic, unstructured, or semi-structured decisions was stressed [16], but recently, this restriction has been relaxed [38,22]. Second, a DSS uses sophisticated modeling techniques. Third, DSS's are built with specialized DSS tools that allow the design of flexible systems at low cost.

Many DSS texts compare DSS's with "traditional EDP systems", which lack of all three of these. Such comparisons often make two apparently conflicting claims: On the one hand, DSS's contain more advanced features and consequently give more relevant information to management than traditional EDP systems; on the other hand, DSS's can be built with much less effort. Sometimes these arguments give the impression that only a conspiracy between hardware vendors and COBOL programmers is holding back the total replacement of traditional EDP by DSS's [35]. Recently, some authors have stressed the similarities, rather than the differences, between DSS's and other types of IS's [4]. While this view provides sound guidelines for DSS design, it cannot serve as a base for this research, which focuses on features that are specific to DSS's.

## 2. Classification of Information Systems

For our classification we first define our terms. A user DSS is an is aimed purely at helping to make decisions. An is using sophisticated modeling techniques is a logical DSS. An is that is built with the aid of specific DSS tools is a DSS implementation. Table 1 shows the relation between various types of IS. To better understand the characteristics of a genuine DSS, we compare it with the IS's closest to it; i.e. the traditionally built DSS, the MIS prototype, and the spurious DSS.

Table 1  
DSS and related systems

<table><tr><td></td><td>User DSS</td><td>No user DSS</td></tr><tr><td>Logical DSS and DSS implementation</td><td>Genuine DSS</td><td>Spurious DSS</td></tr><tr><td>Logical DSS</td><td>Traditionally built DSS</td><td>Traditional modeling system</td></tr><tr><td>DSS Implementation</td><td>MIS prototype</td><td>IS prototype</td></tr><tr><td>Neither logical DSS nor DSS implementation</td><td>Traditional MIS</td><td>Traditional EDP system</td></tr></table>

## 2.1. Genuine DSS versus Traditionally Built DSS

A traditionally built DSS is designed and programmed in a general purpose programming language, such as Fortran or Pascal, by a single analyst or designed and implemented by a group of professionals using a generally accepted system development method, such as ISAC [27]. In contrast, a genuine DSS is built with specific DSS tools and generators. However, the dividing line is blurred, because APL, which certainly is a general-purpose language, is cited as a powerful DSS tool [29]. Language and system development method choice belong to the discipline of software engineering [7].

There is some empirical and experimental research showing large productivity gains from the adoption of fourth generation languages [15,17]; this does not, however, pertain explicitly to DSS problems, and the study of the factors that influence programmer productivity is still in its infancy [21]. This leaves this field to prophets of diverse faith such as Dijkstra [14] and Martin [28], whose sermons reach beyond the DSS community. As a consequence, we do not exclude traditionally built DSS's from the DSS field. Of course, DSS practitioners should have a firm command of DSS tools, but they should also recognize circumstances, such as low cost of programming or scarcity of computer resources, that favor other techniques.

## 2.2. Genuine DSS versus MIS Prototype

Traditional financial statements have long been the most important sources of information for managers. Some DSS tools, such as model building languages, are well suited for developing systems for this purpose.

The possible superiority of genuine DSS's over information systems producing financial statements as a base for decision making is part of a well-established subject of research. especially experimental research using management games [5,6,10,13,19,20]. As the superiority of advanced techniques as a base for decision making has not yet been proven, there is no reason to exclude MIS prototypes from the DSS field.

## 2.3. Genuine DSS versus Spurious DSS

The main purpose of information systems, other than helping to make decisions, is in establishing the rights and obligations of the organization and its members, and in exercising control over subordinates. The first is the major purpose of salary systems that involve payment to government and social security agencies to establish rights that sometimes will be exercised only after decades.

The need for the second, providing control information, stems from limited responsibility. A subordinate is not responsible for errors caused by executing his superior's orders, but it may be necessary to prove, by punctilious accounting, that the orders were executed. For example, a buyer who is instructed to buy from a specified supplier must prove that the specified order was made, but it is not necessary to show that this supplier is less expensive than competitors.

We define a spurious DSS as an IS with the characteristics of a genuine DSS, except that it is used for other purposes than helping the manager make decisions he used to make before. We distinguish three purposes: Establishing rights or obligations of the organization, increasing control over the manager's actions, and delegation of authority to subordinates.

## 2.3.1. Spurious DSS's for Establishing Rights and Obligations

Typically, a new organization has significant freedom in its way of making decisions. However, as customers become more sophisticated, they ask for better predictions of organizational behavior. As decisions can be better predicted when the decision process and the information used in it are known, customers will tend to call for publication of DSS rules. A typical example is in student grading, where teachers now are required to apply strict averaging rules. As a result, a score awarded to a student is an obligation and not an item that can be used freely in final grading. This change of character diminishes the value of an established DSS for decision support because the ability of the user to improve decision rules during the data collection phase is forfeited. Moreover, system costs will increase with the need for security, and customers may thwart the purposes of the organization by adapting to the rules defined in the DSS. The threat posed by this evolution, termed "Migration" by Moore and Chang [30], may dominate the value of a genuine DSS, thus stalling DSS activity in fields such as personnel.

Similarly, many industries face increasing government regulation with a corresponding increase in the volume of data that must be supplied. A DSS adding to or interpreting those data may be appropriated by the regulatory agency. A textbook example is the case of a company that refrained from designing a DSS to track dangerous chemicals lest claims could be raised against it [12].

## 2.3.2. Spurious DSS's for Increased Control

The control view of organizations differs from the management science view adopted in the DSS literature in its treatment of deviation from the average. In the management science view, deviations are considered noise with no other significance; in the control view, they are aberrations from a norm that have to be corrected lest the average be incorrectly influenced. Moreover, it is assumed that deviations will increase when control is loosened. The control view has a strong influence on management practice, as demonstrated by the large outlays for control systems, the highest esteem for auditors, and recurring stories about strict controls on petty expenses to encourage a general atmosphere of parsimony, but it is systematically underrated in the is literature. The management science view is also seen in game theory [31], which models economic activity after inactive games, such as chess where the decision "to make a move" is tantamount to making the move itself, and nct after sport games, such as tennis where the main difficulty is in implementing the decision "to put the ball out of reach of the opponent". Another example of the conflict between these views is found in the census debates in some European countries, where proponents defend the census because of the management information it could provide, while opponents argue that authorieis would use census data for control.

The large gains that are possible from increased control favor the use of DSS's for this purpose. As a first step toward this end, use of the DSS is made mandatory. Next, management control may be increased in four ways:

\- First, the DSS may restrict the choices a manager may make.

\- Second, the DSS may operate on prescribed input, thus focusing the managers' attention on a particular set of variables that is not of their choice.

\- Third, the DSS may monitor input and output of the DSS as well as deviations from DSS advice on the part of the manager.

\- Fourth, the DSS may monitor variables entirely unrelated to the decisions at hand, e.g. attendance.

It is to be expected that managers will quickly adapt to the use of a DSS for control by supplying inputs that produce the desired results. A system supplying such inputs might use a personal computer and could be called an inverse DSS.

Higher level management can counter such behavior by auditing inputs, but then the system is no longer a DSS.

Just as DSS's introduced by higher level management will be viewed with suspicion, managers may refrain from developing DSS's they need in case they are appropriated by higher level management. In this respect, the attitude of managers to superiors is the same as the attitude of top management towards customers and government. It may be preferable not to collect information that could do harm if accessible to the "opponent"

## 2.3.3. Expert Systems and Spurious DSS's

We define an Expert System (ES) by its function and not by its internal architecture. An ES is a computer program that advises decision makers on decisions that they would not normally make.

This definition is consistent with the intent of an ES, as defined in the literature [39]. If the decision making rules of a manager are codified in a DSS and its operation is entrusted to a subordinate, this DSS is working as an ES. It is a spurious DSS, because it changes the decision making process. Especially, codification diminishes the flexibility of decision rules. However, in contrast to spurious DSS's forced onto a manager who previously made decisions, ES's will be welcomed by users because their responsibilities are apparently widened.

## 3. Characteristics of Genuine DSS's

The value of information is a well-defined concept in the context of decision making [24] and in decision analysis [26]. However, there is no similar definition in the context of control. Even the generally accepted assertion that business applications need high accuracy in number representation [8] is apparently not supported in the literature. Consequently, it is assumed that an is used for control, termed Control Support System (CSS), always needs full, detailed and accurate data, and it will be argued that a genuine DSS does not.

## 3.1. Accuracy

## 3.1.1. Impact of Accuracy

As a rule, a better decision may be made when more accurate information is available. An illustrative example is found in the “newsboy problem”, where a newsboy has to decide how many copies of a newspaper to buy, given his prediction of the number he will sell [24,26]. Here accurate information has a high value, because unsold copies represent an immediate loss. However, in many cases it is possible to compensate for the lack of information by other means; e.g. by carrying stock or by reserving spare capacity. Then the final result will be far less influenced by the accuracy of the prediction. A pertinent example is the computation of the economic order quantity (EOQ), where 100% error in the estimate for order cost may entail only a 6% error in total costs [24]. Even if a prediction is considered highly accurate, such as a prediction of currency rates a year hence within a 1% margin, it is orders of magnitude less accurate than the historical data routinely used in a css. The relatively low demand on accuracy influences a number of design variables.

## 3.1.2. Data Types

All numeric variables in a DSS may be represented by a single data type: a real or floating point number. This diminishes program size, because of the absence of data type definitions and because of the smaller number of data type conversions needed, and the complexity of the programming language, because of the small number of data types and the absence of duplicate functions. As a corollary, the use of a single numeric data type has kept DSS languages having a large number of functions within reasonable limits.

## 3.1.3. Data Structures

The use of samples instead of the full set of the data has been studied extensively in statistical theory. It entails a lower data volume, which implies that complicated data structures, such as trees, intended to save memory space and retrieval time, can be replaced by simple data structures such as arrays. Simple procedures may be used to perform common operations, such as extracting a row or a column, on arrays. Moreover, arrays can be transported from external to internal memory and from memory to screen without conversion. It is significant that many tools that have been successfully used in DSS design, such as APL, spreadsheets, and model building languages, use arrays as their principal data structure. An additional advantage of the use of arrays is that mathematical models are often defined in matrix format.

## 3.1.4. Procedures

As a consequence of the relatively low data volume, procedures need not to be designed for maximum speed. The trade-off between program size and execution speed is a well known subject in elementary programming texts, but there are few experimental of empirical data on the relationship, even for such well-studied programs as optimizing compilers [1].

## 3.1.5. Organization

The low priority of efficiency in DSS design implies there is less need to divide the design effort between a designer who concentrates on the model, and a programmer, who concentrates on implementation efficiency. Such a division of labor entails an increase in the total time of the design, because of communication and waiting costs, which will not be counterbalanced by the lower salary and the higher productivity of the programmer.

## 3.1.6. Reliability

An IS is reliable if there is no danger of accidental loss or corruption of program and data. Reliability is provided by redundancy, e.g. by duplication or by the use of error-correcting codes. In a genuine DSS, a data item often is an item in a sample, so its loss merely reduces sample size, with a concomitant loss of accuracy. This diminishes the demand for reliability, with a corresponding decrease in cost.

## 3.2. Security

## 3.2.1. Impact of Security

Security of an IS implies both reliability and protection against illegal data modification and unauthorized reading. Illegal data modification threatens IS's that record rights and obligations and IS's used for control, rather than genuine DSS's. In an IS that records rights and obligations, an intruder may directly profit from a modification in its data; e.g. when he changes the balance of a bank account. In an IS used for control, a modification may cover up an illegal transaction that would otherwise be detected by comparing physical data with that in the IS. A DSS offers less scope for fraud, because the impact of a modification in DSS data will not be known to the intruder. In general, results from a DSS will be compared with data from other sources before a decision is actually implemented.

On the other hand, the danger of unauthorized reading pertains equally to DSS data and that in other IS's and this may be acute in competitive industries, such as oil prospecting and contracting.

## 3.2.3. Costs of Security

The literature on security tends to present technology that helps to attain security [18,36] rather than risk analysis. Recently, more attention has been given to cost-effectiveness of security measures, but the relation to the type of IS is not covered in the relevant papers [9,32]. Moreover, authors often are of the opinion that too little attention is given to security in EDP operations [11]. This makes it difficult to assess the gains that can be reaped from lowering security standards for DSS's. However, in view of the length of the lists of security measures recommended for secure systems, they should be considerable.

## 3.3. Data Collection

A DSS may use data extracted from an EDP system. This simplifies DSS design by excluding the data collection phase. Use of a generalized Database Management System also simplifies data extraction. However, appropriate data for a DSS will not always be found in a database maintained for other purposes. For example, EDP systems for utilities normally deal with data on individual consumers and do not contain information on peak loads needed for investment decisions. In such a case, there are two possibilities: either the appropriate data are included in the general database, or a separate data collection process is started. The first alternative may, however, be more expensive, as data included in the general database will have to satisfy much higher completeness and reliability requirements. Moreover, once the data have been collected, an opportunity exists for using them in a css, and this may be given priority over DSS building.

On the other hand, various techniques may be used to capture DSS data. One is sampling, another, which may be termed analog aggregation, is used when a variable can be measured that is functionally dependent on the sum of a number of variables. Examples include measuring the total output of a power plant, counting the number of supermarket visitors through an aerial photograph of the parking lots, weighing invoices, which was actually practised in the Ford Motor Company [25], and estimating total working hours from coffee consumption. In the last example, it is clear that analog aggregation cannot be used for control.

## 3.4. Models

Modeling systems are sometimes thought to be synonymous with DSS. A model provides an interpretation of a set of data. Thus, both continuous and discrete simulation models map states over time. Models contain rules that define relations between variables. A simple rule is a triple $\langle f, x, y \rangle$ , where x and y are variables and f is mapping of x into y. Variables x and y may be measured; the mapping f is derived from logic or operations research. In a DSS, it suffices to measure x and compute $y = f(x)$ . In a control system $y' = f(x)$ is computed and then $y'$ is compared to the recorded value of y. A difference signals the necessity of specific control actions. The equation is termed an invariant in the theory of program correctness [3], and an integrity constraint in database theory [37]. As the difficulty of a programming task increases with the number of invariants, programming a genuine DSS is easier than programming a css using the same model.

As an example, the following rule is valid for any organization:

$$
\mathrm{cash} _ {i} = \mathrm{cash} _ {i - 1} + \text { receipts } _ {i} - \text { expenses } _ {i}.
$$

When the value of cash $_{i-1}$ is known, application of this rule in a DSS implies that inputs have to be given for only two of the three variables cash $_{i}$ , receipts $_{i}$ and expenses $_{i}$ . Of course, this has been known by shopkeepers from ancient times. In a css, all three variables must be recorded to detect theft, as well as counting errors. Cash registers and point of sales systems (POS) diminish the cost of recording receipts. In a css, this directly reduces the cost of data collection, in a DSS, cost reduction results only if the reduced cost of recording receipts is lower than the cost of recording cash or expenses.

The notion that extensive use of models facilitates rather than impedes DSS design may come as a surprise to some practitioners, but it is in line with long traditions of statistics and OR. Once this is recognized, the details of the actual implementation are less important. Users of DSS tools and generators may rely on built-in functions; designers of traditionally built DSS's may use generally available libraries.

## 4. Conclusions

The comparison between different types of IS's has shown that the purpose of an IS is the main determinant of design attributes. This has different implications for DSS research, DSS education and DSS practice. DSS research should center on determining how information systems affect decision making. This implies it should have solid foundations in management science [22]. Alongside DSS's, other types of information systems should be studied, as this field deserves more fundamental research.

For education in DSS, the direction is clear. A DSS curriculum should largely be made up of Management and Computer Science courses, crowned by assignments in DSS design.

Dss practitioners should pay more attention to the real purpose of the systems they are building and the impact of that on design. They should recognize spurious Dss's as a source of practical difficulties in Dss design.

## References

[1] Aho, A.V., Sethi, R. and Ullman, J.D., Compilers: Principles, Techniques and Tools. Addison-Wesley, Reading, Mass., 1986.

[2] Alter, S.L., Decision Support Systems: Current Practices and Continuing Challenges. Addison-Wesley, Reading, Mass., 1980.

[3] Apt, K.R., Ten Years of Hoare's Logic. ACM Trans. on Progr. Lang. and Syst., Vol. 3 No. 4 (October 1981), pp. 431–484.

[4] Ariav, G. and Ginzberg, M.J., DSS Design: A Systemic View of Decision Support. CACM, Vol. 28 No. 10 (October 1985), pp. 1045–1052.

[5] Bell, J., The Effect of Presentation Form on the Use of Information in Annual Reports. Management Science, Vol. 30 No. 2 (Februari 1984), pp. 169–185.

[6] Benbasat, I. and Schroeder, R.G., An Experimental Investigation into some MIS Design Variables. MIS Quarterly, Vol. 1 No. 1 (March 1977), pp. 37–50.

[7] Boehm, B.W., Software Engineering Economics. Prentice-Hall, Englewood Cliffs, N.J., 1981.

[8] Borland International, Turbo Pascal Reference Manual Version 3.0. Borland International, Scotts Valley, Calif., 1985.

[9] Bui, T. and Sivasankaran, T.R., Cost-effectiveness Modeling for a Decision Support System in Computer Security. Computers and Security, Vol. 6 No. 2 (April 1987), pp. 139–151.

[10] Courtney, J.F., DeSanctis, G. and Kasper, G.M., Continuity in MIS/DSS Laboratory Research: The Case for a Common Gaming Simulator. Decision Sciences, Vol. 14 No. 3 (July 1983), pp. 419–439.

[11] Courtney, R.H. and Todd, M.A., Problem Quantification - Its Importance to Cost-Effective Computer Security. in: J.B. Grimson and H.J. Kugler (eds.), Computer Security: the Practical Issues in a Troubled World, pp. 55–63. North Holland, Amsterdam, 1985.

[12] Davis, G.B. and Olson, M.H., Information Systems, Conceptual Foundations, Structure and Development. McGraw-Hill, New York, 1985 (p. 320).

[13] Dickson, G.W., Senn, J.A. and Chervany, N.L., Research in Management Information Systems: The Minnesota Experiments. Management Science, Vol. 23 No. 9 (May 1977), pp. 913–923.

[14] Dijkstra, E.W., The Humble Programmer. CACM, Vol. 15 No. 10 (October 1972), pp. 859–866.

[15] Forage, G., Fourth Generation Languages and Advanced Software Development Aids. Data Processing, Vol. 27 No. 9 (November 1985), pp. 6–8.

[16] Gorry, G.A. and Scott Morton. M.S., A Framework for Management Information Systems, Sloan Management Review, Vol. 13 No. 1 (Fall 1971), pp. 56–70.

[17] Harel, E.C. and McLean, E.R., The Effects of Using a Nonprocedural Computer Language on Programmer Productivity. MIS Quarterly, Vol. 9 No. 2 (June 1985), pp. 109–120.

[18] Hsiao, D.K., Kerr, D.S. and Madnick, S.E., Computer Security. Academic Press, New York, 1979.

[19] Jarvenpaa, S.L., Dickson, G.W. and DeSanctis, G., Methodological Issues in Experimental IS Research: Experiences and Recommendations. MIS Quarterly, Vol. 9 No. 2 (June 1985), pp. 141–156.

[20] Kasper, G.M. and Cerveny, R.P., A Laboratory Study of User Characteristics and Decision-making Performance in End-user Computing. Information and Management, 9 (1985), pp. 87–96.

[21] Kearney, J.K., Sedlmeyer, R.L., Thompson, W.B., Gray, M.A. and Adler, M.A., Software Complexity Measurement. CACM, Vol. 29 No. 11 (November 1986), pp. 1044–1050.

[22] Keen, P.G.W., Decision Support Systems: The Next Decade. in: E.R. McLean and H.G. Sol (eds.): Decision Support Systems, A Decade in Perspective, North Holland, Amsterdam, 1986.

[23] Keen, P.G.W. and Scott Morton, M.S., Decision Support Systems: An Organizational Perspective, Addison-Wesley, Reading, Mass., 1978.

[24] Kleijnen, J.P.C., Computers and Profits. Addison-Wesley, Reading, Mass., 1980.

[25] Lacey, R., Ford, the Man and the Machine. Ballantine Books, New York 1987 (p. 451).

[26] LaValle, I.H., Fundamentals of Decision Analysis. Holt, Rinehart and Winston, New York, 1978.

[27] Lundeberg, M., Goldkuhl, G. and Nilsson, A., Information Systems Development, A Systematic Approach. Prentice-Hall, Englewood Cliffs, N.J., 1981.

[28] Martin, J., An Information Systems Manifesto, Prentice Hall, Englewood Cliffs, N.J., 1984.

[29] McLean, E.R. and Reasing, T.F., Installing a Decision Support System: Implications for Research. in: G. Fick and R.H. Sprague (eds): Decision Support Systems: Issues and Challenges. Pergamon Press. Oxford, 1980.

[30] Moore, J.H. and Chang, M.G., Meta Design Considerations in Building DSS. in J.L. Bennet (ed): Building Decision Support Systems. Addison-Wesley, Reading, Mass., 1983.

[31] von Neuman, J. and Morgenstern, O., Theory of Games and Economic Behavior. Princeton University Press, Princeton, 1947.

[32] Post, G.V. and Diltz, J.D., A Stochastic Dominance Approach to Risk Analysis of Computer Systems. MISQ, Vol. 10 No. 4 (December 1986), pp. 363–374.

[33] Reimann, C. and Waren, A.D., User-oriented Criteria for the Selection of DSS Software. CACM, Vol. 28 No. 2 (Februari 1985), pp. 166–179.

[34] Sprague, R.H. and Carlson, E.D., Building Effective Decision Support Systems. Prentice-Hall, Englewood Cliffs, N.J., 1982.

[35] Thierauf, R.J., Decision Support Systems for Effective Planning and Control. Prentice-Hall, Englewood Cliffs, N.J., 1982.

[36] Tomkins, F.G. and Rice, R., Integrating Security in the Software Development Life Cycle. in: J.B. Grimson and H.J. Kugler (eds): Computer Security: The Practical Issues in a Troubled World. North Holland, Amsterdam, 1985, pp. 65–106.

[37] Ullman, J.D., Principles of Database Systems. Pitman, London, 1980.

[38] Van Groenendaal, W.J.H., Towards a Workable Definition of DSS. Journal of Applied Systems Analysis, forthcoming.

[39] Waterman, D.A., A Guide to Expert Systems. Addison-Wesley, Reading, Mass, 1986.
