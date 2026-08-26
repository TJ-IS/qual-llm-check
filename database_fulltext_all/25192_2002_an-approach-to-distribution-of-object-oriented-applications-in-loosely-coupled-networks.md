---
otero_id: 25192
otero_key: "2793FRDE"
title: "An Approach to Distribution of Object-Oriented Applications in Loosely Coupled Networks"
authors: "Sandeep Purao; Hemant K. Jain; Derek L. Nazareth"
year: "2002"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2002.11045689"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An Approach to Distribution of Object-Oriented Applications in Loosely Coupled Networks

Sandeep Purao, Hemant K. Jain, Derek L. Nazareth

To cite this article: Sandeep Purao, Hemant K. Jain, Derek L. Nazareth (2002) An Approach to Distribution of Object-Oriented Applications in Loosely Coupled Networks, Journal of Management Information Systems, 18:3, 195-234, DOI: 10.1080/07421222.2002.11045689

To link to this article: http://dx.doi.org/10.1080/07421222.2002.11045689

![](/api/attachments/2793FRDE/fulltext/images/be2179b95afb13c5ee5b7b095f702cb6c52365c0916a6216d7c76c8926ee17de.jpg)

Published online: 09 Jan 2015.

![](/api/attachments/2793FRDE/fulltext/images/a11d2116e105394f6e5a06f209d3ef0ce6d986de0e41f961b606fd34b026afe2.jpg)

Submit your article to this journal

![](/api/attachments/2793FRDE/fulltext/images/14db7f586d0df9fa716acc0fc6ff8b840c4f8e1c2e5beb43c62e6d5f28d0083c.jpg)

Article views: 6

![](/api/attachments/2793FRDE/fulltext/images/5c6e64eebd016d7aa0f95567dc01ae74e08b20f637790039e00659ead13d9c89.jpg)

View related articles

# An Approach to Distribution of Object-Oriented Applications in Loosely Coupled Networks

SANDEEP PURAO, HEMANT K. JAIN, AND DEREK L. NAZARETH

SANDEEP PURAO is an assistant professor of Computer Information Systems at Georgia State University. He holds a doctorate in Management Science from University of Wisconsin–Milwaukee. His research interests include system development methods, reuse-based development, knowledge management for system development, system development processes, measurement for system development, and pedagogical concerns in information system development. His work has appeared in several journals, including Communications of the ACM, Journal of Management Information Systems, Decision Support Systems, Information & Management, DataBase, and Jour nal of Education for MIS. He is a member of IEEE, ACM, and AIS.

HEMANT JAIN is Tata Consulting Services Professor of Management Information System in the School of Business Administration at the University of Wisconsin–Milwaukee. Professor Jain received his Ph.D. in information systems from Lehigh University in 1981, an M.Tech in Industrial Engineering from I.I.T. Kharagpur (India), and a B.S. in Mechanical Engineering from the University of Indore (India). Jain’s interests are in the area of electronic commerce, system development using reusable components, distributed and cooperative computing systems, architecture design, database management and data warehousing, data mining, and visualization. He has published large number of articles in leading journals such as Information Systems Research, MIS Quarterly, IEEE Transactions on Software Engineering, Naval Research Quarterly, Decision Sciences, Decision Support Systems, Information & Management, and others. Professor Jain is on the editorial board of Information Technology & Management, and is book review editor for the Journal of Information Technology Cases & Applications.

DEREK L. NAZARETH is Associate Professor of Management Information Systems at the University of Wisconsin–Milwaukee. He holds a Ph.D. in Management from Case Western Reserve University. His papers appear in Communications of the ACM, IEEE Transactions on Knowledge and Data Engineering, Decision Support Systems, Knowledge Acquisition, and OMEGA, among others. His current research interests include data warehousing, distributed object systems, Web application development, and knowledge-base verification. He is a member of AIS, ACM, IEEE Computer Society, INFORMS, and served as the Program Chair for AMCIS 1999.

ABSTRACT: With the move to distributed systems and an increasing emphasis on the use of object-orientation for new system design, effective distribution of object-oriented applications is becoming an important concern for designers. Early research in this area has focused on object-clustering schemes for shared memory configuration that have limited value to business applications, which must be distributed over loosely coupled networks. These applications also exhibit the properties of simpler structural relationships and a large number of instances, demanding approaches closer to fragmentation and allocation instead of clustering. This paper develops an approach to distribution of object-oriented applications over geographically dispersed sites in loosely coupled networks—taking account of concerns such as encapsulation, inheritance, messaging, and implicit joins. The approach consists of two phases. First, we develop a scheme for generating class fragments, which ensures that encapsulation is not violated and inheritance is not stretched across sites. Second, considering the message-intensive operation of object-oriented systems, we devise models for allocation of class fragments to sites that minimize inter-site traffic. A nonarbitrary procedure to compile traffic volume estimates exploiting the notion of implicit joins in object-oriented applications provides the natural linkage between the two phases. A research prototype was implemented to establish feasibility of the proposals. We demonstrate usefulness of the approach by its application for distribution of a real-world information system.

KEY WORDS AND PHRASES: allocation models, distributed systems, horizontal frag mentation, object distribution, object-oriented development.

DISTRIBUTION OF SYSTEM COMPONENTS has been a concern of system designers for many years. To ensure acceptable performance within resource constraints, system designers need to deploy application components on different sites or platforms [71]. This involves (1) partitioning the system into appropriate distributable units, and (2) placing these units across existing networks of computers, in a manner that would maximize some measure(s) of performance or minimize cost or both. The problem has been investigated, in the context of traditional computing models such as filebased or database systems, by a number of researchers [39]. The state of the art in distributed object computing has not adequately dealt with this problem. Öszu et al. [60] indicate that “no work is done in [object distribution schemes] . . . , the major reason for this is that it is a very complicated problem.” A few distribution techniques, providing partial solutions, have been proposed [2, 4]. As an increasing number of applications are being designed with the object-oriented (OO) technology [43, 60] for deployment in corporate-wide infrastructures, few distribution approaches [1, 2, 3] are available for designers.

A few object-clustering schemes have been proposed [3, 14, 69]. However, their applicability to business information systems, such as inventory control or order processing, is suspect [64]. These systems have class models with relatively simple struc tural relationships and a large number of object instances that require deployment over loosely coupled networks. A few object-distribution techniques are also reported. They, however, provide only partial solutions [e.g., 2, 4, 71]. The objective of this paper is, therefore, to develop a comprehensive approach for distribution of business applications, designed with the object-oriented paradigm, in loosely coupled networks. At least two factors make this problem interesting and different from traditional data distribution approaches. First, it requires recognition and exploitation of key object-orientation properties, such as encapsulation and inheritance. Second, it requires a recasting of familiar problems fragmentation and allocation to take into account operational characteristics, such as messaging and implicit joins.

This paper first traces prior work in system distribution with particular emphasis on possible extensions of this research to OO applications. The third section discusses complexities introduced by object-orientation in the distribution process, formulates the underlying models, and outlines our plan to manipulate the information available in our distribution scheme. The fourth section addresses the first phase, fragmentation. It formulates surrogate measures for assessing the quality of fragments and presents a procedure for deriving appropriate class fragments. The fifth section addresses the second phase, allocation. It proposes a procedure for estimating messaging traffic and develops alternate allocation models. The sixth section describes implementation of the approach and its application to distribute a real-world OO system. The paper concludes with a brief discussion, known limitations of our approach, and proposed extensions.

## Previous Work in System Distribution

MUCH PRIOR RESEARCH HAS FOCUSED ON DISTRIBUTION in the context of relationa databases [13] following the two phases of fragmentation and allocation suggested by Ceri and Navathe [11]. The first phase, fragmentation, involves identification of appropriate distributable units, using vertical or horizontal fragmentation.<sup>1</sup> A number of approaches have been proposed for these including attribute affinity [40], exploitation of semantic dependencies [75], semantic fragmentation [51], use of information from user views of E-C-R (Entity-Category-Relationship) models to create candidate fragments [26, 37], and knowledge-based schemes [70]. The second phase, allocation [15], involves placement of fragments at appropriate platforms, to achieve goals such as locality of processing. Some researchers suggest tight coupling between the two phases [58], whereas others—typically those proposing semantic schemes—opt to decouple the two [37, 51, 70]. Solution approaches suggested for this phase include problem decomposition into a sequence of solvable linear models [53], combination of optimal techniques and heuristic algorithms [28], integer programming [62], and heuristic algorithms enhanced by interactive decision support [50]. Dowdy and Foster [23], Gavish [32], and Hevner and Rao [39] present comprehensive reviews of this research stream.

## Object Clustering

For OO systems, research on distribution strategies is still in its infancy [60]. Much research has focused on object clustering, that is, preserving associations between objects in the form of proximity within secondary storage—to ensure efficient retrieval and assembly of objects. This focus is comparable to early distributed relationa database research that emphasized allocation between primary and secondary memory [40]. In the absence of an accepted underlying model, and faced with complex struc tural relationships, research on object clustering has assumed an important role. A number of clustering schemes have been proposed, including semantic clustering [69], placement trees [5], inheritance-based clustering [14], stochastic clustering [72], leveled clustering [16], and user-defined clustering [36]. Detailed accounts and perfor mance analyses of these are available in [21, 22, 56].

The clustering schemes have proved useful for distribution of OO applications involving complex structural relationships and few object instances (such as, scientific applications) that do not need to be geographically distributed. On the other hand, many business applications exhibit structurally simpler data models with fairly shallow inheritance hierarchies. Many classes in such applications (such as Customer and Order), however, have a large number of instances. Their processing requirements can also be diverse such as intensive input/output, dedicated user-interaction or complex algorithmic processing. The clustering schemes do not take these into account, limiting their applicability to business applications.

## Object Distribution as an Extension of Data Distribution

Object distribution as an extension of relational database distribution has recently begun to emerge as a very complex problem [2, 60]. Although significant differences exist between relational and OO databases, the former has been posed as a special case of the latter [55], suggesting the possibility of extending data distribution research for developing fragmentation and allocation schemes for OO applications [47]. The basic modeling required for OO systems [73] can be framed as an extension of the entity-relationship model, making results from research on distributed relationa databases extendable for OO systems [49, pp. 120–126]. Any such extensions must, however, (1) accommodate OO constructs [36, 60], and (2) take appropriate account of properties of OO systems that may significantly affect the distribution schemes [47], particularly in the context of business applications.

Few such extensions have been reported. Karlapalem et al. [47] discuss objectdistribution issues and present possibilities for fragmentation present algorithms for vertical class fragmentation [30]. Bellatreche et al. [2, 3, 4] present a series of algorithms aimed at partitioning classes, which come closest in spirit to our focus. Their proposals, however, address partitioning for efficient access of pages from secondary memory and require information that may not be easily available during the design stage. Ezeife and Barker [27] propose an algorithm, using a technique similar to attribute affinities, for vertical class fragmentation. Malinowski and Chakravarty [55] report an algorithm for vertical fragmentation of classes. None of these proposals, however, include an allocation procedure. Stoyenko et al. [71], on the other hand, present a technique for allocation of objects to minimize communications, based on a graph partitioning heuristic. Their approach assumes availability of the distributable units, and makes a number of assumptions regarding execution and communication costs, which can be hard to estimate in practice.

The shortcomings observed, thus, form the motivation for research we present in this paper. First, we propose to develop an approach that addresses object distribution for business applications, that is, simpler structures with a large number of instances. Second, we address object distribution in loosely coupled networks instead of clustering in secondary storage. Finally, we propose to devise a complete approach covering both fragmentation and allocation.

## Object Distribution in Loosely Coupled Networks

A LOOSELY COUPLED NETWORK consists of sites connected by wide area network technology. Each site in the network denotes a geographical location, where an organizational unit, such as a branch office or a factory, may be located. The wide area network—connecting the sites—is subject to the penalties of higher communication costs, slower response times, and lower reliability, determining the boundary around a site. With improvements in speeds, the wide area networks are getting closer in performance to local networks. In particular, costs have dropped and reliability has increased. However, the distinction between intranets and extranets remains, as the latter often cannot be controlled by the organization. This is particularly true when delays are experienced due to net congestion or widely varying levels of quality of service are observed, lowering reliability.

A distributed application may need to run at several such sites due to the exigencies of business, and may have substantial communication requirements. Although some site-to-site communication is dictated by the business requirements, distribution of the application components over the network can greatly influence the overall communication and the ensuing penalties. The key criterion for distribution, therefore, is maximization of locality of processing. An object-distribution strategy in loosely coupled networks, therefore, must (1) derive appropriate distributable units, and (2) place these at appropriate sites—with the goal of maximizing the locality of processing at each site. Figure 1 outlines these requirements.

Support technologies such as CORBA [59], and products such as Dynasty [24], Forte [29], and Orbix [42], are available, which provide mechanisms such as naming and routing of messages to local and remote objects [61], facilitating implementation of distribution results. Distribution can, therefore, be tackled during the design stage, without being constrained by specific packages or languages used for implementation. Such initial, static-distribution schemes<sup>2</sup> for data and task allocation have been proposed and implemented in the past with impressive results. Arguably, the ideal scheme is an initial static distribution, coupled with a monitoring mechanism to refine the decisions as needed. The approach we plan to develop is aimed at providing such an initial distribution during the design stage. We must, therefore, exploit infor mation available at the design stage without making unreasonable demands abou information that may be available only after the system is implemented.

![](/api/attachments/2793FRDE/fulltext/images/88157476c9050892ec7790a5001d896956ccad3f1cf3c5461d4cd6482362e6df.jpg)  
Figure 1. Distribution in Loosely Coupled Networks

## The Computing Infrastructure and Application Models

The existing computing infrastructure and the application being designed clearly form the two key inputs to the distribution process. The first specifies the distribution platforms and their arrangement; the second specifies the application to be distributed.

## The Computing Infrastructure

The computing infrastructure specifies computing resources at each site and interconnections across these sites [7]. We model the computing resources at each site as the availability of processor types [25, 35] and processing capabilities at sites. For example, a site may contain processing capabilities, such as a video server, which may be needed by some classes. These are modeled as “special processing capabili ties.” Interconnections across sites are modeled as the “traversal penalty” between every pair of sites, treating it as a surrogate representation of preference (for the “local” site) among competing “remote” sites. For instance, consider sites Atlanta (A), Boston (B), and Chicago (C). It is conceivable that from A’s perspective the link to C is faster than that to B. In this case, traversing link A–C will be preferred over traversing link A–B. The traversal penalty in our model, therefore, represents a surrogate for the preference between competing “remote” sites, not the physical distance. This is consistent with the dominant communication paradigm where WAN services are purchased from a provider, with price and service level agreements.

Channel capacity and channel load, although important to the WAN service provider, are not appropriate constructs in our model. First, additional capacity, although expensive, can be easily purchased, within reasonable limits, from a WAN provider Second, our distribution approach is focused on a single application, which may require a certain bandwidth, but capacity and load are affected by the aggregate re quirements of the applications portfolio. The capacity costs, therefore, represent fixed costs. Punishing a single application with the fixed cost of adding extra capacity would, therefore, be inappropriate. The total capacity costs may be allocated across applications in some form using a charge-back or other scheme, adjusting the per unit cost apportioned to each application. The notation below captures the discussion. The traversal penalty (trav) captures the relative attractiveness of remote sites from the perspective of each site. The processor type availability (type) and processing capability (char) is attributed to each site.

k Î L = Sites

$\mathbf { t } \in \mathrm { ~ T ~ }$ = Processor types

$\mathbf { r } \in \textbf { R }$ = Special processing capabilities

$\mathrm { T r a v } _ { \mathrm { k l } }$ = Traversal penalty for remote access between sites k and l

$\mathrm { T y p e } _ { \mathrm { k t } }$ = Availability of processor type t at site k, {0,1}

$\mathrm { C h a r } _ { \mathrm { k r } }$ = Availability of special processing capability r at site k, {0,1}.

## Application Models

The logical specification of the OO application [24, 29, 42] represents the primary source of information that can be exploited for distribution at the design stage. It consists of a structural model with classes, attributes and methods, and different types of relationships [9, 44, 67]. It includes a representation of the application that is relatively technology-independent. Although the eventual implementation must respect the technologies, the distribution process need not be burdened with these details.<sup>3</sup> Our approach, therefore, is similar to the separation between logical and physica design.<sup>4</sup> The methods are specified with the object.method syntax, but the complete method code is not available at this stage. The execution is expected to involve method invocations [74] accompanied by the required arguments, if any, which would block the calling process, spawn a new one, and return objects (or values), if any, to the caller. The model is similar to that suggested by other researchers [71] with the restriction that only information reasonably expected to be available at the design stage is considered. The model also recognizes implicit joins [10], which allow traversal across objects via references or pointers without requiring a primary key—foreign key search and explicit join. The messaging operations can, therefore, be accomplished without being bothered by the most expensive operation in relational database systems viz. joins. Finally, for the purpose of distribution, the model is augmented by including information such as expected cardinalities for classes and multi-valued attributes, if any.

## Distributable Units

Several candidate distributable units can be identified from the logical specification [8, 64]. Chin and Chanson [18] suggest three broad anchor points for considering the granularity continuum—the two extremes, coarse (such as, subsystems) and fine granularity (such as, individual attributes or program statements) and the center, medium granularity, which suggests units such as classes, methods, and instance sets. Considerations for determining the appropriate granularity include: the potential for distribution opportunities and availability of information at the design stage.

## Granularity

The fine grain model provides ample opportunities for distribution, and is appropriate for partitioning between primary and secondary memory or even for distributing among tightly coupled processors. However, considering fine-grain units such as a line of code or individual objects can present a significant burden, especially for applications with a large number of object instances, since recognizing and managing them can require considerable processing overhead. It can also increase the size of the distribution model, making the problem intractable. Further, detailed information necessary for considering fine-grain units as distributable units cannot be assumed at the design stage. The other extreme, coarse-grain units such as subsystems are rela tively easier to identify, and information about these can be obtained easily. How ever, the potential distribution opportunities these coarse-grain units provided are minimal. Typically, only a few subsystems may be identified for an application, restricting the ability to allocate or replicate different application components. The reduced potential for distribution opportunities renders this alternative ineffective. Medium-grain units—such as classes, instance sets or methods—provide semantically meaningful units that do not involve exceedingly inefficient operations, yet provide adequate opportunities for distribution. Much of the information to identif the medium-grain units is also available in the logical specification. Many classes, thus, present themselves as ideal distributable units. However, classes that contain a large number of instances may still be too coarse. For example, in some organizations, the Order class contains millions of instances, different subsets of which may be needed at different sites. Such classes can then be fragmented to derive meaningful medium-grain units.

## Class Fragmentation

The decision to fragment a class can, however, make it difficult and expensive to maintain encapsulation, depending upon the nature of fragmentation. For example, if it leads to method-attribute separation, it could lead to performance degradation, due to remote method invocations. Although such separation may be acceptable, or even desirable, within a site (or for clustering, such as [31]), it is not a reasonable choice in loosely coupled networks. As a second possibility, if fragments comprise subsets of attributes (similar to [27, 55]), they may be augmented by bundling appropriate methods using a measure such as method-attribute-usage (such as LCOM [17] or affinity [27, 30]). However, unless completely nonoverlapping sets of methods can be identified, such fragmentation could lead to problems similar to those faced under the first choice. In both cases, code replication may alleviate the problem. However, the more important concern will remain. Neither choice will address partitioning of the large number of instances that a class may contain. To address this concern, a third alternative, horizontal fragmentation, is more appropriate.

With horizontal fragmentation, a fragment comprises a subset of instances, and all methods are replicated with each fragment, avoiding remote method invocations. A related concern, clearly, is the effect of inheritance [68, 74]. If the classes and subclasses are kept separate during fragmentation, remote-method invocation may be necessary after implementation, degrading performance. Again, code replication may alleviate this concern, but separation of the class hierarchy may lead to unintended breaking up of instances, that is, virtual vertical fragmentation. For example, if the class hierarchy Customer–Corporate Customer is separated, each instance of Corporate Customer will be broken up as values for some of its attributes will be located with the class Customer, and for some other attributes will be located with the class Corporate Customer. For business applications with a large number of instances, this can become a particularly severe problem due to the large number of instances. An alternative is to collapse class hierarchies so that classes at either the first level of classification (in our example, class Customer) or the last level of classification can be considered for fragmentation (in our example, classes Corporate Customer and, say, Government Customer). We, therefore, recommend one of these as a precursor to fragmentation. Considering the convention of treating non-leaf classes as abstract classes [67], and the low values for the depth of inheritance metric observed in practice (DIT [depth of inheritance tree] median of one and three [38, 54]), it represents an appropriate choice. The collapsing is solely for the purpose of distribution—it neither indicates nor warrants such merging for actual implementation of the OO system.<sup>5</sup> Figure 2 captures the choices outlined above and clearly identifies the distributable units.

## Application Behavior

Another key input to the distribution process is the expected behavior of the application. Arrival rates [46], traffic value between sites, communication flow between files [45, 63], execution and communication costs [71] and so on, are often required from the designers. Accurate estimates of these parameters are, in fact, crucial for effective distribution. The values of these parameters are often obtained by requesting application designers to provide best-guess estimates. Such estimating is quite difficult, since it depends on factors, such as degree of replication and routing strategies employed. Relying on designer input for these parameters (such as, number of bytes transferred between sites Aand B) can place undue burden on application designers and can result in grossly inaccurate estimates that underlie (and undermine) sophisticated distribution approaches [45, 71]. On the other hand, if information that is more naturally available from the designers is exploited to estimate the required parameters, the resulting distribution is likely to be more reliable. For example, it is easier for the designer to specify that orders of books from the East Coast, which represent abou 20 percent of our orders, are shipped from our Atlanta warehouse. Currently, there are no objective approaches that we know of, to estimate the distribution parameters from such readily available information. We propose to make this possible by exploiting information about expected application behavior, specified as interaction patterns.

![](/api/attachments/2793FRDE/fulltext/images/ba0adef21da48246a4b9b3a027c630081453fadbb0068b07d1f7f2775d3f0b97.jpg)  
Figure 2. Deriving Distributable Units

## Interaction Patterns

An interaction pattern specifies interactions among classes as a result of a trigger initiated in the environment. A number of schemes have been proposed to capture and depict interactions in OO applications [9, 67]. Since these are often suggested as a means of collecting and documenting system requirements [9], they are generally easy to specify. Typically, they contain an expected subgraph representation of interactions among objects as message exchanges and responses.

To capture the interactions, we use the collaboration diagrams [9] and use cases that have been created as part of the application design [44]. This representation allows the designer to specify interactions with minimum implementation-specific information. The notation and technique (similar to [41]), allows specification of classes as participants in the interaction. After an “interaction pattern” is specified, with par ticipating classes and messaging among them, such as requesting information or updating attributes, it can be instantiated, as necessary, into several “scenarios,” each containing additional information, such as initiating site(s), frequency(ies), and condition(s), for identifying instances affected by the scenario. Figure 3 demonstrates the Create Customer Order interaction pattern and a related scenario.

![](/api/attachments/2793FRDE/fulltext/images/439db273f83e07482c6a419fd00a22e9072ef5cd720e3f5c345897d0a759ac59.jpg)  
Figure 3. Interaction Patterns and Scenarios

It indicates that an external trigger first invokes the Customer class, which queries the Cust\_Credit and Product classes, and then updates the Order class. Items ordered are then added in the Orderline class, and the Product class is updated to reflect amounts committed for this order. The scenario Create Customer Order for California Customers indicates the initiating site: Los Angeles, frequency: 500, and provides the condition: $S t a t e = { \bf \nabla } ^ { \cdot } C A ^ { \prime }$ for identifying affected instances of the class Customer. The notation below captures the discussion. The set S denotes the scenarios. The variable “importance” allows the designer to specify some scenarios as more important than others to dictate distribution. During our application of the approach, we did not vary the importance, retaining it as one for all scenarios. The variable “frequency” represents how often the scenario is initiated from a site s. Finally, the variable “use” indicates whether a scenario uses a condition (called predicate, denoted by the set P), from an attribute (denoted by the set N).

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
s ∈ S = Scenarios
Importance $_{s}$  = Importance of scenario s
Frequency $_{sk}$  = Frequency of scenario s from site k
p ∈ P = Predicates
n ∈ N = Fragmentation Attributes
Use $_{snp}$  = Scenario s uses predicate p of attribute n, {0,1}.
</div>

Our proposal for, and use of, the interaction patterns differs from that of Stoyenko et al. [71], who model the implemented application as a single directed acyclic graph (DAG), representing the entire application by making a number of assumptions [71, p. 120]. The interaction patterns we propose allow us to create multiple graphica views of the application based on the limited information available at the design stage. Coupled with the construct of implicit joins, the collection of interaction patterns and scenarios provides a way to compile the necessary distribution parameters we describe next.

## Fragmentation

FRAGMENTATION, THE FIRST PHASE of the distribution process (Figure 1), consists of models and techniques to arrive at appropriate distributable units (Figure 2), that is, horizontal class fragments. Horizontal class fragmentation resembles relational data fragmentation with a few key differences. First is the prevalence of implicit joins [10]. Unlike relational databases, where “joins” are the most expensive operation, the use of references make joins largely unnecessary for OO applications. Instead, messaging becomes the most important operation. Second, OO data models include inheritance. Following the rationale presented earlier (see “Distributable Units” section), we use classes at a single level of classification as candidates for fragmentation, either promoting up or rolling down the hierarchy for the purpose of distribution. Third, OO applications include methods (requiring encapsulation) and complex attributes. Encapsulation is ensured using code replication as reasoned earlier (see “Distributable Units”). For complex or multi-valued attributes, we exploit designer input that augments the logical specification (see “Distributable Units”). In spite of these differences, the overriding goal of class fragmentation is similar to that of relation fragmentation—ensuring maximization of “locality.” Locality refers to the ability to conduct an operation, such as, an access or an update within a site, without requiring traversal of an inter-site network link. The success of a horizontal fragmentation scheme is reflected in its ability to preserve opportunities for such allocation.

## Deriving Horizontal Class Fragments

A horizontal fragment is defined by predicates that place conditions on attribute values resulting in subsets of instances. Since the attribute values can be discrete or continuous, characterization of the search space of potentially beneficial horizonta partitions can be difficult [39]. The difficulty is caused by the very nature of the horizontal fragmentation problem, which involves breaking up a class to create appropriate fragments (as opposed to vertical fragmentation, which involves clustering available attributes into appropriate partitions). As a result, few measures or algorithms have been suggested for quantifying or evaluating the benefits or costs of fragmentation. Research on “appropriateness” of horizontal fragmentation is almost nonexistent. Many researchers [12, 69] have acknowledged the difficulty of determining appropriate horizontal fragments, since a good scheme requires a coordinated application of semantic properties such as predicate values, and statistical properties such as expected number of accesses or updates. Most horizontal fragmentation schemes for relational databases have focused on the use of semantic information, disregarding statistical information, which has been exploited for vertical fragmentation of relational data [58] as well as OO data [27, 55]. When researchers have exploited statistical information [2], they have often disregarded the semantic aspects, treating it as an add-on algorithm for related classes [3].

![](/api/attachments/2793FRDE/fulltext/images/dfdf8554f5f01b5f865935f09d063ed38f03735d4e52f70eff95f301a4adb021.jpg)  
Figure 4. Fragmentation Procedure

The procedure we have devised recognizes this duality and uses both types of information to derive appropriate horizontal fragments. Examples of relevant semantic information include instance sets identified by the predicates (that is, attribute-value pairs), such as Cust\_ $T y p e = \cdot { \cal C } o r p o r a t e ^ { , }$ or Cust $\mathit { . } \mathit { T y p e } = \mathit { \cdot } \mathit { I n d i v i d u a l } ^ { \mathrm { , } }$ for the class Customer or the instance sets identified by the same two predicates for the related class Order. An example of relevant statistical information is frequencies indicated for the different scenarios, such as 500 for the scenario “Create Orders for Customers in California.” Figure 4 presents an overview of the proposed fragmentation procedure, using both semantic and statistical information, that includes the steps (1) compilation, and (2) evaluation, which are described next.

## Compiling Candidate Fragmentation Criteria

The first step compiles candidate fragmentation criteria based on information available in the scenarios. For example, the interaction pattern Create Customer Order may have two scenarios: “Create Customer Order for California Customers” and “Create Customer Order for Wisconsin Customers.” Based on this information, the designer may have specified partitioning predicates for the class Customer, $C u s t o m e r . S t a t e = \cdot C A ^ { \prime }$ and $C u s t o m e r . S t a t e = \cdot W I , ^ { \prime }$ respectively, along with the estimated selectivities at 60 percent and 25 percent. Generally, the predicates are specified for the class initiating the interaction pattern, although it is possible that they may involve other classes in the interaction pattern. For example, another scenario of the “Create Customer Order” pattern may be “Create Large Orders,” yielding the criteria $[ O r d e r . T o t a l \ge 1 0 0 , 0 0 0 ]$ and $[ O r d e r . T o t a l < 1 0 0 , 0 0 0 ]$ for the class Order. For a complex scenario, the designer may have knowledge of many predicates, for many different classes in the interaction pattern, say, for a scenario such as “Create Small Orders for Privileged Customers.” It may be neither desirable nor feasible to consider all predicates for fragmentation. Designer experience and judgment is invaluable here to ensure that only the important predicates will be used. For example, a scenario may require predicates such as $[ O r d e r . T o t a l \ge 1 0 0 ] , [ P r o d u c t . T y p e = \mathrm { ` B o o k ` ] }$ , and [Order.type $= \cdot \mathrm { G i f t } ^ { \prime } ]$ . The judgment to use or ignore any of these must lie with the designer. A mechanical algorithm cannot make such “common-sense” judgments. Addition of se mantic and statistical information does not make this task any easier or more difficult, as the designer can continue to specify the predicates with phrases such as “customers from California, which account for about 30 percent of our customer base,” that is, $[ C u s t o m e r . S t a t e = ^ { \cdot } \mathrm { C A ^ { \prime } } ]$ . Generally, important attributes that can be used for fragmentation are not large in number and the designers are aware of the selectivities. Further, if an earlier version of the system or data needed for the system has been implemented, it can also be queried to find these answers such as “select \* from customer where state $\mathbf { \mu } = \cdot \mathbf { C A } . \mathbf { \mu } ^ { \mathsf { 3 } \mathsf { 5 } }$ The notation below captures the discussion. The sets N and P represent the fragmentation attributes and predicates respectively (shown earlier when discussing application behavior [“The Computing Infrastructure and Application Models”], and are repeated here for ease of reference). The variable “select” records the membership of predicates in attributes and stores the selectivity of the predicate value.

n Î N = Fragmentation Attributes

p Î P = Partitioning Predicates

Select = Selectivity of predicate p of attribute k, selec $\mathbf { t } _ { \mathrm { k p } } \in [ 0 , 1 ]$

## Propagating Predicates

The predicates gathered from all scenarios of all interaction patterns are then propagated to other classes participating in the interaction pattern in a manner resembling semantic fragmentation in relational database [50]. This propagation may not occur for all classes in the interaction pattern, depending on the association cardinality or semantics of the interaction pattern. For example, in the Create Customer Order interaction pattern, it is appropriate to propagate predicates $\begin{array} { r } { [ C u s t o m e r . S t a t e = \ ^ { \cdot } C A ^ { \prime } \ } \end{array}$ ] and $\left[ C u s t o m e r . S t a t e = \right. \left. ^ { \cdot } W I ^ { \prime } \right]$ to the Order and Cust\_Credit classes, but not to the Product class. In some cases, the propagation may occur to several levels, for example, propagation to the Orderline class.

## Compiling Fragmentation Attributes

The predicates identified for each class are compiled to create fragmentation attributes. The compilation may involve some refinement to ensure that the predicates are mutually exclusive and exhaustive. For example, consider the class Customer. It may have predicates $[ S t a t e = \cdot { C A } ^ { \prime } ]$ and $[ S t a t e = \cdot \mathbf { W } I ^ { \prime } ]$ from one pattern, and the predicates $[ S t a t e = \cdot { H I } ^ { \prime } ]$ and $[ S t a t e \neq \cdot H I ^ { \prime } ]$ from a different pattern. These will be compiled to create a fragmentation attribute State for the class, with predicates $[ S t a t e = { } ^ { \cdot } C A { } ^ { \cdot } ]$ $[ S t a t e = \cdot W I ^ { \prime } ] , [ S t a t e = \cdot  H I ^ { \prime } ]$ , and [State NOT IN $( ^ { \cdot } C A , ^ { \cdot } W I , ^ { \cdot } H I ^ { \cdot } ) ]$ . The residual predicate, ‘State NOT IN’ will contain instances left over after removing those satisfying other predicates. Similarly, the Order class may have predicates $[ A m o u n t \geq$ 100,000], [Amount $< \ 1 0 0 , 0 0 0 ]$ , as well as propagated predicates such as $[ C u s t o m e r . S t a t e = \ ^ { \cdot } C A ^ { \prime } ]$ $\left[ C u s t o m e r . S t a t e = \cdot \right. W I ^ { \prime } ]$ $[ C u s t o m e r . S t a t e = \cdot H I ^ { \prime } ]$ , and so on. These will be compiled to create the fragmentation attributes Amount and Customer.State for the class Order.

The computation of the residual may require input from the designer. This is true in the case of fragmentation attributes where the values of predicates are textual. For instance, consider the attribute Student.Status.Knowing the permissible values (such as, in a given case, Freshman, Sophomore, Junior, and Senior) will inevitably require some domain knowledge that can assist in the formulation of the residual predicate. If the values are numerical, knowing the range (high and low) the gaps may be mechanically filled in by examining the available predicates. For example, the attribute Order.Amount with predicates such as $\left[ O r d e r . A m o u n t < 1 , 0 0 0 \right]$ , and $[ \dots < 1 0 0 , 0 0 0 ]$ the compilation can result in predicates $[ \ldots < 1 , 0 0 0 ] , [ \ldots \geq 1 , 0 0 0 \mathrm { a n d } < 1 0 0 , 0 0 0 ]$ , and $[ \dots \geq 1 0 0 , 0 0 0 ]$ , the last predicate serving as the residual.

Each resulting candidate fragmentation attribute (such as, Customer:State Order:Amount, Order:Customer:State) is capable of creating mutually exclusive fragments of the specified class. Figure 5 illustrates several candidates for Order, derived from multiple scenarios of the “Create Customer Order” interaction pattern.

## Evaluation and Choice

Since a number of candidate fragmentation attributes may be available for fragmentation of a class, the next logical step is selection from the available attributes. If multiple attributes are selected, predicates from different attributes are superimposed. The number of fragments generated is, therefore, a product of the number of predicates in each selected attribute. Each combination of fragmentation attributes will generate different fragments. For example, if the fragmentation attributes Customer:State, OrdTotal, and Status (see Figure 5) are selected, the result would be 12 fragments of the class Order, including ${ \bf F 1 : } ~ [ C S t a t e = { \bf \nabla } ^ { \cdot } C A ^ { \prime } ] \wedge [ O r d T o t a l > =$ $1 0 0 , 0 0 0 ] \wedge [ C S t a t u s = " P r i \nu i l e g e d ^ { \prime } ] , { \bf F } 2 \colon [ C S t a t e = " C A ^ { \prime } ] \wedge [ O r d T o t a l > = 1 0 0 , 0 0 0 ] \wedge$ $[ C S t a t u s = O t h e r ] , \mathbf { F 3 : } \ [ C S t a t e = \ ^ { \ast } C A ^ { \prime } ] \wedge [ A m o u n t < 1 0 0 , 0 0 0 ] \wedge [ C S t a t u s = \cdot P r i \nu i - \cdot \ \wedge \ \wedge \ \wedge \ ]$ leged’], ${ \bf F 4 : } \ [ C S t a t e = \ ^ { * } C A ^ { \prime } ] \wedge [ A m o u n t < 1 0 0 , 0 0 0 ] \wedge [ C S t a t u s = \ ^ { * } P r i \nu i l e g e d ^ { \prime } ]$ (see Figure 6).

![](/api/attachments/2793FRDE/fulltext/images/bc17c0d8644c636bb46f0203ed60a2cd4fdfdc5b56bf6568b6f4cbcc338c7277.jpg)

![](/api/attachments/2793FRDE/fulltext/images/47756e9177733d8f259b0db0d885f1430741608b2b461db92383457e5119a73f.jpg)

Fragmenting Attribute: OrdType Predicate Selectivity 41 OrdType = "Regular" 0.65 42 OrdType: Other 0.35

Candidate fragmentation attributes for the class Order OrdTotal and OrdType represent native attributes, while CState, CStatus, and CType are propagated

Figure 5. Candidate Fragmentation Attributes  
![](/api/attachments/2793FRDE/fulltext/images/a62362e012093527165ab8307963add62aed234e8e65ea83a75056067ce238e6.jpg)  
Figure 6. Fragments and Predicates

<table><tr><td>F1</td><td>11,21,31</td></tr><tr><td>F2</td><td>11,21,32</td></tr><tr><td>F3</td><td>11,22,31</td></tr><tr><td>F4</td><td>11,22,32</td></tr><tr><td>F5</td><td>12,21,31</td></tr><tr><td>F6</td><td>12,21,32</td></tr><tr><td>F7</td><td>12,22,31</td></tr><tr><td>F8</td><td>12,22,32</td></tr><tr><td>F9</td><td>13,21,31</td></tr><tr><td>F10</td><td>13,21,32</td></tr><tr><td>F11</td><td>13,22,31</td></tr><tr><td>F12</td><td>13,22,32</td></tr></table>

A given combination of candidates may benefit some scenarios, but may hinder others. In other words, selecting a fragmentation attribute may improve the potentia locality of references, however, selecting too many may increase the cost of assembling some required fragments. It is necessary, therefore, to devise measures that wil allow selection of the best combination of fragmentation attributes for each class. The notation below captures the discussion. The decision variable, X, shows whether an attribute will be accepted for fragmentation, and the set J contains fragments that may be generated after applying a combination of fragmentation attributes.

Xn = Fragmentation attribute n is selected, {0,1}

$$
\mathrm{i}, \mathrm{j} \in \mathrm{J} = \text {Fragments}.
$$

## Measuring the Benefits of Fragmentation

As a fragmentation attribute is applied, it creates fragments required by some scenarios. These may eventually be placed at the appropriate site, augmenting locality of processing for those scenarios. The actual placement is dictated by a separate allocation procedure. By creating the required fragment, we preserve the “potential” for such allocation. As successive fragmentation attributes are accepted, each fragment (a superimposition of predicates) satisfies an increasing number of scenarios. For example, if fragmentation attributes Customer:State and Customer:Status are accepted, the resulting fragments of the class Order will include $[ C S t a t e = { } ^ { \cdot } C A ^ { \prime } ] \wedge [ C S t a t u s =$ ‘Privileged’], $[ C S t a t e = { ^ { * } C A ^ { \prime } } ] \wedge [ C S t a t u s = O t h e r ] , [ C S t a t e = { ^ { * } W I } ^ { \prime } ] \wedge [ C S t a t u s = O t h e r ] .$ ‘Privileged’], $[ C S t a t e = { } ^ { \cdot } W I ^ { \prime } ] \wedge [ C S t a t u s = O t h e r ] .$ , and so on. The first two fragments are useful to a scenario that requires the predicate $[ C S t a t e = { } ^ { \cdot } C A ^ { \prime } ]$ , whereas the first and the third fragments are useful for the scenarios that require the predicate [CStatus $= \cdot P r i \nu i l e g e d ^ { \prime } ]$ . Thus, as we accept additional fragmentation attributes, the fragmentation benefits would mount. We define this as the potential of realizing locality for a scenario. To compute it, we aggregate the product of predicate selectivities and scenario frequencies for which the required predicates have been accepted. Specifically, the locality benefit is computed as the product between predicate selectivity (“select”), its use by a scenario (“use”), and the aggregate frequency of the scenario, adjusted for importance (“frequency,” and “importance”). Selecting a fragmentation attribute, thus leads to the aggregation of benefits obtained by use of predicates in that attribute by different scenarios. The use of selectivity in the formula ensures that predicates with higher selectivity are weighted more. For example, if a predicate value (say, $[ O r d e r . T y p e = ^ { \cdot } B o o k s ^ { \prime } ] )$ has 70 percent selectivity, it is more valuable than another (say, [Order.Type = ‘Auction’]), which may have only 2 percent selectivity. The formulation for locality benefit, summed for all attributes, is:

$$
\text { Locality } = \Sigma_ {\mathrm{n} \in \mathrm{N}} \left[ X _ {\mathrm{n}} \times \Sigma_ {\mathrm{p} \in \mathrm{P}} \left(\text { select } _ {\mathrm{np}} \times \Sigma_ {\mathrm{s} \in \mathrm{S}} \text { use } _ {\mathrm{snp}} \times \left(\text { importance } _ {\mathrm{s}} \times \left(\Sigma_ {\mathrm{k} \in \mathrm{L}} \text { frequency } _ {\mathrm{sk}}\right)\right)\right) \right].
$$

## Measuring the Costs of Fragmentation

A consequence of successive acceptance of fragmentation attributes is the rapid multiplication of the number of fragments. Since each fragment represents a superimposition of predicates, the number of fragments that need to be accessed to satisfy a particular scenario increases. For example, if a scenario requires instances that satisfy the predicate $[ C S t a t e = { } ^ { \cdot } C A ^ { \prime } ]$ , and the fragmentation attributes CState and CStatus have been accepted, the required instances are split into multiple fragments such as $[ C S t a t e = { } ^ { * } C A { } ^ { \prime } ] \wedge [ C S t a t u s = { } ^ { * } P r i \nu i l e g e d { } ^ { \prime } ]$ , and $[ C S t a t e = { } ^ { \cdot } C A ^ { \prime } ] \wedge [ C S t a t u s = { } ^ { \cdot } P r i \nu i -$ leged’]. Thus, instead of getting one fragment that satisfies the predicate $[ C S t a t e =$ $\cdot C A \ ' ] .$ , the scenario must obtain the required instances from two separate fragments. This breaking up of a required fragment creates the “threat” that some or all of the fragments required to process a scenario may be dispersed at different locations. Bringing these fragments together would then entail an additional cost every time the sce nario is executed. Whether these fragments are allocated to different sites is eventually decided by a separate allocation procedure. By accepting successive fragmentation attributes, we increase the threat that the required instances will be dispersed, resulting in a higher reconstruction cost. We define this as the effort for reconstructing the set of instances required by a scenario. We compute it by aggregating the product of predicate selectivities and frequencies of scenarios for which predicates that are not required have been accepted. The formulation mirrors that for locality, with two differences. The aggregate is computed for all scenarios (the set S), considering predicate selectivity $\mathrm { ( ^ { 6 6 } s e l e c t ^ { 7 7 } ) }$ of attributes that are selected for fragmentation $( \Chi _ { \mathrm { { n } } } = 1 )$ , but are not used by the scenario $( \mathrm { u s e } _ { \mathrm { s n p } } = 0 )$ . Other arguments similar to the ones made for locality benefit prevail for computation of reconstruction cost. The formulation, summed for all scenarios, is:

## " sÎS DO

IF $\exists \ \mathrm { n { \in N } , p { \in P } \mid [ X _ { \mathrm { n } } = 1 ] \land [ u s e _ { \mathrm { s n p } } = 0 ] }$ // fragmentation attributes selected but not required

$$
\mathrm{Sum} \leftarrow 0; \mathrm{Product} \leftarrow 1
$$

$$
\forall \mathrm{n} \in \mathrm{N} \mid [ \mathrm{X} _ {\mathrm{n}} = 1 ] \mathrm{DO}
$$

$$
\text { Sum } \leftarrow \text { Sum } + \Sigma_ {\mathrm{p} \in \mathrm{P}} \text { use } _ {\mathrm{snp}} \times \text { select } _ {\mathrm{np}}
$$

$$
\text { Product } \leftarrow \text { Product } \leftarrow \text { Sum }
$$

ENDDO

$$
\text { Reconstruction } \leftarrow \text { Reconstruction } + \text { Product } \times (\text { uses } _ {\mathrm{np}} \times (\text { importance } _ {\mathrm{s}} \times
$$

$$
(\Sigma_ {\mathrm{k} \in \mathrm{L}} \text { frequency } _ {\mathrm{sk}}))
$$

ENDIF

ENDDO

## Ensuring Threshold Granularity

The granularity of fragments also needs to be monitored. For example, fragments that are too small, or fragments that are too varied in size (such as one fragment with 99,900 instances and the other with the remaining 100 instances), are undesirable outcomes of the fragmentation process. Having such fragments can lead to the additional costs of managing a fragment, such as unnecessary overhead and coordination costs, as well as those associated with replicating and updating the methods. To formalize these nebulous concerns, we have devised two simple measures. The first,

Smallest Fragment, specifies the smallest acceptable size of the fragment, addressing the notion of fragment similarity [12]. Since classes can be of different sizes, we specify this measure in relative terms, as a percentage. The second, Disparity in Frag ment Sizes, specifies the relative spread in fragment sizes. This measure is typically assessed through the first or second moment of the distribution, adjusted for absolute size. We measure this by computing the coefficient of variation. For each measure, the designer can specify thresholds, either separately for each class, or for different categories of classes, which can then be profitably utilized in the fragmentation process to prevent possible undesirable effects of uncontrolled fragmentation.

The computation of coefficient of variation does not result in any further demands on the designer as it is computed from the available information. Designer interaction is restricted to specification of threshold values. For the research prototype implementation, several predefined threshold values were provided using categories such as number of instances in the class or total size of the class. In a more robust or commercial implementation, it is conceivable that more sophisticated threshold values can be made available to the designer. The notation below captures this. The variable “size” denotes the size of the fragment. The granularity parameters specified next denote the smallest size (“smallest”) and the disparity among sizes (“disparity”).

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$\mathrm{Size}_{\mathrm{i}} = \mathrm{Size}$ of fragment i, size$_{\mathrm{i}}$ ∈ [0,1]  
Smallest = min$_{\mathrm{i}\in\mathrm{J}}$ (size$_{\mathrm{i}}$)  
Disparity = σ(size$_{\mathrm{j}}$)/μ(size$_{\mathrm{j}}$), where, in usual notation, μ is mean and σ is standard deviation.
</div>

## Selecting the Best Combination of Fragmentation Attribute

With the above metrics—benefits, costs, and thresholds—the fragmentation decision can be expressed in a quantitative manner. Finding the best fragmentation involves maximizing the benefits accruing from Locality offset by costs incurred due to Reconstruction, subject to the constraints on Granularity. Each combination of fragmentation attributes is checked for feasibility, ensuring that the granularity thresholds are met, and a net benefit (Locality minus Reconstruction) is computed. To generate the different combinations, we have devised a procedure similar to that proposed by Chu and Ieong [19]. Although the procedure has 0(2<sup>n</sup>) complexity, this should not be a concern since it is performed separately for each class, which has only a limited number of fragmentations available. For example, it would be very unlikely that more than, say, 10 attributes will be considered for fragmenting a large class, resulting in a maximum of 1,024 possible combinations. Considering the limited computationa demands, the procedure will perform adequately. In applying the procedure to realworld applications, the complexity did not pose a major concern. Further, in our implementation of the algorithm, we preempted the computation of “disparity” by first computing the “smallest” fragment. Only when the “smallest” fragment threshold was satisfied, did we compute “disparity.” If the number of attributes is very large for a certain class, the complete enumeration algorithm we suggest can pose a problem.

The important attributes for fragmentation is, however, unlikely to be a large number. Supporting evidence for this comes from two sources. First, other research on horizontal fragmentation $\left[ \mathrm { e . g . , 4 } \right]$ suggests that only a few attributes (five) are often considered relevant for fragmentation. Second, work on OO metrics from real-world projects [54, p. 56] suggests that the average number of attributes (instance variables) for a class is between five and ten. Even in the unlikely scenario that all of these are considered as important, it would result in no more than 1,024 combinations of frag mentation attributes. Finally, our informal interactions with designers who participated in the case study reported in the paper, also suggests that the number of importan fragmentation attributes is likely to remain small, even if the total number of fragmentation attributes increases. The $0 ( 2 ^ { \mathrm { n } } )$ complexity or the procedure, however, remains a limitation.<sup>6</sup> The algorithm, thus, considers different combinations of attributes, and within the constraints, finds the best fragmentation alternative.

BEGIN

$\mathrm { S m a l l } _ { \mathrm { u r e s h o l d } }$ ¬ smallest acceptable fragment size

$\mathrm { D i s p a r i t y } _ { \mathrm { t h r e s h o l d } }$ ¬ largest acceptable fragment disparity

BestScore ¬ 0; BestCombination ¬ Æ

WHILE \$ another unique combination of the possible $[ 2 ^ { \mathrm { N } } - 1 ]$ combinations

Build a combination of attributes

Generate fragments using the combination

Compute Smallest and Disparity for this set of fragments

IF $\cdot S m a l l e s t > \mathrm { S m a l l e s t } _ { \mathrm { t h r e s h o l d } }$ and Disparity < Disparity

Compute Locality and Reconstruction

IF (Locality – Reconstruction) > BestScore

BestScore = Locality – Reconstruction

BestCombination ¬ Current Combination

ENDIF

ENDIF

ENDWHILE

END

## Allocation

ALLOCATION IS THE SECOND PHASE IN THE DISTRIBUTION PROCESS. Here, the problem involves placement of fragments (derived in phase 1) at sites to minimize intersite communication penalties. Like the fragmentation process, the allocation models we propose represent an extension of prior work in several ways. First, we explicitly recognize messaging as the key element of communication costs. Instead of unduly burdening the designer for these estimates and sabotaging the allocation model with unreliable estimates, we devise a procedure that automatically compiles estimates of aggregate traffic costs by exploiting the information available in (1) the interaction patterns, and (2) the fragmentation decisions made in the first phase. Second, since messaging may follow different routing strategies, the models we develop reflect alternate strategies appropriate for OO systems. We develop two allocation models, either of which can be selected by the designer, depending upon the routing strategy that will be employed in the eventual implementation. Third, our allocation models recognize that all “remote” sites may not be equally attractive as placement choices when viewed from the perspective of a “local” site. Unlike earlier models (for instance, [45, 52]), which distinguish local versus remote operations, but ignore differ ences between remote sites, we formulate traversal penalty as a surrogate for relative attractiveness of different remote sites. The allocation process, thus, first uses a procedure to estimate messaging traffic, and then applies the models to allocate frag ments to sites.

## Estimation of Messaging Traffic

The primary source of traffic volumes is inter-object message invocations, and attributes and object values returned in response. The traffic of interest falls into two groups—fragment-to-site and fragment-to-fragment.The procedure we propose compiles this traffic by exploiting information available in scenarios (Figure 3) and frag ments (Figure 6). It involves two steps: mapping scenarios to fragments and compiling traffic volumes.

## Mapping Scenarios to Fragments

Since messaging traffic results from scenarios, which utilize the fragments, a mapping between the two is necessary to ensure that the messaging traffic is attributed to the appropriate fragments. To arrive at this mapping, we exploit the dimension shared by both fragments and scenarios—the partitioning predicates. Predicates contribute to fragment definition, and they are used to identify fragments required by scenarios. For example, a predicate, say, $[ S t a t e = { } ^ { \cdot } C A { } ^ { \cdot } ]$ , may contribute to the derivation of some fragments and may be required by some scenarios. Figure 6 shows, for example, that predicate 11 $[ S t a t e = { } ^ { \cdot } C A ^ { \prime } ]$ , is used to derive fragments F1 through F4; predicate 31 [Status = ‘Privileged’] is used to derive all odd-numbered fragments; and fragment F1 is defined by predicates 11, 21, and 31; that is, $[ S t a t e = { } ^ { \cdot } C A { } ^ { \prime } ]$ $[ O r d e r T o t a l > 1 0 0 , 0 0 0 ]$ , and $\left[ S t a t u s = \cdot P r i \nu i l e g e d ^ { \prime } \right]$ . Similar information is also available for scenarios. For example, a scenario may involve orders placed by privileged customers from the state of California (that is, fragments satisfying predicates 31 and 11, respectively). Another scenario may require all orders valued greater than \$100,000 (predicate 21). Yet another scenario may require orders placed by customers from

California or Wisconsin, that have values greater than \$100,000 (predicates 11 or 12, and 21). The examples in Table 1 illustrate the complex mix of conjunctions and unions involved in identifying fragments of the class Order (see Figure 6) required by each scenario.

To capture the rationale illustrated above, the mapping procedure utilizes one overriding principle: The most appropriate fragment(s) are those that satisfy the maximum number of required predicates. Using this principle, fragments (of each class) required by each scenario are identified, and the scenario is mapped against the appropriate fragments.

## Compiling Traffic Volumes

The major contributor to traffic between interacting classes is the attribute values of object instances. For update interactions, these are passed as message parameters; for observe interactions, they are returned in response to messages. Given the context of an interaction pattern, say, Create Customer Order, it is relatively easy to obtain an approximation of the fraction of each object instance that will be updated or observed for each interaction. These parameters, along with the method signature provide the “size” of each message. The expected cardinality of classes together with the frequency of scenarios provides the multiplicity of messages. For example, the class Order may update the class OrderLine five times for every order created. Then, if the frequency of that scenario is known as 100, the interaction between these two classes is computed to be 500. Using scenario frequencies and the notion of reference joins [10, pp. 186–187], messaging traffic among classes can, therefore, be computed (see Figure 7a). However, since the classes may be fragmented, the traffic needs to be apportioned over the appropriate class fragments. By exploiting the scenario-fragment mapping and based on an assumption of uniform distribution of predicate values [11], the fragment-to-fragment traffic volume is computed using relative fragment sizes (see Figure 7b). The compilation procedure retains the distinction between observe and update interactions compiling these separately. Similar, but simpler computations allow compilation of fragment-to-site traffic volumes [65].

The traffic volume estimates, viz. fragment-to-site and fragment-to-fragment communication, provide a key input to the allocation models we develop next. These are used, along with a predefined unit cost element, to denote the costs of messaging traffic. The notations below capture the discussion. The variable “SflowO” denotes the traffic cost incurred when a fragment is accessed from a site, and the variable “SflowM” denotes the traffic cost incurred when a fragment is updated from the site. The corresponding variables “CflowO” and “CflowM” denote traffic costs for similar interactions between two fragments.

$$
\begin{array}{r l} \text { SflowO } _ {\text { ik }} & = \text { Traffic   cost   per   unit   period   between   fragment   i   and   site   k   (access   or } \\ & \text { observe) } \end{array}
$$

SflowM = Traffic cost per unit period between fragment i and site k (update or modify)

Table 1. Mapping Fragments to Scenarios

<table><tr><td>Scenario</td><td>Predicates required</td><td>Fragments required (refer to Figure 6)</td><td>Rationale</td></tr><tr><td>1</td><td>11</td><td>F1, F2, F3, F4</td><td>Any fragment with predicate 11.</td></tr><tr><td>2</td><td>13, 42</td><td>F9, F10, F11, F12</td><td>Any fragment with predicate 13, since predicate 42 is not accepted.</td></tr><tr><td>3</td><td>11, 22, 31</td><td>F3</td><td>The fragment satisfying all predicates.</td></tr><tr><td>4</td><td>11, 12, 32</td><td>F2, F4, F6, F8</td><td>Any fragment with predicates 11 and 32, plus any fragment with predicates 12 and 32.</td></tr><tr><td>5</td><td>41</td><td>F1 through F12</td><td>All fragments, since predicate 41 is not accepted.</td></tr></table>

$\mathrm { C f l o w O _ { i j } }$ = Traffic cost per unit period between fragments i and j (access or observe)

$\mathbf { C f l o w M _ { \mathrm { i j } } }$ = Traffic cost per unit period between fragments i and j (update or modify).

## Allocation Model

The allocation model places fragments at sites to minimize inter-site messaging traf fic. During this placement, the distinction between observe and update traffic be comes important, since an “observe” operation requires reading a single copy of the fragment, but an “update” must write to all copies of the fragment (that is, read one and write all [52]). Most routing strategies attempt to read the closest copy. For example, the read operation is performed locally, if a copy is available, otherwise, th copy residing at the closest site is read. An update (or modify) requires a write-all approach, which can be accomplished in several ways. Most allocation models, how ever, distinguish only between local and remote operations failing to distinguish between different remote sites. This distinction is, in fact, important since it can affect communication penalties. For example, one approach may be to make each copy of an “updating” fragment responsible for updating the closest copy of the fragment “being updated” (Nearest Neighbor). Another possibility is to make one copy of the “updating” fragment responsible for updating all copies of the fragment “being updated” (Global Update). These distinctions are particularly relevant for OO applications, which rely primarily on messaging.<sup>7</sup> If any object is replicated, the message routing must rely on knowledge of the location of different copies to route the messages appropriately. The two strategies are intrinsically different as they follow different rules for realizing the update operations. Since they affect the communication penalties, the distribution re sults may be different, depending on which strategy is followed. Therefore, we formulate models to reflect both strategies (see Figure 8). We present the base model first, followed by incremental extensions required by each update strategy to complete the model.

```txt
Instances of Customer Participating in the Scenario: select = 60%
Cardinality of Customer: card = 1,000
Association Cardinality: a-card=20
Instance Size of Affected Class Order: i-size =70 Bytes
Fraction of Each Instance Affected: fraction = 10%
```

```txt
Total Flow = card * select * freq * a-card * i-size * fraction
= 1,000 * 60% * 50 * 20 * 70 * 10% = 4,200,000 bytes
```  
(a) Traffic Flow Resulting from a Scenario

![](/api/attachments/2793FRDE/fulltext/images/e7ef619357ff0cbb895a66f91ba517e8a0997e3f1498a55890c954e75006be3b.jpg)  
(b) Traffic Flow Among Fragments of Customer and Order  
Figure 7. Compilation of Data Traffic Estimates

![](/api/attachments/2793FRDE/fulltext/images/45f8e191ea7c1e559d724945190efb62e4af0dca63bc7027958249f2a05eca7a.jpg)  
Nearest Neighbor Strategy

![](/api/attachments/2793FRDE/fulltext/images/bfd6e3ad3e006c139cc9d90b21863ccca877c3ca84a8d99f65b053090568d680.jpg)  
Figure 8. Alternative Update Strategies

## Base Model

Messaging traffic cost estimates compiled earlier—fragment-to-site and fragment-to fragment—with distinction between observe and update interactions, provide a key input to the allocation model. Neither estimate, by itself, indicates the incurred siteto-site communication penalties, since the required fragment may be located at the requesting site or the two interacting fragments may be colocated. A specific allocation (placement of fragments at sites) materializes these traffic costs as site-to-site communication penalties, which the model attempts to minimize with appropriate placement of fragments. Since a class fragment can contain attributes as well as methods (see Figure 2), the model needs to ensure that the site will have sufficient processing capabilities to perform the types of services needed for these methods. We ensure this by tracking availability of processor types [25, 35] and any special processing characteristics at sites. The notation below captures the discussion. The variable “Proc” denotes the requirement of a processor type by a fragment, and the variable “Reqm” indicates the requirement of special processing capabilities, if any. The variable “Stor age” simply records the storage cost per unit period for each fragment.

Proc = Processor type t required by fragment i, {0,1}

Reqm = Special processing characteristic r required by fragment i, {0,1}

Storage = Storage cost per unit period for fragment i.

The base model is driven by the primary decision variable X, which represents the decision to locate a fragment at a site. The other variables, Y and Z capture routing decisions that enable computation of site-to-site communication penalties resulting from a specific distribution.

$\mathrm { X } _ { \mathrm { i k } }$ = Fragment i is allocated to site k, {0,1}

$\mathrm { Y _ { i k l } }$ = Site k observes the copy of fragment i, allocated at site l, {0,1}

$Z _ { \mathrm { i j k l } }$ = Fragment i, at site k observes fragment j, allocated at site l, {0,1}.

Objective Function. The objective function consists of four elements of communication costs plus storage cost. SFLOWO captures the cost associated with observing a required fragment from a site, SFLOWM, the cost associated with updating (modifying) a required fragment from a site, CFLOWO, the cost associated with observe interactions between class fragments, and CFLOWM, the cost associated with update (modify) interactions between class fragments. Of these, the first three can be formulated without regard to the update strategy. The specific form of the last, CFLOWM, requires selection of the update strategy (see Figure 8). The elements of communication cost are adjusted for the relative traversal penalty between sites (trav). The fifth and final element, STORAGE, captures storage costs as a linear function of degree of replication.

$$
\text { TOTALCOST } = \text { SFLOWO } + \text { SFLOWM } + \text { CFLOWO } + \text { CFLOWM } + \text { STORAGE },\tag{1}
$$

where

$$
\mathrm{SFLOWO} = \Sigma_ {\mathrm{i} \in \mathrm{J}} \Sigma_ {\mathrm{k} \in \mathrm{L}} \Sigma_ {\mathrm{l} \in \mathrm{L}} \mathrm{SflowO} _ {\mathrm{ik}} \times \operatorname{Trav} _ {\mathrm{kl}} \times \mathrm{Y} _ {\mathrm{ikl}}\tag{2}
$$

$$
\mathrm{SFLOWM} = \Sigma_ {\mathrm{i} \in \mathrm{J}} \Sigma_ {\mathrm{k} \in \mathrm{L}} \Sigma_ {\mathrm{l} \in \mathrm{L}} \mathrm{SflowM} _ {\mathrm{ik}} \times \mathrm{Trav} _ {\mathrm{kl}} \times X _ {\mathrm{il}}\tag{3}
$$

$$
\mathrm{CFLOWO} = \Sigma_ {\mathrm{i} \in \mathrm{J}} \Sigma_ {\mathrm{j} \in \mathrm{J}} \Sigma_ {\mathrm{k} \in \mathrm{L}} \Sigma_ {\mathrm{l} \in \mathrm{L}} \mathrm{CflowO} _ {\mathrm{ij}} \times \operatorname{Trav} _ {\mathrm{kl}} \times \mathrm{Z} _ {\mathrm{ijkl}}\tag{4}
$$

$$
\begin{array}{l} \text {CFLOWM} = (\text {formulated independently for alternate update policies}, \\ \text {see below}) \end{array}
$$

$$
\text { STORAGE } = \Sigma_ {\mathrm{i} \in \mathrm{J}} \Sigma_ {\mathrm{k} \in \mathrm{L}} \text { Storage } _ {\mathrm{i}} \times \mathrm{X} _ {\mathrm{ik}}.\tag{5}
$$

Two sets of constraints define the search space for our model—integrity constraints and structural constraints. The first set refers to basic concerns such as availability of processor capabilities and processing capabilities. The second set enforces the routing strategy.

Integrity Constraints. The first constraint (6) ensures that a copy of the fragment will be allocated to at least one site by enforcing the sum of the allocation decision variable X to be one or greater for each fragment. The second constraint (7) ensures that a fragment will not be allocated at a site unless at least one of the required processor types (type) is available (proc) at that site. Finally, the third constraint (8) ensures that an allocation will not be permitted unless all of the required special processing capabilities (reqm) are met by the site (char).

$$
\Sigma_ {\mathrm{k} \in \mathrm{L}} \qquad \mathrm {X_ {ik}} \qquad \geq 1 \qquad \forall \mathrm{i} \in \mathrm{J}\tag{6}
$$

$$
\Sigma_ {t \in T} \quad \left(\text { type } _ {k t} \times \text { proc } _ {i t}\right) \geq X _ {i k} \quad \forall i \in J, k \in L\tag{7}
$$

$$
\left(\operatorname{reqm} _ {\mathrm{ir}} \times \mathrm{X} _ {\mathrm{ik}}\right) \leq \operatorname{char} _ {\mathrm{kr}} \quad \forall \mathrm{i} \in \mathrm{J}, \mathrm{k} \in \mathrm{L}, \mathrm{r} \in \mathrm{R}.\tag{8}
$$

Structural Constraints. Constraint (9) ensures that a site, k, cannot decide to read the required fragment, i, from another site, l, unless it is available at that site. Constraint (10) ensures that at least one copy of the required fragment, i, is read. Constraints (11) and (12) ensure that if a fragment, i, at a site, k, decides to update a fragment, j, at another site, l—the operation cannot be performed unless a copy of the fragments— i and j—reside at the sites—k and l—respectively. Finally, constraint (13) ensures that every copy of fragment, j, is updated by at least one copy of the fragment, i.

$$
\mathrm{Y} _ {\mathrm{ikl}} \leq \mathrm{X} _ {\mathrm{il}} \quad \forall \mathrm{i} \in \mathrm{J}, \mathrm{k} \in \mathrm{L}, \mathrm{l} \in \mathrm{L}\tag{9}
$$

$$
\Sigma_ {\mathrm{l} \in \mathrm{L}} \quad \mathrm{Y} _ {\mathrm{ikl}} \geq 1 \quad \forall \mathrm{i} \in \mathrm{J}, \mathrm{k} \in \mathrm{L}\tag{10}
$$

$$
Z _ {i j k l} \leq X _ {i k} \quad \forall i \in J, j \in J, k \in L, l \in L\tag{11}
$$

$$
Z _ {i j k l} \leq X _ {j l} \quad \forall i \in J, j \in J, k \in L, l \in L\tag{12}
$$

$$
\Sigma_ {k \in L} \Sigma_ {l \in L} \quad Z _ {i j k l} \geq 1 \quad \forall i \in J, j \in J.\tag{13}
$$

## Alternate Update Strategies

To complete the model, we formulate the remaining cost component by operationalizing the routing strategy. Using mechanisms such as the object adapter [59], we rely on the “managers” at each site to communicate with one another to coordinate routing. We have opted to model two update strategies, either of which may be used by the designer.

The first update propagation strategy we model captures the following policy—the update to a copy of a fragment is performed by the closest copy of the updating fragment (see Figure 8). This strategy (Nearest Neighbor) requires additions to variables and constraints, and formulation of the remaining component of the objective function. The alternative update propagation strategy we model captures the following policy—the update to all copies of a fragment is performed by the copy of the updating fragment that has the smallest total distance to all copies of the updated fragment (see Figure 8). This strategy (Global Update) too, requires additions to variables and constraints, and formulation of the remaining component.

First Update Strategy: Nearest Neighbor. The additional decision variable, and the constraints we introduce, enforce the update propagation strategy. In effect, they capture how message routing will be performed under the strategy, allowing us to compute the resulting communication cost. We define a routing variable (v) to capture the choice made when a fragment (i) updates another fragment (j). When the objective function is minimized, the closest fragment (i) is selected to perform the required update for each fragment (j). The first constraint (14) for this policy ensures that the update to a fragment will be performed (v) from a site where the updating fragment (i) is, in fact, allocated (x). The second constraint (15) ensures that a fragment that requires an update will, in fact, be updated (v) at least once by requiring that the summation of updates to it from all sites is at least one for each of its copies (x).

$$
\mathrm{V} _ {\text {ijkl}} \quad \text {fragment i, at site k updates fragment j, allocated at site l \{0,1\}}
$$

$$
\mathrm{V} _ {\mathrm{ijkl}} \leq \mathrm{X} _ {\mathrm{ik}} \quad \forall \mathrm{i} \in \mathrm{J}, \mathrm{j} \in \mathrm{J}, \mathrm{k} \in \mathrm{L}, \mathrm{l} \in \mathrm{L}\tag{14}
$$

$$
\Sigma \mathrm{k} \in \mathrm{L} \quad \mathrm{V} _ {\mathrm{ijkl}} \geq \mathrm{X} _ {\mathrm{jl}} \quad \forall \mathrm{i} \in \mathrm{J}, \mathrm{j} \in \mathrm{J}, \mathrm{l} \in \mathrm{L}.\tag{15}
$$

Formulation of the final element of the objective function, thus, will take into account communication cost CFLOWM, adjusted for preference between remote sites (trav) and the routing (v).

$$
\mathrm{CFLOWM} = \Sigma \mathrm{i} \in \mathrm{J} \Sigma \mathrm{j} \in \mathrm{J} \Sigma \mathrm{k} \in \mathrm{L} \Sigma \mathrm{l} \in \mathrm{L} \quad \mathrm{CflowM} _ {\mathrm{ij}} \times \operatorname{Trav} _ {\mathrm{kl}} \times \mathrm{V} _ {\mathrm{ijkl}}\tag{16}
$$

Alternate Update Strategy: Global Update.8 We define a corresponding routing variable (w) for the alternate strategy to capture the choice made when a certain copy (at site “k”) of a fragment (i) updates all copies of another fragment (j). When the objective function is minimized, the copy of fragment (i) that is closest, in sum, to all copies of the fragment (j) will be selected to perform the required update for each copy of that fragment (j). The first constraint (17) for this policy ensures that the update to a fragment will be performed (w) from a site (k) where the updating fragment (i) is, in fact, allocated (x). The second constraint (18) ensures that a fragment that requires an update will, in fact, be updated (w) at least once by requiring that the summation of updates to it from all sites is at least one.

$\mathrm { W _ { i j k } }$ fragment i, allocated at site k updates fragment j {0,1}

$$
\mathrm{W} _ {\mathrm{ijk}} \leq \mathrm{X} _ {\mathrm{ik}} \quad \forall \mathrm{i} \in \mathrm{J}, \mathrm{j} \in \mathrm{J}, \mathrm{k} \in \mathrm{L}\tag{17}
$$

$$
\Sigma_ {k \in L} \quad W _ {i j k} \geq 1 \quad \forall i \in J, j \in J\tag{18}
$$

Formulation of the final element of the objective function, thus, takes into accoun the communication cost CFLOWM, adjusted for preference between remote sites (trav) and the routing (w).

$$
\mathrm{CFLOWM} = \Sigma_ {\mathrm{i} \in \mathrm{J}} \Sigma_ {\mathrm{j} \in \mathrm{J}} \Sigma_ {\mathrm{k} \in \mathrm{L}} \Sigma_ {\mathrm{l} \in \mathrm{L}} \quad \mathrm{CflowM} _ {\mathrm{ij}} \times \operatorname{trav} _ {\mathrm{kl}} \times \mathrm{W} _ {\mathrm{ijk}} \times \mathrm{X} _ {\mathrm{jl}}\tag{19}
$$

The nonlinear term $\mathrm { W _ { i j k } } \times \mathrm { X _ { j l } }$ in the objective function can be linearized by adjustments such as those suggested by Glover [34] and Kettani and Oral [48]. A number of commercial systems such as GAMS [33], and solvers such as ZOOM [33], employing the branch-and-bound algorithm, are available for solving the model.

## Application

THE ALGORITHMS AND MODELS DESCRIBED IN THIS PAPER were implemented as part of a prototype called ODE (Object Distribution Environment) [66]. The algorithms were implemented using Microsoft Visual C++™ on a Pentium class PC. The integer-programming models implemented in GAMS [33] for execution on a Sun workstation. The entire approach was verified by using the prototype for distribution of a nontrivial marketing information system for a Midwestern utility company. The application consisted of 16 domain-level classes, with the number of instances ranging from 50 to 54,000,000. The computing infrastructure consisted of four sites, with different processing capabilities. The distribution requirements were obtained from 53 scenarios, based on 13 interaction patterns.

## Results

The fragmentation phase created 61 fragments. They ranged in size from 1 percent to 70 percent for different classes. The designer-specified thresholds for the smallest fragment size varied from 0.01 to 1.00, and for fragment disparity varied from 0.00 to 2.00. Candidate fragmentation attributes compiled for each class varied from one to four, and one class, being too small, had none. For example, the class Account, consisting of 1,800,000 instances had 4 candidate fragmentation attributes: BillAddrState, MktGrpCode, Customer:CustType, and SalesSeg:AreaName. The fragmentation algorithm (subject to the thresholds of 0.01 and 1.25 for smallest fragment and disparity, respectively) accepted two fragmentation attributes (BillAddrState—four predicates, and CustType—three predicates) and rejected the others, resulting in 12 fragments—ranging from 1 percent to 28 percent in size with a disparity measure of 0.289. Examination of the results revealed that four interaction patterns required the attribute BillAddrState, just one interaction pattern needed the second attribute, and the third and the fourth attributes were required by three interaction patterns each. The aggregate frequency of scenarios was much higher for the attributes BillAddrState and CustType when compared to the other attributes. The fragmentation algorithm thus, confirmed these informal observations. Table 2 shows a summary of results from this phase for all classes.

<table><tr><td rowspan="2">Classes</td><td rowspan="2">Number of instances</td><td rowspan="2">Fragmentation attributes/class</td><td colspan="2">Thresholds specified</td><td colspan="2">Results obtained</td></tr><tr><td>Smallest fragment</td><td>Fragment disparity</td><td>Number of fragments</td><td>Sizes</td></tr><tr><td>16</td><td>Min: 50Max: 54 million</td><td>Min: 1 (one with 0)Max: 4</td><td>Min: 0.001Max: 1.00</td><td>Min: 0.00Max: 2.00</td><td>61</td><td>Min: 1%Max: 70%</td></tr><tr><td colspan="7">Example: Class Account—1,800,000 Instances</td></tr><tr><td colspan="7">Candidate fragmentation attributes: 4</td></tr><tr><td>BillAddrState</td><td>MktGrpCode</td><td>Customer:CustType</td><td colspan="2">SalesSeg:AreaName</td><td></td><td></td></tr><tr><td>‘AB’—10%‘IJ’—40%‘PQ’—35%‘XY’—15%</td><td>‘A1xx’—30%‘I2xx’—20%‘P3xx’—15%‘X4xx’—35%</td><td>‘Corp’—5%‘SmallBus’—80%‘Govt’—15%</td><td colspan="2">‘C4xx’—25%‘K6xx’—20%‘S8xx’—25%‘Z0xx’—30%</td><td></td><td></td></tr><tr><td colspan="7">Granularity thresholds</td></tr><tr><td>Smallest fragmentFragment disparity</td><td></td><td>0.001 (lower limit)1.25 (upper limit)</td><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td>BillAddrState</td><td>MktGrpCode</td><td>Customer:CustType</td><td>SalesSeg:AreaName</td><td></td></tr><tr><td>√ Accepted</td><td>⊗ Rejected</td><td>√ Accepted</td><td>⊗ Rejected</td><td></td></tr><tr><td colspan="5">Fragments Generated—Smallest fragment: 0.005, Fragment disparity: 0.289</td></tr><tr><td>Number</td><td>Predicates</td><td></td><td>Size</td><td></td></tr><tr><td>1</td><td colspan="2">BillAddrState = ‘AB’ ∧ Customer:CustType = ‘Corp’</td><td>0.005</td><td></td></tr><tr><td>2</td><td colspan="2">BillAddrState = ‘AB’ ∧ Customer:CustType = ‘SmallBus’</td><td>0.08</td><td></td></tr><tr><td>3</td><td colspan="2">BillAddrState = ‘AB’ ∧ Customer:CustType = ‘Govt’</td><td>0.015</td><td></td></tr><tr><td>4</td><td colspan="2">BillAddrState = ‘IJ’ ∧ Customer:CustType = ‘Corp’</td><td></td><td>0.02</td></tr><tr><td>5</td><td colspan="2">BillAddrState = ‘IJ’ ∧ Customer:CustType = ‘SmallBus’</td><td>0.32</td><td></td></tr><tr><td>6</td><td colspan="2">BillAddrState = ‘IJ’ ∧ Customer:CustType = ‘Govt’</td><td>0.06</td><td></td></tr><tr><td>7</td><td colspan="2">BillAddrState = ‘PQ’ ∧ Customer:CustType = ‘Corp’</td><td>0.0175</td><td></td></tr><tr><td>8</td><td colspan="2">BillAddrState = ‘PQ’ ∧ Customer:CustType = ‘SmallBus’</td><td>0.28</td><td></td></tr><tr><td>9</td><td colspan="2">BillAddrState = ‘PQ’ ∧ Customer:CustType = ‘Govt’</td><td>0.0525</td><td></td></tr><tr><td>10</td><td colspan="2">BillAddrState = ‘XY’ ∧ Customer:CustType = ‘Corp’</td><td>0.0075</td><td></td></tr><tr><td>11</td><td colspan="2">BillAddrState = ‘XY’ ∧ Customer:CustType = ‘SmallBus’</td><td>0.12</td><td></td></tr><tr><td>12</td><td colspan="2">BillAddrState = ‘XY’ ∧ Customer:CustType = ‘Govt’</td><td>0.0225</td><td></td></tr><tr><td></td><td>Smallest Fragment</td><td>0.005 &gt; threshold: 0.001</td><td></td><td></td></tr><tr><td></td><td>Fragment Disparity</td><td>0.289 &lt; threshold: 1.25</td><td></td><td></td></tr></table>

Input to the allocation model consisted of compiled traffic estimates. A mapping between fragments and predicates was performed first using the mapping procedure. For example, a fragment of the class Account $( B i l l A d d r S t a t e = \dot { } \mathbf { A } \mathbf { B }$ ,’ and CustType = ‘Govt’) was mapped to seven scenarios that required these predicates. Using the fre quencies of these scenarios, traffic estimates were mechanically compiled. Two separate allocation models were invoked corresponding to the two update strategies outlined in the paper, with user-specified improvement threshold and iteration limits. Table 3 shows a summary of results from this phase.

Continuing the example, the first fragment of the class Account (BillAddrState = ‘AB,’ and $C u s t T y p e = \mathbf { \dot { \omega } } \mathbf { G o v t } ^ { \prime } )$ was allocated to sites 1 and 3 under both update strategies. Another fragment of the class (BillAddrState = ‘PQ,’ and $C u s t T y p e = \mathrm { \cdot S m a l l B u s ^ { \circ } ) }$ was allocated to sites 1 and 3 under the Nearest Neighbor model, but was allocated to only site 1 under the Global Update model. An examination of the scenario frequencies revealed that though these fragments were required at both sites 1 and 3, the update frequencies of the second fragment were higher than those for the first— informally confirming the model outcome.

Overall, the first model, Nearest Neighbor, resulted in an allocation with replication level 1.75, that is, each fragment was allocated, on average to 1.75 sites out of a possible 4. The second model, Global Update, resulted in a slightly lower replication level, at 1.44, that is, for this application, the first model more readily replicated the fragments compared to the other. A possible explanation may lie in the operation of the routing strategies. The first strategy, Nearest Neighbor, makes the closest copy responsible for updating a fragment, whereas the second strategy, Global Update, makes one copy responsible for updating all copies of a fragment. It can be argued that the first strategy would generally result in a slightly lower update cost, since each update would be made by the closest copy, as opposed to the second strategy, which uses copy that is closest, in sum, to all copies of the fragment being updated. In other words, the penalty for replication would be lower under Nearest Neighbor compared to Global Update leading to slightly different replication levels. For the test case under consideration, the total costs for the distribution results were projected to be \$29,424 per month for the “Nearest Neighbor” strategy, and \$30,488 per month for the “Global Update” strategy, based on 1¢ per MB for storage costs (amortized over 36 months) and communication costs at 5 times the storage costs. Details of this breakdown appear in Tables 2 and 3.

Although the preferred basis for evaluation of our approach would be a direct comparison with conventional distribution of the application, this can be exceedingly difficult, since it would require considerable effort from the system designers, essentially distributing the application twice. In lieu of this comparison, we articulate several elements that contribute to the effectiveness of our approach over a conventional approach. First, by tackling the problem at medium granularity, the fragmentation and allocation phases provide intuitively more opportunities during distribution than the coarse grain model. Second, use of interaction patterns and scenarios to generate distribution parameters adds considerably to the authenticity of inputs to the fragmentation and allocation models. The ability to trace these decisions to specific inputs should provide another level of confidence in the results. The allocation models reflect routing strategies appropriate for OO systems, suggesting higher fidelity of the model with the underlying technological basis. Further, the allocation models include multiple possible update strategies, which allow the designer to consider more options in making the final allocation decisions. Finally, a clearer understanding of the models and techniques that represent different elements of the approach should contribute to a greater degree of confidence in the effectiveness of the application distribution generated through our approach.

<sub>d</sub> <sub>by</sub> <sub>[University</sub> <sub>of</sub> W<sup>aterloo]</sup> <sup>at</sup> <sup>00:46</sup> <sup>07</sup> <sup>A</sup>

<table><tr><td rowspan="2">Fragment number</td><td colspan="2">Site A</td><td colspan="2">Site B</td><td colspan="2">Site C</td><td colspan="2">Site D</td></tr><tr><td>N</td><td>G</td><td>N</td><td>G</td><td>N</td><td>G</td><td>N</td><td>G</td></tr><tr><td>1</td><td>1</td><td>1</td><td></td><td></td><td>1</td><td>1</td><td></td><td></td></tr><tr><td>2</td><td>1</td><td>1</td><td></td><td></td><td>1</td><td>1</td><td></td><td></td></tr><tr><td>3</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>4</td><td>1</td><td>1</td><td></td><td></td><td>1</td><td>1</td><td></td><td></td></tr><tr><td>5</td><td>1</td><td>1</td><td></td><td></td><td>1</td><td></td><td></td><td></td></tr><tr><td>6</td><td></td><td></td><td>1</td><td>1</td><td>1</td><td>1</td><td></td><td></td></tr><tr><td>7</td><td>1</td><td>1</td><td></td><td></td><td>1</td><td>1</td><td></td><td></td></tr><tr><td>8</td><td>1</td><td>1</td><td></td><td></td><td>1</td><td></td><td></td><td></td></tr><tr><td>9</td><td></td><td></td><td></td><td></td><td>1</td><td>1</td><td></td><td></td></tr><tr><td>10</td><td></td><td></td><td></td><td></td><td>1</td><td>1</td><td></td><td></td></tr><tr><td>11</td><td></td><td></td><td></td><td></td><td>1</td><td>1</td><td></td><td></td></tr><tr><td>12</td><td></td><td></td><td></td><td></td><td>1</td><td>1</td><td></td><td></td></tr><tr><td colspan="9">Note: N = nearest neighbor strategy, G = global update strategy.</td></tr></table>

<table><tr><td rowspan="2">Sites in the computing infrastructure</td><td rowspan="2">Fragments to be allocated</td><td rowspan="2"></td><td colspan="5">Results obtained</td></tr><tr><td>Site A</td><td>Site B</td><td>Site C</td><td>Site D</td><td>Replication level</td></tr><tr><td rowspan="2">Four sites designated as A, B, C, D</td><td rowspan="2">61(see Table 2)</td><td>Strategy: Nearest Neighbor</td><td>47</td><td>10</td><td>41</td><td>9</td><td>1.75</td></tr><tr><td>Strategy: Global Update</td><td>44</td><td>8</td><td>43</td><td>5</td><td>1.44</td></tr><tr><td colspan="8">Example: Allocation of fragments of class account (see Table 2)</td></tr></table>

<sub>.SummaryofResults</sub>—<sup>Allo</sup>

## Conclusions

WE HAVE DESCRIBED AN APPROACH for distribution of OO applications in loosely coupled networks. The approach consists of two phases: a horizontal class fragmentation scheme and fragment allocation models.

The horizontal fragmentation scheme represents a novel contribution for distribut ing OO applications. It extends research in relational data fragmentation by addressing specific properties unique to OO applications, such as encapsulation and inheritance. The scheme is unique in that it utilizes both semantic as well as statistica information. To identify fragments, it makes use of surrogate measures for benefits and costs of fragmentation, subject to granularity thresholds, which ensure that the fragmentation is reasonable. By delegating the responsibility to search for optima fragmentation to each class, the scheme retains the ability to make or adjust fragmentation decisions, even in the absence of complete knowledge of the schema. For example, after the application is implemented, a monitoring system can track predicates and scenario frequencies, and the fragmentation algorithm may be periodically in voked to adjust the fragmentation decisions for any class.

The allocation model improves on previous research in several ways. First, it distinguishes between multiple remote sites, based on the traversal penalty from the current site. Previous research has made a distinction between local versus remote operations, but not between multiple remote sites. It is possible that some remote sites may be more attractive than others, due to a number of reasons including link reliability, link speed, traffic patterns, and so forth. The variables we have suggested and the resulting formulations can be effectively used as a surrogate for different concerns, such as communication costs, response time, link reliability, and so on, to reflect the relative attractiveness of different remote sites. Second, our model captures the message-intensive nature of OO systems to model alternate routing strategies. The two strategies—nearest neighbor and global update—represent viable object-interaction strategies for distributed objects. The nearest neighbor strategy relies on local knowledge about the closest copy of the required object, whereas the global update strategy exploits a global dictionary service similar to that suggested by CORBA 2.0.

The two phases—fragmentation and allocation—are tied together by a procedure to automatically compile traffic estimates among class fragments. Traditionally, allocation models have assumed availability of parameters such as traffic volumes, requiring a “guesstimate” from the system designers. Instead of relying on such guesswork, our procedure compiles these estimates. It is a nonarbitrary procedure that builds on available information from available sources to generate these estimates. These estimates then provide natural inputs to the allocation models. Table 4 compiles the information sought from the designer for and through the distribution process. Compared with other approaches [e.g., 63, 71], the approach we have developed requires much fewer inputs.

The models and results presented have demonstrated how conventional distribution techniques can be extended and enhanced to derive an initial, static distribution of OO applications. This is a hard problem, particularly if tackled using distributable units of medium-grain granularity. Our approach makes this more tractable for the designer. A lot of information is needed for both phases to work effectively. Some of these are derived automatically, such as, traffic from interaction patterns, formulating residual predicates, and so on. Nevertheless, effective distribution still requires some designer input. Conventional distribution practices rely on rules of thumb or simple heuristics that cannot be verified post hoc. Our approach, on the other hand, provides a quantitative operationalization that can be traced to the designer inputs. Results from resource migration strategies [57] can be used to fine-tune the initial distribution. Application designers also have the option of using one or both phases.

During application of the scheme to real-world systems, we discovered some limi tations that we deem areas for future improvements. The fragmentation procedure is sensitive to predicates with low selectivity values, which may result in the rejection of reasonable fragmentation criteria on account of granularity constraints. This i particularly evident for very small and extremely large classes. The fragmentation process can also be improved to incorporate some domain knowledge, so that unnatural fragments are not considered. Additional update strategies are possible for the allocation models. For example, a “Master Copy” strategy, where one copy of the fragment is designated as the master and is responsible for propagating updates to all other copies. Another concern is ease of solvability. For testing, we elected to use a generally accepted solution approach that can tackle repeated applications, employing the Branch-and-Bound algorithm with commercial solvers such as ZOOM [33], and specifying improvement tolerances. Since many constraints in the problem em ploy integer values, and the matrix of messaging traffic estimates is generally sparsely populated, specialized solution approaches employing network and integer programming techniques (for instance, [20]), may improve solution performance

<sub>signerInputstoandInteractionsDuri</sub><sup>ngD</sup>

<table><tr><td>Available sources</td><td>Designer input</td><td>Example</td></tr><tr><td>Computing infrastructure: sites and links across sites</td><td>Relative attractiveness of remote sites, that is, traversal penalty</td><td>Site X is twice as attractive as site Y for site A.</td></tr><tr><td rowspan="2">Static application models: classes, attributes, methods</td><td>Expected cardinality of classes</td><td>The class “Customer” has 100,000 instances.</td></tr><tr><td>Expected cardinality of multi-valued attributes</td><td>On average, three “Items” are part of every “Order.”</td></tr><tr><td rowspan="2">Dynamic application models: scenarios and interaction patterns</td><td>Scenario frequency from sites</td><td>A given scenario is performed 100 times a month.</td></tr><tr><td>Predicates and selectivities</td><td>The scenario applies to customers from New York, who make up about 30 percent of our customers.</td></tr><tr><td>Distribution phase</td><td>Designer interaction</td><td>Example</td></tr><tr><td rowspan="2">Fragmentation</td><td>Judgment about significant attributes</td><td>Attribute “ProductType” is not relevant for fragmentation.</td></tr><tr><td>Smallest and disparity thresholds</td><td>The “Smallest” fragment should not contain fewer than 10,000 tuples; the “Disparity” for class “Customer” should not be more than 2.5.</td></tr><tr><td rowspan="2">Allocation</td><td>Fragment processing requirements</td><td>A given “Fragment” will require the video server and a mid-range or better processor.</td></tr><tr><td>Per unit communication and storage cost</td><td>The storage cost is one cent per MB and communication cost five center per MB—approximated per month.</td></tr></table>

## NOTES

1. Vertical fragmentation requires grouping of frequently accessed attributes [58]. Hori zontal fragmentation [11, 19], on the other hand, is accomplished by placing conditions on attribute values.

2. A static strategy does not base its routing assignments on measurements of current traffic load. Its goal is to optimize system performance (in our case, minimize inter-site communica tions) over a period [6].

3. If, on the other hand, technological requirements are a constraint, they must be observed during distribution. We address these accordingly as we develop the model.

4. Similar to Ceri and Navathe [11], who use a logical data model as an input to the distribution process.

5. Our approach does not require such promoting up or rolling down. Our proposals work equally well, with minimal adjustments, even if subclasses and superclasses are separated.

6. Bellatreche et al. [2] concede that exhaustive enumeration may be necessary for class fragmentation, but suggest an approximate hill-climbing algorithm for searching through combinations of terms, which may be adapted to enhance our algorithm

7. A third less-frequently used strategy, not modeled, may involve a rolling propagation across copies of fragments.

8. Note that these represent increments to the Base model, and not to the Nearest Neighbo model. The variables and constraints, therefore, replace the corresponding increments specified for the first strategy.

## REFERENCES

1. Andleigh, P., and Gretzinger, W. Distributed Object-Oriented Data-Systems Design Englewood Cliffs, NJ: Prentice Hall, 1992.

2. Bellatreche, L.; Karlapalem, K.; and Basak, G.B. Query-driven horizontal class partition ing in object-oriented databases. In G. Quirchmayr, E. Schweighofer, and T.J.M. Bench-Capon (eds.), The Ninth International Conference on Databases and Expert Systems (DEXA ’98). Lecture Notes in Computer Science No. 1460. Berlin: Springer-Verlag, 1998, pp. 692–701.

3. Bellatreche, L.; Karlapalem, K.; and Qin, L. Derived horizontal class partitioning in OODBSs: Design strategy, analytical model and evaluation. In T.W. Ling, S. Ram, and M.-L. Lee (eds.), Proceedings of Seventeenth International Conference on Conceptual Modeling (ER ’98). Lecture Notes in Computer Science No. 1507. Berlin, Germany: Springer-Verlag, November 1998, pp. 465–479.

4. Bellatreche, L.; Karlapalem, K.; and Simonet, A. Horizontal class partitioning in object oriented databases. In A. Hameurlain and A.M. Tjoa (eds.), Proceedings of the Eighth Interna tional Conference on Databases and Expert Systems (DEXA ’97). Lecture Notes in Computer Science No. 1308. Berlin, Germany: Springer-Verlag, September 1997, pp. 58–67.

5. Benzaken, V., and Delobel, C. Dynamic clustering strategies in the O2 object-oriented database system. Rapport Techique Altair, August 18, 1989, pp. 34–89.

6. Bertsekas, D., and Gallager, R. Data Networks. Englewood Cliffs, NJ: Prentice Hall, 1989.

7. Bhattacharjee, S. Development of integrated distributed computing environments: An infrastructure and resource planning model. Ph.D. dissertation, State University of New York, Buffalo, 1999.

8. Blair, G. and Lea, R. The impact of distribution on support for object-oriented software development. IEEE Software Engineering Journal, 7, 2 (March 1992), 130–138.

9. Booch, G.; Rumbaugh, J.; and Jacobson, I. The Unified Modeling Language (UML). Rational Software Corporation, Cupertino, CA, 2001, available at www.rational.com.

10. Cattell, R.G.G. Object Data Management. Reading, MA: Addison-Wesley, 1994.

11. Ceri, S., and Navathe, S.B. A methodology for the distribution design of databases. In Twenty-Sixth IEEE Computer Society International Conference (COMPCON), Digest of Pa pers. Los Alamitos, CA: IEEE Computer Society Press, February 1983, pp. 426–431.

30. Fung, C.W.; Karlapalem, K.; and Li, Q. Cost-driven evaluation of vertical class partitioning in object-oriented databases. In R.W. Topor and K. Tanaka (eds.), Proceedings of Fifth International Conference on Database Systems for Advanced Applications (DASFAA). Singapore: World Scientific, 1997, pp. 11–20.

12. Ceri, S., and Pelagatti, G. Distributed Databases, Principles and Systems. New York: McGraw-Hill, 1984.

13. Ceri, S.; Navathe, S.; and Wiederhold, G. Distribution design of logical database schemas. Transactions on Software Engineering, 9, 4 (1983), 487–504.

14. Chang, E., and Katz, R. Exploiting inheritance and structure semantics for effective clustering and buffering in an object-oriented DBMS. In Proceedings of the ACM SIGMOD Conference. New York: ACM Press, 1989, pp. 348–352.

15. Chari, K. Resource allocation and capacity assignment in distributed systems. Computers and Operations Research, 23, 11 (1996), 1025–1041.

16. Cheng, J., and Hurson, A. Effective clustering of complex objects in object-oriented databases. SIGMOD Record, 20, 2 (1991), 22–31.

17. Chidamber, S.R., and Kemerer, C.F. A metrics suite for object-oriented design. IEEE Transactions on Software Engineering, 20, 6 (June 1994), 476–493.

18. Chin, R., and Chanson, S. Distributed object-based programming systems. ACM Com puting Surveys, 23, 1 (1991), 91–124.

19. Chu, W.W., and Ieong, I.T. A transaction-based approach to vertical partitioning for relational databases. Computer Science Department Technical Report CSD-900043, Univer sity of California–Los Angeles, 1990.

20. Crowder, H.; Johnson, E.L.; and Padberg, M. Solving large-scale zero-one linear programming problems. Operations Research, 31, 5 (September–October, 1983), 803–834.

21. Darmont, J., and Gruenwald, L. A comparison study of object-oriented database clustering techniques. Information Sciences, 14, 1–4 (1996), 55–86.

22. Darmont, J., and Schneider, M. VOODB: A generic discrete-event random simulation model to evaluate the performances of OODBs. In M.P. Atkinson, M.E. Orlowska, P. Alduriez,

S.B. Zdonik, and M.L. Brodie (eds.), Proceedings of the Twenty-Fifth International Conference on Very Large Data Bases (VLDB 1999). Edinburgh: Morgan Kaufmann, 1999, pp. 254– 265.

23. Dowdy, L.W., and Foster, D.V. Comparative models of the file assignment problem. ACM Computing Surveys, 14, 2 (1982), 287–313.

24. Dynasty Product Suite. Dynasty Technologies, Kingwood, TX, available at www.dynasty .com, 2000.

25. Ein-Dor, P. Grosch’s law re-revisited: CPU power and the cost of computation. Communications of the ACM, 28, 2 (1985), 142–151.

26. Elmasri, R.; Weedryer, J.; and Hevner, A. The category concept: An extension to the entity-relationshipmodel. Data & Knowledge Engineering, 1, 1 (1985), 75–116.

27. Ezeife, C., and Barker, V. Vertical class fragmentation in a distributed object based system. In Proceedings of the Seventh International Conference on Computing and Information,

vol. 8. Los Alamitos, CA: IEEE Computer Society Press, July 1995, pp. 613–632.

28. Fisher, M., and Hochblaum, D. Database location in computer networks. Journal of the ACM, 27, 4 (1980), 718–735.

29. Forte. All About Forté. Sun Microsystems, Palo Alto, CA, available at www.sun.com forte, 2000.

31. Fung, C.W.; Karlapalem, K.; and Li, Q. Structural join index hierarchy: A mechanism for efficient complex object retrieval. In Fifth International Conference on the Foundations of Data Organization. Kobe, Japan, November 1998, pp. 121–130.

32. Gavish, B. Models for configuring distributed computer systems. IEEE Transactions on Computers, C-36, 7 (1987), 773–793.

33. General Algebraic Modeling System (GAMS) and Solvers. Washington, DC: GAMS Development Corporation, 1999.

34. Glover, F. Improved linear integer programming formulations of nonlinear integer programming problems. Management Science, 22, 4 (December 1975), 455–460.

35. Grosch, H.A. Grosch’s law revisited. Computerworld, 8, 16 (April 16, 1975), 24.

36. Gruber, O., and Amsaleg, L. Object clustering in Eos. In M.T. Öszu, U. Dayal, and P. Valduriez (eds.), Distributed Object Management. San Mateo, CA: Morgan Kaufmann, 1994, pp. 117–131.

37. Hale, D. A framework for distributed database fragment allocation utilizing semantic meta-data to compose data fragments. Ph.D. dissertation, University of Wisconsin–Milwaukee, 1986.

38. Henderson-Sellers, B. Object-Oriented Metrics: Measures of Complexity. Englewood Cliffs, NJ: Prentice Hall, 1996.

39. Hevner, A., and Rao, A. Distributed data allocation strategies. In M. Yovits (ed.), Advances in Computers, vol. 27. San Diego: Academic Press, 1988, pp. 121–155.

40. Hoffer, J.A., and Severance, D.G. The use of cluster analysis in physical database design.

In D.S. Kerr (ed.), Proceedings of the First International Conference on Very Large Data Bases. New York: ACM Press, September 1975, pp. 69–86.

41. Hogan, R. Usage Path Analysis. A Practical Guide to Database Design. Englewood Cliffs, NJ: Prentice Hall, 1990.

42. Iona. Orbix, An Implementation of OMG’s CORBA. Iona, Waltham, MA, 2001, available at www.orbix.com/products/orbhome.htm.

43. Jaaksi, A.; Aalto, J.M.; Aalto, A.; and Vatto, K. Tried & True Object Development: Indus try Proven Approaches with UML. New York: Cambridge University Press, 1999.

44. Jacobson, I. Object-Oriented Software Engineering. A Use Case Driven Approach, revised 4th printing. Reading, MA: Addison-Wesley, 1992.

45. Jain, H.K. A comprehensive model for the design of distributed computer systems. IEEE Transactions on Software Engineering, 13, 10 (1987), 1092–1104.

46. Jain, H.K., and Dutta, A. Distributed computer system design: A multicriteria decision making methodology. Decision Sciences, 17, 4 (1986), 437–453.

47. Karlapalem, K.; Navathe, S.; and Morsi, M.A. Issues in the distribution design of object oriented databases. In M.T. Öszu, U. Dayal, and P. Valduriez (eds.), Distributed Object Management. San Mateo, CA: Morgan Kaufmann, 1994, pp. 148–164.

48. Kettani, O., and Oral, M. Equivalent formulations of nonlinear integer problems for efficient optimization. Management Science, 36, 1 (January 1990), 115–119.

49. Kim, W. Introduction to Object-Oriented Databases. Cambridge, MA: MIT Press, 1990.

50. Kulkarni, U. An integrated support system for design of distributed databases. Ph.D. dissertation, University of Wisconsin–Milwaukee, 1989.

51. Kulkarni, U., and Jain, H.K. Interaction between concurrent transactions in the design of distributed databases. Decision Sciences, 24, 2 (1993), 253–277.

52. Lee, H., and Sheng, O. A multiple criteria model for the allocation of data files in a distributed information system. Computers & Operations Research, 19, 1 (1992), 21–23.

53. Levin, K., and Morgan, H. A dynamic optimization model for distributed databases. Operations Research, 26, 4 (1978), 824–835.

54. Lorenz, M., and Kidd, J. Object-Oriented Software Metrics. Englewood Cliffs, NJ: Prentice Hall, 1994.

55. Malinowski, E., and Chakravarthy, S. Fragmentation techniques for distributing object oriented databases. In D.W. Embley and R.C. Goldstein (eds.), Conceptual Modeling—ER ’97. Sixteenth International Conference on Conceptual Modeling. Lecture Notes in Computer Science 1331. Berlin, Germany: Springer-Verlag, 1997, pp. 347–360.

56. Meads, A. Clustering strategies for object databases. Ph.D. dissertation, Aston Univer sity, Birmingham, UK, 1997.

57. MIT Parallel and Distributed Operating Systems Group. Various research projects. MIT, Cambridge, MA, 2000, available at www.pdos.lcs.mit.edu/pubs.html.

58. Navathe, S.; Ceri, S.; Weiderhold, G.; and Dou, J. Vertical partitioning algorithms for database design. ACM Transactions on Database Systems, 9, 4 (December 1984), 680–710.

59. Object Management Group (OMG). Common Object Request Broker: Architecture and Specifications.Framingham, MA: Object Management Group, available at www.omg.org, 2000.

60. Öszu, M.T.; Dayal, U.; and Valduriez, P. An introduction to distributed object management. In M.T. Öszu, U. Dayal, and P. Valduriez (eds.), Distributed Object Management. San Mateo, CA: Morgan Kaufmann, 1994. pp. 1–24.

61. Otte, R.; Patrick, P; and Roy, M. Understanding CORBA. Englewood Cliffs, NJ: Prentice Hall, 1997.

62. Pirkul, H. An integer programming model for the allocation of databases in a distributed computer system. European Journal of Operational Research, 26, 3 (1986), 401–411.

63. Price, C., and Krishnaprasad, S. Software allocation models for distributed computing systems. In Proceedings of the Fourth International Conference on Distributed Computer Systems (DCS). Los Alamitos, CA: IEEE Computer Society Press, 1984, pp. 40–48.

64. Purao, S.; Jain, H.K.; and Nazareth, D.L. Distributing object-oriented applications. In M. Ajuga, D. Galletta, and H. Watson (eds.), Proceedings of Americas Conference on Informa tion Systems (AIS). Pittsburgh: Association for Information Systems, 1995, pp. 399–402.

65. Purao, S.; Jain, H.K.; and Nazareth, D.L. Derivation of traffic volumes for distribution of object-oriented applications. In J. Nunamaker and R. Sprague (eds.), Proceedings of Hawaii International Conference on System Sciences (HICSS). Los Alamitos, CA: IEEE Computer Society Press, 1996, pp. 119–128.

66. Purao, S.; Jain, H.K.; and Nazareth, D.L. A Tool for distribution of object-oriented applications. Working Paper, Georgia State University, Atlanta, GA, 2000.

67. Rumbaugh, J.; Blaha, M.; Premerlani, W.; Eddy, S.; and Lorensen, W. Object-Oriented Modeling and Design. Englewood Cliffs, NJ: Prentice Hall, 1991.

68. Ryant, I. Why inheritance means extra trouble. Communications of the ACM, 40, 10 (October 1997), 118–119.

69. Shannon, K., and Snodgrass, R. Semantic clustering. In A. Dearle, G.M. Shaw, and S.B. Zdonik (eds.), Implementing Persistent Object Bases, Principles and Practices. Proceedings of the Fourth International Workshop on Persistent Objects. San Mateo, CA: Morgan Kaufmann, 1990, pp. 389–402.

70. Shin, D., and Irani, K. Fragmenting relations horizontally using a knowledge-based approach. IEEE Transactions on Software Engineering, 17, 9 (1991), 1004–1009.

71. Stoyenko, A.D.; Bosch, J.; Aksit, M.; and Marlowe, T.J. Load balanced mapping of distributed objects to minimize network communication. Journal of Parallel and Distributed Computing, 34, 2 (1996), 117–136.

72. Tsangaris, M., and Naughton, J. A stochastic approach for clustering in object bases. SIGMOD Record, 20, 2 (1991), 12–21.

73. Wegner, P. Dimensions of object-based language design. In N.K. Meyrowitz (ed.), Conference on Object-Oriented Programming Systems, Languages, and Applications (OOPSLA 87). Orlando, FL: SIGPLAN Notices 22, 12 December 1987, pp. 168–182.

74. Wegner, P. Why interaction is more powerful than algorithms. Communications of the ACM, 40, 5, (May 1997), 80–91.

75. Wong, E., and Katz, R.H. Distributing a database for parallelism. In D.J. DeWitt and G. Gardarin (eds.), Proceedings of the 1983 ACM SIGMOD Conference, SIGMOD Record 13(4). New York: ACM Press, 1983, pp. 67–78.
