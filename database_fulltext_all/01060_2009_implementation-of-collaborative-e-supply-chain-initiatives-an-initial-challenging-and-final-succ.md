---
otero_id: 1060
otero_key: "J4GSCA2U"
title: "Implementation of Collaborative E-Supply-Chain Initiatives: An Initial Challenging and Final Success Case from Grocery Retailing"
authors: "Katerina Pramatari; Theodoros (Theos) Evgeniou; Georgios Doukidis"
year: "2009"
journal: "Journal of Information Technology"
doi: "10.1057/jit.2008.11"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Teaching case

# Implementation of collaborative e-supplychain initiatives: an initial challenging and final success case from grocery retailing

Katerina Pramatari<sup>1</sup>, Theodoros (Theos) Evgeniou<sup>2</sup>, Georgios Doukidis

<sup>1</sup>Department of Management Science and Technology, Athens University of Economics & Business, Athens, Greece; <sup>2</sup>INSEAD, Fontainebleau, France

Correspondence:

K Pramatari, Department of Management Science and Technology, Athens University of Economics & Business, 47A Evelpidon & 33 Lefkados Street, 113 62 Athens, Greece.

Tel: þ 30 210 8203855;

Fax: þ 30 210 8203854;

E-mail: k.pramatari@aueb.gr

## Abstract

We discuss the challenges of implementing an Internet-based platform for creating collaborative supply chains using a case study in the retail sector. The case presents how an Internet-based collaboration platform was implemented to address the strategic issue of increasing shelf availability and customer service in grocery retailing, an issue that has emerged as one of the major confrontations for the whole sector over the past years. The case presented shows the challenges of executing such strategic collaborative supplychain initiatives which, although arguably beneficial, can be hindered by IT adoption failures. A longitudinal view of the case is presented, from an initial pilot back in 2001 to the final success in 2005. We discuss the particular challenges of the execution of Internetenabled collaborative supply-chain initiatives as well as possible managerial actions through a simple framework we develop based on the lessons from the case. Journal of Information Technology (2009) 24, 269–281. doi:10.1057/jit.2008.11

Published online 17 November 2008.

Keywords: supply-chain collaboration; store-ordering systems; business-to-business; e-business platform; IT implementation; inter-organisational systems; CPFR

## Motivation for and introduction to the study

he advent of e-business has created several challenges and opportunities in the supply-chain environment.<sup>1</sup> The Internet has made it easier to share information among supply-chain partners and the current trend is to try to leverage the benefits obtained through information sharing (also called visibility) across the supply chain to improve operational performance, customer service, and solution development (Swaminathan and Tayur, 2003). Following this trend, core business processes may need to be rethought and redesigned, new organisational forms and inter-organisational structures may need to be developed, and the emphasis shifts towards collaboration rather than competition (Hackney et al., 2004).

In grocery retailing and the fast-moving consumer goods (FMCG) sector, this collaboration aspect has been expressed through the Efficient Consumer Response (ECR) movement. ECR encompasses multiple technological and managerial innovations which aim to transform retailers, distributors, and manufacturers into more efficient and inter-linked organisations placing special emphasis on collaboration (JIPOECR, 1995). One of the first forms of supply-chain collaboration has been the practice of Vendor-Managed Inventory (VMI) or Continuous Replenishment Program (CRP), as it is often called in the context of grocery retailing, where the buyer shares demand information with the supplier who, in turn, manages the buyer’s inventory. The practice of Collaborative Planning Forecasting and Replenishment (CPFR) has extended this collaboration to include the exchange of forecasts based on widely shared information (usually point-of-sales (POS) data and promotion plans), having a more strategic focus and placing more emphasis on the demand side.

More specifically, the VMI/CRP practice has been implemented at the level of the retailer’s central warehouse, based on the daily sharing of the warehouse inventory report data and orders information. Most CPFR initiatives also focus on the central warehouse rather than on store replenishment, and deal mainly with mid-/long-term replenishment planning for promotion items and new product introductions. The VMI/CRP practice has been extensively studied by researchers but mainly from the perspective of evaluating the impact of information sharing on supply-chain performance rather than from the Information Technology (IT) implementation perspective. Furthermore, studies on CPFR mainly define it as a new practice and discuss its adoption or evaluate its business impact.

To better understand the technology adoption challenges of such initiatives, we analyse a case of implementing a web platform enabling information sharing and collaboration between retailers (Veropoulos Spar, a h770 million major Greek retailer) and suppliers (i.e. Procter & Gamble (P&G), Unilever, and Elgeka) to support the store-replenishment process. Contrary to the VMI/CRP practice and prior CPFR initiatives, the focus of this case is on store replenishment rather than on central-warehouse replenishment, addressing the daily ordering process with the objective of maintaining optimum levels of stock in the store and avoiding out-of-stock or ‘out-of-shelf’ (OOS) situations. The problem of OOS is a critical issue for both suppliers and retailers today, as low OOS levels have been positively related to increased consumer value, higher consumer loyalty to the brand and shopper loyalty to the store, increased sales, and higher category profitability (Campo et al., 2000).

The main focus of the case is to illustrate that realising the promises of Internet-enabled collaborative supply chains requires something more than just high-level strategic planning; it also demands the successful implementation of the enabling IT systems. Through the case we discuss the particular challenges of the implementation of collaborative supply-chain initiatives using Internet technologies, and suggest possible managerial actions based on the lessons from the case.

The case has a number of other interesting aspects:

\- it entails an innovative retailer–supplier collaborative business process in a many-to-many environment;

\- it represents a technical challenge: employing an ebusiness platform to support critical operations requiring vast data exchange and synchronisation on a daily basis between various information systems;

\- it addresses a problem that is currently considered as one of the major issues faced by companies in the FMCG sector, that of shelf availability;

\- it shows the extra challenges of such collaborative initiatives due to the need for coordination among a number of organisations;

\- it shows that collaborative supply-chain IT systems can be executed only after the in-house business processes and systems are reorganised and stabilised: companies need to consider Internet-enabled outward-looking processes only after preparing their in-house processes and IT systems.

In the following section, we describe the case context in more detail, covering company background and the process of collaborative store ordering. Next, the course of implementing the web-based collaboration platform in the specific context is presented, from the initial pilot to the fall-out phase and final reincarnation of the project. Then, the lessons from this case as well as relevant problems and propositions are discussed. Finally, we conclude with a discussion and suggestions for further research.

## The case context

## Company background

In the competitive business environment of the Greek retail-grocery market, where two international and three national retail chains account for approximately 60% of the total retail market, Veropoulos is ranked in fourth place with about 9% market share. With 196 stores around Greece, Veropoulos covers almost the whole country, with sales estimated at around 770 million euros for the year 2005. Recent expansion outside Greece has added nine new large stores in the Balkan area.

The company has an organisational structure with three main arms: commercial, logistics, and financial. Nick Veropoulos, CEO and son of one of the two brothers that founded the company, is open to new ideas and a great supporter of ECR global industry activities, participating in both local and European ECR groups. Since 2001, Veropoulos has been the first and only supermarket chain in Greece offering Internet online-store services to its customers.

In terms of product distribution, the company owns a central warehouse serving all the supermarkets around the country with its own fleet of vans. Almost 50% of the products in large stores are replenished through the central warehouse, whereas for the smaller stores the percentage of centralisation is around 60–70%. The remaining is replenished directly to the stores by the non-centralised suppliers.

In spring 2001, Veropoulos suffered an average OOS rate of 8.4%, which can be translated into a yearly turnover loss of more than 20 million euros, leaving aside the negative impact on shopper loyalty and long-term profitability. More than 70% of these situations were attributed to mistakes and omissions in the store-ordering process. Clearly, these numbers indicated that there was a need to improve store ordering and replenishment practices in use at that time. Nick Veropoulos was convinced that ‘even a small reduction in out-of-shelf can bring significant results in turnover increase and improved consumer satisfaction; y clearly this is not a problem we can ignore and the suppliers have to get involved as well; it’s not only ours but also their problem’.

## Collaborative store ordering

A typical grocery retail store (supermarket) has more than 10,000 products in its assortment. Deciding what to order every day at the store level is, naturally, a daunting task. Currently, the store-ordering and replenishment process is a combination of direct-store-delivery (DSD), where the respective product suppliers are those preparing the order (i.e. the list of what needs to be supplied to the store) and delivering their products directly to the store, and centralised delivery, where the responsible store personnel prepare and send the order to a central warehouse, which in turn delivers the products of several suppliers to the store.

Traditionally, various IT systems have supported these processes.

Ogawa (2002) distinguishes between three different types of systems used to support store ordering to the central warehouse. These range from simple replenishment-ordering systems, merely supporting the typing or handscanning and electronic transmission of the order, to automated-ordering and hypothesis-testing-ordering systems, relying on decision support tools using sales data and other information in order to prepare the order, which is either automatically sent or first proposed to and confirmed by a user.

In the case of DSDs, supplier salesmen may use handheld devices (e.g. PDAs) to type in the order and send it electronically over mobile networks while still being in the field. This type of system does not provide any decision support, but in some cases past order data may be used to facilitate the order decision making.

The employment of such systems by both retailers and suppliers in the store-ordering process has had a positive effect on process efficiency, but has not been proved sufficient to address the OOS problem, as reported in several studies (Gruen et al., 2002; Roland Berger, 2003). A reason for this can probably be sought in the difficulty to correctly estimate consumer demand in such a complex environment and the limited information that is available to either retailers or suppliers when working independently to prepare a store-replenishment order. In their attempt to address the problem, retailers and suppliers have turned, during the last decade, towards collaborative replenishment practices, such as CRP/VMI and CPFR.

CPR/VMI has been employed to support the daily ordering process at the level of the retailer’s central warehouse, rendering the product supplier responsible for the demand forecasting and order preparation. In order to do so, the supplier receives the inventory report (in the form of an Electronic Data Interchange (EDI) message) from the retailer’s central warehouse on a daily basis and prepares a suggested order. This may require confirmation by the retailer (in which case the process is called CMI, for Co-Managed Inventory) or not (thus called VMI). CRP moves one step ahead of VMI and reveals demand from the retailers’ stores. The inventory policy is then based on the sales forecast, built from historical demand data and no longer purely based on the variations of inventory levels at the customers’ main stock-holding facility. CPFR can be seen as an evolution from VMI and CRP. It addresses not only replenishment but also joint demand forecasting and promotions planning, focusing on promotions and specialline items. CPFR is based on extended information sharing between retailer and supplier, including POS data, forecasts, and promotion plans. Based on these short descriptions, VMI and CRP are more about efficient replenishment and supply, whereas CPFR puts more emphasis on the demand side.

Combining the characteristics of conventional storeordering systems with information-sharing and collaboration capabilities and applying the notions of CRP/VMI and CPFR at daily store level define new collaborative storeordering processes. The following description illustrates how a web platform can be used to support collaborative store ordering for both DSD and central-warehouse ordering. The central web platform is updated daily with store-level information, including POS data, delivery quantities, product assortment, promotion activities, new product codes, etc. Most of these data come from the retailer’s central information system (e.g. product assortment and product catalogues) and directly or indirectly from the store information system (e.g. POS data), but some information may also come from the central warehouse or the suppliers’ information systems. Based on this information, the system running on the central web platform prepares respective order proposals per individual store. For centralised deliveries, the store personnel review the respective order proposal and, upon confirmation, the order is sent to the retailer’s central warehouse. For DSD, the supplier salesman first reviews the system’s order proposal, which is then sent to the store for final confirmation and then to the supplier for execution. Both the stores and the suppliers’ salesmen access the system through the web. This is schematically depicted in Figure 1.

## Employing an e-business platform for collaborative store replenishment

## The initial pilot

In the context described above, and with the objective of addressing the stockout problems, the promising capabilities of a web platform supporting collaborative store ordering were presented to the top management of Veropoulos by a software service provider, a start-up called OniaNet, in the spring of 2001. OniaNet was a new company acting as an intermediary between supermarkets and their suppliers, supporting their business transactions and exchange of information via its electronic marketplace as an Application Service Provider (ASP).

The positive attitude of Nick Veropoulos, the CEO, towards ECR-related supply-chain initiatives, the presentation of the value proposition by OniaNet, and the full support of a key and trusted supplier (Elgeka) who was also an investor in OniaNet spurred enthusiasm to Nick for such a project and triggered the decision of Veropoulos to pilot test such a system in the spring of 2001.

Suppliers were invited to view this as a unique opportunity to have direct access to daily store sales data (POS data), a possibility that apart from supporting the store-replenishment process would enable them to monitor promotion activities and new product launches, identify missed sales opportunities, etc. Three suppliers agreed to participate in the pilot project. Elgeka, a domestic company with an international clientele, P&G, and Unilever. Elgeka is a DSD supplier operating their own logistics fleet. They were also shareholders of OniaNet, the software service provider. P&G and Unilever, on the other hand, delivered to the stores through Veropoulos’ central warehouse. Moreover, five representative stores were selected to participate in the pilot programme.

The pilot went live on 1 October 2001 and ran in the five pilot stores for 6 weeks, from the 1st week of October to the 2nd week of November 2001. At this stage, the five pilot stores used the Internet-based platform for their collaboration with the direct-delivery-supplier Elgeka, and for ordering the products of the two centralised suppliers,

![](/api/attachments/J4GSCA2U/fulltext/images/e42cc7b08b9fb8ef84e72b868f805800cfc4d13d92ca1dc360c7b9f97999e6db.jpg)  
Figure 1 Collaborative store ordering through a web platform.

![](/api/attachments/J4GSCA2U/fulltext/images/7e4b0a5e745af26cab5f127fe76356f47a8e2df8ff0bcd7c0a6a2b3e9c6c74f4.jpg)  
Figure 2 OOS reduction results from the pilot running.

P&G and Unilever, from Veropoulos’ central warehouse. For the rest of the centralised products, they followed the traditional processes. Moreover, for the remaining suppliers the processes were unchanged.

The evaluation of the pilot, based on systematic OOS and stock measurements, returned business results that were well above expectations soon after the implementation of the pilot: in a 6-week period, the OOS reduced by 62% in the pilot stores but only by 23% in five control stores.<sup>2</sup> In addition, the OOS attributed to the two main reasons, wrong order quantity and no order at all, showed an even higher decrease in the pilot stores (see Figure 2). At the same time, the inventory measurements showed that the OOS reduction was not due to any inventory increase.

However, leaving aside the positive business results, an important lesson from the pilot was that the system could not operate only for a few of the suppliers as this meant that the store employees would have to deal with four different processes just for ordering: ordering to the central warehouse and ordering for DSD in both the traditional and the new way.

Thus, at this point the objectives of the project changed to include the upgrade of the system to support the orderings to the central warehouse for all the centralised products – hence all internal to the organisation ordering – covering over 6000 products from about 600 products during the pilot. Moreover, ‘intelligence’ for making order recommendations to simplify the ordering task of the employees was to be added at this stage. This was very challenging from a technical perspective. These requirements also had to be met in a very narrow time window of about 3 months, as set out by the service provider, who was under funding pressure. It was at this time that the objective of using the e-business platform, therefore, shifted focus from enabling strategic supplier–retailer collaboration to supporting critical within-company operations, mainly the store-ordering process to the central warehouse.

## The failure of the roll-out

Influenced by the relatively positive early business results and by the time pressure of the service provider OniaNet, the top management of Veropoulos decided to roll out the system to the rest of the stores and sign a 3 years contract with OniaNet. After an initial roll-out phase to 20 stores and further work on the system for the next 3 months, the rollout continued with the rest of the stores till November 2002.

Unfortunately, users were not very happy with the new technology as their Internet connections were slow and the web interface seemed too complicated to them. Once all the stores were online the situation got worst, as users started experiencing even more system delays and their frustration with the new technology increased. Many problems also arose from information quality issues, resulting in the system proposing wrong products to be ordered or not including in the order proposal others that should be ordered. This further undermined the users’ trust in the system and the quality of the order proposal. During this time, the service provider worked intensively for over 3 months to overcome the various information-quality issues while the system was in use.

More importantly, it turned out that the actual users in the stores were poorly trained: in fact, although initially the store managers were originally intended to be prime system users (to enable them to evaluate the information and place orders), eventually the store managers ‘pushed’ the system use to other store personnel. These ‘unplanned actual users’, however, were not appropriately trained to use the new system.

On the suppliers’ side the situation was also mixed. For Elgeka, the story was more positive. Apart from being a shareholder in OniaNet, Elgeka as a direct supplier had the human resources to invest in the new system and process and was enjoying benefits that it did not have with the traditional process, such as access to the daily POS information, possibility to order from a distance, etc. With a single salesman, Elgeka was managing orders for 20 of the Veropoulos stores through the collaboration platform.

However, for the centralised suppliers the new process was bringing about major organisational changes, as it required reinvestment in human resources. For example, Unilever as a centralised supplier had laid the responsibility for the whole Veropoulos account to just one salesperson visiting the central warehouse. If the company were to implement the new process, a lot more sales effort would be required to prepare suggested orders for the many retail stores on a daily basis. As the two centralised suppliers were not prepared to undergo these organisational changes for just one of their retail customers, they abandoned the initiative immediately after the pilot. However, they continued to send their product catalogue electronically to the web platform, in order to support Veropoulos in maintaining proper product information and run the storeordering process internally.

Apart from the initial three suppliers, the participation of other suppliers was very limited, as both the problems that the Veropoulos stores were facing with their internal ordering and the anticipated organisational changes were raising serious concerns to them too.

In early 2003, OniaNet, due to financial problems attributed to the suppliers’ limited participation to a great extent, had to stop operations. Nick Veropoulos was caught by surprise. However, most of the people in the stores felt happy they would return to the old familiar system and process.

## The reincarnation phase

From the ashes of OniaNet, a new service provider, having some key personnel from the old OniaNet team, decided to invest in the OniaNet business model in the summer of 2003. The new company, Retail@Link, again approached Veropoulos to recommend a resurrection of the ambitious collaborative ordering initiative. The argument was that, first, the benefits of such a system are clear if they succeeded in implementing it, and second, this time around they knew much more about how to succeed as they had already done a lot of their ‘homework’.

The dilemma for Veropoulos was smaller than initially appeared: if they did not continue they would have to go back to the previous situation; if they continued they had a good chance of achieving the promising business results this time, provided the lessons from the previous attempt were taken into account. Moreover, the internal IT department was not in a position to take this as a new project aboard, so the only alternative still remained with a service provider.

However, the approach to be followed needed to be different this time, especially as far as the participation of suppliers was concerned. The Veropoulos management were convinced that they should first make the system support the internal ordering process efficiently before any attempt was made to open it up to supplier collaboration. This is in line with evidence provided from other industries and cases (e.g. what is considered to be a best practice Internet-enabled business model of Cisco (Nolan, 2001)), suggesting that companies need first to rationalise and webenable their internal systems and processes before implementing Internet-enabled collaborative processes and systems.

In September 2003, Retail@Link was given the green light to pilot test the system, for a second time, in five Veropoulos stores to support orders to the company’s central warehouse only. The implementation approach was quite different this time. Instead of customising an existing e-business platform to the needs of the specific case, which was the approach OniaNet had followed in the past, the new service provider built the system from scratch, based on the user requirements that had been collected during the previous phase from the actual users this time, store managers and personnel, while the technical requirements were focused around scalability, efficient and robust dataloading processes, and fast system response – key technical requirements that hurt the usage of the system during the first attempt. In addition, many data-validation checks were implemented to ensure a high quality of information and reliable order proposals.

The new system was pilot tested for more than 3 months, with the service provider working hard to sort out any issue, even a minor one, that would cause frustration to the end-users. Scalability of the system was ensured by operating the platform for all the stores from the very beginning, even though only five stores were actually using it at this stage.

With the old system as a benchmark, the new system was exceeding by far the pilot users’ expectations this time. Their positive attitude soon spread around, creating a positive anticipation among the rest of the stores. After the system had operated for a full month with no error incident and user complaint, Veropoulos management, being more cautious this time, took the decision to expand the system to the whole chain. Expansion went fast, as the system was centrally hosted and no installations at store level were required. After about 2 months, 160 Veropoulos stores were online, utilising the Internet platform to place orders to the central warehouse.

After a year of successful operation, and after becoming convinced that the new system was internally successful and was there to stay, Veropoulos decided to open up the system, as originally planned in 2001, to supplier participation. Schwarzkopf&Rilken was the first DSD supplier to join in 2005. This time the inclusion of suppliers showed many signs of success. For example, Schwarzkopf&Rilken reported a 64% sales increase in the pilot stores for its products compared to a 3% increase in the total Veropoulos stores and started rolling out the system to the rest of the stores. Other suppliers started piloting as well, mainly centralised ones wishing to access store sales data.

## Discussion: challenges and lessons learned

In this section, we identify the main challenges encountered and discuss some of the lessons from the case. We group the challenges of execution in three main categories: technical challenges, organisational challenges, and multiparty coordination challenges (see the framework in Figure 3). Table 1 also summarises the main points that were done differently, regarding these challenges, the second time relative to the first one, which turned this case from an initial failure to a final success.

The objective of this discussion is to illustrate that realising the promises of Internet-enabled collaborative supply chains does not just require high-level strategic planning and top-management commitment, but also the successful implementation of the enabling IT systems, addressing technical, organisational, and coordination issues in a many-to-many environment. Other dimensions, pertaining to the translation and power perspectives of different actors, as discussed in the last part of this section, need also be considered.

## Technical challenges

First, the case exposes some important yet often disregarded ‘technical’ principles that should characterise any information system development and that are especially

# Technical Challenges

Information quality User friendliness and system response speed Scalability Data-links management

![](/api/attachments/J4GSCA2U/fulltext/images/1359901396898ca2613611b7c02aac50dca6b4f432d6402f88cfdab5a365e5ba.jpg)

Organisational Challenges

Multi-party Coordination Challenges

Alignment of organisation and technology User involvement Communication Roll-out plan and testing

ASP capabilities Supplier involvement

Figure 3 A framework depicting the key challenges of implementing Internet-enabled collaborative supply-chain initiatives.

Table 1 Key challenges and managerial actions: comparison between first and second phase

<table><tr><td></td><td>First phase - failure</td><td>Second phase - success</td></tr><tr><td colspan="3">Technical issues</td></tr><tr><td>Information quality</td><td>Information quality was improved gradually, with new data-validation mechanisms being integrated into the system as new problems appeared</td><td>Information quality was ensured with many data-validation mechanisms being incorporated in the system from the beginning</td></tr><tr><td>User friendliness and system response speed</td><td>The system suffered slow response speed and poor usability, due to slow Internet connections and many web pages</td><td>The user interface was totally reorganised, requiring much less interaction by the user, which greatly improved response rates and usability</td></tr><tr><td>Scalability</td><td>The system was not designed to support many stores and suppliers in a demanding data environment, which resulted in serious performance degradations as more stores were added to the platform</td><td>The system was designed from the beginning to meet the requirements of the specific case, thus scalability was ensured from the onset</td></tr><tr><td>Data-links management</td><td>Information exchange was based on unreliable FTP connections</td><td>A new reliable file exchange mechanism was built based on the web-services technology</td></tr><tr><td colspan="3">Organisational issues</td></tr><tr><td>Alignment of organisation and technology</td><td>The system was based on the customisation of an existing e-business platform supporting typical functionality of a B2B marketplace</td><td>The system was designed and built from scratch to match the specific requirements of the company with changes to work practices carefully managed</td></tr><tr><td>User involvement</td><td>Not all actual users were consideredActual users were not involved in the user-requirements phaseSome users liked the system but others expressed strong negative comments that were partly disregardedThe actual users were not trained to use the new system</td><td>The users had active participation in the definition of the requirements and experience from using the first systemAll comments expressed by the pilot users were taken into great considerationMore emphasis was given to user training</td></tr><tr><td>Communication</td><td>Users felt the ‘hard to use’ new system may at some point get ‘unplugged’Some users liked the system but others expressed strong negative comments that were partly disregarded</td><td>Top management communicated clearly that ‘the system is here to stay’All comments expressed by the pilot users were taken into great consideration</td></tr><tr><td>Roll-out plan and testing</td><td>The roll-out plan was guided by external pressure by the service provider and not by internal capabilities and assessment</td><td>The roll-out to the rest of the stores would not start before all the pilot stores were satisfied and the new system would work without a single disruption for quite some time</td></tr><tr><td colspan="3">Multi-party coordination issues</td></tr><tr><td>ASP capabilities</td><td>The risk of bankruptcy for the ASP provider was ignored</td><td>The financial viability of the new ASP provider was well examined before the new start</td></tr><tr><td>Supplier involvement</td><td>Collaboration with the suppliers was sought before internal processes were streamlined</td><td>The system was opened to suppliers after internal business processes started running smoothly</td></tr></table>

important in supporting supply-chain integration:

1. Efficient data management and validation mechanisms are crucial to ensure information quality which in turn is crucial for instilling trust in people towards any decision support system.

2. System user friendliness, ease of use, and speed of response are important determinants of user satisfaction and system acceptance.

3. For large IT systems connecting many other systems (possibly from many organisations), the points of possible failures increase exponentially (why exponentially? Don’t they increase more-or-less linearly as the number of suppliers involved increases?), requiring extra technical and management care before broader roll-out.

If these principles had been respected, many technical and usage (‘on the ground’) problems with the system could have been avoided the first time. However, the technical challenges of setting up this collaboration platform for the first time were, as always, too many and possibly disorientated people from these basic principles. The technical challenges, stemming from the three key principles outlined above, are mainly related to the following.

## Data-integrity and synchronisation issues

Roland Berger (2003) identifies data accuracy and synchronisation as one of the top five challenges the grocery sector faces today in the attempt to streamline the supply chain. Although the sector has adopted barcoding technology as a standard to identify products, yet the information is maintained at different levels in either the retailers’ or the suppliers’ systems causing serious integrity issues when data synchronisation is required. In order to overcome these issues, several data-validation and integrity-checking rules had to be built into the final system so that information quality problems did not confuse the endusers and undermine the order proposals’ reliability.

Quality of the automated inter-organisational system links Many of the data-quality problems resulted from errors and mistakes in the file-transfer process and exchange of data files between the retailer’s systems and the collaboration platform. The use of FTP, which was the initial approach, was not adequate to meet the requirements of such a demanding data environment in terms of both reliable and secure file transfer. In the second approach, the technology of web-services (Ferris and Farrell, 2003) was used instead to support the exchange of data files. Here, several control mechanisms were implemented to ensure reliable and secure information exchange. The data-loading processes were also enhanced to become more robust to data failures and send e-mail and/or SMS notifications in case of critical errors.

Web-user interface combined with slow Internet connections One of the most technically challenging issues was to enable efficient decision support for the ordering of about 1000 products (which was the average size of an order proposal) over a dial-up Internet connection of 56kbps at best. The challenge involved both deciding what information to display to the user in order to enable the right ordering decision and selecting the right functionality to allow for fast browsing and order update. What was causing a lot of frustration to the users with the initial OniaNet system was the idle time they had to spend in front of a PC just waiting for web-pages to download (in some cases this was more than half an hour in total for updating a single order). With the new system, the users take a printout of the order proposal, consult it when physically checking the store, and then type in the final order in much the same way they did before the OniaNet system but just faster. Further improvement of the system is currently sought towards the direction of loading the order proposal on a hand-held device, enabling the user to update the order simultaneously with the physical shelf check.

## Scalability of the centralised software architecture

Schuff and St. Louis (2001) have analysed the benefits of centralisation vs decentralisation of application software. In our case, the centralised software architecture, imposed by the central web collaboration platform model, led to serious scalability issues initially. When all the 260 stores were using the OniaNet platform for their ordering to the central warehouse, the users started experiencing serious delays in the system response. However, the scalability problem dissolved after (a) the system’s database was redesigned and (b) new functionality was provided for order –update, which resulted in limited user interaction with the system. Table 2 summarises the advantages and disadvantages of centralised vs decentralised software architecture to support collaborative store ordering.

A variation of the centralised model, enabled, for example, by the use of web-services technology, allows that part of the processing (e.g. what requires extensive user interaction, such as the order update) to take place in the store, while the gathering of the information, the management of the order proposal criteria, etc., continues to take place centrally. This hybrid approach combines the benefits of both models, but the respective technology is not fully implemented and tested yet.

## Controlling the various points of system failure

Last but not least is the technical challenge of controlling the plethora of points of failure in such a complex system. In addition to controlling hardware and software failures of the main platform (web servers, application servers, database servers, data-loading processes, etc.), many new points of failure are added, most of which relate to the ebusiness characteristics and inter-organisational nature of this environment. These range from Internet connectivity issues in the stores to back-end integration and file-transfer issues between the central platform and the various information systems, to hardware printer failures in the stores, etc. No matter what reason applies, in the eyes of the end-user any of these failures results in either system unavailability or information flaws, translated further into inability to carry out the critical business process of store ordering. Therefore, any such system should be equipped with various failure control mechanisms and should be iteratively and rigorously tested (and pilot tested before broader, possibly phased, roll-out) in order to eliminate or minimise such a possibility.

Table 2 Centralised vs decentralised IT implementation

<table><tr><td>IT implementation model</td><td>Pros</td><td>Cons</td></tr><tr><td>Centralised</td><td>Easy management of data integration linksData quality need only be maintained in one single systemLess expensive as there is only one central node requiring processing powerEasy upgrades of hardware and software</td><td>Slight delays in the system response if accessed in interactive modeIn case of a central failure, all the stores are affected</td></tr><tr><td>Decentralised</td><td>Faster system response in interactive modeA failure in a local system does not affect the other store systems</td><td>Rather infeasible to get the suppliers involved in the collaboration processDifficult to manage all the links between the required data sources and all the storesDifficult to maintain high levels of data quality in all store systemsHigher cost for software and hardware upgradesMore expensive as considerable processing power is required in each store</td></tr></table>

## Organisational challenges

This case is clearly a demonstration of technochange, defined by Markus (2004) as situations where IT is used in ways that trigger major organisational changes. Hence, unavoidably the success of such systems and the strategic initiatives they support relies on the careful management of change in the organisation (Kallio et al., 1999). The contrast between the initial failure and later success provides lessons on the challenges of such a technochange. These challenges can be seen at various levels: user involvement, communication, and technology/business alignment and business process redesign. We consider these next.

## User involvement challenges

To begin with, the case provides a vivid example of the difficulty of even sometimes defining in large organisations ‘who the actual users of the new system will be’. During the first attempt, the company’s management team assumed the actual users would be the store managers. However, over time it became clear that, largely due to the difficulties in using the new system (which also shows how all challenges are inter-twined in complex ways), the managers ‘pushed’ the usage of the system to other store personnel. It is often the situation that the final users of new technologies are a broader (or even different) group than the one initially considered, and this case clearly shows the degree of this challenge. Moreover, a main difference between the two attempts was the more careful definition of requirements – given also the experience from the initial failure – in collaboration with the users during the second attempt. Finally, training is a fundamental part of any large IT implementation often overlooked. The initial difficulties in the early attempt show the dangers of poor training of the actual users.

## Top-down and bottom-up communication

Despite the positive business results from the very beginning, many end-users were resisting the introduction of the new system – probably due to usage difficulties and unclear vision of the value of the system. For example, there is anecdotal evidence that during a company-wide event in 2002 some store managers ‘requested the withdrawal of the new system’. Some users were also under the impression that the system will finally ‘fail’ and hence be withdrawn. Such phenomena emphasise a key success factor of such implementations: heavy top-down communication of the value of the new system and of its final persistence. At the same time, bottom-up communication is also valuable. While initially some of the negative comments of the users were disregarded, in the second attempt all users’ comments (i.e. complaints from the initial pilot) and perceptions of the new system were very carefully gathered and taken into consideration.

## Technology/business alignment and business process redesign

A fundamental principle in information systems implementation is the very delicate balance between building the system according to user requirements and changing the users’ work practices to conform to specific system dictates (Butler and Fitzgerald, 1999), such as those posed by a predefined e-business platform. Some of the key decisions of large implementations are answers to the question ‘should we change the system or should we change the business practices’. The case also shows the challenges of managing the complexity of business processes with the introduction of new technologies. For example, during the first attempt it became clear that the introduction of two new processes (order processes via the new system from the central warehouse as well as from the direct suppliers) increased the overall complexity of the order processes: there were now four different processes instead of two. It therefore became crucial to redesign the business processes by effectively eliminating the old ones from the central warehouse. As clearly noted in the past, business process re-engineering – effectively involved during large IT implementations – is not only about ‘automating business processes’ but also about ‘obliterating’ them (Hammer, 1990).

## Multi-party coordination challenges

E-business initiatives across companies, such as the esupply chain one considered here, have a whole new set of challenges, compared to within-company large IT implementations, due to the involvement of many independent organisations. The case shows clearly the challenges of such e-supply-chain initiatives that arise from the need for coordinating many parties ‘outside the boundaries of the firm’. Some of the challenges arise from the nature of the ASP business model, and of e-marketplaces in general, while others arise from the coordination between the retailers and the suppliers.

## The challenges of the ASP model

According to the ASP model, ASPs offer and manage outsourced application services to many organisations via the Internet, while organisations outsource applications to ASPs to reduce upgrade and maintenance costs and to focus their efforts on core competencies (Soliman et al., 2003). The appeals of ASPs are the per-user pricing models, one-to-many access possibilities to applications, IT expertise and capabilities, and value-added management services (Kern et al., 2002).

What Veropoulos learned from the first experience was that before deciding to use the services of an ASP, the financial viability and long-term commitment of the provider need to be ensured, especially when the switching costs are high. Kern et al. (2002) argue that although the ASP model offers an electronic outsourcing solution, there are in fact many similarities with more traditional IT outsourcing. Soliman et al. (2003) also mention additional issues that need to be addressed by a retailer when examining the use of the ASP model for supporting the store-ordering process, such as reliability, service level, etc. Given the many points of system failure as discussed above and the high dependence of the store-ordering process on information quality, the definition and guarantee of a clear service level is quite difficult in the case discussed. Furthermore, because of the extent of information provided by the retailer’s information system and loaded on the collaboration platform, a retailer may feel uncomfortable to provide all this information to a third party and lose control over it. From informal discussions with all major Greek retailers, it is clear that many of them feel concerned about having a big portion of their internal data hosted on the platform of an ASP.

At the same time, some global retailers such as Wal-Mart, Metro, and Tesco have built their own private exchanges to support collaboration with their suppliers. However, suppliers do not feel comfortable with the idea of being connected to a separate collaboration platform/exchange for each retailer. A neutral platform operated by an independent third party, which enables information exchange and collaboration between retailers and suppliers in a many-to-many environment, positively contributes to achieving a critical mass on both sides (Hsiao, 2003). On the other hand, neutral marketplaces face more difficulties than private and consortia exchanges, because they need to develop trust relationships among buyers and suppliers before a critical mass of users can be reached (Christiaanse et al., 2004). This statement is also supported by the case presented, where both the old and the new service provider, operating as vertical, neutral, electronic marketplaces, or else independent exchanges, faced the problem of building the critical mass of retailers and suppliers. As already mentioned, this is one of the main reasons behind the liquidation of the first service provider. Grieger (2003) further concludes that a reason for failures of electronic marketplaces can be found in the dilemma that operators of such marketplaces concentrated on the integration of information systems rather than on integration of specific business processes, which is also supported by this case, as more emphasis was placed on overcoming the technical challenges rather than the organisational ones.

## Supplier–retailer coordination challenges

One of the reasons that led the initial service provider, OniaNet, to bankruptcy relates to the overestimates of the entrance rate of suppliers into this new form of collaboration with Veropoulos and respective income streams for the service provider. While the suppliers initially appeared enthusiastic about it with clear incentives (in case of success) to participate, several barriers soon had a slowdown effect on their decision to exploit this new opportunity. These relate to the barriers to electronic marketplace adoption mentioned by Hsiao (2003), including technology, organisational, and collaboration barriers. In addition, suppliers felt concerned that this was an innovative business process with very local impact, not implemented elsewhere in the world. While this new form of collaboration between retailers and suppliers can be regarded as a new form of CPFR (Pramatari et al., 2002), the suppliers, especially multinational companies, did not feel that this process would become common business practice across many retailers in different markets.

Regarding the incentives of the suppliers, it was clear (i.e. see Figure 4) that DSD suppliers had stronger incentives for adopting the process of collaborative store ordering as for them it represents not only a chance to improve shelf availability but also a cost-reduction opportunity through reduced store visits. Hence, it was probably expected that the one direct-store-supplier, Elgeka, would remain in the project longer than the others. Moreover, Elgeka as a direct supplier had the human resources to invest in the new system and process: in fact the new system did not require more human capital, since with a single salesman Elgeka was able to manage orders for 20 of the Veropoulos stores through the collaboration platform. The story was very different for the centralised suppliers P&G and Unilever: while initially supportive of the initiative, over time it became clear that to succeed these suppliers needed to increase the number of employees working with Veropoulos. Their decision in the past to move to centralised deliveries had been followed by reductions in their sales force which would now need to be reversed because of the particular collaborative ordering initiative. Given the challenges the initial pilot faced, it was not clear for these centralised suppliers whether it was worth to take the risk and put extra, possibly permanent (human) resources to this programme.

![](/api/attachments/J4GSCA2U/fulltext/images/82cb5507f8b6a9533567213650f44c7abbd79d2420e00e72d3f1cad882472fbf.jpg)  
Figure 4 First pilot users’ feedback on ‘The new way of work does not present any difficulties’.

The change over time of the centralised suppliers shows the importance of commitment to such initiatives by all participants. Such initiatives unavoidably face many implementation challenges, as discussed above, so they require strong commitment and involvement of extra resources (i.e. more human capital) by all parties (i.e. the centralised suppliers, too) if they are to succeed. Unlike the case of within-organisation implementations where commitment can be secured, for example, by strong topmanagement support overarching the whole implementation, such ‘inter-organisational top management’ support is, by definition, lacking for multi-party implementations. This makes the commitment of every single party involved crucial. Moreover, the need to increase the sales force for some of the suppliers (i.e. the centralised ones) shows the organisational impact such initiatives can have to all parties involved. The realisation of this need only later in the process also shows how these large multi-party IT-enabled initiatives can have consequences that were not fully expected initially. Had the centralised suppliers committed extra sales people beforehand they might have remained in the project throughout.

We also note that in the long run, the adoption of the new system would lead to changes in the roles of the suppliers’ sales force, requiring sales people to work as consultants/merchandisers, who can identify growth opportunities and become problem-solvers, rather than mere order-takers, who follow a fixed store-visiting schedule. This further implies significant organisational changes, especially for DSD suppliers, as well as new skills for the sales personnel.

The coordination with the suppliers therefore brings up a number of new challenges, beyond the ‘within organisation ones discussed in the above section. It was thus a wise decision for Veropoulos to go, the second time around, for a solution that would work for the stores internally first, regardless of the suppliers’ entrance rate into the collaboration process.

The case shows clearly the importance of first rationalising the IT systems and processes and implementing esupply-chain modules in-house before starting the creation of more electronic links with the suppliers.

## Conclusions

In this paper, we have presented a case of employing a web platform to support a new process of supply-chain collaboration in grocery retailing. The case shows that web technologies can offer companies new alternatives towards achieving strategic business objectives, by enabling new collaboration processes and extended information sharing. At the same time, the case illustrates that collaborative supply chains enabled by new Internet technology can be hindered by difficulties in implementing large IT systems. Several technical, organisational, and multi-party coordination challenges had to be overcome in order to turn this case from an initial failure to a final success.

The initial decision to customise an existing e-procurement platform to support the new collaboration process proved inadequate. Other technical challenges ranged from mastering the various data quality issues and information links to controlling the various points of failure and achieving a scalable system architecture. On the organisational side, the involvement and proper training of endusers appeared to be one of the major challenges, which required the proper management of top-down and bottomup communications as well as the alignment of technology with the business processes. Apart from these, the ASP and marketplace model as well as coordination with suppliers raised issues that were initially underestimated. Moreover, the case suggests that collaborative supply-chain IT systems can be easier to execute after the in-house business processes and systems have been properly settled.

After the roll-out of the new system in 2003 and 2004, Veropoulos has been using it continuously to support the store-ordering process to the central warehouse. Three years afterwards, the management of Veropoulos declares satisfaction with the use of the system and believes that it has helped them maintain relatively low levels of OOS. However, periodical trainings of the store personnel are considered necessary in order to keep new people familiar with the system and make the best out of it.

Schwarzkopf&Rilken, the first supplier to collaborate with Veropoulos in 2005, currently uses the system for about 40 of the Veropoulos stores, but has not rolled it out to all the stores as initially planned. This is mainly attributed to information quality issues with store inventory data, which require that the supplier salesmen visit the store and physically inspect the product inventory quite often, if not each time they place an order. This certainly undermines the benefits of this supply-chain collaboration initiative, since it does not reduce the cost of store ordering as initially expected by the supplier. However, this has not been the case with another retailer that followed shortly after the Veropoulos example.

Galaxias, one of the top five Greek retailers with about 100 stores, after an initial pilot with three stores, rolled out the system to all the stores gradually in about a year’s time. The introduction of the system in the new retailer ran smoothly, as the service provider who led the project could build on the lessons learnt from the first case, as explained above. The supplier Schwarzkopf&Rilken, despite having started with Veropoulos, reports today that collaboration with the Galaxias stores has proceeded faster and easier. This, as the Galaxias store people play an active role in monitoring and updating the store inventory data, allows the supplier to place orders from a distance. This fact, which greatly facilitates the role of the salesman, has enabled two other multinational suppliers, apart from Schwarzkopf&Rilken, to work collaboratively with the Galaxias stores in the ordering process. For several other suppliers, the system is used for monitoring product sales for the Veropoulos and Galaxias stores rather than for ordering purposes.

The list of challenges mentioned in this paper is obviously not exhaustive. The topic of collaborative supply chains is relatively new, so there is a lot more to learn from various perspectives. In addition, the lessons acquired from this case need to be ‘transferred’ to other organisations with care, since this particular case is from a company in a relatively small and possibly not as technologically mature market, although it is a large company and itself open to new technologies and business practices.

On the other hand, the lessons acquired from this case pertain to other supply-chain collaboration initiatives, such as CPFR, involving supplier–retailer collaboration in a many-to-many environment and accompanied by organisational changes and coordination issues. From an e-business perspective, the study contributes in presenting practical issues associated with new Internet-enabled supply-chain management practices and draws attention to issues other than technical aspects.

While the study has been carried out in the Greek grocery retail market, its findings are relevant to practitioners in other western markets as well. This is supported by a recent study comparing retail practices in more than seven western European markets (ECR Europe, 2005), which shows that big retail chains and their suppliers, which are mainly multinational companies, operate in a similar way in the various western European markets including Greece.

More implementations and pilot experiments, other than the first case reported in this paper, are required in order to shed more light on the different aspects of this new supply-chain collaboration practice and the enabling role of new e-business infrastructures. Questions relating to the adequacy of the infrastructure, to the business model and operation mode of the collaboration platform, to the motives and barriers to adoption of supply-chain collaboration practices and electronic marketplaces are some examples for further research directions suggested by the presented case.

## Notes

1 A copy of the accompanying teaching notes is available to bona fide faculty members and can be obtained by contacting the authors directly.

2 The reason there was an OOS reduction in the control stores has to do with the fact that the subjects taking part in the experiment (the order decision makers in the stores) take notice of the fact there is a measurement and this influences their behaviour, which is referred to as the Hawthorne effect.

## References

Butler, T. and Fitzgerald, B. (1999). Unpacking the Systems Development Process: An empirical application of the CSF concept in a research context, The Journal of Strategic Information Systems 8(4): 351–371.

Campo, K., Gijsbrechts, E. and Nisol, P. (2000). Towards Understanding Consumer Response to Stock-Outs, Journal of Retailing 76(2): 219–242.

Christiaanse, E., Diepen, T.V. and Damsgaard, D. (2004). Proprietary versus Internet Technologies and the Adoption and Impact of Electronic Marketplaces, The Journal of Strategic Information Systems 13(2): 151–165.

ECR Europe (2005). The Business Case of ECR, ECR Europe Publications, www.ecrnet.org.

Ferris, C. and Farrell, J. (2003). What Are Web Services? Communications of the ACM 46(6): 31.

Grieger, M. (2003). Electronic Marketplaces: A literature review and a call for supply chain management research, European Journal of Operational Research 14(4): 280–294.

Gruen, T.W., Corsten, D.S. and Bharadwaj, S. (2002). Retail Out-of-Stocks: A worldwide examination of extent causes and consumer responses, The Food Institute Forum (CIES, FMI, GMA).

Hackney, R., Burn, J. and Salazar, A. (2004). Strategies for Value Creation in Electronic Markets: Towards a framework for managing evolutionary change, The Journal of Strategic Information Systems 13(2): 91–103.

Hammer, M. (1990). Reengineering Work: Don’t automate, obliterate, Harvard Business Review 68(4): 104–112.

Hsiao, R.L. (2003). Technology Fears: Distrust and cultural persistence in electronic marketplace adoption, The Journal of Strategic Information Systems 12(2003): 169–199.

Kallio, J., Saarinen, T., Salo, S., Tinnila¨, M. and Vepsa¨la¨inen, A.P.J. (1999). Drivers and Tracers of Business Process Changes, The Journal of Strategic Information Systems 8(2): 125–142.

Kern, T., Kreijger, J. and Wilcocks, L. (2002). Exploring ASP as Sourcing Strategy: Theoretical perspectives, propositions for practice, The Journal of Strategic Information Systems 11(2): 153–177.

Markus, M.L. (2004). Technochange Management: Using IT to drive organisational change, Journal of Information Technology 19: 3–19.

Nolan, R. (2001). Cisco Systems Architecture: ERP and web-enabled IT, Harvard Business School Case, 9-301-099, 15 October 2001.

Ogawa, S. (2002). The Hypothesis-Testing Ordering System: A new competitive weapon of Japanese convenience stores in a new digital Era, Industrial Relations 41(4): 579–604

Pramatari, K., Papakiriakopoulos, D., Poulymenakou, A. and Doukidis, G.I. (2002). New Forms of CPFR, The ECR Journal – International Commerce Review 2(2): 38–43.

Roland Berger (2003). ECR-Optimal Shelf Availability, ECR Europe, www.ecrnet.org.

Schmitz, J., Frankel, R. and Frayer, D.J. (1995) ECR Alliances: A best practices model, A research monograph for the Best Practices Operating Committee: Joint Industry Project on Efficient Consumer Response.

Schuff, D. and St Louis, R. (2001). Centralization vs. Decentralization of Application Software, Communications of the ACM 44(6): 88–94.

Soliman, K.S., Chen, L. and Frolick, M.N. (2003). ASPs: Do they work? Information Systems Management 20(4): 50–57.

Swaminathan, J.M. and Tayur, S.R. (2003). Models for Supply Chains in E-Business, Management Science 49(10): 1387–1406.

## About the authors

Katerina Pramatari is Assistant Professor at the Department of Management Science and Technology of the Athens University of Economics and Business (AUEB). She holds a B.Sc. in informatics and an M.Sc. in Information Systems from AUEB, and a Ph.D. in Information Systems and Supply Chain Management also from AUEB. She has won both business and academic distinctions and has been granted eight state and school scholarships. Her research and teaching areas are supply and demand chain collaboration, traceability and RFID, e-procurement, e-business integration, and electronic services. She has published 18 papers in scientific journals including the Information Systems Journal, European Journal of Operational Research, Computers and Operations Research, Supply Chain Management: An International Journal, and International Journal of Information Management.

Theodoros (Theos) Evgeniou is an Associate Professor of Decision Sciences and Technology Management at INSEAD.

Having won medals in international mathematical olympiads (in places like China, Sweden, Romania, etc.), he received two B.Sc. degrees, one in Computer Science and one in Mathematics, simultaneously from MIT, from where he also graduated first in the MIT class of 1995 dual degrees in Mathematics. He then received a Master’s and a Ph.D. degree in Computer Science, also from MIT. Before joining INSEAD, he has held positions in companies in Japan and in the US and has been involved in a Boston-based hightech start-up. At INSEAD, Theos has been teaching courses on IT strategies, data mining, and information systems management. His current research interests are in the areas of data mining and business intelligence as well as online market research.

Professor Georgios Doukidis has a B.Sc. in Mathematics, University of Thessaloniki, an M.Sc. in Operational Research, London School of Economics, and a Ph.D. in Simulation/Artificial Intelligence, London School of Economics – LSE. He worked as a lecturer at LSE and a visiting professor at Brunel University. Currently, he is Professor in the Department of Management Science and Technology at the Athens University of Economics and Business (AUEB) and Director of the ELTRUN E-Business Research Center. He has published more than 60 papers in scientific journals and acted as guest editor in the Journal of the Operational Research Society, European Journal of Information Systems, Journal of Information Systems, International Journal of E-Commerce, and Supply Chain Management: An International Journal.
