---
otero_id: 18135
otero_key: "9JTGHCBG"
title: "Using database machines in embedded computer systems"
authors: "Csaba Egyhazy"
year: "1985"
journal: "Information & Management"
doi: "10.1016/0378-7206(85)90016-3"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Using Database Machines in Embedded Computer Systems

Csaba Egyhazy

Virginia Polytechnic Institute and State University, Computer Science Department, 2990 Telestar Corut, Falls Church, VA 22042, USA

A discussion whether or not present database machine technology addresses the needs of embedded computer systems is presented. The interface between the embedded system and its environment tends to be complex, asynchronous, highly parallel and sometimes distributed. In addition, embedded systems are likely to have stringent resource requirements, both physical and logical. An answer to both the complexity issue and the resource limitation can be potentially found in the database machine.

Functions are identified for two applications that the embedded system in general and the database machine specifically are asked to perform. Given the requirements of such applications the current database machine technology is evaluated.

Finally, given the primary requirements of data security and system throughput of tactical embedded computer systems, a database machine using distributed architecture is proposed. The system has the potential for connecting multiple database machines to each host or for connecting multiple hosts to one database machine.

Keywords: Requirements, Database Machines, Embedded Computer systems, Database Schema, Software Maintenance.

![](/api/attachments/9JTGHCBG/fulltext/images/213d0c3c8290cdaeaedae8a17fc7ef1e3a0b0788063f4334d5e163f935392fd7.jpg)

Dr. C.J. Egyhazy is an Assistant Professor of Computer Science at Virginia Polytechnic Institute and State University. He is the Director of the graduate off-campus program in Northern Virginia.

He holds a Ph.D. from Case Western Reserve University and has published on subjects ranging from requirements analysis to design and implementation of information systems.

One of his current research projects is to identify and evaluate policies and strategies for query processing in distributed database systems.

## 1. Introduction

The term “embedded” as used by the U.S. Department of Defense implies that these systems are embedded in larger systems whose primary purposes are not informational. However, this is not new as many developments were part of a larger non-computational system: e.g. rolling (steel) mill control or medical patient monitoring.

The common thread that runs through embedded systems is process control: providing continual or continuous feedback to an environment where the input is a data source that is modified by the feedback. Switching systems, flight guidance and fire control are a few examples of such systems.

## 2. Requirements of Embedded Systems

The demands of embedded environments cause the computer systems to have relatively rigid performance requirements, with rapid real-time response and fail-safe methods. This emphasis on performance really characterized embedded systems, and designers must be aware of such requirements.

Software is the dominant cost in the development of computer systems. Often software costs are 90 percent of the total in software development. Software development is labor intensive and while the number of programmers is increasing, there remains a critical shortage of trained personnel to automate the variety of applications. The result is a very sharp increase in money spent on direct software.

At the same time, it is necessary to reduce software complexity, which provides a reasonably good indication of the cost that may be expected. As the complexity of a system goes up, so do the schedule and cost overruns. Database Management Systems (DBMS) are one of the most complex units of general purpose software in any system, though Operating Systems are almost an order of magnitude higher. For an application associated with embedded systems, the DBMS is generally of equal or greater complexity than the remaining system. Any reduction in the complexity of this software should show real and immediate gains in the cost and schedule. However, few strongly feel the need to establish DBMS standards in embedded systems.

Clearly coping with complexity is not easy in the domain of embedded systems. In addition these systems are especially likely to have stringent resource requirements on both their development and operation.

This resource limitation is a result of embedded systems being installed in places (such as satellites) where their weights, volume, or power consumption may have to be limited, or where pressure, temperature, humidity and other factors cannot be as carefully controlled. Furthermore, these development systems normally require a host or support system for the development and initial verification of the software which further increases the complexity of the software development.

Additionally, the interface between an embedded system and its environment tends to be complex, asynchronous, highly parallel, and in some instances distributed. This is a direct result of the external environment, which is likely to consist of a number of objects interacting with the system and with each other in an asynchronous, parallel fashion.

For these reasons, any system that can reduce the size or other resource constraint on embedded systems will be looked upon with favor. An answer to both the complexity issue and the resource limitation might be found in the database machine.

However, before evaluating the usefulness of database machines, let us identify the applications that the embedded systems in general and the database machines in particular will be asked to perform.

Command and control systems are those that interface a human to an automated control system which provides information and may or may not respond to the command process. Such systems are concerned with ship or battlefield situations, emergency room processing in a hospital or avionics where the pilot is to use 'heads-up' instrumentation. A general characteristic of these systems is the distributed nature of the database. For the ship commander, information resides in different locations on the ship and individual processors maintain the data on fire control, damage assessment and control, maneuvering and intelligence. For emergency room processing, the databases would contain a table of multiple symptoms to aid diagnosis, expected and monitored physiological responses, potential and available drugs and a log sheet of all actions taken.

These systems result in and must respond to alternative data flows. Most systems contain backup or alternate data sources and so the systems must be capable of responding to conflicting information (due to the multiple sources), integrating the 'human' processing (by accepting commands or modifying data according to the human's decision, e.g. if calling for a drug at too high a dosage and allowing control and data to co-exist and co-mingle). This application type also has the characteristic of huge, massive data sets. These databases may be of the order of $10^{12}$ to $10^{15}$ characters and may be displayed as text, graph, plots or as instrumentation data from digital or analog sensors.

A second type of application is an automatic correlation system, which evaluates a threat and outputs actions or warnings. Examples of this are early-warning air raid or hospital patient monitoring systems. Here the raw real-time data usually undergoes signal processing prior to its retention in the correlated database. This signal processing normally results in a throughput-limited system, due to saturation of the processing capacity of the embedded computer. In addition, this processing is usually of a directed nature; that is, the results dictate the type of, or the conditions for, the continued processing. Such systems are knowledge-based, artificial-intelligence-related systems. Most of the knowledge is heuristic in nature with deep decision trees. In addition, the knowledge-based actions are data driven; new operator modified data may force an alternative recommendation depending upon the assessed risk.

These systems are characterized by auto-alert or auto-action response to evaluation. They must be capable of deriving and presenting a full justification for all recommended actions, as the user may want to know what data affected the result on how the recommended action was developed. These systems must also be able to answer ‘what if’ questions based on the data and the set of possible alternatives.

For both the above types of applications, a DBMS must be an integral part of the system. However, the DBMS should have, as a minimum, the following properties:

(i) Minimum resource requirement: the embedded systems may be so taxed that it will not support a full software DBMS.

(ii) Limited overhead: as most systems are real-time process control, the more overhead the less processing.

(iii) Wide performance bounds: the requirements and specifications vary from application to application.

(iv) Complex data relationships: may be best suited to any of the DBMS models plus combinations.

(v) Massive data sets: of the order $10^{12}$ to $10^{15}$ bytes.

(vi) Interactive user interface.

(vii) Fail safe: prevent an unrecoverable or catastrophic error or poor data.

These requirements and the fact that the database management system functions consume so much of the available system resources suggests that a database machine may be an effective solution to the problem. The major advantages of database machines are given in [11]. They are basically problem oriented processor architectures that reside in dedicated hardware. This allows for low cost and wide performance bounds. Most database machines can be matched to the performance requirements of the system. They reduce the software size and complexity by moving processing into the hardware and requiring only interface software in the host [1,2]. Furthermore, database machines can be connected to existing networks, and thus can distribute data and processing [6]. A brief discussion of the architectures of three commercial database machines, as it related to embedded systems, is given in the Appendix.

## 3. The Suitability of Existing Database Machines for Embedded Computer Systems

Given the requirements of applications in embedded systems and the characteristics of the better known database machines, we are now in a position to assess the degree to which existing database machines fulfill these requirements.

The embedded systems demand that the database machine should not require extensive system resources or computing overhead. Unfortunately, most database machines require approximately the same amount of space and power as another embedded computer system. In addition, the target software is not a low overhead item. The target software is initially difficult to develop. This is basically a result of the software development occurring on a host machine. Furthermore, the software is extremely complex. The transaction management, data definition languages, query development and optimization (for the particular database machine selected), as well as the conflict resolution resulting from both contention and the possibly incompatible data make both the target software difficult to use and modify. Modifications will be required not only when errors are discovered, but must also be anticipated as the result of changing requirements. Finally, most database machines are really single hosted, and to find machine transportable software is indeed rare $[3,4]$ .

Another area of embedded system requirements where the existing database machines display some deficiencies is in providing wide performance capabilities and complex data relations. First, since the devices are hardware units, one can only get a single database model for any particular system. Optimization efforts would be difficult over multiple models and application requirements. Secondly, the processing code in the database machines is in firmware, which slows the process of modification and may actually preclude an optimal system from being developed for a number of applications. All the database machines evaluated in [7] had basically static interface processing; if the schema changes, the applications code in the host and the target machine has to change as well. No existing database machine could efficiently cope with the massive data sets ( $10^{12}$ bytes and over) required by embedded systems. Also, the database machines are quite slow if the query does not match the original database schema. This is very constraining for a number of queries associated with either type of application requiring free association. Additionally, general purpose requests may occasionally be considered desirable, and if the schema must be modified to support this type of query, a rebuild of all the target software may be required with a completely new set of data definitions.

Another system requirement is for high reliability, maintainability and availability. Database machines have extremely complex algorithms for balancing multiple copies of the data (their only means of true reliability) among the associated disc drives. The duplication of information among several database machines is left to the host software developer. Because each database machine is basically an independent peripheral, it is extremely difficult to prove consistency of transactions. The multiple copies and multiple transaction logs, compounded by potential data conflicts, are not well handled by these systems.

Maintainability suffers because any change to the database schema requires host applications software modifications. This is a case of very high cost overruns in software development. Furthermore, the embedded system, to meet these requirements, would have to develop very complex failure analysis and transaction updating logic to track failures (both the recognition of failures and the recovery from their impact).

The last area of embedded system requirements that the database machines do not meet are those associated with an interactive user and fail-safe provisions. The user is required to have a full working knowledge of all database schemas in order to make the most of them. In a large distributed system this may require another DBMS (dictionary) just to handle this.

## 4. A New Type of Database Architecture That Might Fulfill The Requirements

A database machine for embedded computer systems, using a distributed architecture, is shown in Fig. 1. This new type of architecture could answer most of the demands placed by the kinds of applications presented in Section 2 and satisfy most of the requirements discussed in Section 3.

The advantage of this architecture is that the control flow and data flow are assigned to dedicated networks that can be duplicated if the contention problem becomes excessive. This addresses the problem learned in the DIRECT system [10]. Secondly, mass storage is provided to each computer through an attached database machine (with its associated discs), and through a mass storage device for the processor alone. This could be used to buffer or store raw data and processing conditions. Additionally, the system has the potential for connecting multiple database machines to each host or for connecting multiple hosts to one database machine [9].

![](/api/attachments/9JTGHCBG/fulltext/images/5d39918aa7736e390a6dbbc30d30bcdc14a544b90eb3b48affa66ca5ed2a3ef8.jpg)  
Fig. 1. Hypothetical Database Machine using a Distributed Architecture.

![](/api/attachments/9JTGHCBG/fulltext/images/a09b4d83873ea166b6c00f751f9f887d0612189d539266cd555a681e3e3a084b.jpg)  
Fig. 2. Direct's Representative Architecture.

## 5. Conclusions

Research and development of database machines continues, and as the current and future evaluations begin to produce documented evidence of the viability of the database machine concept, specifications for their use in embedded computer systems may not be far off.

At the present time, however, given the complexity and unique requirements of embedded systems, none of the existing database machines has proven to be the cure it was once predicted to be. A recently suggested database machine architecture may provide some of the capabilities embedded systems require. The main advantage of this architecture being that the control flow and data flow are assigned to dedicated networks that can be duplicated if the contention problem becomes excessive.

## Appendix

This briefly describes three existing database machines likely to be added to embedded computer systems.

![](/api/attachments/9JTGHCBG/fulltext/images/ba02c253c33a28e63fee54b721e8c95909891e83e9b7f92f7183669e2840cda0.jpg)  
Fig. 3. Brittan-Lee IDM 500's Representative Architecture.

![](/api/attachments/9JTGHCBG/fulltext/images/49e9a9f37540927ed839a3a43c4cb0230605bb174ca47aa46af1fa73ac9d763e.jpg)  
Fig. 4. Terradata's DBC/1012 Representative Architecture.

DIRECT is a database machine developed at the University of Wisconsin. Its basic architecture is shown in Figure 2. The process is a multiple instruction stream/multiple data stream (MIS/MDS).

The backend process is located in the host machine and produces all command and queries to the system. Each processor has its own memory in addition to the one-half mega-byte multi-posted memory. All control and data flow is over the single bus.

Several lessons have been learned from this database machine. In particular, there is a high cost in processing associated with controlling the execution of a query, as the backend processor in the host has to handle this and the returning data. Secondly, code adoption (the system is based on INGRES) is not a trivial task. And lastly, the software overhead associated with message protocols may be an order of magnitude greater than the processing required on the data. The system works, but the bus is marginally effective and is the limiting component in this design.

A second database machine is the Britton-Lee IDM 500. Its architecture is shown in Fig. 3.

The process is a single instruction stream/single data stream (SIS/SDS), and therefore relatively slow. One attempt to speed the process was to add a database accelerator to the basic machine. This option is a special instruction set, hardware device that is optimized for certain sets of queries and allows for the processing of the data to occur during the input of data from the disc. For the queries handled, this allows the system to process in real-time. The host contains the query and command code, plus if the system requires multiple units for capacity or redundancy, all control logic and software must be in the host machine; all translation has to be handled by the host computer.

The Terradata DBC/1012, a prototype database machine, corresponds to a multiple instruction stream/multiple data stream processor [8]. The system's architecture, shown in Fig. 4, allows for multiple units to be connected to one or more host computers. This results in substantial software dependence on the host, not clearly supported by the system.

## References

[1] Auer H. et al., "RDBM - A Relational Database Machine," Informational Systems Vol. 6 No. 2, 1981.

[2] Dogac, A. and Ozkarahan, E. “A Generalized DBMS Implementation on a Database Machine,” SIGMOD Conference Proceedings, Santa Monica, Ca. 1980.

[3] Boral, H. and DeWitt, D. “Design Consideration for Dataflow Database Machines,” SIGMOD Conference Proceedings, Santa Monica, Ca. 1980.

[4] Hawthorn and DeWitt, D. "Performance Analysis of Alternative Database Machine Architectures," IEEE TOSE Vol. SE-8, No. 1, Jan. 1982.

[5] Matsushita, Yu, et al., "Cost Evaluation of Directory Management Schemes for Distributed Processing Systems," SIGMOD Conference Proceeding, Santa Monica, Ca. 1980.

[6] Hardgrave, W.T. "Distributed Database Technology: An Assessment," Information and Management 1 (1978) page 157–167.

[7] Hsiao, D.K. editor “Advanced Database Machine Architecture,” Prentice Hall, 1983.

[8] Downes, V.A. and Goldsack, S.J. "Programming Em-

bedded Systems with ADA $^{®}$ Prentice Hall International, 1982.

[9] Egyhazy, C.J. "Database Machines for Embedded Computer Systems, TR835 Department of Computer Science, Virginia Polytechnic Institute and State University.

[10] Boral, H. et al. "Implementation of the Database Machine DIRECT," IEEE TOSE Vol. Sc-8, No. 6, November, 1982.

[11] Malabarba, E.J. "Review of Available Database Machine Technology" Proceedings Trends and Application, 1984, National Bureau of Standards, U.S. Department of Commerce.
