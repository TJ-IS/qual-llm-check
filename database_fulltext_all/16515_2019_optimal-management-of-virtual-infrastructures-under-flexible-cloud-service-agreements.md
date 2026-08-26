---
otero_id: 16515
otero_key: "RSBEMUES"
title: "Optimal Management of Virtual Infrastructures Under Flexible Cloud Service Agreements"
authors: "Zhiling Guo; Jin Li; Ram Ramesh"
year: "2019"
journal: "Information Systems Research"
doi: "10.1287/isre.2019.0871"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [198.255.74.30] On: 25 April 2025, At: 23:47 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

![](/api/attachments/RSBEMUES/fulltext/images/c8d724a4e3577b045e9d08177e389d579d2e040838a36d705747ddc72ad235c5.jpg)

# Information Systems Research

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Optimal Management of Virtual Infrastructures Under Flexible Cloud Service Agreements

Zhiling Guo, Jin Li\*, Ram Ramesh

To cite this article:

Zhiling Guo, Jin Li\*, Ram Ramesh (2019) Optimal Management of Virtual Infrastructures Under Flexible Cloud Service Agreements. Information Systems Research 30(4):1424-1446. https://doi.org/10.1287/isre.2019.0871

Full terms and conditions of use: https://pubsonline.informs.org/Publications/Librarians-Portal/PubsOnLine-Terms-and-Conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2019, INFORMS

Please scroll down for article—it is on subsequent pages

## inferms

With 12,500 members from nearly 90 countries, INFORMS is the largest international association of operations research (O.R.) and analytics professionals and students. INFORMS provides unique networking and learning opportunities for individual professionals, and organizations of all types and sizes, to better understand and use O.R. and analytics tools and methods to transform strategic visions and achieve better outcomes. For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Optimal Management of Virtual Infrastructures Under Flexible Cloud Service Agreements

Zhiling Guo,<sup>a</sup> Jin Li,<sup>b,</sup>\* Ram Ramesh<sup>c</sup>

<sup>a</sup> School of Information Systems, Singapore Management University, 178902 Singapore; <sup>b</sup> School of Management, Xi’an Jiaotong University, Xi’an 710049, China; <sup>c</sup> Department of Management Science and Systems, School of Management, University at Buffalo (SUNY), Buffalo, New York 14260

\*Corresponding author Contact: zhilingguo@smu.edu.sg, http://orcid.org/0000-0002-9058-4710 (ZG); jinlimis@xjtu.edu.cn, http://orcid.org/0000-0003-3340-1516 (JL); rramesh@buffalo.edu, http://orcid.org/0000-0002-6232-1841 (RR)

Received: March 9, 2018 Revised: February 18, 2019 Accepted: May 5, 2019 Published Online in Articles in Advance: December 10, 2019

https://doi.org/10.1287/isre.2019.087

Copyright: © 2019 INFORMS

Abstract. A cloud service agreement entails the provisioning of a required set of virtual infrastructure resources at a specified level of availability to a client. The agreement also lays out the price charged to the client and a penalty to the provider when the assured availability is not met. The availability assurance involves backup resource provisioning, and the provider needs to allocate backups cost-effectively by balancing the resource provisioning costs with the potential penalty costs. We develop stochastic dynamic optimization models of the backup resource-provisioning problem, leading to cost-effective resource-management policies in different practical settings. We present two sets of dynamic provisioning strategies: periodic policies, where resources are adjusted at regular intervals, and aperiodic policies that allow flexible timing of such interventions. A closed-loop (CL) optimization model under conservative resource control and a certainty-equivalent (CE) optimization model under aggressive resource control are developed for periodic resource management. Similarly, aperiodic resource management is modeled by using two different strategies: single intervention with single look-ahead (SISL) and multiple interventions with single look-ahead (MISL). Online optimization algorithms for both the periodic and aperiodic models are developed. The worst-case behavior of the algorithms is studied by using competitive ratio analysis and the expected behavior by using computational investigations. By using these studies, managerial guidelines for choosing the best resourcemanagement strategy under different client-specific, service-specific, and system-specific resource-optimization conditions are presented. We validate our models based on use cases constructed from Amazon Elastic Compute Cloud (EC2) with their actual pricing and service-credit data. The practical guidelines from this study will aid contract adminis trators in cloud data centers to both efficiently formulate service-level agreements and costeffectively manage the virtual infrastructure resources committed in such agreements.

History: Ravi Bapna, Senior Editor; Martin Bichler, Associate Editor. Funding: J. Li received support from the China Postdoctoral Science Foundation [Grant 2019M650035]. Supplemental Material: The online supplement is available at https://doi.org/10.1287/isre.2019.0871.

Keywords: cloud computing • service level agreement (SLA) • dynamic programming (DP) • online algorithm • virtual machines (VMs) • cloud resource management

## 1. Introduction

The broad concept of cloud computing entails three fundamental models of service hosting and delivery: Software-as-a-Service (SaaS), Platform-as-a-Service (PaaS), and Infrastructure-as-a-Service (IaaS). IaaS functions at the lowest level by providing virtualized computing, storage, and network services that would support PaaS and SaaS (Colman 2013). A cloud service-level agreement (SLA) for IaaS typically includes dynamic metrics such as infrastructure service availability, performance latency and response delay for emergencies, and a host of medium- to long-term metrics such as data security, privacy, and integrity.<sup>1</sup> Availability is a central commitment in all SLA abstractions―computing, networking, and storage (Cloud Standards Customer Council 2017)―and a failure to meet the committed level of availability by a service provider results in either penalties or service credits given by the provider to the client. For example, Dimension Data proposes a system of service credits, and other vendors such as Amazon Web Services (AWS) also provide similar terms to compensate clients for system downtime that exceeds the promised level of availability in an SLA. These contractual arrangements lend valuable flexibility to a service provider in fulfilling the availability commitment in an SLA, especially when faced with system failures and other service disruptions that may be hard to predict and control.

Central to IaaS is the concept of virtualization. Virtualization is essentially software that encapsulates multiple operating systems individually and enables them to coexist and run independently on the same physical server platform. Each such operating system is a virtual machine (VM). Multiple virtual machines that are cohosted on a physical server would execute concurrently and independently. Accordingly, a virtual infrastructure typically comprises a set of virtual machines that are hosted on a set of physical servers; the virtual machines provide the basic functionalities of computing, storage, and networking in the distributed cloud architecture. This IaaS model is widely adopted by several cloud service providers such as AWS, Google, Microsoft, Rackspace, Salesforce, and many others.<sup>2</sup> Under the notion of virtual infrastructures, when a client requests cloud services, the client requirements translate to an SLA for IaaS that broadly specifies the number of VMs needed, their critical dynamic service-level metrics, the service window over which the metrics are evaluated, and the service pricing and service credit schemes (Cloud Standards Customer Council 2017).

Denoting the VMs required in an SLA as primary VMs, the service provider usually builds redundancy in the virtual infrastructure in the form of backup VMs to ensure the availability of the required number of VMs at the level promised in the SLA. This redundancy enables fault tolerance by checkpointing and rollback recovery, and guidelines for VM checkpointing using backups are given in the Microsoft communication.<sup>3</sup> Various models of backup checkpointing exist in both the literature and practice, and the widely adopted models are the powered-on models under conventional VM failures and especially when critical applications are supported (Du et al. 2015). In the above context of an SLA for a virtual infrastructure under powered-on checkpointing, Yuan et al. (2018) address the trifecta of backups, VM pricing, and penalty for shortfall in the assured availability in an SLA. As we increase the number of backup VMs, the likelihood of SLA violation decreases, and hence the expected penalty cost, but the VM provisioning cost increases. For a given price–penalty combination, Yuan et al. (2018) derive the optimal level of backups to minimize the expected total cost over a contract period by balancing the trade-off between the VM provisioning cost and the expected penalty cost.

A limitation of the study of Yuan et al. (2018) is the single and static determination of the level of backups needed for a service agreement at the beginning of the contracted period and its enforcement throughout the period. In the presence of practical random events, such as system failures and recovery, such static determination could be suboptimal in real-world datacenter operations, especially when system downtimes are common and significant. Consequently, cloud resource provisioning should be a dynamic rather than a static decision. As the cumulative system downtime randomly grows with the progression of service in a contracted period, a cloud data center needs to take advantage of the observed downtime information, reassess existing resource commitments, and make dynamic decisions on backup deployment. Although such dynamic management would lead to efficient resource allocation, the challenge is how to time such backup adjustments and determine the optimal adjustment levels, especially under the transient random failure and recovery processes involved.

Motivated by the above, we develop dynamic optimization models to guide the service provider’s resource-provisioning strategies. By modeling the number of primary and backup VMs deployed as resources, and denoting the times of resource ad justment as interventions, we develop both periodic and aperiodic policies for dynamic resource management. In periodic resource optimization, the service provider would intervene regularly at fixed time intervals and may adjust the backup deployment at each intervention. This policy leads to two implementation strategies: conservative versus aggressive backup VM provisioning. Under conservative provisioning, the service provider initially provides a small number of backup VMs when no downtime is incurred yet. As the cumulative downtime increases over time, the service provider becomes more concerned about potential contract violation and, consequently, could fine-tune or even increase the number of backups if needed. Under aggressive provisioning, the service provider initially provides a large number of backup VMs to ensure sufficient redundant capacity to cope with future downtime uncertainty. As time goes by, when the service provider becomes less uncertain about future downtime, the level of backup deployment can be fine-tuned or even reduced if warranted. We develop a closed-loop (CL) stochastic dynamic optimization model of the conservative strategy and a certainty-equivalent (CE) dynamic optimization model of the aggressive strategy.<sup>4</sup> The CL model always produces optimal solutions under all conditions. However, the CE model requires significantly less computational effort than the CL model. Furthermore, the CE model produces nearoptimal solutions when (1) the ratio of penalty to backup provisioning cost is relatively low, (2) the failure and recovery processes are less predictable,<sup>5</sup> and (3) the availability level required in the SLA is high. Hence, the CE model is recommended due to its significant computational effectiveness when these conditions are prevalent.

Although periodic resource management focuses on how much adjustment to the backup VM deployment should be made when the number and timing of such adjustments are fixed, aperiodic resource management focuses on the quanta of VM adjustments, the number of such adjustments, and their timing, all at once. Flexible timing of adjustments would bring a number of benefits, such as cost savings from less frequent assessments and adaptations than fixed interventions. However, the underlying optimization may be computationally overwhelming. Accordingly, we develop a tractable approach to aperiodic optimization by categorizing such policies along two dimensions: interventions and look-aheads. A lookahead is the determination of the expected performance over the remaining part of the contract period after an intervention. This optimization occurs recursively over the continuum of time, rolling over from intervention to intervention. Therefore, such policies could lead to multiple interventions that are unevenly spaced in the contract period. In this research, we develop two aperiodic policies, denoted as Single Intervention with Single Look-ahead (SISL) and Multiple Interventions with Single Look-ahead (MISL). Intuitively, as the number of interventions increases, the total costs of aperiodic policies would decrease, up to a certain optimal number of interventions, which asymptotically converge to the costs of frequently periodic policies. However, under conditions of (1) greater predictability of the failure and recovery processes, (2) not too stringent availability requirements in an SLA, and (3) small-sized service contracts, aperiodic policies outperform periodic policies. Our extensive computational studies confirm this.

Finally, we develop online as well as offline implementation algorithms for both periodic (CL and CE) and aperiodic (SISL and MISL) management policies. The offline algorithm of a model solves the problem at the start of the planning horizon and produces a solution as a predetermined control policy, regardless of the information revealed during the course of the contract duration. The online algorithm implements the first-step solution of an offline algorithm, resolves the model every time new pieces of information arrive dynamically, and yields new control decisions using the new information. We implemented the online algorithms based on use cases constructed from Amazon Elastic Compute Cloud (EC2) with their actual pricing and service credit data. We derived practical guidelines for contract administrators in cloud data centers to cost-effectively manage their virtual infrastructure resources.

The rest of the paper is organized as follows. Section 2 focuses on the research context and summarizes our key contributions. Section 3 reviews the relevant literature. Section 4 develops the periodic policies under conservative resource management and Section 5 under aggressive management. Section 6 develops aperiodic intervention policies under the SISL and MISL resource management. Section 7 presents the computational results, and Section 8 further validates our models based on use cases constructed from Amazon EC2 service structures. Section 9 discusses the managerial implications of the proposed resource-management policies. Section 10 concludes with directions for future research. The online supplement provides more details of our computational study and the proofs to all our theoretical results.

## 2. Research Context and Contributions

Cloud service providers typically offer a wide range of flexible contracts and pricing mechanisms. Based on a survey of 19 leading cloud service vendors across 27 types of service offerings, Kauffman et al. (2014) classify the state-of-the-art cloud pricing and service provision into two major categories: reservationbased pricing for reserved services delivery and usagebased pricing for on-demand services delivery. This observation is also supported by large-scale cloud platforms such as Amazon EC2.<sup>6</sup> For example, Amazon offers four classes of EC2 instances: on-demand instances, spot instances, reserved instances, and dedicated hosts (which provide EC2 instance capacity on dedicated physical servers). Under on-demand pricing, customers pay for computing capacity by hour without long-term commitment; under spot pricing, customers request spare Amazon EC2 computing capacity for up to 90% off the on-demand price. These two pricing models are suitable for ap plications with short-term, unpredictable workloads In contrast, reserved instances and dedicated hosts can be purchased with the commitment of a 1- or 3-year contract term. These models are more suitable for applications with relatively stable workloads for dedicated usage. Our proposed virtual infrastructure resource-management framework is in the context of IaaS providers’ service contracts of reserved instances or dedicated hosts, where precommitted VM resources are provided to clients in a service contract over a fixed contract period.

We develop a multidisciplinary approach to study the IaaS virtual infrastructure resource-management problem in the cloud. The proposed approach draws upon research from computing resource optimization, algorithm design, and statistical estimation of downtime distributions, together leading to the development of effective IT policies for cloud data centers. We model the service downtime allowed in an SLA as a perishable commodity in the underlying service period. This leads to inventory-like approaches to dynamic VM management in the cloud. Drawing from the literature on dynamic systems control and online algorithm design, we develop effective VM resourcemanagement strategies that are both relevant and easily implementable in cloud data centers. Thus, our modeling approach integrates ideas from Management Science and Computer Science in addressing resourcemanagement problems in the cloud IT domain.

The unique contributions of our research are threefold. First, we develop both periodic and aperiodic dynamic decision models for cloud VM provisioning under an SLA. Under the periodic focus, we model both conservative and aggressive approaches to address the question of how many VMs to allocate in a periodic manner over the contract window, and under the aperiodic focus, we develop dynamic approaches to concurrently address the questions of how many VMs to allocate and when to allocate them over the contract period of an SLA. In particular, the closedloop conservative optimization solution can be easily translated into a reference chart to guide backup resource provisioning in real time. Second, we design tractable online and offline algorithms to solve for the optimal solutions with reasonable computational effort, which is critical to provide practical decision support for cloud service providers’ cost-effective resource-allocation decisions. Third, using extensive computational studies, we evaluate how the clientlevel parameters (i.e., service availability and contract duration), service-level parameters (i.e., VM requirements and VM provisioning and penalty costs), and system-level parameters (i.e., mean time between failures and mean time to repair of the VMs) would affect the service provider’s optimal resource management. These studies, together with Amazon use cases evaluation, lead to practical insights into the service provider’s flexible resource provisioning to minimize its total operational cost and a relevant policy framework to guide SLA contract administrators in their VM resources management under different conditions.

## 3. Related Literature

We review the literature on cloud pricing and service delivery mechanisms using the classification scheme of Kauffman et al. (2014). Because SLA and resource management differ across the service-provisioning models (i.e., reserved or on-demand) and the types of service (i.e., IaaS, PaaS, and SaaS), we present a taxonomy of service models and pricing structures in the online supplement. Based on this taxonomy, we summarize the relevant literature as follows.

## 3.1. Reserved Services Provisioning and Service Contracts

Recent trends in IaaS cloud focus on virtual infrastructure resources, including computing, storage, and networking that are deployed over a number of VMs in a distributed manner (Chowdhury and

Boutaba 2010). Because of virtualization, the cloud infrastructure is more prone to a wide range of hardware and software failures (Gill et al. 2011). Because robust and failure-resilient infrastructure is critical to cloud consumers, infrastructure availability is the most important quality-of-service (QoS) metric in the IaaS cloud SLA for reserved services. A common practice to ensure infrastructure availability is to deploy redundant VMs to increase fault tolerance in the cloud provider’s service provision (Qiu et al. 2014). Because full redundancy is costly, a more effective approach is to allocate a set of backup VMs to replace the failed primary VMs as needed (Lu et al. 2012, Xu et al. 2012). Technically, this can be achieved by checkpointing (Goiri et al. 2010). The checkpointing mechanism periodically saves the execution state of a running task (e.g., a VM image file) and enables the task to be resumed from the latest saved state after failure occurs (Du et al. 2015). Zhou et al. (2017) propose a network topology-aware backup VM placement approach to minimizing the consumption of network communication resources when the primary VM failures need to be recovered by backup VMs under the k-faulttolerance reliability constraints.

In the context of PaaS and SaaS, a broader range of SLAs have been studied for different applications hosted on the cloud infrastructure. Zhao et al. (2015) propose a consumer-centric SLA management framework for cloud-hosted databases. Wang et al. (2008) develop a resource-management framework to support multitier web applications in shared data centers, which helps to meet different service-quality targets at minimum operational cost. Wu et al. (2011) propose resource-allocation algorithms for SaaS providers to schedule enterprise applications on VMs that minimize infrastructure cost and SLA violation. Nevertheless, most of these works consider lower-level cloud architectural design to support cloud-based applications, as well as QoS metrics like latency and execution time that affect application delivery (Goudarzi et al. 2012). In contrast, our research focuses on availability-aware infrastructure-resource provisioning, which is the most important consideration in IaaS cloud SLAs.

## 3.2. On-Demand Services Provisioning and Service Contracts

Bruneo (2014) studies QoS in IaaS clouds under the on-demand service model. Liu et al. (2015) define quick response time as the key QoS metric in the service contracts. They propose an aggressive VM provisioning strategy to minimize the adaptation time and maintain a high level of QoS of hosted services. Singh et al. (2017) present an SLA-aware autonomic management framework aiming to reduce SLA violation rates for on-demand cloud service delivery.

Because workload uncertainty is a key feature of the on-demand services, dynamic IaaS resource provisioning is an emerging research topic in cloud data-center research (Bilal et al. 2014). A substantial amount of research in this area has studied server consolidation, optimal VM placement, and sizing to reduce operating cost in the IaaS cloud (Bobroff et al. 2007, Ahmad et al. 2015). Silva Filho et al. (2018) provide a recent survey for the approaches to optimizing VM placement and migration in the cloud environment. Various algorithms and frameworks have been proposed in the literature for this purpose. For example, Laalaoui and Al-Omari (2018) propose an iterative direct-move heuristic approach for reassigning VMs into clusters in the IaaS cloud platform. In the context of PaaS/SaaS, Shabeera et al. (2017) develop a metaheuristic algorithm based on ant-colony optimization to simultaneously optimize VM placement and location of data for hosting data-intensive applications in the cloud.

## 3.3. IaaS Dynamic Resource Provisioning Under Reserved/On-Demand Services

Because most cloud providers offer both reservation and on-demand services, Chase and Niyato (2017) consider that resources can be utilized under the reservation plan or provisioned under the on-demand plan at a higher rate. They propose joint optimization of VMs and bandwidth allocation to account for the VM overprovisioning and underprovisioning risks. Similarly, Ran et al. (2017) present a dynamic instanceprovisioning strategy by controlling the predicted overload probability of a service below a threshold level to ensure QoS, as well as a reserved instanceprovisioning strategy for further reducing the total cost. From the IaaS provider’s point of view, Mistry et al. (2018) propose a dynamic metaheuristic optimization model to compose long-term service requests under reserved instances, subject to resource and QoS constraints. Differently from their approaches that focus on stochastic arrival of requests, we consider the uncertainty involved in the infrastructure availability. Although failure-aware resource management has been studied in the literature (Fu 2010), dynamic backup resource provisioning to fulfill service contracts in the IaaS cloud is an underexplored area of research. We propose an availability-aware cloud resourcemanagement framework to fill this research gap.

## 3.4. Other Cloud-Based Business Models

In the PaaS and SaaS environment, a few studies have focused on resource optimization by taking into consideration the cloud consumers’ requirements. For example, Liu et al. (2010) study the resource-allocation policies for personalization services on content-delivery sites. The website trades off the benefit from providing optimal personalized content with a long delay and suboptimal content with less waiting time. Johar et al. (2014) propose an optimal control model to determine the size and composition of the firm’s offer set to engage a customer. Our work is different from this line of research because we focus on cloud providers’ infrastructure resource management rather than cloud consumers’ personalized content offerings. We propose a forward-looking, dynamic optimization model for resource provisioning and incorporate various factors including client-specific, system-specific, and servicespecific parameters into the cloud service provider’s decision making. We aim to provide higher-level policy recommendations that help guide data-center managers to choose the appropriate resource-management strategy in the course of their availability-aware SLA execution.

In addition to the operational cost models of resources, pricing models of services have been widely studied in the cloud IT domain. Cheng et al. (2016) show that price heterogeneity exists among different cloud-computing providers because of the network latency differentials. Sen et al. (2009) propose a dynamic priority-based price-penalty mechanism for fulfilling the SLA, considering the users’ preference variance and their demand fluctuations. In addition to pricing, service contract design has been widely studied in various other contexts such as software outsourcing (Dey et al. 2010), online storage services (Das et al. 2011), and supply-chain coordination (Sieke et al. 2012). In the cloud infrastructure, Yuan et al. (2018) study the SLA contract-pricing problem based on the trade-off between resource-provisioning cost to ensure availability and penalty cost for potential service downtime. We complement their work by focusing on efficient resource allocation under an SLA to optimize the service provider’s resource provisioning decisions in the dynamic cloud environment.

Integrating methods from Operations Research and Computer Science has demonstrated great promise in business problem solving. Technically, our solution approach follows the multistage dynamic programming optimization models in Operations Research and online algorithms in Computer Science. To deal with the “curse of dimensionality” (Bellman 1957), characterized as the exponentially increased computational requirements to solve the dynamic programming models as the problem’s size increases, we employ techniques such as certainty-equivalent models and limited steps of look-ahead models to handle the computational challenges (Bertsekas 1995). In addition, online optimization is crucial to provide practical decision support (Jaillet and Wagner 2012). The assessment of the solution of an online algorithm when compared with the solution of a corresponding ideal offline algorithm that knows the entire input sequence in advance is termed competitive analysis (Sleator and Tarjan 1985). We show that the online algorithms developed in this research are competitive and that the resource-management strategies we propose can be used to support IaaS cloud SLA management in practice.

## 4. Periodic Resource Optimization: Conservative Strategy

The SLA considered in this research is as follows. Let the client require n VMs over contract duration T with a required level of service availability $\alpha ~ \in ~ ( 0 , 1 )$ Whenever the number of VMs available is less than n, the overall system of VMs in the contract is said to be down, resulting in SLA violation. Hence, the allowed total downtime without any penalty to the service provider by contract is $B = \bar { ( 1 - \alpha ) } T$ . Any downtime incurred in excess of B is denoted as penalizable downtime (Yuan et al. 2018), and the service provider compensates the client at the unit penalty rate π for the penalizable downtime. Linear penalty functions for SLA violations in IaaS have been commonly used in the literature (Mistry et al. 2018). In addition, several variances of such functions (e.g., step penalty function) have been used in practice (e.g., Amazon EC2, Alibaba, Microsoft Azure, and Google). Please see the online supplement for details. We further assume that the cost of provisioning one VM per unit of time is h.

Without loss of generality, we assume one-to-one mapping of virtual to physical servers for a given client in the data center. Although the same physical server may host multiple VMs, the VMs for a given client may be spread across different physical server racks in order to mitigate the SLA violation risk from a single point of failure. Using the powered-on checkpointing model, we assume that k backup VMs are provided. The total expected cost consists of the provisioning cost of (n + k) VMs over the contract period and the expected penalty of not meeting the availability guarantee. Assuming independent server failures, an SLA violation would occur when more than k servers are concurrently down at a given time. Denoting the duration of SLA violation in a contract period T as system downtime, Du et al. (2015) model the states of the system of $( n + k )$ VMs in terms of the number of VMs that have failed at any time and obtain a birth–death recurrent Markov process over the system states. Using a sample path randomization approach, they derive the transient probability distribution of system downtime. Because system steady states may not be guaranteed in many practical data-center operations, the derivation of the transient distribution is needed. In this research, we adapt the approach by Du et al. (2015) to obtain the transient downtime distribution as input to the pro posed optimization models. A summary of the methodology is presented in the accompanying online supplement.

Periodic resource optimization involves decisions on VM deployment at a fixed set of stages in the contract duration T. We denote the decision stages as $\delta = 1 , 2 , . . . S ,$ , where S is the total number of stages. Although the stages need not be equally spaced in $T ,$ for the sake of simplicity in presentation and without loss of generality, we assume that the stages are equally spaced. A system state in stage δ is characterized as a pair $( x _ { \delta } , k _ { \delta } )$ , where $x _ { \delta }$ is the total incurred downtime and $k _ { \delta }$ is the number of backup VMs at the beginning of stage δ. Furthermore, $x _ { \delta }$ ranges in the interval $[ 0 , \frac { ( \delta - 1 ) T } { S } ]$ and $k _ { \delta } = 0 , 1 , . . . K ,$ , where K is the maximum number of backups available for the SLA. Because there is no downtime to begin with stage 1, we have $x _ { 1 } = 0$ . The state transition equation is $k _ { \delta + 1 } =$ $k _ { \delta } + u _ { \delta } ,$ where $u _ { \delta }$ is the integer decision variable at the beginning of stage δ, and $- k _ { \delta } \leq u _ { \delta } \leq K - k _ { \delta }$ . Therefore, $u _ { \delta } ( x _ { \delta } , k _ { \delta } ) \stackrel { - } { = } \{ - k _ { \delta } , ( - k _ { \delta } + 1 ) , . . . , 0 , 1 , 2 , . . . , K - k _ { \delta } \}$ }. These decisions lead to the state transitions from any stage δ to a state in the subsequent stage, as illustrated in the left panel of Figure 1.

To focus on the backup adjustment decision and to simplify our notation, we assume that the number of primary backup VMs is fixed at n in our theoretical model development. We denote D(k) as the random

Figure 1. Staged VM Deployment and a Four-Stage Transition Paths Example downtime incurred in any given stage with k backup VMs and d(k) as the expected downtime in the given stage. Therefore, we have $x _ { \delta + 1 } = x _ { \delta } + D ( k _ { \delta } + u _ { \delta } )$ . The right panel of Figure 1 illustrates a four-stage problem with $K = 2$ . The top of this panel illustrates the initial states and controls in each stage, where stage 5 is the ending stage at which no further cost is incurred, and, hence, no control is necessary. The bottom of this panel shows the full set of transition paths.

![](/api/attachments/RSBEMUES/fulltext/images/75e22863fb9b6d12caae52dbc1cf4740cfbf2b0cae1631654917afc0809a3df4.jpg)

![](/api/attachments/RSBEMUES/fulltext/images/1df72b3e0b52273d9737ce3ae909f3539f954111655af05496aa64cf70d8e2a2.jpg)

![](/api/attachments/RSBEMUES/fulltext/images/b13e6029a995fad04d2eaa417aec619a76fc7bfda1dd0fe65aeed6311e6f3d77.jpg)

Denote $J _ { \delta } ( x _ { \delta } , k _ { \delta } )$ as the cost-to-go function, which is the minimum expected total cost from stage δ to the end of stage S, which is the end of the horizon. The terminal cost incurred at the end of the horizon is $J _ { S + 1 }$ $( x _ { S + 1 } , k _ { S + 1 } ) = 0$ . The dynamic stochastic optimization problem at any stage δ, where $\delta = 1 , \ldots , \bar { S }$ and $u _ { \delta }$ the control decision is as follows:

Problem CL

$$
\begin{array}{r l} & J _ {\delta} (x _ {\delta}, k _ {\delta}) = \min \bigg [ h (k _ {\delta} + u _ {\delta}) \frac {T}{S} \\ & \qquad + E [ \pi \max \{0, x _ {\delta} + D (k _ {\delta} + u _ {\delta}) \\ & \qquad - \max (B, x _ {\delta}) \} ] + J _ {\delta + 1} (x _ {\delta + 1}, k _ {\delta + 1}) \bigg ]. \end{array}
$$

s.t. ${ x } _ { \delta + 1 } = { x } _ { \delta } + { D } ( { k } _ { \delta } + { u } _ { \delta } ) , { k } _ { \delta + 1 } = { k } _ { \delta } + { u } _ { \delta } , - { k } _ { \delta } \leq { u } _ { \delta } \leq { K } - { k } _ { \delta } ,$ and $u _ { \delta }$ is integer.

The cost-to-go function $J _ { \delta } ( x _ { \delta } , \ k _ { \delta } )$ minimizes the expected total cost in the current stage δ plus the minimum expected total cost from stage $\delta + 1$ to the end of the horizon $J _ { \delta + 1 } ( x _ { \delta + 1 } , k _ { \delta + 1 } )$ . The first term in the minimization function is the backup provisioning cost in stage δ. The second term is the expected penalty cost in stage δ. Note that if $x _ { \delta } > B ,$ , then the penalizable downtime incurred in stage δ is $D ( k _ { \delta } + u _ { \delta } )$ If $x _ { \delta } \leq B ,$ , then the penalizable downtime in stage $\delta$ is max $\{ 0 , x _ { \delta } + D ( k _ { \delta } + u _ { \delta } ) - B \}$

Closed-loop optimization derives a control policy that depends on the current state information on the system. Accordingly, the closed-loop solution to Problem CL yields rules for choosing $u _ { \delta }$ for each stage δ with knowledge of the current level of downtime incurred $x _ { \delta }$ and the current level of backup provision $k _ { \delta }$ . Because there is no closed-form solution to characterize the closed-loop strategy, we develop an efficient algorithm to solve for the optimal state-contingent strategies. Building upon the approach proposed by Du et al. (2015) to estimate transient system downtime, Section 1 of the online supplement details our strategy to obtain the empirical estimation of system downtime in our current context. For any given $( n , k )$ configuration, define $f _ { k } ( \tau )$ and $F _ { k } ( \tau )$ as the density function and cumulative distribution function of incurring τ downtime over the contract period $T ,$ and $\eta _ { k }$ as the mean percentage of downtime incurred over the contract period. We next show that the downtime distribution satisfies the following properties:

Lemma 1. If the number of backup VMs $k _ { 1 } < k _ { 2 }$ , then the downtime distribution has the following properties: $\mathrm { ( i ) } F _ { k _ { 1 } } ( \tau ) \le F _ { k _ { 2 } } ( \tau )$ —that is, $F _ { k _ { 1 } } ( \tau )$ first-order stochastically dominates $F _ { k _ { 2 } } ( \tau ) ;$ (ii) $\begin{array} { r } { \int _ { 0 } ^ { \tau } [ \dot { F _ { k _ { 2 } } } ( t ) - F _ { k _ { 1 } } ( t ) ] d t \geq 0 . } \end{array}$ —that $i s ,$ $F _ { k _ { 1 } } ( \tau )$ second-order stochastically dominates $F _ { k _ { 2 } } ( \tau ) ;$ ; and (iii) the mean percentage of downtime $\eta _ { k _ { 1 } } > \eta _ { k _ { 2 } }$

These distributional properties are important to guide our numerical optimization in Section 6. In particular, Lemma 1(iii) implies that, all else being equal, the mean percentage of downtime (or, equivalently, uptime) over a contract period decreases (increases) as the service provider increases the number of backup resources.

## 4.1. Closed-Loop Optimization

The following Closed-Loop Optimization Algorithm solves the optimization Problem CL and derives the closed-loop solution. Using the characterization of decision stages and the states within each stage as described above, the algorithm finds the stage-wise, state-dependent cost function $J _ { \delta } ^ { * } ( x _ { \delta } , k _ { \delta } )$ and the optimal decision $\boldsymbol { u } _ { \delta } ^ { * } ( \boldsymbol { x } _ { \delta } , \boldsymbol { k } _ { \delta } )$ . These functions are computed recursively backward in time, starting from stage S and ending at stage 1. The optimal expected cost is given by the last step of the algorithm

## 4.2. Online Solution Implementation

In many multistage decision problems, decisions at any given stage may have to be made either with incomplete knowledge of the future or under notvery-reliable distributional assumptions on the future (Bertsekas 1995). In such cases, online optimization should be used (Jaillet and Wagner 2012). An online algorithm resolves the decision model based on se quentially arriving new information on the system behavior as it evolves over time. The closed-loop resource-provisioning strategy presented above is in essence an online algorithm implementation, where the realized downtime serves as input in a piece-by-piece serial fashion as the SLA contract evolves over time. Based on the observed downtime information, different state-contingent control decisions will be made. Therefore, by design, the proposed CL optimization mode provides the online solutions. The following example shows the online implementation of the closed-loop solution.

Assume the number of primary VMs n = 100, and the number of backup VMs can vary from $k = 0 , 1 , \ldots 3$ . Let the service window $T = 1 2 0$ . Let the mean time between failures and mean time to repair of a VM be as follows: $M T B F = 2 , 4 0 0$ , and $M T T R = 2 0$ , respectively

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Closed-Loop Optimization Algorithm
Input: SLA contract parameters: contract duration T, guaranteed service level  $\alpha$ , unit provisioning cost h, unit penalty cost  $\pi$ ;
System parameters: Number of primary VMs n, server mean time between failures MTBF, server mean time to repair MTTR;
User choices: maximum number of stages S, maximum number of backup VMs K, discretization Interval  $\Delta t$ 
Output: Minimum expected cost-to-go  $J_{\delta}^{*}(x_{\delta}, k_{\delta})$  and optimal policy  $u_{\delta}^{*}(x_{\delta}, k_{\delta})$  for  $\delta = 1, \ldots, S$ 
Let  $W = \frac{T}{S}$ ;
Call EmpDistribution(n,k, W) for  $k = 0, 1, \ldots, K$ ; /* see online supplement for the EmpDistribution procedure */
Get downtime probability distribution  $p_{w}(i, n, k)$ , for  $i = 1, \ldots, \left[\frac{W}{\Delta t}\right]$ ;
Let  $z_{\delta}^{max} = (\delta - 1)\left[\frac{W}{\Delta t}\right]$  for  $\delta = 1, \ldots, S$ ;
Let  $k_{\delta} = 0, \ldots, K$  for  $\delta = 1, \ldots, S$ ;
Begin
    $\delta = S;$ $J_{S+1}^{*}(x_{S+1}, k_{S+1}) = 0;$ 
    Repeat
    Let  $z_{\delta} = \{0, 1, \ldots, z_{\delta}^{max}\}$  and denote  $x_{\delta} = z_{\delta}\Delta t$  as the cumulated downtime at the beginning of stage  $\delta$ 
    For each  $(x_{\delta}, k_{\delta})$ , solve Problem CL for  $u_{\delta} = -k_{\delta}, \ldots, K - k_{\delta};$ 
    Let  $u_{\delta}^{*}(x_{\delta}, k_{\delta})$  denote the optimal solution to CL
    Let  $J_{\delta}^{*}(x_{\delta}, k_{\delta})$  denote the minimum expected cost
    $\delta = \delta - 1;$ 
    Until  $\delta = 0$ 
End
</div>

Using these parameters, we generated 5,000 samples with a discrete grid $\varDelta t = 0 . 1$ to derive the empirical downtime distribution. Further assume the cost of provisioning 1 VM per unit of time is $h = 1 .$ , the penalty per unit of time is $\pi = 1 0 0$ , and the SLA service availability requirement is $\alpha = 9 0 \%$ . Now, consider a four-stage decision problem with these data. Figure 2 shows the optimal transition paths based on the closedloop solution to this problem. The nodes denote decisions on the number of backup VMs at each stage, and the associated conditions on $x _ { \delta } , \delta = 1 , 2 , 3 , 4$ , are labeled on the edges.

Note that the length of each stage is $^ { 3 0 , }$ , because $T = 1 2 0 ,$ , and $S = 4 .$ . Because there is no downtime to begin with, we have $x _ { 1 } = 0$ . The optimal closed-loop decision is to provide two backup VMs in the first stage. Given an initial allocation $k _ { 1 } ,$ , the service provider will then adjust the provision accordingly. For example, if the initial allocation is two backups, then the service provider will not make any adjustment. If the initial allocation is three backups, then the service provider will remove one backup VM.

Figure 2. Optimal Transition Paths of Dynamic Resource Provisioning

<table><tr><td> $x_{1}$ </td><td> $x_{2}$ </td><td> $x_{3}$ </td><td> $x_{4}$ </td><td> $x_{5}$ </td></tr><tr><td>0</td><td>30</td><td>60</td><td>90</td><td>120</td></tr><tr><td> $k_{1}$ </td><td> $k_{2}$ </td><td> $k_{3}$ </td><td> $k_{4}$ </td><td> $k_{5}$ </td></tr></table>

![](/api/attachments/RSBEMUES/fulltext/images/313232aecc98f21ea70b87d9d249565410b0822c633df6fb906f3b0573e8bfea.jpg)

The adjustment decision in the second stage will depend on the realized downtime in the first stage. As per the closed-loop solution, if the realized downtime is low $( x _ { 2 } \leq 1 )$ , then the optimal decision is to remove one backup VM in the second stage. If the realized downtime is medium $( 1 < x _ { 2 } \le 8 . 6 )$ , then the optimal decision is to keep two backup VMs in the second stage. If the realized downtime in the first stage is high $( 8 . \bar { 6 } < x _ { 2 } \leq 3 0 )$ , then the optimal decision is to increase to three backup VMs. Decisions for other stages can be interpreted in the same way. Figure 3 translates the optimal decision rules into a resource-provisioning reference chart based on the observed state conditions. The horizontal axis shows the possible range of values for $x _ { 2 } \in [ 0 , 3 0 ] , x _ { 3 } \in [ 0 , 6 0 ]$ , and $x _ { 4 } \in [ 0 , 9 0 ]$ The vertical axis shows the optimal number of backup VMs.

The closed-loop solution yields an easy reference chart to the service provider for making decisions on VM allocation at each stage after observing the actual accrued downtime. For example, at t = 90, the service provider needs to make the fourth-stage decision. Using the right panel of Figure 3, the following decisions can easily be identified for this stage: I $\mathrm { \Delta } \mathrm { f } x _ { 4 } \le 4 . 6 ,$ then one backup VM is needed; if 4 $. 6 < x _ { 4 } \le 1 0 . 2$ , then two backups are needed; and if $x _ { 4 } \geq 1 0 . 2$ , then three backups are necessary.

Clearly, our closed-loop dynamic optimization model finds the state-dependent optimal resource-provisioning policies, based on which practical reference charts as in Figure 3 can be created. As time goes by, the service provider just needs to monitor the incurred downtime in real time and make optimal resource-adjustment decisions using the reference charts.

Because the service provider does not have full information about the future, the online algorithm may not perform as well as an offline algorithm that knows the entire sequence of information in advance and responds optimally. The competitive ratio is defined as the maximum of the ratio between the cost incurred by the online algorithm and that of an ideal offline algorithm over all possible input sequences (Sleator and Tarjan 1985). It is also the worst-case performance ratio between the online algorithm and an optimal offline algorithm. We establish the following competitive ratio bound based on worst-case scenario analysis. The bound shows that the closedloop optimization is competitive.

Proposition 1. The competitive ratio for the closed-loo optimization algorithm $r _ { C L }$ is bounded by $\begin{array} { r } { r _ { C L } < 1 + \frac { K } { n } < 2 } \end{array}$

## 5. Periodic Resource Optimization: Aggressive Strategy

The above closed-loop optimization follows a conservative approach to VM provisioning; it begins with low level of backup VM provisioning and subsequently increases or adjusts the allocation as actual downtimes are successively realized over the stages. On the other hand, an aggressive approach would involve a sufficient backup provisioning to begin with and subsequently decrease or adjust the level of backup VMs as actual downtimes are realized over time. Because the chances of contract violation under the aggressive strategy are significantly less than the conservative strategy, an expected value analysis of the stochastic downtime may be sufficient for the underlying optimization problem. We thus develop an online Certainty-Equivalent (CE) optimization model using the mean value of downtime. The CE model serves as both an approximation to the computationally extensive full stochastic CL model and an implementation of the aggressive strategy. Although closed-loop optimization is designed as an online algorithm, certaintyequivalent optimization has both online and offline counterparts. In the following discussion, we first present the offline model and subsequently develop the online approach.

## 5.1. Of<sup>fl</sup>ine Certainty-Equivalent Optimization

Certainty-equivalent control applies at each stage of the control that would be optimal if the uncertain downtime were fixed at some “typical” values, such as the mean values. It solves a deterministic optimal control problem at each stage. The advantage of the CE model is that the potentially expensive determination of the expected cost is replaced by the calculation of single stage-control trajectory. To develop this model, we define the following variables:

Figure 3. Dynamic Resource Provisioning Reference Chart  
![](/api/attachments/RSBEMUES/fulltext/images/29753f3c248fc8b61347b59ca0a568bc27ecb384d0e02a84e6b0c9c3080408b2.jpg)

![](/api/attachments/RSBEMUES/fulltext/images/365f8f5f0c77e9a3f407f7d6af08a01d48290bc9c1fdad3cea4a2dd41f6f41da.jpg)

![](/api/attachments/RSBEMUES/fulltext/images/0514bf76ee58c5724da3df19d26d90c80ade40a2e00cb3c9a9ea33f2162cd374.jpg)

$G _ { \delta } ( k _ { \delta } ) = \hat { \mathbf { \rho } } .$ The minimum expected total cost from state $k _ { \delta }$ of stage δ till the end

$\Omega _ { \delta } ( k _ { \delta } ) = \mathrm { T o t a l }$ expected downtime from state $k _ { \delta }$ of stage δ till the end along the path corresponding to $G _ { \delta } ( \bar { k } _ { \delta } )$

We present the optimization model underlying the certainty-equivalent approach as follows.

Problem CE

$$
\begin{array}{r l} & G _ {\delta} (k _ {\delta}) = \min \bigg [ h \frac {T}{S} (k _ {\delta} + u _ {\delta}) + \pi \max \{0, d (k _ {\delta} + u _ {\delta}) \\ & \qquad + \Omega_ {\delta + 1} (k _ {\delta} + u _ {\delta}) - \max \{B, \Omega_ {\delta + 1} (k _ {\delta} + u _ {\delta}) \} \} \\ & \qquad + G _ {\delta + 1} (k _ {\delta} + u _ {\delta}) \bigg ] \end{array}
$$

s.t. $k _ { \delta + 1 } = k _ { \delta } + u _ { \delta } , - k _ { \delta } \leq u _ { \delta } \leq K - k _ { \delta } ,$ and $u _ { \delta }$ is integer.

The cost-to-go function in Problem CE is similar to that of Problem CL. However, there are several differences. First, the state variable in Problem CE is $\left( k _ { \delta } \right)$ rather than $( x _ { \delta } , k _ { \delta } )$ . Second, the cost computation is simplified. The expectation outside of the max function in Problem CL is replaced by $d ( k _ { \delta } + u _ { \delta } )$ and $\Omega _ { \delta + 1 } ( k _ { \delta } + u _ { \delta } )$ , which are mean expected downtimes. These simplifications significantly reduce the computation time of the CE model. Compared with the CL model, the CE model could be suboptimal, but is computationally more tractable because of the dramatically reduced state space of the dynamic programming model and, hence, the computational effort. Furthermore, because the CE model uses the mean value of the random downtime, it is a deterministic optimization. We identify a unique path that fully characterizes the resource provisioning and adjustment strategy. This is the offline solution. Proposition 2 shows that the offline CE solution is not unique, and the provision of backup VMs is not stagedependent in an offline implementation.

Proposition 2. If the optimal offline CE solution yields the backup provision sequence $( k _ { 1 } , k _ { 2 } , \ldots , k _ { S } )$ , then any permutation of the sequence also provides an optimal offline backup provision.

The intuition of Proposition 2 is as follows. Note that the deterministic downtime in stage δ is uniquely determined by the number of backup VMs in that stage. In the offline implementation, because the service provider only implements a fixed sequence of controls, the order of the sequence does not matter in terms of total cost minimization. Therefore, any permutation of the sequence yields the same provisioning cost and penalty cost in the deterministic environment. To support an aggressive resource-provisioning strategy, the CE solution would pick a decreasing backup provisioning sequence. This high initial number of backup VMs will minimize the occurrence of downtime at the beginning stages of the contract period. The service provider will then reduce the number of backup VMs in later stages of the contract period if the actual incurred downtime is low.

The offline CE solution is an open-loop solution without knowledge of the future states; thus, it may not be optimal. However, in practice, the service provider could simply choose to implement only the control for the first stage at the beginning of the contract period. As stages arrive over time, the available non-penalizable downtime B can be updated with the observed actual downtime, and the CE model can be resolved with this updated information at every stage. This leads to the online CE optimization.

## 5.2. Online Certainty-Equivalent Optimization

The Online Certainty-Equivalent Optimization Algorithm is presented below. This algorithm consists of two passes: a forward pass and a backward pass. The forward pass constitutes the outer loop, and the backward pass constitutes the inner loop of the algorithm. The evaluation strategy is as follows. Consider any time in the contract period where stages $1 , \ldots , \Delta - 1$ have been realized, and we are at stage <sup>Δ</sup> to decide upon the allocation. Let $C _ { \Delta }$ denote the accrued total realized downtime from stages 1 to stage <sup>Δ</sup>. The forward-passing outer loop starts with $\Delta = 1 .$ . At each realization of stages, <sup>Δ</sup> advances to $\Delta + 1$ until $\Delta = S + 1$ where it ends. At each advance of the outer loop, a backward-passing inner loop is performed. This inner loop starts from $\delta { \bar { = } } S ,$ , and ends at $\delta = \Delta$ . The inner loop is embedded within the outer loop, as illustrated in Figure 4. The solution from the inner loop is a control trajectory $( u _ { \Delta } ^ { * } , . . . , u _ { S } ^ { * } )$ . But only $u _ { \Delta } ^ { * }$ is adopted in the decision making at stage <sup>Δ</sup>. In stage $\Delta + 1$ , the actual downtime till then is observed, the allowable down time B<sup>ˆ</sup> is updated, and another CE optimization problem is solved by using the inner loop.

Two versions of CE optimization are possible. The first version is a simple offline CE solution obtained from a single complete backward pass from stage S to stage 1 of the inner loop in the Online Certainty-Equivalent Optimization Algorithm. The second version is the online solution presented in Figure 4.

Because the CE model does not assume any uncertainty, it identifies a fixed control trajectory. The full set of staged decisions in the offline model is implemented right at the beginning of the contract period. In contrast, the online CE solution could achieve better performance because the decisions are made in a stage-wise manner over time, after observing the actual downtime at each stage and updating the nonpenalizable downtime accordingly. Similar to the CL optimization model, we derive the competitive ratio for the online CE algorithm as shown in Proposition 3.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Online Certainty-Equivalent Optimization Algorithm
Outer Loop
Begin
    Set  $\Delta \leftarrow 1$ ;  $C_{\Delta} \leftarrow 0$ ;  $k_{\Delta} \leftarrow k^{*}$ ;
    Repeat
    Run the Inner Loop;
    Allocate ( $k_{\Delta} + u_{\Delta}^{*}$ ) backup servers for stage  $\Delta$ ;
    Observe actual downtime in stage  $\Delta$  with this decision and denote it as  $\hat{X}_{\Delta}(k_{\Delta} + u_{\Delta}^{*})$ ;
    $C_{\Delta+1} \leftarrow C_{\Delta} + \hat{X}(k_{\Delta} + u_{\Delta}^{*})$ ;
    $k_{\Delta} \leftarrow k_{\Delta} + u_{\Delta}^{*}$ ;
    $\Delta \leftarrow \Delta + 1$ ;
    Until  $\Delta = S + 1$ ;
End
Inner Loop
Begin
    $\hat{B} = \max\{0, B - C_{\Delta}\}$  Allowable total downtime at the beginning of stage  $\Delta$ ;
    $\Omega_{S}(k), k = 0, \ldots, K;$ $G_{S}(k) = h \frac{T}{S} k + \pi \max\{0, \Omega_{S}(k) - \hat{B}\}, k = 0, \ldots, K;$ $\delta = S - 1;$ 
    Repeat
    $B = \hat{B};$ 
    Solve for Problem CE;
    Let  $u_{\delta}^{*}$  denote the optimal solution to CE;
    $\Omega_{\delta}(k) = d(k + u_{\delta}^{*}) + \Omega_{\delta+1}(k + u_{\delta}^{*}), k = 0, \ldots, K;$ $\delta = \delta - 1;$ 
    Until  $\delta = \Delta - 1.$ 
End
</div>

Proposition 3. The competitive ratio for the online CE algorithm is no lower than that under the CL optimization algorithm, and it is bounded by $r _ { C L } \leq r _ { C E } < 1 + \dot { \frac { \kappa } { n } } < 2$

Although the competitive ratio under the CE algorithm is greater than or equal to that under the CL optimization, both algorithms are competitive because their competitive ratios are bounded by 2.

Figure 4. Online Certainty-Equivalent Optimization Strategy

$$
\begin{array}{c c c c c c c c c} 1 & 2 & 3 & \cdot & \cdot & \cdot & S - 1 & S & \text {End} \\ \Delta = 1 & \delta = S, \dots , \Delta \\ & \Delta = 2 & \\ & \delta = S, \dots , \Delta \\ & \Delta = 3 & \\ & \delta = S, \dots , \Delta \\ & \Delta = S & \\ & \delta = S, \dots , \Delta \end{array}
$$

## 6. Aperiodic Resource Optimization: Flexible Interventions

An intervention pertains to the action of adjusting the backup allocation at any time in the contract period. In periodic optimization, an intervention corresponds to a decision stage whose timing is prefixed; contrarily, in aperiodic resource optimization, we allow the time of intervention to be flexible and determined through cost optimization rather than following a set schedule. Accordingly, the decision problem involves two concurrent decisions: when to intervene next and how much backup to allocate at each intervention. This involves a triad of decisions at an intervention: the backup allocation from the current time till the next intervention, the time of next intervention, and the new backup allocation after the intervention time The underlying optimization requires an estimation of the expected total cost from the current intervention time till the end of the horizon. We term the estimation of the cost from the next intervention time till the end as the look-ahead. The service provider may perform single or multiple interventions in the contract period. If the choice is to perform just a single intervention, then there will be just one look-ahead period. This is termed as the Single Intervention with Single Look-ahead strategy. If the choice is to perform multiple interventions, then we could either employ just a single look-ahead period or recursively use multiple look-ahead in estimating the postintervention costs at each intervention. We term these as Multiple Interventions with Single Look-ahead and Multiple Interventions with Multiple Look-aheads (MIML) strat egies, respectively. MIML is inherently more complex because a flexible intervention time has to be determined for each look-ahead period. Determining the interven tion time for each future period needs the knowledge of the intervention time in the current period, which is unknown at the time of decision making. So, we only focus on SISL and MISL. Our objective is to solve an aperiodic optimization problem that is simpler and computationally tractable.

## 6.1. Single-Intervention with Single Look-Ahead Strategy

Assume the service provider only intervenes once over the entire contract period. Denote the intervention time $t \in [ 0 , T ]$ , and the number of backups before and after the intervention time is $k _ { 1 }$ and $k _ { 2 } ,$ respectively. Denote $D _ { t } ( k _ { 1 } )$ and $D _ { T - t } ( k _ { 2 } )$ as the random downtime occurred before and after the intervention. The SISL decision problem is to determine an optimal intervention time $t ^ { * }$ and the optimal resource provisioning $( k _ { 1 } ^ { * } , k _ { 2 } ^ { * } )$ to minimize the expected cost function $C ( k _ { 1 } , k _ { 2 } , t )$

Problem SISL

$$
\begin{array}{r l} \min _ {k _ {1}, k _ {2}, t} C (k _ {1}, k _ {2}, t) & = h k _ {1} t + h k _ {2} (W - t) \\ & \quad + E [ \pi \max \{0, D _ {t} (k _ {1}) + D _ {T - t} (k _ {2}) - B \} ]. \end{array}
$$

The objective function minimizes the expected total cost over the two stages: The first two terms are the backup provisioning cost before and after the intervention, and the third term is the expected penalty cost over the two stages. Next, we examine some properties of the expected cost function.

Lemma 2. The expected cost function of SISL is symmetric: $C ( k _ { 1 } , k _ { 2 } , t ) = C ( k _ { 2 } , \dot { k } _ { 1 } , T - t )$

Lemma 2 is intuitive. Because the downtime of the two stages is independent, we can simply switch the two stages, and the symmetric property holds. Also, the random downtime incurred over the period T is separable. Define $D _ { t , T - t } ( k _ { 1 } , k _ { 2 } ) = D _ { t } ( k _ { 1 } ) + \hat { D _ { T - t } } ( k _ { 2 } )$ and denote the expected downtime as $d _ { t , T - t } ( k _ { 1 } , k _ { 2 } )$ . We have the following property.

Lemma 3. For given $( k _ { 1 } , k _ { 2 } ) .$ , the mean downtime $d _ { t , T - t }$ $( k _ { 1 } , k _ { 2 } ) = T \eta _ { k _ { 2 } } + ( \eta _ { k _ { 1 } } - \eta _ { k _ { 2 } } ) t$

Immediately from Lemma $^ { 3 , }$ we know that the expected downtime with one intervention is a linear function of t. By Lemma $1 , \eta _ { k _ { 1 } } > \eta _ { k } , \mathrm { i f } k _ { 1 } < k _ { 2 } ,$ , so the mean downtime linearly increases in t. Similarly, the mean downtime linearly decreases in t if $k _ { 1 } > k _ { 2 } ,$ and is constant over $t \operatorname { i f } k _ { 1 } = k _ { 2 }$ . Without loss of generality, we next focus on the case $k _ { 1 } < k _ { 2 }$ by assuming the service provider adopt a conservative strategy. The case $k _ { 1 } > k _ { 2 }$ is the mirror case of $k _ { 1 } < k _ { 2 }$

Lemma 4. $H k _ { 1 } < k _ { 2 } ,$ , then the expected penalizable downtime $E [ \mathrm { m a x } [ 0 , D _ { t , T - t } ( k _ { 1 } , k _ { 2 } ) - B ] ]$ is either linearly increasing in t or convex in t.

Define $\Phi _ { k } ( \tau )$ as the normalized cumulative downtime distribution function when k backups are provided, where τ is interpreted as percentage of downtime incurred over the contract period rather than the real downtime. Based on Lemma $^ { 4 , }$ the following proposition shows that the cost function is wellbehaved in t and the unique optimal solution exists.

Proposition 4. $H k _ { 1 } < k _ { 2 }$ , then the expected cost function $C ( k _ { 1 } , k _ { 2 } , t )$ has the following properties:

(i) $I f \ \Phi _ { k _ { 1 } } ( 1 - \stackrel { \cdot } { \alpha } ) = 1 _ { \cdot }$ , then $C ( k _ { 1 } , k _ { 2 } , t )$ is a linear and strictly decreasing function of t;

(ii) $J f \Phi _ { k _ { 2 } } ( 1 - \alpha ) < 1$ , then $C ( k _ { 1 } , k _ { 2 } , t )$ is a linear and strictly increasing function of t if $\pi / h > ( k _ { 2 } - k _ { 1 } ) / ( \eta _ { k _ { 1 } } - \eta _ { k } +$ $\begin{array} { r l } { \int _ { 0 } ^ { 1 - \alpha } \left[ \Phi _ { k _ { 1 } } ( \tau ) - \Phi _ { k _ { 2 } } ( \tau ) \right] \dot { d } \tau ) ; } \end{array}$ ; otherwise, $C ( k _ { 1 } , k _ { 2 } , t )$ is a linear and strictly decreasing function of $t \ i f \ \pi / h < ( k _ { 2 } - k _ { 1 } ) /$ $\begin{array} { r } { ( \eta _ { k _ { 1 } } - \eta _ { k _ { 2 } } + \int _ { 0 } ^ { 1 - \alpha } \left[ \Phi _ { k _ { 1 } } ( \tau ) - \Phi _ { k _ { 2 } } ( \tau ) \right] \dot { d \tau } ) } \end{array}$

(iii) If $\Phi _ { k _ { 2 } } ( 1 - \alpha ) = 1$ and $\Phi _ { k _ { 1 } } ( 1 - \alpha ) < 1$ , then $C ( k _ { 1 } , k _ { 2 } , t )$ is convex in t.

Note that when $t = 0 ,$ , the total number of backups is $k _ { 2 } ,$ , and when $t = T ,$ the total number of backups is $k _ { 1 }$ There are three cases. Proposition 4(i) shows that, if no penalty would be incurred when $k _ { 1 }$ backups are provided over the entire time period T, or, equivalently, $k _ { 1 }$ is so high such that all occurrences of its normalized percentage of downtime are below the critical threshold $1 - \alpha$ (the same holds for $k _ { 2 } ) .$ , then the expected penalizable downtime is always 0 as t increases. The total expected cost only consists of the resource provisioning cost, which linearly increases in k. So as t increases, the total provisioning cost decreases.

Proposition 4(ii) shows that, $\mathrm { i f } k _ { 2 }$ is not large enough such that there is positive probability that the normalized percentage of downtime in some cases would exceed the critical value $1 - \alpha$ (the same holds for $k _ { 1 } ) _ { \mathstrut } .$ then the expected penalizable downtime is linear in t and the expected total cost is also linear in t in this case. If the per-unit penalty cost is relatively more expensive than the per unit provisioning cost such that the condition $\bar { \pi } / h > ( \bar { k _ { 2 } } - k _ { 1 } ) / ( \eta _ { k _ { 1 } } \bar { - } \eta _ { k } +$ $\begin{array} { r } { \int _ { 0 } ^ { 1 - \alpha } [ \Phi _ { k _ { 1 } } ( \tau ) - \Phi _ { k _ { 2 } } ( \tau ) ] d \tau ) } \end{array}$ is satisfied, then the expected penalty cost dominates the provisioning cost, and thus the total cost increases in t. Otherwise, if the provisioning cost is relatively higher than the penalty cost, the total cost decreases in t.

Proposition 4(iii) shows the scenario where $k _ { 2 }$ is large enough so that no penalty would be incurred if $k _ { 2 }$ backups are provided over the entire time period $T ,$ but $k _ { 1 }$ is not large enough so that some penalty would be incurred if $k _ { 1 }$ backups are provided over the entire time period T. Because the provisioning cost decreases in t whereas the expected penalty is convex and increases in t under this case, the expected total cost is convex in t. There exists an optimal intervention time to trade off the total provisioning cost against the expected penalty cost. In sum, the optimal intervention time can be identified as follows.

Proposition 5. Assume $k _ { 1 } < k _ { 2 }$ . The optimal intervention time occurs at:

${ \mathrm { ( i ) } } \quad t ^ { * } = 0 \quad . i f \quad \Phi _ { k _ { 2 } } ( 1 - \alpha ) < 1$ and $\pi / h > ( k _ { 2 } - k _ { 1 } ) /$ $\begin{array} { r l } { ( \eta _ { k _ { 1 } } - \eta _ { k _ { 2 } } + \int _ { 0 } ^ { 1 - \alpha } { [ \Phi _ { k _ { 1 } } ( \tau ) - \Phi _ { k _ { 2 } } ( \tau ) ] } d \tau ) ; } \end{array}$

(ii) $t ^ { * } = \tilde { t } \quad i f \quad \Phi _ { k _ { 2 } } ( 1 - \alpha ) = 1 , \quad \Phi _ { k _ { 1 } } ( 1 - \alpha ) < 1 _ { \ L }$ , and $\begin{array} { r } { \pi / h > ( k _ { 2 } - k _ { 1 } ) / ( \eta _ { k _ { 1 } } - \eta _ { k _ { 2 } } + \int _ { 0 } ^ { 1 - \alpha } { [ \Phi _ { k _ { 1 } } ( \tau ) - \Phi _ { k _ { 2 } } ( \tau ) ] } d \tau ) ; } \end{array}$

(iii) $t ^ { * } = T$ if any of the following cases holds: (a) $\Phi _ { k _ { 1 } } ( 1 - \alpha ) = 1 ; ~ \Phi _ { k _ { 2 } } ( 1 - \alpha ) < 1$ and $\pi / h < ( k _ { 2 } - k _ { 1 } ) /$ $\begin{array} { r } { ( \eta _ { k _ { 1 } } - \eta _ { k _ { 2 } } + \int _ { 0 } ^ { 1 - \alpha } [ \Phi _ { k _ { 1 } } ( \tau ) - \Phi _ { k _ { 2 } } ( \tau ) ] d \tau ) ; \mathrm { ~ o r ~ } ( \mathrm { c } ) \ \Phi _ { k _ { 2 } } ( 1 - \alpha ) = 1 , } \end{array}$ $\begin{array} { r } { \Phi _ { k _ { 1 } } ( 1 - \alpha ) < 1 , a n d \pi / h < ( k _ { 2 } - k _ { 1 } ) / ( \eta _ { k _ { 1 } } - \eta _ { k _ { 2 } } + \int _ { 0 } ^ { 1 - \alpha } [ \Phi _ { k _ { 1 } } ( \tau ) - } \end{array}$ $\Phi _ { k _ { 2 } } ( \tau ) ] d \tau )$

Note that the threshold value $( k _ { 2 } - k _ { 1 } ) / ( \eta _ { k _ { 1 } } - \eta _ { k _ { 2 } } +$ $\begin{array} { r l } { \int _ { 0 } ^ { 1 - \alpha } [ \Phi _ { k _ { 1 } } ( \tau ) - \Phi _ { k _ { 2 } } ( \tau ) ] d \tau ) } \end{array}$ is determined by the backup provisioning choices and their corresponding downtime distributions, as well as the availability requirement, but is independent of the penalty to provisioning cost ratio $\textstyle { \frac { \pi } { h } } .$ All else being equal, if the per-unit penalty is likely more expensive than the per-unit of resource provision, then the service provider tends to intervene early to provide a higher number of backups and avoid possible penalty cost.

When providing $k _ { 1 }$ backups over the entire contract period $\hat { T }$ would incur penalty, but providing $k _ { 2 }$ backups would not, then the optimal intervention time $\acute { \tau }$ is the time when the combined downtime variable $D _ { t , T - t } ( k _ { 1 } , k _ { 2 } ) = D _ { t } ( k _ { 1 } ) + D _ { T - t } ( k _ { 2 } )$ just starts to have nonzero probability of incurring penalizable downtime. The condition $\pi / h > ( k _ { 2 } - \bar { k } _ { 1 } ) ^ { \top } ( \eta _ { k _ { 1 } } - \eta _ { k _ { 2 } } +$ $\begin{array} { r l } { \int _ { 0 } ^ { 1 - \alpha } [ \Phi _ { k _ { 1 } } ( \tau ) - \Phi _ { k _ { 2 } } ( \tau ) ] d \tau ) } \end{array}$ suggests that, to warrant the intervention, the savings from the reduced downtime as well as the penalty cost should be larger than the additional provisioning cost.

Under the conditions specified in Proposition $5 ,$ $t ^ { * } = 0$ and $t ^ { * } = T$ can be easily identified. Given $( k _ { 1 } , k _ { 2 } )$ it might be optimal to keep the number of backup VMs constant over the entire period. When the cost function $C ( k _ { 1 } , k _ { 2 } , t )$ is convex in $t ,$ the optimal intervention time occurs at ${ \tilde { t } } ,$ where <sup>˜</sup>t is defined in the online supplement. Although we can theoretically characterize this time, we still need to design an efficient algorithm to empirically search for it because the intervention time is affected by the empirical downtime distribution, which is a function of the number of backup VMs provided.

## 6.2. The SISL Algorithm

When the empirical downtime distribution satisfies conditions specified in Proposition 5(ii), we need to search for the optimal intervention time. This could involve significant computational effort, as the intervention time is a continuous decision variable. We propose an efficient, offline, two-step approach to solve this problem as shown in the Offline SISL Algorithm. The inner loop employs a search algorithm to find the optimal solution $\mathbf { \bar { \mathit { C } } } ( k _ { 1 } , k _ { 2 } , t ^ { * } )$ for any given $( k _ { 1 } , k _ { 2 } )$ combinations. The outer loop enumerates the limited number of $( k _ { 1 } , k _ { 2 } )$ combinations to find the global optimal $C ( k _ { 1 } ^ { * } , k _ { 2 } ^ { * } , t ^ { * } )$

Note that there are $( K + 1 ) ^ { 2 }$ possible combinations of the $( k _ { 1 } , k _ { 2 } )$ pairs. However, the $( K + 1 )$ combinations where $k _ { 1 } = k _ { 2 }$ can be directly solved without any intervention. This is the first part of the Offline SISL Algorithm. Because of the symmetric property demonstrated in Lemma $^ { 2 , }$ we can further reduce the search by half its size. Thus, the total number of combinations in search is at most $\begin{array} { r } { \frac { ( \bar { K } + 1 ) ^ { 2 } - ( K + 1 ) } { 2 } = \frac { \bar { K ( K + 1 ) } } { 2 } . } \end{array}$ This is the second half of the Offline SISL Algorithm.

The Offline SISL Algorithm employs a module called Search $( k _ { 1 } , k _ { 2 } , T )$ , where we propose a ternary partition search algorithm to numerically search for the optimal intervention time when conditions in Proposition 5(ii) are satisfied. Please refer to the online supplement for details. The online SISL algorithm would outperform the Offline SISL Algorithm due to the value of information. It follows the offline algorithm to implement $k _ { 1 }$ backups in stage 1 until the intervention time $t _ { 1 }$ . At time $t _ { 1 } ,$ , the total realized downtime $\tau = C _ { 1 }$ is observed. The online algorithm then adjusts the allowable downtime $\hat { B } = \operatorname* { m a x } [ 0 ,$ $( 1 - \alpha ) T - C _ { 1 } ]$ , based on which $k _ { 2 }$ is reoptimized, assuming there is no more adjustment in the remaining $( T - t )$ period. For every realized downtime $C _ { 1 } ,$ , we obtain the minimum cost $C ( k _ { 2 } | k _ { 1 } , C _ { 1 } )$ . The expected cost of the online SISL algorithm is computed as $\begin{array} { r l } { \int _ { 0 } ^ { t _ { 1 } } C ( k _ { 2 } | k _ { 1 } , C _ { 1 } ) f _ { k _ { 1 } } ( \tau ) d \tau } \end{array}$

## 6.3. Multiple Interventions with Single Look Ahead Strategy

Under MISL, the optimal cost-to-go is approximated by assuming there is only one intervention opportunity in the remaining time period. Starting from $\delta = 1 \dot { }$ , the MISL strategy repeats the following steps: (1) At the beginning of stage $\delta$ (the last intervention time $t _ { \delta - 1 } )$ , the service provider determines $( k _ { \delta } , t _ { \delta } , k _ { \delta + 1 } )$ to minimize the expected cost over the contract horizon $T - t _ { \delta - 1 } ,$ , assuming there is one intervention in the remaining time period, based on which the service provider implements $k _ { \delta }$ until the next intervention time $t _ { \delta \cdot } ( 2 ) \operatorname { I f } t _ { \delta } = T$ , following the decision $k _ { \delta }$ until the end of contract period; otherwise, following the decision $k _ { \delta }$ until $t _ { \delta } , \delta = \delta + 1$ , and repeat (1). Note that the original decision $k _ { \delta + 1 }$ from the previous stage may not be followed as new decisions about backup resource provision are made at times $t _ { \delta } .$ . Figure 5 graphically illustrates the decision sequence.

Problem MISL

$$
\begin{array}{l} H _ {\delta} (x _ {\delta}, k _ {\delta}) = \min \bigl [ h k _ {\delta} (T - t _ {\delta - 1}) + h u _ {\delta} (T - t _ {\delta - 1} - t) \\ \qquad + E \bigl [ \pi \max \{0, x _ {\delta} + D (k _ {\delta} + u _ {\delta}) - \max (B, x _ {\delta}) \} \\ \qquad + H _ {\delta - 1} (x _ {\delta - 1}, k _ {\delta - 1}) \bigr ] \bigr ] \end{array}
$$

$$
\begin{array}{l} \text { s.t. } x _ {\delta + 1} = x _ {\delta} + d (k _ {\delta} + u _ {\delta}), k _ {\delta + 1} = k _ {\delta} + u _ {\delta}; - k _ {\delta} \leq u _ {\delta} \leq K - k _ {\delta}, \\ \text { and } u _ {\delta} \text { is   integer. } \end{array}
$$

Here, $H _ { \delta } ( x _ { \delta } , k _ { \delta } )$ ) is the cost-to-go function and $T - t _ { \delta - 1 }$ is the remaining contract window at the beginning of stage $\delta . H _ { \delta - 1 } ( x _ { \delta - 1 } , k _ { \delta - 1 } )$ is the cost incurred up to stage $\delta - 1$ and the initial cost $H _ { 0 } ( x _ { 0 } , k _ { 0 } ) = 0$ . This optimization problem follows the same interpretation of Problem CL. The difference is that now the time of intervention is also a decision variable, and we use a forward strategy to solve the problem. The full MISL model implementation is thus more challenging than the CL model because it not only depends on the observed downtime information, but needs to search for the optimal intervention times.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Offline SISL Algorithm
Input: maximum number of backups K and contract duration T;
Output:  $I(k_{1}^{*}, k_{2}^{*}, t^{*})$  and corresponding total cost TC;
Main: SISL(T)
Begin
    I = (0,0,0);
    TC = G, where G is a very large number;
    For  $k = 0, \ldots, K$ , do
    Compute  $C(k,k,T) = hkT + E[\pi\max\{0, D_{T}(k) - B\}]$ ;
    If  $C(k,k,T) &lt; TC$  then
    $TC = C(k,k,T)$ ;
    $I = (k,k,T)$ ;
    End If
End
For  $k_{1} = 0, \ldots, K - 1$ , do
    For  $k_{2} = k_{1} + 1, \ldots, K$ , do
    If conditions in Proposition 5(i) are satisfied
    $t^{*} = 0$ ;
    $C(k_{1}, k_{2}, t^{*})$ ;
    Else if conditions in Proposition 5(iii) are satisfied
    $t^{*} = T$ ;
    $C(k_{1}, k_{2}, t^{*})$ ;
    Else
    Call Search ( $k_{1}, k_{2}, T$ ); /*the search algorithm is executed under conditions in Proposition 5(ii)*/
    End
    If  $C(k_{1}, k_{2}, t^{*}) &lt; TC$  then
    $TC = C(k_{1}, k_{2}, t^{*})$ ;
    $I = (k_{1}, k_{2}, t^{*})$ ;
    End If
    End
End
End
</div>

The Offline MISL Algorithm calls for a series of SISL optimizations until no more intervention can be found. The online MISL algorithm involves an update of B that is based on the realized downtime observed at the intervention time, rather than the expected downtime as in the Offline MISL Algorithm. Consider the example in Figure 5. The online algorithm follows the offline MISL solution $( k _ { 1 } , t _ { 1 } )$ to implement $k _ { 1 }$ backups and to intervene at $t _ { 1 } . \ \mathrm { A t } \ t _ { 1 } ,$ following the downtime distribution $F _ { k _ { 1 } } ( \tau )$ , the total realized downtime $\tau = C _ { 1 }$ is observed. The online algorithm then adjusts the allowable downtime $\hat { B } = \operatorname* { m a x } [ 0 , ( 1 - \alpha ) T - \check { C _ { 1 } } ]$ and resolves the offline MISL algorithm in the remaining period $( T - t _ { 1 } )$ to yield an optimal first-stage solution $( k _ { 2 } , t _ { 2 } , k _ { 3 } )$ and minimum expected cost $\backslash \overline { { C ( k _ { 2 } , t _ { 2 } , k _ { 3 } | k _ { 1 } , C _ { 1 } ) } }$ , where only the first part of the solution $( k _ { 2 } , t _ { 2 } )$ will be implemented, and so on.

The expected cost of the online MISL algorithm with two interventions is computed as $\int _ { 0 } ^ { t _ { 1 } } C ( \breve { k } _ { 2 } , t _ { 2 } , k _ { 3 } |$ $k _ { 1 } , C _ { 1 } ) f _ { k _ { 1 } } ( \tau ) d \tau$ . Clearly, the expected cost of the online MISL algorithm depends on the realized downtime in each step of the algorithm implementation $( C _ { 1 } , C _ { 2 } ,$ etc.). The state space grows exponentially as the number of interventions increases. However, as shown in Section 5.4 of the online supplement, the algorithm runs in polynomial time and thus is considered as “fast.”

Now, we turn to competitive ratio analysis. The following proposition establishes the competitive ratios of both SISL and MISL online algorithms.

Proposition 6. (i) The competitive ratio of the SISL and MISL online algorithm is the same, which is bounded by 2 $( i . e . , r _ { S I S L } = r _ { M I S L } < 1 + { \frac { K } { n } } < 2 ) ;$ (ii) The competitive ratio of SISL and MISL online algorithm is lower than that of the CL algorithm if the number of decision stages in CL is large enough $( i . { \dot { e } } . , \ r _ { S I S L } = r _ { M I S L } \ < \ r _ { C L } \ i f \ t _ { 1 } ^ { * } > \tilde { \frac { T } { S } } )$

The competitive ratio analysis of all our online algorithms (Propositions 1, 3, and 6) show that our proposed solutions are competitive and perform well in the worst-case scenarios. In particular, when the number of decision stages in the periodic intervention policy is relatively large, the aperiodic intervention algorithms tend to yield better online performance than the periodic online algorithms.

## 7. Computational Analyses

In this section, we comprehensively evaluate the solu tion quality and computational performance of both the periodic and aperiodic resource-optimization models under different system configurations.

We classify the parameters of the cloud resourcemanagement problem into four general categories. We choose two values for each parameter in our main experiments. The first category includes two clientspecific parameters: required service availability α (0.9 for low availability and 0.99 for high availability) and contract duration T (30 days for short term and 180 days for long term). The second category involves two service-specific parameters: the number of primary VMs n (100 for small-size service contract and 1,000 for large-size service contract), and the penalty/ provision cost ratio per VM (100 for low penalty and 1,000 for high penalty). The third category consists of two system-specific operational-level parameters: the mean time between failures of a physical server (60 days for failure-prone systems and 300 days for fault-tolerant systems), and the mean time to repair (half day). The fourth category pertains to resource-optimization parameters. It involves the service provider’s decisions regarding the maximum

## Of<sup>fl</sup>ine MISL Algorithm

Input: maximum number of backups K and contract duration T; Output: $I _ { W } = ( k _ { 1 } ^ { * } , k _ { 2 } ^ { * } , t ^ { * } )$ and corresponding $C ( k _ { 1 } ^ { * } , k _ { 2 } ^ { * } , t ^ { * } )$ Begin ${ \bar { W } } = T ;$ While $W > 0$ Call SISL (W); $W = W - t ^ { * } ;$ $B = \operatorname* { m a x } [ 0 , B - t ^ { * } \eta _ { k _ { 1 } ^ { * } } ] ;$ End While End

number of backup VMs K to provide, which we set as 10% of the number of primary backup VMs required in SLA (10% n). The service provider can choose from four online algorithm choices corresponding to periodic intervention (CL and online CE) or aperiodic intervention (online SISL and online MISL) policies. The rationale of the experiment design and detailed solutions of all experiments are provided in the online supplement. We implemented our algorithms in R 3.4 (64-bit edition). An Intel(R) Core(TM) i7-7500U 2.90- GHz processor equipped with 8 GB of RAM was used for all experiments.

## 7.1. Effect of Intervention

Using the static, no-intervention (denoted as NI) optimal solution of Yuan et al. (2018) as a benchmark, we first demonstrate the performance improvement under the periodic policies (the CL model and the online CE model, denoted as $C E ^ { \mathrm { o n } } )$ . Denote the expected costs under NI, CL, and $\mathrm { C E } ^ { \mathrm { o n } }$ models as E[NI], E[CL], and $E [ C E ^ { \mathrm { o n } } ]$ . We define the expected cost performance ratio as $\begin{array} { r } { R [ C L ] = \frac { E [ N I ] - E [ C L ] } { E [ N I ] } } \end{array}$ and $R [ C E ^ { o n } ] =$ $\frac { \ ' E [ N I ] - E [ C E ^ { o n } ] } { E [ N I ] } .$ , respectively, to measure the relative cost reduction of the CL and $\mathrm { C E } ^ { \mathrm { o n } }$ model from the nointervention benchmark. The larger the ratio, the higher the expected cost reduction.

Table 1 shows the expected cost-performance ratios under different configurations when there are eight decision stages to represent relatively frequent periodic interventions. Tables A4 and A5 in the online supplement provides the complete model solutions and the expected costs of the NI, CL, and $\mathrm { C E } ^ { \mathrm { o n } }$ models. Several interesting observations can be made from Table 1. First, both the online CE model and the CL model have the potential to significantly reduce the expected cost due to the ability to adjust the backup provision dynamically over the contract duration. The highest cost reduction achieved is around 44%–46% for the online CE model and 48%–50% for the CL model when the service contract size is small, the availability is low, the penalty cost is low compared with provisioning cost, and in the fault-tolerant system.

Figure 5. Illustration of MISL Strategy  
![](/api/attachments/RSBEMUES/fulltext/images/eed635326c3bbab66e4cb01fd0e66813e296556c6ea09ffe8f0fd372857daab0.jpg)

Second, we observe two scenarios where the cost performance of the online CE model is comparable to that of the no-intervention benchmark (<sup>−</sup>3.6% and <sup>−</sup>1.6% in Table 1). This is because the CE model uses the deterministic mean downtime approximation rather than the stochastic downtime distribution in making the dynamic adjustment decisions. Both cases occur for short-term contracts when the required availability is low, provision/penalty cost ratio is high, and is managed by fault-tolerant servers. Fortunately, in such cases, the CL model can significantly reduce the costs. Thus, we caution the contract managers of such cases and recommend the CL model in these instances.

Third, comparing the best-performing CL model with the no-intervention benchmark, we identify scenarios where there is little need for intervention (within 2% expected cost reduction). These scenarios occur when the contract size is large, the required availability is high, the penalty cost is low compared with provisioning cost, and in the fault-prone system.

Table 1. Expected Cost-Performance Ratios of CL and Online CE Models

<table><tr><td rowspan="2" colspan="3">SLA requirements</td><td colspan="4">MTBF low (fault-prone)</td><td colspan="4">MTBF high (fault-tolerant)</td></tr><tr><td colspan="2"> $\pi/h_{\text{Low}}$ </td><td colspan="2"> $\pi/h_{\text{High}}$ </td><td colspan="2"> $\pi/h_{\text{Low}}$ </td><td colspan="2"> $\pi/h_{\text{High}}$ </td></tr><tr><td>n</td><td>T</td><td> $\alpha$ </td><td>R[CL]</td><td> $R[CE^{\text{on}}]$ </td><td>R[CL]</td><td> $R[CE^{\text{on}}]$ </td><td>R[CL]</td><td> $R[CE^{\text{on}}]$ </td><td>R[CL]</td><td> $R[CE^{\text{on}}]$ </td></tr><tr><td rowspan="4">Small</td><td rowspan="2">Short term</td><td>Low</td><td>16.5%</td><td>11.5%</td><td>38.4%</td><td>16.7%</td><td>48.1%</td><td>44.6%</td><td>43.4%</td><td>-3.6%</td></tr><tr><td>High</td><td>3.4%</td><td>3.0%</td><td>15.5%</td><td>9.8%</td><td>15.3%</td><td>13.4%</td><td>20.8%</td><td>8.4%</td></tr><tr><td rowspan="2">Long term</td><td>Low</td><td>17.2%</td><td>12.1%</td><td>39.0%</td><td>19.9%</td><td>49.8%</td><td>45.7%</td><td>44.8%</td><td>3.0%</td></tr><tr><td>High</td><td>7.5%</td><td>7.4%</td><td>18.9%</td><td>12.6%</td><td>20.5%</td><td>17.0%</td><td>24.7%</td><td>17.2%</td></tr><tr><td rowspan="4">Large</td><td rowspan="2">Short term</td><td>Low</td><td>6.6%</td><td>5.5%</td><td>11.9%</td><td>2.6%</td><td>23.6%</td><td>19.0%</td><td>23.1%</td><td>-1.6%</td></tr><tr><td>High</td><td>0%</td><td>0%</td><td>6.6%</td><td>4.5%</td><td>3.0%</td><td>2.7%</td><td>14.3%</td><td>5.8%</td></tr><tr><td rowspan="2">Long term</td><td>Low</td><td>7.0%</td><td>5.7%</td><td>12.2%</td><td>3.5%</td><td>24.2%</td><td>19.5%</td><td>23.7%</td><td>1.8%</td></tr><tr><td>High</td><td>1.4%</td><td>1.3%</td><td>8.7%</td><td>6.6%</td><td>5.3%</td><td>5.1%</td><td>17.1%</td><td>11.1%</td></tr></table>

Because the expected cost reduction is limited, the service provider may find the computationally expensive CL model not be economically justified. In such cases, if the service provider still prefers to perform dynamic interventions, we recommend the online CE model due to the closeness of its solution to the optimum and its computational efficiency.

On average, across all configurations, the online CE model and the CL model achieved cost reductions of 10.4% and 19.4%, respectively. Overall, the benefits of dynamic optimization are more significant for small contracts with low availability in fault-tolerant systems.

## 7.2. Effect of Flexible Timing

In the following discussion, we compare periodic and aperiodic intervention policies to examine under what conditions it is beneficial to perform flexible interventions. We choose the best-performing CL model under the periodic policy as the benchmark and compare it with online SISL and online MISL solutions. Obviously, the number of decision stages affects the CL solution. Because there is one intervention in the online SISL model by design, we choose the two-stage CL model (CL2) for its comparison. Note that the MISL model with two interventions establishes a performance lower bound of MISL policy. We use it as a conservative benchmark to compare the performance. Denote the corresponding three-stage CL model as CL3. Define the expected cost performance ratio of the online SISL and MISL models as $\begin{array} { r } { R [ S I S L ^ { o n } ] = \frac { E [ C L 2 ] - E [ S I S L ^ { o n } ] } { E [ C L 2 ] } } \end{array}$ and $\begin{array} { r } { R [ M I S L ^ { o n } ] = \frac { E [ C L 3 ] - E [ M I S L ^ { o n } ] } { E [ C L 3 ] } . } \end{array}$ , respectively. So a positive ratio indicates expected cost reduction of the aperiodic intervention over the periodic intervention policies. Because the contract length does not seem to significantly affect the solution, we focus on short-term contracts for illustration purposes. Table 2 presents expected cost-performance ratios of the online SISL and online MISL policies under different system configurations.

We note that the aperiodic models may not necessarily outperform the periodic models. The main reason is the use of single look-ahead until the end of the horizon at each intervention stage of the MISL strategy. As Table 2 shows, there is a clear trade-off between the potential gain brought by flexible timing and the potential loss due to the myopic single lookahead. We find that the performance differences in smallsized contracts are more than those in large-sized contracts. When the contract size is small, it is better to use the CL model when the penalty/provisioning cost ratio is low in fault-prone systems, and when both the penalty/provisioning cost ratio is low and the availability is high in fault-tolerant systems.

On average, the highest cost reduction of the online SISL algorithm over the CL2 model is 23.3% and of the online MISL algorithm over the CL3 model is 20.3%, respectively. Please see Table A7 of the online supplement for expected costs under different models. The aperiodic models outperform the periodic models significantly when the contract size is small, availability is low, and in fault-tolerant systems. Intuitively, this is because under these scenarios, the total required number of backups is relatively small; thus, the marginal effect of adding or removing one backup is significant. Flexible timing allows for fine-tuning the marginal benefit-cost trade-off and thus turns out to be beneficial.

## 8. Model Validation with Amazon EC2 Service Structure

In this section, we validate our models based on actual pricing and service-credit data on dedicated hosts obtained from the Amazon EC2 website. Consider the case of a client requesting to contract with Amazon for n instances (VMs). A dedicated host is configured to support one VM at a time. For simplicity, we consider both small and large contract sizes, denoted by n = {100, 1,000} primary VMs, respectively.

The contract can have different configurations based on Amazon instance types and its pricing/penalty structures.<sup>7</sup> For illustration purposes, we choose the 1-year contract for the cheapest instance type a1 and a similar 1-year contract for the most expensive instance type p3. These instance-type designations are from the Amazon EC2 website. The monthly price p for one a1 VM is \$206.59 and for one p3 VM is \$13,415.94 Because service credits for violations of uptime guarantees are offered as fractions of the prices charged, it is realistic to consider the low-cost a1 hosts to be less fault-tolerant (or, equivalently, more fault-prone)

Table 2. Expected Cost-Performance Ratios of Online SISL and Online MISL Models

<table><tr><td rowspan="2" colspan="2">SLA requirements</td><td colspan="4">MTBF low (fault-prone)</td><td colspan="4">MTBF high (fault-tolerant)</td></tr><tr><td colspan="2"> $\pi/h_{\text{Low}}$ </td><td colspan="2"> $\pi/h_{\text{High}}$ </td><td colspan="2"> $\pi/h_{\text{Low}}$ </td><td colspan="2"> $\pi/h_{\text{High}}$ </td></tr><tr><td>n</td><td> $\alpha$ </td><td> $R[SISL^{\text{on}}]$ </td><td> $R[MISL^{\text{on}}]$ </td><td> $R[SISL^{\text{on}}]$ </td><td> $R[MISL^{\text{on}}]$ </td><td> $R[SISL^{\text{on}}]$ </td><td> $R[MISL^{\text{on}}]$ </td><td> $R[SISL^{\text{on}}]$ </td><td> $R[MISL^{\text{on}}]$ </td></tr><tr><td rowspan="2">Small</td><td>Low</td><td>-6.0%</td><td>-7.5%</td><td>0.9%</td><td>1.1%</td><td>23.3%</td><td>10.7%</td><td>14.3%</td><td>20.3%</td></tr><tr><td>High</td><td>-3.1%</td><td>-4.2%</td><td>-1.7%</td><td>-0.6%</td><td>-2.7%</td><td>-6.8%</td><td>-0.3%</td><td>2.4%</td></tr><tr><td rowspan="2">Large</td><td>Low</td><td>0.7%</td><td>0.0%</td><td>-1.6%</td><td>-1.6%</td><td>0.8%</td><td>-0.8%</td><td>-1.4%</td><td>-2.3%</td></tr><tr><td>High</td><td>0.0%</td><td>0.0%</td><td>-0.1%</td><td>-0.5%</td><td>-0.3%</td><td>-0.9%</td><td>0.7%</td><td>-1.2%</td></tr></table>

than the high-cost $p 3$ hosts. Accordingly, we term the two instance types a1 and $p 3$ considered in this study as fault-prone and fault-tolerant instances, respectively. As we do not have access to the MTBF and MTTR data from Amazon, we obtained these parameters from the server logs provided by the Center for Computational Research (CCR) at the University at Buffalo, which is a high-performance computing node. Using these parameters as surrogates for the Amazon data-center operations, we conducted a detailed computational study of the proposed algorithms using their price and penalty structures for the a1 and $p 3$ instance types. These results can be easily replicated if the server log data from Amazon are available.

Our experiment consisted of four independent factors: contract size {small, large}, level of fault tolerance of the instances {fault-prone, fault-tolerant}, provisioning cost {low, medium, high}, and penalty cost {low, medium, high}. Accordingly, a fully crossed experimental design consisting of 36 unique treatments has been carried out. In all these treatments, we consider a 1-month contract window. We set $\psi = 1 2 , 0 0 0$ as the number of discrete time intervals in the 1-month evaluation period, which is equivalent to about 4 minutes per interval. This is consistent with what is done in practice to measure downtime. For example, Amazon S3 tracks and calculates the error rate (i.e., downtime) for each Amazon S3 service account in every 5-minute interval in the monthly billing cycle.

Define the selling price per VM per unit time interval as ${ \bar { p } } = p / \psi$ . First, we assume the resource provisioning cost per VM per unit time is a percentage of the selling price per VM per unit time: $h = \{ 1 0 \% , 3 0 \% , 5 0 \% \} * \bar { p } .$ These define three levels of the provisioning cost. Second, we estimate the penalty cost per unit time π based on Amazon penalty-price structures. There are three cases: (1) Amazon pays no penalty if the monthly uptime percentage is greater than or equal to 99.95%; (2) it provides 10% of the monthly fee as service credit if the monthly uptime percentage is between 99% and 99.95%; and (3) it pays 30% of the monthly fee as service credit if the monthly uptime percentage is below 99%. Clearly, Amazon EC2 SLA belongs to the high-availability (high α) scenario. For a given n, recall that the density and cumulative distribution functions of the random downtime for k backup servers are $f _ { k } ( \tau )$ and $F _ { k } ( \tau )$ , respectively. We use the baseline distribution $\begin{array} { r } { F _ { 0 } ( \tau ) ( \mathrm { i . e . , } } \end{array}$ when no backup is provided) as the basis for calculating the expected unit penalty cost as follows:

$$
\hat{\pi} = \frac{10\% \times n\times p\times\left[F_{0}(0.01) - F_{0}(0.005)\right] + 30\% \times n}{\times p\times\left[1 - F_{0}(0.01)\right]}\]\[\mu (\tau - 0.01|\tau \geq 0.01) + j\times \sigma(\tau - 0.01|\tau \geq 0.01).
$$

Here, the numerator is the expected total service credit amount paid for n VMs, and the denominator is the (expected penalizable downtime $+ j \times$ standard de viation of penalizable downtime), where we set $j =$ $\{ - 1 , 0 , 1 \}$ to derive three (i.e., high, medium, and low) estimates of π. The expected penalizable downtime is computed as $\begin{array} { r } { \mu ( \tau - 0 . 0 1 \hat { \vert \tau } \geq 0 . 0 \hat { 1 } ) = \int _ { 0 . 0 1 } ^ { 1 } ( \tau - 0 . 0 1 ) f _ { 0 } ( \tau ) d \tau , } \end{array}$ and the variance of penalizable downtime is calculated as $\begin{array} { r } { \sigma ^ { 2 } ( \tau - 0 . 0 1 | \dot { \tau } \geq 0 . 0 1 ) = \int _ { 0 . 0 1 } ^ { 1 } ( \tau - 0 . 0 1 ) ^ { 2 } f _ { 0 } ( \tau ) d \tau - } \end{array}$ $\begin{array} { r } { [ \int _ { 0 . 0 1 } ^ { 1 } ( \tau - 0 . \dot { 0 } 1 ) f _ { 0 } ( \tau ) \dot { d } \tau ] ^ { 2 } } \end{array}$ . Based on Amazon data, Table 3 shows the values of the π/h ratio used in the 36 treatments of the experiment. Together, the 36 treatments cover a wide variety of real-world use cases. This validation can be repeated for any other system parameters in a cloud data center.

In practice, service providers such as Amazon typically configure the resource provisioning at the time the service contract is offered. They adopt a static resource provisioning strategy as required by the service contract and may or may not deploy backups. We as sume that Amazon optimally chooses the number of backups to deploy and that the deployment does not change over the 1-month period. We implemented our periodic intervention and aperiodic intervention strategies in each of the 36 treatments using their respective parametric settings. We demonstrate the potential cost savings that can be generated using our dynamic resource-provisioning framework in the following discussion.

Table 3. The π/h Ratio Under Different Treatments

<table><tr><td rowspan="2">Contract size</td><td rowspan="2"> $h/\bar{p}$ </td><td colspan="3">Fault-prone VMs</td><td colspan="3">Fault-tolerant VMs</td></tr><tr><td> $\hat{\pi}(j=1)$ </td><td> $\hat{\pi}(j=0)$ </td><td> $\hat{\pi}(j=-1)$ </td><td> $\hat{\pi}(j=1)$ </td><td> $\hat{\pi}(j=0)$ </td><td> $\hat{\pi}(j=-1)$ </td></tr><tr><td rowspan="3">Small</td><td>0.1</td><td>477.53</td><td>546.40</td><td>638.48</td><td>1,454.36</td><td>2,108.53</td><td>3,832.27</td></tr><tr><td>0.3</td><td>159.18</td><td>182.13</td><td>212.83</td><td>484.79</td><td>702.84</td><td>1,277.42</td></tr><tr><td>0.5</td><td>95.51</td><td>109.28</td><td>127.70</td><td>290.87</td><td>421.71</td><td>766.45</td></tr><tr><td rowspan="3">Large</td><td>0.1</td><td>3,030.06</td><td>3,037.95</td><td>3,045.87</td><td>3,532.41</td><td>3,785.64</td><td>4,078.00</td></tr><tr><td>0.3</td><td>1,010.02</td><td>1,012.65</td><td>1,015.29</td><td>1,177.47</td><td>1,261.88</td><td>1,359.33</td></tr><tr><td>0.5</td><td>606.01</td><td>607.59</td><td>609.17</td><td>706.48</td><td>757.13</td><td>815.60</td></tr></table>

Table 4. Expected Cost Savings of Periodic Intervention over Static Backup Deployment

<table><tr><td rowspan="2">Contract size</td><td rowspan="2"> $h/\bar{p}$ </td><td colspan="3">Fault-prone VMs</td><td colspan="3">Fault-tolerant VMs</td></tr><tr><td> $\hat{\pi}(j=1)$ </td><td> $\hat{\pi}(j=0)$ </td><td> $\hat{\pi}(j=-1)$ </td><td> $\hat{\pi}(j=1)$ </td><td> $\hat{\pi}(j=0)$ </td><td> $\hat{\pi}(j=-1)$ </td></tr><tr><td rowspan="3">Small</td><td>0.1</td><td>13.79%</td><td>13.94%</td><td>14.14%</td><td>21.80%</td><td>23.86%</td><td>30.03%</td></tr><tr><td>0.3</td><td>9.10%</td><td>11.30%</td><td>14.1%</td><td>21.79%</td><td>20.94%</td><td>21.36%</td></tr><tr><td>0.5</td><td>2.93%</td><td>4.27%</td><td>6.07%</td><td>23.69%</td><td>22.22%</td><td>20.84%</td></tr><tr><td rowspan="3">Large</td><td>0.1</td><td>9.64%</td><td>9.65%</td><td>9.67%</td><td>20.88%</td><td>21.53%</td><td>22.28%</td></tr><tr><td>0.3</td><td>6.60%</td><td>6.60%</td><td>6.60%</td><td>14.66%</td><td>14.86%</td><td>15.09%</td></tr><tr><td>0.5</td><td>4.80%</td><td>4.81%</td><td>4.82%</td><td>13.78%</td><td>13.85%</td><td>13.95%</td></tr></table>

## 8.1. Periodic Model Implementation

We compare our periodic dynamic resource-provisioning model with the static model commonly used in practice. Table 4 presents the percentage of cost savings under different treatment conditions.

Other things being equal, as the unit provisioning cost decreases and the unit penalty cost increases, the percentage of cost savings increases. This is not surprising because lower provisioning cost directly leads to operational cost savings. The high unit penalty cost justifies the benefit of using a dynamic adjustment strategy rather than a static provisioning strategy. Overall, the savings over the static model is up to 30%.

Similar to the insights gained from the main experiments, we find that managing small contracts yields higher cost savings than large contracts, and fault-tolerant systems achieve higher cost savings than fault-prone systems. Intuitively, this is because the mean and variance of the downtime distribution are small in both cases, which require small number of backups. The larger marginal benefit of adjusting VM provisioning leads to higher cost savings.

## 8.2. Aperiodic Model Implementation

In the following, we demonstrate the benefit of implementing the aperiodic intervention strategy over the periodic intervention. To have a fair comparison, we should allow the MISL and CL models to have the same number of stages (S). Because an MISL model has at least three stages, for illustration purposes, we choose S = 3 and denote the three-stage CL model as CL3. As the number of stages increases, the advantage of aperiodic intervention over periodic intervention would diminish, and this is intuitive. Table 5 presents the percentage of cost savings of the online MISL model over the CL3 model under different treatment conditions, given by <sup>E[CL3]−E[MISLon]</sup>. Note that a positive value indicates that E CL3 the MISL model yielded lower expected cost than the CL3 model.

We see that the highest percentage of cost savings of the aperiodic intervention over periodic intervention is 8.08%. This occurs for small-sized contracts with fault-tolerant VMs when the penalty/provisioning cost ratio is moderately high (i.e., 484.79). Based on these experimental assessments, a decision tree for the choice of intervention strategy by Amazon EC2 can be formulated as in Figure 6.

<table><tr><td rowspan="2">Contract size</td><td rowspan="2"> $h/\bar{p}$ </td><td colspan="3">Fault-prone VMs</td><td colspan="3">Fault-tolerant VMs</td></tr><tr><td></td><td> $\hat{\pi}(j=0)$ </td><td> $\hat{\pi}(j=-1)$ </td><td> $\hat{\pi}(j=1)$ </td><td> $\hat{\pi}(j=0)$ </td><td> $\hat{\pi}(j=-1)$ </td></tr><tr><td rowspan="3">Small</td><td>0.1</td><td>0.49%</td><td>0.64%</td><td>0.59%</td><td>-2.3%</td><td>-7.9%</td><td>-5.21%</td></tr><tr><td>0.3</td><td>-2.29%</td><td>-2.16%</td><td>-1.96%</td><td>8.08%</td><td>5.7%</td><td>-0.53%</td></tr><tr><td>0.5</td><td>-4.03%</td><td>-4.68%</td><td>-6.12%</td><td>3.76%</td><td>7.5%</td><td>4.91%</td></tr><tr><td rowspan="3">Large</td><td>0.1</td><td>-0.67%</td><td>-0.67%</td><td>-0.67%</td><td>0.5%</td><td>0.49%</td><td>0.31%</td></tr><tr><td>0.3</td><td>-0.47%</td><td>-0.47%</td><td>-0.47%</td><td>-0.9%</td><td>-0.77%</td><td>-0.63%</td></tr><tr><td>0.5</td><td>-0.97%</td><td>-0.98%</td><td>-0.98%</td><td>-1.71%</td><td>-1.65%</td><td>-1.58%</td></tr></table>

Table 5. Expected Cost Savings of Aperiodic Intervention over Periodic Intervention

The above analysis yields a proof-of-concept of the proposed intervention framework and demonstrates the efficiencies of the proposed algorithms using Amazon EC2 price/penalty data as a testbed of use cases, in conjunction with the system-specific parameters drawn from the CCR data. This study also yields a decision-tree-based strategy for any contract administrator to follow in the choice of intervention policies by appropriately calibrating them according to the prevailing contract-specific, system-specific, and service-specific parameters.

## 9. Discussion of Managerial Implications

In this research, we develop different resourcemanagement strategies to support the cloud contract administrators’ needs to conservatively or aggressively manage virtual infrastructure resources and preferences to periodically or aperiodically adjust the backup VMs.

Figure 6. Decision Tree Calibration of CL vs. MISL Intervention Policies  
![](/api/attachments/RSBEMUES/fulltext/images/1d80852129f4f86f4c5f806171ee20301b03be68c89cf4f1e506645d5917f09f.jpg)

Our CL model supports conservative resource provisioning under the periodic intervention policy. The CL algorithm yields a reference chart of optimal allocations for a given service agreement, and the service provider would dynamically allocate the backup VMs according to the realized conditions during the course of the contract. It offers valuable guidance for cloud service providers to structure the VM resources in the data center based on client service agreements in a dynamic and uncertain operating environment. The dynamic optimization significantly outperforms static optimization (no intervention), especially for small contracts that require low availability in fault-tolerant systems.

In the event where the cloud service providers prefer to use an aggressive resource-management strategy, we recommend the use of the computationally costeffective online CE model. Although the CL model would yield optimal allocations, the online CE model is quite cost-effective and yields near-optimal allocations in most cases, and especially for large contracts when the penalty/provisioning cost ratio is low and the required availability is high in fault-prone systems.

In general, solving the aperiodic optimization problem is more computationally demanding than the periodic optimization. The trade-off between the periodic and aperiodic optimization is the additional cost reduction brought by flexible interventions and the increased time complexity to solve the aperiodic models. Based on the evaluation of use cases constructed from Amazon EC2 price and service credit structure, we find that it is more beneficial to employ aperiodic intervention than periodic intervention when managing small-sized service contracts with fault-tolerant VMs under high availability requirements.

To guide contract administrators to choose between the best-performing periodic (CL) and aperiodic (online

MISL) intervention policies, we compare their expected costs based on which we can construct a decisiontree recommendation. This analysis serves as a proofof-concept for any cloud data center to adopt our analytical strategy in SLA resource management. Through comprehensive testing of our model using both synthetic data and Amazon use cases, we provide collaborative evidence that our proposed dynamic backup resource-provisioning strategy can generate significant cost savings over the static backup provisioning approach.

Overall, our model is most suitable to IaaS providers’ virtual infrastructure resource management based on their precommitted resource requirements in the service contracts. Our model can be applied to both stateless and stateful VMs, as long as appropriate checkpointing strategy and backup VMs are used to guarantee service continuity in the case of primary VM failure. Thus, our model can be extended and implemented in a PaaS environment, where th PaaS service providers handle both infrastructure and services. However, we note that our current mode is not directly applicable to big-data management on the cloud. For example, MapReduce proposed by Google and its open-source implementation Hadoop are the most popular big-data management frameworks today. By moving big data and its processing to cloud, data are stored in storage clouds, and computation is done with compute clouds. The Hadoop distributed file system handles large data sets on commodity servers. Data need to be copied from the location where they are stored to the instance on which the computation wil occur. This will incur data-transmission costs as wel as time delay, according to the size of the data trans mitted. Network structure and data-transfer latency may be some important factors to consider in such applica tions. In addition, when using a backup, there is cost involved in the frequency and volume of updates, which can be an important issue in service contract design, negotiation with the clients, and solution implementa tion. Because PaaS involves client-level applications, it is different from the primary goal of this research, as we do not model the operational details such as the datareplication structures and how the VMs are used from the client’s perspective. Extending our framework along the above-discussed dimensions is interesting and leads to important future research directions

## 10. Conclusion

In this research, we develop cost-effective solutions to the optimal management of virtual infrastructure resources in cloud service agreements by an integration of ideas from multiple disciplines. More specifically, this integration involves the following concepts: (i) dynamic resource optimization from Operations

Management; (ii) availability modelling based on sample path randomization techniques derived from the disciplines of Statistics and Machine Learning; and (iii) design of online algorithms drawn from Computer Science. We develop stochastic optimization models to support both periodic and aperiodic cloud infrastructure resourcemanagement strategies in a dynamic environment. We propose computationally efficient online algorithms that utilize their corresponding offline solutions to achieve both high computational performance and solution quality. We perform both competitive ratio analysis and expected value analysis to investigate the worst-case and average model performance, respectively. We further conduct comprehensive computational experiments and validate our model performance based on use cases constructed from Amazon EC2 price and service-credit data. Findings from this research provide practical decision support for cloud data center’s virtual resource management under flexible service agreements.

Under the periodic intervention policy, we develop dynamic optimization models to adjust the provision of backup VMs based on the observed system downtime at regular time intervals. We examine both a conservative strategy (the CL model) that is computationally expensive but minimizes the expected total operational cost and an aggressive strategy (the CE model) that is computationally less expensive but would only yield nearoptimal solutions. We find that the dynamic periodic intervention significantly outperforms its static, nointervention counterpart when service contracts are small-sized, require low availability, and demand low contract penalty in fault-tolerant systems. In addition, we recommend the use of the aggressive strategy for managing large service contracts with high availability in fault-prone systems with low penalty/provisioning cost ratios, as it produces a near-optimal solution to the conservative strategy, but is more computationally effective.

Under the aperiodic intervention strategies, we allow flexible timing of intervention and examine both single-intervention and multiple-intervention policies. We find that the flexible intervention time is more beneficial than the fixed time of intervention when the size of the service contract is small and availability is low in fault-tolerant systems. We also find that it might be sufficient to use a single intervention rather than multiple interventions for smallsized service contracts when the penalty/provisioning cost ratio is low and the availability is high.

In terms of computational performance, all our online algorithms have competitive ratios bounded by a factor of less than 2. It shows that the algorithms we developed are economical and can achieve good performance guarantee at the worst-case scenarios. In terms of solution quality, the potential advantage of flexible timing would diminish when the number of stages in periodic intervention increases. Our extensive computational experiments and Amazon use cases evaluation offer us empirical evidences of the effectiveness and robustness of our model performance under various system-level, service-level, and user-level parametric conditions. We also construct a decision tree to provide intervention policy recommendations and managerial guidelines with insights that facilitate cloud contract administrators to execute their service contracts cost-effectively. This study leads to several important, viable, and practical directions for future research. We outline some of these avenues in the following discussion.

First, in this study, we do not explicitly model the cost of intervention and cost of server repair. Presumably, the server-repair cost can be factored into the serverprovisioning cost. In this case, both the number of backup VMs and the intervention frequency would be reduced compared with our base model. Although the main insights obtained from this study would still be valid, specifically considering the costs of intervention and repair could affect the cost and benefit trade-offs in the service provisioning. It would be an interesting new dimension of investigation for the future.

Second, we assume the simpler architecture of powered-on without delay in the backup provision, where a set of backup VMs regularly capture the system states from the primaries and ensure continuity of service when primary VMs fail. An alternative consideration is the powered-off model where a single large backup that periodically captures the primary VM states is used as recovery and rollback mechanism in the case of VM failures. Although the powered-on without delay architecture is widely used in normal data-center operations, future research may consider the powered-off model, which is common in highly fault resilient and high-performance computing platforms.

Third, we focus on the exponential failures in deriving the transient downtime distribution, which represents constant random failure rates in the cloud infrastructure. Although exponential failures are common in practical data-center operations, servers in certain data centers could have changing failure rates in their life cycles. The case of decreasing failure rates over time can be modelled by using the Weibull distribution, which represents the infant mortality of servers. In this case, the servers more frequently fail during the early stages of their life cycles and attain stability over time. Similarly, the case of increasing failure rates over time can be modelled by using the Erlang distribution, which captures the aging condition of servers. In this case, servers tend to fail more often as they age. Different failure-rate distributions will affect the server downtime empirical distribution, which in turn would affect the cloud service provider’s backup VM provisioning decisions. Future research on Weibull and Erlang failures would generate their appropriate virtual resource-management strategies with richer practical insights.

In conclusion, IaaS cloud resource management is a complex issue. Performance metrics such as delay, bandwidth overhead, computation overhead, reliability, and security have to be taken into consideration in the design of resource-management schemes.

In addition, modeling the backup replication structure and user requirements at the PaaS level is an interesting future research direction.

## Appendix. Notation Table

## Acknowledgments

The authors sincerely thank the senior editor, the associate editor, and the reviewers for their many helpful suggestions, which greatly contributed to this research

<table><tr><td>Variable</td><td>Definition</td></tr><tr><td> $\alpha \in (0,1)$ </td><td>Required availability level (the uptime guarantee) specified in the SLA</td></tr><tr><td> $T$ </td><td>Contract period over which the uptime guarantee should be fulfilled</td></tr><tr><td> $B = (1 - \alpha)T$ </td><td>Total allowable downtime by SLA contract</td></tr><tr><td> $h$ </td><td>Provisioning cost per VM per unit of time</td></tr><tr><td> $\pi$ </td><td>SLA violation penalty per unit of time</td></tr><tr><td> $n$ </td><td>Number of primary VMs needed in the SLA contract</td></tr><tr><td> $k = \{1, 2, \ldots K\}$ </td><td>Number of backup VMs, where  $K$  is the maximum number of backups</td></tr><tr><td> $f_k(\tau), F_k(\tau)$ </td><td>The downtime density function and cumulative distribution function</td></tr><tr><td> $\phi_k(\tau), \Phi_k(\tau)$ </td><td>The normalized percentage of downtime density function and cumulative distribution function</td></tr><tr><td> $\eta_k$ </td><td>Mean percentage of downtime when the number of backup VMs is  $k$ </td></tr><tr><td>MTBF</td><td>Mean time between failures of primary and backup servers</td></tr><tr><td>MTTR</td><td>Mean time to repair of primary and backup servers</td></tr><tr><td> $\delta = \{1, 2, \ldots S\}$ </td><td>Index of stage, where there are total of  $S$  decision stages</td></tr><tr><td> $x_\delta$ </td><td>Total incurred downtime at the beginning of stage  $\delta$ </td></tr><tr><td> $k_\delta$ </td><td>Number of backup VMs at the beginning of stage  $\delta$ </td></tr><tr><td> $u_\delta \in [-k_\delta, K - k_\delta]$ </td><td>Backup VM adjustment decision in stage  $\delta$ </td></tr><tr><td> $\hat{v}(\tau, n, k)$ </td><td>Estimated probability distribution function of  $\tau$  downtime on [0,  $T$ ] for an  $(n, k)$  VM configuration</td></tr><tr><td> $\Delta t$ </td><td>Discretized time intervals to track downtime over [0,  $T$ ]</td></tr><tr><td> $\psi = \lceil \frac{T}{\Delta t} \rceil$ </td><td>The total number of discretization intervals over the contract period  $T$ </td></tr><tr><td> $D_W(k)$ </td><td>Random downtime in a stage with length  $W$  when the number of backup VMs is  $k$ </td></tr><tr><td> $d_W(k)$ </td><td>Expected downtime in a stage with length  $W$  when the number of backup VMs is  $k$ </td></tr><tr><td> $D_W(i, n, k)$ </td><td>Discretized downtime corresponding to  $i$  number of downtime intervals in a stage with length  $W$ </td></tr><tr><td> $p_W(i, n, k)$ </td><td>Discretized probability corresponding to  $i$  number of downtime intervals in a stage with length  $W$ </td></tr><tr><td> $C(k_1, k_2, t)$ </td><td>Cost function of SISL strategy with the number of backup VM provisions before and after intervention as  $(k_1, k_2)$  and the intervention time  $t$ </td></tr><tr><td> $J_\delta(x_\delta, k_\delta)$ </td><td>Cost-to-go function in stage  $\delta$  of Problem CL, which is the minimum expected total cost from stage  $\delta$  to the end of stage  $S$ </td></tr><tr><td> $G_\delta(k_\delta)$ </td><td>Cost-to-go function in stage  $\delta$  of Problem CE, which is the minimum expected total cost from stage  $\delta$  to the end of stage  $S$ </td></tr><tr><td> $H_\delta(x_\delta, k_\delta)$ </td><td>Cost-to-go function in stage  $\delta$  of Problem MSL, which is the minimum expected total cost from stage  $\delta$  to the end of stage  $S$ </td></tr><tr><td> $\Omega_\delta(k_\delta)$ </td><td>Total expected downtime from state  $k_\delta$  of stage  $\delta$  till the end of stage  $S$  along the path corresponding to  $G_\delta(k_\delta)$ </td></tr><tr><td> $C_\Delta$ </td><td>Accrued total realized downtime from time 0 to stage  $\Delta$ </td></tr><tr><td> $\hat{X}_\Delta$ </td><td>Observed actual downtime in stage  $\Delta$ </td></tr><tr><td> $\hat{B}$ </td><td>Allowable total downtime at the beginning of stage  $\Delta$ </td></tr><tr><td> $p$ </td><td>Monthly price of an instance (VM)</td></tr><tr><td> $\bar{p} = p/\rho_{max}$ </td><td>Selling price per VM per unit time interval</td></tr></table>

Note. This notation table includes all variables defined and used in the main paper and the online supplement.

## Endnotes

<sup>1</sup> Dimension Data Cloud Terms of Services and Related Service Levels Descriptions: https://www.dimensiondata.com/en-US/Solutions/ Cloud/Pages/Service-level-agreement-of-Public-IaaS.aspx.

<sup>2</sup> The Essential Guide—Infrastructure as a Service: http:// searchcloudcomputing.techtarget.com/definition/Infrastructure-as -a-Service-IaaS.

<sup>3</sup> Virtual Machine Checkpoints: https://technet.microsoft.com/en -us/library/bb740891.aspx.

<sup>4</sup> The notion of conservatism used here refers to backup VM management; hence, conservative backup VM management is equivalent to aggressive penalty management, and aggressive backup VM management corresponds to conservative penalty management.

<sup>5</sup> In general, the failure and recovery processes of fault-tolerant systems are more predictable than the fault-prone system.

<sup>6</sup> Amazon EC2 service offerings and pricing: https://aws.amazon .com/ec2/pricing/.

<sup>7</sup> Amazon EC2 dedicated hosts pricing: https://aws.amazon.com/ ec2/dedicated-hosts/pricing/.

## References

Ahmad RW, Gani A, Hamid SH, Shiraz M, Yousafzai A, Xia F (2015) A survey on virtual machine migration and server consolidation frameworks for cloud data centers. J. Network Comput. Appl. 52: 11–25.

Bellman R (1957) Dynamic Programming (Princeton University Press, Princeton, NJ).

Bertsekas DP (1995) Dynamic Programming and Optimal Control, vol. 1, 3rd ed. (Athena Scientific, Belmont, MA).

Bilal K, Malik SUR, Khan SU, Zomaya AY (2014) Trends and chal lenges in cloud datacenters. IEEE Cloud Comput. 1(1):10–20.

Bobroff N, Kochut A, Beaty K (2007) Dynamic placement of virtual machines for managing SLA violations. IEEE Internat. Sympos. Integrated Network Management (IEEE, Piscataway, NJ), 119–128.

Bruneo D (2014) A stochastic model to investigate data center performance and QoS in IaaS cloud computing systems. IEEE Trans. Parallel Distributed Systems 25(3):560–569.

Chase J, Niyato D (2017) Joint optimization of resource provisioning in cloud computing. IEEE Trans. Services Comput. 10(3): 396–409.

Cheng HK, Li Z, Naranjo A (2016) Research note: Cloud computing spot pricing dynamics: Latency and limits to arbitrage. Inform. Systems Res. 27(1):145–165.

Chowdhury NMMK, Boutaba R (2010) A survey of network virtualization. Comput. Networks 54(5):862–876.

Cloud Standards Customer Council (2017) Practical Guide to Cloud Computing (version 3.0), Accessed March 6, 2018, http://www .cloud-council.org/deliverables/CSCC-Practical-Guide-to-Cloud -Computing.pdf.

Colman E (2013) When to Use SaaS, PaaS, and IaaS? Computenext.com (August 27), https://www.computenext.com/blog/when-to-use -saas-paas-and-iaas/.

Das S, Du AY, Gopal R, Ramesh R (2011) Risk management and optimal pricing in online storage grids. Inform. Systems Res. 22(4): 756–773.

Dey D, Fan M, Zhang C (2010) Design and analysis of contracts for software outsourcing. Inform. Systems Res. 21(1):93–114.

Du AY, Das S, Yang Z, Qiao C, Ramesh R (2015) Predicting transient downtime in virtual server systems: An efficient sample path randomization approach. IEEE Trans. Comput. 64(12): 3541-3554

Fu S (2010) Failure-aware resource management for high-availability computing clusters with distributed virtual machines. J. Parallel Distributed Comput. 70(4):384–393.

Gill P, Jain N, Nagappan N (2011) Understanding network failures in data centers: Measurement, analysis, and implications. Proc. ACM SIGCOMM Conf. (ACM, New York), 350–361.

Goiri I, Julia F, Guitart J, Torres J (2010) Checkpoint-based fault tolerant infrastructure for virtualized service providers. IEEE Network Oper. Management Sympos. (NOMS) (IEEE, Piscataway, NJ), 455–462.

Goudarzi H, Ghasemazar M, Pedram M (2012) SLA-based optimi zation of power and migration cost in cloud computing. Proc. 12th IEEE/ACM Internat. Sympos. Cluster Cloud Grid Comput. (CCGrid) (IEEE, Piscataway, NJ), 172–179

Jaillet P, Wagner MR (2012) Online Optimization (Springer, New York)

Johar M, Mookerjee V, Sarkar S (2014) Selling vs profiling: optimizing the offer set in web-based personalization. Inform. Systems Res. 25(2):285–306.

Kauffman RJ, Ma D, Shang R, Huang J, Yang Y (2014) On the financification of cloud computing: An agenda for pricing and service delivery mechanism design research. Internat. J. Cloud Comput. 2(1):1–14.

Laalaoui Y, Al-Omari J (2018) A planning approach for reassigning virtual machines in IaaS clouds. IEEE Trans. Cloud Comput., ePub ahead of print April 13, https://doi.org/10.1109/ TCC.2018.2826548.

Liu D, Sarkar S, Sriskandarajah C (2010) Resource allocation policies for personalization in content delivery sites. Inform. Systems Res. 21(2):227–248.

Liu J, Zhang Y, Zhou Y, Zhang D (2015) Aggressive resource provisioning for ensuring QoS in virtualized environments. IEEE Trans. Cloud Comput. 3(2):119–131.

Lu P, Ravindran B, Kim C (2012) VPC: Scalable, low downtime checkpointing for virtual clusters. Proc. IEEE 24th Internat. Sympos. Comput. Architecture High Performance Comput. (SBAC-PAD) (IEEE, Piscataway, NJ), 203–210.

Mistry S, Bouguettaya A, Dong H, Qin AK (2018) Metaheuristic optimization for long-term IaaS service composition. IEEE Trans. Services Comput. 11(1):131–143.

Qiu W, Zheng Z, Wang X, Yang X, Lyu MR (2014) Reliability-based design optimization for cloud migration. IEEE Trans. Services Comput. 7(2):223–236.

Ran Y, Yang J, Zhang S, Xi H (2017) Dynamic IaaS computing resource provisioning strategy with QoS constraint. IEEE Trans. Services Comput. 10(2):190–202.

Sen S, Raghu TS, Vinze A (2009) Demand heterogeneity in IT infrastructure services: Modeling and evaluation of a dynamic approach to defining service levels. Inform. Systems Res. 20(2): 258–276.

Shabeera TP, Kumar, SM, Salam SM, Krishnan KM (2017) Optimizing VM allocation and data placement for data-intensive applica tions in cloud using ACO metaheuristic algorithm. Engrg. Sci. Tech. 20(2):616–628.

Sieke MA, Seifert RW, Thonemann UW (2012) Designing service level contracts for supply chain coordination. Production Oper. Management 21(4):698–714.

Silva Filho MC, Monteiro CC, Inacio PR, Freire MM (2018) Approaches´ for optimizing virtual machine placement and migration in cloud environments: A survey. J. Parallel Distributed Comput. 111:222-250.

Singh S, Chana I, Buyya R (2017) STAR: SLA-aware autonomic management of cloud resources. IEEE Trans. Cloud Comput., ePub ahead of print January 5, https://doi.org/10.1109/TCC.2017.2648788.

Sleator DD, Tarjan RE (1985) Amortized efficiency of list update and paging rules. Commun. ACM 28(2):202–208.

Wang X, Du Z, Chen Y, Li S (2008) Virtualization-based autonomic resource management for multi-tier web applications in shared data center. J. Systems Software 81(9):1591–1608.

Wu L, Garg SK, Buyya R (2011) SLA-based resource allocation for software as a service provider (SaaS) in cloud computing environments. Proc. 11th IEEE/ACM Internat. Sympos. Cluster Cloud Grid Computing (CCGrid) (IEEE, Piscataway, NJ), 195–204.

Xu J, Tang J, Kwiat K, Zhang W, Xue G (2012) Survivable virtual infrastructure mapping in virtualized data centers. Proc. IEEE 5th Internat. Conf. Cloud Comput. (IEEE, Piscataway, NJ), 196–203.

Yuan S, Das S, Ramesh R, Qiao C (2018) Service agreement trifecta: Backup resources, price and penalty in the availability-aware cloud. Inform. Systems Res. 29(4):947–964.

Zhao L, Sakr S, Liu A (2015) A framework for consumer-centric SLA management of cloud-hosted databases. IEEE Trans. Services Comput. 8(4):534–549.

Zhou A, Wang S, Cheng B, Zheng Z, Yang F, Chang RN, Lyu MR, Buyya R (2017) Cloud service reliability enhancement via virtual machine placement optimization. IEEE Trans. Services Comput. 10(6):902–913.

## CORRECTION

In this article, “Optimal Management of Virtual Infrastructures Under Flexible Cloud Service Agreements” by Zhiling Guo, Jin Li, and Ram Ramesh (first published in Articles in Advance, December 10, 2019, Information Systems Research, DOI: 10.1287/isre.2019.0871), the format of the equations in Section 6.1 has been modified to improve readability, and a typo has been corrected in the integral of one of the equations in the text following Proposition 4 on page 1435.
