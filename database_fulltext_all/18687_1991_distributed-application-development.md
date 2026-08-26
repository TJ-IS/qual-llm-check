---
otero_id: 18687
otero_key: "P63E9VD7"
title: "Distributed application development"
authors: "Hemant K. Jain; Sandeep Purao"
year: "1991"
journal: "Information & Management"
doi: "10.1016/0378-7206(91)90017-v"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Research

# Distributed application development SDLC revisited

Hemant K. Jain and Sandeep Purao
School of Business Administration, University of Wisconsin-Milwaukee, Milwaukee, WI 53209, USA

Proliferation of microcomputers and the advances in data communication technology have accelerated the trend towards the development of distributed computer systems. The design and development of applications in this environment present various opportunities and challenges. This paper examines the important phases of System Development Life Cycle (SDLC) to identify the changes required for application development in a distributed environment. Additional steps required in obtaining user requirements have been identified. The commonly used tools in logical system design have been modified, and some available CASE products are examined to judge the ease of implementing these modifications. Finally, issues related to the physical design have been discussed.

Keywords: Distributed systems, Distributed applications, Application development, Developing logical models for distributed applications, CASE tools, System development life cycle

![](/api/attachments/P63E9VD7/fulltext/images/e57b0580ce25762f34fe7804ea477206a5b7da71477639031b7d9361541a1a93.jpg)

Hemant K. Jain is Research Professor of Management Information Systems in the School of Business Administration at the University of Wisconsin-Milwaukee. He also held faculty positions at Syracuse University and National Institute for Training in Industrial Engineering, Bombay. His research interests lie in the areas of Distributed System Design, Database Management, Decision Support Systems, Model Management and Expert Systems. He received his B.S. in

Mechanical Engineering from the University of Indore (India), a M.Tech. in Industrial Engineering from I.I.T. Kharagpur, and Ph.D. from Lehigh University. He is a member of ACM, IEEE Computer Society and TIMS.

## 1. Introduction

The principal motivation for distributing computer systems has come from the decline in the costs of computing and data communication. With costs of computing falling dramatically in the seventies, the validity of Grosch's Law [13] was questioned [9]. Also, rapid decline in communication costs offered incentives for distributing processing power and linking geographically dispersed processors.

A fundamental characteristic of distributed systems is that there are more than one processing units in the system and they are capable of communicating with one another. This offers an opportunity for implementing a single logical set of processing functions across a number of physical devices, such that each physical device performs the processing functions for which it is best suited. Thus, a distributed system has distributed processing functions, often accompanied by distributed databases, though this is not a requirement.

Lorin [18] defined the idea of ‘significant processing unit’ which consists of an independent processor capable of processing and storing data. We extend this notion into the concept of a ‘logical processing unit’, characterized by apparent control over a defined set of computing resources (programming capability, software, computational & storage capacities etc.). Drawing on this, we define the term Logical Site (LS) as a unit of the organization which has a distinct geographical location and is characterized by:

![](/api/attachments/P63E9VD7/fulltext/images/c8347de335e5c10ac703526e7520e0bbd27d291ec39972be4f5f96da577593a2.jpg)  
and accounting effectiveness through computers.

\- processing capability,

\- data storage,

\- software availability,

\- programming and analyst staff.

Thus, an LS might represent an organizational unit, such as a subdivision, branch office, regional office, or a subsidiary of the company having information processing capability. A distributed system then consists of a number of LSs. Here, it is assumed that one or more processors already exist at the LSs and they are connected through a data communication network.

In this context, a distributed application can be defined as an application in which the processing functions are partitioned and allocated over multiple LSs. Since geographical location is one of the dimensions in the definition of LS, it automatically becomes an essential component of a distributed application.

Patrick [21] classified applications into four categories based on their complexity:

\- Independent local processing - discrete applications that run locally.

\- Interrelated applications - interface with other applications that run locally.

\- Applications that run to completion locally and then pass information to other locations.

\- Applications that require coordinated processing at two or more locations.

The fourth category of applications are good candidates for development and implementation as distributed applications. It is assumed that the proposed application is new and has not been implemented previously.

The primary purpose here is to examine the process of developing distributed applications. The System Development Life Cycle (SDLC) for application development is examined to identify the changes required in its key phases. The additional tasks required in each phase are identified and the existing system design and development tools are modified to support these tasks.

## 2. System development life cycle

Although there is no standard description of SDLC, most authors describe it as an iterative process consisting of overlapping steps similar to any ‘construction’ project. A slightly different perspective of SDLC is provided by Powers, Adams, and Mills [22]. They perceive it as a combination and successive application of two strategies – Analysis and Synthesis – to problem solving. They collapse SDLC into five major phases with checkpoints after each phase:

\- Investigation.

\- Analysis and General Design.

\- Detailed Design and Implementation.

\- Installation.

\- Review.

Gane and Sarson [12] advocated Structured Systems Analysis and emphasized ‘Creation of a Functional Specification’ as the key phase in the process. Explosion of the functional specification helps in building and designing components of a logical model of the proposed application. Meilir [19] concentrated on ‘Development of Essential Structured Specification’. According to him, the final step of the analysis is the creation of a configuration for the essential model of the proposed application.

All these views appear to concentrate on one critical section of the SDLC process: where the ‘analysis’ and ‘synthesis’ takes place. The key phases in this have been outlined by Powers et al. [22] as:

\- Understand the current system.

Study and model it to derive its logical model.

\- Get user requirements/Identify changes in the current system.

Derive the set of logical requirements.

Document physical requirements.

\- Develop specifications of the new system.

Create its logical model.

Construct its physical model.

Since the primary assumption here is that the proposed application has not yet been implemented, the key phases may be rewritten as:

\- Study the current system and identify new user requirements.

\- Develop a logical model of the proposed application.

\- Develop its alternative physical models.

These are the phases which, in our opinion, will require significant modification in case of distributed application development.

## 3. Distributed application development

Based on management philosophy and information requirements, Kanter [15] identified the following patterns of decentralization of MIS functions (Table 1).

These patterns are used as the basis for identifying the following strategies for distributed application development.

a. Centralized development: Here, one of the LSs is responsible for development of the application. The requirements are collected from all users. The design and programming is done at the responsible LS. The application may, however, run at more than one logical site.

b. Shared development: Here, each LS participating in the application is responsible for the development of a part of the application. One may be designated as the coordinator of the development effort. However, some of the tasks (e.g., database design) may be performed at only one LS.

A variation of these strategies may also be used. Selection of an appropriate strategy may depend upon the type of application, organization of data processing and user departments, and other technical and political considerations. Detailed analysis of these is beyond the scope of this paper; however, some critical issues which need to be considered are:

– Each of the LSs affected by the application should participate in identifying the requirements, examining the feasibility of running the application in their hardware and software environment plus other required resources. This may be achieved by establishing a formal project group consisting of representatives from each LS or through informal communication.

Table 1

<table><tr><td rowspan="2">Patterns</td><td colspan="4">Functions</td></tr><tr><td>MIS Planning</td><td>DataBase Administn</td><td>Application Development</td><td>Opera-tions</td></tr><tr><td>Centralized</td><td>C</td><td>C</td><td>C</td><td>C</td></tr><tr><td>Hybrid</td><td>C/D</td><td>C/D</td><td>C</td><td>C</td></tr><tr><td>Decentralized</td><td>C/D</td><td>C/D</td><td>D</td><td>D</td></tr></table>

Key: C = Centralized, D = Decentralized.

\- Since the application will be running on multiple LSs, standardization will be essential to ensure compatibility. Specifically, data formats, data names, and user interfaces need to be standardized.

\- In the case of shared development, it will be necessary to examine the feasibility of decomposing tasks into cohesive units. The basis of assigning these units to different LSs also needs to be determined. Factors, such as competence of an LS for a certain type of task and location at which the task will be implemented, may be considered in determining this basis.

Having identified some of the critical issues in the development of distributed applications, we will examine the key phases of the SDLC.

## 3.1. Define user requirements

Obtaining, analyzing, and documenting user requirements in the distributed environment will be similar to Requirements definition in the centralized environment. However, the distributed environment will add a location dimension. The end-product of this phase will be a Statement of User Requirements which will represent the aggregation and integration of the requirements of all the LSs.

Figure 1 represents the typical steps in User Requirement Analysis in a centralized environment [2,17,22]. For development of a distributed application, these steps have been modified and some additional ones have been identified; Figure 2 describes them.

The scope of the system defines the boundary for gathering information about user requirements. This is gathered from each of the affected LSs. Techniques such as review of procedures, on-site observations, and interviews (used in a centralized environment) can be adopted for this purpose. Based on this information, user requirements for each LS are identified. The following strategies can be used for identifying user requirements.

At some LSs, a local version of the proposed application may have been implemented, thereby crystallizing their requirements. These may be used

![](/api/attachments/P63E9VD7/fulltext/images/b20822a3e494ab530182747787e8462a4fd3109ef8f43b56150dfa952c781140.jpg)  
Fig. 1. Steps in user requirements analysis (centralized application development).

as a reference to obtain the requirements from other LSs. If no local version of the proposed application exists at any LS, the requirements collected at an arbitrarily selected LS may be used as a starting point for identifying requirements at others. The priorities and the critical issues may differ from one to another. The analyst should be aware of this, and ensure that the priorities of one LS are not unnecessarily foisted on another.

![](/api/attachments/P63E9VD7/fulltext/images/85fa3a1ccdfb6b5c91ae262ba436cdb47f77bc71b4f831aa9fbcb01185c3b00c.jpg)  
Fig. 2. Steps in user requirements analysis (distributed application development).

Another approach for identifying the requirements may be to obtain them independently from each LS. This will eliminate the risk of imposing the priorities and requirements of one LS onto another.

After obtaining the requirements from each LS, they will be analyzed and classified as organizational, informational, and procedural $[17]$ . They should be documented using the standard format currently used by the organization. This will help identify the similarities and differences and will also identify requirements which are unique to particular LSs. In addition, this will bring out gaps and overlaps: requirements of certain LSs may reveal conflicts. These may be resolved based on ‘organizational’ and ‘political’ considerations. Aggregation of requirements involves summing the performance statistics of common requirements from each LS. This will result in a number of requirement sets. Integration of these will provide an overall perspective of system requirements. The end-product will potentially have many components/levels:

i. Requirements Common to all Logical Sites.

ii. Requirements Common to all but one Logical Sites.

iii. Site-specific requirements which are unique to a particular Logical Site.

## 3.2. Develop the logical model

The set of requirements can be used to develop the logical model of the proposed system. This emphasizes the system characteristics and relationships among components. It is an efficient way of focusing on functions rather than physical implementation alternatives.

In case of a distributed application development, the location information needs to be incorporated in the logical model. Existing structured system design tools need to be modified to include this.

One of the most commonly used tool in structured systems design is the Data Flow Diagram (DFD). It is a representation of data movement, processing functions, and data stores of the system. In a recent survey by Necco et al. [20], it was found that 80% of the responding corporations use

DFDs. However, to be useful in the development of logical model of distributed applications, they need to be modified to include the location dimension. The modified approach to drawing DFDs for a distributed application system is described here with the help of an example.

Consider a distributed system with four LSs: A, B, C, and D. Let us assume that the proposed application will affect the first three LSs, and also, that the common and site-specific requirements have been identified and documented. A logical model of the proposed system needs to be derived.

The development of the logical model for a centralized application begins with the Context Diagram. This is converted into a high level DFD to represent the major processes in the application. Each process is then partitioned into lower level component processes, yielding a set of DFDs representing the functional processes. The lower level DFDs are supplemented by the Data Dictionary, in which details of each process are maintained.

For a distributed application, development of the logical model will begin with the Context Diagram (Figure 3). This will be converted into a high level DFD using the common and site-specific components of the requirement set. The processes necessary to support each of these will be represented as a process in the high level DFD. The data stores required by one or more of these higher level processes will also be shown (Figure 4).

Each process in the high level DFD will be exploded into its component processes similar to the derivation of lower level DFDs in a centralized environment. The Data Stores required by a particular process will be represented in the explosion. Figures 5, 6, and 7 represent such explosions of the integrated processes 1, 2, and 4. Process 1 represents those required at all LSs (A, B, and C). Process 2 represents those required at LSs B and C. Process 4 represents those required only at LS B. The DFD can then be derived from the set of explosions. For example, the DFD for LS B can be derived from the DFDs representing the explosions of processes 1,2, and 4 (Figure 8).

![](/api/attachments/P63E9VD7/fulltext/images/6ca27b182bba2233e7c233f9a837908793e3c0343a2299370b97778bef65672b.jpg)  
Fig. 3. Context diagram.

![](/api/attachments/P63E9VD7/fulltext/images/26ce32d09212d47070d6c3beffc8e6d46b299e77f4d6a4f209a410eb42505ad8.jpg)  
Fig. 4. High level data flow diagram.

![](/api/attachments/P63E9VD7/fulltext/images/076c8c7cf6c27929117f33f56199779e17fdfba014b5e6922b3e6205c6b807e1.jpg)  
Fig. 5. Data flow diagram for process 1.

![](/api/attachments/P63E9VD7/fulltext/images/22ab06a3503a0bfdac2cefae8918581875c6406d71bb938b9bfaf7394d213ad3.jpg)  
Fig. 6. Data flow diagram for process 2.

The process description in the Data Dictionary can then be modified to include information about the LSs requiring the process, and the LSs at which the process will be performed. Figure 9 shows a modified process description entry in the

![](/api/attachments/P63E9VD7/fulltext/images/0ce733b4bfb55f0307cae643a2fa64e9abf324f279b3f36a2735646d9a51dec3.jpg)  
Fig. 7. Data flow diagram for process 4.

Data Dictionary. Existing CASE tools can easily implement these enhancements.

## 3.3. Develop alternate physical models

Development of alternative physical models of the proposed application involves design of data structures and/or database, design of programs implementing the processes, and communications between processes. In a distributed environment, data may be located at one LS or may be distributed over multiple LSs. Further, data distribution may or may not be redundant. A number of models are available for the allocation of data in a distributed system $[1,3,7,14]$ .

![](/api/attachments/P63E9VD7/fulltext/images/8dce103fee9f3af7eff2baf66f351470a5f3bea09d600a89eccb71f13b36d979.jpg)  
Fig. 8. Complete data flow diagram for logical site B.

![](/api/attachments/P63E9VD7/fulltext/images/989cac3adc3f05d9651c15d22084220e41581346b32b6cbb9cd21d400ec42717.jpg)  
Fig. 9. Extract from data dictionary.

In an integrated database environment the data distribution decision is based on the data semantics and types and frequencies of query and update transactions. A number of approaches for distributed database design have been proposed in the literature $[4,5,16]$ . In most cases data location decision is made separately, as common data are used by multiple applications. Thus, the existing location of data can be treated as an input to the physical design of the distributed application. If the application requires its own private data set, then the data location will be part of the physical design decision.

The second important physical design decision is the assignment of processes to LSs. Each of the processes shown in the DFD can be assigned to one or more LSs for processing. The assignment decision should be based on the following criteria:

## a. Type of processing required.

Some of the simple operations required by a process can be performed efficiently and economically on microcomputers or a minicomputer [9]. This is because of the simple instruction set of these machines and the smaller software path length, defined as the number of machine instructions required to process a transaction. Thus, such operations should be assigned to the LS having micro or mini computers.

b. Availability of required data and use of output. The data required for the process assigned to an LS should be available at the site. Also the LS at which the output of the processes will be used should be considered in the assignment of processes. If the required data is not available or the output is not used at the LS to which the process is assigned, then the cost and delay due to data communication needs to be considered.

## c. Inter-process communication.

The communication between processes is an important criterion which needs to be considered in making the process assignment decision.

## d. Processing capacity available.

The processing capacity available at the LS will determine the feasibility of the assignment decision.

Thus, the assignment of processes to LSs will involve trade-offs among the criteria. Even though no comprehensive model to support such decision making is available, a number of models have been developed to support one or more aspects of this process assignment problem $[14,8]$ . The selected physical design alternative may be implemented by using one or more techniques, such as parallel, cutoff, or gradual $[2]$ . In addition, it might be possible to do a pilot implementation at one LS.

## 4. Enhancements required in the existing case tools

Computer Aided Software Engineering (CASE) tools are playing an increasingly important role in application development, by automating some of the mundane tasks of the system design process. These include tasks such as creating pictorial representations, creating and maintaining data and project dictionaries, and ensuring consistency and completeness of design. Most commercial CASE products implement a structured analysis and design methodology [19]. They support the development of system specifications with the help of DFD's and associated Data Dictionaries. While the diagrams are the visual focus of these products, the repository containing the descriptions of data flow, data stores, and processes is the real heart of these programs. They provide the basis required for implementing the enhancements required by distributed application development.

The location information needs to be added to the DFD's and the Data Dictionary, which will allow manipulation of the DFD's on the basis of location. A module may be added to support the derivation of the DFD for any specific LS from the set of lower level DFDs. This can be accomplished by using the location information stored in the Data Dictionary. Almost all the products we reviewed support creation and maintenance of project and data dictionaries. They also allow access to these dictionaries via external modules. Thus, we feel that the addition of such a module can be easily accomplished. We, therefore, review some representative CASE products to demonstrate the ease with which the external module can be added or internal changes can be effected to implement our enhancements.

Teamwork from Cadre Technologies, Inc. has an editor for creating and editing structured data flow diagrams. Starting at the highest level, each process can be partitioned into its “child” processes. Each process is described by a simple textual description called process specification. The process specifications are stored in data dictionary. These specifications are attached to diagrams for retrieval and updating. They are also stored in a central project data base. The project data base can be easily augmented to store the location information. The Teamwork/ACCESS feature of the package opens the project data base to allow integration with other packages and tools. Access to the project data base is provided via a C programming language interface. This feature of Teamwork can be used to add the module for manipulating the location information. This will have the ability to extract the processes and data stores relevant for a specific LS, structure them, and present them in a pictorial format.

DesignAid/CASE 2000 is a set of integrated CASE tools from Nastec Corporation. It supports the traditional written specifications with the graphically based DFDs and mini-specifications generated using the Yourdon/DeMarco Structured Analysis methodology [10]. One of DesignAid's unique characteristics is its open architecture. Unlike other products, DesignAid is a file-based system with sophisticated hierarchical file management capabilities. It has powerful file-handling techniques which allow designers to embed file references within diagrams to read the file contents. For instance, each DFD is stored in its own file. Inside each DFD, there might be references to the underlying process specifications, each of them stored in its own file. Separating the design into a number of files makes it easy to rearrange individual design components. DesignAid also includes a project dictionary where information about a design is stored. Enhancements can be easily implemented using its file management capabilities and open architecture. The location information can be recorded in the project dictionary and the files containing the process specifications. The individual processes and data stores can be accessed from various files to produce a DFD similar to that shown in Figure 8.

Excelerator from Index Technology Corporation is one of the popular CASE products. Its data flow diagramming conventions closely follow the Yourdon conventions. Like other products, its XLDictionary facility lets the designer probe the project dictionary in a variety of different ways to examine data elements and graph objects. The project dictionary can be modified to store the location information pertaining to the data elements and processes. An external module that accesses the project dictionary through XLDictionary and creates the DFDs for a specific LS based on this location information can be added.

Teledyne Brown Corporation's TAGS is a specialized CASE product that supports the full implementation of their proprietary Input/Output Requirements Language (IORL). It is one of the few tools focusing exclusively on real-time system development. IORL is a graphics-based language that allows creation and manipulation of diagrams using its own conventions. IORL's Schematic Block Diagram is the highest level of data and process abstraction. Rectangles represent independently functioning processes – called components. Components can communicate over the connectors – called interfaces. This level can be compared to the High Level DFD we suggest in Figure 4. Each Component can further consist of one or more independent processes. An IORL Document consists of all the sections needed to elaborate a Component as though it were itself a system. Another symbol, a dotted connector – called an ‘external interfaces’ – is used to represent data flow at the higher level. An IORL Document may be compared to a site-specific DFD shown in figure 8. In order to develop the IORL Document for a specific LS it will be necessary to add the location information to the individual Functions and Components. This information can be stored in the data dictionary. An additional module in the Library Tools will be necessary to extract and regroup all the Components, Functions, and Data elements relevant to a specific LS. An external module to accomplish this may be added to TAGS.

## 5. Conclusion

The availability of inexpensive computing power and advances in data communication facilities has increased the tendency to distribute computing power. Development of applications in this environment presents many interesting problems that have not been addressed in the literature. This paper makes an initial attempt to identify some of the key issues in distributed application development and presents an approach based on the SDLC. Specifically, certain key phases of the System Development Life Cycle have been examined with a view to determining the modifications required for the development of distributed applications.

A location dimension has been added to the requirements analysis phase. The issues that either facilitate or hinder requirement analysis have been discussed. An additional step of aggregation and integration of requirements has been added. A modified approach to developing the logical model is suggested. This involves enhancing the structured system design tools, in particular the data flow diagram, by incorporating location information. A brief example to demonstrate the application of the enhanced data flow diagram is presented. A representative sample of CASE tools is reviewed to indicate the changes necessary to automate the enhancement. Finally, issues related to physical design have been discussed.

## References

[1] Apers, P.M.G., "Data Allocation in Distributed Database Systems", ACM Transactions on Database Systems, Vol. 13, September, 1988, pp. 263-304.

[2] Awad, Elias M., Systems Analysis and Design, Richard D. Irwin Inc., 1985.

[3] Casey, R.G., “Allocation of Copies of a File in an Information Network”, AFIPS Conference Proceedings, 1972, 41, pp. 617–625.

[4] Ceri, S., Navathe, S., and Wiederhold, G., “Distribution Design of Logical Database Schemas”, IEEE Transactions on Software Engineering, 1983, 9, 4 (July) pp. 487–504.

[5] Ceri, S. and Pelagatti, G., Distributed Databases: Principles and Systems, McGraw-Hill, 1984.

[6] Chakravarty, A.K. and Jain H.K., “Distributed Computer System Capacity Planning and Capacity Loading” Decision Sciences, Vol. 21, No. 1, Spring 1990.

[7] Chu, W.W., “Optimal File Allocation in Multiple Computer Systems”, IEEE Transactions on Computers, 1969, C-18, pp. 885–889.

[8] Dutta, A., Koehler, G. and Whinston, A., “On Optimal Allocation in a Distributed Processing Environment”, Management Science, Vol. 28, No. 8, August, 1982, pp. 839–853.

[9] Ein-Dor, Phillip, “Grosch’s Law Re-Revisited: CPU Power and the Cost of Computation”, Communications of the ACM, Vol. 18, No. 2, 1985.

[10] Fisher, Alan S., CASE: Using the Newest Tools in Software Development, John Wiley & Sons, Inc., 1988, pp. 141–194.

[11] Fresko-Weiss et al., “CASE Tools for Designing Your Applications”, PC Magazine, January 30, 1990.

[12] Gane, C. and Sarson, T., Structured Systems Analysis: Tools and Techniques, Prentice-Hall Inc., 1979.

[13] Grosch, H., “Grosch’s Law Revisited”, Computerworld, Vol. 8, No. 16, April 1975.

[14] Jain, H.K. and Dutta, A., “Distributed Computer System Design: A Multicriteria Decision-making Methodology”, Decision Sciences, Vol. 17, No. 4, Fall 1986, pp. 437–453.

[15] Kanter, J. Management Information Systems, Prentice-Hall Inc., 1984, pp. 154.

[16] Kulkarni, U.K. and Jain, H.K., “Fragmentation and Allocation of Data in Distributed Data Bases Using Semantic Knowledge”, Working Paper, School of Business Administration, University of Wisconsin-Milwaukee, 1989.

[17] Licker, P.S., Fundamentals of Systems Analysis with Application Design, Boyd & Fraser Publishing Company, 1987.

[18] Lorin, H., Aspects of Distributed Computer Systems, John Wiley & Sons, 1980.

[19] Meilir, Page-Jones, The Practical Guide to Structured System Design, Yourdon Press, 1988.

[20] Necco, C.R., Gordon, C.L. and Tsai, N.W., “Systems Analysis and Design: Current Practices”, MIS Quarterly, December, 1987, pp. 461–474.

[21] Patrick, R.L., Application Design Handbook for Distributed Systems, CBI Publishing Company, Inc., 1980.

[22] Powers, M.J., Adams, D.R. and Mills, H.D., Computer Information Systems Development: Analysis and Design, South-Western Publishing Company, 1984.
