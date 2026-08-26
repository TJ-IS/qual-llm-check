---
otero_id: 18763
otero_key: "NMWHCHNK"
title: "A knowledge-based approach for improving information and decision making in a small business"
authors: "Jerrold H. May; William E. Spangler; Richard E. Wendell; Hartmut U. Zaun"
year: "1991"
journal: "Information & Management"
doi: "10.1016/0378-7206(91)90063-8"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
SOS

# A knowledge-based approach for improving information and decision making in a small business

Jerrold H. May, William E. Spangler and Richard E. Wendell

Joseph M. Katz Graduate School of Business, University of Pittsburgh, Pittsburgh, PA 15260, USA

Hartmut U. Zaun

Thermal Industries Inc., Pittsburgh, PA 15221, USA

This article describes the development of a prototype knowledge-based decision support system for a small manufacturing company. The prototype was designed to aid in the diagnosis and resolution of various production problems, as well as to assist in the collection and recording of information required for improved management decision making, as the first step toward a fully-integrated, real-time expert system for production management. The project illustrates a number of auxiliary issues and lessons arising from the development of the prototype system. These include: (1) the effectiveness of a multiple-expert approach in modeling the knowledge that comprises the system, (2) the need for prototyping during the incremental system development process, and (3) the growing impact of inexpensive software development tools and microcomputers on the ability of small companies to develop and implement highly-specialized knowledge-based systems.

Keywords: Decision Support Systems, Knowledge-based Systems, Systems Development, Production Management

![](/api/attachments/NMWHCHNK/fulltext/images/ab68e8cd655f1762b7cd796bffce8d1b73c9f28e6b6b78b3f872e2264fabb536.jpg)

Jerrold H. May is an associate professor and co-director of the Artificial Intelligence in Management Laboratory at the Joseph M. Katz Graduate School of Business, University of Pittsburgh. Prof. May has a Ph.D. in Administrative Sciences from Yale University. His current research interests are in the use of artificial intelligence and expert systems approaches, together with management science techniques, to solve managerial problems.

## 1. Introduction

Decision Support Systems (DSS) are ostensibly designed to improve decisions by assisting in the

![](/api/attachments/NMWHCHNK/fulltext/images/d2ffa8a73d787b590a6f401b30b947e63273832517d219d0265a8829d123a72f.jpg)

William E. Spangler is currently a Ph.D. candidate in the Katz Graduate School of Business at the University of Pittsburgh. He holds an MBA from the University of Hawaii, and has seven years of experience in the computer industry. Mr. Spangler has worked at Westinghouse Credit Corporation and Burroughs (now Unisys) Corporation, and has consulted for a number of other companies, including several Fortune 500 firms. His research interests focus on the applica-

tion of artificial intelligence to strategic decision making.

![](/api/attachments/NMWHCHNK/fulltext/images/329d609be5e34b10cc53ac442a3e3b5f833e6637dbb86cb0074172bdd5934802.jpg)

Richard E. Wendell is Professor of Operations Management in the Katz Graduate School of Business, University of Pittsburgh. After receiving his Ph.D. in Operations Research from Northwestern University, Prof. Wendell held positions at the Argonne National Laboratory, Ohio State University, Carnegie-Mellon University, and Rensselaer Polytechnic Institute. He was also in residence at the European Institute for Advanced Studies in Management (Brussels), and was a research associate at the Center for Operations Research and Econometrics, Catholic University of Louvain. His publications and current research interests include work in sensitivity analysis, location analysis, multiple objective optimization, voting theory, and applications of operations research.

![](/api/attachments/NMWHCHNK/fulltext/images/d337147efa53b45fd30b4e05035d866eaf0c922f4a5fd6f954efac887b7e07c7.jpg)

Hartmut U. Zaun holds a BS degree in Meteorology from the Pennsylvania State University and an MBA from the University of Pittsburgh. He has thirteen years of management experience, the last seven of which have been with Thermal Industries, Inc. His first position with Thermal was as the Production Manager of the Extrusion Department. He currently serves as the corporation's Systems Manager, with primary responsibilities including profit analysis of sales and manufacturing, and the evaluation and application of emerging technologies to appropriate corporate operating divisions.

organization and evaluation of information. However, DSS that rely on inaccurate information may lead to poor decisions, and disastrous outcomes, regardless of the information technology being used. Thus, it is incumbent to insure that the relevant decision data are accurate and timely. Fortunately, a knowledge-based DSS can aid in the collection and verification of such data.

In this paper, we describe the development of a knowledge-based system prototype developed for Thermal Industries, Inc. We began the project described in this paper with two goals: (1) the development of a working prototype knowledge-based system that could actually be used by shop floor personnel, and (2) the education and training of MBAs in the development of such systems. The first goal was not attained because of our discovery, during the knowledge acquisition process, of the questionable quality of the data available to management. We expect to resolve this problem with a second stage project, beginning shortly, that will involve real-time monitoring of the production process. The second stage project should result in a fielded system which will be of significant value on the shop floor. Although the prototype, as delivered, was not useful to floor personnel, it, and the process involved in its structuring and implementation, provided substantial benefits to company management as well as to the students involved.

## 2. Thermal Industries

Thermal Industries is a small, Pittsburgh-based manufacturer of top quality custom vinyl-framed replacement windows. The window frames are formed through an extrusion process which is sensitive, at several steps of the process, to a variety of input and process variables, including temperature, throughput rate, and variability in the quality of raw materials (vinyl). The company's machine operators are responsible for setting up and monitoring production runs, and for correcting problems that may occur during an extruder production run. Due to the large number of variables that influence the manufacturing process, the operator's task is subject to error, which may result in costly delays and material waste.

Although a small company in absolute terms (annual sales of \$30 million, with 450 employees), Thermal is nevertheless the domestic industry leader in the production and sales of vinyl-framed replacement windows, and is highly motivated to retain its leadership in the face of increasing foreign competition. In response to the delays and waste described above and their potential effect on the competitiveness of the firm, the management of Thermal Industries began to explore the myriad factors that were impacting upon the extrusion process, and contributing to the production problems. Through improvements in its labor-intensive production methods, management estimated that it could increase production efficiency by 5 to 10 percent (measured by the expected reduction of wasted raw material), thereby increasing profits by 45 to 90 percent. The company could then pass these savings on to its customers, and significantly improve the competitiveness of Thermal products in the marketplace.

Toward this end, the company sponsored a project course at the Katz Graduate School of Business of the University of Pittsburgh. In that project, a team, composed of faculty and graduate students, worked with a liaison group from Thermal Industries, coordinated through a single manager at the company. The project team was asked to investigate all factors relevant to the reported problems, to present recommendations for action, and then to begin implementation of specific recommendations, subject to certain time constraints.

The project culminated in the development of a small, demonstration prototype knowledge-based system designed to assist machine operators in the diagnosis of the most common production problems. The prototype, with recommendations for extension of the basic system, was presented to Thermal management. In addition, the project team presented recommendations pertaining to data collection, data recording, and procedural documentation.

The accuracy, consistency and timeliness of the information used as the basis for production decisions ultimately became a key issue in the analysis, and a barrier to fielding the system in its current state.

## 3. A Prototyping Approach to System Development

The project team chose a prototyping approach for the development of the knowledge-based system. Researchers in systems development have described a number of potential advantages of the prototyping method, including enthusiastic users, improved communications between developers and users, increased accuracy in determining user information requirements, and a modular approach which allows implementation of validated portions of the system as they are developed and tested [1]. In a survey of information systems developers and users, Mahmood [11] described other perceived advantages of prototyping. These included greater flexibility in development, increased relevance of output to intended function, greater overall satisfaction among both developers and users, and increased likelihood of user implementation and acceptance of the system.

In addition to the generic considerations listed above, projects that involve the construction of knowledge-based systems are particularly appropriate for a prototyping approach. Because a knowledge-based system attempts to incorporate some aspects of observed human expertise, Weiss and Kulikowski [17, pg 106] advise that it is important for the expert to periodically verify the accuracy of the work-in-process so that suggestions and criticisms can be made based on a running prototype, rather than on something more abstract. They suggest that the prototyping approach creates a common focus for the expert and the systems developer, and thus accelerates the development process. Our experience demonstrates that the prototyping approach can help identify problematic issues in the knowledge acquisition process.

For these reasons, the project followed a composite prototyping approach based on somewhat similar methodologies prescribed by various researchers $[4,16,17]$ , and included the following stages:

1. Problem definition and information requirements.

2. Elicitation and formalization of an expert's knowledge.

3. Development of a computer model.

4. Validation of the computer model.

Steps 2, 3 and 4 were performed in an iterative manner, with model development and validation often requiring corrective feedback from the operators.

## 4. Background and Problem Definition

The project team began its work by clearly delineating the problem or problems facing Thermal Industries. The problem definition process began with the team holding a series of meetings with Thermal Industries personnel, including the Systems Manager, Production Manager, and various other production supervisors, operators, and technicians. Because the team and Thermal management both felt that the analysis and development should begin within a limited scope, Thermal management identified a particular production line (and window frame cross-sectional profile) which was not only used in a significant percentage of their product line, but was also a potential source of numerous delays and material waste. The idea was that if the problems involved with the single production line and cross-sectional profile could be successfully analyzed and solved, then the project could be expanded to include other production lines and cross-sectional profiles.

It soon became clear that the problem involved two distinct but interrelated elements of the production process: (1) diagnosing the existence of a production problem, which involved understanding the data used by the operators and management, and (2) given that a problem has been diagnosed, determining a strategy for remedying the problem. As a result, the project team was divided into two subgroups, each addressing one component of the process.

## 3.1. Data Collection and Recording

The data analysis subgroup studied the data collection and recording activities in the production process. Their aim was to discover how the data could be analyzed, through statistical regression and other techniques, in order to detect possible dependencies between certain variables in the production process.

The extrusion production environment was not conducive to timely and accurate recording of data. Periodic data concerning machine settings, sensor readings, and problems encountered (and any corrective action) were supposed to be recorded manually in a log book by the operator on duty. The log, which was designed to maintain a history of production activities, is used (1) by management in order to monitor the production process, (2) by operators in order to discover previous actions taken while attempting to solve a particular problem (because problem diagnosis and solution is often a trial-and-error process) and (3) by operators who may be attempting to ascertain how another operator may have successfully solved a similar problem.

The information actually recorded in the log book, though, tended to be somewhat sketchy, and subject to inaccuracies and inconsistencies. There were several reasons for this.

First, accurate data collection is most critical when a problem occurs, but that is exactly the time when an operator has the least opportunity to record it. When a problem occurs, the operator is under pressure to fix it as fast as he can, and cannot be expected to be able to remember all the various settings and adjustments he might be making. As a result, data collection activities often took place some time after a problem had been corrected. Second, because there was not a perceived pressing need to collect and record data at particular times when no problems were occurring, the activity was easily forgotten. As a result, data was often recorded late, if at all. Third, worker shift changes tended to produce discontinuities in the log book, as the workers attended to other activities at the end and beginning of each shift. Fourth, 'fudging' was apparently quite common. If an operator was late in recording the production status at a particular time, he might be inclined to record the 'correct' time and settings anyway. Fifth, an operator's recording of machine gauge readings would not always be accurate or consistent, since the reading of an analog gauge, in particular, is often subject to interpretation, and varies based on the experience of the operator. Finally, the tedious nature of the data collection process, particularly the reading of machine gauges, encouraged the operators to occasionally neglect the activity entirely, and to record the settings for the previous time period or the nominal, as opposed to the actual, settings.

These considerations made a thorough analysis of the data nearly impossible, and motivated the subgroup to search for methods for improving the accuracy of the recorded data. Discussions that centered on the feasibility of a computer-based data collection system resulted from the goal of improving the accuracy of the data, a task that is to be pursued this year.

## 3.2. Modeling Operator Problem Solving Behavior

The modelling subgroup studied the activities of machine operators in order to understand the problem solving strategies of the operators, as well as the consistency and the quality of those strategies across operators. The subgroup visited the production line, observed the operators' activities, and asked questions. Other information was obtained through semi-structured interviews with individual operators and production supervisors, questionnaires, as well as a variety of written documents.

The major goals of the subgroup were to (1) understand the generic tasks performed by operators, (2) identify and understand problems that can arise during the production process, (3) understand how the operators deal with those problems, (4) compare and contrast the methods used by different operators to correct similar problems, and (5) in coordination with the data analysis subgroup, identify the methods for gathering and recording production data.

## 3.3. Description of the Task

The modeling subgroup discovered that the operator's task is complicated, for a number of reasons. First, many of the production process variables are interdependent, with more than one variable contributing to a single problem. The operator must understand the one-to-many relationships between problems and input variables, and be able to adjust each of the relevant variables properly and in a timely manner.

Second, a significant time lag may exist between adjustment of the input variable(s) and change in the quality of the output, and the time lags might vary depending on the circumstances. While one adjustment may take five minutes to affect the process, another adjustment may take thirty minutes. Even in the presence of time and cost pressures, the operator must have the patience to wait for the adjustment to take effect.

Third, an initial adjustment (1) may not correct the problem, (2) may not correct it completely, or (3) may over-correct the problem. In addition, an adjustment may correct one problem, but replace it with another. Thus, the adjustment process is iterative, perhaps involving a number of minor adjustments of various input variables until the quality of the output is within specification.

The operators appeared to deal with the variables in a qualitative, as well as a quantitative, manner. The symptoms of many of the production problems would indicate to the operators the direction of a required adjustment to a variable, but not necessarily the magnitude of the adjustment. The speed of the extruder, for example, may initially be set at a specific value. In response to a problem, rather than adjust the speed to another designated value, an operator might instead simply 'go up' or 'go down' on the extruder speed, and then observe the results. If the problem was not corrected, the operator might continue adjusting and observing in an iterative, systematic manner until the problem was solved.

## 3.4. Data and Process-related Issues

Following the initial stage, the subgroups summarized the problems and circumstances that were to be addressed during the next phase of the project:

\- Collection and recording of data were somewhat inaccurate, inconsistent, and incomplete.

\- Methods used to correct production problems had not been standardized, or even recorded in a systematic fashion.

\- Different operators varied somewhat in their solutions to similar problems.

\- Individual operators tended to be more familiar with some problems than with others.

The first issue above argues for a more systematic and efficient data collection scheme. The remaining issues suggest that the methods for diagnosing and correcting production problems should be standardized and recorded in order to make the solution process more effective and efficient. After further discussions between Thermal Industries and the project team, it was agreed that a good first step for addressing each of these issues would be the development of a demonstration prototype knowledge-based system that might assist an operator in control of the extrusion process. The tasks necessary to program a knowledge-based prototype might aid in the standardization of operator actions by modeling key parts of their problem-solving methods, while also serving as a computer-based mechanism for collecting and recording historical data.

## 5. General Objectives of the Knowledge-Based Prototype

Because even experienced operators do not always follow the same decision path when problem-solving, a primary objective of the knowledge-based prototype was the creation of a computer model designed to assist production personnel. This model would help to define the ‘proper’ or ‘standard’ response to common production problems, and could serve as a uniform ‘institutional memory’ resource. Even when the prototype would be expanded to a full-fledged system, it was not intended to replace the operators, and would not be capable of doing so. Instead, it was designed to act as an ‘intelligent assistant,’ guiding the less-experienced operators, and serving as a resource for the senior operators. Furthermore, the eventual knowledge-based system could serve as a mechanism for collecting and automatically recording specific portions of the data that were currently recorded manually.

## 6. Elicitation of Operator Knowledge

The first step in the development of the prototype was to expand the scope of the operator interview and observation process in order to more fully understand the details of each problem and any corrective action taken. The goal of the rule elicitation stage was twofold.

First, designing and implementing an effective knowledge-based system, even a prototype, requires that the system developers understand and develop some level of expertise in the task being modeled. That expertise is important for the comprehension of the subtleties of a particular task, and for understanding the constraints that limit the scope of the computer model. The project team used the interviewing and elicitation process to extend their knowledge of the general Thermal Industries production environment, as well as the detailed aspects of the particular production line being studied.

Second, the knowledge elicitation process allowed the project team to record the problem diagnosis and solution process in sufficient detail so as to encode it into the if-then rules required by the software. They needed to model the hypothesis-driven reasoning processes of the operators.

In order to accurately record and represent the knowledge of the operators, the project team used small microcassette recorders to record operator statements. The recorders are unobtrusive, and did not seem to inhibit the operators from speaking. Later, the team formalized the operators' statements by carefully transcribing the recorded statements, as well as any other notes that were taken during interaction with the operators. After comparing responses among various operators, detailed follow-up interviews were arranged in order to clarify answers, and to resolve the differences in responses among operators.

Differences in responses were generally attributable to two causes: (1) experienced operators differed from novice operators, and (2) the multidimensional aspects of some problems led to differences in interpretation. That is, a single problem may have several manifestations, each requiring different actions. This led to a more finely-grained definition of some problems. The interviewing process also clarified other ambiguities, particularly in operator references to specific problems. A single problem may be described differently by different operators (for example, a problem called ‘twisting’ is referred to by some operators as ‘bowing’). In short, the team discovered that careful definition of the problem set is a critical step in the development of a prototype of this variety.

This task clarification and resolution process led to the discovery and formalization of a generic, consensus problem-solving strategy encompassing the combined heuristic knowledge of the various operators.

## 7. Designing the Knowledge-based Prototype

The design of the prototype system began with (1) the types of problems that had been discovered during the knowledge acquisition phase, and (2) the consensus solution processes used to solve those problems. The project team then developed a schematic representation of the solution process, in the form of a decision tree, for each problem.

Understanding the general diagnostic process in this way served to reinforce the shared opinion that a commercial expert system development shell tool would be the most appropriate vehicle for implementing the prototype and perhaps the final system. The observed problem-solving process was compatible with the backward-chaining reasoning mechanism used in many commercial shells. $^{1}$ The project team and Thermal management together selected VP-Expert, an inexpensive shell, from an extensive list of development tools that satisfied the following requirements:

\- An ability to rapidly develop modular, prototype systems. This is critical for the development of any knowledge-based system.

\- A ‘user-friendly’ development and user environment. The long-term viability of the system depended on a program that was relatively simple to learn, and convenient to use and to modify.

\- An ability to run on IBM (and compatible) microcomputers. This ensured compatibility with a wide-variety of microcomputers, including the PCs at Thermal Industries.

\- An ability to access external programs, files, and databases. This would be necessary in order to use the knowledge-based system as an automated mechanism for logging sensor data, and recording historical information.

Although the decision tree format for the operators problem solving process could have been accommodated using decision tree software, we chose to use an expert system package because of its ability to incorporate other analytical approaches, should they become necessary. VP-Expert, for example, can incorporate forward-chaining. In addition, it has the ability to induce backward-chaining rules from examples, which could be of value in validating the monitoring of the knowledge base over time.

## 8. Implementation of the Prototype

The general implementation strategy was to begin with the derived decision tree for each production problem, and then to incorporate each decision tree within the backward-chaining mechanism used by the commercial development tool.

## 8.1. Production Problems

The project team focused on specific problems that were common on the particular production line for the cross-sectional profile under investigation. These problems generally involved an extruded product (i.e., a portion of a vinyl window frame) that was not within certain quality assurance tolerances due to variations in one or more of the input variables (temperature, extruder speed, raw material mix, etc.).

The following problems were then incorporated into the knowledge-based prototype:

\- pinking: a condition in which a visible discoloration occurs in the vinyl of the extruded product. Pinking can range from 'slight' to 'severe', and corrective action differs depending on the severity.

lumps: the appearance of lumps or swellings in the extruded vinyl.

\- wall thickness; variations in the thickness of the vinyl frame (either the wall of the extruded frame is too thick or too thin in one or more places)

profile size: a class of problems in which the size of portions of the extruded product are not correct

\- small channel or large channel: variations in the size of the channel of the frame (i.e., the part of the frame that will hold the window)

\- surging: variation in the consistency of the extruded product's dimensions, caused by variation in the extruder output

\- sink marks: indentations in the extruded vinyl at the intersecting walls

\- twisting/bowing: the extruded frame is not straight; a condition caused by differential cooling of the profile

## 8.2. Software Development

The prototype was developed in a sequential fashion. We addressed each problem individually, encoding the solution process for each problem, and thoroughly testing the validity of the prototype's reasoning before moving on to the next problem.

During the encoding stage, the project team met frequently with Thermal operators in order to clarify ambiguities and resolve inconsistencies that were not previously apparent (under less rigorous circumstances). Our experience emphasizes the iterative nature of knowledge-based systems development, which frequently requires the developer to return to the knowledge elicitation stage, and the expert, for additional information.

## 8.3. Feedback

A limited initial prototype was made available to Thermal Industries personnel for experimentation and feedback. Because acceptance by the operators would determine the eventual success or failure of the project, we were particularly interested in comments regarding (1) the accuracy of the rule base and (2) its convenience and ease-of-use. We also emphasized the non-threatening nature of the prototype. The feedback process resulted in some minor modifications to existing rules, and enhancement of the rule base to include the remaining production problems.

## 9. Operation of the Knowledge-based Prototype

The diagnostic process employed by the operators begins with the appearance of a problem, and ends with a specific action or series of actions. The rules incorporated within the knowledge-based prototype system fit into this pattern, establishing a goal of finding an appropriate recommendation for corrective action. The prototype uses a recursive ‘hypothesize-and-test’ strategy in order to arrive at a conclusion.

A variety of factors enter into the decision process, including the severity of the problem and any variations, as well as previous actions that have been taken to correct this or other problems. The prototype follows the decision tree, testing the appropriate decision criteria until it concludes with a recommendation that is consistent with the context of the problem.

The prototype proceeds, using a generic hypothesis-driven strategy (see Figure 1), by requesting the needed information from an operator through a menu system, eventually reaching a recommendation. The recommendation is then displayed to the operator, along with other information, such as how long to wait before again trying to correct the problem.

![](/api/attachments/NMWHCHNK/fulltext/images/49fd6e40a1773413f36275fbe728ddb6143fd886a7979570237904b388d8bfa3.jpg)  
Fig. 1. The generic strategy for the knowledge-based system.

After displaying a recommendation, the prototype logs a record of its actions into an external database file. That history file includes information on the nature of the problem, the recommendation(s) for corrective action, and the time and date when the problem occurred.

## 10. Possible Extensions of the Model

During the final meeting between Thermal Industries and the project team, Thermal management expressed satisfaction with the functionality of the prototype, and, along with the team, discussed several potential avenues for future expansion of it to a full-fledged system. Because we followed a prototyping approach, the current prototype can be easily modified in order to expand its applicability and address other related production issues.

## 10.1. Expansion of the Rule Base

The current prototype contains 64 rules addressing eight generic problems that affect a single cross-sectional profile (a portion of one type of window frame). The particular profile was chosen because of its complexity and resulting propensity for problems. Consequently, in terms of the overall design goal realized by the prototype, Thermal management and technical staff estimate that the 64 rules pertaining to that profile encompass seventy to eighty percent of all known extrusion problems.

The prototype could be expanded to include the remaining problems pertaining to the other sixty active profiles. Some of the profiles, including the one used for this prototype, are used only on a temporary basis, and are then discontinued. Therefore, a comprehensive system that can address the common problems encompassing many different profiles will help to keep the eventual, fielded system current and relevant to the operators. Such a system might also prove especially valuable in keeping track of problems with low-volume profiles, with which even skilled operators might have only limited experience.

## 10.2. Integrated Reporting System

The machine operators keep a manual log of actions taken during production runs (including problems encountered, machine settings, type of profile, time, date, etc.). As mentioned earlier, the manual logs tend to be somewhat sketchy, because they may be treated as an afterthought on the part of the operator. Although the current prototype logs information concerning problems encountered, it could be enhanced in the fielded system, in order to more fully automate the current manual logging procedure. With historical information in a microcomputer database, a variety of valuable production reports might be produced. For example, a report could describe past production problems of a specific type, or past production runs made with a specific supplier's raw material.

## 10.3. Training

Artificial intelligence techniques, including knowledge-based systems, have been used as tutoring and training tools in other domains $[3,7,12,14,18]$ , and the Thermal Industries prototype has similar potential. Novice operators might use a fully-developed system in hypothetical environments, as well as on-the-job in dealing with real problems.

## 10.4. Expert Data Base

A fully-developed system might become increasingly sophisticated by utilizing its own database for the solution of new production problems. Although the current prototype relies solely on input from the operator, it could be augmented to include a knowledge-based analysis of historical database information. For example, the system could analyze prior trends and patterns that are related to a current problem, and incorporate this information within the current problem-solving context.

## 10.5 Real-time Knowledge-based System

Automated logging of critical input data, with a corresponding reduction in the number of operator errors, could be accomplished through an integration of the production machinery and a knowledge-based system. In this type of system, the computer would receive data directly from various sensors attached to the extrusion equipment.

The major initial benefit of using sensor data (as opposed to the operator's manual data recording) would be an increase in the accuracy and timeliness of input data. The system could be instructed to sample sensor data at regular intervals, and to store the received data directly into the database. When a problem arises, the system could look to its database in order to determine current machine readings, and then recommend action based on those accurate and timely readings. Because the readings would already be in the database, the system would not have to ask the operator as many questions. Questions would instead be limited to events that the system could not see, such as the problem itself. Ideally, the operator might choose a particular problem from the system's menu, and the system would respond, after checking its database, with an appropriate recommendation. With improved accuracy of historical data, production reporting, as well as trend analysis and other evaluations of the data, would be more accurate.

The prototype system, as well as its future offspring, illustrate many of the computer-based support issues involved in solving problems in time-dependent situations (i.e., in ‘real-time’). According to Laffey [9], real-time expert systems differ from ‘traditional’ expert systems with regard to the dynamic nature of their environment and their data.

Response times, for example, may be highly constrained, because changing events may require decisions within a specified time range. Furthermore, since information may be created, deleted, or updated on a continuing basis, recommendations and decisions based on the changing data may also have to change.

Although the above considerations may challenge attempts to automate more of the operator's task, and although the software technology is still new, real-time systems are becoming increasingly popular in a variety of domains requiring accurate information and timely response to problems. Such domains include process control environments, such as the one at Thermal Industries, which are particularly well-suited to real-time knowledge-based systems. Researchers and practitioners are developing a number of real-time systems in process control environments $[2,8,13,19]$ . To facilitate this trend, an assortment of general-purpose, real-time development tools have begun to appear, including shells that run on personal computers $[6,9]$ . Prior to the development of a sensor-based, real-time system at Thermal Industries, one of these PC-based shells would likely replace the current shell, which is not capable of automated data collection and reasoning in real-time situations.

The prototype development process has highlighted the potentially far-reaching evolution of an expert system within the process control environment of a small company. The discussion to this point has centered around a prototype and possi-

ble system that are primarily consultants, assisting in the collection and analysis of data, and recommending corrective action. Thermal management, however, has expressed a longer-term desire to extend the functionality of the prototype to include taking action, either by sensing a problem or by receiving input from an operator (ultimately, the goal is the former). This would, in effect, culminate the development process with the implementation of an automated, independent, production control expert system (see Figure 2).

![](/api/attachments/NMWHCHNK/fulltext/images/6106ce0821f7e229f4c22de0fcc6f6a114eadeb95d34271e668dc123567be93a.jpg)  
Fig. 2. Evolution of an intelligent production control system.

## 11. Continuation of the Project

Thermal management has approved continuation of the project through the development of a sensor-based diagnostic system, tailored to their environment. The project will continue in two stages. The first stage will involved the installation of equipment, including computer hardware and software, required to collect sensor information directly from the production machinery. This stage is expected to take approximately 4 months, and again will be undertaken jointly with University faculty and MBA students. The following stage will involve integration of the rule-based expert system, modeled on the prototype with appropriate modifications. Management estimates the cost of the integrated system to be roughly \$225,000, with a non-discounted payback period of 1–2 years.

By comparison, Thermal granted \$10,000 to the University for the prototype development project, which required approximately 4 1/2 months to complete. We should reiterate that the goals of the prototype development project, as recognized by both Thermal management and the University of Pittsburgh, included the education of MBA students, as well as the development of a prototype. Consequently, the figures for the prototype may be somewhat misleading. We estimate that an experienced knowledge engineer, such as a skilled doctoral student or faculty member, could have completed the project in about half the time.

## 12. Summary and Conclusions

The Thermal project illustrates some issues and lessons that can arise from a knowledge-based development project. The following are a sampling of the primary findings.

12.1. A consensus approach to modeling knowledge worked well in this particular environment

Experience among operators varied, not only in total years on the production line, but also in the specific problems that each had encountered. Follow-up interviews (often involving groups of operators) resolved the differences, and produced a consensus that could be encoded within the prototype system.

12.2. Prototyping is an appropriate vehicle for the incremental systems development approach chosen by the project team and Thermal Industries.

When the project began, the dynamic production environment at Thermal Industries represented a rather complex modeling task. Prototyping allowed us to implement portions of the code as they became ready. This, in turn, helped retain the interest of the users, because they could see (and use) the prototype as it was being developed. The more ambitious plans, such as implementation of a full-fledged, real-time system, could be implemented later. The entire prototype did not have to be designed and developed at once, and future changes could be implemented in a modular fashion.

12.3. Prototyping allowed a more accurate and responsive system.

Developers could arrange follow-up interviews with operators in order to clarify ambiguities, as well as to gather feedback concerning the ‘look and feel’ of the user interface.

12.4. The tool used to create the prototype was relatively easy to learn and use.

This facilitated several aspects of the project. First, the developers could concentrate on developing a working prototype rather than on trying to learn to use an obscure development package. Training of the implementation team was kept to a minimum. Second, the simple, menu-driven interface supported by the tool was judged easy to understand by the test users of the prototype, leading us to expect that a fully-developed system built on the same platform would be accessible to floor personnel. Third, Thermal Industries personnel could accept the prototype system at a certain stage of development, and then continue with its development after the project team had completed its work. Maintenance and future work could be accomplished by them as needed, and as time permitted.

## 12.5. The development tool was inexpensive, and capable of running on inexpensive microcomputers.

Considering the low cost and ease-of-use of the package, knowledge-based prototypes, and perhaps even full-fledged systems can be developed and implemented by small companies, such as Thermal, $^{2}$ that do not have the data processing budgets and specialized expertise of larger companies. Although small businesses have traditionally received less attention by IS researchers, they are nevertheless a vitally important segment of the U.S. economy, comprising nearly half of the nation's GNP [15]. Therefore, with the availability of inexpensive and increasingly convenient development tools, small businesses represent a large potential market for DSS in general, and knowledge-based systems in particular.

12.6. Although not intended as a mechanism for replacement of human experts, a knowledge-based project can nevertheless be used to increase the accuracy and timeliness of input data, as well as to increase the accuracy of information used by management for making decisions.

An automated data recording environment will not eliminate all data-related problems. In such an environment, the quality of the data may still be occasionally suspect, since one or more sensors may malfunction or fail from time to time. A rule-based approach is particularly sensitive to inaccurate data, and, in that sense, may not represent a robust model of human problem solving. Human expertise degrades more gracefully in the face of inaccurate, incomplete, or conflicting data $[5,10]$ . As a result, even a fully-developed system would likely only be useful in relatively clear-cut situations, and would, of necessity, require human intervention for complicated problems.

Nevertheless, a knowledge-based system can greatly improve the quality of information available to management. A PC-based, integrated real-time system, with generally accurate sensory data and modeled domain knowledge, might use its inferencing and information processing capabilities to provide management with sophisticated data analyses that were previously unattainable.

## Acknowledgements

This paper is based on an MBA student project, funded by a grant from Thermal Industries Inc. to the Katz Graduate School of Business, University of Pittsburgh. The following students were members of the project team: Jennifer Castor, Chris Danusiar, Craig Dean, Dave Feigel, Nick Florkowski, Melissa Kopko, Dave Olney, Jennifer Parr, Dan Peters, Linda Rapach, and Oliver Sachse. Richard E. Wendell and Jerrold H. May were the faculty project advisors, and William E. Spangler was the systems consultant. Representatives of Thermal Industries for the project were David H. Weis, Eric Rascoe, Hartmut Zaun, and William Yanyo.

## References

[1] Alavi, M., “An Assessment of the Prototyping Approach to Information Systems Development”, Communications of the ACM, Vol. 27, No. 6, 1984, pp. 556–563.

[2] Allard, J.R. and Kaemmerer, W.F., “The Goa]/Subgoal Knowledge Representation for Real-Time Process Monitoring”, Proceedings of the Sixth National Conference on Artificial Intelligence, 1987, pp. 394–398.

[3] Barzilay, A., An Expert System for Tutoring Probability Theory, unpublished PhD dissertation, Univ. of Pittsburgh, Pittsburgh, Pennsylvania, November 1984.

[4] Buchanan, B.G., Barstow, D., Bechtal, R., Bennett, J., Clancey, W., Kulikowski, C., Mitchell, T., and Waterman, D.A., “Constructing an Expert System”, in Hayes-Roth, F., Waterman, D.A., and Lenat, D.B., (editors), Building Expert Systems, Addison-Wesley, Reading, Massachusetts, 1983, pp. 127–167.

[5] Buchanan, B.G., and Smith, R.G., “Fundamentals of Expert Systems”, in Barr, A., Cohen, P.R., and Feigenbaum, E.A., (editors), Handbook of Artificial Intelligence, Vol. 4, Addison-Wesley, Reading, Massachusetts, 1989, pp. 149–192.

[6] CHRONOS Users Manual, Euristic Systemes, Clamart, France, 1989,

[7] Clancey. W.J.. “Dialogue management for rule-based tutorials”, Proceedings of the International Joint Conference on Artificial Intelligence, IJCAI, August 1979, pp. 155–161.

[8] D'Ambrosio, B., Fehling, M., Forrest, S., Raulefs, P., and Wilbur, B., "Process Management for Materials Composition in Chemical Manufacturing", IEEE Expert, Vol. 2, No. 2, 1987, pp. 80–89.

[9] Laffey, T.J., Cox, P.A., Schmidt, J.L., Kao, S.M., and Read, J.Y., “Real-time Knowledge-based Systems”, AI Magazine, Vol. 9, No. 1, 1988, pp. 27–45.

[10] Lenat, D.B., Prakash, M., and Shepherd, M., “Using Common Sense Knowledge to Overcome Brittleness and Knowledge Acquisition Bottlenecks”, AI Magazine, Vol. 6, No. 4, 1986, pp. 65–85.

[11] Mahmood, M.A., “System Development Methods-A Comparative Investigation”, MIS Quarterly, Vol. 13, No. 3, 1987, pp. 292–311.

[12] Mockler, R.J. and Dologite, D.G., Knowledge-based Systems for Strategic Corporate Planning, The Planning Forum, Oxford, Ohio, 1987.

[13] Nelson, W.R., “REACTOR: An Expert System for Diagnosis and Treatment of Nuclear Reactor Accidents”, Proceedings of the Second National Conference on Artificial Intelligence, 1982, pp. 296–301.

[14] Sleeman, D.H. and Brown, J.S., “Intelligent Tutoring

Systems: An Overview", in Sleeman, D.H. and Brown, J.S., (editors), Intelligent Tutoring systems, Academic Press, New York, 1981.

[15] Torkzadeh, G., and Rao, S.S., “Expert Systems for Small Businesses”, Information and Management, Vol. 15, 1988, pp. 229–235.

[16] Waterman, D.A., A Guide to Expert Systems, Addison-Wesley, Reading, Massachusetts, 1986.

[17] Weiss, S.M. and Kulikowski, C.A., A Practical Guide to Designing Expert Systems, Rowman & Allanheld, Totowa, New Jersey, 1984.

[18] Wenger, E., Artificial Intelligence and Tutoring Systems: Computational Approaches to the Communication of Knowledge, Morgan-Kaufmann, Los Altos, California, 1986.

[19] Woods, D.D., Pople, H.E., and Roth, E.M., The Cognitive Environment Simulation as a Tool for Modeling Human Performance and Reliability. Technical Report NUREG-CR-5213, U.S. Nuclear Regulatory Commission, 1988.
