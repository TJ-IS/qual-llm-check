---
otero_id: 22832
otero_key: "438STX7D"
title: "A strategic client/server implementation: new technology, lessons from history"
authors: "Mary C. Lacity; Leslie P. Willcocks; Ashok Subramanian"
year: "1997"
journal: "The Journal of Strategic Information Systems"
doi: "10.1016/s0963-8687(97)00009-7"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A strategic client/server implementation: new technology, lessons from history

Mary C. Lacity $^{a,*}$ , Leslie P. Willcocks $^{b}$ , Ashok Subramanian $^{c}$

$^{a}$ School of Business Administration, University of Missouri, St. Louis, MI, USA $^{b}$ School of Management Studies, Templeton College, University of Oxford, Oxford, UK $^{c}$ School of Business Administration, University of Missouri, St. Louis, MI, USA

Received 1 November 1996; accepted 1 May 1997

## Abstract

Despite the rapid growth in client/server technologies and their development and usage in work organizations, there have been all too few academic studies of the technical human and organizational issues associated with the phenomenon. This paper provides a longitudinal case study of a 1989–1995 client/server project in a \$1 billion annual revenue United States based silicon chip manufacturing company. Using an interpretive research approach the financial and business dimensions of the projects' success were analysed. Seven critical enabling factors were identified, namely business re-engineering driving technical choices, insourcing of new development, the form of vendor partnering adopted, incremental implementation approach, senior level support and participation, close IS-user relationships and IS seen as a business investment, not just a cost centre. These suggest that there is little difference in implementing client/server compared to any other information technology new to an organization. The paper tests this point further by comparing distinctive issues raised by client/server as suggested in the wider IS literature, against the specifics of the case history. © 1997 Elsevier Science B.V.

Keywords: Client/server; Technology; Strategy

## 1. Introduction

There is much evidence that organizational adoption of client/server computing (see Appendix A for a description of the client/server paradigm) has become one of the more significant phenomena in the information technology field. According to recent surveys 71% of all new applications are being developed for desktop or mid-range computers as compared to 29% for mainframe computers. Moreover, 68% of organizations use specialized servers in their computing architecture in contrast to 9% which use mainframes only (Allen, 1995; ComputerWeekly, 1996). In the United Kingdom (UK), a 1995 survey of 750 IT professionals found 43% of respondent organizations had already implemented client/server and 34.5% were considering implementing the approach. Only 5.8% had considered client/server and rejected it (Green-Armytage, 1995). In the USA, Gerber (1995) has estimated that 40% of information technology dollars are being spent on client/server development, deployment, and support. If infrastructure costs, such as hardware, systems software, and networking gear are included, client/server expenditures rise to 60%. In a survey of 207 US companies Kole et al. (1995) found that 66% were planning to implement client/server on an enterprise level. The study concluded that the scope of client/server systems between 1996 and 1998 would increase from intra-departmental to global systems. Seemingly, these statistics are strong evidence of the significance of client/server information systems and the rapid adoption and diffusion of client/server systems in the 1990s.

However, as for many 'advances' in information technology (IT), the public sources, including trade journals and newspapers, regularly underplay the organizational issues associated with adopting new technologies. There is an inherent assumption that adoption will lead to business success. Invariably the business case is logically argued and grounded: through enhanced data sharing, integrated services, cost reduction due to downsizing, interoperability and data interchangeability, location independence of data and processing, and centralized management, client/server promises to transform data into knowledge, to empower users, to increase the quality and speed of decisions (see, for example, King, 1994; Simpson, 1995). Moreover, given advances in technology, such as increases in input/output over networks, storage capacity and cost, graphical user interfaces, relational databases, and the proliferation of local area networks, these business benefits can be affordably achieved (Muller, 1994; Renaud, 1993; Wagner, 1995a).

However, by 1995–1996, studies had begun to uncover organizational and technical barriers and implementation issues associated with client/server technology. Thus the Gartner Group conducted a survey in 1995 of 100 companies that had implemented client/server. Over half of the implementations were late and over-budget, although the final implementations did produce business benefits (Lyons, 1995). A study by Sentry Market Research shows only a 3% increase in client/server adoption in 1995 over the previous year across 712 large enterprises in North America and Europe. The reasons cited include unexpected complexity of infrastructure demands (Pontin, 1995). Recent survey research found a range of difficulties registered by respondents, including skills shortages, lack of executive management support, lack of money and complete development tools, and mistaken reliance on a centralised management model to keep distributed management costs in line (Forrester Research, 1995). Sometimes the difficulties have resulted in abandonment of moves to client/server. As one high profile example in the UK, after a £235 million client/server investment programme, in 1996 North West Water abandoned plans to implement its main Oracle database on a distributed Unix platform, and reverted to a mainframe-based strategy (Collins, 1996).

However, despite a number of large-scale client/server surveys, and much prescriptive, together with some relatively rudimentary case study work (see, for example, Bochenski,

1994; Levis and von Schilling, 1994; Mill, 1994; Renaud, 1993) there has been all too little systematic, let alone academically rigorous, study of client/server implementations within the context of specific organizations. In this paper, therefore, we present findings from a detailed case study of a world-wide client/server implementation at a silicon manufacturing company, here called Silicon Inc. to retain the confidentiality requested by our respondents. We selected the case of Silicon Inc.'s world-wide implementation of customer ordering, manufacturing planning, plant scheduling and product specification system because it had been widely recognised — and portrayed externally (by Computerworld) — as a successful project. Our aim in studying this case in considerable detail was to investigate academically the dimensions and degrees of 'success'; the factors that were cited by managerial respondents as responsible for effective implementation; and whether there were difficulties and issues that arose distinctive to large-scale client/server implementation in a work organization, or whether such difficulties were typical of any major new information-based technology project.

## 2. Research methodology

## 2.1. Case study approach

The strengths and limitations of case research in the study of information systems, and the reasons for pursuing a case research strategy, are by now well established in the literature (see Benbasat et al., 1987; Eisenhardt, 1989; Kaplan and Duchon, 1988; Lee, 1989; Yin, 1989). There is also now a considerable supportive literature on the adoption of qualitative and interpretive methods in information systems studies (see, for example, Lacity and Jansons, 1994; Van Maanen, 1979; Walsham, 1995). Additionally a number of researchers have successfully justified and applied a single case study research strategy for examining phenomena in the information systems field (see, for example, Markus, 1983; Smith, 1990; Walsham and Waema, 1994). Informed by this literature the present research adopted an interpretive and qualitative longitudinal single case research strategy in order to explore the under-researched area of client/server implementation. In more detail, the case study is a history studied retrospectively in a 6 month period in 1995–1996, relying largely on recollection by respondents rather than on personal observation of events during the 1989–1995 period. The study is not only retrospective but also relies on the recollection of a small group of respondents, though these were central to and very knowledgeable about the events under review. A further issue and caveat: since the study is largely interpretive, a double hermeneutic should be noted — the researchers are interpreting the interpretations of the respondents. While noting these issues and limitations, it should be noted that client/server surveys of varying degrees of rigour have regularly appeared, together with short case histories largely in trade magazines, but client/server has rarely been the subject of a detailed, academically conducted case study.

Detailed interview protocols were prepared (see Table 1 for a summary of issues covered). The research sought to elicit descriptive contextual information together with respondent opinion on a range of issues in a project widely considered 'successful'. We sought to explore the dimensions of this 'success' and also the difficulties experienced in the project. Within this prior structuring of concerns and questioning the research then proceeded inductively to build the case study from interview material, documentation, organizational records, and a review of physical evidence in the form of systems and their operation in various organizational contexts. This allowed us to develop our own analysis as an overlay on the several accounts produced by the organizational respondents at Silicon, Inc.. We then sought to compare and evaluate the lessons and difficulties that emerged from our analysis with those to be found in the wider literature on client/server implementation. The comparison allowed us to suggest ways in which client/server may be distinctive, and more difficult to implement, or encounters similar problems and requires implementation approaches not dissimilar for all new information-based technology projects of any size.

Table 1  
Interviewees and interview objectives

<table><tr><td>Subscript</td><td>Senior Level IT Manager (Robert)</td><td>IT Manager/staff member involved in client-server implementation (David &amp; John)</td><td>Senior Business Manager for whom the client-server was built (Michael)</td><td>Supervisor of users of client-server application (Steven)</td></tr><tr><td>Generic interview script</td><td>X</td><td>X</td><td>X</td><td>X</td></tr><tr><td>Motivation for client-server project</td><td>X</td><td>X</td><td>X</td><td>X</td></tr><tr><td>Outcome of client-server project</td><td>X</td><td>X</td><td>X</td><td>X</td></tr><tr><td>Objective information</td><td>X</td><td></td><td></td><td></td></tr><tr><td>Perceptions of IT within organization</td><td>X</td><td>X</td><td>X</td><td>X</td></tr><tr><td>Technical issues</td><td></td><td>x</td><td></td><td></td></tr><tr><td>Project management issues</td><td>X</td><td>X</td><td></td><td></td></tr></table>

## 2.2. Interviewing

We interviewed different stakeholders within Silicon, Inc., including business unit managers, IT managers, and IT staff (see Table 1). The specific titles and pseudonyms of the participants are:

• Robert, the Director of MIS, inherited the project in 1991 when he became head of IS;

\- Steven, the Manufacturing Services Support Systems Supervisor, is a current business manager over the users of the system;

\- Michael, the Strategic Manager of Marketing, was the lead user and project manager of the entire project;

\- David, the Manager of Business Information Systems, headed the business applications development, implementation, and support;

\- John, a Senior Analyst, worked on David's team.

Two researchers together interviewed each respondent. This permitted an element of cross-checking on subsequent interpretations of the information communicated. The individuals described in Table 1 held different views on the client/server project. They provided longitudinal accounts of the decision-making process, and explained the context in which the client/server implementation was embedded. All interviews were conducted in person at the company site. All interviews were tape-recorded and transcribed, but participants were assured of anonymity so as to promote open discussions. We also gathered a number of documents including the acquisition request, user and technical documentation of the client/server project, annual reports, and the organizational chart. As can be seen from Table 1 the interview strategy permitted triangulation and cross-checking across the interviews on most issues investigated. While Robert was the main source for what we termed 'objective information' — basically company information like market share, number of employees, company's main markets — all statements could be checked also against documentation. David and John supplied most of the 'technical information' — for example descriptions of systems, IT organization, development tools — which was also verified against documentation.

Interviews followed the same protocol, proceeding from an unstructured to a structured format. During the unstructured portion, participants were asked to tell their client/server story. The unstructured format allowed the participants free rein to convey their interpretations. After participants completed their stories, they were asked semi-structured questions designed to solicit information on specific sourcing issues that may have been absent from their previous recollections. These interview protocols were highly detailed. A generic interview script focused attention on motivation for the client-server project (semi-structured questions on sponsorship, role of BPR, justification, budgeting, risk perceptions), on outcomes (success/failure; costs; benefits; critical factors), on perceptions of IT within the organization (for example, different stakeholders views, was IT seen as cost or asset, leader or follower with IT) technical issues, and project management issues (for example, project team membership, development methodology, level of user participation, problems that arose). As indicated above participants were also asked specific questions about their company and IT department. Pertaining to their company, participants described the organizational structure, the major products and services produced, competition in their industry, their financial situation, corporate goals, and business successes and failures. Pertaining to IT, participants described their IT activity in terms of headcount, budget, chargeback system, user satisfaction, challenges, goals, and reputation.

The research approach enabled the construction of the case history that now follows. The analysis proceeds in two stages. In the first stage the financial and business outcomes of the implementation are analysed. We then isolate the critical success factors emerging from the case. In the second stage we review the client/server research literature to identify the distinctive technical and managerial issues that are invariably associated with client/server implementation. There follows an analysis of the degree to which these issues were supporting or constraining factors in the implementation. Finally, the paper identifies eight learning points on client/server implementation emerging from the case.

## 3. The case study: Silicon, Inc. 1989–1995

## 3.1. Context and history

Silicon, Inc. was started in 1989 as a result of a merger between a North American and a European company. Since then, Silicon has become one of the largest manufacturers of silicon in the world, with 11 plants spread throughout the United States, Asia, and Europe. At the end of 1995 Silicon, Inc. employed 5000 people world-wide. Annual sales were almost \$1 billion and expected to continue to grow as the world demand for silicon increases.

Silicon, Inc., exclusively makes custom products, taking special orders from the world's largest electronic companies. These customers are extremely sophisticated in engineering, computing technology, and manufacturing. Their demands for custom wafers requires as many as 200 parameters for product specification. Given their rate of innovation, customers' requirements change on average every six months. Thus, Silicon, Inc. rarely makes the exact same product twice.

To compete in this industry, silicon manufacturers must be able to meet the custom needs of their highly technical customers in a timely manner. Back in 1989, Silicon was at a competitive disadvantage because customers were frustrated by its inability to commit to orders, fill orders on schedule, or change orders in a timely fashion. The problem stemmed from a lack of shared information about each of the manufacturing plant's capabilities, capacities, and schedules. When a customer called the centralized sales office to ask whether X product could be manufactured by Y date, Silicon, Inc. took up to three weeks to call the customer back and confirm the order. The old business process first required a headquarters person taking the order to determine which plant had the capability to manufacturer silicon with the requested properties. Once the targeted plant was notified, that plant then determined what supply they needed to make that product. This often generated another internal order to another Silicon, Inc. plant. That second plant would then determine its ability to deliver the supply, and call back to Plant A, which would then be in a position to determine its ability to deliver the product. Plant A passed this information back to headquarters, which would then call back the customer to see if they still wanted the order. Many times, the customers found silicon manufacturers who responded quicker, thus representing a lost sale to Silicon, Inc. Michael describes the situation as follows:

It was a mess because you couldn't get accurate information. The cycle time to place an order after a customer calls in and says I want 2,000 more of Part Number Six for delivery in June, it would take us six or seven days $^{1}$ to process that because we would have to first receive the order in, then they'd have to figure out where to source the slices, and then the slice people say, 'Oh we need crystal.' Now we have to submit an order for the crystal people. They would have to find out where they were going to make it. In the meanwhile, no one was talking to the people in specifications and the customer says, 'I'll take material from site A but not from Site B.' And we were in a constant swirl there. – Michael, Strategic Manager of Marketing

Although an IT solution seemed obvious, traditionally IT was perceived as a necessary cost burden, rather than a business enabler, with senior management reticent to invest large sums in IT. Robert explains:

There is an agonising that goes on about the cost of this. Each year, going through the budgeting process, every year the budget goes up for two reasons. One — we are doing more and more, and two — we are getting bigger. We have more sites to support. And we need more people to do all of that. — Robert, Director of MIS

In addition to senior management perceiving IT as costly, they also perceived that service was poor. The IT managers blamed an outsourcing arrangement for the high costs and low service levels. At the time of the merger in 1989, Silicon, Inc. was forced to migrate off the mainframe of its previous parent company. Rather than build an internal data centre, Silicon, Inc. opted to sign with a service bureau for a \$100 000 per month fee. David, Manager of Business Information Systems, explains why service from the vendor was poor:

We were just one little fish in a big pond. So what we wanted was inconsequential to their other clients, which were significantly larger than we were in terms of revenue. So we tended to get—we got support—but it was slow.... We knew a lot more about what we wanted than they did. It became difficult to explain to them...it was easier for us to code up the macro and hand it to them than to explain, “I want an LU2.6 terminal that will do SNA/RJE to an AS400.” They would scratch their head and say, “We’ve never done that before.”— David, Manager of Business Information Systems

Thus, from a service and cost perspective, people at Silicon, Inc.'s US operations were dissatisfied with their mainframe supplier. At the same time, the European operations were looking to replace their mainframe systems. At that time, they had over-customized a manufacturing software package to the point where the vendor would no longer support it. The software was also lacking needed functionality as a result of the merger, such as dealing with multiple currencies and price breaks. The Chief Financial Officer in Europe had a vision that software running on smaller platforms was the future of IS, whereas as these antiquated mainframe systems were becoming increasingly obsolescent. More specifically, he wanted to replace these mainframe manufacturing systems with an integrated package which runs on a smaller platform (AS400). The need for such an integrated, world-wide information system prompted the World-Wide Systems Project in 1989. From this time on senior management's views on IT began to shift from seeing IT as a cost burden to viewing IT as a significant business investment, albeit one whose costs could not be limitless.

## 3.2. Client/server project

The original acquisition request (AR) for the world-wide systems project stated reduced cycle time to respond to customers as the primary justification. There was an attempt to quantify the costs and benefits, but the benefits, in particular, represented very rough estimates. On the cost side, the original AR requested \$6 million for a two-year project.

The expected cost benefits were loosely stated as \$15 million a year for projected increased sales due to better customer service and a savings of approximately \$500 000 a year to migrate off the mainframe. Michael gives his impressions of the projected benefits:

It was a bit loose, there is no doubt about that. It's almost one of those things where faith is an issue. Especially, when you deal with, “How is this going to affect the customer relationship?” Those are very difficult to put dollar values on, but just about everybody grasped that going from six days to less than a day has to be cost beneficial. But how much? We don't know. —Michael, Strategic Manager of Marketing

Michael, as Strategic Manager for Marketing, was put in charge of the project. He recruited ‘volunteers’ from the major user groups—order processing, product specifications, and production scheduling. These users were seen a vital for ensuring that the project not only met its business objectives, but to also foster faith in the system:

The working group took a lead role in coordinating amongst their peers to make sure that what we were building was what they wanted and needed. We had some oversight groups that made sure that was the direction we wanted to go in. –Michael, Strategic Manager of Marketing

## 3.3. Business applications

In the beginning (1989), the project team's first major task was to evaluate the specific software product solution proposed by the European CFO. The more the team studied the package, the more they realized it did not fit their business model. In particular, Silicon, Inc.'s custom-made products requires scheduling that conflicted with the assumptions of the package. Michael explains:

The deeper that we got into it, the more we started realizing that it didn't do scheduling. They used the classical MRP $^{2}$ type of system where there is an infinite schedule situation, which works real well in an environment where you are going to be making product to a forecast, putting it on a shelf and then drawing from the inventories to satisfy the customers. Well, that is not our business. Our business is a custom order fabrication type business. —Michael, Strategic Manager of Marketing

The parts of the package that did match Silicon Inc.'s business needs were not significantly different from their current mainframe applications. If they bought this package, they would have to retrain every user worldwide to perform essentially the same functions, with no added business benefit. The project team decided to augment the home-grown systems with packaged software to add functionality for order processing, planning, scheduling, and multiple currencies. These packages would be integrated with 'non-mainframe' versions of the current systems. The search for these additional software packages created a spin-off project team, headed by David.

David and his team evaluated several packages in the US and Europe. From a business standpoint, the best software was MIMI, which stands for ‘Manager for Interactive Modeling Interfaces.’ Michael describes the MIMI system from a user perspective:

It looked like it had most of the things that we were interested in. It was based on finite capacity... It was based on a premise that you would have master models and submodels and they all talked together. Initially, we were looking at it more using the automated tools as opposed to the Star Wars tools as I call them, the drag and drop things.... The people in scheduling were getting excited about this.... When you start thinking about what's going on, you are essentially grabbing a block which is a schedule for a particular product with all the underlying data hiding underneath the block. If you decide, "I don't want to put that on that piece of equipment, I want to put it on this piece of equipment," you just point, click, drag, drop, and it spreads out the other schedules and recalculates all the underlying data like the start date, the start time, the quantities of the raw materials. It's pretty fantastic. —Michael, Strategic Manager of Marketing

From a technical perspective, however, the package was lacking because it was a single-user system. Each user had their own models stored in RAM, much like a stand alone spreadsheet package. When David was charged with enhancing this package to share models across user groups, the client/server solution emerged:

So, we looked at the tool and determined a major problem with it. That is, it was single user. It was essentially like a LOTUS spreadsheet. Everything was in memory. You couldn't share tables across users. So the only way to use this tool, which was an excellent finite capacity scheduling system—it had artificial intelligence, a backwards chaining inference engine, linear programming, a macro language, SQL links—the only way to use this in a multi-user mode was to take the tables that needed to be shared and put them into a relational database that sat in the middle of all of these various models as they are called...or programs or macros—whatever you want to call them. And then have all that data updated on a server that was sitting in the middle of all of the MIMI clients. We were suddenly client/server, although we didn't know it at the time. So it just evolved as the reason we did this. The reason we did this: there was no other way to get around the deficiency of the system at that time. —David, Manager of Business Information Systems

In 1991 the MIMI system was implemented. Robert's team downloaded the mainframe data containing all the parametric product specifications to the MIMI server. The MIMI system processed the specifications to create a standard set of parameters with a consistent set of measures (such as converting all quantities to the metric system). This functionality was known as 'central specification'.

After central specification, the data would be used as input for ‘central planning’. The central planning model looked at the product specifications and plant characteristics to determine which Silicon, Inc. plant should manufacture it. Robert explains:

The central planning model looked at bottle necked resources, and the relative capacities and capabilities of the plant sites on a world-wide basis and then determined what the allocation for manufacturing the product would to each of the plant sites world, which we have several throughout the world, each with different capabilities and capacities. The central planning model determined the best way to divvy out the manufacture of the product. — Robert, Director of MIS

The next step was ‘local recipe generation’. Once a plant was assigned to manufacture a product, the central specification data would be used to generate a local recipe to determine exactly how the plant will manufacture the product. This business requirement led to the purchase of another software package running on a client/server platform. David explains:

That took information from the central specifications database and at a specific site...we would generate a recipe, which is in essence taking information from this homogenized central spec data, looking at it and generating a 'here's how you would make it' route within the plant for that part that would be done in that plant. And then generate a document which was used at the shop floor through either a terminal inquiry or on hardcopy paper or both. —David, Manager of Business Information Systems

At this point in 1991, order-processing on the mainframe still served as the front end to all the downstream client/server systems. In addition, outputs from the client/server systems were uploaded to the mainframe so the sales offices could answer customer queries about scheduling. The fourth generation languages which queried this data generated over 700 mainframe reports per month. Both the order-processing and reporting were the last to be migrated off the mainframe in 1992.

The migration of the reports off the mainframe in May 1992 reduced the charges by \$20 000 per month, which pleased senior management. Once the 700 reports were migrated, however, several technical problems surfaced, such as rollback, transaction backout, locking records, and slow response time. For example, Silicon Inc. had to shut the US mainframe down over night to run the batch extracts, which was making the mainframe useless for most of day in Asia. Once again, David engaged the vendor as a ‘strategic partner’ to improve the product. The product was enhanced to concurrently run batch and online. The mainframe was only brought down one hour a night to do backups.

In November 1992, David and his group began the migration of the customer order entry and management system off the mainframe. They wanted to purchase a new product which essentially ran mainframe programs in a UNIX environment. David and John, a senior analyst, took the vendor's course in this new technology. During breaks, David compiled some of his programs and felt that the product showed promise to meet their needs, but the current version had many technical bugs. Silicon Inc. and the vendor became ‘strategic partners’, which mutually benefited both parties. Silicon Inc. received an immense discount on the vendor's resources, including use of the vendor's data centre to convert the 700 programs and access to their top technical specialists, in exchange for the vendor using Silicon, Inc. as a software test sight. David explains:

They would give us facilities, machine, consulting resources and the early release code and direct access to the developers. As it turned out, it was an excellent opportunity for both of us because we would shake out a lot of bugs in their code while we were converting our system. So we did that—that took four months. —David, Manager of Business Information Systems

The order entry and management system, which was the last piece of the world wide system, was fully implemented at the end of 1994.

## 3.4. Technological infrastructure

Initially, when the mandate to eliminate the mainframe came from its European headquarters, Silicon Inc. chose the AS/400 mid-range computer as its computing platform. This was, primarily because it was viewed favourably by the Chief Finance Officer. In addition, the software package considered initially in 1989 was designed to run on an AS/400 computer. Subsequently, when David and his group determined that the software package was not suitable, the AS/400 was no longer the computing platform of choice. The MIMI package was evaluated and found to be an effective tool for the fixed capacity scheduling and planning required to support Silicon Inc.'s operations. Because MIMI was designed to operate in the UNIX operating system environment the choice of the computing platform to be selected was restricted to UNIX based computers. Specifically, the RS/600 RISC computers were selected. The RS/600 uses the AIX operating system which is IBM's version of the UNIX operating system. Its RISC architecture makes the RS/6000 an effective computer for intensive mathematical applications such as fixed capacity scheduling. It also serves as an effective communication bridge between AS/400 based applications and the older VAX computers still existing in some departments within the organization.

As at end of 1995 the worldwide system comprised several RS/600 application and database servers linked by a dual ring fibre distributed data interface (FDDI) metropolitan area network (MAN). This configuration supported an aggregate data rate of 200 Mbps between the servers. A few servers — primarily used for testing applications — were connected to the FDDI ring using Ethernet local area networks (LANs). Client stations were also connected to the servers on the FDDI ring using Ethernet LANs which support a data rate of 10 Mbps. One of the RS/600 computers on the FDDI ring functioned as a router to route traffic to and from the client stations and the appropriate servers. It also functioned as a terminal server to support traffic from VT100, VT 220 and IBM 3270 ASCII terminals.

As described earlier, Silicon Inc.'s worldwide system is a collection of client applications that obtain services from a collection of servers interconnected by a high speed network. The entire system may be viewed as comprising two sub-systems—the planning and scheduling system and the order entry management system. In the planning and scheduling system the primary application software is MIMI. The MIMI software is a client-server package. The server modules contain relevant data and provide mathematical modeling functions. The client modules are essentially the GUI front ends that function as the user interface to the system. The planning and scheduling system is supported by six RS/6000 servers:

1. One server contains the central specifications data in a relational database.

2. One server that contains the MIMI mathematical models used for central planning.

3. Two servers provide local shop-floor scheduling services for each of the manufacturing sites.

4. One server provides the chemical recipes used by each manufacturing site for growing silicon crystals of various specifications.

5. One server is used for testing new MIMI models.

The services of each of these servers is utilized by client MIMI applications. These clients utilize local recipe data and local scheduling services to develop work plans for each shop floor. Some of the client applications are specification queries from local sites which are supported by the database servers. MIMI client applications that perform central planning and scheduling utilize the services of the central specifications database server and the central planning applications server.

The main application software in order entry management system consists of the CICS/600 transaction control system and ENCINA—a product that provides enhanced transaction processing functions. These layers of software operate over the distributed computing environment software (DCE). DCE is a product that provides essential services in a distributed computing environment such as file services, directory services and security. These layers of software work co-operatively to enter, control and manage all aspects of transaction processing such as user authentication, order entry, data validation, transaction backout and recovery etc. The order entry management system consists of five RS/6000 servers.

1. One server functions as a terminal server to handle data entry and queries from terminals used by sales personnel, and also serves as a router to route traffic to and from other DCE clients and servers.

2. One server functions as the CICS server that provides the core transaction processing service.

3. One server functions as the database server that contains the transaction data.

4. One server provides the report writing function. These reports are generated in a batch mode.

5. One server provides data backup and archiving services.

This 1995/1996 architecture was developed gradually over a period of five years. Along the way numerous technical problems were encountered and addressed. The technical problems were primarily due to the newness and lack of maturity of the technology both for the vendor as well as for Silicon, Inc. For example, in the planning and scheduling system, the MIMI software was not originally designed to support multiple users. However, because there was no other comparable tool available David and his group had to modify MIMI to suit their needs. In the order entry system the CICS and ENCINA products had never been tested with realistic transaction loads. Thus, when it was initially tested at Silicon, Inc. the system proved to be inadequate. For example, when a transaction was aborted and backed out, the system would get bogged down for hours. As David described it:

we would put in a transaction that would do 20 000 I/O per logical unit of work and hit the rollback button and two days later it would come back... which we decided wasn't an acceptable response time (sarcastically).” Problems such as these were gradually ironed out with the close support and co-operation of the vendor. — David, Manager of Business Systems

Finally, on respondent accounts and on what we have seen of the technology in operation, what has emerged is a very open system with connectivity across the organization. Moreover it would appear to be a system designed to grow and evolve with the changing needs of Silicon, Inc.:

So if I want to characterize what this project was, more than anything else, it was an infrastructure building project. We built a world-wide infrastructure for data communications, client-server computing—and quite honestly, if someone came in tomorrow and said, hey guys, we are done with IBM, no more RS/6000, switch everything to ALPHAs - Great! give me a week; give me OSF1; buy the packages for that version—I'm done. We built an open architecture that allows us to plug the pieces in any way we want... we built this to be open, modularized so pieces could be swapped in and out. —David, Manager of Business Systems

## 4. Case analysis and discussion: client/server 'success' and emerging issues

The participants all agreed that the project was a financial and business success, although admitting they could not quantify accurately the outcomes. In this section we analyze the ‘success’ of the project from two perspectives: cost savings and better business decisions. We then carry out two further analyses. Firstly, seven critical enabling factors are distilled from the case material (see Table 2). The fact that these have been consistently cited in the extant IT project implementation literature for over a decade suggests that, from a management perspective, in many ways there is little that is new in how client/server implementation needs to be handled. However, secondly, we identified from the literature ten technical and managerial features of client/server environments considered distinctive, and rendering implementations more difficult than for previous technologies. Here each is investigated against the Silicon, Inc. experience, and an assessment made of the difficulties encountered and how they were handled.

## 4.1. Financial outcomes

The original acquisition request called for an investment of \$6 million for a two year project. The project took twice as long and —according to some participants—cost twice as much as originally estimated. (Others note that broadening the project scope accounts for the increased cost.) Despite this overrun, all participants agreed that it was a project that had to be done in order for the business to survive, and thus was worth the cost.

The most concrete financial justification for the project was moving off the mainframe. In terms of operating costs, the mainframe environment was costing \$1 200 000 a year. By end of 1995, Silicon, Inc. operated 15 RISC machines for only \$50 000 a month. These numbers, however, do not include the investment costs of development, training, or implementation. When Michael was asked about these other costs, he responded:

Yeah, but the biggest problem we had, we had gone into a mode that we knew we were going to discontinue support of the old software and old methodologies. So, yes, it's true we had to add bodies in to support the new applications, but had we decided to continue on with the old applications, we would have had to have as many bodies, if not more, to continue to support it on the old platforms using the old methodologies. We made a conscious decision early on, that if it wasn't true, that's what we were going to state to everybody. Any by and large, everybody bought it. It took us a long time to convince management that probably 85% of the project's cost is the maintenance after the fact. It's not the first bring-it-up-on-line, the computers, it's that fact that everybody wants to continue to tweak them. You had to be careful not to get too carried away with that. But by and large, the tweaks are beneficial. So, yeah, it's true you have to support it, you have to have facilities, people dedicated to it, but it's not going to run itself. You can't walk away from it, no matter what. So you are going to pay that burden. —Michael, Strategic Manager of Marketing

Table 2  
Silicon, Inc.: outcomes and critical enabling factors

<table><tr><td>Outcomes</td><td>Silicon, Inc. — critical enabling factors</td></tr><tr><td colspan="2">Financial</td></tr><tr><td>Cost up to $12 million — twice original estimate</td><td>1. Business process re-engineering drives technology choice</td></tr><tr><td>Operating costs reduced by $600 000 per year</td><td>2. Insourcing preferred</td></tr><tr><td>Most of the investment cost would have gone in maintaining/upgrading existing I.S. anyway</td><td>3. Vendor partnering — timing and type of relationship</td></tr><tr><td>&quot;Significant&quot; improvements in business process operations</td><td>4. Incremental implementation</td></tr><tr><td>Business</td><td>5. Senior level support and participation</td></tr><tr><td>Reduced response time to customer queries (weeks to hours)</td><td>6. Close user-IS professional relationships</td></tr><tr><td>Reduced manufacturing cycle time from 27 to 19 days</td><td>7. I.S. perceived as a business investment in a R&amp;D-type project rather than a cost centre</td></tr><tr><td>Reduced inventory from 60 000 to 20 000 wafers a day</td><td></td></tr><tr><td>Late changes to order by customer possible</td><td></td></tr><tr><td>High customer acceptance</td><td></td></tr><tr><td>Contributed to significant increased sales</td><td></td></tr></table>

Other participants readily admitted that they could not concretely quantify cost savings (other than reduced operating costs.) However, the improvements to the business processes have been so significant, participants were all confident the project was a financial success in the sense that the business would have severely suffered without it.

## 4.2. Business outcomes

All five of our respondents perceived that the project was a success because it:

\- reduced the response time to customer queries from several weeks to less than a few hours. (No participant estimated the worth of this benefit);

\- reduced manufacturing cycle times from 27 days to 19 days due to better planning. (No participant estimated the worth of this benefit);

\- reduced inventory from 60 000 wafers a day to 20 000 wafers a day. (Steven estimates this savings at \$200 000 a year in reduced inventory carrying costs);

In addition to processing new orders faster, Robert explained that the reduced cycle time also includes customers' requests to make changes to existing orders:

That [reduced cycle time to respond to customer queries] has been a big improvement in our relationships with our customers. They obviously want to know, "Can you deliver on time?" because the industry is tight on supply right now. And we also are better able to meet that date, which is obviously part II. And a lot of changes are always coming in. That's the other side of it. Nobody realizes that you take an order and sure you commit it to a date, now they call up two weeks later and say, "Hey we really need twice that much. We really need it two weeks earlier. Can you do it?" And that's where the new COMPASS system has enabled us to answer those questions quickly and accurately, which before was a total guess. On paper, there was no way to determine if indeed it could be done. We would guess and miss and we had a lot of unsatisfied customers. Right now we don't have everything $100\%$ on time, but given the market conditions and the tremendous demand, and the record production levels we a running right now, our on-time delivery is very respectable. The customers are understanding. And when we are going to miss, we will be able to communicate that to them ahead of time which is helping the situation. So that's probably our biggest business impacter. — Robert, Director of MIS

Michael and Robert capture the participants' reluctance to put a dollar value on these business benefits:

Many of our customers come back and say, “It’s almost phenomenal, the change.” There was a lot of frustration before because we took so long to commit. Things of that nature. How do you put a price tag on that? It’s almost impossible to set a price that you know that in a world where people are getting more and more used to things being instantaneous, the closer you are to instantaneous, the happier they are, the more likely they are happy to make orders with you. —Michael, Strategic Manager of Marketing

Its just one component of many that continues to increase sales. A resounding success. If success is measured by customer acceptance, they will all speak highly of it. Day and night they use it to do their job more accurately, more quickly, the cycle time issues. And also the benefit, the business benefit, it's hard to tell because a lot of things keep changing in this industry so you can't just say, "Okay we put that in and our sales went up 10%." You can't ever do that because at the same time you've brought on a new plant site. There are so many things happening. But I am very confident that system enabled us to stay on top of our growing situation. Being able to utilize our facilities more effectively than we would have otherwise.—Robert, Director of MIS

Although all of the respondents (all of whom played a vital role in the project) considered the project a resounding success, all admitted that senior management did not pay that much attention to the project's achievement. For example, Steven noted that they really did not understand the effort needed to implement the system. For him, senior management was glad that the software operated and that the recipes were correct, but they still did not perceive it as a considerable IS success. Other participants comment on senior management's perceptions:

Senior management is glad the project is over. They were glad we didn't kill the business. By and large, they are pleased. —Michael, Strategic Manager of Marketing

But when you try to explain exactly what technology went into this and what we really accomplished as compared to anybody else, or compared to another way of doing it, it's hard to get that across. And I sense that only in the way that they talk about the project. In some ways—as an omission—there isn't a lot of talk about the project. They say, “Oh you did a good job.” But not really a good feeling of why it is it was accomplished. They wouldn't necessarily come back I don't think and say, “You need to do more of that client/server” because there isn't an understanding of what it is and why we want to do it. — Robert, Director of MIS

When the participants were asked how senior management could give a luke-warm reception to the project given the business success, three answers were offered. John noted that the culture of Silicon, Inc. is to expect fantastic results, thus there are few ‘pats on the back’ for project successes of any kind. Robert noted that senior management was focused on other business initiatives, such as opening new manufacturing plants. David felt that senior management failed to understand the amount of work required to create a seamless transition:

They [senior management] see it as a success that it is over with. They are not as excited about it as we are, we being MIS. The main reason I would say that is because from a user standpoint, it was a non-event. Which is in my mind, part of the reason it's a success. There was a minimal perceived interruption to the business and the business flow as a result of this project. Yet it put in place an infrastructure that will allow us to move into the future. So, from my standpoint, it's a fantastic success. It will make my life much easier in the future. From management's perspective, it looks like a duck, it quacks like a duck. —David, Manager of Business Information Systems

## 4.3. Critical success factors

All participants agreed that the client/server project was successful, although the level of enthusiasm differed among stakeholders. Participants were asked to relate the critical success factors (CSF's) to the design, development, and implementation of the system. We have categorized their responses into seven CSFs. which will now be discussed.

## 4.3.1. Business process re-engineering drives technology choice

It's a business problem that we solved using this technology as opposed to the other way around. He thinks, from what he has seen, if you are installing C/S just to install

C/S, you are crazy, because there is a high learning curve to get over. With all the advances recently, the learning curve is not as high as it used to be, but we got into early. —Michael, Strategic Manager of Marketing

All the participants stressed that the world-wide systems project was a result of a business crises because Silicon Inc. could not service their customers. The project teams sought to redesign the business processes to reduce the time needed to place, change, and fill customer orders. The resulting system centralized order processing, central specification (the homogenizing of customer orders to standard units of measurement), and central planning (assigning orders to specific plants) while decentralizing the local recipes and schedules. As in 1996, we would probably call this project business process re-engineering, although that term was not common in 1989. But Robert notes that Silicon, Inc. has always looked at business processes before applying any automation:

We understand that there are processes to doing everything. And we always look to fix the process before we automate it. That is key. That is true of a lot of our IS projects. We’ve got to look at the process first then try to write a program around it because the process is usually what the problem is. As opposed to the software. Some companies go out and buy new software like SAP and they use it—they say they are putting new software in—but they are really putting it in to re-engineer the company to be more like what this software says you should be. That’s where the benefit comes. Quite frankly, I don’t think it’s the software as much as they get the organizational processes re-done in a more streamlined way. —Robert, Director of MIS

All participants stressed that the world-wide systems project actually evolved into a client/server solution. Thus, it was a tool to enable a change in business processes: It being a client/server project is an afterthought. It was not a direction. It just so happened that was the vehicle that we saw as the most economical, most expandable, and didn't lock us into a particular methodology. —Michael, Strategic Manager of Marketing

There was just a very obvious need for a new system for scheduling and planning. It started out...they were looking at the process and asked what it was they wanted to do. No preconceived notion about what system to use. I'm sure [David] has said this before because he and I feel really good about the way we ended up with client/server. That project never envisioned client server in the beginning. It was strictly a project to find a better automated way to do this process. This came from an obvious pain in the company. The customer was beating us up because we couldn't respond fast enough. So they started in with trying to find an artificial intelligence package. That was the first step. It happened to run on the RS6000 quite well so we got into RS6000. This was 4 years ago. And it was just by evaluating the need and trying to apply software solutions that it became more and more obvious that we were generating a C/S solution.— Robert, Director of MIS

## 4.3.2. Insourcing

Participants perceived that outsourcing vendors do not have the same motivation to make service users or to keep IS costs as internal IS employees. By insourcing, Silicon,

Inc.'s IS staff was more responsive to users because they understood the business consequences of their requests. Robert explains:

It's [manufacturing] a very difficult job. Anyone who hasn't been there, can't appreciate that. That 24 hour-a-day, 7 day-a-week demand to have the place produce. No matter what happens. I don't care if the power fails or it snows or we are running out of supplies. It's all the responsibility of manufacturing to get that done. If they have an IS group that is not supporting that, that is not responsive or doesn't sense the urgency that manufacturing always feels, and there is a big difference there. That's where a lot of the animosity I think comes from between IS and the rest of the company comes from. Many times the people in the IS group haven't sensed the urgency that the others are feeling. If the IS function doesn't perform in an urgent way, you obviously have bad feelings. —Robert, Director of MIS.

In a summary report to management, David cited insourcing as one of the major benefits of the client/server project because it reduced costs and increased service:

At [Silicon, Inc.] we determined that by bringing the application in-house and integrating it to the scheduling systems, we would reduce lead times and improve customer service. — David, Summary Report to Management

Moving off the mainframe was an economic advantage and a simplifier of our lives. We have one less vendor out there to worry about. And we've improved the reliability of that system. — Robert, Director of MIS

Although Silicon, Inc., did not outsource the development, implementation, or support of the client/server system, that did not preclude Silicon Inc. from accessing needed talent from external vendors. However, the subsequent success of these arrangements may be partly explained by these vendors being engaged in a form of partnering that resulted in complementary rather than conflicting goals (see Henderson, 1990; Willcocks, 1995).

## 4.3.3. Form of vendor partnering

All participants perceived the vendor partnership as a critical success factor: There is little doubt in our case (of) extremely close support on the part of the vendors. They were practically living here with us in many cases for quite a while. We had some of the top people with IBM working on the CRM side. And physically sitting in cubicles out here and working with the programmers. — Michael, Strategic Manager of Marketing

We were in a client partnership program. The deal was that if they got it going for us we would run around singing their praises. — John, Senior Analyst

I think that [the vendor] contributed heavily in the consulting role, not only giving us advice, but they sent in six people out here, three for a long period of time. A number of them showed up for weeks at a time to get us kicked off. We were having trouble with memory management. A number of things came up that they were good at responding to. Some of our other software vendors weren't quite as responsible after the fact that you own their software, they weren't willing to contribute. — Steven, Manufacturing Services Support Systems Supervisor

We actually helped them debug it and make it a viable product. That was a partnership unlike any I had really seen in the past years I've been in IS. They gave us support to make it happen. But of course, we were checking their product out which needed a lot of checking. So it goes two ways. — Robert, Director of MIS

The timing of the partnership was also key. Silicon, Inc. needed resources to migrate off the mainframe and the vendor needed a customer to help debug their new software. As of 1996, Silicon would not be able to duplicate that deal, although they would search for other opportunities to exploit complementary goals.

## 4.3.4. Incremental implementation

The project represented the single largest acquisition request for IS at Silicon. Given senior management's trepidation over IS expenditures, the project team had been anxious to implement pieces of the system as soon as a significant business function was complete. The major subsystems implemented were: scheduling (1991), central specifications (1991), central planning (1991), migrated 700 reports (1992), and order entry (1993–1994). Participants explained how this incremental approach led to project success:

Being able to have successes along the route and not necessarily everything is installed at once. This piece is installed and running and doing what's its supposed to. In this particular case, it allowed us to drop the charges by \$15 000 a month for the mainframe. In this particular case, we now give manufacturing better visibility as far as what the work load is going to be for the next 6 weeks which helps them figuring out overtime, figuring a way to avoid overtime. It can't be a sit back wait a year and a half and all of a sudden, boom, here it is. It has to be something that comes in pieces of discernible enough sizes that people can see it's there and working and doing what we want it to do. —Michael, Strategic Manager of Marketing

At least this wasn't a thing that waited until the third year before it was turned on. Along the way, benefits were starting to come out. And that helped the situation. It wasn't like they waited three years with a totally manual system.. Several steps, every 6 months, new features were being added. That's one of the advantages of client server approach. You keep adding new features, we added new servers. We kept this very fluid mix of boxes out there. We kept changing the arrangement because we kept seeing a benefit each time as we learned, we found better ways to do things. So I think the project allows you that kind of advantage. You turn things on gradually. You see benefits gradually. The customer likes that. They feel good right away. — Robert, Director of MIS

By 1995 the world-wide systems project had been going on for five years. Although the major components had been installed in 1991, new functionality has been constantly added to accommodate changes, such as new manufacturing plants and new technologies. Thus, all participants stated that the project still was not completed.

## 4.3.5. Senior-level support and participation

From the beginning, the world-wide systems project had at least one senior level manager in full support of the project. This support led to project funding, despite the ‘abstractness’ of the costs and benefits outlined on the acquisition request:

I think the answer is that it wasn't as defined as we would like it to be today when it started out. I tried to be complete in our direction, the tools, the hardware before we write an AR. We don't write some abstract thing and hope for the best. That one was a little like that, abstract and hope for the best. It was a very big project with a lot of dollars in that. It had the backing of people who were influential enough to get it through in spite of its abstractness. It's not typical of how we run projects today. But because of its abstractness, allowed us to experiment a bit on how we were going to get there. — Robert, Director of MIS

The European CFO drove the project at the beginning. His white paper outlining the future of IS called for a migration off the mainframe to smaller platforms (although he did not specify client/server), integrated manufacturing and financial systems, and a worldwide telecommunications infrastructure served as the initial vision of the project. To ensure that this vision would be realized, Michael, a high-level business manager was put in charge of the project. The other participants credited his political ability as a critical success factor. David, for example, explained how Michael competently traversed through Silicon, Inc.'s matrix organization:

The credit really goes to [Michael] in my mind and the CFO. They drove it. They made it work. [Manufacturing] group were on the sidelines, dragged in kicking and screaming. What made a difference—our organization is like this, a mess, and it still is...it's democratic. Getting consensus can be difficult. We didn't always get consensus throughout the project. But what allowed us to be successful was the fact that [Michael] knew how to navigate the matrix organization. He pulled in the right people at the right time to get decisions made. —David, Manager of Business Information Systems

## 4.3.6. Close user-IS relationships

In addition to high-level support and involvement, close user–IS partnering was also cited as a critical success factor. Project teams required full time commitments from both groups. Users and IS team members ‘worked in the same bull pens’, as one respondent described it, so their close physical proximity promoted constant communication. Participants explained:

I think the people that were involved that had worked together for a good period of time. They had an appreciation for each others skills. They weren't ashamed to say, "I don't know this answer but we can talk to this guy..." We really understood each well enough that we could rely on each other's strengths. [David] is a very good resource. You can't top his IS knowledge and the things he can come up with. He is very creative. I consider myself a very good resource from the manufacturing side. I had some management skills. I ran the modification building here for some period of time. Things of that nature. With all of here together as a team, it caused it to be a success. — Steven, Manufacturing Services Support Systems Supervisor

I come back to team work a lot. This company is built is not built on isolated units. We are very much working together as teams. There is no IS project that doesn't have users right on the project team. So it was two ways. We certainly had an outstanding IS group on this group, including the contract people. — Robert, Director of MIS

In my opinion, we could not have pulled this project off by having MIS sit in one area and have the users sit in another area. Physically we were only 20 or 30 feet apart. Literally, the programmers were sitting by the schedulers, next to the people who write the plan orders, the people who deal with the commercial issues. If there hadn't been that close coupling, that would have lead to frustration. It would have led to more false starts. We have a pretty active users group. Basically, the way we try to structure it, as we start tackling different segments, there was involvement from people who did the work, who were going to do the work in the future. One of the people who now maintains part of the system was a plant operator. She's been taught how to use SQL rules, how to use expert systems, things of that nature. There has been real imparting of knowledge to the users and soaking up that knowledge. I think if it had been done in a vacuum, it would have never happened. There had been too many frustrations/fights/battles and the users would not have been able to see that progress was being made. Having them be able to report back to their supervisors and saying, “Yeah, it's moving forward, it's getting there.” I think that was a critical factor. —Michael, Strategic Manager of Marketing.

## 4.3.7. IS seen as a business investment, not just a cost centre

These six critical success factors suggest that Silicon's client/server project possessed many of the characteristics of other large-scale IT implementations (Willcocks and Griffiths, 1994). However, Silicon, Inc., also shares another common characteristic in that it was considerably over-budget and over-due (Saarinen and Vepsalainen, 1993; Willcocks and Griffiths, 1994). Although this can hardly be cited as a critical success factor, the enabling feature in the Silicon, Inc. case was the willingness of business and technical management at senior and operational levels to continue to invest resources, time and effort beyond original estimates into what turned out to be, de facto, a research and development project with considerable significance for the organization's short and long term business performance. While IT expenditures were always subject to budgeting reviews at Silicon Inc., some sense of senior management's changing perception of IT as an investment, rather than merely a cost to be minimised is revealed by the following comments:

IS is seen as an enabler of transformation. We are a valued competency that enables this business to succeed... I think we have a real benefit (in Silicon, Inc.) in that we do have a lot of people who do recognise that. That comes about in the sense of us getting approvals. And being given the OK to try new things and technologies, which do cost money and do have some risk. — Robert, Director of MIS.

It was paid for by the Chief Financial officer but..the chairman of the Board of our parent company... he really was the sponsor. He was the one pushing it... they wanted us to get into a midrange system. It was really more an edict from the top than a push from the bottom. — David, Manager of Business Information Systems.

Table 3
Distinctive client/server issues and Silicon, Inc.

<table><tr><td>Client/server issues</td><td colspan="8">Silicon, Inc. experience</td></tr><tr><td rowspan="2">Technical</td><td colspan="3">Factor present</td><td colspan="4">Level of difficulty incurred</td><td rowspan="2">Remarks</td></tr><tr><td>Minor</td><td>Major</td><td>n/a</td><td>Negligible</td><td>Some</td><td>Considerable</td><td>Project threatening</td></tr><tr><td>● Involves distinctively different and organizationally new set of technologies</td><td></td><td>*</td><td></td><td></td><td></td><td>*</td><td></td><td>Skills shortages. Managed as R&amp;D project</td></tr><tr><td>● Not one technology: complex integration/testing problems</td><td></td><td>*</td><td></td><td></td><td>*</td><td></td><td></td><td>Vendor partnering and close user-IS relationships in systems development</td></tr><tr><td>● Hardware/software compatibility issues</td><td></td><td>*</td><td></td><td></td><td>*</td><td></td><td></td><td>Strong supplier relations and restricted choices made</td></tr><tr><td>● Sizing, configuration and capacity issues</td><td></td><td>*</td><td></td><td></td><td></td><td>*</td><td></td><td>Present but not experienced as technically difficult</td></tr><tr><td>● Centralization/decentralization debate creates short/long term technical issues</td><td>*</td><td></td><td></td><td></td><td>*</td><td></td><td></td><td>Managed incrementally</td></tr><tr><td>● Main pay-offs from enterprise-wide technical planning</td><td>*</td><td>*</td><td></td><td></td><td>*</td><td></td><td></td><td>Grow into this type of planning</td></tr><tr><td>Managerial</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>● Creates lack of clarity about responsibilities of business users, roles, skills</td><td></td><td>*</td><td></td><td></td><td>*</td><td></td><td></td><td>Incremental implementation enabled adjustments</td></tr><tr><td>● Not one technology: everyone has to know something new</td><td></td><td>*</td><td></td><td></td><td></td><td>*</td><td></td><td>Run as a learning project</td></tr><tr><td>● Usually introduced as part of wider organization change</td><td></td><td>*</td><td></td><td></td><td>*</td><td></td><td></td><td>Managed as a re-engineering project</td></tr><tr><td>● Requires matrix management and new approaches tomanaging problems</td><td></td><td>*</td><td></td><td></td><td>*</td><td></td><td></td><td>Existing matrix management redeployed</td></tr></table>

## 4.4. Client/server: distinctive implementation issues?

These all too familiar critical enablers suggest that there will be little difference between the implementation experiences of client/server and those on any relatively large new information technology based project, at least in a relatively large complex organization like Silicon, Inc. However, one final comparison will be made. Table 3 shows the major technical and managerial difficulties that feature regularly in the literature as distinctive to client/server implementations as opposed to other organizationally-used IT-based technologies. Here we compare these against Silicon Inc.'s own client/server experiences.

## 4.4.1. Technical issues

We reviewed published case studies, survey research and the prescriptive literature on client/server implementation. These sources suggest a number of distinctive technical issues.

\- Client/server represents a distinctively different and organizationally new set of technologies (Friend, 1995; King, 1994; Muller, 1994; Orfali et al., 1994).

\- Client/server is not one technology but several. The resulting complexity raises distinctive — and more problematical — integration and testing issues. These are made worse by lack of appropriate client/server development methodologies and generally accepted standards in networking (Bochenski, 1994; Friend, 1995; Levis and von Schilling, 1994; Renaud, 1993).

\- Relatedly, client/server presents a range of distinctive hardware/software compatibility issues (Forrester Research, 1995; Mill, 1994).

\- Sizing, configuration and capacity planning become more difficult with client/server (Collins, 1996).

\- Lack of mature products and tools to support a diverse and complex client/server computing environment (Forrester Research, 1995; Levis and von Schilling, 1994).

\- Client/server invariably intervenes in a dynamic IT centralization–decentralization debate and can confuse rather than clarify the technical directions and options (Mill, 1994; Ross, 1995; Tayntor, 1994).

\- More than other technologies, client/server requires an enterprise-wide technical planning and management (Forrester Research, 1995; Kole et al., 1995).

In reviewing the case documentation and interview transcriptions, it was clear that all these technical issues were present in the client/server implementation at Silicon, Inc.. However, even if distinctive of client/server environments, on our analysis none of these factors emerged as particularly critical barriers to the Silicon, Inc. implementation (see Table 2 — the ratings represent our own view derived from respondent opinion). One key to success was accepting early on that the organization had low 'technology maturity' (Feeny et al., 1996). For Silicon, Inc., client/server was relatively new and unstable in specification and application, and in the first two years there was relatively little relevant in-house technical experience. This implied the need for insourcing and the taking of a 'user' focus, that is using multi-functional teams rather than leaving development to technical specialists. It also meant that external vendors needed to be used on a buy-in or close partnering rather than on a strict contractual basis (Feeny et al., 1996; Lacity et al., 1995). All these approaches were in fact adopted effectively at Silicon, Inc., but represent prescriptions applicable to any new systems development, rather than exclusive to client/server environments. Some flavour of the approach is suggested by the following, but note that the technical rather than the organizational issues of implementation are downplayed by the respondent:

We had no choice but to use in-house people because they understood the business logic. The technical skills required (were) minor to the understanding of the business logic. Training the staff on a new paradigm was at times difficult especially when they were getting stuck in their old roles. We had to isolate them from their old roles and immerse them in the new technology. Eventually, everyone made the transition. — David, Manager, Business Information Services.

What was interesting in the Silicon, Inc. case was that as far as IT was concerned the technology was both centralizing and decentralizing, and yet the enterprise-wide technical planning and management approach stressed as necessary and distinctive for client/server implementations by many sources developed gradually rather than being present at the beginning:

The customer was beating us up because we could not respond fast enough. So we started in with trying to find an artificial intelligence package. .. The key point is that nowhere did we say 'we are doing client/server'. It was more like after we were into it, this tool seemed to fit our need, then we woke up to the fact that this was client/server. And I say this over and over because I think this is the right way to enter into client/server. Now today, we obviously know more about it, you will think C/S more quickly than you did four years ago. — Robert, Director, MIS.

This was not a technology looking for a problem, this was a solution that used a technology. It's a business problem we solved... if you are installing C/S just to install C/S you are crazy, because there is a high learning curve to get over. — Michael, the Strategic Manager of Marketing.

Clearly during the 1989–1995 period there had been so much learning due to the partnering arrangements the in-house approach and close user-IS relationships that any distinctive technical difficulties had been largely surmounted: the outstanding issue remained the perennial one for all IT functions, namely cost containment:

The concept of fully integrating the company world-wide so that we are managing all our resources, all our inventories and that we can produce on the spot demand — all that requires very integrated systems. To do all that and accomplish that within the budget constraints is my biggest challenge. I don’t feel a great challenge to keep up with technology. I have an organization, I believe, that is very capable of being on that leading edge of technology. But applying that cost effectively to our company is the challenge. — Robert, Director, MIS.

## 4.4.2. Managerial difficulties

Published sources also suggest a range of managerial issues distinctive to client/server implementation.

\- Creates lack of clarity about the responsibility of business users, their roles and the new skills needed (Forrester Research, 1995; Levis and von Schilling, 1994).

\- Not one technology, therefore everyone has to learn something new. For example problem and change management must be conducted differently with more interest groups involved than before (Renaud, 1993; Ross, 1995).

\- Usually introduced when the organization is itself centralizing or decentralizing, the background of organizational change exacerbates the technology management issues. Alternatively the organization traditional structure and culture creates barriers to moves to a distributed technical environment (King, 1994; Levis and von Schilling, 1994; Renaud, 1993; Tayntor, 1994; Tebbutt, 1996).

\- Requires matrix management involving many parties and new approaches to managing problems (Levis and von Schilling, 1994).

Again, while all these barriers can be easily read into the case, what is interesting is how none really emerged as critical obstacles. The reasons for this, at least for the first three points, would seem to lie with the critical success factors delineated from our review of documents and the interview transcripts (see above). In particular, these seemed to lead to an overarching emergent approach that mitigated risk while promoting widespread organization-wide learning:

We went from low risk to high risk and learned along the way. Learned a lot along the way.— David, Manager, Business Information Services.

However, on the fourth point, Silicon Inc. management clearly recognised the distinctive implications of client/server for how implementations should be pursued:

Getting consensus can be difficult.... what allowed us to be successful was the fact that (Steven) knew how to navigate the matrix organization. He pulled in the right people at the right time to get the decisions made. There was a lot of this matrix organization (that) made it possible to get access to the right people to get things done. Because so many people work for so many other people you have to build the right strategic alliances to the right parts of the matrix. You have to pull the matrix however you want to pull it. But that's something that helped.— David, Manager, Business Information Services.

In this case the pre-existing matrix organization was an important enabler, but could have been a major obstacle if there had not been managers actively utilizing it to pursue client/server project objectives.

## 5. Discussion and conclusion

The critical success factors associated with Silicon's client/server application were mostly little different from the managerial lessons derived from studies of other new

IT-based projects. Once applied these enabled most of the technical and managerial barriers usually cited as distinctive to client/server to be handled without any becoming major obstacles. Additionally, there was at Silicon, Inc. a wide acceptance of three factors that made for effective implementation: that there was relatively low technology maturity as far as client/server was concerned; that the project was closer to research and development; and that the degree of organization-wide learning over the course of the project would be fundamental to the level of success achieved.

Certainly, the plethora of IT research has demonstrated the need for top management support, the need for IT to be perceived as an investment rather than as merely a cost centre, redesigning business processes before implementing IT, building in-house capability, accessing vendor resources, user participation on development teams, and phased implementation strategies to reduce risk. We also see many of the same problems surfacing, such as IT projects late and over-budget, primarily caused by similar problems: failing to freeze user specifications and underestimating the costs of training, support, and maintenance. In this sense, we can see that Silicon's case is representative of many large scale IT projects.

## 5.1. Business process—re-engineering drives technology choice

Ever since the seminal book, Re-engineering the Corporation (Hammer and Champy, 1993), practitioners have been told, 'don't automate, obliterate.' Their message is simple: improve the business process before implementing IT solutions. However, their methods call for radical change: "It is about beginning again with a clean sheet of paper...marginal improvement is no improvement at all but a detriment." Although these authors argue for radical change, research has suggested that practitioners opt for a more moderate approach to BPR, one of gradual process improvements, rather than obliterating the past (Willcocks, 1996a; Willcocks and Currie, 1995). However, Silicon's BPR project can better be characterized as a process improvement rather than radical re-design. Silicon, Inc. still went through the same process of order-entry-central specification-central planning-local specification-local planning. The process improvements comprised integrating information for faster customer response. Thus, although participants used the rhetoric of 'BPR driving technology', a better description may be 'process improvement before automation.'

## 5.2. Insourcing the development of new technology

The sourcing strategy for client/server implementations was seen as a critical success factor by participants—how could they acquire the skills necessary to build and support this new technology? Many companies are opting to outsource the development of client/server applications rather than build in-house capabilities. For example, First National Bank of Chicago has signed a 7 year, multi-million dollar contract with CSC to install SAP on client/server platform (Grace, 1995). Holiday Inn announced a partnership with IBM to build and install client/server based reservation systems in 1900 hotels by mid-1997 (Wagner, 1995b). Silicon, Inc. rejected outsourcing the project because of they felt that internal IT staff had the necessary business expertise, although they wished to access vendors' technical expertise.

## 5.3. Unique vendor partnership

In recent years, there has been much research on strategic partnering with IT vendors. In many cases, the rhetoric of ‘strategic partners’ is used to describe many client/vendor relationships, although closer scrutiny fails to reveal how many such contracts are ‘strategic’ (Willcocks, 1995). Silicon, however, is an exemplar for a strategic partnership because the contract truly defined ‘complementary goals’. Silicon received resources and talent in exchange for debugging the vendor’s new product. Although Silicon participants stressed that such an opportunity is unique, the lesson to search for complementary goals holds (Lacity et al., 1995)

## 5.4. Incremental implementation

Incremental implementation is the phased delivery of a system. The benefits of incremental implementation include verifying user requirements, verifying system design, capitalize on learning, demonstrating value to secure management approval for full-scale implementation, or gaining user acceptance of the system (Janson and Smith, 1985; Naumann and Jenkins, 1982). We saw evidence that Silicon, Inc.'s incremental implementation served to keep senior managers and users interested in the project as well as to make adjustments as learning occurred. In a more profound sense, implementation was not merely incremental; for the early years the end destination was unknown and unplanned, therefore the implementation path was incremental. Respondents communicated to us (see quotes above) a strong sense of the principle of bricolage operating throughout this client/server development and implementation (Ciborra (1993).

## 5.5. Senior level support

IT research has found that top management ‘support’ is one of the most vital critical success factors in the successful implementation of IT. IT researchers have distinguished four theoretical constructs comprising senior management’s attitudes and behaviours towards IT.

1. Project Champion: “Champions are managers who actively and vigorously promote their personal vision for using IT, pushing the project over or around approval and implementation hurdles. They often risk their reputations in order to ensure the innovation’s success” (Beath, 1991, p. 355).

2. Project Sponsor: “Sponsors have the funds and authority to accomplish their goals” (Beath, 1991, p. 355) (a less active and less enthusiastic role compared to a champion).

3. Senior Management Participation: “activities or substantive personal interventions in the management of IT” (Jarvenpaa and Ives, 1991, p. 206) (active behaviours).

4. Senior Management Involvement: “the psychological state...reflecting the degree of importance placed on IT” (Jarvenpaa and Ives, 1991, p. 206) (moral support).

At Silicon, the CFO and chairman of the Board served as project sponsors, while Michael served as its champion throughout the project. The roles were kept separate, a condition for success emerging from the work of Edwards (1996). Through their efforts, other senior managers came to support and participate on the project as needed during the development.

## 5.6. Close user-IS partnering

IT research has demonstrated that close user–IT partnering is a critical success factor. For example, Mumford (1981) describes three types of user roles on project development teams.

1. Consultative: users are consulted about what they want, but decision-making is done by another group, typically IT.

2. Representative: a group of users is elected to represent the needs of their co-workers in the design process.

3. Consensus: users not only make decisions, but assume full responsibly for the success of the project.

Others have pointed to the significance of close user–IS partnering to project success, and the different ways in which it can be achieved (see, for example, Hirschheim, 1985; Taylor-Cummings and Feeny, 1997; Skyrme, 1996). At Silicon, Inc., lower level users served as representatives on the project team and higher level users accepted responsibility for the success of the project.

Some more detailed factors can be distilled out of this analysis. 'Senior management support' and 'close user–IS partnering' would seem to have set the context for the development of shared values and sustained commitment to the project at many levels — 'soft' factors identified as keys to success in other studies of IT projects (Land, 1992; Land et al., 1992; Taylor-Cummings and Feeny, 1997).

Our own analysis (supported by many of the respondents' quotes above) also suggests an a priori intuitively correct but understudied conclusion: that having highly capable key personnel (including supplier staff) with the right skills working on the project for a sustained period also greatly influenced levels of success. A similar conclusion can be read into other studies, including those in the IS risk and failures literature (as examples only — Beath, 1991; Currie and Willcocks, 1996; Feeny and Willcocks, 1997; Griffiths and Newman, 1996; Lyytinen and Hirschheim, 1987; Sauer, 1993). To take the obvious examples: in the case of Robert, Director of MIS, he shared many of the background, orientations and qualities identified as typical for effective CIOs (Feeny et al., 1997). David, manager of business information systems, had high IS knowledge and 'doing' capability, creativity and at the same time the ability to work closely with users and suppliers on business applications — characteristics combining 'relationship building' and 'technical fixing' capabilities (Feeny and Willcocks, 1997), and elements of the hybrid manager (Skyrme, 1996). Michael, in effect project champion and manager in charge of the project, met many of the criteria for success suggested by other studies (Beath, 1991; Feeny and Willcocks, 1997). He was organizationally credible with IT and business personnel, sufficiently senior, process oriented, had some experience with IT, and an understanding of how the organization worked and how its people could be influenced. Reviewing the research material, it is also clear that the project teams were continuously staffed by high performers from both IT and the business — again an obvious, but frequently under-researched factor in project success/failure (but see Feeny, Abl et al., 1997)

## 5.7. IS perceived as a business investment

As of 1989, IT was largely perceived as a cost centre. However the client/server project itself came to have two drivers: not just to reduce mainframe costs, but also, more primarily, to achieve a significant business objective. Clearly, some senior managers were influential in supporting the client/server development through considerable cost rises. As the project progressed it became increasingly recognised organizationally that it was a strategic project linked intimately with business direction and operational performance. This wider recognition of the business value of IT as an investment is frequently cited in the literature as a fundamental reason why strategic projects come to be proposed endorsed and supported, despite very often fairly unclear financial cost and benefits, as in the Silicon, Inc. case (see, for example, Earl and Feeny, 1994; Grindley, 1995; Keen, 1991; Parker et al., 1989).

## 5.8. Anticipated versus actual costs

At the same time, Silicon, Inc.'s project was not immune from many of the problems encountered on traditional IT projects. This was particularly the case on cost. One aspect of this was the project itself costing as much as twice the original estimates. A further aspect is how far client/server actually saves money directly. When client/server technology was first sold by vendors, it was largely paraded as a cost saver. Thus it was widely suggested that companies could invest in the technology for about \$100 000 compared to a multi-million dollar mainframe, and that the price performance curves were about 30% improvement per year compared with 20% for mainframe improvement. These arguments were used to rationalize the investment in client/server at Silicon, Inc.—the most concrete financial justification for the project was moving off the mainframe. In terms of operating costs, the mainframe environment was costing up to \$1 200 000 a year. By late 1995 Silicon, Inc. operated 15 RISC machines for only \$50 000 a month. These numbers, however, included only the hardware and software investment and neglected the costs of learning the technology, maintenance, and support. These of course could be considerable. Thus International Data Corporation estimated that companies spent more than \$800 million on client–server training out of a total training market of \$6.6 billion. Another study by Forrester Research estimated that “for a little over \$500 000 over a period of one to two years, an organization can get 20 developers 100% trained in client/server technologies” (Lipp, 1996, p. 58).

Aside from these points, there is still a question mark over whether client/server itself can save on organizational costs. In the Silicon, Inc. case, the direct financial impact could not be clearly ascertained; as in other organizations, there are probably a series of IT-related costs that are hidden, and not easily identified as relating to the costs of client/server operations (Willcocks, 1996b). What is perhaps more impressive is the widespread recognition amongst respondents of considerable business gains that would impact on Silicon, Inc. profitability and revenues even if the contribution of client/server to this could not be isolated let alone quantified. This adds a further dimension to the rather mixed picture emerging from other studies on cost savings and business gains emerging from client/server implementations (see, for example, Kole et al., 1995; Simpson, 1995).

Some general points can be added to this discussion. A range of critical success factors have been identified in this strategic IT project. An interesting speculation is: of these factors, which would need to be absent for the project to have turned into a failure? In reviewing all the case materials our own answer would relate fundamentally to processes, relationships and skills. On a large-scale, new technology, fundamentally R.&D., project such as this, lack of close working relations between the IT, business and supplier personnel at all levels combined with low/medium, or incorrectly distributed, business, IT and management, including 'big' project management, skills would, in our estimation, have caused massive difficulties. But this is not to say that the other factors are not critical. Nor is it to play down the role of luck and serendipity in all multi-year major projects. It is the combination of the critical factors, albeit some consciously planned but with flexibility, uncertainty, learning and happen stance built in and allowed for, and the end-point undecided but grown towards, that explain the success at Silicon, Inc., together with the fact that key personnel actively shaped the general direction and principles of operating as events unfurled and needs emerged. In attempting to make sense of a high risk major IT project, as for history, it is always wise to maintain a sense that things could have been otherwise. As one speculation, it may well be that IS case research methodology can learn from recent developments in counterfactual history (Ferguson, 1997), and also Lewis Namier's comment that: “the enduring achievement of historical study is a historical sense — an intuitive sense — of how things do not happen”.

Finally, it is useful to indicate some limitations of this research and some possible future directions. Clearly, research into one case study acknowledged as a success could be counterbalanced by further work looking at those considered failures. A wider, multiple case study approach taking into account a variety of sizes of project and outcomes could also produce some rich comparison, and, indeed this is the direction of our own future research in this area. Furthermore one would welcome more detailed work on the degree to which client/server has distinctive characteristics that make its implementation more, or less difficult, to achieve. Our research here is detailed in many places, suggestive in some others, but as yet there are all too few in-depth studies that investigate this potentially very rich, and useful, direction.

## Appendix A. The client/server paradigm

Client/server computing may be appropriately described as a paradigm of computing characterized by distribution of processing power among a network of processors. More important, the distribution is made to ensure ‘division of labour’ among the processors with each processor specializing in providing certain functions. End user applications (clients) utilize the services provided by these processors (servers) in order to accomplish their purpose. This co-operative sharing of work among clients and servers is the essence of the client/server computing paradigm (Bachteal and Read, 1995).

In order to distribute functions across the network, tasks must be partitioned into discrete functions. There are numerous ways in which the partitioning of tasks may be accomplished. Thus client/server systems can be designed and implemented in various forms depending on the manner in which the tasks are partitioned. The Gartner Group developed a model that has been frequently used to describe a range of client/server systems (see Fig. 1).

Gartner's Classical Five Styles of Cooperative Processing...
This most widely used model for client/server computing strongly associates the logical and physical relationships between components.  
![](/api/attachments/438STX7D/fulltext/images/ba2e6d69451ea8298673e9782e702772880d87d72b38113c71105c9b38257d6b.jpg)  
Fig. 1. The client/server paradigm

The model essentially views computing tasks as belonging to one of three logical categories—data management, application logic (or business rules) and presentation management. The ‘data management’ component comprises database related activities such as storage and retrieval of data. The ‘application logic’ or business rules component represents the processing performed on the data to yield the required results. The ‘presentation management’ component is the user interface to the system. The model describes five different implementations of this three tier architecture. Each implementation distributes different components across the network. Thus, for instance, one implementation could have the presentation manager in a client computer and the application and data on a network server. Another implementation could distribute the application and presentation to the client computer, and the database to a network server. Thus, client/server systems form a continuum, ranging from systems where the client application merely functions as a presentation manager, typically implemented with a user friendly graphical user interface (GUI) as a front end to traditional mainframe based systems, to those systems which optimally distribute processing responsibilities between client applications and servers. The Gartner group estimates that 90% of client/server systems developed today are of the first type where the presentation component is in the client machine and the data and application are in the server. This is very similar to the architecture of mainframe based systems.

## References

Allen, L., 1995. Client/server q&a Mortgage Banking, 56 (2): 95–96.

Bachteal, P., and Read, J., 1995. Client/server solutions. CA Magazine, 128 (9): 41–43.

Beath, C., 1991. Supporting the information technology champion. MIS Quarterly, 15 (3): 355–373.

Benbasat, I., Goldstein, D. and Mead, M., 1987. The case research strategy in studies of information systems. MIS Quarterly, September: 368–386.

Bochenski, B., 1994. Implementing Production-Quality Client/Server Systems. Wiley, Chichester.

Ciborra, C., 1993. Teams Markets and Systems. Cambridge University Press, Cambridge.

Collins, T., 1996. NWW backtracks on £235 m. project. Computer Weekly, March 7th: 1, 4.

ComputerWeekly, 1996. Client/server Report And Directory. Interactive Information Services, London.

Currie, W. and Willcocks, L., 1996. The new branch Columbus project at the Royal Bank of Scotland: the implementation of large-scale business process re-engineering. Journal of Strategic Information Systems, 5:3, September.

Earl, M. and Feeny, D., 1994. Is your CIO adding value? Sloan Management Review, 35 (3): 11–20.

Edwards, B., 1996. The project sponsor. In Earl, M. (ed.). Information Management: the organizational dimension. Oxford University Press, Oxford.

Eisenhardt, K., 1989. Building theories from case study research. Academy Of Management Review, 14 (4): 532–550.

Feeny, D., Abl, V., Millie, E., et al., 1997. Defining new skills and competencies. Oxford Institute of Information Management Research And Discussion Paper. Templeton College, Oxford (forthcoming).

Feeny, D., Earl, M. and Edwards, B., 1996. Organizational arrangements for IS: the role of users and specialists. In: M. Earl (ed.). Information Management: the organizational dimension. Oxford University Press, Oxford. Ferguson, N. (ed.), 1997. Virtual History: alternatives and counterfactuals. Picador, London.

Feeny, D., Edwards, B. and Simpson, K., 1997. Understanding the CEO/CIO relationship. In: L. Willcocks, D. Feeny and G. Islei (eds.), Managing IT As A Strategic Resource. McGraw Hill, Maidenhead.

Feeny, D. and Willcocks, L., 1997. The IT function: changing capabilities and skills. In: L. Willcocks, D. Feeny and G. Islei (eds.), Managing IT As A Strategic Resource. McGraw Hill, Maidenhead.

Forrester Research, 1995. Managing Client/Server. Forrester Research, Boston, MA.

Friend, D., 1995. Client/server versus cooperative processing. In: R. Umbaugh (ed.). Handbook Of IS Management. Auerbach Publications, New York.

Gerber, C., 1995. Client/server price tag: 40% of IS dollars, Computerworld, 29 (45): 6, 7.

Green-Armytage, J., 1995. Client/server wins over majority of management. Tate Bramhalad Survey reported in Computer Weekly, October 12th., 22.

Griffiths, C. and Newman, M., (eds.) 1996. Theme issue: risk in information systems projects. Journal of Information Technology, 11: 4.

Grindley, K., 1995. Managing IT At Board Level. Pitman Publishing, London.

Hammer, M., and Champy, J., 1993. Re-engineering the Corporation: a manifesto for business revolution. Nicholas Brearley Publishing, London.

Henderson, J., 1990. Plugging into strategic partnerships: the critical IS connection. Sloan Management Review, Spring: 7–18.

Hirschheim, R., 1985. User experience with and assessment of participative systems design. MIS Quarterly, 9 (4):295–304.

Janson, M., and Smith, D., 1985. Prototyping for systems development: a critical appraisal. MIS Quarterly, 9 (4):305–316.

Jarvenpaa, S., and Ives, B., 1991. Executive involvement and participation in the management of information technology. MIS, Quarterly, 15 (2): 205–227.

Kaplan and Duchon, 1988.

Keen, P., 1991. Shaping The Future. Harvard Business Press, Boston, MA.

King, W., 1994. Creating a client/server strategy. Information Systems Management, Summer: 71–74.

Kole, A., Roukas, G., and Tate, P., 1995. The Real Costs of Client/Server Computing, Technology Managers Forum International, New York, October.

Lacity, M. and Jansons, M., 1994. Understanding qualitative data: a framework of text analysis methods. Journal Of Management Information Systems, Spring: 95–112.

Lacity, M., Willcocks, L., and Feeny, D., 1995. Information technology outsourcing: maximizing flexibility and control. Harvard Business Review, May–June: 84–93.

Land, F., 1992. The management of change: guidelines for the successful implementation of information systems. In Brown A., (ed.) Creating A Business-based IT Strategy. Chapman and Hall, London.

Land, F., Le Quesne, P., and Wijegunaratne, I., 1992. Technology transfer: organisational factors affecting implementation — some preliminary findings. In: J. Cotterman and J. Senn (eds.), Challenges And Strategies in Systems Development. Wiley, Chichester.

Lee, A., 1989. A scientific methodology for MIS case studies. MIS Quarterly, March: 32-50.

Levis, J. and von Schilling, P., 1994. Lessons from three implementations: knocking down barriers to client/server. Information Systems Management, Summer: 15–22.

Lipp, J., 1996. Building skills for client/server. Business Communications Review, 25 (11): 57–59.

Lyons, D., 1995. Controlling client/server process. InfoWorld, 17 (49): 73.

Lyytinen, K. and Hirschheim, R., 1987. Information system failures — a survey and classification of the empirical literature. In: P. Zorkockzy (ed.). Oxford Surveys in Information Technology, Oxford University Press, Oxford.

Markus, 1983.

Mill, J., 1994. The trouble with client/server. Computer Weekly, October 13th: 32–33.

Muller, N., 1994. Applications development tools: client/server, OOP and CASE. Information Systems Management, Summer: 23–27.

Mumford, E., 1981. Participative systems design: structure and method. Systems, Objectives, Solutions, 1 (1): 5–19.

Naumann, J., and Jenkins, A., 1982. Prototyping: the new paradigm for systems development. MIS Quarterly, 6(3): 29–44.

Orfali, R., Harkey, D. and Edwards, J., 1994. Essential Client/Server Survival Guide. John Wiley, New York.

Parker, M., Trainor, E. and Benson, R., 1989. Information Strategy And Economics. Prentice Hall, Englewood Cliffs, NJ.

Pontin, J., 1995. Client/server adoption stalls, study finds. Inforworld, 17 (46): 13, 34.

Renaud, P., 1993. Introduction To Client/Server Systems — a practical guide for systems professionals. Wiley, Chichester.

Ross, R., 1995. Shifting to distributed computing. In Umbaugh, R. (ed.). Handbook Of IS Management. Auerbach Publications, New York.

Saarinen, T. and Vepsalainen, A., 1993. Managing the risks of Information systems implementation. European Journal of Information Systems, 2 (4): 283–295.

Sauer, C., 1993. Why Information Systems Fail. McGraw Hill, Maidenhead.

Simpson, D., 1995. Cut costs with client/server computing? Here's how. Datamation, October 1st: 38–41.

Skyrme, D., 1996. The hybrid manager. In Earl, M. (ed.). Information Management: the organizational dimension. Oxford University Press, Oxford.

Smith, C., 1990. The case study: a useful research method for information management. Journal of Information Technology, 5 (2): 123–133.

Taylor-Cummings, A. and Feeny, D., 1997. The development and implementation of systems: bridging the user-IS gap. In: L. Willcocks, D. Feeny and G. Islei (eds.), Managing IT As A Strategic Resource. McGraw Hill, Maidenhead.

Tayntor, C., 1994. New challenges or the end of EUC? Information Systems Management, Summer: 86–88.

Tebbutt, D., 1996. IT to the rescue: the thin blue line. Computer Weekly, February 29th: 33.

Van Maanen, J., 1979. The fact of fiction in organizational ethnography. Administrative Science Quarterly, 24(4): 539–550.

Wagner, M., 1995a. Firm thrives on client/server consulting. Computerworld, 29 (46): 13, 87.

Wagner, M., 1995b. Holiday Inn books client/server. Computerworld, 29 (47): 6.

Walsham, G., 1995. Interpretive case studies in IS research: nature and method. European Journal of Information Systems, 4 (2): 74–81.

Walsham, G. and Waema, T., 1994. Information systems strategy and implementation: a case study of a building society. ACM Transactions On Information Systems, 12 (2): 150-173.

Willcocks, L., 1995. Collaborating to compete: towards strategic partnerships In IT outsourcing? Oxford Institute of Information Management Research And Discussion paper 95/4. Templeton College, Oxford.

Willcocks, L., 1996a. Does IT-enabled business process re-engineering pay off? Recent findings on economics and impacts? In: L. Willcocks (ed.), Investing In Information Systems: evaluation and management. Chapman and Hall, London, pp. 171–192.

Willcocks, L., 1996b. Investing In Information Systems: evaluation and management. Chapman and Hall, London.

Willcocks, L. and Currie, W., 1995. Does radical re-engineering really work? A cross-sectoral study of strategic projects. Oxford Institute of Information Management Research Report RDP 95/8. Templeton College, Oxford.

Willcocks, L. and Griffiths, C., 1994. Predicting risk of failure in large-scale information technology projects. Technological Forecasting And Social Change, 47 (1): 1–23.

Yin, R., 1989. Case Study Research: design and methods, Sage, London.
