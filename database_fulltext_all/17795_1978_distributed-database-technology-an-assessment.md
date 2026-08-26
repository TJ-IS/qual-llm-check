---
otero_id: 17795
otero_key: "P3S95C89"
title: "Distributed database technology: An assessment"
authors: "W.T. Hardgrave"
year: "1978"
journal: "Information & Management"
doi: "10.1016/0378-7206(78)90003-4"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Distributed Database Technology: An Assessment

W.T. Hardgrave

Department of Information Systems Management, University of Maryland, College Park, MD 20742, USA

This article reviews the current state of distributed database technology and discusses several major problem areas that are critical for its success in non-trivial applications. The paper also discusses several rules-of-thumb that a manager considering a distributed approach will want to consider. Several hardware configurations are enumerated and evaluated as part of a general framework that helps in understanding the evolutionary nature of distributed configurations.

In distributed systems, different users often want to maintain different views of the same data. This problem and possible solutions are discussed. The topic of languages for use with specialized data-base machines is a central issue, because the responsibilities of a data-base machine vis-a-vis the host-machine depend to a large extent on the choice of language (or protocol) that is used for communication between them.

Finally, some of the available literature is reviewed and discussed. Other important topics such as integrity, security and performance are not treated in depth.

Keywords: Data-base systems, distributed systems, backend. network, management of database systems

## 1. Introduction

Recently, much attention has been given to distributed databases and their associated problems (e.g. see [21,22]). However, there are few examples of practical distributed data-base systems in day-to-day operation. Managers in large-scale information processing organizations are likely to be confused by the claims and counter-claims in this rapidly-evolving area. The design of a distributed database environ-

![](/api/attachments/P3S95C89/fulltext/images/bcf1f27f0965d01eb517ac588ce04eb64f81944e57eb7265a22527f6d4f26bfa.jpg)

Dr. W. Terry Hardgrave is Assistant Professor of Information Systems Management, University of Maryland, College Park, and. Prior to joining the Maryland faculty in 1975, Dr. Hardgrave was a Research Associate at NASA/ICASE, and before that a Visiting Scientist at CERN, Geneva Switzerland. Dr. Hardgrave's educational background includes a Ph.D. in computer science (1972) from the University of Texas at Austin. Dr.

Hardgrave has participated in the development of several research prototype data-base management systems. While doing graduate work, Dr. Hardgrave worked on the RFMS project at the University of Texas. RFMS was a research prototype which led to the development of SYSTEM 2000 as a commercial database product. Dr. Hardgrave studied buffer management strategies, report generation techniques and query processing for tree-structures. His dissertation is a complete analysis of query processing on tree-structures using predicate-calculus-based languages. Since 1973, Dr. Hardgrave has been developing positional set theory, a mathematical approach to the study of data-structures, data models and data-base management. An experimental prototype positional-self-processor has been implemented over a five-year period. This system, written mostly in FORTRAN, runs on several different computers and represents a case-study in modular portable programming and research prototype development. In addition, Dr. Hardgrave has consulted for various private and government organizations in the areas of project managements distributed processing and database management. He is a member of ACM and the IEEE Computer Society and regularly serves as a referee for ACM Transactions on Database Systems (TODS), Information & Management, and numerous conferences on database technology.

ment becomes a particularly difficult task and the literature provides little help or insights.

Managers and information system designers are now seeking good rules-of-thumb for creating and operating a network of databases. This article proposes a few and discusses the philosophy that led to their development. The reader should be aware that the field is so new that even these guidelines are not well-tested and are far from established principles.

## 1.1. Terminology

In this paper, the phrase, distributed data-base technology, is meant to include all computer-systems that contain a separate computer that is responsible for the management of the data-base resources. By now, database technology has been extensively discussed in the literature (e.g. see [23]). One important aspect of this technology is the notion of a stored data-base-definition. That is, this stored definition, sometimes called a schema, is a (usually) small amount of stored data that describes the contents of the larger populated data-base. Before data-base technology appeared, this descriptive data was usually held as part of the program as written in some programming language (e.g. the DATA DIVISION IN COBOL). Members in the populated data-base that correspond to particular elements in the schema are called instances of those schema elements. There are several different approaches to schema definition and naturally the instances must conform to the particular schema definition approach.

A special computer that manages data-base resources may be called a data-base-computer, a database-node, or a data-base-machine. In addition, some authors use the term, back-end-computer, because of the analogy with the front-end-computer which is used in many systems to manage the communications system including on-line terminals and remote-job-entry stations. The data-base resources would normally include hardware (e.g. disks, drums, tapes, and mass-storage-systems such as the IBM 3850 or the Ampex Terabit Memory), software, and some important data such as stored-data-definitions as well as the populated data-bases themselves.

The term, data-consumer, is defined to be any user of permanently stored or derivable data on the database resources. The data-consumer may be a human-user or a process (i.e., a program) executing on some other computer (ternied the host), data-base, or other special purpose computer.

Here, we shall discuss three aspects of distributed data-base technology that are critical to its success in non-trivial applications; they are:

\- Hardware Configuration(s)

• Multiple Schema Views of a Data-base

\- Interface Languages for Data-Consumer/Data-Base Machine Communication

These three topics are further defined and summarized below and discussed in detail throughout the article.

## 1.2. Hardware configuration

In section 2, we enumerate and briefly discuss several possible hardware configurations that might be used to implement a distributed system; in particular, we suggest an evolutionary approach that begins with a standard back-end configuration and results in a general network environment. The final configuration includes several special data-base-nodes that handle the data-management functions. This evolutionary process, though it might be painful for some organizations, can be partially circumvented if a communications network is planned prior to the introduction of distributed data-base technology.

## 1.3. Multiple-schema-views

As noted earlier, the stored data definition is sometimes called a schema. However, the term schema is used in two different, but closely related contexts. One interpretation of schema is the stored-data-definition. The other interpretation is an attempt to capture the human-user's perception of the meaning of the data in the data-base. The latter interpretation is also called a logical view of the data-base. Most authors have recognized that an important aspect of data-base technology is the sharing of data among users and further, different users may hold somewhat different views of the same data.

Two classes of distributed data-base systems are germane to this discussion:

\- Central Schema and Distributed Instances - Distributed Schema and Distributed Instances
If schemas are to be distributed, a framework (e.g. ANSI/SPARC [16]) must be available that provides support for multiple-logical-views from distributed nodes by a consistent central view that is the synthesis of all of the distributed views. Naturally, some mechanism for mapping from one view to another is essential. The discussion in Section 3 focuses on the issue.

## 1.4. Interface languages

The next topic, interface languages for communication between the data-consumers and the data-base-machines, reviews the debate between the navigational-language approach to data-base management and the query-language approach using predicate-calculus-based languages. This discussion is central because the duties of the data-base-machine vis-a-vis the host machine depend to a large extent on the choice of language interface. The typical front-end communications system has a very simple host interface language when compared to the wide spectrum of possible languages and data-modelling approaches that might be chosen for a data-base machine. The simple front-end/back-end analogy breaks down when the complexity of interface languages is considered.

## 1.5. Rules-of-thumb for distributed databases

The reader may consider the following as merely a distillation of good practice sweetened with homilies – however, too many of the pioneers in distributed systems have ignored them at their peril. The technical terms used in this summary are already defined and will be further explained in later parts of this article.

1. Be sure that an adequate and reliable communications-network has been implemented before embarking on a distributed data-base venture.

2. Estimate the load on the communications network. This usually begins in "transactions-per-day" and is eventually translated to "bits-per-second". Review item 1 above for adequacy. N.B. The quickest way to establish a communicative network is to purchase service from one of the networking or teleprocessing service bureaus. For example, one U.S. Federal agency is implementing a personnel information system (for 300,000 employees spread across the USA) using the communications and data-base resources of a national teleprocessing network. This system is currently 20% operational and has evolved from other prototypes over several years.

3. Decide whether a central schema and distributed instance type of system will meet the requirements. Systems needing distributed schemas as well as distributed instances are clearly avanteguard and must be assigned a higher risk of failure. Davenport [25] advises against them altogether.

4. Next decide whether multiple-logical-views are necessary and whether they can be (trivially) translated to the central schema. Decide how data items will be mapped from one schema to another.

5. Last but not least, define precisely the interface language between the data-base-machines and the data-consumers. This might be a collection of FORTRAN or COBOL callable procedures or it might resemble a higher level programming or query language. In any case, the semantics (and probably the syntax) of the language must be defined at the outset. When these questions are satisfactorily resolved, the manager may allow the staff to proceed in the design of a distributed data-base configuration with a higher level of confidence. Ironically, the pursuit of these answers often uncovers other aspects that help in understanding the overall problem and consequently provide for a better analysis.

## 2. Back-end concept versus data-base-node concept

A back-end computer is, in general terms, a specialized database management machine that provides database services to another computer called a host-computer. Fig. 1 depicts a simple back-end configuration. The back-end is obviously analogous to the front-end machine that manages the (terminal) communications for the host. The back-end manages the data base resources such as disks, drums, mass-storage-systems, etc. In our diagrams, we will show the data-base storage as disks; but this simplification is easily relaxed in most cases. In fig. 1, the host-computer is the center of attention. The front-end and the back-end both exist to off-load the host computer thus saving expensive CPU cycles.

Fig. 2 shows a multiple back-end configuration.

![](/api/attachments/P3S95C89/fulltext/images/c5456bf21a8b0db4e2399e84f569f3e23c8b8a3115c8d2719256b8e250c03214.jpg)  
Fig. 1. Simple back-end configuration.

This situation might arise when:

\- The first back-end becomes overloaded and more processing power (or more storage) is needed;

\- Data-bases need to be separated (or processed in parallel) for security, integrity, or performance reasons;

\- Geographic considerations dictated that multiple back-end machines are needed.

In such a configuration, it is likely that, as the system evolves, the back-end machines would need to communicate with one another as well as the host. This may be accomplished by:

\- Making the host serve as a message-switching communication system;

\- Selecting one of the back-ends to take the additional load of message-handling;

![](/api/attachments/P3S95C89/fulltext/images/738ed702ca59c6bc0802e66467249303d2595d3981b69f76ddd336b4c36863af.jpg)  
Fig. 2. Multiple back-end configuration.

\- Installing a communications system between the host and the back-end machines.

The first alternative is counterproductive, it loads the host with a task for which it is not designed. Typical host machines (e.g., IBM 360's/370's, CDC 6000's/7000's) are not cost-effective communications processors.

The second alternative destroys the homogeneity and the modular design of the back-end concept. Further, it would take a careful design to ensure integrity in such a system. While this alternative may be useful as a stop-gap measure, the long-run assessment is that this alternative is inherently inflexible and would undoubtedly lead to later problems.

Because we have eliminated the others, the third alternative is a clear favorite. While its initial cost is somewhat higher, this approach separates applications, communications, and data-management into three controllable spheres of influence. Modules can be added, deleted or replaced in any one of the spheres without affecting the others.

Figure 3 shows a reverse situation; a single back-end computer and multiple hosts. This situation is likely to arise when:

\- The host is overloaded and a new host is added; or

\- Because of user requirements, hosts from different vendors are desired to meet different needs.

One stated advantage of the back-end or data-base machine approach is that multiple hosts can access data bases. An evolution to such a configuration is very likely over a five-year period within an organization.

Figure 4 shows the eventual evolution of the back-end approach; multiple hosts and multiple back-end machines. The only way to insure adequate communication is to install a sophisticated communications system (message-switching and possibly also circuit-switching system). To avoid this by running cables from the various hosts to the various back-ends results in a spaghetti-like configuration. This spaghetti-like configuration can easily evolve if an initially single-host/single back-end system is augmented by adding new hosts and new back-ends one at a time.

One way of avoiding this evolutionary problem is shown in figure 5. The steps in building this configuration (after a thorough systems analysis) are:

\- Procure a sophisticated communications system (involving, at least, message-switching). Data-rates should be determined during the systems analysis phase. Gateways to other networks may also be desirable.

![](/api/attachments/P3S95C89/fulltext/images/3fbd773df22b9d7d8d1c681597bf710ff3c9dda95942dd4170e7a9f73d98bcd8.jpg)  
Fig. 3. Multiple host configuration.

![](/api/attachments/P3S95C89/fulltext/images/f7decac1354ae73448479b6da667d53d26bd5a014a3343729b19880b060ab063.jpg)  
Fig. 4. Multiple-host-multiple-back-end.

![](/api/attachments/P3S95C89/fulltext/images/a5ef79e8edcf41ff8f77505b52e49b56f6961590ae884e1ca9483f394ebc1e7a.jpg)  
Fig. 5. Data-base node(s) concept.

\- Interface the current host(s) to the communications system. Terminals should be connected directly to communications network rather than to a particular host.

\- Interface the (first) data-base-machine to the communications system.

\- Add new hosts and/or data-base-nodes as necessary.

To summarize, the distributed approach to data management requires a communications system. The simple back-end configuration is a stop-gap measure at best; it cannot endure through time. Therefore, the management of the organization should require that the digital communications system is in place before embarking on a significant distributed database effort. There are several other problems which may occur; for example, it is not easy to estimate required data-rates on the communications network for needs that are several years in the future.

## 3. Logical data-base design

Sibley [12] discusses sixteen possibilities for centralized/decentralized (1) data, (2) dictionary, (3) directory and (4) administration. Further he reviews two concept of Booth [1] for designing distributed data-base systems: replication and partition.

Replication implies that a unit of the data-base (e.g., the data, the dictionary, or the schema) is held at a central control point but that copies of (part of) the unit are distributed at various nodes. The problems associated with replication are largely update problems. That is, how can all copies of the same stored information be kept up-to-date and consistent, and how can contamination be detected early and kept from spreading?

![](/api/attachments/P3S95C89/fulltext/images/29ec2308d3a67a80e4dca5b21ff5bbf8ef4b07db4cb56b31303ab6283e0d4806.jpg)  
Fig. 6. Logical views.

The concept of partition is different; the goal is non-redundancy rather than redundancy. A unit (e.g., the schema) of the data base may be partitioned. Each partition may be stored, maintained and controlled at a different node in the system. In this section we discuss the need for a framework to support the partitioning of the schema as well as the data.

Figure 6 shows the overall organizational view of information and the view at each of the nodes. A framework is needed to support this kind of architecture. The framework must provide:

\- A rigorous definition of a view (or a schema)

\- A mechanism for mapping data elements and their groupings from one view to another.

In a partitioned environment, the organizational view (or conceptual schema) would probably exist; but there would be (little or) no data that conformed directly to that view. Organizational data-consumers would request data items from the manager (i.e., a program) of this organizational view. However, then the request (normally) would be mapped to the appropriate node for retrieval or processing. A nodal data-consumer may also request items that are not available at the issuing node. The request for items would be mapped through the organizational view to the appropriate node.

Recent ANSI/SPARC [16] work attacks a similar problem by proposing a conceptual schema for the organization. This notion can be useful if the concept of a schema (or view) is precisely defined and the relationships among schemas (internal, external and conceptual schemas) and instances are precisely defined. Finally, the mechanisms for mapping from one schema to another must be precise.

Consider the question of location of the dictionary. A centralized dictionary in a distributed environment may be unwieldy and cause undue hardships on remote personnel whose data items (for the most part) are local and unused by other nodes in the network. A decentralized data dictionary is only possible if precise mappings are maintained for translation of common items among the dictionaries.

The research approach (see [17-20]) in the Department of Information Systems Management at the University of Maryland involves an increasing reliance on mathematics, particularly set theory, to make these notions precise. Without such a precise approach, it is difficult to imagine that complex data relationships can be maintained as data is transferred to and from the various nodes in the network.

## 4. Data-base-machine interface language

One question that has not been resolved is the interface language between the data-consumers and the data-base machines. There are two different major approaches to generalized database management interface languages that must be considered:

\- Navigational-language systems;

\- Content-based query-language systems.

The Navigational approach emphasizes:

\- Record-by-record access;

\- Stating an algorithm (how) rather than a request (what) to define the query.

The content-based language approach emphasized:

\- Group manipulation and access;

\- Stating the request in a very high level language—generally specifying the criteria for retrieval rather than the procedure for retrieving the information.

Thus a query in a Navigational language often has the following structure:

1. Get next record where condition $C_{1}$

2. Get next record where condition $C_{2}$

3. Get next record where condition $C_{3}$

$$
\begin{array}{c} \vdots \\ n. \text {   Loop   back   to   1   until   condition   } C _ {4} \\ \vdots \end{array}
$$

The content-based language tends to look like:

GET ALL RECORDS WHERE CONDITION $K_{1}$

The major difference between these approaches is in the power of the conditions that may be given. Content-based language systems are often based on predicate-calculus and mathematical logic; the conditions may be more complex than those given in navigational language systems.

The ramifications associated with the choice of data-base machine interface language are substantial. The method affects the division of labor; the navigational approach requires that the data-consumer provide more processing logic, which means that more programming time is invested by the human data-consumers. If the programmer is careful, this may lead to less processing time, though the host machine may take more load than the back-end. Navigational languages are usually easy for experienced computer programmers to learn; they mimic programming languages.

The content-based approach requires that the database machine take a larger portion of the work-load. The data-consumer may formulate the request in high-level but precise terms; little if any programming is required in the host. However, sophisticated query languages are not easily mastered by those not familiar with mathematical logic.

Some query systems provide another access level: parametric access. With this, trained personnel can develop parameterized “canned” queries that may be executed by less sophisticated users (e.g., clerks and other non-professional staff).

One can expect more traffic on the communications network using the navigational approach. Data which is not required in the final output must be transferred to the data consumer in the host only to be rejected by a later condition. Less data traffic is normally expected using the content-based languages because more restriction is possible in the query language. However, a careless user can inadvertently transfer more data than anticipated, and the effect of distribution may obviate this advantage.

The trade-offs between network traffic and processor power within the data-base machine are complex issues. Substantial research is necessary before a general methodology is available to help with these decisions.

## 5. Summary and conclusions

In summary, there are several statements which echo our rules of thumb:

Distributed database implementation should not be undertaken before a long-term communications policy is developed. The first step is to (design and) install a digital data network capable of handling the data load expected. To some extent the communications philosophy must be designed in parallel with the data-base philosophy in order to determine key parameters (e.g., data rates). This decision may be impacted by the outcome of the interface-language decisions.

\- Distributed schemas cannot be maintained without a formal framework (e.g., mathematics) for mapping data elements between (among) schemas. A central schema system with distributed instances is not as vulnerable to this problem as distributed schemas.

\- The interface language between data-consumer and data-machine is a critical decision. Navigational systems will be easier to implement, but they increase the burden on the data-consumer and the host-machine. Content-based query language systems will increase the burden on the data-base-machine. Proposed applications are the main criteria for making the host/query decision; but the decision has other ramifications in the distributed environment. As noted above, the data rate on the communications system is affected.

## 6. Related work

A substantial amount of the space [2,5,6,8,26] devoted to distributed and back-end database systems is devoted to a discussion of their advantages and disadvantages. Furthermore, these are usually potential advantages and disadvantages since most of the conjectures are yet to be verified by experience in use. The tradeoffs are certainly not obvious. These advantages and disadvantages are listed in table 1. The reader is referred to the references for further discussion.

The first back-end computer to be described in the open literature was at Bell Labs [2]. However, this was an experimental prototype and the system is no longer operating.

The first data-base-machine connected to a national computer network was described by Marill and Stern [9]. This Datacomputer uses a data language designed for communication between machines; not people. However, the data language allows content-based requests and acts more like a query language than a navigational language. As the number of applications using this facility increases, the experience gained here will become very valuable. However, to date, the Datacomputer has only been used for a few (although some quite large) applications, though it is now a node on the ARPA network.

In addition to the Datacomputer project, CCA is pursuing the design of a System for Distributed Databases [11]; This work is very recent and the ultimate contribution is not yet clear.

## Table 1

## ADVANTAGES

## Cost-Related

1. Cost-benefits from machine designed especially for data management may exist.

2. Better utilization of host memory and central processing power will probably occur.

3. Performance of a data-base-machine may be monitored (and tuned) separately from that of the host.

## Integrity-Related

1. Data protection is improved by isolation of data from the host machine;

2. Data-Base-Machines (which are usually assumed to be specialized mini-computers) usually have longer mean-time-between-failure than their large scale computer hosts;

3. Voting systems may be used in the implementation of the multiple back-ends.

## Security-Related

1. Data protection is improved by the added isolation and controlled access.

2. Natural audit points occur at the communication points.

Access-Related

1. Data may be shared among data-consumers executing on different hosts.

## DISADVANTAGES

## Cost-Related

1. Additional expense in the additional hardware of the database-machines and communications equipment may exist.

2. The back-end machine may become obsolete, either in its hardware or software. This may cause added problems in conversion.

3. Unbalanced resources are possible, giving loss of flexibility for load-leveling.

4. Performance is still an unknown factor, and may not be as good as expected.

## Management-Related

1. Multiple-vendor problems in maintenance of equipment often occur; this can result in circular finger-pointing, with no one willing to accept responsibility for an error.

2. Unforeseeable technical and management problems associated with a major change in the data-processing configuration may occur.

The RAP project [14] at University of Toronto is developing a specialized data-base machine for use with relational data bases. The database operations are built into the controllers for the rotating devices. This could lead to a substantial improvement in the performance of database machines, if successful.

Lowenthal [7,8] discusses the back-end computer concept including several possible configurations. None use a general communications system; but instead an assortment of "multiplexers", "programmable switches", "inter-processor links" and "back-end adapters". Lowenthal does call for a high-level data-consumer/data-base-machine interface language (similar to that found in SYSTEM 2000).

Several commercial data-base companies are working on mini-computer versions of their respective products. With some care these can be used as back-ends and data-base machines; for example, Cullinane has announced a mini-computer version of IDMS. CINCOM is developing a version of TOTAL. Communications costs will be high for these host-language systems because of the large number of records that (usually) must be transferred to the host. It might be wiser to execute some application programs on the back-end (or data-base machine).

Sibley [12] gives a good overview of the technical and managerial problems that accompany distributed database technology. He asks some questions that too often are ignored until too late. Particularly, he notes that only a few technical problems remain to be solved in order to make distributed data base systems a reality. However, the hard problems, managerial, human, and legal have hardly been considered.

## References

[1] G.M. Booth, Distributed Information Systems AFIPS Conference Proceedings - 1976 (AFIPS, 210 Summit Ave., Montvale, NJ 07645), pp. 789-94.

[2] R.H. Canaday, R.D. Harrison, E.L. Ivie, J.L. Ryder and L.A. Wher, A Back-end Computer For Database Management, Communication of the ACM, Vol. 17, No. 10 (October 1974), pp. 575–582.

[3] R.G. Canning, Distributed Data Systems, EDP Analyzer, Vol. 14, No. 6 (June 1976).

[4] R.G. Canning, Network structures for Distributed Systems, EDP Analyzer, Vol. 14, No. 7 (July 1976).

[5] J. Cullinane, R. Goldman, T. Meurer, and R. Nawara, Commercial Data Management Processor Study, Technical Report, Cullinane Corporation, Wellesley Office Park. 20 William Street, Wellesley, MA 02121.

[6] R.F. Dyke, Advantages of a Back-end Data Base Management System to the Civil Service Commission, Proceedings of Fifth Annual Texas Conference on Computing Systems (October 1976).

[7] E.I. Lowenthal, Back-end Machines for Data Case Management: A Tutorial, Proceedings of Fifth Annual Texas Conference on Computing Systems (October 1976).

[8] E.I. Lowenthal, The Back-end Computer, Parts I and II, Auerbach Data Base Management Series (Auerbach Publishers, NJ, 1976).

[9] T. Marill and D. Stern, The Datacomputer - A Network Data Utility, AFIPS Conference Proceedings - 1975 (AFIPS, Montvale, NJ), pp. 389-395.

[10] J.B. Rothnie, and N. Goodman, An Approach to Updating in a Redundant Distributed Data Base Environment, Technical Report CCA-77-01, Computer Corporation of America, 575 Technology Square, Cambridge, MA. 02139 (1977).

[11] J.B. Rothnie, and N. Goodman, An Overview of the Preliminary Design of SDD-1: A System for Distributed Databases, Technical Report CCA-77-04, Computer Corporation of America, Cambridge, MA (1977).

[12] E.H. Sibley, The Distributed Information System: Its Architecture and Management, Technical Report No. 11, Department of Information Systems Management, University of Maryland, College Park, MD 20742 (Nov. 1976).

[13] W.E. Simonson and W.T. Alsbrooks, A DBMS for the U.S. Census Bureau, Proceedings of the First International Conference on Very Large Data Bases (ACM, New York, 1975).

[14] E.A. Ozkarahan, S.A. Schuster and K.C. Smith, RAP - An associative Processor for Data Base Mangement, AFIPS Conference Proceedings - 1975 (AFIPS, Montvale, NJ), pp. 379-387.

[15] S.Y.W. Su, and G.J. Liovski, CASSM: A Cellular System for Very Large Data Bases, Proceedings of the Conference on Very Large Data Bases (ACM, New York, 1975), pp. 456–472.

[16] ANSI/X3/SPARC Study Group on Data Base Management Systems: Interim Report, ACM SIGMOD FDT, Vol. 7, No. 2 (1975).

[17] W.T. Hardgrave, A Technique for Implementing a Set Processor, Proceedings of ACM SIGPLAN-SIGMOD Conference on Data Abstraction (March 1976).

[18] W.T. Hardgrave, Set Processing: A Tool for Data Management, Proceedings of ACM/NBS Fifteenth Annual Technical Symposium (June 1976).

[19] J.B. Rothnie, and W.T. Hardgrave, Data Model Theory: A beginning, Proceedings of the Fifth Annual Texas Conference on Computing Systems (October 1976).

[20] E.H. Sibley, and L. Kerschberg, Data Architecture and Data Model Considerations, AFIPS Conference Proceedings - 1977, (AFIPS, Montvale, NJ).

[21] C. Houen, An Inter-Related Processing Network Architecture, Information & Management, Vol. 1, No. 1 (Nov. 1977), pp. 27–37.

[22] C. Houen, An Inter-Related Processing Network Architecture: The Functional Architecture, Information & Management, Vol. 1, No. 2 (Feb. 1978), pp. 75–84.

[23] E.H. Sibley, Guest-Editor, Special Issue: Data-base Management Systems, ACM, Computer Surveys, Vol. 8, No. 1 (March 1976).

[24] J. Martin, Principles of Data-base Management, (Prentice-Hall, Englewood Cliffs, N.J., 1976).

[25] R.A. Davenport, Distributed or Centralized Data Base, The Computer Journal, Vol. 21, No. 1 (Feb. 1978), pp. 7–14.

[26] F.J. Maryanski, A Survey of Developments in Distributed Data Base Management Systems, Computer, Vol. 11, No. 2 (Feb. 1978), pp. 28–38.
