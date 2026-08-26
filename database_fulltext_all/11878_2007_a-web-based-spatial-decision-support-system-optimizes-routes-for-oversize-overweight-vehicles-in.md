---
otero_id: 11878
otero_key: "JW9J86MS"
title: "A web-based spatial decision support system optimizes routes for oversize/overweight vehicles in Delaware"
authors: "Julian J. Ray"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2005.07.007"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A web-based spatial decision support system optimizes routes for oversize/overweight vehicles in Delaware

Julian J. Ray

University of Redlands, School of Business, Redlands, CA, United States

Available online 15 August 2005

## Abstract

Delaware Department of Transportation has developed a web-based spatial decision support system for managing the movement of oversize and overweight vehicles over the State’s highways. This system combines network optimization techniques and a J2EE web-architecture to provide a robust, high-performance and scalable system meeting Delaware’s current and future permit processing needs. The new system replaces existing manual processes, providing a number of immediate and future benefits including reducing time to calculate some permits from weeks to seconds, reducing processing costs and providing potential safety benefits by reacting to rapidly changing highway conditions. <sup>D</sup> 2005 Published by Elsevier B.V.

Keywords: Spatial decision support systems; Web-based DSS; Vehicle routing; GIS; J2EE

## 1. Introduction

Vehicles and vehicle combinations exceeding maximum allowable height, length or weight limits are considered oversize or overweight (OS/OW) and require permits issued by State Transportation Agencies to traverse the nation’s highways. These permits seek to manage the movement of OS/OW vehicles by restricting them to specific routes capable of supporting their physical size and weight characteristics, limiting potential damage to roads and bridges and avoiding increasing congestion in already congested areas [32].

While each State is free to define their own permit rules, general permitting procedures remain the same. An OS/OW vehicle operator wishing to travel through a particular State applies for a permit well in advance of traveling, providing the vehicle’s physical characteristics including gross weight, height, length, width and axle configuration and a date on which the trip will occur. Permit applications often include a proposed route to be taken by the permit-vehicle through the State’s highway system. Each State Department of Transportation (DOT) is responsible for ensuring that all highways, bridges and other structures along the length of a proposed permit route can accommodate the physical size and weight characteristics of the permit vehicle. If a potential problem with a proposed route is identified, a new route which can support the vehicle is proposed by the DOT. Once a viable route has been determined, a permit is issued which allows the permit vehicle to legally traverse the permit route on the specified day.

Traditional methods for generating and validating vehicle permit routes are manual and thus labor intensive. Permit routes are usually traced by hand over paper or computer-generated maps. Bridges and other way-side structures such as gantries, toll-booths and road signs which might cause an obstruction or otherwise be damaged by a vehicle as it passes are identified and checked against engineering diagrams to ensure adequate clearance. Additionally, detailed structural analyses of bridges are performed to ensure that all bridges along the permit route can support the gross weight and axle-load characteristics of the permit-vehicle. In an effort to reduce costs, several DOTs have recently sought to develop spatial decision support systems (SDSSs) to automate validation of permit routes and generation of alternative routings when necessary.

This article describes the design and development of a permit routing SDSS developed for Delaware DOT (DelDOT). Unlike existing permit routing SDSSs developed on top of single-user Geographic Information Systems (GISs), this system uses a webarchitecture and the application is hosted on DelDOTs Intranet as a decision module within a statewide Integrated Transportation Management System (ITMS). Several design issues had to be overcome in order to achieve this integration. First, a new web-friendly permit routing algorithm capable of efficiently validating and generating concurrent permit routes on a server had to be developed because existing algorithms designed for single-user systems would cause unacceptable processing loads. Part of the algorithm design required developing a strategy for making most effective use of a third-party software component for which there were limited licenses available. Next, a set of web-based SDSS components had to be designed and developed to implement the new algorithm. The development of web-based SDSSs, and transportation SDSS in particular, is a relatively new field of research and presents several challenges for system designers. These challenges are identified and discussed later in this paper. Last, the permit routing application has to interoperate with other ITMShosted systems and share business logic and data within the ITMS framework. These interoperability requirements shaped final system design, forcing the development of a number of SDSS components which can operate independently but also collaborate to solve complex permit routing problems.

In the next section of the article SDSSs and permit routing are described. This is followed by a review of existing permit processing activities at Delaware DOT and a description of the new permit routing application and its implementation as a series of Enterprise Java web components. The final sections discuss the immediate and future benefits afforded by the new system and compare this system, implemented using a J2EE platform, with generic web-based DSSs.

## 2. SDSS and permit routing background

Creating and validating permit routes is inherently a spatial problem involving many facets of transportation-oriented GIS. Indeed, all primary decision components in the permit routing problem contain a spatial dimension. The origins and destinations for permit vehicles are described using street addresses, Interstate mile markers, street intersections or well known locations such as <sup>b</sup>Dover Air Force Base<sup>Q</sup>. These locations have to be validated and geocoded by a GIS before they can be used. The locations of bridges and other structures of interest, such as tollbooths, road signs and gantries, are stored as spatial features in a spatial data base and maintained by a GIS. Highway assets and their characteristics are stored as a spatial features in a spatial database and maintained by a GIS and external factors affecting permit routing including locations of highway maintenance, congestion, accidents and lane closures are described using spatial references which are also located using a GIS.

Generating vehicle routes requires access to sophisticated spatial data management sub-systems, network optimization procedures and specialized geo-processing functions such as address geocoding. GISs traditionally provide these functions as resourceintensive desktop systems using proprietary spatial data storage formats and specialized data management systems. Spatial Decision Support Systems (SDSS) combine traditional GIS functions with database storage technologies and decision modeling tools, allowing decision makers to solve complex spatial problems such as site selection and vehicle routing [27]. These systems are shown to increase the quality of decision making in certain circumstances [17] and be effective tools for strategic planning and risk management, especially by government agencies [13].

The combination of DSS and GIS functions provides a natural platform for vehicle routing DSSs as they synthesize the advantages of traditional routing methods with spatial tools provided by GISs, including the ability to manage large volumes of spatial data and provide visual feedback in the form of maps [14]. Many examples of vehicle routing SDSSs are available in the literature including dispatch and delivery systems [30], car-pooling [15], snow removal [5] and ship scheduling [7] among others. These systems generally fall into the category of Model-Driven DSS where core routing problems are formalized and solved using optimization and other quantitative models [20].

Web-based SDSSs, where all decision support related operations are performed on a network server, first appeared in the literature in 1996. Rinner [22] suggests that web-based SDSSs are primarily motivated by a need to better support group decision making. However, additional advantages have also been identified including platform independence, shorter learning curves for users already familiar with web tools and web navigation, lower software distribution costs and ease of performing system updates [27]. This movement of SDSSs to web-platforms is part of a more general DSS trend. The movement of decision support applications to Internet servers is a recent trend allowing traditional optimization, forecasting and quantitative models to be distributed more widely [20]. Access to Internet-based DSS resources is through ubiquitous thin-clients such as Internet browsers. Bhargava and Power [4] identify web-based systems as the <sup>b</sup>platform of choice<sup>Q</sup> for delivering decision support today, although the authors identify several technical, economic and social challenges which have yet to be overcome to fully realize the benefits of web-based DSS platforms.

While a few companies such as Microsoft with their MapPoint.NET product have resolved some of the economic and technical challenges for web-based vehi cle routing SDSSs, the majority of commercially available vehicle routing SDSSs still use traditional thickclient or client–server architectures. In a recent survey of vehicle-routing DSS companies, Hall [12] identifies only 9 of 24 surveyed companies providing web-based interfaces for their products, due in part, perhaps, to the technical challenges of system interaction and data management associated with building web-based DSSs as well as the economic challenges of sustaining viable payment models identified previously.

With respect to SDSSs in general, technical rather than economic or social challenges appear to predominate in the literature. Green and Bossomaier [11] note that most web-based SDSS are either simple spatial query systems or map-building programs, while access to more resource and data intensive GIS functions such as spatial analyses is limited. The authors attribute this lack of development to the technical challenges of managing the transfer of large volumes of spatial data between sites as well as managing spatial data which is being used, created or changed by multiple users in a stateless web-based system. Another factor limiting the adoption of webbased transportation oriented GIS is the availability of network algorithms designed to exploit the computing resources and bandwidth characteristics of computer networks [28]. These tools are costly to develop and also introduce many technical problems associated with data management, algorithm development and user-interface design.

Although several vehicle-routing SDSSs are commercially available, these systems either solve generic minimum cost network problems or are highly specialized for use within particular industries such as garbage and snow removal [12,18]. These generic tools are unable to create permit routes directly as they cannot process constraints representing vehicle/edge combinations constrained by height, weight and width characteristics of structures aligned sequentially along the length of each highway segment. These constraining dimensions create a set of monotonically non-increasing step-wise functions of distance over each highway segment. This concept is illustrated in Fig. 1.

Highway segment $x _ { i j }$ in Fig. 1 is successively constrained in dimension h by structures located at positions $B _ { 1 } , \ B _ { 2 } , . . . . , B _ { n }$ along its length. The minimum overall constraining value for $x _ { i j }$ is found at $h ( x _ { i j } )$ . The permit routing optimization problem can be stated as finding a minimum cost path, $P ,$ between an origin node and a destination node in the network where $\begin{array} { r } { H _ { \nu } { \leq } \operatorname* { m i n } _ { x _ { i j } : ( i . j ) \in P } h \left( x _ { i j } \right) } \end{array}$ where $H _ { \nu }$ is the corresponding maximum dimension of vehicle v. This general problem, called the constrained bottleneck path problem, has been previously addressed in the context of transportation networks [2]. More recently, the problem has re-appeared in the literature as a means of finding guaranteed bandwidth in computer networks for high-bandwidth applications such as streaming video [16].

![](/api/attachments/JW9J86MS/fulltext/images/1f053fbe863e6958536e52f837cef3f82c0145402adb04229c52110efd5854f0.jpg)  
Fig. 1. Constraining dimension over a highway segment.

One method for solving the constrained bottleneck path problem is to pre-process the network, determining the set of edges which fail to meet minimum service criteria and removing them from the problem. A minimum cost path through the remaining edges, if one exists, can be shown to be optimal with respect to the full network. This approach is advantageous as, once pre-processed, the problem reduces to a simple minimum cost path algorithm which can be solved using commercial SDSS network solvers and is the method used by existing permit routing systems [19,32]. Other approaches to solving the generic constrained bottleneck path problem have also been reported including parametric algorithms [2] and labeling methods [6].

## 3. Existing permit processing at Delaware DOT

Vehicles planning to travel through Delaware which exceed allowable size and weight limits are required to purchase a permit from DelDOT prior to travel. Each year DelDOT receives over 50,000 requests for vehicle permits by telephone, mail and more recently via their Oversize/Overweight Permitting System (OOPS) [24]. OOPS is a publicly available web-based user-interface enabling vehicle operators to apply for permits over the Internet and pay for them by credit card [25]. OOPS was developed internally by DelDOT as part of ITMS and is the primary user interface for recording permit applications, replacing paper permit applications with webforms which are completed and submitted over the Internet. Permit requests received by mail and phone are entered into OOPS by DelDOT employees.

The OOPS application collects a variety of information from permit applicants including the time and date for proposed trips, origin and destination locations, vehicle identification information, physical dimensions of permit vehicles and vehicle axle configurations. Axle configurations describe the number of axle groups on a permit vehicle, distances between axle groups, number of axles in each axle group and distribution of gross vehicle weight over each axle group and are used to calculate load-stresses on bridges using specialized commercial bridge analysis software. Starting and ending locations for each trip are specified as street addresses, names of particular businesses or identifiable organizations within the State (e.g., Dover Air Force Base) or Interstate mile-markers.

The first version of OOPS collected information from permit applications and stored it in a relational database. DelDOT staff would extract permit requests from the permit database and manually validate permit routes against pre-generated paper maps, engineering information and bridge reports. Once validated and paid for, a permit describing the route and vehicle would be mailed to the vehicle operator (Fig. 2).

The complexity of the permit route validation process and related labor costs often delay permit processing. Indeed, using the manual validation system, permit applications for some vehicles could take as long as 2 weeks before a permit could be issued [23]. Normal annual increases in permit traffic only exacerbate these problems, leading DelDOT to identify several areas where existing permitting processes failed to meet organizational goals: paper maps, engineering reports and bridge reports could be up to 2 years old and contain missing or incomplete information, creating potential safety issues; delays in generating permits result in poor customer service as vehicle operators have to plan permit routes well in advance; permit processing methods cannot react to rapidly changing highway conditions which could affect route choice, bridges damaged by accidents or extreme weather, for example, present potential safety concerns; normal annual increases in permit traffic along with State and Federal policy changes generally increases the numbers of vehicles requiring permits, exacerbating burdens on DelDOT’s already constrained human resources, and permits fees are between US\$10 and US\$30. These fees do not cover actual processing costs, leading to a significant and increasing cost burden on the agency.

![](/api/attachments/JW9J86MS/fulltext/images/5fca5ea70d28bd188ea7d4e5d15bb19464ca038666447d71ef955acbdf0c8c81.jpg)  
Fig. 2. Permit processing at DelDOT.

A first attempt to automate permit-validation and routing was started in 1997 [21]. A traditional thickclient based SDSS using Visual Basic and a commercial GIS platform from Intergraph Corp. was designed. This system would have replaced the manual validation process in Fig. 2 by automatically extracting permit requests from the permit database and validating each permit route, suggesting alternative routings when proposed routes failed. The work, however, was eventually abandoned for a number of technical reasons [23]. Part of the decision to abandon this work was based on the realization that when completed, the thick-client SDSS permit routing system could not integrate with the ITMS web-platform or share data across other ITMS applications and would, therefore, immediately create legacy issues even though the system was new [21].

## 4. DelDOT’s web-based permit routing system

Specifications for a new permit routing system were created by DelDOT in early 2000. The new permit routing system would be hosted within ITMS so that it can share permit application data in real-time with a new version of OOPS, providing an end-to-end automated permit processing platform. This new system would enable vehicle operators to apply for and receive validated permits over the Internet during a single session.

## 4.1. ITMS architecture

ITMS provides user-access to all DelDOT transportation management information systems through a common web browser interface. ITMS is hosted on DelDOTs Intranet at a central location and connected via a high-speed network to the various Delaware departments and organizations requiring access. At the heart of ITMS is a single Oracle database storing transportation data collected from all ITMS management systems including real-time data from DelDOT’s traffic control systems [31] as well as spatial data necessary for supporting ITMS’s various SDSSs.

Within ITMS, applications share data using Extensible Markup Language (XML) and access the common data storage system through a set of shared resources (Fig. 3). Applications hosted in ITMS have access to all available real-time and historical transportation data within the enterprise as well as shared business logic from other ITMS applications. ITMS initially included OOPS and electronic payment systems. Weather monitoring systems, transit management systems and location mapping systems are planned for future inclusion into the system.

## 4.2. Solution design

The first challenge for the project was to develop an approach for validating and creating permit routes which could work efficiently within the ITMS platform. The pre-processing strategy described previously is technically easy to implement and the resulting path problem can be solved using generic transportation GIS functions which has distinct advantages as a commercial vehicle routing SDSS could be used to solve the resultant optimization problem. This approach, however, is not tractable for use within ITMS, or web-based platforms in general, as weight limits, $h ( x _ { i j } )$ , for each edge are dependent on vehiclespecific axle configurations. Evaluating $h ( x _ { i j } )$ for each edge in the network requires performing a resourceintensive structural analysis for each vehicle/bridge combination using third-party bridge analysis software. There are approximately 2500 bridge structures on the DelDOT network and pre-evaluating $h ( x _ { i j } )$ for each edge would take approximately 1 h to compute on the server. This algorithm also exhibits worst-case performance when a vehicle is unrestricted, that is, the network is unconstrained with respect to the dimensions of the current vehicle. An analysis of historical permit routes indicated that approximately 97% of permit routes processed by DelDOT fall into this worst-case category.

![](/api/attachments/JW9J86MS/fulltext/images/69c1b12610942090ac042b0eafb1f4c413f8ed83f4ebc12eddc30e94630fb6ea.jpg)  
Fig. 3. ITMS conceptual architecture.

Implementing this algorithm in ITMS would have several negative system-wide impacts: the amount of data processing necessary to solve a single permit routing problem would require dedicated servers within ITMS or otherwise draw processing resources from other ITMS applications affecting their usability; limited available licenses for the third-party bridge analysis software restricts the number of permit routes that can be solved concurrently; and it would take over an hour to process each permit route resulting in poor system performance negating advantages of an end-to-end permit processing platform.

To this end, an alternative algorithm using a hybrid-iterative search algorithm after [2] was developed. This algorithm, described in detail in Appendix B, quickly and efficiently calculates optimal permit routes through the DelDOT highway network. The algorithm combines a pre-processing strategy with an iterative search algorithm and approximation function to successively constrain the network until a termination condition is met. A simple minimum cost path sub-problem over successively constrained networks is solved during each iteration. The advantages of this approach lie in the ability to use a generic vehicle routing SDSS without the need to pre-process the entire network. Processing efficiencies are gained by increasing the number of optimizations which can be solved in a fraction of a second and decreasing the number of detailed bridge analyses performed which are both resource intensive (each bridge analysis takes between 1 and 2 s to set up and run) and require access to a limited pool of critical resources. This processing strategy results in an average 16 bridge analyses performed rather than the full 2500 being processed during the execution of each permit routing problem.

The number of permit routes which could be solved concurrently using the web-based system is limited by the number of licenses available for the third-party bridge analysis software. This software then becomes a constraining critical resource, limiting the ultimate scalability of the application. In order to reduce overall execution time and increase the number of concurrent permit routes which could be processed, the algorithm was modified to include a bridge-filtering function which approximates the more rigorous detailed structural analysis. This approximation function acts as a filter, performing a quick and <sup>b</sup>web-friendly<sup>Q</sup> analysis of permit vehicles and bridges. Bridges failing the approximation are further analyzed using the thirdparty software while bridges passing the filter-test are not tested further. This filtering approach has three major design benefits. First, it greatly increases the speed of execution because only failing and marginal bridges are analyzed in detail. Second, fewer licenses for the third-party analysis software are required because the majority of bridges do not require detailed analysis. This reduces overall implementation costs as fewer third-party software licenses are required. Last, scalability issues associated with access to critical resources are removed as the number of detailed analyses per permit is greatly reduced.

## 4.3. Implementation

Once designed, a systems architecture to implement the algorithm had to be developed. The iterative nature of the permit routing algorithm creates a set of minimum cost path sub-problems during execution. These sub-problems can be trivially solved using a generic vehicle routing SDSS. Additionally, a generic geocoding SDSS can be used to validate and locate trip ends as this process occurs prior to the start of the algorithm and is used to set origin and destination nodes on the network. These generalized requirements were used to define several logical SDSS components each of which performs a specialized function within the overall permit routing application. In addition to the vehicle routing and geocoding modules, a specialized module to implement the algorithm and evaluate candidate permit routes and an interface component to perform input, output, validation and error checking functions were designed (Fig. 4).

Complete and valid permit routing requests are delegated to the OS/OW algorithm component which, in turn, creates and delegates sub-problems to location components and route-finding components as a permit routing problem is solved.

J2EE Enterprise Java Beans (EJBs) were selected as the development platform for all permit routing components as the EJB design pattern provides an interoperable platform for high-performance, scalable and reliable distributed systems, meeting requirements of ITMS (see Appendix A). Each decision component is implemented as an EJB and managed in separate bean pools which operate independently but can collaborate to perform complex tasks. In the initial deployment, all three bean pools run in a single J2EE Application Server and interact with the centralized relational database using shared system resources.

Client applications such as OOPS access the permit routing application via a J2EE Servlet residing within a J2EE Container. Servlets are managed by the Web Services layer and are multi-threaded, allowing concurrent requests to be serviced. Clients send permit routing requests to the Servlet as XML documents which conform to an OSOWRouteRequest Data Type Definition (DTD). These documents are transmitted as simple strings in an HTTP POST request. The Servlet validates the input XML document and delegates the request to an EJB in the OSOW pool where the request is executed. Upon termination, the OSOW EJB returns the result to the Servlet which, in turn, transmits the results back to the client as a XML document which conforms to an OSOWRouteResponse DTD. Both the OSOWRouteRequest and OSOWRouteResponse DTDs were developed as part of the project.

## 4.4. Testing and configuration

The DelDOT permit routing application is designed to service requests from other applications, relying on other systems such as OOPS or simple web-browsers to format, transmit and receive XML documents and provide user-interactions. The run-time behavior of the SDSS is controlled through a set of configurable parameters which are loaded when the server is started while the number of beans in each bean pool and interaction between bean pools is controlled by configuration options of the J2EE application server.

![](/api/attachments/JW9J86MS/fulltext/images/5f654f54d33fa3683d1974d76ec29af57f6b14fc392cb7e387df2b2d5a9c325f.jpg)  
Fig. 4. Logical decision components and their interaction.

The absence of a native user-interface for the permit routing application became a problem during system testing and acceptance. The initial project scope failed to include adequate testing facilities for the permit application, mistakenly assuming that the OOPS system and user-interface would prove adequate as a testing platform. This led to several project issues which ultimately delayed delivery of the permit routing application for almost 12 months. Staffing issues and changing priorities within DelDOT delayed modification of OOPS so that it could interoperate with the permit routing application. Moreover, licensing restrictions limiting non-DOT access to ITMS and OOPS greatly restricted testing opportunities. Finally, a set of system validation and testing tools were developed at additional cost so that DelDOT staff could measure the effectiveness of the SDSS, determine the quality of results and fine-tune algorithm parameters for use within ITMS. Two testing tools were developed as part of this process. The first testing tool provides a browser-based user-interface allowing users to select candidate permit routes from a historical permit database and perform route validations as if the data originated from OOPS. Results of each analysis are returned in tabular form and as an interactive GIS map allowing the user to graphically display and validate each permit route generated.

The second testing application tests the speed and throughput of the permit routing system under varying simulated system loads. This multi-threaded client randomly selects permits from the same historical database and validates them against the permit routing application for a specified testing period, 2 h for example. User-configurable parameters control the number of concurrent requests processed on the permit routing server and the length of the test. Results of this testing indicate expected average time required to validate a permit under operational conditions.

The J2EE application server is configured via an administration interface provided by the J2EE application server. This system console allows the user to see the number of concurrent transactions and manage the EJB resources in each of the bean pools. Among the important configuration information provided by the J2EE system console is number of queued requests, number of failed requests and number of EJBs idle and in use within each bean pool. This information enables a user to fine-tune the number of EJBs in each pool such that overall throughput in the system is maximized.

## 5. System benefits

The system described in this paper was installed in March 2002. Average processing times for validating permit routes and generating alternatives range from 5 to 30 s depending on several factors including number of structural analyses performed, number of alternative candidate routes generated and number of concurrent requests. In addition to the immediate benefits realized by the permit routing system, several additional benefits which could facilitate future DelDOT planning operations are realized. This section identifies and discusses these benefits.

## 5.1. Immediate benefits

Some of the immediate benefits afforded by the permit routing system include improved customer service, reduced permit processing costs and improved safety. Customer service is improved by reducing lead-times for permit applications from weeks to seconds and coupling OOPS with the new application enabling an end-to-end permit-processing solution capable of generating fully validated permits within a few seconds. Customer service is important to DelDOT as their mission as a publicly funded institution is to provide an efficient and cost-effective transportation network for highway users. Over 73% of goods moved in Delaware use highway transport, consequently, highway transportation plays a vital role in the state’s economy as it supports statewide commerce and serves the state’s busy ports and military facilities. Recent highway user surveys, however, report that only 31% of respondents feel that the highway system supports their needs <sup>b</sup>very well<sup>Q</sup> while 59% of respondents state that their highway needs are <sup>b</sup>somewhat met<sup>Q</sup> [26].

The permit routing system helps reduce DelDOTs permit processing costs since a full-time staff for validating permit routes is no longer needed. DelDOT initially planned to re-assign up to five staff members to other activities within their bridge division as a direct result of the permit routing application. As the permit routing system is scaleable, it can meet anticipated demand increases, currently at 6% per year, for many years to come, providing additional cost benefits over the life of the application.

Potential safety improvements and highway maintenance cost reductions stem from a system which reacts to changing highway conditions by incorporating updated highway information into permit routing decisions. The ITMS framework provides the permit routing application access to all applicable transportation data including a spatial database of planned events which can affect permit routing including locations of highway and bridge maintenance activities as well as unplanned events such as damage reports to structures and accidents which can affect the flow of highway traffic. Moreover, potential damage to bridges can be mitigated by managing heavy truck routes. DelDOT currently spends over US\$100 million each year on bridge repairs, representing almost 25% of DelDOTs annual highway budget [26].

## 5.2. Potential future benefits

The new permit routing system stores permit routes to ITMS’s shared relational database. Over time, this historical repository of permit routes provides DelDOT with valuable business intelligence which can provide significant potential benefits including enhanced planning information and the ability to pro-actively notify vehicle operators of changes which might affect preplanned permit routes.

Planning operations can be greatly improved over time as permit routes stored in the ITMS database provide a repository of historical information which can be analyzed by a GIS to understand the spatial and temporal patterns of demand for permit routes and this information used to better serve highway users in the future. For example, permit route data can be queried to determine the number and characteristics of vehicles permitted to traverse any bridge or section of highway for a given range of dates, the sections of highway and bridges which carry the most permit route traffic, or the routes taken by the heaviest, widest or highest vehicles. Deficiencies in the existing highway system can also be identified. Structures which restrict vehicle travel causing permit vehicles to route around them leading to increased vehicle miles can be identified using a combination of historical permit route data and a GISs spatial query functions. Similarly, potential benefits of upgrading sections of highway to accommodate larger, heavier or taller vehicles can be determined and the spatial impact of restricting certain types of vehicles from sections of the existing highway can be calculated. This type of information would enable DelDOT to better understand existing and changing patterns of highway use and better accommodate current and changing needs of highway users. Prior to this project, this information could only be created by manually processing archived paper permits, analyzing each permit against paper maps to determine the routes and collating this information by hand in a spreadsheet.

Another potential customer-service benefit afforded by the new permit routing system exists. Changes occurring in the highway system can be queried against the permit route database and routes affected by the changes identified. The location of an unplanned event which weakens a bridge structure, closes part of a highway or requires a traffic diversion, for example, can be queried against the permit database and permit routes which will traverse an affected section of highway identified. If necessary, these affected routes can be automatically re-validated and revised permits generated and sent to vehicle operators prior to travel.

## 6. Conclusions

The web-based permit routing SDSS described in this paper replaces a labor intensive manual process and helps DelDOT achieve several organizational goals. Creating the application required developing a spatial decision support system that could work within an existing web-architecture, could inter-operate with other hosted applications and could interface with a variety of current and future client systems. As no existing commercial solutions could meet these requirements a new SDSS was designed and developed along with formalized XML specifications for data input and output and a set of user interfaces for testing and configuring the system.

During the course of the project, several important issues specific to the web-development effort became apparent and had to be resolved. First, not enough attention was placed on the development of user interfaces and tools which could sufficiently test the completed application during the specification of the contract. This management oversight caused a delay in delivering the system and increased development costs because appropriate testing and validation tools had to be designed and developed. Second, a new web-friendly algorithm was developed because existing algorithms for solving the permit routing problem are designed for single-user systems and are too resource-intensive and, therefore, not well suited for implementation in web-architectures where processing resources are shared.

The permit routing application conforms to the major requirements of a Web-Based DSS described by Power [20]. Differences between the characteristics of generic web-based DSSs and this implementation lie in the use of XML rather than HTML as the document format for interfacing between client and server systems and the use of a J2EE Servlet operating within a J2EE application server rather than a generic HTTP server such as Apache, as the primary interface of the web-tier.

The J2EE web-architecture provides several benefits over traditional thick-client or client-server architectures which are consistent with the benefits identified in [20]. First, web-architectures are designed to manage large numbers of concurrent requests while maintaining consistent response times. The permit routing SDSS described can simultaneously process multiple permit routing requests as they are submitted through the Internet and generate responses quickly within a known processing time of 5 to 30 s. Second, the web-based SDSS is available 24 h a day, 7 days a week, allowing vehicle operators process permits according to their needs rather than conforming to normal workday hours of DelDOT staff.

Additional benefits associated with the J2EE webplatform are also identifiable. First, The EJB architecture used to implement the system enforces modular system design and component reusability. This approach to systems design enables DelDOT to create a suite of re-usable spatial decision support tools which can be used by other applications, thereby avoiding possible duplication of functionality within ITMS and reducing development costs of future applications. This project contributes a generic location analysis tool, a generic minimum cost path solver and the specialized OS/OW solver component to the ITMS toolbox. Follow on ITMS projects using these SDSS components are already in progress [23].

Second, all input and output in the new system is performed using MIME-compliant, text-based XML documents which can be generated by a wide variety of applications. XML, a W3C standard, removes issues associated with transferring data between heterogeneous systems while transmission of these documents via HTTP over TCP/IP networks enables a wide variety of existing and future systems to interact with the permit routing application. Indeed, permit routing problems can be generated, solved and results analyzed using nothing more sophisticated than a simple text editor and a web-browser.

Last, the web-based system can scale to meet future processing demands. Increasing the number of permit routes which can be analyzed per day using a traditional client based SDSS application requires adding additional staff, workstations and software licenses, increasing overall processing costs. In contrast, web-based systems have scalability designed-in. Scalability in this case is achieved through the management of independent pools of distributed components. As demand increases, more EJB instances within each EJB pool can be enabled thereby allowing more permit routes be simultaneously analyzed. This increase in scalability can continue until the physical capacity of the hardware is reached at which time, additional hardware can be used to distribute the decision components across multiple physical systems, providing a sustainable systems architecture for the foreseeable future.

## Acknowledgements

Part of the work described in this article was performed under contract with Delaware Department of Transportation by TransDecisions Inc., Boston, MA between 1999 and 2002 where Dr. Ray was co-founder and Chief Technology Officer. Ownership of the permit routing SDSS was transferred to Bentley Systems in December 2003 who now own all rights to the software. In order to protect confidentiality agreements and copyrights, all information provided in this manuscript is drawn from publicly available sources of information including conference proceedings, published white papers and marketing materials.

The author would like to thank the anonymous referees and editors for their insightful comments and suggestions during the preparation of the manuscript.

## Appendix A. J2EE-based web architectures

Software architectures determine how system elements are identified, how they interact to form a system and the methods by which system elements communicate [8]. Web architectures are specialized software architectures designed around principles of system-wide universality of access and interoperability between systems [3]. These principles are implemented through a number of fundamental specifications including Universal Resource Identifiers (URIs) providing generic identification methods for any identifiable resource on the Web; Hyper Text Transfer Protocol (HTTP) providing naming schemes and access mechanisms to resources and remote operations; and data formats including Hyper-Text Markup Language (HTML) and more recently Extensible Markup Language (XML), a simplified meta-language derived from SGML facilitating seamless cross-platform data exchanges [9].

Java is a programming language and application development platform designed to enable development of secure, high performance and highly robust applications on multiple platforms in heterogeneous, distributed networks [10]. Java 2 Enterprise Edition (J2EE) extends the basic Java environment providing a multi-tiered architecture consisting of four distinct application tiers: clients, web, business logic and database, hosted over three distinct logical domains: client machines, J2EE application server machines called J2EE Containers and database machines [1]. J2EE Containers interface between application components and platform-specific functionality promoting platform independence. Containers also provide security models, transaction management functions, component life-cycles and access to shared resources both within and across containers [1].

Within the J2EE architecture, business logic is organized into self-contained functional units called J2EE Components composed of Java classes and other files necessary to perform some atomic function. Servlets, Applets and Enterprise Java Beans

(EJBs) are examples of various types of J2EE Components available for developers to use. J2EE Containers manage component life-cycles and enable components distributed across different J2EE Containers to communicate as if they were in the same Container. EJBs are managed by a Container as homogenous collections of objects called EJB pools. Each EJB pool is independently configured to allow a maximum number of EJB instances be available for an application. EJB instances are inactive until they are allocated work, at which time they are activated. As EJBs are selfcontained components, the number of simultaneous operations that can be performed is equal to the number of EJB instances in the pool.

## Appendix B. Optimal permit routing algorithm

The permit routing problem can be formulated as a binary integer programming problem as follows. Let $G = ( N , A )$ be a directed graph consisting of a set of nodes, $N _ { \ast }$ and a set of arcs, A, each with non-negative cost $c _ { i j }$ . The objective function is then:

![](/api/attachments/JW9J86MS/fulltext/images/20eaf2eb7b2ed05b3ca6afda3ab7d98f69b31b41a71d070d1ff15c53b205a635.jpg)  
Fig. 5. Search algorithm.

![](/api/attachments/JW9J86MS/fulltext/images/d19382a468bb233c403f5cb8b38c6d87bf7585f599d3a21fc305ead6b2398352.jpg)  
Fig. 6. Bridge analysis algorithm.

$$
\operatorname{Min} (z) = \sum_ {(i, j) \in A} c _ {i j} x _ {i j}\tag{1}
$$

Such that,

$$
\sum_ {j: (i, j) \in A} x _ {i j} - \sum_ {j: (j, i) \in A} x _ {j i} = \left\{ \begin{array}{l l} + 1 & \text { if   } i \text {   is   the   origin } \\ - 1 & \text { if   } i \text {   is   the   destination } \\ 0 & \text { else } \end{array} \right.\tag{2}
$$

$$
h \left(x _ {i j}\right) \geq H _ {v} \quad \forall \left\{x _ {i j}: (i, j) \in A \right\}\tag{3}
$$

$$
w \left(x _ {i j}\right) \geq W _ {v} \quad \forall \left\{x _ {i j}: (i, j) \in A \right\}\tag{4}
$$

$$
l \left(x _ {i j}\right) \geq L _ {v} \quad \forall \left\{x _ {i j}: (i, j) \in A \right\}\tag{5}
$$

$$
x _ {i j} = \{0, 1 \} \quad \forall \left\{x _ {i j}: (i, j) \in A \right\}\tag{6}
$$

where $h ( x _ { i j } ) , w ( x _ { i j } )$ and $l ( x _ { i j } )$ are functions defining the maximum allowable vehicle height, width and weight respectively for any structure aligned over arc $( i , j )$ and $H _ { \nu } , W _ { \nu }$ and $L _ { \nu }$ are corresponding maximum physical dimensions for vehicle v.

Objective (1) with constraints (2) and (6) defines a standard minimum cost path problem in $G .$ As constraints (3), (4) and (5) are linear and the right-hand sides are known at run time, problems (1)–(6) reduces to a simple minimum cost path problem by pre-processing A and fixing $x _ { i j } = 0$ for all edges which fail sufficiency tests (3), (4) and (5). Removing these edges from $G$ creates a reduced network, $G ^ { \prime }$ . Solving (1), (2) and (6) over $G ^ { \prime }$ provides an optimal solution to (1)–(6) which can be trivially solved by a finding the shortest simple chain in $G ^ { \prime }$ from the origin to the destination.

In order to solve (1)–(6) efficiently, an iterative search algorithm after [3] was developed. The threephase algorithm illustrated in Fig. 5 initially pre-processes height (3) and width (4) constraints to remove deficient highway segments from the network creating reduced graph $G ^ { \prime }$ (Phase I). The algorithm then solves (1) in $G ^ { \prime }$ subject to (2) and (6) (Phase II). At each iteration a new candidate route is found and constraint (5) is evaluated for each edge where $x _ { i j } = 1$ (Phase III). If any bridges along any edge $x _ { i j }$ in the candidate path fail the weight test, the route is flagged as being infeasible and failing edge $x _ { i j }$ is removed from $G ^ { \prime }$ and, therefore, removed from consideration in subsequent iterations. The algorithm continues to iterate Phase II and Phase III until one of three termination criteria occurs: a route feasible to (5) is found, this route is then optimal to (1)–(6); no route is found, the problem is then infeasible; or the number of allowable iterations is exceeded and the algorithm is prematurely terminated.

Constraint (5) is analyzed in Phase III. In order to speed up execution and remove dependency on thirdparty software, an approximation to the detailed structural analysis based on the Federal Bridge Weight Formula is calculated [29]. This formula rates a vehicle’s ability to traverse a given bridge based on its axle configuration and weight distribution over the axles. If a bridge/vehicle combination fails the bridge formula test a detailed structural analysis is performed on the bridge (Fig. 6).

Once a vehicle has been tested against a bridge, the bridge/vehicle combination is added to a list of passing bridges or failing bridges based on the result of the test and will not be tested again during the analysis. If a bridge fails the structural analysis the corresponding network edge is removed from the network and the candidate route is flagged as being infeasible.

## References

[1] E. Armstrong, J. Ball, S. Bodoff, D. Carson, I. Evans, D. Green, K. Haase, E. Jendrock, The J2EE 1.4 Tutorial, 2004 (Available online at http://java.sun.com/j2ee/1.4/docs/tutorial/doc/).

[2] O. Berman, D. Einav, G. Handler, The constrained bottleneck problem in networks, Operations Research 38 (1) (1990)1998.

[3] T. Berners-Lee, Web Architecture from 50,000 Feet, W3C, 1998 (Online at www.w3c.org/DesignIssues/Architecture. html).

[4] H.K. Bhargava, D.J. Power, Decision support systems and web technologies: a status report, Proceedings of the Americas Conference on Information Systems, 2001.

[5] J.F. Campbell, A. Labelle, A. Langevin, A hybrid travel distance approximation for a GIS-based decision support system, Journal of Business Logistics 22 (2) (2001).

[6] R.L. Carraway, T.L. Morin, H. Moskowitz, Generalized dynamic programming for multicriteria optimization, European Journal of Operational Research 44 (1) (1990).

[7] K. Fagerholt, A computer-based decision support system for vessel fleet scheduling—experience and future research, Decision Support Systems 37 (1) (2004).

[8] R.T. Fielding, R.N. Taylor, Principled design of the modern web architecture, ACM Transactions on Internet Technology 2 (2) (2002).

[9] R.J. Glushko, J.M. Tenenbaum, B. Meltzer, An XML framework for agent-based E-Commerce, Communications of the ACM 42 (3) (1999).

[10] J. Gosling, H. McGilton, The Java Language Environment: A White Paper, 1996, Available online at http://java.sun.com/ docs/white/langenv/ Access 10/3/2003.

[11] D. Green, T. Bossomaier, Online GIS and Spatial Metadata, Taylor & Francis, London, 2001.

[12] R.W. Hall, Change of direction, OR/MS Today 29 (1) (2002).

[13] S. Jarupathirun, F. Zahedi, GIS as spatial decision support systems, in: J. Pick (Ed.), GIS in Business, Idea Group, Hershey, PA, 2005.

[14] P.B. Keenan, Spatial decision support systems for vehicle routing, Decision Support Systems 22 (1) (1998).

[15] P. Keenan, S. Brodie, A prototype web-based carpooling system, Proceedings of the Americas Conference on Information Systems, 2000.

[16] Q. Ma, P. Steenkiste, On path selection for traffic with bandwidth guarantees, Proceedings of IEEE Conference on Network Protocols, 1997.

[17] B.E. Mennecke, M.D. Crossland, B.L. Killingsworth, Is a map more than a picture? The role of SDSS technology, subject characteristics, and problem complexity on map reading and problem solving, MIS Quarterly 24 (4) (2000).

[18] H. Miller, S.-L. Shaw, Geographic Information Systems for Transportation: Principles and Applications, Oxford University Press, New York, NY, 2001.

[19] R. Osegueda, A. Garcia-Diaz, S. Ashur, O. Melchor, S.-H. Chang, C. Carrasco, A. Kuyumcu, GIS-based network routing procedures for overweight and oversized vehicles, Journal of Transportation Engineering 125 (4) (1999).

[20] D.J. Power, Web-based and model-driven decision support systems: concepts and issues, Proceedings of the Americas Conference on Information Systems, 2000.

[21] J.J. Ray, Oversize/overweight routing server, GIS-T Symposium, 2001.

[22] C. Rinner, Web-based spatial decision support: status and research directions, Journal of Geographic Information and Decision Analysis 7 (1) (2003).

[23] V. Rucinski, Everyplace is someplace: a universal location based service at Delaware DOT, GIS-T Symposium, 2002.

[24] State of Delaware Department of Transportation, Oversize Overweight Hauling Permit: Policy and Procedures Manual, 2000.

[25] State of Delaware Department of Transportation, User’s Guide for the Permit Service Customer, 2001.

[26] State of Delaware Department of Transportation, Delaware Transportation Facts, 2003.

[27] V. Sugumaran, R. Sugumaran, Spatial decision support systems using intelligent agents and GIS web services, Proceedings of the Americas Conference on Information Systems, 2003.

[28] J.-C. Thill, Geographic information systems for transportation in perspective, in: J.-C. Thill (Ed.), Geographic Information Systems in Transportation Research, Pergamon Press, Oxford, 2000.

[29] U.S. DOT, Federal Bridge Formula, 2000, Available online at http://www.fhwa.dot.gov/policy/otps/truck/wusr/chapap.htm. Accessed 1/3/2005).

[30] D. Weigel, B. Cao, Applying GIS and OR techniques to solve sears technician-dispatching and home-delivery problems, Interfaces 29 (1) (1999).

[31] J. Werner, Inside Delaware’s DelTrac Integrated Transportation Management System, 2002, Available on line at http:// www.nawgits.com/icdn/deltrac.html. Accessed 9/27/2003.

[32] Wisconsin Department of Transportation, Faster Route Permitting for Oversize/Overweight Vehicles, 2001, Report No. 0092-45-19.

Julian J. Ray is an Assistant Professor in the University of Redlands, School of Business and co-founder and Chief Technology Officer, C2GLogistics, Boston, MA. Dr. Ray received a BA (Hons.) from Reading University, England in 1984 and a PhD in Geography from the University of Tennessee in 1990. Julian is an active practitioner and entrepreneur and has developed spatial information systems and authored commercial Geographic Information Systems software for a number of private, Federal and State organizations. Dr. Ray researches, practices and publishes in the general areas of spatial information systems, decision support systems and electronic commerce and is co-chair of the GIS/LBS mini track at AMCIS.
