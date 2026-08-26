---
otero_id: 18724
otero_key: "Z942ZGCT"
title: "A DSS approach for implementing an online retail banking system"
authors: "Mohammed H. Omar"
year: "1991"
journal: "Information & Management"
doi: "10.1016/0378-7206(91)90040-9"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
SOS

# A DSS approach for implementing an online retail banking system

A case study

Mohammed H Omar

University of Richmond, Richmond VA 23173, USA

This article is based on the author's experience in supervising the development and implementation of a distributed online retail banking decision support system (DSS) for Arab National Bank (ANB) in Riyadh – Saudi Arabia. The system emphasizes the different components and characteristics of DSS in terms of flexibility, responsiveness, ease of use, interactive interface, and the use of an adaptive process for design and implementation. The system provides branch management with facilities for direct control and monitoring of branch operations and for immediate access to information needed for decision making. Customer service was drastically reduced from an average of 30 minutes per transaction to a one minute average. The prototyping approach made it possible to solicit user participation and to facilitate the training and conversion processes which in turn eased the way for smooth and successful implementation.

Keywords Decision support systems (DSS), Prototyping, User participation, Interactive interface, Bank automation

![](/api/attachments/Z942ZGCT/fulltext/images/d3f88d2366cf791ec6b36cf5687db7ab020df2a0750b88bee5fba84bde072127.jpg)

Mohammed H Omar is an Assistant Professor of Management Systems at the University of Richmond Virginia B A from the American University of Beirut, his MIS and Ph D in Management Information Systems from Texas Tech University in 1979 He worked as a MIS executive Manager in a bank and as a computer consultant He also taught at the University of South Carolina-Spartanburg His research interests include decision support and expert systems, end user computing, user satisfaction, and system development methodologies

## 1 Introduction

The banking industry has been one of the pioneers in using computer based information systems (CBIS) Bankers need reliable, accurate, and timely information to properly serve their customers and to aid the bank managers in making proper decisions. However, most of the CBIS in banks have been developed around the concept of batch, overnight processing of transactions Rifkin [18] noted that many banks are disproportionately invested in “back-end” technologies such as automated accounting systems. While necessary and useful, these cost-minimizing transaction processing systems are unable to perform the “front-end” customer oriented tasks necessary to gain competitive advantage. Ironically, many of the banks that invested early and heavily in technology are today the least flexible in taking advantage of the new electronic environment. Nowadays, deregulation is forcing banks to build smaller distributed systems and networks that increase the effectiveness of branch banking

Recently, new types of information systems found their way to banking applications First, decision support systems (DSS) and knowledge based systems (KBS) are currently used in such applications like balance sheet management, cash management, mortgages and loans management, and international banking Second, branch automation is currently getting a great deal of attention Machlis [15] presents cases of banks that have redesigned their operational systems to make each branch an individual profit center which provides managers with the information needed to run their branches efficiently Some of the innovative systems and devices that are currently being installed in branches include interactive terminals, platform automation systems, and voice response technologies. The term “platform” is used to designate that area of a branch devised to customer service like opening of new accounts, accepting loan applications, and responding to customer inquiries. The goals of such systems are to identify and capitalize on sales opportunities provide detailed knowledge of the customer-bank relationship, increase productivity, and provide fast accurate, and cost effective customer services

Yet, inspite of the implementation of the mentioned systems and services, full branch automation as part of a comprehensive banking network has a long way to go. The main thrust of transaction processing still remains batch oriented

The objective and novel contribution of this article is in presenting a case that (1) describes a methodology of developing and implementing an online real time comprehensive and bilingual banking information system, (2) demonstrates how new technology and new approaches in system development help overcome some difficulties and constraints inherent in the nature and culture of developing countries, (3) presents an example of implementing a CBIS that integrates concepts of DSS, KBS, and electronic data interchange (EDI), and (4) provides insights on how information systems are going to cope with the deregulation issue that is forcing banks to build smaller distributed systems and networks that increase the effectiveness of branch banking

## 2 Background

ANB is currently the third largest bank in Saudi Arabia Prior to 1980 the bank was a Jordanian bank operating through five branches in the major cities. In 1980, the bank became a shareholding corporation with 60% of the shares owned by the Saudi public and 40% owned by the parent bank. The new board adopted a five year plan to expand by opening new branches at a rate of 10 to 15 per year. To face the challenges of the expansion plan and to stay competitive in the market, the board decided to automate the bank operations. In July 1981, I joined the bank to start the automation project. At subsequent meetings the board members set the objectives of the bank automation. These objectives were (1) to enhance and improve the competitive position of the bank in the face of the other major banks who had already automated their operations, (2) to improve customer service by reducing the current service time of 30 minutes per transaction and by producing timely customer statements and notices, (3) to implement a system that processes bilingual (Arabic/English) input and output, (4) to adopt a distributed processing approach that supports the decision processes at the branch, regional, and central levels of management, and (5) to implement automated security and control procedures over the online processing of transactions and the real time update of the master files. The latter was of particular importance because most of the transactions involve large amounts of cash deposits and withdrawals

## 3 The Search for Solutions

Following the guidelines of the board, a more detailed study of the existing manual system was performed to identify the data flow of each type of transaction and the decisions taken at each operational and managerial level in the branch. The findings of the study revealed certain unique requirements and constraints

The unique requirements of operations, namely the ability of the system to handle bilingual data, the semi-structured decision making process, and the availability of hardware and software with bilingual capability, were some of the main constraints. In addition, bank operation procedures were not available in a written form useful for determining the decision and data flows in the branches, and most of the decisions relied on the judgement of branch managers on case-by-case basis. Processing a transaction, for example, goes through a series of steps and involves redundant checking by several levels of supervisors before being completed

A request for proposal was prepared and major computer vendors and software houses worldwide were invited to bid through their local distributors. Most of the computer vendors responded favorably to providing bilingual hardware English-based online banking software packages were offered from major software houses like HOGAN and ANACOMP, but the cost of modifying and

Arabizing the software were prohibitive and the time of completion was never guaranteed

Faced with the above constraints and complexities, a decision was made to develop a banking system that would meet the needs of ANB The Digital Equipment Corporation (DEC) distributor, who had experience in supporting bilingual hardware and software, was awarded a contract to supply the hardware and application software to the bank. The hardware component of the system consist of dual VAX 780 at each of the three regions a minicomputer PDP11 at each branch, and communication devices to connect branches of each region to the regional system and to connect the three regions together to facilitate inter-branch banking all over the country. The software component of the system included a relational DBMS with query capability (TOTAL), a transaction management software for electronic data interchange, COBOL compiler, and DE-CNET communications software

Due to the supplier's lack of experience in banking applications, it was agreed to develop the application jointly by the bank and the supplier. The development team was formed from members of the bank operations department (future trainers of users), the bank MIS department system analysts (future maintainers of system), and the system builder (the supplier). The development approach was, to a great extent, influenced by the following factors (1) the system builder could not provide functional specifications on the sub-task level because of the lack of banking experience and nonavailability of clear written bank procedures, (2) the users could not specify their actual needs and had no past experience in computer applications, (3) the branch managers had different levels of authority, depending on the size of branch operations, that prevented standardization and required a system flexible enough to handle the common functions and to allow for personalized usage and support, and (4) the overall system was complex and the interfaces between the subsystems of the bank functions (i.e. withdrawal/deposit, branch accounts, foreign exchange, letter of credit, bills and collections, loans and facilities etc.) were not clearly defined or anticipated

The semi-structured nature of the application coupled with the above mentioned characteristics of the supplier and the user triggered the need to adopt a decision support system approach for development of the interactive banking application

## 4. System Development Philosophy

Decision support systems are designed to help improve the effectiveness and productivity of managers and professionals. They are interactive systems frequently used by individuals with little experience in computers. They support, rather than replace, judgement in that they do not automate the decision process. A DSS must be flexible to handle varied situations, easy to use, responsive to user needs, communicative with the user, and emerges through an adaptive process of design and usage [13]

There is a virtual consensus in the literature $[1,6,11,20,21,22]$ that the development approach for a DSS should differ from other types of CBIS Because of the difficulty of initially specifying information requirements, possible changes in the decision making environment, and changing in the decision making tasks, the development of a DSS should be iterative and evolutionary in nature $[6]$

Based upon the objectives of the bank management, the nature of the organization, the desire to meet the user requirements and provide support for decision makers, the following underlying DSS principles were applied in developing the banking system

## 41 Interactiveness

Interactiveness is one of the main characteristics of a DSS that influences decision performance quality and efficiency of the decision process. In their study, Cats-Baril and Huber [4] found that the “interactiveness” feature of a DSS positively affected decision quality. This provides support for the use of interaction in the decision making process

The bank system was designed as an interactive system to provide online functions for responding to queries of customers and bank personnel as well as to facilitate the reconciliation work for the teller, the cashier, and the accounting department. Such functions include customer account information, customer profile showing all customer accounts, teller activity during the day, online customer statement starting from any given date, on demand hard copy of customer statement, journal summaries for each ledger and type of transaction for reconciliation purposes

The interactive feature supported by the EDI software allows the branch manager to switch from one query screen to another and come back to the original screen. For example, if a manager is looking at a teller's activity screen to check the cash flow at that point and a beep signal comes to his screen designating the need to approve a teller transaction, he can accept the transmitted screen, call for that particular customer profile screen, make a decision to approve or disapprove the teller's transaction, then go back to what he was doing before. The interactive nature in the banking system proved to be an important tool for supporting the decision making functions of the bank managers and for producing a flexible and easy to use system

## 42 Prototyping

Naumann and Jenkins [17] define prototyping as a system that captures the essential features of a later system. A prototype system is intentionally incomplete, is to be modified, expanded and supplemented Groner, Hopwood, Palley, and Sibley [5] present a case study illustrating the effectiveness of prototyping in conducting a thorough information requirement analysis. In their article, they describe the use of prototyping to deal with uncertainty in both the user and designer environments. Research findings of Behrens [3] in project development productivity measurement, and the Kraushaar and Shirland [14] illustration of a state-transition model indicate that a prototyping process can encourage the efficient development of systems by breaking a complex and often ill-structured problem into several comprehensive yet smaller and simpler parts

Due to the dynamic nature of the bank's organizational environment and the characteristics of the user and supplier, determination of precise specifications prior to implementation was impossible or, at best, unrealistic. Thus an evolutionary approach for a DSS development of the banking system was adopted. The development process was broken into four stages (1) branch customer information, (2) branch accounting (3) other branch functions (L/C, Loans, etc), and (4) integration of the branch subsystems. A prototype was developed for the first stage and put through an iterative process of testing and modifications until an initial system was approved and implemented in parallel mode in a selected branch. Live implementations resulted in another iterative process of modifications until it became the final customer information system and was distributed to all branches for online implementation. During this time another prototype was built for the second stage to be integrated with the first. The process took three years to implement the first stage, one year for the second, one year for the third, and the fourth stage was still under implementation when I left the bank. Later I knew that it took two years to successfully complete the implementation of the fourth and last stage

Our experience of using the prototyping approach confirms the advantages attributed to this approach in the literature $[9,13,20]$ Yet, the literature over emphasizes the importance of time and cost savings. Some researchers $[11,21,22]$ indicate that the total time for a useful working system to evolve is often measured in days, weeks, or occasionally months. Such benefits might be true for small scale and specific types of problem oriented applications, but time management was the main problem faced by the bank. This difficulty is attributed to the complexity of the system, the uniqueness of the user needs, the high turnover of the participants in development (from both the bank side and the supplier side). Another fact inherent in the prototyping approach is that once the user learning curve rises, their demands for modifications rise which tends to keep the system open for a much longer time than anticipated and delays the final cutover and implementation. The most important advantage of the prototyping approach is that it guaranteed producing a system that met the user needs of the bank personnel and management.

## 43 User Participation

User involvement is not a new concept in the development of any CBIS, but it has received particular attention with regard to DSS Many researchers $[16,17,19,20]$ advocate not only user involvement but also user control over the project, thus requiring continuous involvement and responsibility This involvement often makes the ultimate user an “organizational champion” for the system and uses influence to gain needed organizational acceptance. In our case the users were involved in the stages of defining the information requirements, screen and report layout design, initial testing and experimentation, the conversion and final implementation of the system Table 1 shows the number of change orders that were initiated by the user departments and were incorporated into the prototypes during each stage of the development process. A change order might contain a request for changes in screen or report layouts, additions of new screens, reports and queries, correction of dictational or grammatical error, discovery of computational or logical error

Table 1  
Number of change orders for each stage of development

<table><tr><td>Stage</td><td>No of Changes</td></tr><tr><td>1 Technical testing of prototype 1</td><td>22</td></tr><tr><td>2 User experimentation with prototype 1</td><td>80</td></tr><tr><td>3 Parallel installation of prototype 1</td><td>60</td></tr><tr><td>4 Building prototype 2</td><td>225</td></tr><tr><td>5 Testing prototype 2</td><td>137</td></tr><tr><td>6 Building and testing prototype 3</td><td>174</td></tr><tr><td>7 Building and testing prototype 4</td><td>265</td></tr><tr><td>Total</td><td>963</td></tr></table>

Table 2 shows the total number of screens and reports at the end of each prototype. The changes and additions were identified mainly due to user participation and their feedback after the testing, experimentation, and implementation of each prototype

The bank experience showed that user participation created a sense of belongingness and ownership of the system which helped smooth the conversion and implementation. Yet, it was noticed that after the second stage was implemented and the users immediate needs were met, the level of involvement decreased and the users started to take more time for acceptance testing in order to have enough time to chew what they get

Table 2  
Number of screens and reports at the end of each prototype

<table><tr><td rowspan="2"></td><td colspan="4">Prototype</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td>No of screens</td><td>19</td><td>25</td><td>30</td><td>156</td></tr><tr><td>No of batch reports</td><td>6</td><td>28</td><td>50</td><td>60</td></tr><tr><td>No of online reports</td><td>0</td><td>12</td><td>15</td><td>20</td></tr><tr><td>No of inquiry screens</td><td>3</td><td>8</td><td>11</td><td>15</td></tr></table>

## 44 The User-System Interface

The term user-interface covers all aspects of the communications between the user and the DSS User-interface is the most important component of a DSS because most of the power, flexibility, and ease of use characteristics of DSS are derived from this component [21] The user interface facility is the visible part of the system to the user. The user-interface in the banking system application was accomplished in two ways

1 Programmable function keys that represent the main functions performed by the user

2 Main menus and sub-menus written in Arabic (the user language) covering all the range of functions and queries the user needs The user-system interface is designed in a modular way such that new options can be added easily to main menus and sub-menus

In addition, the system gives the authorized users the facility to maintain certain tables and production rules that are subject to change according to changes in data or changes in the decision rules. The system also provides the manager with the ability to move from one screen to another and come back to the original screen

## 5 Application Development Philosophy

In order to develop an efficient and adaptive system, the following principles were adopted

1 Transaction data is entered only once in its most basic form (1 g amount to be debited or credited, interest rate, value days/date, maturity date etc) and updates all related records automatically

2 Every financial transaction or control information affecting the account balances or the static data can be traced to the person making the transaction, the approving authority, and the date and time of the transaction

3 Each customer is assigned a unique customer number that is part of the account key for all types of activities related to the customer. The key consists of customer number (7 digits + check digit), home branch number (3 digits), currency code (2 digits), ledger code (3 digits), sub-account/sub-ledger code (2 digits) This way all customer activities can be consolidated for statement printing and for providing a full customer profile for departmental and corporate management use especially to aid in making credit and loans decisions

4 A knowledge base containing production rules that determine the action to be taken in each given situation is created and constantly maintained and monitored. Each type of transaction processed against each type of account has its own rules. Authority levels of tellers, supervisors, and managers are also formulated as production rules depending on preset amount limits for each level of management and for each type and amount of transaction. This method of representation ensured that the system works according to the same heuristic rules that managers used to apply in the manual system. The automation of the rules coupled with the EDI functions helped simplify the procedures for processing transactions and minimized the time and cost of paper handling and manual redundant checking and obtaining approvals

To better understand how the system works, an example of a session is presented here to show the transaction processing logic portrayed in Figure 1 and the user interface portrayed in Figure 2

Once the online system is up, a screen is displayed on all terminals for user identification where the system checks for access authorization and displays the main menu. The user can choose a function from the main menu to go to a submenu or shortcut the process by pressing a programmable function key to display the targeted screen. In processing a customer's transaction for cashing a check, for example, the teller would choose the withdrawal option from main menu thus a withdrawal screen appears as in Figure 2(c).

Data is then input for branch number and customer number. The system responds displaying branch name and customer name for visual verification and prompts for entering the account number, sub-account code and currency code. The system validates the input data and displays the

![](/api/attachments/Z942ZGCT/fulltext/images/acb62177418e9cbb8c817f05de83a890e78efe05cc3efea45bcbb78d08d3d73e.jpg)  
Fig 1 The Logic of Processing a Transaction

![](/api/attachments/Z942ZGCT/fulltext/images/a64358f1f1a52e2816941798e8a479e191329e00e7a0c53c258a138fb85daaa6.jpg)

![](/api/attachments/Z942ZGCT/fulltext/images/be1a0204c925945e43cb043723bc9485de760b3c0bf41395856828f5b4ef4b2b.jpg)

![](/api/attachments/Z942ZGCT/fulltext/images/f5b8e7bb98ba90fb640de428c7116de1877d3a66ff3d80578ff48547b8d26ae6.jpg)

![](/api/attachments/Z942ZGCT/fulltext/images/e94076e36bbe004cbc5c0d19d9b8422e373675a94ced9e6934d9f298da98a57e.jpg)

![](/api/attachments/Z942ZGCT/fulltext/images/3ebe738dfb9c49f49d0df066af64639bc3b47dda841abc504c08df44a27b0dce.jpg)

![](/api/attachments/Z942ZGCT/fulltext/images/fe163b2712c8c9d5f53834acefeea49fb3ef70c4fa9acd5268cfe6a135c5c3e9.jpg)

![](/api/attachments/Z942ZGCT/fulltext/images/deb450d91688d027b70af2e3bd9aee884e1460183d6d9bf0370ae0e198dbe079.jpg)  
Fig 2

account name and currency name for visual verification and prompts for entering check number, value date and amount The system validates the check number against numbers issued to the customer and checks the status of the account and the amount to determine the authority level for such case as set in the knowledge base. If the account is clear from any restrictions and if there were sufficient funds and the amount was within the teller's authority, then the system would signal the teller to process the transaction, otherwise the system would route the transaction to the appropriate level (the manager for example) determined by the decision rules in the knowledge base The manager would then receive a beep sound on his terminal and a message requesting him to press a function key to accept transmission If the manager does not answer within ten seconds, the system automatically transmits the message to the next level of authority Once transmission is accepted, the teller's screen would be displayed with additional information about the available balance in the customer's account, the amounts of checks deposited but not available yet, and the amount the account would be overdrawn due to execution of the transaction – if applicable as in Figure 2(e) The manager would then approve or disapprove by choosing the proper response on the screen If the manager needed more information about the customer, he could press a function key for queries and display balances in all customer accounts then go back to the previous screen and make the decision After making the decision, the teller gets a message to act accordingly All this happens in less than a minute without the customer's or teller's awareness

At this time, the transaction would be stamped – by an online document verification printer – and assigned a unique number consisting of the teller's ID, time and date, the ID of the person authorizing the action, the account number affected, and the amount

## 6. Impact of the system on bank operations

The implementation of the system resulted intangible benefits to the customers, branch personnel, branch management, and the bank general management. The following are some of these benefits

1 Customer benefits were manifested by (a) improved service by reducing the average service time from thirty minutes to one minute, (b) ability to complete a transaction through the customer's contact with one teller, contrary to old procedures which required interface with more than one of the branch personnel, and (c) improved quality and timeliness of customer statements which include consolidation of all customer account types

2 Branch personnel benefits were realized through (a) reduction of stress from the pressure of previously dealing with long queues of customers, (b) reduction of teller cash shortages due to improvement of security and control measures, (c) time saving in obtaining approval for transactions, (d) elimination of the daily after-hours back-office operations due to automating the accounting and reconciliation functions, and (e) elimination of repetitive writing of static information and reduction of errors due to illegible hand writing

3 Branch management benefits were achieved as a byproduct of the facilities provided by the system like (a) the automation of authority levels and approvals freed managers to do more planning, monitoring and selling of bank services, (b) the online inquiry enabled managers to immediately answer questions regarding customer accounts and to have access to information about all activities of the customer, (c) the online reports enabled the managers to monitor the teller activities and the cash flow any time in the day and helped the managers make better investment decisions, (d) the system enabled the expansion of branch activities and the ability to process more transactions without increase in manpower, and (e) the availability of statistical reports on demand enabled the manager to access information about customer characteristics and types of businesses and their activities which helped planning for expansion and provided better awareness to the ongoing activity in the different sectors of the economy

4 General management benefits were manifested in (a) the ability to use the network to transmit information to all branches allowing for consistency in implementation (such as interest rates, changes in policies, and currency exchange rates), (b) the ability to produce consolidated financial and statistical reports needed by decision makers at the corporate level, (c) the ability to download new releases of software from the central computer to all branch computers, and (d) the ability to open and staff new branches in shorter periods of time The number of branches increased from 15 branches at the beginning of system development to over hundred branches currently using the online system

## 7 Conclusion

Because the bank never had an existing mainframe network and because availability of funds never created a problem, corporate data personnel had the luxury of installing the most up-to-date systems without the worry of supporting older technology. The total cost of the project was very much in line with total costs obtained from major suppliers as quoted in their responses to the request for proposal. The length of time it took to complete implementation was the main drawback to this experience

The system framework employed in this case is consistent with that proposed by Keen [1981], and Keen and Wagner [1979] This paper presents live experience in implementing a DSS. The validity of this experience is high in that the system was successfully implemented and continues to be used. This experience is generally consistent with the growing body of research on DSS, and thus merit the following conclusions

First the prototype development process proved to be a useful strategy, and in our experience was the only strategy that promised fruitful results although final implementation took much longer time than anticipated

Second, the adaptive process employed in system development stimulated the learning of the users and their understanding to what the system might offer. This resulted in active participation and constructive feedback that helped to expand the system capabilities and the range of its uses. The number of changes implemented in response to user feedback amounted to 963

Third, the relationship between the user and the system builder is extremely important in implementing the adaptive process. The two parties have to be patient and understanding during the iterative process of design and implementation. The close relationship in our experience was a determinant factor in the success of the project

Fourth, the simplicity and clarity of the user interface facility is of utmost importance. The impact is clearly felt in the stages of implementation and user training where the users have little experience in computers, yet their being part of the system left no room for any resistance to change especially after promoting many of the personnel in the early starting branches to higher positions in the new branches to become trainers of others

## References

[1] Alavi M and Henderson, J C “An Evolutionary Strategy for Implementing a Decision Support System,” Management Science, Vol 27, No 11, 1981 pp 1309–1322

[2] Bally, L., Brittan, J., and Wagner K H “A Prototype Approach to Information System Design and Development” Information & Management Vol 1 No 1, 1977 pp 21–26

[3] Behrens, C “Measuring the Productivity of Computer Systems Development Activities with Function Points,” IEEE Transactions on Software Engineering, SE-9, No 6, 1983, pp 648–652

[4] Cats-Baril W L, and Huber, G P, “Decision Support Systems for Ill-Structured Problems An Empirical Study,” Decision Sciences, Vol 18, Summer 1987 pp 350–372

[5] Groner, C., Hopwood, M D., Palley, N A., and Sibley, W "Requirements Analysis in Clinical Research Information Processing - A Case Study," Computer Vol 12, No 9 1979 pp 100–108

[6] Hogue, J T, and Watson, H J, “Current Practices in the Development of Decision Support Systems,” Proceedings from the International Conference on Information Systems, 1984

[7] Jackson, D M, “Service Quality Improves with Branch Automation,” The Magazine of Bank Administration, March 1988, pp 32–33

[8] Jackson, D M, “Platform Automation A Banking Priority,” The Magazine of Bank Administration, January 1988, pp 58–62

[9] Janson, M A, and Smith, L D, “Prototyping For Systems Development A Critical Approach,” MIS Quarterly, Vol 9, No 4, 1985, pp 305–315

[10] Keen, P G, and Wagner, G R, “DSS An Executive Mind-Support System,” Datamation, Vol 25 No 12, 1979, pp 117–122

[11] Keen, P G and Morton, M S, Decision Support Systems An Organizational Perspective, Addison Wesley, Reading, Mass, 1978

[12] Keen, P G, “Value Analysis Justifying DSS,” MIS Quarterly, Vol 5, No 1, 1981, pp 1–15

[13] Keen, P G, “Decision Support Systems A Perspective Approach,” In The Rise of Managerial Computing, ed John F Rockart and Christine V Bullen, Dow Jones-Irwin, Homewood, Illinois, 1986

[14] Kraushaar, J M, and Shirland, L E, “A Prototyping Method for Applications Development by End Users and Information Systems Specialists,” MIS Quarterly, Vol 9, No 3, 1985, pp 189–197

[15] Machlis, Stephen A, “MIS in Banking The State of the Art” The Bankers Magazine Vol 16, No 5, 1983, pp 48–54

[16] McClean, E R, “End Users as Application Developers,” MIS Quarterly, Vol 3, No 4, 1979, pp 37–46

[17] Naumann, J D, and Jenkins, M A, “Prototyping The New Paradigm for Systems Development,” MIS Quarterly, Vol 6, No 3, 1982, pp 29–44

[18] Rifkin, G “Technology in Banking Who is Cashing In?” Computerworld, March 9, 1987 pp 65ff

[19] Sanders, G L, and Courtney, J F, "A Field Study of Organizational Factors Influencing DSS Successes," MIS Quarterly, Vol 9, No 1, 1985, pp 77–99

[20] Sprague, R H Jr., “A Framework for the Development of Decision Support Systems,” MIS Quarterly, Vol 4, No 4, 1980, pp 1–24

[21] Sprague, R H, Jr, and Carlson, E D, "Building Effective Decision Support Systems, Englewood Chiffs, N J Prentice Hall, 1982

[22] Wagner, Gerald R “Decision Support Systems The Real Substance,” Interfaces, Vol 11, No 2, 1981 pp 77–86
