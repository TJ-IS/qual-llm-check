---
otero_id: 27040
otero_key: "KZE9XRZK"
title: "Airline Management Information System at Arkia Israeli Airlines"
authors: "Israel Borovits; Seev Neumann"
year: "1988"
journal: "MIS Quarterly"
doi: "10.2307/248813"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Airline Management Information System at Arkia Israeli Airlines
Author(s): Israel Borovits and Seev Neumann
Source: MIS Quarterly, Vol. 12, No. 1 (Mar., 1988), pp. 127-137
Published by: Management Information Systems Research Center, University of Minnesota
Stable URL: http://www.jstor.org/stable/248813

Accessed: 08/05/2014 22:03

Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at http://www.jstor.org/page/info/about/policies/terms.jsp

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

# Airline Management Information System at Arkia Israeli Airlines

By: Israel Borovits
Director of Planning and Information Systems
Arkia Israeli Airlines Ltd.
Dov Airport, P.O.B. 39301
Tel-Aviv 61392, ISRAEL

Seev Neumann
Information Systems Program
Faculty of Management
Tel-Aviv University
Tel-Aviv 69978, ISRAEL

## Abstract

This paper presents an approach to developing and implementing a management information system for small airlines. The system presented is a new, comprehensive, real-time sales support and reservation system based on state-of-the-art computer technology, advanced concepts in software design, and practical experience in the travel industry. The system represents a departure from the philosophy underlying most existing airline reservation systems. It is an important strategic asset and a valuable weapon in an increasingly competitive market.

Keywords: Information systems design, information systems implementation, airline reservation systems, decision support.

ACM Categories: H.3.5, H.4.0, H.4.2

## Introduction

As Donald Fink says, “Automation has played an increasingly important role over the past decade in all phases of air transport operations. It will become a critical element of survival in the next decade when the airline industry will be dominated by those large carriers which have the resources to expand their business bases and attain the efficiencies needed to compete in a free-wheeling marketplace.” (Fink, 1986) It is projected that the investment in computerized information systems by U.S. carriers will total \$4 billion by 1990 (Fink, 1986).

The Airline Deregulation Act of 1978 provided U.S. airlines the freedom to experiment with a variety of new, creative pricing and marketing strategies. Entry into new markets and withdrawal from others as well as schedule and fare changes began occurring almost overnight. Airlines previously used relatively simple and inexpensive internal reservation systems which, along with lower airfare rates, became a key to their competitive success and share in the air travel market. But as a result of constant changes associated with the deregulated environment of the 1980s, airlines recognized that their reservation systems, developed during the regulated years of the 1960s,' could not keep pace. They also recognized that the lack of a good reservation system was a competitive disadvantage.

The system discussed here represents a departure from the philosophy underlying most existing airline reservation systems. Such systems (e.g., SABRE of American Airlines, APOLLO of United Airlines, PARS of TWA) required heavy capital outlays to develop their software, are massive and difficult to maintain, and are based on relatively outdated information technologies. There are many small airlines (e.g., commuter airlines) that cannot afford to invest in these systems.

The new system, AMSYS (Airline Management SYSTEM), uses contemporary hardware and software technologies and applies them to a small airline at affordable costs, and enables the company to grow along with the technology. The system is modular in terms of its growth; it is not necessary for a large initial investment. An important underlying design principle is machine-independence on a variety of hardware and operating systems.

AMSYS is more than an airline reservation system. In addition to reservations, it is a planning, costing, and controlling system. It is also an interactive DSS, which is used for sensitivity analysis (“what if” questions) of important parameters, for scheduling aircraft, crews, and general personnel, and for assessing and determining schedule and fare changes. AMSYS is an important strategic asset for the company and an important weapon in an increasingly competitive market.

## Description of Arkia Airlines

Arkia Israeli Airlines operates scheduled and cargo domestic services linking Tel-Aviv, Jerusalem, Eilat, Haifa, and Rosh-Pina, as well as charter flights to European destinations such as London, Paris, Munich, Frankfurt, Cologne and other seasonal destinations. Ancillary activities include ground handling, wet and dry leasing of aircraft, pilot training, maintenance services, general flight services for foreign airlines, short excursion tours in Israel and abroad, cloud seeding, and other general aviation services. The airline was founded in 1950 as Arkia Inland Airlines. Its headquarters is at Dov Airport in Tel-Aviv. There are 350 employees. Its fleet consists of two Dash-7 aircraft for domestic operations, as well as five Navajo Chieftain, two Islanders, one Aero Commander, and two Cessna 337s. For international operations Arkia is using three Boeing 707 aircraft. Arkia carries a total of 350,000 passengers a year.

## The Old System

A manual reservation system was in use until the installation of AMSYS. The reservation clerks at each location sat at a round table on which a carousel contained charts for each leg of the flights. Each chart listed the names of the reservations for the particular leg. When a call came in requesting information or a reservation for a specific flight, the clerk would look for the correct chart, which at times another clerk would be using, and record the name on the chart. A pencil and eraser were used to record, update, and delete names. Since a manual system was used, each of the various geographically dispersed reservation offices was assigned a certain number of seats for each flight which the clerks were allowed to sell. That procedure could not provide management with the true status of the flights because each office was allotted only part of the available seating. In many cases an office finished selling its allocation and rejected potential passengers, while other offices still had seats to sell. There were many other problems, such as double booking (booking by the same passenger for a number of flights) and the inability to relate outbound and inbound flights of specific passengers. As a result of these problems and the inability to cope with the increased number of passengers, there was no alternative but to develop or acquire a computerized information system to assist operations and management in reservation scheduling, planning and controlling.

## The Evolution of the New System

AMSYS was developed from 1982 to 1985, and its first version was implemented in 1983. Fifteen person-years were invested in the development. The system runs on a multi-user NCR Tower-32 supermicro computer operating under UNIX. It has a network of 33 terminals, soon to grow to 48. AMSYS is connected to SITA, the airlines worldwide message switching network, and thus can interact with information systems of other carriers.

Ahituv and Neumann (1986) list five reasons for a finite information system life cycle and the needs for embarking on a new one. These apply in the case of Arkia:

Increase in input quantities. In recent years, passenger traffic in Israel has increased at a phenomenal rate. This has placed a tremendous strain on the handling capacity of the manual system. The old manual system used by Arkia could not cope with the volume of transactions. As the number of flights increased, the load factor decreased because it was not possible to react quickly to changes in demand, which, in the case of the domestic operations, occur on a daily basis.

Advances in technology. Rapid advances in software and hardware technologies affect the economic feasibility of a computerized information system. This made it possible for small airlines like Arkia to develop and install their own computerized systems rather than relying on service bureaus, software houses, or on linking with other airlines' reservation systems.

Changes in related systems. The existing manual reservation system could not interact with two external computerized systems that were implemented in the 1970s: SITA, the airlines worldwide message switching network, and CARMEL, the reservation system used by ELAL, the international Israeli carrier.

Changes in the environment. A rival, new domestic airline was established in 1981, and success in the competitive domestic market became crucial for Arkia's survival. Better service to customers was needed, as well as better tools for managing and planning. In addition to the competition in the domestic market, a “charter war” started in international operations. Arkia's share, as the only Israeli charter carrier, dropped to as low as 18 percent of the total charter market involving Israel. Management mandated that Arkia was to gain at least a 50 percent share of the market involving Israel, thereby becoming the dominant force in the domestic charter market. Again, the need for a reliable and fast planning and central system became vital.

Changes in user expectations and requirements. The old system produced biweekly and then weekly reports to the various users within Arkia (scheduling, maintenance, personnel, credit, reservations). By the late 1970s it became clear that managers and operators could not adequately make decisions and keep pace with daily operations without a system that would be interactive, reliable, and free of the numerous errors that plagued the manual system.

Another extremely important development was the change in management that took place at Arkia in the early 1980s. At that time, ownership at Arkia changed, along with senior management. The new management team consisted of relatively young executives with recent training in finance and marketing who had exposure to and awareness of the opportunities presented by information technologies.

## The alternatives and the decisions

As a result of the above, four alternatives were considered:

1. Continue with the existing manual system (do nothing)

2. Tie in to a system hosted by another carrier

3. Acquire a system from other airlines or vendors

4. Develop a system in-house

It was clear from the beginning, as described previously, that alternative 1 was unacceptable. Therefore, the other three alternatives were evaluated. As for alternative 2, the only available systems for cohosting were those of British Airways (London) and Swissair (Zurich). The estimated cost was very high, about \$3 per passenger, including the communication costs, amounting to a total annual cost of about \$1 million. The CAR-MEL system used by EL-AL, the Israeli international carrier acquired from British Airways in 1976, did not have and still does not have a multi-host capability. For alternative 3, several systems were evaluated for purchase. The available systems required large mainframes, and the total purchase cost of software and hardware would have been over \$3 million. Therefore, the decision was made to develop Arkia's own system. Immediately, other decisions followed:

## Minimize Cost

The budget that Arkia was able to allocate for the project was \$400,000, much lower than the sums mentioned above. Hence, it was decided to search for a solution that would be feasible on one hand, and within budget on the other. Such a solution would have to be based on a small system rather than on the large mainframes used by other airlines. It would also be necessary that the system support the necessary number of terminals. The use of a super micro-computer seemed to be the only possible solution.

## Use a Software House

It was decided to subcontract the development of the system to a software house because Arkia lacked sufficient personnel to complete the project on time and within the allocated budget. Arkia established a project management team, headed by the airline's information systems director, which assumed full responsibility for monitoring and controlling the development process.

## Develop a Portable System

It was hoped that the system would be as machine independent as possible and easy to maintain. RM/COBOL was selected as the programming language. RM/COBOL is not tied to any specific hardware or operating system; the applications coded in it can run on a large number of hardware/operating system configurations and can be easily maintained. The language is available on almost all popular small system processors, including MC68000, Z80, Z8000, 8086, 9900, PDP-11, and LSI-11; it is also available on IBM's 30xx, 43xx, and 370 mainframes. The applications coded in RM/COBOL execute on a large number of operating systems, including RM/COS, OASIS, UNIX and UNIX look-alikes, CP/M and MP/M, PC and MS/DOS, TRSDOS, RT-11, RSX-11, and VM/CMS.

## Adopt Phased Development

In order to assure the successful completion of the project, Arkia adopted a phased development approach. This approach is a step-by-approved-step process for developing applications (Borovits, 1984), which for AMSYS consisted of three major phases: the definition phase, which included the preliminary analysis, feasibility study, system analysis, and system design; the construction phase, which included programming and procedures writing; the implementation phase, which included testing, training, and conversion. A detailed discussion of the implementation phase follows.

## Implementation Issues

## Commitment of top management

The success of any development process depends largely on the involvement of and commitment by top management. During the development of AMSYS, Arkia's management committed the necessary resources, participated in various activities, and provided encouragement when it was needed.

## User involvement

AMSYS was developed for users at all levels of the organization. User involvement was vital during the design stage, for it was there where they defined the information problems to be solved and specified their needs. The users approved the specifications, design, and results of the various tests, including the final acceptance test. Users were also involved in the implementation phase, both in quality assurance and pre-installation activities.

## Evolutionary implementation approach

Training of the various levels of users started very early in the development process. A simulator trained the users in learning the various commands, screens, options, and reports. The simulator, which was a prototype of the final software, was executed automatically and displayed different types of input data and the resulting system responses. The prototype is still used today for training new employees and records all transactions per each trainee, providing the instructor with information regarding their competence. The simulation approach also helped in testing the various modules of the system as they were completed. As will be described later, the implementation of the system in the various locations was done in phases.

## Managing the change

The primary concern of the project team was the successful installation of the new system into the organization. Such a change has an impact on the people involved as well as the operations. The problem was how to implement the new system without affecting the equilibrium of the organization.

One of the most effective methods for forestalling organizational suspicion is to involve as many affected employees as possible, making sure that the formal and informal leaders of the groups subject to change are included in the process (Chruden and Sherman, 1976). By having reservation personnel participate from the start, the project manager satisfied their personal and social needs, giving them a feeling of “ownership” of the project. The people involved felt they had a stake in the successful implementation of AMSYS. These feelings were reflected in periodical employee attitude surveys and by the willingness of the affected employees to offer various ideas that contributed to the smooth implementation of the system.

Project managers initiated a program for communicating the details of the implementation of AMSYS, and the employees were kept advised of its progress. This program included a feedback mechanism, which increased the employees sense of participation. Once a week the newly accumulated additions and modifications were presented to all user levels, whose comments were recorded and acted upon. It was thereby hoped to remove any existing suspicions and prevent the development of new ones.

Since it is human nature to distrust anything that happens “too fast,” project managers implemented the new system gradually to allow the employees adequate adjustment time. This process of change was a building process which involved the acceptance of new ideas and methods, the learning of new techniques, and the assimilation of new methods into the work flow.

The implementation process of AMSYS was divided into five phases:

Phase 1 (1983): Training and “playing” with the new system.

Phase 2 (1983): Installation and implementation of AMSYS at the Tel-Aviv reservation center.

Phase 3 (1984): Installation and implementation of AMSYS at the Eilat reservation center.

Phase 4 (1985): Integration of both centers into one database.

Phase 5 (1986): Implementation at all reservation offices. Table 1 exhibits the expansion of the system as the implementation moved through the various phases.

## General System Description

The following discussion of the major functions of AMSYS is not exhaustive. Figure 1 exhibits the MAIN MENU screen, which lists some functions. AMSYS contains quite a large number of functions; only the most important are described in Figure 1.

## Information and reservations

The information and reservations subsystem is a conversational system with online data update. It provides the following facilities:

— display of schedules and service availability for various types of services (e.g., flight, hotel, inclusive tours, car rental) in up to five classes/categories

— creation, retrieval and modification of passenger name records (PNRs) from in-house inventory.

— free sales services or services with availability request

— group handling

— other service information (OSI)

— special service request (SSR) handling

— up to 100 queues (buffers) for storing information that requires special attention

Table 1. Expansion of Hardware During Implementation

<table><tr><td>Implementation Phases</td><td>1,2</td><td>3</td><td>4,5</td></tr><tr><td>Computer Hardware</td><td>Dynabyte Monarch 8000</td><td>Zilog Model 22</td><td>NCR Tower-32</td></tr><tr><td>Location</td><td colspan="3">Number of CRTS</td></tr><tr><td>Seat Control (Domestic)</td><td></td><td>1</td><td>1</td></tr><tr><td>Seat Control (International)</td><td></td><td>1</td><td>1</td></tr><tr><td>Tel-Aviv Reservation Center</td><td>4</td><td>9</td><td>10</td></tr><tr><td>Tel-Aviv Town Office</td><td></td><td>2</td><td>3</td></tr><tr><td>Tel-Aviv Airport</td><td></td><td>1</td><td>1</td></tr><tr><td>Eilat Reservation Center</td><td></td><td>3</td><td>5</td></tr><tr><td>Eilat Airport</td><td></td><td>1</td><td>2</td></tr><tr><td>Haifa Town Office</td><td></td><td>1</td><td>2</td></tr><tr><td>Jerusalem Town Office</td><td></td><td>1</td><td>2</td></tr><tr><td>Netania Town Office</td><td></td><td></td><td>1</td></tr><tr><td>Internal Sales</td><td></td><td>2</td><td>2</td></tr><tr><td>Travel Agencies</td><td></td><td>1</td><td>2</td></tr><tr><td>AMSYS Manager</td><td>1</td><td>1</td><td>1</td></tr><tr><td>Total CRTs</td><td>5</td><td>24</td><td>33</td></tr></table>

![](/api/attachments/KZE9XRZK/fulltext/images/7bc72d64e5f10c2f0a36bb8e68e6e4894bd06236b2d8d1eced1dc2b95393fa2c.jpg)  
Note: The MAIN MENU screen lists all the programs in AMSYS on a single screen. All programs are started from this MAIN MENU screen and return to this screen when completed.

Figure 1. Selections from the Main Menu Screen

—fare information

— payment collection

Figure 2 is an example of the main reservation screen.

— tickets, vouchers, confirmation and itineraries

— automatically triggered invoicing

— sales reports

— boarding cards (non IATA ticket format)

## Reservation control facilities

The reservation control subsystem provides the following facilities:

— real-time inventory maintained for each leg and class of service

— authorization control profiles, such as automatic notification of exceptional conditions that require manual handling

— option date and waiting list processing — inventory and PNR history — ticketing and payment time limits — schedule changes and re-accommodation of passengers

## Document printing

The document printing subsystem issues:

## Management information system

The management information system (subsystem) includes:

— an integrated report generator, which allows the creation of new or specific reports within a very short time

— user-defined sort criteria for individual reports
— updated accounts receivable, accounts payable and potential profit reports

— debit and/or credit balance reports

— agency sales and staff performance statistics

— boarding and arrival lists

## Commercial facilities

AMSYS allows defined classes of seating space (i.e., first class, business class, coach, etc.) at

defined fares and an overbooking factor for each class of space. These may be altered at the commercial department or supervisor level, but the flights can only be set up and the schedule changed at the commercial level. This subsystem allows the commercial department to blockbook space to agents and other operators and release space as required.

AMSYS allows the commercial department to make online amendments to the schedule, class allocations, and block bookings as may be re-

![](/api/attachments/KZE9XRZK/fulltext/images/da3b004a86d843f8e7cc39e11b8489aece08fdefeaabeb1e77b5180790dfa6f0.jpg)

## Legend:

[1] Flight item line number

[2] Airline code and flight number

[3] Date of flight

[4] Classes of service on the flight and available seats for each flight

[5] Origin and destination (airport to airport)

[6] Departure time

[7] Arrival time

[8] Service on flight

[9] Aircraft type code

[10] \* indicates that a message is stored for this flight

[11] Various data elements about passenger

[12] A ..... Availability Action Code

26MAY .. Date of Travel

TLV ..... Boardpoint (i.e. Tel-Aviv)

ORY .... Offpoint (i.e. Paris-Orly)

[13] System messages (if any)

Figure 2. The Reservation Screen quired in the day-to-day running of the operation. Figure 3 exhibits the control and planning screen.

Other marketing features of AMSYS include passenger and revenue statistics by destination, agency statistics, and promotion facilities for special offers.

## Accounting facilities

AMSYS allows for the establishment of conversion rates, updated daily for foreign currencies that are used by Arkia.

AMSYS is used by the accounting department in setting up and maintaining agents' accounts, and generates messages to the accounting department if attempts are made to access agents who are not defined or were cancelled because of unapproved credit lines. Bookings will not be made in these circumstances unless approved by a supervisor.

A major function of AMSYS is ticket and voucher control. It provides the capability for the allocation of prepaid ticket advices (vouchers or exchange orders) to travel agents and allocates ticket stock. AMSYS allows the logging of these documents and the reporting of their status.

Once a flight has departed, the pulled flight coupons are returned to the accounting department where they are matched against flight ticket numbers. AMSYS allows full reporting facilities for ticket status and of unused coupons.

AMSYS provides a complete revenue analysis for each flight, showing each PNR and the method of payment. AMSYS also provides on demand a revenue summary by flight number.

## Message handling facility

Any system terminal may send a message to any other terminal or its associated printer through the system. AMSYS itself uses this facility to route errors and control messages to the correct locations.

## Supervisor facilities

An extensive range of facilities is provided to allow the user to reroute messages to various operational equipment. For example, if a ticket printer goes down, a supervisor can reroute ticket printing to any other printer on the same site, or, if the supervisor printer goes down, any ticket printer can be designated “supervisor” and the ticket printing is then routed to another printer.

## Reporting facilities

AMSYS supplies operational and accounting reports on an automatic or on-demand basis. The following is a partial list of available reports:

— passenger manifests

— revenue analysis (for each flight)

— revenue summary (for flight number within a period)

— tickets

— invoices

— vouchers

— availability summaries

— forward booking summary — coupon control report (showing the status of tickets)

— housekeeping control

— security control

## User aids

AMSYS contains a series of help screens, which a user can call up for an explanation of how to perform a given job. These can be set up and amended at will by the supervisors and the commercial/accounting personnel.

## Security functions

Security in a critical information system such as AMSYS requires attention to accountability, prevention, detection, and enforcement. This may be accomplished through sophisticated tools for data base security, back-up and recovery. There are tools available to prevent and detect break-ins. The system has a number of security levels, which allow users to use only those functions for which they are authorized. For example, a reservation agent can access the Reservation Screen only: the system manager is the only one who is allowed to use all functions of AMSYS, including assignment of new codes and passwords.

## Interface with other Arkia information systems

AMSYS interfaces with other major information systems of Arkia. These systems include maintenance and logistics, payroll, station management, catering, and accounting and costing.

<table><tr><td colspan="7">AMSYS Airline Management System - A R K I A -
SPECIFIC FLIGHTS</td><td colspan="4">SC/RS 25 APR 87</td></tr><tr><td colspan="7">From To Date Day Flight</td><td>F</td><td>B</td><td>C</td><td>Total</td></tr><tr><td colspan="7">TLV ORY 29 MAR 87 7 IZ 0741 1 Seats</td><td>12</td><td>30</td><td>110</td><td>142</td></tr><tr><td colspan="6">Flight is: TLV ORY</td><td>Ticket</td><td>8</td><td>18</td><td>92</td><td>118</td></tr><tr><td></td><td></td><td></td><td>Time</td><td></td><td></td><td>Regular</td><td>10</td><td>22</td><td>94</td><td>126</td></tr><tr><td colspan="6">Dep Arr A/C Service Limit Tariff</td><td>Group</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>NRPS</td><td></td><td></td><td></td><td></td></tr><tr><td colspan="6">02:50 06:45 ATY 00</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="6">comm.</td><td>Total</td><td>10</td><td>22</td><td>94</td><td>126</td></tr><tr><td colspan="6">Status catg. Remarks</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>W.L.</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>01</td><td></td><td></td><td></td><td></td><td>N.R.</td><td></td><td></td><td></td><td></td></tr><tr><td colspan="11">Select: 2-3.Paging Flight 4.Display R. Re Amend A.Amend Flight5-6.Paging Leg K.Keep Flight (2,3) B.Amend Seats7-8.Paging City To +,-,W.Change Date S.Shift SeatsConfirm (Y/N)</td></tr><tr><td colspan="11">System Messages:</td></tr></table>

## Legend:

![](/api/attachments/KZE9XRZK/fulltext/images/8f1ce20ef714f3b663c4522b3e5dc7a05d87faba5e84fccc913c65824d1ae42b.jpg)  
Figure 3. The Control and Planning Screen

AMSYS, which constitutes the passengers' information system, is installed on a super microcomputer, while the other information systems are installed on an IBM S/36 computer. A standard off-the-shelf commercial software package enables these two computers to "talk" to each other and transfer data daily.

## Business Impact and Benefits

Escalating costs in fuel, fleet replacement, payroll, facilities, and equipment require a strong financial posture and higher returns from the sale of products (i.e., seats on airplanes, tour packages, and other services provided by the airline). The implementation of AMSYS resulted in better service for passengers and yielded better loading factors, contributing to far more efficient and profitable operations for Arkia. Arkia is using AMSYS power to increase sales, returns, and market share. The system made it possible to provide more extensive travel data for other airlines, travel agents, and corporate users nationwide. Its return management capability has made it possible to launch discount programs and compete with other low-cost, low-fare carriers. One of Arkia's major competitors, SHACHAF Airlines Ltd., attributed its marketing troubles to Arkia's capability to fine-tune its computerized fare programs, which prevented SHACHAF from continuing its previous underselling tactics. As a result of this activity, SHACHAF has ceased operation on all routes where it competed with Arkia.

While AMSYS provides operational control on a day-by-day, flight-by-flight, seat-by-seat basis, it evolved to change the nature and scope of the operations of Arkia by broadening the packaging of air travel beyond simply selling airline tickets. It includes a wide range of travel-related functions and stores data on a nationwide and worldwide basis (e.g., hotels, car rentals, foreign currency rates, etc.). AMSYS has thus transformed Arkia from an airline to a travel service company. As mentioned previously, AMSYS is used currently by other small airlines, a number of wholesalers, and some travel agents (retailers). AMSYS has evolved from a support tool to a strategic weapon and finally to a product sold by Arkia.

Another major impact of AMSYS has been as a decision support aid to senior management. The data collected and information produced by AMSYS provide input to a model based on Lotus 1-2-3 software. The model enables top management to evaluate the sensitivity of alternative solutions to critical business issues (“what if”). Meetings of the board of directors and all levels of management are held with easy access to a PC connected to AMSYS. Many decisions can therefore be evaluated immediately.

## Future plans

The successful implementation of AMSYS convinced Arkia's management that micro-computer technology could result in major benefits for the company. Therefore, future plans call for the rewriting of the existing software of other Arkia systems and migrating their execution from mini-computer technology to super micro-computer technology. The objective is within the next three years to have a total integrated information system which will support all operational and managerial functions performed by the airline and its personnel and managers, and will include AMSYS as one of its major modules.

## Conclusions

The paper addressed the main design concepts of an airline passenger information system that supports operational and managerial decision makers in the context of a small regional airline. The investment in both hardware and software development totaled approximately \$250,000. The implementation of AMSYS showed that it is possible to use new hardware and software technologies to develop systems which until recently were prohibitive to implement or very costly. Relatively small companies, like Arkia, can now benefit from computerized information systems. AMSYS demonstrates that the use of microcomputer technology makes it possible for small regional airlines like Arkia to have their own information systems without the need to rely on the “big brothers.” AMSYS may be used by other regional airlines, tour operators, and travel agents, on almost any hardware that fits their size and budget. Indeed, Arkia is vigorously negotiating with interested parties worldwide on the sale of AMSYS and is considering the formation of a subsidiary to maintain this new line of business. AMSYS thus may embody the shape of things to come in the use of information systems and their added value to organizations.

From a humble beginning as a necessary support tool, AMSYS became a strategically important executive support and marketing tool and finally became a product in its own right. (In fact, Arkia's information system director is now devoting more time to selling Arkia's information systems. AMSYS is presently used by two other airlines in Europe, and seven tour-operators in Europe and Israel, where it is installed on IBM/PC, Zilog 22, IBM System 36, NCR Tower 32, Nixdorf and other equipment.) Arkia's management is now convinced that AMSYS not only changed the nature of operations and the competitive arena in which the company operates, but also changed Arkia itself from a company moving passengers to a company offering numerous travel-related services and information-related products.

## References

Ahituv, N. and Neumann, S. Principles of Information Systems for Management, 2nd Edition, William C. Brown Company, Dubuque, IA, 1986, Ch. 7.

Borovits, I. Management of Computer Operations, Prentice-Hall, Inc., Englewood Cliffs, NJ, 1984, Ch. 5.

Chruden, H.J. and Sherman, A.W., Jr. Personal Management, South-Western Publishing Co., Cincinnati, OH, 1976.

Fink, D.E. “Automating the Airlines,” Aviation Week and Space Technology, 125:18, November 3, 1986, p. 27.

## About the Authors

Israel Borovits is Director of Planning and Information Systems at Arkia Israeli Airlines Ltd. He is also professor of computers and information systems at the Faculty of Management and director of the Marcel and Annie Adams Institute for Business Management Information Systems at Tel-Aviv University. He was formerly the chairman of the Computers and Information Systems Program at Tel-Aviv University. He received his Ph.D. in operations research from the Polytechnic Institute of Brooklyn. He is the author and co-author of books and articles in the management and economics of information systems, systems development, and simulation. He has broad experience in teaching and consulting in these fields.

Seev Neumann is Mexico Professor of Management Information Systems and dean of the Faculty of Management, Tel-Aviv University. He holds a BSS from the Hebrew University in Jerusalem, and an MBA and Ph.D. from the Graduate School of Management, University of California, Los Angeles. His research and teaching interests are in the areas of information systems management, economics, and information system policy. He has authored and co-authored books and articles in these areas. He has been extensively active as a consultant in the field of computers and information systems.
