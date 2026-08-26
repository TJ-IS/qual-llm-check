---
otero_id: 26243
otero_key: "XGS73Q33"
title: "Business-to-Business Electronic Commerce and Convergent Assembly Supply Chain Management"
authors: "Troy J. Strader; Fu-Ren Lin; Michael J. Shaw"
year: "1999"
journal: "Journal of Information Technology"
doi: "10.1177/026839629901400405"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Business-to-business electronic commerce and convergent assembly supply chain management

TROY J. STRADER

Department of Logistics, Operations and MIS, Iowa State University, Ames, IA 50011± 2063, USA

FU-REN LIN

Department of Information Management, National Sun Yat-sen University, Hsi-tze Wan, Kaohsiung, Taiwan, ROC

MICHAEL J. SHAW

Department of Business Administration and Beckman Institute for Advanced Science and Technology, University of Illinois at Urbana-Champaign, IL, USA.

Electronic commerce (e-commerce) can occur between a business and its customers, as well as between a business and its suppliers. To facilitate interorganizational e-commerce it is often necessary to share supply and demand information between supply chain partners. Based on our analysis of supply chains in several industries we identify the mechanisms (business processes) required for effective supply chain management. We also identify the information system components needed to support these mechanisms, show how the individual components can be integrated into an information infrastructure framework and identify some technologies currently available that can ® t within our proposed infrastructure. We illustrate the usefulness of our framework by simulating convergent assembly (commonly associated with motor vehicle and aerospace production) supply chain performance under various information-sharing strategies supported by our proposed infrastructure. We ® nd that inventory costs can be reduced while maintaining acceptable order ful® lment cycle times. This is true because information, which provides the basis for enhanced coordination and reduced uncertainty, can substitute for inventory.

## Introduction

Intense competition in most industries is forcing business organizations to search for ways to improve product quality, customer service and operating ef® - ciency to remain competitive. In the past, ideas from the Industrial Revolution pointed organizations to production and transportation ef® ciency as the best way to remain competitive. Most changes were made at the operational level within an organization. Organizations are now ® nding that ef® ciency alone is insuf® cient for maintaining competitiveness in today’ s business climate. \`The revolution of the 1990s is driven not by changes in production and transportation but by changes in coordination. Whenever people work together they must somehow communicate, make decisions, allocate resources and get products and services to the right place at the right time. Managers, clerks, salespeople, buyers, brokers, accountants ± in fact, almost everyone who works ± must perform coordination activities’ (Malone and Rockart, 1991, p. 128).

One example of an attempt to improve coordination and competitiveness is supply chain management (SCM). SCM expands the scope of the organization being managed beyond the enterprise level to include interorganizational relationships. Examples include improving coordination between suppliers and manufacturers, as well as between manufacturers and distributors. As improvements in information technology (IT) have enabled the costs of coordination to decrease (Malone et al., 1987), there has been a general movement towards organizing as partnerships between more specialized ® rms or business units. SCM is an important topic to study because it is an instance of these partnerships. The focus of this study, business-tobusiness electronic commerce (e-commerce), enables the separate organizations to share information and complete transactions using current IT.

Early research in this area focused on identifying the important issues for management of supply chain networks (SCNs) using relatively simple analysis and observation (Lee and Billington, 1992, 1993; Davis, 1993; Lee et al., 1993; Billington, 1994). One of the issues identi® ed in these studies is the importance of information sharing for managing supply chains. Recent research has focused on supply chain design, supply chain operation and information sharing in supply chains, using more complex analytical and multiagent computational simulation models (Bhaskaran, 1998; Swaminathan et al., 1998; D’ Amours et al., 1999; Gavirneni et al., 1999). Our research builds on these studies by using multiagent computational simulation to evaluate the impact of information sharing on supply chain operational performance.

This study addresses two questions. First, does IT exist for feasibly sharing information between supply chain partners? Second, what impact does ef® - cient information sharing have on supply chain management (SCM)? We investigate the impact of several characteristics of SCM in an environment of e-commerce. These include centralized, global business and management strategies (e.g. make-to-order. assembly-to-order and make-to-stock), on-line, realtime distributed information processing to the desktop, providing total supply chain information visibility and the ability to manage information not only within a company but across industries and enterprises (Kalakota and Whinston, 1996). Within an overall framework for studying e-commerce, our research is at the application level (e.g. SCM), enabled by the Information Superhighway, multimedia content and network publishing, messaging and information distribution and common business services infrastructures (Applegate et al., 1996).

Based on our analysis of supply chains in several industries we identify the mechanisms (business processes) required for effective SCM. We also identify the information system components needed to support these mechanisms, show how the individual components can be integrated into an information infrastructure framework and identify some technologies currently available that can ® t within our proposed infrastructure. We illustrate the usefulness of our framework by simulating convergent assembly (commonly associated with motor vehicle and aerospace production) supply chain performance under various information-sharing strategies supported by our proposed infrastructure.

In the following sections we provide a brief overview of SCM, discuss our information-sharing infrastructure framework and analyse how ef® cient information sharing impacts on convergent-assembly supply chain performance. Finally, we present our conclusions. To point out how our analysis and ® ndings relate to a real-world convergent assembly supply chain, throughout the paper we make reference to a General Motors (GM) supply chain consisting of steel suppliers, a motor vehicle stamping plant and the ® nal automobile assembly plants. Bhaskaran (1998) described the GM supply chain in more detail.

## Supply chain management

We introduce supply chains by presenting a general overview and a summary description of SCM.

## General overview of supply chain management

A supply chain is a network of facilities that procures raw materials, transforms them into intermediate subassemblies and ® nal products and then delivers the products to customers through a distribution system (Billington, 1994). Supply chains exist in virtually every industry, particularly industries that involve product manufacturing and the management of supply chains is not an easy task because of the large amount of activities that must be coordinated across organizational and global boundaries. The most common problems involve coordinating the materials inventory and production capacity availability across several organizations to produce products that can satisfy forecasted demand in an environment with a high level of uncertainty.

Several factors are making SCM an important issue for today’ s managers. These factors include more instances of multisite manufacturing, where several independent entities are involved in the production and delivery process, increasingly cut-throat marketing channels, the maturation of the world economy, with heightened demand for \`local’ products and competitive pressures to provide exceptional customer service, including quick, reliable delivery (Davis, 1993). In the past, management would concentrate on making each node of the SCN ef® cient. What managers are now realizing is that ef® ciency at each node does not result in the supply chain as a whole operating optimally. Increasingly, the challenges related to improved product quality, customer service and operating ef® ciency cannot be effectively met by isolated change to speci® c organizational units, but instead depend critically on the relationships and interdependencies between different organizations (or organizational units) (Swaminathan et al., 1998).

SCM is a management process that attempts to optimize the operation of the entire supply chain. Different entities in a supply chain typically operate subject to different sets of constraints and objectives. Even when belonging to the same company, supply chain entities often report to different divisions. Supply chain entities are highly interdependent when it comes to improving due date performance, increasing quality or reducing costs. As a result, the welfare of any entity in the system directly depends on the performance of the others and their willingness and ability to coordinate (Swaminathan et al., 1998).

## Business-to-business electronic commerce

Speci® cally, SCM involves balancing reliable customer delivery with manufacturing and inventory management costs (Billington, 1994). Two metrics commonly used to measure overall supply chain performance include order ful® lment cycle time and inventory level and cost. One major problem involved in SCM is understanding and managing the uncertainties involved in the supply chain. This is particularly true in the fashion skiwear industry where demand is heavily dependent on a variety of factors that are dif® - cult to predict ± the weather, fashion trends and the economy ± and the peak of the retail selling season is only two months long (Fisher et al., 1994). Different sources of uncertainty exist along a supply chain. They include demand (volume and mix), process (yield, machine downtimes and transportation reliabilities) and supply (part quality and delivery reliabilities) (Lee and Billington, 1993; Lee et al., 1993; Billington, 1994). Inventories are often used to protect the chain from these uncertainties.

Another major problem involved in SCM is the management of lead time. A role of IT in SCM is to assist managers in managing uncertainty and lead time through improved collection and sharing of information between supply chain nodes. It is felt that this will result in better customer service, through better coordination and improve asset management by giving decision makers the information necessary to optimize inventory and capital asset costs. Many of these improvements occur because IT enables changes to be made in inventory management and production planning dynamically. The dif® culty arises when trying to design an information system that can handle the information needs of each of the supply chain nodes to allow ef® cient, ¯ exible and decentralized SCM. The information infrastructure that we propose addresses these issues.

## Summary description of supply chain management

The information infrastructure that is required by SCM is by nature supported by a distributed information system. Because of this, we feel that a distributed system model is most appropriate to describe an SCN. Distributed problem solving is the cooperative solution of problems by a decentralized and loosely coupled collection of knowledge sources located in a number of distinct processor nodes (Smith and Davis, 1988). Distributed problem solving is often necessary because no one node has suf® cient information to solve the entire problem. The components of a distributed, coordination-intensive problem include goals, activities, actors and interdependencies (Malone and Crowston, 1990). We feel that a supply chain can be described by identifying its actors, activities, interdependencies, goals and objective. Our supply chain description is summarized in Table 1.

Table 1 Supply chain management summary description

<table><tr><td>Actors</td><td>Suppliers, manufacturers, assemblers, distributors and customers</td></tr><tr><td>Activities</td><td>Material and information processing</td></tr><tr><td>Interdependencies</td><td>Material shipments and orders, funds transfer and information sharing</td></tr><tr><td>Goals</td><td>Minimize order fulfilment cycle time and minimize inventory levels and costs</td></tr><tr><td>Overall objective</td><td>Balance individual goals based on priorities to produce the best ‘average’ performance or the best ‘worst case’ performance</td></tr></table>

For all supply chains, the overall objective is to balance each of the goals based on their importance to supply chain managers. In some situations costs may be the priority, while in other situations customer service may be the priority.

For the GM supply chain, the actors include the steel suppliers, stamping plant and vehicle assembly centres (VACs). The activities include materia processing, such as blanking, stamping and metal assembly at the stamping plant and information processing for forecasting and production planning at each supplier, manufacturer and assembler. The interdependencies include shipment of steel sheets to the stamping plant and shipment of doors, roofs, hoods and minor parts to the VACs in addition to transfer of information for plans and orders. The overall objective is to minimize the inventory levels necessary to maintain reasonable order ful® lment cycle times, taking into account demand, process and supply uncertainty across the supply chain.

## Information infrastructure framework for supporting supply chain management

Does IT exist for feasibly sharing information between supply chain partners? In this section we describe our proposed information-sharing infrastructure framework. We discuss the mechanisms required for effective SCM, the information infrastructure components required to support these mechanisms and how these components may be integrated into a complete information-sharing infrastructure. We also discuss existing technologies that make our infrastructure technologically feasible, as well as identify one set of technologies that provides the best information-sharing infrastructure currently available for SCM.

## Required mechanisms

SCM requires mechanisms (underlying business processes) that go beyond what was needed for ef® - cient operations management within an enterprise. It requires business processes that improve the integration and coordination of interorganizational processes. Based upon our analysis of supply chains in several industries we have identi® ed the following mechanisms required for effective SCM. They support both the transactions involved in the order ful® lment cycle as well as support activities such as forecasting, organizing, controlling, planning and customer service. SCM requires mechanisms for (1) forecasting demand based on information such as market research, (2) placing and receiving customer orders, (3) purchasing between supply chain partners, (4) processing orders internally, (5) identifying new sources for capacity and/or inventory when needed, (6) managing inventory, (7) planning production, (8) managing distribution (shipping), (9) communicating between supply chain partners and (10) supporting customer service.

## Information infrastructure components

Several components are necessary to meet the minimum requirements of an information infrastructure that supports the mechanisms required for effective SCM. These components are listed in Table 2. The components fall within one of three groups: applications, database and functional requirements.

## Application requirements of the infrastructure

The ® rst infrastructure components (components 1± 6) are the application requirements and the information systems needed for collection, processing and analysis of the information needed to support transaction processing and decision making (for required mechanisms) within each supply chain partner.

Table 2 Information infrastructure components

<table><tr><td>Application requirements</td><td>Electronic sales/Order processingElectronic inventory managementElectronic production planningElectronic purchasingElectronic distribution managementElectronic payments</td></tr><tr><td>Database requirements</td><td>Supply chain databaseCustomer service database</td></tr><tr><td>Functional requirements</td><td>Electronic transaction transfer systemElectronic information-sharing systemNetwork interface system</td></tr></table>

Electronic sales and order processing systems enable ® rms to process information related to customer orders. The order information can be entered once, as near to the source of the information as possible. The result is information that is more likely to be correct.

Electronic inventory management systems are needed to support inventory management decision making. It enables managers to make decisions based on current inventory data and production data resulting in more effective decisions related to purchasing, inventory levels and inventory locations. In the past, higher inventory levels were held because of high uncertainty about how much inventory was needed, how much was available and where it was.

Electronic production planning is similar to the previous component. In the past, production decision making was made based on less information and information that was more out-of-date and ® lled with errors. Today, production decisions such as job sequencing and lot sizing are based on a wider range of data that is more current and less uncertain. The result is more effective matching of production to demand with lower overall costs.

Electronic purchasing systems are needed to enable managers to make purchasing decisions based on production and inventory decisions. They enable managers to keep track of what was purchased, when it was purchased, how much it cost and when the shipment is expected to arrive.

Electronic distribution management systems are needed to support distribution activities such as product packing and shipping. It enables managers to know what was shipped, where it was shipped and when it should arrive.

Electronic payment systems are relatively new. These systems enable payments to be made electronically between buyers and sellers and generally involve third parties such as banks or credit card companies. Because electronic payment systems are still relatively new and undeveloped we refer you to Kalakota and Whinston (1996) for an overview of these systems including a discussion of important issues such as privacy, authentication and security.

## Database requirements of the infrastructure

The second infrastructure components (components 7 and 8) are the database requirements, the components that are required for the storage of information that needs to be shared by supply chain partners and customers. The supply chain database maintains information speci® c to the operations of the supply chain partners. This information would most likely not be available to customers. This database stores internal

## Business-to-business electronic commerce

supply chain information such as demand forecasts, sales data, inventory levels and location, production schedules, capacity availability and distribution data across the entire supply chain. Currently, in most supply chains, partner operations information is not available to supply chain managers. They only know what is going on in their ® rm and maybe not even that. With this information available, managers can make decisions based on much more accurate and complete information, thus resulting in improved supply chain performance.

The other database is the customer service database. This database stores information such as the status of customer orders. Customer service can be improved by allowing customers to access the status of their orders electronically so that they know when their orders will be shipped and when they should arrive. This reduces their supply uncertainty.

## Functional requirements of the infrastructure

The ® nal infrastructure components (components 9± 11) are the functional requirement components. Functional requirements are the components that are required for electronically connecting the applications, databases and users (internal users, supply chain partner users, customers and so forth) across the supply chain. Electronic transaction transfer systems provide a method for the transfer of information such as product orders and payments. Currently, some customers are placing orders electronically, but not many \`non-business’ customers. In the future, as more customers place orders electronically, information systems will be able to be even more integrated to increase the effectiveness of SCM.

Electronic information sharing systems support a wide range of activities including electronic advertising, market research, on-line information services and electronic communications. In the future, as issues such as security are better addressed, these systems will support an even wider range of activities. These future activities include electronic ordering, electronic markets for identifying new sources of production capacity or inventory and electronic payments and banking. In the future it is likely that direct connections such as transaction transfer systems will be handled through information sharing systems. This is because the information sharing systems are more ¯ exible and ® rms will be able to integrate their enterprise information systems with them much more easily. This is particularly useful for partnerships that are less permanent such as virtual organizations.

Network interface software is necessary for accessing the information and services that will be available through the information sharing systems. The effectiveness of these systems will increase as more activities can be handled through a single network interface software system.

## Information infrastructure framework

To support overall SCM, each of the information system components must be integrated into a supply chain information-sharing infrastructure. Figure 1 describes our supply chain information infrastructure.

Each of the supply chain partners, suppliers, manufacturers and distributors has an enterprise information system. Customers may also have this if they are a business and not an individual consumer. This system supports enterprise-level sales and order processing, inventory management, production planning, purchasing, distribution management and payment processes. It also supports the enterprise’s database systems, internal transaction processing systems and global network interface.

Information transfers between these enterprise information systems is done through the transaction transfer systems across a telecommunications network. A common use for this system is transferring order information. Supply chain partners have access to supply chain databases containing information such as demand forecasts, sales data, inventory data, production data and distribution data. This provides information to managers facilitating improved decision making and coordination across the supply chain. Each supply chain entity, including customers, can access information about the status of their orders through the customer service database. The databases can be accessed either through a wide area network or through the global information network depending on how the systems are implemented.

![](/api/attachments/XGS73Q33/fulltext/images/ef3a34b7e8823cd369f05267a2f49cfd1c71c7cde2df5503c6b9bba8b59bd3f7.jpg)  
Figure 1 Information-sharing infrastructure framework

Finally, all supply chain entities have access to the global information network. The activities supported by this system were discussed earlier. This system allows all supply chain entities to share information that may improve coordination and reduce the level of supply, process and demand uncertainty. It may also reduce the lead time for many activities because information can be transferred quickly using electronic methods.

For the GM supply chain, the steel suppliers, stamping plant and VACs each have an enterprise information system that allows them to process the plan and order information received to produce their own production plans utilizing their Kanban systems. Bhaskaran (1998) provided a detailed discussion of the operation of this Kanban system. Plan and order information transfers between these business units can be done through the transaction transfer systems across a telecommunications network. The units could also access supply chain databases containing more detailed information such as demand forecasts, sales data, inventory data, production data and distribution data if necessary. The stamping plant and VACs can also access information about the status of their orders through the customer service database. Finally, each unit can have access to the global information network. Overall, the infrastructure enables the steel suppliers, stamping plant and VACs to share information ef® ciently which allows them to minimize the inventory required to maintain acceptable order ful® lment cycle times.

## Functional component information technologies

In this section we discuss the evolution of informationsharing technologies that provide the functional components of our infrastructure. Most companies already have systems that ful® l the application and database requirements. The technologies that we discuss include electronic data interchange (EDI), the Internet-based World Wide Web (WWW), Intranets and Extranets.

EDI is an existing IT, which has been widely used for more than a decade, that provides a method of electronic transaction transfer. It is the process of computer-to-computer, business-to-business transaction transfer. EDI involves the direct routeing of information from one computer to another without interpretation or transcription by people and, to achieve this, the information must be structured according to prede® ned formats and rules which a computer can use directly (Holland et al., 1992). It provides several bene® ts for SCM.

EDI technology was shown to facilitate accurate, frequent and timely exchange of information to coordinate material movements between trading partners. Suppliers receiving just-in-time schedule information achieved better shipping performance. Similarly, suppliers with the ability to map incoming information to internal production control systems directly were found to enjoy even greater bene® ts. Moreover, as the supplier handles a higher fraction of customers electronically, it was found that shipment errors continued to diminish (Srinivasan et al., 1993).

Each year the use of EDI increases as organizations look for methods of improving enterprise integration and interorganizational coordination. Numerous studies have been done on various aspects of EDI and they all draw the same conclusion. EDI increases the speed and accuracy of processes compared with nonelectronic transfer of information (Snapp, 1990) and it is a potential source of competitive advantage (Johnston and Vitale, 1988). When a supplier and a procurer use IT to create joint, interpenetrating processes at the interface between value-adding stages, they are taking advantage of the electronic integration effect. This effect occurs when IT is used not just to speed communication, but to change ± and lead to tighter coupling of ± the processes that create and use information. One simple bene® t of this effect is the time saved and the errors avoided by the fact that data need only be entered once (Malone et al., 1987).

A practical problem that must be addressed when designing an EDI process is the lack of a globally recognized standard format for data storage and transfer (Snapp, 1990). Because standards are lacking, organizations must agree upon the translation software and data format on a project by project basis. Without an agreement upon a standard the EDI process will not work. This is one of the reasons why there will be a general movement away from these transactionspeci® c connections to more ¯ exible methods of electronic information transfer. One solution that has been considered by a number of businesses is using the Internet-based WWW and Net browsers (such as Netscape Navigator).

The Internet is an example of a global information network composed of an existing set of ITs that provide a method for electronic information sharing. One component of the Internet is the WWW. Although the WWW was not developed speci® cally for the sharing of information among supply chain partners, it provides a model for these types of systems. The WWW was developed to be a pool of human knowledge, which would allow collaborators in remote sites to share their ideas and all aspects of a common project (Berners-Lee et al., 1994). Because SCM is similar to the projects the WWW was designed for (remote sites, shared knowledge and common project) it can serve as a method for sharing of information in a supply chain. Netscape Navigator is an example of a WWW browser or global network interface which provides seamless access to a wide range of data through the WWW. The HyperText Transfer Protocol (HTTP) and the Common Gateway Interface (CGI) provide standard communication protocols for information sharing across the WWW. It enables applications and databases to be connected across organizations.

The major problem with using the Internet for SCM is security. Experts say reports of Internet-related security breaches are rising. Nearly one in four respondents to an Information Week survey conducted in February 1996 say fear of Internet break ins is keeping them from using the Internet (Violino, 1996). The solution seems to be a more secure version of the Internet, an Intranet.

An Intranet is essentially any site based on Internet technology but placed on private servers and designed not to allow outsiders in (Miller, 1996). The outsiders in this case would be individuals and companies not directly involved in the management of the supply chain. Intranets use WWW-based and Internet technology to share (organizational) data across a private network inexpensively and easily (Carr, 1996). We feel that the \`organization’ can encompass several separate ® rms such as in a supply chain. Intranet usage is predicted to overwhelm external Internet usage before the turn of the century. The key enablers of WWW growth are (1) the proliferation of PCs, local area networks (LANs) and modems, (2) open standards such as Transmission Control Protocol/Internet Protocol (TCP/IP), HTTP, Hyper Text Markup Language (HTML) and CGI, (3) cross-platform support, (4) multimedia support and ease of use and (5) support for secure transactions. (Organizational) Intranets can provide information in a way that is immediate, costeffective, easy to use, rich in format and versatile (Netscape Communications Corporation, 1996). What we have described is an extended Intranet (or Extranet). This is in line with the third wave of Internet usage identi® ed by Netscape Communications Corporation’s Marc Andreessen. We are ready for a new era: the emergence of the Extranet or extended Intranet connecting companies with their suppliers and customers via WWW links (Karpinski, 1997).

Based upon our analysis, our conclusion is that Extranets using the WWW (with its standard protocols, middleware and browser software) provide existing technologies that ful® l the three functional requirements of our proposed infrastructure to support supply chain operations. It may also be used as an interface between the supply chain and its customers. Looking at Figure 1, an Extranet can be used to support information sharing between the ® rms within the SCN box (shown by arrows within the SCN box). It can also be used as an interface between the supply chain and external entities, such as customers (shown by arrows between the SCN and the external environment). For example, an assembler in an automobile supply chain can request supply information from a component manufacturer by sending an HTTP request through their browser to a WWW server. The server runs a CGI script to execute programs that access any necessary databases to process the request and return output to the HTTP server. The server translates the output into an HTTP response to the client (Farrell, 1996). Therefore, technologies do exist for feasibly sharing information between supply chain partners. These technologies can be used for the GM supply chain to enable ef® cient information sharing between the steel suppliers, stamping plant and VACs.

## Performance improvements enabled by the information infrastructure

We illustrate the usefulness of our information-sharing infrastructure by presenting and discussing results from simulations of convergent assembly supply chain performance under various information-sharing strategies. Information sharing can be implemented through a supply chain-wide Extranet. In this section we focus on one of the core business processes, the order ful® lment process (OFP) and use the Swarm simulation platform (Santa Fe Institute, 1996) to simulate the OFP in SCNs (Lin, 1996; Lin et al., 1996). Swarm is a multiagent simulation platform developed for the study of complex adaptive systems. It was developed at the Santa Fe Institute and aims to provide a general purpose simulation tool for building simulation models. A detailed description of Swarm is outside the scope of this paper, but can be found in Lin et al. (1996). Our supply chain implementation in Swarm is described in more detail later.

An OFP begins with receiving orders from customers and ends with having the ® nished goods delivered (Lin, 1996). It consists of several activities (subprocesses), such as order management, manufacturing and distribution. The main objectives of the OFP can be generalized into two dimensions (Christopher, 1993; Goldman et al., 1995; Lin, 1996): delivering quali® ed products to ful® l customer orders at the right time and right place and achieving agility to handle uncertainties from the internal and external environments.

## Issues in managing supply chain networks for supporting the order ful® lment process

Because of the complexity of an SCN, it is a challenge to coordinate the actions of entities within the network to perform in a coherent manner. When orders come into an entity in an SCN, the lead time for delivering products (called the order ful® lment cycle time) is composed of the following.

(1) Order processing times, including the order transfer time from customers to manufacturers or distributors and the due date assignment process.

(2) Material lead times, including material planning and purchase lead time, supplier lead time, transport lead time, receipt and inspection lead time, assembly release time and material order picking time.

(3) Assembly lead times, including waiting time, processing times and transport time to the next stage.

(4) Distribution lead times, including dispatch preparation time (documents, packages) and transportation time to the customer.

(5) Installation lead times.

These components of the order ful® lment cycle time distribute across the network and the variation of lead times at any stage will affect the execution of the other stages and result in uncertainties for the overall order cycle time. This is called the ripple effect.

Take, for example, a product that is assembled by component parts from several different suppliers. The cycle time for assembling the product can be affected by the lead time of material supply from different suppliers. If parts from some of the suppliers come later than the other parts for assembly, the assembly will be delayed due to the unavailability of required parts. This also increases the inventory costs for those parts available. If the product is a component for the downstream manufacturing process, the delay for shipping this product will affect the subsequent stages and, in turn, in¯ uence the whole network. Therefore, the ® rst issue in managing an SCN is how to control the ripple effect of lead time so that the variability of an SCN can be mitigated. How to coordinate the policies of up- and downstream entities in facilitating such variability reduction is the main concern. Demand forecasting is used to estimate the demand for each stage and the inventory between stages of the network is used for protecting against ¯ uctuations in supply and demand across the network such as machine breakdown, extra large demand, etc. Due to the shortening of product life cycles, such protection seems unwise and actually reduces ¯ exibility.

Because of the decentralized control properties of the SCN, control of the ripple effect requires coordination between entities in performing their tasks. The management of interdependencies is the key to smooth material ¯ ow within the SCN. The interdependencies between entities of the SCN can be described in the following situations.

(1) Producer/consumer dependence can be used to describe the supplier/manufacturer relationship in the SCN. This requires cooperation between suppliers and manufacturers in an ef® cient and effective way. Ef® ciency means to reduce material lead times and effectiveness means to supply only the needed materials. This dependence also implies a constraint satisfaction problem and it is a constraint propagation issue through the network too.

(2) Material ¯ ow within the SCN implies a synchronization problem, where related materials for a product are delivered to the manufacturer at a coherent speed which incurs minimal inventory and delay.

Inventory is an unwise approach to dealing with highly changing market demand and short life cycle products. What would be the substitution for inventory? Information can substitute for inventory. The material lead time information from different suppliers can be used for planning the material arrival, instead of building up inventory. The demand information can be transmitted to the manufacturers on a timely basis, so that orders can be ful® lled with less inventory costs. The second main issue is how to manage the information ¯ ow within an SCN so that decisions made by business entities can take more global factors into consideration. In this way, we can increase SCN visibility.

These issues are brought up because of the essential concern of how to make the network respond effectively and ef® ciently to satisfy customer demand, which leads to the motivation for managing SCNs to support the OFP.

Lin (1996) identi® ed three main types of SCNs (Types I, II and III) based on such attributes as manufacturing process, primary business objective, product differentiation, range of product variation, assembly stages, product life cycle and main inventory type, as shown in Table 3.

In this paper we focus on the automobile and aerospace industries. These industries and the GM supply chain discussed throughout this paper are associated with type I SCNs, where how to meet customer demand ef® ciently without carrying excessive inventory and how to coordinate suppliers and assemblers to smooth material ¯ ow are two main issues and challenges. Structurally, there are many suppliers. The wide range of materials and subcomponents that come from these suppliers converges through a series of manufacturing stages until the ® nal product is assembled at one location. The ® nal product is then shipped to several distributors and ultimately to a large number of retailers.

Table 3 The properties of type I, II and III SCNs

<table><tr><td>Attributes</td><td>Type I SCN</td><td>Type II SCN</td><td>Type III SCN</td></tr><tr><td>Manufacturing process</td><td>Convergent assembly</td><td>Divergent assembly</td><td>Divergent differentiation</td></tr><tr><td>Primary business objectives</td><td>Lean production</td><td>Customization</td><td>Responsiveness</td></tr><tr><td>Product differentiation</td><td>Early</td><td>Late</td><td>Late</td></tr><tr><td>Range of product variations</td><td>Small</td><td>Medium</td><td>Large</td></tr><tr><td>Assembly process</td><td>Concentrating at the manufacturing stage</td><td>Distributed to the distribution stage</td><td>Concentrating at the manufacturing stage</td></tr><tr><td>Product life cycle</td><td>Years</td><td>Months to years</td><td>Weeks to months</td></tr><tr><td>Main inventory type</td><td>End products</td><td>Semi-products</td><td>Raw materials</td></tr><tr><td>Example industries</td><td>Motor vehicle and aerospace</td><td>Appliance, electronics and computers</td><td>Apparel/Fashion</td></tr></table>

## The implementation of Swarm for simulating order ful® lment in supply chain networks

Figure 2 describes the SCN implementation on the Swarm platform. The topmost swarm, the OFP batch swarm, is designed to control the whole simulation. It creates two swarms, the OFP model swarm and the statistics swarm, creates actions and then activates the simulation process. The OFP model swarm is composed of an array of SCN entities created while building objects. The SCN con® guration with each entity’ s properties and product information are fed in during the entities’ creation. The OFP model actions are composed of each SCN entity’ s actions and are activated when the OFP model swarm is activated. An SCN entity is composed of several agents, such as an order management agent, an inventory management agent and an SCN management agent. An entity with manufacturing capability includes a production planning agent, a capacity planning agent, a materials planning agent, a shop ¯ oor control agent and a manufacturing systems agent. An SCN entity swarm holds entity-level information such as suppliers, customers, order transfer delay time and product delivery time, which are accessible by internal agents and other entities. The encapsulated agents perform certain functions in enabling the movement of information and material within the entity and between entities. The statistics swarm is used to compute the statistics data gathered through the simulation for analysis purposes.

The following scenario describes the interactions between these agents and Figure 3 summarizes them. Mapping Figure 3 to the GM supply chain, ScnESwarm B would be the steel suppliers, ScnESwarm A would be the stamping plant and ScnESwarm C would be the VACs. Using a general example, an entity ScnESwarm A receives an order from its customer ScnESwarm C. The order ¯ ows to the order management agent (OrdM). According to the customer lead times, the inventory availability information (from InvM), the production plan (from PrdP) and the manufacturing capacity (CapP), the order management agent assigns a due date to the order. If the products are in stock, the order is ® lled by shipping the products from inventory. If the products are in receiving, the due date is set according to the delivery date of the products.

![](/api/attachments/XGS73Q33/fulltext/images/5fbf8333e45e26b94620ab30f7b27ce403bc343b6915105d54591ab17987f5ed.jpg)  
Figure 2 The implementation of SCNs in Swarm

ScnESwarm A  
![](/api/attachments/XGS73Q33/fulltext/images/055d38d3ed321c15d40d8861243355c6aec65275da6abfc5e154e4db26aca6f4.jpg)  
Figure 3 SCN agent interactions in the Swarm implementation

For an entity with manufacturing capability, the order is forwarded to the PrdP agent where the schedule for making the products is planned. The CapP agent and the material planning (MatP) agent are partner agents in generating achievable build plans. The MatP agent obtains build plans from the PrdP agent to allocate materials for manufacturing. It also contributes information about material availability to PrdP for scheduling. The CapP agent plans capacity by taking the build plan from PrdP and sends capacity usage information to PrdP for scheduling the build plan. The SCN management (ScnM) agent takes the order information to choose suppliers in allocating material sources. The outgoing orders are transferred through its SCN entity (ScnESwarm A) to be transferred to other entities (i.e. ScnESwarm B). This describes the information within an entity.

If the entity is a distribution centre or a retailer without manufacturing capability, the products ordered products are delivered from suppliers as end products to ship to its customers. For an entity with manufacturing capability, the ordered end products are supplied from the shop ¯ oor (ManuS) to its customers. The input materials are components for the end products. This represents the material ¯ ow with an entity. The interaction of these agents enables the ¯ ow of materials and information within an entity and, through the SCN entity swarm (ScnESwarm), the information and materials flow across the SCN.

In this section we described the components of our SCN simulation model. The speci® c business environments that we simulate are described in the next section.

![](/api/attachments/XGS73Q33/fulltext/images/d8cd954c2e0b9ce84c659111f3e74069aa9b9d637ca72a1829bde9286fb41581.jpg)  
Figure 4 Simulated SCN structure ± Scn-1

## Impact of information sharing on convergent assembly supply chains

We implemented an SCN designed to simulate a convergent assembly supply chain. The SCN simulated is more complex than the GM supply chain example, but their structure and operations are similar. Scn-I in Figure 4 represents a type I SCN consisting of 20 business entities aligned into six tiers. Entities in tiers 1± 4 have manufacturing capability and entities in tiers 5 and 6 do not. Scn-I captures some features of a type I SCN such as performing convergent assembly, early product differentiation, few product models and an assembly process concentrating at the manufacturing stages.

We conducted experiments to evaluate the OFP performance using various information-sharing strategies. Information sharing between business entities considers three issues: (1) the information contents, (2) the depth of information penetration (the number of tiers for which information is accessible) and (3) the information acquisition direction (upward or downward sharing). Agent decision-making processes are held constant to isolate the impact of information sharing.

In the design of the simulation platform, the information acquired by downstream entities is mainly material and capacity availability information from their suppliers. The information acquired by an upstream entity is information about customer demand and orders. The depth of information penetration can be speci® ed to various degrees, e.g. isolated, upward one tier, upward two tiers, downward one tier, downward two tiers and so forth.

The capacity obtained and material information from suppliers is used to estimate the due dates of incoming orders, which are the basis for generating build plans or reordering schedules. The customer demand information obtained is used to estimate the demand for the next period, so that the production or reordering schedules can adapt to external demand.

The characteristics and application situations of demand management policies, such as make-to-order (MTO), make-to-stock (MTS) and assembly-to-order (ATO), are described in Table 4 (McCutcheon et al., 1994; Lin, 1996).

If the amount of customization is low, the ® rm can usually employ an MTS approach and then use inventories of ® nished goods to provide short lead times. For products with high customization, the MTS strategy cannot match customer preferences ef® ciently and effectively. If customers are willing to wait for customized products after submitting orders, the MTO strategy can be applied to high-customization ® rms. When the product design allows the product differentiation stage to occur late enough in the production process, the ® rm can employ an ATO approach.

The results from evaluating various informationsharing strategies under these three types of demand management policies in the type I SCN are shown in Figures 5 and 6. The three information-sharing strategies are (1) no information sharing, (2) supply information sharing and (3) supply and demand information sharing. The three demand management policies are MTO, ATO, and MTS (Lin, 1996).

Figures 5 and 6 show the order cycle times and the inventory costs, respectively, under three demand management policies using the three informationsharing strategies. The order cycle time is the cycle time per order in the SCN. Inventory costs are the sum of the inventory costs across the SCN. From Figure 5 we see that cycle time remains stable under MTO and MTS demand management policies as more information is shared. The cycle time under the ATO policy does bene® t from supply information sharing and further bene® ts from the addition of demand information sharing. From Figure 6 we see that inventory costs are dramatically reduced for MTS and ATO policies when supply information is shared. The bene® ts from sharing demand information are slight. Combining the cycle time and inventory ® ndings we feel that MTS is the best demand management strategy. Its resulting cycle time is low and inventory costs are very low. Supply information is critical to improving performance in a type I SCN.

This can be explained by the structural characteristics of this type of supply chain. Materials for products in a type I SCN (e.g. such as that of a carmaker) are unique and supplied by different suppliers; the supply information enables customers to schedule the build plans by scheduling the material arrivals for constituent components on a timely basis. Therefore, the inventory costs are reduced by eliminating the inventory of constituent components waiting for unavailable components. Because the range of product variations is small in a type I SCN, the addition of demand information sharing does not signi® cantly reduce the order cycle time and inventory cost. The critical component in the infrastructure is the link between suppliers, manufacturers and assemblers.

![](/api/attachments/XGS73Q33/fulltext/images/56873e1a97762cab9346a17b8d712c5c8c5d30ec1471a13c5d003c76dc42de5a.jpg)  
NONE: No information sharing SI: Supply information is shared SDI: Supply and demand information is shared MTO: Make-to-order ATO: Assemble-to-order MTS: Make-to-stock

Figure 5 OFP improvement in order cycle time reduction using various information-sharing strategies in a type I SCN  
![](/api/attachments/XGS73Q33/fulltext/images/64919473cf5fb2180d0aad542f5b4435a91b566818d6c718f77ef2072e5d6899.jpg)

NONE: No information sharing SI: Supply information is shared SDI: Supply and demand information is shared MTO: Make-to-order ATO: Assemble-to-order MTS: Make-to-stock

Figure 6 OFP improvement in inventory cost reduction using various information-sharing strategies in a type I SCN  
Table 4 Example demand management policies for the OFP

<table><tr><td>Policies</td><td>Characteristics</td><td>Application situations</td></tr><tr><td>MTO</td><td>Production is triggered by customer orders</td><td>High customization pressure but low responsiveness</td></tr><tr><td>ATO</td><td>Final assembly is order driven, but the component parts are forecast driven and built to stock</td><td>High customization pressure, high responsiveness and products with late differentiation</td></tr><tr><td>MTS</td><td>Production is triggered by inventory replenishment points</td><td>Low customization pressure</td></tr></table>

Two sets of conclusions can be drawn from our study. The ® rst set relates to ® ndings speci® c to convergent assembly supply chains, while the second set relates to overall ® ndings concerning the relationship between information infrastructure and SCM.

Management of supply chains in industries involving type I (convergent assembly) supply chains is most effective when using an MTS demand management policy coupled with sharing of supply (material availability and capacity) information. Inventory costs are dramatically reduced while acceptable order ful® lment cycle times are maintained. This is particularly important for these SCNs because the number of components is large and the primary business objective is lean production. These ® ndings related to convergent assembly supply chains produce some interesting overall conclusions.

First, SCM relies heavily on its information infrastructure. Supply chain performance can be improved through the information sharing and coordination enabled by our infrastructure. In addition, Extranets are a current technology that ® t within our infrastructure to support management of supply chain operations. An Extranet, with its associated components, provides a current technology for the functional requirements of our infrastructure that is more ¯ exible than EDI, while increasing data and message security relative to the Internet. It is useful for supporting information sharing within the supply chain.

Finally, SCM involves a fundamental trade-off between cycle time, inventory and information. In many cases information can replace inventory while maintaining acceptable cycle times. In the past, when information costs were high, inventory was held to manage uncertainty. Today, when IT continues to reduce information costs, uncertainty can be reduced resulting in lower inventory requirements. Our results illustrate some of the potential impacts of the electronic integration effect (Malone et al., 1987). The bene® ts that we illustrate related to this effect are that supply chain managers may reduce inventory costs because of reduced uncertainty in decision making. This is possible because IT (incorporated into electronic hierarchies) reduces coordination costs. The development of an analytical model to describe this trade-off is an issue that should be addressed by future research. It is essentially a matter of information economics (Stigler, 1961), identifying the \`value’ of information, in this case the reduction of inventory costs versus the cost of \`searching’ for the information. Overall, we feel that an interorganizational information system design based on our framework can support the processes and decision making required for effective SCM.

## References

Applegate, L.M., Holsapple, C.W., Kalakota, R., Radermacher, F.J. and Whinston, A.B. (1996) Electronic commerce: building blocks of new business opportunity. Journal of Organizational Computing and Electronic Commerce 6(1), 1± 10.

Berners-Lee, T., Cailliau, R., Luotonen, A., Nielsen, H.F. and Secret, A. (1994) The World-Wide Web. Communications of the ACM 37(8), 76± 82.

Bhaskaran, S. (1998) Simulation analysis of a manufacturing supply chain. Decision Sciences 29(3), 633± 57.

Billington, C. (1994) Strategic supply chain management. OR/MS Today April 21(2), 20± 7.

Carr, J. (1996) Intranets deliver. InfoWorld, 18 (8), 61± 63.

Christopher, M. (1993) Logistics and Supply Chain Management (Pitman Publishing, London).

D’ Amours, S., Montreuil, B., Lefrancois, P. and Soumis, F. (1999) Networked manufacturing: the impact of information sharing. International Journal of Production Economics 58, 63± 79.

Davis, T. (1993) Effective supply chain management. Sloan Management Review Summer 34(4), 35± 73.

Farrell, R. (1996) 60 Minute Guide to CGI Programming with Perl 5 (IDG Books Worldwide, Inc., Foster City, CA).

Fisher, M.L., Hammond, J.H., Obermeyer, W.R. and Raman, A. (1994) Making supply meet demand in an uncertain world. Harvard Business Review, May± June, 83± 93.

Gavirneni, S., Kapuscinski, R. and Tayur, S. (1999) Value of information in capacitated supply chains. Management Science 45(1), 16± 24.

Goldman, S.L., Nagel, R.N. and Preiss, K. (1995) Agile Competitors and Virtual Organizations: Strategies for Enriching the Customer (Van Nostrand Reinhold, New York).

Holland, C., Lockett, G. and Blackman, I. (1992) Planning for electronic data interchange. Strategic Management Journal 13, 539± 50.

Johnston, H.R. and Vitale, M.R. (1988) Creating advantage with interorganizational information systems. MIS Quarterly 12(2), 153± 66.

Kalakota, R. and Whinston, A.B. (1996) Frontiers of Electronic Commerce (Addison-Wesley Publishing Company, Inc., Reading, MA).

Karpinski, R. (1997) Extranets emerge as next challenge for marketers. Netmarketing April, M-4.

Lee, H.L. and Billington, C. (1992) Managing supply chain inventory: pitfalls and opportunities. Sloan Management Review Spring 33(3), 65± 73.

Lee, H.L. and Billington, C. (1993) Material management in decentralized supply chains. Operations Research 41(5), 835± 47.

Lee, H.L., Billington, C. and Carter, B. (1993) Hewlett-Packard gains control of inventory and service through design for localization. Interfaces 23(4), 1± 11.

Lin, F. (1996) Reengineering the order ful® llment process in supply chain networks: a mutliagent information systems approach. PhD thesis, University of Illinois at Urbana-Champaign.

Lin, F., Tan, G.W. and Shaw, M.J. (1996) Multi-agent Enterprise Modeling (University of Illinois at Urbana-Champaign, College of Commerce and Business Administration, Of® ce of Research, Champaign, IL).

McCutcheon, D.M., Amitabh, S. and Meredith, J.R. (1994) The customization-responsiveness squeeze. Sloan Management Review Winter 35(2), 89± 99.

Malone, T.W. and Crowston, K. (1990) What is coordination theory and how can it help design cooperative work systems? In Proceedings of Computer Supported Cooperative Work ’90, pp. 375± 88.

Malone, T.W. and Rockart, J.F. (1991) Computers, networks, and the corporation. Scienti® c American 265(3), 128± 36.

Malone, T.W., Yates, J. and Benjamin, R.I. (1987) Electronic markets and electronic hierarchies. Communications of the ACM 30(6), 484± 97.

Miller, M.J. (1996) Your own private Internet. PC Magazine 15(5), 29.

Netscape Communications Corporation (1996) Intranets rede® ne corporate information systems.

Santa Fe Institute (1996) The swarm simulation system.

Smith, R.G. and Davis, R. (1988) Frameworks for cooperation in distributed problem solving, in Readings in Distributed Arti® cial Intelligence, Bond, A.H. and Gasser, L. (eds) (Morgan Kaufmann Publishers, Inc., San Mateo, CA).

Snapp, C.D. (1990) EDI aims high for global growth. Datamation 1 March, 77± 80.

Srinivasan, K., Kekre, S. and Mukhopadhyay, T. (1993) Impact of Electronic Data Interchange Technology on JIT Shipments (Graduate School of Industrial Administration, Carnegie Mellon University, Pitsburgh, PA).

Stigler, G. (1961) The economics of information. Journal of Political Economy 69(3), 213± 25.

Swaminathan, J.M., Smith, S.F. and Sadeh, N.M. (1998) Modeling supply chain dynamics: a multiagent approach. Decision Sciences 29(3), 607± 32.

Violino, B. (1996) Your worst nightmare. Information Week 19 February, 34± 6.

## Biographical notes

Troy J. Strader is an assistant professor of management information systems in the Department of Logistics, Operations and MIS at Iowa State University. He received his PhD in business administration (information systems) from the University of Illinois at Urbana-Champaign in 1997. His research interests include electronic commerce, strategic impacts of information systems and information economics.

Fu-Ren Lin is an associate professor of management information systems in the Department of Information Management at the National Sun Yat-sen University in Taiwan. He received his PhD in business administration (information systems) from the University of Illinois at Urbana-Champaign in 1996. His research interests include decision support systems, arti® cial intelligence applications for business, supply chain management and electronic commerce.

Michael J. Shaw is a professor of information systems and technology in the Department of Business Administration at the University of Illinois at Urbana-Champaign where he has been a faculty member since 1984. He is also a senior research scientist at the National Center for Supercomputing Applications (NCSA) and a professor at the Beckman Institute for Advanced Science and Technology. His research is focused on the management of information technology, electronic commerce, information technology for business process re-engineering, data mining and decision support systems.

Address for correspondence: Management Information Systems, 300 Carver Hall, Iowa State University, Ames, IA 50011± 2063, USA
