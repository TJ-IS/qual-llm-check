---
otero_id: 23559
otero_key: "YFAZB3RU"
title: "Moving from an Executive Information System to Everyone's Information System: lessons from a case study"
authors: "F P Wheeler; S H Chang; R J Thomas"
year: "1993"
journal: "Journal of Information Technology"
doi: "10.1057/jit.1993.24"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Moving from an Executive Information System to Everyone's Information System: lessons from a case study

F.P. WHEELER, S.H. CHANG and R.J. THOMAS $^{1}$ Management Centre and $^{1}$ Department of Computing, University of Bradford, UK

The history of a major steel company's executive information system (EIS) is reported from its inception in 1984, through its demise as a system for top management, to its transformation in 1991 as a strikingly successful information system for all managers and administrative staff. This case has significant implications for all those who are interested in providing technical support to top decision-makers. It also has important lessons for any organization that has an EIS or that is planning to implement the current generation of EIS technology.

## Introduction

The past decade has seen the adoption by many large organizations of ‘Executive Information Systems’ (EIS). These are computer systems that deliver information to senior executives. An EIS should make it easier for senior people to have the information they need to do their jobs. EIS development addresses an issue that is of importance to decision-support specialists since it is a serious attempt to provide technical support to top decision-makers.

In what follows, we examine the history of one EIS. In several ways this case is typical of many EIS developments, because it confirms most of the conclusions of authors (Rockart and Delong, 1988; Burkan, 1989; Gulden and Ewers, 1989; Watson and Glover, 1989; Preedy, 1990; Watson et al., 1991) who have investigated other cases and causes of EIS failure. This case is also different because it is a story of a failure that has become a dramatic success. It is the story of an information system that was initially not used more than once a month and suddenly became used several thousand times a month. We shall attempt to explain these startling observations and draw conclusions of interest to all those who aim to build support systems for decision-makers.

## The company

We report below the history of an EIS within a major steel corporation, with a production level that places it among the top 20 worldwide. There is a high level of sophistication in the use of IT within this organization. The IT department employs over 100 people and its reputation is such that it provides consultancy to the industry, both domestically and internationally. Information technology is highly visible. Manufacturing is automatically controlled by process computers or local computers with a near real-time data link to a mainframe. An optical fibre network extends throughout the plant so that on-line processing can function in real time. This sophisticated technology permits customers, who use the public telecommunications network, to perform order entry and to inquire into the readiness or shipping status of their orders. Information is accurate, not only because of near real-time processing, but also by enforcing rigid controls on data entry and batch report generation.

## Development of the EIS

Decision-support software was already supported by the IT department when the EIS was developed in the mid 1980s. For example, packages such as SAS and IFPS were available from the mainframe. These facilities were offered via on-line entry and queued batch processing with a turn-round of 2 h on average. The users were mid to low level managers and administrative staff. Currently, these users can choose between the mainframe and a networked PC. In the latter case, data is down-loaded for further analysis (e.g. on a spreadsheet). Bridges between the IT department and functional departments existed in the form of departmental DP staff, who had had one or two years' training in the IT department. This was the environment within which the EIS was specified, developed and maintained.

## The executive information system

In 1984, the executive vice-president asked the IT department about the possibility of an on-line inquiry system to meet his specific information needs. At that time, no suitable product was available for purchase in the country, so the system was developed in-house. A traditional methodology was adopted, beginning with an analysis and specification of the vice-president's information requirements.

The system was developed with COBOL/CICS on an IBM mainframe. The database for the EIS consisted of about 20 indexed sequential (VSAM) files with multiple-index keys. This key structure enabled the system to offer the user multi-dimensional views of the data. Typically, the EIS database consolidated base-level data to three higher levels. Interaction with the system was by keyboard selection from a menu, using an IBM dumb terminal with colour display.

Six months later, the EIS was implemented and a further five senior executives, who had expressed interest, were also supplied with colour terminals in their offices. Each executive received one-to-one training in the use of the simple menu-driven interface. The main menu of the EIS, shown schematically in Figure 1, offered internal information on the corporate operational status (i.e. current production, sales, finished goods inventory), raw materials, personnel, finance and accounting, and capital expenditure. External data included details of competitors, in the steel industry worldwide and nationally, of national and global economic conditions.

![](/api/attachments/YFAZB3RU/fulltext/images/96d4a169d703bb34c136c24df62cc1a1e659098a32ec64b922632bb6a43395a7.jpg)  
Figure 1 The content of the EIS main menu and sub-menus

## Executive use of the EIS

The initial response to the system was good. The executives were impressed by the rapid access to information and the visually attractive graphics. The EIS was regularly demonstrated to visitors.

After three months, the original sponsor (i.e. the executive vice-president) departed. As the novelty wore off, the IT department became aware that the system was not being used. An embedded audit module had been built into the system to provide monitoring information. This revealed details of who used the system, when they used it, and what they accessed. It soon became evident that the system had no senior executive users. Later, the increasing popularity of personal computers (PCs) led to the replacement of executives' terminals by desktop PCs. Executive users now had typical stand-alone PC applications such as word processor, spreadsheet and diary, as well as mainframe access to the EIS. The EIS itself was slightly modified to meet the changed requirements. Despite these improvements, the system was so infrequently used that in some months the EIS database was not accessed at all.

## Contents of the EIS database

The EIS database drew in data from a range of internal and external sources. Internal data (i.e. that taken from the coporate database) were imported and summarized at the same time that daily batch reports were generated, in order to ensure accuracy and integrity. They included data from finance, accounting, sales, production and inventory. Essentially, the same data were summarized in the daily exception and status control reports, although the EIS permitted additional options, such as trend analysis. External data covered the macro economy, the steel industry and competitors. Some, such as exchange rates and market indexes, were bought in while other data were gathered by functional departments. Most external data had been established before the EIS was developed. They were already required by various departmental DSS, or were part of routine operations (e.g. the market research department regularly used industry and competitor data). The EIS database incorporated these data and thus offered senior executives on-line access to them. The information in the EIS database was, in principle, vital input to the senior executives' decision-making and yet it was not used.

In fact, the need for continuing support for an EIS, and the demise of the system when the executive sponsor departs, are commonly cited as reasons for failure (Rockart and Delong, 1988; Watson and Glover, 1989; Friend, 1990; Schenk and Vitalari, 1990; Volonino and Robinson, 1990). We believe that there are also fundamental reasons why current EIS technology is not successful and some of these are illustrated by this case, as will now be seen.

## Implementation problems

In 1991, an internal investigation by the company's IT and auditing departments into the lack of executive use of the EIS revealed several problems. The inquiry team interviewed the executives and the staff who would normally provide them with information. They tracked the executives' information sources and drew the following conclusions.

## Computer literacy

Although the system was easy to operate, the EIS did demand a minimum knowledge of its operating commands. The executives, as is typical elsewhere (Rockart and Delong, 1988; Mohan et al., 1990; Watson et al., 1991) had poor keyboard skills and lacked computer training. Their busy schedules did not permit them to become familiar with the EIS by regular use. The ‘unfriendly interface’ has been a common excuse for the failure of EIS elsewhere (Rockart and Delong, 1988; Watson et al., 1991).

## Lack of justifiable benefits

The EIS provided essentially similar information to that already available on paper reports: the added features, such as graphics and flexible data manipulation, were not sufficiently attractive to make executives give up the reports they had been using for years. One executive said he wished the EIS could deliver more timely information than these reports. Lack of cost justification is a common feature of many EIS implementations.

## Nature of executive work

One of the main roles of an executive is that of 'disturbance handler' (Mintzberg, 1973). Executives use intuition, based on experience, to find and define problems. They tolerate ambiguity as they intuitively generate ideas, perceiving and understanding novelty in the choice of solutions (Isenberg, 1984). This activity is spontaneous. Once dealt with, the problem area is briefly monitored until the executive is satisfied that it can be handled by subordinates. Then it becomes a routine job for the relevant department.

Senior executives in this company preferred not to ask the IS department to modify the EIS when their information requirements changed. Instead, they would turn to subordinates with specialized knowledge of end-user computing and DSS packages to deliver the reports they needed. They gave the following reasons for this:

## Difficulty of modification

Executives typically dealt with new problems that were event-driven. Their true information requirements could not be known beforehand and so could not have been specified during the EIS development. For example, the changing competitive environment should dictate the rules for exception reporting. But the EIS had fixed detection rules for exception control. These rules were embedded in the data extraction procedures, developed by the IS department, in a conventional programming language. Thus, executive users had no flexibility to make modifications on-line.

## Need to specify requirements

In their search for information, executives were able to tolerate ambiguity in their requirements and used a ‘trial and error’ approach to information retrieval. It was clear that the IS department could not modify the EIS to meet ambiguous requirements.

## Inappropriate data model

The logical data model of the EIS used a limited number of pre-defined key-field relations across different subject areas. This data structure was too rigid. Typically, actual queries were related to one another and to attributes of the problem at hand. A logical data model based on some form of inter-related network would have been more appropriate.

## Difficulty of communication

It was easier for executives to communicate with their direct subordinates than with the computer or the IS department. Oral communication with their staff, who were business oriented, was more effective than written memos to technologically oriented IS people. For example, one executive perceived the IS department as bureaucratic. This behaviour was verified by Mintzberg (1976), who found that executives prefer oral communication to any form of reading or writing.

## Lack of a 'what if facility

This EIS, unlike the DSS packages used by subordinates, had no ‘what if’ facility to investigate alternative scenarios. Today, according to Wagner (1988), spreadsheet what if analysis is routine even for high level managers. The lack of a ‘what if’ capability in this EIS meant that executives would ask subordinates to perform analyses on DSS packages, thus not using the EIS for important decisions.

For example, one executive could not use the EIS to evaluate the effects of alternative discount policies. Instead, he had to ask his subordinate to generate alternative scenarios on a DSS.

## Lack of support

The information-retrieval problem was ‘owned’ by the original senior executive sponsor. When this person left, a lack of support contributed to the demise of the system. Much current literature (Rockart and Delong, 1988; Burkan, 1989; Evans et al., 1989; Gulden and Ewers, 1989; Plein, 1989; Watson and Glover, 1989; Barrow, 1990; Friend, 1990; Volonino and Robinson, 1990; Watson et al., 1991; Wetherbe, 1991) stresses the importance of support from an executive sponsor and also the need for an operating sponsor who is appointed to ensure that the system is implemented. When the executive sponsor departed, the EIS lost the necessary budget for resources and manpower. Without an operating sponsor, there was little communication between the IS department and executive users.

## Development method

A traditional development method was adopted. The traditional specify-design-build approach is not appropriate to EIS development because it is too inflexible for the changeable nature of executives' requirements. An improved method is the prototyping approach. This provides the ability to create and modify a model of the system before the executives lose their patience (Rockart and Delong, 1988; Plein, 1989; Volonino and Robinson, 1990; Wetherbe, 1991).

## Lack of flexibility

In summary, the EIS was inflexible. Perhaps more flexibility could have been incorporated (e.g. it would have been easy to provide a what if facility). Obviously, a prototyping development methodology would have been an improvement. Even so, it is difficult to see how the contradiction between pre-specified requirements and the need to cope with spontaneity, ambiguity, flexibility, ease of use and so on, could have been resolved with a system of this type. The internal company inquiry came to similar conclusions.

## Epilogue

Thus far, this story contains similar lessons to those of other documented cases. The internal investigation of the EIS had, in fact, been stimulated by a wider study of information requirements throughout the company by an office automation committee. This was led by an assistant vice-president and had representatives from each department. It soon became clear that most departmental information requirements were already met by the EIS. Once this had been realized, the next step was to open up the EIS to staff throughout the company. It was also renamed, 'Everyone's Information System'.

## Everyone's Information System

The EIS was duly extended throughout the company, following a number of technological improvements. The old system had reflected the technology and perceived EIS use of the time when it was developed. It resided on the mainframe and interaction was via one of six dumb colour terminals, which were dedicated to senior executive users. With the change of perception to everyone's IS, the user base was redefined and the number of access points was expanded by providing links to 1000 dumb terminals and several hundred IBM PCs. In addition, managers and staff users of the IBM PCs were given a graphical interface.

## Modifications to the EIS

Everybody's Information System was a modification of the original EIS. It resided on an IBM 3090 mainframe, used essentially the same file structure and employed much of the original code, even though the original mainframe and its operating system had, by then, been replaced. The new system offered a true drill-down capability by incorporating links to management IS and to the hierarchical database (IMS) supporting daily transactions. These linkages made use of existing database query procedures that were originally developed to generate the MIS report files and to permit ad hoc MIS queries. In this way, the additional development effort was minimized and yet the new system offered the capability of drilling down through nine hierarchical levels. Figure 2 shows the system architecture and how the EIS was linked into the existing management information system.

Added security mechanisms were installed because of the very wide user base. File transfer functions were also developed and were offered on the main menu of the new EIS. Under security control, reports were made accessible by on-line inquiry (i.e. using a networked PC or terminal). Data interchange between PC and mainframe or between PCs was made possible. Thus, with the permission of the data owner, DSS report files residing on the PC of one department could be transferred to the PC of another department.

Users of PCs were offered additional graphics capabilities, as follows. Source data files, kept on the mainframe system for ease of maintenance, would be transferred to the PC across the communications network. A presentation module, resident on the PC, would receive the data and the user would select the appropriate graphic function for display of the information. Evidently, users with dumb terminals were not offered this graphics facility. Finally, word processing tools were introduced that allowed on-line keyword search and retrieval or browsing of text documents on the mainframe. The technological characteristics of both the old and new systems are compared in Table 1.

![](/api/attachments/YFAZB3RU/fulltext/images/9e1dcd002227f1b660e8c9ca5523abb11b392bfcea597cd449d605b8516ea6c5.jpg)  
Figure 2 Architecture of the new EIS and its links to MIS

It would have been possible at that time to have bought an off-the-shelf solution but in-house development was chosen instead. There were two reasons for this. First, timeliness was very important. Among the wide user group were many managers whose critical information requirements included current production, inventory and summary shipping data (e.g. for rush orders). Therefore it was necessary to update two files, namely the operational detail and the EIS summary, in one transaction. Most bought-in EIS products could not have provided a function to communicate with the on-line real-time transaction processing system (IBM CICS, in this case). Second, there already existed a highly integrated MIS and, by modifying the EIS, it was possible to make use of this and to ensure that all file structures and contents remained essentially unchanged. The only additions were links from the EIS files to the MIS detail files (or IMS/

Table 1 Comparative technical features of the old and new EIS

<table><tr><td>Feature of system</td><td>Executive Information System</td><td>Everyone&#x27;s Information System</td></tr><tr><td>Mainframe</td><td>IBM 4381</td><td>IBM 3090</td></tr><tr><td rowspan="2">Operating system</td><td rowspan="2">DOS/VSE</td><td>MVS/XA</td></tr><tr><td>PC: PC DOS</td></tr><tr><td rowspan="2">Software</td><td rowspan="2">CICS, COBOL</td><td>CICS, COBOL</td></tr><tr><td>PC: graphical software</td></tr><tr><td rowspan="2">File</td><td rowspan="2">IBM VSAM</td><td>IBM VSAM</td></tr><tr><td>IMS/DB</td></tr><tr><td>Users</td><td>Six senior executives</td><td>All staff</td></tr></table>

![](/api/attachments/YFAZB3RU/fulltext/images/28e2e0776d8c7726308fa2d1bcbc59a6b91d0e2105757d4eebcbaaa62b98ec33.jpg)  
Figure 3 Daily queries to the EIS data base. The number of daily queries was observed closely in the months indicated (columns). Other values are estimates (■)

DB). As noted above, the query functions to the MIS database were those already in use for daily operations.

## Use of the new EIS

Everyone's Information System was implemented in November 1991 with startling results. Queries to the EIS database immediately shot to 3000 daily. By April, 1992, these were running at an average of 7000 daily. Not only did their number rise sharply in June as people responded to the information demands of the accounting year end but it remained high once users had discovered the value of the system (see Figure 3).

On reflection, it is easy to see why this was so. Most of the reasons for executives not using the EIS do not apply to lower levels of staff. As already explained, this organization has a high level of IT already implemented, so staff are computer literate. With a wide user base, many more people benefit from the system and maintenance and developments costs are more easily justified. For example, paper-based MIS reports have been largely eliminated since this information is available on-line. Functional departments have a narrower focus of interest, managers' targets and performance measures are more stable and requirements are easier to specify. The pre-determined database structure maps onto the routine queries of lower-level staff. Senior executives still turn to their subordinates for information and now can expect that information to be delivered more efficiently. Follow-up interviews by the company's IS department with users have confirmed the wisdom of this change.

## Conclusion

Friend (1990) was the first to suggest that EIS ought to mean ‘everybody’s information system’. However, he envisaged a different development path. In his view, a successful executive IS would spread to a successful system for everybody. That type of development history is indeed possible (see, for example, Cottrell and Rapley, 1991). We have described a very different experience. The EIS failed as a system for senior executives, since it was almost certainly not appropriate for them in the first place. However, it did supply vital corporate information in a form that was appropriate for lower level staff.

In a recent paper in this Journal, Holohan (1992) reported on a survey of over 20 UK and Irish organizational users of executive IS and was unable to find one organization that had modelled its EIS on its business strategy. This result is unfortunate if one takes the conventional view that current EIS can effectively support strategic decision makers. It is not a surprising result, however, if one sees current EIS as support tools for lower-level managers.

In the case described here, expanding the system to everyone not only justified its cost by spreading its benefits to a wide range of users, but also made the human information suppliers more efficient at servicing senior managers. Thus it is still true to say, following Rockart and Delong (1988), that any successful EIS must prove to be more responsive than a human. We believe that most current EIS technology, as typified by this company's system, is a tool for lower levels of management and administration.

## References

Barrow, C. (1990) Implementing an executive information system: seven steps for success. Journal of Information Systems Management, 7, 41–46.

Burkan, W.C. (1989) Wringing every last dollar from your DSS/EIS investment. DSS 89 Transactions (The Institute of Management Sciences, Providence, RI) pp. 5–9.

Cottrell, N. and Rapley, K. (1991) Factors critical to the success of executive information systems at British Airways. European Journal of Information Systems, 1, 65–71.

Evans, W.F., Gray, P. and Rhodes, J.E. (1989) Executive information systems for manufacturing: a case study. DSS-89 Transactions (The Institute of Management Sciences, Providence, RI) pp. 46–52.

Friend, D. (1990) EIS and the collapse of the information pyramid. Information Center, 6, 22–28.

Gulden, G.K. and Ewers, D.E. (1989) Is your ESS meeting the need? Computer World, 23 (July 10), 85–91.

Holohan, J. (1992) Use of executive information systems in measuring business performance. Journal of Information Technology, 7, 177–186.

Isenberg, D.J. (1984) How senior managers think. Harvard Business Review, 61, 81–90.

Mintzberg, H. (1973) The Nature of Managerial Work (Harper and Row, New York).

Mintzberg, H. (1976) Planning on the left side and managing on the right. Harvard Business Review, 54, 49–58.

Mohan, L., Holstein, W.K. and Adams, R.B. (1990) EIS: it can work in the public sector. MIS Quarterly, 14, 435–448.

Plein, H.R. (1989) EIS at PCA. DSS-89 Transactions (The Institute of Management Sciences, Providence, RI) pp. 25–28.

Preedy, D. (1990) The theory and practical use of executive information systems. International Journal of Information Management, 10, 96–104.

Rockart, J.F. and Delong, D.W. (1988) Executive Support Systems (Dow-Jones Irwin, Homewood, IL).

Schenk, K.D. and Vitalari, N.P. (1990) User initiation and participation in the implementation of the executive information system: a case study. DSS-90 Transactions (The Institute of Management Sciences, Providence, RI) pp. 173–185.

Volonino, L. and Robinson, S. (1990) The experiences of Marine Midland Bank in sustaining an EIS. DSS-90 Transactions (The Institute of Management Sciences, Providence, RI) pp. 164–172.

Wagner, H.M. (1988) A global language for business strategy. Operations Research, 36, 797–803.

Watson, H.J. and Glover, H. (1989) Common and avoidable causes of EIS failure. Computer World, 23 (December 4), 90–91.

Watson, H.J., Rainer, R.K. and Koh, C.E. (1991) Executive information systems: a framework for development and a survey of current practices. MIS Quarterly, 15, 13–30.

Wetherbe, J.C. (1991) Executive information requirements: getting it right. MIS Quarterly, 15, 51–65.

## Biographical notes

Frederick P Wheeler, PhD is Chairman of the Doctoral Programme in Management at Bradford Management Centre. His research and consulting interests include the theoretical and practical aspects of decision support technology and IS for strategic planning and control.

Shyh Ho Chang holds BS and MS degrees in computer science and is a Senior Auditor of a leading steel company. Currently he is on sabbatical leave as a PhD candidate at the University of Bradford Management Centre. His previous posts have included IT manager of his present company and also a senior management position in the public sector.

Ronald J Thomas, PhD is Senior Lecturer in the Department of Computing, Bradford University. He has extensive experience in systems analysis research and also has research interests in the area of computer-aided learning.

Address for correspondence: Dr Frederick P. Wheeler, Management Centre, University of Bradford, Emm Lane, Bradford, BD9 4JL, UK.
