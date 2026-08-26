---
otero_id: 26992
otero_key: "85QCKB7N"
title: "Integrating Islands of Automation"
authors: "David P. Hale; William D. Haseman; Frank Groom"
year: "1989"
journal: "MIS Quarterly"
doi: "10.2307/248729"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Integrating Islands of Automation
Author(s): David P. Hale, William D. Haseman and Frank Groom
Source: MIS Quarterly, Vol. 13, No. 4 (Dec., 1989), pp. 433-445
Published by: Management Information Systems Research Center, University of Minnesota
Stable URL: http://www.jstor.org/stable/248729

Accessed: 09/05/2014 15:30

Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at http://www.jstor.org/page/info/about/policies/terms.jsp

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

# Integrating Islands of Automation

By: David P. Hale
Department of Information Systems and Quantitative Sciences
College of Business Administration
Texas Tech University
Lubbock, Texas 79409

William D. Haseman
School of Business Administration
University of Wisconsin-
Milwaukee
Milwaukee, Wisconsin 53201

Frank Groom
Customer Services and
Marketing

Ameritech Applied Technologies, Inc.

845 North 35th Street
Milwaukee, Wisconsin 53208

## Abstract

This article describes the design, implementation, and post-implementation evaluation of the corporate data transport system used at Wisconsin Bell, Inc. to aid distributed, inter-department decision making. Elements of the system's architecture include a user-friendly executive support system, enhanced professional/managerial workstation environments, and a common presentation system that integrates multiple heterogeneous systems, thus creating “virtual homogeneity” of information presentation throughout the organization. The system has been developed to connect geographically dispersed executives and professionals from different functional areas, regardless of hardware, software, and data configurations. The intent of the system is to allow its users to share information and work together as a single operating entity and integrated planning unit. Key success factors leading to the system's use over a three-year period are explored, along with unanticipated limiting factors.

Keywords: Distributed decision support systems, end-user computing, electronic mail, electronic meetings, executive support, group decision support systems, information systems design, office automation

ACM Categories: C.2.1, C.2.4, H.1.2, H.4, K.6.4

## Introduction

Similar to many firms, Wisconsin Bell, Inc. permits its managers to justify the purchase of personal computers to satisfy their individual information and productivity needs. Use of these machines has grown from the creation and storage of personal files for simple word processing and elementary spreadsheet calculations to departmental database systems and an organizational communication system for decision support. To expedite the exchange of information and to support ad hoc groups (many projects within the firm employ a matrix organization structure), Wisconsin Bell, Inc. (hereafter referred to as Wisconsin Bell or WBI) has created a corporate data transport system (CDTS). It facilitates communication by integrating isolated personal computers and heterogeneous mainframe systems to form an organization-wide information and communication system. The system establishes a virtual local office environment regardless of managers' geographic locations and is not dependent on homogenous hardware.

## Description of Wisconsin Bell

Wisconsin Bell was forced to change its organizational structure January 1, 1984. It had been a local operating company for American Telephone and Telegraph (AT&T). As part of the antitrust settlement between AT&T and the U.S. Department of Justice, the local operating companies were divested from AT&T. Wisconsin Bell combined with the other midwestern local operating subsidiaries of AT&T to form Ameritech. WBI's mission is to provide local telecommunication facilities to the general public in compliance with state and federal regulations. The company's basic function is to transmit point-to-point communications within a predefined geographic area. WBI has 1.2 million customers throughout the state of Wisconsin.

## The Problem Setting

WBI has slightly less than 7,000 employees to service its customers. Approximately one-half (3,500) are technical support and managerial positions. Considerable resources have been spent for new computer applications to aid the support and managerial personnel in their operational and strategic duties. Essentially, every member of the professional and managerial staff has a computer terminal or personal computer in his or her work area. The firm computerized its data processing in the 1960s and has several major online application databases today. The organization has multiple processing centers to physically support its personnel. Figure 1 presents the telecommunication system linking WBI's four primary data centers. Each data center has multiple IBM 3090-class mainframe computers. One data center also houses a tightly coupled DEC-VAX 8650 cluster. The high-speed wideband cable and optical fiber network provides fast inter-site transmission.

Wisconsin Bell now operates in a highly competitive market for value-added services and computer branch exchanges. It actively employs participative management techniques that prescribe the involvement of numerous personnel in every decision. In practice, this often requires employees from geographically separated departments to cooperate and exchange information. The organization is committed to a decentralized structure that employs a matrix organization to form problem-solving groups. These groups need to operate as if they are in a “virtual office” even though their members are physically separated. One method to facilitate this organizational structure is to allow staff personnel to act as liaison and coordination vehicles. However, in the highly competitive environment now facing WBI, adding staff positions to fulfill coordination needs is not feasible, and systems that reduce labor requirements are given high priority. The corporate data transport system (CDTS) was conceived as a technical solution to achieve this end. It furnishes staff professionals and senior executives with the capability to communicate with one another while reducing the support personnel requirements.

![](/api/attachments/85QCKB7N/fulltext/images/bcfb9dad171326c5d4bf82b65b429ad2c60d42072bab2991a341a7926deb58f6.jpg)  
Figure 1. Conceptual View of WBI's Telecommunication Network

The CDTS has been implemented in phases over a three-year period. Prior to the project's current phase, personal computer-to-mainframe connections were difficult to use. When connections did exist, personal computers were primarily used as terminal emulators. However, local pockets of automation existed; users employing various hardware and software had created make-shift facilities to meet their needs. A survey by Campbell (1987), conducted as a joint effort by Wisconsin Bell and Digital Equipment Corporation (DEC), evaluated the information needs of both the senior management and the technical professional personnel at WBI early in 1987.

The survey was sent to 730 employees drawn from a random sample of the approximately 3,500 managerial and technical support employees. Of those receiving the survey, 607 (83 percent) returned the survey, and of those, 508 respondents (84 percent) said they were computer users. Reported computer utilization is shown in Table 1.

The vast majority (82 percent) of the respondents had a computer in their work area, and 42 percent of the respondents used computer applications in more than 25 percent of their work activities. Although the respondents relied heavily on their traditional channels of communications, such as face-to-face and telephone contact, the information technology with the highest level of user satisfaction and utilization was electronic mail. Accessing corporate data ranked second in use but received low user-satisfaction marks.

Eighty percent of the respondents strongly agreed that it was critical to the organization's success to manage its information. Of those surveyed, only 46 percent felt that Wisconsin Bell managed information well. The most frequently mentioned reasons for this frustration included wading through irrelevant data, not knowing where to look for information, being unable to get timely data, and being unable to personally manipulate and analyze data in a user-friendly format.

## The CDTS Architecture

The corporate data transport system has been designed to reduce the frustrations described by survey respondents and to promote communication exchanges between end users. The early phases of the project included providing a user-friendly system for senior management (selling this group on the importance of exchanging ideas provided the financial and leadership support necessary to continue the project), incorporating personal computers into workstations (of senior management and professional staff), training personnel, and addressing system weak points.

Although the CDTS provided a top-down view of the organization's total communication and decision support needs, a bottom-up implementation strategy was chosen for this phase. This strategy emphasized the priorities of maintaining current user satisfaction, evolving to a new level of support, minimizing end-user disruption, satisfying local needs quickly, and building a positive image quickly. Reliance was placed on the organization's networking strengths to conquer the data-link and protocol-control problems of connecting diverse technologies.

Table 1. Reported Computer Utilization

<table><tr><td>Computer Type</td><td>Percent of Respondents</td><td>Primary Activities</td></tr><tr><td colspan="3">Mainframe Computers:</td></tr><tr><td>DEC-VAX 8650</td><td>32%</td><td>Electronic Mail</td></tr><tr><td>IBM 3090</td><td>63%</td><td>Electronic MailTSO/CIS Applications</td></tr><tr><td>Other</td><td>5%</td><td>Network Management</td></tr><tr><td></td><td>100%</td><td></td></tr><tr><td colspan="3">Personal Computers:</td></tr><tr><td>IBM PC</td><td>69%</td><td>Word ProcessingSpreadsheets</td></tr><tr><td>APPLE Macintosh</td><td>8%</td><td>Electronic Publishing</td></tr><tr><td>Other</td><td>5%</td><td>Network Management</td></tr><tr><td></td><td>82%</td><td></td></tr></table>

As a result of earlier CDTS phases, end users were assigned to mainframe computers and mail systems based on their level in the organization. Senior executives were serviced by office automation software on a cluster of DEC 8650 computers, and the professional staff was serviced by a variety of software on networked IBM 3090 computers. Secretaries were assigned to systems based on whose work they supported.

Figure 2 depicts Wisconsin Bell's corporate data transport system, including the most recent enhancements. The system architecture provides access to corporate data through the connectivity and protocol translation subsystem. This subsystem enables end users to exchange information regardless of hardware and software configurations. Hardware and communication software supported includes IBM's System Network Architecture (SNA), DEC's DECNET (Ethernet), and a variety of local area networks (LANs). General applications written for end users on specific hardware are filtered through the use of a common presentation system so that there is virtual homogeneity across the entire system. Personnel from operations/production, staff/professional and strategic/executive/senior management each have their own system interface, which allows them to manipulate corporate and local data. Thus the system's architecture supports: (1) the functional needs of senior management and technical professionals; (2) communication protocol translations; and (3) corporate data storage and retrieval requirements. The following sections refine each of these architecture components.

![](/api/attachments/85QCKB7N/fulltext/images/00623841096113f3196d1147a86475395381b7fdbf335927f261c7871e54a075.jpg)  
Figure 2. Corporate Data Transport System Architecture

## Supporting senior management's functional needs

Senior executives spend a large portion of their time and effort as information transmitters and recipients. As transmitters, they dispatch letters and memos giving direction or requesting information, clarification, or action. As recipients, they receive summarized reports, memos, letters, and results. Their messages require quick delivery, flexible dissemination patterns, archival and retrieval procedures, system reliability, and functional expandability. Due to time pressures and human-computer interaction anxieties, a presentation system to facilitate their actions was deemed to be fundamental. The CDTS was designed to contain simple, distinct screen design and consistent keystroke assignments. Appropriate messages and an online help function were also included. Thorough testing of the system was necessary to prevent “black holes” through which users could fall.

Senior management is supported through DEC's All-In-One office automation system. It provides communication, word processing, filing services, calendar/meeting scheduling, and access to external and internal corporate files of information with minimal initial training. As users are added to the system, standard reports they require on a periodic basis are cataloged. Users can browse through their catalogs with the touch of a single keystroke.

## Supporting technical professionals' functional needs

Technical professional personnel are in such functional areas as accounting, management information systems, personnel, and marketing. These workers spend a significant portion of their time creating corporate action reports, position papers, and recommendations. These papers include such things as product forecasts, product pricing alternatives, cost/benefit analysis, and summary statements of technology, competition, and economic plans. System users require readily available data and software manipulation packages. Past difficulties for these professionals included inabilities to: (1) access corporate information contained in production data files; (2) collect, organize and incorporate segments of other works in a specific document; (3) disseminate a completed document to others (including peers, subordinates, and supervisors); (4) gather and categorize responses to a specific document; and (5) alert senior management to work assignment modifications.

Technical professionals are equipped with local intelligent workstations (IBM XT, IBM 3270 PC/XT, IBM PC/AT, IBM 3270 PC/AT, IBM PS/2, and Apple Macintosh personal computers) and appropriate software (Dbase, Lotus, PC-Focus, PC-IFPS, SPSS-X, and a variety of word-processor packages) to accomplish their work. An information center has been created to catalog, store, and provide access to corporate data. Relational databases and associated data dictionaries exist for end users.

To aid system users, a common presentation system (CPS) was developed as an in-house application. CPS provides a simple user interface for the complex navigation and manipulation rules found in mainframe database management packages. This allows professionals to concentrate on their functional responsibilities rather than syntax. CPS also delivers personal computer software and data through its menu system. Users can access operating system commands, data files, and software packages without any knowledge of specific start-up commands or naming conventions. Thus professionals use the corporate databases as end users rather than data processors. In addition to application tool knowledge, the only skill needed by CPS users is the ability to use arrow keys. Users are presented with pop-down menus so that they can quickly move between options and observe item relationships. Sample CPS screens are presented in Figures 3 through 6. Users merely navigate through the main menu (Figure 3) until a menu containing the files they require appears (Figure 4). Upon selecting a file, a user chooses the items of interest from another menu containing the fields that they are authorized to retrieve (Figure 5). Once the fields are identified, the system automatically generates, transmits, and executes the necessary queries to obtain the data from information center files. At the user's discretion, the extracted data can be transferred (downloaded) to a personal computer or kept in a mainframe file. The system has the ability to automatically join and summarize fields as well as export files in specific personal computer software package formats (Figure 6).

![](/api/attachments/85QCKB7N/fulltext/images/1366077a6867467205733444dbb717b57845151fc629fe215d8eade71fa93fcf.jpg)  
Figure 3. Sample Common Presentation System Master Menu

![](/api/attachments/85QCKB7N/fulltext/images/792098b5330f9bce290720578666fdcf2ea24b64cba4b44d32b4286e8d694d3d.jpg)  
Figure 4. Sample CPS File Selection Menu

<table><tr><td>SELECT FIELDS</td><td colspan="3">Download of Mainframe Data Bases to dBase</td><td>09/13/89</td></tr><tr><td>Version 1.1</td><td>Data Base: FOCUS</td><td colspan="2">File: EMPLOYEE</td><td>08:34:34</td></tr><tr><td>Data Base</td><td>Files</td><td>Data Fields</td><td>Selection Criteria</td><td>Commands</td></tr><tr><td></td><td></td><td>EMP_IDLAST_NAMEFIRST_NAMEHIRE_DATEDEPARTMENTCURR_SALCJCED_HOURSUNION_IDDEPARTMENTULDAT_INCPCT_INCSALARY</td><td></td><td></td></tr><tr><td>SELECT FIELDS:</td><td>↑Up</td><td>↓Down</td><td>◀To Select entry</td><td>Esc To Exit</td></tr></table>

Figure 5. Sample CPS Field Selection Menu

<table><tr><td colspan="6">DOWNLOAD Version 1.1 DOWNLOAD MAIN MENU 09/13/89 08:35:08</td></tr><tr><td>Download Data</td><td>Display Data</td><td>Convert Data</td><td>Define Files</td><td>Exit</td><td></td></tr><tr><td></td><td></td><td colspan="3">Convert to Lotus (WKS) Convert to VisiCalc (DIF) Convert to Multiplan (SYLK) Convert to Comma Delimited Convert to Word Processor Convert to ASCII</td><td></td></tr><tr><td colspan="6">SELECT OPTION: ↑Up ↓Down ←Left →Right ←To Select entry Esc To Exit</td></tr></table>

Figure 6. Sample CPS Download Main Menu Highlighting the Conversion Utility

In addition to the standard CPS, specialized storage, retrieval and presentation systems have been built for specific groups. The marketing information system is an example of such a corporate information system; it has numerous selection and display routines that are executable from personal computer workstations by striking a single key. Users can simply request predefined queries and reports on demand without specifying individual fields.

## Connectivity and protocol translation

To accomplish the exchange of documents and models, the corporate data transport system provides a transparent gateway between IBM-SNA, DEC-DECNET, IBM-Token Ring local area network, and Appletalk. The system provides electronic mail transmission, ASCII/EBCDIC conversions, and binary file transfers. Transmittable material includes any combination of data, graphs, text, spreadsheets, and models. The recipient can view, revise, forward, and/or return the revised material to its originator. Thus professionals can iteratively communicate among themselves and senior executives. Currently over 12,000 users across the state of Wisconsin, including WBI customers, are connected through the corporate data transport system.

Although not explicitly depicted in Figure 1, Wisconsin Bell's corporate data transport architecture furnishes transparent gateways between heterogeneous computer systems. The architecture allows users to exchange data, information, ideas, and models without regard to geographic location, organizational status, or hardware configuration. Connectivity and protocol translations occur between the DEC 8650 cluster, IBM-SNA network, Integrated Service Digital Network (ISDN), and a variety of local area networks. Physical facilities within the greater Milwaukee area are connected by high capacity T1 (1.544 megabits per second) carrier lines, with additional bi-sync (56 kps) and voice grade (9.6 kps) lines available for specialized applications. System users in cities other than Milwaukee are connected through Wisconsin Bell's packet-switched network. Packet assembler/disassemblers (PAD) using the CCITT X.25 protocol are linked to the DEC 8650 computer cluster. Dial-up facilities are also supplied for those users not connected to a PAD.

Users requiring shared local file storage and/or high quality printing utilize local area networks. Currently, WBI is conducting an evaluation of various LANs. Those currently in use include Appletalk, DECNET, Ethernet, IBM Token Ring, Centrex Office LAN, and AT&T's Starlan. Each individual LAN is connected to the CDTS via an SNA gateway, an X.25 bridge, or a set of asynchronous modems. In addition, many non-management workers have online access to the organization's production systems and interact continually with these systems to perform their daily assignments. These workers employ non-intelligent workstations to execute IMS/DC, CICS, and TSO applications. Multiple system sessions can be maintained simultaneously.

## Corporate data storage and retrieval system

The CDTS relies on production and end-user databases to obtain and store needed data. Without data, the technologies described thus far provide little more than advanced electronic messages. The common presentation system allows users to search and extract data sets from these databases. Once extracted, these data sets can be used throughout the organization on any component of the CDTS.

An end-user database administration group has been established to formally structure the corporate data for the information center. This group interacts with a cross section of the organization including application support, the end-user community, the information center, the training center, and data service's production control. The group is responsible for selecting one or more formats for representing data, thus ensuring that all data are properly structured, placed, and accessible to authorized users. Those responsible for the data's structure balance performance with storage constraints, internal anomalies, machine structure, and encoding techniques. The primary storage for the corporate data set is attached to the IBM-based data centers. Data exist in IMS, DB2, Focus, and Info Center-1 files.

## Example Problem-Domain

## Three WBI departments

The following is a description of three departments within Wisconsin Bell using the CDTS from its inception. The departments are geographically dispersed throughout the city of Milwaukee. One of the situations in which these departments use CDTS is to work together on product pricing and bid submissions. Personnel from all the departments collaborate to form a “team” that maximizes corporate resources.

## Corporate Accounting Department

The Corporate Accounting Department houses financial accounting as well as budgeting, disbursement accounting, tax accounting, and independent cost-review accounting. This was the first department to equip all of its senior executives and technical professionals with networked IBM PC/AT or IBM 3270 PC/AT personal computers. As a remnant of the early phases of CDTS, the personal computers are connected to both the SNA network for access to information center data and the Ethernet to DEC's All-In-One office automation system for electronic messaging.

## Marketing Department

The Business Product Marketing, Residence and Consumer Product Marketing, and Market Planning Department is in the final stages of equipping all its personnel with IBM PC/AT and IBM PS/2 personal computers. Each employee is connected via an SNA network to an electronic mail system and an internally developed marketing information system. The IBM-SNA/DEC-VAX gateway provides access to over 20,000 mail addresses at WBI and the other Ameritech companies.

## Service Costs and Tariffs Department

The Service Costs and Access Tariffs, Separations, and Capital Recovery Department has an IBM PC/AT or IBM PS/2 personal computer at every workstation. Personnel in this department access centralized time share systems for analytic evaluations. They require large quantities of data storage facilities, including information center files, production database files, and locally generated and stored models. The information center provides initial training for these employees in a wide variety of mainframe and personal-computer analysis packages. The professional analysts use electronic mail on the IBM mainframe system while senior executives in the group are connected to DEC's All-In-One for electronic messaging and word processing. The gateway between the IBM-SNA and DEC-VAX cluster provides connectivity between the groups.

## Pricing problem

Although each of these departments is independent, they are required to work together as a unit when a new product is to be introduced or a bid is to be tendered. The marketing department initiates the process when it receives a “request for proposal” by informing both the Corporate Accounting and the Service Costs and Tariffs departments as to the bid’s nature and the time frame in which a response must be given. The accounting personnel derive underlying costs through models and data stored in end-user databases. They use both mainframe and personal computer-based analytical tools in making their estimates. The Service Costs and Tariffs department is responsible for final pricing and filing for tariffs, when necessary.

The time frame from receiving a request for proposal to the actual bid being issued varies from a few days to several months. In the past, differences in perceptions were aggravated by geographical barriers. Underlying model assumptions sometimes were not relayed from department to department. As a result, the bidding process was cumbersome and provided less than optimal results.

To resolve these problems, the CDTS was used to make models and data commonly accessible to all groups. This is not to say all groups had the right to change data and/or models, but the groups could review the data and models for completeness and accuracy. In the early phases of the CDTS, electronic images of text files were exchanged; later as the technology improved, actual binary versions of the models and data were exchanged. The bidding process is more streamlined today with realistic bids being produced in a much more timely manner.

## CDTS Project Evaluation

Substantial changes have occurred in the process used by senior executives and professional staff personnel to conduct their activities. The flexibility of data exchange between previously isolated systems has allowed an increase in communication that more closely matches functional needs. The quantity of communications among organizational units has significantly increased. Throughout the design, implementation, and use of the corporate data transport system, several key factors have become evident. The remainder of this article describes both the positive and negative factors that have affected the systems' use.

## Electronic communications

The following subsections describe the key success factors leading to the acceptance of CDTS's electronic communication component. These factors include transmission immediacy, message accuracy, personnel interaction, action report support, and project management support.

## Transmission Immediacy

Users tend to start their day by logging onto the system. They send messages to subordinates, peers, and supervisors. Unlike telephone calls, electronic messages do not require the originator and the recipient to be simultaneously connected. Telephone tag has been reduced; additionally, the recipient of an electronic mail message is not interrupted as with a telephone call. A response to a message can occur as soon as it arrives (through the alerting system within electronic mail) or at the recipient's convenience (perhaps not at all — but unlike a telephone message, the originator of the electronic mail message is confident that the recipient has been notified).

## Message Accuracy

Messages sent through the CDTS have tended to be more accurately received than telephone conversations or relayed messages. Authors of documents have quickly learned that their readers will read only what is there, and they attempt to remove ambiguity by using bold type, underlining, and extended dashes for emphasis. The need to formalize thoughts has also decreased the use of off-the-wall estimates as facts.

## Personnel Interaction

The interactive nature of the communication fosters idea generation and critique. The CDTS provides for active “bantering” between users as they request and are asked for information and clarifications. This has led to several spontaneous electronic meetings, often involving many people, and has promoted formation of ad hoc task groups. The interaction between individuals has also reduced the time-consuming preliminary meeting activities; now each participant can read background material and ask for basic information outside of a physical meeting. Two worthwhile by-products of electronic meetings are the creation of a permanent record generated through the electronic correspondence itself and the inability of a group member or a clique to monopolize an electronic meeting as might occur in a physical meeting.

## Action Report Support

Senior executives now receive action reports on a regular basis. These reports contain results, progress notes, exceptions, and corporate “hotspots”. Executives have specific electronic folders for such reports (report dissemination lists include these folders). Depending on the nature of the report, the system either automatically alerts the recipient of the new report or files the report in a folder for review at a later time. Suggested periodic reviews include early-day hotspots review, time-permitting review of project results, progress notes, exception reports, and detailed review of results from the prior month/quarter/year.

## Project Management Support

The system allows managers at all levels of the organization to better control projects as they decompose assignments and combine outputs. As subordinates complete specific task assignments, not only can their results be conveyed to others, but the CDTS also facilitates the merging of results.

## Connectivity technology

Although the technology employed in this system does exist commercially today, considerable resources were allocated to connect the various systems. It has been necessary to test several different links due to the void between vendor claims and actual performance. For example, the link between the DEC cluster and IBM-SNA network has been upgraded three times in the past 18 months.

## Innovation

Executives are using new planning tools that change the way they manage the organization. Electronic information gathering has reduced the number of fact-finding meetings and increased the number of substantive tactical, control, and strategic planning meetings. In addition, the frequency and quantity of numerical analysis seems to be increasing. It is not yet clear whether the quality of analysis has improved; however, the number of copies of personal computer versions of IFPS, Lotus-123, and SPSS-X has increased dramatically along with the number of computer cycles attributable to mainframe data analysis software. At this point, it is not clear whether senior executives are doing more analysis now that they have access to data or if they are better directing their subordinates. It is clear that several problems and opportunities have been handled faster, with more alternatives discussed than there were prior to the existence of the CDTS.

## Organizational factors

Using Cheney, et al.'s (1986) propositions for future end-user research to evaluate Wisconsin Bell's corporate data transport system, it is clear that the following organizational factors aided in the successful introduction of the system.

1. The CDTS was first conceived to support senior executives. As many researchers (Dickson and Simmons, 1970; Gingras and McLean, 1982; Schonberger, 1980) have indicated, the higher the level of managers, the higher the perceived value of the support system.

2. The CPS provides structure to what would otherwise be unstructured tasks, thus promoting the acceptance of the system as a support tool (Culnan, 1983).

3. The CPS provides clarity and simplification. Tasks that were unrelated are now supported under a common structure.

4. Executives and professionals can extract and manipulate data themselves (or have subordinates perform the tasks at their direction) rather than have to wait for the information system personnel to develop a program.

5. Considerable resources have been expended for training and continued support of system users. As Sprague and Carlson (1982) suggest, preliminary training sessions, online help, help-lines, resident experts (secretaries), and user reference manuals aid personnel in utilizing the system.

## Unanticipated limiting factors

In addition to the positive factors listed above, five limiting factors emerged: the transmission of reports, memos, and requests outside official and traditional flows; the transmission of unedited, uncensored thoughts; the lack of private communications; the lack of specialized aptitudes by technical support staffs; and the need to extend the CDTS to electronic brainstorming and group mediation activities.

## Transmission of Material Outside Traditional Flows

Inhibitions to level-jumping within the organization structure have been diminished. Junior-level CDTS users are not reluctant to write to senior executives, nor are senior executives hesitant to request information directly from junior-level employees. As a result, a new openness has occurred that has had a mixed reception. Across organizational boundaries the CDTS has been used to generate misinformation and miscommunication; however, within the same organizational unit, personnel seem to have a better grasp of what is acceptable to be sent and requested. Although this level-jumping violates both formal and traditional lines of communication and authority, there are no plans to restrict access to the CDTS.

## Transmission of Unedited, Uncensored Thoughts

Electronic mail users tend (once familiar with the system and the keyboard) to create and send messages in one session at the terminal. Traditional editing and self-restraint common to oral conversations and dictated letters are often abandoned. Culturally learned skills related to self-editing and controlling the form of messages to elicit specific effects on the recipient has not been internalized by all electronic mail users. This has created some embarrassing situations when the recipient has reacted in a manner opposite to that which was intended by the message's author.

## Lack of Private Communications

Messages sent to a single individual, even when classified as “private,” are often naively forwarded to others (the technology allows easy copying). This has been embarrassing to both the message’s originator and transceiver (recipient/forwarder).

## Lack of Specialized Aptitudes by Technical Support Staffs

End users who have access to the CDTS are not fully exploiting its features. Although we have not fully studied the reasons for the low utilization, we believe, in part, that many technical consultants are not familiar enough with the CDTS and end-user computing to properly advise their clients. Little attention has been given to the different skill sets needed in mainframe application support as compared with CDTS user support. A study is currently being conducted to determine what can be done to rectify this situation.

## Additional Need to Support Group Decision Making

The next stage of the corporate data transport system will be to improve the group decision support facilitator and mediator aids. Planning systems similar to PLEXSYS (Applegate, et al., 1987) are now being designed and implemented. The enhancements will manage the knowledge acquisition for strategic planning. Users will be able to create electronic brainstorming sessions (Osborne, 1953) while at their own workstations (cf. Nunamaker, et al., 1987). Ideas will be structured and analyzed prior to face-to-face meetings.

## Conclusion

Management and decision-making support are common processes within all organizations. Thus, the application of the technology, support software, approach, emphasis, and effects of the CDTS are of general interest to other organizations. Success requires the support, resources, and efforts of senior management. Policy statements must detail the organization's intent over a longer horizon. An effort should be made to correlate capital expenditures with changes in productivity. To create initial support for such systems, end users must realize that isolated corporate data limits their effectiveness. In this context, Wisconsin Bell has overcome many of the problems associated with geographic separation — specifically, the exchange of information and ideas.

## References

Applegate, L.M., Chen, C.C., Konsynski, B.R. and Nunamaker, J.F. “Knowledge Management in Planning,” Journal of Management Information Systems (3:4), Spring 1987, pp. 20-38.

Campbell, M.M. "Report on the Results of the Business Needs Survey," Wisconsin Bell Internal Report, unpublished report, Fall 1987.

Cheney, P.H., Mann, R.I. and Amoroso, D.L. “Organizational Factors and End-User Computing,” Journal of Management Information Systems (3:1), Summer 1986, pp. 65-80.

Culnan, M.J. “Chauffeured Versus End User Access to Commercial Databases: The Effects of Task and Individual Differences,” MIS Quarterly (7:1), March 1983, pp. 55-68.

Dickson, G.W. and Simmons, J.K. "The Behavioral Side of MIS," Business Horizons (13:4), August 1970, pp. 59-71.

Gingras, L. and McLean, E.R. “Designers and Users of Information Systems: A Study in Differing Profiles,” Proceedings of the Third International Conference on Information Systems, Ann Arbor, MI, November 12-15, 1982, pp. 169-181.

Nunamaker, J.F., Applegate, L.M. and Konsynski, B.R. "Facilitating Group Creativity with GDSS," Journal of Management Information Systems (3:4), Spring 1987, pp. 5-19.

Osborne, A. Applied Imagination, Charles Scribner and Sons, New York, NY, 1953.

Schonberger, R.J. "MIS Design: A Contingency Approach," MIS Quarterly (4:1), January 1980, pp. 13-20.

Sprague, R.H. and Carlson, E.D. Building Effective Decision Support Systems, Prentice-Hall, Inc., Englewood Cliffs, NJ, 1982.

## About the Authors

David P. Hale is assistant professor of information systems and quantitative sciences at Texas Tech University's College of Business Administration. He received his Ph.D. in management information systems from the University of Wisconsin-Milwaukee in 1986. His research interests include collaborative problem-solving systems and software maintenance. His papers on joint human-computer problem-solving systems, database management system design, decision-group connectivity, and software maintenance have appeared in MIS Quarterly, Journal of Management Information Systems, and several conference proceedings.

William D. Haseman is research professor of management information systems at the University of Wisconsin-Milwaukee's School of Business Administration. He received his Ph.D. in management information systems from Purdue

University. He has published numerous articles in the areas of database management systems design, decision support systems, end-user computing, interface design, and network connectivity. His work has been funded by the National Science foundation. He also is founder and president of M-Link, a computer and information system consulting firm.

Frank Groom is senior director of customer services and marketing at Ameritech Applied Technologies, Incorporated. He has held a variety of positions in the areas of application development, data center operation and support, database administration, end-user computing, and telecommunications at Wisconsin Bell, American Telephone and Telegraph, and Southern New England Telephone Company. He serves on the University of Wisconsin-Milwaukee Management Information Systems Advisory Board. He also is a member of the Milwaukee chapter of the Society for Information Management.
