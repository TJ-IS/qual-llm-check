---
otero_id: 3276
otero_key: "FPZQHQ5A"
title: "How High Should We Go? Determining Reservation Values to Negotiate Successfully for Composite Software Services"
authors: "Sherry X. Sun; Jing Zhao; Sumit Sarkar"
year: "2017"
journal: "Information Systems Research"
doi: "10.1287/isre.2016.0678"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/FPZQHQ5A/fulltext/images/7cc4ee07fd9ba4e305ab3c56fdcf4651d3f995b092a5e3794b15e54108dec912.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## How High Should We Go? Determining Reservation Values to Negotiate Successfully for Composite Software Services

Sherry X. Sun, Jing Zhao, Sumit Sarkar

To cite this article:

Sherry X. Sun, Jing Zhao, Sumit Sarkar (2017) How High Should We Go? Determining Reservation Values to Negotiate Successfully for Composite Software Services. Information Systems Research

Published online in Articles in Advance 19 Apr 2017

http://dx.doi.org/10.1287/isre.2016.0678

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2017, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/FPZQHQ5A/fulltext/images/fe7f1b21742f97babdf44196dec88edd7c920a8cbb2554d83b95ecff2f7a5acb.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# How High Should We Go? Determining Reservation Values to Negotiate Successfully for Composite Software Services

Sherry X. Sun,<sup>a</sup> Jing Zhao,<sup>b</sup> Sumit Sarkar<sup>c</sup>

<sup>a</sup> Management Department, Albers School of Business and Economics, Seattle University, Seattle, Washington 98122; <sup>b</sup> City University of Hong Kong, Kowloon, Hong Kong SAR; <sup>c</sup> Naveen Jindal School of Management, University of Texas at Dallas, Richardson, Texas 75080 Contact: sxsun2015@gmail.com (SXS); zhaojingwhut@126.com (JZ); sumit@utdallas.edu (SS)

Received: April 30, 2012 Revised: February 18, 2013; April 23, 2014; October 25, 2014; April 30, 2015; May 16, 2016 Accepted: July 31, 2016 Published Online in Articles in Advance: April 19, 2017

https://doi.org/10.1287/isre.2016.0678

Copyright: © 2017 INFORMS

Abstract. In the paradigm of service-centric computing, new value-added applications can be developed dynamically and flexibly by combining and integrating existing services. While software applications are traditionally specified and implemented as a set of functions uniform to all users, this new paradigm allows the same software service to be delivered with a diferent price, response time, availability, and other nonfunctional attributes to accommodate diferent modes of use. These nonfunctional attributes together are referred to as Quality of Service (QoS). When creating a new composite service, negotiation makes it possible for a service provider to ofer the service with the QoS properties customized to the needs of a user. Automated negotiation tactics require the specification of reservation values for the QoS attributes. We present a methodology that determines the reservation values a user (or broker) should use for each component service based on the user’s minimum requirements for the composite service. Our methodology maximizes the chance of reaching a successful negotiation outcome while staying within the user’s reservation values for the composite service. We show that the problem of determining the user’s reservation values for component services can be modeled as a multiobjective optimization problem and then transformed to a single-objective optimization problem using a max-min approach. The formulation can incorporate providers’ diferent QoS preferences to increase the chance of negotiation success. We identify problem instances for which closed-form solutions can be found for the reservation values. We show how the method of setting reservation values can be incorporated into a negotiation process that uses extant concession and trade-of tactics. Simulation experiments demonstrate the efectiveness of the proposed approach. If some providers accept ofers before the negotiation process deadline, we show that dynamically changing the reservation values for the remaining providers makes the overall negotiation process more likely to succeed.

History: Ram Gopal, Senior Editor; Vĳay Khatri, Associate Editor. Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2016.0678.

Keywords: service composition • automated negotiation • Quality of Service • multiobjective optimization

## 1. Introduction

Service-centric computing and related technologies, such as Web services and service-oriented architecture, are emerging as a new and important paradigm for corporations to organize information technology (IT) resources and to enable business agility. Bardhan et al. (2010) identify service-orientation as one of the fastest growing paradigms in technology management, with important relevance for the information systems (IS) discipline. In such a paradigm, software components are packaged as independent, self-contained, and reusable services that can be delivered and consumed on demand (Zhao et al. 2007, 2008). New valueadded applications can be developed dynamically by combining and integrating the existing services to automate complex business processes and to address the rapidly changing needs of users. Tasks in a business process can be accomplished by invoking software services that ofer the required functions.

While software applications are traditionally specified and implemented as a set of functions uniform to all users, the service-centric paradigm is characterized as one where the same software service can be delivered to diferent users with diferent response time, availability, price,<sup>1</sup> and other nonfunctional attributes to accommodate diferent modes of use (Menasce 2002). These nonfunctional attributes together are referred to as Quality of Service (QoS) and are applicable to not only atomic software services but also composite services, i.e., services composed of other services. When creating a value-added service from existing services, the QoS of the resulting composite service has to meet certain constraints (e.g., response time, data quality, price, etc.) to satisfy the user.

Figure 1. A Composite Service for Personalized Multimedia Content Delivery  
![](/api/attachments/FPZQHQ5A/fulltext/images/c62ca7200c8f23f9d397f470f8fb243abce543650aeeade46975116d10c7f190.jpg)  
Notes. We use Unified Modeling Language (UML) activity diagrams to represent the composition structures because they are efective for graphically representing workflows (Sun et al. 2006) and they have been widely used in modeling service composition (Zeng et al. 2004, Ardagna and Pernici 2007). In keeping with standard notations for UML activity diagrams (Miles and Hamilton 2006), the black circles represent dummy starting and ending services for a workflow.

Figure 1 shows how a composite service that delivers multimedia content (e.g., news videos) to users could be composed of component services (Wagner and Kellerer 2004). The videos need to be transcoded to fit the target format. The videos include subtitles in foreign languages that have to be translated to the user’s native language. Thereafter, the subtitles have to be embedded into the video. Finally, the content has to be compressed into the appropriate format for transmission to the user’s device. Each step (component service) in the composite service is ofered by a diferent provider.

Diferent users of this composite service could have diferent requirements toward the quality of the video, such as the resolution, error rate, delay, and jitter. For example, a user desiring to view a video on a cell phone may be willing to compromise on the resolution of the image recognizing the implications on delay and price while another user may want the best quality resolution that is available if her target device is a highdefinition television. Based on the user’s requirements, the composite service could be tailored to the appropriate QoS specifications. To meet such QoS requirements for the composite service, each component service needs to deliver its functions at appropriate QoS levels. The promise of service-oriented computing is to provide services (atomic or composite) that are tailored to users’ unique requirements at the time users wish to utilize those services (Comuzzi and Pernici 2009). To redeem such a promise, it is important to let service users and providers explore what is possible at the time of a service request through negotiation (Elfatatry and Layzell 2004).

Users and providers often have conflicting interests, e.g., a user wants to pay as little as possible for a high-resolution video while a provider may only be willing to provide a low-resolution version for a low price. Negotiation can help resolve such conflicts and develop agreements acceptable to both parties. It is particularly useful when a feasible solution is not readily available on the service market. Through exchanging ofers and counterofers between service providers and users, it is possible to reach an agreement for a service with QoS tailored to the unique needs of a service user.

The importance of negotiation for software services has been well recognized (Elfatatry and Layzell 2004, Mbarek et al. 2008), with particular interest in the context of next generation networks (NGN). Such networks aim to bring autonomy in IT infrastructures by enabling software self-management (Mbarek et al. 2008). In NGN networks, negotiation allows selfmanaged software services to interact with each other without human intervention such that a global connectivity can be provided despite the use of heterogeneous technologies. For instance, this is particularly useful when a mobile user’s access network changes, with the guarantee of end-to-end QoS becoming increasingly critical for applications such as VoIP, VoD, and IPTV (Chalouf et al. 2012). Nevertheless, key challenges remain that prevent the full potential of negotiation from being realized in service composition. Importantly, it is not clear how the negotiation techniques developed in bilateral negotiations can be used to facilitate the search for contracts acceptable to the user and to all of the providers involved in service composition. In bilateral negotiations, it is reasonably assumed that an agent involved in a negotiation knows his own reservation value for the service under consideration, where the reservation value is the least value acceptable to the agent (Faratin et al. 1998). However, this assumption does not hold any more when negotiation is used in the context of service composition where a user may only know her minimum QoS requirements (i.e., reser vation values) for the composite service. The composite service consists of a set of tasks that are fulfilled by diferent providers. Thus, the user (usually through a broker) has to negotiate with a group of providers. While the negotiations with all of the providers could be conducted using the reservation values for the composite service, successful negotiation outcomes may be reached more efectively by determining reservation values specific to each component service.

The dificulty in finding appropriate reservation values for component services is that they are constructed into a composite service through diferent composition structures such as sequential, parallel, conditional, and loops (Sun et al. 2006, Ardagna and Pernici 2007). Furthermore, the aggregation of QoS metrics across component services depends not only on the composition structure but also on the type of attribute (Zeng et al. 2004). For example, if two component services to be executed in parallel have diferent response times, then negotiating down the time requirement for the longer service contributes more toward meeting the time constraint for the composite service. On the other hand, a unit decrease in price for either service contributes equally toward meeting the cost constraint. Because a composite service can be comprised of complex combinations of component services, and the reservation values for each attribute of every component service must account for the reservation values associated with all other component services to meet the user’s minimum requirement for the composite service, determining reservation values for each component is not straightforward.

We show that determining the reservation value for each QoS attribute of every component service can be modeled as a multiobjective optimization problem. We focus on identifying reservation values that maximize the chance of finding a contract acceptable to all of the providers. This is accomplished using a notion of preferability between the reservation values of the user and the ofers listed by the providers. This method (that we refer to as the base approach) is applicable to any composite service consisting of the four fundamental composition structures mentioned above. We then show how the multiobjective optimization problem can be transformed to a single-objective optimization problem using the max-min approach (Zimmermann 1987). Because a linear utility function is typically used to evaluate a software service (Ardagna and Pernici 2007, Yu et al. 2007), this problem can be solved using linear programming. The transformation may lead to a weak Pareto-optimal solution depending on the composition structure. We show how such solutions can be improved to strong Pareto-optimal ones.

If the user (or broker) knows the preferences of the diferent providers across diferent QoS attributes when creating a composite service, the chance of successfully creating a composite service can be increased by making trade-ofs between diferent QoS attributes for each provider.<sup>2</sup> Moreover, trade-ofs can also be made across providers of diferent component services. We extend the problem formulation for setting reservation values by taking into account the providers’ preferences, also considering situations where only some providers’ preferences are available. We then show how these extended problem formulations can also be solved using the max-min approach. We further identify special problem instances for which closed-form solutions can be obtained for the reservation values.

We then show how the reservation values can be incorporated in extant negotiation tactics. Importantly, if a provider accepts an ofer for a component service that is more preferable to the user than the corresponding reservation values, the reservation values for other component services could be dynamically changed to make the negotiation more likely to succeed for the composite service as a whole. To validate our method, we have conducted simulation experiments that show our method considerably increases the chance of successful negotiations over two benchmark approaches.

Furthermore, it increases the benefit for both the user and the providers. The improvements are more marked when the user (broker) knows the providers’ preferences. We also examine a less conservative variant of the base approach—such an approach generally leads to a reduced chance of negotiation success while slightly increasing the expected utility to the negotiating parties when negotiations are successful. We demonstrate that dynamically adjusting the reservation values further improves the chance of successful negotiations.

## 2. Literature Review

Our study contributes to the literature on QoS management for software services. Under the service level agreements framework (Ludwig et al. 2003), service provision is diferentiated based on properties (attributes) such as cost, responsiveness, and availability, and can be managed through creating service level agreements. In this framework, in addition to the functional specifications of their service, providers would specify typical nonfunctional properties in a service registry that users can search (Ran 2003, Al-Masri and Mahmoud 2007). Such registries allow automated discovery of services based on their functionalities, enabling users (or their brokers) to determine the typical attribute values associated with the component services they require. The registries also enable users (brokers) to determine for a specific functionality the range of values for each of the relevant QoS attributes across diferent providers of such a service; this can help establish the feasible ranges for the reservation values of the relevant attributes.

The life cycle of a QoS agreement consists of three stages: negotiation, execution, and termination (Koistinen and Seetharaman 1998). While a user can reach a service level agreement for the QoS through negotiation, the quality that the user eventually experiences when the service is executed may be diferent from what has been agreed—this is referred to as quality of experience (van Moorsel 2001). If the experienced quality is inferior to what was negotiated, the provider may be penalized to compensate for this. Penalties for noncompliance can be considered as QoS attributes for negotiation (Liu et al. 2004, Leitner et al. 2013); we assume this in our work as well. To determine whether an agreement is violated, the QoS needs to be monitored so that any violation can be tracked down: who committed the violation, the extent of the violation, at what time, etc. (Rana et al. 2008, Clark et al. 2010). This would help determine the penalty to be imposed on the corresponding party. When multiple parties are involved in providing services, the obligations of every party needs to be verified. While the literature has discussed several alternative approaches, the most promising approach appears to be one where a trusted third party is charged with fulfilling the monitoring function (Rana et al. 2008, Clark et al. 2010). This can help ensure a fair process, as neither the provider nor the client may fully trust the results from the other side.

Another body of research examines how existing software services should be selected to meet desired QoS requirements. These methods can be grouped into two categories: local selection and global optimization (Zeng et al. 2004). The local approach selects optimal service candidates for each individual task without considering the global constraints for a composite service. The global approach selects the set of service candidates that satisfy the global QoS requirements and maximize the overall utility of the composite service. Integer linear programming techniques have been proposed to identify the best service candidates for composing a new service (Zeng et al. 2004, Ardagna and Pernici 2007), and heuristics have been developed to solve the service selection problem in polynomial time (Yu et al. 2007). These approaches assume the QoS ofered by providers are fixed at any given time, without taking advantage of the potential flexibilities a provider may have in providing a specific service.

Negotiation has been investigated extensively in the game theory, economics, management science, and artificial intelligence literatures (Raifa 1982, Rubinstein 1982, Faratin et al. 2002). The game-theoretic negotiation models consider negotiation as a bilateral bargaining game and predict optimal outcomes under both complete and incomplete information scenarios. However, equilibrium conditions are available for very narrow settings of information uncertainty (Gatti et al. 2008); for instance, Chatterjee and Samuelson (1988) analyze a scenario where each player can be of two types, with each type corresponding to a predefined reservation value that is common knowledge.

Because of the dificulty in identifying equilibrium solutions in more general negotiation contexts, computational solutions have received substantial attention in the area of artificial intelligence and multiagent systems. Various mechanisms have been developed to negotiate using a set of predefined bargaining tactics (Faratin et al. 1998, 2002, Jennings et al. 2001). In the context of bilateral negotiations, Faratin et al. (1998) have proposed approaches that use a variety of polynomial and exponential functions to compute ofers in each iteration of a negotiation process; these approaches are also referred to as concession tactics. These tactics model concession behaviors that concede at diferent rates to the reservation value of a negotiation agent (recall that the reservation value is the least acceptable value to an agent). The concession tactics attempt to maximize the utility of the agent while determining a course of action that will potentially result in an agreement—the functional form adopted by the agent determines the concession amount acceptable to the agent in each iteration of the negotiation process. Faratin et al. (2002) show that when multiple issues are involved in bilateral negotiations, lowering the requirement on some issues to demand more on other issues can increase the chance of finding solutions acceptable to both sides involved in the negotiation. Our approach to determining reservation values also considers such trade-ofs.

Several negotiation protocols have been developed toward dynamic and flexible service provision (Sarangan and Chen 2006), e.g., resource negotiation and pricing (RNAP) protocol, service negotiation protocol (SrNP), and dynamic service negotiation protocol (DSNP). Mbarek et al. (2008) have proposed a service level negotiation protocol (SLNP) for end-toend QoS guarantees across heterogeneous domains, using a video conferencing application for illustration. Chalouf and Krief (2009) have proposed secure SLNP (SSLNP), which not only enables QoS negotiation but also ensures the security of such negotiations. The Open Grid Forum has proposed the Web Services Agreement Negotiation Specification to enable software service negotiation in grid and cloud computing (Waeldrich et al. 2011). The IEEE Next Generation Service Overlay Network (NGSON) working group has been working on developing standards and protocols, where negotiation is considered an important functionality to accomplish flexible and dynamic service provisioning (Lee and Kang 2012). In 2011, the working group developed a standard for functional architecture of NGSON with several protocols of NGSON still being worked out to fulfill all of the functional requirements of NGSON (https://standards.ieee.org/develop/wg/ 1903\_WG.html).

With the newly developed (and developing) negotiation protocols, guaranteeing end-to-end QoS through negotiation has become closer to reality. However, research on incorporating negotiation into service composition is quite limited. Lock (2006) proposes a method based on logic operators to specify a service contract for negotiation between users and providers. Napoli (2009) considers temporal constraints in the negotiation for service composition. Paurobally et al. (2007) employ automated negotiation to facilitate collaboration in the grid. The concession strategy has been adopted for service negotiation in mobile electronic commerce (Paurobally et al. 2003) and in QoS-aware service composition (Ardagna and Pernici 2007) where an extra budget (i.e., price) is allocated in exchange for a QoS improvement from the providers. Chalouf et al. (2011) have proposed an architecture for next generation networks. Based on this architecture, Chalouf et al. (2012) discuss an IPTV application where SLNP is used to allow QoS negotiation to guarantee end-to-end QoS. To our knowledge, no method exists for finding appropriate reservation values for the QoS attributes of each component service, to improve the chance of a successful negotiation.

## 3. Concepts of Service Composition

With the surge of interest in service-centric computing, service composition is attracting considerable attention. As discussed, several industry standards have been developed for collaboration across diferent webenabled services and to support the specification of composite services. In those standards, composite services are defined similar to workflows that contain a set of abstract services, which can be mapped to concrete component services at run time. We also use workflowbased service composition. We next introduce the concepts of service composition, including composite service specifications, the software service quality model, and the software service utility function.

## 3.1. Composite Service Specifications

Conceptually, a composite service can be specified as a high-level workflow including multiple tasks. Each task is accomplished by a component service delivered by a diferent provider. A composite service can be constructed with several component services using various composition structures, which are also referred to as workflow patterns (van der Aalst 2003, Wohed et al. 2003). In this study, we consider four basic composition structures—sequential, parallel, conditional branching, and loop structures—given the importance of these basic structures in service composition (Zeng et al. 2004) and the fact that most workflow structures can be simulated using them (Bi and Zhao 2004, Sun et al. 2006).

In a sequential structure (Figure 2(a)), a task $S _ { i + 1 }$ in a process is not enabled until the preceding task $S _ { i }$ is completed. In a parallel structure (Figure 2(b)), all tasks $\mathbf { \dot { ( } } S _ { 1 } , \dots , S _ { n } )$ in parallel branches are executed concurrently. In a conditional branching structure (Figure 2(c)), one execution path $S _ { i }$ is chosen among many alternative paths with probability $P R _ { i } ,$ where $\begin{array} { r } { \sum _ { i = 1 } ^ { n } P R _ { i } = 1 } \end{array}$ . In a loop structure (Figure 2(d)), a task $S _ { i }$ is executed n $( n \leq { \dot { K } }$ where K is a predefined maximum loop count) times before the next task is executed. Other complex structures can be considered as a combination of the four basic composition structures (Sun et al. 2006, Ardagna and Pernici 2007). For example, the multimedia content delivery service shown in Figure 1 is created through combining the sequential and parallel composition structures.

To simplify the service composition problem, loop structures in a composite service can be unfolded through cloning the tasks involved in the loop as many times as the maximum loop count specifies (Zeng et al. 2004). When a composite service includes conditional branching structures, there can be diferent execution paths for the composite service. We describe two concepts, execution route and subroute, which are useful in computing the QoS attributes of composite services (Zeng et al. 2004, Ardagna and Pernici 2007, Zheng and Lyu 2013).

Execution route. An execution route is defined as the set of tasks $\{ V _ { s } , S _ { 1 } , S _ { 2 } , \ldots , S _ { n } , V _ { e } \}$ that are executed from the start to the end in a composite service, and it includes only one branch in a conditional branching structure but all branches in a parallel structure. Each execution route $E R _ { l }$ has a probability $P R _ { l }$ to be executed where $P R _ { l }$ is given by the product of all of the probabilities for all of the conditional branches that are involved in the route $E R _ { l }$ . For a composite service with L execution routes, $\begin{array} { r } { \sum _ { l = 1 } ^ { L } P R _ { l } = 1 } \end{array}$ . For example, there is only one execution route for the composite service shown in Figure 1

$$
\begin{array}{c} E R _ {1} \colon \{V _ {s}, S _ {1}, S _ {2}, S _ {3}, S _ {4}, V _ {e} \} \\ \text { with   the   probability } P R _ {1} (P R _ {1} = 1) \text { to   be   executed. } \end{array}
$$

Subroute. A subroute of an execution route $E R _ { l }$ is a sequence of tasks from the start to the end tasks in $E \bar { R _ { l } }$ that do not contain any two branches that can be executed in parallel. When $E R _ { l }$ involves parallel structures, $E R _ { l }$ contains multiple subroutes. For example, in Figure 1, there are two subroutes

Figure 2. UML Activity Diagrams for Four Basic Composition Structures  
![](/api/attachments/FPZQHQ5A/fulltext/images/6bbb3b889f845aabfaa57dc525172bc24801ae3fe4472e20fdb69a3970bcfb88.jpg)

$$
\begin{array}{c} S R _ {1} \colon \{V _ {s}, S _ {1}, S _ {3}, S _ {4}, V _ {e} \}; \quad S R _ {2} \colon \{V _ {s}, S _ {2}, S _ {3}, S _ {4}, V _ {e} \}; \\ \text { and } \quad S R _ {1} \subset E R _ {1} \quad \text { and } \quad S R _ {2} \subset E R _ {1}. \end{array}
$$

## 3.2. The Software Service Quality Model

The QoS attributes, such as price, availability, execution time, and data quality, are associated with software service execution (Zeng et al. 2004, Ardagna and Pernici 2007, Yu et al. 2007). While there are nonnegotiable QoS attributes, e.g., reputation, we focus only on negotiable QoS attributes. Each software service $\dot { \boldsymbol { S } } _ { i }$ is associated with a vector $[ q _ { i , 1 } , \dots , q _ { i , k } , \dots , q _ { i , m } ]$ that represents the m QoS attribute values of the service. The value of a QoS attribute is a real number in a bounded range. For a composite service, the value of a QoS attribute is determined by aggregating the value of the attribute of the invoked component services using appropriate aggregation functions.

For some attributes, the aggregation is based on the execution routes in a composite service (Zeng et al. 2004). For example, the price of a composite service is given by the sum of the price of all of the component services in an invoked execution route. The availability of the composite service is given by the product of the availabilities of the component services included in an execution route. The data quality<sup>3</sup> of the composite service is determined by the minimum data quality of the component services invoked in an execution route (Ardagna and Pernici 2007). For some other attributes, the subroutes need to be considered as well. For instance, the execution time of a composite service with a parallel composition structure is the execution time of the subroute with the maximum execution time.

In general, the QoS attribute values of a composite service CS with n component services $\{ S _ { 1 } , \ldots , S _ { n } \}$ can be evaluated based on its execution routes $E R _ { l }$ $( l = 1 , 2 , \ldots , L )$ . Table 1 lists four important aggregation functions for determining representative QoS attribute values of an execution route. We consider these aggregation functions within the scope of our paper as they are the most widely used for negotiable QoS attributes (Zeng et al. 2004, Yu et al. 2007), including contextdependent QoS attributes (Pernici 2006).

A QoS attribute can be classified as either a positive or a negative attribute. A QoS attribute is positive (negative) if a higher (lower) value indicates a higher quality. We consider the negotiable QoS attributes that service brokers and service providers conflict over, e.g., an attribute that is negative for a service broker and positive for a service provider (for instance, price).

Consistent with the literature, we consider penalties for noncompliance as QoS attributes (Liu et al. 2004, Leitner et al. 2013). Leitner et al. (2013) observe that penalties for noncompliance could be modeled as either a constant penalty or a dynamic penalty, where the latter indicates that the penalty amount be tied to the extent of violation from the contracted attribute value (in other words, there is a penalty rate). Since multiple providers may be involved in service composition, a dynamic penalty will be appropriate as each provider can be held responsible for the extent of the violation with the delivery of their service. Thus, a penalty rate QoS attribute can be associated with each relevant intrinsic attribute (e.g., response time, data quality, etc.) of every component service involved. It can be handled similar to such QoS attributes as data quality because the minimum acceptable penalty rate of a composite service should be uniformly enforced on all of the component services.

## 3.3. Utility Function

To evaluate a software service, a utility function is used to map all of the QoS attribute values into a single value. In the service composition literature, the linear utility function has been widely adopted (Zeng et al. 2004, Ardagna and Pernici 2007, Yu et al. 2007). For a service $S _ { i }$ with the QoS attribute values $q _ { i , 1 } , \ldots , q _ { i , k } , \ldots , q _ { i , m } ,$ the utility function is defined as

$$
U _ {i} ^ {A} = \sum_ {k = 1} ^ {m} V _ {k} ^ {A} (q _ {i, k}) \cdot w _ {k} ^ {A},\tag{1}
$$

where $w _ { k } ^ { A }$ represents the importance of the QoS attribute k to agent $A , \Sigma _ { k = 1 } ^ { m } w _ { k } ^ { A } \dot { = } 1 , V _ { k } ^ { A } ( q _ { i , k } )$ is agent A’s scaling function that maps the QoS attribute value $q _ { i , k }$ to the interval <sup>[</sup>0, 1<sup>]</sup>, and the agent A can be either a service broker (representing the user) denoted as B or a service provider denoted as $P .$ The scaling functions for positive and negative attributes are defined in (2) and (3) where $q _ { i , k } ^ { \operatorname* { m a x } }$ and $q _ { i , k } ^ { \operatorname* { m i n } }$ are the maximal and minimal values of attribute k available on the market for service $S _ { i }$ and $q _ { i , k } ^ { \operatorname* { m a x } } \neq q _ { i , k } ^ { \operatorname* { m i n } }$ . The scaling function ensures that the utility function is not biased by any attribute with a large absolute value

Table 1. Aggregation Functions for Computing the QoS of Execution Routes

<table><tr><td>Aggregation function</td><td>Example attributes</td><td>Aggregation function</td><td>Example attributes</td></tr><tr><td> $q_{ER_l,k} = \sum_{S_i \in ER_l} q_{i,k}$ </td><td>Cost, CPU load, memory</td><td> $q_{ER_l,k} = \max_{SR_h \in ER_l} \left( \sum_{S_i \in SR_h} q_{i,k} \right)$ </td><td>Response time, estimate delay, packet jitter</td></tr><tr><td> $q_{ER_l,k} = \min_{S_i \in ER_l} q_{i,k}$ </td><td>Data quality, bandwidth</td><td> $q_{ER_l,k} = \prod_{S_i \in ER_l} q_{i,k}$ </td><td>Availability, reliability, packet loss</td></tr></table>

$$
V _ {k} ^ {A} (q _ {i, k}) = \frac {q _ {i , k} ^ {\max} - q _ {i , k}}{q _ {i , k} ^ {\max} - q _ {i , k} ^ {\min}} \quad \text { for   a   negative   attribute } k,\tag{2}
$$

$$
V _ {k} ^ {A} (q _ {i, k}) = \frac {q _ {i , k} - q _ {i , k} ^ {\min}}{q _ {i , k} ^ {\max} - q _ {i , k} ^ {\min}} \quad \text { for   a   positive   attribute } k.\tag{3}
$$

For a composite service CS with a total of L execution routes and each route $E R _ { l } \ ( l = 1 , 2 , \ldots , L )$ is to be executed with a probability $P R _ { l } ,$ we evaluate the expected utility of CS as follows:

$$
U _ {C S} ^ {B} = \sum_ {l = 1} ^ {L} (U _ {E R _ {l}} ^ {B} \cdot P R _ {l}),\tag{4}
$$

where $U _ { E R _ { 1 } } ^ { B }$ is the utility of route $E R _ { l }$ and can be computed from its QoS attributes using Equations $( 1 ) ‐ ( 3 )$ Note that the utility of a composite service is considered only for the service broker.

## 4. Determining Reservation Values

When a user requests a new composite service CS requiring n component services $\{ \bar { S _ { 1 } } , \ldots , S _ { n } \}$ , the user’s minimum requirements for the quality of CS (e.g., the price of CS has to be less than a certain amount) are specified as a set of global constraints $c _ { k }$ defined on a set of m QoS attributes of the composite service CS.<sup>4</sup> Consistent with the literature, we assume the user will typically not be aware of the structure of a composite service and can only specify the minimum QoS requirements (i.e., reservation values) for the composite service (Ardagna and Pernici 2007). For example, in the context of multimedia content delivery (Figure 1), when a user requests the latest news from a provider under a budget limit, the user may not know how the multimedia content is transcoded, translated, merged, and compressed before being delivered, not to mention setting the budget and other parameters for each component service.

The service broker, who is responsible for creating CS, negotiates with a group of service providers $1 , \ldots , n ,$ , each of whom will provide a component service $S _ { i } .$ . To facilitate the negotiation with each individual provider, the broker can first determine the reservation value for each QoS attribute of every component service based on the corresponding global constraint $c _ { k }$ and the ofers listed by the providers for the component services. Note that, for a QoS attribute, the reservation values of all component services should jointly satisfy the corresponding global constraint $c _ { k }$ An ofer with every QoS attribute equal to an agent’s reservation value is referred to as the agent’s reservation ofer. In Section 4.1, we discuss how to determine the user’s best reservation ofer for each component service when providers’ preferences are not known to the broker. Section 4.2 extends the proposed method to consider the providers’ preferences. In Section 4.3, we discuss situations where some providers’ preferences are known and others’ preferences are not. We present an example in Section 4.4 to illustrate our method. In Section 4.5, we show how to improve the solutions to strong Pareto optimality. We identify in Section 4.6 conditions under which closed-form solutions are available. For simplicity but without loss of generality, we use the attributes negative to the user to elaborate the proposed method.

## 4.1. Determining Reservation Values Without Knowing Providers’ Preferences

We use the multimedia content delivery example to first illustrate the problem of determining the reservation values and then discuss the problem formulation and the solution.

Example 1. The content delivery service in Figure 1 has four component services: $S _ { 1 }$ (transcoding), $S _ { 2 }$ (translation), $S _ { 3 }$ (merging), and $S _ { 4 }$ (compression). Each component service is delivered by a diferent predetermined provider. Two QoS attributes, price and response time, are associated with the component services. Table 2 shows the minimum and maximum values available on the market for every QoS attribute of each component service, and the ofer initially listed by the provider of each component.<sup>5</sup> The user has the following global QoS constraints for the composite service: $c _ { 1 } \leq \$ 1$ and $c _ { 2 } \leq 6 0$ seconds. Given this information, the broker cannot simply set its reservation values for $S _ { 1 } , S _ { 2 } , S _ { 3 } ,$ and $S _ { 4 }$ to be the ofers initially listed by the provider. This is because the global constraint $c _ { 1 }$ is violated in the execution route $\langle \check { S } _ { 1 } , S _ { 2 } , S _ { 3 } , S _ { 4 } \rangle$ , and $c _ { 2 }$ is violated in both subexecution routes $\{ S _ { 1 } , S _ { 3 } , S _ { 4 } \}$ and $\{ S _ { 2 } , S _ { 3 } , S _ { 4 } \}$ ♦

On one hand, the reservation values need to meet the global constraints. On the other hand, the reservation values need to be as close as possible to the ofer listed by a provider to improve the chance of acceptance by the provider. The more preferable the reservation values are to the provider, the more likely the negotiation will be successful. We define the preferability of the value $q _ { i , k } ^ { y }$ of QoS attribute k over the value $\boldsymbol { q } _ { i , k } ^ { x }$ of the same attribute for component service $S _ { i }$ as a normalized measure that captures the extent to which the former is preferred over the latter with respect to that attribute. Mathematically

$$
\operatorname{Pref} (q _ {i, k} ^ {x}, q _ {i, k} ^ {y}) = 1 - (V _ {k} ^ {P} (q _ {i, k} ^ {x}) - V _ {k} ^ {P} (q _ {i, k} ^ {y})) = 1 - \frac {q _ {i , k} ^ {x} - q _ {i , k} ^ {y}}{q _ {i , k} ^ {\max} - q _ {i , k} ^ {\min}}.\tag{5}
$$

The function Pre $\mathbb { f } ( q _ { i , k } ^ { x } , q _ { i , k } ^ { y } )$ has the range <sup>[</sup>0, 2<sup>]</sup>.

Without any information regarding providers’ preferences for diferent QoS attributes, to avoid underestimating the importance of any QoS attribute to a provider, the reservation value for every QoS attribute needs to be set as preferable as possible relative to the value acceptable to the service provider. Let the ofer listed by provider i for component service $S _ { i }$ be denoted as $\mathbf { \Phi } ^ { \mathrm { { i } } \mathrm { { i } } \mathrm { { s t } } } = \{ q _ { i , 1 } ^ { \mathrm { { l i s t } } } , \dots , q _ { i , k } ^ { \mathrm { { l i s t } } } , \dots , q _ { i , m } ^ { \mathrm { { l i s t } } } \}$ . We denote the broker’s reservation ofer for $S _ { i }$ as $o _ { i } ^ { \mathrm { { r e s e r v e d } } } =$ $\{ q _ { i , 1 } ^ { \mathrm { r e s e r v e d } } , \ldots , q _ { i , k } ^ { \mathrm { r e s e r v e d } } , \ldots , q _ { i , m } ^ { \mathrm { r e s e r v e d } } \}$ , which is to be determined. For each attribute $\overset { \cdot } { k } \left( k = 1 , \ldots , m \right)$ , the problem of setting reservation values for every component service can be formulated as the following multiobjective optimization problem:

Table 2. QoS Information for the Component Services in Example 1

<table><tr><td rowspan="2"></td><td colspan="2"> $S_1$ </td><td colspan="2"> $S_2$ </td><td colspan="2"> $S_3$ </td><td colspan="2"> $S_4$ </td></tr><tr><td>Price ($)</td><td>Response time (sec)</td><td>Price ($)</td><td>Response time (sec)</td><td>Price ($)</td><td>Response time (sec)</td><td>Price ($)</td><td>Response time (sec)</td></tr><tr><td>Minimum</td><td>0.40</td><td>30</td><td>0.20</td><td>20</td><td>0.10</td><td>5</td><td>0.10</td><td>5</td></tr><tr><td>Maximum</td><td>0.50</td><td>40</td><td>0.30</td><td>40</td><td>0.20</td><td>15</td><td>0.20</td><td>15</td></tr><tr><td>Listed offer</td><td>0.48</td><td>39</td><td>0.28</td><td>35</td><td>0.18</td><td>13</td><td>0.18</td><td>14</td></tr></table>

[P1]

Maximize $P r e f ( q _ { i , k } ^ { \mathrm { l i s t } } , q _ { i , k } ^ { \mathrm { r e s e r v e d } } )$ for every i <sup></sup> 1, . . . , n

(6)

Subject to $q _ { C S , k } ^ { \mathrm { r e s e r v e d } } \leq c _ { k } ,$

$$
q _ {i, k} ^ {\mathrm{min}} \leq q _ {i, k} ^ {\mathrm{reserved}} \leq q _ {i, k} ^ {\mathrm{max}},\tag{7}
$$

$$
\text {   for   every   } i = 1, \dots , n.\tag{8}
$$

Constraint (7) indicates that the reservation values for every component service together should satisfy the corresponding global constraint. Constraint (8) ensures that the reservation value $q _ { i , k } ^ { \mathrm { r e s e r v e d } }$ lies within its valid domain. Maximizing the objective functions leads to the values $q _ { i , k _ { . } } ^ { \mathrm { r e s e r v e d } }$ that are as desirable as possible from the providers’ points of view.

The reservation value for attribute k of the composite service, i.e., $q _ { C S , k } ^ { \mathrm { r e s e r v e d } }$ in (7), is a function of $q _ { i , k } ^ { \mathrm { r e s e r v e d } } .$ To compute $q _ { C S , k } ^ { \mathrm { r e s e r v e d } }$ , the reservation values for all of the component services, i.e., $q _ { i , k } ^ { \mathrm { r e s e r v e d } } .$ , are aggregated using the appropriate aggregation function. Given that the aggregation is computed based on either execution routes (e.g., price and availability) or subroutes (e.g, execution time), in order for an attribute k of the composite service, $\mathrm { i . e . , } q _ { C S , k } ^ { \mathrm { r e s e r v e d } }$ , to satisfy the global constraint $c _ { k } ,$ we ensure every execution route satisfies $c _ { k } .$ Constraint (7) in [P1] equivalent to Constraints (9) and (10); here EP is the set of numbers indexing the attributes for which reservation values have to be computed based on every execution route for the composite service, SP is the set of numbers indexing the attributes for which reservation values have to be computed based on every subroute for the composite service, and $E P \cup S P = \left\{ 1 , \dots , m \right\}$

$$
q _ {E R _ {l}, k} ^ {\text { reserved }} \leq c _ {k} \quad \text { for   every } k \in E P \text { and } l = 1, \ldots , L,\tag{9}
$$

$$
q _ {S R _ {h}, k} ^ {\text { reserved }} \leq c _ {k} \quad \text { for   every } k \in S P \text { and } h = 1, \dots , H.\tag{10}
$$

Constraints (9) and (10) guarantee that the relevant global constraints are met for every execution route and subroute.

For some attributes, $q _ { E R _ { I } , k } ^ { \mathrm { r e s e r v e d } }$ is decided by the product of the values of attribute k of all of the involved component services, $\mathrm { e . g . }$ , availability. Then constraints (9) and (10) are nonlinear and are linearized as follows. If for attribute $\begin{array} { r } { k , q _ { E R _ { l } , k } ^ { \mathrm { r e s e r v e d } } = \prod _ { s _ { i } \in E R _ { l } } q _ { i , k } } \end{array}$ then constraint (9) can be written as (Zeng et al. 2004)

$$
\prod_ {s _ {i} \in E R _ {l}} q _ {i, k} \leq c _ {k}.\tag{11}
$$

After applying the logarithm function, the constraint becomes linear

$$
\sum_ {s _ {i} \in E R _ {l}} \ln (q _ {i, k}) \leq \ln (c _ {k}).\tag{12}
$$

Note that the objective function must also be changed as follows. Let $q _ { i , k } ^ { \prime } = \ln ( q _ { i , k } )$ . Then in the objective function $\boldsymbol { q } _ { i , k } ^ { \prime }$ is considered to be the QoS attribute value instead of $q _ { i , k }$ . After the transformation, the original constraint still holds and both the objective functions and the constraints are linear in [P1].

Next, we show how [P1] can be solved (for each attribute separately) by transforming it to a singleobjective optimization problem. Using a max-min approach (Zimmermann 1987), the number of objectives can be reduced by introducing a new variable $\beta _ { k } .$ Here, $\beta _ { k }$ is the infimum of the preferability to the providers of the reservation value $q _ { i , k } ^ { \mathrm { r e s e r v e d } }$ over the value $q _ { i , k } ^ { \mathrm { l i s t } }$ for QoS attribute k that can be obtained from all of the component services. The underlying rationale for maximizing the minimum preferability is that the negotiation between the broker and any service provider is assumed equally important. If the negotiation for any component service fails, then the composite service cannot be obtained.<sup>6</sup> By introducing $\beta _ { k } , \mathrm { [ P 1 ] }$ can be transformed to a single objective optimization problem. Thus, for each QoS attribute $k ,$ we need to solve the following linear programming problem:

[P2]

Maximize $\beta _ { k }$

$$
\text { Subject   to } \quad \operatorname{Pref} (q _ {i, k} ^ {\text { list }}, q _ {i, k} ^ {\text { reserved }}) \geq \beta_ {k}, \quad \text { for   every } i = 1, \dots , n,
$$

$$
q _ {C S, k} ^ {\text { reserved }} \leq c _ {k},
$$

$$
q _ {i, k} ^ {\min} \leq q _ {i, k} ^ {\text { reserved }} \leq q _ {i, k} ^ {\max}, \quad \text { for   every } i = 1, \dots , n.
$$

Table 3. Providers Preferences for QoS Attributes in Example 1

<table><tr><td></td><td> $S_{1}$ </td><td> $S_{2}$ </td><td> $S_{3}$ </td><td> $S_{4}$ </td></tr><tr><td>Weight for price</td><td>0.4</td><td>0.6</td><td>0.3</td><td>0.7</td></tr><tr><td>Weight for response time</td><td>0.6</td><td>0.4</td><td>0.7</td><td>0.3</td></tr></table>

## 4.2. Determining Reservation Values Knowing All Providers’ Preferences

When a service provider’s preferences for diferent QoS attributes are known, making trade-ofs between the diferent attributes can help find reservation ofers more beneficial to the provider and thus increase the chance of negotiation success without sacrificing the utility to the user. Furthermore, if preferences for QoS attributes are diferent across diferent providers, it may be possible to find reservation ofers that ask less for QoS attributes from the providers who are more concerned with those attributes and request more of those attributes from other providers. In this manner, the reservation ofers can together still meet the global constraints and open up additional possibilities of generating ofers more beneficial to providers.

For instance, in Example 1, the providers’ preferences may be as shown in Table 3. The providers for $S _ { 1 }$ and $S _ { 3 }$ weigh response time more than price, and providers for $S _ { 2 }$ and $S _ { 4 }$ weigh price more. The broker can then set relatively low reservation prices for $S _ { 1 }$ and $S _ { 3 }$ and relatively short reservation response times for $S _ { 2 }$ and $S _ { 4 }$ to increase the chance of negotiation success for all of the component services.

Based on the notion of preferability between two values of a QoS attribute defined in (5), we define the preferability between two ofers<sup>7</sup> by taking into account all of the involved QoS attributes and how the providers weigh these attributes. Given two ofers $o _ { i } ^ { x } =$ $\mathbf { \widetilde { \{ } } q  _ { i , 1 } ^ { x } , \ldots , q _ { i , k } ^ { x } , \ldots , q _ { i , m } ^ { x } \}$ and $o _ { i } ^ { y } = \{ q _ { i , 1 } ^ { y } , \ldots , q _ { i , k } ^ { y } , \ldots , q _ { i , m } ^ { y } \}$ for component service $S _ { i }$ , the preferability of $o _ { i } ^ { y }$ over $o _ { i } ^ { x }$ is defined as a weighted combination of the preferability of all of the involved QoS attributes

$$
P r e f (o _ {i} ^ {x}, o _ {i} ^ {y}) = \sum_ {k = 1} ^ {m} w _ {i, k} \cdot P r e f (q _ {i, k} ^ {x}, q _ {i, k} ^ {y}),\tag{13}
$$

where $w _ { i , k }$ indicates the weight that provider i places on the QoS attribute k and $\begin{array} { r } { \sum _ { k = 1 } ^ { \overset { \smile } { m } } w _ { i , k } = \hat { 1 } } \end{array}$ . Based on Equations (5) and (13), we have

$$
P r e f (o _ {i} ^ {x}, o _ {i} ^ {y}) = 1 - \sum_ {k = 1} ^ {m} w _ {i, k} \cdot (V _ {k} ^ {p} (q _ {i, k} ^ {x}) - V _ {k} ^ {p} (q _ {i, k} ^ {y})).\tag{14}
$$

Function $P r e f ( o _ { i } ^ { x } , o _ { i } ^ { y } )$ indicates whether the ofer $o _ { i } ^ { y }$ is more preferable than the ofer $o _ { i } ^ { x }$ to provider i by considering the importance of each QoS attribute to service provider i. If $\hat { P r e f } ( o _ { i } ^ { x } , o _ { i } ^ { y } ) > 1$ , ofer $o _ { i } ^ { y }$ is more preferable to ofer $o _ { i } ^ { x } )$ ; if $P r e f ( o _ { i } ^ { x } , o _ { i } ^ { y } ) < 1$ , ofer $\stackrel { \cdot } { o } _ { i } ^ { y }$ is less preferable to ofer $o _ { i } ^ { x } ;$ and if $P r e f ( o _ { i } ^ { x } , o _ { i } ^ { y } ) = 1 , o _ { i } ^ { y }$ and $o _ { i } ^ { x }$ are equally preferable. Note that the range for $P r e f ( o _ { i } ^ { \dot { x } } , o _ { i } ^ { y } )$ is <sup>[</sup>0, 2<sup>]</sup> and the preferability between two ofers is analogous to the concept of similarity between two ofers proposed by Faratin et al. (2002).

Given the preferability between the two ofers, the problem of determining the reservation ofer is formulated as the following multiobjective optimization problem:

[P3]

$$
\text { Maximize } \quad P r e f (o _ {i} ^ {\text { list }}, o _ {i} ^ {\text { reserved }}) \quad \text { for   every } i = 1, \ldots , n
$$

Subject to $q _ { C S , k } ^ { \mathrm { r e s e r v e d } } \leq c _ { k }$ , for every k <sup></sup> 1, . . . , m ,

$$
\begin{array}{l} q _ {i, k} ^ {\min} \leq q _ {i, k} ^ {\text { reserved }} \leq q _ {i, k} ^ {\max}, \\ \quad \text { for   every } i = 1, \ldots , n, \text { and } k = 1, \ldots , m. \end{array}
$$

The objective functions maximize the preferability for each provider. The constraints have the same meaning and can be computed in the same way as constraints $( 7 )$ and (8) in [P1]. We note that the problem is no longer separable across the QoS attributes.

Since every component service is important for the composite service, the max-min approach is again appropriate. Therefore, we maximize the minimum preferability between ofers $o _ { i } ^ { \mathrm { l i s t } }$ and $o _ { i } ^ { \mathrm { r e s e r v e d } }$ that can be obtained across all of the component services. Denoting this minimum preferability as α, [P3] is transformed to the following linear programming problem:

[P4]

Maximize α

$$
\begin{array}{l} \text { Subject   to } \quad P r e f (o _ {i} ^ {\text { list }}, o _ {i} ^ {\text { reserved }}) \geq \alpha , \quad \text { for   every } i = 1, \ldots , n, \\ \quad q _ {C S, k} ^ {\text { reserved }} \leq c _ {k}, \quad \text { for } k = 1, \ldots , m, \\ \quad q _ {i, k} ^ {\min} \leq q _ {i, k} ^ {\text { reserved }} \leq q _ {i, k} ^ {\max}, \\ \quad \text { for   every } i = 1, \ldots , n, \text { and } k = 1, \ldots , m. \end{array}
$$

[P4] captures the trade-ofs between the QoS attributes through the preferability function in the first set of constraints.

## 4.3. Determining Reservation Values with Partial Preference Information

When some providers’ preferences are known to the broker and others are not, the problem of determining the appropriate reservation ofer can be formulated with two groups of objectives. If the preference of provider i is known, then the preferability between $\mathbf { \phi } _ { o _ { i } ^ { \mathrm { r e s e r v e d } } } ^ { \mathrm { r e s e r v e d } }$ and $o _ { i } ^ { \mathrm { l i s t } }$ needs to be optimized. If provider $i \prime \mathrm { s }$ preference is unknown, the preferability between $q _ { i , k } ^ { \mathrm { r e s e r v e d } }$ and $q _ { i , k } ^ { \mathrm { l i s t } }$ needs to be maximized for every QoS attribute $k = \mathrm { 1 } , \dots , m$ . Let SY denote the set of component services where providers’ preferences are known and SN denote the set of component services where providers’ preferences are unknown (note that $S Y \cup S N = \{ 1 , \ldots , n \} )$ . The reservation ofer o<sup>reserved</sup> can be determined by solving the following problem:

[P5]

Maximize $\{ P r e f ( o _ { i _ { 1 } } ^ { \mathrm { l i s t } } , o _ { i _ { 1 } } ^ { \mathrm { r e s e r v e d } } ) , P r e f ( q _ { i _ { 2 } , k } ^ { \mathrm { l i s t } } , q _ { i _ { 2 } , k } ^ { \mathrm { r e s e r v e d } } ) \} _ { . }$

for $i _ { 1 } \in S Y , i _ { 2 } \in S N , k = 1 , \dots , m$

Subject to $q _ { C S , k } ^ { \mathrm { r e s e r v e d } } \leq c _ { k } .$ , for every $k = 1 , \ldots , m$

$$
\begin{array}{l} q _ {i, k} ^ {\min} \leq q _ {i, k} ^ {\text { reserved }} \leq q _ {i, k} ^ {\max}, \\ \quad \text { for   every } i = 1, \ldots , n \text { and } k = 1, \ldots , m. \end{array}
$$

In this case, the problem cannot be separated for each attribute. Using the max-min approach, the number of objectives for [P5] can be reduced by introducing the variables α and $\beta _ { k }$ as follows:

[P6]

Maximize $\{ \alpha , \beta _ { k } \}$ , for $k = 1 , \ldots , m$

Subject to $q _ { C S , k } ^ { \mathrm { r e s e r v e d } } \leq c _ { k }$ , for $k = 1 , \ldots , m ,$

$$
\begin{array}{c} q _ {i, k} ^ {\min} \leq q _ {i, k} ^ {\text { reserved }} \leq q _ {i, k} ^ {\max}, \\ \text { for } i = 1, \ldots , n, \text { and } k = 1, \ldots , m, \end{array}
$$

$$
\operatorname{Pref} \left(o _ {i _ {1}} ^ {\text {list}}, o _ {i _ {1}} ^ {\text {reserved}}\right) \geq \alpha , \quad \text {for} i _ {1} \in S Y,
$$

$$
\begin{array}{c} P r e f (q _ {i _ {2}, k} ^ {\text {list}}, q _ {i _ {2}, k} ^ {\text {reserved}}) \geq \beta_ {k}, \\ \text {for i_{2} \in SN and k = 1,\ldots,m}. \end{array}
$$

In formulation [P6], α is the minimum preferability between the two ofers $o _ { i } ^ { \mathrm { l i s t } }$ and $o _ { i } ^ { \mathrm { r e s e r v e \hat { d } } }$ that can be obtained for those component services whose providers’ preferences are known. Similarly, $\beta _ { k }$ is the minimum preferability between the values $q _ { i _ { 2 } , k } ^ { \mathrm { l i s t } }$ and $q _ { i _ { 2 } , k } ^ { \mathrm { r e s e r v e d } }$ of QoS attribute $k ( k = 1 , \ldots , m )$ that can be obtained for those component services whose providers’ preferences are unknown. It is easy to see that when no preference information is available for any provider, $\mathrm { i . e . , } \ : \bar { S } Y = \emptyset .$ , [P6] reduces to [P2] and when the preference information for every provider is known, $\mathrm { i . e . , } \mathsf { \bar { { S } Y } } = \{ 1 , \ldots , n \}$ , [P6] reduces to [P4].

[P6] is also a multiobjective optimization problem. To provide a general solution to [P6], the ε-constraint method (Miettinen 1999) is used to transform [P6] to a single objective optimization problem by keeping one objective (α<sup>)</sup> and converting other objectives $( \beta _ { k } )$ into constraints

[P7]

Maximize α

Subject to $\beta _ { k } \ge \varepsilon _ { k } ,$ , for k <sup></sup> 1, . . . , m ,

$$
q _ {C S, k} ^ {\text { reserved }} \leq c _ {k}, \quad \text { for } k = 1, \dots , m,
$$

$$
q _ {i, k} ^ {\mathrm{min}} \leq q _ {i, k} ^ {\mathrm{reserved}} \leq q _ {i, k} ^ {\mathrm{max}},
$$

$$
\text {   for   } i = 1, \dots , n, \text {   and   } k = 1, \dots , m,
$$

$$
P r e f (o _ {i} ^ {\mathrm{list}}, o _ {i} ^ {\mathrm{reserved}}) \geq \alpha , \quad \mathrm{for} i _ {1} \in S Y,
$$

$$
\begin{array}{c} P r e f (q _ {i _ {2}, k} ^ {\text {list}}, q _ {i _ {2}, k} ^ {\text {reserved}}) \geq \beta_ {k}, \\ \text {for i_{2} \in SN and k = 1,\ldots,m}. \end{array}
$$

The appropriate values for the $\varepsilon _ { k } ^ { \phantom { } ^ { \prime } } \mathbf { s }$ are obtained as follows. Without considering any provider’s preference, we solve [P2] for each attribute $k = 1 , \ldots , m$ Suppose $\beta _ { k } ^ { \prime }$ is the lowest preferability obtained for attribute $k$ when providers’ preferences are assumed to be unknown. When some providers’ preferences are known, the minimal preferability between $q _ { i , k } ^ { \mathrm { r e s e r v e d } }$ and $q _ { i , k } ^ { \mathrm { l i s t } }$ obtained from the group of providers whose preferences are unknown should not be reduced. Therefore, $\beta _ { k } ^ { \prime }$ is a good lower bound for $\beta _ { k }$ when only some of the providers’ preferences are available. In other words, $\varepsilon _ { k } = \beta _ { k } ^ { \prime }$ . Once $\varepsilon _ { k }$ is identified by solving [P2] for every attribute, [P7] can be solved using linear programming.

## 4.4. An Illustration of the Solution

We illustrate using Example 1 the determination of the reservation values.

Example 1 (Continued). When the providers’ preferences are not known, formulation [P2] results in two linear programs (Table 4): EP1 to decide the reservation values for the prices, and EP2 to decide the reservation values for the response times. When all of the providers’ preferences are available, formulation [P4] results in problem EP3 (Table 4).

If the preferences of only providers $S _ { 1 }$ and $S _ { 4 }$ are known, then the reservation values can be determined from formulation [P7]. To solve [P7], $\varepsilon _ { k }$ is determined from the solutions to EP1 and EP2, from where we find that $\beta _ { 1 } ^ { \prime } = 0 . 7$ and $\beta _ { 2 } ^ { \prime } = 0 . 8$ . The parameters $\beta _ { 1 } ^ { \prime }$ and $\beta _ { 2 } ^ { \prime }$ are the lowest preferabilities between the reservation values and the values listed by the providers for $S _ { 2 }$ and $S _ { 3 }$ for attributes price and response time, respectively, when no service providers’ preferences are considered; therefore, $\varepsilon _ { 1 } = \beta _ { 1 } ^ { \prime }$ and $\varepsilon _ { 2 } = \beta _ { 2 } ^ { \prime }$ . Using these values for $\varepsilon _ { 1 }$ and $\varepsilon _ { 2 }$ in formulation [P7], we obtain EP4 as shown in Table 5.

Table 6 shows the estimate of the best utility that each provider can obtain if the broker was to concede to the reservation ofers. It illustrates how the consideration of providers’ preferences can help increase the utility of the reservation ofers to providers by making trade-ofs across diferent attributes and diferent component services, thus enhancing the chance of a successful negotiation. <sup>♦</sup>

## 4.5. Finding Strongly Pareto-Optimal Solutions

A solution is strongly Pareto optimal if no reservation value can be further relaxed without violating some constraints.<sup>8</sup> Both the min-max and the ε-constraint methods guarantee weak Pareto optimality of the solution obtained (Miettinen 1999), i.e., the set of reservation values obtained cannot all be relaxed without violation of the global constraints. As a result, it may be possible to further relax some reservation values without either afecting the other reservation values or

Table 4. Problem Formulations to Determine Reservation Values

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
All of the providers' preferences are unknown (no information) All of the providers' preferences are known (perfect information)

EP 1: Attribute price EP 2: Attribute response time EP 3
Maximize $\beta_{1}$ Maximize $\beta_{2}$ Maximize $\alpha$
Subject to Subject to Subject to
$1 - \frac{0.48 - q_{1,1}^{\text{reserved}}}{0.5 - 0.4} \geq \beta_{1}$ $1 - \frac{39 - q_{1,2}^{\text{reserved}}}{40 - 30} \geq \beta_{2}$ $1 - 0.4 \cdot \frac{0.48 - q_{1,1}^{\text{reserved}}}{0.5 - 0.4} - 0.6 \cdot \frac{39 - q_{1,2}^{\text{reserved}}}{40 - 30} \geq \alpha$ $1 - \frac{0.28 - q_{2,1}^{\text{reserved}}}{0.3 - 0.2} \geq \beta_{1}$ $1 - \frac{35 - q_{2,2}^{\text{reserved}}}{40 - 20} \geq \beta_{2}$ $1 - 0.6 \cdot \frac{0.28 - q_{2,1}^{\text{reserved}}}{0.3 - 0.2} - 0.4 \cdot \frac{35 - q_{2,2}^{\text{reserved}}}{40 - 20} \geq \alpha$ $1 - \frac{0.18 - q_{3,1}^{\text{reserved}}}{0.2 - 0.1} \geq \beta_{1}$ $1 - \frac{13 - q_{3,2}^{\text{reserved}}}{15 - 5} \geq \beta_{2}$ $1 - 0.3 \cdot \frac{0.18 - q_{3,1}^{\text{reserved}}}{0.2 - 0.1} - 0.7 \cdot \frac{13 - q_{3,2}^{\text{reserved}}}{15 - 5} \geq \alpha$ $1 - \frac{0.18 - q_{4,1}^{\text{reserved}}}{0.2 - 0.1} \geq \beta_{1}$ $1 - \frac{14 - q_{4,2}^{\text{reserved}}}{15 - 5} \geq \beta_{2}$ $1 - 0.7 \cdot \frac{0.18 - q_{4,1}^{\text{reserved}}}{0.2 - 0.1} - 0.3 \cdot \frac{14 - q_{4,2}^{\text{reserved}}}{15 - 5} \geq \alpha$ $0.4 \leq q_{1,1}^{\text{reserved}} \leq 0.5$ $30 \leq q_{1,2}^{\text{reserved}} \leq 40$ $0.4 \leq q_{1,1}^{\text{reserved}} \leq 0.5$, $30 \leq q_{1,2}^{\text{reserved}} \leq 40$ $0.2 \leq q_{2,1}^{\text{reserved}} \leq 0.3$, $20 \leq q_{2,2}^{\text{reserved}} \leq 40$ $0.1 \leq q_{3,1}^{\text{reserved}} \leq 0.2$, $5 \leq q_{3,2}^{\text{reserved}} \leq 15$ $0.1 \leq q_{4,1}^{\text{reserved}} \leq 0.2$, $5 \leq q_{4,2}^{\text{reserved}} \leq 15$ $q_{1,1}^{\text{reserved}} + q_{2,1}^{\text{reserved}} + q_{3,1}^{\text{reserved}} + q_{4,1}^{\text{reserved}} \leq 1$ $q_{1,2}^{\text{reserved}} + q_{3,2}^{\text{reserved}} + q_{4,2}^{\text{reserved}} \leq 60$ (i) $q_{1,2}^{\text{reserved}} + q_{3,2}^{\text{reserved}} + q_{4,2}^{\text{reserved}} \leq 60$ $q_{1,2}^{\text{reserved}} + q_{3,2}^{\text{reserved}} + q_{4,2}^{\text{reserved}} \leq 60$ Solution $q_{2,1}^{\text{reserved}} = 0.45$ Solution $q_{2,1}^{\text{reserved}} = 0.25$ Solution $q_{3,1}^{\text{reserved}} = 0.15$ Solution $q_{3,1}^{\text{reserved}} = 0.15$ Solution $q_{4,1}^{\text{reserved}} = 0.15$ Solution $q_{4,1}^{\text{reserved}} = 0.7$ Solution $q_{4,2}^{\text{reserved}} = 12$ Solution $q_{4,2}^{\text{reserved}} = 12$ Solution $q_{4,2}^{\text{reserved}} = 12$ Solution $q_{4,1}^{\text{reserved}} = 0.8$ Solution $q_{4,2}^{\text{reserved}} = 5.9$ Solution $q_{4,1}^{\text{reserved}} = 0.896$
</div>

## Table 5. Determining Reservation Values with Partial Preference Information

$$
S _ {1}
$$

$$
S _ {4}
$$

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
EP 4: Maximize $\alpha$

Subject to $\beta_{1} \geq 0.7$ $1 - \frac{0.28 - q_{2,1}^{\text{reserved}}}{0.3 - 0.2} \geq \beta_{1}; \quad 1 - \frac{0.18 - q_{3,1}^{\text{reserved}}}{0.2 - 0.1} \geq \beta_{1};$ $1 - 0.4 \cdot \frac{0.48 - q_{1,1}^{\text{reserved}}}{0.5 - 0.4} - 0.6 \cdot \frac{39 - q_{1,2}^{\text{reserved}}}{40 - 30} \geq \alpha;$ $0.4 \leq q_{1,1}^{\text{reserved}} \leq 0.5; \quad 0.2 \leq q_{2,1}^{\text{reserved}} \leq 0.3;$ $30 \leq q_{1,2}^{\text{reserved}} \leq 40; \quad 20 \leq q_{2,2}^{\text{reserved}} \leq 40;$ $q_{1,1}^{\text{reserved}} + q_{2,1}^{\text{reserved}} + q_{3,1}^{\text{reserved}} + q_{4,1}^{\text{reserved}} \leq 1;$ $q_{1,2}^{\text{reserved}} + q_{3,2}^{\text{reserved}} + q_{4,2}^{\text{reserved}} \leq 60;$

Solution $q_{1,1}^{\text{reserved}} = 0.42 \quad q_{1,2}^{\text{reserved}} = 40 \quad q_{2,1}^{\text{reserved}} = 0.25$ $q_{4,1}^{\text{reserved}} = 0.18 \quad q_{4,2}^{\text{reserved}} = 9 \quad \alpha = 0.83$
</div>

Table 6. Reservation Values Obtained with Diferent Availability of Preference Information

<table><tr><td rowspan="2"></td><td colspan="2">No information</td><td colspan="2">Partial information</td><td colspan="2">Perfect information</td></tr><tr><td>Reservation offer</td><td>Utility</td><td>Reservation offer</td><td>Utility</td><td>Reservation offer</td><td>Utility</td></tr><tr><td> $S_1$ </td><td>($0.45, 37.0 sec)</td><td>0.62</td><td>($0.42, 40.0 sec)</td><td>0.69</td><td>($0.45, 39.2 sec)</td><td>0.76</td></tr><tr><td> $S_2$ </td><td>($0.25, 31.0 sec)</td><td>0.52</td><td>($0.25, 31.0 sec)</td><td>0.52</td><td>($0.25, 39.2 sec)</td><td>0.68</td></tr><tr><td> $S_3$ </td><td>($0.15, 11.0 sec)</td><td>0.57</td><td>($0.15, 11.0 sec)</td><td>0.57</td><td>($0.10, 14.9 sec)</td><td>0.70</td></tr><tr><td> $S_4$ </td><td>($0.15, 12.0 sec)</td><td>0.56</td><td>($0.18, 9.0 sec)</td><td>0.66</td><td>($0.20, 5.9 sec)</td><td>0.73</td></tr></table>

violating the global constraints. This occurs when the workflow involves parallel or conditional structures; such structures can give rise to multiple optima. We next show how such solutions can be further improved to strong Pareto-optimal solutions.

We demonstrate this phenomenon using the reservation ofers for prices obtained in example EP2 in Table 4 (where no provider preferences are known). Constraint (i) is binding since the sum of the reservation response times for the subroute $\{ S _ { 1 } , S _ { 3 } , S _ { 4 } \}$ is 60 seconds and equals the global constraint. Constraint (ii) is nonbinding since the sum of the reservation response times for the subroute $\{ S _ { 2 } , S _ { 3 } , S _ { 4 } \}$ is only 54 seconds and thus there is a slack for this subroute. While the reservation values for the response time of $S _ { 3 }$ and $S _ { 4 }$ cannot be relaxed without afecting the binding constraint, the reservation value for the response time of $S _ { 2 }$ can be further relaxed to increase the chance of negotiation success for $S _ { 2 }$ . Similarly, the reservation value for the response time of $S _ { 2 }$ in EP4 can be further relaxed.

In general, after solving the problem at hand $( \mathrm { e . g . , }$ based on [P2], [P4], or [P7]), a reservation value for a component service may be further relaxed if the component service is involved only in the execution routes or subroutes where there remains some slack from a global constraint, i.e., the strict inequality $q _ { E R _ { l } , k } ^ { \mathrm { r e s e r v e d } } < c _ { k }$ or $q _ { S R _ { h } , k } ^ { \mathrm { r e s e r v e d } } < c _ { k }$ holds. To find a strong Pareto-optimal solution, the following steps are needed. First, the routes or subroutes with a slack are identified. Each attribute value (decision variable) involved in such constraints is then checked against the binding constraints to determine if they can be further relaxed; we denote such an attribute value as $q _ { i , k } ^ { \mathrm { r e s e r v e d } \prime }$ . Next, the original problem is revised to include only those constraints in which such attributes appear. The constraints are adjusted by incorporating the reservation values of attributes that cannot be adjusted, and the revised problem is solved. Repeating this process until no further relaxations can be made for any component service leads to a strong Pareto-optimal solution. We illustrate this for examples EP2 and EP4.

Example 2. As discussed previously, constraint (i) is binding while constraint (ii) is not for Problem EP2. Services $S _ { 3 }$ and $S _ { 4 }$ in constraint (ii) also appear in the subroute $\{ S _ { 1 } , S _ { 3 } , S _ { 4 } \}$ for which constraint (i) is binding, and therefore cannot be relaxed further. On the other hand, $S _ { 2 }$ is not involved in constraint (i) and therefore the reservation value for the response time of $S _ { 2 }$ can be further relaxed; we denote this relaxed reservation value as $q _ { 3 , 2 } ^ { \mathrm { r e s e r v e d } \prime }$ <sup>0</sup>. Revising EP2 given the reservation values obtained for $S _ { 3 }$ and $S _ { 4 } ,$ we obtain formulation EP5 in Table 7. EP5 only needs to check the subroute $\{ S _ { 2 } , S _ { 3 } , S _ { 4 } \}$ , which is afected by the relaxation. Similarly, we obtain formulation EP6 (Table 7) from EP4 to relax the response time of $S _ { 2 }$ . ♦

Table 7. The Problem Formulation for Obtaining Strong Pareto-Optimal Reservation Values

<table><tr><td>EP5 (from EP2)Maximize  $\beta_{2}$ Subject to $1 - \frac{35 - q_{2,2}^{\text {reserved}}}{40 - 20} \geq \beta_{2}$  $20 \leq q_{2,2}^{\text {reserved}} \leq 40$  $q_{2,2}^{\text {reserved}} + 11 + 12 \leq 60$ Solution  $q_{2,2}^{\text {reserved}} = 37 \quad \beta_{2} = 1.1$ </td><td>EP6 (from EP4)Maximize  $\beta_{2}$ Subject to $1 - \frac{35 - q_{2,2}^{\text {reserved}}}{40 - 20} \geq \beta_{2}$  $20 \leq q_{2,2}^{\text {reserved}} \leq 40$  $q_{2,2}^{\text {reserved}} + 11 + 9 \leq 60$ Solution  $q_{2,2}^{\text {reserved}} = 40 \quad \beta_{2} = 1.25$ </td></tr></table>

In the worst-case, finding strongly Pareto-optimal solutions may require relaxing $n \cdot m - 1$ reservation values and the corresponding linear program needs to be solved whenever a reservation value needs to be relaxed. Since the linear program can be solved in polynomial time (Vanderbei 2008), our method of finding strongly Pareto-optimal solutions is also of polynomial time complexity.

## 4.6. Properties of Solutions for Some Special Problem Instances

Because of the myriad diferent composition structures that may be encountered in practice, it is not possible to obtain closed-form solutions in general—this is because there is no closed-form solution for a general linear programming problem (Padberg 1999). However, we are able to show that closed-form solutions may be obtained under some specific conditions. These conditions and associated findings are summarized in the following propositions. We denote the optimal solution for provider i and attribute k as $q _ { i , k } ^ { \mathrm { r e s e r v e d * } }$ . All proofs are provided in the online appendix.

Proposition 1. For any general structure, if attribute k’s aggregation function is minimization, $q _ { i , k } ^ { \mathrm { r e s e r v e d * } } = c _ { k }$ provided that $q _ { i , k } ^ { \mathrm { { \dot { m i n } } } } \leq c _ { k } \leq q _ { i , k } ^ { \mathrm { { m a x } } }$

Proposition 1 shows that for attributes whose aggregation functions are minimization, the best reservation value for each component is the global constraint itself regardless of the composition structure or whether the providers’ preferences are known to the broker. Proposition 1 is also applicable to an attribute with a maximization aggregation function because such an attribute can be converted into an attribute with a minimization aggregation function by using the negation of that attribute value.

Proposition 2. For strictly sequential structures with unknown providers’ preferences [P2],

(a) if an attribute’s aggregation function is summation

$$
q _ {i, k} ^ {\text {reserved*}} = q _ {i, k} ^ {l i s t} - \frac {q _ {i , k} ^ {\max} - q _ {i , k} ^ {\min}}{\sum_ {i = 1} ^ {n} (q _ {i , k} ^ {\max} - q _ {i , k} ^ {\min})} \cdot \left(\sum_ {i = 1} ^ {n} q _ {i, k} ^ {l i s t} - c _ {k}\right),
$$

provided that

$$
q _ {i, k} ^ {\min} \leq q _ {i, k} ^ {l i s t} - \frac {q _ {i , k} ^ {\max} - q _ {i , k} ^ {\min}}{\sum_ {i = 1} ^ {n} (q _ {i , k} ^ {\max} - q _ {i , k} ^ {\min})} \cdot \left(\sum_ {i = 1} ^ {n} q _ {i, k} ^ {l i s t} - c _ {k}\right) \leq q _ {i, k} ^ {\max};
$$

(b) if an attribute’s aggregation function is multiplication, the optimal solution is one where

$$
\begin{array}{c} \ln (q _ {i, k} ^ {\text {reserved*}}) = \ln (q _ {i, k} ^ {\text {list}}) - \frac {\ln (q _ {i , k} ^ {\text {max}}) - \ln (q _ {i , k} ^ {\text {min}})}{\sum_ {i = 1} ^ {n} (\ln (q _ {i , k} ^ {\text {max}}) - \ln (q _ {i , k} ^ {\text {min}}))} \\ \cdot \left(\sum_ {i = 1} ^ {n} \ln (q _ {i, k} ^ {\text {list}}) - \ln (c _ {k})\right), \end{array}
$$

provided that

$$
\begin{array}{c} \ln (q _ {i, k} ^ {\min}) \leq \ln (q _ {i, k} ^ {l i s t}) - \frac {\ln (q _ {i , k} ^ {\max}) - \ln (q _ {i , k} ^ {\min})}{\sum_ {i = 1} ^ {n} (\ln (q _ {i , k} ^ {\max}) - \ln (q _ {i , k} ^ {\min}))} \\ \cdot \left(\sum_ {i = 1} ^ {n} \ln (q _ {i, k} ^ {l i s t}) - \ln (c _ {k})\right) \leq \ln (q _ {i, k} ^ {\max}). \end{array}
$$

Proposition 2(a) shows that for a strictly sequential composite structure where the broker has no information about providers’ preferences, the optimal reservation values for a QoS attribute that has a summation aggregation function can be obtained by first determining the diference between the aggregate of the listed values over the components and the global constraint $( \mathrm { i . e . , }$ the infeasible amount), and then adjusting that amount from the individual listed values of the component services in a manner proportional to the dispersion (range) of the attribute values of the component services provided the solutions remain feasible. A similar idea, with appropriate log transformation, applies to attributes whose aggregation function is multiplication (Proposition 2(b)).

We show in Proposition 3 that a closed-form solution can also exist under some additional conditions when the broker knows all providers’ preferences [P4]. As the aggregation functions multiplication and maximization can be converted to summation and minimization, respectively, after suitable transformations, we only consider two sets of attributes—those with an aggregation function summation (this set is denoted by A<sup>)</sup> and those with minimization (denoted by B).

Proposition 3. For strictly sequential structures where the broker knows all providers’ preferences [P4]

$$
q _ {i, k} ^ {\text { reserved* }} = q _ {i, k} ^ {\text { list }} - \frac {q _ {i , k} ^ {\max} - q _ {i , k} ^ {\min}}{\sum_ {i = 1} ^ {n} (q _ {i , k} ^ {\max} - q _ {i , k} ^ {\min})} \cdot \left(\sum_ {i = 1} ^ {n} q _ {i, k} ^ {\text { list }} - c _ {k}\right) \quad \forall   k \in A,
$$

if the following conditions are satisfied: (1) for every $k ,$ $w _ { i , k }$ is equal $\forall i ; ( 2 )$ for every $k , q _ { i , k } ^ { \mathrm { m a x } } - q _ { i , k } ^ { \mathrm { m i n } }$ is equal $\forall i ;$ (3) when $k \in A$

$$
q _ {i, k} ^ {\min} <   q _ {i, k} ^ {\text {list}} - \frac {q _ {i , k} ^ {\max} - q _ {i , k} ^ {\min}}{\sum_ {i = 1} ^ {n} (q _ {i , k} ^ {\max} - q _ {i , k} ^ {\min})} \cdot \left(\sum_ {i = 1} ^ {n} q _ {i, k} ^ {\text {list}} - c _ {k}\right) <   q _ {i, k} ^ {\max};
$$

(4) when $k \in { \cal B } , q _ { i , k } ^ { \operatorname* { m i n } } \le c _ { k } \le q _ { i , k } ^ { \operatorname* { m a x } } ;$ ; and (5) when $k \in B , q _ { i , k } ^ { \mathrm { l i s t } }$ is equal <sup>∀</sup> i.

Interestingly, Proposition 2 is also applicable to a general structure when the aggregation of an attribute in the structure is equivalent to the aggregation of the attribute in a strictly sequential structure. For example, the closed-form solution for the attribute price in Example 1 (i.e., problem EP1 in Table 4) can be derived from Proposition 2(a) because the aggregated price of component services $S _ { 1 }$ (transcoding), $S _ { 2 }$ (translation), $S _ { 3 }$ (merging), and $S _ { 4 }$ (compression) is the same regardless of whether the services are executed in sequence or in parallel, and the condition specified in the proposition is satisfied. However, Proposition 2 does not provide the optimal solution for the attribute response time in Example 1 $( \mathrm { i . e . , }$ problem EP2 in Table 4) because, due to the parallel structure, the aggregate function for response time in Example 1 is diferent from that of a composite service in which $S _ { 1 } , S _ { 2 } , S _ { 3 } ,$ and $S _ { 4 }$ are executed sequentially. Similarly, Proposition 3 cannot be used to derive the optimal solution for problem EP3.

The closed-form solutions from Propositions 2 and 3 provide useful insights regarding properties of desirable solutions. We use these solutions to develop the second benchmark approach in Section 6.

## 5. Incorporating the Proposed Approach in the Negotiation Process

We discuss next how the proposed method of setting reservation values can be embedded into existing negotiation processes. We should point out that the main contribution of our work is the proper determination of reservation values for component services. The other aspects of the negotiation processes we assume (such as agents’ concession and trade-of tactics, concurrent or sequential negotiation, etc.) reflect best practices in the extant literature, and we do not attempt to improve on those aspects themselves. Our method to determine reservation values is applicable regardless of how these other aspects of the negotiation process are implemented.

Consistent with the literature, we assume the broker negotiates with a group of providers concurrently (Nguyen and Jennings 2005, Ardagna and Pernici $2 0 0 7 ) . ^ { \circ }$ The negotiation between the broker and each service provider is considered as a bilateral bargaining session. Therefore, the whole negotiation process consists of a set of parallel bilateral bargaining sessions. In each such session the broker negotiates with one provider to identify an acceptable ofer for a component service.

At the beginning of the negotiation process, the broker computes the reservation ofers for each component service using the appropriate formulation depending on how much of the providers’ preferences are known. Then, in each session, the broker and the corresponding provider take turns sending messages to each other. A message can be either a new ofer or an indication that the ofer proposed by the opponent is acceptable. To generate a new ofer, each agent uses its own concession tactic—we describe this process in Section 5.1. These tactics are a function of the utility to the agent from its most aggressive ofer, the utility from its reservation ofer,<sup>10</sup> and the remaining time before the deadline. The deadlines, reservation values, and functional forms of the concession rates are all assumed to be private information to the agents involved in the negotiation. If the broker knows the preference of a provider, the broker can further modify its ofer using a trade-of tactic of the nature proposed by Faratin et al. (2002). This helps generate ofers more likely to be acceptable to the provider, as described in Section 5.2.<sup>11</sup>

If an ofer proposed by an agent has a higher utility to the opponent than the ofer the opponent would have proposed in the next iteration, then the ofer is acceptable to the opponent. If an acceptable ofer is identified for a component service prior to the deadline, it will be no worse to the user than its reservation ofer for that component. This can provide flexibility to the broker in relaxing the reservation values of the remaining services, and the broker can adjust those reservation values in the other ongoing sessions. We discuss how the reservation values can be dynamically adjusted in Section 5.3.

Each negotiation session has multiple iterations of exchanging ofers and counterofers between the broker and a provider; for simplicity we assume the iterations are synchronized across diferent sessions (with the diferent providers). An acceptable ofer must be identified for every component service before the final deadline in order for the whole negotiation process to end successfully. If an acceptable ofer cannot be identified for even one component service by the deadline, then the whole negotiation process fails. The overall negotiation process is formally described in the appendix.

## 5.1. The Concession Tactic

We adopt the time-dependent concession heuristic (tactic) proposed by Faratin et al. (1998) for each negotiation session. In each session, the broker first determines the utility level (to the broker/user) of the ofer to be made using the concession tactic. Based on this utility level, the broker determines the attribute values of the ofer. Let the ofer to be proposed by the broker for service $S _ { i }$ at iteration t be denoted by $o _ { i , t } = \{ q _ { i , 1 , t } , \dots , q _ { i , k , t } , \dots , q _ { i , m , t } \}$ , where $q _ { i , k , t }$ is the value ofered for the QoS attribute k of $S _ { i }$ . The utility of $o _ { i , t } ,$ $U _ { i } ^ { B } ( t )$ , is obtained by the following concession function:

$$
U _ {i} ^ {B} (t) = U _ {i, \mathrm{reserved}} ^ {B} + (1 - \mu_ {i} ^ {B} (t)) (U _ {i, \mathrm{max}} ^ {B} - U _ {i, \mathrm{reserved}} ^ {B})
$$

$$
\text { where } \mu_ {i} ^ {B} (t) = \left(\frac {\min (t , t _ {i , \max} ^ {B})}{t _ {i , \max} ^ {B}}\right) ^ {1 / \nu_ {i} ^ {B}}.\tag{15}
$$

Utility $U _ { i , \operatorname* { m a x } } ^ { B }$ is the utility of the most aggressive ofer the broker B wants to ask from provider i and $U _ { i . } ^ { B }$ i, reserved is the utility of the broker’s reservation ofer for component service $S _ { i }$ . The function $\mu _ { i } ^ { B } ( t )$ satisfies $0 \leq$ ${ \bf { \dot { \mu } } } \mu _ { i } ^ { B } ( t ) \le 1 , \ \mu _ { i } ^ { B } ( 0 ) = 0 ,$ and $\mu _ { i } ^ { B } ( t _ { i , \operatorname* { m a x } } ^ { B } ) \dot { = } 1$ , and $t _ { i , \mathrm { m a x } } ^ { B } \ \mathrm { i s }$ the predefined maximum number of iterations. The heuristic shown in (15) helps the broker concede to its reservation ofer by the deadline $t _ { i , \mathrm { m a x } } ^ { B }$ . Coeficient $\nu _ { i } ^ { B }$ determines the degree of concavity/convexity of the concession curve. If $\nu _ { i } ^ { B } > 1$ , the curve is convex and the broker quickly concedes to its reservation ofer. If $\nu _ { i } ^ { B } < 1$ , the curve is concave and the broker concedes slowly at the beginning of a negotiation process and concedes quickly to the utility of the broker’s reservation ofer only when the deadline is approaching. If ${ \nu } _ { i } ^ { B } { = } 1 , { \mu } _ { i } ^ { B } ( t )$ is linear, indicating that the service broker concedes at a constant rate (Faratin et al. 1998).

When a provider’s preferences are unknown, after deciding the utility level of the ofer to be made the broker determines the new ofer’s attribute values by conceding the same proportion on every attribute.

## 5.2. Incorporating a Provider’s Preferences Information

If a provider’s preference is known, we adopt the tradeof tactic of Faratin et al. (2002) in conjunction with the concession tactic to help the broker generate ofers not only beneficial to the service user but also more likely to be acceptable to the provider. The utility level of a new ofer is obtained as before using the concession tactic. The parameters of the ofer are decided so as to provide the best possible utility to the provider without compromising on the utility to the user—this is accomplished by trade-ofs made between diferent QoS attributes. Let $o _ { i , t } = \{ q _ { i , 1 , t } , \ldots , q _ { i , m , t } \}$ be the ofer the broker is preparing to issue to provider i at iteration t. The problem of determining ofer $o _ { i , t }$ is the following linear program:

$$
\text { Maximize } U ^ {p} (o _ {i, t})\tag{16}
$$

$$
\text { Subject   to } \quad q _ {i, k, t} \leq q _ {i, k} ^ {\text { reserved }} \quad \text { for } k = 1, 2, \dots , m,\tag{17}
$$

$$
U ^ {B} (o _ {i, t}) = U _ {i} ^ {B} (t),\tag{18}
$$

where $q _ { i , k } ^ { \mathrm { r e s e r v e d } }$ is the reservation value the broker has obtained for the QoS attribute k of component service $S _ { i } ; U ^ { B } ( o _ { i , t } )$ and $U ^ { P } ( o _ { i , t } )$ are the utilities of ofer $o _ { i , t }$ to the broker and the involved provider, respectively, and determined using Equation (1); and $U _ { i } ^ { B } ( t )$ is the utility level for the broker at iteration t as decided by the concession heuristic shown in (15). Constraint (17) indicates that the new ofer is no worse for the broker than the broker’s reservation ofer for each attribute. Constraint (18) ensures that the new ofer has the utility to the broker determined by the concession tactic.

## 5.3. Adjusting Reservation Values in the Negotiation Process

In the course of negotiation, some providers may accept ofers before the negotiation deadline. When a provider accepts such an ofer, it will be no worse to the broker than the broker’s reservation ofer, and can be better. This adds flexibility (slack) to the global constraints, and can be used to relax the reservation values for the remaining component services; the broker may now be able to concede more for these components. Thus, whenever a provider accepts an ofer, the reservation values for the other component services should be adjusted. The adjusted reservation values can be obtained using formulations [P2], [P4], or [P7] as appropriate. The constraints corresponding to global requirements are adjusted by accounting for the completed negotiation sessions. For the constraints corresponding to the preferability functions, only those are retained that correspond to component services where negotiation is ongoing. Moreover, for these constraints, the ofer proposed by the provider most recently can be used in calculating the preferability functions. Because a provider’s ofers get closer to the provider’s reservation ofer as the negotiation progresses, the broker’s reservation values can be adjusted more efectively by considering the providers’ most recent ofers.

Interestingly, if the providers concede at very diferent rates, it is possible that for some component services the adjusted reservation ofers may have worse utilities to the corresponding providers, as compared to the original reservation ofer without adjustment. This is undesirable as it can jeopardize the likelihood of a successful negotiation. To prevent this, an additional constraint is added to the pertinent problem formulation. Constraint (19) is added for component services where the providers’ preferences are unknown, and constraint (20) for the component services where the providers’ preferences are known

$$
q _ {i, k} ^ {\text { reserved }} \geq q _ {i, k} ^ {\text { reserved }}, \quad \text { and }\tag{19}
$$

$$
U ^ {P} (o _ {i} ^ {\text { reserved } \prime \prime}) \geq U ^ {P} (o _ {i} ^ {\text { reserved }}),\tag{20}
$$

where $o _ { i } ^ { \mathrm { r e s e r v e d } \prime \prime } = \{ q _ { i , 1 } ^ { \mathrm { r e s e r v e d } \prime \prime } , \ldots , q _ { i , k } ^ { \mathrm { r e s e r v e d } \prime \prime } , \ldots , q _ { i , m } ^ { \mathrm { r e s e r v e d } \prime \prime } \}$ is the adjusted reservation ofer for component service $S _ { i }$ and $o _ { i } ^ { \mathrm { r e s e r v e d } }$ is the reservation ofer before making the adjustment.

When the reservation values have been adjusted, the concession tactics shown in (15) also need to be revised accordingly to incorporate the new reservation values. Suppose at the $t _ { 1 } { \cdot } \mathrm { t h } ^ { - }$ iteration, the broker has reached agreements with some providers and thus adjusted the reservation values. The utility of the broker’s previous reservation ofer, $U _ { i , \mathrm { r e s e r v e d } } ^ { B }$ , must be replaced with the utility of the adjusted reservation ofer, $U _ { i , \mathrm { r e s e r v e d } } ^ { B \prime \prime } ,$ in Equation (15). We define the revised concession function as

$$
U _ {i} ^ {B} (t) ^ {\prime \prime} = U _ {i, \mathrm{reserved}} ^ {B \prime \prime} + (1 - \mu_ {i} ^ {B} (t)) \cdot (U _ {i, \mathrm{max}} ^ {B \prime \prime} - U _ {i, \mathrm{reserved}} ^ {B \prime \prime}),\tag{21}
$$

where $t \geq t _ { 1 } ,$ and the term $U _ { i , \mathrm { m a x } } ^ { B { \prime \prime } }$ can be determined as follows. To ensure continuity in the concession process, the utility from the revised concession function $U _ { i } ^ { B } ( t ) ^ { \prime \prime }$ is set equal to the utility of the previous concession function $U _ { i } ^ { B } ( t )$ at iteration $t _ { 1 } , \mathbf { i . e . }$

$$
\begin{array}{l} U _ {i} ^ {B} (t _ {1}) ^ {\prime \prime} = U _ {i} ^ {B} (t _ {1}) \quad \text { where } \\ U _ {i} ^ {B} (t _ {1}) = U _ {i, \text { reserved }} ^ {B} + (1 - \mu_ {i} ^ {B} (t _ {1})) \cdot (U _ {i, \max} ^ {B} - U _ {i, \text { reserved }} ^ {B}). \end{array}\tag{22}
$$

Equating Equation (21) with (22), we obtain

$$
U _ {i, \max} ^ {B \prime \prime} = \frac {U _ {i} ^ {B} (t _ {1}) - U _ {i , \text {reserved}} ^ {B \prime \prime}}{1 - \mu_ {i} ^ {B} (t _ {1})} + U _ {i, \text {reserved}} ^ {B \prime \prime}.\tag{23}
$$

Therefore, the revised concession function is

$$
U _ {i} ^ {B} (t) ^ {\prime \prime} = U _ {i, \text {reserved}} ^ {B \prime \prime} + \frac {1 - \mu_ {i} ^ {B} (t)}{1 - \mu_ {i} ^ {B} (t _ {1})} \cdot (U _ {i} ^ {B} (t _ {1}) - U _ {i, \text {reserved}} ^ {B \prime \prime}).\tag{24}
$$

The revised concession function enables the broker to continue to concede from the utility it was at after the $t _ { 1 } \mathrm { - t h }$ iteration to the utility of the adjusted reservation ofer by the deadline.

## 6. Experimental Analysis

## 6.1. Benchmark Methods and Evaluation Metrics Metrics

The problem we examine (i.e., determining optimal reservation values for component services when constructing a composite service through negotiation) has not been studied in prior research, and there are no existing solutions in the literature. Therefore, to study the performance of our methodology, we create two benchmark methods that we believe are reasonable approaches that could be adopted in practice. In the first benchmark, the broker uses the concession tactic to negotiate concurrently with all providers without setting separate reservation values for each component service. In each iteration of the negotiation, the broker first applies the time-dependent concession tactic to determine the aggregate ofer for the composite service. The ofers for component services are then derived in a manner that attempts to ensure the preferabilities of these new ofers to the diferent providers are being adjusted in an equitable fashion. For example, for an attribute whose aggregation function is summation, the broker allocates to each component service a portion of the relaxation being made for the attribute in this ofer—this allocation is done proportional to the dispersion (range) of the QoS attribute values of the component services. A similar approach is used for attributes whose aggregation functions are multiplications after a logarithm transformation. For an attribute with a minimization aggregation function, the value determined by the concession tactic for the composite service is used directly as the ofer for every component service. We call this benchmark

Global\_RV\_Bench. By comparing our approach with this benchmark, we demonstrate the value of setting reservation values for individual component services.

The second benchmark allows the broker to set reservation values for the component services separately. In this benchmark, for attributes with summation aggregation function, the broker first determines the diference between the aggregate of the listed values over the components and the global constraint (i.e., the infeasible amount). To ensure the global constraint is satisfied, the individual listed value of each component service is then adjusted downward in a manner proportional to the dispersion (range) of the attribute value of the component service to arrive at the reservation value (this approach would lead to optimal reservation values for structures for which closed-form solutions can be obtained, i.e., those discussed in Propositions 2 and 3). A similar approach, with a logarithm transformation, is used for attributes with multiplication aggregation functions. For an attribute whose aggregation function is minimization, the global constraint itself becomes the reservation value for each component; this is guaranteed to be optimal (from Proposition 1). The underlying rationale is the same as for the first benchmark—an attempt to ensure the adjustment of the infeasible amount leads to an equitable adjustment of the preferabilities to the diferent providers from the reservation values. Once the reservation values have been decided, the bilateral negotiation stage is the same as in our method—if a provider’s preference is known to the broker, the similarity-based negotiation strategy (Faratin et al. 2002) is used; if a provider’s preference is unknown, the broker concedes with the same proportion on each attribute. We refer to this approach as Component\_RV\_Bench. This benchmark is an intelligent one in its own right, and a comparison of our approach with this benchmark demonstrates the efectiveness of using our proposed method for setting reservation values.

We refer to our base method as Fixed\_RV\_Proposed and our method with dynamic adjustment as Dynamic \_RV\_Proposed. We first compare the performance of the base method with the two benchmarks. Next, we examine whether using the dynamic approach improves on the performance of our base approach. Finally, for situations where the broker knows the preferences of some but not all providers (the partial information scenario), we consider an alternative to our proposed approach that we call Fixed\_RV\_Median, which uses the median of the known preference weights to approximate the preferences of the providers whose preferences are not known. To evaluate the negotiation outcomes, we use the following metrics adopted in the literature (Faratin et al. 2002, Cheng et al. 2006): (i) negotiation success rate, (ii) the average utility of the composite service to the user when negotiations are successful, and (iii) the average utility obtained by providers when negotiations are successful.

## 6.2. Experimental Procedures

The experiments have been conducted on an HP Compaq dc7900 machine with an Intel Core 2 Duo E8400 CPU, a clock speed of 3 GHz, and 2 GB RAM. We use the open source package LpSolve (version 5.5) to solve the linear programs. To ensure that the results we report are robust, and are as representative as possible with regards to a wide range of feasible real-world scenarios, we have varied the problem parameters over a large range of values, as discussed below.

Negotiation is conducted over four QoS attributes (execution time, cost, availability, data quality)<sup>12</sup> for composite services with 10, 20, and 30 components, respectively. The composite services contain all of the basic composition structures with some structures being nested with others. Because of the nested structures, there are a total of 6, 20, and 36 subroutes in the composite services with 10, 20, and 30 components, respectively.<sup>13</sup> The length of the subroutes varies from 6 to 24 component services. The minimum and maximum execution times of a component service are randomly generated within the ranges [4–15 seconds] and [20–40 seconds], respectively. The minimum and maximum costs of a component service are randomly generated within the ranges [\$10–\$30] and [\$40–\$70], respectively. The lower bounds of the availability and the data quality of a component service are randomly generated within the ranges [0.9–0.95] and [0.85–0.9], respectively. The upper bounds of the availability and the data quality of a component service are both set to 1.<sup>14</sup> The preference weights for the attributes are randomly generated for the broker and for each provider, ensuring they sum to 1 for each agent.

In the negotiation process, each provider has a reservation utility, i.e., the least utility level of an ofer acceptable to the provider. The reservation utility for each provider is randomly set between 0.4 and 0.6. A provider does not disclose its reservation utility to the broker. The ofer initially listed by a provider is the ofer that has the maximum (minimum) value for every positive (negative) attribute. To generate a subsequent ofer, the provider first uses the time dependent concession tactic to determine the utility of the ofer and then determines the ofer parameters by conceding equally on every attribute. The coeficient $v _ { i } ^ { P }$ that determines the concavity/convexity degree of the concession tactic for the provider is randomly generated in the range [0.4–2.5]. The provider accepts an ofer from the broker only if the utility of the ofer is not less than that of the counterofer the provider would propose in the next iteration.

The coeficient $v _ { i } ^ { B }$ for the broker’s concession tactic is also varied over the values 0.4, 1.0, and 2.5. It is set to be the same for both the proposed approach and the benchmarks. The experimental results were very similar for all three values of $v _ { i } ^ { B } .$ , therefore we report only the results when $v _ { i } ^ { B } = 1$ . When using the proposed approach, the broker may have perfect, partial, or no information on how the providers weight different attributes. When the broker has partial information, the broker knows the preferences of 50% of the providers. The maximum number of iterations is set to 100 for both the broker and providers.<sup>15</sup>

The success of the negotiation process depends on whether the reservation ofer held by the broker can deliver at least the reservation utility expected by a provider. Because the broker’s reservation ofers are determined based on the global constraints, the overall negotiation between the broker and the providers is more likely to fail when the global constraints are stringent. In the experiments, we generate sets of global constraints that have diferent levels of stringency. We use the lowest preferability (denoted as $\alpha ^ { \prime } )$ that can be obtained between the reservation ofer of the broker and the reservation ofer of a provider among all of the component services to indicate the stringency of the global constraints. Given the randomly generated weights and the reservation utility for each provider, each set of global constraints corresponds to an $\alpha ^ { \prime } ,$ which can be determined by solving [Problem P4]. Only when $\alpha ^ { \prime } \geq 1$ can the broker’s reservation ofers satisfy all of the providers’ reservation requirements and allow the negotiation process to succeed. We choose sets of global constraints corresponding to diferent values of $\alpha ^ { \prime }$ such that $\alpha ^ { \prime } \geq 1$

For each value of $\alpha ^ { \prime } ,$ the experiment is repeated 40 times, randomly varying the coeficients $v _ { i } ^ { P }$ of the concession tactics for the providers. For the experiments where the providers’ preferences are partially known, we randomly identify the set of providers whose preferences are known. The average over the 40 runs is calculated for all of the metrics that measure the negotiation outcome.

## 6.3. Comparing the Base Approach with the Benchmarks

Figure 3 shows the negotiation success rates achieved by the three approaches, Global\_RV\_Bench, Component \_RV\_Bench, and Fixed\_RV\_Proposed. Given that Global\_RV\_Bench does not consider the providers’ information, the same negotiation result is obtained when the broker has no, partial, or full preference information. We find the two benchmarks Global\_RV\_Bench and Component\_RV\_Bench achieve practically the same success rate for all of the experiments.

Our base approach achieves better success rates than the benchmarks for all experiments except one. When the broker has no information about the providers’ preferences and the composite service is relatively small (10 components only), the performances of all three approaches are practically the same. When the composite service becomes more complex $( \mathrm { e . g . }$ when n is 20 or 30), then even if the broker has no information about the providers’ preferences, the base approach is able to identify more discriminating reservation values for several of the component services, often by improving the reservation values from weak Paretooptimal solutions to strong Pareto-optimal ones. After such improvements, the best utilities some providers can obtain increase, which makes it possible for those providers, who otherwise may not accept any ofers, to reach agreements with the broker. When the broker has partial or full information of providers’ preferences, our base approach outperforms the two benchmarks even for small composite services—the more information the broker has, the greater the improvement achieved by our approach.

Figure 4 shows the utility of the composite service to the user and the average utility to the providers achieved by the three approaches. The second benchmark (Component\_RV\_Bench) outperforms the first benchmark (Global\_RV\_Bench) when the broker has partial or full preference information. This is because Component\_RV\_Bench uses a similarity-based approach in the bilateral negotiation process that can increase the utility for both the broker and the provider. When there is no information available to the broker, there is no diference in the performance of the two benchmarks.

Our base method outperforms both benchmarks in terms of utility of the composite service and the average utility obtained by providers for all problem sizes and all levels of providers’ information. The more information the broker has, the higher the improvement. We note that even when the broker has no information about the service providers’ preferences, the broker can still achieve a higher utility for the composite service using our approach. Relaxing the reservation values from weak Pareto-optimal solutions to strong ones allows the broker to ofer more on some attributes to providers without afecting the utility of the composite service to the user. Thus, the broker can achieve an agreement by conceding less overall, resulting in a higher utility for the composite service as compared to the benchmarks. For the same reason, our approach also brings more benefits to the providers without adversely afecting the user.

## 6.4. Comparing the Dynamic Adjustment Approach with the Base Approach

Figure 5 compares the negotiation success rates for the dynamic adjustment approach when compared with the base approach. As is evident from the figure, the dynamic adjustment approach handily outperforms the base approach regardless of how much information the broker has regarding the providers’ preferences. The potential flexibility provided by negotiation sessions that conclude successfully early in the process is not exploited by the base approach to relax the reservation values for ongoing negotiation sessions, leading to the lower success rate for the base approach.

Figure 3. (Color online) The Success Rates for the Base Approach and the Benchmarks  
![](/api/attachments/FPZQHQ5A/fulltext/images/35b1e99e04d52b8d42f5b0347d0c3f8f4a6516875f962247f8071b8d68a3ffc7.jpg)  
Global\_RV\_Bench Component\_RV\_Bench Fixed\_RV\_Proposed

Figure 6 shows the utility of the composite service and the average utility of the providers achieved using the two approaches. When the base approach is able to reach a successful outcome, it usually provides higher utility to the user. This is because the additional relaxations of the reservation values for some providers in the dynamic approach can reduce the utility the broker can obtain; of course this comes in exchange for a higher success rate. Furthermore, the average utility achieved by the providers is higher for the dynamic approach; these relaxed reservation values help the providers of those component services obtain higher utilities.

In summary, we find that dynamically adjusting reservation values considerably increases the chance of successful negotiations, especially when the global constraints are stringent. When the global constraints are not very tight, then the dynamic adjustment approach could result in solutions with lower utility of the composite service. In such situations, the broker (or the user) has to decide whether the increased risk of negotiation failure compensates for a higher utility.

## 6.5. Comparing the Median Approximation Approach with the Base Approach for Partial Preference Information Scenarios

The base approach is a conservative one in that when negotiating with providers whose preferences are not known it attempts to determine the reservation values

CS\_Utility\_Global\_RV\_Bench CS\_Utility\_Component\_RV\_Bench CS\_Utility\_Fixed\_RV\_Proposed

Figure 4. (Color online) The Utilities Achieved Under the Base Approach and the Benchmarks  
![](/api/attachments/FPZQHQ5A/fulltext/images/10e78735d24278257f693440a28608c16fcf659028b0ff244c86759da56553a2.jpg)  
Provider\_Utility\_Global\_RV\_Bench Provider\_Utility\_Component\_RV\_Bench Provider\_Utility\_Fixed\_RV\_Proposed

for each attribute separately and equitably to increase the probability of success. Consequently, the approach does not consider any trade-of across the attribute values for such providers either when determining the reservation values or subsequently while negotiating. When preference weights for some providers are known, a less conservative approach could be to approximate the preference weights for the remaining providers based on these known preferences. We conduct experiments where the median of the known preferences are used to approximate the unknown ones (experiments where the mean was used led to qualitatively similar results). Since the results were very similar when the composite service had 10, 20, and 30 component services (i.e., n <sup></sup> 10, 20, or 30), we only report the results for n <sup></sup> 20.

Figure 7 shows the performance of the median approximation relative to the base approach. From the figure we see that when $\alpha ^ { \prime }$ is very low, neither approach is able to negotiate successfully—this corresponds to situations where the global constraints are too stringent to have any realistic chance of successful negotiations. Thereafter, for a small range of α <sup>(</sup>1.12 < $\alpha ^ { \prime } < 1 . 1 7 )$ , the median approximation approach is able to negotiate successfully in a handful of the 40 experiments, while the base approach is not. This is surprising at first glance, since the base approach is more conservative and we expect it to have a higher chance of negotiating successfully. On further examination, we find that for this range of $\alpha ^ { \prime }$ , the negotiations typically fail because of a lack of successful convergence with only a few providers. However, for some of the problem instances, the median approximation can become quite close to the true preferences (that are unknown to the broker) for enough of the providers such that the negotiation using these approximations are close to what would have occurred if the preferences were known—this leads to successful negotiations for those problem instances. When $\alpha ^ { \prime }$ is relatively higher $( \alpha ^ { \prime } >$ 1.17), the base approach does achieve a higher success rate than the median weight approach as expected. Eventually, the global constraints become suficiently loose such that both approaches are able to negotiate successfully with every provider in all 40 experiments.

Figure 5. (Color online) The Success Rates from Using the Base Approach and the Dynamic Adjustment Approach  
![](/api/attachments/FPZQHQ5A/fulltext/images/34047e72d871fa438be56ee97a63f629d8089cc64dac3f28de1b3e87314e7eee.jpg)

The median approximation approach achieves a slightly higher utility than the base approach for both the users and the providers when the negotiations are successful. When the median approximation results in preference weights that are close to a provider’s true preference weights, the negotiation outcome for such a provider is similar to when the provider’s preference information is available. For such providers, the eventual solution leads to higher utilities for not only the provider but the broker as well (as observed in Figure 4). When the approximation is quite diferent from the true preference weights, the derived reservation values of the broker could lead to provider preferabilities that are quite far from the preferabilities when the true preference weights of the provider are known to the broker. When this is in favor of the provider, not only is the negotiation between the broker and such a provider guaranteed to be successful, the eventual outcome can generate more utility for the provider and the broker (since the final negotiation outcome could

![](/api/attachments/FPZQHQ5A/fulltext/images/e51e31064d6ed798e777d9d37ef7e889b82df101e83c6a5c97c9e04b55102134.jpg)

Figure 6. (Color online) The Utilities Achieved Under the Base and the Dynamic Adjustment Approaches

CS\_Utility\_Fixed\_RV\_Proposed CS\_Utility\_Dynamic\_RV\_Proposed Provider\_Utility\_Fixed\_RV\_Proposed Provider\_Utility\_Dynamic\_RV\_Proposed lead to a solution that is somewhere in between as far as the preferabilities are considered). When this is not in favor of the provider, in some cases this can lead to unsuccessful negotiations, and therefore such problem instances do not get factored in the calculation of average utilities. As a result of all of this, when the negotiations are successful, the median approximation approach leads to slightly higher utilities on average than the proposed approach.

![](/api/attachments/FPZQHQ5A/fulltext/images/18cb4bae36dbb400d19b93638e94e9932f19a5457e6bd6b900fc8659c16881b4.jpg)

Figure 7. (Color online) The Success Rate and Utilities Achieved Under the Base and Median Weight Approaches  
![](/api/attachments/FPZQHQ5A/fulltext/images/19c83534cd8639f5a25d49d3f87c8a8106a0385dfeaf7a1c01e10fa987d0dc42.jpg)

![](/api/attachments/FPZQHQ5A/fulltext/images/44c6063d25c2b432f3d8980dfd06972ae9e5b29d8f69b00b1092f6356dc090e1.jpg)

## 7. Conclusions

## 7.1. Contributions of Our Work

There exist several technical and economic challenges to the future growth of software services. While research on such services has only started recently in the IS community (Bardhan et al. 2010), the authors explicitly call on the IS community to conduct research on enterprise application modeling and component integration. Our research makes an important contribution in the area of component integration in general, and service level agreement negotiation in particular. The paper presents a novel method to help a service broker determine the reservation values to use for each component service when negotiating with a group of providers to compose value-added services from existing software services. Our contributions are fivefold. First, the method proposed in this paper is the first efort to formulate the problem of determining the reservation values for each component service to maximize the chance of reaching a successful negotiation outcome based on a user’s requirements for a composite service. The problem is a challenging one because component services can be constructed into a composite service through diferent composition structures, and negotiating down a unit of one attribute for a component service could impact the ability to negotiate on attributes for other component services in diferent ways depending on the structure. We show how the max-min approach and ε-constraint method can be used to transform the multiobjective optimization formulations for determining the reservation values for several component services into a single linear program; when the transformation leads to weak Paretooptimal solutions, we show how the solutions can be improved to strong Pareto optimality.

Second, when the providers’ preferences are available, our method utilizes this information to generate reservation values and ofers that are more likely to lead to successful negotiation outcomes. Third, we identify several problem instances for which there exist closed-form solutions for the reservation values. Fourth, we show how the proposed approach can be incorporated in existing negotiation processes and reservation values can be changed dynamically in the course of negotiation; this further improves the likelihood of successful negotiation. Finally, our proposed method of setting reservation values can help reduce deadlocks through avoiding unnecessarily stringent reservation values for attributes of component services. Our experiments demonstrate that the proposed method outperforms two viable benchmarks on all relevant dimensions under practically all conditions. We should emphasize that the proposed method to determine reservation values is quite general and is applicable regardless of other aspects of the negotiation process, e.g., agents’ concession tactics, trade-of tactics, preference learning, approximation mechanisms, etc.

## 7.2. Implications for Research

In this study, we have assumed that a service broker knows which provider to negotiate with for each component service. How to identify service providers for the purpose of negotiation is a problem that needs further investigation. The problem becomes more complex if some service providers ofer bundled services. In addition, we only consider the situation where the broker negotiates with one provider for each component service. Another interesting extension would be to determine appropriate reservation values where the broker negotiates with multiple providers simultaneously for each component service. Furthermore, we have not considered the contracting issues between the user and the broker if the broker negotiates on behalf of the user. It would be interesting to study how diferent contracts could afect the negotiation process between the broker and the providers.

We have considered a negotiation process that works concurrently with multiple service providers as that model is more time eficient than a sequential model for service composition in real time (Nguyen and Jennings 2005). In environments where a sequential model is applicable, the sequence in which a broker negotiates with diferent providers can impact the negotiation outcome. Determining the best sequence to conduct negotiations could be an interesting research problem. In addition, we have assumed that the negotiation attributes take on continuous values. If some of the attributes were discrete valued, then the problem formulation would be a mixed-integer program. Determining eficient methods to solve such formulations is another viable direction for future research. Finally, it would be interesting to investigate how the ability to negotiate in a service marketplace impacts the participation of providers and users in such platforms. Our findings suggest that when providers’ preference weights are known to the broker, both users and providers are better of. At the same time, providers may not be comfortable in publicly revealing their preferences, especially when there are multiple providers competing to deliver the same functionality. Future research could examine information sharing mechanisms that facilitate negotiations while also protecting the providers’ private information in a service marketplace.

## 7.3. Implications for Practice

The adoption of service-centric computing is considered pivotal for the 21st century enterprises (SOA Consortium 2010). The methods proposed in this research can improve the efectiveness of automated negotiation when developing new value-added services, thus injecting more flexibility to the development of software services. A naïve approach for setting reservation values for component services can severely impact a firm’s ability to negotiate successfully. The improved ability to conduct successful negotiations using our method reduces the frictional costs associated with implementing such services and will help accelerate the growth of these kinds of markets.

We have assumed that a broker negotiates with the diferent providers on behalf of the user. If the user is aware of the structure of the composite service and knows the appropriate providers to negotiate with, the user could directly negotiate with the providers. The procedure to determine the reservation values will remain the same. However, it is less likely that the user will know the providers’ preferences without the help of a broker. As shown in our study, if the broker has more information about providers’ preferences, the utilities of the user and the providers are both improved. Therefore, if the user wishes to conduct the negotiations, the user should make eforts to understand (learn) the preferences of the providers to improve the chance of successful negotiations.

We have also assumed that the user can specify the QoS requirements for a composite service in an accurate manner. This can be a challenge in practice, particularly if the composite service being considered is a completely novel one. The user must evaluate the role of the service in the context of the firms’ larger business goals, and determine the QoS parameters (global constraints) that would make the service worth implementing. If the global constraints cannot be met with the minimum possible attribute values available for each component, then there is no chance of negotiation success. On the other hand, if the global constraints can be met with the listed ofers for each component, then success is guaranteed. The broker can assist the user in determining global constraints that have a reasonable chance of negotiation success based on such an analysis.

We have shown that dynamically adjusting the reservation values may be desirable even though that can reduce the utility of the composite service to the user. Moreover, when only some providers’ preference information are known, our experiments show that approximating the preference of other providers (whose preferences are not known) could lead to increased utility for the user, while possibly decreasing the chance of negotiation success. Thus, a firm needs to balance the risk of negotiation failure with the expected utility of the composite service when considering adopting the dynamic adjustment method or other aggressive negotiation strategies.

Finally, while we have assumed each task in a composite service is performed by a diferent software service, it is possible that multiple tasks in the composite service are performed by the same software service. In such a case, if the multiple tasks can be cleanly encapsulated as a distinct subprocess, then the subprocess should be considered as one distinct component service for negotiation. If such an encapsulation is not possible, the QoS parameters for each task would need to be negotiated independently to meet the QoS requirement for the entire composite service.

## Appendix. Procedure

## Negotiation\_For\_Service\_Composition

Symbols X and Y denote the set of numbers indexing the negotiation sessions that end successfully and unsuccessfully, respectively, and X and Y satisfy $\bar { X } \cup Y = \{ 1 , \dotsc , n \}$ $t _ { i , \operatorname* { m a x } } ^ { B }$ is the predefined maximum number of iterations.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
2 Determine reservation values for all component services; //Section 4
3 Initialization: $t \leftarrow 0$; $X \leftarrow \emptyset$; $Y \leftarrow \{1, \ldots, n\}$; STOP $\leftarrow$ false; updateRV $\leftarrow$ false;
4 while $t &lt; t_{i,\max}^{B}$ and not(STOP) do
5 for each $j \in Y$ do
6 generate an offer for session $j$ by using the concession tactic; //Section 5.1
7 if provider $j$'s preference is available then
8 find the offer most preferable to provider $j$; //Section 5.2
9 send the offer to provider $j$;
10 if an offer is acceptable to both the broker and provider $j$ then
11 $X \leftarrow X \cup \{j\}$; $Y \leftarrow Y - \{j\}$; updateRV $\leftarrow$ true;
12 endif
13 endfor
14 $t \leftarrow t + 1$
15 if $Y = \emptyset$ then
16 STOP $\leftarrow$ true;
17 else if updateRV = true then
18 update the reservation values for any session $j \in Y$; //Section 5.3
19 updateRV $\leftarrow$ false;
20 endif
21 endif
22 endwhile
23 if $Y = \emptyset$ then
24 return Success; //The broker has successfully obtained the composite service
25 else
26 return Failure; //The broker has failed to obtain the composite service
27 endif.
</div>

## Endnotes

<sup>1</sup> We use the terms price and cost interchangeably depending on the context.

<sup>2</sup> Providers’ preferences are more likely to be known when the user negotiates with the help of a service broker, since brokers learn providers’ preferences through previous negotiation experiences (Nielsen and Jensen 2004, Bufett and Spencer 2007). We consider the broker as a surrogate for the user and ignore any contracting issues between the broker and the user.

<sup>3</sup> Data quality is defined as the ratio of the amount of data produced correctly relative to the total amount of data produced (Ardagna and Pernici 2007, Pernici 2006).

<sup>4</sup> If a broker negotiates on behalf of the user, the user does not benefit from misrepresenting her global constraints to the broker. This is because the broker, to ensure the negotiation outcome does not violate these constraints, must use them (otherwise unwarranted negotiation failures may occur). Consequently, misrepresentation only hurts the user.

<sup>5</sup> As discussed in Section 2, the listed ofers for each QoS attribute and the corresponding minimum and maximum values could be obtained from service registries (Ran 2003, Al-Masri and Mahmoud 2007).

<sup>6</sup> If the negotiation with a provider fails, the broker can select another provider who ofers the service with the same functionality and restart the negotiation process with the revised set of providers.

<sup>7</sup> We use the term preferability for comparing both pairs of attribute values as well as pairs of ofers; the usage is generally unambiguous given the context.

<sup>8</sup> The Pareto-optimal solutions for the reservation values using the multiobjective optimization formulations are diferent from Paretooptimal solutions for negotiation outcomes as commonly discussed in the negotiation literature. In the former, the goal is to obtain solutions (reservation values in our problem) such that an additional relaxation to any of the reservation values would lead to violating some constraint. The latter refers to ofers that cannot be changed to make one participant better of without making any other participants worse of (Rubinstein 1982).

<sup>9</sup> We note that the proposed method of determining reservation values would work even if the negotiations with the providers were conducted sequentially.

<sup>10</sup> The providers set their private reservation values based on their understanding of the market for their service, their operating costs, and previous negotiation experience.

<sup>11</sup> The preferences of the user will typically not be known to the providers. First, if a provider is negotiating with a broker, the provider may not know the identity of the user. In addition, the provider may not be aware of the full functionality of the composite service. We note that the problem formulations do not change even if a provider does know the user’s preferences.

<sup>12</sup> We have chosen these four attributes because they correspond to the four important aggregation functions recognized in the literature (Zeng et al. 2004, Pernici 2006, Yu et al. 2007). Details are provided in Table 1.

<sup>13</sup> By varying the number of activities and subroutes, we have varied both the activity complexity and control-flow complexity, which are two important ways of measuring the complexity of workflow-based composite services (Cardoso 2006).

<sup>14</sup> The QoS attribute-values are randomly varied to cover a wide range of real-world scenarios.

<sup>15</sup> The deadlines for the broker and the providers are set to be the same so that the broker and providers can concede to their reservation ofers at the same time. Using diferent deadlines for the broker and the providers would not afect the qualitative nature of our findings.

## References

Al-Masri E, Mahmoud QH (2007) QoS-based discovery and ranking of Web services. Proc. 16th Internat. Conf. Comput. Comm. Networks (IEEE, Washington, DC), 529–534.

Ardagna D, Pernici B (2007) Adaptive service composition in flexible processes. IEEE Trans. Software Engrg. 33(6):369–384.

Bardhan IR, Demirkan H, Kannan PK, Kaufman RJ, Sougstad R (2010) An interdisciplinary perspective on IT services management and service science. J. Management Inform. Systems 26(4): 13–64.

Bi HH, Zhao JL (2004) Applying propositional logic to workflow verification. Inform. Tech. Management 5(3–4):293–318.

Bufett S, Spencer B (2007) A Bayesian classifier for learning opponents’ preferences in multi-object automated negotiation. Electronic Commerce Res. Appl. 6(3):274–284.

Cardoso J (2006) Approaches to compute workflow complexity. Leymann F, Reisig W, Thatte SR, van der Aalst W, eds. Dagstuhl Seminar: The Role of Bus. Processes Service Oriented Architectures, 1–15.

Chalouf MA, Krief F (2009) SSLNP: Secure service level negotiation protocol. Proc. Second Internat. Conf. Global Inform. Infrastructure Sympos. (IEEE, Piscataway, NJ), 1–4.

Chalouf MA, Mbarek N, Krief F (2011) Quality of service and security negotiation for autonomous management of next generation networks. Network Protocols Algorithms 3(2):54–86.

Chalouf MA, Djama I, Ahmed T, Krief F (2012) An end-to-end QoS and security joint management for IPTV service delivery. Internat. J. Autonomous Adaptive Comm. Systems 5(4):398–416.

Chatterjee K, Samuelson L (1988) Bargaining under two-sided incomplete information: The unrestricted ofers case. Oper. Res. 36(4):605–618.

Cheng CB, Chan HCC, Lin KC (2006) Intelligent agents for e-marketplace: Negotiation with issue trade-ofs by fuzzy inference systems. Decision Support Systems 42(2):626–638.

Clark KP, Warnier ME, Brazier FMT, Quillinan TB (2010) Secure monitoring of service level agreements. O’Conner L, ed. Internat. Conf. Availability, Reliability Security (IEEE, Piscataway, NJ), 454–461.

Comuzzi M, Pernici B (2009) A framework for QoS-based Web service contracting. ACM Trans. Web 3(3):Article 10.

Elfatatry A, Layzell P (2004) Negotiating in service-oriented environments. Comm. ACM 47(8):103–108.

Faratin P, Sierra C, Jennings NR (1998) Negotiation decision functions for autonomous agents. J. Robotics Autonomous Systems 24(3–4):159–182.

Faratin S, Sierra C, Jennings NR (2002) Using similarity criteria to make trade-ofs in automated negotiations. Artificial Intelligence 142:205–237.

Gatti N, Di Giunta F, Marino S (2008) Alternating-ofers bargaining with one-sided uncertain deadlines: An eficient algorithm. Artificial Intelligence 172:1119–1157.

Jennings NR, Faratin P, Lomuscio AR, Parsons S, Sierra C, Wooldridge M (2001) Automated negotiation: Prospects, methods and challenges. Group Decision Negotiation 10:199–215.

Koistinen J, Seetharaman A (1998) Worth-based multi-category quality-of-service negotiation. Second Internat. Enterprise Distributed Object Comput. Workshop (IEEE, Piscataway, NJ), 239–249.

Lee S-I, Kang S-G (2012) NGSON: Features, state of the art, and realization. IEEE Comm. Magazine 50(1):54–61.

Leitner P, Hummer W, Dustdar S (2013) Cost-based optimization of service compositions. IEEE Trans. Services Comput. 6(2):239–251.

Liu Y, Ngu AH, Zeng LZ (2004) QoS computation and policing in dynamic Web service selection. Proc. 13th Internat. World Wide Web Conf. Alternate Track Papers Posters (ACM, New York), 66–73.

Lock R (2006) Automated negotiation for service contracts. Ceballos S, ed. Proc. 30th Annual Internat. Comput. Software Appl. Conf., Vol. 2 (IEEE, Piscataway, NJ), 127–134.

Ludwig H, Keller A, Dan A, King RP, Frank R (2003) Web Service Level Agreements (WSLA) Language Specification. IBM, http:// www.research.ibm.com/wsla/WSLASpecV1-20030128.pdf.

Mbarek N, Krief F, Negru D (2008) SLNP usage for QoS negotiation in heterogeneous environments. IEEE/ACS Internat. Conf. Comput. Systems Appl. (IEEE, Piscataway, NJ), 958–963.

Menasce DA (2002) QoS issues in Web services. IEEE Internet Comput. 6(6):72–75.

Miettinen K (1999) Nonlinear Multiobjective Optimization (Kluwer, Boston).

Miles R, Hamilton K (2006) Learning UML 2.0 (O’Reilly Media, Sebastopol, CA).

Napoli CD (2009) Software agents to enable service composition through negotiation. Knowledge Processing Decision Making Agent-Based Systems 170:275–296.

Nguyen TD, Jennings NR (2005) Managing commitments in multiple concurrent negotiations. Electronic Commerce Res. Appl. 4(4): 362–376.

Nielsen TD, Jensen FV (2004) Learning a decision maker’s utility function from (possibly) inconsistent behavior. Artificial Intelligence 160(1–2):53–78.

Padberg M (1999) Linear Optimization and Extensions, 2nd ed. (Springer, Heidelberg, Germany).

Paurobally S, Tamma V, Wooldrdige M (2007) A framework for Web service negotiation. ACM Trans. Autonomous Adaptive Systems 2(4):Article 14.

Paurobally S, Turner PJ, Jennings NR (2003) Automating negotiation for m-services. IEEE Trans. Systems, Man, Cybernetics—Part A 33(6):709–724.

Pernici B (2006) Mobile Information Systems: Infrastructure and Design for Adaptivity and Flexibility (Springer, Berlin).

Raifa H (1982) The Art and Science of Negotiation (Harvard University Press, Cambridge MA).

Ran S (2003) A model for Web services discovery with QoS. ACM SIGecom Exchanges 4(1):1–10.

Rana O, Warnier M, Quillinan TB, Brazier F (2008) Monitoring and reputation mechanisms for service level agreements. Altmann J, Neumann D, Fahringer T, eds. Proc. 5th Internat. Workshop Grid Econom. Bus. Models (Springer-Verlag, Berlin Heidelberg), 125–139.

Rubinstein A (1982) Perfect equilibrium in a bargaining model. Econometrica 51(1):97–109.

Sarangan V, Chen J-C (2006) Comparative study of protocols for dynamic service negotiation in the next-generation Internet. IEEE Comm. Magazine 44(3):151–156.

SOA Consortium (2010) http://www.soa-consortium.com/.

Sun SX, Zhao JL, Nunamaker JF, Sheng OR (2006) Formulating the data flow perspective for business process management. Inform. Systems Res. 17(4):374–391.

van der Aalst WMP (2003) Don’t go with the flow: Web services composition standards exposed. IEEE Intelligent Systems 18(1): 72–76.

van Moorsel A (2001) Metrics for the Internet age: Quality of experience and quality of business. Technical Report HPL-2001-179, HP Labs, Palo Alto, CA.

Vanderbei RJ (2008) Linear Programming: Foundations and Extensions, Third ed. (Springer-Verlag, New York).

Waeldrich O, Battré D, Brazier F, Clark K, Oey M, Papaspyrou A, Wieder P, Ziegler W (2011) WS-Agreement Negotiation Version 1.0. http://www.ogf.org/Public\_Comment\_Docs/Documents/ 2011-03/WS-Agreement-Negotiation<sup>+</sup>v1.0.pdf.

Wagner M, Kellerer W (2004) Web services selection for distributed composition of multimedia content. Proc. 12th Annual ACM Internat. Conf. Multimedia (ACM, New York), 104–107.

Wohed P, van der Aalst WMP, Dumas M, ter Hofstede AHM (2003) Analysis of Web services composition languages: The case of BPEL4WS. Song IY, Liddle SW, Ling TW, Scheuermann P, eds. Conceptual Modeling–ER 2003, Lecture Notes Comput. Sci., Vol. 2813 (Springer, Berlin Heidelberg), 200–215.

Yu T, Zhang Y, Lin K-J (2007) Eficient algorithms for Web services selection with end-to-end QoS constraints. ACM Trans. Web 1(1):Article 6.

Zeng L, Benatallah B, Dumas M, Kalagnamam J, Chang H (2004) QoS-aware middleware for Web services composition. IEEE Trans. Software Engrg. 30(5):311–327.

Zhao JL, Tanniru M, Zhang LJ (2007) Services computing as the foundation of enterprise agility: Overview of recent advances and introduction to the special issue. Inform. Systems Frontiers 9(1): 1–8.

Zhao JL, Goul M, Purao S, Vitharana P, Wang HJ (2008) Impact of service centric computing on business and education. Comm. AIS 22:Article 16.

Zheng Z, Lyu MR (2013) Selecting an optimal fault tolerance strategy for reliable service-oriented systems with local and global constraints. IEEE Trans. Comput. 64(1):219–232.

Zimmermann H-J (1987) Fuzzy Sets, Decision Making and Expert Systems (Kluwer Academic Publishers, Boston).
