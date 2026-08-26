---
otero_id: 24276
otero_key: "25PPQ6V7"
title: "Smart cards: a design for the future"
authors: "Robert H Davis; Hamish Mitchell"
year: "1996"
journal: "Journal of Information Technology"
doi: "10.1080/026839696345450"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Smart cards: a design for the future

ROBERT H. DAVIS and HAMISH MITCHELL
Department of Computer Science, Heriot-Watt University, Edinburgh, UK

A new smart card system, Vitesse, is outlined in design detail to meet many needs stemming from the current ability to manipulate information over the network medium. A new smart card operating system, object oriented in nature, is described in terms of a client/server architecture where clients (desktop computers) run front end applications and interact with information servers running in the background. Vitesse servers, designed to be portable – ranging in size from a credit card to a small computer – perform dedicated information processing with typical applications such as telecommunications, stockbroking and interactive entertainment. A design simulator is used to model the abstract design of Vitesse, allowing for prototyping of ideas and demonstration of design models.

## Introduction

Roland Moreno, a French journalist, is credited with conceiving the notion of the smart card in 1974, registering the first patent which described a smart card as ‘a card with a self-protected integrated memory’. When Dr Kunitaka Arimura recognized the growing importance of harnessing the power of technology within the form of a plastic wallet size medium, he too filed patents, only within Japan, defining smart cards as ‘a plastic card incorporating one or more integrated circuit chips’.

Moreno and Arimura created the genesis of smart card technology. This paper picks up the strings of their fundamental concepts and aims at providing a design for the next generation of smart cards using a redefinition of the smart card as 'a tool for the storage and retrieval of information in a secure environment; a tool which allows for the manipulation of the stored data, independent of any external processing device; a tool which provides a method of communication between the tool and its external environment'.

Here we focus on an operating system that may be used to drive the new generation of hardware and describe a simulator built so that applications and components of the operating system can be modelled.

This design has been given the name Vitesse and relates to both hardware and software, with the new smart card being controlled by VitesseOS and running on a hardware platform called VitesseWare. Before presenting the proposed design for Vitesse, background material will be presented to support the following summary which identifies key areas for enhancement and change in existing smart card design, along with objectives which the new design should meet in order to achieve success in the market place.

Table 1 identifies the major areas for change in existing smart card design, with more subtle enhancements being incorporated as the design evolves. To achieve a focus for the new design, a series of objectives is required, designed to maximize the prospects of Vitesse being selected when applied within the framework of a profitable business proposition. Outlined in Table 2 are the objectives and design criteria which Vitesse must match.

Above all, Vitesse must match the objectives of the client/server model by focusing on the end user, creating network transparency, making information a more productive commodity and allowing the system to grow with demand and technological innovation.

## Background

The combination of powerful, miniature, low cost technology has resulted in the evolution of the smart card: a card that has the ability to service multiple applications at the same time, to reduce fraud and counterfeiting, to facilitate encryption and decryption on and off line, to create a secure environment for personal privacy of data in protected memory and to offer a longer life cycle than conventional cards. However the most important attribute is that the technology is enhanceable and extendable.

The card has no fixed user base. Typical applications (Bright, 1988) currently being developed or in use are shown in Table 3.

The intelligence and memory capabilities of a smart card are supplemented by other facilities, mainly the ability of the card to communicate. This can be achieved through the use of a built in keyboard, input/output contacts on the card or a liquid crystal display on the card itself.

Table 1 Areas for change in smart card design

<table><tr><td>Current design areas</td><td>Enhancement or change</td></tr><tr><td>Powerful, miniature, low cost technology</td><td>Remove dedicated processors and use general purpose technology</td></tr><tr><td>Multiple applications/OS stay with card for its lifetime</td><td>Allow applications/OS to be changed and updated anytime</td></tr><tr><td>Widespread application base</td><td>Use new technology to exploit new markets</td></tr><tr><td>Resemble traditional credit card</td><td>Card can be of any size or shape</td></tr><tr><td>Keyboard, screen, contact I/O</td><td>Removal of all interfaces – add network communication port</td></tr><tr><td>Device reader required</td><td>All communication takes place via a network</td></tr><tr><td>Lock bit based security</td><td>Object oriented security – UNIX style protection</td></tr><tr><td>Limited life cycle, no hard/software changes possible</td><td>Improved life cycle through upgrades soft/hardware – data can be passed from one hardware platform to next</td></tr><tr><td>Survivability, compactness, ruggedness, portability, independent processing</td><td>Use new technologies to enhance these areas. Example – develop cards resistant to low temperatures</td></tr><tr><td>Processing of information</td><td>Exploit relationship of information and communication</td></tr></table>

The plastic in our wallets has become known as the first generation smart card technology, though under the previous definitions it cannot be strictly treated as ‘true’ smart cards. By having the original ‘plastic’ as the first generation, continuity in evolution of the technology can be achieved.

The early nineties see smart card technology in its third generation, but the current generation heralds the active card after the earlier passive generations. All cards by preconceived definition resemble a traditional credit or bank card in size and dimensions, though this is not essential. Embedded within each active card is a custom designed microprocessor for the tasks for which the card will be used. Different cards use different processors. These notions will be further abstracted and used in the fourth generation design presented later.

The second and third generation technologies have increased memory capacity, electronically erasable programmable read only memory, input and output, along with the ability to carry out independent authorization, when compared with the original plastic technology. All data passing between the card and the external system may be encrypted and decrypted in order to render the transmissions unreadable to any intruders attempting to intercept confidential information. The card can demand that the user provide a password before making any meaningful response.

Table 2 Objectives and design criteria

<table><tr><td>Objective</td><td>Criteria for Vitesse</td></tr><tr><td>Increased productivity</td><td>Improve the efficiency of information processing</td></tr><tr><td>Reduced system costs</td><td>Allow Vitesse to replace hardware already tied up with information processing, e.g. mail servers. VitesseWare uses no keyboard, screen, sound chip etc (therefore cheaper) and releases expensive hardware back into work place</td></tr><tr><td>Improved customer services</td><td>Portability of information and ease of access to information, e.g. for salespeople</td></tr><tr><td>New business opportunities</td><td>Allow application of technology to problems</td></tr><tr><td>Higher security</td><td>Object oriented security. Information restricted to authorized persons</td></tr><tr><td>Enhanced performance</td><td>Dedicated information processing: avoids combination of information processing and running of applications on same hardware platform</td></tr><tr><td>More effective management</td><td>Information is the most valuable commodity that exists – allow managers to exploit it</td></tr><tr><td>Decentralization</td><td>Vitesse must fit in with current corporate philosophy. Make use of client/server model</td></tr><tr><td>Lower operating costs</td><td>Simplicity of Vitesse</td></tr><tr><td>Hardware/software</td><td>Run on multiple hardware platforms. Information stored accessed from multiple languages</td></tr><tr><td>Network/communication</td><td>Vitesse will only communicate via a network interface. Able to communicate with all types of networks</td></tr><tr><td>Upgrade/replacement</td><td>All components of the hard/software can be updated at anytime to keep pace with technology</td></tr><tr><td>Maintenance/support</td><td>An operating system whose components can easily be modified. Client/server approach.Provide a powerful application programming interface to VitesseOS, to aid developers in programming new applications</td></tr><tr><td>Staff/user education</td><td>Provide an easy to use/learn interface to Vitesse. Aid productive use of Vitesse facilities</td></tr><tr><td>Compactness</td><td>The size of the card must reflect the power and performance</td></tr><tr><td>Conviviality</td><td>A socially acceptable product is required</td></tr><tr><td>Information processing</td><td>To be able to ‘evaluate’ incoming information</td></tr></table>

Table 3 Typical applications (from Bright, 1988)

<table><tr><td>Application</td><td>Examples</td></tr><tr><td>Finance</td><td>Electronic funds transfer, stock market, credit cards</td></tr><tr><td>Government</td><td>National identity scheme, taxes</td></tr><tr><td>Retail</td><td>Point of sales, deliveries, inventories</td></tr><tr><td>Security</td><td>Access to networks or buildings</td></tr><tr><td>Telecoms</td><td>Payphones, home shopping, banking, videotex</td></tr><tr><td>Leisure</td><td>Airlines, hotels, car rental, casino chips</td></tr><tr><td>Medical</td><td>Health profile, doctor/dentist details</td></tr><tr><td>Education</td><td>Campus facilities, libraries, progress reports</td></tr><tr><td>Maintenance</td><td>Aircraft, shipping, vehicles, customers</td></tr><tr><td>Transport</td><td>Subways, buses, taxis</td></tr><tr><td>Entertainment</td><td>Pay TV, cinema, theatre, leisure centres</td></tr></table>

The microelectronic circuitry of a smart card consists of a memory with a given capacity plus wired or micro-programmed logic to control and manage the read/write accesses to memory. The hardware enables levels of security to be built in before software is added. Memory access can be restricted, and types of memory can be made nonerasable to avoid deliberate or accidental erasure of information.

A common security feature found in most smart card memory architectures is to ensure the security of its own memory. This is done by dividing the memory of a smart card into several zones, each with a different security barrier to restrict access to each zone and to dictate actions that can be performed on the data stored in each zone. The smart card microprocessor and its associated operating system can keep track of which memory addresses belong to which zones and the circumstances under which each zone can be accessed. Currently smart cards have a four zone scenario: secret, confidential, usage and public zones. Permutations of these zones should provide any application with all the appropriate levels of security required.

The secret zone is usually reserved for the storage of information such as passwords, cryptographic keys, biometric data or any other confidential information which should be used only by the microprocessor itself. This zone is usually constructed in ROM memory format, to prevent external tampering or accidental erasing of data. The confidential zone should have a password known only to the card issuer and be used to store an audit trail listing all transactions, or attempted transactions, made with the card so that the issuer can examine the history of the card for evidence of misuse. The usage zone is used for information storage relating to specific data required by the application and is subject to periodic updates and modifications (for example, the date of the card holder's last access to the host, or the amount of computer time used). Finally the public zone is a region for keeping nonsensitive information, such as the card issuer's name and address. This zone is open with read access to all, but write access should be restricted. As an additional precaution against future interference, various time constraints can be imposed when the data may be written to each zone.

Each smart card's container comprises three physical items. The plastic carry case, the electronic chip circuitry and the surface mounted contacts. The plastic carrier is formed from a multi-layer laminate which is created through a combination of heat and pressure. The chips are held in the card by use of automated tape bonding, which seals the chips and contacts in a sealed envelope, providing protection against heat, contamination and electrostatic fields. The carry case must have heat dissipation created by the circuitry built into its design (heat created by the electronic circuitry).

Smart card chip technology followed the trends in transistor technology, taking advantage of new concepts that evolved so that with the arrival of complementary MOS (CMOS) technology high packing densities could be achieved. Newer high-performance CMOS chips allow the integration of EPROM and CMOS on the same chip (Clements, 1991). As elsewhere, developers face the dilemma of a cost performance trade-off.

The basic memory function requirements are: operating system instruction storage; temporary storage for immediate calculation ('scratch pad'); and zoned memory (long term storage).

The operating system instructions must be entered during fabrication and retained throughout the life of the card, even when no power is available to the card. This is achieved through the use of read only memory (ROM). Scratch calculations are performed in random access memory (RAM), due to its high access speeds. RAM is volatile, which means its contents are lost when the power is turned off. EPROM and EEPROM, standing for erasable ROM and electrically erasable ROM, are both non-volatile and form the silicon base for long term storage.

Communication of information stored in the card with the external environment is achieved in many ways. This is one area in which passive and active cards differ. Both generations of card can communicate by means of the contacts on the surface of the card, but active cards come equipped with a keyboard and liquid crystal display.

Contactless cards however have the benefit of placing the card reader behind a partition or affixed to the underside of a desk. Research into improving the range of contactless data exchange is opening up exciting applications. For example, security checks can be made anywhere in a building with remote sensors, or cards could be carried that equate to a travel pass. Cards are interrogated whenever the holder boards a vehicle. This type of card removes the need for a 'throat' on the card reader. It is a sealed unit, decreasing the chances for vandalism. The card works in any orientation, so there is no problem with physical orientation. Currently contactless cards are in the minority, when compared in volume to other types of smart cards. This is due to higher production costs, lack of standardization between manufacturers and the need to encrypt transmissions.

Second and third generation smart cards have a life cycle consisting of four general stages: manufacturing stage, application preparation stage, active use stage and retirement stage (Bright, 1988). With all secret zone passwords, keys and functional parameters set, the smart card is ready for use and can be presented to the card bearer. In the smart card's active use stage, information can be read from and written to the usage zone of the card's memory. This memory will normally be of EEPROM or RAM type. The smart card will remain in its active use stage until its memory is filled up or it has been invalidated. A smart card can be invalidated if several unsuccessful attempts at accessing a memory zone are made. Having entered its retirement stage, the card is no longer functional. The issuer may require that the card is returned or destroyed.

There are a number of projects reported concerning the introduction of smart cards including Visa (credit card), Citibank (Marbella Project), Midland Bank/Loughborough University, the USA Defense Department and the French Phone-In Service. Summaries and significant conclusions are described elsewhere, courtesy of Smart Card International Ltd (Mitchell, 1993).

## An overview of Vitesse

VitesseOS is an operating system that is dedicated to the storage, processing, retrieval and communication of information in a secure environment. Vitesse contains no graphical user interface, and runs on a hardware platform that has no keyboard, no screen, no sound, no interfaces except for a communications network interface. This keeps the cost of the hardware down, and enables Vitesse to reflect itself – speed. The Vitesse smart card is a physical portable device that can only be accessed via a network. Vitesse can be interrogated by another smart card, a terminal, a computer or any device on the network that has the ability to handle Vitesse's protocols. This expresses the notion of a client/server relationship.

At the heart of every smart card is a processor. This is an arena that is rapidly emerging, with new technologies appearing every year. Currently the market is split into two major schools of thought, the CISC and the RISC. Intel is a major player in the complex instruction set computer (CISC) market, with current processors such as 80386 and the 80486, though these are soon to be superseded by the Pentium. The chief characteristic of these processors is a large number of instructions, now complemented by speed and power. CISC's main rival is the reduced instruction set computer (RISC). This works on the principal of simplicity in the design of instruction set, faster clock speed and consequently higher execution speed. To exploit these and other hardware advances, it is necessary to create an OS that is portable from one hardware platform to the next.

The processor is complemented with a simple range of hardware peripherals: a network interface; an OS storage and working store; and a long term store.

With the notion carried forward that smart cards will vary in size and application, Vitesse will have to cope with scalability. The network interface may be a simple set of contacts as in second generation technology, or a high speed fibre optic link. The operating system may be stored in ROM, or loaded from the network or from backing store. Finally Vitesse will have to cope with varying storage requirements. Applications may require a small EEPROM chip or a 100MB hard disk. It can be seen that a smart card could stay the same size as a modern credit card, or increase up to the size of a small portable computer.

## Properties of VitesseOS

Market requirements and demands of a product are always changing. Unless products adapt to changes in the market, they will lose their competitive edge. Changes come in the form of new hardware devices or support for developing new software technologies, such as object-orientation. To allow VitesseOS to expand over time, techniques originally developed for the Mach operating system at Carnegie-Mellon University will be used (Clapp, 1990). Vitesse will make use of a core kernel, providing the primitive operations for the card. The kernel will be supported by a series of servers which provide additional system capabilities. The core is stable, while servers can change over time to deal with new requirements.

A modular approach for design will be used where individual components communicate only through the use of interfaces. Applications communicate via an application programming interface (API), while servers make use of a server router in the kernel, whose main task is to interpret messages between different servers and pass them on.

Another key feature will be the device server, which will allow for loadable drivers to support new file systems, devices and networks.

Portability enables the entire operating system to move to a new hardware platform with as little recoding as possible. Vitesse was designed to be easily portable, enabling developers to make use of processors and hardware configurations ideal for their particular application.

Vitesse follows a series of guidelines to ensure portability. As much of the code as possible must be written in a language that can be compiled on all the processors that will want to run Vitesse. This usually entails a high level language, and hopefully one that has been standardized. The obvious choice is ANSI C, which is widely available across multiple platforms. Assembly language is only used for parts of the OS that communicate directly with the hardware, or written for optimum performance.

Awareness of the physical environment which Vitesse will be ported to means different hardware and different constraints on the OS. A classic example is porting an OS designed for 32-bit address access to a 16-bit environment or processor dependent data structures and registers. It is important to minimize the amount of code that interacts directly with the hardware. To overcome the problems of hardware dependent code, a hardware abstraction level (HAL) will be created. Hardware dependent code should not be spread throughout the system, but located in easily found modules.

Vitesse will protect itself from both internal error and external tampering. It will behave predictably at all times, and applications will not be able to harm the operating system. Exception handling will be used for capturing error messages and responding to them. Robustness is enhanced by using modular design, with each module communicating via predefined APIs. A security architecture will be in place which provides a series of mechanisms such as user logon, resource protection and auditing. The operating system is protected from applications due to features found in microprocessors, such as the distinction between supervisor/kernel mode and user mode. This combined with memory management hardware means applications can have their memory accesses restricted.

Within the constraints of these features, Vitesse must operate as fast and responsively as possible on each hardware platform. Application interfaces must be clean and efficient, and message passing through the kernel server router must be quick, as message passing is a major performance overhead.

## VitesseOS - the model

Vitesse uses multitasking to control execution of its applications or processes. Each process executes for a short period of time before control is passed to the next process. Each process can have memory and resources allocated to it. In addition to sharing out the processor's time, the operating system controls access to files and devices. When creating a new OS, it is important to create a model which blends all elements of the proposed system into a cohesive form. The model can be used graphically to appraise a system, and to ensure that the objectives of the system can be accommodated without compromising the design goals. In the world of operating systems several models exist – monolithic, layered and client/server. VitesseOS does not fit directly into any of these categories, but has become a hybrid of several.

With the main goal of VitesseOS focused on the processing of information, it seems logical to design the OS around the needs of data and to create software that allows for easy and cheap modification of that data. A large proportion of software costs is attributable to maintenance which includes new features, modifying data formats, bug correction and accommodating new hardware. This is where client/server use is advantageous since parts of the system can easily be isolated and modified. Other features can be developed through the use of object orientated design thus minimizing changes by hiding physical representation of data within objects (since an object is a data structure whose physical format is hidden behind a type definition). In this way every object has a set of formal properties called attributes, and is manipulated by a set of services (Coffin, 1988).

Vitesse takes these fundamental object concepts and incorporates them into its design. All system resources – files, memory, devices, programmes, servers – are implemented as objects and manipulated by object services. This approach lessens the impact of changes that could be made to the system over time. For example, if hardware change forces alterations to be made to the OS, only the object representing the hardware and the services that use that object need be recoded. All code that uses the object remains the same. Similarly, a new resource can be added to a system by creating a new object and new services.

Vitesse is a hybrid of the layered and client/server models (see Figure 1). The whole operating system revolves around the relationship between clients and servers, while individual servers use notions of layered design. Of course servers do not have to stay strictly layered based, and can incorporate client/server techniques into their design.

Vitesse splits itself into two main sections: those parts of it which run in supervisor mode and those which execute in user mode. All applications are restricted to user mode to provide a secure environment for the main kernel. Non-applications which are part of the OS can also run in user mode, like the card access system (CAS). These are clients/servers which do not need the benefits of supervisor mode.

![](/api/attachments/25PPQ6V7/fulltext/images/179e8e1d98cc7dc375b30e3bfc163a631cce497f461d228f6e251c9009be87c5.jpg)  
Figure 1 VitesseOS: client/server model.

All applications and servers run in a multitasking environment provided by the information technology executive kernel (ITEK). All applications request services of the operating system through the smart card application programming interface (API) server. The API switches the processor between user and supervisor mode, passing the request on to the ITEK. The API decoder in the ITEK decodes all requests, passing them on to appropriate parts of the kernel. The ITEK contains a program execution manager to control the multitasking environment, and a server manager to control the passing of messages between servers. The hardware abstraction level (HAL) places a layer of code between servers and hardware, hiding hardware-dependent details. This is one of the most likely layers to be removed and exchanged when porting across platforms.

The ITEK calls on the services provided by dedicated servers. A key server not found in many operating systems is the database management server. This uses a structured query language for interaction and stores data by use of objects. The security server is designed to protect the system from attack and provide data integrity. The information server is designed to interpret the meaning of information and control the flow of information in and out of the card. This server is used if Vitesse is hooked into an information network and the flow has to be controlled. All objects used within the system have to have a level of administration placed on them, and this is provided by the object manager. Finally all file systems and network devices are handled by the device manager.

## Information technology executive kernel

The kernel provides the most fundamental operations in VitesseOS, determining how the rest of the operating system uses the processor and ensuring the smooth running of message communication and access to hardware. The kernel is like the hub of a wheel, the centre of the operating system, around which everything revolves. It is constructed from layers of code, each layer relying on the previous, more primitive layer. The whole OS relies on the correct and efficient operation of the kernel.

The VitesseOS kernel became coded as the information technology executive kernel (ITEK). Its objective is to provide a low-level base of well defined, predictable operating system operations. Access to the kernel is provided through an application programming interface. The VitesseOS ITEK borrows kernel design concepts from the Mach kernel, part of a UNIX operating system. Mach provides a lean, clean, powerful kernel. Vitesse follows the same route as Mach and introduces system features through a client/server system (Clapp, 1990).

ITEK is split into four main modules: application programming interface decoder; program execution manager; server manager; and hardware abstraction level.

All clients of the ITEK communicate via an API. The API simply provides a set of primitives and interfaces that control access to the ITEK and its resources. The job of the API decoder is to interpret legitimate API calls to the ITEK, and decide which part of the ITEK or its associated servers would best be suited to serving the request. Policy decisions can be implemented and updated here. The decoder is a simple but intelligent router, responsible for the passing on of requests.

Early versions of operating systems, like MS-DOS, could only run one program at a time. Vitesse overcomes this problem with the ability to execute more than one program on a single processor at the same time. In Vitesse a program or application is referred to as a process, and the technique of multiple execution is known as multitasking.

Each process in Vitesse is handled as an object to remain consistent with providing a secure environment and dealing with resources. Each process in the system is identified by means of an object, described in the section about the object server. At an abstract level a process can be defined as: an executable program, which defines initial code and data; a private address space, which is a set of virtual memory locations; a program with associated system resources such as communication ports.

The program manager uses a basic memory handling technique known as virtual memory. The problem lies in making this technique scalable over multiple hardware platforms, where the ability to handle virtual memory may be restricted. For example a standard smart card, with only 32k of RAM for all storage requirements, would have great difficulty in handling virtual memory, whereas a system with over 100MB of storage would provide an ideal environment. To overcome this problem, programs can execute in either one of two environments. They can either restrict themselves to physical addressing, found in operating systems that do not have virtual memory, or they can execute in a virtual environment. All applications must operate in the same environment.

To achieve multitasking, Vitesse uses the following simple scenario (Tanenbaum, 1987):

(1) A process is executed until the process is interrupted or until the process must wait for a resource to become available.

(2) The context of the process is saved.

(3) The context of the next process is loaded.

(4) This process is repeated as long as there are processes waiting to execute.

Switching between processes is known as context switching. The manager constantly switches between processes, and the sheer power of the processor gives the illusion that all the processes are running at the same time.

Vitesse makes use of preemptive multitasking. It is a form in which the manager does not wait for the process to voluntarily yield the processor to another process. Instead, the manager interrupts a process after the process has run for a preset amount of time called a time slice or time quantum, or when a process with a higher priority arrives, ready to execute. This method prevents one process from monopolizing the processor.

The execution manager uses a priority based scheme to select the order in which processes execute. Higher priority processes execute before lower order. The manager will alter the priority of individual processes periodically to ensure all processes execute. All processes within the system are held in one of six states (Tanenbaum, 1987):

(1) Ready: when looking for a process to execute, the manager considers the pool of applications in the ready state.

(2) Standby: this is the process selected to be executed next. When the correct conditions exist, the manager context switches to this process. Only one process can be in standby mode at a time.

(3) Running: once a process has been context switched in, it enters the running state and executes. The execution continues until the kernel preempts it due to a higher priority process being ready; its time slice expires, it terminates, or it voluntarily enters the waiting state.

(4) Waiting: the process is awaiting the availability of a previously unavailable resource to become available. If the resource is directly available it enters the ready state otherwise it enters the transition state.

(5) Transition: a process arrives in this state if it is ready for execution but the resources it needs are not available. Once the resources become available it will reenter the ready state.

(6) Terminated: when a process finishes execution it enters the terminated state. The object manager will then be told to delete the process object.

To control execution the execution manager uses a priority coding system to determine order, scheduling higher priorities before lower. On creation, a process is set a default priority, depending on current ready applications and priority value assigned by the process creator. The manager maintains a database of processes, keeping track of waiting, ready and executing states, along with assigned priorities. When the manager is scheduling the processor it starts at the highest priority value (ten) and works towards one, until it finds a process with a matching priority value. This process then joins an execution queue. Priority zero is reserved for system use. Processes with priority values between one and ten are called variable priority since the execution manager can alter their priorities to optimize system response time.

Above priority level ten, the potential exists to implement real time operating systems. Links will exist within the manager to allow for real time applications, but currently VitesseOS will not support the execution of real time processes (Custer, 1994).

The scheduling process occurs in one of the following situations: when a process enters the ready state; when a process's time slice finishes, terminates, or enters the wait state; when the execution manager alters the priority of a process; or when a process with a higher priority than the executing process arrives.

When a process switches context, the following saving and restoring of data occurs within the following low-level processor hardware components: program counter; processor status registers; other register contents; user and supervisor stacks; a pointer to the address space in which the process runs. To execute a context switch, the above information is pushed onto the ITEK's own stack.

The programme execution manager also provides services for interrupt and trap handling, by providing simple interrupt service routines and error detection routines, when exceptions occur.

The server manager is responsible for the communication of messages between servers. All messages pass through the server manager. A server must inform the server manager of its presence, creating a connection port. The manager creates a port object, described in the object server section, for each connected server. To communicate with a server, each client application places a call with the server manager to be connected to the server's port. A successful connection establishes a handle between the server and the client. The channel remains open until either party, or the server manager, closes the connection.

The communication channel is a two-way 'highway' allowing the server to communicate information back to the calling client. Data transfer is established by means of shared memory techniques. Each communication port has associated with it a transfer buffer, which is addressed via the handler. The server manager informs both parties of replies, or sends, allowing each party to access the shared memory. To stop both parties accessing memory at the same time, lock bits are established controlling which party has read or write access. The server manager draws on services provided by the program execution manager to handle shared memory (de)allocation.

A layer of code is placed here between the operating system and the hardware. It hides from the OS hardware-dependent details such as I/O interfaces, interrupt controllers and machine dependent code. The HAL contains a basic set of primitives for low level access to the hardware, such as controlling the floppy disc controller to load/save sectors on a disc. The primitives are consistent across all hardware platforms, but due to their nature the code is not. Low level system software is usually coded in assembly language, which is processor dependent. Grouping machine dependent code in one module allows for the easy modification of software when porting. Only one module has to be recoded, not various parts of the OS. The HAL is the only method for accessing hardware directly. All access directly to hardware must be through the HAL. This restricts the likelihood of side-effects from unauthorized code.

## The application programming interface server

The application program interface (API) server is a process created by the ITEK in user execution space. The API allows application processes to take advantage of sophisticated operating system capabilities, accessing dedicated servers, and addressing the problems of hardware interaction. Applications and the API server go through the following interaction stages:

(1) Application is a client process to the API server

(2) Client passes message to API, requesting OS facility

(3) API server validates request

(4) API server causes exception to occur

(5) Processor switches from user to supervisor mode

(6) API server becomes client to ITEK

(7) ITEK services application request, returns results to API

(8) API server passes results to client

The API provides a whole host of different functions, for several reasons. The API removes the need for application developers to code low level functions, especially hardware access. It provides a control framework, restricting the abilities of user-mode processes, ensuring the safety and integrity of stored information. Services are made available to developers which would be complex, difficult and time-consuming to write. Finally, the API creates a standard set of interface mechanisms, in the form of an abstract data type. This allows for the interface to function consistently whilst allowing system developers to change the code behind the function.

Deciding which function interfaces should be made available to application clients through the API server is a difficult task. Services should be made available that will cover all the demands of system developers. Too many functions make Vitesse become large and slow, while too few and developers will find writing applications a very slow, difficult and time-consuming task. To overcome this problem, Vitesse introduces a 'function library' into the API server. This library contains all the functions available, and the parameters required by each function. It is the job of the API server to check that application client messages are consistent with the prototypes held in the library. No attempt is made to check the semantic content of the messages, just the syntax. Semantic decoding is left to the ITEK and its associated servers. If a message is found to be syntactically correct, the API server passes the message onto the ITEK, or an error message is returned, identifying the errors in the message structure.

The contents of the library vary depending on which servers are present, which devices connected, and the versions of ITEK available. This occurs due to the way the library is constructed when the API server process is created. Library creation takes the following steps:

(1) API server process created

(2) ITEK contains one consistent function: POLL

(3) API server requests execution of POLL service

(4) Results of POLL service are placed in library

(5) API server awaits messages

The POLL service in the ITEK interrogates all servers connected and known to the ITEK server manager. The

POLL service requests from each server the prototypes for functions available to users. Every server is obliged to release this information, which should be included by the developers. The ITEK is also questioned, and returns its list of available functions. If a server does not release its function prototypes then an application will not be able to use it since it will not be in the library. Problems will occur in the porting of applications when a system is encountered that does not provide the expected function prototypes, probably due to a server not being installed. The main benefit of using a control library is that it hides internal function calls from user applications, enabling a level of control to be placed on function access.

To enable applications to know if a server is present on a system, the ITEK has a guaranteed command: SERVER <name>. This allows applications to deduce whether certain facilities will be available to them during execution.

## Card access system

The second process created by the ITEK is the card access system (CAS), and is executed in user space. Like user applications, the CAS becomes a client of the API server for ITEK access. The CAS provides a mechanism for controlling access to Vitesse. The CAS builds upon the concepts of client/server computing explained earlier. Vitesse is considered to be a server, while users who access the smart card are clients.

Every client on the network must be executing an interaction manager. These managers are small, efficient sections of code, responsible for constructing packets of information to be sent across a network, and receiving information sent back by the server. Vitesse contains its own interaction manager, though different to the clients, since Vitesse can make use of client servers available in the kernel. This attribute allows Vitesse to become a client to any other server on the network. Applications can use the CAS to communicate with other smart cards and machines running interaction managers.

Every transmission between client and server over the network takes the form of packets. Every packet is constructed in an identical fashion and contains the information shown in Table 4. The header allows the CAS to determine the purpose of the incoming message, and decide upon the most appropriate action to take. To allow this to happen, the CAS maintains a library of 'headers' and a list of API calls to execute in relation to a particular header. A standard set of headers is available for use by client applications and could take the form of SQL, PROCESS, KILL etc. An SQL header would result in an API call to the database server.

The destination address forms part of a network addressing scheme, which allows for the correct routing and delivery of messages.

Error detection and correction is a vital part of networking. Ensuring the integrity and security of information in transit is vital. Checksums are included in the packet, and used by the CAS or interaction manager to check the contents of a packet. Multiple checksums and error checking systems exist, so the first byte of the checksum field is an identifier for the checksum system being used. For example 00000001 may be cyclic redundancy check, while 00000110 will represent parity checking.

The security descriptor is a data structure created upon execution of the interaction manager. It reflects the privileges available to the client to perform operations on a particular server. Each interaction manager will have stored a list of security descriptors, depending on the server and action chosen by the client. Security descriptors are issued by developers or can be created by information systems managers. Each security descriptor is encrypted to prevent alteration, and embedded within each interaction manager. The contents of a security descriptor are described later.

It should be noted that the executable interaction manager program itself must be kept secure, either within a secure environment like UNIX or on a floppy disc held in restricted access when not in use. Interaction managers are like cash cards. They are a means of access, and must be treated with care and respect.

The following are steps taken by the CAS client:

(1) Message received by the hardware;

(2) ITEK informs the CAS via the server manager;

(3) CAS instructs the device manager server to handle the incoming message;

(4) Device manager verifies the message;

(5) If message is for this particular smart card, control is passed back to the CAS;

(6) Vitesse controls data by objects;

(7) Object manager is instructed to create a PACKET OBJECT called packet x;

(8) x is an incremental number each time a new packet arrives;

(9) Object manager copies security descriptor from packet to header of object;

(10) Object type is defined as OBJECT;

(11) CAS opens a handle to the packet object;

Table 4 Packet field description

<table><tr><td>Packet field</td><td>Description</td></tr><tr><td>Header</td><td>Stores type of message being transmitted</td></tr><tr><td>Destination address</td><td>Allows messages to be routed correctly</td></tr><tr><td>Checksums</td><td>Determines whether errors occurred</td></tr><tr><td>Security descriptor</td><td>Stores client security information</td></tr></table>

(12) Proceeds to copy the contents of the packet into the object body;

(13) CAS references packet header type;

(14) CAS internal library checked for header type; and

(15) Corresponding API instructions executed.

No security checking is done by the CAS. This is left solely to the object server, which works in conjunction with the security server to ensure the integrity of the system.

## Design of Vitesse - object server

Vitesse requires a system that is responsible for the creation, deletion and manipulation of Vitesse objects. To serve these processes the ITEK makes use of an object server which provides a common, uniform mechanism for controlling system resources (Clapp, 1990; Custer, 1994).

To the ITEK, an object can take on the form of hardware resources, memory, software applications and stored data. The main benefit of using objects is that the internal structure of an object is hidden from view. An object service must be used to get data out of, or place data in, an object. This allows the separation of the underlying implementation of the object, from the code that uses it. This allows for implementations to change over time, but keeps the interfaces consistent.

All objects created in the system are of a particular type. This type determines the data the object contains and the services that can be applied to the object. Type examples are shown in Table 5. To manage all objects uniformly, every object has a header which contains a standard set of fields. These fields allow the object server to ignore the rest of the data encapsulated within the object. Vitesse uses the object header shown in Figure 2.

Object names are used as a means for distinguishing one object from another, as well as providing a method for finding and retrieving an object. When an object is created and given a name, the name is filed into the object server's global library. This library depicts all objects existing within the system, and allows other processes to share objects. By specifying the object name, the server locates the name in the library, and then creates a handle to the object. If an object is not meant to be visible to other processes then a name should not be given and the object will be held invisible. The only other instance when the object name is used is at creation, when name conflicts in the object library are checked for.

Table 5 Examples of object types

<table><tr><td>Object type</td><td>Definition</td></tr><tr><td>File</td><td>An instance of an opened file for I/O</td></tr><tr><td>Port</td><td>Buffer area for the passing of messages</td></tr><tr><td>Process</td><td>An application with resources allocated</td></tr><tr><td>Server</td><td>Identifies application as a server</td></tr><tr><td>Packet</td><td>Defines a packet message on the network</td></tr></table>

Handles are used to increase the efficiency of accessing objects, removing the need for the object server constantly to look up names in the object library. When an object is created the memory address of the object is placed in the object server global library. So when an object opens a handle to another object, the address is copied from the library into the handle library in the header of each object. The handle returned is an index into the handle library, allowing fact access to objects. When an object has opened a handle to another object, and performs an action on that handle, the object server simply uses the supplied handle as an index in the handle library to find the memory address of the desired handle. The action is then applied to the requested object.

The object model used by Vitesse was chosen to provide enhanced levels of security over other OS designs. When an object is created it inherits the privileges of its creator. A security descriptor is used by the security server to determine whether requests by an object to open a handle to another object can be executed. The security descriptor is described in more detail in the security chapter.

The object type determines the structure of the rest of the object. Each object type is defined in an internal library, along with the actions that can be carried out on an object of that type. For example, an object of type PROCESS, may have the actions EXECUTE,SUSPEND,WAIT, etc. All actions are available through the API, and action/type checking is done by the object server.

![](/api/attachments/25PPQ6V7/fulltext/images/86fa4acfc18cd46a56ed32472eaba485a8269a42d234b79965c5d8ed0a7fe25d.jpg)  
Figure 2 Object header.

## Objects calling the object server

Objects call the object server either to create, delete, open a handle to, or execute an action on, an object. The object server checks that the call to an object server is legitimate by referencing an internal library which holds all action/type calls, and the privileges required to execute such an action on an object of a particular type. If privileges are required then the object server calls on the services of the security server to verify that the calling object has the appropriate security descriptor.

## VitesseOS - the remaining servers

## Security server

The Vitesse security system provides a system of priority access combined with auditing facilities to monitor all interactions between objects. Since everything in the system, applications and data, are represented by objects, and the object server requests authorization from the security server on all object interactions, the security server becomes a gate through which all clients of the smart card must pass.

Every object in the Vitesse system has an associated security descriptor in its header. This field itself is split into separate parts. Each part can be assigned a value, or priority. Priorities range from zero to ten, low to high priority respectively. Fields within the descriptor are general, and the meaning applied to them depends on the object type. A typical security descriptor, in abstract form, may look as in Table 6.

Fields of the security descriptor are 'low-level' in that they control the most basic access rights. For example, if an object was granted write access over a file object, then the APPEND command would be interpreted by the object server as an action requiring write access to an object. The descriptor list could easily be expanded if the need for extra security privileges required it.

The creation of privileges allows for a notion of user groups to be created. All clients of the smart card can be split into eleven groups (0–10). This enables restrictions to be placed on different clients as to what data objects they can access, and what applications they can execute.

Priorities within the system can only be altered by a special security descriptor with client ID-ROOT. This descriptor has its priorities set at ten for create, delete, read and write. This means that the owner of the interaction manager with ROOT security descriptor can access and control objects on any smart card. To overcome this problem, a library exists within the security server that lists all the client IDs allowed on the system. The library can be extended to hold all of the client IDs allowed to access the system. If it is found that other interaction managers with identical IDs are accessing the system when they should not, a random string of characters can be added to the client ID. This is stored in the interaction manager and the security library, but is never displayed anywhere else. The random string acts like a password in normal security environments.

Table 6 Typical security descriptor

<table><tr><td>Descriptor field title</td><td>Description</td></tr><tr><td>Create</td><td>Used to check for privilege to open a file, create a process</td></tr><tr><td>Delete</td><td>Used to check for privilege to delete a file, terminate a process</td></tr><tr><td>Read</td><td>Check field for right to read a file</td></tr><tr><td>Write</td><td>Check field for right to write to a file</td></tr><tr><td>Client ID</td><td>Identifier of client who owns the object</td></tr></table>

The job of the security server is to verify the specified security descriptors on specific fields, as directed by the object server. Also the server can check the client ID library if indicated to do so.

The final task of the security server is to compile an audit log. These files keep a permanent record of events occurring in the system. Logs act as a useful deterrent to would-be penetrators, and can be used to analyse trends in user access to particular objects.

## Device manager server

The device manager (DM) server provides a uniform, high-level interface for applications and other servers. It protects its clients from differences in physical devices and organization of data. The DM works in conjunction with the hardware abstraction level (HAL) which provides the low-level code needed in device management.

Devices within Vitesse such as the network interface and backing store are controlled by drivers. Drivers are portable and written in a high level language to remain consistent with the main design objective of Vitesse. The drivers are also designed to recover gracefully after a power failure and restart interrupted operations.

The DM's first objective is to provide multiple file systems. Examples of existing file systems are: FAT (file allocation table - MS-DOS); HPFS (high performance file system); CDROM (optical storage file system); and SunNFS (SUN MicroSystems net filing system).

Many more systems exist, and the one selected depends on the application, the needs of the application and the backing store medium being used. These filing systems provide high level access and in turn request services/functions of the HAL, for example reading and writing sectors on a floppy disc.

## Power failure recovery

If Vitesse were to experience a power failure, any data stored in a device register or buffer can become corrupted, and the device itself can be knocked offline or reset to a random state. With all device drivers in Vitesse operating in supervisor mode, a power failure can cause serious problems. To overcome any potential difficulties a number of counter measures are employed:

(1) Device driver must know when power failed – high priority interrupt

(2) Device reset to a known state after power failure

(3) Any I/O operation that was interrupted should be restarted

(4) If 3 is not possible, error message should be returned to client

The device manager works in conjunction with the ITEK to allow device drivers to fail gracefully in the instance of power loss. When power fails, a brief instance occurs when the ITEK has the opportunity to copy all important memory registers into battery backed up RAM. When power resumes, this stored information can be used to resume execution.

When writing data to a device, a drive should mask out the power failure interrupt to ensure that time critical writing sequences are not interrupted. This also means that if a power failure occurs partway through a write sequence, then the sequence will be restarted when power resumes.

## Network management

The second device management system required by Vitesse is network management. The proliferation of large networks and the need for users to communicate and share databases of information has elevated networking software from the realm of usefulness to the realm of necessity. Networking is an integral part of Vitesse, and is optimized for speed and efficiency. The network device driver works towards the concept of open systems, supporting different network architectures. To create this scenario, Vitesse adopts the notions put forward in the open systems interconnection (OSI) reference model. This is a software model put forward by the International Standards Organisation for sending messages between machines that originate from different manufacturers (Sheldon, 1990, p. 24).

Vitesse's integration manager calls upon the services of the network device driver, located in the device manager server, which in turn uses other parts of the system – such as the HAL for the data and physical level.

By designing the network driver in layers, and using standard interfaces between each layer, invoking implementation hiding, layers can be substituted if requirements of the network driver change.

## Information server

A phenomena created by the information technology revolution is 'InfoJunk', the worldwide electronic circulation of packets of largely unwanted information, and one that is about to explode with unknown quantity. To combat this problem, applications can call upon the services of Vitesse's information server. This server is used to analyse incoming packet objects, determining their importance and evaluating their usefulness. The need for the server is application dependent. For example a simple diary, address system would have no need for the server, while an application scanning packets from a news agency, like Reuters or Teletext, may want to know only about financially related issues like stock prices, interest rate changes, etc. A filtering mechanism is required to separate the required from the unwanted.

The information server contains lists of keywords, phrases and numbers, along with semantic/context checking details. The server searches packets, using templates created from the list. Boolean operators can also be applied, ensuring whether or not a packet contains a combination of keywords. The server is programmed to accept or reject packets according to whether they match the criteria in the stored lists. Applications inform the interaction manager of the need to route all further messages through the information server.

The concept of the information server is still in its infancy, with techniques for text analysis still at the research level. Effective techniques are available that can be used to perform levels of data searching and extraction, but notions of semantic checking still lie in the hands of artificial intelligence.

## Database management server

At the heart of the Vitesse philosophy is the manipulation of data. To provide a mechanism that can accommodate the manipulation requirements, a server will be required to handle all the information processing (Date, 1990). Vitesse ‘subcontracts’ this work out to the database management server (DBMS).

The DBMS has some inherent levels of complexity that must be considered:

(1) Different clients may want to use the database at the same time.

(2) Different clients require different interfaces to the database (forms, queries, programs).

(3) Different users may require different levels of access.

(4) The system tries to avoid the problems of data corruption if server crashes.

To solve these problems, VitesseOS's DBMS is designed to conform to a three-level architecture, which allows for one aspect of a database to be changed without impacting on the others.

The conceptual level provides several key facilities, including data definition language (DDL) and data manipulation language (DML). The DDL provides facilities such as the update statements of SQL, while the DML consists of statements such as the SQL query command. These languages make use of lower level facilities supported by the internal level, and underpin facilities in the external level.

The internal level includes the following features: data structures for storing relations in backing store; query optimization for declarative query languages; concurrency support for multiple users; recovery support; and an interface onto the underlying operating system.

The internal level is the 'meat and bones' of the DBMS, and optimization of the facilities provided here is critical to the efficient and smooth running of the system. This is where the DBMS introduces facilities available from other parts of the system. The object server and the device manager server control the structure of stored relations, and how they are organized in the backing store. An interface to the internal level is provided through the API server for applications, and multiple users/clients are organized via the program manager as clients and are treated as objects, and also treated like process applications allowing for concurrency. Internal concurrency relating to file access is essential to ensure the correct order of access and updating of stored objects. All transactions on the database are controlled by locks which limit the reading and writing of files, to ensure no side effects occur due to multiple client access on one file.

The third level of the DBMS is the external level, where the global view and user perspective of the underlying data is provided. This perspective may be unique to the individual user, as access to parts of the database or individual data objects may be restricted. This is where security priority levels can be implemented to control access to data objects. SQL commands exist to control access to individual fields in an object.

To allow client access to the DBMS, a number of tools can be provided which bolt onto or use the interaction manager. These are: interactive SQL; C language interface; and a package for creating form based interfaces. These tools provide different levels of access to the database API calls provided by Vitesse. They enable multiple applications to act as a front-end to a smart card.

## Overview of DBMS

The DBMS follows the relational database model. A relation is basically a table of data, with one or more named columns which define its attributes, and zero or more rows whose contents are commonly known as tuples. To access relations, applications and clients can make use of the standard query language (SQL), or C-based applications linked into the API server.

The relational approach has specific advantages that accrue from the notion of centralized control: redundancy can be reduced, inconsistency can be avoided, data can be shared, standards can be enforced, security restrictions can be applied and integrity can be maintained.

If the relational model is not acceptable as a DBMS, then as a consequence of the client/server arrangement, new DBMSs can easily be installed (for example, persistent, deductive, or functional based). The query languages interrogating the database must match the DBMS being used, for example Prolog queries will not work with a SQL relational database.

## Vitesse - design applications

The possibilities for applications based upon the designs for Vitesse given over the previous sections are extensive. The following examples are intended to explore and explain different parts of the smart card design in a practical context.

## Stock broking - share portfolio analysis

The stock exchange has moved with the times such that with the revolutionary big bang in the city, information technology is so widely in place that the stock market is no longer just for the institutional investor but now the ordinary man in the street can buy and sell shares freely and easily. Easy management of this share portfolio can be achieved by a fourth generation smart card to handle portfolio updates as well as a statistical analysis of shares.

Hooked up to a network, an application polls the share prices for the stocks held in the portfolio, while another statistical application analyses changes in share prices, evaluating whether to buy or sell. Another application, in conjunction with the information server, analyses information over the network from news agencies, such as Reuters, looking for information which could affect share prices, such as employment figures, the latest inflation index, or interest rates.

The powerful statistical and analytical applications operate side by side on the shared data held in the smart card. Recommendations to buy or sell are held in the database until the user logs on to the smart card, via their own personal computer. If the recommendations of the application are to be ‘trusted’ then the smart card can be programmed to buy and sell shares over the network.

For on-the-move analysis, the smart card is portable and can be updated by being linked with a portable telephone, and data accessed by a speech synthesis application in the smart card, which uses the telephone as an output device. Input is via the keypad on the telephone.

Due to the nature of the client/server application relationship, more sophisticated analysis programmes can be uploaded by the user at any time. In the near future this may take the form of neural net analysis programs, which will attempt to use intelligence to analyse share movements, looking for patterns and building upon the experiences of city traders.

## Telecommunications

To create a telecommunications smart card, Vitesse would need the services of a high capacity network interface, capable of connecting with the latest in optical fibre cables, along with standard telephone networks. The backing store utilized would be of optical or hard-disc type in nature, with high transfer and access speeds, capable of storing fax, telephone, email and multimedia messages.

Applications would consist of managers designed to store, archive, encrypt and manipulate incoming messages and requests. Use could be made of the information server to filter out unwanted mail or messages.

## Security

A truly portable Vitesse based smart card could be designed to be worn by staff or employees in a building. Typical data stored would be name, address, employee number and biometric data (signature, fingerprint, retina, etc). Communication would be via a radio based interface, allowing security cards to be interrogated freely. The issue of 'Big Brother is watching' raises its head here. People can feel they are constantly being monitored with this method of radio interfacing. Following a person's movements becomes very easy. This is an issue of personal privacy which will have to be dealt with, probably through legislation.

This type of smart card has many applications, typically where an identification has to be made – for example, bus passes, national identity schemes for animals or humans, or driving licences. Here the opportunity arises for the government to combine currently separate documents into one. Everybody could be issued with a smart card holding medical details, employer information, driving details, and so on.

## Credit/charge/bank cards

For many years people have been used to carrying around cheque books, and according to surveys by banks the majority of the general public do not find the size of the cheque book obtrusive or bulky. From this we can conclude that banking smart cards would not need to be confined to the typical credit card dimensions, and if the need arises then size can be increased.

A bank Vitesse card would handle all accounting functions, credit limit checking and signature/biometric comparisons when a purchase is made with the card. In essence this card is a portable bank. Money can be moved from account to account, bills paid, balances requested, etc. All these functions are carried over the network from the home to the bank. Security is achieved since the card is issued with the user's biometric security details already pre-programmed.

## Cars/aircraft/shipping

As all means of transport become more complicated to control and maintain, engineers require a new way of creating control, and having a record of performance. In response to this need a car, for example, could have a series of Vitesse-based smart cards installed. A central smart card is responsible for collating information from a series of smaller smart cards which are connected to the engine, suspension, lights, air conditioning, etc, and then determining the best course of action to refine or enhance the car's performance.

Each local smart card is responsible for maintaining its 'component' within the limits set by the central smart card. By using a single network cable throughout the car, the need for a complex wiring loom is removed. For example, the user indicates left, so the central smart card is informed of this choice and sends a message down the network to the smart card supporting the indicators. The indicator's smart card realizes the message is for it, and acts upon the message content – flash left indicator. When it comes to maintenance the central smart card can supply engineers with a detailed log of the car's performance. These techniques could be applied to any means of transport.

## Interactive entertainment

Home entertainment is now a multimedia experience, with sound and vision being extensively used. To control what the user wants to experience, a Vitesse smart card can be linked to music centres, televisions and videos. The card can control the correct acoustics for the room, the intensity of the picture being displayed, right down to dimming the lights in a room when a movie starts.

One step further is interactive entertainment, whereby the user can select films, television programmes or music from libraries held at the other end of the network. The smart card controls the entertainment to be downloaded, and in the future interaction can be incorporated. Imagine being able to decide what happens next in a film!

## Implementation of the Vitesse smart card design

The designs for Vitesse which have been laid out over the preceding sections have created a model for an operating system, and an outline of the typical hardware base which VitesseOS might run on. To complement the written aspect of this project, a software introduction to the design was created. A variety of possible solutions of how to bring the design to life are outlined below.

## Implementation of VitesseWare and VitesseOS in full

This approach would involve constructing hardware that modelled the simplicity of VitesseWare - a central processor, RAM, backing store and communications port. To enable the hardware to operate, VitesseOS would have to be implemented in part or full.

This choice is the preferred approach, enabling the design to be realized in full, and allowing for flaws and drawbacks in the design to be highlighted. Due to time constraints, implementing VitesseOS in full was impractical. Modern operating system design and construction is a time consuming occupation – further design would have to take place for the individual components of the system, and then coded. The hardware model would be expensive to implement, but could be facilitated by modelling VitesseOS on a 'normal' computer system, though no real prototype of a Vitesse smart card would be created.

## Part implementation of VitesseOS

An alternative leads to individual parts of the operating system being designed in detail and then coded into a working implementation. Typical components that could be modelled are the program manager, memory manager, database manager, and so on.

Modelling of components in this way leads to a detailed knowledge being obtained about particular parts of operating system design, which is not the objective of this project. Any implementation must maintain a flavour of the whole operating system, to allow any future user of the design to focus in on, and learn about, any aspect of the system. Also, coding of individual components does not enable the integration of the whole design to be tested, which at this stage of the design is important. Errors in overview designs which are not corrected can be costly to rectify later. Finally the components which can be coded easily and demonstrated independently are the least interesting. Much research has already been carried out into memory management techniques, security, and so on. The more interesting aspects of the design – client/server, object orientation, message routing, information interpretation, etc – require a more integrated system to be coded, which as already noted is outside the immediate limits of time available.

## Simulated modelling of smart card environment

The third implementation idea revolves around the notion of interacting objects. Everything in the smart card world, from the card itself to users, card readers, networks, information, etc, may be considered as an object. All these objects can interact, and a set of rules can be defined to determine what happens on interaction. Each rule can define an outcome if the interaction is legitimate, either displaying text or graphics to represent the result of the interaction or updating an internal simulated model of the smart card.

The internal model represents components such as the memory/programme manager, database, network, etc. At any time during the simulation the user can ask to examine any part of the internal model, to view the results of interactions.

## Visual design simulator

The final implementation technique proposed is a simulation of the design itself. By remaining at the abstract/overview level throughout the project, the visual design simulator can be used as a teaching aid to help readers understand the concepts put forward. The simulator uses multimedia techniques to put forward the proposed design.

The simulator provides a method for creating a representation of the model quickly, and allowing the design to be modified and extended easily by use of a control language. The language provides a simple set of commands for construction of visual objects. This approach allows for design prototyping, enabling new features to be freely added to enhance understanding.

A working prototype of the simulator was constructed, and aspects of the Vitesse design were modelled successfully. Usability problems with the simulator were fed back and resulted in a redesign of the simulator system (Mitchell, 1993, p. 57).

## Vitesse - implications and conclusions

Vitesse, the design for a new generation of smart card, has been researched and developed to the stage of producing a series of models representing overviews of both hardware and software. These models have been grouped together to form VitesseWare, the hardware base, and VitesseOS, the operating system. With the driving force of an object orientated operating system, implemented using a client/server architecture, dedicated to information processing, and running on top of scalable and extensible hardware, Vitesse smart cards are shown to be able to take advantage of the information revolution in the nineties and beyond.

Vitesse displays attributes of simplicity, power, flexibility and the ability to keep pace with technology, while fitting in with current organizational philosophy. The client/server architecture, with the smart card as the server communicating with the client over the network, imposed a constraint that restricted input and output from the smart card, dictating that interaction with the smart card could only occur via a network interface. With smart cards designed to be portable this constraint requires connection to a client computer at each time of use.

To make Vitesse truly portable and independent of networks as a communications medium, a future revised hardware architecture would include a portable visual interaction manager. The interaction manager is the software which controls communication with a Vitesse smart card, and is executed on client computers. The visual component would take the form of a small plug-in hardware option for the network port, providing a high definition output device, typically a screen or printer, complemented by an input device such as a lightpen, keypad, touchscreen or keyboard.

The PVIM could thus open up a new arena of applications, such as car navigation – different smart cards representing different cities, or an information retrieval system for police cars. The processing power of Vitesse with the PVIM for interaction would use the portable telephone network as a communications medium.

The decision to step backwards to third generation smart cards and develop attributes from existing technologies demonstrates that progress should be careful not to ignore what has thus far been so successful. The PVIM evolves the input and output concepts of third generation smart cards – liquid crystal displays and plastic keyboards – which are the attributes which have made the smart card so popular and a commercial success.

Thus while Vitesse cards are portable their use is not always convenient, access only being achievable via a network. However Vitesse smart cards have attributes lacking in the previous generations of cards, that is, their expandability and enhanceability and their ability to adapt to new technology, thus taking advantage of new application opportunities.

This research conducted into smart cards and technology trends has led to some interesting questions, and highlighted possible directions for smart cards in the future. To the question, 'Do we really need fourth generation smart cards like Vitesse?', the answer is both yes and no. Today's society has become absorbed in technology as a medium for achieving solutions to many of its problems. Too frequently companies look towards technology whereas organizations reevaluating their needs and restructuring should take the simple approach and aim to eliminate excess technology. Information within an organization has to be regulated, and efficient handling of information will lead to productive management information systems and effective decision support tools.

Organizations may wish to consider and adopt the straightforward client/server philosophy. They may thus achieve the position of being able to integrate multiple vendors in open system architectures, making their networks interoperable, seamless and transparent to the user. If companies are prepared to accept the challenges of client/server computing, then they can evolve their information systems into the world of smart cards, providing a dynamic environment which focuses on the end user, and provides the ability of information processing handling to expand with demand.

With information becoming so valuable when placed in the above context, the infojunk revolution is bound to appear as the influence of networks spreads. Today people are faced with unsolicited mail, junk mail. Tomorrow it will appear electronically – infojunk. This increases the importance of the objective for computers and networks to understand the content of the information they are processing, so that they can isolate, simplify and present useful information and reject irrelevant data before users' lives become too cluttered.

The existing web of computer, telephone, broadcast and other kinds of network do not constitute the kind of powerful infrastructure that the authors envisage. Today researchers and academics use megabit-per-second networks to communicate. Banks, factories, financial institutions and other businesses work with 50 000 to 100 000 bits per second networks – fast enough to provide real time stock quotations, for example. At the bottom end of the scale, networks exist that service news information, and mail service, operating between 1200 and 2400 bits per second (Burch and Grudnitski, 1989, p. 326).

Vitesse provides a solution to the infojunk revolution, a problem caused by technology in the late twentieth century. Man has been greedy, exploiting the communications media and overloading them with information. A means of control is now required, a tool to evaluate the value of information, acting as a filter and extracting only information that is of relevance to individuals. The information server present in every Vitesse smart card, if extended, provides a powerful facility for regulating information within a system.

Networks are becoming the predominant infrastructure within a country and represent the lifeline for Vitesse smart cards. Vitesse needs a medium to communicate and networks are proving to be the dominant highway. Alternative communications media such as newspapers and the postal service are currently being replaced by technological equivalents like electronic mail and the Reuters news agency. The power of Vitesse used through networks removes the need to go to the bank, the post office or the library and provides people with more free time, and the ability to avoid many of the mundane tasks in life.

As the influence of networks spreads, so does our dependency on the services provided by the network, and an increase in the information supplied. As information is a most valuable commodity, it places considerable power with the suppliers of the information: an ability to dictate the content, accuracy and price of information. As networks expand, information about an individual can be collated more easily, thus increasing the potential for misuse. Incorrect data becomes harder to correct, and leads to the 'Big Brother' syndrome – somebody is watching.

As smart cards may become so dependent on networks, and society itself more reliant on the electronic communication medium, a scenario exists where the infrastructure collapses as a result of complete hardware failure of the network. Organizations and individuals would become paralysed and unable to function.

Coincident with the study presented here, the signs are apparent that an increasingly emergent market is creating the conditions for manufacturers and developers to take advantage. At the end of 1988 the total number of smart cards produced was estimated to be just over 30 million, with the global prediction for 1995 being over 400 million.

Within the UK the Bank of Scotland is the first UK bank, apart from the original members of the development programme, National Westminster and Midland, to sign up for Mondex, the world's first 'cash on a card' system. Mondex is due to start a pilot scheme in Swindon in July and is a unique payment system based on the electronic storage of money using smart technology. A Mondex card can store money in the same way as a wallet or purse and can be used to pay for goods and services in the same way as cash. It can exploit electronic links including ATMs, electronic check-outs and special BT telephones. Money can be transferred to and from a bank account and, like cash, can also be used for person-to-person payments by transferring money from one card to another (The Scotsman 3.iv.95).

To capitalize on this favourable trend, the smart card industry should consider reducing its emphasis on the technology itself and devote more of its efforts to identifying and serving the needs of the market. To secure the future of smart cards in the business market place, there needs to be increased allocation of resources to software engineering in developing new applications. This is where business ideas will be converted into commercial success.

Technology presents a growing number of organizations with the complex task of determining whether new products, like smart cards, should be adopted as part of their future information technology strategy. Managers responsible for assessing and recommending new business solutions involving smart cards would expect to consider the following issues (Burch and Grudnitski, 1989, p. 64).

(1) Will new technology improve our competitive situation?

(2) Can additional revenue be created by providing new products and services?

(3) Can the technology be exploited to fend off existing or new competitors?

(4) Does it offer a long term competitive advantage as opposed to short term benefit?

(5) Does it enhance the fundamental way in which business is conducted?

The above five-point checklist needs to be refined to produce a more rigorous framework for analysis consisting of two sections – objectives and evaluation criteria. The objectives can be used as a basis for comparison, and though the comparison can be quantitative, it is more likely to subjective. Evaluation criteria allow for direct cost-effective comparison between solutions (see Table 7).

Costs naturally vary depending on volume, with small scale projects being viewed as expensive. This problem is being overcome. As the industry matures, more and more systems will be developed for specific applications. These so-called ‘turn key’ solutions where everything is supplied by the manufacturer, ready to go, will make the implementation of small projects a more viable business proposition.

Like other technological innovations, smart cards are part of a fast developing technology. Companies never know whether to hold off and wait for the technology to mature, or go with a relatively untested product to achieve maximum competitive advantage. These are the problems for the next generation of smart card to try and overcome, enabling businesses to forget about the problems of deciding on supplier, mixing and matching of technology, and supply of proven technology while providing a profitable and usable technology solution.

To have designed an innovative technology is an achievement in itself, but without success in the market place the smart card will die. Smart cards have to contend with three main parties: the supplier, the operator and the user. The largest unknown quantity when predicting the demand for smart cards is customer acceptance. Everything is dependent upon this unquantifiable but essential ingredient.

When analysing the user or consumer, there are a series of factors that should be considered - cost, value-added and perceived benefits. These are the issues that will determine the level of acceptance in the market place. It is important that the cost of a smart card reflects the benefits that the card will bring to the user. Costs can be absorbed by the card issuer, like credit cards, or can be recovered through subscription fees or payments for services which the smart card makes use of. If the user has to pay directly for the card, then value for money must be a key issue.

If the user has to pay directly for the card, then the expenditure on the card system has to be justified. Apart from giving value for money, the value added factors of a smart card must be heavily promoted. To market smart cards effectively, an approach exists that relies on a piece of marketing theory called the three Cs (Waterworth, 1987).

(1) Compactness: in power and performance the typical smart card can be compared to a personal computer, yet it is pocket sized and unobtrusive. The next generation of smart cards will maintain this philosophy.

(2) Conviviality: the user interaction with the smart card consists of programs which are highly informative and portray friendly prompts, to guide the non-technical card holder through every operation.

(3) Convenience: this is an attribute which is virtually unmatched by any other computer based technology. Designed to be carried at all times, it requires no external support, allowing use at home. Again, just as for compactness, fourth generation smart cards will utilize this aspect of convenience, but will extend the principle and create a new meaning for convenience.

Assistance must be given to lowering the barriers of acceptance. Due to the lack of comprehension and education, particularly amongst older generations, large segments of the population are ‘afraid’ of new technology. A socially desirable product is required. Another value added factor which must be included is security, which due to the nature of smart cards – storage of information and the ability to combine multiple applications onto one card – is an economic reality.

To give the smart card an edge in the market place, the services provided by smart cards would be positioned on their status appeal and their perceived benefits. In ranking plastic cards of all types, smart cards are acknowledged as offering particular appeal. Properly imaged, the status of the card holder can appear to be enhanced. This is achieved by appealing to that potent market force known as lifestyle. The market for smart cards is full of affluent niche markets, an aspect which the new smart cards will be able to exploit.

Reconsidering the design developed here, several avenues for future work exist. Firstly, to move the existing models forward specifications could be devised, the present models modified and designs iterated to a finer level of detail. It will only be at this stage, when models depict detailed information flow round the system, that it will be possible to determine more fully the success of a design if implemented.

Secondly, individual design elements that have been proposed could be taken and applied to the current generation of smart cards, thus avoiding the leap taken in this paper by considering a radical progression in technology. Instead smart cards could evolve more slowly, testing new ideas like client/server, ensuring that individual components work before committing to Vitesse.

Whilst implementation of the various models that have been discussed here is desirable, with modern operating systems taking many years of design and coding a full implementation is unlikely to prove viable unless a commercial product were being produced. Vitesse however can be replicated using existing client/server operating systems, such as Mach, Windows NT, and Unix (X windows). The kernels provided by these systems enable software to be produced representing the higher level services, such as the information server, interaction managers, security servers and database management system.

The client/server architecture enables expansion of the facilities provided by VitesseOS. Future design enhancements could include real time execution of applications. Links exist within the program execution manager to set priorities for real time execution of processes. To enable real time execution Vitesse must run predictably. Detailed specifications must be given of how long it takes to complete various tasks, such as interrupt latency, program scheduler overhead, calls to different operating system functions and execution times of instructions. These timings would enable the execution times of applications to be predictable and consistent, allowing Vitesse smart cards to be used in safety critical applications – for example different smart cards could be used in hospitals to monitor patients in intensive care, using expert system applications to assess the health of a patient, provide care and supply recommendations on possible treatments.

The interaction managers used by clients to communicate with Vitesse smart cards use their own set of protocols. The need to achieve a common set of global communication protocols to make true open systems a reality has been emphasized. A design revision could easily accommodate current standards, and by incorporating a protocol server, any changes in standards could easily be maintained by deleting the server from the system and installing a new protocol server.

Vitesse aims to achieve a system which focuses on the end user, providing a high level of user productivity when manipulating information, and supporting the ability to grow as needs grow. Further design is required to consolidate Vitesse – building upon the notions of distributed computing, and configuring the database management systems to follow in the same style. Vitesse ought to be developed so that it can more naturally interact with people and networks. Designers would seek to transform Vitesse into a tool as accommodating as a wristwatch, enabling the smart card of the nineties to fade into an inconspicuous feature of the environment.

Table 7 Framework for analysis of smart card solutions and alternatives

<table><tr><td>Solution objectives</td><td>Direct evaluation criteria</td></tr><tr><td>Increased productivity</td><td>System design/development</td></tr><tr><td>Stronger competitive positioning</td><td>Implementation/integration</td></tr><tr><td>Reduced system costs</td><td>Hardware/software</td></tr><tr><td>Higher security</td><td>Upgrade/replacement</td></tr><tr><td>New business opportunities</td><td>Network/communication</td></tr><tr><td>More effective management</td><td>Maintenance/support</td></tr><tr><td>Enhanced performance</td><td>Upgrade/replacement</td></tr><tr><td>Lower operating costs</td><td>Management/administration</td></tr><tr><td>Decentralization</td><td>Staff training/user education</td></tr><tr><td>Improved customer services</td><td>Licence/contractual</td></tr><tr><td>Stronger competitive positioning</td><td></td></tr></table>

## References

Bright, R. (1988) Smart Cards: Principles, Practices, Applications (Ellis-Horwood, UK).

Burch, J.G. and Grudnitski, G. (1989) Information Systems: Theory and Practice (J. Wylie).

Clapp, D. (1990) The NeXT Bible: Hardware and Software for the NeXT Computer (Prentice-Hall, Englewood Cliffs, NJ).

Clements, A. (1991) The Principles of Computer Hardware (Oxford University Press, UK).

Coffin, S. (1988) C: The Complete Reference (McGraw-Hill, New York).

Custer, H. (1994) Inside Windows NT (Microsoft Corporation, USA).

Date, C.J. (1990) Introduction to Database Systems (Addison-Wesley, UK).

Mitchell, H. (1993) Vitesse smart cards, BSc dissertation, Heriot-Watt University, Edinburgh, UK.

Sheldon, T. (1990) Novell Network 386 (A. Osborne Pubs, USA).

Tanenbaum, A.S. (1987) Operating Systems: Design and Implementation (Prentice-Hall, Englewood Cliffs, NJ).

## Biographical notes

After working as a systems analyst on the direct digital control of a chemical plant at Avonmouth, Robert Davis was appointed lecturer and subsequently senior lecturer in the Department of Computing and Electrical Engineering at Heriot-Watt University, Edinburgh. He holds a BSc degree in electrical engineering, specializing in instrumentation and control, and a PhD in computer control systems, both from the Queen's University Belfast. He has throughout his academic career developed an interest in the management and control of real-time information systems where the majority of his 50 publications are to be found. He has jointly held SERC grants for study into concurrency control of relational databases and into system architecture for logic databases.

Hamish Mitchell graduated with an honours BSc degree in computer science from Heriot-Watt University in 1993. He is currently working as a computer consultant with Intelligent Office Co. Ltd.

Address for correspondence: Robert Davis, Department of Computer Science, Heriot-Watt University, Edinburgh, UK.
