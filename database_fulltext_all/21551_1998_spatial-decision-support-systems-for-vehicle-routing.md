---
otero_id: 21551
otero_key: "NQR6HYM8"
title: "Spatial decision support systems for vehicle routing"
authors: "Peter B Keenan"
year: "1998"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(97)00054-7"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Spatial decision support systems for vehicle routing

Peter B. Keenan )

Department of Management Information Systems, Faculty of Commerce, UniÕersity College Dublin, Dublin 4, Ireland

## Abstract

The vehicle routing field is a well-developed area of management science application. There is increasing recognition that effective decision-making in this field requires the incorporation of vehicle routing techniques into a decision support system Ž . DSS . In order to provide decision support for a wide range of problems, routing techniques should be combined with systems that can take advantage of new technologies. These include spatial techniques drawn from the field of geographic information systems GIS . A synthesis of appropriate algorithms and a GIS based computer system is identified as beingŽ . necessary for effective decision support for the vehicle routing problem. q 1998 Elsevier Science B.V.

Keywords: Vehicle routing; Decision support systems; Geographic information systems; Spatial decision support systems

## 1. Vehicle routing

## 1.1. The Õehicle routing problem

The problem of how to route and schedule vehicles is a long established area of operations research <sup>w</sup> <sup>x</sup> 14 , and routing models have been long been incorporated into decision support systems DSS . RoutingŽ . problems typically have a requirement for customers at known locations to be supplied with their demand by a set of vehicles; subject to limitations on the capacity of the vehicles, the duration of the routes, and the time at which the customer receives a delivery. All routing problems require that the products to be carried are assigned to the available set of vehicles and the vehicles are routed in an efficient way around the points to be visited. The difficulty of the overall problem is increased by the inevitable interaction between the phases; for example, an efficient allocation of loads to vehicles may lead to inefficient routes.

A wide variety of routing problems have been identified, a recent bibliographic review 27 identifies 500 articles representing relatively important contributions to the field of routing. These include arc routing problems where a sequence of arcs rather than points is the result of the routing process. The variation that is found in real world vehicle routing problems can greatly influence the type of decision to be made. A number of standard characteristics distinguish routing problems 8 . The most important of these characteristics include the location of demands: at network nodes or on arcs, the nature of the vehicle capacity constraints and the nature of the objective that defines a better route. These characteristics affect both the relevant data and the degree of difficulty in finding a good solution to the problem.

Some early routing software was based on the use of location coordinates and straight-line distance was used as a surrogate for actual travel distance. This abstraction of the problem assumed that selection of an appropriate path was a trivial exercise. In practice, the actual route is constrained by the need to use suitable roads. Therefore, the use of straight-line distance is unsatisfactory in many cases. The true distance approach, using distances calculated from the road network, reduced these problems. The use of the true distance approach has become an increasingly important feature of routing DSS design. However, this approach requires increased data and a consequent increase in the sophistication of the software used for the organisation of that data. In practice, routing problems are frequently constrained by time rather than by distance travelled. Estimates of the time taken for a route may be derived from the use of different speeds on different sections of the road network. The incorporation of this type of additional path data increased the usefulness of the problem formulation at the cost of making the software to solve it more complex.

## 1.2. Traditional Õehicle routing DSS

When considering vehicle routing problems using non-computerised methods, much reliance is placed on the spatial layout of the problem. Routes will typically be devised using paper maps, typically moving from one point to another, which appears to be visually close. Such manually designed routes will generally form compact blocks when completed. These compact blocks will generally seem reasonable to all those involved, including the customers and the vehicle drivers.

Mathematical techniques will obviously tend to produce routes which link neighbouring points. However, the routing heuristics commonly used will sometimes produce routes that look quite bizarre in shape. For a small number of problems that are tightly constrained, by factors other than the location of the points to be visited, unusually shaped routes may in fact be optimal. However, for most problems, skilled manual alteration of the shape of a route in a DSS can improve the routes generated by the heuristics that are commonly used. These alterations will improve the spatial organisation of the route. These changes will also tend to improve the acceptability of the route to customers and staff. User intervention is often the only way of ensuring that the routes meet ‘soft’ constraints that are not part of the mathematical formulation. Experienced schedulers have considerable knowledge of local conditions and of the relative importance of the various constraints. Human intervention in the routing process can substantially improve the quality of the routes produced. For these reasons there has been increasing recognition that the available algorithmic techniques can most effectively be used as part of a DSS.

With the greater availability of graphics terminals and personal computers, there has been increasing use of graphics to represent routes on screen. By the early 1980s there was increasing recognition of the need to combine management science algorithms with appropriate graphics 4 . A mid-decade review <sup>w</sup> <sup>x</sup> of the vehicle routing field 11 argued for the use of <sup>w</sup> <sup>x</sup> graphically based interactive techniques combined with appropriate algorithms. The use of microcomputers has allowed the cost-effective implementation of routing software with a graphic component that recognises the spatial component of the problem <sup>w</sup> <sup>x</sup> 10 . The role of visual interfaces is widely recognised as a critical issue in the continuing development of management science generally 23 and rout-<sup>w</sup> <sup>x</sup> ing in particular 9 .<sup>w</sup> <sup>x</sup>

The routing software that became available during the 1980s provided on-line access to increasing amounts of information that the scheduler might require to evaluate a route. This trend reflected the need to include a variety of information sources relevant to a routing decision. Most traditional routing problems use information that is particular to the problem. Examples of such information might be the specific demand volumes of a firm’s customers or the size of an organisation’s vehicles. This information will probably already be available in the Management Information System MIS of the organisa-Ž . tion. Effective decision support, for problems making use of this type of information, requires a suitable link to the MIS database and an interface that is customised to the specific problem. A good example of such a routing system was that used in the Air Products in Canada 6 . In order to organise the <sup>w</sup> <sup>x</sup> larger amounts of information incorporated in routing systems, database management systems were increasingly required. By the mid-1980s, routing systems combined algorithms with the increasing use of graphic interfaces and links to databases. These systems could increasingly be seen as a form of DSS, as they contain the recognised components of a DSS, i.e., the interface, solver and database modules. Modern routing DSS has taken advantage of developments such as graphical user interfaces, of which a recent example is the FleetManager DSS in New Zealand 5 .<sup>w</sup> <sup>x</sup>

An analysis of DSS applications 16 identified <sup>w</sup> <sup>x</sup> routing as the most important area of DSS application in business. The authors suggest that the relative importance of routing DSS reflects the nature of routing problems. They suggest that these are less suitable for the expert systems approach used in other business applications. This analysis indicates the importance of skilled user intervention in the routing problem solving. This form of user interaction is inherent in DSS but it is not found in expert systems, where the user is assumed not to have the expertise required to intervene in the problem solving process. While traditional routing systems generally utilise algorithmic approaches rather than a rule based approach, systems that are more complex may incorporate elements of both. It has been argued that routing DSS can be enhanced by including a knowledge base component 15 . This is especially likely <sup>w</sup> <sup>x</sup> to be true for DSS designed to support more complex routing problems. An important prototype DSS, Tolomeo 1,2 uses artificial intelligence techniques<sup>w</sup> <sup>x</sup> to identify the appropriate algorithmic representation of a problem, including routing type problems.

It has been argued that the user interface is the most important component of a DSS and that the interface design may provide a framework for the entire DSS 21 . By designing the entire DSS around <sup>w</sup> <sup>x</sup> the interface, the user’s view of the problem can be more accurately captured, thereby providing more effective decision support. In the case of vehicle routing, the user’s view of the problem is a spatial one and the user can most effectively interact with a system that accommodates this view. The trend within routing systems has been to facilitate the spatial representation of routes as part of the interface, in keeping with the user’s perception of the problem.

Jones 22 discusses the concept of anchoring,<sup>w</sup> <sup>x</sup> which recognises that people prefer the problem representation that they are first introduced to. For routing problems, without the use of a computer, problem solvers traditionally make use of paper maps. These maps provide a number of geographic reference points other than just the location of the customers to be routed. In order for a routing DSS to accommodate this anchored view of the problem, it may be appropriate to display geographic information other than just the customer locations. The most obvious need is for a display of the road network, but other geographic information may also contribute to user decision-making. This type of information usually originates from external sources, such as public mapping agencies, rather than the internal MIS of the company.

One example of the integration of geographic data into a DSS might be the use of a bitmapped raster Ž . image of the standard paper map as a backdrop to the interface. The incorporation of onscreen maps and appropriate algorithms is not a new concept, with systems being used in the 1970s, for example the GADS system at IBM 18 . In many cases, <sup>w</sup> <sup>x</sup> however, the map displayed on screen is only background information for the routing process and is not well integrated with it. For example, a recent version of the Autoroute package uses a CD-ROM to store bitmap representations of UK maps, as a background to the routing network 20 . However, if the display<sup>w</sup> <sup>x</sup> lacks links to a geographic database, such maps provide only a limited contribution to the decisionmaking process.

## 2. Spatial decision support systems

## 2.1. Geographic information systems GIS( )

Routing models, and related areas of management science such as location analysis, make extensive use of geographic data. A system to support these decisions must be capable of effectively handling this spatial data. The display and manipulation of geographic and spatial information on a computer is usually achieved using a Geographic Information System GIS . While a large variety of GIS softwareŽ . exists, it is characterised by the ability to display and manipulate data stored in a spatial database. GIS allows the use of point, arc and polygon data and often allows the use of bitmap images. GIS allows users to perform spatial queries, for example using contour data to identify the area liable to be affected by flooding on the banks of a river. In the past GIS software was typically workstation based and relatively specialised and expensive. However as personal computers have become more powerful, new general purpose desktop GIS systems with substantial functionality have become available.

The growth of GIS has been rapid as numerous potential applications have been recognised. A recent paper prepared on behalf of the European Commission 19 indicates the GIS software’s international<sup>w</sup> <sup>x</sup> market is worth about US\$1 billion in 1996. It is estimated that up to 80% of data needed for the activities of business and government is spatially related 17 . This includes much of the non-<sup>w</sup> <sup>x</sup> problem-specific data used in vehicle routing e.g.,Ž population data . The growth of GIS has lead to the. increasing availability of spatially related data, with digital mapping data being readily available for most regions. As this data becomes widely used, its cost will fall, providing a valuable source of additional information for vehicle routing decision support software. In developed countries digital data is being prepared for use by car navigation software 19 and<sup>w</sup> <sup>x</sup> this data is relevant to a wide range of routing problems. Therefore, a useful contribution can be made, by GIS techniques, to the design of a decision support system for vehicle routing. Such a system would be a spatial decision support system SDSS ,Ž . such systems have been shown to facilitate decision-making 13 . Various types of SDSS are <sup>w</sup> <sup>x</sup> being used which combine GIS information with appropriate algorithms. Muller 28 identified SDSS<sup>w</sup> <sup>x</sup> as a growth area in the application of GIS technology. A recognised existing application of SDSS that is relevant to vehicle routing is in facility location applications 3 . Facility location is an area of appli- <sup>w</sup> <sup>x</sup> cation of traditional management science techniques where the spatial dimension to the problem is obvious.

The focus of an SDSS, as of a DSS generally, is to provide specific support for the problem to be solved 3 . In the case of a routing problem, this may<sup>w</sup> <sup>x</sup> entail the display of features such as the road network, administrative boundaries, and an indication of the density of population within the region. The specific requirements of particular applications will determine the geographic information, which must be displayed. Where interaction between road networks and other types of geographic entities is required, an SDSS approach can greatly enhance the development of a routing DSS.

## 2.2. GIS based routing software

A number of existing systems incorporate geographic data and network algorithms, without using conventional GIS software. Two of the most important are Tolomeo 1,2 and Georoute 26 . These<sup>w</sup> <sup>x</sup> <sup>w x</sup> systems give users considerable autonomy to tailor the operation of the DSS by manipulating the networks represented on screen. This flexibility is facilitated by the use of maps as a static backdrop to the manipulation taking place. Such a DSS might be built around a number of available GIS packages. Traditionally GIS software supported routing in a limited way by providing routines for the calculation of shortest paths. However, some newer software has a more comprehensive set of routing procedures. A good example of this trend is the Transcad GIS software 30 , which offers a variety of routing tools.<sup>w</sup> <sup>x</sup> However, these routing tools must inevitably be general purpose in nature, while effective decision support requires specific customised techniques for the problems being supported. These existing GIS products which have support for routing techniques can be used as a DSS generator for a routing SDSS, with the inclusion of appropriate customised routing algorithms 24 . GIS products are increasingly avail-<sup>w</sup> <sup>x</sup> able on inexpensive personal computers. These products offer significant GIS functionality at a much lower cost than traditional workstation based software. While some of these PC based GIS systems are less powerful than their workstation based equivalents, the subset of functionality offered is often quite suitable for routing applications.

Spatial Decision Support Systems provide a synthesis of the advantages of traditional routing systems and the spatial tools provided with GIS software Table 1 . With the increasing use of GIS, theŽ . possibility exists of developing a SDSS to be used on relatively inexpensive equipment with which potential users are familiar. The growth of SDSS applications is also made possible by the growing availability of spatial data for popular GIS software, thereby reducing the costs of data collection. While this data has some limitations for use in a routing context 9 , it will increasingly become available in<sup>w</sup> <sup>x</sup> formats suitable for routing applications. As this data is increasingly used in a wide variety of situations, its cost will decline. This reduction in the cost of data will facilitate the use of additional information to more accurately model real world situations. GIS can provide a more comprehensive model of the road network, allowing more realistic modelling of path constraints 25 . As GIS use increases, comprehen-<sup>w</sup> <sup>x</sup> sive integrated databases of road networks will become available, for use in a variety of routing and vehicle navigation problems. These databases will contain data sourced from multiple information providers. Effective integration of data from these sources will become an important issue in their use for routing applications 12 . This will have implica- <sup>w</sup> <sup>x</sup> tions for the design of SDSS and the database structures to support decision-making.

Table 1  
Main characteristics of routing systems

<table><tr><td></td><td>Vehicle routing DSS</td><td>GIS</td><td>SDSS</td></tr><tr><td>Data</td><td>location coordinates, true distance matrix, multiple vehicle parameters</td><td>points, arcs and polygons, complex network data</td><td>points, arcs and polygons, complex network data and multiple vehicle parameters</td></tr><tr><td>Models</td><td>customised multi-vehicle multi-depot routing models</td><td>general purpose one vehicle shortest path type models</td><td>customised multi-vehicle multi-depot routing models</td></tr><tr><td>Interface representation</td><td>representation of points and routes</td><td>representation of multiple layers of spatial data</td><td>customised subset of available spatial data</td></tr><tr><td>Interface operations</td><td>ability to edit parameters and alter route sequence</td><td>map editing facilities</td><td>ability to edit maps, routing parameters and route sequence</td></tr></table>

The widespread use of spatial decision support systems will allow a greater diversity of modelling approaches than traditional vehicle routing applications. Vehicle routing techniques are generally based around the use of well-established management science techniques; for example travelling salesman heuristics or linear programming approaches. Modelling approaches drawn from the GIS environment will need to be used in addition to the traditional techniques used in the routing domain. The construction of a spatial decision support system will require an effective synthesis of these diverse techniques and the data needed to support them.

Routing SDSS may be built incorporating routing modules in existing GIS software 24 . This allows<sup>w</sup> <sup>x</sup> the GIS provide the database and interface components of the DSS for the spatial data, while the added module contains the models. The best current example, that we are aware of, where substantial routing functionality is combined with GIS software is the Routesmart software 7,9 . This software has been<sup>w</sup> <sup>x</sup> predominantly been used for arc routing problems in urban areas. This reflects the importance of geographic data such as the existence of one way streets or no left turns in this type of problem. The Routesmart algorithms can be incorporated into a number of GIS products. Another example is the routing modules produced by the RT-Soft 29 .<sup>w</sup> <sup>x</sup>

## 3. Conclusion

In this paper, we have suggested that GIS techniques can contribute to a broad class of routing problems. Standard GIS software may have some features, such as the provision of shortest path algorithms, which can be used as part of a routing system. However, a general purpose GIS will not allow the decision maker easily interact with the algorithms needed for complex multi-vehicle routing problems. A spatial decision support system is needed to combine appropriate routing algorithms with the use of GIS spatial data handling techniques. Existing work in the GIS and management science areas have concentrated on different aspects of the routing problem. Management science researchers have developed sophisticated algorithms to deal with various vehicle and location constraints while paying less attention to path constraints. GIS researchers have developed techniques to represent different types of location and networks and to generate appropriate paths through these networks. GIS software also provides a sophisticated interface to allow the representation and manipulation of geographic data.

We suggest that a combination of GIS and management science techniques would facilitate decision support for problems with complex path restrictions and multiple vehicles. Some of the problems we have identified, such as hazardous waste routing, have been researched in the past by researchers working within both the management science and GIS traditions. We suggest that for these problems, superior decision support can be achieved by a synthesis of techniques drawn from both of these fields. Such a synthesis will allow more complicated problems be addressed and will allow systems be developed for complex problems where there appears to be little work to date. Geographic data plays an important role in many routing problems relevant to current business needs; for instance topics such as routing in urban areas and hazardous waste routing. The effective combination of GIS and vehicle routing models, to build routing SDSS, is an area where there are many interesting and relevant research problems that have yet to be fully investigated.

## References

<sup>w</sup> <sup>x</sup> 1 A.A. Angehrn, Modelling by example: a link between users, models and methods in DSS, Eur. J. Oper. Res. 55 1991Ž . 296–308.

<sup>w</sup> <sup>x</sup> 2 A.A. Angehrn, H.-J. Luthi, Intelligent support systems: a ¨ visual interactive approach, Interfaces 20 6 1991 17–28.Ž . Ž .

<sup>w</sup> <sup>x</sup> 3 A.P. Armstrong, P.J. Densham, Database organization strategies for spatial decision support systems, Int. J. Geogr. Info. Syst. 4 1 1990 3–20.Ž . Ž .

<sup>w</sup> <sup>x</sup> 4 L.C. Barbosa, R.G. Hirko, Integration of algorithmic aids into decision support systems, MIS Q. 4 1980 1–12.Ž .

<sup>w</sup> <sup>x</sup> 5 C. Basnet, L. Foulds, M. Igbaria, FleetManager: a microcomputer-based decision support system for vehicle routing, Decision Support Syst. 16 1996 195–207.Ž .

<sup>w</sup> <sup>x</sup> 6 W.J. Bell, L.M. Dalberto, M.L. Fisher et al., Improving the distribution of industrial gases with an online computerized routing and scheduling optimizer, Interfaces 13 1983 4–23. Ž .

<sup>w</sup> <sup>x</sup> 7 L. Bodin, G. Fagan, L. Levy, et al., The RouteSmart system, in: Proceedings of the Conference on GIS in Business and Commerce, 1992, Denver, CO, USA.

<sup>w</sup> <sup>x</sup> 8 L. Bodin, B. Golden, Classification in vehicle routing and scheduling, Networks 11 2 1981 97–108.Ž . Ž .

<sup>w</sup> <sup>x</sup> 9 L. Bodin, L. Levy, Visualization in vehicle routing and scheduling problems, ORSA J. Comput. 6 3 1994 261–Ž . Ž . 268.

<sup>w</sup> <sup>x</sup> 10 L. Bodin, D. Salamone, The development of a microcomputer based system for vehicle routing and scheduling and its use for solving spatial and temporal problems, Math. Comput. Modelling 11 1988 558–562.Ž .

<sup>w</sup> <sup>x</sup> 11 K. Bott, R. Ballou, Research perspectives in vehicle routing and scheduling, Transportation Res., Part A 20A 1986Ž . 239–243.

<sup>w</sup> <sup>x</sup> 12 T. Cova, M. Goodchild, Spatially distributed navigable databases for intelligent vehicle highway systems, in: GIS<sup>r</sup>LIS ’94 proceedings, 1994, American Society for Photogrammetry and Remote Sensing, American Congress on Surveying and Mapping.

<sup>w</sup> <sup>x</sup> 13 M.D. Crossland, B.E. Wynne, W.C. Perkins, Spatial decision support systems: an overview of technology and a test of efficacy, Decision Support Syst. 14 3 1995 219–235. Ž . Ž .

<sup>w</sup> <sup>x</sup> 14 G.B. Dantzig, J.H. Ramser, The truck dispatching problem, Manage. Sci. 6 1959 80–91.Ž .

<sup>w</sup> <sup>x</sup> 15 P. Duchessi, S. Belardo, J.P. Seagle, Artificial intelligence and the management science practitioner: knowledge enhancements to a decision support system for vehicle routing, Interfaces 18 2 1988 85–93. Ž . Ž .

<sup>w</sup> <sup>x</sup> 16 S. Eom, S. Lee, J. Kim, The intellectual structure of decision support systems 1971–1989 , Decision Support Syst. 10 1 Ž . Ž . Ž . 1993 19–35.

<sup>w</sup> <sup>x</sup> 17 C. Franklin, An introduction to geographic information systems: linking maps to databases, Database 15 2 1992Ž . Ž . 12–21.

<sup>w</sup> <sup>x</sup> 18 B.F. Grace, Training Users of a Decision Support System, IBM Thomas J. Watson Research Laboratory, 1976.

<sup>w</sup> <sup>x</sup> 19 IMO, Geographic Information Systems in Europe: Problems and Potential, Information Market Observatory IMO , Euro-Ž . pean Commission, Luxembourg, 1995.

<sup>w</sup> <sup>x</sup> 20 D. Jarrett, AutoRoute on CD-ROM—route planning software, PC User 237, June 15, 1994, p. 80.

<sup>w</sup> <sup>x</sup> 21 C. Jones, User interface development and decision support systems, in: C. Holsapple, A. Whinston Eds. , Recent De-Ž . velopments in Decision Support Systems, Nato ASI Series, Springer-Verlag, Berlin, 1991, pp. 181–209.

<sup>w</sup> <sup>x</sup> 22 C. Jones, Anchoring and cross-fertilization, ORSA J. Comput. 6 3 1994 278–280.Ž . Ž .

<sup>w</sup> <sup>x</sup> 23 C. Jones, Visualization and optimization, ORSA J. Comput. 6 3 1994 221–257.Ž . Ž .

<sup>w</sup> <sup>x</sup> 24 P. Keenan, Using a GIS as a DSS Generator, in: J. Darzentas, J.S. Darzentas, T. Spyrou Eds. , Perspectives on DSS, Ž . University of the Aegean, Greece, 1996, pp. 33–40 ISBNŽ 960-7475-07-0 ..

<sup>w</sup> <sup>x</sup> 25 P. Keenan, Modelling routing problems in GIS, Working Paper MIS 97<sup>r</sup>4, Graduate School of Business, University College Dublin, Dublin, Ireland, 1997.

<sup>w</sup> <sup>x</sup> 26 G. Lapalme, J.-M. Rosseau, Georoute: a geographic information system for transportation applications, Commun. ACM 35 1 1992 81–88.Ž . Ž .

<sup>w</sup> <sup>x</sup> 27 G. Laporte, I. Osman, Routing problems: a bibliography, Ann. Oper. Res. 61 1995 227–262.Ž .

<sup>w</sup> <sup>x</sup> 28 J.-C. Muller, Latest developments in GIS<sup>r</sup>LIS, Int. J. Geogr. Info. Syst. 7 4 1993 293–303.Ž . Ž .

<sup>w</sup> <sup>x</sup> 29 RT-Soft, RT-Soft, 10205 Kingston Pike, Suite D161, Knoxville, TN 37922, 1997.

<sup>w</sup> <sup>x</sup> 30 Transcad, Transcad User’s Guide Version 3.0 for Windows, Caliper, Newton, MA, USA, 1996.

![](/api/attachments/NQR6HYM8/fulltext/images/032066b681b07c0054df40191534e2be8fef06b5b531328c345e3338e7fcd6a0.jpg)

Peter Keenan is a member of the Department of Management Information Systems at University College Dublin. He holds Bachelor of Commerce and Master of Management Science degrees from the National University of Ireland. Before joining UCD, he developed logistics software for a number of large Irish organisations. Currently, his research interests include geographic information systems in business, spatial decision support systems and the use of

the Internet for decision support.
