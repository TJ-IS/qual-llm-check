---
otero_id: 18319
otero_key: "PTVAC6TH"
title: "Microcomputer based multiple criteria decision support system for strategic planning"
authors: "G. Chandrasekaran; R. Ramesh"
year: "1987"
journal: "Information & Management"
doi: "10.1016/0378-7206(87)90039-5"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Microcomputer Based Multiple Criteria Decision Support System for Strategic Planning

G. Chandrasekaran and R. Ramesh

310 Jacobs School of Management, State University of New York at Buffalo, Buffalo, New York 14260, USA

There are two major approaches currently used for developing Decision support Systems (DSS) for strategic planning, especially in the objective formulation stage. Several mathematical models have been developed to abstract the decision situation. However, they do not take into account either behavioral aspects of decision making or the presence of multiple and conflicting objectives. A second approach is to consider the several qualitative factors that go into decision making; such considerations are normally situation-dependent and hence it is difficult to provide a system for general managerial situations.

The Multiple Criteria Decision Making (MCDM) approach combines the advantages of both the approaches and, therefore, is an excellent alternative for designing DSS. This paper develops an MCDM approach to strategic planning. The model is applied to such a problem in a simulated environment and the problem is solved interactively. Our experience shows that the proposed methodology is a viable approach for solving practical decision problems in strategic planning.

Keywords: Decision Support Systems, Strategy Formulation, Multi Criteria Modelling, Micro Computer Based Applications.

## 1. Introduction

It is difficult to make a decision based on organizational objectives, because they tend to be conflicting in nature. For instance, increasing market share is a desirable objective, but often the resources required to achieve this objective reduce the financial returns measured in ROA or ROE. Furthermore, there are always conflicts among the managers of different functional areas because of their separate concerns and goals which may not agree with the stated organizational goals. Against this background, several methods have been suggested as ways to improve the decision making process in a systematic manner. The approach involves the use of mathematical models.

![](/api/attachments/PTVAC6TH/fulltext/images/41b0ff40227335c48719708670f01c9117a25e877714a79be11eeec6cc5e40d6.jpg)

![](/api/attachments/PTVAC6TH/fulltext/images/816c0f3e7e1b1f90e9fe2fade7e59b074d33c0f925746debc7d4f848bc4e7fe4.jpg)  
G. Chandrasekaran is an Assistant Professor in the Department of Management Science and Systems, School of Management at SYNYAB. He holds a Ph.D. from State University of New York at Buffalo. He won the General Electric award for best dissertation in Strategic Planning for 1981. He is actively involved in consulting and research in planning and information systems. His publications appear in strategic planning and information systems journals.

R. Ramesh is an Assistant Professor in the Department of Management Science and Systems, School of Management at SUNAB. He obtained his Ph.D. in Operations Research from the State University of New York at Buffalo. His areas of specialization include mathematical programming, combinatorial optimization, database theory and optimization. His publications appear in European Journal of Operations Research, Annals of Operations Research and Information Processing & Management.

Models are abstractions of the real-world and must incorporate the recognizable and significant aspects of the decision making process. They are generally based on popular and widely used techniques such as linear programming, integer programming, network, and other optimization methods. These techniques are used to optimize specific decision objectives under resource constraints. Although such models are fairly representative of real-world decision problems, they are not adequate in assessing either the behavioral aspects or any multiple conflicting objectives.

The second approach advocated by the organization theory researchers is to focus on decision making models which move away from the rationality assumption of mathematical models and suggest alternatives, such as garbage-can models $[7]$ or incremental logical inputs $[8]$ at different stages of the decision process. Although, in theory, these political processes describe situations as they occur, it is very difficult to apply them to a managerial situation. It is also imperative to recognize the need to consider tradeoffs among objectives and between decision makers before arriving at a final set of objectives.

The Multiple Criteria Decision Making (MCDM) approach offers an excellent middle ground alternative, incorporating several mathematical principles while recognizing the need for the consideration and evaluation of many alternatives before making the decision. This aspect concerns itself especially with qualitative approaches to decision making.

One of the major reasons of low popularity of complex models is the difficulty in understanding the various components of the model and setting up the information required for running the program. However, software such as LOTUS 1-2-3 allows the MCDM problem to be set up in a user-friendly manner with spreadsheet tables and menus. Increased user friendliness, we believe, will lead to the highest acceptance by managers.

The focus of this paper is to demonstrate the applicability of the MCDM approach to decision making in the strategic planning area. Furthermore, it identifies the reasons why a microcomputer based approach will be more successful from an implementation point of view.

## 2. An Overview of MCDM Modeling

Decision making in real world situations usually involves the evaluation of alternative courses of action under multiple objectives; most real world objectives are conflicting in nature. As an illustration, consider the purchase of an automobile. The buyer may wish to buy a car that is not expensive, provides good fuel economy, is safe and is sporty. Given these expectations and the cars available, no car may satisfy all the requirements. In such situations, the buyer must compromise or make tradeoffs among objectives: according to the availability of cars, the urgency or need for an immediate decision, etc. Accordingly, the solution techniques for multicriteria decision problems are based on an exploration and approximation of the preference structure. A general process for management decision making involves:

(i) A decision maker or a group of decision makers who are central to the decision process.

(ii) A set of possible alternative available courses of action.

(iii) A decision rule or an implicit preference structure within which the alternatives are evaluated.

(iv) Tradeoffs among the alternatives in terms of the objectives of the decision makers and the process of compromise and consensus leading to a most agreeable solution.

In general, the general multiple criteria decision making problem may be formulated as:

“Maximize” $F(x)$

subject to: $x \in S$

where x is the vector of decision variables, $F(x)$ is the vector of objectives to be maximized simultaneously and S is the set of feasible alternatives. The set S may be stated explicitly and may consist of linear or nonlinear inequalities involving the decision variables. Alternatively, the constraints may be stated implicitly by listing alternatives. The vector of objectives F may consist of cardinal as well as ordinal criteria. Attributes such as quality and convenience of a car may only be measurable on an ordinal scale. The word maximize is quoted because its meaning for a vector is not a well-defined mathematical operation.

The solution techniques for MCDM problems based on interacting with the decision maker usually proceed by selecting a pair of alternatives from the set S and asking the decision maker to choose between them. Based on this choice, the solution space is then restricted, and the procedure is repeated with the remaining solutions until the most preferred solution is found. The solutions selected for the consideration of the decision maker provide unique combinations of objective values. In other words, this implies that there is not another solution whose objective values are better than those of the selected solutions with respect to all the objectives. The selected solutions are called 'efficient' or 'pareto-optimal' [6,10]. The search for the most preferred solution is restricted to the set of efficient solutions of the decision problem. Further, the solution procedures follow different strategies for converging to the most preferred solution with minimal interaction with the decision maker and minimal computational effort.

The decision problem considered here has been modelled as a multicriteria linear programming problem. It is solved interactively.

## 3. The Decision Situation

The simulated environment used in this study is contained in the management game described in Jensen and Cherrington [4]. The participants in the game are required to have sufficient knowledge of the management techniques needed to solve practical strategic planning problems. Accordingly, in our study the participants have been drawn from the final-year graduating M.B.A. students at the State University of New York at Buffalo. The game consists of eight firms competing by marketing two products in two geographic areas. Teams of two members manage each firm and are responsible for the entire operations – marketing, production, financial and materials planning. The teams run their firms for 1 to 2 years and make operational decisions for all the functional areas on a quarterly basis. The actual performance is obtained by the game administrator executing all the decisions made by all the firms. The overall evaluation of the teams is based on how well they perform on market share, net income, and shareprice; market share is computed for each area and product and there are four measures. These measures constitute the multiple objectives faced by the managers of the firms.

The decision objectives are quite conflicting and teams are expected to balance their organizational functioning suitably. The participants perform the following projects: (i) a sales forecasting project, where the teams determine the critical variables for success in each market along with an approximate estimation of elasticities; (ii) a production planning project, to show the interrelationships among capacity used and the opportunity costs of decisions; and (iii) financial forecasting, to appreciate the linkages of various functional areas to financial results. Based on such a detailed understanding, the teams are expected to determine their strategy in each functional area.

## 3.1. Marketing

The teams can choose to operate in all four areas or some, based on their appreciation of contribution margin, capacity use, and demand volume. They can choose to gain market share in the areas by moderating price, advertising, number of salesreps, sales compensation – commission and salary, product innovation (R&D expense), and quality (quality control expense). The choice of the level of expenditure in each factor will depend on the team's perception of the market and its estimate of competition.

## 3.2. Production

There are two stages of production; both products have to be processed in these two stages. The initial available capacity is provided to the teams. Appropriate maintenance is needed in order not-to-lose the available capacity. There is one plant available for production in area 1; the requirement in area 2 has to be met by shipping the required quantity either by regular or emergency shipments. Furthermore, the available capacity can be increased by second shift or overtime.

## 3.3. Finance

The teams can use stocks, bonds, term loan, or short period loan to meet their cash needs. Their decision has to be moderated by the need to conform to required financial ratios, such as current ratios and debt-equity ratio. Similarly, the stock issue has to be viewed in terms of the effect on share price. In addition to all these options for raising cash, the teams can also factor their account receivables to gain the cash needed for operations.

## 3.4. Materials Planning

There are two types of raw materials used in the production process; both products use the two materials in differing quantities. The required quantity of materials can be either procured in the open or futures market. The latter method requires prior planning but procures materials at a cheaper cost.

Altogether the teams have to make about 50 decisions for each quarter for all these areas. The decision on the variables are based on an understanding of the industry background and experience gained from one quarter to another.

## 4. The MCDM Model

Although the teams can choose values for the various strategic variables based on their study of the relationship of the strategy variables and performance criteria, the choice of strategies which yield the best combination on all objectives – market share, income and share price – has to be achieved based on the individual ability to work out all the tradeoffs. The MCDM approach offers an ideal decision support framework to help the teams to determine the optimal mix of objectives based on their analysis of the market environment (which they can input into the MCDM program) and other resource constraints. Furthermore, the MCDM model explicitly recognizes the preference pattern of the decision maker when they are presented with competing alternatives. That is, MCDM acts as an expert system, gaining insight into the decision-maker's preferences based on interactive execution, leading to the determination of the optimal mix of objectives. The above decision situation has been mathematically formulated as a multicriteria linear programming problem as follows:

"Maximize"

1. Market Share: Product 1, Area 1

2. Market Share: Product 1, Area 2

3. Market Share: Product 2, Area 1

4. Market Share: Product 2, Area 2

5. Net Income

6. Share Prices

Subject to:

1. Marketing constraints

\- Bounds on market shares

\- Pricing constraints

\- Budget constraints on product promotion

\- Constraints on commission to salesmen, salaries and distribution costs

2. Production constraints

\- Production capacity constraints

\- Budget constraints on material costs and labor costs

3. Demand constraints

\- Supply (quantity produced + opening stock) > demand (est.sales)

4. Financial constraints

\- Limits on borrowings

\- Limits on expenses

5. Operational level constraints - The strategies should be within $50\%$ to $150\%$ of the industry norms with respect to all the decision variables.

All the six objectives in the above problem are to be simultaneously maximized. Clearly, the objectives are in conflict. The interactive multicriteria linear programming method of Zionts and Wallenius [11] is used to solve this decision problem. The decision maker interacts with a computer program and expresses preferences to alternate efficient feasible strategies generated from the model. The problem is solved in an iterative manner, generating a sequence of strategies that are monotonically preferred by the decision maker, and stopping with the most appropriate strategy from the decision-maker's point of view. Throughout the interactive phase of the procedure, the decision-maker's implicit preference structure is explored and approximated. The above model consists of several strategic decision variables and the program has been designed also to allow user's input of the estimates on these variables. Furthermore, the model has been made flexible to accommodate changes in the problem formulation and the model parameters to perform several sensitivity analyses.

The teams managing the firms employ the model to arrive at their decisions in each quarter. The members of a team could operate the model in either of the following ways:

(i) Collective interactive sessions, in which all the members operate the model together. In this case, the alternative strategies generated by the model are considered and evaluated through a process of conferring, discussing and consensus at every stage of the solution process. The main advantage of this approach is that each decision maker gains a clear understanding of the effects of various strategies through discussion. This will ensure that the final solution obtained from the model will have the collective sanction and commitment of all the team members. However, the main disadvantage of this method is that the process of solution is rather slow and could even be severely impacted at several stages by difficulties in reaching an agreement.

(ii) Each decision maker could first solve the problem using the model individually; then all could collectively confer on their respective solutions through a process of exchanging notes. The main advantage of this method is that the problem can be solved in a short time. However, this method could lead to an impasse in reaching a consensus during the final deliberations.

We are experimenting with both these approaches. However, we feel from our experience that collective interactive sessions are preferable in view of the strength of the collective sanction that the final solution would receive from the team members.

## 5. Configuration of the DSS

Application of MCDM models to solve practical problems necessitates a DSS. But although the models provide a convergent strategy, the model is actually driven by the decision maker. Therefore appropriate decision aids, in the form of scenario projections of decision consequences, should be provided. Furthermore, the quality and the reliability of the model along with information presentation are critical to quick consensus. An approach for the design of databases and user interfaces for decision making is given in [3].

Figure 1 shows a tree component framework for the DSS. The decision problem is defined, formulated and stores as software in the front end. The problem is solved by a procedure also resident as software in the front end. In our prototype, the front-end consist of the multicriteria linear programming problem and its solution procedure [11]. The front-end generates efficient alternative solutions and provides for scaling the preference structure of the decision maker within a convergent procedure. These solutions are then transmitted to the baseline support system, from which they are projected in the form of scenarios for evaluation.

![](/api/attachments/PTVAC6TH/fulltext/images/94419ea63d69e4d6352ad6e1b494a3c70f9f358649833fb82dd00238b3f2a855.jpg)  
Fig. 1. Systems Framework for Multicriteria Decision Making.

The baseline support system can be designed in many ways. If the decisions are made by an expert system, then decision analysis uses its decision logic. Then the scenario assessment system performs detailed assessment of expected consequences by projections from an information base. But, if the decisions are made by decision makers, then they consider alternate scenarios and trade-offs and make choices interactively. In our decision situation, the team members were therefore part of the baseline support system. The information base of decision consequences is primarily composed of statistical estimates. For example, if a given strategy ensures 15% market share of product 1 in Area 1, then its consequences on the company's capital structure, reactions from competitors, and future growth in market shares can be projected from the database.

![](/api/attachments/PTVAC6TH/fulltext/images/3296e312493434e08a56e39d6e6b8dcae7240d735666838c268d25ec5c6878a5.jpg)  
Fig. 2. Executive Framework for Decision-Support Systems.

The configuration in Figure 1 presents a systems framework for designing expert decision systems as well as interactive decision support systems. In the expert decision systems, decisions are made usually on a repetitive basis, and are designed as artificially intelligent systems. Such systems employ decision analysis through a batch process, and a logical scenario assessment system to evaluate alternatives generated in the procedure. However, in a human-based decision support system, the alternatives are directly evaluated by the decision makers. In both the systems, an information base is used to evaluate the consequences of the decision alternatives.

Figure 2 shows an executive framework: the logical integration of the functions.

## 6. Microcomputer Based Modelling

The MCDM model and the support systems for the decisions situation described earlier are implemented on CDC-Cyber/730 mainframe computer. We are now implementing the model and associated systems on an IBM-Personal Computer. The conversion of programs to microcomputers will result in a number of advantages. These can be divided into three broad categories; self-management capability, efficiency improvement, and privacy.

## 6.1. Self-management Capabilities

Systems that support multicriteria decision making require the following system management capabilities:

(i) Software and hardware for the maintenance and operation of the front-end model

(ii) Adequate system for supporting a variety of databases with built-in access and retrieval

(iii) Support functions for scenario projection

(iv) User friendly interaction with the decision maker.

Systems such as the IBM-Personal computer are sufficient for handling front-end models of moderate size and complexity. Most practical multicriteria decision problems that can be solved interactively involve up to seven objectives [6], [10]; problems with more objectives and not easily amenable to solution by MCDM techniques involving pairwise comparisons. This limitation is based on consideration of the cognitive load on the decision maker in evaluating alternate solutions.

The decision situation described here involves six objectives, thirty decision-variables and twenty-five constraints. Such problems are well within the available memory capacities and computational speeds of microcomputers. Furthermore, the introduction of larger PCs with enhanced storage and computing capabilities indicates that it is now possible to use them for even bigger multicriteria decision problems. Thus restrictions on the size of problems arise more from the cognitive limitations of the decision maker.

Database management systems (DBMS) such as DBASE II and DBASE III provide excellent baseline support. Their use allows independent creation and maintenance of information bases for various users and applications. Furthermore, these systems are quite inexpensive compared to the mainframe database management systems. Therefore from the point of view of a systems designer who wishes to develop support systems for moderate sized problems, a microcomputer based approach seems feasible as well as economical.

Spreadsheet packages allow the decision maker to define, formulate and set up the problem easily. In our example problem, the decision maker must set up the matrices of constraint coefficients and the objective functions, and the vector of right hand sides. If a sensitivity analysis is required, the user will have to modify these coefficients: again spreadsheets are extremely useful for this.

The projection of scenarios from the information base can be enhanced by the use of color graphics, etc. Such displays enhance the user appeal and give the decision maker a clear understanding of the consequences of the decisions. In this respect, the availability of good and relatively inexpensive graphics packages makes the microcomputer a powerful tool.

## 6.1.1. Efficiency Improvement

One of the major advantages of microcomputers is the increased speed of turnaround in smaller installations. In a centralized computer environment with a large number of users and relatively heavy demands, the response time and system accessibility tend to be low. Furthermore, in the decision situation the users may with to solve the problem repeatedly in order to gain insight. This is done by conducting several iterations, examining a wide variety of alternatives over an extended time interval. We have observed that this enables the decision maker to organize priorities and obtain a clear understanding of the needs and constraints of the decision situation. Therefore, a PC will be of tremendous help in providing the accessibility and flexibility. In addition, the use of a microcomputer network would enhance conferencing capabilities: decision makers invariably are located at different places, and the network provides immediate access to them simultaneously and enables them to interact with one another through the model. This is the most important advantage of microcomputers.

## 6.1.2. Privacy

One of the major advantages of using microcomputers is the possibility of increased privacy and security gained by the user. The mainframe computer needs a secure interface to prevent unauthorized access to sensitive data, such as that for strategy formulation. The problem arises when there are more people and data using common storage devices. The microcomputer is one way to solve this. We have observed that developing input data is difficult and time consuming. The system problems such as insufficient memory space, response time, etc, also have proved to be difficult hurdles. Given the complexity associated with the setting of objectives, we had to minimize these problems to get user acceptance.

## 7. The Microcomputer Implementation

The program for multiple criteria modelling using several objectives is now in its final stages of development, but here we present a discussion based on a working bicriteria model. The multiple criteria model is a direct extension of this version.

The Interactive Bi-Criteria Linear Programming System (IBCLPS) uses the Zionts and Wallenius approach to determine the optimal solution. The problem consists of two objectives: maximization of sales volume and maximization of net income. These are functions of seven decision variables – advertising, price, commission, quality control, the production volume in regular and second shift. The constraints relate to capacity of plant, financial resources, product price ceiling, minimum volume requirements and the fact that production should at least equal the sales volume.

<table><tr><td>MAIN MENU</td></tr><tr><td>1. CREATE A NEW BI-CRITERIA MODEL2. ALTER AN EXISTING MODEL3. DISPLAY DIRECTORY OF EXISTING MODELS4. SOLVE MODEL5. REPLACE MODEL ON DISK6. QUIT</td></tr><tr><td>TO SELECT YOUR CHOICE:ENTER THE CORRESPONDING NUMBER (1-6)ORENTER THE FIRST LETTER (C,A,D,S,R,E)</td></tr></table>

Fig. 3. Screen 2 in IBCLPS Execution.

It is assumed that the user knows how the decision variables affect the objectives and has little or no knowledge about computer programming or MCDM modelling.

The user accesses the IBCLPS and is given the menu shown in Figure 3. The choice is based on numbers or the first letter of the alternatives.

After giving the name of the model to be altered or created, use of the screen in Figure 4 illustrate a worksheet based on the data provided by the user – the number of objectives, the number constraints, and the number of decision variables. In this problem, 9 rows are created to accommodate 2 objectives and 7 constraints. Similarly, 7 columns are created for the 6 decision variables and the right hand side values. The display, at any one time, is limited to 9 rows and 5 columns of information (that is, excluding the titles of columns and rows).

Several function keys are provided to the user to move back and forth between regular columns and RHS values (F1), changing the signs of the constraints (F2), introducing names for column or row (F3 and F4) and adding or deleting columns and rows (F7 to F10). F6 key is provided for specifying upper bounds and F5 provides the means to get back to main menu. Warnings are issued to protect the user from specifying incorrect values or exceeding the defined dimensions.

Based on his knowledge of the organizational situation the user specifies how the objectives are affected by the decision variables. Thus, if the user believes that the sales volume is linearly related to

<table><tr><td rowspan="2">ROW NAME</td><td>sales</td><td>COL NAME</td><td>adv</td><td></td><td></td></tr><tr><td>adv</td><td>price</td><td>comsn</td><td>quality</td><td>RHS</td></tr><tr><td>sales</td><td>0.756</td><td>-275.543</td><td>525.847</td><td>0.028*</td><td>0.000</td></tr><tr><td>income</td><td>-1.000</td><td>10000.000</td><td>-10000.000</td><td>-1.000*</td><td>0.000</td></tr><tr><td>CON2</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000&lt;</td><td>21000.000</td></tr><tr><td>CON4</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000&lt;</td><td>21000.000</td></tr><tr><td>CON5</td><td>0.758</td><td>-275.543</td><td>525.847</td><td>0.028&lt;</td><td>0.000</td></tr><tr><td>CON6</td><td>1.000</td><td>0.000</td><td>10000.000</td><td>1.000&lt;</td><td>75000.000</td></tr><tr><td>CON7</td><td>0.000</td><td>1.000</td><td>0.000</td><td>0.000&lt;</td><td>55.000</td></tr><tr><td>CON8</td><td>0.000</td><td>1.000</td><td>0.000</td><td>0.000&gt;</td><td>37.500</td></tr><tr><td>CON9</td><td>0.758</td><td>-275.543</td><td>525.847</td><td>0.028&gt;</td><td>3000.000</td></tr><tr><td rowspan="2">ROW NAME</td><td>sales</td><td>COL NAME</td><td>prodn2</td><td></td><td></td></tr><tr><td>comsn</td><td>quality</td><td>prodn1</td><td>prodn2</td><td>RHS</td></tr><tr><td>sales</td><td>525.847</td><td>0.028</td><td>0.000</td><td>0.000*</td><td>0.000</td></tr><tr><td>income</td><td>-10000.000</td><td>-1.000</td><td>-31.430</td><td>-32.400*</td><td>0.000</td></tr><tr><td>CON2</td><td>0.000</td><td>0.000</td><td>3.700</td><td>0.000&lt;</td><td>21000.000</td></tr><tr><td>CON4</td><td>0.000</td><td>0.000</td><td>0.000</td><td>3.700&lt;</td><td>21000.000</td></tr><tr><td>CON5</td><td>525.847</td><td>0.028</td><td>-1.000</td><td>1.000&lt;</td><td>0.000</td></tr><tr><td>CON6</td><td>10000.000</td><td>1.000</td><td>0.000</td><td>0.000&lt;</td><td>75000.000</td></tr><tr><td>CON7</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000&lt;</td><td>55.000</td></tr><tr><td>CON8</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000&gt;</td><td>37.500</td></tr><tr><td>CON9</td><td>525.847</td><td>0.028</td><td>0.000</td><td>0.000&gt;</td><td>3000.000</td></tr><tr><td colspan="6">F1: RHS/ F2: SIGN/ F3: COLUMN NAME/ F4: ROW NAME/ F5: MAIN MENU</td></tr><tr><td colspan="6">F6: UB/ F7: +ROW/ F8: +COLUMN/ F9: -ROW/ F10: -COLUMN</td></tr></table>

Fig. 4. Screen 4 in IBCLPS Execution.

TO SELECT YOUR CHOICE
USE THE KEY TO MOVE THE POINTER RIGHT
USE THE KEY TO MOVE THE POINTER LEFT
USE THE ENTER KEY (CARRIAGE RETURN) TO ENTER YOUR CHOICE

<table><tr><td>sales</td><td>3000.002</td><td>5675.678</td></tr><tr><td>income</td><td>431759</td><td>344132.6</td></tr><tr><td></td><td>CHOICE 1</td><td>CHOICE 2</td></tr></table>

Fig. 5. Screen 5 in IBCLPS – Presentation of Alternatives.

IF YOU ARE FINISHED, REMOVE THE DISK FROM DRIVE A, TURN OFF THE COMPUTER. TO RESTART THE PACKAGE, PRESS THE CTRL, ALT, AND DEL KEYS SIMULTANEOUSLY

THANK YOU FOR USING IBCLPS

<table><tr><td>sales</td><td>4471.625</td><td>4337.841</td><td>4204.057</td></tr><tr><td>income</td><td>383564.5</td><td>387945.8</td><td>392327.1</td></tr><tr><td></td><td>CHOICE 1</td><td>CHOICE 2</td><td>CHOICE 3</td></tr></table>

END OF SEARCH, CHOICE 2 IS OPTIMAL  
Fig. 6. Final Screen in IBCLPS Solution.

advertising, price, commission and quality control, this relationship is input in terms of the effect of each variable. Here, we used a linear regression model to determine the relationship.

The constraints are easily developed by specifying the appropriate values of each decision variable. For example, the CON2 constraint refers to the capacity constraint in first shift. The total available capacity of 2100 units is indicated in RHS and the fact that each unit of production takes up 3.7 units of capacity is entered such under 'prdn 1', which is the affected variable.

Figure 5, shows how the user is presented with two alternatives. The choice made here gives the direction for the program to search for appropriate other choice leading to optimal solution. The program determines the two efficient solutions and presents them to the user for choice. As seen here, the user can choose either lower sales volume and higher net income (Choice 1) or higher sales volume at the expense of net income (Choice

![](/api/attachments/PTVAC6TH/fulltext/images/30878cd695e7d4b89220fab1a44de7ad079fcecce8f19cd605a74f55d270bfed.jpg)  
Fig. 7. Objective-function Space in the Bicriteria Problem.

2). For this illustration, we chose Choice 2.

Based on this preference, the program now searches for and presents two choices – one of them being the choice made now and the other with even higher sales volume but at the cost of net income being more than halved. We chose the latter, again indicating we did not prefer to lose any more profit. From this point onwards, the program has only to determine the end values searching for all possible combinations between these choices.

The program now searches for several alternatives to narrow the choice and finally converge on the solution. At each stage now three choices are presented to determine the direction of movement at the next stage. The final table is shown in Figure 6.

The successive steps taken in the algorithm before converging to the most preferred solution (the optimal solution) are illustrated in the objective-function space of the bicriteria problem in Figure 7.

This demonstrates the ease with which such programs can be handled by the user. The increased attractiveness is a direct result of using such PC innovations as a spreadsheet. Furthermore, the choices are entered easily by use of a few keystrokes, thus minimizing the need for extensive knowledge of the computer or the need for interfacing with a programmer specialist.

## 8. Conclusion

The decision situation described here very closely approximates that of real life organizations. The problem which involves six objectives, is quite complex and needs some form of decision support for its solution. MCDM offers a unique method of combining qualitative assessment of the user with management science techniques. We have described the MCDM approach and a decision situation to demonstrate the feasibility of the application of such a method.

We have also shown that a PC based software can easily be developed to increase the acceptability of such complex models for strategy formulation in real life organizations.

## References

[1] Constantine, L. and Yourdon, E., Structured Design, Yourdon Inc. (1978).

[2] FitzGerald, J., Business Data Communications - Basic Concepts, Security and Design, John Wiley and Sons (1984).

[3] Jelassi, M.T., Jarke, M. and Stohr, E.A., “Designing a Generalized Multiple Criteria Design Support System”, Journal of Management Information Systems, Vol. 1, No. 4 (1968).

[4] Jensen, R.L., and Cherrington, D.J., Participant's Manual: Business Management Laboratory, BPI, 1977.

[5] Keen, P.G.W. and Scott Morton, M.S., Decision Support Systems - An Organizational Perspective, Addison-Wesley (1978).

[6] Keeney, R.L. and Raiffa, H., Decisions with Multiple Objectives: Preferences and Value Tradeoffs, John Wiley and Sons, New York (1976).

[7] Mouzelis, N.P., Organization and Bureaucracy: An Analysis of Modern Theories, Aldine Publishing: Chicago, 1977.

[8] Quinn, J.B., “Strategic Goals: Process and Politics”, Sloan Management Review, Fall 1977, p. 21–37.

[9] Tom Demarco, Structured Analysis and System Specification, Yourdon Inc. (1978).

[10] Zionts, S., “Multiple Criteria Decision Making: An Overview and Several Approaches”, Working paper No. 454, School of Management, State University of New York at Buffalo (1982).

[11] Zionts, S. and Wallenius, J., “An Interactive Multiple Objective Linear Programming Method for a Class of Underlying Nonlinear Utility Functions”, Management Science, Vol. 29, No. 5 (1983).

[12] Zionts, S. and Wallenius, J., “Recent Developments in Our Approach to Multiple Criteria Decision Making”, in Grauer, M. and Wierzbicki, A.P. (Eds.), Interactive Decision Analysis, Lecture Notes in Economics and Mathematical Systems, Springer-Verlag (1984).
