---
otero_id: 26953
otero_key: "XQSA8BR3"
title: "A Powerful MIS/DSS Developed For A Remote Sawmill Operation"
authors: "J.B. O’Keefe; P.F. Wade"
year: "1987"
journal: "MIS Quarterly"
doi: "10.2307/248672"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
A Powerful MIS/DSS Developed for a Remote Sawmill Operation
Author(s): J. B. O'Keefe and P. F. Wade
Source: MIS Quarterly, Vol. 11, No. 3 (Sep., 1987), pp. 279-290
Published by: Management Information Systems Research Center, University of Minnesota
Stable URL: http://www.jstor.org/stable/248672

Accessed: 28/06/2014 08:35

Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at http://www.jstor.org/page/info/about/policies/terms.jsp

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

# A Powerful MIS/DSS Developed For A Remote Sawmill Operation

By: J.B. O'Keefe
President and General Manager
Juniper Lumber Co. Ltd.,
Juniper, New Brunswick
Canada

By: P.F. Wade
Associate Professor of Decision Sciences and MIS
Concordia University
Montreal, Quebec
Canada

## Abstract

With the widespread popularity and reliability of microcomputers and the availability of easy-to-use application generators and application packages, it has become possible to introduce computer systems into environments where this was not practical either from a technical or an economic standpoint. This paper will describe how an integrated, multi-application system was developed and successfully implemented two years ago for a forest products company. Emphasis will be placed on:

\- How the application generator aided or constrained development.

\- How the development process and system design differed from the traditional approach, in view of the requirement that the system should operate entirely without trained technical support.

Keywords: Management information system, system development

ACM Categories: H.1.1, H.4.0

## Company Background

Juniper Lumber Co. Ltd. is a New Brunswick forest products company combining a woodlands division and manufacturing facility with a production capacity of 50 million board feet of lumber (\$18–\$19 million annual sales value). The company is the only independent sawmill in the province with a Crown License (permitted to carry out its woodland operations on designated government land). Including its own holdings, it has a resource base in excess of 350,000 acres of timber land.

The company directly employs about 160 people and indirectly another 200 through contractors who cut the trees and transport the logs from the bush. There are two mills, some thirty minutes apart, one at Stickney and one at Juniper.

With the exception of a few large sawmill operations which are associated with pulp and paper companies, most sawmills in the province are family owned and managed. Any available capital is traditionally channelled to the mill to improve sawing, grading and handling efficiency. The administrative aspects usually receive less attention. One reason for this is the influential role of operator judgement which pervades the production operations, thwarting efforts for stringent management control $[2, 4, 5]$ .

Before acquiring a majority interest in the company, the President of Juniper Lumber had been with a larger firm which had a mainframe and which utilized more formal planning and control procedures. When he moved to Juniper in 1977 he took with him a strong reliance on daily production, sales and inventory statistics. By 1983 the office staff were under pressure each afternoon to prepare the six packets of reports which had to be ready at 4 p.m. for the line managers. Daily operating statistics were obtained directly from the mills and by radio telephone from the woodland operations. Because of the amount of manual work required, some of the reports were not ready until 11 a.m. the next morning.

All production reporting, order processing and accounting in the company was done manually by a staff of ten clerks, an accountant and a controller in the Juniper office. Juniper is a small town (a post office and two grocery stores), located 90 minutes from Fredericton, the nearest city. Winter storms cause power disruptions and hazardous road conditions, bringing temporary isolation. The closest company is another sawmill some 15 miles away.

## The MIS/DSS System

In the spring of 1983, Mr. O'Keefe decided that the Juniper office should have a computer. He was aware that such a project would involve special risks and problems, as well as substantial costs, but he believed that the potential benefits would justify at least a preliminary study.

Through the company's auditors, he contacted a consultant in Montreal who was familiar with the forest products industry. The initial system to be developed was to account for raw material and finished products from the stump to the customer (see Figure 1). Input transactions included: customer orders, contractor cutting, slashing and trucking activity, production volumes, and saw log purchases from independent cutters. Output included: tally cards (packing slips), invoices, government stumpage (royalty) reports, production reports, contractor settlements and perpetual inventories of raw material (tree length and log) and lumber (rough and dressed). Subsequent phases would extend the system to cover payroll and general ledger functions and forestry planning.

During the consultant's visit a specification book was prepared which included copies of transaction and output documents with estimates of file volumes and input frequencies. No documentation existed regarding the procedures, some of which were highly complex and involved a multitude of wood conversion factors. In many cases the procedures were not standardized, differing by species of wood, finished product, contractor and customer.

There were 25 routine reports associated with the operations to be computerized. These were filed in the specification book under three headings: daily, weekly and monthly reports. Each was reviewed with the accountant and the manager concerned. Annotations were made regarding calculations involved, how the report was used, and requested modifications.

The president requested the consultant to analyze three questions:

1. Was such a system feasible?

2. If it was, how much would it cost (a rough estimate)?

3. Would the benefits justify the cost?

At this point, the consultant had a fair idea of what was required from a conceptual design standpoint, but the costs for developing the software were hard to estimate. It was clear however, that they would be substantial.

![](/api/attachments/XQSA8BR3/fulltext/images/fdbf2d39ea20a5119168788feb7c85ed687e64e27f9e11158e574d3d7e1ef08f.jpg)  
Figure 1. Functions of the Proposed System

Even if the estimated software costs were considered acceptable by the client, there was additional concern about the technical feasibility of providing a system which could be operated in a severe environment by non-technical staff who were several hours away from software support and hardware maintenance personnel.

The consultant's answers to the three questions then were:

(1) Yes, he believed that technology had probably advanced to the point that such a system was practicable, but he proposed that a short feasibility study be carried out to confirm this.

(2) The estimated cost seemed reasonable.

(3) It was very difficult to determine whether the benefits would justify the cost since benefits would appear to be mainly intangible.

The question of cost justification is always a difficult one to resolve $[3]$ . In this case, benefits were perceived to be more managerial than clerical. There was no stated objective of staff reductions; instead there was a general desire for improved analysis and control capabilities. It was also felt that the heavy reliance on one or two key individuals to supervise complex, undocumented procedures was undesirable.

## Feasibility study

It was obvious that this would be a demanding project. It had the complexity of a multi-application mainframe system without the same budget and with the added requirement that it must be run completely by the users. And while many mainframe applications and microcomputer packages are in a state of continual upgrading, the Juniper Lumber Information System (JLIS) was going to be a one-shot installation with 'hooks' for future expansion. Since it would be a custom system, there were no automatic system updates.

The particular operating environment also presented some special requirements:

\- The Canadian government had embarked on a program to convert from imperial to metric measure. At Juniper perhaps a quarter of the system had already been converted. The JLIS would have to work in either one, or both, sets of units.

\- Some years earlier the provincial governments had changed their methods of scaling (estimating wood volumes) from measuring the logs (conventional method) to measuring the stems (tree length method). Both of these methods had to be accommodated within the system.

\- Because of differing practices related to customers and wood species, a wide variety of computational procedures were employed for various customer, contractor, wood species and product combinations.

\- The complex scaling and computation procedures were not documented. (However, from previous experience the consultant was familiar with many of them.)

The main concern, however, was the practicality of developing a computer system which could run itself despite power interruptions and user error. How quickly could the staff get used to mechanization and its idiosyncrasies? As envisaged there would be a two to three week on-site training/conversion period and then the staff would be on their own.

It was clear that a microcomputer would be able to handle the necessary volume of processing and data entry (see Table 1). A more expensive minicomputer was eliminated from consideration because: (1) it was believed that the range of high quality, inexpensive business software on the market in the future would be greater for microcomputers and (2) we had decided that the installation of two identical configurations would reduce the impact of equipment failure.

## Table 1. Processing Volumes

## File sizes

100 customer/location/product records
350 contractor/location/activity records
500 product/location records

Transaction volumes

200 cutting cards per week
25 lumber orders per week
250 contractor movement slips per week
10–20 lumber production lots per day

Decisions regarding software acquisition/development were not so easy.

Microcomputers had just begun to impact the business market. The IBM-PC was introduced in 1981 and the IBM-XT (with a 10 MB hard disk) in 1983. Lotus 1-2-3 made its appearance in 1982, gradually replacing Visicalc in popularity, and by 1983 a large proportion of microcomputer sales were associated with the application of spreadsheets [1].

Was software technology sufficiently advanced that the company could be encouraged to proceed with a project of this nature?

Only a limited number of database languages were available. Application generators such as FOCUS would appear only the next year. BASIC was the accepted procedural language for custom software. The idea of developing a custom, multi-application system on a micro using a fourth generation language would have been considered novel and probably not very feasible.

It did not take much further thought to decide that programming such a system in a language like BASIC, while possible, could not be justified economically. For example, too much time would be required to develop custom entry screens with advanced cursor control and error handling. DBASE II was considered too difficult for interpretation and modification by staff.

With the help of the accountant, we planned to use a non-procedural language to develop command files which would capture the required accounting procedures. There was not much time, however, for a protracted investigation of available packages because the client was waiting for a recommendation regarding project feasibility.

In May we learned of an application generator, APG, developed by XRT, a software house in Philadelphia. This package had not been distributed commercially since it was used by XRT themselves as a system development tool. Originally developed for minicomputers, APG had been converted to run on the PC and seemed to have most of the features we were looking for with the exception of an import/export capability.

After spending some time with XRT, we decided that the package should be able to handle the required functions. However, it was recognized that we were going to be extending APG to its limits. Our intention was to use the “Report Writer” for as much of the processing as possible so that the client could then make minor alterations and develop new reports without outside assistance. It was recognized that the list-type format would not be suitable for some of the reports and custom programming would be required.

Even though at this point the consultant had no ‘hands on’ experience with the package and our design requirements were far from complete, we were confident enough to recommend that a prototype be developed using APG to test the approach.

A three-phase work program was proposed which would allow the company a mid-project bail-out point.

<table><tr><td></td><td>Development and Implementation Cost %</td></tr><tr><td>Phase 1—Prepare Prototype</td><td rowspan="10">40</td></tr><tr><td>Become familiar with APG</td></tr><tr><td>Prepare tentative design for data base</td></tr><tr><td>Develop prototype to produce selected reports</td></tr><tr><td>Review and Decision Point</td></tr><tr><td>Demonstration for Juniper management</td></tr><tr><td>Approval to proceed with:</td></tr><tr><td>• Equipment purchase</td></tr><tr><td>• Software license</td></tr><tr><td>• Remainder of development</td></tr><tr><td>Phase 2—System Development</td><td rowspan="3">48</td></tr><tr><td>Complete ‘programming’</td></tr><tr><td>Prepare documentation</td></tr><tr><td>Phase 3—Implementation</td><td rowspan="3">12</td></tr><tr><td>Train staff</td></tr><tr><td>Enter inventory data</td></tr><tr><td>Phase out manual system</td><td>100%</td></tr></table>

The client was advised that the project would be subject to special risks because of its unusual nature. The proposal was accepted.

## Phase 1—Prepare prototype

As envisaged the system would consist of a set of independent modules, microcomputer-based and sharing data where necessary through import/export facilities. The nucleus would be the custom module being developed in APG. Future modules, such as payroll and general ledger functions, would likely be purchased off-the-shelf. Spreadsheet and statistical packages would extend the processing capability for DSS applications. Whether the microcomputers would eventually be connected by a network was a decision left for the future. An obvious disadvantage of this arrangement was the lack of consistency in the user interface, but this would not be a severe limitation if individual operators did not have to use multiple packages.

The next step was to establish some design objectives. Seven desirable, if not mandatory, goals for the JLIS were defined:

\- No technical staff should be required to operate or support the system on a daily basis. This implied ease of use, good input screen design, and tolerance of user mistakes, preventing them when possible, and allowing easy recovery.

\- The system should be available when needed and relatively invulnerable to power bumps and disruptions. This called for robust hardware, capable of operating in a range of temperatures, and accessories to prevent problems caused by power disruptions.

\- The company should be as independent as possible from the consultant. This entailed software enabling the company, without outside assistance, to add customers, products, mills and shifts to files and reports. It should also accommodate the conversion of measurements from imperial to metric units, and permit the generation of ad hoc reports when required.

\- The system should allow for analytical studies using processed transactions. This meant incorporating simple procedures to archive and retrieve posted transactions. As well, each transaction record would have to be self-contained (for example, the “order line item” record would also contain price, cost and shipping details).

\- The system should be expandable without major expense or changes to equipment or software.

\- The system should be adaptable to procedural anomalies and changes. For example, it should be able to accommodate different procedures for the same function, e.g., one contractor can be paid on a different basis than another.

\- It should be reasonably probable that hardware and software suppliers would still be in business five years later.

In terms of functions to be performed, the JLIS was expected to duplicate the output of the existing manual system. However, in view of the effort and expense which were being invested, it seemed that the elements included in the database should permit expansion to meet the foreseeable needs of management.

Formal planning approaches are well documented. In our case, however, these did not seem appropriate considering the company's size, the client's expectations, and the size of the project. We did follow some of the more useful steps such as the identification of critical success factors.

It was determined that the major factors affecting the profitability of Juniper Lumber Co. were:

\- the costs, size and species of sawlogs produced and purchased, and

\- the success of the mill in maximizing the value of output (grade and size of dressed lumber) for the given sawlog input.

The JLIS database should provide indicators to monitor the above critical success factors, as well as produce the required reports.

In late July, the president and his management team attended a demonstration of the prototype system. The test went well and approval was given to proceed with the remainder of the project. The target date for implementation was set for October.

## Phase 2—System development

Before completing the design of the database, it was necessary to decide where the Report Writer could be used for report generation and masterfile updates. The Report Writer presented three constraints (1) only two files could be used simultaneously, (2) each record, or pair of linked records, was processed independently (i.e., there were no global variables other than 'total,' 'average' and 'count'), and (3) the reports produced were lists without programmable headers or trailers. A main consequence of the above was that all of the necessary factors and base variable values had to be present in the two linked files.

The Report Writer was used for about 80% of the processing but doing so made the record layouts more complex than desirable. Figure 2 shows screen #1 of the Contractor History file. Some of the many conversion factors involved in the calculations can be seen.

When the database design reached the stage of 85–90% completion, we worked with the accountant to clarify the calculations and factors required to duplicate the current procedures. The associated files were created in APG, sample data were entered, and a Report Writer command file was prepared and run. The process was repeated until the output was considered acceptable. The coding structure was developed at the same time using mnemonic abbreviations.

By the end of October, changes to the data files and the Report Writer command files were decreasing in frequency and the custom reports were nearing completion. For a variety of reasons it was decided to move the implementation data to January. However, an

IBM-XT was delivered to Juniper in November for training purposes.

## Finishing Touches

Before implementing the system at Juniper, three tasks had to be completed:

\- All possible problems that could arise with the system were identified and means devised to prevent them. If this could not be done, then efforts focused on minimizing the impact and developing instructions for client recovery. An example of this analysis is given in the Appendix.

\- DOS command files were constructed for tasks such as backing up and archiving.

\- The user manual (by now 200 pages) was completed and tested on non-technical personnel.

## Phase 3 – Implementation

The consultant and the programmer began staff training and supervising the conversion in the latter half of January. Because the accountant had been exposed to the system during the prototyping sessions, he was able to take charge almost from the start. The three members of the staff responsible for the activities to be mechanized were shown how to enter and modify data. These were the most frequently used functions. At the beginning, the accountant initiated all processing runs. However, as the staff became familiar with the equipment, some of these duties were delegated.

![](/api/attachments/XQSA8BR3/fulltext/images/f62c569de6eb28aabe13b55cf3b2efa4bcc26e602c6c522dc3518ebab8f2993f.jpg)  
Figure 2. Entry Screen #1 for the Contractor History File

Five weeks after the conversion had been completed, the accountant decided to accept a job offer from another company. This created some concern since there was no one else with sufficient knowledge of the system to supervise its operation. We returned to train a forestry technician with an interest in micro's. He proved a quick learner and after a week was competent to carry on by himself. (He made much use of the User's Manual during the next six months. This justified the effort spent on its preparation.)

Apart from the detection of some bugs in the special reports, which were described over the phone with the fixes sent by mail, the consultant had no further contact with the system. The acquisition of a spreadsheet package had been recommended and this was mailed in March, together with an instruction manual.

## System Overview

## Hardware

The system consisted of two identical IBM-XT's each with 640K of memory, a 10MB hard disk, and an Epson FX-100 printer. Power was fed to each micro through an auxiliary unit which supplied up to ten minutes of battery power in the event that hydro power was interrupted.

## System highlights

Every member of the office staff was issued an ID and password. The technical supervisor was given a higher security clearance than the others, enabling him to change passwords, edit the Report Writer command files, etc.

Each of the two free standing machines was labelled and reserved for a certain set of file updating and processing functions. Functions which were not dependent on the updated files could be performed on either machine. A schedule was prepared showing when data were to be entered for the various transaction files, and the sequence (where important) of the daily, weekly and monthly runs.

After entering the ID and password, the user views the Executive Menu (see Figure 3). The Data Entry and Display function is menu selection #1, Report Writer-processing is selection #2. The Special (Custom) Reports menu is displayed with selection #3, etc. The sub-menu for Data Entry shows the Directory of Files (see Figure 4) from which a selection can be made.

Processing runs can be selected from the Report Writer Directory Screen (Figure 5) or the menus of Special (Custom) Reports. The import/export routines which were developed later are also accessed from a Special Report menu.

Each day, data are entered following a flexible schedule. At 3:30 p.m., data entry starts for the daily management reports. Tally sheets showing the production of rough and dressed lumber are sent by hand from the mill, and woodlands data are sent over the radio telephone. The processing runs are made and by 4 p.m. management is provided with reports by day, week to date, and month to date, covering sales, production and mill downtime. Current inventories of dressed lumber by product group are also reported.

![](/api/attachments/XQSA8BR3/fulltext/images/94e17916162e0deac33803364a7db26487b61f818fa2c1ce8b29c5f73bc93def.jpg)  
Figure 3. Executive Menu of JLIS

![](/api/attachments/XQSA8BR3/fulltext/images/443835fc503ff04a5e5354f78d71c99c754eaad4f72115821086391d064800d5.jpg)  
Figure 4. Directory of Files for JLIS

The final step for the day is the file exchange and backup. Every night the files in the two computers are brought into line. Data files altered in Machine #2 are backed up on one or two diskettes and copied to Machine #1. Then, the two reports using these files are run on Machine #1. Afterwards all of the data files from Machine #1 are backed up (5 to 8 diskettes depending on the season) and copied to Machine #2. The diskettes are then carried off-site for storage.

![](/api/attachments/XQSA8BR3/fulltext/images/75dadc5dd4f778eaa3f45d0c41dbbfd0207603179a8d2408d0bfbc776c7a665a.jpg)  
Figure 5. Directory of Report Writer Command Files

## Juniper Lumber Co. Revisited

In the spring of 1986, two years after the initial contact, a visit was arranged for the consultant to review the system. We found that the system had not remained static. A payroll package and two additional hard-disk IBM-compatible microcomputers had been acquired.

The spreadsheet package was being used extensively—too extensively as it turned out, because parallel inventory records were being maintained in spreadsheet files and in the original system. This had come about because users found the system's entry procedures for production data too slow to meet the 4 p.m. deadline. (This deficiency is now being examined.)

In other respects, the system was operating exactly as planned. Archived data was being analyzed using the spreadsheet and export routines. Backup files were faithfully being transported off-site each day and the original schedules for the processing runs were being followed with only minor alterations.

The equipment utilization (one shift only) was as expected. At peak-time, the #1 unit was being used 90–100% of the time, whereas the #2 unit, including now the weekly payroll, was used only 50% of the time. The present archiving policy kept the total storage requirements to less than 6.5 MB.

The equipment has performed flawlessly (no malfunctions or repairs in two years of continuous and heavy operation). We suspect that some of this may be due to the filtering effect of the backup power supply units. While a carry-in maintenance contract had been purchased for the first year, this had been allowed to lapse. The equipment received no preventive maintenance attention for two years except for drive head cleaning. Doubtless, the printers should now be oiled.

Two major changes had occurred in the Juni-per operating environment:

\- Because of productivity improvements in the Juniper mill, the Stickney mill had been closed.

\- A retail lumber yard had been opened at Stickney.

These changes had created no problems for the system.

The forestry technician, now the data processing manager, was the only one in the office who knew how to use the Report Writer to generate a new report. Other employees could enter data and initiate runs, but most would have been hesitant to operate in DOS, (to copy a diskette, for example). The exception to this was the main operator who was responsible for preparing the management reports and transferring the files between computers. Management personnel did not use the microcomputers directly. (The president recognizes that there has to be a more conscious attempt to distribute computer expertise among the staff because the company is still too dependent on one individual.)

## Impact of JLIS on Juniper Lumber Co.

When the decision was originally made to acquire a computer, the president of the company recognized the risks. He was aware that the idea of using a microcomputer to provide the functions of a mainframe was (at the time) without extensive precedents, and he had heard the usual run of horror stories from business colleagues describing how even less ambitious projects had been unsuccessful. In addition, he knew that larger competitors using mainframes had not mechanized the inventory system to the extent being contemplated. On the other hand, he had a conviction that improved management control was essential in order to remain competitive at a time when lumber selling prices were stable but costs were increasing.

Two years after the system was implemented, the president tried to summarize its impact. "It was one of the best investments I ever made," he claims. He explained this as follows:

"The system was one of the most influential factors in the survival of the company in the lumber business in the face of events occurring in the past two years. The reduced delays in reporting, the increased accuracy of the reports, and the additional information available permitted management to make necessary rapid decisions to remain lean and responsive to the market.

The daily management reports required by 4 p.m. were often not available until 11 a.m. the next morning with the manual system. The new system produced them on time. This had an immediate impact because management was able to diagnose problems before the start of production the next morning at 7 a.m."

One example cited to show the impact of tighter management control related to the distribution of log sizes fed into the sawmill. Each year estimates of sawlog quality are made by measuring a sample of the trees to be cut. The mill equipment is balanced for this quality and production targets are set accordingly (e.g., an average of 38 board feet of dressed lumber should result from each sawlog of input). Should the actual sawlog input quality be significantly different (either better or worse) during the day, productivity will suffer. Consequently it is important that the loader operator in the mill yard consciously select a mixture of logs with the targeted quality. When the daily production report is available before the start of the next day's production, instead of 11 a.m., the mill superintendent is able to take remedial action four hours earlier to correct an inattentive loader operator.

Another example of the impact of faster, more accurate data concerns inventory discrepancies. With the new system, inventory costs were reduced and customer service was improved due to the fact that inventory discrepancy reports were available on the second or third of the month instead of the 20th. Discrepancies previously as large as \$25,000 now rarely exceed \$500.

An over-all measure of the impact of the JLIS may be judged from the improvement in mill yield between 1984 and 1986. In 1984 when the system was developed, the sawmill was producing chips (equivalent to scrap) at the rate of 1.1 bone dried tons per 1,000 board feet of lumber. By 1986, this figure had been reduced to 0.7 bone dried tons per 1,000 board feet of lumber, an improvement in yield of 36%. Some of this is attributable to the new mill equipment, but a significant portion is ascribed to the tighter management control provided by more timely production reports.

The system paid for itself in less than two years as a result of staff reductions. This had not been expected. Two months after the accountant left, so did the controller, and neither was replaced. The office staff has been reduced from ten to six despite the fact that the volume of input data has remained essentially the same and reporting delays have been reduced.

## Reasons for Success

Since the president had decided to implement the system, the staff had a strong incentive to make it work. However, a receptive attitude is not always a sufficient condition for success, especially in the face of recalcitrant technology. What factors helped produce (within budget, but admittedly three months late) a system that performed as planned and was assimilated so easily by the staff?

The first factor was probably a budget that was sufficiently realistic to allow us to do the job properly. Also there were no stringent time pressures. We could, therefore, attend to matters which are often rushed or neglected altogether, such as developing command files for utility functions, removing the sources of potential problems, and preparing comprehensive documentation. (For example, PC-DOS would erase the hard disk if the user forgot to enter the drive designation when formatting a diskette. A patch was put in to prevent this.)

Next, the combination of the reliable hardware and the 10-minute back up power supply eliminated essentially all restart and recovery situations. The only problems experienced were user-entered errors which were corrected by manually editing the field contents in the appropriate contractor, customer or product records. Every record in the system could be displayed and modified by the JLIS database functions.

The company was fortunate to have a capable replacement for the accountant. This individual has shown a strong aptitude for working with the computer and has been responsible for extending its application.

The use of an application generator significantly reduced the amount of programming and testing time in the development process.

This left us more time to concentrate on the design of the database.

Two features of the system design have given the JLIS great flexibility: (1) the fact that it was essentially table-driven has permitted the addition or removal of products, customers, mills and machines, and (2) the creation of a comprehensive import/export facility means that a user can move beyond the restrictions of JLIS by transferring the relevant data to a package with the required functions.

This flexibility has permitted Juniper Lumber to continue the nonstandardized procedures which were the legacy of the manual system and which suited the circumstances, to modify their practices to keep pace with a changing environment, and to use the computer for more sophisticated purposes as they grow accustomed to its capabilities.

Finally, and perhaps most importantly, credit must be given to the Juniper Lumber Co. office staff who adapted to technological innovation with such equanimity. Maritimers are renowned for their independence and self-sufficiency. The JLIS was just another natural challenge to be faced and overcome.

## References

1. Benson, D.H. "A Field Study of End User Computing: Findings and Issues," MIS Quarterly, Volume 7, Number 4, December 1983, pp. 35–45.

2. Clapham, J.C. and Lambe, T.A. "The Sorting of Sawmill Lumber," Operations Research, Volume 11, Number 4, July-August, 1963, pp. 502–517.

3. Epstein, B.J. and King, W.R. "An Experimental Study of the Value of Information," Omega, Volume 10, Number 3, 1982 pp. 249–258.

4. Hehnen, M.T., Chou, S.C., Scheurman, H.L., Robinson, G.J., Luken, T.P. and Baker, D.W. "An Integrated Decision Support and Manufacturing Control System," Interfaces, Volume 14, Number 5, September/October 1984, pp. 44–52.

5. Van Gigch, J.P. "Applications of a Model Used in Calculating the Mental Load of Workers in Industry," CORS Journal, Volume 8, Number 4, November 1970, pp. 176–184.

## About the Authors

J. B. O'Keefe is the Chief Executive Officer and President of Juniper Lumber Co., Juniper, New Brunswick. He was responsible for incorporating Juniper Lumber Co. Ltd. in 1977. Mr. O'Keefe is also an officer of other New Brunswick companies as well as holding several Directorships. Previously, he was President and Chief Executive Officer of Thomas Equipment Ltd., a division of McCain Foods Ltd. Prior to that, he was an executive responsible for sales and operations in New Brunswick and Quebec for Irving Oil Ltd.

P.F. Wade is Associate Professor of Decision Sciences and MIS, and Director, Faculty Information Systems at Concordia University. His background includes 25 years as a management consultant with experience in the forest products industry. At one time he was Director, Information Systems for Celanese Canada and General Manager of Trans-Canada Computer Utility Ltd. He is the author of two interactive software packages, MER-LIN\* for decision support and QUESTAN\* for survey analysis.

Appendix

<table><tr><td colspan="2">Problem Classes and Remedies</td></tr><tr><td>Type</td><td>Preventive/Remedial Measure</td></tr><tr><td>power disruption</td><td>provide standby power supply with 10 minute back up andensure that all runs are less than 10 minutes in duration</td></tr><tr><td>power cord pulled from socketequipment malfunction</td><td>maintain a printer log of transactions</td></tr><tr><td>no corresponding masterfile record to update during transaction processing</td><td rowspan="2">print message on logapply limit and other checks on entered data.</td></tr><tr><td>error in data entry</td></tr><tr><td>process a run out of sequenceduplicate processing</td><td>try to prevent through use of posting flags</td></tr><tr><td>failure to enter document on data entry</td><td>no check (no batch totalling feature in APG)</td></tr></table>
