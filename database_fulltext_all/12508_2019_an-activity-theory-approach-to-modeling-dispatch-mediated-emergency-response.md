---
otero_id: 12508
otero_key: "YMBG9CM5"
title: "An Activity Theory Approach to Modeling Dispatch-Mediated Emergency Response"
authors: "Rohit Valecha; H. Raghav Rao; Shambhu J. Upadhyaya; Raj Sharman"
year: "2019"
journal: "Journal of the Association for Information Systems"
doi: "10.17705/1jais.00528"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# An Activity Theory Approach to Modeling Dispatch-Mediated Emergency Response

Rohit Valecha<sup>1</sup>, H. Raghav Rao<sup>2</sup>, Shambhu J. Upadhyaya<sup>3</sup>, Raj Sharman<sup>4</sup>

<sup>1</sup>University of Texas at San Antonio, U.S.A., rvalecha6446@gmail.com <sup>2</sup>University of Texas at San Antonio, U.S.A., mgmtrao@gmail.com <sup>3</sup>University at Buffalo, U.S.A., shambhu@cse.buffalo.edu <sup>4</sup>University at Buffalo, U.S.A., rsharman@buffalo.edu

## Abstract

Emergency response involves multiple local, state, and federal communities of responders. These communities are supported by emergency dispatch agencies that share digital traces of task-critical information. However, the communities of responders often comprise an informal network of people and lack structured mechanisms of information sharing. To standardize the exchange of task-critical information in communities of responders, we develop a conceptual modeling grammar. We base the grammar on an activity-theory perspective and ground it in an analysis of emergency dispatch incident reports. The paper contributes to research in dispatch-mediated emergency response literature by (1) developing a framework of elements and relationships to support critical information flow within emergency communities of responders, (2) developing a conceptual modeling grammar for modeling emergency tasks in dispatch-mediated emergency response, and (3) implementing a prototype system to demonstrate the utility of the conceptual modeling grammar.

Keywords: Dispatch-Mediated Response, Conceptual Modeling Grammar, Activity Theory, Emergency Response, Community of Responders, Information Sharing

Sandeep Purao was the accepting senior editor. This research article was submitted on February 2, 2015 and went through three revisions.

## 1 Introduction

Emergency response in the US is dispatch mediated i.e. information from the scene is directed toward responders and agencies through the dispatch agency (Valecha, 2015). It is a complex operation involving multiple communities of fire, EMS, police, dispatch, etc. The “community of responders” is a group of emergency personnel who share a set of activities, and who interact to achieve shared objectives, and to maintain their community (Fisher & Bennion, 2005). These communities of responders help cumulate and transfer expertise, and improve the capacity to respond to emergencies (Aedo, Díaz, Carroll, Convertino, &

Rosson, 2010). As the role of these communities grows, particularly in such intensive settings, it becomes increasingly important to understand them and to provide computer tools to support their functioning (Fisher & Bennion, 2005). However, unlike an organizational network, which has welldefined information pathways, a community of responders is often an informal network of responders who share expertise and practical advice at different levels. The responders engage in various practices and utilize different resources and tools that are a part of the work systems. Furthermore, they utilize different vocabularies, different spoken languages, different universes of discourses, and different concerns. The differing terminologies make it difficult for responders to exchange information efficiently (Valecha, Sharman, Rao, & Upadhyaya, 2013; Valecha, 2019). Consequently, there is a need for common knowledge about how to interoperate disparate emergency systems (Chen, Sharman, Chakravarti, Rao, & Upadhyaya, 2008; Chen, Sharman, Rao, & Upadhyaya, 2013).

A conceptual modeling grammar would facilitate a unified vocabulary with a set of elements and relationships (Wand & Weber, 2002) to enable emergency responders to share vital task-critical data with parts of their own agencies—as well as with agencies in neighboring cities, counties, or states, or voice information across jurisdictions—to successfully respond to day-to-day incidents and largescale emergencies (Valecha, Sudumbrekar, & Sharman, 2012). In this paper, we develop a conceptual modeling grammar as a tool to help communities of responders to share their expertise. A first step in developing the grammar is to model dispatch-mediated emergency tasks. <sup>1</sup> We utilize activity theory (Engeström, 1987) for the extraction of key concepts embedded in task-critical information supplied by the emergency communities of responders. The conceptual modeling grammar is grounded in an analysis of more than 1000 emergency dispatch incident reports. Further, we design and develop a prototype system to demonstrate the utility of the conceptual modeling grammar.

In line with the existing discussions in design science, this paper adheres to the design science research guidelines (Hevner, March, Park, & Ram, 2004; Niederman & March, 2012; Peffers, Tuunanen, Rothenberger, & Chatterjee, 2007; Purao et al., 2008). This paper is organized as follows. Section 2 presents the emergency scenario and the emergency organizational hierarchy. In Section 3, we discuss related work. Section 4 presents the methodology for grammar development, including the design considerations. In Section 5, we discuss the grammar, including the key elements and relationships used to model emergency tasks. In Section 6, we evaluate the grammar through case application and prototype implementation. Finally, we conclude the paper with remarks on the contributions of this research and some future research directions.

## 2 Emergency Response Overview

Figure 1 depicts the emergency situation that is common for most day-to-day incidents. Various emergency agencies such as fire, emergency medical service (EMS), and police swing into action following the initial 911 call to the dispatch agency. The dispatch agency assigns an incident commander to the emergency. The incident commander becomes responsible for mitigation of the incident and is charged with the authority to take appropriate actions. Upon arrival at the scene of the incident, the incident commander may request additional resources from the dispatch agency based on his/her assessment of the situation.

![](/api/attachments/YMBG9CM5/fulltext/images/b229a555506b39df8c8186b6f327b65002071921e4f193c7dca678737136b83c.jpg)  
Figure 1. Emergency Scenario

The initial notification of the incident is received by the dispatch agency, which then generates an incidentrelated document known as the “incident report”. The initial notification, along with geographical information, emergency details, etc. is entered by the dispatch personnel in the incident report as “general information”. The information about the responding vehicles that arrive at the scene of incident is stored in the report as “vehicle response summary”. This section also lists physical resources such as ladders, pumpers, rescue trucks, and other emergency equipment.

The response comments are logged under “dispatcher comments”. Dispatcher comments do not denote direct communication (of responder messages), but rather refer to emergency tasks that take place in the course of time. For example, let us consider the comment “Not National Fuel” (Line 1 under “Dispatchers Comments” in Figure 2). This comment does not identify who sent the message, for whom it was intended, or from what channel it was delivered; rather, it denotes the task of notifying the national fuel agency. The report also includes a summary of the incident under “incident comments”. Figure 2 shows an excerpt of the dispatcher comments (depicting response tasks) from an incident report of a massive fire.

While the incident report seems well organized, consisting of sender information, time stamp, and information content (in the three columns), it does not follow a set standard. For example, the National Fuel and Gas Agency is identified as “National Fuel” and “NATL FUEL” in the below report. In similar other reports, they are also identified as “nfg”, “nf” and so on. Another example is that of notifications. The report uses terms like “not” and “notfd”. Some other reports use “notified”, “paged”, “alerted”, etc. for the same. Different emergency agencies create incident reports using their own vocabularies. Due to the lack of a common standard between the agencies, the adoption of one of the existing incident reporting vocabularies would still not achieve standardization. Toward this end, we aim to standardize the incident reports by developing a common vocabulary.

The incident reports identify different response tasks that take place during the response. Let us consider an example task: the responder is reporting the contact information for the commander (Line 2 under Dispatchers Comments in Figure 2). In a second task, Cheektowaga fire agency (denoted as CHEEK) and Niagara Country Sheriff are notified of the commander’s (denoted as EOC) contact information (Line 7 and 8 under Dispatchers Comments in Figure 2). The red box shows the resource transition of the ambulance unit, where the EMS agency provides the unit’s status. The status of the ambulance unit changes from “dispatched” (DS) to “enroute” (EN) to “at scene” (AS).

Dispatchers Comments  
![](/api/attachments/YMBG9CM5/fulltext/images/a1e403de596ccfe332e6c5d05981f84234c52802908f35321270b87d97574a8e.jpg)  
Figure 2. Dispatcher Comments in Incident Report

The emergency tasks are subject to rules delineated in the mutual aids—agreements that denote the exchange of resources between agencies. Moreover, these tasks also follow a division of labor as per the chain of command, based on the Federal Emergency Management Agency’s (FEMA), Incident Command Structure (ICS; available at http://www.firescope.org). The command structure (also known as chain of command) is the formal line of authority and responsibility within an organization. It defines specific information channels that need to be followed in the organization, and often provides task associations and responsibilities. Higher ranked officers supervise those under them, but they are typically not permitted to command responders from other units that are not under their direct supervision. Chain of command helps avoid conflicts relating to authority, jurisdiction, and responsibility of the agencies and the agents.

## 3 Literature Review

In this section, we discuss the existing literature on conceptual modeling grammar. Subsequently, in order to elicit the development process for the grammar, we provide a discussion on activity theory, which provides the theoretical lens used in this paper.

## 3.1 Conceptual Modeling Grammar

A conceptual modeling grammar provides a set of elements to model real-world domains (Wand & Weber, 2002), and to define their representation schema. In addition, it also determines the rules on combining the elements (Kishore & Sharman, 2004; Zhang, Kishore, Sharman, Ramesh, 2007). Developing a conceptual modeling grammar can help bridge the gap in the literature in this area. As a case in point, Purao & Woo (2014) also suggest developing new grammars for modeling complex domains.

There are two theoretical traditions within the information systems literature that can be utilized to create a representation of the emergency domain in the design of conceptual modeling grammars: linguistic theories and activity theory.

(1) Linguistic theories: Prior literature in linguistic theories has explored conventions for creating linguistic-based conceptual models (Barker, 1990; Chen, 1983). These theories recommend “using the part-of-speech for identifying objects and methods; associating classes with nouns, relationships with verbs, and attributes with adjectives and prepositional phrases” (Overmyer, Lavoie, & Rambow, 2001, p. 402). Linguistic theories allow for the examination of sentences containing clauses and phrases that describe and relate several objects, conditions, events and/or actions, generalizations, and are open to multiple interpretations (Al-Safadi, 2009).

Some researchers have suggested speech act theory as a basis for developing conceptual modeling grammars (Wand & Weber, 2002). Speech act theory offers promising avenues for identifying interactions (Winograd & Flores, 1987; Wand, Monarchi, Parsons, Woo, 1995). The extension of conceptual modeling techniques with linguistic theories “increases…the capability to formalize well-known conceptual aspects, like object roles and constraints” (Burg & Van de Riet, 1997, p. 131).

(2) Activity theory (AT): Researchers have used the alternative approach, activity theory, as a theoretical framework to inform conceptual model development (Kuhn, 2001; O’Leary, 2010). Activity theory provides a lens capable of deconstructing the complexities in the natural setting, to analyze the current practices, and also to inform the design process (Kaptelinin, Kuutti, Bannon, 1995; Igira, 2008; Chen et al., 2008). For instance, Korpela, Soriyan, Olufokunbi (2001) have utilized activity theory to understand work practices and used the insight to inform the design of information systems.

Activity theory deals with the purpose of information exchange as well as the result achieved by relevant processes. It uses the modeling of dynamic relations in society, between people. Activity theory is “individual-centered”—i.e., generally oriented toward putting the subject in the center and giving an important place to the negotiation (a mediated coordination) of the flow of actions (Chaudhury, Mallick, Rao, 2001). This allows us to analyze emergency response as an activity-centric and agentcentric process (Raghu, Jayaraman, Rao, 2004).

As a case in point, we note that many dispatcher comments require an understanding of the context surrounding the task. For example, let us consider the comment—“Clarence Center Chief” (line 9 under Dispatcher Comments in Figure 2). Using linguistic theoretical approaches that perform the identification of specific semantic elements within the user’s requirements (such as entities, attributes, relationships, cardinalities and multiplicities), this piece of information may be identified as an entity (responder). On the other hand, the activity theory framework allows us to conceptualize this task within its context (using the concept of division of labor), which implies that the Clarence Center Chief is assuming the role of the incident commander for that fire incident.

Due to the consideration of emergency tasks within the dispatch incident reports (discussed in Section 2) and the metarequirements of the conceptual modeling grammar for complex domain (discussed in Section 3.1), we choose activity theory over linguistic theories. We suggest that the insights offered by activity theory can support the development of the conceptual model for complex activities within the emergency response context (Wells, 2002).

## 3.2 Activity Theory Approach

In activity theory, the minimal unit of analysis is the activity system (Kuutti, 1996). An activity consists of six elements: subject, tools, object, division of labor, community, and rules and procedures (Chaudhury et al., 2001; Chen et al., 2013). The activity is directed toward an object, mediated by tools, and socially constituted within the community (Bertelsen & Bodker, 2003). The subject is the individual or the group performing the activity and is supported by the instruments that can be either conceptual or material tools (Valecha, Kashyap, Rajeev, Rao, & Upadhyaya, 2014). The object is shared by the people in the community making up the activity system. The interaction between the subject and the object is confined within the community that consists of rules and division of labor (Chen et al., 2013). Rules cover norms, expectations, conventions and social relations within a community (Kuutti, 1996). Division of labor refers to the allocation of tasks within the community.

Engeström (2001) outlines four fundamental principles of AT: object-orientedness and mediation, multivoicedness and context, historicity and emergence, and expansive transformations (Nardi, 1995; Kaptelinin, Nardi, & Macaulay, 1999; Kaptelinin & Nardi, 2006; Clemmensen, Kaptelinin, & Nardi, 2016), which are discussed below. These basic principles of activity theory are important considerations in the design of conceptual modeling grammar within the emergency domain.

(1) The prime unit of analysis is an activity system— an artifact-mediated (tool-driven) and object-oriented (goal-directed) system of actions. Artifacts shape the way human beings interact with reality (Kaptelinin et al., 1999). An activity utilizes various artifacts such as procedures, signs, instruments, methods and laws, etc. through which actions on objects are mediated. An object is “something given and something projected” (Engeström, 1995, p. 397). Objects <sup>2</sup> reflect the motivational (objective) or purposeful nature of activity and are targeted toward the satisfaction of identified objectives (Mwanza, 2001). By explicating five distinct conceptions of object <sup>3</sup> in the context of medical work and general practice, Engeström (1995) identifies that “fundamentally different conceptions of the object…also exist side by side across specializations and within one and the same domain of specialization” (p. 400).

(2) An important principle of activity theory is social behavior. Every activity system engages diverse groups of actors, and thus is subject to multiple perspectives and beliefs (i.e., multivoicedness). Activities are collective systems situated in a meaningful context and socially constructed (Nardi, 1995). An activity system starts with an abstract representation of context and then situates this representation in reality (Kaptelinin et al., 1999). As pointed out by Kuutti (1996), it is impossible to understand an activity in isolation, without the meaningful context. Activity theory considers the engagement of people with their world as a socially mediated process (Cole & Engeström, 1993), and studies activity as a system of coordinated actions within a social group oriented toward a goal. For example, responders work together as communities (such as police, fire, EMS, etc.), and they impose their culture, skills, and training on the response action.

(3) The activity systems get transformed with time or context—in other words, human actions, and institutional structures can be analyzed by their own history (i.e., historicity). This is an important driving force in the development of activity systems (Allen, Karanasios, & Slavova, 2011; Allen, Brown, Karanasios, & Norman, 2013; Karanasios et al., 2013). Moreover, as practices change and processes develop, responders and teams move back and forth from their usual workplaces. The elements involved in the response activities change as the activities undergo frequent transitions. We observe the transitions of emergency response activities, to capture important state-related elements into the conceptual modeling grammar. For example, resources that are deployed at the scene get exhausted, and thus are released to their respective agencies. Activity theory allows us to focus on the processes and creative interactions that enable responders to develop the new process experience necessary to move forward.

(4) An activity system’s capability can be expanded through changing actions. It is through interactions that the structural components of the activity system expand. In other words, interaction within the activity system can lead to a reimagined activity system by expanding the object of activity (Shankar, Agrawal, & Rao, 2010). For example, there is a relationship between the subject and community elements. If there is a change in the community element, it will affect the subject element. Such interactions indicate emergent opportunities for activity development and can be used as sources of improvement (Kuutti, 1996). The systemic nature of activity systems implies that if there were a change in one element, it would cause changes in other elements as well (Nicolini, 2013).

We apply activity theory to investigate emergency response along the dimensions of the activity system— including subject, object, instrument, community, rules, division of labor, and the principles of the activity system: object-orientedness and toolmediation, multivoicedness and context, historicity and emergence, and expansive transformations. By enabling responders to capture the key concepts of emergency response tasks, activity theory can be used to simplify the complex workflows. This structure provides the “root model” of the emergency activity (Engeström, 1987), and a conceptual framework for the inquiry of the emergency response. There is a mapping between the activity system structure and the ontological structure (i.e., “concepts” and “relationships between concepts”), which lends itself to bridging the transition between the human-based and machine-based models. This facilitates an in-depth understanding of the response setting.

## 4 Methodology

In this section, we explicate the activity theorydriven process of developing the conceptual modeling grammar. Figure 3 provides an overview of the grammar development process.

![](/api/attachments/YMBG9CM5/fulltext/images/2d50141678ed38323877fc5fb31020834235ea7e04c72cd7327454d0794b83b2.jpg)  
Figure 3. Process of Conceptual Grammar Development

## 4.1 Data Collection

We used multiple methods and sources of evidence to study the work of the emergency teams. These sources provided a foundation for understanding the emergency response to help us develop a conceptual grammar. Following Valecha et al. (2013), the data collection methods included: (a) incident reports that documented all the phases of the emergency response, and (b) responder interviews that assisted in triangulating the data from the incident reports. The responders’ role was to clarify the emergency terminology in the incident reports, allowing the the researchers to derive an overview of the emergency activities, elements, and interactions.

To acquire a deeper understanding of the dispatchmediated response, we collected 1147 incident reports generated between 2008 and 2010 from a dispatch agency in the western New York area. These documents included general information about the incident, information about the resources deployed, and details of the response tasks. The data collection strategy was premised on collecting enough rich data of interaction between emergency responders to enable the tracing of emergency events, and the understanding of work disagreements and their solutions. This resulted in extracting 10,411 tasks from the incident reports performed by dispatch and other emergency agencies.

## 4.2 Activity Theory Guided Expert Interviews

We contacted four dispatch responders with more than five years of experience in dispatching resources to emergencies. Each of the dispatch responders also had experience dealing with emergencies in their other roles as volunteer fire chiefs, emergency medical technicians, or other emergency personnel. The responders were not familiar with activity theory; thus, following previous researchers (such as Barley, 1990), who have sought to understand work processes by engaging with actors in their own languages, we conducted interviews to grasp the emergency terminology and to understand the flow of events from a responder’s perspective. The interviews were conducted in the context of the incident reports—we chose a random sample of 10 reports<sup>4</sup> on which to seek responders’ feedback during the interviews.

In the interviews, we asked responders to describe the emergency terminology in the incident reports for the purposes of understanding the various aspects of the process. The responders read each element from the reports and clarified its meaning. We also asked the responders to (1) describe the attributes of each element, and to comment on its restrictions and relationship <sup>5</sup> to other elements; (2) identify the states through which each of the elements transitions; and (3) discuss the different emergency activities and their inherent contradictions. The responders also addressed how emergency responders negotiate to handle such contradictions.

## 4.3 Activity Theory Guided Information Processing

After identifying the emergency activities, we adopted an iterative process of “within” and “across” activitysystem analysis to produce a rich descriptive account of how activities are organized and developed at different phases of an emergency. We used this descriptive account as a basis for identifying how emergency practices emerge, develop, and change. The raw data (10,411 tasks) were examined to understand the nature of activity in detail. In this process, we utilized activity theory as a framework for grouping <sup>6</sup> the various elements together. We now move to a discussion of the details of element extraction and relationship formalization.

We performed the iterative process of “within” activity-system analysis in a first, second, and third round (detailed here). At the outset, the responders provided three key emergency elements—namely, responder, agency, and resource—which are pivotal to most emergency activities. We extracted the contents of 10,411 tasks based on this element set. For example, in the task “Rapids alerted for manpower”, Rapids refers to the agency and manpower refers to the resource needed. However, there were also some tasks, such as “New command phone XXX-XXXX”, that included additional details not relevant to the elements of responder, agency, or resource. We extracted 3943 tasks that we identified as having at least one component that was not relevant to responder, agency, or resource.

In the second round, the responders inspected the unidentified elements in this set of 3943 tasks. They pointed out that the unidentified elements were often related to information or workflow. The responders were also able to recognize response elements that included traces of emergency information, and suggested that mutual agreements following a certain chain of command instantiated the emergency workflow element. We extracted content from the previously excluded 3943 tasks based on this new element set, comprising responder, agency, resource, response, mutual aid, and command. The extraction based on this new element set accounted for all the tasks in the incident reports.

In the third round, we started off with the set of six elements obtained from the second round. We asked the experts to identify relationships between the elements. The experts compared the elements to derive relationships among them. For example, the experts pointed out that a responder belongs to an agency. Their analysis generated a set of 12 relationship types: utilize, request, deliver, direct, manage, deploy, belong, offer, act, provide, restrict, and follow.

We performed the iterative process of “across” activity system analysis in the fourth round (detailed here). In this round, we asked the dispatch responders to suggest the key negotiations between on-site commanders and remote agency chiefs. They described how responders, commanders, and agencies negotiate resources and aid/assistance based on the response. For example, the incident commander at the emergency site may need a 100-gallon water pumper for extinguishing small fires, which is already in use at a different emergency site. In this case, the incident commander negotiates the pumper from nearest available emergency agency.

In summary, during our interviews, the four experts identified the various elements available during the response. They provided explanations pertaining to the use, attributes, and restrictions of these elements. Finally, they identified the interaction of these elements in contradicting emergency activities.

## 5 Conceptual Modeling Grammar

In this section, we describe the activity theorybased conceptual modeling grammar, which consists of constructs and predicates, emergency negotiations, and state transitions.

## 5.1 Constructs and Predicates

An emergency response operation is composed of emergency activity components and the relationships among them. Thus, it is important to identify which aspects of an activity theory-based analysis can help capture a view of emergency activity. Emergency activities include the acting subjects and the objects the activities are directed toward using the mediating components within the external environment (see Figure 4). The subject is the responder who participates in the activity by sharing the task-critical information. The responder’s role determines how tasks are integrated into the emergency activity. The conceptualization of the activity illustrates that the responder (subject) undertakes response tasks (activities).

Object-orientedness: The information about the object guides the construction of the problem space. In the analysis of the object, Engeström (1987) emphasizes a thorough understanding of the motivations for the activity being modeled. The subject’s motivation determines the perspectives that are represented in the understanding of the activity system goals. The object in the emergency activity system can be on-site or offsite response data, and the objective can be the responder’s motivation to respond to the task at hand through various attempts. In some cases, the response motivation can be to update the dispatch agencies of the on-site information or to request updates from offsite agencies, while in some other cases, the response intent can be to respond to the emergency (e.g., by suppressing or containing fire).

Tool-mediation: A tool enables an activity by making it feasible and possible (Kuutti, 1996). Tools primarily describe the types of methods and information resources that constrain the activity. Tools are needed to articulate the problem space, specifically in terms of the kinds of instruments that are available to subjects for transforming objects in that space (Leont’ev, 1974). In an emergency response, the responder performs emergency tasks using physical and mental resources. The physical resources in this case (i.e., ladders, pumpers, rescue trucks, and so on) are clearly listed in various databases, but intangibles like skills and training, are less well-defined in terms of when and how they should be employed to interact with the environment.

Multivoicedness: The community and its rules determine the problem setting, and the division of labor determines the relationships among the actors. The relationship among community members in the context of the the activity constitutes the social context. This means that the activity is distributed across and is situated within the community, and that it is based on community rules and the division of labor (Barab & Plucker, 2002). In the context of emergency response, the community is the network of on-site, dispatch or off-site responders, which specifies the aspects relevant to the external emergency environment. The emergency activity is bounded by rules and norms that are influenced by mutual aid. Mutual aid ensures agreement on response capacity during each phase of the emergency. The emergency activity adheres to a division of labor that identifies the responsibilities of the responders within the incident command structure.

The conceptualization of emergency activity also depicts the relationship between the emergency activity elements. The responders act in response, and utilize the resources deployed for the response. These responders report to the agency and request mutual aid and assistance. The agencies follow the command(er), provide a response, deliver mutual aid and offer resources, and the command center manages the response. The process of element identification and relationship formalization yields the conceptual grammar.

Figure 4 provides a graphical representation of the resulting activity theory-based framework for modeling emergency tasks. Here we illustrate a higher level of abstraction, consisting of key elements (denoted in underlined text: subject, object, instrument, community, rule and responsibility, and division of labor) and their relationships (identified as circles from A through L).

Next, we define the elements as a set of schemas using controlled natural language description. The relationships, attributes, and constraints, which govern the use of the elements, are also discussed. Table 1 defines the key emergency activity elements, presents the notations and symbols used in specifying the elements, and provides examples for each of the elements. The notations apply to all the symbols used to explicate the various ontological categories and relationships. Table 2 provides a list of predicates that are used in specifying the grammar. These predicates can be considered as relationships linking the elements together. Table 2 also explains each of the predicates with constraints.

Figure 5 provides the conceptual representation of the toplevel emergency response elements: responder, resource, agency, mutual aid, command, and response. It also identifies the various relationships between the elements (Sowa, 1999): utilize, request, deliver, direct, manage, deploy, belong, provide, act, offer, restrict and follow. At the top level is the emergency response universe.

The conceptual modeling grammar uses the notion of activity to capture system requirements. As a central concept in the conceptual modeling, activity is the focus of the grammar. An activity is a series of processing actions performed by a responder while providing response to chaotic event(s). Each responder performs activity individually and interacts with other responders in the system. The responder is a part of the emergency agencies that uses the notion of a command structure to represent the business rules and hierarchical structure that governs responders’ behaviors. The notion of resource is used to model inputs required and outputs generated during the course of the activity. The key features of the conceptual modeling grammar are, therefore, activity, responder, resource, agency, response, mutual aid, and command, which interact with one another during the course of emergency operations. Figure 5 depicts these fundamentals in a metamodel of the conceptual modeling grammar.

## 5.2 Emergency Negotiations

Activity interactions: Activity theory recognizes changing actions through the notion of “interactions”. AT allows us to focus on the interactions that enable participants to develop the new process experience necessary to move forward. It provides a lens for investigating the interaction of the responders from different backgrounds as they engage in a collaborative response. Accordingly, the conceptual modeling grammar uses the notion of interaction as a mechanism of negotiation between the activity systems. An interaction is a series of actions that take place between activity systems to resolve interdependencies.

In our interviews, the responders mentioned that the emergency operation is a two-way setup. The emergency response consists of two activity operations, namely request operation (on-site to remote) and response operation (remote to on-site). The incident commander evaluates the intensity of the damage at the event site. Based on these perceptions, the incident commander requests resources from the remote agencies. To provide the resources to the incident commander, the remote agency responds based on a set agreement. Each activity may be analyzed in terms of the dimensions of responder, resource, agency, response, command, and mutual aid. In addition, the two activity systems interact with each other. In cases where the requests cannot be fulfilled partially or fully, the dispatch responders negotiate with on-site commanders and remote agency chiefs before responding to the requests. The negotiations help resolve resource conflicts, command issues, etc. Figure 6 depicts the activity theory-based framework for considering emergency response negotiations

Table 1. Element Formalization with Constraints

<table><tr><td>Element</td><td>Example</td><td>Attribute</td><td>Constraint</td></tr><tr><td>Responder ‘r’</td><td>M91: Main &amp; Transit chief first assist</td><td>Agency</td><td>Each responder belongs to an agency</td></tr><tr><td>Agency ‘g’</td><td>CC: Clarence center</td><td>Agreement</td><td>Each agency specifies its agreement</td></tr><tr><td>Resource ‘s’</td><td>G5: Getzville pumper</td><td>Type, agency</td><td>Each resource is offered by an agency</td></tr><tr><td>Command ‘m’</td><td>E9 COMMAND: Eggert chief assigned as commander</td><td>Role</td><td>Commander is assigned to a role</td></tr><tr><td>Response ‘v’</td><td>NOT: Notify National Fuel</td><td>Agency</td><td>A response can be provided by single or multiple agencies</td></tr><tr><td>Mutual Aid ‘d’</td><td>THIRD ALARM EMS: Medical aid agreement in effect</td><td>Level, type</td><td>Each alarm denotes type and severity</td></tr></table>

Table 2. Predicate Formalization with Constraints<sup>a</sup>

<table><tr><td>#</td><td>Predicate</td><td>Meaning</td><td>Constraint (from)</td><td>Constraint (to)</td></tr><tr><td>A</td><td>Utilize (r, s)</td><td>Responder utilizes resource</td><td>Each responder can use multiple resources</td><td>Each resource can be used by only one responder</td></tr><tr><td>B</td><td>Request (r, d)</td><td>Responder requests aid</td><td>Each responder can request multiple mutual aids</td><td>Each mutual aid can be requested by multiple responders</td></tr><tr><td>C</td><td>Deliver (g, d)</td><td>Agency delivers aid</td><td>Each agency can respond to one mutual aid</td><td>Each mutual aid can be responded by multiple agencies</td></tr><tr><td>D</td><td>Direct (m, g)</td><td>Commander directs agency</td><td>Each commander can direct multiple agencies</td><td>Each agency can be directed by one commander</td></tr><tr><td>E</td><td>Manage (m, v)</td><td>Commander manages response</td><td>Each commander manages multiple responses</td><td>Each response is managed by one commander</td></tr><tr><td>F</td><td>Deploy (v, s)</td><td>Response deploys resource</td><td>Each response can deploy multiple resources</td><td>Each resource can be deployed in one response</td></tr><tr><td>G</td><td>Belong (r, g)</td><td>Responder belongs to the agency</td><td>Each responder can belong to one agency</td><td>Each agency can utilize multiple responders</td></tr><tr><td>H</td><td>Provide (g, v)</td><td>Agency provides response</td><td>Each agency can provide multiple responses</td><td>Each response can be provided by multiple agencies</td></tr><tr><td>I</td><td>Act (r, v)</td><td>Responder acts in response</td><td>Each responder can act in multiple responses</td><td>Each response can be acted upon by multiple responders</td></tr><tr><td>J</td><td>Offer (g, s)</td><td>Agency offers resource</td><td>Each agency can offer multiple resources</td><td>Each resource can be offered by one agency</td></tr><tr><td>K</td><td>Restrict (v, d)</td><td>Response restricts aid</td><td>Each response can restrict multiple aids</td><td>Each aid is restricted by multiple responses</td></tr><tr><td>L</td><td>Follow (r, m)</td><td>Responder follows commander</td><td>Each responder can follow one commander</td><td>Each commander can be followed by multiple responders</td></tr><tr><td colspan="5"> $^\text{a}$ Terms in parentheses in Table 2 refer to elements from Table 1.</td></tr></table>

During an emergency event, the responder negotiates resources, roles and assistance when the resource is deployed in a different incident, or when the role requires specialized skills, or assistance necessitates custom resources, respectively. An agency negotiates for responders based on their availability (especially given that majority of the responders are volunteer workers). Resource and aid negotiations by an agency are based on the operating status of the resource, and the geographical proximity to event location. The incident commander negotiates for resources depending on their need or the shortage on the scene. Finally, the relief negotiations by the commander are centered around the incident category. Table 3 explains the emergency negotiations using an example scenario.

![](/api/attachments/YMBG9CM5/fulltext/images/c4ff22756b3f812a4d17357f3e6fceaa5a92e1131f27bc3ee90ea4fe23d7db90.jpg)

Figure 4. Activity Theory-Based Emergency Response Framework  
![](/api/attachments/YMBG9CM5/fulltext/images/27503bd69dcb66329dd4d6744d80fb9eba5caab120208b9d126ab426615d4476.jpg)  
Figure 5. Conceptual Modeling Grammar Element Taxonomy

## 5.3 State Transitions

Activity historicity: Activity systems and their elements have a history of their own, which implies that they develop over time or context. An analysis of historicity is needed to understand the activity in its entirety. Emergency structures are dynamic and have a life cycle associated with them. In order to interpret the dynamism within the emergency response tasks, it is important to consider various states that the tasks go through during the response. A simple view of emergency response life cycle could be studied though the process flows of the activity. In this process flow, both the elements and the tasks undergo frequent transitions.

The resource, responder, and agency elements go through four stages, namely dormant, dispatched, cold, and active as shown in Figure 7 below. The element is in a dormant state before it is dispatched for the incident. Once it is dispatched, it becomes available for use on-site and can be deployed. When it arrives on the scene, it can be in the cold state (i.e., not utilized) or in the active state. An element in cold state can transition to active state and vice-versa when it is assigned to or withdrawn from the activity (Valecha, Sharman, Rao, & Upadhyaya, 2012).

The tasks go through six stages—namely, dormant, queued, approved, active, suspended, and completed as shown in Figure 8 below. A dormant task is under consideration for approval. It can transition to a queued state if it is a lower priority. Once it is approved, it comes into action and can be implemented. During its execution phase, it is in the active state. An active task can be halted for any reason, transitioning it into the suspended state. A suspended task can be released to an active state, and, finally, to a completed state (Valecha et al., 2012).

While the structural elements of emergency response across various settings (counties, cities or states) are likely to be similar, it is quite possible that each setting would have some key distinguishing factors <sup>7</sup> . Therefore, it is important to point out that we do not think that a strict, one-to-one mapping exists. Our view on emergency activity is that different interpretations exist. For example, what is considered role information in one setting can be part of the division of labor in another setting. Likewise, the same piece of information can be part of different categories based on the activity. The same holds for the activity theorybased analysis itself: the same thing can be an object and a tool in different task settings. Activity theory allows the designer to focus on task-related information instead of being lost in the modeling of emergency details without being able to see the interactions between different aspects of the emergency system (Kofod-Petersen & Cassens, 2006). This allows the conceptual modeling grammar being developed to be extensible<sup>8</sup> in different contexts.

Table 3. Negotiation Formalization with Constraints<sup>a</sup>

<table><tr><td>Negotiation</td><td>Source</td><td>Target</td><td>Support</td><td>Scenario</td></tr><tr><td>N (r, s)</td><td>Responder</td><td>Resource</td><td>Multi-incident deployment</td><td>A fire engine needed in East Amherst is in-use by Main &amp; Transit site</td></tr><tr><td>N (r, m)</td><td>Responder</td><td>Commander</td><td>Role training</td><td>Responder presents chemical training for fire extinguishing</td></tr><tr><td>N (r, d)</td><td>Responder</td><td>Mutual aid</td><td>Custom tools</td><td>A rescue truck from third alarm is needed in a first alarm response</td></tr><tr><td>N (g, r)</td><td>Agency</td><td>Responder</td><td>Labor supply</td><td>Volunteer fire fighters are not available at a certain time</td></tr><tr><td>N (g, s)</td><td>Agency</td><td>Resource</td><td>Maintenance control</td><td>A 100-gallon water pumper needs its hose serviced</td></tr><tr><td>N (g, d)</td><td>Agency</td><td>Mutual Aid</td><td>Event proximity</td><td>A second alarm from Swornville updated due to road closures in the area</td></tr><tr><td>N (m, s)</td><td>Commander</td><td>Resource</td><td>Inventory levels</td><td>Unit 201 is released from the scene</td></tr><tr><td>N (m, d)</td><td>Commander</td><td>Mutual Aid</td><td>Incident category</td><td>Injuries on-site, mutual aid ambulance requested</td></tr><tr><td colspan="5"> $^{a}$ Terms in parentheses in Table 3 refer to elements from Table 1.</td></tr></table>

![](/api/attachments/YMBG9CM5/fulltext/images/c271e571ce47dc4dc113ae20d16c7801a3f6ed0e349321bf3c14a0913106708c.jpg)  
Figure 6. Activity Theory-Based Formulation of Emergency Negotiations

![](/api/attachments/YMBG9CM5/fulltext/images/d8edce7e2f5b4494abefd12c950c7ab12ee3f230e837fa0c804b37e110df0572.jpg)  
Figure 7. Conceptual Modeling Grammar Element Transitions

![](/api/attachments/YMBG9CM5/fulltext/images/694b6d1c4c005fd710b7b58c678eec108feb7ca13ab45c624576d49a482b14a6.jpg)  
Figure 8. Conceptual Modeling Grammar Activity Transitions

## 6 Evaluation

Some researchers have evaluated conceptual modeling grammar by comparing the similarities and differences with competing grammars (e.g., Henk, Olle, & Verrijn-Stuart, 1986; Zhang et al., 2007). For evaluation of their grammars, these researchers have considered characteristics such as number of constructs, reactiveness and proactiveness, and social behavior.

Connolly and Begg (2002) provide useful guidance on validating conceptual models effectively and efficiently. They recommend that conceptual models be validated using two validation tasks—test transactions against the conceptual model, and review the conceptual model with users. Transaction testing includes events in the domain, referred to as transactions, which can be evaluated to determine whether they are represented in the conceptual model. Participant review involves participants who are asked to review the model in whatever way they choose. Following their recommendation, we validate the conceptual model in two ways: transaction testing using an emergency case, and participant review of how the conceptual model represents the domain.

In using transaction testing and participant review for validating conceptual modeling grammar, we chose two criteria: (1) minimum overlap is achieved when the same construct cannot be represented via alternate constructs, and (2) maximum coverage is achieved if the constructs in combination cover all phenomena to be modeled. Minimum overlap reduces the likelihood of producing conflicting domain representations, while maximum coverage increases the likelihood of producing complete domain representations (Wand & Weber, 2002).

## 6.1 Case Evaluation

The conceptual modeling grammar can be evaluated based on its usage and application (Chen et al., 2013). In accordance, we utilize a real case (incident report) in order to determine how well the grammar fits a real scenario. For the real case, we chose an additional incident that was not used in the grammar development process (see excerpt in Figure 9). This incident reports on various emergency tasks that were performed during the mitigation of the emergency. The incident pertains to a brew pub fire that was reported by alarms and spread quickly through multiple areas. The total damage caused by the fire was estimated to be over \$200,000.

Validating a conceptual model involves checking its representativeness—namely, how closely the conceptual model represents the domain. It is representative if it has the attributes of accuracy and completeness; in other words, the model should represent the domain accurately and completely. Thus, we asked a key validation question to four different emergency dispatch responders (each with more than five years of experience) who were not involved in the process of grammar development: Does the conceptual model allow for a complete representation of the emergency tasks (maximum coverage)? Does the conceptual model allow for an accurate representation of the emergency tasks (minimum overlap)? These questions served the purpose of validating the conceptual modeling grammar and illuminated the transition of activity theory concepts from conceptual to modeling form, which is detailed next.

In order to answer these questions, the authors provided sample raw data (tasks) from the incident report to the four experts in group meetings (see Figure 9). The authors also provided the key elements and their relationships derived by using the conceptual modeling grammar. For example, see Sample Tasks $1 - \mathrm { ^ { 6 6 } D ^ { 9 } }$ and Task 2—“Channel 2” in Figure 9. In the first task, the authors revealed that the aid is dispatched (denoted by “D”) to the incident, the agency is the dispatch agency, the type of mutual aid is fire-related (MAF), the command is under the control of fire chief, and the response (motivation) is fire suppression. In the second task, the authors identified that the radio (channel 2) was used for communication purposes. Thus, the resource is the radio (channel 2), the agency is the dispatch agency, and the response (motivation) is communication. This is depicted as Tasks 1 and 2 in Table 4. Furthermore, the authors also identified the relationship between the elements. In the first task, the authors recognized that TOM belongs to the dispatch agency that responded to the on-site location. In the second task, the authors identified that the dispatch agency provided the radio channel that is deployed for on-site communication. This is summarized in Table 5. For the details of other elements within the sample messages provided in the real case, refer to Table A1 in Appendix A.1.

The four experts reviewed the tasks from the incident report by comparing the raw information with the structured information derived by the authors (using the grammar). They were allowed to ask (and discuss with) one another about the domain being modeled during the group meetings. They endorsed that tasks within the report were completely represented by the elements and relationships (in both Table 4 and Table A1). In addition, they also identified that the concepts were extracted accurately. Thus, the model offers a significant improvement over the current form of the logging tasks. The experts concurred that the conceptual modeling grammar may be used to improve the exchange of task-critical information.

```txt
Dispatched 04:56:16
Enroute 04:56:16
At Scene 05:01:18
Transport
At Hospital
Available 05:27:23

Vehicle: ID Number S91 SNYDER 1ST ASST CHIEF
Dispatched 04:56:16
Enroute 04:56:16
At Scene 05:01:18
Transport
At Hospital
Available 05:27:23

Dispatchers Comments
RICKB 04:42:18 Received: 05/01/10 04:40:55 Phone:
RICKB 04:42:18 Caller: CENTRAL STATION
RICKB 04:42:18 City/St: Type MF
RICKB 04:42:17 BFLO BREW PUB / SOME TYPE OF FIRE
TOM 04:42:34 BFLO BREW PUB /SOME TYPE OF FIRE
TOM 04:42:41 D
TOM 04:47:57 POSSIBLY DUMPSTER EXTENDING INTO BUILDING
RICKB 04:49:43 244 FROM MAPLE TRANSIT
TOM 04:50:14 CHANNEL 2
RICKB 04:52:31 ALPHA PAGE AFI / AES GROUPS
TOM 04:55:03 NFG NOTIFIED
TOM 04:56:37 NATL GRID NOTIFIED
TOM 04:58:15 BULK OF FIRE KNOCKED DOWN, CHECKING FOR EXTENSION
RICKB 04:58:52 AFI-1 RESP
RICKB 05:04:20 15 MIN ETA / NAT GRID
TOM 05:26:07 KNOCKING DOWN HOT SPOTS
TOM 05:26:21 PICKING UP FAST
RICKB 05:34:16 APD FIRE INVESTIGATORS RESP
TOM 06:54:27 $150000 TO BLDG
TOM 06:54:34 $50000 TO CONTENTS
TOM 06:54:43 UNDER INVESTIGATION'
Incident Comments
ALARM COMPANY REPORTED A FIRE ALARM ACTIVATION. AT THE SAME TIME, APD REPORTED
```  
Figure 9. Dispatch Incident Report Excerpt (Sample Tasks in Red Box)

Besides the participants who are aware of the domain of the conceptual model, there may be IS professionals (having had no part in the preparation of a conceptual model) who can validate the conceptual model (Shanks, Tansley, Weber, 2003). In accordance, we validate the conceptual model through a testing team of professionals (who were not involved in the model development).

## 6.2 Prototype System Test

In order to enable the validation of the conceptual model by a testing team of professionals without the knowledge of the domain, we built a prototype system using Visual Basic to facilitate support for fire incident response. This prototype utilized the grammar to standardize sharing of task-critical information in the emergency context. It enabled first responders to enter pertinent information dealing with situation assessment, resource application, collaboration, and so forth.

A team of two software developers (graduate students) led by the first author developed the prototype, which was tested by a team of two testers (also graduate students). We provided both teams with the requirements for the design of the system based on the aforementioned emergency framework. Previously, all four graduate students had worked on software development in industry contexts. The prototype followed the standard software development life cycle (SDLC) methodology and took four months to complete.

Table 4. Key Elements from Emergency Tasks

<table><tr><td>Task</td><td>Responder</td><td>Resource</td><td>Agency</td><td>Response</td><td>Aid</td><td>Commander</td></tr><tr><td>1</td><td>TOM</td><td>-</td><td>Dispatch</td><td>Suppression</td><td>MAF</td><td>Chief</td></tr><tr><td>2</td><td>TOM</td><td>Radio (Channel 2)</td><td>Dispatch</td><td>Communication</td><td>-</td><td>-</td></tr></table>

Table 5. Key Relationships from Emergency Tasks

<table><tr><td>Task</td><td>Element</td><td>Element</td><td>Relation</td></tr><tr><td>1</td><td>Tom</td><td>Dispatch</td><td>Belong</td></tr><tr><td>1</td><td>Tom</td><td>Chief</td><td>Follow</td></tr><tr><td>2</td><td>Dispatch</td><td>Communication</td><td>Provide</td></tr><tr><td>2</td><td>Dispatch</td><td>Channel 2</td><td>Offer</td></tr></table>

As a prototype, this system developed only a portion of the functionalities required by the actual fire response system. The prototype system contained four modules including logging, reporting, modularizing and exporting. There were a total of 49 forms generated over 11 database tables to store relevant element and relationship information. Figure 10 provides a snapshot of the prototype<sup>9</sup>.

We tested the prototype for functionality utilizing the key elements—responder and resource, and their relationships. The prototype demonstrates how the subject and tool were instantiated, along with a goal (activity) assignment scenario where the responder used the resource assigned to a certain activity. For example, firefighter used water pump assigned for extinguishing the fire (as shown in Figure 10). The testing team performed various types of tests<sup>10</sup>, such as unit, database, regression, integration, and system tests, based on the specified design requirements.

The testing team concluded that the responder and resource modules worked independently. There was no overlap between the constructs, confirming the minimum overlap criteria. The assignment module populated the relationship data correctly. It was also determined that the element module and the relationship module completely and accurately modeled the scenario at hand, and that the system performed as expected for the information logging requirement. This confirmed the maximum coverage criteria setup at the beginning of testing phase.

## 7 Conclusion

Emergency response is dispatch-mediated process, and a complex operation consisting of several “communities of responders”, which facilitate sharing domain expertise and improve the capacity to respond to emergencies over time.

Utilizing emergency dispatch incident reports, we develop a framework for sharing task-critical information. Such a framework can be useful in developing a tool to help communities of responders share their expertise. The paper contributes to research in dispatch-mediated emergency response literature by (1) developing a framework of elements and relationships within the emergency communities of responders; (2) developing a conceptual modeling grammar based on activity theory and grounded in an analysis of more than 1000 emergency dispatch incident reports; and (3) implementing a prototype system to demonstrate the utility of the conceptual modeling grammar.

![](/api/attachments/YMBG9CM5/fulltext/images/0e80611ed3179cff34511f6c2e4f073c70fe6bb10275889cc0538ba369381c91.jpg)  
Figure 10. Snapshot of Prototype System

The grammar is grounded in activity theory to elicit development of its elements and relationships. This paper adheres to the design science research guidelines (Hevner et al. 2004; Peffers et al. 2006), and makes the following contributions to the literature: (1) it undertakes empirical work on conceptual modeling grammar in a realistic setting; and (2) it studies the conceptual-modeling needs of complex domains, involving multiple response organizations. Such a conceptual modeling grammar can be used to model real-world complex domains (Wand & Weber, 2002), aid solution development by specifying a common vocabulary, and help personnel share vital task-critical data while responding to day-to-day emergency incidents. Furthermore, the grammar can provide the foundations needed to define a modeling language in the form of symbols and vocabulary capable of serving as building blocks for constructing more complicated expressions.

One limitation of our work is that it is based on emergency dispatch incident reports from selected counties in northeastern United States. Practices in other parts of the country may vary somewhat. Future studies should aim to generalize the model developed in this article. Another limitation of the current system is that repeated task-critical updates were not logged. It may be noted that a unidirectional update may be multicast to several responding agencies to ascertain which agency has the resources to respond. In addition, a mechanism for dealing with missed information in the system needs to be addressed in future research. Resource interdependencies—which arise when two or more responders require access to the same resource— need to be handled effectively. There should be a way of defining the order in which agents access the resource and its locking mechanism. Richer data could, perhaps, be utilized to arrive at patterns leading to more predictive analysis, and an early detection of the aborted 911 calls and prank calls. We hope that the conceptual modeling grammar developed in this paper will be subjected to more rigorous evaluation focusing on how the grammar helps in resource assignment, responder accountability, and other emergency operations that are a part of the day-to-day emergency response.

## Acknowledgements

The authors would like to thank the editors and referees for their critical comments that have greatly improved the article. The authors would also like to thank all the emergency response experts for their great help in this research project. This research was funded by the NSF under grant # 1241709 awarded to Drs. Upadhyaya and Rao. Dr. Valecha was also funded in part under NSF grant # 1651475, and Dr. Rao was funded in part by NSF grant # 1724725. Dr. Sharman was supported in part by a generous financial grant from the School of Management at the University at Buffalo. Any opinions, findings, and conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the National Science Foundation. Professor H. R. Rao is the corresponding author for this paper.

## References

Aedo, I., Díaz, P., Carroll, J. M., Convertino, G., & Rosson, M. B. (2010). End-user oriented strategies to facilitate multi-organizational adoption of emergency management information systems. Information Processing & Management, 46(1), 11-21.

Al-Safadi, L. A. (2009). Natural language processing for conceptual modeling. International Journal of Digital Content Technology and its Applications, 3(3), 47-59.

Allen, D. K., Brown, A., Karanasios, S., & Norman, A. (2013). How should technology-mediated organizational change be explained? A comparison of the contributions of critical realism and activity theory. MIS Quarterly, 37(3), 835-854.

Allen, D., Karanasios, S., & Slavova, M. (2011). Working with activity theory: Context, technology, and information behavior. Journal of the American Society for Information Science and Technology, 62(4), 776-788.

Barab, S. A., & Plucker, J. A. (2002). Smart people or smart contexts? Cognition, ability, and talent development in an age of situated approaches to knowing and learning. Educational psychologist, 37(3), 165-182.

Barker, R. (1990). CASE method: Tasks and deliverables. Boston, MA: Addison-Wesley.

Barley, S. R. (1990). Images of imaging: Notes on doing longitudinal field work. Organization Science, 1(3), 220-247.

Bertelsen, O., & Bodker, S. (2003). Activity theory. In J. M. Carroll (Ed.), HCI Models, Theories and Frameworks: Towards a Multidisciplinary Science. San Francisco, CA: Mogan Kaufmann: 291-324

Burg, J. F. M., & van de Riet, R. P. (1997). The impact of linguistics on conceptual models: Consistency and understandability. Data & Knowledge Engineering, 21(2), 131-146.

Chaudhury, A., Mallick, D., & Rao, H. R. (2001). Web channels in e-commerce. Communications of the ACM, 44(1), 99-104.

Chen, P. (1983). English sentence structure and entityrelationship diagrams. Information Sciences, 29(2), 127-149.

Chen, P. (2002). Entity-relationship modeling: historical events, future trends, and lessons learned. In M. Broy & E. Denert (Eds.)

Software pioneers (pp. 296-310). Berlin: Springer.

Chen, R., Sharman, R., Chakravarti, N., Rao, H.R., & Upadhyaya, S. (2008). Emergency response information system interoperability: Development of chemical incident response data model. Journal of the Association for Information Systems, 9(3-4), 200-230.

Chen, R., Sharman, R., Rao, H. R., & Upadhyaya, S. (2013). Data model development for fire related extreme events: An activity theory approach. MIS Quarterly, 37(1), 125-147.

Clemmensen, T., Kaptelinin, V., & Nardi, B. (2016). Making HCI theory work: An analysis of the use of activity theory in HCI research. Behaviour & Information Technology, 35(8), 608-627.

Cole, M., & Engeström, Y. (1993). A culturalhistorical approach to distributed cognition. Distributed cognitions: In G. Salomon (Ed.), Psychological and educational considerations, 1-46. Cambridge, U.K.: Cambridge University Press.

Connolly, T. & Begg, C. (2002). Database systems: A practical approach to design, implementation, and management (3rd ed.) Harlow, U.K.: Addison-Wesley.

DHS. (2004). National incident management system. Department of Homeland Security. Retrieved from http://www.fema.gov/emergency/nims.

DHS. (2006). The system of systems approach for interoperable communications. Department of Homeland Security. Retrieved from file:///C:/Users/monica/Downloads/16417%20 (2).pdf

DHS. (2007). Homeland security grant program. Department of Homeland Security https://www.dhs.gov/xlibrary/assets/grantprogram-overview-fy2010.pdf

Engeström, Y. (1987). Learning by expanding: An activity-theoretical approach to developmental research. Helsinki: Orienta-Konsultit.

Engeström, Y. (1995). Objects, contradictions and collaboration in medical cognition: an activitytheoretical perspective. Artificial intelligence in medicine, 7(5), 395-412.

Engeström, Y. (1999). Activity theory and individual and social transformation. In Y. Engeström (Ed.), Perspectives on Activity Theory (pp. 19- 38). Cambridge, U.K.: Cambridge University Press.

Fisher, L., & Bennion, L. (2005). Organizational implications of the future development of technical communication: Fostering communities of practice in the workplace. Technical communication, 52(3), 277-288.

Gregor, S., & Hevner, A. R. (2013). Positioning and presenting design science research for maximum impact. MIS Quarterly, 37(2), 337- 355.

Henk, G., Olle, T. W., & Verrijn-Stuart, A. A. (Eds.). (1986). Information systems design methodologies: Improving the practice. Amsterdam: Elsevier.

Hevner, A.R., March, S.T., Park, J., & Ram, S. (2004). Design science in information systems research. MIS Quarterly, 28(1), 75-105.

Igira, F.T. (2008). The situatedness of work practices and organizational culture: Implications for information systems innovation uptake. Journal of Information Technology, 23(2), 79- 88.

Kaptelinin, V., Kuutti, K., & Bannon, L. (1995). Activity theory: Basic concepts and applications. In Human-computer interaction: Proceedings of the 5<sup>th</sup> International EWHCI Conference (pp. 189-201). Berlin: Springer.

Kaptelinin, V., & Nardi, B. A. (2006). Acting with technology: Activity theory and interaction design. Cambridge, MA: Massachusetts Institute of Technology Press.

Kaptelinin, V., Nardi, B. A., & Macaulay, C. (1999). Methods and tools: The activity checklist: a tool for representing the “space” of context. Interactions, 6(4), 27-39.

Karanasios, S., Thakker, D., Lau, L., Allen, D., Dimitrova, V., & Norman, A. (2013). Making sense of digital traces: An activity theory driven ontological approach. Journal of the American Society for Information Science and Technology, 64(12), 2452-2467.

Kishore, R., & Sharman, R. (2004). Computational ontologies and information systems I: foundations. Communications of the Association for Information Systems, 14(1), 8.

Kishore, R., Zhang, H., & Ramesh, R. (2006). Enterprise integration using the agent paradigm: foundations of multiagent-based integrative business information systems. Decision Support Systems, 42(1), 48-78

Kofod-Petersen, A., & Cassens, J. (2006). Using activity theory to model context awareness. In R. C. Roth-Berghofer, S. Schulz, & D. Leake

(Eds.), Modeling and Retrieval of Context (pp. 1-17). Berlin: Springer.

Korpela, M., Soriyan, H.A. & Olufokunbi, K.C. (2001) Activity analysis as a method for information systems development. Scandinavian Journal of Information Systems, 12(1-2), 191-210.

Kuhn, W. (2001). Ontologies in support of activities in geographical space. International Journal of Geographical Information Science, 15(7), 613- 631.

Kuutti, K. (1996). Activity theory as a potential framework for human-computer interaction research. In B. A. Nardi (Ed.), Context and Consciousness: Activity Theory and Human-Computer Interaction (p. 17-44). Cambridge, MA: Massachusetts Institute of Technology Press.

Mwanza, D. (2001). Where theory meets practice: A case for an activity theory based methodology to guide computer system design. In Proceedings of INTERACT’ 2001: Eighth IFIP TC 13 Conference on Human-Computer Interaction.

Nardi, B. (1995). Activity theory and human-computer interaction, In B. A. Nardi (Ed.), Context and Consciousness: Activity Theory and Human-Computer Interaction (p. 7-16). Cambridge, MA: Massachusetts Institute of Technology Press..

Nicolini, D. (2013) Practice theory, work, and organization: An introduction. Oxford, U.K.: Oxford University Press.

Niederman, F., & March, S. T. (2012). Design science and the accumulation of knowledge in the information systems discipline. ACM Transactions on MIS, 3(1), Article 1.

O'Leary, D. E. (2010). Enterprise ontologies: Review and an activity theory approach. International Journal of Accounting Information Systems, 11(4), 336-352.

Overmyer, S. P., Lavoie, B., & Rambow, O. (2001). Conceptual modeling through linguistic analysis using LIDA. In Proceedings of the 23rd International Conference on Software Engineering (pp. 401-410).

Peffers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. (2007). A design science research methodology for information systems research. Journal of Management Information Systems, 24(3), 45-77.

Purao, S., Baldwin, C. Y., Hevner, A., Storey, V. C., Pries-Heje, J., Smith, B. and Zhu, Y. (2008). The sciences of design: Observations on an

emerging field. Communications of the Association for Information Systems, 23, Article 29.

Purao, S. & Woo, C. (2014). Conceptual modeling: Going beyond the stigma of YAMA. In Proceedings of SIGSAND.

Raghu, T. S., Jayaraman, B., & Rao, H. R. (2004). Toward an integration of agent-and activitycentric approaches in organizational process modeling: Incorporating incentive mechanisms. Information Systems Research, 15(4), 316-335.

Rao, H. R., Chaudhury, A., & Chakka, M. (1995). Modeling team processes: Issues and a specific example. Information Systems Research, 6(3), 255-285.

Shankar, D., Agrawal, M., & Rao, H.R. (2009). Emergency response of Mumbai terror attacks: An activity theory analysis, In Proceedings of ICSCF 09.

Shanks, G., Tansley, E., & Weber, R. (2003). Using ontology to validate conceptual models. Communications of the ACM, 46(10), 85-89.

Sowa, J. (1999). Ontology, knowledge representation: Logical, philosophical, and computational foundations (pp. 51-131). New York, NY: Brooks/Cole.

Valecha, R. (2019). An investigation of interaction patterns in emergency management: A case study of the crash of continental flight 3407. Information Systems Frontiers, forthcoming.

Valecha, R. (2015). Information & communication in “mediated” crisis response. (Unpublished doctoral dissertation). State University of New York at Buffalo, Buffalo, NY.

Valecha, R., Kashyap, M., Rajeev, S., Rao, H. R., & Upadhyaya, S. (2014). An activity theory approach to specification of access control policies in transitive health workflows. In Proceedings of International Conference on Information Systems.

Valecha, R., Sharman, R., Rao, H. R., & Upadhyaya, S. (2013). A dispatch-mediated communication model for emergency response systems. ACM Transactions on MIS, 4(1), Article 2.

Valecha, R., Sharman, R., Rao, H. R., & Upadhyaya, S. (2012). Design principles for emergency collaborative systems: A situation awareness study of Buffalo plane crash. In Proceedings of American Conference on Information Systems.

Valecha, R., Sharman, R., Rao, H. R., & Upadhyaya, S. (2012). Emergency response system design: An examination of emergency communication messages. In Proceedings of Design Science Research on Information Systems and Technology.

Valecha, R., Sharman, R., Rao, H. R., & Upadhyaya, S. (2012). Messaging model for emergency communication. In Proceedings of the Mid-West Association of Information Systems.

Valecha, R., Sudumbrekar, K., & Sharman, R. (2012). Grammar for agent-based emergency response systems. In Proceedings of the Workshop on E-Business.

Wand, Y., Monarchi, D. E., Parsons, J., & Woo, C. C. (1995). Theoretical foundations for conceptual modelling in information systems development. Decision Support Systems, 15(4), 285-304.

Wand, Y., & Weber, R. (1995). On the deep structure of information systems. Information Systems Journal, 5(3), 203-223.

Wand, Y. & Weber, R. (2002). Research commentary: information systems and conceptual modeling - a research agenda. Information Systems Research, 13(4), 363-376.

Wells, G. (2002). The role of dialogue in activity theory. Mind, Culture, and Activity, 9(1), 43-46.

Zhang, H., Kishore, R., Sharman, R., & Ramesh, R. (2007). Agile integration modeling language (AIML): A conceptual modeling grammar for agile integrative business information systems. Decision Support Systems, 44(1), 266-284.

## Appendix A

A.1 Case Details

Table A1. Key Elements from Sample Messages in Fire Case Study

<table><tr><td>Msg.</td><td>Responder</td><td>Resource</td><td>Agency</td><td>Response</td><td>Aid</td><td>Command</td></tr><tr><td>1</td><td>Caller</td><td>-</td><td>Public</td><td>Initial notification</td><td>-</td><td>-</td></tr><tr><td>2</td><td>RICKB</td><td>-</td><td>-</td><td>Fire update</td><td>-</td><td>-</td></tr><tr><td>3</td><td>TOM</td><td>-</td><td>-</td><td>Fire update</td><td>-</td><td>-</td></tr><tr><td>4</td><td>TOM</td><td>Aid</td><td>Dispatch</td><td>Suppression</td><td>MAF Dispatched</td><td>Chief</td></tr><tr><td>5</td><td>TOM</td><td>-</td><td>-</td><td>Fire update</td><td>-</td><td>-</td></tr><tr><td>6</td><td>RICKB</td><td>Ambulance (Unit 244)</td><td>EMS</td><td>Medical care</td><td>-</td><td>-</td></tr><tr><td>7</td><td>TOM</td><td>Radio (Channel 2)</td><td>Dispatch</td><td>Communication</td><td>-</td><td>-</td></tr><tr><td>8</td><td>RICKB</td><td>Pager</td><td>AFI, AES</td><td>Alert</td><td>-</td><td>-</td></tr><tr><td>9</td><td>TOM</td><td>-</td><td>NFG</td><td>Alert</td><td>-</td><td>-</td></tr><tr><td>10</td><td>TOM</td><td>-</td><td>NG</td><td>Alert</td><td>-</td><td>-</td></tr><tr><td>11</td><td>TOM</td><td>-</td><td>-</td><td>Fire update</td><td>-</td><td>-</td></tr><tr><td>12</td><td>RICKB</td><td>-</td><td>Status (Responding)</td><td>Status update</td><td>-</td><td>-</td></tr><tr><td>13</td><td>RICKB</td><td>-</td><td>Status (ETA)</td><td>Status update</td><td>-</td><td>-</td></tr><tr><td>14</td><td>TOM</td><td>-</td><td>-</td><td>Fire update</td><td>-</td><td>-</td></tr><tr><td>15</td><td>TOM</td><td>-</td><td>FAST</td><td>Alert</td><td>-</td><td>-</td></tr><tr><td>16</td><td>RICKB</td><td>-</td><td>APD, FI</td><td>Alert</td><td>-</td><td>-</td></tr><tr><td>17</td><td>TOM</td><td>-</td><td>-</td><td>Location update</td><td>-</td><td>-</td></tr><tr><td>18</td><td>TOM</td><td>-</td><td>-</td><td>Content update</td><td>-</td><td>-</td></tr><tr><td>19</td><td>TOM</td><td>-</td><td>-</td><td>Incident update</td><td>-</td><td>-</td></tr></table>

## A.2 System Design

The database diagram in Figure A1 explains the back-end functionality related to the key elements and their relationships. It depicts the role-centric view wherein each role can be played by multiple agents, assigned multiple goals, and allocated multiple resources. The use-case diagram in Figure A1 also depicts the cases for the user groups that the system serves.

![](/api/attachments/YMBG9CM5/fulltext/images/d83a93fb00f9d61830ba7a82fc1716ffd6cae8c6242efedbaee57f4976a5c04b.jpg)  
Figure A1. System Database Diagram and Use-Case Diagram

## A.3 System Testing

The prototype was developed by a team of two software developers (currently graduate students) led by the first author and another testing team of two developers (also currently graduate students). We provided both teams with the requirements for the design of the system based on the aforementioned communication framework. We evaluated the prototype system to assess its quality and level of support in fire response, and the evaluation results are presented in Table A2.

Table A2. Prototype Evaluation Results

<table><tr><td>Test</td><td>Result</td></tr><tr><td>Unit testing</td><td>Description: This test is performed at the functional level and ensures that the specific function is working as expected.Relevance: This test was performed to ensure that different modules, which form the building blocks of the software, work independently of each other.Details: Responder and resource modules worked independently.</td></tr><tr><td>Database testing</td><td>Description: This test ensures the interaction of the system with the data.Relevance: This was performed by verifying data entered through the forms, populated the database at the back end.Details: Resource assignment form populated the assignment data table.</td></tr><tr><td>Regression testing</td><td>Description: This test ensures that the newer functionality does not affect the previously working functionalities.Relevance: This was performed by checking whether previously fixed faults have reemerged.Details: The assignment module does not affect responder module.</td></tr><tr><td>Integration testing</td><td>Description: This test ensures that the different modules interact as expected when integrated.Relevance: The interaction between the modules was reported for bug fixes.Details: The element module interacted with the relationship module.</td></tr><tr><td>System testing</td><td>Description: This test ensures that the entire system meets the requirements.Relevance: Any of the reported errors were fixed and the new version of the system was retested.Details: The system performed as expected for info logging requirement.</td></tr></table>

## About the Authors

Rohit Valecha is an assistant professor in the Department of Information Systems and Cyber Security at The University of Texas at San Antonio. He received his PhD from the University at Buffalo. His current research interests are in crisis response, social media, and system design. He also specializes in methodologies using natural language processing, text mining, social network analysis and machine learning. He has published in the ACM Transactions on Information Systems, Journal of the Association for Information Systems, and Information Systems Frontiers (ISF) and his work has been featured in the Networking and Information Technology Research and Development Program. He is also a recipient of the NSF EAGER and RAPID grants.

H. Raghav Rao has been the AT&T Distinguished Chair in Infrastructure Assurance and Security at the University of Texas at San Antonio College of Business since January 2016. He also holds a courtesy appointment as full professor in the UTSA Department of Computer Science. Prior to working at UTSA, Professor Rao was the SUNY Distinguished Service Professor at the University at Buffalo. He graduated from Krannert Graduate School of Management at Purdue University. His interests are in the areas of management information systems, decision support systems, e-business, emergency response management systems, and information assurance. He has chaired sessions at international conferences and presented numerous papers. He also has coedited four books, including Information Assurance Security and Privacy Services and Information Assurance in Financial Services. He has authored or coauthored more than 200 technical papers, of which more than 125 are published in archival journals. He has received funding for his research from the National Science Foundation, the Department of Defense, and the Canadian Embassy. He also received a Fulbright fellowship in 2004.

Shambhu J. Upadhyaya is a Professor of Computer Science and Engineering at the University at Buffalo, SUNY, where he also directs the Center of Excellence in Information Systems Assurance Research and Education, designated by the National Security Agency. Prior to July 1998, he was a faculty member in the Electrical and Computer Engineering department. His research interests are in broad areas of information assurance, computer security and fault tolerant computing. He has authored or coauthored more than 280 articles published in refereed journals and presented at conferences in these areas. His research has been supported by the National Science Foundation, the U.S. Air Force Research Laboratory, the U.S. Air Force Office of Scientific Research, DARPA, and National Security Agency. He is a senior member of the IEEE.

Raj Sharman is a professor in the Management Science and Systems Department at the University at Buffalo. He has served as the director of the Master’s degree program in Management Information Systems (MIS) and as the Ph.D. faculty adviser for the Department of Management Science and Systems at the University at Buffalo. He has devoted his time to mentoring many diverse and aspiring students at the university. He received his doctoral degree in Computer Science and a Master of Science degree in Industrial Engineering from Louisiana State University. He also earned a Bachelor’s degree in Engineering and a Master’s degree in Industrial Management from the Indian Institute of Technology, Bombay, India. His interests are in the areas of Artificial Intelligence, Disaster Response Management, Information Assurance, and Health Information Technology. He has published widely in scholarly journals and is the recipient of numerous grants from the university and external agencies, including the National Science Foundation.
