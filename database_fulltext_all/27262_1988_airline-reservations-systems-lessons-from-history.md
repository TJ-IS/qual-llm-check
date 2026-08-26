---
otero_id: 27262
otero_key: "GFTD9NJE"
title: "Airline Reservations Systems: Lessons From History"
authors: "Duncan G. Copeland; James L McKenney"
year: "1988"
journal: "MIS Quarterly"
doi: "10.2307/249202"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Airline Reservations Systems: Lessons from History
Author(s): Duncan G. Copeland and James L. McKenney
Source: MIS Quarterly, Vol. 12, No. 3 (Sep., 1988), pp. 353-370
Published by: Management Information Systems Research Center, University of Minnesota
Stable URL: http://www.jstor.org/stable/249202

Accessed: 08/05/2014 19:29

Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at http://www.jstor.org/page/info/about/policies/terms.jsp

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

# Airline Reservations Systems: Lessons From History

By: Duncan G. Copeland
Graduate School of Business Administration
Harvard University
Boston, MA 02163

James L. McKenney
Graduate School of Business Administration
Harvard University
Boston, MA 02163

## Abstract

This article discusses the evolution of airline reservations systems—from their inception as manually maintained inventories of seat availability, through their description as “anticompetitive weapons” used “unlawfully” to obtain and exercise monopoly power. The evolutionary perspective reveals interdependent industry, company, and technology forces that shaped the pattern of competition. Although many facets of the airline experience are unique to the air transport industry, the authors identify three features with broad implications for the strategic use of information technology. First, large installed processing capacity can be a source of economies of scale and scope. Second, established technical competence is a necessary requirement for gaining competitive advantage. Finally, sustainable advantage need not be the result of extraordinary vision, but the result of consistent exploitation of opportunities revealed during the evolution of adaptable systems.

Keywords: Reservations systems, competitive advantage, strategic information systems, business history

ACM Categories: C.3, H.4, J.1, K.2

## Introduction

The reservations systems of American Airlines and United Airlines have helped make these carriers major forces in the air travel distribution chain. These systems have become popular examples of the use of information technology for competitive advantage. Less well known is precisely how these carriers came to preempt their competitors.

The dominant positions of American and United can be understood as the outcome of an evolutionary process that parallels developments in information technology and the air transport industry. Since the late 1940s, the goals for reservations systems have changed and expanded. At first, the primary incentive was to reduce clerical costs; it soon became apparent that an accurate count of the number and names of passengers for each flight was fundamental to controlling airline operations. Information captured through the reservations process was used to manage passenger service levels and aircraft capacity and to plan for ancillary requirements such as baggage handling, food, and fuel. Eventually, the marketing potential inherent in the systems came to dominate the airline industry's retail distribution channels. Starting from an electromechanical base, the airline reservations systems evolved along with the computer and air transport industries. Their expanding scale and scope influenced developments in both software and hardware and were affected by the regulation and deregulation of the domestic airline market. In the process, these systems went from being useful to being essential assets, equal in importance to an airline's fleet.

This article documents each stage in the evolution of reservations systems—from their inception as manually maintained inventories of seat availability, through their description as “anticompetitive weapons” used unlawfully to obtain and exercise monopolistic power. The usefulness of the airline example extends beyond the anecdotal citation of reservations systems as evidence of the existence of strategic information systems. This evolutionary perspective reveals patterns of technological competition between actual and potential rivals possessing different capabilities. Notable among these patterns is the importance of scale economies, cumulative technological experience, managerial learning, and opportunism.

## The Evolution of Airline Reservations Systems

## The experimental years

Manual reservations systems were first automated using the electromechanical technologies available after World War II. With the commercial production of second generation digital computers, a few innovative carriers joined with IBM to build the first privately owned, real-time computer networks.

## Humble Beginnings

In the years immediately following World War II, the demand for air travel began to exceed the available supply, and the airlines' ability to process passenger reservations assumed increased importance. Manual systems in use at the time maintained seat inventories for a given flight at its point of departure. Reservations agents were free to book space on a flight after confirming seat availability posted on large display boards in each reservations office. After selling a seat, an agent sent a one-way booking message via telephone or teletype to the reservations office in the flight's originating city. Upon receipt of the booking message, a clerk decreased the count of available seats for the flight from an inventory maintained in a looseleaf folder. When the number of available seats for a flight dropped below a specified level, a "stop sale" message was sent to all reservations offices for posting on the availability boards.

In addition to the availability of seats for a flight, the airlines' reservation function required a second type of information called a passenger-name record (PNR). Upon confirming the sale of a seat, a reservations agent noted passenger-specific information on a PNR card. These data were subsequently transmitted, either by telephone or teletype, to the flight's originating city. As the departure date for a flight neared, the reservations office in the originating city reconciled the seat inventory with the card file of PNRs. Frequent inconsistencies in these data led to flight under/overbookings and to the deterioration of both customer service levels and utilization of aircraft capacity.

During the 1950s, availability boards were replaced by magnetic drum memories, which held seat inventories in the reservations offices. $^{1}$ To determine seat availability, reservations agents inserted “plates” for each flight in their desk sets (i.e., terminals). In the event of a booking or cancellation, the agent adjusted the inventory count on the drum. While “availability systems” improved the accuracy of the seat inventories, they did not capture passenger data, so reconciliation problems due to the inability to link passenger records to seat records remained.

C.R. Smith, president of American Airlines, was acutely aware of American's problems with passenger reservations. Smith knew that the coming of passenger jets would only exacerbate the operating difficulties and increase the reservation cost per passenger. His meeting in 1953 with Blair Smith, an IBM sales executive, led to a five-year joint effort by IBM and American to study the technical feasibility of creating an automated, integrated marriage of a passenger's name to a seat reservation. Upon completion of this project in 1958, American signed a contract with IBM to work out the detailed specifications for the airline industry's first "PNR system" (American, 1967). Within American, responsibility for the system was assigned to the newly formed Reservations Special Projects Group, which reported to the airline's marketing unit.

## The IBM SABER Projects

American envisioned a system that could match passengers to seats; speed communications among airlines; contain seat availability on all carriers' schedules; print passenger itineraries; and issue boarding passes, with terminals located in the offices of travel agents (Paul, 1986; Webb, 1986). Despite the application of advanced data processing techniques learned by IBM during the development of an air defense system for the air force, technical constraints limited the initial design of American's system to passenger-name records, seat availability, and interairline communication via teletype (Paul, 1986). $^{2}$ The full implementation of American's conceptual design had to wait nearly 20 years before its functional complexity was matched by technological capability. But the initial system, code-named SABER (Semi-Automatic Business Environment Research), was scheduled for a phased installation, beginning in 1961.

The heart of SABER was two IBM 7090s, one for real-time processing and the other for backup and lower-priority routine batch jobs. Six magnetic drums with a total capacity of 7.2 million characters contained records for seat inventories, flight schedules, application programs, and a large memory space to store inquiries from and confirmations to 1,100 reservations agent terminals. Sixteen of the first IBM 1301 disk storage units, with a combined capacity of 800 million characters, held passenger reservations and duplicate copies of all information stored on the drums. IBM 7286 Real Time Channels, developed specifically for SABER, scheduled, controlled, and assembled input-output data between the 7090 and the magnetic drums, disk files, and communication lines (Bashe, et al., 1986; Jarema and Sussenguth, 1981; Liebeck, 1986; Plugge and Perry, 1961).

## Technological innovations

PNR functionality meant that most transactions required accessing the drums for seat availability and the disks for passenger information. The resulting volume of input-output operations and the need for fast response time made the simultaneous operation of multiple programs to match seat and PNR records imperative for acceptable processor utilization. Important innovations in the SABER control program were its ability to control both the element of randomness introduced by teleprocessing and the concurrent execution of 30 programs through the use of memory cycle stealing and dynamic allocation of main memory.

The communications system became an integral function of SABER due to the system's geographically dispersed terminals and centralized data files. The network used leased voice-grade lines with initial transmission speeds of 1200 bps, later increased to 2400 bps. At each of the 110 remote terminal locations, a Multiplexor-Communications (Mulcom) switch controlled transmissions between the local terminals and one of the nine high-speed lines connected to the real-time channels. A line control technique devised for SABER coordinated a large number of interactive terminals on multi-drop lines using minimal system overhead, improving response time (Jarema and Sussenguth, 1981; Plugge and Perry, 1961).

A unique feature of SABER was its message-driven nature. Unlike batch-processing systems common to commercial environments, the source of all input was the result of polling the remote multiplexors. This feature had a potential market among other airlines, and by 1960 Delta and Pan Am had signed contracts with IBM for similar PNR systems (Delta, 1961; Pan American, 1961). IBM organized the contracts with American, Delta, and Pan Am under an umbrella project also named SABER, forcing American to seek a new moniker for its own system; hence the coining of "SABRE". $^{3}$

IBM's prior experience was insufficient to shepherd the SABER projects safely through the complex construction of the first commercial teleprocessing systems. Yet the belief that the airline systems augured the future of data processing (Liebeck, 1986), and that it was an opportunity to create a software application with market potential, led IBM to persist in improvising solutions to unanticipated problems. For example, inefficiencies in the original code forced the rapid development of system diagnostic tests to reduce actual response times by an order of magnitude to meet contractual specifications (Bedford, 1986; Paul, 1986). The difficulties did, however, have the merit of inculcating advanced data processing skills in the airline personnel assigned to the projects. As programming and testing proceeded, knowledge of control programs, memory management, and file retrieval techniques accrued to all project participants.

From IBM's perspective, these general problems were compounded by the challenge of developing the three systems in discrete architectural environments. Although functionally similar, the systems differed in their throughput capabilities and processors (Siwiec, 1977). Only American's SABRE used the binary IBM 7090 computers. Delta's DELTAMATIC was based on the IBM 7070, and Pan Am's PANAMAC relied on the IBM 7080, both decimal machines (Webb, 1986). $^{4}$

Because American's project was breaking ground for the others, it experienced a disproportionate number of problems. $^{5}$ Despite delays, aborted conversions, unreliable communication lines, and health emergencies among project team members, the crash development of performance measurement techniques and some hardware modifications permitted American's SABRE to become fully operational by 1964, while installation of DELTAMATIC and PANAMAC was completed in 1965.

## The PARS influence

By 1965, the IBM SABER projects had demonstrated that real-time teleprocessing was a viable solution to the core problems associated with passenger reservations. The early experience spurred two principal developments of the late 1960s. The first development was the desire of IBM to exit the custom PNR system business and earn a return on its investment by marketing a PNR product to all airlines. The advent of the powerful System/360 computers allowed IBM to include innovations from the SABER projects in the OS/360 operating system and to launch a standardized airline reservations product. The second development was the desire of Eastern, TWA, and United to acquire PNR systems to keep pace with their rivals. Eastern expanded the IBM software and set a technological standard for a large-scale reservations system. TWA and United each tried to build comprehensive custom systems that went far beyond PNR functions, and even exceeded the original goals envisioned for SABRE. Unfortunately, TWA and United failed because they lacked experience with both the application and the technology.

## System/360

IBM's 1964 announcement of the System/360 marked a turning point in its product strategy by making software compatible for different hardware configurations. However, System/360 did not affect IBM's policy of bundling the cost of software with the total cost of a computer system. As part of this approach, it was natural for IBM to leverage its experience from the SABER projects into the development of its own Programmed Airline Reservations System (PARS). This system would not only promote sales of System/360 hardware to airlines, but also free the company from the time-consuming, risky business of developing custom reservations systems.

PARS was intended to have maximum market appeal, and was therefore targeted to the functional requirements and transaction volumes of mid-sized airlines. It included the application software for a passenger-name reservation and seat inventory system, and a specialized operating system, the Airline Control Program (ACP). ACP was designed to handle a large volume of inputs that, although unpredictable, required limited computational functions and flexibility. The software objective was to achieve optimal terminal response, system availability, reliability, and recoverability. It could run on System/360 models 40 through 75, although Model 65 was the heart of the most common configuration (Siwiec, 1977). Beginning in 1965, IBM began taking orders for processors with the PARS software for installation in 1968. Initial purchasers included Braniff, Continental, Delta, Northeast, and Western.

## Eastern-Based PARS

By 1965, Eastern had concluded that its operations required the functionality of a PNR system. Bolstered by strong technical expertise recruited from Delta, Eastern chose to expand IBM's PARS product to meet the needs of a large trunk carrier, rather than build a system from scratch (Heinzmann, 1986). After TWA and United became allied with other hardware vendors, Eastern was IBM's only contract with a major carrier. As such, the success of Eastern's effort was important to IBM, and the project received commensurate support (Bedford, 1986). In 1968, Eastern-based PARS, as it became known in the industry, was installed in Eastern's new data center in Miami. The carrier's stated goal of "having the most advanced system for computerized reservations, traffic handling, and operations service" in the industry had become a reality (Eastern, 1968).

The creation of Eastern-based PARS was an important chapter in the history of airline reservations systems for two reasons. First, the system superseded American's preeminence in this facet of airline operations. Second, the system turned out to be a blessing for TWA and United. In 1965, these two carriers had decided to follow American's example and build custom systems in partnership with a hardware vendor. However, whereas American, relying on IBM's experience, chose to install only a subset of the conceivable reservations functions, TWA and United pursued vastly more comprehensive information systems. United selected Univac to design and install a system to run on four Univac 1108s that would support 3,000 CRT terminals and include reservations, management information, flight $^{5}$ Lundstrom (1987) believed that “only IBM’s unwillingness to admit defeat and (its) unlimited financial resources had averted another software development disaster.”

planning, ticket issuance, freight billing, market research, and location control for major spare parts (United, 1965). TWA contracted with Burroughs for a system that would, among other things, automatically encode the names of Israeli passengers on flights passing through Arab countries (Schafers and Williams, 1986). $^{6}$

TWA and United encountered difficulties when neither they nor their respective vendors could devise technological solutions to the demands imposed by their ambitious functional designs. Their difficulties were essentially the same as those experienced by American and IBM five years earlier. In other words, these projects suffered from a lack of relevant experience, which for TWA and United was magnified by the extensive functional requirements (Bedford, 1986; Hopper, 1986) and the fact that Burroughs and Univac had no prior experience with teleprocessing systems (unlike IBM through the SAGE project for the air force). In addition to a lack of experience, the available technology, regardless of vendor, was incapable of satisfying the goals of the two systems. American had sought similarly ambitious functions for SABRE in 1958, but these were pared, through trial and error, to a design that was consistent with the capabilities of hardware and software available at the time of installation. In the absence of experience, TWA and United attempted to install in the late 1960s the sort of systems that did not emerge until the late 1970s.

Both systems were scheduled for completion in 1968, but United, by 1969, and TWA, by 1970, found themselves experiencing classic data processing calamities. Because they had underestimated the complexity of their requirements and overestimated the capability of the available technology, these two major trunk carriers were faced with the prospect of scrambling to accommodate the passenger volumes of the 1970s while using primitive availability systems that had long since been deemed inadequate. This lack of functionality had become a competitive liability (O'Brian, 1986; Lundstrom, 1987). In contrast, their competitors that had PNR systems, most notably American, had begun utilizing reservations data to fine tune their operations and focus their marketing strategies (Bard, 1986). These accurate passenger inventories afforded the opportunity to control under/overbookings to jointly optimize passenger service levels and load factors. $^{7}$ Passenger databases could be used to model alternative decision scenarios. Both capabilities were skills that took time to perfect, and the early innovators' accrued experience was more difficult to imitate than their technology.

Although TWA reached an out-of-court cash settlement with Burroughs (Aviation Week, 1972), $^{8}$ and United came to an understanding with Univac that allowed it to salvage its flight operations and message-switching applications to run on Univac hardware, both carriers were forced to seek alternative solutions for their reservations problems as quickly as possible (O'Brian, 1986). Accordingly, in 1970 each arranged to purchase Eastern's software and contracted with IBM for assistance with accelerated installation projects. By the end of 1971, TWA had successfully implemented the system it continued to call PARS, and United's APOLLO was also up and running (Trans World, 1970; United, 1971).

In 1970, American acquired Eastern-based PARS in exchange for providing Eastern with programming assistance for its fare quote system. Eastern was also given Sabretalk, a high-level programming language developed by American, which Eastern subsequently sold to Delta and United (Murray and Goodlet, 1986). American spent the next two years modifying the user interface to Eastern's software to meet American's needs, and in 1972 implemented the upgraded SABRE in its new data center in Tulsa, Oklahoma (Hopper, 1986).

By 1972, Northwest, with its Univac-based reservations system, was the only one of the ten trunk airlines that had not adopted the PARS standard. $^{9}$

With the completion of the conversions to what was generically referred to as “PARS 2”, the airlines were successfully able to add functions such as fare-quotation, advance check-in, boarding pass issuance, stand-by passenger handling, and itinerary generation. The common architecture permitted increased airline interaction on technical challenges. For example, the Arinc $^{10}$ voice network was modified in accordance with the PARS 2 design for digital transmission to accommodate the increased demand for intertrunk exchange of seat availability and booking data (Rader, 1987; Aviation Week, 1971).

Industry opinions regarding a rank ordering of the "best" systems at the time place United first, TWA second, Eastern third, and American fourth (Blackney, 1986; Hopper, 1986; Murray and Goodlet, 1986). These ratings are based on highly subjective technical and functional criteria, and are arguable in terms of their specific order. What is clear, however, is that the preeminence once enjoyed consecutively by the systems of American and Eastern had eroded by the early 1970s. But it would be misleading to suggest that there was no disparity among the systems. Each reservations system's scale was commensurate with each airline's operating scale, which meant a wide distribution in the size of installed processing bases. However, by the early-1970s, all major carriers possessed stable, reliable internal systems and communications networks, which had become essential components of their operations.

## Retail automation

Retail automation refers to the practice of extending the reach of the reservations systems beyond the airline's organizational boundaries to the industry's distribution system. Placing reservations system terminals in travel agencies and on the premises of large corporations began slowly and experimentally. In addition, several studies were made by travel agents and airlines into the feasibility of creating a cooperative system for shared use by all industry participants. This prospective cooperation ended in 1976 when American and United began marketing their systems in competition with each other. Retail automation developed concurrently with airline deregulation. After 1978, the marketing potential inherent in the reservations systems complemented the market threats and opportunities accompanying the new competitive environment. American and United were so successful in devising ways to use their systems to exploit the deregulated environment that their rivals were forced to seek legislative protection.

## Early Trials

American began experimenting with expanding the reach of SABRE in 1967 when it placed terminals with a limited number of travel agents and commercial accounts. $^{[11]}$ At that time, travel agents sold approximately 30 percent of the industry's tickets. The bulk of retail distribution was through the airlines' ticket offices in major cities and at airport ticket counters. By the early 1970s, the major carriers were selectively distributing systems' terminals to third party locations and arriving at varying conclusions as to the long-term viability of such a strategy (Doty, 1973). The airlines reached a tacit understanding that they should place a moratorium on further retail expansion in order to avoid a “computer war” (Sohn, 1986). Of course, limitations on computer capacity and the avoidance of unnecessary communications costs also entered into that decision (Celentino, 1987). Further, the early 1970s was the nadir of competition in the airline industry. In response to this environment, the Civil Aeronautics Board had ceased granting new route authority and was sanctioning interairline agreements to limit excess capacity.

## Industry System Attempts

Several efforts were initiated between 1967 and 1974 to develop an industry standard passenger reservations system for use by travel agents. Without access to a computerized system, travel agents had to rely on printed paper schedules and telephone or teletype communication to determine seat availability and to make reservations for their customers. The first attempt at a common system, the Donnelly Official Airlines Reservations System (DOARS), began in 1967 but failed for lack of agreement on financing among the participants. In 1969, the Civil Aeronautics Board was asked to approve the PARS-based Automated Travel Agency Reservations System (ATARS), which was intended as an exclusive industry system for use only by airlines and travel agents. The Justice Department characterized the exclusivity feature as a per se violation of antitrust laws, prompting an investigation into the competitive ramifications of an industrywide system. The ATARS agreement was modified to meet the objections, but the project was abandoned before the Civil Aeronautics Board completed its review (American, 1982; U.S. Civil Aeronautics Board, Docket 41207), in part because building a system to support the entire industry, given the available technology, would have been extremely expensive. During this heavily regulated period, there was little perceived advantage from an individual carrier's ownership of a retail reservations system. Supporters of both the DOARS and ATARS attempts hoped to establish ticket distribution as a cooperative effort, with interairline competition based on other grounds. An industry solution was seen as a way to avoid duplication of effort and expense (Hopper, 1986).

In 1972, the president of the American Society of Travel Agents (ASTA) approached Control Data Corporation (CDC) to propose a joint effort to develop a common integrated travel agency system. After studying the idea, CDC concluded that such an endeavor had become not only technologically feasible but financially desirable, and signed a contract with ASTA in 1973 (Bedford, 1986; Sohn, 1986). $^{12}$ This pending cooperation between CDC and ASTA did not escape the attention of Max Hopper, who had assumed responsibility for SABRE upon joining American in 1972. Hopper was uncomfortable, as were managers at other airlines, with the prospect of a computer vendor controlling access to travel agents, who were a small but growing segment of the airlines' distribution chain. According to Hopper, the arrangement would have resulted in carriers being charged for the use of the system, either by the travel agents, CDC, or both (Hopper, 1986). Hopper discussed his concerns with American's newly hired chief financial officer, Robert Crandall, who had overall responsibility for data processing. While at TWA, Crandall had assumed responsibility for that carrier's data processing following its difficulties with the Burroughs' system (Paul, 1986; Labich, 1986). He concurred with Hopper's assessment of the situation, and in late 1974 American proposed a joint task force comprising carriers, hardware suppliers, and ASTA members to consider a Joint Industry Computerized Reservations System (JICRS) (Bedford, 1986; Hopper, 1986; Sohn, 1986). The airlines offered ASTA members an additional 1 percent commission on the value of their ticket sales in return for delaying development of the CDC system and participating in the JICRS study (Sohn, 1986).

Crandall volunteered Hopper's services as JICRS project leader, and for two years the JICRS team studied the matter in terms of the costs and benefits involved and the functional specifications on which such a system should be based. The JICRS Technical Team issued a report in July 1975, concluding that a joint system was technically feasible and economically attractive (American, 1982). United expressed a dissenting opinion, which held that the projected economics of the system was overly optimistic. Further, United objected to the committee nature of JICRS, which had one-member-one-vote authority yet called for development costs to be allocated in proportion to passenger volumes. Hence, the largest carrier, United, would shoulder the majority of the financial burden. In addition, United expected the final result to be the lowest common denominator system developed at the slowest possible speed (Blackney, 1986).

Hopper's involvement with the JICRS study alerted him to United's dissatisfaction and to the possibility that his competitor could withdraw from the project and make its own reservation system, APOLLO, widely available to travel agents and commercial accounts. As the JICRS study proceeded, Crandall authorized Hopper to prepare American to be able to compete should United withdraw from the joint effort (Hopper, 1986).

During the latter half of 1975, United concluded that the JICRS proposal was going to result in United paying dearly for the industry solution, which would serve only to reduce their advantage by making all airlines equal in their reservations processing capacity (U.S. District Court, Document UA001374). From United's point of view, it made both economic and, to a lesser degree, strategic sense to invest in the marketing of APOLLO and offer its distribution chain what United believed was a superior product (Blackney, 1986; Hopper, 1986). In January 1976, United announced both its withdrawal from the JICRS proposal and its intention to make APOLLO available to travel agents and commercial accounts. United notified the industry that it would begin accepting orders for APOLLO beginning in May 1976, for delivery starting that September.

## Learning by Doing

By announcing its marketing plans nine months in advance of delivery, United handed American an opening and essentially forced TWA into making a similar announcement. Having anticipated a faster rollout by United, American was in a position to install the first SABRE terminals under its Travel Agency Automation program in April 1976; by the end of the year it had installed SABRE in approximately 130 travel agent offices (American, 1976). American's sales effort benefited from the goodwill generated during the JICRS project (U.S. District Court, Document AA080706). Travel agents were enticed because SABRE included several features highlighted during the JICRS proposal, with a promise of more to come (Hopper, 1986). American had estimated that two years were needed before it would reach its initial objective of 200 locations. When it became apparent that this goal would be achieved in under 11 months, funding for an additional 200 installations was quickly arranged (U.S. District Court, Document AA080706). Faced with the potential foreclosure of a major distribution channel, TWA opted to protect its interests, but on a limited basis. Acting within budgetary constraints, TWA focused its efforts on selected travel agencies in its principal markets (Haecker, 1982). Additionally, TWA's route structure required that its resources be balanced between its domestic and international operations.

Eastern and Delta adopted an alternative approach. Each maintained its historical stance of focusing on head-to-head route competition, reasoning that as long as the other did not adopt a retail automation strategy, unnecessary expenses could be avoided (Heinzmann, 1986). Meanwhile, Eastern was involved with yet another attempt to develop an industry-wide solution, the Multi-Access Agent Reservations System (MARS). $^{13}$ At Delta, decisions regarding retail automation were affected by a perception that computers were appropriate only for major, discrete tasks. Except for the very largest travel agencies, retail automation did not meet this criterion. Delta expected to continue its regional dominance in the Southeast and saw no need to commit to the retail market for reservations systems (Hawkins, 1987). It was not until 1981, for Eastern, and 1982, for Delta, that the level of effort being expended by American and United led both to conclude that continuing their isolationist policies was no longer in their best interests. As for the smaller trunks or local service carriers, none ever attempted retail automation to a significant degree.

Unlike American, United was not convinced of the need to make modifications to its system during the early days of retail automation. The first APOLLO terminals were installed in September 1976 in four pilot locations to determine what functional enhancements might be required (Blackney, 1986). Evidence suggests that United did not initially place much importance on the reservations systems as a marketing tool. For example, APOLLO marketing was assigned to United's field sales force as an additional responsibility, resulting in a relatively low-level promotional effort. Further, United furloughed 30 PARS programmers in October 1976 (one month after the initial delivery of APOLLO terminals) as part of a 3 percent across-the-board head count reduction mandated in response to a recessionary economy and low profitability. The cuts, which were based on seniority, resulted in the loss of some of the airline's most relevant expertise in data processing. $^{14}$ Many of those let go were immediately hired by American (Blackney, 1986; Lee and Schwartz, 1986).

At American, Robert Crandall established Travel Agency Automation as a separate organizational unit and championed its funding (Hopper, 1986; Sohn, 1986). SABRE's marketing plan was initiated from the top down, with a strategy of targeting large or geographically well-situated travel agents and commercial accounts, in turn producing a local ripple effect on demand for the system. American felt that its reputation would be sufficient to make it the carrier of choice for many travel agents, provided its schedules were made available to them. United's APOLLO was seen as a threat to American's continued access to the travel agent segment of the industry's distribution chain representing more than 50 percent of all tickets sold in 1976 (Hopper, 1986).

American's original motivation for marketing SABRE was to secure a place for the system in the airline industry's distribution system. To American, automating the initial locations seemed justified on the basis of revenue retention; however, it quickly became apparent that retail automation would lead to substantial revenue generation. The first 200 installations were originally estimated to contribute \$3.1 million annually in incremental passenger revenues; return on investment was projected to be 6 percent without incremental revenues, rising to 67 percent if they were included in the calculation. Before the introductory installation effort was complete, the estimate for incremental passenger revenues was revised to \$20.1 million, resulting in a return on investment exceeding 500 percent (U.S. District Court, Document AA080707).

After the first 200 SABRE locations were installed, American's justification for appropriating funds to install 200 more can be found in the following paragraph, which captures the essence of the "learning by doing" that American was experiencing in early 1977:

What began as a necessary competitive counter to a precipitous action on the part of a major competitor has now evolved into a project of significant financial magnitude to American Airlines. Further, it is occurring at a time when we are threatened with major regulatory changes which potentially could lead to a situation in which the marketing information provided and even a limited control over the distribution mechanism could prove invaluable (U.S. District Court, Document AA080717).

Despite the growing importance of information technology as a competitive variable, the longstanding practice of sharing technical information had yet to end. The major carriers faced a common technical problem not directly related to their pursuit of market share of travel agencies. Their systems' capacities were being strained by transaction volumes that even a new generation of IBM computer, the 303X series, would be insufficient to handle. Beginning in 1978 American, Eastern, TWA, and United joined technical forces to develop software that permitted multiple processors to be simultaneously controlled by a single application program. Implementation of the solution created a processing base that was significantly larger than the standard PARS systems and required a commitment to a long-term, large-scale programming support effort. $^{15}$

## Co-host Programs

Despite its coordinated marketing approach, American felt by 1978 that it was falling behind United in travel agent market share due to the greater breadth of United's route structure (Hopper, 1986). American's response was to introduce the co-host concept whereby other carriers were given preferential treatment in the display of their schedules on SABRE for a fee. By the end of 1978 five carriers had signed co-host agreements with American (American, 1978). Although the fee helped defray the costs of expanding the Travel Agency Automation program, the primary intention was to increase SABRE's presence in markets that American did not serve, since the importance of travel agent market share was becoming increasingly evident (American, 1978; Hopper, 1986). The co-host program was a way of extending SABRE's reach to markets served by United, thereby locking in travel agents and slowing the expansion of APOLLO. United immediately introduced its own co-host option.

For an airline without its own retail automation program, co-hosting offered several advantages. For example, in 1979 Western was alarmed to learn that while its flights dominated the Salt Lake City market, the travel agents there all used APOLLO. This meant that the “halo effect” of an APOLLO installation gradually increased United’s market share at the expense of Western. $^{16}$ Further, United had access to Western’s traffic statistics in markets where the majority of the reservations were booked through APOLLO. As an affordable alternative to offering its own system in competition with that of United, Western signed a co-host agreement with American and actively promoted SABRE to travel agents throughout the western U.S. market in an attempt to stem the advance of APOLLO. Similarly, Delta struck a deal with United in 1982 to promote APOLLO in the Southeast to protect Delta’s markets from SABRE’s inroads (Rader, 1987). $^{17}$ For both Western and Delta, the promotion of a reservations system owned by a carrier whose schedules were relatively uncompetitive with their own (American in the West; United in the Southeast) was the lesser of two evils.

## Deregulation

The airline Deregulation Act of 1978 and the two years of regulatory reform that preceded it introduced airlines to a much larger array of competitive threats and opportunities. No longer could the airline bosses “graze sleepily on a peaceful playing field” (Labich, 1987). The approval of the Civil Aeronautics board was no longer required for entry and exit to city-pair markets, which could now be made with 90 days’ notice. $^{18}$ The airlines’ objective became adding routes in high traffic markets and dropping routes with low traffic. Without regulatory price controls, the carriers significantly increased the variety of fares and the frequency with which they changed them. The number of different fares for city pairs in the large reservations systems rose from tens of thousands in a regulated environment to millions. The rate of fare changes shifted from semiannually to monthly, semimonthly, and in some cases daily. As the nature of passenger inquiries changed from simple seat availability to price shopping, real-time access to the carriers’ volatile schedules and fares became a necessity for travel agents.

At the same time, some carriers were questioning the cost effectiveness of their city ticket offices and were looking for ways to control the expense of reservations offices, reservations agents, and internal communications (Celentino, 1987). These factors combined to create a strong incentive for the airlines to transfer the burden from their own reservations offices to travel agencies. As a result, the percentage of tickets sold through travel agents continued to grow. $^{19}$

By the late 1970s, the other carriers began to recognize the potential market power of reservations systems. The 1978 annual report for Continental Airlines conceded that its position as a preferred carrier was threatened when either APOLLO or SABRE was installed in a travel agency in one of its markets. With 55 percent of its seats being sold through travel agents, Continental felt that signing a co-host agreement with American was necessary to ensure the availability of its schedules (Continental, 1978).

Beginning in 1978, American and United intensified efforts to add features to their systems that helped travel agents to manage their businesses and to improve their productivity. $^{20}$ The expense of creating reservations systems that were responsive to the competitive environment effectively drove all but the largest carriers from the retail automation arena. The processing complexity added by the co-host programs, the increase in the size of the fares database, and the added features and transaction volumes associated with usage by travel agents required a multiprocessor installation and a supporting communications network with all its attendant remote hardware.

The joint effort by the largest carriers to create multiprocessor systems had provided them with installations large enough to handle work loads that were beyond the capabilities of uniprocessor systems. Up to this point, a carrier's willingness to invest had been more significant than its capacity to invest, but as the stakes climbed and the largest systems approached nationwide coverage, scale economies began to affect a carrier's ability to participate in the substantial available returns. For example, in 1980 American estimated that its SABRE locations collectively generated \$78.5 million in incremental passenger revenues (U.S. District Court, Document AA072616), and in 1981 SABRE's nine domestic co-hosts contributed \$6.9 million in fees to American (U.S. District Court, Document AA072613). However, obtaining such rents required financial support, and American's 1982-83 budget for retail automation called for spending at an annual rate of nearly \$20 million. American justified the expenditure based on a projected return on investment that remained in excess of 500 percent (U.S. District Court, Document AA072608), recognizing that American had "been able to increase its influence over the flow of passengers through the air transportation network in a manner most beneficial to American" (U.S. District Court, Document AA072613).

## Revived Regulatory Scrutiny

In 1982, allegations appeared that retail automation activity since 1976 perhaps had not been in the public interest. The Justice Department began a preliminary civil investigation in May 1982 to determine whether the owners of reservations systems made it difficult or time-consuming for travel agents to access the schedules of competing airlines. The Justice Department's opening position held that there was sufficient evidence to "point" to anticompetitive practices (Aviation Week, 1982).

In 1983, the Civil Aeronautics Board conducted a study of the reservations systems to determine the effects on competition and any “antitrust implications that may exist” (Aviation Week, 1983). The issues investigated included lease costs and conditions, co-host charges, and “display bias” for carriers’ schedules. Display bias determines where a particular carrier’s flights appear in relation to the first line of the first screen displayed to a travel agent. Preference went to the host airline, followed by co-hosts, followed by carriers not considered acute competitive threats to the host. Since studies indicated that approximately 70 percent of all bookings made through the systems were sold from the first screen displayed, the extent to which a system’s schedules were subject to bias was salient. By June 1983, the Civil Aeronautics Board felt it had sufficient evidence to show that the opportunity for abuse of the systems existed, and its tentative report recommended guidelines for system access (Ott, 1983a). As one Board member put it, the process of deregulation “apparently has hit a very serious stumbling block” with the reservations systems (Ott, 1983b).

In July 1984, the Board promulgated a set of rules designed to eliminate display bias and prohibit unjustly discriminatory fees charged to rival carriers (Aviation Week, 1984). The response by American and United to the Board's ruling indicates how disadvantaged the competitive positions of the "have-not" airlines had become. Prior to the elimination of display bias, American's schedules received decidedly unfavorable treatment in APOLLO, and United's flights were accorded a similar status on SABRE. With bias restricted, the sheer number of flights American and United offered guaranteed that these two carriers would dominate any system containing all domestic flights, to the inevitable detriment of their smaller rivals. Also, prohibiting discriminatory fees without stipulating a specific remedy invited an "equitable" fee structure based on a higher assessment for the service. Prior to the ruling, American and United had been able to discriminate in price: Fees ranged from zero to \$3.60 per segment booked (Ott, 1983b), with many carriers charged nothing, their schedules having been included in the interest of completeness (Hopper, 1986). Subsequent to the 1984 ruling, the booking fees American and United charged climbed to \$1.75 and \$1.85 respectively (U.S. Civil Aeronautics Board, Docket 43605). Republic Airlines labeled the ruling a “license to steal” (U.S. Civil Aeronautics Board, Docket 41686, 1984).

Setting uniform booking fees significantly increased the revenues American and United received from their systems. $^{21}$ Operating profits from SABRE in 1985 were reportedly \$143 million on revenues of \$336 million (Labich, 1986). Paradoxically, the Civil Aeronautic Board's guidelines against display bias dealt the final blow to smaller carriers still harboring hopes of mounting retail automation strategies. It was financially impractical, if not impossible, for all but the largest trunks to modify their internal reservations systems to eliminate bias and comply with the Board's guidelines (Rader, 1987). Further, generating incremental passenger revenues sufficient to offset the cost of reprogramming would be unlikely without a biased display that favored the host airline.

In November 1984, 11 domestic airlines concluded that the reservations systems of American and United were not merely a competitive advantage, but a “powerful, anticompetitive weapon” (U.S. District Court, Docket 43065, Exhibit NW-R-730). They filed suit, charging that American and United possessed a monopoly in the electronic booking of airline seats. The suit sought \$250 million from American and \$150 million from United based on the rationale that “no carrier can afford to give up the chance to sell tickets to the customers of the agents booking a large portion of the revenues in a region it serves” (U.S. District Court, Docket 43065, Exhibit NW-R-731), and that it would not be feasible to duplicate the facilities provided by American and United (Preble, 1984). The suit alleged that American and United intended to require travel agents using their systems to become franchised dealers, selling tickets on other carriers only to the extent that the hosts permitted (U.S. District Court, CV No. 84-8918 ER). Several other carriers subsequently brought suit against the two dominant hosts. In January 1986, the outstanding complaints were consolidated into one air passenger computer reservation systems antitrust litigation. $^{22}$ Essentially, the suit was grounded on a recognized tenet of antitrust law, the “essential facility” doctrine: When a vertically integrated monopolist controls a non-duplicable resource at one level that is essential to competition at a second level, it must offer the resources to all on the same terms (Saunders, 1985).

Robert Crandall, American's president and chief operating officer, responded to the charges by stating that:

American spent millions of its own dollars and took enormous business risks to create SABRE. In exchange for the superlative selling which SABRE represents we expect a fair profit. We will make no excuses for our charges and we are determined to oppose and to defeat those who seek to use the antitrust laws to deprive us of our rightful reward for the capital, skill and risk we have invested (Preble, 1984).

To a Congressional subcommittee, American and United argued that their systems' profitability was consistent with those earned from other investments entailing similar risks. The plaintiffs countered with a report asserting that American and United had understated their profitability figures by omitting incremental revenues and by overstating costs (Duffy, 1985). $^{23}$ At the request of the Congressional subcommittee, the General Accounting Office attempted to reconcile the conflicting profitability estimates. In its May 1986 report, the GAO decided that the available data were insufficient for it to make its own determination of reservations system profitability, and that it was unclear whether booking fees were substantially above cost or harmful to competition (U.S. General Accounting Office, 1986).

The largest carriers did not sit idly awaiting the outcome of the antitrust proceedings, because the market structure began to change quickly as a wave of consolidation overtook the industry. $^{24}$ The merger of large airlines often resulted in a single carrier dominating a hub airport (Ott, 1986). $^{25}$ Since the economies associated with regional dominance are complemented by a strong retail presence for an airline's reservations system (Bailey and Williams, 1987; Levine, 1987), Delta,

Texas Air, $^{26}$ and TWA $^{27}$ sought market shares for their systems to match their merger-based status as “megacarriers.” With approximately 95 percent of the 29,000 travel agents in the United States automated by late 1987 (Economist, November 7, 1987), gains in retail share were achievable only at the expense of incumbent systems.

But the owners of incumbent systems were not inclined to relinquish their dominance without a fight. In October 1987, American sued Texas Air, alleging that illegal inducements were being used to convert travel agencies to System One. This suit was filed after Texas Air provided legal assistance to travel agents who had been sued by American and United for breaching their contracts by subscribing to System One (Brown, 1987). In November 1987, Texas Air sued American, alleging anticompetitive tactics designed to protect its 38 percent share of travel agents by excluding competing reservations systems from the retail market (Shifrin, 1987; Thomas, 1987). Finally, in February 1988, Texas Air leveled similar charges related to United's 30 percent market share for APOLLO (Phillips, 1987). All litigation was pending at the time of this writing. Figures 1 and 2 illustrate the growth in the number of automated locations for each system since 1976 and the number of remote terminals since 1984.

## Discussion and Analysis

Much of the history of reservations systems was clearly influenced by factors specific to the airline industry. But within this context, individual carriers' behavior contributed significantly to their respective fortunes. Much of this behavior has relevance for other industries where an information system is fundamental to operations through its span of multiple activities in the value chains of member firms. Further, the story has general implications for the strategic use of information technology.

## Industry factors

Economic regulation influenced all facets of the airline industry's development. The Civil Aeronautics Board protected the trunk airlines from serious competition and the effects of business cycles, and its policy toward individual carriers was designed to reduce disparities among these airlines (Caves, 1962). The regulatory pattern reduced the prerogatives of airline management to the point where passenger service was the only competitive variable available for manipulation (Meyer and Oster, 1981). Fruhan (1972) concludes that “in matters of profitability the CAB represents each carrier’s 'first string' management team; the second string group (the ones with shareholder responsibility) get to play only when the outcome of this game is essentially decided.”

![](/api/attachments/GFTD9NJE/fulltext/images/11fa7c9e5c637b75d06bd6a98ab0b5ee239fd642fda55a671fa12e26194f7403.jpg)  
Figure 1. Automated Locations

![](/api/attachments/GFTD9NJE/fulltext/images/0d369e1f6208eb40cd809de820b8922f9168097edbb840e0a9d286ec38b3e819.jpg)  
Figure 2. Remote Terminals  
Note: Data prior to 1978 are from various industry sources.  
Data from 1979 through 1987 are from Travel Weekly.  
Data for Eastern include data for Continental/System One.

Given this situation, much of the original impetus for the reservations systems can be understood in terms of their contribution to differentiated service. To the extent that a passenger inquiry or reservation could be processed more quickly or effectively, an airline realized a product advantage. Accurate passenger inventories allowed the airlines to manage their under/overbookings to jointly optimize passenger service and capacity utilization levels. In addition, by enabling a carrier to reduce the labor content in its reservations process while increasing the productivity of the remaining reservations personnel, an automated system offered a rare source of cost leverage. Yet regulatory protection fostered a spirit of cooperation among the trunks. Once it became apparent that PNR systems were an operational imperative, the trunks shared their technical knowledge and resources. In an era when public policy was designed to reduce disparities among carriers, technological cooperation reduced the costs and risks of adopting the new technology, without the specter of forfeited competitive advantage.

In terms of historical influences, the changes wrought by deregulation were an aberration unlikely to be experienced in many other settings. The heightened competition unleashed by deregulation made the airline industry very information-intensive, and the conduit for much of that information was the reservations systems. Dynamic fares and schedules increased both ticketing complexity and the importance of travel agents as a distribution channel. Travel agents, provided they had access to a comprehensive reservations system, were transformed from vendors of tickets to vendors of information (Levine, 1987). Carriers with retail automation strategies already in place reaped some decidedly windfall benefits in terms of incremental revenues and downstream intelligence.

## Carrier-specific factors

An important lesson from the history of reservations systems is that the airlines' individual characteristics and actions made a difference in their ability to profit from the structural circumstances of the industry. The dominance of the reservations systems of American and United is neither an accident nor the result of extraordinary vision. Rather, the competitive advantage these carriers have enjoyed is the result of a confluence of scale economies, cumulative technological experience, management outlooks, and learning by doing. These factors will be taken up in turn.

## Scale Economies

Scale economies influenced the reservations systems' development from the start. Since the early PNR systems were built in response to pressures from increased passenger volumes, passenger processing was a critical aspect of operations worthy of an expensive computerized solution only for airlines having reached the operational scale of a medium-sized trunk. In other words, only relatively large carriers could use the systems profitably. The functional additions to the systems after the conversion to the PARS standard in the early 1970s were scale-enhancing. By 1976, when retail automation began, only the largest airlines possessed the installed processing base required to accommodate the additional message volumes. As more travel agents were automated, the minimum-efficient scale increased and the number of airlines that could viably compete became progressively smaller.

## Technological Experience

The role played by cumulative technological experience is intertwined with the evolution of data processing technology. The first reservations systems were made possible by IBM's experience with a real-time, message-driven system for air defense and the availability of second generation processors. Nevertheless, the intricacy of a commercial teleprocessing system became evident during its implementation. Without hands-on experience, it was not possible to appreciate the complexity of the problem or the limits of the technology. This experience is the key feature that distinguished Eastern's successful installation of a PNR system from the calamitous early experiences of TWA and United.

By 1976, the largest airlines had stable internal systems and communication networks that successfully handled the geographic spread of their route structures. Based on these successes, retail automation became an incremental technical innovation for American and United, to a lesser extent for TWA, and eventually for Delta and Eastern. As increasing numbers of travel agents subscribed to the systems, the associated demand for processing capacity was met by extensions to the IBM System/370 architecture. The accrued scale and scope of the multiprocessor systems that today belong to American and United, as well as TWA, Delta and Eastern/Texas Air, make them different in kind, not just in degree, from the uniprocessor systems common to the rest of the airline industry.

## Management Outlooks

Scale and experience were necessary but not sufficient conditions for an airline to lead the evolution of reservations systems. Management outlooks and attitudes played a deciding role. American, TWA, and United were traditional competitors because of their transcontinental route structures and comparably large fleets. This rivalry overshadowed the cooperative industry-wide reservations system plan proposed in 1974. When United announced its intention of offering APOLLO to travel agents at the start of 1976, American responded aggressively to what it perceived to be the threatened foreclosure of its access to an increasingly important distribution channel. TWA also was compelled to join in. Once started, the fight for retail market share quickly intensified. Both American and United benefited from formal structural links between their information systems and marketing functions, which had long been the arrangement at American and was initiated at United in 1977 (Blackney, 1986).

## Learning by Doing

The extent of incremental passenger revenues was only evident with experience, but such revenues quickly became the rationale for continued investment in retail automation. The focused rivalry between American and United complemented their growing knowledge of how best to use their systems' retail reach. The systems' influence pervaded multiple facets of deregulated competition through their importance to the airline industry's information flow. As such, the systems have proven to be robust sources of market power as their owners learned to exploit emergent opportunities. Travel agent incentive schemes, display bias, co-host programs, frequent flyer programs, uniform booking fees, and the management of elaborate fare structures are examples of the innovations perfected as the systems' market shares grew and deregulation unfolded. American and United were virtually unchallenged for five years in their quest for retail market share. Because learning by doing characterized these years, non-participating airlines were unable to perceive the profit potential of travel agent automation, and, because they were unaccustomed to the rigors of price competition, they did not understand the threat posed by preemption.

## Implications

Viewing the airlines' experience in a broader sense, we find three patterns with implications for the strategic use of information technology. The first is the role played by economies of scale. The second is the required congruence between task and technology. Finally, the importance of intelligent persistence—a combination of learning by doing and opportunism—cannot be overstated.

## Role of Scale Economies

Engineers and economists have long understood the significance of process scale, and if the airline experience portends the future for some applications of information technology, then the issue of scale economies will increase in importance for MIS managers. The processing scale of the reservations systems in early 1987 ranged from Western's single IBM 4381 handling around 50 internal messages per second (Rader, 1987), to United's eight IBM 3090s for more than 1,000 internal and external messages per second (Lee and Schwartz, 1986). Now that the importance of travel agent market share is evident to aspiring megacarriers, adding processing capacity specifically for the purpose of retail automation is easily justifiable. But in the critical growth stages of retail automation, American and United, with their large internal systems, enjoyed scale-based advantages over their smaller rivals. In sum, the scale economies of the installed processing bases of American and United enabled them to expand the scope of their systems by integrating forward into their industry's distribution chain. The relative lack of such economies, combined with a false sense of security that was a legacy of the regulated past, led other carriers to decide against making the investment required to keep pace. The lesson from airline history is that information technology can be a source of economies of scale and scope. As such, if properly utilized, large installed processing capacity can provide sustainable competitive advantage over less well-endowed rivals.

## Task/Technology Congruence

Congruence between task and technology is essential for successful implementation. This may seem trite, yet the evolution of the reservations systems underscores its significance. For all the attention it received at the time, the original SABRE was just an inventory control system. The nature of the air transport business, requiring 24-hour access by distributed locations, made SABRE strain the bounds of the available technology in the early 1960s. In the late 1960s, TWA and United sought to leapfrog the functionality of SABRE by attempting to install comprehensive real-time management information systems on three- and four-processor configurations. However, these carriers (and their hardware vendors) were guilty of technological chauvinism. They underestimated the complexity of the task and overestimated the capability of the technology to supply a workable solution. If failures like these occurred in an unregulated industry, where firms could not be rescued through their purchase of a competitor's software, the consequences would be devastating.

Eastern appreciated the importance of congruence between task and technology. Its expansion of the IBM's PARS software was functionally conservative but resulted in a reliable, enduring technological standard. With the virtual storage and multiprocessing facilities of System/370, technological capability in some ways exceeded the task requirements of most early internal reservations systems. This was the start of a technically mature, internally stable base that made retail automation an evolutionary, rather than a revolutionary, technical innovation.

The lesson gained from the airlines is that technical competence is a necessary requirement for gaining competitive advantage from information technology. Many prescriptions for identifying and developing strategic information systems focus exclusively on market opportunities, and thus imply that management vision is a sufficient condition. What may appear to be “demand-pull” innovations in a market sense, are more likely to be successful if they are actually “technology-push” innovations for the organizations involved.

## Importance of Intelligent Persistence

The success that American and United achieved in controlling retail distribution highlights the importance of intelligent persistence—the combination of learning by doing and opportunism. The lesson from the airlines is that creating sustainable advantage with information technology need not be the result of extraordinary vision. In this instance success was the result of consistent exploitation of opportunities revealed during the evolution of adaptable systems. American's approach is a case in point. Starting with a stable internal system and initial increments of 200 travel agent locations, American first discovered SABRE's potential to generate incremental passenger revenues and then learned to extract fees from competitors for having their schedules listed in the systems. With experience and steady annual budgetary increases of 5% to 10% (Hopper, 1986; Rader, 1987), American created passenger loyalty due to the first frequent flyer program. American also came to perfect its management of a complex fare structure and benefited considerably from using SABRE's downstream intelligence. As for United, its success indicates that being first is not essential, provided a firm can respond fast enough to keep pace with an aggressive innovator.

Intelligent persistence leads to invaluable experience not easily imitated by rivals. Firms that begin to ride an experience curve ahead of their competitors realize a head start that will endure as long as new opportunities continue to be revealed. Technology can always be purchased, but the same can rarely be said for knowledge.

## Acknowledgement

The authors are indebted to Michael R. Vitale for the contributions he made to the preparation of this paper and the research that underlies it.

## References

American Airlines, Inc. Annual Report, 1976.

American Airlines, Inc. Annual Report, 1978.

American Airlines, Inc. Annual Report, 1982.

American Airlines SABRE (A). Harvard Business School, Case No. EA-C 758, 1967.

Astrahan, M.M. and Jacobs, J.J. “History of the Design of the SAGE Computer—the AN/FSQ-7,” Annals of the History of Computing (5), 1983, pp. 340-349.

Aviation Week & Space Technology. "TWA Suit," October 26, 1970, p. 25.

Aviation Week & Space Technology. "Data Link Network Expansion Planned," January 11, 1971, p. 45.

Aviation Week & Space Technology. "Trans World Airlines, Burroughs Resolve Data Processing Lawsuits," October 23, 1972, p. 28.

Aviation Week & Space Technology. "Justice Eyeing Reservations on Antitrust," May 31, 1982, p. 27.

Aviation Week & Space Technology. "Conferees Direct Computer Reservations Study," January 1, 1983, p. 26.

Aviation Week & Space Technology. "CAB Adopts Final Regulations for Computer Reservations," August 6, 1984, p. 32.

Bailey, E.E. and Williams, J.R. “Sources of Economic Rent in the Deregulated Airline Industry,” Working Paper 28-86-87, Graduate School of Industrial Administration, Carnegie-Mellon University, 1987.

Bard, W., SystemOne Corporation, Houston. Interview with authors, July 7, 1986.

Bashe, C.J., Johnson, L. R., Palmer, J.H. and Pugh, E.W. IBM's Early Computers, MIT Press, Cambridge, MA, 1986.

Bedford, H., formerly of IBM, Norwalk, CT. Interview with authors, July 23, 1986.

Blackney, P., United Airlines, Chicago. Interview with authors, August 25, 1986.

Brown, F.C., III. "American Air Sues Texas Air Over Contracts," Wall Street Journal, October 16, 1987, p. 16.

Caves, R.E. Air Transport and Its Regulators, Harvard University Press, Cambridge, MA, 1962.

Celentino, T., Piedmont Airlines. Correspondence with authors, June 9, 1987.

Continental Airlines. Annual Report, 1978.

Delta Air Lines. Annual Report, 1961.

Doty, L. "Scorecard Shows Some Big Gains, Some Losses," Aviation Week & Space Technology, October 22, 1973, p. 41.

Duffy, W.J. "Analysis of American's and United's Statements Regarding the Profitability of SABRE and APOLLO," Simat, Helliesen & Eichner, Inc., May 1985.

Eastern Airlines, Inc. Annual Report, 1968.

Economist. "Sabre Rattling," November 7, 1987, pp. 72-73.

Fruhan, W.E., Jr. The Fight for Competitive Advantage: A Study of the United States Domestic Trunk Air Carriers, Division of Research, Harvard Business School, Boston, 1972.

Haecker, F. “Service to Travel/Cargo Agents,” presented before the IATA Data Processing Subcommittee, April 1982.

Hawkins, W., Delta Air Lines, Atlanta. Interview with authors, June 4, 1987.

Heinzmann, F., Eastern Airlines, Miami. Interview with authors, July 25 and December 12, 1986.

Hopper, M., American Airlines, Dallas. Interview with authors, August 7, 1986.

Jarema, D.R. and Sussenguth, E.H. "IBM Data Communications: A Quarter Century of Evolution and Progress," IBM Journal of Research and Development (25), 1981, pp. 391-405.

Kilman, S. "Growing Giants," Wall Street Journal, July 20, 1987, p. 1.

Labich, K. "Bob Crandall Soars by Flying Solo," Fortune, September 29, 1986, pp. 118-124.

Labich, K. "Winners in the Air Wars," Fortune, May 11, 1987, pp. 68-79.

Lee, R. and Schwartz, T. United Airlines, Denver. Interview with authors, August 14, 1986.

Levine, M.E. “Airline Competition in Deregulated Markets: Theory, Firm Strategy, and Public Policy,” Yale Journal of Regulation (4), 1987, pp. 393-494.

Liebeck, W., formerly of IBM, Alamo, CA. Interview with authors, July 18, 1986.

Lundstrom, D.E. A Few Good Men From Univac, MIT Press, Cambridge, MA, 1987.

Meyer, J.R., and Oster, C.V. (eds.). Airline Deregulation: The Early Experience, Auburn House, Boston, 1981.

Murray, R. and Goodlet, J., SystemOne Corporation, Houston. Interview with authors, July 6, 1986.

Northwest Airlines, Inc. Annual Report, 1959.

Northwest Airlines, Inc. Annual Report, 1961.

Northwest Airlines, Inc. Annual Report, 1964.

Northwest Airlines, Inc. Annual Report, 1970.

O'Brian, W., formerly of IBM, Monroe, CT. Interview with authors, July 15, 1986.

Ott, J. "CAB Weighs Six Options on Computer Reservations," Aviation Week & Space Technology, June 20, 1983a, p. 44.

Ott, J. "CAB Studies Reservations Bias in Connecting Flights," Aviation Week & Space Technology, September 26, 1983b, pp. 50-54.

Ott, J. "Mergers Allow Domination of Individual Airports," Aviation Week & Space Technology, September 29, 1986, pp. 27-28.

Pan American World Airways, Inc. Annual Report, 1955.

Pan American World Airways, Inc. Annual Report, 1961.

Paul, J., The Flagship Group (formerly of IBM), Dallas. Interview with authors, August 11, 1986.

Phillips, C. "Texas Air Corp. Reservations Unit Sues United Air," Wall Street Journal, February 24, 1988, p. 27.

Plugge, W.R. and Perry, M.N. "American Airlines 'SABRE' Electronic Reservations System," AFIPS Conference Proceedings, Western Joint Computer Conference, 1961, pp. 593-601.

Preble, C. "Ruling Raises Airline Computer System Fees," Aviation Week & Space Technology, December 10, 1984.

Rader, C., Delta Air Lines (formerly of Western Airlines), Atlanta. Interview with authors, June 4, 1987.

Saunders, D. “The Antitrust Implication of Computer Reservations Systems (CRS’s),” Journal of Air Law and Commerce (51), 1985, pp. 157-196.

Schafers, J. and Williams, H., Eastern Airlines, Miami. Interview with authors, December 12, 1986.

Shifrin, C.A. "Texas Air Unit Charges American with Restraining CRS Business," Aviation Week & Space Technology, December 7, 1987, p. 51.

Siwiec, J.E. "A High-Performance DB/DC System," IBM System Journal (16), 1977, pp. 169-195.

Sohn, D., Heritage Travel, Cambridge, MA. Interview with authors, October 1, 1986.

Thomas, P. "Texas Air Corps. Reservations Unit Sues American," The Wall Street Journal, November 24, 1987, p. 44.

Trans World Airlines, Inc. Annual Report, 1970.

United Airlines, Inc. Annual Report, 1965.

United Airlines, Inc. Annual Report, 1971.

U.S. Civil Aeronautics Board. Report to Congress on Airline Computer Reservations Systems, Docket 41207, 1983.

U.S. Civil Aeronautics Board. Advance Notice of Proposed Rulemaking on Computer Reservations Systems (Proposed Part 255), Docket 41686, Comment of Republic Airlines, Inc., April 26, 1984.

U.S. Civil Aeronautics Board. Advance Notice of Proposed Rulemaking on Computer Reservations Systems (Proposed Part 255), Docket 41686, Comment of United Airlines, Inc., November 29, 1983.

U.S. Civil Aeronautics Board. “Evaluation of the Increases in Computer Reservation Systems Booking Fees to Participating Carriers,” Docket 43605, Exhibit NW-R-733.

U.S. Department of Justice, Civil Investigative Division. Civil Investigation Demand No. 5087, Deposition of Richard E. Murray, June 1, 1983.

U.S. District Court, Central District of California. Appropriation Request, AR 901-566-5-8, American Airlines document AA072608.

U.S. District Court, Central District of California.
American Airlines document AA072613.

U.S. District Court, Central District of California.
American Airlines document AA072616.

U.S. District Court, Central District of California. Memorandum from T.G. Plaskett to A.V. Casey, January 17, 1977, American Airlines documents AA080706, AA080707, and AA080708.

U.S. District Court, Central District of California.
American Airlines document AA080717.

U.S. District Court, Central District of California.
Continental Airlines document CH032910.

U.S. District Court, Central District of California.
United Airlines document UA001374.

U.S. District Court, Central District of California. Complaint for Damages and Injunctive Relief, Plaintiffs vs. American Airlines, Inc., and United Airlines, Inc., Docket 43065, Exhibit NW-RT-730.

U.S. District Court, Central District of California. Complaint for Damages and Injunctive Relief, Plaintiffs vs. American Airlines, Inc., and United Airlines, Inc., Docket 43065, Exhibit NW-R-731.

U.S. District Court, Central District of California. Supplemental and Amended Complaint for Damages and Injunctive Relief, Plaintiffs vs. American Airlines, Inc., and United Airlines, Inc., CV No. 84-8918 ER.

U.S. General Accounting Office. “Airline Competition: Impact of Computerized Reservation Systems,” Resources, Community, and Economic Development Division, B-223042, May 1986.

Webb, C., formerly of IBM, Marathon, FL. Interview with authors, July 9, 1986.

## About the Authors

Duncan G. Copeland is a candidate for the doctor of business administration degree at the Harvard Business School. He holds an H.B.A from the University of Western Ontario. Prior to arriving at Harvard in 1985, he worked as a management consultant for five years. His research involves the effect of information technology on the conduct of the firm.

James L. McKenney is a professor of business administration at the Harvard Business School. He received a B.S. and an M.S. from Purdue University and his Ph.D. from the University of California, Los Angeles. He has been at Harvard since 1960, where he has taught in the MBA, doctoral, and executive education programs. Recently, his research has focused on the design and management of computer-oriented network systems, and office support and knowledge-based systems. He is the author of several books and papers, including his most recent book, Corporate Information Systems Management—The Issues Facing Senior Executives, which was co-authored with Jim Cash and Warren McFarlan.
