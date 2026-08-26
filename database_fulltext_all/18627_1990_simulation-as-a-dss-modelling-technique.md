---
otero_id: 18627
otero_key: "8YTNXU2S"
title: "Simulation as a DSS modelling technique"
authors: "A.K. Aggarwal"
year: "1990"
journal: "Information & Management"
doi: "10.1016/0378-7206(90)90044-i"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Research

# Simulation as a DSS modelling technique

A.K. Aggarwal

University of Baltimore, Baltimore, MD 21201, USA

Technological advances of the 1980s have changed the ways managers are using information to make decisions. Advances in management science and improvements in information technology are allowing decision makers to use techniques that were previously unavailable and/or limited to mainframes. This paper discusses the use of one such technique, simulation, to model the non-steady (transient) behavior exhibited by many business applications. The paper also develops a model-centered DSS that uses a simulation technique to model the task environment. This model-centered DSS is then used to develop a scheduling system for the credit department of a retail store.

Keywords: Model-centered DSS, Modelling Interfaces, Simulation, Transient Systems, Application.

![](/api/attachments/8YTNXU2S/fulltext/images/189a41aad91e61f85ee0e037a2217cba21e415ae19c12f63552e22faaccf5835.jpg)

A.K. Aggarwal is an Associate Professor in the department of Information and Quantitative Sciences at the University of Baltimore. He received his B.Tech(hons) from Indian Institute of Technology, India and his PhD from University of Houston. His articles have appeared in various publications such as Decision Sciences, Journal of System Management, Decision Support Systems (transaction) and Interface. His research interests include decision-making models, expert systems,

## 1. Introduction

More and more managers are becoming comfortable with the information provided by Decision Support Systems (DSS). Given this, it is not surprising that DSS arc being demanded and developed to support various phases of the manager's decision making process. With the move towards model-centered systems, the DSS builders are increasingly focusing on sophisticated management science and statistical techniques $[1,6,22]$ to model the task environment.

Decision models are becoming important as the focus shifts from data-centered to model-centered DSS (A data-centered approach uses data and associations between data to develop complex or large report oriented DSS, whereas a model-centered approach uses decision models as the building blocks for DSS). In fact the current literature $[10,12]$ clearly suggests that it is the models that are the stable entities of the system and should be the basis of data and dialog subsystem design. This is especially true when the task environment is relatively stable. Some applications of model based DSS have been reported in the literature, for example, O'Keefe and Wade $[17]$ describe a DSS for a sawmill operation, Veddar and Mason $[21]$ describe an expert system based DSS for law enforcement in hostage-taking incidents and Blakely and Evans $[5]$ describe a DSS which uses a set of difference equations to manage supplier/distributor relationships. Linear programming (LP) and regressions are the most widely used modelling techniques. However, many business situations do not conform to the restrictions imposed when using LP: they are either too complex or do not map to a linearable problem. In such cases it is necessary to resort to simulation; it permits controlled experimentation with an unlimited number of different combinations. For example, in waiting-line systems, simulation involves representation of a queuing system with time sequence of arrival and servicing activities. Not long ago, simulation required significant expenditure of time, capital, and resources – both human and computer, but this is changing. Technological advances in the 1980s have made simulation techniques cost-effective and feasible on microcomputers.

## 2. Model-Centered DSS

A DSS is defined as a computer centered system which integrates data and decision models to support semi-structured decision making in a user-friendly environment. This set of capabilities is usually defined in terms of a dialog-data-model $[20]$ system. The data subsystem provides relevant data in the desired format to the user (manager and/or model subsystem), the model subsystem analyzes and interprets data by using decision models, and the dialog subsystem provides user-friendly interface with the system. In a model-centered DSS, the model subsystem is the building block and data and dialog subsystems are derived from it.

## 2.1. The Model Subsystem

The objective of a model subsystem is to model the decision environment, provide sensitivity analysis ('What-If') support and thereby help improve user effectiveness. The modelling tool should be simple to use, flexible, and as realistic as possible. Also, it should be free of any arbitrary and restrictive assumptions and be able to analyze different business scenarios. Advances in management science are making it feasible to model complex tasks while economics of information technology $[3,4]$ is allowing implementation at a reasonable cost.

Since the model subsystem is the core of this DSS, it is logical to emphasize the modelling-interfaces with other components of the DSS. We define the following interfaces.

(1) Model-user interface. This is probably the least studied but most important interface for model-centered DSS. One frequent criticism of the lack of use of models is the complexity and time involved in learning the model. However, this interface can automate many of the modelling features while providing flexibility; it should allow a decision maker to define complete unit models (unit models are parts or elements of the global model that intra- or interact) and their synthesis without assistance from experts. In addition, this interface should allow users to specify model parameters and their values and model interrogations ('What-If' or 'trade-off' analysis).

For effective model usage the following capabilities are needed through a model user interface:

(a) Synthesis: Which unit models can be synthesized in what situations?

(b) Solution Techniques: Which solution techniques are appropriate for the synthesized model?

(c) Solution (Inference): What output is expected when the model is solved?

(d) Backtracking: Why are the results as they are? (referred to as backtracking)

(e) Interrogation: What happens If the parameter(s) are changed?

(f) Selection: What is the best course of action?

(2) Data-model interface. Although transparent to the user, this is required for efficient functioning of the system. Its primary purposes are to store and maintain appropriate data and to transfer it from model to database and vice-versa. The following capabilities are needed:

(a) Data Maintenance: What are the most efficient data structures for input data (system data, cost data and other data required to formulate the model)?

(b) Data Transfer Mode: How can data be appended to the model (usually dictated by the software used)?

(c) Output Data Structure: What are the efficient structures for model output (any information needed for decision making)?

## 2.2. The Data Subsystem

The data subsystem together with the data-model interface is used for data storage, maintenance, and input to the modelling subsystem. Its key function is to provide flexibility in terms of

-Input data;

-Data maintenance;

-Future expansion.

Input data flexibility is very important in some systems. For example, in transient systems probability distributions of input variables, as well as their associated parameters change over time. The database subsystem should be flexible enough to handle time-dependent data (e.g., the probability distribution of interarrival time may be exponential from 1pm–2pm and uniform from 2pm–3pm, etc.). Data maintenance requires normalization which has been discussed extensively in the literature [8,15]. The overall strategy should be to construct a data base containing all data relevant to the current and future situation.

(3) Data-user interface. Though not a necessity for successful model implementation, it is essential for flexibility and adaptability. The purpose of this interface is to allow users to input system and transactional data (e.g., cost data), to provide maintenance (addition, deletion, and modification) of data elements and to provide data look-up capabilities.

The data-user and the model-user interfaces are usually combined into a dialog subsystem.

## 2.3. The Dialog Subsystem

The dialog subsystem provides a system interface with the user. Some potential problems arise. First, the users may not be familiar with simulation methodology. This necessitates an interactive 'What-if' analysis capability. Second, the number of variables in the model may be very large and require a user friendly input/output environment. Finally, to get hands-on experience, interactive query and model solution capabilities are desirable. The dialog subsystem requirements can be summarized as follows:

## A. User Friendliness

\- Menu-driven data maintenance

-On-line input/output

–Easy start-up procedures

—On-line help system and detailed documentation

\- Popular user-oriented software

-Graphical capabilities

-Natural language interface

\- Interactive sensitivity and trade-off analysis

B. System Flexibility which allows for
-Input data
-Values of controllable variables
-Alternate business scenarios

## 3. Simulation as a Modelling Technique

Management problems commonly arise from business systems in which people, materials, or machines wait for some type of servicing or processing; i.e., whenever a flow of arriving traffic establishes a variable demand for service at facilities of limited service capacity.

Operator scheduling has been an important planning and control issue for many firms and agencies. Often, the financial well-being of departments within these companies depends on the accuracy of scheduling, since such information will be used to make interrelated budgetary and operative decisions on personnel, finance, and management. Any significant over- or underscheduling of operators may cause the department to be burdened with excessive operators cost or create lost customer revenues as they depart due to long waiting time, especially for consumer and service oriented industries.

Management's objective is to select a ‘best’ operating scheme: one that maintains an economic balance between waiting time and service capacity. Meeting this objective requires a practical and effective analytical solution, i.e., of predicting delays reduced at specific arrival and service capacity levels. As one would expect, difficulty in determining a solution increases with the scope and complexity of different types of waiting-line systems.

## 3.1. Need for Simulation

In many problems the same levels of arrival rates and service capacity are maintained during a specified period. In other problems one or both may vary from interval to interval. Such variations require a period of system operation to be a sequential chain of transitional states of system loading: these are usually termed transient systems.

Recently various standard analytical techniques have been developed for solving special types of waiting-line problems [14]. In a transient business environment, it is not possible to determine the minimum number of operators needed to provide a given service level using traditional queuing techniques. In the non-steady state, the probability distribution associated with objects (e.g., customers) may change with time, thus the modelling tool should be able to handle such transients. A queuing model appears to be the appropriate choice, but there are no analytical or numerical solutions available for GI/G/C models [11] [though analytical solutions are available for M/M/1].

## 3.2. Simulation-centered model

A typical simulation model consists of data collection and analysis, the simulation process, and output analysis. Data analysis deals with any partially or totally uncontrollable information. The purpose of simulation, then is to provide optimal or best policies for controllable variables by studying the behavior of the model in light of uncontrollable variables. Figure 1 shows the various components of the simulation model in terms of a scheduling system.

## 3.2.1. Data Collection and Analysis

The data needed (i.e., customer interarrival time or operator service time) must be collected from external and internal sources. It should then be analyzed to fit various probability distribution functions using goodness-of-Fit techniques [7]. For non steady systems, data analysis may be based on some time unit. For example, an hourly schedule if the manager feels that the input information changes hourly.

## 3.2.2. The simulation process

Figure 2 shows a simplified schematic diagram of the operations of a scheduling process.

![](/api/attachments/8YTNXU2S/fulltext/images/e8ade7d6adea3f10c762381b3c085a24aebf1973ba8ebe353cafc3fd3c2d5887.jpg)  
Fig. 2. Schematic of Operation of a Scheduling System.

The actual simulation depends on the transition conditions $[16,18]$ and a basic time unit. The basic time unit updates the state of the system when an event occurs. For example, a single queue waiting-line system has two events that change the state of the system: arrival of a customer and completion of service. The state of the system for a credit department, as these events occur, is shown in Figure 3(a) and 3(b) respectively.

![](/api/attachments/8YTNXU2S/fulltext/images/aac0552cec6811c4fa8d071a54b9365ade9e5a433a04c218a175806eb0ebd724.jpg)  
Fig. 1. Pertinent Characteristics of a Scheduling System.

![](/api/attachments/8YTNXU2S/fulltext/images/1fa295e77b4f8d1e63e473f4f7f9d74018a4f12e9fdf1f82113269f94d5500de.jpg)  
Fig. 3(a). Schematic Diagram of a Banking System Upon Customer Arrival.

In transient systems, scheduling may differ from day to day, therefore the system must be designed to simulate daily operations (Monday through Saturday) with different interarrival rate for each hour, or other selected interval.

## 3.2.3. Output Analysis

Since the simulation model is a representation of some real life process, it can be used repeatedly to examine management alternatives, i.e. to study the effects of different inputs, model changes, or perturbations. Usually two studies are performed: on the simulation process itself (sensitivity) and in 'trade-off' or 'what-if' analysis, which provides [20] the desired management support.

![](/api/attachments/8YTNXU2S/fulltext/images/a5f0b363d9364b189df6276a4c17765961dfbe4c5d6e7d094165cbdd200287d3.jpg)  
Fig. 3(b). Schematic Diagram of a Banking System Upon Service Completion.

‘What-If’ analysis varies the system parameters and/or input variables and observes the model behavior. It can determine the effect of a different interarrival time or service time distribution or the effect if the queue length is restricted. Trade-off analysis involves studying the behavior of the system for different policies and management objectives. For example, a company may have policies that a customer should not wait for more than 5 minutes and that the facility should be busy at least 70% of the time. Since different policies may provide different recommendations, management must use its own judgement in making final decisions. The simulation model, therefore, should only be used as a supporting tool and not as an end in itself.

## 4. An Application

The credit department of a retail organization is responsible for checking credits for its local retail outlets. A check is made whenever a credit sale is made and the account is overdue, overdrawn, or delinquent. Because of the nature of the business, the demand fluctuates throughout the day (e.g., sales may increase during lunch hour or after office hours).

## 4.1. The Decision Environment

Historically, the credit department had 4 operators and the scheduling was arbitrary; it often resulted in significant under/over operator utilization. The manager was not certain whether to add new operators or retrain some. For any proposed operational configuration he was interested in answering the following questions:

A. What is the maximum/average time a customer has to wait before being serviced?  
B. Is the operator utilization efficient?

C. How will the proposed system handle demand fluctuation and future growth?

The following information was provided by the manager:

A. Approximately 20% of the credit card sales are referred to the credit department for a credit check.

B. Approximately 50% of the customers leave if the waiting time is too long (manager was not sure what too long meant).

C. There is no difference in service time at any time of the day or the week.

D. Units were serviced on a first-come first-served basis.

## 4.2. The Model Subsystem

Since the decision environment changes by the hour, it is transient in nature. The simulation model transactional information (specification) is:

<table><tr><td>System</td><td>: Credit checking system</td></tr><tr><td>Object</td><td>: Customer</td></tr><tr><td>Attributes</td><td>: Customer account/Credit check</td></tr><tr><td>Entities</td><td>: Operator</td></tr><tr><td>Service activity</td><td>: Check credit status</td></tr><tr><td>Events</td><td>: Arrival of a customer, Service completion, and termination condition</td></tr><tr><td>State variable</td><td>: Number of customers in the system</td></tr><tr><td>Duration of Simulation</td><td>: 39600 intervals (11 hours)</td></tr><tr><td>Input data</td><td>: Customer interarrival and service time distribution</td></tr></table>

## 4.2.1. The Data

Data concerning credit card sales were extracted from the computerized sales log maintained by the central processing department. Interarrival time between credit card sales was analyzed; it revealed several factors

A. There is no significant difference in the customers' calls on Tuesday, Wednesday and Thursday of the week (i.e., these days could be treated similarly).

B. There is no significant difference in the customer calls between 9 am–11 am and 2 pm–4 pm on any day of the week except Saturday.

The data did not fit any of the tested distribution (normal, exponential or uniform) and, therefore, an empirical distribution was used.

## 4.3.2. The Simulation Process

The credit system was simulated with input data and parameter values provided by the user. Once initial results are available, the system can be interrogated and the results graphed.

## 4.3.3. The Output

Output analysis is based on the following objectives and policies:

## Management policies

\- At any given hour average operator utilization should not be less than 60 percent.

\- On the average a customer should not wait more than 5 minutes (approximately).

Management Objective

\- Minimize operating cost.

## 4.4. The Data Subsystem

Since the manager was not familiar with simulation, it was necessary to provide an interactive user-friendly system. The data subsystem provides the hourly probability distribution function. The appropriate data are automatically selected for a given business condition and day of the week.

## 4.5. The Dialog Subsystem

The system is fairly self contained and requires little knowledge of the software. Currently it has the following features:

\- User friendliness:

\- Menu-driven data maintenance

\- On-line help system

\- Easy start-up procedures

\- Interactive model input/output

\- Popular user-oriented commercial software

\- System flexibility allowing for:

\- Constant, exponential, uniform or empirical distributions for interarrival time

\- Exponential, constant, uniform or empirical distributions for processing time

\- Model simulation with varying number of operators (1-99).

![](/api/attachments/8YTNXU2S/fulltext/images/c031b5230af6d242e8aa913048f6310da1e0794ae6e292a011417ca6801352d8.jpg)  
Fig. 4. An Integrated System for the Credit Department.

\- Different business scenarios

\- Business as usual

\- +10% or +20%

\- -10% or -20%

\- Interactive trade-off analysis between operator schedule and:

\- Operator utilization

\- Waiting time (maximum/average)

\- Number in the queue (maximum/average).

## 4.6. The Model-Centered DSS

Once the subsystems were specified, they were developed on commercially available software. The database subsystem used RBASE5000 $[9,13]$ , the dialog subsystem used LOTUS123, and the simulation model $[2]$ used BASIC. All the interfaces were developed in the command mode. Figure 4 shows the interfaces which integrate the three subsystems.

Currently the system has the following interfaces:

Data-user interface: Allows data maintenance (add, delete, and modification) and look-up through a menu system.

Model-user interface: Allows user to specify model parameter values (number of operators and credit check time distribution) and 'What-If-analysis with tabular and graphical representation of output.

Data-model interface: Allows data to be transferred from the database to the simulation model.

The system has the following limitations:

\- The process of accepting raw data (i.e., actual arrival times), fitting various probability distribution functions, and updating is not automatic.

\- There is no natural language interface.

## 4.7. System Operation and Decision Marking

The first step in operation involves selection of the credit check environment (input to the modelling system). A typical selection is structured as a vector Q1:

Q1 = (Business Scenario, Day of the week).

Once the business and day (for example, “business as usual” and “Monday”) are selected (menu driven) the corresponding data tuple is transferred from the data base to the simulator. The selected tuple contains probability distribution and associated parameters for hourly customer interarrival time.

Next, model entities and processing time is selected through vectors Q2 and Q3:

$Q2 = (\text{Number of operators from (I) Number of operators to (J)})$

Q3 = (Credit check processing time distribution, parameters of the distribution)

For example, the user may want to simulate the system for 2,3,4...8 operators with “normal service time” distribution. In this case I is 2, J is 8 and the service time distribution as “normal.” Selection (interactive) completes the model specification.

The simulator then runs the model for 11 hours and results for average operator utilization, maximum/average waiting time, and maximum/average number in the queue for each value in the selected range are stored as a class of matrix R given by

$\mathrm{Ri} = (\text{Hour of the day, Range of servers}),$

where i = I...J. Then the system performs trade-off analysis. It provides an operator schedule (interactively) by the hour for various user provided policies (e.g., average operator utilization = 80%, maximum number in queue = 3, etc.). The results are then transferred to LOTUS 123 through the model-output interface and presented in the desired mode using LOTUS123 (this requires knowledge of LOTUS123).

The final step involves interpretation of the results and making a scheduling decision.

Appendix A through E provide a graphical summary of the output as applied to the following system specification and management policies:

System specifications:

Q1 = (Business as usual, Friday)

$$
\mathrm{Q} 2 = (1, 6)
$$

Q3 = (uniform, 120,400)

Management Policies:

1. Average operator utilization should be between 40 and 60 percent.

2. Maximum customer wait time should not be more than 10 minutes.

3. Average waiting time should not be more than 5 minutes.

4. Maximum number in the queue should not be more than 5.

5. Average number in the queue should not be more than 3.

An examination reveals that the DSS provides different schedule for different policies. For example, it suggests 3 operators (Appendix A) between 5pm–6pm for policy 1 (cost efficiency), 5 operators (Appendix B and C) for policy 2 and 3 (customer goodwill) and 2 operators (Appendix D and E) for policy 4 and 5 (customer goodwill). The manager now must make a scheduling decision, for 5pm–6pm for business as usual on Friday, based on the priorities of these policies, or some other subjective or intuitive criteria.

## Conclusion

This paper has presented a model-centered DSS of scheduling systems. Recognizing that decision makers are concerned with the economic and the non-economic implications of their decisions, it suggests simulation techniques to model the non-steady state of the business and heuristic to supplement simulation results to make final decisions. This framework was tested and implemented for a scheduling system for a credit department and is currently being tested for a major bank.

DSS, however, is not a panacea for all the business problems. Its purpose is to provide support and not replace effective decision making. As with any system or technique, managers should not use simulation techniques or the DSS if they do not understand the model, assumptions and its limitations.

Appendix A  
![](/api/attachments/8YTNXU2S/fulltext/images/e17347c47d64b3ef36c963be5feb284c2c570d61bf13ca2ad6c32bfb84af7c1d.jpg)  
Appendix B

![](/api/attachments/8YTNXU2S/fulltext/images/aaa68243b644d650a966c40be744cd33ad72ac230be613035ef7db2d0bd6ef07.jpg)

Appendix C  
![](/api/attachments/8YTNXU2S/fulltext/images/4323d7f33f4120c568e4bea267934b93a976c28085005da0b557d55c71420dbc.jpg)

Appendix D  
![](/api/attachments/8YTNXU2S/fulltext/images/d65db21a1cb23922faf9a27e1dc05cb63cce9a9d59d25539da5124a66e35c58f.jpg)

## Appendix E

![](/api/attachments/8YTNXU2S/fulltext/images/eeae31ad28edddbf5a6d8e0450762f9c4c0bb9b76ba1c5ebcbc0b31d66cce63a.jpg)

## References

[1] Avramovich, D., Cook, T., Largston, G.D. and Sutherland, F. “Decision Support System for Fleet Management: A Linear Programming Approach”, Interfaces (1982).

[2] Banks, J., and Carson II, J.S., Discrete-Event System Simulation, Prentice-Hall International Series in Industrial and Systems Engineering, USA (1984).

[3] Benjamin, R., Rockart, J., Morton, Scott and Wyman, John, “Information Technology: A Strategic Opportunity”, Sloan Management Review (1984).

[4] Benjamin, R. and Morton, S., “Information Technology, Integration, and Organizational Change”, Interfaces (1988).

[5] Blakely, D., and Evans, Stuart, “Managing High Technology Supplier/Distribution Relationships”, Fifth International DSS-85 Conference on Decision Support Systems, DSS-85 Transactions, Sponsored by IADSS, USA (1985).

[6] Christy, D.P. and Watson, M.J., “The Application of Simulation: A Survey of Industry Practice”, Interfaces (1983).

[7] D'Agostino, R.B. and Stephens, M.A., Goodness-of-Fit Techniques, Marcel Dekker Inc., USA (1986).

[8] Date, C.J., Relational DataBase: Selected Writings, Addison-Wesley Publishing Company", USA (1985).

[9] Dinerstein, Nelson T., R: base5000 for the Programmer, Scott, Foresman and Company, USA (1986).

[10] Dolk, D.R., “Data As Models: An Approach to Implementing Model Management Decision Support System”, Decision Support Systems (March 1986).

[11] Gross, D. and Harris, C.M., Fundamentals of Queueing Theory, 2nd edition John Wiley & Sons, USA (1985).

[12] Konsynski, B. and Spraque, Jr. H.R., “Future Research Directions in Model Management”, Decision Support Systems (March 1986).

[13] Kroenke, D.M. and Nelson, D.E., Database Processing for Microcomputers, SRA Inc., USA (1986).

[14] Law, A.M. and Kelton, W.D., Simulation Modeling and Analysis, McGraw-Hill Inc., USA (1982).

[15] McFadden, F.R. and Hoffer, J.A., DataBase Management, The Benjamin/Cummings Publishing Company, USA (1985).

[16] Nance, R.E., “The Time and State Relationships in Simulation Modeling”, Communication of the ACM (1981).

[17] O'Keefe, J.B. and Wade P.F., "A Powerful MIS/DSS Developed for A Remote Sawmill Operation", MIS Quarterly (1987).

[18] Overstreet, C., Michael, C. and Nance, Richard C., A "Specification Language to Assist in Analysis of Discrete Event Simulation Models", Communications of the ACM (1985).

[19] Shannon, R.E., Long, S.S. and Buckles, B.P., “Operation Research Methodologies in Industrial Engineering”, AIIE Transactions (1980).

[20] Sprague, R.H. and Carlson, E.D., Building Effective Decision Support Systems, Prentice-Hall, USA (1982).

[21] Veddar, Richard and Mason, Richard, "An Expert System Application for Decision Support in Law Enforcement", Decision Sciences (1987).

[22] Wallace, P.C., “Decision Support Tools for Analyzing Automated Manufacturing Systems”, CIM Technology (1985).
