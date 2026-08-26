---
otero_id: 24095
otero_key: "XTSKDN5H"
title: "Potential of Webservices to Enable Smart Business Networks"
authors: "Jos van Hillegersberg; Ruurd Boeke; Willem-Jan van den Heuvel"
year: "2004"
journal: "Journal of Information Technology"
doi: "10.1057/palgrave.jit.2000027"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Special edition

# Potential of Webservices to enable smart business networks

Jos van Hillegersberg<sup>1</sup>, Ruurd Boeke<sup>2</sup> and Willem-Jan van den Heuvel<sup>3</sup>

<sup>1</sup>Bedrijfskunde, Rotterdam School of Management, Erasmus University, Rotterdam, The Netherlands;

<sup>2</sup>Sitechno, The Netherlands;

<sup>3</sup>InfoLab, Tilburg University, The Netherlands

## Correspondence:

J van Hillegersberg, Bedrijfskunde, Rotterdam School of Management, Erasmus University, F1-27, PO Box 1738, 3000 DR Rotterdam, The Netherlands

Tel: þ 31 10 4082624;

Fax: þ 31 10 4089010;

E-mail: jhillegersberg@fbk.eur.nl

## Abstract

Webservices (WSs) are believed to be among the key technologies to enable the transformation of current static supply chains into dynamic virtual networks of enterprises. Others have said that these technologies are not yet ready for large-scale applications to supply chains and propose ‘traditional’ cross-enterprise integration methods. However, there is currently little research available that objectively evaluates the usefulness of WSs to enable smart business networks. In this study, this question is addressed through developing a typical scenario in which we transform a static supply chain into a ‘loosely coupled’ business network. We implement the scenario using state-of-the-art ‘enterprise application integration’ and WSs orchestration technology. The comparison of these alternative approaches reveals that WSs technology has some clear advantages above enterprise integration technology currently in use. However, there are also some limitations and research issues which are presented as a future research agenda for WSs technology. Journal of Information Technology (2004) 19, 281–287. doi:10.1057/palgrave.jit.2000027 Published online 9 November 2004

Keywords: webservices; orchestration; supply chain management; smart business networks

## Introduction

A <sup>fter</sup> <sup>the</sup> <sup>hype,</sup> <sup>the</sup> <sup>web</sup> <sup>still</sup> <sup>holds</sup> <sup>huge</sup> <sup>potential</sup>for B2B integration. Now that a majority of com- for B2B integration. Now that a majority of companies have realized some sort of, mostly static, web presence, the web’s new promise is to enable smooth and cross-organizational business integration. Webservices (WSs) seem to be among the key webtechnologies that will allow this to happen. Eventually, these technologies should enable the transformation of current static supply chains into dynamic virtual networks of enterprises.

Proponents of WS-technology frequently claim that WS will lower barriers for ‘plug-and-play’ B2B integration. Through WS-oriented architectures, current supply chains could become better integrated, more agile and eventually intelligent. Others have said that these technologies are not yet ready for large-scale applications to supply chains and propose ‘traditional’ cross-enterprise integration methods such as custom built point-to-point interfaces or centralized E-Hubs, which are able to connect systems through custom made adapters.

Unfortunately, extensive reports from practice that address this debate are lacking. Dynamic business networks enabled through WSs technologies are not yet a reality. The vast majority of current practical work is applying WSs to improve intra-organizational integration rather than connecting different organizations together. Most research and industry reports in this area focus on new WS-technologies and standards. Few research addresses the potential benefits to current supply chains or addresses implementation issues. There is a lack of experience reports, case studies, demos, simulations and sample applications concerning the application of recent WS-technologies to illustrate and evaluate how WSs could transform static and inefficient supply chains into more efficient and dynamic ‘smart’ business networks.

This paper attempts to start bridging this gap by focusing on the application of WSs technologies to enable dynamic and smart business networks. The paper will address the following research questions sequentially:

Question 1: What are the current and near-future standardized components of WS-technology relevant to enabling smart business networks? (Section 2)

This question is addressed through a literature review and by evaluating tools, technologies and methods for WS development.

Question 2: What is the current state-of-the-art in WSs to enable smart business networks? (Section 3)

This question is addressed through developing a typical scenario in which we transform a static supply chain into a ‘loosely coupled’ business network. We implement the scenario using state-of-the art ‘enterprise application integration (EAI)’ and WSs orchestration technology.

Question 3: What are research issues regarding the use of WSs technology to enable smart business networks? (Section 4)

This question we deal with by reflecting on our experiences with the development of the scenario. From our development experiences, we deduct research issues and an agenda for WSs technology in the light of its application to enable smart and dynamic business networks.

## Webservices (WS)

The service-oriented computing (SOC) paradigm (Papazoglou and Georgakopoulos, 2003), with as its main materialization WS-technology, promises to deliver a profound new way of developing business applications and a significant step forward in the quest to maximize software reuse and integrate systems across different technology platforms. Although a variety of definitions of SOC exist, key to SOC is the process of constructing a software application by way of orchestration of prefabricated and pre-tested WSs.

WSs can be defined as self-describing, interoperable and reusable business components that can be published and invoked through the Internet, even when they reside behind a company’s firewall. WSs constitute, in fact, both designand runtime, platform-agnostic distributed enterprise building blocks that can be composed into higher order assemblies that support (inter- or intra-) organizational business transactions. Hence, WSs enable enterprises to leverage massively distributed applications, cutting across ‘traditional’ supply chains and vertical industries.

WSs are considered an important candidate to overcome some severe obstacles of CBD. In particular, WSs are described in a standard manner by their interface separating value-adding commodities from the actual implementation. WSs employ open, text-based standards to achieve interoperation between applications that possibly reside at various collaborating organizations. While doing so, SOC overcomes one of the major disadvantages of object middleware technologies such as CORBA, which in fact were too complex, firewall unfriendly and hard to maintain. In addition, SOC puts greater emphasis on three complementary views on services: a client view, a provider view and a broker perspective (Burbeck, 2000). Software components usually needed to be licensed and integrated on the customer’s site. WSs reside at the supplier’s site, thus supporting a federated architecture. The customer buys access to the WS instead of a license to download and integrate software code or a component. This model delivers potential benefits similar to application service provision (ASP). These include automatic upgrades to new versions, clear contracts through service-level agreements and often specialized support from the vendor, etc. Lastly, services extend traditional class interfaces by including information that is vital to setup Service-Level Agreements by attaching information about extra-functional properties (OASIS, 2003), like performance, security and pricing information.

The first wave of WS-technology standards has been devoted to developing infrastructural solutions for achieving interoperation at the level of messaging middleware. By now, industry has reached common agreement on interfacing standards for WSs using W3C’s WS Description Language (WSDL, (W3C, 2001)) that builds top of W3C’s Simply Object Access Protocol (SOAP) (W3C, 2000). These technologies and standards allow organizations to expose their services and invoke services of other organizations using the Internet. For locating services, directory services have been developed such as UDDI (OASIS, 2003). Although these initial WS standards enable simple transactions using basic describe, publish and interact mechanisms, they are not sufficient to support the more complex and long transactions that take place in a business network (Curbera et al., 2003).

Therefore, several industry consortia are now developing higher order WS stacks on top of SOAP that provide process composition languages. Current initiatives include ebXML Business Process Specification Schema (BPSS) (EbXML, 2001) and the Business Process Execution language for WS (BPEL4WS) (BPEL, 2003), an initiative of BEA, IBM, Microsoft SAP and Siebel. The W3C has initiated the Web Services Choreography Working Group to establish a vendor-neutral choreography specification which commands consensus and wide support. Today such a standard is not available and therefore for this study we focus on evaluating the current possibilities of the prominent current WS standards for transport (SOAP, XML), description (WSDL) and business processes (BPEL4WS), and explore their potential to support dynamic business networks. Thus, even though BPEL may be challenged or replaced, its current industry and development tool support made it a logical choice for this study. Figure 1 illustrates how the standards used fit into the WS standards stack.

The key properties of BPEL are summarized in (BPEL, 2003): ‘BPEL4WS defines a model and a grammar for describing the behavior of a business process based on interactions between the process and its partners. The interaction with each partner occurs through WS interfaces, and the structure of the relationship at the interface level is encapsulated in what we call a partner link. The BPEL4WS process defines how multiple service interactions with these partners are coordinated to achieve a business goal, as well as the state and the logic necessary for this coordination. BPEL4WS also introduces systematic mechanisms for dealing with business exceptions and processing faults. Finally, BPEL4WS introduces a mechanism to define how individual or composite activities within a process are to be compensated in cases where exceptions occur or a partner requests reversal’. BPEL is built upon, and heavily uses WSDL. Every BPEL process is exposed itself as a WS described in WSDL. The BPEL process uses WSDL datatypes and WSDL to call external WSs required (see Figure 2).

![](/api/attachments/XTSKDN5H/fulltext/images/a0c591909e8e8f40c4b2f6c64aafedf9c066f108b7403f45f32bb7cae795c226.jpg)  
Figure 1 WSs standards stack.

![](/api/attachments/XTSKDN5H/fulltext/images/dce2b25bf5c24f6520390633ad5d03bde207d49ec77350d9d8449feb33fa7936.jpg)  
Figure 2 BPEL4WS process components (adapted from Peltz, 2003).

BPEL supports both WS-orchestration and WS-choreography. Peltz (2003) describes the difference between the two as; ‘Orchestration refers to an executable business process that may interact with both internal and external WSs. For orchestration, the process is always controlled from the perspective of one of the business parties. Choreography is more collaborative in nature, in which each party involved in the process describes the part they play in the interaction’. For our exploratory study, we focus on WS-orchestration. A WS-orchestration allows a party in a business network to define and execute a business process quickly incorporating the services of business partners in the network. Therefore, WS-orchestration technology seems especially useful for enabling dynamic business networks. The actual possibilities of BPEL combined with the early WS standards SOAP and WSDL will receive more attention in the next section when we implement a business network scenario.

## Implementing a business network enabled by WSs

To explore the potential of the current WSs technology to enable smart business networks, we now develop a typical scenario in which we transform a static supply chain scenario into a ‘loosely coupled’ business network that can be easily adapted and configured. We first implement the scenario using state-of-the art ‘EAI’ and then deploy WSs orchestration technology. The scenario used here is partly based on a supply chain scenario developed by the WSs Interoperability organisation (WS-I.org, 2004). WS-I has developed UML specifications of a Supply Chain Management scenario for the purpose of evaluating WS standards and tools. The specification documents include Use Cases, Use Case Scenarios, Activity Diagrams and a sample architecture.

The WS-I, a supply chain scenario, is based on a typical B2C model in which retailer receives customer orders and has to fulfill these by ordering from a collection of warehouses. The retailer has to manage stock levels in warehouses and replenish by ordering from a manufacturer’s inventory (a typical B2B model). In order to fulfill a retailer’s request, a manufacturer may have to execute a production run to build the finished goods (WS-I.org, 2004). Figure 3 illustrates part of the WS-I scenario (sourcing of goods from a warehouse) in an UML Activity Diagram. The process flow shows that ordered goods are located and shipped from warehouse(s). The objective of this sourcing process is to deliver all goods ordered and prevent ‘out of stock’.

The WS-I scenario is a useful basis for our study. However, it is quite broad and models a static supply chain. For example, the number of warehouses is fixed (3). Moreover, the business rules are very basic. For example, as Figure 3 illustrates, orders are shipped from the warehouses only based on a fixed sequence checking of the available stock at warehouse A, B and finally C, thus not comparing cost information. Therefore, we have developed our own scenario, which is based on the WS-I supply chain scenario, but adds dynamics to the business network and more complexity to the business rules.

Similarly to the WS-I scenario, the sourcing process will sequentially check multiple warehouses if the stock of a single warehouse is not sufficient. Differing from the WS-I scenario is the option to change the number of warehouses and the product assortment of each warehouse. The scenario can thus be used to experiment with ‘smart’ WSs orchestrations that use more complicated business rules to simulate the efficiency of order delivery for various business networks and warehouse product assortments.

![](/api/attachments/XTSKDN5H/fulltext/images/664489fdd74e98ccdb00800169111644d8da017144086795c633c23d9e437852.jpg)  
Figure 3 Sourcing process of a retailer in the WS-I sample supply chain scenario based on (WS-I (2004).

The warehouse system stores product IDs, prices and stock levels and replenishes stock by ordering from a producer whenever the stock level drops below a minimum level. The warehouse system keeps track of the number of items in stock, the number of items ordered by customers and the number of items in backorder with a producer (status awaited). Other than in the standard WS-I scenario, prices can be different for the same product in different warehouses. Using this information, smart WS orchestrations can be devised that optimize in time delivery and aim for the lowest price. Finally, producers are included in the scenario. Producers can be configured to produce certain products in certain batches. The warehouse can order from any producer in the business network. At this stage, the emphasis is on enhancing the retailer–warehouse relationship.

The scenario was implemented by building small software applications for each group of actors (producers, warehouses), a webshop application to serve the testcustomer, and an application to configure the scenario. The user interface of the webshop is shown in Figure 4. Test consumers can order products order multiple products in a single session. The shop application checks the warehouses through calling their interfaces (services) to inquire about stock levels. Figure 5 shows the scenario configuration application. It can be used to configure the business network, for example, setting the number of warehouses, their product assortment and prices.

![](/api/attachments/XTSKDN5H/fulltext/images/b99caf2e4dc2b4d2e5da43a6f7a70bd139c5d4dc43bd16dfec3851755919a2f2.jpg)  
Figure 4 Sample webshop application.

Initially, the scenario was implemented in the Microsoft. Net framework. Using standard EAI techniques (like

1-4 out of 4

<table><tr><td></td><td>Description</td><td>Product id</td><td>Price</td><td>Standard Level</td><td>Stock</td><td>Ordered</td><td>Awaited</td><td>Producer</td><td></td></tr><tr><td rowspan="9">update cancel</td><td colspan="3">Description:</td><td colspan="5">dvd speler</td><td rowspan="9">delete</td></tr><tr><td colspan="3">Product Id:</td><td colspan="5">1s</td></tr><tr><td colspan="3">Price:</td><td colspan="5">120</td></tr><tr><td colspan="3">Standard Level:</td><td colspan="5">100</td></tr><tr><td colspan="8">Following settings should be managed by the system. Only change for testing purposes</td></tr><tr><td colspan="3">Instock:</td><td colspan="5">0</td></tr><tr><td colspan="3">Ordered:</td><td colspan="5">70</td></tr><tr><td colspan="3">Awaited:</td><td colspan="5">170</td></tr><tr><td colspan="3">Producent:</td><td colspan="5">Sony</td></tr><tr><td>edit</td><td>video recorder</td><td>134BX</td><td>$140.00</td><td>100</td><td>0</td><td>260</td><td>360</td><td>6</td><td>delete</td></tr><tr><td>edit</td><td>flat screen 20&quot;</td><td>2001FS</td><td>$999.00</td><td>10</td><td>0</td><td>790</td><td>800</td><td>5</td><td>delete</td></tr><tr><td>edit</td><td>plasma tv 69&quot;</td><td>VG69b</td><td>$2,900.00</td><td>5</td><td>0</td><td>95</td><td>100</td><td>5</td><td>delete</td></tr></table>

Orders are automatically delivered every 60 seconds. Click here to reload this page Click here to deliver immediately.

Figure 5 Managing the warehouses and product assortment in the business network.

Remote Method invocation), the communications between webshop, warehouse and producer were established. Then, the scenario was ported to WS-technology. By using a WSorchestration tool (BizTalk 2004) and BPEL WS-orchestration, the B2B processes were replaced by WS-orchestration. These were previously ‘hard coded’ into the .net (C#) code. This exercise allowed us to clearly compare the potential of WS-orchestration languages and tools as compared to traditional EAI techniques. In the following discussion, we focus on the sourcing process between the Webshop and the retailer.

In porting the standard EAI scenario to a WS-orchestration, we focused on the following questions: First, what is the power of BPEL to support more complex B2B interactions? Would it be limited to modelling simple straightforward interactions or could it also be used to quickly setup more complex and long business transactions? Second, how mature and compatible are the standards and tools? As mentioned in the previous section, orchestration standards such as BPEL are still under development. Does this cause unexpected side-effects and unpredictable behaviour of the supporting tools? Even more importantly, will WS-orchestration technology enable the end-user to setup and adapt B2B processes quickly? Will WS-orchestration technologies finally allow business users to escape from costly, and error prone traditional EAI technologies that they did not understand? In other words, will these technologies soon empower the end-user to become a ‘business network supervisor and configurator’?

The implementation project started in 2003. Initially, we used Microsoft BizTalk 2002 as the WS-orchestration product. However, the product had several shortcomings, and when BizTalk 2004 was launched in February 2004, we decided to migrate to this product. We have considered several other tools that supported WS-orchestration for this study, such as tools from Collaxa, BEA, IBM and Cordys. However, comparisons of several of these products illustrate that differences are minor (Peltz, 2003) and for our purposes any of these tools could have been used.

BizTalk 2004 includes several components such as a visual orchestration designer, a ‘message-mapper’ to translate and map different XML messages graphically and a Business Rule composer that is meant to isolate business rules from the application. The BizTalk monitoring environment contains a performance measurement tool and a debugging tool. To get a feel for the usability and adaptability of BPEL WS-orchestrations in BizTalk, we will briefly discuss the WS-orchestration between the webshop and the warehouses.

As mentioned earlier, a BPEL WS-orchestration is itself set up as a WS. Therefore, the orchestration starts with an incoming request, which is a customer order requesting some quantity of a product. The orchestration monitors a ‘port’ for incoming requests and starts an orchestration whenever an order message is received.

As our scenario uses a dynamic number of warehouses that have unique IDs, we built separate WSs to locate warehouses IDs (a kind of simple directory service). In a truly dynamic business network, indeed, an orchestration process could decide to check directory services to shortlist potential partners in a business network. Once the list of warehouses to check for stock has been identified, the orchestration can start checking product availabilities at each warehouse. Figure 6 shows one of the orchestrations designed to evaluate the ease of designing and implementing B2B processes through WSs. The orchestration flow starts by retrieving warehouse IDs of three preferred business partners. It then proceeds by concurrently getting price and availability quotes from these three warehouses based on the customer order. The connection to the external warehouse WS is quickly established in BPEL. An external ‘port’ can be created by simply specifying the Webaddress of the WS and the request and response messages are connected graphically by using ‘drag and drop’ to the node ‘avail request’. As all quotes have been received, a decision is built-in to evaluate if the quotes received can individually or jointly fulfill the order (The IF–THEN construct is visually shown by the diamond shape in Figure 6). If this is the case, another orchestration (Place Order) is invoked. If the quotes received cannot meet the order, an orchestration is invoked that requests quotes from additional warehouses.

We have implemented several variants to test the adaptability of the orchestration language and tools. From the scenarios we developed and implemented using WSorchestration, and the comparison to the initial traditional EAI approach, several conclusions can be drawn:

First, the well-established and relatively simple SOAP and WSDL standards enable a true cross-platform distributed architecture. As long as these standards are well-supported across platforms, WSs will truly allow straightforward B2B integration using standard and low-cost Internet technology. This is a major advantage in enabling business networks, as small companies within these networks usually do not have the knowledge, time and money to implement traditional and complex EAI technologies.

Second, our scenario implementation clearly demonstrated that the network orchestration could be designed mostly separately from the various systems available in the business network. Thus, the network business rules (such as selecting a warehouse to order from) are isolated from the ‘back-office systems’ and therefore more ‘visible’ and easier to change. It could be stated that the B2B logic is extracted from the individual systems, and now resides in a separated WS-orchestration layer. This is a key advantage to creating dynamic business networks. Although it is hard to define what exactly is meant by a ‘smart’ business network, the example also illustrated that basic decision logic could be easily built into an orchestration and adapted with relatively little effort.

![](/api/attachments/XTSKDN5H/fulltext/images/982f9212b6e00ba8c45f59d70452d762e88227c764a8385e2f025e17036d6484.jpg)  
Figure 6 A BPEL flow to select concurrently a warehouse for ordering.

Third, we found that orchestration technology has greatly advanced over the last 2 years that we have been carrying out this project. Still, although it has become much easier to put together orchestrations, it is in our opinion still the work of specialized consultants/developers. It is more likely that after some training, non-IT staff could adapt the business rules within an orchestration. However, businesses should handle these changes with care, as the impact of malicious code in a WS-orchestration will not be limited to the internal business, but will also impact suppliers, partners and even worst, customers.

## Conclusion and discussion: an R&D agenda for WSs to enable smart business networks

WSs are a promising technology to enable dynamic and smart business networks. However, the current WS stack of standards can no longer be considered a set of simple and coherent technologies as in the early days of WS. The technology is maturing, and as issues such as WS orchestration, choreography, security, quality of service and transactions are resolved, the set of standards gets richer and naturally also more complex. An area in which standards are still evolving and competing is the area of WS orchestration. In the last couple of years, we have seen many different standards rising and disappearing, and given this high technological pace, it is not surprising that businesses are reluctant to invest considerably in this part of WS-technologies. Thus, examples of business networks that already use orchestration technologies are scarce.

Therefore, to evaluate the state-of-the-art and its potential to enable smart and dynamic business networks in the future, implementing scenarios is a useful research method. Work as done by the WS-I to develop standard sample specifications to serve as a test-bed, interoperability test and reality check for the new WS-technologies is very imperative. However, a downside of such initiatives is that mostly only vendors are providing sample solutions, and objective reviews of the possibilities of the tools and standards are scarce.

In this study, we aimed to evaluate the current state-ofthe-art in WSs to enable smart business networks. The evaluation demonstrated that (1) SOAP and WSDL standards enable an easy to setup true cross-platform distributed architecture, (2) WS orchestration facilitates the creation of dynamic business networks by clearly separating B2B logic from the separate systems and making it easier to built-in ‘smart’ and adaptable decisions, (3) although WS standards make B2B integration easier to put together orchestrations, it is certainly not yet an enduser task. Putting together successful orchestration will require close collaboration of business and IT specialists.

Our scenario has not tested performance, security and scalability of the orchestration tools, nor were the B2B processes complex enough to reach the limits of the expressive power of BPEL. Also, we have assumed that the various warehouses in the business network had adopted the same industry-specific standards for quotes, orders, etc. In reality, such standards are currently under development and often rivaling initiatives exists. Although orchestration tools included basic translation support, semantic differences in business processes can be nontrivial to resolve. Moreover, as business networks often lack a ‘chain director’ designing the orchestration will in many cases be a collaborative process. We therefore claim that languages and tools to design B2B interaction should have features to support team collaboration.

Intelligence is required as the coordination cost (searching for appropriate services, negotiating for price and quality of services, monitoring B2B transactions) may become too high in dynamic business networks. Therefore, intelligence should be added to WS-enabled business networks. This is where research on agent technologies in supply chains and WSs technology are likely to meet in the future. It is our first assumption that both technologies are complementary and developing agents is more feasible in a B2B network that utilizes WSs standards.

Nevertheless, the progress in WS-orchestration technologies has been substantial recently, and the scenario implemented in this paper has demonstrated that enabling a business network through WS-orchestration seems feasible. Real benefits are only expected in cases where supply chains can profit from transforming into a dynamic network of businesses. Especially when quick adaptability of the B2B processes or the configuration of the business network is an important issue, the use of WS and WSorchestration should definitely be considered.

## References

BPEL. (2003). BEA Systems, IBM. Microsoft, SAP AG, Siebel Systems, Specification: business process execution language for web services version 1.1 [WWW document], http://www-106.ibm.com/developerworks/library/ ws-bpel/(accessed July 2004).

Burbeck, S. (2000). The evolution of Web applications into service-oriented components with Webservices, [WWW document] http://www-106.ibm.com/ developerworks/WSs/library/ws-tao(accessed July 2004).

Curbera, F., Khalaf, R., Mukhi, N., Tai, S. and Weerawarana, S. (2003). The Next Step in Webservices, Communications of the ACM 2003 46(10): 29–34.

EbXML. (2001). ebXML business process specification schema, version 1.01, [WWW document] http://www.ebxml.org/specs/ebBPSS.pdf(accessed July 2004).

OASIS. (2003). UDDI V 3.0.1, [WWW document] http://uddi.org/pubs/uddiv3.0.1-20031014.htm(accessed July 2004).

Papazoglou, M.P. and Georgakopoulos, D. (2003). Service Oriented Computing: Introduction M, Communications of the ACM 46(10): 24–28.

Peltz, C. (2003). Webservices Orchestration and Choreography, IEEE Computer 36(10): 46–52.

W3C. (2000). Simple Object Access Protocol (SOAP) 1.1, W3C note 08 May 2000, [WWW document] http://www.w3.org/TR/2000/NOTE-SOAP-20000508/(accessed July 2004).

W3C. (2001). WSs Description Language (WSDL) 11, W3C technical report, March 2001, [WWW document] http://www.w3.org/TR/wsdl.

WS-I.org. (2004). Supply chain management use cases, [WWW document] http://www.ws-i.org/(accessed July 2004).

## About the authors

Dr Jos van Hillegersberg is an associate professor at the Rotterdam School of Management, Erasmus University, Rotterdam. His research interests include: software devel opment for E-business (CBD, EAI, UML, Software process improvement), global software development, ICT support for coordination of global teams, and ICT architectures. He worked earlier at the IBM Knowledge Based Center, as a visiting researcher at the CIS Department of Georgia State University, Atlanta, USA, as a visiting professor at Florida International University and at AEGON Bank on the development of an E-banking system.

Ruurd Boeke, MSc in Business Administration, is an active developer in the area of Enterprise application development and Webservices. He completed many commercial projects applying object-oriented and webservice technology. In his most recent project, he is engaged in architecting a social security system for the city of The Hague.

Dr. Willem-Jan van den Heuvel is an assistant professor at the department of information management and information systems of Tilburg University. His research focuses on developing methods and tools for supporting enterprise integration, both at the horizontal (business process) and the vertical (legacy) level. Willem-Jan (co)organized several workshops, among them: two Enterprise Application Minitracks as part of two subsequent Hawaii’ International Conference on Systems Sciences (HICSS) conferences. In addition, he served as a program committee member of international workshops and conferences, such as the European Federated Information Systems (EFIS). Lastly, he acted as referee for several international workshops, conferences, and journals in the field of business object and web-service technology, conceptual modeling and (intelligent) agent technology.
