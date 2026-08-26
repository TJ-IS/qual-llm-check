---
otero_id: 6744
otero_key: "TQEY3ZWM"
title: "Using enterprise architecture analysis and interview data to estimate service response time"
authors: "Per Närman; Hannes Holm; Mathias Ekstedt; Nicholas Honeth"
year: "2013"
journal: "The Journal of Strategic Information Systems"
doi: "10.1016/j.jsis.2012.10.002"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Using enterprise architecture analysis and interview data to estimate service response time

Per Närman ⇑, Hannes Holm, Mathias Ekstedt, Nicholas Honeth

Industrial Information and Control Systems, Osquldas v. 12, SE-10044 Stockholm, Sweden Industrial information and Control Systems, Royal Institute of Technology, Stockholm, Sweden

## a r t i c l e i n f o

Article history: Available online 3 December 2012

Keywords: Enterprise architecture Performance Design science Quality of service Service management Service engineering

## a b s t r a c t

Insights into service response time is important for service-oriented architectures and service management. However, directly measuring the service response time is not always feasible or can be very costly. This paper extends an analytical modeling method which uses enterprise architecture modeling to support the analysis. The extensions consist of (i) a formalization using the Hybrid Probabilistic Relational Model formalism, (ii) an implementation in an analysis tool for enterprise architecture and (iii) a data collection approach using expert assessments collected via interviews and questionnaires. The accuracy and cost effectiveness of the method was tested empirically by comparing it with direct performance measurements of five services of a geographical information system at a Swedish utility company. The tests indicate that the proposed method can be a viable option for rapid service response time estimates when a moderate accuracy within 15% is sufficient. - 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

Information technology (IT) permeates every modern organization. Presently, the most prevalent IT architecture style is service-oriented architecture (SOA) (Papazoglou and Van Den Heuvel, 2006). SOA facilitates re-use and easy integration by abstracting the delivered functionality from the underlying technical infrastructure thereby exposing functionality as services, which are accessible through well-defined interfaces (Papazoglou and Van Den Heuvel, 2006).

These properties have the potential to allow for greater enterprise flexibility and a higher level of interoperability (Ren and Lyytinen, 2008; Chen et al., 2010). However, the benefits of service orientation are contingent upon maintaining adequate Quality of Service (QoS) levels (Gorla et al., 2010). Response time is a QoS attribute which when degraded significantly impairs user experience (Palmer, 2003). Thus, a business-oriented service management and engineering approach is necessary (Papazoglou and Van Den Heuvel, 2006; Riedl et al., 2009). Architecture models can for instance be employed for QoS analysis (Ullberg et al., 2008) and can aid service management by providing decision makers with design and analysis capabilities (Braun and Winter, 2007; Alwadain et al., 2010; Aier et al., 2009). Enterprise Architecture (EA) has become an established discipline for business and IT management (Ross et al., 2006). EA relies on models to depict the overall organization of major components of the infrastructure, application and business layers, thus helping IT-decision makers understand the business impact of IT and increasing business-IT alignment (Winter et al., 2007). Iacob and Jonkers (2004, 2006) presented a method that uses the enterprise architecture language ArchiMate (Lankhorst et al., 2009) to analyse service response times.

This paper suggests augmenting the original method by (i) formalizing it through the use of the Hybrid Probabilistic Relational Model formalism (Närman et al., 2010). (ii) by implementing it in the EA analysis tool Enterprise Architecture Analysis

Tool (EAAT) (Buschle et al., 2010), and (iii) by using data based on expert assessments collected via interviews and questionnaires. Expert assessments are used because performance and capacity monitoring equipment is not always practical in industry and can be time consuming; thus, the method proposed is useful for a broader range of organizations.

An important success criterion of this approach is the accuracy of the response time estimates.Additionally, because service response time management may not always be prioritized, an important constraint on the method is that it must be inexpensive to use (Johansson et al., 2006; Närman et al., 2009; Zahedi, 1997). To test whether the method satisfies these criteria, the architecture-based method was compared with direct measurements in a study using empirical data where the response times of five services of a Geographical Information System (GIS) at a Swedish utility company were evaluated. The results were then compared in terms of accuracy and cost.

In summary, this paper aims to design and evaluate and an analytical method for modeling and estimating service response time based on enterprise architecture by:

1. Formalizing the method of Iacob and Jonkers for performance analysis and implementing it in a modeling and analysis tool.

2. Suggesting a data collection approach based on expert assessments using questionnaires and interviews.

3. Testing whether the method produces accurate service response time estimates and is cost effective.

The paper proceeds as follows. Section 2 reviews related work, and Section 3 introduces the overall research design. Section 4 explains the method of Iacob and Jonkers’ and the HPRM formalism. The studyin which the proposed method was tested is described in Section 5. Section 6 describes the response time measurements, and Section 7 presents the results and discusses possible sources of error. Finally, Section 8 concludes the paper by presenting the contributions and limitations of this study.

## 2. Related work

This section presents related work, which is divided into three subsections on SOA, IT service management and performance analysis.

## 2.1. Service quality and performance in SOA

The SOA domain has received much recent research attention (e.g. Erl, 2005; Kohlborn et al., 2009). SOA refers to an IT architecture style in which functionality is separated from its realizing applications by packaging it as services with welldefined interfaces and by orchestrating the services to fit the requirements of business processes (Erl, 2005). A frequent theme regarding service orientation is how to derive business and IT services based on functional requirements, elicited from business process models (Leymann et al., 2002; Kohlmann and Alt, 2007).

Being able to elicit the functional content of the services, however, provides no details about the response times of the services. A number of studies have therefore provided in-depth investigations on various aspects of Quality of Service (QoS) and Service Level Agreements (SLA) management including aspects related to response time analysis. For instance Zeng et al. (2003) describes an implementation prototype which selects services based on QoS attributes including execution time. Jaeger et al. (2004, 2005) employ workflow patterns as defined by van Der Aalst et al. (2003) to derive QoS, including execution time, of composed services. In these studies, it was assumed that the QoS of the individual, atomic services is known and quite stable, independent of for instance workload which is not always the case, a deeper analysis needs to take workload into account.

QoS is a concept closely linked with many other disciplines such as service level management, fault management and Riedl et al. (2009, 2008) offered a general model that integrates these aspects with the perceived quality perspective, i.e. how service users perceive QoS. However, the framework offer few details on or response time monitoring. With regard to resource usage, which is closely related to service response time, Almeida et al. (2006) proposed a method for optimizing the infrastructure usage of web services accessed over the internet. Although very relevant, this does not solve the problem of how to estimate service response times. Within software architecture, architecture analysis is often employed for QoS analysis and for instance Chen et al. (2010) employed an adaptation of the Architecture Tradeoff Analysis Method (ATAM), an established architecture analysis method, for QoS measurements to facilitate the adoption of SOA in a Fortune 50 company. However, the study provides little insight about response time analysis.

## 2.2. Service quality and performance in IT service management

Service quality and performance play an important role in IT service management, where it is discussed both from the perspective of the customer as perceived service quality and from the perspective the organization as part of capacity management and service level agreements.

The quality of service as perceived by customers is often measured by the SERVQUAL model (Parasuraman et al., 1985) which is a survey instrument that originated in the marketing community. SERVQUAL has been used to assess the quality of services provided by the IT department (Jiang et al., 2002). Models for perceived quality have been applied to IT services in general, see (Praeg and Schnabel, 2006) or services provided through the Internet, see e.g. (Zeithaml et al., 2002, Lee and Lin (2005)). However, measuring perceived quality through a survey offers little understanding regarding why services exhibit poor response time.

Both the COBIT (IT, 2007) and ITIL (Van Bon, 2007) frameworks describe capacity management processes. These deal with service response time management but offer little support on how to perform service response time analysis.

Buco et al. (2004) describes a system for how to uphold and describe service level agreements, including response time, but offers no methods for how to measure performance. Similarly, Hanemann et al. (2005) describes a framework for service fault management including QoS measurements but provides no assistance on how to perform this measurement.

## 2.3. Performance evaluation methods

With regard to pure performance evaluation methods Jain (1991) divides these into three categories: measurements, simulation-based methods and analytical modeling.

Measuring performance experimentally (Montgomery, 1991) yields the most accurate results (Jain, 1991), but these methods come with several drawbacks. In particular, these methods cannot be applied in the design stage as it is costly to collect the measurement data and design the experiments, and the information required to conduct the experiments properly is rarely available (Jain, 1991).

There are numerous performance simulation methods (Barber et al., 2002; de Miguel et al., 2000; Dunsire et al., 2005). Simulations require less time to complete than measurements and provide more accuracy compared to analytical methods (Jain, 1991). However, any performance simulation is a sizeable project and often requires simulation expertise (Jain, 1991).

Although analytical methods are less accurate than both measurements and simulations, they are cheaper to use and do not require the same level of expertise (Jain. 1991) This makes them well suited for providing rapid response time estimates Queuing theory (Allen, 1990) is the dominant analytical approach and can be applied in several manners, see e.g. (Buzen, 1973, 1976; Buchholz, 1994; Reiser and Lavenberg, 1980; Lam and Lien, 1983).

Turning to architecture-based methods for performance and response time analysis, analytical modeling methods have been used for architecture analysis and design, including Software Performance Engineering (SPE) (Smith and Williams, 2002) and SPE extensions, such as (Petriu and Wang, 2000).

In the field of architecture analysis for performance and response time analysis, most methods for the response time analysis are limited to a particular architectural layer. For instance, they focus on business processes (Van der Aalst and Van Hee, 1996), software applications. (Smith and Williams 2002) the infrastructure domain (Harrison and Patel 1992) or embedded systems (Demathieu et al., 2008). To be able to capture the response time of an IT service that is offered to the business and realized by applications residing in IT infrastructure, the architecture analysis must be able to integrate response time analyses across the business, application and infrastructure layers. One method with this ability was introduced by Iacob and Jonkers (2004, 2006). The method is based on queuing models and designed for response time assessments of services; it accounts for the business, application and infrastructure domains using the enterprise architecture language ArchiMate (Lankhorst et al., 2009). However, the method was not empirically tested with respect to accuracy or cost effectiveness. Furthermore, the original method is not formalized to the point where it can be implemented in a tool, thus diminishing its practical utility. To ameliorate this, the current study purports to formalize the method to allow implementation in a tool and to empirically investigate its accuracy and cost effectiveness.

## 3. Research design

This article presents the design and evaluation of an analytical method for modeling and estimating service response time based on enterprise architecture. A ‘method’ is a design science product that here is represented as an algorithm that can be used to perform a task based on a set of underlying constructs and a representation (March and Smith, 1995). Design science research is about building and evaluating IT artifacts (Hevner et al., 2004). The term design science originated with Simon’s ‘‘Sciences of the Artificial’’ (Simon, 1996) and considers the systematic and formalized creation of design artifacts to fulfill certain goals (March and Smith, 1995). By concerning itself with prescriptions that provide solutions to problems, design science differs from the more traditional sciences which deal with theories of how and why things are (Gregor and Jones, 2007). Below the method is first described as a design science product, and then the steps for developing and evaluating the method are presented.

A combination of concepts from Walls et al. (1992) and Gregor and Jones (2007) are used to describe the method as a design science product: meta-requirements (purpose and scope), meta-design (form and function). kernel theory (justifica: tory knowledge), and design product hypothesis (testable proposition).

The meta-requirements (Walls et al., 1992) of the research were to devise an analytical method for modeling and estimating service response time as (i) direct measurement is not always feasible, especially prior to service implementation and (ii) direct measurements can be very costly. The method should be accurate enough compared to direct measurement, relative to the goals it is used for, which may for instance be service capacity management. Moreover, the method should provide an overall service response time estimation taking into account elements from all enterprise architecture domains (business, application and infrastructure).

The meta-design (Walls et al., 1992) is based upon a formalization of Iacob and Jonkers’ method for the quantitative analysis of enterprise architecture using the Hybrid Probabilistic Relational Modeling (HPRM) formalism supported by a data collection approach based on expert assessments. The enterprise architecture metamodel employed in the method is based on the enterprise architecture language ArchiMate as presented by Lankhorst et al. (2009). Providing an underlying basis and explanation for the design of the artifact (Gregor and Jones, 2007) involves the identification of the appropriate justificatory knowledge or ‘kernel theory’ (Walls et al., 1992) – in this case queuing models and Little’s law as applied by Iacob and Jonkers (2004, 2006).

The testable proposition (Walls et al., 1992) for the artifact is heuristic (Gregor and Jones, 2007), i.e. on the form ‘‘If you want to achieve Y in situation Z, then something like action X will help’’. In this paper, the proposition is ‘‘If you want to perform an analysis of service response time and the direct measurement is not possible or too time-consuming, then the proposed EA analysis framework using interviews and surveys to collect input data could be used, as it yields reasonably accurate response time estimates’’.

The research process describing the development and evaluation of the method is outlined in Fig. 1 below. The first step consisted of a literature review of related work, which resulted in the identification of Iacob and Jonkers’ method for the quantitative analysis of enterprise architecture. This was followed by a formalization using the Hybrid Probabilistic Relational Modeling (HPRM) formalism. The formalization consisted of adapting and extending the relevant ArchiMate metamodel so as to make it possible to express the queueing models used by Iacob and Jonkers. The formalization was implemented in the Enterprise Architecture Analysis Tool (EAAT). Implementation was done in the metamodel module of the tool which provides an interface to capture metamodels with the HPRM formalism. A data collection approach to suit the method was also devised. These steps are described in more detail in the following sections.

There are a number of ways of evaluating artifacts, for instance through case studies, experiments, testing or other methods (Hevner et al., 2004). In this research, the evaluation consisted of comparing response time assessments from using the analytical method with response time measurements. Response time measurements serve as a good reference point when assessing the accuracy of the analytical method’s results (Jain, 1991). Studies within medicine have employed the same approach where one expensive yet accurate method is used to validate the accuracy of a less expensive one (Byass et al., 2010)

To compare the analytical method with response time measurements, five services of a Geographical Information System (GIS) used by a Swedish utility company were studied. The GIS exhibited some response time issues and the researchers could therefore employ the analytical method in a real case setting where expert assessments are available. The employment of the method consisted of architectural modeling, collecting data from experts via interviews and surveys, and an analysis using the data in the architectural model. These steps are described in more detail in the following sections.

The measurement of the response times consisted of a pilot study followed by experiments. A pilot study was conducted for the five GIS services to determine the approximate range of the response times as well as their likely probability distribution. All response times were measured using the standard settings. The pilot study was followed by experiments, as the utility company experienced poor performance of the GIS and wanted an analysis of the contributing factors. This allowed the researchers to conduct experimental studies for 3 out of the five GIS services involving multiple measurements to test which factors affected response time the most. Such experiments are recommended by Jain (1991) to obtain accurate response time measurements. The experiments could be performed on three out of the five services.

![](/api/attachments/TQEY3ZWM/fulltext/images/df367bbce0cd3ca13e4de31b2848787fd634edaf2c9ce3a35f2a7dd5ee2dcb10.jpg)  
Fig. 1. The overall research process activities and their output (the numbers in parenthesis refer to sections in the paper).

To determine the cost-effectiveness of the EA analysis approach, the number of person-hours spent applying the analytical method as well as performing the response time measurements was recorded. Based on the recorded data the costs of each study can be compared and the cost-effectiveness of the proposed method assessed.

## 4. Analysing service response time using enterprise architecture

This section will introduce the response time analysis method proposed by Iacob and Jonkers, briefly introduce the Hybrid Probabilistic Relational Modeling (HPRM) formalism, and describe how the method was formalized. The section is concluded with a short description on data collection.

## 4.1. An ArchiMate based performance analysis framework

The method developed by Iacob and Jonkers is based on ArchiMate, a mature EA modeling language (The Open Group, 2009a). A limited number of ArchiMate constructs are used:

\- Resources – structural elements that provide some sort of behavior, e.g. Nodes, Application Components or Business Roles.

\- Internal behavior – models of the internal behavior of resources, e.g. Application Function or Business Processes.

\- Service – the externally visible behavior, e.g. Business Services, Application Services or Infrastructure Services.

Furthermore, only the ‘‘realized’’, ‘‘used-by’’ and ‘‘access’’ relations are used for performance analysis. The following variables are used within the framework:

\- Response time R (s) – The time that it takes to complete one service request.

\- Processing time P (s) – The time that it takes for a behavior component to perform one service request including the time waiting for other services to complete their requests.

\- Arrival rate $\lambda ( s ^ { - 1 } )$ – Also known as workload, the number of service requests per second.

\- Weight n (no unit) – The average number of times that a ‘‘used-by’’ relation is called upon in one service request.

\- Arrival frequency f (s<sup>1</sup>) – The ‘‘local’’ arrival rate for each architecture component not including the arrival rate already derived from the overlying architecture components.

\- Capacity C (no unit) – The number of instances in which a resource is capable of managing requests simultaneously.

\- Utilization U (%) – The degree of utilization of a resource.

Response time is computed by employing Little’s law (Little, 1961) and queuing models. Queues for resource access are treated as independent from each other, which will introduce minor errors in the performance estimates (Iacob and Jonkers 2006).

The approach for workload estimation is top-down and begins with the arrival frequency stemming from the business layer, which is converted into arrival rates for the underlying components in the architecture. Based on the workload, the response times of the behavioral components and the utilizations of the resources can be determined in a bottom-up manner.

The arrival rate $\lambda _ { a }$ of (behavioral) node a is computed using Eq. (1). Here $d _ { a } ^ { + }$ is the number of outgoing relations to other components, i.e. components that uses or are realized by component a. $k _ { i }$ refers to one of the $d _ { a } ^ { + }$ child components of component a, i.e. those that use or are realized by component a. $\lambda _ { k _ { i } }$ refers to the child components respective arrival rates. $n _ { a , k _ { i } }$ is the number of times that $f _ { a }$ is the local arrival frequency of component a.

$$
\lambda_ {a} = f _ {a} + \sum_ {i = 1} ^ {d _ {a} ^ {+}} n _ {a, k _ {i}} * \lambda_ {k _ {i}}\tag{1}
$$

The utilization of resource r is found recursively using Eq. (2)

$$
U _ {r} = \frac {\sum_ {i = 1} ^ {d _ {r}} \lambda_ {k _ {i}} * T _ {k _ {i}}}{C _ {r}}\tag{2}
$$

where $d _ { r }$ is the number of behavioral components $k _ { i }$ that are assigned to the resource. The process time is computed as follows:

$$
T _ {a} = S _ {a} + \sum_ {i = 1} ^ {d _ {a} ^ {-}} n _ {k _ {i}, a} * R _ {k _ {i}}\tag{3}
$$

and

$$
R _ {a} = F (a, r _ {a})\tag{4}
$$

where $d _ { a } ^ { - }$ denotes the ‘‘in-degree’’ of node a, i.e. the number of parent components of component a that are either used by component a or realizing component a. $k _ { i }$ is a parent of $a , r _ { a }$ is a resource assigned to a and F is the response time of a expressed as a function of attributes of a and $r _ { a } ,$ to which we will return below. The internal service time $S _ { a }$ is taken to be a known constant for every behavior element.

It is assumed that the response time of an Application Service is the sum of the response times of its realizing Application Functions.

To compute the response time, a commonly used queuing model is the M/M/1 model, which assumes that the arrival rates follow a Poisson distribution, that the Service time is exponential and that a single server queue is used (Jain, 1991). Under these assumptions $R _ { a }$ becomes

$$
R _ {a} = F (a, r _ {a}) = \frac {T _ {a}}{1 - U _ {r _ {a}}}\tag{5}
$$

## 4.2. Hybrid probabilistic relational models

The Hybrid Probabilistic Relational Model (HPRM) formalism allows for the integrated modeling and probabilistic analysis of complex phenomena through the merger of entity relation models with Hybrid Bayesian networks (Närman et al., 2010). The HPRM formalism is an extension of the Probabilistic Relational Model (PRM) formalism (Friedman et al., 1999), which has been emploved for enterprise architecture analysis previously (Lagerström et al., 2009: Sommestad et al., 2010; Närman et al., 2011).

An architecture metamodel M describes a set of classes, ${ \mathcal { X } } = X _ { 1 } , \ldots , X _ { n } .$ Each class is associated with a set of descriptive attributes ${ \mathcal { A } } ( X )$ . Attribute A of class X is denoted X  A and its domain of values is denoted $V ( X \cdot A )$ . Each class also has a set of reference slots (relationships). The set of reference slots of class X is denoted RðXÞ. We use $X . \rho$ to denote the reference slot $\rho$ of class X. For example, the class Application Function may have the attribute ApplicationFunction.ResponseTime and a reference slot ApplicationFunction.Uses where the range is the class Infrastructure Service and the domain is the class Application Function. Each reference slot $\rho$ is typed with the domain type Dom $\vert \rho \vert = X _ { i }$ and the range type Range $\rho ] = X _ { j }$ , where $X _ { i } ; ~ X _ { j } \in \mathcal { X } . ~ \mathsf { A }$ slot $\rho$ denotes a function from $X _ { i }$ to $X _ { j } ,$ and its inverse $\rho ^ { - 1 }$ denotes a function from $X _ { j }$ to $X _ { i \cdot }$

A probabilistic relational model P specifies a probability distribution over all instantiations I of the metamodel M. This probability distribution is specified in terms of a Hybrid Bayesian network (Lauritzen, 1992) which are formed by a quali tative dependency structure and associated quantitative parameters.

The qualitative dependency structure is defined by associating with each attribute X  A a set of parents Pa(X  A) through so called attribute relations. Each parent of X  A is defined as $X \cdot \tau \cdot B$ where $B \in \mathcal { A } ( X . \tau )$ and s is either empty, a single reference slot q or a sequence of reference slots $\rho _ { 1 } , . . . , \rho _ { k }$ (called a slot chain) such that for all i, Range $\rho _ { i } ] = D o m [ \rho _ { i + 1 } ]$ . For instance, the attribute ApplicationFunction.ResponseTime could be affected by the attribute ApplicationComponent.Utilization through the attribute relation ApplicationComponent.IsAssigned. Considering the quantitative dependency, each attribute of the HPRM is seen as a node in a Hybrid Bayesian Network and thus has a probability distribution which is conditioned on that of its parents. This distribution is expressed in Hybrid Conditional Probability Tables (HCPT) defined as follows (Yuan and Druzdzel, 2007).

Definition 1. For every attribute A(X), its parents Pa(X) are divided into two disjoint sets: discrete parents $D P a ( A ( X ) )$ and continuous parents CPa(A(X)). Then, its HCPT $P ( A ( X ) _ { j } | P a ( A ( X ) ) )$ is a table indexed by its discrete parents DPa(A(X)) and with each entry representing one of the following conditional relations:

1. If A(X) is a discrete variable with only discrete parents, a discrete probability distribution.

2. If A(X) is a discrete variable with continuous parents, a discrete probability distribution dependent on CPa(A(X)).

3. If A(X) is a continuous and deterministic variable, a deterministic equation dependent on CPa(A(X)).

4. If A(X) is a continuous and stochastic variable, a deterministic equation dependent on CPa(A(X)) plus a noise term having an arbitrary continuous probability distribution with parameters dependent on CPa(A(X)) as well.

In the metamodel for service response times, we will confine ourselves to case 3 above, i.e. continuous relations only. This due to the fact that the variables were all continuous and the attributes were difficult to assess as stochastic variables.

## 4.3. An HPRM metamodel for performance analysis

The following discussion refers to the HPRM metamodel in Fig. 2 which shows classes, attributes and the dependency structure. Starting from the top, the class Business Process uses Application Service which is itself realized by Application Function. Application Function uses class Infrastructure Service to implement the functionality, these two classes are assigned resource classes Application Component and Node respectively.

![](/api/attachments/TQEY3ZWM/fulltext/images/67ba7bfd9d59f612a5018b7a6d0fa6be5ab4525f4c2119905f80d26207e2516a.jpg)  
Fig. 2. The HPRM for response time assessments.

Considering the dependency structure the attribute relations flowing top-down represent the workload relations as described in Eq. (1). The workload for the Business Process is equal to the arrival frequency and this workload is then propagated recursively through the Application Service, Application Function and Infrastructure Service.

The indirect relation from Business Process to Application Service defines that it is used, n times, by the Business Process. This property belongs neither to the business process nor the application service but rather on their relation. Since the HPRM formalism does not allow attributes on reference slots, we introduce the ‘‘help classes’’ Process Use Relation and Application Use Relation which have the attribute weight (n): the average number of times a service is used. The attributes of the Process and Application Use Relation classes perform the pair-wise multiplication of n and the workload of the overlying class. This is represented through the attribute weighted workload $\rho$ which is calculated as shown in Eq. (6) below.

$$
\rho_ {a} = n _ {a} \lambda_ {a}\tag{6}
$$

Eq. (1) thus reduces to

$$
\lambda_ {a} = f _ {a} + \sum_ {i = 1} ^ {d _ {a} ^ {+}} \rho_ {a, k _ {i}}\tag{7}
$$

Furthermore, the pairwise multiplication in Eq. (2) is managed through the introduction of the attributes Application-Function.Throughput and InfrastructureService.Throughput which are defined as

$$
\tau = \lambda_ {a} T _ {a}\tag{8}
$$

Eq. (2) is thus reformulated to become

$$
U _ {r} = \frac {\sum_ {i = 1} ^ {d _ {r}} \tau_ {k _ {i}}}{C _ {r}}\tag{9}
$$

This formalized model was then implemented into the Enterprise Architecture Analysis Tool (EAAT). The EAAT offers two interfaces: (i) in which metamodels can be created and modified to support whatever analysis the researcher wants to perform, in this case service response time and (ii) a modeling interface where the metamodel is instantiated into models containing the qualitative and quantitative elements required by the metamodel to complete the analysis. Once the models are complete, the modeler is able to perform inference using the HPRM formalism.

## 4.4. Data collection

The data collection approach is based on expert assessments of the attributes required for service response time estimates as outlined above. The assessments can be made using interviews and questionnaires. The approach entails first performing a qualitative modeling of the architecture and then eliciting quantitative estimates for the attributes required to compute service response time. The quantitative estimates concern both the workload and technical properties of the structure realizing the service.

To find respondents knowledgeable in the architecture and the quantitative attributes, some initial questions regarding the most suitable respondent should be posed to a number of people in the organization to single out the best expert for the task as recommended by O’Hagan et al. (2006). As for respondents concerning service workload, as many as possible of the current users should be included in the data collection. Workload estimates are elicited by a questionnaire sent to the service users. These answer questions about the workload and arrival rate.

To model the architecture, the respondent is trained on the concepts of ArchiMate during the first interview or in a premeeting. Training is recommended by Cooke (1991).

After the training but during the first interview, the respondent is asked to model the architecture together with the researcher. Next follows one or several interviews to assess the other quantitative attributes of the architecture – service time (S), weight (n), arrival frequency (f) and capacity (C).

In the following section, where we describe the application and testing of the method, more details about the data collection approach are provided.

## 5. Applying the method

The EA response time analysis method was employed to assess response times for a GIS application at a Swedish electrical utility company.

Initial interviews identified three GIS components to be of particular interest for evaluation purposes: a log-in component, a report handling component and a network calculations component. Because it was possible to log into and create reports pertaining to two different databases (one for district heating and one for the electricity and fiber optics network), five services suitable for analysis were identified: two services related to login, two services for reporting and one service for load calculations see Table 1.

## Table 1

Estimated (using both the M/G/1 and M/M/1 models) and measured response times for the five services. The two rightmost columns show differences between estimates and measured values.

<table><tr><td>No.</td><td>Service</td><td>Estimate M/M/1 (s)</td><td>Estimate M/G/1 (s)</td><td>Measured (s)</td><td>Difference measurement and M/M/1 (%)</td><td>Difference measurement and M/G/1 (%)</td></tr><tr><td>1</td><td>Log in (el. and fiber.)</td><td>70</td><td>66</td><td>73</td><td>4</td><td>9</td></tr><tr><td>2</td><td>Log in (district heating)</td><td>68</td><td>64</td><td>62</td><td>10</td><td>4</td></tr><tr><td>3</td><td>Report (el. and fiber.)</td><td>34</td><td>34</td><td>25</td><td>36</td><td>36</td></tr><tr><td>4</td><td>Report (district heating)</td><td>39</td><td>39</td><td>34</td><td>15</td><td>15</td></tr><tr><td>5</td><td>Load calculation</td><td>3.6</td><td>3.6</td><td>4</td><td>10</td><td>10</td></tr></table>

![](/api/attachments/TQEY3ZWM/fulltext/images/ab6e78181d9bc87d4ed3fc30c94a887974efa502b3bb854a675c25bad12ff89a.jpg)  
Fig. 3. The architecture underlying service 5, screenshot from the Archi tool.

## 5.1. Data collection

In-depth interviews were used to elicit data for the architecture modeling. The models for the three application components were created through three interviews with the head of the IT infrastructure department, who was singled out by the company as the most knowledgeable person in regard to service response time. The respondent was trained at the beginning of the first interview regarding the definitions of the ArchiMate language constructs and attributes. A questionnaire concerning the arrival frequency of the Application services was distributed to the 46 daily users of the GIS application (26 of which answered). All respondents were able to answer questions regarding the log-in and report components, but there was onl one user that could address the questions for the network calculation component. Thus, this information was collected through an interview instead of a survey.

The head of the IT infrastructure department was interviewed to elicit the values S, k, n and C for the architecture components that realized the five services. During the interview, it was assumed that all parameter settings of the GIS were configured according to the standard theme. The respondent provided confident replies for the attribute values of all services except the report generation with regard to district heating (service 3), which was not used as frequently as the other services. Below, we elaborate on the process used to estimate the response time of the load calculation (service 5).

## 5.2. Example model: network calculation application component

Before connecting new customers to the grid, various electric network properties must be calculated. This step is completed in the Business Process Connect new customer. The Application Service Load calculation new customer (service 5) offers the functionality of calculating the electric load given some estimated load profiles of the customers connected. Fig. 3 shows the architecture as drawn in the ArchiMate tool Archi.<sup>1</sup>

The Application Component Network calculation contains the Application functions Load Calculation and Download data for electricity and fiber optics. These functions run on a Node Local Client which realizes the Infrastructure Service Perform calculations. Finally, Download data for electricity and fiberoptics requires that the Infrastructure Service Database manager for electricity and fiberoptics must send a request to the Node Local server. The service response time was estimated to 3.6 s (See Fig. 4). The EAT tool (Buschle et al., 2010) was used for modeling and analysis (see Fig. 5).

## 6. Measuring service response times

Experimental design was utilized to obtain accurate service time measurements as recommended by Jain (1991). These measurements were used to validate the analytical framework’s accuracy and cost-effectiveness.

![](/api/attachments/TQEY3ZWM/fulltext/images/600c3c74989d80107e1f91fc795e734b90441c636d06fd7b5ef069f535d17f23.jpg)  
Fig. 4. An HPRM model of service 5. Data was collected for the grey attributes. All Use Relation weights were assessed by the respondent to 1. For readability, the Use Relations are not modeled explicitly here.

## 6.1. Pilot study

To assess the ‘‘normal’’ performance of the services, i.e., the approximate range of the response times and their probability distributions, a pilot study was conducted according to the recommendations of Jain (1991). There were no reliable log applications; thus, a manual stopwatch was used for the measurements. Ten samples were taken for each service over a certain time period, which was presumed to include significant changes of the network traffic. Recommended design tools were utilized for this task in the form of QQ plots.

## 6.2. Experimental study

Information from the pilot study was used to design three experimental designs. Complete two-level factorial designs using two replicates and fully randomized test runs were used. No experiments were performed for two of the studied services (Nos. 2 and 4) because the architecture underlying these services were very similar to those of the other studied services. The experimental designs were analyzed through QQ plots, ANOVA, regression analysis and the evaluation of model assumptions through an analysis of residuals.

The resulting regression models provided high degrees of fit. The factors that were found to have an impact on component performance (e.g. the choice of database or age of server) had a significance level of $p < 0 . 0 5$ , which was recommended by Warner (2008). The response time of the log-in service had an adjusted $R ^ { 2 }$ of 0.997, and the report service for electricity and fiber optics had an adjusted $R ^ { 2 }$ of 0.948.These values are high, but given that the experiments were undertaken on a rather simple architecture and that theories on response time in computer systems are quite well-established (Jain,

![](/api/attachments/TQEY3ZWM/fulltext/images/e29898ddae954f26063f2e601138fa8090a307d994ecdb4bef331b7d013e8e25.jpg)  
Fig. 5. A screenshot of a model from the EAT tool.

1991), they are not out of the ordinary. No problems regarding residual lack of fit were found, and thus, the model assumptions should not be rejected. The adjusted $\dot { R ^ { 2 } }$ of the Load Calculation service could not be evaluated because none of the factors appeared to influence the performance significantly

The resulting regression models provided high degrees of fit. Factors which were found to have an impact on component performance had a significance level of $p < 0 . 0 5 ,$ , which is recommended by Warner (2008), the response time of the log in service had an adjusted $R ^ { 2 }$ of 0.997 and the report service for electricity and fiber optics had an adjusted $R ^ { 2 }$ of $\phantom { - } 0 . 9 4 8$ . No problems regarding residual lack of fit were found, and thus the model assumptions should not be rejected. Adjusted $R ^ { 2 }$ could not be evaluated for the Load Calculation service, this since no factor seemed to significantly influence performance.

The resulting regression models were used as a point of reference to determine the accuracy of the estimates from the first part of the study. The factorial levels of the regression models were set as they were configured during the first study to obtain a comparable reference. For services 2 and 4, the averages from the measurements of the pilot studies were used as a reference for comparison purposes.

## 7. Results and likely sources of error

## 7.1. Results

The results of the analytical modeling with expert data and the measurements are compared in Table 1. The estimates were accurate, as they were within 15% of the measured values for services 1, 2, 4 and 5. There was a larger gap between the estimated and actual response time of service 3.

The cost, in person-hours, was recorded for both studies. Records of this were kept continuously, with book-keeping in Microsoft Excel being performed several times a day in conjunction with the data collection activities and measurements. The resulting spreadsheet contained a total amount of 93 posts, each containing information regarding the activity name, the date when performed, the time spent by the researcher, the time spent by the respondents, the activity type, the area (which study) and a text field for comments. The cost of creating the architecture model was considered to incur costs for both studies because the architecture model was used as an input for the pilot study. As is evident from Table 2, measuring the response times using experimental designs, as advocated by literature, took almost three times as long as using the proposed model.

## 7.2. Likely sources of error

The discrepancies between the measured and estimated values can be attributed to either estimates based on the analytical modeling with expert data or the validating measurements.The designed experiments were based thoroughly on the standard approach as presented by Montgomery (1991) and the parameters defined by Jain (1991). The measurement error arising from the use of a stopwatch was assessed in a number of randomized trials in which the stopwatch was used to time randomly generated alarms. The measurement error was found to follow a normal probability distribution with parameters $\mu = 0 . 2 7 5 8 s$ and $\sigma = { 0 . 0 4 7 2 6 7 s } ,$ , representing a fairly small error compared to the collected data.

A common threat to validity when discussing experiments is that one must control for many variables to obtain statistically sound results. The experiment in this study aimed to counter this issue through representative samples and a thorough pilot study. Furthermore, only factors that were found to have a strong causal effect on response time $\left( p < 0 . 0 5 \right)$ were included in the models. These factors in connection with a sufficient measurement tool reliability should provide an acceptable level of validity. These factors, combined with a sufficiently reliable measurement tool, should provide an acceptable level of validity. In conclusion, we believe that the measured data are very likely to be accurate.

Table 2  
The costs, in person-hours for the two studies.<sup>a</sup>

<table><tr><td rowspan="2">Activity</td><td colspan="2">Time spent</td></tr><tr><td>Respondent</td><td>Researcher</td></tr><tr><td>Qualitative model creation process (both studies)</td><td></td><td></td></tr><tr><td>Eliciting respondents and interviews</td><td>01:10</td><td>02:10</td></tr><tr><td>Modeling</td><td></td><td>07:16</td></tr><tr><td>Quantitative model creation process (expert assessments)</td><td></td><td></td></tr><tr><td>Creating, testing and scheduling interviews</td><td>00:35</td><td>05:45</td></tr><tr><td>Performing interviews</td><td>01:00</td><td>01:00</td></tr><tr><td>Performing experiments (measurements)</td><td></td><td></td></tr><tr><td>Planning tests</td><td>02:55</td><td>32:15</td></tr><tr><td>Pilot study</td><td>00:05</td><td>00:10</td></tr><tr><td>Main study</td><td></td><td>10:00</td></tr><tr><td>Handling and analyzing data</td><td></td><td></td></tr><tr><td>Expert assessments</td><td></td><td>03:00</td></tr><tr><td>Measurements</td><td></td><td>07:00</td></tr><tr><td>Summed up time</td><td></td><td></td></tr><tr><td>Expert Assessments</td><td>02:45</td><td>19:11</td></tr><tr><td>Measurements</td><td>04:10</td><td>58:51</td></tr></table>

<sup>a</sup> ‘‘Expert assessments’’ refers to the first study applying the method and ‘‘measurements’’ to the second study providing the measurements.

Table 3  
A comparison of response times (in seconds) for Application Functions of the third experimental study. The right-most column shows the difference in percent between the studies.

<table><tr><td>No.</td><td>Application Function</td><td>Estimated (s)</td><td>Measured (s)</td><td>Difference (%)</td></tr><tr><td>3.1</td><td>Display graphics</td><td>20.1</td><td>9.9</td><td>54.1</td></tr><tr><td>3.2</td><td>Download data (el. and fiber.)</td><td>7.5</td><td>5.6</td><td>27.3</td></tr><tr><td>3.3</td><td>Download shared map data</td><td>36.6</td><td>57.1</td><td>53</td></tr></table>

There are three likely sources of error that may explain the errors of the estimates for service 3: (i) a poor analytical framework, (ii) erroneous modeling, or (iii) poor performance parameter estimations by the respondents (Iacob and Jonkers, 2004) perhaps due to poor respondent knowledge or interviewer bias (Saunders et al., 2009).

The employed analytical frameworks include a number of simplifications in terms of connecting the queues. These simplifications may cause inaccuracies, but as was shown in Iacob and Jonkers (2004) these inaccuracies should be rather small (single digit percentage points). these inaccuracies should be rather small (single-digit percentage points). Additionally, an assumption was made concerning the single-server queuing model (M/M/1) to determine response times because the Application Components and Nodes in this study only involved single server queues. Furthermore, there was no prior knowledge about the process and service time distributions, and according to Jain (1991), the assumption of exponential distributions covers the majority of cases.

To determine the impact of the M/M/1 queue assumption, the results were compared with the results when assuming an M/G/1 queue instead. M/G/1 queues assume one server with Poisson-distributed arrival rates and service times that could assume any distribution. To determine the response time using these queuing models, the Pollaczek–Khinchine formula was employed as follows:

$$
R = \frac {U + \sigma^ {2} \lambda \mu}{2 (\mu - \lambda)}\tag{10}
$$

where $\mu$ is service rate, i.e. $S ^ { - 1 }$ , and $\sigma ^ { 2 }$ is the variance of the service rates.

The variance was not elicited in the study, but a reasonable estimate can be obtained by using the variances of the response time measurements from the pilot study. It was assumed that the respondents would err as much when estimating variances in service times as when estimating service mean times. Using these variances, new estimates were made, as shown in Table 1.

It is evident from Table 1 that the differences between the measured values and the estimates using M/G/1 queues are similar to those obtained from the M/M/1 queues. This observation is particularly true for services 3–5, where the differences between M/M/1 and M/G/1 are almost zero. The result is likely due to the rather low utilization (U) of the resource, particularly for services 3–5, which were used rather infrequently. Services 1 and 2, which are accessed daily and frequently, vary more when using the different queuing models because the high utilization of these services has a higher impact on the response time in the M/M/1 model. The differences between the M/M/1, M/G/1 and measured values are more or less the same in either case.

Based on the above findings, the following tentative conclusions can be drawn: (i) the choice of queuing models are likely to be more important when the length of the queues increase, and (ii) when workloads are rather low, as in this case, the choice of M/M/1 and M/G/1 queues does not appear to have a significant impact on the accuracy of the estimates.

Service 3 was used considerably less by the company than the other services, indicating that no one at the company had detailed knowledge about the service. Furthermore, report generation can vary substantially depending on the type of report being used, which may account for the greater variations. In conjunction with the experiments, measurements were made for the Application Function level (see Table 3). It is not likely that the magnitude of the errors of these observations stems from faulty theoretical assumptions. Thus, a combination of modeling errors and poor quantitative input data are the most likely candidates for explaining the greater deviation for service 3.

## 8. Discussion and conclusions

The aim of this paper was to develop a formalized analytical modeling method for rapidly estimating service response times without measurement by (1) expressing Iacob and Jonkers’ method for performance analysis in terms of the HPRM formalism. (2) coupling this method with a low-effort approach for data collection, and (3) testing whether the proposed method produces accurate response time estimates and is cost effective.

Iacob and Jonkers’ method was formalized using the HPRM formalism, implemented in a tool and applied by modeling three application components and five services of a GIS of a Swedish utility company. Data were collected from experts through interviews and questionnaires, thus addressing goals (1) and (2). Upon completion of the model-based study, an experimental study measured the exact response times of the five services. When comparing the results from the first and second studies, thereby determining whether goal (3) was met, the service response time estimates for four out of five services were found to differ by less than 15% from the true value, which represents a good approximation in terms of basic and indicative capacity planning. Regarding the cost of the analytical modeling method, it took approximately 22 h to apply the method and 63 man-hours to complete the response time measurements. Thus, as long as the desired accuracy is not greater than plus or minus 15%, the model-based method is preferable.

## 8.1. Contributions of this study

Two conclusions can be drawn from the study:

1. The proposed method can be used quickly to determine whether the as-is response time of a service is too low. A key strength of the method is that this assessment can be achieved based on expert assessments for individual components without having to implement expensive performance monitoring equipment.

2. The proposed method can be used to determine how architecture changes will affect response time, i.e., to predict to-be response time. The analysis can be performed based on expert assessments for individual components that are then grouped into different potential architectural to-be configurations.

For such purposes, an accuracy of several significant digits is not necessary. Indeed, ITIL Van Bon (2007) states that an accuracy within 15–20% of the actual values is typically satisfactory for response time measurements. When comparing potential to-be architectures, it could even be argued that several significant digits of service time do not exist because fundamental uncertainties about the architecture itself overshadow factors particular to response time. In this context, the approximate nature of the method poses no real limitation.

As for research contributions, there have been numerous studies published on the accuracy of various software prediction methods (see, e.g. (Molkken-stvold et al., 2008; Matson et al., 1994; Boehm et al., 2000)),but as far as enterprise architecture analysis is concerned, which spans the business, application and infrastructure layers, little has been published, with the notable exceptions of Lagerström et al. (2009) or Närman et al. (2011). In (Clements et al., 2002), the cost of performing architecture analysis using ATAM was investigated, but the accuracy of the results was not addressed. The empirical validation of the accuracy or cost of using these methods has been assessed by, for instance, Cox et al. (2009), but from a purely qualitative perspective. With regards to service management, the study augments the capacity planning process in ITIL service design and continual improvement (Van Bon, 2007), by being more specific in terms of how the analysis is performed.

Turning to modeling aspects, although the current study employed Archi- Mate as the basic language, the method is not constrained to ArchiMate per se. The main requirement for the language is that it clearly differentiates between resources and services and that it does so in several architecture layers. The TOGAF 9 content metamodel, for instance, would meet this requirement (The Open Group, 2009b). Additionally, while currently focusing on Application Services it is perfectly possible to extend the framework to also include Business Services as well thus making it applicable for business capacity planning (Iacob and Jonkers, 2004). Thus, the framework should be a convenient tool for architects when supporting Capacity Managers (Van Bon, 2007), Head of Operations (IT, 2007) or even business developers (Jambekar, 2000) in determining current or future capacity and performance.

## 8.2. Limitations and future work

The method yields approximate results, which means that as soon as the requirements for response time becomes business critical, as is the case for stock markets or online gaming servers, the precision is likely insufficient. However, companies in those industries already have mature capacity management practices and are not the primary target group for the method presented here. Furthermore, such companies could still use the method when making early stage design decisions for to-be enterprise architectures.

Regarding the cost estimations, the person-hours of architectural modeling were included for the analytical modeling study as well as the pilot study for the direct measurements. This is because the architectural modeling replaced the usual activities associated with gaining an initial understanding to be able to perform the pilot study. When the modeling activities are excluded from the person-hours for direct measurement, measurement would still require significantly more effort to perform; applying the method required approximately 22 h of which 10 h were architecture modeling. Measurements took 63 h including modeling. Excluding the modeling part would still mean that measurements required more than double the person-hours to complete. It should also be noted that this study equals cost and effort. If the measurements could be performed at lower hourly costs than the analytical method, then this could change the cost-effectiveness balance. This seems quite unlikely given that design of experiments for direct measurement is a complex undertaking.

When using the method in an as-is scenario, there are two limitations: (i) the service and its realizing components need to have been in operation for some time, and (ii) there must be knowledgeable respondents available.

When using the method in a to-be scenario, such as when wanting to compare alternative solutions, the scenario should preferably consist of components that have been deployed elsewhere, and the respondents must have experience with these components.

The testing of the method involved five services of a single application at a single company, mainly using estimates from a single respondent. These limitations make it difficult to make definitive judgments concerning the general accuracy or cost effectiveness of the method. Thus, the results should be interpreted as interesting and positive indications rather than conclusive proof of the method’s accuracy and resource efficiency, and more studies in different settings are needed. However, it is not uncommon in the design science paradigm to use single empirical studies as validation (see e.g., Becker, 2009 or Reussner et al., 2003).

Future studies should preferably vary the unit of analysis with respect to the following dimensions: (i) different sourcing of IT operations-when services are delivered by an external supplier, respondents may be more difficult to come by; (ii) the life cycle stage of the application-is it possible to use the method in, for instance, the design stage of the services?; (iii) type of application-some of the model assumptions, notably the queuing models and probability distributions, may be inapplica ble if applied to, for instance, applications featuring extensive parallel processing.

## References

Aier, S., Ahrens, M., Stutz, M., Bub, U., 2009. Deriving SOA evaluation metrics in an enterprise architecture context. In: Service-Oriented Computing-ICSOC 2007 Workshops. Springer, pp. 224–233.

Allen, A., 1990. Probability, Statistics, and Queueing Theory: With Computer Science Applications. Academic Pr.

Almeida, J., Almeida, V., Ardagna, D., Francalanci, C., Trubian, M., 2006. Resource management in the autonomic service-oriented architecture. International Conference on Autonomic Computing 1, 84–92. http://dx.doi.org/10.1109/ICAC.2006.1662 385.

Alwadain, A., Korthaus, A., Fielt, E., Rosemann, M., 2010. Integrating SOA into an enterprise architecture: a comparative analysis of alternative approaches. In: Proceedings of the 5th IFIP International Conference on Research and Practical Issues of Enterprise Information Systems (CONFENIS), Ministry of Education (Brazil)

Barber, K.S., Graser, T., Holt, J., 2002. Enabling iterative software architecture derivation using early non-functional property evaluation. In: Proceedings of the 17th IEEE International Conference on Automated Software Engineering, pp. 172–182.

Becker, S., Koziolek, H., Reussner, R., 2009. The Palladio component model for model-driven performance prediction. Journal of Systems and Software 82 (1), 3–22 [cityed by (since 1996) 72].

Boehm, B., Abts, C., Chulani, S., 2000. Software development cost estimation approaches: a survey. Annals of Software Engineering 10, 177–205, ISSN 1022- 7091.

Braun, C., Winter, R., 2007. Integration of IT service management into enterprise architecture. In: Proceedings of the 2007 ACM Symposium on Applied Computing, ACM, pp. 1215–1219. ISBN 1595934804.

Buchholz, P., 1994. A class of hierarchical queueing networks and their analysis. Queueing Systems 15 (1), 59–80.

Buco, M., Chang, R., Luan, L., Ward, C., Wolf, J., Yu, P., 2004. Utility computing SLA management based upon business objectives. IBM Systems Journal 43 (1), 159–178.

Buschle, M., Ullberg, J., Franke, U., Lagerström, R., Sommestad, T., 2010. A tool for enterprise architecture analysis using the PRM formalism. In: CAiSE2010 Forum PostProceedings.

Buzen, J., 1973. Computational algorithms for closed queueing networks with exponential servers. Communications of the ACM 16 (9), 527–531.

Buzen, J., 1976. Fundamental operational laws of computer system performance. Acta Informatica 7 (2), 167–182.

Byass, P., Kahn, K., Fottrell, E., Collinson, M.A., Tollman, S.M., 2010. Moving from data on deaths to public health policy in Agincourt, South Africa: approaches to analysing and understanding verbal autopsy findings, PLoS Med 7.

Chen, H., Kazman, R., Perry, O., 2010. From software architecture analysis to service engineering: an empirical study of methodology development for enterprise SOA implementation. IEEE Transactions on Services Computing, 145–160.

Clements, P., Kazman, R., Klein, M., 2002. Evaluating Software Architectures: Methods and Case Studies. Addison-Wesley, Reading, MA, ISBN 020170482X. Cooke, R., 1991. Experts in Uncertainty: Opinion and Subjective Probability in Science. Oxford University Press, USA.

Cox, K., Niazi, M., Verner, J., 2009. Empirical study of Sommerville and Sawyer’s requirements engineering practices. IET SOFTWARE 3 (5), 339–355.

Demathieu, S., Thomas, F., André, C., Gérard, S., Terrier, F., 2008. First experiments using the UML profile for marte. In: Object Oriented Real-Time Distributed Computing (ISORC), 2008 11th IEEE International Symposium on, IEEE, pp. 50–57.

de Miguel, M., Lambolais, T., Hannouz, M., Betgé-Brezetz, S., Piekarec, S., 2000. UML extensions for the specification and evaluation of latency constraints in architectural models. In: Proceedings of the 2nd international workshop on Software and performance. ACM, pp. 83–88.

Dunsire, K., O’Neill, T., Denford, M., Leaney, J., 2005. The ABACUS architectural approach to computer-based system and enterprise evolution. In: Proceedings of the 12th IEEE International Conference and Workshops on Engineering of Computer-Based Systems. IEEE Computer Society, p. 69 Proceedings of the 12th IFFE International Conference and Workshons on Engineering of Computer-Based Systems, IFFE Computer Society, p. 69

Erl, T., 2005. Service-Oriented Architecture: Concepts, Technology, and Design. Prentice Hall PTR.

Friedman, N., Getoor, L., Koller, D., Pfeffer, A., 1999. Learning probabilistic relational models. In: International Joint Conference on Artificial Intelligence: Stockholm, Sweden, vol. 16, Citeseer, pp. 1300–1309.

Gorla, N., Somers, T., Wong, B., 2010. Organizational impact of system quality, information quality, and service quality. The Journal of Strategic Information Systems. ISSN 0963-8687.

Gregor, S., Jones, D., 2007. The anatomy of a design theory. Journal of the Association for Information Systems 8 (5), 312–335

Hanemann, A., Sailer, M., Schmitz. D., 2005, Towards a framework for IT service fault management, In: Proceedings of the European University Information Systems Conference (EUNIS 2005), Citeseer.

Harrison, P., Patel, N., 1992. Performance Modelling of Communication Networks and Computer Architectures (International Computer. Addison-Wesley Longman Publishing Co., Inc., Boston, MA, USA.

Hevner, A., March, S., Park, J., Ram, S., 2004. Design science in information systems research. MIS Quarterly 28 (1), 75–105, ISSN 0276-7783.

Iacob, M.-E., Jonkers, H., 2004. Analysis of Enterprise Architectures, Tech. Rep., Telematica Instituut (TI).

Iacob, M., Jonkers, H., 2006. Quantitative analysis of enterprise architectures. Interoperability of Enterprise Software and Applications, 239–252.

IT Governance Institute, Cobit 4.1, 2007.

Jaeger, M., Rojec-Goldmann, G., Mühl, G., 2004. Qos aggregation for web service composition using workflow patterns.

Jaeger, M., Rojec-Goldmann, G., Gero, M., 2005. QoS Aggregation in Web Service Compositions.

Jain, R., 1991. The Art of Computer Systems Performance Analysis: Techniques for Experimental Design, Measurement, Simulation, and Modeling. Wiley, New York, ISBN 0-471-50336-3.

Jambekar, A., 2000. A systems thinking perspective of maintenance, operations, and process quality. Journal of Quality in Maintenance Engineering 6 (2), 123–132.

Jiang, J., Klein, G., Carr, C., 2002. Measuring information system service quality: SERVQUAL from the other side. MIS Quarterly, 145–166

Johansson, E., Ekstedt, M., Johnson, P., 2006. Assessment of enterprise information security: the importance of information search cost. In: Proceedings of the 39th Annual Hawaii International Conference on System Sciences, 2006. HICSS’06, p. 219a.

Kohlborn, T., Korthaus, A., Chan, T., Rosemann, M., 2009. Identification and analysis of business and software services: a consolidated approach. IEEE Transactions on Services Computing, 50–64.

Kohlmann, F., Alt, R., 2007. Business-driven service modeling – a methodological approach from the finance industry. In: Maciaszek, L.A., Abramowicz, W. (Eds.), Business Process and Services Computing (BPSC’07). Leipzig, Germany.

Lagerström, R., Franke, U., Johnson, P., Ullberg, J., 2009. A Method for creating enterprise architecture metamodels – applied to systems modifiability analysis. International Journal of Computer Science and Applications 6 (5), 89–120.

Lam, S., Lien, Y., 1983. A tree convolution algorithm for the solution of queueing networks. Communications of the ACM 26 (3), 215

Lankhorst, M. et al, 2009. Enterprise Architecture at Work: Modelling, Communication and Analysis. Springer-Verlag GmbH.

Lauritzen, S., 1992. Propagation of probabilities, means, and variances in mixed graphical association models. Journal of the American Statistical Association 87 (420), 1098–1108.

Lee, G., Lin, H., 2005. Customer perceptions of e-service quality in online shopping. International Journal of Retail & Distribution Management 33 (2), 161– 176.

Leymann, F., Roller, D., Schmidt, M., 2002. Web services and business process management. IBM Systems Journal 41 (2), 198–211.

Little, J.D.C., 1961. A proof for the queuing formula: L = kW. Operations Research 9 (3), 383–387, ISSN 0030364X.

March, S.T., Smith, G.F., 1995. Design and natural science research on information technology. Decision Support Systems 15 (4), 251–266, ISSN 0167-9236, http://dx.doi.org/10.1016/0167-9236(94)00041-2. <http://www.sciencedirect.com/science/article/pii/0167923694000412>.

Matson, J., Barrett, B., Mellichamp, J., 1994. Software development cost estimation using function points. IEEE Transactions on Software Engineering 20 (4), 275–287.

Molkken-stvold, K., Haugen, N., Benestad, H., 2008. Using planning poker for combining expert estimates in software projects. Journal of Systems and Software 81 (12), 2106–2117 [cited By (since 1996) 3].

Montgomery, D., 1991. Design and Analysis of Experiments. Wiley, New York.

Närman, P., Johnson, P., Lagerström, R., Franke, U., Ekstedt, M., 2009. Data collection prioritization for system quality analysis. Electronic Notes in Theoretica Computer Science 233, 29–42.

Närman, P., Buschle, M., König, J., Johnson, P., 2010. Hybrid probabilistic relational models for system quality analysis. In: Enterprise Distributed Object Computing Conference 2010, EDOC ’10: Vitoria, ES, Brazil. 14th International IEEE, IEEE.

Närman, P., Holm, H., Johnson, P., König, J., Chenine, M., Ekstedt, M., 2011. Data accuracy assessments using enterprise architecture, Enterprise Information Systems 5(1).

O'Hagan, A., Buck, C.. Daneshkhah, A., Eiser, I.. Garthwaite, P., Jenkinson, D., Oakley, I.. Rakow. T., 2006, Uncertain Judgements: Eliciting Experts' Probabilities. John Wiley & Sons.

Palmer, J., 2003. Web site usability, design, and performance metrics. Information Systems Research 13 (2), 151–167.

Papazoglou, M., Van Den Heuvel, W., 2006. Service-oriented design and development methodology. International Journal of Web Engineering and Technology 2 (4), 412–442, ISSN 1476-1289.

Parasuraman, A., Zeithaml, V., Berry, L., 1985. A conceptual model of service quality and its implications for future research. The Journal of Marketing, 41–50.

Petriu, D.. Wang, X., 200o. From UML descriptions of high-level software architectures to LON performance models. Applications of Graph Transformations with Industrial Relevance, 217–221.

Praeg, C., Schnabel, U., 2006. IT-service cachet-managing IT-service performance and IT-service quality. In: Proceedings of the 39th Annual Hawai International Conference on System Sciences, 2006, HICSS’06, vol. 2. IEEE, p. 34a.

Reiser, M., Lavenberg, S., 1980. Mean-value analysis of closed multichain queuing networks. Journal of the ACM (JACM) 27 (2), 313–322.

Ren, M., Lyytinen, K., 2008. Building enterprise architecture agility and sustenance with SOA. Communications of the Association for Information Systems 22 (1), 4.

Reussner, R., Schmidt, H., Poernomo, I., 2003. Reliability prediction for component-based software architectures. Journal of Systems and Software 66 (3), 241–252.

Riedl, C., Böhmann, T., Rosemann, M., Krcmar, H., 2008. Quality aspects in service ecosystems: areas for exploitation and exploration. In: Proceedings of the 10th International Conference on Electronic Commerce. ACM, 19.

Riedl, C., Böhmann, T., Rosemann, M., Krcmar, H., 2009. Quality management in service ecosystems. Information Systems and E – Business Management 7 (2), 199–221, ISSN 1617-9846.

Ross, J., Weill, P., Robertson, D., 2006. Enterprise Architecture as Strategy: Creating a Foundation for Business Execution. Harvard Business Press.

Saunders, M., Lewis, P., Thornhill, A., 2009. Research Methods for Business Students. Financial Times/Prentice Hall.

Simon, H., 1996. The Sciences of the Artificial. The MIT Press.

Smith, C., Williams, L., 2002. Performance Solutions: A Practical Guide to Creating Responsive, Scalable Software. Addison-Wesley, Boston, MA.

Sommestad, T., Ekstedt, M., Johnson, P., 2010. A probabilistic relational model for security risk analysis. Computers & Security, 659–679.

The Open Group, 2009a. ArchiMate 1.0 Specification

The Open Group, 2009b. TOGAF Version 9 ‘‘Enterprise Edition’’.

Ullberg, J., Lagerström, R., Johnson, P., 2008. A framework for service interoperability analysis using enterprise architecture models. In: IEEE International Conference on Services Computing.

Van Bon, J., 2007. Foundations of IT Service Management based on ITIL. Van Haren Pub.

Van der Aalst, W., Van Hee, K., 1996. Business process redesign: a Petri-net-based approach. Computers in Industry 29 (1–2), 15–26.

van Der Aalst, W., Ter Hofstede, A., Kiepuszewski, B., Barros, A., 2003. Workflow patterns. Distributed and Parallel Databases 14 (1), 5–51.

Walls, J., Widmeyer, G., El Sawy, O., 1992. Building an information system design theory for vigilant EIS. Information Systems Research 3 (1), 36–59. Warner, R., 2008, Applied Statistics, SAGE Publications

Winter, R., Fischer, R., 2007. Essential layers artifacts, and dependencies of enterprise architecture. Journal of Enterprise Architecture 3 (2), 7–18.

Yuan, C., Druzdzel, M., 2007. Importance Sampling for General Hybrid Bayesian Networks.

Zahedi, F., 1997. Reliability metric for information systems based on customer requirements. International Journal of Quality & # 38; Reliability Management 14 (8), 791–813, ISSN 0265-671X.

Zeithaml, V., Parasuraman, A., Malhotra, A., 2002. Service quality delivery through web sites: a critical review of extant knowledge. Journal of the academy of marketing science 30 (4), 362–375.

Zeng, L., Benatallah, B., Dumas, M., Kalagnanam, J., Sheng, Q., 2003. Quality driven web services composition. In: Proceedings of the 12th Internationa Conference on World Wide Web, ACM, pp. 411–421.
