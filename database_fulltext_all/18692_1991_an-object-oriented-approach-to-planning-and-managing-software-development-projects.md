---
otero_id: 18692
otero_key: "ZZP6KWCB"
title: "An object-oriented approach to planning and managing software development projects"
authors: "Timothy J. Heintz"
year: "1991"
journal: "Information & Management"
doi: "10.1016/0378-7206(91)90020-3"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
SOS

# An object-oriented approach to planning and managing software development projects

Timothy J. Heintz

Department of Management, Marquette University, Milwaukee, WI 53233, USA

An object-oriented systems development approach is applied to the planning and control of software development projects with the objective examining places where the computer can provide “intelligent” facilitation of the process. An application design is presented that is based on the procedures used by a moderately sized custom software house. Smalltalk language object classes are defined for project entities such as client, objectives, functions, tasks, and resources. Other objects are used to generate functional and implementation plans and to provide routine reporting, maintenance, and control of active projects. Historical project data can be used to update a planning knowledge base. A constraint directed planning algorithm is used to assign resources and schedule tasks, and points within the system where project management “expertise” can be embedded within the system are identified. It is concluded that the concepts presented within this paper could be extended into related systems design and group decision making activities.

Keywords: Project management, Object-oriented programming, Planning knowledge representation, Artificial intelligence, Software design and development.

![](/api/attachments/ZZP6KWCB/fulltext/images/8bbd00a60e7f38b338bf5ebc928c5102cd65c504687fa6c1b9a07fc99c2a1467.jpg)

Timothy J. Heintz is an Associate Professor of Management at Marquette University. He received his DBA from Indiana University in Quantitative Business Analysis with a minor area in MIS. Since Joining the Marquette Faculty 1972, he helped develop their Information Systems program and served as Department Chairman for five years. He has been active as a researcher in applications of computing and simulation. In 1986, during a Sabbatical leave at Johnson Controls,

Inc., he became Involved in the use of Artificial Intelligence techniques. He has recently focused on object-oriented systems design issues and on the design and use of systems to support group decision making. He has authored papers appearing in the Transportation Research Record, The Journal for Experiential Learning and Simulation, The Canadian Journal of Operations Research, The Journal for Systems Management and others.

## 1. Introduction

Over the past 25 years, there have been few new approaches to the computerized management of complex projects. Since PERT [17] and CPM [13] methods were developed, much research effort has concentrated on refining the mathematical or heuristic approaches to network scheduling, usually under resource constrained conditions (for recent articles in this area see [9,20,28]). Work has also been expended in the project measurement area [22]. The major research efforts have primarily examined the issue of sequencing and reporting on project tasks. There has been little emphasis on having the computer actively assist in identifying the tasks needed to complete the project or in implementing or controlling the project plan once it has been formulated.

Liberatore and Titus [14] surveyed a number of companies involved in managing research and development projects. They concluded that, at least within this environment, less formalized techniques were used and that the survey respondents were not satisfied with the available techniques for project monitoring, scheduling, and control. An interest in simple, interactive systems for resource allocation, tracking, and control was cited.

Recently, activity from the field of Artificial Intelligence has produced a different perspective on attacking project planning and control problems. Sathi, Morton, and Roth [23] have reported on the Callisto project, which was sponsored by Digital Equipment Corporation for the purpose of controlling large engineering projects. This project focused on representing project knowledge in schemata or frames. Knowledge structures were defined for project activities and resources and for the products that were being designed by the project teams. There was also an attempt made to store rules that captured expertise on the project management process, but they were unable to develop expertise that was generalizable from one project to another.

The Callisto project also examined placing project knowledge at dispersed locations. Thus a series of “Mini-Callistos” were developed. Each one of which was embedded within a negotiation support system designed for initiating and managing change among project participants. As part developing this negotiation system, operations were defined for initiating change requests and resolving conflicts.

In a different vein, Philips, Staley, and Gold [21] examined a Smalltalk language-based approach to project management in which objects were created to access project calendars and a project data knowledge base they called the Project Encyclopedia. This research focused on developing a rich, graphically oriented user interface that enabled users to browse through project knowledge. Like the Callisto project, there was some discussion on developing an electronic system to handle electronic information exchange and facilitate a negotiation process among project participants, although these aspects of the system do not appear to be as well developed.

Both of these projects rely on the storage of information in knowledge units, called “schemata” in the first paper and “objects” in the second. These units form the basis for representing and processing project information. Neither, however, have appeared to handle the issue of representing project “expertise.” The Callisto project actually admits to a lack of success in this regard. Knowledge acquisition and representation has always been a difficult problem associated with building “intelligent” systems. Traditional solutions have focused on limiting the scope of the problem domain, thus breaking a tough knowledge problem into manageable pieces.

This paper thus addresses the issue of representing project expertise. In accomplishing this task, the discussion is limited to management of software development projects. A knowledge architecture is presented that uses information from prior projects as a basis for planning new problems. Specific means of using expertise to modify this “historical” knowledge is suggested. The type of tool is similar to that used by the two just discussed projects, but a different approach to knowledge representation and processing is used.

This paper introduces a relatively simple case of a software house that must bid upon and implement computer programming projects. The case provides the basis for developing an object-oriented knowledge structure for this specific type of project management task. Emphasis is placed on using an object-oriented design methodology and on how specific planning and control functions can be accomplished using this approach.

## 2. Object-oriented development

The term, object-oriented development, has been used by Booch [2] to describe a systems development approach based on concepts derived from the object-oriented programming (OOP) languages. Creating systems from an object-oriented perspective involve the definition of objects which are entities “whose behavior is characterized by the actions that it suffers and that it requires of other objects.” Objects are described by a series of attributes which represent the object’s “state,” and procedural code called methods that describe the object’s “behavior.” Attributes of an object can reference other objects, and the methods typically invoke action by calling methods associated with these referenced objects. This process of objects invoking other objects is called message passing. We thus have a software system in which objects undergo state changes through a process of passing messages between one another.

OOP has evolved from conceptual work by programming language theorists on abstract data types $[12,15,24]$ . From their perspective, OOP involves a process of defining data (object) types called classes and associating specific methods to these classes $[6]$ . Thus all objects are instances of a class; this includes, within a full OOP implementation, the class definitions themselves.

Methods written for objects are similar to function definitions within traditional functionally oriented programming languages such as PASCAL, APL, and LISP. Instead of “calling functions,” OOP applications send messages that are represented by the object followed by a selector or method name. Arguments optionally follow the object-selector sequence. For instance, assuming that we define an inventory object consisting of such attributes as product number, cost, amount-on-hand, and amount-on-order, we could also define a method called “receiveOrder: anAmount,” which takes an argument value (anAmount), adds it to the amount-on-hand, and subtracts it from the amount-on-order. If a variable called, selectedProduct, contains an instance of an inventory object (ie. of type inventory), then a message to update this item takes the form, “currentProduct receiveOrder: anAmount.” Typically, OOP methods are composed of a series of these messages.

OOP has drawn considerable interest within both the popular and academic literature $[7,19,29]$ . This programming approach, and the design methodologies implied by it, are characterized by three major features; data encapsulation, inheritance, and polymorphism $[4,5]$ . Data encapsulation entails combining both code (methods) and data (attributes) within self contained objects. Within OOP environments, data within objects can only be accessed and changed through methods or messages.

Inheritance is the capability of an object to obtain attribute definitions and methods from higher-level objects. Within OOP systems, subclasses of classes can be defined. The subclasses would represent specializations of their superclasses, inheriting superclass methods, but also extending the superclass through the definition of locally owned attributes and methods. For instance, within an inventory system, there may be classes of products, such as finished goods and parts that contain information unique to its class. These would be defined as subclasses of inventory.

Polymorphism is the ability of differing objects to respond to the same message in their unique way. For instance, consider the message “draw” used in the context of displaying a network graph on the screen. Objects for representing nodes, edges, and the entire network would be defined, with each containing its own draw methods. The “node draw” would generate a labeled oval, the “edge drawn” would produce an arrow between two nodes, and the “network draw” would compose the entire network through a process of sending draw messages to its node and edge objects.

In general, OOP is designed to facilitate software modeling that closely resembles the physical system $[3]$ and to enable code reusability. This concept of code reusability is implemented through the inheritance feature (generic code being used by subclasses) and through encapsulation (code is modularized to a point where it is easy to extract and modify).

Smalltalk [11] is the object-oriented language in which the case application presented in this paper has been partially prototyped. Smalltalk, like many OOP programming environments, is delivered with a large number of predefined objects designed to assist in system development and the creation of the user interface [8]. These include a very rich windowing system with mouse driven terminal input/output, an ability to browse interactively and maintain object definitions, powerful debuggers, and extensive graphics support. Other object classes support multiprocessing, disk and printer output, and a large variety of data types that allow easy manipulation of strings, arrays, and sets of objects. As a result, it is considerably easier to develop complex systems using such tools.

The multi-tasking operating environments that are now becoming available, such as IBM's Presentation Manager and UNIX's X-Windows, are implemented with an OOP context. A recently released IBM PC version of Smalltalk [25] does a very nice job of integrating its own message handling with that of presentation manager. The result of the implementation is a very powerful development tool for presentation manager applications. Clearly, OOP and systems developed around it will become the most persuasive software technology of the 1990's. This paper thus shows how one can take advantage of OOP within the specific task of software requirements analysis and the subsequent management of software projects.

## 3. The project management process for a software house

The concepts presented within this paper are derived from the actual project management procedures of a moderately sized contract software development firm. This company consists of a president, marketing manager, and four project managers who have primary customer contact and project supervision responsibility. Project activities are allocated among about 40 programmers or system analysts that are on the company payroll.

A phased development approach is used for most projects. This approach starts with an initial customer contact, which is immediately followed with a proposal for the development of a functional plan. The customer pays an initial fee for this functional plan; this typically is based upon either 20, 40, or 60 man hours of work, depending on the complexity of the application. This proposal provides a ballpark estimate for the total system development cost.

The functional plan describes the current client situation, and lists a series of proposed hardware and software solutions to the problem. The plan clearly outlines the system's objectives and activities needed to accomplish them. It also provides a cost estimate for the system design phase.

Upon completion of the design phase, a detailed implementation plan is developed. Although the functional plan specifies the tasks needed to obtain the customer's objectives, the results refine the resource requirements implied by each task. The availability, timing, and acquisition of people and hardware resources are assessed at this point and become the basis for generating an estimate of the cost for system implementation. Project cash flows are also analyzed to develop a reasonable payment plan.

During the systems design, project activities are defined for both specific hardware and software implementation functions and specific programming tasks. These tasks include meetings, forms creation, project management, technical support, programmer support, programming, testing, training, and installation. Different individuals may assume responsibility for different tasks.

Upon approval of the systems design, the actual scheduling of resources to the project is undertaken. This initiates the implementation phase, during which routine project progress reports are generated that compare the actual time spent with the estimate for each function and task. The current status of the project is also compared with planned milestones.

Besides using a phased development approach, the company may work on either a time and material basis or, in responding to an RFP, provide a fixed bid for both design and implementation. In both cases, an estimating process similar to that just outlined would be undertaken. Since detailed design data is usually not available in the RFP situation, bids for implementation tend to be higher, allowing for unforeseen contingencies.

Since the software house focuses much of its sales efforts along certain vertical markets, the client projects tend to be similar in their objectives and potential solutions. However, being a custom software house, the project managers try to conform specific proposals to specific needs and avoid completely turn-key solutions. Consequently, many proposals are developed from old ones, but there is no consistent way in which this has been done. It was generally felt that the software house could benefit by having a more systematic way of both generating the proposal and then following up on the execution of proposals that were implemented.

## 4. Object-oriented support for project management

The main premise of this paper is that the modular approach provided by the object-oriented design process would enable the development of an integrated perspective on the project management process. With this approach, development of the entire process, starting from the initial functional plan through the use of past project experience to review and refine a knowledge base that can be used for plan generation and estimating, can be achieved.

A prototype has been developed that implements the knowledge structures. This, through the use of tools available within the object-oriented software development environment, provides a rich interface as illustrated in Figure 1. The ability to create this interface, along with capabilities enabling the representation and manipulation of complex object-based knowledge structures, demonstrates the real power of using an object-oriented methodology.

The subsequent sections focus on the object-based knowledge structures needed to support this activity. Object classes are first described in terms of their key attributes and methods. A strategy in which instances of these objects are used in implementing an intelligent support system is then presented.

## 4.1 Functional plan generation

The implementation of an OOP system to generate functional plans starts with establishing contextual information related to the clients application. Instances of the “Client” object, as illustrated in Figure 2, contain attributes that reference objects describing the clients current hardware and software situation. As the planning process proceeds, functional and implementation plans will be generated for the client's project.

![](/api/attachments/ZZP6KWCB/fulltext/images/8aedef1f0ca06c1320b17bc6b40677b9affa59a7cae6c79036d2e184d8f11250.jpg)  
Fig. 1. Illustrative smalltalk generated interface.

The Hardware class in this Figure illustrates a need for subclass definition with subclasses providing specific descriptions for components such as disks, memory, terminals, and printers. Capacity data would be stored within these objects. The instances of the Software class provide lists of functions served by the software along with transaction volume data (not shown).

The object-oriented representation is ideal for documenting hardware and software systems. Separate objects for representing transactions, files, and reports could provide an even more detailed and complete description of the application. This representation, however, is better addressed within a discussion of object-oriented, computer-aided system design, which is beyond the scope of this paper.

An object, “StandardSystem,” would contain collections of specific Hardware objects. Its maintenance would help a project manager specify a client’s hardware configuration through copying and updating of typical system configurations.

The development of a functional plan for the client requires identification of a client's objectives and the functions implied by them. Through the specification of these requirements, the project management system determines the needs for acquisition of hardware or software or for the writing of specific programs. The implementation tasks, which are the basis for planning, then follow from the recognition of these hardware, software, or programming needs.

Figure 3 illustrates this mapping of objectives to functions and finally to implementation tasks. Since it is often convenient to arrange both objectives and functions hierarchically, these are defined as subclasses of an abstract object called “Tree” (In OOP abstract objects do not have instances of their own, but rather they just provide attributes and methods to be inherited by their subclasses). The Tree object has attributes indicating the parents and sons within the hierarchy and methods for accessing a parent or son.

![](/api/attachments/ZZP6KWCB/fulltext/images/293df97b102227e55becf5996f5e132c083b559a6710561380a47453ea8014c8.jpg)  
Fig. 2. Object oriented representation of client information.

Methods within a “FunctionalPlanGenerator” object use two basic intelligent system implementation strategies, commonly found in the AI, to generate the functional plan. The first strategy, constraint propagation $[10,26]$ , is implemented in two ways:

1. Specific project objectives provide links to functions which are either to be included or excluded from the plan.

2. Functions provide links to specific hardware and software implementation tasks or the programming activities associated with them.

The second strategy uses rule systems to take the contextual information associated with the client and a partially developed functional plan and use them to develop and refine the plan. These include:

1. The use of “filters” to exclude functions from the functional plan.

2. The use of "expanders" to add functions to the plan.

3. The use of "refiners" to modify specific tasks or adjust time or cost estimates.

The “FunctionalPlanGenerator” class contains methods allowing the project manager to either select or create project Objectives. The “includes” and “excludes” attributes contain lists that point to specific nodes within a tree of function instances. As illustrated in the shaded oval in Figure 3, the selection of an Objective will automatically place into consideration a function and its subfunctions that are specified in the includes list.

![](/api/attachments/ZZP6KWCB/fulltext/images/f045128deb5ab468f91893653b13e77a56665e6dfd2e7ddf1be69e20de559aae.jpg)  
methods or rule sets are in italics  
Fig. 3. Objects used to generate the functional plan.

Conversely, if a function is specified within an exclusion list, it (with its subfunctions) will be eliminated from consideration. Thus the selection of objectives for an client's application automatically generates a initial draft of a functional plan.

As an example, consider the following three objective statements.

1. Build a new order processing system that will maintain a “picture” of an order within a system and distribute appropriate order information to users when needed.

2. Allow for order entry by field representatives from portable terminals or personal computers.

3. Process only cash or credit card orders.

Objective statement 1 will automatically include a series of tasks associated with a standard order processing system. Objective 2 will add additional remote communications functions not typically included with the first objective, while the final objective will exclude functional specifications related to interfacing the Order Processing system with an Accounts Receivable application.

Methods within the FunctionalPlanGenerator that represent the “filters” and “expanders” are designed to use rules that consider other contextual information, such as the client’s current hardware or software situation, to remove (filter) or add (expand) functional specifications. For example, if a client has an existing order processing system but has established the objective of building a new one, additional functional specifications regarding the transfer of the old data to the new system must be added. In this case, a rule of the form “IF order processing system exists and objective is to build a new one THEN add function to transfer old data” would be one of a set of rules that an expander method could check and trigger.

methods or rule sets are in italics  
![](/api/attachments/ZZP6KWCB/fulltext/images/d1d68b1ddc407901ba781f7179e730e54a22e9b81a1d0cb3ce93e65eb78dd79a.jpg)  
Fig. 4. Objects used to generate the implementation plan.

Instances of Objectives and Functions are maintained within instances of a “Planning-Knowledge” class that lists all objectives and functions that would be used in meeting the needs of certain types of customer applications. This object is a frame of reference for planning individual projects. As each client’s functional plan is generated, copies of “PlanningKnowledge” objects would be created and modified and eventually stored within an instance of the “FunctionalPlan” object. The completed functional plan would then be stored within the object representing the client.

Task objects provide a perspective of the amount of time or expense necessary to implement the function completely. Default time estimates for tasks are provided within the task instances that are associated with the objectives specified within “PlanningKnowledge” objects. The “FunctionalPlanGenerator” also has the “refiners” methods; these provide rules that use contextual data to eliminate tasks or adjust their estimates within the individual functional plans. For instance, one type of “refiner” rule could ask for an assessment of the client’s level of technical sophistication. If the project manager specifies a low or high level for this item, the time estimate for certain tasks, such as training, could be adjusted up or down.

This enables the system to make an allowance for more “qualitative” considerations. The degree of adjustment and specification of factors to be considered for adjustment is best determined by an experienced project manager, and this would be part of the knowledge to be acquired as part of the implementation process for the project management system.

Finally, the “FunctionalPlanGenerator” provides a plan browser that enables the project manager to modify components of the functional plan generated by the objective selection and the action of the filters, expanders, and refiners. A method that reports on the functional plan in a format to be presented to the client is also included.

## 4.2 Implementation plan generation

The implementation plan uses and expands upon the functional plan by:

1. Refining the task lists and associated time/expense amounts associated with the functional plan.

2. Establishing task precedence constraints.

3. Scheduling people and equipment.

4. Scheduling hardware and software acquisition activities.

Figure 4 diagrams the objects used to generate the implementation plan: a collection of assignments which, over a specific period of time, links a task to a specific resource. Resources are either staff or facilities. Instances of the same Hardware and Software classes used in describing the client's current situation are used to describe what specific hardware or software is to be installed at a facility. Facilities may be owned by either the client or the software house.

A Calendar object indicates availability of both staff and facilities. Contained within a calendar is a collection of time slots and methods (such as assign task, release task, and display day's or month's schedule) that are needed to manage these slots. Time slots specify a day and specific hour or contiguous set of hours for which a task has been assigned to a person or facility. Time slots may also be used to indicate that a particular resource is not available for reasons such as staff person being on vacation, facility not yet operational, etc. Existence of no time slot for a specific period would imply availability.

An important distinction should be made between a time slot and an assignment. Assignments provide a time period at the end of which a task is to be completed. During this period resources can have multiple assignments. A person, for example, may work on one task for a while and then switch to another, only to come back to the first. Within time slots, however, no two tasks can be assigned to the same resource.

A Staff object contains a set of skill definitions. These definitions, which specify the type of work (e.g., COBOL programming or systems analysis), application type, and man-months of experience, provide the basis for assigning qualified personnel to projects.

Precedence constraints are represented by a constraintList attribute within the Task class. This contains a collection of “Task Constraint” objects, each indicating the tasks that must or should be performed before the given task. Instances of TaskConstraint contain a “hardSoft” attribute that indicates whether or not the constraint is desired or mandatory. A status attribute is used to indicate if the constraint is currently violated. Default precedence structures can be derived from applications described within instances of the PlanningKnowledge objects.

The “ImplementationPlanGenerator” object produces a proposed plan. A generate and test strategy is used that involves the following steps:

1. Collect and Sequence Tasks. The precedence constraints along with the estimated task times are used to produce a minimum time line for a project. Redundant tasks, if any, are eliminated.

2. Make Tentative Resource Assignments. The initial time line is adjusted for resource availability. A “canDo” method is invoked by sending a message to all resource objects, each of which will respond if the resource can do the job within the time frame specified by the functional plan.

3. Check for Feasible Plan. Depending upon the existence of a feasible solution, one or both of the next two steps may be performed. If no feasible solution is found, constraints on the project will have to be relaxed. If a feasible solution is found then additional alternatives could be generated by placing additional restrictions on the plan; then certain constraints could also be relaxed.

4. Relax Constraints. There are at least four strategies that can be used to relax constraints: completion dates, as specified within the functional plan, can be pushed back, resources could be acquired by hiring staff or purchasing equipment, skill restrictions can be relaxed by either allowing for assignment of over or under skilled staff to certain tasks, and “soft” precedence constraints can be dropped.

5. Restrict Problem. Three restriction strategies can also be applied; exclude assignment of resources to a task or project by assigning the project or task to the exclusion attribute within the Resource object, increasing skill requirements associated with a task, and add a slack time to a task.

6. Commit to a Plan. As a result of relaxation and restriction strategies a number of plans could be generated. The commit operation will select one from a set of plans stored within the proposedPlans attribute of the ImplementationPlanGenerator. An ImplementationPlan object would then be created and assigned to the client's project.

Within the “canDo” method for Staff, a decision to allow a person to be considered for assignment is based upon matching the skills required by the task to the skills possessed by the staff person. This matching process involves comparing the type of skill, application, and experience. Since exact matches would be unlikely, rules are used to infer whether or not an individual’s skills allows him or her to qualify for the task. Rules allow ranges in experience to be matched with a desired experience level and allow for substitutions of similar types of experience. For example, a rule could allow for trading off additional years of programming experience with lack of experience in a specific application area.

When, during the planning process, new resources are required or existing resources are committed to a project, the resource object referred to in the specific plan must be flagged. A commit attribute within the resource class is designed to provide this functionality; it must be updated as part of the commit operation. Conversely, resources that are not needed can be decommitted.

## 4.3 Management and control of project

In completing the planning process, the data necessary to control and manage the project is essentially available. Addition control capabilities include:

1. The ability to make minor updates to resource calendars so that time slots can be rearranged,

2. A time and project status reporting function,

3. A plan updating function,

4. A project rescheduler.

Methods associated with instances of individual Calendar objects provide a time management function by allowing the user to browse the time slots, rearrange them within limits set by current project assignments, and add to them non-project related tasks, such as company meetings and vacation time. Individual updates regarding project status would also be done through Calendar objects.

A ProjectController object contains methods for accessing individual calendars to view the time commitments and progress made toward project completion. It can generate routine project progress reports. A rule system can also be used to report, on an exception basis, potential problems with projects. For instance, a message might be generated if delivery of a client's hardware is delayed by more than one week or if more than 20% of the programs scheduled for completion have not been indicated as such. In these cases, the triggering of the messages could be moderated by how close the overall project is to completion. These knowledge “elements,” the specific rules to be applied, would be acquired at the time of implementation and perhaps refined over time.

A ProjectRescheduler is implemented as subclass of the Implementation-PlanGenerator. A rescheduling procedure removes current plan commitments and selects the current Implementation plan, updated for completed activities, as a proposed plan. It then updates the function list to exclude completed functions and to adjust for partially completed tasks. At this point in time scheduling methods inherited from the ImplementationPlanGenerator can be used to generate and evaluate alternative schedules.

The ProjectController also has methods for updating the implementation plan in light of the tasks accomplished to date. This activity involves removing old assignments that are stored as part of a Project's “implementationPlan” attribute. The removed assignments would be transferred to the Project's “projectHistory” attribute in order to maintain a log of activities performed on it. When all the assignments stored within the implementationPlan have been exhausted, the project is deemed completed.

## 4.4 Project review

Once a project is completed the opportunity exists to use the experience obtained to update the application knowledge stored within the PlanningKnowledge object. An instance of a “ProjectReviewer” would contain methods that allow the user to compare an existing project’s set of objectives and the functions and tasks associated with it with comparable data in a PlanningKnowledge object. Decisions can then be made concerning adding, deleting, or modifying Planning-Knowledge objectives using a “cut and paste” operation. Similarly, modifications can be made to the functions that are associated with these objectives along with the hardware, software, program, and related task objects. Actual versus estimated time and expense data associated with specific tasks is also compared and can be updated.

System maintenance functions are also provided. These support activities such as: adding new clients, removing client data, archiving completed project data, performing backups, recovering archived or backuped data, and providing a master menu for the selection of system options. Methods to perform these operations are contained within a SystemManager object that is activated upon entry into the project management system.

Some user interfaces are handled by separate browsers or interfacing objects. For instance, the first window in figure 1, illustrates the use of a TreeBrowser object that enables the user to move up and down an objective and/or function tree easily. When the desired node is selected, text can be edited or a data form can be used to change values associated with objective or function attributes.

Other objects created for this application include Predicate and Rule objects that enable representation of rule sets within objects. An instance of an InferenceEngine object is called by other objects that have rules for the purpose of maintaining the rule sets and performing generalized inferencing operations.

## 5. Conclusions

At present, a partial prototype implementation of the capabilities described in this paper has been coded on an IBM, PS2 model 80. As experience is gained with using the system, many minor refinements are anticipated. This system, as currently conceived, has a number of points where “intelligence” can be added to it in the form of either expert system rules or knowledge embedded within the object-oriented representation. These include:

1. The information structures represented within the Planningknowledge and StandardSystem objects. These structures, by identifying typical applications and their objectives (and indirectly, the functions and tasks associated with them) make available considerable expertise about previous projects. The system makes this knowledge available for planning future projects.

2. The filters, expanders, and refiners associated with formulating the functional plan are implemented as rule systems. These implement expertise on how contextual variables affect the inclusion or exclusion of a specific function and its associated tasks. Revision of time and expenses for individual tasks is also performed here.

3. The “canDo” methods used in determining whether or not a certain resource can be assigned to a project requires expertise in the form of rules that assess skill matches and time availability.

4. The constraint relaxers and restricters use expertise to determine which of the possible constraints are candidates for applying a restriction or relaxation strategy at any point of time. Related to this activity is the possible inclusion of knowledge that will determine when it is necessary to procure additional resources or increase or decrease the slack times associated with a task assignment.

5. The exception reporting in the Project-Controller is rule based.

The “knowledge acquisition” task associated with building these knowledge elements is viewed as an implementation related activity. The current system provides a “shell,” producing an architecture in which there are clearly identifiable places for adding and refining its “intelligence.”

The above list is not exhaustive. Other possible areas for incorporating expertise include:

1. Recommendations on which of a set of candidate plans should be selected for implementation.

2. Assumptions that went into the planning process (i.e. constraint relaxations or refinements on functional specifications); these could be maintained separately and be incorporated within the exception reporting or rescheduling activities.

3. Rules to help make decisions concerning when and how to update the planning knowledge; these could be embedded within the plan review process.

4. More detailed system design information, such as information on files and file structures, reports, input transactions. This information could be used for both providing a more detailed basis for planning and for supporting the systems design effort.

Indeed, this object-oriented approach to project management could provide the basis for developing a completely automated approach to systems analysis, design, and implementation.

Issues related to managing multiple projects or collaboration among multiple staff members on a single project are not addressed in this discussion. There recently has been considerable interest in systems to support collaborative work and group decision making $[1,16,27]$ . The Callisto project mentioned earlier places a major emphasis on coordinating teams of people working on multiple projects. Malone $[18]$ has proposed the idea of having “intelligent” software agents classify electronic mail messages for individuals within organizations. The object-oriented programming concepts developed in this paper involves having “objects” coordinate project activities by passing messages between them. This is a natural paradigm for systems that require coordination between a large number of individuals and activities.

A graphical browsing capability is also being considered as a future enhancement. This browser would allow the user to use a mouse to select objects for presentation or edit. Nodes on objective or function trees or tasks associated with specific hardware, software, or program object could be quickly accessed though a graphical display.

In summary, this paper applies a very powerful software development approach to the project management problem.

## References

[1] Applegate, L., Chen, T.T., Kronsynski, B.R., and Nunemaker, J.F. Knowledge management in organizational planning, Journal of Management Information Systems, 3, 4 (Spring 1987), 20–38.

[2] Booch, G. Object-oriented development. IEEE Transactions on Software Engineering, SE-12, 2 (February 1986), 211–221.

[3] Borgida, A., S. Greenspan and J. Mylopoulos, “Knowledge Representation as A Basis for Requirements Specifications,” Computer, 18(4), April, 1984, p.75.

[4] Cardelli, L., "A Semantics of Multiple Inheritance," Lecture Notes in Computing Science. New York: Springer-Verlag, 1984, pp. 51–67.

[5] Cardelli, L., and P. Wegner, “On Understanding Types, Data Abstraction, and Polymorphism,” Computing Surveys, 17(4), December, 1985.

[6] Cox, B., “Message/Object Programming; An Evolutionary Change in Programming Technology,” IEEE Software, 1(1), January, 1984.

[7] Cox, B., Object-Oriented Programming: An Evolutionary Approach. Reading, MA: Addison-Wesley, 1986.

[8] Cox, B., and B. Hunt “Objects, Icons, and Software-IC’s, BYTE, August, 1986, pp. 161–176.

[9] Dumond, J. and Malbert, V.A. Evaluating project scheduling and due date assignment procedures: An experimental Analysis, Management Science, 34, 1 (January 1988), 101–118.

[10] Fox, M.S. Constraint-Directed Search: A Case Study of Job-Shop Scheduling, unpublished Ph.D. dissertation. Computer Science Department, Carnegie-Mellon University, 1983.

[11] Goldberg, A., and Robson, D. Smalltalk-80, The Language and Its Implementation. Reading: Addison Wesley, 1983.

[12] Guttag, J., E. Horowitz, and D. Musser, The Design of Data Type Specifications (Current Trends in Programming Methodology, Vol. 4). Englewood Cliffs, NJ: Prentice-Hall, 1978.

[13] Kelly, J.E. Critical-path planning and scheduling: Mathematical basis. Operations Research, 9, 3 (May-June 1959), 296–320.

[14] Liberatore, M.J., and Titus, G.J. Management Science practice and R&D project management. Management Science, 29, 8 (August 1983), 962–974.

[15] Liskov, B., and S. Zillis, "Specification Techniques for

Data Abstractions," IEEE Transactions on Software Engineering, SE-1(3), March, 1975.

[16] Nunemaker, J.F., Applegate, L.M., and Konsynski, B.R. Facilitating group creativity: Experience with a group decision support system. Journal of Management Information Systems, 3, 4 (Spring 1987), 6–19.

[17] Malcolm, D., Roseboom, J., Clark, C, and Fazar, W. Application of a technique for research and development program evaluation. Operations Research, 7, 5 (September-October 1959), 646–669.

[18] Malone, T., Grant, K., Turbank, F., Brobst, S., and Cohen, M., Intelligent information sharing systems. Communications of the ACM, 30, 5 (December 1987) 1391–1404.

[19] Pascoe, G., “Elements of Object-Oriented Programming,” BYTE, August, 1986, pp. 139–159.

[20] Patterson, J.H. A comparison of exact approaches for solving the multiple constrained resources, project scheduling problem. Management Science, 30, 7 (July 1984), 854–867.

[21] Philips, B., Staley, J., and Gold, E. Artificial Intelligence in project support. in B.J. Silverman, Expert Systems for Business. Reading: Addison Wesley, 1987, 305–337.

[22] Saitow, A.R. CSPC: Reporting project progress to the top. Harvard Business Review, 47, 1 (January 1969), 88–97.

[23] Sathi, A., Morton, T., and Roth, S. Callisto: An intelligent project management system. AI Magazine (Winter 1986), 34–51.

[24] Shaw, M., “Abstraction Techniques in Modern Programming Languages,” IEEE Software, 1(4), October, 1984.

[25] Smalltalk/PM, Tutorial and Programming Handbook. Los Angeles: Digitalk, Inc., 1989.

[26] Stefik, M. Planning with constraints (MOLGEN: Part I) and Planning and meta-planning (MOLGEN: Part II). Artificial Intelligence, 16, 2 (1977), 111–139 and 141–169.

[27] Stefik, M., Foster, G., Bobrow, D.G., Kahn, K., Lanning, S., and Suchman, L. Beyond the chalkboard: computer support for collaborations and problem solving in meetings. Communications of the ACM, 30, 1 (January 1987) 32–47.

[28] Talbot, F.B. Resource-constrained project scheduling with time-resource tradeoffs: The non-preemptive case. Management Science, 28, 10 (October 1982), 1197–1210.

[29] Thomas, D., “What’s in an Object?” BYTE, March 1989, pp. 231–240.
