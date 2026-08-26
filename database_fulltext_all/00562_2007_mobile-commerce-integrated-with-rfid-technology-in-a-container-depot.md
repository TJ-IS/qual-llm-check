---
otero_id: 562
otero_key: "9QC4NMQR"
title: "Mobile commerce integrated with RFID technology in a container depot"
authors: "E.W.T. Ngai; T.C.E. Cheng; S. Au; Kee-hung Lai"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2005.05.006"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Mobile commerce integrated with RFID technology in a container depot

E.W.T. Ngai <sup>a,\*</sup>, T.C.E. Cheng <sup>b</sup>, S. Au<sup>c</sup>, Kee-hung Lai <sup>b</sup>

<sup>a</sup> Department of Management and Marketing, The Hong Kong Polytechnic University, Hung Hom, Kowloon, Hong Kong <sup>b</sup> Department of Logistics, The Hong Kong Polytechnic University, Hung Hom, Kowloon, Hong Kong <sup>c</sup> Multi Base Ltd., Kowloon, Hong Kong

Available online 16 June 2005

## Abstract

In this paper, we present the findings of a case study on the development of a radio frequency identification (RFID) prototype system that is integrated with mobile commerce (m-commerce) in a container depot. A system architecture capable of integrating mobile commerce and RFID applications is proposed. The system architecture is examined and explained in the context of the case study. The aims of the system are to (i) keep track of the locations of stackers and containers, (ii) provide greater visibility of the operations data, and (iii) improve the control processes. The case study illustrates the benefits and advantages of using an RFID system, particularly its support of m-commerce activities in the container depot, and describes some of the most important problems and issues. Finally, several research issues and directions of RFID applications in container depots are presented and discussed. <sup>D</sup> 2005 Elsevier B.V. All rights reserved.

Keywords: M-commerce; RFID; Container depot; Case study

## 1. Introduction

Radio frequency identification (RFID) is an emerging technology that has been increasingly used in logistics and supply chain management (SCM) in recent years. RFID technology can identify, categorize, and manage the flow of goods and information throughout a supply chain. Basically, it is made up of two components: the transponder, which is located on the object to be identified, and the reader, which, depending upon the design and the technology used, may be a read or write/read device [1].

According to the International Data Corporation (IDC), the market for RFID technology in US retail supply chains will rise from \$91.5 million in 2003 to \$1.3 billion in 2008. (http://www.rfidjournal.com/ article/articleprint/733/-1/1/). The Freedonia Group, a research firm, estimated that through the year 2007, the total US market for smart labels will grow more than 23% annually, approaching 11 billion units and a value of \$460 million. Through 2007, RFID will be by far the fastest-growing smart label market segment, with an estimated growth of 180% annually from sales of around 10 million RFID labels in 2002 (http://www.rfidjournal.com/article/articleprint/ 712/-1/1/). By 2006, Insight forecasted that tagging will be well on its way to becoming commonplace within supply chains, including among smaller retailers and suppliers, with an expected tag price of 1 to 2 US cents. Insight Research expected that tagging at the item level to be widespread, virtually replacing bar coding and making the <sup>b</sup>Internet of Things<sup>Q</sup> a reality (http://www.rfidjournal.com/article/articleprint/ 675/-1/1/).

In general, the development of an RFID system is still relatively new to many organizations in Asia, in particular, in Hong Kong and China. With more and more organizations having a strong interest in RFID, RFID tools have assumed an important role in supporting logistics and supply chains. However, very little has been reported on how RFID systems for small–medium enterprises are designed and developed.

RFID is an emerging technology to support supply chains [7]. As the concept of RFID-based Supply Chain Management (SCM) evolves, systems that integrate the whole chain that provide instant visibility across the supply chain are likely to emerge. With the growing importance of logistics to the economies of Hong Kong and China, it is vital that local logistics companies come to grip with the issues concerning the adoption of RFID technology. They need to proactively raise their level of awareness of the strategic advantages of, and of their competence in, applying this disruptive technology.

In this paper, we describe the research and development of an RFID prototype system they integrates with mobile commerce (m-commerce) in a container depot to enhance its daily operations and support its location management. An RFID system integrated m-commerce architecture will first be introduced as a framework for research and the viability of the RFID integrated m-commerce framework will be tested in a container depot. This involves both business and technical aspects. Following the development of the framework, a case study is included to show how the framework can be applied in a container depot in Hong Kong. We will then discuss the benefits of m-commerce and RFID integration. We will see from this study that the innovative use of RFID technology can help a container depot gain competitive advantages through achieving better quality, greater visibility of data, and higher speed over competitors.

At present, the prototype system can track the containers and replaces the manual processes in the container depot. It is the real-time visibility of each container’s position in the container depot that enables the operator to process the container more quickly and efficiently. This helps increase the throughput and reduce operating expenses for the container depot operator and can help reduce the waiting time at the depot of third-party truckers seeking to pick up their containers.

## 2. Literature review

There have been few publications on RFID research and applications in academic journals. Karkkainen [3] discussed the potential of utilizing RFID technology to increase the efficiency in the supply chain for products with a short shelf life. He concluded that when applied to recyclable transport containers, investments in RFID can provide quick amortization of capital while offering a range of operational benefits. Kourouthanassis and Roussos [4] designed and implemented a prototype system catering to consumers on the move by using a wirelessly connected cart with a display device and an RFID sensor that detects the objects placed in the cart. They presented the results and implications of the front-end and formative evaluation studies they had conducted of the second-generation pervasive retail system. Ruff and Hession-Kunz [6] described the application of RFID systems to avoid collisions in metal/nonmetal mines. They conducted tests of the systems and subsequently developed a custom RFID system that can be used for both surface and underground mining equipment. Hengst and Sol [2] presented a framework that shows the direction in which inter-organizational structures of coordination will change under the impact of ecommence. They applied their framework to the container-transport industry for evaluation. We expect that its use will grow as applications of RFID increase.

This paper is organized as follows. In Section 2, details of a case study are presented as an example to illustrate RFID application in the real world. In Section 3, we show how the proposed system architecture, which is capable of integrating m-commerce and RFID applications, has been applied to support further m-commerce applications. Then, in Section 4, concluding remarks about the findings of the results, the lessons learned, future work, and the benefits of the approach are drawn.

## 3. Case study: a container depot

The case study company is a leading Hong Kongbased container depot that provides spaces to store empty shipping containers, container maintenance services, as well as container return and pickup services. It is located in Tin Shui Wai, occupies an area of 21,000 m<sup>2</sup>, and has a maximum storage capacity of about 32,000 twenty-foot equivalent units (TEU). The company provides major shipping lines and container leasing companies with container repair services. The company, which relies on a computer information system to process order requests to place and locate the containers, suffers from the following disadvantages:

i) Walkie-Talkie Limitation—inside the container depot, operators and stacker drivers communicate with one another via a Walkie-Talkie system. However, usually more than one driver in the depot wants to communicate with the operators in the control office to acquire information related to the containers. This will lead to air channel congestion.

ii) Container Misplacement—the drivers of the stackers have to access information on the containers and on the positions of the placement of the containers via the operators in the control office. This increases the chances of human errors in dealing with information on the containers.

iii) Ownership of Containers—the depot also faces the problem of not being able to determine the ownership of the containers. Though the containers usually have company logos on them, customers may sometimes exchange containers. This has led to the problem where workers in the depot are unable to determine the ownership of the containers.

iv) Dependence on Experienced Staff—as the operation of the container depot is not fully computerized, the container depot depends on experienced staff to determine the location of the containers. It takes a long time to train new staff. Should some experienced staff retire or resign, the normal operations of the depot would be seriously affected.

v) Inefficiency in the Search for Containers—it is sometimes very difficult to look for containers that meet the specifications of customers. As usual, whenever there is a pickup order, the stacker operators will have to look for the desired containers that are wanted. However, because they may have been misplaced, the containers may not be in the locations shown. In such a situation, it usually takes workers a long time to look for the containers in the depot and they may sometimes pick up other unwanted containers instead.

## 4. Research questions

A research question evidently arises from these disadvantages. Can information technology be used to improve this situation? What kinds of technologies would be most appropriately employed to tackle the problem? With these questions in mind, we propose a solution that can be integrated with the existing system. The proposed solution takes the form of RFID technology that is integrated with the existing system. The use of RFID technology is motivated by the following:

1) to keep track of the locations of stackers and containers in the depot,

2) to give greater visibility of the operations data,

3) to improve the business and control processes,

4) using the latest RFID technology can promote the technical advancement of the company in the industry and so it can act as a marketing tool for the company, and

5) an RFID system involves very little maintenance.

The major operations in the container depot are the return and pickup of containers and the maintenance operations. Operations reports that are requested are generated to customers via an electronic data interchange (EDI) system.

## 5. Architectural framework of an RFID technology integrated m-commerce system for a container depot

The architectural framework of RFID technology integrated with an m-commerce system consists of the following fundamental parts (Fig. 1).

## 5.1. RFID system

Basically, this system is made up of two components: the transponder, which is located on the object to be identified, and the reader, which, depending upon the design and the technology used, may be a read or write/read device [1]. RFID is based around radio or electromagnetic propagation. It has the ability to allow energy to penetrate certain goods and to read a tag that is not visible and is thereby able to identify those goods without scanning a barcode. Different frequencies of the radio system result in a system with different reading ranges and properties. The range within which the transponder can <sup>b</sup>talk<sup>Q</sup> with the interrogator depends on the size of the transponder and on whether the transponder has built-in power supplies [1].

![](/api/attachments/9QC4NMQR/fulltext/images/48998c3f4b7b147191cfe52418f45cddedaf0a7b596a9a4b7b464cc5b1f7a1d7.jpg)  
Fig. 1. The architecture of RFID integrated m-commerce.

## 5.1.1. System specifications

The system uses electronic product code (EPC) compliant Ultra High Frequency (UHF) (915 MHz) tags and readers from Thing Magic, as well as computer software developed in-house. RFID tags are attached to the containers and readers are installed in the stackers. A wireless LAN system is installed in the container depot, which allows the readers to communicate with the backend system. The developed computer system can be integrated with any RFID reader and tag with a reading range of 3–4 m.

## 5.2. Wireless network

A wireless local area network (WLAN) is one in which a mobile user can connect to a LAN through a wireless (radio) connection. A standard, IEEE 802.11, specifies the technologies for WLANs. The standard includes an encryption method—the Wired Equivalent Privacy algorithm.

In the container depot, apart from identifying the containers, the RFID prototype system also plays a role in positioning the containers in the depot. This involves tracking the containers and assigning a location for each container. To provide such functionalities, the exact location of each container must be known by the system. However, the traditional positioning system can only provide a near-exact location of the objects being tracked. Sophisticated software has to be designed and a huge investment will be incurred. However, with RFID technology, we can make use of reference points to determine the exact location of each object. A detailed algorithm for positioning the container is beyond the scope of this paper.

## 5.2.1. Integration of wireless LAN with RFID

The RFID readers are installed in the stackers. In order to transmit the information from the tags in real time, a wireless network between the RFID readers and the computer system is needed. Therefore, it is necessary to integrate WLAN and an RFID network. The RFID reader will have to interface with the WLAN with a TCP/IP protocol. Not all readers have the capability to provide this protocol stack. Therefore, the RFID may be interfaced with a mini-computer or mobile device that supports TCP/IP, as well as WLAN.

## 5.3. RFID integration with CDMSS

The Container Depot Management Support System (CDMSS) is a management support system designed to support the container depot using RFID and mcommerce technologies. The CDMSS is comprised of four modules: an account management module, a container management module, a transaction management module, and a monitoring and a data analysis module, which perform various kinds of decisionmaking and analyses of data.

## 5.3.1. Account management module

It handles customer and partner accounts and EDI profiles. Details of each customer and partner are stored in the system. Each member is assigned with an EDI profile. The information is used in other modules.

## 5.3.2. Container management module

To have better control of each container, the container management module provides the functionalities to keep track of the maintenance status of the containers. This lets the operators know exactly where the containers are. The stacking of containers is also managed under this module. Containers are tagged with RFID tags when they arrive at the container depot. The tag is attached to the container until it is checked out. The location of the container is then recognized in real time. Detailed information is then stored in the CDMSS database. The operators can also electronically mark the containers to indicate whether a container needs to be maintained.

## 5.3.3. Transaction management module

This module interacts intelligently with the container management module to assist in scheduling orders, recording transactions, and predicting costs/ profits. The system can also interface with the systems of customers/partners using EDI.

## 5.3.4. Monitoring and data analysis

As data accumulate, a data analysis can be conducted to evaluate the efficiency and cost of the operations of the container depot. The results are then fed back to the system to further improve the operations in the depot. At the same time, the depot is continuously monitored. In case of any improper operations due to human errors, the system will alert the operators of what problem has been found. Alarms can also be set to fit different situations in different container depots.

A sample of a user interface is shown in Fig. 2 for the container assignment function. A Booking Table menu (first menu choice in Fig. 2) provides the customer booking status for a container or for the owner of the container. A customer table menu is intended to provide on-line customers with the user information function related to his containers in the depot, user booking history, and so forth. The Position Object table provides all object information status in the depot. The Container Damage Form menu provides two functions including (i) real-time damage reports, with a repair cost estimation, and (ii) an online damage report viewer for customers. The map menu displays the Base Map of the Container Depot as shown in Fig. 3.

Fig. 3 shows an example of the resulting screen display of the base map of the container depot including job queue listings, a location map showing the real-time container depot status, i.e., the position of the container and the stacker. It allows users to search by type of container, company name, and current status of the container. Fig. 3 also displays the zone, row, and column of where the container is located, the process status of the container (pending, being maintained, stacked, etc.) as well as the electronic product code (EPC) of the container. The photo shows the corresponding photo of the container when the user clicks on the resulting search of a container in the search table.

## 5.4. The portals

The portals are the interfaces between the users and the system. The users can be either staff in the container depot or partners and customers of the container depot. There are two different kinds of portal in this framework: the Wireless Portal and the Web Portal. A Short Message Service (SMS) Gateway is added as an alternative to the portals as SMS is widely used and easily accessible. There are trade-offs among the three choices. The Web Portal, which provides more user-friendly interface and functionalities, is not available everywhere, while the SMS service, which provides the least userfriendly interface and functionalities, is available nearly everywhere.

![](/api/attachments/9QC4NMQR/fulltext/images/affbfb41aa8ea270081e944732852a826e7b6551bbb140221053f4eb2957bd8c.jpg)  
Fig. 2. User interface for CDMSS.

## 5.4.1. The Web Portal

The Web Portal allows all users to access different parts of the CDMSS via the Internet. Different users have different access rights. The Web Portal is a Javabased system, which makes use of Java Servlet technology to generate dynamic web pages and control the access for different users. Session management and a Secure Socket Layer (SSL) will be used for security. Java-2D and Java-3D technology will also be used to display information on the locations of containers in the container depot (see Fig. 4).

The Web Portal provides all of the functionalities available in the system. Sophisticated information can be displayed in the browsers. However, security is a greater concern, as the system is accessible via the Internet.

## 5.4.2. The Wireless Portal

The Wireless Portal allows staff in the container depot to access the CDMSS to obtain any needed information in real time. Unlike the Web Portal, staff can access the CDMSS anywhere in the container depot. With a mobile device and customized software, the operator can update or obtain the locations of the containers. Messages of alert can also be sent from the CDMSS to the operator.

The Wireless Portal is specially designed to display information in mobile devices with a screen of a limited size and browsers of limited functions. It can

Applet started.

![](/api/attachments/9QC4NMQR/fulltext/images/5cc47f6ca47778b6dfd42c1eb150d4d3a9c71968f490792f4687859f3e01d420.jpg)  
Fig. 3. A sample screen of the base map of the container depot.

only provide a subset of the functions provided by the Web Portal. In case the staff want to gain access to more detailed information or have a more userfriendly interface, they may switch to using the Web Portal.

As is shown in Fig. 4, users are able to:

i) display a map showing the current status of the containers in the depot including the locations of the containers and the movement of container stackers;

ii) create and display the holding-container profiles of the stackers; and

iii) save container profiles for future use.

A screen shot shows the container information as shown in Fig. 4 displaying the name of the container owner; the status of the container (e.g., waiting for repair, repaired, unserviceable, etc.); the dates on which the container entered the depot and will leave it; the target position of the container that needs to be dropped off at the correct location, which is generated by the CDMSS; and the current location of the container stacker in the depot. The operator clicks on the OK button to confirm that the target position of the container that needs to be dropped off at the correct location is the same as the current position of the stacker.

## 5.4.3. SMS Gateway

The SMS Gateway allows all the users to request information from the CDMSS. Users can send preset messages in their mobile phone to ask for different kinds of information. The SMS

![](/api/attachments/9QC4NMQR/fulltext/images/a7ce5630650b83c4834115b24c43db9833de918af95113bcab4791f2232cad8f.jpg)  
Fig. 4. A screen shot shows information about the container.

Gateway will then handle the request and reply with appropriate messages. Messages of alert can also be sent from the CDMSS to the users. The SMS Gateway only provides limited functionalities to the system because the SMS service is limited by being text-based. In case the staff want to gain access to more detailed information or have a more user-friendly interface, they may switch to using the Web Portal.

## 5.5. The key functionalities

## 5.5.1. Customer services

Based on the wireless network and the CDMSS, better customer services can be provided. The customers can obtain more accurate information on how many and what kinds of containers are available in the container depot. A scheduled return and pickup time is also accessible. The customers will also be informed once the containers they need are available. This saves the time needed to check the availability of the containers in different depots.

5.5.1.1. Requesting information. When customers plan to put the containers in the depot, they can ask for information on whether spaces are available in the container depot. With the system, the time needed to obtain the information can be shortened. Upon the return of their containers, customers can ask for information on the status of the containers, the types of containers available, and the number of containers in stock. This information is important in helping customers to plan the use of their containers. All of the information can be obtained via the portals and the SMS gateway.

5.5.1.2. Personalization. Customers and partners can subscribe to the different kinds of information they are interested in to enhance the planning of their use of containers. Certain customers may be interested in different kinds of statistics, such as what type of container is mostly used by other users of the container depot. Customers can also subscribe to receive related news and information on events. This gives vendors opportunities to promote their products and services. The user interface can also be personalized for the users.

5.5.1.3. Recommendations based on history. The system can also provide customers with recommendations on their plan to use and purchase different containers based on their usage history. In the case of certain types or brands of containers that are damaged most frequently, the system can suggest that customers use other types or brands of containers. The system can also keep track of what kinds of damage are usually found on the containers owned by that customer. This provides customers with valuable information to determine the cost of damage on the containers.

## 5.5.2. Order management

By accessing the Web Portal, registered customers can place their orders via the web. To pick up containers, the system will then look for the containers the customer needs and schedule a pickup time for them. For the returning of containers, the system will look for available spaces and schedule a return time. All payment transactions can be done via the Web. Customers can check their order status via the portal whenever they wish.

5.5.2.1. Registration. Customers or partners using this system will first register in the system. The customers or partners’ profiles will then be stored in the system. The profile will include the payment information required for future transactions.

5.5.2.2. Place order. Registered customers can place their orders via the portals. All order information will be transferred electronically. Once the system receives information, it will schedule the return or pickup based on the availability of spaces and containers. The system will then inform the customer of the scheduled time. If the customer is not satisfied with the scheduled time, he/she can queue for a better time, which the system will then try to schedule.

5.5.2.3. Payment transaction. Once the return or pickup is carried out, the system will automatically handle the payment transaction. With the advance in electronic payment systems, online transactions can be conducted securely and reliably. Both the customers and the container depot staff can check the transaction history via the system.

## 5.5.3. Container management

The tracking of a container within the container depot can be carried out via both the Wireless and Web Portal. With regard to the Wireless Portal, because mobile devices are limited in terms of screen size, memory, and processing power, only a textbased or 2D depot map can be shown. However, the user can still access useful information such as the location of a specific container, the number of containers available, the status of a specific container, and so forth. The same information is also accessible via the Web Portal, together with a 3D map of the container depot.

5.5.3.1. 2D/3D map. With the RFID integrated network, the system can construct a simulated map of the container depot with the exact position of each container. Via the Web Portal, the users can take a virtual tour of the container depot with 3D simulation. They can also locate the containers immediately. The status of that container can also be shown. Staff working inside the depot can also obtain a 2D map from their mobile devices. Once they receive a task to relocate some containers, they can locate the exact locations of the containers and follow the guidelines from the mobile device to relocate the containers.

5.5.3.2. Tracking. The system tracks and stores all of the information about the containers in the depot. Users can search for different information in the system via the search engine. Apart from the locations and the status of the containers, users can also obtain the history of the containers. For example, a user can obtain the maintenance history of the container. All such details as the date of maintenance, damaged parts, cost of maintenance, and so forth can be made available. The location history is also stored so that the user will know how many times the container has been relocated, and the positions before and after each relocation.

5.5.3.3. Security. As all order information is stored in the system and all the containers are tagged, cases of customer getting the wrong containers can be prevented. It is also much more difficult to forge an order.

5.5.3.4. Container identification. In the container depot, all of the containers will be tagged once they are returned. Detailed information on that container will also be stored in the system database. The information in the database will then be linked with the tag. Therefore, all of the containers can be identified by the tags. As many customers will use the same brand of container, or may have exchanged their containers, there will always be such mistakes as company A’s containers being checked out by company B. However, with the RFID tags, all the containers can be identified easily via the Web or Wireless Portal.

5.5.3.5. Order verification. As all the orders will be processed by the system, whenever orders and transactions are carried out, a notification will be sent to all the parties involved. This ensures that the order that is made is correct and not forged, thus reducing the chances of containers being stolen or checked-out by wrong parties. This kind of notification is available on the Web Portal, Wireless Portal, and the SMS service.

## 5.5.4. Real-time alert and notification

Real time alert and monitoring is available via the Web Portal, Wireless Portal, and SMS service. This allows users to keep track of any changes in the container depot and of any orders or transactions being made.

5.5.4.1. Container information notification. Customers will usually be interested in the stock information of the type of container they usually use. They can register to receive an alert if a certain number of such containers are available, or if the number of available containers drops below a threshold level. They can also register to receive a notification when the maintenance of their containers has been completed. A notification can also be sent when their containers leave or arrive at the container depot.

5.5.4.2. Order and transaction notification. Another aspect of information that customers will be interested in is information on schedules, orders, and transactions. Customers can register to receive notification whenever orders or transactions are made. This prevents the making of incorrect or forged orders. Whenever there is any update on the schedule, customers will be informed immediately. SMS messages can be sent to the drivers as well.

## 6. Decision support

The RFID integrated m-commerce framework discussed above provides a great deal of valuable real time data such as information on the location of a container and the transactions related to it. The data are gathered and stored in the data analysis module of the CDMSS for data mining. We can make use of the data to extract business information that enables better decision-making. Using Online Analytical Processing (OLAP), with RFID technology and OLAP technology, instant decisions can be made based on the data collected from the RFID integrated m-commerce framework. Different popular data mining techniques such as Discriminant Analysis (DA), Decision Trees (DT), and Artificial Neural Networks (ANNs) can be applied in the framework to enhance the data analysis process.

Traditionally, container depots have depended on operators to decide where the containers should be put and located. The quality of customer services also depends on the experience of the operators. Even if computer systems are installed, data are only stored for future reference and no instant decision support can be given. With the decision support from the framework, better risk management can be achieved. In the container depot, based on the movement of the containers, transactions made, and customer behaviour, different predictions can be made to enhance the operations of the depot and customer services.

## 6.1. Predicting customer needs

Based on the transaction history and the behaviour of the customers under different conditions, we can always guess what they need now or even in the future. However, there are usually thousands of customers for large container depots. The operators will not be able to accurately guess the needs of each customer. In order to provide better services for customers, it is necessary to perform a better data analysis for each customer. We can predict when they will return or pick up containers, how many of each type of containers will be needed during different shipment periods, what kinds of information they are most interested in, and so forth. Different kinds of advice can then be given to the depot operators to better serve the customers. At the same time, customized reports and recommendations can be given to the customers as a value-added service.

## 6.2. Predicting container usage

A shortage of containers is usually the problem faced by a depot and its customers. If the depot cannot provide enough containers for customers, the customers will usually rent containers from other container depots, thus resulting in a loss of customers and a drop in revenues for the depot. Being able to predict container usage in different periods of time allows a container depot to provide the best customer services and to make all kinds of containers available to customers at all times. Container usage can be predicted by transaction history and related events. Once it is predicted that there will be a shortage, the container depot can request more containers from its suppliers.

## 6.3. Assigning the location of a container

Assigning the best locations to containers has always been a difficult task for a container depot. The operators can only assign a location based on their experience. Wrong decisions are usually made, necessitating the relocation of containers, thus wasting manpower and fuel required by the operation car. Assigning locations to containers is a very complicated task. Many factors affect the choice of the best location: the space available in the depot, where the entrance and exit are located, pending container return and pickup orders, estimations of future container usage, the maintenance status of other containers being repaired, the container stocks in the depot, and so forth. Being able to determine where to store the containers in the best way can lead to reductions in the cost of fuel and in manpower, and especially shorten the lead time needed for container pickups, about which customers are always concerned.

## 7. Issues arising in the implementation of RFID systems

Although the implementation of an RFID system is an advantageous move for container depots, there are issues that need to be further addressed. Because the container depot business involves different parties from container manufacturers and suppliers to maintenance contractors and users, it is possible that the entire industry is not technologically advanced enough to incorporate RFID. The major issues of implementation are described below.

## 7.1. Technical issues

i) Material matters: For the implementation of RFID in container depots, the shipping containers are metals which reflect radio wave. Water absorbs radio waves so it is difficult for RFID to track products with a high water content, or that are in metal. The performance of the system will be adversely affected by both factors. A careful design in placing the tags is required to overcome this limitation.

ii) Electromagnetic interference: Onsite testing must be carried out carefully if multiple sources of electromagnetic interference (EMI) are to be found, such as other readers, other tags, wireless LANs, and data transmission systems.

## 7.2. Behavioural issues

i) Resistance to change: The implementation of information systems is affected by the way people perceive these systems and how people behave. RFID systems are no exception. Resistance to change is another important issue. It is a major behavioural factor that can have a significant impact on the implementation of RFID systems.

ii) Organizational expectations: Over the past 2 years, RFID has gained tremendous publicity. The general level of expectations regarding the system held both by top management and users may now be too high. Over-expectations can be dangerous to the success of an RFID system.

## 7.3. Cultural issues

People may not have confidence in the RFID system because it is relatively new to them. It may take them a long time to understand and trust the technology.

## 7.4. Business process issues

As is the case with most breakthrough technologies in container depots, implementing RFID can require the fundamental redesigning of business processes if optimal benefits from using RFID are to be obtained.

## 7.5. Security issues

RFID could make possible an omnipresent state of surveillance. The security and integrity of information and the privacy of consumers are always primary issues surrounding the adoption of RFID.

## 7.6. Code conversion issues

There is lack of standardization on codes. Some may use ISO or EPC standards. Code conversion may be required for implementation.

## 7.7. Data management issues

RFID systems capture and deal with enormous volumes of data. We need to filter out the useless data, identify what needs to be stored, and consider how and where to store data.

## 8. Concluding remarks and future research

Most container companies do the planning and locating of containers manually based on their experience. There are no RFID-based decision support systems that support planning and location management. There has been little work done on this subject. The majority of the published work on container scheduling is theoretical, with a focus on designing optimization algorithms. Few real RFID-based applications have been reported, especially in Asia.

The goal of using RFID in container depots is to enhance efficiency, thus providing better customer services while lowering the cost of operations. While most container depots are moving towards adopting mobile technologies, implementing RFID integrated systems will enable them to realize true, real-time tracking of containers.

Wireless technologies are changing the way businesses serve their customers. This has now evolved as m-commerce. With RFID technology, m-commerce can be enhanced to a fully automated process. We have seen the blending of existing m-commerce technology with RFID, a layering over existing infrastructure to provide additional functionality in applications that require this.

1) With the RFID-based system, the drivers can access the system anywhere inside the container depot via handheld devices. Information on the containers will be updated and sent to the system via a wireless system to the backend computer system. This reduces human errors, and drivers no longer have to wait for the system computer operator in the depot control office to become available.

2) The system can determine where to put the containers based on developed algorithms and prescheduled orders. The system can inform workers where to put and get the containers. The time needed to train new staff is shortened. Dependence on the experience of staff to pick up and deal with the containers is greatly reduced.

3) All of the containers are identified by RFID tags. Workers can access detailed information about the containers easily via their handheld devices. The system can inform the workers where the containers of the customers are located. In case mismatch containers are found, an alert can be sent to the operators.

Any misplacement of containers can be detected by the system in real time and the system will inform the drivers to correct the problem. Chances of mistakes made by computer operators are reduced. The drivers will also immediately know about any misplacements as indicated by the system.

The system enables the RFID system to keep track of the location of a truck and container. Based on the information sent from tags attached to the floor and the container, a PC in the operator’s cab wirelessly receives confirmation of the container that needs to be dropped off at the correct location. The wireless PC can then direct the operator to a specific location in the depot at which to place the container and, later on, where to quickly find the container when it needs to be retrieved.

This paper describes the research and development of an RFID-based prototype system for supporting a local container depot to reduce container handling errors and enhance operational efficiency. A system architecture is proposed to integrate RFID with mcommerce technology of the management support container system. The framework is examined and explained in the context of a case study. The system features wireless, real-time applications for locating, tracking, and managing all of the containers stacked in the depot. The system enables the company to achieve a new level of efficiency for the movement of containers in the depot. Essentially, just about anything that moves throughout a depot can be tagged and tracked in real time.

There is a significant advantage in deploying RFID in the container depot. Staff members in the container depot know the exact location of each container in real time. Whenever containers are misplaced, alerts will be given both to the driver of the stacker and to the container control office.

Since the development of such a system can require significant resources, it is important to understand and document their benefits. At present, the RFID system reported in this study yields a number of advantages:

i) Container utilization—integrating with RFID allows container depot companies to save a huge amount in operating costs annually by identifying inefficiencies in their daily operations and allowing them to easily and automatically manage and locate their containers. It also enables the automation of processes such as the tracking and monitoring of the containers, resulting in a reduction in labour.

ii) Operational efficiency—the RFID technologies will provide even greater visibility to operations data. The misplacement of containers will be eliminated. Labour-intensive processes such as data capture, yard control, and continue return and pickup will all be controlled by the technologies. Container depot companies will be able to quickly locate a container and accelerate the entire pickup process so that the number of returns and pickups per day can be increased.

iii) Quality control and customer services—data on the container stored can be used to alert operators of potential mismatching of orders. Human mistakes can be tracked in real time and alerts will be sent to the operators. Corrective actions can then be taken. The automated capturing of data also enhances data analysis. Therefore, inefficiencies can be identified and eliminated before any mistakes are made. The RFID integrated network streamlines the return and pickup processes, making them more efficient. Such commitment-articulation and commitmenttracking processes provide greater visibility to the operations data trust [5].

iv) Reduced return and pickup lead-times and costs—an RFID integrated wireless network can significantly improve the container return and pickup processes. Waiting times for trucks can be reduced. This results in the ability to increase the capability with existing assets and labour.

v) Improved service quality and profitability—as real-time and more accurate information is obtained, container depots can provide customers and partners with information about the status of containers via web-based information systems. In addition, by tagging containers with RFID tags, the types of containers that are not being used or that are frequently in shortage can be identified easily. The container depot can then start renting out the types of containers of which there are shortages.

We believe that RFID is an emerging important technology that may co-exist with bar codes for years to come. The lessons learned from carrying out this project are summarized as follows:

i) There is a need to calculate deployment costs and estimate the business risks and value of adopting an RFID system to satisfy customer demands before implementing the system.

ii) It is necessary to carry out a detailed survey of RFID systems before deciding on what type of RFID technology to adopt so that the technology can be harnessed to yield satisfactory results.

iii) There is a need to be aware that implementing an RFID system is not just an IT issue. Rather, it involves behavioural issues and issues of organizational culture, although most organizations view the adoption of RFID as strictly an IT issue.

iv) It is necessary to have a very detailed solution analysis from the selection of tags to the locations of the readers to integrate the RFID system with the existing system. Every implementation requires a detailed solution analysis.

v) There is a need to narrow down the scope for the adoption of an RFID system, because such a system is still too expensive for organizations to fully implement. It is advised that the implementation be carried out in phases.

vi) It is necessary to be aware that even WLAN and RFID-based systems can support applications requiring indoor location management. Many of the proposed outdoor schemes will encounter problems in performing in an outdoor environment due to triangulation difficulties caused by weak signer signals and line of sight requirements.

vii) It is necessary to let people, particularly senior management, know that RFID is not a magical technology allowing everything to happen automatically once tags and readers are installed. Over-expectations can lead to disappointments and to the termination of the innovation that is adopted.

We are interested in the following areas and propose them as subjects for further research.

1) At present, the company has two container depots, one in Hong Kong and one on the adjacent side of the border in Shekou, Shenzhen, mainland China. It has been considering integrating the two sites to improve communication, although the sites are physically separated by the sea. As far as location is concerned, this is close enough to establish a wireless connection. Connection by using leased lines is a more feasible solution, but the cost is higher. However, regulations concerning cross-border communications are usually very strict, and it is difficult to apply for licenses. We are exploring the possibility of extending the RFID system to the Shekou depot using a wireless system. The crossborder integration of the two systems could be an interesting topic of study.

2) At present, RFID applications have been mostly closed systems within the boundaries of a company’s operations. As RFID tags are added to the containers, the containers can be tracked throughout the whole supply chain. In order to realize RFID integrated supply chain management, the whole industry will have to adopt a set of open standards so that the systems can collaborate with other part ners along the supply chain. Electronic product code (EPC) technology is a possible solution.

3) Other areas for further research include examining suitable models for the adoption of RFID in organizations and investigating the managerial and business implications of adopting RFID technology in an organization.

4) A further concern is the integration of RFID technology with the existing legacy system that provides the core and primitive functions to operate the container depot, such as the repair estimate system, which examines, validates, and records the estimates for repairing each damaged container, and controls the repair workflow cycle with the agreement of the parties involved.

6) Finally, we will explore the integration of an advanced depot business module with such things as the multi-interface EDI engine, which supports those derived EDI specifications based on different coding specifications with the multi-interface EDI engine.

## Acknowledgements

This research was supported in part by The Hong Kong Polytechnic University under a research grant from the Area of Strategic Development in China Business Services–<sup>b</sup>IT for Logistics Management and Maritime Studies (grant number A632).<sup>Q</sup> The authors are grateful for the constructive comments of the referees on earlier versions of this paper and appreciate the support from Container System Ltd. and help from Mr. Y.S. Choi, Mr. K.Y. Sin and Mr. Y.F. Chai in this research.

## References

[1] K. Finkenzeller, RFID Handbook Radio-Frequency Identification Fundamentals and Applications, John Wiley & Sons, Ltd., England, 2003.

[2] M.D. Hengst, H.G. Sol, The impact of electronic commerce on interorganizational coordination: a framework from theory applied to the container-transport, International Journal of Electronic Commerce 6 (4) (2002) 73–91.

[3] M. Karkkainen, Increasing efficiency in the supply chain for short life goods using RFID tagging, International Journal of Retail & Distribution Management 31 (10) (2003) 529-536.

[4] P. Kourouthanassis, G. Roussos, Developing consumer-friendly pervasive retail systems, IEEE Pervasive Computing 2 (2) (2003) 32– 39.

[5] K. Kuldeep, Technology for supporting supply chain management, Communications of the ACM 44 (6) (2001) 58– 61.

[6] T.M. Ruff, D. Hession-Kunz, Application of radio-frequency identification systems to collision avoidance in metal/nonmetal mines, IEEE Transactions on Industry Applications 37 (1) (2001) 112– 116.

[7] N. Singh, Emerging technology to support supply chain management, Communications of the ACM 46 (9) (2003) 243– 247.

![](/api/attachments/9QC4NMQR/fulltext/images/98b3edd630c85f2ac500b178cfe58b6c20c58f814f20a5fabe541dd94d8491a3.jpg)

Dr. Eric W. T. Ngai is currently an Associate Professor in the Department of Management and Marketing at The Hong Kong Polytechnic University. His current research interests are in the areas of elec tronic commerce, decision support systems and e-supply chain management. He has published in a number of journals includ ing IEEE Transactions on Systems, Man and Cybernetics, Information and Man agement, Expert Systems, Expert Systems

and Applications, International Journal of Operations and Production Management, Omega, Transportation Research and others. He serves as an associate editor for the International Journal of Enterprise Information Systems and on the Editorial Board of International Journal of Production Research. Dr Eric Ngai has received the Faculty Award for Outstanding Performance/Achievement in Teaching (2003–2004).

![](/api/attachments/9QC4NMQR/fulltext/images/a4d75a3adcdee013c618aabdab7e1737b4f0e4d55e54db0ee1f6187b6356331a.jpg)

Prof. T.C. Edwin Cheng is Chair Professor of Management in the Department of Logistics of The Hong Kong Polytechnic University. He obtained his bachelor’s, master’s and PhD degree from the Universities of Hong Kong, Birmingham, and Cambridge, respectively. Prof. Cheng’s research interests are in Operations Management and Operations Research. He has published over 250 journal papers and co-authored two books. He received the Outstanding

Young Engineer of the Year Award of the Institute of Industrial Engineers, U.S.A., in 1992, and the Croucher Senior Research Fellowship (the top Science award in Hong Kong) in 2001. He was named one of the <sup>b</sup>most cited scientists<sup>Q</sup> in Engineering over the period 1994–2004 by the ISI Web of Knowledge in 2004.

![](/api/attachments/9QC4NMQR/fulltext/images/e3f9646a5d3baf660f8318d8af2632aac9aa0da698373e2a1652b14cc83e9f60.jpg)  
Sherlock Au is the director of Multi Base Ltd. His research interests include artificial intelligence, intelligent agents, and applications of AI. Au received a PhD in computer science from the University of New South Wales, Australia. Contact him at sherlock@ multibase.com.hk.

![](/api/attachments/9QC4NMQR/fulltext/images/396595a8b188975fcd6e9ceef9d7f6ce85b569f9794324dcaf3dfaa2a26f7de0.jpg)  
Kee-hung Lai is an Assistant Professor, specialized in logistics and operations management, in the Department of Logistics, The Hong Kong Polytechnic University. He received his PhD in business from the same university. His research papers have appeared in academic journals such as International Journal of Production Economics, Journal of Business Research, Omega, and Transportation Research.
