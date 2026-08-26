---
otero_id: 17808
otero_key: "APQF8B2G"
title: "An inter-related processing network architecture"
authors: "Charles Houen"
year: "1978"
journal: "Information & Management"
doi: "10.1016/0378-7206(78)90013-7"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An Inter-Related Processing Network Architecture.

II. The Functional Architecture\*

Charles Houen

The Royal Bank of Canada, Systems and Processing Operations, P.O. Box 6001, Montreal, Quebec, Canada H3C 3A9

A set of objectives and policies have been established to guide the design and development of a multi-centre processing network architecture to meet the Bank's requirements well into the 1980's. Based on these objectives and the initial conceptual model of the architecture, a functional architecture has been developed. This is a plan for mapping the component subsystems onto hardware, software and communication networks.

The overall communication network architecture comprises networks for real-time transactions and for bulk file transmission between processing centres. The real-time communication networks are application-independent, common systems through which terminal workstations can access any Service Processing System for which they are authorized.

The real-time processing systems architecture supports independent Service Processing Systems on physically modular processing facilities which are minicomputer-based; each processing facility is dedicated to a given Service Processing System. A pilot project had demonstrated the basic viability of this approach, which will provide a means of implementing Service processing systems at lower cost, with higher reliability and with better accommodation of differing scales of operation than a large mainframe approach.

Keywords: Processing networks, virtual circuits, packet switching, distributed/distributive processing, real-time transaction processing.

## 1. Introduction

This is the second paper which describes the evolution of a processing network architecture designed to meet the information processing requirements of the Royal Bank of Canada.

The first paper was published in Vol. 1, No. 1 (pp. 27–33); it provided a background description of the Bank and its operations, described the set of objectives and policies established to guide the design and development of the processing network architecture (which must be serviceable well into the 1980's), and discussed the initial conceptual model of the architecture.

This paper addresses the further development of a functional architecture, which is a plan for the mapping of the component subsystems onto hardware and software modules and communication networks. It covers the practical requirements and constraints and the considerations involved in implementing the functional architecture using technologies such as

![](/api/attachments/APQF8B2G/fulltext/images/4343c254e035b9f0f8f316ffb2d14d4084ae097eb095ccb412550cee18d8d1ff.jpg)

Charles Houen is Manager of Planning in the Processing Systems Group of Systems and Processing Operations at the Royal Bank of Canada. Prior to joining the Bank in 1974, his sixteen year data processing career included eight years as a Systems Engineer with I.B.M. in Australia and Europe, and two years as an independent consultant in Europe.

virtual communication circuits, large mainframe computers and distributive processing based on mini-computers. Our experience with a distributive processing pilot and our plans for implementing the architecture are described.

## 2. The communication network architecture

The overall communication network architecture is shown in fig. 1. The major components of this architecture are:

\- For real-time services

\- The regional real-time communication network
- The inter-system real-time network

\- For file exchange between centres

\- The inter-centre bulk transmission network. Before proceeding to discuss these networks, it should be noted that each is logically independent and separate, even though physical facilities may be shared.

## 2.1. The real-time communication networks

Figure 1 illustrates that each Central Processing Centre (CPC) is linked to the Customer Service outlets in the region served by that CPC by a Real-Time Communication Network. It will be recalled that each of the six CPCs serves a geographic region, roughly following provincial boundaries as was illustrated by fig. 1 in our first paper (Vol. 1, No. 1, p. 28). The Customer Service outlets connected to the Real-Time Communication Network may be any one or a combination of the following types:

\- Manned Branches, where customers are served by tellers, loan officers, etc.,

\- Unmanned Customer-operated convenience banking facilities (ATM's, cash dispensers),

\- Special Service Branches (e.g. a Credit Card centre handling authorization enquiries from merchants and general enquiries from credit card holders).

![](/api/attachments/APQF8B2G/fulltext/images/5b275b337449d33a3f00fe138fe818b7ff41a38a5966c4e9eb506080140b0527.jpg)  
Fig. 1. Overall communication network architecture.

These Customer Service outlets are linked by the regional communication network to Real-Time Service Processing Systems in the regional CPC. In looking at the required network architecture for Real-Time Services, we proceeded with the objective of making the network an independent and common system via which users at the Customer Service outlets could access any Service Processing System for which they were authorized. This means that neither the terminals at the Customer Service outlets nor the physical communication network should be constrained by the communication network architecture to be dedicated to a particular Service. Operational considerations naturally lead to some types of workstations accessing only a subset of the available Service Processing Systems related to the workstations functions, and security considerations impose access restrictions, but these are externally imposed constraints rather than a limitation of the communication network architecture per se.

In the first paper we defined an Electronic Message Control and Switching function which interfaces all CPC functions to the communication networks. In the early days of the project, we tended to think in terms of private, leased line networks of the type in use today for our present on-line branch banking Services. In conjunction with that type of communication network, the communication architectures of the major computer manufacturers favoured the dedication of terminal workstations to a given "application system". Our initial answer to these constraints was to define a Transaction Distribution and Control (TD & C) function within Electronic Message Switching and Control. This function would effectively "own" all the terminal workstations in the Service delivery network, and distribute incoming transaction messages to the appropriate Service Processing Systems by examining transaction identifiers in the messages; it would also distribute output messages from the processing systems to the terminals. The TD & C function was also seen as routing transaction messages between interacting processing systems in the same or different CPCs.

The centralized Electronic Message Control and Switching and TD & C concepts were overtaken by developing technology during the course of the project. The advent of commercially available packet switching services in Canada plus evolution of the computer manufacturers' communication architectures (IBM's System Network Architecture/ACF, DEC's DECNET, etc.) provided tools for the implementation of virtual circuits between terminal workstations and multiple, independent central application systems. Without going into the details of supplier-dependent implementations, it suffices to say that a terminal workstation attached to a programmable terminal controller can concurrently have available to it virtual circuits to each of the independent application systems it needs to access. This leads to a logical network architecture as illustrated in fig. 2. The functions of TD & C have been distributed to each of the terminal controllers, where programmed logic determines which Service Processing System will handle each transaction, and then sends the transaction message(s) over the appropriate dedicated virtual circuit. This allows high volume transactions to be processed without the delay and overhead of setting up a virtual circuit each time the Service Processing System being accessed by a workstation changes. This is important for branch teller workstations where several Service Processing Systems may be accessed in servicing one customer. Additionally, the terminal controller programmability is further utilized to distribute some other processing functions, such as operator/system dialogue, application-dependent transaction editing, formatting functions dependent on workstation characteristics, and application-independent functions such as teller cash position control.

The Electronic Message Control and Switching functions are also distributed to the following:

\- The terminal controller's communication network interface software, which participates in the set up, control and use of virtual circuits which may be carved out of leased communication links or provided by a common carrier packet switching network.

\- The communication network interface software of the central processing facilities supporting Service Processing Systems.

\- Network interface machines (NIMs) which may be interposed between the communication network (leased or packet switching) to distribute virtual circuits coming in off physical links to multiple processing facilities.

![](/api/attachments/APQF8B2G/fulltext/images/24fdc8c22a3a489fb60858207f880a7efd4698e855e039ffb398b9e2c971e1d7.jpg)  
Fig. 2. Real-time communication network architecture.

Figure 2 thus represents our target communication architecture for the Real-Time Service Network. The figure has been simplified by showing only one terminal controller with two active virtual circuits to central processing systems. It also illustrates the same virtual circuit approach applied to the Inter-System Real-Time Communication Network linking real-time Service Processing Systems in the same and different CPCs.

## 2.2. The inter-centre bulk transmission network

Figure 1 shows Electronic Data Control and Distribution (EDCD) in the CPC linked to the Inter-Centre Bulk Transmission Network. Via this network, EDCD exchanges data files with document capture and output systems in the subsidiary APCs of the CPC, and with EDCD systems in other CPCs. This network also provides the capability for exchange of files by data transmission with other banks and financial institutions.

## 3. Real-time service processing system architecture

## 3.1. Requirements and constraints

In developing a functional architecture to support these systems, we worked with the following practical requirements and constraints (these were more generally defined in the first paper):

\- It is a policy to decentralize or distribute Service Processing to each of the six CPCs for a variety of social, business and operational reasons. This policy is already implemented for most customer Service Processing Systems; however, several major Service Systems are currently decentralized only to three CPCs. This partial centralization is related to economy of scale considerations applicable to large mainframe computers; it is not economic to operate these systems in all six CPCs until the concepts described have been developed and implemented in the three smaller CPCs.

This points up a very practical constraint: where there are widely differing volumes of business between Centres, for Service Systems to be economically viable for implementation in all CPCs the standard processing facility architecture must be amenable to a wide variation in processing capacity.

\- It is also policy that standard hardware and software be used in all CPCs, thereby keeping development, support and maintenance efforts for both operating software and application systems at a minimum.

\- Real-time systems in particular must provide a very high level of service availability to the Service Delivery Network to ensure smooth operation and high productivity in Branches, and to avoid interruption of customer service where the level of Service availability at tellers, ATM's etc. is highly visible. With a delivery network which handles so many Services, it is not sufficient that the general level of availability be high; it is also necessary that problems with any given component, such as a workstation or a particular Service system, should not impact or "infect" other components.

\- The Bank's Service Production and Delivery systems are continuously evolving as new Services and new features are added to existing Services. Further, many of these additions and enhancements necessarily involve phased implementation over considerable periods which gives rise to a requirement that processing systems architecture be able to accommodate the incremental addition and enhancement of individual systems without disrupting the normal operation of other systems.

\- The implementation of new Service systems in Branches is necessarily a lengthy process. Branch personnel require training, new procedures have to be implemented, new/additional terminal equipment may be required. An additional factor is that the volume of business and transactions will normally increase with elapsed time, with the result that there may be a very substantial difference in the processing capacity required at initial implementation, twelve months later, twenty-four months later and so on. It can be extremely expensive to provide, at a particular point in time, the aggregate processing capacity that is expected to be required in one or two years for a number of systems. Therefore, a practical requirement for a processing systems architecture is that it should allow the gradual addition of processing capacity in reasonable increments, again without disrupting on-going operations.

## 3.2. Service processing system philosophy

In conjunction with the objective of an independent and common Service delivery network able to access any Service Processing System, it is also an objective to design and implement Service Processing Systems as an array of independent and modular entities which perform the processing required for a Service or a set of closely related Services. Such processing systems are self-sufficient for normal operation, and interact via transaction interfaces with other Service systems.

Considering the mapping of these independent Real-Time Services Processing Systems onto hardware/software architecture, and taking into account the requirements and constraints defined above, led to detailed studies of various mainframe implementations. The results of these studies may be summarized as follows:

\- The implementation of all planned real-time systems would require large mainframes, which would be too expensive for the smaller CPCs.

\- Large mainframe hardware and software architecture such as we presently use make it necessary to use separate partitions or regions for application systems to give them minimal isolation and protection from each other; this requires that each application region carry a heavy overhead in having its own copy of application management (teleprocessing monitor) software.

\- In order to provide a high level of hardware availability, it would be necessary to provide extensive and expensive redundancy.

\- Mainframe processing capacity comes in large steps, leading either to the installation of configurations sized to a load that will not be achieved for a considerable period, or to a series of major upgrades which are not only disruptive but expensive since they interfere with the optimization of buy/lease/rent policies.

In short, we found it difficult to reconcile our objectives, requirements and constraints with large mainframe architectures. We began to examine alternatives, including minicomputers. In our on-going discussions with other large banks, we found that we were not alone in our quest for more modular and flexible processing system architectures. For example, the Bank of America was working on the use of arrays of minicomputer-based processing modules. By early 1975 they had committed to a development project following a comprehensive evaluation and live pilot. Our own work, reinforced by an evaluation of their approach, convinced us that this type of technology had real potential for meeting our needs. We therefore commenced work on the definition and evaluation of a minicomputer-based architecture for the Real-Time Service Processing systems.

Figure 3 illustrates this architecture. It will be seen that the essential feature of the architecture is the use of minicomputer-based processing facilities as the modular building blocks. Each processing facility is dedicated to supporting the Real-Time segment of a Service Processing System or a portion of the total processing for such a system, depending on the size of that system. The distribution of the total processing load of a system across multiple processing facilities would normally be on the basis of dividing the files or database; for example, most customer Service accounts are domiciled by branch, so a natural division of the processing load for a particular service would be to allocate the branches in a subregion to a given processing facility. This is illustrated in fig. 4. The communication network architecture previously described provides great flexibility in the allocation

![](/api/attachments/APQF8B2G/fulltext/images/2b8e3fe697269b6aafbf2378f508fa46fc7ccb0fc9a83d4b7e2b371440ec77c8.jpg)  
Fig. 3. Real-time processing systems architecture.

![](/api/attachments/APQF8B2G/fulltext/images/8e85397001aa9e4f5cc10113dc88248cdee3f2d2d57aa24b4030d9ea56090536.jpg)  
Fig. 4. Service processing system distribution over multiple processing facilities.

of branches to processing facilities for different Services, since individual virtual circuits are used for each Service system accessed.

There is considerable scope for flexibility in the physical implementation of the processing facility architecture. For example, high levels of Service System availability may be achieved by:

\- Providing internal redundancy in a processing facility; e.g. dual, load-sharing CPUs each handling half the data base, with disk drive switching in case of a CPU failure.

\- Providing external backup for a processing facility, again with peripheral switching or file volume transfer.

In this area, the physical modularity and relatively low cost of minicomputers allow a greater degree of physical redundancy to be used.

Examining the architecture at this level, its physical modularity matches well the objectives, requirements and constraints outlined before. Specifically, this modularity provides the following characteristics:

\- Differing scales of operation across the CPCs is naturally accommodated; in a large CPC, a given service system may be supported by three processing facilities, in another by one.

\- The hardware and software remains standard regardless of the scale of operations.

\- Reliability and availability are enhanced in a number of ways:

– dedicated operation requires less complex software.

\- the effects of hardware/software faults are isolated to a particular module.

\- the availability of critical modules may be increased by internal component redundancy or external backup.

\- The evolutionary implementation and enhancement of individual Service systems is readily handled at the independent module level, without disruption of other systems.

\- Growth in the processing load of individual systems is met by relatively small modular increments.

In addition to the above characteristics, it was calculated that the cost of such distributive processing architecture would be in the region of one half that of a functionally equivalent mainframe architecture, owing to the inherently better cost/performance characteristics of minicomputers and the ability to match processing loads and processing capacities more closely.

There were a number of doubts and unknowns about the use of minicomputers in this critical area of application processing; chief among these were the availability and quality of system software, particularly in the area of application support (application management, file management, commercial language compilers). However, it was decided that the potential of a minicomputer-based distributive architecture was sufficient to warrant practical evaluation in the form of a pilot system.

## 3.3. The distributive processing pilot

Figure 5 illustrates the configuration of the pilot system, for which a development project was initiated with the objectives of:

\- testing the application of minicomputer technology to the distributive real-time processing.

• assessing the suitability of available hardware and software.

\- learning sufficient about the technology to be able realistically to project the impact of its application to larger scale modular configurations.

A real application that would provide a reasonable volume of transactions was deemed to be necessary, and the provision of ATM (Automated Teller Machine) Service delivery to the Bank's Head Office staff was chosen for this purpose. Thus the terminals in the pilot configuration are ATM's and administrative terminals, the latter being used for updating the cardholder data base with status changes, card activation transactions, etc. As the application in this case was a vehicle for the technology aspects of the trial, this article concentrates on the latter.

Figure 5 identifies the major components of the software architecture. Note that standard basic software is used, in the form of DEC's RSX-11M operating system, RMS-11 file system, and communication drivers. DECNET is used to provide logical communication channels or virtual circuits between processes in the Terminal Controller and Processing Facility.

![](/api/attachments/APQF8B2G/fulltext/images/13a21cb8ada418b76deed1637086b29940d22373baa371ff6bf92263d3701500.jpg)  
Fig. 5. Distributive processing pilot configuration.

We did have to develop in-house the "Application Manager," which is the equivalent of mainframe teleprocessing monitors such as Informatics Incorporated's INTERCOMM or IBM's CICS. This was not developed from scratch, as we had already developed a package for a stand-alone mini-based foreign exchange system.

This pilot system will shortly go into live operation, but at this stage we have already been able to

make a partial appraisal:

\- Although we are using some new initial release software, it has been reasonably stable and we have not experienced significant problems or deficiencies.

\- As an organization steeped in large mainframe technology, we have had some problems, not the least in obtaining experienced minicomputer system people.

\- The most significant shortcoming in the available technology is the lack of application management software (as mentioned previously) and we believe that this is a general situation applicable to the major minicomputer product lines. As a policy, we are not in the business of developing and maintaining this type of software, but we believe that such software products will be available from one or more sources within a year.

\- We have learned to live with the more limited address space of 16-bit minicomputers. It is apparent to us that a larger address space and commercial instructions would be more efficient for our type of applications.

\- Given all the limitations, we have established to our satisfaction the basic viability of present mini-computer technology for distributive real-time transaction processing. While we would not be prepared to base the development of production Service Processing systems on the software we are using for the pilot, we are reasonably confident that deficiencies in this area will be recitified in the near future.

## 4. Plans for migration to the new architecture

## 4.1. Communication networks and terminal systems

We are committed to a phased implementation of the shared communication and terminal networks for our branches. As a first phase, we have started to replace the present unintelligent teller terminals by intelligent modular terminal systems in which branch workstations for tellers, loans officers, etc. are controlled by programmable controllers. Initially, these terminal subsystems will emulate the functions of the old terminals and access the existing on-line Service Processing System. The development of new Service Processing and Delivery systems will envolve the allocation of some application logic to the Terminal Controllers as previously mentioned. Virtual circuits will link this terminal logic to each central Service Processing System. Very flexible migration strategies are possible with this approach. From the branch perspective, the initiation of a new Service system will involve the installation of the appropriate terminal controller application logic which will then communicate with the new Service Processing System.

## 4.2. Real-time service processing systems

A conservative approach to the implementation of the new distributive processing technology is planned. Part of our development effort has the objective of providing a standard application system environment which will allow the applications to be transportable between different hardware and system software environments in a manner which is as transparent as possible to the application programs. This will be source language transportability. The essential elements of this standard application environment are:

\- a standard source language: ANS COBOL.

\- standard application management software interfaces for:

\- transaction parameters passed to the application.
- application management services interfaces, e.g. for file/data base access, working storage, context preservation during conversational transactions, etc.

This is a reasonably ambitious objective, but work to date indicates that it will be possible to achieve a high degree of application-transparent portability.

With this approach, we will be able to take the time to ensure that the new processing system architecture is developed to a level of function and efficiency that we are prepared to implement in the production environment. In the meantime, certain planned, new Real-Time Service Processing Systems will be developed and implemented according to the standard application interface design and operated on large mainframe computers. The benefits of physical modularity of the processing configurations will not be available during this relatively short phase (probably two years), but this constraint will be alleviated by the fact that the new Service systems will initially be implemented in the larger CPCs which have the load to justify large machines. Once the minicomputer-based distributive architecture is ready, it will be implemented in the smaller CPCs supporting the same Service systems and retro-fitted in the larger CPCs.

## 4.3. Other elements of the architecture

Apart from the communication networks and Real-Time Service Processing, the Inter-related Processing Network Architecture includes other major components as described in the first article: Electronic Data Control and Distribution, Scheduled Service Processing, Management Control Processing, Message and Document Control and Capture, and Document and COM Output.

All of these are well established operations, with the exception of Electronic Data Control and Distribution (EDCD); in this case, a subset of the target function is operational as two separate subsystems. The first distributes data sets from Capture to a multitude of application systems, and the second handles inter-centre (CPC-CPC, CPC-APC) file transmission, control and distribution. There will be a gradual enhancement and evolution of these functions to a unified EDCD system which will reduce file media handling (through the use of shared mass storage subsystems accessible from multiple configurations) and provide more automated control and status monitoring capability.

Scheduled Service Processing and Management Control Processing are largely mainframe-based. The design philosophy of new Service Processing Systems is tending towards the allocation of more processing responsibility to real-time subsystems, so that most transactions will be processed by them. During business hours these systems will process mainly terminal-initiated transactions. As branches begin to close and transactions captured from documents become available, these too will be processed by the real-time subsystems. They will pass transaction files to the scheduled subsystems, whose main responsibility will be analysis and generation of cyclic reports such as customer statements and control and management reports.

## 5. Conclusion

This two-part series has traced the development of a processing network architecture which we believe provides the Bank with the framework for the orderly and flexible evolution of our Service Production and Delivery capability. Essential characteristics include a common, application independent communication network architecture which allows terminal workstations to access multiple, independent Service Processing Systems; and an open-ended modular processing facility architecture which enhances service availability and facilitates the matching of processing capacity to actual processing loads. Additionally, we believe that the use of minicomputers in this architecture for real-time service processing will achieve significant cost reductions and greater reliability over a mainframe-based approach.

We intend to give further operational description and findings in a year or two, but we expect (and hope) to generate discussion and questions to which we shall reply in subsequent issues of the journal.
