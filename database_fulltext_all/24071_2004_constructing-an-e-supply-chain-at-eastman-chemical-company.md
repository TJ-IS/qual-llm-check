---
otero_id: 24071
otero_key: "26HTXTXD"
title: "Constructing an E-Supply Chain at Eastman Chemical Company"
authors: "Benjamin Yen; Ali Farhoomand; Pauline Ng"
year: "2004"
journal: "Journal of Information Technology"
doi: "10.1057/palgrave.jit.2000011"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Teaching case

# Constructing an e-Supply Chain at Eastman Chemical Company

Benjamin Yen<sup>1</sup>, Ali Farhoomand<sup>1</sup>, Pauline Ng<sup>2</sup>

<sup>1</sup>School of Business, The University of Hong Kong, Hong Kong; <sup>2</sup>Centre for Asian Business Cases, The University of Hong Kong, Hong Kong

Correspondence:

B Yen, School of Business, The University of Hong Kong, Hong Kong. E-mail: benyen@business.hku.hk

## Abstract

Craig Knight, Asia Pacific Digital Business and Customer Services Manager of Eastman Chemical Company, was given a mandate to sell Eastman’s philosophy for an integrated electronic supply chain, otherwise known as the Integrated System Solution (ISS), to its business partners in the region, and to encourage adoption. Having invested in a state-ofthe-art technical architecture that would support interconnectivity with all parties along the supply chain, Eastman was keen to realise the full benefits to be gained from an integrated e-supply chain on a global scale. Following numerous rounds of discussion with key business partners in the Asia Pacific region, some progress had been made. Nagase & Co., Ltd. of Japan had agreed to adopt ISS connections with Eastman, but had some reservations regarding the extent of integration. Although the benefits of integration were proven, suppliers, customers, distributors and other interested parties were faced with numerous limitations and considerations that would have significant implications on their established business processes and even the shaping of their corporate strategy. Adoption was not a simple choice. Craig understood these shortcomings and was making every effort to ease the adoption process by identifying the longer-term benefits to Nagase and other business partners of applying XML technology to their businesses. Journal of Information Technology (2004) 19, 93–107. doi:10.1057/palgrave.jit.2000011 Published online 6 July 2004

Keywords: electronic commerce; supply chain; information technology

Considering how many companies we deal with around the world, we only have 22 companies connected at this stage. We still have a long way to go. We have an infrastructure that would allow us to connect with hundreds of strategic partners, but it is slow for partners to take it on board. yOne of the hurdles now is with companies having sufficiently integrated systems internally to actually get the value from connecting with us. yIn pushing others to adopt the technology, we are trying to get the industry to adopt the e-business approach.

Craig Knight, Digital Business & Customer Services Manager – Asia Pacific

## Introduction

t was a sultry day in the middle of June 2002. Craig Knight, Asia Pacific Digital Business and Customer Services Manager of Eastman Chemical Company, was heading out of his Singapore regional head office on another two-week trip to Tokyo, Shanghai and Kuantan in Malaysia. The mandate he had been given was to sell Eastman’s philosophy for an integrated electronic supply chain, otherwise known as the Integrated System Solution (ISS), to its business partners in the region, and to encourage adoption. Having invested in a state-of-the-art technical architecture that would support interconnectivity with all parties along the supply chain, Eastman was keen to realise the full benefits to be gained from an integrated esupply chain on a global scale. Following numerous rounds of discussion with key business partners in the Asia Pacific region, some progress had been made. Nagase & Co., Ltd. of Japan had agreed to adopt ISS connections with Eastman, but had some reservations regarding the extent of integration. Although the benefits of integration were proven, suppliers, customers, distributors and other interested parties were faced with numerous limitations and considerations that would have significant implications on their established business processes and even the shaping of their corporate strategy. Adoption was not a simple choice. Craig understood these shortcomings and was making every effort to ease the adoption process by identifying the longer-term benefits to Nagase and other business partners of applying XML technology to their businesses.

## The chemical industry

The chemical industry consisted of manufacturers of basic and immediate chemicals, specialty chemicals, agricultural chemicals, petrochemicals, plastics and fibres, and paints and coatings. It provided intermediate and raw materials for industry and a variety of synthetic and formulated products for industry, agriculture, business and individual consumers.<sup>1</sup> At the same time, it was dependent on many of these same industries for raw materials, including, for example, agriculture and petroleum. The relationship between the industries is illustrated in Exhibit 1.

The industry was unique in many ways. Unlike, say, the steel industry, which made a group of products from only a few key raw materials, the chemical industry took low-cost basic chemicals and converted them into a series of intermediaries that would, in turn, be reacted or formulated into a wide variety of end products, usually of high unit value and for a diverse range of industries. In this way, many chemicals were actually the raw materials for making usable end products.

Synthesis and formulation were the two basic technologies used in the industry. Formulation involved mixing the chemicals by blending, emulsification, solution or other physical manipulation. Synthesis was a newer processing technique used to create new synthetic products. Through these technologies the industry grew by 2.9% annually in terms of physical output between 1985 and 1998 (See Note 1). Formulated products could achieve proprietary positions as they were continually modified to meet customers’ changing needs.

![](/api/attachments/26HTXTXD/fulltext/images/f7b0fc797508a34f33dd18ed59464cabce90a76de7bb04360ec9757c371ecdee.jpg)  
Exhibit 1 The chemical industry: materials and product flow. Source: ‘Economics of the Industry: US Specialty Chemicals, 1999, GAPS Sheet’, Kline & Company, http://www.klinegroup.com/Practices/chemicals/industry\_business.htm, accessed 4 June, 2002.

The chemical industry was also unique in terms of capital investment, ranking second in the world when measured by annual expenditure. The cost of building a new facility would often be hundreds of millions of dollars. Large plants were needed to incorporate efficiencies and economies of scale.

The demand for chemicals was directly correlated to the demand for consumer products. The industry was highly dependent on the automobile, manufacturing and housing business sectors, which were very cyclical. Supply and demand imbalances resulting from economic cycles were a major concern for chemical companies. The imbalance was also partly due to the limited flexibility of the continuous and semi-continuous manufacturing processes requisite for producing chemicals. Such processes complicated overall supply chain planning.

Most continuous, semi-continuous and batch processes operated 24/7. The processing of materials was transferred automatically from one stage to the next, with monitoring and self-adjusting flow and quality forming part of the automated process. The only human intervention involved checking the system. The enormous capital investment meant that maximising operating time was a major concern for manufacturers. Furthermore, the nature of the processes was complex and procedures for shutdowns and start-ups were costly. Hence, the manufacturing cycles were more or less fixed and measured in weeks or months. Unexpected fluctuations in demand or unexpected problems with equipment created major problems for inventory management and customer service performance. Another factor affecting inventory management was the practice of ‘optimal transition wheels’, where multiple products shared one reactor and production was restricted by a time sequence. For example, a paint manufacturer might make green paint only once every 45 days due to product sequence restrictions.

In 1999, the chemical industry reported a very difficult year, impacted by weakened international economies, slackening demand, over-capacity and a squeeze on prices and margins.<sup>2</sup> These factors made for some of the poorest results in many years. Players in the industry resolved to find new and innovative ways to improve profitability while delivering superior customer service, reducing operating costs, improving plant efficiencies and lowering inventory costs.

The traditional strategies were to extract additional value from existing assets: improving sales and operations functions, reaping economies of scale and capturing synergies. However, the most forward-thinking companies were beginning to see the need to improve supply chain planning processes as the key to future success. The characteristics of the chemical business (notably its finite capacity and cyclical-based manufacturing processes) required a three-way balance of agile demand planning, agile production scheduling and efficient distribution of inventories.<sup>3</sup>

## Eastman chemical and its e-business strategy

Eastman Chemical Company, headquartered in Kingsport, Tennessee, manufactured over 1,200 chemicals, fibres and plastics. It was the world’s largest supplier of polyester plastics for packaging; a leading supplier of coatings raw materials, specialty chemicals and plastics, and a major supplier of cellulose acetate fibres and basic chemicals. In addition, Eastman was one of the top 10 global suppliers of custom-manufactured fine chemicals for pharmaceuticals, agricultural chemicals and other markets. Its chemicals and polymers kept paints and coatings from cracking and extended the shelf life of foods; were used in the manufacture of safer medical equipment, film for smaller electronic devices and more efficient circuit boards for computers; retarded mould in animal feed; enabled garden hoses to bend; contributed to the manufacturing of packaging for beverages, foods, electronics, cosmetics, pharmaceuticals and household products; were raw materials for producing credit and debit cards, electrical connectors, medical devices, vending machines, signs, display cases, carpet fibre, binding fibre for car interiors and upholstery, heavy-duty shipping sacks and pond liners, toothbrushes and tool handles, sports equipment and movie and X-ray film; and were used as ingredients for artificial sweeteners, pain medication, bleach activators in laundry detergent, safety glass, vinyl flooring, disposable gloves, toys and countless other consumer products. As the needs of its customers evolved, so did its product offerings.

Eastman employed 15,800 people in more than 30 countries, with manufacturing sites strategically located in 17 countries. Sales in 2001 amounted to US\$5.4 billion, of which the Asia Pacific Region accounted for US\$547 million. In the 5 December, 2001, issue of Chemical Week, Eastman was ranked 43rd by sales, 59th by profitability and 29th by innovation in the US\$1.7 trillion global industry.

Our primary rationale for making digital business investments has been to enable Eastman to help transform the way the chemical industry does business and to help create industry standards.

(Roger Mowen, CIO & VP – Global Customer Solutions)<sup>4</sup>

Eastman was a recognised industry and world leader in ebusiness transformation. It was the first chemical company to offer customers an easier way to do business with the Company through a portfolio of Web-enabled options. Its e-business strategy included an online storefront and transactional Customer Centre; Web-enabled auctions; alliances and investments in digital business ventures, and system-to-system (S2S) ERP connections. The foundational principles for its e-business strategy were:

 To focus on creating customer-centric solutions.

 To hold a portfolio of options, choices and solutions for customers via electronic channels.

 To invest in technologies/capabilities that bring real value to customers.

 To be externally focused.

 To form partnerships (‘‘We cannot do it alone’’).

 To build an ‘‘e-brand’’ to attract customers, suppliers and technology partners.

 To leverage its intellectual capital, industry knowledge, network of contacts, credibility, brand and customer base.

The Customer Centre (at www.eastman.com), launched in July 1999, enabled registered users to access Eastman’s product information (including technical specifications); check the status of orders; access certificates of analysis, material safety data sheets and other compliance-related documents; track railcar shipments and access the Technical Help service desk. Other e-business related initiatives and capabilities that were introduced are listed in Exhibit 2.

Eastman announced significant achievements towards its e-business goals in 2001. Electronic sales were approaching

30% of total annual sales through all electronic channels such as eastman.com, eastmanmarketplace.com, online marketplaces, EDI and ISS. Over 30% of total procurement for direct and indirect materials was procured electronically. It managed to establish over 20 system-to-system connections with key trading partners. Three digital business ventures were launched in 2000: PaintandCoatings.com, a provider of marketing and commerce solutions for the paint and coatings industry; Cendian Corporation, a virtual logistics provider for in-transit freight and services; and Asia BizNet, an organisation that aimed to facilitate chemical industry e-business solution investments in China and Asia. These ventures were aimed at creating new solutions and reducing inefficiencies in the chemical industry.

<table><tr><td>July 1999</td><td>Launched Customer Centre on its Website in North America. This enabled registered users to access Eastman's product information (data sheets, etc.), check the status of orders, access certificates of analysis, material safety data sheets and other compliance-type documents, track railcar shipments and access the Technical Help service desk. This made Eastman the first chemical company to do business online. ($300 million + online revenue reported in 2000.)</td></tr><tr><td>September 1999</td><td>Announced Eastman's equity investment in ChemConnect, the largest global Internet exchange, making it the first charter Member. The horizontal marketplace provided an open neutral environment where buyers and sellers from around the world met, in real time, to negotiate transactions for all types of chemicals. ChemConnect's World Chemical Exchange was the world's largest Internet chemical exchange, with over 2,000 members.</td></tr><tr><td>October 1999</td><td>Established relationships with Dell Computer Corporation and UUNET to create a Customer Enabling Program that would make it easier for Eastman customers in the US to engage in e-commerce via eastman.com. The program aimed to help customers who did not have computer hardware or Internet access to obtain these capabilities through Dell and UUNET, thus removing barriers to e-commerce.</td></tr><tr><td>November 1999</td><td>Launched EastmanMarketPlace.com, an online solution to quickly liquidate certain materials on an as-needed basis. Auctions are private - by invitation only - in order to ensure that the audience contains valid and qualified participants.</td></tr><tr><td>December 1999</td><td>Launched Customer Centre globally.</td></tr><tr><td>February 2000</td><td>Announced its first B2B pilot programme to provide a direct link via the Internet from Eastman's backend systems to the IT infrastructures of its customer, Albemarle Corporation, and its supplier, Rayonier. The link was enabled by webMethodsB2B. This demonstrated the ability to link separate systems not originally designed to communicate with one another using a Web-enabled platform. Also affirmed the value of supplier-customer partnerships. Eastman pioneered B2B e-commerce in the chemical industry.</td></tr><tr><td>February 2000</td><td>Announced a strategic alliance with SESAMI.com to pioneer e-commerce for the chemical industry in Asia. Eastman became the first tenant on SESAMI.com's chemical portal and implemented SESAMI.com's Web-based eMRO (materials, repairs and operations materials) solution at its plants across Asia. The portal provided a comprehensive online catalogue, auction services, information and e-procurement for direct and indirect goods and services. For Eastman, the vertical portal reduced search and information transfer costs and enhanced matching for buyers and sellers.</td></tr><tr><td>February 2000</td><td>Nagase &amp; Co., Ltd. (Headquarters: Tokyo), Eastman's largest distributor in Asia Pacific, began placing orders online through eastman.com.</td></tr><tr><td>August 2000</td><td>Completed migration from IBM DB2 to the Oracle®Database for its SAP R/3 environment in August 2000. The migration was to</td></tr><tr><td>February 2000</td><td>Announced its first B2B pilot programme to provide a direct link via the Internet from Eastman's backend systems to the IT infrastructures of its customer, Albemarle Corporation, and its supplier, Rayonier. The link was enabled by webMethodsB2B. This demonstrated the ability to link separate systems not originally designed to communicate with one another using a Web-enabled platform. Also affirmed the value of supplier-customer partnerships. Eastman pioneered B2B e-commerce in the chemical industry.</td></tr><tr><td>February 2000</td><td>Announced a strategic alliance with SESAMI.com to pioneer e-commerce for the chemical industry in Asia. Eastman became the first tenant on SESAMI.com's chemical portal and implemented SESAMI.com's Web-based eMRO (materials, repairs and operations materials) solution at its plants across Asia. The portal provided a comprehensive online catalogue, auction services, information and e-procurement for direct and indirect goods and services. For Eastman, the vertical portal reduced search and information transfer costs and enhanced matching for buyers and sellers.</td></tr><tr><td>February 2000</td><td>Nagase &amp; Co., Ltd. (Headquarters: Tokyo), Eastman's largest distributor in Asia Pacific, began placing orders online through eastman.com.</td></tr><tr><td>August 2000</td><td>Completed migration from IBM DB2 to the Oracle®Database for its SAP R/3 environment in August 2000. The migration was to</td></tr></table>

Exhibit 2 Eastman’s e-business initiatives and capabilities.

Exhibit 2 Continued.

Eastman’s mission was to make it easier for business partners to do business with Eastman and to invest in technologies that would bring value to customers. The goals were to change the way the Company interacted with customers and other business partners, and to transform its internal business processes.

## Linking the front end and the backend

In 1992, Eastman adopted the SAP enterprise resource planning (ERP) system, making it probably one of SAP’s largest customers at the time. The system managed information throughout the Company across the supply chain, including bringing raw materials into the plants, operating the manufacturing processes within the plants and fulfilling customer orders. At the production level, production planning tools for continuous manufacturing were deployed to enable manufacturing line changes between product runs, variable supply sourcing, managing maintenance schedules and so on. Eastman later deployed SAP’s Advanced Planner and Optimizer (APO) for these functions (see Figure 1 for the standard APO architecture). The APO provided functions that enabled intra- and intercompany planning of the supply chain and for scheduling and monitoring various processes. For Eastman’s business, acquiring rapid, accurate external data for planning purposes was critical, and for this same reason, the XML integration across its supply chain was strategic. Early versions of SAP were designed for batch and repetitive manufacturing. Eastman worked with SAP in an attempt to apply ‘‘discrete’’ logic to a continuous manufacturing environment. In R/3, additional functionalities such as continuous display of inventory consumption and output were incorporated, but the continuous Available-to-Promise function was not yet available.<sup>5</sup> The Production Planning and Detailed Scheduling (PP/DS) functions would select best manufacturing sequences to minimise costs and/ or time and/or other ‘‘penalty factors’’. Variable supply sourcing could be handled by having multiple R/3 production versions (otherwise known as Production Process Models in SAP lingo) for manufactured items, or if necessary, multi-vendors could be set up with associated transportation lanes to offer selection options for sourcing raw materials. Maintenance Schedules for plant maintenance work were incorporated manually by adding downtime for any equipment resource in APO; production scheduled for these periods would then be ‘‘blocked’’.

![](/api/attachments/26HTXTXD/fulltext/images/473211c9a80ac51aa9fcc90f435c68f353f4a2d138c096bb2427e5f46c80821e.jpg)  
Figure 1 SAP’s standard architecture of the APO.

With Demand Planning, Supply Network Planning, Production Planning and Detailed Scheduling integrated in APO, the planner could display and make decisions regarding demand, supply and inventory data at one plant or many plants. Demand Planning and Supply Network Planning handled aggregation when desired, while Production Planning and Detailed Scheduling aggregated at the plant level.

Forecasting was performed by another system – the Logility Voyager Solution – that helped Eastman create a single forecasting process based on real-time sales data collected from its worldwide sales force via the Company’s Intranet, not historical trends and guesswork. Eastman manufactured a diverse product line. Furthermore, chemical manufacturing was very different to electronics components manufacturing for instance, in that it was a lot more difficult to anticipate market requirements. For example, some products were fourth step or fifth step derivatives of a raw material, e.g., propylene. The continuous manufacturing processes branched off into other processes. Depending on which branches of products were in most demand, production would need to be adjusted to place emphasis on certain branches at any given time. In the past, forecasting was performed by ‘‘departmental islands’’. Logility Voyager enabled Eastman to dynamically combine all those individual forecasts. Aggregating market demand and funnelling this information down to the ‘‘individual product’’ assessment of which products were going to sell in the next 3–12 months therefore demanded accurate forecasting. The supply chain started off with demand planning and ended with fulfilment (transportation planning).

Eastman also engaged in Vendor Managed Inventory (VMI) scenarios with key customers and used data communication technologies (provided by Integrated Support Systems, Inc.) to acquire timely inventory and forecast data, and to respond to order commitments. Furthermore, Eastman engaged in projects to acquire tank telemetry signals via XML directly into its ERP systems for automatic replenishment requests. Re-order points were agreed for each tank so the tank, in effect, would request Eastman’s ERP to schedule a shipment to keep the inventory at specific levels.

The ability to link supply chain computing systems together afforded all the trading partners the opportunity to re-engineer their business processes. It was possible for Eastman to remove work and unnecessary tasks from its internal processes and to re-think the inter-company processes, thus removing work in the extended relationships also. For example, sales and delivery systems were linked such that the systems audited each other as the orders progressed in real time. This eliminated the need for staff to identify discrepancies at the end of each month.

SAP<sup>6</sup> was Eastman’s core technical infrastructure. Data and information about nearly every aspect of its business was contained in SAP. This kind of infrastructure provided connectivity to multi-parties beyond simply point-to-point interactions. Based on this infrastructure, the value of ISS was in its ability to make available to all connected parties the information necessary to manage their businesses. As Craig put it, ‘‘You have to really leverage the network effect you get out of visibility to data from this kind of infrastructure’’.

## The integrated systems solution

Integrating supply chain activities with key customers and suppliers represents a tremendous opportunity to provide more value at reduced cost.

(Mary Kay Devillier, Director – e-Business & Information Resources, Arbemarle Corporation, an Eastman customer)<sup>7</sup>

your vision is to link our production directly to our customers’ manufacturing need. This is more than ecommerce. It is industry-to-industry e-business.

(Lynne Taylor, Manager – Market Development, Rayonier, an Eastman supplier)<sup>8</sup>

There were four elements to Eastman’s e-business strategy (see Figure 2), and one of Craig’s areas of responsibility fell within the system-to-system integration (Integrated Systems Solution or ISS) element. ISS was a means by which Eastman could leverage Internet and XML technologies to enable it to connect its core computing platform or ERP system with the core computing platforms of other companies. This would allow direct data transfer between core systems.

Since 1999, Eastman had invested heavily in a technological infrastructure that would enable it to deploy collaborative supply chain solutions and services based on XML technology (see Figure 3). Upon this infrastructure, Eastman was able to build e-business solutions that would facilitate direct or exchange/marketplace connections with its sales channels, fulfilment channels, financial services providers and logistics services providers (see Exhibit 3). By giving trading partners the option of deploying a webMethods server to process XML messages between Eastman’s SAP system and the Internet, and using webMethods Trading Networks and a CIDX<sup>9</sup> Adaptor to mediate communication between trading partners’ and Eastman’s systems, the Company intended to build in collaborative supply chain management capabilities that would deliver value to Eastman and its business partners (see Figure 4). Fundamental to its strategy was the anticipated ability of ISS and collaborative supply chain management to optimise working capital and increase the Company’s flexibility to market changes. Reducing working capital through integrated production planning systems

![](/api/attachments/26HTXTXD/fulltext/images/46b57f7da4b130ab1285ba25ea38602dc08f44fe5aad4209a0663c4f2b2d353c.jpg)  
Figure 3 The integrated system solution architecture.

![](/api/attachments/26HTXTXD/fulltext/images/49e21291f7705dd69a289128150b7f533d414f00e58bd8902bf619e7b2d1296f.jpg)  
Figure 2 Four elements of Eastman’s e-business strategy.

![](/api/attachments/26HTXTXD/fulltext/images/45560d7ef9abecc8fcdc770264a543b1aaeebbccaa38cbef5b901b0326cf1cac.jpg)  
Exhibit 3 Connecting the various bussiness partners.

![](/api/attachments/26HTXTXD/fulltext/images/22121fd6d9a4db5d3defa05941fd5593da776a799f6d8255cfb665ace80130d4.jpg)  
Figure 4 Applying the webMethods B2B Solutions.

across the supply chain was a priority at Eastman. However, the reduction of working capital was possible only via the deployment of integrated collaborative planning processes in which customers sent electronic demand data, goods receipts and inventory positions, and Eastman automatically replenished the customer’s stock and sent electronic replenishment notifications. Almost all of Eastman’s trading partners wanted to start with the integration of the basic order-to-cash transaction cycle to prove the viability of the technological concept and realise modest savings in data entry relief.<sup>10</sup>

The webMethods partner server software, Trading Networks and CIDX Adapter licence, were offered to business partners free-of-charge to encourage adoption, although they could select any other XML software provider that used a standard protocol for transporting data through the Internet to connect with Eastman. In this way, regardless of whether the partner’s system was an ERP, a legacy system or an EAI engine, systems-to-systems communication could be established. The webMethods Integration Modules could deliver simple files into a legacy system and facilitate XML-to-EDI operations without a VAN. The layout costs for partners included the hardware and network services for installation of the webMethods technology and user training provided by webMethods. Connections typically took 8–12 weeks. Once connected, partners had to ensure sufficient support for the technology at their end. It was also up to the partners to explore and develop the options for multiple tiers of integration with their business partners.

When ISS was launched on a trial basis in 1999, Eastman invited a few of its large customers and suppliers in the US to experiment with the technology in a production environment. Albemarle Corporation and Rayonier were two of the early adopters. At the time, CIDX had not arrived at the Chem eStandards that were subsequently introduced in 2001. Eastman therefore had to work initially with its own agreed definitions and terminologies for, say, export shipment and hazardous warnings, etc. The results were encouraging, with basic purchase orders, sales orders and acknowledgements exchanged electronically after negotiating the business process and data formats with the pilot trading partners. For example, a strategic customer would key in a purchase order to Eastman. Once the order was confirmed, the customer’s system would be programmed to recognise that it was an Eastman order and would automatically generate an XML transmission to Eastman’s receiving system via standard HTTPS Internet protocol. By the end of 2001, Eastman reported monthly transaction volumes in excess of 30,000 XML documents. Eastman saw a lot of potential in the ability to operate a system that could capitalise on other people’s systems and information.

By June 2002, Eastman’s ISS allowed for the issuing of certificates of analysis, the placing of orders, order changes, order cancellations, the issuing of order acknowledgments, ship notices, invoicing and payment notices. Other mainstream transactions including production planning and logistics transactions, and vendor-managed inventory enablement were under development.

Other connections established included service providers such as Cendian. Cendian was an independent chemical logistics service provider that had been spun off from Eastman. The industry benchmark was that a global supplier of chemicals would typically spend 8–10% of revenue on logistics and trade compliance (e.g., regulations for shipping certain products into certain countries, safety warnings, etc). Many business processes were unique to shipping chemicals. In the formative period, Eastman invested significant amounts in Cendian’s technological infrastructure to build a business that would become one of the first specialists in chemical logistics. Cendian used software from Global Logistics Technologies (GLT) to manage and optimise freight movements so as to balance different shipments coming from different countries across the same routing. As a specialist in handling chemical products and with established XML connections with Eastman, Cendian handled all of Eastman’s logistics requirements. Eastman’s relationship with Cendian was vital, as every order that needed to be fulfilled, except airfreight shipments, which were handled by FedEx and UPS, was handled by Cendian. Only on rare occasions were goods transported by air. Many thousands of documents were exchanged between the two companies every month, by far the most heavily trafficked connection. The benefits to Eastman were improved customer service, reduced transportation costs, timely deliveries and reliability, significantly reduced logistics planning time (as the logistics function was now outsourced to Cendian), high visibility and improved control over the tracking of shipments, and optimisation of transactions and processes.

Having the technical infrastructure in place enabled Cendian to benefit from connecting not only with Eastman but also with freight forwarders and other Cendian business partners.

ywe expect these system-to-system links with major trading partners to account for at least half of our online revenues (by 2005).

(Fred Buehler, VP – e-Business)<sup>11</sup>

## Linking the chain

In Asia, Eastman will step up efforts to establish several integrated direct system-to-system digitised connections with its leading trading partners and increase the adoption rate of XML technology and the associated chemical industry standards. 12

In the Asia Pacific region (AP), online sales accounted for approximately 25% of Eastman’s revenue – the highest out of all the regions – at the end of June 2002. The target was to see sales from all electronic channels (refer to Figure 2) increase to around 40% in 12–18 months’ time worldwide. Eastman operated six manufacturing plants in the region that manufactured different products from different raw materials, with each serving different markets. The location of a plant was therefore dependent on access to raw materials, customers and markets. The ISS concept took off much faster in the US, where the majority of the earlier connections were based. The AP region presented some new challenges.

One of the major hurdles companies faced was that they did not have a sufficiently integrated systems infrastructure to fully benefit from connecting with Eastman. Some of the companies that Craig had approached were keen to make the connection with Eastman but wanted to undertake the project as part of their broader business strategy rather than on a piecemeal basis. Many were in the process of planning for or implementing an ERP layer before considering making the Eastman connection.

Eastman ranked its trading partners by volume of exchanged purchase orders and sales orders to identify the largest opportunities for integration. A modest percentage of its trading partners comprised 50% of the total order transaction volume (not revenue or spend), providing a focused opportunity set. When engaging these key trading partners, business experts from both sides examined processes that required significant labour to manage, and considered these pain points for re-engineering projects. For example, processes for monthly invoice reconciliation, pricing change management and pricing support all required significant human attention by both parties, sometimes resulting in mutual write-offs to clear the books. Part of the ISS value proposition was to analyse and discover new process-integration solutions that could extend the value of interconnectivity beyond order-to-cash data-entry labour savings. Integrated collaborative planning, evaluated receipt settlements and so on were part of a growing portfolio of solutions that leveraged the efficiencies of system-to-system e-commerce.

Nagase & Co., Ltd.

In May 2002, Nagase and Eastman celebrated their 50th year of doing business together. Nagase was a major distributor, headquartered in Tokyo. It comprised 102 member companies worldwide and provided trading, marketing, R & D, manufacturing and processing functions to its customers in the chemicals, plastics, electronics and healthcare industries. Japan was Eastman’s single largest market in the AP region. Nagase represented Eastman in the Japan market in almost all business segments. Annual purchases from Eastman totalled around JPY3 billion.<sup>13</sup> The two companies transacted a huge number and a broad cross-section of business interactions. Hence, Craig anticipated that the integration with Nagase would truly be a test case for the technology in a complex business environment.

In spring 2002, Nagase agreed to go ahead with the XML connection with Eastman. As an international trading company, Nagase had thousands of customers and suppliers worldwide. XML technology was considered to be the key to engaging in e-business with these business partners. In preparation for connecting with Nagase, Eastman sent two technical staff from Singapore over to the US for training in implementation, which was planned for Q3. Eastman had provided Nagase with information about what they needed to do to prepare to run the connection. Discussions took place concerning the processes and systems involved, and the mapping of data. Nagase did not have an ERP system. Even before it could embark on connectivity with Eastman, Nagase had to engage in the painstaking task of customising its systems and work processes. The very complex business interactions between the two companies (including understanding the CIDX standards application and agreeing on business process event flows for order-to-cash transactions) and the language difficulties presented challenges for both parties.

Nagase’s information systems consisted of two separate components that handled import/export orders and domestic orders respectively (see Figure 5). PRONETS was the import/export system used to manage foreign order fulfilment, including logistics and customs clearance. APORO was the domestic order management system that was also used to manage the whole company’s inventory. Typically, purchase order requests would be keyed into either system by staff in the Sales Department. Orders were then passed to the Logistics Planning Office, which instructed shippers and administered shippers’ and goods invoices through an accounting system (FINE) that was linked to the Finance Department. From there, the Finance Department would handle payments and a Nagase Logistics Subsidiary would handle customs clearance. When goods reached Nagase’s warehouse, the inventory database in APORO would be updated. A stand-alone system was used by Nagase for order forecasting.

![](/api/attachments/26HTXTXD/fulltext/images/35f507c26dc3390c0c0c0362c8789162327194e26a0fef0bb43cb811e716a35c.jpg)  
Figure 5 Nagase’s import workflow (simplified).

Connecting the two companies required integration not only of technical systems but also of business processes. The trading partners had to assess their business needs and technical proficiency before deciding on the extent to which the business processes could be transferred onto the electronic medium. While the CIDX standard did define processes to handle a multitude of situations, variances in these standard processes were foreseen. These included:

 Agreeing on transaction response timeframes;

 Handling of unmatched order quantities (i.e., when Eastman could not satisfy the order in full);

 Changes in shipment dates.

Electronic solutions to some of these variances were dependent on the technical capabilities of both companies and their willingness to tackle some of the more complicated issues.

Of the order-to-cash cycle, the initial phase of development concentrated on the order and acknowledgment processes. Processes for future consideration included invoicing and shipment notification.

## Only as strong as the weakest Link

The true value is really being able to connect across the whole value chain from raw materials through to our customers.

(Craig Knight)

Before the management of Nagase could decide on the degree of investment they wanted to make in the interconnection with Eastman’s information systems, both sides were to meet to discuss the business needs of each company; the systems and business processes that would require integration, including data mapping, and the likely value added of each integrated process to both companies. Craig focused his thoughts on these issues as he was leaving his office. Labour savings from electronically exchanging purchase-order-related documents for any two companies were typically not significant enough to justify any one connection. Each company had to have strategic plans for multiple connections with high-volume trading partners to begin to realise cumulative savings. How could Craig convince Nagase of the strategic benefits of its investment?

Without doubt, Eastman wanted not only to ride the wave of the transformation that was taking place in the industry but also to lead it. To do so, it had packaged a technological solution that would facilitate interconnectivity in different ways with its business partners. For example, besides the ISS solution, Eastman benefited from the use of its XML infrastructure to initiate purchase orders with companies that did not have the true ISS connection with it. Eastman was confident that the full backend XML integration would deliver productivity gains of 7% in the procurement of direct materials through its supplier portal. All that was required of the suppliers was an interface with a browser-based system. This solution worked well with the non-strategic trading partners or those companies that were not pursuing a comprehensive IT strategy.

On the grander scale of things and beyond the simple order-loop connections, Eastman was also leading a CIDX CPFR Business Process Guidelines Committee to define the initial steps in a standard collaborative planning, forecasting and replenishment (CPFR) process in the chemical industry. Adoption of initial CPFR guidelines would allow more process automation in supply chain management, opening the door to more opportunities to leverage Eastman’s B2Bi expertise. Along the way, the re-engineering of traditionally linear business processes was giving way to dynamic and simultaneous business processes that would capture value for all parties concerned. This was enabled through ‘‘day-in-the-life’’ interviews with strategic partners whereby Eastman staff would trace the interactions that the various staff in the partner company had with Eastman to identify opportunities to capture value and simplify processes or shorten cycle times.

What were the full benefits that could be gained by both Eastman and Nagase through ISS? What was the significance of an integrated supply-chain for Eastman and Nagase? What options did Nagase have for connecting with Eastman? With these options presented to Nagase, it had to decide which option would be most beneficial to its business.

## Teaching note

## Summary

Craig Knight, Asia Pacific Digital Business and Customer Services Manager of Eastman Chemical Company, had been given a mandate to sell Eastman’s philosophy for an integrated electronic supply chain, otherwise known as the Integrated System Solution (ISS), to its business partners in the region, and to encourage its adoption. Having invested in a state-of-the-art technical architecture that would support interconnectivity with all parties along the supply chain, Eastman was keen to realise the full benefits to be gained from an integrated e-supply chain on a global scale. Following numerous rounds of discussion with key business partners in the Asia Pacific region, some progress had been made. Nagase & Co., Ltd. of Japan had agreed to adopt ISS connections with Eastman, but had some reservations regarding the extent of integration. Although the benefits of integration were proven, suppliers, customers, distributors and other interested parties were faced with numerous limitations and considerations that would have significant implications for their established business processes and even the shaping of their corporate strategy. Adoption was not a simple choice. Craig understood these shortcomings and was making every effort to ease the adoption process by identifying the longer-term benefits to

Nagase and other business partners of applying XML technology to their businesses.

## Teaching objectives

The objectives of this case are:

(1) To show that e-supply chain strategy is integral to a company’s competitive strategy;

(2) To identify the underlying technical requirements of an e-supply chain;

(3) To enhance students’ appreciation of the systems and business process re-engineering and integration issues that form the broader picture of what implementation of an e-supply chain entails.

## Suggested student assignment questions

(1) What is the significance of an integrated supply-chain for Eastman?

(2) What are the options available to Nagase for connecting with Eastman?

(3) What are the underlying requirements for integration and what could the limitations be?

(4) Identify the business needs of each company (Eastman and Nagase) and the systems and business processes that would require re-engineering and integration.

(5) Evaluate the full benefits that could be gained by both Eastman and Nagase through ISS, and present this as though you were writing an independent consultant’s report to Nagase.

## Major topics for class discussion

 Integrated supply chain solutions

 Value chain efficiency

 Collaborative advantage and the balance of power within a supply chain

## Analysis

What is the significance of an integrated supply-chain for Eastman?

(This question is designed to identify the benefits of having an e-supply chain.)

In the past, chemical companies have relied on traditional strategies for growth and competition, such as extracting additional value from existing assets. Hence, in the 1970s and 1980s they focused on the functions of sales and operations; in the 1990s they focused on consolidations and restructuring to reap economies of scale and capture synergies to realise cost savings. However, in the 21st century, such traditional strategies are no longer the means for creating shareholder value. Knowledge is becoming an increasingly important part of a company’s capital. Companies will have to focus on knowledge-based strategies to support long-term growth. Knowledge-based strategies are becoming synonymous with Internet-based strategies. The Internet has become a tool or channel for exchanging knowledge, all with the ultimate goal of satisfying end customers.

The single greatest efficiency to be gained from Internet technology is value chain integration.<sup>14</sup> The integrated supply chain that Eastman wants to achieve facilitates optimisation of information flow at each transaction point of the chain. It allows for substantial improvements in profitability and efficiency by affecting multiple factors simultaneously (such as cost-savings, better inventory management and reduced trade-cycle times). While these benefits are commonly identified by many companies and industries as essential to competition today, students should appreciate from the case the peculiarities of the chemical industry and how these peculiarities lend themselves to the full potential offered by Internet technology.

Chemical manufacturers face a number of challenges beyond the manufacturing process itself that directly affect the fulfilment of an order. These include the range of logistics options, the quality of the chemicals, and health and safety issues. They are faced with questions such as whether they can find a chemical tanker that can ship in time; whether the shipping company will preserve the necessary qualities of the chemicals; and whether the quantity of impurities in the products will be acceptable. While these issues have traditionally been resolved offline, companies such as Eastman are now trying to handle these issues electronically. As yet, no e-marketplace or organisation offers the full range of services required by chemical manufacturers. Eastman believes that these offline services can be managed more efficiently through the Internet. Its investment in state-of-the-art technological infrastructure was aimed not only at creating benefits for Eastman’s own business, but also at creating opportunities for it to sell its services and expertise to other players in the industry. To address the peculiarities of the industry and give it a head start in realising its goal, Eastman formed Cendian, a chemical logistics service provider, which it later spun off. Cendian’s role in Eastman’s e-supply chain is crucial. By setting the technical standards and establishing XML connections with Cendian, Eastman is pushing the industry to adopt the same standards.

The integration with Cendian provided the ‘‘proof-ofconcept’’ for Eastman in realising the benefits of being able to pull information from Cendian’s systems and push information out from Eastman’s internal systems to Cendian’s. Being able to share information and knowledge in this way gave Eastman the impetus to connect its systems with its wider network of suppliers, customers and service providers. The traditional EDI approach to supply-chain ecommerce failed to achieve 100% compliance. However, the Internet provides a new solution to achieving 100% compliance. It is less costly, uses a new means of digital document presentation, and accommodates diverse ways for distributing business documents among trading partners. Hence, many of the small, unsophisticated trading partners have the opportunity to participate in the ebusiness network. New mechanisms for data transmission and presentation (e.g., XML) have created new ways of presenting business documents to technologically unsophisticated users that are required to have only minimal software and hardware. This ability to share information beyond geographic and corporate boundaries for the benefit of all parties in the supply chain in fulfilling the customer’s requirements in a timely, efficient and costeffective way is what Eastman sees as its potential competitive advantage. The Internet has forced down the traditional cost barriers to supply chain collaboration. It has also shifted the emphasis to adding value rather than simply competing on price.

What are the options available to Nagase for connecting with Eastman?

Three options are available to Nagase (refer to Figure 2 in the case):

## (1) Eastman Online Storefront

The portal approach allows customers to input orders to Eastman through Eastman’s Website, eastman.com. This was the approach Nagase had been using. Within the Website is a Customer Center where Nagase would log in, place orders, check the order fulfilment status and so on. However, this was a manual process of ordering, which had its limitations. The manual process was slow and prone to human error.

## (2) e-Ventures

Industry solutions are available to Nagase. Middlemen, such as ChemConnect, provide online services that connect buyers to sellers using XML technology. In September 1999, Eastman held an equity interest in ChemConnect, making it the first charter member (refer to Exhibit 2). ChemConnect is a vertical marketplace for the transaction of all types of chemicals. With over 2,000 members, it is the world’s largest online chemical exchange. Subscribers to ChemConnect effectively outsource their XML architecture to the third party. The advantage of this is that subscribers do not have to be too concerned about implementation, as ChemConnect handles the customisation of information systems for them. This is appealing to companies that lack technical expertise. Subscribers also gain access to a ready pool of trading partners with which they can transact online. (Refer to ‘‘E-Hubs: The New B2B Marketplace’’ for additional reading about the future role of e-hubs such as ChemConnect and Chemdex.)

However, the downside to this option is that Nagase would lose some flexibility in the architectural design. The implementation could also be costly, depending on how capable the team is in managing the project. In projects of this nature, the hardware is not the most expensive part; rather, the manpower costs could escalate. Having access to a ready pool of trading partners is also not without its cost. ChemConnect charges annual subscription and per-transaction fees. Nagase would have to assess the value of its investment and the volume of communication and business it would gain from the ChemConnect members, compared with the volume of business transacted with trading partners that do not subscribe to ChemConnect. For Eastman, which had its own XML-based architecture, subscribing to ChemConnect became too costly, and (although this is not mentioned in the case) it decided to relinquish its membership.

## (3) System-to-system Integration (ISS)

ISS, based on the CIDX standard, automates the purchase-order loop. By linking front-end and backend systems, Eastman can work with its trading partners to affect vendor-managed inventory (VMI) processes, outsourcing of logistics functions and so on. ISS allows companies to by-pass the middlemen, and provides greater flexibility for customisation based on the customer’s needs. The CIDX standard defines sets of information (or modules) that must be provided in every purchase order, logistics request and invoice. Adoption of the CIDX standard would enable Nagase to communicate with other companies, besides Eastman, that also use the CIDX standard.

Nagase’s back-end systems, although simplistic, are good enough for applying ISS. Nagase can make use of the webMethods services and tools, but the extent of integration will be dependent on:

 The extent to which it is willing to re-engineer its business processes

 The amount of financial investment it is willing to make  The commitment of senior executives to adopting electronic means of doing business

 The technical capabilities of the company

What are the underlying requirements for integration and what could the limitations be?

(This question is designed to identify the challenges in implementing an e-supply chain.)

Edward Cone writes:

It’s hard to play a team game without teammates, and the supply chain is definitely a coordinated activity. The whole chain suffers if one link is slow to provide information or access.<sup>15</sup>

To achieve full integration, systems need to be able to communicate using common standards. Eastman adopted the CIDX standard. However, it is limited by the challenge of interfacing information flowing between its systems and its partners’ systems because the latter may not have the necessary IT infrastructure to support the CIDX standard. As Ted McDermott puts it:

Becoming e-connected with poor quality data from lower IT systems will do nothing to improve efficiencies in the supply chain or reduce costs.<sup>16</sup>

Standards are essential for realising a fully integrated supply chain. However, convincing players in the supply chain to adopt a radically different approach to doing business can be a painstaking task, as can be seen from the case. For small players, minimal capital investment is required to link their basic back-office systems with those of their trading partners. Eastman provides the web-Methods partner server, Trading Networks and CIDX Adapter licence free-of-charge to its partners. However, for the larger partners, such as Nagase, the implications of adopting XML standards must be assessed in terms of the benefits they would gain from connecting not only with Eastman but also with all the other trading partners in their supply chain. Although Eastman provides the infrastructure for connecting with its partners regardless of the partner’s systems, be they ERP, legacy or an EAI engine, its partners (seeing the longer-term potential of XML-based technology) want to gain more from their capital investment. They do not want to be in a position where they are giving up control for what they see as a limited payback. The true benefits of the e-supply chain can only be realised when the systems that manage the supply chain reach right back into the systems that manage the manufacturing and back-office processes. But achieving operational integration between disparate systems and processes to deliver immediate and reliable results to customers and all the partners in the supply chain is not an easy task.

In order to integrate technical and business processes, large trading partners are having to assess the value that may be gained from various collaborative business scenarios across the supply chain. Such collaboration may be in the areas of engineering project collaboration, customer order and inventory collaboration, distributor– reseller collaboration, supplier and procurement collaboration, demand planning collaboration and warehouse management and freight collaboration. The opportunities that await them are immense. However, before they can realise these opportunities, there needs to be technical and business process integration across enterprises and across heterogeneous applications that reside in the different enterprises.

Many of the back-end systems of Eastman’s trading partners operate in isolation. The first problem they need to address is the internal operations inefficiencies as a result of these disparate systems. Hence, it is not surprising that PricewarterhouseCooper reported in December 1999 that chemical companies are major investors in systems, and SAP’s early growth was primarily due to such investments.<sup>17</sup> One of the conclusions drawn by the report was that the increasing amount of investment in new technology is related to the need to control complexity and generate information for internal and external use. The major areas of spend are reported to be on ERP systems, plant computerisation and networks. Like other industries, the chemical industry is under pressure to change to become more responsive to change. e-Business is becoming an accelerator of change and a shaper of new businesses. In an industry where 80% of costs are estimated to be locked into the supply chain, chemical companies are having to take a holistic approach to re-engineering their processes and systems.

ERPs, such as SAP, are becoming the enabler of operational improvements. These ERPs are integrated packages of software that are deployed enterprise-wide, including human resources, manufacturing, finance, sales and logistics. But implementing an ERP involves fundamental changes to a company’s processes. While technology is the enabler, change management and project execution are critical to the success of the implementation. Furthermore, the pressure to implement an ERP comes not only from the need to resolve internal operational inefficiencies, but also from the need to link processes beyond the organisation to include trading partners – the second problem. One of the fundamental underlying requirements for integration would therefore be to involve both internal staff and external parties who have a role to play in the supply chain. They need to develop global business process concepts that map the resources and information requirements of each party.<sup>18</sup> A gap analysis to compare the business requirements and the systems capability of each party has to be carried out. There follows various decisions for business process changes and systems configurations. So organisations are having to re-engineer the way they interact with their trading partners and customers. The task of integration is similar to business network redesign and business scope redefinition, as described by Venkatraman.<sup>19</sup>

Eastman needs to convince its trading partners that the full benefits of an integrated supply chain requires them to:

 Upgrade their IT systems at all levels to handle the new information demands

 View themselves as part of a value chain

 Focus on providing value to the customer above all else

(Instructors may wish to expand on each of these three points.)

Identify the business needs of each company (Eastman and Nagase) and the systems and business processes that would require re-engineering and integration

Nagase is a major distributor for Eastman. Since Japan is Eastman’s single largest market in the AP region, the potential value of integrating the supply chains of the two companies is immense. Nagase represents Eastman in the Japan market in almost all business segments. Annual purchases from Eastman total around US\$25 million. The two companies transacted a huge number and a wide crosssection of business interactions, which would make the

Table 1 Systems and business processes for Eastman to pull from Nagase’s information systems

<table><tr><td>Information from Nagase</td><td>Rationale</td><td>Re-engineering necessary</td></tr><tr><td>Order forecasts</td><td>For production planning and scheduling</td><td>A stand-alone system is used by Nagase for order forecasting. This means that forecasts would need to be manually generated from the system and passed to Eastman for input into its production planning system. Automating this process would allow Eastman to respond to changes in forecasts in a more timely manner.</td></tr><tr><td>Inventory status</td><td>For production planning and scheduling; materials and capacity requirements planning; just-in-time inventory management and coordinated replenishment</td><td>APORO is used to manage the whole Company&#x27;s inventory. Eastman needs to be able to tap into this database and both companies must agree to minimum inventory levels at which automatic replenishment requests are triggered.</td></tr><tr><td>Logistics requirements</td><td>For shipping consolidation; and distribution requirements planning</td><td>The FINE system is used to co-ordinate logistics. Data from this system should be sent with the orders to Eastman and Cendian. Since Nagase operates out of many locations in Japan, such information would be useful for shipping consolidation and distribution planning.</td></tr><tr><td>Payment status</td><td>For cashflow management</td><td>The FINE system handles payments. It would be useful for Eastman to know the status of payments by being able to log into Nagase&#x27;s payment system. The ease of being able to do so online would eliminate the time and manpower needed for communicating by conventional means.</td></tr></table>

Table 2 Systems and business processes for Nagase to pull from Eastman’s information systems

<table><tr><td>Information from Eastman</td><td>Rationale</td><td>Re-engineering necessary</td></tr><tr><td>Order fulfilment status</td><td>For customer relationship management</td><td>Nagase would be able to respond to customers quickly and with timely information on the status of their orders. Once again, the re-engineering would involve eliminating manual means of communication, which are costly and inefficient. Nagase could pull information from Eastman&#x27;s SAP.</td></tr><tr><td>Shipping details</td><td>For just-in-time inventory management</td><td>The Transportation Planning System within SAP would feed information about shipments to Nagase to ensure scheduled delivery dates are met, etc.</td></tr><tr><td>Inventory status</td><td>For inventory control of perishable items</td><td>As most chemicals are perishable, Nagase wouldn&#x27;t want to hold large stocks of perishable chemicals. Having access to Eastman&#x27;s inventory status would ensure that it could confidently commit to customer requests. Having this information online would improve Nagase&#x27;s response time to customers.</td></tr></table>

1 ‘Economics of the Industry: US Specialty Chemicals, 1999, GAPS Sheet’, Kline & Company, http://www.klinegroup.com/Practices/chemicals/industry\_bu siness.htm, accessed 4 June, 2002.

integration effort a good test case for the technology under a complex business environment.

Table 1 shows the information Eastman would like to pull from Nagase’s information systems on a real-time basis, and the re-engineering of systems and business processes that would be required to enable this:

Table 2 summarises the information Nagase would like to pull from Eastman’s information systems on a real-time basis and the necessary re-engineering of systems and business processes to enable this:

Evaluate the full benefits that could be gained by both Eastman and Nagase through ISS, and present this as though you were writing an independent consultant’s report to Nagase

This report should bring out the discussion points covered in the analysis section of this teaching note. The idea is to have the students come up with rationalised decisions/ recommendations to Nagase.

## Notes

2 ‘2001 Chemical Industry Review’, Chemical and Engineering News, http://pubs.acs.org/cen/topstory/7952/7952bus1.html, accessed on 4 June, 2002.

3 ‘Chemical Companies Discover Supply Chain Planning is Key to Increasing Revenues’, http://wamsystems.com, accessed on 3 June, 2002.

4 ‘Eastman Announces e-Business results for 2000 Establishes e-Business Goals for 2001’, News Archive, http://www.eastman.com, 26 February, 2001, accessed on 28 May, 2002.

5 Available-to-Promise (ATP) was a multi-level, rule-based availability-checking function with due consideration for inventories, allocations, production and transportation capabilities, and costs.

6 Knolmayer, G., Mertens, P. and Zeier, A. (2002). Supply Chain Management Based on SAP Systems, Berlin, Heidelberg: Springer-Verlag , 117, Figure 3.1. Original source: SAP AG.

7 ‘Eastman Pilot Links IT Infrastructure with Supplier and Customer; Based on webMethods B2B’, News Archive, http:// www.eastman.com, 23 February, 2000, accessed on 28 May, 2002.

8 ‘Eastman Pilot Links IT Infrastructure with Supplier and Customer; Based on webMethods B2B’, News Archive, http:// www.eastman.com, 23 February, 2000, accessed on 28 May, 2002.

9 Chemical Industry Data eXchange (CIDX) was a global trade association and standards body that built the XML-based Chem eStandards to define business messages required by chemical companies to carry out highly secure transactions with business partners over the Internet.

10 The order-to-cash cycle refers to the following sequence of information flow: a customer submits an order to Eastman; Eastman acknowledges the order; the customer requests changes to the order; Eastman acknowledges these changes; Eastman advises the customer of the shipment details; Eastman invoices the customer; the customer pays Eastman; the customer advises Eastman of the payment.

11 ‘Eastman announces 15 system-to-system connections; Computer-to-computer links may account for half of the company’s online revenues’, News Archive, http://www.eastman.com, 23 January, 2001.

12 ‘Eastman Commences Online Trading in Japan’, News Archive, http://www.eastman.com, accessed 28 May, 2002.

13 JPY3 billion ¼ US\$25 million.

14 Davydov, M. M. (2001). Corporate Portals and e-Business Integration, New york: McGraw-Hill.

15 Cone, E. (1998). Cautious Automation, InformationWeek Online, 19 October.

16 McDermott, Ted (2000). Forging a Link to the e-Supply Chain, Paper Industry Management Association, Vol. 82 (10), October, pp 34–36.

17 PricewaterhouseCooper, Chemicals – Third Millennium: The New Business Model, European Edition, December 1999.

18 Light, B. (1999). Realizing the Potential of ERP Systems: The strategic implications of implementing an ERP strategy: The case of global petroleum, Electronic Markets 9 (4) 238–241.

19 Venkatraman, N. (1994). IT-Enabled Business Transformation: From automation to business scope redefinition, Sloan Management Review Winter 73–87.

## Further reading

The Economist Intelligence Unit and KPMG International. (2000). Chapter 3: Chemicals, in The e-Business Value Chain: Winning strategies in seven global industries, pp 29–35.

Kaplan, S. and Sawhney, M. (2000). E-Hubs: The New B2B Marketplaces, Harvard Business Review, May–June.

Kulbeda, J. and Roscoe, C. (2000). Chemicals: Strategically Positioning Your e-Business, PricewaterhouseCoopers.

McKeen, J.D. and Smith, H.A. (2002). New Developments in Practice II: Enterprise application integration, Communication of the Association for Information Systems, Vol. 8, pp 451–466.

Roberts, M. (2000). The dawning of next-generation digital supply chains, Chemical Week, New York, 26 July.
