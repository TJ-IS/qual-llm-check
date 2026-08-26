---
otero_id: 13170
otero_key: "3JJRXXEF"
title: "Workflow composition of service level agreements for web services"
authors: "M. Brian Blake; David J. Cummings; Ajay Bansal; Srividya Kona Bansal"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.01.017"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Work<sup>fl</sup>ow composition of service level agreements for web services

M. Brian Blake <sup>a,</sup>⁎, David J. Cummings <sup>b</sup>, Ajay Bansal <sup>c</sup>, Srividya Kona Bansal <sup>c</sup>

<sup>a</sup> Department of Computer Science and Engineering, University of Notre Dame, Notre Dame, IN, United States

<sup>b</sup> Department of Computer Science, Stanford University, United States

<sup>c</sup> Department of Engineering, Arizona State University, United State

## a r t i c l e i n f o

Article history: Received 19 July 2010 Received in revised form 22 December 2011 Accepted 30 January 2012 Available online 8 February 2012

Keywords: Service level agreements Quality of service Web services Service-oriented computing

## a b s t r a c t

Service-oriented architecture enables an environment where businesses can expose services for use by their collaborators and their peer organizations. In this dynamic environment, organizations require the use of service level agreements (SLAs) to assure the quality of service (QoS) standards of services provided by their collaborators. In an ad-hoc work<sup>fl</sup>ow scenario, a business may need to perform real-time composition of existing services in response to consumer requests. In this work, we suggest that, in parallel to traditional web service composition, the business must also compose the existing SLAs in order to ensure the service levels that must be guaranteed to new consumers. Ultimately, this approach to SLA composition must align with the overarching principles of the provider and the priorities of the consumer. In this paper, we introduce a model and representations of service level agreement attributes appropriate for managing a service provider's expectations when adding new partners. Our evaluations suggest that the SLA composition can ef<sup>fi</sup>ciently run concurrently with traditional service composition.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

A service level agreement, SLA, is a technical contract between two types of businesses, producers and consumers. A SLA captures the agreed-upon terms between organizations with respect to quality of service (QoS) and other related concerns. In simple cases, one consumer forms a SLA with a producer. In more complex cases, a consumer may form a SLA that de<sup>fi</sup>nes a set of producer businesses. Considering a service-oriented computing environment, capabilities are shared via the implementation of web services exposed by a producer organization. The ultimate goal of service-oriented computing is for consumers to access these shared capabilities on-demand. As such, in cases where businesses have longstanding relationships, such as work<sup>fl</sup>ow and supply chain environments, peer companies that share services must be able to assure a level of service to their underlying customers [4,8].

New speci<sup>fi</sup>cations, such as the Web Service Level Agreement (WSLA) and Web Service Agreement (WS-Agreement) [2] enable SLAs to be associated with an individual web service or even groups of web services. These speci<sup>fi</sup>cations de<sup>fi</sup>ne an eXtensible Markup Language (XML)- based data model that can be used along with the Web Service Description Language (WSDL) documents that traditionally describe the web services. These speci<sup>fi</sup>cations provide a signi<sup>fi</sup>cant opportunity.

Organizations can specify QoS-related concerns in concert with the functionality concerns already captured in the WSDL <sup>fi</sup>les. As a result, when a new organization searches for a pertinent web service, the SLA-enhanced WSDL <sup>fi</sup>le can be used to determine the appropriateness of the service to meet the required business need. Furthermore organizations can use the SLA-enhanced WSDL <sup>fi</sup>le to negotiate the QoS terms.

Although these SLA technologies and speci<sup>fi</sup>cations present new opportunities for service-oriented business processes, there are a number of signi<sup>fi</sup>cant barriers. When a consumer organization must create a new business capability that requires the work<sup>fl</sup>ow composition of multiple web services, then that organization will also need to understand the composite impact of the underlying SLAs. Consequently, in addition to composing web services that are functionally compatible, the organization will need to ensure that the web services are compatible with regard to their service levels. Also, the product of all the SLAs for a composition of web services must be within the required threshold of feasibility as de<sup>fi</sup>ned by the end users. As the service-oriented computing paradigm increases in popularity, the consumer will have the option of many similar services that may meet a particular requirement. As such, the composition of web services that is most ef<sup>fi</sup>cient for a particular business purpose will rest on the organization's ability to understand and optimize the corresponding composition of SLAs.

To deal with the aforementioned issues, we introduce the phrase, workflow composition of SLAs. Our approach suggests the multidimensional evaluation of existing agreed-upon QoS standards in order to predict the standards possible for the introduction of new agreements. While the notions of multi-dimensional analysis, optimization, dynamic programming are not new [9,10,12,17,35] in this work, we identify the speci<sup>fi</sup>c SLA-based attributes that allows for the introduction of new partners. Furthermore we develop a set of principles and the associated process that utilize the SLA information to estimate service levels. This approach favors services with clean request/response (RPC-type) communication, generally known as WSDL-based web services. Further investigation would be required to assess this approach as it relates to REST-based services [37].

In this work, we investigate several research issues relevant to the integration of web services-based work<sup>fl</sup>ow:

1. What SLA measures and principles are appropriate to support QoSbased assessment of existing service level guarantees?

2. Given a group of SLAs and knowledge about current consumer service level needs, can an on-demand request be analyzed against existing SLAs to guarantee a certain service level for a new consumer?

The paper proceeds in the following section with a discussion of related work. In Section 3, we discuss how the SLA-based QoS assessment values are derived from higher-level organizational principles. The formal details of the attributes are de<sup>fi</sup>ned in Section 4, and how the attributes are physically captured in markup languages in shown in Section 5. Finally, in Section 6 we evaluate the performance SLA composition as it runs parallel with traditional service composition routines.

## 2. Related work

There are many related projects that investigate the general use of SLAs for web services [18]. Some projects characterize SLA approaches to speci<sup>fi</sup>c domains, such as military, database management, or information systems [13,20,26,29]. There is also a large body of work that attempts to automate the management and negotiation of SLAs [11,16,23,27,33]. Other work attempts to use semantics to automate the negotiation of SLAs [15,25].

Our work leverages markup language (i.e. WS-Agreements) for providing SLA measures as in other studies [1,28,30]. All related work describes the importance of composing SLAs. In [28], their emphasis is on compatibility between user requirements and provider constraints. Their approach suggests a promising model-based approach to assuring the compatibility.

Our work is closely related to the comprehensive work performed by [9,10,35]. Each of these approaches investigates the QoS-based and constrained composition of web services. Although Canfora et al. [9] has an elegant approach that allows for the insertion and aggregation of any user-de<sup>fi</sup>ned QoS attribute, our approach identi<sup>fi</sup>es the speci<sup>fi</sup>c SLA measures that support the user-driven assessment of an environment where their SLAs dictate current system state. Table 1 shows a survey of SLA attributes and how they are exploited in related projects speci<sup>fi</sup>cally in the service-oriented computing domain.

Our work can be loosely classi<sup>fi</sup>ed in the body of work that looks to automate the aggregation of QoS attributes [14,21,24,32]. The uniqueness of our approach is that we consider the impacts when new web service work<sup>fl</sup>ows must be added as they affect the existing operational SLAs. More speci<sup>fi</sup>cally, if a composite capability overlaps multiple SLAs, then the characteristics of an early SLA can impact a later SLA in the composition routine. Canfora et al., Cardoso et al., Zeng et al., [9,10,35] concentrate on deriving a speci<sup>fi</sup>c composition routine as constrained by QoS values. Canfora et al., Zhang et al., and Yu et al. focus on iterative multiattribute utility approaches [12] where to focus is on the overall optimization function and less on the details of each of the attribute. Our work attempts to consider both consumer and producer concerns when assessing the entry of a new work<sup>fl</sup>ow. As such, our work contains low-level details for each service level objective such that subsequent optimization approaches use them as a model for optimization that targets each attribute at a low-level. Although [22] has a similar approach where SLAs are aggregated formally, they do not consider consumer and producer services independently as in our work.

In summary, we de<sup>fi</sup>ne speci<sup>fi</sup>c SLA measures and formally integrate measures across multiple SLAs. We also de<sup>fi</sup>ne a principled process for the composition of SLAs. This work extends related work [6] by concentrating on SLA measures in markup language <sup>fi</sup>les as opposed to Uni<sup>fi</sup>ed Modeling Language (UML) models. Unlike other work in QoS-based web service composition, we attempt to classify QoS attributes by those associated with the provider and those associated with the consumer. Another variation here is the introduction of several high-level criteria that can be used to characterize organizations. We believe that by aggregating all lower-level attributes into a smaller set of higher-level criteria then organizations can be quantitatively evaluated or scored. Further evaluation in this paper justi<sup>fi</sup>es that such on-demand assessment of SLAs performs feasibly in an operational environment where very large numbers of web service work<sup>fl</sup>ows exist.

## 3. Assessing an enterprise based on its SLAs

The typical SLA has a large number of measures and criteria. However, in this work, we attempt to choose the measures that are most closely aligned to aggregation of a group of SLAs and ultimately their assessment. In the operational notion of web service composition, a basic web services work<sup>fl</sup>ow system must ensure that the input information supplied by the consumer ultimately leads to the required actions and outputs required by that consumer. In parallel, the work<sup>fl</sup>ow management system must ensure that the predicates and requisites match (either by syntactical or semantic techniques) in each step of the work<sup>fl</sup>ow. It is the operational composition routines that motivate the set of SLA attributes relevant to our work.

In order to designate which attributes that are most relevant to our proposed innovation, we developed a set of principles important to managing the quality of an enterprise with many business processes. The three relevant principles are Compliance (Suitability),

Survey of research projects that consider SLA attributes for web services.

<table><tr><td>Author names</td><td>Run time</td><td>Reputation</td><td>Uptime (Avail)</td><td>Resp time ***</td><td>Negotiation (rebinding)</td><td>Cost (price)</td><td>Success rate/ reliability</td><td>Problem resolution</td><td>Maintenance</td></tr><tr><td>(Blake et al.) [7] and this paper</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr><tr><td>(Canfora et al.) [9]</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr><tr><td>(Yu et al.) [34] Zhang et al.) [36] **</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(Zeng et al.) [35]</td><td></td><td>✓</td><td>✓</td><td>✓</td><td></td><td>✓</td><td>✓</td><td></td><td></td></tr><tr><td>(Cardoso et al.) [10]</td><td></td><td></td><td>✓</td><td>✓</td><td></td><td>✓</td><td>✓</td><td></td><td></td></tr><tr><td>(Jin et al.)[18]*</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td></td><td>✓</td><td>✓</td><td></td><td></td></tr><tr><td>(Mohabey et al.) [22]</td><td></td><td>✓</td><td>✓</td><td>✓</td><td></td><td>✓</td><td>✓</td><td></td><td></td></tr></table>

\* [18] list attributes, but do not develop formal approaches for composition.  
\*\* Although Canfora et al., Yu et al., and Zhang et al. do not formally de<sup>fi</sup>ne each attribute, their work focuses on an approach that allows any attribute to be aggregated within the composition routine.

Sustainability, and Resiliency. By correlating the QoS attributes to these principles, we have developed a list that is suitable for assessing an organization based on existing SLAs. The three principles (illustrated in Fig. 1 as a Uni<sup>fi</sup>ed Modeling Language class diagram) are de<sup>fi</sup>ned below in addition to their underlying SLA measures.

## 3.1. Compliance (suitability)

Compliance is the principle that ensures that the consumer receives the requested composite capability at the service level that is required. The functional notion of web service composition (as illustrated in Fig. 1) <sup>fi</sup>ts within this principle, since the consumer speci<sup>fi</sup>es their required outputs of the composition. Considering SLA terms, the composition process must assure that the aggregate cost, uptime, and run time are compliant with the user requirements. Cost is the sum total price of all services participating in the solution process. Uptime is a guarantee by the service providers that their services will be available a speci<sup>fi</sup>ed percentage of the time per day or month. Finally, run time is the time it takes to complete the process by adding the response times of each service in the composition.

## 3.2. Sustainability

Sustainability is the ability to maintain the underlying services in a timely fashion. Success rate, Negotiation/renegotiation, and problem resolution are related to ensuring the process continues to execute effectively. Success rate is de<sup>fi</sup>ned by the historical rate at which a provider successfully completes a request. A consumer will require assurance that a particular business is capable of agreeing on contract terms (i.e. negotiation/renegotiation) in a timely manner. Moreover, the result of a negotiation scheme might be the development of new agreement. In addition, the service providers must be capable of resolving highimpact problems (perhaps identi<sup>fi</sup>ed by the consumer) in a timely manner. Success rate, negotiation, and problem resolution times ensure that a consumer can meet the demands of their end users.

## 3.3. Resiliency

Resiliency is the principle of a service to perform at high service levels over an extended period of time. This principle was derived from our work with data-centric government transactional systems. The resiliency principle specializes many of the principles that underly the general notion of mean time between failures (MTBF) [3,31]. Low resiliency is represented by a service that is frequently taken off-line for maintenance. Additional, the frequency of updates may impede the predictability of its operation. Consumers will need adequate notice prior to maintenance downtimes. In addition, resiliency dictates a low frequency of maintenance downtime. Peer consumers may also add comments about a particular provider and thus create a quanti<sup>fi</sup>ed reputation. The reputation rating also in<sup>fl</sup>uences the resiliency of a service.

The model elements of our work were derived from our literature review and from work with collaborating stakeholders acknowledge in this paper. As such, we assume the validity of this model as the applicability of the work to other domains, in some sense, relies on these underlying elements. The paper proceeds with a formal de<sup>fi</sup>nition of all attributes relevant to aggregating and assessing a group of SLAs, and subsequently a description of how the information can be stored physically. The <sup>fi</sup>nal sections discuss the approach and performance for aggregating SLAs of many business processes.

## 4. Aggregating and assessing service level agreements

When assessing a group of web service work<sup>fl</sup>ows, the resulting assessment must be a result of the aggregated SLA terms of the underlying services. In some cases, aggregating the SLA terms is as straightforward as adding the measures of each of the dependent services, but in other cases the aggregate measure must be created based on consumer requirements. Since there may be subjectivity with respect to how the aforementioned SLA measures can be aggregated and calculated, we introduce the following formal concepts for composing the SLA measures in the context of web service composition.

## 4.1. Defining the physical entities for assessing SLAs

## De<sup>fi</sup>nition 1. Server

Composition in a service-oriented architecture involves a consumer collaborating with a producer. The mapping from service to resources (servers and computational units) must consider system boundaries (i.e. which servers are dedicated, which are not), the size of the messages and transactions, and initialization/set up costs. Here, we illustrate an over-simpli<sup>fi</sup>ed correlation of the services to the server. The capabilities of the producers and consumers are hosted on servers. Each server can be characterized by its performance, uptime percentage, throughput, and the pre-noti<sup>fi</sup>cation time, i.e., the server informing its constituents prior to any downtime associated with server enhancements and repairs. A server, v, can be formally de<sup>fi</sup>ned as a tuple of these SLA measures as shown below:

$$
v = \left(P e r f _ {v}, U p _ {v}, T i _ {v}, T o _ {v}, P r e N T _ {v}\right)\tag{1}
$$

where Perf is the performance of the server measured loosely in computations/second, $U p _ { \nu }$ is the uptime percentage of the server, $\mathrm { T i } _ { \mathrm { v } }$ is the throughput of input messages measured in bytes/second, $\mathrm { T o } _ { \mathrm { v } }$ is the throughput of output messages measured in bytes/second, and PreNT is the pre-noti<sup>fi</sup>cation time measured in seconds.

## De<sup>fi</sup>nition 2. Set of servers

Let Ω be the set of servers of all producer and consumers involved in the collaboration.

$$
\Omega = \{v _ {1}, v _ {2}, v _ {3}, \dots , v _ {n} \}.
$$

![](/api/attachments/3JJRXXEF/fulltext/images/524a38bb25ed6088e424f8efabd4ca115ca8084c3d329b7fb0e75e2779a2e29b.jpg)  
Fig. 1. A taxonomy of SLA measures for web services work<sup>fl</sup>ow composition.

where $\nu _ { 1 } , \nu _ { 2 } , \nu _ { 3 } , . . . , \nu _ { n }$ are the producer and consumer servers. Each v<sub>i</sub> Ω (for all $\mathrm { i } = 1 \ \mathrm { t o } \ \mathrm { n } )$ , is a tuple of SLA measures as described above.

## De<sup>fi</sup>nition 3. Service

A service can be de<sup>fi</sup>ned by some function (in some cases the average) of computations (i.e. processor cycles or relevant measure for the speci<sup>fi</sup>c domain) it requires based on the nature of the processing domain. This computation must incorporate length of the message it receives when realizing its capabilities. A service, s, can be de<sup>fi</sup>ned as the following pair:

$$
s = (C o m p _ {s}, M L _ {s})\tag{2}
$$

where Comp is the number of required computations of the service and $M L _ { s }$ is the message length measured in bytes. The intention of this formalization is to illuminate conceptually the connection between the services and the servers that host them.

## De<sup>fi</sup>nition 4. Set of services

Let Γ be the set of all services involved in a composition.

$$
\Gamma = \{s _ {1}, s _ {2}, s _ {3}, \dots , s _ {m} \}
$$

where $s _ { 1 } , s _ { 2 } , s _ { 3 } , . . . , s _ { m }$ are the services involved in the composition. Each $s _ { i } ~ T$ (for al $\lfloor \mathrm { i } = 1$ to m), is a pair of the number of required computations and the message length (in bytes) as described above.

## De<sup>fi</sup>nition 5. SLA of a service

SLA of a service consists of speci<sup>fi</sup>c web service-oriented measures, as de<sup>fi</sup>ned in the lower elements in the taxonomy in Fig. 2. Let $A _ { s i }$ be the SLA of a service $s _ { i } , A _ { s i }$ can be represented as a tuple shown below:

$$
A _ {s i} = \left(U p _ {s i}, R T i m e _ {s i}, S R e s p _ {s i}, C o s t _ {s i}, P r e N T _ {s i}, R e n e g o t T _ {s i}, R e p _ {s i}, R e l _ {s i}\right)\tag{3}
$$

where $U p _ { s i }$ is the uptime of the service speci<sup>fi</sup>ed by the agreement, $R T i m e _ { s i }$ is the allowable run time, $\mathsf { S R e s p } _ { \mathrm { s i } }$ is the allowable service response time, $C o s t _ { s i }$ is the subscription cost or price of the service, $P r e N T _ { s i }$ is the maintenance pre-noti<sup>fi</sup>cation time, RenegotT is the renegotiation (expiration) time of the agreement, $R e p _ { s i }$ is the reputation of the service and $R e l _ { s i }$ is the reliability rating of the service.

## 4.2. Generating aggregate SLAs across workflows

In this context, we de<sup>fi</sup>ne a web service work<sup>fl</sup>ow as a preestablished process (as de<sup>fi</sup>ned by an SLA) between a consumer and provider (consisting of a group of web services). At composition time, this web service work<sup>fl</sup>ow is not yet an active process or instance, but the speci<sup>fi</sup>cation of all pre-established partnerships or agreements of organizations to share web services. The SLA for a body of many web service work<sup>fl</sup>ows is obtained by composing the set of SLAs of all the services participating in each composition. This process is similar to the traditional QoS-based service composition process although QoS measures must be separated by provider and consumer concerns. The authors work closely with a federal government organization that leverages data-centric web services to develop the list of attributes that are most closely related to services concerned with sharing data from distributed information stores. Hence, the SLAs here consists of uptime of the composite service, the allowable run time, the service response time, the subscription cost or price, the maintenance pre-noti<sup>fi</sup>cation time, and the renegotiation time of the agreement.

![](/api/attachments/3JJRXXEF/fulltext/images/7db064909a9b827455c7a95704c9cbaa291114f9b9337d9c2390b82ba366e95d.jpg)  
Fig. 2. Task time and run time.

Let $A _ { W f }$ represent the composite SLA that is calculated by composing the set of all agreements of all relevant services, i.e., the services on the producer servers and any other services on the consumer's server that might impact the overall system-wide assessment.

Let $A _ { P S }$ represent the set of agreements of the services on the producer's servers that are involved in the composition.

$$
A _ {P S} = \{A _ {P S 1}, A _ {P S 2}, A _ {P S 3}, \dots , A _ {P S m} \}
$$

Let $A _ { C S }$ represent the set of agreements of the services on the consumer's servers that may impact the composite agreement $A _ { W f }$

$$
A _ {C S} = \left\{A _ {C S 1}, A _ {C S 2}, A _ {C S 3}, \dots , A _ {C S n} \right\}
$$

4.2.1. Composite service uptime $( U p _ { W f } )$

The uptime for the composite SLA must be less than the minimum of:

• The uptime $U p _ { v i }$ for consumer's server v Ω and

• The agreed uptimes of the producer's services in $A _ { P S } = \{ A _ { P S 1 } , A$ <sub>PS2</sub>, …, A <sub>PSm</sub>}

The relationship can be shown as:

$$
U p _ {W f} <   \min (U p _ {v i}, \min _ {i = 1 t o m} (U p _ {P S i}))\tag{5}
$$

## 4.2.2. Composite run time $( R T i m e _ { W f } )$

The time required for an individual service to complete its execution can be considered the task time. The repeatability of the task time while the service is in commission translates to the run time. For a web service, the run time is a function of the internet connection, the internal network connection, the hosting hardware, and the software service. Run time is de<sup>fi</sup>ned by the provider or consumer which is captured within the SLA. The combined run time is illustrated in Fig. 2.

The run time for the composite SLA must be less than the minimum of:

• The producer server throughput divided by the message lengths of service input and output

• The consumer server throughput divided by the message lengths of service input and output

Let RTime represent the run time of the consumer. Including the sum of run times already guaranteed to others is important to avoid the impact of a voluminous load from external operations. The run time of the consumer server is obtained by dividing the server throughput T by the message length of the consumer services $M L _ { C S } .$

$$
R T i m e _ {C} = T _ {C} / M L _ {C S}\tag{6}
$$

Let RTime represent the run time of all the stakeholders, i.e., the producers, p. It is the difference of the run times of the sum, m, of all services on the provider-side and the sum, n, of all client-side services.

$$
R T i m e _ {P} = \sum_ {\mathrm{i=1tom}} R T i m e _ {P S i} - \sum_ {\mathrm{i=1ton}} R T i m e _ {C S i}\tag{7}
$$

The run time for the composite SLA is represented as:

$$
R T i m e _ {W f} <   \min (R T i m e _ {P}, R T i m e _ {C})\tag{8}
$$

## 4.2.3. Composite service cost (Cost<sub>Wf</sub>)

The cost of using a web service can be aggregated to understand the price of an entire process. The cost of an individual service is the sum of:

• The bandwidth used (i.e. the product of the usage frequency and the message length) multiplied by the cost per byte/sec of bandwidth, which is a prede<sup>fi</sup>ned constant BC. BC could be zero if bandwidth costs are negligible to the service provider.

• The computations used multiplied by the cost of computation/sec, which is some prede<sup>fi</sup>ned constant CC. As above, CC could be zero if computation costs are negligible to the provider.

• The sum of the costs of all dependent services.

This results in the following equation:

$$
\begin{array}{l} C o s t _ {W f} \geq \left(R T i m e _ {W f} \times M L _ {C S} \times B C\right) + \left(R T i m e _ {W f} \times C _ {S} \times C C\right) \\ + \sum_ {i = 1 \text { tom }} C o s t _ {P S i} \end{array}\tag{9}
$$

4.2.4. Composite service pre-notification time (PreNT<sub>Wf</sub>)

When a service must be disabled for maintenance, organizations must inform their collaborators. The minimum time for noti<sup>fi</sup>cation before maintenance begins is calculated as the minimum of:

• The time of noti<sup>fi</sup>cation for the consumer server v<sub>i</sub>

• The minimum of all noti<sup>fi</sup>cation times agreed upon for all dependent services

This relationship can be illustrated as:

$$
\operatorname{PreNT} _ {W f} \leq \min \left(\operatorname{PreNT} _ {v i}, \min _ {\mathrm{i} = 1 \text { tom }} \left(\operatorname{PreNT} _ {P S i}\right)\right)\tag{10}
$$

4.2.5. Composite service renegotiation time (RenegotT<sub>Wf</sub>)

Negotiation/renegotional time is the guarantee giving by the provider and consumer that de<sup>fi</sup>nes how quickly a request for new QoS attributes will be acknowledged the other party. The renegotiation date for this agreement must be after the prede<sup>fi</sup>ned constant waiting time, WT, with respect to each other's agreement to which this server is a party. This notion of renegotiation time is illustrated in Fig. 3. The equation below must hold for each agreement $A _ { C S i } \ A _ { C S }$ to which the service provider is a party. This test can be shown as:

$$
\text {   for   all   } i = 1 \text {   to   } n, \text {   Renegot   } T _ {W f} = \max (\text { Renegot } T _ {C S i} + W T)\tag{11}
$$

Problem resolution is not formally de<sup>fi</sup>ned because the calculation is a similar formula as renegotiation. As a de<sup>fi</sup>nition (shown in Fig. 4), problem resolution can be de<sup>fi</sup>ned as the sum of the time for recognizing the error, the time that it takes for a provider to acknowledge the error, and the actual time for resolving the problem.

## 4.2.6. Composite service reputation (Rep<sub>Wf</sub>)

In a service composition scenario, reputation is de<sup>fi</sup>ned as a numeric score on a relative scale for a web service as captured by consumers and providers in a web service repository. The Reputation for the composite service is calculated as the average of:

![](/api/attachments/3JJRXXEF/fulltext/images/162b2d0275376d7fadca581e008d84195cfe4b0fa0fb8dcff435198054c2ab18.jpg)  
Fig. 3. Aspects of renegotiation time.

• The reputation for the consumer server v<sub>i</sub>

• The average reputation for all the dependent services

This relationship can be illustrated as:

$$
R e p _ {W f} = \text { average } (R e p _ {v i} + (\sum_ {i = 1 \text { tom }} R e p _ {P s i}) / m)\tag{12}
$$

4.2.7. Composite service reliability $( R e l _ { W f } )$

Reliability in traditional QoS-based web service composition has been calculated using several approaches in related work [19]. Unlike other approaches, this approach deals with SLA speci<sup>fi</sup>cations which tend to be the worst case agreement between consumer and provider. As such, we believe closest estimate is to aggregate the values by calculating the minimum of:

• The reliability for the consumer server v<sub>i</sub>

• The minimum of reliabilities for all the dependent services

This relationship can be illustrated as:

$$
R e l _ {W f} \leq \min (R e l _ {v i}, \min _ {i = 1 \text { tom }} (R e l _ {P S i}))\tag{13}
$$

De<sup>fi</sup>nition 6. Composite SLA

The composite SLA, A is a tuple of all the aggregated SLA measures as shown:

$$
A _ {W f} = \left(U p _ {W f}, R T i m e _ {W f}, S R e s p _ {W f}, C o s t _ {W f}, P r e N T _ {W f}, R e n e g o t T _ {W f}, R e p _ {W f}, R e l _ {W f}\right)
$$

where the aggregated SLA measures Up<sub>Wf</sub>, RTime<sub>Wf</sub>, SResp<sub>Wf</sub>, Cost<sub>Wf</sub>, PreNT<sub>Wf</sub>, RenegT<sub>Wf ,</sub> Rep<sub>Wf ,</sub> Rel<sub>Wf</sub> are obtained from the relations shown in Eqs. (5), (8), (9), (10), (11), (12), and (13) respectively.

## 5. Representing SLA attributes as WS-Agreements (WSAG)

In order to store and manage SLAs, the attributes must be represented in a format conducive for distributed data management. XML is a language that allows complex information to be represented with embedded metadata. An XML-based approach to representing SLA information facilitates quick interpretation of data and using translation techniques, such as the eXtensible Stylesheet Language, XSL, allows the comparison and aggregation of the underlying information. WSAG is an XML-based language that is de<sup>fi</sup>ned with SLA attributes. A brief background is discussed here, but more information can be found at [21]. In a WSAG document, the data are represented hierarchically underneath the notion of an agreement. An agreement can be further speci<sup>fi</sup>ed with name or identifying string. An agreement can also be described by its context. Context information includes the name of the consumer and producer, the timeframe by which the agreement is valid, and other related template information. Each agreement encapsulates a list of terms. Terms describe the information of the services that are included.

Of most importance to this work are the guarantee terms. Guarantee terms consist of a service scope which contains the service names of the speci<sup>fi</sup>c service relevant to the guarantee. The service level objective contains a predicate for the metrics that quantitatively de<sup>fi</sup>ne the guarantee. The service level objective contains the parameter name, value, and unit of measure. As an example, the SLA attributes of uptime and maintenance are shown in Table 2. Uptime is a common attribute for SLAs. As described earlier, an uptime SLA guarantees the availability of a service by percentage over a designated period of time. The other SLA metric, maintenance noti<sup>fi</sup>cation time, is not as universally used as uptime. The example in Table 2 shows that maintenance noti<sup>fi</sup>cation time is also straightforward with regard to representation in the WS-Agreement notations.

![](/api/attachments/3JJRXXEF/fulltext/images/e5103466b1a12f68fc40633a82b0bf10e6f9adba07c6621ff15d79576a187b58.jpg)  
Fig. 4. Aspects of problem resolution.

Capturing service level agreements in XML-based notations allows the SLA attributes to be represented in a format similar to the WSDL <sup>fi</sup>les that represent the operational speci<sup>fi</sup>cations of the service. WSAG can be transported and negotiated along with WSDL <sup>fi</sup>les. This represents a bene<sup>fi</sup>t if a service stakeholder wants to evaluate multiple services, side-by-side. Another bene<sup>fi</sup>t of capturing SLA attributes in XML-based <sup>fi</sup>les is the ability of enhancing attributes with semantics. It is possible that organizations will name attributes with their own specialized naming schemes. Semantics would allow disparate organizations to mediate SLA attributes that are the same but may be named differently. This approach leverages the numerous projects that use semantics to highlight web services for mediation.

However, a detriment of capturing these attributes in XML-based notations occurs when organizations have pre-established agreements. It is likely that, in a service-oriented computing environment, coalitions of businesses will form similar to partnerships that occur in traditional businesses. In such cases, the overhead of descriptive tags may be unnecessary. In addition, SLA constraints may become more comprehensive as the partnerships enhance their coordination and negotiation. These <sup>fi</sup>les may become too cumbersome for semi-automated manipulation where human inspection may be a required step in overall process.

## 6. Creating aggregated SLAs on-demand

The formalization in previous sections shows the necessary measures for creating SLAs for new business work<sup>fl</sup>ows that re<sup>fl</sup>ect the effects of other work<sup>fl</sup>ows existing at the same organization. The authors collaborated with The MITRE Corporation for the development of a framework for defense information systems organizations shown in

```xml
WS-Agreement for uptime

<wsag:GuaranteeTerm wsag:Name="uptimePref" wsag:Obligated="ACME">
    <wsag:ServiceScope>
    <wsag:ServiceName>AcmeService1</wsag:ServiceName>
    </wsag:ServiceScope>
    <wsag:ServiceLevelObjective>
    <wsag:predicate type="greater">
    <wsag:parameter>job:uptimePercentage</wsag:parameter>
    <wsag:value>5</wsag:value>
    <wsag:unit>time:seconds</wsag:unit>
    </wsag:predicate>
    </wsag:ServiceLevelObjective>
    </wsag:GuaranteeTerm>

WS-Agreement for Maintenance

<wsag:GuaranteeTerm wsag:Name="maintenanceNotificationPref" wsag:Obligated="ACME">
    <wsag:ServiceScope>
    <wsag:ServiceName>AcmeService1</wsag:ServiceName>
    </wsag:ServiceScope>
    <wsag:ServiceLevelObjective>
    <wsag:predicate type="greater">
    <wsag:parameter>job:maintPreNotification</wsag:parameter>
    <wsag:value>7</wsag:value>
    <wsag:unit>time:days</wsag:unit>
    </wsag:predicate>
    </wsag:ServiceLevelObjective>
    </wsag:GuaranteeTerm>
```

Fig. 5. These organizations host large numbers of web services that provide battle<sup>fi</sup>eld information such as weather information, force location and tracking information, and satellite telemetry. Each of the various defense forces (Army, Navy, Air Force, etc.) provides access their web services via this shared portal. The sources vary in their guaranteed service level objectives. The defense information systems organizations are devising portals that manage SLAs in governance database while recording historical service level information. The approaches devise in this paper are incorporated within the portal logic. As such, when producers provide new services and when clients gain access to existing services, SLAs are veri<sup>fi</sup>ed for validity.

In such an ad-hoc environment, it is important to understand if the SLA composition process can be performed ef<sup>fi</sup>ciently enough to support the real-time insertion of new partners looking to exploit existing services. In this work, we de<sup>fi</sup>ne an integrated process for work<sup>fl</sup>ow-based SLA composition when suggesting new SLAs. This process can be decomposed into two steps, SLA composition and evaluation. These two steps are illustrated in Fig. 6.

The SLA composition step is similar to traditional QoS-based web service composition approaches. In the evaluation step, user preferences are used to prioritize the list of candidate service chains. Numerous dynamic programming techniques can be used to achieve this step. We present a unique approach where instead of acquiring speci<sup>fi</sup>c QoS value expectation from the user, instead user's priorities are collected. A quality score is generated based on the user's preferences. Our evaluation shows that, in real-time operations, the composition and evaluation steps are feasible considering a large number of existing business processes.

## 6.1. Composition: building candidate workflows

In order for SLA measures to be useful for both real-time operations and decision support, the web services work<sup>fl</sup>ow generation must integrate traditional web service composition with the SLA composition procedures. The SLA composition procedure must be integrated at each step and also applied to the work<sup>fl</sup>ow as a whole once the full process is generated. We de<sup>fi</sup>ned the information provided by the user to be the user.predicate and the desired outcome to be the user.reqresults. The step.predicate is the set of information used to select subsequent services in the composition. At the initiation of a composition routine, the user.predicate is equivalent to the step.predicate. These relationships are illustrated in Fig. 7.

We introduce an integrated procedure that combines standard web service composition with SLA composition. Table 3 shows the pseudocode of the integrated process. The composition process has a main integrated process, IntegratedComp(). The StepCompose() process occurs at each step and WorkflowChk() process occurs once the required information and actions are realized with the execution of the sequence of web services. The ComposeSLA() process is the computation mechanisms that implement the SLA aggregation procedures.

## 6.2. Evaluation: prioritizing SLA compositions

In the prior section, candidate service chains are generated that meet the functional and SLA requirements of the user. Nevertheless, at this point, there are still multiple chains that can ful<sup>fi</sup>ll a capability. As such, there remains an open requirement to sort the chains based on quality and choose the best chain in the group.

In order to prioritize service chains, users are asked to provide a priority, Pr, for each attribute with respect to their environment, where $R r { = } \{ P r _ { 1 } , P r _ { 2 } , P r _ { 3 } { , } . . . , P r _ { n } \}$ . The priorities represent the rank ordered SLA measures from greatest to least importance. The priorities relate to the corresponding set of SLA measures, where $S L A { = } \{ S L A _ { 1 } , S L A _ { 2 } ,$ $S L A _ { 3 } . . . , S L A _ { n } \}$ . A SLA attribute has the best possible value, B. Our approach will strongly consider chains that perform favorably with respect to the user's preferences. After evaluation, $G _ { S }$ and $G _ { \mathsf { W } }$ represent the quality score for the service and work<sup>fl</sup>ow, respectively.

![](/api/attachments/3JJRXXEF/fulltext/images/30f4b33ebf93e4774e9cd4f99fe1a7e5b32776d0ae8ee37b39b3e98ec6ad969d.jpg)  
Fig. 5. A practical operational scenario.

As such, the quality score for an individual service can be de<sup>fi</sup>ned by weighing the user's priority with respect to the ratio of the SLA measure to the best possible measure for that attribute. The calculation is de<sup>fi</sup>ned as:

$$
G _ {S} = \sum_ {n = 0} ^ {n} \left(\operatorname * {P r} _ {n} \cdot \frac {S L A _ {n} - B (S L A _ {n})}{B (S L A _ {n})}\right)\tag{14}
$$

<sup>¼</sup>The corresponding quality score for the service chain is:

$$
G _ {W} = \sum_ {m = 0} \left((G _ {S}) _ {m}\right)\tag{15}
$$

This approach relies on user-supplied priority weights and perhaps lacks the precision of standard multiple criteria decision analysis [12] which focuses on decision optimization. However, in the next section, we demonstrate that this approach performs favorably as a real-time assessment during the dynamic composition process.

## 7. Performance evaluation of the integrated composition process

In real-time operations, SLA composition will be required to occur within a reasonable response time. In this work, we evaluate expected response time for the composition and prioritization of SLA measures. Our experiments are performed on a Mobile Intel Pentium 4, 2.4 GHz, 1 GB RAM, running Windows XP and the Java Runtime Environment (JRE) 6 Update 1. An initial experiment was performed that evaluates the response when prioritizing SLAannotated work<sup>fl</sup>ows of web services. Based on a set of random WSAG <sup>fi</sup>les (with uniformly distributed randomly generated SLA terms and their values), we created software that generates web service objects. In this context, using a uniformly distributed, randomly generated set of attributes for values is appropriate. This experimentation is a proof of concept that the SLA composition can execute fast enough to appropriately be included into the real-time composition scenarios. This is mostly an information management procedure. The authors understand that a non-uniform list of attributes may incur additional overhead. Here, the argument is made that datacentric organizations must keep their list of guarantees (as represented by attributes) uniform, such that their operations are consistent across each of their consumers. It is also not implausible that the provider use such policy to ensure a predictable processing time.

![](/api/attachments/3JJRXXEF/fulltext/images/489666746ebbf98ee1850e5a09c12e4e31b28ad5f9ec4e18af6a41b6923f0825.jpg)  
Fig. 6. Two-step process for integrated SLA work<sup>fl</sup>ow composition.

![](/api/attachments/3JJRXXEF/fulltext/images/26f86211158265603c1d5e9a3220cfac8c6572a7485667cf6c1a4d9fe0a1721f.jpg)  
Fig. 7. Data <sup>fl</sup>ow in a composition routine.

Each service objects has a unique identi<sup>fi</sup>cation codes that associates it with the corresponding WSAG <sup>fi</sup>les. We duplicated identi<sup>fi</sup>cation codes (i.e. ids) such that increasing numbers of services have the same ids. The process of aggregating ids was done in an attempt to

## Table 3

Integrated composition pseudo-code.

```txt
IntegratedComp: Main integrated composition function
StepCompose: Function that occurs at each step
WorkflowChk : Process-Level Functional/SLA check
composeSLA: Function that aggregates SLA measures
PR,RenegotT,Cost : Problem Resolution, Renegotiation, Cost
RTime,Up,PreNT: Run time, uptime, maintenance
Rel,Rep: Reliability, reputation
step.predicate: Message information required to execute service
ws WSDL Object with SLA measures
user.reqresults: Message information required as output of service
service_chain: Candidate workflow of web services
IntegratedComp
{
    step.predicate = user.predicate
    WHILE (step.predicate != user.reqresults)
    { StepCompose() }
    WorkflowChk()
}
StepCompose
{
    FOR EACH candidate ws where
    ws.message step.predicate
    THEN ADD (ws) to List<ws>
    FOR EACH candidate ws IN List<ws>
    IF ((ws.PR <= step.PR) || (ws.RenegotT <= step.RenegotT) ||
    (ws.Cost >step.Cost) || (ws.RTime <= step.RTime) ||
    (ws.Up <= step.Up) || (ws.PreNT <= step.PreNT) ||
    (ws.Rel <= step.Rel) || (ws.Rep <= step.Rep))
    THEN REMOVE (ws) from List<ws>
    ELSE {
    ADD ws to List<service_chain>
    ADD ws.outputs to List<step.predicate >
    }
}
WorkflowChk
{
    FOR EACH service_chain
    IF (chain.outputs user.reqresults) &&
    (ComposeSLA (ws.PR, ws.RenegotT, ws.Cost, ws.Up,
    ws.PreNT, ws.RTime, ws.Rep, ws.Rel )<user.SLA))
    THEN ADD (service_chain) to Candidate List
}
```

simulate composition as a prerequisite step to the actual SLA composition. Each web service object was populated with six SLA measures. Although there are more attributes, we decided to experiment with 6 with the expectation that more attributes would scale consistently. Our experimentation searches the repository of web service objects, composes services of the same id, and then prioritizes the resulting chain. This experiment was executed on a repository with varying sizes from 100 to 100,000 services. The work<sup>fl</sup>ow size (number of services in a chain) was also varied. The number of services per chain is varied from 10 to 100,000 services within a repository of 1,000,000 services. Fig. 8 shows the results of this <sup>fi</sup>rst experiment. Response time represents the average time required for the proposed algorithm to correlate the SLA attributes to generate a composite measure for a particular web service composition routine. Considering a reasonable work<sup>fl</sup>ow of web services of 100 interconnected services or less, a response time of 1.6 ms per service chain is promising. As a variation of the response time experimentation, we also investigated how the size of the repository affects the performance of our algorithm. Fig. 9 shows the response time of our algorithm as the repository increases. The work<sup>fl</sup>ow chain of the composition request is held constant at 10 services but the repository increases from 100 to 100,000. In the results of this experiment, search time is also considered. Given the largest repository of 100,000 services, the SLA composition time (including the processing time for discovering the relevant services (i.e. 10 services) is 30.2 s. Although the results are favorable in a simulated environment, the reader should understand that many other conditions with regard to performance variations and real-time factors on open systems reduce the con<sup>fi</sup>dence of these results.

In a second experiment, we evaluated the performance by varying the number of SLA attributes that are used for calculation. In this paper, we experiment with up to six attributes, but we expect that other attributes will be required to extend this approach in the future. As such, it is important to understand the overhead associated with adding a new SLA attribute for real-time operations. Although it is understood that the performance increases as the computing hardware is improved, we are generally interested in how the approach scales as the number of attributes increases in a <sup>fi</sup>xed-size repository.

Fig. 10 shows the search and calculation time when varying the numbers of attributes (i.e. the number of attributes tested for each). Although this graph has a high concentration of search time (\~90%), it is clear that the performance degrades favorably (linearly) at less than 12 ms per attribute (i.e. the calculation time increases less than 1 millisecond for the addition of each new attribute). Another variation of this experiment, also shown in Fig. 10, considers the impact of SLAs that process fewer attributes. In some cases, service agreements may only consider a subset of the total possible guarantee conditions. As such, less attributes may be stored per service (i.e. Attributes Stored). The Attributes Stored measure in Fig. 10 shows that there is only a slight advantage for service-oriented providers to be less stringent. Another variation considers increasing performance of SLA composition by limiting the number of attributes that a service composition considers. The major question is “Can runtime performance increase if the business management system only considers a subset of possible SLA attributes?”. Experimentation shows that even at the most extreme case, if a service provider only allows services to be constrained by one attribute, the performance is only improved by approximately 30%. Predictably, as shown in

![](/api/attachments/3JJRXXEF/fulltext/images/8ad78053f758e84261dc03f07a201dcd34a1e9634efc06747f604e76272dc2cd.jpg)  
Fig. 8. The performance of the SLA prioritization function as the number of services per work<sup>fl</sup>ow increase (service discovery time excluded).

Fig. 10, the improvement in performance decreases as more attributes are considered.

## 8. Conclusion

When provider organizations expose their services for consumption by their peers, it is important for them to understand what they are guaranteeing. Moreover, consumers that receive such commitments must abide by their own commitments such that the providers can meet their guarantees to all consumers. In this work, we introduce a method of assessing an organization based on both pending and existing SLAs. Since the estimation of QoS measures for web services has been investigated in great detail, in this paper, we make a varied contribution. Our work builds on the existing studies by considering the QoS guarantees, as captured in SLAs, such that provider and consumer concerns can be modeled independently. This work also considers that SLA assessment occurs in a separate process than standard QoS estimation at service composition time. Here, we introduce high-level criteria that can be created from the aggregation of a comprehensive list of lower-level QoS-based attributes. This variation to related work facilitates automated cross-enterprise SLA negotiation. In this paper, we de<sup>fi</sup>ne a two-step process for composing SLAs and evaluating their ef<sup>fi</sup>ciency. Consistent with results in related work that estimate QoS on fully operational web services, we have found through simulated experimentation that the management of third-party SLA information can be composed ef<sup>fi</sup>ciently in parallel with the actual operational service composition. In future work, we plan to implement our approach within a real operational setting as opposed to the simulation setting that is represented in this paper. In the real operational setting, data will be produce using a variety of distributions. As such, WS-Agreement <sup>fi</sup>les will be appended to WSDL <sup>fi</sup>les and evaluated in a network environment for performance and feasibility. In addition, we plan to extend the SLA composition paradigm to protocols that mandate the discovery process within web service registries. In this way, it may be possible for adaptive software (or intelligent agents) to negotiate SLAs, in real time, while they perform on-demand, service discovery.

## Acknowledgment

This work was bene<sup>fi</sup>ted by the participation of Dr. M. Brian Blake in the Service Level Agreement Technical Exchange Meeting held at The MITRE Corporation on July 2006 in McLean, Virginia. In addition, the service discovery approach/software used in this work was partially funded by the National Science Foundation under award number 0548514.

![](/api/attachments/3JJRXXEF/fulltext/images/6604997e13035eee3d1bfdfd42c6c952cfdc0ccd3f7e8e95e4390a141b5023ae.jpg)  
Fig. 9. The performance of the SLA prioritization function as the repository increases (service discovery time included).

Performance Evaluation by Attributes Stored and Attributes Tested (100,000 services, 10 services per chain)  
![](/api/attachments/3JJRXXEF/fulltext/images/2dcb954fc5d2e7d495483809e991db02864e7a28095fcc17ded8c0833302208a.jpg)  
Fig. 10. The performance overhead associated with the addition of new attributes

## References

[1] P. Alipio, S. Lima, P. Carvalho, XML service level speci<sup>fi</sup>cation and validation, Proc. of the 10th IEEE Symposium on Computers and Communications (ISCC), June 2005, pp. 975–980.

[2] A. Andrieux, K. Czajkowski, A. Dan, K. Keahe, H. Ludwig, T. Nakata, J. Pruyne, J. Rofrano, S. Tuecke, M. Xu, “Web Service Agreements Speci<sup>fi</sup>cation (WS-Agreement),” Proposed Recommendation, Open Grid Forum (OGF) Document Number GFD-R-P.107, Mar 2007 OGF Grid Resource Allocation Agreement Protocol Working Group (GRAAP-WG)Acces sible at, http://www.gridforum.org/Public\_Comment\_Docs/Documents/Oct-2005/WS AgreementSpeci<sup>fi</sup>cationDraft050920.pdf.

[3] J.E. Angus, On computing MTBF for a k-out-of-n: G repairable system, IEEE Transactions on Reliability 37 (3) (1988) 312–313.

[4] M.B. Blake, B2B electronic commerce: where do agents <sup>fi</sup>t in? Proceedings at the AAAI-2002 Workshop on Agent Technologies for B2B E-Commerce/AAAI Press, Edmonton, Alberta, Canada, July 2002.

[5] M.B. Blake, Decomposing composition: service-oriented software engineers, IEEE Software 24 (6) (Nov/Dec 2007) 68–77.

[6] M.B. Blake, A lightweight software design process for web services work<sup>fl</sup>ows, Proc. of the 4th IEEE International Conference on Web Services (ICWS), Sept. 2006, pp. 411-418.

[7] M.B. Blake, D.J. Cummings, Work<sup>fl</sup>ow composition of service level agreements Proc. of the IEEE International Conference on Services Computing (SCC 2007) July 2007, pp. 138–145.

[8] M.B. Blake, M. Gini, Guest editorial: agent-based approaches to B2B electronic commerce, International Journal of Electronic Commerce 7 (1) (2002) 113–114.

[9] G. Canfora, G. M Di Penta, R. Esposito, F. Perfetto, M.L. Villani, Service composition (re)binding driven by application-speci<sup>fi</sup>c QoS, Proc of International Conference on Service-Oriented Computing (ICSOC), 2006, pp. 141–152.

[10] A.J. Cardoso, “Quality of Service and Semantic Composition of Work<sup>fl</sup>ows,” Ph.D. Dissertation, University of Georgia, 2002.

[11] G. Di Modica, V. Regalbuto, O. Tomarchio, L. Vita, Dynamic re-negotiations of SLA in service composition scenarios, Proc. of the 33rd EUROMICRO Conference on Software Engineeringand Advanced Applications, August 2007, pp. 359–366.

[12] J. Dyer, Maut — multiattribute utility theory in multiple criteria decision analysis: state of the art surveys, International Series in Operations Research, Management Science, vol. 78, Springer, 2005, pp. 265–292.

[13] T. Falkowski, S. Vob, Application service providing as part of intelligent decision support for supply-chain management, Proc. of the 36th Annual Hawaii International Conference on System Sciences (HICSS), vol. 3, 2003, p. 80.

[14] M. Gillman, G. Weikum, W. Wonner, Work<sup>fl</sup>ow management with service quality guarantees, Proc. of ACM SIGMOD International Conference on Management of Data, 2002, pp. 223–239.

[15] L. Green, Service level agreements: an ontological approach, Proc. of the 8th ACM International Conference on Electronic Commerce (ICEC), August 2006, pp. 185–194, Fredericton, Canada.

[16] D. Greenwood, G. Vitaglione, L. Keller, M. Calisti, Service level agreement management with adaptive coordination. Proc. of the International Conference on Networking and Services (ICNS) July 2006 p. 45–50 Silicon Valley USA.

[17] C.-W. Hang, M.P. Singh, Trustworthy service selection and composition, ACM Transactions on Autonomous and Adaptive Systems 6 (1) (Feb 2011).

[18] L. Jin, V. Machiraju, A. Sahai, Analysis on service level agreement of web services, HP Technical Report, HPL-2002-180, June 2002, accessible at (2008), http://www. hpl.hp.com/techreports/2002/HPL-2002-180.pdf.

[19] J. Ko, C.O. Kim, I. Kwon, Quality-of-service oriented web service composition algorithm and planning architecture, Journal of Systems and Software 81 (11) (November 2008) 2079-2090.

[20] H. Ludwig A. Keller, A Dan R.P. King, R. Franck Web Service Level Agreement (WSIA) Language Speci<sup>fi</sup>cationAccessible at, http://www.research.ibm.com/wsla2007.

[21] M. Mecella, M. Scannapieco, A. Virgillito, R. Baldoni, T. Catarci, C. Batini, Managing data quality in cooperative information systems, Lecture Notes in Comptuer Science 2512 (2002) 486–502.

[22] M. Mohabey, Y. Narahari, S. Mallick, P. Suresh, S.V. Subrahmanya, An intelligent procurement marketplace for web services composition, Proc. of the IEEE/WI-C/ACM International Conference on Web Intelligence, Nov. 2007, pp. 551–554.

[23] N.J. Muller, Managing service level agreements, International Journal of Network Management 9 (3) (May 1999)

[24] F. Naurmann, U. Leser, J.C. Freytag, Quality-driven integration of heterogeneous information systems, Proc. of the 25th International Conference on Very Large Databases, September 1999, pp. 447–458, Edinburgh, Scotland, UK.

[25] N. Oldham, K. Verma, A.P. Sheth, F. Hakimpour, Semantic WS-Agreement partner selection, Proc. of the 15th International World Wide Web Conference (WWW), 2006.

[26] F.R. Reiss, T. Kanungo, Satisfying database service level agreements while minimizing cost through storage QoS, Proc. of the IEEE International Conference on Services Computing (SCC), July 2005, pp. 13–21.

[27] A. Sahai, V. Machiraju, M. Sayal, A. Moorsel, F. Casati, Automated SLA monitoring for web services, Proc. of the IEEE/IFIP International Workshop on Distributed Systems: Operation and Management (DSOM), October 2002, pp. 28–41, Montreal, Canada.

[28] D. Skene, Lamanna, W. Emmerich, Precise service level agreements, Proc. of the 26th International Conference on Software Engineering (ICSE) 2004 pp. 179–188 Edinburgh, UK.

[29] I. Sorteberg, O. Kure, The use of service level agreements in tactical military coalition force networks, IEEE Communications Magazine 43 (11) (November 2005) 107–114

[30] W. Sun, Y. Xu, F. Liu, The role of XML in service level agreements management, Proc. of the International Conference on Services Systems and Services Management, June 2005, pp. 1118–1120.

[31] K.M. van Hee, L.J. Somers, M. Voorhoeve, A modeling environment for decision support systems, Decision Support Systems 7 (1) (1991) 241–251.

[32] G. Xiaohui, K. Nahrstedt, A scalable QoS-aware service aggregation model for peer-to-peer computing grids, Proc. of the 11th IEEE International Symposium on Higher Performance Distributed Computing (HPDC), 2002, pp. 73–82.

[33] J. Yan, R. Kowalczyk, J. Lin, M.B. Chhetri, S.K. Goh, J. Zhang, Autonomous service level agreement negotiation for service composition provision, Future Generation Computer Systems 23 (6) (July 2007) 748–759.

[34] T. Yu, K.J. Lin, Service selection algorithms for composing complex services with end-to-end QoS constraints. Proc. 3rd International Conference on Service Oriented Computing (ICSOC2005), The Netherlands Amsterdam, 2005.

[35] L. Zeng, B. Benatallah, A.H.H. Ngu, M. Dumas, J. Kalagnanam, H. Chang, QoS-aware middleware for web services composition, IEEE Transactions on Software Engineering 30 (5) (May 2004) 311–327

[36] Y. Zhang, K.J. Lin, J.Y.J. Hsu, Accountability monitoring and reasoning in service oriented architectures, Service-Oriented Computing and Applications 1 (2007) 35–50.

[37] M. zur Muehlen, J. Nickerson, K.D. Swenson, Developing web services choreography standards — the case of REST vs. SOAP, Decision Support Systems 40 (1) (2005).

M. Brian Blake received the BS degree in electrical engineering from the Georgia Institute of Technology, Atlanta and the PhD degree in information technology with a concentration in information and software engineering from George Mason University, Fairfax, Virginia. He is currently Professor of Computer Science and Associate Dean of Engineering at the University of Notre Dame, Indiana. As a professor, he has published more than 120 journal and refereed conference papers in the domains of work<sup>fl</sup>ow and agent-based systems, service-oriented computing, distributed data management, and software engineering education. His investigations cover the spectrum of software engineering: design, speci<sup>fi</sup>cation, proof of correctness, implementation/experimentation, performance evaluation, and application.

Ajay Bansal received his B. Tech. degree in Computer Science from NIT (previously known as REC), Warangal, India, M.S. in Computer Science from Texas Tech Univ., Lubbock and Ph.D. in Computer Science from the University of Texas at Dallas. He is currently a lecturer in the College of Technology and Innovation at Arizona State University. He has over 3 years of industry experience. His research interests include Programming Languages, Logic Programming, Declarative Programming, Automated Reasoning, Service-Oriented Computing, Semantic Web Services, and Language-based Security.

Srividya Kona Bansal received her B. Tech. degree in Computer Science from NIT (previously known as REC), Warangal, India, M.S. in Computer Science from Texas Tech Univ., Lubbock and Ph.D. in Computer Science from the University of Texas at Dallas. She is currently an assistant professor in the College of Technology and Innovation at Arizona State University. She has over 5 years of industry experience. Her research interests include Service-Oriented Computing, Semantic Web, Software Engineering, Engineering Education, and Bioinformatics.
