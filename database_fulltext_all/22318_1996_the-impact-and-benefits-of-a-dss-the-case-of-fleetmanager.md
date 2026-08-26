---
otero_id: 22318
otero_key: "YA6NSKWY"
title: "The impact and benefits of a DSS: The case of FleetManager"
authors: "Magid Igbaria; Ralph H. Sprague; Chuda Basnet; Les Foulds"
year: "1996"
journal: "Information & Management"
doi: "10.1016/s0378-7206(96)01078-6"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Case Study

# The impact and benefits of a DSS: The case of FleetManager

Magid Igbaria $^{a,b,*}$ , Ralph H. Sprague Jr. $^{c}$ , Chuda Basnet $^{d}$ , Les Foulds $^{d}$

$^{a}$ Program in Information Science, Claremont Graduate School, 130 East Ninth Street, Claremont, CA 91711, USA $^{b}$ Faculty of Management, Tel Aviv University, Ramat Aviv, Tel Aviv 69978, Israel

$^{c}$ Department of Decision Sciences, College of Business Administration, University of Hawaii, 2404 Maile Way, Honolulu, HI 6822, USA $^{d}$ Department of Management Systems, The University of Waikato, Hamilton, New Zealand

## Abstract

A DSS used for vehicle routing at the Westland Co-operative Dairy Company Ltd., New Zealand, is providing a spectrum of benefits and business values. Labor hours, required by the schedulers, have been significantly reduced; the schedules they develop are more efficient, the number of truck drivers has been reduced even though the volume of the traffic is increasing, and the Transport Office has a greater flexibility and higher morale. The system includes powerful tools to plan schedules, choose plans, generate alternative plans, and assess alternative plans with respect to the given criteria. The system also allows the scheduler to create routes automatically, minimize the total distance traveled, and manually modify routes created by a model. It also has several classic characteristics that are too seldom actually realized: it leverages the judgment of the DSS user; it has evolved over time through an iterative development process and is being adapted for use in another company. Taken together, these benefits and attributes make the system a rare example of a successful DSS that can provide guidance for the development of other systems in the important problem domain of vehicle routing.

Keywords: Business performance; Decision support system; Impact; Milk tanker routing; New Zealand; Vehicle scheduling © 1996 Published by Elsevier Science B.V.

## 1. Introduction

Since the early 1970s, Decision Support Systems (DSS) have emerged as a way, over the years, to help people perform information-handling activities to attain goals, pursue objectives, and solve problems. DSS have been characterized as interactive computer-based systems that help users perform semistructured tasks, utilize models with internal and external databases, and provide flexibility, effectiveness, and adaptability. Even though the definition of the DSS concept has been elusive [4, 9, 12, 20], DSS have been developed and used effectively in organizations. However, judging from the examples of DSS reported in the literature, [1, 3, 6, 15, 16], the majority of these cases are either large-scale systems built to facilitate well-defined and repetitive decision tasks, or they are small PC-systems offering quick and economic routines to support one-time decision making [10].

This paper first describes a PC-based DSS that addresses a non-routine and ill-defined decision environment. It stresses on a DSS that uses models, not just to create a ‘solution,’ but also to leverage the judgment of the decision makers. Then, it analyzes a spectrum of benefits and impacts that have been realized by the company through the use of the system. The spectrum includes a significant reduction in the labor time, more effective and efficient decisions, and higher morale among the users. The result is a rich blend of quantitative and qualitative benefits and impacts.

To a large extent these benefits derived from characteristics of the system – which, although generally thought of as a part of the classic model of DSS – are seldom actually realized. First is the way the system leverages the judgment and intellect of the user. The comfortable user interface encourages a level of interaction that enables the user to explore many alternative decision sets suggested by their experience, judgment, and intuition. Second, the system has evolved significantly over time a process of interactive design involving substantial interaction between the builders and users. More than just simple back-and-forth iteration of specifications, the system has acted as a platform for the collaborative development of each incremental advance. Third, the system has the ability to act as a DSS generator [18] as evidenced by its adaptation to another company.

The problem of evaluating DSS, and especially of measuring their benefits, was recognized in the early 1980s [11]. Many quantitative benefits that are important in improving the profitability and performance of the company have been identified [14, 17, 21]. In addition, there are significant qualitative benefits, many of them behavioral, that are important in improving the performance and quality of working environment of the decision makers [8, 13, 22]. This paper examines both the qualitative and quantitative impact and benefits of a DSS.

The DSS we describe here is called FleetManager: it addresses a milk tanker routing problem in the New Zealand dairy industry. It incorporates vehicle routing and judgmental models. The purpose of the system is to help the vehicle schedulers of the dairy companies plan the schedules using their experience and preferences. It has also proven valuable as a strategic planning tool. The system evolved as a result of several years of collaboration between the vehicle schedulers at the Westland Dairy Company and researchers at the Department of Management Systems, The University of Waikato, New Zealand.

## 2. The problem

Throughout New Zealand, dairy companies face the need to collect milk efficiently from their supplier farms using road milk tankers and have it delivered to their factories for processing. The dairy companies operate one or more factories, each of which has a daily demand that must be satisfied. They also operate fleets of milk tankers over two shifts per day. The bases, where the tanker fleets are maintained, may be at sites other than the factories. Each company has contracts with hundreds of farmers (suppliers) to supply milk, usually (but not always) daily to the company. The amount of milk produced by each supplier varies daily and must be estimated while developing schedules.

Additionally, the dairy industry in New Zealand has been restructured and, as a result, many companies have been consolidated. The vehicle routing problem, therefore, has become even more complex because of a significant increase in the number of suppliers, tankers, and factories. This has led to a drastic decrease in the quality and timeliness of schedules generated by a manual system. The objective, therefore, was to allow vehicle schedulers to operate the tanker fleet within the location, budget and other constraints, while minimizing the cost of milk delivered to the factories.

The company to address this problem most aggressively has been the Westland Dairy Company. Westland was formed on November 1, 1937. It has its base at Hokatika, on the West Coast of the South Island of New Zealand, and manufactures dairy products as part of the New Zealand Dairy Industry Co-operative movement. In 1992, it processed approximately 2 percent of New Zealand's milk flow. Annual milk intake is approximately 142 million liters supplied by its 322 dairy farms located between Karamea at the north to Franz Josef at the south, a distance of about 380 kilometers. Ten tanker vehicles travel approximately 1.3 million kilometers collecting milk annually. The average farmer milks 125 cows which produce 21 700 kilograms of milk. In the last few years, there has been an annual growth of approximately 5 percent in milk production, so Westland was looking for ways to improve the productivity and efficiency of its operations continuously. The development of the vehicle routing DSS became a part of that overall effort.

## 2.1. The current approach

Suppliers are grouped into what is called a 'run': a sequence of suppliers visited by a tanker in a specific order. The complete set of runs for a shift is called a schedule. The runs must be developed and then allocated to the factories to satisfy their demands by assigning a tanker to each run. The initial run for each tanker begins at its base, visits the suppliers in the order specified, and then ends at the final factory (which may be at a different location from the initial base), and so on. It is usually efficient to attempt to orchestrate the final run of the shift for each tanker to end at its own base to minimize empty run. As some suppliers have a relatively low output at certain times of the season, it is not considered worthwhile to visit them daily. Thus, a part of the allocation problem is the identification of the suppliers to be visited in the current shift. There is also the matter of accurate prediction of the supplier output. Further, a judgment has to be drawn regarding the frequency (increase or decrease) of the visit to a particular supplier in the event of a change in the output.

Schedulers often approach these issues by first establishing the suppliers that are to be visited during a given shift and then allocating them different factories to satisfy factory demand. If there has been no significant change from a previous shift, the runs of that shift are usually modified to generate the runs for the present shift. While examining previous runs, schedulers often ask themselves two questions:

1. What are the requirements of a new schedule that differ from the previous one?

2. How should the previous schedule be modified to create a satisfactory new one?

The first question usually involves constraints governing the feasibility of any new schedule. The second involves, not only these constraints, but also the measurement of the satisfaction of the new schedule in terms of various objectives. The New Zealand Dairy Company's vehicle schedulers have traditionally used a large-scale map with colored pins showing the suppliers. A manual file system was used for information concerning the suppliers and tankers, and for creating the schedule. One supervisor, thoroughly knowledgeable about the vehicle scheduling system, performed virtually all the scheduling, but had difficulties in handling all requests and accommodating all demands.

## 2.2. The mathematical programming approach

Traditionally, such vehicle routing problems have been modeled as mixed integer programs to be solved by advanced mathematical programming techniques. The classical vehicle routing problem (VRP) is concerned with an efficient routing of a fleet of vehicles that must visit – from a central depot – a collection of clients to collect or deliver some commodities or render some services. An excellent survey of the VRP has been given by Bodin [2], who discussed important concepts and approaches for solving practical problems, and other issues. Milk tanker routing is an excellent example of this type of problem. There are, however, some significant difficulties in this approach.

Dairy company's vehicle schedulers often face problems that cannot be represented by a single well-defined optimality criterion and with families of well-defined constraints expressed in mathematical forms. Their decisions are based, not only on objective data points and formulas that can be optimized, but also on subjective judgment. The total cost of servicing all the customers is only one of the many considerations in the comparison of possible options. Often, it is only a secondary consideration of the busy planner, who is under pressure to produce a satisfactory schedule. Combinations of other factors that often need to be considered are as follows:

• the level of customer satisfaction,

\- equity of route generation including driving and visiting times,

\- rostering arrangements for drivers,

• efficient vehicle and driver utilization,

• the total schedule time,

• company financial strategies,

\- access problems including certain vehicle-customer combinations,

\- road inclinations in winter conditions,

\- queuing of tankers returning to factories, - accidents and breakdowns, and geographical obstacles which complicate distance and time estimation,

\- vehicle cleaning and servicing, and union rules,

• labor and traffic codes,

\- company and customer policies, and

\- human error.

Thus the dairy company scheduler is typically faced with a multitude of ill-defined objectives and constraints, the relative priorities of which may change markedly in a short span of time. There are goal programming and other approaches available for this scenario, but they are computationally complex and are usually not suitable for the practical problems arising from a relatively large size.

Some commercial packages, based on mathematical programming, such as some of those discussed by Golden et al. [7], are available for addressing vehicle scheduling problems; however, they usually suffer from major deficiencies when applied to practical milk tanker routes. The major difficulty with these packages is their inflexibility. Most of them ignore the talents of the experienced schedulers, and do not lend themselves very well to manual 'tweaking' of the routes suggested by the package. In other words, the problem cannot be solved merely by implementing a model: vehicle schedulers still requires a system that supports their decision-making processes.

## 2.3. The need for a DSS

The vehicle schedulers realized the potential of judgmental models that use computer support for capturing and evaluating basic data, and they thought that such systems might offer a more transparent and effective method for vehicle routing than the unrealistic schedules obtained using mathematical models. A system which follows their daily human decision-making processes and takes into account some of the non-quantitative considerations would be useful. Recognizing the importance of both models and judgmental considerations, the dairy companies, together with the authors, studied the companies' operations and vehicle routing methods and decided to develop a DSS.

## 3. The decision support system

FleetManager uses multiple, resizable, overlapping windows to assist schedulers in their tasks. Users can also interact with the system through a graphical interface that displays a road map of the area and the location of the milk processing plants and suppliers. FleetManager also contains the option of automatically creating vehicle routes that can be modified by the users. The system can also be used to analyze a wide variety of 'What-if' scenarios with potential cost impacts.

## 3.1. System characteristics

The traditional large-scale map with colored pins displaying the farms is a very useful visual aid for schedulers. In order to gain acceptance, it is necessary for a DSS to contain a computerized map to replace the large-scale map. Geographical features and all relevant locations can be represented on the screen as a result of digitizing their coordinates. Relevant factory, milk tanker, and supplier information can be represented on a color display. This combines the strength of the schedulers and the computer. The schedulers have the skill to recognize patterns in the location of suppliers and routes and suggest possible options when routes have to be modified. Before these patterns can be translated into new routes, the scheduler needs information on individual supplier output totaled for any cluster of suppliers. The micro-computer is ideally suited to this task. Such a scheduler-computer combination combines the pattern recognition skills and specialized knowledge of the experienced scheduler and the numerical processing and recalling ability of the PC.

## 3.2. System functionality

The development process began with a series of discussions with the potential system users and other concerned individuals. The result of these meetings was the main menu functions needed by the users to identify the requirements and create a satisfactory new schedule.

1. File open/close: The user must first be able to access the previous schedule. Schedulers should be able to open and manipulate all the data files: suppliers, tankers, road network, etc.

2. Checking: The user must ascertain the efficacy of a schedule to meet the requirements. A schedule may be checked for: the tanker capacity, amount of milk collected from individual suppliers, amount of milk remaining in the vats of the suppliers, and distance traveled.

3. Modification: Having pinpointed deficiencies, the user must devise modifications to produce a satisfactory new schedule. The system must allow for modification of existing schedules by:

\- adding a new supplier to a run;

\- deleting a supplier from a run;

• transferring a supplier from one run to another;

\- interchanging suppliers between different runs; and

\- creating a new run.

The DSS should also be able to respond to inquiries, and address questions about changes in the size of the tanker fleet base, the acquisition of new suppliers, or the location of a new factory. Changes in these attributes and constraints require the construction of a completely new schedule from scratch, rather than modification of an existing schedule.

The system consists of a PC-based DSS able to communicate with the company's mainframe computer, mainly to import the information necessary to support it. We also incorporated some strategic planning tools which allow testing of the effects of changes in the milk yield, factory demands, shifts, and tanker capacities. The system includes a digitized map of the area of operations which shows all relevant locations and roads. The system is user-friendly and mouse-driven with pull-down menus, windows and graphical displays.

The assignments of suppliers to milk tanker runs can be automatically generated and then manually fine-tuned to meet specific needs. The system recommends the scheduler by displaying the information on the digitized map and the scheduler modifies the runs by clicking the mouse at the represented locations of the suppliers. Once a schedule is finalized, the assignments (run-sheets) for the tanker drivers can be printed. Additional summary information is provided, such as warnings of possible routing oversights, such as unscheduled suppliers and overfull tankers. Various statistics are automatically generated, such as the percentage of vehicle capacity utilized and distance traveled.

![](/api/attachments/YA6NSKWY/fulltext/images/2bbc60a35fb9e6f7e74f5a84e18157cc5c0515d89e21ed848bb5109c3c17db2f.jpg)  
The Architecture of FleetManager  
Fig. 1.

## 3.3. The DSS architecture

FleetManager is a Specific DSS (SDSS) as described by Sprague and Carlson [18], because it contains the attributes and parameters that make it useful in a specific decision situation. The tool used to develop it was Turbo Pascal version 6.0 for an IBM-compatible PC with a high resolution color monitor. The architecture of the system conforms to the data-dialog model paradigm. Figure 1 illustrates the alignment of the elements of the system with the three components of the paradigm: the user interface, model base and database.

## 3.3.1. The database component

The system maintains a database of suppliers, tankers, roads, factories, and base information that can be interactively entered and updated. This database can be easily accessed and manipulated through the FILE module. Schedules can also be saved and recalled for use in future routing. The file recording the actual output collected from each supplier during the last shift is also saved. FleetManager accesses the external company-wide mainframe database to estimate the milk output.

## 3.3.2. The model component

There is no model available to solve the problem, but models are used by FleetManager to suggest schedules to the user. The Sweep algorithm of Gillet and Miller [5] is available to plan the runs. The Farthest Insertion algorithm [19] is available to determine the sequence of suppliers that minimize the distance traveled in a run. A linear interpolation scheme is used to forecast the milk output. Estimates can be altered by the schedulers based on their subjective judgment and experience, such as the knowledge of the amount of rainfall and the length of time since the beginning of the milk producing season.

## 3.3.3. The dialog component

The dialog component of the architecture has two subsystems: (1) a windows based interface; and (2) a graphical interface. The first gives the user access to five functional modules corresponding to the activities that must be performed by the scheduler. In addition, it has the standard menu, ABOUT, which displays general information about the FleetManager program including version number, copyright information, calculator, and calendar. Figure 2 shows the pull-down menus and the secondary menus of these modules. All procedures are independent and can be used in any order.

The FILE module provides file manipulations, exit, and DOS-shell functions. FleetManager automatically loads the supplier, tanker, factory, roads and base files. These files are used in the routing process and can be viewed and edited using the File Open menu command.

The AUTO module allows FleetManager to generate all schedules automatically and examine the effects of changes in the milk yield. It can automatically generate a schedule using information from the user or a database, provide a schedule without the intervention of the user, and display or print the schedule or an individual run in a way that can easily be understood. The suggested schedules can then be modified by the user. When used as a planning tool, the system allows the user to ask 'what-if' queries to examine the effect of changes in the milk yield, factory demands, shifts, and tanker capacities. The steps in the automatic generation of the routes are the assignments of suppliers to factories, assignments of tankers to factories, creation of an initial run for each tanker, and assignment of a subsequent run to each tanker from a factory.

![](/api/attachments/YA6NSKWY/fulltext/images/e0f20d9fb9d2e54c9f7bc62ed1ef5e74f361e8dc5c996606bff1c54fc17058b3.jpg)  
Fig. 2.

As a part of the process for generating the initial schedules, FleetManager also allows the users to edit the supplier outputs manually, i.e. to change the estimates of supplier outputs by a specific percentage. These changes can apply to:

\- all suppliers in the supplier database;

\- a single supplier;

\- only current shift suppliers;

\- all suppliers other than the current shift suppliers;

• currently scheduled suppliers;

\- currently unscheduled shift suppliers; or

\- suppliers in a particular area.

After making these changes, the system can generate a schedule for all the suppliers. The user can decide whether to generate an automatic schedule for all runs or for only one. The system allows the suppliers to be ordered in a way that minimizes the distance traveled by the tanker.

The SCHEDULE module provides most of the schedule manipulation functions. There are provisions for looking at a summary of the schedule for editing a run (including swapping of suppliers between runs) and checking the performance of the schedule. In addition, the SCHEDULE module allows the user to:

\- summarize all the runs of a schedule for a given shift;

\- print the run sheets and supply tickets;

\- display allocation of the total output of each shift among various destinations;

\- remove schedules and accordingly adjust the supplier outputs;

\- view a summary of the tanker runs currently scheduled and total milk to be collected by each tanker (runs in which the total milk collection exceeds a user-specified percentage of the tanker capacity are displayed in red);

\- modify and fine-tune the existing schedules including the transfer of supplies between runs and shifts; and

\- remove a supplier from a run and not schedule for it in any other run

Using the SWAP RUNS function, the system also allows the user to swap the complete set of suppliers on one run with the suppliers currently assigned to another run.

The VIEW menu allows the user to query the supplier database. The system displays sets of suppliers which satisfy certain user-selectable criteria, such as:

• display all suppliers;

\- display only those suppliers whose current uncollected total output exceeds a user-specified percentage of their milk holding tank (vat);

\- display only those suppliers which are estimated to have less than a certain user-specified percentage of their vat size or with less than a specified liter vat estimates; and

\- display only those suppliers which have been split into two or more runs or whose vat estimate has been only partially assigned to a run.

The OPTION module permits users to customize the display. Certain user-definable information can be viewed and altered using this module. The values that can be set include the maximum or minimum percentage of tanker capacity or vat size that will generate an alarm. Another option allows the users to change the colors of the foreground and background and the color of the letters appearing at the desktop, dialogue boxes and other interactive desktop items, using this module.

A second user interface is the graphical interface. It displays a road map of the area and the location of the suppliers based on digitized coordinates supplied by the Department of Survey and Land Information of the New Zealand government. The interface has the provisions for zooming and panning.

Figure 3 shows a screen illustrating the graphical interface. The information about the current tanker run is displayed at the top left and the current supplier information is shown underneath. FleetManager displays the suppliers' location using the following color scheme:

![](/api/attachments/YA6NSKWY/fulltext/images/da3eb3af68aa2b2bc1fe5678526a2ba4a91cb8ff6a596c46b805c0618383d814.jpg)  
Fig. 3.

Red Unscheduled or partially scheduled suppliers
Green Scheduled (including fully scheduled split)
suppliers

Pink Suppliers scheduled on the current run
Black Other suppliers

This display simplifies the system and emphasizes the ease of use, flexibility, and adaptability of the system.

## 3.4. Implementation

FleetManager was implemented on IBM-compatible PCs having super VGA monitors. It was developed using a prototyping approach. The system was used on a daily basis along with the manual system for a couple of months. During this time, we implemented several revisions to make the system more robust and user-friendly. This iterative development approach enabled the team to work on both the model building and interface between other components of the system simultaneously. Involving the users from the beginning allowed periodic testing of the enhancements and progress, and checks on the performance of the whole system.

Most changes have dealt with the process of transferring information from other systems to FleetManager and in the implementation of the graphical interface. Minor changes have also been made in other areas. The layout of the files that make up the FleetManager system has also been improved. Currently, the system is used as a stand-alone DSS, helping the schedulers plan and schedule their workforce and vehicles in a more effective way.

## 4. System benefits and impacts

The impact and benefits of FleetManager was measured by auditing the operating performance and comparing it with the performance of the manual system. In general, the Transport Office considers the system a major success. It has saved schedulers' time, created valuable flexibility, improved scheduler morale and enthusiasm, led to more creativity, and improved the quality of decision making. The system has been able to create schedules, choose plans, generate alternative plans, and to assess alternative plans with respect to the given criteria. The system also creates routes automatically, minimizing the total distance traveled, and allows schedulers to override created routes manually. It allows for more than one source or destination, skip-a-day clients, multiple shifts, as well as fine tuning. These options are very important to the Transport Office.

More specifically, the manual system used to take 6 hours. With the new system, the scheduling now takes 60–90 minutes. Since the system is used seven days a week, this represents a reduction of up to 35 hours per week – a huge saving. There are other immediate benefits: suppliers can easily be rostered on a 3-shift rotation instead of the customary every day or skip-a-day regimes.

Further, the schedulers and transport manager now have more time and energy for more creative and productive tasks than was possible with all the menial work that the old system entailed: e.g. the manager has much more time to work with his colleagues and manage his office. In his own words, he has “more time for my people”. The manager became a ‘manager’ instead of forms preparer. He finds that he can use his unique knowledge and inspiration better, and be more creative in finding answers. In short, his job is more challenging and interesting.

All of the scheduling staff find that, as the scheduling now takes less time, they have more time for other important tasks and are not demoralized by long hours of routine work. They believe that the schedules are improved and are generating savings for the company. They can also plan ahead in a more organized way. In addition, the schedulers find FleetManager enjoyable and user-friendly. They believe, as a result of it, they are a more efficient and effective team. They can cope with more complex situations and unexpected events with more confidence.

The manager now has a feeling of ownership for the system. He considers it his system, defends its operation, praises it to other companies, and wants it to succeed. His attitude is largely based on the way FleetManager has allowed his office to cope with the strains of their increased workload. The company had 69 staff in 1982 and now has 105. Milk volume has increased by 25 percent in the last two years, while the number of drivers has been reduced. This reinforces the importance of FleetManager so that the Transport Office can cope effectively with the resulting strains.

In summary, FleetManager is now successful at the Westland Dairy Company. It has been accepted by the Transport Office, and its staff are, at last, pleased with it. The system has led to direct benefits in terms of time and money and more intangible benefits concerning flexibility, more productive time, morale, and enthusiasm. The top management is to be commended for its innovative attitude toward the adoption of new ideas, and the Transport Office for its determination to make the system work.

We are developing enhancements that promise to increase the power of FleetManager and further improve the ability of the Transport Office to manage their vehicles and workforce. Improvements include a link to other systems at the Westland Dairy Company, and improved estimation and scheduling models.

FleetManager is a stand-alone system and there is little interfacing with other systems – only the transfer of one ASCII file. The system can be connected to the payroll system where the milk volume can be reported and the drivers' schedule and work hours can be reported.

The automatic scheduling option could be improved by adding available road information. However, this is not seen as an essential improvement by the schedulers. In addition, the automatic routine requires major (and expensive) alterations to produce viable schedules automatically, so that in the near future, these routines should only be used to compare different alternatives, or for strategic planning.

Additionally, there is a need to enhance the estimation model. Currently, the linear trend estimation model, which is based on a few previous milk collections, causes too much fluctuation in the milk estimates. A better model using historic and seasonal data is required.

## 5. Conclusion

In summary, FleetManager is a successful DSS that has generated a spectrum of benefits for the Westland Dairy Company. Much of the benefit is derived from the characteristics and attributes of a ‘classic’ DSS given below:

\- It supports but does not replace the decision maker. It does not try to provide the ‘answers’ nor impose a predefined sequence of analysis.

\- It supports semi-structured decisions where parts of the analysis can be systematized for the computer, but where the decision maker's insight and judgment are ‘leveraged.’

\- It combines modeling techniques with database and presentation techniques.

\- It emphasizes ease of use, user-friendliness, user control, and flexibility and adaptability.

\- It supports all phases of decision making.

\- It interacts with other computer-based systems, mainly with the company mainframe system to download and upload information.

The success of the system can be attributed to an extensive user participation and involvement; evolutionary approach to system development; flexibility and simplicity of system architecture; a committed and informed sponsor (mainly the Transport Office manager); accessibility and transferability of models and data; availability of graphics; and clarity of insights by using both judgmental and analytical models. The development and implementation of the system was enhanced by good relationships and close collaboration between the potential users and developers.

Westland's use of FleetManager has improved its vehicle-scheduling process by reducing the deployment of drivers and vehicles, using existing staff and vehicles more efficiently, and thereby reducing costs. In addition, it has freed up time for the schedulers and managers to improve productivity and manage people instead of running shifts and schedules manually. It provides powerful tools to create schedules, choose plans, generate alternative plans, and to assess alternative plans with respect to the given criteria. The system allows the scheduler to allot vehicle routes automatically, minimize the total distance traveled, and override routes created manually. It allows for more than one source or destination, skip-a-day clients, and multiple shifts, as well as allowing fine-tuning.

The system has generated tangible and intangible benefits. In addition to the reduction in labor costs, it can benefit the schedulers by fine tuning of the existing schedules, creation of entirely new schedules, strategic planning for new sites, efficient fleet utilization, and rendering flexibility to plan for and cope with unexpected situations. The DSS also allows the scheduler to carry out an ad hoc analysis through 'what-if?' queries. It provides the scheduler with a better understanding of the business since the system alerts the users to illogical outcomes, such as unvisited suppliers and overloaded tankers.

Taken together, these benefits and attributes make FleetManager a rare example of a successful DSS that can provide guidance for the development of other systems in the important problem domain of vehicle routing.

## References

[1] Arinze, B., Igbaria, M. and Young, L.F., “A knowledge based decision support system for computer performance management”, Decision Support Systems, 8(6), 1992, 501–515.

[2] Bodin, L.D., “Twenty years of routing and scheduling”, Operations Research, 38(4), 1990, 571–579.

[3] Couillard, J., “A decision support system for vehicle fleet planning”, Decision Support Systems, 9(2), 1993, 149–159.

[4] Er, M.C., “Decision support systems: A summary, problems, and future trends”, Decision Support Systems, 4(3), 1988, 355–363.

[5] Gillet, B. and Miller, L., “A heuristic algorithm for the vehicle dispatch problem”, Operations Research, 22(2), 1974, 340–349.

[6] Gopalakrishnan, M., Gopalakrishnan, S. and Miller, D.M., "A decision support system for scheduling personnel in a newspaper publishing environment", Interfaces, 23(4), 1993, 104–115.

[7] Golden, B., Bodin, L. and Goodwin, T., "A microcomputer-based vehicle routing and scheduling software", Computers and Operations Research, 13(2–3), 1986, 277–285.

[8] Goldstein, D.K., “Information support for sales and marketing”, Information and Management, 19, 1990, 257–268.

[9] Gray, P. (Ed.), Decision Support and Executive Information Systems, Prentice-Hall, Englewood Cliffs, NJ, 1994.

[10] Islei, G., Lockett, G., Cox, B., Gisbourne, S. and Stratford, M., “Modeling strategic decision making and performance measurement at ICI Pharmaceuticals”, Interfaces, 21(6), 1991, 4–22.

[11] Keen, P.G.W., “Value analysis: Justifying decision support systems”, MIS Quarterly, 5(1), 1981, 1–16.

[12] Keen, P.G.W., “Decision support systems: The next decade”, Decision Support Systems, 3(3), 1988, 253–265.

[13] Kettelhut, M.C., “Using a DSS to incorporate expert opinion in strategic product development funding decisions”, Information and Management, 20, 1991, 363–371.

[14] LeBlanc, L.A., “An assessment of DSS performance”, Information and Management, 20, 1991, 137–141.

[15] Min, H., “A model-based decision support system for locating banks”, Information and Management, 17, 1989, 207–215.

[16] Omar, M.H., “A DSS approach for implementing an on-line retail banking system”, Information and Management, 21, 1991, 89–98.

[17] Pearson, J.M. and Shim, J.P., “An empirical investigation into decision support systems capabilities: A proposed taxonomy”, Information and Management, 27, 1994, 45–57.

[18] Sprague, R.H. and Carlson, E.D., Building Effective Decision Support Systems, Prentice-Hall, Englewood Cliffs, NJ, 1982.

[19] Syslo, M.M., Deo, N. and Kowalik, J.S., Discrete Optimization Algorithms, Prentice-Hall, Englewood Cliffs, NJ, 1983.

[20] Turban, E., Decision Support and Expert Systems: Management Support Systems, 3rd edn., Macmillan, New York, NY, 1993.

[21] Vetschera, R. and Walterscheid, H., “A process-oriented framework for the evaluation of managerial support systems”, Information and Management, 28, 1995, 197–213.

[22] Young, L.F., “Decision support systems for workers: A bridge to advancing productivity”, Information and Management, 16, 1989, 131–140.

Magid Igbaria is a Professor of Information Science at the Claremont Graduate School and the School of Management, Tel Aviv University. Formerly, he was a Professor of MIS at the Drexel University and a Visiting Professor of Decision Sciences at the University of Hawaii in Manoa and lectured at the University of Waikato in New Zealand. He has published articles on DSS, computer technology acceptance, IS personnel, management of IS, economics of computers, and international IS in Applied Statistics, Communications of the ACM, Computers & Operations Research.

Decision Sciences, Decision Support Systems, Information & Management, Information Systems Research, Journal of Management Information Systems, Omega, MIS Quarterly, and others. His current research interests focus upon information and computer economics, virtual workplace, computer technology acceptance, IS personnel, and international IS. He is an associate editor of ACM Transactions on Information Systems and MIS Quarterly and serves Journal of Engineering and Technology Management, Journal of End-User Computing, and Information Technology & People, in the editorial board.

Ralph H. Sprague, Jr. is a Professor of Decision Science in the College of Business Administration at the University of Hawaii. He has over 30 years of experience in teaching, research, and consulting in the use of computers and information technologies in organizations. His specialties are Decision Support Systems, Strategic Systems Planning, the Management of Information Systems, and Electronic Document Management. His book on DSS has been translated into Japanese and Portuguese. His book on Information Systems Management is a leading text on that subject, and has been translated into Chinese.

Chuda Basnet is a Senior Lecturer at the University of Waikato in New Zealand. He received a M.S. in Industrial and Management Engineering from Montana State University and a Ph.D. in Industrial Engineering and Management from the Oklahoma State University. His current research interests include vehicle routing, manufacturing systems modeling, and production planning and control.

Les Foulds is the Foundation Chairperson of the Department of Management Systems, at the University of Waikato, New Zealand. He received a Ph.D. in industrial engineering (traffic network design) from the VPI. He taught in the Economics Department at Canterbury and the University of Florida as a professor of Systems Engineering for 1984–85. His research interests were in the theoretical end of OR; combinatorial optimization and graph theory/networks. His current research interests focus upon applied work: evolutionary trees, facilities planning, vehicle scheduling, quality management and world class manufacturing. He has published over 100 papers and 8 books in the above areas.
