---
otero_id: 3602
otero_key: "JAC8YN2B"
title: "A declarative approach to composing web services in dynamic environments"
authors: "Therani Madhusudan; N. Uttamsingh"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2004.07.003"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A declarative approach to composing web services in dynamic environments

Therani Madhusudan<sup>\*</sup>, N. Uttamsingh

MIS Department, University of Arizona, 430 McClelland Hall, Tucson, AZ 85721, USA

Received 29 April 2003; received in revised form 16 July 2004; accepted 18 July 2004 Available online 1 September 2004

## Abstract

A recent trend in E-business is the deployment of a variety of web services by product and service vendors to facilitate B2B and B2C E-commerce. To utilize these web services effectively, customer’s have to (a) locate each of these services from service directories and retrieve brief service descriptions, (b) analyze service features and evaluate their applicability to the task at hand dynamically, and finally (c) invoke these services in a certain sequence to complete an overall business or personal need. Alternatively, intermediaries execute the aforementioned steps manually and provide a composite service for access from a single service platform. Both these approaches are highly tedious (either for the customer or intermediary) and non-scalable due to the volatility and size of the web. The dynamic nature of the availability and features of web services, real-time requirements on service composition and the large number of alternative combinations of service choices to fulfill a service need makes major demands on the service composition process.

This paper presents a novel declarative approach to facilitate dynamic and scalable web service composition called Integrated Service Planning and Execution (ISP&E) based on AI planning techniques. Implementation of an architecture for dynamic web service composition and execution based on a domain-independent AI planning framework called Hierarchical Task Network (HTN) planning is described in this paper. Simulated experiments highlight the effectiveness of our proposed approach which interleaves service composition and execution, to cope with dynamic service capabilities and service volatility.

<sup>D</sup> 2004 Elsevier B.V. All rights reserved.

Keywords: Web services composition; Interleaving planning and execution

## 1. Introduction

Web services are being promoted as a viable technology to develop the next generation of electronic marketplaces [60]. A web service is defined as a networked application that is able to interact using standard application-to-application web protocols over well-defined interfaces such as Simple Object Access Protocol (SOAP), and which is described using a standard functional description language such as Web Services Description Languages (WSDL) [35]. Examples of web services range from ordering books, buying travel tickets, booking rental cars, buying market research information to making restaurant reservations [68]. Some of these web services are elementary and some are composite. Elementary web services do not rely on other web services to fulfill external requests. In contrast, composite services integrate multiple component services (either elementary or composite) to fulfill a request. For example, a travel assistant service may combine car rental, hotel and possibly flight reservation services. Composition of elementary services is essential to the growth of the web services model of application interaction [5].

Consider, for example, that a customer wants to send a gift package consisting of flowers and a book to an acquaintance for a special occasion. In order to send the gift, he/she can assemble a (virtual) package consisting of tasks such as selecting and ordering flowers at a flower service, possibly at web sites such as www.Florist.com, www.FTD.com and selecting a book at an online bookstore, from sites such as www.Amazon.com, www.fatbrain. com and request that they be shipped to the acquaintance. This assembly process requires the customer to access two web services and possibly execute similar processes such as searching for the required flower or book to meet the occasion and then placing the order, providing the credit card information and shipping addresses, all of which may be repetitious. Further, if the gift package meeting ones’ needs are not available, it would require the customer to search through catalogs across multiple web services till the requisite package can be assembled and an order placed for the same. In the above example, two elementary services are composed into a composite gift-ordering service on-the-fly by the customer. A similar example in the context of freight management is illustrated in Ref. [50]. Current approaches to composing such services place the responsibility on the customer to define the sequence in which services are invoked, henceforth called a service plan. To ameliorate the customer’s task, the growth of value-adding intermediary services that provide such composite functionality is being promoted with the recent advances in commercial web services technology and standardization of business protocols [35]. However, establishing and managing such intermediary E-commerce services can be extremely burdensome both for business-to-business (B2B) and business-to-consumer (B2C) interactions for the following reasons:

! <sub>Dynamic</sub> <sub>availability</sub> <sub>of</sub> <sub>large</sub> <sub>numbers</sub> <sub>of</sub> <sub>web</sub> services with similar service capabilities: The multiple numbers of elementary services with similar capabilities make the combinatorial choices for a virtual package large. The set of similar services available is constantly changing as services are online or offline. For example, at a given time, such as when a customer is issuing a particular request, currently available services need to be located and then invoked to fulfill the request.

! <sub>Dynamic variety amongst service offerings: Serv-</sub> ices (even those advertised with similar capabilities) may differ amongst each other on a variety of criteria ranging from the products they carry, prices, discounts and after-sales support. These criteria need to be considered in terms of evaluating a particular service plan to fulfill a request. Composite services need to provide value-added benefits to clients in real-time, to be attractive to online customers. For example, evaluation of the overall cost of the gift package may need to consider multiple criteria such as delivery costs, reliability and lead-times.

! <sub>Dynamic</sub> <sub>constraint</sub> <sub>introduction:</sub> <sub>Elementary</sub> <sub>serv-</sub> ices when combined into a service plan may introduce a variety of additional constraints. For example, invoking an offshore web service may impose currency and import restrictions that may not be known a priori. In the gift shopping example mentioned earlier, books may be procured at the UK Amazon store, triggering the need for currency conversion. Even within a global organization (for example, an internationally coordinated supply-chain), constraints may be imposed due to changing logistic and service requirements. Detecting such new constraints and incorporating them into a currently executing service plan is essential.

! <sub>Changing</sub> <sub>customer</sub> <sub>requirements:</sub> <sub>The</sub> <sub>component</sub> elementary services of a service plan may be affected dynamically based on new customer needs that arise as the services are being invoked. For example, in the above gift-ordering example, the customer may decide to send a customized Ecard (concurrently as the flower service is being invoked), thus requiring access to an E-card service. This new request has to be incorporated in the current service plan and the plan may change depending on the cost considerations. Predefined web service sequences may restrict customer usability.

! <sub>Dynamic</sub> <sub>operational</sub> <sub>conditions:</sub> <sub>From</sub> <sub>an</sub> <sub>opera-</sub> tional perspective, as service plans are being executed, failures can occur for a variety of technological and application-specific reasons such as network congestion to product stock-out situations, and need to be gracefully handled. Implications of failures at one elementary service on other constituent services in the service plan need to be propagated, alternative service plans with recovery steps need to be re-planned and executed.

Consideration of these dynamic requirements in developing web services frameworks is essential. Developing robust web services infrastructures to meet the aforementioned needs has attracted significant research. Recent studies have focused on service execution and inter-service runtime coordination such as the Business Process Execution Language (BPEL) framework from IBM and the Self-Serv system [21,18,9]. The primary focus in these efforts has been on developing technologies for better process enactment such as service selection, service execution, fault tolerance and peer-to-peer service coordination. Service composition under static conditions is considered, assuming service capabilities do not change or services are always available. In these approaches, the effects of recovery strategies on service plans when services fail, such as service substitution or fault handling via compensation are predefined. The effective quality of a composite web service under dynamic conditions listed earlier is unclear. In realworld contexts, service capabilities and availability may change frequently and constraints amongst the component services in a service plan may emerge dynamically based on emerging customer requirements. Developing service plans that embed a priori knowledge to handle all possible contingencies during execution is nearly impossible. Deployment of largescale web service architectures requires approaches for robust initial web service plan generation, service re-planning and execution.

The focus of this paper is on developing a structured approach to integrated web service composition and execution. In a manner similar to Structured Query Language (SQL), which decouples the content of the query from how the query is to be processed, the proposed framework decouples description of enduser service requests from how the service is to be fulfilled. We present a declarative composition language based on a domain-independent AI planning framework for modeling service plans. In this article, the use of Hierarchical Task Network (HTN) planning [25] to facilitate service composition is described. HTN planning facilitates the generation of service plans given requirements of a service goal. Additionally, we discuss an integrated service processing framework called Integrated Service Planning and Execution, (ISP&E) consisting of interleaving service planning and service execution tasks. The ISP&E approach considers the dynamics of the environment during both planning and execution, with control strategies such as service re-planning and re-execution leading to design of robust service plans.

In this paper, service composition based on a service request (defined by the user) involves generating a service plan. Developing service plans efficiently consists of two key steps: (a) component service selection (composite or elementary) and (b) generating a service plan wherein the component service invocations are sequenced. We demonstrate service selection with the aid of domain-independent planning and illustrate how integrating planning and service plan execution can help in developing a web services composition framework that is responsive. Intermediary services that are needed to complete the task are seamlessly considered during the service planning phase. Our approach is complete in the sense that if a service plan exists (given all possible relevant services), it will be found given enough time. This approach is also sound in the sense that service plans generated will be validly executable. In the gift shopping scenario, if a feasible plan exists to procure the items within the given criteria, the planner will identify the same. In the worst-case scenario, an exhaustive search may be necessary and the planning time may not be bounded. Developing effective strategies for interleaving service composition and execution in such cases is discussed further in Section 5.

One of the key issues in developing web services is the development of well-defined semantics and resolution of semantic heterogeneity issues [24]. For purposes of our research, we consider the domain of product and service shopping and have developed the necessary ontology to illustrate the capabilities of the ISP&E architecture. Semantic issues in the context of web services and the development of essential ontologies are discussed in Refs. [39,47,23]. Details of the shopping domain ontology will be discussed as necessary in the ensuing sections.

Main contributions of this paper are: (a) the development of a representational and computational framework, for studying integrated planning and execution strategies in the context of web services, based on Hierarchical Task Network (HTN)-based domain-independent planning technology, and (b) an experimental study exploring the trade-off between service planning strategies such as re-planning and reexecution under dynamic conditions.

The rest of the paper is organized as follows. Section 2 provides background to web services and AI planning. In Section 3, we discuss web service models and service plan representation in the HTN framework. In Section 4, we describe our ISP&E approach including service processing strategies that interleave planning and plan execution. Section 5 reports a simulation-based study to evaluate the effectiveness of the ISP&E framework and examine the trade-offs between different service processing strategies. Section 6 discusses the implications of the proposed framework in the context of intelligent business process management. Concluding remarks along with future research directions are in Section 7.

## 2. Background and related work

The heterogeneity, autonomy and dynamic characteristics of web services makes the development of an integrated framework for web services composition and execution a formidable task. The basic architectural model of web services is illustrated in Fig. 1. In the framework, three key roles are identified: (a) service requestors, namely, customers; (b) service providers, namely, specific online businesses (who provide services such as S1, S2, S3, S31 and

![](/api/attachments/JAC8YN2B/fulltext/images/1c1599555cb6a2c3cc4db756d7beed3f85bc53b2ead35446566c2efc09dd49b7.jpg)  
Fig. 1. Web services architecture.

S32); and (c) service brokers, who maintain registries (catalogs) of services and their capabilities. Service providers publish the capabilities of their services (Step 0) and rules to access them via WSDL descriptions to these service registries which follow the Universal Description, Discovery and Integration (UDDI) standards [46,61]. Interaction amongst these three roles is supported by the service platform which provides facilities for service composition (Steps 2 and 3) and service execution (Step 4) for fulfilling service requests (Step 1).

The relationship between WSDL and UDDI is shown in Fig. 2. A business entity in UDDI indicates information about the business that may provide services such as names and contact information. A business service contains descriptive information about services such as service names and narratives. Business services may utilize business classification codes such as UNSPSC and NAICS [58,59]. Implementation-specific information on the service is described in the binding template. Binding templates include a tModel—technology model which contains machine-readable, implementation-specific information, on the business and a pointer to the actual service location defined by an access point. The machinereadable WSDL descriptions provide a minimal explicit characterization of the services in terms of both an implementation and interface definition. WSDL is adequate for describing elementary services as it takes a stateless view of services with welldefined inputs and outputs. From the URL provided by the access point, one may retrieve the WSDL which encodes actual information about the service and use the interface definition to enable appropriate exchange of SOAP messages. In summary, the metadata about services provided by UDDI includes a reference to a service description (WSDL) based on an predefined service taxonomy. Customers request services from service platforms. The service platforms execute the task of locating tModels and acquiring the necessary WSDL descriptions. Services are located based on possibly registry-specific UDDI taxonomy and the actual description (the WSDL) is obtained via the access point. For example, services S1, S2, S31 and S32 publish to the UDDI registry. Services may be composed in advance, registered by a service provider and used to service multiple requests. For example, service S3 composed of services S31 and S32 may be predefined manually by an intermediary provider. However, under volatile conditions, such advanced composition may be unreliable during execution if component service capabilities or predefined assumptions on the composite behavior required change.

![](/api/attachments/JAC8YN2B/fulltext/images/61982d37efc29c74f96c8d5642276094799ada33500de35d962dcccdf4823335.jpg)  
Fig. 2. Relationship between UDDI and WSDL.

Recent research has focused on developing advanced service composition and execution components of the service platform of Fig. 1. Scaling up utilization of web services in open, dynamic environments would require automated support for service design, service redesign and execution. We provide an overview of major challenges in facilitating automated service composition and discuss the applicability of AI planning techniques to this task. Additionally, we also consider the dynamics of the execution environment on the service composition process and provide a summary of the current state-of-art in developing service platforms.

## 2.1. Web service composition

Facilitating web service composition is a major step towards large-scale adoption of web service technology to enable E-business. Unlike traditional business processes that are repetitive and executed in a predictable manner, web services on the Internet have to cope with a highly dynamic environment.

Service processes should be able to adapt to changes in service capability and availability and to changing customer needs in a transparent manner.

The basic process of interactive web service composition as supported by current technologies in the domain of travel planning is illustrated in Fig. 3. We assume that various web services such as car rentals, flight rental and hotel reservation services have published in advance (Step 0 in figure) their web services in (WSDL) to an UDDI-based service registry from which these services can be located. Consider the common example scenario where a customer assembles a package consisting of a flight, hotel reservations and a car rental. The typical steps for manually invoking a single service are:

! <sub>Find</sub> <sub>the</sub> <sub>services</sub> <sub>based</sub> <sub>on</sub> <sub>a</sub> <sub>category</sub> <sub>code</sub> <sub>of</sub> NAICS (Step 1).

! <sub>Filter</sub> <sub>the</sub> <sub>services</sub> <sub>provided</sub> <sub>by</sub> <sub>the</sub> <sub>businesses</sub> <sub>based</sub> on a category code of UNSPSC.

! <sub>Find</sub> <sub>access</sub> <sub>points</sub> <sub>from</sub> <sub>binding</sub> <sub>templates</sub> <sub>in</sub> <sub>the</sub> filtered services description.

! <sub>Find</sub> <sub>tModels</sub> <sub>by</sub> <sub>using</sub> <sub>the</sub> <sub>tModel</sub> <sub>key</sub> <sub>provided</sub> <sub>in</sub> the binding templates

! <sub>Find the locations of WSDL documents from the</sub> tModels

![](/api/attachments/JAC8YN2B/fulltext/images/763a03062fd1186b7338165bbc4cfbf814abd4a5fb9a104986833c0782c013dc.jpg)  
Fig. 3. Composing a service providing a travel package.

! <sub>Retrieve WSDL documents from the locations</sub>

! <sub>Invoke</sub> <sub>services</sub> <sub>by</sub> <sub>referring</sub> <sub>to</sub> <sub>the</sub> <sub>access</sub> <sub>points</sub> and the WSDL documents (Steps 2 and 3).

The above steps are executed for each service (flight, hotel and car rental services) in an order of service requests defined by the customer or predefined by an intermediary provider. During service execution, data and constraints between the services, such as airport constraints and arrival/departure information, need to be input manually and checked by the customer. Even while invoking a single service, reasoning among constraints and making choices can be complex. The task of flight reservations involves decision-making regarding seat selection, choices amongst alternative flights, pricing and discounts. An intermediary may provide a composite service with all the tasks presequenced and support services (for service-specific information) preincluded. A service platform may facilitate execution of such a composite service. However, dynamic changes to either customer requirements or service capabilities may render such a priori composition ineffective. The service plan definition for such composite services is hard-coded as a sequence of SOAP calls, by the intermediary, possibly with limited flexibility for service definition and execution.

Current approaches to service discovery, composition and execution exhibit the following limitations of UDDI and WSDL technologies:

! <sub>UDDI</sub> <sub>supports</sub> <sub>search</sub> <sub>for</sub> <sub>services</sub> <sub>based</sub> <sub>on</sub> service metadata and not really based on actual service descriptions that characterize a service. Service registries need to include declarative descriptions of conditions of service use and side-effects of service usage need to be provided for selecting a service.

! <sub>Once</sub> <sub>a</sub> <sub>service</sub> <sub>is</sub> <sub>located,</sub> <sub>WSDL</sub> <sub>descriptions</sub> <sub>of</sub> the service do not describe in detail effects of service actions (operators or methods). WSDL descriptions do not provide information on preconditions to execute a service action (method) in an explicit manner. Further, contextual information to cope with issues such as service cancellation, service authorization and payments is not explicitly described. This precludes reasoning about services and their capabilities in an explicit manner during service composition.

! <sub>WSDL is a stateless description. Execution of</sub> composite web services requires the maintenance of a service state at the service platform to facilitate exchange of data and control between services. Though current service platforms provide this ability in an implicit form, an explicit state representation is required to reason about interaction between elementary services. There is a lack of sufficient process control capabilities (based on state descriptions) to cope with dynamic changes. Though the notion of fault handlers and compensating transactions have been proposed in service programming languages such as Business Process Execution Language [21] based on workflow technologies, their viability in a web services context is yet to be evaluated.

Steps in facilitating automated dynamic service composition are as follows: (a) Given a customer request, locate possible services (based on adequate descriptions) that are currently available and may possibly be combined to meet the request; and (b) develop an execution order among the services such that the necessary control and data flow constraints among the services are satisfied. Step (a) involves resolving semantic issues regarding service descriptions and bindings, matching requirement descriptions with service capabilities and ensuring service availability. Step (b) involves checking inter-service constraints such data ordering between services (for example, reserving flights before car rental to provide arrival and departure timing information) and evaluating service plan quality. Research efforts towards facilitating the above steps have adopted techniques from workflow management systems. eFlow is a service platform based on facilitating service process composition and enactment [18]. The composition approach in Ref. [18] is based on adapting templates of predefined composite processes. A similar approach is advocated in the development of Business Process Execution Language(BPEL) [35,21]. BPEL is an XML-based language and provides conventional control flow and data flow programming constructs to manually program the interaction between components of a composite service. BPEL provides constructs to explicitly refer to web services methods and manage the data flow between services. The program defining a composite web service is interpreted by an execution engine in a manner similar to workflow systems. Managing programs defining composite services in BPEL exhibit the same problems as managing workflow models such as inflexible definitions and lack of robustness to changes in the execution environment. Composition in the Self-Serv system is based on manually defining state transition diagrams wherein substates identify component services [8]. Semantic composition based on ontologies is addressed in Ref. [17]. Composition is enabled by matching service capability descriptions to requirements based on similarity measures. A variety of agent-based approaches to service execution and coordination based on exploiting the flexibility in agent systems have been proposed in Refs. [10–12]. Approaches addressing service composition from a software perspective include: (a) enabling component-based design of large-scale distributed systems [4,64,41], and (b) developing effective resource allocation mechanisms in mobile and distributed environments for intelligent execution [19,28]. In the approaches discussed above, the service platform functions like a workflow execution engine performing tasks of dispatching service calls, receiving responses, mediating and transforming intermediary data for manually defined service plans, thus executing all the steps in a service plan. Strategies to cope with failure may be domain- or programmer-dependent but are encoded in the service definition before execution. Such approaches cannot address all possible exigencies that may be encountered during execution. For reliable and large-scale business process management, more robust techniques are required as outlined in Ref. [16].

One of the possible approaches to service composition is the utilization of AI planning techniques as suggested in [37,38,49]. Planning techniques have been successful in the context of building complex robotic and enterprise systems adapting to dynamic conditions [65]. The main features of AI planning are summarized in the following section.

## 2.2. AI planning

AI planning involves generating a network of actions (or operators), i.e., a plan, that transforms a world state from an initial state to a goal state. An operator is a parameterized function that transforms a given state into a new state if the operator is applicable in the given state. The parameters to the operator provide access to the various entities in the current state and the new values that their current values may need to be changed $^ { \mathrm { t o , } }$ in order to evolve into the new state. More specifically, a plan is composed of (a) a sequence of operators with a temporal ordering constraint, i.e., $O _ { i } { < } O _ { j }$ implies that operator $O _ { i }$ must occur sometime before operator $O _ { j } ;$ and (b) for each parameterized operator $O _ { i } ;$ a set of parameter values that can be applied to the current state to transform it into a new state. A simple formulation of the classical planning problem defines three inputs also called the domain description [54]:

! <sub>a</sub> <sub>description</sub> <sub>of</sub> <sub>the</sub> <sub>initial</sub> <sub>state</sub> <sub>of</sub> <sub>the</sub> <sub>world</sub> <sub>in</sub> some formal language, usually first-order predicate logic and its variants

! <sub>a description of the goal, i.e., the final state of the</sub> world in the same formal language as above.

! <sub>a</sub> <sub>description</sub> <sub>of</sub> <sub>the</sub> <sub>possible</sub> <sub>operators</sub> <sub>that</sub> <sub>can</sub> <sub>be</sub> performed.

A domain-independent planner’s output is a sequence of operators—a plan—which, when executed in a world satisfying the initial state description, will achieve the goal. This abstract definition defines a class of problems parameterized by the languages used to represent the worlds, goals, and actions. The capabilities of domain0independent planners vary based on the expressivity of languages used, assumptions of time, deterministic effects, etc. Many approaches to solving these planning problems under different contexts have been proposed in the literature and readers are referred to Refs. [63,30] for more details. Advances in the speed and performance of AI planning algorithms over the past decade make it feasible to embed them in real-world application contexts.

Recently, domain-independent AI planning techniques have been adopted by researchers to make the traditional (database-oriented) query planning approaches more applicable to facilitate mediatorbased information integration of information sources in distributed and dynamic environments [34]. Planning techniques have been applied in the context of workflow modeling and verification [57,5]. Applicability of planning in the context of web services has been briefly discussed in Refs. [37,39] with proposals towards developing customized planners. In Ref. [37], the focus of planning is to generate interaction sequences for message exchange. In this paper, we develop a similar framework to service processing in dynamic environments using a domain-independent planning framework. Facilitating dynamic on-the-fly service composition is a key step towards scalable and robust web services frameworks. Current approaches (as discussed in the previous section) to web services composition assume a closed world assumption, i.e., the world dynamics is predictable before service planning is initiated. Web services are manually composed via a graphical interface (possibly like a workflow build-time system [35]) and then executed. In real-world situations, web services may be unstable, web service capabilities may vary dynamically, and the network environment is hard to predict. This may lead to execution failure of manually created composite services. Failure to recognize the dynamic factors in the application environment may adversely affect the system performance and its potential use. A proposal for planningbased approaches to web services composition is presented in Ref. [56].

In this paper, we present a service plan generation and execution architecture in the context of web services deployment that addresses problems associated with the open world assumption and dynamic service capabilities. The ISP&E architecture is based on a domain-independent planner called Simple Hierarchical Ordered Planning (SHOP) [25,43,44] for dynamic service planning. SHOP is based on the Hierarchical Task Network planning technique. Our choice of this methodology for planning-based service composition was guided by several considerations which we discuss below.

Firstly, we provide a brief background on the stateof-art in planning methodology before outlining our rationale. Two generic classes of planning algorithms have been developed in the literature, namely, partial order planners and total order planners [54]. Partial order planners develop project networks, consisting of directed networks of actions, whereas total order planners develop a plan with sequential actions. A given partial order plan may be linearized into multiple sequential plan alternatives. Partial order planners search in plan space, whereas total order planners search in state space. A variety of algorithms have been developed for both types of planners, based on techniques such as constraint satisfaction, logic resolution and theorem proving, satisfiability and model checking [54]. Partial order planners embed a leastcommitment strategy and the plans they generate are inherently flexible because of their networked nature. However, developing such partial order plans incurs higher plan search costs unlike state-space planners which have exhibited excellent performance on large problems. Recent research in AI planning has been focused on developing plans involving concurrent and durative actions for both partial and total order planners. However, developing such plans with parallel actions requires explicit temporal models for actions such as their durations and metric models of resources in the plan representation. Consideration of such numeric quantities considerably increases the size of the search space [6,54]. Developing efficient and scalable algorithms for temporal and metric reasoning in planning domains is an active research area whose results may be incorporated in our framework in future. An alternative approach used in our framework is first the generation of totally ordered sequential plans followed by the relaxation of precedence constraints to generate partially ordered plans [7,66]. Details are further discussed in Section 4.

In the web services domain, our choice of a planning approach was guided by the need for (a) performance, (b) the ability to embed domain knowledge to guide and control the search for a viable plan, and (c) an explicit state representation to enable interleaving of planning and execution. These criteria guided our decision to develop ISP&E based on a state-space, linear-order planning algorithm. The benefits of exploiting concurrency (in parallel plans), to provide better response times during execution over the additional search cost incurred in temporal partial order planning, for establishing concurrency, are yet to be studied. Additionally, in the web services context, durations of the actions are unbounded and nondeterministic, which adds to the complexity of temporal reasoning that may be required. Further, when failures occur, control strategies for interleaving planning and concurrent action execution in a distributed environment can be complex. However, in a linearized sequential plan generated via a state-space planner, the current execution state (upon failure) can be reconciled with its corresponding representation in the planner and re-planning initiated accordingly. We also observed that in practice, interactively created service plans do not have a large number of intermediary steps, wherein concurrency can be effectively exploited. Further, if web service transactions are not long-running, benefits of developing plans with concurrent actions may be minimal. Thus our initial evaluation of the ISP&E approach described in Section 5 is conducted for sequential plans.

There are two types of total order, state-space planning techniques, one based on state space search, (either forward to goal or backward from goal) and the other, namely Hierarchical Task Network (HTN) planning, which uses task decomposition to partition its state space effectively. State-space, search-based techniques require finely tuned heuristics to work effectively in large state spaces. In contrast, HTN planning provides the following benefits: (a) It enables embedding domain knowledge to control search space and improve efficiency of the state-space search in multiple ways. It has been successfully used in a variety of real-world planning-based applications. (b) It allows inclusion of different types of precondition constraints for service operators. SHOP’s knowledge of the current state during planning enables incorporation of powerful reasoning mechanisms, including calls to external systems. (c) It is extensible to include metric and temporal constraints for consideration of concurrency [69]. (d) It enables modeling process abstractions in terms of method/operator hierarchies. (e) It enables reuse by facilitating selection of appropriate methods from domain-related methods and operator libraries based on a combination of user and default domain preferences. These benefits of HTN planning support its use in an exploratory planning-based approach for service composition. We chose the SHOP planner for modeling service composition as it is a robust implementation of the HTN planning technique and has performed well in international planning competitions [51].

We use a two-step approach to enabling dynamic service composition in the ISP&E framework based on the SHOP planner. In the first step, a service plan is generated based on a logical description of web service methods modelled as operators, domain-dependent composition rules and service requirements modelled as initial and goal states. In the second step, the abstract logic-based service plan is transformed into a sequence of XML-based method calls to web services and then executed. In the shopping domain, during planning in the first step, the latest world information such as product availability and prices in a web service catalog is obtained from the web services. Based on this information, a service plan consisting of a sequence of web service operators is generated. In the second step, failure during execution of the service plan or interruption may lead to re-planning. Thus in the ISP&E framework, planning and execution of web service operators is interleaved. This interleaving enables the SHOP planner to incorporate the latest dynamic information regarding web service characteristics to facilitate choice among alternative plans during re-planning. In the ensuing section, we formally describe the basic elements of the ISP&E framework.

## 3. Composing web services

Facilitating dynamic and automated web service composition is a key enabling technology towards widespread usage of web services technology. Web service composition needs to locate the correct set of services and develop a service plan to invoke operators at these services in the correct order. A service platform needs to determine which service requests can be feasibly processed and which requests cannot be fulfilled. Further if a request can be met, it must be processed reliably under dynamic conditions. In this section, we present our approach towards web services composition considering the dynamics of the environment during service composition and execution. Our approach consists of the following: (a) models of elementary web services and service requests, and (b) representation of composite services as service plans. The formal description of these models along with an evaluation scheme for service plans are described in the ensuing section.

## 3.1. Modeling elementary web services

Elementary web services (denoted S ) in Fig. 1 provide a collection of basic operations. For example, a shopping web service such as Amazon provides nearly 20 operators amongst which are (a) methods for different types of searching their catalogs, customer and seller profiles, and (b) methods for managing a shopping cart [2]. Intermediary services use these methods at their sites to access information from Amazon’s back-end systems. In our framework, we model each elementary web service as having multiple operators (also referred to as operations, actions or methods). The collection of these operators define the capabilities of a web service. A capability of a web service is the kind of operations that can be requested of the web service [27]. For example, there are many kinds of browsing capabilities at Ref. [2], each different based on the kind of search input. Similarly, there are different kinds of payment capabilities, based on the kind of payment choice. Each web service capability is triggered by a request and generates an appropriate response. Each possible type of request–response pair is called a service operator $s _ { i j }$ for service i and capability j, $1 \leq i \leq N$ and $1 \leq j \leq M ,$ , where N is the number of services and M is the maximum number of capabilities per service. Assume that each request to a service operator is made in terms of a set of input data bindings $b _ { \mathrm { i } }$ and the operator returns the results in terms of output bindings $b _ { \mathrm { o } } , 1 { \le } i { \le } P$ and $1 \leq j \leq Q$ , where $P$ and $\boldsymbol { Q }$ denote the maximum number of input and output arguments per operator, respectively.

In our framework, web service operators are classified into two types, namely, (a) informational operators and (b) transactional operators. For example, consider the following service operators in Table 1 defined by the WSDL from a shopping service. The first column describes the basic functionality of each operator. Informational operators provide information regarding the state of the service or the knowledge of the world maintained by the service. For example, all the three operators, $s _ { 1 - 3 } ,$ in Table 1 are informational operators. Transactional operators, $s _ { 4 \scriptscriptstyle - }$ <sub>5</sub> update the world state. For example, the payment operator in Table 1 updates the world state by making a payment and generating an order. During web services execution, both informational operators and transactional operators may need to be invoked. Information gathered enables planning a sequence of transactions. For example, browsing a catalog enables making a purchase. We discuss the interleaving of these operators during service composition in Section 3.3.

The first two operators in Table 1 are search operators whereas the third manages a shopping cart. The operator in the first row uses a person’s name as a binding for Author and returns a set of all books written by the author with information of their title, price and category. The operator in the second row returns all book titles belonging to a given category. The third operator returns a list of all current items in the cart. The fourth operator takes the current shopping cart information, the customer credit card information and approved payment to generate a final order. The fifth operator updates the shopping cart with new items. Additionally, each service capability $s _ { i j }$ may have constraints on both the input and output bindings such as range of possible domain values for each attribute in both input and output bindings of an operator. For example, the first operator may only return books of a certain category or may return titles consisting of only authors whose names start with the letter A. Constraints may also define the necessary preconditions that need to be satisfied in the world to execute a method and also define postconditions that may be satisfied when the operator execution completes successfully. We denote these constraints as $( c _ { i j } ^ { \mathrm { { i } } } ,$ $c _ { i j } ^ { \mathrm { o } } )$ for input and output constraints. In general, the constraints $( c _ { i j } ^ { \mathrm { i } } , ~ c _ { i j } ^ { \mathrm { o } } )$ are defined by unary, binary and higher-order, application-specific predicates that define preconditions for accessing a web service and required after-effects (postconditions) after successful service invocation.

Service operators for a shopping service

<table><tr><td>Operator type</td><td>Input bindings</td><td>Output bindings</td></tr><tr><td>Search/Informational,  $s_{11}$ </td><td>Author</td><td>Title, Price, Category</td></tr><tr><td>Search/Informational,  $s_{12}$ </td><td>Category</td><td>Title</td></tr><tr><td>Query/Informational,  $s_{13}$ </td><td>ShoppingCartID</td><td>Item, Price, Quantity</td></tr><tr><td>Transactional,  $s_{14}$ </td><td>ShoppingCartID, CreditCardInfo, Payment</td><td>OrderID</td></tr><tr><td>Transactional,  $s_{15}$ </td><td>ShoppingCartID, Item, Quantity</td><td>ShoppingCartID</td></tr></table>

To summarize, each service Si is represented by a set of service operators and each such operator is denoted by $( s _ { i j } , ~ c _ { i j } ^ { i } , ~ c _ { i j } ^ { 0 } )$ . Each service platform maintains a catalog of currently available web services and their service operators. Two types of web service operator definitions are maintained at the service platform catalog, namely, (a) a declarative definition described by the aforementioned formalism, and (b) a procedural definition describing the WSDL method calls for that service. Every declarative definition has a corresponding procedural definition to enable execution. The declarative definitions are created based on the WSDL definition and background domain knowledge. The status of services in the catalog is constantly updated by a concurrently running monitoring service in the ISP&E framework.

During interleaving of planning and execution in the ISP&E framework, planning utilizes information gathering operators to develop a service plan consisting of transactional operators. Re-planning (upon failure or changed conditions) utilizes the latest service operator information obtained from the catalog, to cope with the world dynamics. The monitoring cost of acquiring information related to the changes in number of active web services or functional changes to existing web services can be significant. This cost has to be evaluated with respect to the potential benefit of exploiting the new information in an opportunistic manner during planning. Further discussion on our initial studies on understanding this trade-off is discussed in Section 5.

## 3.2. Modeling service requests

Customers access web services via service platforms which are responsible for invoking methods at web services during execution. In the framework, service requests to the platform are classified into two types: (a) information seeking requests, and (b) transactional requests, including information update and decision-making tasks. For example, a service platform supporting the gift packaging scenario has to support information gathering (searching catalogs), decision-making (comparing prices of items with budget) and transactional (placing orders and making payments) tasks. In the ISP&E framework, we support both types of requests. Support for information gathering in ISP&E has been discussed in the context of information integration in [52,33]. In this article, we discuss service composition for transactional requests since it subsumes information gathering tasks.

Transactional service requests can be specified in terms of the following: (a) the set of tasks to be completed and the initial inputs, or (b) the initial inputs and final outputs. Further, these requests can include constraints on the request inputs, request outputs, intermediary process states, component service inputs and outputs. Service requests, denoted $\mathrm { S R } _ { i } ,$ to a platform are modelled in terms of the following tuple, $( ( t _ { 1 } , \ t _ { 2 } , . . . ) , \sigma _ { \mathrm { i } } , \ \sigma _ { \mathrm { f } } , \ c ^ { i } , \ c ^ { \mathrm { i n t } } , \ c ^ { \mathrm { o } } ) . \ t _ { i }$ denotes the tasks requested; $\sigma _ { \mathrm { i } }$ and $\sigma _ { \mathrm { f } }$ denote the description of the initial and final states, respectively; $c ^ { \mathrm { i } } , \ : c ^ { \mathrm { i n t } }$ and $c ^ { \mathrm { o } }$ denote the input, intermediate and output constraints, respectively.

## 3.3. Modeling the service platform

Given service requests, SR , the role of the service platform is to identify services $S _ { i }$ (from its current service catalog) that can fulfill the request and then generate a service plan consisting of a sequence of transactional service operators. During service planning, additional steps may be performed at the service platform to facilitate: (a) decision-making operations, (b) packaging of data for inputs to web services methods, (c) extraction of data from outputs of web services, and (d) support intermediary storage and transformations of data. These computational steps may be modelled explicitly as operators at the service platform or as intermediary and auxiliary procedures executed by the planner. Further, the service platform may provide a variety of additional functions to query the current state of execution and schedule service access. In the current ISP&E framework, we model the decision-making and data management service platform functions as operator precondition evaluations executed by the planner.

## 3.4. Representing composite services as service plans

Service requests to the platform can be fulfilled possibly by a single operator invoked at a single elementary service $S _ { i }$ or by a combination of operator invocations at one or more elementary services. The sequence of multiple operator invocations to fulfill a particular service request defines a composite service.

A composite service invokes methods at possibly multiple elementary services or other statically defined composite services. A composite service can be created by a service platform either at compile-time and reused to serve many requests (a static composite service) or created dynamically when a service request is received by the platform. Dynamic composite services may exist for the duration of fulfilling the service request. We define a composite service (both dynamic and static) as a service plan, which is a sequence of transactional service operators invocations that fulfill the service request. The composite service, denoted $\mathrm { { S C } } _ { i } ,$ is made up of a sequence of $s _ { i j }$ operators. For example (with reference to Table 1), a service request to buy a collection of books at one online book web service may be fulfilled with the following service plan: $s _ { 1 5 } \mathrm { ( C a r t I D , }$ Title1, $1 ) { \longrightarrow } _ { S _ { 1 5 } } ( \mathbb { C } \cap \mathbb { C } \mathbb { 1 } \mathbb { D } .$ $\mathtt { T i t 1 e 2 , 5 ) } { \longrightarrow } _ { S _ { 1 4 } } ( \mathtt { C a r t I D , C a r d I n f o }$ , Payment). The symbol Y denotes the sequence of invocation of the operators. The fields in the parenthesis denote input bindings to the operators. $s _ { 1 5 } ( ^ { * } )$ adds selected books to the shopping cart and $s _ { 1 4 }$ executes the payment transaction. Operators $s _ { 1 1 } , \ s _ { 1 2 }$ and $s _ { 1 3 }$ from Table 1 are used during planning to identify available books at the online bookstore. The task of service planning is to develop such transactional plans from the available catalog of web service operators. The service execution module of the service platform executes each web service operator according to the plan till the service request is fulfilled.

Service planning can generate a variety of alternative service plans to fulfill a request if multiple web services providing common services are accessible from the service platform. If multiple bookstores are available as web services, alternative plans may be developed. Two plans can differ based on the combination of service operators (due to their respective service capabilities) and the intermediary operations at the platform. When a service request is issued to the platform, it is a priori unclear if a plan can even be formulated. In the ISP&E framework, the SHOP planner will search the complete plan space for alternative plans or fail based on a timeout mechanism.

## 3.5. Service plan optimization

Service plan optimization is performed to facilitate selection of a good plan from among the various plan alternatives based on a generic notion of cost and/or response time [15]. In conventional distributed systems, reliable cost statistics such as network response time, service update frequency, service availability, etc., are available from the services and are assumed to change slowly. However, in a dynamic and open environment, obtaining such statistics from web services is usually not possible. Though such statistics may be collected and maintained at the service platform based on historical usage, during service planning, these estimates may lead to suboptimal plans under current execution conditions.

In this paper, we model the operator costs both at the platform and at the services in terms of time units and the best service plan is considered to be the one with minimum execution time. The cost of a service operator [1] $s _ { i j }$ for service i (as perceived at the platform) consists of two components, the time taken to process the service request at the web service $( c _ { i j } )$ and the total transmission time to transfer the results from the service to the platform $( t _ { i j } ) _ { : }$ , where $t _ { i j }$ is the network transmission time per result. In our cost model, we assume the time to transmit the request from the platform to the service to be negligible. Under dynamic conditions, $t _ { i j }$ varies as the service and network characteristics change. Thus each service operator cost is in terms of total time units to issue the request and obtain the response $( c _ { i j } + t _ { i j } )$ and varies dynamically. We assume all the output needs to be received at the platform before the ensuing operator in a service plan can be executed. In the current framework, the cost of platform operator executions is considered negligible. Given these measures, the total cost of a service plan consisting of transactional service operators can be estimated as $\sum ( c _ { i j } + t _ { i j } )$ for all service operators.

Service planning approaches discussed in Section 2 make a closed-world assumption that operator cost and service characteristics do not change during service processing. Our basic model described in this section relaxes the assumption and considers service processing under dynamic conditions. We explicitly incorporate execution in the overall service processing cycle to consider dynamic information from open environments. In the following section, we describe the details of the integrated service planning and execution framework that utilizes the above model to perform service composition and execution.

## 4. Integrated Service Planning and Execution

Service planning in our framework is the generation of alternative sequences of transactional service operators for a given service request. The overall service planning and plan execution cycle is illustrated in Fig. 4. Service requests are received from the user in terms of a declarative goal-driven language (1, 2), service plans are generated (3), verified (4) and then executed (5). Changes in the execution environment (world conditions) are checked periodically (6), triggering replanning (6.2) from the current state, during which, the service platform incorporates the latest available information to develop a new service plan and reexecute the same. Alternative strategies include reexecuting (6.1) the remainder of the original plan from the current state with the belief that the environment will return to a more conducive state in the near future.

Section 5 discusses our experiments on several designs of reactive strategies towards interleaving plan generation and execution. The following sections describe two key phases of our framework, namely, the plan generation phase and the plan execution phase.

## 4.1. Service plan generation

Service planning in our framework is done by modeling the service planning problem in terms of a domain-independent planning framework called

Hierarchical Task Network (HTN) planning. In the following subsections, we provide an overview of HTN planning and describe the modeling of the service planning task in terms of the HTN approach.

## 4.1.1. HTN planning

HTN planning is a technique that creates plans by task decomposition. The planning problem is specified by an initial task network, which is a collection of tasks that need to be performed under a specified set of constraints. The planning process decomposes tasks in the initial task network into progressively smaller subtasks until the task network contains only primitive tasks or operators. The decomposition of a task into subtasks is performed using a method from a domain description. A method specifies how to decompose the task into a set of subtasks. Each method is associated with various constraints that limit the applicability of the method to certain conditions and define the relations between the subtasks of the method. HTN planning performs recursive search of the planning state space via task decomposition and constraint satisfaction. Readers are referred to Refs. [44,43,25] for further details. HTN planning techniques have been implemented in a variety of systems such as O-Plan [22] and SIPE [65]. For our research, we have used the Simple Hierarchical Ordered Planner (SHOP) system [44]. SHOP has been implemented in LISP and uses a lisp-like lambda calculus formalism. We briefly describe the key syntactic and semantic elements of the HTN approach relevant to our service planner implementation based on [44].

![](/api/attachments/JAC8YN2B/fulltext/images/e61fbc821c3dbcf3946e32046340656c5d716a8511ea79a8b3a954c53956e9e3.jpg)  
Fig. 4. Integrated Service Planning and Execution cycle.

SHOP uses first-order logic definitions of variable and constant symbols, function and predicate symbols, atoms, conjuncts, most general satisfiers and Horn clauses. A state is a set of ground atoms and an axiom set is a set of Horn clauses. If S is a state and X is an axiom set then S<sub>v</sub>X satisfies a conjunct C if there is a substitution u called a satisfier such that S<sub>v</sub>X entails C. u is a most general satisfier (called mgs in short) if there is no other satisfier v more general than u. A task is a list of the form $( s , \ t _ { 1 } , t _ { 2 } , . \ . \ t _ { n } )$ where s (the task’s name) is a task symbol and $t _ { i }$ (the task arguments) are terms. The task is primitive if s is a primitive task symbol (denoted !s) and it is compound otherwise. A task list is a list of tasks. An operator is an expression (:operator $\mathrm { ~ h ~ c ~ D ~ A ~ }$ where h (the head) is a primitive task, c is a list of preconditions and D and A (the deletions and additions) are sets of atoms containing no variable symbols than those in h. For example, a primitive operator in our context is a web service operator or a data manipulation operator at the platform. Primitive operators manipulate the state description of the planning domain. A method is an expression of the form (:method h C T) where h is a compound task, C is the methods precondition defined as a conjunct and T is a list of tasks.

The intent of an operator o<sup>w</sup>(:operator h c D A) is to specify that h can be accomplished by modifying the current state of the world by removing every atom in D and adding every atom in A. More specifically, if t is a primitive task and there is an mgs u for t and h such that $h ^ { u }$ is ground, then o is applicable and the list $h ^ { u }$ is a simple plan for t. If we execute this plan in some state S, it produces the state $h ^ { u } ( S ) { = } o ^ { u } ( S ) { = } ( S { - } D ^ { u } ) \cup A ^ { u }$ . The intent of a method m<sup>w</sup>(:method h C T) is to specify that if the current state of the world satisfies C, then h can be accomplished by performing the tasks in T with a specified ordering. More specifically, let S be a state, X be a set of axioms and t be a task atom. Suppose there is an mgs u that unifies t with h and suppose S<sub>v</sub>X satisfies $C ^ { u }$ , then m is applicable to t in S<sub>v</sub>X and the result of applying m to t is the set of task lists $R { = } \{ ( T ^ { u } ) ^ { \nu } \colon$ v is an mgs for $C ^ { u }$ from $S \}$ . Each task list $r { \in } R$ is a simple reduction of t by m in S<sub>v</sub>X.

A plan is a list of heads (in the lambda calculus sense) of ground operator instances. If p is a plan and S is a state, then $p ( S )$ is the state produced by starting with S and executing the operator instances in the given order. Given a service request as a tuple $P { = } ( S ,$ T, D) where S is the initial state (defined by the services available and the budget), T the task list (consisting of the items to be procured) and D a domain description consisting of a set of operators, axioms and methods (the web service methods and operators), then <sup>j</sup>(S, T, D), is the set of all plans for T from S in D: It is defined recursively as follows:

If T is empty, then <sup>j</sup>(S, T, D) contains exactly one plan, namely the empty plan. Otherwise let t be the first task atom in T and R be remaining task atoms. There are three cases: (1) If t is primitive and there is a simple plan p for t, then $\Pi ( S , T , D ) { = } \{ a p p e n d ( p , q ) \colon$ $q { \in } \Pi ( p ( S ) , R , D ) \}$ . (2) If t is primitive and there is no simple plan for t, then <sup>j</sup>(S, T, D)=h. (3) If t is compound, then <sup>j</sup>(S, T, D)=<sub>v</sub>(<sup>j</sup>(S, append(r, R), D): r is a simple reduction of t. Given the set of methods and operators for a domain, the SHOP algorithm for computing <sup>j</sup>(S, T, D) (all plans) (based on the above definitions) is as follows:

(1) PROCEDURE find-plan (S, T, D)

(2) return seek-plan (S, T, D, nil)

(3) end find-plan

(1) PROCEDURE seek-plan (S, T, D, p)

(2) if T=nil, then return the list( p).

(3) Let t be the first task in $T ;$ R be the remaining tasks in T.

(4) if t is primitive, then

! <sub>if there is a simple plan q for t, then</sub>

! <sub>return</sub> <sub>seek-plan</sub> <sub>(</sub> <sub>q(S),</sub> <sub>R,</sub> <sub>D,</sub> <sub>append(</sub> <sub>p,</sub> <sub>q))</sub>

! <sub>else</sub> <sub>return FAIL</sub>

(5) else for every simple reduction r for t in S, ! <sub>ans=seek-plan(S, append(r, R), D, p)</sub>

! <sub>if anspFAIL, then</sub> <sub>return ans</sub>

! <sub>end for</sub>

! <sub>return</sub> <sub>FAIL</sub>

(6) end if

(7) end seek-plan

The SHOP algorithm is shown to be complete and sound in Ref. [44]. State spaces for planning problems can be finite or infinite depending on the underlying domain description. The SHOP algorithm is recursive in nature and termination criteria include stopping after finding a single plan, exhaustively exploring the search space to find all plans and then find an optimal plan. Each such criteria would incur different search costs. The nature of the search costs is discussed further in Section 5. For our purposes, we treat the SHOP planner as a black box and focus on its use for web services composition. Given descriptions of web service operators, the generic planner computes multiple service plans for a given service request (in a given web services domain).

## 4.1.2. Developing concurrent service plans

The output of the SHOP algorithm is a sequential totally ordered plan. We further postprocess this plan to generate a plan with concurrent actions based on a greedy variant of the Minimal Deordering algorithm (from Ref. [7]) called PlanParallelize. The algorithm is as follows:

(1) PROCEDURE PlanParallelize

(2) Input: A valid totally order plan $P { = } \langle A , \ { \prec } \rangle$ 4 wherein $A { = } \langle a _ { 1 } , a _ { 2 } , . . . a _ { z } \rangle$ is an action sequence,  is the set of precedence constraints between these actions, the initial state, sinit.

(3) Output: A deordering of $P , A _ { \mathrm { c } }$ consists of sets of actions,

$\left( \left( a _ { 2 } , . . . , a _ { n } \right) , \quad \left( a _ { n + 1 } , \quad a _ { n + 2 } , . . . , a _ { m } \right) , . . . , a _ { n } \right)$ $( a _ { m } , . . . , a _ { z } ) ) . \ A _ { \mathrm { c } }$ is the set of partially ordered actions.

(4) Initialize variables, $s _ { \mathrm { c u r r } } { = } s _ { \mathrm { i n i t } } ; ~ \mathcal { A } _ { c } = N U L L .$

(5) If $\scriptstyle \mathrm { A = N U L L , \ s t o p }$

(6) Else, for $a \in A ,$ , if a is applicable to $s _ { \mathrm { c u r r } }$ without violating constraints in , collect a into templist. Apply actions a in templist to $s _ { \mathrm { c u r r } }$ to update $s _ { \mathrm { c u r r } }$ Append templist to $A _ { \mathrm { c } } .$ . Update $A $ $\left( { \cal A } - t e m p l i s t \right)$ . Goto Step 5.

(7) Finally return $A _ { \mathrm { c } } .$

Given a sequential plan, and the current state, the above algorithm selects all the applicable actions to the current state, while checking that no two actions conflict in the current state, based on the precedence constraints. It updates the current state with the set of applicable actions to generate a successor state and repeats the process on the remaining set of actions (that were not applicable in the previous state). The algorithm terminates when there are no more actions to parallelize. This two stage approach enables generation of both sequential and concurrent plans, which may be executed appropriately. We illustrate this approach in the ensuing section.

4.2. Modeling service composition in the HTN approach

In general, the following steps need to be followed to use a domain-independent planner to solve a nontrivial problem:

! <sub>Developing</sub> <sub>a</sub> <sub>domain</sub> <sub>ontology</sub> <sub>based</sub> <sub>on</sub> <sub>first</sub> <sub>order</sub> logic.

! <sub>Identifying</sub> <sub>and</sub> <sub>representing</sub> <sub>relevant</sub> <sub>operators</sub> <sub>(or</sub> tasks in a domain).

! <sub>Identifying</sub> <sub>and</sub> <sub>representing</sub> <sub>the</sub> <sub>state</sub> <sub>description</sub> <sub>in</sub> terms of the domain ontology.

! <sub>Defining</sub> <sub>initial</sub> <sub>states</sub> <sub>and</sub> <sub>goals</sub> <sub>for</sub> <sub>different</sub> <sub>types</sub> of problems in the domain.

A planning-based approach to problem solving supports generality in the following steps: (1) The same planning algorithm may be used in multiple problem domains, for example, online shopping, engineering design, procurement, etc. (as discussed in Section 6). This would require the definition of domain ontologies for each appropriate domain. The generality is supported by the use of first-order logic for reasoning. However, the ontologies differ in the operators and predicate terms used to describe the domain. (2) Once a domain is defined, different types of problems may be posed in the domain by choice of appropriate state predicates defining the initial and final states, and (3) for each type of problem, multiple ground instances may be defined.

We use a concrete scenario from the online shopping domain to illustrate declarative service composition. Additional scenarios are illustrated in Section 5. The approach is illustrated in the context of shopping for a set of items (possibly with interrelationship constraints) given a budget. Ontology development and resolving semantic heterogeneity is a key issue in using web services [24]. The essential shopping ontology is discussed as needed to illustrate the approach.

We use HTN planning to generate a service plan to fulfill shopping requests. Consider three web services $S _ { 1 } , S _ { 2 }$ and $S _ { 4 } ,$ each selling a set of different items i with each item i having a set of features j. These online services provide the following capabilities: (a) getting information regarding items and their features from product catalogs, (b) getting information regarding item availability (in terms of inventory levels), (c) getting prices of an item i, (d) placing orders, and (e) making payments. Additionally we also model a credit card verification web service, $S _ { 3 } ,$ , which provides the ability to check credit cards. Table 2 lists the service operators in terms of their input and output bindings for service $S _ { 1 } .$ . Operators $s _ { 1 - 4 }$ are transactional operators for logging on and logging off the web service, placing the order and making a payment. Operator $s _ { 1 5 }$ is an information gathering operator to query the web service for item availability and $s _ { 1 6 }$ is an operator for obtaining item prices. Similar operators are defined for services $S _ { 2 }$ and $S _ { 4 }$ . Service $S _ { 3 }$ has an operator to check for card status.

Shown in Fig. 5 is the set of items and features available at each service (Note service $S _ { i }$ is denoted as WSi in our encoding). For purposes of illustration, we assume that these are available as part of the description of each web service maintained by the service platform. For each item, information on its features, prices and current availability (shown by the label quant) is available. This information is obtained during execution by operators $s _ { 1 5 }$ and $s _ { 1 6 }$ and the catalog at the service platform updated.

A shopping service request, SR=(Itemlist,b), (defining one type of problem in the shopping domain), to the platform consists of a list of items $( I t e m l i s t { = } ( i _ { 1 } , i _ { 2 } , . ~ . ~ . ) )$ , the feature values for each item i, the quantity q of each item i, and a budget, b, for the purchase. This is provided (an example of shopping for three items) as follows:

Table 2  
Service operators for web service $S _ { 1 }$

<table><tr><td>Wrapper Id</td><td>Input view</td><td>Output view</td></tr><tr><td> $s_{11}$ </td><td>(CUSTOMER ID PASSWORD)</td><td>(LOGSTATUS)</td></tr><tr><td> $s_{12}$ </td><td>(CUSTOMER ID)</td><td>(LOGSTATUS)</td></tr><tr><td> $s_{13}$ </td><td>(ORDERLIST QUANTITY)</td><td>(ORDERID)</td></tr><tr><td> $s_{14}$ </td><td>(ORDERID PAYMENT)</td><td>(PAYMENT STATUS)</td></tr><tr><td> $s_{15}$ </td><td>(ITEM FEATURELIST QUANTITY)</td><td>(AVAILABILITY STATUS QUANTITY)</td></tr><tr><td> $s_{16}$ </td><td>(ITEM FEATURELIST)</td><td>(PRICE)</td></tr></table>

```lisp
((shoplist (
    ((item DVD-player) ((brand
SONY) (weight 100))
    (quant 2))
    ((item MusicCD) ((artist Prince)
    (title "hullo"))
    (quant 12))
    ((item VideoDVD) ((language English) (title "Blue Sky"))
    (quant 12))))
    (budget 3000))
```

In our implementation, such service requests are obtained via a form-based web interface and the corresponding list representation developed from the same. The declarative representations for a variety of service requests for a given domain can be generated from an appropriately designed user interface. The approach is similar to current techniques used to search databases from web-based interfaces wherein user interface elements correspond to logic constructs for a SQL query.

## 4.3. Service composition: overview

The above service request defines an instance of an online shopping problem and implicitly defines the state space show in Fig. 6 based on the web services in Fig. 5.

The state space is shown with eight numbered states (including the initial and final states). Each state shows the key goal terms, denoted GOAL, with the quantity of items required in the final bundle. CURR denotes the items procured thus far, in the current state. Thus in the initial state no items have been procured yet. State 2 shows that on accessing WS1, 2 units of DVD-player have been bought. Note that, the domain logic of the operator procures all the units of an item currently available in the inventory of a web service. The current availability of an item is a precondition (that is evaluated in a given state by calling the information-gathering operator of the web service) before an appropriate method can be applied to that state. For clarity, each arc between two states labelled Access WS, abstracts the five operators to log on, place an order, check a credit card (accessing another web service), pay for the order on approval and then log off. This is illustrated in the figure by the abstraction hierarchy. Note that Access WS is modelled as the select\_operator method in Fig. 9 in the paper. Also note, Fig. 6 does not illustrate the budget or current costs in each state (for clarity). These are also updated appropriately during the search process.

```lisp
;;CATALOG DESCRIPTION FOR ITEMS SOLD AT EACH WEBSERVICE
(defvar *WS1-Catalog* '
((item DVD-player)
((brand SONY)(weight 100)) (quant 3) (price-per-unit 250))
((item CD-player)
((brand SAMSUNG) (age 10)) (quant 4) (price-per-unit 150))
((item AnalogCamera) ((brand CANON) (age 10)) (quant 10)
(price-per-unit 70))
((item Binoculars) ((brand ZEISS) (age 10)) (quant 10) (price-per-unit 200))
((item Camcorder) ((brand HITACHI) (age 10)) (quant 10) (price-per-unit 300))
((item DigitalCamera) ((brand SONY) (age 10)) (quant 10) (price-per-unit 450))
((item MP3Player) ((brand SAMSUNG) (age 10)) (quant 10) (price-per-unit 295))
((item TV) ((brand MAGNAVOX) (age 10)) (quant 10) (price-per-unit 700)))
(defvar *WS2-Catalog* '
((item TextBook) ((author Eddington)(title "New Physics"))
(quant 3) (price-per-unit 45))
((item Magazine) ((name GQ) (date 10/02)) (quant 4)
(price-per-unit 5))
((item MusicCD) ((artist Prince)(title "hullo"))
(quant 10) (price-per-unit 20))
((item VideoDVD)((language English)
(title "Blue Sky")) (quant 10) (price-per-unit 10))
((item CasetteTape) ((title "ABBA Returns"))
(quant 10) (price-per-unit 5))
((item BoardGame) ((title "Monopoly"))
(quant 10) (price-per-unit 15))
((item Roses) ((type Flower)) (quant 25) (price-per-unit 35))
((item Lily) ((type Flower)) (quant 10) (price-per-unit 15))
(Manufacturer Hasbro)) (quant 10) (price-per-unit 65))
((item FictionBook) ((author Robbins)(title Carpetbaggers))
(quant 10) (price-per-unit 17))
((item FictionBook) ((author Keillor)(title "PHC")) (quant 10)
(price-per-unit 35)))
(defvar *WS4-Catalog* '(((item TextBook)
((author Eddington)(title "New Physics"))
(quant 3) (price-per-unit 35))
((item MusicCD) ((artist Prince)(title "hullo"))
(quant 4) (price-per-unit 14))
((item TV) ((brand MAGNAVOX) (age 10))
((brand MAGNAVOX) (age 10)) (quant 10) (price-per-unit 225))
((item CD-player) ((brand SAMSUNG) (age 10))
(quant 10) (price-per-unit 175))
((item VideoDVD)((language English)
(title "Blue Sky")) (quant 10) (price-per-unit 165))
((item Roses) ((type Flower)) (quant 5) (price-per-unit 10))
((item Lily) ((type Flower)) (quant 25) (price-per-unit 5)))
```  
Fig. 5. Catalog at each web service.

The SHOP algorithm explores the above described state space to find a path from the initial problem state to the final state. The SHOP planning algorithm starts from the initial state, generates the successor states (based on the applicable methods and operators in the current state), chooses a valid successor state nondeterministically and recursively executes the algorithm. For example, the three successor states to the initial state in Fig. 6 are generated by applying the select\_operator method, followed by its primitive operators (based upon its reduction). Termination criteria for the search include stopping when a path is found (a single plan), exhaustive breadth-first search of the state space to find all paths (hence all plans) and also for possibly for an optimal plan. Different search criteria would incur different search costs (in terms of computation time).

![](/api/attachments/JAC8YN2B/fulltext/images/48222c621268b73618ee291e2b902e736a476e157b7888a91948f3da3fbad3b1.jpg)  
Fig. 6. State space for example shopping request.

As shown in Fig. 6, there may be multiple paths in the state space that allow transformation of the initial state into the final state. The example state space illustrates six viable paths from the initial state to the final state. Though the same web services may be accessed, different quantities of items are ordered. For example, an order at WS2 between states 1 and 3 consists of 10 units of MusicCD and VideoDVD, whereas an order at WS2 between states 4 and 7 consists of 8 units of MusicCD and 2 units of VideoDVD. The order quantities differ based on what has been ordered previously and what remains to be bought. The size of this state space is determined by the number of available web services, the number of items and their quantities, the budgets and prices of the items. In the following section, we describe the details of the service planning process including the domain and state space descriptions.

## 4.4. Service composition: details of the approach

The service request, SR, is converted into an initial state definition shown in Fig. 7 for state 1 in Fig. 6. A state during the planning process is defined as collections of views along with predicates defining inputs to and outputs from web service operators and the current intermediary state. In Fig. 7, the service request is converted into the predicate (GOAL(- SHOPLIST. . .)) in the initial state. The current empty shopping cart is denoted by (CURRENTSHOPLIST ()). The status of each web service is defined by the predicate (SERVICE ?x ?service-features), where for each service, its type and status are maintained. In the future, we plan to extend these

![](/api/attachments/JAC8YN2B/fulltext/images/05673f864824c623dbb6435a1b376022792f87ad0c40275f9f1c23cd0621ab59.jpg)  
Fig. 7. Initial state definition.

descriptions based on the DAML-S initiative [23] as discussed in Section 6. Also the current budget is used to initiate a predicate (REM\_BUDGET ?z) which maintains the amount available for further purchases. The predicate (ORDERS ()) maintains the list of placed orders at each web service. The task of planning for service composition is to select a sequence of service operators that will transform the empty current shopping cart into one containing all the items requested within the budget amount. We do not capture item availability, prices or their inventory in the initial state as these may have to be obtained from the web services during service planning via information gathering operators. As planning is performed, this initial state is transformed by application of service operators.

Fig. 8 shows an intermediary search state from a test run for the above example. The state illustrates that two orders (denoted by predicate ORDER) have been placed at web services WS1 and WS2 and all the goal items have been obtained. However, note that quantities of two items MusicCD and VideoDVD is 10 and two additional units of each need to be procured before reaching the goal state. The service related predicates from the initial state are not changed through the planning process and carried along in every state description since they are always true in every intermediary state. However, after execution, the state description may be updated based on the availability of the service. Depending on the domains of interest, this state description may need to be modified accordingly.

![](/api/attachments/JAC8YN2B/fulltext/images/c1b0b266e8a2d4aafcea80a2db5f7eccf516716eb8529ccf5839f0f7a983fa54.jpg)  
Fig. 8. Intermediary state definition.

Shown in Fig. 9 are examples of an HTN method and an HTN operator in the service planning domain for deciding when operator $s _ { 1 3 }$ for placing an order is applicable given the current state of the overall execution. In the SHOP framework, methods allow evaluation of the current state and choice of which operators or decomposition methods that may be executed in the current state. Operators update the state by changing the predicates that describe the state.

The select<sup>\_</sup>ws<sup>\_</sup>operator obtains remaining items from the shopping list and checks a variety of preconditions that need to be satisfied. It validates if the service is a catalog web service and is available. Then it identifies all items from the remaining list that can be order at the web service. During planning, the predicate check<sup>\_</sup>avail<sup>\_</sup>items triggers an information gathering operator $( s _ { 1 5 }$ in Table 2) to the web service and the latest item availability is obtained. The predicate estimate<sup>\_</sup>item<sup>\_</sup>prices obtains the payment (again by accessing the price via information gathering operator $\left( { { s _ { 1 6 } } } \right)$ at the web service) that would be necessary if all the items are obtained. We have implemented a greedy policy to obtain all the items that are available at a given web service. Based on the price, the predicate check\_criteria checks if the budget is available and approval is issued. Once approval is obtained, it implies that the customer can log on to the web service, place the order and make the payment for the order. The planpmt methods in the post conditions invokes an operator to the credit card checking service. Similar methods and operators are defined for the other web services. In our current framework, the planner is optimistic in the sense that it assumes ideal conditions for success of each task, for example, credit approval. If credit is not approved and fails during execution, a new state predicate is introduced by the execution mechanism and an operator to obtain the essential information from the customer is introduced during the re-planning phase.

```lisp
;;METHOD CHECKS IF A WEBSITE CAN PROVIDE ANY ITEMS,
;;IF SO OPERATORS ARE EXECUTED ON THE CURRENT STATE
(:method (select_ws_operator)
(
;;Preconditions
(currshoplist ?y)
(goal (shoplist ?g))
(assign ?r_items_list (find_remaining_items`?y `?g))
(orders ?o)
(service ?ws ?wsfeats)
(valid-WS1 ?ws)
(valid-catalog-service ?ws ?wsfeats)
(valid-service-available ?ws ?wsfeats)
(assign ?currorder (check_avail_items`?ws `?r_items_list `?o))
(assign ?currpmt (estimate_item_prices`?ws `?currorder))
( goal (budget ?b))
(rem_budget ?b1)
(assign ?approval (check_criteria `?currorder `?b1 `?currpmt))
(customer ?c ?custinfo)
(valid-currorder ?currorder)
(valid-approval ?approval)
(assign ?newcurrlist (update_currlist `?y `?currorder))
(assign ?newbudget (update_budget `?b1 `?currpmt))
)

;;After Effects of the Method
(:ordered
(!WS1_logon ?c ?custinfo ?approval )
(!WS1_placeorder ?currorder ?newcurrlist)
(planpmt ?ws ?currpmt ?custinfo ?newbudget ?newcurrlist ?currorder)
(!WS1_logoff ?custinfo))
);

;;A Logon operator
(:operator (!WS1_logon ?c ?custinfo ?approval)
((customer ?c ?y)) (())
((customer ?c WS1 logged))
);

;;A Logoff operator
(:operator (!WS1_logoff ?custinfo)
((customer ?x WS1 logged))
((customer ?x WS1 logged)) ()
);

;;A placeholder operator
(:operator (!WS1_placeorder ?currorder ?newcurrlist)
((customer ?x WS1 logged)) ()
((customer ?x WS1 order_placed))
)
```  
Fig. 9. A web service method and operator.

Each HTN method for the web services domain model embeds heuristics which guide the plan search towards reaching the goal state. These heuristics try to choose only operators that can buy items in the shopping list. All relevant web service operators in a given search state will be explored and promising paths followed. Thus service selection is inherently embedded in the planning processes. Planning terminates when the current shopping list is equal to the goal list. As indicated earlier, on complete search of the state space, alternative plans will be generated, if there are multiple paths in the state space that reach the same goal state from an initial state. Exhaustive search for the shopping example generates six alternative plans, differing in the items and quantities procured at each web service as suggested in Fig. 6.

Two of the six alternative sequential plans (at the service operator level), generated by SHOP, are shown in Fig. 10. The figure shows only the signatures of the operators (input and output bindings are not shown). The two plans differ in the items, quantity ordered and the total price to be paid. The plans differ in the access sequence of these web services. In the first plan on the left, web service $S _ { 4 }$ is accessed first (plan Steps 1–5) followed by $S _ { 2 }$ (Steps 6–10) and $S _ { 1 }$ (Steps 11–15). In the plan on the right, a different order of web services is accessed. The two alternatives in Fig. 10 differ in (a) which web services are accessed, (b) what order, and (c) the quantities ordered at each web service (as illustrated in the state space of Fig. 6). For example, 12 MusicCDs are ordered in the shopping request. These MusicCDs are bought in batches of 4 and 8 in the first alternative. In the second plan alternative, these are bought in batches of 10 and 2. The batch size bought is dictated by the available inventory at each web service at the time the order is placed. We note that different quantities of items may be ordered at different web sites based on remaining budget, availability, features and current prices leading to different plans. The choice of available web services, the items available at each service, the available quantities of each item and the prices of each item define a combinatorial state space. Different shopping strategies can be used to guide search and select feasible solutions in this space.

The sequential plans in Fig. 10 are also parallelized based on the algorithm outlined in Section 4.1. The concurrent version of the first plan alternative is shown in Fig. 11. Note that web services are accessed in parallel in this version with the same set of items being ordered as in sequential solution above. The numbers denote the stages of partial ordering.

![](/api/attachments/JAC8YN2B/fulltext/images/dc61741265defc13d1146872f8d5bbba8c3654dd9cd070c845718b1109a0a92f.jpg)  
Fig. 10. Two alternative sequential service plans.

In our encoding of the shopping domain, the strategy is to procure all requested items within the budget amount or else fail. This is checked by the predicate, check<sup>\_</sup>criteria in Fig. 9 which compares the current remaining budget with the cost of a new order to be placed in the current state. Alternatively, if the budget is an unconstrained resource, and the overall shopping strategy is to procure whatever items are available from the shopping list within the budget, this may also be codified in the declarative planning logic. Another approach is to query a price comparison web service, select the cheapest web service and develop a plan accordingly. Different strategies for shopping may be encoded in the domain methods and operators. Specific choices such as price limits on an item, brands on items and user tastes may be modelled as preconditions on the domain methods and used for filtering items from a web service catalog. We observe that our description of items is general in nature, described by a list of features. We have restricted our choice of item features to prices, quantities and brands to manage the search space and also represent what is currently available in real-world web services. Design of effective shopping strategies may be extremely complex as discussed in Ref. [42]. We observe that any relevant optimization based decision-making strategy may be encoded as precondition for a service operator. Instead of domain level strategies, plans may be selected based on the cost models discussed in Section 3. Since our current focus is on providing reliable, responsive access, we select a plan based on estimated response times. The cheapest plan may be the slowest to execute.

The planning based approach is general in nature. In the shopping scenario, as the complexity of a shopping request increases in (a) the number of items, and (b) the constraints on the features, it is difficult to manually generate all valid item bundles in an efficient manner. A manual approach to generating multiple plan alternatives, as search space complexity grows, is not scalable. The ISP&E approach may be deployed in different domains by encoding the web service capabilities and the appropriate domain knowledge in terms of relevant methods and operators. Further, during re-planning in the ISP&E framework, the new plan may be completely different from the initial one. To illustrate the generality of our approach, we develop shopping service plans for the introductory example. A shopping request for gift package consisting of a book, CD and flowers (within a budget of \$70) is provided as follows:

```lisp
((shoplist (
    ((item Fictionbook)((author Keillor)(title "PHC"))(quant 1))
    ((item MusicCD)((artist Prince)(title "hullo"))(quant 1))
    ((item Lily)((type Flower))
    (quant 2))))
    (budget 70))))
```

The shopping plans for the request, based on the catalog descriptions in Fig. 5 are shown in Fig. 12. In the first plan, all items may be bought at one web service (at WS2, for a total cost of \$67) whereas in the second plan, items are procured at two services (at WS4 and WS2, for a total cost of \$41 (24+17)). Applicability of the ISP&E framework to other domains is discussed in Section 6.

In the context of service planning, it is important to find a feasible plan first and then only optimize. In our framework, each set of five steps in the plans of Fig. 10 such as logging on (WS<sup>\_</sup>LOGON), placing an order (WS4<sup>\_</sup>PLACEORDER), checking credit (WS3<sup>\_</sup>CHECKCARD), making a payment (WS4<sup>\_</sup>PAY) and logging off (WS4<sup>\_</sup>LOGOFF) is treated as a transaction. Failure in any of the five steps is equivalent to failure of the complete set. Each plan in the figure is converted into a sequence of WSDL method calls for appropriately defined web services based on the procedural definition maintained at the service platform. This is then executed by the platform.

```txt
1: !WS4_LOGON C1 !WS2_LOGON C1 !WS1_LOGON C1
2: (!WS4_PLACEORDER !WS3_CHECKCARD) (!WS2_PLACEORDER !WS3_CHECKCARD)
(!WS1_PLACEORDER !WS3_CHECKCARD)
3: !WS4_PAY 1706 !WS2_PAY 180 !WS1_PAY 500
4: !WS4_LOGOFF !WS2_LOGOFF !WS1_LOGOFF
```  
Fig. 11. Concurrent version for PLAN 1.

![](/api/attachments/JAC8YN2B/fulltext/images/f875a8db6b865a4cbe880ebca597e34f70f5e4d5909ac574741cd6bdd99e9830.jpg)  
Fig. 12. Two alternative service plans for introductory example.

## 4.5. Interleaving service planning and plan execution

Interleaving planning with execution has attracted considerable attention in the context of building complex and robust autonomous control systems for a wide variety of applications [62,3,45,31]. Strategies for reacting to execution failures range from replanning, reactive planning or plain re-execution. Replanning on failure involves developing a new plan considering the latest world information and then executing the newly generated plan. Reactive planning on failure involves modifying the current plan according to rules that define how the plan should be tweaked for each possible kind of failure. Re-execution strategies attempt to re-execute the initial plan with the belief that the root causes of plan failure are random and the world will return to a state that is consistent with the assumptions of the plan. Thus if the world returns to a consistent state with respect to initial assumptions, the initial plan will succeed. Each of these strategies assumes different kinds of knowledge about changes to the world from the time the plan was conceived [54]. However, to the best of our knowledge, the relevance of these techniques has not been explored in the context of web services composition and execution.

In order to assimilate changes in customer requests, web services and network characteristics and react to failures during service plan execution, we have integrated the service planning and execution phases. In our framework, we have integrated them in a cycle as shown in Fig. 4, where control is transferred alternatively between planning and execution. The service plan generated by the planning module is executed by the plan execution module. The operators are executed in sequence. During execution, operators can time out due to network or source dynamics or plan execution can be interrupted to accommodate new customer requests. When failures or interruptions occur during execution, two options are available on resumption—(a) re-execute the remaining steps of the plan from current state or (b) re-plan to find a new alternative plan and then execute. The choice between these two options is usually not clear and depends on the environmental conditions. Developing optimal strategies for such different scenarios is a long-term research goal. The issues are further discussed in Section 5. When execution failures occur, the execution module updates the current state and chooses one of the above options as shown in Fig. 3. The cycle is repeated until a preset time limit expires or a successful answer to the service request is obtained.

## 5. Evaluation of IS P&E

Based on our proposed approach, we have implemented the IS P&E system as a proof-of-concept prototype. The focus of our implementation has been on developing the planning and execution modules of the service platform. The architecture of the implemented system is shown in Fig. 13. The service platform consists of three main components, the planning module, the execution module and a world monitor that is monitoring the web services for dynamic information.

![](/api/attachments/JAC8YN2B/fulltext/images/342dc482c02ff0d8d0eefa56a46af2cae8a9838e36d78a9bae6c2c9deee87784.jpg)  
Fig. 13. IS P&E architecture.

For the planning module, we have utilized the SHOP system implemented in Common Lisp and run as a LISP servlet. Further, the execution module is also implemented as a JAVA-based servlet and coordinates with the planning module. The generic steps are indicated by the numbers on arrows. The service request is issued in a browser and sent to the planning module (Step 1), a service plan is generated and sent to the execution engine (Step 2), during execution service operations and platform operations are executed at the execution module (Step 3) and finally a result is returned to the user (Step 4) or if failure occurs, re-planning is considered (Step 5). In our current implementation, description about web services in the world is managed at two sites in the ISP&E framework: (1) in the service catalog maintained at the service platform, and (2) in the world monitor maintained as part of the execution framework. The service catalog maintains the declarative description of the WSDL functions and their procedural mappings. The world monitor maintains the dynamic information and accesses statistics about each web service such as uptime since last failure, current availability and number of method calls. These two descriptions mimic UDDI to provide design-level and execution level support. The service platform catalog is initialized manually in our current testbed. In future work, we aim to enable dynamic ontology update based on the semantic web capabilities as suggested in [40]. The world monitor is a multithreaded JAVA object maintaining real-time proxies of all the relevant web services and runs concurrently with the other modules.

A simulation-based study to evaluate the validity of our overall approach and compare different reactive strategies is described in the ensuing section.

## 5.1. Experiments

We conducted a set of experiments to evaluate the advantages of interleaving planning for service composition and execution in providing reactive behavior over a static hardwired service composition approach. Strategies for interleaving planning and execution is an active area of research in different kinds of dynamic systems such as robotics, distributed and mobile systems [14,32]. The aim of the experiments were:

! <sub>to illustrate interleaving service planning and</sub> execution as a viable alternative approach (in constrast to hardwiring web service interactions in languages such as BPEL4WS) to web service composition. A hardwired approach may not be scalable as it may be infeasible to encode all possible conditional alternatives to cope with various kinds of exceptions in a reliable manner.

! <sub>to illustrate that the ISP&E approach assimilates</sub> new information (possibly available after failure such as service inavailability) to develop robust service plans and copes successfully with the dynamics during execution.

! <sub>to</sub> <sub>understand</sub> <sub>the</sub> <sub>nature</sub> <sub>of</sub> <sub>the</sub> <sub>trade-off</sub> <sub>between</sub> planning and execution times under different dynamic conditions in the ISP&E approach. Interleaving planning with execution may have an impact on the total response time due to the time required for planning between each cycle of planning and execution. This may guide the development of effective interleaving strategies in the near future.

The experiments are exploratory in nature to provide insights into the behavior of the interleaved approach and test the proof-of-concept. The focus in these set of experiments is not on evaluating the computational properties per se. The simulation studies were conducted as no testbeds for comparing web service composition techniques are currently available.

## 5.1.1. Experimental setup

Our experimental studies are intended to obtain basic insights on the following questions: (a) How does the interleaving strategy compare to current static approaches in coping with service dynamics? and (b) In different types of interleaving strategies under varied dynamic conditions, what is the trade-off between planning time and execution time and their impact on total response time? We utilize the online shopping domain for our study.

Three web services and their operators, as discussed in Section 4, were used in the simulation to model the underlying information environment. For each service operator, we simulated the result transmission time $( t _ { i j } )$ in milliseconds and processing time $c _ { i j }$ in seconds as obtained from an uniform distribution, over a time-period of 3600 seconds at every second interval. $t _ { i j }$ was generated from a uniform (10– 250) distribution, and $c _ { i j }$ from a uniform (1–25) distribution. Information gathering operators were executed to update the web services catalog at the service platform before the initiation of each planning cycle.

Three service requests of increasing complexity (in terms of the number of items requested and intermediary web service accesses) were executed under different dynamic conditions. These test requests ensure that the planner will develop service plans that require split quantities of items to be ordered from multiple web services. Further, the success of the planner in finding a solution is also bounded by the available budget. The service requests in terms of number of items are listed in Table 3 below along with the number of plan alternatives. As the complexity of the request increases, the number of alternative plans increases. These test service requests were further fulfilled for different interleaved planning and execution strategies under dynamic conditions.

To simulate network dynamics, operators could fail during their execution due to randomly generated events from a Bernoulli distribution denoted $B ( p )$ Two failure settings of $\scriptstyle p = 1 0 \%$ and 30%, along with no failure $p { = } 0$ were simulated. In the real world, these failures could be caused by various dynamic interrupts outlined in introductory section. Further, under each such setting, the service requests were executed with a total response time limit of 1000 seconds in three different strategies:

S-1 Generation of a plan followed by a single attempt at execution.

S-2 Generation of a plan, followed by multiple attempts at execution. If failures occur, the original plan is re-executed.

S-3 Generation of a plan, followed by multiple attempts at planning and execution. If failures occur, re-planning is performed followed by execution of the new plan.

For each strategy, we evaluated the totalresponse-time for a service request from the time it is issued to completion of execution. Further, we also measured the total planning time and total execution time. The total response time is obtained as the sum of the actual planning time and the simulated execution time for each operator in the plan. Setup times between operator executions are considered negligible. Re-planning considers the notion of transactions and the last correct state is used to initiate re-planning. For example, a failure in the payment operator implies failure of the transaction and re-planning creates new plans including logging on and reordering.

Table 3  
Experimental service requests

<table><tr><td>Request label</td><td>Number of items</td><td>Number of plans</td></tr><tr><td>SR1</td><td>3</td><td>6</td></tr><tr><td>SR2</td><td>5</td><td>6</td></tr><tr><td>SR3</td><td>7</td><td>3</td></tr></table>

## 5.1.2. Hypothesis and observations

In the ISP&E framework we expect to see the following nominal behaviors (denoted H-\*) of the system under different dynamic conditions: (H-1) The ISP&E approach (strategies S-2 and S-3) should be able to cope with the dynamics in the system, i.e., find a plan if it exists and execute the same successfully. (H-2) Re-planning (strategy S-3) will increase planning costs and thus possibly the response time. However, re-planning may also identify alternative shorter plans if the opportunity is available. (H-3) Rexecution strategies (strategy S-2) may succeed if the dynamics is benign. However, if a component web service fails, the strategy may fail completely whereas re-planning may exploit an alternative web service if it is available, and (H-4) The nature of the dynamics will affect the cost of planning and execution. Planning costs may increase with high dynamics (in strategy S-3) and tend to dominate the total response time. In general, planning costs may be expected to increase with increase in the service request size, i.e., the number of items, their features and the number of available web services.

The results of our experiments (wherein service requests were replicated five times for each possible setting), conducted on a dual-processor Pentium III 900 MHz system are shown in Table 4 below. Total denotes total time, Plan denotes time for planning, and Exec denotes time for execution. There are a total 27 treatments, for three strategies, under three failure rate conditions, for three test requests. SR1, SR2 and SR3 denote the three test service requests as listed in Table 3.

## 5.2. Analysis of results

Analysing the results in Table 4 illustrates the following: For a nil failrate, there is no significant difference between the different strategies. However, whenever failure occurs, the baseline strategy, S-1, leads to failed execution. Strategies S-2 and S-3 do cope with the dynamics supporting hypothesis H-1. Further as hypothesized (H-2 and H-3), strategy S-2 incurs increased execution times but planning time remains low. Strategy S-3 also succeeds under different failure conditions but is robust to cope with service outages. Alternative plans are generated considering current status and then executed. However, depending on the nature of the dynamics, extra planning costs are incurred in strategy S-3. Overall for all strategies, as service request size increases, total planning time increases as the number of operators in the plan increase. However, if a particular service is unavailable for long periods of time, a request may not be fulfilled till that service is available again.

Table 4  
Experimental results comparing execution strategies

<table><tr><td rowspan="2">Request:Strategy</td><td colspan="3">Failrate 0.0</td><td colspan="3">Failrate 0.1</td><td colspan="3">Failrate 0.3</td></tr><tr><td>Total</td><td>Plan</td><td>Exec</td><td>Total</td><td>Plan</td><td>Exec</td><td>Total</td><td>Plan</td><td>Exec</td></tr><tr><td>SR1:S-1</td><td>473.26</td><td>0.37</td><td>472.89</td><td>FAIL</td><td>0.45</td><td>*</td><td>FAIL</td><td>0.32</td><td>*</td></tr><tr><td>SR1:S-2</td><td>468.11</td><td>0.35</td><td>467.66</td><td>525.25</td><td>0.33</td><td>524.92</td><td>625.2</td><td>0.39</td><td>624.81</td></tr><tr><td>SR1:S-3</td><td>466.2</td><td>0.37</td><td>465.83</td><td>499.28</td><td>0.39</td><td>498.89</td><td>643.5</td><td>1.9</td><td>641.6</td></tr><tr><td>SR2:S-1</td><td>553.2</td><td>0.4</td><td>552.8</td><td>FAIL</td><td>0.38</td><td>*</td><td>FAIL</td><td>0.42</td><td>*</td></tr><tr><td>SR2:S-2</td><td>557.1</td><td>0.39</td><td>556.81</td><td>611.1</td><td>0.42</td><td>610.68</td><td>600.6</td><td>0.42</td><td>600.18</td></tr><tr><td>SR2:S-3</td><td>535.1</td><td>0.43</td><td>534.67</td><td>687.1</td><td>1.43</td><td>685.67</td><td>849.45</td><td>3.23</td><td>845.78</td></tr><tr><td>SR3:S-1</td><td>556.1</td><td>0.45</td><td>555.65</td><td>FAIL</td><td>0.47</td><td>*</td><td>FAIL</td><td>0.46</td><td>*</td></tr><tr><td>SR3:S-2</td><td>581.2</td><td>0.45</td><td>580.75</td><td>621.2</td><td>0.49</td><td>620.71</td><td>675.1</td><td>0.49</td><td>674.61</td></tr><tr><td>SR3:S-3</td><td>575.2</td><td>0.46</td><td>574.74</td><td>681.7</td><td>1.2</td><td>680.5</td><td>961.53</td><td>3.55</td><td>957.98</td></tr></table>

Comparison of strategies S-2 and S-3 illustrates that the plan generated during re-planning (S-3) from the current state may be considerably different from the original plan and may take advantage of a newly available web service. Consider the scenario where a new web service (say WS7) with all the items in the requisite quantities is available just after initiating execution of the first plan of Fig. 10. Consider that the plan fails in Step 2 because of failure of service WS4. Re-planning should generate a plan where all the items are ordered at the newly available web service, WS7, if they can be ordered within budget and better response times may be obtained. Just plain reexecution (strategy S-2) may not take advantage of such a scenario. We do observe this in our studies with the ISP&E architecture.

In summary, the results of the experiments support the occurrence of suggested system behaviors in Section 5.1.2. If the system volatility is high, the difference between strategies S-2 and S-3 is unclear under highly dynamic conditions (wherein even alternative web services are not stable for long periods of time). Both strategies seem to perform equally well and the benefit of re-planning in reducing overall response time is marginal. Without time limits on the service response, strategy S-3 is the best. The replanning cycle in strategy S-3 is triggered in our framework by network failures, service failures or new customer requirements.

Understanding the interrelationship between the nature of the dynamics and different interleaving strategies will enable development of better process management policies in the near future as organizations deploy flexible process delivery technologies. The current ISP&E setup includes a feedback loop, where the intermediate results of plan execution are fed back to the planning module. A number of alternative interleaving strategies (other than those experimented with) are possible such as: (a) based on the nature of the dynamics, decide to re-execute or replan thus switching between the two; (b) based on identifying stable patterns (via learning) in the dynamics of the environment, develop partial plans on subgoals and fulfill the service; (c) reduce planning time based on retrieving successful plans from a repository; (d) reduce planning time by locally <sup>b</sup>repairing<sup>Q</sup> a failed plan to bypass the encountered problem as opposed to re-generating a new plan based on the current execution state from scratch [62]; and (e) based on a trade-off/utility analysis between the information acquistion cost during monitoring versus the cost of re-planning, choose a strategy. Our current studies are investigating these various strategies in a large-scale testbed.

Improving the performance of the ISP&E architecture depends on improved planner performance. We are currently exploring the applicability of other domain-independent planners such as MBP [20] and UMOP [29], which are based on fast manipulation of binary decision diagrams to obtain the required performance. The strategy of interleaving planning and execution is viable when the dynamics of the environment are moderate. If the rate of changes is high, it may be cost-effective to plan and execute myopically. However, when the rate of change is moderate and is much slower than the total time it takes to update the service catalog at the service platform, the ISP&E strategy is effective and responsive as shown by our experiments.

## 6. Discussion

The development of the ISP&E approach was intended to explore the applicability of recent advances of AI planning and execution techniques, which have been successful in the robotics domain, in the context of web services. Planning techniques enable the development of effective courses of action for a problem by assimilating new information gained during execution in dynamic situations. In the context of web services, planning provides many advantages. Firstly, in a complex search space, developing a plan manually may be time-consuming and tedious. Further, if the requests are complex (such as increase in the number of items, type and number of constraints and multi-criteria objectives) finding even a feasible plan may be difficult. Secondly, re-planning provides the ability to react to dynamics of the environment. Trivial static plans may not exploit the new information in opportunistic manner. Though trivial partial plans may be developed on the fly in a myopic manner, such as ordering each item in turn, such an approach may be suboptimal and not satisfy all constraints. Thirdly, planning enables a flexible modeling and composition approach for a wide variety of web services by providing a declarative framework for operator definition and composition. The work presented in this paper is also motivated by the need to automate software design and development of web services [36].

The focus of our work has been on the mechanism of composition which we believe may be common for both B2B and B2C scenarios. However, these two types interactions may differ on the following dimensions: (a) the nature of the constraints on the service, (b) end-user interactivity with the service platform that needs to be supported, (c) running time of the composed services; B2B interactions may be long-running transactions whereas B2C interactions may require realtime responses, and (d) recovery and re-planning strategies in the two contexts may be very different. Further, B2B interactions involving negotiations (modelled by asynchronous message interactions called conversations) may require an additional level of dialogue and conversation planning between the platform and web service. The current framework is guided by the availability of RPC request–reply model of interaction. We are extending the framework to include asynchronous service interactions.

The planning-based composition approach is applicable to a variety of web services process management scenarios. Firstly, the ISP&E approach can cope with any type of inter-service method call topology that may exist between a service platform and the component services. For example, Fig. 1 is a hub and spoke topology. One important type of topology is the existence of recursive structure amongst web services. For example, a web service intermediary may provide product configuration services by accessing component web services that are independent assembly services, as shown in Fig. 14. Such independent assembly services may themselves access supplier web services to fulfill their needs. Such topologies may be modelled by having ISP&E based platforms at each intermediary as shown in the figure, wherein the intermediary publishes its services in WSDL. Each of the intermediary platforms may generate an appropriate service plan based on the request received from a requestor higher up in the topology. We have extended the ISP&E framework to the domain of engineering design to enable component sourcing (manuscript in progress). A related issue is the existence of recursive structure in information gathering queries posted to web services. For example, inferring that a particular item is a member of an assembly, based on the results of a catalog search for that item, requires recursive reasoning capabilities. For example, a song may be available as part of a CD album or as a single, which may be part of an anthology. In the current setup, the service platform is agnostic of such relationships and trusts the catalog service to provide all possible alternatives in which an item may be available. With the development of Semantic Web ontologies, such inferences may become routine in the near future, performed either at the service platform or at the web service.

![](/api/attachments/JAC8YN2B/fulltext/images/79a4f47411f606441220de3fb8dd56c46ee6e12a39c0afc2b1d7507e887e84d8.jpg)  
Fig. 14. A recursive web services topology.

We would like to note that our ISP&E approach to web services has been motivated by the observation of the frame problem in programmatic approaches to process management. The frame problem occurs in the context of modeling dynamic systems, where the issue is to represent all the things that stay the same in two consecutive states of the world. Actions between two states identify only what changes. Inferences regarding other state variables are highly domain-dependent. In the real world, almost everything stays the same, almost all the time. Programmatic process modeling approaches (such as compensations in workflow models) try to envision and then encode reactive strategies to all the possible combinations of changes in the world that the system may encounter. If such encoding is incomplete or reflects erroneous assumptions regarding how the world may evolve, the process management system may be brittle. The process state (for example, in workflow engines) is implicitly embedded in a distributed manner across the participant task providers and the workflow engine and cannot be explicitly reasoned with. In Ref. [55], the benefits of an explicit state representation for adaptive process management are outlined. Such a state representation is provided by a planning-based approach to process management. Further, the classical frame problem, including qualification and ramification problems have been resolved formally using situational calculus over the past decade [53]. The current generation of planning methodologies reflect this underlying resolution when a new state is generated in state-space search or plan-space search [54]. In summary, by interleaving planning and execution, we are able to utilize the latest knowledge about the world to react appropriately in contrast to programmatic approaches.

The plans generated in the ISP&E framework are linear in nature. Languages such as BPEL include operators for branching and iteration. In our framework, branching occurs as a behavioral side-effect of re-planning. Instead of encoding all alternatives programmatically, the re-planning approach chooses a branch based on the current state providing a similar behavior. Our current work is exploring the need for iterative web service method invocations in the context of service fulfillment. Conditional iterations such as loop-while or loop-until is captured by replanning. However, bounded iterations such as defined by for loops may need to be embedded as a method in the web service. Though planning in the general sense is a computationally expensive approach, our experience in the web services context suggests that for wellstructured domains it may be a feasible approach to enable service composition.

From a semantic perspective, we are extending our work to utilize recent advances in DAML. Recent research on converting WSDL definitions into simple processes in the DAML-S notation and converting DAML-S process specifications into plans will enable our approach to seamlessly integrate in the semantic web services framework [48,67]. Our current work is focused on conversion of the plans generated by the ISP&E approach into DAML-S notations and enable service composition across domains such as coordinating sourcing choices during engineering design (requiring an engineering ontology) with procurement processes (requiring a purchasing ontology).

As the complexity and availability of web services, supporting tasks in domains such as enterprise application integration[26] and scientific grid computing increase, planning services may become an integral part of the distributed systems framework [13]. We are evaluating the ISP&E framework in multiple domains, such as (a) enabling engineering design activities such as catalog-driven design of electromechanical systems, (b) enabling distributed simulation, wherein multiple simulation models are available as web services and a new simulation needs to be composed, (c) Enterprise application integration, wherein a single business process may require formulation of a composite service, to access information from multiple enterprise systems, which expose their data via web services, and (d) model management in aid of distributed decision support systems.

## 7. Concluding remarks

In this paper, we have presented an AI-planning based declarative service composition approach, called Integrated Service Planning and Execution (ISP&E) for building robust on-the-fly customized web services in dynamic environments. Additionally, we have illustrated the strategy of interleaving service planning with plan execution that helps achieve responsiveness and flexibility in an open, dynamic environment like the Internet. An implementation based on a domain-independent Hierarchical Task Network (HTN) planning framework is described. The ISP&E approach provides the ability to integrate information obtained during execution into the planning cycle facilitating coupling of service planning and execution. Simulation experiments have illustrated the feasibility of this approach to successfully return a response under various failure scenarios. However, the planning performance is a major bottleneck in processing complex service requests. The studies indicate that in dynamic environments the best approach is to initially find a plan (not necessarily the best) and execute the same till failure. If failure occurs, the cycle is repeated till the goal is reached or the cycle is aborted when a predefined time limit is reached. Determining appropriate control strategies based on stable environmental behavior characteristics is an issue requiring further study.

For future work, we plan to (a) improve the performance of the planning module, (b) extend our framework to handle a variety of service request constraints, enable concurrency of operators, allow asynchronous interactions and evaluate ISP&E in other domains, (c) perform detailed evaluation of the dynamic factors discussed in Section 1, (d) incorporate data mining/learning techniques to profile service characteristics and costs to aid planning, and (e) evaluate the scalability of our approach via application on real-world web services.

## Acknowledgements

We would like to thank all the anonymous reviewers for providing valuable comments. These have helped us improve the contents of the paper.

## References

[1] S. Adali, K.S. Candan, Y. Papakonstantinou, V.S. Subramanian, Query caching and optimization in distributed mediator systems, SIGMOD Conference on Management of Data, ACM Press, 1996, pp. 137– 148.

[2] Amazon Inc., Amazon webservices, http://www.amazon.com/ webservices, 2002.

[3] J. Ambros-Ingerson, S. Steel, Integrating planning, execution and monitoring, Proceedings of the Seventh National Conference on Artificial Intelligence (AAAI-88), St. Paul, MN, AAAI Press, CA, 1988, pp. 83– 88.

[4] D. Amyot, R.J.A. Buhr, T. Gray, L. Logrippo, Use case maps for the capture and validation of distributed systems requirements, Proceedings of RE’99, Fourth IEEE International Symposium on Requirements Engineering, IEEE Publications, CA, 1999 (June), pp. 44– 53.

[5] Anthony J. Bonner, Workflow, transactions, and datalog, Proceedings of the Eighteenth ACM SIGACT-SIGMOD-SIGART Symposium on Principles of Database Systems, May 31–June 2, 1999, Philadelphia, Pennsylvania, ACM Press, 1999, pp. 294– 305.

[6] Fahiem Bacchus, Michael Ady, Planning with resources and concurrency: a forward chaining approach, Proceedings of IJCAI, AAAI Press, CA, 2001, pp. 417– 424.

[7] Christer B<sup>7</sup>ckstr<sup>f</sup>m, Computational aspects of reordering plans, Journal of Artificial Intelligence Research 9 (1998) 99 – 137.

[8] B. Benatallah, Q.Z. Sheng, M. Dumas, The self-serv environment for web services composition, IEEE Computer (2003 Jan/Feb) 40–48.

[9] B. Benatallah, M. Dumas, Q.Z. Sheng, A.H.H. Ngu, Declarative composition and peer-to-peer provisioning of dynamic web services, Proceedings of the 18th International Conference on Data Engineering, 2002, pp. 297 – 308.

[10] M.B. Blake, Agent-oriented approaches to B2B interoperability, The Knowledge Engineering Review 16 (4) (2001) 383– 388.

[11] M.B. Blake, An agent-based cross-organizational workflow architecture in support of web services, 11th IEEE International Workshops on Enabling Technologies: Infrastructure for Collaborative Enterprises, IEEE Computer Society Press, 2002, pp. 176 – 181.

[12] M.B. Blake, M. Gini, Guest editorial: agent-based approaches to b2b electronic commerce, International Journal of Electronic Commerce 7 (1) (2002) 5 –6.

[13] J. Blythe, E. Deelman, Y. Gil, Planning for workflow construction and maintenance on the grid, Proceedings of ICAPS’03 Workshop on Planning for Web Services, Trento, Italy, June, 2003.

[14] Guido Boella, Rossana Damiano, Empirical evaluation of a replanning algorithm, Proceedings of ICAPS’03 Workshop on Plan Execution, Trento, Italy, June, 2003.

[15] R. Braumandl, M. Keidl, A. Kemper, D. Kossmann, S. Seltzsam, K. Stocker, ObjectGlobe: ubiquitous query processing on the internet, VLDB Journal 10 (1) (2001) 48 – 71.

[16] Mike Burner, The deliberate revolution, ACM Queue 1 (1) (2003 March) 28– 37.

[17] J. Cardoso, Quality of Service and Semantic Composition of Workflows. PhD thesis, University of Georgia, 2002.

[18] F. Casati, M. Shan, Dynamic and adaptive composition of Eservices, Information Systems 6 (3) (2001) 143 – 163.

[19] D. Chakraborty, F. Perich, A. Joshi, T. Finin, Y. Yesha, Middleware for mobile information access, Proceedings

of the 5th International Work-shop on Mobility in Databases and Distributed Systems (MDDS’2002), 2002, pp. 729–733.

[20] A. Cimatti, F. Giunchiglia, E. Giunchiglia, P. Traverso, Planning via model checking: a decision procedure for AR, ECP, 1997, pp. 130 – 142.

[21] F. Curbera, Y. Goland, J. Klein, et al., Business Process Execution Language, www.ibm.com/software/solutions/webservices/ pdf/BPEL.pdf, 2002.

[22] K. Currie, A. Tate, O-Plan, the open planning architecture, Artificial Intelligence 52 (1) (1991) 49 – 86.

[23] DAML Coalition, Darpa Agent Markup Language, http:// www.daml.org, 2001.

[24] A. Dogac, G. Laleci, Y. Kabak, I. Cingil, Exploiting web service semantics: taxonomies vs. ontologies, IEEE Data Engineering Bulletin (2002 December) 10 – 16.

[25] K. Erol, J. Hendler, D.S. Nau, HTN planning: complexity and expressivity, in: Proceedings of the Twelfth National Conference on Artificial Intelligence (AAAI-94), vol. 2, AAAI Press/MIT Press, Seattle, Washington, USA, 1994, pp. 1123–1128.

[26] D. Fensel, C. Bussler, The web service modeling framework, Electronic Commerce Research and Applications 1 (2) (2002) 113– 137.

[27] Hector Garcia-Molina, Jeffrey D. Ullman, Jennifer Widom, Database Systems: The Complete Book, Prentice-Hall, 2002.

[28] R. Ginis, K.M. Chandy, Service composition issues for distributed business processes, in: L. Zhang (Ed.), Proceedings of the International Conference on Web Services, CSREA Press, Las Vegas, Nevada, USA, 2003.

[29] R. Jensen, M. Veloso, OBDD-based deterministic planning using the UMOP planning framework, Proceedings of the AIPS-00 Workshop on Model-Theoretic Approaches to Planning, AAAI Press, CA, 2000, pp. 26 – 31.

[30] S. Kambhampati, Refinement planning as a unifying framework for plan synthesis, AI Magazine 18 (2) (1997) 67 – 95.

[31] S. Koenig, Minimax real-time heuristic search, Artificial Intelligence 129 (1–2) (2001) 165 – 197.

[32] Solange Lemai, Felix Ingrand, Interleaving temporal planning and execution: IxTeT-eXeC, Proceedings of ICAPS’03 Workshop on Plan Execution, Trento, Italy, June, 2003.

[33] A. Levy, Combining artificial intelligence and databases for data integration, AI Today, 1999, pp. 249– 268, number 1600 in LNCS.

[34] A. Levy, D.S. Weld, Intelligent internet systems, Artificial Intelligence 118 (1–2) (2000) 1 – 14.

[35] F. Leymann, D. Roller, M. Schmidt, Web services and business process management, IBM Systems Journal 41 (2) (2002) 198– 211.

[36] T.A. Linden, Representing software designs as partially developed plans, in: M.R. Lowry, R.D McCartney (Eds.), Automating Software Design, AAAI Press/The MIT Press, 1991, pp. 603–625.

[37] D. McDermott, Estimated-regression planning for interactions with web services, Proceedings of the AI Planning and Scheduling Conference, Toulose, France, 2002.

[38] S. McIlraith, T. Son, Adapting Golog for composition of semantic web services, Proceedings of 8th Intl. Conf. of Knowledge Representation and Reasoning, 2002.

[39] S. McIlraith, T.C. Son, H. Zeng, Semantic web services, IEEE Intelligent Systems. Special Issue on the Semantic Web 16 (2) (2001) 46 – 53.

[40] Fiona McNeill, Alan Bundy, Marco Schorlemmer, Dynamic ontology refinement, Proceedings of ICAPS’03 Workshop on Plan Execution, Trento, Italy, June, 2003.

[41] D. Mennie, B. Pagurek, A runtime composite service creation and deployment infrastructure and its applications in internet security, e-commerce, and software provisioning, Proceedings of the 25th Annual International Computer Software and Applications Conference (COMPSAC 2001), IEEE Computer Society, Chicago, Illinois, USA, 2001, pp. 371 – 376.

[42] A. Montgomery, R. Hosanagar, K. Krishnan, K. Clay, Designing a better shopbot. Heinz School of Public Policy, CMU, Pittsburgh, PA Working Paper, 2003.

[43] D.S. Nau, S.J.J. Smith, K. Erol, Control Strategies in HTN planning: theory versus practice, Proceedings of AAAI-98, AAAI Press, CA, 1998, pp. 1127–1133.

[44] D.S. Nau, Y. Cao, A. Lotem, H. Munoz-Avilla, SHOP: Simple Hierarchical Ordered Planner, Proceedings of IJCAI-99, AAAI Press, CA, 1999, pp. 968 – 973.

[45] I.R. Nourbakhsh, Interleaving Planning and Execution for Autonomous Robots, Kluwer, 1997.

[46] OASIS Consortium, Universal description, discovery and integration of web services, http://www.uddi.org, 2002.

[47] M. Paolucci, T. Kawmura, T. Payne, K. Sycara, Semantic matching of web services capabilities, Proceedings of First International Semantic Web Conf., 2002.

[48] M. Paolucci, N. Srinivasan, K. Sycara, T. Nishimura, Towards a semantic choreography of web services: from WSDL to DAML-S, in: L. Zhang (Ed.), Proceedings of the International Conference on Web Services, Las Vegas, NV, USA, 2003.

[49] M. Papazoglou, M. Aiello, M. Pistore, J. Yang, Xsrl: an xml web-services request language. Technical Report DIT-02-079, Informatica e Telecomunicazioni, University of Trento, 2002.

[50] G. Piccinelli, G. Di Vitantonio, L. Mokrushin, Dynamic service aggregation in electronic marketplaces, Computer Networks Journal 37 (2) (2001) 95 – 109.

[51] AI Planning, SHOP system, http://www.cs.umd.edu/projects/ shop/ (2003).

[52] Sudha Ram, Daniel Zeng, Vijay Khatri, Limin Zhang, Efficient and scalable query planning in distributed open environments, Proceedings of WITS, New Orleans, Lousiana, 2001.

[53] R. Reiter, Knowledge in Action: Logical Foundations for Specifying and Implementing Dynamical Systems, MIT Press, 2001.

[54] S. Russell, P. Norvig, Artificial Intelligence: A Modern Approach, second edition, Prentice-Hall, 2003.

[55] A. Sheth, W. van der Aalst, I. Arpinar, Processes driving the networked economy, IEEE Concurrency 7 (3) (1999) 18 – 31.

[56] B. Srivastava, J. Koehler, Web service composition—current solutions and open problems, Proceedings of ICAPS’03 Workshop on Planning for Web Services, Trento, Italy, June, 2003.

[57] G. Trajcevski, C. Baral, J. Lobo, Formalizing and reasoning about the requirements specifications of workflow systems, International Journal on Cooperative Information Systems 10 (4) (2001) 483 – 507.

[58] U.S. Census Bureau. North American Industry Classification System. http://www.naics.com (2002).

[59] United Nations Development Programme. United Nations Standard Products and Services Code. http://www.unspsc.com (2002).

[60] S. Vinoski, D. Lea, Middleware for web services, IEEE Internet Computing 7 (1) (2003 Jan–Feb) 28 – 29.

[61] W3 Consortium. WSDL standards. http://www.w3.org/TR/ wsdl (2001).

[62] G. Weiss, Multiagent Systems, MIT Press, 2000

[63] D.S. Weld, Recent advances in AI planning, AI Magazine (1999) 55–68.

[64] G. Wiederhold, et al., Composition of multi-site services, Proceedings of IDPT’2000, Dallas, TX, USA, 2000.

[65] D.E. Wilkins, M. desJardins, A call for knowledge-based planning, AI Magazine (2001) 99– 115.

[66] E. Winner, M. Veloso, Analyzing plans with conditional effects, Proceedings of the Sixth International Conference on AI Planning and Scheduling, April, 2002.

[67] D. Wu, E. Sirin, J. Hendler, D. Nau, B. Parsia, Automatic web services composition using SHOP2, Proceedings of ICAPS’03 Workshop on Planning for Web Services, Trento, Italy, 2003 June.

[68] Xmethods Inc. Web services. http://www.xmethods.com (2002).

[69] F. Yaman, D.S. Nau, Timeline: an HTN planner that can reason about time, Proceedings of AIPS’02 Workshop on Planning for Temporal Domains, 2002.

![](/api/attachments/JAC8YN2B/fulltext/images/1e9a5d04254fa5c1c6678b30f1fd2a031dbf2d6eb9030b85be37bbd81b2c4762.jpg)

Therani Madhusudan (Madhu) is an Assistant Professor at the MIS Department, University of Arizona. He holds Ph. D. (1998) and M. S. degrees (1994) from Carnegie-Mellon University and a B.Tech (1990) from the Indian Institute of Technology, Madras, India. Prior to joining the University of Arizona, he was a lead systems architect for Engineering Knowledge Man-

agement at Honeywell International, South Bend, IN. His research focuses on the development of knowledge-based tools to support the design and management of complex hardware and software systems. He has published over 20 refereed research articles in academic conferences and journals in the areas of Workflow Management, Information Integration, Product Lifecycle Management, and Engineering design automation.

![](/api/attachments/JAC8YN2B/fulltext/images/4c6f6536e2c79725cfc5796bd1a09a268ee5871c9fa656a500bd03897d7ffebe.jpg)

Naveen Uttamsingh is a Software Engineer in the applications group at Model N Inc., South San Francisco. He holds a Masters degree in Management Information Systems (2003) from the University of Arizona and a Bachelors degree in Civil Engineering (1999) from the University of Pune, India. Prior to joining Model N Inc., he worked as a Software Engineer for

Indsoft Pvt. Ltd., India where he was involved in developing a premier healthcare portal, MDIndia, which offers Third Party Administration Services for Insurance Companies, Policyholders and Healthcare Providers. His current contributions at Model N Inc., involve analysis, design and development of the Model N suite of applications that help life science companies automate critical business process such as contract management, pricing strategy and rebate management. Additionally, he has been involved, in coordination with the MIS department at the University of Arizona, in providing IT solutions to Tucson based companies such as Intuit and Ventana Medical Systems in the areas of database and data warehouse design.
