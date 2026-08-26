---
otero_id: 17695
otero_key: "47GRCKRM"
title: "FleetManager: a microcomputer-based decision support system for vehicle routing"
authors: "Chuda Basnet; Les Foulds; Magid Igbaria"
year: "1996"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(95)00010-0"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# FleetManager: a microcomputer-based decision support system for vehicle routing

Chuda Basnet $^{a}$ , Les Foulds $^{a}$ , Magid Igbaria $^{b,*}$

$^{a}$ Department of Management Systems, The University of Waikato, Hamilton New Zealand

$^{b}$ Program in Information Science, Claremont Graduate School, 130 East Ninth Street, Claremont, CA 91711, USA

## Abstract

We report on a decision support system (DSS) that recommends solutions to a particular version of the vehicle routing problem occurring in the New Zealand dairy industry. FleetManager is a DSS developed for use by New Zealand milk tanker schedulers and is designed to aid them in creating or improving milk tanker routes using their experience and preferences. The DSS uses multiple, resizable, overlapping windows to assist schedulers in their tasks. Users can also interact with the system through a graphical interface which displays a road map of the area and the location of the milk processing plants and milk suppliers. FleetManager also contains the option of automatically creating vehicle routes, which can be modified by the users. The system can be used to analyze a wide variety of “What-if?” scenarios with potential cost impacts.

Keywords: Vehicle scheduling; Milk tanker routing; Decision support systems; Microcomputer application; New Zealand

## 1. Introduction

Decision Support Systems (DSS) have emerged as the computer-based system to assist decision makers address semistructured problems by allowing them to access and use data and analytic models $[15,17]$ . Such systems have the following characteristics: They are interactive computer-based systems, they are aimed at semistructured problems, they utilize models with internal and external databases, and they emphasize flexibility, effectiveness, and adaptability. These characteristics have guided much of the research in the DSS area, but the potential benefits of DSS in the business environment has not been fully realized. Nevertheless, several cases have been reported in the literature $[1,3,6,7,11,12,16]$ . Most of them are either large-scale systems built to facilitate well-defined and repetitive decision tasks, or else they are small PC-systems offering quick and economic routines to support one-time decision making $[8]$ . This paper describes a PC-based DSS which addresses a non-routine and ill-defined decision environment.

Although the definition of the DSS concept has been elusive $[2,4,7,10,15,17]$ , the field has flourished with the development of computer technology. Keen $[10]$ reviewed the decade of DSS development and concluded that there is a need for balance between each of the three DSS elements: decision, support, and systems. He felt that more research effort on the decision component was required to restore this balance, as the technology for the system component was no longer the bottleneck. To achieve the “mission of DSS – helping people make better decisions,” Keen stressed the need for an active supporting role for “decisions that really matter.” This paper focuses on the decision component of the DSS.

PC technologies are becoming accepted and incorporated into organizations and our personal lives. PC-based systems have the potential to improve both individual and organizational performance. As decision makers recognize the potential benefits, many companies are investing in information technology. PC-based systems have been generally hailed as a revolution that will change the nature of professional work and transform the way people work. It is expected that almost all knowledgeable workers are likely to have their own PC to perform both stand-alone tasks and network services. Despite the proliferation of microprocessor-based systems, the potential benefits of these systems, as aids to managerial decision making, may not be fully realized due to poor design and low acceptance by users. It is recognized that individuals are sometimes unwilling to use these systems, even if the system may increase their productivity. While some of these systems may have an impact on individuals and organizations, the adoption and acceptance of these systems among decision-makers has been limited. This may be due to the inflexibility in the systems as well as their narrow design. Therefore, it is important to understand the environment of the decision makers and the type of support they need in order to make effective decisions, and to examine the models appropriate for addressing their problems.

In this paper we describe a PC-based DSS, called FleetManager, which addresses the milk tanker routing scenario in the New Zealand dairy industry. It incorporates vehicle routing and judgmental models. The purpose of the system is to help the vehicle schedulers of the dairy companies build the schedules using their experience and preferences, and it can also be used as a strategic planning tool. The system evolved as a result of several years of collaboration between vehicle schedulers and researchers at the Department of Management Systems, The University of Waikato, New Zealand.

In the first part of the paper, we present a description of the New Zealand dairy industry focusing on the issue of efficient milk tanker routing. The second part of the paper describes the formulation and development of a DSS for this environment. Finally, we illustrate how the DSS was used in practice to improve tanker routing efficiency.

## 2. Overview of milk tanker scheduling

Throughout New Zealand, dairy companies are faced with the question of how to collect milk from their supplier farms efficiently, using road milk tankers, and have it delivered to their factories for processing. The dairy companies operate one or more factories, each of which has a daily demand for milk that must be satisfied. They also operate fleets of milk tankers over two shifts per day. The bases, where the tanker fleets are maintained, may be at sites other than factories. Each company has contracts with hundreds of farmers (suppliers) to supply milk usually (but not always) daily to the company. The amount of milk produced by each supplier varies daily and must be estimated. The company's vehicle schedulers operate the tanker fleet within location, budget and other constraints attempting, among other objectives, to minimize the cost per kilogram of milk delivered to the factories.

In order to achieve this objective, suppliers are grouped together into what is called a run: a sequence of suppliers which are visited by a tanker in a specific order (The complete set of runs for a shift is called a schedule). The runs must be developed and then allocated to the factories so as to satisfy the demands of each factory. This also involves assigning a tanker to each run. The initial run for each tanker begins at its base, visits the suppliers of the run in the order specified, and then ends at the factory for that run (which may be at a different location from the initial base). Subsequent runs of the tanker will begin at that factory and may well end at another factory. It is usually efficient to attempt to orchestrate the final run of the shift for each tanker to end at its base (when the base is a factory with positive demand) in order to minimize empty running. Because some suppliers have a relatively low output at certain times of the season, it is not considered worthwhile to visit them daily. Thus part of the allocation problem is the identification of which suppliers are to be visited in the current shift. There is also the question of the accurate prediction of supplier output. Further, a judgment has to be made as to when frequency of visiting a particular supplier is to be either increased or decreased, due to a change in output.

Tanker schedulers often approach these issues by first establishing which suppliers are to be visited during a given shift and then allocating them to the different factories in order to satisfy factory demand. If there has been no significant change from a previous similar shift, the runs of that shift are usually modified in order to generate the runs for the present shift. In examining previous runs, schedulers often ask themselves two key questions:

1. What are the requirements of a new schedule which differ from the previous schedule?; and

2. How should the previous schedule be modified in order to create a satisfactory new schedule?

The first question usually involves constraints governing the feasibility of any new schedule. The second question involves not only these constraints but also the measurement of how satisfactory the new schedule is, in terms of various objectives. The New Zealand dairy company vehicle schedulers have traditionally used a large-scale map together with coloured pins displaying the suppliers. A manual file system was used for handling the information concerning the suppliers and the tankers, and for creating the schedule.

The dairy industry in New Zealand has been restructured and as a result many companies have been consolidated. The vehicle routing problem therefore became even more complex because of the significant increase in the number of suppliers, tankers, and factories. This has often led to a drastic decrease in the quality and timeliness of the schedules generated by the manual system. The dairy companies invited us to study their operations and vehicle routing methods and recommend areas for improvement. Recognizing the importance of both models and judgmental considerations, the dairy companies together with the authors studied the companies' operations and vehicle routing methods and decided to develop a DSS to address the issue of milk tanker routing. We now present a DSS designed to aid the vehicle schedulers of the dairy companies.

## 3. The DSS environment

The traditional large-scale map, together with coloured pins displaying the farms, is a very useful visual aid and, in order to gain acceptance, it is productive for a DSS to contain a computerized map which is used in place of the large-scale map. Geographical features and all relevant locations can be represented on the screen as a result of digitizing their coordinates. Relevant factory, milk tanker, and supplier information can be represented by using a colour graphics display system with windows and pull-down menus. This allows a complementary combination of skills. The schedulers have the skill, superior to that of the computer, to recognize patterns in the location of suppliers and routes. Based on these patterns, the scheduler can create or modify the schedules. The use of a computerised map permits the computer to present immediately to the scheduler the consequences of these options. The scheduler then chooses an option, and the computer updates the schedule. Such a scheduler-computer combination marries the pattern recognition skills and the specialized knowledge that the experienced scheduler usually has, along with the numerical and recall ability of the PC.

To develop the DSS, we held a series of discussions with vehicle schedulers and other concerned individuals over a period of time. This helped us to understand their needs and requirements. In order to meet the schedulers' needs and requirements and follow their decision making processes, possible main-menu functions of a DSS were developed. These functions are needed by the schedulers to identify the requirements of the new schedule and to create a satisfactory new schedule.

1. File open/close: in order to begin the process of new schedule generation, based on a previous schedule, the scheduler must first be able to access the previous schedule. Schedulers should be able to open and manipulate all the data files: suppliers, tankers, road network, etc.

2. Schedule checking: There should be some means whereby the scheduler can ascertain how well a schedule will meet the requirements of the scheduler. A schedule may be checked for: tanker capacity, amount of milk collected from individual suppliers, amount of milk remaining in the vats of suppliers, and distance travelled.

3. Schedule modification: Having pinpointed where a schedule is deficient, the scheduler must then devise modifications to it which produce a satisfactory new schedule. The system must allow for modification of existing schedules by such means as:

\- adding a new supplier to a run;

\- deleting a supplier from a run;

• transferring a supplier from one run to another;

\- interchanging suppliers between different runs; and

\- creating a new run.

These functions should be guided by the provision of relevant statistics associated with them, such as, tanker capacity utilization and run duration. Naturally, there must be a mechanism whereby the new schedule can be recorded.

It is also desirable that the DSS can be used to respond to enquiries and to address questions concerning changes to the size of the tanker fleet base, the acquisition of new suppliers or the location of a new factory. In these cases, and other similar inquiries and questions, it is not a modification of an existing schedule, rather a construction of a complete schedule from scratch. This is appropriate in a start-up situation, or when there are significant changes in the conditions or data which trigger a rationalization of resources. This task can be accomplished by carrying out systematically the clustering of suppliers into subregions. We now introduce the system structure of our DSS which has been devised for the New Zealand dairy industry.

## 4. The system structure

The DSS (called FleetManager) was developed at the University of Waikato for use by New Zealand milk tanker schedulers. It can be categorized as a Specific DSS (SDSS). It is divided into three components: the user-interface, the modelling base and the database. The integration of the three components of the SDSS, i.e., the structure of our SDSS, is presented in Fig. 1. It was written in Turbo Pascal version 6.0 for an IBMcompatible PC with a high resolution colour monitor. we made several revisions to make the system more robust and user-friendly. Currently it is used as a PC-based decision support system with the capability of communicating with the company mainframe computer, mainly to import the information necessary to support it, including the updating of supplier outputs. We also incorporated some strategic planning tools to create runs and examine the effects of changes in the milk yield, factory demands, shifts, and tanker capacities. The system includes a digitized map of the area of operations of the dairy company which shows all relevant locations and roads. The system is composed of pull-down menus, windows which display factory, suppliers, and milk tanker information, and is user-friendly and mouse-driven. It can be used to create new, or to improve existing, milk tanker routes.

![](/api/attachments/47GRCKRM/fulltext/images/a22fe1fee0a147b2a6466571bb6615700fcf5016d7588d9014ee87edc51fb7e4.jpg)  
Fig. 1. A conceptual model of milk tanker routing.

The assignments of suppliers to milk tanker runs can be automatically generated and then manually fine-tuned to meet user's specific needs. The system makes its recommendation to the scheduler by displaying the information on a digitized map of the area of operations of the dairy company, which shows all the relevant locations and roads. The system displays the map containing all relevant locations and roads and the scheduler modifies runs by clicking with a mouse on the locations of suppliers. When a schedule has been decided upon, the final assignments (run-sheets) to be used by the tanker drivers can be printed. Additional summary information about suppliers and scheduled tanker runs is provided, as are warnings of possible routing oversights such as unscheduled suppliers and overfull tankers. Various statistics are automatically generated, such as the percentage of vehicle capacity utilized, distance travelled.

## 4.1. Database and model base components

The system maintains a database of suppliers, tankers, roads, factories, and base information that can be interactively entered and updated. This includes such information as: supplier name, location, milk tank capacities, current output rate, tanker capacities, and road segment coordinates.

This database can be easily accessed and manipulated through a File module. The database is initially created by the scheduler using this module. However, the digitized coordinates of the supplier locations and the road segments were supplied by the Department of Survey and Land Information of the New Zealand Government. Schedules can also be saved and recalled for use in future routing. The information on the actual milk output collected from each supplier is lodged with the company wide mainframe database. The mainframe writes this out to a file. FleetManager accesses this file to prepare an estimate of the milk output of suppliers.

Models are used by FleetManager to suggest schedules to the user. The Sweep Algorithm of Gillet and Miller [5] is available to form the runs. Suppliers with sufficient milk in their tanks are first identified using estimates and preset criteria. This algorithm then forms clusters of these suppliers. Each cluster is allocated to a tanker. A cluster is formed by rotating a vertical plane around the factory. As long as the tanker capacity is not exceeded, any supplier swept by the plane is included in the cluster. The Farthest Insertion Algorithm [14] is available to determine the sequence of suppliers in a run to minimise the distance travelled. In this algorithm, the run is successively formed by adding to the current run a supplier which is farthest from the suppliers in the current run. Every time a supplier is added, it is inserted in such a position in the run that the total distance is minimized. A linear interpolation scheme is used to forecast the milk output. In this scheme, a gradient is established by looking at the previous output and the current output. This gradient is then used to forecast milk output for the next shift. These estimates can be altered by the schedulers based on their subjective judgment and experience concerning such factors as the amount of rainfall, and the passage of time since the beginning of the milk producing season.

## 4.2. User-interface component

The interface component has three subsystems: (1) the window based user-interface; (2)

graphical user interface; and (3) automatic schedule creation.

## 4.3. The window-based user interface

The DSS is composed of five modules: ABOUT, FILE; AUTO; SCHEDULE; VIEW; and OPTIONS. The window based user interface is illustrated in Fig. 2.

The pull-down menus give access to the modules. Each module includes a secondary menu of procedures. All procedures are independent and can be used in any order. All data can easily be stored for further processing. A short description of the modules and their procedures follows.

The FILE module provides file manipulations, exit, and DOS-shell functions. FleetManager automatically loads the supplier, tanker, factory, roads and base files. These files are used in the routing process and can be viewed and edited using the File Open menu command.

The AUTO module provides for the use of FleetManager to generate automatically all schedules and to examine the effects of changes in milk yield. The schedule is constructed for all current suppliers using the tankers available for that shift.

FleetManager also allows users to edit manually supplier outputs. The SCHEDULE module provides most of the schedule manipulation functions. There are provisions for looking at a summary of the schedule, to edit a run (including swapping of suppliers between runs) and to check the performance of the schedule. The system also provides the scheduler with a summary of all runs of a schedule for a given shift. It also allows the users to print the run sheets as well as supply tickets (a list of runs with a corresponding supplier number). The SCHEDULE module also allows the user to view a summary of the tanker runs currently scheduled and the total milk to be collected by each tanker. For every run, a list of suppliers currently assigned to it, the capacity of the tanker, the total of milk assigned and the total distance to be travelled are presented. Runs in which total milk collection exceeds a user-specified percentage of the tanker capacity are displayed in red. Additionally, supplier vat estimates which exceed the user-specified percentage are also displayed in red.

The user can also modify the schedule by moving suppliers from one run to another. The system is also able to modify and fine tune existing schedules including the transfer of suppliers between runs and shifts. The system allows the user to remove a supplier from a run and not schedule it on any other run. Using the SWAP RUNS function, the system also allows the user to swap the complete set of suppliers on one run with the suppliers currently assigned to another run.

![](/api/attachments/47GRCKRM/fulltext/images/88e77a5ddf2cdb686bc198af24c66351a69816f0819266f62f38c2feffabdc90.jpg)  
Fig. 2. Menu function.

FleetManager also has a VIEW menu which allows the user to query the DSS about the suppliers. The system displays sets of suppliers which satisfy certain user-selectable criteria. The user can specify the following criteria: display all suppliers; display only those suppliers whose current uncollected total output exceeds a user-specified percentage of their milk holding tank (vat); display only those suppliers that are estimated to have less than a certain user-specified percentage of their vat size or with less than a specified litre vat estimates; or display only those suppliers which have been split between two or more runs or whose vat estimate have been only partially assigned to a run.

## 4.4. The graphical user interface

A second user interface is the graphical user interface. Both, the graphical user interface and the window based interface can be accessed from each other at the touch of a button. The graphical interface displays a road map of the area and the location of the suppliers. The interface has provisions for zooming and panning. In order to build up a run, the user successively selects the supplier locations. Suppliers may be removed from runs or the output may be split between different runs. Information on current run and current supplier is continually updated and displayed.

## 4.5. Automatic schedule creation

FleetManager contains the option of automatically creating the runs. It can automatically generate a schedule using information from the user or a database, provide a schedule without the intervention of the user, and display or print the schedule or an individual run in a way that can easily be understood by most schedulers. Because users are often reluctant to use the solution of a model they do not understand (Turban [15] and Sprague and Carlson [12] listed “understandable model-base” as a desirable DSS characteristic), it was proposed that the system provides suggested schedules, which can be modified by the user. This option is also useful as a planning tool, where the system allows the user to have the “what-if” queries by examining the effect of changes in the milk yield, factory demands, shifts, and tanker capacities. The automatic creation of routes involves the following steps: the assignments of suppliers to factories, the assignments of tankers to factories, the creation of an initial run for each tanker and the assignment of subsequent run to each tanker from a factory.

We should stress that our models do not generate schedules satisfying all the various constraints while recognizing the complicating factors that were mentioned earlier. Rather, the use of our models is to suggest an initial schedule. This schedule may then be modified by the scheduler in the light of those complicating factors. Automatic schedule generation may also be used as a strategic planning tool in which various options can be tested and the costs of those can be compared.

In summary, the proposed DSS (FleetManager) can accommodate the following:

\- Multiple shifts;

\- Supplier vat size limitation;

\- Suppliers that are visited on less than a daily basis and the capability of judging how often a supplier should be visited;

\- Tanker capacity;

\- The ability to identify suppliers of various output sizes not yet visited;

\- The ability to identify tankers with spare capacity during run construction;

\- The ability to modify and fine tune existing schedules including the transfer of suppliers between runs and shifts, a summary of all runs of a schedule for a given shift;

\- The allocation of the total output of each shift among various destinations; and

\- Warnings concerning illogical outcomes, such as unvisited suppliers and overloaded tankers. FleetManager includes all of the characteristics of an effective DSS from the generic DSS framework of Sprague and Carlson [12] and Turban [15]:

\- It supports but does not replace the decision-maker. It should therefore neither try to provide the “answers” nor impose a predefined sequence of analysis;

File Auto Schedule View Window Options - It supports a semi-structured decisions, where parts of the analysis can be systematized for the computer, but where the decision maker's insight and judgment are needed to control the process;

\- It combines modeling techniques with database and presentation techniques;

\- It emphasizes ease of use, user friendliness, user control, and flexibility and adaptability;

\- It supports all phases of decision making;

\- It interacts with other computer-based systems, mainly with the company mainframe system to download and upload information.

## 5. Implementation and illustration of the decision support system

FleetManager has been implemented on IBM-PC compatible with a Super VGA monitor. It was developed using a prototyping approach (“The iterative (prototyping) approach is most common in DSS since the information requirements are not known precisely” [15], p. 304). The core of the DSS was written in a general-purpose programming language – a set of Pascal subroutines and library functions. Systematic testing assured that each process was error-free before the next layer of complexity was added. Implementation enabled the team to work on both the model building and the interface between other components of the systems, allowing for periodic testing of their enhancements and progress and checks on performance of the whole system. The need for involvement and participation of the potential users was recognized right from the beginning.

Version 1.0 was first developed and following users' feedback and reaction, the system was refined, expanded and modified. The changes have largely occurred in the area of transferring information from other systems to FleetManager and in the implementation of the graphical interface. Minor changes have also been made to other areas. The layout of the files that make up the FleetManager system has also been improved.

![](/api/attachments/47GRCKRM/fulltext/images/7e612ccc12951695654398bd7f8d9419e548d8b957fabfe6ac372605841d5359.jpg)  
Fig. 3. Modifying a tanker run.

We now give an example to illustrate the use of FleetManager by the Dairy companies. Fig. 3 shows a window displaying a summary of all the generated runs (the top window). All the runs can be modified. If the scheduler wants to edit a particular run (say run 2 of tanker 14) the scheduler needs to select it by double-clicking on it. The system then automatically displays the bottom part of Fig. 3 (the run window). At this point, the output of a supplier can be removed from the

![](/api/attachments/47GRCKRM/fulltext/images/24e71a7442460a1ca804cef142d81b26fdc4bd0d68923179676a43ef1edd498f.jpg)  
Vehicle Maintenance Required:

Fig. 4. A run sheet.

![](/api/attachments/47GRCKRM/fulltext/images/8abff95cd029dfb109dd2b05a123d374195faf8438b4db71015ed5e4427b4583.jpg)

![](/api/attachments/47GRCKRM/fulltext/images/1964761ec82421c27d1b26c565e0f859e937653b30323036c4a120fd022ac27d.jpg)  
Fig. 6. A warning window.

run or partly or wholly transferred to another run. This is a very important feature of the DSS, making it a useful tool to respond to different circumstances.

Fig. 4 presents the run sheet for a particular run to be given to the tanker driver concerned. It shows the number and the name of the suppliers in the order they have to be visited, and the estimates of the suppliers' output. Tanker drivers are required to complete the sheet by filling in the actual milk collected from each vat of the supplier, total milk collected, and the temperature of the collected milk. This sheets is used to update the record of milk collections.

Fig. 5 shows the window that permits the user to query the DSS regarding suppliers and a schedule. The scheduler can generate reports by specifying the type of suppliers (display all suppliers; suppliers usually collected in the current shift; scheduled suppliers; unscheduled suppliers; or others) and the attributes of these suppliers (all; estimated milk exceeding x% of their vat capacity; less than x% of their vat capacity; less than x litres; suppliers whose output is split between tankers; or in a particular area). The report can be sorted by the milk suppliers' ID, name, area, or estimate of the milk.

The system can also display the deficiencies of a schedule. Fig. 6 illustrates a warning window. In this example, there are four types of warning characteristics: some suppliers which exceed 80 percent of their vat capacity have not been scheduled; some suppliers which have less than 12 percent of their vats full are scheduled for collection; some tankers runs have more than 80 percent of their capacities; and some tankers runs have less than 3 percent of the tanker capacities. When one of the four is selected, the system displays corresponding list of suppliers or tankers.

![](/api/attachments/47GRCKRM/fulltext/images/7459499f4101b2d5834ced23306ce38295ec015857bf70fa89fd6d59bacf13be.jpg)  
Fig. 7. The graphical interface.

An example of the use of the graphical interface screen is shown in Fig. 7. The information about the current tanker run is displayed at the top left and the current supplier information is shown underneath. FleetManager displays the suppliers' location using the following colour scheme:

RED Unscheduled or partially scheduled suppliers

GREEN Scheduled (including fully scheduled split) suppliers

PINK Suppliers scheduled on the current run

BLACK Other suppliers

This display with colour aims to simplify the system and emphasize the ease of use and flexibility and adaptability of the system.

The DSS has been in use in a dairy company over a year. Initially, teething problems were encountered and some bugs were discovered. There were gaps in our perception of the functions of the DSS and the desires of the users. There were also gaps in communicating the instructions to be followed. After a year of usage, the schedulers have expressed satisfaction with the DSS. The time spent by the schedulers in preparing the schedules have been cut significantly and the boredom of the task has been reduced, thus freeing the schedulers for more creative tasks. However, it is too early to gather evidence of actual savings of transportation costs.

## 6. Conclusion

We introduced a DSS, called FleetManager, which is designed to address issues concerning milk tanker routing that commonly occurs within the New Zealand dairy industry. A conceptual model for providing a decision support system for vehicle routing has been presented. FleetManager was designed to assist vehicle schedulers in every step of the vehicle routing process. It does not automate the decision-making process but helps vehicle schedulers by providing powerful tools to create schedules, choose between plans, generate alternative plans, and to assess alternative plans with respect to given criteria. The system allows the scheduler to create vehicle routes automatically, minimize the total distance travelled, and to manually override created routes. It allows for more than one source or destination, skip a-day clients, multiple shifts, as well as fine tuning.

In general, DSS benefits are often uncertain and are difficult to assess. In our case, with the prototyping approach, where development is evolutionary, this is especially the case. The ongoing schedule changes and changing environments make it even more so. The true value of a DSS is whether it improves a manager's decision making, which is not easily measured. Therefore, the traditional cost-benefit analysis will not be able to capture all DSS benefits $[9,15]$ . Actually in some cases, it may not be well-suited to the DSS. However, some of the benefits in our case can be measured, such as a reduction in milk collection costs. The use of FleetManager as a DSS may also result in a reduction in labour costs. The system also has tangible and intangible benefits. It can benefit the schedulers in the fine tuning of existing schedules, creation of entirely new schedules, strategic planning for new sites, efficient fleet utilization, and the flexibility to plan for and cope with unexpected situations. The DSS also allows the scheduler to carry out ad hoc analysis through “what-if?” queries. It also provides the scheduler with a better understanding of the business, where the system can alert users concerning illogical outcomes such as unvisited suppliers and overloaded tankers. In summary, this papers show that the milk tanker routing problem is a complex management process involving subjective and objective information and judgments. FleetManager is designed to deal with such complex situations.

## References

[1] B. Arinze, M. Igbaria and L.F. Young, A Knowledge Based Decision Support System for Computer Perfor-

mance Management, Decision Support Systems 8, No. 6 (1992) 501–515.

[2] R.H. Bonczek, C.W. Holsapple and A.B. Whinston, Foundations of Decision Support Systems (Academic Press, New York, NY, 1981).

[3] J. Couillard, A Decision Support System for Vehicle Fleet Planning, Decision Support Systems 9, No. 2 (February 1993) 149–159.

[4] M.C. Er, Decision Support Systems: a Summary, Problems, and Future Trends, Decision Support Systems 4, No. 3 (September 1988) 355–363.

[5] B. Gillet and L. Miller, A Heuristic Algorithm for the Vehicle Dispatch Problem, Operations Research 22, No. 2 (March-April 1974) 340–349.

[6] M. Gopalakrishnan, S. Gopalakrishnan and D.M. Miller, A Decision Support System for Scheduling Personnel in a Newspaper Publishing Environment, Interfaces 23, No. 4 (July August 1993) 104–115.

[7] P. Gray, Ed., Decision Support and Executive Information Systems (Prentice-Hall, Englewood Cliffs, NJ, 1994).

[8] G. Islei, G. Lockett, B. Cox, S. Gisbourne and M. Stratford, Modeling Strategic Decision Making and Performance Measurement at ICI Pharmaceuticals, Interfaces 21, No. 6 (November-December 1991) 4–22.

[9] P.G.W. Keen, Value Analysis: Justifying Decision Support Systems, MIS Quarterly 5, No. 1 (March 1981) 1–16.

[10] P.G.W. Keen, Decision Support Systems: the Next Decade, Decision Support Systems 3, No. 3 (September 1988) 253–265.

[11] R. Ravichandran, A Decision Support System for Stochastic Cost-Volume-Profit Analysis, Decision Support Systems 10, No. 4 (November 1993) 379–399.

[12] R.H. Sprague and E.D. Carlson, Building Effective Decision Support Systems, (Prentice-Hall, Englewood Cliffs, NJ, 1982).

[13] R.H. Sprague and H.J. Watson, Decision Support for Management (Prentice-Hall, Englewood Cliffs, NJ, 1996).

[14] M.M. Syslo, N. Deo and J.S. Kowalik, Discrete Optimization Algorithms (Prentice-Hall, Englewood Cliffs, NJ, 1983).

[15] E. Turban, Decision Support and Expert Systems: Management Support Systems, Third Edition (Macmillan Publishing Company, New York, NY, 1993).

[16] H.S. Weigel and S.P. Wilcox, The Army's Personnel Decision Support System, Decision Support Systems 9, No. 3 (April 1993) 281–306.

[17] L.F. Young, Decision Support and Idea Processing Systems (W.C. Brown, Dubuque, Iowa, 1989).

Chuda Basnet is a Senior Lecturer at the University of Waikato in New Zealand. He received a M.S. in Industrial and Management Engineering from Montana State University and a Ph.D. in Industrial Engineering and Management from Oklahoma State University. His current research interests include vehicle routing, manufacturing systems modelling, and production planning and control.

Les Foulds completed a doctorate in industrial engineering and operations research at Virginia Polytechnic Institute in 1974 and spent 1975 as a visiting lecturer in operations research at the University of Canterbury in New Zealand. He spent the next 4 years lecturing on optimization at Massey University, also in New Zealand. He returned to become a senior lecturer, for 1980–1983, to the Economics Department at the University of Canterbury. Then he went to the University of Florida as a professor of systems engineering for 1984 and 1985. He then settled at the University of Waikato, (New Zealand) where he was the Dean of the School of Management Studies from 1986–1990 and then the foundation chair of the new Department of Management Systems. His research interests were initially at the theoretical end of Operations Research; in combinatorial optimization and graph theory/networks. Over the last 20 years he has gradually mellowed into doing more and more applied work: evolutionary trees, to facilities planning, to vehicle scheduling and the interface between OR and operations management, especially quality management and world class manufacturing. He has published over 100 papers and 8 books in the above areas.

Magid Igbaria is a Professor of Information Science at the Claremont Graduate School. He spent a year as a Visiting Professor of Decision Sciences at the University of Hawaii in Manoa and a Professor of MIS, College of Business and Administration, at Drexel University, and lectured at the University of Waikato in New Zealand, Tel Aviv University, Hebrew University and Ben-Gurion University in Israel. He holds a B.A. in Statistics, and a M.A. in Information Systems and Operations Research from Hebrew University; he received his Ph.D. in computers and Information Systems from Tel Aviv University. His current research interests focus upon DSS, IS personnel, computer technology acceptance, management of IS, virtual workplace and teleworking, cross-cultural differences in IS, and international IS.
