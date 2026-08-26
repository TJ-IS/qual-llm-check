---
otero_id: 17206
otero_key: "TJEVH8AC"
title: "Communication requirements and network evaluation within electronic meeting system environments"
authors: "Alan R. Dennis; Tom Abens; Sudha Ram; J.F. Nunamaker"
year: "1991"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(91)90074-l"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Communication requirements and network evaluation within electronic meeting system environments

Alan R. Dennis, Tom Abens, Sudha Ram and J.F. Nunamaker Jr.

Department of Management Information Systems, College of Business and Public Administration, University of Arizona, Tucson, AZ 85721, USA

One of the key issues in the design and implementation of Electronic Meeting Systems (EMS) is the identification of appropriate support for computer communications. Lack of adequate communication support can create a bottleneck in the use of EMS. Our objective is to identify the communication needs of several different EMS environments and to discuss an approach that can be used to evaluate the required communication support. We then use this approach to benchmark the performance of two Local Area Network (LAN) operating systems (IBM LAN program and Novell Netware) and three network servers (IBM PS/2 models 50, 60 and 80) in one EMS environment. While network operating systems have received comparatively less attention in LAN evaluation and design, fully 75% of the response time in some configurations was due solely to the network operating system. The Novell Netware software running on the IBM PS/2 model 50 server provided at least as great speed at lower cost than any other configuration tested. For the small files common to one style of EMS environment (i.e. under 2.5K), response time was not affected by the size of the file but rather was determined by the fixed overhead imposed by the network operating system.

Keywords: Electronic meeting systems, Group support systems, Local area networks, Performance evaluation

![](/api/attachments/TJEVH8AC/fulltext/images/a97f3bdca588a3fa667d0767b7b0f256ede6ee9484b0b924da56f2af528f43b0.jpg)

Alan Dennis is a doctoral candidate in Management Information Systems at the University of Arizona. He received a Bachelor of Computer Science from Acadia University and an MBA from Queens University in Kingston, Ontario, and was a 1987 winner of the AACSB National Doctoral Fellowship. Mr. Dennis has published articles in MIS Quarterly, Information and Management, Computers & Graphics, and DataBase. His current research interests include electronic meeting systems and management graphics.

\* We would like to acknowledge the research assistance provided by Frank DiMaggio, Shiow-Jiuan Huang, Sandhya Sathe, and Jane Stodola, and the helpful comments of Joey George and Mark Pendergast on an earlier draft of this paper.

![](/api/attachments/TJEVH8AC/fulltext/images/4cfd70bd594f62a50ef5d8c4b6d16c7772166b02f411480eea55c3ac0b4bba49.jpg)  
budgeting process.

Tom Abens is a Computer Applications Specialist for the University of Arizona. He holds a Bachelor of Science in Finance and Economics (Magna Cum Laude) from Northern Illinois University, and is enrolled part time in the Master of Science in Management Information Systems program. Mr. Abens has held various positions in the financial and aerospace industries, and is currently developing database systems to more efficiently manage the University's

![](/api/attachments/TJEVH8AC/fulltext/images/fbf05086be734632510e05c92db1e9db5a8cff50d79bfa60e9aeb1c603f2f18e.jpg)

Jay F. Nunamaker, Jr. is Head of the Department of Management of Management Information Systems and is a Professor of MIS and Computer Science at the University of Arizona. He received a PhD from Case Institute of Technology in systems engineering and operations research. He was an Associate Professor of Computer Science and Industrial Administration at Purdue University. Dr. Nunamaker joined the faculty at the University of Arizona in 1974 to develop the MIS program. He has authored numerous papers on electronic meeting systems, the automation of software construction, performance evaluation of computer systems, decision support systems for systems analysis and design, and has lectured throughout Europe, Russia, Asia, and South America. Dr. Nunamaker is Chairman of the ACM Curriculum Committee on Information Systems.

![](/api/attachments/TJEVH8AC/fulltext/images/7fb9670cbd57cd6785d092d93e80dd59dd11d3c916703562b764be638f40a556.jpg)

Sudha Ram is currently an Assistant Professor of Management Information Systems at the University of Arizona. She received her Ph.D. in Management Information Systems from the University of Illinois at Urbana-Champaign, in 1985. Dr. Ram has published in journals such as Communications of the ACM, Information Systems, Information Science, and Journal of Systems and Software. Her research interests are in the areas of distributed database and knowledge based systems, semantic modeling, automated tools for database design, and application of knowledge based systems in business. Her research in these areas has been funded by IBM, US Army, The National Institute of Standards and Technology and The Marketing Science Institute. In configuring the networks, the default parameters were used for Novell Netware. For IBM PC LAN, parameters were set to use 10K network buffers at both the server and user workstations, with four buffers on the server. Time slicing on the server was set as recommended for a dedicated server [14, p. 12–17]. One mega-byte was used for caching.

## 1. Introduction

In recent years, there has been rapidly growing interest among both researchers and practitioners in the use of information technology to support group work [e.g. 10, 26]. Many different terms have been used to describe this use of information technology, including Group Decision Support Systems, and Computer Supported Collaborative Work [13,17,31]. While these systems are used to support collaborative work and to make decisions, they are also used to support a much wider variety of group tasks [10,17]. For this reason, we prefer the term Electronic Meeting System (EMS), which has been defined as an information technology-based environment to support group meetings, which may be dispersed in space and time [6].

Most early efforts to develop EMS met with very limited success $[17]$ . In 1986, Kraemer and King identified three barriers to the widespread use of EMS technology $[16]$ . First, developers and researchers had an incomplete understanding of group work processes. Second, professional quality EMS systems were not readily available. Third, there were problems with the underlying technology to support EMS, including a lack of adequate systems to support computer communications. The importance of adequate network support for communications has also been noted by other researchers. In 1987, network efficiency was cited as one of three major factors inhibiting effective support of group work $[20]$ . Providing adequate network support is a crucial issue in the design of EMS environments.

These barriers to success are gradually being overcome. First, while we still have an incomplete understanding of group work processes, our knowledge of computer support for group work processes is expanding [see 6, 17 for reviews of EMS literature]. Second, several new EMS systems have been developed [e.g. 8,11, 20, 31, 34]. Third, since 1986, the underlying technology to support microcomputer-based EMS has continued to evolve. Microcomputers have become faster and more powerful as has local area network hardware and software.

The purpose of this paper is to describe the communication needs of several different forms of EMS technology and to benchmark the performance of two local area network (LAN) software packages and three network servers for one EMS environment. Section 2 discusses the EMS concept, examines several EMS environments and configurations, and presents general approach to the evaluation of communication systems to support EMS. In the third section, we examine previous LAN evaluations. The fourth section presents the communication requirements of one specific EMS environment, and describes the benchmarking methodology used in this study, which is somewhat different from the benchmarking strategies discussed elsewhere (e.g. 26). The fifth and sixth sections present the results and discuss their implications, respectively. We conclude with a summary of our observations, and a discussion of directions for future research.

## 2. Evaluating Communications Support in EMS Environments

## 2.1. The EMS Concept

One primary purpose of EMS is to enhance communication among group members $[10,13,16]$ . While there are several ways that a EMS can enhance group communication, one major contribution is the addition of a new communication channel. With a EMS, each group member has a workstation (although it could be shared with another group member), linked via a computer network to other group members' workstations. Each member can use the workstation to communicate with other group members, although in many EMS environments, group members can have verbal conversations as well.

While the tasks performed by groups (e.g. strategic planning, operational decision making, negotiation, collaborative writing) are different, they often share common activities, such as idea generation, idea organization and voting/decision making $[13]$ . More recent EMS systems have been designed as tool kits, similar in concept to a Decision Support System (DSS) model base or tool set $[28]$ EMS tool kits are collections of specific tools that support specific group activities, rather than entire business functions. Fig. 1 illustrates some activity-based tools that could be used to support specific business functions; this figure is certainly not complete, but does provide an illustration of the basic needs of several business functions. For example, strategic planning often involves a wide variety of activities, from idea generation and organization to impact analysis and the drafting of specific policies. In contrast, writing a proposal will often involve fewer activities, perhaps just an initial idea generation phase where key issues are identified, followed by a more in-depth exploration of each issue that needs to be addressed in the proposal.

![](/api/attachments/TJEVH8AC/fulltext/images/1a29dfa582826976fdd95b64e76a0d1a1f1222be4c0386229b34a86d8fa30669.jpg)  
Fig. 1.

The key advantage provided by EMS tool kits is flexibility. There may be a variety of tools to support each activity. For example, the EMS developed at the University of Arizona provides several idea generation tools, such as Brainstorming, Nominal Group Technique and Delphi. Each tool in the tool kit will have its own meeting dynamics. One tool in the tool kit may support a highly structured interchange of ideas via the computer supported electronic communication channel, while another tool may encourage more verbal discussion. Thus the electronic communication requirements of a EMS will depend on the specific EMS tools used to support the group meeting.

## 2.2. EMS Environments

The environment within which EMS software tools are used also has a significant impact on the communications support required. Several classifications for EMS environments have been developed [eg. 9, 10, 15]. Fig. 2 presents a taxonomy of EMS environments that integrates and builds on earlier EMS categorizations [6]. Although only the front six blocks are labelled (i.e. synchronous meetings), these labels also apply to their asynchronous counterparts.

With a Decision Room EMS environment, a small group of participants meets at one time in one room equipped with a EMS and wide screen computer video projection screens for public viewing of comments. Face-to-face (e.g. verbal) group interaction is available as well as EMS-supported electronic interaction. Legislative Sessions differ from Decision Room sessions only in size (they accommodate larger groups) and in the degree of communication sophistication required of the EMS software. While verbal communication is still possible with a large group, it is less effective. Either the equal participation of all group members is removed, or, if equal participation occurs, each participant has far less time in which to communicate his/her ideas and opinions than he/she would in an equivalent small group meeting. Thus supporting a Legislative Session will place more of a load on a LAN than supporting a Decision Room session, as there is a higher volume of electronic communication.

Fig. 2. EMS Environment Taxonomy.  
![](/api/attachments/TJEVH8AC/fulltext/images/fc400854f243fb1f98a5b1d9a2b59bf42af80eda92f28b1cd67afc1960ae7e30.jpg)

A group of dispersed individuals could use a Local Area Decision Net to support small group work or Computer Conferencing for larger groups. Both Local Area Decision Nets and Computer Conferencing can be used by groups meeting at the same time, or at different times. The demands placed on the supporting LAN increase, as verbal communication is no longer possible. For otherwise equivalent meetings held in a Decision Room and Local Area Decision Net, the Local Area Decision Net will require more electronic communication.

When several groups (of any size) meet in separate locations, EMS Teleconferencing facilities are used. This is similar to non-EMS supported teleconferences, but with the addition of a EMS to facilitate intra- and inter-group communication. Each group works within itself, but transmits its results to the other groups for consideration in their subsequent sessions. The LANs supporting a EMS Teleconference need to be more sophisticated, as they must support both intra-group communication and inter-group communication. Long distance information transmission between LANs also becomes an issue.

## 2.3. Decision Room Meeting Processes

Most EMS research to date has focused on the use of decision rooms, although research is beginning to examine distributed environments [6]. Developers have taken rather different approaches to the basic design of EMS Decision Room technology. We have identified three types of EMS-supported group work process requiring network communication support, which we term a supported meeting process, graphically supported meeting process, and an interactive meeting process. Some EMS are capable of supporting two or even all three styles of meeting process, and thus it can be difficult to classify entire specific EMS into one category. However, each type of meeting process places different demands on the supporting network software, and thus in evaluating network software, the specific meeting process should be considered. It should also be noted that meetings observed in field studies have used more than one meeting process at different stages of a given meeting to address different sub-tasks.

With a supported meeting process, each group member has a workstation that is used to communicate ideas, comments and opinions to other group members. A large public display screen is also used to provide a repository for the group's information, thus providing an electronic version of the traditional blackboard, whiteboard or flipchart. The group verbally discusses the issues under consideration, with the electronic blackboard used to record and structure information the group deems appropriate. Any member of the group can work with the information on the blackboard, thus enabling some work to be done in parallel - i.e. two or more group members can add information simultaneously. The meeting proceeds using a mixture of sequential and parallel processing; participants can work in parallel using the electronic channel, but work sequentially when using the verbal channel. This type of EMS potentially provides both formal/informal structure and an additional communication channel. Examples of supported meeting processes include work done at the University of Minnesota as reported in [8].

A graphically supported meeting process is similar to a supported meeting process, but differs in that the basic form of information and information presentation is graphical. Rather than the lists of textual information found in the supported meeting process, information is typically displayed with lines, boxes, windows, etc. visually displaying relationships, precedence, and interconnections. Examples of graphically supported meeting processes include work done at Xerox PARC as reported in [31].

An interactive meeting process is distinctly different from either a supported or graphically supported meeting process, in that the electronic communication channel provided by the EMS is used for most group communication. During an electronic meeting process, virtually no one speaks. All participants work in parallel, sending typed comments to other participants without waiting for others to finish “speaking.” While an electronic blackboard may be provided, the group information is typically too large to fit on one screen, and thus group information is typically maintained so that all group members can access it electronically. This parallelism potentially enables more to be accomplished in less time. While typing comments into a computer is slower than speaking, reading is faster than listening [12]. In this case, the EMS can contribute structure, a new, fully parallel, communication channel, and a recording of the meeting. Examples of interactive meeting processes include work conducted at the University of Arizona as reported in [20,21,22].

We expect that as each of these different styles of meeting has different effects on the group work processes of the meeting, some may be better than others for specific tasks, groups, and organizations. For example, in larger groups the major problem with a traditional non-automated meeting is communication among group members. For a meeting of a given length, the amount of time available for each member to speak is directly reduced as group size increases. Either everyone participates in the same proportion for less time, or participation becomes less equal, with a few group members dominating the meeting. The ability of a supported or graphically supported meeting process to improve communication in a large group is more limited than that of an interactive meeting process as much communication is still verbal, and thus suffers from these same problems. Therefore, for a large group, we speculate that the use of an interactive meeting process would be more appropriate. For small groups, however, verbal communication is likely to remain a viable option, as there are fewer people competing for “air time.” As verbal communication is a more natural form of communication, we speculate that for small groups, a supported or graphically supported meeting process could be more appropriate.

Each of these three meeting processes differ in the network support they require. A supported meeting process often generates a small number of extremely short text messages. Messages can typically occur in bursts, as members work in phases of verbal and electronic communication (i.e. “let’s generate some alternatives now”). Graphically supported meetings are similar, except that the exchange of graphical images requires much larger message sizes. Interactive meetings, on the other hand, have continuous exchanges of short to medium length text messages.

## 2.4. Factors for Evaluating Communication Support

In the previous sections, we have seen that EMS can provide support for several business functions. This support is provided by a collection of tools providing different meeting processes. In order to provide meeting support, one of the most important infrastructural facilities required is adequate electronic communication technology. Given the wide array of communication technology available in the market today, it is indeed very difficult to select the appropriate type of communication support. This section provides an approach for evaluating communication alternatives, specifically, local area networks.

Several factors can be used to evaluate LANs. These factors can be subdivided into three categories: technical factors that are generally applicable to local area networks, factors that need to be considered in the light of the specific application (in this case EMS tools), and miscellaneous factors (see table 1). The technical factors involve choice of topology, transmission technique, communication medium, and medium access protocol. These are the standard factors used in evaluating LANs [30].

However, it is also important to consider factors specific to the nature of the application $[4,23]$ . Since we are dealing with a set of EMS tools, each tool may perform a different activity. Hence, the traffic patterns generated by each tool may be different. For some EMS tools the traffic stems from the workstation to the network server and back. These transfers typically involve fairly small files that keep growing in size but not significantly. For other EMS tools, the file sizes may be large and flow of traffic may be from the network server to each workstation. The size of groups using the tools is yet another factor to be taken into account when evaluating the performance of the communication system. Currently, most EMS tools are used in a single location, usually one Decision Room. In the future, we expect group proximity to be an issue in evaluating the communication support. Several groups that are geographically dispersed may be simultaneously using the tools. Intergroup communication becomes an important issue in such a situation. Further, the dispersed groups may each be using a different type of LAN. This would require linking heterogeneous LANS together. Video, audio and teleconferencing also require transfer of voice and graphics (images) in addition to data and text. The nature of the tool determines the type of data transferred.

Table 1  
Factors for Evaluating LANS.

<table><tr><td>Technical Factors</td><td>TopologyTransmission TechniqueCommunications MediumMedium Access Protocol</td></tr><tr><td>Application Specific Factors (for EMS)</td><td>Type of EMSTraffic PatternsSize of FilesNumber of UsersGroup Proximity</td></tr><tr><td>Miscellaneous Factors</td><td>CostVendor SupportAdherence to StandardsReliabilityEase of InstallationSecurity</td></tr></table>

Evaluation of the communication and network system support should consider the effect of each of these factors on the performance of the system. Such a study would help to determine the relationship between the response time and the factors outlined above. However, it is not enough to choose the configuration that provides the minimum response time. While minimizing response time is important, we should not lose track of another set of miscellaneous factors that will help in choosing the appropriate communication system. These factors are vendor support, adherence to standards, and total cost of the hardware and software used for communication. The choice of an appropriate communication system is a multi criteria decision.

## 3. Previous LAN Evaluations

Traditionally, there have been three approaches to studying the performance of communication networks: analytical modeling, simulation, and benchmarking $[25,33]$ . In the evaluation of LANs, analytical modeling, where mathematical models are built based on network characteristics, seems to be the most common approach $[1,29]$ . In many cases, models used in the evaluations do not apply to a specific LAN product, but rather apply to a class of LANs. For example, many articles compare medium access protocols (eg. token ring architecture to slotted ring architecture or CSMA-CD architecture) [eg. 2, 30, 32].

However, as Bux observes:

Models of the above type are suitable to assess the performance characteristics of different access mechanisms (which usually imply a certain network topology) and thus are helpful in finding good network design. Such models, however, are not appropriate for determining application-oriented performance measures. [1, p. 351].

As well as being inappropriate for determining performance for specific applications (e.g. EMS), such models are also inappropriate for evaluating specific network products. Due to implementation issues in the network hardware and software design, products that appear to have the same network performance based on an analytical model or simulation, may have considerably different performance in practice $[27]$ . Finally, these models do not reflect the kind of performance that an actual user could expect, as they do not address the needs of a specific application $[3]$ . Therefore, in cases where we wish to examine specific network products for specific applications to determine the level of performance that a user could expect, direct performance benchmarking via a controlled experiment is most appropriate.

Although several experimental benchmarking studies of LAN performance have been done, most of these have examined the transfer of raw data between two operating systems, rather than examining the performance that a software application would have in these environments $[3]$ . An exception is a study that examined the performance of an Ethernet network under “typical” traffic patterns in a specific application environment of networked printers, shared data bases, and down loading of data and programs $[27]$ . Another study also examined application performance, but used an old implementation of an Ethernet network to examine general purpose LAN applications $[3]$ . While these studies are useful, technology has dramatically changed in the years since they were conducted $[24]$ .

More recently, several experimental evaluations of LANs have been conducted. One study examined the performance of the 3Comm Ethernet network using three different computers as the network server (an IBM XT, and IBM AT, and a 3Comm 3Server) [23]. Data was written to, and read from, each server in two groups (20 blocks of 1500 bytes, and 600 blocks of 50 bytes) by 1 through 12 workstations. Mean response time at each workstation increased exponentially with the number of workstations for both IBM servers, in both the read and write tests. After 4 workstations for the IBM XT and 6 for the IBM AT performance degraded sharply. In contrast, mean response times increased linearly with the number of workstations for the 3Comm 3Server.

In another study, four configurations were tested: (1) 3Comm Ethernet network hardware and software with a 3Comm 3Server network server; (2) 3Comm Ethernet network hardware and software with an IBM AT network: server; (3) 3Comm Ethernet hardware and Novell Netware software with an IBM AT network server; and, (4) IBM PC Network hardware and PC LAN software with an IBM AT network server [24]. Data was written to, and read from, the server in each configuration in three test sizes (750 bytes, 6K and 30K) by 1 through 15 workstations.

With the smallest data sizes, the Novell configuration performed the best, with mean workstation response times being essentially unaffected by increasing the number of workstations on the network. The pattern was similar for the pure 3Comm configuration until 10-11 workstations were added, whereupon response times began to increase. Both IBM configurations produced dramatically longer response times rising linearly with the number of workstations. With 15 workstations, the IBM PC Network configuration produced a response 20 times longer than that of Novell. For larger data sizes, response times increased more directly with the number of workstations on the network, but with the same general performance pattern among the configurations. Performance studies conducted by Novell have also shown Novell to outperform other network software [19].

The LAN evaluations discussed above provide some guidance in selecting an appropriate LAN for EMS applications, but most have not specifically addressed the data transfer needs of EMS. In summary, most previous evaluations have examined now obsolete LAN technology, focused on the non-EMS applications, or tested LANs with a smaller number of workstations than are often available in EMS applications.

## 4. Benchmarking Methodology

## 4.1. Benchmarking Strategy

In evaluating the performance of LANs, it is important to conduct network tests in the same environment, and under the same conditions as a typical user of the target application $[4,23]$ . The challenge is how to provide this environment in a consistent, yet realistic manner in all test conditions. Press $[25]$ addresses this problem by adopting a two-tier strategy. First, a program is developed to simulate the typical background activities that occur in the network, such as file transfer, file opening and closing, etc. This program is then started on several “background” workstations to generate typical network traffic. Second, one “foreground” workstation runs the application being tested, and records the actual response times encountered.

In this case, we determined that it would be more useful to examine the actual application environment with all workstations participating in the tests, rather than use a series of simulated “background” workstations running simulated tasks. This also had the advantage of providing application specific timing data from all workstations, not just one “foreground” workstation. As Press [25] noted, and as we observed in this study, there can be considerable variation in the mean response time recorded at each workstation, even among seemingly identical trials, depending upon the application’s and network’s conflict resolution strategy. Thus collecting data from many workstations can increase the accuracy of the timing results.

In this case, we used a special utility that enabled us to control the keyboards of all workstations participating in the test from one control workstation. Using this remote keyboard controller, we were able to conduct the tests with all participating workstations running the specific application software and collecting timing data. As the remote keyboard controller itself was operating across the network underneath the application layer, some degradation in application performance could be expected from the extra load caused by transmitting this one keystroke. However, it would be miniscule. Likewise, due to propagation delay over the physical medium, not all workstations would truly be controlled simultaneously. However, the propagation delay would be too small to measure, and was consistent across all test configurations.

## 4.2. Communications Needs of One EMS Environment

We have seen that different EMS technology configurations will have different communication support needs, and that different tools in those configurations that provide different meeting processes may place different loads on the supporting LAN technology. Defining a “typical” EMS session is impossible, as each category of environment has its own needs. One EMS that has been well accepted is the Group Systems EMS developed at the University of Arizona, which has been installed at more than 18 universities. Group Systems has been used for experimental research, as well as for field study research involving well over one hundred groups from the public and private sectors. It has also been installed at 33 corporate sites, where it is in daily use. Therefore, while identifying a “typical” EMS meeting session is impossible, the wide acceptance and use of this EMS suggests that using previous sessions supported by Group Systems would not be unreasonable. Group Systems provides many tools that can be used to support group work, each of which place different demands on the supporting LAN. However, the most commonly used tool is an idea generation tool called Electronic Brainstorming (EBS), which provides an interactive meeting process.

EBS is an idea generation tool that allows group members to simultaneously share comments via a series of networked computers. EBS provides an interactive meeting process. With EBS, each group member receives a file containing a brief question. Each member then enters initial comments and sends the file back out on the network in exchange for another file from another group member. He/she reads this file, adds more comments, and exchanges the file once again. All group members work simultaneously and in parallel. EBS can be configured to run under any category of EMS, but has primarily been used in Decision Rooms (with 4–12 users) and Legislative Sessions (with 12–24 users). While verbal communication is possible in these settings, past experience has shown that the electronic communication channel dominates the verbal channel [7,20].

What are the communication needs of a “typical” EBS session? EBS is essentially a series of file transfers between user workstations and the network server. Initially, a short file is sent to each user workstation. Comments are appended to this file and it is sent back to the server, exchanged for another file, to which more comments are added. Thus, the size of files transferred in the system is initially small, and gradually grows. From a study of 20 EBS sessions, we determined that the average size of comments added to the file at each workstation was 250 bytes, with an average of 10 file exchanges per user during each 30–45 minute session.

While EBS is one of the cornerstones of the EMS, it is certainly not the only tool in regular use. Many other tools place similar demands on the supporting LAN: frequent transfers of small files to and from the network server. However, some tools, which are used less frequently during sessions, involve the transfer of larger files (primarily from the server to each workstation). For example, Issue Identification (an idea organization tool), typically begins with the transfer of all comments entered during EBS from the server to each workstation. This file of all EBS comments typically ranges in size from 50K to 100K. In other cases, medium sized files (typically 10K in size) are transferred to and from each workstation. In summary then, the most common data communications needs of the Group Systems EMS involves the transfer of small files, which grow in size from 250 bytes to 2.5K. With other tools, medium (10K), and large files (50K–100K) are also transferred across the network.

## 4.3. Identifying Test Configurations

The performance of a LAN is determined by many factors, as discussed previously. Network hardware, such as the network interface cards installed in the network server and network workstations, and the physical medium connecting the workstations to the server, plays a key role (eg. twisted pair or coax cable). In addition to network hardware, performance is also influenced by the processors and disk storage media in the workstations and network server.

The network software also plays a key role. The network interface software manages the information transfer between the application software (the EMS), the operating system (DOS) and the network interface card. The network operating system is the operating system running on the network server(s), the computer(s) responsible for managing the operation of the network. In examining LAN performance, it is useful to examine the effects of network operating system characteristics, as well as specific network hardware and interface software, as, in some cases, it may be more efficient or effective to increase LAN performance by upgrading the network server's operating system, rather than upgrading the network hardware or installing a new network server.

## 4.3.1. Network Hardware and Network Operating System

The LAN configurations to be tested were chosen based upon several subjective and objective measurements. In determining which LAN's to evaluate, one of the primary driving forces behind the decision was the LAN's compatibility with present and future EMS environments. Another important consideration was the customer base of various network vendors. EMS applications will be used within a business environment, as compared to manufacturing or engineering environments. To be considered, the network vendor had to be a leader in the field with a generally positive reputation among business users. Product support also had to be evident in the choice of EMS network configurations to evaluate. In a recent survey of network users by DataPro [5], IBM Token Ring and Novell were perceived by business users to be among the best networks available, in terms of network speed, reliability, vendor support, and overall performance. Novell has been a key figure in the PC LAN market for the last several years and consequently is well represented among the Fortune 500 companies, as well as smaller companies. IBM also has a considerable presence. A final consideration, was the commitment vendors have shown to supporting network products, to better ensure that the benchmarked systems would last into the future.

The results of previous evaluations also helped determine the candidates for our test evaluation. We did not want to duplicate work already done, but rather build upon prior research. As mentioned earlier, two recent studies $[23,24]$ evaluated network hardware for 3Comm Ethernet and the IBM PC Network. The network operating system evaluated in these studies was the Novell Advanced NetWare, 3Comm 3Plus Network, and the IBM PC Network program. Novell's Advanced NetWare outperformed the other 2 network software packages on both hardware networks. Both Hardware configurations were of a CSMA/CD type. Would Novell perform as well in a Token Ring environment?

## 4.3.2. Network Servers and Workstations

Microcomputer technology continues to advance at a rapid pace. Development of the Intel 80286 and 80386 chips have led to a new standard in the PC market for business applications: IBM's PS/2 series. In selecting network servers and workstations for evaluation, the choice is essentially between the older PC/XT/AT technology and the newer PS/2 technology. We expect the PS/2 series to increase its presence in the business marketplace in the future. As our objective is to focus on the needs of present and future EMS applications, we chose to evaluate the performance of IBM PS/2 series.

## 4.4. Test Configurations

Therefore, the network hardware and software evaluated were the IBM PC LAN program, and Novell Advanced NetWare v2.0 running on the IBM Token Ring Hardware. The PS/2 models 50, 60, and 80 were used as network servers for the IBM PC LAN. As the version of Novell Netware we tested would not run on 80386-based microcomputers, only the Model 50, and Model 60 were used as network server for NetWare. We will refer to these configurations as NOV/50 (Novell software with the model 50 server), NOV/60 (Novell software with the model 60 server), IBM/80 (IBM software with the model 80 server), etc. (See table 2).

Table 2  
Test Configurations.

<table><tr><td>Name</td><td>Server</td><td>Software</td></tr><tr><td>IBM/50</td><td>IBM PS/2 50</td><td>IBM LAN</td></tr><tr><td>IBM/60</td><td>IBM PS/2 60</td><td>IBM LAN</td></tr><tr><td>IBM/80</td><td>IBM PS/2 80</td><td>IBM LAN</td></tr><tr><td>NOV/50</td><td>IBM PS/2 50</td><td>Novell</td></tr><tr><td>NOV/60</td><td>IBM PS/2 60</td><td>Novell</td></tr></table>

## 4.4.1. Network Software Differences

Novell's Netware integrates three software modules into one comprehensive package. The three software modules are: The Network Operating System; the Workstation Shell; and the Bridge. The Network Operating System is responsible for providing all network services including file, print and software protection services, as well as network security and messaging. The Network Operating System is a multi-tasking (and multithreaded) operating system. The Workstation Shell provides the means to incorporate the native operating system of the workstations with the network environment. The Bridge is necessary to provide for multiple network interconnections among dissimilar networks. Novell NetWare effectively requires a dedicated network server.

IBM's PC LAN Network does not require the use of a dedicated network server. The PC LAN Program consists of four basic components: PC-DOS 3.3; the Microsoft Redirector, the network server software and network utilities. While the PC LAN program offers some concurrent processing [14, p. 7–85], it is limited. Due to the reliance of DOS for file handling and file structure use and since DOS is a single-user, single-tasking operating system throughput diminishes quickly.

Another important difference between the IBM PC LAN Program and Novell's NetWare Program is the high level of flexibility that Novell offers due to its memory caching, hashing and disk access elevator seeking routines [19]. While both the IBM LAN program and Novell offer caching, Novell also indexes frequently used files and programs with a hashing scheme which reduces the overhead time needed to access the file or program. Another way in which Novell reduces the time required to access information involves an efficient scanning method called elevator seeking. Read/write requests are sorted into a priority list based on the current position of the read/write head, thus minimizing the disk head movement. $^{1}$

Thus, a priori, one would expect Novell NetWare to provide better performance than the IBM LAN software in general in a LAN environment. The question is: is there a performance difference in a EMS application environment, and, if so, is it significant?

## 4.4.2. Network Server Differences

Both the IBM PS/2 model 50, and model 60 use the 80286 microprocessor chip, whereas the model 80 uses the more powerful 80386 microprocessor. The model 60 and the model 80 share similar hard disks, while the model 50 has a slower hard disk. A priori, one would expect the model 80 to outperform the model 60, which in turn would outperform the model 50. Once again, the question is whether there is a performance difference in a EMS application environment, and, if so, whether it is significant. Another issue is cost. The cost of the model 80 is greater than the model 60, which in turn is greater than the model 50. Is the additional cost outweighed by the increased performance of the models 60 and 80?

## 4.5. Benchmarking Tests

As discussed previously, our objective was to measure the performance of specific LAN configurations supporting a typical EMS application. As such, the primary measure of performance was response time $[3,18]$ . Of course, measures of response time will also include the processing time required for application software to interface with the network hardware and software, which is as it should be. The total response time faced by an actual user application involves more than just network transit time; it also includes the time required for the network hardware and software to accumulate the information at the workstation or server, and present the information to the user application for processing.

One key variable in the use of EMS systems is the number of user workstations. Past EMS sessions have involved group sizes of 3 to 24 user workstations. To provide an evaluation that would be useful to many EMS builders, we chose to evaluate the configurations with several different group sizes. We balanced the desire for a limited number of group sizes against the need for a range of sizes by choosing 5 group sizes: 4, 7, 10, 15 and 20 user workstations.

Two general test categories were developed, EBS tests and DOS tests. The EBS tests involved testing the speed at which the actual EBS software operated on the specific LAN configuration. However, while EBS is the principal software tool used in the system, it is not the only tool. To simulate the network requirements of other tools, and to further investigate LAN performance, a series of file transfer tests using DOS were also performed. The DOS tests were run independent of EBS, and were developed to test the networks' speed to copy files from and to the network server as is done when using other Group Systems tools. These tests can be easily replicated by other researchers and do not require the presence of Group Systems. They also provide a broader range of tests than the EBS tests, as files of different sizes could to be used to determine the effect of increased volume on network speed.

## 4.5.1. EBS Tests

With EBS, each user enters comments into a local workstation file. When a comment is complete, the user presses a function key, and that file is copied to the network server, and another file is read from the server to the workstation. The EBS software was modified to generate time stamps before a file was copied to the sever and after a file was read from the server. The difference between these two times was the time required by the network software to send the file to the server, transfer another file back to the workstation, and present it to EBS processing. This time difference was calculated by EBS and stored in a local log file at each workstation for later analysis. The EBS tests were designed to simulate an EBS session, based on statistics compiled from 20 actual EBS sessions. As mentioned previously, those statistics indicated that the average comment size was approximately 250 bytes, with an average of 10 comments per user per session.

Due to the constraints imposed by the operation of the EBS facility, EBS could not be installed under all five network configurations. Therefore, only the IBM/60, IBM/80 and NOV/60 configurations were tested. Five separate, but identical, EBS tests were run for each configuration - one for each group size (4, 7, 10, 15, and 20).

The testing process went as follows. The EBS tool was started at each user workstation. Using the remote keyboard controller, a utility that enables one keyboard to control the keyboards of any or all workstations on the network, 250 bytes of information was entered on all workstations involved in the test. Then, using the remote keyboard controller, the function key instructing EBS to copy a file to the server and read a new file from the server was pressed. All workstations simultaneously attempted to transmit this information across the network. This process was repeated 9 more times, thus giving a total of 10 comments entered, and 10 data points per workstation collected.

## 4.5.2. DOS Tests

The DOS tests used batch files to copy files to and from the network server. As with the EBS tests, the time was recorded in a local log file at each workstation before and after the execution of the copy command. To provide a range of file sizes “typical” for EMS applications, we choose to test the time required to transfer files of size 250 bytes, 1K bytes, 10K bytes and 100K bytes, for reasons discussed earlier. As with the EBS tests, we ran the DOS tests with 4, 7, 10, 15, and 20 users.

Separate batch files were created for each test and for each and every workstation. We ran three trials for each file size/number of users/network configuration combination to provide a more reliable set of data for statistical analysis. To test the network under a load, we ran the copy commands at each workstation simultaneously. The keyboard controller was again used to synchronize the tests.

The copy “from” (read) test tested the speed of the server and network in reading a file from the server’s hard disk, transferring it across the network and storing it on each workstation. This process is affected by the speed of the network, and by the speed of the processor in the network server. The copy “to” (write) test tested the network speed, the processor speed of the server and, most importantly, the speed of the server’s hard disk.

## 5. Results

## 5.1. EBS Tests

As shown in fig. 3, the NOV/60 configuration outperformed both IBM configurations; NOV/60 is faster than IBM/80 (t = 13.24, p = 0.000) and IBM/60 configuration (t = 16.25, p = 0.000). The IBM/80 configuration is faster than the IBM/60 configuration (t = 4.54, p = 0.000). This graph also shows the effect of adding more users to the network. The performance of the Novell network is only slightly affected by adding more users. In contrast, the response time of the IBM PC LAN program increases linearly with the number of users.

To better understand the relationships between the factors influencing network performance, we performed a linear regression analysis. This analysis used the original response time data from the EBS tests (expressed in seconds) as the dependent variable. The three network configurations were coded using three indicator (0-1) variables. Several transformations (eg. natural logs, exponentials, squares, square roots) and interaction terms were tested. The results of the linear regression analysis using the Minitab statistical package are presented in table 3. The best regression model includes a constant plus three interaction terms, one for each network configuration. In this model, the first interaction term (shown as User\*I60 in table 3), represents the slope on the variable “number of users” for the IBM/60 configuration. In other words, for the IBM/60 configuration with between 4 and 20 users, we would expect average response time to increase by approximately 0.38 seconds for each user workstation added to the network. Similarly, for the IBM/80 and NOV/60 configurations, we would expect response time to increase by 0.28 seconds and 0.07 seconds, respectively, for each workstation added to the network.

![](/api/attachments/TJEVH8AC/fulltext/images/8c9cbcda065f3aabd4a205c85a0e9430f55ff7d89d0e852f7ccdcff493e2a63e.jpg)  
Fig. 3. Brainstorming Average Response Times.

Table 3

<table><tr><td colspan="5">Regression Analysis of Electronic Brainstorming Response Times.</td></tr><tr><td colspan="5">The regression equation is Time = 0.429 + 0.381 User * I60 + 0.279 User * I80 + 0.0745 User * N60</td></tr><tr><td>Predictor</td><td>Coef</td><td>Stdev</td><td>t-ratio</td><td>VIF</td></tr><tr><td>Constant</td><td>0.42886</td><td>0.06011</td><td>7.13</td><td></td></tr><tr><td>User * I60</td><td>0.381189</td><td>0.005683</td><td>67.07</td><td>1.7</td></tr><tr><td>User * I80</td><td>0.278990</td><td>0.005683</td><td>49.09</td><td>1.7</td></tr><tr><td>User * N60</td><td>0.074485</td><td>0.005683</td><td>13.11</td><td>1.7</td></tr><tr><td>s = 0.3342</td><td>R-sq = 97.7%</td><td colspan="3">R-sq(adj) = 97.6%</td></tr><tr><td colspan="5">Analysis of Variance</td></tr><tr><td>SOURCE</td><td>DF</td><td>SS</td><td>MS</td><td></td></tr><tr><td>Regression</td><td>3</td><td>678.24</td><td>226.08</td><td></td></tr><tr><td>Error</td><td>146</td><td>16.31</td><td>0.11</td><td></td></tr><tr><td>Total</td><td>149</td><td>694.55</td><td></td><td></td></tr></table>

Key. VIF: Variance Inflation Factor, DF: Degrees of Freedom, SS: Sum of Squares, MS: Mean Square.

The t-ratios for the coefficients on each variable are statistically significant at p = 0.000. The MSE and R-Squared values indicate that the overall regression model is statistically significant and useful. Approximately 97.6% of the variation in processing time can be explained by the number of users and the network configuration. The remaining 2.4% is random variation or is due to other factors.

This regression model can also be used to predict average response times for EBS. For example, for a 16 workstation EMS, we would expect an average response of 4.89 seconds for the IBM/80 configuration, as compared to 1.62 seconds for the NOV/60 configuration. Prediction is also a means by which to test the robustness of a regression model. In this case, the original response time data was randomly partitioned into two halves of 75 observations each. The first half was used to generate a new model of the same form as that shown in table 3. The coefficients for this new model were, of course, different from those of the model in table 3, but were remarkably similar – the same rounded to 2 decimal places. Using this model, predictions were made for the remaining 75 observations. The mean difference between the actual observations and the predicted observations was 0.09 seconds (mean absolute difference of 0.20 seconds), indicating that the regression model in this form is remarkably robust, and therefore, should be a reliable predictor of network performance.

![](/api/attachments/TJEVH8AC/fulltext/images/a97e29e5ce16941da8433a36fc6f94be8f02ea7c1bd3693de910d95a8bf9e530.jpg)  
Fig. 4. Effect of Adding Users to Network. (Read 250 byte file from server).

![](/api/attachments/TJEVH8AC/fulltext/images/c00f3887cf9fd97e5c84337609432a240f7cbb82e3013caa21cad2645f37cfb6.jpg)  
Fig. 5. Effect of Adding Users to Network. (Read 100K file from server).

## 5.2. DOS Tests

## 5.2.1. Read From Tests

As the read from and write to tests examine the network configurations for different speed characteristics, we will examine them separately. Fig. 4 graphically displays the effects of adding more users to the network configurations, when small files are read from the server. Novell provides the fastest time, with speed largely unaffected by adding more users to the system. NOV/50 and NOV/60 provide similar response times, as do the IBM/50 and IBM/60 configurations. As this is a test of server processor speed as well as network characteristics, it is not surprising that the IBM PS/2 Model 50 and Model 60 have similar performance – they both share the same 286 processor. Fig. 5 presents a graph of the same test, but with large file sizes. The pattern remains basically the same with the Novell configurations being faster than the IBM configurations.

Table 4  
Mean Response Times of Copy From Tests.

<table><tr><td rowspan="2"></td><td rowspan="2">Mean</td><td rowspan="2">Std</td><td rowspan="2">n</td><td rowspan="2"></td><td colspan="4">t-tests</td></tr><tr><td>N50</td><td>N60</td><td>I60</td><td>I50</td></tr><tr><td>I80</td><td>3.437</td><td>2.566</td><td>60</td><td>I80</td><td>2.57</td><td>2.51</td><td>-1.73</td><td>-2.00</td></tr><tr><td>N50</td><td>2.295</td><td>2.294</td><td>60</td><td>N50</td><td></td><td>-0.05</td><td>-3.91</td><td>-3.83</td></tr><tr><td>N60</td><td>2.316</td><td>2.321</td><td>60</td><td>N60</td><td></td><td></td><td>-3.86</td><td>-3.79</td></tr><tr><td>I60</td><td>4.401</td><td>3.483</td><td>60</td><td>I60</td><td></td><td></td><td></td><td>-0.48</td></tr><tr><td>I50</td><td>4.752</td><td>4.401</td><td>60</td><td></td><td></td><td></td><td></td><td></td></tr></table>

Regression Analysis of Copy From Tests Response Times.

<table><tr><td colspan="5">The regression equation is Time = 1.06 + 0.00515 User *Size + 0.0647 User *I80 - 0.0324 User *N50 - 0.0319 User *N60 + 0.157 User *I60 + 0.188 User *I50</td></tr><tr><td>Predictor</td><td>Coef</td><td>Stdev</td><td>t-ratio</td><td>VIF</td></tr><tr><td>Constant</td><td>1.06436</td><td>0.09031</td><td>11.79</td><td></td></tr><tr><td>User *Size</td><td>0.00514863</td><td>0.00007792</td><td>66.07</td><td>1.1</td></tr><tr><td>User *I80</td><td>0.064737</td><td>0.009943</td><td>6.51</td><td>1.6</td></tr><tr><td>User *N50</td><td>-0.032380</td><td>0.009943</td><td>-3.26</td><td>1.6</td></tr><tr><td>User *N60</td><td>-0.031935</td><td>0.009943</td><td>-3.21</td><td>1.6</td></tr><tr><td>User *I60</td><td>0.156658</td><td>0.009943</td><td>15.76</td><td>1.6</td></tr><tr><td>User *I50</td><td>0.187506</td><td>0.009943</td><td>18.86</td><td>1.6</td></tr><tr><td colspan="5">s = 0.7101 R-sq = 95.4% R-sq(adj) = 95.3%</td></tr><tr><td colspan="5">Analysis of Variance</td></tr><tr><td>SOURCE</td><td>DF</td><td>SS</td><td>MS</td><td></td></tr><tr><td>Regression</td><td>6</td><td>3040.70</td><td>506.78</td><td></td></tr><tr><td>Error</td><td>293</td><td>147.73</td><td>0.50</td><td></td></tr><tr><td>Total</td><td>299</td><td>3188.43</td><td></td><td></td></tr></table>

Key. VIF: Variance Inflation Factor, DF: Degrees of Freedom, SS: Sum of Squares, MS: Mean Square.

Are these differences statistically significant? Table 4 presents the means and standard deviations for all configurations, as well as t-tests on the differences. The NOV/50 and NOV/60 configurations provide essentially the same response time, as do the IBM/50 and IBM/60 configurations. Both Novell configurations are faster than the IBM/80 configuration, which in turn is faster than the IBM/50 and IBM/60 configurations.

A regression analysis was again performed to better understand the effects of file size and number of users on network response time. Table 5 presents the best regression model for the “from” tests. The MSE is statistically significant at p = 0.000, indicating that the entire regression model is statistically significant. The R-squared value is approximately 95.3%, indicating that 95.3% of the variability in processing time can be explained by the number of users, file size and network configuration. The remaining 4.7% is random variation or is caused by other factors.

The model has six interaction terms, all of which are statistically significant. The first variable (User\*Size) represents the total information volume flowing through the network. The remaining five variables indicate the effects of adding more users to each network configuration. The first of these five interaction terms (shown as User\*I80), indicates that, on average, for the IBM/80 configuration with between 4 and 20 users, we would expect response time to increase by approximately 0.06 seconds for each user workstation added to the network, assuming that the total network volume remained constant. Similarly, for each user added to the network (holding total network volume constant) we would expect response time to increase by 0.16 seconds for the IBM/60 configuration, and 0.19 seconds for the IBM/50 configuration.

The coefficients for the two Novell configurations are negative, which implies that response time decreases as we add users to the network, holding total network volume constant; in other words, for a given network volume, response time is better if that volume is spread across more users. While this could be interaction effects caused by the mathematics of the regression modeling technique (ie. multicolinearity), further analysis effectively ruled this out (see also the Variance Inflation Factors (VIF) in table 5). It more likely indicates the performance benefits provided by Novell's multi-threaded operating system. With multiple threads, several user file read requests can be handled simultaneously. Spreading a given volume across more users provides better response time.

Once again, in order to test the robustness of the regression model, the original response time data was randomly partitioned into two parts of 100 observations and 50 observations, with the larger part used to generate a new model and make predictions for the remaining 50 observations. The mean difference between the actual observations and the predicted observations was 0.30 seconds (mean absolute difference of 0.51 seconds), thus indicating that the regression model in this form is robust, and therefore, should be a reliable predictor of network performance.

## 5.2.2. Write To Tests

Figs. 6 and 7 graphically present the results of the tests writing small and large files (respectively)

![](/api/attachments/TJEVH8AC/fulltext/images/ab5b317a97196cb704b8567c5eafc2f2d83ef16ee73488374bb8c5ef2357222f.jpg)  
Fig. 6. Effect of Adding Users to Network. (Write 250 byte file to server).

![](/api/attachments/TJEVH8AC/fulltext/images/64ba01db6391b46560e724dd95358b5abf27685d14f8c7b315f2a49a49889cef.jpg)  
Fig. 7. Effect of Adding Users to Network. (Write 100K file to server).

to the server. Due to disk space limitations, the "To" tests using 100K files could not be performed with the NOV/50 configuration. The patterns are similar to the read from tests. Novell is again faster than the IBM network, except for large files. The IBM PS/2 Model 60 and the Model 80 produce similar test times, as they have the same model of hard disk; the model 50 is slower, as it has a slower hard disk. The Novell configurations are less affected by hard disk speed (especially for small files), as the Novell software uses multitasking and disk caching to increase I/O throughput.

Table 6 presents the means, standard deviations, and t-test results for the "To" tests. Two sets of data are presented: one for all file sizes (which omits the NOV/50 configuration), and one for the 250 byte to 10K files sizes. The NOV/50 and NOV/60 configurations provide essentially the same response time, as do the IBM/80 and IBM/60 configurations. Both Novell configurations are faster than the IBM/80 and IBM/60 configurations and the IBM/50 configuration, but not significantly faster than IBM/80 for files of 100K. IBM/80 and IBM/60 are faster than IBM/50.

Statistical regression analysis of the 'To' tests was conducted in the same manner as that described above for the "From" tests. Table 7 presents the results of this regression. The MSE is again statistically significant at $p = 0.000$ , and the R-squared value is $93.7\%$ . On average, for the IBM/80 configuration with between 4 and 20 users, we would expect response time to increase by approximately 0.13 seconds for each user workstation added to the network, assuming that the total network volume remained constant. Similarly, for each user added to the network holding total network volume constant, we would expect response time to increase by 0.22 seconds for IBM/60, and 0.65 seconds for IBM/50. The t-ratios on the two coefficients for the Novell configurations are not statistically significant. Therefore, we can conclude that the Novell configurations are primarily influenced by total network volume, not the number of workstations on the network.

Once again, in order to test the robustness of the regression model, the original response time data was randomly partitioned into two parts of 100 observations and 50 observations, a new model generated, and predictions made. The mean difference between the actual observations and the predicted observations was -0.23 seconds (mean absolute difference of 0.90 seconds), thus indicating that the regression model in this form is fairly robust, and should be a reasonable predictor of network performance.

Mean Response Times of Copy To Tests.

<table><tr><td rowspan="2"></td><td rowspan="2">Mean</td><td rowspan="2">Std</td><td rowspan="2">n</td><td rowspan="2"></td><td colspan="4">t-tests</td></tr><tr><td>N50</td><td>N60</td><td>I60</td><td>I50</td></tr><tr><td colspan="9">Smaller File Sizes (250 bytes - 10K)</td></tr><tr><td>I80</td><td>3.771</td><td>1.642</td><td>45</td><td>I80</td><td>8.29</td><td>8.96</td><td>-0.17</td><td>-6.55</td></tr><tr><td>N50</td><td>1.316</td><td>1.118</td><td>45</td><td>N50</td><td></td><td>0.28</td><td>-8.19</td><td>-11.56</td></tr><tr><td>N60</td><td>1.256</td><td>0.921</td><td>45</td><td>N60</td><td></td><td></td><td>-8.81</td><td>-11.87</td></tr><tr><td>I60</td><td>3.830</td><td>1.730</td><td>45</td><td>I60</td><td></td><td></td><td></td><td>-6.38</td></tr><tr><td>I50</td><td>7.425</td><td>3.363</td><td>45</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="9">All File Sizes (250 bytes - 100K)</td></tr><tr><td>I80</td><td>6.003</td><td>5.368</td><td>60</td><td>I80</td><td></td><td>1.19</td><td>-0.89</td><td>-3.86</td></tr><tr><td>N60</td><td>4.664</td><td>6.838</td><td>60</td><td>N60</td><td></td><td></td><td>-1.85</td><td>-4.45</td></tr><tr><td>I60</td><td>7.030</td><td>7.184</td><td>60</td><td>I60</td><td></td><td></td><td></td><td>-2.98</td></tr><tr><td>I50</td><td>12.03</td><td>10.850</td><td>60</td><td></td><td></td><td></td><td></td><td></td></tr></table>

Table 7  
Regression Analysis of Copy To Tests Response Times.

<table><tr><td colspan="5">The regression equation is</td></tr><tr><td colspan="5">Time = 0.729 + 0.0124 User *Size + 0.128 User *I80 + 0.0163 User *N50 + 0.0046 User *N60 + 0.222 User *I60 + 0.654 User *I50</td></tr><tr><td>Predictor</td><td>Coef</td><td>Stdev</td><td>t-ratio</td><td>VIF</td></tr><tr><td>Constant</td><td>0.7290</td><td>0.2589</td><td>2.82</td><td></td></tr><tr><td>User *Size</td><td>0.0123857</td><td>0.0002432</td><td>50.93</td><td>1.1</td></tr><tr><td>User *I80</td><td>0.12801</td><td>0.02824</td><td>4.53</td><td>1.6</td></tr><tr><td>User *N50</td><td>0.01634</td><td>0.02985</td><td>0.55</td><td>1.4</td></tr><tr><td>User *N60</td><td>0.00463</td><td>0.02824</td><td>0.16</td><td>1.6</td></tr><tr><td>User *I60</td><td>0.22185</td><td>0.02824</td><td>7.86</td><td>1.6</td></tr><tr><td>User *I50</td><td>0.65395</td><td>0.02824</td><td>23.15</td><td>1.6</td></tr><tr><td colspan="5">s = 1.984 R-sq = 93.8% R-sq(adj) = 93.7%</td></tr><tr><td colspan="5">Analysis of Variance</td></tr><tr><td>SOURCE</td><td>DF</td><td>SS</td><td>MS</td><td></td></tr><tr><td>Regression</td><td>6</td><td>16619.0</td><td>2769.8</td><td></td></tr><tr><td>Error</td><td>278</td><td>1094.2</td><td>3.9</td><td></td></tr><tr><td>Total</td><td>284</td><td>17713.2</td><td></td><td></td></tr></table>

Key. VIF: Variance Inflation Factor, DF: Degrees of Freedom, SS: Sum of Squares, MS: Mean Square.

## 6. Discussion of Results

Our first observation is about the performance effects of network operating systems. While network topology, transmission media and medium access protocols have received a great deal of attention in the design and development of communications networks, considerably less attention has been paid to network operating systems. This study has shown the dramatic performance effects that can be obtained from improved network operating system design. For example, as the NOV/50 configuration is 75% faster than the IBM/50 configuration, we can conclude that more than 75% of the response time in the IBM/50 configuration is due to the network operating system. For this configuration, increasing the speed of the network hardware would be ineffective; increasing network hardware speed by a factor of 100 could be expected to decrease response time by at most 25%.

Perhaps the most interesting observations have to do with the transfer of small files. As mentioned before, EMS applications typically involve the transfer of small files. With EBS, files start very small in size (eg. 250 bytes) and gradually grow, usually to about 2.5K in size. After examining the EBS response time data, an unusual pattern emerged: although the file sizes grew from 250 bytes to 2.5K, response times appeared to remain constant, regardless of file size. A series of 675 t-tests were performed to test this hypothesis of constant response time (every trial's mean response times versus every other trial for the same configuration). From this set, only 15 pairs were statistically significantly different (at p = 0.05), which is less than could be expected in a perfectly random distribution. This, combined with a lack of a pattern in the significant values, indicates that when using the EBS software, file size has no effect on response time.

To further confirm this finding, we examined the differences in response time for the DOS tests between the 250 byte and 1K file sizes. Across all network configurations and all numbers of users, the mean response time for reading a 250 byte file from the server was 0.785 seconds with a standard deviation of 0.925 seconds. For 1K files it was 1.978 seconds with a standard deviation of 1.043 seconds. The difference in response time is not statistically significant (t = 1.70, p = 0.0892). Likewise, there is no statistically significant difference between 250 byte files and 1K files when writing to the network server (t = 1.10, p = 0.2714). Therefore, we can conclude that for small files (in the 250 byte to 1K range), file size has no effect on response time when writing to the server, but may have a small effect when reading from the server.

This suggests that one important factor in network performance of particular interest in an EMS environment is the overhead imposed by the network operating system. For each data transfer across the network, the network operating system has to manage the token passing process, the allocation of disk space at the server and/or workstation(s), and the opening, writing and closing of data file(s). For the small files typical of an interactive meeting process, this fixed overhead is much larger than the variable transit time due to the size of the file, and thus overhead dominates transit time. The bottleneck is at the server with the network operating system, not with the transit speed of the physical network media. This further suggests that in a Decision Room environment providing a supported meeting process or interactive meeting process, improving the physical media (by replacing twisted pair cabling with fiber optics for example) should have only a minor effect on the overall response time encountered by users. However, in an EMS environment providing graphically supported meeting process, or an environment with integrated voice and video transmission, the physical media may still play a key role, as the data and file sizes transmitted across the network are potentially much larger and could dominate the fixed overhead.

From these two observations (that network operating systems have significant effects on response times and that for small files, file sizes have very limited effects on response times) we can make another observation. For EMS environments providing supported and/or interactive meeting processes, theoretical models of network performance and simulations based on them may not be appropriate, as they are based substantially on file size and network hardware speed. For example, the predicted network performance calculated by a token ring model [2] is many orders of magnitude below the actual response times encountered by users.

## 7. Conclusions

The networking requirements of several EMS environments and the Group Systems EMS environment in particular, have been discussed. The principle requirement for many of the tools in this EMS and other EMS environments that provide an interactive meeting process is fast and accurate transfer of small groups of text, usually less than 5K in size. Occasionally, larger blocks of text (10K and 50–100K) are transmitted across the network. Previous evaluations have shown several network configurations, including the IBM Token Ring hardware/Novell software configuration

Table 8
Key Findings.

\- In Electronic Brainstorming Tests, Novell Netware ran twice as fast as the IBM PC LAN Program for 4 users, and 4 times faster for 20 users.

\- In reading information from the network server, Novell Netware ran twice as fast as the IBM PC LAN program overall.

\- In writing information to the network server, Novell Netware ran three times as fast as the IBM PC LAN program overall.

\- In all tests, Novell Netware was less affected by increasing network volume or the number of users for a given network volume. For very small files (1K and less), Novell's performance was unaffected by total network volume or the number of user workstations.

\- When using Novell Netware, there was no performance difference between an IBM PS/2 Model 50 and a Model 60 server.

\- When using the IBM PC LAN program, there was no performance difference between a Model 50 and a Model 60 server then reading files from the server.

\- When using the IBM PC LAN program, there was no performance difference between a Model 80 and a Model 60 server when writing files to the server.

\- In virtually all cases, Novell Netware on a Model 50 server ran faster than the IBM PC LAN program on a Model 80 server.

\- When dealing with the small files common to EMS applications (2.5K and less), files size has no effect on network performance. Therefore, increases in network hardware speed are likely to have little effect on response time.

available to provide a good level of performance across a wide range of applications. Our EMS-specific testing has produced similar results, as summarized in table 8.

In short, the Novell network operating system running on an IBM PS/2 Model 50 or Model 60 server consistently outperformed the IBM PC LAN software running on an IBM PS/2 Model 50, Model 60 or Model 80 server. The Novell software was 2–4 times faster than the IBM software on the same server; NOV/50 was $1\frac{1}{2}$ -3 times faster than IBM/80. One configuration outperforms all others tested. From a both a cost and a performance perspective, the best choice appears to be the IBM Token Ring hardware/Novell software configuration running on an IBM PS/2 Model 50. This configuration provides at least as great speed as any configuration tested, and the list price of the Model 50 processor with hard disk is substantially less than the Model 60 or Model 80. While the Model 60 and 80 provide more disk space than the Model 50, EMS applications typically do not require a substantial amount of server disk space, as most software is resident on the individual workstations, not the server.

Finally, and perhaps most importantly, the network operating system is arguably the most significant factor in determining network performance in interactive EMS environments. Rather than increasing network bandwidth to provide higher data transmission speeds, a more effective strategy is to use a more efficient network operating system. Increasing data transmission rates can be expected to provide marginal impacts on response time.

The overall objective is to determine the appropriate form of communications support within a variety of EMS environments. In this study, we have focused on one set of factors (network operating system and network server) within one EMS environment configuration (a Decision Room EMS providing an interactive meeting process). The next step is to move into other environments, studying other sets of factors. The factor with the greatest effect on network performance in a Decision Room environment (network operating system), may not be as significant in other environments, such as EMS Teleconferencing, once the distance between groups or group members increases. In these environments, for example, the need for voice and video signal transmissions, with their greater bandwidth needs, may suggest the greater importance of network hardware speed. Similarly, as the use of graphics in EMS becomes more wide spread, other performance factors may become more significant. Connectivity with other LAN's (in EMS teleconferencing, for example) and the ability to use existing organizational resources, such as corporate data bases stored on a mainframe computing system, will become increasingly important in the future. Thus factors other than performance may also have a major impact on the communications requirements for EMS in the future.

## References

[1] W. Bux, "Performance Issues in Local-Area Networks", IBM Systems Journal, 23:4, 1984, pp. 351–373.

[2] W. Bux, “Local-Area Subnetworks: A Performance Comparison”, IEEE Transactions on Communications, 29:10, October, 1981, pp. 1465–1473.

[3] L. Cabrera, E. Hunter, M.J. Karels, and D.A. Mosher, "User-Process Communication Performance in Networks of Computers", IEEE Transactions on Software Engineering, 14:1, January, 1988, pp. 38–53.

[4] R. Cowart, and P. Feldmann, “Benchmarks for Network Ratings”, PC Magazine, February, 195.

[5] Data Pro Reports on Communication: Network Architecture, Volume 1, C11-010, June 1986. pp. 501–508.

[6] A.R. Dennis, J.F. George, L.M. Jessup, J.F. Nunamaker Jr. and D.R. Vogel, "Information Technology to Support Electronic Meetings", MIS Quarterly, 12:4, Dec 1988, pp. 591–624.

[7] A.R. Dennis, A.R. Heminger, J.F. Nunamaker Jr., and D.R. Vogel, “Bringing Automated Support to Large Groups: The Burr Brown Experience,” Information & Management, 18:3, 1990, pp. 111–121.

[8] G. DeSanctis, and G.W. Dickson, "GDSS Software: A Shell System in Support of a Program of Research", Proceedings of HICCS Conference, 1987.

[9] G. DeSanctis, and R.B. Gallupe, "Group Decision Support Systems: A New Frontier", Data Base, 16:2, Winter 1985, pp. 3–9.

[10] G. DeSanctis, and R.B. Gallupe, "A Foundation for the Study of Group Decision Support Systems", Management Science, 33:5, May 1987, pp. 589–609.

[11] R.B. Gallupe, and J.D. McKeen, "Beyond Computer Mediated Communication: An Experimental Study into the Use of A Group Decision Support System for Face-to-Face Versus Remote Meetings", Administrative Sciences Association of Canada, 1988 Conference, pp. 103–116.

[12] S.R. Hiltz, K. Johnson, and M. Turoff, “Experiments in Group Decision Making Communication Process and Outcome in Face-to-Face Versus Computerized Conference”, Human Communication Research, 13:2, Winter 1986, pp. 225–252.

[13] G.P. Huber, “Issues in the Design of Group Decision Support Systems”, MIS Quarterly, Sept 1984, pp. 195–204.

[14] International Business Machines Corporation, IBM PC Local Area Network Program User's Guide, Third Edition, April 1987, Boca Raton, Florida.

[15] M.T. Jelassi and R.A. Beauclair, "An Integrated Framework for Group Decision Support Systems Design", Systems, Objectives, Solutions in Information and Management, 13, 1987. pp. 143–153.

[16] K.L. Kraemer, and J.L. King, “Computer-Based Systems for Cooperative Work and Group Decision Making: Status of Use and Problems in Development”, Proceedings of the 1986 Conference on Computer supported Collaborative Work, pp. 353–375.

[17] K.L. Kraemer and J.L. King, “Computer-Based Systems for Cooperative Work”, Computing Surveys, 20:2, June 1988, pp. 115–146.

[18] K.A. Lantz, W.I. Nowicki, and M.M. Theimer, "An Empirical Study of Distributed Application Performance", IEEE Transactions on Software Engineering, 11:10, October, 1985, pp. 1162–1173.

[19] Novell Inc., LAN Operating System Report 1956, Novell Inc., Provo, Utah, February, 1987.

[20] J.F. Nunamaker Jr., L.M. Applegate and B.R. Konsynski, "Facilitating Group Creativity with GDSS", Journal of Management Information Systems, 3:4, Spring 1987, pp. 5–19.

[21] J.F. Nunamaker Jr., L.M. Applegate and B.R. Konsynski, "Computer-Aided Deliberation: Model Management and Group Decision Support," Journal of Operations Research, November-December, 1988.

[22] J.F. Nunamaker Jr., D.R. Vogel, A.R. Heminger, B. Martz, R. Grohowski and C. McGoff, "Group Support Systems in practice: Experience at IBM", Decision Support Systems, 5:2, 1989, pp. 183–196.

[23] G.S. Poo, and G.H. Ong, "Performance Evaluation of an Ethernet Network", Computer Communication, 9:3, June, 1986, pp. 128–134.

[24] G.S. Poo, and T.S. Tan, "Performance Comparison of PC

LAN File Servers - An Experimental Study", Computer Communication, 11:2, April, 1988, pp. 71–79.

[25] L. Press, “Benchmarks for LAN Performance Evaluation”, Communications of the ACM, 31:8 August 1988, pp. 1014–1017.

[26] L.S. Richman, "Software Catches the Team Spirit", Fortune, June 8, 1987.

[27] J.F. Shoch, and J.A. Hupp, "Measured Performance of an Ethernet Local Network", Communications of the ACM, 23:12, December, 1980, pp. 711-721.

[28] R.H. Sprague, “A Framework for the Development of Decision Support Systems”, MIS Quarterly, 4:4, December 1980.

[29] W. Stallings, “Local Networks”, Computing Surveys, 16:1, March, 1984, pp. 3–41.

[30] W. Stallings, Data and Computer Communications, second edition, Macmillan Publishing Company, New York, 1988.

[31] M. Stefik, G. Foster, D.G. Bobrow, K. Kahn, S. Lanning and L. Suchman, “Beyond the Chalkboard: Computer Support for Collaboration and Problem Solving in Meetings,” Communications of the ACM, 30, 1, January, 1987, pp. 32A7.

[32] B.W. Stuck, "Calculating the Maximum Mean Data Rate in Local Area Networks", IEEE Computer, May, 1983, pp. 72–76.

[33] S.K. Tripathi, Y. Huang, and S. Jajodia, "Local Area Networks: Software and Related Issues", IEEE Transactions on Software Engineering, 13:8, August, 1987, pp. 872–879.

[34] D.R. Vogel, J.F. Nunamaker Jr., J.F. George, and A.R. Dennis, “Group Decision Support Systems: Evolution and Status at the University of Arizona”, in R.M. Lee, A.M. McCosh, and P. Migliarese (eds), Organizational Decision Support Systems, Proceedings of IFIP WG 8.3 Working Conference on Organizational DSS, North Holland, 1988, pp. 287–305.
