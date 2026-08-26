---
otero_id: 18463
otero_key: "33QHDMA5"
title: "Structured prototyping: Integrating prototyping into structured system development"
authors: "Peretz Shoval; Nava Pliskin"
year: "1988"
journal: "Information & Management"
doi: "10.1016/0378-7206(88)90064-x"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Structured Prototyping: Integrating Prototyping into Structured System Development

Peretz Shoval and Nava Pliskin

Computer and Information Systems Program, Department of Industrial Engineering and Management, Ben-Gurion University of the Negev, P.O. Rox 653, Beer-Sheva 84105, Israel

Submitted: March 1987

Revised: October 1987

Software development methodologies present two major schools of thought: one is that of structured system development and the other is that of prototyping. Between these extremes, there are many mixed approaches. But any form of prototyping, though attractive, is difficult to implement for large systems because of its implied lack of structure. This paper proposes a framework for the integration of prototyping into structured system development. We first carry out structured analysis and design; these products are then used to support systematic prototyping. The resulting prototype serves to provide the user with an iterative process of understanding and improving the requirements until they are satisfactory. This methodology for structured prototyping has four elements: interface, data, process, and system prototypes. The methodology is based on a new unified approach to the analysis and design phases.

Keywords: Systems analysis and design, Prototyping, Structured development life cycle, User interface, Software engineering, Software development methodologies.

## 1. Background

Approaches to information system development today normally utilize either a structured life cycle approach or attempt some form of rapid prototyping; sometimes they use a mix of both [3]. The prototyping approach is, however, controversial [7], with conflicting reports on its effectiveness and efficiency. Prototyping seems appropriate for small problems and is especially useful in determining requirements [17]. For complex prob-

![](/api/attachments/33QHDMA5/fulltext/images/2c37bfa8e5faa9406950595243c60c5c19ff6160d5b0cfd055d76b2d31b993a8.jpg)

eval. He has published in journals such as Information Systems, Int' Journal of Man-Machine Studies, Information & Management, Information Processing & Management, Data & Knowledge Engineering, and Data-Base.

![](/api/attachments/33QHDMA5/fulltext/images/40c37b23813b97ae7618af6d6b4bce2d9609725456dc1f7364a6bad3f08e5487.jpg)

leins, prototyping is being criticized; there are several reasons, such as the increased project risk compared to structured life cycle techniques [13].

The Structured Development Life Cycle (SDLC) approach to information systems development has been used for about two decades. Though the software engineering literature $[8,11,20,21,23]$ provides many definitions and alternative methods, SDLC is essentially a standard $[1]$ ; SDLC generally is defined to have five phases: the preliminary survey, analysis, design, creation, and implementation.

One method in the analysis phase is Structured Analysis, which is based on the use of hierarchical data flow diagram (DFD) that define and describe the various functions, the data stores, the external entities, and the data flows [9,12]. This method also produces a data dictionary, a database schema, and structured descriptions of the elementary functions (mini specs). These products provide a specification of the system to be used in the next stage – system design.

In the design phase, a distinction is usually made between architectural design (preliminary, structural, or subsystem design) and detailed design. The Structured Design technique is most commonly used to create a modular description of the system $[26,27,28]$ , and Structure Charts are the vehicle to show the partitioning of the system into modules and their necessary control.

Transition from the DFDS to Structure Charts suffers from severe limitations because:

a. since Structured Design was originally used to develop programs rather than for architectural design, it is not a comprehensive system design technique,

b. DFDs play a minor role in Structured Design; only limited DFD notation is applied (i.e. to functions and data flows),

c. the generation of an initial Structure Chart from a DFD can be complicated and difficult,

d. the DFDS are not updated when the Structure Charts are changed,

e. Structured Analysis provides other products, such as database schema and mini specs, that the Structured Design does not use, and

f. neither Structured Analysis nor Structured Design deal with the user-system interface.

Because of these reasons, the ADISSA (Architectural Design of Information Systems based on Structured Analysis) methodology [22] was developed. It is fully compatible with, and is a direct continuum of Structured Analysis and combines the stages of analysis and design into a complete process.

SDLC is also criticized because of the problems in communication between the systems analysts/designers and the users throughout the development process. SDLC techniques are usually applied by professionals working with users expected to provide their requirements, at the start, and to accept the system upon completion. Often the SDLC tools provide textual or graphical representations that are neither effective nor efficient, so that both user and analyst inadequately understand the requirements, even though the design is approved. Moreover, since SDLC often involves a requirements "freeze" before implementation, the final output carries the risk of not accounting for the dynamics of the environment. This may therefore be unsatisfactory or even useless from the user point of view [6]. Thus, Wasserman [24] states that user dissatisfaction is a major issue of concern with SDLC.

These user-related drawbacks of SDLC triggered the concept of prototyping $[2,4,5,14,18,25]$ , borrowed from other engineering disciplines. In prototyping, as in SDLC, a builder and a user cooperate to reach a working application. The means of communication are demonstration models that the developer may build quickly, possibly using a fourth generation language. These models present the user with an approximate system rather than an imaginary one, introducing the reality missing from communication using the SDLC. According to Keus $[24]$ , if the process results in an actual production system it is an “add-on”, using evolutionary prototyping. Otherwise, when the prototype is discarded and a production system is constructed, it is a “throw-away”.

Many success stories on prototyping have appeared in the information systems literature $[10,16]$ , especially for systems with heavy user interaction $[15,17]$ , but there has been criticism as well. While prototyping is associated with more user satisfaction and less cost than SDLC, it is also known to result in less efficient systems and development processes which are more difficult to manage and control. This critique is most relevant to evolutionary prototyping, where lack of structure in the development process can lead to sloppy systems. Small information systems (developed on a small computer, serving one or a few users, featuring limiting storage volume and transaction load) can be developed with no precise distinction between phases of development. Thus, structured techniques are not essential and evolutionary development is often successful. On the other hand, for large information systems (implemented on mainframes, multiuser, complex, high transaction load, and where performance is important) prototyping has not been an effective substitute for structured techniques.

This outlook has brought on discussions of the advantages of developing a hybrid SDLC-prototyping approach, where prototyping is mainly used to cope with the preliminary survey and requirement definition, and the remainder of the development is carried out according to SDLC [6]. Under this approach, the professional developer quickly creates a working model based on initial requirements, and adjusts the prototype to meet further requests of the user. Eventually, it is thrown away, and modified structured methods are pursued to create the production system.

Systems analysts who perform well within the framework of SDLC find it difficult to manage hybrid system development, because of the improvisation inherent in prototyping. Connor [8] argues that systems cannot be prototyped without prior specification, and he proposes a combination of prototyping with good SDLC techniques. We offer to remedy the situation with Structured Prototyping (SP); this integrates methods by making products of the ADISSA methodology the basis of a systematic and consistent prototyping process.

SP is consistent with engineering prototyping. There, prototyping takes place only after detailed planning; it represents a proof of concept. The intention of SP is not to shorten development time, but is incorporated into SDLC to achieve more user satisfaction.

## 2. Structured Analysis and Design, the ADISSA Way

Shoval [22] has developed a methodology for Architectural Design of Information Systems based on Structured Analysis (ADISSA); this provides the missing links between Structured Analysis and Structured Design, closes the gaps discussed in the previous section, and yields a robust basis for a structured prototyping process. Two major products are the essence of ADISSA: one is the user interface, a menu-tree, viewed as the external architecture of the system; the other is the internal architecture, a set of system transactions activated in response to various events and user-requests. Fig. 1 shows the seven parts of ADISSA.

In online interactive systems there are two major types of user interface: one for experienced users using a command language, and the other for naive users using menus. Since a command-driven interface has the same functionality as a menu-driven one, only the latter is discussed here. A menu-tree consists of a hierarchy of menu screens that express the possible options in terms of menu lines, which may either lead to other menus (selection lines) or terminate by activating specific system procedures (terminal lines).

The menu-tree is the external architecture of the system, as understood by its users. Thus, menu-tree design must be systematic and structured. In ADISSA, the menus are derived almost automatically from the DFDs, yielding a menu-tree that is a subset of the DFDs tree. Menu lines are derived from data flows between external entities and elementary functions. If the data flow is between an entity and a general function, the menu line is a selection line, but if the data flow connects to an elementary function, a terminal line results.

A transaction is a collection of elementary functions performed in response to a trigger, user-initiated or otherwise. In transaction design, it is necessary to identify the transactions of the system and to define for each their trigger(s), elementary functions, order of execution, inputs, outputs, and database records.

An event is a trigger, or stimulus, that initiates a transaction. These may be user, time, real-time, communication, and internal events. In order to manage these event types, ADISSA classifies associated entities according to the triggering event type. A user entity (UE) is represented as a rectangle, as is the original external entity in Structured Analysis. To activate a user transaction the user chooses selection lines in a series of menus until a terminal line is reached. In ADISSA, the DFD terminology is augmented to include the other events and their associated entities.

Time, real-time, and communication entities are represented as triangles, appearing outside the DFD frame, denoted TE, RTE, and CE. A time event

![](/api/attachments/33QHDMA5/fulltext/images/795fd69f1e22e1f8a0fabaa269da3f0da21a28836daf369c0d76af9197fa69ef.jpg)  
Fig. 1. Stages of Structured-Analysis + ADISSA.

activates a transaction on a regular temporal basis. The data flow which connects the TE with the DFD function indicates the trigger time. It is possible to have mixed transactions that may be activated both automatically (as a function of time) and by a user (according to need). Time activated transactions appear in the menu tree only if they are mixed. In real-time systems, a sensor/detector device, the RTE, may trigger a transaction, thus causing a real-time event. The information sensed by an RTE is carried by a data flow connecting it to a function in the DFD. A communication event occurs when a message is received from another system. It is represented in the DFD by a data flow connecting a CE with a function. The data flow carries the message that is communicated.

An internal event occurs when one elementary function activates another via a data-flow. Hence, a transaction is composed of chained elementary functions and can terminate either with a database update (when connected to a data store) or with some output to the user (when connected to a UE).

To explain the ADISSA stages, two DFDs are presented in Figs 2 and 3. These represent an information system for a plumber analyzed and designed using ADISSA [22]. In Fig. 2, DFD-0 contains three general functions (concentric circles). The TE triangle in DFD-0 is related to function-3, indicating that there are activities that take place at month end. Fig. 3 includes only elementary functions (circles) that provides the details of function-2.

![](/api/attachments/33QHDMA5/fulltext/images/be45b61c37a67d38c9552a0a228f3930e3598ee705dec670b125d17ccd483dd9.jpg)  
Fig. 2. DFD-0 of the Plumber information system.

Event Analysis is an extension and refinement of the functional analysis stage of Structured Analysis; it is embedded in stage 1 of the combined Structured Analysis and ADISSA methodologies. It includes the identification of the various types of events and incorporation of the new types of entities (TES, RTES, and CES, where relevant) along with the UES in the DFDS and the data dictionary.

Initial Menu-tree Design involves a review of the DFD hierarchy in a search of functions connected to UES. Such a DFD leads to the definition of a menu-screen that includes a line for every function linked to a UE. Each line is denoted with the DFD identification number and name of the involved function. A menu-screen will include a terminal-line if the UE is connected to an elementary function, otherwise it will have a selection line. Terminal lines are marked with a 'T'. The initial menu-tree will be revised after the next stage.

![](/api/attachments/33QHDMA5/fulltext/images/3dfff73818dab537867b6c39efb3995f46577637163875d1dae76ed14da50b89.jpg)  
Fig. 3. DFD-2 of the Plumber information system.

Transaction Design is almost identical for all types of transactions except for identification of the trigger. User-transactions begin at terminal lines in the menu-tree, whereas connections of TES, RTES or CES to elementary functions in the DFDS mark the beginning of other transaction types. Transaction design requires the identification of chained elementary functions. Identification of input and output activities (occurring whenever a function is connected with a UE) and database updates and retrievals (occurring whenever a function is also connected to a data store) is also included.

DFD-2 has four user transactions. One transaction contains function 2.1, which is activated by the user who wishes to enter a job request from a customer. Another transaction includes functions 2.7 and 2.8 and is activated when the plumber wants a report on job completion: after statement of the actual materials used on a job, function 2.7 retrieves the job details (from data store D3) and updates data store D1 with this consumption of material. Next, function 2.8 is activated to retrieve data on prices (to be used in cost calculations) from D1, to update the customer's debt record in D4, and to produce the job completion report for the customer.

Throughout the process of transaction design, some changes in the DFDS may be required, resulting in feedback to earlier stages. At this point, the menu-tree is finalized. If a menu screen has only one line (and thus is "degenerate") it is pruned. If this single line is a terminal line, the selection line leading to it in the corresponding parent screen is considered quasi-terminal (and marked 'fQ'). Then, line identification numbers and names are changed to become more meaningful to users.

Fig. 4 presents the menu-tree for the plumber's system. The main screen contains three selection lines because each of the general functions in

DFD-0 is tied to at least one UE. Screen-2 has four terminal lines that trigger the four transactions of DFD-2. Altogether there are ten user transactions associated with terminal lines ('T' and 'TQ's) in the menu screens. Eventually, every transaction will be programmed to contain elementary function modules, thus achieving a modular structure for the system consistent with the DFDs.

Structured Description of Transactions now replaces the structured description of elementary functions (the mini-specs of Structured Analysis). ADISSA opts for such description at the transaction level, because elementary functions are not usually isolated and there are interrelationships among functions, data stores, input-output related activities.

In transaction design, a two-level method is employed to facilitate the transaction description. The top-level description defines the “skeleton” of the transaction and its general control in four ways: (a) the execution of elementary functions, (b) inputs / outputs of external entities, (c) reads / writes to the database, and (d) moves of data elements from one function to another.

![](/api/attachments/33QHDMA5/fulltext/images/6d2e7bbbfca50f3176b65015c0d8bd0eaa78b3dba53e38e9544b3acbafb89707.jpg)  
Fig. 4. Menu-tree of the Plumber information system.

![](/api/attachments/33QHDMA5/fulltext/images/00cdc3eab83e3e54729243ccf7560273104e552ee3a3421ccb7e2e60a11646f9.jpg)

```txt
Begin User-Transaction 2.3-2.6
Input from UE3 (customer): rejection or approval
Read from D3 (job proposals): job proposal
Execute Function 2.3: accept customer's reply
If (reply=approval)
    then Move to Function 2.4: approval
    Input from UE3 (customer): first payment
    Execute Function 2.4: accept payment
    Write to D3 (job proposals): status of accepted
    Move to Function 2.5: payment details
    Execute Function 2.5: open customer account
    Write to D4 (customers' accounts): details of payment
    Output to UE3 (customer): receipt
    else Move to Function 2.6: rejection
    Execute Function 2.6: close job proposal
    Write to D3 (job proposals): job proposal to delete
End-If
End Transaction.
```  
Fig. 5. A User-Transaction and top-level description.

One of the transactions of DFD-2 is presented in Fig. 5, both graphically and in terms of a top-level structured description. The details of each line will be included in the lower-level description of the transaction. For each Execute Function in the top-level description there is a detailed layout of the process logic of the elementary function in the transaction (by means of structured programming techniques). This segment is equivalent to the original mini-specs of Structured Analysis, only now they are expressed in the context of the appropriate transaction. For each top-level Read/Write, the exact record types and access paths will be defined after the database schema design. For each Input/Output, the associated type and media will be defined in the Input/Output schema design.

The Database Schema Design is deferred until completion of transaction design, because modifications of DFDs, data stores, and data flows are possible during transaction design. The database design process results in a set of normal form relations. It is bridged to the transaction design via the lower-level description of the Reads/Writes.

The Input / Output Schema Design involves the specification of types and media for every Input/Output line in the top-level transaction description. These may include input-screens, forms, output-screens, and printed reports. The entire set of inputs and outputs comprise the Input/Output schema.

The Data Dictionary of ADISSA has two components: the menu-tree component is an inventory of all menu-screens, and the transaction component is the top-level description of all transactions.

ADISSA is a methodology that provides a smooth transition from Structured Analysis to architectural design; its tools fulfill established software engineering principles, such as top-down approach, stepwise refinement, and modular design. Moreover, the resulting documents provide a basis for structured prototyping, composed of the interface, the data, the process, and the whole system.

## 3. A Methodology for Structured Prototyping

In SP, prototyping is not a substitute to structured development. On the contrary, the ADISSA approach to structured analysis and design is a prerequisite for creation of the system prototype. With that prototype in hand, the developer is not expected to use any other products of analysis and design for communication with the user. Rather, the prototype is used in consultation sessions with the user to refine and improve the analysis and design. Changes following interactive work with the prototype are fed back to update earlier ADISSA products that will be used to create the production system (unless the prototype itself becomes the system). Documentation will thus be kept up-to-date at all times.

![](/api/attachments/33QHDMA5/fulltext/images/2739e19f60ff4d7f3f6b86134b71730cc23c5c4ba8b02c8ffc5aed0994d7db40.jpg)  
Fig. 6. Structured Prototyping.

ADISSA and the utilization of its products provide structure to the prototyping; hence the term structured prototyping. While structure is unusual in prototyping, SP assumes the same fourth generation environments as normal rapid prototyping. The process of iteratively creating and improving prototypes necessitates a fourth generation language for quick and inexpensive creation of test models.

Fig. 6 shows how the elements of SP are related to products of ADISSA.

The SP method is composed of four components. The interface, data, and process prototypes provide the ingredients for the final element: the system prototype. These are now defined.

## 3.1. Interface Prototype

This is based on two ADISSA products, the menu-tree and the Input, Output schema. Of all SP elements, this one is most likely to be used in the production system, even when the prototype becomes a throw-away.

The prototype builder uses a menu generator module to develop, from the menu-tree, a hierarchy of menu screens. The user is allowed to navigate through these and comment on the functionality and the friendliness of the menu tree. The user may then express wishes for help screens or the ease of movement between screens.

The ADISSA Input/Output schema contains the sketches of input screens and forms and of output screens and reports. In prototyping the interface, the builder can apply the screen management module for screens, etc., to create the Input/Output tools. The user reacts to the screens, forms, and reports to improve on these interfaces both visually and functionally. Error checking of the various input fields, titles and explanations, etc. are also included.

## 3.2. Data Prototype

The data prototype is a database schema created using the database management module of an application generator and its data definition language. Included are definition of record types, fields, keys, domains, etc. For fields that are used as access paths, such an environment enables a straightforward definition of secondary keys or indexes.

Most of the work with the data prototype is delayed until the defined record types are tied to functions (within transactions) that perform retrievals and updates. The data prototype need not be disclosed to the user. However, to provide user interaction, addition of real data may be needed, for at least some of the record types, to allow builders and users to cooperate in the simulation.

## 3.3. Process Prototype

The process prototype is a collection of program modules based on the mini-specs of ADISSA. The structured descriptions of elementary functions and the fourth generation language make the programming and testing quick and manageable. Testing also covers the reads and writes versus the data prototype, and the inputs/outputs versus the interface prototype.

In a large and complex system, there will be many elementary functions. Since the amount of work to be invested in prototyping may be overwhelming, it is not necessary to program all modules. Rather, the prototype builder may concentrate on the most important transactions associated with heavy use, etc. In the sample transaction (Fig. 5), writing program modules for each of the four elementary functions will facilitate real testing with the user of: input of the customer response, accepting payment details, retrieval from data store, update of data stores, and output of the customer receipt. At this stage, each module is tested separately.

## 3.4. System Prototype

The system prototype is achieved through the prototyping of complete transactions. The top-level description provides a transaction “skeleton” (Execute Function, Read/Write and Input/Output) as well as process logic and control. The prototype builder programs this “skeleton”, creating a program module call for each Execute Function, accessing records for each Read/Write, and generating a screen/form/report call for each Input/Output. Calling and accessing is with respect to earlier prototype products; thus complete programs are created for each transaction, including test simulations with test data and cases.

To complete the system prototype, it is necessary to create clusters of transactions for the event types. User transactions are tied to the menu-tree by creating the appropriate transaction calls at terminal lines. Thus a cluster of user transactions activated through menu screens is developed. For activation of time transactions, the builder must program a scheduler to simulate the passing of time and setting triggers. Real-time and communication transactions are activated randomly and their testing is done by simulating sensor or communication data.

## 4. Conclusions

The methodology for structured prototyping presented in this paper combines SDLC and prototyping. The ADISSA methodology is a prerequisite to it, as its products are the basic upon which SP builds. Four components make up the SP methodology: interface, data, process, and system prototype.

So far, SP has only been applied in an academic setting. A few small projects have been analyzed and designed by students and then a prototype generated using dBASE III. The following advantages were evident:

1. The approach introduced the structure, so often missing from prototyping, by forcing order on the process.

2. The documents created in ADISSA increased prototyping speed and efficiency.

3. Because communication with the client was limited only to live working models that resulted from prototyping, convergence to requirements was relatively fast and good.

4. Communication with users throughout the SP process covered some aspects of system testing, saving time in future implementation tests.

5. Though with ADISSA or prototyping alone the time to implementation of a production system might be shorter, the time loss was easily regained during testing and implementation, because the prototype was almost identical to the production system, and modifications were rarely required.

Further research is needed to evaluate the SP methodology. In particular, the dominance of SP over the parent development options should be investigated. In our observations, the advantages of SDLC as well as most positive features of rapid prototyping were not compromised. But more experience must be gained before it can be concluded that, though SP development costs are higher than with either parent methodology alone, total life cycle cost under SP is competitive. Once these questions are laid to rest, research should strive to identify systems and environments that are ideal for SP application.

Another direction of research concerns the adaptation of SP to end user prototyping [5,19]. The authors feel that users of information technology, such as implementors of Lotus 1-2-3 and dBASE III, might improve upon their prototyping skills and contribute more to development of information systems. The methodology is straightforward, so that sophisticated users might be better equipped to perform in the prototyping mode if introduced to ADISSA user-related components.

Should further research support the validity of SP, information systems practitioners will be able to engage SP for better management and control of information systems departments. Improvement will occur in system development, with reduction of the development backlog. There would also be a better relationship between the information systems organization and users.

## References

[1] Ahituv, N., M. Hadass, and S. Neumann, "A Flexible Approach to Information System Development". MIS Quarterly, Vol 8 (2) (June 1984) 69–78.

[2] Alavi, M., "An Assessment of the Prototyping Approach to Information Systems Development". Communications of the ACM, Vol 27 (6) (June 1985) 556–563.

[3] Alavi, M., "The Evolution of Information Systems Development Approach: Some Field Observations". DATABASE, Vol 18 (3) (Spring 1984) 19–24.

[4] Berrisford, T.R. and J.C. Wetherbe, "Heuristic Development: A Redesign of Systems Design". MIS Quarterly, Volume 3 (1) (March 1979) 11–19.

[5] Bohr, B.H., Application Prototyping: A Requirements Definition Strategy for the 80s. John Wiley & Sons, New York, NY (1984).

[6] Burns, R.N. and A.R. Dennis, "Selecting the Appropriate Application Development Methodology". DATABASE, Vol 17 (1) (Fall 1985) 19-23.

[7] Carey, T.T. and R.E.A. Mason, "Information System Prototyping: Techniques, Tools and Methodologies". INFOR, Vol 21 (3) (August 1983) 177–187.

[8] Connor, D., Information System Specification & Design Road Map. Prentice-Hall, Englewood Cliffs, NJ (1985).

[9] DeMarco, T., Structured Analysis and System Specification. Prentice-Hall, Englewood Cliffs, NJ (1982).

[10] Earl, M.J., "Prototype Systems for Accounting, Information and Control". DATABASE, Vol 13 (2-3) (WinterSpring 1982) 39–46.

[11] Freeman, P. and A.I. Wasserman: Tutorial on Software Design Techniques. Fourth Edition, IEEE Computer Society, Long Beach, CA (1983).

[12] Gane, C.P. and T. Sarson: Structured Systems Analysis: Tools and Techniques. Prentice-Hall, Englewood Cliffs, NJ (1979).

[13] Janson, M.A. and L.D. Smith, "Prototyping for Systems Development: A Critical Approach". Mis Quarterly, Vol 9 (4) (December 1985) 305–316.

[14] Jenkins, A.M., 'Prototyping: A Methodology for the Design and Development of Applications Systems'. Spectrum, Vol 2 (2) (April 1985).

[15] Keen, P.G.W., "Adaptive Design for DSS". DATABASE, Vol 12 (1) (Fall 1980) 15–25.

[16] Kraushaar, I.M. and L.E. Shirland, “A Prototyping Method for Applications Development by End Users and Information Systems Specialists”. MIS Quarterly, Volume 9 (3) (September 1985) 189–196.

[17] Mason, R.E.A. and T.T. Carey, "Prototyping Interactive

Information Systems". Communications of the ACM, Vol 26 (5) (May 1983) 347–354.

[18] Naumann, J.D. and A.M. Jenkins, "Prototyping: The New Paradigm for Systems Development". MIS Quarterly, Vol 6 (3) (September 1982) 29–44.

[19] Pliskin, N. and P. Shoval, "End User Prototyping: Sophisticated Users Supporting System Development", DATABASE, Vol 18 (4) (Summer 1987) 7–12.

[20] Pressman, R.S., Software Engineering: A Practitioner's Approach. McGraw-Hill, New York, NY (1982).

[21] Shooman, M.L., Software Engineering: Design, Reliability and Management. McGraw-Hill, New York, NY (1983).

[22] Shoval, P., "ADISSA: Architectural Design of Information Systems Based on Structured Analysis". Information Systems, Vol 13 (2) (1988).

[23] Sommerville, I., Software Engineering. Addison Wesley, London (1982)

[24] Special Issue on Rapid Prototyping, Software Engineering Notes, Vol 7 (5) (December 1985).

[25] Sprague, R.H. and B.C. McNuriin, Information Systems Management in Practice. Prentice-Hall, Englewood Cliffs, NJ (1986).

[26] Stevens, W.P., Using Structured Design. John Wiley and Sons, New York, NY (1981).

[27] Stevens, W.P., G.J. Myers and L.L. Constantine, "Structured Design". IBM Systems Journal, Vol 13 (2) (1974) 115–139.

[28] Yourdon, Y. and L.L. Constantine, Structured Design, Prentice-Hall, Englewood Cliffs, NJ (1979).
