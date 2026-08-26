---
otero_id: 1152
otero_key: "2HW39XQZ"
title: "Toward the Inter-organizational Product Information Supply Chain – Evidence from the Retail and Consumer Goods Industries"
authors: "Jan Schemm; Christine Legner"
year: "2008"
journal: "Journal of the Association for Information Systems"
doi: "10.17705/1jais.00156"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
4-2008

# Toward the Inter-organizational Product Information Supply Chain – Evidence from the Retail and Consumer Goods Industries

Christine Legner , christine.legner@ebs.edu

Jan Schemm , jan.schemm@unisg.ch

Follow this and additional works at: https://aisel.aisnet.org/jais

# Journal of the Association for Information Systems JAIS

Special Issue

# Toward the Inter-organizational Product Information Supply Chain – Evidence from the Retail and Consumer Goods Industries\*

Christine Legner Institute of Information Management University of St. Gallen, Switzerland, and Institute of Research on Information Systems European Business School, Germany christine.legner@ebs.edu

Jan Schemm Institute of Information Management University of St. Gallen, Switzerland jan.schemm@unisg.ch

## Abstract

Since the 1980s, the retail and consumer goods industries have been making very extensive use of EDI-based data exchange and subsequently developed the vision of Efficient Consumer Response (ECR). In the meantime, a growing number of studies report that poor data quality, in particular outdated or wrong product information, negatively impacts demand and supply chain performance. Whereas prior literature intensively studied the positive effects of information sharing on the coordination of supply and demand, this research is aimed at establishing a basis for understanding the phenomena of the underlying inter-organizational product information supply chain. Using coordination theory as an overarching framework, the main research contribution is a set of dependencies, coordination problems, and coordination mechanisms that characterize the product information supply chain. From an analysis of two retailer-manufacturer relationships, we conclude that flow and sharing dependencies evolve into reciprocal dependencies as the intensity of demand and supply collaboration increases. We also find that industry standards — notably Global Data Synchronization (GDS) — do not yet fully cover the inter-organizational coordination requirements that result from the identified set of sharing and flow dependencies.

Keywords: Efficient Consumer Response (ECR), Global Data Synchronization (GDSN), Information Supply Chain, Inter-Organizational Systems (IOS), Industry Standards, Master Data, Retail-Supplier Relationships

# Toward the Inter-organizational Product Information Supply Chain: Evidence from the Retail and Consumer Goods Industries

## 1. Introduction

Most practitioners and the academic community agree that integrated supply chains heavily rely on the exchange and sharing of information between the actors. A prominent example is the collaboration between the retail and consumer goods industries. Since the 1980s, these industries have been making very extensive use of EDI-based data exchange and subsequently developed the vision of Efficient Consumer Response (ECR) in order to align their activities more closely. In the context of ECR (cf. Corsten and Kumar, 2005; Holweg et al., 2005; Kurnia and Johnston, 2003; Reyes and Bhutta, 2005) as well as in IS (cf. Clark and Stoddard, 1996; Gosain et al., 2004; Saeed et al., 2005) and operations management research (cf. Aviv, 2001; Cohen Kulp et al., 2004; Gavirneni et al., 1999; Lee et al., 2000; Sahin and Robinson, 2002), much attention has been given to the coordination of supply and demand chains and the benefits of information sharing. It is only recently that the underlying exchange of product information has started to gain broader attention: A growing number of studies report that poor data quality, in particular outdated or wrong product information, negatively impacts the benefits that retailers and their suppliers pursue as they implement tighter forms of collaboration (Accenture, 2006; Global Commerce Initiative and Capgemini, 2005; Grocery Manufacturers of America et al., 2003). Various alternative concepts have been suggested as electronic infrastructure for exchanging product information among supply chain partners. But up to now, neither the EDI-based, bilateral product data exchange nor data pools that facilitate multilateral data exchange have been broadly adopted (Horst, 2007; Nakatani et al., 2006). In 2004, the Globa Data Synchronization Network (GDSN) was launched with the objective of establishing many-to-many relationships between retailers and their suppliers for sharing product master data. Retailers and suppliers have high expectations for the GDSN, given the recent consolidation of master data pools (Garf and Romanow, 2005) and announcements in favor of GDSN by leading retailers such as Wal Mart, Ahold, Tesco and Metro and their suppliers Nestlé, Procter & Gamble and Kraft Foods (Field, 2005; Pendrous, 2006).

Building on the vision of the information supply chain as suggested by (Marinos, 2005; Sun and Yen, 2005), this research suggests differentiating two sets of information sharing and coordination problems in the retail and consumer goods industries: (1) the transactional information flow that allows for coordinating the physical demand and supply chain, and (2) the contextual information flow that ensures that retailers and manufacturers interpret data in the same way (Goh et al., 1999; Madnick, 1995). The latter is a prerequisite for electronic ECR collaboration and comprises the exchange of product and partner information. Whereas previous research focuses on the transactional information flow and demonstrates the positive effects of information sharing on the coordination of supply and demand, this paper is aimed at establishing a basis for understanding the phenomenon of the underlying inter-organizational product information supply chain. Using coordination theory (Malone and Crowston, 1994; March and Simon, 1958) as an overarching framework, we explore the characteristics of the inter-organizational product information supply chain by systematically analyzing the acquisition and consumption of product information in retailermanufacturer relationships. We give particular emphasis to the contribution of Global Data Synchronization (GDS) to organizing and streamlining the inter-organizational product information supply chain.

The remainder of this paper is structured as follows: We first present a review of the literature to establish the research context. From the assessment of the literature, we derive a conceptualization of the product information supply chain and identify the issues and questions that motivate our research. Subsequently, we explain our research method and approach. By analyzing two pairs o retailer-manufacturer relationships, we explore the coordination problems and mechanisms in the inter-organizational product information supply chain. On the basis of these findings, we discuss implications for the conceptualization of the inter-organizational product information supply chain and the role and adoption of Global Data Synchronization.

## 2. Prior Research

This research relates to three distinct streams of prior work: (1) the emerging field of research on the information supply chain, (2) research into the effect of information sharing on supply chains from the perspective of operations management and IS research, and (3) specific studies related to supply chain collaboration in the retail and consumer goods industries.

## 2.1. The Information Supply Chain

The notion of an information supply chain has only recently been introduced. Using supply chain management as a metaphor, it aims to create and unify concepts, methods, theories and technologies for information sharing problems. According to Sun and Yen (2005), “An information supply chain (ISC) fulfills users’ information requirements by a network of information-sharing agents (ISA) that gather, interpret, and satisfy the requirements with proper information.” Other authors consider the information supply chain to be an information-centric view of physical and virtual supply chains, where each entity adds value to the chain by providing the right information to the right entity at the right time in a secure manner (cf. Sahin and Robinson, 2002). Similar to the case in a supply chain, insufficient information supply leads to information deficiency, whereas abundant information may create information overflow. There are different perspectives on how the information supply chain relates to the physical supply chain: Whereas Sahin and Robinson (2002) tightly couple the value of information sharing with the physical coordination of goods flow, other scholars (Marinos, 2005; Sun and Yen, 2005) argue that the information supply chain does not coincide with the transactional information flow within a supply chain.

Although the vision of the information supply chain seems intuitive, few models and little related research are available so far. Some links can be drawn to prior work on the management of information assets, which transfers concepts from resource management to the field of information management. In order to overcome information generation as a by-product of physical processes, Wang et al. (1998) emphasize the need for an information product (IP) approach. They suggest defining information products based on the consumer’s information needs and quality criteria, and managing them over the information life-cycle in the same way as a physical product. While Wang et al. (1998) distinguish the roles of information manufacturers, suppliers, and consumers, Lee and Strong (2003) describe a role model consisting of data collectors, data custodians, and data consumers. According to the same authors, a data production process encompasses distinctive work processes for data collection, storage, and use. In their information manufacturing model, Ballou et al. (1998) address the issue of measuring the quality of information products delivered and suggest a set of relevant attributes, namely the timeliness, quality, cost, and value of information products.

## 2.2. Information Sharing along the Supply Chain

Whereas the notion of the “information supply chain” is rather new, operations management researchers have intensively studied information distortion and the value of shared information in supply chains (e.g. Aviv, 2001; Gavirneni et al., 1999; Lee et al., 2000; Sahin and Robinson, 2002), as have information systems researchers (e.g. Clark and Stoddard, 1996; Gosain et al., 2004; Premkumar, 2000; Saeed et al., 2005). Lee et al. (1997) were the first to identify information asymmetry as the main reason for the amplification of the demand signal and fluctuation of inventory level along a supply chain, which consists of customers, retailers, wholesalers, distributors, and factories. This phenomenon, which is well-known as the ”bullwhip effect”, has been extensively analyzed (e.g. Cachon and Fisher, 2000; Chen et al., 2000; Cohen Kulp et al., 2004; Lau et al., 2002; Sheu et al., 2006). There is consensus that information sharing improves the decision-making of supply chain actors with regard to ordering, capacity allocation, and production / materials planning, enabling the supply chain as a whole to reduce costs and respond more quickly to end-consumer demand. In a numerical study, Cachon and Fisher (2000) find that supply chain costs are on average 2.2 percent lower with the full information policy than with the traditional information policy, and the maximum difference is 12.1 percent. Cohen Kulp et al. (2004) report that information sharing, specifically sharing information about consumer needs and store-level inventory, is related to a positive change in profit margins. The same authors demonstrate that companies only realize above-average profit margins when they work together on inventory management and/or new product development. This particular aspect is the focus of the extensive literature review performed by Sahin and Robinson (2002). From categorizing the existing body of research in terms of information sharing and coordination, they conclude that effective supply chain integration requires not only information sharing, but also physical flow coordination, and that the magnitude of the benefits largely depends on the specific supply chain structures, demand patterns, and other operational characteristics.

From their studies of the role and effects of inter-organizational systems (IOS), IS researchers have proposed various categorization schemes and modes in order to systemize the different levels of external integration and their support for different types of supplier-buyer relationships (e.g. Choudhury, 1997; Massetti and Zmud, 1996; Mukhopadhyay and Kekre, 2002; Saeed et al., 2005). If an IOS is used to automate an existing communication process, its effects are limited to reducing manual data processing and improving the reliability as well as the timeliness of information (Hoogewegen and Wagenaar, 1996). As the firms progress to using IOS for closely coupling business processes between firms, they are able to realize additional benefits of vertical integration (Mukhopadhyay and Kekre, 2002; Saeed et al., 2005; Zhu et al., 2004). Hence, the use of IOS is considered most beneficial if applied in cooperative relationships (Chatfield and Yetton, 2000; Johnston and Vitale, 1988) and accompanied by process innovation such as vendor-managed inventory or continuous replenishment in the retail and consumer goods industries (Clark and Stoddard, 1996; Riggins and Mukhopadhyay, 1994). In accordance with the findings from operations management, IS researchers suggest that sharing “more” information is not necessarily “better” (Gosain et al., 2004; Premkumar, 2000). Gosain et al. (2004) recommend that organizations should prioritize their investments toward improving the quality of information shared with their business partners rather than sharing low-quality information in a broad variety of areas. According to Bensaou and Venkatraman (1996) and Kim et al. (2006), information processing capabilities need to fit a number of contextual factors, which are summarized as information processing needs, thus they call for a congruence of IOS design and the supply chain context.

Since IOS generate high setup costs and are associated with significant network effects, the use of open standards is claimed to be an important enabler for IOS-based interactions and to reduce the relationship specificity of the related investments (Gosain et al., 2003; Zhu et al., 2006). Given that the adoption of EDI-based standards (e.g., UN/EDIFACT or ANSI X.12) and the newer XML-based vertical industry standards (cf. Nurmilaakso et al., 2006) is not as widespread as originally hoped, this leads to a continuing debate about the way standards are created and adopted. While most of the literature focuses on the socio-technical phenomena related to standards development and diffusion, a relatively small research community has investigated the scope and limitations of the many domainspecific standards that have been launched over the last decades (Brousseau, 1994; Damsgaard and Truex, 2000; Kubicek, 1992; Reimers, 2001). Building on the semiotic structure of communication, they argue that the inherent difficulties of specifying machine-to-machine interactions hamper the migration of companies to higher levels of electronic process integration.

So far, both streams of research, i.e., operations management and IS research, closely relate information sharing to physical flow coordination and the related business processes. This is manifested by their focus on the transmission of customer demand signals, orders, the physical goods flow, capacities, and planning data. Existing research has given little attention to other types of information sharing problems, with the exception of Vermeer (2000), who argues that a poor context data quality negatively impacts the positive EDI effects on business processes. His studies draw attention to the concept of context interchange, which was introduced by Madnick (1995) and Goh et al. (1999) and has recently regained popularity in the context of the Semantic Web (Edgington et al., 2004; Zhao, 2007). It postulates that information transferred from a sending to a receiving system may be misinterpreted, since the systems usually operate in different contexts. To solve this problem, contexts need to be exchanged or aligned whenever changes in the sending or receiving systems occur.

## 2.3. Supply Chain Collaboration in the Retail and Consumer Goods Industries

The retail and consumer goods industries have reacted to the bullwhip effect by adopting the vision of Efficient Consumer Response (ECR). Introduced by Kurt Salmon Associates (1993) ECR is a strategy in which retailers, wholesalers, and suppliers act as one virtual entity, working together to reduce operating costs and inventories and improve supply chain performance (Corsten and Kumar, 2005; Reyes and Bhutta, 2005). Figure 1 outlines the two collaboration areas postulated by ECR. Whereas the focus of supply management is on streamlining the supply chain by improving product replenishment, demand management is aimed at creating and satisfying customer demand by optimizing product assortment strategies, promotions, and new product introductions (Dupre and Gruen, 2004). Demand-side and supply-side collaboration is supported by so-called integrators and enablers — most importantly, information technology and process improvement tools.

![](/api/attachments/2HW39XQZ/fulltext/images/2915e8c7a326b6c1f3f58374bfae5c5b252834ab3242ebabf3330606ece31ad6.jpg)  
Figure 1. ECR supply and demand chain model

In their literature review, Reyes and Bhutta (2005) identify a total of 775 articles on ECR and 170 publications in academic journals, which mostly deal with supply strategy choices (28.24 percent) and process coordination (21.76 percent). Whereas the positive effects of ECR have been demonstrated, studies on ECR adoption (Dupre and Gruen, 2004; Kurnia, 2000; Lohtia et al., 2004) reveal the lack of organizational and technological capabilities as major inhibitors to realizing ECR benefits. While the ECR concept relies on a seamless and accurate flow of information primarily achieved through electronic data interchange (EDI), there is empirical evidence that the quality of the underlying context information exchange directly affects the coordination of the demand and supply chain. According to Corsten and Gruen (2003), inaccurate product data records constitute one of the major root causes of out-of-stock-situations in retail stores, leading to a decrease in revenue. Other studies (Accenture, 2006; Global Commerce Initiative and Capgemini, 2005; Grocery Manufacturers of America et al., 2003) report significant direct labor costs due to the existing manual transfer of product information and its administrative processing as well as indirect effects of poor data quality on the supply and demand chain. Grocery Manufacturers of America et al. (2003) estimate that retailers may save between 5,000 and 10,000 hours per year in merchandising and data entry time dealing with new item introductions and updates. The same study reveals further savings of 1,000 to 2,000 hours per year in invoice verification and warehouse operations by eliminating data discrepancies. Additionally, efficient data alignment indirectly impacts revenue, given the fact that retailers and manufacturers are able to speed up their time-to-shelf in product introduction processes by 23 percent and 67 percent respectively (Accenture, 2006), ultimately resulting in an increase in sales.

As a consequence, industry initiatives have addressed the field of data synchronization, which denotes the process involving the timely updating of product data to maintain data consistency between retailers and manufacturers, under the umbrella of GS1<sup>2</sup>, ECR Europe (Hofstetter and

Jones, 2005), and the Global Commerce Initiative (GCI). Major outcomes of these initiatives are a set of technical standards (GS1, 2004; Nakatani et al., 2006) for product identification, description, and classification as well as message standards for electronic communication (cf. Table 1). The latter are available as EDI message types PROINQ (product information inquiry), PRODAT (product data), and PRICAT (pricing and sales catalog), which are part of the UN/EDIFACT subset EANCOM (Kotzab, 2005), or as platform-independent XML-based extensions of the EANCOM standard (GS1, 2005b).

<table><tr><td colspan="3">Table 1: Standards for Global Data Synchronization (GDS)</td></tr><tr><td colspan="3"></td></tr><tr><td>Coordination area</td><td>Standard</td><td>Description</td></tr><tr><td>Product identification</td><td>Global Trade Item Number (GTIN)</td><td>GTIN is 14-digit number used to uniquely identify a trade item so that it can be priced, ordered or invoiced at any point within the supply chain. It extends the former EAN//UCC codes.</td></tr><tr><td>Product classification</td><td>Global Product Classification (GPC)</td><td>GPC provides a set of common categories to group products globally. It defines a hierarchy, starting by industry sector or segments and going down to bricks as categories of like products.</td></tr><tr><td>Product description</td><td>Data Model for Trade Item</td><td>The data model for trade items defines core attributes for product description as well as extensions (e.g., for specific target markets or assortments).</td></tr><tr><td>Partner identification</td><td>Global Location Number (GLN)</td><td>GLN is a 13-digit unique location number which identifies physical, functional, logical or legal entities in a supply chain.</td></tr><tr><td>Message</td><td>EANCOM</td><td>EANCOM is an industry-specific subset of UN/EDIFACT standards which defines 47 electronic business documents in the following categories:master data (e.g., PROINQ / product information inquiry, PRODAT / product data, PRICAT / price and sales catalog)transactions (e.g., ORDER / purchase order, INVRPT / inventory report, DESADV / dispatch advice)planning and reporting (e.g., SLSFCT / sales forecast)other messages</td></tr><tr><td>Message</td><td>GS1 XML</td><td>GS1 XML is an extension of the EANCOM standard which defines XML-based business documents.</td></tr></table>

Since the bilateral exchange of product information based on message standards has proven to be costly and complex to realize with a larger number of business partners, data pools that reduce the number of bilateral interfaces and allow for many-to-many relationships between retailers and manufacturers have been promoted. As a specific type of industry exchange (Ordanini, 2005; Sparks and Wagner, 2003), data pools are operated by consortia of retail and consumer goods companies for collecting and redistributing product master data. By offering multiple interfacing technologies (e.g., EDI using PRICAT, XML, or web interface), a data pool eases integration and reduces entry barriers to electronic product data exchange. Examples of globally operating data pools are SINFOS (Germany) and U.S.-based companies Agentrics (merger of WWRE and GNX) and 1SYNC (merger of Transora and UCCnet). Since the number of data pools exceeds 25 worldwide (Schemm and Legner, 2008), network effects come into play, and data pools face start-up problems and excess inertia (Shapiro and Varian, 1998), which often prevent them from attracting critical mass. The Global Data Synchronization Network (GDSN) is targeted at establishing interoperability and federation between the data pools (Bowling et al., 2004; Nakatani et al., 2006): When product data is published at a GDSN-compliant data pool, it can be accessed from all other certified data pools based on the GS1 Global Registry (GS1, 2004), which acts as a global directory for the registration of items and parties. GDSN federates data pools and the global registry, and ensures interoperability by defining standards and protocols for synchronization. From a firm-level perspective, the synchronization of product master data with other organizations based on GDSN comprises seven steps (cf. Figure 2):

1. Preparation: The manufacturer prepares the product data according to GDSN standards.

2. Publication: The manufacturer loads product and company information into the GDSNcertified home data pool.

3. Registration: The manufacturer’s home data pool sends a subset of the product data (GLN, GTIN, GPC, target market and pool) to the GS1 Global Registry.

4. Search and subscription: The retailer searches for product information and subscribes to a seller's GLN, product category (GPC), target market or GTIN to receive the corresponding product and company information.

5. Identification of home data pool: By using the GS1 Global Registry, the data pool containing the requested item and location information is identified. The subscription is forwarded to that data pool.

6. Data synchronization: The manufacturer’s data pool then publishes the complete item and party information to the retailer’s data pool.

7. Receipt: The retailer obtains the subscribed product data via its home data pool.

![](/api/attachments/2HW39XQZ/fulltext/images/db8008a480b05a62889f26fdf0a47ceec03f14e47c176d268bd58c4c6edafdb0.jpg)  
Figure 2. Global exchange of product master data using the Global Data Synchronization Network (GDSN)

The process is also used to communicate changes and phase out information using a publish-andsubscribe mechanism. In December 2006, the Global Registry comprised approximately 10,800 GLNs and 1,161,000 GTINs (GS1, 2007) and grew to 15,000 GLNs and 1,990,000 GTINs by the end of 2007 (GS1, 2008). The coverage of the Global Registry seems to be relatively limited at present if we compare these figures to the total of 30,000 to 100,000 stock keeping units in an average retail store. The relatively slow adoption of GDSN and data pools, in general, is also underpinned by a recent survey of ECR adoption (Horst, 2007), which reveals that less than 6 percent of all master data records are exchanged via data pools and only 14 percent are exchanged electronically based on bilateral standard-based messages. This leads to the interesting questions of how the product information supply chain is organized today and whether GDS is to play a role in the future.

## 3. Research Framework

Prior studies on ECR collaboration (cf. Corsten and Kumar, 2005; Holweg et al., 2005; Kurnia and Johnston, 2003; Reyes and Bhutta, 2005), the bullwhip effect (cf. Aviv, 2001; Cohen Kulp et al., 2004; Gavirneni et al., 1999; Lee et al., 2000; Sahin and Robinson, 2002), and IOS (cf. Clark and Stoddard, 1996; Gosain et al., 2004; Saeed et al., 2005) are in agreement that supply chain inefficiencies are the result of information distortion and decentralized decision-making and that information sharing supports the effective coordination of the supply and demand chain. Based on the assessment of the existing body of research, the following section derives a conceptualization of the inter-organizational information supply chain in retailer-supplier relationships. It motivates the scope and focus of our research and outlines the research questions.

## 3.1. Transactional vs. Contextual Information Supply Chain

In applying the concept of the information supply chain to retailer-manufacturer relationships, two sets of information sharing and coordination problems can be identified. Sahin and Robertson (2002) draw attention to the transactional information flow (e.g., demand signals, forecasts, orders, shipping notifications, or invoices) that coordinates the inter-organizational supply and demand chain. Following Marinos (2005) and Sun and Yen (2005), the information supply chain comprises data production and consumption activities, but does not coincide with information sharing along the physical information supply chain. In the case of ECR, this would comprise the timely and accurate acquiring and updating of contextual information, which is a prerequisite for the correct interpretation of transactional supply and demand chain messages. For instance, an electronic order message contains at least a trading partner identification number and identification of the product to be delivered as well as the amount ordered and the accepted price. Manufacturer and retailer are only able to process the order message correctly if they maintain consistent partner and product information in their information systems. As an example, inconsistencies may occur if a manufacturer discontinues a certain product variant or changes the package size without disseminating the change to all trading partners.

Since both conceptualizations of the information supply chain are valuable in the context of ECR, we suggest distinguishing the transactional information supply chain (physical demand and supply chain) from the contextual information supply chain (product information supply chain), as depicted in Figure 3. While there is abundant literature on the effects of information sharing on the physical demand and supply chain and on the electronic communication of transactional data such as demand signals, forecasts, orders, and shipping notifications, little attention has been paid to the product information supply chain. From our literature assessment, there is increasing practical evidence that the interorganizational alignment of contextual information, notably product information, impacts the effectiveness of demand and supply chain coordination in ECR collaboration (Corsten and Gruen, 2003). Despite its practical relevance, the early stage of reasoning on the inter-organizational product information supply chain is reflected in a lack of models and definitions in the academic world. The latter will be the focus of our research.

## 3.2. Conceptualization of the Product Information Supply Chain

In the case of retailer and supplier collaboration, the most relevant context interchanges relate to product information, which is also referred to as master data. Compared to transactional data, master data (Chisholm, 2006; Russom, 2006; White et al., 2004) is considered as core data which that is needed to uniquely identify and describe business objects. It is infrequently changed, and often referenced, and usually used by various functions or units of an organization. Master data is organized in views which that group the attributes that are relevant to a specific function or organizational unit.

![](/api/attachments/2HW39XQZ/fulltext/images/f736126e65dbb60a983fbdfcdfc8946f3709dedb8aa425ce6d1cd5055e1b87c8.jpg)  
Figure 3. Transactional vs. contextual information supply chain

Prior research on information assets (Lee and Strong, 2003; Wang et al., 1998) allows us to deduce a process model of the product information supply chain at the firm level. Reflecting the life-cycle of information assets as well as the so-called data production processes, the master data-related business processes encompass information acquisition (sometimes also called collection), maintenance (sometimes also denoted as stewardship), and phase-out. These processes are performed internally on the side of both the requester (typically the retailer) and the provider (typically the manufacturer) and are supported by a number of software applications. In this context, master data management (MDM) or product information management (PIM) systems (Rugullies, 2004; White, 2005) are propagated as new application categories for managing product-related data, with dedicated functionality for master data distribution and enhanced workflow support. Alternatively, packaged Composite Applications (Woods, 2003) from vendors such as Logical Apps, Optura, MDQ Systems, or BackOffice Associates complement well-established ERP systems with functionality for data consolidation, workflow support, and monitoring of data quality (Swanton, 2006).

## 3.3. The Inter-organizational Product Information Supply Chain as a Coordination Problem

Prior research on the demand and supply chain emphasizes the interplay between coordination and information sharing among different organizations. Since information distortion and decentralized decision making also apply to the inter-organizational product information supply chain, we argue that information sharing and coordination problems exist between the product information-related activities on the retailer and manufacturer sides. Coordination theory (Malone and Crowston, 1994; March and Simon, 1958) seems to be the most promising of the different theoretical perspectives from which the phenomenon of the inter-organizational product information supply chain could be viewed. It has been used to analyze and redesign complex process interactions (Crowston, 1997; Iyer et al., 2006; Kraut and Streeter, 1995) and inter-organizational dependencies (Gosain et al., 2004; Tan and Sia,

2007). Coordination theory posits that dependencies exist among activities and defines coordination as the management of dependencies. When the activities performed by multiple individuals in different organizations need to interrelate in a synchronized fashion, these dependencies have to be effectively managed. Applied to the inter-organizational product information supply chain, this leads to the following research question:

Research question 1: What are the inter-organizational dependencies and coordination issues that retailers and manufacturers encounter in acquiring and consuming product information?

Coordination theory suggests dependencies can be managed by appropriate coordination mechanisms, notably the implementation of organizational structures (processes, task assignment) and information systems for supporting information processing activities. Thus, we are particularly interested in learning about the coordination mechanisms that retailers and manufacturers apply in today’s business environment.

Research question 2: To what extent do retailers and their suppliers manage the dependencies in the inter-organizational product information supply chain today, and which coordination mechanisms do they use?

In the context of ECR, industry standards and the emerging Global Data Synchronization Network (GDSN) have been promoted for multi-lateral product data exchange, but have failed to reach broader adoption so far. Therefore, we ask:

Research question 3: Given the current state of the inter-organizational product information supply chain, what issues arise and what conclusions can be drawn for the further adoption of GDSN?

## 4. Research Approach

Given the explorative character of our research, we adopted a case study research design. The following section motivates our research method and describes the different stages of our research process.

## 4.1. Research Method and Process

Due to the lack of prior research, our primary research goal is to understand and explain the various phenomena related to the inter-organizational information supply chain. (Gregor, 2006) classifies this type of research as the “Theory for Explaining (Type II).” Among the recommended research approaches for explaining how and why things happen in real-world situations are case studies, surveys, ethnographic, phenomenological and hermeneutic approaches, and interpretive field studies. We chose a case study approach, since it is particularly useful in cases where a contemporary phenomenon is studied in its natural context and where “research and theory are still at their early, formative stages” (Benbasat et al., 1987). Following a positivist approach (Orlikowski and Baroudi, 1991) and in accordance with Yin (2002), our research process consisted of the three stages:

1. Theory development and case study design (“define & design”): As prescribed by Yin (2002),<sup>3</sup> even exploratory case study research should make use of a conceptual framework to define the priorities to be explored. Thus, we started by reviewing the existing literature in order to construct a conceptual framework of the inter-organizational product information supply chain. In the context of our study, the use of a framework helped us make sense of occurrences, ensured that important issues were not overlooked, provided a set of constructs to be investigated, and guided our interpretation and focus.

2. Data collection (“prepare, collect & analyze”): We analyzed three companies, one retailer and two suppliers, resulting in two retailer-supplier relationships and allowing for withinand cross-case analysis.

3. Data analysis and conclusions (“analyze and conclude”): Based on the case study, we were able to draw conclusions with regard to the coordination problems and the current state of the product information supply chain as well as the role of GDSN standards and their adoption.

While case study research has been criticized for its lack of rigor, we closely followed the guidelines of building theory from case study research by Yin (2002) and Darke et al. (1998) to ensure the validity of this study.

## 4.2. Theory Development and Case Study Design

Building on the overarching framework of coordination theory (Malone and Crowston, 1994; March and Simon, 1958), we argue that the inter-organizational product information supply chain is characterized by a set of dependencies and needs to be explicitly managed. Our case study design was aimed at identifying and operationalizing the main constructs suggested by coordination theory, notably coordination problems (or dependencies), coordination mechanisms and coordination outcomes. Table 2 summarizes the main constructs from coordination theory and relates them to the inter-organizational product information supply chain.

Coordination problems can be differentiated according to the type of dependency on which they are based on (Crowston, 1997; Malone et al., 1999). While flow dependencies characterize sequential input-output relationships, sharing (or pooled) dependencies exist if activities use one common resource. In the most complicated form, the activities are dependent on each other (fit or reciproca dependencies). In order to identify the potential flow dependencies in the case of the interorganizational product information supply chain, we collected data about the various activities related to acquiring and consuming product information and their inter-organizational interactions. Since retailers and suppliers need to exchange contextual information, product information represents a common information resource. Unlike other resources, information resources are shareable and reusable as long as their specificity is low. Consequently, we had to analyze and compare the product data models in order to identify sharing dependencies.

Coordination theory has come up with generic coordination mechanisms, most importantly coordination by plan — i.e. pre-established schedules — and coordination by feedback, which involves the processing of new information (March and Simon, 1958). Since governance and coordination are more difficult between firms than within a single firm, this typology has been substantiated by Gosain et al. (2004) for the inter-enterprise setting. They propose “advance structuring” of inter-organizational processes and information exchange (coordination by plan) or “dynamic adjustment” through IT-supported learning and adaptation (coordination by feedback). The literature on ECR and GDSN (Nakatani et al., 2006) suggests a number of coordination mechanisms for product master data management, which can be classified as “advance structuring”, most importantly electronic integration (either as bilateral or as multilateral connections using data pools) and standardization. The transmission of structured product information in electronic form between retailers and manufacturers is said to improve process efficiency by facilitating the seamless flow of information between the different functional and organizational units and the real-time access to upto-date product information. The use of open standards, notably the ones depicted in Table 1, and the creation of the Global Data Synchronization Network (Figure 2), is claimed to reduce the variety of product data exchange specifications and to create positive network effects. Our case study design comprises additional coordination mechanisms that have been suggested for managing interorganizational dependencies, notably formal procedures and process coordination (Fleisch and Österle, 2000; Gosain et al., 2004).

For assessing coordination outcomes, coordination theory builds on concepts from transaction cost theory (Clemons et al., 1993; Malone et al., 1987; Premkumar, 2000; Saeed et al., 2005). It argues that high levels of coordination will allow a firm to gain process efficiencies in terms of reduced

<table><tr><td colspan="4">Table 2: Propositions from coordination theory</td></tr><tr><td>Constructs</td><td>Description</td><td>Relevance for the product information supply chain</td><td>Case study design and data collection</td></tr><tr><td>Coordination problems</td><td>Coordination problems can be classified according to the type of dependencies they are based on (Malone et al., 1999):Flow dependencies (sequential activities),Sharing dependencies (pooled resources),Fit dependencies (reciprocal).</td><td>Inter-organizational dependencies are possiblebetween product information related activities (flow dependencies),due to multiple activities using a common product information resource (sharing dependencies).</td><td>Process analysis:Internal master data processes and their inter-organizational dependencies;Analysis of product data models: Degree of information sharing and information specificity.</td></tr><tr><td>Coordination mechanisms</td><td>According to (March and Simon, 1958), generic coordination mechanisms include:Coordination by plan,Coordination by feedback.(Gosain et al., 2004) substantiate these main coordination mechanisms for inter-organizational relationships:&#x27;Advance structuring&#x27; of inter-organizational processes and information exchange,&#x27;Dynamic adjustment&#x27; through IT-supported learning and adaptation.</td><td>Existing studies on ECR and GDSN suggest the following coordination mechanisms which can be classified as &#x27;advance structuring&#x27;:Electronic integration (bilateral or multilateral / data pools),Standardization (GDSN),Other possible coordination mechanisms include common process specifications.</td><td>Common process specifications:Definition and implementation of master data processes;Electronic integration: level of electronic integration of master data systems;Standardization: use and appropriateness of GDSN standards.</td></tr><tr><td>Coordination outcome</td><td>Higher levels of coordination result in decreased coordination costs (or transaction costs) and operations risks, and in improved decision-making</td><td>Coordination outcomes are likely to affect two levels:Product information supply chain,Physical demand and supply chain.</td><td>Effects of lacking coordination are assessed at two levels:Product information supply chain,Physical demand and supply chain.</td></tr></table>

outdated or wrong product information in the context of ECR at two levels: the inter-organizational product information supply chain as well as the physical demand and supply chain.

## 4.3. Case Sites and Data Collection

Case selection was mainly driven by purposeful sampling, availability of multiple sources of information, and the willingness to cooperate. In order to ensure the generalizability of our research, we selected cases that are to be considered representative of the prevailing forms of retailer-supplier collaboration and allow for replication: (1) The companies represent major players within the retailer and consumer goods industries; (2) The assortment under consideration consists of non-fashion products with a relatively stable demand and medium shelf-life, thus reflecting product characteristics that, according to Holweg et al. (2005), are conducive to more intensive forms of supply chain collaboration; (3) The companies are involved in reciprocal business relationships, representing different types of retail-supplier relationships with different intensities of demand and supply chain collaboration; (4) Due to their size and their market positioning, the companies are able to shape the inter-organizational product information supply chain and do not merely assume the passive role of “adopters;” (5) The companies have been intensively investigating GDSN implementation and thus are considered knowledgeable of GDSN concepts.

The resulting case sites are depicted in Table 3: We selected a retailer that is the market leader in a medium-sized European country and two suppliers of non-food articles that are global players. Supplier 1 acts in a traditional buyer-supplier relationship for branded products and has entered into a supply chain collaboration (vendor-managed inventory) with the retailer. With a contribution of 10 percent of all articles to the retailer’s cosmetics and personal care assortment, Supplier 1 represents a key supplier. Supplier 2 produces private label articles (adhesives) under the retailer’s brand. Despite the very limited number of articles, the high and stable revenues associated with these products make this firm a main supplier within this assortment.

<table><tr><td colspan="4">Table 3: Overview of case studies</td></tr><tr><td colspan="4"></td></tr><tr><td colspan="4">Unit of analysis: Firm level</td></tr><tr><td></td><td>Retailer</td><td>Supplier 1</td><td>Supplier 2</td></tr><tr><td>Revenues (2005)</td><td>approx. EUR 11.2 bn</td><td>approx. EUR 12 bn</td><td>approx. EUR 4.7 bn</td></tr><tr><td>Employees</td><td>approx. 80,000</td><td>approx. 50,000</td><td>approx. 17,000</td></tr><tr><td>Geographical focus</td><td>National (Europe)</td><td>Global</td><td>Global</td></tr><tr><td>Product portfolio / assortment</td><td>FoodNon-foodElectronicsSports equipmentHardware / toolsFurniture</td><td>DetergentsCosmetics / personal careAdhesives</td><td>Cosmetics / personal careAdhesives</td></tr><tr><td>Number of interviewees per function</td><td>CategoryManagement (2)InformationTechnology (2)Logistics (3)</td><td>InformationTechnology (2)Material Management(Global) (1)Supply ChainManagement (1)</td><td>InformationTechnology (2)Local Sales (2)Logistics (1)Material Management(Global &amp; Local) (3)</td></tr><tr><td colspan="4"></td></tr><tr><td colspan="4">Unit of analysis: Retailer – supplier relationship</td></tr><tr><td></td><td colspan="2">Retailer – Supplier 1</td><td>Retailer – Supplier 2</td></tr><tr><td>Number of articles</td><td colspan="2">40 articles (adhesives)</td><td>540 articles (cosmetics, personal care)</td></tr><tr><td>% of total assortment (retailer)</td><td colspan="2">0.2%</td><td>10%</td></tr><tr><td>Assortment characteristics</td><td colspan="2">Private label articlesStable assortment</td><td>Branded articlesShort product innovation cycles</td></tr><tr><td>ECR collaboration</td><td colspan="2">Joint product definition (private label)Buyer managed inventory (BMI)</td><td>Vendor managed inventory (VMI)</td></tr><tr><td colspan="4"></td></tr></table>

In view of our research objective, case studies have been conducted at two levels of analysis: at the firm level and at the level of the business relationship. As company representatives tend to have an internal view of the product information supply chain and ignore the inter-organizationa dependencies, significant efforts were necessary in order to gather data related to the interorganizational product information supply chain. Consequently, data collection involved the following steps:

1. During an initial one-day workshop, company representatives presented an overview of their internal product information supply chain (master data processes and systems, GDS adoption) and were introduced to the concept of the inter-organizational product information supply chain (Figure 3).

2. During several on-site interviews and individual workshops with every company, we studied their internal information supply chain and its external integration. On average, we spent two full days per company working with the on-site experts. We documented the results of this analysis in the form of process models, data models, and depictions of the IS architecture, and collected additional quantitative data.

3. We conducted a one-day workshop with representatives from all companies in order to assemble their partial views into a consolidated view on the inter-organizational information supply chain.

4. We identified and clarified several issues requiring further investigation through by telephone interviews with the appropriate experts.

5. Finally, we consolidated the documentation and findings and allowed all participants to review them. The results include individual documentations of the product information supply chain at the firm level as well as a documentation of the inter-organizational coordination in the two retailer-supplier relationships.

Data validity was ensured through multiple sources of evidence, reviews of case interpretations by interviewees, and a chain of evidence provided by the case data. We shared our developing theories and conceptualizations with the company representatives. As we identified constructs and created theoretical frameworks, we sought clarification from the data, which, in turn, led to further theory development (Yin, 2002). In order to validate our findings and ensure generalizability, we reviewed recent studies and the outcomes of GS1 standardization initiatives and conducted further interviews with industry experts.

## 5. Case Study Analysis

## 5.1. Flow Dependencies in the Inter-Organizational Product Information Supply Chain

Prior to our documentation of the inter-organizational process, the companies did not have visibility into the interdependencies between their internal product information supply chains, even if they were aware of their existence due to some obvious coordination problems. They were lacking a broader understanding of the temporal sequence of product information requirements on the retailer side and the interdependencies between the retail and manufacturer processes. As an example, the manufacturer was not aware at which point in time the retailer needed which product master data attributes, at what level of detail, and in what quantity. Based on the analysis of the actual interactions, we derived activity chains that depict the inter-organizational process flow in the as-is situation (cf. Figure 4).

On both the retailer and consumer goods company sides several functional units are involved along the entire product information supply chain, including central and regional or local units. Both manufacturers have appointed a central organization for master data management, but regional production, sales, and distribution units are responsible for the supplementation and maintenance of local data. On the retailer side, responsibilities are split between the category management, materials management, and a master data management unit. These shared responsibilities reflect the global structure of the business with central-decentral coordination,<sup>4</sup> which for the two globally operating consumer goods companies can be characterized as an “international” (Marchand, 2004) or a “transnational / integrated network” (Karimi and Konsynski, 1991).

![](/api/attachments/2HW39XQZ/fulltext/images/fb934a52c20384d082f3e3649a74f2601a51554859d2bb6a88686cc264a0d595.jpg)  
Legend: MDM = Master Data Management, CM = Category Management  
Figure 4. Product master data acquisition – inter-organizational process flow (here: branded articles operated by vendor managed inventory, VMI)

Although intuitively perceived as a single-step activity, the acquisition of product information involves multiple interactions between manufacturer and retailer. Due to the strong coupling with demand chain activities, the entire process spans a period of three to six months. It starts as early as in the assortment phase, when the retailer decides on which products it is to make available to consumers and how to best use the limited selling space. When evaluating and redefining the product assortment, category managers collect information about new products (e.g., by organizing product presentations or contacting suppliers with a request for quotations). Once the assortment has been defined, the category management unit prepares the introduction of the listed products in the stores and requests logistics data from the manufacturer. Subsequently, category management and further internal units add retailer-specific attributes, among them procurement, logistics, and sales data. In the case of VMI, the supplier takes responsibility for maintaining the retailer’s inventory. This implies that an additional transfer back to the manufacturer takes place, which comprises a set of listing data such as the number of receiving stores and initial demand volumes.

<table><tr><td colspan="5">Table 4: Phases and intensity of product master data acquisition</td></tr><tr><td>Process phase</td><td>Product master data views</td><td>Product attributes (examples)</td><td># of attributes provided by supplier</td><td># of attributes provided by retailer</td></tr><tr><td rowspan="2">Assortment planning(#1 in Figure 4 and Figure 5)</td><td>Basic Data</td><td>GTIN, Quantity, Relation Consumer Unit (CU) to Trade Unit (TU)</td><td>4*</td><td>-</td></tr><tr><td>Procurement Data</td><td>Purchase Price</td><td>1</td><td>-</td></tr><tr><td rowspan="6">Product introduction(Provision of logistics data by supplier / #2 in Figure 4 and Figure 5)</td><td>Basic Data</td><td>Depth, Width, Height</td><td>9*</td><td></td></tr><tr><td>Logistics Data</td><td>Customs Tariff Number, Country of Origin</td><td>4</td><td>-</td></tr><tr><td>Sales Data</td><td>Currency, Tax Rate</td><td>2</td><td></td></tr><tr><td>Dangerous Goods Data</td><td>Poisonous category, Dangerous Goods Code</td><td>7</td><td>-</td></tr><tr><td>Dates</td><td>Production Date, Sales Date</td><td>4</td><td>-</td></tr><tr><td>Returnable Packaging Data</td><td>Returnable Packaging, Content</td><td>2</td><td></td></tr><tr><td rowspan="7">Product introduction(Data supplementation through retailer / #3 in Figure 4 and Figure 5)</td><td>Basic Data</td><td>Trade Item No. Retailer, Category Code, Incoterms</td><td>-</td><td>12*</td></tr><tr><td>Procurement Data</td><td>Purchase Key, Standard Delivery Time</td><td>-</td><td>3</td></tr><tr><td>Logistics Data</td><td>Incoming Distribution Center, Outgoing Distribution Center</td><td>-</td><td>3</td></tr><tr><td>Sales Data</td><td>Wholesale Price, Brand</td><td>-</td><td>3</td></tr><tr><td>POS Data</td><td>Cash Register Text, Returnable Deposit?</td><td>-</td><td>5</td></tr><tr><td>Listing Data</td><td>Category Layer National, Category Layer Regional</td><td></td><td>3</td></tr><tr><td>Dates</td><td>Limit Type, Time Limit 1</td><td></td><td>5</td></tr><tr><td>Product introduction(Provision of distribution data by retailer / #4 in Figure 4 and Figure 5)</td><td>Listing Data</td><td>Listing Date, Initial Stock Quantities</td><td>-</td><td>4</td></tr><tr><td colspan="3">Total number of attributes</td><td>33*</td><td>38*</td></tr><tr><td colspan="5">*May vary by assortment (depending on trade item structure and number of logistic units)</td></tr></table>

Whereas Figure 4 depicts the activity chain for the case of branded articles operated by vendor managed inventory, Table 4 summarizes the number of attributes that are exchanged and the temporal sequence. From this analysis, we can further characterize the inter-organizational dependencies related to product master data acquisition: While in the early phase, the retailer requests basic product and price information for planning the assortment, the latter interactions prepare the market introduction and transfer the full set of product data required for running purchasing, logistics, distribution, and sales processes.

Hence, the VMI scenario that represents an example of a more intensive form of ECR collaboration generates additional requirements with regard to context interchange, in comparison with the traditional retailer-manufacturer relationship. In the case of private label products, which are not depicted here, the retailer determines the key characteristics of the product and transfers them to potential suppliers. This changes the activity chain for product master data acquisition as follows: The initial transfer of product data (#1 product presentation in Figure 4) is replaced by the retailer’s request for a quotation, resulting in a transfer from retailer to supplier.

Since product information is initially acquired when a new product is introduced to the assortment, this process is typically performed once. Its frequency depends on the product innovation cycle, which is significantly higher in the case of Supplier 2 (250 new products in 12 months) than in the case of Supplier 1 (two new products in 12 months). Updates of existing product information may be necessary when the product changes. In the two retailer-supplier relationships, four different process variants have been identified: (1) smaller changes (e.g., in product composition or packaging) which do not affect the retailer or the consumer and are occasionally communicated by the supplier; (2) significant changes (e.g., change of product name, significant changes in packaging, specific product promotions) that need to be communicated in advance from the supplier to the retailer and result in the relaunch of the product; (3) changes of logistic units by the supplier, which require that a new GTIN is attributed; (4) changes in sales information that are determined by the retailer and need to be communicated to the supplier for packaging and labeling.

## 5.2. Sharing Dependencies in the Inter-organizational Product Information Supply Chain

The inter-organizational product information supply chain relies on product information as a shared resource. Figure 5 depicts the product data model used by the retailer in the non-food assortment and indicates whether the information is acquired from the supplier or generated internally. The entire set of product data consists of 71 attributes that are organized in several views. While basic data such as product name and number are typically needed by all functions, other views represent information that is specific to single functions such as the logistics or category management units. From Figure 5 it is also evident that only a subset of the retailer’s overall product information requirements can be fulfilled by the manufacturers. While 33 of the 71 attributes are requested from the suppliers, the rest (e.g., internal disposition and marketing data) have to be supplemented by internal units. These attributes are retailer-specific, since they comprise attributes that are steering the internal sales, marketing, and logistics processes.

## 5.3. Coordination Mechanisms

## Process Specifications

At the firm level, the retailer and the manufacturers have defined organizational responsibilities as well as their internal master data processes, as outlined in the conceptual model (i.e., acquire, maintain / update and phase out). As shown in Table 5, the internal information acquisition process can be considered the most mature, whereas companies admit that the other two processes are not yet fully implemented. Only Supplier 1 has recently designed these processes. While process specifications are used as coordination mechanisms at the firm level, coordination mechanisms at the inter-enterprise level reflect the power distribution in the retail-supplier collaboration. While the retailer imposes certain procedures for master data acquisition on its suppliers, the suppliers merely react to the requests from the retailer, typically a request to fill in product information in a spreadsheet form (“product passport"). Inter-organizational update and phase-out processes were not defined at all.

![](/api/attachments/2HW39XQZ/fulltext/images/4d80f95098436ec3d3b6af091170b84205ba71e9ecb044d70d7f9f05ffdf1730.jpg)  
Figure 5. Product master data model and views (retailer side)

<table><tr><td colspan="4">Table 5: Coordination mechanisms - process specifications</td></tr><tr><td colspan="4"></td></tr><tr><td></td><td>Retailer</td><td>Supplier 1</td><td>Supplier 2</td></tr><tr><td colspan="4">Internal master data processes</td></tr><tr><td>- Acquire</td><td>+</td><td>+</td><td>+</td></tr><tr><td>- Maintain / update</td><td>0</td><td>+</td><td>0</td></tr><tr><td>- Phase out</td><td>0</td><td>+</td><td>0</td></tr><tr><td colspan="4">Inter-organizational master data processes</td></tr><tr><td></td><td>(imposing internal processes on suppliers)</td><td>(responding to retailers’ requests)</td><td>(responding to retailers’ requests)</td></tr><tr><td>- Acquire</td><td>-</td><td>-</td><td>-</td></tr><tr><td>- Maintain / update</td><td>-</td><td>-</td><td>-</td></tr><tr><td>- Phase out</td><td></td><td>-</td><td>-</td></tr><tr><td colspan="4">+ (defined and implemented), o (partly defined and implemented), - (not defined, not implemented)</td></tr></table>

With regard to IS support, the retailer and its suppliers have only recently defined a single, central information system that distributes product information to the regional or local ERP, and to the warehouse or store systems, respectively. Internal master data distribution reflects the structure of the business as well as the grown application landscape: As depicted in Table 6, manufacturers maintain global product information (i.e., those attributes are either used by global processes (e.g., product development) or by several local processes (e.g., logistics)) in a centralized master data system. Typically, this master data system corresponds to an instance of an ERP system that is specifically designed to administrate global attributes, such as product numbers, descriptions, and classifications. It regularly distributes global master data to the local ERP systems that support the production and sales units. These units supplement the global master data attributes with further local attributes, such as prices and conditions or logistics information for managing specific local processes.

<table><tr><td colspan="4">Table 6: Coordination mechanisms - electronic integration</td></tr><tr><td></td><td>Retailer</td><td>Supplier 1</td><td>Supplier 2</td></tr><tr><td colspan="4">Internal electronic integration</td></tr><tr><td>Master data system</td><td>+(Central ERP system)</td><td>+(Dedicated ERP system)</td><td>+(Dedicated ERP system)</td></tr><tr><td>Internal master data distribution</td><td>+</td><td>+</td><td>+</td></tr><tr><td>Electronic workflows</td><td>o / -(Spreadsheets)</td><td>+(Collaboration tool / Workflow)</td><td>o / -</td></tr><tr><td colspan="4">Inter-organizational electronic integration</td></tr><tr><td>Electronic integration</td><td>Mainly human-to-human (e-mail, xls), limited use of human-to-machine (Portal), limited use of machine-to-machine (EDI).</td><td>Mainly human-to-human (e-mail, xls)</td><td>Mainly human-human (e-mail, xls)</td></tr><tr><td>Data pools</td><td>Evaluating pool solution</td><td>Partly national data pools; plans to implement GDSN</td><td>Partly national data pools; plans to implement GDSN</td></tr><tr><td colspan="4">+ (defined and implemented), o (partly defined and implemented), - (not defined, not implemented)</td></tr></table>

A similar situation characterizes the retail side: Global master data is kept in the central ERP system, which further distributes a subset of the global product master data to the local warehouse and store systems. In contrast to the consumer goods companies, the retail company establishes a much higher degree of centralization with a significantly higher percentage of global master data attributes.

Despite the internal efforts, the level of external integration is still low. The investigated companies transfer spreadsheets in order to exchange master data across the organizational boundaries, as depicted in Figure 6. On the retailer side, category management defines templates for collecting product information, which are sent out to the suppliers via e-mail. They supplement the product information provided by the manufacturer with additional information and manually consolidate data from different manufacturers before entering it into the central ERP system. On the manufacturer side, the two companies are already connected to national data pools in selected countries, but in the existing customer relationship, manual data transfer prevails. For this purpose, sales representatives transfer all retailer-relevant master data attributes into specific databases that are then used to extract the required product information according to the retailer-specific templates.

## Standardization

From the range of GDS standards that are outlined in Table 1, our investigation demonstrates the wide use of standards only for the area of product and partner identification. While GTINs and GLNs are consistently used in both retailer-manufacturer relationships, higher-level product description and message standards are not applied. When communicating product information via spreadsheets, the companies do not rely on the harmonized trade item model suggested by GDS, but use the retailer’s proprietary data model. Interestingly, the studied retailer requests only 33 master data attributes

![](/api/attachments/2HW39XQZ/fulltext/images/45a1353ee710bf893b30424df03819b180a543585056a6c35a2065941ad3324b.jpg)  
Figure 6. Product master data creation – information flow in the as-is situation

directly from the manufacturer, while the data model for trade items currently comprises 11 core attributes and approximately 200 further attributes (GS1, 2005a; GS1, 2005b), without counting the existing category-specific extensions and several attributes pending on their way through the standardization process.

This leads to the question of why neither the bilateral product data exchange (based on GDS message standards) nor the multilateral product data exchange based on data pools is implemented. All companies admit difficulties in calculating the business case for GDSN, given the significant setup costs for electronic integration. However, they also express their doubts as to whether the current set of standards and the GDS concept adequately addresses the coordination problems of the interorganizational product information supply chain. By defining the publish-and-subscribe mechanism, GDSN describes the basic principles of acquiring product master data, but many questions remain: As outlined in Figure 4, rather than transferring product data once (en bloc), different subsets of product data are exchanged in multiple interactions. Product data are subsequently collected, transferred, and supplemented, starting from the phase of product assortment planning. While the acquisition process is usually initiated and dictated by the retailer, the change and phase-out processes are much more complex and currently not defined at all by GDS. In addition, GDS has not created business standards or rules underlying the inter-organizational product information supply chain. There are no formal agreements that define and assign the responsibilities of the business partners, outline provisions for error handling (e.g., in the case of outdated or wrong product data), and define the quality of service.

Table 7: Coordination mechanism – GDS standards

<table><tr><td>Coordination area</td><td>GDS standard</td><td>Adoption</td><td>Type of dependency that is addressed</td></tr><tr><td>Product identification</td><td>Global Trade Item Number (GTIN)</td><td>+</td><td>Sharing dependency</td></tr><tr><td>Product classification</td><td>Global Product Classification (GPC)</td><td>-</td><td>Sharing dependency</td></tr><tr><td>Product description</td><td>Data Model for Trade Item</td><td>-</td><td>Sharing dependency</td></tr><tr><td>Partner identification</td><td>Global Location Number (GLN)</td><td>+</td><td>Sharing dependency</td></tr><tr><td>Message</td><td>EANCOM</td><td>o</td><td>Flow dependency</td></tr><tr><td>Message</td><td>GS1 XML</td><td>-</td><td>Flow dependency</td></tr><tr><td colspan="4">+ (consistently used in both retailer-manufacturer relationships)o (not applied in the two retailer-manufacturer relationships, but used by the retailer or manufacturers)- (not applied, neither by the retailer nor by the manufacturers)</td></tr></table>

## Coordination Outcomes

Figure 7 illustrates the effects of coordination of the inter-organizational product information supply chain. Since all three companies are only beginning to improve inter-organizational coordination, impact assessment is based on projections from the as-is situation. As of today, manual efforts for master data administration are high, notably on the supplier side. For this particular retailer relationship, both manufacturers estimate savings of roughly 0.1 full-time equivalents (FTE) in sales personnel and 0.2 FTE in VMI disposition personnel due to automated transformation (between the different product data models) and electronic data distribution.

Whereas improved coordination directly impacts the transaction costs in the product information supply chain, coordination problems, such as time lags in propagating product information changes, affect the quality of the stored information and, thereby, the effectiveness of demand and supply chain coordination. Although all companies support this argumentation, the resulting effects on the physical demand and supply chain are more difficult to trace in the concrete scenario. With regard to the replenishment processes, 50 percent of the occurring EDI errors in the as-is-situation are caused by inadequate alignment of master data with manufacturers, leading to various forms of errors in the streamlined demand and supply chain processes. The analysis of EDI error protocols reveals that these are most frequently errors in basic product data (e.g., GTIN not attributed), ordering errors (wrong procurement and supplier data, e.g., wrong price), listing errors (non-existing product master data record), and logistics data errors (lacking logistics attributes). The lack of coordination is particularly harmful in the case of changes (e.g., if manufacturers do not know whether or not to communicate a minor change in package size that may cause product overhang and hamper transport or logistics operations in the retail store). Master data problems are also the reason for 50 percent of the invoice discrepancies that have to be manually resolved by the retailer.

On the demand side, the retailer and its suppliers expect a streamlined product information supply chain to accelerate product introduction times and to increase revenue. In some assortments notably fast-moving goods like DVDs and games that are not yet managed on an item-level basis — the higher quality of master data allows for a more concise reporting and planning of marketing activities, ultimately resulting in a faster response to customer demand and higher on-shelf availability. However, both effects are not measurable for the two retailer-supplier relationships.

![](/api/attachments/2HW39XQZ/fulltext/images/29767c5bc9c56f836b1b718282df6fb4fdb26cbd85916cdfe4d898ed0be3f7cd.jpg)

## 6. Findings and Discussion

In this section, we answer our research questions and discuss the findings in the context of the existing IOS literature. In order to demonstrate how our analysis might generalize, we have derived seven statements that characterize the inter-organizational product information supply chain in the retail and consumer goods industries (c.f. Figure 8). We acknowledge that our analysis represents a “snap-shot” given the fact that new technologies are evolving and that the industrial environment is constantly changing. However, we feel that these statements might be useful to frame future research activities and to conduct further empirical and longitudinal studies.

## 6.1. Dependencies and Coordination Problems in the Inter-Organizational Product Information Supply Chain

Our case study analysis confirms our view of the inter-organizational product information supply chain between retailers and manufacturers as a coordination problem. Although the product-information supply chain is intuitively perceived as a simple single-step interaction, the case studies reveal significant flow dependencies between the master data processes on the retailer and supplier sides.

Dependencies in product information acquisition are due to the fact that product information is generated by suppliers when launching a new product on the market and acquired by retailers in several steps during assortment planning and product introduction. While our study clearly demonstrates the existence of flow dependencies, it finds that sharing dependencies only exist for the smaller subset of product data attributes that are not retailer- or supplier-specific. Since more than 50 percent of the product information attributes are required to steer internal processes, information specificity (Choudhury and Sampler, 1997) even plays for mass-market consumer goods.

(1) The inter-organizational product information supply chain is characterized by flow and sharing dependencies.

![](/api/attachments/2HW39XQZ/fulltext/images/e695c96442461075c7af32c146d9d846611189dc51ccb0d606b70a85f9bad71c.jpg)

Compared with traditional retailer-supplier relationships, the flow of product information-related interactions changes with higher levels of ECR collaboration. Whereas the VMI scenario requires additional logistics data to be transferred from retailer to supplier, private labels imply joint product definition and the determination of key product characteristics by the retailer (c.f. Table 8).

(2) Flow and sharing dependencies evolve into reciprocal dependencies with the increasing intensity of demand and supply chain collaboration.

<table><tr><td colspan="4"></td></tr><tr><td></td><td>(1) Traditional retailer-manufacturer relationship</td><td>(2) ECR / Supply management: Vendor managed inventory</td><td>(3) ECR / Demand management: Private labels</td></tr><tr><td>Flow dependencies</td><td>→ (product presentation)→ (quotation)→ (listing data)</td><td>→ (product presentation)→ (quotation)→ (listing data)← (VMI data)</td><td>← (product requirements)→ (quotation)→ (listing data)</td></tr><tr><td>Sharing dependencies</td><td>29 (out of 71) attributes</td><td>33 (out of 71) attributes</td><td>&gt;29 (out of 71) attributes (retailer-specific)</td></tr><tr><td colspan="4">Legend: → (flow from manufacturer to retailer), ← (flow from retailer to manufacturer)</td></tr></table>

## 6.2. Status of the Inter-Organizational Product Information Supply Chain

Both retailer-supplier relationships rely on ECR concepts and heavily use EDI in the transactional processes. While the companies in our study have carefully designed their demand and supply chain processes, they still lack a thorough understanding of the inter-organizational dependencies in the product information supply chain. As demonstrated by the EDI error protocols, the lacking of coordination affects the transactional information flow, thus putting the electronic coordination of demand and supply chain at risk.

(3) Inter-organizational dependencies in the acquisition and consumption of product information are still largely unknown to retailers and their suppliers, although the effects of coordination problems are measurable. We conclude that the inter-organizational product

With regard to coordination mechanisms, companies have so far focused on streamlining their internal product information supply chain by setting up master data processes and defining their master data architecture. Interaction with external partners is mostly initiated by the retailer in a dyadic relationship. Since the effects of coordination problems are more significant on the retailer side, the retailer has started to define procedures for acquiring product information from its suppliers, thus pursuing “advanced structuring.” Both suppliers simply react to the retailer’s requirements, which can be characterized as an “adapt and sense” strategy.

(4) Similar to demand and supply chain coordination, retailers will increasingly impose coordination mechanisms, notably formal procedures and instruments for acquiring product information, on their suppliers.

As with process coordination, external electronic integration is still at an early stage. Companies have created an internal “single point of truth” by implementing a central master data system that distributes master data to local systems. Although manufacturers have made provision for external integration by connecting to selected home data pools, manual transfer of product data prevails with a high penetration of spreadsheets as an instrument for inter-organizational product data exchange. This is partly due to the difficulties in justifying the rationale for tighter electronic integration, given the relatively infrequent interactions, as documented in the two retailer-manufacturer relationships. The penetration of spreadsheets as an instrument for inter-organizational product data exchange also underlines the requirements for flexibility and usability of master data-related applications. The future electronic support of the inter-organizational product information supply chain requires the connectivity of internal master data systems with those of the external partners to be so user-friendly and flexible that sales assistants, purchasers, etc. accept its use in their daily work.

(5) Several factors restrict the adoption of EDI- or XML-based integration in the interorganizational product information supply chain: (a) the level of internal integration and harmonization of master data, (b) end-user requirements related to the flexibility and usability of electronic product information exchange, and (c) the relatively low frequency of interactions for aligning contextual information in comparison to the transactional information flow.

## 6.3. Role and Adoption of GDSN

With regard to inter-organizational standardization, GDS is currently promoted as the most promising approach for achieving many-to-many relationships between the retail and consumer goods industries. Despite the popularity of the concept, our study reveals some shortcomings of GDS as a coordination mechanism in the inter-organizational product information supply chain.

While GDS has focused on the sharing of product information by specifying the trade item data model, it has paid little attention to the flow dependencies in product data acquisition and consumption. GDS conceives a simple catalog-type product information exchange, but the actual interactions are more frequent and more difficult to specify than foreseen by standards and data pools. From our analysis, there is evidence that the publish-and-subscribe pattern for product data as well as the existing message standards do not address the more complicated flow dependencies that result from increasing ECR collaboration. This situation is highly reminiscent of past experiences with IOS and the difficulties in setting up standards on the pragmatic level (Reimers, 2001).

(6) Today, GDS standards exclusively comprise coordination mechanisms for sharing dependencies, notably the global trade item data model. In order to successfully address the coordination issues of the inter-organizational product information supply chain, GDS has to address flow dependencies. This implies that “public master data processes” are specified and supported by appropriate message standards.

Although the case study analysis confirmed the value of higher levels of coordination in the product information supply chain, our investigation also reveals important factors that hinder GDS adoption. Given the current state of the internal product information supply chain, implementation of GDS requires substantial investments in process redesign and technical infrastructure, quite apart from the significant subscription fees to the home data pool and to GDSN. Our findings are consistent with studies by Iacovou et al. (1995) and Zhu et al. (2006), which not only explain standard diffusion by network effects and perceived benefits, but identify adoption costs and the lack of organizational readiness as major inhibitors in the adoption of open standards. Besides the significant financial investments, which have been outlined earlier, the managerial complexity is, by far, the more influential barrier to GDS adoption. Grown business processes and system landscapes do reflect the internal business structure, but are not prepared to meet the needs of a global inter-organizational product information supply chain. In order to lay the foundations for implementing the GDS concept, companies need to (re-)design their internal data and application landscapes as well as their interna workflows for coupling them with the inter-organizational information supply chain. From the perspective of a global manufacturer, significant challenges arise, since the responsibility for a large portion of the product master data items lies in the hands of the local production and sales units. If a global home data pool, as envisioned by the GDSN, has to be served, a centralization of local master data attributes will be necessary, at least virtually. To summarize,

(7) Given the current state of the internal product information supply chain, adoption costs are an important barrier to GDS implementation. The extent of the preparatory projects for harmonizing the internal product information architecture on an enterprise-wide scale is so large that adoption might be very slow or may even fail.

## 7. Summary and Outlook

## 7.1. Research Contribution

Prior research has primarily considered the effects of information sharing along the supply chain, but no study has systematically investigated the contextual information flow. This paper contributes to filling this gap by deriving a conceptual model of the inter-organizational product information supply chain between retailers and manufacturers, which builds on context interchange and coordination theory. Our research suggests that the product information supply chain maintains contextual information that is relevant to the supply chain partners in transactional ECR processes. By analyzing product master data exchange in two retailer-manufacturer relationships, we have been able to characterize the inter-organizational product information supply chain by a set of dependencies, coordination problems, and coordination mechanisms.

An important contribution of our research is the identification of flow and sharing dependencies that are the root cause of coordination problems in today’s inter-organizational product information supply chains. We have found that these dependencies evolve into reciprocal dependencies as the intensity of demand and supply collaboration increases. Although the effects of the associated coordination problems have been measurable in both retailer-supplier relationships, the inter-organizationa product information supply chain is still far less structured and managed than the physical supply and demand chain. This is partly due to the fact that companies are still in the process of setting up appropriate coordination mechanisms for managing their internal product information supply chain. However, existing and emerging industry standardization, notably GDS, does not yet adequately cover the inter-organizational coordination requirements that result from the identified set of sharing and flow dependencies. In accordance with studies on IOS adoption (Iacovou et al., 1995; Zhu et al., 2006), our research reveals that GDS-based electronic integration is associated with significant adoption costs, given the current state of the internal product information supply chain.

## 7.2. Limitations and Future Fields for Research

There are several limitations to our research. As in all case study research designs, the most important one lies in the limited empirical basis, which involves the risk of focusing on unique conditions and events, rather than on general concepts and trends. We tried to minimize this risk by basing our analysis on prior theoretical findings from IOS research, by triangulating our results against the most recent industry statistics issued by GS1, and by validating our findings in expert interviews. Given the popularity of the GDSN concept, the selection of three cases that reflect the situation prior to GDSN implementation might seem arbitrary at first sight. However, case sites reflect the vast majority of firms that are still in the process of evaluating GDSN (Horst, 2007) and provide valuable insights into the “real” issues related to the design of the inter-organizational product information supply chain. Another limitation concerns the risk that our findings only apply to a specific type of assortment. Although we aimed at selecting cases that are representative of more intensive forms of supply chain collaboration, it might be argued that other assortments, such as food or electronics, generate additional product information requirements and imply more sophisticated ECR strategies.

Based on our study, we have identified the following fields for future research:

Given the limitations of a case study methodology, empirical studies are needed to further enhance and test our propositions and their generalization to other market environments and geographical settings. We encourage further qualitative and quantitative studies that elaborate on this model. More specifically, we anticipate interesting questions for IS researchers related to the impact of the product information supply chain on supply and demand chain performance.

The lack of models and empirical evidence related to the inter-organizational product information supply chain is reminiscent of the early stages of supply chain research and calls for a more extensive investigation of the inter-organizational interdependencies and coordination mechanisms. As a direction for future research, researchers should come up with appropriate modeling techniques for the inter-organizational product information supply chain. The latter may comprise numerical models from operations management as well as process and information models for visualization of flow and sharing dependencies.

With regard to the further development of open standards, future research should investigate alternative concepts for increasing interoperability in inter-organizational product information supply chains (Legner and Lebreton, 2007). We expect significant contributions from the fields of enterprise and process modeling, Semantic Web and the use of ontologies.

Another research stream will have to investigate how RFID technology and upcoming process innovations in the retail supply chain (Lee and Özer, 2007; Loebbecke and Palmer, 2006) impact the product information supply chain. RFID-based process innovations extend the need for context interchange to the object level, while offering new technological capabilities for storing product information. The current discussion related to product information stored on RFID tags focuses on the Electronic Product Code and the EPC Information Service (EPCIS) (Nakatani et al., 2006; Thiesse and Michahelles, 2006), but does not address how they interplay with the existing GDSN. On the basis of our findings, we expect that RFID-related process innovations significantly increase coordination requirements in the product information supply chain.

## Acknowledgements

This research has been conducted in the context of the Competence Center Business Networking at the University of St. Gallen, Switzerland. We would like to thank all industry partners for funding and supporting this research. We gratefully acknowledge the valuable comments and suggestions of two anonymous reviewers and the JAIS guest editors that have greatly improved the paper.

## References

Accenture (2006). Synchronization - The Next Generation of Business Partnering, Grocery

Manufacturers Association (GMA), Food Marketing Institute (FMI), Wegmans Food Markets, Accenture LLP and 1SYNC, Hamilton.

Aviv, Y. (2001). "The effect of collaborative forecasting on supply chain performance", Management Science 47(10), pp. 1326-1343.

Ballou, D., Wang, R., Pazer, H., and Kumar-Tayi, G. (1998). "Modeling Information Manufacturing Systems to Determine Information Product Quality", Management Science 44(4), pp. 462- 484.

Benbasat, I., Goldstein, D.K., and Mead, M. (1987). "The Case Research Strategy in Studies of Information Systems", MIS Quarterly 11(3), pp. 369-386.

Bensaou, M., and Venkatraman, N. (1996). "Inter-organizational relationships and information technology: A conceptual synthesis and a research framework", European Journal of Information Systems 5(2), pp. 84-91.

Bowling, T., Licul, E., and Van Hammond, D. (2004). "Global Data Synchronization: Building a flexible approach", IBM Institute for Business Value, Somers.

Brousseau, E. (1994). "EDI and inter-firm relationships: toward a standardization of coordination processes?" Information Economics and Policy 12(6), pp. 319-347.

Cachon, G.P., and Fisher, M. (2000). "Supply Chain Inventory Management and the Value of Shared Information", Management Science 46(5), pp. 1032-1048.

Chatfield, A.T., and Yetton, P. (2000). "Strategic Payoff from EDI as a Function of EDI Embeddedness", Journal of Management Information Systems 16(4), pp. 195-224.

Chen, F., Dresner, J., Ryan, K., and Simchi-Levi, D. (2000). "Quantifying the bull-whip effect in a simple supply chain: The impact of forecasting lead time and information", Management Science 46(3), pp. 436-443.

Chisholm, M. (2006). "Master Data vs. Reference Data", DMReview.com 16(4), pp. http://www.dmreview.com/article\_sub.cfm?articleId=1051002 (current Jan 1051030, 1052007).

Choudhury, V. (1997). "Strategic choices in the development of inter-organizational information systems", Information Systems Research 8(1), pp. 1-24.

Choudhury, V., and Sampler, J.L. (1997). "Information specificity and environmental scanning: An economic perspective", MIS Quarterly 21(1), pp. 25-53.

Clark, T.H., and Stoddard, D.B. (1996). "Interorganizational Business Process Redesign: Merging Technological and Process Innovation", Journal of Management Information Systems 13(2), pp. 9-29.

Clemons, E.K., Reddi, S.P., and Row, M.C. (1993). "The Impact of Information Technology on the Organization of Economic Activity: The "Move to the Middle" Hypothesis", Journal of Management Information Systems 10(2), pp. 9-35.

Cohen Kulp, S., Lee, H.L., and Ofek, E. (2004). "Manufacturer Benefits from Information Integration with Retail Customers", Management Science 50(4), pp. 431-444.

Corsten, D., and Kumar, N. (2005). "Do Suppliers Benefit from Collaborative Relationships with Large Retailers? An Empirical Investigation of Efficient Consumer Response Adoption", Journal of Marketing 69(3), pp. 80-94.

Corsten, D.S., and Gruen, T. (2003). "Desperately seeking shelf-availability: an examination of the extent, the causes, and the efforts to address retail out-of-stocks", International Journal of Retail & Distribution Management 31(12), pp. 605-617.

Crowston, K. (1997). "A Coordination Theory Approach to Organizational Process Design", Organization Science 8(2), pp. 157-175.

Damsgaard, J., and Lyytinen, K. (2001). "The Role of Intermediating Institutions in the Diffusion of Electronic Data Interchange (EDI): How Industry Associations Intervened in Denmark, Finland, and Hong Kong", Information Society 17(3), pp. 195-210.

Damsgaard, J., and Truex, D. (2000). "Binary trading relations and the limits of EDI standards: the Procrustean bed of standards", European Journal of Information Systems 9(3), pp. 173-188.

Darke, P., Shanks, G., and Broadbent, M. (1998). "Successfully completing case study research: combining rigour, relevance and pragmatism", Information Systems Journal 8(4), pp. 273- 289.

Dupre, K., and Gruen, T.W. (2004). "The use of category management practices to obtain a sustainable competitive advantage in the fast-moving consumer-goods industry", Journal of Business & Industrial Marketing 19(7), pp. 444-459.

Edgington, T., Choi, B., Henson, K., Raghu, T.S., and Vinze, A. (2004). "Adopting Ontology to Facilitate Knowledge Sharing", Communications of the ACM 47(11), pp. 85-90.

Eisenhardt, K.M. (1989). "Building Theories from Case Study Research", Academy of Management

Iacovou, C., Benbasat, I., and Dexter, A. (1995). "Electronic data interchange and small organisations: adoption and impact of technology", MIS Quarterly 19(4), pp. 495-479.

Review 14(4), pp. 532-550.

Field, A.M. (2005). "Getting in sync", Journal of Commerce 6(10), pp. 10-14.

Fleisch, E., and Österle, H. (2000). "A Process-oriented Approach to Business Networking", Electronic Journal of Organizational Virtualness 2(2), pp. 1-18.

Garf, R., and Romanow, K. (2005). GNX and WWRE Finalize Merger: Say Hello to Agentrics, AMR Research, Boston.

Gavirneni, S., Kapuscinski, R., and Tayur, S. (1999). "Value of Information in Capacitated Supply Chains", Management Science 45(1), pp. 16-24.

Global Commerce Initiative, and Capgemini (2005). "Global Data Synchronisation At Work in the Real World - Illustrating the Business Benefits", Paris.

Goh, C.H., Bressan, S., Madnick, S., and Siegel, M. (1999). "Context Interchange: New Features and Formalisms for the Intelligent Integration of Information", ACM Transactions on Information Systems 17(8), pp. 270-293.

Gosain, S., Malhotra, A., and El Sawy, O.A. (2004). "Coordinating for Flexibility in e-Business Supply Chains", Journal of Management Information Systems 21(3), pp. 7-45.

Gosain, S., Malhotra, A., El Sawy, O.A., and Chehade, F. (2003). "The impact of common e-business interfaces", Communications of the ACM 46(12), pp. 186 - 195.

Gregor, S. (2006). "The Nature of Theory in Information Systems", MIS Quarterly 30(3), pp. 611-642.

Grocery Manufacturers of America, Food Marketing Institute, and A. T. Kearney (2003). Action Plan to Accelerate Trading Partner Electronic Collaboration, Washington.

GS1 (2004). GDSN Introductory Brochure, EAN International, Brussels.

GS1 (2005a). "Business Requirement Document For Data Synchronization Data Model for Trade Item (Data Definition) Version 7.7.1", http://www.gs1belu.org/cdb-uk/BRD\_Item.pdf, (current Jan 15, 2007).

GS1 (2005b). "eCom Standards in the GS1 Community".

GS1 (2007). "GS1 Global Registry Statistics", http://www.gs1.org/docs/gdsn/gdsn\_adoption.pdf, (current Jan 30, 2007).

GS1 (2008) ""GS1 Global Registry Statistics", http://www.gs1.org/docs/gdsn/gdsn\_adoption.pdf, (current March 31, 2008).

Hanseth, O., Jacucci, E., Grisot, M., and Aanestad, M. (2006). "Reflexive standardization: Side effects and complexity in standard making", MIS Quarterly 30(Aug2006 Supplement), pp. 564-581.

Hofstetter, J., and Jones, C.C. (2005). "The Case for ECR. A review and outlook of continuous ECR adoption in Western Europe", ECR Europe, Brussels.

Holweg, M., Disney, S., Holmström, J., and Småros, J. (2005). "Supply Chain Collaboration: Making Sense of the Strategy Continuum", European Management Journal 23(2), pp. 170-181.

Hong, I. (2002). "A new framework for interorganizational systems based on the linkage of participants' roles", Information & Management 4(2), pp. 261-270.

Hoogewegen, M.R., and Wagenaar, R. (1996). "A Method to Assess the Expected Net Benefits of EDI Investments", International Journal of Electronic Commerce 1(1), pp. 73-94.

Horst, F. (2007). "ECR-Basistechnologien etablieren sich", retail technology(4), pp. 10-12.

Iyer, B., Shankaranarayanan, G., and Wyner, G. (2006). "Process Coordination Requirements: Implications for the Design of Knowledge Management Systems", Journal of Computer Information Systems XLVI(5), pp. 1-13.

Johnston, H.R., and Vitale, M.R. (1988). "Creating competitive advantage with Interorganizational Information systems", MIS Quarterly 12(2), pp. 153-165.

Karimi, J., and Konsynski, B.R. (1991). "Globalization and Information Management Strategies", Journal of Management Information Systems 7(4), pp. 7-26.

Kim, K.K., Umanath, N.S., and Kim, B.H. (2006). "An Assessment of Electronic Information Transfer in B2B Supply-Channel Relationships", Journal of Management Information Systems 22(3), pp. 293-320.

Kotzab, H. (2005). "The automation of retail logistics", in: Retailing in a SCM-Perspective, H. Kotzab and M. Bjerre (eds.), Copenhagen Business School Press, Copenhagen, pp. 114-159.

Kraut, R.E., and Streeter, L.A. (1995). "Coordination in software development", Communications of the ACM 38(3), pp. 69-81.

Kubicek, H. (1992). "The Organization Gap in Large-Scale EDI Systems", in: Scientific Research on EDI "Bringing Worlds Together", R.J. Streng, C.F. Ekering, E. van Heck and J.F.H. Schultz (eds.), Samsom, Amsterdam, pp. 11-41.

Kurnia, S., and Johnston, R.B. (2003). "Adoption of efficient consumer response: key issues and challenges in Australia", Supply Chain Management 8(3), pp. 251-262.

Kurnia, S.J.R.B. (2000)."Understanding the Adoption of ECR: A Broader Perspective," Proceedings of Global Networked Organizations, Proceedings 13th International Bled Electronic Commerce Conference, pp. 372-390.

Kurt Salmon Associates (1993). Efficient Consumer Response - Enhancing Consumer Value in the Grocery Industrie, Washington.

Lau, J.S.K., Huang, G.Q., and Mak, K.L. (2002). "Web-based simulation portal for investigating the impacts of sharing production information on supply chain dynamics from the perspective of inventory allocation", Integrated Manufacturing Systems 13(5), pp. 345-358.

Lee, H.L., and Özer, Ö. (2007). "Unlocking the Value of RFID", Production and Operations Management 16(1), pp. 40-64.

Lee, H.L., Padmanabhan, V., and Whang, S. (1997). "Information Distortion in a Supply Chain: The Bullwhip Effect", Management Science 43(4), pp. 546-558.

Lee, H.L., So, K., and Tang, C. (2000). "The Value of Information Sharing in a Two-Level Supply Chain", Management Science 46(5), pp. 626-643.

Lee, Y.W., and Strong, D.M. (2003). "Knowing-Why About Data Processes and Data Quality", Journal of Management Information Systems 20(3), pp. 13-39.

Legner, C., and Lebreton, B. (2007). "Preface to the Focus Theme Section on Business Interoperability: Business Interoperability Research – Present Achievements and Upcoming Challenges", Electronic Markets 17(3), pp. 176-186.

Loebbecke, C., and Palmer, J.W. (2006). "RFID in the Fashion Industry: Kaufhof Department Stores AG and Gerry WeberInternational AG, Fashion Manufacturer", MIS Quarterly Executive 5(2), pp. 59-79.

Lohtia, R., Xie, F.T., and Subramaniam, R. (2004). "Efficient consumer response in Japan: Industry concerns, current status, benefits, and barriers to implementation", Journal of Business Research 57(3), pp. 306-312.

Löwer, U.M. (2005). Interorganisational Standards: Managing Web Services Specifications for Flexible Supply Chains, Physica-Verlag, Heidelberg.

Madnick, S. (1995). "Integrating information from global systems: dealing with the “on- and off-ramps” of the information superhighway", Journal of Organizational Computing 5(2), pp. 69-82.

Malone, T.W., and Crowston, K. (1994). "The Interdisciplinary Study of Coordination", ACM Computing Surveys 26(1), pp. 87-119.

Malone, T.W., Crowston, K., Lee, J., Pentland, B., Dellarocas, C.N., Wyner, G., Quimby, J., Osborn, C.S., Bernstein, A., Herman, G., Klein, M., and O'Donnell, E. (1999). "Tools for Inventing Organizations: Toward a Handbook of Organizational Processes", Management Science 45(3), pp. 425-443.

Malone, T.W., Yates, J., and Benjamin, R.I. (1987). "Electronic Markets and Electronic Hierarchies", Communications of the ACM 30(6), pp. 484-497.

March, J.G., and Simon, H.A. (1958). Organizations, John Wiley & Sons, New York.

Marchand, D.A. (2004). "Seeking Global Advantage with Information Management and Information Technology Capabilities", in: The Blackwell Handbook of Global Management, H.W. Lane, M.L. Maznevski, M.E. Mendenhall and J. McNett (eds.), Blackwell Publishing, Oxford, pp. 300-321.

Marinos, G. (2005). "The Information Supply Chain: Achieving Business Objectives by Enhancing Critical Business Processes", http://www.dmreview.com/article\_sub.cfm?articleId=1023896, (current Apr. 15, 2007).

Markus, L.M., Steinfeld, C.W., Wigand, R.T., and Minton, G. (2006). "Industry-Wide Information Systems Standardization as Collective Action: The Case of the U.S. Residential Mortgage Industry", MIS Quarterly 30, pp. 439-465.

Massetti, B., and Zmud, R. (1996). "Measuring the Extent of EDI Usage in Complex Organisations: Strategies and Illustrative Examples", MIS Quarterly 20(3), pp. 331-345.

Mukhopadhyay, T., and Kekre, S. (2002). "Strategic and Operational Benefits of Electronic Integration

in B2B Procurement Processes", Management Science 48(10), pp. 1301-1331.

Nakatani, K., Chuang, T.-T., and Zhou, D. (2006). "Data Synchronization Technology: Standards, Business Values and Implications", Communications of AIS 44(17), pp. 2-60.

Nickerson, J.V., and zur Muehlen, M. (2006). "The Ecology of Standards Processes: Insights from Internet Standard Making", MIS Quarterly 30(Special Issue), pp. 467-488.

Nurmilaakso, J.-M., Kotinurmi, P., and Laesvuori, H. (2006). "XML-based e-business frameworks and standardization", Computer Standards & Interfaces 28(5), pp. 585-599.

Ordanini, A. (2005). "The Effects of Participation on B2B Exchanges: A Resource-Based View", California Management Review 47(2), pp. 97-113.

Orlikowski, W.J., and Baroudi, J.J. (1991). "Studying Information Technology in Organizations: Research Approaches and Assumptions", Information Systems Research 2(1), pp. 1-28.

Paré, G. (2004). "Investigating Information Systems with Positivist Case Study Research", Communications of AIS 2004(13), pp. 233-264.

Pendrous, N. (2006). "Global data exchange system shows huge growth", Food Manufacture(7), p. 24.

Premkumar, G. (2000). "Interorganization Systems and Supply Chain Management: An Information Processing Perspective", Information Systems Management 17(3), pp. 56-69.

Reimers, K. (2001). "Standardizing the new e-business platform: Learning from the EDI experience", Electronic Markets 11(4), pp. 231-237.

Reimers, K., and Li, M. (2005). "Antecendents of a Transaction Cost Theory of Vertical IS Standardization Processes", Electronic Markets 15(4), pp. 301-312.

Reyes, P.M., and Bhutta, K. (2005). "Efficient consumer response: literature review", International Journal of Integrated Supply Management 1(4), pp. 346-386.

Riggins, F.J., and Mukhopadhyay, T. (1994). "Interdependent Benefits from interorganizational Systems: Opportunities for Business Partner Reegineering", Journal of Management Inforamation Systems 11(2), pp. 37-57.

Rugullies, E. (2004). Product Information Management Leaders Emerge, Forrester Research, Cambridge.

Russom, P. (2006). "Master Data Management: Consensus-Driven Data Definitions for Cross-Application Consistency", The Data Warehousing Institute, Seattle.

Saeed, K.A., Malhotra, M.K., and Grover, V. (2005). "Examining the Impact of Interorganizational Systems on Process Efficiency and Sourcing Leverage in Buyer - Supplier Dyads", Decision Sciences 36(3), pp. 365-396.

Sahin, F., and Robinson, E.P. (2002). "Flow coordination and information sharing in supply chains: Review, implications, and directions for future research", Decision Sciences 33(4), pp. 505- 536.

Schemm, J., and Legner, C. (2008)."The Role and Emerging Landscape of Data Pools in the Retail and Consumer Goods Industries," Proceedings of the 41st Annual Hawaii International Conference on System Sciences (CD-ROM), Computer Society Press.

Shapiro, C., and Varian, H.R. (1998). Information Rules - A Strategic Guide to the Network Economy, Harvard Business School Press, Boston/Massachusetts.

Sheu, C., Yen, H.R., and Chae, B. (2006). "Determinants of supplier-retailer collaboration: evidence from an international study", International Journal of Operations & Production Management 26(1), pp. 24-49.

Sparks, L., and Wagner, B.A. (2003). "Retail exchanges: a research agenda", Supply Chain Management 8(3), pp. 201-108.

Sun, S., and Yen, J. (2005). "Information Supply Chain: A Unified Framework for Information-Sharing", in: Intelligence and Security Informatics, P. Kantor, G. Muresan, F. Roberts, D. Zeng, F.-Y. Wang, H. Chen and R. Merkle (eds.), Springer, pp. 422-429.

Swanton, B. (2006). "MDM on a Single ERP Instance: Workflow and Data Quality", in: Boston.

Tan, C., and Sia, S.K. (2007). "Managing Flexibility in Outsourcing", Journal of the Association for Information Systems 7(4), pp. 179-206.

Thiesse, F., and Michahelles, F. (2006). "An overview of EPC technology", Sensor Networks 26(2), pp. 101-105.

Vermeer, B.H.P.J. (2000)."How Important is Data Quality for Evaluating the Impact of EDI on Global Supply Chains?," Proceedings of the 33rd Annual Hawaii International Conference on System

Sciences (CD-ROM), IEEE Computer Society.

Wang, R.Y., Lee, Y.W., Pipino, L.L., and Strong, D.M. (1998). "Manage Your Information as a Product", Sloan Management Review 39(4), pp. 95-105.

White, A. (2005). Magic Quadrant for Product Information Management, Stamford.

White, A., Prior, D., Radcliffe, J., Wood, B., and Holincheck, J. (2004). "Emergence of EIM Drives Semantic Reconciliation", Gartner Group, Stamford.

Woods, D. (2003). Packaged Composite Applications, O'Reilly, London.

Yin, R.K. (2002). Case Study Research. Design and Methods, Sage Publications, London.

Zhao, H. (2007). "Semantic Matching Across Heterogeneous Data Sources", Communications of the ACM 50(1), pp. 44-50.

Zhu, K., Kraemer, K.L., Gurbaxani, V., and Xu, S.X. (2006). "Migration to Open-Standard

Interorganizational Systems: Network Effects, Switching Costs, and Path Dependency", MIS Quarterly 30(Special Issue), pp. 515-539.

Zhu, K., Kraemer, K.L., Xu, S., and Dedrick, J. (2004). "Information Technology Payoff in E-Business Environments: An International Perspective on Value Creation of E-Business in the Financial Services Industry", Journal of Management Information Systems 21(1), pp. 17-54.

List of Acronyms

ECR Efficient Consumer Response

GDS Global Data Synchronization

GDSN Global Data Synchronization Network

GTIN Global Trade Item Number

GPC Global Product Classification

IOS Inter-Organizational Systems

IP Information Product

ISC Information Supply Chain

VMI Vendor-Managed Inventory

## About the Authors

Dr. Christine Legner has recently been appointed head of the Chair of Enterprise Systems and Electronic Business at European Business School in Oestrich-Winkel (Germany). In her previous position, she was senior lecturer and project manager of the Competence Center Business Networking at AACSB-accredited University of St.Gallen (Switzerland). She has practical and academic experience in designing e-business solutions. Her research interests include business networking, collaborative business processes, inter- and intra-enterprise systems and serviceoriented architectures. She has published more than 30 articles in academic journals, including the International Journal of Technology Management, Electronic Markets, Journal of Electronic Commerce in Organizations and IEEE Pervasive Computing, and conference proceedings, such as those of the European Conference on Information Systems, Hawaii International Conference on System Sciences and the Bled eConference. She holds a PhD in Information Management from the University of St. Gallen, a Master in Applied Economics from the Université Paris-Dauphine (France) and a Master in Industrial Engineering from the Technical University of Karlsruhe (Germany).

Jan Schemm is a PhD candidate at University of St. Gallen (Switzerland) and a former member of the Competence Center Business Networking. He studied at University of Münster (Germany) and Virginia Polytechnic Institute and State University (US). His research interests are in the field of master data management and electronic collaboration in the retail and consumer goods industries.

Copyright © 2008, by the Association for Information Systems. Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and full citation on the first page. Copyright for components of this work owned by others than the Association for Information Systems must be honored. Abstracting with credit is permitted. To copy otherwise, to republish, to post on servers for commercial use, or to redistribute to lists requires prior specific permission and/or fee. Request permission to publish from: AIS Administrative Office, P.O. Box 2712 Atlanta, GA, 30301-2712 Attn: Reprints, or via e-mail from ais@gsu.edu.

ISSN: 1536-9323

Editor Kalle Lyytinen Case Western Reserve University, USA

<table><tr><td colspan="4">Senior Editors</td></tr><tr><td>Izak Benbasat</td><td>University of British Columbia, Canada</td><td>Robert Fichman</td><td>Boston College, USA</td></tr><tr><td>Varun Grover</td><td>Clemson University, USA</td><td>Rudy Hirschheim</td><td>Louisiana State University, USA</td></tr><tr><td>Juhani livari</td><td>University of Oulu, Finland</td><td>Robert Kauffman</td><td>University of Minnesota, USA</td></tr><tr><td>Frank Land</td><td>London School of Economics, UK</td><td>Jeffrey Parsons</td><td>Memorial University of Newfoundland, Canada</td></tr><tr><td>Suzanne Rivard</td><td>Ecole des Hautes Etudes Commerciales, Canada</td><td>Bernard C.Y. Tan</td><td>National University of Singapore, Singapore</td></tr><tr><td>Yair Wand</td><td>University of British Columbia, Canada</td><td></td><td></td></tr><tr><td colspan="4">Editorial Board</td></tr><tr><td>Steve Alter</td><td>University of San Francisco, USA</td><td>Michael Barrett</td><td>University of Cambridge, UK</td></tr><tr><td>Cynthia Beath</td><td>University of Texas at Austin, USA</td><td>Anandhi S. Bharadwaj</td><td>Emory University, USA</td></tr><tr><td>Francois Bodart</td><td>University of Namur, Belgium</td><td>Marie-Claude Boudreau</td><td>University of Georgia, USA</td></tr><tr><td>Susan A. Brown</td><td>University of Arizona, USA</td><td>Tung Bui</td><td>University of Hawaii, USA</td></tr><tr><td>Dave Chatterjee</td><td>University of Georgia, USA</td><td>Patrick Y.K. Chau</td><td>University of Hong Kong, China</td></tr><tr><td>Wynne Chin</td><td>University of Houston, USA</td><td>Ellen Christiaanse</td><td>University of Amsterdam, Nederland</td></tr><tr><td>Mary J. Culnan</td><td>Bentley College, USA</td><td>Jan Damsgaard</td><td>Copenhagen Business School, Denmark</td></tr><tr><td>Samer Faraj</td><td>University of Maryland, College Park, USA</td><td>Chris Forman</td><td>Carnegie Mellon University, USA</td></tr><tr><td>Guy G. Gable</td><td>Queensland University of Technology, Australia</td><td>Dennis Galletta</td><td>University of Pittsburg, USA</td></tr><tr><td>Hitotora Higashikuni</td><td>Tokyo University of Science, Japan</td><td>Kai Lung Hui</td><td>National University of Singapore, Singapore</td></tr><tr><td>Bill Kettinger</td><td>University of South Carolina, USA</td><td>Rajiv Kohli</td><td>College of William and Mary, USA</td></tr><tr><td>Chidambaram Laku</td><td>University of Oklahoma, USA</td><td>Ho Geun Lee</td><td>Yonsei University, Korea</td></tr><tr><td>Jae-Nam Lee</td><td>Korea University</td><td>Kai H. Lim</td><td>City University of Hong Kong, Hong Kong</td></tr><tr><td>Mats Lundeberg</td><td>Stockholm School of Economics, Sweden</td><td>Ann Majchrzak</td><td>University of Southern California, USA</td></tr><tr><td>Ji-Ye Mao</td><td>Remnin University, China</td><td>Anne Massey</td><td>Indiana University, USA</td></tr><tr><td>Emmanuel Monod</td><td>Dauphine University, France</td><td>Eric Monteiro</td><td>Norwegian University of Science and Technology, Norway</td></tr><tr><td>Mike Newman</td><td>University of Manchester, UK</td><td>Jonathan Palmer</td><td>College of William and Mary, USA</td></tr><tr><td>Paul Palou</td><td>University of California, Riverside, USA</td><td>Yves Pigneur</td><td>HEC, Lausanne, Switzerland</td></tr><tr><td>Dewan Rajiv</td><td>University of Rochester, USA</td><td>Sudha Ram</td><td>University of Arizona, USA</td></tr><tr><td>Balasubramaniam Ramesh</td><td>Georgia State University, USA</td><td>Timo Saarinen</td><td>Helsinki School of Economics, Finland</td></tr><tr><td>Rajiv Sabherwal</td><td>University of Missouri, St. Louis, USA</td><td>Raghu Santanam</td><td>Arizona State University, USA</td></tr><tr><td>Susan Scott</td><td>The London School of Economics and Political Science, UK</td><td>Olivia Sheng</td><td>University of Utah, USA</td></tr><tr><td>Carsten Sorensen</td><td>The London School of Economics and Political Science, UK</td><td>Ananth Srinivasan</td><td>University of Auckland, New Zealand</td></tr><tr><td>Katherine Stewart</td><td>University of Maryland, USA</td><td>Mani Subramani</td><td>University of Minnesota, USA</td></tr><tr><td>Dov Te&#x27;eni</td><td>Tel Aviv University, Israel</td><td>Viswanath Venkatesh</td><td>University of Arkansas, USA</td></tr><tr><td>Richard T. Watson</td><td>University of Georgia, USA</td><td>Bruce Weber</td><td>London Business School, UK</td></tr><tr><td>Richard Welke</td><td>Georgia State University, USA</td><td>George Westerman</td><td>Massachusetts Institute of Technology, USA</td></tr><tr><td>Youngjin Yoo</td><td>Temple University, USA</td><td>Kevin Zhu</td><td>University of California at Irvine, USA</td></tr><tr><td colspan="4">Administrator</td></tr><tr><td>J. Peter Tinsley</td><td>AIS, Executive Director</td><td colspan="2">Association for Information Systems, USA</td></tr><tr><td>Reagan Ramsower</td><td>Publisher</td><td colspan="2">Baylor University</td></tr></table>
