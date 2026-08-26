---
otero_id: 17851
otero_key: "FUKSZ9HK"
title: "The state of the art of distributed databases"
authors: "R.A. Davenport"
year: "1979"
journal: "Information & Management"
doi: "10.1016/0378-7206(79)90022-3"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# The State of the Art of Distributed Databases

R.A. Davenport

London School of Economics and Political Science, Houghton Street, London WC2A 2AE, England

Distributed database is an exciting concept since it combines the functional advantages of an integrated database with the economic advantages of a distributed implementation. However, a potential implementor may well ask how much expensive special purpose software must be produced locally or otherwise added to realise a distributed database or, in other words, how much support for the distributed database concept is currently available from manufacturers or software vendors. This paper outlines the requirements of distributed database systems and attempts to survey the present level of support.

Keywords: Distributed databases, database management systems, computer networks, communication software.

![](/api/attachments/FUKSZ9HK/fulltext/images/6aa284923dbeebff26c3c92f233eaf525782c0ba49a9399af11fbf845f7b224e.jpg)

Robert Davenport is a lecturer in Systems Analysis at the London School of Economics (University of London) and a Consultant to CACI Inc. International. He is also a visiting lecturer in On-Line Systems at the City University, London, and a member of the Codasyl DDLC Data Base Administration Working Group. Before joining the London School of Economics, he had been concerned with the design and implementation of transaction processing systems for several years, working for a major software house. Doctoral research has been performed on the design methodology for transaction processing systems. He is a member of ACM and BCS.

## 1. The Reasons for Distributed Systems

The geographically distributed computer user currently has two distinct approaches for implementing an integrated data processing system.

a) The data files and processing can be centralised with access by remote terminals (centralised system)

b) The system can be implemented with a number of computers, typically small, at the various locations, each with its own auxiliary storage and terminals (distributed systems).

Centralised systems have dominated the computer field for a number of years. There are a number of reasons for this. Designers found that a large computer could do the work of several small or medium ones at lower cost and a central computer centre can support a wide range of capabilities that would be prohibitively expensive to provide at each of several smaller centres (economies of scale). A continuing lack of qualified computer staff reinforced this significant cost benefit and the emergence of database technology that enabled organisations to integrate data concerning their operations, accelerated this trend of centralisation. In addition, if operations are centralised the attraction and development of competent technical staff is made easier as is the maintenance of complex hardware and software. Control of operations by management is simplified if those operations are centralised.

However, at the present time an opposing trend is developing; this has been evident for the past three or four years [5]. Progress in the concentration of components within silicon cnips has been spectacular and this in turn has led to rapid decreases in the costs of computing hardware [21]. This progress in cost performance has been exploited up until the present by mini-computer manufacturers considerably earlier than it has been by mainframe manufacturers. This, together with the absorption of a large proportion of the power of a mainframe by its complex operating system has meant that the economy of scale arguments of processors, i.e. Grosch's Law, do not hold to the same extent as previously. However, certain hardware economies of scale do exist, particularly in auxiliary storage, and certain operating costs, e.g. personnel costs, continue to exhibit substantial economies of scale.

In addition, the trend to remote input and processing will continue because users wish to access the computer directly, i.e. terminal-based systems. A recent European study [27] predicts that the terminal population of Europe which is now 450,000 will grow to two millions by 1985. The majority of terminal-based systems up to the present have been centralised. Centralised systems, however, have a number of disadvantages.

First, with a centralised system, data communication costs are significant and have not shown the same rate of cost decrease as hardware. While terminal costs for a specific application may change very little, there is expected to be a steadily increasing cost for transmitting the data. Second, management have also become aware that a centralised system, which may have economic benefits in areas such as operations introduces a number of undesirable side effects. These include the complexities of trying to service an increasing community of remote users, the number of user types increasing and the need to deal with more concurrent events. Third, and perhaps most important, management must be willing to endorse and enforce standardised, centralised data processing project development; this is often contrary to the management philosophy of the organisation which is hierarchical and decentralised.

As well as overcoming problems, distributed systems have positive points. First, distributed systems can be developed on an incremental basis with only as much computing power as is required at that moment in time. Second, reliability of a distributed system is likely to be better. If a large central system goes down, everything stops. If one node of a distributed system goes down, processing can continue on other nodes with reduced capacity. Distributed systems, then, are aimed to fit more closely to the structure of the organisation by moving the computing power to the user. Further discussion of the above points can be found in [6–9,17–19,29], and [24] contains an extensive bibliography. Since both centralised and distributed systems have significant advantages, a systematic methodology [14] for choosing between the two approaches should be employed and for carrying out the design [16].

## 2. Distributed Database Systems

Distributed systems in the terms that they will be discussed in this paper are identified by three criteria [18].

The first criterion is that the system possesses two or more geographically displaced computing facilities (nodes). A computing facility consists of a processing unit with main store, associated auxiliary storage and communication capabilities; the nodes need not have the same computing facilities, and typically serve a separate organisational sub-unit. Each node must be application logic oriented so that application programs are loaded and run at each node.

The second criterion is that the computing facilities are linked, which is accomplished normally today through telecommunications.

The third criterion is that there are relatively weak interactions among the distributed computing facilities. This characteristic excludes tightly-coupled processors working in parallel on a cooperative computing task.

A particular form of a distributed system is a distributed database system. In the broadest sense a distributed database system could be considered to exist when each processor of the system has permanent files. However, this does not imply any relation between the databases, which are seen to be merely elements of the different processors. Therefore, by our definition, a distributed database exists when a logically integrated database is physically distributed over several distinct linked computing facilities – logical integration means that each node has potential access to the entire database. Ideally, the physical distribution of the database is transparent to the application programs. At each node the system software consists minimally of an operating system, a database management system (DBMS) and communications management. With the exception of the latter, the software components may also be similar or dissimilar. The aim of the distributed database is to gain the benefits of the database approach by the central control of integrated data, whilst not imposing centralisation on data processing.

## 3. Distributed Database Architecture

To provide an architectural overview, the reference model of the ANSI Study Group on Distributed Systems [3,4] is employed.

This model begins with the idea that the information processing aspects of an enterprise should be viewed as a network of cooperating workstations. Each workstation is a “location” where a certain kind of work takes place. This workstation may be manual, industrial or computerised. It supports one or more processes which execute its procedures and which primarily access the locally stored data. Access to remote stored data is acceptable but known to be slower and more expensive. The processes of the workstations cooperate by exchanging messages which request certain actions and transfer appropriate data.

Figure 1 illustrates the four major architecture sub-systems storage, database, message and communication management as they are aligned on both sides of the computerised workstations (the application). Process and program management is provided by the operating system. The data storage retrieval functions are divided into a physical and logical part (storage management and database management) and the same approach can be applied to subdividing the data exchange function into a physical part, communication management and the logical part, message management.

As far as the data exchange function is concerned, a considerable effort has been expended within the International Standards Organisation, where a sub-committee ISO/TC97 (SC16) has increased the division of the data exchange function by breaking it down into seven layers, which form what is referred to as the Reference Model of Open System Architecture. The seven layers are:

1. The Application Layer. This is the highest layer in the Open Systems Architecture. An application is composed of cooperating application processes (i.e., application workstations) which intercommunicate according to Application Layer protocols.

2. The Presentation Layer. The purpose of this is to provide the set of services which may be selected by the Application Layer to enable it to interpret the meaning of the data exchanged.

3. The Session Layer. The purpose of this is to support the interaction between cooperating application processes.

4. The Transport Layer. This exists to provide a universal transport service in association with the underlying services provided by supporting layers. It is required to optimise the use of the available communications resources to provide the performance required for each connection between session entities.

![](/api/attachments/FUKSZ9HK/fulltext/images/e57e12ab9a4c483330845b942d4209e724ef979aba1dd7386c0732ccac8f5a2a.jpg)  
Fig. 1.

![](/api/attachments/FUKSZ9HK/fulltext/images/27536049eb9f679b77bef039d523f8f791fb91b3ad44d69470e883bbac0f0a2e.jpg)  
Fig. 2.

5. The Network Layer. This provides functional and procedural means to exchange network service data units between two transport entities over a network connection. It provides transport entities with independence from routing and switching considerations, including the case where several communications resources are used in tandem.

6. The Link Layer. The purpose of this is to provide the functional and procedural means to establish, maintain and release one or more data links between two or more nodes (i.e., network entities).

7. The Physical Layer. This provides mechanical electrical, functional and procedural characteristics to establish, maintain and release data circuits.

Layers 2 and 3 correspond to message management and layers 4, 5 and 6 correspond to communication management of the ANSI distributed system reference model.

## 4. Required Software

There are a number of functions required to be handled in a distributed database system, though ideally there would be only one integrated piece of software. However, the most likely method of clevelopment is that additional software will be written to interface to the standard components supplied by the manufacturer or software vendor in order to handle the distributed database aspect. The standard components would be the same for either a single computing facility or a distributed system, Fig. 3.

The first component is the standard operating system of each computing facility.

The second component is network communication software, [7] that allows information exchanges between remote programs. The architecture of such software involves two levels of control for information exchanges; these are:

a) control of the physical transmission of data

b) control of logical message links between processes (running programs).

The third component is a database management system (DBMS). Associated with this is a description of the database (the schema) and a user's view of the database (the subschema). Ideally, the database management system should be available on mini-computers as well as mainframes to allow the power of the computing facilities to be matched to the local needs while providing database facilities.

The fourth component, is a control structure or network component. The CODASYL Systems Committee [11] refers to this as the network database management systems (NDBMS). It is this component that converts a conventional database environment to a distributed database environment. This component is responsible for knowledge of where data is held in the system, for achieving transparency, for maintaining integrity, for providing translations of data and for preserving database consistency. In the majority of existing distributed systems, the network components tasks are handled by application programs.

With a centralised database, all the intelligence relating to the database is in one place. A conventional data definition can provide all the information for a DBMS to locate and process the stored data.

As soon as data becomes distributed, there must be some information which indicates the location of the different databases, their partitions and their replications. This is the primary role of the network directory.

The network data directory does not contain information about the physical location of nodes or the routing between nodes; this information is part of the communications facility.

![](/api/attachments/FUKSZ9HK/fulltext/images/0affb6d7558810d083c7d878f48b70be9495fea59430cf0dbfefa048931ee98c.jpg)  
Fig. 3.

If it is assumed that a DBMS includes only functions which relate to a local database then all other functions needed in a distributed environment can be packaged in the network component, which must include functions that:

\- Intercept a user request and determine either where to send it for processing, or what nodes must be accessed for data.

\- Access the network directory (or at least know how to request and use its information)

\- Coordinate the processing and responses to a user request (i.e. if the target data exists at multiple nodes).

\- Provide data and process translation in a heterogeneous environment.

## 5. Distributed Database Configuration

In the implementation of a distributed database system, there are a number of options concerning the configuration of the system. These options apply to the:

1. Control structure;

2. Data distribution;

3. Accessing Method;

4. Dictionary/Directory;

5. Currency requirement.

## 5.1. Control Structure

Two distinct control structures can be identified for distributed systems:

a) Central control

b) Distributed control

The term “control” means the handling of message traffic between nodes, the synchronising of update transactions and the initiation of recovery actions affecting more than one node, i.e. network component tasks.

With central control, overall control of the system is vested in one node. Typically such a system will be implemented physically in a hierarchical manner, Fig. 4, with the computing facilities sharing tasks in a structured manner, with each component (to some degree) controlled by the higher level members of the hierarchy. The central control node, which is responsible for overall control, is located at the top of the hierarchy.

With distributed control, fig. 5, all computing facilities cooperate at an equal level logically, to perform a set of tasks. Linking between nodes is on a dynamic basis (dynamic master/slave switching) and control of the data flow is performed by the node that originally established the link. As Bachman [4] points out, distributed control has the advantage of not making the entire system vulnerable to the failure of one element.

![](/api/attachments/FUKSZ9HK/fulltext/images/3693d890000aaa0fc31175fa9e942aab93afba02e0a8d2a0efb88dedc94c918d.jpg)  
Fig. 4.

## 5.2. Data Distribution

The distributed database itself can be a replicated and/or a partitioned database. In a replicated database, Fig. 6, all or part of the conceptual database is replicated at two or more nodes. Fig. 6 shows a distributed database where all occurrences of each data type are held in the storage device at location A, while only some of the occurrences are held at location B and C.

A number of possibilities exist concerning the data structure. For example, each location may have the same data structure as shown in Fig. 7. The data structure is shown as a Bachman diagram [2] where the boxes represent record types and the lines represent links between record types. An alternative is for the complete data structure to be present at only one location and the other locations contain only subsets of the complete structure as shown in Fig. 8.

![](/api/attachments/FUKSZ9HK/fulltext/images/c7d6b5f576c80cc9125096d6751adc8a431fdb8280c542e44f72a1aba63dedd3.jpg)  
Fig. 5.

![](/api/attachments/FUKSZ9HK/fulltext/images/882a49b4eaaceeb8646d2ee37ac86c49eed2118e58961b111126ed02ff7e213b.jpg)  
Fig. 6.

![](/api/attachments/FUKSZ9HK/fulltext/images/1389dfff958650cca8bb4b21a270e35c6c59bc6029a6d3d7fb8dfb8e54a11867.jpg)  
Fig. 7.

![](/api/attachments/FUKSZ9HK/fulltext/images/14f0d8f96439295c7854ea74338d9bdeeb372e7142a8c5db46ddf24fd0062495.jpg)  
Fig. 8.

![](/api/attachments/FUKSZ9HK/fulltext/images/4d949d887b9dccb90ce2a38320576d9c5e885966fe90da8aa4b405cd2d1b7a7f.jpg)  
Fig. 9.

In a partitioned database, Fig. 9, the conceptual database is separated into sections and the sections spread across multiple facilities. A number of possibilities exist concerning the data structure. For example, the data structure may be repeated in each location as shown in Fig. 10, so the partition is only by data occurrences or value. As an alternative, the data structure itself may be partitioned between locations so that a particular data type is found in only one location, as shown in Fig. 11.

It should be stressed that partitioning and replicating of the database are not necessarily mutually exclusive. Both types of data distribution may be present in a particular implementation. For example, Fig. 6 which shows replication of the data between A and B and between A and C also exhibits some degree of partitioning of the database between B and C.

![](/api/attachments/FUKSZ9HK/fulltext/images/b76841b92874d8fa1d1d151b540b2251e23fabf098e405c85ffbd88fb3482c32.jpg)  
Fig. 10.

The distribution of data is one problem of database design peculiar to the distributed environment. There is considerable literature, for example, [22,23], concerning this problem, frequently referred to as file allocation. These research efforts have applied classical mathematical programming techniques to variants of the following problems.

Given: a description of user demand for service stated as the volume of retrievals and volume of updates from each node of the network to each file (piece of the database);

Given: a description of the resources available to supply this demand stated as the network topology, link capacities and costs and the node capacities and costs.

Determine: an assignment of files to nodes which does not violate any capacity constraints and which minimise total costs.

![](/api/attachments/FUKSZ9HK/fulltext/images/25f8e21cc7048429b820a5e211e575f3fcf798c9d334ea14751276eafec47e5f.jpg)  
Fig. 11.

The variations on this problem which have been explored include:

\- consideration of the time varying and uncertain demand;

\- consideration of the dual problem of constraining costs and determining capacities; and

\- the use of heuristics to reduce the computational complexity of finding an acceptable solution.

However, as Rothnie and Goodman [28] point out, the problem stated above is only a small piece of the file allocation problem in a distributed database. There are three specific shortcomings of the existing body of research in this field which limit the usefulness of these results.

1. The user demand model is stated as a set of requirements to access a given file from a given node. This model does not adequately reflect user demand for database access involving more than one file.

2. The complete neglect of synchronisation costs in updating redundantly stored data.

3. The assumption that complete files should be the unit of assignment of data to nodes. There are many situations in which permitting a partitioning of files will reduce accessing and storage costs.

## 5.3. Accessing Method

A transaction is defined to be a logical unit of work. It is typically equivalent to a user activity which is manifest as the execution of an application program. The execution of the application program is usually initiated by an input message from a terminal operator. After the input message is processed and the database is accessed (and perhaps amended), results are produced which are transmitted back to the terminal operator. The input message and the associated output message are referred to as a message pair. There may be several message pairs for a single transaction occurrence.

Transaction handling in a distributed database system can be classified into three methods.

a) Transaction switching, Fig. 12, where the input messages for a transaction generated by a terminal attached to one node (local) wishes to initiate the execution of an application program on a remote node. The network communications software in the local node will intercept the input message and transmit it to the remote node. The messages are transmitted to the remote computing facility and they
they then cause the execution of the application pro-
gram and perhaps amendment of the database section
resident there. Results are transmitted back to the
local node which parses those results to the terminal
that originated the transaction. Transaction switching
is the equivalent of moving the transaction to the
data.

![](/api/attachments/FUKSZ9HK/fulltext/images/8ba59cb714f140996e1761a1ce9f074a0a228a7d9813b9a2c6673446f1872f46.jpg)  
Fig. 12.

b) Split processing, Fig. 13, where the processing of the transaction is split into a number of components. Each component consists of the processing of an application program and the accessing and, perhaps, amending of a database section, wholly within the confines of a single node. When one component finishes, it passes intermediate results to and activates the next component in a remote node. The network component in the local node is responsible for intercepting the intermediate results and passing them to the appropriate remote node. In the remote node the network component initiates the appropriate application program and passes the final results back to the local node. When all components have completed, the final results are transmitted back to the node where execution of the first component took place and those results are passed back to the terminal (local) that originated the transaction. Split processing involves the execution of application programs that are on the same node as the database section that is being accessed and can be considered as having the processing local to the data.

![](/api/attachments/FUKSZ9HK/fulltext/images/c0d2106bfa8a5de1e6dae33d946beeeef03fa8efb198a99ef816801e9eafe1cf.jpg)  
Fig. 13.

![](/api/attachments/FUKSZ9HK/fulltext/images/6a0512c131f058678000d4ed5dd83ee8117731da85a9c5946615d00d9292eb18.jpg)  
Fig. 14.

c) Remote access, Fig. 14, where the processing of the transaction takes place within one node but that processing may require the accessing of data within database sections which are held on remote nodes. Remote access can be summarised as moving the data to the point where the processing of the transaction takes place.

Remote access may be handled on a physical or logical level. The former [4], is based upon the fact that most database systems are built as virtual memory systems and do 'page turning' independent of the operating system and hardware. When a page is requested by the database management sub-system, the storage management sub-system must determine if the page is in a main memory buffer or must it be fetched from the disc. If it must come from the disc, then the appropriate location on the disc must be determined. With a distributed system it must also determine whether the disc is local or at a remote node. If it is at a remote node, then the storage management sub-system must pass a request to the network component which establishes the node with the disc. The network component passes the request to the remote node. The network in the remote node requests the page from storage management and passes it back to the local node (assuming that it is available). The response to the request will be to return the page, state that the process must wait until the page is available or state that deadlock would result if the process waited.

If remote access is handled on a logical basis the same procedure is carried out except that network component interfaces with the database management sub-system rather than the storage management subsystem. The network component intercepts database requests issued by the application program and either passes them to the database management sub-system or passes them to the network component in the appropriate remote node.

All the above accessing methods may be found in a particular distributed database implementation. However, the accessing of data remote from the point where a transaction is initiated should be an exceptional situation otherwise the choice of a distributed approach, or the particular locating of the data in a distributed system, is suspect.

The data distribution decision determines where data is located in a distributed database system while the accessing method decision determines where the processes are located.

## 5.4. Dictionary/Directory

A dictionary/directory typically contains four types of information:

\- logical structure definition (names of records, names of relationships, their domains, etc.)

\- physical structure definition (date field formats, inverted fields, etc.

\- file statistics (size etc.)

\- accounting data (who has accessed the file, who owns the file etc.)

For a distributed database, an additional category of directory information must be added: the location of each piece of the database in the network. (The network data directory).

The system software (the database management system and the network component) must have access to this information in order to analyse user requests, choose and execute an accessing method and account for the resources to be used. Therefore a decision has to be made concerning the structure of the directory and where the directory is located.

Chu [10] investigated the performance of four directory structures. In each of the structures it is assumed that each node has its own directory which contains information about the data stored at that node. The structures are:

a) Centralised. A master directory is located at one of the nodes. When a user requires data that is not stored at the local directory the master directory is consulted. The centralised directory must be updated when there is a change in the storage location or contents (addition, deletion) of a database section. There are communication costs incurred for each transaction that requires remote data.

b) Extended and Centralised. This is a modification of the centralised directory. Once the user finds the location or description of data, that information can be appended onto the local directory. Should the user require that information again, the directory information can be obtained from the local directory, thereby reducing the communication cost as well as time for querying the master directory. However, when the information of that data at the master directory is updated, updating of the information on that data in the local directories is also necessary.

c) Local. In the local directory case there is no master directory in the system. When information about requested data is not stored in the user's local directory, the user queries all the other local directories in the system until the requested data has been located. Such a directory system has high communication costs. (The system may broadcast the request.)

d) Distributed. In the distributed directory case, each node in the system has a master directory. The advantage of this system is its fast response. The disadvantages are the cost of storing master file directories at each node and the communication cost for updating all these directories.

The general conclusions of Chu's investigations, assuming that transmission cost was much higher than storage costs, were that at low directory modification rates, a distributed file directory yields the lowest operating costs. As the modification rate increases extended centralised directory provides the cheapest solution, while at high modification rates the centralised solution is the cheapest. About a third of all transactions were assumed to require remote data.

## 5.5. Currency

While speed of response is important, another prime question is the need for up-to-date data. For the user, few systems really need reference data to be highly up-to-date. The tighter the specification, the more costly the design. For this reason designers often choose to update files overnight (in batch) as it simplifies many technical aspects and can meet system objectives. Currency will be a factor of particular relevance to a distributed system when more than one copy exists, i.e., the conceptual database is replicated. When there is more than one copy of data, the currency requirement can be one of the following:

a) Delayed, which implies that amendments are made to only one copy of the data; the other copies are amended at some later time. This will tend to reduce data communications traffic at the cost of data consistency.

b) Immediate, which implies that all copies are kept in step. This will require accesses to be blocked to all copies when the value of the data is to be changed. All copies are then amended. Only after all amendments are completed are any of the copies once again available for access.

## 6. Data Distribution – Currency Combinations

Four combinations of data distribution and currency can be identified for a distributed database system. The selection of a particular combination may affect the choices available for control, directory and access method. The combinations are the following:

a) Delayed Update - Partitioned Database. Delayed update to a partitioned database necessitates a read-only mode of operation of the complete conceptual database when operating in transaction processing mode. Transactions, generated by terminals, are processed by application programs which require a read-only mode of access to the database. The access method for these read-only transactions can be transaction switching, split processing or remote access. Transactions which when processed will cause amendments to be made to the databases are simply validated and added to a transaction file. This necessitates the access method for transactions, which will cause amendments to the database, to be transaction switching. The transaction file in each node in input to an application program which is run in a batch processing mode at some convenient time (e.g. overnight) when there is no transaction processing activity. It is the processing of this application program which actually causes amendments to be made to the database.

b) Delayed Update - Replicated Database. Delayed update to a replicated database requires that one node is designated as containing the master copy of the section of the database that has been replicated. Any amendments are made only to the master copy. Other nodes operate in a read-only mode, i.e., transactions, the processing of which results in changes to the database, are processed at the node that contains the master copy. The access method used for accessing sections of the database held on remote can be either transaction switching or split processing. Normally such accessing will only be necessary for transactions, the processing of which will cause amendments to the database. If split processing is the access method, only one component of the application program that is processing the transaction (the one resident in the master node) will cause amendments to be made to the database. The read-only copies of the database section involved are updated in a batch mode and some convenient time (e.g. overnight). One method, [26] of handling the reconciliation of the copies of a replicated database is for each physical record to have an indicator field to denote an insert/amend/delete action. The indicator is set to one of five values.

A - this record has been inserted

B - this record has been amended

C - this record is to be deleted

D -- this record is to be deleted and the node containing the second copy has been informed

Z - this record has not been changed

The processing of transactions which cause the master copy to be amended will also cause the indicator field to be altered. A utility program is run at the master site at some suitable time (e.g. overnight) to transfer all changed records to the remote slave node and changes the appropriate records on the read only copy to D. Further utility programs are run on both sites to delete D records.

c) Immediate Update - Partitioned Database. If immediate update of a partitioned database is required, any one of the three access methods may be employed.

1. Transaction switching. If the access method employed is transaction switching then the actual processing of the transaction which involves the execution of an application program which accesses and amends the database, is confined to a single node.

2. Split processing. If the access method is split processing this implies that accesses and amendments may be required to be made to database sections attached to more than one node. In order to maintain content consistency of the database, the processing of the transaction may require sole accessing rights to data in more than one node. Accessing of that data may be blocked for a significant period of time because of the data communications necessary between the nodes involved in the processing of the transaction. If content consistency between data items held in different nodes is not necessary, then the amount of time that the data is blocked will be reduced appreciably since the data communication time will be removed from the length of time that the data is blocked.

3. Remote Access. If this access method is chosen, it is certain that the processing of a transaction which requires sole access to data on a remote node will cause that data to be blocked to further access for an appreciable period of time. This is because of the messages that must be transmitted between nodes to request the data to read and lock the data, to modify the data and to release the data. As Rothnie and Goodman [28] point out, the delay associated with locking in a distributed system can be some 2 to 3 orders of magnitude greater than the delay typically encountered when setting locks in a centralised system. In the case of split processing the length of time that an item of data is blocked may only be for the duration of processing in one node unless there is not a requirement to maintain consistency between items of data in different nodes.

d) Immediate Update - Replicated Data. Immediate update in a replicated database is likely to be a viable solution only if the majority of transaction processing, which requires data at remote nodes, only need to read the data, i.e. only a very small proportion of the processing requires amendments to be made to remote data.

If immediate update is required of all copies of data in a database with some degree of replication, two access methods are possible: split processing and remote access.

Split Processing. If this is employed, identical application programs are run when amendments are to be made against each copy. In order to keep the copies consistent the application programs are initiated at the same time. The node where the transaction has been received will have to determine the data that is to be amended and request that sole access is given to that data for all copies. Once sole access is granted the application programs that cause amendments to the database are initiated at the nodes containing copies of the data.

Remote Access. With this split processing there is no saving in time since in order to keep the database consistent, locking messages must still be sent to all nodes containing copies of the data to be amended. Therefore remote access which does not require the synchronising of application programs but only the synchronising of data amendments is a more straightforward approach. A possible sequence of action is the following:

i) Inhibit access at all copies

ii) Lock copies as soon as current accesses finish

iii) Amend all copies

iv. Unlock all copies

## 7. The State of the Art

A potential implementor may well ask how much expensive special purpose software has to be produced to realise a distributed database system, or how much support is currently available from manufacturers or software vendors.

A number of distributed database implementations have been reported in the literature in the past few years [6,9,26]. However, each of these systems is a special purpose, one of a kind system designed to handle the particular data management needs of a single organisation. What is needed is a general purpose distributed DBMS. Such systems, like conventional non-distributed DBMS's are seen as being available off-the-shelf, and as being able to solve a wide range of data management problems. The reason that such systems do not yet exist is that there is an assortment of difficult technical problems which must be solved before a workable system can be produced. These problems include:

\- effective processing of multi-site queries;

\- efficient distributed concurrency control;

\- continuity of operation in the presence of failures;

\- efficient directory management; and

\- distributed data base design

Each of these problems is being investigated in a number of research centres at the present time and surveys of such efforts may be found elsewhere [1,28,31].

At the present time, adequate solutions to all of these problems exist, although new and better solutions can be expected to be introduced for many years to come. Therefore we are very close to a distributed database system product though of a particular class.

There are two distinct classes of system to be considered. The first class is a homogeneous distributed database system. This is the kind of system in which the database system designers have control over the entire system, including both the global and local views of the databases. It is this class of system which is very near at hand as a product. The other class of system is a heterogeneous distributed database system. Such systems must accept the local database

view of pre-existing databases. They offer all the benefits of homogeneous distributed database systems, plus the advantage that they do not require the expensive re-implementation of existing applications. Unfortunately, however, as has been previously pointed out [30], the technological hurdles to the implementation of such systems are much higher and probably will not be overcome within the next few years. The problem arises from the tremendous variability which exists in the way people structure and employ databases. Pre-existing databases differ in data models, data manipulation languages, schemas, data types, coding, etc. Dealing with this variability involves mapping from differing local views into a common global view. To accomplish this, the mapping facilities must be able to capture semantics (which are not explicit in the local data representations, but are present only in application programs or the minds of users.)

To demonstrate the proximity of a homogeneous distributed database system, two examples are given of available systems from hardware manufacturers. Further examples are given elsewhere [15].

## 7.1.IBM

Systems Network Architecture (SNA) is a reasonably centrally controlled, distributed intelligence network structure [12]. A recent addition to SNA is the multisystem network facility that allows application programs and databases to be distributed across multiple IBM 370s in multiple data centres. A terminal may be switched from an application in one IBM 370 to an application in another. However, to perform the switchover both 370s must be operating, i.e. a terminal cannot be switched from one IBM 370 to another because the first IBM 370 has failed. There are four levels of intelligence in SNA but the user need not use all four levels. The top level is the Virtual Telecommunications Access Method (VTAM), located in the main computing facility, which provides overall control for the whole network. At the next level is the Network Control Program (NCP) which provides local network management under the direction of VTAM. The NCP resides in the front end processors and intermediate node processors. The next level is the cluster control level. The fourth level is the terminal level. Not only are some network functions moved out of the host facility into the network processors but also some application logic can be moved into the network processors but also some application logic can be moved into minicomputers (or programmable controllers) such as the recently announced IBM 8100. At the present time there is no inherent distributed database capability in the 8100.

The only file organisations handled are sequential, multiple indexed and direct access. The application logic is responsible for determining if the data is held locally and, if data is not present, responsible for directing a request to the host computing facility. One significant development with the introduction of the 8100 is the ability to have dynamic master-slave control in a SNA network. IMV/VS [25] is the standard database system which at present is only available on 370 computing facilities. However, there has recently been released a facility referred to as the Multiple System Coupling (MSC) feature which allows individual IMS/VS systems to access one another. Access may be via main storage, when IMS/VS systems are running on the same processor, via a channel link or via a data communications link.

MSC permits two nodes of accessing; transaction switching and split processing. With the first, transaction generated at one IMS/VS system may access a remote IMS/VS database. With the second if there is a requirement for a transaction to access multiple IMS/VS databases, then the processing must be broken into several application programs, each of which is contained in one IMS/VS system and is only accessing one IMS/VS database. Communications between application programs is by program-to-program switches. Note that an IMS/VS database must be completely contained within a single node, i.e. if data is duplicated it is contained in two logically different databases on two different nodes. This would require two separate logical and physical updating operations when required.

## 7.2. Hewlett-Packard

Hewlett-Packard have recently introduced Hewlett-Packard Distributed System Network (HP-DSN) [20]. HP-DSN consists of an architecture implemented presently in a number of products, DS/3000, DS/1000 and HP2026. HP-DSN allows the user to treat each node as an equal, i.e. there is a dynamic master-slave control. Using DP-DSN, users have the following capabilities available.

a) Remote file acces

b) Remote database access

c) Program to program communications

d) User access to any terminal in the network

e) Terminal access to any system in the network.

Remote database access (RDBA) is presently possible only between two HP 3000s. RDBA allows a local HP 3000 user to access remote databases that is, DS/3000 will direct standard local IMAGE program calls to be executed on a remote computer. IMAGE is HP's database management system. Associated with IMAGE is a database enquiry facility QUERY which can be used interactively to store, modify, retrieve or report on data in IMAGE databases that reside on remote HP systems. Program-to-Program Communication (PTOPC) allows two programs in different HP 3000 or HP 1000 systems to execute and exchange data in a coordinated manner. For data transfer to occur between the programs of remote computer systems, one of the programs must be the master and the other the slave. With PTOPC, programs can be run on one system that indirectly access and update an IMAGE database residing on another system.

HP-DSN supports the three methods of accessing; transaction switching, split processing and remote access. However, in IMAGE database must be completely contained within a single node, i.e. if data is duplicated it is contained in two logically different databases on two separate nodes. Alos, as far as programs are concerned, the location of data is predefined, i.e. there is no dynamic searching of directories after a program has been initiated.

## 8. Conclusion

This paper has identified the components of a distributed database system and shown two examples of the current level of support available from manufacturers. It has shown that commercially available distributed database system products can be expected to be seen within the product lines of a number of vendors within a comparatively short space of time. However, it is not surprising that such systems will be homogeneous, i.e. restricted to a single manufacturer and a single database management system.

## References

[1] A. Adiba, J.C. Chupin, R. Demolombe, G. Gardarin, J. Le Bihan, Issues in distributed data base management

systems; A technical overview, Proceedings of Fourth International Conference on Very Large Databases IEEE, 1978, pp. 89--110.

[2] C. Bachman, Data Structure Diagrams, Vol. 1, 2. 1969.

[3] C. Bachman, Future image of computers, Data Show 77 - International Symposium, Tokyo, October, 1977.

[4] C. Bachman, Commentary of CODASYL systems committee interim report on distributed database technology, AFIPS NCC, 1978, pp. 919–921.

[5] R.G. Canning, Structures for future systems, EDP Analyser, Vol. 12, 8, 1974.

[5] R.G. Canning, Distributed data systems, EDP Analyser, Vol. 14, 6, 1976.

[7] R.G. Canning, Network structures for distributed systems, EDP Analyser, Vol. 14, 7, 1976.

[8] R.G. Canning, Distributed systems and the end user, EDP Analyser, Vol. 14, 10, 1976.

[9] G.A. Champine, Six approaches to distributed databases, Datamation, Vol. 23, 5, 1977, pp. 69–72.

[10] W.W.. Chu, Performance of file directory systems for databases in store and distributed networks, AFIPS NCC, 1976, pp. 577–587.

[11] CODASYL, Distributed database technology - An interim report of the CODASYL systems committee, AFIPS NCC, 1978, pp. 909-917.

[12] R.J. Cypser, Communication Architecture for Distributed Systems, Addison-Wesley, 1978.

[13] Datamation, Distributed tentacles take hold, Datamation, Vol. 22, 9, 1976, p. 190–7.

[14] R:A. Davenport, Centralised or distributed database – A methodology for selection, The Computer Journal, Vol. 21, 1, 1978, pp. 7–14.

[15] R.A. Davenport, Distributed database technology - A survey, Computer Networks, Vol. 2, 3, 1978, pp. 155-167.

[16] R.A. Davenport, The design of distributed database systems, The Computer Journal, Vol. 23, 1, 1980.

[17] P.J. Down and F.E. Taylor, Why Distributed Computing?, NCC publications, 1976.

[18] J.C. Emery, Managerial and economic issues in distributed computing, Information Processing 77, North Holland 1977, pp. 945–955.

[19] W.T. Hardgrave, Distributed database technology: An assessment, Information & Management, Vol. 1, 1978, pp. 157–167.

[20] The Hewlett-Packard distributed system network (five articles) Hewlett-Packard Journal, Vol. 29, 7, 1978.

[21] D. Hsaio and S. Madnick, Database machine architecture in the context of information technology evolution, Proceedings of Third International Conference on Very Large Databases IEEE, 1977, pp. 633–684.

[22] K.D. Levin and H.R. Morgan, Optimising distributed databases - A framework for research, AFIPS NCC, 1975, pp. 473-478.

[23] S. Mahmoud and J.S. Rioidan, Optimal allocation of resources in distributed information networks, ACM Transactions on Database Systems, Vol. 1, 1, 1976, pp. 66–78.

[24] M. Muller, A survey of distributed database management, Information & Management, Vol. 1: 1978, pp. 243–264.

[25] W.C. McGee, The information management system, IMS/VS, IBM Systems Journal, Vol. 16, 2, 1977, pp. 84–168.

[26] P. Murray, Getting the network mixture right first time, Computer Weekly, August 25th, 1977, p. 16.

[27] R.A. Peters and H.F. Bunn, Economy dips, terminal forecast climbs, Datamation, Vol. 22, 1576, pp. 102-B-102-H.

[28] J.B. Rothnie and N. Goodman, Survey of research and development in distributed database management, Proceedings of Third International Conference on Very Large Databases, IEEE, 1977, pp. 48–62.

[29] A.L. Scherr, Distributed data processing, IBM Systems Journal, Vol. 17, 4, 1978, pp. 324–343.

[30] Panelists' statements on distributed databases, Proceedings of Fourth International Conference on Very Large Databases, IEEE 1978.

[31] K. Ziegler, A distributed information system study, IBM Systems Journal, Vol. 18, 3, 1979, pp. 374–401.
