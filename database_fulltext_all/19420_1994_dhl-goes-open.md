---
otero_id: 19420
otero_key: "ABYR7EFV"
title: "DHL goes ‘open’"
authors: "K V Ramani; Rick McKinney"
year: "1994"
journal: "The Journal of Strategic Information Systems"
doi: "10.1016/0963-8687(94)90013-2"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Case study

DHL goes 'open'

K V Ramani
Computers and Information Systems, Indian Institute of Management,
Ahmedabad 380015, India

Vice President (Information Systems), DHL Worldwide Express, 1 Tai Seng Drive, Singapore 1953

DHL is the market leader in the worldwide air express industry. During the late 1980s DHL moved to an open architecture based on Unix for all its operations worldwide. The business benefits of this move have been recognized by the award to DHL Singapore of the National IT Award for outstanding achievements in the application of IT for competitive advantage.

Keywords: air express service, information technology, competitive advantage

DHL, known after its founders Dalsey, Hillblom and Lynn, was founded in 1969 to serve a specific need of the maritime industry: to reduce the time for customs clearance of seaborne cargo. DHL introduced an air express service to send the shipping documents by air to the customs facility in the destination country well ahead of the ship's arrival, and this move expedited the clearance procedures. This innovative offering of a dependable and fast door-to-door service from DHL proved an overwhelming success and gave rise to the international air express industry.

DHL's first door-to-door air express service started in the USA, linking San Francisco to the Hawaiian islands in 1969. The network then expanded to include South-east Asia, the Far East and the South Pacific in 1971, UK and Ireland in 1974, Europe in 1975, Canada in 1976, followed by Mexico, the Caribbean islands and Latin America in 1978. Service to Africa was established in 1979, Eastern Europe in 1983 and the People's Republic of China in 1986. Today, DHL is the largest international cross border air express company in the world, serving over 70 000 destinations and covering 186 countries. DHL's share of the world market for air express services is estimated at around 50 to 60 per cent, far ahead of its competitors Federal Express, UPS and TNT.

Table 1 charts the rapid growth of DHL. The company owns and operates about 200 aircraft and uses a multitude of commercial and charter airlines, thereby offering more than 1500 flights every day to carry its shipments between international destinations. On the ground, DHL's operations are supported by more than 7000 vehicles to transport the documents to their final destinations.

Table 1 Growth of DHL

<table><tr><td>Year</td><td>Number of shipments</td><td>Customer base</td><td>Personnel</td></tr><tr><td>1975</td><td>2 000 000</td><td>30 500</td><td>400</td></tr><tr><td>1978</td><td>5 400 000</td><td>85 000</td><td>6 500</td></tr><tr><td>1983</td><td>12 400 000</td><td>250 000</td><td>11 300</td></tr><tr><td>1988</td><td>44 000 000</td><td>550 000</td><td>19 000</td></tr><tr><td>1990</td><td>60 000 000</td><td>900 000</td><td>25 000</td></tr></table>

Source: DHL annual report, 1991.

DHL employs about 30 000 people to staff its 1400 locations worldwide, including its headquarters in Brussels.

## Early uses of IT

IT in DHL started in 1981 with the implementation of a System/34 in the UK for billing applications. Today, DHL has Pyramid and IBM systems in the USA and UK, HP systems in Europe and South America, NCR systems in Africa, and HP and Fujitsu systems in the Asia-Pacific region.

Apart from standard computer applications such as accounts receivables, finance, marketing and sales analysis etc., DHL offers a highly automated and user friendly PC-based shipment processing system for on-site customer use. This system known as 'Easyship' automates the preparation of air bills, prints shipping labels, weighs packages and automatically calculates the proper rate based on weight and destination. Easyship also performs a number of other routine procedures such as storage and maintenance of mailing lists, location or departmental charge-back capabilities, report-to-diskette transfer for use in a customer's own applications and customer shipping history retention. Easyship is also available in more than half-a-dozen different languages.

DHL has exploited the developments in communications technology to develop its own DHLNET communications network. This provides a uniform, consistent and timely means of tracking and tracing customers' shipments from pick-up to final delivery. The 'Track and Trace' system allows the client to locate a package anywhere in the world at any point in time while it is in transit. Tracking and tracing a shipment begins with the couriers, who carry computerized handheld laser scanners. When a courier first picks up a document or package, basic information such as source, destination and billing date are entered into the scanner. This information forms a unique shipment record. As the shipment moves from the origin to its final destination, additional information is added to this record by the service centre, region, etc. DHLNET stores this information at a central network hub known as the global data centre. The information is then made available upon request to any DHL service centre worldwide, to provide immediate response to its customers regarding the status of their shipments.

Today DHL uses DHLNET to send shipment documents over computer networks directly to the customs facility in the destination country. This has enabled DHL to make sure that special handling requests such as translations, authorizations or contacting consignees are all taken care of before the shipments actually arrive. When the shipments arrive, the customs authorities need only to match the information with the correct shipment to clear it. DHLNET has reduced the time for customs clearance of air cargo, just as its air express service in 1969 reduced the time for customs clearance of seaborne cargo.

## The move to open systems

In the mid 1980s, DHL's business was growing very rapidly and management was concerned about the company's ability to meet its business objective of providing high quality service. Major concerns included the incompatible computer systems, insufficient computing power, and inefficient global communications.

## Incompatible computer systems

Existing computer support was not sufficient to transport computer applications across regions. For example, some of the core applications on finance, billing, customer support etc. developed on IBM System/36 in the UK were not running on the NCR machines in Africa. Rewriting the programmes to suit the NCR architecture meant duplication of effort. Neither was it feasible to replace NCR machines by IBM machines as IBM maintained a very low profile in the region (NCR was the dominant hardware supplier in Africa), IBM machines were very expensive and IBM technical support was minimal. As a result, DHL decided to 'standardize' its computer applications in order to ensure some portability across machines from different vendors in different regions.

## Insufficient computing power

DHL had a number of IBM System/36 and the capacity on these machines was nearing saturation. Upgrading System/36 to System/38 or AS400 meant accepting a new architecture completely different from System/36.

Also, as the business was growing, DHL found it needed to maintain a DBMS to support its operations efficiently. System/36 supported only 'flat files', and even the DBMS package available on System/38 was a proprietary product. If upgrading meant re-inventing the wheel, why not go to a 'standard' platform once and for all?

## Inefficient global communications

In the mid 1980s, South-east Asia and Far East Asia regions were using leased lines for communication. Europe had Geisco, while simple dial-up modems were used in the USA. This meant installing Geisco and dial-up modems in the Asian regions for establishing communication links to Europe and the USA, and installing dial-up modems in Europe for communications to the USA. Africa had no direct communication link with any region and all its requests were routed through the Geisco gateway in Europe. There was clearly scope to improve the communications links, especially given the developments in computers and communication technologies which offered improvements in efficiency and effectiveness. This prompted DHL to consider adopting ‘standards’ for global communication.

## The adoption of Unix

It was imperative that DHL standardize its IT applications across all regions in order to meet its business objective. The Unix operating system which offered open systems standards was available and it had already established its strong presence in the university campuses in the USA as a very powerful operating system. Senior management was convinced that Unix was the solution if DHL was to maintain its competitive edge in the world air express industry. The proven track record of DHL favoured the acceptance of Unix, standards even though Unix was a relatively new product. The management, supported by a team of experts on Unix, communication technology and DBMS applications, announced the decision to adopt Unix in 1986. There was an undercurrent of disbelief from IT professionals regarding the promises of Unix but top management had already made its decision. All computer applications had to be converted into Unix standards on Pyramid computer systems by the end of 1987.

The move towards open systems at DHL was a very conscious move, consistent with the organization's goal to continue providing excellent service to its customers. Even though the decision to adopt the Unix system was taken in 1986, it was only in 1989 when the vision of the 1986 decision was fully implemented.

Following the decision of the top management to adopt Unix standards, each region selected a Unix vendor based on the vendor's support capabilities in that region. DHL believed that an international organization like DHL could not and should not rely on a single vendor worldwide, as no single vendor could meet all the needs of users worldwide. This move led to the selection of Pyramid and IBM systems for operations in the USA and UK, HP systems in Europe and South America, NCR systems in Africa, and HP and Fujitsu systems in the Asia-Pacific region.

DHL has been able to lever technology innovations from the different vendors without being locked into a single proprietary supplier. By going open, the cost and speed of system development has improved as the open system environment has made it possible to port applications across computers in different regions. For example, one of the important applications at DHL, the 'Customer Service Module' which was first developed on an IBM PC in the USA, has now been ported onto almost all the computing platforms in all the regions. The open system also provided the flexibility to modify computer applications to suit any specific requirements of the individual regions. The standard applications have also had implications for human resources management. DHL is able to provide uniform training worldwide for the same set of applications and this improves the ability of staff to move from one location to another.

## Implementing Unix in the South-east Asia region

Singapore is the regional headquarters for DHL's South-east Asia region. South-east Asia is one of DHL's largest regions covering over 30 million square miles, eight time zones and more than 1.2 billion people from 28 countries (Table 2). The main markets include India, Singapore, Indonesia, Malaysia, Australia and Thailand. The region has over 300 service centres and 1300 employees handling almost 10 million shipments a year and accounting for approximately 7 per cent of the worldwide revenue.

Planning for an open system for the South-east Asia region started in 1989, when the DHL regional office in Singapore identified Hewlett-Packard as the best vendor in the region meeting the requirements. However, the process of moving towards open systems has been very slow and painful.

Moving towards an open system involved integrating different computer systems distributed across seven countries: Australia, Indonesia, Malaysia, New Zealand, Singapore, Thailand and India. All the computer applications had to be converted from System/36 and Omni systems to Unix on the HP platform (Table 3).

The regional management was very happy with the support from the System/36, and did not understand the need for a transition to an unknown platform. The IT professionals understood the complexity and the power of Unix but were concerned about its user hostile environment. With System/36, it was not necessary for the systems analysts to know the operating system in detail, but this was not the case with Unix. Transition from System/36 to Unix was a frightening prospect but it had to be done.

Table 2 Countries in the South-east Asia region

<table><tr><td>American Samoa</td><td>Nauru</td></tr><tr><td>Australia</td><td>Nepal</td></tr><tr><td>Bangladesh</td><td>New Caledonia</td></tr><tr><td>Bhutan</td><td>New Zealand</td></tr><tr><td>Brunei</td><td>Papua New Guinea</td></tr><tr><td>Cook Islands</td><td>Singapore</td></tr><tr><td>Fiji</td><td>Solomon Islands</td></tr><tr><td>India</td><td>Sri Lanka</td></tr><tr><td>Indonesia</td><td>Tahiti</td></tr><tr><td>Kiribati</td><td>Thailand</td></tr><tr><td>Laos</td><td>Tonga</td></tr><tr><td>Malaysia</td><td>Vanuatu</td></tr><tr><td>Maldives</td><td>Vietnam</td></tr><tr><td>Myanmar</td><td>Western Samoa</td></tr></table>

The transition process started with training programmes on Unix for the System/36 staff. These people had to learn Unix and at the same time manage the System/36 applications to meet customer needs. It turned out to be an impossible task as the architecture of Unix was very different from that of System/36.

Subsequently, a small group of System/36 staff was formed to master the fundamentals of Unix. This group was completely relieved of its responsibility of managing System/36. Over a period of time, the number of developments in System/36 declined and more System/36 staff accepted the transition to Unix.

The Unix experts brought from outside to run the training programmes found it difficult to interact with the System/36 staff. One of the reasons was that the System/36 staff knew the DHL operations very well, while the Unix experts had little relevant business knowledge. All the System/36 staff had considerable field experience and therefore understood the business operations very well. This was one of the reasons for the success of IT at DHL. The Unix team, on the other hand, was technically well qualified, but did not understand the DHL operations. This led to some serious concerns regarding the relevance of the software developments on Unix and their usefulness in supporting the DHL operations at a local level.

Table 3 Computer applications at DHL (South-east Asia region) before going 'open'

<table><tr><td rowspan="2">Country</td><td colspan="3">Details on DHL computer systems</td></tr><tr><td>Location</td><td>Computer system</td><td>Applications</td></tr><tr><td>Australia</td><td>Sydney</td><td>IBM System/36</td><td rowspan="5">Billing, accounts receivables,customer service,finance ground and airoperations, marketing and sales</td></tr><tr><td>Indonesia</td><td>Jakarta</td><td>IBM System/36</td></tr><tr><td>Malaysia</td><td>Kuala Lumpur</td><td>IBM System/36</td></tr><tr><td>New Zealand</td><td>Auckland</td><td>IBM System/36</td></tr><tr><td>Thailand</td><td>Bangkok</td><td>IBM System/36</td></tr><tr><td>Singapore</td><td>Singapore</td><td>IBM System/36</td><td>plus communications controlcentre</td></tr><tr><td rowspan="4">India</td><td>Bombay</td><td>Omni</td><td>Billing and finance</td></tr><tr><td>Calcutta</td><td>Omni</td><td>Billing and finance</td></tr><tr><td>Delhi</td><td>Omni</td><td>Billing and finance</td></tr><tr><td>Madras</td><td>Omni</td><td>Billing and finance</td></tr></table>

The Unix system developers faced another problem in that the local management was not happy with merely reproducing the System/36 functionality on Unix. The managers wanted significant enhancements from the transition. As a result, the Unix system developers took a very long time to develop successful applications and establish the superiority of these systems over the existing applications on System/36.

One of the first successful applications on the Unix platform was the implementation of Uniplex, an office automation package, on the NCR Tower. This took place in 1989 around the time that DHLNET was implemented. Singapore was chosen as one of the first eight sites to be on the DHLNET. E-mail capability was established on the NCR machine. The NCR machine was replaced shortly afterwards by an HP machine and the Uniplex software was ported onto the HP platform (by the Uniplex vendors) without much difficulty. This was followed by the successful porting of the communication software from the Pyramid in the USA onto the HP system in Singapore. Later on, the Customer Service Module was also ported from PC Scounix onto the HP platform. By late 1991, many applications were running under Unix, the most important application being the track and trace system which is currently available in six out of 28 countries in the South-east Asia region.

One of the reasons for the successful transition onto the Unix platform in Singapore was the management's philosophy of 'one box — one application'. There was a Unix box for communication infrastructure, another box for the Informix database, a third box for customer applications etc. This approach was justified as the Unix operating system allowed chaining all the applications at a later stage, unlike System/36. This approach provided a number of advantages. System development activities could take place in parallel. Investment in IT was distributed over time as a number of smaller boxes were purchased in sequence rather than one major purchase of a mainframe. It was possible to catch up with emerging technologies by buying state-of-the-art machines over a period of time. Finally the approach offered the option of transferring smaller machines to smaller countries in the region when upgrading the computer systems in bigger countries, thereby increasing the life span of investments in IT.

## Conclusion

The move towards an open system has been demanding, both in terms of management and technical effort. However, the success in introducing Unix and the business benefits achieved have been recognized by the award to DHL International (Singapore) Pte Ltd of the National IT award (Private Sector) organized by the National Computer Board, Singapore for outstanding achievements in the application of IT for competitive advantage (Appendix).

## Appendix

National IT Award for the Private Sector — DHL International (S) Pte Ltd

## A Citation

Aggressive exploitation of IT and commitment to quality service has distinguished DHL International (Singapore) as a company par excellence and the market leader in the air express industry. By investing in the latest state-of-the-art distribution and communication systems, DHL is able to gain advantage over its competitors by providing customized solutions to serve the distribution requirements of customers.

DHL's commitment to the exploitation of technology covers the entire scope of its operations, enabling the company to achieve continuous and significant improvement in service level and operational efficiency.

DHL leads in IT innovation and strategic applications. It is the first DHL office outside the United States to implement Easyship, a total customer service for mail and parcel delivery, installed at the customer's premises. It has also implemented the Memo Paging System, the first of its kind in the world that gives instructions to its couriers on the run. This system was developed locally and will be gradually adopted by DHL offices worldwide.

The company has achieved phenomenal growth in the industry, a growth that has been fuelled by its strategic investment in IT.
