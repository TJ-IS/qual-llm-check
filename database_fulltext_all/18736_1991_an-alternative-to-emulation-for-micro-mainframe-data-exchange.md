---
otero_id: 18736
otero_key: "SQ8EFG7K"
title: "An alternative to emulation for micro-mainframe data exchange"
authors: "Charlotte S. Stephens; Charles A. Snyder"
year: "1991"
journal: "Information & Management"
doi: "10.1016/0378-7206(91)90048-7"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Case Study

# An alternative to emulation for micro-mainframe data exchange

Charlotte S. Stephens

and Charles A. Snyder

Department of Management, Auburn University, Auburn, AL 36849, USA

The exchange of data between the dispersed units of a business has become a significant part of the modern organization's IRM environment. Moving quickly from a generic description of the issues associated with the business environment of the 1990's, the paper focuses on a specific Fortune 200 manufacturing firm, its organizational structure, and the responsibilities of a centralized Technical Services group.

After an assessment of overall requirements for interactive and batch mode data exchange, the Technical Services group determined that emulation did not meet criteria of security, flexibility, and economy for batch mode exchange. Therefore, the group developed a customized “gateway” solution, using commercially available components whenever possible. Examples of this solution’s applications are given and the resulting benefits discussed.

The important message is to introduce the “best” technology to solve a business problem only after the problem and the long range impact of a solution are understood, not by selecting a solution based only on commercially available products.

Keywords: Information Resource Management, Micro to Mainframe Link, Emulation, File Transfer, Data Communications.

![](/api/attachments/SQ8EFG7K/fulltext/images/71d9e698ce2c66d3e079668f567a1bf2b8fc06093f30f75fbbaa2137a4cd1936.jpg)

Charlotte Stephens is an Assistant Professor of Management at the Abbott Turner School of Business, Columbus College, Columbus, Georgia. She has over ten years experience in operations management, industrial engineering, and information systems with two major textile companies, Milliken and Co. and WestPoint Pepperell. Current research interests include cooperative processing, data communications, information resource management, and the role of the Chief

Information Officer. Ms. Stephens holds an MBA from Auburn University and a BA from Georgia State University. She is currently completing the Ph.D. in Management (Concentration in MIS) at Auburn University.

## 1. Introduction

During the 1980's, businesses have become more geographically dispersed, have reduced layers of management, and have moved toward decentralization. According to Tom Peters, “In 1987, and for the foreseeable future, there is no such thing as a ‘solid’ or even substantial lead over one’s competitors. Too much is changing for anyone to be complacent” [15]. The 1990’s are expected to bring an “evermore interconnected world … even more decentralization” [6]. The hierarchical, military model’s span of control is becoming what Quinn has called a “span of communications.” Peter Drucker has likened the “new organization” to a symphony orchestra and called it the “information based organization” [4]. Hammer finds that the availability of information is the agent for “moving power down an organization’s hierarchy” [7]. Robert Waterman asserts that renewing companies will view information as their main strategic advantage and flexibility as their main strategic weapon [19].

This changing business environment has been paralleled by the growth in end user computing, particularly in microcomputer usage. For information systems managers, the “current and anticipated increase in user computing activity” has exacerbated “three major operational problems for MIS management: satisfying end-user demands for appropriate computing equipment, supplying the necessary data items, and providing the capability for local area and long-haul information exchange” [5]. These problems are bringing data communications issues to the forefront of information resource management (IRM). According to Howard Anderson, Managing Director of the Yankee Group, “What happens is that people put in PCs, workstations, file servers, and all of a sudden the need for data communications explodes” [1].

![](/api/attachments/SQ8EFG7K/fulltext/images/6d8015c5290d3effc8e5350a43583e003731d0a69b827a76d36e3a0b1b38e063.jpg)  
turing, and systems analysis and design. He has published in Information & Management, the Journal of Management Information Systems, the Academy of Management Review, the International Journal for Man-Machine Studies, and many others. Dr. Snyder is a member of SIM, ACM, DSI, APICS, and several other regional, national, and international professional societies.

Decentralized computing is “sweeping business like a wave rolling onto a beach. Its advance is unstoppable,” according to John Donovan [3]. He cites the economic advantage of microcomputers versus mainframes: \$200,000 per mip (millions of instructions per second) on the mainframe versus \$4,000 per mip on a microcomputer. He finds that software costs can be similarly compared. Yet exploiting this advantage has a hazard: hundreds of isolated applications – what I call information islands – unable to share data.” Donovan describes the mutiny among users when IS management tries to resist decentralization. He predicts that information management must become network management with guaranteed network security and consistent, easy-to-use, standard interfaces.

Robert Reich, speaking at a conference on “The Elusive Payoff of Information Technology,” identified three contradictory strategies for information technology: speed, flexibility, and customization [11]. According to him, important issues are whether to build toward some anticipated standard, pick generic, commercially available solutions, or provide a proprietary solution.

While business and information managers recognize the environmental, organizational, and data communications changes, these prescriptive strategies may be difficult to translate into real projects with the proper impact on the organization. Placing the problem and effective solutions in a specific context may be a useful complement to prescriptive strategies. Thus, the purpose of this paper is to examine a particular information management situation where an innovative mindset led to a solution characterized by speed, flexibility, and customization and which selected the appropriate mix of standard, generic, and proprietary alternatives. More important, as a result of the project the company became more adaptable because of the increased flexibility of the data communications function and IS responsiveness.

![](/api/attachments/SQ8EFG7K/fulltext/images/6077dd72a759beda2a4c4c1864e399f1dded679e38b81e23688cc5a145c61ed4.jpg)  
Fig. 1. Organizational Structure. A Divisional Structure By Product.

## 2. A Case in Point

This Fortune 200 manufacturing firm employed approximately 40,000 people in twenty states and three international locations. Sales were in excess of \$2 billion per year. In the past eight years, the company's operating environment changed drastically and it responded by changing strategies and redefining its mission. With global competition and the impact of imports, the company became more aggressive and sought a higher public profile. Instead of a focus on efficient manufacturing, the focus shifted to marketing quality brand products in the domestic and international market. The organizational structure is shown in Figure 1.

The company was organized into five product divisions, all exercising considerable autonomy. Each had its own information systems (IS) management group, with a corporate IS group responsible for corporate finance and human resource systems. Although each division IS Manager reported to the Corporate Director of Information Systems, division management participated in performance evaluations and wielded considerable influence over the activities of the division IS group. In reality, the IS group's organizational structure, depicted in Figure 2, was a matrix organization.

![](/api/attachments/SQ8EFG7K/fulltext/images/7c5a1b53e514793a0edeed7ecb7272cc54ad307c0ebde51f3c92f7bec51dfde8.jpg)  
Fig. 2. Group Organizational Structure. A Matrix.

The Technical Services group located at the Corporate Information Management Center was responsible for the data communications network. Therefore, this group participated in all mainframe hardware/software acquisitions to ensure standards. Because of centralized decision making, many of the organizational upheavals experienced during the previous eight years had minimal impact upon data communications. Although the company had sold some businesses and acquired others, standardization of equipment, operating systems, and network management software had allowed Technical Services to make changes and adapt the network to structural change with relative ease. The corporation's data communications network is diagrammed in Figure 3.

![](/api/attachments/SQ8EFG7K/fulltext/images/a7257d84aad1aa536b1cb4024374a9ac3cb1a0da41673122ca1f5702962d44b6.jpg)  
Fig. 3. Data Communications Network.

A situation which this centralized approval process was not handling with ease was the growth of microcomputer usage. Even as global competition caused some plant closings and stimulated some new businesses, businesses were acquired and sold, microcomputer usage continued to grow steadily. Reflecting on the situation, the Technical Services Manager concluded that the increased use of microcomputers led to two situations, one a dilemma and another, a distinct opportunity for improved resource management:

(1) increased user requests for mainframe to microcomputer data exchange;

(2) the opportunity to minimize the use of mainframe resources for data entry and some processing.

Varied responses to these situations began to occur in the five divisions. For online, interactive modes of query and for file transfer in batch mode, emulation of a mainframe terminal was the conventionally accepted solution [see 13, 12, 18, 2, 8, 9 for examples of this acceptance]. The “data exchange method” involved equipping the microcomputer with a terminal emulator board and emulation software. Then it could be attached to an IBM 3274 cluster controller in the same way as an IBM 3270 terminal. Terminal emulation would then provide the microcomputer with the capability to operate as a terminal and to access data. "Hot key switching" would allow the microcomputer to switch from mainframe to microcomputer sessions. Emulation would provide multitasking capability and purchased communications software and hardware would provide SNA/SDLC (Systems Network Architecture/Synchronous Data Link Control) protocol conversions for sending screens of information between the microcomputer and mainframe. While the microcomputer emulated a terminal, it would require the same mainframe resources as a terminal. Emulation would provide the same query capability as a mainframe terminal and additionally, the capability to download or upload data. Emulation therefore provided a means to exchange data between microcomputers and mainframes. Emulation for file transfer is depicted in Figure 4.

If interactive, online data exchange was required, the emulation solution was appropriate and available from many vendors. However, Technical Services realized that many of the requests for data exchange did not require interactive, online data exchange. Instead, a periodic update of data was needed. Furthermore, many of the opportunities for better mainframe resource usage for data entry were also batch mode requirements for stand alone, remote microcomputers. Technical Services saw this distinction in requirements, online versus batch, as an important one when considering how the increased need for data exchange could best be met. The following three examples illustrate the hazards they faced in their decentralized organization as data exchange needs grew.

![](/api/attachments/SQ8EFG7K/fulltext/images/100b09643afd64f5e30a5bae47f0d719b77760dcfdf8ed67dab0b715fa9a5b78.jpg)  
Fig. 4. Emulation For File Transfer.

Seizing the opportunity to relieve the mainframe resource of some data entry and processing tasks, Division E's IS group provided a BASIC program for plant payroll entry and some payroll processing. Then Division E requested that the corporate IS group generate a program to receive these ASCII files for the corporate finance and human resources system. Formerly, a mainframe file had been transmitted through the mainframe network. Technical Services agreed with the concept of data entry and some processing on microcomputers versus mainframe terminals, but wanted to avoid five different divisional solutions requiring different interfaces.

Division A's accounting group purchased emulation equipment from a local vendor as an “office supply” and demanded that they no longer be charged for an IBM 3270 terminal since they could use the microcomputer equipped for emulation of the terminal. Furthermore, they requested that their emulation capabilities be used for file transfer so that data could be imported from the mainframe to spreadsheets and so that spreadsheet data could be exported to the mainframe, thus eliminating some data entry jobs.

At the corporate level, a telecommunications manager began using a microcomputer to poll telephone switches. Because a mainframe program processed the data collected on switch usage, the telecommunications manager equipped the microcomputer with a mainframe tape drive which had been well advertised. Processing errors were prevalent and drive compatibility problems resulted despite the vendor's continued efforts to correct the problems.

Technical services realized that the problem statement and the criteria for its solution would serve as a guide for the batch mode data exchange project. Data exchange per se was not the problem or the opportunity: batch mode data exchange - exchange on a periodic rather than online, interactive basis - was a problem and offered many IRM opportunities. Technical Services established the criteria for the mainframe to microcomputer data exchange solution.

## 3. Planning for Resource Management

## 3.1. Solution Criteria

The criteria established by Technical Services for a general purpose microcomputer-mainframe data exchange method were:

(1) security - a high degree of security must be maintained during data exchange;

(2) flexibility - to provide a wide variety of applications without requiring extensive and sophisticated programming;

(3) economy - not to increase mainframe and programming resource usage and to incorporate existing hardware and software.

The commercially available solution for moving data from standalone, remote microcomputers to mainframes or vice versa was emulation. Emulation did not meet Technical Services' criteria. Therefore, Technical Services decided to develop a customized solution. This provided significant benefits to the corporation.

## 3.2. Overview of the Solution

Herbert Simon's description of the science of the artificial is an apt description of Technical Services' solution: "the relative simplicity of the interface" is "its primary source of abstraction and generality" [17]. The customized solution for general purpose batch transfer of data used commercially available material driven by a software component from Technical Services. While the details of the solution are proprietary, the concept is elegant and could be implemented in many different ways. Essentially, a microcomputer is used as a gateway for data exchange from microcomputer to mainframe, and in some cases vice versa. The concept is similar to that of a LAN where many users share the emulation capability of one gateway microcomputer. However, here users are not part of a LAN; the link is by modem. Microcomputer users operate with the corporation's standard communications software, sometimes automating the process with microcomputer based DOS batch files and Crosstalk script files. Mainframe users find what appears to be the mainframe network environment. Technical Services' general purpose alternative to emulation for batch mode transfer is shown in Figure 5.

Security was provided for microcomputer and mainframe users for a wide variety of applications. Users were not required to purchase additional, special purpose hardware and software in order to use the data exchange facility. It could be expanded by adding gateways. When IBM's SAA (Systems Application Architecture) becomes a reality, the investment in an interim provision for data exchange will have been minimized.

This alternative to emulation is described by: (1) contrasting emulation with the solution;

(2) describing the solution;

(3) providing examples of the applications;

(4) citing some of the benefits gained by avoiding emulation for batch mode data transfer.

## 4. An Alternative to Emulation

## 4.1. Using Emulation to Move Data

In the mainframe environment, an IBM 3270 and RJE (remote job entry) emulation capability would be required. Both 3270 and RJE emulation make unnecessary demands on the mainframe and the programming staff when an interactive mode is not necessary. Remote Job Entry emulation requires the reformatting of a variety of different file types, because it is formatted for 80 character card images and up to 132 character print lines. To transmit other record sizes, especially larger ones, a programmer has to break the records into multiple parts (80 or 132 character increments). Then these must be transmitted and a program written to reassemble them into the original record.

An interactive protocol is used for 3270 emulation. To use it for file transfer, a program must be written so that the mainframe will accept screen images and write them from the interactive protocol to a file.

A further problem for Technical Services was that emulation of 3270 terminal must take place in the CICS environment. With this, a separate file definition is required for every file format. It uses buffers for the data received. Routines must be written to move the data from them and to write the data to a CICS file with a prespecified definition. If users transmitted the same kind of data or data in the same formats, emulation in a CICS environment would be a more viable alternative. For example, an insurance company or bank might have more homogeneous file formats than this diverse, decentralized manufacturing firm. For them, emulation in a CICS environment with many file formats would require extensive programming support.

If a more general purpose means of exchanging data could be found, CICS could be bypassed and programming resources better utilized. Of particular importance was the fact that the personnel required for CICS programming must be highly skilled and experienced. Eliminating the need for CICS programming became an important objective. Another goal was to save the mainframe time to process the programs required for 3270 and RJE emulation in a CICS environment.

## 4.2. Batch Mode Exchange of Data

Emulation and batch mode exchange of data serve two different purposes. Although emulation will allow transfer of data, emulation is designed for the interactive mode. When the interactive mode is not required for the data exchange application, emulation has two major expenses: for mainframe processing and for programming time required. The main concept of a Technical Services' solution to the overall need for data exchange was to move data whenever possible in batch mode, using stand alone microcomputers.

With batch mode exchange, most reformatting could be performed using a fourth generation language, such as Easytrieve, or microcomputer software, such as dBase. Using batch mode, CICS would be bypassed. The level of programming skill to exchange data was thus lower and programming time was less.

To accomplish batch mode data exchange, a microcomputer was used as a gateway machine, which was equipped for emulation (though not all features of emulation were used). Customized software provided by Technical Services, the TS Data Exchange System, manages the data exchange operation, employing “off-the-shelf” SNA/SDLC protocol conversion hardware and software and the multitasking capabilities of emulation.

![](/api/attachments/SQ8EFG7K/fulltext/images/1ddada2a38e1b1831411deba32c7b32ce4de7cea897162c35ff59557dfc615a6.jpg)  
Fig. 5. An Alternative to Emulation for Batch Mode File Transfer.

## 4.3. A Description of the Solution

The TS Data Exchange System manages data exchange between microcomputers and mainframes. Several microcomputer gateways can be used, each one supporting ten modems. Although the mainframe and microcomputer components of the TS system may be combined in many ways, a mainframe must always exist between gateways.

To implement a TS Microcomputer Gateway, the following environment was created:

IBM PC/AT (plans now call for using PS/2's), Quadport AT serial port with expansion.
ITI System One SDLC communications board
ITI ITF3270 communications software,
Hayes V 9600 modems and Hayes 2400 Smartmodems,

MS DOS - microcomputer operating system, TS Data Exchange Software (function request processor, shared function processor, asynchronous port handler).

The Gateway software creates a reference name for files stored, using a different extension for microcomputer and mainframe files. A numbering system creates file names. When file preparation procedures performed by TS Software (EBCDIC-ASCII translation, insertion of carriage returns and line feeds, data packed into 2K blocks) are complete, the extensions are dropped. Although a file may appear on 16 user directories as an entry number, the file is stored once in the data directory. If a file is submitted with multiple routing, a routine loops through user ID directory files posting that entry into each file. When users list files on their directory, they receive a log of file names. When that file is requested and the request completed, the entry on the user's directory file is deleted. If a file appears in no user's directory file, the file is deleted. Periodically, older files are deleted.

The mainframe TS Software supports any standard IBM sequential file format or VSAM (Virtual Storage Access Method) file. The mainframe user could be from an OS/MVS, MVS/XA, or DOS/VSE operating environment. IBM mainframe 43XX and 30XX CPU's are supported with 3705 or 3725 communication controllers or 43XX/ICA if the operating system is DOS/VSE. The mainframe TS Software includes a network manager program and a transfer program. The manager program queues files for transmission to one or more destinations and allows for mainframe user retrieval of files. It also provides for updates to network data definitions and provides status information on transmission. The transfer program scans the file of transfer requests, establishes sessions for transfer and accepts sessions to receive. It provides automatic restart if communications are interrupted, and relays files to the mainframe network management system, Multi-system Networking and Virtual Telecommunications Access Method, if the destination is another mainframe.

Because Technical Services' innovative solution incorporated existing hardware and software into the TS Data Exchange System', training for data exchange is minimized. A microcomputer user wishing to transfer data to the mainframe calls in to the microcomputer gateway using the company's standard microcomputer communications software and a modem. Microcomputer based DOS batch files and Crosstalk script files can be used to automate the process. Once the microcomputer file is on the gateway machine, TS Data Exchange software checks its identity and mainframe destination for security purposes. If cleared, the file is routed to the appropriate mainframe and there, mainframe TS Software automatically activates JCL to run the job which processes the data. If a mainframe job uses TS Software to transfer a mainframe file to a Gateway for a microcomputer user, the microcomputer user can use Crosstalk to receive the file, provided security requirements are met. If a microcomputer user transmits a file to a mainframe user, the mainframe user can use the mainframe network to receive the file. Microcomputer to microcomputer data exchange is also simplified.

Microcomputer users use the TS Gateway as a "store and forward" electronic mail facility, avoiding the inconvenience of scheduling concurrent communications. At the same time, the security of the TS Data Exchange System is provided for these communications. Each user is free to use the highest speed modem available rather than having to transmit and receive at the slower of the two parties' modem rates. Several examples of how the TS Data Exchange System is used should further clarify the description of the Technical Services' Data Exchange System.

## 4.4. Examples of the Alternative to Emulation

The three examples already used to illustrate the need for data exchange (payroll entry/ processing, accounting, and a telecommunications manager) are now revisited and three additional examples provided:

A division human resources manager needed to query a mainframe personnel file, but periodic updates of the file were sufficient for his search purposes.

Five hundred miles from the TS Gateway, a manufacturing facility recorded packed goods data on a microcomputer located on the plant floor. The data collected had to be processed by a mainframe located at the same facility. The data was needed by the mainframe on a periodic basis.

Customers were given user identifications for the TS Gateway so that they could use microcomputers to access mainframe order status information.

## 4.4.1. Eliminating the mainframe terminal: payroll and accounting

Payroll data from several states are now entered on microcomputers and transmitted to the TS Gateway microcomputer with the corporate mainframe indicated as its destination. An “off-the-shelf” software package was purchased for data entry on a microcomputer. This package could be easily customized for different applications. It also allowed for custom definition of the microcomputer’s keyboard and came with key covers for labeling the keyboard to fit this new definition. Thus, proficient 3270 data entry operators did not need to be retrained. If data entry was by microcomputer users, the keyboard was not redefined. Payroll transmissions from micro to mainframe were automated with DOS batch files and Crosstalk script files. The mainframe component of the TS Data Exchange Software submitted JCL upon receipt of the data files. On the mainframe log screen, one can trace the transmission of payroll data files, their receipt on the gateway, and transmission to the mainframe where specific payroll jobs are automatically submitted.

Another example of eliminating a terminal for data entry occurred with the Division A's accountants. They had developed product style standards using spreadsheets and then developed spreadsheets for data entry of these standards. With the TS Data Exchange facility, the data were placed in an ASCII file using a spreadsheet utility for this purpose and a spreadsheet macro. Then the file was transmitted to the TS Gateway and from there, to the mainframe, eliminating data entry from spreadsheets.

## 4.4.2. Polling telecommunications switches

Before the TS Data Exchange solution was available, the Telecommunications Manager had purchased a mainframe tape drive designed for attachment to an IBM PC/AT. The PC/AT was used to poll telephone switches for usage studies. This detailed switch usage data was processed on the mainframe by running the tape from the PC/AT. In addition to transporting the tape from the Telecommunications office to the Corporate Information Management Center, loading it, submitting JCL to process data upon receipt of the tape, processing the tape was seldom a trouble free operation.

With the TS Data Exchange facility, a DOS batch file activated a Crosstalk script file which then transmitted the switch usage data to the

Gateway. Gateway software then transmitted the data to the addressed corporate mainframe where TS Software on the mainframe invoked JCL to process the data. Time, material, and equipment savings resulted from this application. The Technical Services Manager cited this application as an example of the problems which could be avoided when a general purpose method of moving data is available versus having a wide variety of specific applications, each with its own method of data transfer.

![](/api/attachments/SQ8EFG7K/fulltext/images/29a2579910f87713199d707c2c323a6c272a8590a4b2d4c5310f7cdb5e6c3abb.jpg)  
Fig. 6. Human Resources Search.

## 4.4.3. Human resources search

A fourth, descriptive example of the Technical Services Data Exchange facility is the need of the Division A employee relations manager to query a mainframe human resources file. The division extracted data from a Human Resources mainframe file and reformatted these records into a dBase record layout. The formatted file was transmitted from the mainframe to the TS microcomputer gateway where TS Software recognized its microcomputer destination, translated the file from EBCDIC to ASCII, and inserted carriage returns and line feeds. The employee relations manager could then call into the Gateway to pick up the file. Division A's microcomputer consultant provided DOS batch files, Crosstalk script files, and dBase program files to automate the procedure for the employee relations manager. The manager receives the file, it is loaded into dBase automatically, and he is able to use his microcomputer to perform searches, listings, etc. from a mainframe file without requiring mainframe time or special requests of information systems personnel. The IS requirement for this ongoing service to the employee relations manager was simply to provide a program to reformat the file. The process described above is shown in Figure 6.

## 4.4.4. From Micro to Mainframe to Mainframe

A fifth example demonstrates the importance of a widely applicable data exchange facility, one which can be used when the volume of data exchange would not justify the cost of terminal emulation at present. One of the fifty manufacturing facilities used a microcomputer to record goods packed for shipment to customers. These data were also needed by a mainframe system at the same location. To transfer these data to their mainframe, the TS Gateway located 500 miles away was used. The packed goods file was transmitted from this microcomputer to the TS Gateway microcomputer. The destination address was the mainframe at the manufacturing facility. The TS Software on the gateway transferred the file to the corporate mainframe where the mainframe network, using TS Data Exchange Software for the mainframe, transferred the data to the manufacturing site's mainframe. Both the microcomputer and mainframe Data Exchange Software were used in conjunction with the standard mainframe network management system. While this application took data across the country to go next door, the volume of transmission from microcomputer to mainframe did not justify a gateway at the manufacturing site. Traffic volume was monitored to determine the need for a Gateway microcomputer.

## 4.4.5. Data exchange with customers

The final example of this solution's application is the use of the Gateway by customers to receive order status reports and other approved information. Their access, like that for all users, was limited to files transmitted to their destination code. This access helped to strengthen the ties of the customers to the company, particularly when goods manufactured by the company were components for the manufacture of the customer's product. In these cases, order status was a vital factor in the customer's production planning and the availability of this information gave the company a competitive advantage. Effectively, these customers have become a part of the company's data communications network, providing many of the benefits of backward integration without the capital expenditure. Of course, the implementation of this simple idea for batch mode data exchange provided many benefits, tangible and intangible, to the company as well.

## 5. Tangible and Intangible Benefits

Approximately 100 microcomputers (most of which were already in place for spreadsheet and word processing applications) are now being used for data entry, eliminating mainframe terminals and the mainframe resources devoted to interactive data entry. Technical Services estimated the hardware cost to perform this data entry via emulation would be \$240,000. The additional programming costs and mainframe processing costs which would have been incurred with emulation, although substantial, were difficult to accurately estimate. Development costs for the Data Exchange Software were \$80,000 with the microcomputer gateway costing approximately \$16,000. Even though the tangible benefits of this customized solution were apparent, Technical Services believed the intangible benefits were even greater.

Benefits of TS's provision for batch mode transmission versus emulation included

(1) the reduced level of programming skills required to prepare files for use by the mainframe or by microcomputers after the exchange;

(2) the information systems group's ability to respond quickly to special requests;

(3) increased security for microcomputer file transfer.

With 3270 or RJE emulation, a special request required a special program and therefore, response to the request was slow. In this company's environment, data exchange via emulation required CICS programming. However, with the batch mode solution, the response was much quicker and more cost effective. In contrast to CICS programming, Easytrieve's fourth generation language characteristics enabled less specialized users to manipulate data.

The Technical Services Manager said that the internal EDP auditors loved the Data Exchange System because the gateway software enforced user identification and passwords for microcomputer users and mainframe users alike. Each user can only see and access what is routed to his/her location by user identification. Even if multiple routings of a file are made, only one file exists on the gateway. Only the destination mainframe can invoke JCL to process data received. The system log created by the microcomputer and mainframe Data Exchange Software allowed auditors to trace all transmissions and system activity.

In summary, the solution met all three criteria: security, flexibility, and economy. Instead of having many remote, stand alone microcomputers emulate terminals to facilitate both interactive and batch mode data exchange, a gateway microcomputer with customized software using generic SNA/SDLC and multitasking capabilities was employed for batch mode requirements. Benefits included a significant reduction in the hardware and software cost to exchange data, a reduction in mainframe usage when terminals were eliminated, a reduction in programming skill requirements for data exchange, the ability to respond more quickly to a wide range of data exchange requests, the ability to exchange data with the wide base of microcomputer users including customers, and to exchange data with security requirements met. Furthermore, with IBM's System Application Architecture as the long term plan for data exchange, investment for an interim provision for data exchange was minimized. The company was not locked in to one vendor's proprietary solution.

## 6. Conclusion

Frequently, information resource management decisions are made based on commercially available alternatives. By establishing criteria for the solution of the data exchange problem and its long range impact on information resources, Technical Services was led to develop an innovative solution which used a combination of commercially available products and proprietary developments to provide a better utilization of resources and increased adaptability to changing requirements. TS Gateways can be added as needed and the hardware used for the Gateway can be changed as microcomputer technology advances. Again, the company is not locked in to one vendor's solution.

Technical Services provided data exchange in batch mode with microcomputer users employing their standard communications software and mainframe users employing what looks like their familiar network software. In the words of Donovan, they “guarantee network security and create consistent easy-to-use interfaces” [3]. The TS Data Exchange System is based on “simplicity and self direction,” and required “the development of a customized solution.” The customized, general purpose, data exchange facility provided a quick response to information needs – a company’s main strategic advantage – and flexibility, a company’s main strategic weapon. The economic advantage of the microcomputer is captured without creating “information islands.” Technical Services followed Anderson’s prescription [1], effectively identifying the things they could do well themselves, the things they should never do, and the things that fall in the middle. For the choice between (a) building toward standards, (b) generic or commercially available solutions, (c) proprietary solutions, they chose all three.

An innovative mindset is apparent from the conceptualization of the solution criteria to the implementation of the solution. The wide variety of applications supported attests to the solution's flexibility. The speed with which requests for data can be met attests to its adaptability. Ironically, the customized solution at a corporate level was implemented to minimize customized solutions to data exchange problems throughout the corporation. As Anderson cautions, “The more decentralized your company, the more centralized your communications must be” [1]. Else one of the chief strengths of our information based organizations may quickly become a chief weakness. This paper provides an example of how one decentralized and geographically dispersed corporation reinforced one of its major strengths, centralized management of the data communications network, by providing an innovative solution to the batch mode data exchange needs of its microcomputer users.

## References

[1] Anderson, Howard. "Using Telecommunications Strategically"; Telecommunications (January, 1989), 41–42.

[2] Anderson, Kevin and Bernard, Alan. "Micro-Mainframe Link Options"; Journal of Accounting and EDP, Vol. 3, No. 2 (Summer, 1987), 84–88.

[3] Donovan, John J. "Beyond Chief Information Officer to Network Manager"; Harvard Business Review (September–October 1988), 134–140.

[4] Drucker, Peter E. "The Coming of the New Organization"; Harvard Business Review (January-February 1988), 45–53.

[5] Guimaraes, Tor. “IRM Revisited”; Datamation, Vol. 31, No. 5 (March 1, 1985), 130–134.

[6] Kupfer, Andrew. “Managing Now for the 1990’s”; Fortune (September 26, 1988), 44–60.

[7] Hammer, Michael and Mangurian, Glenn E. "The Changing Value of Communications Technology"; The Sloan Management Review (Winter, 1987), 65–71.

[8] Hannan, James. "A Primer on Micro-to-Mainframe Links"; Infosystems, Vol. 33, No. 2, (February 1986), 32–34.

[9] Mack, Rolf. “Communications: Talking to the Host”; Systems International, Vol. 15, No. 12 (December, 1987), 55–58.

[10] Miller, Glenn. “Micro-to-Host Links: Making Sense of Mainframe Access”; Computerworld, Vol. 22, No. 13 (March 28, 1988), 86.

[11] Neubarth, Michael. “MIS Needs Flexibility As Business Changes”; MIS Week (May 16, 1988), 15.

[12] Nolle, Thomas. "3270 Emulation Becomes a Multipurpose PC-Mainframe Link"; PC Week, Vol. 4, No. 231 (June 9, 1987), C/17.

[13] Ouptill, Bruce. "Micro-to-Host Links: From Emulation to Cooperative Processing"; Network World Vol. 8, No. 3 (January 23, 1989), 39–51.

[14] Peters, Tom. “Restoring American Competitiveness: Looking for New Models of Organizations”; The Academy of Management EXECUTIVE, Vol. II, No. 2 (1988), 103–109.

[15] Peters, Tom. Thriving on Chaos; Alfred A. Knopf, 1987.

[16] Scisco, Peter. "Micro-to-Host Links: Dreams of Access without Effort"; Computerworld, Vol. 22, No. 13 (March 28, 1988), 81–90.

[17] Simon, Herbert A. The Sciences of the Artificial; M.I.T. Press, Cambridge, Mass, 1969, 9.

[18] Walker, Dwayne and Burr, Michael. “Not every Micro-Mainframe Link is the same: The Four Different Ways to Do It”; Computing Canada, Vol. 12, No. 5 (March 8, 1988), 19–22.

[19] Waterman, Robert F. The Renewal Factor, Bantam Books, 1987.
