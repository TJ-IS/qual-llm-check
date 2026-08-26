---
otero_id: 19431
otero_key: "T7BNR8FA"
title: "RyderFIRST: facilitating a turnaround in ryder system's consumer truck rental division"
authors: "Dennis Klinger; Joyce Elam; Rajiv Sabherwal"
year: "1994"
journal: "The Journal of Strategic Information Systems"
doi: "10.1016/0963-8687(94)90029-9"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Case study

# RyderFIRST: facilitating a turnaround in Ryder System's Consumer Truck Rental division

Dennis Klinger

Vice-President of MIS and CIO, Ryder System, Miami, FL 33166, USA

Joyce Elam and Rajiv Sabherwal

Florida International University, Miami, FL 33199, USA

In April 1993, the roll-out of RyderFIRST, a \$25 million, PC-based system that links Ryder System's Consumer Truck Rental division with its 5000 independent dealers, was completed. RyderFIRST automates order entry, sales, marketing, and inventory management. After two consecutive years of losses, the Consumer Truck Rental division is finding that RyderFIRST is helping its return to profitability through improvements in inventory control, pricing, and marketing. RyderFIRST provides a very powerful example of how an information system can create significant business value, especially for an organization facing financial difficulties. The development of a strategically oriented information system is seldom easy. When a proposed system is targeted to help a business that is currently under major financial pressure, the urgency surrounding its development may make the risk of project failure or abandonment especially high. RyderFIRST was a high-priority, high-profile project that was considered essential for turning the Consumer Truck Rental division around. The success of RyderFIRST depended on the management of the relationships among the key stakeholders in this project. The RyderFIRST experience demonstrates that in order to effectively manage these relationships the organization must possess some critical strengths — namely, a well-established partnership between information systems and line management and a strong information technology capability.

Keywords: strategic systems, IS-line management partnerships, IS project management

Senior corporate executives are now quite cognizant of the critical role of information technology (IT) in making their organizations more competitive. Stories of the use of IT as a major competitive tool, reported in the popular press as well as the academic literature during the 1980s, have become legendary. In fact, one of the major responsibilities of senior information systems (IS) executives today is to ensure that opportunities to use IT to help the organization achieve strategic objectives are identified and exploited.

However, exploiting strategic IT opportunities has become more complex and urgent. The primary reason for the greater complexity is that strategic IT initiatives are integrally linked with efforts to fundamentally transform the way the business operates. Many people, both inside and outside the organization, are affected by these changes. The primary reason for the urgency is that the future viability of many businesses depends on these IT-based changes. For many senior IS executives, this presents a new opportunity to clearly demonstrate the link between IT investments and business value. But it also presents significant challenges, especially when such strategic IT initiatives are pursued during periods of financial difficulties. Wholesale senior management changes and reorganizations that frequently occur during these periods make it difficult to sustain the level of management support required for the IT initiative. In other cases, there may be tremendous pressure placed on the development team to get the strategic IT application completed as quickly as possible, but few slack resources may be available to support the process.

During the period 1989–92, the Consumer Truck Rental division of Ryder was under considerable pressure from a sagging economy and fierce competition. Several management actions were taken to improve the financial position of this division. One such action was to authorize the development of RyderFIRST, a \$25 million, PC-based system that would link Ryder with its 5000 dealers. By automating order entry, sales, marketing, and inventory management, RyderFIRST could provide Ryder and the dealers with up-to-the-minute information on customer inquiries and reservations, vehicle availability and pricing, and vehicle features and condition. Ryder's corporate management was counting on this investment to help return the Consumer Truck Rental unit to profitability through improvements in inventory control, pricing, and marketing.

RyderFIRST is proving to be a very successful system. In this paper, we describe how RyderFIRST is delivering tangible, business value. Because of the number of stakeholders involved in this project, several challenges were faced in effectively managing the relationships among these stakeholders. We describe the relationships and the key management issues involved. We then discuss the importance of having some critical organizational strengths — namely, a well-established partnership between IS and Consumer Truck Rental and a strong IT capability. This is followed by a discussion of the actions taken to facilitate effective management of these relationships.

## Ryder System

Ryder Truck Rental began in Miami, Florida, in 1933 with one truck. Today, Ryder System, Inc is the world's premier transportation-related services company. Ryder provides such basic highway transportation services as full service truck leasing, consumer and commercial truck rental, dedicated contract carriage, student transportation, public transit management and automotive carriage. Ryder also provides worldwide commercial and general aviation industries with such services as turbine engine maintenance and new and used parts distribution. Ryder is one of the 20 companies that are included in the Dow Jones Transportation Average and is among Fortune magazine's top 50 diversified service companies.

Throughout the 1980s, Ryder System was Wall Street's darling. During this time, profits increased an average of 14 per cent per year. Its stock price reached a peak of \$43 in 1987 and its profits reached a record \$197 million in 1988. This growth was fueled by an aggressive expansion and diversification plan that tripled Ryder's assets through more than 100 acquisitions. By 1988, however, the business of renting trucks to consumers and business began to slow down. Earnings began a decline in 1989 that continued through 1991. Earnings were \$15 million in 1991.

The price of the stock dipped into the teens. Chairman M Anthony Burns responded to investor complaints by reducing the workforce by over 4000 people, including dozens of top-level managers, and selling numerous unprofitable or non-core businesses.

Ryder's performance problems were especially apparent in the Consumer Truck Rental unit whose fleet of 36 000 yellow trucks represented the company's most visible product. Revenues from consumer truck rental declined two per cent in 1990 and 11 per cent in 1991. The consumer truck rental product line lost \$40 million in 1991. These declines reflected a weakened economy, which led to fewer household moves, and the resurgence of a large competitor, U-Haul International, which resulted in rental rates below what they were in 1987.

An analysis of the consumer truck rental business is helpful in understanding the reasons behind the recent decline in earnings. Unlike most retail operations, such as grocery stores or services stations, Ryder's inventory of trucks is mobile, which poses a unique management challenge. Simply keeping track of the trucks requires a tremendous logistical effort.

Trucks are rented to consumers through dealers who are independent businesses such as service stations and storage facilities. Usually, truck rentals are only a small part of their business. A Ryder dealer is not required to make any capital investment; nor does the dealer incur any charges for the trucks on his lot. As a result, a dealer is motivated to keep as many trucks as possible.

Ryder's ability to keep track of its vehicles depended on two things. One was the after-the-fact batch processing of rental agreements executed by dealers at their assigned district offices. There was a two-week delay in obtaining information from these agreements. To have more timely information, Ryder depended upon the dealers to call their district office whenever a truck showed up at their location or whenever they received a reservation directly from a customer. The information supplied by a dealer was manually input into a computer-based system, called the Field Information System (FIS), that resided on an AS/400 midrange computer located at each district office. This approach to keeping track of inventory, not surprisingly, resulted in very low utilization rates.

Increasing the utilization of its vehicles was one way for Ryder to improve revenues. Demand-driven pricing was another since the demand for trucks varied by the season, varied by the month, and varied by the week. Ryder published more than 2.5 million different rates that changed daily. However, by the time the dealers got an updated rate sheet through the mail, it could be as long as a month after the initial pricing analysis had been done.

Ryder also estimated that they lost two per cent of their annual revenue because contracts were not calculated correctly. For example, it was easy for a dealer to forget to charge a customer for additional days of insurance when the customer brought the truck back later than originally scheduled.

## RyderFIRST: system overview

RyderFIRST operates on a PC installed at a dealer's location. Graphical features, menus, and prompts are extensively used to make the system as easy to use as possible. A dealer is required to use RyderFIRST continually throughout the day to conduct all aspects of Ryder's business: checking availability of vehicles, quoting prices, making reservations, opening or closing contracts. Every 15 minutes, dealer PCs dial into communications servers located in Miami. These servers coordinate transactions between the thousands of remote PCs and the AS/400 midrange

computers located in district offices.

The district-level FIS was modified to produce numerous on-screen displays and reports that integrated the point-of-sale data provided by the dealers with other relevant operational data. FIS also transmitted consolidated district data back to an IBM mainframe located in Miami for integration with other applications. One of these applications was a yield management system that used reservation information supplied by the dealers and by a centralized reservation system to automatically calculate prices that reflected regional supply and demand. Parallel to RyderFIRST's development, an enhanced yield management system was being developed to run on an IBM RISC workstation.

RyderFIRST is the latest addition to a comprehensive, integrated IS strategy to automate the consumer truck rental business. This strategy called for four major applications — RyderFIRST, Field Information System, Centralized Reservations, and Yield Management System — to be implemented on a multi-tiered system consisting of IBM mainframes, AS/400 midrange computers, PCs, LANs, and a value-added network. An overview of the integrated IT architecture that has resulted from this strategy is shown in Figure 1.

## The RyderFIRST project: key events

In order to understand the challenges involved in the RyderFIRST project, we review the key events that took place during its development. These key events, which are shown in Figure 2, are discussed below.

## Getting the initial approval

In 1979, Dennis Klinger, CIO and Vice-President of Management Information Systems, first raised the idea of developing a telephone-based system that dealers could use to transmit information on incoming and outgoing trucks in much the same way that credit card information was transmitted. This idea resurfaced a few years later as the prices of credit card approval devices declined and telecommunications got better and cheaper. In 1988, Klinger received the approval of the Ryder Board of Directors to build a system around such an intelligent credit card authorization/check guarantee machine. The system was subsequently placed in 500 dealer locations. Experience with the prototype helped to confirm some of the beliefs about what was needed to better run the consumer truck rental business. It also highlighted the need to build more value into the system for the dealers and the need to make the use of the system mandatory. These ideas were to later shape the design of RyderFIRST.

![](/api/attachments/T7BNR8FA/fulltext/images/9436652f0efb168a34a35d5250e230d2d8d0b0cc9403ad73beafaf8cdf261b81.jpg)  
Figure 1 Integrated IT architecture for Consumer Truck Rental

![](/api/attachments/T7BNR8FA/fulltext/images/83856e204b361baaad7aee2e3e367f1e479d42930ce2dc94505067b75fbdaac0.jpg)  
Figure 2 RyderFIRST project: key events

After the prototype had been in operation for about a year, Klinger sought approval for developing an enhanced dealer automation system called RyderFIRST. Original estimates for RyderFIRST were around \$20 million. While the consumer truck rental organization was generally supportive, the senior management of the Vehicle Leasing and Services Division\* saw no value in going beyond the prototype.

Two things happened to change this situation. First, Klinger was able to enlist the support of an influential executive, Dick Green, from the consumer truck rental organization. Second, a new president, David Parker, was appointed to the Vehicle Leasing and Services Division. Parker was very comfortable with technology and, having identified what Consumer Truck Rental was trying to achieve in the product line, welcomed the idea of using technology to help them.

After the project was defined, it worked its way through the management chain in the Vehicle Leasing and Services Division. Next, it had to be approved by Chairman Burns. Green and Klinger then took it to the Board of Directors. In September 1989, approval to proceed with the project was received. The cost of the project was now estimated at \$25 million. RyderFIRST was sold to the Board based on its projected ability to increase vehicle utilization, to recover additional revenues that were being lost due to mistakes in calculating rental contracts, and to reduce the data-entry costs associated with the rental agreements.

## Getting started

There were differences of opinion concerning what should be done next. Managers in IS and Consumer Truck Rental spent six months trying to decide what RyderFIRST should look like and what it should do. A senior IS executive commented:

Different people had different ideas; they would want to take it this way or that way. There was a fellow in the consumer truck rental unit at that time who was the de facto leader of this effort and he had his own opinion. He was a pretty good marketing guy but he tended to view this whole thing as a marketing tool and spent a lot of time taking it off in that direction without considering the operational aspects. He never really thought about the overall business process. The President was looking at MIS and asking when we were going to build this system and we were saying that we couldn't get a definition of what the system should consist of. There was not a clear management focus and consensus.

Early in 1990 some important management changes were made in the Consumer Truck Rental organization. One of these changes was the appointment of Wayne Mincey as Vice-President, Development and Central Operations. Mincey was a very dynamic, business-oriented executive who saw very clearly the potential benefits of RyderFIRST. He was a master at articulating the business benefits of RyderFIRST in a way that both corporate management and field operations within the Consumer Truck Rental organization could understand.

With Mincey's involvement, the project began to move forward. A group of executives from MIS and Consumer Truck Rental came together to form the core management team for RyderFIRST. Team members from MIS included Klinger and Eric Whiteside, Group Director, Development. Mincey was the key member from the Consumer Truck Rental organization. In February 1990, Whiteside initiated a formal process for defining the requirements of the system. He organized a group of people that consisted of the core management team for the project, operating management in the field, rental managers, a couple of controllers who were in charge of administering the accounting functions of the business, and some dealers who would be using the system. IBM was engaged to facilitate this requirement definition process using their joint application development methodology. From this process, a good description of what RyderFIRST should do emerged.

Following the requirements definition stage, external design specifications were developed using the same group of people with the assistance of IBM. The external design specifications were completed in June 1990.

While the external design specifications were being completed, Whiteside began to identify potential third-party vendors who could help in the development of RyderFIRST. This was necessary for two major reasons. First, Ryder did not have the expertise to build PC-based systems currently in house. Second, given the recent downsizing that had taken place within Ryder, including IS, the hiring of additional personnel was not possible. The Ryder IS organization would be responsible for modifying FIS to make it work with RyderFIRST. The third-party vendor would be responsible for the internal design and development of the dealer PC-based software and of the software for supporting all communications between a dealer PC and the AS/400 at a district office. The third-party vendor would also be responsible for configuring the hardware to Ryder specifications, shipping the hardware to dealer locations, overseeing dealer installation, and providing technical support.

The process to select a vendor for RyderFIRST was highly spirited. Each different group had its own favorite. In June 1990, MicroBILT, a small Georgia-based company that had developed PC-based systems for restaurants and retail stores, was selected to develop RyderFIRST. MicroBILT had been acquired in 1990 by a larger, more well-established company that was in the business of providing transaction processing services to financial institutions. MicroBILT was selected as a result of the user-friendliness of their systems and their ability to quickly grasp what Ryder wanted to do with RyderFIRST.

## Scheduled pilot installation delayed

Using the external design specifications as a starting point, MicroBILT was to have a pilot ready by the end of 1990. Roll-out was to proceed rapidly with all dealer sites automated by the start of the next busy season in May 1991. This did not happen. Ryder was already in their system acceptance/testing phase when they realized that major problems existed.

The delay could not have come at a worse time. Financially, the consumer truck rental business was not getting any better. Anxiously awaiting some confirmation that RyderFIRST could indeed help the current situation, senior corporate management began to monitor the progress of the project very closely.

## Testing a pre-pilot

In order to demonstrate to corporate management that significant progress was being made, a preliminary version of the system was tested with two dealers in Houston in the spring of 1991. This preliminary version was a stand-alone system—that is, it had the capability to perform all of the point-of-sale functions at a dealer's location but lacked the capability to send or receive data electronically to or from the district office.

## Revisiting the decision to invest in RyderFIRST

Given the delays in the development of RyderFIRST and the worsening financial performance of the consumer truck rental product line, the decision to proceed with RyderFIRST was revisited over and over again with corporate management. Corporate management constantly questioned the feasibility and value of the system. Every time a quarter came around and the financial results were disappointing, corporate management reevaluated whether Ryder could afford to keep funding the development of the system.

The project also had to be reapproved as a result of changes in the senior management of the Consumer Truck Rental division. In late 1990, Jerry Riordan replaced Green as the senior executive in charge of the consumer truck rental business. Riordan had previously spent several years in the management of the truck rental business. Riordan and Klinger had known each other and worked together for many years. Riordan was in the truck rental organization when the original idea for RyderFIRST came up in 1979. At that time, Riordan was very interested in pursuing this idea with Klinger but together they could not get the people above them to go along. Now, 12 years later, he had to decide whether or not to continue the development of RyderFIRST. In March 1991, Riordan and Klinger went back before the Board of Directors to obtain the authorization to continue the development of RyderFIRST. One of the original supporters of RyderFIRST, David Parker, left Ryder in June 1991. Chairman Burns assumed Parker's responsibilities.

## Reorganization in the Consumer Truck Rental organization

Before RyderFIRST was ready to be pilot tested, a major reorganization involving the consumer truck rental business occurred. The consumer line of business was separated from the commercial line of business and made a separate business unit. Riordan became the senior vice-president and general manager, Consumer Truck Rental. As a separate business unit, Consumer Truck Rental decided to organize its field operations into 20 geographical districts. Previously, its field operations were combined with commercial's field operations in 80 districts. This reorganization had many consequences. Organizationally, a much smaller management staff would be responsible for the consumer line of business. Technically, the intensity of communications between a district and its associated dealers would increase fourfold. RyderFIRST would have to be modified to work with this new organizational structure.

## Installing the pilot

After a delay of nine months, RyderFIRST was piloted in the northwest district in September 1991. This was the first live test of the communication features integrated with the point-of-sale features. As a result of some subtle problems in the communications software, a very small percentage of the transactions were getting lost. In November 1991, Klinger decided to delay the roll-out that was scheduled to begin in January 1992, until these problems were corrected. Burns was not happy about this delay. He decided to send a group of Ryder senior executives to the northwest district office located in Seattle in January 1992, to provide an independent assessment of RyderFIRST.

Fortunately, the problems with the lost transactions were corrected by the end of 1991 and the system began to function properly. When the visiting senior executive team met with the northwest district's management and operations staff as well as with the dealer council, they heard some incredible stories — how for the first time ever the district had been able to get UPS all of the trucks that they wanted over Christmas and how the district had been able to secure a rental by tracking down a customer using only the phone number supplied by a dealer through RyderFIRST. They heard first-hand from the dealers that they had no problems using RyderFIRST.

The trip proved to be a turning point in getting corporate management to believe and accept RyderFIRST. All the members of the visiting group were very excited about the system and its potential. The team shared what it had learned with Chairman Burns upon its return.

Ryder decided to proceed with a moderate roll-out schedule in order to spread the cost over a longer period. By the second quarter of 1992, however, the roll-out speed had been doubled because the results were so positive and, financially, Ryder was doing much better. The roll-out of RyderFIRST was completed by April 1993.

For implementing RyderFIRST in each district, a six-month schedule was developed. It included planning sessions with the district's managers, site surveys of dealer locations, installation of equipment, and training. Dealer training had proceeded smoothly. Typically, hardware was delivered to a dealer about a month before the dealer was expected to begin using RyderFIRST. The dealer was brought in for formal classroom training a few days before he was to begin conducting business using the system. The dealer was encouraged to go through the computer-based training that came with the system.

Ryder was responsible for all dealer training. MicroBILT was responsible for the installation and maintenance of hardware. MicroBILT was also responsible for a help-line that the dealers could call if they had a problem with the system. If a problem was clearly a business problem, it was referred to Ryder. All other problems were handled by MicroBILT. MicroBILT was also responsible for providing enhancements to RyderFIRST. Since the roll-out began in 1992, two new versions of RyderFIRST have been released.

RyderFIRST was delivered close to its estimated price of \$25 million. Because of declining hardware prices, the dealers were given more computer power than originally planned for. Of the \$25 million, the hardware cost is a little more than half. The development cost is relatively moderate — around \$3.5 million. The cost of installation and maintenance of the hardware was \$4 million. The remaining cost was for the support of RyderFIRST over five years. RyderFIRST has delivered all of its promised benefits — increased utilization; increased revenues by capturing all relevant charges on rental contracts; and reduced headcount for data entry. The payback period for RyderFIRST is estimated to be two years.

## The impacts of RyderFIRST

Actions taken to return the Consumer Truck Rental unit to profitability were beginning to pay off by the end of 1992. The following appeared in the Miami Herald, December 1992:

Consumer truck rental revenues went up by 15 per cent in the third quarter, and this year, the unit will lose \$15 million compared with \$40 million in the previous year. M. Anthony Burns calls it ‘the best turnaround in the whole company’. He said the unit’s objective is to break even or make a small profit in 1993.

RyderFIRST has been credited with facilitating the turnaround in the Consumer Truck Rental unit. The following announcement on RyderFIRST appeared in the December 1992 issue of Ryder Dealer:

Our new computer system, RyderFIRST, made its debut at the Northwest dealers in January. While we had some early anxious moments, the system started to deliver every promised payback. Throughout the year we installed this state of the art system at over 2,000 dealers. After taking time to settle in, dealers with the automation system have higher revenues, higher utilization, lower transfer cost, and cash higher commission checks.

The availability of timely management-oriented information, along with the ability to communicate between the district and its dealers, has enabled fundamental changes to be made in the way that Consumer Truck Rental does business in the areas of inventory control, pricing, and marketing. These changes are described briefly below.

## Improved utilization through better inventory management

RyderFIRST is proving to be an extremely effective tool for inventory management. A dealer coordinator explains how she now manages the inventory for her assigned dealers:

On Monday morning, I normally go through the dealers' inventories and see what they have on their lots. I compare their target inventory levels, that have been set by the company, and the actual inventories that they have on their lots. Also a report is produced each week that compares their actual revenue per unit numbers with their target numbers. If a dealer is below his revenue per unit target, that is a good indication that he has too many trucks. A dealer may say that he is not making enough money because he doesn't have enough trucks. Well, this report says whether this is true or not.

The electronic mail feature within RyderFIRST has also been used as an inventory management tool. When there is an inventory overage or shortage, the dealer coordinators will send a message to the dealers to let them know about the problem and will provide suggestions on how the dealer can correct the problem. A Consumer Truck Rental senior executive illustrated how this feature has been used as an effective inventory management tool:

If all of a sudden we see a dip in supply in an area, the dealer coordinator can send a message something like ‘Critical shortage of trucks in the Miami–Fort Lauderdale area. We need intrastate rentals to Miami–Fort Lauderdale. We will pay a \$50 bonus for the next 100 reservations going to Miami–Fort Lauderdale.’ You can just stand back and watch the reservations start coming in. Money motivates people in this world. All of a sudden, the dealer will try to close the deal on anybody going anywhere even remotely near Miami–Fort Lauderdale.

RyderFIRST has also improved inventory management by helping the districts manage transfers more effectively. A district manager explained:

Because we are on top of inventory for the first time since I have been with this company, we are spending money to move trucks from one city to another, which is something that we would have never done in the past. Because we know where our trucks are and we are able to monitor our reservations, we are able to be proactive in a way not possible before. So, we are spending money that we normally would not have spent, but these expenditures are ‘good’ in that they are in pursuit of additional revenues. We are making some moves today that two years ago people would have thought were insane.

## Dynamic pricing policy

Prior to RyderFIRST, communicating the pricing, which was all by paper, was too slow for immediate response and too easy to ignore and too hard to implement correctly. Today, changing prices is as easy as pushing a button. It allows Ryder to react to economic or competitive situations instantaneously and to implement pricing changes at the same time in all of its dealer locations. A district manager commented:

We now consider whether to raise local prices. Before RyderFIRST we would never have dreamed of doing that because it would be too cumbersome. We would have had to make hundreds of phone calls to our dealers. Now, communication of new prices takes place automatically. Another reason that we wouldn't have changed prices is that we would not feel comfortable that we were making the right decision. Now, we have more information to deal with. We have the confidence that the information we are using is good enough to make a decision on. In the past I didn't have the confidence to make a decision on something like that. We didn't have information that made us feel warm and fuzzy.

We now conduct weekly pricing surveys of our competitors. I would not have attempted to have anyone do weekly pricing surveys without knowing that once we had the information to make the decision, it could be done quickly. It is killing competition; they are screaming about it.

Not only can new prices be communicated instantaneously, but different prices can be set for different markets. A pricing strategy can strive to improve utilization and lower transfer costs at the same time. By making the right pricing decision, we not only can make money on a rental leaving Tampa in the winter but we also don't have a truck sitting in Tampa that can't be rented out for another three months.

## More effective marketing

The ability to close deals involving customers who had previously been given quotes was significantly impacted by RyderFIRST. Dealers are encouraged to capture the names and phone numbers of all persons who make an inquiry. These leads are given to representatives at the district office for follow-up. It is estimated that the number of leads has more than doubled.

These fundamental changes led to an increase in revenues. In the first quarter of 1993, the northwest district was reporting revenue increases across the board — local rental revenues, average revenue per local rental transaction, total one-way rental revenues, and average revenue per one-way rentals were all up. A district manager commented on RyderFIRST's contributions:

Revenues can increase as the result of hundreds of factors and it is difficult to unequivocally tie those increases to RyderFIRST. What we have seen is that revenues have gone up in the districts where RyderFIRST has been implemented and have declined in those without RyderFIRST. Take the northwest district, for example, where revenues have increased. Revenues could be up because of a more favorable economic climate or because the management in the Seattle office is more effective. However, as this pattern repeats itself in other districts following the implementation of RyderFIRST, there is more evidence that RyderFIRST is directly contributing to improved performance.

## Managing stakeholder relationships: key challenges

RyderFIRST was a high-priority, high-profile project that involved four major stakeholders: the RyderFIRST project team (which consisted of IS and Consumer Truck Rental), Ryder System corporate executives, MicroBILT, and the dealers. A key challenge facing the RyderFIRST project team was the management of the relationships between itself and the three other stakeholders. The major issues that had to be addressed in the management of each of these relationships are discussed below.

## Ryder System corporate executives and RyderFIRST project team

Acquiring and maintaining the support of Ryder System corporate executives (and the Board of Directors) was a major challenge for the project team. It is widely accepted that positive signals from the CEO's office contribute significantly toward establishing a conducive environment for developing strategic IT applications (Jarvenpaa and Ives, 1990). In fact, the lack of top management support has been shown to be the strongest obstacle in a company's effort to create strategic systems (King et al, 1989). RyderFIRST did not receive the level of support from the corporate management team that has been advocated in the IT literature. The one champion from Ryder System's corporate executive ranks, David Parker, left the company midway through the project. Therefore, the project team had to continually deal with the risk that the development of RyderFIRST might be stopped at any point.

The urgency of the project had made everyone optimistic about how long it would take to complete this project. Over time, the project team realized that the original estimates were unrealistic. Ryder System executives, however, expected the project team to meet the schedules it had originally specified. Dealing with the unrealistic expectation that the project could be completed by the end of 1990 represented a major challenge for the project team.

## Dealers and RyderFIRST project team

The ultimate success of RyderFIRST rested on the independent dealers accepting it. This caused three major concerns. First, a majority of dealers had no experience at all with PCs. Second, most of the benefits from using RyderFIRST would accrue to Ryder. RyderFIRST would allow Ryder to exert a level of control over the dealers that had not been possible earlier.\* Third, the Consumer Truck Rental had decided to impose a monthly usage fee for the system. Therefore, effectiveness in managing the relationship with the dealers would ultimately be judged by the dealers' evaluation of the system, the ease with which they could use the system, and Ryder's ability to support the dealers on an ongoing basis.

## MicroBILT and RyderFIRST project team

RyderFIRST was a high-risk project (Cash et al, 1992). It was large in scope, utilized unfamiliar technology, and the objectives could only be broadly defined at the outset. MicroBILT was responsible for developing some parts of the system; Ryder was responsible for developing others. The RyderFIRST project team had to ensure that the portion of the system that was developed by MicroBILT would work well within Ryder's existing IT architecture. Ryder had no prior experience in managing these 'arm's-length' deliverables.

Another major challenge faced with regards to MicroBILT was the building and maintenance of a partnership relationship. A partnership describes a relationship that reflects a long-term commitment, a sense of mutual cooperation, and shared risk and benefits rather than an arm's-length relationship where the failure of either party to deliver on commitments can be resolved through litigation (Henderson, 1990). The basis for such a partnership, as described in more detail below, did not exist when MicroBILT was selected to develop a major part of RyderFIRST and had to be created once the project was underway.

## Strengths needed to meet the challenges

In meeting the challenges faced during the development of RyderFIRST, some strengths possessed by Ryder contributed significantly. Two critical strengths were a well-established IS–Consumer Truck Rental partnership and a strong IT capability. We describe these organizational capabilities below.

## A well-established IS-Consumer Truck Rental partnership

It has long been acknowledged that the successful delivery of information systems products and services, particularly strategic information services, requires an effective partnership between IS and line management (Henderson, 1990; Lasher et al, 1991). The existence of a strong, well-established partnership between IS and Consumer Truck Rental was perhaps the most important contributing factor to having an effective RyderFIRST project team. A strong partnership existed between Klinger and Whiteside from IS and Green, Riordan, and Mincey from Consumer Truck Rental. Without this partnership, the RyderFIRST project team would never have gotten approval to proceed; neither, would it have been able to overcome the problems that emerged during RyderFIRST's development. The RyderFIRST experience provides an unusual opportunity to examine a successful partnership between IS and line management in action.

Previous research on the IS-line management relationships has identified six major characteristics that can be used to determine the strength of a partnership: mutual benefits, commitment, predisposition, shared knowledge, distinctive competencies and organizational linkages (Henderson, 1990). We use these characteristics to describe the nature of the IS-Consumer Truck Rental partnership as it related to RyderFIRST.

RyderFIRST provided mutual benefits to IS and Consumer Truck Rental. For Consumer Truck Rental, the system attacked the very problems that were central to the business. If RyderFIRST was not successful, there would likely be no more chances to try again. For IS, this was an opportunity to make a tangible, visible contribution to the business and to finally realize a vision for using IT in the consumer business that had been articulated many years ago.

A high level of commitment to RyderFIRST was evident in both IS and Consumer Truck Rental. While these two groups often disagreed with each other within the project team, they presented a united front to the outside world. Perhaps the most striking aspect of commitment was the fact that senior management in both IS and Consumer Truck Rental put their careers on the line with this project. IS and Consumer Truck Rental assumed equal responsibility for the success or failure of RyderFIRST.

Predisposition is defined as the attitudes of the partners on key issues and the level of trust existing among the members of the partnership. IS and Consumer Truck Rental had a long-established relationship going into the RyderFIRST project. They had worked together on many projects in the past, the most recent being the successful development and implementation of the Field Information System. As a result, a high level of trust existed between IS and Consumer Truck Rental senior executives. This trust, along with a number of long-term personal friendships between executives in IS and Consumer Truck Rental, helped to get the project through many of the rough spots that it faced.

The RyderFIRST project team scored very high on the level of shared knowledge needed to make the project a success. IS had long been involved in strategic planning activities for Consumer Truck Rental. In fact, Klinger was part of a task force to develop a strategic plan for Consumer Truck Rental just prior to the start of the RyderFIRST project. The experiences gained by both IS and Consumer Truck Rental during the implementation of the Field Information System also substantially contributed to the building of a strong shared knowledge base. IS gained valuable knowledge about the business of renting trucks. Consumer Truck Rental gained valuable knowledge about the dynamics of system development. And of course, the experiences with the precursor of RyderFIRST, the intelligent credit card authorization/check guarantee machine, provided both IS and Consumer Truck Rental with invaluable insights on the requirements of a successful dealer automation system.

Each party to the partnership had distinctive competencies that were critical to the success of RyderFIRST. IS brought the technical know-how and an understanding how IT could be used to improve business operations. Consumer Truck Rental brought expertise in the business area, the resources necessary for the project, and the ability to articulate the business benefits of the system in a way that corporate management as well as field personnel could understand. The project team was adept at bringing these competencies together as needed.

Organizational linkages between IS and Consumer Truck Rental had been established prior to RyderFIRST. In 1988, Klinger persuaded Consumer Truck Rental to set up a special group of individuals with extensive field experience to work with IS in the design, testing, and implementation of the Field Information System. This group was in place to provide the same level of assistance for RyderFIRST. The acceptance of RyderFIRST by the dealers (discussed in more detail below) and the ease with which the roll-out was accomplished attests to the importance of this group. Within the context of the RyderFIRST project itself, linkages between the two organizations were pervasive. This can be seen in the development of the external design specifications, the selection of MicroBILT, and the management of the MicroBILT–Ryder relationship.

## A strong IT capability

A strong IT capability has been found to be an important contributing factor to the success of strategic systems (Copeland and McKenney, 1988; Johnston and Carrico, 1988; Runge, 1988; King et al, 1989). The RyderFIRST project team benefited greatly from the strong IT capability that existed within Ryder. The strong IT capability resulted in part from the information systems that were already in place. The Field Information System was an essential first step. With that in place, RyderFIRST could proceed. Without it, RyderFIRST would have been impossible. The wealth of experience that the IS organization had gained through the development of such systems as FIS resulted in a high level of technical competence that was available to the RyderFIRST project team.

Also contributing to the strong IT capability was the capable, proactive leadership provided within IS. Through this leadership, a strong integration between IS and the strategy of the consumer business had been established. IS was valued for the contributions that they had made. Thus, it was not surprising that an environment had been created where the strategic IT opportunities for this business could be identified and vigorously pursued.

## Actions taken to meet the challenges

We now discuss the actions that were taken to address the challenges encountered while developing RyderFIRST. These actions benefited to a considerable extent from the above strengths possessed by Ryder.

## Managing the corporate executives-RyderFIRST relationship

The importance of having champions for strategic systems is well established (Runge, 1988; Reich and Benbasat, 1990; Beath, 1991). Beath (1991) defines champions as ‘managers who actively and vigorously promote their personal vision for using information technology, pushing the project over or around approval and implementation hurdles’. As discussed earlier, the absence of sustained championship from corporate management was a key challenge in developing RyderFIRST. However, the strong partnership that existed between IS and

Consumer Truck Rental led to the emergence of champions from the line management. Klinger was able to enlist Dick Green as a champion. Green represented the views of all of the people in the consumer line of business who had always wanted a system like RyderFIRST. He was willing to take a chance. The combination of Klinger pushing, Green being a really innovative individual, and Parker willing to listen to Green and Klinger was crucial in getting the approval of corporate management to begin RyderFIRST.

After Green left, Mincey took over the role of champion from the line function. Mincey impacted the project in a number of key ways including getting the project going after it was stalled early in the development and, along with Riordan and Klinger, kept corporate management committed to the project. When corporate management expressed concerns about RyderFIRST, Klinger and Mincey would go visit them together to address their concerns. Mincey would strongly reaffirm his belief that RyderFIRST was absolutely essential to successfully running the consumer line of business. Klinger would provide a realistic assessment of how the development was progressing. He tried to make corporate management understand that the testing of RyderFIRST — as good and as thorough as they tried to make it — was unlikely to fully simulate the complexities of the real world in which RyderFIRST would operate. Unexpected problems were therefore likely to occur. During this period, Riordan also made his support of the project well known to corporate management.

In addition to the above actions to manage the expectations of corporate executives, corporate support for RyderFIRST was sustained by actively marketing it through pilot tests, periodic demonstrations of the system to corporate management, and visits by corporate executives to the pilot site. Individually, each of these incidents bought the project team some time, and cumulatively, they helped sustain a high level of corporate management support throughout the project.

## Managing the MicroBILT-RyderFIRST relationship

Monthly executive status meetings at Ryder's corporate headquarters were held between the senior executives involved with RyderFIRST from both organizations. In attendance from MicroBILT were the President, his Executive Vice-President of Industry Development, and the project manager for RyderFIRST. Whiteside chaired the meeting. Mincey attended the meetings religiously. Others in attendance from Ryder were the RyderFIRST project manager and Ben DiNatale, who was responsible for the implementation of RyderFIRST. Klinger and Riordan attended some of the meetings.

After it was discovered that RyderFIRST would not be ready for pilot testing at the end of 1990, daily meetings via conference calls were held by the project managers and development staff from both Ryder and MicroBILT. Ryder felt that this gave them much tighter control over the project.

Some of the conflict that existed between Ryder and MicroBILT could be traced to different interpretations concerning what was to be delivered. MicroBILT felt that it had delivered what was asked for and Ryder did not. Some of the conflict could be traced to unanticipated events such as the reorganization in summer 1991 that required some modification of software. And some of the conflict could be traced to the fact that MicroBILT did not have an understanding of the truck rental business. MicroBILT was occasionally unaware of requirements that the Ryder project team thought were intuitively obvious.

A senior Ryder executive commented on working with MicroBILT during this period:

Those were very touchy times and I think Ryder tried to do those things that would make the system work. It was really a question of willpower. It is mostly whether or not you want to do it. There were two people at the party and neither one was willing to walk away from obstacles that surfaced. But there were some trying times. There were a lot of people involved with a lot of different personalities and at times they would feel that they had gone as far as they could. Some people may question our marriage with MicroBILT. We had good arguments. People in marriage have arguments and then they make-up and I think we did that very well.

Many of the problems in managing the relationship with MicroBILT can be traced to a weak partnership at the beginning of the project. There was no basis for trust since MicroBILT and Ryder had never worked together. MicroBILT had very little knowledge about the truck rental business and few organizational linkages were put in place. The basis for developing a strong partnership was present, however. The benefits to MicroBILT for working with Ryder to deliver RyderFIRST were enormous. This was the largest contract that MicroBILT had ever been given. The experience gained and the exposure received from the RyderFIRST project would greatly facilitate the growth of MicroBILT. There was a strong personal commitment from the senior management on both sides. In the end, this personal commitment was more important to the successful completion of the project than the contract that specified the legal commitments. And, of course, MicroBILT brought the critical skills related to PC development that were required for the project.

Over time, MicroBILT gained more knowledge of the business and Ryder created more formal organizational linkages to facilitate better communication between the two sides. By diligently and aggressively working together to solve problems, a level of trust began to develop. Project managers from Ryder as well as MicroBILT took great pains to ensure that, despite the various areas of disagreements, project participants from the two sides got along with each other. There was considerable give-and-take during the project. The excellent interpersonal relationships, along with the strong and mutual desire to succeed, played a key role in the successful development of RyderFIRST. The project manager from MicroBILT remarked:

If you have 20 people . . . you are not going to get everyone to get along with everyone else. But what is important is that the vast majority of people actually get along . . . That is what made it work, people getting along.

Today, a strong, ongoing partnership exists between Ryder and MicroBILT. MicroBILT will make necessary enhancements to RyderFIRST and provide first-level support to dealers in the foreseeable future.

## Managing the dealer-RyderFIRST relationship

As mentioned above, a major concern in the RyderFIRST project was whether the dealers would willingly accept the system. To address this concern, a group of dealers was involved from the very beginning in the design of the system. This was a somewhat controversial thing to do since one of the objectives of RyderFIRST was to provide more dealer discipline. Some individuals within Consumer Truck Rental felt that the dealers might not like what they saw and they were not sure that they wanted to show their cards. IS management made a convincing argument that

RyderFIRST could not be successful without including them. In addition to involving a set of dealers in the design session held in Miami, an early prototype was developed and shown to dealers across the country. Their reactions provided more input into the design specifications. In order to build up excitement for the system, Ryder launched a massive public relations campaign and grass-roots consensus-building effort with dealers. At regional and national dealer council meetings, Ryder talked extensively with the dealers about what they were doing, what was going on and why RyderFIRST was important to them. At the national dealer conventions, prototypes were put on display. As one executive stated:

We did all of those types of things to get their fingerprints all over it so that there was ownership.

The pre-pilot was also an essential step in delivering a dealer-friendly system. Many changes were made in the design of RyderFIRST as a result of watching how the dealers in Houston used the system. The pre-pilot ensured that there was value in the system for the dealers.

As a result of all these efforts, getting dealers to accept the system did not prove to be a major problem. Only a very small percentage of the dealers were unwilling or unable to learn how to use the system or refused to pay the monthly charges. As one executive commented:

There are a lot of dealers out there who are really proud of having RyderFIRST. I have seen some remarkable changes in people who never thought they could do anything like this. They are now making recommendations about how to run it. It has changed their lives.

## Conclusions

The strategic benefits that IT can provide are now widely recognized. However, obtaining such strategic benefits from IT is no easy task, especially in organizations facing financial difficulties. Poor financial performance increases the urgency for the system. The situation is further aggravated by the multiplicity of stakeholders involved in potentially strategic systems. In addition to the IS group and the line function, corporate management, vendors of hardware and software, and other external organizations, such as customers, suppliers and even competitors, may be involved.

In this paper, we have described the challenges faced during the development of one strategic system, RyderFIRST. This system links Ryder with its dealers and has provided several strategic benefits to Ryder as well as to the dealers. However, the development of this system encountered several difficulties due to the need to manage relationships with corporate management, dealers, and the external software vendor, MicroBILT.

Ryder possessed two key strengths which went a long way in addressing the challenges faced. First, there was a well-established partnership between IS and the management of the line function, Consumer Truck Rental. IS had a good track record and IS executives got along very well with executives from Consumer Truck Rental. Second, Ryder had a strong IT capability upon which RyderFIRST could be based.

The successful development of RyderFIRST also depended on several actions Ryder's project management team (including executives from IS and Consumer Truck Rental) took during the project to manage the relationships with each of the other three stakeholders — corporate management, MicroBILT and dealers. In order to sustain corporate management support, they kept the expectations of corporate executives at a realistic level, carefully marketed the benefits of the system, and periodically demonstrated progress through pilot tests and other means. Management of the relationship with MicroBILT was based on a mutual desire to succeed along with good interpersonal relationships and frequent interactions between participants from the two sides. Management of the relationship with the dealers was based on keeping them involved throughout the project, actively selling the system's benefits to them, and ensuring that the system was extremely easy to use.

So far, RyderFIRST seems very much like the systems that have become part of the strategic IT folklore. It has contributed to the business performance of Ryder's Consumer Truck Rental division by significantly improving inventory control, pricing and marketing. However, several difficulties were encountered while developing the system. Learning from the RyderFIRST experience, executives embarking upon the development of potentially strategic systems would do well not to underestimate the obstacles that may lie ahead. They may also benefit from emulating some of the actions that led to the success of RyderFIRST.

## References

Beath, C (1991) 'Supporting the information technology champion' MIS Quarterly 15, 3, pp 355–374.

Cash, J., McFarlan, W., McKenney, J and Applegate, L (1992) Corporate Information Systems Management: Text and Cases Irwin, Boston, MA

Copeland, D and McKenney, J (1988) 'Airline reservations systems: lessons from history' MIS Quarterly 12, 3, pp 353–371

Henderson, J (1990) 'Plugging into strategic partnerships: the critical connection' Sloan Manage Rev Spring, pp 7–18

Jarvenpaa, S and Ives, B (1990) 'Information technology and corporate strategy: a view from the top' Inf Systems Res 1, 4, pp 351–376

Johnston, H and Carrico, S (1988) 'Developing capabilities to use information strategically' MIS Quarterly March, pp 37–48

King, W, Grover, V and Hufnagel, E (1989) 'Seeking competitive advantage using information-intensive strategies: facilitators and inhibitors' in Laudon, K C and Turner, J A (eds) Information Technology and Management Strategy Prentice-Hall, Englewood Cliffs, NJ

Lasher, D, Ives, B and Jarvenpaa, S (1991) 'USAA-IBM partnerships in information technology: managing the image project' MIS Quarterly December, pp 551–565

Reich, B and Benbasat, I (1990) 'An empirical investigation of factors influencing the success of customer-oriented strategic systems' Inf Systems Res 1, 3, pp 325–347

Runge, D (1988) Winning With Telecommunications International Center for Information Technologies Press, Washington, DC
