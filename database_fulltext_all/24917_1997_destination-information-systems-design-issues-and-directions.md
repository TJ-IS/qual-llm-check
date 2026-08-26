---
otero_id: 24917
otero_key: "5DP9C6WE"
title: "Destination Information Systems: Design Issues and Directions"
authors: "Hong-Mel Chen; Pauline J. Sheldon"
year: "1997"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1997.11518169"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Destination Information Systems: Design Issues and Directions

Hong-Mel Chen & Pauline J. Sheldon

To cite this article: Hong-Mel Chen & Pauline J. Sheldon (1997) Destination Information Systems: Design Issues and Directions, Journal of Management Information Systems, 14:2, 151-176, DOI: 10.1080/07421222.1997.11518169

To link to this article: http://dx.doi.org/10.1080/07421222.1997.11518169

![](/api/attachments/5DP9C6WE/fulltext/images/dba994c6568ffb50e68cd09c783dcf9d307b7264e460fa3e203b43bb97302b49.jpg)

Published online: 08 Dec 2015.

![](/api/attachments/5DP9C6WE/fulltext/images/419ba98ee303e5113d26bad577e2e5eae2421f7822fb2604ceed9e3423ea6a07.jpg)

Submit your article to this journal ↗

![](/api/attachments/5DP9C6WE/fulltext/images/cb1c3f68ff8e0ea2d7c465affef94605d25d5968459a0cb6a43e3b02f310b9ab.jpg)

Article views: 4

![](/api/attachments/5DP9C6WE/fulltext/images/c1488c11d666afe747a72af23aeac516a5e5e127c45518923fd946e65d5ef1d7.jpg)

View related articles ↗

![](/api/attachments/5DP9C6WE/fulltext/images/fe8ea497331c80f8fd818bbee446b09e2acf863fba2a28bcf31bc629e8ce52f6.jpg)

Citing articles: 3 View citing articles ↗

# Destination Information Systems: Design Issues and Directions

HONG-MEI CHEN AND PAULINE J. SHELDON

HONG-MEI CHEN received her master's and Ph.D. in management information systems (with a minor in electrical and computer engineering) from the University of Arizona. She received her B.S. in business administration from National Taiwan University in Taipei. Dr. Chen is Assistant Professor of Decision Sciences in the College of Business Administration at the University of Hawaii, where she serves as the Director of the Advanced Information Management Solutions (AIMS) Laboratory. Her current research activities focus on the design and development of distributed multimedia database systems for health care, tourism, engineering, and marketing applications. She has been leading large-scale research projects involving Web-integrated data warehousing of electric vehicle time-series performance data as well as medical image communication via a NASA gigabit satellite-integrated optical fiber network. She is a member of the IEEE Computer Society, the Association of Information Systems, Association for Computing Machinery (ACM), ACM Special Interest Group on Management of Data and Special Interest Group on Business Information Technology.

PAULINE J. SHELDON is a Professor of Tourism at the School of Travel Industry Management, University of Hawaii. She has a Ph.D. in economics and management information systems from the University of Hawaii. She has published widely in tourism journals on tourism information systems, tourism demand modeling, and tourism as an academic discipline. She is the author of Tourism Information Technology. Dr. Sheldon serves on the editorial boards of Annals of Tourism Research, Journal of Travel Research, Tourism Economics, Journal of Travel and Tourism Marketing, Tourism Analysis, and Progress in Tourism and Hospitality Research. She has served on the Board of Directors of the Travel and Tourism Research Association, the Society of Travel and Tourism Educators, and the Hawaii Visitors Bureau. She and Jafar Jafari founded the international tourism researchers' electronic bulletin board called TRINET which has over 300 international subscribers. She is a member of Travel and Tourism Research Association, Society of Travel and Tourism Educators, Hospitality Information Technology Association, and the American Economic Association.

ABSTRACT: A destination information system (DIS) is defined as an interorganizational system (IOS) that provides travelers and travel counselors with easy access to comprehensive, timely and accurate information on a destination's facilities, and the option of making reservations. Its development requires extensive cooperation by competing tourism product suppliers and destination promoters in both the public and private sectors. This paper identifies challenges encountered in the design of a DIS such as: (1) comprehensive information content from multiple data sources, (2) multimedia data management, (3) interfacing with global electronic markets, and (4) resolving problems arising from different data formats and standards. Technical design options are examined to address these design challenges. A proposed system architecture, called VIDIS, integrating viable design options is then presented. The VIDIS architecture exploits current technological advances in heterogeneous distributed databases, intelligent multimedia communication, and global electronic commerce. Implementation strategies of a DIS that adapt to organizational changes and rapid technological advances are suggested. Finally, design tasks and related organizational issues are discussed.

KEY WORDS AND PHRASES: cooperative interorganizational systems, destination information systems, heterogeneous distributed databases, IS design issues, metadatabase, multimedia information management, strategic information systems, travel industry, tourism, virtual integration.

TOURISM IS NOW THE WORLD'S LARGEST INDUSTRY and it is still expanding. The World Tourism Organization expects it to employ one in nine people in the next decade and to generate \$4.3 trillion in revenue in the year 2000 [43]. The trends in world tourism supplies and demands have shifted considerably over the last decade. Increasing complexity and competition in the tourism industry as well as increasing diversity and sophistication of travelers have made destination information management a critical task for all the stakeholders. Travelers seek greater flexibility in their travel arrangements and expect more customization to match their individual tastes [37]. Special-interest travel to experience unique destinations requires that travelers and travel intermediaries have access to specialized destination information. Studies have shown that the provision of information to tourists affects their destination choice, their satisfaction, and their repeat visitation [14, 32]. Destinations, therefore, must provide easy access to comprehensive and timely destination information to remain competitive in this environment.

Destination information systems (DIS) are a relatively new application of information technology to assist in this task. A DIS is defined as a database system that contains comprehensive information about a destination's facilities and tourism products and is accessible by the travelers themselves or by travel planners, either in the destination or in the home region. A DIS is designed to facilitate travelers' and potential travelers' vacation planning, trip organization, and subsequent settlement of travel transactions $[15, 37]$ . A DIS may also provide reservations capabilities, a customer database, a market database, and statistical analysis capabilities $[36]$ . Because they require coordination of information from multiple sources, DIS are examples of interorganizational systems (IOSs) $[24]$ . The development of a DIS is motivated by the benefits an IOS can provide for its participants, including cost reduction and increased revenue resulting from the enlarged market scope, new customers, a larger product line, cross-selling, and the “halo effect,” which make customers more willing to deal with DIS sponsors $[6, 24]$ .

Unlike existing systems in the travel industry, a DIS aims to provide unbiased, comprehensive destination information, including public and private tourism products from both small and large companies. The successful implementation of a DIS not only increases market efficiency but also promotes market equity [36] for all information providers. DIS development, however, faces many unique technical challenges and organizational issues. DIS promoters (e.g., government agents) may not conceive of technical options, whereas information system designers are poorly prepared to deal with complex interorganizational issues in the tourism industry. This paper aims to bridge this gap.

We first define and position DIS within the tourism industry structure and distinguish its functionality from other tourism electronic market (EM) systems. We then identify key challenges in DIS design and development, discuss design alternatives, and present a system architecture that integrates viable design options. This discussion of design tasks and organizational issues, with strategies recommended for phased DIS implementation, will be of interest to tourism officials in national and state tourism offices wishing to represent their destination electronically. It should also be of interest to information system (IS) professionals of interorganizational or EM systems.

## Design Challenges and Requirements

## Destination Information Provision

TRADITIONALLY, TRAVELERS ACQUIRE DESTINATION INFORMATION through past experiences, advertisements, guidebooks, brochures, and videos from tourism suppliers, tourist offices, and travel agents, and by word of mouth. It is time-consuming and expensive to obtain this information, which is often incomplete and outdated, leading to suboptimal tourist satisfaction with the planning process and perhaps with the trip. Zealous competition and shrinking margins in the travel industry have prompted the use of more EM systems [36]. EM systems are IOS that automate and support information exchange on price and product offering, and negotiation and settlement of market transactions among consumers, intermediaries, and suppliers. Such EM systems use information and communication technology to facilitate the creation, storage, processing, and transmission of information across organizational boundaries.

Many EM systems assist the distribution of information on travel products. Figure 1 provides a schematic view of electronic tourism markets, built on the basic structure of tourism distribution channels presented by Buhalis [9]. The first EM systems implemented in the tourism industry were airline reservation systems—computer reservation systems (CRS). When these systems were made available to retail travel agents in the mid-1970s, they became the major distribution channels for a wide range of travel products, and became known as global distribution systems (GDS). The major GDS are SABRE, GALILEO/APOLLO, SYSTEMONE/AMADEUS, WORLDSPAN, and ABACUS. These immense systems are now the main electronic distribution channels available to travel intermediaries. They not only provide flight information on the host airlines, but, through travel industry networks (SITA, ARINC and direct access links) and switches or gateways (Ultraswitch and Wizcom), they allow connection to other airline systems, hotel reservation systems, car rental reservation systems, cruise reservation systems, and other travel products. Independent databases are also accessible through most of the GDS, such as TravelFile, and the Official Airline Guide (OAG).

Consumer access to GDS is now possible through online networks such as America On-Line, Compuserve, Prodigy, and the Internet. EaasySabre is one example; although more user-friendly, it lacks the comprehensiveness of travel agent or airline access to the databases. Destinations can present information on their facilities, activities, events, and border controls on the GDS for a fee. Apollo's Travel Guide, an example of this, lists detailed information on over thirty major tourist-receiving countries. A burgeoning number of travel products, from hotel chains to travel agencies to destination information, are now accessible on the World Wide Web (WWW). Tourism offices with home pages often create links to the independent suppliers in the destination. Consumers then have access to a more comprehensive electronic destination search than previously known. Travel agencies online are now writing interfaces to the major GDS so that consumers can forward information and booking requests to them directly. An additional electronic media used for destination information distribution is Videotex, widely used in Europe and Asia.

Few of the current EM systems mentioned above provide comprehensive information on a specific destination. GDS favor airlines and larger travel suppliers or destinations that can afford the substantial listing fees. They also tend to list high-priced, homogenous products, and thus create an upwardly skewed impression of the destinations $[37]$ , leaving many destination facilities with no electronic access to the markets. Piecemeal destination information available via Web pages comes closest but does not ensure full representation by all suppliers. These individual destination home pages on the WWW often are not connected with any DIS databases. Most provide only hypertext-based static descriptions of a destination or a particular tourism product. Many home pages of different hotel chains must be accessed in order to compare different hotel prices in a destination unless easy links are created. Small tourism suppliers may not have the technical and financial resources to maintain a Web server, severely affecting the information quality and comprehensiveness and thereby hindering market efficiency and equity.

The balance of this paper shows how a destination can design and implement a DIS that connects with global networks, such as WWW, to address the aforementioned problems.

## Objectives and Design Challenges

DIS development has been spurred by both demand and supply factors. Initially, DIS were developed by national, state, and city tourist offices to handle large volumes of travelers' inquiries, particularly to include information on small and medium-size tourist suppliers not listed on other EMs. For other cases reported in the literature, tourism offices and tourism product suppliers considered DIS an effective tool for marketing and managing a destination $[37]$ . Government tourism offices are usually responsible for harnessing the financial resources for its creation.

![](/api/attachments/5DP9C6WE/fulltext/images/1ee2051913c7323b71569decda298f3befc7fb7b3a13c0c2ab18cee2ffbe39da.jpg)  
Figure 1. Electronic Markets in Tourism

A DIS is expected to store a diversity of destination information, such as attractions, events, entertainment, transportation, restaurants, and accommodations, as well as demographic, statistical, ecological, and geographical information. Several intended characteristics that distinguish a DIS from other tourism EM systems are listed below, although many DIS in operation today are still in their infancy:

1. Users. To serve the destination information processing and promotion needs. Destination information must be accessed by multiple users: by the traveling public, travel intermediaries, and destination promotion agencies, as well as by travel product suppliers. This means that a DIS has to interface with global networks serving a geographically dispersed range of users.

2. Information content. To provide unbiased, correct, timely, and comprehensive information on the wide range of tourism products in a destination, both business and leisure, supplied by both public and private sectors regardless of company size and product price range. This may be needed in a multimedia, multilingual context. The cooperation required from competing tourism products has organizational and economic implications for DIS design.

3. System functions. To facilitate all phases of a tourism market transaction, from information gathering (both before and during a trip) to transaction settlement; eventually to facilitate travel counseling and marketing research activities of tourism offices. This is in contrast to the more specialized functions for which GDS were designed [12].

The best way to achieve these objectives rests in the design of the DIS. The interorganizational nature of DIS, however, and the characteristics of tourism products pose many design challenges. Based on travel industry literature, we identify four design challenges (DC1–DC4) concerning the information input, processing and output aspects of a DIS design:

## DC1. Comprehensive Information Input from Diverse Data Sources

The quality of the data is critical to the success of the DIS. Information quality refers to the following aspects of data: accuracy, precision, comprehensiveness (freedom from bias, nonexclusionary), currency, timeliness, content, understandability, and readability. If data are found to be false or misleading, the entire DIS could lose its credibility. “Any inaccuracy is greeted by an unrecoverable drop in confidence and usage” [44].

DIS information content and quality depend on cooperation among possibly competitive tourism suppliers from both the private and the public sector. Large travel suppliers already represented on other EMs may not want to see their smaller competitors receiving equal access to markets. This raises many organizational issues (e.g., leadership) and economic issues (e.g., listing cost) as well as technical issues for implementing data standards and data quality control measures. Most DIS are administered by public-sector agencies in the specific nation or region and offer free or inexpensive listings to ensure comprehensiveness (see examples in Table 1). When a DIS includes a reservations feature, it is typical to charge the supplier for each booking received. The inclusion of the reservation feature increases the design complexity, since inventories and availability must be updated online. When more system features are included in a DIS, the cost of transaction processing will often incur a fee.

Data standards are important on two levels. On a syntactical level, for example, a DIS needs to enforce standard formats for data collected from multiple sources. On a semantic level, there are issues of standardization of the product information itself. For example, are the properties of a “suite” in Hotel A the same as in Hotel B? Enforcement of semantic standards is very difficult and is often augmented by consulting “standards” input from other agencies such as the Chamber of Commerce or the regional hotel association. Responsibility for data standards enforcement and data validation lies either totally with the individual suppliers or with the database administration team. In the latter case, DIS managers often accomplish validation by sending suppliers standard questionnaires to complete with their product information. This requires them to abide by standards for data type and display format. In some systems, the National Tourism Office (NTO) staff collect the data, whereas in other systems the responsibility is placed on the supplier. The latter option is less expensive but can yield misleading information. Destination information can be divided into static and dynamic categories. For dynamic information (e.g., times, schedules, availabilities), one would want automated real-time data entry and update methods embedded in the DIS. Although some systems provide online direct access, most existing DIS still use manual, offline data entry and update methods such as diskettes, phone, answering machines, fax, and mail.

## DC2. Online Retrieval of Multimedia Data

The time-specific nature of the industry and other characteristics of tourism products have implications for storage, transmission, and online retrieval of multimedia data. Most tourism products such as hotel room-nights and airline seat-miles are perishable products, making online capability a desirable function of a DIS. Furthermore, information on most tourism products is best conveyed using multimedia (audio, video, images, and text) making them more tangible to the consumers. Attractions, cultural events, and accommodation environments are examples of products with a high need for multimedia [1]. A multimedia DIS provides a richness in data types that facilitates flexibility in expressing destination information. This improves the DIS user interfaces and facilitates public acceptance and usage. The recent popularity of the Internet browsers (2D and 3D), burgeoning multimedia commercials on the WWW, and CD-ROMs on destinations have raised public expectation for multimedia information [4]. Accomplishing the storage, transmission, and online retrieval (search or navigation) of multimedia data, however, is not a trivial undertaking.

Many DIS implementations utilize relational database technology and deal primarily with alphanumeric data and a few scanned images. Existing multimedia and hypermedia systems $[1, 17, 44]$ are implemented as stand-alone systems. Current multimedia storage of destination information is limited to read-only, static archival medium and thus does not allow frequent updates. This is expected to change, with the new wave of accelerated multimedia technology and its decreasing costs. Because of the rapid development of the information superhighway, multimedia destination information can now be transmitted to homes in numerous ways. It can be transmitted through the WWW and through ISDN networks as they become more available. It can also be transmitted via cable TV and online service networks. Many systems are considering the use of public access terminals (PAT) in shopping centers, airports, and other public areas, and recognize the need for user-friendly, multimedia technology.

## DC3. Interfacing with Global EM Systems

To effectively reach potential customers and for economies of scale, a DIS needs to interface with global EM systems such as the GDS $[36]$ . The interfacing of DIS with external EM systems is not merely a technical problem but also involves many organizational issues. This requires the public tourism offices to be responsible for negotiation with global EM systems and to be knowledgeable of the regulatory and political environment in which these communication networks are created. National systems have a stronger negotiating power while regional systems that do not represent the entire country's tourism industry are less attractive for interfacing with global EM systems. Some DIS already interface with international or national EM systems, such as Videotex and GDS databases. The DIS designed by the Irish, Dutch, and Finnish tourism offices are all accessible through various Videotex systems. Videotex interfaces are either manual or through a primitive gateway for data transmission. Users, however, are still required to deal with multiple query languages and data formats. It is critical to provide better “integration” of the DIS with other EM systems in order to take advantage of international distribution channels.

## DC4. Resolving Data Heterogeneity

Some DIS face problems of data heterogeneity as a result of the many data models and access languages used by different companies in the industry. DIS typically operate in a distributed environment $[13]$ . Large destinations often have stand-alone DIS, each with a narrower destination scope (e.g., a city or county) implemented on an ad-hoc basis. Other stand-alone DIS may only store selected attractions or products such as car rentals or accommodations. Table 1 shows some examples of these. The information exchange between and among these component databases and regional DISs is difficult and raises the cost for tourists to search and obtain destination information. An important design challenge, therefore, is how to integrate the existing stand-alone legacy databases.

The integration design is constrained by many factors. Some of these are financial sources, the nature of tourism in the area (whether trips are typically multidestinational or unidestinational, individual or group tour, whether air, rail, or automobile is the major mode of travel), and whether travel is predominantly international or domestic. In countries where regional DIS are created, the need for interconnectivity increases in response to the demand for nonlocal information by tourists. In Austria and Switzerland, the development of DIS has been at the regional level. A regionally networked system is a natural “next step” in a country that has previously had only regional systems. Travelers need transparent access to such participating regional DIS that are implemented on a variety of hardware and software platforms without encountering a multiplicity of data models and query languages. Data heterogeneity at the access level (e.g., data model and query languages) has not yet been dealt with by existing systems. Centralized national systems may not have to address data heterogeneity issues within their systems. In Denmark, for example, where tourism is centrally organized at the national level, the DIS (DANDATA) is a centralized system. A network of visitor information offices throughout Denmark and in major foreign markets can access the database in Copenhagen online. The Gulliver system in Ireland is a similarly centralized DIS.

The requirements suggested by the above four design challenges can be summed up as the following design criteria: (1) information quality, (2) operational efficiency, (3) ease of access and use, (4) flexibility for incremental growth, and (5) scalability and extensibility of the system. The interrelationship among the design challenges, design options, and design requirements (criteria) are depicted in figure 2. The technical design options for addressing each design challenge are discussed in the next section.

## Integrated Management of Destination Information

COMMON UNDERSTANDING OF THE TECHNICAL DESIGN OPTIONS is expected to help formulate technology strategy and facilitate the cooperation among key players in DIS development (e.g., planning, analysis, design, and implementation). Research has shown that a key aspect of technology strategy is a clear system architecture. Technical building blocks necessary for DIS are identified to form a system architecture for facilitating DIS development.

## Design Options

Our discussion of design options is organized around each design challenge. The design options for addressing each design challenge look beyond the current technology, thereby suggesting future directions for existing DIS development. Some technologies can be used to address one or more design challenges and one design alternative does not always exclude the others.

## DC1. Comprehensive Information Input from Diverse Data Sources

Most current implementations manually enforce data standards and data quality control on data from multiple data sources. The following alternatives can replace the manual process to reduce operational errors and increase efficiency.

Table 1. Examples of DIS (1992–94) in Europe and Their System Features Corresponding to the Design Challenges (DC)

<table><tr><td></td><td>Features</td><td>DANDATA</td><td>GULLIVER</td><td>NBTIS</td><td>TIS</td><td>APPENZELL</td></tr><tr><td rowspan="3">Back-ground</td><td>Country</td><td>Denmark</td><td>Ireland</td><td>Netherlands</td><td>Austria</td><td>Switzerland</td></tr><tr><td>Financial sources</td><td>National tourism office (NTO)</td><td>NTO and EEC grant</td><td>NTO</td><td>NTO</td><td>Private sector</td></tr><tr><td>System topology</td><td>National</td><td>National</td><td>Networked regional</td><td>regional (Tyrol)</td><td>Regional (Appen-zellerland)</td></tr><tr><td rowspan="6">DC1</td><td>System admin.</td><td>NTO</td><td>NTO</td><td>NTO</td><td>Regional tourism office</td><td>Local tourism office</td></tr><tr><td>Cost to travel product supplier</td><td>Free</td><td>Annual subscription</td><td>Free</td><td>Free</td><td>Commission per booking</td></tr><tr><td>Product data entry</td><td>Supplier generated</td><td>NTO data collection</td><td>NTO data collection</td><td>Supplier generated</td><td>Supplier generated</td></tr><tr><td>Information content (travel products)</td><td>Comprehensive (private + public)</td><td>Comprehensive</td><td>Comprehensive</td><td>Comprehensive</td><td>Private sector only</td></tr><tr><td>Update methods</td><td>Diskettes and online upload</td><td>FAX and phone</td><td>Diskettes, phone, fax</td><td>Fax, phone, mail</td><td>Phone</td></tr><tr><td>Database</td><td>Relational database</td><td>Relational database</td><td>Relational database</td><td>Relational database</td><td>Videotex software</td></tr><tr><td rowspan="2">DC2</td><td>Public access</td><td>None</td><td>Future public access terminals (PAT)</td><td>Future PAT</td><td>PAT</td><td>PAT</td></tr><tr><td>Multimedia</td><td>Future</td><td>Future</td><td>Future</td><td>Future</td><td>Not considered</td></tr><tr><td>DC3</td><td>Interfaced systems (upload, online gateway)</td><td>Direct link or switch</td><td>French &amp; British videotex</td><td>French videotex</td><td>Weather systems</td><td>Swiss &amp; German videotex</td></tr><tr><td>DC4</td><td>Integration</td><td>N/A</td><td>N/A</td><td>Future</td><td>Future</td><td>Future</td></tr></table>

1. EDI (electronic data interchange) technology is the standards-based computer-to-computer exchange of intercompany business documents and information. As the network tendrils offered by the Internet and other online services reach out to the smallest entities, small companies can grow online and thus the use of EDI technology will become feasible for DIS. EDIFACT (EDI for administration, commerce, and transport) is a public standard developed jointly by the United Nations; ANSI and is a standard message protocol being used in tourism applications in Europe. Another similar protocol is ANSI X12. The standard can be proprietary—developed by companies large enough to impose standards on their trading partners. This has happened in the case of the GDS that use the unique ALC (Airline Line Control)

![](/api/attachments/5DP9C6WE/fulltext/images/91ce9c99a82c0ca6c216d19b1505f007661c2aa05fbcf9eb5b4fc5149fe3d0d5.jpg)  
Figure 2. DIS Design Challenges, Requirements & Alternatives

protocol. There are also many online EDI clearinghouses that translate data from one standard to another, sparing individual companies from having to program their computers with standards used by their trading partners. Although EDI standards facilitate the moving of data, this does not remove the need for negotiation and data validation for DIS.

2. The database approach traditionally enforces data standards in an organization. With small companies online, database "forms" (a programmed electronic form to allow users to edit, insert, and delete data items from a database) built upon a DIS can be accessed by the tourism product suppliers. Access authorization and data validation functions can be built into the database program that is connected to the Web. Questionnaires for surveying tourism product suppliers can also be incorporated as a database application within a DIS. Centralized systems can more easily impose data standards on DIS input format and output display than can networked regional systems.

3. Database federation using gateway technology is a third approach whereby automatic links are built between a DIS and the databases of tourism suppliers. Changes in product inventory can be captured immediately to maintain the timeliness of the data content. This approach will only be feasible with bigger product suppliers. Therefore, it should be used with the first two design alternatives for smaller suppliers.

## DC2: Multimedia Data Management

Multimedia information storage and retrieval can be achieved through attribute-based, full-text-based, and content-based approaches. For image management (still or motion video), a multimodal approach that utilizes a combination of the following approaches is suitable for DIS when the technology is available and proven. For performance consideration, distributed parallel query mechanisms with knowledge-based augmentation can complement each of these approaches $[8]$ .

1. In current practice, conventional retrieval methods for alphanumeric data are extended for image retrieval. Attribute-based retrieval utilizes a relational approach that treats an image as a BLOB (Binary Large Object) and uses an image identifier and related attributes to describe and retrieve images. The relational approach is efficient but falls short in providing flexibility, particularly when user queries contain attributes that are not predefined in the databases. Most database management systems (DBMS) support attribute-based retrieval of images.

2. A full-text approach is used for text retrieval. Commercial full-text DBMS, such as Folio, BasisPlus, Oracle Book, are available. Some DIS are based on these approaches, such as the one developed by the Hawaii Visitors Bureau. This approach is also used for multimedia object retrieval: The retrieval of images is mediated via the retrieval of full-text description (in natural language or keywords) of images. Instead of free full-text descriptions, various models and techniques in the information retrieval (IR) research field have been proposed to allow the use of application semantics and user feedback to build keywords, a thesaurus, and automatic indexing. These models achieve greater efficiency $[10, 34]$ .

3. Although the IR-based approach can offer much flexibility in query formulation, it is still difficult to enumerate all possible descriptions of some tourism products. Content-based retrieval is critical to empower users to store and retrieve image data with the same flexibility as traditional database applications for alphanumeric data. In a content-based approach, features of images are analyzed and extracted, and image retrieval is then based on the similarity between the query image objects and the stored image objects. Content-based retrieval is still being studied with artificial intelligence (AI) and neural network (NN) techniques $[8, 40, 47]$ . This requires sophisticated multimedia storage, communication, and display facilities. The current capabilities are far from ideal, but commercial support for content-based retrieval has already been announced, such as IBM's Query by Image Content (QBIC) $[22]$ . DIS should prepare to take advantage of this capability.

## DC3: Interfacing with Global EM Systems

There are three alternatives for DIS to interface with external global EM systems, thereby meeting the requirement of operational efficiency.

1. EDIFACT is a standard used by DIS for accomplishing transactions with other EM systems. GDS have their own standard and provide their own interfacing software and hardware to subscribers. Some emerging EDI technologies promise to bring features such as digital signatures (verified by anyone in any place without the need for identification), digital cash that can move anonymously without forgery, and digital time-stamps that can provide incontrovertible proof that a document existed at a certain time. Car rental companies are already using digital signatures for their contracts. The use of such technology over the Internet promises many opportunities for DIS transaction settlement if reservations are a feature of the DIS.

2. Many companies are now utilizing the Internet to accomplish EDI functions. Platform-independent languages (e.g., Java) and tools for Web-based development have proliferated in the past year. The standardized Web browser interface also makes the development cost for such connection less than traditional EDI development.

3. The proliferation of online information has made it impossible for an average user to cope with the large number of command languages, operational modes, communication protocols, or seamless access to information/reservation services. Some gateways connecting together the different travel sector databases already exist. Ultraswitch and Wizcom are two examples—the former focusing on the connection between accommodation databases and GDS, the latter on connections between smaller travel companies and GDS. More of these will be needed in the future to connect the DIS of numerous countries. Functions such as making reservations can be implemented as precompiled remote procedure calls. Some existing programmable gateways can be custom-designed for this purpose. Many DIS are developing gateways that can potentially become a software product offering to other DIS.

## DC4: Resolving Data Heterogeneity

To meet the requirements of operational efficiency and ease of use, data heterogeneity must be handled in both syntactical and semantic levels to allow users transparent access to heterogeneous databases. We discuss three methods (in addition to gateway technology being the “interface” solution for resolving data heterogeneity encountered by noncentralized DIS).

1. The problem of formally representing the full range of tourism information is considerable. Setting a single standard is controversial when coupled with rapidly changing technology and greater use of networking, as well as investments in time and software. Nevertheless, it is desirable that an international tourism body be set up to promote tourism product standards. That body can work with existing systems while encouraging the evolution of information interchange in an “open systems” context [35]. Specifications of how to exchange the information should be published and made widely available. Industry-wide standard setting, however, will not resolve data heterogeneity, even though it facilitates it.

2. The second alternative, consolidated database integration, is to integrate multiple DIS by designing and developing a new system from scratch. The design can be either centralized or homogeneously distributed $[7]$ . It can be physically dispersed over a computer network, appearing to the user as a centralized database. Because either design offers an integrated view of data in the system and provides one single data model and one single query language, data standards can automatically be enforced. With strong leadership, this approach could be very effective but would be difficult where the investment in legacy systems is substantial. In this alternative, only the distributed design can offer the required extensibility by adding a heterogeneous database management component when the DIS needs to expand to incorporate other heterogeneous databases.

3. Virtual database integration, the third alternative, is a bottom-up virtual integration approach $[20, 28, 31, 39]$ . This approach allows heterogeneity among different databases while hiding it from the users. This is particularly appropriate if a destination has several local and regional DIS and travel databases that need to be integrated. These existing databases are called local databases; the existing database structure and definition according to the local DBMS data model are called a local schema. This approach involves designing a unified global schema from all the local schemata and then defining the translation functions between the global schema and the local schemata (see figure 3). The translation is done at both semantic and syntactical levels and utilizes knowledge about how data are used. The global schema, the mapping functions, and the data usage knowledge are stored in a metadatabase $[21]$ . A single high-level query language can then be provided for all users. All database operations and user query processing to the integrated database are then mediated through the global schema and knowledge contained in the metadatabase. As such, the differences in DBMS, query languages, and data models among databases will be hidden from users; in addition, conflicts in data semantics among local databases will be resolved while each local database maintains its autonomy.

The most important advantage of virtual integration for DIS is that it can easily incorporate additional databases (centralized or homogeneously distributed) as new databases are developed or the scope of the DIS is extended. This meets the scalability and extensibility requirement. Virtual integration also offers flexibility for each local database to determine the sharable part of each local database by means of export and import schema. (This is called database federation [18].) The export schema specifies the information that a database will share with other databases, while the import schema specifies the nonlocal information that a database will share with other databases.

## Proposed VIDIS System Architecture

The proposed Virtually Integrated DIS (VIDIS) architecture (figure 3) is designed as a framework for DIS development based on the design considerations discussed above. The architecture integrates the appropriate design alternatives for each of the four design challenges while exploiting rapid advancements in information technology. The architecture clearly specifies necessary functions required for a DIS and discusses how each component interfaces with each other. Specifically, the VIDIS architecture adopts the use of database functions (forms and data validation programs) for enforcing standards on data from multiple sources, the virtual database integration approach for transparent access to heterogeneous databases, the multimodal (poly-paradigmatic) approach [8] for flexible multimedia information management, and finally gateway technology for interfacing with large tourism product suppliers and external EM systems. The DIS database is designed to be connected to a Web server to exploit “Internet commerce.” The recent rapid development of database tools for easy connection with Web servers makes such connection a must for future DIS development.

The unique characteristics of the VIDIS design lies in the incorporation of a metadatabase that provides integrated management of both database system catalogue and knowledge bases necessary for intelligent interpretation and retrieval of heterogeneous multimedia data. It also includes a heterogeneous distributed database management system (HDBMS) that incorporates the necessary software modules to handle multimodal query processing, database transaction management, and communication interfaces. The graphical user interface (GUI) supports multilingual translation and hypertext-based navigation of multimedia destination information, so important for tourism applications. A gateway subsystem is included for managing online updates of tourism products and online access to airline CRS and other EM systems. Smaller tourism product suppliers can update product information via database forms.

## Graphical User Interface (GUI) Subsystem

The graphical user interface resides in the public access terminals, whether they are public access kiosks in the destination or PC terminals accessing the DIS in the tourism office, or Web pages. An interactive relational query language, natural language-based

Downloaded by [Newcastle University] at 06:10 30 March 2016

Figure 3. Open Distributed VIDIS System Architecture
Figure 3. Open Distributed VIDIS System Architecture

TPDB: Tourism Product Database
LDB: Local Database
LDM: Local Data Manager

GDS: Global Distribution Systems
CRS: Computer Reservation Systems
EMS: Electronic Market Systems

![](/api/attachments/5DP9C6WE/fulltext/images/35fb7bcf3985b2594a4c0f972f99fc2819b4b805fc0fbd8a850cbbf1a2689ee6.jpg)

as well as a pictorial query language, will be used for different types of database queries (e.g., relational, full-text, or content-based retrievals). Flexible image-viewing capabilities such as zooming and image browsing will be included to view destination information such as maps, buildings, or museums. Hypertext navigation, for example, will allow users to zoom into a city map and be linked to the hotels and restaurants. In addition, the following knowledge-based modules can be added to increase the flexibility and intelligence of the system:

\- Multilingual manager: This module allows users to select a language for interaction and handles translations among multiple human languages, particularly appropriate for destinations with a high proportion of foreign visitors.

\- Dialogue manager: This module conducts dialogues with users to clarify ambiguous information requests and assist users in system usage. Tutorials and help facilities are available.

\- Multimodal query manager: This module maintains concepts, key words, and a thesaurus in the metadatabase to assist users in formulating multimodal database queries. It also manages an image processing toolset for content-based retrieval.

\- Hypertext navigator: This module uses automated expertise and the knowledge of destination experts to assist tourists in acquiring environmental information about a destination.

## Metadata

The metadatabase stores the following data and knowledge to facilitate intelligent access and manipulation of heterogeneous multimedia destination information:

\- Knowledge about local databases and operations: This module includes knowledge about the global schema, the local schemata, and interschema properties. It also includes the global to local mapping definition, access methods and patterns of query/transaction activities to allow query processing, such as quick search and access to local data. Information such as usage statistics, protection, and access authorization are also stored to maintain data security and integrity.

\- Tourism industry domain knowledge and destination expert knowledge: This module uses the hypertext navigator to assist users in formulating destination database queries and to facilitate fast environmental learning for different travel purposes.

\- Thesaurus: This contains natural-language rules for resolving data semantics conflicts among local databases and to facilitate natural-language user queries.

\- Image feature catalogue: This module stores preprocessed image objects to facilitate content-based retrieval by matching stored objects with requested objects presented by the user.

\- User profiles: Traveler profiles are set up to anticipate the sequence of user interaction with the VIDIS and, for example, to intelligently suggest different travel itineraries.

## Heterogeneous Distributed Database Management System

The HDBMS encompasses query processors for handling different media and different types of queries from public users, while hiding the data heterogeneity and distribution from the users. It manages complicated distributed operation problems for the users, including distributed query processing, distributed concurrency/recovery control, global resources management, distributed security control, schema translation, and mapping. In addition, the HDBMS supports additional language features for full-text-based or content-based image information retrieval. The HDBMS employs an image processing toolset that contains software for feature extraction, and symbolic coding, and a knowledge inference engine, which provides reasoning and searching capabilities to perform tasks in image object understanding and fast retrieval of destination information. In addition, the following modules are included:

\- Multimodal query processor: This module decomposes and translates a user request for destination information into subtransactions for local DIS via communication with local data managers (LDM) and a specialized medium handler for each medium type. It also performs all relevant Input/Output operations and then integrates the results of the subtransactions for the user. This involves query decomposition, optimization, query language translation and schema translation. Three query processors would be necessary: a pictorial SQL query processor for relational pictorial query, an IR query processor for full-text processing, and a content search processor for content-based graphical object retrieval.

\- Transaction manager: This module performs and ensures distributed concurrency control and distributed recovery functions. Distributed concurrency control avoids nonserializable executions, determines any conflicts of a transaction with another, and deals with the serialization order of transactions and deadlock solutions. The distributed recovery control mechanism also ensures database integrity in the presence of hardware, software, communication, and storage media failure.

\- Communication manager: This module handles the data format and transfer functions according to the underlying multimedia communication protocols. It oversees gateway and router activities.

\- Local data manager: Each LDM is responsible for executing individual subtransactions for each component database. It contains a local DBMS with a distributed parallel query processor, a file manager that manages storage spaces, and a migration manager that moves multimedia data up or down within a storage hierarchy of magnetic, optical, and tape media.

## Gateway Subsystem

A gateway subsystem is important for a DIS that wishes to connect to users, travel intermediaries, the tourist industry, and suppliers around the world. The gateway subsystem includes both inward and outward gateway interfaces. An inward gateway interfaces with tourism product databases (TPDB) for online updates of destination information as well as streamlined booking of multivendor products in a destination, such as hotels and entertainment box offices. An outward gateway provides uniform access from each terminal to external EM systems, such as airline and hotel computer reservation systems and Videotex databases. The interface is achieved by using a common data manipulation language and precompiled remote procedure calls to interact with external databases. The provision of a common command/query language greatly simplifies reservation and payment functions and allows efficient access to accurate product description. By this gateway approach, new connections to additional TPDB or EM systems can be easily added when needed. The data validation and semantic conflict resolution will be performed by the query processors in the HDBMS using the knowledge stored in the Metadatabase. The services rendered include: (1) remote booking, (2) booking confirmation, and (3) remote ticketing and payments. Commands can be sent in either text format or multimedia data types. The modules in a gateway include:

\- Gateway front end: The front end manages the dialogue with multiple terminals, receiving commands from and sending results to the line.

\- Translator: For the outward gateway, this module will translate a command (or a sequence of commands) in the global query language for the specific remote service (one-to-many or 1-M translation). The results obtained are then processed and formatted following a standard definition of a local database. For the inward gateway, this module will translate a command (or a sequence of commands) in one of the many command languages from various TPDBs to the global query language for accessing the local database (many-to-one or M–I translation). Although the one-to-many or many-to-one translators are logically separable, they can be implemented in one physical gateway.

\- Communication manager: This module manages the dialogue with a specific remote service and hides all the different communication links.

## Design Issues

THE VIDIS ARCHITECTURE ALLOWS FOR THE MODULAR DEVELOPMENT of each system component. Each can range from a “poor man” alternative to a “rich man” alternative. This is significant because a DIS is often implemented incrementally with many players involved. The design and implementation of each module in the VIDIS architecture can be so complex that we recommend its design capitalize on commercial products in order to be cost-effective. Designers are then left to concentrate on the design of destination information contents and formats, virtual database integration, metadatabase design, as well as evaluation and selection of various technology for accomplishing VIDIS functions.

Designers may find traditional database design methodology inadequate since multimedia information content as well as interorganizational issues must be addressed. In particular, the establishment of data standards, the planning for virtual integration design, and gateway design all entail substantial cooperation and commitment from product suppliers and negotiation among various players. Currently, none of the DIS in operation uses VIDIS architecture. There have, however, been attempts by travel companies to create integrated reservations and decision support systems. One endeavor created by a consortium of travel companies (Hilton, Marriott, AMR, and Budget Rent A Car) called “Confirm” was abandoned in 1993 after \$125 million and three and a half years of work [16]. Although the “Confirm” system integration effort tackled different challenges from those of the DIS development, and was not destination-specific, it teaches us is that system integration is not an easy undertaking and takes careful planning, technical competency, and strong leadership to succeed. The design issues examined here and strategies suggested based on the VIDIS architecture are intended to help mitigate problems that could arise in the integration process.

In the following, we describe VIDIS integration design tasks that integrate analysis and modeling for various modules in the architecture and then recommend phased implementation strategy. The organizational issues are discussed last.

## Core Virtual Integration Design Tasks

The critical tasks for virtual integration design based on the VIDIS architecture include selection of a metadata model, integration modeling and the metadatabase design, and implementation. The addition of multimedia data to the VIDIS design significantly increases the complexity. Based on the VIDIS architecture, it is clear that the selection of a metadata model must consider representing both data and knowledge (to be stored in the metadatabase) to allow virtual integration of heterogeneous databases and efficient (knowledge-based) retrieval of multimedia data. Specifically, the metadata model must support (1) effective conceptual representation of the temporal and spatial relationships of destination information; (2) representation of operational, contextual, and usage knowledge; (3) neutral accommodation of heterogeneous data views that permit easy schema integration of heterogeneous databases; (4) transformation from conceptual level to logical level to physical level so that multimedia data can be easily stored, indexed, searched, and retrieved; (5) attribute-based, text-based, and content-based information retrieval; and (6) unified representation of the multimedia data and knowledge and automatic image object classification and indexing.

After a metadata model is selected, the integration modeling proceeds. The task focuses on designing a global schema that mediates heterogeneous multimedia database operations. Three steps are in order: schema analysis, schema integration, and mapping definition. The VIDIS architecture suggests an integrated process (for both knowledge and data) of schema analysis.

\- Schema analysis: The first step consists of a comprehensive analysis of the schemata of the participating (local) databases of destination information. All the data and knowledge sources (e.g., documents, databases, experts) will be identified and the semantic constructs in local schemata and data integrity constraints will be examined. The analysis may include schema designs for an existing file-based system. Application domain knowledge will be structurally and algorithmically acquired by means of metadata modeling. For facilitating content-based image retrieval, the symbolic descriptions of images that are meaningful or relevant to user queries will be identified and constructed automatically. This description includes the identity and structure of objects and their spatial relationships. In this step, the integrated modeling of common application knowledge (rules, facts, or data) will have the advantages of reducing duplicated modeling efforts and increasing metadata management efficiency.

\- Schema integration: The schema integration process includes (1) schema translation—component schemata of various data models are translated into the metadata model; (2) conflict resolution—local schemata are compared to detect differences in the semantic constructs such as naming conflicts (synonyms and homonyms), structural differences, differences in abstraction and scale differences (e.g., currencies, measurement difference); and (3) merging and restructuring—once differences are detected and resolved, the various transformed schemata can be merged and restructured to form a global schema with desired qualities. Detailed methodology can be found in [10, 28, 31].

\- Mapping definition: While the schema integration process stresses the unification of semantic information, the mapping definition aims at providing users with information processing efficiency. Mapping is the reverse of the schema integration process in that schema translation from one component schema in a global data model to a corresponding schema in a local data model and vice versa is defined. The mapping definition includes information needed for integration to facilitate query processing, such as interschema properties that express how data in distinct component schemata are interrelated [31].

Finally, the design of the VIDIS metadatabase involves the integrated modeling of metadata and metaknowledge into the global schema, mapping definition, integrity constraints, thesaurus, image feature catalogue, and user profiles (see figure 3). Integrated modeling will simplify the interface between the database (of schemata) and the knowledge-base in the metadatabase. Developments in adding deductive mechanisms (logic-based) to database management (relational) show promise for integration implementation [25, 29, 30]. It is hoped that research and development in metadatabase management systems (MDBMS) [21] will lead to easier construction of the metadatabase component for VIDIS.

Many gateway design tasks are similar to virtual integration tasks, including data analysis, data format translation, and confirmation to a common query language, but in a controlled interface context. We expect collective efforts from the tourism industry to induce more commercial development of specialized gateways and a central comprehensive gateway for international services. More commercially developed gateways for tourism applications will shorten the development time of a VIDIS and meet the major goal of a DIS—universal access to comprehensive information on a tourist destination.

## Phased Implementation Strategy

We suggest a progressive strategy for the DIS implementation, from a minimal DIS to an intelligent DIS, using the VIDIS architecture as a development framework. A database administrator (DBA) team would be responsible for maintaining as well as overseeing the functions of the VIDIS. The position would typically reside in the national tourist office, but might be distributed, depending on the organizational and economic structure of the participating entities of the VIDIS. The DBA would govern the entry of new products into the VIDIS and the creation of new links to EM systems. The DBA would also manage the growth and expansion of the VIDIS.

1. Minimal DIS: Equipped with data quality control modules, online information retrieval utilizing attributed-based retrieval of destination information formats (text, still images). Usage would be primarily by travel counselors in visitor information offices.

2. Functional DIS: Minimal DIS enhanced with a gateway subsystem. This would set the stage for public access use and for connection with the hundreds of thousands of travel agents connected to GDS terminals. Videotex gateways would also permit in-home searching of the DIS. The connection of a DIS to a Web server is a critical task here.

3. Hypermedia DIS: Functional DIS augmented with GUI allowing a hypermedia navigation of destination information content and full-text information retrieval capability. At this level of development, more sophisticated user terminals in the destination would be appropriate.

4. Intelligent DIS: Hypermedia DIS augmented with full multimodal retrieval capability implemented in a parallel computing environment (so that associative search of images can be speeded up). Pictorial query-by-example can be offered. User profiles will be added and used not only for travel packaging but also for market research.

Our strategy ensures information quality while incrementally increasing system capabilities. Such planned growth and expansion of the VIDIS depend upon technological issues, such as the technology that is already in place and the availability of new technologies. More important, it requires a strong vision and a quality management process to upgrade information technology continuously in a timely manner for competitive advantages $[3]$ . This requires the consideration of organizational issues, particularly in the government tourism office that will house the system.

## Organizational Issues

To implement a DIS, strong leadership is needed to secure cooperation from the various players in a destination. Such leadership will ideally come from within the public tourism office and will be backed up with a substantial IS department within that organization. The IS department should house the DBA who will oversee the development and maintenance of the system. Leadership is not only needed to secure cooperation but also to obtain the necessary funds through lobbying and other actions. In addition to the development costs, maintenance of information in the DIS for currency and accuracy requires substantial resources that must be accounted for in the budgeting process. Strong leadership will also facilitate the determination of the “common goals” of the system. To accomplish this, it is recommended that representatives from the national tourism office, state and local tourism offices, and owners of any existing proprietary systems form a committee to define strategies, guidelines, and procedures for the integration efforts.

On the technical side, the leadership must direct preintegration planning such as deciding on integration priorities and order for the VIDIS design $[28]$ . Top management support is also required to ensure end-user involvement in the modeling of data semantics. In fact, electronic data interchange or virtual integration issues are often regarded as strategic rather than technical issues $[42]$ . Leadership issues also include ensuring information comprehensiveness and enforcing data standards and negotiating with external EM systems.

Another organizational issue is the examination of the costs and benefits of the system. Most IOS literature offers “benefit-induced” cooperation by analyzing the cost and benefits for each stakeholder. The success of information systems in creating a competitive advantage has prompted researchers to study IS impacts not only on firm performance but also on industry structure $[2, 11, 24]$ . On the firm level, financial measures can be used to quantify the improvement of process efficiency. At the industry level, it is harder to measure impacts. Economies of scale and scope and market concentration are possible measures, but further work is needed $[2]$ . However, benefit measures for DIS should be at both the “industry” level and the firm level because of its “cooperative” nature. One DIS developer, the director of Edinburgh Tourism Office in Scotland, expects that a development cost of approximately 800,000 in the system will result in an increase in travel revenues to the region of 7 million $[41]$ .

## Conclusion

THE DEVELOPMENT OF A DIS IS CRITICAL IF A DESTINATION is to remain competitive in the increasingly complex international tourism market. A DIS aims at not only providing high-quality and timely destination information to attract destination customers—both business and leisure—but also assisting them in all phases of tourism transactions, including pretrip planning, travel transaction settlement, and in-trip environmental learning. Adopting the VIDIS strategic approach should promote market efficiency and benefit all the actors in electronic marketplaces.

Even though DIS development is high on many governments' agenda, the design and implementation of a DIS is a very new experience for all. This paper suggests a VIDIS system architecture to address most effectively the many design challenges faced in their design and implementation. The architectural design exploits technologies in distributed databases, multimedia storage and communication, as well as artificial intelligence. Its modular design serves as a strategic plan for phased development of a DIS, allowing for smooth technological upgrading. Both technical and organizational issues for realizing VIDIS are discussed. Most important, the successful implementation of VIDIS requires the cooperation and coordination of all actors in a destination and calls for strong leadership, ideally created from both the private and the public sector in a destination. The architecture will help build “common goals” among key players through understanding of design issues. It is hoped that this will eventually lead to higher levels of tourism industry performance and thus competitive advantages for the destination.

## REFERENCES

1. Austin, W.J., et al. Processing travel queries in a multimedia information system. Proceedings of the International Conference on Information and Communications Technologies in Tourism, 1994, pp. 64–71.

2. Bakos, J.Y. Dependent variables for the study of firm and industry-level impacts on information technology. Proceedings of the Eighth International Conference on Information Systems, December 1987, pp. 10–23.

3. Bakos, J.Y., and Treacy, M.E. Information technology and corporate strategy: a research perspective. MIS Quarterly (June 1986), 107–119.

4. Batini, C.; Lenzerini, M.; and Navathe, S.B. A comparative analysis of methodologies for database schema integration. ACM Computer Surveys, 18, 4 (December 1986), 323–364.

5. Berce, J., et al. Tourism promotion needs multimedia information system. Proceedings of the International Conference Technologies in Tourism, 1995, pp. 260–267.

6. Cash, J.I., and Konsynski, B. IS redraw competitive boundaries. Harvard Business Review, 63, 2 (March–April 1985), 134–142.

7. Ceri, S., and Pelagatti, G. Distributed Databases: Principles and Systems. New York: McGraw-Hill, 1984.

8. Chen Garcia, H.-M., and Yun, D.Y.Y. Intelligent distributed medical image management. SPIE Medical Imaging (February 26–March 2, 1995), 154–165.

9. Buhalis, D. Regional integrated computer information reservation management systems and tourism distribution channels. Proceedings of the International Conference, Technologies in Tourism, January 18–20, 1995, pp. 53–64.

10. Chua, T.-S.; Pung, H.-K.; Lu, G.-J.; and Jong, H.-S. A concept-based image retrieval system. Proceedings of 27th Hawaiian International Conference on System Sciences, January 4–6, 1994, pp. 590–598.

11. Clemons, E.K., and Kimbrough, S.O. Information systems, telecommunications, and their effects on industrial organization. Proceedings of the Seventh International Conference on Information Systems, December 1985, pp. 45–56.

12. Copeland, D.G., and McKenney, J.L. Airline reservation systems: lessons from history. MIS Quarterly, 12, 3 (September 1988), 353–370.

13. Czap, H. Improving service in the field of tourism by open distributed processing. Proceedings of the International Conference on Information and Communications Technologies in Tourism, 1994, pp. 214–220.

14. Guy, B.S.; Curtis, W.W.; and Crotts, J.C. Environmental learning of first-time travelers. Annals of Tourism Research, 17 (1987), 419–431.

15. Haines, P. Destination marketing systems. Proceedings of the International Conference on Information and Communications Technologies in Tourism, 1994, pp. 50–55.

16. Halper, M. Outsourcer confirms demise of reservation coalition plan. Computer Weekly (1993).

17. Hardman, L. Evaluating the usability of the Glasgow Online Hypertext. Hypermedia, 1 (1989), 34–63.

18. Heimbigner, D., and McLeod, D. A federated architecture for information management.

ACM TOIS, 3, 3 (July 1987), 253–278.

19. Hruschka, H., and Mazanec J. Computer-assisted travel counseling. Annals of Tourism Research, 17 (1990), 208–227.

20. Hsiao, D.K., and Kamel, M.N. Heterogeneous databases: proliferations, issues, and solutions. IEEE Transactions on Knowledge and Data Engineering, 1, 1 (March 1989), 45–62.

21. Hsu, C.; Bouziane, M.; Rattner, L.; and Yee, L. Information resources management in heterogeneous, distributed environments: a metadatabase approach. IEEE Transactions on Software Engineering, 17, 6 (June 1991), 604–624.

22. IBM wants to soup up image finding. Business Week (November 28, 1994), 149.

23. Ives, B., and Learmonth, G.P. The information system as a competitive weapon. Communication of the ACM, 27, 12 (December 1984), 1193–1201.

24. Johnston, R.H., and Vitale, M.R. Creating competitive advantage with interorganizational information systems. MIS Quarterly (June 1988), 153–165.

25. Kellogg, C. From data management to knowledge management. IEEE Computer (January 1986), 75–84.

26. Lella, G., and Lo Reto, G. Integrating tourism services via gateways. Proceedings of the International Conference on Information and Communications Technologies in Tourism, 1994, pp. 209–213.

27. Litwin, W.; Mark, L.; and Roussopoulos, N. Interoperability of multiple autonomous databases. ACM Computing Surveys, 22, 3 (September 1990), 293–303.

28. Liu Sheng, O.R., and Chen Garcia, H.-M. Information management in hospitals: an integrated approach. IEEE Proceedings of International Phoenix Conference on Computers and Communications, March 21–23, 1990, pp. 296–303.

29. Mark, L., and Roussopoulos, N. Metadata management. IEEE Computer (December 1986), 26–36.

30. Missikoff, M., and Wiederhold, G. Towards a unified approach for expert and database systems. Expert Database Systems (1986), 383–399.

31. Motro, A. Superviews: virtual integration of multiple databases. IEEE Transactions on Software Engineering, 13, 7 (July 1987), 785–798.

32. Perdue, R.R. Segmenting state travel information inquiries by timing of the destination decision and previous experience. Journal of Travel Research, 26, 4 (1985), 2–6.

33. Porter, M.E., and Millar, V.E. How information gives you competitive advantage. Harvard Business Review (July–August 1985), 149–160.

34. Salton, G. Automatic Text Processing: The Transformation, Analysis and Retrieval of Information by Computer. Reading, MA: Addison-Wesley, 1989.

35. Sawyer, D, et al. Standards: a view from the office of standards and technology. Science Information Systems Newsletter, 13 (August 1994), 22–26.

36. Schmid, B. Electronic markets in tourism. Proceedings of the International Conference on Information and Communications Technologies in Tourism, 1994, pp. 1–8.

37. Sheldon, P.J. Destination information systems. Annals of Tourism Research, 20 (1993), 633–649.

38. Sheth, A.P., and Larson, J. Federated databases systems for managing distributed, heterogeneous, and autonomous databases. Computing Survey, 22, 3 (September 1990), 183–237.

39. Smith, J.M., et al. Multibase: integrating heterogeneous distributed database systems. Proceedings of the National Computer Conference, June 1986, pp. 487–499.

40. Smoliar, S.W., and Zhang, H. Content-based video indexing and retrieval. IEEE Multimedia, 1, 2 (Summer 1994), 62–72.

41. Stafford, R. Destination heaven. Presentation at the International Conference on Information and Communications Technologies in Tourism, January 19, 1995.

42. Swatman, P.M.C., and Swatman, P.A. Integration EDI into the organization's systems: a model of the stages of integration. Proceedings of the 20th International Conference on Information Systems, December 16–18, 1991, pp. 141–152.

43. The Travel Industry World Yearbook, vol. 37, 1994.

44. Tsalgatidou, A.; Spiliopoulou, M.; Apostolaki, K.; Roussou, I.; and Hatzopoulos, M. A hypermedia tourist guide. Proceedings of the International Conference on Information and Communications Technologies in Tourism, 1994, pp. 72–92.

45. Wayne, N. Hi-Line: a case study of a working computerized central reservation office in the public sector tourism. Proceedings of the Information Technology in Public Tourism Offices, 1991.

46. Wiseman, C. Strategic Information Systems. Homewood, IL: Richard D. Irwin, 1988.

47. Yoshitaka, A., ed. Knowledge-assisted content-based retrieval for multimedia databases. IEEE Multimedia, 1, 4 (Winter 1994), 12–21.
