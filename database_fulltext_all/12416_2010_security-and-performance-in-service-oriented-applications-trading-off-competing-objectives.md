---
otero_id: 12416
otero_key: "DDJXV3XC"
title: "Security and performance in service-oriented applications: Trading off competing objectives"
authors: "Hangjung Zo; Derek L. Nazareth; Hemant K. Jain"
year: "2010"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.09.002"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Security and performance in service-oriented applications: Trading off competing objectives

Hangjung Zo <sup>a</sup>, Derek L. Nazareth <sup>b,</sup>⁎, Hemant K. Jain <sup>b</sup>

<sup>a</sup> Department of Management Science, Korea Advanced Institute of Science and Technology, 335 Gwahak-ro, Yuseong-gu, Daejeon, 305-701, Republic of Korea <sup>b</sup> Lubar School of Business, University of Wisconsin–Milwaukee, P.O. Box 742, Milwaukee, WI 53201, United States

## a r t i c l e i n f o

Article history: Received 10 December 2009 Received in revised form 30 August 2010 Accepted 5 September 2010 Available online 16 September 2010

Keywords: Service-oriented computing Application composition Performance Security Multiple criteria decision making

## a b s t r a c t

As service-oriented computing becomes more prevalent, an increasing number of applications will be developed using existing software components with standard interfaces. These components may be developed in-house, may represent purchased software, or may involve vendor located leased services. The use of multiple services, possibly utilizing different technologies and different sources, has signi<sup>fi</sup>cant implications for the performance and security of these applications to support a business process effectively. Estimating performance and security in this distributed environment is a hard problem. This paper examines how performance and security measures can be developed for service-based applications. Business processes are broken down into constituent tasks and a formal mechanism is developed for deriving performance and security measures for the application. Given the competing nature of these two objectives, a tradeoff strategy is utilized wherein managers can trade improved performance for reduced security or vice versa. As the number of alternative services for each task increases, the composition problem becomes combinatorially explosive. A genetic algorithm approach is adopted to <sup>fi</sup>nd the Pareto optimal set of services that can be assembled to support the business process. An application to a real-world business process illustrates its effectiveness.

© 2010 Elsevier B.V. All rights reserved.

## 1. Introduction

As modern business environments have become more dynamic and competitive, many organizations need to be equipped with a more agile and <sup>fl</sup>exible IT architecture to respond to internal and external changes [45]. In the agile and <sup>fl</sup>exible IT architecture, serviceoriented computing (SOC) has been prevalent to develop a number of applications by composing services. Services refer to software constructs that support and deliver business functionalities over networks, and SOC indicates “a new computing paradigm that utilizes services as fundamental elements for developing applications” [32]. The paradigm of SOC enables organizations to de<sup>fi</sup>ne and execute business transactions across multiple business partners and enhance interoperability to compose business process with a plug-and-play capability, thereby organizations can easily build business service networks (BSNs) to implement collaboration and orchestration of business processes among business partners [3].

Papazoglou et al. [33] propose a research roadmap for SOC research. They identify three research planes including service foundations, service composition, and service management plane. They emphasize that semantics, non-functional characteristics of services, and quality of service (QoS) are permeating issues across all three research planes. Especially, QoS measures such as performance metrics, security attributes, reliability, availability, etc. play a vital role when services are selected and composed to build applications. Bichler and Lin [3] insist that QoS for a single service as well as end-toend QoS for business process are critical to compose services. Thus, QoS issues in selecting and composing services present signi<sup>fi</sup>cant challenges in SOC.

Among various QoS criteria, it is evident that performance, security, and reliability are the most signi<sup>fi</sup>cant and widely used measures for service assessment [45]. Performance indicates “a measure of speed in completing a service request” [34]. Although SOC offers <sup>fl</sup>exibility and reusability for application composition, increased communication between disparate providers may lead to deterioration in performance when service-oriented applications are executed. Service granularity and frequency of reuse need to be considered to enhance application performance — smaller services offer greater opportunity for reuse, but increase communication delays between services. Security is one of the most critical challenges in SOC because the applications with SOC are inherently distributed and network-oriented [11]. Numerous techniques and tools have been proposed to enhance security in SOC. Reliability is also an important QoS measure in SOC [46], as is accuracy [42], cost, and vendor reputation [45].

In an increasingly competitive environment, the ability to perform transactions quickly and reliably in a cost effective manner assumes greater importance. Distributed service-oriented applications assume a performance penalty, but may engender savings on other dimensions, in terms of cost to develop and use. These tradeoffs need to be weighed when considering performance of an application composed of multiple services provided by a host of vendors. In an increasingly networked world, coupled with greater threats to applications and their data, <sup>fi</sup>rms are focusing on security as a key component in application design. The push towards Web-enabled applications that can be accessed from a variety of non-traditional platforms accentuates the security issue even more. The use of multiple services, from a variety of providers, cobbled together through a patchwork of channels only exacerbates the situation. Nonetheless, security considerations for the entire application must be factored in when selecting services for application composition. A planning-based approach to service composition is presented in [23]. The approach uses service descriptions and constraints, and ignores most QoS measures. This study views QoS issues to be an integral part of service composition, and focuses on performance and security for selecting appropriate services to compose applications. This is not to suggest that the other dimensions are unimportant. Rather, they will play a role in the selection, though their relative importance will vary by application designer and application context.

Performance and security typically work against each other, in that efforts to make applications more secure frequently result in slower performance. The inverse relationship is not universally true, and it is possible to create examples involving poor security and performance, and vice versa. However, as a general rule, an emphasis on one objective typically entails some tradeoff on the other. Application designers and managers need to determine acceptable levels on both objectives when composing an application from existing Web services. Designers will have different preferences, depending upon the risk they are willing to tolerate, and the performance penalty that they are willing to incur. The application composition process should support this tradeoff between the competing objectives. This paper investigates application composition using available services guided by the twin and competing objectives of performance and security. It develops a formal mechanism for deriving measures for application performance and security. For large business processes with a wide selection of candidate services, the number of viable solutions becomes combinatorially explosive. The paper proposes a heuristic solution method using genetic algorithms to decide appropriate selection of services to compose agile applications, based upon designer preference between performance and security. The rest of the paper is organized as follows. Section 2 provides an overview of measures for performance and security, and adapts them to serviceoriented applications. Formal methods for deriving performance and security metrics, particularly in the context of business processes supported by services are provided. Section 3 describes the use of genetic algorithms as a heuristic search technique to the service selection problem using performance and security as pertinent objectives. Section 4 describes the application of this approach to a real-world example. Implications for managers and system architects are presented in Section 5. Limitations and conclusions round out the paper.

## 2. Measuring service-oriented application performance and security

Service-oriented application development requires that all system functionality be broken down into tasks or activities that can be effectively supported by simple or composite services, with wellde<sup>fi</sup>ned interfaces. Business processes are typically composed of tasks that performed in accordance with stated requirements. The interdependency between services and business process management has been acknowledged, in the research and practitioner contexts [7,44]. Realistic business processes will involve tasks that can be performed in parallel, or in lieu of other tasks, in addition to the tasks performed in a strict precedence. Some processes may involve looping and other structures. Traditional business processes typically represent a complex network of tasks that are linked using multiple combining options. The overall performance and security of the application are determined by the services selected to support each task as well as the manner in which these tasks are integrated into the process. Computing performance and security metrics for an application composed of existing services represent one challenge. Using these measures to select the services for the most appropriate composition is a different matter. The remainder of this section reviews performance and security metrics that are relevant to service-oriented applications and provides a formal mechanism for computing them within the context of generalized business processes. As a general rule, it is expected that any software metric should be simple, easily understood, quanti<sup>fi</sup>able, easily computed, reliable, and robust [27]. For application level metrics to meet these criteria, the underlying service level metrics should also conform to these criteria, and the combining rules should also yield usable metrics.

## 2.1. Software performance metrics

Several different metrics have been employed for assessing the performance of software artifacts. Common measures include throughput, response time [39], processing time, and processing delays [5], among others. Individual stakeholders tend to prefer different performance metrics since their objectives for assessing the software are not always the same. Throughput measures, which relate to the number of transactions processed per unit time, are preferred by software architects and architectural engineers. Application designers tend to favor response time metrics, as they provide a measure of how quickly a transaction can be attended to. Users are more interested in processing and delay time, since it represents the total wait that they experience before a transaction can be processed. Clearly, these measures are affected by a number of situational and contextual factors. Processing capacity, overall system load, implementation environment, communication linkages between requestor and provider, congestion in these linkages, handshaking, and protocols are but a few of the factors that will affect these metrics. For a given con<sup>fi</sup>guration, however, it is expected that performance metrics will be stable to some extent.

Performance metrics can be speci<sup>fi</sup>ed in a number of ways. A complete speci<sup>fi</sup>cation would include a distribution of likely values. However, these are not always easy to come by. More frequently they are typi<sup>fi</sup>ed by an average value and a range of expected values. License agreements frequently tend to use worst case estimates, with expected performance typically outperforming the worst case scenario. Though agreements also frequently specify reliability and quality measures, these represent other dimensions not directly related to performance.

## 2.2. Performance metrics for services

When transitioning to software as a service, the core performance measures remain the same. Since the application is now composed of a variety of distributed services, it is logical for developers to focus more on total processing time, including communication, delay, and on-site processing. However the con<sup>fi</sup>guration between requestor and provider will be quite different from an in-house deployment. There may be several hops between the client and server, including internal networks at both enterprises. Congestion in any of these components will increase the overall perceived processing time. Communication protocols add a layer of overhead to this. Security wrappers will cause further degradation. Utilization levels of each resource in the chain will determine service time at that resource. Nonetheless, an average response time can be computed for each service. For the purposes of application composition using services, the total processing time represents an appropriate performance metric for assessing alternative services to support a speci<sup>fi</sup>c task or activity within a business process [5].

## 2.3. Software security metrics

Software security metrics represent an area of considerable activity and <sup>fl</sup>ux. Over the last few years several attempts have been made to quantify the security associated with a software artifact. These measures range considerably in terms of their degree of formality, ease of collection, and utility. Corporate measures for software security abound, ranging from data collection, to assessment of vulnerabilities, to prevention of attacks. Most involve some form of weighted score that assesses vulnerability. Given that hard data is often dif<sup>fi</sup>cult to come by, the measures often employ subjective assessments on the part of evaluators. These include ordinal assessments of risk [12], and ordinal assessment of multiple vulnerability dimensions [25]. Other approaches advocate metrics based on counts, frequencies, and densities. While these techniques provide useful information about one aspect of a software asset, it does not adequately provide an aggregate assessment of the level of security. In an effort to obtain a larger picture on security for organizations, several different strategies have been advocated, including the use of scorecards based on counts and densities [30], classi<sup>fi</sup>cation and statistical analysis of security defects [13], and time series analysis of defect densities [13], among others.

The use of organized hierarchies to catalog, structure, and advocate for security metrics is also evident. One approach calls for assessment of security throughout the software development life cycle using a series of ratios and densities [41]. A top-down strategy that uses security objectives to drive security policies and security metrics is suggested in [43]. A structured taxonomy of security metrics based on metric type is developed and presented in [37] and adapted for the information and communication industry in [36]. An alternative taxonomy of security metrics for process control systems that is organized along the lines of organizational and technical metrics is presented in [24]. A more complete taxonomy using families of metrics that are organized along the lines of organizational, operational, and technical metrics is presented in [40]. Efforts to assess an organization's capability to collect and manage security metrics have been proposed. These include the Systems Security Engineering Capability Maturity Model [20], and the information security measurement program [8].

Given the wide range and applicability of security metrics, it is not surprising that there have been calls to provide more direction for research in security metrics [21]. There are also contrary views that assert that security metrics for software are infeasible [2]. Despite the disagreement, measures for security remain essential, in that assessment of security for software assets would be problematic in their absence.

## 2.4. Security metrics for services

Security measures for services suffer from the same ambiguity and inconsistency. A wide variety of measures have been used to evaluate services, including percentage compliance on authentication, nonrepudiation, con<sup>fi</sup>dentiality, integrity, and availability [38]. The use of radar graphs to evaluate the security of individual services vis-à-vis management targets for security is proposed in [38].

Typically, security speci<sup>fi</sup>cations for the use of a service are written into a service level agreement with the vendor. These agreements could specify restrictions on access, prevention of data tampering and eavesdropping, encryption, data backup, denial of service, business continuity, compliance with security standards, and the like. They may also specify procedures for noti<sup>fi</sup>cation in cases of security breaches, warranties and remedies for both parties, and legal options available to the client. However, quantitative security measures may be hard to incorporate into the agreements [16].

When assessing security for services, end-to-end surety should be emphasized. Given that the service may be provided at a remote location, the end-to-end security is a function of the connection between the requestor and service provider, the security mechanisms in place at the provider (including hardware and software provisions), and the internal security within the provider's infrastructure. Several security risks are easy to overlook [11]. On the other hand, it has been suggested that security could be an enabler for Web services, though it is acknowledged that the use of Web services bring in added security concerns [15]. Using a core set of security services that center around authentication, authorization, cryptography, accountability, and administration, coupled with a set of vendor provided security services, enterprise applications created using Web services can be made more secure [15]. Other provisions for securing services center on the use of communication protocols like SOAP to improve security (WS-Security reference). For applications that are assembled using services, the overall attackability has been employed as a security metric [22].

## 3. Service-oriented application performance and security

For the purposes of this research, performance is measured in terms of total task completion duration, given the service chosen. This represents an end-to-end measure, and includes times for local processing, communication, and service processing, as illustrated in Fig. 1. In this case, the duration associated with processing task i with service j is given by:

$$
D \left(t _ {i j}\right) = D _ {I N} + D _ {E N} + D \left(s _ {j}\right)\tag{1}
$$

where $D _ { I N }$ represents the duration within the internal network, $D _ { E N }$ represents the duration associated with communicating with the vendor (both request and response), and $D ( s _ { j } )$ represents the service processing duration at the vendor. If the service is locally hosted, then this expression can be modi<sup>fi</sup>ed appropriately. If multiple services are available to perform the task, then the performance metric is given by the minimum value of the competing services, using the reasoning that fast services are preferred.

For the purposes of this research, security is measured as a ratio of the number of transactions not compromised by security breaches to the total transactions processed by the service provider. From an application designer's perspective, this is a more meaningful measure than the metrics based on attacks, vulnerabilities, and the like. The use of transactions as a basis for measuring security grounds the metric in the local context. This metric is assembled using data from the service provider. As with any measure of security, it is fraught with possible concerns. At the outset, self reported measures must be viewed with some caution. While the tendency to underreport breaches is expected, a vendor can hardly establish a solid reputation for security on the basis of misleading information. Attempts to cover up problems often result in larger credibility issues when the true extent of the problem eventually surfaces. A second concern represents the accuracy of the metric. Not all security breaches may be detected. This has the unintended consequence of in<sup>fl</sup>ating the security metric. Not all breaches have the same impact. Eavesdropping on a transaction has a different impact from changing the data in a transaction, or generating bogus transactions. Compensating for this would require some measure of the severity of the breach and a weighted averaging strategy for utilizing this information. Alternative measures and surrogates include the frequency of breaches, the dollar value of the breaches, down-time experienced by breaches, and the like. Some of these may be harder to come by, and may not be indicative of the true level of security, but represent the impact of the absence of adequate security instead. As such, the metric currently employed is acknowledged to have limitations, but is practical in many respects. First, it can be easily assembled using objective data. It is a simple metric that is easily grasped by decision makers, who can relate to it at a practical level. It is relatively robust and not prone to massive shifts. The use of a ratio compensates for disproportionate use of alternative services and provides a more meaningful basis for comparison.

![](/api/attachments/DDJXV3XC/fulltext/images/3799ad579b27c666e841855fa99ed50f93460b2a58b81ebf5ed2a78c6d130097.jpg)  
Fig. 1. End-to-end performance and security.

Many principles guide the evaluation of security of services, including conservatism in defaults, minimization of privileges, and weakness of links. The <sup>fi</sup>rst argues for granting no privileges as the default option, much like a shared database with multiple users. The second restricts user access to the minimum privileges needed to perform their tasks, in an effort to curtail damage through compromised user accounts. The last asserts that security of the composite is shaped by security of the weakest link in the chain of tasks that constitute the composite. Adopting the third strategy generates a conservative, but more acceptable measure for security of services. Accordingly, the security associated with processing task i with service j is given by:

$$
S \left(t _ {i j}\right) = \min \left(S _ {I N}, S _ {E N}, S \left(s _ {j}\right)\right)\tag{2}
$$

where $S _ { I N }$ represents the security within the internal network, $S _ { E N }$ represents the security associated with communicating with the vendor, and $S ( s _ { j } )$ represents the security associated with the service at the vendor. If the service is locally hosted, then this expression defaults to $S _ { I N } .$ If multiple services are available to perform the task, then the security metric is given by the maximum value of the competing services, using the reasoning that the most secure service will be selected.

## 3.1. Application composition using business process patterns

Business processes are typically divided into tasks that follow some organized pattern of completion. Simple processes are likely to exhibit a sequential pattern. However, in general, a business process may represent a complex network of tasks that are linked using multiple combining options including sequential, parallel, selection, or looping structures. The use of distinct services to support each task in this network will affect the performance and security associated with the application that supports the process. Clearly, the performance and security will be determined by the characteristics of the individual services and the manner in which they are integrated into the enterprise application. Deriving measures for performance and security for the application requires that appropriate combining functions be derived for the chosen performance and security metrics.

Relationships between tasks that constitute a process can be depicted in a variety of mechanisms. Flow graphs have been used to describe processes supported by Web services [19]. In the SOA security context, user system interaction effect graphs have been proposed [22]. Process modeling and work<sup>fl</sup>ow management techniques provide a host of representations for processes. However, while these representations are effective in terms of depicting process structure, they do not intrinsically support security and performance measures. The performance and security metrics discussed earlier need to be overlaid on the selected representation, in a manner that permits the computation of aggregate security and performance metrics for the process. This paper draws upon prior research in business process modeling that uses a number of distinct patterns for combining tasks into business processes [1,35]. These patterns seek to provide a comprehensive speci<sup>fi</sup>cation of business processes in a formal manner. From a practical standpoint, most business processes can be speci<sup>fi</sup>ed using a relatively small subset of these patterns. This research proposes the use of six combining patterns, representing one sequence, three parallel, and two loop structures. Speci<sup>fi</sup>cally, these patterns are sequence; parallel-AND, parallel-XOR, parallel-OR, simple loop, and composite loop. Performance and security metrics are derived and presented for each of these patterns. The patterns are illustrated using BPMN notation [31].

## 3.2. Performance and security computation using patterns

Several different combining functions have been proposed for assessing performance and security of applications supported through multiple services. In the case of performance metrics, a model that is based on average performance is provided in [19]. This model generates an upper bound estimate based on performance times and frequency of invocation of services, based on a <sup>fl</sup>ow graph of all services. It is assumed that all services are necessary, and there are no cases involving multiple competing services. An alternative approach that permits the use of competing services through the use of an OR combination, as well as loops in services is presented in [5]. In this case, performance is modeled as task response time, which is measured in terms of task processing time and task delay. Combining functions are provided for sequence, parallel-AND, parallel-OR, and simple and composite loops. Our research extends this to include parallel-XOR cases as well.

Combining security metrics is acknowledged as a challenge. Several approaches to measuring security present multiple metrics, but provide little composite information. In [38], security metrics for multiple services are presented as a radar graph, with a simple average used to assess overall security. Likewise, in [30], a security scorecard is presented detailing current and trend information about multiple dimensions of security, with a simple average used for overall security assessment. One approach that seeks to combine security metrics involves the use of risk trees and vulnerability assessments [9]. In this case, the primary mission of the organization/ application is broken down into objectives, sub-goals, and eventually is linked to assets. Relative weights for each sub-tree and the vulnerabilities associated with each asset are used to compute an overall risk for the mission. A similar approach to combining objectives is presented in [17]. This approach uses dependency graphs, and employs AND–OR patterns. In this case, the combining mechanisms use minimum and maximum functions. Metrics for individual tasks are derived as a percentage of events <sup>fl</sup>agged in the audit log to the total number of events. Since neither approach provides a formal mechanism for deriving security metrics within all chosen patterns, this research provides a new set of combining rules that extends prior work in the area.

## 3.2.1. The sequence pattern

The sequence pattern represents the simplest and most common way in which tasks are related in a business process. This pattern assumes that a task will be initiated only after the completion of its predecessor. The precedence is typically shaped by a temporal, communication, information, or resource dependence between the tasks. Assuming independence between tasks, the performance of the sequence is given by the sum of the individual performance measures, assuming no delays between the completion of a task, and the invocation of the successive task. In the case of security, based on the weakest link principle, the security is given by the minimum security afforded by each individual service. This is illustrated in Fig. 2a.

## 3.2.2. The parallel-AND pattern

The parallel-AND pattern represents a common pattern in business processes, wherein several tasks need to be performed independently, and all tasks must be completed before any successor tasks can be initiated. For example, checking product availability, assessing customer creditworthiness, and determining shipping feasibility, represent tasks that must precede order acceptance, but can be performed independently and simultaneously. If the same resources are needed for all tasks, this may preempt parallel execution. Assuming separate services for each task, the overall performance for this pattern is given by the maximum performance value for individual services. For the case of security, since all tasks must necessarily be performed, the overall security metric is given by the minimum value for the parallel tasks, as illustrated in Fig. 2b.

## 3.2.3. The parallel-XOR (conditional) pattern

The parallel-XOR or conditional pattern is one that is common in many business processes where a task can be completed in several ways, but only one is typically employed. Processing a payment may involve payment by cash, check, or credit card, any one of which can satisfy the task requirements. These options could be supported through a single service, but are more likely to utilize different services as they access distinct external processors. The frequency of invocation is bound to be different among these options. However, historical data will provide relative frequencies, with probabilities summing to 1. The performance metric represents a probability weighted measure of their relative task completion times. Security will also be computed in a similar fashion. This is illustrated in Fig. 2c.

Note that this pattern assumes an invocation of exactly one task, and does not permit multiple or repeated invocations.

## 3.2.4. The parallel-OR pattern

The parallel-OR pattern is present in business processes, though not quite as commonly. Typically, this involves a task that uses multiple sources of information, all or some of which may be suf<sup>fi</sup>cient to complete the task. Determining creditworthiness of a customer is an example. It may involve a review of customer payment history, or an external credit check. In some cases, both options may be pursued, assuming that one yields insuf<sup>fi</sup>cient results. From a business process perspective, the key difference between the XOR and the OR patterns is that the XOR pattern is usually transaction dependent and is externally speci<sup>fi</sup>ed, while the OR pattern is internally selected. For the situation involving a true selection that is not externally mandated, the expected performance metric represents the quickest task to complete the process, using the logic that the fastest service is the preferred option. Likewise, for the security metric, the combined security should be the maximum value, based on the notion that the most secure process should be selected, when there is a choice. The combining functions for performance and security in the parallel-OR case are illustrated in Fig. 2d.

## 3.2.5. The simple loop pattern

Business processes frequently include loop patterns in the tasks performed. Loops could involve a single task, termed a simple loop, or multiple tasks, termed a composite loop. The single loop case occurs when there is sustained invocation of the task, due to need for multiple transaction components, or due to unsatisfactory performance on a prior invocation. An example of the former would be checking product availability for multiple products on an order. In effect, this pattern amounts to a special case of the sequence pattern, and the measures for performance and security are derived from the sequence formulation. The latter case is more interesting, and the invocation of a second instance occurs only when the <sup>fi</sup>rst fails. An example would be a directive to ship from a second warehouse, when the preferred warehouse is unable to ship the product. In this case, the service will be invoked more than once, with a probability illustrating the likelihood of multiple invocations. The performance measure for the simple loop pattern is given by

$$
D = (1 - p _ {1}) D (t _ {i}) + 2 p _ {1} (1 - p _ {1}) D (t _ {i}) + 3 p _ {1} ^ {2} (1 - p _ {1}) D (t _ {i}) + \ldots\tag{3}
$$

where $D ( t _ { i } )$ represents the completion time for task i and $p _ { 1 }$ represents the probability that the task will be re-invoked. This can be repackaged as:

$$
D = (1 - p _ {1}) D (t _ {i}) \sum_ {n = 0} ^ {\infty} (n + 1) p _ {1} ^ {n}\tag{4}
$$

or more succinctly, as

$$
D = \frac {D (t _ {i})}{(1 - p _ {1})}.\tag{5}
$$

The composite security measure for a service that is invoked more than once is the minimum of all these invocation, which is the measure for the service itself. These are illustrated in Fig. 2e.

## 3.2.6. The composite loop pattern

The composite loop pattern involves multiple tasks, and represents a cycle in the business process. As with the single loop, the cycle can be invoked multiple times, but there must be clear entry and exit conditions. This pattern is often observed when an error is detected in the processing, and a separate correcting task is invoked. The revised transaction will need to be validated again, with potential erroneous situations detected once again. Inclusion of a non-existent product on an order, use of an expired credit card, etc. will trigger an error that needs a corrective task and a revalidation. As with the simple loop case, knowledge of a priori probabilities for multiple invocations of the tasks in the cycle is necessary for effective estimation of security and performance metrics. The composite performance measure can be derived using the simple loop formula, with the caveat that the corrective tasks may not need to be performed in some cases, and is given by:

![](/api/attachments/DDJXV3XC/fulltext/images/2888710a66df03bddaf3eac931839b7e97d2464a6df84853bd9fe6016b68e487.jpg)  
Fig. 2. a. The sequence pattern. b. The parallel-AND pattern. c. The parallel-XOR pattern. d. The parallel-OR pattern. e. The simple loop pattern. f. The composite loop pattern

$$
\begin{array}{c} D = (1 - p _ {1}) D (t _ {i}) + 2 p _ {1} (1 - p _ {1}) \Big (D (t _ {i}) + D \Big (t _ {j} \Big) \Big) \\ + 3 p _ {1} ^ {2} (1 - p _ {1}) \Big (D (t _ {i}) + D \Big (t _ {j} \Big) \Big) + \ldots \end{array}\tag{6}
$$

where $D ( t _ { i } )$ represents the completion time for the original task $i , D ( t _ { j } )$ represents the completion time for the correct task j, and $p _ { 1 }$ represents the probability that the corrective task will be invoked. This can be repackaged as:

$$
D = (1 - p _ {1}) \Bigl (D (t _ {i}) + D \Bigl (t _ {j} \Bigr) \Bigr) \sum_ {n = 0} ^ {\infty} (n + 1) p _ {1} ^ {n} - D \Bigl (t _ {j} \Bigr)\tag{7}
$$

or more succinctly, as

$$
D = \frac {D (t _ {i}) + D (t _ {j})}{(1 - p _ {1})} - D (t _ {j}).\tag{8}
$$

For assessing the composite security measure, the loop can be expanded into a potentially in<sup>fi</sup>nite sequence, which would lead to the minimum value being selected, as illustrated in Fig. 2f.

3.3. Deriving performance and security measures for applications composed of services

Business processes can be represented as a set of tasks that are arranged using any combination of the six patterns, provided that the patterns are wholly nested within each other. Deriving performance and security metrics then becomes an application of these combining functions, based on the underlying process structure. The Software Reduction Algorithm [4,6] has been proposed as a mechanism for computing quality of service measures for a process. In this approach adjacent tasks are coalesced into composite tasks using combining functions similar to those employed in the prior section. It works well for the computation of quality of service metrics for a single solution. However, repeated application of this approach for the large number of possible solutions encountered in service selection proves inef<sup>fi</sup>cient. Instead, this research elects to create a symbolic expression for the combined performance and security of an application composed of services, using the functions presented in the earlier section, based on the process representation using the speci<sup>fi</sup>ed patterns.

## 4. Application composition using services

A major impetus to the adoption of service-oriented computing is the ability to assemble robust applications using a set of available services. The availability of services is critical in this context. If only a few services are available, then application designers have few opportunities to trade off different objectives when assembling the application. Assuming that a reasonable number of viable services exist for each task, a likely scenario as the marketplace develops, the composition of the application includes a signi<sup>fi</sup>cant selection effort. Selection of a service for a task requires that all functional requirements for the task be met before the service can even be considered as a candidate. Issues like cost, vendor reputation, reliability, performance, and security represent non-functional requirements that must be addressed as part of the selection. In addition, technical issues like orchestration and choreography must be addressed to ensure that effective interfacing is possible between related services. Several standards for web service choreography have been proposed, using a range of coupling [29]. Selection of services cannot focus on individual tasks alone, but must consider all tasks in the application. Given that the non-functional objectives are con<sup>fl</sup>icting in nature, the software architect's preferences need to be incorporated into the selection of services. These tradeoffs need to be clearly articulated for an appropriate selection of services to be made. This paper focuses on performance and security as criteria for selecting appropriate services and seeks to explicate the complexities that entail in this approach to application development. Clearly performance and security are expected to be at odds with each other, i.e. a more secure service may not perform quite as quickly.

## 4.1. Service selection problem complexity and solution approaches

The service selection problem is potentially combinatorially explosive. For a set of m tasks, each of which can be supported by n services, the total number of viable combinations is given by $n ^ { m }$ . For a complex process supporting 40 tasks with an average of 8 Web services available to support each task, this translates to 8<sup>40</sup> solutions, or approximately $1 . 3 \bar { 3 } \times 1 0 ^ { 3 6 }$ . Clearly an exhaustive search among these alternatives is infeasible. Decomposition of the problem may provide some relief in this context. This assumes relative independence between the sub-problems. For the service selection problem, this translates into little to no overlap among services across different sub-processes. If the above process was decomposed into 4 separate sub-processes of equal size, then the number of solutions to be explored is $4 \times 8 ^ { 1 0 } ,$ , or approximately $4 . 2 9 \times 1 0 ^ { 9 }$ , which is clearly more manageable. It is unlikely that a process will be decomposed into equal length sub-processes. With a slightly skewed decomposition, where one sub-process contains up to half the tasks, the search space increases to an unmanageable $1 . \dot { 1 } 5 \times 1 0 ^ { 1 8 }$ solutions. As a simpli<sup>fi</sup>cation strategy, decomposition cannot be reliably counted upon to make the problem size tractable. However, it does provide some relief. This paper employs decomposition on the basis of semantic content, i.e. the process is decomposed into separate sub-processes using functional, temporal, and user characteristics. It is acknowledged that decomposition will likely result in a sub-optimal solution.

Mathematical programming approaches represent one option for locating the ideal solution. The sheer size of the problem, combined with non-linear and discontinuous metrics for performance and security, would appear to rule out mathematical programming as a viable approach for the service selection problem as currently formulated. Instead, a satis<sup>fi</sup>cing approach may be preferable. Several heuristic solution techniques are available, including genetic algorithms, particle swarm optimization, and ant colony optimization, among others. In light of the many dimensions being considered, and the size of the problem space, this paper examines the use of genetic algorithms to effectively address the selection problem. The genetic algorithm approach is an adaptive search technique based on principles of natural evolution and heredity. Since its initial development by Holland [18], it has been widely used in variety of areas including machine learning, genetics, economics, social systems, etc. [10,14,26]. Generally, genetic algorithms are considered appropriate methods for solving a problem in a space that is too large to be searched exhaustively, is not smooth and unimodal, or not wellunderstood. In addition, if the evaluation function is noisy, or if a non global optimum solution is acceptable, genetic algorithms will provide satisfactory solutions [28].

Genetic algorithms represent a computational equivalent of an adaptive system based on biological principles of evolution and selection of the <sup>fi</sup>ttest. Candidate solutions to the problem are encoded as chromosomes (typically a binary representation of 0's and 1's), and an initial population of solutions is generated randomly. Solutions are evaluated using a prede<sup>fi</sup>ned <sup>fi</sup>tness function that unequivocally assigns a numeric value to each solution. An equal number of new candidate solutions are generated from this population, using random pairing of solutions, coupled with crossover and mutation functions. Crossovers specify how parent solutions are combined to form offspring solutions, and mutations introduce variations from expected pairings. These new candidate solutions represent the next generation of the population, and can be selected using the <sup>fi</sup>tness function to retain preferred solutions. The process repeats for a <sup>fi</sup>xed number of generations or until a prede<sup>fi</sup>ned threshold is met on the <sup>fi</sup>tness function. Though not guaranteed to generate an optimal solution, genetic algorithms perform well in a number of applications. Applying genetic algorithms to the service selection problem requires careful attention to problem representation, initial population generation, robustness of the evaluation function, tradeoff among competing objectives, and genetic transformation to generate new solutions.

## 4.2. Application to a drop-ship example

To validate the proposed approach and demonstrate its utility we applied it to a case study involving the direct-to-customer drop-ship retail process. This represents a retail business model in which products are shipped directly to a customer from a direct supply vendor based on orders placed with an on-line retailer, and is a typical business processes in the on-line retailing area. The process involves multiple business partners, including the customer, retailer, direct supply vendor, credit authority and a transport carrier. It comprises multiple data <sup>fl</sup>ows between the business partners. The drop-ship process comprised 34 tasks, and utilized an average of 14 services per task. This put the total number of viable solutions at $4 . 3 2 \times 1 0 ^ { 3 7 }$ Clearly the problem was too large to solve using exact solution techniques. Adding to the complexity was the fact that some services could be used to support multiple tasks. Based on the semantics of the process, the overall process was decomposed into four sub-processes involving customer identi<sup>fi</sup>cation, sales order processing, purchase order management, and shipping, and is depicted in Fig. 3.

In this case the sub-processes consisted of 4, 14, 6, and 10 tasks with 24, 33, 33, and 57 candidate services respectively. Since a genetic algorithm formulation may entail a few additional bits in its representation, not all solutions are feasible. The decomposition yielded $3 . 3 2 \times 1 0 ^ { 5 } , 1 . 8 2 \times 1 0 ^ { 2 1 } , 1 . 2 9 \times 1 0 ^ { 9 }$ , and $3 . 6 2 \times 1 0 ^ { 1 7 }$ possible solutions, and a separate computation indicated $1 . 0 5 \times 1 0 ^ { 5 } , \dot { 3 } . 2 1 \times 1 0 ^ { 1 3 }$ , 8.20× $1 0 ^ { 6 } ,$ and $1 . 5 6 \times 0 ^ { 1 2 }$ feasible solutions, respectively. Despite the reduction from the original number, an exhaustive search for the second and fourth sub-processes would still require several years of computation. These details are summarized in Table 1.

A genetic algorithm formulation of the problem was assembled. Chromosomes were created for each sub-process, with lengths determined by the number of tasks and number of services per task. The evaluation function used a combination of the performance and

![](/api/attachments/DDJXV3XC/fulltext/images/e51fb6602cc62b14f7e82834710ef89f4c2aee56b1e8b65fe42b116aa8434142.jpg)  
Customer Identification Sub-Process

![](/api/attachments/DDJXV3XC/fulltext/images/60bb982ea94a47a8cf92427094346ac6ac9c41beb0fa1d2dcad3f36ee032f66d.jpg)  
Sales Order Sub-Process

Legend:

5: Search Products

6: Browse Product

12: Acquire Payment Information

7: Add Products to Shopping Car

13: Validate Customer Credit

14: Charge Customer Credit Card

8: Check Availability of Shopping Cart Items

15: Create Order

9: Create Back Order to DSVendor

16: Send Order Confirmation to Customer

10: Acquire Shipping Address Information

17: Create Purchase Order for Transactiop

11: Acquire Shipping Method

18: Send Purchase Order to Vendor

![](/api/attachments/DDJXV3XC/fulltext/images/53140a3da77a0ad1fcdb63a6f7ef65166902f03b108bebfa6a11c2feca35cf18.jpg)  
Purchase Order Sub-Process

![](/api/attachments/DDJXV3XC/fulltext/images/c95f81aaf0f8f8a9574e60532be58124a2c56707a0af61bea2d5f7a969f5e7be.jpg)  
Shipping Sub-Process  
Fig. 3. Drop-ship business process

Table 1  
Characteristics of drop-ship example.

<table><tr><td>Sub-process</td><td>A (customer identification)</td><td>B (sales order processing)</td><td>C (purchase order management)</td><td>D (shipping)</td></tr><tr><td>Tasks</td><td>4</td><td>14</td><td>6</td><td>10</td></tr><tr><td>Services</td><td>24</td><td>33</td><td>33</td><td>57</td></tr><tr><td>Total solutions</td><td> $3.32 \times 10^{5}$ </td><td> $1.82 \times 10^{21}$ </td><td> $1.29 \times 10^{9}$ </td><td> $3.62 \times 10^{17}$ </td></tr><tr><td>Feasible solutions</td><td> $1.05 \times 10^{5}$ </td><td> $3.21 \times 10^{13}$ </td><td> $8.20 \times 10^{6}$ </td><td> $1.56 \times 10^{12}$ </td></tr></table>

security metrics. Since the two objectives do not work together, a tradeoff approach was adopted, wherein the software architect could specify the relative weights between performance and security. The weights were varied so as to provide a better understanding of the implications of leaning towards either objective. Expressions for performance and security measures for each sub-process appear in Table 2.

As the market for services is not developed to a signi<sup>fi</sup>cant extent, the availability of suf<sup>fi</sup>cient services for each task is a concern. To counter this, we used a set of simulated data to demonstrate the viability of the GA solution process. Some tasks have several candidate services to draw upon, while others are restricted in the number of available services. Performance metrics are generated from a normal distribution, while security metrics are generated from an inverted lognormal distribution since viable services are expected to provide high security, and the shape of the inverted lognormal distribution is skewed to the left. Metrics were generated for individual services for each task. Performance metrics varied widely by task, but ranged from 0.9092 to 5.8301 time units. Security data varied from 0.7266 to 0.9770 on a 0–1 scale. In an effort to ensure that the data was reasonable, correlation analysis between performance and security data was performed for each task. Since performance was measured as elapsed time, a more secure service would, on average entail a higher number for performance, and the correlation is expected to be positive. For the 34 tasks, the correlations ranged from 0.0076 to 0.7582, indicating acceptable input.

The GA population size was set at 1000. Crossover was set at 0.8, and the mutation parameter was set at 0.5. The algorithm was run for 1000 generations. The genetic algorithm parameters are summarized in Table 3. In an attempt to determine the effectiveness of the GA approach for larger and more complex processes, the separate subprocesses were combined into larger processes and the analysis performed for the entire process. It is acknowledged that this is not a true indication of scalability due to the independence between the sub-processes. Since the processes are entirely sequential, measures for performance and security are easily derived as functions of the measures for the sub-processes.

The evaluation function for the GA used the performance and security measures presented in Table 2. In general, performance and security do not go hand in hand, in that improvements on one objective typically entail some sacri<sup>fi</sup>ce on the other. Maximizing both at the same time is therefore infeasible. Instead, a weighted objective function was employed using performance and security metrics. The weights were varied from 0.0 to 1.0 in 0.1 increments. For each sub-process, the GA was run 11 times. This allowed the decision maker to explore the effect of trading off performance for security. In addition, the best solution for performance and security was logged for each sub-process, along with the generation in which it occurred. These results appear in Table 4.

From the tables it is seen that the GA was able to locate solutions with good performance and security measures relatively easily. This is readily apparent for the small sub-processes. With a population size of 1000, and execution of the GA for 1000 generations, this entails an exploration of up to $5 . 0 \times 1 0 ^ { 5 }$ possible solutions, which represents an almost exhaustive search for sub-process A. Finding good solutions early on in the search is not unexpected. For the larger sub-processes, and for the entire process, the most promising solutions were elicited later in the search. The table also illustrates that some services were used to support multiple tasks. For the security objective, since the combining function often utilized a minimum operator, the solutions were biased in favor of more secure services that could be used to support multiple tasks.

## 4.3. Trading off between competing objectives

Table 4 indicates that when pursuing different objectives, entirely different solutions are recommended. Given the competing nature of performance and security objectives, this research explored the effect of attempting to trade off between the two objectives. The solutions were then included on a scatter plot using performance and security as the measures of interest. This generated an ef<sup>fi</sup>cient frontier, representing a set of non-dominated solutions. The ef<sup>fi</sup>cient frontier for the complete process is presented in Fig. 4.

All other solutions will fall below this line, and represent dominated solutions, i.e. solutions that can be bettered on both performance and security objectives. Individual application designers and differing application contexts will call for varying emphasis on the two objectives. As is clear from the <sup>fi</sup>gure, if security is paramount, then designers have to accept some penalty on performance. Likewise, an emphasis on performance will entail some compromise on security. Application designers can select their preferred location on this ef<sup>fi</sup>cient frontier. Tradeoff graphs were also assembled for individual sub-processes, and exhibited similar patterns.

## 5. Discussion and implications

Service-oriented applications represent a new paradigm for business application development. In this case applications are composed from preexisting services provided by various vendors, which may be hosted at various locations. To gain widespread acceptance of this approach to application development, nonfunctional concerns of managers and users needs to be addressed. This research focused on performance and security as two of the more pressing concerns for users. While security and performance measures for individual services are important to vendors and designers, the end-to-end measures are of greater concern to users and managers. Without the ability to effectively compose the application in a manner that it exhibits an acceptable level of security and performance, the service-oriented approach is not likely to be adopted for business application development.

Performance measures for sub-processes.

<table><tr><td colspan="2">A. Performance measures for sub-process</td></tr><tr><td>Sub-process</td><td>Performance (D)</td></tr><tr><td>A</td><td> $p_1D_1 + p_2(D_3 + D_4) + D_2$  where  $p_1 + p_2 = 1$ </td></tr><tr><td>B</td><td> $\frac{(p_3D_5 + p_4D_6 + D_7)}{(1 - p_5)} + D_8 + p_7D_9 + D_{10} + D_{11} + \frac{(D_{12} + D_{13})}{(1 - p_9)} + \max((D_{15} + D_{16}), (D_{17} + D_{18}))$  where  $p_3 + p_4 = 1; p_5 + p_6 = 1; p_7 + p_8 = 1; p_9 + p_{10} = 1$ </td></tr><tr><td>C</td><td> $D_{19} + p_{11}(D_{20} + D_{21}) + D_{22} + D_{23} + D_{24}$  where  $p_{11} + p_{12} = 1$ </td></tr><tr><td>D</td><td> $D_{25} + p_{13}(D_{27} + D_{28} + \max((D_{29} + D_{30}), (D_{31} + D_{32}), (D_{33} + D_{34}))) + p_{14}D_{26}$  where  $p_{13} + p_{14} = 1$ </td></tr><tr><td colspan="2">B. Security measures for sub-process</td></tr><tr><td>Sub-process</td><td>Security (S)</td></tr><tr><td>A</td><td> $\min((p_1S_1 + p_2(\min(S_3,S_4))), S_2)$  where  $p_1 + p_2 = 1$ </td></tr><tr><td>B</td><td> $\min(\min((p_3S_5 + p_4S_6), S_7), S_8), (p_7S_9 + p_8), \min(S_{10}, S_{11}, \min(S_{12}, S_{13}), S_{14}, \min(S_{15}, S_{16}, S_{17}, S_{18})))$  where  $p_3 + p_4 = 1; p_5 + p_6 = 1; p_7 + p_8 = 1; p_9 + p_{10} = 1$ </td></tr><tr><td>C</td><td> $\min(S_{19}, (p_{11} \times \min(\min(S_{20}, S_{21}) + p_{12}), \min(S_{22}, S_{23}, S_{24})))$  where  $p_{11} + p_{12} = 1$ </td></tr><tr><td>D</td><td> $\min(S_{25}, (p_{13} \times \min(S_{27}, S_{28}, \min(\min(S_{29}, S_{30}), \min(S_{31}, S_{32}), \min(S_{33}, S_{34}))) + p_{14}S_{26}))$  where  $p_{13} + p_{14} = 1$ </td></tr></table>

Table 3 Characteristics of genetic algorithm.

<table><tr><td>Sub-process</td><td>A</td><td>B</td><td>C</td><td>D</td><td>A+B</td><td>C+D</td><td>A+B+C+D</td></tr><tr><td>Chromosome size</td><td>68</td><td>118</td><td>81</td><td>164</td><td>186</td><td>245</td><td>431</td></tr><tr><td>Population size</td><td>1000</td><td>1000</td><td>1000</td><td>1000</td><td>1000</td><td>1000</td><td>1000</td></tr><tr><td>Performance metric</td><td> $D_A$ </td><td> $D_B$ </td><td> $D_C$ </td><td> $D_D$ </td><td> $D_A + D_B$ </td><td> $D_C + D_D$ </td><td> $D_A + D_B + D_C + D_D$ </td></tr><tr><td>Security metric</td><td> $S_A$ </td><td> $S_B$ </td><td> $S_C$ </td><td> $S_D$ </td><td>Min( $S_A,S_B$ )</td><td>Min( $S_C,S_D$ )</td><td>Min( $S_A,S_B,S_C,S_D$ )</td></tr><tr><td>Crossover</td><td>0.8</td><td>0.8</td><td>0.8</td><td>0.8</td><td>0.8</td><td>0.8</td><td>0.8</td></tr><tr><td>Mutation</td><td>0.5</td><td>0.5</td><td>0.5</td><td>0.5</td><td>0.5</td><td>0.5</td><td>0.5</td></tr><tr><td>Generations</td><td>1000</td><td>1000</td><td>1000</td><td>1000</td><td>1000</td><td>1000</td><td>1000</td></tr></table>

This research developed measures for deriving end-to-end security and performance metrics for an application composed of individual services. These metrics were then used in a service selection model that helps the designer in selecting a set of services that will achieve the objective of required level of security and performance of the application. Since the two objectives of higher security and improved performance are often at odds with each other, a multiple criteria decision approach that relies on tradeoffs between the two objectives was presented. This permits the application designer to visualize the impact of choosing one objective over the other, and clearly see the impact of their service selection decision on these two important characteristics of the application. The tradeoff between security and performance may be performed at the process level, or at the sub-process level, if so desired. Thus, if there are situations where individual sub-processes demand additional performance or security, this can be addressed without affecting the other sub-processes.

For managers and application designers, the proposed model can serve as an effective decision support tool for service selection, and also give users con<sup>fi</sup>dence that the resulting application will be secure and will perform well. Simply selecting the service with the fastest performance or the highest level of security for each task will result in solutions that perform well on one objective and poorly on other objectives. Good solutions require that all objectives be considered, and appropriate tradeoffs be made. Without the ability to identify solutions that demonstrate superior values for both performance and security, the adoption of service-oriented application development is less likely.

For the providers of services, this approach requires them to focus on non-functional characteristics like security and performance, in addition to the traditional emphasis on correct functionality of services. They will also need to specify the security characteristics of the services they are providing, along with measures of expected performance. As the market place for services matures, vendors will increasingly compete on these non-functional characteristics. Development of standardized measures for these characteristics and techniques to evaluate their impact on overall application will go a long way in developing competitive market place for services.

Table 4  
Results from genetic algorithm.

<table><tr><td>Sub-process</td><td>Best performance</td><td>Generation</td><td>Best security</td><td>Generation</td></tr><tr><td>A</td><td>2.2318</td><td>10</td><td>0.9272</td><td>10</td></tr><tr><td>B</td><td>20.9772</td><td>37</td><td>0.9506</td><td>54</td></tr><tr><td>C</td><td>9.6513</td><td>27</td><td>0.9648</td><td>4</td></tr><tr><td>D</td><td>9.4727</td><td>29</td><td>0.9365</td><td>13</td></tr><tr><td>A+B</td><td>23.2090</td><td>61</td><td>0.9272</td><td>136</td></tr><tr><td>C+D</td><td>19.1241</td><td>56</td><td>0.9488</td><td>392</td></tr><tr><td>A+B+C+D</td><td>42.3330</td><td>136</td><td>0.9272</td><td>179</td></tr></table>

## 6. Conclusions

The problem of selecting services to support all tasks in a business process is an NP-hard problem. Non-linear and discontinuous combining functions add to the complexity of determining good solutions. As the number of tasks and services per task increase, the problem size increases exponentially. This research advocates decomposing the process into sub-processes to alleviate the complexity. Even with this reduction, the solution space for real-world business problems is so large that exact search strategies remain infeasible. A heuristic search strategy, viz. genetic algorithms, was employed to address the problem. Two distinct objectives of performance and security were adopted when searching for promising solutions. Formulations for end-to-end measures of performance and security were developed. The ability to tradeoff between the two con<sup>fl</sup>icting objectives of security and performance was provided to users and application designers.

Though performance and security represent important non-functional considerations in the selection of services, there are clearly other objectives that could be used. Additional factors include reliability, cost, vendor reputation, availability, among others. Other research has addressed some of these, including reliability [46], and cost and vendor reputation [45]. A more holistic approach that considers all criteria represents a logical follow-up. When dealing with multiple criteria, tradeoffs among the criteria will vary with application designer, and a mechanism to combine the heuristic search and the multiple criteria decision making component will be required.

![](/api/attachments/DDJXV3XC/fulltext/images/2dca9ab9140e4e1da6be9f13bcf6361fee6a6cd3264e862a9292f8a809bb7d20.jpg)  
Fig. 4. Performance and security tradeoffs for drop-ship process.

Further validation of the <sup>fi</sup>ndings from this research is necessary. The application to a reasonably complex drop-ship process demonstrates its viability. Application to a wide variety of processes of varying complexity, with differing numbers of candidate services to select from, will demonstrate the robustness of the approach, and will serve as an impetus for service-oriented application development.

## References

[1] W.M.P. v.d. Aalst, A.H.M. t. Hofstede, B. Kiepuszewski, A.P. Barros, Work<sup>fl</sup>ow patterns, Distributed and Parallel Databases 14 (1) (2003) 5–51.

[2] S.M. Bellovin, On the brittleness of software and the infeasibility of security metrics, IEEE Security and Privacy 4 (4) (2006) 96.

[3] M. Bichler, K.-J. Lin, Service-oriented computing, Computer 39 (3) (2006) 99–101.

[4] J. Cardoso, Quality of Service and Semantic Composition of Work<sup>fl</sup>ows, Department of Computer Science, University of Georgia, Athens, GA, 2002.

[5] J. Cardoso, J. Miller, A. Sheth, J. Arnold, Modeling Quality of Services for Work<sup>fl</sup>ows and Web Services Processes, LSDIS Lab, Computer Science Department, University of Georgia, Athens, May 2002 02-002.

[6] J. Cardoso, A. Sheth, J. Miller, J. Arnold, K. Kochut, Quality of service for work<sup>fl</sup>ows and web service processes, Web Semantics: Science, Services and Agents on the World Wide Web 1 (3) (2004) 281–308.

[7] M. Chen, D. Zhang, L. Zhou, Empowering collaborative commerce with Web services enabled business process management systems, Decision Support Systems 43 (2) (2007) 530–546.

[8] E. Chew, M. Swanson, K. Stine, N. Bartol, A. Brown, W. Robinson, Performance Measurement Guide for Information Security National Institute of Standards and Technology, Gaithesburgh, MD, July 2008.

[9] K. Clark, J. Dawkins, J. Hale, Security risk metrics: fusing enterprise objectives and vulnerabilities, Sixth Annual IEEE SMC Information Assurance Workshop (IAW '05), 2005, pp. 388–393, West Point, NY.

[10] L. Davis, Handbook of Genetic Algorithms, Van Nostrand Reinhold, New York, 1991.

[11] J. Epstein, S. Matsumoto, G. McGraw, Software security and SOA: danger, Will Robinson! IEEE Security and Privacy 4 (1) (2006) 80–83.

[12] Foundstone, Using Foundstone's FoundScore to Assign Metrics and Measure Enterprise Risk, Foundstone Strategic Security, Mission Viejo, CA, April 2003.

[13] D. Geer Jr., K.S. Hoo, A. Jaquith, Information security: why the future belongs to the quants, IEEE Security and Privacy 1 (4) (2003) 24–32.

[14] D.E. Goldberg, Genetic Algorithms in Search, Optimization, and Machine Learning Addison-Wesley, Reading, MA, 1989.

[15] B. Hartman, D.J. Flinn, K. Beznosov, S. Kawamoto, Mastering Web Services Security, Wiley Publishing, New York, NY, 2003.

[16] R.R. Henning, Security service level agreements: quanti<sup>fi</sup>able security for the enterprise? 1999 Workshop on New Security Paradigms, Caledon Hills, Ontario, Canada, 1999, pp. 54–60.

[17] T. Heyman, R. Scandariato, C. Huygens, W. Joosen, Using security patterns to combine security metrics, Third International Conference on Availability, Reliability and Security (ARES 08), Barcelona, Spain, 2008, pp. 1156–1163.

[18] J.H. Holland, Adaptation in Natural and Arti<sup>fi</sup>cial Systems: An Introductory Analysis with Applications to Biology, Control, and Arti<sup>fi</sup>cial Intelligence, University of Michigan Press, Ann Arbor, MI, 1975.

[19] M. Hu, Web services composition, partition, and quality of service in distributed system integration and re-engineering, XML Conference & Exposition, Philadelphia, PA, 2003.

[20] ISSEA, Systems Security Engineering Capability Maturity Model (SSE-CMM<sup>®</sup>) Model Description Document Version 3.0, The International Systems Security Engineering Association Herndon, VA SSE-CMM – ISO/IEC 21827, June 15 2003.

[21] W. Jansen, Directions in Security Metrics Research, National Institute of Standards and Technology, Gaithersburg, MD, April 2009.

[22] Y. Liu, "Quantitative security analysis for service-oriented software architectures", Doctoral dissertation, Dept. of Electrical and Computer Engineering, Victoria, BC, Canada: University of Victoria, (2008).

[23] T. Madhusudan, N. Uttamsingh, A declarative approach to composing web services in dynamic environments. Decision Support Systems 41 (2) (2006) 325-357

[24] A. McIntyre, B. Becker, R. Halbgewachs, Security Metrics for Process Control Systems, Sandia National Laboratories, Albuquerque, NM, September 2007 SAND2007-2070P.

[25] P. Mell, K. Scarfone, S. Romanosky, CVSS: A Complete Guide to the Common Vulnerability Scoring System Version 2.0, FIRST, Morrisville, NC, June 2007.

[26] Z. Michalewicz, Genetic Algorithms + Data Structures = Evolution Programs, Springer-Verlag, New York, 1998.

[27] E.E. Mills, Software Metrics, Software Engineering Institute, CMU, Pittsburgh, December 1988.

[28] M. Mitchell, An Introduction to Genetic Algorithms, The MIT Press, Cambridge MA, 1996.

[29] M.Z. Muehlen, J.V. Nickerson, K.D. Swenson, Developing web services choreography standards—the case of REST vs. SOAP, Decision Support Systems 40 (1) (2005) 9–29.

[30] E.A. Nichols, G. Peterson, A metrics framework to drive application security improvement, IEEE Security and Privacy 5 (2) (2007) 88–91.

[31] OMG, Business Process Modeling Notation (BPMN) Speci<sup>fi</sup>cation: Final Adopted Speci<sup>fi</sup>cation, Object Management Group, February 1 2006 dtc/06-02-01.

[32] M.P. Papazoglou, D. Georgakopoulos, Service-oriented computing: introduction, Communications of the ACM 46 (10) (2003) 24–28.

[33] M.P. Papazoglou, P. Traverso, S. Dustdar, F. Leymann, Service-oriented computing: a research roadmap, International Journal of Cooperative Information Systems 17 (2) (2008) 223–255.

[34] S. Ran, A model for web services discovery with QoS, ACM SIGecom Exchanges 4 (1) (2003) 1–10.

[35] N. Russell, A.H.M. t. Hofstede, W.M.P. v.d. Aalst, N. Mulyar, Work<sup>fl</sup>ow Control-Flow Patterns: A Revised View, Business Process Management Center, 2006 BPM-06-22

[36] R. Savola, Towards a security metrics taxonomy for the information and communication technology industry, International Conference on Software Engineering Advances (ICSEA 2007) Cap Esterel 2007 p. 60

[37] R.M. Savola, Towards a taxonomy for information security metrics, 2007 ACM Workshop on Quality of Protection, Alexandria, VA, 2007, pp. 28–30.

[38] E. Serrelis, N. Alexandris, An empirical model for quantifying security based on services, International Multi-Conference on Computing in the Global Information Technology (ICCGI 2007), Guadeloupe City, 2007, p. 30.

[39] C.U. Smith, Software performance engineering, in: L. Donatiello, R. Nelson (Eds.), Performance Evaluation of Computer and Communication Systems, vol. 729, Springer, Berlin/Heidelberg, 1993, pp. 509–536.

[40] M. Stoddard, Y. Haimes, D. Bodeau, C. Lian, R. Carlson, J. Santos, C. Glantz, J. Shaw, Process Control System Security Metrics — State of Practice, Institute for Information Infrastructure Protection, Dartmouth College, Hanover, NH, August 31 2005 Research Report No. 1.

[41] K. Sultan, A. En-Nouaary, A. Hamou-Lhadj, Catalog of Metrics for Assessing Security Risks of Software Throughout the Software Development Life Cycle, International Conference on Information Security and Assurance (ISA 2008), Busan, 2008, pp. 461–465.

[42] Y. Sun, S. He, J.Y. Leu, Syndicating Web services: a QoS and user-driven approach, Decision Support Systems 43 (1) (2007) 243–255.

[43] I. Tashi, S. Ghernaouti-Helie, Ef<sup>fi</sup>cient security measurements and metrics for risk assessment, Third International Conference on Internet Monitoring and Protection (ICIMP '08), Bucharest, Romania, 2008, pp. 131–138.

[44] J.L. Zhao, H.K. Cheng, Web services and process management: a union of convenience or a new area of research? Decision Support Systems 40 (1) (2005) 1–8.

[45] H. Zo, "Supporting Intra- and Inter-Organizational Business Processes with Web Services," Doctoral dissertation, University of Wisconsin–Milwaukee, Milwaukee, 2006.

[46] H. Zo, D.L. Nazareth, H.K. Jain, Measuring reliability of applications composed of web services, 40th Annual Hawaii International Conference on System Sciences (HICSS'07), Waikoloa, Hawaii, 2007, p. 278c.

Hangjung Zo is Assistant Professor of MIS in the Department of Management Science at Korea Advanced Institute of Science and Technology, He received his PhD in MIS from the University of Wisconsin-Milwaukee. His research interests include Web services and Web-based systems, e-business and e-commerce, software engineering, business process management, and IT strategy. His papers have appeared in IEEE Transactions on Systems Man &r Cybernetics HICSS among others He was the chair for the ICT Innovations and Progresses in Developing Countries Workshop at ICCIT 2009.

Derek Nazareth is Associate Professor of MIS at the University of Wisconsin–Milwaukee. He received his PhD in MIS from Case Western Reserve University. His current research interests include Web services composition, business process modeling, and software reuse. His papers appear in IEEE Transactions on Knowledge and Data Engineering, IEEE Transactions on Systems Man & Cybernetics, Journal of Management Information Systems, Decision Support Systems, Communications of the ACM, and in Information & Management among others. He served as the Program Chair for AMCIS 1999, and the Treasurer for ICIS 2006.

Hemant Jain is Wisconsin Distinguished & Tata Consultancy Services Professor of Management Information System in Sheldon B. Lubar School of Business at University of Wisconsin–Milwaukee. Dr. Jain specializes in information system agility through Web services, service-oriented architecture and component based development. Dr. Jain has published over 50 articles in leading journals including Information Systems Research, MIS Quarterly, IEEE Transactions on Software Engineering, Journal of MIS, IEEE Transactions on Systems Man and Cybernetics, Naval Research Quarterly, Decision Sciences, Decision Support Systems, Communications of ACM, and Information & Management. Additionally, he has published over 55 papers in referred conference proceedings. Dr. Jain is the Associate Editor-in-Chief of IFFE Transactions on Services Computing and is Associate Editor of Journal of AIS, <sup>fl</sup>agship journal of Association of Information system. Additionally, he serves on the editorial board of a number of other highly regarded Journals. He is on the board and member of the Steering Committee of IEEE Technical Community for Services Computing and is a member of the Service. Systems and Organizations Technical Committee of the IEEE SMC Society. He was the program committee Co-chair of 2004 IEEE conference on Web services and is General Chair of IEEE Services Computing Conference 2006 and IEEE International Conference on Web services in 2008. He received his Ph. D. in information systems from Lehigh University, an M. Tech from IIT Kharagpur, India, and B. E. from University of Indore, India.
