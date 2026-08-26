---
otero_id: 20949
otero_key: "ZV4VMHCK"
title: "Design considerations for a virtual information center for humanitarian assistance/disaster relief using workflow modeling"
authors: "Tung X Bui; Siva R Sankaran"
year: "2001"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(00)00129-9"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Design considerations for a virtual information center for humanitarian assistance<sup>r</sup>disaster relief using workflow modeling

Tung X. Bui <sup>a,)</sup>, Siva R. Sankaran <sup>b</sup>

UniÕersity of Hawaii, Manoa, Honolulu, HI 96822, USA

<sup>b</sup> California State UniÕersity, Northridge, CA 91330, USA

## Abstract

There are innumerable human and organizational circumstances when free flowing information is essential for effective decision-making. In a closed system with limited boundary scanning, information handling is a fairly manageable task <sup>w</sup>School Library Journal, 39 1993 146 . However, where sources of data andŽ . <sup>x</sup> <sup>r</sup>or decisions are high volume encompass a large geographic area and cover a gamut of organizational entities, information gathering and fusing can be daunting <sup>w</sup>FEMA, Publication No. 229 4 1995 . This paper analyzes the workflow typical in a disaster scenario and discusses theŽ . Ž .<sup>x</sup> design considerations for a virtual information center VIC that can both efficiently and effectively coordinate and process aŽ . large number of information requests for disaster preparation<sup>r</sup>management<sup>r</sup>recovery teams. The proposed design is domain independent, uses a net-centric approach and can be readily exported to many other governmental and organizational decision environments. The prototype version of the system uses the object-oriented model in connecting to multiple databases across the Internet and has all the essential features that can readily be cloned to enlarge the system’s scope. q 2001 Elsevier Science B.V. All rights reserved.

Keywords: Crisis management; Workflow modeling

## 1. An example scenario

A quiet Friday on a July afternoon was slowly settling towards what was promising to be a sunny three-day weekend over San Francisco Bay. The city was gearing for the annual Independence Day celebrations coming up on the following Monday. In his office at the CalTech Seismic Lab in Pasadena, John continued to monitor the earthquake measuring instruments with concentration. The seismograph had never been quiet but that was normal for the region. The city had been warned of the ‘big one’ for years but nothing major had occurred over the last 6 years. Since that time, the city had been planted with hundreds of sensors across the San Andreas Fault Ž . Fig. 1 . These sensors had been linked by an intricate emergency management system interconnecting several governmental and non-governmental agencies over the cyberspace.

At 3:46 pm, the monitors started picking up earth movements on a scale that was unusual and indicative of a major shake. The seismograph began swinging wildly. The emergency system issued out warnings to all. An adrenaline rush struck John. A big one indeed was coming. He knew it would reach the city in minutes. He collected himself and instantaneously activated the virtual information center VICŽ . he had been trained to operate for just an emergency. In nanoseconds, all the information centers working under it were on standby to take a barrage of information requests from the disaster management team. The system itself was proactively searching for lifesaving information to be passed along as potential warnings to the team. Years of effort in designing the workflow for the dream VIC and building the system were now paying off.

![](/api/attachments/ZV4VMHCK/fulltext/images/ab418f7c597685309ced6381c353f6bb5ec37e85f38c8970355c55c0a404e6d1.jpg)  
Fig. 1. Map showing the San Andreas Fault along the Californian coast USGS . Ž .

The above scenario may well sound futuristic. But the technology for implementing such systems is already beginning to evolve. The explosion of telecommunications technology, the ever expanding Internet, the availability of inter-platform connectivity software and theoretical progress made in group decision and negotiation are all making the concept of the VIC for humanitarian assistance<sup>r</sup>disaster relief a reality more than ever before.

## 2. Toward a global VIC

Given the cosmic design or lack of design of the universe and the inevitability of human errors, disasters are a distinct reality of everyday life. Disasters —both natural and man-made—can strike anytime and anyplace. Perrow 12 advocated that disasters<sup>w</sup> <sup>x</sup> are non-preventable and even argued they can be considered a ‘normal’ occurrence. Some organizations tend to believe disasters do happen but that they only happen to other people 1 . Experience<sup>w</sup> <sup>x</sup> shows that today for their very survival both organizations and nations should design and implement disaster preparedness systems.

There are two ways to overcome disasters: the first is to avert them from occurring through disaster prevention programs, and second to have an emergency system and a plan of preparation and operation 6 . In either method, communication plays an <sup>w</sup> <sup>x</sup> important role in disaster management. In most of the disasters in recent history, at some level or another, information was available which could have prevented or minimized the destruction 7 . But the<sup>w</sup> <sup>x</sup> information was either possessed by those with authority to act upon it but who did not act; or it was possessed by those who did not have the power to act but who did not share them with those who could have. In other cases, information even when received was discounted by the bureaucracy 9 . Hence, in the<sup>w</sup> <sup>x</sup> future, any system devised to manage disaster emergencies should ensure information flows freely and the decision-makers act on such information without fail 5 .<sup>w</sup> <sup>x</sup>

A free flowing information system, if not properly managed, may lead to a barrage of inputs that could be a problem by itself 6 . Decades ago, it was called<sup>w</sup> <sup>x</sup> gathering intelligence, but now it is a constant battle to sort and make meaning out of the glut of data 11 .<sup>w</sup> <sup>x</sup> Over the years, the computer has evolved into an effective tool for managing large volumes of data, filtering and processing them into meaningful information readily usable by decision-makers. With the advent of telecommunications, and due to its versatility and low cost, the Internet has now become the instrument of choice in planning and managing disaster information systems 15 .<sup>w</sup> <sup>x</sup>

A formal organizational structure is thus needed to deal with disaster situations effectively. We refer to this organization as the VIC. The primary task of the VIC is to gather data from field sensors and a variety of crisis-related data warehouses in virtual space and time and process them into life<sup>r</sup>resource saving decisions. Organizing a VIC is expected to demand the latest in technology, a network of command and communications, and the best of managerial skills. This paper discusses the concept of a VIC and the design considerations towards its implementation using workflow modeling. The proposed netcentric approach when implemented on the Internet can serve as a decision support tool for all those responsible for managing a crisis that requires management of multi<sup>r</sup> inter-organizational<sup>r</sup>governmental interactions and covers a large geographic region. Among many, two fundamental functional requirements of the VIC that are considered here are: iŽ . produce answers to a request for information RFI Ž . generated by an emergency relief administrator<sup>r</sup>participant, and ii sift lowest level data, formulate, andŽ . forward a request for attention RFA which areŽ . warning information to be acted upon by the decision makers. We present a domain-independent architecture for the VIC and the workflows involved in processing a RFI. In implementing the RFA, we offer a design strategy that uses a forward-chaining approach along with the application of intelligent software agents. Other objectives of the VIC include streamlining the VIC workflows, improving operational awareness to the decision participants, using new approaches to access non-traditional sources of information and new concepts for managing the acquisition, processing, analysis and presentation of this information.

## 3. Anatomy of a VIC

## 3.1. Organizational Õiew

Typically, the VIC staff consists of a director, senior analysts and researchers. A system administrator and librarians assist in the continuity of operations at each center. The overall architecture of the VIC is shown in Fig. 2. It is envisioned that there will be several VICs each focusing on a specific type of disaster such as earthquake, floods, war<sup>r</sup>aggression. To coordinate the activities at the VICs, we propose the creation of an entity called Crisis Response Center CRC . As the center is ultimately Ž . responsible for the management of all crises, the CRC oversees all the VICs.

Although the VIC is usually implemented physically in the real world, it is envisioned for this study as existing only in cyberspace. An Internet server exists at the CRC and each of the VICs equipped with functional components capable of serving the roles described earlier. Other participating entities in the disaster management such as foreign governments, United Nations relief agencies, and other non-governmental organizations are linked to VIC via the Internet. There are several benefits to using the network-centric approach for the VIC. First, it can take advantage of technology in processing massive amounts of data at a fast rate. Second, since by their very nature, crises require decisions under pressure, rapidly evolving scenarios and uncertain information, response management can be enhanced by the application of technologies capable of facilitating quick and efficient decision making. This could literally translate to lives saved. Third, it can provide a high level of objectivity in decisions. This is particularly useful when multinational relief operations are involved where cultural differences can add to multiple objectives and competing interests. Finally, with the decreasing trend in costs in installing and managing Internet connections, VICs are feasible even for developing countries 4 . <sup>w</sup> <sup>x</sup>

![](/api/attachments/ZV4VMHCK/fulltext/images/24d9c828dddfe64e49f59fa0ada2cb66e0c1dfcfbdb8d9fb47e1848f626c6a65.jpg)  
Fig. 2. Architecture of virtual information center VIC 3 .Ž . <sup>w</sup> <sup>x</sup>

## 3.2. Process Õiew

From a strict operational perspective, workflow deals with the automation of business processes. A workflow could be a one-time-only process or ad hoc workflow, a collaborative process that coordinates a team working together to achieve a goal Ž . e.g., designing systems specifications , or a mission-critical, transaction-oriented production workflow. A workflow management application defines all the business processes, from the start to finish, including all exception conditions, tracks process-related information and the status of each instance of the process as it gets executed.

An efficient workflow is one that is 1 capable of Ž . identifying the best procedural routes either serial,Ž parallel or conditional , 2 able to document and . Ž . make use of rules to ensure the proper load balancing of work assignments based on established business principles and roles of process participants.

Workflow management technology provides a mechanism for planning and controlling how people work together in business environments. It acts as the connectivity tools to manage, monitor, organize and distribute specific business tasks and the associated required information. A principal concept in workflow management is the coordination of tasks in the business process. The medium through which these are conducted might include verbal information, human gesture, documents, images, graphics, sounds and<sup>r</sup>or any type of ‘information’. Due to this wide scope of workflow management, it is difficult to find any one complete definition for it, even though many different definitions have been put forward 13 . We further adopt the expanded view of<sup>w</sup> <sup>x</sup> workflow management by Stohr and Zhao 14 . Ac-<sup>w</sup> <sup>x</sup> cording to Stohr and Zhao 14 , a workflow should<sup>w</sup> <sup>x</sup> not only be used to automate business processes, but also to informate and illuminate its users. The term ‘informate’ refers to the exploitation of information generated by information technology to provide decision makers with more insightful understanding and apprehension of the business situation. The illumination function refers to the use of workflow technologies as a means for knowledge sharing and learning via cognitive feedback 2 .

Based on this expanded definition of a workflow mission, VIC workflow should thus provide four types of support to its users:

v Information

v Cognition

v Collaboration<sup>r</sup>coordination

v Decision

Fig. 3 provides examples of IT technologies that could be used to support these four functions.

The ability of the VICs to respond to crises depends largely on their ability to treat every event as another mode of planned operation, instead of as ad hoc and isolated events requiring unique decision techniques and processes. However, for portability to multiple operational scenarios, it is necessary for these processes to be as generic in their functional scope as possible.

<table><tr><td rowspan="2">Support type</td><td colspan="3">Phases of HA/DR operations</td></tr><tr><td>Pre-crisis</td><td>Crisis response</td><td>Post-crisis</td></tr><tr><td>Information</td><td>- remote sensing &amp; warning- data standardization- document management- needs assessment- integration of infrastructure system database</td><td>- real-time information center-GIS- data standardization</td><td>- dissemination of activity results- dissemination of lessons learned</td></tr><tr><td>Cognition</td><td>- electronic discussion group- satellite network- dissemination of help request to expert group world wide</td><td>- knowledge-based information, filtering- teleconferencing</td><td>- review and self-assessment- knowledge-building and revision of organizational memory</td></tr><tr><td>Collaboration/ coordination</td><td>- group/event scheduling- coordination with regional/national network</td><td>- computer-assisted logistics (tracking, monitoring)- just-in-time support- group/event scheduling- coordination of planing- security (vpn)- language translation</td><td>- interpersonal skills assessment- communications improvements- re-alignment of interorganizational relations</td></tr><tr><td>Decision</td><td>- adoption of decision procedures- staffing- resource allocation</td><td>- group decision support system- computer assisted voting system</td><td>- revised decision procedures and responsibilities- refinement of readiness metrics- re-examination of organizational structure</td></tr></table>

Fig. 3. Workflow functions in humanitarian assistance<sup>r</sup>disaster relief operations.

Five processes are proposed: input, assessment, research, publication and attention Fig. 4 . The in-Ž . put process acts as the interface to gather the user’s

RFI. Typically, this takes the form of email, phone, fax, or a form on the Web. The task of the assessment is to validate, search, and locate the most appropriate researcher-process es that can generate Ž . the answer to the user’s request. The research process consults the knowledge base and develops a response for the RFI. The publication process fuses the results into a presentable response.

![](/api/attachments/ZV4VMHCK/fulltext/images/55c8e816b91966e39b3cc6af335a5fe21fbcbb7e547209e7303a2e2b246fbfcb.jpg)  
User  
Fig. 4. Process view of VIC.

For example, if an RFI had concern with airborne diseases that may occur in the aftermath of an earthquake, medical expertise could articulate the typical airborne diseases currently endemic in the country. This information coupled with modeling information that highlights the likely areas to have atmospheric inversion layers days after the earthquake coupled further with the population base of people in the affected areas could be fused to give a rough idea of how many people could be affected by airborne diseases. This information could then be used to determine the type and quantity of medical supplies required. The publication process finally sends out the recommended answer to the initiator of the RFI.

It must be noted that the VIC also includes an attention process that can proactively search the database for conditions that require urgent intervention from the user even though no RFI had been generated. This is important because in a complex and evolving disaster scenario, it is humanly impossible to assimilate all incoming information and expect a decision-maker to be aware of all the operations to be initiated. The attention process solves this problem. It identifies the data as they get constantly updated and sends out RFA as required.

## 4. Workflow modeling for a VIC

## 4.1. Workflow analysis

At its most basic level, workflow is the automation of a business process. It consists in managing the flow of information that runs across the multiple entities involved in a specific business process. Workflow applications decompose a business process into a number of steps called tasks. In addition to speeding up execution of tasks wherever possible in parallel, understanding of workflow also enables tracking the status of tasks in progress. Earlier studies have shown workflow analysis to be a viable technique in crisis management scenarios 10,13,16 . <sup>w</sup> <sup>x</sup> Workflow analysis involves six steps: identification of processes, policies, practices, routes, rules and roles.

## 4.1.1. Process

This is a fundamental step in workflow design and management that helps to ascertain the real business operations faithfully. It identifies the individual tasks and the algorithms to execute them. In the process definition phase, it is essential to determine what are the goals of the process also known as outputs and what are the requirements for the process known as inputs. Attention should also be focused on the interfaces of the process known as data couplings. Data couplings are useful in guiding the execution of processes in parallel, concurrent, and multitasking environments.

## 4.1.2. Policies

Policies are the rules that govern the way the entities handle a special process. Policies are often written documents and therefore are quite static by nature. These are the rules used to make decisions in the business process and are usually implemented as business rules in the workflow system.

## 4.1.3. Practices

Organizations are not static entities and policies are often adjusted by practices. When developing a workflow system, it is important to take into account all the ‘unofficial’ ways of moving the process. Perhaps, not all of these practices will be reflected in the final workflow system, but those who wish to improve the system to keep with new developments certainly will do so. The policies and selected practices will ultimately dictate the future behavior of the workflow system.

## 4.1.4. Routes

Routes define the way the information is channeled through the different steps of the process. Information can be routed serially, in parallel or conditionally based on a business rule. Whenever possible, using parallel routes tend to avoid bottlenecks.

## 4.1.5. Rules

Rules are the result of the fuse of policies and practices. They describe the way information packets will be routed. They can be triggered by the information on the process e.g., ‘if expenses are bigger than Ž \$10,000 then two levels of approval are required’ ,. or by the internal rules of the business workflow Ži.e., ‘after approval the loan application goes back to the clerk’ . Some rules usually ensure a fair load. among all the process participants.

## 4.1.6. Roles

A role is a metaphor for the individual. In traditional transaction-based information systems, business roles are often hard coded and remain inflexible regardless of who is going to execute the defined set of tasks. So instead of having the document being sent to a specific individual and having to change the workflow system each time the individual does the job, it is much easier to assign the workflow to a role and then the individuals to their specific roles. This separation of role and role executors also enables an individual worker to fulfill more than one role in the process. It also gives more flexibility in load balancing of the workload across multiple workers assigned to perform the same job.

The benefits of implementing a workflow system can be seen at all the levels inside and even outside the company. At the operational level, employees have more control over their processes. Response time from the different actors is reduced and the efficiency of the process improved. Bottlenecks can be easily spotted and addressed. Managers can focus on process improvement rather than supervising the process effectiveness. At the top management level, the information gathered by the workflow system will allow for a rapid evaluation of the importance of the process on day-to-day operations and on the overall productivity. This also ensures a coherent answer each time the organization deals with its clients. Lessons learned from successful implementation of workflow systems suggest that response time and quality of service are improved. Yet, workflow is not the miracle solution. It is difficult to identify the processes that represent a fair level of complexity and bring the most to the organization. It is also a difficult task to decide what the workflow system should automate and what should still be done manually. Another risk is the creation of a ‘parallel procedure’ by the employees who are discontent with the model proposed. Thus, the users input and commitment are critical success factors for the design of any workflow model.

## 4.2. Workflow design

Workflows can be categorized depending on their organizational function and complexity level. This can help in subsequent system implementations since workflows of the same class tend to share coding techniques. Some of the workflows are the result of ad hoc requests common in decision support system environments. Concurrent workflows, on the other hand, coordinate a process among several system components in order to formulate an overall decision for a complex request for information. A third type of workflow can be categorized as jurisdictional workflows. They typically occur within an organizational function or unit alone such as sales or marketing. The VIC workflows are a combination of all the above types.

Fig. 4 shows the workflow model in response to a user RFI. As the procedures vary according to the nature of the request specified in the RFI and resources made available at the time of the operations, the workflow might not necessarily follow the exact path described in the figure. It is the responsibility of the chief of the disaster management team to monitor the VIC accordingly. Thus, in reality, VIC is a context-driven workflow and any model developed and implemented should be flexible enough to dynamically accommodate for certain amount of variations 3 . In addition, there could very well be some<sup>w</sup> <sup>x</sup> processes that cannot be automated at all.

While designing the workflow, it is necessary to take into account all the participants which can be a large number depending on the operation at hand <sup>w</sup> <sup>x</sup> 16 . For example, in an earthquake scenario, apart from the chief of the disaster management team at the crisis resource center, other managers in the various VICs should be considered for accommodating their roles, expectations, type and level of interactions 8 . Typically, these could include the Fed- <sup>w</sup> <sup>x</sup> eral Emergency Management Agency, National Guard, US Geological Survey, CalTech, local medical, police, fire and other service representatives. In international disaster situations, it could be more complicated with having to deal with foreign governments. The contributions of non-governmental players such as the Red Cross, CARE, UN agencies may also complicate the communications. The level of involvement will vary with the nature of every RFI transaction.

Further, the information routed in the VIC workflow is in principle not sent to specific individuals or entities, but rather to the roles that these individuals or entities play. Most often, the behaviors suggest the roles of the participants to achieve a particular task during the workflow. For instance, the ‘Acquire–Integrate–Analyze’ task typically requires that the participants should respond to the RFI using a reasonable amount of joint effort. It could also be either the CRC<sup>r</sup>VIC staff or any other task-competent actor. Finally, the business rules outline the rule of engagement for each of the tasks of the VIC workflow. The group expects that collaboration, timeliness, preparedness and trust are the ground rules for all actors when they join their effort in searching for a RFI response.

## 4.3. Workflow model requirements

Any workflow model should provide a comprehensive workflow diagram similar to Fig. 5 for describing the various paths through which a decision process may flow. This provides an infrastructure for programmers who later would be coding the system. An incomplete or an incorrect model could lead to expensive alterations to the program later. If undetected, it might have serious consequences during an actual emergency. A sound workflow model possesses many other important requirements as well. They are discussed below.

## 4.3.1. Information characteristics

A major design requirement for the workflow model is that the quality of response to the RFIs should meet the goals of the participants in terms of information content, timeliness and ease of interaction. The VIC workflow system should be able to collect critical project status and performance feedback through various online mechanisms such as performance reviewers, email, memo, meeting minutes and conference calls, to report deliverables and variances.

## 4.3.2. Data warehouse

Yet another requirement is that the workflow system supports an information repository for all multi-platform information interchange. This includes RFI, RFA templates and FAQ repositories. The RFI and RFA templates, created and validated, before the occurrence of a particular event could significantly speed up the processing of a RFI during a crisis.

With regard to FAQ, the best approach to deal with a crisis event is to anticipate as much as possible its likely occurrence and the information required to manage it. A repository of frequently asked questions with a comprehensive classification and search capability should be made available to all users. Such a data base would not only help reduce the number of RFIs, but also reduce the response time for providing response to specific RFIs whose answers cannot be entirely found in the FAQ repository. The VIC workflow should be able to update the FAQ repository as it populates its dedicated RFI database, and whenever appropriate, build links to the FAQ repository.

A complementary VIC DBMS is required to provide data manipulation capabilities for handling managerial tasks related to the VIC activities. Two areas of particular importance are the management of expert knowledge bases and performance reporting.

## 4.3.3. Analytical tools

No workflow design activity can be complete without incorporating analytical and quantitative model bases. Although the primary task of the workflow system is to automate business tasks for generating RFI responses, the system should be designed to allow for integration of analytical processing capabilities to manage and filter massive yet possibly not complete incoming information. Analytical tools that can help justify, clarify, and substantiate information via qualitative and quantitative methods are required to help the analysts explore new dimensions of intelligence and strengthen the robustness of their reports. As joint effort among various participants is a key success factor to the VIC process for complex RFIs, tools that help support collaborative and negotiation tools should constitute an integral component of the analysts’ workbench 4 .<sup>w</sup> <sup>x</sup>

![](/api/attachments/ZV4VMHCK/fulltext/images/b87e60a6921dce7192e624fa2734e61ce77dabda33f0ad2bf60560c086d46af1.jpg)  
Fig. 5. Workflow diagram for processing a RIF in VIC.

## 4.3.4. Workload allocation

Managing teamwork dependencies and workload balancing are also vital to workflow models. Triggered by a crisis, workload is typically most intense during the first few hours. The workflow system should have scheduling capacity to even out workload among the participants and support staff. The CRC, as a common resource pool, and the RFI processes, in time of a major event, are likely to require multiple task inter-dependencies. Although the VIC is a centralized one with a CRC conceived to execute the VIC, the variety of information sources Ž . as suppliers of information and the potential variety of requesters of information resemble to one of a matrix organization with a common resource pool and multiple task inter-dependencies across multiple RFI projects. And it is crucial to allow resources in predecessor task to notify affected resources of all critical work critical stoppages and delays.

The VIC workflow system should allow posting of scheduled dependencies to affected resources and add crucial update forecast information, empowering team members in schedule conflict resolution. This would allow the VIC director to focus on critical scheduling issues that may affect the RFI completion date or even require the automatic leveling of the entire program schedule to combine tasks across RFIs i.e., one task can serve more than one RFI ,Ž . and across multiple participants and research processes supporting them.

## 4.3.5. System interface

By its very nature, a RFI is not a frequent activity, unless crises occur more often. It is expected that requesters of RFI do not have access to the VIC workflow system on a regular basis. Thus, the user interface should be simple and easy-to-use. Number of choices e.g., menu selection should be limited toŽ . the minimum. Same design considerations also apply for designing interface for researcher analysts. With a high turnover of personnel, screens should be conformed to standard practices of GUI interface design. If VIC is in full-scale operation with a high volume of RFI processing, electronic signatures for planning and execution authorization should be implemented to increase system interaction efficiency.

## 5. Implementation model for VIC

The prototype implementation of the VIC adapts many of the features of the object-oriented model. The objects, their properties and their relationships used in the system are shown in Fig. 6. In addition, the objects have encapsulated methods that can be transparently invoked when the appropriate events occur during the processing. Table 1 shows an example method packaged in the RFI object.

Objects and methods interact with other objects through the programs. When program statements are executed, depending on the computed values, they generate different events. It is these events that objects respond to. Thus, it is important to have the program charted out carefully during the analysis and design phase. In the VIC prototype implementation, the events that objects respond to are the results of computation arising from the decision statements in the program. The implementation architecture is mirrored after the VIC process described in Section 3.2 earlier.

## 5.1. User interface

This module deals with the input and publication processes. Several templates have been predesigned for RFIs and system responses. A sample form is shown in Fig. 7. Menus guide the user to the relevant choices from the forms library. Java has been used to validate user inputs wherever appropriate. The inputs are typically parsed to create a Structured Query Language SQL query. The query is executed viaŽ . Open Data Base Connectivity ODBC mechanismŽ . in the meta database at the local node and the results are forwarded to the assessment module.

## 5.2. Assessment

The objective of the assessment module is to determine from the input RFI and the connection to the meta data base established by the Input module as to which other secondary databases are to be accessed before a final response can be generated. The meta database relational table consists of attributes that contain both the conditions that the RFI satisfies and the heuristics of which subsequent databases are to be accessed in order to answer it. It must be noted that the methods associated with the objects can pass values among them in the form of parameters. Thus, the AssessCall method Table 1Ž . passes the user RFI values to the research module in the system. The user need not know how the object interacts with the other modules nor with the Internet.

![](/api/attachments/ZV4VMHCK/fulltext/images/15189f801632e294fb07e6b56e002f0b3e5b9d57f88cecf8dc43e5977c02fa67.jpg)  
Fig. 6. Objects and their properties in VIC prototype.

Table 1

<table><tr><td colspan="2">Methods in an RFI object</td></tr><tr><td>Method name</td><td>Description</td></tr><tr><td>Validate</td><td>Validate RFI Interface Input</td></tr><tr><td>AssessCall</td><td>Place call to assessment process module</td></tr><tr><td>ConnectKB</td><td>Connect to knowledge base objects</td></tr><tr><td>Disconnect</td><td>Disconnect after RFI is provided</td></tr></table>

Wherever, there are inconsistencies in the individual answers returned from each database, further negotiation sessions may be established by research to create a compromise solution to the initial RFI. Thus, the final recommendation to the initial RFI could range from a simple additive solution of all the individual database responses to a complex Pareto optimal response.

## 5.3. Research

Once the specific independent databases that are to be connected to are determined and passed as parameter values by the assessment module from the meta table, the research system component takes over. The necessary connection objects and SQL statements are generated and after establishing the ODBC, the query is executed. The retrieved answers are assembled into a single file and passed along to the input-publication interface.

## 5.4. Attention

The implementation model also includes capability to find, assemble<sup>r</sup>report, organize, visualize, and push information tailored to users’ needs. It allows access to multiple heterogeneous databases distributed geographically, facilitated by the use of intelligent agents to search for historical data and new data relevant to defined needs. When fully implemented, the prototype will employ a forwardchaining approach in conjunction with intelligent software agents in order to process RFAs. The agent will continually review data in the database and identify if any of the master list of events has occurred and trigger appropriate methods. Feedback from policy makers to analysts is enabled by on-thefly creation of Web pages for use as a rapid means of distributing hypotheses, directives, decisions, and other types of information.

![](/api/attachments/ZV4VMHCK/fulltext/images/12ffd8b99bfbf0f58d7dc5c2017ed11e8b89bf77cad2cfab62852b9899d30f69.jpg)  
Fig. 7. Request for information RFI Web interface. Ž .

## 6. Lessons learned

Initial experience with the VIC framework and simulations show promise for the overall approach proposed in this study in developing Web-centric disaster management systems. Most of the expectations in terms of information accuracy, response time, and value were met, further confirming the feasibility of the concept. The object-oriented design coupled with the workflow modeling was a powerful combination in exploiting the new trends in the Internet and programming technologies. The utmost shortcomings were felt in the area of collaboration and generating RAFs in push format due to limitations of available tools. Currently, effort is under way in improving the prototype through streamlining of VIC processes, enriching the knowledge bases, embedding intelligence and further enhancing the transparency of the net-centric transactions.

The final version is planned to have the ability to deal with multi-dimensional and rapidly changing data characteristic of disaster emergencies. This will allow the system to accumulate critical decision information for decision-makers while guarding against the information overload in the crisis planning and execution process. This task will focus on providing the team managers with tools that will quickly distill the voluminous quantities of retrieved data<sup>r</sup>information package into knowledge. It will also intelligently organize and present information in advanced visualization formats, such as electronic briefing books or watch boards, tailored to specific crises. Users will be able to drill down to the underlying data, if desired. The briefing books or watch boards must be able to provide for an arbitrary mix of text, diagrams, equations, tables, images single frames orŽ live video , spreadsheets, recorded sound, etc. All of. these formats must be bundled within a common ‘envelope’ to be stored, transmitted, and read playedŽ . as a coherent document entity. The briefing functionality must also include robust analysis and collaboration tools to enable exploitation of data relationships, develop corporate memory, and facilitate group<sup>r</sup>team collaboration and information sharing. The interface will facilitate video-, audio-, and text-based collaboration.

## Acknowledgements

The authors would like to thank Dr Michael Sovereign, from the Naval Postgraduate School, and USN Captain Retired Carl Schuster, for their inspi- Ž . rational work on humanitarian assistance<sup>r</sup>disaster relief and to Sunwon Cho and Joao Lourenco, both graduate students at the University of Hawaii, for their inputs on the design of the VIC workflow and its database structure.

## References

<sup>w</sup> <sup>x</sup> 1 R. Allinson, Global Disasters, Prentice Hall, New York, 1993.

<sup>w</sup> <sup>x</sup> 2 T. Bui, C. Loebbecke, Supporting cognitive feedback using systems dynamics: a demand model of the global systems of mobile telecommunication, Decision Support Systems 17 2Ž . Ž .1996 83–98.

<sup>w</sup> <sup>x</sup>3 T. Bui, J. Lourenco, Evaluation of the Current VIC Resource Center Workflow Process, Technical Report, University of Hawaii, Manoa, 1999.

<sup>w</sup> <sup>x</sup> 4 T. Bui, S. Cho, M. Sovereign, A framework for designing a global information network for multinational humanitarian assistance<sup>r</sup>disaster relief, Information Systems Frontiers 1 Ž . Ž . 4 2000 427–442, April.

<sup>w</sup> <sup>x</sup> 5 S. Champion, C. Master, When disaster strikes, School Library Journal 39 9 1993 146–149.Ž . Ž .

<sup>w</sup> <sup>x</sup> 6 D. Crichlow, Taking a comprehensive approach to handling disasters, American City and County 1997 50–60, June.Ž .

<sup>w</sup> <sup>x</sup> 7 R. Delude, Dealing with disasters, School Planning and Management 35 2 1996 35–37.Ž . Ž .

<sup>w</sup> <sup>x</sup> 8 V. Garland, M. Morimoto, Kobe earthquake, T.H.E. Journal 23 8 1996 79–81.Ž . Ž .

<sup>w</sup> <sup>x</sup> 9 J. Hale, A layered communication architecture for the support of crisis response, Journal of Management Information Systems 14 1 1997 235–255, Summer.Ž . Ž .

<sup>w</sup> <sup>x</sup> 10 H.Y. Mak, A.P. Mallard, T. Bui, G. Au, Building online crisis management support using workflow systems, Decision Support Systems 25 3 1999 209–224.Ž . Ž .

<sup>w</sup> <sup>x</sup> 11 I. Mitroff, P. Shrivastava, F. Udwadia, Effective crisis man-

agement, The Academy of Management Executive 1 3Ž . Ž . 1987 18–27, November.

<sup>w</sup> <sup>x</sup> 12 C. Perrow, Normal Accidents: Living with High Risk Technologies, Basic Books, New York, 1984.

<sup>w</sup> <sup>x</sup> 13 M. G. Sovereign, Humanitarian Assistance and Disaster Relief in the Next Century, Workshop Report, October 28–30, 1997.

<sup>w</sup> <sup>x</sup> 14 E.A. Stohr, L. Zhao, The expanding mission of workflow technology, Document World 3 5 1998 21–26, Oct–Nov.Ž . Ž .

<sup>w</sup> <sup>x</sup> 15 R. Tobin, R. Tobin, Emergency Planning on the Internet, Government Institutes, Rockville, MD, 1997.

<sup>w</sup> <sup>x</sup> 16 K. Weick, Enacted sensemaking in crisis situations, Journal of Management Studies 25 4 1988 316–331, July.Ž . Ž .

Tung Bui is Matson Navigation Company Professor at the College of Business Administration, University of Hawaii, Manoa. Dr Bui holds a doctorate in managerial economics from the University of Fribourg, Switzerland, and a PhD in information systems from New York University. He has done extensive work in effective implementation of information technology in organizations.

Siva Sankaran is professor of Management Information Systems at the California State University at Northridge. Earlier, he taught at the Naval Postgraduate school in Monterey, CA. He holds a PhD in information systems from New York University. His research interests include Web-based education, entrepreneurship and telemedicine.
