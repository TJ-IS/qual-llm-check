---
otero_id: 22042
otero_key: "E8CEB8AN"
title: "ODE: a tool for distributing object-oriented applications"
authors: "Sandeep Purao; Hemant K. Jain; Derek L. Nazareth"
year: "2002"
journal: "Information & Management"
doi: "10.1016/s0378-7206(01)00122-7"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# ODE: a tool for distributing object-oriented applications

Sandeep Purao $^{a,*}$ , Hemant K. Jain $^{b}$ , Derek L. Nazareth $^{b}$

$^{a}$ Department of CIS, Georgia State University, Atlanta, GA 30303, USA

$^{b}$ School of Business Administration, University of Wisconsin-Milwaukee, Milwaukee, WI 53201, USA

Received 6 June 1999; received in revised form 6 February 2001; accepted 31 May 2001

## Abstract

Object-oriented applications are increasingly being deployed in distributed computing environments. Technologies, such as Java RMI, and architectures, such as CORBA, DCOM, and Enterprise Java Beans, are facilitating and enhancing this trend. The performance and eventual success of these applications is dependent on distribution decisions made by the application designer. This decision is a complex one, involving a large number of alternatives and multiple conflicting criteria. Rigorous approaches for effective distribution of object-oriented applications are still lacking. This paper describes the implementation of a practical and effective approach for distributing object-oriented applications. A prototype decision support system—object distribution environment (ODE)—that implements the approach in the form of a user-friendly tool for the design of distributed object-oriented applications is described. ODE has been successfully used in the distribution of a real world distributed object-oriented system. © 2002 Elsevier Science B.V. All rights reserved.

Keywords: Object distribution; Distributed systems; Decision support system; Linear programming; Multiple criteria optimization

## 1. Introduction

Object-orientation and distributed systems are two key technologies driving much application development efforts today. The use of object-orientation for software design is clearly evident in new application development $[5]$ and migration $[11]$ fueled by the promise of easier maintenance and reuse. Increasingly, these application systems are being designed for deployment in distributed computing environments for greater flexibility and responsiveness. To exploit the benefits of both these technologies, significant efforts have been directed towards facilitation and standardization of distributed object computing. Architectures and technologies, such as OMG's CORBA, Microsoft's D'COM, and Sun's Enterprise Java Beans are making it easier to develop and deploy distributed object-oriented applications.

Another critical prerequisite for the successful design and deployment of these systems is effective object distribution, that is, a strategy for partitioning the system into appropriate distributable units and placing them across the existing network of computers to maximize some measure of performance and/or minimize cost. Distribution of object-oriented applications can present many interesting challenges. For example, conventional object-oriented wisdom may dictate that an entire class, that is, the set of instances along with the methods, be treated as an indivisible unit to maintain encapsulation. If, however, the entire set is assigned to a single processor, it may result in ineffective exploitation of processing capabilities, overburden a processor, and limit replication opportunities, as well as increase communication and messaging. On the other hand, if encapsulation is preserved, but superclasses and subclasses are assigned to different sites, it may generate messaging overhead when inherited methods are invoked. Further, if it is decided that instances and methods will be separated to exploit relative processing capabilities of different computing platforms, it may require expensive runtime migration of objects and attribute values. A distribution strategy must consider these issues. Further, the strategy may be complicated by the presence of an extremely large number of alternatives, typical of a distribution problem. Finally, it would be unfair to require the designer to guessimate how each issue may interact with the others to impact different decision criteria, such as cost, response time, storage, and communication cost or reliability. These criteria themselves may be different when the focus is on distribution across sites or within site; that is, across different processor types. The system distribution problem for object-oriented systems is, therefore, complex and difficult.

In prior research, the system distribution problem has been investigated for structured applications that use files or database tables $[8]$ . Research in the area of object distribution, on the other hand, has generally focused on implementation issues and low-level considerations, such as object clustering within primary memory and assembly of complex objects $[6]$ . Few object-oriented development approaches have addressed distribution at the design stage $[10]$ . Designers of object-oriented systems have no guidelines on which they may base their distribution decisions. This has lead to the use of simple heuristics for object distribution, resulting in systems that either do not exploit the distributed architecture fully or suffer from unfavorable cost/performance ratios. Generic guidelines for application splitting—data management, business logic and user interface—have been identified for some time $[15,7]$ , but rigorous approaches or computer-aided tools are still lacking.

Tools, such as Orbix [9], Forte [4], and Dynasty [2] facilitate management of distributed object oriented applications. However, their emphasis is on the mechanics of object distribution, and managing the deployment of distributed object-oriented applications. The decision as to how to partition and distribute the object-oriented application still rests with the designer. This remains a complex task for which effective support is generally lacking.

## 2. Distributing object oriented applications

The process of developing applications typically includes the phases of analysis, design, and implementation. The analysis phase generates a conceptual/logical specification of the application that is independent of the computing environment. During the design phase, the application designers make a number of decisions to ensure appropriate performance—including distribution of the application over the existing networked environment. Such an environment may consist geographically dispersed sites. Each site may contain multiple, possibly heterogeneous, processors connected by local area networks. A site can, thus, be characterized by the negligible interprocessor communication, compared to the significant communication penalties associated with across site transmissions.

Distribution across sites, therefore, requires identifying appropriate units (parts) of applications and allocating them to various sites in the geographically dispersed environment to minimize communication and storage costs. The units allocated to a site may require some adjustment, such as consolidation or further subdivision, for assignment to processors within each site. Such distribution (within each site) may need to satisfy criteria, such as lower processing costs, increased concurrency, and reduction in interprocessor flow, while maintaining an acceptable level of reliability.

The distribution approach needs to select a granularity level for the distributable units, such as large-grain (sub-system, applications), medium grain (classes, objects, sets of objects, methods) or fine-grained (char, objectid, line of code). The appropriate level is dictated by opportunities it provides for effective distribution. For example, the large grain model does not provide sufficient opportunities for effective distribution. At the other extreme, a fine grain model presents too many alternatives making the distribution problem intractable. The medium granularity model, with appropriate units of distribution, provides opportunities for effective distribution without making the problem intractable or causing implementation inefficiencies. The possibilities of distributable units for the medium grain model indicate a multitude of feasible units, including the partial or complete state of an object, collection of objects, the class template, methods implemented in the class template, and clusters of methods.

While the medium grain model is useful for distribution, information available about these is necessarily constrained by the stage at which distribution is attempted, i.e. the design phase. The task is aided somewhat by a key characteristic of object-oriented applications. Interactions among objects (i.e. messages and transmission of objects and attributes in response to them) are accomplished by following pointers, that is, implicitly joining, instead of performing explicit joins as in relational databases. This allows leveraging information about class interactions in a multitude of ways.

The final consideration for a distribution strategy is the degree of dynamism. While dynamic allocation is becoming feasible [16], object migration across heterogeneous systems is still difficult [12]. On the other hand, static allocation schemes have been implemented with favorable results. The distribution scheme we discuss here focuses on static distribution of an application $^{1}$ .

## 2.1. Object distribution methodology

Object distribution is heavily influenced by two key operational characteristics of object-oriented applications. First, communication costs represent an important element of cost during across-site distribution. Second, considerations, such as concurrent execution or best processor type match are important for within-site distribution, where the inter-processor communication penalty is insignificant. This provides a natural separation between the two. Accordingly, the object distribution methodology addresses the object distribution problem in two phases: Phase 1 addresses distribution across sites, with the objective of minimizing inter-site communication and storage costs; Phase 2 follows, addressing distribution within each site with the objectives of lower processing cost, increased concurrent processing, lower inter processor flow, and lower replication costs. Key inputs to the distribution methodology consist of the logical specification of the application (augmented with information, such as class cardinality), a description of the distributed environment, and usage patterns that specify how the application is used and the volume of activities. Fig. 1 outlines the distribution process.

## 2.1.1. Phase 1: distribution across sites

This phase consists of two major tasks: derivation of appropriate class fragments and their allocation to sites. Research for distributed relational databases provides a good starting point to address class fragmentation. The technique we have devised extends and adjusts the fragmentation process to ensure that data, methods, and superclass behaviors are retained together. The classes are partitioned using a horizontal partitioning strategy, i.e. individual objects are preserved with all attributes and methods intact. For example, the accounting department located on the East coast may only require information about employees on the East coast. The classes are, therefore, fragmented to satisfy one or more predicates, such as Region = “East coast”. A fragment of a class is defined by the application of one or more predicates.

The identification of predicates is driven by investigation of usage patterns. A semantic fragmentation strategy propagates fragmentation predicates to related classes to preserve the links between classes for fragmenting a class. If multiple attributes are selected, the result is a simultaneous application of independent predicates. Applying predicates from an attribute can result in fragments appropriate for different usage patterns providing better allocation opportunities and improving the potential for local access. On the other hand, applying too many attributes can lead to too many or very small fragments. An algorithm has been devised that maximizes the potential for local access, subject to designer-specified limits on undesirable consequences, such as too many or too small fragments. The fragments generated in this process represent the distributable units that need to be allocated to sites. Fig. 2 shows fragments of the class ‘Order.’

A mathematical programming model that minimizes inter-site communication helps allocate these class fragments to sites. The model distinguishes between retrieve and update operations—since replication reduces retrieval costs while increasing update costs. A key input to the model is inter-fragment traffic. This is estimated by exploiting the usage patterns and the notion of implicit joins. The allocation model then generates and evaluates various allocation possibilities. Since each specific allocation realizes a specific aggregate traffic across sites generated by fragments allocated to these sites, the model suggests an allocation that minimizes the aggregate traffic. Designer-specified constraints ensure that processors and storage capacity needed is available at the site. Two alternative update schemes, a nearest neighbor update and a global update, are supported in the model. In the nearest neighbor scheme, the closest available copy makes the update. In the global update scheme, a single copy is responsible for updating all copies. The models are formulated as an integer-programming models, which can be solved by any commercial solver $[13]$ .

<table><tr><td>Object Fragment</td><td>Underlying Predicates</td></tr><tr><td>F1</td><td>11,21,31</td></tr><tr><td>F2</td><td>11,21,32</td></tr><tr><td>F3</td><td>11,22,31</td></tr><tr><td>F4</td><td>11,22,32</td></tr><tr><td>F5</td><td>12,21,31</td></tr><tr><td>F6</td><td>12,21,32</td></tr><tr><td>F7</td><td>12,22,31</td></tr><tr><td>F8</td><td>12,22,32</td></tr><tr><td>F9</td><td>13,21,31</td></tr><tr><td>F10</td><td>13,21,32</td></tr><tr><td>F11</td><td>13,22,31</td></tr><tr><td>F12</td><td>13,22,32</td></tr></table>

![](/api/attachments/E8CEB8AN/fulltext/images/6c60775d3452343e579a7101539a9578b9a145648312f09a05e35d01782f1c8e.jpg)  
Fig. 1. Object distribution methodology.

![](/api/attachments/E8CEB8AN/fulltext/images/d6d2b437938a53f59644124b7992cde395d26f7a5c4c41b09f30b9f98dbbe7a6.jpg)  
Fig. 2. Distributable units in Phase 1.

## 2.1.2. Phase 2: distribution within each site

The focus in this phase is on distribution within each site. It too has two major tasks: derivation of appropriate units of assignment and assignment of these units to processors within each site. The class fragments allocated to each site in the first phase represent the starting point. These, however, represent fragments from merged classes. The lower inter-processor communication penalties within the site make it feasible to exploit subclass–superclass and method–instance separation to gain benefits, such as concurrency potential or processing efficiencies across the diverse processors.

To create appropriate distributable units, fragments from the merged classes are, therefore, separated into super- and sub-classes. The adjusted fragments are further separated into object instances and methods that may demand different processing requirements. For example, methods requiring extensive computation can be better processed on a mainframe, while user interface methods can be placed on workstations. To keep the problem tractable, and to exploit the default assignments, similar methods can also be grouped together. Similarly, data related methods implementing actions, such as access/update of attribute values or deletion/creation of object instances, can be retained with object instances. Processing-intensive related methods performing transaction processing, report generation, or extensive computation cannot have such default assignments and must, therefore, be considered separately for distribution. Fig. 3 shows the distributable units used in this phase.

![](/api/attachments/E8CEB8AN/fulltext/images/b13cc211a8368f75ebda7f0b1c3a2a9f3cfdad4461fedca8a9143d369f9d885b.jpg)  
Fig. 3. Distributable units in Phase 2.

Using these distributable units and exploiting the usage patterns, a number of decision criteria are then formalized. These include match (between processor capabilities and processing requirements), concurrency potential (among fragments), flow (between methods and fragments and across fragments) and replication penalties. Operationalization of these criteria also takes into account the networked environment within each site, which may consist of several diverse processors, such as desktops, servers, and host machines connected in various configurations, such as LANs, backbone networks, etc. We use two significant properties to model these environments: heterogeneity of processing elements $[3]$ and network layers to capture inter-processor communications $[1]$ . Finally, to deal with the conflicting criteria and the large search space, a multi-criteria decision-making technique is devised that assists the designer in arriving at a satisfying solution to the assignment problem $[14]$ .

## 3. The object distribution environment (ODE) prototype

The approach is implemented in the form of a design tool named object distribution environment (ODE). The prototype was developed in a Windows $^{TM}$ environment. The complex numerical computations for class fragmentation, traffic estimation criteria operationalizations were implemented in C, the linear programming optimization routines were coded in general algebraic modeling language (GAMS), and the interface and data was managed using ObjectPAL and a relational DBMS environment. Fig. 4 shows the architecture of ODE. The functioning of the tool is illustrated here with the help of screen shots. The data in the screen shots refer to a real world application of the tool in a large midwestern corporation.

The opening screen contains three options: the first permits the designer to specify or modify the object-oriented application and the distributed computing environment; the other two allow the designer to run Phase 1 and Phase 2 of the distribution process. This version of the tool allows the designer to enter logical specification of the application via a user-friendly interface. As the prototype improves, we expect to add the capability to read in the logical specification directly from existing CASE tools. The designer can then be queried for additional information, such as number of instances for classes or number of values for multi-valued attributes. The prototype uses a similar user-friendly set of dialogs to allow definition of the distributed computing environment. The designer can specify the network architecture by defining sites, distances between sites, processor types available at the sites and their layering within sites.

![](/api/attachments/E8CEB8AN/fulltext/images/e6143ef21551da28c0184e418e9581035f4e4d67af54d0d57d86b644e0f79888.jpg)  
Fig. 4. Architecture of ODE.

![](/api/attachments/E8CEB8AN/fulltext/images/e5c96083e60f9675a1ea57c2314aa0316c1e5d34dc2c6e78eeaef6cb2ffe14b0.jpg)  
Fig. 5. Specifying the distributed environment in ODE.

Fig. 5 illustrates the typical sequence of invocation by the designer.

The designer then specifies interaction patterns by identifying classes participating in the interaction and linking them in sequence. Multiple scenarios can be specified for each interaction pattern. This involves specifying frequencies with which the interaction is realized from different sites and by selecting attributes and predicates operating on these classes. This presents an opportunity to the designer to define an abbreviated but augmented picture of the sequence diagrams. Asking the designer for this information alleviates the burden of repeatedly asking him/her to produce estimates, such as traffic volumes, etc. Instead, these are compiled. Fig. 6 shows some screens used in this process. The data is added to the underlying repository.

A fragmentation procedure is then invoked by the designer. It first compiles predicates within one or more attributes for each class and exports the data to a grid evaluation algorithm, which generates successive combinations of attributes and evaluates the result of applying each combination. The evaluation can be refined by the designer by specifying different thresholds. The algorithm suggests acceptance of some attributes and discarding of others. The accepted attributes are then used to generate the fragments for each affected class. Fig. 7 shows the sequence of screens during the fragmentation process.

Using information available in the interaction diagrams and fragmentation decisions, another algorithm is then invoked to estimate data traffic between fragments. The estimates are used as input to the allocation model. The designer selects one of the two update schemes and invokes the optimization program. This completes the first phase.

A prerequisite to the second phase is definition of processor capabilities within each site. If these were not fully specified previously, they can be added at this stage. These ensure that the distributable units—object instances and methods—are assigned to appropriate processor types. As the first step, the units assigned to sites—class fragments—are adjusted for assignment within each site. This involves propagation of fragmentation criteria through the class hierarchy and separation of instance subsets and methods. Using information about interaction patterns, a number of different estimates are then computed; this becomes the basis for assigning distributable units to various processors in the site. These estimates include: match, concurrency, flow, and replication. A sequence of buttons makes these tasks transparent to the designer.

![](/api/attachments/E8CEB8AN/fulltext/images/4e03a273cc3672e2b993cf112030ccbe79e7541621990c63fb004358a11be78e.jpg)  
Fig. 6. Specifying usage patterns with ODE.

![](/api/attachments/E8CEB8AN/fulltext/images/93755482a1d4480edbd23966d4e6a1b50cae2e38a363a8778021fb3ea5af94a5.jpg)  
Fig. 7. Fragmenting classes with ODE.

The multiple criteria used during the within-site distribution process can be in conflict. The assignment process is, therefore, interactive and iterative. A specific assignment of instances and methods to processors can result in different valuation of these criteria. For example, if two instance fragments are used concurrently 100 times in various scenarios, separating them during the assignment can realize the concurrency. The designer can learn about these decision criteria along with the trade-off involved, as shown in Fig. 8.

A heuristic approach is used to explore this multidimensional decision space $[14]$ . First, ODE generates a sample of feasible solution vectors and computes the criteria values. The distribution of values characterizes the decision spaces for these, which are computed and retained for later analysis. The results are normalized to allow easier interpretation and comparison across decision criteria. Fig. 9 shows a typical display of decision space. This provides the designer a visual display of the decision space and can be valuable in making trade-offs between the criteria.

During the sampling, a filter is applied to check for non-dominance among the alternatives generated. The tool tracks these and retains a set of non-dominated solutions. To proceed with the decision process, the designer can simply select a non-dominated solution and probe the decision space around it by specifying tolerances for each criterion. ODE generates non-dominated solutions within the specified tolerances.

The designer can probe various promising areas until a satisfactory solution is obtained. The designer can also probe a region several times by specifying different tolerances. Solutions generated can also serve as additional seed points for further investigation.

The tool provides feedback by characterizing each region in terms, such as highs and averages for each criterion. Fig. 10 shows the investigation of a region with ODE.

The decision to stop rests with the designer. The tool aids this by providing feedback, such as the attractiveness of a solution in terms of improvement probability and risk of stopping using fuzzy probabilities.

## 4. Application of ODE

The tool was used for distribution of a moderate size marketing application in a midwestern corporation. The application involved four different sites connected by a wide area network. The architecture at each site contained three to four layers of networks. The logical specification of the application contained 16 major classes. The designers identified 14 interaction patterns, which were instantiated into 54 specific scenarios. During the first phase, the fragmentation step generated 61 fragments, fragmenting 12 classes. Some classes, such as 'Customer,' were fragmented on a single attribute, whereas other classes, such as 'Account' and 'Address,' were fragmented using multiple attributes.

The fragments, along with information about predicates, were used to generate a mapping between scenarios and fragments and compile estimates of data traffic. These inputs were used by the allocation model to allocate fragments to various sites. For this case, the storage cost was found to have insignificant influence on the allocation. The results of allocation showed that sites one and three had a higher concentration of fragments, while sites two and four had fewer fragments assigned to them. An analysis of the usage patterns revealed that sites one and three frequently initiated many transactions, which influenced the allocation. The model was executed for both ‘nearest neighbor’ and ‘global update’ strategies. The first resulted in a slightly higher level of replication probably due to slightly lower update costs compared to the ‘global update’ strategy.

During the second phase, the fragmentation criteria were propagated to subclasses to derive appropriate units for within-site assignment. For one of the sites, this resulted in 88 fragments (instance subsets). In addition, 31 processing-related methods were identified as distributable units. The multi-criteria decision-making model was used to assign the instance subsets and methods to processors within the site.

![](/api/attachments/E8CEB8AN/fulltext/images/430495d6d3174bd0ed8b98f8b924b5f01327e401597150b0fbf986c1cd1082f7.jpg)  
Fig. 8. Multiple distribution criteria for within-site distribution.

![](/api/attachments/E8CEB8AN/fulltext/images/1542037c458b2e427a4dd34bb705e0a1dae4d5daa62d4b438807e844a969ab65.jpg)  
Fig. 9. Decision spaces for multiple criteria within ODE.

![](/api/attachments/E8CEB8AN/fulltext/images/75d4395bfac854a331339b432051397e8cf70ecfcdc9435b2bc367538bed7dca.jpg)  
Fig. 10. Investigating a region with ODE.

The assignment process began by generating a large sample of solutions. These solutions were normalized and non-dominated solutions were graphically represented to characterize the decision space. The sampling run generated a sufficient number of non-dominated solutions to be used as starting points in probing various regions of decision space. In practice, we found that probing about five regions was sufficient. In the sessions conducted, only once was there need to generate, via sampling, additional non-dominated solutions, though probes of existing solutions often lead to the generation of additional non-dominated solutions. We also found that the characterization of the decision space provided the designer with valuable context to weigh the relative merits of alternative solutions. However, it was relatively difficult to form impressions about the trade-offs among the criteria by simple visual inspection of non-dominated solution pool (Table 1).

Finally, probes were conducted around promising candidates from the pool and also around promising candidates found during previous probes to narrow down the list. In the session reported here, the designer conducted nine such probes before selecting the final shortlist and the preferred solution. Fig. 11 shows the four finalists and the solution selected by the designer.

Table 1  
A sample non-dominated solutions pool

<table><tr><td></td><td>Solution no.</td><td>Match</td><td>Concurrency</td><td>Flow</td><td>Replication</td></tr><tr><td>1</td><td>30</td><td>69</td><td>59</td><td>29</td><td>59</td></tr><tr><td>2</td><td>121</td><td>26</td><td>79</td><td>79</td><td>65</td></tr><tr><td>3</td><td>351</td><td>73</td><td>61</td><td>28</td><td>73</td></tr><tr><td>4</td><td>381</td><td>08</td><td>20</td><td>72</td><td>73</td></tr><tr><td>5</td><td>775</td><td>66</td><td>56</td><td>58</td><td>32</td></tr><tr><td>6</td><td>937</td><td>50</td><td>33</td><td>72</td><td>59</td></tr><tr><td>7</td><td>961</td><td>78</td><td>14</td><td>32</td><td>42</td></tr><tr><td>8</td><td>973</td><td>77</td><td>37</td><td>48</td><td>43</td></tr><tr><td>9</td><td>983</td><td>53</td><td>43</td><td>58</td><td>47</td></tr><tr><td>10</td><td>986</td><td>55</td><td>40</td><td>68</td><td>47</td></tr><tr><td>11</td><td>973</td><td>64</td><td>31</td><td>57</td><td>35</td></tr></table>

![](/api/attachments/E8CEB8AN/fulltext/images/85e2931576d84b4f7f152cc8e0475cde02f8b89a89428b861b5ed4af99cdceab.jpg)  
Fig. 11. The final solution obtained with ODE.

## 5. Discussion and conclusions

As distributed object-oriented computing matures and architectures, such as CORBA, DCOM, Enterprise Java Beans, become popular, there is increasing interest in automated support for the design of distributed applications. The availability of tools for management of distributed objects, such as Orbix, Forte, Dynasty, etc. represents a step in the right direction. These facilitate the communication between multiple distributed objects, enabling seamless functioning of distributed object-oriented applications. Some provide support for client/server distribution employing coarse distribution criteria, i.e. structuring the application as fat-clients or thin-clients. However, they assume that the decision to partition and locate the object instances has been made. This is critical to the effective and efficient operation of the application.

This paper presented an overview of a tool that provides a comprehensive methodology for object distribution. The tool was designed to support distribution of business applications to be deployed in enterprises that conduct operations at multiple locations. It is likely that there will be overlap of activities at these locations with some unique processing at individual locations, e.g. regional sales and service of customers at branch locations and consolidation at headquarters. The tool allows the application designer to explore various distribution options, and provides a baseline assessment of candidate solutions. Selection of the final design is a decision that is shaped by criteria that are important to the designer and the enterprise. It should be stressed that there is no ‘optimal’ solution—rather, the final solution represents that which matches the designer and enterprise preferences the closest. The tool permits the designer to systematically explore the solution space to arrive at the most preferred distribution. Applying the approach for distribution of a real world application has revealed some shortcomings that we continue to pursue. These include addition of direct manipulation capabilities to enhance the multiple criteria decision support and the addition of an interface to existing CASE tools.

## Acknowledgements

We would like to express our acknowledgements to Tae-Dong Han for his comments on earlier drafts of this manuscript.

## References

[1] H. Bal, et al., Replication Techniques for Speeding up Parallel Applications on Distributed Systems, Final Report for Research Grant 125-30-10, submitted to The Netherlands Organization for Scientific Research, 1992.

[2] Dynasty 2001, Dynasty Technologies, Inc., Available on the World Wide Web at http://www.dynasty.com/.

[3] P. Ein-Dor, Grosch's law re-revisited: CPU power and the cost of computation, Communications of the ACM 28 (2), 1985, pp. 142–151.

[4] Forte, All About Forté V1.1, On the World Wide Web at http://decwww.epfl.ch/cdrom/html/Digital/Forte/default.html, 2001.

[5] J. Fedorowicz, A.O. Villeneuve, Studying object technology usage and benefits: A test of conventional wisdom, Information and Management 35 (6), 1999, pp. 331–344.

[6] O. Gruber, L. Amsaleg, Object clustering in Eos, in: Distributed Object Management, Morgan Kaufmann, CA, 1994, pp. 117–131.

[7] J. Hart, B. Rosenberg, Client/Server Strategies, Addison-Wesley, Reading, MA, 1995.

[8] A. Hevner, A. Rao, Distributed data allocation strategies, in: Advances in Computers, Vol. 27, 1988, pp. 121–155.

[9] Iona, Orbix: An Implementation of OMG's CORBA, On the World Wide Web at http://www.iona.ie: 8000/www/Orbix/orbix.html, 2001.

[10] K. Karlapalem, Q. Li, A Framework for class partitioning in object-oriented databases, Distributed and Parallel Databases 8 (3), 2000, pp. 333–366.

[11] T. McDonough, Getting where you want to go with objects, Methodology Mentor, Application Development Trends, 1999.

[12] U. Nestmann, A. Ravara, Semantics of objects as processes, in: A. M. D. Moreira, S. Demeyer (Eds.): Proceedings of the ECOOP'99, Lisbon, Portugal, June 14–18 1999, Lecture Notes in Computer Science, Vol. 1743, Springer, Berlin, 1999, pp. 314–325.

[13] S. Purao, H.K. Jain, D.L. Nazareth, An approach to distribution of object-oriented systems in loosely coupled networks, Journal of Management Information Systems, in preparation.

[14] S. Purao, H.K. Jain, D.L. Nazareth, Exploiting design information to derive object distribution schemes, Decision Support Systems 26 (3), 1999, pp. 225–249.

[15] A. Umar, Distributed Computing and Client/Server Systems, Prentice-Hall, 1993.

[16] O. Wolfson, Y. Huang, Competitive analysis of caching in distributed databases, IEEE Transactions on Parallel and Distributed Systems 9 (4), 1998, pp. 391–409.

![](/api/attachments/E8CEB8AN/fulltext/images/b68b14af105b4bac8a6a5ba273a0fc0d1b39a1fd01ec196ac0312a5bf7f47cce.jpg)  
Sandeep Purao is an Assistant Professor of computer information systems at Georgia State University. He holds a doctorate in management science from University of Wisconsin-Milwaukee. His research interests include system

development methods, reuse-based development, knowledge management for system development, system development processes, measurement for system development and pedagogical concerns in information system development. His work has appeared in several journals, including Communications of the ACM, Journal of Management Information Systems, Decision Support Systems, Information and Management, DataBase, and Journal of Education in MIS. He is a member of IEEE, ACM, and AIS.

![](/api/attachments/E8CEB8AN/fulltext/images/825cbfbcca22586b38f509a12e7b371c5ec8018cfb1c8ffb69ebf24fab9c1cef.jpg)

Hemant Jain is Tata Consulting Services Professor of Management Information System in the School of Business Administration at the University of Wisconsin-Milwaukee. Prof. Jain received his PhD in information system from Lehigh University in 1981, an M Tech in industrial engineering from IIT, Kharagpur (India) and BS in mechanical engineering from University of Indore (India). Prof. Jain's interests are in the

area of electronic commerce, system development using resuable components, distributed and co-operative computing systems, architecture design, database management and data warehousing, data mining and visualization. He has published large number of articles in leading journals like Information Systems Research, MIS Quarterly, IEEE Transactions on Software Engineering, Navel Research Quarterly, Decision Sciences, Decision Support Systems, Information and Management, etc. Prof. Jain is on the editorial board of the Information Technology and Management and is book review editor for Journal of Information Technology Cases and Applications.

![](/api/attachments/E8CEB8AN/fulltext/images/be5a84276e75849cdbe41c5cd96b4b4d749d5c43346d47d0b873c141007e8736.jpg)

Derek L. Nazareth is Associate Professor of management information systems at the University of Wisconsin-Milwaukee. He holds a PhD in management from Case Western Reserve University. His papers appear in Communications of the ACM, IEEE Transactions on Knowledge and Data Engineering, Decision Support Systems, Knowledge Acquisition, OMEGA among others. His current research interests include data ware-

housing, distributed object systems, web application development, and knowledge base verification. He is a member of AIS, ACM, IEEE Computer Society, INFORMS, and served as the Program Chair for AMCIS 1999.
