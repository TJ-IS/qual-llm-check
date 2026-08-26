---
otero_id: 13038
otero_key: "SBDHR3BV"
title: "An intelligent decision support system for service network planning"
authors: "Waiman Cheung; Lawrence C. Leung; Philip C.F. Tam"
year: "2005"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2003.09.007"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An intelligent decision support system for service network planning<sup>\$</sup>

Waiman Cheung\*, Lawrence C. Leung, Philip C.F. Tam

Department of Decision Sciences and Managerial Economics, The Chinese University of Hong Kong, Shatin, Hong Kong

Received 1 June 2002; accepted 1 September 2003 Available online 2 April 2004

## Abstract

The joint use of an optimization model and a simulation model as a two-stage methodology has been successfully applied in various operation planning situations, such as service network planning. While using the two-stage methodology, the decisionmaker, who is normally a domain expert, also needs to be familiar with the models. He/she manipulates the two models iteratively to reach a planning solution. This paper presents an intelligent decision support system (IDSS), which integrates a decision support system (DSS) with an expert system (ES), to provide guidance to the decision-maker during the planning process. As proof of this concept, a PC-based IDSS prototype was built and implemented in the design of a service network for a major air-express courier. <sup>D</sup> 2004 Elsevier B.V. All rights reserved.

Keywords: Decision support system; Expert system; Network planning

## 1. Introduction

Hong Kong international airport has been relocated, from a position relatively close to the center of the city to a remote island at Chek Lap Kok. Major infrastructure developments have also been rapidly developed to support changes in logistic services and shifting customer demands. In response to such changes, DHL, a leading worldwide air-express courier, has sought to redesign its distribution network in Hong Kong in order to capitalize on opportunities, minimize costs and improve customer service. The joint use of an optimization model and a simulation model was developed as a two-stage methodology for designing the network [3,7]. Implementing such a distribution network is a long-term process, requiring periodical review and assessment of the network using the two models. Changes to the original design may be recommended according to the updated operation and demand data. An intelligent decision support system (IDSS) was developed to assist the planning as well as the review processes.

## 1.1. The service network

DHL(HK)’s service network consists of demand zones, satellite depots, service centers and the airport. Demand zones are predetermined service areas, organized according to the level of customer demand as well as geographical characteristics; there are more zones within busy and commercial areas where order pattern is concentrated. When couriers pick up shipments in demand zones, they are assigned to a specific satellite depot covering several zones. At the depots, packages are consolidated and the consolidated load is then delivered to the corresponding service center responsible for the depot. A service center, which also functions as a depot, is responsible for several depots. At the service center all major processing, such as labeling, X-ray screening, re-weighing, sorting and documentation, is carried out. Shipments are then further consolidated into air containers or bags and transported to the airport for transfer onto the corresponding aircraft.

DHL(HK) must effectively manage the processes of pickup, consolidation, processing, further consolidation and delivery to the airport. The service network is at the heart of this process. The critical decisions in the design of the service network are concerned with installation decisions relating to depots and service centers:

 Location of the depots and their coverage of demand zones.

 Location of service centers and their coverage of depots.

 Capacity of these facilities.

 Installation schedule for these facilities.

## 1.2. Two-stage network design methodology

A two-stage methodology (Fig. 1), with a macroplanning model and an operation simulation model, was developed [7] for designing the distribution network for DHL(HK). While the macro-model searches for the least-cost network plan in a 10-year horizon, the simulation model is used to validate and evaluate the performance of the given distribution network at the operational level.

## 1.2.1. Macro-planning model

The macro-planning model is a mixed integer programming (MIP) model, which aims to search for the distribution network with minimal cost settings, subject to customer demands, facility capacity and response time. The major decisions to be made are the locations of two types of facilities (satellite depots and service centers), their corresponding capacities and the year of installation, together with the assignment of shipment routes. The planning model was implemented using PC-based mixed integer programming software MPSIII, with 45,900 continuous variables, 1050 zero – one variables and 820 constraints.

![](/api/attachments/SBDHR3BV/fulltext/images/20aca7c72d618486aedcd84f6063828528b769a0ec947ed985933d1eacd5e154.jpg)  
Fig. 1. Two-stage network planning approach.

## 1.2.2. Operation simulation model

As the macro-planning model develops the network using aggregate data, such as yearly demands and average costs, it does not take into account operation fluctuations and random behaviors. A SIMAN-based simulation software, ARENA, was used to model and simulate the air express courier’s daily operations. The simulation model was used first to validate then to evaluate the performance of the recommended network. The locations of the depots and service centers, as well as shipment assignments of zone-depots-service centers, were in accordance with the results of the planning model. The validations included checking the utilization of each facility and comparing the estimated operating costs used in the MIP model with the simulated costs. The performance measures of the service network include:

 Service coverage—the percentage of shipment requests that arrive before cut-off time.

 Service reliability—the percentage of pick-ups that make same-day flights.

## 1.3. The iterative planning process

Network planning using the two-stage methodology is an iterative process. The decision-maker first obtains a distribution network for a 10-year planning horizon using the mixed integer programming model. The suggested network is then simulated using the SIMAN-based simulation model. Based on the simulated results, the decision-maker validates the input data used in the optimization model, assesses the facility utilization of the network and evaluates the performance (i.e., service coverage and reliability) of the suggested network. The validation and evaluation processes often require the decision-maker to execute the two models iteratively until he/she is satisfied with the performance measures concerned. Fig. 2 illustrates the iterative process of the network design. Operation characteristics collected from the simulation are analyzed and the feedback is used to implement the next round of model execution.

![](/api/attachments/SBDHR3BV/fulltext/images/f3e9a3b570d77183d6aad17100a656d91f98963cfc21b77e4037c4499b5025c5.jpg)  
Fig. 2. An iterative planning process.

While the two-stage methodology has also been successfully used in planning other operations [2,8, 10], the planning exercises require a decision-maker who is not only a domain expert but is also (1) familiar with the two models and (2) capable of manipulating the data and models. In this paper, we propose an IDSS, which combines a decision support system (DSS) with an expert system (ES), to facilitate the two-stage methodology for operations planning. Besides data and model manipulations, the functionality of the proposed system focuses on providing intelligent guidance while searching and assessing the planning results. Furthermore, since most operation planning is for long-term purposes (i.e. 5 – 10 years), the recommended plan needs to be reviewed periodically (e.g. every 3– 6 months), or modified within the planning horizon. The knowledge gained and lessons learnt from the initial planning exercise should be documented and reused in the next exercise. The proposed IDSS is able to capture such knowledge as a set of rules, which are further operationalized in an expert system.

## 2. Developing an intelligent DSS for the network planning

A regular decision support system helps decisionmakers to manipulate data and models. It does not play the role of an intelligent assistant to the decisionmaker. IDSS is needed and is economically feasible for generic problems that require repetitive decisions, such as service network planning. Recent applications of intelligent DSS include IDSSFLEX for the design and evaluation of flexible manufacturing systems [1], Markex for product development decisions [9] and an IDSS for selecting IT applications that match company strategy [5]. There may be different ways to make a DSS more intelligent; the most frequently suggested method is to integrate a DSS with an ES [4,6,11].

## 2.1. Integration of expert system and decision support system

Turban and Watson [11] suggested two fundamental ES/DSS integration models: they are (1) ESs integrated into DSS components (Fig. 3) and (2) ES as a separate component in the DSS (Fig. 4). In the first model, the incorporation of ESs aims to enhance the function of particular components in a DSS; for example, integrating an ES into the database management system (DBMS) of a DSS, which adds reasoning capability to data manipulation. This particular integration enables users to perform higher-level queries, such as asking ‘why’ or ‘how’ questions. According to Turban, the integration of ESs in DSS components could be applied independently.

![](/api/attachments/SBDHR3BV/fulltext/images/2b8b4d7f11bd3eb58180a80988d400b5666ff3a78d53d07a719ef0c07ac73041.jpg)  
Fig. 4. ES as a separate DSS component.

In the second model, an ES is an add-on to the original DSS. The ES complements the DSS in one or more steps of a decision-making process. Such integration may be conceptualized as using the ES to play the role of a human expert who carries out strategy formulation, interpretation or alternative evaluation. In our network planning, we followed the second model, where the DSS is responsible for both data and model manipulations, while the ES provides domain knowledge and recommends resolutions during the planning iteration.

![](/api/attachments/SBDHR3BV/fulltext/images/1a46cb7e7044b08a57fa8b9ee30113f3926bc62ff6122bed470d918c5315aee8.jpg)  
Fig. 3. ESs attached to DSS components.

## 2.2. The architectural design of the proposed IDSS

Fig. 5 shows the detailed system architecture of the IDSS designed for network planning. The architecture signifies the integration of a DSS and an ES. During the planning process, data and models are manipulated through the DBMS and model base management system (MBMS), respectively. Instructions for data modifications and model executions may come from the ES interface directly. The MBMS obtains the relevant input data for model executions from the DBMS and, in return, results generated from model executions are sent back to the DBMS for storage. The database also provides facts for the ES as part of the knowledge base. Using these facts together with the predefined rules, the inference engine of the ES performs model validations and planning evaluations, according to what a domain expert is supposed to do. Conclusions and recommendations are then passed to the interface, where they are displayed to the decisionmaker and transferred to the MBMS and DBMS, in the form of procedure calls for various actions.

## 3. Implementation of the intelligent DSS

## 3.1. Data management

PC-based DBMS: Microsoft Access is used to manage all the data and respond to requests from the MBMS and the ES interface (see Fig. 6). An advantage of using Access is its ability to manage data stored in

![](/api/attachments/SBDHR3BV/fulltext/images/b1baaebf65ae03bb5a580c7aae6ffa38d79182db9aae0bc14012e8feefc79aa7.jpg)  
Fig. 5. System architecture and interactions.

![](/api/attachments/SBDHR3BV/fulltext/images/723c3f82652b6df0020acf2631ad4ad54ead4e410b9fa4441b9ce36d041efbff.jpg)  
Fig. 6. Data and model manipulation.

Microsoft Excel, since a lot of the original demand and operation data are in Excel format. A C program is written to interpret and convert the pure text file generated by the MPSIII into comma-separated values that are meaningful to Access. Data stored in the database include the following.

Input data—refers to the aggregate data, such as yearly demand profiles for all the zones and operating costs for various facilities and activities for the optimization model, as well as probabilistic operation parameters such as travel times and daily demand arrival patterns for the simulation model.

Output results—refers to both the intermediate and final network results (i.e., network configurations and simulation statistics) produced by the two models during the iterations.

Iteration history—refers to the activity logs throughout the planning process, which include model modifications and parameter changes for each iteration.

## 3.2. Model manipulation

During the network planning, the MBMS performs various model manipulations according to instructions received from the decision-maker or the expert system interface. Parameter initialization, model modification and model execution are the three major functions provided, respectively, by the three program modules in the MBMS. The modules consist of C programs and batch programs, which are described as follows:

## 3.2.1. Parameter initialization module

This module is responsible for retrieving the necessary data and parameters from the database and converting them into specific input formats for MPSIII and Arena. The input files must be generated before model execution. Two C programs are developed for the purpose:

 Init<sup>\_</sup>mip ([filename])—filename is the name of the output file of this program, which is the input file for the subsequent round of MPSIII execution. The filename should follow a naming convention that can differentiate files for different scenarios during the iterative planning process.

 Init<sup>\_</sup>sim ([filename])—filename is the name of the output file of this program, which is the input file for the subsequent round of simulation.

## 3.2.2. Model execution module

This module consists of two DOS batch files, namely mip.bat and sim.bat. Besides the DOS command lines for setting the computing environment, the other two command lines in the batch files are for parameter initialization and model execution.

 Mip ([nodes, filename])—nodes specifies the number of solution nodes to be searched during the MPSIII execution and filename is the input file name.

 Sim ([replications, filename])—replications specifies the number of simulation cycles. In our simulation model, a replication represents 1 week of operation. filename is the input file name for Arena execution.

## 3.2.3. Model modification module

During the validation and performance evaluation, the models often need to be re-executed using modified data sets and/or parameters. The major C program for these modifications include:

Cost<sup>\_</sup>update (scenario, period, zone, depot, cost)— changes the transportation cost from a zone to a depot to \$cost in year period of the objective function of the MIP model for the scenarioth iteration.

 Time<sup>\_</sup>window<sup>\_</sup>update (scenario, time<sup>\_</sup>window)— changes the allowable transportation and processing time to time<sup>\_</sup>window in a constraint of the MIP model for the scenarioth iteration. A smaller time window will result in a more efficient network with a higher operating cost.

utilization<sup>\_</sup>limit<sup>\_</sup>update (scenario, utilization<sup>\_</sup>limit)—changes the acceptable utilization rate for all facilities to utilization<sup>\_</sup>limit in a constraint of the MIP model for the scenarioth iteration. A smaller utilization limit will result in more or bigger facilities being built.

 facilities<sup>\_</sup>selection (scenario, facility, zone, type, period)—modifies a constraint in the MIP model to force a facility (depot or center) of capacity type to be established at location zone in year period, for the scenarioth iteration.

 workforce<sup>\_</sup>change (scenario, zone, change)— modifies the number of couriers assigned to demand zone to change for the scenarioth simulation iteration. More couriers will result in better service reliability for the specific zone.

 cutoff<sup>\_</sup>change (scenario, cutoff)—modifies the daily operation cutoff time for the scenarioth simulation iteration. A later cutoff time will result in better service coverage but lower reliability.

## 3.3. Representing domain knowledge in rules

The knowledge base stores the domain knowledge acquired from human experts and the knowledge accumulated from the previous planning exercises in the form of ‘‘If–Then’’ rules. Together with an inference engine, intelligent guidance can be provided for the following tasks: (1) interpret and validate the planning results generated from the two models; (2) evaluate the performance of the suggested network based on service coverage and liability measures; and (3) determine the next course of action in the iterative planning process. Knowledge engineering for the IDSS was carried out in three steps.

![](/api/attachments/SBDHR3BV/fulltext/images/4f9b16cefe6628cd7010a70b4ff3d03ed59d50b1082ebc14dadb0d2c32e80033.jpg)  
Fig. 7. Network planning overall logic flow.

## 3.3.1. Domain and task identification

We first identified the tasks and procedures that a decision-maker has to accomplish throughout the network planning process. Fig. 7 illustrates the overall logic flow of the process. The four major tasks are (1) unit transportation cost validation, (2) facilities utilization validation, (3) service coverage evaluation and (4) service reliability evaluation. In general, each iteration involves (1) assessing the completed task based on specific measures and (2) determining the course of actions, including model modifications and executions, and moving on to the next task.

## 3.3.2. Knowledge acquisition, representation and coding

The opinions of field experts are a major source of knowledge; we therefore worked closely with the operations manager and many experienced couriers on specific cases. Decision algorithms for the validation and evaluation tasks were captured and can be found in Ref. [7]. To represent and subsequently implement the acquired knowledge in our expert system, a dependency diagram and a decision chart were used.

A reasoning process can be represented by a set of dependency diagrams, which are maps of the causal relationships between conditions and actions for different goals. The diagrams can also serve as a graphical model of a knowledge-based system. Fig. 8 illustrates a dependency diagram for the goal, validating the unit transportation cost.

Each triangle in the dependency diagram is given a number preceded by an ‘‘R’’. A triangle represents a set of rules, with conditions (represented by arrows or rectangles) on its left-hand side and conclusions or actions on its right-hand side. The name of a

![](/api/attachments/SBDHR3BV/fulltext/images/ee518d57230ff97c7cdd0a784a8a41797b076ed961cc19a96a29d4ffd85cf475.jpg)  
Fig. 8. Dependency diagram-unit transportation cost validation.

![](/api/attachments/SBDHR3BV/fulltext/images/3aaef4ae04ae7ab4869ffe010525c35175929120ea7efc5234852e47563ffab1.jpg)  
Fig. 9. Decision chart-unit transportation cost modification.

condition is written on an arrow or in a rectangle. A question mark indicates that a value is needed for further inferencing, which may be obtained either from the database or by prompting the decisionmaker for a value. Possible values for each condition or action are shown underneath the arrow or box, respectively. The goal of the reasoning is marked on the right-hand side of the right-most triangle in the dependency diagram. In this case, transportation cost is validated if the estimated costs used in the MIP model and the simulated costs are comparable for all the valid routes.

![](/api/attachments/SBDHR3BV/fulltext/images/b942e936a04e2a034e8bde0e23d83d8fd0db65ee8eb1ecd566e6a391b7174040.jpg)  
Fig. 10. Rule set for decision chart R102.

Each triangle is associated with a decision chart. Fig. 9 illustrates a decision chart for rule set R102 in Fig. 8. The decision chart contains two pieces of important information for rule-based inferencing. First, it provides a list of all possible combinations of condition values and corresponding conclusions/ actions; each column except the first one represents a rule. Column 2 in the chart can be read ‘‘if route existence is no (i.e., an invalid route), then the unit transportation cost of the route remains unchanged.’’ The second important piece of information is how the sequence of rules are fired during inferencing, which means the system will attempt to fire each rule in sequence, starting from left to right, until one is fired.

With the help of the dependency diagrams and decision charts, knowledge can now be coded as ‘‘if – then’’ rules. Fig. 10 shows the rules extracted directly from the decision chart R102. Similar extractions are performed for all the decision charts corresponding to the triangles in all the dependency diagrams. The resulting rule sets are then implemented in a backward chaining, PC-based expert system shell, M.4 for the system prototyping and testing.

## 4. A case study using the IDSS

The test scenario was to design a service network for DHL(HK) with 33 demand zones, 15 of which were candidates for depots and 9 of which were potential sites for service centers. Operation policies included (1) facility utilization of less than 85% for all depots and service centers; (2) cut-off time not earlier than 5:15 p.m.; (3) service coverage of at least 90%; and (4) service reliability of at least 95%.

## 4.1. The system-assisted planning process

To begin the planning process, the decision-maker issues a command, which triggers the decision support subsystem to initiate the MPSIII model execution. The resulting network together with the operation parameters are then used as inputs for simulation. Both the network configuration and simulation statistics are subsequently passed to the expert subsystem for validation and performance evaluation. Throughout the iterative process, the ES may display recommendations for the decision-maker’s choice or it will continue until a satisfying network design is found. The iteration history can be displayed when a problem is encountered during the execution.

During the network validation, the IDSS validates the cost and facility utilization according to the predefined rules and simulated results. Fig. 11 shows some of the system messages displayed on the interface when the system checks the relevancy of each route, performs the necessary unit cost calculation, comparison, and then recommends actions to the notvalidated routes. Re-execution of the MIP model using the modified unit cost is also recommended. The validation process will repeat until both the cost and facility utilization are validated.

When the validations are completed, the system starts to examine the service performance and to determine whether modification of the network design is needed. The two performance measures, service coverage and service reliability, are computed from the simulation statistics and displayed (see Fig. 12). The decision-maker may change the performance requirement online and the ES will determine the appropriate modifications and initiate the necessary iterations according to the feedback.

## 4.2. The iteration summary

In the case study, there were a total of 14 iterations before the IDSS reached the final network design. Fig. 13 summarizes the iteration history in the planning process.

Throughout the test scenario, many of the iterations (iterations 1 – 5 and 9 – 11) were for unit transportation cost validation. Since the service network configurations are very sensitive to the unit transportation costs, changes in the unit cost will result in new configurations, which need to be revalidated.

The convergence of the unit cost during the iterations is not guaranteed. In some cases, unit cost modification and validation may run into looped iterations. Hence, the number of iterations for cost validation is closely monitored and the intervention of the decision-maker may be required.

![](/api/attachments/SBDHR3BV/fulltext/images/09af3555e5668121c86655fe2fd39ac80f896ab6eea19bfbc1f6ff68d8ef3bc8.jpg)  
Fig. 11. Validating unit transportation cost.

After the transportation cost was validated during the fifth iteration, the ES system proceeded to check whether the facilities were operating within the designed utilization. Both weekly and daily utilization for all facilities were checked. According to the iteration history, weekly utilization for all facilities was within the allowable limit, while two facilities were over-utilized on Wednesday and Friday. To rectify the problem, the system needed help in identifying which routes could be re-assigned to less utilized facilities to alleviate the situation. All possible routes were listed and the decision-maker was prompted to make the selection. Modifications were then made via the DSS and the simulation was re-executed.

![](/api/attachments/SBDHR3BV/fulltext/images/173b3d8e341caa7e90df29d911b2d3dc3fed433e7f9014c0c375fe05ec0c6c29.jpg)  
Fig. 12. Performance evaluation consultation.

<table><tr><td>Itns</td><td>Problems</td><td>Suggested Rectification</td><td>Actions</td></tr><tr><td>1-5</td><td>Unit cost validation failure</td><td>Modify unit transportation costs</td><td>Re-run MIP model with modified unit cost</td></tr><tr><td>6</td><td>Over-utilization in specific facilities</td><td>Route re-assignment to alleviate over-utilization</td><td>Re-run simulation model with new route re-assignment</td></tr><tr><td>7</td><td>Unsatisfactory service coverage</td><td>Delay operational cutoff time</td><td>Re-run simulation model with new cutoff</td></tr><tr><td>8</td><td>Unsatisfactory overall service reliability</td><td>Re-design a more time efficient network</td><td>Re-run MIP model with next binding time window</td></tr><tr><td>9-12</td><td>Unit cost validation failure</td><td>Modify unit transportation costs</td><td>Re-run MIP model with modified unit cost</td></tr><tr><td>13</td><td>Unsatisfactory service reliability in specific zone</td><td>Increase workforce for respective zone</td><td>Re-run simulation model with new workforce</td></tr><tr><td>14</td><td>Nil</td><td>N/A</td><td>Finalize network design</td></tr></table>

Fig. 13. Summary of testing scenario iteration history.

The simulation recommended a delay in operational cutoff time to improve the service coverage in the seventh iteration after validation was completed. Due to unsatisfactory service reliability, re-execution of the MIP model using the next binding time window, derived from the last macro-planning results, was recommended in the eighth iteration. The whole process of validation and evaluation was reiterated using this new network design. A satisfactory network design was reached at the 14th iteration. Several design cases with slightly different settings were also done using the IDSS. All cases required further iterations to achieve satisfactory results, but the resulting designs are comparable to those that are done manually without the help of the IDSS.

## 5. Analysis and evaluation

The PC-based IDSS offered an opportunity to test the feasibility and effectiveness of such a system when applied to a real-life planning problem. The advantages and limitations of the system are summarized as follows.

## 5.1. Knowledge accumulation and management

The dependency diagrams and decision charts provide valuable documentation of the knowledge acquired and accumulated. Knowledge acquired during subsequent planning exercises can also be incorporated into these diagrams and charts, and new rules can then be added to the existing knowledge base. The decision-maker can also modify existing rules to adapt to new validation or evaluation criteria. In the current implementation of the IDSS, the enforcement of the consistency and integrity of the knowledge base is delegated to the domain expert, with the help of a monitoring mechanism. Here, the system will automatically monitor the number of iterations and will record all iteration history. In the knowledge base (in a rule), the maximum number of iterations for a problem rectification is set to 10. When a problem is not rectified within the maximum number of iterations, the system will call for human intervention and will present the modifications history for the current problem. The domain expert will then diagnose the problem history and is expected to provide adjustment to the rules. For example, if the current problem is stalled due to cost validation failure, the system will present a profile of cost modifications on respective routes. The domain expert will judge the routing and cost combinations and adjust the knowledge base accordingly. For new planners and operation managers, the IDSS can also be used as a training tool.

## 5.2. Intelligent guidance

The IDSS provides guidance to the planner on the overall planning flow logic, advising on necessary modifications and, consequently, which model(s) needs to be re-run. For instance, when a reliability test fails, the system may advise increasing the workforce at a facility and then re-running the simulation, or tightening the time window then re-running the two models, depending on whether it is a minor reliability problem on a specific day or an overall failure. At the micro-level, the IDSS provides guidance not only on ‘‘why’’—identifying what causes the problem—but also on ‘‘what’’ needs to be changed. For instance, when cost validation fails, the system will re-calculate new costs for the problematic routes, which will be used for the next round of execution. The decisionmaker can also interact with the system to finalize the next course of action. To alleviate over-utilization of a facility, the decision-maker may re-assign routes from a given list of all eligible routes, to a less utilized facility. Expert’s opinions are, therefore, incorporated in the planning process through these interactions with the system.

## 5.3. Better data and model manipulation

During the planning process, the manipulation of data and models is tedious and often prone to errors. Most decision-makers are not trained to be computer experts or modelers. The use of the IDSS releases them from direct data manipulations at the file level. Since the system keeps a record of intermediate results and the iteration history in its database, decision-makers can easily trace back to past designs, which enables rapid reference during the network planning process. On the other hand, the IDSS also offers simple but very useful model manipulation functions for model modification and execution. The decision-maker does not need to understand the complex syntax of both MPSIII and Arena in order to modify the models. As a result, they can focus on critical planning decisions.

## 5.4. Limitations

The IDSS cannot play the role of a modeler. The model modification capability of the IDSS prototype is limited to changing the coefficients of a constraint or objective function, tightening or relaxing a constraint and binding variables with specific values. Major changes such as adding new variables(s) or constraint(s) are not supported with the current prototype system. Furthermore, such major changes may even cause existing model modification program(s) to be modified. In order to allow modifications to the simulation model, the network configuration and other parameters (i.e., facility capacity, workforce, number of trucks, start time, cutoff time, etc.) cannot be hard-coded in the model. Instead, they are stored in an initial file, which is read at the beginning of the simulation execution. For example, the eligible routes between 33 zones and 6 depots are represented by a 33 - 6 matrix of ‘‘1’’ and ‘‘0’’ in the initial file. Therefore, to re-assign a route is equivalent to changing a ‘‘0’’ to ‘‘1’’ and another ‘‘1’’ to ‘‘0.’’ While it is easy to modify the simulation model by programs, it is more difficult to program and debug the simulation model to begin with, and the resulting simulation model may not be the most efficient one to run.

## 6. Conclusions

In this paper, we have proposed an IDSS, which integrates a DSS and an ES to facilitate the two-stage methodology for operations planning. An architecture that characterizes the conceptual design of the system and the two-stage planning approach is constructed. The proposed IDSS is able to capture the domain knowledge and provide intelligent guidance during the planning process. While the data and model manipulations are done through the DSS, decisionmakers can focus solely on the planning issues.

To illustrate the functionality and effectiveness of the proposed IDSS, a PC-based prototype was built and tested on a real-life project, which was to design a service network for an air express courier. The IDSS prototype has demonstrated its ability to document the planning knowledge in rules and further operationalize this knowledge through the inference engine. A planning manager with only basic knowledge of the two models and no experience of either MPSIII or Arena can still carry out the network planning. A junior manager could also use the system for training and learning purposes. We believe that our IDSS has provided a significant improvement in applying the two-stage methodology for operations planning.

## References

[1] D. Borenstein, IDSSFLEX: an intelligent DSS for the design and evaluation of flexible manufacturing systems, The Journal of the Operational Research Society 49 (7) (1998) 734 – 745.

[2] R.C. Carlson, J.C. Hershey, D.H. Kropp, Use of optimization and simulation models to analyze outpatient health care settings, Decision Sciences 10 (1979) 412– 433.

[3] W. Cheung, L.C. Leung, Y.M. Wong, Strategic service network design for DHL Hong Kong, Interfaces 31 (4) (2001) 1 – 14.

[4] J. Fedorowicz, G. Williams, Representing modeling knowledge in an intelligent decision support system, Decision Sup port Systems 2 (1) (1986) 3 –14.

[5] R. Kathuria, M. Anandarajan, M. Igbaria, Linking IT applications with manufacturing strategy: an intelligent decision support system approach, Decision Sciences Journal 30 (4) (1999) 959 – 992.

[6] D. King, Intelligent decision support: strategies of integrating decision support, database management, and expert system technologies, Expert Systems with Applications 1 (1) (1990) 23 – 38.

[7] L.C. Leung, W. Cheung, An integrative decision methodology for designing and operating an air-express courier’s dis-

tribution network, Decision Sciences Journal 31 (1) (2000) 105– 127.

[8] L.C. Leung, S. Maheshwari, W.A. Miller, Concurrent part assignment and tool allocation in FMS with materials handling considerations, International Journal of Production Research 31 (1993) 117– 138.

[9] N.F. Matsatsinis, MARKEX: an intelligent decision support system for product development decisions, European Journal of Operational Research 113 (2) (1999) 336 – 355.

[10] R.L. Nolan, M.G. Sovereign, A recursive optimization and simulation approach to analysis with an application to transportation systems, Management Science 18 (1972) B676– B690.

[11] E. Turban, H. Watson, Integrating expert systems and decision support systems, Management Information Systems Quarterly, (1986 June) 121– 136.

Dr. Waiman Cheung holds an MBA and a PhD in Decision Sciences and Engineering Systems from Rensselaer Polytechnic Institute. He is currently a Professor at Business Administration, The Chinese University of Hong Kong, where he teaches both graduate and undergraduate MIS courses. Prior to that, he had operated his own MIS consulting company and had worked as a Technical Staff for Oracle Systems in the US. Dr. Cheung has contributed articles to ACM Transactions on Information Systems, Decision Sciences, IEEE Transactions on Systems, Man and Cybernetics, Decision Support Systems, Information and Management, Journal of Intelligent Manufacturing, Annals of Operations Research, etc.

Lawrence C. Leung received his degrees in Industrial Engineering from Northeastern University (BS) and Virginia Tech (MS and PhD). He is a Professor at the Chinese University business school in Hong Kong, where he teaches operations management. He has designed distribution networks for large electric utilities and air express couriers. Dr. Leung has contributed articles to Decision Sciences, European Journal of Operational Research, IEEE Transactions on Power Systems, IEEE Transactions on System, Man, and Cybernetics, IIE Transactions, Interfaces, International Journal of Production Economics, International Journal of Production Research, and Journal of Manufacturing Systems.

Mr. Tam is currently working as an e-marketing specialist for Samsung Electronics Hong Kong. He received his BBA and Master of Philosophy degrees from the Chinese University of Hong Kong.
