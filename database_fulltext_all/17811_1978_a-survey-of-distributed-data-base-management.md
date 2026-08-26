---
otero_id: 17811
otero_key: "BZ57FG4N"
title: "A survey of distributed data base management"
authors: "Myron Miller"
year: "1978"
journal: "Information & Management"
doi: "10.1016/0378-7206(78)90016-2"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Survey of Distributed Data Base Management

Myron Miller

Boeing Computer Services Company. P.O. Box 24346, Seattle, Washington 98124, USA

A survey of the literature on Distributed Data Base Management Systems is presented. The problems associated with distributing data throughout a network are summarized into two major areas: Data Distribution and Data Transfer. Each area is described detailing some of the major proposed solutions to the problems therein. The intention here is to provide the reader with an overview and an extensive bibliography for further study on any aspect of Distributed DBMS.

Keywords: Distributed data base, file allocation, synchronization, deadlock, data base computers, back-end data base machines, data base model, network information systems, data translation

![](/api/attachments/BZ57FG4N/fulltext/images/470918ff153186ff48ad39154457ec209244bebf9a312900eeb9792122c74c90.jpg)

Myron Miller (born 1944) is a senior data base analyst for Boeing Computer Services in Seattle, Washington, USA. After graduating in Mathematics from the University of Western Washington (BA 1966), he attended Lehigh University before entering the U.S. Air Force. He has worked as a statistician at the University of Colorado Medical Center and at Marshall Space Flight Center in Huntsville, Alabama. After working as a data consultant at the State of Tennessee and with Programming Methods, Inc., he joined Boeing Computer Services in 1977.

## 1. Introduction

This article surveys the literature on Distributed Data Base Maganement Systems (DDBMS) with primary emphasis on the past six years. The intention here is to brief the reader and provide an introduction to the extensive bibliography for further reading on DDBMS. This survey concentrates on research and manufacturing applications published in English. If the reader has knowledge of other systems or research, the author would appreciate hearing about it to update the bibliography. The emphasis of this survey, therefore, excludes comment on purely localized Data Base Management Systems. For comprehensive surveys and studies of those, the reader can read either Fry and Sibley [160], or Munson and Smith [301]; both articles give bibliographies and are good starting points for extended study in localized Data Base Management Systems.

Similarly, network communications and line protocols will not be covered here. There are excellent bibliographies by Pernard [37], Blanc [43], and Kimbleton and Schneider [315] which provide an excellent starting point. Kimbleton and Schneider survey the various technical considerations when using computer networks and describe the various functional components and interactions involved in networking. Cotton [89] provides a survey of some of the various network management practices using five different networks as examples: ARPA, MERIT, Triangle Universities Computation Center (TUCC), Oregon State Regional, and Tymnet. Blanc [43] describes technical characteristics and approaches in networking. He also categorizes the features of a network and relates the communication support functions to the various user support capabilities. In doing so, he illustrates by describing CYBERNET, GE

Information Systems, TSSNET, and some of the previously mentioned networks.

Here, Distributed Processing is defined as computing capabilities at either local or remote sites which may or may not be connected by communication lines but which have interleaved or interconnected memories. Examples of systems which are not distributed processing systems are the IBM MP type system and the shared-spool HASP systems. On the other hand, the IBM concept of the 3790 Distributed Functions or the Digital Equipment full DECNET $^{(R)}$ distributed system are examples of Distributed Processing systems in one sense of the term.

A Distributed Data Base is defined as a logical collection of data which is partitioned, managed, and stored as autonomous units at physically separate and independently addressable nodes in a network. Thus, a Distributed Data Base is a logical body of data stored at several geographic locations. An example is the Distributed File System in the Distributed Computing System of Farber [135]. The back-end data base, as proposed by Canaday [62] and Cullinane [95], is not, by definition, a distributed data base.

Placing the data at various nodes in the network causes a number of complications and problems to arise. Some of these are also found in the nondistributed environment: e.g., the updates between various files must be synchronized; the architect must decide how copies of the file are to be placed around the network: the recovery of the files, the update traffic, and communication between the nodes all add complications. This paper provides a general survey of the literature in this field.

Unique to the networked environment is the problem of distributing the data. This involves the complicated question of whether to introduce multiple copies of files within the network or whether to distribute the data nonredundantly throughout the network. The introduction of multiple copies creates additional problems.

The distribution of data base management functions can provide the user with capabilities which would be unavailable on a local scale; it should also be possible to realize increased performance, versatility, and responsiveness. By storing the data at its source, the user should be able to better control the integrity and validity of his data. As hardware costs continued to decline, many functions which formerly had to be done on large centralized machines can be localized to allow distributed minicomputers to remove some of the processing load from the original centralized machine. This could reduce the need for larger, more powerful centralized machines as hosts for interactive data management.

The problems c. implementing distributed data bases can be simplified into two major categories: 1) the distribution of data across the nodes and 2) the transfer of data between nodes.

## 2. Data distribution

The distribution of data involves allocating the data in the network, locating the data for processing it, and coordinating its processing. The data allocation issue involves a decision on degree of data replication and need for redundancy. The latter issue includes the question of allocating the multiple copies to provide the desired availability. Deadlock and synchronization considerations as well as recovery from local or global failure are also part of the coordination problem.

If significantly greater data base reliability and availability are desired, multiple copies of the data base have been shown to be desirable. Belford [31] developed a model which quantifies “the improvement in data base availability which can be achieved by storing a backup copy at one (or more) remote sites in a network and transferring usage to the backup when the master fails.” Belford shows that the probability that a site is not available is

$$
U = (1 - a _ {1}) (1 - a _ {2}) (1 - a _ {3}) \dots (1 - a _ {n}),
$$

where the $a$ 's are the availability at each node. The probability that at least one site is still available $A = 1 - U$ . Thus, if the availability of a data base at one site is 0.9, then adding a second site with the same availability results in an overall availability of 0.99, while three such sites have an availability of 0.999.

## 3. Location of multiple copies

Next we have the question: How many copies of the data base should exist in the network? The problem of locating multiple copies of a file has been studied by several research groups. The question of how m copies of a file should be distributed among n nodes requires consideration of the effect of different constraints such as cost, time, communication lines, etc. Chu's [80] formulation, in terms of minimizing the total cost with constraints on response and availability, is one of the earliest studies on this problem. Casey [67] states the model slightly differently; he attempts to minimize the total cost of communication in the network and gives a heuristic solution. A refinement of this approach using tree structures is given by Casey [69], but here again the size of the solution for any real situation is immense. He computes the possible number of link capacity assignment strategies as $\binom{n}{2}^{1}$ and the number of file location strategies as $2^{mn}$ , where n is the number of nodes and m is the number of files. Obviously, this is too large to solve by direct calculation, even though the problem is computationally straightforward. Chandy and Hewes [35] have reformulated Casey's model as an integer programming problem. They show that in solving the integer programming problem, but with the elimination of the integral constraints, that using standard linear programming techniques almost always still yields solutions with integer values. But most of the proposed algorithms involve nonlinear integer programming, and the solutions are not easily computable. Levin [237] and Chandy [74] both provide heuristic solutions, but further study is needed to develop better solutions of these complicated problems. Grapa and Belford [171] have attempted to decrease the size of the problem by applying some theorems which give rules for determining apriori if certain sites should or should not be induced in an optimal allocation.

An extension to the multiple copy problem is to use them for parallel searching and retrieval of data. Ghosh [165] describes this and the properties of the distributions involved. He develops mathematical proofs for algorithms which determine the minimum and maximum number of nodes needed for different types of distributed data storage for parallel searching. These different types of distributed data storage include both redundant and nonredundant data storage.

Little other work addresses the problem of how much of the file should be replicated at each node or how much redundancy should be allowed. Some common sense solutions have been suggested - e.g., storing the data where it originated or where it is most used. Additionally, there has been some theoretical work on locating data base segments to provide technical optimal allocation strategies. Mahmoud and Riordon [258] discuss a model for the allocation of files and communication nodes. They provide a model to allocate copies of files to various nodes and capacities to various lengths such that a minimal cost is achieved subject to network delay and viability constraints. The solution again is a nonlinear integer programming problem. Mahmoud and Riordon provide a heuristic algorithm based on a decomposition technique. This algorithm, although it is not guaranteed to provide optimal solutions, does yield practical, low cost solutions with savings in processing time and the storage requirement.

Loomis [243,244] proposes two models for distributing records based on minimizing transmission and processing time for query and update requests. She shows that if the update traffic is zero, the optimal solution is one copy at each node. And conversely, when the query traffic is zero, the optimum solution is one copy of the data. One of the models is a nonlinear zero-one programming problem. The model is transformed into a constrained linear form which can be solved by linear integer programming techniques. She estimates that the solution set involves a polynomial based on the number of “objects” and the number of nodes. Loomis’ other proposed model is based on cluster analysis. The distribution model is partitioned into subproblems, each formulated to optimize one of the following factors of the whole problem:

"1) Object distribution to provide separation for parallel processing;

2) Object distribution to take advantage of node processing specialization; and

3) Object distribution to reduce transmission times."

Each subproblem is then solved by cluster analysis and the three types of clusters are, themselves, clustered to distribute object copies among the network nodes. The performance of this model is claimed to be optimal.

Alsberg [6] describes the solution proposed for the World-Wide Military Command and Control Systems (WWMCCS) which imposes a cache architecture similar to the IBM 3790 distributed systems. The main host data center has a front-end computer and terminals with intelligent capabilities are connected to it. Partial copies of the files (at the nodes) then provide highspeed query capabilities at the mini front ends; the main storage and central control are retained at the host machine.

## 4. Back-end data base machine

An alternative solution to the location of data in a network is to place it and data management functions at one or more nodes called "back-ends".

The back-end data base machine takes all the data base management functions off the mainframe. Lowenthal's tutorials [248,249] provide excellent sources of general information about back-end data base machines. He defines a back-end data base machine as:

“a semi-autonomous processor which is situated between a computer, called a host, and a complement of secondary storage on which data bases reside. The function of the back end is to provide data base management services on behalf of the host.”

Several authors [62,95,271] have shown, either through simulation or through actual implementation, that back-end base machines provide several useful advantages over current techniques. Some advantages are: improved performance capabilities for the whole system; greater security for the entire system; the back end is capable of screening requests and only passing properly coded and authorized requests to the host; cheaper conversion when changing host computers; use of specialized hardware and software for exclusive data base processing; easier movement of application programs from one host computer to another (the DBMS system does not have to be changed); multiple heterogeneous hosts showing the same data base; and older, smaller hosts may communicate with the latest I/O storage devices (though these hosts would not be able to do so). For example, a PDP-8 interface through a 370 back end would allow the PDP-8 indirectly to utilize 3850 mass storage devices (though PDP-8 was never designed to handle that device). It also allows the back-end to screen every data base request and to continue processing or gracefully recover when the host system fails; then terminals communicating with the host for data requests can be switched to the back end for continued processing while the host is recovering thereby providing better availability of data to the user.

This is, however, merely skirting the real issue of data distribution and is only a temporary (albeit effective) solution. Although locating the data at one node simplifies the data location problems, it can increase the overall cost of the system. There is significantly greater communication overhead between the nodes and a data base machine than if the data were distributed directly at the various nodes. Also, this solution has similar limitations with respect to data availability that a single site does. Even though better than a single site, it still does not have the availability that multiple copies of a data base in a network would have. The back-end machines themselves could be distributed. This improves the data availability limitations but introduces the full garnet of problems that ensue when one distributes a data base. Although dedicating network machines to data base processing allows the aforementioned back-end machine benefits, this still increases the communications overhead of the system.

## 5. Distribution costs

Belford [29,31] describes some mathematical models for distribution of data based on cost of the system, data usage, response time, and availability. There are four different types of models:

1) Response and other time-oriented aspects which deal with time delays

2) Throughput

3) Data availability (the probability that the data base is accessible when needed, including network reliability, system failures, recovery strategies) and 4) Cost of various types of resource utilization There are many different factors involved in cost, such as CPU, storage, access, I/Os, people, etc.

Casey [67] models the cost of network file allocation using the following parameters:

1) Locating (storing) the file at any site

2) Transmitting a fixed known amount of data between two given sites (update and query transaction may have different costs)

3) The volume of update traffic emitted from each site, and

4) The volume of query traffic

His work gives a first approximation to transmission costs.

## 6. Synchronization

Even assuming that the data can be distributed, there are still the problems of deadlock, synchronization, and recovery of multiple files. There are many articles on single site solutions to these problems, but known solutions to multiple site problems are limited. Multiple sites require consideration of questions such as central control, time delay, and resiliency. Alsberg [5] describes the nature of these problems, proposes some solutions to them, and has developed a model to simulate their action. Mahmoud and Riordon [254,260] in a pair of papers describe various software controlled access schemes for distributing data bases. They discuss the various control, deadlock, and critical race conditions which arise when software controlled access methods exist. They propose two different types of software controlled access schemes, one centralized and one distributed. Centralized control is shown to be more efficient whenever perfect reliability is assumed. They describe a control scheme with a center of control which can shift its location to adapt to the failure of network elements and then evaluate each model using a number of performance criteria. These models are used to demonstrate the effectiveness of their proposals to handle critical race conditions, allocation of file resources with local and remote user processes, and results of various queuing algorithms on deadlock situations.

Donnelley [111] proposes using a Transaction Controller for scheduling computer resources. This Transaction Controller handles all data requests from application programs and automatically dials any node. The controller determines whether full files, partial files, or results are to be transferred; it also determines which nodes have the data to satisfy the application requests. The controller has a capability list (C-list) operating system to ensure that all resource calls serviced outside to process domain are by a single invocation of a capability mechanism. Synchronization and deadlock is mostly discussed in the section of the single processor solution. Dykstra's paper [118] discussing P and V operations on semaphores is a classic. P and V are "indivisible operations" (i.e., they are implemented in an inseparable, uninterruptible fashion). One semaphore (S) is used with these operations. Each process precedes its critical section with $P(S)$ and follows it with $V(S)$ . $P(S)$ decreases the value of the semaphore by one and the process is only allowed to proceed if the resultant value is nonnegative when the process is blocked and placed on a waiting queue. $V(S)$ increases the value of S by one and if any processes are waiting, the next one is removed from the queue and permitted to proceed. This scheme guarantees that no more than a fixed number of concurrent processes are in their critical phase at any time [5].

## 7. Multi-site synchronization

For multi-site synchronization, Lamport [226] describes a solution to a problem of synchronizing a number of processors, each running cyclic programs with two parts, one critical and one noncritical. Alsberg and Day [9] propose a resiliency protocol scheme: the basic approach is to have at lease two hosts aware of an action before it is allowed to proceed.

Grapa [170] discusses three models for handling the synchronization of updates in a distributed environment - Johnson's [202,203], Bunch's [58], and the Reservation Center Model [170]. Johnson's model utilizes a five-element vector $(t,v,f,ct,t)$ where:

$l$ is a selector (or location)

v is the associated value

f is the deletion flag

ct is the creation time stamp

t is the time-stamp of the last operation which modified the entry.

The time-stamp components are used to synchronize updates.

Bunch's model uses a primary or central control for all the updates. All messages are sent to the primary and then transmitted to each of the other (backup) sites.

The Reservation Center model utilizes a facility which issues sets of tickets $(S_{tj})$ to each data base manager. The data base manager takes a ticket out of its set and attaches it to each update. This ticket number is broadcast with the update to other node copies and is used to synchronize the order of the updates. Johnson's model is shown to be a subset of this latter model.

Thomas [406] describes a similar mechanism which does not guarantee that the data base copies will be identical at any given time, but that they will be reconciled upon the cessation of update activity. After an application process (an AP) initiates an update request, all the data base managers (DBM) vote, thereby rejecting or deferring a request: if a majority of the DBM's accept a request, then each DBM is notified to perform the update; otherwise, a detailed set of procedures determine the result of the request. The AP can ask that a rejected request be revoked.

## 8. Deadlock

Deadlock occurs when several processes may mutually block each other from further progress, while holding a resource needed by others; e.g., if process $P_{1}$ has resource $r_{1}$ and process $P_{2}$ has resource $r_{2}$ then if $P_{1}$ requests $r_{2}$ and $P_{2}$ requests $r_{1}$ , a deadlock condition occurs. This situation is the classic “deadly embrace.”

Coffman [35] formalized the study of deadlock conditions by setting down four criteria for deadlock conditions:

1) mutual exclusion;

2) wait for;

3) no preemption;

4) circular wait:

Habermann [177] presents an algorithm for detecting and avoiding deadlocks. He requires a statement of resources in advance and utilizes matrices for the solution of deadlock problems. He examines a request in terms of existing requirements and determines whether granting that request could cause a deadlock.

Holt [188,189] describes some problems with Habermann's algorithm, especially with respect to permanent blocking. He then proposes a graphical method to prevent this. He further defines the concepts of reusable and consumable resources and proposes an algorithm to handle them.

Shemer and Collmeyer [372] attempt to quantify the frequency of deadlocks in a system by simulating deadlock conditions. They define a simulated deadlock as occurring when a process attempts to lock a process already held by a blocked process. Even with their “worst case” situation, they found that “unless the operating system is atypical (e.g., 20 concurrent data base users in a 100 group data base with 70% of the users being WRITERS),” the frequency of deadlock occurrence becomes very small. Goldman [167] describes a method for detecting deadlocks in a computer network and reviews existing research. Alsberg [5] provides a survey and tutorial on synchronization and deadlock. He provides a summary of various proposed solutions.

## 9. Backup and recovery

There has been little research on backup and recovery in the distributed environment. Belford [30] discusses backup data bases on a network with respect to data base availability. She is concerned with improving the probability that a copy of a data base will be available for use by the network when needed. Very little consideration is given to how to recover these multiple copies.

Chandy et al. [74], describes rollback and recovery of a file of data base systems with an audit trail. He utilizes checkpoints which are copies of the entire data base for accomplishing this. He develops three models for rollback and recovery of a system handling a stream of transactions. Each model has the following assumptions.

1) The detection of faults occur at random times.

2) The time required to reprocess the audit trail from a checkpoint is assumed to be directly proportional to the number of transactions recorded on the audit trail since that checkpoint.

3) Transactions which arrive when the system is either checkpointing or recovering from an error are stored until the checkpointing or recovery is complete. The time required to process stored transactions is assumed to be small compared to MTBF (Mean-Time-Between-Failures).

4) System availability given optimal checkpointing

strategies is assumed to be high.

Given these assumptions, he develops formulas based on various restrictions of the environment which enable one to determine the optimal intercheckpoint time, the maximum recovery time, and cost of recovery given optimal checkpointing. He discusses the extension of his models to a multiple data base environment and concludes that a more detailed model is necessary to handle the interdependency of the multiple data bases. However, his models are adequate as a first approximation, and he is currently studying the application of his models to the Air Force Logistics System. His models, however, do not consider communication time delays nor synchronization between multiple copies.

Morgan and Taylor [293] survey the reliability and availability of computer networks, including research on the causes of failure in a network, how to prevent failures through the use of communication protocols, methods of detecting and diagnosing failures, and the correction and recovery of errors. Some mention is made of error detection in a distributed environment, but their emphasis is at the communication or processor level.

Maryanski and Fisher [270] present a methodology for recovering distributed data bases. They propose a selective mechanism which recovers only the failing task and those tasks which used data items modified by it. This mechanism uses a “potential shared data list” which is formed when each new sub-schema is created and stored at each processing node.

When a host processor determines that an application has terminated abnormally, it notifies all the processors for that task that rollback must occur and provides the task name, its initiation time, its potential shared data list, and a list of its areas which are open for update. Then, each processor rolls back the file from that point using its log file. In addition, they propose the use of noncritical and critical data items to eliminate some of the recovery traffic. Only those data items which have been identified as critical would be rolled back. They do not, however, handle the recovery of multiple copies of files in a network.

## 10. Data transfer

The problem of data transfer includes questions of data translation, data protocols and the description of transferred data, the volume of data to be transferred, and communication system protocol. Data transfers also involves questions of whether full files, partial files, records, summaries, or individual data items should be transferred, and finally security.

Aschim [14] provides an excellent summary of the problems of transferring data from one system to another. First, there is the problem of different word lengths (e.g., the PDP-11 uses 16-bit word, the IBM 370 has 32-bit, etc.). Translation of data may require proper alignment on word boundaries. In addition, the internal character set representation may be different (EBCDIC versus ASCII) or the control characters may vary from one machine to another.

Fry [157] discusses data translation methodology including the data conversion and restructuring problem. He describes a twostep approach:

1. The user specification of necessary data descriptions.

2. The execution of a data translator based on these descriptions.

This approach is implemented with a "Reader," "Restructurer," and "Writer." The tasks take the source data base, translate it (according to the user specifications) to an internal form, and then to the target data base.

Bonczek [47] proposes a similar technique. He describes a generalized mapping language whereby a user defines a map which defines the translation from one data base structure to another. This map is stored and used by the translator as needed. The target data base can be created from multiple source data bases with the use of this mapping language. Given enough information, these mapping structures can be generated automatically. A data dictionary is used to identify the location of any data item in the network as well as standard data identification functions. Full file transfer protocols exist on a number of current networks. The ARPA File Transfer Protocol [208] is well defined; Boeing [46] has defined a protocol for the transfer of engineering data between their labs. ARPANET also has an experimental File Access Protocol [105] which considers the question of addressing and retrieving individual data items within a file.

An extension to the ANSI Z39.2 standard has been proposed to facilitate data transfer [55]. Although this extension is a magnetic tape proposal, a modification of it could be applied to nonhomogeneous computer networks. Basically, it encompasses existing standards plus has a model for structured fields which permits a definition of different structures for each field. A data base structure is employed to identify each logical record with pointers and tags used to identify higher level elements in the structure. One important feature of this proposed standard is a data base designation file which permits a predefined subsystem to be invoked. If so desired, this subsystem can view data on a field-by-field basis which allows the identification of a specific type of structure out of the many different allowable structures.

## 11. Dictionary schemes

To handle the transferral of individual data items, a number of different dictionary/directory schemes have been proposed. Aschim [14] provides a classification scheme for networks according to the geographical location of the files and the directories which describe the various types of directory schemes available in a network. A hierarchical naming scheme has been proposed for the ARPANET [92]. This type of scheme uniquely describes a resource location as each part of the composite name makes the reference more specific.

Healy, et al [182], propose a tree structure of naming the file. Each name consists of two parts; the name of a directory and the name of an entry in that directory. Since each entry name could be a directory name, a recursive procedure can be set up. Thus, a tree structure is formed from the sequence of names starting from the root name. This procedure is just a generalized extension of that proposed for the ARPANET [105].

Chu [83] develops mathematical models for three types of file directory systems: centralized, local, and distributed. A number of different parameters are used including costs for communication, storage and code translations, query and update rates, directory size, and response time. He finds that the operating cost of a file directory depends significantly on the query and update rate. He supports Loomis' findings that as the query traffic decreases, the optimal placement is a centralized directory and as the update traffic decreases (with respect to the query traffic), that a distributed directory becomes more optimal. He gives percentage breakdowns of when each type of directory system should be used.

Farber and Heinrich [133] use an one-level non-hierarchical naming scheme. They utilize a cataloging scheme whereby a “central component” process is used to associate user file names with catalog names. A “volume process” is used to search a particular volume for a file.

The NAVLIS [306] system uses a data dictionary/ directory of all data items stored at each node. The dictionary is used to identify the location and name of each data item. The directory (called a File Content Directory) was first used to determine which data bases (called "candidate") at which nodes could satisfy the query. Then the query is sent only to sites at which these "candidate" data bases reside. At these nodes, an inverted file would be used to determine whether the required values for that query are present in the data base. A synonym resolution capability was provided to overcome the lack of data element name standardization between and within data bases, it enabled the user to phrase the query in a familiar nomenclature and still ensure that the query names would be translated as appropriate at other nodes. A number of other systems also utilize a centralized data dictionary to handle the problem of finding remotely stored data.

IBM's DMS/3790 [197] function allows a user program to access data by looking up the segment name in a predefined table and either retrieve the data directly (if it is stored locally) or pass a request to the host. This is just another very redimentary application of the data directory concept.

Digital Equipment Corporation's DECNET $^{(R)}$ provides different levels of protocol for transferring or accessing data. DDCMP is the line management protocol, and the Data Access Protocol provides for data file access and transfer protocol. "User programs on the local IAS system may make requests for input-output operations at remote systems which are serviced by DAP and the file system at the remote node. User programs on remote systems may request I/O operations to be performed at the local IAS system. Such requests are serviced by the local DAP handler and the local file control services (FCS on IAS)". [108].

## 12. Applications

There are a number of experimental distributed data base systems which have shown varying degrees of success. The University of California Distributed Computer System [136] is operational. This system uses a ring network and is process oriented, Control is distributed throughout the network; i.e., there is no central controller. Resources are treated as processes; each resource is associated with a process, and all use of that resource is through the associated process. Resource allocation is through the process management mechanism. Each resource allocation bids on services desired by a user. Load balancing is achieved through the bid process: a processor with unused capacity will return a low bid, whereas a busy processor will return a high bid. The file control system is also distributed [133] and is controlled by a series of modules distributed over several processors. All files retain their fully qualified global names. A cataloging scheme is used to access the files, though access to the files could be obtained by searching the volume table of contents. Both the catalog searching and volume searching are once again processes and are controlled by the process manager.

At the University of Waterloo, a distributed medical data base [77] was built which utilizes PDP-11's and the UNIX operating system. It utilizes a "virtual user machine" concept. The user builds a request in which is passed to a "Network Access Machine" (NAM) and subsequently to a "File Machine" (FM) for final processing. The NAM provides all the protocol and logic needed to decide which messages are sent to what node. The FM processes all queries against the appropriate data bases passed to it by the NAM. There exists one EAM and one FM to a node with the virtual machine being unique to each.

A number of users describe back-end data base systems which have been implemented. Maryanski et al. [271], describe one implementation utilizing a CODASYL based system. Canaday [62] in a classic article described the implementation of a data base management system on a Digital Scientific Meta FM machine. ARPANET has one node which contains the Data Computer provided by Computer Corporation of America as back-end data base [265]. Hsiao [192] describes a data base computer being designed and built at the Ohio State University. This is an array processor type machine which has been specially designed for fast query processing. Intel is proposing to build a similar type of data base machine for the commercial market [198].

The NASA Deep Space Network [59] has data bases which are functionally separated but which cross transmit exception reporting. At UC-Berkeley, a file allocation system has been designed and implemented [333]. It provides for sharing of files only by transmission of copies. There is a "Control Monitor" at a particular electronically identified node which controls the rest of the resources and processes; a "Local Monitor" runs at every node (except the control) and is responsible for use access to programs' files and the network.

Sperry Univac has been developing a distributed processing system which also has a central controller called a "System Director" [155]. The System Director is a process, or a number of duplicate processes, utilizing a common system data table that is used for global resource allocation in a distributed system. The System Director examines the process requirements, determines the local node that will execute the process, directs the process to that node, and purges the process from the system when execution is completed and the process is no longer needed.

Hewlett-Packard [107] has designed an automatic control system for interactive computers which utilizes a distributed system. Here again, a centralized node is used for the control of the network and data management functions.

Outside the United States, there are a number of implemented distributed systems using distributed data base techniques. One is the ARAMIS Network [229] in France which provides services to a town, university, and a hospital. This is a fully distributed system utilizing the $\mathbf{ST}_2$ protocol designed for the Cyclades network with SYMBAD and DBMS as the data base management systems used. There are distributed subsystems which control the areas of distributed data. Resource and synchronization packets are shipped to each node cyclically.

The RWS-Data Network [115] was developed for the Water Control and Public Works Department in the Netherlands. It utilizes a central data base with various subdata computers being used for regional processing.

At Elida Gibbs [304], a health and beauty aids company in England, a fully connected network of minicomputers is being linked to a central IBM mainframe. All nodes will employ the TOTAL data base management system. Full DECNET $^{(R)}$ is being used as the internode protocol for file and resource sharing.

Obviously, these are not all the applications of distributed data base which have been developed. But they are some of the more interesting and are meant to give a flavor of the many varied types of applications which have been implemented using distributed data base technology.

## 13. Summary

This article contains a general summary of some of the problems and research results connected with distributed data bases. It was intended to provide a guide to the reader through the mechanism of a bibliography containing in-depth discussion of various areas of interest.

Although much research is currently being conducted in this field, further research is needed in:

1) The allocation data throughout the network, especially the question of redundancy.

2) Synchronization, deadlock, and research schemes with special reference to the communications time-lag and cost problems of various schemes.

3) Conversions of data between heterogeneous hardware nodes.

As shown by the size of the bibliography, there is currently much interest in distributed data base technology. Although much still needs to be done, the existing literature exposes many of the benefits of distributed data base and provides solutions to some of the technical difficulties in utilizing a distributed data base.

4) Improved data location techniques.

The placing of data at multiple nodes in the network, either redundantly or nonredundantly, provides increased data resiliency and availability. It can provide the user with better control over data and increased integrity and validity.

The development and implementation of back-end machines in the commercial, military, and research environment may prove an interim solution to some of the data distribution problems. The principle advantage to the data base machine concept is assumed to be its ability to use single site solutions to the issues of data location, data base recovery, synchronization and deadlock detection and prevention while providing network access to the data. The data base machine may also provide a defacto standard for data storage and transmission, thereby reducing the multiplicity of translocations required in heterogeneous systems. Such an architecture approach may provide effective utilization of current technological advances, such as associate processors and storage hardware.

## Bibliography

[1] P.A. Alsberg, et al., Preliminary Research Study Report, Center for Advanced Computation, University of Illinois, Urbana, May (1975).

[2] P.A. Alsberg, et al., Survey Report, Center for Advanced Computation, University of Illinois, Urbana (May 1975).

[3] P.A. Alsberg, et al., Research Plan, Report No. 164, Center for Advanced Computation, University of Illinois, Urbana (June 1975).

[4] P.A. Alsberg, et al., Synchronization and Deadlock, NTIS, AD-A043 093 (March 1976).

[5] P.A. Alsberg, Synchronization and Resiliency in Network Data Access, Berkeley Workshop on Distributed Data Management and Computer Networks, Berkeley, California (May 1976).

[6] P.A. Alsberg, Data Distribution Strategy, Berkeley Workshop on Distributed Data Management and Computer Networks, Berkeley, California (May 1976).

[7] P.A. Alsberg, et al., Multi-Copy Resiliency Techniques, Report No. 202, Center for Advanced Computation, University of Illinois, Urbana (May 1976).

[8] P.A. Alsberg, et al., Final Research Report, Report No. 210, Center for Advanced Computation, University of Illinois, Urbana (September 1976).

[9] P.A. Alsberg, and J.D. Day, A Principle of Resilient Sharing of Distributed Resources, 2nd International Conference on Software Engineering (October 1976).

[10] J.E. Ames, IV, and D. Foster, Dynamic File Assignment on a Star Network, Computer Networking Symposium (December 1977).

[11] L.W. Amiot, Front-Ending at Argonne National Laboratory, Berkeley Workshop on Distributed Data Management and Computer Networks, Berkeley, California (May 1976).

[12] D.R. Anderson, Data Base Processor Technology, NCC (June 1976).

[13] R.D. Anderson, et al., The Data Reconfiguration Service, An Experiment in Adaptable Process to Process

Communication, Proceedings of Symposium on Problems in the Optimization of Data Communication Systems (October 1971).

[14] F. Aschim, Data Base Networks, An Overview, Management Informatics (February 1974).

[15] R. Ashemy, and M. Adamowicz, Data Base Systems, IBM Systems Journal, No. 3. (1976).

[16] R.L. Ashenhurst, and R.H. Vonderohe, Hierarchical Network, DATAMATION (February 1975).

[17] Auerbach Editorial Staff, What is Network Architecture?, Computer Decisions (June 1976).

[18] D.M. Austin, D.L. Hall, and D. Richards, Berkeley Workshop on Distributed Data Management and Computer Networks, NTIS, LBL-5315 (May 1976).

[19] I.L. Avrunin, IEEE Computer Networks, Trends and Applications, The Navy Laboratory Computer Network (NALCON) (1976).

[20] P. Balays, Minicomputer Networks, Past, Present, Future, Canadian Data Systems (April 1977).

[21] R.M. Balzer, T.E. Cheatham, S.V. Crocker, and S. Warshall, Design of a National Software Works, USC/Information Sciences Institute, ISI-RR-73-16 (1973).

[22] J. Banerjee, D.K. Hsiao, and D.S. Kerr, DBC Software Requirements for Supporting Network Data Base, NTIS, AD-A041 651 (June 1977).

[23] A.E. Bandurski and D.K. Jefferson, Data Description for Computer-Aided Design, NTIS, AD-A020 023 (September 1975).

[24] E.L. Battiste, Portability Assumptions, Proceedings of Workshop on Portability of Numerical Software (June 1976).

[25] R.I. Baum, The Architectural Design of a Secure Data Base Management System, NTIS, AD-A021 158, Ph.D. Dissertation, Ohio State University (November 1975).

[26] R.I. Baum and D.K. Hsiao, Data Base Computers, A Step Toward Data Utilities, IEEE Transactions on Computers, Vol. 25 (April–December 1976).

[27] G.G. Belford, et al., A State of the Art Report, Network Data Management and Related Technology, Center for Advanced Computation, Report No. 150, University of Illinois, Urbana (April 1975).

[28] G.G. Belford, Technological Summary, Center for Advanced Computation, University of Illinois, Urbana (May 1975).

[29] G.G. Belford, et al., Initial Mathematical Model Report, NTIS, AD-A042 894 (August 1975).

[30] G.G. Belford, P.M. Schwarz, and S. Sluisher, The Effect of Backup Strategy on Data Base Availability, NTIS, AD-A042 897 (February 1976).

[31] G.G. Belford, Optimization Problems in Distributed Data Management, Report No. 197, (CCTC-WAD Doc 650) Center for Advanced Computation, University of Illinois, Urbana (May 1976).

[32] G.G., Belford, et al., Network File Allocation, NTIS, AD-A042 898 (August 1976).

[33] J.M. Bell and T. Gunton, A Network-Oriented Mass Storage Facility, Computer Networking Symposium (December 1977).

[34] L.B. Belokrinitskaya, et al., Distribution of Functions Between Central Processor and Peripheral Computer, Automatika and Telemekharika (January 1972).

[35] A.J. Benjamin, Improving Information Storage Reliability Using a Data Network, MIT Lab Computer Science Report MIT/LCS/TM-78 (October 1976).

[36] Bensoussana, Sclingenct. and R.C. Daley, The Multi-Virtual Memory Concept and Design, Communications ACM (May 1972).

[37] D. Bernard, Intercomputer Networks, An Overview and Bibliography, MS Thesis, Moore School of Electrical Engineering, University of Pennsylvania (1973).

[38] M.I. Bernstein, Interactive Systems Research, NTIS, AD-A012 894 (May 1975).

[39] P.A. Bernstein, et al., Analysis of Serializability in SDD-1: A system for Distributed Data Bases (The Fully Redundant Case), Technical Report CCA-77-05, Computer Corporation of America (June 1977).

[40] E.W. Birss, J.E. Donnelley, and J.W. Yeh, Monitor of Distributed Data Systems (MODDS) Part 1, Digest of Functional Specifications, Lawrence Livermore Laboratory, NTIS, UCID-17314 (Part 1) (November 1976).

[41] L.A. Bjork, Recovery Scenario for DB/DC Systems, ACM (1973).

[42] R.P. Planc, Annotated Bibliography of the Literature on Resource Sharing Computer Networks, NBS Special Publication 384 (September 1973).

[43] R.P. Blanc, Review of Computer Networking Technology, NBS Technical Note No. 804 (January 1974).

[44] R.P. Blanc, Assisting Network Users with a Network-Access Machine, ACM (November 1974).

[45] P.R., Blevins and C.V. Ramamoorthy, Aspects of a namely Adaptive Operating System, IEEE Transactions on Computers (July 1976).

[46] Boeing, Common File Structure for Data Transmission, Document D6-44185 (September 1977).

[47] R.H. Bonczek, C.W. Holsapple, and A.B. Whinston, Information Transferral Within a Distributed Data Base Via a Generalized Mapping Language, NTIS, PB-267 343 (November 1976).

[48] G.M. Booth, The Use of Distributed Data Bases in Information Networks, Proceedings of ICC Impacts and Implications (October 1972).

[49] G.M. Booth, The Use of Distributed Data Bases in Information Networks, !CCC (1972).

[50] G.M. Booth, User's Urging Move to Data Base Distribution, COMPWRLD (October 1977).

[51] D. Boylan, DBMS for Mini's Computer Decisions (January 1976).

[52] O.H. Bray, Distributed Data Base Design Considerations, IEEE Computer Networks, Trends and Applications (1976).

[53] O.H. Bray, Data Management Requirements: The Similarity of Memory Management, Data Base Systems, and Message Processing. SIGIR Third Workshop on Computer Architecture for Non-Numeric Processing (May 1977).

[54] O.H. Bray, Data Base Processor: Benefits and Architect-

tural Alternatives, to be Presented IEEE COMPCON (1978).

[55] A.A. Brooks, An Extension of the ANSI Z39.2 Standard to General Information Exchange, Berkeley Workshop on Distributed Data Management and Computer Networks, Berkeley, California (May 1976).

[56] Brown, There Ain't No Free Lunch, COMP DEC (April 1977).

[57] I. Bryan, A Distributed Data Base Management System, NAECON 75.

[58] S.R. Bunch, S.R., Automated Back Up, Preliminary Research Study Report, Center for Advanced Computation, University of Illinois, Urbana No. 162, JTSA No. 5509 (May 1975).

[59] J.P. Buzen, Computational Algorithms for Closed Queuing Networks with Exponential Servers, Communications of ACM, Vol. 16 (September 1973).

[60] J.P. Buzen and P.P.S. Chen, Optimal Load Balance in Memory Hierarchi.s, Proc. IFIPS (1974).

[61] J. Cady, R.M. Sorli, and B.S. Thornton, Performance Evaluation of a Batch Processing Computer Network Under Different Processing Strategies, Proceedings of International Symposium on Computer Performance Modeling, Measurement, and Evaluation (March 1976).

[62] R.H. Canaday, e\* al., A Back-End Computer for Data Base Management, Communications of ACM (October 1974).

[63] R.G. Canning, Distributed Data Systems, EPD Analyzer, Vol. 14, No. 6 (June 1976).

[64] R.G. Canning, Network Structures for Distributed Systems, EPD Analyzer, Vol. 14, No. 7 (July 1976).

[65] C. Carr, D. Crocker, and G. Cerf, Host-Host Communication Protocol in the ARPA Network, SJCC (1970).

[66] J.H. Carson, An experimental Distributed Data Base System, NTIS, PB-264 882 (January 1977).

[67] R.G. Casey, Allocation of Copies of a File in an Information Network, SJCC (1972).

[68] R.G. Casey, Design of Tree Networks for Distributed Data, NCC 73.

[69] R.G. Casey, Design of Tree Structures for Efficient Querying, CACM 16 (1973).

[70] P. Cashin, Data Base Interworking, Unpublished Working Paper, National Physical Laboratory, Teddington, Middlesex, England (1974).

[71] D.D. Chamberlin, R.F. Boyce, and I.L. Traiger, A Deadlock-Free Scheme for Resource Locking in a Data Base Environment, Information Processing 74 (North-Holland Publishing Company, Amsterdam, 1974).

[72] D.D. Chamberlin, J.N. Gray, and I.L., Traiger, Views, Authorization and Locking in a Relational Data Base System, NCC 75.

[73] A.N. Chandra, Some Considerations on the Design of Homogeneous Distributed Data Bases, COMPCON 73.

[74] K.M. Chandy, et al., Analytical Models for Rollback and Recovery Strategies in Data Base Systems, IEEE Transaction on Software Engineering (March 1975).

[75] K.M. Chandy and J.E. Hewes, File Allocation in Distributed Systems, Proceedings of International Symposium on Computer Performance Modeling, Measurement, and Evaluation (March 1976).

[76] E. Chang and J. Linders, A Distributed Medical Data Base, Meth. Int. Med. 4 (1974).

[77] E. Chang, A Distributed Medical Data Base, Computer Networks 1 (1976).

[78] A.S. Chandler, et al., Report of the Higher Level Protocol Working Group, INWG Note No. 6 (1974).

[79] P.P.S. Chen, Optimal File Allocation in Multi-Level Storage Systems, AFIPS 42 (1973).

[80] W.W. Chu, File Allocation in a Multiple Computer System, IEEE Transactions on Computers, C-18 (10) (1969).

[81] W.W. Chu, Optimal File Allocation in a Computer Network, Computer Communication Networks, Editor N. Abrams, and F.F. Coo, Prentice Hall (1973).

[82] W.W. Chu, and G. Ohlmacher, Avoiding Deadlock in Distributed Data Bases, ACM (1974).

[83] W.W. Chu, Performance of File Directory Systems for Data Base in Star and Distributed Networks, NCC (1976).

[84] CODASYL, Data Base Task Group Report (April 1971).

[85] E.G. Coffman, M.J. Elphick, and A. Shoshani, System Deadlocks Computer Surveys (June 1971).

[86] F. Cohen, Alerters on Network Data Bases, NTIS, AD A037 438 (December 1976).

[87] W.W. Collier, Asynchronous Interactions on Shared Data, IBM SIGOPS (1974).

[88] R.E. Conn, R.E., Resource Sharing Computer Networks, Proceedings of IEEE (November 1972).

[89] I.V. Cotton, I.V., Network Management Survey, NBS Technical Note 805 (February 1974).

[90] G. Cowan, Jr., Management of Resources in a Potentially Hostile Environment (Logical and Physical), Ph.D. Thesis, University of Wisconsin, Madison (1975).

[91] J.M. Crammer, Jr., and D.R. Fitzwater, The Architecture of a Machine Independent Network Operating System for Hierarchical Delegation of Authority, Doctorial Study Program, NTIS, AD-A033 888 (October 1976).

[92] D. Crocker, Network Standard Data Specification Syntax, RFC 645 (1974).

[93] S. Crocker, Host Software, RFC, NIC No. 4687 (April 1969).

[94] S. Crocker, et al., Function Oriented Protocols for the ARPA Network, SJCC (1972).

[95] J. Cullinane, et al., Commercial Data Management Processor Study, NTIS, AD-A035 790 (December 1975).

[96] L.M. Culpepper, Network Models: A Survey, NTIS, AD-A041 716 (December 1975).

[97] Dalal, Y.K., Distributed File Systems, Berkeley Workshop on Distributed Data Management and Computer Networks, Berkeley, California (May 1976).

[98] B.P. D'Ambrosio, Design Studies for an On-Line U.C.

Library Catalog Network, Proceedings Second Berkeley Workshop on Distributed Data Management and Computer Networks (May 1977).

[99] Data Computer Project, Data Language, Working Paper No. 3, Computer Corporation of America (October 1971).

[100] Data Computer Project, Further Data Language Design Concepts, Working Paper No. 8, Computer Corporation of America (December 1973).

[101] Data Computer Project, Data Computer Version 0/11 User Manual, Working Paper No. 10, Computer Corporation of America (December 1974).

[102] Data Reduction and Computing Group, Centralization/Decentralization of Computer Facilities, White Sands, NTIS, AD-A040 252 (January 1975).

[103] C.J. Date, An Introduction to Date Base Systems, Addison-Wesley (1975).

[104] C.T. Davies, Recovery Semantics for a DB/DC System, ACM (1973).

[105] J. Day, Proposal for File Access Protocol, RFC 520 (1973).

[106] J.A. Day, Proposed File Access Protocol Specification, Center for Advanced Computation, University of Illinois, Urbana (June 1975).

[107] S. Dicky, Data Management Within a Transparant Distributed Computer System Development for a FORTRAN User, Advanced Instruction, V29. 14 (1974).

[108] Digital Equipment Corporation, Digital Software Product Description: IAS Network Software, DEC-11-XPDCK-A-D (April 1975).

[109] J.E. Donnelley, A Distributed Capability Computing System, Lawrence Livermore Laboratory, Report UCRL-77800 (1976).

[110] J.E. Donnelley, Extendable Information Formats, Berkeley Workshop on Distributed Data Management and Computer Networks, Berkeley, California (May 1976).

[111] J.E. Donnelley, Controlling Transactions Between Distributed Computer Resources, Lawrence Livermore Laboratory, NTIS, UCRL-78282 (June 1976).

[112] J.E. Donnelley, A Distributed Capability Computing System, Proceedings of the International Conference on Computer Communication (August 1976).

[113] J.E. Donnelley, Controlling Transactions Between Distributed Computer Resources, Texas Conference on Computing Systems (October 1976).

[114] D.J. DeWitt, Applicability of Micro-Programming in the Translation of Data and Data Base Management Systems, NTIS, AD-A023 614 (June 1975).

[115] M. Drenthen, et al., The RWS-Data-Network Structure, International Symposium Tech., Selective Des. Information (1976).

[116] L.W. Dowdy, Optimal Branching Probabilities and their Relationship to Computer Network Distribution, Ph.D. Dissertation Duke University (1977).

[117] R.F. Dyke, Advantages of a Back End Data Base Man-

agement System to the Civil Service Commission, Texas Conference on Computing Systems (October 1976).

[118] E.W. Dykstra, Cooperating Sequential Processes, Programming Languages, I. Genuys, Editor, Academic Press, New York (1968).

[119] H.C. Ecox, et al., An Experiment in Dedicated Data Management. Proceedings of First International Conference in Very Large Data Bases, ACM 75.

[120] M.J. Eisner and D.G. Severance, Mathematical Technique for Efficient Record Segmentation on Large Data Bases, NTIS, AD-A020 377 (July 1975).

[121] J. Elam and J. Stutz, Some Considerations for the Distribution of a Data Base, NTIS, AD-A035 923 (May 1976).

[122] J. Elam, Some Considerations for the Distribution of a Data Base, ACM-77.

[123] C.A. Ellis, A Robust Algorithm for Updating Duplicated Data Bases, Proc. Second Berkeley Workshop on Distributed Data Management and Computer Networks (May 1977).

[124] J. Emory, et al., A Comprehensive Data Base Access Methodologies Design Guide, NTIS, AD-A041 459 (September 1976).

[125] K.P. Ewaran, Placement of Records in a File and File allocation in a Computer Network, IFIP (1974).

[126] K P. Eswaran, et al., On the Notions of Consistency and Predicate Locks in a Data Base System, IBM Research Report No. RJ1487 (December 1974).

[127] Evaluating and Selection Hardware for Remore Sites: It's no Easy Task, DARAMATION (October 1976).

[128] G.C. Everest, Concurrent Update Control and Data Base Integrity, Data Base Management (North Holland/American Elsevier, 1974).

[129] G.C. Everest, Basic Data Structure Models Explained with a Common Example, Texas Conference on Computing Systems (October 1976).

[130] G.C, Everest, O. Bray, and I. Valters, An Automated Annotated Bibliography on the Specification of Information System Requirements, NTIS, AD-A038 400 (October 1976).

[131] D.J. Farber, Networks: An Introduction, DATAMATION (April 1972).

[132] D.J. Farber, Data Ring Oriented Computer Networks, Computer Networks, R. Rustin Editor (Prentice-Hall, Inc., 1972).

[133] D.J. Farber and F.R. Heinrich, Structure of Distributed Computer System, The Distributed File System, Proceedings ICC, Impacts and Implications (October 1972).

[134] D.J. Farber and K. Larson, Structure of a Distributed Computer System, Communications, Proceedings Symposium on Computer Communications, Network and Teletraffic, Brooklyn Polytechnic (1972).

[135] D.J. Farber and K. Larson, The Structure of a Distributed Computing System, Software, Symposium on Computer Communication Network and Teletraffic,

Sponsored by the Polytech NIC Institute of Brooklyn, New York, Microwave Research Institute (1972).

[136] D.J. Farber, et al., The Distributed Computing System, Proceedings 7th Annual, IEEE Computer Society International Conference (1973).

[137] D.J. Farber, A Ring Network, DATAMATION (February 1975).

[138] J. Farell, The Data Computer, A Network Data Utility, Berkeley Workshop on Distributed Data Management and Computer Networks, Berkeley, California (May 1976).

[139] File Transfer Protocol, ARPA Network, Network Information Center, NIC No. 17760.

[140] P.S. Fisher and F.J. Maryanski, Design Considerations on Distributed Data Base Management Systems, Technical Report TR CS 77-08, Computer Science Department, Kansas State University (April 1977).

[141] D.R. Fitzwater, The Formal Design and Analysis of Distributed Data Processing Systems, University of Wisconsin, Madison, NTIS, AS-A033 888 (October 1976).

[142] D.R. Fitzwater and C.A. Hence, A System for the Formal Definition of Digital Systems, CS Technical Report No. 141, University of Wisconsin, Computer Sciences Department (1971).

[143] D.R. Fitzwater and P.C. Smith, A Formal Definition Universe for Complexes of Interacting Digital Systems, University of Wisconsin, Madison, Computer Sciences Technical Report No. 184 (1973).

[144] J.G. Fletcher, Large Data Base at the Lawrence Livermore Laboratory, Journal of Chemical Information and Computer Science, Vol. 15, No. 1 (1975).

[145] D.V. Foster, File Assignment in Memory Hierarchies, Ph.D. Dissertation, University of Texas (August 1974).

[146] S. Fox, A Multi-Computer Communication System, MS Report, Computer Science Department, Kansas State University (January 1976).

[147] D.J. Fraily, A Practical Approach to Managing Resources and Avoiding Deadlocks, Communications of the ACM (May 1973).

[148] E. Franceschini, An ARPANET Front-End for Large Computers, Berkeley Workshop on Distributed Data Management and Computer Network, Berkeley, California (May 1976).

[149] P. Franchi, Distribution of Functions Between Hosts and Communication Subnetwork, IEEE Computer Networks, Trends and Applications (1976).

[150] H. Frank and W. Chou, Network Properties of the ARP\^Computer Network, Networks, 4 (1974).

[151] R.L. Frank, A Model for a Generalized Data Access Method, NCCC 74.

[152] G.F. Franklin, Implementation and Future Plans for Existing Networks, Berkeley Workshop on Distributed Data Management and Computer Networks, Berkeley, California (May 1976).

[153] T.A. Franks, Use as Front-End, Controller, Text Editor Possible, COMPWRLD, January 1975.

[154] A.G. Fraser, A Virtual Channel Network, DATAMATION (February 1975).

[155] A. Freeman, A Distributed Processing System Control Structure, ACM 77.

[156] D.H. Fredricksen, Describing Data in Computer Networks, IBM Systems Journal No. 3 (1973).

[157] J.P. Fry, R.L. Frank, and E.A. Hersey, III, A Development Model for Data Translation, Proceedings of ACM, SIGFIDET Workshop on Data Description and Access (1972).

[158] J.P. Fry, Distributed Data Bases: A Summary of Research, The University of Michigan, Data Translation Working Paper, DE801 (August 1975).

[159] J.P. Fry and A.G. Merter, Toward the Development of a Data Translation Methodology and Selection of Target Data Base Structures, NTIS, AD-A041 715 (February 1977).

[160] J.P. Fry and E.H. Sibley, Evolution of Data Base Management Systems, Computing Surveys (March 1976).

[161] J.P. Fry, D.P. Smith, and R.W. Taylor, An Approach to Stored Data Definition and Translation, Proceedings of ACM SIGFIDET Workshop on Data Description and Access (1972).

[162] D.L. Fulton, D. Overstreet, and R.T. Thomas, The Design of Minicomputer Network Operating System, IEEE, Computer Networks, Trends and Applications (1976).

[163] A. Fusi, Reel Project: CNS-VM, The Virtual Machine Environment Computer Network Subsystem, IEEE Computer Networks, Trends and Applications (1976).

[164] R.G. Gallager, A Minimum Delay Routing Algorithm Using Distributed Computation, IEEE Transactions on Communications (January 1977).

[165] S.P. Ghosh, Distributing a Data Base with Logical Association on a Computer Network for Parallel Searching, IEEE Transaction on Software Engineering (June 1976).

[166] G. Giannatti, Data Base Integrity, Data Management (May 1974).

[167] B. Goldman, Deadlock Detection in a Computer Network, MIT Masters Thesis (1977).

[168] M.J. Gonzales, Jr., and C.V. Ramamoorthy, Program Suitability for Parallel Processing, IEEE Transactions on Computers (June 1971).

[169] S. Gornstien and D. Claudy, Data Base Reorganization for a Storage Hierarchy, IBM Research Report RC5063 (October 1974).

[170] E. Grapa, Characterization of a Distributed Data Base System, Ph.D., Thesis, University of Illinois, Urbana (1976).

[171] E. Grapa and G.C. Belford, Some Theorems to Aid in Solving the File Allocation Problem, Communications of ACM (November 1977).

[172] J.N. Gray, R.A. Lorie, and G.R. Putzolu, Granularity of Locks in a Share Data Base, Proceedings 1975 Very Large Data Base Conference, Massachusetts (September 1975).

[173] T.E. Gray, Job Control in a Network Computing Environment, Berkeley Workshop on Distributed Data Management and Computer Networks, Berkeley, California (May 1976).

[174] M.J. Grohm, A Model of a Protected Data Management System, NTIS, AD-A035 526 (June 1976).

[175] G.R. Grossman, A Host Front-End Protocol, Berkeley Workshop on Distributed Data Management and Computer Networks, Berkeley, California (May 1976).

[176] G.R. Grossman, An Alternative Front-End Architecture, Berkeley Workshop on Distributed Data Management and Computer Networks, Berkeley, California (May 1976).

[177] A.N. Habermann, Prevention of System Deadlocks, Communication of ACM (July 1969).

[178] A.N. Habermann, Synchronization of Communication Processes, Communication of ACM (March 1972).

[179] S.B. Harvey, The Concept of the Singer World-Wide Compute: Network, COMPCON (1973).

[180] S.B. Harvey, One More Try at FTP, ARPANET Library RFC 691 (June 1975).

[181] J.W. Havender, Avoiding Deadlocks in Multi-Tasking Systems, IBM Systems Journal, 7, No. 2 (1968).

[182] D.C. Healy, E.J. McCauley, and D.A. Wilcox, Experimental Systems Progress Report, NTIS, AD-A042 899 (September 1976).

[183] J.M. Hennings, A Study of Access Control Costs in Data Base Systems, Texas Conference on Computer Systems (October 1976).

[184] T.H. Hinke and M. Schnefer, Secure Data Management Systems, NTIS, AD-A019 201 (November 1975).

[185] L.J. Hoffman, The Formulary Model for the Flexible Privacy and Access Controls, AFIPS Conference Proceedings 39 (1971).

[186] E. Holler, Files in Computer Networks, First European Workshop on Computer Aries, IRIA Frame (May 1973).

[187] B. Holmes, Minicomputer Networks, Past, Present, and Future, TCS Technical Feature (October 1976).

[188] R.C. Holt, Comments on Prevention of System Deadlocks, Communications of ACM (January 1971).

[189] R.C. Holt, Some Deadlock Properties of Computer Systems, Computing (September 1972).

[190] M.D. Hopwood, D.C. Loomis, and L.A. Roe, Design of the Distributed Computing System, Technical Report No. 25, Department of Information and Computer Science, University of California, Irvine (June 1973).

[191] D.K. Hsiao, K. Kannan, and D.S. Kerr, Structure Memory Designs for a Data Base Computer, ACM 77.

[192] D.K. Hsiao and K. Kannan, The Architecture of Data Base Computer, A Summary SIGIR Third Workshop on Computer Architecture, May 1977.

[193] J.J. Hunter, Distributing a Data Base, Computer Decisions (June 1976).

[194] J.J. Hunter, Distributed Data Base Easily Accepted, COMPWRLD (March 1977).

[195] IBM, Introduction to Advanced Communications

Function, GC30-3033-0 (October 1976).

[196] IBM, Advanced Communications Function for VTAM, General Information, GC38-0254-1 (August: 1977).

[197] IBM Display Management System/3790 (DMS/3790) General Information Manual, GH20-2002-0 (August 1977).

[198] Intel Memory Systems, Product Proposal: A Data Base Computer (November 1977).

[199] B.E. Jackson and C.D. Stubbs, A Study of Multi-Access Computer Communications, Proceedings of the AFIPPS, SJCC, Vol. 34 (1969).

[200] J.Q. Jackson, Ship Board Application of a Ring Structured Distributed Computing System, Master Thes. Naval Post Graduate School, Monterey, California (1976).

[201] D.K. Jefferson, Data Base Design, NTIS, AD-A035 945 (June 1976).

[202] P.R. Johnson and M. Beeler, Notes on Distributive Data Bases: Draft Report, Bolt, Berenek, and Newman, Cambridge, Massachusetts (1974).

[203] P.R. Johnson and R.H. Thomas, The Maintenance of Duplicate Data Bases, RFC No. 677, NIC No. 31507 (January 1975).

[204] R.E. Kohn, Resource-Sharing Computer Networks, Proc. IEL E (November 1972).

[205] R. Kanoa, "Some Comments on the Procedure Call Protocol," Project MAC, Massachusetts, Institute of Technology, A Working Paper (1975).

[206] Kelnut, Protocol Specification, NIC 18639 (August 1973).

[207] J. Killeen, A Computer Network, Berkeley Workshop on Distributed Data Management and Computer Networks (May 1976).

[208] S R. Kimbleton, "An Atlantic Framework for Computer Systems Sizing and Tuning," Proceedings of the NBS/ACM Workshop Performance Analysis, San Diego (March 1973).

[209] S.R. Kimbleton, "Network Management Information Center, A Research Program in the Field of Computer Technology," Annual Technical Report, ISI/SR-74-2, USC/Information Science Institute (May 1974).

[210] S.R. Kimbleton, "Modeling Considerations in Computer Communication Resource Control," Proceedings of the 8th Hawaii International Conference on Systems Sciences (January 1975).

[211] S.R. Kimbleton, "Computer Communication Networks: Approaches, Objectives, and Performance Considerations," Computing Surveys (December 1975).

[212] S.R. Kimbleton, Network Operating Systems, NCC (1976).

[213] S.R. Kimbleton, A Fast Approach to Network Data Assignment, Proceedings Second Berkeley Workshop on Distributed Data Management and Computer Networks (May 1977).

[214] S.R. Kimbleton and R.L. Mandell, Distributed Computation Study, USC/Information Sciences Institute, NTIS, AD-A034 670 (April 1976).

[215] S.R. Kimbleton and G.M. Schneider, Computer Communications Networks: Approaches, Objectives, and Performance Considerations, Computing Survey (September 1975).

[216] P.F. King and A.J. Collemyer, Data Base Sharing, An Efficient Mechanism for Supporting Concurrent Processes, AFIPS NCC (1973).

[217] K.A. Kirk, A Prototype Ring-Structured Computing Network Using Micro Computers, Master Thesis, Naval Post Graduate School (1973).

[218] L. Kleinrock, Analytic and Simulation Methods in Computer Network Design, Spring Joint Computer Conference, Vol. 36 (1970).

[219] L. Kleinrock, Scheduling Queuing and Delays in Time Shared Systems and Computer Networks, Computer Communication Networks, Prentice Hall (1973).

[220] N.E. Knottek, Selecting a Distributed Processing System, Computer Decisions (June 1976).

[221] D.E. Knuth, Additional Comments on a Problem in Concurrent Programming Control, ACM 9 (1966).

[222] S.R. Kosaraju, Limitations of Dykstra's Semaphore Primitives and Pertrinets, Operating Systems Reviews, 7, ACM (October 1973).

[223] J.F. Kramer, A General Structure for Uncooperative Processes Distributed Over a System Network, Ph.D. Thesis, University of Wisconsin, Madison (1975).

[224] J.R. Kramer and D.R. Fitzwater, The Architecture of a Machine Independent Network Operating System for Hierarchical Delegation of Authority, NTIS, AD-A033 888 (October 1976).

[225] J. Labetoulle and G. Pujolle, A Study of Queuing Networks with Deterministic Service and Applications to Computer Networks, Proceedings of International Symposium on Computer Performance Modeling, Measurement, and Evaluation (March 1976).

[226] L. Lamport, A New Solution of Dykstra Concurrent Programming Problems, Communications of ACM 17 (August 1974).

[227] L. Lampost, Time, Clocks, and the Orderings of Events in a Distributed System, Massachusetts Computer Associates (March 1976).

[228] B.W. Lampson, On Reliable and Extendable Operating Systems, Techniques in Software Engineering, NATO SIISCI, COMM. Workshop Material, Vol. II (1969).

[229] J.P. Lagasse G. Artauel, and J.P. Cabunal, ARAMIS, A Processing Network With User Data Base: Interactive Systems, FA2 COMPCON (1975).

[230] T.E. Lang, B. Fernandez, and R.C. Summers, A System Architecture for Compile-Time Actions in Data Base, ACM 77.

[231] W.M. Lancy, D.L. Mills, and M.V. Selkowitz, Design of a Distributed Computer Network for Resource Sharing, AIAA Computer Networks System Conference, Huntsville, Alabama (April 1973).

[232] W.M. Laney, D.L. Mills, and M.V. Selkowitz, Operating Systems Architecture for a Distributed Computer Network, ACM Conference on Trends and Applica-

tions of Mini Computer Networks, Gathersburg, Maryland (April 1974).

[233] P. LaVoie, Distributed Computing, Systematically, Computer Decisions (March 1977).

[234] D. Lefkovitz, File Structured for On-Line Systems, Sparton Books, New York (1969).

[235] M. Lehman, A Survey of Poblems and Preliminary Results Concerning Parallel Processing and Parallel Processors, Proceedings of IEEE (December 1966).

[236] K.D. Levin and H.L. Morgan, Optimizing Distributed Data Bases, A Framework for Research, NCC (1973).

[237] K.D. Levin, Organizing Distributed Data Bases and Computer Networks, Ph.D. Dissertation, University of Pennsylvania, Tech. Report No. 74-09-01 (1974).

[238] A. Lew, Optimal Ressource Allocation and Scheduling Among Parallel Processes, Parallel Processing: Proceedings 3rd Segamore Computer Conference (August 1974).

[239] W.P. Lidinsky, The Argonne Intra-Laboratory Network, Berkeley Workshop on Distributed Data Management and Computer Networks, Berkeley, California (May 1976).

[240] R.R. Lind, R. Gates, and T. Feng, Associative Processor Applications to Real Time Data Management, AFIPS Conference Proceedings 42 (1973).

[241] J.G. Linders, Distributed Data Bases, Computer and Geoscience, Vol. 2. (1976).

[242] A. Lew, Optimal Resource Allocation and Scheduling Among Parallel Processes, Parallel Processing (Editor T. Feng), Springer-Verlerg, Berlin (1975).

[243] M.E. Loomis, Data Base Design: Object Distribution and Resource Constrained Task Scheduling, Ph.D. Thesis, University of California, Los Angeles (1975).

[244] M.E. Loomis and G.J. Popek, A Model for Data Base Distribution, IEEE Computer Networks, Trends and Applications (1976).

[245] D.E. Lough and A.D. Burns, An Analysis of Data Base Query Language, NTIS, AD-A039 783 (March 1977).

[246] E.I. Lowenthal, The Distributed Data Management Function, Texas Conference of Computing Systems (1974).

[247] E.I. Lowenthal, Computing Systems for the Data Management Function, NCC (1974).

[248] E.I. Lowenthal, The Back-End (Data Base) Computer, Parts I and II. Current Directions in DPM-Development, Auerbach (1976).

[249] E.I. Lowenthal, The Back-End Machine for Data Base Management: A Tutorial, Texas Conference on Computing Systems (October 1976).

[250] E.I. Lowenthal, A Survey, The Application of Data Base Management Computers in Distributed Systems, 3rd Very Large Data Base Conference, Tokyo (October 1977).

[251] H.C. Lucas and L. Presscr, A Method of Software Evaluation, The Case of Programming Language Translators, Computer Journal 16 (1973).

[252] V.Y. Lum, et al., A Cost Oriented Algorithm for Data

Set Allocation in Storage Hierarchies, Communications of ACM (June 1975).

[253] A. Lynch, Distributed Processing Solves Mainframe Problems, Data Communications (November/December 1976).

[254] A. Lynch, Protocols Key to Communications Future, COMPWRLD (September 26, 1977).

[255] J.L. Mack and N.B. Wagner, Secure Multilevel Data Base System, Demonstration Scenario's, NTIS, AD-A032 956 (October 1976).

[256] S.E. Madnick, Design of General Hierarchical Storage System, Report CISR-6, MIT Sloan School of Management (March 1975).

[257] S.E. Madnick, INFOPLEX, Hierarchical Decomposition of a Large Information Management System Using a Microprocessor Complex, NCC (June 1975).

[258] S.A. Mahmoud and J.S. Riordon, Protocol Considerations for Software Controlled Access Methods in Distributed Data Bases, Proceedings of International Symposium on Computer Performance Modeling, Measurement, and Evaluation (March 1976).

[259] S.A. Mahmoud and J.S. Riordon, Optimal Allocation of Resources in Distributed Information Networks, ACM TODS (March 1976).

[260] S.A. Mahmond and J.S. Riordon, Software Controlled Access to Distributed Data Bases, INFOR (February 1977).

[261] A.P. Mallery and R.M. Goldwyn, Considerations in the Design of a Future Data Organization and Data Management for Medical Use, 6th International Symposium on Interface (1972).

[262] R.S. Marcus, A Translation Computer Interface for a Network of Heterogeneous Interactive Information Retrieval Systems, SIGPLAN Notice, Vol. 10, No. 1 (January 1975).

[263] T. Marill, T.E.A. Message System, Berkeley Workshop in Distributed Data Management and Computer Network, Berkeley, California (May 1976).

[264] T. Marill and D. Stern, The Data Computer, A Network Data Utility, NCC (1975).

[265] F.J. Maryanski, Memory Management in Distributed Data Base Systems, Technical Report CS 76-14, Computer Science Department, Kansas State University (October 1976).

[266] F.J. Maryanski, A Survey of Developments in Distributed Data Base Management Systems, Technical Report CS 77-01, Department of Computer Science, Kansas State University (January 1977).

[267] F.J. Maryanski, A Deadlock Prevention Algorithm for Distributed Date Base Management Systems, Technical Report CS 77-02, Computer Science Department, Kansas State University (February 1977).

[268] F.J. Maryanski, Performance of Multi-Processor Back-End Data Base Systems, Technical Report TR CS 77-07, Department of Computer Science Kansas State University (April 1977).

[269] F.J. Maryanski and P.S. Fisher, Language Specifications for Distributed Data Base Management System,

Technical Report, Computer Science Department, Kansas State University (May 1976).

[270] F.J. Maryanski and P.S. Fisher, Rollback and Recovery in Distributed Data Base Management Systems, ACM (1977).

[271] F.J. Maryanski, P.S. Fisher, and V.E. Wallentine, Visibility and Feasibility of Back-End Data Base Management System, Proceedings of 7th Pittsburg Conference on Modeling and Simulation (April 1976).

[272] F.J. Maryanski, P.S. Fisher, and V.E. Wallentine, A User-Transparent Mechanism for the Distribution of a CODASYL Data Base Management System, Technical Report TR CS 76-22, Computer Science Department, Kansas State University (December 1976).

[273] F.J. Maryanski and V.E. Wallentine, A Simulation Model of a Back-End Data Base Management System, Pittsburgh Conference on Modeling and Simulation (April 1976).

[274] F.J. Maryanski, et al., A Mini Computer Based Distributed Data Base System, Symposium on Trends and Applications 1976 Micro and Mini Systems.

[275] F.I. Maryanski, et al., Evaluation of Conversion to a Back-End Data Base Management System, Technical Report CS 76-08, Computer Science Department, Kansas State University (March 1976).

[267] F.J. Maryanski, et al., Distributed Data Base Management Using Minicomputer, Technical Report TR CS 77-22, Computer Science Department, Kansas State University (October 1977).

[277] E.J. McCawley, A Model for Data Secure Systems, NTIS, AD-A011 359 (March 1973).

[278] W.C. McGee, File Level Operations on Network Data Structures Proceedings, 1975 ACM SIGMOD International Conference on Management of Data, San Jose (May 1975).

[279] McKenzie, File Transfer Protocol, NIC 14353 (February 1973).

[280] D.J. McLeod, High-Level Expression of Semantic Integrity Specifications on a Relational Data Base System, NTIS, AD-A034 184 (September 1976).

[281] P.K. Merrill, Computer Netting and Distributed Data, A Tutorial, IBM Tech. Report No. 02-610, IBM Systems Development Division (February 1974).

[282] A.G. Merten and J.P. Fry, A Data Description Language Approach to File Translation, Proceedings ACM-SIGFIDET Workshop (New York, 1974).

[283] H. Merten, Communication With Data Bases, International Conference on Computer Communications (1974).

[284] R.E. Miller, Some Relationship Between Various Models of Parallelism and Synchronization, IBM Research Document RC5074 (No. 22391), IBM Corporation (1974).

[285] D.J. Miller, Deadlock in Distributed Computer Networks, MS Thesis, Department of Computer Science Report UIUCDCS-R-74-619, University of Illinois, Urbana (1974).

[286] D.L. Mills, A Design for a Distributed Catalog System,

Computer Science Technical Report TR-415, University of Maryland (October 1975).

[287] D.L. Mills. An Overview of the Distributed Computer Network, NTIS, AS-A018 734 (October 1975).

[288] D.L. Mills, The Basic Operating System, for the Distributed Computer Network, NTIS, AD-A021 989 (October 1975).

[289] D.L. Mills, Transient Fault Recovery in the Distributed Computer Network, NITS, AD-A022 018 (February 1976).

[296] D.L. Mills, The Distributed Computer Network Project, NTIS, AD-A044 727 (July 1977).

[291] D.L. Mills, M.W. Lany, and J. Belezy, The Virtual Operating System for the Distributed Computer Network Computer Science Technical report, University of Maryland (1977).

[292] M.F. Mitima, Optimal Data Base Schema Design, NTIS, AD-A016 431 (August 1975).

[293] D.F. Morgan, D.J. Taylor, and G. Casteau, A Survey of Methods for Improving Computer Network Reliability and Availability, Computer (November 1977).

[294] H.1. Morgan and O.P. Bunchan, Alerting in Data Base Systems: Concepts and Techniques, NTIS, AD-A037 437 (June 1976).

[293] H.L. Morgan and K.D. Levin, Optimal Program and Data Locations in Computer Networks, Report 74-10-01. Department of Decision Sciences, The Wharton School, University of Pennsylvania, Presented at TIM SXXI International Meeting, San Juan (October 1974).

[296] H.L. Morgan and K.D. Levin, Optimal Program and Data Locations in Computer Networks, Communications of ACM, Vol. 20 (May 1977).

[297] P. Morris and D. Sugalowicz, Managing Network Access to a Distributed Data Base, Proceedings Second Berkeley Workshop on Distributed Data Management and Computer Networks (May 1977).

[298] R. Mulden, An Implementation of Data Management System on an Associative Processor, AFIPS Conference Proceedings 42 (1973).

[299] A.P. Mullery, The Description of Structure and Meaning of I ata, IBM Tech. Report RC 3653 (December 1971).

[300] A.P. Mullery, The Distributed Control of Multiple Copies of Data, IBM Techn. Report RC 5782 (December 1975).

[301] B. Munson and C. Smith, Jr., The study of Data Base Management Systems with Bibliography, Data Base, Vol. 8, No. 2 (Fall 1976).

[302] J.F. Murphy. Resource Allocation with Interlock Detection in a Multi-Task System, FJCC (1968).

[303] J.E. Murphy, Resource Allocation with Interlock Detection in a Multi-Task System, Fall Joint Computer Conference Proceedings, Vol. 33 (1968).

[304] P.A. Murray, Distributed Data Base, One User's Viewpoint, European Total Users Conference (1977).

[305] T.H. Myer and D.W. Dodds, Notes on the Development of Message Technology, Berkeley Workshop on

Distributed Data Management and Computer Networks, Berkeley, California (May 1976).

[306] Navlis Office Staff, Navy Logistics Information Sharing (NAVLIS) Project (Final Report), NTIS, AD-A035 847 (June 1976).

[307] W.M. Neilstein, Works Manager Procedures (DPNB) TXT37, A Working Paper (April 1975).

[308] N. Neigus, File Transfer Protocol, RFC No. 542 (1973).

[309] Networks Still a Challenge to Software, Elec. News, Suppl. (August 1976).

[310] D.D. Novak and J.P. Fry, The State of the Art of Logistical Data Base Design, Texas Conference on Computing Systems (October 1976).

[311] K.A. Ochel, Distributed Data Base Management, Online Network Systems and Data Base Systems Seminar (November 1977).

[312] M.L. O'Connell, Distributed Data Base Covers Range of Forms, Range of Users, CMPWRLD (October 25, 1976).

[313] M.L. O'Connelli, Data Base Machines Relieve CPU's Overhead, COMPWRLD (October 31, 1977).

[314] E.A. Ozharahan, S.A. Schuster, and K.C. Sevcik, Performance Evaluation of Relational Associative Processor, Tech. Report CSRG-65, Computer Systems Research Group, University of Toronto (January 1976).

[315] R. Pardo, M.T. Lin, and G.A. Babiz, Distributed Services in Computer Networks: Designing the Distributed Loop Data Base System (DLDBS), Computer Networking Symposium (December 1977).

[316] S.S. Patill, Limitations and Capabilities of Dystra's Semaphore Primitives for Coordination Among Processes, Project MAC Memo No. 57, Massachusetts Institute of Technology, Cambridge, Massachusetts (1971).

[317] J.J. Passatiume and S. Weeker, Distributed File Access in DECNET. Proceedings Second Berkeley Workshop on Distributed Data Management and Computer Networks (May 1977).

[318] R. Peoples, Design Considerations for a Distributed Data Access System, Ph.D. Dissertation, Moore School of Electrical Engineering, University of Pennsylvania, NTIS AD-775 569 (May 1973).

[319] Peran, F.D.A.R., Dynamic File Allocation in a Computer Network, NTIS, AD-A031 608 (June 1976).

[320] M. Pliner, L. McGowan, and K. Spalding, A Distributed Data Management System for Real-Time Applications, Proceedings Second Berkeley Workshop on Distributed Data Management and Computer Networks (May 1977).

[321] J.C.T. Poole, Mathematical Software in the Network Environment, Berkeley Workshop on Distributed Data Management and Computer Networks, Berkeley, California (May 1976).

[322] J.B. Postell, Survey of Network Control Programs in the ARPA Computer Network Mitre Technical Report No. 6722, Revision 1, Mitre Corporation, McLean, Virginia.

[323] J.B. Postell, National Software Works Protocols, Augmentation Research Center, Stanford Research Institute, Menlo Park, California (1975).

[324] J.B. Postell, Consistent Access to Programs, Berkeley, Workshop on Distributed Data Management and Computer Networks, Berkeley, California (May 1976).

[325] J.B. Postell, Front-End/Back-End Split Programs, Berkeley Workshop in Distributed Data Management and Computer Networks, Berkeley, California (May 1976).

[326] J.B. Postell, L.L. Garlick, and R. Rom, Terminal-To-Host Protocol, NTIS, AD-A035 338 (July 1976).

[327] L. Pouzin, Presentation and Major Design Aspects of the Cyclades Computer Network, 3rd Data Communications Symposium (1973).

[328] B. Purhami, A. Highly Parallel Computing System for Information Retrieval, SJCC (1972).

[329] C.V. Ramamoorthy, K.M. Chandy, and M.J. Gonzales, Jr., Optimal Scheduling Strategies in a Multiprocessor System, IEEE Transactions on Computers (February 1972).

[330] C.V. Ramamoorthy and M.J. Gonzalez, A Survey of Techniques for Recognizing Parallel Processable Streams in Computer Programs, FJCC (1969).

[331] J.A. Ramirez and D.R. Richards, Representations on Hierarchically Structured Data in a Proposed ERDA Exchange Standards, Berkeley Workshop on Distributed Data Management and Computer Networks, Berkeley, California (May 1976).

[332] J.A. Ramirez, N.A. Rin, and N.S. Prywes, Automatic Generation of Data Conversion Programs Using a Data Description Language, Proceedings of 1974 SIGMOD Workshop on Data Description, Access and Control (May 1974).

[333] C.V. Ravi, A Distributed File System, ACM (1975).

[334] A. Reiter, Some Experiments on Directory Organization, A Simulation Study, NTIS AD-A022 750 (December 1975).

[335] A. Reiter and B. Finkel, Simulating a Virtual Machine, NTIS, AD-A027 894 (May 1976).

[336] D.L. Retz, Elf, A System for Network Access, Access to Computer Networks, IEEE Intercom (April 1975).

[337] L.B. Roberts, Access Control and File Directories in Computer Networks, Proceedings 4th Annual IEEE Intercom (March 1968).

[338] L.G. Roberts and D.T. Wessler, Computer Networks, Development to Achieve Resource Sharing, SJCC (1970).

[339] L.L. Rose and M.H. Gotterer, A Theory of Dynamic File Management in a Multilevel Store, International Journal of Computer and Information Sciences, Vol. 2, No. 4 (December 1973).

[340] L.L. Rose and M.H. Gotterer, An Analysis of File Movement Under Dynamic File Management Strategies, Bit, Vol. 15, 3 (1975).

[341] L.L. Rose, M.H. Gotterer, and J.C. Hayya, A Simulation Model for Dynamic File Management, Proceedings

of the Winter Simulation Conference (1974).

[342] D.J. Rosenkrantz, R.E. Sterns, and P.M. Lewis, A System Level Concurrency Control for Distributed Data Base Systems, Proceedings Second Berkeley Workshop on Distributed Data Management and Computer Networks (May 1977).

[343] R. Rosenthal, The Distributed Data Base Concept, Proceedings of Guide 35 (November 1972).

[344] R. Rosenthal, Accessing On-Line Network Resources for the Network Access Machine, IEEE Intercom (1973).

[345] R. Rosenthal, Accessing On-Line Network Resource with a Network Access Machine. IEEE Intercom (1975).

[346] R. Rosenthal, An Evaluation of a Back-End Data Base Management Machine, Proceedings of the Annual Computer Related Information Systems Symposium, US Air Force Academy (1977).

[347] R. Rosenthal, The Data Management Machine, A Classification, SIGIR, Third Workshop on Computer Architecture for Non-Numeric Processing (May 1977).

[348] J.A. Rothnie and N. Goodman, An Approach to Updating i. a Redundant Distributed Data Base Environment, Computer Corporation of America, CCA-77-01 (February 1977).

[349] J.A. Rothnie and N. Goodman, An Overview of the Preliminary Design of SDD-1: A System for Distributed Data Bases, Proceedings of Second Berkeley Workshop on Distributed Data Management and Computer Networks (May 1977).

[350] J.A. Rothnie, N. Goodman, and P.A. Bernstein, The Redundant Update Methodology of SDD-1: A Systems for Distributed Data Bases (The Fully Redundant Case), Technical Report CCA-77-02, Computer Corporation of America (June 1977).

[351] J.A. Rothnie and N. Goodman, A Survey of Research and Development: in Distributed Data Management, Proceedings of the 3rd International Conference on Very Large Data Bases, Tokyo, Japan (October 1977).

[352] L.A. Rowe, The Distributed Computing Operating System, Technical Report No. 66, Department of Information and Computer Science, University of California, Irvine (June 1975).

[353] L.A. Rowe, M.D. Hoppwood, and D.J. Parker. Software Methods for Achieving Fail-Soft Behavior in a Distributed Computing System, IEEE Symposium on Computer Software Reliability (April 1973).

[354] L.A. Rowe, M.D. Hopwood, and D.J. Farber, Fail-Soft Behavior in the Distributed Computer System, IEEE Symposium on Computer System Reliability, New York, (1973).

[355] R.M. Russell, Approaches to Network Design, Computer Decisions (June 1976).

[356] W.E. Rzepka, Considerations in the Design of a Secure Data Base Management System, NTIS, AD-A039 169 (March 1977).

[357] E. Sacerdoti, Language Access to Distributed Data

with Error Recovery, Fifth International Joint Conference on Artificial Intelligence, Cambridge, Massachusetts (August 1977).

[358] A. Salako, A Locality Model for File Structure Organization, Conference on Information Sciences and Systems (March 1976).

[359] R. Schantz and B. Thomas, Distributed Computation and Tenex-Related Activities, NTIS, AD-A037 596 (March 1977).

[360] G.M. Schneider, DSCI, A Data Specification and Conversion Language for Networks, Proceedings of ACM SIGMOD Workshop, San Jose, California (May 1975).

[361] 3. Schneiderman, Bibliography on Data Base Structures, Data Base, Vol. 4 (Winter 1972).

[362] D.E. Schultz, Interim Report on the HELPER Project, Los Alamos, NTIS, LA-6470-MS (August 1976).

[363] S.A. Schuster, E.A. Ozkarahlen, and K.C. Smith, The Case for a Parallel-Associative Approach to Data Base Machine Architecture, Berkeley Workshop on Distributed Data Management and Computer Networks, Berkeley, California (May 1976).

[364] A. Segall, Dynamic File Assignment in a Computer Network, Part 2: Random Rates of Demand, MIT, IEEE Transactions on Automatic Control (February 1975).

[365] A. Segall, Dynamic File Assignment in a Computer Network, Part 1: Deterministic Parameters, MIT, IEEE Transactions on Automatic Control (1975).

[366] A. Segall, Dynamic File Assignment in a Computer Network. IEEE Transactions on Automatic Control (April 1976).

[367] W.V. Selkowitz, Simulation and Implementation of Computer Networks, Proceedings 13th Annual ACM Washington Chapter Symposium (June 1974).

[368] E.H. Sensikath, Jr., The Use of Tree Structures for Processing Files, Communications ACM 6 (1963).

[369] M.E. Senko, Data Structures and Data Accessing on Data Base Systems. Past, Present, Future, IBM Systems Journal No. 3 (1977).

[370] E.F. Severino, Data Bases and Distributed Processing Computer Decisions (March 1977).

[371] A.C. Shaw, The Logical Design of Operating Systems, Prentice Hall, Inc. (1974).

[372] J.E. Shemer and A.M. Collmeyer, Data Base Sharing: A Study of Interference, Roadblock, and Deadlock, Proceedings ACM SIGFIDET Workshop on Data Description, Access and Control (1972).

[373] J.T. Shen, Multi-Level Security for Computer System Networks, A Survey and Discussion, NTIS, AD-919 838L (May 1974).

[374] A. Shoshani, Data Sharing in Computer Networks, Wescon Conference (September 1972).

[375] A. Sheshani, A Logical-Level to Data Base Conversion, Proceedings of ACM, SIGMOD International Conference on Management of Data (May 1975).

[376] A. Shoshani, On the Importance of Common Standards for Logical Structures, Data Formats and Query

Langauges, Berkeley Workshop on Distributed Data Management and Computer Networks, Berkeley, California (May 1976).

[377] A. Shoshani and A.J. Bernstein, Synchronization in a Parallel Access Data Base, Communications of ACM 12 (No. 11) (November 1959).

[378] A. Shoshani and I. Spiegner, Integration of Data Management Systems on a Computer Network AIAA Computer Network Systems Conference (April 1973).

[379] N.C. Shu, B.C. Housel, and V.Y. Lum, CONVERT: A High-Level Translation Definition Language for Data Conversion, Communications of ACM (October 1975).

[380] N.C. Shu, V.Y. Lum, and B.C. Housel, An Approach to Data Migration in Computer Networks, Berkeley Workshop on Distributed Data Management and Computer Networks, Berkeley, California (May 1976).

[381] E.H. Sibley and R.W. Taylor, A Data Definition and Mapping Language, Communications of ACM, 16 (1973).

[382] D.P. Smith, A Method for Data Translation Using the Stored Data Definition and Translation Tasks Group Languages, Proceedings of ACM Workshop on Data Description and Access (1972).

[383] P.C. Smith and D.R. Fitzwater, Efficient Analysis of the Process Structures of Formally Defined Complexes of Interacting Digital Systems, University of Wisconsin, Madison, Computer Sciences Technical Report No. 219.

[384] M. Somia, Synchronization Problems in a Computer Network International Computer Symposium, A. Gunther, Editor, North Holland (1973).

[385] P.B. Snyder, Redundant Ring Structures for Shipboard Distributed Computer Systems, NTIS, AD-A035 886 (December 1976).

[386] R.D. Spinetto, A Facility Location Problem, Siam Review (April 1976).

[387] P.M. Spira, Communication Complexity of Distributed Minimum Spanning Tree Algorithms, Proceedings Second Workshop on Distributed Data Management and Computer Networks (May 1977).

[388] A.E. Stansell, Optimal Trees for a Class of Information Retrieval Problems, Information Storage Retrieval 9 (1973).

[389] J.E. Stemer and A.E. Collmyer, Data Base Sharing, A Study of Interference Rollback and Deadlock, Proceedings ACM SIGFIDET Workshop (1972).

[390] D.M. Stemple, A Data Base Management Facility for Automatic Generation of Data Base Managers, ACM TODS (March 1976).

[391] H.S. Stone, Multiprocessor Scheduling with the Aid of Network Flow Algorithms, IEEE Transactions on Software Engineering, Vol. SE-3, No. 1 (January 1977).

[392] M. Stonebreaker, Proposal for a Network INGRES, Berkeley Workshop on Distributed Data Management and Computer Networks, Berkeley, California (May 1976).

[393] M. Stonebreaker and E. Neuhold, A Distributed Data

Base Version of INGRES, Proc. Second Berkeley Workshop on Distributed Data Management and Computer Networks (May 1977).

[394] S. Su and H. Lam, A Semi-Automatic Data Base Translation System for Achieving Data Sharing in a Network Environment, Proceedings of the ACM SIGMOD Workshop (May 1974).

[395] I.C. Summers, E.B. Fernandez, and C.D. Coleman, Shared Data Access Controls with Programming Language Support, Proceedings 8th Hawaii International Conference on Systems Sciences, Western Periodicals Company (1975).

[396] C. Sunshine, Issues in Communications Protocols Design, Formal Correctness, INWG Protocol No. 5, Note No. 5 (1974).

[397] C. Sunshine, In a Process Communication Protocol for Computer Networks, Ph.D. Thesis, Stanford University, SDL Technical Report No. 105 (1975).

[398] E. Surden, Distributed DP No Longer Vague Concept for Malmo, COMPWRLD (September 26, 1977).

[399] Survey Finds Users Slow to Adopt DDP, COMPWRLD (September 26, 1977).

[400] W.R. Sutherland, Distributed Computation Research at BBN, Vol. III, BBN Tech. Report 2976 (December 1974).

[401] F.E. Taylor, Distributive Data Bases Arrival Before DBMS, COMPWRLD (March 28, 1977).

[402] F.E. Taylor, Trial DBMS Use Seems Best Way for Recognizing Problems, COMPWRLD (April 4, 1977).

[403] F.E. Taylor, Standards the Key to Data Base Interworking, COMPWRLD (October 31, 1977).

[404] Telnet Protocol Specification, ARPA Network Information Center (NIC), NIC No. 18639.

[405] R.H. Thomas, A Resource Sharing Executive for the ARPANET, BBN Report 2522, Bolt, Beranek, and Neuman, Cambridge, Massachusetts, NCC (1973).

[406] R.H. Thomas, A Solution to the Update Problem for Multiple Copy Data Bases Which Use Multiple Control, NTIS, AD-A078 251 (July 1976).

[407] Y. Urano, et al., Optimal Design of Distributed Networks, Proceedings ICCC, (August 1974).

[408] C.G. Val, More Power by Networking, IEEE Spectrum (February 1974).

[409] A. Van Lamsweerde, Deadlock Prevention in Real Time Systems, International Computing Symposium, Editors, A. Gunther, et al. (North-Holland, 1973).

[410] S.C. Vortal, et al., GCOS/Multics File Transfer Tool, NTIS, AD-A019 748 (December 1975).

[411] D.C. Visseneseu and C.C. White, Modeling and Dynamic Control of Multicomputer Network, IEEE Computer Networks, Trends and Applications (1976).

[412] A. Viver and H. Zimmerman, Virtual Terminal Protocol (VTP) Proposes Specifications, Reseau Cyclades, 503.1 (1974).

[413] H. Vold and B.H. Sjogren, Optimal Back-Up of Data Bases: A Statistical Investigation, BIT 13 (1973).

[414] D.C. Walden, A System for Interprocess Communica-

tion in a Resource Sharing Computer Network, Communications of ACM 15 (April 1972).

[415] P.L. Walden, Still Another Tool for Synchronizing Co-operating Processes, Department of Computer Sciences, Carnegie Mellon University, Pittsburgh, Pennsylvania (1972).

[416] V.E. Wallentine and F.J. Maryanski, Implementation of a Distributed Data Base System, CS76-03, Computer Science Department, Kansas State University, Manhattan, Kansas (February 1976).

[417] B.A. Walls, et al., Preliminary Design Specifications for the NAVLIS Plot Network Project, NTIS, AD-A011 823 (April 1974).

[418] R.W. Watson, Some Thoughts on System Design to Facilitate Resource Sharing, ARPA Network Working Group RFC 592, SRI-ARC Catalog Item No. 20391 (November 1973).

[419] S. Wecker, A. Design for a Multiple Processor Operating Environment, COMPCON (1973).

[420] A.H. Weis, Distributed Network Activity at IBM, IBM Tech. Report RC 3392 (June 1971).

[421] T. Weisman, Distributed DP Seem Efficient Business Task, CC MPWRLD (September 26, 1977).

[422] J.L. Welom, Data Storage Decisions for Large Data Bases, Ph.D. Thesis, NTIS, AD-A025 874 (February 1976).

[423] J.E. White, The Procedure Call Protocol, Version 2, NIC No. 24459 (January 1975).

[424] J.E. White, The Distributed Processing System (ISIC) NLS OPSJSYS NLS: 1, A Working Paper.

[425] J.E. White, A Network World-Wide Virtual Programming Environment, Berkeley Workshop on Distributed Data Management and Computer Networks, Berkeley, California (May 1976).

[426] J.E. White, A High-Level Framework for Network-Based Resource Sharing, AFIPS Conference Proceedings, NCC, SRI-ARC Catalog Item 34263, NWT RFC 707 (1976).

[427] J.E. White, I elements of a Distributed Processing (Programming) System, Journal of Computer Languages (SRI-ARC Catalog Item 34353) RFC 708.

[428] V.K.M. Whitney, A Study of Optimal File Assignment and Communication Network Configuration, Ph.D. Dissertation. University of Michigan, 1970.

[429] V.K.M. Whitney, Fourth Generation Data Management Systems, NCC (June 1973).

[430] C.A. Wiatrowski and C.R. Teeple, Add Flexibility to Your Control System with Distributed Data Processing, Instruments and Control System (March 1976).

[431] A.J. Winkle, Air Force Data Base Management Reference List and Annotated Bibliography, NTIS, AD-783 778 (July 1974).

[432] P.L. Wodon, Still Another Tool for Synchronizing Co-operating Processes, Department of Computer Science, Carnegie-Mellon University, Pittsburgh, Pennsylvania (1972).

[433] W. Wolf, e al., Hydra: A Kernel of a Multi-Processor

Operating System. CACM Vol. 9, No. 6 (June 1974).

[434] W. Wolf and R. Levin, A Local Network, DATAMATION (February 1974).

[435] E. Wong, Retrieving Dispersed Data From SDD-1: A System for Distributed Data Bases, Proc. Second Berkeley Workshop on Distributed Data Management and Computer Networks (May 1977).

[436] E.F. Wunderlich, Load Sharing in a Computer-Communication Network, NTIS AD-A032 135 (August 1976).

[437] K. Yamaguchi and A.G. Merten, Methodology for Transferring Programs and Data, Proceedings ACM SIGMOD Workshop (May 1974).

[438] S.B. Yao, A Hierarchical Access Model for Data Base

Organizations, Technical Report TR-177, Computer Sciences, Purdue University (February 1976).

[439] S.B. Yao, A Model for Combined Attribute Index Organization, Texas Conference on Computing Systems (October 1976).

[440] Y. Yurono and K. Ono, Inoues, Optimal Design of Distributed Networks, Proceedings ICCC (August 1974).

[441] M.V. Zelkowitz, Simulation and Implementation of Computer Networks, Proc. Thirteenth Annual ACM Washington Chapter symposium (June 1974).

[442] H.N. Zimmerman and M. Elie, Transport Protocol Standard Host-Host Protocol for Energies Computer Networks, Resear-Cyclades Sch. 519.1 (1974).
