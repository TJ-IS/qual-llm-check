---
otero_id: 6576
otero_key: "CCD68CVJ"
title: "Optimal Strategies for a Monopoly Intermediary in the Supply Chain of Complementary Web Services"
authors: "Qian \"Candy\" Tang; Hsing \"Kenneth\" Cheng"
year: "2006"
journal: "Journal of Management Information Systems"
doi: "10.2753/mis0742-1222230310"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
![](/api/attachments/CCD68CVJ/fulltext/images/06331ee0e9fe0ffb1db2d78bfc0870d5fb7d841f4b79521db847feedb70e698c.jpg)

# Optimal Strategies for a Monopoly Intermediary in the Supply Chain of Complementary Web Services

Qian "Candy" Tang & Hsing "Kenneth" Cheng

To cite this article: Qian "Candy" Tang & Hsing "Kenneth" Cheng (2006) Optimal Strategies for a Monopoly Intermediary in the Supply Chain of Complementary Web Services, Journal of Management Information Systems, 23:3, 275-307

To link to this article: http://dx.doi.org/10.2753/MIS0742-1222230310

![](/api/attachments/CCD68CVJ/fulltext/images/5f710bdc21a4a415f63f25e4b7bf8f1c0146d2e20a7d08e67a4a9878724b5f4e.jpg)

Published online: 09 Dec 2014.

![](/api/attachments/CCD68CVJ/fulltext/images/39b02a1ab73ec2c47f4f03a49c6fe2e127f738467074fd85837461e1a7b63f23.jpg)

Submit your article to this journal

Article views: 8

![](/api/attachments/CCD68CVJ/fulltext/images/ba5c34147fa01a671cd821bece0109eb0ed449060111a0d9e3b272cb3b728673.jpg)

View related articles

# Optimal Strategies for a Monopoly Intermediary in the Supply Chain of Complementary Web Services

QIAN “CANDY” TANG AND HSING “KENNETH” CHENG

QIAN “CANDY” TANG is an Assistant Professor in the Department of Information Systems, School of Computing, National University of Singapore. She received her Ph.D. in Decision and Information Sciences from Warrington College of Business Administration, University of Florida, in 2004. Her research interests include economics of information systems and security, e-commerce, and the effect of IT on firm strategies and supply-chain management. Currently, her research is focused on software pricing, marketing strategies of intermediaries in Web services supply chains, and software security. Her work has appeared in Decision Support Systems and IEEE Transactions on Engineering Management. Dr. Tang is a member of AIS, DSI, and INFORMS.

HSING “KENNETH” CHENG is an Associate Professor of Information Technology and an American Economic Institutions Faculty Fellow at the Department of Decision and Information Sciences (to be renamed Information Systems and Operations Management) of Warrington College of Business Administration at the University of Florida. Prior to joining UF, he served on the faculty at The College of William & Mary from 1992 to 1998. He received his Ph.D. in Computers and Information Systems from William E. Simon Graduate School of Business Administration, University of Rochester, in 1992. Professor Cheng teaches information technology strategy, electronic commerce, and supply chain management. He was awarded the Warrington College of Business Administration Teacher of the Year for 2000–1. Dr. Cheng’s research interests involve electronic commerce, economics of information systems, and information technology in supply-chain management. His recent research focuses on modeling the effect of Internet technology on software development and marketing, and issues surrounding the application services supply chain and Web services. His work has appeared in Computers and Operations Research, Decision Support Systems, European Journal of Operational Research, IEICE Transactions, IEEE Transactions on Engineering Management, Information Technology and Management, International Journal of Electronic Commerce, International Journal of Web Services Research, Journal of Business Ethics, Journal of Information Systems and e-Business Management, Journal of Management Information Systems, and Socio-Economic Planning Sciences. He also contributed book chapters on “Hacking, Computer Viruses, and Software Piracy: The Implications of Modern Computer Fraud for Corporations” and “The Critical Role of Information Technology for Employee Success in the Coming Decade.” Dr. Cheng has coedited several special issues in various information systems journals. He has served on the program committee of many information systems conferences and workshops, and was a program cochair for the Workshop on E-Business 2003.

276 TANG AND CHENG

ABSTRACT: Web services are interoperable and reusable software components that can be dynamically discovered and integrated over the Internet. Developed on open standards, Web services have become a promising solution to inter- and intra-organization application integration. The supply chain of Web services exhibits two distinct features that are not considered in previous literature on information and physicalgood supply chain: the integration of multiple Web services and the cross-network externality effect between Web service vendors and users. In a quest to fill in the research gap, this paper studies the optimal pricing strategies of a monopolistic intermediary in the supply chain of complementary Web services. The Web service intermediary (WSI) provides both technical and aggregation services, and seeks to charge optimal subscription and listing fees. Analytical results show that in a supply chain of complementary Web services exhibiting cross-network effects, the optimal strategy for the WSI is to set the listing fee such that all service providers list on it. On the other hand, the optimal subscription fee depends on the intensity of the cross-network effect, consumers’ valuation of value-added services, and the characteristics of the Web services under consideration.

KEY WORDS AND PHRASES: business intermediary, complementarity, network externalities, supply chains, Web services.

THE INTENSE COMPETITION AND THE CONSTANTLY changing nature of the global economy call for an agile information technology (IT) infrastructure for firms to stay competitive and adapt to new threats and opportunities. IT managers face an enormous pressure to cut costs and leverage existing information technology resources, a task complicated by legacy systems built on technologies of different ages. Software reusability and interoperability has long been recognized as the key to a cost-efficient and responsive IT solution to the ever-changing business requirements. Many technologies have been proposed to this end with disappointing results. The Web service technology, touted as the foundation to an interoperable and location-transparent service-oriented computing architecture, is the most promising solution to date [19].

Web services are “loosely coupled, reusable software components that semantically encapsulate discrete functionality and are distributed and programmatically accessible over standard Internet protocols.”<sup>1</sup> From the technical perspective, Web services are platform-, language-, and vendor-neutral interoperable software components defined by a stack of open standards, such as XML, SOAP, WSDL, and UDDI [16]. From the business perspective, Web services enable “just-in-time” application integration that helps to reduce software development and integration cost by allowing firms to leverage existing systems and utilize business modules developed by other companies. Furthermore, firms can enjoy the flexibility to choose the best-ofbreed applications instead of being tied to a particular software vendor. The scope of Web services ranges from personal services (e.g., stock quotes) to enterprise-level services such as sales force automation systems.

Providing interoperable Web services alone, however, does not guarantee a “plugand-play” service-oriented architecture, which is essential to enterprise application integration (EAI) and business-to-business (B2B) integration. The integration of various Web services to perform business functions is not as straightforward as bundling physical goods together. Although Web services are platform- and vendor-independent, they leave unspecified the context necessary for service integration on the business process level. For example, Web service consumers have to define the order of sequence, control information flow, handle exceptions, and enforce transactional integrity, just to name a few [9, 14]. Furthermore, a directory service is required if runtime discovery and integration of Web services are to be materialized.

Catering to the need for a practical service-oriented architecture, a Web service intermediary (WSI) provides technical and aggregation services to the Web service supply chain [11]. In this paper, we study the optimal pricing strategy for a monopoly WSI. The WSI charges Web service vendors and consumers for listing and for searching through the intermediary as well as for access to other technical services. We consider a supply chain of two complementary Web services such that some consumers have interest in the individual Web services while others have demand for an integrated Web service. We aim to address the following research questions: What are the optimal subscription and listing fees? Should the WSI subsidize one side of the market (the vendors or the consumers) to maximize its profit, and if so, which side should it subsidize? What are the effects of technical and aggregation services on its pricing strategies? How do the characteristics of Web services (i.e., their prices and potential market sizes) affect the optimal strategies by the WSI?

In this paper, we study the WSI’s pricing strategy in a monopolistic setting. Although there are in practice multiple WSIs, each intermediary differentiates its services in order to reduce competition (i.e., to create monopoly power). For example, Xmethods.net has strength in aggregation services such as Web service listing and searching, Infravio distinguishes itself as a Web services governance company that enables organizations to deliver software as a service to customers, and StrikeIron prides itself as the world’s largest marketplace of commercial Web services. In this sense, each WSI can be viewed as a monopoly of certain types of aggregation or technical services. The study of a monopoly WSI provides the advantage of rich managerial interpretations in a simple and tractable model, which lays the groundwork for further study in a competitive market. To the best of our knowledge, this paper is among the first to study WSI in the market of complementary Web services.

Although there is abundant study on supply chains and intermediaries, our research on WSI is motivated by several distinct features of the Web service supply chain. First, Web services are software components distributed on the Internet. Therefore, many issues regarding the supply chains of physical goods are irrelevant, such as inventory and transportation costs, and order quantities. Second, Web services boast the advantage of interoperability. The complementary functions of Web services bring new issues not studied in previous literature, which normally focus on single-product supply chains. Third, we take into account the cross-network externality effect. That is, consumer’s valuation of the intermediary increases with the number of vendors listed, while vendor’s valuation of the intermediary increases with number of the subscribing consumers. It is found that the intensity of cross-network effect plays a key role in determining the optimal strategies of the WSI.

We find that in the context of a Web service supply chain exhibiting product complementarity and cross-network externality effects, a WSI always has incentive to subsidize the Web service vendors by setting a low listing fee to induce all service vendors to list on it. The WSI, on the other hand, may choose to serve only a portion of Web service consumers, depending on how consumers value its aggregation and technical services. In addition, the optimal subscription fee is dependent on the characteristics of Web services provided by the service vendors, such as the prices and potential market sizes of Web service components and the integrated Web service.

## The Web Service Supply Chain

WE FIRST EXPLAIN THE INTERACTION AMONG the three parties of a Web service supply chain—service vendors, intermediary, and consumers. A Web service vendor develops a Web service with certain business functions and exposes it to the Internet, most likely by hosting the Web service on its own server. To make the Web service interoperable and discoverable, a Web service description file (WSDL), which describes the functions of a Web service and specifies its technical signatures, is published on a registry. The Web service registry can be understood as a database, or the “yellow page,” of Web service descriptions, which accepts queries by Web service consumers. The registry can be either a public business registry (PBR) or a private registry, such as a WSI. Listing and searching on the PBR is free, while a WSI may charge a subscription fee to service consumers and/or a listing fee to service vendors.

When a Web service consumer needs a certain type of Web service, the consumer searches the WSI or the PBR. After obtaining information from the registry, that is, retrieving the WSDL file, the Web service consumer decides whether to “purchase” the Web service from its vendor. In the context of a Web service–based architecture, the purchase of a Web service involves binding and invoking the Web service stored on the provider’s server. Figure 1 illustrates the interactions of the three parties in a Web service supply chain.

Although the idea of “software as service” bears some resemblance to that of the application service provider (ASP), the Web service technology is different from ASP in terms of technical aspects and business purposes. The ASP model is based on the concept of software renting to reduce total cost of software ownership. Often, ASP hosts monolithic software systems such as enterprise resource planning (ERP) and customer relation management (CRM) software and they are generally not discoverable. Web services, however, are developed to meet the demand of dynamic application integration. Web services are loosely coupled software components that perform discrete business functions and can be searched and dynamically integrated.

In general, a WSI provides two types of value-added services in linking Web service vendors and consumers—technical and aggregation services. Technical service includes providing Web service development and integration tools (e.g., Xmethods.net), enforcing quality guarantee, and enhancing security (e.g., FlamencoNetworks.com). BlueTitan.com provides a centralized Web service network and acts as a trusted broker that handles the issues of message delivery, routing, and security for Web service integration.

![](/api/attachments/CCD68CVJ/fulltext/images/8b3d25c6944935731e89b8a072a8f1a88941913b6c19c970cb614dde8807e381.jpg)  
Bind/Invocation  
Figure 1. Web Service Supply Chain

Apart from providing technical services, a WSI can act as an aggregator in the Web service supply chain. For example, Xmethods.net maintains a comprehensive directory of Web services so that service consumers can browse, search, and audit particular types of Web services. Compared to the public registries that are based on coarsely defined categories and complex APIs, a WSI provides more advanced search tools that lead to a higher rate of relevance and accuracy. As a result, consumers who subscribe to the WSI usually do not search the public registry as they benefit from reduced search costs via WSI’s advanced search capability.

The value of technical services does not depend on how many vendors or consumers use the intermediary (size independent). The value of aggregation services, on the other hand, is determined by the size of the Web service supply chain (size dependent). For Web service consumers, the value of aggregation services increases if more service vendors are listed because it implies a broader coverage and selection; at the same time, Web service vendors have more incentive to list on the intermediary if more consumers subscribe to the WSI. Therefore, the Web service supply chain exhibits cross-network externality effect, defined as the increased valuation by one side of the supply chain with more participants of the other side of the chain. In this paper, we aim to analyze how the technical as well as aggregation services (cross-network externality effect) affect the pricing strategies of the intermediary.

## Literature Review

THERE HAS BEEN A VAST AMOUNT OF RESEARCH on traditional intermediaries, with applications mostly in financial, labor, and physical goods supply-chain markets. In addition, previous research on Web services and WSIs has primarily centered on technical issues in the computer science field, leaving unanswered the business effect of Web services, as well as optimal business strategies of a WSI.

Prior literature on traditional intermediaries can be generally classified into two categories. The first stream of research on traditional intermediaries studies the role of intermediaries. According to Spulber [20], intermediaries can play several roles in a vertical market—matching and searching, price setting and market clearing, providing liquidity and immediacy, as well as guaranteeing of quality. There is ample research on each aspect of the roles played by the intermediaries. Rubinstein and Wolinsky [18] model the interaction between buyers and sellers as a time-consuming bilateral search process and study how a matchmaking intermediary can affect profit division between the two parties of transaction. Yavas [22] studies the effect of an intermediary on consumer search behavior, while Naert [15] takes the perspective of producers and analyzes the producer’s optimal decisions on advertising and markup in an intermediated market. Biglaiser [7] takes another avenue of research and shows that an expert intermediary can contribute to quality guarantee. The advent of the Internet technologies and the ensuing e-commerce has led to rising interests in the research functions of electronic intermediaries [2, 4, 13]. By observing reduced search cost via the Internet [3], Bailey [1] sets out to study whether the intermediation via the Internet reduces friction and finds empirically that there is greater price dispersion in online intermediaries.

The second stream of abundant research on traditional intermediaries examines the optimal strategies of intermediaries. Gehrig [10] studies the trade-off between ask– bid spread with intermediation and the cost of delay in a private search and finds that a monopoly intermediary will charge a positive spread. In another paper, by Wooders [21], it is shown that a profit-maximizing intermediary may act as a Walrasian auctioneer by setting bid and ask prices to near-Walrasian equilibrium prices. Prior research on intermediaries of traditional physical goods unfortunately cannot be directly applied to online intermediaries, because there are no issues of inventory costs, shipping costs, order quantities and transfer prices that underline previous research on traditional supply chain.

The study of WSIs is also related to a recent research stream on “two-sided markets.” Rochet and Tirole define two-sided markets as “markets in which one or several platforms enable interactions between end-users, and try to get the two sides on board by appropriately charging each side” [17, p. 2]. They point out that the theory of two-sided markets is related to the theories of network externalities and marketregulated pricing because the pricing level and structures charged by the platform (or intermediary) determine the end-user’s presence on the platform. Jullien [12] studies the socially optimal subscription and listing fees charged by electronic intermediaries. Jullien [12] shows that the welfare-maximizing strategy requires a social planner to subsidize both sellers and buyers with an amount equal to the total surplus on the other side of the market. However, only one product is considered and the seller’s benefit from the intermediary is exogenous—that is, independent of its profit gain from joining the intermediary.

Recent research on information intermediaries is more related to our study of WSIs. Baye and Morgan [5] study how an information gatekeeper, which provides product and price information to consumers, should optimally set subscription fees to consumers and advertising fees to producers. Baye and Morgan find that the gatekeeper will set a low subscription fee to attract all customers. There are two key differences between Baye and Morgan [5] and this research. First, they assume that customers are geographically segmented, so that consumers only buy from local firms if they do not subscribe to the gatekeeper. The cyberspace, in contrast, is not geographically limited. Web services requestors can search a PBR and obtain an entire list of available service vendors over the Internet. Second, the advertised price is lower than unadvertised price according to Baye and Morgan [5]. The consumers of Web services, however, pay a uniform price because the service providers and requestors trade directly even if the match is completed via WSI (see Figure 1). These two key differences result in opposite conclusions to those in Baye and Morgan [5]. Bhargava and Choudhary [6] study the product line design (vertical differentiation) of an information intermediary in the presence of aggregation benefits. In their model, consumers have heterogeneous search costs and producers’ expectation of gains from the intermediary is independent of the intermediary’s pricing. In this paper, we model the interaction among service vendors, WSI, and consumers in response to the subscription fee and listing fee charged by the WSI.

Of most relevance to this research is the work by Corbett and Karmarkar [8], which analyzes optimal subscription fees and listing fees by an intermediary in the presence of cross-network externalities. Their study, however, focuses on a supply chain where the sellers and consumers trade for a single product. Because the primary advantage of Web services is the ease of software integration, we study a supply chain of two complementary Web services. In accordance, there are three groups of consumers, namely, two groups of consumers interested in the individual Web services and a third group of consumers interested in the integrated Web service, resulting in a far more complicated analysis of optimal pricing strategies of the WSI than that of Corbett and Karmarkar [8]. We obtain insights into the WSI’s optimal strategies not available in prior literature. In particular, we find that the optimal subscription fee is dependent on several factors: (1) consumers’ valuation for technical services versus aggregation services, and (2) the prices and sizes of potential markets of the Web service components and the integrated Web service. In comparison, the optimal subscription fee found in the paper by Corbett and Karmarkar [8] is not affected by the relationship between size-independent (reduced search cost) and size-dependent (aggregation services) factors.

## The Model

WE CONSIDER TWO GROUPS OF WEB SERVICE VENDORS that provide two types of complementary Web services, denoted by $S _ { 1 }$ and $S _ { 2 }$ . The two complementary Web services can be integrated into a new integrated Web service $S _ { 3 } .$ Following the modeling approach of Corbett and Karmarkar [8], there are $N _ { 1 }$ service vendors of $S _ { 1 }$ and $N _ { 2 }$ service vendors of $S _ { 2 }$ . The Web service markets of $S _ { 1 }$ and $S _ { 2 }$ become perfectly competitive when the numbers of service providers $N _ { 1 }$ and $N _ { 2 }$ are sufficiently large. Therefore, we treat the prices of $S _ { 1 }$ and $S _ { 2 }$ as exogenously given, denoted by $P _ { 1 }$ and $P _ { 2 } ,$ respectively. Because in this paper we focus on the intermediary’s pricing strategies, the consumers under consideration have high enough reservation prices that consumers’ main decision is whether to subscribe to the WSI given the subscription fee.

The Web service consumers consist of three distinct ${ \tt g r o u p s { - } } Q _ { 1 }$ consumers are interested in $S _ { 1 } , Q _ { 2 }$ consumers are interested in $S _ { 2 } ,$ and $Q _ { 3 }$ consumers are interested in the integrated Web service $S _ { 3 } .$ . Those $Q _ { 3 }$ consumers of $S _ { 3 }$ need to purchase Web services $S _ { 1 }$ and $S _ { 2 }$ (from the service vendors directly), and perform the integration by themselves to produce $S _ { 3 } .$ . Consumers incur the same cost of integrating $S _ { 1 }$ and $S _ { 2 } ,$ regardless of whether they find the Web services via WSI or public registry. Therefore, this model makes no assumption about the integration cost, as it is irrelevant to the consumer’s subscription decision. In the Conclusions and Future Research section, we discuss a possible extension of this model in terms of reduced integration cost facilitated by the integration tools offered by WSI. We consider those consumers who derive positive utilities from Web service consumption, given the prices of Web services of $S _ { 1 }$ and $S _ { 2 }$ and the integration cost, in order to focus on the interaction between WSI and the Web service consumers.

Consider a monopolist WSI that provides value-added (technical and aggregation) services to the Web service market. The WSI charges a fixed listing fee L to Web service providers and a fixed subscription fee $F$ to service consumers. Let $x _ { i } \left( i = 1 , 2 \right)$ be the proportion of service vendors listing on the WSI and $y _ { j } \left( j = 1 , 2 , 3 \right)$ be the proportion of consumers subscribing to the intermediary; see Table 1 for summary of notation. Figure 2 delineates the basic setup of the model discussed above.

The sequence of events is described as follows. First, the WSI announces the subscription fee $F$ and listing fee $L .$ On observing the listing fee and subscription fee, consumers decide whether or not to subscribe to the WSI by evaluating the expected benefit from subscription. At the same time, the service vendors decide whether or not to list on the WSI by considering the expected number of subscribers and vendors joining the intermediary. In equilibrium, service consumers have rational expectation of the proportion of listed service vendors, and vice versa.

We assume that the consumers who subscribe to the WSI will not ${ \bf g 0 }$ outside the WSI to search the public registry, because of the higher search cost involved with the public registry. The effect of this assumption is also negligible. As to be shown later, the WSI’s optimal strategy is to induce all Web service vendors to list on the intermediary. This assumption is reasonable as long as there are sufficient vendors listed by the WSI.

We use backward induction to solve the WSI’s decision of optimal subscription fee and listing fee. First we derive the proportions of Web service consumers $( y _ { j } , j =$ $^ { 1 , 2 , 3 ) }$ and vendors $( x _ { i } , i = 1 , 2 )$ who decide to join the WSI given the subscription fee F and the listing fee $L .$ In the next section, we analyze how the WSI optimally sets the subscription fee and listing fee.

Table 1. Notations

<table><tr><td>Notation</td><td>Description</td></tr><tr><td> $N_{1}$ </td><td>Number of Web service vendors providing Web service  $S_{1}$ .</td></tr><tr><td> $N_{2}$ </td><td>Number of Web service vendors providing Web service  $S_{2}$ .</td></tr><tr><td> $x_{1}$ </td><td>Proportion of listed Web service vendors of  $S_{1}$  on the WSI.</td></tr><tr><td> $x_{2}$ </td><td>Proportion of listed Web service vendors of  $S_{2}$  on the WSI.</td></tr><tr><td> $Q_{1}$ </td><td>Number of Web service consumers interested in  $S_{1}$ .</td></tr><tr><td> $Q_{2}$ </td><td>Number of Web service consumers interested in  $S_{2}$ .</td></tr><tr><td> $Q_{3}$ </td><td>Number of Web service consumers interested in integrated Web service  $S_{3}$ .</td></tr><tr><td> $y_{1}$ </td><td>Proportion of Web service consumers of  $S_{1}$  subscribing to the WSI.</td></tr><tr><td> $y_{2}$ </td><td>Proportion of Web service consumers of  $S_{2}$ subscribing to the WSI.</td></tr><tr><td> $y_{3}$ </td><td>Proportion of Web service consumers of  $S_{3}$ subscribing to the WSI.</td></tr><tr><td> $P_{1}$ </td><td>Price of Web service  $S_{1}$ .</td></tr><tr><td> $P_{2}$ </td><td>Price of Web service  $S_{2}$ .</td></tr><tr><td> $L$ </td><td>Listing fee charged by the WSI to Web service vendors.</td></tr><tr><td> $F$ </td><td>Subscription fee charged by the WSI to Web service consumers.</td></tr><tr><td> $v$ </td><td>Consumer&#x27;s valuation of the intrinsic value of the WSI, uniformly distributed in the interval [0,  $\bar{v}$ ].</td></tr><tr><td> $\gamma$ </td><td>Intensity of the cross-network externality effect.</td></tr></table>

## Consumers’ Subscription Decision

From the service consumer’s point of view, the added value offered by the WSI consists of intrinsic and network value. The intrinsic value is derived from the technical services offered by the WSI, such as tools for Web service integration, account management, enhanced security, and quality management via service-level agreement. The intrinsic value is related to the technical strength of the WSI and is independent of the number of service vendors listed on it. Obviously, the value of the technical services depends on the specific types of service provided by the WSI. However, we do not explicitly restrict our study to any specific type of service, for the sake of generality. The consumers are heterogeneous in their evaluation of the intrinsic value, characterized by a random variable v, uniformly distributed in the interval [0,v\]. Note that the upper bound of the distribution v\ is a representative measure of consumers valuation of the intrinsic value.

The network value for consumers derives from cross-network externality effect, which is increasing in the number of Web service vendors listed on the intermediary. Let γ indicate the intensity of the cross-network externality, or consumer’s valuation of the network effect. Following a common modeling approach in the literature, we let the network value to a consumer be $\gamma$ multiplied by the proportion of service vendors listed on the WSI (x ).

Web service consumers decide whether to subscribe to the WSI by evaluating the cost (subscription fee) and benefit from subscribing to it. For a customer who is interested in $S _ { 1 }$ , the total benefit from subscribing to the intermediary is $\nu + \gamma x _ { 1 }$ , where v is the consumer’s valuation of the intrinsic value and $\gamma x _ { 1 }$ is the network value. Let $\nu _ { 0 1 }$ be the valuation of the marginal consumer of $S _ { 1 }$ who is indifferent between subscribing and not subscribing to the WSI. Then for this marginal consumer of $S _ { 1 } ^ { \phantom { \dagger } }$ , the equation $\nu _ { 0 1 } + \gamma x _ { 1 } = F$ holds. Similarly, the marginal consumer of $S _ { 2 }$ with intrinsic value $\nu _ { 0 2 }$ is described by the equation $\nu _ { 0 2 } + \gamma x _ { 2 } = F$ . Consumers of $S _ { 1 }$ (or $S _ { 2 } )$ who subscribe to the WSI are those who have higher valuation than that of the marginal consumer, as specified in Equations (1a) to (1c). Note that if the subscription fee is prohibitively high, all consumers will stay away from the WSI (1b), while a sufficiently low subscription fee attracts all consumers to subscribe (1c).

![](/api/attachments/CCD68CVJ/fulltext/images/9141b1547f65c8b2f0ecb26834ef61e20416b6fd26dde0f1d3eaa419148fa4d5.jpg)  
Figure 2. The Model

$$
\left[ \left(\overline {{v}} - F + \gamma x _ {1}\right) \sqrt {v} \quad \text { if } \quad \gamma x _ {i} \leq \overline {{v}} + \gamma x _ {i} \right.\tag{1a}
$$

$$
y _ {i} \left(x _ {i}\right) = \left\{1 \quad \text { if } \quad F > \bar {v} + \gamma x _ {i} (\text { no   subscriber }) \right.\tag{1b}
$$

$$
i = 1, 2 \quad \left\lfloor 0 \quad \text {   if   } \quad F <   \gamma x _ {i} (\text {   all   subscribe   }) \right.\tag{1c}
$$

The consumer who is interested in the integrated Web service, $S _ { 3 } ,$ derives v + $\gamma x _ { 1 }$ + $\gamma x _ { 2 }$ benefit from subscribing to the WSI.<sup>2</sup> That is, the network value for the consumers of integrated service $S _ { 3 }$ is increasing in the proportions of listed service vendors of $S _ { 1 }$ and $S _ { 2 }$ . In accordance, the proportion of consumers of $S _ { 3 }$ who subscribe to the intermediary is as follows:

$$
\left\{ \begin{array}{l l} \frac {\bar {v} - F + \gamma x _ {1} + \gamma x _ {2}}{\bar {v}} & \text { if } \quad \gamma x _ {1} + \gamma x _ {2} \leq F \leq \bar {v} + \gamma x _ {1} + \gamma x _ {2} \end{array} \right.\tag{2a}
$$

$$
y _ {3} \left(x _ {1}, x _ {2}\right) = \left\{0 \quad \text { if } \quad F > \overline {{v}} + \gamma x _ {1} + \gamma x _ {2} (\text { no   subscriber }) \right.\tag{2b}
$$

$$
1 \quad \text { if } \quad F <   \gamma x _ {1} + \gamma x _ {2} (\text { all   subscribe })\tag{2c}
$$

## Service Vendor’s Listing Decision

When a WSI provides aggregation services such as advanced search with a more user-friendly interface, product reviews, and usage statistics, its subscribers often choose not to search the PBR, because it involves higher search cost with less relevant and useful outcome. On the other hand, nonsubscribers have to search through the PBR, which contains an entire list of service vendors. As a result, listing to the WSI helps the service vendors increase the chance of accomplishing transactions with more consumers (unless none of the consumers subscribe to the WSI) and reduce the competition from peer service vendors (if not all service vendors publish on the intermediary).

Given the proportions of consumers subscribing to the WSI $( y _ { 1 } , y _ { 2 } ,$ , and $y _ { 3 } )$ and assuming zero marginal cost of providing Web services, the profits for a service vendor to list $( \pi _ { i } ^ { I } )$ or not list $( \pi _ { i } ^ { N I } )$ on the WSI are formulated in Equations $( 3 )$ and (4), respectively, where the subscript i indicates types of Web services offered $( S _ { 1 } \mathrm { o r } S _ { 2 } )$ Notice that the demand of Web service $S _ { 1 } \left( S _ { 2 } \right)$ comes from both the consumers of $S _ { 1 }$ $( S _ { 2 } )$ and those of the integrated Web service $S _ { 3 }$

$$
\pi_ {i} ^ {I} = \left(\frac {1 - y _ {i}}{N _ {i}} + \frac {y _ {i}}{x _ {i} N _ {i}}\right) P _ {i} Q _ {i} + \left(\frac {1 - y _ {3}}{N _ {i}} + \frac {y _ {3}}{x _ {i} N _ {i}}\right) P _ {i} Q _ {3} - L, i = 1, 2\tag{3}
$$

$$
\pi_ {i} ^ {N I} = \frac {1 - y _ {i}}{N _ {i}} P _ {i} Q _ {i} + \frac {1 - y _ {3}}{N _ {i}} P _ {i} Q _ {3}, i = 1, 2.\tag{4}
$$

A Web service vendor of $S _ { 1 }$ will choose to list on the WSI if $\pi _ { i } ^ { I } \geq \pi _ { i } ^ { N I }$ holds.<sup>3</sup> Hence, one derives the proportion of service vendors listing on the WSI from the equation $\pi _ { i } ^ { { \cal N } } = \pi _ { i } ^ { I } \left( i = 1 , 2 \right)$ , described in Equation (5). Like the consumer side, the intermediary will attract all service vendors if the listing fee is low enough. It is interesting to observe from Equation (5) that although a high subscription fee will drive all consumers away from the intermediary, a high listing fee will not deter all service vendors. This is because those consumers who subscribe to the intermediary will not search beyond the WSI, creating a niche market for those service vendors listed on the WSI.

$$
x _ {i} \left(y _ {i}, y _ {3}\right) = \left\{ \begin{array}{l l} \frac {\left(y _ {i} Q _ {i} + y _ {3} Q _ {3}\right) P _ {i}}{L N _ {i}} & \text { if } L \geq \frac {\left(y _ {i} Q _ {i} + y _ {3} Q _ {3}\right) P _ {i}}{N _ {i}} \\ 1 & \text { otherwise. } \end{array} \right.\tag{5}
$$

## Optimal Strategies for a Web Service Intermediary

AFTER DERIVING THE RESPONSE FUNCTIONS of service vendors and consumers, we solve for the optimal subscription fee and listing fee problem facing the WSI, resulting in Equation (6). The initial setup cost for the WSI is sunk and the marginal operational cost incurred by the intermediary is assumed to be negligible.

$$
\max _ {L, F} \Pi = \left(y _ {1} Q _ {1} + y _ {2} Q _ {2} + y _ {3} Q _ {3}\right) F + \left(x _ {1} N _ {1} + x _ {2} N _ {2}\right) L\tag{6}
$$

subject to (1a)–(1c), (2a)–(2c), and (5).

Lemma 1: The optimal strategy for the WSI is to induce all service vendors to list on it, that is, $x _ { I } = x _ { 2 } = I .$ . The WSI will set the listing fee at $L = m i n \{ L _ { I } , L _ { 2 } \}$ , where $L _ { i } = ( ( y _ { i } Q _ { i } + y _ { 3 } Q _ { 3 } ) P _ { i } ) / N _ { \dot { r } } i = I , 2 .$

## Proof: See the Appendix

Lemma 1 specifies that the listing fee should be low enough such that all service vendors list on the WSI $( x _ { 1 } = x _ { 2 } = 1 )$ ). Knowing the optimal strategy toward the Web service vendors, we are naturally confronted with the next question: Should the WSI attract all customers to subscribe? Lemma 2 suggests that it is not the case.

Lemma 2: The WSI’s profit is not always maximized when all customers subscribe to its service, that is, $y _ { I } = y _ { 2 } = y _ { 3 } = I$

## Proof: See the Appendix

Lemma 2 indicates the optimal subscription fee is yet to be determined. Substituting the optimal listing fee obtained from Lemma 1, we transform the profit-maximizing problem into finding the optimal subscription fee as follows:

$$
\max _ {F} \Pi = \left(y _ {1} Q _ {1} + y _ {2} Q _ {2} + y _ {3} Q _ {3}\right) F + \left(y _ {1} Q _ {1} + y _ {3} Q _ {3}\right) P _ {1} + \left(y _ {2} Q _ {2} + y _ {3} Q _ {3}\right) P _ {2}\tag{7}
$$

subject to (1a)–(1c) and (2a)–(2c).

Note from (1a)–(1c) and (2a)–(2c) that the functional form of the proportions of subscribers $( y _ { j } )$ is conditional on the value of subscription fee F. The WSI’s profit function is determined by the value of the subscription fee. In order to solve for the optimal subscription fee, we will compare the profits under every possible combination of $y _ { j } \left( j = 1 , 2 , 3 \right)$ . Furthermore, notice that the proportion of consumers who subscribe varies under different relationships of $\gamma$ and v\ given the subscription fee. For example, if the WSI charges the subscription fee at $\bar { \nu } + \gamma ,$ all consumers of $S _ { 3 }$ will subscribe to it $\operatorname { i f } \gamma > \bar { \nu }$ , while only a proportion of consumers of $S _ { 3 }$ will subscribe if γ $< \bar { \nu } .$ . In the following two subsections, we solve for the optimal subscription fee $F ^ { * }$ by analyzing the WSI’s profits under different values of $\gamma$ and $\bar { \nu } .$

## Scenario I: The Network Value Is Less Than the Intrinsic Value $( \gamma < \bar { \nu } )$

When the network value is less than the intrinsic value for consumers $( \gamma < \bar { \nu } )$ , the proportion of customers who subscribe to the WSI can be categorized into three subcases under different settings of the subscription fee $( F )$ , as illustrated in Figure 3. If the subscription fee is between γ and $2 \gamma ,$ some customers of $S _ { 1 }$ and $S _ { 2 }$ will subscribe while all customers of $S _ { 3 }$ will subscribe (case I-1). If the subscription fee is between 2γ and $\bar { \nu } + \gamma _ { ; }$ some customers of $S _ { 1 } , S _ { 2 } ,$ and $S _ { 3 }$ will subscribe (case I-2). If the subscription fee is between $\bar { \nu } + \gamma$ and $\bar { \nu } + 2 \gamma$ , none of $S _ { 1 }$ and $S _ { 2 }$ customers will subscribe while

![](/api/attachments/CCD68CVJ/fulltext/images/f2ef3c8f51fae663890eefc4720b5a0a2e73e6f19f845175f5f5d4524890ebe7.jpg)

$$
\gamma \leq F \leq 2 \gamma (0 <   y _ {1}, y _ {2} \leq 1, y _ {3} = 1)
$$

$$
2 \gamma \leq F \leq \overline {{{\nu}}} + \gamma (0 <   y _ {1}, y _ {2}, y _ {3} <   1)
$$

$$
\overline {{{v}}} + \gamma \leq F \leq \overline {{{v}}} + 2 \gamma \left(y _ {1} = y _ {2} = 0, 0 \leq y _ {3} <   1\right)
$$

Figure 3. Scenario I $( \gamma < \bar { \nu } )$

some customers of $S _ { 3 }$ will subscribe (case I-3). Obviously, the WSI has no incentive to set the subscription fee lower than γ or higher than $\bar { \nu } + 2 \gamma .$ , because the market is saturated under subscription fee at γ and no customer will subscribe in the latter case.

We first derive the locally optimal subscription fee that maximizes the WSI’s profit in each subcase. The overall optimal subscription fee (when $\gamma < \bar { \nu } )$ is found as the one that generates the maximum profit among all three subcases.

Case I-1: $\gamma \leq F \leq 2 \gamma$

If the subscription fee charged by the intermediary is between γ and $2 \gamma ,$ all customers of $S _ { 3 }$ will subscribe while only some customers of $S _ { 1 }$ and $S _ { 2 }$ will subscribe. That is, we have $0 < y _ { 1 } , y _ { 2 } \leq 1$ and $y _ { 3 } = 1$ in this case. Correspondingly, the profit-maximization problem for the WSI is defined as follows:

$$
\max _ {F} \Pi_ {1 1} = \left[ \frac {\bar {v} + \gamma - F}{\bar {v}} \left(Q _ {1} + Q _ {2}\right) + Q _ {3} \right] F + \sum_ {i = 1} ^ {2} \left(\frac {\bar {v} + \gamma - F}{\bar {v}} Q _ {i} + Q _ {3}\right) P _ {i}\tag{8}
$$

subject to $\gamma \leq F \leq 2 \gamma$

Lemma 3: If the network value is less than the intrinsic value $( \gamma < \bar { \nu } )$ and $\gamma \le F \le$ $2 \gamma ,$ the optimal subscription fee that maximizes the WSI’s profit $( F _ { I I } { } ^ { * } )$ is specified as follows:

$$
\text {   If   } \frac {\left(\bar {v} - P _ {1}\right) Q _ {1} + \left(\bar {v} - P _ {2}\right) Q _ {2} + \bar {v} Q _ {3}}{\left(Q _ {1} + Q _ {2}\right)} \leq \gamma <   \bar {v}, \quad F _ {1 1} ^ {*} = \gamma\tag{9a}
$$

$$
\begin{array}{c} \text {   If   } \frac {\left(\overline {{v}} - P _ {1}\right) Q _ {1} + \left(\overline {{v}} - P _ {2}\right) Q _ {2} + \overline {{v}} Q _ {3}}{3 \left(Q _ {1} + Q _ {2}\right)} <   \gamma <   \frac {\left(\overline {{v}} - P _ {1}\right) Q _ {1} + \left(\overline {{v}} - P _ {2}\right) Q _ {2} + \overline {{v}} Q _ {3}}{Q _ {1} + Q _ {2}}, \\ F _ {1 1} ^ {*} = F _ {1 1}, \end{array}\tag{9b}
$$

where $F _ { I I }$ is defined as

$$
F _ {1 1} = \frac {\left(\bar {v} + \gamma - P _ {1}\right) Q _ {1} + \left(\bar {v} + \gamma - P _ {2}\right) Q _ {2} + \bar {v} Q _ {3}}{2 \left(Q _ {1} + Q _ {2}\right)}
$$

$$
\text {   If   } 0 <   \gamma \leq \frac {\left(\overline {{v}} - P _ {1}\right) Q _ {1} + \left(\overline {{v}} - P _ {2}\right) Q _ {2} + \overline {{v}} Q _ {3}}{3 \left(Q _ {1} + Q _ {2}\right)}, \quad F _ {1 1} ^ {*} = 2 \gamma .\tag{9c}
$$

Proof: Lemma 3 is derived by solving the constrained optimization problem in Equation (8). See the Appendix for a detailed derivation.

Case I-2: $2 \gamma \leq F \leq \bar { \nu } + \gamma$

If the subscription fee charged by the WSI is between $2 \gamma$ and $\bar { \nu } + \gamma _ { ; }$ , only a portion of customers of $S _ { 1 } , S _ { 2 } ,$ , and $S _ { 3 }$ will subscribe, that is, $0 < y _ { j } < 1 , j = 1 , 2 , 3$ . Correspondingly, the WSI’s profit-maximization problem is defined as follows:

$$
\begin{array}{l} \max _ {F} \Pi_ {1 2} = \left[ \frac {\overline {{v}} + \gamma - F}{\overline {{v}}} \left(Q _ {1} + Q _ {2}\right) + \frac {\overline {{v}} + 2 \gamma - F}{\overline {{v}}} Q _ {3} \right] F \\ \quad + \sum_ {i = 1} ^ {2} \left(\frac {\overline {{v}} + \gamma - F}{\overline {{v}}} Q _ {i} + \frac {\overline {{v}} + 2 \gamma - F}{\overline {{v}}} Q _ {3}\right) P _ {i} \end{array}\tag{10}
$$

subject to $2 \gamma \leq F \leq \bar { \nu } + \gamma$

Lemma 4: If the network value is less than the intrinsic value $( \gamma < \bar { \nu } )$ and $2 \gamma \leq$ $F \leq \bar { \nu } + \gamma ,$ the profit-maximizing subscription fee $( { F _ { I 2 } } ^ { * } )$ is specified as follows:

$$
\text {   If   } 0 \leq \gamma <   \frac {\left(\overline {{v}} - P _ {1}\right) Q _ {1} + \left(\overline {{v}} - P _ {2}\right) Q _ {2} + \left(\overline {{v}} - P _ {1} - P _ {2}\right) Q _ {3}}{3 Q _ {1} + 3 Q _ {2} + 2 Q _ {3}}, \quad F _ {1 2} ^ {*} = F _ {1 2},\tag{11a}
$$

where $\mathrm { F } _ { I 2 }$ is defined as

$$
F _ {1 2} = \frac {\left(\bar {v} + \gamma - P _ {1}\right) Q _ {1} + \left(\bar {v} + \gamma - P _ {2}\right) Q _ {2} + \left(\bar {v} + 2 \gamma - P _ {1} - P _ {2}\right) Q _ {3}}{2 \left(Q _ {1} + Q _ {2} + Q _ {3}\right)}
$$

$$
\text {   If   } \frac {\left(\overline {{v}} - P _ {1}\right) Q _ {1} + \left(\overline {{v}} - P _ {2}\right) Q _ {2} + \left(\overline {{v}} - P _ {1} - P _ {2}\right) Q _ {3}}{3 Q _ {1} + 3 Q _ {2} + 2 Q _ {3}} \leq \gamma <   \overline {{v}}, \quad F _ {1 2} ^ {*} = 2 \gamma .\tag{11b}
$$

Proof: Lemma 4 is drawn from solving Equation (10). The proof is similar to that of Lemma 3. Q.E.D.

Case I-3: $\bar { \nu } + \gamma \leq F \leq \bar { \nu } + 2 \gamma$

If the subscription fee charged by the intermediary is between $\bar { \nu } + \gamma$ and $\bar { \nu } + 2 \gamma .$ , no customers of $S _ { 1 }$ and $S _ { 2 }$ will subscribe while some customers of $S _ { 3 }$ will subscribe, that is, $y _ { 1 } = y _ { 2 } = 0$ and $0 \leq y _ { 3 } < 1$ . Correspondingly, the intermediary’s profit-maximization problem is defined as follows:

$$
\max _ {F} \Pi_ {1 3} = \frac {\bar {v} + 2 \gamma - F}{\bar {v}} Q _ {3} F + (P _ {1} + P _ {2}) \frac {\bar {v} + 2 \gamma - F}{\bar {v}} Q _ {3}\tag{12}
$$

subject to $\bar { \nu } + \gamma \leq F \leq \bar { \nu } + 2 \gamma$

Lemma 5: If the network value is less than the intrinsic value $( \gamma < \bar { \nu } )$ and $\bar { \nu } + \gamma \leq$ $F \leq \bar { \nu } + 2 \gamma ,$ the subscription fee that maximizes the profit of the intermediary is ${ F _ { I 3 } } ^ { * } = \bar { \nu } + \gamma .$

Proof: We derive Lemma 5 by solving the constrained optimization problem in Equation (12). Q.E.D.

Proposition 1: If the network value is less than the intrinsic value $( \gamma < \bar { \nu } )$ , the optimal subscription fee charged by the intermediary is specified in (13a) to (13d), where

$$
\gamma_ {1 1} = \frac {\left(\bar {v} - P _ {1}\right) Q _ {1} + \left(\bar {v} - P _ {2}\right) Q _ {2} + \left(\bar {v} - P _ {1} - P _ {2}\right) Q _ {3}}{3 Q _ {1} + 3 Q _ {2} + 2 Q _ {3}}
$$

$$
\gamma_ {1 2} = \frac {\left(\bar {v} - P _ {1}\right) Q _ {1} + \left(\bar {v} - P _ {2}\right) Q _ {2} + \bar {v} Q _ {3}}{3 \left(Q _ {1} + Q _ {2}\right)}
$$

$$
\gamma_ {1 3} = \frac {\left(\overline {{v}} - P _ {1}\right) Q _ {1} + \left(\overline {{v}} - P _ {2}\right) Q _ {2} + \overline {{v}} Q _ {3}}{Q _ {1} + Q _ {2}}.
$$

$$
\text {   If   } 0 \leq \gamma <   \gamma_ {1 1},\tag{13a}
$$

the optimal subscription fee is $F _ { _ { I 2 } } ,$ defined in Equation (11a) of Lemma 4. Only some customers of $\dot { S } _ { I } , S _ { 2 } ,$ , and $S _ { 3 }$ will subscribe, that is, $\theta < y _ { j } < I \ ( j = I , 2 , 3 )$ .

$$
\text {   If   } \gamma_ {1 1} \leq \gamma <   \gamma_ {1 2},\tag{13b}
$$

the optimal subscription fee is $2 \gamma .$ . All $S _ { 3 }$ customers will subscribe while some customers of $S _ { I }$ and $S _ { 2 }$ will subscribe, that is, $y _ { 3 } = I$ and $O < y _ { I } , y _ { 2 } < I$

$$
\text {   If   } \gamma_ {1 2} \leq \gamma <   \gamma_ {1 3},\tag{13c}
$$

the optimal subscription fee is $F _ { _ { I I } } ,$ , defined in Equation (9b) of Lemma 3. All $S _ { 3 }$ customers will subscribe while only some customers $o f S _ { I }$ and S will subscribe, that is, $y _ { 3 } = I$ and $O < y _ { I } , y _ { 2 } < I .$

$$
\text {   If   } \gamma_ {1 3} \leq \gamma <   \overline {{v}},\tag{13d}
$$

the optimal subscription fee is . All customers will subscribe, that is, $y _ { j } = l ( j =$ 1,2,3).

Proof: See the Appendix.

Proposition 1 suggests that the optimal subscription fee is conditional on the intensity of cross-network externality $( \gamma )$ . Notice that $\gamma _ { 1 1 } < \gamma _ { 1 2 } < \gamma _ { 1 3 }$ which implies that as the intensity of the network effect increases, or consumers’ valuation of the network value increases, the intermediary tends to set the subscription fee to allow more customers to subscribe, because the proportions of customers (y ) who subscribe increase from (13a) to (13d). Next we summarize the behaviors of optimal subscription fee and profit with respect to cross-network intensity in Proposition 2.

Proposition 2: When the network value is less than the intrinsic value $( \gamma < \bar { \nu } ) _ { ; }$ , the optimal subscription fee and optimal profit are increasing in cross-network intensity ( ).

Proof: By inspection, the subscription fee is increasing in cross-network intensity in each scenario according to (13a) to (13d) of Proposition 1. Next note that the subscription fee coincides at the conjunction of successive cases from (13a) to (13d). Overall, the optimal subscription increases with cross-network externality intensity. The network effect has similar effect on the optimal profit for the intermediary. Q.E.D.

Figures 4 and 5 illustrate the optimal subscription fee and profit with respect to γ when the network value is less than the intrinsic value $( \gamma < \bar { \nu } )$

Another interesting observation from Proposition 1 is that the WSI has more incentive to serve customers of the integrated Web service $( S _ { 3 } )$ than to serve customers who need the individual Web services. Unless the network effect is very large (see (13d) in Proposition 1), the WSI only wants to allow partial customers of $S _ { 1 }$ and $S _ { 2 }$ to subscribe. In contrast, the WSI will set the subscription fee to attract all customers of $S _ { 3 }$ except for the case where the network externality is as described in (13a) of Proposition 1. Corollaries 1 and 2 present more managerial insights by analyzing the effect of intrinsic value (v\) on the optimal subscription fee.

Corollary 1a: The WSI will set the subscription fee to attract all customers of $S _ { I } ,$ $S _ { 2 } , S _ { 3 }$ to subscribe $i f \bar { \nu } < \bar { V } _ { a } ,$ , where

$$
\overline {{V}} _ {a} = \frac {P _ {1} Q _ {1} + P _ {2} Q _ {2}}{Q _ {1} + Q _ {2} + Q _ {3}}
$$

Subscription Fee  
![](/api/attachments/CCD68CVJ/fulltext/images/5145b525ddb4f809d2424f408468742df1cbfe326f0f46807024029976862eb3.jpg)  
Figure 4. Impact of Network Effect on Optimal Subscription Fee Parameters: $Q _ { 1 } = 1 0 0 , Q _ { 2 } = 1 5 0 , Q _ { 3 } = 9 0 , P _ { 1 } = 5 , P _ { 2 } = 2 , \bar { \nu } = 5 , \gamma _ { 1 1 } = 0 . 2 9 , \gamma _ { 1 2 } = 1 . 2 , \gamma _ { 1 3 } = 3 . 6 .$

![](/api/attachments/CCD68CVJ/fulltext/images/3d6791500c146267f6c2929a010fe378548b52e26c8ac81a7a4037fdbf6073e4.jpg)  
Figure 5. Impact of Network Effect on Optimal Profit  
Parameters: $Q _ { 1 } = 1 0 0 , Q _ { 2 } = 1 5 0 , Q _ { 3 } = 9 0 , P _ { 1 } = 5 , P _ { 2 } = 2 , \bar { \nu } = 5 , \gamma _ { 1 1 } = 0 . 2 9 , \gamma _ { 1 2 } = 1 . 2 , \gamma _ { 1 3 } = 3 . 6 .$

Corollary 1b: The WSI will set the subscription fee to attract all customers of $\dot { S } _ { 3 }$ to subscribe $i f \bar { \nu } < \bar { V } _ { b } ,$ where

$$
\overline {{V}} _ {b} = \frac {P _ {1} Q _ {1} + P _ {2} Q _ {2} + (P _ {1} + P _ {2}) Q _ {3}}{Q _ {1} + Q _ {2} + Q _ {3}}.
$$

Proof: $I f \gamma _ { I 3 } < 0 ,$ condition (13d) is always satisfied, thus suggesting $\gamma$ as the optimal subscription fee. Further, $i f \gamma _ { _ { I I } } < 0 ,$ , the condition specified in (13a) will never be satisfied. Therefore, the optimal subscription fee must be realized in one of the remaining cases, which all suggest total subscription from customers of $\cdot _ { S _ { 3 } , }$ that is, $y _ { 3 } = I , Q . E . D$

Corollary 2: The WSI will not serve all customers of $\therefore S _ { I } , S _ { 2 } ,$ , and $S _ { 3 } i f \bar { \nu } > \underline { { { V } } }$ where

$$
\underline {{V}} = \frac {P _ {1} Q _ {1} + P _ {2} Q _ {2}}{Q _ {3}}.
$$

Proof: To attract all customers to subscribe, the intermediary has to set the subscription fee at . According to Proposition 1, the subscription fee  is optimal only when $\gamma _ { I 3 } \leq \gamma < \bar { \nu } .$ . However, $i f \gamma _ { I 3 } > \bar { \nu } ,$ which translates to $\bar { \nu } > \underline { { { V } } }$ the condition in (13d) can never be satisfied. Q.E.D.

Corollaries 1 and 2 are derived based on the optimal subscription fee described in Proposition 1, suggesting that the optimal subscription fee is affected by the value of technical services provided by the WSI and such market characteristics as prices and market sizes of underlying Web services. In particular, Corollaries 1 and 2 discuss the special cases when the WSI desires to set a low or high subscription fee to get a certain level of consumer subscription rate.

Corollary 1 specifies the condition under which the WSI has incentive to attract more customers to subscribe. Specifically, the WSI wants to attract more customers (even all of them) to subscribe if the value of the technical service is not sufficiently high. By comparing the conditions in Corollary (1a) and (1b), one observes that the WSI has less incentive to attract subscriptions from consumers when the technical value increases. In addition, the threshold value of technical services $\bar { V } _ { a } \ ( \mathrm { o r } \ \bar { V } _ { b } )$ is increasing in the weighted average price of the Web services. This implies that higher prices of the individual Web services $( S _ { 1 } \mathrm { o r } S _ { 2 } )$ will lead to a higher subscription rate by the customers. On the other hand, Corollary 2 specifies the condition under which the WSI desires to attract fewer consumers. Specifically, if the consumers have relatively high valuations of the technical services, the intermediary will not set a low subscription fee to attract all customers. In contrast to Corollary 1, we find that lower prices of the Web services cut the threshold value of V and thus will lead to a lower subscription rate by the customers. Furthermore, if the integrated Web service enjoys a large market size $( Q _ { 3 } )$ , it is more likely that the condition specified in Corollary 2 will be satisfied, implying that the WSI will not set the subscription fee low to attract all customers.

## Scenario II: The Network Value Is Higher Than the Intrinsic Value $( \gamma > \bar { \nu } )$

Similar analysis can be applied to the second scenario where consumers place a higher value on network value (aggregation services) than intrinsic value (technical services). The proportion of customers who subscribe with different subscription fees is illustrated in Figure $^ { 6 , }$ which has three subcases. If the subscription fee is between γ and v $+ \gamma ,$ some consumers of $S _ { 1 }$ and $S _ { 2 }$ will subscribe while all customers of $S _ { 3 }$ will subscribe (case II-1). If the subscription fee is between $\bar { \nu } + \gamma$ and $2 \gamma$ , none of $S _ { 1 }$ and $S _ { 2 }$ customers will subscribe while all customers of $S _ { 3 }$ will subscribe (case $\left[ \left[ - 2 \right) \right.$ . If the subscription fee is between $2 \gamma$ and $\bar { \nu } + 2 \gamma$ , some customers of $S _ { 3 }$ will subscribe while no customer of $S _ { 1 }$ and $S _ { 2 }$ will subscribe (case II-3). The optimal subscription fee in this scenario is derived by calculating and comparing the WSI’s profits in all three subcases using the similar approach in Scenario I. As in Scenario I, we exclude the situations when the subscription fee is too low (less than $\gamma )$ or too high (greater than $\bar { \nu } + 2 \gamma )$ .

Case II-1: $\gamma \leq F \leq \bar { \nu } + \gamma$

If the subscription fee is between γ and $\bar { \nu } + \gamma ,$ all customers of $S _ { 3 }$ will subscribe while only some consumers of $S _ { 1 }$ and $S _ { 2 }$ will subscribe, that is, $0 < y _ { 1 } , y _ { 2 } < 1$ and $y _ { 3 } = 1$ . The WSI’s profit function is the same as defined in Case I-1. Note, however, that the value of the subscription fee is different from that of Case I-1 $( \gamma \leq F \leq \bar { \nu } + \gamma )$ .

Lemma 6: When the network value is greater than the intrinsic value $( g < \bar { \nu } )$ and $\begin{array} { r } { \gamma \le F \le \bar { \nu } + \gamma , } \end{array}$ the subscription fee that maximizes the profit of the WSI (F <sup>\*</sup>) is specified as follows.

$$
\text {   If   } \bar {v} \leq \gamma \leq \frac {\bar {v} Q _ {3} - (\bar {v} + \gamma + P _ {1}) Q _ {1} - (\bar {v} + \gamma + P _ {2}) Q _ {2}}{Q _ {1} + Q _ {2}}, \quad F _ {2 1} ^ {*} = \bar {v} + \gamma\tag{14a}
$$

$$
\begin{array}{l} \text {   If   } \frac {\overline {{v}} Q _ {3} - (\overline {{v}} + P _ {1}) Q _ {1} - (\overline {{v}} + P _ {2}) Q _ {2}}{Q _ {1} + Q _ {2}} <   \gamma \\ <   \frac {(\overline {{v}} - P _ {1}) Q _ {1} + (\overline {{v}} - P _ {2}) Q _ {2} + \overline {{v}} Q _ {3}}{Q _ {1} + Q _ {2}}, \quad F _ {2 1} ^ {*} = F _ {2 1} \end{array}\tag{14b}
$$

where $F _ { 2 l }$ is defined as

$$
F _ {2 1} = \frac {\left(\bar {v} + \gamma - P _ {1}\right) Q _ {1} + \left(\bar {v} + \gamma - P _ {2}\right) Q _ {2} + \bar {v} Q _ {3}}{2 \left(Q _ {1} + Q _ {2}\right)}
$$

$$
\text {   If   } \gamma \geq \frac {\left(\overline {{v}} - P _ {1}\right) Q _ {1} + \left(\overline {{v}} - P _ {2}\right) Q _ {2} + \overline {{v}} Q _ {3}}{Q _ {1} + Q _ {2}}, \quad F _ {2 1} ^ {*} = \gamma .\tag{14c}
$$

![](/api/attachments/CCD68CVJ/fulltext/images/b72de8ed3b43f5d07aa92adb0f57c763683eaa1038fcc47b05c458c96cb19cdc.jpg)  
Figure 6. Scenario II (γ > v\)

Proof: This lemma results from the same approach used in proving Lemma $3 .$ $Q . E . D .$

Case II-2: $\bar { \nu } + \gamma \leq F \leq 2 \gamma$

If the subscription fee is between $\bar { \nu } + \gamma$ and $2 \gamma .$ , all customers of $S _ { 3 }$ will subscribe while no customer of $S _ { 1 }$ or $S _ { 2 }$ will subscribe to the WSI, that is, $y _ { 1 } = y _ { 2 } = 0$ and $y _ { 3 } = 1$ Because all customers of $S _ { 3 }$ will subscribe regardless of the subscription fee in Case II-2, the WSI will set the subscription fee at $2 \gamma .$ , which is the highest subscription fee the WSI can charge. Case II-2 can be viewed as a special case of Case II-3 to be discussed below.

## Case II-3: 2γ $\leq F \leq \bar { \nu } + 2 \gamma$

If the subscription fee is between $2 \gamma$ and $\bar { \nu } + 2 \gamma$ , no customer of $S _ { 1 }$ or S will subscribe while some consumers of $S _ { 3 }$ will subscribe, that is, $y _ { 1 } = y _ { 2 } = 0$ and $0 \le y _ { 3 } \le 1$ . The profit-maximization problem for the WSI is same as defined in Case I-3, except for different settings of the subscription fee $( 2 \gamma \leq F \leq \bar { \nu } + 2 \gamma )$ .

Lemma 7: When the consumers have a higher valuation of the network value than the intrinsic value $( g > \bar { \nu } )$ and the WSI desires to attract subscription from $S _ { 3 }$ customers only, the subscription fee that maximizes the profit of the intermediary is ${ F _ { 2 3 } } ^ { * } = 2 \gamma$

Proof: The proof is similar to that of Lemma 5. Q.E.D.

Proposition 3: When the consumers have a higher valuation of the network value than the intrinsic value $( \gamma > \bar { \nu } ) _ { ; }$ , the optimal subscription fee charged by the WSI is described as follows, where

$$
\gamma_ {2 1} = \frac {\overline {{v}} Q _ {3} - (\overline {{v}} + P _ {1}) Q _ {1} - (\overline {{v}} + P _ {2}) Q _ {2}}{Q _ {1} + Q _ {2}}
$$

and

$$
\gamma_ {2 2} = \frac {\left(\bar {v} - P _ {1}\right) Q _ {1} + \left(\bar {v} - P _ {2}\right) Q _ {2} + \bar {v} Q _ {3}}{Q _ {1} + Q _ {2}}
$$

$$
\text {   If   } \overline {{v}} \leq \gamma \leq \gamma_ {2 1},\tag{15a}
$$

the optimal subscription fee is $2 \gamma . A l l$ customers of $S _ { 3 }$ will subscribe while no customer of $S _ { I }$ or $S _ { 2 }$ will subscribe, that is, $y _ { I } = y _ { 2 } = O$ and $y _ { 3 } = I$

$$
\text {   If   } \gamma_ {2 1} <   \gamma <   \gamma_ {2 2},\tag{15b}
$$

the WSI’s optimal strategy is to set the subscription fee such that all customers of $S _ { 3 }$ subscribe while some consumers of $\dot { \mathbf { \nabla } } S _ { I }$ or $S _ { 2 }$ subscribe, that is, $y _ { 3 } = I$ and $O <$ $y _ { I } , y _ { 2 } \leq I .$ . Specifically, the optimal subscription fee is

$$
F ^ {*} = \left\{ \begin{array}{l l} F _ {2 1} & \text { if } \Phi \geq 0 \\ 2 \gamma & \text { if } \Phi <   0 \end{array} \right.
$$

where $F _ { 2 I }$ is defined in (14b) and

$$
\begin{array}{c} \Phi = \Big [ \big (\overline {{v}} + \gamma + P _ {1} \big) Q _ {1} + \big (\overline {{v}} + \gamma + P _ {2} \big) Q _ {2} - \overline {{v}} Q _ {3} \Big ] ^ {2} \\ + 4 \overline {{v}} \big (\overline {{v}} - \gamma \big) \big (Q _ {1} + Q _ {2} \big) Q _ {3}. \end{array}
$$

$$
\text {   If   } \gamma \geq \gamma_ {2 2},\tag{15c}
$$

the optimal subscription fee charged by the WSI is as follows.

$$
F ^ {*} = \left\{ \begin{array}{l l} \gamma & \text { if } \Psi > 0 \\ 2 \gamma & \text { if } \Psi \leq 0 \end{array} \right.
$$

where $\psi = \gamma \cdot ( Q _ { I } + Q _ { 2 } - Q _ { 3 } ) + P _ { I } Q _ { I } + P _ { 2 } Q _ { 2 } .$

The WSI attracts all $S _ { 3 }$ customers to subscribe. All customers of $S _ { I }$ and $S _ { 2 }$ will subscribe $\begin{array} { r } { { \mathfrak { j } } f F ^ { * } = \gamma ; } \end{array}$ or no customer of $S _ { I } o r S _ { 2 }$ will subscribe $i f F ^ { * } = 2 \gamma .$

Proof: See the Appendix.

Scenario II $( \gamma > \bar { \nu } )$ is a bit more complex than Scenario I $( \gamma < \bar { \nu } )$ , as we do not have conclusive solutions for the optimal subscription fee under conditions (15b) and (15c). Nonetheless, we observe that the optimal subscription fee is dependent on the value of services provided by the WSI and the market characteristics of the underlying Web services (price and market size). Figures 7 and 8 give an example of the optimal subscription fee with respect to the cross-network intensity under conditions (15b) and (15c). The crossover points designate the change of optimal subscription fee due to switching signs of Φ and Ψ. We investigate the managerial implications of the optimal subscription fee in this scenario with respect to different settings of v\, P, and Q in Corollaries 3, 4, 5, and 6.

![](/api/attachments/CCD68CVJ/fulltext/images/0d8088cb24338741220b025dd91f0ac42e08c0b9e8037e5e79e9732476e0dcb0.jpg)  
Figure 7. Optimal Subscription Fee Depends on Φ $( \gamma _ { 2 1 } < \gamma < \gamma _ { 2 2 } )$ $Q _ { 1 } = 8 0 , Q _ { 2 } = 8 0 , Q _ { 3 } = 2 0 0 , P _ { 1 } = 1 , P _ { 2 } = 1 , \bar { \nu } = 1 0 .$

![](/api/attachments/CCD68CVJ/fulltext/images/c60d29ad045c8ea338e0cd9257855cb5c8905d347074a2687d58b7a2c44a7dbf.jpg)  
Figure 8. Optimal Subscription Fee Depends on $\Psi \left( \gamma > \gamma _ { 2 2 } \right)$ $Q _ { 1 } = 8 0 , Q _ { 2 } = 8 0 , Q _ { 3 } = 2 0 0 , P _ { 1 } = 1 , P _ { 2 } = 1 , \bar { \nu } = 1 0 .$

Corollary 3: When the consumers have a higher valuation of the network value than the intrinsic value $( \gamma > \bar { \nu } ) ,$ , the WSI will not attract all customers $i f Q _ { I } + Q _ { 2 } <$ Q3 and

$$
\overline {{v}} > \frac {P _ {1} Q _ {1} + P _ {2} Q _ {2}}{Q _ {3} - Q _ {1} - Q _ {2}}.
$$

Proof: According to (15c) of Proposition 3, the WSI will attract all customers to subscribe $i f \psi > 0 .$ Because  is negative when $Q _ { I } + Q _ { 2 } < Q _ { 3 }$ and $\nu > ( P _ { I } Q _ { I } +$ $P _ { 2 } Q _ { 2 } ) / ( Q _ { 3 } - Q _ { I } - Q _ { 2 } )$ , this implies that the WSI will not attract all customers to subscribe. Q.E.D.

Corollary 4: When the consumers have a higher valuation of the network value than the intrinsic value $( \gamma > \bar { \nu } ) ,$ , the WSI will set the subscription fee at $2 \gamma$ to attract all customers of $S _ { 3 }$ while turning away customers of $S _ { I }$ or $S _ { 2 } ~ i f 2 ( Q _ { I }$ + $ { { \cal Q } } _ { 2 } ) <  { { \cal Q } } _ { 3 }$ and

$$
\overline {{v}} \geq \frac {P _ {1} Q _ {1} + P _ {2} Q _ {2}}{Q _ {3} - 2 Q _ {1} - 2 Q _ {2}}.
$$

Proof: We show that under the conditions specified in Corollary 4, the following inequalities hold: $\gamma _ { _ { 2 I } } > \bar { \nu } , \phi < 0 ,$ , and $\psi _ { < } O .$ A detailed proof is relegated to the Appendix. Q.E.D.

Corollary 5: When the consumers have a higher valuation of the network value than the intrinsic value $( \gamma > \bar { \nu } ) ,$ , the optimal subscription fee charged by the intermediary is $i f Q _ { I } + Q _ { 2 } > Q _ { 3 }$ and $\gamma > \gamma _ { 2 2 } .$

Proof: It can be shown by inspection of condition (15c) that  is positive when $Q _ { I } + Q _ { 2 } > Q 3 . \ Q . E . D .$

Corollary 6: When the consumers have a higher valuation of the network value than the intrinsic value $( \gamma > \bar { \nu } )$ , the optimal subscription fee is increasing in cross-network intensity $i f 2 ( Q _ { I } + Q _ { 2 } ) < Q .$ 3

Proof: We show that under the conditions specified, the trajectory of the optimal subscription fee falls into one of the following three possible cases: (1) 2 for the entire region $\gamma > \bar { \nu } , ( 2 ) F _ { 2 I }$ when $\gamma _ { 2 I } ,$ ,  and then 2 when $\gamma > \gamma _ { 2 2 } ,$ and $( 3 ) F _ { 2 I }$ and then 2 for the region $\gamma _ { 2 I } < \gamma < \gamma _ { 2 2 } ,$ , then 2 for $\gamma > \gamma _ { 2 2 } .$ . See the Appendix for a detailed proof. Q.E.D.

Proposition 3 prescribes three possible strategies for the WSI when the network effect is more significant $( \gamma > \bar { \nu } )$ —charge a low subscription fee to attract all customers (γ), attract only customers of $S _ { 3 }$ to subscribe (2γ), or allow some consumers of $S _ { 1 }$ (or S ) and all consumers of $S _ { 3 }$ to subscribe $( F _ { 2 1 } )$ . Although the optimal subscription fee is yet to be determined by the cross-network intensity as well as the sign of functions Φ and Ψ, there are cases where we are certain about the optimal subscription fee without having to evaluate the values of Φ or Ψ.

Corollary 3 specifies the condition when the WSI will not charge a low subscription fee to attract all customers to subscribe. It suggests that if the market for the integrated Web service is large and consumers have high valuation of the technical services provided by the WSI (intrinsic value), the WSI does not need to offer a low subscription fee to attract all customers. Corollary 4 further gives the condition under which the WSI only needs to attract consumers of $S _ { 3 } ,$ if the market size of the integrated Web service and the value of the technical services are even higher than those specified in Corollary 3. Further, we observe that if the market size of $S _ { 3 }$ increases, the threshold values of technical services in Corollaries 3 and 4 decrease. Therefore, a larger market size of the integrated Web service leads to a greater possibility of high subscription fee (2γ or $F _ { 2 1 } )$ charged by the intermediary. On the other hand, if the market size of the integrated Web service $S _ { 3 }$ is small, Corollary 5 suggests that the WSI should set the subscription fee to attract all customers to subscribe if the crossnetwork intensity is sufficiently large while the market size of the integrated Web service is less than the sum of market sizes of individual Web services.

Corollary 6 characterizes how the optimal subscription fee is affected by the network intensity when the market size of the integrated Web service is large compared to the market sizes of the individual Web service components. Yet one should not confuse the subscription fee with the subscription rate. For example, when the subscription fee is $2 \gamma ,$ the WSI will attract only those consumers who are interested in the integrated Web service $( S _ { 3 } )$ . Corollary 6 suggests that larger network intensity allows the WSI to charge a higher subscription fee while still maintaining a certain level of subscription rate. In other words, the WSI is better off with higher network intensity. By studying the trajectory of optimal subscription fee, one observes an interesting implication that, if at some point the optimal subscription fee is $2 \gamma .$ , the WSI will never set the subscription fee at $\gamma$ as the cross-network intensity increases. In other words, if the best strategy for the WSI is to attract customers of $S _ { 3 }$ only, the WSI will not lower the subscription fee to attract all consumers even if the network effect intensifies.

## Conclusions and Future Research

IN THIS PAPER, WE STUDY THE OPTIMAL PRICING STRATEGY of a monopoly WSI in the supply chain of complementary Web services. The WSI provides added value to Web service vendors and consumers in two ways. The first added value, termed the intrinsic value, is due to the technical expertise of the WSI, such as enforcing quality of service, enhancing security, and so on. The second added value results from the aggregation service that associates Web service vendors and consumers. In addition, the Web service consumers place a higher valuation on the WSI when more Web service vendors are listed on it, and vice versa, because of the cross-network externality effect between two sides of the Web service supply chain. The emergence of WSI in the service-oriented computing architecture brings forth distinct research issues that differ from earlier research on intermediary of physical goods and information intermediary. In particular, the integration of complementary Web services and the cross-network externality effect complicates research involving the WSI. In this study, we analyze the optimal subscription fee and listing fee for a monopolistic WSI that serves multiple groups of Web service consumers and vendors. Specifically, the WSI serves two groups of Web service vendors that provide two complementary Web services. Correspondingly, there are demands for both the individual Web services and the integrated Web service.

Our research finds that in the presence of cross-network externality effect, the optimal strategy for the WSI is to set a low listing fee such that all Web service vendors list on it. On the other hand, it is not always optimal if the WSI attracts all Web service consumers to subscribe. The optimal subscription fee is dependent on the relationship between the network value (aggregation services) and the intrinsic value (technical services) provided by the WSI. In addition, the optimal subscription fee is affected by such market characteristics as the prices and the market sizes of the underlying Web services. Therefore, the value-added services provided by the WSI, together with the market characteristics of Web services, determine the optimal strategy for the WSI. If the consumers appreciate the intrinsic value more than the network value, the optimal subscription fee is increasing in the intensity of the cross-network externality effect and the WSI will attract more consumers as the network effect intensifies. On the other hand, if the consumers have a higher valuation of the network effect than the intrinsic value, the WSI’s optimal strategy becomes more complicated and depends on certain threshold values.

Our analytical result is also consistent with industry practice. According to a survey by InfoWorld (www.infoworld.com) published in July 2004, GrandCentral<sup>4</sup> implements a pricing scheme that goes so far as to offer free accounts for the developers (i.e., service providers) in order to attract all potential Web service providers, a practice consistent with the recommendation of Lemma 1. In the same survey by Infoworld, all four major WSIs charge subscription fees ranging from \$50,000, \$75,000, to \$500,000 per CPU per year.

In our model, the distribution of valuation for technical services is uniform across all customers. In reality, it is possible that customers who are interested in the integrated Web service have a higher valuation for technical services, especially if the intermediary provides integration tools. Therefore, one way to extend the current model is to study the scenario when customers incur lower integration cost through WSI. Although this possibility is not analyzed specifically in our model, we expect the general results should still hold in such cases. For example, the WSI should still subsidize service vendors and the optimal subscription fee is still determined by several factors, such as value of technical versus aggregation services and the prices and market sizes of underlying Web services. The threshold value that determines the optimal subscription strategies will, however, change if customers of $S _ { 3 }$ have a higher valuation for technical services. As we can easily infer from the current findings, the WSI will have more incentive to attract $S _ { 3 }$ customers than $S _ { 1 }$ and $S _ { 2 }$ customers.

There are several potential extensions to our research. A WSI with strong technical expertise can extend its business scope by developing and selling the integrated Web service. One natural extension is to analyze the optimal strategy of the WSI that provides the integrated Web service to consumers because we only consider the WSI as an intermediary in this paper. This means the relationship between the WSI and Web service vendors can become both cooperative and competitive.

Another avenue of future research is to extend the monopolistic setting to consider competition in a duopolistic setting. The interesting problem in a duopoly market is that the WSIs compete in two dimensions—technical services and aggregation services. In addition, there is positive feedback effect between technical and aggregation services. For example, the intermediary likes to enhance the value of technical services to attract more subscription and listing, which in turn increases the value for its aggregation services. Therefore, it is worthwhile to study the endogenous choice of technical services in a competitive market.

Acknowledgments: We thank three anonymous reviewers for their invaluable comments and suggestions, which greatly improved this paper. The first author thanks Dr. Ivan Png from the National University of Singapore for sharing his opinions and suggestions on this research. The second author gratefully acknowledges the generous support of the summer research grant of Warrington College of Business Administration, University of Florida. Any remaining errors belong to the authors.

## NOTES

1. The original definition is given by Stencil Group. Although Stencil Group has gone out of business, their definition of Web services is widely cited. Readers can access a copy of the definition at www.site.uottawa.ca/\~stan/csi5389/readings/wsdefined.pdf.

2. The linear additive form is chosen following the standard approach from the literature. Other functional form such as multiplicative is also possible, but it makes the analysis intractable without the benefit of additional insights.

3. In case $\pi _ { i } ^ { N I } = \pi _ { i } ^ { I } .$ , we assume that the vendors will list on the WSI due to nonmonetary benefits such as enhanced publicity, account management, and so on.

4. GrandCentral.com was expected to be relaunched in summer of 2006.

## REFERENCES

1. Bailey, J. 1999. Intermediation and electronic markets: Aggregation and pricing in Internet commerce. Ph.D. dissertation, Massachusetts Institute of Technology, Cambridge.

2. Bailey, J., and Bakos, Y. An exploratory study of the emerging roles of electronic intermediaries. International Journal of Electronic Commerce, 1, 3 (Spring 1997), 7–20.

3. Bakos, Y. Reducing buyer search costs: Implications for electronic marketplaces. Management Science, 43, 12 (1997), 1676–1692.

4. Bakos, Y. Towards friction-free markets: The emerging role of electronic marketplaces on the Internet. Communications of the ACM, 41, 8 (1998), 35–42.

5. Baye, M., and Morgan, J. Information gatekeepers on the Internet and the competitiveness of homogeneous product markets. American Economic Review, 91, 3 (2001), 454–474.

6. Bhargava, H., and Choudhary, V. Economics of an information intermediary with aggregation benefits. Information Systems Research, 15, 1 (2004), 22–36.

7. Biglaiser, G. Middlemen as experts. Rand Journal of Economics, 24, 2 (1993), 212–223.

8. Corbett, J.C., and Karmarkar, U.S. Optimal pricing strategies for an information intermediary. Working Paper, University of California–Los Angeles, 1999.

9. Cubera, F.; Khalaf, R.; Mukhi, N.; Tai, S.; and Weerawarana, S. The next step in Web services. Communications of the ACM, 46, 10 (2003), 29–34.

10. Gehrig, T. Intermediation in search markets. Journal of Economics and Management Strategy, 2 (March 1993), 97–120.

11. Irani, R. Web services intermediaries: Adding value to Web services. Web Services Architect, Chicago, IL, 2001 (available at www.webservicesarchitect.com/content/articles/ irani07print.asp).

12. Jullien, B. Two-sided markets and electronic intermediaries. Institut d’Économie Industrielle, Toulouse University, Toulouse, France, July 24, 2004 (available at ideas.repec.org/ p/ces/ceswps/\_1345.html).

13. Kaplan, E., and Sawhney, M. E-hubs: The new B2B marketplaces. Harvard Business Review, 78, 3 (May–June 2000), 97–103.

14. Little, M. Transactions and Web services. Communications of the ACM, 46, 10 (2003), 49–54.

15. Naert, P. Optimizing consumer advertising, intermediary and markup in a vertical market structure. Management Science, 18, 4 (1971), 90–101.

16. Newcomer, E. Understanding Web Services: XML, WSDL, SOAP and UDDI. Boston: Addison-Wesley, 2002.

17. Rochet, J.-C., and Tirole, J. Two-sided markets: An overview. Institut d’Economie Industrielle, Toulouse University, Toulouse, France, March 12, 2004 (available at www.frbatlanta.org/filelegacydocs/ep\_rochetover.pdf).

18. Rubinstein, A., and Wolinsky, A. Middleman. Quarterly Journal of Economics, 102, 3 (1987), 581–594.

19. Schmelzer, R. XML and Web Services Unleashed. Indianapolis: SAMS, 2002.

20. Spulber, D. Market microstructure and intermediation. Journal of Economic Perspectives, 10, 3 (1996), 135–152.

21. Wooders, J. Equilibrium in a market with intermediation is Walrasian. Review of Economic Design, 3, 1 (1997), 75–89.

22. Yavas, A. Middleman in bilateral search markets. Journal of Labor Economics, 12, 3 (1994), 406–429.

## Appendix. Proofs

## Proof of Lemma 1

WE LOOK AT THE INTERMEDIARY’S REVENUE from subscription and listing separately. According to the definition of $y _ { j }$ (see Equations (1a) to (1c) and (2a) to (2c)), the intermediary’s revenue from collecting subscription fee is nondecreasing in the proportion of listed service vendors (x ). Next, we rewrite the intermediary’s revenue from listing (Π ) according to the definition of x in Equation (5) as follows:

$$
\left[ P _ {1} \left(y _ {1} Q _ {1} + y _ {3} Q _ {3}\right) + P _ {2} \left(y _ {2} Q _ {2} + y _ {3} Q _ {3}\right) \text { if } L \geq \max \left\{L _ {1}, L _ {2} \right\} \right.\tag{A1}
$$

$$
\Pi_ {x} = \left\{ \begin{array}{l} P _ {1} \left(y _ {1} Q _ {1} + y _ {3} Q _ {3}\right) + L N _ {2} \end{array} \right.
$$

$$
\Pi_ {L} = \left\{ \begin{array}{l} P _ {1} (y _ {1} Q _ {1} - y _ {3} Q _ {3}) \\ P _ {2} (y _ {2} Q _ {2} + y _ {3} Q _ {3}) + L N _ {1} \end{array} \right.
$$

$$
\text { if   } L _ {1} <   L _ {2} \text {   and   } L _ {1} <   L <   L _ {2}\tag{A2}
$$

$$
\left\lfloor L N _ {1} + L N _ {2} \right.
$$

$$
\text { if } L _ {2} <   L _ {1} \text { and } L _ {2} <   L <   L _ {1}\tag{A3}
$$

$$
\text { if } L \leq \min \left\{L _ {1}, L _ {2} \right\}.\tag{A4}
$$

Let

$$
L _ {1} = \frac {\left(y _ {1} Q _ {1} + y _ {3} Q _ {3}\right) P _ {1}}{N _ {1}}
$$

and

$$
L _ {2} = \frac {\left(y _ {2} Q _ {2} + y _ {3} Q _ {3}\right) P _ {2}}{N _ {2}}
$$

be the highest listing fee the intermediary can charge in order to induce all service vendors to list. Note that case (A1) corresponds to $0 \leq x _ { 1 } ,$ case (A2) corresponds to $x _ { 2 } = 1$ and $0 < x _ { 1 } < 1$ , case (A3) corresponds to $x _ { 1 } = 1$ and $0 < x _ { 2 } < 1$ , and case (A4) corresponds to $x _ { 1 } = x _ { 2 } = 1$

If the WSI set the listing fee at $L _ { 1 }$ , all service vendors of $S _ { 1 }$ will list on it $( x _ { 1 } = 1 )$ and, correspondingly, the revenue from charging listing fee to service vendor of $S _ { 1 } \mathrm { i s } x _ { 1 } L N _ { 1 } =$ $( y _ { 1 } Q _ { 1 } + y _ { 3 } Q _ { 3 } ) P _ { 1 }$ . If the listing fee is higher than $L _ { 1 } ( L ^ { \prime } > L _ { 1 } )$ , then there will be fewer service vendors listed on the WSI, that $\mathrm { i s } , x _ { \mathrm { ~ 1 ~ } } ^ { \prime } < 1$ . This, in turn, leads to a lower subscription rate, that is, $y _ { \mathrm { ~ 1 ~ } } ^ { \prime } < y _ { 1 }$ and $y _ { \ 3 } ^ { \prime } < y _ { 3 }$ . It follows that $P _ { 1 } \cdot ( y ^ { \prime } , Q _ { 1 } + y ^ { \prime } , Q _ { 3 } ) < P _ { 1 }$ $( y _ { 1 } Q _ { 1 } + y _ { 3 } Q _ { 3 } )$ . Therefore, the WSI obtains less profit from service vendors of $S _ { 1 }$ . At the same time, the profit from the subscription side is decreasing due to a lower subscription rate. The similar argument applies to the case when the listing fee is higher than $L _ { 2 } ( L ^ { * } > L _ { 2 } )$ . Furthermore, the intermediary’s profit will not improve if it charges a listing fee lower than min $\{ L _ { 1 } , L _ { 2 } \}$ , because the proportion of listing service vendors and subscribers remains unchanged. In summary, the intermediary should set the listing fee to allow all service vendors to list on it. Q.E.D.

## Proof of Lemma 2

We prove Lemma 2 by showing an example in which the WSI obtains more profit without full subscription from all the service consumers. First note that $F = \gamma$ is the maximum subscription fee the WSI can charge to induce total subscription. Following the result from Lemma 1, we know that the WSI will set the listing fee to attract all service vendors. Consequently, the WSI obtains a profit of $\pi _ { 1 } = \gamma ( Q _ { 1 } + Q _ { 2 } + Q _ { 3 } ) +$ $P _ { 1 } ( Q _ { 1 } + Q _ { 3 } ) + P _ { 2 } ( Q _ { 2 } + Q _ { 3 } )$ if all consumers subscribe. However, if the WSI charges a subscription fee of $\hat { F } = 2 \gamma$ , all customers of $S _ { 3 }$ will subscribe while some or no customers of $S _ { 1 }$ and $S _ { 2 }$ will subscribe, that is, $0 \le y _ { 1 } , y _ { 3 } = 1$ . Then the profit of the WSI is $\hat { \pi } \geq \pi _ { 2 } .$ , where $\pi _ { 2 } = 2 \gamma Q _ { 3 } + P _ { 1 } Q _ { 3 } + P _ { 2 } Q _ { 3 }$ is calculated by applying $F = 2 \gamma , y _ { 3 } = 1$ , and $y _ { 1 } = y _ { 2 } = 0$ in profit function. We find that the WSI obtains more profit $( \hat { \pi } \geq \pi _ { 2 } > \pi _ { 1 } )$ i $\mathrm { f } \gamma Q _ { 3 } > \gamma ( Q _ { 1 } + Q _ { 2 } ) + P _ { 1 } Q _ { 1 } + P _ { 2 } Q _ { 2 } . \mathrm { Q . E . D }$

## Proof of Lemma 3

Lemma 3 is drawn from solving the profit-maximization problem in Equation (8), which is a constrained optimization problem with quadratic objective function. The approach presented here is equivalent to applying KKT conditions. Because the optimal solution is either an interior solution or boundary solution, we first solve the unconstrained version problem. Optimal subscription fee and profit for the unconstrained optimization problem are described in Equations (A5) and (A6), respectively.

$$
F _ {1 1} = \frac {\left(\bar {v} + \gamma - P _ {1}\right) Q _ {1} + \left(\bar {v} + \gamma - P _ {2}\right) Q _ {2} + \bar {v} Q _ {3}}{2 \left(Q _ {1} + Q _ {2}\right)}\tag{A5}
$$

$$
\begin{array}{c} \Pi_ {1 1} \left(F _ {1 1}\right) = \frac {\left[ (\overline {{v}} + \gamma + P _ {1}) Q _ {1} + (\overline {{v}} + \gamma + P _ {2}) Q _ {2} \right] ^ {2} + \overline {{v}} ^ {2} Q _ {3} ^ {2}}{4 \overline {{v}} \cdot (Q _ {1} + Q _ {2})} \\ + \frac {2 Q _ {1} Q _ {3} \cdot (\overline {{v}} ^ {2} + \gamma \overline {{v}} + \overline {{v}} P _ {1} + 2 \overline {{v}} P _ {2}) + 2 Q _ {2} Q _ {3} \cdot (\overline {{v}} ^ {2} + \gamma \overline {{v}} + \overline {{v}} P _ {2} + 2 \overline {{v}} P _ {1})}{4 \overline {{v}} \cdot (Q _ {1} + Q _ {2})}. \end{array}\tag{A6}
$$

Next, we analyze whether $F _ { 1 1 }$ is a feasible solution as follows:

$$
F _ {1 1} - \gamma = \frac {\left(\bar {v} - \gamma - P _ {1}\right) Q _ {1} + \left(\bar {v} - \gamma - P _ {2}\right) Q _ {2} + \bar {v} Q _ {3}}{2 \left(Q _ {1} + Q _ {2}\right)}\tag{A7}
$$

and

$$
F _ {1 1} - 2 \gamma = \frac {\left(\bar {v} - 3 \gamma - P _ {1}\right) Q _ {1} + \left(\bar {v} - 3 \gamma - P _ {2}\right) Q _ {2} + \bar {v} Q _ {3}}{2 \left(Q _ {1} + Q _ {2}\right)}.\tag{A8}
$$

Then we calculate and compare the profits at lower- and upper-bound in Equations (A9), (A10), and (A11).

$$
\Pi_ {1 1} (\gamma) = (\gamma + P _ {1}) Q _ {1} + (\gamma + P _ {2}) Q _ {2} + (\gamma + P _ {1} + P _ {2}) Q _ {3}\tag{A9}
$$

$$
\Pi_ {1 1} (2 \gamma) = \frac {(\bar {\nu} - \gamma) (2 \gamma + P _ {1}) Q _ {1} + (\bar {\nu} - \gamma) (2 \gamma + P _ {2}) Q _ {2} + \bar {\nu} (2 \gamma + P _ {1} + P _ {2}) Q _ {3}}{\bar {\nu}}\tag{A10}
$$

$$
\Pi_ {1 1} (2 \gamma) - \Pi_ {1 1} (\gamma) = \frac {\gamma (\bar {v} - 2 \gamma - P _ {1}) Q _ {1} + \gamma (\bar {v} - 2 \gamma - P _ {2}) Q _ {2} + \gamma \bar {v} Q _ {3}}{\bar {v}}.\tag{A11}
$$

Last, the optimal subscription fee is calculated as follows.

If $( \bar { \nu } - \gamma - { \cal P } _ { 1 } ) { \cal Q } _ { 1 } + ( \bar { \nu } - \gamma - { \cal P } _ { 2 } ) { \cal Q } _ { 2 } + \bar { \nu } { \cal Q } _ { 3 } \leq 0$ , then the optimal subscription fee is γ since $F _ { 1 1 } \leq \gamma$ (see Equation (A7)) and $\Pi _ { 1 1 } ( 2 \gamma ) < \Pi _ { 1 1 } ( \gamma )$ (see Equation (A11)). The result corresponds to Equation (9a) of Lemma 3.

$\mathrm { I f } ~ ( \bar { \nu } - \gamma - { \cal P } _ { 1 } ) { \cal Q } _ { 1 } + ( \bar { \nu } - \gamma - { \cal P } _ { 2 } ) { \cal Q } _ { 2 } + \bar { \nu } { \cal Q } _ { 3 } > 0$ and $( \bar { \nu } - 3 \gamma - P _ { 1 } ) Q _ { 1 } + ( \bar { \nu } - 3 \gamma - P _ { 2 } ) Q _ { 2 } +$ $\bar { \nu } Q _ { 3 } < 0 ,$ , it follows from Equations (A7) and (A8) that $\gamma < F _ { 1 1 } < 2 \gamma$ . Therefore, the optimal subscription fee is $F _ { 1 1 } .$ which corresponds to Equation (9b) of Lemma 3.

$\mathrm { I f } ( \bar { \nu } - 3 \gamma - { \cal P } _ { 1 } ) { \cal Q } _ { 1 } + ( \bar { \nu } - 3 \gamma - { \cal P } _ { 2 } ) { \cal Q } _ { 2 } + \bar { \nu } { \cal Q } _ { 3 } \geq 0$ , then the optimal subscription fee is 2γ since $F \geq 2 \gamma$ (see Equation (A8)) and $\Pi _ { 1 1 } ( 2 \gamma ) > \Pi _ { 1 1 } ( \gamma )$ (see Equation (A11)). The result corresponds to Equation (9c) of Lemma 3. Q.E.D.

## Proof of Proposition 1

Lemmas 3, 4, and 5 specify the optimal strategy under different combinations of $y _ { j }$ $( j = 1 , 2 , 3 )$ in cases (I-1), (I-2), and (I-3), which is summarized in Table A1.

The optimal subscription fee can be found as the one that maximizes profit among ${ F _ { 1 1 } } ^ { * } , { F _ { 1 2 } } ^ { * }$ , and ${ F _ { 1 3 } } ^ { * }$ . Because the optimal strategy is dependent on the cross-network intensity (γ), we solve for the optimal subscription fee under each of the four situations in Table A1.

1. If $0 \leq \gamma \leq \gamma _ { _ { 1 1 } }$ , the optimal subscription fee is $F _ { _ { 1 2 } }$ as in Equation (13a) because

$$
\begin{array}{c} \Pi_ {1 2} (F _ {1 2}) - \Pi_ {1 1} (2 \gamma) = \\ \frac {\left[ (\bar {v} - 3 \gamma - P _ {1}) Q _ {1} + (\bar {v} - 3 \gamma - P _ {2}) Q _ {2} + (\bar {v} - 2 \gamma - P _ {1} - P _ {2}) Q _ {3} \right] ^ {2}}{4 \bar {v} \cdot (Q _ {1} + Q _ {2} + Q _ {3})} > 0 \end{array}\tag{A12}
$$

$$
\begin{array}{c} \Pi_ {1 2} (F _ {1 2}) - \Pi_ {1 3} (\overline {{{v}}} + \gamma) = \\ \frac {\left[ (\overline {{{v}}} - \gamma - P _ {1}) Q _ {1} + (\overline {{{v}}} - \gamma - P _ {2}) Q _ {2} + (\overline {{{v}}} + P _ {1} + P _ {2}) Q _ {3} \right] ^ {2}}{4 \overline {{{v}}} \cdot (Q _ {1} + Q _ {2} + Q _ {3})} > 0 \end{array}\tag{A13}
$$

Table A1. Optimal Subscription Fee $( \gamma < \bar { \nu } )$

<table><tr><td> $F_{1i}^{*}$ </td><td> $0 \leq \gamma \leq \gamma_{11}$ </td><td> $\gamma_{11} < \gamma < \gamma_{12}$ </td><td> $\gamma_{12} \leq \gamma < \gamma_{13}$ </td><td> $\gamma_{13} \leq \gamma \leq \bar{\nu}$ </td></tr><tr><td> $F_{11}^{*}$ </td><td> $2\gamma$ </td><td> $2\gamma$ </td><td> $F_{11}$ </td><td> $\gamma$ </td></tr><tr><td> $F_{12}^{*}$ </td><td> $F_{12}$ </td><td> $2\gamma$ </td><td> $2\gamma$ </td><td> $2\gamma$ </td></tr><tr><td> $F_{13}^{*}$ </td><td> $\bar{\nu} + \gamma$ </td><td> $\bar{\nu} + \gamma$ </td><td> $\bar{\nu} + \gamma$ </td><td> $\bar{\nu} + \gamma$ </td></tr></table>

2. $\mathrm { I f } \gamma _ { _ { 1 1 } } \leq \gamma < \gamma _ { _ { 1 2 } } ,$ , the optimal subscription fee is 2γ as in Equation (13b) because

$$
\begin{array}{c} \Pi_ {1 1} (2 \gamma) - \Pi_ {1 3} (\overline {{v}} + \gamma) = \\ \frac {(\overline {{v}} - \gamma) (2 \gamma + P _ {1}) Q _ {1} + (\overline {{v}} - \gamma) (2 \gamma + P _ {2}) Q _ {2} + (\overline {{v}} - \gamma) (\gamma + P _ {1} + P _ {2})}{\overline {{v}}} > 0. \end{array}\tag{A14}
$$

3. $\mathrm { I f } \gamma _ { _ { 1 2 } } \leq \gamma < \gamma _ { _ { 1 3 } } ,$ the optimal subscription fee is $F _ { 1 1 }$ as in Equation (13c) because

$$
\Pi_ {1 1} \left(F _ {1 1}\right) - \Pi_ {1 2} (2 \gamma) = \frac {\left[ (\bar {v} - 3 \gamma - P _ {1}) Q _ {1} + (\bar {v} - 3 \gamma - P _ {2}) Q _ {2} + \bar {v} Q _ {3} \right] ^ {2}}{4 \bar {v} \cdot \left(Q _ {1} + Q _ {2}\right)} > 0,\tag{A15}
$$

and from Equation (A14), we know $\Pi _ { _ { 1 1 } } ( F _ { _ { 1 1 } } ) > \Pi _ { _ { 1 2 } } ( 2 \gamma ) < \Pi _ { _ { 1 3 } } ( \bar { \nu } + \gamma )$

4. $\mathrm { I f } \gamma _ { _ { 1 3 } } \le \gamma < \bar { \nu }$ , the optimal subscription fee is γ as in Equation (13d) because we have proved in Lemma 3 that $\Pi _ { _ { 1 1 } } ( \gamma ) > \Pi _ { _ { 1 1 } } ( 2 \gamma )$ and $\Pi _ { _ { 1 1 } } ( 2 \gamma ) > \Pi _ { _ { 1 3 } } ( \bar { \nu } + \gamma )$ (see Equation (A14)). Q.E.D.

## Proof of Proposition 3

Proposition 3 can be proved by applying the same approach used in proving Proposition 1. First we summarize the optimal strategy of the intermediary under different settings of the cross-network intensity (γ) and propositions of subscribers $( y _ { j } , j = 1 , 2 , 3 )$ , see Table A2.

1. If $\bar { \nu } \leq \gamma \leq \gamma _ { _ { 2 1 } }$ , the optimal subscription fee is $2 \gamma$ as in Equation (15a) because

$$
\Pi_ {2 1} (\overline {{v}} + \gamma) - \Pi_ {2 3} (2 \gamma) = Q _ {3} \cdot (\overline {{v}} - \gamma) <   0.\tag{A16}
$$

2. If $\gamma _ { _ { 2 1 } } < \gamma < \gamma _ { _ { 2 2 } }$ , the optimal subscription fee is dependent on the sign of Φ because

$$
\begin{array}{c} \Pi_ {2 1} (F _ {2 1}) - \Pi_ {2 3} (2 \gamma) = \\ \frac {\left[ (\bar {v} + \gamma + P _ {1}) Q _ {1} + (\bar {v} + \gamma + P _ {2}) Q _ {2} - \bar {v} Q _ {3} \right] ^ {2} + 4 \bar {v} (\bar {v} - \gamma) (Q _ {1} + Q _ {2}) Q _ {3}}{4 \bar {v} \cdot (Q _ {1} + Q _ {2})}. \end{array}\tag{A17}
$$

Table A2. Optimal Subscription Fee $( \gamma > \bar { \nu } )$

<table><tr><td> $F_{2i}^{*}$ </td><td> $\bar{v} \leq \gamma \leq \gamma_{21}$ </td><td> $\gamma_{21} < \gamma < \gamma_{22}$ </td><td> $\gamma >\gamma_{22}$ </td></tr><tr><td> $F_{21}^{*}$ </td><td> $\bar{v} + \gamma$ </td><td> $F_{21}$ </td><td> $\gamma$ </td></tr><tr><td> $F_{22}^{*}$ </td><td> $2\gamma$ </td><td> $2\gamma$ </td><td> $2\gamma$ </td></tr><tr><td> $F_{23}^{*}$ </td><td> $2\gamma$ </td><td> $2\gamma$ </td><td> $2\gamma$ </td></tr></table>

Note that Φ is defined as the numerator of $\Pi _ { 2 1 } ( F _ { 2 1 } ) - \Pi _ { 2 3 } ( 2 \gamma )$ . Therefore, the optimal subscription fee is $F _ { 2 1 }$ when $\Phi \geq 0$ while the optimal subscription fee is 2γ otherwise.

$\operatorname { I f } \gamma > \gamma _ { 2 2 } ,$ the optimal subscription fee is dependent on the sign of Ψ because

$$
\Pi_ {2 1} (\gamma) - \Pi_ {2 3} (2 \gamma) \equiv \Psi = (\gamma + P _ {1}) Q _ {1} + (\gamma + P _ {2}) Q _ {2} - \gamma Q _ {3}.\tag{A18}
$$

Therefore, the optimal subscription fee is γ i $\mathbf { \partial } \cdot \mathbf { \Psi } \Psi > 0$ while $2 \gamma$ otherwise. Q.E.D.

## Proof of Corollary 4

It can be easily checked after simple algebra that under the conditions specified in Corollary 4, we must have $\gamma _ { 2 1 } > \bar { \nu }$ and $\bar { \nu } Q _ { 3 } > ( 2 \bar { \nu } + P _ { 1 } ) Q _ { 1 } + ( 2 \bar { \nu } + P _ { 2 } ) Q _ { 3 }$ . According to Proposition 3, the optimal subscription fee is $2 \gamma$ when $\bar { \nu } \leq \gamma \leq \gamma _ { 2 1 } .$ , see Equation (15a). As for the optimal subscription fee when $\gamma _ { 2 1 } < \gamma < \gamma _ { 2 2 }$ , first note that $\Phi$ is negative $\mathrm { i f } \gamma = \gamma _ { 2 1 }$ :

$$
\Phi \left(\gamma_ {2 1}\right) = 4 \overline {{v}} Q _ {3} \Big [ \big (2 \overline {{v}} + P _ {1} \big) Q _ {1} + \big (2 \overline {{v}} + P _ {2} \big) Q _ {2} - \overline {{v}} Q _ {3} \Big ] <   0.\tag{A19}
$$

Further, we evaluate the derivative of Φ as follows:

$$
\Phi_ {\gamma} \equiv \frac {\partial \Phi}{\partial \gamma} = (Q _ {1} + Q _ {2}) [ (\bar {v} + \gamma + P _ {1}) Q _ {1} + (\bar {v} + \gamma + P _ {2}) Q _ {2} - 3 \bar {v} Q _ {3} ]\tag{A20}
$$

$$
\Phi_ {\gamma} \left(\gamma_ {2 2}\right) = 2 \overline {{v}} \cdot \left(Q _ {1} + Q _ {2} - Q _ {3}\right) <   0.\tag{A21}
$$

Because $\Phi _ { \gamma }$ is increasing in $\gamma$ and it is evaluated negative at $\gamma _ { 2 2 } ,$ , it follows that $\Phi _ { \gamma }$ is negative for the interval $\gamma _ { 2 1 } < \gamma < \gamma _ { 2 2 }$ . Adding the fact that Φ is negative at $\gamma _ { 2 1 }$ , we conclude that $\Phi < 0$ is negative in the interval $\gamma _ { 2 1 } < \gamma < \gamma _ { 2 2 } .$ . Therefore, the optimal subscription fee is $2 \gamma$ under the condition $\gamma _ { 2 1 } < \gamma < \gamma _ { 2 2 } .$ , according to Equation (15b). In addition, we observe that the optimal subscription fee will never switch from $2 \gamma$ to $F _ { 2 1 }$ in the range $\gamma _ { 2 1 } < \gamma < \gamma _ { 2 2 }$ <sub>2</sub> when $Q _ { 1 } + Q _ { 2 } < Q _ { 3 }$ 3

Last, we show that if $\Phi ( \gamma _ { 2 2 } ) < 0$ , function Ψ is negative in the interval $\gamma \geq \gamma _ { 2 2 }$ due to two facts: (1) functions Φ and Ψ have the same sign, see Equations (A22) and (A23); and (2) Ψ is decreasing in γ when $2 ( Q _ { 1 } + Q _ { 2 } ) < Q _ { 3 }$ .

$$
\Phi \left(\gamma_ {2 2}\right) = 4 \bar {v} \cdot \left(\bar {v} Q _ {1} ^ {2} + 2 \bar {v} Q _ {1} Q _ {2} + P _ {1} Q _ {1} Q _ {3} + \bar {v} Q _ {2} ^ {2} + P _ {2} Q _ {2} Q _ {3} - \bar {v} Q _ {3} ^ {2}\right)\tag{A22}
$$

$$
\Psi \left(\gamma_ {2 2}\right) = \frac {\bar {v} Q _ {1} ^ {2} + 2 \bar {v} Q _ {1} Q _ {2} + P _ {1} Q _ {1} Q _ {3} + \bar {v} Q _ {2} ^ {2} + P _ {2} Q _ {2} Q _ {3} - \bar {v} Q _ {3} ^ {2}}{Q _ {1} + Q _ {2}}.\tag{A23}
$$

In summary, under the conditions specified in Corollary 4, the optimal subscription charged by the intermediary is 2γ. Q.E.D.

## Proof of Corollary 6

We can prove that the optimal subscription fee is increasing in $\gamma$ because there are only three possible cases for the optimal subscription fee: (1) 2γ for the entire region $\gamma > \bar { \nu } ; ( 2 ) F _ { 2 1 }$ when $\gamma _ { 2 1 } < \gamma < \gamma _ { 2 2 } , \gamma$ and then $2 \gamma$ when $\gamma > \gamma _ { 2 2 } ;$ and (3) $F _ { 2 1 }$ and then 2γ for the region $\gamma _ { 2 1 } < \gamma < \gamma _ { 2 2 } ,$ then 2γ when $\gamma > \gamma _ { 2 2 }$

1. If $2 ( Q _ { 1 } + Q _ { 2 } ) < Q _ { 3 }$ Q and $\bar { \nu } \geq ( P _ { 1 } \mathcal { Q } _ { 1 } + P _ { 2 } \mathcal { Q } _ { 2 } ) / ( \mathcal { Q } _ { 3 } - 2 \mathcal { Q } _ { 1 } - 2 \mathcal { Q } _ { 2 } )$ , the optimal subscription fee is 2γ for the entire region (see Corollary 4). Obviously, optimal subscription fee is increasing in γ.

2. If $2 ( Q _ { 1 } + Q _ { 2 } ) < Q _ { \bar { \imath } }$ and $\bar { \nu } < ( P _ { 1 } \mathcal { Q } _ { 1 } + P _ { 2 } \mathcal { Q } _ { 2 } ) / ( Q _ { 3 } - 2 Q _ { 1 } - 2 Q _ { 2 } )$ , we must have $\gamma _ { { \scriptscriptstyle 2 1 } } <$ v\ and $\Phi ( \gamma _ { _ { 2 1 } } ) > 0 . \mathrm { I f } \gamma _ { _ { 2 1 } } < \bar { \nu } .$ , condition (15a) of Proposition 3 will never be satisfied. Therefore, we only need to consider the conditions specified in (15b) and (15c). If $\Phi ( \gamma _ { _ { 2 1 } } ) > 0$ , we must have $F _ { 2 1 }$ as optimal subscription fee at the junction $\gamma = \gamma _ { _ { 2 1 } }$ . If the optimal subscription fee is $F _ { 2 1 }$ in the entire interval $\gamma _ { 2 1 } <$ $\gamma < \gamma _ { _ { 2 2 } } ,$ we must have $F ( \gamma _ { _ { 2 2 } } ) > 0$ . Because functions Φ and Ψ have same sign at the junction $\gamma = \gamma _ { _ { 2 2 } } ,$ it follows that $\Psi ( \gamma _ { \gamma } ) > 0$ , implying that the optimal subscription takes the form of $\gamma \mathrm { a t } \gamma = \gamma _ { _ { 2 2 } } ,$ which coincides with $F _ { _ { 2 1 } } \mathrm { a t } \gamma _ { _ { 2 2 } }$ (one can verify that $F _ { _ { 2 1 } } ( \gamma _ { _ { 2 2 } } ) = \gamma _ { _ { 2 2 } } )$ . Because Ψ is decreasing in $\gamma ,$ the optimal subscription fee might switch from γ to $2 \gamma .$ . This corresponds to the second case.

3. If the optimal subscription fee is $F _ { 2 1 }$ and then $2 \gamma$ for the region $\gamma _ { { } _ { 2 1 } } < \gamma < \gamma _ { { } _ { 2 2 } } ,$ it follows that $\Phi ( \gamma _ { _ { 2 2 } } ) < 0$ , thus the optimal subscription fee takes the form of $2 \gamma$ in the interval $\gamma > \gamma _ { _ { 2 2 } }$ (see proof of Corollary 4). Q.E.D.
