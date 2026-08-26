---
otero_id: 5418
otero_key: "4EM9QK8P"
title: "Marketplace and technology standards for B2B e-commerce: progress, challenges, and the state of the art"
authors: "Conan C. Albrecht; Douglas L. Dean; James V. Hansen"
year: "2005"
journal: "Information & Management"
doi: "10.1016/j.im.2004.09.003"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Marketplace and technology standards for B2B e-commerce: progress, challenges, and the state of the art

Conan C. Albrecht <sup>\*</sup>, Douglas L. Dean, James V. Hansen

Marriott School of Management and Rollins Center for e-business, Brigham Young University, 513 TNRB, Provo, UT 84602, USA

Received 12 February 2003; received in revised form 19 January 2004; accepted 25 September 2004 Available online 17 May 2005

## Abstract

We have examined standards required for successful e-commerce (EC) architectures and evaluated the strengths and limitations of current systems that have been developed to support EC. We find that there is an unfilled need for systems that can reliably locate buyers and sellers in electronic marketplaces and also facilitate automated transactions. The notion of a ubiquitous network where loosely coupled buyers and sellers can reliably find each other in real time, evaluate products, negotiate prices, and conduct transactions is not adequately supported by current systems. These findings were based on an analysis of mainline EC architectures: EDI, company Websites, B2B hubs, e-Procurement systems, and Web Services. Limitations of each architecture were identified. Particular attention was given to the strengths and weaknesses of the Web Services architecture, since it may overcome some limitations of the other approaches. C 2004 Elsevier B V All rights resel

Keywords: B2B e-commerce; Standards; Procurement; EDI; Web Services; Technology adapters; e-Procurement; Electronic markets; B2B hubs

## 1. Introduction

For more than three decades, businesses have been using electronic mechanisms to exchange transaction data. Standards have played an integral role in the success of some e-commerce architectures. Here, we propose and discuss a set of standards required in any

EC platform. We also evaluate past and current architectures against these standards.

The development and implementation of standards and technologies have accelerated over the past 15 years. A seminal event in this evolution was the development of electronic data interchange (EDI), whereby trading partners established standard formats for the exchange of electronic documents to facilitate electronic transactions [45]. Today, the emerging set of technologies referred to collectively as Web Services has the potential to extend the reach of EC.

Web Services offers many advantages not found in earlier technologies, but the technology has yet to realize its potential because of the lack of standards. The development and adoption of these could allow Web Services to meet the needs of a broader range of EC transactions, including B2C, B2B, C2C, and peerto-peer (P2P) transactions.

This study focuses on B2B transactions. Although there are different definitions of EC [33,39], it is generally acknowledged that B2B accounts for the largest dollar volume of EC, with approximately US\$ 700 billion in transactions in 2001. The Gartner Group estimated that by 2005 all types of EC transactions will exceed US\$ 8.5 trillion, 90% of which will be B2B transactions [30]. Similarly, Jupiter Research estimated that the combination of B2B and B2C EC transactions will surpass US\$ 7 trillion by 2005 [21].

Some businesses have engaged in EDI for a number of years. This has occurred when one business transmitted computer-readable data transactions in a standard format to another business. EDI standards captured the same information that businesses have traditionally included in paper transaction documents. Yet EDI was designed to support business transactions between sets of known trading partners [36]; it did not facilitate discovery of new vendors—a significant limitation for firms that wished to extend their reach to new participants in a broader marketplace.

Subsequently, the World Wide Web has enabled businesses to share documents across a generalized, global network. In several ways, it facilitated EC: sellers have been able to publish company and product information via their Websites, and to some degree, search engines have allowed buyers to find and analyze this information. Yet such searches are not reliable because of the diverse systems and data presentations. Moreover, sellers on the WWW generally do not use industry-wide standard transaction templates for accessing product information and executing purchase transactions. This has limited the ability of automated services to find sellers and conduct automated transactions.

Notwithstanding these limitations, the evolution of EDI and the WWW, together with a new set of technologies, has the potential to provide a more robust and powerful platform for EC than exists today. If supported by appropriate EC-supporting standards, this platform could enable buyers and sellers to find each other more easily and exchange product and service information with more precision and reliability than today. This portends a ubiquitous generalized marketplace that will have attributes of EDI, the WWW, and other evolving EC technologies.

## 2. e-Commerce enabling standards

For purposes of evaluation, we propose eight ECenabling standards (Fig. 1). We evaluate current and past EC technologies based on these. They can be grouped into three areas: foundation technology standards, marketplace standards, and commerce services and applications.

## 2.1. Foundation technology standards

Foundation technology standards serve as building blocks for higher standards. Three are essential to reliable, predictable EC communication:

 Data standards. Participants must share a common definition.

 Schema expression languages (SEL). For example, in the eXtensible Markup Language (XML) SEL data is delimited with hierarchical tags [50], while in the comma separated values (CSV) [37] SEL, fields and records are delimited by commas and hard returns. SEL may be used by designers and entities that create standards to define data patterns. However, SEL are format definition languages, not definitions. For instance, XML does not provide a standard but gives some basic rules and conventions to assist in the creation of standards.

 Common communication methods define how data is transferred from one machine to another across a network; e.g. hypertext transfer protocol (HTTP), file transfer protocol (FTP), and Internet inter-orb protocol (IIOP).

## 2.2. Marketplace standards

Marketplace standards include product and service representation schemas, transaction templates, and business categories. While the creation and widespread adoption of useful standards for these would greatly improve EC efficiency, their definition and adoption is significantly more difficult. Powerful competing organizations sometimes promote competing standards [41,42]. In addition, the diverse needs of participants complicate the adoption of standards. Despite these complexities, defining the following three standards would significantly benefit EC systems:

![](/api/attachments/4EM9QK8P/fulltext/images/228b3ce78f2e7cf8803f76674c0e72ab4e2205894d72dfcce3a9793f40936eae.jpg)  
Fig. 1. Required standards for generalized, global e-business.

 Business categorization schemes allow discovery technologies to index participants by type and name. Examples of systems that categorize businesses include the North American Industry Classification System (NAICS) [32] and the United Nations Standard Products and Services Code (UNSPSC) [48]. While a business categorization system is difficult to create because of diverse industries, discovery services must rely on some type of categorization scheme. Moreover, many organizations must be listed in multiple categories.

 Product and service representation schemas allow businesses to describe attributes of the services they offer and the products they sell. Computer applications are impeded in their ability to find and evaluate sellers of specific products and services by inconsistencies in representations [29]. Schemas include field names, field definitions, and data types. For example, fish suppliers need to describe the types of fish they sell, whereas accounting firms need schemas to describe the accounting services they provide. Many industries buy and sell commodities that are well suited for standardized product description formats [15,16].

 Shared transaction templates group data fields into meaningful combinations for transactions. They allow developers of heterogeneous systems to write software to translate data to and from the standard transaction format. Because of this, buyers can exchange transactions with many sellers rather than have to write translation routines for each seller.

## 2.3. Commerce services and applications

Discovery services and transaction execution applications complete the EC architecture.

 Discovery technology includes market search mechanisms that index businesses by type and product offering. Discovery technologies are important when buyers or sellers are not known, when offerings need to be found and evaluated, and when markets are fragmented [4,5]. Their usefulness depends on: (1) whether or not network participants use standards and (2) whether or not a large proportion of participants choose to participate.

![](/api/attachments/4EM9QK8P/fulltext/images/48a865c90ec0949e5ebee9b7338edf884cde9f22b050d884031649920e3e1b6a.jpg)  
Fig. 2. e-Business architectures.

 Transaction execution technology (TET) supports transactions between buyers and sellers. Two categories are important. First, informational transactions help buyers and sellers evaluate organizations and products. They include transactions that access product features, cost, and availability. Second, consummation transactions relate to the actual consummation of purchases. These include transactions that buy, coordinate delivery, and remit payments. For the greatest benefit, TET should be well integration with internal organizational systems [10,22,31,38,43,46]. TET should support both ad hoc connections to potential or new trading partners and connections that support privately negotiated agreements between trading partners [23].

## 3. Current technologies: strengths and limitations

Fig. 2 illustrates connections between objects in EC technology platforms including EDI, Websites, B2B hubs, e-Procurement systems, and Web Services supporting B2B.

Table 1 summarizes the technologies and standards used by each architecture. Their strengths and weaknesses are shown in Table 2.

## 3.1. EDI

EDI was motivated by the need for standard transmission between trading partners. In particular, it reduced cost, delays, and errors inherent in the manual exchange of transaction documents. This effort was primarily driven by large entities, such as General Motors, Sears, and Kodak. EDI was also used by some large retailers like Wal-Mart to buy from wholesalers. EDI limited a company’s reach to only one trading partner at a time. Moreover, trading partnerships were limited to relationships supported by legal contracts that specified trading partner obligations.

EDI standards for data interchange initially evolved from early proprietary agreements between pairs of trading partners to industry-wide standards. Later, they evolved into comprehensive and flexible EDIFAC and ANSI X12 standards. They include data standard, transaction templates, and limited product and service representations.

Trading partnerships between two firms using EDI are well defined and generally stable. This stability means that EDI is used for automated replenishment and efficient supply chains [11,12,14]. EDI occurred over value-added networks (VANs), which served as the common communication method but were expensive, with an initial cost of about US\$ 250,000 for a mainframe installation and subsequent fees as high as US\$ 0.70 per transaction.

Table 1  
Summary of e-business Architectures

<table><tr><td>#</td><td>Standard</td><td>EDI</td><td>WWW</td><td>e-Procurement</td><td>B2B hubs</td><td>Web Services</td></tr><tr><td>8</td><td>Transaction execution</td><td>No standard</td><td>CGI forms</td><td>Proprietary</td><td>Proprietary</td><td>J2EE, .NET, others</td></tr><tr><td>7</td><td>Discovery</td><td>No standard</td><td>Search engines</td><td>Vendor catalog or third-party catalog</td><td>Proprietary</td><td>UDDI</td></tr><tr><td>6</td><td>Transaction templates</td><td>X12</td><td>No standard</td><td>Proprietary</td><td>Proprietary</td><td>No standard</td></tr><tr><td>5</td><td>Product/service representation</td><td>Moderate</td><td>No standard</td><td>Proprietary</td><td>Proprietary</td><td>WSDL</td></tr><tr><td>4</td><td>Business categorization</td><td>No standard</td><td>No standard</td><td>None</td><td>Proprietary</td><td>Several supported</td></tr><tr><td>3</td><td>Communication method</td><td>VAN</td><td>Standard HTTP</td><td>Standard HTTP</td><td>Proprietary</td><td>SOAP</td></tr><tr><td>2</td><td>Schema language</td><td>Tags, delimited text</td><td>HTML</td><td>Proprietary</td><td>Proprietary</td><td>XML</td></tr><tr><td>1</td><td>Data standard</td><td>X12</td><td>No standard</td><td>Proprietary</td><td>Proprietary</td><td>Limited, basic types</td></tr></table>

T<sub>a</sub>bl<sub>e</sub> 2 <sub>e</sub>-C<sub>ommerce</sub> <sub>p</sub>l<sub>a</sub>tf<sub>orm</sub> <sub>compar</sub>i<sub>son</sub>

<table><tr><td>Platform</td><td>Market reach by sellers</td><td>Entity that sets data and transaction standards</td><td>Rigor of data and transaction standards</td><td>Index mechanism for discovery services</td><td>Adequacy of index</td><td>Type of search client</td><td>Degree of support for machine-executable transaction services</td></tr><tr><td>EDI</td><td>Limited to EDI partners</td><td>Industry consortium</td><td>Good</td><td>None</td><td>Index is specific to company, and is not organized for external marketplace access</td><td>EDI software generates price and availability requests exclusively to EDI partners</td><td>Good</td></tr><tr><td>Company Website</td><td>Greater than EDI but hampered by lack of standards</td><td>Multi-company standards do not exist</td><td>Very poor</td><td>Search engines (e.g., Yahoo, Google, etc.)</td><td>Keyword-based indexing exists but there are no efficient business, business type, or product and service indexes</td><td>Browser</td><td>Low</td></tr><tr><td>B2B hub</td><td>Limited to entities connected to the hub</td><td>Hub developer; standards are not common to other hubs</td><td>Varies in quality by specific hub</td><td>Hub index</td><td>Some categorization by the hub; the hub creates and maintains the index</td><td>Hub-specific client enabled through browser</td><td>Good, but not loosely coupled</td></tr><tr><td>e-Procurement systems</td><td>Limited to e-Procurement partners</td><td>e-Procurement software provider</td><td>Quality varies for different e-Procurement systems</td><td>e-Procurement system</td><td>Categorized within the e-Procurement system; sellers maintain product catalogs</td><td>e-Procurement system client enabled through browser</td><td>Good, but not loosely coupled</td></tr><tr><td>Web Services with UDDI</td><td>Large companies who list themselves on UDDI</td><td>UDDI consortium</td><td>Data and transaction standards need further development</td><td>UDDI index</td><td>Multiple business category indexes; product category indexing; no indexing and comparisons for specific product and services</td><td>Browser</td><td>Low</td></tr></table>

The EDI telecommunications vehicle is currently changing from the VAN to the Internet. Indeed, some of the larger VANs now offer Internet services in addition to traditional connectivity methods. Some industry groups are also adopting XML as the language for communicating EDI transaction information via the Internet. There are relatively few actual implementations of XML thus far, but substantial growth is expected in the future [13].

The strength of EDI stems from its well-defined data and transaction standards. With these standards, EDI software has been able to provide transaction services that make it possible to execute viable commercial transactions between two firms. However, EDI has been limited because it is most often used by larger buyers [8,47] and does not scale easily to include new participants. It is also not designed to operate in efficient electronic markets where buyers search for products, prices, and related information from all sellers in a dynamic broader market.

## 3.2. Company Websites

Although an increasing number of companies have a presence on the Internet, Websites lack important standards for product and service representations, transaction templates, and field definitions used to provide information for specific products and services. Although improvements have been made in automation [19], page scraping is not practical for general application to the great diversity of products on the web [9]. Consequently, humans must participate in all stages of the search.

Search engines like Google and Inktomi provide discovery services but are limited by a lack of product and service schemas. The lack of reach is another problem for search engines; not all potential suppliers and Web pages are indexed [20].

Once a search engine locates a company that sells a desired product, human operators must search the site.

Then, operators either purchase products through shopping carts or call the seller to arrange terms.

## 3.3. B2B hubs

B2B hubs are electronic marketplaces that play the role of digital intermediaries [2,4]. Ideally, they facilitate product and information exchange and support product search, negotiation, contracting, and settlement. Recently, some EC analysts and B2B software developers expected that hubs would radically reduce purchasing costs and provide comparability across vendors. Hubs consolidate multiple suppliers’ product offerings and help buyers search for desired products. They also offer their own catalogs or links to the product catalogs of sellers, thereby providing indexing services [6]. This was expected to exert downward pressure on prices [23,25] and promised reduced automation costs. Ideally, each buyer and seller would incur only the cost of connecting to a hub. Once buyers and suppliers were connected to the hub, it would be the instrument through which data could be shared on products and services.

However, these lofty expectations did not materialize. Many hubs have failed, and those that have survived have struggled to achieve critical mass. The success of hubs depended on the number of buyers and sellers participating. No single hub has reached a level of participation to fully realize these effects. Instead, hubs connect buyers and sellers to only a portion of the market. Hubs seldom connect to other hubs and competition for subscribers has resulted in market fragmentation [51].

Second, some suppliers are reluctant to subject themselves to the price comparison possible in a hub. This is unattractive to sellers who charge lower prices for large, centralized buyers and higher prices for small, decentralized buyers.

A third problem is that some buyers, like Wal-Mart and Dell Computer, have established strategic sourcing and coordinated replenishment agreements with suppliers [11,26]. The buyers have already invested in automated EDI links to suppliers and do not see the need to participate in hubs. Also, some hubs focus on liquidity but many lack channel coordination ability; that is, they do not coordinate the production schedule of suppliers with that of buyers.

A fourth problem is in automation diversity: data and transaction standards are specific to a hub but are not universal across hubs. Companies have to pay to implement multiple translation pathways between their purchasing and sales databases and hubs, making it costly to connect to multiple hubs.

Such factors have put pressure on the hub industry: for example, Ariba and CommerceOne have failed to achieve profitability and large market reach.

## 3.4. e-Procurement systems

A number of organizations have recently adopted e-Procurement systems to purchase indirect materials for processes like operations, sales, maintenance, and administration [18,44]; e.g., office supplies, computer equipment, cleaning solvents, and office furniture. Such systems allow organizations to distribute purchasing decisions to people across the organization. Moreover, automated links to suppliers allow buyers to reduce the paperwork and overhead associated with the buying process and shorten the purchasing cycle. Only those vendors connected to a buyer’s e-Procurement system are visible to the buyer. The systems catalogs contain generalized product and service database fields rather than catalogs based on product and service specific to product types. A main limitation of e-Procurement systems is that they are closed and cannot support automated searches and comparisons across all vendors.

## 4. Web Services

This platform takes advantage of the ubiquity of the WWW by using, XML, and UDDI. Web Services use open standards and have been submitted to the World Wide Web Consortium (W3C) [49]. Web Services focus mainly on data type standards, schema expression languages, and common communication methods. While UDDI attempts to meet the needs in the middle layers (categorization, schemas, and transaction templates), it does not provide sufficient support. In order to meet all the requirements for a successful architecture, UDDI needs to be combined with other frameworks, such as RosettaNet [40], ebXML [17], Universal Business Language (UBL), or the Semantic Web.

## 4.1. Web Service components

The Web Services architecture involves the Web Services Description Language (WSDL), Simple Object Access Protocol (SOAP), and Universal Description, Discovery and Integration registry (UDDI) [7].

## 4.1.1. Web Services description language

WSDL specification provides a set of rules for defining XML schema. The WSDL specification is a machine-readable fingerprint that describes an automated service and its attributes and is loosely analogous to an interface or header file used to describe the interface and behavior of a module in a program. It was developed by Microsoft, Ariba, and IBM and has been submitted to the W3C. Client software can query services for their WSDL definition. If the client software is prepared to make use of the services, it can interact with them through specific calls to the services. WSDL defines XML definitions for basic data types, including specific common data types that correspond to specific data fields.

## 4.1.2. Simple Object Access Protocol

SOAP is responsible for transferring XMLencoded information from one computer to another. Because it uses HTTP, Web servers allow it to pass through firewalls with relative ease, though companies are currently exploring ways to maintain adequate security when using it [1]. SOAP also supports standard data types that can be used for requests made to services and provides asynchronous messaging and event notification to help the host and client programs communicate.

WSDL and SOAP are widely supported in many different languages. Implementation libraries exist in languages such as Java, .NET, Perl, Python, Visual Basic, etc. [34]. Together WSDL and SOAP provide the framework for the definition and execution of remote calls on services such as enterprise objects that can be used to both publish data and execute transactions. While both WSDL and SOAP support the use of standard data types, no standard exists for which standard data types will correspond to specific data fields used by different service APIs. Also, field names like ‘‘product code’’ or ‘‘product description’ have not been standardized.

Table 3  
Types of listings within UDDI

<table><tr><td>Type of listing</td><td>UDDI component</td><td>Description</td></tr><tr><td>Business information</td><td>White pages</td><td>Organizations list information about the organization such as name, address, and contact information</td></tr><tr><td>Business categories</td><td>Yellow pages</td><td>Organizations can list themselves by one or more business categorization schemes</td></tr><tr><td>Product and service categories</td><td>Yellow pages</td><td>Organizations can list categories of the products and services they offer. Organizations cannot list specific product instances within product categories</td></tr><tr><td>Service description listings</td><td>Green pages (tModels)</td><td>Organizations can describe automated services and interfaces for those transaction-supporting services that they provide. External organizations can use automation to access information on (1) the organization, and (2) the classes of products and services it offers</td></tr></table>

## 4.1.3. Universal description, discovery, and integration registry system

The UDDI registry provides a central location for registering and finding services within the Web Services architecture. Currently, public services created by IBM, Microsoft, SAP, and HP replicate registrations and provide redundant lookup services. Because of registration replication, participants need to register with only one registry to be included in all UDDI servers. Table 3 shows the components of the UDDI registry.

UDDI has been criticized because it relies too heavily on a centralized registry [3]. Moreover, it may take time to develop functioning public directories that could be used to conduct business [28]. While this technology appears to have potential [13,27], the lack of standards is a limitation.

## 4.2. Limitations of Web Services

While the Web Services architecture represents a step forward, limitations still exist for automated services. Table 4 lists those important here.

## 4.2.1. Business categorization is unreliable and variable

The UDDI registry is able to locate organizations that belong to specific business types; however, since organizations can register with a variety of categorization schemes, the UDDI registry does not support economical and reliable searching for all businesses of a given type. Searchers must query several different business categorization schemes to find businesses of a specific type.

Jewell and Chappell [24] have written the following about the anticipated limited market reach of the UDDI registry:

It’s probably not realistic to expect software to dynamically discover and use new businesses on the fly in the near future. Realistically, human analysts need to browse a UDDI portal that allows customized searches and queries to discover the businesses they are interested in working with. It’s more likely that software will contain the logic necessary to locate and integrate with Web Services for companies that have been predetermined. It’s also likely that businesses will set up private UDDI registries that they can share with their approved partners to facilitate B2B integration.

## 4.2.2. Product and service representations are nonexistent or inconsistent

Because of the UDDI yellow pages, the registry can help searchers find businesses that offer a given class of products or services, but it does not support automated searches for specific products or comparisons of products and prices across vendors. For example, with UDDI it is possible to find companies that manufacture TVs, but not find all vendors who sell high-definition, stereo, 27 in. color TVs. Moreover, it is not possible for an automated search client to collect the model numbers, prices, and features of all those offered by the registered manufacturers. WSDL definitions do not exist for categories of products and services that should have equivalent or similar descriptive fields. While some industries may standardize their WSDL signatures or use existing ones from the existing pool, formal involvement with the registry does not provide any incentive for participants to standardize or adopt standards defined by other organizations. This lack of standardization significantly impedes its usefulness [35].

Table 4 Web Services weaknesses

<table><tr><td>#</td><td>Standard</td><td>Web Services support</td><td>Comment</td></tr><tr><td>8</td><td>Transaction execution</td><td>J2EE, .NET, others</td><td>A variety of implementations would work if based upon appropriate standards</td></tr><tr><td>7</td><td>Discovery</td><td>UDDI</td><td>Indexing is limited because of the lack of standards in items 4, 5, and 6. The existence of such standards would support creation of superior indexes</td></tr><tr><td>6</td><td>Transaction templates</td><td>No standards</td><td>Implementations are variable and unreliable</td></tr><tr><td>5</td><td>Product/service representation</td><td>WSDL</td><td>Different tModels exist, so it is impossible for search agents to infer meaning without human guidance</td></tr><tr><td>4</td><td>Business categorization</td><td>Several supported</td><td>Implementations are variable and unreliable</td></tr><tr><td>3</td><td>Communication method</td><td>SOAP</td><td>SOAP is adequate</td></tr><tr><td>2</td><td>Schema language</td><td>XML</td><td>XML is an adequate schema language</td></tr><tr><td>1</td><td>Data standard</td><td>Basic types</td><td>The basic types are adequate</td></tr></table>

## 4.2.3. Transaction templates are nonexistent or inconsistent

While UDDI provides the tModel structure [UDDI Version 3], which can be used by many businesses, the structure allows any number of external schemes for categorization. Since any registered entity can define tModels, many different specifications for the same business or product will exist.

## 4.2.4. Discovery services are limited because of a lack of standards

There are important implications for deficiencies for both the seller and the searcher. Companies lack defined product and service representation schemas and transaction template definitions to guide the development of automated commerce support software. This hinders the development of automation for both sellers and buyers, because different sellers expose different automation interfaces.

Sellers’ lack of standards leads to problems on the client side: it is difficult to search and discover competing vendor services. Without common field names and transaction templates, search clients cannot be developed that effectively exploit these fields. Moreover, indexing services cannot use standard interfaces to collect product and service information across vendors. Because of this heterogeneity, clients must be programmed to interact with specific seller interfaces, making the network fragile and extremely difficult to maintain.

In summary, the Web Services architecture provides emerging standards and technologies for most areas, but it still has significant limitations.

## 5. Conclusion

This paper has presented evidence of the need for common or shared marketplace and technology standards through examining and contrasting the major platforms that have been developed to enable EC. We have found that no single technology provides a complete solution for all components of a standardized, loosely coupled marketplace. Each platform has strengths and weaknesses.

One author recently spoke with a senior executive at a large manufacturer about the possibility of EC with accurate, efficient, worldwide searches, connections, and business transactions using agent technologies. The executive was unenthusiastic about a truly efficient, platform because it would partially level the playing field for smaller and new competitors. This executive’s business had already set up efficient EDI connections with preferred buyers and sellers, just-intime agreements, and preferred pricing. This private EC network provided the company with a significant competitive advantage.

While the Web Services architecture is a technological step forward, the lack of required standards limits its usefulness and widespread adoption. The technology toolbox of today is sufficient to support EC, but the standards that must be developed are conceptual standards required for efficient technological implementation. In particular, a shared set of APIs should support representation definition from top-down industry consortiums as well as from bottom-up participants. It should enable a standard API for specific transactions and industries over time, while allowing for individual and changing needs.

## Acknowledgement

The Rollins Center for eBusiness at Brigham Young University helped fund this study.

## References

[1] C.C. Albrecht, How clean is the future of SOAP? Communications of the ACM 47(2), 2004, pp. 66–68.

[2] J.P. Bailey, J.Y. Bakos, An exploratory study of the emerging role of electronic intermediaries, International Journal of Electronic Commerce 1(3), 1997, pp. 7–20.

[3] M. Baker, UDDI v3 Announced; did anybody notice? O’Reilly Network Weblogs, 2002. http://www.oreillynet.com/pub/wlg/ 1680.

[4] J.Y. Bakos, Reducing buyer search costs: implications for electronic marketplaces, Management Science 43(12), 1997, pp. 1676–1692.

[5] J.Y. Bakos, The emerging role of electronic marketplaces on the Internet, Communications of the ACM 41(8), 1998, pp. 35– 42.

[6] J.P. Baron, M.J. Shaw, A.D. Bailey Jr., Web-based E-catalog systems in B2B procurement, Communications of the ACM 43(5), 2000, pp. 93–100.

[7] T. Bellwood, L. Cle´ment, D. Ehnebuske, A. Hately, M. Hondo, Y.L. Husband, K. Januszewski, S. Lee, B. McKee, J. Munter, C.V. Riegen, UDDI Version 3 Specifications Document, UDDI Working Group, 2002. http://www.uddi.org/pubs/uddi-v3.00- published-20020719.htm.

[8] F. Bergeron, L. Raymond, Managing EDI for corporate advantage: a longitudinal study, Information and Management 31, 1997, pp. 319–333.

[9] D. Bergmark, P. Phempoonpanich, S. Zhao, Scraping the ACM Digital Library, Forum 35(2), 2001, p. 7.

[10] V. Choudhury, Strategic choices in the development of inter organizational information systems, Information Systems Research 8(1), 1997, pp. 1–24.

[11] T.H.K. Clark, D.B. Stoddard, Interorganizational business process redesign: merging technological and process innova-

tion, Journal of Management Information Systems 13(2), 1996, pp. 9–28.

[12] E. Clemons, S. Reddi, M. Row, The impact of information technology on the organization of economic activity: the ‘‘move to the middle’’ hypothesis, Journal of Management Information Systems 10(2), 1993, pp. 9–35.

[13] F. Coyle, XML, Web Services and the Data Revolution, Addison-Wesley Professional, Boston, 2002.

[14] C.W. Crook, R.L. Kumar, Electronic data interchange: a multiindustry investigation using grounded theory, Information and Management 34, 1998, pp. 75–89.

[15] Q. Dai, R. Kauffman, B2B E-commerce revisited: leading perspectives on the key issues and research directions, Electronic Markets 12(2), 2002, pp. 67–83.

[16] J.M. de Figueiredo, Finding sustainable profitability in electronic commerce, Sloan Management Review 41(4), 2000, pp. 41–52.

[17] ebXML, ebXML Technical Architecture Specification, 2001. http://www.ebxml.org/specs/ebTA.pdf.

[18] B. Eichler, K. Evans, N. Parks, S. Alaniz, R. Roberts, B. McCarver, E-Procurement: A Guide to Buy-side Applications, Stephens, 1999 http://www.stephens.con/.

[19] D.W. Embley, D.M. Campbell, Y.S. Jiang, S.W. Liddle, Y. Ng, D. Quass, R.D. Smith, Conceptual-model-based data extraction from multiple-record web pages, Data and Knowledge Engineering 31(3), 1999, pp. 227–251.

[20] E. Glossbrenner, A. Glossbrenner, Search Engines for the World Wide Web: Visual QuickStart Guide, Peachpit Press, Berkeley, CA, 2001.

[21] V. Grover, J.T.C. Teng, E-Commerce and the information market, Communications of the ACM 44(4), 2001, pp. 79– 86.

[22] D.L. Iacovou, I. Benbasat, A.S. Dexter, Electronic data interchange and small organizations: adoption and impact of technology, Management Information Systems Quarterly 19(4), 1995, pp. 465–485.

[23] S.D. Jap, J.J. Mohr, Leveraging Internet technologies in B2B relationships, California Management Review 44(4), 2002, pp. 24–38.

[24] T. Jewell, D. Chappell, Java Web Services, O’Reilly Press, Cambridge, 2002.

[25] S. Kaplan, M. Sawhney, E-hubs: the new B2B marketplaces, Harvard Business Review 78(3), 2000, pp. 97–103.

[26] Kurt Salmon Associates, Efficient Consumer Response: Enhancing Consumer Value in the Grocery Industry, Food Marketing Institute, Washington, DC, 1993.

[27] A. Lawrence, Virtual Formations, Infoconomy, 2002 http:// www.infoconomy.com/pages/search/group67737.adp.

[28] S. Masood, UDDI: Better on the Inside, Infoconomy, 2002 http://www.infoconomy.com/pages/search/group60381.adp..

[29] A. McAfee, The Napsterization of B2B, Harvard Business Review 2000, pp. 2–3.

[30] T. McCall, Worldwide business-to-business Internet commerce to reach \$8.5 trillion in 2005. Gartner Group, 2001. http://www3.gartner.com/5-about/press-room/pr20010313a. html.

[31] T. Mukhopadhyay, S. Kekre, Strategic and operational benefits of electronic integration in B2B procurement processes, Management Science 48(10), 2002, pp. 1301–1313.

[32] NAICS, Complete Source of NAICS and SIC Information and Products, NAICS Association, 2002 http://www.naics.com/.

[33] E.W.T. Ngai, F.K.T. Wat, A literature review and classification of electronic commerce research, Information and Management 39(5), 2002, pp. 415–429.

[34] T. O’Reilly, Web Services Center, 2002. http://webservices.oreilly.com/.

[35] T. O’Reilly, Amazon Web Services API, 2002. http://www.oreillynet.com/cs/weblog/view/wlg/1707.

[36] R. Suomi, Inter-organizational information systems as company resources, Information and Management 15, 1988, pp. 105–112.

[37] J. Repici, Understanding the CSV File Format, Creativyst Docs, 2002. http://www.creativyst.com/Doc/Articles/CSV/ CSV01.htm.

[38] F.J. Riggins, T. Mukhopadhyay, Interdependent benefits from interorganizational systems, Journal of Management Information Systems 11(2), 1994, pp. 37–57.

[39] F.J. Riggins, H. Rhee, Toward a unified view of electronic commerce, Communications of the ACM 41(10), 1998, pp. 88–95.

[40] RosettaNet, RosettaNet Background Information, 2001. http:// www.rosettanet.org/background/.

[41] C. Shapiro, H. Varian, The art of standard wars, California Management Review 41(2), 1999, pp. 8–32.

[42] C. Shapiro, H.R. Varian, Information Rules, Harvard Business School Press, Boston, 1999.

[43] K. Srinivasan, S. Kekre, T. Mukhopadhyay, Impact of electronic data interchange technology on JIT shipments, Management Science 40(10), 1994, pp. 1291–1304.

[44] C. Subramaniam, M.J. Shaw, A study of the value and impact of B2B E-commerce: the case of web-based procurement, International Journal of Electronic Commerce 6(4), 2002, pp. 19–40.

[45] G. Truman, An empirical appraisal of EDI implementation strategies, International Journal of Electronic Commerce 2(4), 1998, pp. 43–70.

[46] G.E. Truman, Integration in electronic exchange environments, Journal of Management Information Systems 17(1), 2000, pp. 209–244.

[47] V.K. Tuunainen, Opportunities of effective integration of EDI for small businesses in the automotive industry, Information and Management 34, 1998, pp. 361–375.

[48] UNSPSC, United Nations Standard Products and Services Code, 2002. http://www.un-spsc.net/.

[49] W3C, Web Services Architecture Working Group, 2002. http:// www.w3.org/2002/ws/arch/.

[50] P. Walmsley, Definitive XML Schema, Prentice-Hall, 2001.

[51] R. Wise, D. Morrison, Beyond the exchange: the future of B2B, Harvard Business Review 78(6), 2000, pp. 86–96.

![](/api/attachments/4EM9QK8P/fulltext/images/24f0059d1d8e8d0350ca7c190aa272e5f640992936bc5cc707967a060c2adf16.jpg)

Conan C. Albrecht is an Assistant Professor and Rollins Fellow at the Marriott School of Management at Brigham Young University. He researches computer-related fraud detection, collaborative computing, peer-to-peer architectures, and network programming. He has developed three groupware systems to research group dynamics, and he is currently creating open source software to make fraud

detection within corporate systems more available to auditors and fraud detectives. His work has been published in Decision Support Systems, The Journal of Forensic Accounting, The Communications of the ACM, and Expert Systems with Applications.

![](/api/attachments/4EM9QK8P/fulltext/images/486748514dcd7d6b2bcf15aa80f86ba00beb9eb47fea8c8ed33b44ea57c01890.jpg)

Douglas L. Dean is an Associate Professor and David and Knight Fellow at the Marriott School of Management at Brigham Young University. He is also the research coordinator at the Rollins eBusiness Center at Brigham Young University. He received his Ph.D. in MIS from the University of Arizona in 1995. His research interests include electronic commerce technology and strategy, software

project management, requirements analysis, and collaborative tools and methods. His work has been published in Management Science, Journal of Management Information Systems, Data Base, Group Decision and Negotiation, Expert Systems with Applications, and IEEE Transactions on Systems, Man, and Cybernetics.

![](/api/attachments/4EM9QK8P/fulltext/images/150e6479c55cac70919fb222d3a86815493668820ad6aa7eceaa70a8b4b10526.jpg)

James V. Hansen is Glen Ardis Professor in the Information Systems Group of the Marriott School of Management at Brigham Young University. He received his Ph.D. from the University of Washington, Seattle. He serves on the editorial boards of IEEE Intelligent Systems, Information Systems Frontiers, and Intelligent Systems in Accounting, Finance and Management, and is listed

in Who’s Who in Science and Engineering. His research interests are in machine learning and agent-based systems, with recent publications appearing in Computers and Operations Research, Genetic Programming and Evolvable Machines, IEEE Transactions on Neural Networks, and Journal of Experimental and Theoretical Artificial Intelligence.
