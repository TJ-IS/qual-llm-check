---
otero_id: 18303
otero_key: "BEJ3C6RT"
title: "Logic-based decision support for computer capacity planning"
authors: "Stephen D. Burd; Suleiman K. Kassicieh"
year: "1987"
journal: "Information & Management"
doi: "10.1016/0378-7206(87)90020-6"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
pear in Operations Research, OMEGA, Information & Management, California Management Review among others.

# Logic-Based Decision Support for Computer Capacity Planning

Stephen D. Burd and Suleiman K. Kassicieh
Anderson Schools of Management, University of New Mexico
Albuquerque, NM 87131, USA

This paper reports on a decision support system for computer capacity planning. The system is currently under development for Sandia National Laboratories to support planning in an environment characterized by large scale scientific as well as more traditional administrative computing needs, governmental budgetary limitations, and specific planning documentation required by the funding source. The implementation vehicle for this system is an extended version of Prolog which allows interactions with externally defined computational routines and sources of data. This provides for the integration of various data sources with a set of models for estimating capacity requirements and optimizing different objective functions subject to budgetary constraints. This paper outlines the decision environment, pointing out the benefits of using a DSS to support management in forecasting user requirements and optimizing their supercomputer acquisitions, subject to cost, time, financial options and user needs.

Keywords: Artificial intelligence, PROLOG, DSS, Logic programming, Models in A.I.

![](/api/attachments/BEJ3C6RT/fulltext/images/4b4be376cd83993a620cbc5026a90dd569313ab77d0ef24247e7d4879210122d.jpg)

Stephen D. Burd is Assistant Professor of Management Information Systems at the Anderson Schools of Management, University of New Mexico. He earned his Ph.D. in management from Purdue University in 1983. He is a Certified Public Accountant (licensed in Maryland).

His current research interests are the application of artificial intelligence techniques to the design and implementation of decision support systems and accounting information systems.

Other research and teaching interests include database management systems, natural language processing, systems analysis and design, and auditing.

This research was supported by Sandia National Laboratories Grant No. 56-3737. Sandia is managed by AT&T Technologies for the U.S. Department of Energy.

## 1. Introduction

Advances in theoretical and technical research on decision support systems research have augmented their requirements considerably. The ideal decision support system (DSS) has evolved into a system which allows users to interact directly with models and data in order to formulate hypotheses, test them against 'live' organizational data, and make decisions based on the test results. In order to make these systems easy to use, they must also represent modeling knowledge and data semantics to relieve users from the burden of specifying the procedural details of model usage or data retrieval and its interpretation.

This paper describes a DSS that aids the management of a large national laboratory in developing long range plans for computer capacity acquisition and budgeting. The system will be referred to as the CCP-DSS (Computer Capacity Planning DSS). Ultimately, the issues faced in its building will aid in the development of more generalized Dsss which use logic programming (Prolog) as a vehicle for accessing different types of knowledge bases containing data, decision rules, and models.

The paper presents a model-based DSS used by the decision-makers in planning and responding quickly to changes. The system includes a number of alternative quantitative techniques that support the varied tasks that comprise long range planning. The system also allows the use of “what if” scenarios of budgets and computer capacity.

![](/api/attachments/BEJ3C6RT/fulltext/images/68352930c3981f01f19fc4e88f7d5bd625edfd31d20ae58828d07810df805225.jpg)

## 2. The Decision Environment

Sandia National Laboratories (SNL) are managed by AT&T Technologies for the U.S. Department of Energy (DOE). Funding for the labs passes through the U.S. Congress as part of the U.S. Budget. The computer capacity planning decision-making process covers a moving period of eight years. In the current year (year n), information about expenditures for years n-1 to $n+6$ are examined with respect to costs and requirements in future years.

The planning process starts with the user departments or divisions specifying their computer capacity needs. These needs are translated into NSU (nominal standard units) or RCU (relative capacity units), and eventually to dollar figures by considering current machine class costs. Estimates of required computer capacity for individual departments are derived by department managers, who are given wide latitude in their choice of methods and facts to support their requests. The process is initiated by providing individual managers with their estimates and actual utilization for current and prior years. A few of the department managers choose structured models (e.g. regression, time-series, etc.) but the majority choose more ad hoc methods. A manager will typically estimate future capacity requirements by projecting past usage. These projections may be adjusted due to the introduction of new technologies (e.g. engineering departments have experienced a sharp rise due to hardware and software needs in computer-aided design) and due to periodic shifts in the scope and/or importance of each department's work.

Once derived, individual estimates must be aggregated. The lab-wide estimates are then used to plan for additional equipment taking into consideration:

1. The capacity of existing machines available for purchase (the national labs use a standard guide to obtain these figures).

2. The manufacturer's estimated capacity of yetto-be-introduced machine(s). For example if a new Cyber is estimated by Control Data Corporation to have 4 times the capacity of the Cyber 205, then 4 times the RCU or NSU capacity of the Cyber 205 is used for the new machine.

3. Financial options of different buying and leasing strategies.

4. Maintenance, labor, peripherals, and other costs, including overhead.

5. A learning curve, applicable to new environments, which assumes that a new machine or a new operating system will not provide full capacity at the time of installation, but provides roughly 50%, 75%, and 100% in the year of introduction, second, and third years respectively.

The management of SNL seeks to balance the budgetary, technical, and department needs through the planning process. For example, they would like to examine a scenario in which all of the user requirements are satisfied, but the financial outlays for the total cost of machines and operations follow a slight upward trend, such as an increase of 3–5% in real terms, rather than an irregular spiked pattern. Such scenarios require the generation of several different types of budget analyses, used to assess the effects of different budget objectives and the effect of change in the constraints imposed by management, the user departments, the DOE and the U.S. Congress.

Once the user department capacity estimates have been obtained and aggregated, summaries are entered in a spreadsheet which models the entire budget (6-year plan). This model can then be manipulated in several ways, such as changing acquisition plans, purchase/financing options, learning curve assumptions, etc.

The planning process for meeting user capacity needs is carried out using this basic model and by applying a series of “what-if” scenarios (e.g. what if we buy out our Cray a year early; what if our budget for year $n + 2$ is held to a 2% increase, etc.) as modifications to the spreadsheet. Those manipulations are initiated by managers in charge of the planning process and carried out by a staff member. The model may be used for purposes other than planning to meet user needs (e.g. it is often used to justify budget requests for future years). The total time devoted by the staff member to creating the initial model and making modifications for all of the scenarios is 1 to 2 person-months.

## 3. Modeling and Data in CCP-DSS

The management feels that the current system offers modeling capabilities that are too limited and are too slow in generating new scenarios and decisions. They would like to build a system that performs optimization without managers having to guess at good solutions and then check them using spreadsheet manipulations. They would like the new system to respond quickly to change, require less staff time, and provide support to the managers of individual departments in order to increase the reliability of the capacity requirements estimates.

The complexity of computer capacity planning arises from the multitude of factors that require consideration and examination. These are both internal and external to the organization. External factors include technological changes that affect cost or capacity, and programmatic changes that affect the amount of funding available for issues that the U.S. Government deems important for national security and economic viability. Internal factors include support and administrative facilities, maintenance, and staff availability, among others.

At first glance, the task of planning appears to be straightforward. In most instances, the budgeting process is performed via a “naive” planning model that increases last year’s capacity by a certain percentage. This procedure greatly simplifies the job in the short run but causes problems in the long run, due to the effect of changing technology on capacity and cost and the difficulty in obtaining capacity increases in the desired increments (especially in the acquisition of supercomputers).

Naive planning models work well under totally static conditions. Past demand reflects future demand as long as conditions in the environment remain stable. This assumes that the number of employees and research programs remain unchanged, budgetary conditions are similar, and, perhaps most importantly, demand for scientific research (quantity and quality) never changes from year to year. But, due to technological and social pressures, this has not been the situation in the national laboratories.

Computer capacity management is an unstructured activity. Kleijnen [13] maintains that technical performance of a computer system is usually an issue of efficiency but it cannot nevertheless be separated from the study of its effectiveness. He points out also that although the technical performance measurements using formula timing, simulation, or other quantitative techniques are highly structured, the economic evaluation of computer capacity is very unstructured. In today's environment, predicting technological development over the next six years, as the laboratory's capacity planning model tries to do, is very difficult indeed.

Howard [9,10] indicates that there is no widely accepted definition for computer capacity management. EDP Performance Review [8] defines it as a set of functions concerned with determining and maintaining the balance between costs and benefits of the system, taking into consideration its workload, throughput, response time and reliability. Bronner [6] lists the variables that need to be considered in capacity evaluations. They are:

1. CPU utilization

2. software utilization

3. utilization of channel control units

4. transactions per unit time

5. total number of transactions

6. average response time for each transaction

7. average response time for each class of transactions

8. number of execute channel program instructions per transaction

9. number of execute channel program instructions per class of transactions.

Stevens [20] indicates that the service objectives of timeliness, accuracy, cost, and reliability are important in evaluation of computer capacity management. He points out that the goal is not to achieve 100% utilization, but rather an acceptable level of service such that the system is meeting the needs of the users.

Another major consideration is the cost of computer capacity. International Data Corporation [11] tracked trends in computer budgets in U.S. organizations. They identified six major groups of costs: personnel, hardware, media and supplies, software, outside services, and communications. Personnel and hardware make up about two-thirds of the cost but are on a downward trend, whereas all other costs are going up. Total cost is also linked to financial considerations of buying or leasing, external or internal maintenance contracts, and bundling or separating equipment such as peripherals and memory devices.

Data for all the above variables is rarely available, and even if it were, its collection and utilization in modeling would be a difficult and time consuming task. For the purposes of national labs, the externally imposed requirements of specifying capacity needs in NSUs or RCUs largely negates the need to consider a large number of capacity variables.

For SNL, it is sufficient to model the planning process in terms of present and future capacity requirements (in NSUS or RCUs), current capacity and its associated cost, and the capacity and cost of acquisition alternatives. This is more complex than it may appear at first, as configuration options must be considered in deriving capacity and capital needs, and various types of operating costs must be considered in specifying total costs.

The modeling for the CCP-DSS is of two distinct types. The first is in the form of prediction models for estimating the future capacity requirements of individual departments. Such a model using regression can be specified as:

$$
\boldsymbol {Y} = (\boldsymbol {a} \boldsymbol {X} + \boldsymbol {b}),
$$

where Y is a vector of capacity utilizations for previous years, X is a matrix of past values for predictor (independent) variables, a is a vector of slope coefficients, and b is the intercept vector. Variables a and b allow the prediction of future capacity needs based on past experience and the model can be implemented via any multiple regression software. The estimates of capacity may be adjusted subjectively by the user to account for a fundamental shift in technology or other changes.

The second type of modeling is for optimization. The planning process can be described as a maximization of user capacity needs subject to budget constraints. Thus the objective function represents the summation of attainable user capacity requirements while the constraints represent limitations in operating and capital budgets and machine costs. The constraints are complex, in that they must cover the entire six-year planning horizon as well as the financing/purchase requirements for each machine. The model can be implemented in its entirety as an integer programming problem.

## 4. Decision Support for CCP

Models for planning support are widely known and available, yet there has been little application of them in real planning problems. One reason for the lack of actual applications of these management science models is often in their narrow and limited problem scope. While being theoretically satisfying, several models offer application to only a very small problem subset. Another reason for limited application of some models is their macro-system approach, resulting in the fact that they are of little use for short or intermediate term planning. Few have addressed themselves to the problems of the planning unit. Models have also been static in nature, with no capability for update or revision as actual system conditions vary. Finally, these models often fail to consider the information needs of the user. Thus, while the analysis is theoretically proper, models are often an academic exercise rather than a problem-solving one.

Keen and Scott Morton [12] and Sprague and Carlson [19] maintain that dsss offer the concepts and methodologies to exploit available technologies, thereby applying computers and mathematical modeling to the decisions faced by management. According to Alter [1], dsss are beneficial because they:

1. allow quick access to information otherwise unavailable,

2. enable the use of explicit modeling capabilities that provide structure for a particular decision, and

3. facilitate communication among people and/or organizational units whose work must be coordinated.

A DSS framework must consider the identification of the decision-maker, the real decisions to be made, the required information, and the necessary output format of the results. Implied in this framework is the realization that the resulting system will support the managers responsible for making and implementing decision rather than replacing the manager with some sort of automated decision-maker.

The CCP-DSS supports the laboratory's planning and budgeting efforts by providing a structured and useable access to prediction and optimization models. It provides these models in order to:

1. allow planners to assess the effect of changing

costs, technologies, budgets and user needs.

2. provide forecasts of computer capacity demand in future time periods.

3. provide information on the effect of changes, such as introduction of new technologies, different research programs, and new budgetary constraints.

4. allow decision-makers to examine the sensitivity of the solution to changes.

5. allow planners to estimate and anticipate the effect of political and economic changes.

The management decisions that are supported can be categorized into two groups; the first is the determination of an acquisition budget; the second is the justification of a budget proposal for periods in the intermediate 2–6 year planning horizon. To support the first activity, the DSS allows the users to:

1. establish the usage requirements for the next planning horizon by using regression, time series, and other models.

2. determine the best schedule for the purchase of machines over the next six years to satisfy different objectives. These objectives serve to create the different scenarios used by management to choose the best alternative.

3. compare the current requirements to the budgeted amounts so as to postpone the acquisition of lower-ranking requirements. If the requirements exceed the budgeted amount, the system produces a list of alternative schedules that satisfy the requirements by shifting between different financing arrangements or by postponing certain costs. If the budget exceeds requirements (a rare occurrence but nevertheless logically possible) the system will suggest a combination of financial options that will bring purchases to the budget limits, such as memory or machine buyouts ahead of schedule.

## 5. System Implementation

In order to develop a system such as this, it is necessary to choose a development tool that allows the necessary models and data to interact easily with one another. Other desired features of such a tool are its ease of implementation, its ability to represent knowledge for model manipulation, and the ease with which a system constructed using it can be modified to accommodate future changes, such as additions of new models or databases.

Numerous researchers have examined the use of how logic may be used as a basis for DSS development and to provide intelligent capabilities for model selection, model interpretation, and data handling. Bonczek et al. [4] demonstrated the formulation of model selection via first order predicate calculus (FOPC) and used resolution to answer queries within that system. Reiter [18] and Kowalski [14] examined the use of resolution as a basis for answering queries to a database represented via predicate calculus. Minch and Burns [16] present a “model management” technique for linking the database and the models through a problem processing system.

Blanning [3] describes three current approaches to model-based management and decision support systems. The first approach involves applying techniques of artificial intelligence. Examples of such approaches include the use of and/or graphs and the use of resolution to answer queries expressed in FOPC. The second approach involves extending the CODASYL database model to include information describing the characteristics of stored models and the interface between the database and such models. The third approach utilizes the relational database model and views a model as a relation with attributes representing input and output parameters. The first and third approaches form the basis of model representation and manipulation in the CCP-DSS.

Prolog was chosen as the basis for implementation of the CCP-DSS due to its ability to incorporate all of the logical and relational representations developed in the above mentioned research. In terms of the components of a DSS as defined by Bonczek, Holsapple, and Whinston [5], the Prolog resolution mechanism is the problem processor, and the logical representations of models, data, and knowledge of their use and interpretation constitute one component of the knowledge system. In order to complete the knowledge system, the predicate representations of data and models must be further defined in terms of actual model computations and data retrieval.

## 5.1 Model Interfaces

In the case of models, definition in terms of logic is seldom practical. Although many Prolog implementations (including the one used for this system) provide a rich set of mathematical operators, their expressive power and efficiency makes their use for representing complex calculations impractical. Thus, a facility for defining model calculations in non-logical terms is required and must be integrated with the logical representation used within Prolog. This is accomplished by allowing the Prolog interpreter to make use of procedural attachments.

The idea behind a procedural attachment is simple. It allows a computational (or other type of) routine to be represented as a predicate, using its input and output parameters as arguments (variables). When such a predicate is encountered in the course of resolution, the actual values of the input parameters are passed to an external routine for the model (e.g. a precompiled FORTRAN program). The external routine is then allowed to run to completion and the output parameters are passed back to the logic system and bound to the corresponding variables in the predicate representing the program. Such a facility provides the opportunity to incorporate existing or newly developed procedural programs into the logic system without having to recode the procedures in terms of logic (e.g. provide the capability of a system such as SAS by implementing calls to it rather than recoding SAS in Prolog and incorporating it into the code of the DSS).

In the CCP-DSS, procedural attachments are implemented through a programmed facility which allows the Prolog interpreter to execute an external program as a spawned (child) process. Parameter passing is physically realized through the input/output piping facilities of the operating system. Input parameters are extracted from the predicate representing the procedure and passed to the external program. Output parameters are passed back and bound to corresponding Prolog variables. This was the method used to allow the Prolog interpreter to execute models defined within the statistical package 'S' [2].

In addition to the code necessary to execute a model, the system contains a substantial amount of code devoted to the selection of appropriate models, the formulation of model parameters, and the interpretation of model outputs. This coding is designed to allow untrained users to use sophisticated models to support their decision making activities. Additional coding is also provided to allow utilization of the contents of the database in modeling activities.

An example of these capabilities is the portion of the system devoted to estimating computer capacity needs for individual departments. Since department managers are seldom trained in the use of prediction models, the system is designed to facilitate their use of such models by guiding the user through the selection of an appropriate model, the selection of data upon which to base a prediction, and the interpretation of the results of model execution. These capabilities are provided by an interface to the multiple regression model of the 'S' statistical package. Some of the more important features of this interface are:

1. The user is totally insulated from the specific command language. All interactions are guided by questions from the system. The user's answers to these questions guide that system in constructing a syntactically and semantically valid regression call to S.

2. The user is presented with a set of available data for use in prediction (the contents of the historical database). The user can choose any subset of this data (e.g. decide to base the prediction on five years of past data for the number of users in the department and its budget). The user may also enter data not contained in the database (this can be incorporated into it if the user wishes).

3. Along with the normal regression parameters (slopes and intercept), relevant regression statistics are returned to the system by S (e.g. R-square, F, and T values). These parameters are interpreted by the system and the user is informed (in English) of these interpretations; e.g. a low R-square value causes the system to inform the user that “the results are unreliable” and that “a new model (new set of predictor variables) should be selected”.

4. In the event of a successful model run (i.e. high reliability with all predictor variables relevant) a prediction formula is automatically constructed. The user is then queried for the expected values of the predictor variables and an estimate is derived.

The user is not restricted to using only estimates derived from models, but is free to modify these estimates or to bypass them entirely. Thus, the user is not constrained to prediction based on historical data in situations where such a constraint might lead to inaccurate results.

The use of integer or linear programming is guided by the system, allowing the user the flexibility to specify decision variables, the objective function, and constraints and providing the user with the solution to the scenario examined.

## 5.2 Data Interface

The number of implementation choices available for data interfaces is greater than the number of options for models interface. As has been shown, queries against a database represented in terms of predicates can be formulated in terms of FOPC and answers generated via resolution. Thus, it is possible to utilize Prolog's inherent pattern matching and deductive capabilities to answer queries against internally stored data. Database modification capabilities can also be implemented in Prolog via the 'assert' and 'retract' predicates.

Such an implementation is practical for small databases with simple retrievals. However, when large amounts of data are to be stored and/or complex queries are to be made against the data, the Prolog resolution and matching facilities tend to be inefficient. In such cases, it is desirable to 'subcontract' the work of data management to a program specifically designed for these tasks (i.e. a database management system (DBMS)). This is the approach used in the DSS-CCP.

Although it is possible to generate queries deductively against a network database [7], the interface between predicate logic data representations and a relational database is much cleaner. Thus, INGRES was chosen because of its relational characteristics and availability within the UNIX environment. The INGRES interface consists of a set of generalized data manipulation predicates. The generalized predicates are implemented as procedural attachments which pass the generated command(s) to INGRES.

## 5.3 User Interface

User interfaces are as important to the DSS as the other components. The power of logic programming makes a wide range of options available for implementing this interface. As demonstrated by Pereira and Warren [17] and McCord [15], implementation of natural language interfaces in Prolog is quite feasible.

If the goal of a DSS implementation is to make the capabilities of the DSS general and usable in a wide range of areas, a natural language interface might be desirable and necessary. In the CCP-DSS, however, the application of the models and data represented is narrowly defined. Thus, the use of more structured interfaces is easier for the user and more efficient in terms of system resources. Therefore, the users' input and output interfaces are tailored to the specifics of the problem, the data inputs required, and the output desired by the user for internal use, as well as the output required by external entities (i.e. governmental funding agencies).

The bulk of the interface is constructed as menu (or list) selections and questions asked of the user. Menus are used at the top levels of the system in order to direct the user to the subsystem(s) appropriate to his needs. List selection is used where all options available to the user can be derived (e.g. when a list of variables in the database is presented to the user). Question and answer interfaces are used extensively in the formulation (and reformulation) of models and parameters.

The system allows the user the option of presenting information in graphical form. This capability can be used both to plot existing sets of data or to display model generated results (e.g. predictions for the entire planning horizon).

## 6. Conclusions

The development of the CCP-DSS is an attempt to provide sophisticated model-based support to a complex planning and budgeting process. The optimization portion of the system has been installed and tested by the users but has not yet been used in an actual planning cycle. SNL has delayed testing and installation of the predictive portion of the system until the optimization portion has been successfully utilized.

Improved input to the long range planning process should be obtained by the application of models to the prediction of individual departments' capacity requirements. As discussed previously, few managers had previously approached this problem with tools any more sophisticated than simple extrapolation based on previous years' capacity utilization. Such extrapolation may still be used in the current system, but it can be conducted in a statistically rigorous manner via a simple regression based on time.

The availability of stored modeling knowledge to guide the user in the formulation of more complex prediction models provides the opportunity for a department manager to improve predictions via statistical techniques that may have been previously unknown or unavailable. This modeling capability is further supplemented by a database interface which makes it possible to extend the bases of the predictions. Although the interfaces to these capabilities are user-friendly and require virtually no training, it remains to be seen whether or not they will gain widespread acceptance.

As regards the generation of the long range plan, improved decision-making should result both from increased confidence in the capacity needs estimates provided by department managers and from the application of optimization modeling. The model currently used is simply a spreadsheet containing total capacity requirements, existing capacity, and planned capacity acquisitions. Optimization (providing the maximum capacity within budget constraints) cannot be performed in a reliable or rigorous manner. Possible acquisition scenarios must be added to the model by hand, the model recomputed, and the results checked for feasibility.

The CCP-DSS will support this facet of the planning process by providing access to an optimization model, thus negating the need for the iterative hit and miss approach used previously. It also considers all factors simultaneously (budget, capacity, learning curve, and financing options). Changes in parameters and recalculation can be performed much more quickly than was previously possible. The combination of speed and reliability provides management with the ability to perform more analyses with less effort and should provide a higher level of confidence in the final result.

User reactions based on test of this portion of the system have been favorable. The decrease in time required for optimal solution has been identified as the primary advantage of the new system. Suggestions by SNL managers for improvements were made in the areas of text manipulation of the results, downloading results to spreadsheet software, and the user interface to the database.

Significant advantages in development time and system flexibility have been realized by the utilization of logic-based tools (Prolog and extensions) as opposed to more conventional implementation language tools. These arise both from the inherent power of logic programming as well as the incorporation of modeling and database capabilities via relational representations.

The use of such relations within a logic programming system allows all of the power of logic programming to be utilized for model selection, formulation of inputs, interpretation of results, and data manipulation. This power is apparent not only in the ability to program such tasks in Prolog, but in the efficiency with which any such task can be programmed (e.g. the current regression interface is less than 100 lines of Prolog code and should be less than 250 lines in the final version). This also results in a considerable reduction in programming time over more traditional programming tools.

The use of procedural attachments also provides economy in programming effort as well as a great deal of system flexibility. The ability to use “off-the-shelf” software for computational models and database processing restricts the programming effort associated with these tasks to input/output translation and output interpretation. New models can be added with a minimum of effort, provided programs for the models are available in the implementation environment.

## References

[1] Alter, Steven L.: Decision Support Systems: Current Practice and Continuing Challenge, Addison-Wesley, Reading, Massachusetts, 1980.

[2] Becker, R.A. and Chambers, J.M.: An Interactive Environment for Data Analysis and Graphics, Wadsworth, 1984.

[3] Blanning, R.W.: A Relational Framework for Join Implementation in Model Management Systems, Owen Graduate School of Management Working Paper, 1983.

[4] Bonczek, R.H.; Holsapple, C.W., and Whinston, A.B.: "A Generalized Decision Support System Using Predicate Calculus and Network Data Base Management", Operations Research, vol. 29 (1981), pp. 263–281.

[5] Bonczek, R.H.; Holsapple, C.W. and Whinston, A.B.: Foundations of Decision Support Systems, Academic Press, 1981.

[6] Bronner, L.: "Overview of the Capacity Planning Process for Production Data Processing", IBM Systems Journal, vol. 19 (1980), pp. 4-27.

[7] Dutta, Amitava, and Amit Basu: Deductive Query Processing in a CODASYL Database, Krannert Graduate School of Management Working Paper, Purdue University, December, 1983.

[8] Capacity Management and Software Physics, EDP Performance Review, vol. 7 (1979), pp. 1.

[9] Howard, P.C.: "Capacity Management and Planning (part 1)," EDP Performance Review, vol. 8 (1980), pp. 1–7.

[10] Howard, P.C.: “Capacity Management and Planning (part 2),” EDP Performance Review, vol. 8 (1980), pp. 1–7.

[11] International Data Corporation: “Trends in Computing: Application of the 80's,” Fortune, May 31, 1982, pp. 21–30.

[12] Keen, P.G.W. and Scott Morton, M.S.: Decision Support Systems: An Organizational Perspective, Addison-Wesley, Reading, Massachusetts, 1978.

[13] Kleijnen, J.P.C.: Computers and Profits: Quantifying Financial Benefits of Information, Addison-Wesley, 1980, pp. 28–29.

[14] Kowalski, R.: Logic for Problem Solving, North Holland, 1979.

[15] McCord, M.C.: “Using Slots and Modifiers in Logic Grammars for Natural Language”, Artificial Intelligence, vol 18 (1982), pp. 327–367.

[16] Mich, R.P., and Burns, J.R.: “Conceptual Design of a Decision Support System Utilizing Management Science Models”, IEEE Transactions on Systems, Man, and Cybernetics, vol. SMC-13 (1983), pp. 549–557.

[17] Pereira, F.C.N., and Warren, D.H.D.: “Definite Clause Grammars for Language Analysis – A Survey of the Formalism and a Comparison with Augmented Transition Networks”, Artificial Intelligence, vol. 13 (1980), pp. 231–278.

[18] Reiter, R.: 'On Closed World Data Bases', in Logic and Databases, Gaillaire, H., and Minker, J. (eds.), Plenum Press, 1978.

[19] Sprague, R.H., Jr. and Carlson, E.D.: Building Effective Decision Support Systems, Prentice-Hall, Englewood Cliffs, New Jersey, 1982.

[20] Stevens, B.A.: “Audit and Control of Performance in Data Processing,” EDP Performance Review, vol. 8 (1980), pp. 1–13.
