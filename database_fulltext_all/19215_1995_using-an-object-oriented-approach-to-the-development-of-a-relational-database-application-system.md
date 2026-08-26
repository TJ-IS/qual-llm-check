---
otero_id: 19215
otero_key: "3GZ4BRBY"
title: "Using an object-oriented approach to the development of a relational database application system"
authors: "Pi-Sheng Deng; Cynthia L. Fuhr"
year: "1995"
journal: "Information & Management"
doi: "10.1016/0378-7206(95)00020-w"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Techniques

# Using an object-oriented approach to the development of a relational database application system

Pi-Sheng Deng $^{a,*}$ , Cynthia L. Fuhr $^{b}$

$^{a}$ Department of Computer Information Systems, School of Business Administration, California State University at Stanislaus, Turlock, CA 95380, USA

$^{b}$ Department of Information Systems, Yosemite Community College District, Modesto, CA 95352, USA

## Abstract

Object-oriented technology has been proposed in recent years as a promising approach to increasing programmer productivity and the quality of software development. The traditional development of a database application system distinctively separates a system's behavior and its data by using entity-relationship diagrams, functional decomposition, and process-dependency diagrams. The object-oriented approach, on the other hand, integrates both data and behavior, and this can result in a merging of both software and databases. To gain more insight into the object-oriented approach to the analysis and design of software development, we applied this approach to the development of a simplified hospital administration system. The resulting application system is an object-based system but uses a relational database manager. This illustrates the fact that object-oriented approaches are not limited to object-oriented systems or databases: they can, in fact, be used for more traditional design. This technique may allow easier transition from data-based to object-based systems. Software that is reusable, improved in its design, more reliable, and simpler in its programming and maintenance requirements would truly be an advantage to users and developers alike.

Keywords: Classes; Messages; Objects; Object-based database systems; Object-oriented analysis and design; Object-oriented technology; Signatures

## 1. Introduction

Computer industry analysts have been stating for many years that we have a “software crisis.” As computers are becoming faster, cheaper, and more powerful, software development has become more costly and time-consuming. In fact, studies have shown that up to 95% of all software development projects are never completed without some major reconstruction or redesign.

The problem lies in the approach to software development. Traditional structured analysis and design techniques leading towards modular top-down programming is very time-consuming and often cannot allow even simple modifications to a module without a complete redesign of the system. Although CASE tools were once acclaimed to solve the software problem by automatically generating programs, they still require a lengthy design process and are relatively fragile in use.

One approach that is growing in popularity and which may solve this problem is object-oriented programming (OOP) [10,17]. The premise of objectorientation is that it can model the real world. Programmers can organize entities through objects using encapsulation, classification and messaging. This allows end users to access a more user-friendly system with graphical user interfaces and more understandable designs. Other advantages are:

1. Reusability. Classes can be put into libraries and parts reused later in other systems.

2. Productivity. It is “natural” to solve problems in object form rather than in low-level detail. Complex objects can be built simpler, in building blocks consisting of simple objects. Also, the design phase could be made faster by using ready-made classes and case tools. Changes are easier.

3. Reliability. One class used in several areas is likely to reduce the total number of bugs.

4. Easier programming and maintenance. Coding is at a high-level, using a building blocks method. Classes are independent of each other and changes do not upset other independent objects.

5. Communications. The object-orientation way of thinking promotes better communications between business people and their Information Systems staff.

The application developer should have an easier job as well. An increase in productivity will result when code can be reused, because models of the real world will not have to be “reinvented” for each project $[1]$ . Programming should be at a higher level (building blocks method) and easier to accomplish $[7]$ . Changes can be made in the implementation cycle so that most of the earlier design can be retained.

Object-orientation is not a new concept. Object-oriented programming began in the 1960's with the SIMULA language, followed by SMALLTALK, and hybrid languages, such as $C^{++}$ and ADA. Since then, analysis and design methods have been developed to aid the modeling of data-oriented systems. There are over 100 object-based and object-oriented languages available today [3].

An object-based language directly supports data abstraction and classes, while an object-oriented language is object-based and supports inheritance. Pure languages have been built to be object-oriented and only accept objects, methods, and classes. Hybrid languages are non-object-oriented, accepting other data types than objects, but also allowing objects, classes, and methods. A disadvantage to this type of language is that it tends to lead the programmer back to a traditional approach [5].

In terms of database technology, there seems to be an on-going controversy over object-oriented versus relational approaches $[2,9,11,16]$ . One solution has been to merge the technologies, allowing object-based routines in SQL databases $[13]$ .

In order to gain more insight into the object-oriented technology, we apply the approach to the analysis and design of a relational database application system. MicroSoft's Visual Basic 3.0 standard edition was used in implementing the research.

## 2. Principles of object-oriented technology

The object-oriented approach to information system development is built upon three basic ideas: objects, messages, and classes. An object is a software entity with behavior (or a collection of procedures) and data. It is autonomous, in the sense that it can satisfy requests sent from other objects without a need for any external step-by-step instruction. This is attained through the set of procedures (called methods) embedded in the object. Such self-sufficiency renders objects ideal software modules, and their maintenance can be accomplished independently.

Objects communicate by sending messages, and objects respond by carrying out their own methods. A message for an object mainly consists of the name of the object and the name of a method that the object can execute. Message passing is the necessary means to activate objects, and objects respond only to messages.

Since objects communicate through message passing, an object cannot directly access another object's variables. This provides a form of encapsulation, protecting an object's variables from being corrupted by other objects; this also simplifies the interactions between objects. In addition, the same message can be used to obtain different results by sending it to different objects. This hiding alternative procedures behind a common interface is called polymorphism. One of its key benefits is that it helps keep the number of names for different tasks or operations to a minimum. This also simplifies the programming process and improves the readability of the program. As a consequence, modification and maintenance are also simplified.

The object oriented approach uses the concept of classes: similar objects are grouped together. The objects belonging to the same class are called instances of that class. A class serves as a template (or definition) for the common methods and variables shared by its objects; the actual values for the variables or the parameters used in the methods are contained in the object instance.

Actually, a class is a generalization of its objects. Thus, classes can be grouped into superclasses to form different levels of generalization. In this class hierarchy, a lower level class can inherit methods and variables from its superclass, but still establishes its own special characteristics by adding to the inherited behavior. When an object receives a message to carry out a method that has not been defined in its class, the object searches up its class hierarchy until it finds the definition of that method and then applies it to its own local data values.

Another characteristic of the class hierarchy is its ability to accommodate exceptions. In the class hierarchy, exceptions defined at a lower level always override the more general methods defined at a higher level. With overriding, special cases can be handled efficiently and easily.

## 3. Object-oriented approach

## 3.1. Object-oriented analysis

Although a traditional structured analysis approach can still be used, other views have surfaced to handle object oriented (OO) analysis. In object-oriented analysis, the behavior and data of the system are treated as integrated objects using a variety of techniques [8]: there is still no current standard approach.

Martin [15] uses object structure and object behavior analysis for building the model. The main purpose of the analysis is to identify object types and their associations; then their relations to other objects, as well as their purpose and role, are also defined. In OO analysis, the primary focus is in finding out what happens to the objects over time: state transitions –the states that the objects can take and the events that cause the change and the resulting outputs. Object-flow diagrams, event schemata, operation diagrams, object states, and trigger rules are used to do this.

![](/api/attachments/3GZ4BRBY/fulltext/images/4bddfc2b0b04ac18c8c45bcc8b451580c0a3544afe936c541efbe39d214110d4.jpg)  
Fig. 1. Enterprise model of the patient care administrative system.

Table 1  
Candidate classes after elimination of redundant classes.

<table><tr><td>Patient Name</td><td>Physician Name</td><td>Room (Location)</td></tr><tr><td>Treatment</td><td>Patient Record (Patient)</td><td>Physician Identification</td></tr><tr><td>Patient Bill</td><td>Insurer</td><td>Patient Balance</td></tr><tr><td>Patient Service</td><td>Service Charge</td><td>Date Admitted</td></tr><tr><td>Expected Date Discharged</td><td>Date Discharged</td><td>Physician Specialty</td></tr><tr><td>Room Accommodations</td><td>Patient Address (Contact Info)</td><td>Patient Identification</td></tr><tr><td>Patient SSN</td><td>Room Identification (Location)</td><td>Room Phone Ext.</td></tr><tr><td>Main Menu</td><td>Physician Phone Ext.</td><td>Third Party (Insurer)</td></tr><tr><td>Patient Information Display</td><td>Patient Bill Display</td><td>Patient Treat. Display</td></tr><tr><td>Room Utilization Display</td><td>Services Display</td><td>Physician Info Display</td></tr><tr><td>Phone (Contact Info)</td><td>Patient Procedure (Treatment)</td><td>Service Identification</td></tr><tr><td>Patient Home Phone</td><td>Patient Charge</td><td>Patient Contact Info</td></tr><tr><td>Room Location</td><td></td><td></td></tr></table>

According to Jacobson et al. [12], during the analysis phase we must identify objects, organize them, describe how they interact, define the operations of them, and define their internal aspects. The model captures the information, behavior, and presentation of the objects. Objects are one of three types: entity, interface or control.

The “core model,” proposed by de Champeaux et al. [6], has four components. A matrix shows how objects are defined based on their static and dynamic characteristics and behavior both inside the object and between objects. In a static dimension, objects need attributes to describe them. Constraints define the limitations of attribute value combinations. For example, a department may have the attributes director and secretary with “employee” as their value; however, a director is not a secretary, and vice versa, so a constraint could be: director ≠ secretary. In the dynamic dimension, the different states and expected behavior of the object and its interactions are defined.

Coad and Yourdon [4] have developed a well-known approach to analysis that consists of:

Table 2  
Superclasses identified during the exploratory phase.

<table><tr><td>Super Class</td><td>Classes</td><td>Super Class</td><td>Classes</td></tr><tr><td rowspan="7">Display</td><td>Main Menu</td><td>Identification</td><td>Patient Identification</td></tr><tr><td>Patient Information</td><td></td><td>Patient SSN</td></tr><tr><td>Patient Billing</td><td></td><td>Physician Identification</td></tr><tr><td>Patient Treatment</td><td></td><td>Service Identification</td></tr><tr><td>Physician Information</td><td></td><td>Location Identification</td></tr><tr><td>Service Information</td><td></td><td></td></tr><tr><td>Room Information</td><td></td><td></td></tr><tr><td rowspan="5">Phone</td><td>Room Phone Ext</td><td>Name</td><td>Patient Name</td></tr><tr><td>Physician Phone Ext</td><td></td><td>Physician Name</td></tr><tr><td></td><td></td><td>Insurer</td></tr><tr><td>Patient Home</td><td></td><td></td></tr><tr><td>Phone</td><td></td><td></td></tr><tr><td rowspan="3">Charge</td><td>Patient Charge</td><td>Date</td><td>Date Admitted</td></tr><tr><td>Service Charge</td><td></td><td>Expected Discharge Date</td></tr><tr><td></td><td></td><td>Discharge Date</td></tr></table>

1. identify objects by studying the “problem space,” reading requirements, noting any nouns, and listening to the users. Analyze text and pictures.

2. identify structures of the problem by class-member grouping and whole-part grouping. For example, the class vehicle could have car, truck, and motorcycle members, while a car could contain an engine, tires, steering wheel, and transmission.

3. define each structure and object limiting the number of components of each so that the intended user can easily comprehend the problem. Using the “7 ± 2” rule is one way of accomplishing this.

4. define attributes to add detail to the object or classification structure; e.g., the class vehicle and all its members will have VIN, model, and color attributes.

5. define services or required behavior of each object and classification structure upon receipt of a message.

## 3.2. Object-oriented design

In object-oriented design, a variety of techniques can be used to design a system. Several possible approaches have been proposed.

Martin's approach uses class structure and method design. The results from the object structure analysis are used to define and design classes, class methods, class hierarchies, inheritance, data structures, and databases. In method design, the primary focus is towards designing the methods of objects, based on the behavior analysis. The design of methods and operations, procedural logic, non-procedural code, input to code generators, screen and dialog design, and prototyping are accomplished here.

Table 3  
Purpose of each class.

<table><tr><td>Class</td><td>Description and Purpose of Class</td></tr><tr><td>Patient Name</td><td>First, Middle Initial, Last Name identifying patient</td></tr><tr><td>Physician Name</td><td>First, Middle Initial, Last Name identifying physician</td></tr><tr><td>Treatment</td><td>Procedure physician performed on patient</td></tr><tr><td>Patient Bill</td><td>Patient charges for services rendered at the hospital</td></tr><tr><td>Insurer</td><td>Third Party agency for cost coverage</td></tr><tr><td>Patient Balance</td><td>Amount Patient owes for a particular service</td></tr><tr><td>Patient Service</td><td>Service/item a patient has received at the hospital</td></tr><tr><td>Service Charge</td><td>Default amount that is charged a patient for a service</td></tr><tr><td>Date Admitted</td><td>Date patient was admitted into the hospital</td></tr><tr><td>Expected Date Discharged</td><td>Expected date patient will leave the hospital</td></tr><tr><td>Date Discharged</td><td>Date patient was discharged or released to coroner</td></tr><tr><td>Physician Specialty</td><td>Specialization or title of physician</td></tr><tr><td>Room Accommodations</td><td>General/specific room characteristics</td></tr><tr><td>Patient Identification</td><td>Unique number identifying patient (SSN can change)</td></tr><tr><td>Patient SSN</td><td>Patient social security number</td></tr><tr><td>Physician Identification</td><td>Unique number identifying physician (SSN can change)</td></tr><tr><td>Room Phone Ext.</td><td>4 digit extension for rooms that have a phone</td></tr><tr><td>Main Menu</td><td>Entry menu of patient care administration system</td></tr><tr><td>Patient Treatment Display</td><td>Entry/Query screen for patient treatment (from main/info)</td></tr><tr><td>Physician Phone Ext.</td><td>4 digit extension for physicians that have a phone</td></tr><tr><td>Room Utilization Display</td><td>Entry/Query screen for room information (from main/info)</td></tr><tr><td>Services Display</td><td>Entry/Query screen for services information (from main menu)</td></tr><tr><td>Physician Info Display</td><td>Entry/Query screen for physician information (from main menu)</td></tr><tr><td>Service Identification</td><td>Unique code identifying type of service</td></tr><tr><td>Patient Home Phone</td><td>Home phone number to reach patient/immediate family</td></tr><tr><td>Patient Charge</td><td>Amount patient charged for service (may be different than default service charge)</td></tr><tr><td>Patient Contact Information</td><td>Mailing Address, city, state and zip code of patient</td></tr><tr><td>Room Location</td><td>Unique room number identifying a particular room</td></tr><tr><td>Patient Information Display</td><td>Entry/Query screen for patient information (from main menu)</td></tr><tr><td>Patient Bill Display</td><td>Entry/Query screen for patient billing (from main menu/info)</td></tr></table>

Table 4
Roles of each class.

<table><tr><td>Class</td><td>Roles of Class</td></tr><tr><td>Patient Name</td><td>Identify patient</td></tr><tr><td>Physician Name</td><td>Identify physician</td></tr><tr><td>Treatment</td><td>Provide medical/surgical care to patients</td></tr><tr><td>Patient Bill</td><td>Inform patient of charges incurred and balance due</td></tr><tr><td>Insurer</td><td>Identify agency for partial/full payment of patient bill</td></tr><tr><td>Patient Balance</td><td>Accept/Display balance due for service rendered</td></tr><tr><td>Patient Service</td><td>Accept/Display service renderedProvide service/item to patient</td></tr><tr><td>Service Charge</td><td>Accept/Display default service charge for serviceDisplay default charge when adding patient billing record</td></tr><tr><td>Date Admitted</td><td>Accept/Display date</td></tr><tr><td>Expected Date Discharged</td><td>Accept/Display date</td></tr><tr><td>Date Discharged</td><td>Accept/Display date</td></tr><tr><td>Physician Specialty</td><td>Accept/Display specializationQuery doctors for particular specialization needed for a patient</td></tr><tr><td>Room Accommodations</td><td>Accept/Display accommodationsProvide specific options for patient care bedding</td></tr><tr><td>Patient Identification</td><td>Accept/Display/Validate unique identification</td></tr><tr><td>Patient SSN</td><td>Accept/Display/Validate unique SSNInform third party agencies of SSN for identification</td></tr><tr><td>Physician Identification</td><td>Accept/Display/Validate unique identification</td></tr><tr><td>Room Phone Ext.</td><td>Accept/Display phone extension</td></tr><tr><td>Main Menu</td><td>Present user with choicesDetermine when and what user responded to</td></tr><tr><td>Physician Phone Ext.</td><td>Accept/Display phone extension</td></tr><tr><td>Patient Information Display</td><td>Present user with choices:(add/edit/delete/view/query/search/help)(treatment/billing/room)Determine when and what user responded toView/maintain Patient Information recordsValidate/Update corresponding room information if patient assigned to a locationValidate patient not assigned to multiple rooms or occupied rooms</td></tr><tr><td>Patient Bill Display</td><td>User choices: (add/edit/delete/view/query/search/help)Determine when and what user responded toView/maintain Patient Billing recordsReturn to main menu if selected from main menuReturn to patient information if selected from there</td></tr><tr><td>Patient Treatment Display</td><td>User choices: (add/edit/delete/view/query/search/help)Determine when and what user responded toView/maintain Patient Treatment recordsReturn to main menu if selected from main menuReturn to patient information if selected from there</td></tr><tr><td>Room Utilization Display</td><td>User choices: (add/edit/delete/view/query/search/help)Determine when and what user responded toView/maintain Room Information recordsValidate patient not assigned to multiple roomsReturn to main menu if selected from main menuReturn to patient information if selected from there</td></tr><tr><td>Services Display</td><td>User choices: (add/edit/delete/view/query/search/help)Determine when and what user responded toView/maintain Service Information records</td></tr><tr><td>Physician Info Display</td><td>User choices: (add/edit/delete/view/query/search/help)Determine when and what user responded toView/maintain Physician Information records</td></tr><tr><td>Service Identification</td><td>Accept/Display/Validate unique identification</td></tr><tr><td>Patient Home Phone</td><td>Accept/Display phone numberReach patient/immediate family if emergency</td></tr><tr><td>Patient Charge</td><td>Accept/Display chargeDisplay default service charge when adding record</td></tr><tr><td>Patient Contact Info</td><td>Accept/Display contact information</td></tr><tr><td>Room Location</td><td>Accept/Display/Validate unique Room Number</td></tr></table>

Wirfs-Brock et al. [18] design method encompasses definition of a system of objects, description of their public behavior, and their patterns of communication. In the exploratory phase, classes will be developed, assigned responsibilities stating their purpose and required actions and information, and their collaborations with other classes producing a list of other classes that are needed. In the analysis phase, hierarchies of classes are developed, followed by their subsystems. Then protocols are setup for each class. The final design process results in a graph of each class hierarchy, a graph of the paths of collaboration for each subsystem, a specification of each subsystem, and the contracts supported by each class and subsystem.

Booch [3] suggests a “notation” for showing logical and physical and static and dynamic models of the system.

Lastly, de Champeaux et al. identify three types of design: functional, physical, and performance. The first includes defining properties of “classes obeying the declarative constraints specified.” Physical design maps objects to the physical system. Performance design reconciles functional and physical requirements to meet performance requirements.

## 4. Development of an object-based relational database application system

A case example of a patient care administrative system adapted from McFadden and Hoffer [14] is used to illustrate the application of object-based principles to the development of a data base application system.

The hospital is a medium-sized non-profit organization. Its main goal is to provide high-quality health care and, at the same time, lower the cost of care. To do this, the hospital physically expanded in 5 years by adding and renovating facilities. What is now needed is to improve its patient care administrative system. Currently, the hospital uses a minicomputer to handle batch-oriented processing for accounting, billing and accounts receivable, and financial accounting. The new system should allow on-line procedures, such as patient registration or billing inquiries, and also track medical staff, laboratory test results, and patient treatments. Months of planning and analysis led the study team to determine the ten basic functions of the hospital with 22 total processes. The enterprise model is shown in Fig. 1.

## 4.1. Exploratory phase

In the exploratory phase of system design, classes are fully defined indicating the purpose of the class, its task(s) that need to be performed when called upon, and any collaborations with other objects to perform the desired task. Completion of the following steps will result in a list of candidate classes and superclasses. In order to develop classes and superclasses we follow the six-step procedure of Wirfs-Brock et al.

1. List a description of the goals of the design

2. Discover expected inputs and desired outputs

3. Look for noun phrases in required specifications

4. Model categories of classes

5. Model interfaces to the system

6. Model values of attributes, not attributes themselves

After obtaining a list of candidate classes, we eliminate redundancies: see Table 1. Then, we group related classes into a superclass: see Table 2.

Table 5  
Class interactions.

<table><tr><td>Class</td><td>Interactions Between Classes</td></tr><tr><td>Patient Bill</td><td>Patient Information Display(patient id, ssn, name, contact information, insurer)Service Information Display (service description)Patient ServicePatient Service ChargePatient Balance</td></tr><tr><td>Main Menu</td><td>Monitor</td></tr><tr><td>Patient Information Display</td><td>Patient Identification, Patient Name, Patient SSN, Patient Contact Information, Patient Home Phone, Date Admitted, Expected Discharge Date, Discharge Date, Location, InsurerRoom Information Display</td></tr><tr><td>Patient Treatment Display</td><td>Patient Information Display (patient id, ssn, name)Physician Information Display (physician id, physician name)Treatment</td></tr><tr><td>Patient Bill Display</td><td>Patient Information Display(patient id, ssn, name, contact information, insurer)Service Information Display (service description)Patient ServicePatient Service ChargePatient Balance</td></tr><tr><td>Room Utilization Display</td><td>Patient Information Display (patient id, ssn, name)Location, Accommodations, phone extension</td></tr><tr><td>Services Display</td><td>Service IdentificationPatient ServiceService Charge</td></tr><tr><td>Physician Info Display</td><td>Physician IdentificationPhysician NamePhysician Phone ExtensionPhysician Specialty</td></tr></table>

In order to exist, a class must have a purpose. The purpose is simply a definition of what it is, elaborating on the name in which it was assigned. The purpose of each class is documented in Table 3.

Next, the role of each class is defined to show the operations that an object must perform when it receives a message.

1. Split classes if they have too many roles to perform. This will result in a system that is easier to maintain by having fewer areas for modification.

![](/api/attachments/3GZ4BRBY/fulltext/images/480747e959389cdacbc0e3f91d1d2463d510b141fca0249bcce9fb1b0d8a9ed2.jpg)  
Fig. 2. Stand-alone classes.

Table 6  
Message request and provision between client and server objects.

<table><tr><td>Class (Client/Server)</td><td colspan="2">Message</td></tr><tr><td>Patient Name</td><td>1.</td><td>Identify patient (35,36,37,38,41)</td></tr><tr><td>Physician Name</td><td>2.</td><td>Identify physician (40)</td></tr><tr><td>Treatment</td><td>3.</td><td>Provide medical/surgical care to patients (37)</td></tr><tr><td>Patient Bill</td><td>41.</td><td>Inform patient of charges incurred and balance due (36)</td></tr><tr><td>Insurer</td><td>4.</td><td>Identify agency for partial/full payment of patient bill (35,41)</td></tr><tr><td>Patient Balance</td><td>5.</td><td>Accept/Display balance due for service rendered (36,41)</td></tr><tr><td>Patient Service</td><td>6.</td><td>Accept/Display service rendered (36,39,41)</td></tr><tr><td></td><td>7.</td><td>Provide service/item to patient</td></tr><tr><td>Service Charge</td><td>8.</td><td>Accept/Display default service charge for service (36,39)</td></tr><tr><td></td><td>9.</td><td>Display default charge in patient charge when adding patient billing record (36)</td></tr><tr><td>Date Admitted</td><td>10.</td><td>Accept/Display date (35)</td></tr><tr><td>Expected Date Discharged</td><td>11.</td><td>Accept/Display date (35)</td></tr><tr><td>Date Discharged</td><td>12.</td><td>Accept/Display date (31,35)</td></tr><tr><td>Physician Specialty</td><td>13.</td><td>Accept/Display specialization (40)</td></tr><tr><td></td><td>14.</td><td>Inform, through query, those doctors for particular specialization that is needed for a patient (37)</td></tr><tr><td>Room Accommodations</td><td>15.</td><td>Accept/Display accommodations (38)</td></tr><tr><td></td><td>16.</td><td>Provide specific options for patient care bedding</td></tr><tr><td>Patient Identification</td><td>17.</td><td>Accept/Display identification (1,3,5-7,10-12,19,26,28,30,41)</td></tr><tr><td></td><td>18.</td><td>Validate that patient identification is unique (35)</td></tr><tr><td>Patient SSN</td><td>19.</td><td>Accept/Display SSN (1,4-7,10-12,41)</td></tr><tr><td></td><td></td><td>Validate that patient SSN is unique</td></tr><tr><td></td><td>20.</td><td>Inform third party agencies of SSN for identification (41)</td></tr><tr><td>Physician Identification</td><td>21.</td><td>Accept/Display identification</td></tr><tr><td></td><td></td><td>Validate that physician identification is unique (37)</td></tr><tr><td>Room Phone Ext.</td><td>22.</td><td>Accept/Display phone extension (38)</td></tr><tr><td>Main Menu</td><td>23.</td><td>Present user with choices</td></tr><tr><td></td><td></td><td>Determine when and what user responded to</td></tr><tr><td>Physician Phone Ext.</td><td>24.</td><td>Accept/Display phone extension (40)</td></tr><tr><td>Patient Information Display</td><td>35.</td><td>Present user with choices:</td></tr><tr><td></td><td></td><td>Determine when and what user responded to</td></tr><tr><td></td><td></td><td>View/maintain Patient Information records</td></tr><tr><td></td><td></td><td>Validate/Update corresponding room information if patient assigned to a location</td></tr><tr><td></td><td></td><td>Validate patient not assigned to multiple rooms or occupied rooms (23, 36, 37, 38)</td></tr><tr><td>Patient Bill Display</td><td>36.</td><td>Present user with choices:</td></tr><tr><td></td><td></td><td>Determine when and what user responded to</td></tr><tr><td></td><td></td><td>View/maintain Patient Billing records</td></tr><tr><td></td><td></td><td>Return to main menu if selected from main menu</td></tr><tr><td></td><td></td><td>Return to patient information if selected from there (23, 35)</td></tr><tr><td>Patient Treatment Display</td><td>37.</td><td>Present user with choices:</td></tr><tr><td></td><td></td><td>Determine when and what user responded to</td></tr><tr><td></td><td></td><td>View/maintain Patient Treatment records</td></tr><tr><td></td><td></td><td>Return to main menu if selected from main menu</td></tr><tr><td></td><td></td><td>Return to patient information if selected from there (23, 35)</td></tr><tr><td>Room Utilization Display</td><td>38.</td><td>Present user with choices:</td></tr><tr><td></td><td></td><td>Determine when and what user responded to</td></tr><tr><td></td><td></td><td>View/maintain Room Information records</td></tr><tr><td></td><td></td><td>Validate patient not assigned to multiple rooms</td></tr><tr><td></td><td></td><td>Return to main menu if selected from main menu</td></tr><tr><td></td><td></td><td>Return to patient information if selected from there (23, 35)</td></tr><tr><td>Services Display</td><td>39.</td><td>Present user with choices:</td></tr><tr><td></td><td></td><td>Determine when and what user responded to</td></tr><tr><td></td><td></td><td>View/maintain Service Information records (23)</td></tr><tr><td>Physician Info Display</td><td>40.</td><td>Present user with choices:</td></tr><tr><td></td><td></td><td>Determine when and what user responded to</td></tr><tr><td></td><td></td><td>View/maintain Physician Information records (23)</td></tr><tr><td>Class (Client/Server)</td><td>Message</td><td></td></tr><tr><td>Service Identification</td><td>25.</td><td>Accept/Display identificationValidate that service identification is unique (41,8,9,39)</td></tr><tr><td rowspan="2">Patient Home Phone</td><td>26.</td><td>Accept/Display phone number (35)</td></tr><tr><td>27.</td><td>Reach patient/immediate family if emergency</td></tr><tr><td rowspan="2">Patient Charge</td><td>28.</td><td>Accept/Display charge (41,36)</td></tr><tr><td>29.</td><td>Display default service charge when adding record (36)</td></tr><tr><td>Patient Contact Info</td><td>30.</td><td>Accept/Display contact information (41,35)</td></tr><tr><td>Room Location</td><td>31.</td><td>Accept/Display Room Number (38)Validate that number is unique</td></tr></table>

2. Define roles of a class in order to search for related classes more easily.

3. Objects requiring information would be most efficient if they could maintain it, thus reducing the number of messages between objects.

4. Maintain data integrity -keep information about one thing in one place.

5. Share roles between objects, when needed. Larger roles can sometimes be broken down into smaller ones and assigned to more suitable classes.

Following these guidelines, the role(s) for each class are shown in Table 4.

Lastly, we need to identify the interactions between classes; i.e., collaborations. This could be viewed as the first part of a message, the name of the receiving object, without detailing the method of obtaining this information or the parameters to be used: these show the flow of control and data within and between classes. Table 5 shows the high-level interactions between classes that are required in order to perform the roles.

## 4.2. Analysis phase

In the analysis phase, hierarchies of classes are developed, as well as subsystems for classes with a high level of interaction. Detailed messages are then defined for each class, resulting in a graph of each class hierarchy, a graph of the class interactions, a specification of each subsystem, and the messages supported by each class.

The first step is to review the previous class roles and interactions in order to determine if other superclasses can be formed. The hierarchies generated from this step are essentially a graphical view of each of the final superclasses and its subclasses. Abstract classes are created only as the top of a hierarchy. These classes are Identification, Charge, Name, Date, and Phone. Concrete classes are created to be instantiated. Examples are Patient Information, Patient Billing, Physician Information, Service Information, etc..

There are still some stand-alone classes that could not be grouped into a superclass. That type of standalone classes are shown in Fig. 2. These classes are still required for the hospital patient care management system.

The next step is to detail what inputs are needed from other classes for a class to perform its duties. This establishes communication between two classes and is similar to a client/server environment where one class (client) requests some kind of action(s) from another class (server). This demand and supply relationship between the client and the server is shown in Table 6. The numbers in parenthesis indicate what the client requests from the server. This form of messaging shows the receiver of the message, the method or action to be taken, and the requirements from other classes. For example, the class “Patient Name” is required for classes “Patient Information Display,” “Patient Bill Display,” “Patient Treatment Display,” “Room Utilization Display,” and “Patient Bill,” while it requires the class “Patient SSN.” The “Identify” method, or procedure, is included in those messages that require locating information based on some key, such as locating a patient record by social security number in order to find his/her name.

After identifying what is required by a client and what can be supplied by a server, they must be able to send messages to one another. Message passing among client objects and server objects is controlled by the “signature,” which specifies the type of parameters and objects that it can receive and send. Table 7 shows the signatures for the patient care administrative system.

Table 7
Signatures of each Class

<table><tr><td>Class</td><td>Signatures</td></tr><tr><td>Patient Name</td><td>Get_PatientName(Text)</td></tr><tr><td>Physician Name</td><td>Get_PhysicianName(Text)</td></tr><tr><td>Treatment</td><td>Get_Treatment(Text)</td></tr><tr><td>Patient Bill</td><td>PrintBill(Text) returns (Boolean)</td></tr><tr><td>Insurer</td><td>Get_Insurer(Text)</td></tr><tr><td>Patient Balance</td><td>Get_PatientBalance(Currency)</td></tr><tr><td>Patient Service</td><td>Get_PatientService(Text)</td></tr><tr><td>Service Charge</td><td>Get_ServiceCharge(Currency)</td></tr><tr><td>Date Admitted</td><td>Get_Admitted(Date)</td></tr><tr><td>Expected Date Discharged</td><td>Get_ExpDischarge(Date)</td></tr><tr><td>Date Discharged</td><td>Get_Discharge(Date)</td></tr><tr><td>Physician Specialty</td><td>Get_PhysicianSpecialty(Text)Query_Physician(Text) returns Physician Info Display</td></tr><tr><td>Room Accommodations</td><td>Get_RoomAccommodations(Text)</td></tr><tr><td>Patient Identification</td><td>Get_PatientId(Integer)Validate_PatientId(Integer) returns (Boolean)</td></tr><tr><td>Patient SSN</td><td>Get_PatientSSN(Integer)Validate_PatientSSN(Integer) returns (Boolean)</td></tr><tr><td>Physician Identification</td><td>Get_PhysicianId(Integer)Validate_PhysicianId(Integer) returns (Boolean)</td></tr><tr><td>Room Phone Ext.</td><td>Get_RoomPhone(Integer)</td></tr><tr><td>Main Menu</td><td>Display_MainForm(Text)</td></tr><tr><td>Physician Phone Ext.</td><td>Get_PhysicianPhone(Integer)</td></tr><tr><td>Patient Information Display</td><td>Display_PatientInformation(Text)AddPatientRecord(Boolean)EditPatientRecord(Boolean)DeletePatientRecord(Boolean)ViewPatientRecord(Boolean)QueryPatientRecord(Boolean)SearchPatientRecord(Boolean)HelpPatientRecord(Boolean)Validate_RoomNumber(Integer) returns (Boolean)</td></tr><tr><td>Patient Bill Display</td><td>Display_PatientBilling(Text)AddPatientBillRecord(Boolean)EditPatientBillRecord(Boolean)DeletePatientBillRecord(Boolean)ViewPatientBillRecord(Boolean)QueryPatientBillRecord(Boolean)SearchPatientBillRecord(Boolean)HelpPatientBillRecord(Boolean)</td></tr><tr><td>Patient Treatment Display</td><td>Display_Treatment(Text)AddTreatmentRecord(Boolean)EditTreatmentRecord(Boolean)DeleteTreatmentRecord(Boolean)ViewTreatmentRecord(Boolean)QueryTreatmentRecord(Boolean)SearchTreatmentRecord(Boolean)HelpTreatmentRecord(Boolean)</td></tr><tr><td>Room Utilization Display</td><td>Display_Room(Text)AddRoomRecord(Boolean)EditRoomRecord(Boolean)DeleteRoomRecord(Boolean)ViewRoomRecord(Boolean)QueryRoomRecord(Boolean)SearchRoomRecord(Boolean)HelpRoomRecord(Boolean)</td></tr></table>

Table 7 (continued)

<table><tr><td>Class</td><td>Signatures</td></tr><tr><td>Services Display</td><td>Display_Service(Text)AddServiceRecord(Boolean)EditServiceRecord(Boolean)DeleteServiceRecord(Boolean)ViewServiceRecord(Boolean)QueryServiceRecord(Boolean)SearchServiceRecord(Boolean)HelpServiceRecord(Boolean)</td></tr><tr><td>Physician Info Display</td><td>Display_PhysicianInformation(Text)AddPhysicianRecord(Boolean)EditPhysicianRecord(Boolean)DeletePhysicianRecord(Boolean)ViewPhysicianRecord(Boolean)QueryPhysicianRecord(Boolean)SearchPhysicianRecord(Boolean)HelpPhysicianRecord(Boolean)</td></tr><tr><td>Service Identification</td><td>Get_ServiceId(Text)Validate_ServiceId(Text) returns (Boolean)</td></tr><tr><td>Patient Home Phone</td><td>Get_PatientPhone(Integer)</td></tr><tr><td>Patient Charge</td><td>Get_PatientCharge(Currency)Display_ServiceCharge (Currency)</td></tr><tr><td>Patient Contact Info</td><td>Get_PatientContactInfo(Text)</td></tr><tr><td>Room Location</td><td>Get_RoomNumber(Integer)Validate_RoomNumber(Integer) returns (Boolean)</td></tr></table>

![](/api/attachments/3GZ4BRBY/fulltext/images/51fd3dce9f866c205aa86843cc1a50725d298a88e3de912b58a71b130853cf18.jpg)  
Fig. 3. Structure of the main menu.

![](/api/attachments/3GZ4BRBY/fulltext/images/0160a006cce8727b39615ef37eacfe635f1c32c5676d800bf24e3a7274bac772.jpg)  
Patient Care Administration System  
Fig. 4. The main menu screen.

The final step is creating a set of subsystems in which the classes and superclasses are graphically grouped so that they can perform efficiently. The structure of the main menu, as shown in Fig. 3, consists of six choices, or subsystems, of patient care information. The dotted lines represent the data flow relationship between the two subsystems. The screen of the main menu is displayed in Fig. 4. Since physicians treat patients, the treatment subsystem can also be accessed through the physician subsystem. Likewise, since services are charged to patients in the form of a bill, the billing subsystem can be accessed through the service and patient subsystems. These two subsystems are activated through the pull-down menu of the Patient command in the menu bar of the system.

Each subsystem has been designed and fully implemented. For example, Fig. 5 shows the structure of the Patient subsystem, which is designed to display the contact (i.e. address, relative), insurance, and scheduling information about the patient. A sample screen for the Patient subsystem is shown in Fig. 6. The other subsystems are described briefly here. The physician subsystem shows physician information, including his/her specialization for patient treatment. The room subsystem displays its location within the hospital, phone extension, and the accommodations (outside view, television, etc.). Each room has one bed and no more than one patient. The service subsystem maintains services performed by hospital staff. The patient billing subsystem will indicate what is owed by the patient, the original amount owed and the remaining balance. Lastly, the treatment subsystem records services performed on patients by physicians. Charges of services are updated in patient billing.

![](/api/attachments/3GZ4BRBY/fulltext/images/257a73a52f4ac4fb662c6dbe45a35d276d2e78e20c904bc3b82a7fb5339f6466.jpg)  
Fig. 5. Structure of the Patient subsystem.

![](/api/attachments/3GZ4BRBY/fulltext/images/9d0aaa6d49575e71584da6835720b93ed70e6ab96e123e734b7966fc6bf8568c.jpg)  
Fig. 6. A sample screen of the Patient subsystem.

The database component is built by using Microsoft® Access™, a PC-based relational database management system. This database component is accessible through each subsystem. The Record Selection menu bar at the bottom of the display screen of each subsystem serves this function. We also built indexes for each table. Users can issue their own queries through the Record Selection menu bar.

## 5. Discussion and conclusion

In conclusion, object-oriented technology is more than a programming language. It is an approach to software development that uses objects, classes and messages to model real world processes. Objects can be both clients and servers in performing their different roles, just as humans can both request as well as provide services within their varying roles. In the same way that humans are dependent on others to provide a service.

To demonstrate the object-oriented approach to software development, a case of hospital management situation was adapted as an illustration. The system is an object-based relational database application system. This allows an easier transition from data-based to object-based systems.

Due to the limitations of the software used in implementing our application system, it should be noted that our system is just object-based instead of object-oriented. As a consequence, our system cannot utilize many of the advantages of an object-oriented system. It would be easier to use an object-oriented database that can utilize this design to store and access objects instead of a relational database. Secondly, structured and object-based programming languages do not support inheritance, and thus the advantage of reusing code by one or more classes ‘adopting’ the behavior and structure of another can not be implemented.

Ad-hoc queries are not possible with encapsulation, since data can be accessed only through pre-defined methods or functions. Also, object-oriented databases require object-ids instead of keys.

This approach along with the use of an object-oriented programming language should solve the ever-increasing software crisis. Software that is reusable, improved in its design, more reliable, and simpler in its programming and maintenance requirements would truly be an advantage to both users and developers.

[12] I. Jacobson, M. Christerson, P. Jonsson, and G. Overgaard, Object-Oriented Software Engineering: A Use Case Driven Approach, Menlo Park, CA: Addison-Wesley, 1993.

[13] B. Machrone, “Object Oriented: Old Wine, New Bottles?” PC Magazine, Vol. 8, No. 9, 1989, pp. 65–66.

[14] F.R. McFadden and J.A. Hoffer, Data Base Management, Fourth edition, Menlo Park, CA: Benjamin/Cummings, 1994.

[15] J. Martin, Principles of Object-Oriented Analysis and Design, Englewood Cliffs, NJ: Prentice Hall, 1993.

[16] G. Ray, “Growing Pains: Object-Oriented Databases Lack Development Tools,” ComputerWorld, Vol. 27, No. 21, pp. 79–80.

[17] D. Taylor, Object-Oriented Information Systems: Planning and Implementation, New York, NY: John Wiley and Sons, Inc, 1992.

[18] R. Wirfs-Brock, B. Wilkerson, and L. Wiener, Designing Object-Oriented Software, Prentice Hall, 1990.

## References

[1] C. Babcock, “Object Lessons,” ComputerWorld, Vol. 27, No. 18, 1993, p. 58.

[2] C. Babcock, “Relational Backlash,” ComputerWorld, Vol. 27, No. 26, 1993, p. 36.

[3] G. Booch, Object-Oriented Design with Applications, Menlo Park, CA: Benjamin/Cummings, 1991.

[4] P. Coad and E. Yourdon, Object-Oriented Analysis, Englewood Cliffs, NJ: Prentice Hall, 1990.

[5] C. ComaFord, “Are You Object-Based or Object-Oriented?” PC Week, Vol. 10, No. 23, 1993, p. 56.

[6] D. de Champeaux, D. Lea, and P. Faure, Object-Oriented System Development, Reading, MA: Addison-Wesley, 1993.

[7] R. DelRossi, “Update Makes a Good Visual Basic Even Better,” InfoWorld, Vol. 15, No. 29, 1993, pp. 78–79.

[8] J. Fitzgerald and A. Fitzgerald, Fundamentals of Systems Analysis. New York, NY: John Wiley and Sons, 1987.

[9] T.J. Heintz, “Object-Oriented Databases and Their Impact On Future Business Database Applications,” Information and Management, Vol. 20, No. 2, 1991, pp. 95–103.

[10] T.J. Heintz, “An Object-Oriented Approach to Planning and Managing Software Development Projects,” Information and Management, Vol. 20, No. 4, 1991, pp. 281–293.

[11] Interface: Candle's View on IBM's Database World, "The Relational World of Chris Date," Vol. 3, No. 2, 1993, pp. 1–5.

![](/api/attachments/3GZ4BRBY/fulltext/images/8b1d3058680118f15ad3b79989c1e90c2ba1cf4c400c57fa40e5ec4959815265.jpg)

Pi-Sheng Deng is Professor of Computer Information Systems at California State University, Stanislaus. He received his Ph.D. in Management Information Systems from the Krannert Graduate School of Management at Purdue University. His current research interests include machine learning and its application to the design of intelligent agents, distributed decision systems, ecology of computation, knowledge-based software engineering, and object-oriented systems

analysis and design.  
![](/api/attachments/3GZ4BRBY/fulltext/images/7e97dd3fbde3ead0d8cdf19fcca7dce0327084c365c2d5ed854ade7a66e942ec.jpg)

Cynthia L. Fuhr received her MBA from California State University at Stanislaus with a concentration in Computer Information Systems. Currently, she is a Programmer/Analyst with the Yosemite Community College District in Modesto, California, which serves both Modesto Junior College and Columbia Community College in the California Central Valley. Her research and consulting interests include object-oriented programming systems and

database management applications. Ms. Fuhr is a member of Association of Systems Management.
