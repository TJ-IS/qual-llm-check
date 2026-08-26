---
otero_id: 7602
otero_key: "5WF75Y9M"
title: "Design and development of a context-aware decision support system for real-time accident handling in logistics"
authors: "E.W.T. Ngai; T.K.P. Leung; Y.H. Wong; M.C.M. Lee; P.Y.F. Chai; Y.S. Choi"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.11.016"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Design and development of a context-aware decision support system for real-time accident handling in logistics

E.W.T. Ngai ⁎, T.K.P. Leung, Y.H. Wong, M.C.M. Lee, P.Y.F. Chai, Y.S. Choi

Department of Management & Marketing, The Hong Kong Polytechnic University, Hung Hom, Kowloon, Hong Kong, China

a r t i c l e i n f o

Available online 23 November 2011

Keywords: Context-aware decision support system Fleet management system prototype Real-time accident handling

## a b s t r a c t

This paper describes the design and development of a context-aware <sup>fl</sup>eet management system (CFMS) prototype for real-time accident handling in logistics using a design science approach. One of the most important decisions in <sup>fl</sup>eet management is the optimization of vehicle scheduling during an accident, such as a vehicle breakdown and mechanical failure during delivery. The schedule planner has to assign another vehicle to take over the task; thus, accident handling needs the reassignment or re-scheduling of vehicles. The large number of available vehicles for reassignment and numerous trips in a day make rescheduling complicated and dif<sup>fi</sup>cult to resolve. In this paper, we propose a CFMS integrated with global positioning system (GPS) for real-time vehicle positioning and eSeal enabled by the RFID technology, to help human planners with rescheduling. A CFMS prototype was built and evaluated in a real-world setting. The system prototype was satisfactory during evaluation. The system was found to be more effective by its potential users and <sup>fi</sup>eld logistics experts in aiding real-time accident handling in logistics. The design science approach used to develop the prototype could form a basis for further research.

© 2011 Elsevier B.V. All rights reserved.

## 1. Introduction

Facing keen competition, transportation and logistics industries have adopted information technologies such as eSeal, global positioning system (GPS), general packet radio service (GPRS), and thirdgeneration mobile telecommunications (3 G) to enhance ef<sup>fi</sup>ciency and <sup>fl</sup>exibility in <sup>fl</sup>eet operation and management. However, human experts usually schedule the trips. These experts plan the sequence of trips and vehicle assignments every day. When an accident or vehicle breakdown occurs, the planner will reschedule the interrupted trips and other related accidents using common sense and past experience. Therefore, the rescheduling and its outcome may be fuzzy, inconsistent, and not optimized. In addition, this approach is applicable only for a limited-sized <sup>fl</sup>eet. A large crew size and number of trips provide thousands or millions of scheduling options. The human planner may overlook the good options, and the rescheduling may take a very long time.

In this paper, we propose a merging of the information technologies that have already been adopted in the transportation and logistics industries to design and develop a context-aware <sup>fl</sup>eet management system (CFMS) prototype for real-time accident handling in logistics. A design science approach was used. The proposed system integrates eSeal, GPS, and mobile network technologies that collect various data, including real-time crew and vehicle status and positions, to support the planner in deciding the new trip schedule and vehicle assignment during an accident. The proposed system can support both practical use and further research by providing a design artifact—the prototype architecture and its implementation. The careful construction of artifacts has been transformed into a set of design principles for CFMS.

Theoretical guidance for designing and developing a CFMS for real-time accident handling is limited. Therefore, the present study developed the information system design theory (ISDT) for CFMS. This paper is organized as follows. Section 2 is the literature review on the <sup>fl</sup>eet management and logistics system. Section 3 presents the ISDT for a CFMS for real-time accident handling. Section 3.3.5 introduces the architecture of the proposed system. In Section 5, the proposed system is illustrated by a case study to demonstrate the application of the prototype system in a real-world case. The prototype system is evaluated in Section 6. Finally, Section 7 discusses the contributions of the current study, and Section 8 presents the conclusion and recommendations for further research.

## 2. Literature review

Fleet management is one of the important topics in logistics and transportation research. Fleet management system helps accomplish a series of tasks in managing any or all aspects relating to the <sup>fl</sup>eet operation of vehicles, such as cars, vans, and trucks. Several recent academic studies on the design and development of a decision support system (DSS) for <sup>fl</sup>eet management are reviewed below.

Avramovich et al. [1] proposed a DSS for <sup>fl</sup>eet management based on a large linear programming (LP) model. The system is implemented to plan the <sup>fl</sup>eet con<sup>fi</sup>guration and assist management in making decisions on buying, selling, and trading-in tractor units. The system helps reduce the tractor inventory and its carrying cost by approximately \$600,000 a year.

Couillard [4] developed a DSS to solve the <sup>fl</sup>eet planning problem. The system assists managers in each step of the planning process, such as forecasting demand and choosing the best plan. An example shows that the system can help deal with the complex management process of determining <sup>fl</sup>eet size and composition, which involves trade-offs between short- and long-term objectives and uncertainty. Basnet et al. [2] reported a microcomputer-based DSS for vehicle routing, particularly occurring in the New Zealand dairy industry. The system helps create or improve milk tanker routes, leading to reduced milk collection, lower labor cost, and improved scheduling.

Fagerholt [5] presented a DSS for vessel <sup>fl</sup>eet schedule. The system was developed to be a commercial software, and is now used by several shipping companies. Implementation in several organizations shows that the system signi<sup>fi</sup>cantly improves <sup>fl</sup>eet scheduling and <sup>fl</sup>eet utilization.

Zografos et al. [15] designed and developed a DSS for supporting real-time decisions related to incident response logistics. The proposed DSS is based on an extensive user-requirements survey in six European countries. Mathematical models, rules, and algorithms are integrated into a user-friendly environment to minimize incident response time.

Zeimpekis et al. [13] proposed a dynamic <sup>fl</sup>eet management system to handle unforeseen events. They described and categorized typical accidents that may occur during delivery execution. The proposed system supports decision making to handle dynamic accidents. A conceptual system architecture was introduced, but not implemented in any real-world case study.

Li et al. [7] reported a prototype DSS that recommends solutions for single-depot rescheduling. The system has been proven effective by an experimental study using randomly generated data, and by a real-world problem involving the operational planning for solid waste collection in a Brazilian city.

Zeimpekis et al. [14] presented and evaluated a real-time <sup>fl</sup>eet management system that handles unexpected events (e.g., traf<sup>fi</sup>c congestion). The system monitors the delivery vehicles in realtime, detects deviations from the initial distribution plan, and adjusts the schedule accordingly by suggesting effective rerouting strategies.

Sorensen and Bochtis [11] developed a conceptual model based on a participatory approach and subsequent system analysis for an effective <sup>fl</sup>eet management system. The model involves system scope and user requirements identi<sup>fi</sup>cation, conceptual modeling, identi<sup>fi</sup>cation of actors and decision processes, and information-needs modeling.

Despite the previous literature on DSS that aids <sup>fl</sup>eet management and decision making on handling accidents, design science research into designing and developing a context-aware DSS for <sup>fl</sup>eet management in general, and accidents handling in logistics in particular, is lacking. We cannot <sup>fi</sup>nd any ready-to-use plug-ins that have not become commercially available. Theory and system development literature to guide design and development of a context-aware DSS for <sup>fl</sup>eet management is also lacking. Hence, this problem needs to be addressed.

## 3. Design theory for CFMS for real-time accident handling

Walls et al. [12] de<sup>fi</sup>ned the ISDT as a prescriptive theory integrating normative and descriptive theories into design paths intended to produce more effective information systems. The ISDT is concerned with how to design the artifact (design product) and the design process (method being used to realize the product) [12]. An ISDT is a package of three interrelated elements: a set of user requirements derived from kernel theory, principles governing the development process, and principles governing the design of a system [8]. The present paper outlines the design theory for CFMS for real-time accident handling, and de<sup>fi</sup>nes and elaborates the kernel theory and these three interrelated elements.

## 3.1. Kernel theory

Kernel theories are natural or social sciences theories governing design requirements [12]. The kernel theory, which underlies an IS design theory, may be an academic theory or a practitioner theoryin-use [10]. Developing an ISDT for CFMS requires a kernel theory to provide the basis for prototype system development. Following Markus et al. [8], the characteristics of handling accidents in <sup>fl</sup>eet management are analyzed as the kernel theory. Action research approach was adopted, and the process started with user requirements derived from kernel theories and development principles. Over a 16-month period, the project development team in the current study embarked on the following: participated in the organizational design activities of the prototype system in the case study company; deployed the prototype system and tests and conducted an evaluation of the system; and observed how users responded. Finally, the learning was articulated into IS design and development principles described in Section 3.3.

First, the overview of handling accidents in <sup>fl</sup>eet management is discussed. Traf<sup>fi</sup>c accidents refer to unplanned events that occur randomly in time and space, such as accidents and disabled vehicles. These accidents substantially reduce the capacity of the roadway section where they occur, and result in traf<sup>fi</sup>c congestion [15]. Generally, handling accidents must involve vehicle reassignment. A vehicle cannot serve the current trip during a breakdown or an accident; thus, a reassignment of vehicles might be requested to complete the interrupted trip and the next ones that have been assigned to the disabled vehicle. Two possible situations may occur. The <sup>fi</sup>rst situation is when the cargo on the trip has been loaded onto the vehicle, and the cargo is unique that the reassigned vehicle has to go to the breakdown point to pick up the cargo prior to delivery to the destination. The second situation arises when the cargo has not been loaded onto the vehicle before the breakdown, or the cargo on the disabled vehicle is not unique and the re-assigned vehicle can go to the starting location to pick up the cargo. On the other hand, if the vehicle cannot complete the current trip before the expected delivery time, vehicle reassignment is necessary to serve the successive trips assigned to that vehicle so that the remaining trip schedules are not affected. In general, the characteristics of handling accidents in <sup>fl</sup>eet management are listed as follows.

3.1.1. Characteristic #1: Predicting accidents in advance is nearly impossible

Accidents are speci<sup>fi</sup>c, unpredictable, unusual, and unintended accidents, but with marked effects. Nobody can predict when, where, and how the traf<sup>fi</sup>c incident will happen or to whom.

3.1.2. Characteristic #2: Traffic accidents are of different kinds

Accidents in <sup>fl</sup>eet management do not only include vehicle breakdowns and crashes. The different kinds of accidents that may happen in <sup>fl</sup>eet management are shown in Table 1.

3.1.3. Characteristic #3: Handling vehicular accidents needs information on the environment and other vehicles

Aside from the vehicle status and condition, information on the environment around the vehicle is also needed in accident handling. For example, to respond to an accident of a vehicle breakdown, the reassignment of vehicles should note the traf<sup>fi</sup>c conditions of different places to optimize the new schedule and ensure that the path of all vehicles is the shortest. In addition, handling a vehicular accident usually causes a chain reaction that affects the schedule and planning of other vehicles. Thus, the status and condition of other vehicles should also be considered in vehicle reassignment.

Table 1  
Traf<sup>fi</sup>c accidents in <sup>fl</sup>eet management.

<table><tr><td>Incident</td><td>Description</td></tr><tr><td>Vehicle breakdown or crash</td><td>The vehicle is out of order or crashed, and cannot serve the current and future trips of the day.</td></tr><tr><td>Delay</td><td>No confirmation is received at or before the expected delivery time; thus, the future trip schedule for the vehicle is affected.</td></tr><tr><td>Unplanned trip</td><td>An unplanned new trip is added to the current schedule; thus, a vehicle is assigned to this trip.</td></tr><tr><td>Trip cancellation</td><td>A trip that has not been started is cancelled by users; hence, the assigned vehicle becomes idle at the scheduled time.</td></tr></table>

3.1.4. Characteristic #4: The parties handling the accident are not staying in the same location

As mentioned, accident handling involves reassignment of the crew and vehicles. However, vehicles may not be staying in the same place when the reassignment is required. Several vehicles could be on the road for deliveries, while some may be parked at the depot. The re-assigned vehicles to handle the accidents may be distributed in different areas.

## 3.2. User requirements

A set of user requirements for the CFMS for accident handling was derived mainly from the kernel theory and asked directly from logistics practitioners and planners. The requirements would be the basis of the design and development principles of the system.

3.2.1. Requirement #1: Systems must be operated in real-time and provide prompt responses

As mentioned in characteristic #1, accidents in <sup>fl</sup>eet management are unpredictable. No one can expect when the system will be required to handle accidents; thus, vehicle reassignment cannot be done in advance. The system must handle the accident once it happens, and the response should be prompt.

3.2.2. Requirement #2: Systems must be able to handle different kinds of accidents

According to characteristic #2, accidents are of different kinds. Therefore, the system has to provide the appropriate approach to handle different kinds of accidents. For example, if the vehicle is broken down and cannot serve the current or future trips of the day, the vehicle reassignment for that day should exclude this vehicle. All the trips must be served by the other vehicles. On the other hand, if the vehicle is late due to the traf<sup>fi</sup>c jam, it will be late for the next trip only. Therefore, vehicle reassignment may be needed for the next trip only, and the vehicle can still proceed with the other schedules after serving the current trip.

3.2.3. Requirement #3: Systems must consider different kinds of contexts when deciding the responses

Characteristic #3 mentioned that handling vehicular accidents needs information on the environment and other vehicles. Therefore, when deciding the response to accidents, the system should not only involve the contexts of the vehicle that caused the disturbance, but also the status of the environment around it and those of other vehicles in the <sup>fl</sup>eet. The sample contexts could be the location of the vehicles, the estimated point-to-point travelling time among different regions, and vehicle loading, among others.

3.2.4. Requirement #4: Systems must distribute the accident response to multiple parties accurately, effectively, and quickly

The parties taking action to handle the accident (i.e., other vehi cles) may not be staying at the same location (characteristic #4). Thus, after generating the new schedule or vehicle assignment, the system has distributed the new schedule or assignment accurately and quickly. The new schedule or assignment needs to be noticed by all involved parties in a timely manner, so that the new schedule or assignment can be executed without any delay or mistake.

## 3.3. Design and development principles

Design and development principles govern the design and development process of a system [8]. In the present study, design theory is described as a set of <sup>fi</sup>ve combined design and development principles of the <sup>fl</sup>eet management system for accident handling, based on the user requirements presented in the previous section.

## 3.3.1. Principle #1: Design for prompt and online actions

The system design must support accident handling once the accident occurs, and the response should be prompt. Accidents cannot be predicted; hence, the system should be an online one to allow seamless communication among different parties for reporting or detecting accidents, and informing the involved parties of the need to handle the accident in a timely manner.

3.3.2. Principle #2: Design for the intelligent provision of appropriate responses to different kinds of accidents

The system has to intelligently provide appropriate responses to handling different kinds of accidents under different situations. For a vehicle breakdown or crash, two alternatives are possible for vehicle reassignment. The <sup>fi</sup>rst option is to send a new vehicle from the depot to the breakdown point to pick up the cargo and serve the interrupted trip. Nevertheless, the total cost of all the trips increases as the <sup>fl</sup>eet size increases. The second option is to re-assign the vehicle serving the trip that ends closest to the breakdown point of the disabled vehicle, to pick up the cargo and complete the interrupted trip. However, the planned trips of the re-assigned vehicle will be affected during this substitution. Therefore, the remaining vehicles will likely have their changes in route and schedule to accommodate the disturbances caused by the interrupted trip. Thus, the trips of a series of vehicles need to be rescheduled.

Similar to the cases of vehicle breakdown or accident, the same two possible alternatives for vehicle assignment are available when the vehicle cannot complete the current trip before the expected schedule or during unplanned trips. However, the rescheduling of this case only involves future trips and not the current ones.

If any trip is cancelled, the vehicle originally assigned to the trip becomes idle. Vehicle reassignment may be done to reduce the number of vehicles needed and to optimize the schedule.

3.3.3. Principle #3: Design for handling and processing different contexts from different sources

Different contexts from different sources are required to handle accidents; thus, the system should be designed for handling and processing such contexts effectively. The system should contain the modules for capturing, <sup>fi</sup>ltering, storing, and processing the required contexts. For example, the database design should consider the data type of the contexts and their relationships. The system should also be able to convert the context from raw data to a composite that the system can further analyze, for example, converting the GPS raw data to the latitude and longitude coordinates of the location of the vehicle (i.e., the region in the city).

Table 2  
Design and development principles vs proposed system features.

<table><tr><td>Design and Development Principles</td><td>Features of the Proposed System</td></tr><tr><td>Principle #1: Design for prompt and online actions.</td><td>The system is an online and real-time system.</td></tr><tr><td>Principle #2: Design for intelligent provision of appropriate responses to different kinds of accidents.</td><td>The system implements logistics strategy algorithms to handle different accident types (see Fig. 6 for the process before handling different accidents).</td></tr><tr><td>Principle #3: Design for handling and processing different contexts from different sources.</td><td>The system includes the context-aware subsystem (see Section 4.4 for details).</td></tr><tr><td>Principle #4: Design for integrating different information and communication technologies.</td><td>The context capture subsystem supports GPS receivers and eSeal/eSeal reader (see Section 4.5 for details).</td></tr><tr><td>Principle #5: Design for mobile communication.</td><td>The user interface of the system includes PDAs and smart phones (see Section 4.1 for details).</td></tr></table>

3.3.4. Principle #4: Design for integrating different information and communication technologies

The contexts are retrieved from different sources, which are enabled by different information and communication technologies. The location of vehicles is based on data collected from the GPS receiver, whereas the goods departure and arrival time estimates are based on the eSeal log data. Therefore, the system should be designed to provide interfaces that can integrate the information and communication technologies involved for capturing different kinds of contexts.

## 3.3.5. Principle #5: Design for mobile communication

The vehicle drivers are required to communicate with the operators in the of<sup>fi</sup>ce and report status, accidents, or any other required information. The operators need to inform the drivers about any new schedule or reassignment via the system. The vehicle drivers may be in different regions in the city; hence, communication between drivers and operators must involve the use of mobile devices such as PDAs, which can access the mobile network, smart phones, and others. Therefore, the system design should include support for mobile communication.

## 4. Context-aware <sup>fl</sup>eet management system for real-time accident handling

A system is considered to be context-aware if it can extract, interpret, and use context information, then adapt its functionality to the current context of use [3]. Context is any information that can be used to characterize the situation of an entity [6], whereas context awareness means the capacity to use context information. In the present study, a context-aware <sup>fl</sup>eet management system refers to a support system that enhances decision-making capabilities and improves decision quality using context-aware computing. Table 2 shows how the proposed prototype system follows the design and development principles.

The proposed prototype CFMS consists of <sup>fi</sup>ve major subsystems: user interface, model management, database management, context-aware, and context capture. Fig. 1 shows the basic CFMS architecture.

![](/api/attachments/5WF75Y9M/fulltext/images/237da0d00e4023507e73f8c61830e856de9493a5d65a6ad3ad0f2acbec5b1f9d.jpg)  
Fig. 1. System architecture of CFMS.

Table 3  
Category of information input and managed through the GUI.

<table><tr><td>Information Category</td><td>Examples</td></tr><tr><td>Vehicle</td><td>Vehicle ID, capacity, available time frame, etc.</td></tr><tr><td>Driver</td><td>Driver ID, driver name, available time frame, etc.</td></tr><tr><td>Trip</td><td>Shipping/service items, starting point, ending point, time window, priority, etc.</td></tr><tr><td>Customer</td><td>Customer name, contact person, priority, etc.</td></tr></table>

## 4.1. User interface

The user interface allows human schedulers and drivers to visually and interactively communicate with the CFMS. There are two major types of user devices: PC and mobile terminal devices (e.g., PDA and smart phone).

## 4.1.1. PC user interface

The web browser provides a familiar and consistent graphic user interface (GUI) to the CFMS. With this interface, the logistics scheduler/ planner can input and manage information on vehicles, drivers, trips, and customers (Table 3).

On the other hand, the user interface displays the information and data requested by users, as well as the schedules obtained using the algorithm in the model management subsystem, among others. Fig. 2 shows the screen displaying the information about a trip.

## 4.1.2. Mobile terminal user interface

Each vehicle has an installed mobile terminal, such as a smart phone or a PDA, which enables the driver to communicate with the CFMS. The mobile terminal connects to the server via GPRS. Allowing drivers to report accidents when the vehicle breaks down or crashes is one of the important functions of this terminal. Fig. 3 shows the user interface for reporting accidents.

## 4.2. Model management subsystem

In the proposed CFMS, the model management subsystem is designed to solve the vehicle scheduling and rescheduling problems. This subsystem has two components: optimal model and logistics strategy algorithm. The optimal model contains the constraints, framework, rule of thumb, theory, formula, assumptions, and de<sup>fi</sup>nitions, among other details, which are needed to provide scheduling solutions. One of the aims of the optimal model is to minimize the total expenditure of all the trips in a day. Total expenditure is de<sup>fi</sup>ned as follows:

$$
C = \sum_ {i = 1} ^ {V} c _ {i} d _ {i} + \sum_ {i = 1} ^ {V} f _ {i}
$$

where

$c _ { i }$ average diesel fuel cost per distance unit,

$d _ { i }$ distance travelled by the vehicle i,

$f _ { i }$ the average daily <sup>fi</sup>xed cost (including maintenance cost,

driver salary, vehicle rent) of vehicle i, and

$V$ total number of vehicles.

In the model management subsystem, the logistics strategy algorithm determines the optimal logistics strategy to minimize total cost. This strategy includes the optimal trip sequence, the optimal vehicle <sup>fl</sup>eet composition, and the optimal vehicle scheduling and rescheduling. Fig. 4 shows the screen display of scheduled trips in a day.

At midnight of each day, or at a time designated by the users (T1), the model management subsystem will generate an initial vehicle assignment and schedule for the trips of the next day. The schedule is based on traf<sup>fi</sup>c prediction provided by the external navigation system. In case of any interruption, such as accident or vehicle breakdown, the CFMS will use the model management subsystem to reschedule the interrupted trip and those it subsequently affected.

![](/api/attachments/5WF75Y9M/fulltext/images/6d0312022181cd35e4d1c7f58b103430548b1fb4b09a79e2ab543add9ae381c3.jpg)  
Fig. 2. Screen displaying the trip information

![](/api/attachments/5WF75Y9M/fulltext/images/56546468a0c706d940cc5494aa1c80c7cb3d7482345d21b90d9077e1dde79b6e.jpg)  
Fig. 3. Screen for reporting accidents.

Fig. 5 shows the process of decision-making support in the model management subsystem.

When trip interruption occurs, the CFMS will go through the process (Fig. 6) before regenerating the schedule. For example, if a “breakdown/accident” is happened, the system will update the availability and status of related vehicles and trips during the affected time period. If any backup trip is required, the starting point of the trip will be de<sup>fi</sup>ned. This may be the breakdown point or the depot, depending on the uniqueness of the cargo. If the cargo is unique and cannot be re-collected at the depot, the breakdown point will be de<sup>fi</sup>ned as the starting point of the backup trip. The CFMS will then proceed with the rescheduling process, in which new schedules will be determined after analyzing the current location and status of vehicles, as well as the attributes of trips (i.e., starting point, ending point, and time window). The model aims to <sup>fi</sup>nd a schedule with the minimal cost over a set of all possible vehicle assignment combinations. Thus, vehicle location is also important in determining cost. If the backup vehicle candidate is closer to the starting point of the backup trip, the cost for the backup trip is lower. Therefore, real-time vehicle positions captured by GPS are considered in the rescheduling process.

## 4.3. Data management subsystem

The database management subsystem consists of a database and a database management module. The database organizes internal and external data, as well as information required in the system. Most of the internal data are user inputs. External data include those from the government, commercial databases, other companies, and any external data collected by the <sup>fi</sup>rm. Weather reports announced by the government, traf<sup>fi</sup>c forecasts, and historical data provided by external systems are some examples of external data. The database management module stores the data in the database, retrieves data, and controls the database.

## 4.4. Context-aware subsystem

This subsystem is composed of the context acquisition module, context database (DB), context reasoning module, and context inference module. The context acquisition module collects contexts from the context capture subsystem. These raw contexts are called primitive contexts and are stored in the context DB without any processing [9]. The primitive context may be too basic for direct use in the system, or to be displayed to users. Thus, the context reasoning module converts the primitive context into a composite context, which is manipulated from at least one kind of primitive context. Table 4 summarizes the composite context acquired from different primitive contexts used for the present study. Context reasoning is the reasoning process about situational conditions of an entity, by aggregating information collected from the context capture system and the physical environment. Fig. 7 shows the architecture representing the relationship between sensors, context, and context-aware services.

![](/api/attachments/5WF75Y9M/fulltext/images/584a4185c60c0f37e24e507d1af9fd2c1f7193a38c3cf9f28ee2e5441235c7b3.jpg)  
Fig. 4. Screen displaying the scheduled trips in a day.

![](/api/attachments/5WF75Y9M/fulltext/images/93c2513e52276f96a41e6c331ac9d4f6ea3ee1a3dbdb29395f65bc2aeda05c70.jpg)  
Fig. 5. Decision-making support process in the model management subsystem.

This system needs the context inference module because not all the needed information can be extracted from raw context. The module contains diverse rules to create new contexts, and can also convert primitive context into composite context. That is, the context inference module is also used to derive higher-level contexts. For example, the output of the GPS receiver allows the module to derive the location of the vehicle. Inference rules for context matching are also stored. The composite context after processing will pass through the database management and model management subsystems for further processing.

## 4.5. Context capture subsystem

Context is any information that can be used to characterize the situation of an entity [6]. An entity is a person, place, or object that is relevant to the interaction between a user and an application, including the user and applications themselves [2]. For example, the GPS coordination of a vehicle is a context, and the vehicle is an entity. Thus, location can be used to characterize a vehicle situation.

The context capture subsystem acquires the contexts. In the prototype system, contexts related to vehicles and goods are captured by GPS receivers, eSeal, and mobile terminals. Fig. 8 shows the infrastructure of the context capture subsystem.

Usually, the driver will call the of<sup>fi</sup>ce to report the completion of a trip. In the case of cross- border trips, if the container is equipped with an eSeal, an eSeal con<sup>fi</sup>rmation message is sent to the server when the container is opened at the destination. If there is no eSeal message received on or before the expected delivery time, and the GPS data show that the vehicle has not arrived at the destination, then the trip is considered late. Vehicle reassignment may be needed.

A GPS receiver is installed in each vehicle for real-time location tracking. The latitude and longitude coordinates are passed to the mobile terminal, for example, the PDA in the vehicle, and the mobile terminal will send the coordinates to the server via GPRS. On the other hand, the client software installed in the mobile terminal provides an interface for the driver to report accidents to the of<sup>fi</sup>ce.

The eSeal readers are installed at logistics service/distribution centers. When the vehicle arrives at the logistics service or distribution center, the eSeal reader receives the information and updates the eSeal status after opening by the authorized party. The eSeal status will be sent to the server, and the system will know the arrival time and that the vehicle has delivered the container to the destination.

## 5. Case study

The case study is a major portable toilet provider in Hong Kong, founded in 1970. The company has over 1,000 portable toilets and serves more than 200 clients. Among the services the company provides are portable toilet rental and cleaning and disinfecting portable toilets. Each portable toilet must be delivered, cleaned, and maintained promptly, and then retrieved from client site on schedule. Although the daily operation of the toilet rental and onsite maintenance service is complex, the company relies solely on the traditional manual approach to arrange the job schedule, route, and status of the toilet rental. The company <sup>fi</sup>nds it dif<sup>fi</sup>cult to optimize vehicle scheduling and handling accidents without real-time data to support decision making in re-planning the job and route schedule.

A case study was conducted in the company to demonstrate the application of CFMS. Portable toilets are transported daily to different places in Hong Kong. Vehicle assignment and schedule are both decided by human schedulers based on past experience and common sense. During unexpected situations, such as vehicle breakdowns and crashes, the affected trips are usually re-assigned to the <sup>fi</sup>rst vehicle reported to be available by the drivers. The human scheduler does not know the status and location of the crew; thus, he/she cannot decide the rescheduling with suf<sup>fi</sup>cient information. In addition, the re-scheduling is a complicated process, and making the best decision in a short time is dif<sup>fi</sup>cult for a human scheduler.

The vehicles leave the depot at 8:00 AM each day to serve the scheduled trips. The vehicle goes to the starting point of the <sup>fi</sup>rst assigned trip and loads the cargo to be delivered. Then the vehicle must go to the ending point to unload the cargo. The vehicle will not go to the depot directly or serve a new trip without unloading its cargo at the ending point of the current trip. After completing the trip, the vehicle may go to the starting point of a compatible trip or return to the depot, according to the schedule.

In this case study, 30 trips are to be served in a day (Table 5). The time window denotes the latest arrival time of the cargo at the ending point for the trip. Each starting or ending point, which is considered a node, must be in Hong Kong. The estimated travel time between each node is derived from the predicted data provided by the external navigation system. The blue dots in Fig. 9 illustrate the nodes involved in the case study.

The CFMS will calculate the total cost of each possible solution for the initial schedule. The solution with the lowest cost is de<sup>fi</sup>ned as the optimal schedule, as shown in Table 6. The one-hour lunch break for the drivers is also considered in the schedule.

The following situation is described and explained to manifest how the CFMS re-assigns the vehicle when an unexpected event occurs. Assume that vehicle V1 crashed at 11:05 when serving trip T15. At that moment, V1 has already loaded the cargo at the starting point, Mei Foo, and is going to the ending point, Kwun Tong. After analyzing the real-time status and location of the vehicles according to the eSeal and GPS data, and calculating the cost of each schedule, several new schedules are possible, which consider the breakdown of V1. The CFMS will provide the new optimal schedule where the cost is lowest (Table 7). In this case, V4 is on its way to Choi Hung to pick up the goods, and the GPS data show that V4 is near the breakdown point of V1. Therefore, V4 is assigned to pick up the cargo at the breakdown point of V1, and deliver it to Kwun Tong. Afterward, V4 continues to serve trip T19. The two remaining trips of V1, T30 and T18, are re-assigned. T30 and T18 are assigned to V5, and the schedule of V5 is re-arranged.

## 6. Evaluation of the prototype system

The evaluation aims to assess the overall value of the CFMS. Outcome evaluation consists of two phases; the <sup>fi</sup>rst phase is potential user (drivers) evaluation, and the second is domain expert (logistics managers and engineers) evaluation. The outcome evaluation of the prototype system is described below.

![](/api/attachments/5WF75Y9M/fulltext/images/2c4495468dfc09469fa71046e6b4f95d876619615facd8e8dcf626d25fa26c22.jpg)  
Fig. 6. Process before re-scheduling in CFMS.

A questionnaire survey was conducted among 20 potential users and seven experts after the completion of the system prototype

## Table 4

Composite context acquired from different primitive contexts.

<table><tr><td>Composite Context</td><td>Primitive Context</td></tr><tr><td>Location of the vehicle</td><td>GPS latitude and longitude coordinates</td></tr><tr><td>Mobility of the vehicle</td><td>Accident reporting data (crash/breakdown)</td></tr><tr><td>Expected time of arrival at the depot/client</td><td>Point-to-point travel time between districts</td></tr><tr><td>Goods departure time</td><td>eSeal log data</td></tr><tr><td>Goods arrival time</td><td>eSeal log data</td></tr><tr><td>Storage condition of the goods (appropriate/inappropriate)</td><td>Physical environment data of the goods (i.e., temperature and humidity)</td></tr></table>

implementation to evaluate the effectiveness of the developed CFMS. Eleven measurement items indicated by the <sup>fi</sup>ve-point Likert scale (1=strongly disagree, 3=undecided, 5=strongly agree) were used to assess the participant perception of the CFMS. The measurements are grouped into two sections, namely, system effectiveness and usability. The responses from both potential users and experts are summarized in Table 8.

The potential users rated each of the 11 items with mean scores ranging from 3.5 to 4.15, whereas the experts rated each item from 3.70 to 4.4. All mean scores were higher than the neutral value of the scale (i.e., 3=undecided). A one-sample t test using the neutral score as the test value was conducted for each item to ensure that the values of most median responses had a statistically signi<sup>fi</sup>cant difference from the neutral value, 3. Most of the items were significantly different from the test value at the 0.05 level; the only exception was item 6 from both potential users and the expert group. In general, all the participants agreed that CFMS can assist <sup>fl</sup>eet management in general, and real-time accident handling in logistics in particular. Moreover, the prototype can assist in managing the daily <sup>fl</sup>eet schedule and the communication with drivers/planner using PDAs.

![](/api/attachments/5WF75Y9M/fulltext/images/af7898716cf3c7e8ab12f7125223aec68e55a938f31e5c333bebb73eea22a897.jpg)  
Fig. 7. Relationship between sensors, contexts, and services.

Overall, the evaluation of the prototype system was satisfactory. The CFMS can clearly assist in the communication with drivers/planner, as well as in <sup>fl</sup>eet management in general and real-time accident handling in logistics in particular.

## 7. Contributions of the study

We have presented a design theory, which can help both logistics practitioners and researchers to build a <sup>fl</sup>eet management system that supports accident handling. Theory-based guidance, system architecture, and design and development principles are offered to logistics practitioners. For researchers, a number of theory-based principles subject to further empirical validation are identi<sup>fi</sup>ed. Fig. 10 summaries our CFMS design theory.

![](/api/attachments/5WF75Y9M/fulltext/images/e106302b56c78f27a0b5bd885e263cf3cba5e7be914c571fa17c75733db966a4.jpg)  
Fig. 8. Infrastructure of the context capture subsystem.

Table 5 Trips in the case study.

<table><tr><td>Trip ID</td><td>Time Window</td><td>Starting point</td><td>Ending point</td></tr><tr><td>T1</td><td>17:00</td><td>Kwai Chung</td><td>Central</td></tr><tr><td>T2</td><td>12:00</td><td>Mongkok</td><td>Sai Kung</td></tr><tr><td>T3</td><td>17:00</td><td>Quarry Bay</td><td>Shum Shui Po</td></tr><tr><td>T4</td><td>12:00</td><td>Chek Lap Kok</td><td>Yau Ma Tei</td></tr><tr><td>T5</td><td>12:00</td><td>Tsuen Wan</td><td>Shatin</td></tr><tr><td>T6</td><td>12:00</td><td>Lai Chi Kwok</td><td>Kwun Tong</td></tr><tr><td>T7</td><td>17:00</td><td>Cheung Sha Wan</td><td>North Point</td></tr><tr><td>T8</td><td>17:00</td><td>Kwai Chung</td><td>Tai Po</td></tr><tr><td>T9</td><td>12:00</td><td>Sai Kung</td><td>Yuen Long</td></tr><tr><td>T10</td><td>12:00</td><td>North Point</td><td>Hung Ham</td></tr><tr><td>T11</td><td>12:00</td><td>Causeway Bay</td><td>Tai Kwok Shui</td></tr><tr><td>T12</td><td>17:00</td><td>Kwai Chung</td><td>Ma On Shan</td></tr><tr><td>T13</td><td>12:00</td><td>Tai Po</td><td>North Point</td></tr><tr><td>T14</td><td>17:00</td><td>Shatin</td><td>Central</td></tr><tr><td>T15</td><td>12:00</td><td>Mei Foo</td><td>Kwun Tong</td></tr><tr><td>T16</td><td>12:00</td><td>Tseung Kwan O</td><td>Chek Lap Kok</td></tr><tr><td>T17</td><td>17:00</td><td>Sheung Wan</td><td>Kowloon Bay</td></tr><tr><td>T18</td><td>17:00</td><td>Kwai Chung</td><td>Chek Lap Kok</td></tr><tr><td>T19</td><td>17:00</td><td>Choi Hung</td><td>Tsuen Wan</td></tr><tr><td>T20</td><td>12:00</td><td>Tuen Mun</td><td>Causeway Bay</td></tr><tr><td>T21</td><td>12:00</td><td>Wanchai</td><td>Tsuen Wan</td></tr><tr><td>T22</td><td>17:00</td><td>Tai Po</td><td>Tsim Sha Tsui</td></tr><tr><td>T23</td><td>17:00</td><td>Yuen Long</td><td>Causeway Bay</td></tr><tr><td>T24</td><td>12:00</td><td>Tseung Kwan O</td><td>Tsuen Wan</td></tr><tr><td>T25</td><td>12:00</td><td>Tai Po</td><td>Wanchai</td></tr><tr><td>T26</td><td>17:00</td><td>Tsui Yi</td><td>Kwun Tong</td></tr><tr><td>T27</td><td>17:00</td><td>Tai Wai</td><td>North Point</td></tr><tr><td>T28</td><td>12:00</td><td>Quarry Bay</td><td>Cheung Sha Wan</td></tr><tr><td>T29</td><td>12:00</td><td>Cheung Sha Wan</td><td>Kwun Tong</td></tr><tr><td>T30</td><td>17:00</td><td>Mongkok</td><td>Tai Po</td></tr></table>

In this study, we have demonstrated how emerging information technologies can be applied to support decision making in vehicle scheduling and rescheduling. The eSeal data can enable the system to obtain the real-time status of the vehicle or cargo, such as when it is opened, passing the border, or if it is broken. The GPS data allow the CFMS to retrieve the real-time position of the crew, and the system can calculate the cost and time delay for the new schedule more accurately during an accident. The GPRS technology can transmit these real-time data to the server of CFMS for analysis. Therefore, combining several advanced information technologies, the proposed system can provide a more accurate and real-time vehicle scheduling.

Table 6 Initial vehicle assignment.

<table><tr><td>Vehicle</td><td>Route</td></tr><tr><td>V1</td><td>T16→T15→Lunch break→T30→T18</td></tr><tr><td>V2</td><td>T28→T29→T27→Lunch break→T26→T12</td></tr><tr><td>V3</td><td>T25→T24→T23→Lunch break→T22</td></tr><tr><td>V4</td><td>T20→T21→T19→Lunch break→T17</td></tr><tr><td>V5</td><td>T13→T10→T11→T14→Lunch break</td></tr><tr><td>V6</td><td>T9→T5→Lunch break→T1→T7</td></tr><tr><td>V7</td><td>T4→T2→T6→Lunch break→T3→T8</td></tr></table>

The proposed CFMS can bene<sup>fi</sup>t the transportation and logistics industries by providing the human scheduler with an accurate and optimal schedule for vehicle assignment. Therefore, the companies can save on cost and improve ef<sup>fi</sup>ciency if the schedule reduces the distance travelled by the vehicles and the size of the crew is optimal. Moreover, responding to accidents can be faster, and the new schedule that considers the accident is optimal.

The system prototype was reviewed by several logistics practitioners, and the overall response was positive. The most important comment was that the system could help capture a vehicle breakdown or an accident. The existing approach in handling such cases only relies on the experience and common sense of the human schedulers. The lack of visibility of the crew location and status usually makes the decision on rescheduling not optimal, or incorrect. However, using the proposed system, the human schedulers can make a fast, optimal, and accurate decision to re-assign vehicles and reschedule the trips.

## 8. Conclusion and recommendations for further study

The current paper described a design science approach for design and development of a <sup>fl</sup>eet management prototype system that supports accident handling, which can serve as a guideline to practitioners.

![](/api/attachments/5WF75Y9M/fulltext/images/af55a8d5c1a821a4d74d7d3851af4d263d3b9e38d5bedc71aaea82ad42ba346d.jpg)  
Fig. 9. Nodes in Hong Kong involved in the case study.

Table 7  
The new vehicle assignment.

<table><tr><td>Vehicle</td><td>Route</td></tr><tr><td>V2</td><td>T28 → T29 → T27 → Lunch break → T26 → T12</td></tr><tr><td>V3</td><td>T25 → T24 → T23 → Lunch break → T22</td></tr><tr><td>V4</td><td>T20 → T21 → T15 → T19 → Lunch break → T17</td></tr><tr><td>V5</td><td>T13 → T10 → T11 → T30 → Lunch break → T14 → T18</td></tr><tr><td>V6</td><td>T9 → T5 → Lunch break → T1 → T7</td></tr><tr><td>V7</td><td>T4 → T2 → T6 → Lunch break → T3 → T8</td></tr></table>

Based on the proposed design theory, a CFMS integrates the information technologies usually adopted in the transportation and logistics industries, to solve rescheduling problems in case of an accident. This is particularly useful for a logistics company, as the prototype system can help human schedulers <sup>fi</sup>nd the optimal schedule at minimum cost.

A case study was used to illustrate how CFMS can support an actual situation during a vehicle breakdown. The conceptual design of the prototype was validated through evaluation. Feedback was requested from potential users and logistics experts, who have an average of over 10 years of logistics operations experience. The evaluation of users and experts demonstrated the practical viability of the prototype, and they believed that the system could help achieve better <sup>fl</sup>eet planning and management.

Limitations exist for nearly all research projects, and this project is not an exception. First, GPS technology is used. If the vehicle is in the central business district where obtaining a view of the sky is dif<sup>fi</sup>cult, the system is unable to track and trace the vehicle. Second, although user acceptance of the system was not an issue during our system evaluation, note that the potential users in the case study are more exposed to IT-based novel systems. We anticipate that the issue of user acceptance may come from other users and managers, particularly in a conservative <sup>fi</sup>rm that does not tend to use new

Results of the Evaluation CFMS

<table><tr><td></td><td>Drivers Mean (n = 20)</td><td>Experts Mean (n = 7)</td><td>Students SD</td><td>Experts SD</td><td>t-test # (drivers)</td><td>t-test # (experts)</td></tr><tr><td colspan="7">The prototype system can</td></tr><tr><td>1. assist in maintaining customer information</td><td>3.70</td><td>3.90</td><td>1.26</td><td>0.90</td><td>2.48***</td><td>2.64**</td></tr><tr><td>2. assist in managing the daily scheduling of the fleet</td><td>3.70</td><td>3.80</td><td>1.08</td><td>0.85</td><td>2.89***</td><td>2.49**</td></tr><tr><td>3. assist in communication with the drivers/ planner (using PDA)</td><td>3.50</td><td>3.80</td><td>1.05</td><td>0.85</td><td>2.12**</td><td>2.48**</td></tr><tr><td>4. assist in fleet management in general</td><td>3.60</td><td>3.80</td><td>0.94</td><td>0.77</td><td>2.85***</td><td>2.74**</td></tr><tr><td colspan="7">The prototype system is</td></tr><tr><td>5. easy to use</td><td>3.65</td><td>4.00</td><td>1.22</td><td>0.86</td><td>2.38**</td><td>3.07**</td></tr><tr><td>6. easy to start up</td><td>3.40</td><td>4.00</td><td>0.99</td><td>1.22</td><td>1.80*</td><td>2.16*</td></tr><tr><td>7. user-friendly</td><td>3.60</td><td>4.20</td><td>1.04</td><td>0.44</td><td>2.58**</td><td>7.22***</td></tr><tr><td>8. stable and reliable</td><td>3.80</td><td>3.70</td><td>1.23</td><td>0.78</td><td>2.90***</td><td>2.37*</td></tr><tr><td>9. easy to learn</td><td>3.55</td><td>3.80</td><td>1.05</td><td>0.44</td><td>2.34**</td><td>4.81**</td></tr><tr><td>10. You can use the prototype without any difficulty</td><td>3.70</td><td>4.40</td><td>0.93</td><td>0.54</td><td>3.36***</td><td>6.85***</td></tr><tr><td>11. I likely to recommend it to others</td><td>4.15</td><td>4.00</td><td>0.74</td><td>1.00</td><td>6.94***</td><td>2.64**</td></tr></table>

1 – ‘strongly disagree’, 3 – ‘undecided’, 5 – ‘strongly agree’.  
\*p≤0.1; \*\* p≤0.05; \*\*\* p≤0.01 # Difference between respondents and neutral value.

![](/api/attachments/5WF75Y9M/fulltext/images/f5b36b0b8f0e1e9be4b8073a197c6f79179ceacf5f749c9f5b71110432fde10b.jpg)  
Fig. 10. A design theory for the CFMS for real-time accident handling.

technologies. Third, development of CFMS was based on a single case study, and our sample size of evaluation was small. The present study should be considered as only the beginning of research in this promising area.

The above limitations suggest several opportunities for further investigation. Can CFMS help in accident handling in logistics in a real world? Empirical studies on the use of context-aware DSS in <sup>fl</sup>eet management for accident handling in logistics are lacking. The prototype system has been evaluated as a proof of concept, and has been demonstrated in this study to be capable of supporting real-time accident handling in logistics in a quasi-real-world setting. Thus, a <sup>fi</sup>eld study of a larger scale that tests whether CFMS can help in real-time accident handling in logistics in a real-world setting should be conducted. Hence, the following hypotheses are put forward for testing:

H0. No signi<sup>fi</sup>cant difference exists between the outcomes of handling traf<sup>fi</sup>c accidents using CFMS and those that do not.

H1. A signi<sup>fi</sup>cant difference exists between the outcomes of handling traf<sup>fi</sup>c accidents using CFMS and those that do not.

## Acknowledgments

The authors are grateful for the constructive comments of the referees on an earlier version of this paper. This research was supported in part by a grant from the RGC of the HKSAR, China (project number B-Q11L) and The Hong Kong Polytechnic University under a Development of Niche Area research grant (grant number J-BB7Q).

## References

[1] D. Avramovich, T.M. Cook, G.D. Langston, F. Sutherland, A decision support system for <sup>fl</sup>eet management: a linear programming approach, Interfaces 12 (3) (1982) 1–9.

[2] J.C. Basnet, L. Foulds, M. Igbaria, FleetManager: A microcomputer-based decision support system for vehicle routing, Decision Support Systems 16 (1996) 195–207.

[3] H.E. Byrun, K. Cheverst, Utilizing context history to provide dynamic adaptations, Applied Arti<sup>fi</sup>cial Intelligence 18 (6) (2004) 533–548.

[4] J. Couillard, A decision support system for vehicle <sup>fl</sup>eet planning, Decision Support Systems 9 (1993) 149–159.

[5] K. Fagerholt, A computer-based decision support system for vessel <sup>fl</sup>eet schedule - experience and future research, Decision Support Systems 37 (2004) 35–47.

[6] J.I. Hong, E.H. Suh, S.J. Kim, Context-aware systems: A literature review and classi<sup>fi</sup>cation, Expert Systems with Applications 36 (2009) 8509–8522.

[7] J. Li, D. Borenstein, P.B. Mirchandani, A decision support system for the singledepot vehicle rescheduling problem, Computers and Operations Research 34 (2007) 1008–1032.

[8] M.L. Markus, A.L. Majchrzak, L. Gasser, A design theory for systems that support emergent knowledge processes, MIS Quarterly 26 (3) (2002) 179–212.

[9] E.W.T. Ngai, C.L. Li, T.C.E. Cheng, Y.H.V. Lun, K.H. Lai, J. Cao, M.C.M. Lee, Design and development of an intelligent context-aware decision support system for realtime monitoring of container terminal operations, International Journal of Pro duction Research 49 (12) (2011) 3501–3526.

[10] S. Sarker, A.S. Lee, Using a positivist case research methodology to test tree competing theories-in-use of business process reengineering, Journal of the Association for Information Systems 2 (1) (2002) 1–74

[11] C.G. Sorensen, D.D. Bochtis, Conceptual model of <sup>fl</sup>eet management in agriculture Biosystems Engineering 105 (2010) 41–50.

[12] J.G. Walls, G.R. Widmeyer, O.A.E.I. Sawy, Building an information system design theory for vigilant EIS, Information Systems Research 3 (1) (1992) 36–59.

[13] V. Zeimpekis, G. Giaglis, I. Minis, A dynamic real-time <sup>fl</sup>eet management system for incident handling in city logistics, Proceedings of IEEE 61st Vehicular Technology Conference 5 (2005) 2900–2904.

[14] V. Zeimpekis, G. Giaglis, I. Minis, Development and evaluation of an intelligent <sup>fl</sup>eet management system for city logistics, Proceedings of the 41st Hawaii International Conference on System Sciences, 2008.

[15] K.G. Zografos, K.N. Androutsopoulos, G.M. Vasilakis, A real-time decision support system for roadway network incident response logistics, Transportation Research Part C 10 (2002) 1–8.

Eric W.T. Ngai is a Professor in the Department of Management and Marketing at The Hong Kong Polytechnic University. His current research interests are in the areas of ecommerce, supply chain management, decision support systems and RFID technology and applications. He has over 100 refereed international journal publications in such forums as MIS Quarterly, Journal of Operations Management, Decision Support Systems, IEEE Transactions on Systems, Man and Cybernetics, Production & Operation Management.

Thomas K.P. Leung is an Associate Professor in the Department of Management and Marketing at The Hong Kong Polytechnic University. He has published two books and his journal papers have been widely available in such journal as Industrial Marketing Management, International Journal of Production Economics, European Journal of Marketing, Journal of International Consumer Marketing and others.

Y.H. Wong is associate professor, Department of Management and Marketing, The Hong Kong Polytechnic University. His publications include 3 books, Guanxi: Relationship Marketing in a Chinese Context, Handbook of Research on Ubiquitous Commerce for Creating the Personalized Marketplace, Financial Planning and Wealth Management and refereed journal articles, such as, Decision Support Systems, Industrial Mar keting Management, and International Business Review.

Maggie C.M. Lee is a Research Associate in the Department of Management and Marketing at The Hong Kong Polytechnic University. She has published in International Journal of Production Research and International Journal of Production Economics. Her current research interests are in the areas of IT system design theory, wireless sensor technology and applications, and RFID applications.

P.Y.F. Chai is a Research Associate in the Department of Management and Marketing at The Hong Kong Polytechnic University. He has published in Production Operations Management and International Journal of Production Economics. He is interested in supply chain management, decision support systems, data mining and in particular RFID and wireless sensor technology and applications.

Y.S. Choi is a Research Associate in the Department of Management and Marketing at The Hong Kong Polytechnic University. He has published in Production and Operations Management and International Journal of Production Economics. His current research interests are in the areas of green information systems, RFID applications, wireless sensor technology and applications. He has been working in the computer industry for more than 8 years.
