---
otero_id: 18110
otero_key: "VKGGQE84"
title: "A synopsis of present day practices concerning decision support systems"
authors: "Denise C. Eriksen"
year: "1984"
journal: "Information & Management"
doi: "10.1016/0378-7206(84)90048-x"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Synopsis of Present Day Practices Concerning Decision Support Systems

Denise C. Eriksen

Business Computer Information Systems Dept., School of Business, North Texas State University, Denton, TX 76203, USA; teleph.: (817) 565-3110

Selecting a decision support system that fits specific needs, both technically and financially, is a difficult task. The marketplace has been flooded with software bearing the “DSS” label. To provide a clearer picture, the article examines a number of popular DSS definitions and its development. DSS are broken into groups with similar characteristics to examine current software and applications. These groups include Personal Support Systems, DSS and Local Area Networks, DSS and Emulation, Timesharing Systems, Commercial Data Base Systems, and Integrated System. Within each group, current software and practices are reviewed. The potential buyer has the opportunity to compare DSS packages and possible applications. In addition, a list of important questions to ask when choosing DSS Software is included.

Keywords: Semistructured Decisions, Effectiveness, Personal Support Systems, Spreadsheet, LAN, Gateway, Emulation, Commercial Data Base Service, Time-sharing, Integrated System

![](/api/attachments/VKGGQE84/fulltext/images/5974c63a197d6435e274b5334b630cf76c64ff5619c5ef85dd1b4594e4cc5e8a.jpg)

Denise C. Eriksen is currently a M.B.A. student and potential P.H.D. candidate in Business Computer Information Systems at North Texas State University. She also received her B.A. at North Texas State. Her research interests include DSS and data communications. She has worked in industry as a MIS consultant and programmer. She has been an instructor for the IRS in the training of their Computer Audit Specialists.

Ms. Eriksen teaches courses in COBOL and sophisticated debugging techniques. She belongs to the Dallas Chapter of the Data Processing Management Association.

## 1. Introduction

Decision support systems (DSS) is a term used to describe a dynamic field in systems technology; the term began appearing in titles of conferences and research papers in the early seventies. Researchers have defined DSS in various ways, but no single accepted definition has emerged. In fact, there are many new products bearing the “DSS” label appearing daily in the marketplace. Consequently, the object of this paper is to provide the potential buyer with an “overview” of present day viewpoints and practices concerning DSS including specific DSS software and vendor information.

## Decision Support Systems Definitions and Concepts

In 1978, the first book on DSS was published: Decision Support Systems: An Organizational Perspective [19]. The authors, S. Morton and P. Keen, defined DSS to be “the use of computers to:

i) assist managers in their decision processes of semistructured tasks.

ii) support, rather than replace, managerial judgement.

iii) improve the effectiveness of decision making rather than its efficiency."

They used a classification scheme developed by Simon to divide decisions into three categories: structured, semistructured, and unstructured. Structured decisions are those decisions that are procedural and can be automated. Managers need not be involved, because intuitive judgement is not needed. In semistructured decisions, a manager's judgement alone is not sufficient to make a good decision: the problem is either too complex or involves too many computations. The last category, unstructured decisions, involves those that have never previously been encountered, or those in which a process cannot be defined for solving them: these decisions rely on human intuition. Thus, DSS focuses on the semistructured decision process and it is this area that can benefit most from a DSS. Support is provided by way of a data base, models for simulating real-life situations, and a data modeling/retrieving language for accessing the data base.

Refering to the previous definition, decision making effectiveness, not efficiency, is improved. Efficiency is concerned with speed, accuracy, and productivity or “doing things right”. Effectiveness focuses on making a good decision or “doing the right thing”. DSS are then defined as helping managers make better decisions.

Morton and Keen also borrowed a classification scheme from Anthony and Deardon. Anthony and Deardon defined three levels of management activities:

i) Operational Control – concerned with the present; detailed, accurate data; originates within the organization, and performed frequently.

ii) Management Control – concerned with securing all resources needed in order to accomplish the organization objectives.

iii) Strategic Planning – activities concerned with the organization's future. The data is less detailed, less accurate and is often predictions and intelligence about the external world. Here, complex problems arise in a nonroutine manner. [2]

Using Simon's classification for decisions and Anthony's classification of managerial activities, Keen and Morton built a framework for information systems. The matrix was formed from rows of Simon's classification and columns of Anthony's breakdown.

Gerrity [33] took this framework and observed that traditional decision making tends to move from structured/operational to unstructured/strategic planning. Figure 1 illustrates this flow of decision making. Gerrity determined that DSS has its greatest success at the strategic planning level involving a semistructured decision.

In the late 1970's, new technologies made it possible to implement the ideas for a DSS. Advances were made in the cost and speed of computer memories, CPUs, data communications and user interfaces such as color graphics. Software improved in such areas as data base management, planning and query languages. The skills of data processing professionals and management scientists were blended together to make the DSS viable. Alter [1] published a taxonomy of decision support systems in 1977. He classified 56 system then available by the way the output determined the decision; for example, what type of operation did the DSS perform to produce the specific output? Alter's categories include the Accounting Model (which produces financial reports, such as the corporate income statement) and the Suggestion Model (which offers proposed actions for the user). Alter's taxonomy is severely limited because he only reviewed and classified large, corporate-wide DSS. Unfortunately, this is the only taxonomy presently published.

In DSS literature, a distinction is made between

![](/api/attachments/VKGGQE84/fulltext/images/9f055ac4a30471bcdb2c9cfab02bd56ec8d161ba12ec01ddf1d416bedcbdb535.jpg)  
Fig. 1. Decision making flows downward from left to right.

DSS, MIS, and EDP, but the boundaries are ill defined. However, there are several noted differences. EDP systems are application oriented meaning the focus is on manipulating individual transactions at a central facility. The primary interest is data and hardware optimization. MIS differs from EDP in that MIS takes the processed data and attempts to turn it into meaningful information for middle- and upper management users. MIS places the burden of extracting relevant information on the end user. In a DSS, the focus is not on data or information, but on the end product – the manager's decision. Bonzcek [4] says that DSS is an “outgrowth of the MIS area, which in turn stems from data base management.” He believes that DSS is different from MIS because DSS emphasizes the following:

i) incorporating models into the information system software

ii) providing useful information to higher-level management to assist in comparatively unstructured or “semistructured” decision activities

iii) furnishing the system's users with powerful yet simple-to-use languages for problem solving In his review of DSS definitions, he also points out that there is a widespread agreement that the system must possess a query language that is very easy to learn and use.

Today, decision support systems are being integrated with office automation technology. Wagner [31] believes the “Office of the Future” to consist of:

(A) communication technology and information resource management

(B) DSS technology

The first refers to electronic mailboxes and local area networks. The second, will probably outweigh communications technology in its overall impact on the way managers will “manage” their activities.

Wagner [31] provides an optimistic if not futuristic definition of DSS. he explains it as an “intimate coupling with the mind of an executive or manager as a part of his habitual work environment”. There should be no delays or translation processes that would interrupt the individual’s natural concentration patterns. The relationship between the DSS and the manager should be so special that the system actually extends the person’s memory and reasoning powers.

The next section classifies DSS into broad groups based on similar characteristics and methods of interfacing DSS with current data communication technology. This classification has a broad scope: from the single user with a microcomputer to the large corporation with hundreds of users using a large computer system. It is meant to inform the ready of the types of DSS software available and some practical applications using a DSS.

## 3. Types of Decision Support Systems

## 3.1. Personal Support Systems

The first category is personal support systems. This type of system is specifically for a single user interacting with a microcomputer. Software is usually purchased, although some managers write some of their own programs for the microcomputer. The key characteristics that differentiate this category from others are “single users” and “microcomputer”. The software is generally menu-driven and user friendly. Microcomputer software vendors aim at a broad range of skill level in their users, so they must provide user-friendly products. On the other hand, current DSS software designed for large computers is aimed at a smaller market of dedicated users who may be more familiar with computers or have a backup support team of computer specialists. Personal support system software emphasizes ease of use. This software is relatively inexpensive – a package may range from \$29 to \$750 depending on the application and device. It normally employs graphic interfaces, and vendors sometimes have touch screens with color.

The types of decisions that are supported are varied but are limited in size. Because of storage capacity, decisions must be “smaller” and not require the use of the corporate data base. Spreadsheets are the most common type of analytical tool employed. There are also a large number of financial forecasting applications, such as investing. Sales/Marketing analysis and forecasting packages are also available. There are hundreds of vendors selling microcomputer software; consequently, a manager can normally find several DSS that fit special needs, whatever they may be. To illustrate such capabilities, spreadsheets, financial analysis, and sales analysis programs are now discussed.

In its general form, a spreadsheet is a pre-determined grid in which the user fills in the spaces and calculations are made. Spreadsheets are powerful programs, because after the user has defined the columns and rows, the screen can display almost any numerical situation. The user can establish relationships between various locations to answer “what if” questions. Rapidly, the spreadsheet shows the effect changes will have on the “bottom line”. For example, such questions as “What if interest rates go up?” or “What if I give my staff a raise?” or “What if I increase advertising expense?” give valuable answers to the manager. Spreadsheets are a particularly useful analytical tool for the accountant and finance planner but anyone who compares data, makes projections, or formulates strategy will benefit from them.

An example of an advanced spreadsheet program on the market is Planstar by MicroPro International. Planstar is a financial modeling program that goes beyond basic spreadsheet capabilities for financial analysis and forecasting. The program uses English calculation commands rather than formulas, consolidates up to 1000 spreadsheets per project, and has a capacity of more than 32000 cells per spreadsheet. Planstar allows arithmetic calculations between spreadsheets and provides numerous financial functions including net present value, internal rate of return, amortization, and moving averages. Planstar costs \$675 and uses 128K memory. A second example of a spreadsheet program is VisiCalc IV by VisiCorp. VisiCorp has several spreadsheet programs on the market but this is one of their best. VisiCalc IV combines VisiCalc and StretchClac into one program that provides integrated sorting and graphics. It permits permanent and temporary sorting of rows and columns on a spreadsheet. VisiCalc IV includes a data base management system for retrieving information. The program allows a user to query the system or treat spreadsheet rows as records. VisiCalc IV costs \$250 and uses 192K memory. Probably the most sophisticated spreadsheet program available is 1-2-3 from Lotus Development. In addition to typical spreadsheet capabilities, 1-2-3 has graphing facilities that allow the user to make line, bar, pie, stacked-bar, and scatter charts using data from the worksheet. 1-2-3 also has data base facilities that search for and extract previously defined records. The user can sort, build data tables, calculate distributions, and perform other statistical analyses of the records in the data base. A minimum of 128K memory is needed to load the system and it lists for about \$550.

DSS in financial forecasting applications can assist the investor in at least three specific areas: portfolio evaluation, information retrieval, and investment analysis. Portfolio evaluation is actually a method of record keeping. Many investors want to compute their portfolio value as well as gains and losses. More sophisticated portfolio programs enable investors to maintain complete records of purchases, sales, and commission costs. The software can prepare statements of short- and long-term realized gains and losses to use in completing tax returns.

The second area, information retrieval, uses a commercial data base to provide financial information. A description of a commercial data base and its uses will be discussed later. Investment analysis, the third financial application, can be subdivided into technical and fundamental. Technical analysis attempts to predict future prices by studying the past. DSS programs chart indices – such as price, volume, and moving averages. Fundamental analysis studies the relevant factors that affect stock prices. DSS programs allow the user to compare stocks to determine which is best. Most programs help find emerging, growing stocks and compare investment strategies. There are, of course, many software packages available in this area. Bottom Line Strategist by Ashton-Tate and Market Maverick by Financial Software, Inc. are two sophisticated packages. The Bottom Line Strategist is a financial forecasting program that uses graphics to track and analyze business situations. The user enters business assumptions in eight categories. These categories range from marketing, advertising, pricing, and productivity to inflation impact. The program analyzes the feasibility and profitability of each project, graphs and then prints 11 types of financial and marketing forecasts. The Bottom Line Strategist lists for \$400, needs 128K memory and 2 disk drives. The Market Maverick supports the third area of financial analysis – selecting stocks. This program uses volume and momentum to indicate the stocks with the greatest upside potential. The program includes a data base of 960 stocks and regular updates are available on disk. The user may also select model inputs; i.e. of using the data base or an outside source, such as Value Line. The list price of Market Maverick is \$175. It is both cost-effective and easy to use.

Strategy and analysis programs for marketing and sales are available through numerous vendors. For example, Sales Analysis System by Holland Automation or Sates Analyst and Forecaster by Sandy Point Publications are two packages now available. One disadvantage in marketing/sales software is that there tends to be a limited number of hardware types supported. The most popular microcomputer is Radio Shack's TRS series; next are those supporting CP/M operating systems.

Although the advantages of decision support systems using microcomputers appear to outweigh the disadvantages, the disadvantages need to be noted. The greatest drawback is the storage size and amount of data a microcomputer can handle. Limited storage restricts the DSS to smaller applications with less complex models. In addition, the user cannot take advantage of the corporate data base. If managers ignore the information stored in the internal (corporate) data base and rely only on their own data with a microcomputer, serious problems can result. For example, different manager's decisions could be based on inaccurate or contradictory data. Another disadvantage is that executives may be alienated by computers because they do not want to appear foolish. They are not comfortable with a computer and are afraid to learn. Another problem is the so-called "foot prints" (the amount of desk space used by the computer). Executives feel that footprints are excessive, especially for an occasional user. Finally, many executives feel their security is threatened when using a microcomputer. One manager states, "I don't like micros. I have too much confidential data that I want to keep centralized." [28] Most disadvantages will disappear as more executives become familiar with, and storage capacity increases for, microcomputers.

## 3.2. DSS and Local Area Networks

Local area networks (LANs) can have a tangible affect on decision support systems. A LAN is defined as a communications network that interconnects a variety of data communicating devices within a small area. Once connected to the LAN, computers can share data files, programs, hard disks, and printers. The communication is local (hence the name), usually within an office building or several buildings less than one mile apart. As an example, each type of user is provided with electronic mail and word processing to improve the efficiency of creating and distributing messages, memos, and reports. Managers are also given a set of program and budget management tools. Now certain expensive resources, such as a disk and printer, can be shared by all the users of the LAN. Consequently, the microcomputers have access to the files and programs stored on the hard disk and can retrieve it at a speed equivalent to local retrieval. Furthermore, the network can tie into larger network facilities, For example, the corporation may have a long-haul corporate-wide network using, for instance, IBM's SNA.

The DSS software discussed previously is applicable in this situation. Stallings [28] refers to this type of network as “Personal Computer Networks” [28]. A typical network configuration is shown in Figure 2.

The microcomputer, hard disk, and printer are attached to a cable. Users can access data stored on the disk or download software from it to the local workstation. This improves the effectiveness of a manager's decision, because more data is available for decision making. Also, one printer can be shared by a number of users (this allows an organization to purchase better quality printers). Most quality printers are spooled; i.e. users can issue print commands even though the printer is busy and the spooler will store the data until the printer is once more available. The network of Figure 2 is termed a "ring" and is one of the most popular among LAN vendors.

There are many LAN vendors with good products on the market. The Xerox, Ethernet, is one of the most popular LANs today. IBM's PCnet is a very cost-effective network. PCnet interfaces with the IBM PC. Data General offers a "Comprehensive Electronic Office (CEO)". This package has electronic mail, decision support system software and may be tied to Zodiac, the Data General's LAN. In addition, Multi-Calc allows users to exchange VisiCalc worksheets with other users. Furthermore, 3COM is supporting the efforts of software houses to produce network-compatible products, such as data base managers and spreadsheet programs. These programs will be able to communicate across LANs.

![](/api/attachments/VKGGQE84/fulltext/images/b348d8fb96d531278fdf5cd42aaea1fb45ac44b2e1af8c8cb0b1be50a48c10da.jpg)  
Fig. 2. A LAN configuration known as a "ring".

The only real drawback to a LAN is compatibility between networks and compatibility between machines. An IBM PC on PCnet cannot communicate with a computer on Ethernet; an IBM PC generally cannot be used on the same network as an Apple II. However, some networks of the same type can communicate through a gateway. This provides an interface that links the networks. Because most networks do not support a variety of machines, an office with several kinds of microcomputers (such as the TRS-80, Apple, or IBM) suffers from incompatibility. It is advisable for such companies to wait before investing in a LAN [11]. Experts claim that the compatibility problem will soon be solved. Large scale vendors, such as Xerox (Ethernet), Unger-mann Bass (Net/One), and Datapoint (ARCnet), predict that they will have compatible products late this year or early next year [11].

## 2.3. DSS and Emulation

Emulation is the ability to imitate other machines. Usually, a microcomputer will emulate a terminal so that it can communicate with the company's central computer; however, it can also emulate devices such as a printer or disk drive. Accessing the corporate data base from a microcomputer is a tremendous benefit. Data files can be transferred from the mainframe and then used in the DSS. In effect, the microcomputer replaces a terminal and is still used for generating spreadsheets and providing wordprocessing support. Again, this increases managerial effectiveness and efficiency.

Emulation can be achieved through software or hardware. Both translate codes to and from the device being “imitated”. Two types of emulators are: asynchronous CRT emulators and synchronous emulators. The latter will not be discussed, as they are seldom used. Asynchronous CRT emulators are software products; they are cheaper, but only data files can be transferred, not programs. IBM has an attachment that allows the PC to emulate a 3270 terminal. The user must press two keys to switch between terminal and stand alone modes. PC-link is the least expensive emulator (\$60) by Screenware Corp. PC-link allows data file transfer between PC and IBM mainframe. In addition, DEC has developed “All-in-one” which links microcomputers with larger systems such as VAXS.

There are two primary advantages to terminal emulation. First, emulating a device saves money. To get the same effect, a device would either have to be purchased or rented. If a device is purchased, users run the risk of investing in hardware that may soon be obsolete. Secondly, a PC emulating a terminal saves desk space; this seems to worry executives. The only drawback to terminal emulation software is that only file transfer is permitted. The user can fetch data and browse through it on screen. But, the software does not permit the user to move a complete spreadsheet program from the mainframe to the microcomputer.

Another possibility occurs with emulation: a microcomputer can emulate a terminal but also be connected to a local area network. With a LAN, all the microcomputers on the network would have access to the mainframe's data but only one machine needs emulating capabilities. This further reduces cost, because emulating software need not be purchased for each microcomputer. Figure 3 illustrates such a configuration.

## 2.4. DSS and Commercial Data Base Services

A “commercial data base service” sells access to a large (national) database. The user needs a modem, telephone, and password to retrieve data. Daily and historical stock quotations, business news, SEC filings, and fundamental indicators (such as moving averages) are a few examples of current commercial data bases.

In the area of investments, a decision support program could access a commercial data base to retrieve external information. Investment analysis needs pertinent, financial data in order to make effective decisions; therefore, a user could subscribe to The Dow Jones News/Retrieval Service. This provides historical quotes, stock prices, news stories from the Wall Street Journal, and profiles on various corporations. Furthermore, the user could be using software running on the microcomputer or mainframe computer. In either case, the microcomputer or terminal must be connected via a telephone line to the commercial data base.

Jones Market Analyzer. The program is equipped with a subscription to the News/Retrieval Service, and costs 15 cents per minute; in 7 minutes, the user can retrieve 120 days of information or 6 months of trading. The main advantage of the Analyzer is its sophisticated graphing functions. Charts can be prepared comparing the performance of up to 5 stocks on a single graph. Moving averages and regressions lines can then be calculated. The user can also give instructions on charts to be drawn and printed. The program then automatically performs its predefined duties, prints results, and logs itself off. The Analyzer lists for \$349. IBM has a similar product called the Dow Jones Reporter; it also uses the News/Retrieval Service. The Reporter, though not as comprehensive or sophisticated as the Analyzer, is less expensive: lists for \$100. For portfolio evaluation problems, Portfolio by Software Options, Inc. offers a futures and options management system that performs valuation. It produces profit/loss reports that reflect the most current trade entries and prices. The user can connect to a price quotation service for \$175 a month. Portfolio lists for \$1240. There is the External Data Base from Chase Econometrics and Data Resources. This is extremely useful for managers who need to relate internal financial analysis to external macroeconomic forecasts and models.

A popular financial DSS program is the Dow

![](/api/attachments/VKGGQE84/fulltext/images/12c7606ee78f4b394edd69a4cbcb48119a7c3747728be064963244fabf83677e.jpg)  
Fig. 3. A microcomputer emulating a terminal while connected to a LAN.

Commercial data bases add timely, external data to a decision support system. Therefore, a manager's decision is better.

## 2.5 DSS and Timesharing Systems

A timesharing decision support system is one in which the user rents computer time from a vendor; the user shares the vendor's resources with other users. As with a timesharing system, the user only needs a modem, telephone, terminal and password to access the system. However, here, the user not only retrieves information but also invokes the program to process it.

Often, an organization will use the timesharing system for a transitional period before purchasing or building a corporatewide DSS. Timesharing services often provide easy transition to future in-house processing when the user is naive to computing methods. Ther may be four advantages to this:

(a) during the timesharing phase, the appropriate hardware environment can be determined

(b) software can be evaluated to ensure it meets the predefined needs

(c) the internal support group can be organized and trained

(d) the exact needs of the in-house system can be determined

Vendors support a “transition” from timesharing by offering decision support packages through both a timesharing service and later through its purchase. For example, EXPRESS by Management Decision Systems can be rented through TYMSHARE or purchased. TYMSHARE accepts programs from many vendors and “locks” the user out of the unwanted programs.

DSS software available through timesharing services includes modeling and forecasting systems, financial analysis systems and sales/marketing systems. Many reach top-level executives through user-friendly programs. Some programs have “fill in the blanks” data entry and simple commands; others provide large historical data bases particularly suited for business needs. For example, EXPRESS covers long range strategic forecasts from 6 to 20 years, tactical planning from 1 to 5 years, and short term operations up to a year. Applied Data Research has leased its EMPIRE financial modeling, reporting and analysis program to Budget Timeshare for use on Budget’s national timesharing system. EMPIRE has applications for budgeting, capital structure analysis consolidations and investment analysis. More and more vendors are leasing their DSS software to national timesharing services so that users can now get a preview of the system they want to purchase or not purchase as the case may be.

## 2.6. Integrated Systems

Integrated systems are comprehensive decision support systems that support a large number of users. They support managers from all functional areas in the corporation and at all activity levels. An integrated system is characterized by a large data base, at least one mainframe computer, and data modeling and retrieval languages. Usually, there are sophisticated graphic functions available at the terminal. The key to an integrated system is the creation of software that is simple to use and user-friendly while taking advantage of the full power of the mainframe. Logical organization of the data must be in easy-to-define data structures that are familiar to managers. Data should be organized in a manner that makes sense to managers; i.e. they should not be forced into something that seems artificial. Previous DSS have been hard to use especially for the non-computer-oriented executive. However, natural language interfaces are being introduced and expert systems are being developed to assist a DSS in aiding an individual manager's decision process.

An integrated DSS can be implemented in three ways:

(i) Develop a complete in-house system. This requires a complete design of the new system and takes time because no procedural method really exists for implementing DSS, though certain criteria have been defined.

(ii) Purchase a variety of decision support applications and use the DP department to create their interfaces. Such systems tend to be difficult for non-technical executives to use, and vendor enhancements require expensive modifications.

(iii) Purchase the complete DSS system. Few are currently available: Boeing Computing Services, IDC, and Managements Decision System's EXPRESS are among these. However, sophisticated packages for functional areas can be purchased for the mainframe.

Integrated systems represent large initial investments. Even if they offer a fast payback, much care and planning is needed in vendor selection, implementation, and ongoing support.

## 3. Conclusion

Today, there is an abundance of software available, particularly for the microcomputer. This paper describes a few DSS packages on the market for the micro-, mini-, and mainframe computers. A more complete list of software can be found in PC Magazine's Bluebook PC, Personal Computing's Product Reviews, or Personal Software's New Releases. Magazines such as these review and describe the software, then list hardware requirements and prices. Care must be taken in selecting any software to insure satisfaction. When the user is choosing software to purchase, several questions should be asked:

1) What kind of computer capabilities does my company already have? Do the potential users already have terminals or personal computers at their desks or will we have to provide them?

2) Can our present system handle the overload of several users performing interactive financial calculations online, or would it be more economical to provide them with their own microcomputer?

3) Who will be the users of the product? How user-friendly should the software be?

4) What kind of work will be done with this software? Small daily tasks or major long-term studies? How large a historical data base is needed?

Once the type of system needed is determined, a person or group should research various products available and get hands-on demonstrations of the product. Decision support consulting services are also available to help the user select a DSS system.

The explosion of microcomputers in business has had a tremendous effect on decision support systems. Thus, this article is weighted toward decision support for the microcomputer. In addition, if data communications products soon become compatible, executives can look forward to a true multifunctional workstation. This will enable them to retrieve data and programs residing on any system large or small.

## References

[1] Alter, Stephen, Decision Support Systems: Current Practice and Continuing Challenges. Massachusetts: Addison-Wesley, 1980.

[2] Anthony, Robert and John Deardon, Management Control Systems. Illinois: Richard Irwin, Inc., 1980.

[3] Bennett, John, Building Decision Support Systems. Addison-Wesley, 1983.

[4] Bonzcek, Robert, et al., Foundations of Decisions Support Systems. Academic Press, 1981.

[5] Bricklin, Daniel, "Spreadsheets. Software Review-PC Magazine, 1983, p. 108–112.

[6] “Computer Support for Managers”, EDP Analyzer, May 1979, Vol. 17, No. 5, p. 1–13.

[7] Denise, Richard, "Technology for the Executive Thinker." Datamation, 1983, p. 208-216.

[8] Gabel, David, “What If You Build a Model?” Personal Computing, October 1983, p. 82–91.

[9] Hoover, Thomas, "Decision Support at Conrail." Datamation, June 1983, p. 221-230.

[10] Horwitt, Elizabeth, "Fear of Trying." Business Computer Systems, July 1983, p. 51–60.

[11] Horwitt, Elizabeth, "Sharing the Wealth." Business Computer Systems, October 1982, p. 71–76.

[12] “Idaho Power Turns to New Computer Technology for Corporate Planning.” Public Utilities Fortnightly, April 15, 1982, p. 62–66.

[13] "Interesting Decision Support Systems," EDP Analyzer, March 1982, Vol. 20, No. 3, p. 1-9.

[14] Keen, Peter, "Decision Support Systems: Translating Analytic Techniques into Useful Tools." Sloan Management Review, Spring 1980, p. 33-44.

[15] Kennedy, JoAnne, "Financial Applications." Software Review - PC Magazine, p. 324-328.

[16] Kingston, Paul, "Generic Decision Support Systems." Managerial Planning, March/April, p. 7–11.

[17] Lingren, Richard, "Justifying a Decision Support System." Data Management, May 1981, p. 30-32.

[18] Machrone, Bill, "Battle of the Network Stars." PC Magazine, November 1983, p. 96–104.

[19] Morton, Scott and Peter Keen. Decision Support Systems: An Organizational Perspective. Massachusetts: Addison-Wesley, 1978.

[20] "Multiple Personalities: Emulation with the PC." PC Magazine. November 1983, p. 347–354.

[21] Nelson, Steve, “The Profit Prophet.” PC World, Vol. 1, No. 6, 1983, p. 130–133.

[22] Raho, Louis and James Belohlov, "Discriminating Characteristics of EDP, MIS, and DSS Information Interface." Data Management, December 1982, p. 18–20.

[23] Rietmann, Kearney, “Deduction and Reasoning.” Software Review-PC Magazine, 1983, p. 456–7.

[24] Smartt, Philip, “Ingredients for a Successful Decision Support System.” Data Management, January 1983, p. 26–33.

[25] "Software Packages for Sales/Marketing." Industrial Marketing July 1982, p. 50–56.

[26] Sprague, Ralph and Eric Carlson, Building Effective Decision Support Systems, Prentice-Hall, Inc., 1982.

[27] Sprague, Ralph and Onoran Fick, Decision Support Systems: Issues and Challenges. Pergamon Press, 1980.

[28] Stallings, William, Local Networks-An Introduction. MacMillan Publishing, 1984.

[29] Theil, Carol, “Financial Modeling Software Users Forecast Success.” Infosystem, June 1983, p. 104–118.

[30] Wagner, G., “Decision Support in the Office of the Future.” Managerial Planning, My/Je 1980, p. 3–5.

[31] Wagner, G., “DSS: Dealing with Executive Assumptions in the Office of the Future.” Managerial Planning, March/April 1982. p. 4–10.

[32] Williams, Andrew, “Dow Jones Fortune Teller.” PC World, November 1983, p. 96–104.

[33] Zalud, Bill, “Decision Support Systems: Push End User in Design/Build Stage.” Data Management, January 1981, p. 20–22.
