---
otero_id: 11676
otero_key: "Z3RDG76Y"
title: "Modernization of Passenger Reservation System: Indian Railways’ Dilemma"
authors: "Shirish C Srivastava; Sharat S Mathur; Thompson SH Teo"
year: "2007"
journal: "Journal of Information Technology"
doi: "10.1057/palgrave.jit.2000112"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Teaching case

# Modernization of passenger reservation system: Indian Railways’ dilemma

Shirish C Srivastava<sup>1</sup>, Sharat S Mathur<sup>2</sup>, Thompson SH Teo<sup>1</sup>

<sup>1</sup>School of Business, National University of Singapore, Singapore, Singapore; <sup>2</sup>Centre for Railway Information Systems, Indian Railways, New Delhi, India

Correspondence:

SC Srivastava, School of Business, National University of Singapore, 1 Business Link, Singapore, Singapore 117592, Singapore.

Tel: þ 65 6516 3038;

Fax: þ 65 6779 2621;

E-mail: shirish@nus.edu.sg

## Abstract

This teaching case discusses the challenges being faced by the technology managers at Indian Railways (IR) in the current scenario of a resurgent national economy coupled with increasing customer expectations. In the face of growing competition from road and low-cost airlines, to retain its customers, IR has responded by changing its business rules. The Railway Ministry expects a rapid response from Centre for Railway Information Systems (CRIS) to incorporate all these changes in the passenger reservation system (PRS). The old PRS, which is time-tested and reliable, and has been serving the customers’ needs for nearly two decades, is now proving to be relatively inflexible to match the rapidly changing business requirements. Although the current scenario of a constant need to change the programming logic of PRS has been making maintenance tougher for CRIS officials, they have realized that PRS is a time-tested, proven, and reliable technology. Though they would be happy to replace the old PRS with a new state-of-art system that would provide them greater maintenance flexibility, the repercussions associated with possible failure of the new system are far too serious. The case exhibits the current dilemma being faced by the head of CRIS, the umbrella agency for information technology (IT) implementation in IR: whether IR should continue using the old PRS technology with its inherent shortcomings, or should it take the risk and go in for a wholesale replacement with a new state-of-art technology which would provide greater maintenance flexibility?

Journal of Information Technology (2007) 22, 432–439. doi:10.1057/palgrave.jit.2000112

Keywords: railways; government; technology change; legacy system; flexibility; customer; railroad; India

Of the 11 million passengers who climb aboard one of 8,520 trains each day, about 550,000 have reserved accommodation. Their journeys can start in any part of India and end in any other part, with travel times as long as 48 hours and distances up to several thousand kilometers. The challenge is to provide a reservation system that can support such a huge scale of operation – regardless of whether it is measured by kilometers, passenger numbers, routing complexity, or simply the sheer scale of India (Center for Railway Information Systems Website, http://www.cris.org.in)

## Introduction

A Saturday afternoon at the Centre for Railway Information Systems (CRIS)

A fter working in various capacities as an Indian Railway officer, A.V. Ramasundar joined the CRIS as its administrative head in 2004.<sup>1</sup> Since its inception in

1986, CRIS has been entrusted with the job of developing, implementing, and maintaining centralized IT applications for the Indian Railways (IR). With over 350 personnel, CRIS has its headquarters in New Delhi, the capital of India, along with five other regional offices spread evenly across the nation.

Table 2 Impact of PRS implementation

<sup>a</sup>From official documents.

Looking outside through the clear windowpanes of his office, Ramasundar realized that the next few months were going to be tough for him. From the day Ramasundar joined CRIS, the turn of events in the nation (India) and the organization (IR) had been rapidly changing, which had now precipitated into a difficult situation for him. He was currently struggling with the options available before him to decide the future course of action for the IR’s passenger reservation system (PRS), one of the largest and most important information systems of IR. Put simply, his dilemma was: how could he modernize the PRS smoothly without any hitches for the passengers and IR?

Not that the performance of the PRS was in any way unsatisfactory to the casual viewer. On the contrary, it had been efficiently handling the huge and rapidly increasing passenger volumes at the IR, and in recent years, had been spreading across the country at breakneck speed. It could provide reservation in any train managed by the IR from any originating station in the country to any destination from its 5000 terminals placed in over 1350 locations across the country, up from only 600 locations 5 years ago. While the PRS could be accessed from the busiest railway stations in the country, an intending passenger in a remote hill town, 500 km from the nearest railway station, could also walk over to the neighborhood PRS office, get a reservation for the train journey of his choice, and walk home with his ticket, through a 2-min transaction. The objectives of PRS (as envisaged by the IR) and the impact of PRS implementation are given in Tables 1 and 2.

Table 1 Objectives of PRS<sup>a</sup>

<table><tr><td>Objectives of PRS</td></tr><tr><td>1. Service to publica. Reduction in time and expense involved in ticketingb. Quicker service to passengersc. Quick and easy availability of information regarding trains and accommodation availability2. Better working environment for staff3. Reduction in scope for unethical practices in reserving accommodation</td></tr></table>

India’s economic growth, on an upswing since the mid-1980s, had taken a sharper upturn in 2003–2004. From a traditional growth rate of about 5%, it began to grow at over 7%, and the trend is likely to continue in future. IR’s passenger traffic, hitherto growing at about 3% annually, began to show rates of growth of over 6%. Low-cost airlines began to compete with the upper end of the railway passenger segment. The Government of India introduced a comprehensive highway improvement program, and the specter of long-distance road travel loomed on the horizon. To retain its customers, IR responded by changing its business rules to manage the new reality. Passenger upgrades were introduced, age-old wait-listing rules were changed, and the Ministry expected a rapid response from CRIS to incorporate all these changes in the PRS. Here the cracks in PRS began to show. Written almost entirely in C, dependent on a mainframe operating system, and revolving around now unpopular Transaction Processing (TP) monitor software, changing the application was a tedious process. Indeed, one recent day Ramasundar had been forced to warn the IR’s Board of Directors that too many changes in the program logic, demanded all at once, could seriously destabilize the PRS as it existed today.

P.R. Chandran, head of the Information Technology (IT) Directorate and technology policy maker in the Ministry of Railways, agreed with Ramasunder that the present technology platforms were obsolete and needed to be changed. Newer technology would be able to provide more facilities to the passengers and help IR remain competitive.

The new technology being considered for adoption was:

\- Component-based architecture in place of the decadeold, rather monolithic application architecture that was in use. This technology would provide the application with much-needed flexibility to change with changing business rules, enabling IR to respond quickly to passenger needs.

\- RDBMS-based data management, in place of the older file-based data management sub-system being used. A decade ago, RDBMSs had been expensive and resourceintensive, and the desired user response times had been difficult to obtain in large RDBMS-based applications. Nowadays, hardware resources were no longer a constraint, and the flexible data structures possible with an

<table><tr><td>Before PRS Implementation</td><td>After PRS implementation</td></tr><tr><td>1. Reservation possible only at the train originating station. From other stations request sent through telegram.</td><td>1. Immediate reservation from any station to any station over IR, possible from any PRS counter.</td></tr><tr><td>2. Long queues and long waiting time for passengers.</td><td>2. Shorter queues because of availability of large number of universal PRS counters.</td></tr><tr><td>3. Possibility of mistake very high as details written manually in register, leading to passenger inconvenience.</td><td>3. Possibility of mistakes reduced as the information printed on the ticket can be checked by the passenger.</td></tr><tr><td>4. Possibility of booking clerk not giving correct ‘availability position’, since the waitlist information is not universally available.</td><td>4. Information regarding availability status is universally available over touch screens, Internet, and phone.</td></tr><tr><td>5. Possibility of unethical practices while allotting reservation, since information access is restricted.</td><td>5. Possibility of unethical practices largely eliminated.</td></tr></table>

RDBMS core would greatly enhance overall application flexibility.

\- Universal standards-based system communication interfaces (in place of systems unique to IR) that would enable partner organizations to access information in a controlled fashion from the PRS. In future, these interfaces could be used to tap into the larger travel management community to offer innovative travel packages to the passengers.

The introduction of this new technology would result in a flexible application, tuned to the future needs of IR, which was itself in the midst of a transformation to a more responsive, customer-centric organization.

Top management in the Railway Ministry had already indicated their willingness to invest in IT projects. Punit Kumar, the Minister’s Executive Officer enunciated the Railway Minister’s stand on the subject:

The present climate in the Government is extremely ITfriendly. If we want, we can give IT projects on Indian Railways a major boost at this time. Well thought out proposals for IT systems, aligned with our current priorities, would be considered positively: the Government is willing to invest appropriately.

P.L. Gaur, head of the PRS group in CRIS, who oversaw the operation of the PRS, as well as liaising with all stakeholders, was of the more moderate view. He believed that the present PRS technology platform, incorporating a combination of low cost and high performance was hard to beat. In his opinion, a steady technological evolution, without destabilizing the existing PRS, was the need of the hour. The existing PRS had been serving the customers quite satisfactorily, and would continue to do so now. Moreover, the benefits emerging from changing over to a DBMS from the current flat file system might not be commensurate with the resources expended. Above all, there would always be a risk of a drop in system performance. Considering the fact that PRS handles well over 1 million transactions everyday, the fear of a public backlash in case of non-performance of the new system appeared to be completely justified.

Commenting on the subject, PRS group leader Amrita Agarwal, who led the PRS technical team, responsible for maintaining and enhancing the application software, said,

Believe me, no one is more concerned about technology obsolescence than my group. After all, we have to maintain the application, and we face the heat in case of any problem. We are also fully aware of the business implications of a prolonged breakdown in the application: it could lead to a severe disruption of all types of rail services in the country. That is precisely the reason we advocate an informed, if cautious, approach.

Ramasundar believed that switching over to a new stateof-the-art system could be helpful in providing the muchneeded flexibility and the desired level of integration with the Internet-based reservation system. Moreover at present, the Minister and the government were viewing IT favorably, which was an added opportunity to solicit investment for the new PRS. On the other hand, he was not really sure if it was worth discarding an already working, proven, and reliable PRS in anticipation of future requirements. Being a responsible government official, he also fully understood the implications of unintended disruption of services due to poor performance of a completely new system. There would also be problems of retraining the service staff whose numbers had been increasing significantly in the last few years. Besides, there were no heuristics for him to estimate the time window for realizing the anticipated benefits from the new system. Faced with this dilemma, Ramasundar started flipping through the file containing recent statistics of PRS performance, in the hope of finding a solution to decide the future of the IR’s PRS.

## The country and the organizations: India, IR, and CRIS

India is a country of distances and of great travelers. Ever since the introduction of trains in 1853, Indians have thought nothing of hopping onto trains to undertake journeys, often over distances of 1000 km or more. Even the poor rural folk use the ‘rail-gaadi’ (railway train) regularly. Road transport is generally restricted to short journeys of less than 250 km and air transport till recently was limited to a few big cities.

IR is a Government agency. It operates all passenger and freight rail services in the country. Railways are the principal mode of passenger and freight transport in India and have played an important role in nation building. The current importance of IR in the process of national development can be gauged from the fact that the Indian government has two budgets that are presented to the parliament every year: the general budget which is presented by the Finance Minister and includes the estimates and expenditures of the entire central government except the Ministry of Railways; and the railway budget which is presented by the Railway Minister and details the estimates and expenditures of only IR.

IR is among the largest railway systems in the world. Currently it has 63,140 route kilometers of rail track, over 8000 railway stations, and employs around 1.4 million people – making it the largest single employer in India. IR currently handles around 16 million passengers per day (almost 6 billion originating passengers in a year) in over 9500 passenger trains. Nearly 1 million passengers per day get their accommodation reserved through the PRS. The number of transactions on PRS are higher than those handled by other large railways. For example, SNCF, the French Railway, handles about 130 million transactions per year. The increasing passenger traffic (total traffic including reserved, unreserved, and suburban) on IR is given in Table 3. The chart given in Figure 1 shows the increase only in the reserved segment of passenger traffic.

## Centre for Railway Information Systems (CRIS)

IR realized early on that it was essential to provide a dedicated center for IT developmental activities. It also realized that it was essential for the systems personnel and software developers to be in some way a part of the IR so that the embedded tacit knowledge could be effectively transferred to the Railways’ information systems. To meet these goals, in 1986, the Ministry of Railways established the CRIS at New Delhi. CRIS was set up to be an umbrella unit for all computer activities in IR. Initially it was entrusted only with the task of design, development, and implementation of the Freight Operations Information System (FOIS), along with its associated communications infrastructure. Later on, it was entrusted with the PRS and other projects as well.

Table 3 Growth of total passenger traffic on Indian Railways

<table><tr><td>Year</td><td>Number of passenger (millions)</td></tr><tr><td>1950–1951</td><td>1284</td></tr><tr><td>1960–1961</td><td>1594</td></tr><tr><td>1970–1971</td><td>2431</td></tr><tr><td>1980–1981</td><td>3613</td></tr><tr><td>1990–1991</td><td>3858</td></tr><tr><td>1997–1998</td><td>4348</td></tr><tr><td>1998–1999</td><td>4411</td></tr><tr><td>1999–2000</td><td>4585</td></tr><tr><td>2000–2001</td><td>4833</td></tr><tr><td>2001–2002</td><td>5093</td></tr><tr><td>2002–2003</td><td>4971</td></tr><tr><td>2003–2004</td><td>5112</td></tr><tr><td>2004–2005</td><td>5516</td></tr><tr><td>2005–2006</td><td>5886</td></tr></table>

Source: Year books and press releases of Indian Railways.

![](/api/attachments/Z3RDG76Y/fulltext/images/0e8a725b7d731fc50c5e6979db0f7c51144af14b00c177b533bbf8d97f8b265d.jpg)  
Figure 1 Growth of target passenger segment for reserved accommodation.

CRIS is a project-oriented organization, taking up large IT application development and implementation, while also ensuring close coordination of IT and business goals. Though it has been associated with a number of IT projects at IR since its inception, the project that has gained substantial importance, and over time has become CRIS’s flagship project, is the PRS.

## Passenger Reservation System (PRS)

PRS was started as a pilot project in 1985. It was aimed at providing reserved accommodation on any train from any reservation counter across the country. The systems also prepared train reservation charts, and generated detailed accounting statements of revenue collected. Originally the application ran on the VAX-750 computer. The original software was written in FORTRAN by one of the leading Indian software vendors of that time. In November 1985, the first two trains were put on PRS at New Delhi. The original PRS went through three versions. Thereafter, in 1997, the software was largely rewritten by CRIS to provide the present fully networked system with five servers in five major cities, and its own dedicated network of leased lines crisscrossing the country. It still uses a simple and robust host-based architecture and low-cost VT-100 compatible terminals. The simple layer-2 network protocol helps reduce network latency to a minimum. Maintenance is simple, and the system is stable. The important milestones in the implementation of PRS over the years are shown in Table 4.

Table 4 PRS implementation in Indian Railways

<table><tr><td colspan="2">PRS implementation over the years</td></tr><tr><td>Year</td><td>Events</td></tr><tr><td>Before 1985</td><td>Manual system</td></tr><tr><td>1985</td><td>Pilot project online at Delhi</td></tr><tr><td>1986</td><td>Implementation at Mumbai and Kolkata</td></tr><tr><td>1987</td><td>Implementation at Chennai, CRIS handed over the project</td></tr><tr><td>1989</td><td>Lucknow and Bhopal connected with Delhi</td></tr><tr><td>1990</td><td>Implementation at Secunderabad. Bangalore connected to Chennai, Ahmedabad connected to Mumbai</td></tr><tr><td>1994</td><td>Networking phase I implemented at Secunderabad</td></tr><tr><td>1997</td><td>Current version of PRS software (Concert) put on line</td></tr><tr><td>1999</td><td>All India Network commissioned - implementation of Current version of PRS software completed</td></tr><tr><td>2000</td><td>PRS related enquiries made available on website; first major business logic change with introduction of Tatkal (immediate) tickets with different fare structure</td></tr><tr><td>2003</td><td>Facility for Internet booking of tickets started</td></tr><tr><td>2005</td><td>E-ticketing facility commences. Pilot data warehouse set up for PRS. Reports used for passenger service initiatives</td></tr><tr><td>2006</td><td>Upgrading of tickets commences. Pilot project for use of hand-held devices for train conductors commences. Changes in business logic introduced in a number of areas.</td></tr></table>

Although only 15% of the long-distance (that is, nonsuburban) journeys are undertaken using reserved accommodation, it still adds up to over 1 million transactions per day on the PRS. On average the system collects over Rs. 200 million (more than USD 4 million) in daily revenue (railway fares in India are the cheapest in the world). In this plethora of numbers, the PRS has been performing quite well. Average uptime of the application hovers at about 99.2% and average transaction latency has been contained to less than 3 s. In recent years, ticketing has been provided through the Internet (providing for over 2% of all reserved tickets sold). More recently, the e-ticketing system has been introduced, which allows passengers to board trains without a printed ticket, with a photo-id as their authority to travel.

The PRS has been widely lauded as a very successful e-Governance project. Ministry of IT (of India) officials treat IR and CRIS with respect, and industries within India admire it: in great measure because of its successful PRS. The number of PRS locations has been expanding at a very rapid pace in India. Table 5 shows the growth in their numbers over the years. Though widely and successfully implemented, PRS incorporates complex business logic. A glimpse of the volume and complexity can be gauged from the large number of diverse passenger reservation rules and requirements of IR that have been built into the PRS (Table 6).

Table 5 Growth in numbers of PRS locations commissioned

<table><tr><td>Year</td><td>Number of PRS locations commissioned</td><td>Cumulative numbers</td></tr><tr><td>1985–1986</td><td>1</td><td>1</td></tr><tr><td>1986–1987</td><td>5</td><td>6</td></tr><tr><td>1987–1988</td><td>14</td><td>20</td></tr><tr><td>1988–1989</td><td>5</td><td>25</td></tr><tr><td>1989–1990</td><td>14</td><td>39</td></tr><tr><td>1990–1991</td><td>13</td><td>52</td></tr><tr><td>1991–1992</td><td>14</td><td>66</td></tr><tr><td>1992–1993</td><td>22</td><td>88</td></tr><tr><td>1993–1994</td><td>21</td><td>109</td></tr><tr><td>1994–1995</td><td>132</td><td>241</td></tr><tr><td>1995–1996</td><td>45</td><td>286</td></tr><tr><td>1996–1997</td><td>57</td><td>343</td></tr><tr><td>1997–1998</td><td>55</td><td>398</td></tr><tr><td>1998–1999</td><td>61</td><td>459</td></tr><tr><td>1999–2000</td><td>64</td><td>523</td></tr><tr><td>2000–2001</td><td>93</td><td>616</td></tr><tr><td>2001–2002</td><td>108</td><td>724</td></tr><tr><td>2002–2003</td><td>163</td><td>887</td></tr><tr><td>2003–2004</td><td>186</td><td>1073</td></tr><tr><td>2004–2005</td><td>150</td><td>1223</td></tr><tr><td>2005–2006</td><td>97</td><td>1320</td></tr></table>

Table 6 Volume and complexity of PRS

<table><tr><td>Attribute</td><td>Description</td><td>Numbers</td></tr><tr><td rowspan="4">Volume</td><td>Total number of transactions</td><td>Over 1 million per day</td></tr><tr><td>Number of passengers handled</td><td>Over 0.7 million per day</td></tr><tr><td>Number of reserved trains</td><td>Over 2800</td></tr><tr><td>Number of locations</td><td>1320</td></tr><tr><td rowspan="5">Complexity</td><td>Types of trains</td><td>8</td></tr><tr><td>Types of quotas</td><td>40</td></tr><tr><td>Types of classes</td><td>9</td></tr><tr><td>Types of concessions</td><td>199</td></tr><tr><td>Types of coaches (Railway Carriages)</td><td>123</td></tr></table>

## The seeds of discontent

The seeds of Ramasundar’s current concerns had actually been sown in 2001. The newly set up Passenger Marketing (PM) Directorate of the Ministry of Railways had wanted to start booking reserved tickets through the Internet. CRIS had just set up a very successful website for passenger inquiry (currently, the passenger inquiry website experiences over 6 million hits per day during the peak travel season). CRIS and its parent, the IT Directorate of the Ministry of Railways, were inclined to wait for a while before starting Internet booking. However, the PM Directorate got the newly set up IRCTC (Indian Railway Catering and Tourism Corporation) to create the web-booking portal (presently among the top e-commerce sites of India), through which passenger tickets could be booked and payments made through an e-payment gateway to major banks and credit cards. The IRCTC website is available at http://www.irctc.co.in. CRIS developed the back-end interface from PRS to IRCTC’s booking portal. However, this event served to highlight the emerging need for providing channels of service to customers beyond the usual manned counters. The Internet interface of PRS continues to be managed by IRCTC. The reporting relationships of organizational stakeholders for PRS implementation are given in Figure 2.

Meanwhile, the unreserved segment, thus far being serviced through manual card tickets and stand-alone SPTMs (self-printing ticketing machines), started being addressed by the centralized unreserved ticketing system (UTS). The UTS was also developed by CRIS, but in contrast to PRS it was based on an RDBMS-based backend. The number of locations making use of UTS was increasing rapidly (by March 2006 it had reached over 550 locations, and is likely to increase to about 1500 locations by 2007).

As already mentioned, the upsurge in India’s economic growth had enhanced the service expectations of passengers. Competition from low-cost airlines and long-distance road travel, which was unimagined in the past, became a reality. To retain its customers, IR responded by changing its business rules relating to reserved accommodation for passengers to manage the new situation. The Ministry of Railways expected a rapid response from CRIS to incorporate the new business rules in the PRS software. This dynamic business situation exposed the shortcomings of the PRS software, primarily the time and effort involved in making changes in the program logic. Ramasundar recognized these limitations, and had recently told the Board of Directors of the IR that too many changes in the program logic could seriously destabilize the PRS.

![](/api/attachments/Z3RDG76Y/fulltext/images/67d767ca0639d30768f6a03822dcf74541f770e5e68c4850c85f1915146d6a52.jpg)  
Figure 2 Reporting relationships of organizational stakeholders in IR for PRS.

But it was clear that frequent demands for program logic change were here to stay. In addition, futurists in the Ministry of Railways were making the following points:

\- Round-the-clock reservation services were a must (presently, the PRS needed 4 h a day for data consolidation and backups).

\- In the not too distant future, reservation services would have to be offered through diverse media: the Internet, mobile phones, networks of other operators such as airlines and tour and travel operators.

\- Unreserved and reserved ticketing services needed to be combined.

## Two points of view

## We need a new technology

P.R. Chandran, head of the IT Directorate in the Ministry of Railways was of the opinion that the present technology platforms supporting PRS were obsolete and needed to be changed. His Directorate held the notion that a new technology would overcome all the shortcomings of the current PRS. He also realized that it was an opportune time to lobby for funds for replacing the old PRS. This viewpoint was further endorsed by P.R. Bhatt, the executive assistant to the Board Director (Member Traffic) responsible for customer services and railway operation (please see Figure 2). Not too long ago, Bhatt had commented,

Thanks to our performance in the last one year, the Planning Commission is willing to give the Ministry of Railways additional funds for frontline technology projects from the Government general revenues. Our internal accruals are at record levels. Investment on capital projects is at record levels. If we don’t seize this opportunity to upgrade our PRS now, when are we going to do it?

His views were supported by Punit Kumar, the executive officer to the Minister for Railways a few days later. In an exclusive meeting with Basu, the Board Director (Member Traffic of the Indian Railway Board) and Ramasundar, Kumar had indicated his full support for a change in the PRS technology if required. Commenting on the subject he said,

As you know, the Minister has declared the current year as the ‘Year of the Passenger’. PRS is our main customerfacing application. We should strengthen PRS to ensure that we stay ahead in the passenger business. But the Minister is interested in results: quick results.

## Do we need new technology?

In contrast to the views favoring quick introduction of new technology for PRS, many others involved with the PRS implementation had just the opposite view. To them, disturbing an already functional system was taking an unnecessary risk. In fact, what they wanted was an incremental improvement in the current technology to support the increased functionalities. Amrita Agarwal, in the technical head of the PRS group in CRIS, commenting on the subject, mentioned:

Changing over to a DBMS will prove to be very expensive; the benefits are questionable. And the question of ‘proprietary’ and ‘open’ platforms is quite subjective: we have no time and no desire to tinker with low-level code. We need a stable combination of hardware and software that can effectively manage the extremely heavy transaction loads that we have now. The transaction load will only increase in times to come. And we don’t want to take unnecessary risks on new-fangled cutting-edge technology.

Within CRIS, P.L. Gaur, head of the PRS group, highlighted the importance of considering the pros and cons and the net benefits that could be derived from the proposed switchover. He was of the view that:

\- The present technology platforms needed more appreciation: the combination of low cost and high performance was hard to beat.

\- The platforms needed to be changed, but a steady evolution was the need of the hour, without destabilizing the existing PRS.

\- While passengers would demand more avenues for reservation services, the need could be met without disturbing the core of the system: in fact, world-wide, major high-volume ticketing systems were still being run on file-based platforms, rather than DBMSs.

\- The daily maintenance window, which had been reduced from 6 to 4 h, could be further compressed by using better hardware. In the middle of the night, the system would essentially be idle anyway. For a tiny percentage of vocal Internet users based in the USA, there appeared to be no justification to make wholesale changes in a successful system, especially at a juncture when the passenger traffic was set to increase significantly.

The views aired by Gaur were seconded by Amrita Agarwal, who further commented,

We are not giving a superficial assessment when we say that we do not have the luxury of making a wholesale changeover to another platform at this time. We had taken over the original PRS application from its developers (one of the largest system integrators in the country) in the early 1990s. In the mid-90s we developed the present fully networked version of the PRS application, completely in-house, in the face of widespread skepticism. The success of the current application has surpassed everybody’s wildest dreams. So please listen when we tell you: allow us to follow our plan, and we’ll deliver the goods, I promise you.

## Other concerns

Ramasundar had joined the IR as a manager in the late 1960s. He had been associated with CRIS since its inception. In fact, he had helped to set up the organization in the mid-1980s. Between 1996 and 2004, he had left CRIS and had taken up several other assignments concerned with Railway operations. He came back to head CRIS in the year 2004. Ramasundar knew that both Gaur and Agarwal were sincere in their advice, but he also knew that the original PRS team of the mid-1990s had already moved out of CRIS. None from the present PRS team had been directly involved in developing the system. Ramasundar wished that some continuity from the original team had remained within CRIS. He recollected what P.R. Chandran, head of the IT Directorate in the Ministry of Railways, had recently told him,

We must involve our frontline customer relationship managers in developing the new system. They will bring a fresh outlook to our perspective as far as the scope and functionality are concerned. The CRIS PRS team has developed a certain viewpoint, which may be very narrow. After all, we are looking at the next 10 to 15 years: years of rapid economic and technological change. We can’t afford to have our vision restricted by history.

Another source of perplexity had been the IT vendors. The top IT system integrators and consultants had hounded Ramasundar in a steady stream. They had been giving cautious advice, very conscious of the fact that a large deal was in the offing. Their solutions ranged from incremental improvements (vendor A), to a public–private partnership (PPP) model (vendor B). All were wary of sharing their cost estimates (perhaps because they did not have any at this stage).

The issue of e-security was another area of concern. Chandran from the IT directorate of the Ministry of Railways, had said,

The Chairman of the Board of Directors of the Indian Railways has stressed the need for IT audit and compliance of all IT applications of IR. An IT audit of PRS, being the flagship application, is especially important. This aspect is being keenly watched by the Ministry of Home Affairs as well, and the Prime Minister’s office is directly involved.

While Gaur and Agarwal publicly pooh-poohed any suggestions that the PRS could have security vulnerabilities (since the application was based on uncommon and non-standard platforms and data protocols), Ramasundar could not help feeling concerned about this aspect as well.

## The Conundrum

That Saturday afternoon, J.S. Basu, the Board Director (Member Traffic of the Indian Railway Board) himself called up Ramasundar to ask him to come up with an action plan for dealing with the current situation. Basu made his concerns clear by telling Ramasundar,

I think it is high time we got down to business. In two months we should prepare a roadmap for changing the technology platforms of the PRS, so that we can ask for funding in the coming session of Parliament starting in three months.

Although Ramasundar realized the imperative need to look for a solution to deal with the impending crisis, he was not really sure of the direction and decisions he should make.

He dwelt on the issues that were to be considered before deciding the roadmap for the future. The most vital issue that Ramasundar had to resolve was to choose between the options of

\- incrementally enhancing the capabilities of the existing PRS to serve the emergent dynamic requirements of IR customers

or to

\- go in for a wholesale switchover to a new system.

He sensed that IR’s top management was more amenable to the latter alternative. But he also knew that it was up to him to give the correct technical advice. He also brooded over the considerations he would have to keep in view if he decided to scrap the old PRS in favor of a new system:

\- Core technology: The operating system and data storage platforms (or DBMS) to be used.

\- Scope of the system: A standalone PRS, or a combination of reserved and unreserved ticketing; possible integration with external systems to be considered or not?

\- Overall architecture of the system: Should it be centralized or should it continue to be similar to the present system of five geographically dispersed server clusters? Should there be full access through the Internet?

\- Governance model followed: Possibility of PPP model and the extent of involvement of external vendors.

\- Software architecture of the system: Should it be based on service-oriented architecture? How would it be implemented?

\- The role of consultants and degree of in-house effort in design, development, and implementation of the new system.

\- Security aspects especially in a regimen of Internet access.

\- Risk identification and mitigation.

\- Cost and time schedules: Timelines and effort estimates, cost estimates, and cost-reduction strategies

\- Migration strategy: Should the rollout be incremental? If so, how? Or should it be a big-bang approach?

\- Business continuity/contingency planning.

Several alternatives could emerge. But Ramasundar was still not sure if the benefits of switching over to a new PRS outweighed the risks and costs of doing so. Which direction should he take: retain the old system and look for ways for improving its performance? Or go in for a new system, with all its attendant risk? Ramasundar thought about the next few months: they promised to be hectic. With a sigh, but with renewed energy, he began to prepare for his impending meeting with the Railway Minister regarding the progress of IT projects at IR.

## Notes

1 The authors prepared this case as a basis for class discussion, rather than to illustrate either effective or ineffective handling of an administrative situation. Names of the players have been changed. For clarity, some of the roles have been consolidated, and situations have been dramatized.

## About the authors

Shirish C Srivastava is a doctoral candidate at the School of Business, National University of Singapore. He has done his M.B.A. from Management Development Institute (MDI), Gurgaon, India, where he was awarded the Prime Minister’s Medal. His research has either been published or accepted for publication in several international refereed journals and books such as MIS Quarterly Executive, Journal of Global Information Management, Information Resources Management Journal, Electronic Government: An International Journal, IIMB Management Review, International Journal of Information & Communication Technology Education, Encyclopedia of Information Science and Technology, and Vikapla: The Journal of Decision Makers. He has also presented his research in key international refereed conferences like Academy of Management (AOM), Academy of International Business (AIB), International Conference on Information Systems (ICIS), Institute for Operations Research and the Management Sciences (INFORMS), Americas Conference on Information Systems (AMCIS), and Pacific Asia Conference on Information Systems (PACIS). His research interests include IT enabled Offshore Sourcing, e-Government, and IS & E-Business Strategy.

Sharat S Mathur is an IT Manager in the Indian Railways, presently posted at the CRIS at New Delhi as its General Manager – IT. He has worked extensively in the area of IT in the Indian Railways since 1988. His primary assignments have been in IT-based systems for material procurement, material resource planning, shop floor scheduling, EDI, and logistics. He has been the CIO of Container Corporation of India Ltd., a Government of India Undertaking, during 1997–2000. He has also worked on IT strategy planning and management during his assignment as Director, Computerization and Information Systems in the Ministry of Railways during 2002–2006. His present assignment involves coordination of IT resources for the IT projects executed by CRIS for the Indian Railways. He is presently on the advisory board of the Indian edition of CIO magazine.

Thompson SH Teo is Associate Professor in the Department of Decision Sciences at the NUS Business School, National University of Singapore. His research interests include strategic use of IT, e-commerce, adoption and diffusion of IT, and strategic IT management and planning. He has published more than 80 papers in international refereed journals such as Communications of the ACM, Database, Decision Sciences, Decision Support Systems, Information and Management, International Journal of Electronic Commerce, Journal of Management Information Systems and MIS Quarterly Executive. He has also edited four books on IT and e-commerce, and is on the editorial board of several international refereed journals.
