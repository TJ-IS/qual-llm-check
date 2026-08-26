---
otero_id: 24390
otero_key: "X8ZGGM4G"
title: "Global Logistics System Asia Co., Ltd"
authors: "Jan Damsgaard"
year: "1999"
journal: "Journal of Information Technology"
doi: "10.1080/026839699344601"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Journal of Information Technology (1999) 14, 303± 314

# Global Logistics System Asia Co., Ltd

JAN DAMSGAARD

Department of Computer Science, Fr. Bajersvej 7E, Aalborg University, DK-9229 Aalborg, Denmark

This case study examines the air cargo industry in Hong Kong, where an electronic trading network was launched by four international airlines with considerable success in the mid-1990s. Two key factors explain the success. First of all, the electronic network limited its service to preserve carefully the distribution of power among the stakeholders. Secondly, the system roll out took advantage of the four founding airlines local strongholds as points of departure. The case study also addresses the possibilities of extending the network into a full-scale electronic market for Hong Kong’ s air cargo community.

## Introduction

Through the window of his of® ce, Terry Keaveny saw a Cathay Paci® c B747± 400 freighter take off from Kai Tak, the busiest international cargo airport in the world and the third largest in terms of passengers. By the mid-1990s more than HK\$1.5 billion worth of cargo or 20% of Hong Kong’ s exports were handled in Kai Tak airport. Time is the single most critical factor in an industry that prefers to move close to the speed of sound. Any delays in administrative procedures or handling of cargo are costly and may even degrade its value. The mean shipment time for airfreight was 6 days and 90% of that time was spent on the ground. Something had to be done to improve this unsatisfactory situation. As the managing director of Global Logistics Asia Co., Ltd he was in charge of the design and implementation of an electronic air cargo booking and checking system that would cut the excess time considerably. He also knew that he needed to attract the majority of the freight forwarders and airlines for the system to become viable.

The provision of air cargo services is complicated by the fact that an airplane can only lift a maximum weight. The volume capacity is of course ® xed. For ef® ciency reasons, it is therefore extremely important that a plane is always loaded with the optimal weight when airborne. In practice this is achieved by setting a maximum weight for each aluminium air cargo container or pallet that is loaded on to a plane (this way, the weight is also balanced).

These restrictions on weight and volume are also re¯ ected in the provision of air cargo space to customers (shippers). For example, textile products easily ® ll a container without exceeding the maximum weight, while machine parts reach the weight limit long before it is full. To maximize utilization of cargo space, it is therefore imperative that weight and volume match. As a consequence, cargo items from different sources are often matched to ® t the best volume: weight ratio. A high weight, low volume cargo (e.g. machine parts) is then packaged with a low weight, high volume cargo (e.g. designer textiles) into one container or pallet. As we shall see this fact has a tremendous impact on the provision of services and business processes in the air cargo industry and also on the provision of electronic trading net services.

## Industry background

At the beginning of the 1990s the pro® t margin emanating from passenger traf® c via air was constantly decreasing and the competition among various airlines was ® erce. As a response many airlines had turned to new business opportunities to complement declining pro® ts. One answer was the air cargo business, which was becoming an important supplement for many airlines.

In Hong Kong the air cargo transportation industry had developed substantially in the 1990s and it was quite a mature business. Approximately 20% of Hong Kong’s external trade passed through Kai Tak as air cargo. This meant on average over HK\$1.5 billion worth of cargo was handled through the airport on a daily basis.

## Airports

In 1996 Hong Kong’s international airport, Kai Tak, overtook Tokyo’ s Narita airport in terms of international cargo and became the world’s biggest. Next in terms of cargo was Miami, followed by Frankfurt and New York’s Kennedy Airport (see Table 1 for details on the tonnage handled at Kai Tak Airport). The throughput of Kai Tak was even surpassing its nominated cargo capacity of 1.5 million tons, which emphasized the urgent need for the airport that was under construction at Chek Lap Kok. The new airport was designed to be capable of handling 3 million tons of cargo a year, which was expected to be suf® cient well into the new century.

Table 1 Cargo handled at Kai Tak Airport per annum

<table><tr><td>Year</td><td>Million tons</td></tr><tr><td>1997</td><td>1.69</td></tr><tr><td>1996</td><td>1.56</td></tr><tr><td>1995</td><td>1.46</td></tr><tr><td>1994</td><td>1.29</td></tr><tr><td>1993</td><td>1.14</td></tr><tr><td>1992</td><td>0.96</td></tr><tr><td>1990</td><td>0.80</td></tr><tr><td>1987</td><td>0.61</td></tr></table>

The table was compiled using ® gures in the Hong Kong Annual Digest of Statistics (Census and Statistics Department, 1997). Figures from the South China Morning Post were used for 1997.

## Airlines

One of the major airlines operating in the Hong Kong air cargo market was Cathay Paci® c. From its origins as a small regional freight operator established in 1946, by the mid-1990s Cathay Paci® c had grown to become a major airline with 45 destinations on ® ve continents. Cathay Paci® c made around 20% of its revenue from cargo, totalling US\$900 million in 1996.

Cathay Paci® c Cargo had a ¯ eet of six dedicated Boeing 747 freighters, four 747± 200s and two 747± 400s. The ® rst B747 freighter was acquired in 1982 and the ® rst 747± 400 freighter was delivered to Cathay Paci® c in 1994. The 747± 400 freighter could carry more cargo (122 t) further than any other commercial jet freighter and also had the lowest operating cost per ton-kilometre of any dedicated cargo-carrying aircraft.

The demand for cargo capacity was expected to grow so Cathay Paci® c decided to introduce Airbus A330s and A340s into the ¯ eet. In 1997 Cathay Paci® c Cargo’s uplift approached 48 000 t per month with around 57% being uplifted on passenger ¯ ights. Cathay Paci® c was one of the largest but still it was just one of many players active in the provision of air cargo services.

Table 2 Stakeholders and their roles in the air cargo industry

<table><tr><td>Stakeholder</td><td>Function</td></tr><tr><td>Shipper</td><td>Has cargo to send</td></tr><tr><td>Freight forwarder</td><td>Handles cargo from sender to receiver</td></tr><tr><td>Air cargo terminal</td><td>Controls the cargo while at the airport</td></tr><tr><td>Customs</td><td>Releases cargo for import or export</td></tr><tr><td>Airport</td><td>Handles the physical movements of cargo</td></tr><tr><td>Airline</td><td>Provides air transportation for cargo</td></tr></table>

## The Hong Kong air cargo community

Hong Kong’s air cargo community was populated by a number of stakeholders, which performed a number of complementary tasks. Table 2 summarizes the players and their roles.

## Shippers

Some time-critical and high-value products may be worthwhile \`shipping’ via air. This is, for example, the case for designer textiles. They are usually for a speci® c season and they have to reach the market within a certain time span to be sold at the right price (to be pro® table). It may also be true for some electronics, cut ¯ owers and for some critical machine parts (often spare parts). To send cargo to a destination, a shipper will contact several freight forwarders to ® nd space and obtain the best price and service offered.

## Freight forwarders

The freight forwarder negotiates a contract with the shipper for the price and terms of a shipment. The freight forwarder then arranges for the cargo to be packed for transport, handed over to the air cargo terminal operator and ® nally received and delivered at the destination. The freight forwarder also books space with some airline.

In the mid-1990s there were approximately 1000 airfreight forwarders operating in Hong Kong. Most of them were members of HAFFA (Hong Kong Association of Freight Forwarding Agents). Many were small companies with less than 50 employees.

## The air cargo terminal operator

The air cargo terminal operator controls the movements of the cargo while at the airport. On the sending end, they accept cargo from the freight forwarder. They thereafter store the cargo until it has either been released for export by customs or rested for at least 24 h at the terminal (for safety reasons). The terminal operator then arranges for the cargo to be loaded on to the designated plane. On the receiving end, an air cargo terminal operator accepts cargo from arriving planes and stores the cargo until it has been released by the receiving country’s customs department. A freight forwarder thereafter collects the cargo.

A number of competing terminal operators usually operate in an airport. However, Hong Kong Air Cargo Terminals Limited (HACTL) was granted a franchise that ensured them the exclusive right to handle all cargo terminal services at Hong Kong’s Kai Tak airport. HACTL had performed very well ± it had the lowest number of handling errors in the world with only one per 22 000 shipments. Nevertheless the Hong Kong Government saw the migration to the new airport (Chek Lap Kok) as an opportunity to end HACTL’s franchise. At the new airport a Singaporebased consortium, Asia Airfreight Terminal (AAT), was also granted a licence to perform airport logistics. The AAT consortium would offer services parallel to HACTL.

In preparation for open competition HACTL was investing HK\$8 billion to construct an air cargo terminal, SuperTerminal 1, at the new airport with a design cargo capacity of 2.6 million tons, while AAT was investing HK\$800 million for a facility which would handle 420 000 tons on an annual basis.

## Customs

Customs receives an application for export from a shipper or a freight forwarder on his behalf. After checking the application customs issues an export licence. The terminal operator will only accept cargo with an issued export licence. While in the custody of the terminal operator, customs may decide to inspect a shipment physically. Subsequently the air cargo terminal operator will arrange for the cargo to be loaded on to a plane as requested by an airline. At the receiving end, customs receive an application for import and, when issued, the air cargo terminal operator may release the shipment into the custody of a freight forwarder.

In Hong Kong the Customs and Excise Department was responsible for the collection of trade declarations. As a free port Hong Kong had few restrictions on export and imports. (However, Hong Kong exercised strict control on textile exports and on alcohol, tobacco and perfume on the import side. Of course there are the usual restrictions when it came to drugs, weapons, etc.) Customs and Excise would pass the trade declarations on to the Census and Statistics Department for trade-related statistics. The Hong Kong Census and Statistics Department process more than 15 million trade declarations and 10 million manifests annually.

## Airports

Airport personnel handle the physical movements while the cargo is inside the airport. The airport personnel will pick up the cargo from the terminal operator and have the responsibility of getting the cargo on to the right plane. At the receiving end, they move the incoming shipments to the cargo terminal.

## Airlines

An airline provides transportation for air cargo shipments. For usual shipments the items are packed into special air cargo containers made of aluminium or on to pallets. See Figures 1± 3 for a sample of air cargo containers, pallets and racks, respectively. There are restrictions on the weight of a container or pallet (as described earlier). Flights are scheduled in advance according to demand and available planes. Most dedicated freighter ¯ ights take place during night-time when airways and airports are less crowded.

## Business processes

In the mid-1990s air services required much capital as each plane constituted a signi® cant investment. Air cargo travelled both on dedicated freighters and on regular passenger planes. Operating costs were high but relatively ® xed. The high operating costs and the high investments made the supply of air cargo capacity rather constant throughout the year.

![](/api/attachments/X8ZGGM4G/fulltext/images/cb715ca289c745b596796e8218a071216cd03aacc8da707e8a868ca8443b9803.jpg)  
Type: LD3 COOLTAINER Internal volume: 125.41cu.ft. 3.55mc Tare weight: 190kg Weight limitation: 1,588kg Aircraft type: 747, 747F, 777, Airbus

Figure 1 Air cargo container

![](/api/attachments/X8ZGGM4G/fulltext/images/412b045c7dcb247e0aa7c5b848200d3075d0e0a002e25dea6b73e592c211fcb4.jpg)  
Type: 2H NETTED PALLET Internal volume: 745cu.ft. 21.10mc Tare weight: 105kg Weight limitation: 6,804kg Aircraft type: 747F

Figure 2 Air cargo pallet  
![](/api/attachments/X8ZGGM4G/fulltext/images/65bb466575db73907d55d76f928d55d9119509ed10f22e70041d9b7f72568abc.jpg)  
Figure 3 Car rack for air cargo

In contrast, there were huge seasonal ¯ uctuations in the demand for air cargo capacity in Hong Kong. During the peak seasons the demand exceeded the supply, while in the low season the opposite applied. This created an environment of mismatch between supply and demand (see Figure 4).

To minimize the effect of this mismatch between supply and demand, airlines had out-sourced the risk and the responsibility of having an ef® cient usage of their cargo capacity to freight forwarders. They had done so by selling their space in big chunks (allotments) distributed throughout the year. This way they circumvented the discrepancy in demand and supply. Terry Keaveny explained:

![](/api/attachments/X8ZGGM4G/fulltext/images/db83de9c60c553981774bbc31bd422ba3b77f74b826fcb4c78d6ed05f7ca4401.jpg)  
Figure 4 Graph of supply and demand for air cargo capacity distributed throughout the year. Peaks occur in May and in the autumn

In certain times of the year, getting a full load is extremely sure. This is in the peak season, which runs from the end of September to Christmas. In this period you cannot get space without a lot of money. The airlines run a system, which they call a lock-in system with their major customers. The airlines guarantee to provide so much space in the peak season, the freight forwarder then promises to book a certain amount of space in the low season.

The freight forwarders’ business was therefore based on detailed and time-critical knowledge of the industry. They acted as brokers. They put together bits of information about departures, immediate demand for transportation, season variations and available space. Based on these contingencies they calculated a price for a shipment. This would re¯ ect an immediate and timedependent price.

Freight forwarders also reallocated space among themselves, as it was common for a freight forwarder (co-loader) to borrow/lend/sell/buy space to/from colleagues. Another common method of optimizing a shipment was in the packing of the cargo items as described earlier. This was to make a pro® t by matching shipments with inverse density and then repackaging them for the highest allowable density. A quoted price, therefore, did not re¯ ect an actual ® xed price, but it was carefully calculated according to the speci® c freight forwarder’s immediate situation.

These factors combined left the air cargo market very competitive and opaque. The pricing was complex and, to an outsider, the market was impenetrable. This way the freight forwarders had found a niche in the market in which they pro® ted from detailed knowledge and opportunistic behaviour. However, it also meant there was a high degree of interdependence between the forwarders and the airlines.

## The need for an electronic network

Time is the single most important factor in an industry where the distribution of goods moves close to the speed of sound. Any delays in administrative procedures or handling of goods are costly and may even degrade the value of goods (e.g. cut ¯ owers or fruits).

In the early 1990s the average shipment time for airfreight was 6 days. Of that time, 90% was spent on the ground. Something had to be done to improve this unsatisfactory situation. As one freight forwarder passionately explained:

We must do something about this or we will all face a huge problem. All participants in the air cargo industry will have to keep abreast of emerging technologies if they want to survive. Competition will become increasingly ® erce.

Sea-based cargo was becoming a close competitor. Ships were getting faster and the cost for sea cargo was only a fraction of air cargo. Some shippers were already taking advantage of multimode combinations of transportation (e.g. by sea to central hub in Africa followed by air distribution to various parts of Europe).

The need to coordinate, streamline and optimize all the land-based activities were clear. The need prompted four international airlines to take action. They took the initiative to form a company that should address the needs of the growing and complex air cargo industry.

The founders envisioned that electronic means of coordinating cargo-related information was the key that could provide for more reliable, accurate and timely exchange of information. Eventually a smoother exchange of data would speed up the processes in the entire industry. The idea of establishing an electronic trading net raised considerable interest but also some controversy in the business community. Terry Keaveny explained about the vision of the initiating airlines:

The chief executives of the airlines got together and decided that the use of electronic messages on the passenger side worked extremely well, but there were no electronic distributions on the cargo side at all. Therefore they suggested that is was worthwhile putting together a venture to provide electronic cargo distributing services.

## The formation of Global Logistics System Asia Co., Ltd

At the beginning of 1991 Cathay Paci® c, Air France, Lufthansa and Japan Airlines incorporated Global Logistics System Asia Co., Ltd, which soon became more commonly known as Traxon Asia. However, the aim was to create an international electronic network for the growing and complex air cargo industry. The four airlines therefore set up two other companies: Traxon Europe Ltd, and the coordinating company Traxon World Wide Ltd. Traxon Europe was mainly run by Air France, Lufthansa and Traxon World Wide. While in Asia, Traxon was run by Cathay Paci® c, Air Japan and Traxon World Wide. Traxon World Wide played a minor role; its main function was to provide coordination between the two regional companies and the founding airlines. Therefore Air France and Lufthansa German Airlines developed the Traxon Europe System, while in Asia, Cathay Paci® c and Japan Airlines joined by Korean Airlines developed the Traxon Asia system. See Figure 5 for the structure and management of Traxon Asia Ltd.

## The beginning

The founding airlines wished to form one single coherent worldwide network and therefore they tried to persuade other airlines to join their network. However, the other airlines read the initiative as a strategic manoeuvre to hijack the lucrative air cargo market. They feared a situation where a few airlines would dominate (as some airlines had done in the past for passenger ¯ ight reservation systems). Therefore, a lot of defensive actions were launched and competing airlines set up similar systems around the world. Starting with only a portion of the market, Traxon needed to carefully plan the design and implementation of its system.

![](/api/attachments/X8ZGGM4G/fulltext/images/dd95ac187bbf5460e6d3aea3199caf53303e27c64b1f4acfc45d82e9d78d8b82.jpg)  
Figure 5 The structure and management of Traxon Asia Ltd.

## Functionality, technical implementation and pricing

Traxon designed its system to provide a variety of services. This included checking space availability, booking, electronic airway bill transmission (the documentation/paper work needed for sending a shipment, equivalent to a bill of loading) and status checking. Figure 6 depicts Traxon’s system and the information exchange in the air cargo community.

## Introduction to the Traxon system

The idea of the Traxon system was to operate a network with the following aims-

(1) To make electronic data communications possible between the partners participating in the transport chain.

(2) To streamline data.

(3) To use industry standards to simplify data.

(4) To accelerate the data ¯ ow.

The Traxon system was based on the recommendations for a cargo community system (CCS) of the International Air Transport Association (IATA) (URL: http://www.iata.org/). The result was a system which allowed electronic data communications services based on different communication protocols, networks and standards used in the international air cargo industry. It offered value-added services, such as intermediate storage facilities for the data exchanged between communicating partners or conversion facilities for exchanged data between partners that \`do not speak the same language’ and was available 24 h a day in a non-stop operating mode. The exchange of data using electronic means was called electronic data interchange (EDI) (see Appendix A for a description of EDI), which had the following bene® ts,

![](/api/attachments/X8ZGGM4G/fulltext/images/ee5905005429f9a4565bc4cb391cc552c8dede17a5fe4c670003a334b6b8cab9.jpg)  
Figure 6 The information exchange in Hong Kong’ s air cargo community. COSAC was HACTL’ s system for air cargo handling at the Kai Tak Airport in Hong Kong. The Customs and Excise Department cleared cargo through COSAC. The airport updated the COSAC system when it delivered or received cargo to/from HACTL’ s storage facilities. HACTL informed the airport which cargo had been cleared and could be collected. The airlines had access to the COSAC system through the worldwide SITA (Societ‚ Internationale de A‚ ronautiques) system. The freight forwarders had two options. They could be connected to Traxon whereby they also gained access to COSAC. However, they could also choose to connect to the COSAC system directly via a modem (but this way they could not connect to the airlines). The Civil Aviation Department (URL: http://www.info.gov.hk/cad/index.htm) also fed the system with up-to-date ¯ ight data

(1) EDI reduced the paper ¯ ow.

(2) EDI reduced the manual processing of transactions.

(3) EDI reduced delays when forwarding transactions.

(4) EDI reduced the processing time of business transactions.

(5) EDI allowed a faster and more accurate exchange of information between business partners.

(6) EDI allowed the usage of modern communication networks.

## Products

Traxon products can be divided into types of connection and the functions supported (see Figures 7 and 8). There were three connection types available: (1) a Traxon-PC stand-alone version, (2) a Traxon-PC LAN (Local Area Network) version and (3) hostto-host connection.

The Traxon system supported the following functions.

(1) Airline availability.

(2) Air waybill data transfer.

(3) Allotment list.

(4) Allotment status.

(5) Cargo booking.

(6) Flight schedule.

(7) Rate information.

(8) Status history, tracking and update.

It also supported a number of value added functions.

(1) Civil Aviation Department ¯ ight schedule information.

(2) Foreign currency exchange information.

(3) Hong Kong Air Cargo Terminal System (COSAC) access.

(4) House manifest data transmission and management.

(5) Internet e-mail and e-mail to fax service.

(6) Neutral waybill printing.

(7) Traxon mail.

![](/api/attachments/X8ZGGM4G/fulltext/images/c7ef26d8ab936a9a87965cfddb58b2728b40fed0d843b688337af522bada9b4f.jpg)  
Figure 7 LAN set-up of Traxon

![](/api/attachments/X8ZGGM4G/fulltext/images/6f91ba252a6ca33740a3197aba6b4fa6a67984fffedfacf2495427200fddf8bc.jpg)  
Figure 8 Example of a Traxon PC screen

## Pricing

A typical freight forwarder that subscribed to the Traxon system was supplied with a PC, software and a communication link. They were charged a monthly subscription fee of HK\$5500. A fee was also paid per transaction. The fee varied with the kind of transaction. The airway bill transaction was the most expensive. The freight forwarder only paid for status information. A reactive status check cost US\$0.25 and a proactive one US\$0.20. Everything else was paid for by the airlines. An airline paid US\$1.15 for a booking. For an availability request they paid US\$0.15 and US\$0.25 for a status request sent to the freight forwarder. So if there was an availability request by a freight forwarder, the airline was charged because availability requests were regarded as part of the airlines’ marketing efforts. The mean response time anywhere in the world was less than 10 s.

## Systems implementation

The founding airlines wished to form one single coherent worldwide network and, therefore, they tried to persuade other airlines to join their network. Two key factors explain Traxon’s immediate success.

Firstly, their implementation process took advantage of the respective airlines’ strongholds. Thus, locally based Cathay Paci® c was in charge of the roll out in Hong Kong, while in Japan it was Japan Airlines. A similar approach was applied in Europe. Furthermore, each local Traxon system had the other shareholder airlines as initial customers, which constituted a significant share of the air cargo market.

The second factor was Traxon’s ability to attract a majority of users (both non-shareholder airlines and freight forwarders). The Traxon service has high network externalities. In short, this means that, in the beginning, the bene® ts of joining are low and the risks high, but as more adopt, the more attractive and less risky it becomes to join the network. The best analogy is that of having a telephone: if you are the ® rst one to have a telephone, whom are you going to call? However, as more people (relatives, friends and business relations) join, the more bene® cial it becomes to join the adopters. At the same time it is attractive to wait to adopt until it can be determined whether the system will become predominant (e.g. the historic ® ght between Betamax and VHS in setting the standard for video cassette recorders). Therefore, the more adopters Traxon obtained, the more attractive it would become to join them. The dilemma was that the airlines would adopt the system insofar as a majority of the forwarders did. At the same time the freight forwarders would only adopt if most of the airlines did. The major challenge was how to get this spiral of self-enforcement going in favour of Traxon. The number of adopters needed for the spiral to automatically evolve is often referred to as \`critical mass’ (borrowed from nuclear theory where critical mass refers to the minimum mass of radioactive uranium that is necessary to get fusion going).

It was, therefore, essential that all parties would see bene® ts from the arrangement, i.e. decide to participate. Traxon, therefore, designed its system to accommodate the needs of the airlines, forwarders and air cargo terminals, but also carefully preserved the sensitive distribution of power and responsibilities between them.

The airlines bene® ted from Traxon by getting more detailed information about bookings and even an increased number of bookings. They also believed that the use of Traxon reduced the amount of lost business due to busy telephones or absent (busy) sales personnel. The airlines were provided with better information about each booking because the Traxon system reduced the number of errors in the bookings (by avoiding manual typing of bookings).

The freight forwarders improved their ef® ciency using Traxon because they could check available space with different airlines, make bookings electronically and quote prices faster and more ef® ciently. Before, freight forwarders had to use the phone and call several airlines to ® nd available space. Instead, by using Traxon they could perform these activities simultaneously. Traxon also allowed the freight forwarders to monitor cargo from the air cargo terminal in Hong Kong until it reached its destination overseas.

Hence, Traxon was a powerful monitoring, booking and sales tool, but it also had the potential to upset the sensitive distribution of power in the air cargo industry in Hong Kong. The use of an electronic network may add transparency to the market. For example, extending the network beyond the forwarders would allow a shipper to obtain information that was not available earlier. A key success factor for the electronic network was, therefore, that the players would not feel their business threatened by the network and, thus, would refrain from participating (using the network). The people behind Traxon recognized this and, therefore, they decided only to optimize existing routines and not to add new services. The Traxon system consequently did not carry any information about prices or discounts. This left the market opaque for outsiders and preserved the roles and power balance between the airlines, the freight forwarders and the shippers. This was the initial key to the success of Traxon in Hong Kong.

## Traxon after the ® rst initial phase

After its ® rst years of operation Traxon was able to enlarge and sustain its position as the dominant electronic trading network provider in Hong Kong’s air cargo community. As of January 1998 there were 187 freight forwarding agents connected to the system resulting in more than 8.8 million messages per year (1997). A number of airlines had given up their defence actions and they were now taking active part in the cooperative venture giving Traxon a de facto monopoly in the air freight community. Besides the shareholders (Air France, Cathay Paci® c, Japan Asia Airways Co. Ltd, Korean Airlines Co. Ltd and Deutsche Lufthansa AG), Traxon had also reached a distribution agreement with Air Canada, Royal Air Maroc, Finnair, British Airways, Cargolux Airlines, Emirate Airlines, Transasia, Hong Kong Dragon Airlines, KLM Royal Dutch Airlines, Air Hong Kong, Malaysian Airlines System, Martinair Holland, Northwest Airlines, Quantas Airways, Scandinavian Airlines System, Singapore Airlines and Swissair. Traxon Asia Ltd was also connected to a number of CCSs throughout the world (see Table 3).

Table 3 Traxon Asia Ltd’s worldwide-connected CCSs

<table><tr><td>Traxon Europea (Germany)</td></tr><tr><td>Traxon Indiaa (India)</td></tr><tr><td>Brucargo (Belgium)</td></tr><tr><td>Cargonaut (The Netherlands)</td></tr><tr><td>CargoNet (Australia)</td></tr><tr><td>Cargo Switch (Switzerland)</td></tr><tr><td>CCN (Singapore)</td></tr><tr><td>CCS-IL (Israel)</td></tr><tr><td>CCS-UK (UK)</td></tr><tr><td>Compu Clearing (South Africa)</td></tr><tr><td>Equation (UAE)</td></tr><tr><td>Eximnet (Thailand)</td></tr><tr><td>ICARUS (Ireland)</td></tr><tr><td>KargoBayan (Philippines)</td></tr><tr><td>Macnet (Malaysia)</td></tr><tr><td>SNS (North America)</td></tr><tr><td>Trade-Van (Taiwan)</td></tr><tr><td>Tradevision (Scandinavia)</td></tr><tr><td>US-CCS (North America)</td></tr></table>

<sup>a</sup>Sister organizations.

The result was that 94% of the air cargo volume lifted out of Hong Kong was coordinated through Traxon’s network. The rest (6%) accounted for unusual shipments. For example, ¯ ying racehorses was big business in Hong Kong which was worth millions of US dollars a year. Traxon was also extending its activities throughout Asia. Traxon also provided information distribution to 60% of the Japanese air freight market. As of December 1996 there were more than 2000 freight forwarders in approximately 5000 of® ces connected to the Traxon system worldwide. Table 4 summarizes the main events of Traxon Asia Ltd.

## Looking to the future

Terry Keaveny was very successful in building up a basic electronic infrastructure in the air freight industry. The distribution of power in the air cargo industry was maintained with the introduction of the electronic business network for coordinating air cargo services. A next step could be the establishment of an extended electronic market. However, none of the major stakeholders would stand to bene® t from such an arrangement. A realization of an electronic market was therefore not foreseen in the near future.

The airlines argued that the establishment of an electronic market would drive down pro® ts, because space availability and prices could be checked easily. This would make the market more uniform and the competition ® ercer. This had happened in the passenger transportation business, where prices could be checked through various electronic network systems at most travel agents. In the passenger traf® c business, one counter-measure had been to introduce frequent ¯ yer points. Frequent ¯ yer mileage adds haze to the market, it drives down incentives to look for optimal prices and it hooks in customers.

Table 4 Milestones in Traxon’ s history

<table><tr><td>Year</td><td>Milestone</td></tr><tr><td>1991</td><td>Foundation of Traxon Worldwide by Air France, Cathay Pacific, Japan Airlines and Lufthansa as a coordination unit of the worldwide Traxon activities. In August foundation of Traxon Asia by Cathay Pacific and Japan Airlines</td></tr><tr><td>1992</td><td>Datapak on-line flight information was introduced in Hong Kong. Irish CCS and Dutch CCS connected to Traxon. Release of the Traxon mail function</td></tr><tr><td>1993</td><td>American service provider TDNI connected to Traxon. Swissair, Korean Air, Cargolux, SAS, Air Canada, British Airways, Singapore Airlines, Tradevision, Singapore CCS and Belgian CCS joined Traxon. Traxon services were extended to the Philippines</td></tr><tr><td>1994</td><td>Emirates, United Kingdom CCS, Martinair and KLM joined Traxon. Korean Air joined as shareholder. Allotment list and status, status history, ABC flight schedule and Traxon LAN version were introduced in Hong Kong</td></tr><tr><td>1995</td><td>Finnair, and TradeVan joined Traxon. ABC rate information, exchange rate table and datapak on-line foreign exchange information were introduced in Hong Kong</td></tr><tr><td>1996</td><td>Royal Morac joined Traxon. Traxon Internet e-mail and e-mail-to-fax launched in Hong Kong. Traxon users can send house manifest data to HACTL through Traxon PC</td></tr><tr><td>1997</td><td>Qantas and Malaysian Airlines System joined Traxon</td></tr></table>

The freight forwarders were not interested in creating an electronic market for coordinating air cargo services, because they (as brokers) gained from the non-transparency and they made their pro® t from coordinating the market. The freight forwarders would also stand to lose the pro® table business of repacking shipments and of buying and reselling space if such an electronic market was established. With the introduction of Traxon they had successfully in¯ uenced the development of the electronic network. In the future they were ready to pursue every attempt to delay the arrival of a full-scale electronic market system. Terry Keaveny clari® ed the situation in this way:

An air freight futures market has been suggested in Europe along the lines of a foreign exchange market. Airlines would put available space on the market. I doubt if it will be the future, because people wish to keep control of their market-place. They will not voluntarily give away control to the market. . . . The air cargo is not a high yield business, the rates now are exactly the same as they were 10 years ago, so in real terms the rates are declining steadily. The only thing that would come out of an open market is that the rates would be declining faster.

Brokers reduce the need for buyers to contact a large number of alternative suppliers individually. An electronic market pairs buyers and suppliers through a central mediation mechanism that allows the buyers to browse among many sellers’ offerings. This way the buyer can screen out inappropriate suppliers and compare offers quickly, conveniently and inexpensively. Thus, the electronic brokerage can (1) increase the number of alternatives that can be considered, (2) increase the quality of the alternative eventually selected and (3) decrease the cost of the entire product selection process. The consequence of this reduction in search costs drives down prices, because no broker or seller will be able to maintain prices signi® cantly above their marginal costs (this would immediately be detected by buyers).

In the Hong Kong air cargo market it was in the complex selection process that the freight forwarders made their pro® t. The complexity of air cargo brokerage was the single most important reason for the very existence of the freight forwarders. Furthermore, the establishment of an electronic market would drive down pro® ts for the airlines and it would jeopardize the existence of the freight forwarders. So who would push for an electronic market?

The consumers of air cargo services (the shippers) were the ones who would bene® t from an electronic market containing all information about prices, services and space. They would enjoy lower prices due to higher transparency and increased competition among freight forwarders and airlines. An electronic market would also open the possibility for the shippers to bypass the freight forwarders entirely. It was therefore expected that the shippers would ceaselessly push for more transparency and an open market and that they would seek to disintermediate the freight forwarders. Many freight forwarders feared that the shippers could be successful, but the freight forwarders would seek to hinder any move towards a realization of an electronic market in the air cargo industry.

However, in the late 1990s the popularity and low cost of the Internet were prompting some nonshareholder airlines to challenge Traxon by setting up track and trace systems on the World Wide Web (see, for example, http://www.sascargo.com). These systems could be accessed by anyone around the world and they were free of charge. So, despite the apparent order and stability in the air cargo industry, it was not yet clear how the user friendly and universal accessible World Wide World would impact on Traxon’s de facto monopoly, the freight forwarders’ role as indispensable brokers, the airlines’ pro® t margin and the provision of air cargo services to the shippers?

## Acknowledgement

The preparation of this case study was ® nanced in part by the Centre for Asian Business Cases, School of Business, The University of Hong Kong (http;//www.business.hku.hk).

## Biographical note

Jan Damsgaard (damse@cs.auc.dk) is assistant professor in information systems at Aalborg University. His research interests include electronic commerce, electronic markets, Intranets, Extranets, ERP (Enterprise Resource Planning) and EDI, in particular, the diffusion and implementation of these complex, standard-based and network technologies. His work has appeared in international journals and conferences (see http://www.cs.auc.dk/\~damse).

## Address for Correspondence:

Department of Computer Science, Fr. Bajersvej 7E, Aalborg University, DK-9229 Aalborg, Denmark.

## Appendix A

In the 1990s traditional businesses generated and processed a staggering volume of paper documents. These ranged from purchase orders and invoices to product catalogues and sales reports. This information provided the vital information ¯ ow that preceded, accompanied or followed the physical goods in commercial transactions.

The majority of the data on commercial paper documents was generated from existing computer applications. The paper documents were printed and copied before the information they contained was ® nally communicated by mail or fax. The business partner in turn, rekeyed all this information into another computer application for further processing.

EDI provided trading partners with an ef® cient business tool for the automatic transmission of commercial data from one computer system directly to another. The process of transmitting a message via EDI can be summarized as follows (see Figure 9).

(1) Data are extracted from the in-house application of company A.

(2) These data are then passed from the in-house application and input to an EDI translation software package.

(3) This software package takes the data and translates them into an EDI message.

(4) This EDI message is then transmitted via the VAN (Value added network) to company B where it is read by the EDI translation software on their personal computer and \`translated’ back to a format suitable for their particular in-house application system.

In principle, companies should not worry about different incompatible computer systems. Through the use of EDI message standards, data may be communicated quickly, ef® ciently and accurately irrespective of the users’ internal hardware and software equipment.

The successful implementation of EDI promised major bene® ts for a company and its trading partners.

## Cost ef® ciency

Signi® cantly reducing the volume of paper to be handled results in immediate savings in administrative and personnel costs. Staff can be redeployed to other more value-added functions within the organization.

## Increased speed

Large volumes of commercial data can be communicated from one computer to another in a matter of minutes, enabling faster response and greater customer satisfaction.

![](/api/attachments/X8ZGGM4G/fulltext/images/0ff88fd27b93806a1ad9de32755c246eb1140e160f459b0976a2da66e4a3b750.jpg)  
Figure 9 A typical EDI set-up

## Improved accuracy

EDI eliminates the inevitable errors resulting from manual data input.

## Better logistics management

EDI enables companies to manage and control production, purchasing and delivery requirements better. EDI is a key component of just-in-time manufacturing and quick response customer± supplier links, resulting in signi® cant reductions in inventory levels.

## Appendix B

## Learning objectives

Most people concur that electronic markets constitute a signi® cant innovation that will radically alter markets in the future. However, two key questions remain. Who will stand to bene® t from electronic markets? How should various existing market players position themselves in regard to initiatives to establish such markets?

These two questions are examined by studying the air cargo industry in Hong Kong where an electronic network has recently been launched with considerable success. The case study analyses how and why this electronic network became an instant success and it also addresses whether the network will evolve into an electronic market. Furthermore, which stakeholders are in favour of such a move and who will seek to resist it?

## Teaching guide

Suggested assignment questions are as follows.

(1) Describe the different stakeholders using Porter’s (1985) value chain and their interests in the air cargo community, in particular with regard to information needs and the implications of getting access to this information.

(2) Describe the air cargo industry using Porter’s (1985) competitive forces.

(3) Describe a future scenario. Will the shippers be connected to the system? Can two Traxon-like systems co-exist in the air-cargo industry? How will the emergence of Extranets, World Wide Web and the Internet affect Traxon in general?

(4) What should the other airlines (non-shareholder airlines) have done when Traxon was ® rst introduced?

## More on electronic markets in the air cargo industry

Christiaanse and Huigen (1997) described an attempt to establish an electronic market in The Netherlands’ air cargo community. The attempt was launched by the University of Amsterdam and implemented by Reuters (newsagency). The initiative focused on creating transparency in the provision of air cargo space and services. The system failed due to a mis® t of interests between stakeholders, which was ignored by the initiators. The authors explained that the freight forwarders hesitated and ® nally withdrew their support for three reasons: (1) fear of elimination of the freight forwarder, (2) fear of decreasing pro® t margins and, ® nally, (3) negative attitudes towards electronic business. In our study we easily ® nd support for (1) and (2), but in Hong Kong the forwarders have been enthusiastic about using the electronic network. This is mainly because the network was introduced in a manner which preserved and supported forwarders’ business processes. The reason for Dutch forwarders’ reluctance to electronic business may be local or due to their experiences with the failed electronic market system. Christiaanse and Huigen (1997) also reported heavy resistance from the airlines for reasons that are less obvious. The authors concluded that the system was abandoned because it was not viable for an electronic market system to operate if the intended participants refuse to cooperate.

This example from The Netherlands clearly supports the observations made in this case. If the electronic network does not respect and preserve current business practices and the position of the stakeholders, it will fail, because the players will counteract by not playing. A further controversy is the fact that the system was sponsored and promoted by interests residing outside the air cargo community (Reuters and the University of Amsterdam). In our opinion it is clear that established stakeholders will not willingly give up their control of the market to outsiders.

## Supplementary reading

Bakos, J. Y. (1991) A strategic analysis of electronic marketplaces. MIS Quarterly 15(3), 295± 310.

Christiaanse, E. (1996) American Airlines: the smarts system electronically supporting the knowledge worker, in J.D. Coelho, T. Jelassi, W. Koning, H. Krcmar and M. Saaksjarvi (eds) Proceedings of the Fourth European Conference on Information Systems, Vol. II, (Litogra® a Amorim, Lisbon, Portugal), pp. 1293± 307.

Christiaanse, E. and Huigen, J. (1997) Institutional dimensions in information technology implementation in complex network settings. European Journal of Information Systems, 6, 77± 85.

Christiaanse, E., O’Callaghan, R., Been, J. and Diepen, T.V. (1995) Electronic markets in the air cargo community, in G. Doukidis, B. Galliers, T. Jelassi and F. Land (eds) Proceedings of the Third European Conference on Information Systems, (Print Xpress, Athens, Greece), pp. 901± 15.

Damsgaard, J. and Lyytinen, K. (1997) Hong Kong’s EDI bandwagon. Derailed or on the right track?, in T. McMaster, E. Mumford, E.B. Swanson, B. Warboys and D. Wastell (eds) Facilitating Technology Transfer Through Partnership: Learning from Practice and Research, (Chapman & Hall, London pp. 39± 63.

Johnston, H.R. and Vitale, M. (1988) Creating competitive advantage with interorganizational systems. MIS Quarterly, 12(2), 153± 65.

Kambil, A. and Heck, E.V. (1996) Competition in the Dutch Flower Markets (Case). (New York University, New York).

Krcmar, H., Bjù rn-Andersen, N. and O’ Callaghan, R. (eds) (1995) EDI in Europe: How It Works in Practice. (John Wiley & Sons, Chichester, New York, Brisbane, Toronto, Singapore).

McKenny, J. (1995) Waves of change (Harvard Business School Press, Boston).

Porter, M.E. (1985) Competitive Advantage: Creating and Sustaining Superior Performance. (The Free Press, New York).

Wrigley, C.D., Wagenaar, R.W. and Clarke, R.A. (1994) Electronic data interchange in international trade: frameworks for the strategic analysis of ocean port communities. Journal of Strategic Information Systems 3(3), 211± 34.
